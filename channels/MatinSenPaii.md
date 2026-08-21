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
<img src="https://cdn1.telesco.pe/file/r3yWu6DQG9awkllRYuiXa4ojWKuuoq0A1GZ4PH1hlyglz1WjxiThVhCwMLc3riAEjAmfwmHvmOlesb6pJRcfDWb3shP31qVSTMy0lt3EZ6RH1OKrCWaFDdzs2KmhDfN5h3fbgTXpLiRaedoPwim-zmhEqcDxIXukpc-6p21Zy4pIISi22oaTTncl5Sdsdp7jucYgaHCci5HPSM90SIZAKhMVpshqdGutrxTR_HPy7crvBgdR74Fi0KvOgFDMgCQolJ6XJoyDlPmWn9Le5AidOCw05hrfQTZWt1236UMuPMz8i1-7Y3fTYpDXF3mvhONS9eoHfK-lfc6QtqGjY_fgqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 23:14:41</div>
<hr>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/poQ71z99zHIvOsFwZOxCGX-UOLzL8qGtrO1B9A1fb139pMyWlUWKGw2_dO2fcimm5eHebiI-75yzwHASIpJiWYzaKvCcYbhjcOrQhHpF5h_C-eil1xtokFcdbI9txOTfAblrwQBwF_sXnoPjmUE1rc7Ce7WqbPK7BkXRYbrzaN0dB6k9VvFUsTTwu9jhzNwC4otYKUQlOgTkWjVgB0D_5TcGRk_2WmW4rKtZ6nug-q6TlgnCtr3jrZ0oOdHeRNG9IE5dFMNdCQVpgWfVo5n11X2EJmxZ3RSncM5-BDVvHlhDBlG7kxRq72o8ogkztdSgSqiBS08JrMfGjB3GCad2Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DQ9tGrvwyrj2XXkk34ZasWVXONhS_gLHvnlF5uq0g8m8WeYzPni1mZiSsgIc901cgcqs2mxP9WjeeY0EMbabHXs-eZy4hZE_CvRaaRTA5ULYUi1LzoBdappOPNUFuFdITvf3fOJhaUnBl7xS4j4JfDIUjI-LXsxaCQebS9jAB44eutwkKIhM5Pyft28nnEGSFaP1CTvFffPUFBK_u3egTV1E7WBUhg4fIE5_R0tu1W9JfNWt848dkcBYKTWvplLQ4_7mBcSvHHIOvt2arDbedwjihKkEOvStmpC1bcCSkTSLP4lDxfZwIk2CoFTJ3GNAk0YM9ybP8sMUZ-p2QBl7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jp-8IItaaeiWBDrJlqfC66jHqRMOnyHxtyphS-LsRTU8nGKCB68fXcH8qItJ5zWO7xIZDinKRq-ZzQYMxrnunUsDhfhY05lp0_-U977Gl3kERmNU33O6T8lsMtZOUq19P8WI_mW_QVyllNbJfrbHNEj0W5y7BjSpT0F0SjmG1CH9BNKobHGCgtEQrr2GdVUHYUwV4uPPufqHuCBU5TqidMyGBYFbiC5YahrytwV3VmIhUpJXYPvP9DuUrVyyl94GT8zRQLoW4rH_XQBRlllR13k1RpyIfLlVqNhk8to6f34n9LbTvxOY7oZmDyKYoIP4Qm0hBXp_4ztbiWqBmhI8Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/5008" target="_blank">📅 15:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/MatinSenPaii/5007" target="_blank">📅 15:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lBZfo6dltEpCUvwMa3lYQU0phKNvOIlxB9IlxHV-CZqQw2yrSvzlXJuQUq3DGPYVjb6OQw7rAjGPJBLEldxYj53ELwNFKPKH2bBs030VznipHDiQfSit2GfQDnp8JSogic7MK-dOQOyjfkbutpF6x5a3XZnafD1aUsYqlWlQD3zfGpxJ8n85vb19vxQIOfQqRcgTIK9br3e3PF7No8AKJO6yWUenV-fPEA4dxQNBlCeYW1WKQwuk_RYtAUjyfzXVCAtPBE99vkjC6QKv1kCR5lDi-DUM8c4vPRz4tMzR_dWK9_bA_hPse23O9jBg6oOyJzT1AsM-EflIgfsDYqC-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fizSHnVMTkfu2i_FBler_WzPgFAv3OjCUWRLhw78zMdJ8dER4judQfHzXzUy7brh1svtnJp8jXPoUJdcGMLktjC9H-f2Mj35t51e1oE0ZwxTPu95Q6K3vRjdBP-iG2TF3Upbx4VRx4rfPY9SFOV0PJ1bDu_U00aqzRK3V4LsaV8rGWsdoFP5N5gkMKNeqCusjReZQrhSKsGIZdGvIxQAiw28M6QGxaHU2qZvu1dPHCm7F03h7igTpnKo1gtw_TxQXtqgWbKZF0ra4s3NU7niwApbDig2Qnu6MI3V3Y2tV3NTKLT0sY1tBvZ7HcRFLeVISw18fdKzhCUBMvsLqFWtRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب هرمس وب یوآی با یک کلیک
متین سنپای
بهم گفت که Hermes WebUi نصبش سخته و بهتره با یک کلیک بشه نصبش کرد برای همین روی پروژه اصلی PR زدم که اگر تایید بشه از این به بعد میتونید راحت این پنل رو نصب کنید و ازش استفاده کنید.
لینک PR:
https://github.com/nesquena/hermes-webui/pull/7152
میتونید روش ری اکت بدید شاید تاثیری داشته باشه.
اگر هم تایید نکردن مهم نیست
یک پروژه جدید روی گیت هاب خودم اوردم بالا
لینک پروژه:
https://github.com/nesquena/hermes-webui
میتونید به هرمس بدید و بگید براتون نصبش کنه
خیلی ساده همون پروژه اصلی رو میاد براتون نصب میکنه
حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/It8vRwYzDhbKnTr10ASuqjFP-EGhZJ5kYVB8wU71HSFZSKM6zypWsOwsz2TEZZDNN2Dkyxn-yh5D_CbShaqzEC1QcStIUANSTBt-e-iguG4-N_5SkO7JyJEX7FhmkpXgYuriyqzPw--tyDPGxFaXhXRHNlVKUlDn4fkrAd0R2USB1sY4A-Mx_aLOuV-2oG7fSQ-Tilb-mzXL10mrgkl0c-lSBG71uXWvsm_MSy0ofW5iKEhPvJwRJuT29Q7irBjEM9JfUNyk0LHuHSEc1la0-JvHhNBB9_y6wprega13HxfrM18IzucsryM9rOP6NZ21XbpiKANmfL2eVi58EMdqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/irNRcde0SKFjiEt1BxAwgdTh3UcoLN1hsmON2AetVPYhKnCGBJRpTP6907QPwQljQrAsqZ7eaAvf7UqAsnQY3wCmJV--pq-qz0Kz3tizXJEQeHtIgKKVtIeMkT6soioutUkrNliwIVEg-_XJrbdgeFY6OebRD0LlyPXyVemRhuem8bZlO4CA-FFZ_Xy8D9Tjv3VL_cquoDgbgGRG9O0dVgigAWOMwepSYGJ-Ub9qD_9fmwJmbiA6teM2RoyyUmcyJU0Zf40t9Tf-hfN_4L0fBH43gIY7N0WMtrDkZWKrnGMUIKmPkc4L9Ae19ugzIaPGTzT4RBBBA6VLG3yeYnBgvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lMguaY0MY6fztv6k6cErdT5W3sz_gPPCwQlKULGBqQvZQR9aEypR5vBo6PLNvrbYo7DtHfBd1iz5EsNrLXPu8cfn34LAZE9ACUzrouZ4hT_Q05AJrRudDXzgHREAXsXVZ285LYSVtNSsZLIZFVZXLKygY4AEuiwMeAYn233fMONcy4vhTPcfG8Ol0Xj2lpRlW2Suallgi5O7PLVyrcMu3kkL22cYkfEJaAfziJ_GGHd6IW7QL3lwb5KDTYtsqIWIEW5R02NckQipjbvXn_UDqQcZk2y4Wa5NecAbipC3FZ4rwqurdJIYRzmLXVpULeaR8eHrUyEDiMHn2y2R_HhQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس استریم شخصی هم نوشتم واسه خودم که با نت داخلی بیام روی Kick
(تانل rathole
😂
)
هاهاها
به من خندیدین؟
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4993" target="_blank">📅 08:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JeaSERK9AiYBkbFtd_ir1NoVkp2YAmbQNOAORRvkvFF4y61hSRLFcBq6QQWk55do18RhOqAQ3wOVfZOJIl1AwXPSnFqxiQws8NMIE5t1GqaHRQjUi_CaRiZoxXJ8v0vJ1Nz7Yso_1Hc8cg_cJ0SoIQpilxUV6G-DL07EnvLDH9M7VJkVusD3RkeH87mW6vLnL2z-znIp7fjIrI0uJvzL177NXnX8yCA2Ja0_KLl2c-9hWwNPcG9R3yCHqd-YerZIn10uXWtUAz6RmTjL0_gZYpSRowsTqeP22SNPCEx-wIefFtjAYlMeXBjyBPzcDtGItWQufkZiy2HNOsU3ldSRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AyuX_iT8L4WCNI0z9Obefwww2XDWfXC8FyG_gFFBwnkIsI6-WcZbsuMFnjhgDUjpWrL1pNHr9KaqSOpePO0AXgR0_jghu0jOtTAIy1dITBGKSrZdDn882p5IbreSsVca5B0-nEn158Yj_QbZHHQTosiBt351DOr3rf_jK2IKt7RfePqnp9EQj2kDudzgidkFAZEc6YesdQg6PNUQP7kSMkE3Roo9uSrFfkmz-fWRQVWsyugCySb-aGlzWmaz8fs3iHigA2Wsm0xBLCkzapjwmbW6TtZLmoWklOEMncBa98y99reAODIKfFpFXzDySwnAlNsSJfK6Ip4JGkDgYVQWqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pytZsqRGUW2zYvXf0M6PziXCfc307a6SkWxOHUn6LDsoriC_ONKd-vWLeb7NZdJBPv7dUiAaZlK8g0GShmE-29PrraWCKO-zZY40cMZZk3V6dqfCSUuicYuqvSP5BXJEiQ9LIYPH5A28ZsYiusHh-jFTiFBgez5nOnZ5LgsKVm5rR2qGoFyB11LPe7VueeZ5dUqzPme8OVZW-RcT2ePrS6bTujIRTOB_NkTQaNP1RZWa0bhsE8NwBASTIbX7ql2RU8LpHrgauUAoMAJhwZ7yNojHSTwYVCR5CWTJ3O4E7Vtb768fCNwY_hjO3W7DypVprUmqeRTzkpTnIasLvGdatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN رایگان بدون سرور با پنل BPB! ورژن 5
🌊
⚡️
لینک‌های استفاده شده توی ویدئو:
https://t.me/MatinSenPaii/4990
⭐️
توی این ویدئو بهتون یاد میدم که:
1- چطوری با پنل BPB برای خودتون VPN رایگان بسازید
2- روی گوشی و سیستم چطوری ستاپش کنید
3- و برای خودتون و خانوادتون، از یه VPN امن استفاده کنید
ویدئوی آموزش تنظیمات:
https://youtu.be/7G9Fjhe_NxM
ویدئوی بالا بردن سرعت آپلود:
https://youtu.be/dQKfkXnThCE
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ImyOiStGx5vcPoDHSi-Ga_is376I9hGT9toHJWbhGCRLvpQPf9Pcy2FMf3kMc0YTGOEtiIwVw8DAecQ2j-xIxUoPSyX_OfXrVKfi_SRv8LKr9fJ5CwwKJiTj5rO27mXRqSbIdozUhEd7r66Gk3D1qN6ZcePnjBBo7EV9oMwsIb4-NALkMBMu4_iYcX8nD3VJlomFYsqsM3LtlMkED0Ust7lWtxD9I_ET9iduwnVDtqgx2QrM7BDwZ1ef0Ae4bVPDvmMNlGGPdpwc8cukLMb29rmYYViQwFiJA-9vTi290G4fLIiHpZJJimP1LwRaMWxm3WJSYavDh5UGPHdxkf4DRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVctSXt1Qh7Sfvet_BqVZnGFyGuh88vw7Q9ripONIDHMBhC_uIyhHpMKDsYhyHTOx-8CUC-ypZA_UAJmC8_ul-R8-CCAooS1vWZSfIDm0kyJn7SiCkoLkIF7KMq-_C1SYMoKJ4Ibr2Blop_VevcI2vDzJlwsdqMw62gaUxwc0aJbLqk3wHqxQiH48UeAPXyfiNa2vzodyxJMjtYa9Ee4-LL4xrsoQCRxjnNiiWs-2sbKVx5Gti9fYC84BSrbxGbkQynbuaG42sOgaZUkLCmr4-NyCMYCRsv6l-Xutvcioznu6QuicZId393Wl_zLUOnj9jxJ1PUdMr8GmT526pwupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MVmX3HA42vL6Co36Tq21BKqomkc83eQt2HipOHylHgS56bO-tPKcPaECNkGlXKwx7T87rkK5Hx9DioYw8Q3BRAZwMg4Sd-k2cJvBP3vEgDj0yqdRqYV2T62pGkKaK2xwZCHAqXn5HfKIjZXvC2QkL2tj_mSTPZdzkktM0LlLGrmSJVa9w2AGpZ-cPXQajyLh7ILSFvUw6YPXBexCnwJVHegARdqzfax02NP5dRUrofJzRkGo2Go05Wnq6MyEbS2Wy0DbY3ES-TLV1CgEHwf__NbLgYREg0hJsi8_oQxDkKeEZRWIQLqyDMNMSDTusJQf0X3lj7CTBTO3FYQ17TER8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H562RjQMbMtB8MUCGp0dFNzMxJMKTUCAZidKwE_5SzCFqGKKahbQ2OJmJZ1zVmGVs7PgXDmSr-ZlDh7-4-GMYw6PCG6auejHrWnyiWL3l-MEuLj1Qyk7-l6Vv362wHpZ_wq3uDyzPi3QmjEooQc2qp-azFIjk0oqkGPtQ11VJzcaz39WHZYZgOjP_YF-P08qjoesL8ioMXXHiOhqEnI80EmkdZnzcLsDoiCIzfiDSaNoVvGJ1uNxr3HETJqlqKX1QNIGXT6kX70Tg-WGdDC_zRwCq5FUa9yRBQZWQEmm5kdKN2ieI-_9uygnhuzUVgmFumA6DHxKa6qkArnMKSKr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ریپو رو یکی از بچه‌ها واسم فرستاد که دوستش نوشتتش و جالب و کاربردیه، برای گرفتن کانفیگ رایگان
فرقش با بقیه ریپوهای «کانفیگ رایگان» اینه که فقط کانفیگ جمع نمی‌کنه. کانفیگ‌ها وارد یه
pipeline چندمرحله‌ای
می‌شن:
1- اول duplicateها حذف می‌شن و ساختار و endpoint هر کانفیگ چک می‌شه
🧹
2- بعد اتصال TCP سرورها تست می‌شه (سرورهای بی‌راه حذف می‌شن)
🔴
3- در نهایت هر کانفیگ با یه درخواست HTTP واقعی از طریق خود proxy توی
۳ دور مستقل
تست می‌شه
✅
یعنی چیزی که توی خروجی
verified
می‌بینید، ۳ بار واقعا کار کرده. نه فقط روی کاغذ.
🛡
اعداد و ارقامِ آخرین اجرا ( که خودم از روی index.json چک کردم):
- تغذیه از
۲۱ منبع
(۱۶ تاشون الان live هستن)
-
۱۰٬۵۵۲ کانفیگ یکتای
جمع‌آوری شده
-
۲٬۳۶۲ تا
هر ۳ دور تست رو رد کردن و وارد لیست verified شدن
- خروجی‌های
verified
،
fast
،
secure
و
top100
(۱۰۰ تا از سریع‌ترین‌ها)
- خروجی برای
V2Ray/Xray، Clash و sing-box
— اپ‌هایی مثل v2rayNG، Hiddify، NekoBox، Clash Meta پشتیبانی می‌شن
- کل سیستم هر
۱۵ دقیقه
خودکار آپدیت می‌شه
- فیلتر
secure
شامل forward secrecy هم هست و لینک‌های بدون اعتبارسنجی گواهی رو رد می‌کنه
🔐
لینک پروژه:
https://github.com/0xRadikal/Free-v2ray-Configs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gnl6wKU-T-ppFvynrLc3S0rOUYiTBKXKlC3zt6_blUEpWpnHvZJLbvBtq0HUO2P01bLvf3RbJ5zQLrmLpEmLjwnDLaY4vDjsT5kwroVRBZJAk_p7wANovq4RNNDRKU0Z-MLz_gn-5q81sj-8netU4zB1MkvQpJEMgrvIDSbLF6rk9n5akQuoYasW3aiusZCIpWWeYvGJA49kdQWO4gGruUQ1_CoAR4Tq3j1AxCGBahrI4kCeYQqtKbDNFW-6VTLcGCsROzK-upev5FE37Jgl0w6hG-5nCzBvucUK18kRPNVYAKfmeU9RsBbotvpElQ2V2XHTpnLfhWkFBb8Y4ofpLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IacYAncSLY-qMtg6Q-ANl78rWfVyoaNOxISN2TcBAXa9CtZwJv4KkLCjqriwKRsZhI8_LMXMbeAXSgrN6Wz3eX9uQqL2hjmAOXPhx27N5eP5PMBaIq9e2QivJpcouNnY6z2_xZFSMzv-jj05Cf0eX0ZbSNOMe7YkjP7h43VUkif8OBF6vUiadBRotsVx2crpq9tcaGrs7cKU6FXfBXPnO5fFPXUcdXvH6FIXKoWLP3AemmIIiA9HhjrQtZ6B2rpwOT5Yc6cZU3lJpXVKqaaGqEtWz6DBZisLu9pGmFJDh8uMXy8Lk2whxMNmWgxYs53gLauauiLvOrE5cTlob6E7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فایل و نکات مربوط به ویندوز:
https://t.me/patt_channel_x/101
مطالب اندروید:
https://t.me/patt_channel_x/91
اسکنر من:
https://github.com/MatinSenPai/SenPaiScanner
آخرین نسخه V2rayN دسکتاپ:
https://github.com/2dust/v2rayN/releases/tag/7.24.4
اپ PattNG ویژه اندروید:
https://github.com/patterniha/PattNG/releases</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/axlmVI-FGD-joN35NQQviIZ2_eiEPQ6sx9G7h37XYUVabpmldnSEDhncRje2QnN9sP49x0V0QgiODCEWg3_yYNWeMExGvYPWMnzgPCPmsKJXNDNRzFfIxkD8Afi0USBTVjMhft_zLtXSpRZ1S1-yTmUhwpPC-nvtD8-GNaf6BsKGbgi2YI2QoSyEpT1D7VfKPf3uml3hFTs-FHXcCJRGg46siYoJRXiUAjIA6QtZDfkq1xrRxgy3DMMG_Ts85W2q_Cl4VT4MU10YlE7g2KozJ2CSfyK2ViMQE6cJXZVAme3blYMks9ne9nVz2zAkQBWOmFJMqF-zmnslcsc0rHQ7gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
رفع فیلتر کانفیگ های کلودفلر + حل سرعت آپلود
⚡️
لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4973
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش دور زدن فیلترینگ
Workers‌.dev
با متد پترنیها
2- از بین بردن کامل مشکل سرعت آپلود روی کانفیگ‌های کلودفلر
3- استفاده درست از اسکنر من توی این شرایط
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fv99Hm2Tcwk0Eo0LqomGSXeWxK8OW3IDVmVafbXKRk-KAUOSDZBvEJOGtvcpuXh63ty5Ua50Ok84-eXyHOuk9IPYE-wtV13RzdIZl5hBbLj205VBRvvKdKy973XmRY66ghN-OGr-lSU7wZ7YEIt-ehRfqP5Vvev04H6sl_uaA4oHm4IKK64jhlESW41ag0WN59Ngz7BewcjtJFfYx3-lgfqml3Ne-N3kRM3jZDPpBLEvYpwWX1-SSMNHOYad8hmPI4DxAX99NVAZUyzXhLo0zCAKz1utFAuzcTcMggtUOsNSVP-HPS9OrXgluJ4V-lo1LTGCg6k-OUXwJ92lvQIS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J44-aT-cNjEdNcVxp6MfGrV6dRvT8CeqXSzEsw3HKVY2xXkuzadFxBXwC1KlDWiMzaOEKcX_qxXtO4klUdNI418DIUM3Q8JoSmhQ3-nLrbVJ4oWR5GrBUX5BonquI5K8o0Oop8muN9-9kFoEktN2KFYGB3hSGs5ZXSgSKdh7pP7v5OrYanfh_4y44yQxgf0dG2fPjfA1XDPCK5kzCo8v2nrAg2L6Rt6MCDPTz1aT12FVcShpxzZ4c_nDCn3tgPfxR_mq6w9TvC3Cw1uqYb4tDlhlb5d-s3jFBMv96aDxbvkwDgSWc2ZD_MdfnUB2oHkZJkBnO1zD0NRcaONNjlYQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OCGvmNrhYu9yQcHwGZ85tI5ujFnGr6M37Ea_6XSpu7GzLXgfRtRSE-IACNVQfytVHCtrbl3Z237v26Xd4o3lr2tPAk_8o0AdCgOIUlETgrW1Rhkeid168Gm2Kkb_eV5DbGewZSlNOMXDAdC70ouzgc47o75B0y4XGmeGhX11XyavigR7K9Pm18zQVZVreWAFDmdFJJEdY9pKCZyy3EBlgW07Kf_WM29D0lWZ3mM1z68HhEuTVfsnSZpk28-CqGxlb48X8frmByXP8eQ4NYn0ona4Xl_MI3__APlAXMKg1eVe9NehaIrKooPANCWlHh9d0njfBN_hS3zRZFlqOrN6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJrWIWezh630bo-D_8RpuIgk7JvOs3T5QhOuMDPeD0qflGMxOuVru0nkVtU1LW4SHpo-mo4jfVuklvgzJQIaPoxHYVIXpSLcp7Nu1s_8r-hApwgnTlL-uBWEnVlRjmSFE8Sxo3lbKE8gzyn2PKDLH9CWfyK4XKizWaZSRb6oA6iexoIjImFi-c898fP_7CVjNkengOMNxM6CbsnJ1T_SJtzJCmQ8ODjlLWqYr2etvaYICS0uvDzDkf597zRZ365BHjQX54xSbH6iUSo7G0CXx4Z9EICwIjKzxcZQOa-eYA8KY1jUxUhU8jT9x6GT5ER36Qkha0ZkyKf3fAW5M9X4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:
1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴):
https://github.com/2dust/v2rayNG/releases/tag/2.3.4
یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید
برای آیفون هم Sterisand آخرین نسخه کار می‌کنه
2-
این پروژه
از دوست عزیزمون Hidden-Node با الهام گرفتن از نکته‌ای که Patterniha
اینجا
گفته بود، نوشته شده و اوپن سورسه و کانفیگتون هم جایی ذخیره نمیشه:
http://hidden-node.github.io/proxy-builder
3- وارد سایت بالا که شدید، روی بخش Fragment + Fingerprint کلیک کنید
4- کانفیگتون رو کپی، و اینجا Paste کنید
5- پایین، روی Enhance بزنید و بعدش کانفیگ جدید رو کپی و توی
v2rayNG  2.3.4
v2rayN   7.24.7
برای آیفون هم Sterisand نسخه آخر
پیست کنید و به راحتی کار می‌کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfV7Eti4Sf8xa2x_EyRCOfYDDfgUtSMO7GHKgpeE0Bd4Amu1ziVavvM9dH65QpUFkLIbGp-GTQ85mZ7irBfm3zy9JqdP7veJiVxKyKVnZVLJpqwSo9uBlJ3ASBIGhnWUctt9cPvIYcziNaGfR3TSuTUjvEJVNo0dYdOEzqnBbiOj1FNxdiwbjI1uMraGJhUWFe3x4pQoKeF3xQ-mKPxLirvPo8N83eofbVBShyntXifJjNikMSPf_qglUxmL_U3xM877INPz4U3e03WKq0omuhkeNTg_FRXzJmixL4PTnJ680N1kuJg8oZTmGWG9F0WSJyxymbhk7HSyfx7FkkC82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeFhrL3UK6oU3IGsGZIuyNKCOzyIOWjB0ZDx4zVHTxj8V_JOS-HJcmvWosZ0QjCb8XN2QKmwqtYSMM_DiFcFDSezBBWS52kYQaEfnCX30NuAOrfWhKOSQIueb5OMtK_CpluKgsIMXYVGd6-y9sqWG6_SQDDQWJVKZTRAR7TmExGP7lW85B2kVCMoH0nWhYB5P5tghq42sCoqco0oH8FFsArWi2R580VCBJ1wkR3RuEWG9my8EKYW7szqw8uAAwvaAn7YA4DrqH3pxERbfCHBfZDhAysEmPG4u8Z0XdGeUmJckpUhlCycLxUHOLKkKQTFVw6UDbL7hzyNtyl4kY4KnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=slDMCknlUSnXanPs7QTZEDAFh23oTqiT99A_N15v8psqdpGrEEjKIscIQALsrMNFhG9rYRoArJOw5-AadiA29v_Y2Wj1S4BJRLqHFFlyW2ecPVqaBYz2vYAga9v28wS1gN05r9SUVzLuymEtRJxAIAnRmJny85uYpUygewO6wrmHezWRL8uiIRWkh1UjP2CWz6cMGArINblxv5s_GVGOW6fJk7LLDi93W9Vn5U4oiivsEsO4QHmGb5rcE28CS9b_UBkjk_BCkkn9HqEFnQETHmGjqcYp9647J93d5PWH9xj1kGS1uHemZ5ZV6f1zTGyKfVTLzSlD6Ofhhiyt8onxlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=slDMCknlUSnXanPs7QTZEDAFh23oTqiT99A_N15v8psqdpGrEEjKIscIQALsrMNFhG9rYRoArJOw5-AadiA29v_Y2Wj1S4BJRLqHFFlyW2ecPVqaBYz2vYAga9v28wS1gN05r9SUVzLuymEtRJxAIAnRmJny85uYpUygewO6wrmHezWRL8uiIRWkh1UjP2CWz6cMGArINblxv5s_GVGOW6fJk7LLDi93W9Vn5U4oiivsEsO4QHmGb5rcE28CS9b_UBkjk_BCkkn9HqEFnQETHmGjqcYp9647J93d5PWH9xj1kGS1uHemZ5ZV6f1zTGyKfVTLzSlD6Ofhhiyt8onxlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4952" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZD3668qbJfJUhXGM5PALAGMYnkHfuIqwMetEjFWjLnChsvRjjpdTCtygoBaxZyqIqPJNkX_8trTOC6o35A7gDj1KQE-j41racxk2gs-Nj-V3WJqPISMPmavyEetClBITO9Y0XDx_iNd5vcd1C23fvDO30w8DmzL0yIkTRnKJMYPjve50OnG-REAeavVREmaeGDaMK6XtEmOk63epSzkz_W43jW9zbZSYucbyBXT2hWYXcddkwK-CePncMfbC1jUwD4jWyaDqZNOj0sTQ_cNh4VejvH35AJ_MCcl7hW3-lz_ZczKvVjdQ0LxiZP2sWStivJCF8L0V1ZEdkEhsifmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4951" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اپ Defyx وصله
متد Aether هم وصله
کانفیگای رایگان MahsaNG هم وصله
کانفیگای مستقیم هم وصلن
پیشنهاد می‌کنم پول به فیلترشکن ندید. defyx و mahsa رو هم از گوگل پلی می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4950" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ge25e3HLpDMOsxkv0mEfKWRnc5UQd1nPLS6s-AuS29LFnJV99-ENAP76XLHs3tYylLbBkvljzUYKY1Frv1b1jfkh04jowwtAmJPICSeOK8Ii3UAzKAnAz8eeBollU-gOR7unM4J83tsN7NujvLRAdMgFR5Y0Xzh6BkWt8SD3MmQSrRcRvM4e2hV7znkMkZIcK6LsraSdUTMGkrQ3edKYpuADCFV-xjXCi1iDGf-h3B48IC_P601NZ6WU1rxDy0ndAej7t26hWvvwHnf5_0QGXTJPYPJIShim3iXxfjjYoUdCYvHQz8oAaPEtWFRnLZXq6jzMW3LnSC52B37SLSCdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4949" target="_blank">📅 17:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پروتکل MASQUE از Aether-GUI متصله. از اینجا می‌تونید آموزش اندروید و دسکتاپش رو ببینید:
https://youtu.be/2h6qlA1pJFw</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4948" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ihzDcbkml74QT6qeyga9nnJe2mu3ranlxwlPsqpDhrC1jQIGxcvlXrIUmB1dL2aTdetzw9rKW7YbEJp-Ac00SNH95C0G7UysE_E2mSINdocMxFj8zs7qBqQpkNN16EfC8r1xYe6A3UBoAgzsQgeWxjgvEpKmwhgT6YP7cuzPew1iZknJjcKLHUeYSZjiUYJieWUqh6h5rJFauV2B1QxrX2iilJs-chM59RVQYzBWAVHDsP_PmOiLljV4itUnyMVbnHSXSR34x9uoYPiZpDCsK9RvLdFXaaSOnwlCOlJ1_BCZR6SpngfdmOaoQ8yw0Zcmo8t519lbNIXvk2REus77Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cmVR8AoNUhLB20joERWyMRTNQpFQGr43Ur41jFWnsFhG01swSvuE5ZcsuAv81X9OZoIlRqzkoDXfZfGHPjOYHlz32r5LoTUX3AMHyYaKMTDgfn52n89-sesyLvW_EPoNkg3oFjTA9ZoHLFhIJRXAxReErLkKS-URyNHP7tb6zToTNyK06DoFY3hW9969dww5tcNn8TJASKmGM4hxKKILlXUJzwLt2skrdKvsRUtvRgDQg3d4oD-Xzv_XvtI6i0h4idIjJlsk1D6bFHJu0tt4uDh0V-_sPHczrvwymrmhBoVBdiOpYw-9m455AVci0pzjYggWedwbHk3zISI0-xvNgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n656MPPs1v1M6vP0xWX7ZxqeRXW0iUJUxhYQAOlTK5L44k2EFx2SRyTY5iBJhUkzpzw7iuf4QXqhrPBGM_e8I1Ha86A3yuP7z6HFr_apPB5kZMK_Zv9HqFSbNNtlelCxf6W06OqHCre08HYA3_s0RHJRU1v1BYj89M9pts-RmuXhnUXUmq5wbTur01vqmrijOXLQy_AaRy6U_YhSAqN9mxR0nqO6tL-bL3T3kfv1xJQBF1Wmb4wCvU4jZesj0DI3qgvGBRndKw6Skgk3rgurUwAIsNp6y0GYMRJOb2IF1nDIK2GJ5s1ttjbAzpM-6j0LFHZgmyoiDIjvjEEJZVuvLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WfghWI0Mc8M4IKnSDK7rEJxRrRwxzTyrAsIgioutW3xnNJZKln0VYm_OT0QZQokE3Q5nCBmYxM2g91XQ5mqbF1fQjaN5SyCTubKYdgvXEOuLoJVR6pJW1A-9YD2oGzG8SRthcxPfZtQN82r0ZXKoxLlZbZfD1loO32HO6YKZxH7rzwN_PQtyYvW7akcq5pG7Jyh-8mcmy8ZgHMih6nRxVZYwxOmS9HnuLiGjaegtIv0D20wcUNBhLEQt8fjQFoSOCKORfINmHR9NjI0n2zu_won3EEzDq9Q25uTqa0Bsvonubfon5SV7inUVEdKRAQmJwldLdOgzFYJXLW6E0v5hxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uAQTjLEnyw_kXltyjx1uv_FyZbSZCHlk8l7Cx25VENAmSDXaoxqXZZdtqfEZSkBPu02ym1bblp2nr_BwR2AmEUN4DaOEqUUCZOw2wfrM4tpmv1s7Q2OpMNWcXlAqBVMZFER0UuBrK56bIgcC3F3CaaD0bXiQzC8eckTRYc8Ql_bBYYJaeHjbvLI7kM8fMG6jJNkXr_mnt95rRiYwXlRkgYZzyy95oPYgOcjfY-lu0XxoRSMbiz7blSnQc3WDhpzf0KO3fw_wPeAO1FCIanS9IrBbTxuWk7qUUH5fSXlyXWNQTtI8xnB1vNJRZxWg69srMv_x4iMrtgxMKTpAf1UI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1SM1hwzq7Qh3fbmxbs9V5JjYXxjDlPL1SHKtm_sjefkMkXUqtagko4MEfxlcLEhBfNozRiDjNoUb37NZWT4ifwyCY2aukJdOHXPDt9nFl9RBIsABwbynOWF9PdJGy0ZzbQ26dAOYaaw8WI3Zh8Q2UgeNA5m09EPj8kdaHg-9OBB9pEpFaL4U1-2miyCI3_B1gQ92ijIrPCwqOfQZr5jm-YFCkRtoFyrs-_PY2XJEMFM0Kakw6ZD54LIhvnI9rt5FbQamRxphYevTTQVWa8PHhqBYV-Ca-YC6oa_zziqdGFgNvHEDx1lVkOnMg4XVX0dUKQmIGF4_rfpEhhWbR6Xug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U0es0OvD29Mf4_JYYKUhnd68wF7I0pC10ae1Sqa0yE_G5royh9Qg925qziSvPXYLrvKLkjstNujznWVoygjROHFCg4hzlJC9f4kVUzrB-A7749rfn4cY6YIBWGYfv_uUOaRkR7zH9Sx7SYDxOFMKzHEmVu6rgik512-D0PE965cMiKgL3k8aoOpDFofQep1cTa3GQ4r140FvLdmWGvy-XQ29rv9fVKBDtF5zHjB70Yb-nBIwzKZVFeF80GgXfyRgNsNYqp4CYwSp6cZGR6OOfBk553PU_wzaM4dqpWUYcSWcwtS9A5PJVuHqB0CQsGxFNYIDUrtmYkwlsqnwNsuu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KkHq2JMe0h-BL5m4ewd2cmhlxIBrSnNr7vShYAhmTLVHBzFhzm4bJ-qGfggWJnAVrV4c_9FFiosCvFepN9zsZVfvCk7QFTWawjLMPvFd-E-UaZPSSrSHks2My7zyrpwT_Rhxu3H41sjX0aC9uNxO_sdh4LsggSMw7icZVJGLojTE_Ec61gpWzR2Lc8mC-7mRjXEdqNgQao-gS3yhcrVtUbbY_TsBGgyeRiXOKsmMBmc82RzqS9D0XMHGeAJs2RDPcbaFIj7HpiAvHgVy-vz4OrtPheQoLYWXIe1V14KKjtPkYe0iTTwnvofZSK1brqmHuWDGPMM_3j4EzCSfTjgCYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JbTlqTJcZJmiHKycLGtcQE-lFrG5yB_-Z8zbHE1LVfrDwbq9TLORnXkZ87CO-bLK6MFqfa3z0mgFqYC2zi1ZMNPetEQl0TWVw-8qgIWyhx5bIdOFzCk_n2huLyCSJJH9MqopNohx_Y96c7FREQeIUi2k8Z2qAzw41NpL08brRCm-w1HDg_XpmOKxUie5C7sMg7ry_6i3KIYSnqibbnyfRZSKL4VwpOF-RULUQBqkJjoQFBkcFAUJwfAZ0xL92mMm8u14ZIIpOFUo2ffHk1O1x6hG2dxlxpznaSiene1Ovp-HSy0VKRzqmEaJsveYkE9UJPoJMR-KdFlGLHZOH-9SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود
😂
😭
اینو چرا پوش کردین مسلمونا</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4931" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔺
ابزار کدنویسی متن‌باز DeepSeek Harness برای رقابت با Claude Code معرفی شد</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4930" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zywfb2M3j27EKDT_BAsmQjeK9GqwMbQ37FDsaOgY-oWqmJbNJK2wqV7T9rYdDMUjN-c09QuDbNtCZ6VhhNgr6rdejVhf1TyCLgY0HomjnLq06ZEJSQYCnxLGkEU_nKVPudKp81iV2vOSzoUmfQhnlN8ZGhf0orsuy2eayEYkO9dXoA0Vgm7SRkEwYVjMiP4lMEdDYWFzPS63V6sTiPiGfQDLKjRlLc4ZWrVpuK_mtYOilt_1pwWfM1JJ0g5uQW1e30o1Zhm4UBjlBS-YFB4uaeJS53BNQhFN-1GoAnkRR8AwE20oYP8jFZwq_vK5I4GLE4XLjlwMHxyC9dK7ynnDfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه قابلیت خفن برای هرمس ایجنت معرفی شده به اسم Bot Mode
به جای اینکه هر بار سشن جدید باز کنی، می‌تونی چند تا بات جداگانه بسازی.
هر بات پروفایل، عکس، توضیح و کار مخصوص خودش رو داره و حتی می‌تونه با بقیه بات‌هات حرف بزنه و همکاری کنه.
https://github.com/NousResearch/Hermes-Bot-Mode
@RepoFA</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4929" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QOSU-LpBbj3XyRQdtK8FyvxTvvtjV4XHxQ8ImN4mUX-5uQVjcbQumwVRG3sp9fM0Fpk5l6bbdKEV61-RoZ2E4Lvo3w_9FU_OcLznsq7OzhVWC9-y4GYIZk9QMDKrFmhNN8qAhZdB2yllYIGva0V6zvNuogX6VMIDpbZNJXWPhtViJgiTZF-FCrvflwdB4WwZp1_ecOLXA2te6Ss4lW4e5NWLa3YvywvXIGNG_ufBM3ylV2jijzmHFbmZ3FM5R48NXHnroymLmPXhmrzsssTgXXHDH0Rnr9KkEJLr26l5PBItzdSPNpFUBPjfVYQZ--jQjeYldNrEiJuUaOk96FaheA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KvWJC-_g4NqVfMEhvNNafdI0P__2yphAngVaPgpsR278fQLQpa5Fe_xuvfHRQoMKvvn8ArWNi3G87NKvlnQ3iPEu8Rco-6S36qy12cTazdc7PIcJwW7EIv438DKrrm3I_n-l6UsfKqp66Jpq21yX2fnzr4udCbPtlOcsjq7ugiuyJ6DL-u-m-NIRBAd2sNFz-WJByTIdrlj4yGFEkXAnjR3d4bBHz09MxpxJwWM-Dnlg9kuh5O5Ftw4SKhYDAYXsYAa8enkgtNa_vgXE-qf795KREKPoFYcGjOHQBxkvR8apWfutNUyqZgbP0ph7N8I0jSKcY7eb908E8xERHDOGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/emWwuHbe0khiyg9dFPUGXC93-Zr1z6m4pvcCJAA6ZlKVQSRPrLyq-_rjhmd_bFZPSC7zzjQQn0jh3TJeJ39lRebH1-dRvK9BLDKKzzTyaMldAfIr_bEDpMzYz0bWjRT-fx1NC-3WiKaxQUWbt8_199u4Y4CWHLMPvCmnYPr9pQ88zy6W_EF2syuWz9D_a00NWLiKf7Vfw8zFZ5ce1d-MFCQTbZOyVHSrlcAoyisBVSWPVCasrCX0rgS5z8blNwlxE2PXNOMf9DsIKRg-4NTzR7Xkq4lM04u01ZYhRk10JAzB0_kSdTeGDsdYEoMotEfZdyK7my8Ce_KMiFzUifr3aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dk48pxuIeoj7isb8AOwfv_SgXfHZphug1DqZ6rcrRKSl3f7w-AIxqBx0UEA2SrJ9rw1V08-vrfFuoSQ_03RnM7vPzXP9nP-fc-G6ObLXNfV0i85faOXdUGQ9sRBFxXFClcYT9UjlphcykwMfUN_RY5jlXzidbqyJG-kEq9pudmmaL242pGiC7YGc0h5tcglrJhhLOvZuhW9dFSKPvASAD9wRTyucV88ZDLw-EmAyOqn_eagwKHJI7efywFynta5Gw90lOZDZvlDFagaoOFtwnCoXXNOBDTJqQRx_Yr_Pip8I-Tm_Di2ibK1idYAPadmHNxab5f8O3E1A9-wVvYQMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iF3e1kH-rpoK0vNSl9J4jwTD26pwS1K3DrphrX-XkzNKrUcEQLCvoI1AxZDPbIZdaxE1-Q2eFIYygjys218w9R1t0_WM-ORIFExMj-ldlXqGWP90x1RwSv6qLCbbnh-tsVlrZPV-T1CC9zVFJc4Bq2Vv_W_KD8KJmzPS63601p0z5OOHShoxmhRQtqeeVvirhrauO-Vv32LbCRBr4kRpZtVkwmy4YzgnpcbXO5YX7-vkG-w8VhFYi8J6mq0Nxwa7sgrF7vZ7JBvt2K98tNmCq4KnP8sj4o_P_DN-wMmFeXI8XTNtBkMrO-tIJEMu9vcDzt4leXEO2PAH1Vii1O-p5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/niTk6NGhD32SZPQnlMrZEqwb4ceMX8q3gDwnF8YCi20X7xV1NZz0w-s5weKcn-FlZPvGyLtTNT2H_QScbFs6V_12Ve2TvhxonXPloGtPX8mdnawP5RPaKXAr4bP1Dr313BGnA-Bb67KJw70jVEOpvWG1LRgWuXwbXZJ2CBmXtrPlgBi6lwdSPfzmLOqZnjetu7Wflt7cyWn8Ji9Xtnc0yNr3m96mmBEJm6u4iDjv26c47mDTUUi-6PYZKdmY9D_Ut5qp5jnBovpuVrFLdyH12NkAooMXmc0WVoPTlS6nPAdmQ97FvrwsUboqP3zT7JHgBKcynEZPKiL-YCuwDEhq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kTf2j5akUqWD0M1o1aUakGQzpQh8piE9Wy2KI69HaoDKrGcellcwZ98mY2jeasoy2Pmengh5IrzAcxDOx0oBxQtAc6_Ar3iFY8s26lsKH2lf67NHMupLJB9wzJWlZ90dva9DpBGwT5MJFf_-y1psoTyr_P_kL0w-W6hX-fAWYVoys9X3_78q8VwocOZmuB7AtzHm3RWBfXmoI-lhxTHtPpdqh7AbLWykeuQFQ0vLGbUSzVoQ149H6L13fvGPPbxzPSVtb5xAiQexRSsquT2E3LDOVCCczyVrBaZzKafsLsFjdAe9_o8wLXCZBq5cCsvb6ZCGjiMwvz-qFwhxWCLPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pe3X44QyTV6phLimWSL0ZJDvvtZrntHr2n4lprDq-U9f37l8aS1kAhufNSz27EHAX5PdWxNRnQE-49jvDsF7XaR2LRCXRPvkfR3L57cMGaTSvqGV3wAu6cRlJS95KHS6TVUmsWKUAgzoAi3IAgnihgN0b9Dsr7fmv0ENWw6jYwYeacW7vtVnnK2kiIqQbSAMKbP4PvCcbCcinQtBQCD62V3GiQkzVDsCH3cQeKx_jGw0g_NTivsNeYTF7BkgPFz4ORTgTcby1zvAWvLjG42GU2yZrypEg4KUbYGe6CxqRgzlSGt28EvnIQFlNQm4uLyhOzw6DyR9BRKOMgSlhARq-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی تمام سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/psAOsK7LLeRa-jneaFgc6ZervwIumYHu1p99Yr0kLvzlORTNS5QodliY5CIciL2noJ1Hex9wOZj_7i-OV7-ozTrf7aiw5H2BZVT5M2nCKapEFBhiCQMq7Fto9dyDu-wXU5MCyOctOwWS7V7P0TtQw0q71zokkXmt8ZOKkhw0e9tHL5yShP6AyTP613E9ZSQhmJePFInyDvURhD3DMGle8Jg53g6rjUdvialVRvH2rMozfnz9vc2PVjAS490psDS_WrCRxVf-MZ3YkaGFneecXFk6HSfz63hHtjv3ScJpuFObdGAlnG9Rsan3ccs0ioSHBdAQob9SPnFe_R4isyCa0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tj3sC6aUG_Rp0Rvh6yM6tn3-EKiLxkiYW30s0hBtGqeEsoOSiJnKKhuXduWzJ2Hvu8qEzm3MOWj_ManptUJTGhImLVdkp203oXAh9eogQ7HHLxp1iQCKpq62Ew82nOjmp3qTsvi5f2DIiv_6crWtOZngroY_A8eSnqnjaEtY4AHaEz4tUbyGNHgoGOfvBJIa3_QKbdc908C5jV7TWOxeijOuy3fxNsx-hmKZBcwyzM8s8JLpDHGhZqZq7N1Z7_ztrkr0K8jVaHfjTU_m79WYS9k2b75d4MWVSF5fmThi0MxaLaR4oDel_CSx9fvLtNWVKiZqgfYdZFL5EHbFWXDuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oNgar-nTlfkMKM7F9EgZV5f5ZQbPgNndEuxWSXy0VnWd_5y-yFzc41S20wNmsTa77UKfZF1Co_EbOMAO7nLolu1ZlUKGbje95yVSD28vJkk4hPFxAQfy4SNpVk0He2b86jUWVxSB6t4-YtllrjA1J9f5cpZaOXPx76hioiQ4QU23d9YShzLkBMaRW5tCpNlEHXmucCqL-gW9OFUPyevp-OJCrZmoA4dBqr0hJh4xzmJrbEoAt9EBJNEl5BtYR2PAr7hHz617LgVc_kyn-AkcdOj_i6Yl2DFngNT3lSatQ-GeEdUTfkr3eF57w-ZjvvVJopbZ1svfNdERtheYCZzT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WQEEi8mAEYUFv2_QPmJBilmiDVNvcPl1mvODebRcocEaB79jG2TGSUHeXsJ7IlMXZQncJ8Hm1YkXMJZI7mr_SqB00AiBI41twyyqVmkj2JSmgPu1ilHkX92b56Mcul6GKJNx8q7pdxWRb4xTegpoW3Eng-cAVW-RsXwq7M8RRzfNWibmVpgD_bRPXtnSUJSlxpBVB_LVElvCwyPnc936P3m58HFeK0pKS2Rd403K5rkQbk0Ecq4BGkJHj7E3TzoWaNqR-oAYM2A7PXqnmL5uz7h-fGjcSLccmb-ReC61Otju6UGbTKZc9c8gmInU-bJGRyi3NJc8nFl-McQ5RXmGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/haeM5lx0YrBTo_YOL_L0d2vji69WW7nlv81vxcB7Fju1EAqQmeU_QeuJ-ELaIPm3nWUEqMINrUw5nGvemlbcarX80rx6RlY1CJtfFi0T8OA0pqLH4CiqyPQqOhZKkvyckSbiB-XJzjXCSMwsQpbLXxhKPeNfXQxE3WKsFyvFF5auSkBIWScIFjfiHhdiXoGY8RKnvXm417JRl2F83ZDTtBUH5bZdq18BuiD1dEXxCmsUkqM5jnds7eOqPX1CBAdxUSVY7DhWi9X3ptaEkg3QJ59MR0fwaMTXvbmdtGMhtm4jQlB0jd3GkFY_eXWupGXULP13l1mNL2NWQKV7gBjQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8uqfDSjnDqZHonShfkUViKyfS1-y3i2RGwfKTSkuA9tBvEGnpsKYx1zcvUUb0OlB8ZyFRAFLM2frETweqo9OXKyBXX1uI9xWIM9ILwSnn1AjpX61uekkxpMPyHA0vHXKOvvteTVlFoTowQ_HxNHA9fEW-6tIOOQ2YzSKs9riwO9kxynqkrT1rxVCoAAFZi4Ou1-RbsQG6CWYUm912MNkhIxK5qFeSn1X_8EuKXREDstgV3XR1QRwrU2pDzpXHuMZUvm7RYzLl8S8d0k0M7W7uRxA25D_wf6Vl3jUCZQ2K-FnxKiPOlQvJoKFq_zNAHk3eCNfsleZSd_QeesFvmEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
