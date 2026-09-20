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
<img src="https://cdn1.telesco.pe/file/A8gFWqWXmC59N3RmjNQrrlMRaNNiR-vMXxxqgrNfGAw6qK4J5KAEO73zF7LqcuTWdUuHHvQ0sG78ETiqWSzcfzKOy5GWwo9-CfnVkP52n2Y8A-VEebVw-lIBbXwsUqo8Di_kcOC5f89-uFx4G0Pk8pBe9howwRlMTQsbz67R7YbZ0tq-o7yQjDYCdJ4XjBJsbgvKH-Ds0nwTVwJTIxLVOOAkVwDBZonMLqbVwsh6-c-aHzHqGkGKzNPuaGze0vJg1eeoJblvt6qhpK7QWZAyYmHKuEfdOUs7UmHU3LVpT0SwTsJ5NGg-D0s14Am_SQwL-DFRpB1Sw5oA0OxuKJcp1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.1K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 09:03:26</div>
<hr>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O2Ir2Mu8NNtExxQNmkIhMfV7vDjorDzjS78luKw1Cy-Rsx8GTWt_AWBgb7xtC-mmD3crKNwxKx9jJ9db29LTl2OQPSHba5EUrbZtpSkLdJIR4vgKBXoY7fvw8h-uVuN8kGQkeo8NvYObwro5cLletWGW53uh18R0c5v5CUZtqKNhICAYm95vASjebHDnCPw2Lb22_qzIFNaRzraaKDDr15SGRFPtLmxJqzagmfayl-Dg_XhKwhaQnstAeuoTl206JAo6-U2zwUJ2hXRdklHSQMWHpLJFk5JTRHcpbph6HiY_f0GUj7EgvivAPz84dU_Y9xXyrQ00Nwu4P1p-_iMjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O1EbytI86GynekXJ-C71y6SoSAIPN4ZgzlWN0Y2ukGVfK-HqR0BXOelhqTw00aM6SA7Mdw2rmgacopQnVIkc227n1tSSTtITBDVNv9T-1RQZMJwlKxMG3ZPG4mRtLQCzZTXfYVAWpfnuyqH1w7vNbsmKgdYbaymW7FYJg4xcKFf8cG735v0M6Y4oJw-w3wFR700XTH_aqqXLt6PjxMu0jyMKs24E6GDrsdWjE1nLc1ERbuzvnAvZrZlk_9I58v9odc-LESxqn5IMV8zcYTEp-H-sMUHMffSslms4XLdUw70fiWfIVWl_wH0NRCEwg09PpMH445990lMBcF31_8yn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZhvEBRfvIWD08Xd7hiDRjI1DHdD-vt3TsvDYxNPr8KNclx2x1PJ_yI0xrHLImOx8JnhHv4qdxnYJKKlDR10wJ9Dl3ZdCwijqJ7iIdqVRMlt3GPHU-l1clKKbAx0kS_p5iODjumF4Jah7rmhXDEA6BrfX5DPYK0N54-VOMl5BMQ7qo6U6HovgMtKRe5i0QAOiS5D33y--Uz08Cuakgqy7qy9sb5s8ybZZMEuQXXqMFadf4v85RrYNmQgAlsmknEp4EeN7NtvwzPV-X_g3gShMswkcpP2JSnTYtvB1Zz8AM86hNCvrn1bigZBTE0wgcjk6pPpnR9wcAeBQujy-4S4A9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-o7c1fpIc6Hm2vjuirDDFUwJyui3GAqebgZC8ijq7orIt1QhyKfDKjyTNOuKBXsY5LcWO-LGaQevIWmrVoTw_rgKBMz0034cCn4czLYyo772Z3DYHUq1ncb7K5un-DhKlDFOfO0stZEDEbzFRgRwwb2yzUfQbrGUNFQMkpu0WWiijzjiQ4X1mvzzTOisGj8okofaixTq7x90lTxPpe56_RKfCUjzCynkBcLANS_CCKuBCtGervOHhQD4SDCs5PnRtaRZj_t-lqcnIG0Ew6aA7_7ml1OKE7I-vkVmkFO2Zt_vr8t2Z3eJu9FxvjCGXUaw4CigzOJR46KpFpmKpuwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V7jWcXSXCEV2_BRz5ub9m9xuhvKPsK0yRwU3sq2SClXybrKyIsSDthHMUUCcXuLmcRrxgvKq4P6KJXvlY9zVu28vtNeGiqbuEfVTR3Deq0Z3vvmrjsl8yUvwJeF28UcOYEyNDH5v994aS3QrIgoPTmBWHYJSJmTQvkhTDx1gb73dzvi5JhE41v644eNXRFcTMjFeR5duZ3cBQDV4Vh4oXqabS99MYx7Rk4WvbaXOsrm_TdeUjnE4Gsa4vUpdARh4A4rjM-Rmv51oWWMIgpKeYchbVQpgqEzaYar00ZyPCH9j3javBdjH7n885KywDsB69Wa3naY8LuPBWyg81_1EoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LfkeouyQPBQ4OTYaSTuX9fSqOfWsoDQvqWQKFIzRpIk5QKG-3amaoqcC1aNrkWo2fOb7-_X7wG3XWD1ZhInmtBh0zgtsGjcRwx-8sHU-n7qAv7MHS5EHhHE9S6vc1n5WCQV2mwtvNkHKeSxgEUj7ChGqnRT2rE_Uy-t3EPOyEW2nfG8Xq-_fvHO1BLSgBkhndLFlSq1RtLlG1CTyoqm9Ds9Ku2bJbAPNBLJAW-_RQ1Og5xUGL70SDWexl38pqFAaSvq8vFLYvjRmud2KnaexcByy-464F8YOPafUM3zG_vs9ZDlnfW5qlqrzERZc7ZX3clT2o-_fTx5CaKsStzY4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BtrFHvY3pOvk-x9Z5VYplH-AQtOZFKjDHoMRAUnbd_CqcqA1KunnxKwIgGJ_XtGnUNJAUC956hA5BTUHRNv077afdjUQs1R6S36eFzc8Nvg3EsrWpa-yVuO7twkvWjkSCcvpdbdxd8ssgWRX10-jpk0xkYRMbRPJIuOkXGRSFcS0UPWCIeMeBFKu0eWWtvdTzsQV2lYceHNthMZcLx2q1tp7cg8Ebpx34-mse271waXQhTNocR3mo7LP47xhEDSUGN--bRAZzjCVtNUfQBMkuEUV04wqEFe_CYef2YJS4FawPPtJRgcVsK1MQysrxa7Lyxfsl0spUusqiwbEn-GMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jLC0aTMV_oIyWBdUiAiKChv7hkEzQ9ViY3S-fnsqaCTb4KZIurfWHfjuTdsMGQs9ieTf6OwvUm6sBTx7CTqPbSIfMei1KgWfaAJ8zU9a-vn0pfTxKHoPzQCTM3JkB_-VuIKUCeveHC44marTNbrixxZWPXnZht9H4-84HmesfoXR72QyojUUS1wECSuUZ5tupFUfAR84wxjlapJX7SWjWwjg_oXHzEZ1T84oBpaVjx7ZSNytoohY_fdhbTE3xXJfeNqb3-FZv8BjN6251P5G86wgcKAcwj8s41UijjBIV2fp8ir14ViBgyWlUPxm2jyx-k4LIZEryesRt6F3POpu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sY8t7JReoG-jEA0AAwLuiuw34k21l2P35QKZj1HZH1zICUhItdUuPl3rDYXhkl_74efFPxMf9zwYgXHcwPHyHxGBZFp62-ndk17Z0YEiW6P_GYiZS70kvjAOl9ez5MTRbLwUPuacRcdkPTX_L8SBPyNpunOY4SFBAhCU2eIxANdm8BLZhgllHL5JSFUNAergdIsOnWYRQDR4I1J9S_e0ucYXIsDF6fRzsFWMCOFO9lhohzR4nnJTdQfublkmzneoAMvSUZrExpcqJqnnUrxhAKOci-FThHeQ2fefWqMnmfZqbAnfl9AFGwAJnBb3uGsjlTjHICB53MmqoCHkbVc1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frnEvIe4_H0aWEQcRQwW5eQ621t05y9h6J1ZuJRvmJm8AGsBk0OtrXcPgW7XRnchRxKGpmVaei3JUNzUJ-p2TpwSnGB59PNkZxv7PqswNzxXU5bpDOfW1DySGeQTBRQF6AAKUlXiaV-5sZrWDehWo29h2153Dw-J85-L44hhGseIcLJX5MWZmSIfiarCnPyukJJ6t9BFkWnmwinEEfuNqpADf1_ZgQMIWl-F_Nvhp91nUKpNa5VMh6a1zIqqoQjDAweMmf_pQn3H1FVfdE01rm1veeHTEVzlhUS3iyCibgAvCezlTpWZzMly4uwIOvBylab3n4I2XTQU5qohmKNgyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IsO8WN60yHCrllYEVsrizc_ndscTsSWJ_BhbVQvIUMLalUko8p0AHvXoEe95dneETiJ2lzaVjCnWzJsT4ffWQZ-UXcziTi8rIw48zb6r4Ub039FnHbhQdvhln_BbIAoGgNR3aEpbVQRhLPRxryNVUO1xCmkckLJkOcBYaGy1p1jeHrz6SADxC6kwxbvl7c-MzaPWZ74QFOillwZmo3IbfPAJIBmDyWjw872xLcl0ggzODOMogWdh_tzZWHrsG6CzAFt-XOu3oPJsaDLMm7RtJ9F3gMZ3tQDXBh86vCmoNIJwf6ip-kT88FZ7jDphi-U7YRbZ_aIml7zC49QSLwXs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WzzSyqNt1P4SqzVOD8Ay8lYrQFnKLbDKrdaka2Ismvomi4W4Iwo0DBI57dIXIpWHSh-H6Skcx3xxY-D2Wnavg4DLhUoj9vkD33QvMBtPsZdtrDZovSvCz07SIdj1nIU5nRaSRee3gTASjaFRRxgYS1ECRnYZtN1j8HKD7aj4-SzNfAWxf5yQcwvsfDTDUgwhLkVQkiMeRTQT7-NXWhrka6OYGC9adAOHM2gHidBOBqDhP9klSuNKxhvztbJsSI7kp_2SlYRcov4b67JAcjZhfRF3jcymMdWHlGdSTvP8niMhvHqdL8LXc2GOGmA2hUtQ0qkiaWZMSZr1-fBQdn2ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f22mRTWrpEJHiViQ5xRic7zCl98T2RHzaJ0Ox15H8XL-ZLj5ohz9dmDkI11wSgh5ORIpfZw4_6NLBN9I1FJ0Y2kj9IpCj0txeeho5Dw21z_YtN7PHRN-ccgvTXxTqaJgXIVqXaNBNBmAwU5tbFPiSjWgzvfoR883CyEFVoxNKzu9Qb58UMagNf04zZgDTHpkOIlqFocvGmByk4J9S-_4V7Tyx2Y2xgDLk8iXXmNKmb549rdKCnt29OTvxyeFTDePMq96avHkp3m7IcyuBCpHjphHw48SxnskOiRfkjjc9u_fLV1MJUYFmFQCYK3tbtb2F5VAyfUYErceBcAXuwDCwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GEDnicsXfn-HGd4G7ZIPnGI4UL4Ppy6RkV3vGaucAoBFzQCZON2Q3DqShv7diUBkvucHTfWTLSBOHPojd0La-GNmN2FRLU8UsQEgyxzIy_NJzWXdZAAMoBj7kCPjIQyWjzz0F3ZT8Jijbicco6WEjF6W1J385i9uTMVJeCMyXck6QRmCmZCDzE9Jtub-hKKHi6t-O9gJ0wy_R-cWrLDGPFAdw2apwaZtKDWez3j4lt_k7f33DtFVho-UcKJEJ1lrZzYOUIp4uWylQ8AW5jY98sfDZdzIcd6WB-WgXY4CtuyXCbLd_WOcKwAYGMNV9vXf2LgAz4g3WH8OoDBjafXTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rhSiiCSs1FpdGbJnXzzYU3RQXxKN-6BsnlTvZDgsxEkYxSQBwoZogkCvFZFONnSLPozx0xfBZjpuLpPgvRpPUOi_5jwtSR9InqflgfJ2DC7l7JYrMhs_tClJuMIuwuUdMheXXtIv-L1-8fsq2_KgKUdJ4LqGOCxrzv_L8cY2C6eSOrrE4yHAjYfhIy4HI3thDgIR0Xd7VncwpgQhHMFCFIy_1dN6vPTBDFegrZxlzVkjZ912FUZVQHKmflHciOqw-evC_H5wg17k01zhG86tvnceDLIR8dMFpiE-APHRcPa1QtyUGnNp6M9J47BlDTxlut-e4WBDkXHaov7CxO8YoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vI41muAMIUt_cW9zcM9RI8pMqntvZp05gteeR1rWNSOuGwDuAaC_zRVwLgVkRD9dCnrQmMjgqqeEGNJWxqUjUeSz8HH2ZoVdX9zfb70bbWM6NpLjGT63aOP9i4MqwMNVIks_myeaPm_8Ta9THdDf0ecgYxx0w2SEEPdhGDgGypaUNslgKJkdFdGvitSPeOpeqjK3AzycmuN4VO6eb1J8JXmdayWeez9FxaKSe_UfVhfT7nXFQy4gNzjaKjo4tPsbAukM7c36Xg4p4BL9XMoRO1_kjiLbnbjhFI6XAzTAafgKO2y6wxEJOxYPMYb4NsvA2XOZgeoLgOl0jqwVJdQYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RWS3wEmzamZOVGAYDwMKK0NQoFTdSXLrSPjwodkTfvLj5yr6tpc3TvCodnnufXRZ96KsMXU4ZrBPZH-EVpKHaFe9_8q8Y40CAF-hY3XtWFVS-F16fbXeT4951NOcOapiBU3BWBXmmg8SZZFUHgPzcvPjrOOwmchdxoliIO0i4JHX8VHOXH1nlb5EsTPAz--yzSwfSCX4OqGG3qX_HAC_-9mwk0od3-_Qq-EAmgefpGtzNdC1aEE2eIPX2IcD9rw7G3nAQszzg4Z415OQJjQ0yT4Yf_c9Bmdcv8jOuXb5X7OmJNrxXbw5mbUdGJU1z3i4kVoFTmo2hkGanvQRJNTKWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UpiEp2l_U6rW0BqUQybWjyKN9XjgZxRpUGDV5-feJJklQCuK8CXGX5iqjY34-r6H4vq4bHqHLVFA7M4Ek3AUWIHZsc9KHHjXiNXLhUGu50OWoWcUphUWSUTPaY-MBsE5HdFbBiMX8Fh7IbkPyBh9VF8CGUdhiCHN4U25uDW8bTxxQzVDS0A-9qT7EQyHYc1y2cLu7-0C-7Taf4oIyi5mM_kuC94HPo8Ecn2VUCrX3i4pgpMkTrm-uisO4m_MNaICYUN83af9vsfj1GRQI1KpIdCdd3l1DYAMUSfB8f9vIAqTVevGr629WgMSVrtRIdHjzgIZ7AAiWnjWifurwWYlrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ARoqD8hTAjnjN5kmzbJU4UDwOT8dfCs4lAFxGsCHBIP2Ms9QndUe8Rdz_9qkiOgF2tLQGTdb7IGMb8-AChJ0WMv821FNOWwq8k3in-vmFvgC3PmThqvIJysQ5Li1IQ43TaZzvANSwozq5CMD57xzaz-HSJtNZTgi9k7rQNRsrLotR6GWUisKdPfCaCYNOXj4GrJcrmxtProyztYXCkLAIlBOoXLQ01y9H2c1RJEplAnYQyCt5Zfjv3c93OGVaKaYbllvjUik3AkaNpzKgILYrqtNMAhrXD8u7KlexRnZzGXdSaX58r0fMyjnEnmS65zSx3rT3mGSBeykOX41lYdIng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g0_WXLXdN-KC11NR0LYu4WTWvl50RathaCu7AjvGYF_FZa0V-g_adAo-Toq1y0uJKU7b00JLVyqoygc1IVU0d1sg8IWtAVxm7fNcwg1bQFaMgFVRyB1UqvreWviNPZI_f1D1A8m1rFqipewnt1mBjkzgY5SjOdvQ0_PVXD7pSouF1YZaPoFXD2GmCoZMKt53wwMFR9sHdfwHJRl1NN2npuNHFO3HaljVFb-dfD15RHEQmXvd-IXRVeIODthw1Z1bL5icLeRL3QkfbhmU0n5VggViL_vv55_cNhRJ_-YkgWhUQoYH7XcV5BIpmHI00c-4QOYuBXvold94ShzWOS4FQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RdwB-5F8CZf7EJnMnVO9AcdevfeJFSIdaGXtaTusyoaJb3iETKLfYk-3ZTt7xom2HFtAMHci0jBDAHIgla_1DP94q1uN2EpKGnxUEHV1j-R13gp9luMEm3NnkmfdwT319LcN9pciQDjiIr7W0xQPkemnJbNq4WeJ0T-pxdO9txnGU9cPaIaHsxtdAmZp2nDnAmZiFm3fK8zeEfdESNVmAkVOEeLgWfWjHve6yGtKwfZpSvREChoUCacHdEaWbT1WxWuUgCC-L3j_AegQA4sUwH5YcDFIdVEm27_qNSTXoP0M2FaOk_RcNWn5eahJC30LTHZAKJ12bypLPJSEYIXXpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WeABmXBEEdYAqs9Tob4GBHfJAjgKS2J8HfPhQDgcyeNtoU489mAPcJeCjiD8JJajcn3tc2zLxO9HWli1972UxODiAw5jGWO0ChlZ8dAZepHqlMv56mNrJR5Og1i3_ikuD-FQlWeO6tOzIUZ49kXUt7mPPNP_PQ5TCdsxFbCLjmltIoSGSEMtMjxz1XBM9-5LCdimX8rxpq2xCJA7yxWSwB2Gbp7mZtGcx8oL6zeGASxFr8_75R9sFZ96Q-PdedSOomXbWWXh7JIkYjzY4uLh_StkWUaqxMM5IF_KtckurEv6tRoadFLJjYJQhgytnSs_HEL5DpQahJUxfFHBXY5-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/urtuW0R5Fd98EzOq0teTtsaURlYe-J1Fs48fmPfr_7subjWG-JOOJ-TAXxIYznPd22qEbUtkdp9PeNtotBsoM1f8M0O8Ho-Zawi4eo2l_1n4rwGfo4uj67zmv1z7NOyM4GIfQb-DH9VQ1ywu4_dvWnpykIJ363Y9KW38riAGpaKr_iJILhnSsue_EoKvdE7FRXAbu-64iXHX164jsdPmw-c2SqwJ4cftyYhJSahtD2rlXDb1na_gs2xYIXQIt1Qj82KEvLF-EV6Qcidv3CnCQqyp1j7Fq805Xh0UYs7W4Ej71e_rL3kAoBP3KAbDqVgBzY3lHgj9JVNUrAsdHMCjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XPSQna97IXcpfurM-NIACgLUVfeJgsIXXDDybXQYKzplxoK6Oao36njFwKB89RlcMm_RIqJiSbmGmzaRQ1IWkxZzJ3VuN5Ja8VrCEIK3-jkvPXVFRWOdvpADIil5NpNlUQ1zDBq0DSlc9E4WcrksA7n3RFsS3zANU69Gzab7yiwE-POFQdfxicDf9SXT4uUciQgPuh3NswiJMygwOsGD9ghv_p1Nrs7cjY91GzOXQesFxZNvK3BGbZuhYlM9oCT3XRtPp-4GfjbJUHRUeQqMgjbPQ69cHV7aK8Qt9nkTkDzAAfqXaUbf9qCTLnrk6Ogm2s_79FtkOV6CJihvKRQnNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UvpBeGvASnkbC_1Qf4J9GxaNcaPyQM41Mc2tCaZFTgiujUpI6mEheeAt9U0_ECglzoig__R0DFioL3GszHGYoeGzK4MP5kpIqk46cQsFsUKO9DJm5ME2H5n7qyU484R7ZLFmdyGc5tBWIkfL7vv-xG4TH_GsnfeJbZG4gDFk3dmfVWX9Reye9Mo_8SFOq2kKDsvE4olwboHeOLpAg8DcTEXixfkO2ZBruKH5BKB_DrrmaKlBXWdVL4lElY7lbsiRYrGRFKdgO3tfq_vzb-O5U-rhHjhKXcSwoy9KB2t_voZonDHCHDfVIbXkWaDMRZ7Z83rYRGYsnKK81qVC-_DmlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BP1kiLeGPy0MdsHP2362dPnTOU3NW0HuCzaedcV4xzGPtuWkn9aUv4y1Xc-icaFn3xHoeb7i-6Hz87S6SES6WOjZeeYTc1q1G44fEqRTZWmZy_QDG4lFQyRj50o0jGDBCxZnt6rNinbF8t-rp5F02Q_nF849xHWdLcrLbG5QIh5ZzfhZ154gBg62ERW3xFmRChk5Z_EJBFZoi2Y1kzVt71_TjZz3Wah1R-CFGp461v9EuuroEdUNIjLOlt5ImKEFKTfPFo_l4c98P1NtZ7y-eoUQScj8MZ0j1X6D9pZttqJkb-_emH0uBQaNIr0s0Kwi-9jVD5j6KgsdSEViFEeB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M7pn5r-vs7vg7_TrQUYmh73t-D4ynQyFp44P7w4e2MKIxiEOfFde1ltF7dy27ryTjyPkh2M1gl59du4WJumKRmUQtYiojDIp386EUI1uzfxFKQQXQzNKU9zWHGOwIFuVBuc3yNptfznQ_u0jhzxeiPIETPEx5oi2w289PI2LgiPTjTAC4oUySTN6yfRV2tUNcKu1_x2ttUwxGx337T0x1t071lVmDJshU9Uxbco-KJXAnHhTDuP7867uKsH29GoYIn4Nvd8bvJR2wFL8OA07ILFrFVXeN1XS03dd3rcSg5cnbVfuiPk2OJvVicbWW6xRTJAe0Py1xgKNMw6gzAjW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kfkaOpmxHFclP7rFqtH01r2WVDbW7SKJ8i1XtAUlkAJVew95OhYT2vs40I_X7eqF5NkkY5EpznXjpqRsqssBJRR7k9e4nlMvkDlAs-v1x8L1ocsg9DeAVqVnmXnVbNEkqJm5WDdElq_gE1FBsTWhRODEM60CFKkwjefyqFHWmpL__SRAuZwiD9KAoIWrFV7CEBfH0R3xEWVP39_981dGxWYXri4JDikN0W4kI9upZ7lelF-BsQETgy18hVuXeTl3fHgnl8AG7qxp_TdZnsXT9mMX83LMYJv56ThrgEqwV9daUMrqn4FxywsrB-xOfHbN9R4CJ7Ii7qZUAcNjp6TnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ak5AIxE-G2a2FIudmpM1FKn-AE-7hN10NCFnpc7o9RbdtmsCPOfqhq2nLAmiy_NdnfdKTTn9GE5sMFPIaHrTz2ElzUKijhcSVJDv1hrLH33yHSYPtSVmXLuM7XQLh1qMbu8jqr1w6iplU5TT-8xvLOG1UAuFdG_5DU3v4ox5u9Vv3kszyWpYAMsWQWsWQ7QQW1CSjSntuN3WiSggTJBzoCUPSuJgpB0Dp3EOCebybcxHho7gQdMWhdbBVDApjgvRbrEvcIsQnDYePrclhatmKstcmKUJP38LHgYx65UPaKNqKF_1N5k5saLFs4B7JxHOpGximVmmQoYeerEdU9-ZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Klzq7OcHRxXX0n5sgfXoPIezPfnTMFT4pT5_Z_4hF_bobvbmaLcpdhyoJsO8JFx8uO9oJFEhyeDDGTlJq_jvmUr9MoLpqO6Y1mOjYuLbEYPiTTFH3in9j9vW35yCvhva0CVk-VYYkOnAwJoCFl_iwkt2hqRFpNCxJ331dBYoPX3tkLx0TCO_O4jvBGI6bncD963Y3G5b3Km5_9e83SQiiRWlve0i74F3oUQEg9E7EnbNeTI1ioC5rj-U2MAactAe96H2i_2wOryWMAQ4mPOgAiY0bklVpeXR4FXRBbpQOtB5uyA_Iw8Ia0t3Zg6KTrg-QnjXPMzGOOhbtaZIjMJLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t7ov648w9wv8r9PTP2xO2_DFyZD0qqabZy5paBymCbiXIheVvpQQZX7h2OwQv9xVIDaBD9b17Ewd_PUYcnLuq2pn7sXo5PNNunt-dyN0L1BUVGa239UvOTSvZit0YEgmDM9nlrodxnO9CYAl9CGTBCuomEceKOJYU_nv0c4OnLU65ttXdihGKjFAn0ZtGn3ZODCX5zDNPqNGsTrt2R1zWFvIZDLYzbttcB2g6CuvfaXZjCwfeX9tYnOqFFr4PUS_SldGU7VsAatKjYjdHFHEBPXeBlFg_uO_ZXrzKp9_6ci2XtVWhfSq389dmyXA1KiSV6VQs9405aILPBDs3O1MCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dbug45BKMJ1fB4YY1Zbq55AbQxvIMUZHrZhCwVcliRA_svfOI7CYuxhwJFbcnekyxnPFrM30Zky8b3ns9DNDJ1Uha9GQqEQWdtu-21QvUHgePMh0aiFhUl2zRSpVNnIftJPISLFfqX4S85oxV_ObnvmWkpob85b7ZD6HQI7klUGuy5pjXk9BquQqNYYp7Sv3N6vYZptS2Ls0En1LIbQt0tvFvnyPjFj-0oqvcvHB8rTsBSf7Y8QOeu5jpQytxUWhGXXOZVcF4xjVqqPuXrpIyoMVvyNQkAFYC1GNHJ8YbwcY_GZIth_Zi-aA4DjfDQwYdM-zIutfd9XuLOoMb6P2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eta9s3gWw0ZMsQHrNIdNq4GzSopvX6CWH8V9ixrPzkINsCAd8Q7sgNn6ZK5uS-Dv6HrAKXvjCWppUVuLceY18O6Nh0pPKsSmWQa4cD4ZYlIwv4iEH4D63WAPMOCZAWSO8QSK-KtVnBop3K4vbqPDAkvADEvDKbjE9C-VI593Ncg3cUSJV79xJAd5Yo863ktNZ3EXRAcBjloRONpIITcEaHNhPIVQ2H04AYxxEVS94691Z8TKHDUHdIMxOl7mNBxu0UJWXJQIWIuGRgZlkX_D35L7YbuWkJbdlc40pl2DIGmAmm1m6As4BEezMjC9ur_oeNFMf_0bVnIyg8gG5fPZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sixrng-4xhbQhNI2Fjqn70qUq_Mh-i4_w1gIQOxfBoC5mwLq6kKihs9bX7RI_CG5KhxIbKdBgE1PcMzsKzBH_yuTSQ6JA3f9sXiS1Onam1bcWPRrrh-U4Hf1i1cA_ez8Puz4-t0d4KGexIighmrbVFHZUN-iafXDym9OeU-5PO6Ab9ukCV0C0i1k-cv2zwNoGDfFGBjS1o1S2fvDHBKBrVec0dNsubUZufx8WmSnXPykQ9Zzu0dgVOcC36TYzve49PGboXhuf01hTOcIxdTT-gQfrOoEhw6iOfpAxQbAHxgQagR73LCF3bbUafsFqN2rqSnBrHdkIDvF2J8BFeTq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fw2qYntReMC48Ul-XAyx7CNKvnxWm8XnpZNoEekvWPaMQnqC0j1rA4gI7HNRhrxbUwuyHno1NftyOg24db6p0WPMumH94Tpefpcjrb5-ooBhE7k1hH6WjgVbHZNMOqDGjGxOV4a3XsTaBJJBwsMdAltEncWzBB0X9haShXNxXeSz0jhobS01qTwQxcfWrMYwKhpPEt5TGB3kzac0_aeAiLikqaZvbtSVOURPpUWmVB53Qn332yHPgIykllRsP7U_s4buvPTEmo0U7Yv3CSniIfcx6fnvex_RfbXpAXMVGA9evDe3vG3KZFhNH0T6Ny6a8MuW1rKdN3nK2HabSNwUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aqeiXe0Xevq8ProoMnxcxjbFBgbzAYEDSH0fssggs1eGmMWCEzDiYWwpy8UNt4mO9Kz3we9Dwi-IfiYtMnobIkdmBf1IED2qBqjNUtQ3W73Cbi2VkdP3gu9AkDsvuGa0niIW58cc_ecoSxWNOOgsUnlHeftRvi0E0A3gaXOp6snIzlTwUKl05R4C-wflqL8viwzBvWK6dWopwoiO15dPcfMqvBgMX9qwrN2131vlVdWZSsNzt6PbLt52kwDZy00IVApMPUnt1uXOMgfoSREbLPmEhytGLCjF7FzfS9wdzDT1KQW-MZQ6v7h30k4pLKbxsAEDjLlXEmXvEWpqgNJb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CieEbe5QZ5cEU2g01Zr40McxA76VlG53lGvjBQBl5YkSgorzpzV4WJvPzMO-cEFRbEMBlNOOUEzDB0JKepPAKSgK6oe_kqNBIUNTY3bJ0v6Lg3wGgmPZt4P2F80ALVL-LoFTL-5qlfes94rJDaZfjWMrzG2eOt12arSOZBD6aq8UgrM4PDjGlMTDqZtHs3jIVMxPuUd14DLyQyeuP5h3LcI4VhKBDnt748ZF6xKC2rMFz0w4-mukdqx28uZJFwGKVD4pSF-2S69Xldtj-7OfJZW1jheKMYkGCIM8wk2JhiSdDNpWVddbYW5YlwCDYBqHpZwhloscpJgv-JYQmJPppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rRAu-_yvbkKg5R_gQ-xAVZQbQROd3Ah_7kyvlNGs2DikzeEMdMW_0n47SS4TInXiJkxJ3hVwNH7VLf6ubenW1R9g34ST9HTJl5wc3MrKi71AxOqqlNORReNAlvvI6_sjZ-3kSF37DHkIsu2LcUeo6xPWrjHGc92qFoKaTbwSz-MTi9Q3HahDPU_uuYTmyDYwZQdkMbOCESlXrCeEzOigJ9xNSAE9vIME90JD2nSYFZ-Z3fIgiYjO6yufmYP-WIWPgGn4Lf1Pl7r9mQfpq2opRd_oGPQcGOE89ic-FsMSfhewTq4u6g_ugBwQDXSYrorU6wvbPxpCVIM1SzBHrntJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LU2vtd9HH3jPkGzFoTb6LG-0mAOAsqGrbL3VScxZ2BcxmmEFqnt5fNgIw3IAALV41VwNW-0rgOqTgS0umDvOzWCm832GApSlHWL3Z76ZzgrO-pGtf2mKu8_jkN8_ppGNzu-UOCOko_lhKdP6_OVrOM-DR_nV4mbD88XrHLpqLS8FmVRsyXvzDlS9-xsDpLVRO7jJnb2L5chZBq60V7Cuhm1AmvXMgZfUHkLCydARlffRdvV7PrxTW6MpynO1KG5KSmZMhfOoOSUzKAH-B7mONlEkLSknpQiecZGPVCssOhUr3MeLPnqC9kn6aPwjQDDMz6bj8f_C5m5ZF3RB12B8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eX27rqVE8qrsfC4v1NlwW3X4AevVAB0fHrUwLkG7Y6_gAnOG0SQKEYMuC5W5CW8Yyl0HNPTxVsYB-NoZReF4nZDKaNd2jePz63GH1eh8gGruVocsSU-SAU4S9RLQxE5BDBGlF0Bq7zZJTkaorRd9qP2KFhWeD26YS9YWkZS6Oigp2FHOdTvsUNJ_m646Meqt7N-9fQdrQh0ypZDzA5vNroSrnRAxQecgKSEwgXfGCPkvkx5O5_LxVdx4QPdj8bL8ENTMz9dSavOIzHhgvFUdpTxWkJmzj7FA-RJKsocZb4ZwHr0IFJ25CGeIglI1GRaXPQ2ZMFWqIApNSdvMAy8aWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FO8PfNPO0BsMqaU_gJvH-YwMLG1Rf64dNZ-NvUGxOQBubRKSR2KegAuZlhZRHo3rVh7vUKEXIjEUlzAxQIxhelC88o7dtxmeelGQxvNQgQmX297O2EBhymGEH-24l1hiwjU-Q2C-8lct9n_joMOxlqOWNAxb8FU7GvzscESmFtfzdRw-UN35FNmNH1LivVQehPC_3RkUnM5rpZfOjUcJ6-11NNmJaBO0yhheDI0h1sWThKbLLJQhD9fNKUtoFWYls5gSiMMn3Zav7yvQG13C8KG7AmU8wH9dTKHTzLBDzKCyh0SWT9T2m71bLU4N8J6RLR6tMbVK_EGHJabvgU0tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kD345H6AWszCSG8gzd684qsrMPAAk7S_jLC9JfNf5i8GOoK9E9ryPN2ln5VFFipK6DkV3o3wh7zHz3bHNOpzpO3bHqjkZoGEf2lZR0Tm4r0GmhrwpyQ9JGsyOOneTlE8pJ4X3vmEl__ywoixe5peG6HPvPVI6a2mNQVlBuBPw5GE8tOOF40EA1-CCCfAy6Oay8Cdz8KXOwSPpmNyCXAbnleaeHb6H8SQks67zVvbiSQCcEFvMF_fFEvf8VcXqUGqgjVmk8WaIAejVO9M3wM_dGvdayHX-yYS6XgNaPDWwmt-IceeCifv0LAasq8bOhmAGI_wb4ag8ITBVSFm6ANWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/awYJ4z8bWOzn53UykF44WuUFsvfNsu_IlMJbLjxQPMp1p0tPy2YuX11mullvLj29YNTkvI3soYeNO8ISQe5bG62kLTwAuVzWxuqBPfHbD2dP0BPRZS9TgLqOS2TdTS91oYfW2n6YrTafzJhD86637LPuVjYEgd9Jxz8olOZnwmfVWA4XuL6vhwyLXpIdbY-FJWWYk-m-1hOdjqSv0qbeBKv46Jzz-NvqX86UT3txXo2xOnL6bKgHynIewKtaUEawM-BBpMfvHNjFqn7dz5FbIqURUPAOde2ni8L64DI7a-e1dP2hL1DUUwkX5qWY31t0pT_gRW9lC-IW1iIEAVJRLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DD59hn7ZJ20z3AHENtHjYnnmEVnu1kuHA91Cjmyu0VxKE48SulYaOMsPJA0g2vT4MmQSQJEDxwlQou6tRrUs74Lq4pta6Vnaow7vI46odlk3XY9nsaFTSlGWcFJsujfoR0_02jq7x8F6v7O9u77hmCuVpfW9RCCdhXEOP6mCjmHvGZDu0eThMl9CTYWptzIpzvMBbNgpBJaWMrULDM3IeSNjZH4AAl1CWjMgHKV4hxjZ4EfxcNMViYa7U5q-F1EEdivhqezbPVxzQt0MTq0qWNdcP0fvqgtfz9BNR__1bd8mthiInYatLBV5oPbq9BWdhyL8pb62L-t7J8RHZI0bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UjhHLI-zM96dhlm0ROzHcBzilg2JCNcMGRFQwYF0v5vzRiREIP31WlOL9uup3_7iGoKtDJ-cufyqQ6qezT4PqxnRBsMWtoMIBLTO9dlFmAQudseSI9AFUxY8goInx6FWD_QoKK97ff81knptaXvQBH9iv6RugCZVt52L2KklgyvuOXgspXutW0nF0jUCfxmMuSis9yq2O5GfeNMstYxlww1LeD0BfWkCZ0oFT5bvEFVB1DbU5KAJNJS7WDfJcSF4z5QGFf6kF-84tNaEC2CRboHXSY7lN8ocxeWcsujbe09wNRz4POTGCgqEYTxWpEwn1gj086cm1sZca-mD3--U7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P6poEASWWQnJE1xdSxC1UrETn-Odb5jVgxIz3SjhiApBoAc34gyoo88FOyW-6y60pLnIuZaU0BdSTb5B2bO0orRNOCc9UM3coC6yFkXgtFGuJiCSvGBVMtvbnBa_oJud89TY4l6mbQE7b-0yf982HHx_s3lMbiBtrA02AwK-usne3Fpvc6k07xhPA14ygaaSqvOYhPu5MRSSLhMU9FwYptNOUasSPwcOXJ0OMxd8wmEBC5QjEz2BfSPPewpUkWv5W7waup2uGgwNoG7mJBccqT7ZsLphE1L_fGG9onWK91bBfsRuCi6hd1l0VAh5-nwPQ0X3p98QjeVe89CARP9cvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=aRXeFNeGpfW3DH_MWLLjJN_yqkIEeYIsPVL5xj5_eI5D8ae6PehqZgc6kX7JSdxWD9QRgjG9QovmOTc0iy7r6AneTK6VdSYzf5e9NQz7nR5rDi8zr8Km7brlKjCgI4IwVUZRok53nRy6QXW7uexif-x_Ss_DXLupKATi855zaRCFmrbzmBn3YLdQAiTjOsVo1m3KfpdCdnhAQPqBj7mcKBl1NpFhg5-7E1dSJPzt6X1Il-kHVUoNYIMHOzzTtg10q-ZyXuQT9I8q6tsoJ3cxKA64VQz8eRs0hyOloQcgly1_wqZSOo-lNU9HIG7AJRJ3R2kTGW_Hijs5sUo5HSCHYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=aRXeFNeGpfW3DH_MWLLjJN_yqkIEeYIsPVL5xj5_eI5D8ae6PehqZgc6kX7JSdxWD9QRgjG9QovmOTc0iy7r6AneTK6VdSYzf5e9NQz7nR5rDi8zr8Km7brlKjCgI4IwVUZRok53nRy6QXW7uexif-x_Ss_DXLupKATi855zaRCFmrbzmBn3YLdQAiTjOsVo1m3KfpdCdnhAQPqBj7mcKBl1NpFhg5-7E1dSJPzt6X1Il-kHVUoNYIMHOzzTtg10q-ZyXuQT9I8q6tsoJ3cxKA64VQz8eRs0hyOloQcgly1_wqZSOo-lNU9HIG7AJRJ3R2kTGW_Hijs5sUo5HSCHYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PoBwTmIuOBmoDi_q1Lki52itPp6WTxKgREigqDOArwmoOBIQTEjkehCzR9DShhSIWmRCTaV9tz2A6lbrqM9rMe_LTU-eybaFE8F2ZlJeRC4vhusliTxg-BbT3F4LI3cf-q3-CmMcdqTIIkTK7DGHIOSR9H6HwJII3fo8bjCwggP2ftqvP1HUEGE3xDchtnCvJoh2SN92ZjDoXD7DLCleNvHKBHEZtTe2GhFJFaYmHwtlrrhENO1EUoVu88PqktBqO_4oPqy5Kkrv5LmZ3F3DfFFsMTYwQLGXELrwXtvESn8QdYpfA_nm5O_Js8k8xEZwa_DZ5lAEoRkY3iiypBHz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WzJBJciObcghiaNXZSIAQMmMU266C8TF9scgi9CemZvQ9gnGAkFUx0GlVrLu1GZZFBHJ60m2RSewsTPb9w5aU8rfBxlowCvhMExwNBVsILp3IvK6aS528PJELZMBBr9WNdF0dv6tNhEo6wbhz3L4heZmsEuu38B6CtpQNXuOm20zNA6Qcj1cyH5jSfylS_Y8XuNdx_7FY2pDQw8OJg_t_gXe59Idxst8lZe8IHuTrqhMG00vfgq4izY91DPk6Uw0J6I6GgXFZK7XJwhINBbV7jHypfdlMnrptNf_UbWu7ztZgHu2OhjhesRqDkZK_Z5pJ7d5YT6tNaIH-Y-bOAtz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FsS2MV21qRY0iEosO_g7_pOEjyc4hpx0DCWWdgyIS4IQBqRE54_8K5KOlqw2oTV8h7Wta8LikIWIYYp8gexMDI894uOs7QvBPrtRpTqURgLWtIrz2jqADwiAiyZK6AuIpCClM7-fnz0ag3vHIRn5EtnsCd1BxQXaJsYIJQAE0j9CwQvLIR0p6wGeI4yaL7_PBlsG7_zrA36eHgFF9RBDrcNZZs4Gc8rR4r4ElPMYjBr3-Gcihmyizr3CK-Sd2Cqcb3lBj9OOrit8vYn1tElZB-4Ds3fpswcydwiX7IOaGYZnMi1uuqR4162Rh6ixElkUgkIOZDq_4fyWP5uK8Lx7Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cLQllJWOFHs4i81yt2NcH_ApvxgYmmPff_J_KevU1sv3OcVSQ5plMKD05zgSdQVkNspBKqJMQ2WcByJcf9x77P141F46isInwjvlMphO9FhKSMxLaKTsAZPcrC8E45eLoIsWJVQlq11TAkjO8uFJpJUkUKsNEFQsfEhcD6359BvWPghjn0-7AFgItNwKUXy-U8Jp_Mx4u1djCYl7Nqt-0nP7Uz4_NaOLjYG5MKJ246L5cOSkDhSaia-78-7EsmWPgQlJdcYnwulqYWoKdnwn2bXEbZ4MLuf0RzZrZCFMPtCPOr6DejwLL_Pze57FM1Z10gCmxeUisNBIfWykN6lgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/acPcrmFuGekhgOlNTOlSssS-4j2De5fNelYhqOdaLtOB-zRopD181S88NvTTjHS6OiNEbP4wLf0RSxi2SlHRVIN7HPsLNcqqkGHr3xTovkNTdjkCBZu3lFKYCYFQwkt3NNKA6GNLElxsisQjsZqazRjlkYKIkU_MDAkz-YJxMl_lr8bNQbT2tYlxnJ5b05CIsKcWFjnIjeFOMW59W8nkklCZZ-FbrolTR2tTD4TIAFLqCfBisnvjCJsf8Dh0uP-N3Jwe84nIv0H4XgI4PQQRbkjBfE7sJ1GXUS-b28wBadm4CD-Hti4d9b4SsKKaF0_4qPhhT0N2iMGP-vdnkLHTHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UH5O3yzkhxr0aItZWp-gKQfbCfhIDiUPnwYe_alxq6ahmX1uDE1K_1ZpyvJz03K-xHDvnK1jwOU6DMGMSZ1suBdfk1jsSOLa8NBOClBvVt9sqaHzKdtptVdCtugxTXn7LSPuoG_fc6pAMyyHK0mKZjx5LeEs2BKVZ5oQNKIIepAfd6f-oZJcNl254CqEsjNGo6z6sRLcxQKU5KyrtlWIMobHIT7at9l29awmLNbV8xlCYX6WMcXL-CxpLl9JghGh7E7KbKlrJslurAv_-bE-Hwgxf2Gmbd5syMiO97UqkmKYkyTk2tNyO2_oEk4cZeOF-L4t4XZBJEhCmoNC84qE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CUE987eqeXn07kwd0cLUw8BIpg1AOKpSyHpbUkH8ALTn3lso_TvohaNt1813iUS1xRbDHRkDMckWQrhzzmhqijQbX62UliyZeHtt7L5xYeGI9wb7IDYwaQ7_Lhos-tBaqIs_8scq8WIC57nb0maW-eAXC9vAk6s1RQ2fWGHHNh6vwIHZlA1v-EmfM4RECrixw1sJWpiWpFHCazCBJ4tGaJNViGR98xYqIt2lRu1MBlA_2ZpPPDIo7y2iHjYRIDEmmUIQ0TgU9tVGlASgrFmY48o3ddVFtbc9e_s5Hhv6SxsZVcjSCRhEgNl_ec2SM1RUH19mdfXiNM6vBqGhHOjs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c3DbHVTEHNyYbuNNAqpY3aSmAtgwmS_dLMEUfaOnvwUpDsUF1KHZbptbpkrSlV1bRiBe0Wqjgp8n-wAKDd5lUQQ67I_t92dg7E8SIhUF4cWY0RH_8mc0t7TCnukkaOzmk0CWCPqGZtmYmfpA2tYTKo_osrfB8MDSoYROOKDSfB-8oxHGbnAoovpENhc_WREjAeHdYNOD5o1aTCze-ijB_j2yG3RO0DCyiEnwlZAwIX_b2VfvGgYYes0MkTqsr6LYIUz1AJECjno4WvLNDXLqeGJwr-BZyvOLdSJUN3LxJ_1uTHOqjzjY2ENPtkM070Grf--HM3caidDgYfwCwJyiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N1NmokaJTU3QHgM7sKpMJey0hbix1vk9G_cboc1FYBB2Dv68KMFi1lL5cxMgCxKJaWXXeRjMoTtsA6qkKoexQi8hRgylahAJsqkLiDDAFh0jDGfQKUu6Hm7uy3qp89RuxJsEl57djPvWN7CM3KTX6krZ4PE4GKXJFvzEpYOBRcLfTe19DDJvmqLfU9Yp70TQwwkyOOofTqIDYpuJmB5sFSVyO7Lzgedtta4PdblqFxHnY922NFzCnT3s1TzeOnJBeIZFn6oyY55USVYmejfwKmscUlBqUmOZojxRO2euJsBRcx7Msg9IdvZINZ9AEGU8v8OQDdk4OKb3TJAwXjftdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qjWNBrk5JOVL-c8_puCfwEOZ9jn_9ITu9IuskZRJBfFgXNjFbeohBiBRJeCIcT4xPtazxmURDtu3cP5adIf2GB2WOL70ujFIkju6w-CRYF0Y9vfatzyYKO-c1i7OQUmaUYDNa6Y6_T1OOd0LU5E-QrFeZHugKONpm_Er2VLvUIqs-8x-vMMHd6lT6K1jr9E9Ygtgd7iLLTx75U52dGNsGowAKoCyEFv5Yn1AiCB1lvdA5wqtCvTVkzSJBePHJJZGQLnKziSsPKBTdQatdEIqGpJynLKruYClsYiIkv76pJzcc_B8cMc42j4obtOXl7FThtF4rD4IRe2U1B2Zacr8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rh04CdrRGuFiHkHWDOx4kYmQaxF5WP7yYXAbJedS1AlQaBIQ0qio4yuiEtG21Bmq_80sM3YHbecplpS3aqkQ2AWo6NP5x6fZESMeiWntEks3wLxxmkbmG4xITN-sQmqDV_yEqV2eJI2rkTSxoGU3MxdlDSbUOhJz1PdgrnUJX_BOz7vUv2vTlSMUcUeALYuLZF1RIXeH0eob1zhyoXKENeetMFhyMkcmPXA9usAnzI0YvUWi11AFXQxjg5QYCEtHs7Rw2fsIcKmt0KjxsaL7IuQ4eugY4RwDLV5CYAlO1uoecnkddRoWcejCcTRvuMGJ3PTWrr798WNIrMX1Blg_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bpba3ia6UILhJf4rM5EGI890KXZya-Wk0C4Ni6Dq7-WZDDFu_EcebAMWmOKKcMlfvpLqbNhTu1kBz39smch_8i29JzRtE0gpQzhZ2Z4zck09TDcBgEmC5xaFTIaNeIJqdHDIXzMuMsAJ2e6AUvgfhyHzqE5Yrbs1jGYtRyPbsACkA2OSbekOrga807aDLQMdnA-Y3ULaV8dx0qcJaeAjdn0ctbKBIRUayFQx6tGC9h1MuzQ8VWHy3lSdeCjNgagSb8ZWESK68QcNmpTZG422aK6a9Ah1XD1FFBmlHZq95Lt7p2jtxZ3b46x_RjSZGqols7OpZ3egORXGpyRMigks1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tjKBnJbisD3Ryc3D7-apdUJziUd_W5LRV8F7Z_rYxPf7RgAxKIKO2A_QUUTt_Kf3IxHc0ouhOzUWu15Ov-Mb11dRBeSdZCvz5lqgH3XO5ryE59G0V2nkiFwfczk793vUfTDnceT7bszqnpLcxBf_ErZgmfA4iG20gkzA8XIPfUqQzFT6yeArNeHpdneOeu67gRScBLn7F4_Oi6ZsMZF9mQIANM2nq3wZEJpje01BXCJwHl2W6WWE9ngc6ouNlpmhqRiV6jwGOD5wtYasonLl7e4kPnmDrmVEP3oPCKMEU7Uv0Gw9NKKikROvB8CdSFs8SZai6ubykKdyzUV7dYVIgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PsZK472WXHTWLH_PtEJReXCeSKL4Ve5egl2l_tnp4moLykNV4-Q-zPHwktm9ImOcRxCMxy-zPOlk_SzkiwcStOUx0OK1u_eDEu-q49yk-HFN7WwdPt3BdEvca4hIA15zeC3itGfk5nGbppgtYilqcUdCtqUO3DuCyOt3-vFxQu89Z7uoGIidhym_MbqPYnVsjAvppepCTZ5Xd2aCfoHI8jYDI8LB6JG8H8tQxOxAf05GJodhEMsD_EMtFWb_4XGeREBmy77_SxXsfToeMOhMkEHvAcDo31lgCMGW5T3YBCpR3XDVN_BUM7n_qsiQTmpU2T_x8VMqcL85rb0YvGTJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vBmpqlfJ4VGZYiVOTAINH8NNjMExOLhHXcRQmjJJcE9h5GSHDhd2P0a4C14OQ1KpKkYXlR3_M4R8i9zL_heJAG8tyoxRQ_Vou3RTMRvMvhSdEZpP2tvcG1Trsgh9AdVWSXtkm1N841CPWM8ZdYZsUVqk_odjKod7wWNuHf6ywqxbHE21DufBTvnzPiL-3s4cx-MU8UJhouk5HfJ5gFI6MaUik4soi0Vd3qtj1WwhmrU14B-AGozOrYZzA3CPaXsHJaeF8CtktUuH27mqg4nL_NOTqKJw7Glst_b_5g_mfE1tuF_G9C7NOUadpVs0uPT9a1Eqjd2geHxM4gg4J6uvcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oR3AW-j72UArWilt6RPNOsoSLNP_LT04OTaKysBs8OFf0ol1lMCq513yziCUBQkVYFwddece44BqpRUUdyli7Iz8efUKHnp67S5f5xs3_isemo5kGMSIE24ruaQogmv8ZA764O1-UEWcB3Woe9WcgdS8WDaybgRJTZ384ptH8wmuuZ6jTcwlE2gH5axlhY5EVyCVRhQioT6i4uubtuDPYJBf1oj7uisKCGklas3tehki_P_BsrN2Mxa6C9Bo-klFuW7s9KBQRMNhuj8YQa8rqARjYM737T4g93MdRGslpXfavnPXeRwcPY8gEGQLTgjm7tZuSE5AgQicKZhzBYgrFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pGabrSTHJGZz2r0aezgRMQY4iWjuhJ0QM0XiITJ--rlHeP5-qHEEIum19ltxrshXAWpi1MP-wUTaE5v6aduUbQmW_3GUZuF9GVvLGLDk6C00Mme8_LLxugh6YYNpSlZ0L2y3KutHU7sqtj7yz2_xCMgLSn3pkcmKk0h2aIL4J1wAIiwlM-C0maCdPwlIef1x5VD9AYu16iV6VYgLy7OGEQ6p-ORovVyvIY1XbndTgtQheIOLqTmCrQouypIxiMhPuQIbroeqcAwpsiWm67pAMYkUWa9cPcLrupjwBf7Aykp0xYcnsRZKV4QDhotHeidgBfm-yWp-Eu1eInSiz-1i3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOnaoCmRl90qQWrmUhLUNJReuUwti2Sv7GLou5ZEMkJM5YJBoHLGuBY43YYP5zYSUxZ78a6lExdRFDIKQQTYW6T52e1mSspVAqCTbf9cZk34t7eqEckeQ7wN76hOoGbwYKvM2CAdgJSuSqaycz62F360Es7gPXo582iCDkLob3mTypSqV29zgfDU4pcEnfDCGGG9CyKapjL6WByqZ0oI4RNEsc9PQmdpcmP07UC5vftneKUuIW7_CgzrbDxd11t1vDw7oqpbzJky2N-EnyfWAwyrYhKvlIDEiRoNSJo9nWZSjbPlzePcga3GKaq28KIgcn1YfvmP1VDSbSuMuQ44HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b6U2nCqDcEsjLYRpz963Q979BPMP90MwVvYTVO8lFhJ8oO-CP6ICV9695hd23CzDGAYlgLmZ-AvTjsFOzRhutLbKUiaHcnIvuhF7iN_PSonYtoKq18L-y4FSjmdoAGh86uaInnG9PZjXzPr8bZ7FKRJOLs4gzueJsDo6-xJBhg1wArZaONHVyIzyB8CoSaB2vZhZhFsc-Mz6auYfmmsA5UVtlC7XH0Iud3BPXsytqHimNmibL8V-DEISHRQiVuw8cjGCG73Bn4ERRYvL4KKllO7y64Xx6W-zrXYiWsUxGYra6gYT0CrubysWpI0xQmu_ted8arrEESi1gtyDL5FqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bz-fMv0rsOdOhI3cIoN2TNl_Jj8XDY8at4m096Mn5d3f3qkhVxw4lVZeLrwVbWz2FeIBDAIdinFvKTFcvdaL_Ol35-TkgZ4TVX8rpkU4HZCVFOdYCtV8jFduYpdMbzwtgUArz5pWgakJlHR-bB71Y2jPIRTC2uICZvzZSpfkTb7kF1aiRRc9XeI60_3YyzybJ2P_wYK6-JWKGkFHxngODmrFy0nR9lUj4ZR9bsnahcknOUZkgrXby-7MmKMNZ_3l2QaMBn2sGNKPw2Dn_cS1mqdU6NrnMJXmrypNjVmL_1AVf4VDBtuqyonOhyGgvRObjWTzcqQTVyWeQ-z3VItKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/srbKHD4X2naRIhHMTuuvkx9w45ZLRXuOXDSxR7WKQws2MDuQJVY8ZS96ITR-DJSSSXa-xnxzSP4FIFRgIE92aDV9kNm1DIjufKx2IiNb7R9djYsasxKq_0A8qhwnUWr-tlSWAb6blWvtA0Do8S6q77kOpLe9UU_mThmmOuNujHhq04u4BX7dODIIrjjGcthKoUhyYA-cr1BlmfOAGj_xrZ7ptDyj96hK93RDnafLYTYUWRca_wE-hM9DVtW05CB7XlchZuYkP5TSPm51mXF1H_pQA4RNXac8J4ZFbuEeE4ong3OjKuhjTcC8c0pie9MeVrrXOW4WxDjsIX0a2gKWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dz-ED99-L1fwXMyU9tsYxaFOsH-xL3O6Ew9Dy6C_f8By3vQYkOJQWn_a0k0m7NjJj84AVitJpqsLEsL1_AhkCwVQq3jf0gKtDUFhvWoPJxVpQqNrOnI9GvZ_sBNakdg8rS0ZxKI4JdMnanZH7P1bPRDFge1ML6osLVui7FVOTjpbB4yLRBM_jRVLJtd4n8GQw_ylFkndxxVMp79iyFCO8fwovi_AgdbxMD5ZyqY4TNm9ecvZhRedoXU6cQnu_SwlMfGLtV0RMHUa1zj7X3ScqDlXqz5wU7o1KHwe5heg9JeXPMWbzZTjx_G2fBvkWco4VZ2otNA1iU2_eAacY8DgZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ocFMO1v4t2SzZJDZ8_Vat2GIwKTR81YrlKLvCsdfodE4FO1Eq83DjMbviaRkNVwGfMjcLa6LwEEq84ABYHQddqfpjx3N40eyCM4LVy7-l5kHY41tc5E9H202J7P1nnmTYakfBZLo7JXEIJw8MjG-wBJcC4rareAKx6PDveNo9W0sEtxKE8nCK8k-23Gy--zuaNf46qh7VHq2X2QKMidQdM4t7v0eYpYX7EtJWmak3BE46kcRX-NO8Jr7csw7cWZvUvQwXb3ewYci953s7y4pQnk7i8skdOmEwXMkA9bFXIgGjNlrClD17oTAuOZnib4uCozTvvPVrxImxyHMrmpQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j7_q3wxemvMQUZUPKK8RySjCjIMDqJ5_wnO3roGROu50p8v423YPQmGYWDQNuwvFmZTVKojIij3djXpgdGS1hTHAFPl5q_jlNlnaqP1gsiW0hncygSwkc5ekwqhX4Z1_9RCOJ7dyBLNpWs8QdPAkC9UMCwwiGz-xKCloM8KzliFzh-64C0TvT9iDjoiII-AuudQ3fHOSHGBUUCASIHwNzhYVuCzJJHX4onYb1EyiOFDTXRq4LDTLeoi3qdCGsGuqWFwzLh4SNBgAr_tN0wVmwVk9bq1QLZThp99uGEeDqv-9NTl3QQ6nzYBbRt6CI-57tHq4zKfznKSagW13yxe3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j6NunfVs1uzVwB9ZRHVZCN9wkrkez8ERGWnw6fIh_xdKWW4GKio2fR_LEqBlt9ERs6_5iry7N2HAAI8NgoxD_L8IYQJ0YPYIcHEkDdHWDNCJmrKloU6vV0o66LKtBwwdK8Yp8bOG-xQhn5A3Ihx2DZf1Re6FU4N3PEYYkJqnX3bFlPNg12-kH7Qz0we3_6xl8EXZnAFOicbpNadZYqJm6LaQ78hBGYcXF1V2UjezOGwMD3p2Zk0ScJjaavN5Kur60uotfpza0-Sf554ncEO_TgVLsB2Jy_WS8OXcDu04yA3OesWPR3dVxvI0nszi3xLrw46_tp8GG705f8DTH73PHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KM378qhb6yvWtwk8TT62C5MlYpQxxTxkEI__suFRZwv8OfATBXEwHZ7GYkoRKylwRrqesx7RDXBUbl8wFa6_yK8Pr2cjtLYJOEUGWPQgqSWz8WxhaT2bDygAdkejpHu8rxB1fH3s7vIOcD5Unqm8Zj9MeYstJv_Y7q3Y5bDLxQ0WdaGx6hF-6TkdIEZJSwk49sg8-pz4BVWxdfTk2y8jv5_rkw3vJJ950qZpeU6Zc_reSe1hb3Rb6hPSSv5-9QPEK9O3sjKoMD00FgZu7Fa-57h4dRLy1lbC0AFwwn34gLolbccWSWrt5nqpDz-LwyJCmTL_3Rb6BvXWBsR43A5BBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K5sb5Yw96vccsdO2EoeFWGgYPCuOfyZeVos9VzkFuzgma9W_Bqaw8tV3zj2LBnydIVLa1lg2Wqhape6WfNGxwDAt6jmQSUxW90dINWZoHYT3MwPzfOCM7rQ1HN_5Sn7swLNP65Ac0IgQ3p2BTKIp_kvyP_yOAFY0SH2O4ARCIXiB4y7nGzneKmD1vAeK7gaM4YnYOnaq--BuZYehM9MXWrcADwksxJaNTolkiN9cgGU0QiwU8Ys88dyh2WZx-a1-3f-HL6C-AfZAAXw8QDGMOh9yuy0XfEKTtXU60DdeYB5pKd4BqZ9tyk27Aq4aqB-uc9k-5C7iz1J4GfrPrErhJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lgQ26j9qpuGfp9xRkLCPhHAqAcyRVPR_aWR6XDymtBInMYquPpxu0SgZNZzMIVNk_A2-sTm6soZzsBl9fSe0UpkUNCk5rfsgwP9w7UvH5Ip8rH1aOz_ej-oFAK0yuwYWmDUH9yjEmS3hAThUdMxEzmi2Kw8wzfaVvFqF86k6-Q4-DYdnyzcLftzaA45v7aNU5SJ90m4WdxeHKmpblTsm7jFo0QhOIu9l5BaSJmc9nB1DDGzbfSM1Xy66knSB8CyNZPz5BObhPSkyM9xjwuQOuPqrHzUdVRLkhCgi4i6oV3vQ1ZIgcb7jpL87wkdXLkAiZ8e4GDZkK3nMTnK5zzzuzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j1N4an-7pj1NpmAUK57uWFfU4FjmUt0ByEhmrDEs84MD6pSgSpA0UDg7BUggokAL0dOi7WIz70ZVGXsMNsvmc8Ty2JzSh91Knkhzvj7I4p6aqt_vOwEIFPWuy9JtXyDQwdCQ3nBV8HrKmNZ_lq6KNAcUZhv73TWAS7Omu8j-hzOC--W1m1lm4AzwlM8_wzPIZrJVoMzyJWx3VDNouOpFgWBv-U2HMZA84yvtzAFGgbAtxP-iIW0xbIndnQBU86nerSuujn8tpMYbo8yv0GjRKga1RzdllmYvw0rN-1l53AhyFWSoTyTQoetz3VNU6Hn32SE72pBjQGAZZEUkcn7H1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VeVsIzban719X5seJcwXh6F_sHBfcWJvukAAJ0G3OhQcqLGuXcVO50zeUCQQOgpBcf8hSq3GryfKDETU23mAyc1BdjxL7LBs-bC2FbINII9LjpuGFgxZmaqAkDCJ3Wf-iujTVDmdlcZn58ESmC6mUBcnt2VvuhP3CJndpH-CftctduXK2iKgqSL7ekxOpftVABHycy5N2QDqZX2ENWXr-a_67s4wlRZeqG3mHgcDhWRvyx9RQgp7JCri_ky-xpuxkoib69YayG8ReMLylMw2hNoA9q8HfddCtjAeHWSOU2mIG3XJ38VB9xllwWZkAQtcOVerA_MYcevpWriZYjT9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MnJ4mPkcLeYHWaz8TsEnUzPzze37epzYZhRldN64DJ5tzhlbhpccibNW4mxzkzH7SE8ZO8GJuEgLjJCNmbjJJjYf5M1wnPJoDmKt03WmD-STWhzkBp8NWsVyh8061uOBVyd2Sxt3iEVOa3EMJkkEssSFFcPdR2NuyN_ZuJT29SOunZle49rmFsKfWFHxWWeVCu_gdKQynvhx8Y0CToH5dg__UN4PZ41VGsPQxKPlsvenUG8yilnAueLBOF-dLks1p2Xetb5bHOKa4lO8ZI57dNKG-aoOTkKYynytDQ2c4gX4_m_yN1KYiLofPo62edYxDXhyVpYtWRgCttjEmm4sFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qFeRdfBDmvG7rPEU7g-WkAOtuqy0JBKCX60DXgSnKUJ_5Eg7sIPV8qwNU1FE_3d1My10nZjt9E3nUpKajKRBYmHHHtl7ZZbtQqn42zXHe_du7H4WnuOxkAqYGg4-8Ot25-2mdrDlBxs_EJFNF3DO_RRCxXXYOeps3He47snvnVizOMRzzQx2YtvcQc-jFMvPn8vNiS4opvXRuSZqnAETNXRsatZgVCzCuAZBV_boEhv8S4o4R4VWEDLEXcmtwr31h4m8Eg1ipMx987ubxDa6-o6XNS2DEyfraKUaPmTAn6u7Jd1FSUJoj889XTnZBN1QIzLHgg1L7D0x2tNaHOB0SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bHxA6WMoFIJA9lolI7zlbbn0V922re30IKRRuj0giwrZokMn_SxgH_I4kW5IFYI15YQmK21v0Je7ME4gcUaJ9bFQAO6TaFno-BKLLp9QtEQA8e9Ppma1fUgWZOuyXCLqSLyhzVAHNfPtw1f39rx2NzDHeRIFdLbH5WE3pWZStgUvqbvFUyjdcgHk70NOkyNEvTf_Jw9qgq8bVMbc4z1OUm1J3lMG0vqtpbCFFqBGC9oU-9ck19RV5K0rRMdi_66RoZGD7ww0ebUjUzN4W4plA-9ry46PMIhZKu0I18T1TBZQhsFlUE3YpkmjzsDSxxaVN_Dyo6uGlDWJZKQ-99aVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
