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
<img src="https://cdn4.telesco.pe/file/DGVgYmtetC4q-D9bGazmPeSzA5OlVEi3O5C7MGo9_6bfXqPuh_d6ONcdzZhvC0ENpo9FdD2lRLEk3bJUi6Phsc1Zy3PEuZnxJX4PMh3mp2naVRi7x4o_LA3pIszcXwxePGRZvN4U9tngd6cLAJDh_Mtf2Va-Ag-3NXBusNoqKGH8XAT8YxC1Yp-jUt6aJSh5KWqKofM3qkERsc3L48RNe1DsEq4e3DzOJL8wPczn8ikde4A479hDP5bPupvurVT3yFB9EN5jF7EgxCnirl9zJz2nfC0bzK00oruILl1TRiL25uEBKKKHSxVyEtfoAC0_4CMnKTo_a_zFfNmpBe8ydA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 6.4K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 12:53:21</div>
<hr>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxDUSL2tDvW9MLttsTaigtSWKaa0-qEQPAJimYJEhmxxYwEQvOduJwQqVLl_H48smRlggl4nQ2jCZc-2LiwtbOZbQ8yDGivusztLDKhlYeOocYstuMEq2jlyNM1FcMwP9urMUxeCyjU8mUwSx-ASYIaj9yXrtHSFduwbnIW0CUHVvJaleWKB1BNmvU64IQGAd1fB8R49JQxyamGg2KYVcBFiM2Bvx-yhaHF2aUc-jcxYvgJ6Edp-pfO9BgF_hQUgFpPdrZJgmc8EMOM5lhuIWOdP4qFNaFrXiny01pa8-w4RZmNBCdpp347FKl9Maeyo387sjRVMbtUyO8uWxPMkiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🚀
وصل شدیم (بقیه سرور ها هم بزودی فیکس میشن)
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 424 · <a href="https://t.me/archivetell/4820" target="_blank">📅 12:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوستان ، تغییر نتلیفای کسایی که قطع شدن
نمیدونم با این تغییر چقدر دووم داشته باشه من که فعلا وصلم.
یه تغییری باید سمت سرور و کلاینت بدید
اگه سرور ندارید صبر کنید صاحب سرور انجام بده خبر بده
سمت سرور
:
اگه پنل ثنایی دارید ، قسمت inbound
یه فیلد هست نوشته
padding bytes :
و خالیه شما بکنیدش 1-1
اینجوری میشه :
padding bytes : 1-1
اگرم xray دستی نصب کردید و پنل ندارید باید فایل config.json ادیت کنید زیر path همینو اضاف کنید که احتمالا بلد باشه هرکی دستی نصب کرده.
حالا
سمت کلاینت :
کانفیگتون رو ادیت کنید (علامت مداد)
زیر path
عنوانش نوشته Xhttp extra raw JSON...
داخلش اینو بنویسید یا اضاف کنید
{ "xPaddingBytes": "1-1" }
اگر خالی نیست هم همچین فرمتی میشه(البته من از فرمت بالا استفاده کردم این پایینی رو یکی از بچه ها فرستاده تست نکردم) :
{"headers":{"x-host":"netlify.parsashonam.sbs:444"},"xPaddingBytes":"1-1","scMaxEachPostBytes":"1000000"}</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/archivetell/4819" target="_blank">📅 11:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نتلیفای وصل
kubernetes.io
،
50.7.5.83
65.109.34.234
،
kustomize.sigs.k8s.io
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/archivetell/4818" target="_blank">📅 11:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4817">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👾
لیست دانلود برنامه ها با نت ملی
1️⃣
WhiteDNS
1.1.0
(نسخه ی رسمی)
4️⃣
NekoBox v8a
●
NekoBox v7a
1.4.2
7️⃣
The Feed
0.17.5
📱
Telegram
(گوگل پلی)
12.7.2
📱
Telegram
(رسمی)
12.7.2
📱
Telegram
(Windows)
12.7.2
📱
Whatsapp
2‌.26‌.17.‌72
💬
Instagram
v415.0.0.36.76
👑
ShiroKhorshid
2026.03.17
5️⃣
Mhrv Rs
v1.9.14
📶
Npv
123
📶
V2box
5.3.4
📶
V2ray Ng
2.18
📶
V2ray Ng
(Windows)
3️⃣
Am tunnle
(pro)
37
3️⃣
Am tunnle
(lite)
🕊
Slipnet
2.5.3
2️⃣
Masterdns
1.0.9
📶
Open vpn
3.71
📱
Happ
3.20.4
💻
Happ
(Windows)
📶
Psiphon
462
📶
Psiphon
(Windows)
8️⃣
Bd net
104
6️⃣
Mahsang
15
📶
http injector
6.5.0
📶
Wireguard
1.0.20260315</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/archivetell/4817" target="_blank">📅 11:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4816">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">لینک داخلی V2rayn ویندوز
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/archivetell/4816" target="_blank">📅 11:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4815">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">به زودی جنگ میشه..
دارن همه راه ها رو میبندن تا دوباره فقط آیپی های وایت وصل بمونن و قیمت رو ببرن بالا</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/4815" target="_blank">📅 08:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4814">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">جدیدترین سریال ها
https://www.nilfgaard.top
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/4814" target="_blank">📅 07:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه سری گفتن نتلیفای وصل شده دوباره ولی برای من نشده. برای دوستانی که از نتلیفای لعنتی رکب خوردن:
(شکن ظاهرا تو این قطعی نقشی نداشته ولی از کجا معلوم پشت پرده یه صحبت ریزی کرده باشن!)
یه راه حل
موقت
(امیدوارم آدما‌ی نتلیفای اینجا نباشن) که کانفیگ رو دوباره زنده میکنه ولی Pros and Cons خودش رو داره از این قراره: PaddingBytes رو توی کانفیگ غیر فعال کنید و کانفیگتون به کار می‌افته طبق مراحل زیر. قبل از هرچیز: من اینا رو با شکن تست کردم و جواب داد ولی شما باید خودتون اینو تست کنید. اساسا ایده‌ی xPaddingBytes برای مبارزه با DPI بوده و شاید این روش مناسب نباشه.
۱. برای سمت کلاینت v2Ray، این بخش رو به XHTTP Extra Raw Json کانفیگ اضافه کنید تا پدینگ بشه فقط یک بایت. (و بعد مطابق معمول کانفیگ رو به صورت لینک یا JSON بفرستید برای بقیه)
{ "xPaddingBytes": "1-1" }
همچنین ظاهرا ویژگی‌های ظاهری پدینگ هم قابل تغییر و رندوم کردن هست (پیش‌فرض فقط ۱۰۰ الی ۱۰۰۰ تا X). با این من راهی پیدا نکردم که پدینگ رو کامل خاموش کنه از سمت کلاینت.
۲. مهم: قاعدتا باید سمت سرور هم همین تغییر رو بدید، چون سرور Xray حداقل تا نسخه‌ی 26.3.27 حتما چک می‌کنه که کلاینت این پدینگ رو با سایز درست (که پیش فرض اندازه‌ی ۱۰۰ تا ۱۰۰۰ بایت هست) داشته باشه. دو راه پیش روی من بود، یا این تنظیم رو توی سرور عوض کنم (و از اون ور هم سایز پدینگ بشه ۱ بایت)، یا کلا سرور رو پچ کنم (و البته ظاهرا یه درخواست از طرف توسعه‌دهنده‌ها هم هست برای Xray Xhttp که الزام داشتن پدینگ از سمت سرور برای کلاینت رو حذف کنه).
من سرور رو پچ کردم چرا که می‌خواستم رفتار سرور عوض نشه (و نتلیفای حداقل
هنوز
رفتار سرور براش مهم نیست یعنی پدینگ‌های از سمت سرور رو کاری نداره)، شما می‌تونید تلاش کنید که xPaddingBytes رو توی تنظیمات سرور بذارید "1-1" مشابه کلاینت (من با پنل ثنایی و اینا کار نکردم، یحتمل از اونجا هم میشه این تنظیم رو داد).
اگر می‌خواید مثل من پچ کنید، مشابه تغییر branch پایین (نه main) بیلد کنید برای لینوکس یا غیره و باینری رو جایگزین کنید (فورک از ورژن 26.3.27). بیلد کار پنج دیقس، از AI بپرسید.
🔹
به هیچ وجه باینری از کسی نگیرید! خودتون بیلد کنید.
https://github.com/Sprimesson/Xray-core/tree/feature/no-xpadding-checks
اگر میخواید پچ نکنید و بجاش کانفیگ سرور رو با کلاینت یکی کنید (من تست نکردم) باید ذیل xhttpSettings توی config.json همین اضافه شه مثلا:
"xhttpSettings": {
"path": "/s1",
"xPaddingBytes": "1-1"
}
۳. یه موضوع دیگه که من به نظرم مهمه: من کانفیگ‌هام دو تا نسخه داره Normal و Slow. توی Slow، تاخیر توی ارسال POST اضافه کردم و این باعث میشه پینگ کانفیگ بره بالا ولی روی سرعت آپلود تاثیر ملموسی نداره (برای دانلود هم به نظر میاد فرقی نداره). استفاده از Slow باعث میشه تعداد ریکوئست به نتلیفای لعنتی (که سرگردنه وایساده و قیمت گیگی/ریکوئستی‌ش از رقباش که اونم حرومزادن و دامین فرانتینگ رو بستن بالاتره) کمتر بشه و به عبارتی اقتصادی‌تر باشه. مثال برای XHTTP Extra Raw JSON:
{
"xPaddingBytes": "1-1",
"scMaxEachPostBytes": "4000000",
"scMinPostsIntervalMs": "500-1000",
"scMaxBufferedPosts": 30,
"scStreamUpServerSecs": -1,
"xmux": {
"maxConnections": 3,
"hMaxRequestTimes": 0,
"hMaxReusableSecs": 0,
"hKeepAlivePeriod": -1
}
}
این JSON ها وارد لینک کانفیگ میشن و مشکلی نیست.
Source</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/4813" target="_blank">📅 07:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">aio‑downloader  اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده. این…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/4811" target="_blank">📅 00:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">aio‑downloader
اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
لینک پروژه:
https://github.com/ProAlit/aio-downloader</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/4810" target="_blank">📅 00:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnDxTEv2fqK6qxk8uByUCBkHaJ1DQ0pwkYCkxYnKbZIEbsgxfTn83oG6Pjc1yviBaR_m3FuAM_rJRMxGYADSrXtz_yUDSCmCCLedUeftLYCb_WQ0Vbk53B0Be00x0WrRTjJnWLerd5r3fGDevsq7BCgEtLzZj0_mXyZv2l8DTFjlRkn1fTvLKQ_DOiSUg6GA18a3pYKqmzoX91N6n6kixdpo4_PQhWIxeBNX4V0InFDsmRzMjsGQmBwQ95M9AY5CVUCNDMFEzwVOZY7aZNwkQwQemch-3YdtZ9yMiEbR9mx6Ly5IXF-L1AvStyuc07wyRb-649X7z7UAD9GaAipvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتلیفای بای بای       @ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/4802" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تا ۱۰ روز دیگه جنگ میشه..</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/4800" target="_blank">📅 00:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتلیفای بای بای
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/4798" target="_blank">📅 00:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سایت های موزیک بدون فیلتر
http://toogoosh.com
https://rozmusic.com/
https://upmusics.com/category/single-tracks/
https://musics-fa.com/download-songs/
https://bir-music.com/
https://biamusic.ir/
https://mahanmusic.net/top-songs/
https://radio.biato.in/
http://Sptfy.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/4797" target="_blank">📅 00:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فیلم و سریال بدون سانسور
Movieyaab.ir
f2mux.top
www.myf2mi.top
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/4794" target="_blank">📅 23:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سایت داخلی برای دانلود frimware ios
https://ipsw.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/4793" target="_blank">📅 23:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چطوری تشخیص دهیم سرور شما اسپوف خور هست
؟
روی سرور مقصدت بزن
tcpdump icmp
بعد روی سرور ایرانت بزن
iptables -t nat -A POSTROUTING -d TARGET-IP -j SNAT --to-source SPOOF-IP
ping -c 10 TARGET-IP
تارگت ایپی ایپی سرور مقصده،
اسپوف آیپی ایپی ای که سفیده میخوای اسپوفش کنی
اگه تو ترمینال سرور مقصدت پکت ها اومد و ایپی جعلی روشون بود ایرانت میتونه اسپوف بزنه اگه هیچی نیومد تو tcpdump اسپوف خور نیست.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/4792" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ربات جمنای
@Gemini_PV_bot
@NewGeminiAi_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/4791" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ربات های هوش مصنوعی همه مدل ها
@chat_llm_100_bot
@GPT4Telegrambot
@GratomicAiBOT
@GPT4_Unlimit_bot
@GPT4AgentsBot
@grok_gidbot
@ChatGPT_grok4bot
@ChatGPT_General_Bot
@Javidiran_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/4790" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4789">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آموزش_اپلود_و_استفاده_اسکریپت_در_کولب_گوگل.pdf</div>
  <div class="tg-doc-extra">2.5 MB</div>
</div>
<a href="https://t.me/archivetell/4789" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت) خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟ ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها،…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/4789" target="_blank">📅 23:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ربات تبدیل ویس به متن
@VoiceToTextMasterBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/4785" target="_blank">📅 19:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
امروز می‌خوایم درباره موضوعی حرف بزنیم که احتمالا از این به بعد بیشتر اسمش رو می‌شنوید؛ مخصوصا برای کسایی که خرید
کارت به کارت
کانفیگ از شخص یا ربات انجام میدن
❗️
یه سری گزارش بهمون دادن
از طرف No Caller ID براشون زنگ زدن و سوال‌هایی مثل:
● شما به شخص "برفرض قلی زاده" واریز کردید میشناسیدش؟
بدبینانه ترین حالتش اینکه:
● ما از تماس**** میگیریم شما از کجا کانفیگ خرید کردید؟ بیاید اداره تعهد بدید و بیاید اینجا توضیح بدید دارید چه کاری با vpn انجام میدید.
اول باید یه نکته مهم رو بدونید:
خیلی از فروشنده‌های کانفیگ، پرداخت رو به‌صورت کارت‌به‌کارت انجام میدن که بتونن مشتری بکشن این کارت‌ها معمولا دو حالت دارن:
۱️⃣ یه سری فروشنده‌ها مدت طولانی از یک کارت ثابت استفاده می‌کنن و ظاهرا مشکلی هم براشون پیش نمیاد (پارتی دارن)
۲️⃣ یه سری دیگه مدام کارت عوض می‌کنند بصورت روزانه و هفتگی ؛ بحث اصلی ما با این دسته‌ست.
مشکل از جایی شروع میشه که ۱۰۰٪ از این کارت‌ها اجاره‌ای هستن.
معمولا بعد از مدتی حساب مسدود میشه و صاحب کارت باید بابت تراکنش‌ها توضیح بده و درگیر دردسرهای پولشویی و قضایی بشه.
از اون طرف، تمام تراکنش‌ها داخل سیستم بانکی ثبت میشن:
شماره حساب، اسم و شماره طرفین، مبلغ، زمان تراکنش و...
حالا اگر مشخص بشه اون حساب برای فروش VPN یا کانفیگ استفاده میشده، طبیعیه که تراکنش‌ها و افراد مرتبط بیشتر بررسی بشن.
که ۱ ماه پیش خبر این تو کانالها پخش شده بود از پیش شماره Vaja برای کانفیگ فروش هایی که مستقیما از کارت خودشون استفاده می‌کردن پیام رفته براشون
🤔
حالا میپرسید راه‌حل چیه؟
تا جای ممکن کارت به کارت نکنید.
بهتره به جای این مدل پرداخت‌ها از روش‌هایی استفاده بشه که مستقیم به کارت‌به‌کارت نباشن؛
مثلا پرداخت از طریق تراست ولت یا صرافی‌های ارز دیجیتال مثل نوبیتکس یا بیت‌پین و خیلی صرافی های دیگه که ثبت‌نام تو این صرافی ها هیچ سختی نداره و عرض ۵ دقیقه ثبت‌نام میشه کرد
در نتیجه پیشنهاد میشه تا حد امکان از کارت‌به‌کارت به حساب‌های متفرقه خودداری کنید
میگید به خودتون چرا مشکلی نداره که؟ اینم فکرشو بکنید که بابت کانفیگ ۲۵۰ تومنی برید خودتون رو به دردسر انداختید و حالا باید جواب هم پس بدید
🥴
این موضوع احتمالا در هفته‌ها و ماه‌های آینده بیشتر درباره‌ش خواهید شنید که  از No Caller ID تماس گرفته شده. خیلی‌ها الان جدی نمی‌گیرنش، ولی بعدا درگیر این موضوعات میشن که دیگه خیلی دیر شده
ℹ️
هدف ما ترساندن نیست و صرفا جهت آگاهی و امنیت شما اطلاع رسانی شده
❤️‍🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/4784" target="_blank">📅 18:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
قابلیت جدید Codex
با یک کلیک انتقال پروژه‌ها/گفتگوها بین Claude و Codex
- استفاده از قدرتمندترین مدل برای کدنویسی هوش مصنوعی
- صرفه‌جویی در زمان و بهبود کار تیمی
https://chatgpt.com/codex/switch-to-codex/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/4782" target="_blank">📅 17:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Balancer_ArchiveTell.html</div>
  <div class="tg-doc-extra">28.3 KB</div>
</div>
<a href="https://t.me/archivetell/4781" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Balancer.html</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/4781" target="_blank">📅 16:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎉
۸ ابزار هوش مصنوعی فقط برای سرگرمی
1️⃣
هنرمند تتو – طراحی خودکار تتوهای خلاق
🔗
https://tattoosai.com
2️⃣
صحبت با کتاب‌ها – گفتگو با متن‌های کتابی به‌صورت صوتی
🔗
https://books.google.com/talktobooks/
3️⃣
عکس‌های قدیمی – بازسازی و رنگ‌آمیزی تصاویر تاریخی
🔗
https://myheritage.com/ai-time-machine
4️⃣
سلام به گذشته – تعامل با شخصیت‌ها و رویدادهای تاریخی
🔗
https://hellohistory.ai
5️⃣
جعل خود – ساخت صداهای مصنوعی شبیه به خودتان
🔗
https://fakeyou.com
6️⃣
وعده غذایی غیرواقعی – منوهای خیالی و جذاب برای لذت بصری
🔗
https://unrealmeal.ai
7️⃣
تغییر چهره با هوش مصنوعی – سوئیچ و ترکیب چهره‌ها به‌صورت لحظه‌ای
🔗
https://hey.reface.ai
8️⃣
تغییر صدا – تبدیل صدا به انواع شخصیت‌ها و افکت‌ها
🔗
https://voicemod.net
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/4780" target="_blank">📅 16:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Balancer.html</div>
  <div class="tg-doc-extra">13.2 KB</div>
</div>
<a href="https://t.me/archivetell/4779" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
ابزار اختصاصی ساخت کانفیگ بالانسر برای v2rayNG
🚀
> خسته شدی از بس دستی بین کانفیگ‌ها سوییچ کردی تا یه سبزشو پیدا کنی؟
با این ابزار ساده، تمام کانفیگ‌هاتون (حتی لینک‌های نامرتب با پروتکل‌های جدید مثل xhttp) رو یکجا وارد می‌کنید و در ازاش یک «کانفیگ کاستوم هوشمند» تحویل می‌گیرید.
>
⚡️
چیکار می‌کنه؟
> این کانفیگ به صورت خودکار پینگ تمام سرورهای شما رو (مثلاً هر ۶۰ ثانیه) چک می‌کنه و ترافیک شما رو بدون قطعی روی
سریع‌ترین سرور
میندازه (LeastPing).
>
🔒
۱۰۰٪ امن و آفلاین (توی مرورگر خودتون اجرا میشه)
>
📥
کافیه فایل HTML رو باز کنید، کانفیگ‌ها رو بدید و خروجی JSON رو توی v2rayNG کپی کنید. فق دستی کپی کنین
‌
🆔
@archivetell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/4779" target="_blank">📅 16:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستان برنامه نویس خیّر اندروید کسی هست؟
کار اونقدی سخت نیست
دایرکت یا پی وی پیامم بده
کار عام المنفعه هست برای اتصال به اینترنت</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/4778" target="_blank">📅 16:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e40uOADEzJz21ro9xSydr_B6J5EERZSs8Yi776TqlHDePtRqDiJ1-GJbhKRBgmlloCMN82ibYdjsMv9nHOKn-0rPEfEKtLh-w3K8D_bpoVUQhIlcrxBo4h7f95VceKUoXPlNBDR5O3NIaIrwM9FdaUpQyZnYvsid4XG_TUv2d_At2nGuV7fmwcJMCkJg57B_cGuMWS4DeGvuUOyihw5seNZtcjOMGCJat-YHyvLqUVbgXLWxq0nS2OvNooeC0ydkIJWodpwrjFEkf_PkAQpJ_xa3glvEU1q6zyaVGEbW-fkuI6X6PSdl1JB0LkNo2HQLaLT3YvHWFjxVgYdCnoCWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🌐
اضافه شدن سرور های جدید ( اهدایی عزیزان
❤️
)
🔺
بهینه شدن لیست BEST
⚡️
اضافه شدن sni های جدید
●  کانفیگ ساز جدید فقط روی
نسخه 1.0.3 پروژه
کار میکنه
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/4777" target="_blank">📅 14:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ربات فشرده‌سازی فایل‌های PDF
📖
📚
@PDF_Compress_Robot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/4776" target="_blank">📅 13:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UgVfHDoIRWuY-diQ8v4vThPVkvFBgtteQQZk9HDmrCPyP4V2aDi6Ig74XPxvcRb90XKsTq5QO2TCtyzs8loh_QGYJ_NWP1j13qc1_mFAI6hsR9CvCZNbnJT0YRPJfBOJeajCAuF6UvH7I4Bnb6cZj9mSCd1c-Yf-0QqtdhdnqqqgkAuFMOCMNsBljNqi5CdmUNyA64uZ-tWpZcfJudNZO6sHxKYYvfCPNo6DxMWVihoMoz4jFmuWJ-HG6IUsWmVp_Xnkyjp6GISlDVjVDmHpoQpwcj9JCL4hm1GRW0Jg6DOrXAul2x_jo0cVW8aomc3tZS1jRKr063joI4NHNpXnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
MattDownloader
نسخه اول منتشر شد
❤️
می‌خوای ویدیو از یوتیوب (یا هر لینک دانلودی دیگه رو) بدون VPN بگیری؟ با MattDownloader این امکان میسر میشه:
GitHub Actions روی فورک خودت فایل را از اینترنت دانلود میکنه و آماده‌اش میکنه؛ تو فقط با اپ از همون گیت‌هاب بدون اینکه روی گوشی VPN لازم داشته باشی، فایل نهایی رو می‌گیری و ذخیره می‌کنی. یعنی گوشی بیشتر با گیت‌هاب حرف میزنه، نه مستقیم با سایتی که برات مسدود یا ناپایدار است.
چطور کار میکنه؟ لینک را به اپ می‌دهی (مثلاً لینک ویدیوی یوتیوب که به لینک مستقیم تبدیلش کردی)، ورک‌فلو روی ریپوی تو اجرا میشه، بعد اپ فایل آماده را از مسیر jobs میخونه و روی دستگاه دانلود میکنه.
🎬
مناسب برای ویدیوهای یوتیوب و لینک‌های سنگین
⚡
ست‌آپ یک‌بار با توکن و آدرس فورک
📥
دانلود نهایی از گیت‌هاب
🖼️
امکان ذخیره در گالری برای ویدیو/عکس
راهنما و APK اینجاست:
https://github.com/matthewnet/MattDownloader
آخرین نسخه برای نصب:
https://github.com/matthewnet/MattDownloader/releases/latest
تجربه‌تون را بفرستید
💙
برای دریافت نسخه‌های بعدی:
@mattspoof</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/4774" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت) خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟ ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها،…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/4773" target="_blank">📅 12:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLXGDyp6-2l9idUZnkJCTflofFazmDeCxWmQwOrNiKlkV-aqQuwUIBxKDksPIv8QMiWMnZOMIQjfl87CDHF0QCoaq9hUK1ix2nF1gVDCV_fGHCeb5cFiG608XbqghFI_f5q-NOIQeiXZxxO6qERiFEXngh9e52Kdn9XN-qIhz5HIcUAmti0cDM-v8lH-oC_q7r-VfTsGA-Z4sI6iJreQRArbpIwHGxkaTNU0dzeIvWkklekJLUbeIbnCzX-_oHTZDhbZgh6tBf5D94Ce0OgkBOWvIoBXJyPxo85QGOgaU2QSin37tLLbaRUG_NKlDJBJYX-k6GNxeHaVWM_VHXsAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت درحال احراز کردن IP سرور های ایران هستش. اینطوری صاحب هر IP برای حکومت کاملا مشخص میشه.
قبل از این، دیتاسنتر ها احراز رو خودشون انجام میدادن اما برای اکانتی که میسازید نه IP سرور. اگه حکومت هر دستوری بابت پیگیری IP خاصی میداد، باید از فیلتر ISP عبور میکرد که میشد با روش هایی دورش زد یا گردن نگرفتش
اما الان خود حکومت دیگه میدونه کدوم IP برای چه شخصی هستش...
@ArchiveTell
Source</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/4772" target="_blank">📅 12:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ربات تبدیل صدا به متن رایگان
@sedatextbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/4771" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
آموزش صفر تا صد راه‌اندازی تونل ریورس (Reverse Tunnel) در 3x-ui
---
رفقا سلام!
✋
امروز یه آموزش پایه‌ای اما به‌شدت کاربردی داریم برای راه‌اندازی تونل Reverse بین دو پنل 3x-ui (سرور ایران و خارج).
ممکنه بسته به شرایط سرورتون نیاز به یه سری تغییرات ریز داشته باشید، اما ساختار اصلی و تضمینی همینه!
مرحله ۱: ساخت Inbound روی سرور ایران
🇮🇷
1️⃣
وارد پنل 3x-ui سرور ایران بشید و به بخش Inbounds برید.
2️⃣
دو تا کانفیگ باید بسازید:
🔸
کانفیگ اول (برای Tunnel):
• Protocol: VLESS (یا پروتکل دلخواه)
• Transport: WebSocket
• Path: /tunnel
• Remark: tunnel
• Port: حتماً یکی از پورت‌های پشتیبانی‌شده توسط CDN (مثلاً 8080 یا 2082)
🔸
کانفیگ دوم (برای User):
• Protocol: VLESS
• Transport: WebSocket
• Path: /user
• Remark: user
• Port: یکی از پورت‌های CDN (مثلاً 8080)
⚠️
نکته به‌شدت مهم: حتماً از پورت‌هایی استفاده کنید که CDN (مثل ابرآروان یا کلودفلر) اجازه می‌ده؛ مثل: 80, 443, 8080, 2052, 2082, 2086, 2095.
مرحله ۲: تنظیم Reverse روی سرور ایران
🇮🇷
1️⃣
برید به بخش Xray Config و بعد تب Reverse.
2️⃣
یه Reverse جدید بسازید (بخش Portal):
• Tag: portal
• Domain: یه اسم دلخواه (دقت کنید که روی سرور خارج هم باید دقیقاً همین باشه).
3️⃣
حالا Mapping رو انجام بدید: کانفیگ tunnel رو وصل کنید به user (یعنی Tunnel ➔ User) و ذخیره کنید.
مرحله ۳: انتقال کانفیگ به سرور خارج
🌍
1️⃣
از کانفیگ tunnel (که تو ایران ساختید) خروجی (Export) بگیرید.
2️⃣
وارد پنل سرور خارج بشید و برید به بخش Outbounds.
3️⃣
یه Outbound جدید بسازید و لینک ایران رو اونجا Paste کنید.
(دقت کنید که دامنه‌تون باید پشت CDN باشه و به آی‌پی سرور ایران اشاره کنه).
مرحله ۴: تنظیم Reverse روی سرور خارج
🌍
1️⃣
تو پنل خارج برید به بخش Reverse.
2️⃣
یه Bridge بسازید:
• Tag: bridge
• Domain: دقیقاً همون دامین/اسمی که تو سرور ایران گذاشتید.
• Interconnection: همون Outboundی که تو مرحله قبل ساختید.
• Internet: روی direct یا freedom تنظیم کنید.
3️⃣
سیو کنید و تمام!
✅
نتیجه چی می‌شه؟
سرور خارج به ایران متصل می‌شه ➔ تونل ریورس برقرار می‌شه ➔ کاربر به سرور ایران وصل می‌شه و اینترنت آزاد رو از سرور خارج دریافت می‌کنه!
💡
نکات طلایی و عیب‌یابی:
🔹
مسیرها (Path): پث‌ها (مثل tunnel/ و user/) باید مو به مو یکی باشن. یه اسلش (/) اضافه یا کم، کل کار رو خراب می‌کنه.
🔹
نقش CDN: بدون CDN این روش یا کار نمی‌کنه یا شدیداً ناپایداره. حتماً پشت CDN باشید و تیک WebSocket رو هم تو تنظیمات CDN روشن کنید.
🔹
نیاز به TLS یا Nginx: استفاده از Nginx الزامی نیست ولی برای تمیزیِ کار، روت کردن پث‌ها و استفاده از پورت 443 خیلی جوابه. TLS هم بستگی به شبکه داره، بعضی جاها فقط با 443 جواب می‌ده.
🔹
مشکل وصل شدن بدون اینترنت: اگه وصل شدید، چند کیلوبایت سند و ریسیو داشتید ولی اینترنت نبود، شک نکنید مشکل از ایناست: اشتباه بودن Path، مشکل تو هدرهای Upgrade/Connection، مپ نشدن درست Reverse یا گیر دادنِ CDN.
📌
#آموزش
#تونل
#ریورس
#Reverse_Tunnel
#سنایی
#3x_ui
#vless
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/4770" target="_blank">📅 11:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سایت ارسال کانفیگ
http://m.ulni.ir
https://sphost.theazizi.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/4769" target="_blank">📅 09:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آپلودر های فعال
https://up.zaringo.sbs/
https://rozup.ir/
https://uploadgirl.ir/
https://seup.shop/
http://uplod.ir
https://up.20script.ir
https://punkpaste.ir
https://my.files.ir
https://toolschi.com/tools/upload-center
http://nixfile.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4768" target="_blank">📅 09:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ربات کاهش حجم ویدئو رایگان
@mediaEasyBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4767" target="_blank">📅 09:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کاش زودتر آیفون ۱۸ بیاد که آیفون ۱۷ ارزون‌ تر بشه بتونیم تن ماهی بخریم.
@archivetell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/4765" target="_blank">📅 00:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">IR NETLIFY V10.2 • BACHELOR EDITION
⚡️
تغییرات اصلی نسبت به نسخه‌های قبلی: ۳ تب کامل و حرفه‌ای:
⚡️
Generator — با پشتیبانی از چندین دامنه نتلیفای (داینامیک)
🔄
Replacer — جایگزینی دامنه با قابلیت توزیع خودکار بین چند دامنه
🔧
Tools — ابزارهای پیشرفته (Rename…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/4764" target="_blank">📅 00:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👾
لیست دانلود برنامه ها با نت ملی
1️⃣
WhiteDNS
1.1.0
(نسخه ی رسمی)
4️⃣
NekoBox v8a
●
NekoBox v7a
1.4.2
7️⃣
The Feed
0.17.5
📱
Telegram
(گوگل پلی)
12.7.2
📱
Telegram
(رسمی)
12.7.2
📱
Telegram
(Windows)
12.7.2
📱
Whatsapp
2‌.26‌.17.‌72
💬
Instagram
v415.0.0.36.76
👑
ShiroKhorshid
2026.03.17
5️⃣
Mhrv Rs
v1.9.14
📶
Npv
123
📶
V2box
5.3.4
📶
V2ray Ng
2.18
📶
V2ray Ng
(Windows)
3️⃣
Am tunnle
(pro)
37
3️⃣
Am tunnle
(lite)
🕊
Slipnet
2.5.3
2️⃣
Masterdns
1.0.9
📶
Open vpn
3.71
📱
Happ
3.20.4
💻
Happ
(Windows)
📶
Psiphon
462
📶
Psiphon
(Windows)
8️⃣
Bd net
104
6️⃣
Mahsang
15
📶
http injector
6.5.0
📶
Wireguard
1.0.20260315</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/4763" target="_blank">📅 23:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xyh63sQn2I2dlWYIVGbOh6sFpG21LSu9NgKOO8KPhsGeiidUlgs10uUGAnX_tNoxbmRHrSKYZ2rrnkH8TRAk-3N5kYW6H_ukU9aa1BS0Ar1xEUkvjvZPJ5PUUhrii7A8WHAzGjWZLTMZtdfE_nw2L2kqOdNNlBt2hLN6sSVHUJrOF22QFZzvTrMYTNnQ5egtID_7A3CC0CNten1Z-6T2odBHDDjs0NxWert2Qgz4DIG5Uyw4oDqa4dMSEaN0JL-nzr4uMZWujVcZXsYFGeCVhuv5BwP9bCbUhfJhea2mAOC3dswPkfb1vSenIZEasTg1vRZ09m97MfbPIo_IofuEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
بومی‌سازی هوش مصنوعی برای توسعه‌دهندگان.
ترجمه YAML، JSON، TXT و محتوای چندزبانه با حفظ ساختار، جایگزین‌ها، متغیرها و قالب‌بندی.
@LocalynBot
⭐
کد منبع گیت هاب
https://github.com/LocalynAI/LocalynAI
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/4761" target="_blank">📅 22:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">YT_dL.ipynb</div>
  <div class="tg-doc-extra">22.5 KB</div>
</div>
<a href="https://t.me/archivetell/4760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/4760" target="_blank">📅 21:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت)
خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟
ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها، فایل‌های صوتی و حتی پلی‌لیست‌های کامل یوتیوب رو با بالاترین کیفیت ممکن (تا 4K) دانلود کنید.
💡
هدف و مزیت اصلی این اسکریپت چیست؟
تمام فرآیند دانلود توسط سرورهای قدرتمند گوگل انجام میشه. این یعنی شما می‌تونید ویدیوهای چند گیگابایتی رو در چند ثانیه دانلود کنید، بدون اینکه حتی یک مگابایت از حجم اینترنت گوشی یا سیستم شما کم بشه!
🛠
چطور از این ابزار استفاده کنیم؟ (بدون نیاز به کدنویسی)
استفاده از این اسکریپت به شدت ساده است و دارای یک رابط کاربری (فرم گرافیکی) است:
1️⃣
اسکریپت را در گوگل کولب باز کنید (فقط به یک اکانت جیمیل نیاز دارید).
2️⃣
در فرمی که می‌بینید، لینک یوتیوب رو پیست کنید.
3️⃣
کیفیت ویدیو (مثلا 1080p) یا فرمت صوتی (مثلا MP3) رو از منوی کشویی انتخاب کنید.
4️⃣
دکمه اجرا (Play
▶️
) رو بزنید و تمام! اسکریپت به صورت خودکار ابزارهای لازم رو نصب کرده و دانلود رو شروع می‌کنه.
📁
فایل‌های دانلود شده کجا ذخیره میشن؟
در تنظیمات فرم، گزینه‌ای برای اتصال به گوگل درایو وجود داره. اسکریپت به صورت خودکار به درایو شما متصل میشه و فایل‌ها رو در پوشه‌ای به نام YouTube_Downloads (یا هر اسمی که خودتون در فرم بنویسید) ذخیره می‌کنه. بعد از اتمام کار، کافیه برنامه Google Drive رو باز کنید تا فایلتون رو اونجا ببینید!
🔗
لینک ورود به اسکریپت:
[لینک گوگل کولب خود را اینجا قرار دهید]
👇
اگر سوالی در مورد نحوه استفاده داشتید توی کامنت‌ها بپرسید.
Developer : Samad.R
@ArchiveTell
‌
#یوتیوب
#دانلودر
#گوگل_کولب
#ترفند_آموزشی
#ابزار_کاربردی
#دانلود_از_یوتیوب</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4759" target="_blank">📅 21:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c7bc1a6d.mp4?token=IiDaz1H6GzAVlbrwr0JA2RAN0sJCCfIudasgNnPAbplbHon1ua3tAmkS0QcY7f004E1c0FivZdOCAzHSeD3EY4IdRhPcoPQ7zyd5PnFsnBNWQoJ9e4Bv1cnSiusMdjRE349J5inEmw4f-K9DQP5SlRKfVyFT_cgvCs6fjkgTdMIVEGBRNG9f5NFIgOum5TBESau9dTF-pHJL1vZ_o_lKLwCySzbfXa-EOGZRZmUEgrZj16Z9CsnTdP6IgJHfO1bQCclxhTaTJByDqNbh6szzyOGlckB3eia1GJU2DPNskTXcl15CzL9DiJ0mbxs5f4ldEM7cH5iB9oiReawUTbuR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c7bc1a6d.mp4?token=IiDaz1H6GzAVlbrwr0JA2RAN0sJCCfIudasgNnPAbplbHon1ua3tAmkS0QcY7f004E1c0FivZdOCAzHSeD3EY4IdRhPcoPQ7zyd5PnFsnBNWQoJ9e4Bv1cnSiusMdjRE349J5inEmw4f-K9DQP5SlRKfVyFT_cgvCs6fjkgTdMIVEGBRNG9f5NFIgOum5TBESau9dTF-pHJL1vZ_o_lKLwCySzbfXa-EOGZRZmUEgrZj16Z9CsnTdP6IgJHfO1bQCclxhTaTJByDqNbh6szzyOGlckB3eia1GJU2DPNskTXcl15CzL9DiJ0mbxs5f4ldEM7cH5iB9oiReawUTbuR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
گوگل در حال آزمایش Gemini Omni
✅
قابلیت تولید ویدئو – جایگزینی مدل‌های Veo با یک خط تولید یکپارچه.
✅
همزمان خروجی صدا و تصویر – ترکیب چندرسانه‌ای پیشرفته.
✅
معرفی رسمی – انتظار می‌رود در Google I/O هفته آینده به‌صورت کامل اعلام شود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/4756" target="_blank">📅 19:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram-X-0.28.3.1785-arm64-v8a.apk</div>
  <div class="tg-doc-extra">56.6 MB</div>
</div>
<a href="https://t.me/archivetell/4755" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی Telegram x
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/4755" target="_blank">📅 18:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrQiqqsqN5J3mOMKHLseTbehTvXzi1DOnP8CPJ6k2_xbnM1b_4aJVV8pGlOdATGCMJY2woU73w1ysQwF7y8S2WLIHOk_pUmIehX4RiIMg4vkw4jZr0KMFqhajVv30T4Qe1T-37JdpI030QUe31lpYjX1PRsSRKPy56Uhd1o_18JZ4-j7COf9hyz7zJdNG7EnE__kqtblJPKNd5Jb0lDTdg7SvVv7zSdUQHzihARp9wYy-Oyb73LiyZalyDZYNRxethVSjCjD6IKOL8QAFSWyS4Otvza6ssVQJmIhgvJPD1e-GmXrLp89uCyJYq-kqIJ6QsRrWkzCrniHbd45_JIMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ویژگی‌های کلیدی در آپدیت جدید
🛰
امکان اسکن با DNS شکن
(نسخه آزمایشی، ممکنه کار نکنه)
⚙️
کنترل دستی پردازش‌ها (Thread Control):
قابلیت تنظیم تعداد تردها توسط کاربر برای جلوگیری از کرش کردن (خطای Signal 9) در ترموکس اندروید.
💻
نمایش زنده در ترمینال:
نمایش آنی کانفیگ‌های متصل در صفحه ترمینال، علاوه بر ذخیره در فایل.
🛡
عبور از فیلترینگ هوشمند (DPI):
تست واقعی لایه اپلیکیشن (HTTP Status) برای جلوگیری از دریافت پینگ‌های فیک و دراپ شدن پکت‌ها.
🌐
دیتابیس داخلی غنی:
شامل بیش از ۷۰ دامنه CNCF/Cloud-Native و بیش از ۱۰۰ آی‌پی‌ تمیز CDN (بدون نیاز به فایل‌های متنی جداگانه).
https://github.com/johncarterjourney-rgb/NETLIFY-SCANNER</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/4754" target="_blank">📅 18:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تا ۱۰ روز دیگه جنگ میشه..</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/4753" target="_blank">📅 17:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">77.9 MB</div>
</div>
<a href="https://t.me/archivetell/4752" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی Telegram 12.7.2
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/4752" target="_blank">📅 17:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یکم زمانبره. لیست ایپی ها و sni ها افزایش پیدا کرده و تستش هم دقیق هستش. برا همین طول میکشه. ببرین تو کلاینت Exclave یا V2ray همشون پینگ میده.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/4751" target="_blank">📅 16:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtZ3sMq-qz_iK5iUmWc2UGU_7CKZ9-iqn_QrRBrZPGDP9gU2OKDvoElx0CwzOi740YOJMN_N83O0QWEhU9tAQY7A9KR3PDHtyIsXhFcFRZD-JtWXvMNnAr0pOro2QJrcvfSaMAc7bmgpMoWhZ4LwFyIY9-pHCNWUSscz4-pE7Z4gekFzayssUPmGFJ2UrSs5OjiauwvpLGOZ-xhFT-iRXBFAli4LNiF2H_5v9TkubOeIKhycufX0HGHDABFVlbRRL7pialpDvFi9NpK5IUc6UwHVCeS3bypbiLIgB_2_VcBQtEOgJZPFE3HE1ZIRIrdVx7n11GGa1EBBcjWhGMeWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ابزار NETLIFY-SCANNER (نسخه V1 Pro)
🔆
اسکنر IP و SNI های نتلیفای  ---  رفقا سلام.
✋
اگر با کانفیگ‌های نتلیفای کار کرده باشید، می‌دونید که خیلی وقت‌ها پینگ دارن ولی عملاً وصل نمی‌شن (پینگ فیک). این اسکنر پایتونی رو برای حل همین مشکل آماده کردیم.  تفاوت اصلی…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/4750" target="_blank">📅 15:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad--AjRoBWd_-4JZAWCx00ppekfX6OStYollTcmSYLWR6-DKYodAmNafS6NksL_m9OSrOpb1pa5NoRZyAv2im8_Df3XOKXU_QFHKnTjQ_7iYtSem62mqAvrR0mkumGM1MedsAbVfFFz91Ze3uJoHRTKVhh23N9T3ihZpR1uig_6Qw_8E9NpwxkJjHl-N1NWvMV8hkHULLw6J8cRshLXlfEZ6iWQUJm94z3jNNsqZKpBB1EXXlonXw3fkbHj5bM-9GDhXn0PqzYNiEooSmXz1nBfnsKj-spr3lX7aODk4QfJzZWWAVtwzqokxiZNpJkwlLMFZ5x620B7a3AYRbkqRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
اسکنر IP و SNI های نتلیفای
📌
github.com/IR-NETLIFY/NETLIFY-SCANNER
🔺
مواردی که ok میشن بدون نیاز به شکن وصل میشن براتون
🔸
دی ان اس شکن رو کامل حذف کنید از سیستم
🔹
یک بار مودم یا نت رو خاموش روشن کنید تا آیپیتون عوض شه
🔸
بدون هیچ DNS و فیلترشکنی اسکنر…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/archivetell/4749" target="_blank">📅 15:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9PtY_d0kgQhO0GrLcW7XFDz1FJReSz82oke2iTQyr8BxVhm75OLk6F0yOMaA4swCy9hw1NAsKCRmrsxk7IJscvPLDWB8oozKNsgll5aG1iT46XNW4WMkT8UoCtiFsZDatCuHHPP_W8C28yfQKTsQRTHzm8ACHXrPyERlQMM5yOQNTzUKIWORa2vI3b8FrPORKjedwvzJimlp6veeLM2FKyAuGwAo98y54ENYmFVjxsHWBXQ3P7dhkOWeIKiyiz7CqIa4CKF0upY2Dk1XJY_1EWcVFh-PG1_KSJhGAn_sLW1ULUmFXL8nSAp4YzZYztYSiXSk6Y7nfry1dzHQPFYzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🌐
قابلیت انتخاب چند سرور
🔺
اضافه شدن شمارنده تعداد کانفیگ های ساخته شده
⚡️
اضافه شدن بررسی کننده لینک نتلیفای
●  کانفیگ ساز جدید فقط روی
نسخه 1.0.3 پروژه
کار میکنه
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/4748" target="_blank">📅 13:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4746">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns  قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب…</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/4746" target="_blank">📅 12:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4745">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">install_3x_ui.sh</div>
  <div class="tg-doc-extra">22 KB</div>
</div>
<a href="https://t.me/archivetell/4745" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این اسکریپت نصب آفلاین پنل ثنایی هست.
برای افرادی که اعتقاد به بکدور دارن و به میرور ها اعتماد ندارن.
فقط کافیه که توی بخش Releases یک نسخه انتخاب کنید و متناسب با CPU سرور یک نسخه دانلود کنید. و انتقال بدید به سرور.
در نهایت این bash اسکریپت رو اجرا کنید.
bash install_3x_ui.sh
به شکل اوتوماتیک بدون ssl نصب می شه.
فقط بعد نصب با دستور x-ui پورت و یوزر پسورد تغییر بدید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/4745" target="_blank">📅 11:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4743">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLs6fCx6CwG44MFhRr4fbfp8cwGz1at19sy9xzAxaR3GFIbtPaoMFASgfFFOqJhV2NSkN5tAuLyyiPz5fPlP8TYZ-qyV6buWVMI5tGFcgbv3hmN4Rxdl6CVY8cEVFjWk6yrJVESVKU2jLHpxjaVxhPqpuOwcp5pqr61tmk9oj_acMYdleNC0HJ4sF2rJzHs-7BBqHIcCVaDSSymtOTwqt-10hQ8jC5ve_1FI8kJIwwjfDjpCKf-9EJGR6ovuCD_KvfNvUeqJkJWnkI0KivsKsw8KoUS44Vt0c5RoLQO467pQmcf_8Do7hZm02_kcMmrewUaPUoxxlpoOfeKp7xy5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۳ ابزار هوش مصنوعی که ارزش ذخیره در گنجینه شما را دارند
💎
1.
Claude.ai
— حل مسائل
2.
PicWish.com
— حذف پس‌زمینه‌ها
3.
Perplexity.ai
— تحقیق درباره هر موضوعی
4.
Suno.ai
— ساخت موسیقی
5.
Canva.com
— طراحی گرافیک
6.
ElevenLabs.io
— کپی صدای افراد
7.
Grammarly.com
— اصلاح نوشتار
8.
Luma.ai
— ساخت ویدیو
9.
RecCloud.com
— خلاصه‌سازی یوتیوب
10.
Runway.ml
— ویرایش ویدیو
11.
Descript.com
— ویرایش پادکست
12.
Syllaby.io
— ویدیوهای بدون چهره
13.
Skysnail.io
— تصاویر کوچک ویروسی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4743" target="_blank">📅 10:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4742">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚀
نسخه کاملا آفلاین 3X-UI (ورژن ۳)
فقط این چند دستور رو به ترتیب اجرا کن
-  دانلود فایل نصب با نت ملی
wget https://boto3.s3.ir-thr-at1.arvanstorage.ir/3x-ui-3.0.tar.gz
-  استخراج فایل‌ها
tar -xzvf 3x-ui-3.0.tar.gz
- دادن دسترسی اجرا
chmod +x install.sh
- نصب یا آپدیت پنل
./install.sh
📌
نکته:
این نسخه کاملاً آفلاین نصب میشه و نیازی به GitHub یا دانلود فایل اضافه نداره.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/4742" target="_blank">📅 10:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4741">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سایتی جایی که دامنه رایگان (هرچی) بده بفرستید</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/4741" target="_blank">📅 10:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4740">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مجموعه‌ای از برنامه‌های کار راه بنداز آزمایشی!
سلف‌هاست شده، به رایگان، برای همه.
https://hxlab.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4740" target="_blank">📅 08:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4739">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR7q0sUJFEVVAZ_xT2nK8Wqd7CO9Z3z01shchigaRf86yP72bzrk26_kI2IoOWG-Ck6M0XE4explVwUOgpleW10LP64Xawx0ZRtkBs8gFfeBRFOPXF-NyqgXQNw-lgf5nyZHIhXIDoZeFR-QA6NvbdF4x2GU51HYCOjQnGBxq_pU8Uv2c9-9PK5v6wLHy-yHw1QHXyJ1T_rQUrm4hfT6GDYxSjrOKuyNt4q1p-X2qQKT9sbuobou7Tnn54ErW-vMaqM20FoIOA0qmBBtiGQw59ZP2ZUtQyRMfabsbv7wTlVkPu4ZU9vAUDU_LEPSXnVQQpiq8e_sbCbUr1hI5nBSwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
اسکنر IP و SNI های نتلیفای
📌
github.com/IR-NETLIFY/NETLIFY-SCANNER
🔺
مواردی که ok میشن بدون نیاز به شکن وصل میشن براتون
🔸
دی ان اس شکن رو کامل حذف کنید از سیستم
🔹
یک بار مودم یا نت رو خاموش روشن کنید تا آیپیتون عوض شه
🔸
بدون هیچ DNS و فیلترشکنی اسکنر رو ران کنید
🔺
می تونید کد رو روی سرور ایرانتون ران کنید اگه چیزی پیدا کرد تونل نتلیفای بزنید به خارجتون وصل شید (
یه کانفیگم بدید دایرکت
)
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/4739" target="_blank">📅 02:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ultra_downloader_pro.html</div>
  <div class="tg-doc-extra">34.5 KB</div>
</div>
<a href="https://t.me/archivetell/4736" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Untitled 1.mkv</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/4736" target="_blank">📅 02:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فکر کن عراقی که سنگشو به سینه میزنی تلگرامش رفع فیلتره
افغانستانی که مسخرشون میکنیم برای اومدن به ایران 5g اوکی کردن
سوریه ای که میگیم آدم برای دشمنشم نخواد پرداخت با مسترکارت اوکی کرده
اونوقت ایرانی خوشحال میشه که گیگی ۱۸۰ رو خریده ۱۳۰....</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/4734" target="_blank">📅 23:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4733">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">میگم شمام دیگه خسته شدید؟
😕
@archivetell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/4733" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4731">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0MdC_KqosxSTHlwrsC0oERwh74yqYhMel8x7PVPyB9915XtZKbjrbA4tF6p-OYOqP9ATljXGcQG4fqIcouZPr5ID0myrHjGyhzfwYTxeOkCVm1s9TeLVqjLm8bUyeaKDDl4zXMJ7BuF1dTxDDkUCChMuyOytJ5yk3Tl45-HiPJVBJ1Jzr7Klpoeb5Q4dPJO7-Ih347qnO0YpL3wtv4uSXhUZaT7FDz3ALbWfOZ58g4bMFFZvkrVcqU4njJjtNJSR9h-g5za6yMn8TS_BLdUjaoGwGC1qG7PPU2_QuhjnEWj-UaOFoMB3ESbDe-Nb80NOwUCCZNZPcQq8FNdQlpNzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufkBLfuXirCm6rXZQ-IMLQdlyWO9CX48q60NolmDHqBijvKjFWt_2ZQniOLxv4PqyYL8rNw9_g0-vMnivlUgZ7LiPe9u8Ws3W5KBh4RQRtEXEYPR0tdCzHaErPnsoIZJR-ygo4rp51vmQF_RY8TFv19cZLCc94A_pfmERETWelcVi9mWU62uTGdNJ--YaNaN2H9CQEJsXsvIc5V8cdgnp4l4oBr5kr4J-ehyPnVKvWVRbJLLhS_lEJOz83WFA4SYY1CR912KyGOa5s7YGgEc50VlWp7Dr4jbnywJn7Ble7VTxggTGpoTmiUY6xFvO_ozkxkzCujXMQRimPbjNmoxhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns  قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/4731" target="_blank">📅 22:29 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4730">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">client_resolvers.txt</div>
  <div class="tg-doc-extra">9.7 KB</div>
</div>
<a href="https://t.me/archivetell/4730" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns  قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب…</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/4730" target="_blank">📅 22:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4729">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns
قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب برای
🌐
وب‌گردی،
📱
تلگرام،
📱
هوش مصنوعی و ...
(بدرد اینستاگرام، یوتیوب، دانلود فایل‌های حجیم و کارهایی که نیاز به پینگ پایین دارن نمیخوره)
✔️
اگر برای خودتون و دوستاتون  نیاز به سرور کامل دارید، سرورهای StormDNS به همراه پنل مدیریت در اختیارتون قرار میگیره. کاملاً مستقل و شخصی
برای خرید سرور شخصی پیام بدین:
🚀
@Mo3inh</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/4729" target="_blank">📅 22:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4728">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جایگزین گوگل میت
https://meet.theazizi.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4728" target="_blank">📅 21:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4727">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ربات سرچ عکس در Google , Bing , Yandex و TinEye
@ImageEyeBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4727" target="_blank">📅 21:18 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4726">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فشرده‌ساز رایگان ویدیو و صدا برای کاهش مصرف اینترنت
📉
📶
@Compreseebot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4726" target="_blank">📅 21:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4725">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELKuNtNHkbstIIFkdjd0oc3hh-yOYq_dP7eXTuxdV2xsA_z-ZGvUItlqEzXwj0SPdRvbaCK3mxZpFaIwgL5fFKNBneI-TevlWzk2TNmC4ul2EZSi5lQUxxAptlnuT8RNWvnZIJf8bYn5AmbTihLE6TzdX-dWsQTVCytx9AcK2eWEX8LhX59JZaW6t3EMaQ07p_B8nI89MmO56-gPww5sw8QuaLD5_GPjWmTvHBHddW1A842MZUd0hFRyTo9Qt_1nerzwPKNKQznhcbLKlVYbqXoPn5Gvq1pjKYSZVeC21pCuuRCQIIgAV5OAxESCT7ix5WgLBVRnH1Z6hk7a2Z1CcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامپیوتر شخصی
عامل هوش مصنوعی مستقل از Perplexity برای macOS - تعامل با فایل‌ها، برنامه‌ها و اینترنت.
https://www.perplexity.ai/personal-computer
• کار با فایل‌های محلی و برنامه‌های بومی مک
• ادغام با ابزارهای وب از طریق مرورگر Perplexity Comet
• استفاده از بیش از ۴۰۰ اتصال‌دهنده برای هماهنگی ابزارها و فایل‌ها
• در نظر گرفتن زمینه شخصی کاربر
• پردازش داده‌ها در سرورهای Perplexity
• اجرای وظایف به صورت از راه دور با آیفون
• مقایسه فایل‌ها از برنامه‌های مختلف، انتقال یادداشت‌ها
دسترسی از طریق اشتراک Pro یا Max، در Mac App Store موجود نیست — از سایت Perplexity دانلود می‌شود. کلاینت قدیمی به زودی منسوخ خواهد شد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/4725" target="_blank">📅 20:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4724">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btkR8Wd5u4FxwATaSovNfC-2q486yhG3fwSrBO_hPFCEeM4OPBuRn7BrnVDM5MSytxOC0Ti4J8WkEK0XnDN4WD8ySq3O_dlyD8tb6V1RsAJx_4iX4qsRq7f8eSbfY0-GXiiIJYuR6JfYaP-79Lhon9sEwxTeJwfF1ltbSHp-QSMR7xtY7bHBpgsr_fXr-lWyqqIVNPWpKVyRudO7XF7q8vYIqBEJpTadudlcH6CQBiAzwunuHdW9S6evhYZZ9D7r9N79hR2Tuz1gcrp99dDoeXPpjcOasndIhAVllSab5N9UgUltG8oW4EuBNBvlAqnOpLgduSsPSzZn2KHWglQtrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمین گل خیلی دیر پاک کردی پیامتو
😂
چون پاک کردی گذاشتم وگرنه مهم نبود واسم</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4724" target="_blank">📅 18:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4722">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚀
دانلود مستقیم فایل‌های فیلتر شده با سرعت نور (بدون نیاز به VPN!)
---
رفقا سلام!
✋
خسته شدید از اینکه برای یه دانلود ساده از سایت‌های فیلتر شده باید فیلترشکن روشن کنید و سرعتتون نصف بشه؟
امروز یه ابزار پایتونی به‌شدت خفن و خلاقانه براتون پیدا کردیم که دقیقاً برای دور زدن «نت ملی» و فیلترینگ شدید ساخته شده!
🔥
این ابزار چطور کار می‌کنه؟
شما لینک دانلود رو به برنامه می‌دید؛ برنامه به جای اینکه با اینترنت شما دانلود رو شروع کنه، به سرورهای قدرتمند گیت‌هاب دستور می‌ده فایل رو تو خارج از کشور دانلود کنن و بریزن تو اکانت گیت‌هاب شما!
بعدش شما فایل رو مستقیماً از سرورهای گیت‌هاب (که تو ایران فیلتر نیست) با سرعتِ نت داخلی و بدون نیاز به فیلترشکن دانلود می‌کنید!
🤯
🛠
آموزش
راه‌اندازی قدم‌به‌قدم:
1️⃣
ساخت کپی (Fork):
اول وارد لینک پروژه (در پایین پست) بشید و دکمه Fork رو بزنید تا یه کپی ازش تو اکانت گیت‌هاب خودتون ساخته بشه.
2️⃣
گرفتن توکن گیت‌هاب:
تو اکانت گیت‌هابتون برید به مسیر زیر:
Settings ➔ Developer settings ➔ Personal access tokens (classic)
یه توکن جدید بسازید و حتماً تیک دسترسی repo (تیک اول) رو بزنید. توکنی که بهتون می‌ده رو کپی کنید (فقط یک‌بار نشون داده می‌شه).
3️⃣
تنظیمات برنامه:
پروژه‌ای که فورک کردید رو دانلود کنید (یا با git clone یا دانلود فایل زیپ). فایل
main.py
رو با یه ادیتور (مثل نوت‌پد) باز کنید و این ۳ تا خط رو توش پیدا کنید و تغییر بدید:
🔸
REPO_OWNER
= آیدی گیت‌هاب خودتون رو بنویسید.
🔸
GITHUB_TOKEN
= اون توکنی که تو مرحله قبل گرفتید رو اینجا پیست کنید.
🔸
REPO_NAME
= به جای کلمه random، اسم ریپازیتوری خودتون (یعنی
downloader
) رو بنویسید.
فایل رو سیو کنید.
📥
چطور باهاش دانلود کنیم؟
1. اول فایل
req.bat
رو اجرا کنید تا پیش‌نیازها (کتابخونه‌های پایتون) نصب بشن.
2. حالا فایل
run.bat
رو اجرا کنید.
3. لینک دانلودتون رو بهش بدید و اینتر بزنید! برنامه به صورت خودکار فایل رو دانلود می‌کنه، اگه حجمش زیاد باشه پارت‌بندی می‌کنه و در نهایت روی سیستم شما ذخیره می‌کنه.
⚠️
چند تا نکته خیلی مهم:
🔹
ضد فیلترینگ هوشمند: اگر دیدید وسط دانلود سرعت کم شد یا دانلود چند ثانیه متوقف شد، برنامه خراب نیست! این یه ترفند هوشمندانه تو کدهای برنامه‌ست تا سیستم فیلترینگ (DPI) متوجه ترافیک سنگین نشه و سرعتتون رو محدود نکنه.
🔹
یوتیوب: این برنامه لینک مستقیم می‌خواد. برای یوتیوب باید اول لینک رو بدید به ربات‌های تبدیل فایل به لینک (مثل
@file_link_irbot
) و بعد لینک مستقیمش رو بدید به این ابزار.
🔹
امنیت: توکنی که ساختید دسترسی بالایی داره، پس فایل
main.py
رو به هیچ‌کس ندید.
🔗
لینک صفحه اصلی پروژه در گیت‌هاب:
https://github.com/soheilditf5-svg/downloader
📌
#آموزش
#دانلودر
#گیت_هاب
#بدون_فیلتر
#نت_ملی
#پایتون
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/archivetell/4722" target="_blank">📅 16:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4721">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فیلم و سریال بدون سانسور
https://www.sorkhcloud.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/4721" target="_blank">📅 14:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4720">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">g2ray generator v3.html</div>
  <div class="tg-doc-extra">70.2 KB</div>
</div>
<a href="https://t.me/archivetell/4720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚙️
g2ray Setup Generator v3.1
یه ابزار رایگان برای ساخت پروکسی شخصی با GitHub Codespaces
بدون سرور، بدون هزینه، بدون پیکربندی دستی فقط چند کلیک — پروکسی آماده‌ست
✅
─────────────────
چی داره؟
🔑
هر بار UUID کاملاً رندوم می‌سازه
📁
۶ فایل آماده برای آپلود در GitHub
📖
آموزش تصویری قدم به قدم برای مبتدیان
🔋
سیستم Keepalive برای جلوگیری از خاموشی خودکار
🔍
راهنمای تست اتصال قبل از وصل شدن
─────────────────
پروتکل:
VLESS + xHTTP + TLS روی Xray-core
بستر:
GitHub Codespaces رایگان — ماهی ۶۰ ساعت واقعی
─────────────────
⚠️
برای هر اکانت GitHub فقط یه Codespace بسازید</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/archivetell/4720" target="_blank">📅 12:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4719">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ربات یوتیوب به لینک داخلی
@downloaddockbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/4719" target="_blank">📅 11:46 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4718">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رونیو ابزار توسعه دهندگان وب
https://ronio.ir/fa/
اگر توسعه دهنده وب هستید و به ابزار های خاصی برای طراحی نیاز دارید میتوانید از رونیو استفاده کنید که شامل طیف وسعی از ابزار های آنلاین می باشد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/4718" target="_blank">📅 09:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4717">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlqdHQ3MJ6GybXEwUa0U7UOFY-lM-UcXJmos58ykv_lXvxz19cxe-wdJVBRIbNMRpUVoyb7gRh8ej96ZK35bjH3mziRpvC3H8cEy0-vo5leOXRfTwps0sGAMbssR6yQoXcPidDeyoohU3bntfK0xJAiDw4E8mg4egcyvpOHHiivC5Sh7dzK0nyhE-hnkgmwey0BicHlFoW-KPLkeh25gbf3nHJgpJwH-Rmd8ixtju617XXZMcMdOzKj8_RTU2B4V2_E4ptKfjiWQCpkkT2krvL-IdjGTrHmXZXEjqmlxeQ6YbZTecY2mp10mF9v-6_FepLZw_EaGODxbm_QmJg0ujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنظیم NTP سرور داخلی برای تنظیم خودکار ساعت و تاریخ
با تنظیم کردن این دو NTP میتوانید در ویندوز و تمامی دستگاه ها و مودم ها و روتر ها قابلیت بروزرسانی خودکار ساعت را بصورت خودکار انجام دهید همچنین اگر میکروتیک استفاده میکنید هم میتوانید از این دو سرور داخلی استفاده کنید.
194.146.239.1
194.225.150.25
ntp.day.ir
ntp.time.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/4717" target="_blank">📅 09:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4716">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ربات ادیت موزیک
@musiceditor_tgbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/4716" target="_blank">📅 08:59 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4715">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMarwinVPN🌓</strong></div>
<div class="tg-text">چندین سرور رایگان با متد Netlify بدون نیاز به شکن
🌐
لینک ساب زیر رو کپی کنین:
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
توی برنامه های زیر میتونین بزنین، پینگ بگیرین و استفاده کنین. قطع شد به یه سرور دیگه متصل بشین
• V2rayNG
• MahsaNG
• V2Box
• Happ
• Hiddify
• Streisand
....
منبع:
IR_NETLIFY
🧡
اگه خودتون هم با همین متد کانفیگ درست کردین میتونین به کانالشون اهدا کنین تا توی لینک قرار بگیره و ساب مدت بیشتری زنده بمونه
❤️
🛜
@MarwinVPN</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/4715" target="_blank">📅 07:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4714">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اگر کلاس دانشگاه شما در بستر adobe connect برگزار می شود برای دانلود فایل کلاس، آخر آدرس کلاس این متن را اضافه کنید و به جای filename در آن یک اسم انگلیسی دلخواه برای فایل را بنویسید:
output/
filename.zip?download=zip
مثال: اگر آدرس کلاس مجازی شما مانند زیر است:
https://vc4.uni.ir/s14042-23027551-1/?proto=true
آن را به شکل زیر تغییر بدهید:
https://vc4.uni.ir/s14042-23027551-1/output/filename.zip?download=zip
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/4714" target="_blank">📅 02:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4713">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLVzUWfqofmFXKBP5jZdGtMbQvgplP4QpVEKTNOC7gfnIu_N9o10pqDKyNcRCP2VljAnkNdmHIGGSEvjj49fZa8bA2pIwQnFfY2YUtBb5k_FsGX_RYZ9vU0xFCChzqQ02NMf4iWTbv0MHah_ljHLxAnHko0nX6w8ONA-FDSRrmwjFh4VapH-RZa6vEfgjQWtsBScOrrX3kQ4Obj2sQUIRk4GYmM58t4UFCwU08_rP94ngNSHntgfuUHAZWO3RrnLlQplYQTQj-R8ZOyJIWFGmeNGNVB4cTiBLinqJZE0uhDCny-iAJ0vSy3oAt24-zdJxF2skWyuvMUrkHpdZ8Es0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
Canva AI – دستیار همه‌کاره برای محتوای تصویری
✅
بهترین برای: تولید، ویرایش و خودکارسازی پست‌های شبکه‌های اجتماعی، ارائه‌ها و مواد بازاریابی
- نیازی به مهارت حرفه‌ای طراحی نیست
- ایجاد طرح‌های سفارشی با چند کلیک
- بهینه‌سازی هوشمند رنگ، فونت و ترکیب‌بندی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/4713" target="_blank">📅 02:00 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4712">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/archivetell/4712" target="_blank">📅 01:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4711">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ربات دستیار هوش مصنوعی میرا
@mira
🔺
تو شرایطی که اینترنت برای خیلی‌ها محدود شده و اکثر کاربران ایرانی فقط به تلگرام دسترسی دارن، وجود چنین ابزاری واقعا کاربردیه و می‌تونه کمک بزرگی باشه.
🔺
می‌تونید Mira رو به گروه‌ یا کانال‌تون اضافه کنید، ازش سوال بپرسید، باهاش چت کنید یا حتی بخشی از مدیریت کانال‌تون رو بهش بسپارید.
🔺
امکانات نسخه رایگانش هم واقعا قابل توجهه، از جمله:
• پشتیبانی کامل از زبان فارسی
• چت بدون محدودیت
• تبدیل ویس به متن و متن به صدا
• جستجو در وب و پیدا کردن اطلاعات
• تحلیل عکس و لینک و توضیح محتوای اون‌ها
و کلی قابلیت دیگه که رایگان در اختیارتونه.
🔺
در نسخه پولی هم امکانات پیشرفته‌تری مثل:
• ساخت و ادیت عکس
• تولید موسیقی و ویدیو
• کدینگ ، کانکت به گیتهاب و...
• اتصال به جیمیل ، گوگل درایو ، گوگل داک و...
در دسترسه.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/4711" target="_blank">📅 01:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4710">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta_3K-uUfiOg4Z69hZNfHbVUB94g1asQq2qG1wNtHPegpXIDODzWXez1gfDD_RfR0Idi5lOaz1lHBEA6AX6qApYYTuzVSsMyiIFW2ae4-LGWBPKoo-_jg6nx2AuPj011LAsjB3rb3xsAqWitCahdvQvPbwGUcz30I1V1_H4hVTqjEIlGTZnhqNzVuhgyy5WrGXll4jBSncWCk0CsxTQrpPvrr2HQje2jtl5_v4AXjgO8_V_aG7epMI100_UNInVJ_nKrpP5pL_P8VXf0wb6uQT66fb0oqxDeaht96c17OSsernyWMQcU2WAVzKpFBumOBY_wc5enqFDigUt3eALGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IR NETLIFY V10.2 • BACHELOR EDITION
⚡️
تغییرات اصلی نسبت به نسخه‌های قبلی: ۳ تب کامل و حرفه‌ای:
⚡️
Generator — با پشتیبانی از چندین دامنه نتلیفای (داینامیک)
🔄
Replacer — جایگزینی دامنه با قابلیت توزیع خودکار بین چند دامنه
🔧
Tools — ابزارهای پیشرفته (Rename…</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/4710" target="_blank">📅 00:31 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4709">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De-uebltANWTdDLJ1NRBAj3dmVMS2krm7sYYfwJCmy_O4pw_toZUAXDrUowgMz9c7XUm3HyvoTEpMfvjqLyPvGCAvsQeKDQtsJjnX0Wu8fROdh6ZmnShkoADZkbnZN_dCxti6WwS-IkRhYer7Swb2IbKaZmavbW2if69cIa8pAMDoikP1pX-2bQYYmWSY6piEbx5QgPRzcaq_sIG7mwThSA8uStCjzOY77RBHR3qenvQIhztb92rApC4PRuKIzOVTk4mIlC-pshTbdNa44XhMcT9U8ql2qLafQb8UZyA4Gnqza5aB7yun3tw7MtktF0na8heWFb9eP3JJ0DFYp_8pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره
😁
🖤
طراحی سیاه و سفید مینیمال و حرفه‌ای
🌐
دسته‌بندی هوشمند SNI (۹ دسته + دکمه ALL): Helm Ecosystem Core Kubernetes Kubernetes SIGs (.sigs.k8s.io) Service Mesh & Networking Storage GitOps & Delivery Security & PKI Platform & Orchestration
⚡️
دو حالت:…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/4709" target="_blank">📅 00:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4708">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc84xngiu8c9M1yg_EyxcP7nsl7hYZ2U7ytchhrqi0jcumQTNGaY0ssGk5IW6g2RvIRDcF7A8MPbYqi-FeLPIx3GaxY7RR71pForaOuLwrOIIoZkg8EguIDiOYBZAr-nxIVcjevzSZvmrpsfzOXXPK5UjXh2crLHTZkaIHzTmatzk_QlmHIcNgh8eHoukLiyzdQ8e5zizyMaBIrL1Duf0dgzIKKTgkBo-Kg9l00bTcj9c8TQyNg4zsEbIXx_V1NjZd7lafs7cYoer8GpWtJoM0ntBr4LtIxTBuxijxxT1jYDaujvDl0DSOCJL8PjdLae_dX6elHCv5KMG2GlsLj0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نسخه جدید لینک ساب اختصاصی کانال
⚙️
به صورت خودکار با لینک پروژه های اهدایی شما آپدیت میشه
⭕️
با شکن
وصله اگه کانفیگ ها قطع شدن دایرکت بگید
🔺
اضافه کنید به برنامتون یا اینکه بازش کنید کانفیگ ها رو کپی کنید
🔹
برای ساب جدید بهتره که از
هیدیفای
یا V2ray استفاده کنید روی بقیه نرم افزار ها بعید میدونم کار کنه
🔥
ساب جدید
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
🚀
ساب قبلی
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB.txt
🤝
روزی یدونه لینک پروژه (با اعلام نسخه) اهدا کنید دایرکت، کمک کنید این ساب تا ابد وصل بمونه
🤝
❤️
برای اینکه راحت تر پیدا کنم
#اهدایی
بزنید
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/4708" target="_blank">📅 23:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4707">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">@Bitchlorz
دا این جی تو ری چرا استوپ میشه خودکار هر نیم ساعت یکبار
دلیلش یه سیستم محافظتی تو خود گیت‌هاب به اسم
«Idle Timeout» (خاموشی خودکار)
هست.
قضیه اینه که گیت‌هاب برای اینکه اون ۶۰ ساعت تایم رایگان ماهانه‌ت الکی هدر نره، حواسش بهت هست. اگه ببینه نیم ساعت گذشته و تو محیط Codespace هیچ کلیکی نکردی، تایپ نکردی یا اصلاً تب رو بستی، پیش خودش میگه: «خب حتماً کارش تموم شده یا یادش رفته ببنده!» پس برای جلوگیری از مصرف شدن حجمت، سرور رو خودکار متوقف (Stop) می‌کنه.
🛠
چطوری این مشکل رو دور بزنیم؟
🔹
راه اول (ترفند Auto Refresh):
تب مرورگرِ Codespace رو باز بذار و یه افزونه
Auto Refresh
رو مرورگرت نصب کن. تنظیمش کن هر ۱۰ یا ۱۵ دقیقه صفحه رو یه رفرش ریز بکنه. اینطوری گیت‌هاب گول می‌خوره و فکر می‌کنه هنوز پشت سیستمی و داری کار می‌کنی، در نتیجه پروکسی قطع نمی‌شه.
🔹
راه دوم (تغییر تنظیمات گیت‌هاب):
وارد تنظیمات گیت‌هابت بشو و برو به مسیر:
Settings ➔ Codespaces
اونجا یه بخش هست به اسم
Default idle timeout
. می‌تونی عددش رو از ۳۰ دقیقه تغییر بدی و مثلاً بذاری روی ۲۴۰ دقیقه (۴ ساعت).
⚠️
(فقط حواست باشه با این کار، اگه یادت بره سرور رو دستی خاموش کنی، کل تایم رایگان ماهانه‌ت تو دو سه روز دود می‌شه و می‌ره هوا!)</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/archivetell/4707" target="_blank">📅 22:54 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4705">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVX0ITmiNsWhdCCVXsvJ1M9lGEuhj6l62_MwikJ1k-xZXPA8irfTsn-_k3HBSDUW3fzrsuI6ME1-fArq1GevV6dpyjvUqbUWPesE31x3IY_7pE-fGprl1_YM5_rMvO0RAF0u_pAeEP9EPBejwmrmE6aZ0Gi3zF3iKfg2EnXJtbJkuIy4mrUfaLWqnyKjdl2HPigvXebNXTp7Ur183jj5Pyp6iBlbfo4wZsbLD6PjYqN0iSBaYIZOHym_iSOTKDiFw_0LHPVHFr6ZXy7Pn9rgF6ZHQyBjFahG2r2rg5XuGDJQATueoyoYh0NgZUBnblYazwJ1ZwUsxst-OQOr-KfZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83de2fa668.mp4?token=Ks9wjH9X_reFqbOmPSzUjPZ_9hjwJ07RuOmkiGTrguS9kYNgFSPdJB5r5B6oVQdQGjDxq3Dm5IEP-O1wHO7-PfChN_2TqJJwo9oSfE2B9J6niUhbg_yW4IaSynV4CYzC3ORVSpbi38AWoeag57rh_WwFRAoe6GX_NAOX_EK6WvgAkndbbTUYD0FyQi77IrttWyeB5DaY4L81PIms4K8uG_gitSiU07p-mQdn2ySdqPeTJmqgQguoDiCUewCzlVppAUrM1pOX6kQqCA10qNiv2KuQekYAbx_PFtfMmWXH0YEiRgDEnETN9_GAt8UnJrcsI0WXNJ1KIDA5n8REw5BI3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83de2fa668.mp4?token=Ks9wjH9X_reFqbOmPSzUjPZ_9hjwJ07RuOmkiGTrguS9kYNgFSPdJB5r5B6oVQdQGjDxq3Dm5IEP-O1wHO7-PfChN_2TqJJwo9oSfE2B9J6niUhbg_yW4IaSynV4CYzC3ORVSpbi38AWoeag57rh_WwFRAoe6GX_NAOX_EK6WvgAkndbbTUYD0FyQi77IrttWyeB5DaY4L81PIms4K8uG_gitSiU07p-mQdn2ySdqPeTJmqgQguoDiCUewCzlVppAUrM1pOX6kQqCA10qNiv2KuQekYAbx_PFtfMmWXH0YEiRgDEnETN9_GAt8UnJrcsI0WXNJ1KIDA5n8REw5BI3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔆
آموزش 0 تا 100 نتلیفای
💠
netlify.com
🔰
دانلود فایل پروژه
⚠️
نکات مهم متود
⚠️
🔺
با یک فیلترشکن پایدار برید که مشکل اپلود پیدا نکنید
🔺
دقت کنید پس از اپلود باید همه تیک ها سبز بشن و دو فایل باقی بمونه مثل تصویر
❤️
با تشکر از عزیزی که ویدئو ریکورد کرد
❤️
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/4705" target="_blank">📅 22:10 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4702">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آپدیت شد V10  جنریتور https://johncarterjourney-rgb.github.io/netlify-config-generator  گیتهاب https://github.com/johncarterjourney-rgb/netlify-config-generator
🔧
سرور کاملاً دلخواه — UUID تصادفی + مسیر دلخواه + فینگرپرینت (Chrome/Firefox/Safari/Random)
📊
…</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/4702" target="_blank">📅 21:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4701">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚀
رونمایی از IR NETLIFY V9 • BACHELOR EDITION!  ---  رفقا سلام!
✋
بعد از مدت‌ها تلاش و توسعه، نسخه V9 ابزار معروف IR Netlify Config Generator رو با طراحی کاملاً جدید، اختصاصی و با تجربه کاربری Premium براتون آماده کردیم.   این ابزار یه دستیار همه‌چیزتموم و…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/4701" target="_blank">📅 20:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4700">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
ابزار همه‌کاره Meli-Action: دانلود از یوتیوب، تلگرام و وب مستقیم تو گیت‌هاب!
---
رفقا سلام!
✋
با این وضعیت فیلترینگ شدید، امروز یه پروژه اوپن‌سورس و به‌شدت کاربردی به اسم Meli-Action رو براتون آوردیم که حسابی بین کاربرا ترکونده (بیشتر از ۷۹۰ بار فورک شده!).
کارش چیه؟ دقیقاً مثل پروژه‌های قبلی که معرفی کردیم، از سرورهای قدرتمند و بدون فیلتر گیت‌هاب (که تو ایران بازه) به عنوان یه دانلودر واسطه استفاده می‌کنه؛ اما با امکانات خیلی خیلی بیشتر!
✨
ویژگی‌های بی‌نظیر این ابزار:
🔸
دانلود لینک مستقیم: هر فایلی رو دانلود می‌کنه. اگه حجمش بالای ۹۹ مگابایت باشه، خودش هوشمندانه با WinRAR به پارت‌های ۹۵ مگابایتی تقسیمش می‌کنه تا محدودیت گیت‌هاب رو دور بزنه!
🔸
دانلود از یوتیوب: دانلود ویدیوها با کیفیت دلخواه شما.
🔸
دانلود از تلگرام: دریافت مستقیم فایل‌ها از کانال‌های عمومی تلگرام.
🔸
گوگل پلی: دانلود مستقیم فایل نصبی (APK) برنامه‌ها.
🔸
آرشیو صفحات وب: می‌تونه کل یه سایت فیلتر شده رو به صورت فایل آفلاین (MHTML) براتون ذخیره و زیپ کنه.
🛠
آموزش راه‌اندازی (فقط یک‌بار):
1️⃣
وارد لینک ریپازیتوری بشید (پایین پست) و دکمه Fork رو بزنید تا یه کپی تو اکانتتون ساخته بشه.
2️⃣
تو ریپازیتوری خودتون، برید به تب Settings و از منوی سمت چپ مسیر Actions ➔ General رو انتخاب کنید.
3️⃣
تو بخش Actions permissions، گزینه Allow all actions and reusable workflows رو انتخاب و Save کنید.
📥
چطور باهاش دانلود کنیم؟
خیلی ساده‌ست! برید تو تب Actions، از منوی سمت چپ نوع دانلودی که می‌خواید رو انتخاب کنید (مثلاً دانلود از یوتیوب یا فایل مستقیم). بعد سمت راست روی Run workflow کلیک کنید، لینکتون رو بهش بدید و تمام!
گیت‌هاب فایل رو دانلود می‌کنه و تو ریپازیتوری خودتون قرار می‌ده تا با بالاترین سرعت و بدون فیلترشکن دانلودش کنید.
🔗
لینک صفحه اصلی پروژه در گیت‌هاب:
https://github.com/Kurdeus/Meli-Action
📌
#گیت_هاب
#دانلودر
#یوتیوب
#تلگرام
#بدون_فیلتر
#Meli_Action
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/archivetell/4700" target="_blank">📅 17:21 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4699">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)  ---  رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).   این ابزار بهتون اجازه می‌ده از سرورهای ابری و…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/4699" target="_blank">📅 17:10 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4698">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)  ---  رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).   این ابزار بهتون اجازه می‌ده از سرورهای ابری و…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/4698" target="_blank">📅 16:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4697">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرادار وضعیت اینترنت</strong></div>
<div class="tg-text">🔴
هم اکنون اختلال در زیرساخت اینترنت کشور
طبق گزارش‌های کاربران، هم‌اکنون کاهش پهنای باند و اختلال گسترده‌ای در زیرساخت اینترنت کشور رخ داده و برخی سرویس‌دهنده‌ها با قطعی یا از دسترس خارج شدن مواجه شده‌اند.
بر اساس این گزارش‌ها، سرورهای شاتل، مبین‌نت، ایرانسل و رسپینا دچار اختلال شده‌اند و همزمان بسیاری از سرویس‌ها، هاست‌ها و خدمات داخلی نیز با اختلال و کندی شدید مواجه شده‌اند.
همچنین گزارش‌ها حاکی از آن است که برخی VPNها نیز دچار اختلال شدند و یا اتصال آن‌ها به‌طور کامل قطع شده است.
📡
@IRRadar</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/4697" target="_blank">📅 16:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اکثرا وی پی ان فروشای قوی به همراه تانل هاشون یکی دوساعتیه برگشتن روبیکا
😂
🌟</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/4694" target="_blank">📅 16:25 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4692">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">به زودی چنل IR Github از مرزاد
🙈
🗿
🔥</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/4692" target="_blank">📅 16:12 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4691">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🛑
آموزش متوقف کردن (Stop) گیت‌هاب Codespace  ---  رفقا همون‌طور که گفتیم، برای اینکه تایم رایگان ماهیانه‌تون تو گیت‌هاب الکی هدر نره، حتماً بعد از اینکه کارتون با پروکسی تموم شد، سرورش رو خاموش کنید. چطوری؟ خیلی ساده:
🖥
روش اول (سریع‌ترین راه - از داشبورد):…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4691" target="_blank">📅 16:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4690">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAliReza</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Vless.txt</div>
  <div class="tg-doc-extra">121 B</div>
</div>
<a href="https://t.me/archivetell/4690" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مقادیری که داخل فایل txt هست
UUID - ADRESS - xxx.app.github.dev
رو با مقادیری که داخل ترمینال گیت هاب داده بهتون جایگزاری کانفیگ خام بکنید وصل میشید</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/4690" target="_blank">📅 15:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4689">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)  ---  رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).   این ابزار بهتون اجازه می‌ده از سرورهای ابری و…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4689" target="_blank">📅 15:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ArchiveTel
pinned «
🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)  ---  رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).   این ابزار بهتون اجازه می‌ده از سرورهای ابری و…
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/4688" target="_blank">📅 15:50 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7gcjNljrEboL51CyWvdcZuhtXM4XvEOnl-RRsUnxITEGzBwpPcutoJgiD6_oaADNgo8WTmd-sI6EA4SQO1tUpoIqxi-dhcEXTq6O3sJX8KAxauqbcdbKajUTaW3cjrIxcv1Rly88i-KA57MyAuLsiVC8OVPm9U7l-PzJEdyClLPFi9C3x0XIi1oGFzYS_Znr51LNnpSb0h17KOcWNbsaUrHgL6Hn4z4ft33ALwjb_E5GtDd2WEs8pCulfqdBDk-nKTH1u50aOWt4m0Ft8eMFo7nduOnCn4TWyhOIY7hl0uxt1C1x8pOTizgVXZ7M6F91Jbh5KaWwa5E8tb4GDCVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)  ---  رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).   این ابزار بهتون اجازه می‌ده از سرورهای ابری و…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/4687" target="_blank">📅 15:49 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
