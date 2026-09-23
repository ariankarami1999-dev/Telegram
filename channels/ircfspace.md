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
<img src="https://cdn1.telesco.pe/file/PSvS9DZSl620QqK4dGR-RX_7nxf32ydhw62-5AfxJGuhA3RIps3lfjX8YcsMLmSPODpu1_gPp5QGfI3tEaIAmczzOLYpN2xtArB6MlK0phqLHrp3-uFc5sf1XnNm2yU0Ny6xG5TnHu17Q6qDnSL468o4Jn4uQgf82VArF-imNDHIglOglZpw9ZihGtT1Qf-5CfSfo5DmEy8MKQDcyyueqGTS15-d4KTwDiF2fQq_wXwXPyKARu5U0yPjgCAHy7zy3zx0xsTIDXpLPKyN_Jrx1NdERDEM9h3FrsenL-ZDAgnV0S58CxY2hosbsyaDL5jAKRDiDzgbD3QHoRvZTvNEtg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 22:38:16</div>
<hr>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BA4O7COr3i1eSdKQ-4UHxWPZjaZAz8DH-iBe4kpDWuxkI4I8gHrLGPHQuuQgQSWGlC5cvCo2n1MKYdK4A46O_q_cWB0vLVtI9R73VcTb7Pc4mPY39XcPbQQJmLCtXffs3PTx1ORiWbnGKznMYIwgpH7-J9EujsgEy-yIkhVv6CCM0o_0mITwsQr7mMKMpmMxkRS1DHPDcZV3AP4aYxyg0C0uX6w9wEtBaA_RfGHLhes75-rTQJek2WgBubDTqxfu5GRZzDavkYkSJqsTjIH-r2DOiqVfcSpiQt3t9vVeWMrPnjIW1Xvsze_IXj40y3tJeINj7JrReACPcT6b3mtfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aOXksqODbY5n-RkoqvYlEibj14O2tvzWpAL_5cG_b7QWh2KxpxDlOE8IXSoPQsiwEVtB6V6bKCSB28GXypQNOOyESNFL49LWHfwakFCRrYyn0N1AD85RyTNn1K0nXTpu95vyltO1NRCrLnz0a9-D6Mi6Kg17pI3KR2hrBEa3oqJL-30A-Qm0WpfSrBblIXfFKFOkY__kAAglB-wMvg66Hlqp3XFtOSVrhW3dokUS5xHwHWQdheHxEkLRlfvJyMp_RTSxr2PO8h_VCC9y7pC2BgkDPJhRKRHN0Kz6JBaIRJgwwnWQcG-Zi05oQ1ibhwS3O4Cpd6IViS9j3GVmmMS0Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zu2h8gAdtHJMs3BIxRS4PcBT2ImFm0d-xsVpQ5Klz0w_MGxJBv3E3I077hCXRC1qsEIcZn6cenee28S9bQ9Oaex2PT8YtPIX0yyZHpDXfc6z5pMGngL-HZT0wEvEYqMib_M5C_L0GfeVBfpD8bzIzzRdCYXgu0dLprRB2cbMUHKuLQABGaOut_2DXIPtHzO3FUXnCn9KsgrWO4hwOMYZTLWYHIyeXAdgBl3MLHGAxRVL-y63de3r-zEpPVuXFmkZGhFO8O6ReMQp1L4iD3yPfysJ64HE1XtqBLlGDrCNMWTvMI8q7yrlf0_tVdg7uQrBVOt5TfEYhvfIhamGvkHufw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HgiDccRvHtHx_IW2RT_yLnspa0905TkWFp_gtkI_mz--MBbgjPAmX_gGpaTsW7mZycrdl1tWAmbbAdFPkF29o6tI-rDxznIzjSOk3HPEQ8r10fmngoMqNN-bp_imYcAOAHS0Q5kzyAfSy1zBNWCQOq8-Y60jb8648TMZ9qlGX7NGMK3HJbfWi__wRRs5nABvVetpIXarNw-FvjD80XSzNzNPsVro6tYwiE4dSKrOUnD1RFWGLWAjuXxt_TinBaWZmX_QnXmVtBrE5f0R53g7J9luSIX9FJPKgzgYLjoEKM-hG-nad2_hY1s1H_IQ6p4sMmtzhQnaEmhNlNM7gyxJ6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ob2hss8h0A2ljjypXu29BbX6k8XfgI6cB57jjg4-vBBS-bA_OlatqhDMLThgRqG89HHNzIRRRO1zG6DbEU8clK9Rgm_Cn85gi_savgmGvWbk0DzbPc82kpfBNiTHAWDNImKnlmE-IiJnei2--KOvA2fgtGyB30gj-tzN5lk4uePR2l2M920mYtJABUzr8-r52pLmlO5WOMOx_IVIkaC3_ZA-m-zqk9SA4psvZziGt3L_IMOOSK1aKjMRZYRFuz-G9l7qH7tz_I91W1hfGP_0hNRF86cFRLftLoLPuCdqVGYhUHhykAX8E-1KgUQUvov0JHmzxT9KJZMkWEUJX_iplA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fZAS3wdASHFHSMVbyORWcXiug4_JvT5GHeH4vwZH2-Psw0r90pHEQQIvpv94g5neVbuqXIRNpudiN8k3BxIhGszt3qeP0g5WW5eKoVRQj146aboBMmZK9ta22Ye_NNLwh5AHMH6Bb4J5OrjXcrqM0E57ZgWDH5N21BRG3HWJaEIEqjfkCXH8LI6NHyO3Mjt4KkXkFifqNwXKtGOSWkeBoIIYieSm0DSsmGsx1OnbP3fAGwKN5pU-KxpClsDrXIVbZ0INoED4dB0u9PGIqS1h_sUI_cxb13emy-9PIY0XKjt9nH7f7xnoLGV07v2jZYK_zIdYWBwkkfU4f_eE09TB-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCaXheaLmXqGYy1CSTepcDUeHb1GD2el_ku3zc6EEBbRq4cF1LhzfhsX2rKwcsesV5Zn7LILoOvDP78rrALv-iXgpjAF7rzukg6CJpccc2Fhs8n4OiANd2eUqaM2E47DawCUsDvQ-nro1rGrqd6PNcMpL4Y7XxZakEyWp1-dTtb2frJpxwSSBeHOqpoQhTSviAk9EvZl9YlbkE56ydGg3-8BAqZpcCxJucYE2QWUjASWW53dZq_DUY77I9W4Ixz6WZw2eXB_9FYtel8Qqd3A6q-fLGTPeqx-WibRt8oQ8EB6Ar1SIUOi865vjfZYV-mllStImjLxqTaCmFfcP99atA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SwD1QZnI8cgU0YZBVATsFnmbDZFYS1ScqOK7pyREnr5fc7HMSR3czJubWx8Yw43nkkD0spgOrsT84_M4mXvITw426oHiyy1nHW3XHJ6l6mPkHugktFW36_NBCGV5wME3NBBn0fx5zrV2F-Gsm6iDYZ2GAHzDYZKl5ek824OrHWmvsk3k1yZeewk3quGVgZaWVa13n_Rlcxg56aNvlg0BGqmaRSsQZWQnTo9X1FBc-ZQAHgmo_cdjdiEWAA7BhR88--9GFLR5WS9-6xdgn6ZJO4LaGYcFOxlDYdS_c-SZyHsnVmKVIDxAqM9VxRq3dnttgdgsDbJCuD_Fd1NA-znYDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n9uZ-51gNTE9elNNIW4TiVbE489S92ojljBlq4fWy1Gny5YTYooa7MRJhki4zakNYFF0A60_PWbfhgtvX5K-uPJjPOKP2zvqc6n-Gact5Qq_eKzJaOKPS1B6QOMoLmj5Avf9lXox7fKuQGq3UAWd4SQ6R1_hYuGraA8Bssp7cwmDup-c809aG0lqEoG2SKZFLXM_KHTnInljhxE2cfOmsdF5kArf7i8BkbKNF_rV9QKFoGcAetHsuulNe4Pdba9nGatNh0sENr_yXDikk_VTiKTVwFaDxU9GUVbdljOfuKB6f03zvycmW_yaNDrTglw-kioy0ReO7iQDAg5w6PGWFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rd-n3qb16Q2Nf_52z-0rcquxJBYvXZ29-5ksdJwvPtYAytl9J2ZOzqvUv8SQjo3HIU0Lzd2oSiW5MK7-Lnhd8rGpttK0TeuBN0WjpfDW4rf54PEtMqpmlwCbAak2kkgLMcaYHPytdZgA_tocilYxh8vUPXgktK4dVS8ZraGuWVht-MdZfbpsdTp8T3uzLsUKVj_lKRqwphlMT1QwWt1-Kyq2WdwDRfyzdcgeUOYOGVOYViMQuzRDX4UWrbrhJ3x48hIgTDPZVlVGZhQoyvyKwgBfkpk25n2p3d7ukm-S7MI_amTOd1u1RgY8LxFK8AH30pgHueu3a6_7wqgEI6xngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGm0xJdN5nVLy92G-0Op4n9scAEDm8V4VCLYpELfpgy7PWqt_WmWh3L2ygkSK5KX-ITGaPlrs0AqZ55_JuNWnoLLqpyq0w-GrbMqPhfpACq0YdDzuCUrCvOOD4qzSkR5tHBl1UNRdrzE3ctRrCyzX5OPLSs-V7PU38EzvP7ChU1GoqQ5_AIiqG__jfR_nH5nVdL_8FgnEol6c5C2s78x8fwGi8zhpLEPqCcsaV7SzOPrqanPq5hEWvkfCXUHy-rKOaQc7s9jRfzY-KnOAt86k_8pCjdf2OFs55e4JJSUqptf2WbzkmSIqK3hke_75RGjl_EWjPhfjT7h7G6kEJaJKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rXwLikxgqcgHGGbdK_s2Gw5AlxdYbyIvbkMlYiSavPmKg14JJNld8XFUctPxkkaofyIzN8G_OPotSpM88hmqglN9km_MBaa4geRGRHclDpiNS8ezIrok7EX6dJtAuYbWEnUqk-wMcJkJR8d1gsZulyD9Mr5_5NUtoOG0yepmg5zNwTlhgwRRwnSFJA6CrE4iwDhLSaoxeEERfNj4VUbLC2CxfIrkqLNqxE4-PL7jA1q0vLasFqzjk0pnr7wpeVtATj8UqQrf3wB3sO3WhtizVno5Wb3LlE0r4w98KhbOCzxMVKgZXbwOnAmLvETMKYVu_93AzW1nkVeDMH_eJIXUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UR_n2y8Q5U8Wd16FtS6YwUYKuH474xJ0SNPAxC_Pfn1nvlxAVakr5ssiGpBipawIm5_VbWvg_7268UM7eTXWvTUwneNEb4jH_xgtSi6Bw0E_MUvAsCuvvFMgP64a5Fr7Hxi-gr_IUTYs-EVwaq3xYO9Z2KgywpPCYy1P57ryIRrGYyJgaPWwfJS24J5PFMPtM5jd0dUfYcROJcOO3cB90wqLKuQn260ML_twuOPTApVTmwovasDvcZnEJMtUvCLTTHHwcqwc2-YDwe0_AY9x24lgLwgIBI776vH-_ybf6TL2GsEcMfbQK44_ORAup4uvCkoCDXHTnkDtD_v85doLQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K4YkwxOt7Hh89MRUXB8Qv7C8xhVjxVtsbW6hyvk-wN3CAZhLxggzOYg0h11tsIVWh8_09DTNjJMCHERc3HS2_C8QuS-Goiz3qIRJ-6WNOI_kqS-e42brGQbdAWKrCtpVa2ftFuMcDZpp8tMnfuBjaF4U_ne3ree1yDXbhbHaMU763it1c2eGC-pEjSER5abgNedfc8k5hBilnpYAAIdZobvKoBiFAk67ptCpD4CbeT2V54tjmJMxVuA3G-sDLLWttr7kBw9wrA-ic8O2-9qe1IJa3QcWQuREP_sC2SESjv41TC4VGyY4DIq2uZTIyDvPTW0fxdTKjq8uMI-6sLB-SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CJCqQZHnmjmps6VMM6NyiarZy3x3Ya8zunjM8pF3NgCR2YHWm2cRpIx-HRbU9V4tyqf8uuBv8aMQ8akPOdqRiYrfESHajFCcRh_kqACRyH6b4ZmZ5GGHY06MxZ9qyef7UxkyEwdlrVLTsx8twWcf_AWXrj56SlakHTR-z7906frTdzmYiJ8GNOWXOTfu_UNFbmbTYfqgTHm3UmvpO7P0NlFPxtr6KOr4NiP6JY0lhbDSXrIS6AKDnzUu5VK9uNwpcgsmoR_ajGr-xeA9IfdmT2SkTXoXJHJOZC6calNLdActW8vhhhcrvTamaCulbDhWirDnG_OxbnIZO-oWHba8ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RNioiihKYneOgzW9avmxpZnvBDpdBcL9E3mPggSfm0WnHGNLglJ5-U1kyJWcYNF2Ujkru1AiznKImrLhEc6SI3q20vnhvZwddOQSDQNzjmbSRaaacPmcUfe3s1dPXQS4Ge3cMJhIIShdCG2MgPdrJTzyxM5REQGmHbQTQ9DCsHtcsbagJP_VvZAG6oVvclsnMgtO65g9I89n4JPCpvfv4H3m7jBtIwp2RzbDZ7x9WMLaEJK810Mnn9DisSmMZxdhLjfEGc4p8H3J61qIXFJvUEJnthbushbem55YJEUVXRIuDIaiCohFODGFRNpl-YUXnrILOz75bajEsA7PpP0EzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HomzfnN5vexAwLSNMrhhvhg6pckrf0JOZsqlCSxkgAkP-PAjIDA--DKGcL1Et6k14M0jj7WnJOaXIN5nu1dx-jKn9f0SvfwwlciXnc9fItNce667laDqR3ol7pQDd1tRBBrCBgv84YUZBwxLQfr3QICCtF6Otmy0yI7121UsPcb6qdxb15K7K0psaFyBrIjg8lnlM1cyAi34SqchPaDgMpVt14T9tRFRSAkoQNgHznRlrC5yYf7GJs5pL_Xqrjoi7EP1tHZza91nP2L8jHSR2FCnW644a1JeLTfHlKZtGQ0-ILPXIxZg0-q9LQE14WiBOfkpCIs9hznT4HNsQug1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bdp8DAvuYee5L2HgHCQhSLiD-hAPCN6s0YBW4V2Paz2NnIe6SGoPnQI7_I-LLk4CLE7-glsbstIIFBftrRooYHyzPKW3btXgD7W0gpD4HyWD8t8masu2vFNExX43x8n9ts9WivuoSkqHOCNhBo7H9NhgBX1otYhwXF8jvbOnAI2eF8QtTwLc-HEqpNYRtMwdkmIwwYz1Gr1sviNNep94Yoi1WvrUC-eZ07Zs629BgSHvBrBCApYoPUbDNyC-EW8LIv5Dc0iaylO4jgE6agT-C70GryzYW-1vqKAOVebn6IZg6ryId9JJrg_YbqwXiCj94-8iatCw8zI1AZXwzUbERA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ao8g3s-LSgAVcYCa1aCRkuINzs8LjpSf4VwTrpzgkrgLtL7fKPqxtRFtEs5EcL80ydZy5hZuuVKTP_DkgYtZevTCUzLba6vWcR49RCnET3I2BykF32pdjiDmLvPvCTOeNLUtTomOODfvN5zvMOFwdTkfDsdoIhgJ8PQ7CDvAAI7eAKAZgcoUKEd5KdO_-9VN1w5na1Src80gg1zphYS2ePap0-Sw5UG599ViIJgrWwCRdU2yk_x4RmgFDV2dY-1wkMFdxZSkx1LCQSMPmaueg_GzGp82cXYF31L_p4yGA3zT_QH_oPAn2cS4aCSxvTlxy7DUTblhTAeCx1CvJSmyiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GgUBZuX26CCtd3FGF88qdZwvxL5TLKXUUrPlDcvNFH7FwodEkx6fkhF6RZq9P-ifz7HfxHKGAEFxc3iLuCJeEJKvx2pOVOvmH6ZOA3FJya8H4HqmLDoWdTIc2G5QsXDO0PB17j5xK3KTv8e89GaS4sxfN2PcO5XGZDnGAEo9kaHHVoYcyk06APQtzWKa7ARvGXvcTuLsCed5c6y6LKGW_SRHnRBS5i90kohvyYHcRxSSVrK4FPA4V7zbXNuLqfGSiFZsF1mzdrHKJc11fY4kw9C7APkVyS_wQnQVmtGHa47UYu3Jw8OyzeBBfA3zLfgncc24-wAf2W559E8Dc4fpug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AMIdBTdyyc5lGXOcjFEeodMwDS9ElSa1UB-ZzsZ-TzI0KHQ2_71m3COAlVo1clOJqk04vCjbUiDind7FS2hOiUI4cKKSMKRAWfPEA0z4WZPeOcyTuB3T8tY_cgP_qRZlXxzpiDlcFa0GBwZ_rbPJSjQ7AkHJ3DEubKqtiHEarOP4nzTx6DXePFmJXR386jg_oftPz5jGyb4ZP_fg_IpYGYlK-OIOKvt8NTzlY0MBJy_OovN-A6xZ9cAOokK268DZycsArxPt1kz5d4XirSh7_kPv3VZiDOs-vHtz8Jzb85gb74LV2rvT8EG_ZfqMNj3nEQzDCv0G5uY3QnI0QPfkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FncNlmZg6kX0jfGMquynbSYzZQ72NpoktFmQhy1ST7Udy-PKwTROeGOrItFE5eRbgH4gBol8rKyxv9kWjKV1jDRsaXhkKbxmM7KFKhX9LB-R2ivgJGEAgg9D1zr5bKX-967jn7GjtGgp-bLdbvLNRmm9-OFXvESLbyxalvYVPiu2SZL-Yuqb7zIZWhfikhPI7ScazY9aoqG_b59Xc8LDloDH-WMap4nEciZfhqhuqAVVcQPH2jUXYZx-ov0gNMLd9OKHL5MArdpBjyh73vyCjFHl40eln51puuhI7z_PNsXg_OnMhxcJduhaqsXHy1dtVAZE1C-DMH6kwUOgosO9WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R7R8iUyDTp7GzBxlpIP7a-xjWoyF1ITiVA_wrJeFgwyDH-OmH9sbDRKYIZTdHpkEYEJeagk57ZozR1fahwY70KGws1plmI-W97EHBlL9r_z2nXHXHR-9dkCdzPHVHLf0ts0W5vLOosw5-gaOlu0r4X1ia3pfUTslqX9e_5GFDPqK2vt0VxvugUge8mTD9hX8w7kAZiZyBj6EZcPuYrVXA8N_EwhVIEFAjZlJnQkClAuiAG_TW-SxpgfAEyfmOQNUEMHeOZBLT6RZrlsMvl-rtRo_LevKSugPD1mYAL8P-mMG_387nea5hRmvdkX61Ism3arga02d5C04IktjJsrOBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mULj0MUYsVKdI8tZkndDWQ49ucqEJjRkW-62LIbeQH543mBeHbB1LaSj0Hkb3zzQjd0zLmNufF5ZS78aTxwyGVmM1JQLNC09T9u7Wbj7-SZXVvH8SoBlXe2uStXu6ItAvFy5JFrKMlSDkL6PM6fDZD58XQG3tmfk9YYe8_08Xsc-lTwdSHeXFuHJZQWd546_jSgMFxICLu5f6lKDJ-F1fxaE_jfbgfXQapfysU9nYXFB8nTlEieDfj8-YXdPgIv88egoEnbJuemCeqSb0HTatAy8NKMrRpms5T7xPSWpnjd9RiLQeXtt7DqYJwSaLDjuI7smVXw4jQd-8P4JLx9Xpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q6h3Y5Bd9q1XBhp8SI-99bkRqiiFOa6X65Bs2RI76Jk86GE9wpmSWrsZAEGqUEcXoWqOfN_13fzopFWu5IJVaHFUQfXIlsQdd2qlWcy6Oano7e7xLYICsi8RzQsgg_t5Ftznta_ZoibBOYoD4Lzj_qP_rXpf6ifWR8FmOzHDRSzmsJekQ5Cg3c4lIL506qm6goXB0pXd8V-pEYlNiNNJsPfARsNNWnigaiwXZDeVUqVbHsHwFQNoCfaDIPWlxAhNe01A90cMiS41qPDqq-0bqEy7vJjcdv2zH7krkcpwyZjLoZeLx6vGshVuutzVPmiyYTciyPEc_MfPjxPUZW10tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOXT_pK64ZwluJNanXl7OUImaqPS1yr9rZLXDPcK2Nw00bLBb5cirVVg7mtl2RVGnU2kP-XIzDCwe8CkY507eTJiLtMsYONHTe0yqCKGUJXLv65sxyq76WIFY8cvhjkpJu87VC8Bd5K06fL9fgZzszDjLwvbgEc3GQF8wC1c78FRq7FK6hr28wzHvnwAIyB8_sic4bpRUef9PJYzMiokjBpizW_7k-rBo0Mf_zULcr65uD7xDl4U3jWF1py4VyMFTwJ2E7RqnwhsjdpdFKC2-dq9Nr7cIrAZze51WcRdENLirvf1E4syYHZsGx7sBUNoQfYVzKvfUd9v-j3xlLQP2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sQrSu1DH1EiN5MuaacmZxO88jwnXuUUsxnScJRnS4PHjIEDb8YXEhwUJZTAFbwBPsprVR1sDiVeNy5m7ovv5XASDKPUJuVXd9cFpQnS-F5r5YTiEPi77kFuhzxhPiZYgQ2KYBbpRFnFF6UfFFD_XspIKnV_dbI_ZmBITvdA912PJ5qkbSA58eg__0UaMHw8ijN9UdprwC-ve9bvN1xs-1sjR2OJyxKvPRXqn3uuuYRgHodVO3kTHIn95Py7KL0POTcxdNmTrQKNXP3-LIynJfK6D0Rjk_yJ_hL3X-lKInvpQM3-wb5XJiSWkQhiOheihRZ1du-6qc5z38ZIL4o7vKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G2cmMyKAIIbHSXq7bpDUIzk4bhDUaZFjYY7n7ltbYG2m9hki9k8qhplao84xwMUjy9De70XZ3VlQCsW2ucxq9w85QC7h6WuenDDHQvGV59-LQBWi9BQZWbgOnpIR7ECraviTv0KkSmeF8Zuk63WpRIh9RhrjOVj19g6_7l13N5yrcvDWdnzP4VB0QljJzBRTcb1Ik2g52UZnAtuAIBOJp6GNMc65AnPavZf6objNwuYdN0GwbpDJZgRSAJralPZbvtJiUOC0BZ0JTI3sZ1PHCtUksWZR4a6InXEjJzx41ksEehsscCuCEqKDWuZMTnzIRtPWW5oPyJOey7gupKl3Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LP4TJ296u08BD58oI_V_YrmooYS98prugiy5br15ga75tBnQok4JXg8pfTqjs4OCuYXekPybPdsyo6weMKAU7A9ddMtp-Z9TAFoQv7ht3TtVLiTJOniBllNV0ZkXA87n1onHIXUCNuvPJ9v5IYP2yhQv_7B1dAtbQJv1K1IkGetn3OkdPH-REstAXTiP1HsioTdX4EAu21xHGwLoPRWziY8wOsYvlYsfco8AFTjM_Pd_qNfyoXxv1-cw-xn9_qgn2uULRFU1lu8XHZbUUZtSV5bXIolkU28zKH2eBO1ZTM8hNPDIaULEMu16rnPqwPUY9qIHyc2BKXE3MRw3bbiX-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/es7zwWphZEgxZU5vQi_swG443lxTO2QLEHUij9kYI3Cl_3zQGmrLfZV1GMujQBUG8OeNGAkvnSdR49jT9PgUzjKnwh1QQ25Ij4cCYKtWt9F_fyKExCn7xpdnYmQsvR61gB6Lb2FciS1O9RW4AnK_qvu2pRW5JufoRwX-U5puzOweg80qZamlCKs1EykLj7qIS0aWwj7eyWafnxePLiNKK-Lt74-syu5_JEtmoPgfXAzZAWiRsgn5yZZsmI8cSOcSWlsXNzZXDR8_YqTEcjRCdBO9QQvqaZnX6wv8GfC21D-_U8uj_T7cQhwT3j9NbEgvInOYrX_1Al3G0vNUroT-RA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8dTP8f2YTqw4zk0pqwmkHVw7GvgDSkvK55ef9yZe1w3trry-e1bp4ZwQSv2qJJYtgS38Hxum3cHmZtCGjD5LFnw31dvs95KrcwEXaflZ3SGA5q5l8bVFxH6Rwp1tehxcTX3rY7K-C13zkYx2Wjy8O3_wSuraMNw0YWJ7dolvS21Q9VE5HwSSXbR9-m5FHO5ttvUJp49geAGhfntDW4Avhwwzo5sVt_UqYrJS-29o1ljERbCqTgBYwhpKjGHQmgsShUzgydF9kX7byU5PublUKYXtBhc8h4yS3WeXQUr9Nh5vALtM8d3hu0r8tEophWN8NtHNX1KyTewZGGZOi-Lgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uF64X0x8pK1GdwyADIQK3H-QIXaWtnNItc9rIybj4OQIBFNgmYa2vxwQ47KXp0W1iRFXRu9mWreU0ekuxnAFqYdfThaLsBk8KqDdFtDvkfzh6TQ3LhZT2IU4RdSqnftbgTqAZAc7V9cew158H4H1KoMfZ1Kgf_Oi5E3GF6COF5IlMYXtlj5OilskAXc8YDLZPnGofrPQA7Otbj1uq5eguVvSmNJxr7D6bgUP9Zr0xbc28QGDesSNDpBlQAU8gclFwqSZN0Hx3fI20z8AwW7HT0m2zomXOHkUWDRxm7u8CiVUHWms7oNYP8HFy-slsbXV1Hv3VN6CU9oT_ckPKYG60g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hqG-tYZ0DJMEWzBf3CzKphcCEc1h1nC7rFBt5w-x4uat-hPUJBPUJvtS6Cpui3HxnK1B86I06hNnE-oWed2HRN7yulJX9kSr-7PMO8p92AEwhi8_KCF_pqpT-cfvTEG_OpWDBee7OL9niqaLk2bbBEBgNmve20wcDtFGe4Tlb5N92qfmHy7RtnlwGot9Jl8_SbxVpWLF0gOtoyUVqK8wu6mZ3nN0A376VR4e3XZk4B44xWXoU_8BHWV93wY4kU9BZohmGV6TxWwm6kT4BqXcDxBneVln3HMXSB4kGYXAgptfpJHbkqG3c01JvfyqYL5J93_FFnlI7DIQSzVkYwpe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eKcVxtJOPLW28MGZj4_jYagZ2yc-zVISFtu-VXPpFoBWAzrGMgZ_y_EHsP2k7LyJy86ULTi79TsGIlbh9Zk6WTtc3CmSbrriaycN4XNVdY0YqLOqnJHLyyAb0qP9dkf5Po20O0hALTxgyrIuD8xeIPaU2GXmn_XiQE4r6a6mRLFZ11GwVyDczjI99ZP-6e3u4eJmKPSceIUJE1_wDYR_Gs8ega6BIwaL0t2vcT_Lp3LpSyLhJqtZdLG8CG89PzKlV1G1o7yG9WoS_A_oFXq-6HwLGuMHTMhQ5p1tROK-DK0_gDwjk7FRckPE_mQanmGkZZyIGXBa-hmLBAFqHtOZ9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9NTApjGYlmN0E4UqSc-kjZMUnYvQJOJeBwzkdlwJhHtmSon6wo1j4-WKXpMnzQbceVYcB0Xkw_sCRhadtgqUtHfArDISoI8oC25twOfss82nP1ITaI0mNE3GFRLwABI0FcShv-bJi1fh4HcyP0eZ4xoHXhzajIRz1mKZ6GRLzH3Lppwqh2VmfKfjLM6VxfExtLvWB7_7wWuuHWwcBtFeEVmLuQQZvN5bVfLmHci4gGsrXX3bvOYd3IAipSrHRy9zWw01ViylwfNIz6pgPrxd2HmoLuCv3rdTaXGw9W2X7SIkAelj-6Yae_1Zwuxmfc6OzJGIElj-2p97blgrZkYHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s5ax0ZEYEpMCeM6TgPHCaNFT_0aoLSj_x5TxXcJuKhyairwe4xqbKSnFF7mogG2Mj-sY60DX05kKaxYWL0mliTaVdH49xpK5-mP5ZgXdq36DD9O8yKMlauKc7iETJWtlPeFi8E5izDsOBuZdvHiXE9mZdj3uIJpoOI0vX-uzubMNbbMFGSDPO1XpKB7gZnMey1GeJ0ndu_Uz_hGJsDlYCODpUKaGYguI7vlxOnn2mPE1K9Oee1r60hcwSm97cF1apb7s1CIOCE63fXpcuUYlWtCjSHlIUKe1aWORCZQYjHreEp8UkfgIk4UGC0HKV6V1Sz43L2TZ_1iJehPA5Euu5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OemFtg7vYqThHDvABDz9vOQMKCw7uSwVonrWQ2ySclHDUBpvmeDzYIhy7FZqjbP9z_p23ilg7OnkfpiHUPCI-rSaLum6gqF9p9DHxiwTovuxCPNxlyyDH-7SGSKiaVNMLL0LjoESlawA6oxA-jaoQ3yCPwxmCZqcrhzN5aqbJEv9RejE6nD_AeGbcnbvrTWwaLg6Nc60JIEskuyKK_wfHHqwSfTFNbABD2vAQ3aNyoBUd-wr95wuUgRf1odkctrCkmhJJ5d856ZeW1HZ5g942xxocb3O2CaDmqpX2b5m90zNBInEbQM1UvUPet4rCray-SkRV7WCBgf7wunBeWrC8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LtXrl2RackOdOYjvrgmTibNNLssmg0lnSpb19uyvyGkwYOQwPKhP_ahAg1Dwg8MdHk1ihRcXw3qZEPlfO3QhPJyKYN6N9e6yC4WtPVjM6wHFndqRlByfOrA5JSrx0shxg1nooZRZoXJKYnYEiGfllFzmULOCRJz8bPw6DxtH98KtpueB_sUYTnOsvg43htOGnR0arc8a2eFRFRy2Ml3OdFckYG6dd8VZ8EyDU0X_g_eb5Uuap6GdLqtiiUTvRUMHCWVssqKjtGRb_UmQbx95s-s8rvlYMH0Aq6Cbh6xRKIU3bs3bbNXRdpuULj10oxoxlGXCPnC6e7vVR49HCIcrKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGJbdCaCsTbA0dEhrWAp5SYOXtHmE2QbbRo0494819-tIw797LNAGTRjuz2Xj_PtASG5F7uvN5JCl1QiuSv85oGmxehn25maOfV1rUrQryIJRpi1j_AP-gBlqhwrJo0ztw8cQ5odG8eBtGPQ8WLmMlUDPzf5IL3gVNaO9nhC2e7lw99kgdC-lvujobkwPfRQygNB6Nk7uqziQhOtriLZ5xoHBoqxfJGH1Pg_TSrTgkGrhjLYvqw3sXdlJ40scAoxo7MsJ0yKZfp3bwl5ePxBmB7KaBljBx-oQHrBJjFnqwvpUDSvy-f6H5_VSHqXAmUmijCk7VQ6QeIDIjW5dRhhew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yri3EdXGQqiD3YqEJF6tAYMsFO5MAAxgJZEMWxz8RWfm_TdC1y8TdtTd1yTfrvxA87ABtBf886_lsM6HRlnw1vA-djEZpnn_7hT25CrA0xfXUZAV8GNh51oXZoFAL3EijuNXLavuqYNjC-hyEsGMRP0Ua1wLhB8kEh98IDhsF63lleFR3mhecXd_TQVwck13PPZdAvxJ5a25ZY_MHNLc5jtLkBkZ-tXlpRtJJuxsGDkqJ7Caxt9nVuiXzTKdq5eI9K3zNfm5owv8qNyN2hAtXCibUhFw92BOHo5WsfWLERbDFBwJVdD9RvelBf4gSduhu4gkclCBitzCIx30o3B7Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNZo9e90IESZ5fmXT1oMDXluZ9MBnglGRQlXVvwqvR_C4sxwP3-8b2KXZ8Yce0ZHGHqNaobi6wPOpfoCHBKzCr527neUO8rP48-0i4VNlkiCNi5x4zIWzgg6rTu0Y4L7nP5R1I-a9CmX3kID0YjRqYpALjvExRpraSxPCBqFkvRn0mmQvpaETr7BQCskkhyD3090vIaB1sl-b2L5f2PMFFOpx8tTXRvMVvKL_c3b9p0xfD1IHilG7sN0w-MO7JK1lAZMHx7TnXwGtMGk89x_XyklIDjtQ97ikNpcSlrY3ApoQgkEFdlxQEWhaktwX7DQds8NG1JgcEdX9gkOg1s1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TX3M4c15RuNXzuiIAKVvMF1hQ4p87A0IXsGK8UGRWegPOCp2vpMsT7HGmOPiMiWtNZ0MTYRai7sL0WgmFMCyVnzNpHPBTPW3jFsJKThCL18z0t0DDz-u-u9sqRXfrNQBVyZPu2CRjNjKaFj60c6-BsAUJEdb5mKMuIYirI-B9w5WkQlXBpaWqG2YqGQLq-bsjcwTUuBA8mikEkmjbYLbxPFZGb4LwmMGhc_yzDjHzsUwOTj5vzLIdUYYG7LRppsBIq5tnGh_lKmU6EjZiY9RhumnC__N1gLILIRQzHffy4yiemWmG7i3QEAOOq40QmoyQ-S7xNj9ef24FgzkXXDBhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rLwuYn_1B9OZPLQxCpk0kEWnxkuO7cmGGCXs-cnf2he5g1aZzFW_Hf3qkqRFHlhRMogejcIGXGIplv8EG5XciFUqP1RhdY1JWoHEhh2kB25oaLwnDgYiIQmKKNU1zN-ZiuYTfQ3VKX7LVC3VYzZpHFcoqbIcrFIEImGNe1YYOMZ9Tki8y68giNpV2pdbXIa1AJPZ_k0co86M2_0_54Ynl7qvekcN08e4kEnCaHv7Wv75AqFQa6yqqQQpVXIra245QpmPkZNU6qJK1n83evZOyBwBvZRUlwIkP24aFPkttOCaFBY_jXsAiDpoQboxL3AIJPm595ca5IZ54Zw15JDrmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FunwgwGs1QKixHcspMpaQpIZEyLT4L_B2TAmdiYq1G1U7NntdSawDEWUMF3Di-FwFDRf_HKXmhQJZcF_jfrEMYLRbokLS8l06fKZ_yU02EiV1U1K28FhNjhsLMMgK1Kg9WJ3E1O2XYzwQP4MqwvspmtvG4SRArXxYxsA_0Oxl3WkbFyN_I8lxsYymaloW4z82yWBNYnS7bs6WiWktXuI-h5uL0SbeMKV2j7-Y-GZTeWqa7CSxfLQgFbI9JwuV4_4OOKl2nuwV6-pTOsM56tOfscWnKxUqN5ElUiHBA4XtReVyeu2rOojOrL59LNvaWUVkIcR_D7CfCobvpBN6HLWxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtI-Bv9s2hCBfWYAnOvU81bENIesQbiTyFPtiQCgXX18hlov0ed1PrDXFWOPqBGA2xbI5qASj6ojWh4EzjK1yu1vOmRg1jaqoGb1pp0C6YaXSzodsq6dSD9efk5wvA-t1XfwdptuLAqB0dYEMFEMi0fKlCWvPw1iOKcCe-JVRMeYo8v7Gf0pf5gw2Dr1CUYahIW6-VJQXgpSI3kPjo0IZsyutleEdLbXM3yAsCkznS1avvkOGMjzdsf9rKPKcE7iAQSC9_KsSdbVdnBAg8zAGDJXeXFMINlGJ9I26b9MxrjgsAGWpkqWXyFp9OMKlOkcU0_y4THEFinoB4QY3FSvVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHNOSd88MbhpKm2wpUR1iZvrsaU78q79A0nb8p5lQ0xvSI0CWP_VX9FxoNW4ksd10r2vpyRL5_ZQi7vqapVg2TLxtt50rEq561adi9EAxH4Y7K_C8haY4b4MEWqETpeJaSEcB_2PtWJ1F9cK-MY8z5Ykz3fkZ-xvxGwk4XjkISGQ7M2vRl0d52tqtgjkAFUmfMU7GTB-mjsbjcEAVDd1gX_WCof0Ig6jIGwppKS5cK7liUlMtpxuOk4SZYpqhZzwdGwFp7rF0bu-TznVsPe0Gh1muSqAavQ6iO08Yjkni_1VG1CTrSEsIcJ1JB596B21NDuWzRS2u0BvzWfsi5IXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qu8883aj9QEoUE_7dgGiHPRca-P8WXG_1VoI5UJ15j6erhEoM7V7aLdMsASpmkrA0zozlEy1uA98l0rYL3tYc5MUquDq30OebcoFY6SERBjuJwtYWvrTd0tN3OvNfNc2LIDdhA8vCUyP6VUt_KCJoO2TFXx_YnB5RrOsk2si19UFcwWvvfWB7_46ZTFuVG_qjBAImk6X_KXdNji5RJkCuud6F_injevhIrYsYqzblPBc0HEXu-2jorhG3edvC_vaOxBs01rJ5EN2LA2UdW-wt5SP9nrlr56hi39ur47bGC8G1dSps4yhHmDxUenbHTG245d3DQ6UqkuBOZzW_sggxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IStczYW592P3N5CBFIClddvVRhMUjgGgDoVNote0UBt3gfreKjfCVEiz7REK-ViBHUcpL6RMYfySCrEUH9c10yxc2FfssqWobgE-Q8Kmya7Tlqk8EPTTUf3bhce5V0JjjGCGuBn9vWbp8nG328d2S6UQFtKJ0LbaANiqMFQOVuBJo4xLPae-ty7tqk-7vg7CB9DENnNtW926oxSpODYw5MJrlmQdxukJ3u5sVCvfGukPhcCQQU7peD2o8fXr3vjnTqYnbGu20d6bdr6XISLlVKhdHABI7rZqhSlZaGmW6OKehJC85-xsbaX9IVNNAyAq3SxG3QoVo9Cp-8OW-4kdhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=D3E_gduSQz0YXPsos7ahi8JNFoOZm2JTQehNoDrE138P7YC4sFSb6soIB1QPl_1URY5SzSQ09csHGc1epZQZqGzuFEi25DTycpElZAenUKNvZz0JTQ4Hb9hzZSFW7Aeg3gbCw3ghw7mb7n7pu0AOnU7n0TDf45wLGZvAHoPa6v8PNkTeTvgH6HBSkZNzz3aQex4229oOoQh_E9S1EdfyeWMEOedLNLyQ87_Sh-M4dMPXCsoEXHfOJ79IDh8WJv8Ze0Q8bMAo3leIM0Yk0uxT_Up5kEUtZ4I2WtUDacNfIhyhtWPHetXRs214qEKsxOkNZS6mMX3k8ZiUhHDTS6arLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=D3E_gduSQz0YXPsos7ahi8JNFoOZm2JTQehNoDrE138P7YC4sFSb6soIB1QPl_1URY5SzSQ09csHGc1epZQZqGzuFEi25DTycpElZAenUKNvZz0JTQ4Hb9hzZSFW7Aeg3gbCw3ghw7mb7n7pu0AOnU7n0TDf45wLGZvAHoPa6v8PNkTeTvgH6HBSkZNzz3aQex4229oOoQh_E9S1EdfyeWMEOedLNLyQ87_Sh-M4dMPXCsoEXHfOJ79IDh8WJv8Ze0Q8bMAo3leIM0Yk0uxT_Up5kEUtZ4I2WtUDacNfIhyhtWPHetXRs214qEKsxOkNZS6mMX3k8ZiUhHDTS6arLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kdlwVJrKZnnVO-NNZ_u28-fcQt2W2ttKaSBPetaHPp2DsqbRHZWdBureKhFXkwd2qwNULFkbSiWfe4oNcxdLms1xKhB-EJxLcrsmLmVt0WlhMqkDO_Ab0Gauvfp9iCqUXJFT9BXjaLFkZpf2NQ3J6-rykq0w0QlTVk7XfxyzuUrKbaPnkfsCEsH7h0cibSeT3i14-0kGDIWJTQh-HmhPjN09-dg0YS-d6xJbCVt8R6jHR6_FqyyxGbVcKGOpt2cndRbW7v2O0Atdfq9D2jQypM4AwGFqMHeoiyITgeHkz7yl6MPmQeu83kwriIdmGeU-prC4gzdLY4B6GId9onJovQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaFbF9SHF2Xg3RtHJlLreG1ZznKiOBWMjkbkkg0cNYo1hKAqmXn06eck6aizbCFj_-zY0P4pK5HwOARaHI_VbobyrvjUZk_XIxAgKG4CaQTW3g_e3mKYiahLG8Qk0HFCOMZFAO31q373StXK_BS2gRqs87wtwDN5s998FnLRUSMt0VS0oMj4X5Qt7IRRQDFEOB7DZHWndKVUz7Gh4qnb0qIrL3JlVh6_LcVHaP5tbaC7lY1lKv9lSZ2_wCf58rgF8GhbhxlwWQCaIl2DL6nn-TIYgm7pNI0Pfqf3hTJDkoBhuVrJTHGOV0nbAMnjjrkEboJ4jkLe7UAcRRIpgYhcfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vpkZ-aTITUk7_AublnDUUJ7ETXndNFc12oI6f1rACEuhLn5CmYFycobG_Xq3xU0BmIvr60Eib367XO3njmmvHjLg51PhlKVLtZWNfudaCMaJ5E2mkRI55eTq6pXnuAatsFe6p1aKS4FUo4_1CwW5Zu4Ey-DRiSdCBj5f7tjDAadsKhV3KtKk0LFGtFnZiXeqQidOLitYsOrSFMIgT_pN5hAwZ3hbLhrPa2CFtup3vor90utiCdPo_hv7FiSkVDGxZ27EzL8dCc25L0atZ7ly73V5FpetWf3DYBPetcf3RjCvsCsJ8O57ca1z3UusCxQXGcqkL0SD4f82hjbTR4lvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eu9TeM3TTbf-OYVrdPFyp7rfx3XuVJsF-_Be_X_FK6BkQVOHV-J9MaKWrvXbG5TL9Lm7TIkoc1CQBDnaffrJ0E6insooNSAfbRcvT1CAm8iIj5O_HVASn4LDRhtw4NejFebbuwdU54wqBiV3gttPaIX9pICtzjTFu-_wNcFOj2NHZZfMhxdhaYzQHjQ0in0pCbbYKwcr9CxLsBgHnrYvfjFeUBjUBT7BeFR8l4aF8YhnjinWNL0_DJn4Y1dgYQxnOpJ82NFnkDp4vLo8fuvB2GnHBVnStv6T3kN7LmWgxYxpE1pOPyXUQrwajHdXsZzHE7ZuDSJt7tDhqjeZnCFd1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lZRqMhoJiBQCrtiLIuir-Awcmso57fO8pHkJPbywGM56sGi7QBKYq_O3sHeDcsiKMvs90iKruZ4945ChMkKEE6PNwFLd0WEI_hbnQgUQsWqalOh7D376l0vKnj24bjNyhk96ERgZKc34KA7zFYlR5M8js4hak0pOJkm95pw-9GupMYd8v3-rvNiiemTnps3pIckxFExRysfxr42cE4crAonGMpxJxMZjR6RmvNNXmtkUV0h2cj1EI4S9JuYmDIyZfWFU48KViV3xF_k1uLacWzJdbXTQvViKPu4hExzJ87YA70i5SbSpgACoSbIZJI7YDVLNySj3FjmtyViuU4HW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sm88bCPjFxQaO3W1oINbDYVscCsYMQN42EFzht1WHrCmhkfuYGjU2lJECC7DPmbCbvHPOFuy7NHE53kB99FgY1d446BDB56L9D8llsOeOGKIl_1Xoxcs40XlYPOmfs8BHD56taA4RLAVhY6bPDZA_hxPw-Tlb7j1w_yE9D1vq1TFAO1ikMbYUT-eAcwJomvjhBKBQPz7rYNkD7JAVyF3jGZU7iRIwCPUO9tXrVeHdNp8xy3XqiT-Eb5iqYMCCmHx8REyCe83Di2tN60_qXfIdhtTq0bxrDAMKqMq6G4PXlqMIOBFePg9iF3kSP6gMi0oD8Dmxjde4KuYbgmyG3gApw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/suGEdiDRQFWqDMX0ixDvSXOseIvgxK6v1wiLfmwzTF293TW7jPhtoKXmIkSeuxgBFFzF_pDGKveYw5S6GC8erPkOTFQFdCU87f0g-zYetvIr-GH-ZMotE86dN7KI-MEcUBub2nLIhDsH9qOGg6xa3KFWLmuHSHR2Dwp4mcho9czYUnjK4Vh70XhChc3j-bwPly3rUWfuJ2JWkRPZlpWGc8oqO3XRFbCbecFQ_MpJ09u1jly-vJKXEN8z_uLoPqyNCx8GnE3NFqfmtESzSimTEuSZJu5o38TZWdSC3KXFCWSOMF5LhuRq8W1IGn1po6H1qSpxxRwnyd93hH56s53CcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZL3EtfKcDPQ1vpRg3l73UMtY1o8P4Jb0gMrDMg28mTlJf_9eOsM5999J_fg4cI-ddziD2fRaaD9THZyE3tFpE-9WjAS7Pcs57laQE2u64jbWkkrxvAMDKoak1vaRFbeDea_UCuyDdZecXVlbzNBjhmGjUpbXvNrcnEDRiuUC58-45BnIYk4zZvQaOJpHUwwgY0FiWVE6T-T1d-OBINh7lvecDYd79BzYtrbs-iMVYqXhLEb4rTs-WzlviM-MV2MOn8ftjHyLCZ1Elq8JicO8ej2BvIv8k2I9WV_HrE_Kc36ZKh2va9SioWi30U1s4VD1YXWiCdSOgZh1ySRHunUhGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-YrvRkmHV-oxtbbosnE_cS_8gR5TTN3wU21Ok_4fOfkcaT9j3AVRGjzaEHFwrmohRz2ao4s6CVYOox2MzGypodwemdXmnOmmmwDt5X2vX86fcucj9txS6TKApehIGZFgEdznGc7AFt9vZ0gPqwI_vVfeyYO5rgqG2yMn9P3TDr8nM7Xz0czfUwSipO2dFMKlmjmYw8WfLWuo9X1h2dwTC5nNTEoSulxabL7P5vfzqOSKaiXca9g0UWa-UyswSHPgOuOo9C6-zDuJkLqWKpYfhiBQnw-hhAWweWKfnnxzZGaxP-8SU1L8X1RGClfaNzQoey9xfzRFgOeH1n-mPsv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuA7AUu7N_ebUx188_Sm5zzHb0jyxNCIxfSF5WBq3vFalS957tV4C3dhKX0TyS6Xhf3LjkLVc9Z6kTpgJIgjRiqV2LRCEoVXKfNAmSKT469n31i3gXxE6y39FbPdRJ-Rg1xg4rH8J5k6uH9N7P3hhzchzs28Jh7opZflIkm8xpEwviEDvvCXmVwn76xhl7k-8q-WDCkwoS1Nc0zl5c-xSuAElDKp2s5qgYxJfH6g8i0XZqEWTI005vDL7NHscwfQBkLOgF2_YFcckX0_ucoc0rJ1BAUSKDgtEPx7P8PCNjEko1XkJxWc3soCsIipTjHtwCqUf9Tuf79T7bU6xhnsxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vfMI63-3e6P-jYEJO9VbSrsuXpYzJ1y0gtG6vM5gyMUdKBkCGMiKrZVESOO69UI79l4xG1vPYNffL_J5B4H3UXJVYrHoDGCzS7QUdzrDOu1ej4tRUIFeNxcGGOxeayMf4e9MHPd5yKRGsPc8nUeS1CDtDmf_HAp1cxMC6vZvQDjGjxLFSu0NKrFWOAP1QfMiCC7fH5wgB-240EtJBlwmyLo9jPQ1pfqNW1_laejPlRMkolCvMLP89G54P0PAe8Ha3DzgAOdvbq7qe8imZGqsNIhsm0MYG6gvq541-_RJWb_8wxo0I8CqhmVVn48ihGTrkjV-3Wz0PYqkwqS4PSpyQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/osMhQtTtBxe4vjn0nZHyHEEuItzvObbrgJH4QI79YRY3C4GdVTtpJnHMCeIDxLOFAuQUycLRS59ssuA1SIpuSL-1DX7G80VS5Rp9JD0IUrKo6omn8AMZtRaKMuHJgZz88hYdMvu7r-Rd4Y2XjpIWNd0ZEHSi_EEdmlPIazjgl1N0n4ca9AXTy9Z1R3xG7bqKwGpNRNXeFujYltFMUwUJaTOCTsH_2NUutkjS0VRmC019x5u2ltoNPU9hq_HBc8pSlDUifahC28Zi1bVE7RanMmalxClC04m3zGGcIQqGnyP2t8w4WahrDIWmOQLnFFQlznTpzogaLQByB9Y73g-2uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VV944Q0jQndyJfTjJX9pgP_k9Ep6NUpXt_ls0vnPDrbHm6nG_CSwPPkdUuQzAUJ6XbOX19wCEMBcuoIcVtqpxcFXLFYe0fbkIv7IAeCu5ZaIFXhL2ul-wJQqTMKhj8cmpb53CuYYnl3dbks1cML9JfCFv62xE0bLn1cGJJf197CGSrcdaz3jHlKIF_l7HBHQ339ertB2lQz7yybUNx4rVe-Bz0fEjvoH_R-exIeg5ERHDxHhyrsRpwvAbfNGgoZWgdfITazNaND89VvAGHHB3VSoTrLcWDcTLsiAvj877GE6utXJODnXv8POUPUjq11fBSdakJRYGIbwmNsKOghFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_0OhaYIDVZ2WIjNVzTW_D31DcJgShmYcfnc6cJUoYl1nw8CCh1RQbaxaCcP6tfnITFr0AYvdtET7fyR55FYzK_aeiPGHuIv9yjTlHdPpAsa7si-lwNIymNuVsmVDlQ_vk50NbR9Rv8CTGT7XnAr2cL82wo--gnP_XxhmGrL7ItrDSukNUi993WttfelHU4ni6sYN-GSxxAPmNein9A2fdIjRPub_MQDfgtF4eYPQS7__O54fHPPRjUuu8o6o1AIl_elwuibkO4xEcQbDvwR1PC6zHwbAOhIA8f1GmVrVvuzZXH1pCWZFboMceRZE2EO_GOLmNFoddx17q2M-2Mltg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tghtkdLFem_jQZi6jjoj548s7gD0eDANQfESVTfbtCA-P8-BMZyErCm9rEH1uF339ej7KWNMJgIiWhvl50WdiBYPWCimDPkEBQL2XAZ0E9-9x26Qegb-bxfkb1ZDmjDpwvzN-EnNXsHdJ65j8q5ghbdRyv9cq5SNGAO6rc0V7oL25ccE-xzaSyNCBnKAm2LsCiyZZJ5cH2oisfE4ORw01HF00uoOrHp2fQ_8Tl261SC1opr-U1ECzRw-YvLr9WrHrz2xGKmvxsJqFw8aypXxoqVsdJy7qpsw3woPfqTeceglD8d6mLVHkEzPC4qbhv-2R5kzUFLmjOXDDvxmx--1bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OmD6PYUgXvP5GqAxVq9esaY1CQghVXXMhTKkXQiXTskqP0ESuHo3g2gH3C26TOYLT1pU1HMS0klnGSHWynDxe9rrIvIWD6aq8MadTWtmZwQw60QQ3MbYR2sPX0yg14pkMcNN5OBAwCdQsDgQKN5gF_eluKLmsF40PtuhFtSWae1OACX5zv-yov9tHHfLQv8ReazLfAWtBIXv_F950CQzUPgqzGt8VzCxo9xeL94kOwamSC7J0bQtnuYqJ7skIxbptuDbk81kBOnyE5odfuHzOEFlkbsDD2L4nhIkGK3UxZYNdJh2TPqnAtMWG2MkHEFbHvCal5CUBgqk8GNl_833jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jD8nQeSUfgLFAygLjIp0dTSgU6DpmFiOESQnKelif8qJN1a5IMaTQISfdcIilc5zo9lqxKkRm7TmA0nxBGtfWoZlu2gB7Wua1_VJ3Z3Sm1qABNZnIB1uVOwUL83AXMEEJ-U54Ak3FINuze7udCpfet2i1zp00hvoJYIqhGsWahSqcfH3NirbVawkHWrZVdnoclnI8Nfbi10IcmKyZ7R0U7XmKnW50U2_5QtTAKZY0GsPgD4eSDbdbRfyFJ0hBFWqJwcjWGkBz-talusMyybmiLDxKlVJekk4RpVNqgHlg96vyQLFkF1n82D8jNuHGnE2sAQAug0NuAvbvqot9AZuqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FZZ_2KoYp3R0WfTeT53iuGvyj3QKozMe0PdTlmkHJUUUdCMnL03gZ3JQqO9GTGk5MJNWxJ2G4w3d5J5SIJHwbiGr12OpJzH7DzefFkU3Q23i5Ft3ZT_yGwsmStziVC9cdKcw4S6lAPglpXE_Iu35wkvRJU1u6cZvHCvvUuOLsONpFVJ9Ersx8auK-Y6VIm2-JjiqlUaRqBymkC89lNtRvapJcwURw7iQBCeQ6Fvjwz2eYEk87pBIE60WjOZAGFaNQ3GkzRLH0JcDOkad5VzUBAkLD18jJXw-9KaM9Poj2FinFCillj1zgzArcaNWygZa26hOlxW911hQSZIJKjIP8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kg-4wuMusn7Fa-R_O5iUCeU52ncmTgQ1GYkc0gztnmKSfoVI5ji-Yg4BQ76B93hcI8JMXhUKMS-AJks9yuuOi900gvSj9-NSa1cJZwFbKd-n06CpdP6ekfYHvWKv9rt2dWTQ8jgcZYChUCwdVSiTYN8aqJ-Io9w4iGNMfmfR2_cZwuIlbTENyyiW0braNkGKKVE0dGzdA8O0tyusebZN3-SdOLPcaJqRLWN86p_uGDxooW2lWsBYMQvg8SifxWbBdVm0uwK8LiVJeZ_nwxDx5_lJnt8ck0ubMgiZmaJJR2PUxIlRHqeRtbzCv186fl2empPA9AuTVfUT4gZPeBLBlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NAryzvYAlqB4B-rmDZN1H8WO_IWXJeLbNGLDVJKhQ7isie0N3b2UEF193PJblP5-Kv8MGaGqfdNJNAqTKkXhlIyZgOZHNStB5cyzygD_7G7xpRUtrADK0uH3kG6txwPhphbndwyMBi6xVNUYoSfH2jl6SNAymqpTmEmaW1yi38Y4aw-kX7JQWQ4gPvD_M9Rb8xUnt3BJ7B0em6Mq46W4tFNxDHfl_PODLY5HCbcpG6CdS_uOjaFatm4ALgd0RuuIAbiAV9mT9BbGCaAZGhXAS2rPFuu-aNayfLqMDpqmc7VlSaRvbg70A66Y10K8uolpmbQPId_d6YBudPkUIwmYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lb7JN7yJlBYgASTfSta27KMjq3GgFS4rH04nh8LnhVmKwbtizKBKE7xNXl529WhUvYa33sJi9JkuSp9tIiUv8DuRaNnznur4tY-Usc7ulEcywaIdD4BPNoV6V_a90F5OVdOh3ztQZ2WSr-kDKPXNvE8b6sT-PNU9W7jySuw2_Y3sRDMx_SOKa3tWZ7SOGPQXFFp0ePyZ1e9NBrGU_az6rcpu4_XMxVeBjSOjeuTW1NTH1Q112FaYrlaQb56z-dQIQDsyUX-XwFfjedVbRCrzldKgbJevEp2hknOu5bM-phgKbtAAek3nSWZave_UXILCn3Xil_Nyaviwp50uKD5D1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b97K_I4tRS2CkWbDKVK3T67pn8zOxH_Vuo2JYjTj6jQQXY12oOu8QdpZW9BzFkw8z4O1FdVuqsSS6bedG16ac7TL2kl4nr65zuOOPcF6jLBoKc9zh5ssyBF1KDtmAMnP0W5X7oSkcvvovFKFkUeKAXsec4IjQxXx3e2c5p_x7h9HU3Nawg4k6MG7D6R7WeEOzWhA3vTrVePoRpX71kcCdCq7469qljXdzHRwpQfRi5etNusIr6c5VMsxrpU6liz7_gjNVRV8sqSzbIYfJWKigCn3QE5BDSC368LujCusZysQsl_Z6hGahX5kh3ivrVxisV0HN0ZXHqOg39SdQVlGXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bhU7TitSSt32sGIEH9UBdxsL0XmEqI6wEfbDk48E8nUNOpKovR8dGMglEGGwNrg-p5yetO_DQZYiiz6U0VkBsJhJmrsRy1SbBYEIesKuo5iZttjPm62meNaS6aSvoMyIBhexfC6lYoUpLtRNqAR11heBJdiF2LjObuu58wn8YYcuTFdcN8whf4kVcvAy54P9c2O_85IR7QVsHPHHr9ohJu-jlm7sczZ5PCuGn06_9sUp7zcCLd_X5hyaGRfRtIpINsdxyIxWFUtmcxSpr-FJgx0H1BjlecLbr6eabElWK2RGTnHO0ZoRdnUcoaifj04wsHinzSBWEslzPp3-yEHrpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WDHXCOoIJWsZdB8HOLKYs8M_UcXn1Jf1l88l96eGdhnS5bGQPtBhlYsS05VhMCh946qGE9Lnqo8YvL487tp_dxsRxC8ryfZG0VuO37AmYN7qUDJyX3q47Dg9tmZVfXxaDqx7-ee27hCU72hCP8cmniX2X_PhN07Akf5zdcUjWe5pBOAkAYQxANIJZwVQ7DX7SZZ7mtpW3w-tCnQsEpgdUpypYHE-xOxqrF-K--hOMrrDAXJRDS65IwKL9xf1vlyaEFpDJ6xNOXSwlw1YpWCa_j5PFy1NJzL5x7nJpgj9VpDM4sHVeeDJP4r-xbJB_noDDpzFC_LGibLtZT6uZkmEyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P89wlWvQMHWhmje-qrIRoWRq0u3sodxLwbkO8nxTb5cF1WfLj_zxMYGwkelqSWMw1gaa-kwijXXe8KQQNb8PCS4Da9pZogQxZtzyvHRmmVyv3hsSqr0qqZeIWE1UZO5vf-vuU-dZq5gpF2s2SEeGwosNvncXR-ZP3Sl5zOKrA8DzwyoLZSnjRLxgHFMOV8uMul_ZiyoWfbHn8rWjZJc2t0SdqbAdE62HO7kcPzG9L02wVpsS4AzT3dFTI7_laGC23P5W54lLGy_fEptEg5hm3xtWq8fnfZD_Ygptk2nqkLrMSSYRBjtNOMttZ1b9ZFv8JA_ZlhtEXmww1ciV89E0MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P8XMw3mwEgUxbUy9K9uBkn45BP_wfuKNnGqdhRarZDe_i4dw3VzqlIEKQAkPMkFOOBIlcKFTB0uIy5NYDM50pN84mOcCcwb7f0_33OczV9nbpeSIxYWn2Wo2R1cR3WOztxFiv3hmXD92hs24au1sg1T57PMJxhvDeyYNw9w3TtCkULImmYfQAQcXRU7wejGHVNcfLjGHV7RI2WMf8q9-cvWWKBo2oOllUZeKtWmf4CfyYLBjlPVqNun_aEPfxkxsqbgcAOSOOCo0XWRot2HXuODTkOK4-u8eeIOPbEsu39BglUiqV3ou9PJcnTA6lU_zFrhF1GLQS9PFDkMr7pl2XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tfWPkvOtBL6SOP68SuQeWnTZRuoPljz7i5O2JZOQbqflSjKEeI-oZa0sHrlaB9FeJEOFou4ihQCrZUFNASGCCUcSeUGVzpXT0jhBAVoGaK6Uy3_-eBxZt36LZiobYUx9R3RvaBchxgG56O4jl34ikFCpFJANyYRlCJcvSdGLupSs2tiCz31UBjrU5uLAugPgPl1kjij5ikNqCqEN_uMLiddQxUkHQkJTn5LFS2CVfDbLDoiQecLLC1C7BbNjf3K4RXBskFgpFs0e-YA2VbZoo6aurMndPunjODzEiaXL77s51UUWodNpkB6y84C_oCQnTmtbtdEhCWNzb9cv-z3M2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TZuOBCSfm2VlSXQAN1R2cRQhB73DOUuP4GtYUOSX4sIMQrp-NSe52ptOhGITivYz7Ubp-JObZEleol1TYh-j4iJu33-2oDp_gCl16r3fUjqGSWwzMddSU-g7qpKswr9PkKtw8ToCckch-fSRdXK3DefrljRcAnyoeyjBu6VuGbmT0t5jkTXHYQJG__D0cOtwVOhpdUKdrXor0Znr2WApaeVZsCeLzPlduKjA2ZTc5F6G9l-aErJtHQRxMuaeckG0qP2nSwrQ9qjZ_gUh6YM4wVXpnDy1Q-Xy_RuUNyuayAejZe4p9fr4CNhJo2w89kTOKdmp7lPyGPDSQE8y9Yg0mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ifXcIJUK4gfBuE45yiBQxvsZmiZPuDosOuXrVhXn6OyUfM4NrVtNNuROW_T0wNCqNVIfwN-zU3keGcgOM4GZzW5MeZe5ffin2jSB5BF5se09astv38ICDd4xXaEe4FVN2aDMZX9F9UaYJRp0HluW02kMpssDrzB1OHLWhDiIM_apQSOdxvVzrBrpU8awyZBKrN2-nGhO1GOR01fINE7-FEL0fkrUYKcpLCjvsd_92_txQHgx_skCve8IEFzJCdFslaVcMztr2vnWtlLaXGzEIH4rDUT2EuiAMFdZO8YG6wHmbBkEkaQUcYcsHNijPGAmYzRz_A6fu_ZO22Wf8NghBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N_IIJ6cevuw5j7Rt-bm1zEncizXJ3dTui8fsofcK0bLvlHE0lSeLvXJD8TbTL_TBlC8N4MsAb-Xsmo7rbutFMhPGz7Zu1icKFttkf4AuYGCc3GnNFz2s-CTEs7qzEWx2OtnXhqDEOp4YxTYw6BHjw8eDodadyMiy9zIJjImQUvPVMSgVJ1ANCYqH8za8kX1IZ7LqTjw26Zn4GcFeVcEQCOYCjcVLs-fRCD7kOv3zdF598AqlD26iXeAd3Y-XWDELRrw5RaPy3alRGp6NWhQkFFpD0xHCQ1blyPpkMGCfV9Ul5kaYrIEUSmbeQq_liQw_jX3vNmlVCOTUJPU0Ylly9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RsALJRQwsPp41pNQUzq33B7dHFCJJEPzAPlOlEnIXVY-T6nqIXLZzl3fUBQxkcgWSK1nQhGIFrrindTZkkMyfoEnuzgv_UT-66S95fxNCv1oVmhqFiIj5xbRNHwdGfyCoaKZ5lK59_QwuvNGaQd0Jn7M5eJ3dEl4naWlVE-7dOzyFQmKrhzUE9Mx1wMgB44DcCRzx5JttpRzypWQPXr552MkCtIKnpv53ZNwdWY1UkKzBTOhOPjZe5T3RW4rAQi5vhZYcLeW1lURIgyvOFXUBRTa9x7JM5DOJOW996t9KG_wJ0FxDqItGTflZSh72FOAUnOtytDM5GoxJGLFpfCzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
