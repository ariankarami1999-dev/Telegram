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
<img src="https://cdn1.telesco.pe/file/vXFwaRNxbrNyCTGOzni-avSrnhs83nc0fRZJU9fVX0wkqySa8pia_vHj91MzUFqEYApNSBT1uEMcPHy2bnVlTlONxr28L2tMZFr99JGc6IYCIYhrnmBJs0-DhQnEyRiob8dVZ7THtabzbhLtXRspcZaVgzg0kI5h5Hgdne4AreJ7aAUbvSZC43DdA_liRUYxxxSv_T340KSm6X3nDgKxfC9q8h0FkAf7LrtWS3J14K87pJ233ljFlZqF3CyrrpIKjCl8As1PXXbPP4gIsQMHysmwQ8WI48wOrIBkOB13l3WP7hDGUB4z8SVV8YxSsW1EZtX4YtCveRcBHRR5hVxv6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 03:10:30</div>
<hr>

<div class="tg-post" id="msg-5570">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o3eSQOANFlw7YbpfR9ja2cXCn_lQeXwpjR56yFg8Mq38IBZf7zLr0OwJ_cilyfdNhgmofvVVO7vMPP1sXkNHCB2zTtzffYq7qBsmhGPnAxV8VPD6N_jdcONijutYncyL4_D4RkqxHwJxyNgZPRiJke-tSCCW9wUda4LNI5geRC7lhV-EBm6-z7VfidrH5bs8Tk7OKWxqGhfHTOYurOB1eiV4tX4QwBFuhe9DXx1P1SjQXndY8g2oc-31doYhC-Jv2JLxi8MgtLnvXPxoRkfqHdwiEprXEjkeykiIqPOWiGNY91fDZEmHLOwZ0psLkBjeUSnNLHAY99qQAqDGaikr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش راه‌اندازی Muse؛ ایجنتی برای روزمرگی
اول بهتون بگم که Muse چیه از دیدگاه خودم(یه آدم با استفاده معمولی):
هرمس ایجنت رو در نظر بگیرید. اما:
سریعتر، راحتتر، بدون ارور، بدون ارور، بدون ارور، و بدون نیاز به ست کردن  API Key، یه سرور رایگان که این ایجنت داره روش اجرا میشه؛ با راحتیِ وصل کردن هر پلتفرمی بهش که فکرشو بکنید.
صرفا... با سطح کنترل کمتر توی مسائلی مثل محیط اجرا یا خود API. که شاید نیاز معدود افرادی باشه توی این کانال
حدودا یک هفته‌ست که دارم با این ایجنت کار می‌کنم و واقعا عالیه!
مدل پشتش Muse Spark 1.3 هست.
ایمیل‌هام رو جواب میده، واسه‌ام برنامه‌ریزی می‌کنه، چیزایی که می‌خوام رو توی Google Sheets ام وارد میکنه، جزوه‌های دانشگاه و Rustام رو خلاصه برداری میکنه و قسط‌هام رو یادآوری می‌کنه(
😂
).
یهویی مثل هرمس "سکوت" نمیکنه که وقتی بهش گفتم خب چی شد و چرا یادآوری نکردی بهم، بگه "اوه شرمنده داداش! اون لحظه api key یا سرورم قطع بود(دفعات زیادی این اتفاق افتاده توی چیزای مختلف اما هنوز، هرمس عالیه. برای کارهای مختلف. خوب بودن Muse دلیل نمیشه هرمس بد باشه)"
شما نمی‌تونید روی Muse، پنل VPN و DNS و... نصب کنید. لااقل من که نتونستم و اصلا آیپی عمومی نداره و فقط دسترسی HTTPS میده. 9Router و... هم نتونستم طبیعتا. هرچند به نظر یه کم Tricky میاد و باید باهاش کار کرد هنوز شاید قانع شد
😂
در مورد 8 گیگ رم و 2 هسته CPU هم بگم که این منابع اشتراکیه و متا هم سر گنج قارون ننشسته.
سرعتش هم یه وقتایی میاد پایین اما خوبیش اینه که شما با هیچ اروری سر و کله نمی‌زنید! و یه دوری بزنید و برگردید همه چیز اوکی شده.
و میتونه براتون تصویر و ویدئو هم درست کنه(ویدئوی فریم به فریم کوتاه و..)
که متن فارسی هم داخلش خوب میفته.
آموزش راه‌اندازی:
*نکته: اگر که هر چیزی شنیدید(ریجن ایمیل و تایم ساختن اکانت و آیپی تمیز و...) اشتباهه. میوز فقط و فقط به آیپی حساسه. و تنها آیپی‌ای که باهاش تونستم وارد شم، آیپی آمریکای گوگل بود(که صد درصد یعنی با آمازون هم میشه)
1- با این روش یه VM آمازون بسازید با لوکیشن آمریکا(200 دلار کردیت رایگان):
https://t.me/MatinSenPaii/5130
یا با این روش یه VM گوگل بسازید با لوکیشن آمریکا(300 دلار کردیت رایگان اما 10 دلار اولیه باید بدید):
https://t.me/MatinSenPaii/5149
که گوگل خوبیش اینه که سرور Always free میده و منم از همون استفاده میکنم. یعنی مهلت اعتبارش هم تموم بشه، اوکیه.
2- پنل سنایی یا پاسارگارد و هر پنل دیگه‌ای رو روش نصب کنید(توی آمازون نیازه پورت‌ها رو Allow کنید از توی پنل مدیریت سرور روی سایت(به Grok بگید راهنمایی میکنه))
3- یه کانفیگ Vless معمولی Raw بسازید(مهم نیست که مستقیم کار نکنه. گوگل که اصلا امکان نداره مستقیم کار کنه)
4- اپلیکیشن PattN و PattNG رو نصب کنید(یا هر کلاینت V2ray که از قابلیت Chain proxy پشتیبانی کنه)
5- یه کانفیگ که واستون کار می‌کنه رو اد کنید، کانفیگی که از سرورهای گوگل یا آمازون ساختید رو هم اد کنید، و بعدش این دوتا رو با همدیگه Proxy Chain کنید. و VPN رو متصل کنید و پینگ بگیرید.
6- بعدش وارد اپلیکیشن Muse روی گوشی موبایلتون بشید و با یه ایمیل که تا به حال روی سرویس‌های متا ثبتش نکردید، وارد بشید و ثبت نام کنید. به همین راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/MatinSenPaii/5570" target="_blank">📅 18:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hQYMssF0bdsCTeiNoYT3u2N7re-tiT1yGN2B6Q03Tu72Nz9ozmQ3kgE2NNAGD9ypdG9GsbvZavhn9xzjUr7MadWNt_QjQGIyFk1NO0_boUxINiJVuzh8_QuTZI1d9PJP6H5LuWafRsJ8Dl1YHkDLgFy_E7PzKFAQYGAuQhOUhha1YOrI_K-NV0oCeOtvOPnQ4hAIZ6bFM_0246RJIVvNUK5cvv7C_BO86lDCndo7u6nwrJkE4DWNzNZYyLo022jIB3XBHGXK93FBZC-SM_cU49ffo1Aeg9gQuPOHDk-907tcyj8DfcRVD1ZaXZBcr76Yt4UhRwt8_a2rHpnIECjiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشغول نوشتن آموزش ورود به Muse هستم
فوق‌العادست این ایجنت. عملا برای کارهای روزمره، کمتر از هرمس استفاده می‌کنم به جز کرون‌جاب هایی که از قبل داشتم چون Muse همه چیز رو Unified و سرراست داره، و توکنی که میده توی چت برای مدل هم خیلی خیلی زیاده و کامل تمام تصمیمات و کارهام رو یادشه. به زودی از مزایاش بیشتر میگم</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/5569" target="_blank">📅 15:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BOIWv8Wigq4f2hsnAdIuXQfCUIEdu3RzrSC8-sbYZJvOvNBjfSGsRa6yU-e1a4bMkWMKsBcbyN-PfixVfk1o2euDF9elWM3PmXexTw4UVRbAYLJyhd9mc8DpdrcDslWoikfZreUB6S-bK0LYG9jydPS3OmTYVepEAommEdyOmqmdF6YpuGE90yd6octYda-JClnjMR2vsQc8DXjjkn9MVhVmHfORvgxTiY4bqooOB3YhQoQEy4rIGlLlPl-VjGepS6zclC6Kgc5LtAZxxQt67hgsPLIcLjLUi-kRXUx7D90lBvtsqMqBvdyIlZzRq2CxGOrx6v4PaHmkfYTdT6l1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوری؛ جایگزین اوپن‌سورس Canva
پروژه Doory
https://doory.art/
به تازگی روی گیت‌هاب منتشر شده و خودش رو جایگزین اوپن‌سورس Canva معرفی می‌کنه؛ یه ادیتور طراحی تحت وب که می‌تونید خودتون ران کنید و یا توسعه‌ش بدید
🔗
لینک ریپو
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/5568" target="_blank">📅 15:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5567">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtpxYgNgnBhp8G77qmBRRpZ9YlU9p1A6DdEFsb2br34Ul5pSZwGrqJ8r47t8IT7LjSWZ3hUdpzDstETXco1T31vswFOQnkVon1CioTfZ8jjY5wn1eLZFVAoQhADx-MZB3AR8GdjJbETowaP3C5KhbaBq_M64iv2osoJ6lSVPo0ntURj1Jmqf9w1Pb-vz0HqYJtlQXlG31ujprZ7LFXHOlm9lBBSTE6EReSnrkfY2CkkZKf2VOuDkWN4DxwIsVILenlSY7GqwhuL1l6mcYNjhyTz7rbbPmuGAtWSdlxr64keAWYK03YSlfA-JIsuTtf4vOA0Fmr02q3ShahhHk-9cGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل زبانی‌ای که خودش کانتکستش رو مدیریت می‌کنه
محقق‌های متا، MIT و دانشگاه واشنگتن روشی به اسم CLM معرفی کردن؛ به‌جای خلاصه‌سازی و فشرده‌سازی دستی، خود مدل تصمیم می‌گیره کانتکستش رو چطور ویرایش، نگه داره یا دور بریزه. می‌گن هم عملکرد بهتر شده هم هزینه محاسباتی کمتر
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/MatinSenPaii/5567" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">این ویدئو هم ادعا شده که با کد خالص نوشته شده. توسط مدل نامعلوم Claude</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/5566" target="_blank">📅 10:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این ویدئو هم ادعا شده که با کد خالص نوشته شده. توسط
مدل نامعلوم Claude</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/5565" target="_blank">📅 10:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5064aac929.mp4?token=r-GU-KOBYDo__oARmE3IGh-NjuM3CD4rXrkN0ZzZ_-gLrnIVjJhyfLgF7hHNG-DwKYX0hYb1afIUGG-fAvA-c8KbGCanuiJ9dmlc4Urt4yhzIqXmpADhMN4jX-lPEt7W5TcvS2du8hvscwjyCYKTzUYRNFxQnVkWWJ4nKBWXcsuVW5r26jm9RXz_BwRt6A7CCmfFBdtB_NYqX2kFtNneU0RHwoEDU5cqmt_nBeCZSdpx0_RX06EJBfCDxYropFZmyocLP9mQBEKRG5cYjJuP2XohLEC-ru32F4NR8u6aCmoCDiIrkuKsfpptM6DTxujXAYcUZvP-p74M284qlxXCMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5064aac929.mp4?token=r-GU-KOBYDo__oARmE3IGh-NjuM3CD4rXrkN0ZzZ_-gLrnIVjJhyfLgF7hHNG-DwKYX0hYb1afIUGG-fAvA-c8KbGCanuiJ9dmlc4Urt4yhzIqXmpADhMN4jX-lPEt7W5TcvS2du8hvscwjyCYKTzUYRNFxQnVkWWJ4nKBWXcsuVW5r26jm9RXz_BwRt6A7CCmfFBdtB_NYqX2kFtNneU0RHwoEDU5cqmt_nBeCZSdpx0_RX06EJBfCDxYropFZmyocLP9mQBEKRG5cYjJuP2XohLEC-ru32F4NR8u6aCmoCDiIrkuKsfpptM6DTxujXAYcUZvP-p74M284qlxXCMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل جدید Claude قراره خفن باشه(اگر لیک‌ها و شایعات درست باشن).
مخصوصا توی ساخت ویدئو با js خالص.
اکانت توییتر chetaslua شایعه کرده که روی Claude code به مدل جدید Claude Next که فعلا در دست تست هست، دسترسی پیدا کرده و هی داره باهاش چیزمیز میسازه(مدل Image/Video generation نیست)
و میگن احتمال زیاد، Fable 5.5 باشه
(R.I.P Gemini 4 Argon. we all forgot about you brother. hope google come back with Gemini 5 Xenon next time
😂
)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5564" target="_blank">📅 07:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeKyVtH45-iKV4g5xV214qxBd3YHzLxJKE08OAnWKfWN6l9AFtoVOBU95pchQgHfTPao8zImVezKAurA87tYwFasim_WmzJmeKh6r-C8BlMrAsdkW2QnmbdrOIgqOOaLpe79kuzi9uUnSXiV371pIefiWdzSl7Xqgm1gHdG-rza5cuASwI5iyygOcrDVgsEvgz5r8zTTkxNOkFAQdl0sOAD9qwvukCbnMan_HzqbmjVFuybzDOG1ycza0G90jMElKFnT9B7mt58au6d1FWjtdPznBLMwpfak2V7nHwKL5IKTY59vxUdLZQn4BdJmGdjWIkXoydFVx4gs-zj-yOYgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله ClickFix با طعم Claude؛ تبلیغات گوگل آلوده شد
هکرها دارن از ریدایرکت‌های واقعی نتایج جست‌وجوی بینگ به‌عنوان لینک کلیک توی تبلیغات گوگل سوءاستفاده می‌کنن تا کاربرها رو به نصب‌کننده‌های جعلی Claude بکشونن که حمله ClickFix تحویل می‌ده. ترفندش اینه که لینک تبلیغ ظاهرا معتبره ولی به صفحه مخرب می‌رسه و با انجام دادن پروسه‌هاش، دستگاهتون آلوده می‌شه. کلاد رو فقط از سایت رسمیش دانلود کنید.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5563" target="_blank">📅 22:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مدل‌های زبانی بایتی؛ بدون نیاز به توکنایزر
یه مقاله‌ی تازه ادعا می‌کنه ترنسفورمرهای معمولی می‌تونن مستقیم روی بایت خام کار کنن و با بزرگ‌تر شدن پارامترها حتی از مدل‌های ساب‌وُردی بهتر بشن. باور رایج این بود که دنباله‌های بایتی چون ۴ برابر طولانی‌ترن(در مقابل بیت)، ناکارآمدن؛ نویسنده‌ها‌ی مقاله می‌گن این طول اضافه با مقیاس جبران می‌شه و انتزاع‌های زبانی خودشون درون مدل شکل می‌گیرن(که به نظرم اینجا باتل‌نک قضیه‌ست و باید به شدت بره زیر تست). به نظرم مقاله‌ی جالبیه. وقت کردید بخونیدش
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5562" target="_blank">📅 21:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsmWEKBIQ9NyGLRET9K5rfHTBklD76zKx1NCi1YcSlTDHuC5gP6Y_N3H8Itj1porcvs6JeLkjDcLz_RrIOb85f_LQraf3TWy7-IIaZs3OOYpfdSABASDGJN2bM5G5Td9a25ytfB1nuXa5xBRKpn_KEH9a9do-e0BzGVAp2t_z0JyV4Y-rExKkUZBfIiMzHYDYBwiLF15d0IPPxc96f8uZ0tXaCvScX2cuyUhL7aKKq2co4ZVOy_owFjsnL1D9pNhPA03IbUkAn-XbK76hGVnyasWlJfEsmcc7mERcC8eamTw0yKvg9r_8EWYO_LZCuPSIt2auKQKJbDtyoOp3IWN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل اوپن‌ویت پرپلکسی از Jev جلو زد
یه ارزیابی مستقل روی ۶۶۹ کیس پزشکی می‌گه مدل pplx-decider-v1.1-27b پرپلکسی تعداد ۶۴۳ جواب درست گرفته در برابر ۶۲۸ تای Jev، با ۴۲٪ هزینه کمتر برای هر تصمیم(که فوق‌العادست. موندم مدل مایکروسافت چند میگیره
😂
). قیمتش ۰.۰۲ دلار به‌ازای هر میلیون توکن ورودیه، و خروجی رایگانه، کانتکست ۲۵۰ هزارتایی داره و روی OpenRouter در دسترسه همین الان. صدر جدول Decision Index هاگینگ فیس هم مال خودش شده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5561" target="_blank">📅 20:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F4bw1CC4kLJ1KYzlfEPWi8svSOHy7QIHBuEkyAKfpHOseFmj7Rtllf3WXYqdUySw_Wjqiut-3DpIdVoQTZbHmmxJ2vrvsbUEVBpHe2wuzh_NsQMCREO-yqqkC_vvSGVnPPhAbaQxec9nWmGbH5ILCHZqIjlzeEYexdUolgJKjt_bRbfVtnYyPuJFIOOeS2eahw_wflJOJgxwxXTgCx4s6QdAqrDnZ_cjFYcTAGUBQTwFcdfLe-zdtjNfr1-TKXaHoVU1QtY93TMnXz_X8RdtLka9i9KVJW4e-tTStX1FEZGJAANrIeFC-tYX5rLLGUkBuxhr9poIXWZGfDHbQBJpCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت Decision-1؛ مدلی که فقط تصمیم می‌گیره(نسخه تنظیم بازار Jev)
مایکروسافت یه مدل تصمیم‌گیری (decision-scoring) معرفی کرده برای کارهایی مثل روتینگ، دسته‌بندی، اولویت‌بندی و کنترل ورک‌فلو؛ یعنی به‌جای تولید متن، مستقیم خروجی ساخت‌یافته می‌ده که نرم‌افزار بتونه باهاش کار کنه. ادعاشون: بالاترین دقت بین ۳۶ بنچمارک با نزدیک ۱۵۰ هزار سؤال، و سرعت ۴.۵ برابر نزدیک‌ترین رقیب و ۳۵ برابر GPT-6 Sol(چرا باید با Sol مقایسه‌اش کنن؟
👍
). توی Foundry اومده و به‌زودی روی OpenRouter هم میاد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5560" target="_blank">📅 20:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کارزاری ایرانی با ChatGPT مقاله‌ای جعلی در رسانه‌های واقعی آمریکا به جا گذاشت
گزارش واشنگتن‌پست می‌گه یه کارزار منتسب به ایران با کمک ChatGPT مقاله‌های تولیدشده با AI رو تو رسانه‌های واقعی آمریکا جا کرده. و این نشون میده عملیات نفوذ رسانه‌ای با AI چقدر ارزون و تر تمیز شده.
اینجا هم به دلایل مشخص نمی‌تونم بازش کنم جزئیات قضیه رو
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5559" target="_blank">📅 19:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwZ7eYH0ggXMNMmQg64u_8KdP1Gk4Yo3Jk2_XSP6hEXaLb2urx_S5bBWSPFO3PDIXg8H9rkfbywcOmFxPjWiTpe5PaVjUoGyLd_ZFJh4ESCG-UOFN51TXH16flkz_xWV2I4aGDmf0Kx-v6UXRoR9gSbCJwBD0vHMeZyb4SO486r__ULVDHT4bcOsAsUBc9bhXl6oLhyNEnnnIc-SfNjRSwpYrUGw8tOIwvAetvaurTd7EjTRybN826uVHWlCYKr-VAK2A73hZKDl7_aYBA1qPPc0AUA5rXcUnA-lP8HatCsfEgZOr_JuBHjLh-r4pjIhpSHoFoN4NpzBHm95Xdrtag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه‌ای که یه زمانی فورک Redis بود و الان انگار وارد رقابت جد شده: ValKey
پروژه‌ی Valkey که دو سال پیش به‌عنوان فورک Redis شروع شد حالا ۱۲ تا Maintainer اصلی و ۹ عضو کمیته از شرکت‌های مختلف داره؛ تروپوت بهتر، کلاستر قوی‌تر و برنامه برای رپلیکیشن Synchronous و ذخیره‌سازی چندسطحی. تمرکز روی امنیت و اتومیشن هم جدیه و داره از کاربرد «صرفا کش» ردیسی، فاصله می‌گیره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5558" target="_blank">📅 18:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OfGFmqh4QcxWoDvj5rBuTtMYFHwUIy1gkgovJNHm3SiRvqaS2qTnlWCksdK_yjSKkTbSgmX7COZppp_r9Eryr21ykmUH86M62asrdJ0HeLqM2PXvFPhyqMIkfhVXlxD4jDPJ8NvBns4YODrgOqYToCd29Yd_KifMmpn8zWMJfXrf1zQj-bDUzSp1CSMvPUG5Opcox41xEiPr8kd_DHRQzN7b0ZCtIwXvtDSRQYyvOA1g3oBjbemz7WqHhZjJQR7yTtywFi9i9O0ACryX-ziu4-K4TA0HzDKC7o6r1HAOkwqWi1f39YAUIpv2J0rKZ-SZRW4fVq2zX8PyPd8kDTTnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من و ایده‌های استارتاپی خفنم که قرار بود باهاشون پول در بیارم توی ایران:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5557" target="_blank">📅 17:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تیکه گمشده‌ی ارور هندلینگ توی Rust
یه رایت‌آپ خوب که می‌گه درد Rust انتخاب بین تایپ دقیق پر از بایلرپولیت مبهمه؛ راه‌حلش کتابخونه eros با «مجموعه خطا» هست: به‌جای تعریف enum تازه، می‌نویسیم (io::Error, ParseIntError) و کامپایلر چک می‌کنه خطای اضافه propagate نشه. با widen هم ترکیب می‌شن و کانتکست می‌گیرن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5556" target="_blank">📅 15:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c6XhDfYxhv7oEswwFSwl0TexPF8Kzjm_z_6pyr7FPld7sEx_vxVcQiFQma6dhlZTFnFbAsZo8URvjbclRmxJJkvWlwZJsDXxfA56WOUK1gZ8sYgSmSo0lwsIUSzorRg1X1VFx4U1S7b07vzIBoshHuyJJ7ZIPWQRPp7Uk_-_sF09p7A7nhbwz1NXGEHp_CChzfLgKpYuine7-4w_89cUsCrBaUlCFQ8EuQnoMFdwRJ-TZ8PAmwnJbhOcaEG77IfteJNbyC7QrenjtAuURbYVYY2TQAOWNZ_BpVmhpEbmImz1wOj5SsPCcwCihCG1KFqlKA--cDSochzbgEiglgjSTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدلی که وجود نداشت، پس خودت با ML Intern بسازش
یاوراج شارما تعریف می‌کنه دنبال نسخه کوچیک بازنویسی شده‌ی Qwen-Image 2.1 بوده (نسخه رسمی ۹ میلیارد پارامتری که ۲۰ گیگ رم می‌خواد) و با ایجنت ML Intern یه نسخه ۰.۸ میلیاردی ساخته که روی CPU اجرا می‌شه؛ خروجی معتبر ۹۹.۷٪ و کل هزینه محاسبات ۱۶ دلار. تو چند روز شش مدل دیگه هم همین‌جوری ساخته و هر هفت پرامپت رو تو گیت‌هاب گذاشته.
به نظرم جالبه ببینیم برای GLM 5.3 Flash چیکارا میشه کرد
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5555" target="_blank">📅 13:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEJmeSGi5na-43qiX0FmJThZvEm1gqO3fy82a6oIwddkptplpPrwru0HOH4P0vHpcj-f2i6ecHM3aC4a42Jpv31P496srSTi-WX-MUpvMTqj_PQHNdlCjzbONTtC-NCdoPn1_x-sQpi71KzdIMPsCfOuQAITujU8UtlReuLzGTj3_eTrd5jzeiWGX9ufW2RFu19bsgnPm-9XZQaujAwDgqWJkrxmI7e8DP3kZNzT9Fc0IQCWnqSL7WCGv_g9fEIMC-5Q-k9wl3AFTPAzy3RnsvN6pPNuWueCqZ4qqC8EcfSECTj936D4-5jne8kjzZAsmoXynKYmV-O1UyodNskzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داده‌های زیستی آماده برای AI
ابتکار Virtual Biology شبکه‌ی Biohub گسترش پیدا کرده؛ تعهد جهانی ۱.۸ میلیارد دلاری برای تولید داده‌ی زیستی باز و آماده AI تا بشه مدل‌های پیش‌بینی‌کننده زیست‌شناسی ساخت. اگر کسی از شما بچه‌ها توی حوزه‌ی پزشکی یا بیوتکنولوژی کار می‌کنه، دیتاست‌های Open این پروژه ارزش دنبال کردن داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5554" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حمله به بانک‌های کره جنوبی با کمک Claude
یه هکر ۲۶ ساله‌ی چینی مظنون به سرقت داده‌های بانکی کره جنوبیه و شواهد نشون می‌ده از Claude برای پیدا کردن کانال‌های تلگرامی فروش اطلاعات سرقت‌شده استفاده کرده. یه نمونه‌ی تازه از سوءاستفاده از ایجنت‌های AI برای جرایم سایبری که زنگ خطر رو برای دولت‌ها به صدا درمیاره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5553" target="_blank">📅 10:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مدل تصمیم‌گیر خودتون رو بسازید
یه آموزش عملی و تعاملی توضیح می‌ده مدل‌های تصمیم (System One مثل Jev) چطور به‌جای تولید توکن‌به‌توکن، با یه پاس و ماسک کردن وکب فقط از بین گزینه‌های ثابت مثل A تا E انتخاب می‌کنن و احتمال کالیبره‌شده برمی‌گردونن. نویسنده با Qwen3-1.7B و transformers نشون می‌ده چطور همین رفتار رو خودتون شبیه‌سازی کنید. به نظرم خیلی بامزست و ارزش مطالعه داره این مقاله:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5552" target="_blank">📅 09:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5551">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vx2LDkdLV85A6Xh8rYFbqPpdAOEsZRzoADOpDF54pxJmOOjNF_yEyybl9qyU282OOhOgbGlYze9CurxVgol-ZO2qpqnCJLs4DFSK8RXGwRzUoYzzp5tN-4KLXEw2xR26xLu92q9hY9JDk3pHWp67gydJg30_QwzmBJgYDznSbJnQyI6QrYZYRGL4CYuj2an6Pb0EH0BdThMHFHkKyaA86HtYKlkNy9i7f77QDnSMV2dQufA0vuYXbMt_dhh4VyFx-4-fuqCYY7EcUZ0nKzQHJ2CE1uQRxzekbvU8xQJCZ3T5GPJBgHfW4eVgIhrOYLYBXfDp1aQmb6cJTFq8u55HRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفیس اوپن‌سورس با Rust؛ کدنویسی با Claude
استارتاپ ArtCraft نسخه‌های مشابه Word و Excel و PowerPoint رو به لاین‌آپ اوپن‌سورسش اضافه کرده؛ یه جور بازنویسی آفیس مایکروسافت با Rust که بخش زیادی از کدنویسیش رو Claude انجام داده. هنوز برای پروداکشن آماده نیست(که نکته‌ی مهمیه و توی اون اپ‌های جایگزین فوتوشاپ هم دیدیم که به نظرم به زودی آماده‌ی پروداکشن میشن).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5551" target="_blank">📅 08:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">طی امروز سعی میکنم اخبار سه روز اخیر رو پوشش بدم واستون</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5550" target="_blank">📅 08:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سلام
من از غیبت برگشتم
👍</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5549" target="_blank">📅 08:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!  آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست،…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/5548" target="_blank">📅 13:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!
آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست، ولی ارزش امتحان کردن رو داره.
🔗
getartcraft.com/apps
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/5547" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pz1Hr9KyTc9sEGyxNd8_gfaGEyqy9PeOydyW8f6WUcHlPbzSlnmLyvyTDTsNbTvsJMKDXlR_uRCTrJSLNbjWaSVPsjxJmbIAM9MuF4HjyfqW2Iwi0IzoDdpogsrIE26MBRcnizG1EiLDqOmkdOOjwIWmiJKkM35AQXtLH12zbmR6exkpbP7s5GZ6UZlE7J4VFUv7zpk-XSpxH9BOZTCiiY6eYHXWKi5I3XMNtCEY3F99mepEsybtcE3Ngx2QV4q1eIfAPmJF8AhDSSwkEnedSBjpCOD6jLQ2FdCDDw0Fzeyg1Xzz8bzkrXL0Df-Gz7sITaRtMIgSIv7XiIwLvyxpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
ببینید چی برگشته:)) Haiku 5.5
خفن‌تر از GPT 6 Luna</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5546" target="_blank">📅 09:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یادم رفته بود بگم. من از اینجا گرفتم. تا الان مشکلی نداشت اکانتا.  توی رباتش بخش هوش مصنوعی، دوباره هوش مصنوعی یه کم دسته‌بندیاش درب و داغانه
👍
اما کار میکنه @OrcaSubBot</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5545" target="_blank">📅 08:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBIEqF4NoGN0FdvjC5P8viWurOHu2mCnHUFvUq9uFgoBz2zbNTTiq6cEr1uQOSBOBnzQJoT2xkxkr_WtF52Ei_qig6cNuhOWZKPEAQINOHjHwmPbvS-d8JcoGSNl0VOljV_7yAOcgxFJkkwn1OGB89khL18AH2IB6HsR9YV_p8NVSPutUR5XX5x0wZm3PPrlm84vlo3sKVm0bWjlxUGrqBuNPycgHKmhf4zP8ThUsNo_6RVhuapTogkq8LHFBny5a-0ez5rWUgxu0eB_njXwIRagMqNtJilk0WlLO_WMQbqPsiDlUm3NB9qxX94FmgwkiIx66S0He99eNHhN_NnSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابط بصری جدید ChatGPT
گویا اوپن‌ای‌آی داره یه رابط جدید برای ChatGPT میده که جواب‌ها رو خیلی بصری‌تر و تعاملی می‌کنه؛ یعنی به‌جای متن خشک، ویژوال تعاملی می‌بینیم و برای کسایی که هر روز با ChatGPT کار می‌کنن(مثل خودم برای چت روزمره یا سؤالهایی که حین یادگیری Rust می‌پرسم) تجربه‌شون حسابی قراره بهتر بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5544" target="_blank">📅 08:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5543" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5542" target="_blank">📅 22:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTvaIErxXvJNjC3Gy-IzAUZMbfHHHhM9Ztn5lv0YMkQcWL84AWyokQcX0kr-Wn6fy8RE0CKF_58dOKnWkuSWiag8qtzMA9IpezHUwi9b6sCMsEuP8lwy3vt6a1NxObLiXQ0pJsBBKZ09p3Nr-L2VzYBPQ5MZRfSDrWyxJvvozs3kKjvYDP5U8gWQzYVvHFwcdNQqYK0CRat-0tIjJQ8-JmTRffWZ6ijpUInLKD1d99_Y_3QUaO_T4j8bX97l10oXR_jctUALXokDTufnfRSb2SBIyKTzs0gD1oVzgpkw8IRly35uqRYQ086dJuIbGsV7zXKdQ9_ZQhiwYnESEwTpFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5541" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی
و فکر میکنم با ویدئوی بعدی
یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5540" target="_blank">📅 15:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم گفتم به یکی از بچه‌ها دوتا اکانت بهم بده توی پنج دقیقه بهم داد:) اصلا باورم نمیشه و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد هرچند خب استفاده‌ی دیگه‌ای داره کلا.  اگر که اوکی بودش و نپرید و اینها،…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5539" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5538" target="_blank">📅 15:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Math lovers, check this out:
https://github.com/openai/math</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5537" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!  تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/5536" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135826faf3.mp4?token=iHK4LY0hlkpp0ZwkWGedoVodEzrgjZWjCEOv0edud9I6_TkhIQ30LvLqC5hgC8xcfUC8pNVXG9uACnhp0eW0LoEKbRF7sxUMLEtoQKsqG8Fi0fdh2Gg2dJEBFNq24Bh4mDr3siebwIpaNqmxU4nFM6uFAVHgzbX2I1uhXS1xoSsjBUITXOqwNI1nbUMYRY9E2rKcbZeNzzTY8tSF8uTCmVooDBaKzMteiv5NCwuHYOjFImHeYCHG0mF4kWR75q_PhocdUvSzmnBJuPqN0tc_l5rfxfeUrYfe9a1peCQNob9719QLW2QSE5ea9TyKFICoSXEnoS9YVgy2GBG-O7iJzKIxIjHnx1_1BFlDnoQISR51dvZQNeHgPAbNu-ROwCNgQI6TJMTJj-gV3RqJGTVk8Meiz7Lzv2IE2a9WQ9sLXQuOI3q7VTPXypdGTLHYSx5gRSN-lge5EnfGKaz5aXZjB1sTc-F053YxNIX7eZx4BYVardN4MXpqlbiTHigrFKsf8Z014jp8Eox4Y0GcHVr4hilUyUNFv8ntDjGNUm13g8bKJhDRv0a3gJTWaFOy0lJwn2JKb1dICDhf_D5P3OT3z2uAp3dpSik9QP0ObDg9wAD_QiMsdAGGjyAEAgIDkgzmj-B6VLlrf4gLrnYwEYURMqLGe2VPie-EKWmnO3NgBfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135826faf3.mp4?token=iHK4LY0hlkpp0ZwkWGedoVodEzrgjZWjCEOv0edud9I6_TkhIQ30LvLqC5hgC8xcfUC8pNVXG9uACnhp0eW0LoEKbRF7sxUMLEtoQKsqG8Fi0fdh2Gg2dJEBFNq24Bh4mDr3siebwIpaNqmxU4nFM6uFAVHgzbX2I1uhXS1xoSsjBUITXOqwNI1nbUMYRY9E2rKcbZeNzzTY8tSF8uTCmVooDBaKzMteiv5NCwuHYOjFImHeYCHG0mF4kWR75q_PhocdUvSzmnBJuPqN0tc_l5rfxfeUrYfe9a1peCQNob9719QLW2QSE5ea9TyKFICoSXEnoS9YVgy2GBG-O7iJzKIxIjHnx1_1BFlDnoQISR51dvZQNeHgPAbNu-ROwCNgQI6TJMTJj-gV3RqJGTVk8Meiz7Lzv2IE2a9WQ9sLXQuOI3q7VTPXypdGTLHYSx5gRSN-lge5EnfGKaz5aXZjB1sTc-F053YxNIX7eZx4BYVardN4MXpqlbiTHigrFKsf8Z014jp8Eox4Y0GcHVr4hilUyUNFv8ntDjGNUm13g8bKJhDRv0a3gJTWaFOy0lJwn2JKb1dICDhf_D5P3OT3z2uAp3dpSik9QP0ObDg9wAD_QiMsdAGGjyAEAgIDkgzmj-B6VLlrf4gLrnYwEYURMqLGe2VPie-EKWmnO3NgBfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!
تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه فارسی بهینه‌اش کردم و نتیجه این ۸ تا skill شده که اُپن سورسه و می‌تونید برای ساخت ویدیو استفاده کنید :)
https://github.com/atmirrr/persian-motion-director
✍️
AmirAnonn</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5535" target="_blank">📅 11:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کم کم دارم فکر می‌کنم یه نسخه از خودم کلون کنم بذارم هرمس جام کار کنه
🍿</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5534" target="_blank">📅 00:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RizVF5ctX5spXD7A8gB5V2sdVMZid7ET2z3HabaFLIA43PaoOVfS83YcDLz-vLKUTC6JYKbQewc6KggCPfaio0bZYTq543DD-A2Jfv-DzVTFW53yGa4zl-1B7k0cAsbwg8HUFKHAFnBDuY904xXHB8yhQtvgj23kBmXHGE3ggZv45K6rtetEywWkOdT8Gu2RfXR6qfJNo4P4Mpj2xqFVUM90k1BfsIcUtE9Mga1wvGH_SpaaJzHLBZrdslPlNdP6fsQ5nWmJLFND6WMRnakc3YYneOiKesQ7FnRFDeftqoEr7mmmhV-KMOAlgAjjQOiIkc3SBKFB4stJiI1XkdaYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن OpenChamber؛ یه اپ موبایل جمع‌وجور برای مدیریت سشن opencode
نویسنده این پست توی ردیت گفته بود اولش فکر می‌کرده پست‌های OpenChamber فیکه، بعد از تست کردنش می‌گه در عمل، به طرز عجیبی خوبه؛ جایگزین opencode نیست و همچنان opencode رو روی سرورش ران می‌کنه، فقط با OpenChamber از روی گوشی به‌صورت نیتیو به همون سرور وصل می‌شه و تسک می‌ده. برای کسی که opencode رو ریموت اجرا می‌کنه و نیاز به اپ موبایل داره، تجربه‌ی تر و تمیزی داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5533" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GSIkZhGrOooZEkluRYjgpk4vw_hxrFtCZUpPvS4Qa053reBCWQ0PkzlVAYlnPPUK8pbJE5mKjfNdX1Q-FOjelLjlxZnC2sgZb8mHu7vkccPmcVJtv7zm_wSFTi1Xz9khZYTsBawdzAYS7NiM7D7J4mT1xGhVVX_U0aQe7Gi3xwXJHLESUgyawKiAEpYQnKNgSVoSFaqVa5wwmeTKlEMsj5dAKIhsiefzcGxi9ST0DjRIITaxoObxSbo1yr6F-vo3wDn20E5VCyWiedeXhsT5YsQRdMTUB8sQ5IItNIBpb1fJ7JiZA5a97FY5HaLTHMcUg78NS9iX6ayjzwob0edntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل نانو بنانا 2.1 اومد روی Google flow من، و افتضاحه. اینجا با GPT 2.5 مقایسه‌اش کردم:
https://x.com/MatinSenPai/status/2107527090019131503</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5532" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینم کانال تلگرام یزدانه پرسیده بودید توی چت فراموش کردم بگم:
https://t.me/antimatter0x1</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5531" target="_blank">📅 18:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pHDlNgNFYpOEaxiWp-hxfkT4qgQlW-AmoVoFScfd-GU4d27SA-OOm6SkPnPjqTaZ46g2yPw48sNhQsw8puf9F92pvtE3Bp8CQn5kXXeSXJidqZU4RVZ_LhwxLlT-0qTOIOSnpJWi6OMC2tytIgSm1rXOy2omDj7WDQcKC9aTVCIrKtbznyoKh77wAsavn7eAzuKNxxaA8F-0mh5BbBtO_dZGd8mT0fI0XC3jQrHwMHO8bWH6hVikni7gCNOkTfA6M0dcS_ZEXjyl01Miwp_GNDhvoHObi5Ucwvn2ymwiJDYgLzbVAS62hnDp6jKOPjASpM1CTgFC7BUnzaMoKF3vZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو تموم شدش
می‌تونید از اینجا ویدئوی ضبط شده‌اش رو ببینید:
https://www.youtube.com/live/nbOls9zPckM?si=xnkhmSfdlmhENs_2
توی لایو توضیح دادم که همین overlay رو هم کلاد توی 15 دقیقه زد قبل از لایو
😂</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5530" target="_blank">📅 18:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">لایو انتخاب رشته و دانشگاه بریم یا نریم برای برنامه نویس شدن؟
🥸
https://www.youtube.com/live/nbOls9zPckM?si=dnW0hyhkqq7wyJ4-</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5529" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان) با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید: https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5528" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QSZ3svIOeAJ1mArsvxBuRFyuD2vut5bqhj-IFW58Ns0bbu_6UwQz4PbPYOTP6nSDKOT98dXafOym32cqsniRpCMzRXsMg3CqWQb8rgg4l6eYqj8vYkfUmHLVXuBN7YcWpym-_bpyAYDBbkRB1z6FgO3KATdi_J9gtu61_V3j9VLuyYqcfYLVgd45Jb0ZnR1QluBiCgsKmW7p4YItyGSNTresn79dCT-rqZc8DPcEx_p_lRfo9elTNGZh30fBMi7eC1bOJou_Vq106l9SH_AEubQFhrzz4EbYXzkzV7kF90777JJxjIozZlkvNmI0nraKIzZXmDO6jGY4fLnpaeQc8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان)
با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید:
https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5527" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Matin SenPai
pinned «
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:  1. CDN/WORKER with ECH  برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال 188.114.97.6 استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5526" target="_blank">📅 13:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IZiC5UZOfkiwZQKFsNq9HG-BSz5Q6TxXzOiuXwb28dbKP1nGMhhUuHt1NqqzD8t0dRgVgJdDE7jO2Fx8anlNJA2CmYHu-4XncpWj9WlGWwLn5lGsswlvQNLOBDfAwfIsuAgdRpypqQ69hEToN1GSsf_aAwhQoVQhpN6lOpa2Jnz6ptvLydAEJ_KbeIvLyWDCHqBwyzURsDpR1tpSGujWjBNYM5JS4vOu7hOIjO3OJPPyVFpuafEHtOBWmhErw2I9i43anLh8G-gzpGcbHhnkiGfi0SGutXpW8raRcXRnmLutx_MWzsGgWEinTj0cIx41EBvnmFUpyiwIbMvbRikN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتای کشور به قدری اوپن سورسه که الان سایت زدن کد ملی و اسممون رو با شغلمون میفروشن که مخاطب مارکتینگ بقیه شیم :)))
✍️
davodm</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/5525" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo07xrsPO_qovF0Z91Lr4BMWCEEpsFSKEz8tOFKmnyYDzduFHfqk-KuzwTXpsqmOdPTLppCQmYxNh68e8-eHlr0jt7p30Gx3uUg-QxTtRoe51k1VlOeYROgywrtRYa9I8Np4ZBWkzNDPAltC6fgInUGg1PCk2JWTUe7ZTZJ8IhM_jPFstY6q3CyV3aJ1QWPAngf-cfPM3MLRxPKmgvPd42OUncp0QzhilRYElpE4qqub1x7aoe_WfzRXuFCc9Ss7eHBrqAlQr6VL1G2txrcD_9u6gSh9eeDH1W0IUFE2wphoIM16T6STXqdqsI2uAz2_jEachSD3Vm81NtNiCQ4OnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KKjG3YzLrH7Yb828J74zYlXAVLo5KZTa9_JuTY8NqFa_7-6iubxZCjSeDb-J8tY11M4BTjEGMg__EphpHrbGAC4yRgITHryl87VOOo39icuJZ879m6_PhFFsjOt3Lk9x-g-JisuB-CNsQwDiqiXfS-R6_YpAvRUhoX64h1bGi33hZpVjECwGZVxkTpfuxjZdEgpfBnE_d7pdF15UpZf7cHyyFnkg-M-fKK64pA8x4k-WIKuoawYjBkY0G7k4K96mk9q1kv-dUy9FYSOxG-o29kYm6urC6BaGUUH1k6VEIifG4G-FcWjlL7NmgWwFfWT3TYRe75k865BnMHdOapCDgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gIqoS0Qpj8OdM2Um-roydLLtfhFzcYpHdA2Iy6k11gVvUj5ZFbdg5bfCehb8ZDP-6PeAs7BacovmvoEbGy5ZkJTXthyTAhc7PmRJBpRXoOzcxauZxF-yOzCtv9IjYHTTRcOCcH8iwqsZFe4S7CFZ0-xec9UjpAvdoVpwaf8VOBZFlukFFgBrEIo0GcFvcuMBf621gh8eYT3Vbw5xksuPIQaISkTt-SFYg8wX-d4As7S4PoBqsGTiw45eg3bds7OE4CK1ntxtIMtf_FxwVmXScbCiXaUU0vRFGgIFXYgSEBrAcWB_BZAJ4nwYSHAOdvKCZdw6Pph672h5xrclKBwqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QlzVIyi64jT3xMQyBqbPuJzb14VfY0ADVTdXJ_2TUQ7GeGjndX-WcJU8Njoy7hnLQgrM_zOkXBYa2HTPmneYpJhpkjbI1TDbUqKAKqRc9DvotFWD8XTyJaHt6pM1pM5uFKCRFFk65FSRs-DC0J43Inpu-Zd_sDVEo42URZNzRZMEcvwbPjw3IApHEn2qUS4sI4SHUajZ3xBJ4zqOgRc2B3va90kl52ZFIhUh3Mjy42Qeh9ZGOW3rJOA7FsiDi1qqUkVGX2i982fYiWI75lDjCgddICFtLGpakwhYOc5yH0SXSa7kVSlhspDOtJny_xEgMvhO5kW7yw5uIzUqtl1RGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lfp5VNKAIP2Q5OzMszOGp-gzvvD1F3mNaCU6XKAt7x5tp6npkdOAeLv3qzgbFqORBOnJtrkGnyRVEPracBuIQM5fAbwn6XIjzIPCMq14OJUnP68I8ZCz2jlIoyRd90abv0NFhqa8EVmj9TDFcd2Zsn4WrX1DQrBWiG6i9MtfkXZ_uOsEcIMOpNIyWg_fp6xFfJOrB-zSAkOqdBMV2KlRba9VOE-Pj-AV9fsxX10hcG7a15S0Xn-V1fH0HxFOY0oslwyT3w6N2hwgwbaF4XCT7_QMfkNrL6dAUHYIUMC9IRQTXcpt8nBdhgmn8SwkjYUiqubayYhrL6cKmhW9SHgIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AmbEveP5JgeBado-SojB11UQUX5OkH1e-VVyry-wf-bxeEEilPPWvMDoq3nZfMe6pCBOQCNJgXHsKs1xOWgagK1MxEI_-IC-njKuapZSQdOKSv1skE0K8BEHljLDmOCXx2-JTKn6ukCwgAX82MFZFLyRGOes9kAAGzehv--0F-r_vqJqvcZUVWN4GcKr2703OFl6-7ghUkcaf8H8mCRuOKyYZTlnMBAqHhx7XnRp61L0omljLkz00a2XqJ5W5sF5Wa8TgRc37mzri5xt-eaS0rp9yO1AoJueBCDGFvr_aBp837NgUM3ImnSp4VEmyljrG5tEYn7bNSizVm0--_23_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HKQI0zmy1FQ2c5Gmms1r3wF3hh60NXdMP9lybTa50n24e8-8xbSI4Pl8wi292zTffOFMMNVnsD5GymAU-GyniQl0B2bBt59xdmxNtJ930HjhS6U0-SrR_Cv37TPqLWTij-U0qCJFHsmJ9ccXDAulSP6jrEEJhH1TXtqddeBw1pCn_pxTq0YW2eeFiPKV5ixrG6geGXy4O6T2Ll7CtUl4sUC0Fxva1fQq_RkpD1f6q-wFrVJW_culVjI0JLiS6Lz7pk_mBCfmGFvNBpGDL_udn_LkvobWzS6V59eIgKzinE4zy_fFfKpST1rqaE9sF-fyhxI5OYY2TgLc0xz00vUccw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YTJpNjq0-ElZ02USn_N760DVB2gd56qy9KcHfomYj6YygGF_usQCvLXfBZw0Qe3q1RrD9ftay7Yvt9X-v1cWya_ZE4NrJXfBJIrfm6hDRDL07dSA3MfbrOhblZHxutSZa7Vik0dXXldPv_Og0wAmj7xQe5g3jLCe6PMlDp6fqiJX3nDSdEQr6juhz4brn30CmOGa6TOdsZrfcaJ8Us0onRrzJc47dcjB-sBMaSQ6nLTVPdgRMMAWPrXtpeUSyECbAuDdDsV431ZULIRwwi_QJfx7glS4voBu09ALUP0kKK8ZsKkjOQd-lzxadmxDaLekOTl5ve0EqR6KgOszMBu2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mI8Jldtotvcb_Ca1FMeKhk-gRp8qT_TNVxlxznjAYt95uQlr_PjhlOtmpzXmSrNBZiKKmg2dtlUv1CTnsrggZcmkrPC25kGPghHLZvsEdcgETRdqs4Tec-lsY2Xfe60-LfRSaENFyqrAU5i7pQTmD53PF63ZazNKZ520eu3VD_WtcMEYeGVDZ66qMIEGb4ckCn1qpw4gHUuL33CiJnbueJ_oXh1Scr3tpe_9NM9aAMfs8Hd27KcJWlMJidtYMKN0tJcF_wtFlWk1R2pDWyKTcdswhdLbP-64CCS6CseJwrTJHbfbk8IxsHauriV09UW5G5HiXUr8eyBjH-VZ793rfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uX9hhf20W8hdFjcE4cjz9BUAHZYSexUbivIv0lyHr2A_T83Mru8hO0o1ZLepU_7NC1k5yiegSl0tMi3sjG8OAEL_rK-BewZIAWgcQtM5NF5s5KZJZVOiXj1A99N1rGWXAKc0-dlW_SYweGVHm5vmqTzPvwUpGLeEI3Cf0-ZY0EprEVutg0XxzhU9XqFnOnV5DPQRIa5g4q8P4N0BuXBFkflFMqfRtiw4PsLoyB8ko2Jhc-sf5UezsBv8z7qzADiAzOF6QZ4RzbPFlSYm4KI-65UZQIxamw0192VXLzTqJ_hoqku7PSIQdgLDC2K-DsaTavVAr6aIlHEeH0S8BI5-sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZQrJIUQ1uzqmLeDRjKxv_x4IDbVztv_dDVkYphV5Ulr3KsG7lGla9bmrDN7l25mtxoe8SuuYG9fknSVxNTw7_fGw-tN8pU1aPhJolAj8qWstFmhk0IJb-SoEzL6gGwm1bxsTGaK9kJs_XOmykiPgifDccFtA4S9OKcebbdeIm6U11nJPyIE42LqeAJm4s-G8HN5zgLoysZ6jX-QXkh7YO8WV0Pee7rtQyzI27tIEReGrizCkrIMag6yFOSy4iq0uUL4QoEQSpSnwWkr4wifvL5_QkZ9y7KxTckrh4pdu9AIZyXgJgX9hcWyr8mfQxhqKzJ0-R-vl7PK-HViAY9Ha-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oLDqGH5b3sjbe9lujrzHscWhph8GcURjYZtuKeWWg-gMwnpWfwzTCZ_NwYRuHwyEITOwPzjbLaoEDqnCKZTiUWv-nDARP4jlOaXXZTl31zdArwRU0LAEklcq7Ud0OpuK8bNtTbsklEF0ucoDOCzwrGPBHjAQy-19t-R8GeDuBckMHuas8veP78RyHvTisbpX9pqzsKSgmKyaj1Zzw5IXp8cVd2JHbVVvE5TQl963ZP1X_hBs-nS5jt2tDNJHKm07BGCj6ndG-TmE3bttd2LqwmrG46ftFjAQEM9Jn-GpNS3BffoeTvnEPm35G4AOLW_kqDwzIOZoefxQWpzG5lqvrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FeZ1G2nD77atUj6XzcDRDTvZEHTdrcOXGahQ9yOLjku8khp_q-cVKR9E01wtsI-BLPmKw29nUpUSGpdN_xpMEGBrpQeezt1KpqTg7rfHo2IJWRLPRwvTYvl-dxzBAjqQzxkR5ol8MOeyxC7HI9nkocuHvp0_7KFcg4zpQBl6vNJZVivbbktNR_YR7_0YKXodJRb-aFHM1LK3TUEw5MFTq9shRy7dnKhE8z0lrd9R08zR992ERW--dAqNwSpjAgMWOhAjav4xNsUFdC3TtP4SCAmhfSMMOIhSCmiQEas4iM9WyAFl0mzLpcNmEH5Flpyou1i1KZdfuCI5fJTIqKZksQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=CoKucVMxFbDKe2uIbJ14goGstci75UFSVyWFm9lalHjP63DhPkkfAEbdkTwGLyn17Ui53Y0l_Ninc6eUs9JIbp-BD_wORkVB8GTgdTQ1CY1Ls5SLr5JTArpzOog_yxJoPsrlnvA7OggWKzHTAciDrAoTEJVIrqPUI7d42tRSFpwmbWol18S91t7qkDuxrpaa4EM6shZYLUR9EikejlzlK43wkID6YU5ovV7dHxk-C0PwAg8wMEyeRmHEL9_FRenaeV0Hu6-gxNkCn7mKhyP0d8DWvVGL_QMAbqVxAZjr6mzcw0W2BpeOPP1peQ-tW-7ZKrke3wUz6D3firWS5soAQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=CoKucVMxFbDKe2uIbJ14goGstci75UFSVyWFm9lalHjP63DhPkkfAEbdkTwGLyn17Ui53Y0l_Ninc6eUs9JIbp-BD_wORkVB8GTgdTQ1CY1Ls5SLr5JTArpzOog_yxJoPsrlnvA7OggWKzHTAciDrAoTEJVIrqPUI7d42tRSFpwmbWol18S91t7qkDuxrpaa4EM6shZYLUR9EikejlzlK43wkID6YU5ovV7dHxk-C0PwAg8wMEyeRmHEL9_FRenaeV0Hu6-gxNkCn7mKhyP0d8DWvVGL_QMAbqVxAZjr6mzcw0W2BpeOPP1peQ-tW-7ZKrke3wUz6D3firWS5soAQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mlTZs5WFOFGVG0Ue4T5jqEoco81VALoh4zDznYUvCW2fBkjt1jM9LYrfNFXhHCAhL-3eb21S1onUvw2IeOKh0W46groXy-76IV_L7UcCo8FXM8gVBrwL5kcnD9w7om0oUpYzv8wN6-M-w1uAgKQuiLMlQk6eZi6cqK8zwwTMhFE4i3bDKiNbaC-zkfCtFAlPql-6B8ZhiVFGN9b_-ytV0EqDzoZVYKf8QYlRCDH0TlMH6-sM-3VTjsMu-nhfHvMjsRHw3UR6LRci3Q9kLrLK3exn1Fb77rLObpOAzgr7_7v2CXFiE__vR_BaFxqqT__GpMoYel4BlxlRnlmBUgwdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NeWQHXvR1ac5sYjHrHGz97gCh-stId_132gzCOyRxjm6AIH43G7EwLQ-yj6JycenxI0RR7xTGZ-bYMMEk-LMpXCzO3ISAVmP5SvNYVbJVZFyWb7TdTDFmr66io8yBeKcf85tG7OidnXbbpwUTbenPrXyf6i619iWa0tM8iHnVgCTrJ9IRAvBZ3PmxstNI2caPA0n-yH_mQWKqnFiYeFJmspwo2oqVhevLTT4DV8DygkzHuhvYIGkb1BRmqEaPU570U_1_nw7xqf2Y3LSWg7OrTXbxa2sDHD9GKoBWpNiDb8BBmVRK724Nif_zomkkQwrdIr9KN2EMgMk77ta1QRihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UD0n5R2vF422pAy2HDjJSYaMjVJd-Cp68RbD6XyDhVEePaD_Ip2HG-1EzgF6Dnk00P8DFd-EYmch4vHhBDFrKd2LOhRlWxILvjkPjeLtW1KK-tLqw-nTvj1FCbFAEVn4wWm0gEHm-9KqIdcnkyiIE8JwTvx4KUmECKjIBbchcWigMRAmvwARfrlKsxKR-XJYIRXzwvSrUEq9hC7b1HIue_gIf0DjM9ZJ6YT2tfL47zi6c8s4tkPccsgqYuvQXdfL3Kl9lDuWexPEyOe3tEEUzJv6qlvA2C8JYDk104xKWkPD7XzVEHZAnTdfzryendIPo-piaYRAAea2OdF8ZaTxwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/syse_UO00K17_Ux0DVRuiH-sKviUHRn4s8PhhH6b6il_1ZvxVhB1U5tMLMfG9BfmFV9fvmYyJosdFSbSKetg7YpqpNuTrcBzPsceeXfYgP6nh2XcQWfLeYAlHaONym841qvzuCx7XBszt72c5OTCwzOvzob_CmbzwrTbcneWwSJFx53QS4diMvOOFvblVa5E1UNLJ2vZCVLU6PNNoY-0PvYaFwZ7hy4r-wF-nu_82_U-Si1bYmxPrdA3c6QfGofidw1GlDLwlvPiYQTEf3kNQXv18F2Z65CwiU6wGutdRdqP5AASbQ9rECSX2iFG2_RAIE6BabzG8VqG1wvDlNES4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7WMw-Tua2PZLrcBeSbX2QjMw-KYNHAugoEUZgkgJjlFg7-37hjN37Q0StA6Dc4CQwvfj3FL5bGVxh7tX_8dWf4VcgxJj4-2UqODfE255XWXtrMBLvyUnVoQPdc9Q998Wom_rY3QbSuCggyIYfP5xQKOi0fm_PWosYxw6KgUPSZUdlDRfGH0BL7CPL8eOwgbel8l6E0_o2IdmdDeN0ExV7NwFFPiysCA1x7zhC3-Oqhmf_3ekclIK7HBVFbUTYfghDDN6Qai2QW_j8qlXO2VhHHgBc2rSPLcRrkNYfF7a40s5SA8ug0kNzTkGJ2ePeKhc5O-M9LLgTppafUtFI10ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gQG_jZ7-lXryIBOEj3Sx1P9znBW0A0tiN3SZm6SCQHD1kgVna6QTWwa2VI-yuy_92HFTK2RdqZo5yRs6ll9PABQRSw3_beyb3-yi3g2YG2MFj0A7mwvfQXanXp9ZjzwGMOlC9sJH7rmIvCyZkO_2SKr5jB0UyBEPyxrL3Hd_Gqy2Cyyi9Xv_ghSJuTF7phxJhKBDP-0iqwVsGm1dz7RueymWdk6t7hKkJeE-kVR0Ld-JqCtZSQclo-T6h2-mONADNsDsb4fwVYh2QXR02OWmjTD6Ic-WJiYfFibFAxKvjT35vbt8ujREG_nuGNFXfC7tXo79ZHqR7LIoHVgOywOMaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzkHDucgdk9CQSfBMW7SqYzIJGRE7msY6_RAbH17csFoGL0c8aCwKVJKH2WdvLPuhyhFfYXaWfUlaIJOfgcSgxmWCEmYSD6mj-WRjUAXtA78vSHW3z0sMiR9bJFPBkUSdr5Om4FDcvCB2CEOKL1RXzt_rfxhjanO_t5qjgdl7-R947T_y9DgBaJXhZ3DZNDaWyBzhg5XLkEvUtnl394gHE9ARlEuZZ4cs7qzYXLwbkaG--iBkbWeYD648y-qojo7pbu6p_WBjapf1KnepqNOyacvxt1xTwJ9i2PVtNsR2EmS6xvT1UAKnPhwyNAAlI546EkmB1cbbX_acUYEE-TgmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0S_Y8dtkfMkCYobauJH_IzJbYuPw8Ic1bGtdBoNjbaggLFGBYmcH81_l7DKrg0uRciG68NP_2SaUbjJ3fw9BrW74zh9M8T51AZl9bygW_gyuV--0tRI-qZat6gbCyfSG1ly9xNaCRa7l-eCKvyPA5O7M2n8B2B4clP8WTpVj3-919FpOnoYAWxtaaiX9PjGbSDC70i0MQSsARPlttIMrmJOSyf8Aupklf4lwcTFMamM-w8dM371T_oqRaAKUvkkQKsCtD4JgeJ9TeDc2qb_JNDFyN16NmGavdq9Xb4YMzf2rOLjz5QxcjTCSC15vtMukk5dQsrzrUpGf4IKie3qcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dHoebzFsoCVS3BB3U_oc21_UB5ex6he9QjjYBnEqU9imrPF1Y8LHmJQu4umJmMoX-h9inqPROnDOh2nLQnhnooOX-N9y20BryFPvDWIjNLg6CFjgkD2k8RHvzfLYCv0qL5h3yXjDVE5PwevyyrCGiAWoO4zdlcFHbv2kwUb-PUV1XoXArrHPz34HOf-8rLwjRlLpfDQLYPOHJwUxJyh8kWqJFsb-wyYS2cWddVhsmdIKeNv9mbPIluVvno8u_beOEX7ZtcenWyzd37fjHgJokwy5MyVleMedM3RNFXB2cVKQ4I7Uw2wBQxiFCA27Mx-Th2lmz35Qq7AEX469NnprCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LDQ7QGYQvHZuePIR2lKgiBS6GxBMC5o095HsqL2Duttdo2Lhdq_GEvS4M2x5oHoBZXmZQAdz1AQgRm4Og3HeJlZ7EumFFj7jE9F0Y1rdDAz9yg_jYz-Qnes-P88s0Ts6xJF4M3TDwKPbVONyA_P_m31aPDIfW5zGSD5yRdaU92HjFDygumsnZZfwbRw2j3Du2oPoK7ya1plfbnBQLajF8DtFHj3DCLr8sTNKDGsCla7OGBaTmIJkNLm0-sDUCtdVxiPbdFXKQlDTEiR85ksJbTHc_IF4fAtL64BdmmjDIaCYBxDfBMj2u6CwPNUvUHZ6jtpgDD6hh9f5xqWQ6NlB1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dLTugR4Ww6lchFfparl7yILq3hm9bR1YHB8qOttrunpwdwYdEmE3twGIrd9kUPcB8krvmFlJy9_O8x3QHuKX_MR2wHZ5FSJckgbcMO9rIvibr3CYhuJxniDjONWF3Gei2DL8UHj0yk0UXi_7TFdXpH_lvspPTC1kmsqEmDJbIaIcQkmUK-VCXITN8PjYFvRVNobv7CRSJMdN5gDB-1xpXneDPHCVtAfR9rEhy1E-kO0VNRgVi0Hrp1nQv9k8YjchA15xAt_3DQ1RQ_oJceGfE8mbMZU16BCxfODjvesXa4UGZXm7yp_GVI6KcZIWWVcc1u1ht-BDiOvaM0v6K7UGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmHZQD3w-9xexAMmLsbQtwZTW9JcaVEj-nO1DZ2SQybOPSCtOaH-m6e0MYQUmbM7LUeAgCrjWUL6raz4z2caTQhooOF1te9bXXGiyNO18aA7DmMi2xGUC1ArPVamP_sl2znc9PFhFEW2KIrBNYrLeyPG3HEuY_quOojbOqAonTtJZAzb_EzAR3GqFytZUDXb_801TF3tw97eLxHgrA0WZ7nna3KkYdQrkxpJQDL3w4-yWCIAgpPsX_8SahjdlV6bOrrEBhBYtQix7PnIBqMzbvvZiOVpeLr9Qb0kYw_XtiOMNZ5k2tO5pMy4NPLtD_q5dLrxvfvJNUDIwmNzWvvzkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f97PNcy74nqxWz7nYWog_4y8Ww0h84jXn_UcwJmOXMPW8aY95tlerH7V16q0DmHfwazatWByj2gYInUG3rYzowt0yWDsRnpluGmu1Q6EXPw0Jh0f47VHTOCyDsVPt3b1wY1Smu3v6wu0veG9lsmblHdHTOCaI49U9jeOvL7LJveLu7EaPSiolqClaNxdAIirPUQ4HwOwcJfBur9FffzP1FBb6Z4TbSdw8fca4FQp38UpBJswTcNR-ObU9aJS_aiMFvem21YUTmXcbIl0OKaNi3fkWUvibHuTgJbElD4Fjzqi-YRSHOZ25xp9G0vkfnGDKAi4YEkNUqxruuJeVhI-lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BozxoqjoMXTZXwzPrboj402VO9o0ekKijQCrUm6q7oR4x947Okz2sjHC6z0zHChKWdAcaHn8_yQ4U_O24s-mVpCxepO0vK2Dfc1Fq7x2gFDwXRoRxwS215hk7OfFMbTvhS19lzveqVGcQ3eb1kI5E4__9NT7xQbPFTKvBxaRG_6Zf90YTOM3y1Gb-RzstZHOgRQl-2us3k1s0rhC6BdeiN1dGjYadjQCRa4IFYcSqukdz7cmI19h4HJvFQoxMAuNJU3KeInbZJzUgivcNaYv_rv6aHXHpdCmWYdOGnKjmKKEZap-EGQApr12lVbLHh9n_ItzEKZWWVCyRVuZo5Sadw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
