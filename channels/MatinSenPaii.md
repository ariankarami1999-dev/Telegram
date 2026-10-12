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
<img src="https://cdn1.telesco.pe/file/JQqwHaNZFhj7aEmLC0hFMa6rK2MZMZqZHcML4T0NNyqsJ7Dkr4MGeS1Jk_cb0QLyqZnwCO0RyLaXbfAQ0KkWUuONxXzJCXZpIIhpp7KQ_c9-jieouMhU19hDc8C8HZ_UjF1EL9dmIYzASRkO1iU5IEGkZsEKPrFE0LP7srTzDNEONMTTJM4DP5zSz8TUesgC-igwB77308XkMdfcGoUzede1Myp1enVxL-Jcpxoe2_f9d8Uf92jWcnEr38SCkNZp4aUMiIvrAN7YAL43A2TTil1dnKio-Ieekiuv6TkOS9l0YBCQhn8nE0jQ-vJCxtqHEzoIFg1nniMBMaS7Jzm_SQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 04:57:01</div>
<hr>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRnKBhRR5SgDWoJm0GupJrqrJH9FzCUxDbA-vEwbGnvTGziWXherri6cmfshLA_SwfZGj-FY5IS3GralYHUW-ddHGbWLjdFEeAb9L2pWc6sJ8tVPsTGvSghaRf9DLAn6lcKiQW-4vhTFyCUxs-CScz8ezIDibBGD1BqzAKC6AKDXRpm3BDrlzWYIqiWr-RTM4rhanNIyxb611GZH57zWhFYUU2FYqNTfJlQZWh7XSq0noCGXq5EzVYNc7fSSggm487NaUavpAsPTigZ5SuwmDy-H3fuTmsPWksYFENvPAMgvWFpwnfuHi6wp0LrBGktSEtJXI7kIPHN9LUq6bx3iJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله ClickFix با طعم Claude؛ تبلیغات گوگل آلوده شد
هکرها دارن از ریدایرکت‌های واقعی نتایج جست‌وجوی بینگ به‌عنوان لینک کلیک توی تبلیغات گوگل سوءاستفاده می‌کنن تا کاربرها رو به نصب‌کننده‌های جعلی Claude بکشونن که حمله ClickFix تحویل می‌ده. ترفندش اینه که لینک تبلیغ ظاهرا معتبره ولی به صفحه مخرب می‌رسه و با انجام دادن پروسه‌هاش، دستگاهتون آلوده می‌شه. کلاد رو فقط از سایت رسمیش دانلود کنید.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/MatinSenPaii/5563" target="_blank">📅 22:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مدل‌های زبانی بایتی؛ بدون نیاز به توکنایزر
یه مقاله‌ی تازه ادعا می‌کنه ترنسفورمرهای معمولی می‌تونن مستقیم روی بایت خام کار کنن و با بزرگ‌تر شدن پارامترها حتی از مدل‌های ساب‌وُردی بهتر بشن. باور رایج این بود که دنباله‌های بایتی چون ۴ برابر طولانی‌ترن(در مقابل بیت)، ناکارآمدن؛ نویسنده‌ها‌ی مقاله می‌گن این طول اضافه با مقیاس جبران می‌شه و انتزاع‌های زبانی خودشون درون مدل شکل می‌گیرن(که به نظرم اینجا باتل‌نک قضیه‌ست و باید به شدت بره زیر تست). به نظرم مقاله‌ی جالبیه. وقت کردید بخونیدش
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/MatinSenPaii/5562" target="_blank">📅 21:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nhM4dMpUN0-otHNeGcZFHTs103dpRDhpM00Lfs3-R-sEEeYborQa-7rdvd7C4Qldv0TExZ6baf5Cyf-cUUNWawbJGY1TqgJ3vOsVo-V0IaYGdYm5C6HukuJ-QFsf1dtQc85ubnJ3S0eNzdukmcz9VtaKtC2UKf-LppA9zY69vRCXea9a2EtsQQXfokXPgz6J572-wGZNcl_B2phLBuRnl6dJavTd1pgcM4lRaquczE02wZKd9LY63IzNezfi7APF4RcL4OXei6bjZjlPDp2xXYxOuK1Ox_lCxuwNSCqNCT8-ZSuTVpZgDsiX3eT3rvQLNCKsWRFHi2xK8X6cTv_WGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل اوپن‌ویت پرپلکسی از Jev جلو زد
یه ارزیابی مستقل روی ۶۶۹ کیس پزشکی می‌گه مدل pplx-decider-v1.1-27b پرپلکسی تعداد ۶۴۳ جواب درست گرفته در برابر ۶۲۸ تای Jev، با ۴۲٪ هزینه کمتر برای هر تصمیم(که فوق‌العادست. موندم مدل مایکروسافت چند میگیره
😂
). قیمتش ۰.۰۲ دلار به‌ازای هر میلیون توکن ورودیه، و خروجی رایگانه، کانتکست ۲۵۰ هزارتایی داره و روی OpenRouter در دسترسه همین الان. صدر جدول Decision Index هاگینگ فیس هم مال خودش شده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5561" target="_blank">📅 20:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pQyhDHjgtcV0GsnxNPRQpL_Yo3G579dP7pQm3-WlJwv_HS0upIjiMU7Uj9c6yKHqzzIUBzSStWtQJA0sxr3x5SwvcoYTs5uxqyUb8Cw45cy8ntxHh1jjJBziDS-b0c6l06sOz1SDaEtk4MIPTH-8D4cQ17ExSz687n9Y4N02yv7Hdbxai1mPruOfz9oigqkpDsc5LLtKc8X582glDd3cPxIPhw0JP-FE-Gqc7LXVCBphY4ktx2z9ibfyQTCHh1QpFxusmzoJ6hDbLx-lpglMXsvlPGsD5Mn7OjmVO7SpfxgC96tymx5p6kB0QEnIeO549TtWGy7eq8BitD-J5HS5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت Decision-1؛ مدلی که فقط تصمیم می‌گیره(نسخه تنظیم بازار Jev)
مایکروسافت یه مدل تصمیم‌گیری (decision-scoring) معرفی کرده برای کارهایی مثل روتینگ، دسته‌بندی، اولویت‌بندی و کنترل ورک‌فلو؛ یعنی به‌جای تولید متن، مستقیم خروجی ساخت‌یافته می‌ده که نرم‌افزار بتونه باهاش کار کنه. ادعاشون: بالاترین دقت بین ۳۶ بنچمارک با نزدیک ۱۵۰ هزار سؤال، و سرعت ۴.۵ برابر نزدیک‌ترین رقیب و ۳۵ برابر GPT-6 Sol(چرا باید با Sol مقایسه‌اش کنن؟
👍
). توی Foundry اومده و به‌زودی روی OpenRouter هم میاد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/5560" target="_blank">📅 20:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کارزاری ایرانی با ChatGPT مقاله‌ای جعلی در رسانه‌های واقعی آمریکا به جا گذاشت
گزارش واشنگتن‌پست می‌گه یه کارزار منتسب به ایران با کمک ChatGPT مقاله‌های تولیدشده با AI رو تو رسانه‌های واقعی آمریکا جا کرده. و این نشون میده عملیات نفوذ رسانه‌ای با AI چقدر ارزون و تر تمیز شده.
اینجا هم به دلایل مشخص نمی‌تونم بازش کنم جزئیات قضیه رو
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/MatinSenPaii/5559" target="_blank">📅 19:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QujEHxg9Urfqt3nLSWEU51rrhtG0v_45ZMb5x6iDrP_xpsv3zqi9Uhm_9ePjnD8_o9k1xdYbo3QO8v6lt3q2nADHVLqstIwNUwl1MnVRNdVTk374W3-hooqLd1maYL4Uu9cbmEgTlU6-obNiiFTqkW2a036J5xs_oJParPrHWYQTdbCu3pLKr0AUs1yxsoYXyzGdnzTZlXl1u97z1Fw1i0BFcw8Df5oH1e1cKSqIrOTAbVZs1PkaKw9A-9FJW_KDXjRrvaNkFLbjZBjlonn1yg25B0l0OnqD0bOi0Nh91OHZ69c6tAQSFivGqMTMunjXlglaCfqD5YX0riwJb-6Oyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه‌ای که یه زمانی فورک Redis بود و الان انگار وارد رقابت جد شده: ValKey
پروژه‌ی Valkey که دو سال پیش به‌عنوان فورک Redis شروع شد حالا ۱۲ تا Maintainer اصلی و ۹ عضو کمیته از شرکت‌های مختلف داره؛ تروپوت بهتر، کلاستر قوی‌تر و برنامه برای رپلیکیشن Synchronous و ذخیره‌سازی چندسطحی. تمرکز روی امنیت و اتومیشن هم جدیه و داره از کاربرد «صرفا کش» ردیسی، فاصله می‌گیره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/5558" target="_blank">📅 18:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PnHBUwOYPjcv2IlAiHsXr9tixyaUIBVKjlIomvoOLTimBJFijNbLrYogkc2TWzslkCPg2N2PbswqGekXkeMCPDmqOwjsiGUaZDqwjM-CT0WtJ9fFMlULFJUFAetdj5ridUafFbqX0ajEZJWSU17mShXJbYDnHmwo5UFsKT_rz9Wr2fbuifhq8iCNONSJ7YxLwbBsEz-vFipBDmwGcwzYXyaWEmrPhzLSWuZF7RD6Juosja24TfqmuKRt8bFDFXjJ89T7iwD4cw8ztA_Hy61fsY4rajcH-7qbqmEFa3ib6XA9Lsa4eeEKgH19xh6EJOdsNT04EcI3R40hjDY03pVY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من و ایده‌های استارتاپی خفنم که قرار بود باهاشون پول در بیارم توی ایران:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/5557" target="_blank">📅 17:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تیکه گمشده‌ی ارور هندلینگ توی Rust
یه رایت‌آپ خوب که می‌گه درد Rust انتخاب بین تایپ دقیق پر از بایلرپولیت مبهمه؛ راه‌حلش کتابخونه eros با «مجموعه خطا» هست: به‌جای تعریف enum تازه، می‌نویسیم (io::Error, ParseIntError) و کامپایلر چک می‌کنه خطای اضافه propagate نشه. با widen هم ترکیب می‌شن و کانتکست می‌گیرن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/5556" target="_blank">📅 15:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vwCCeajXZ7RLkFbkCa3gVlomTaMGweapESVAg_aQpkVkqR9kVEhEujIXcuv4uea9pld5K5AP1y0CwDqNL2y94ZAXExe06gyj_aSORJcS4cn_UOwpR1wA0xFD822St2l2Sf9X41kDzS5KOB_gEkw-AFXlpzQrfhxeKVtIPL2OnYNojys817uiVP09fg8BYUrsbnZ5Ki-5TXU8f8jOOtM39zX2JrtYSEnfY9LMVfaluiab7An3gBG-L8DK0LdkASQImQH6uoQ5F8-17vZNGnQiJTzgAQBrWutMdbsAUsOGYyVyaNP9-im_GKvhtcOw5g3_mU4Pl3ZHgHS4WjHrYl16pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدلی که وجود نداشت، پس خودت با ML Intern بسازش
یاوراج شارما تعریف می‌کنه دنبال نسخه کوچیک بازنویسی شده‌ی Qwen-Image 2.1 بوده (نسخه رسمی ۹ میلیارد پارامتری که ۲۰ گیگ رم می‌خواد) و با ایجنت ML Intern یه نسخه ۰.۸ میلیاردی ساخته که روی CPU اجرا می‌شه؛ خروجی معتبر ۹۹.۷٪ و کل هزینه محاسبات ۱۶ دلار. تو چند روز شش مدل دیگه هم همین‌جوری ساخته و هر هفت پرامپت رو تو گیت‌هاب گذاشته.
به نظرم جالبه ببینیم برای GLM 5.3 Flash چیکارا میشه کرد
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5555" target="_blank">📅 13:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWMjTqi4QzGzGfd6Q7Qvf-9GbtXueywOVRq0nJP3gfqIqxbe3kUg0MMVMrofZ-vcLBxyEWr2U5vqDGBHbjD_KyVgIeJkIO0bSlDtfklYSKfi1dFPejXeFuXFgmzR0DyjRxZUzarGd0pF6V4UYUUq6PHLno0bdFGvnKo2TLjAlTmk-rbIX4NvMA143sWyt7I_QH3fBhHGEpndnVtSuNINHQegEmiV-F0rGkiqKu5GIDxEEJP8-aQO2AkV2hG-XrPRMH3UxK-aU7Xz1SI7FKc2VA9adBr-__T_dYr-IzovYIuk5yVULUkvtusj9rZ6wvehFJpPDYy0TKion0gWElsdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داده‌های زیستی آماده برای AI
ابتکار Virtual Biology شبکه‌ی Biohub گسترش پیدا کرده؛ تعهد جهانی ۱.۸ میلیارد دلاری برای تولید داده‌ی زیستی باز و آماده AI تا بشه مدل‌های پیش‌بینی‌کننده زیست‌شناسی ساخت. اگر کسی از شما بچه‌ها توی حوزه‌ی پزشکی یا بیوتکنولوژی کار می‌کنه، دیتاست‌های Open این پروژه ارزش دنبال کردن داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5554" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حمله به بانک‌های کره جنوبی با کمک Claude
یه هکر ۲۶ ساله‌ی چینی مظنون به سرقت داده‌های بانکی کره جنوبیه و شواهد نشون می‌ده از Claude برای پیدا کردن کانال‌های تلگرامی فروش اطلاعات سرقت‌شده استفاده کرده. یه نمونه‌ی تازه از سوءاستفاده از ایجنت‌های AI برای جرایم سایبری که زنگ خطر رو برای دولت‌ها به صدا درمیاره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5553" target="_blank">📅 10:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مدل تصمیم‌گیر خودتون رو بسازید
یه آموزش عملی و تعاملی توضیح می‌ده مدل‌های تصمیم (System One مثل Jev) چطور به‌جای تولید توکن‌به‌توکن، با یه پاس و ماسک کردن وکب فقط از بین گزینه‌های ثابت مثل A تا E انتخاب می‌کنن و احتمال کالیبره‌شده برمی‌گردونن. نویسنده با Qwen3-1.7B و transformers نشون می‌ده چطور همین رفتار رو خودتون شبیه‌سازی کنید. به نظرم خیلی بامزست و ارزش مطالعه داره این مقاله:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5552" target="_blank">📅 09:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5551">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YKVJNVsB-AskMVhesVObOOUJbvD3sjyBeFyUKrnXG-XRPtxu4sik8KCaC-hqWJUW83VFRJxnXM5hh60hIovJ9NynE_pS7SxERbFX8zlRTMGE0uJJOFpJ3EmqwSmTDJ8_I82p1PKFIiHkJkh0wGVk5JFOdtJNcu4CXzJ69M7K0s2f9nE0PkyKN-ArwTBs03Op72dILXyNskwDMbS7P4lJguyfuPV__6YeRcqnjTRuycuIWFjOpSQQG4phK1VKkNxfINGToZ5u7ONT5lyLT-N3B33M92beabudpVkNaZgFrpPMlAvGWgcb1Fvx1cJP3AblvYDfAP2SPCJIG5W8zja-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفیس اوپن‌سورس با Rust؛ کدنویسی با Claude
استارتاپ ArtCraft نسخه‌های مشابه Word و Excel و PowerPoint رو به لاین‌آپ اوپن‌سورسش اضافه کرده؛ یه جور بازنویسی آفیس مایکروسافت با Rust که بخش زیادی از کدنویسیش رو Claude انجام داده. هنوز برای پروداکشن آماده نیست(که نکته‌ی مهمیه و توی اون اپ‌های جایگزین فوتوشاپ هم دیدیم که به نظرم به زودی آماده‌ی پروداکشن میشن).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5551" target="_blank">📅 08:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">طی امروز سعی میکنم اخبار سه روز اخیر رو پوشش بدم واستون</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5550" target="_blank">📅 08:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سلام
من از غیبت برگشتم
👍</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5549" target="_blank">📅 08:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!  آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست،…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5548" target="_blank">📅 13:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!
آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست، ولی ارزش امتحان کردن رو داره.
🔗
getartcraft.com/apps
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5547" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l8UC61IYfLyUUhL_IFCJG0b988TqzKk-VEb9QGvbPwhtkdq4IYAV9J2UBEBoJrtdHDpp7bU3FMe2srPYkUgga0r2bNg1i7zv1yVJ8u-v1u54zrD0N-F3UH5o4VqAE4sC8_LcFjfA0tDeQHKunIasc1m5ua308C5aI1XluvevK190Fqv8bGLOW4Wvwy1G4qi3_LNID_0Dy6A_CCL5VOCAw_Q3NmegrKvHZNFxRvTfIR6ZeqsVRcpTowMkyTaeRs8R3yLQXAVZPV9h9B4fhDUhdTnDDPT-Lag_CePrGh6mMvA9RfPxYjFG3w9cAdLIxcJkh5luROTGFtUVkBT_bDHHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
ببینید چی برگشته:)) Haiku 5.5
خفن‌تر از GPT 6 Luna</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5546" target="_blank">📅 09:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یادم رفته بود بگم. من از اینجا گرفتم. تا الان مشکلی نداشت اکانتا.  توی رباتش بخش هوش مصنوعی، دوباره هوش مصنوعی یه کم دسته‌بندیاش درب و داغانه
👍
اما کار میکنه @OrcaSubBot</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5545" target="_blank">📅 08:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNBalkSbECylGmklPaKsl5TLjvEBshhAGsH140fAej2-feQPJWYq9m0PSndsfbEFEHm1y76BQTyw1UPOEg92uhoZZe8Fqcr8Tt8PnffxRAyIn50--fIctXWsQDNAPE9WH7-21f0hwy0-1Yw55HK-ldFfs_NxUfPqFFxQovE9KlFxaZz0LYcFW4AAknTrx73fBUvRLswcnQ4kW88djXvCGKRQYCYHaAThnv1JEKIwwXddjQPuoiHFhvCZpbNPMxICOBqQ1MWPh8g7FUuaxtjULIIOfJC1zjYsCikuuFtg4hbnpk2UfE_rqg23OYvPJxyYEd3-fbkKD5dKyB2UbqqwJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابط بصری جدید ChatGPT
گویا اوپن‌ای‌آی داره یه رابط جدید برای ChatGPT میده که جواب‌ها رو خیلی بصری‌تر و تعاملی می‌کنه؛ یعنی به‌جای متن خشک، ویژوال تعاملی می‌بینیم و برای کسایی که هر روز با ChatGPT کار می‌کنن(مثل خودم برای چت روزمره یا سؤالهایی که حین یادگیری Rust می‌پرسم) تجربه‌شون حسابی قراره بهتر بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5544" target="_blank">📅 08:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5543" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCoreForge</strong></div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!
نسخهٔ مک
ForgeCore
از ریویو اپل گذشت و حالا روی
TestFlight
در دسترسه.
🚀
📥
دانلود و نصب:
https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید:
اول اپ رو کامل
پاک کنید
، بعد از لینک بالا دوباره نصبش کنید. بدون این کار ممکنه نسخهٔ جدید درست بالا نیاد.
ForgeCore چیه؟
یه کلاینت شبکه برای وصل شدن به سرورها و کانفیگ‌های پروکسی/VPN خودتون:
- افزودن کانفیگ با
لینک اشتراک
،
QR کد
یا
لینک تکی
- تست
پینگ و در دسترس بودن
همهٔ کانفیگ‌ها
- پشتیبانی از پروتکل‌های متنوع
- اشتراک‌گذاری اتصال روی
شبکهٔ محلی و Personal Hotspot
برای نصب کافیه اپ
TestFlight
رو از App Store بگیرید و لینک بالا رو باز کنید.
🐞
اگه کرش یا مشکلی تو اتصال دیدید، همین‌جا بگید تا سریع درست بشه.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5542" target="_blank">📅 22:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwYG-98rPk0-6WZJ0PE0YTmP1S596M5H0GT5sQeKNRNcQB1xLcEyHl_LW126MY4_b2exjUr7hsM6jtiXzl-6uweS94pegqdqnnRb0_nlfSFHtju2om78OxQasW_HJ2AZoB5Qky6h5WEE-0EAAbJUr8hWZYNJRrxLxnXhcv0YkOHe5LdNnEpmVSiKmFrbUBsg6dVTxB4O0Hyaldg50djMNU4EQLXrkB0BfI9tFW0dD4DuhzzD6Qj3qcs3dsu1sacU6RxmiwjEDjRrzYA6qkKAghF1DBI9QTi9_4o4Mpp0ldMTjY96cFGzRLne7sZvBO84lxhpBw-mzIcJV_P_QdP27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5541" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی
و فکر میکنم با ویدئوی بعدی
یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5540" target="_blank">📅 15:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم گفتم به یکی از بچه‌ها دوتا اکانت بهم بده توی پنج دقیقه بهم داد:) اصلا باورم نمیشه و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد هرچند خب استفاده‌ی دیگه‌ای داره کلا.  اگر که اوکی بودش و نپرید و اینها،…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5539" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5538" target="_blank">📅 15:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">Math lovers, check this out:
https://github.com/openai/math</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5537" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!  تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5536" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135826faf3.mp4?token=ACft685jlWpDDPgv-ARIFRiUqw004BhO7ziDlx-QK_KfX_vMHKPNo-ZLwd9QSZy4ylR00Yq8DjO2NGj0Sa0VvnAr6aSgJ11CwO0q6Fs3e0DoR0jVmi9W04E-N_UFRUI9kqYZv7Y0bNp6ngNDSc9VFuUcLYcdf2A5A4JFr3aMCxx4ikDpFzbFOR67mxqlvZwISA2YboCwmTm0HjEygZgLfLOzrCqzv_nM8Rs7lb19mY5P3v2Cl_SnUD6vMsjEt6qK38GxP1J1oU-19U2an1bYLtWzcGWPL3mbHh7OR7pLqSu69RRdR990rrBsk0vlJo1XjMsl4g0aubfAttPXVkGO2H853ThgzlXZV_x_ChhiOTHf2YrBcYcEmgdRhUV7P_3rkzPuvoyVQB9XwJ6q6-mnSgQ00ggqSvJgyEreLXeHif_I8Hx0IjNljL5MBds4YYXIVgFwGtWYWSO7E1u9tInT9p2Zs1XwGlDIJrxo76QPAnXhRA083x6krL1NAInn9njoUhVEoRtZeVCJJUK2gyWA6fCbORVGZtiS_eXuIUN8ARsP6OMeKgAg_1j5ZkN-Y6cIB1j1zEl325WfxKCpJDDJw3YU4inlhtW02KmM62SUToCR48fic1ObdzlMs9Dncs7fBwe0mob3G7F4Lo1g3f5mJ9_tYGg0A5wyXyAMR_yRKVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135826faf3.mp4?token=ACft685jlWpDDPgv-ARIFRiUqw004BhO7ziDlx-QK_KfX_vMHKPNo-ZLwd9QSZy4ylR00Yq8DjO2NGj0Sa0VvnAr6aSgJ11CwO0q6Fs3e0DoR0jVmi9W04E-N_UFRUI9kqYZv7Y0bNp6ngNDSc9VFuUcLYcdf2A5A4JFr3aMCxx4ikDpFzbFOR67mxqlvZwISA2YboCwmTm0HjEygZgLfLOzrCqzv_nM8Rs7lb19mY5P3v2Cl_SnUD6vMsjEt6qK38GxP1J1oU-19U2an1bYLtWzcGWPL3mbHh7OR7pLqSu69RRdR990rrBsk0vlJo1XjMsl4g0aubfAttPXVkGO2H853ThgzlXZV_x_ChhiOTHf2YrBcYcEmgdRhUV7P_3rkzPuvoyVQB9XwJ6q6-mnSgQ00ggqSvJgyEreLXeHif_I8Hx0IjNljL5MBds4YYXIVgFwGtWYWSO7E1u9tInT9p2Zs1XwGlDIJrxo76QPAnXhRA083x6krL1NAInn9njoUhVEoRtZeVCJJUK2gyWA6fCbORVGZtiS_eXuIUN8ARsP6OMeKgAg_1j5ZkN-Y6cIB1j1zEl325WfxKCpJDDJw3YU4inlhtW02KmM62SUToCR48fic1ObdzlMs9Dncs7fBwe0mob3G7F4Lo1g3f5mJ9_tYGg0A5wyXyAMR_yRKVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!
تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه فارسی بهینه‌اش کردم و نتیجه این ۸ تا skill شده که اُپن سورسه و می‌تونید برای ساخت ویدیو استفاده کنید :)
https://github.com/atmirrr/persian-motion-director
✍️
AmirAnonn</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5535" target="_blank">📅 11:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کم کم دارم فکر می‌کنم یه نسخه از خودم کلون کنم بذارم هرمس جام کار کنه
🍿</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5534" target="_blank">📅 00:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJqV3GjjD0JRVXTQLsuX2vVaBs-9ofmeSd2P4PWXGs3upGTdFOm3x6WFlYpH6ZvDn78GMz9dsHg82999ToJjUhjz29krRPiljnG7g3RwPnAIIWVcLQKSufwdcg8O0QJYGI2s78u9W4B7_iEZQqMqITcI31iOMpu5XJ8g18N6EHmQcPvzr4WkvOJ0g4IBrzcZ2cXA2QdOqH4UcvQuVJezpDwKHy_sJ_dTr0oJzON_oDyveOO2fWZlOk9VPHabAjD9CoTXvq0KYmzSHYg8ubTksK_l9mpxZtaPcurM7yUFwujQulBYlr_Sn5jfsnrYyxJVKrPGpmyEA0zBa9FSTP6SQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن OpenChamber؛ یه اپ موبایل جمع‌وجور برای مدیریت سشن opencode
نویسنده این پست توی ردیت گفته بود اولش فکر می‌کرده پست‌های OpenChamber فیکه، بعد از تست کردنش می‌گه در عمل، به طرز عجیبی خوبه؛ جایگزین opencode نیست و همچنان opencode رو روی سرورش ران می‌کنه، فقط با OpenChamber از روی گوشی به‌صورت نیتیو به همون سرور وصل می‌شه و تسک می‌ده. برای کسی که opencode رو ریموت اجرا می‌کنه و نیاز به اپ موبایل داره، تجربه‌ی تر و تمیزی داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5533" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B6bWyh7HP7nYb-0_nCyuPKrTByKa0sy7-Pba_Yjhhg2bPl_p0JQx-Juu1vNSBntzyEEGDj81jRca9YGF2v0hpyO0x2gTEh8jfkdvWVEP_Jy2p9Wdlyei1IOGHcRsx7WbIdgbv1KUoDdmtrX5_6ofuH-rYp61r6QXkmWV1Rb1tzqxA-zK-lP0e8RnpvqQdXux_wo5wJIh_fXQUo8z7aZ_KQhQduewq1zXIopCAmRd4683xz6zOKwTj3jx9mUIdAP9s3bTJ_ywC_VR6jFt7qHrYtPXO7dn1mBAyi5OXyd9rOggyu4ggR1ZAY15oxTYnFktXAbCGY8UHwNzcKaaVbECsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل نانو بنانا 2.1 اومد روی Google flow من، و افتضاحه. اینجا با GPT 2.5 مقایسه‌اش کردم:
https://x.com/MatinSenPai/status/2107527090019131503</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5532" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینم کانال تلگرام یزدانه پرسیده بودید توی چت فراموش کردم بگم:
https://t.me/antimatter0x1</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5531" target="_blank">📅 18:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lxa__FXR-R_HM6kPSExobFHUYA7FlRZI6Kcdj1bd9CYUtRaGjObhsNNt1oBJt4GNZintKFlXQQbPyGBButHMslPpoUOl39673uobL0a8gCV2ibgCIGjMgy5Zbz3Q6lavy_Sli9bKSaFgHqHfzc8pWnX6Jmaq7p9dErxzauAArJcXAocfMuMRJ9OTUth8beUQTPRaMtHpgO9GEAQCJxvxbUNm0IB2qLN_E8tuMpg3-5pHK970L3LsbzyNwdQnVmpWeKtYF8dKkkZdwmGZ0qNjR3Z7zaCjxR_13MueIdPxwxWd5fwBqrluIlFOFXY_2SF6HetcYE8HX-oiKOz6JKEsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو تموم شدش
می‌تونید از اینجا ویدئوی ضبط شده‌اش رو ببینید:
https://www.youtube.com/live/nbOls9zPckM?si=xnkhmSfdlmhENs_2
توی لایو توضیح دادم که همین overlay رو هم کلاد توی 15 دقیقه زد قبل از لایو
😂</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5530" target="_blank">📅 18:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">لایو انتخاب رشته و دانشگاه بریم یا نریم برای برنامه نویس شدن؟
🥸
https://www.youtube.com/live/nbOls9zPckM?si=dnW0hyhkqq7wyJ4-</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5529" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان) با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید: https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5528" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FlKY9mccaWDjHJHbG96P72tSrEMIR2zDHo__yBHwPNOLktKDskbIvW7su9O_AbhIKOdGm0JSAcLbF1lRt0nykWgTmMU4K6xqFR9t5qQeKoZZwE2SezgFNIIjv9kxUl7LA7mXrtTkqMtfZpPMqKVCfJ-db8AV4mn2blUTg0FfFpaMvUmYmcRKUtS9qIn8icXKJsqvhiL5TqYSS0ygixa8G75ZxVjIRtO-wEMdJlNPqeoDKhpfEye3CNrLMYKzyhNi9icJ9QsOSdtkcTULfL6g8gM44g6JuMDIlXJy9Tb3el7G1QAkQB9m10K4QhBLOsLj4thYPchAyFsfdZVQq5KaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان)
با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید:
https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5527" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Matin SenPai
pinned «
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:  1. CDN/WORKER with ECH  برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال 188.114.97.6 استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5526" target="_blank">📅 13:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oF5xGFGRcFfeU5veRQHmwKJjuEFRzjlDWF3iZPelsoznSFUKF9_qc5KYU8WJwO_NrlJLakXIOP6IlTFSSE5enhpPd8f_rLxAP8Q8Hh11KR68GQ2ZSVEFvmPH8ht5vkfpHIiNLpDqvMhT4N3h6MmtmExJ6RGomtB5OM-AozDxGc4s5gdtKv0IKIQA4-p8-f7Q1oFK5rQYwzjUB6FcNIaFem8UFqWHYwtWtPZNOCudj9TLGsk2C8w5WVpYmQZ5h_Hc7rdcOLtNIohEV9Da1D7AGQ1Es03yqb1Gcq3UiU7wTIYwZ3UTUskZayzP8CqWQsDhDYJVKAvhveLEC3PWkgcVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتای کشور به قدری اوپن سورسه که الان سایت زدن کد ملی و اسممون رو با شغلمون میفروشن که مخاطب مارکتینگ بقیه شیم :)))
✍️
davodm</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5525" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gerf0R5tYTzI34cXJLMwjC5nQ4ggiGvAL67qFLIWaEQTI36-Lv8cF34VIuJlMHmdbAjCvLc69As3FJVXojxSC-dXip4t2coPlp4oAVBWSkUmZQozHhnoWgBgNBJlCg0fwi1DeIMZ6mYLRFTq0SCdS-lY456W5B_wQd3hRPxKSmgu6bqwCP5nGhuKT7lvZiM0AGSB4HbXiB19Cm93JeCfWjdV-dz5gJWg-YxVQeD2liyC0OkYLIRtkfBYFPnrR8AajgklkyvwbzpmSN7U9it2s7byxPvxTvGSJ_ENBnEJjvhHwEOl-mXqVcLT83ThnJlAEL-f2AbmxTivtq0Jk5f2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:
1. CDN/WORKER with ECH
برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و در قسمت echConfigList به طور مثال مقدار:
cloudflare-ech.com
+udp://1.1.1.1
را وارد کنید.
2. CDN/WORKER with IPv6
ابتدا echConfigList و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و سپس از یک آدرس IPv6 به طور مثال 2a06:98c1:3121::7 استفاده کنید.
سپس در صورتی که دامنه‌ی شما فیلتر نیست، finalMask را خالی بزارید، در غیر این صورت finalMask را باید tlshello-0-len (همان مقدار متد f&f) قرار دهید.
3. WARP with IPv6
از قسمت add aether ابتدا پروتوکل را روی wireguard/warp-in-warp قرار دهید، نوع آیپی را IPv6 انتخاب کنید، اسکن کنید، بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال ایرانسل:
1. CDN/WORKER with F&F method
ابتدا echConfigList را پاک کنید، از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask را tlshello-0-len (همان مقدار متد F&F) قرار دهید و برای فایروال ایرانسل حتما باید cipherSuites را روی semi-python (همان مقدار متد F&F) و فینگرپرینت را روی unsafe قرار دهید، همچنین دقت کنید که مقدار ALPN را درست انتخاب کرده باشید (http/1.1 برای ws و h2,http/1.1 برای XHTTP)
2. WARP
همان مراحل فایروال همراه اول، منتها روی فایروال ایرانسل میتوانید از هر نوع IPی استفاده کنید.
3. MASQUE/H2
از قسمت add aether ابتدا پروتوکل را روی MASQUE-HTTP/2 قرار دهید، فینگرپرینت را روی semi-python و finalMask را روی tlshello-0-len قرار دهید سپس اسکن کنید، و بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
دقت کنید در برخی مناطق سیم کارتتون میتونه همراه اول باشه ولی فایروالتون ایرانسل باشه و بالعکس سیم کارتتون میتونه ایرانسل باشه ولی فایروالتون همراه اول باشه.
سایر نت ها هم معمولا از یکی از این دو فایروال استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eEnzYge9FRgA2syIdeZQvG0jN4VQ4pc7x_hqQ-1QUg2oW6_jLrSEtQzE6YtckbDwZKySBXTwQ47NamnUzU5X7QjL_vEn2JnVZLh5iB2bBfzPYWryC47NZ85VFnJ0SgqG1vtMPxlxL6EJvYkDWIWLR3MIjoUHzMfBWLNf85gJ-l1SwOu4_Z4tqBrqd7_wv8HMJ5FUJLgQG2-qvZPVWOtHyGB7DSYpFWqDklpsZegrbHeGhQscBSloUU5GytE6QEpsLTDaeeS6Qm6jB4kKpGl_HO6pTRMCEIPzhKqqJKsofiB9HL609f5lPla0u8b_Tkvc8xsO9lqUdH0Qz7gYe6Txeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uuzhKmMjhMAJUVxskJ7Gst7oXt4e8qy8_QQyGfIX0fHGCg6M9fvuoLCGXvZ_s0Wvg-A0qiLXFIti_LuC0zTnTycHxYWuY1PjZv87v9YVQEouCtOj1Nt8Lxv-EufJsD_TFKRhKE1VPFjcNR-OeJSJ74OX7InmYhTg9BaBDLk88V28RIWLFsIltspCPLoE92igZzPH6uYUWiLAkw9hgAK7Jen_vGN1teTMzZ9W6CyXtRPqoMvfZfyZ4OPucflJ6O2NnMCXv0lL5fZ3QKNwRvy5mLu0WKNb2rewjFtg4deTvwFjCmE4nF1WkED5D8aC6iRY5vFi5uMOsHAn0kBv6FEzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TvmxPh7ylFeQRfg_RKVZGynnJP3yu-r0qygHDBpIrNUJHdbzod3dbRfwZco8qNC5fcLaxNIVkZqg1l4Cewfxu6c0MQx-Hs3ykBqgSTtg9AZQo0quIZrFsHscX97onQKLl-mmkfyf5EpM45lJr6TS7uipg92fmiigyRk-0_P8xTXFsyP4Rrdd9bap-b8qKqAWv9hPspDg5SpyzJOXwE7o30L5Vd5a1xdf-C3908yEJxz0BUws9k1X_1TAP1Q26Z8iK2HwgL5V_V8iDZTwP6LbNZXtSuWGNJ98zgEIJwGms-OcQTP3aQzYSo8k6eH7ivtBYQMkYXb6O0goXpOZHvLjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t1I46lQqC0vVkePYq6kYli5UTeGvgJf12lsaOGkzcyYApsncHIaXuoQIJPxQk_F8Ub97d32YN5JU5lTT5Lqjnza5k73weojzIxgUfuRCwKnaOSzCX0eFOuES5VkAA-zRqMD-L66NY-Z9VRdUEL3YQTgzUZvuzVVJF2ilnHUCFsoNKT__oG1mzWy1Bx-UqIZuCRVgURUa1pLrOod49iv0sXO9gjG3Hiya8HIprOxdaAZ_MIt9WaUeec5KgtCBF6uXdzR4-jkMzD7o2QT1p5c0wMGn8og94snObM8ph2dggT4bpxMNGnfNYoWT--cxxyeBais5DBn9oHbNeSM5enFe4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CD1ID_phaOGGNo1e4m-vdqB1DNF7q_d-BoyV0bt6Vi97SuX0XD8nloIT1hSHInSSy_wzboMrokSyuvBnyuXWMt_zEKbPcdTPpEZEeHbYzUouZ9YVCUX7oluhkYSY8slfaRX47pfCmsw5EWC9KQ2oBDY_nbTI03cLG1TVTAIBHcMJHoK1U0hDJg4Ik6QEQF0c8LJ4korfEjeLeJOinBTLH4neKmIui8bbnUlZ4wi228NkpUrJFYLqFjrYRbuJMZl6cmzJHVgBI-gckVq3WTZUy6tn3rf9v8gCtSPWAtWuRW7A_BysqSO7C7erJl1xxIrTX4kE9Rihv_VrZsHO7Csdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/maMBcfI5Tr3souqtbhKOcOugFNmZ0PZdRlYthV1W8z91dfZmFfE_oBaMtP2eUEr4BppGVGhX_nbJ9ez-4e2iQhNPD8obhvwxgDz-WG-tmBeZk_xfKtL0spWhJPWAXN7mRrsU6wb1ajfBEAlv3sFaPFDrSvpCC26u4SVSfqqaBmDmNEwgSwX35MWHZoHfRkgvmOX95CShUTSSGENdmKPRZGxVdgc40eOpQL0fZjwTrDiMAhxLOuSKtlHuIzj7mQZAr79DAqvksJZ_ncbK2PVhRIjhVDfCW93Fym_yd8z8j2s38tvOLkxYMPiwSsgyQDMfZc99oQomOGkmD8SYsnd-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده.
توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل.
توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی وصل میشه ولی وقتی میرید جایی که پوشش شبکه وجود نداره، گوشی وصل میشه به استارلینک. یعنی همون اپراتور قبلی ولی با آنتهای فضایی. واسه همین اپراتور تلفن باید فضای فرکانسی خودش رو در اختیار استارلینک بذاره.
حالا در مورد ایران قطعا هیچ اپراتور ایرانی‌ای این کار رو نمیکنه ولی لزومی هم نداره حتما اپراتور ایرانی باشه، مثلا یه اپراتور امریکایی میتونه این کار رو به عهده بگیره. اون وقت شما وقتی دارید شبکه‌های موجود رو جستجو میکنید، اسم اون اپراتور رو میبینید در کنار ایرانسل و همراه اول و غیره.
یعنی از دید موبایل شما انگار یه اپراتور جدید داخل ایران فعال شده.
ولی مساله اصلی اینه که توان ارسال از موبایل به ماهواره خیلی محدود و ضعیفه و حکومت میتونه با ارسال پارازیت کاری کنه که ماهواره‌ها نتونن سیگنال کافی دریافت کنن. حتی توی مسیر ارسال از ماهواره به موبایل هم میشه پارازیت انداخت.
تفاوت این تکنولوژی با استارلینک اینه که توی استارلینک امواج رادیویی به صورت مستقیم ارسال و دریافت میشه واسه همین شناسایی و پارازیت انداختن روش سخته ولی امواج شبکه موبایل توی همه جهات پخش میشن و میشه راحت روش پارازیت انداخت.
من مخابرات بلد نیستم ولی اگه کسی تخصصش رو داره بهتر میتونه نظر بده که آیا روش عملی وجود داره که بشه سیگنال به نویز دریافتی و ارسالی رو بهتر کرد یا نه.
ولی میشه گفت توی مناطقی خالی از جمعیت که پوشش شبکه وجود نداره و در نتیجه پارازیت هم نیست، این روش جواب میده چون پارازیت پخش کردن توی همه نقاط ایران اقتصادی نیست.
✍️
aleskxyz</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PeTytajXong0v0LQ-iuPZBXMSZ1HNOr5ZNvjHI22yZ99zpoZlXyidm4IVIPcnafj6Fby_HfXiMenZ7TR7p6d9hgBQHaTz_8Vd-njixBaKMzqQi3WvjfcnPvLTpkLJeCdeHsE4V3mKX6g72EKZLIxnZieLTMsqfbunxSysbw7lQ1RuRINRZDePSi7uvjaIKs3tzhnwCT2CaVhGOcau7i3OoYs2rDn-rzR45ogf_w4XCy2LfB0UpgxI5J7uut9RJ8DPnNXTgCMFhHyA5Z4gQD7FSnn1q-NiSBOudqC9DkqjtRS9CSKhFgi-1ow5FTg5VnloEArrSAW5hQOQqvnWLWNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tVfuPuBDnZ1I8iWEZudtAg1L4ksh__PtKsztJpDt2JrUR3X0Eo2YXSPVBbCutBP5o14eeqjd4dvbjeAshUlVN1gL8vSj_J9dVCvyzdoZwreXHTiy_U6YEwCGl1pVlnm7GsfFYOuAZzn7x9ZaZkq56qF_V37FVaKjFfmj8ZfEOT7I4TuCioRyUAkeLCxES7XkRa74paWj1q9KFCxK7cgkqAGxATtPdbZWtTRzEQdy5PcrtY0WSzrIXDsbFKXWFZWhwtiqUczZHd8aumuql00mrYgRoouNgzkhKlbhdgyCs8Vcx1vLQ-1l-THsC7K5GGY8xzrI-D0ASUrxDdjUOJ6u0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HvTG9HFPbE20yMsJQexky6VjCgCeLqv-2Ee3Cti6M8C5ZmuZmYatRJnn8e_eCplWRPyeA15_G7eq2-r2hafBmatkQUUs-I4K_QnN03JJk49J1kJaN_wMDTlgpWNKWbsw2X41mMhmIVAR6WTcFz9VyV_lTuB-mJuYt43MZddQUp7XZK1dCyRbR5FnB1Y9APfs-k4_kSn1ICMJZChyQwLbbHqw_QuhDrJVJep9Lud7k7AdV3C9UA5Xg7dormkS-eITqln_fRJGUqEMoXTeyYFDe--jz5ogw58Afl3Y_xttCuYOsxUV5qCSM1DL0BjiGP--pMQ-MnKEqCeXLgD7d_cf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه SenPai Scanner v1.1.1 منتشر شد
"برای اندروید، ورژن قبلی رو حذف و نسخه جدید رو نصب کنید"
• حالت متنی برای صفحه‌خوان (NVDA / JAWS) و افراد نابینا(ببخشید از اون سه عزیز نابینا که درخواست داده بودن و انقدر طول کشید. این آپدیت رو به خاطر شما خیلی زودتر دادم
❤️
)
• قابلیت Anti-DPI: ClientHello تکه‌تکه می‌شه، همون کاری که توی PattNG انجام میشه. مقادیرش هم قابل ویرایشه
• حالت Gentle برای اینترنت‌هایی که وسط اسکن قطع می‌شن
• Paste کردن IP / رنج / دامنه و شروع مستقیم از فاز ۲
• ذخیره و ادامه‌ی اسکن بعد از قطعی
• اندروید حالا همه‌ی قابلیت‌های دسکتاپ رو داره(برخلاف نسخه 1.1.0 که دیشب فراموش کرده بودم. این الان 1.1.1 هست
😂
)
• نسخه‌ی ۳۲ بیتی برای Termux
🛠
رفع باگ
• تست سرعت مستقیم همیشه fail می‌شد و الان نمیشه
• و Stop بعضی وقتا روی اندروید کار نمی‌کرد
📥
دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
این نسخه‌ها تماما روی گیتهاب بیلد گرفته شدن(مشکل اکانتم به لطف یکی از دوستان برطرف شد) و دیگه شبهه‌ای توی امنیتش نداره
👋
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jWPsZt-3R8niSARNCS6zavTM_LM3fKmYL3QMtXTIgusqIqgLK3G7zUu8-AzPmzLiw0lZMuk7XNWt8bVABG0N0bNwuFa8FSPfAuehyolckqsYrTZTQzjpnCYVCjtTUTtWHMPDL0b3Rtd0Q-pir5vhdVpV3NLUm1lP-eg41oyTijjzrn6fGf5pYXRK6PpmqprtbydDHX2x5m3SKCZQvEByhYg2y1UTHuBeeW5gY8f3wkgkPyJdEu9AsJZx_AyDXiozJOW5utKfb8QZ-8DwyQ4LIrUCxbqqUagPcLlZL_hCvsS9TBQM6AL_oTXIWiPpFrfwIh4rk-d37YeJU8MNd0UzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X8ON1QwjucsmHzSFbs2uDcxr11chZfsljxYCaiTZahfq97B5mCa8hjjwgL74wS4oinoqIJKt6otWJJLmEy9iNX_j6cjEAHYUPAJHbuNJvXon8H2S5IH3p1IsjpN1wamCnr1Y3zphCdfBFuPGvbKoC6-OflTlj0zMHh3rKeJOJHEgVx_D58Mx27kox1cEnv9W64HJSG2HLFIq7hs_FBs2nNdHLSHc-vxfwVjXCgNT6eyhRx_RfzItlE7gzOyndWnzQkE4HLgb_oqU-z3uEvTsA0EGpLXxr1ajbKSrESF0MiGxAqzko9YzY2PXqxM4jzcfEsuS1YyhkAAUknAuNp8zjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/suV_x9m2qtECnRQPCQP8V4Fwo9jK7S5P_30-6ntVIpBa5XzS21LIszSKGHdOKWzyZbMYmyV8CwTAQw4LHhanG3ktH4dyt9bmna6Rw3qpHlTwulVw7uuL-jpwfTI_cSwRV0fSJcE1WXkRDsLWCl0-hYYvgYpKaWJBWRot2JdzrILm1Aq2Z-lcCuGIR9xYAx5HNKA8SwUVB2Sx-834c4yp8dEijVGs8Xiapme_WYUT-d3OopBe6O5v-yoyCmP0-VksVMI1F2dvpmGP8Hpku4uKdUxiyeo5oPaHGfkfN28fx_7BYJAJ77dIZ5H9U6RurDM4IW1pHgxZDAvxCPmPy69MAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه دسکتاپ Cline برای لینوکس، منتشر شد
روی Cline می‌تونید از مدلهایی نظیر
Muse spark 1.3
Deepseek 4.1 flash
Mimo 2.6 flash
به رایگان برای کدنویسی استفاده کنید
https://cline.bot/desktop
ویندوز، مک و لینوکس
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=SBtjfX-wFeM5qgvI9TEhZK6MeIoxWAffMk1mNo_bTkykxkJHRi5vMXbXdn8qSGYOASy2TMwZJwOCncTblM3fWXhTDwBdzJj1UV1Af-pmhZcG7CMpTv1Id0SFOwGnyNTmaoD68v8_LQcxGvXnjIvWIWDLz_xDvS_WNG28gEODS3RRQqVB_j-hAPTYBIO-DTiccNjpE90HXwAKdsG7DzMruFwW6YSXqRallgrn9TTtKFSo7dV2wV6WydJKINAQYQ9nryhA_3uHEvlbLVhBoE6IVm3pQnXar1JSU8evujc0Dy-Gz9cy8SD8d2BbTM6kXDMbFqhkzrpiU92jiyTvEL0glA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=SBtjfX-wFeM5qgvI9TEhZK6MeIoxWAffMk1mNo_bTkykxkJHRi5vMXbXdn8qSGYOASy2TMwZJwOCncTblM3fWXhTDwBdzJj1UV1Af-pmhZcG7CMpTv1Id0SFOwGnyNTmaoD68v8_LQcxGvXnjIvWIWDLz_xDvS_WNG28gEODS3RRQqVB_j-hAPTYBIO-DTiccNjpE90HXwAKdsG7DzMruFwW6YSXqRallgrn9TTtKFSo7dV2wV6WydJKINAQYQ9nryhA_3uHEvlbLVhBoE6IVm3pQnXar1JSU8evujc0Dy-Gz9cy8SD8d2BbTM6kXDMbFqhkzrpiU92jiyTvEL0glA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hAawFR4fgqYWPw1973ekGWu_t59WIX6Se5EuNWXERVEGx7xHFqx6Y7yWHTnaUlxNfU6kEnpgDdAXs80llkrZUSiuUw2y0AgVnlaaZx3zCn8rDZJ_obO0tIrQy-uQhY8umAQZ56v0m0PXjHY9_4EOGLWXChOtrsaUApLHPutrMVj54wZhGJEu9DdvSp7nSiWJVKMWpXMyi_N9kVPovPiEZzMRYkL7zgcZkXnDXk34TFdkBH7Gc084pHuLSDRMejPh91VguEcsd9HTQHXNMHkrAmZ-SlxnGa2hAVWmBTbFd_rYuJBPkXZ6vLe3gLx_XrilZXEF3Lc3MKFd87WZXd74ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jq9alZQRMzEAve3iCiDqBRPXnUvy3ttIbgiMhHU-4nC0vUmGqGGXplh97u7UWBmX4X_wNFhjY0Ea66GtjAFsV-vEcQHvg-4XTGJd4bSjbIGG3O7fCAyO8UVjrkUa7npw7C9aGqZjG7iKjJRJ-7dhwuzQwWNkm5kJIAIfJGZQHI1-iBa0qAMEqx-VWrroN0lZzD3-F3XLHYb3jrYRK0QsvivMBozeturxtdazhSN2t_5jviQgMUO_VQ8LM--J64HlpocIpafvBxbqx49JwPnr6OJ4f2FKYINA5lQ-axc7LKPtstkTgVF7XqSgnEWZwNwljkx4DGXW3ivnKFEkFXnT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tfoQtQ4LOPTDp6cGjvRoMEH9ryuZKCXupP382rcypwlS6Y_AaE6CT-42tar3WYkB8qbNOBE12TXw0epZNZ-ZKrYktrjh2IQRc9A8uRGVnZZxnOtJKgyiHwRX_CxLr-ZerfZhOr_wTEt5YBmNch0pR_STeg8DcK130rOURR4AHA3MItZ4VML6kPz-igf7DyhNS0tHgtsQTLj34HghNNzGg3thPOfdv4iQDwjrJQL7sBgTkzzN4OVwEsRuOrZbzjh0nA4cjvuq5Eovm8edV6M8n6eVYORH-QwWQxYFTfDZgpFUEyUJ_CGFAVKxE5FlipdrndB0UNAI4Q23Xo9zq9vOdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LVtfZY3oPb5L2C5GrDLN7YcrHEuF5itYVp5WvCcRgod7R3i9fauElFjUbnhEBjEwD1W7D1MBZRXf9vXjWxHYRMV-dy2dIgR-1uc_LdNpZWbLemeCMR1YLvHJ2d71drVHvKSOXIg2pQRSQNNonKOlZLZMJoKznSJRUO4JSbiq7g5hPiOtnBvZQ0vqssvS65eXE_p5_eOTaeMNPO3cz0YUwElO2eBYV-vFfr8R7gzJlKJCKJGSYgFMiaoqDIw4Y04XhZ0k9ifUKc3_cbmzCyCmR1JNWx7aGOU_82j3VD3XdYaWK23Wl8F3q93ejqKLn2AkweHhtg_bq5icNHVbUWFo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfY2UlKBd2dpWC4xTzGHDIWOZrVmhpwkidn3pde37cJTgt96Mbtdv_hkFJH97kUIvl6d3rqpHwJxAdgxWqn_PvUTAeH5wgwx9kdF3RO8zwTc_6E_Vy6voNesDKDEDg5F_bs2UDPUlK7OZH2PXQAJhybSmXkpXtHXhYCFB8YzlXOIO7HN7rIOcLNKUQ4rtTmNEyDi5_-f0DUSpWVM4BMTcanieo39X2exqtkOd-kkGwqv-1GHm2sWufgiCf7JzPnsFvYad91OIIB5bT9QlRbAnNj3nW5AlNFT1gnpI2OjoeVSKlZHf7PLgOV7sRUr31Wv06DaLOqhoXUy68Qm8SEYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GQOL1h4Jcj_qa0yrR8MKhWpWW7Qtkfw_lAFSN83Xt38qrcXSnOS4fbXok3OfiuamKAM8I6_EedlWWIBdh6FN5E-sbBXI1v6StUr1K_v228ldWBFGsXxfx-54hRfl7kcsZ8S5hrLcrAr1r_sTlCWcLRAZHdydp6w2qHoaceScVCZ2edexdgfK5xryCrboZzK-iXw0kGzqjO9Ys5Y1jBqvP208hbEsohjMxco0kMkJMCzwVAehXOhVUl5QSMPVw9d03lPVEVSUpSHGnjN0EhovlBSjgSPbvVNuMjuXJjLH_rKVGgbnJxR-5-AvSYtrTidJLINaKAuEMo1ijvchfDXwcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUK51EN6oQviWohEqfKj7HZYQi2W2nAeqCbLb3ufG6rDppcd1vA-aXJWkEzvHFFAP73KL19qwnehdQRvQrCxc0LUgSbH14xgwj8LNbCAzm4Agw2fop_x8Sl7MjCqDZd7KWrz35BekVpCYRB43ix8kRudehCNdbkbsw98MaVotJukjYahfydSli0gh8Ps3osnlBhr1HPeLMKpBm8qLZ_yHPn51crAjLgYX08KPMKRYtu5S_IoG1ySOTpnVwi7wFxYMtSRmT3odDDDjv3Vo6_coY9FbicpJu4nuduVYMq4hfHJA2TSmYz0x1AMrQ3L-82S5OQw6lBDhqbrVXJBNnxEMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XiloPIVS_esB3coH7BRU7gjdsCoIAW9LictkOOQbORW_AVIStv19E2POqtDSUdoNo82XA06njBfv2cUeUpIQ4ici9ekGNxEkLUZ_QuIFpEOlE4fFbNV3VQebEaac3g6MBql7Th32JKo7zkdaUh2-0VdnaxXvCsicCTmCuaMBr8168HzluOKsNzVqGyxWNj1WLJAVAq0wlf65LDVK5ioU6dxY_vwzE95srPzlwlTmH2dltjjGQVDVnUDxVr0k67o7jS3aE9FECW8luCfSpdkoOM_oda53NgoSvLRxjHSzG0JvKBDT5rMMrnFzaQLhlJ-3wPySThkoMo1VBuRuPx90Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SxgePG5UESQfT_sU-aa8s-Lj55K24KZ85HgGa7ACPTCFJcNWli9--z9F1qnAgkUqNUB2AUIYCwUZzvOttLAUQndadt37T58h5TF_XXsdITtRSjfBDlYN3uQANS2KEpRpUgZqDxReoC3pFsgQ-wDbuaa54Y0P92MmkOCmC1utWGmV6BFPsPRUIU5pxOnD39E6GZUARxeAmwL7h7SI8SqGkYEzfdukRLPvdv7tWq21Y-ixJNw5npgY2JfGPohV3mNP8UyI9KVH3lLtqilPb7C2416MDzx2uJDN2CrZAhLFstBDBBL_s8fw3731MqbNKejzkdzNbPLdBm2CgsSfwH1DWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gcadeJ61Q4zLUpfcih9nT0WyqnOcVIcrGRj0LsihVAMGz4KeDGeTglvu5XrNbfxB4EULc0PJGDLb2U1qdcbz8kBmSMJDdrdzwsaSStSLyyZm-FYrOR-WyoxIUO4HxeJHN151surldqZo_SOMiNOKa4s0ZBSceV5rpc5D--Y5P5bVd74STOu8r5wdnSx0ieo-f2seXBVQRklvEmaJEfDd_NTcYUIEQD77JRDd9ieCYC2sHKExNuFl7_HBXxAIUlBffV6iBombK0w5MQaCLwxI3ChQE9paDjuKRNJhctFqFEIbrdtLVZKauTTkELdewiRREOCxwAOhCfSOw7SdUP9VEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eGwzIsWEfsvNGstBsCDUt4nc3cnxtkmJsVcy56wnwXuxKdkHeilW_AgbN67MLiGEGaguqdtrVM-Lr1haJhXZBCBg85WTXKtrbF4dZZfsL1US-t8yGrO7GEoayem-v0j1V4KSHl2RGLmrZWvU2lRjzWRGt9Ml7PsPgxWCfkD4LKbdsW3Fy-LfxHktv0uyBBtxPB5tgqT5qLjFTCTtsYyPq8FglZPScKozvODS82Du0bUm-R9VKPjOukJM1LU45gtRtKOblhY1Aeof2RJNqfItvl4cvzpDG6FMIutzySxvun3zXwvvIUvNhs_f6DYmhjwK5b5Scd5w6ia3IAst9CBJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXJrCBVEVUbaYuRsCq_9Rmvv9h8MwdpCoVTUMdke2cJqc9eO8dzix8Kbw1cirXNrfczHM0OH1kHopl3zXmjzbmw-aIenQ27RG3zot2j7_Sx6fnRF2w1xyByDxmF_KUkAOaHMlmxSsTFwAcK_2hrNxkiO-z48YYNJ5zKKeVdfA2xew9iaZqVLLz68OZnK7xJtV3qE3jXUe5C8htVO9gVeohn4ZhUr43xzdX6fAxbhfT7dgeHp27Z0T58amHdDLx6ZrzOlzwzc6q4E5Tj0-ojvghg58VSywAzBJHW_c5UCj95ssJ5ASXSrz-Gtb30PLlFTauME5b7rbCS6tbO1ADyZVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZQywxyKFXvs5Z5zhCfaG0XR90v3kgetU_WFBxcUh1HME5hnzSkuyczzIwgu8Up5fN6fACBsGN_0Uo3rAreQbdUgNp2yX5IImNcxu2KrqwxPFzFIj1gPHf3IGiN2xEYxiqPYVqjR4AQZx_lz0e70I8Z5bC7bf-ZriZLqpzsYZLUV0j1cVAk8Iq4HGEmKcBqkyRlcA-bWAEhmkPIqJp6J-CdLnoU-CQIWNapm437k7dCE7Hik2hXq2fuSY2Lph9t22oa8gm0g6nLMZ4KSwfCFk7OJ58scVmEdMR2Y3ffMjR4ZLV8QFvaKWfV2fLI1BHsCgqq6o2HLUvOjQBRM7g5HtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)
1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا
https://github.com/patterniha/PattNG/releases
)
یا نرم‌افزار PattN(برای ویندوز از اینجا
https://github.com/patterniha/PattN/releases
)
دانلود کنید.
2- کانفیگ V2ray خودتون که با Worker کلودفلر ساختید(آموزش ساخت کانفیگ رایگانش اینجاست:
https://youtu.be/iAbYpjXyLpY
) رو وارد اپلیکیشن(PattNG یا PattN) کنید
3- توی اپلیکیشن اندروید، روی مداد سمت راست کانفیگ و توی اپلیکیشن ویندوز، دوبار روی کانفیگِ وارد شده کلیک کنید تا پنجره‌ی تغییر تنظیماتش باز بشه
4- توی بخش Finalmask raw json، این مقدار رو وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
5- توی بخش Fingerprint، مقدار رو روی
Unsafe
تنظیم کنید.
6- مقدار Alpn رو روی http/1.1 تنظیم کنید
7- توی بخش Cipher Suits، این مقدار رو کپی پیست کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
8- کانفیگ رو ذخیره کنید و پینگ بگیرید. دقت کنید تمام موارد رو انجام بدید. آیپی تمیز
188.114.97.6
عموما کار می‌کنه. اگر کار نکرد، از اسکنر
https://github.com/MatinSenPai/SenPaiScanner/releases
که هم نسخه اندروید داره هم ویندوز و مک و لینوکس، استفاده کنید و آیپی تمیز پیدا کنید.
مقادیر ممکنه عوض بشن، مقادیر جدید رو می‌ذارم خدمتتون.
موفق باشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIcMRTuNVNflAAUsgrYDqavyNU7h_5uXISVFkMpP3Ce7EMZKfLB8RmGCTqvCvPCzA4nlPrwv2peIs63yeTb9aVPmfEjyoO7My0wYVAS4Yggbw4njoqN-9_YKRVWJ_xu2JrxWE6OL26WHr3YzVt1NJwyYDtKXmjXjVLVLXVOWcxAOTJphyzHfQ5CZPW5vxmFYIACgxR66Ej0NT1avLh65roVShg0P3iUhMn4uJ2RTkt89zy-t12IDzY2kfW0zgPmMo3DzJIojWkfRBLkZhqfeyhvJuxnjUym4Y7lccx-zRN5PXPWoxnjmtYoCxShFurRX1JjkqMnU53Etfu-C16aebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل Airbnb: ایجنت‌های هوش مصنوعی به سیستم‌عامل اختصاصی نیاز دارن
برایان چسکی، مدیرعامل Airbnb، توی گفتگوی جدیدش تأکید کرده که
پارادایم اپلیکیشن‌های فعلی پاسخگوی نیاز ایجنت‌های خودمختار نیست و دنیای هوش مصنوعی نیازمند سیستم‌عاملی مستقل و AI-Native هست تا هماهنگی بین ایجنت‌ها و خدمات به شکلی پایدار صورت بگیره.
خب مشتی یه کاری بکن. ما هم میدونیم
😂
طرح نیاز که خیلی وقته شده
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wn6787OCyLhd8UOgPUuxC3OWl3WulOUtBntfonGzbaJ4sunGcL2Us27G6KjawSH1KEhK0b_QVzWMhmqC93ndeZ-YObxGX4K8ofUqokMcK91C1wzSzCfLbWPYif33iBNADhji0QxccRs0-Qo_vkKC32AFHos3KPD2Fou3o-rh7ai7syIsXyNjdlBhcs2QpLj22H8r6138JC-DupjyhvU0WIixhWrQVjIkynE-EOw0LKtCa5MOqVLO7fDI37bkQ6q9KOttohwTMzTX8LKVNi0niGDZFAuR9WEgjle8_Po6KAAQeG9_8PI6Bn2lNNXLNSDWP3qnhaRLpIl4q-tWi_ZE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sdGBT4437Z1NVUJaiuaqIUBULJt5Scyn8wY1IlE1ehCpcbY_Df-JuxSQQ6lC8gokVt3uRqgDEjeCOlaSfHFQSgExo-JzbJFJP1hFtlZXgHIrV5fpunYKElViGiprhnSFyNWhi2WF1XUaFm7zrasoWGevipkFXOrslpDiH2BbRczFG0Zq0PuUHkkzVPJZpglroiHhwVAnX1LOQSxIZ9wuAZV_dUhYRDtntpr1TNNqnwJ2rbE4-A3ZFIzmZEKTnRqLtLQnlNA8S9o5E9aZxk-hwbZ7RXcr6zvVVwoIQNy2sDPMzhgpk5OefQIfjlkvZCC_7MqNKIevVlrk_eugzjWTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cuWgrCVP7vNb7eZiUuIbhVd-lBsI5l59DA8DQOJw9Rng-bZrDn38_Qsbh8tKqVGYAeDNY-Oq28D0ifydONqVODnPUlnKyXEHB2Fq53DHFNjYsI9vMoAsot5PhPH5hsZOrL8VMqzh5SgDOLEzbQiRGrSpVI7QrU_pR6qRfP6VsT8CRNBtDFpX3urCHwLqqF_v-PKJj6yqJKOfELaQEvrAmep37ezUoPwfx2sQZdLFhwK_R496wGVbX6Gwvm9dyS2RD98_KY7_fCZICURnpRXX5X9vtsj52V6qDhWypeeCdoDE7uxyZG8vaP8bUaFUTw9zLqXxk4n4rkgU9xmp2va0Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
