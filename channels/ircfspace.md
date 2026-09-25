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
<img src="https://cdn1.telesco.pe/file/unmQiele21cBvw_TyF2j-tNYjXsfKS7pS6XaMNgwSwLHU1F2-gDD8ze3KsNmxgousFDRTa9Y_P0zP--gRcKfn9f9l6hwRuYecMBcd10BrUq8l4zzIjIGvwtqAaVvJKI-ReJRgLTpXxgaH2H0VYatE6hXc_s5ecX1XhyIPQu--BQIUjwj7KoZG7UqrWJLdCEUkOVO9P8GcNLhpvuHBXi1TbUsKSEoa3lp1eF_-VoASlIL-gdIVfmsaTBEVTTFRTjibTPPVJ4YHue756X77m5taqdDn9bys3-Z9lxd7UyugKT269hqxPGPrPlx1VQPcMrayiGC7kPELe0rYaClnFBbIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 03:12:51</div>
<hr>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/inv8QrjBIX1qOYg_ybBDL4wymqf1msOaoApXYSTVf9DD7YDVLTzalDzhiIs4bF4CVQsfQSE8m30-Fon1FS8EiFHl_TAybYLoQf_EzpWHgur6UKBkovArEJl7tJ39Q6Ev25HN6g4NVU3TICEc-qR5b8on-VhtD203RboXAvm0KpUSIqKhzYe9V8v5VrXO_DtreYUItaZagcfPwcBD4zFcgBj6JiFd0BV5-S1GR30JRP8VqOC2E-t5ejTZ4zjXc9KQpsxQ--lAcM8V1KhIMtrpZHmyCWoXCMS3wfuksU98xb_wS64hNc26CGhzVs4TvcYpaL6ZU9ZiMR4O5Oz3HA33JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gctrwgwV1aFHmGeqnOKurlIihgQDJzpI0yO_S7bAWQGvgN4sN2wKpmIecWP7lBALa6rSFOZLA4CS5GzKqwByG_E51KEO48z3kU2jLZ90KqRwM2fb7DQiOyBDaxvGwj5V2EYbOqZrFbpjMJOfP_WP0C08zYMmwH1b6hU0XnvcvM1u0MMmshBtW-7Gr3JlJjBhBE4WfyawtA_24LvOnaLh-TlUAM--7CjxT09cU4bCITvRWHXX41Aqbgvp4N6GXIsYXtx8ZbpA0mwTZe7UimMvrlDa5AkPMj6MBIkKNZnW1SSFX3wnbJTs-PEADYGJ5gBgWmtSdmN2FzM2T-cpFzY76Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j29My_LfYn8bqsMRhtu8IJ2JcBCfjM6iXhVOwyJsAe3_27zsHwEYJbQIbBzq_lYIN4o4mBhxHzfx83Sm66mDvofbR4Mfun6kwwhKXuu3nDaLqSl6CFPoudrq1aD7qfC2lJjAY0f-1owKiKHCAsSzPc2b_u7blMWoam1gWFODgfGY5XWEg34RD8pywkpjHv0_FFaRJInBGqh0qggqMcS8rUCmJ92cKf5Golk4fH0nmUYqMWq3k90SYC39DmHDMqiZw3qqhg0KsP5K5Rx4nHfDP9qYF3tSWKTsJ2AeqDxgLDbjOlbCTa5Bw9BxAGNQx71wcBXpDgc03hrMyy8wKLKZww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OmVmHxMMk5zLrudc3ZLKS0eKf3E9XEnXPLafbbE-1rFVpwISB0g4kl7QAhIqYpieiwBxd30A8SfnrtO9YDWn-6UySZedPaWMDwKkM3bmsZjHjHLmo0zl_MArri7FCxhasvrVaMx5cZADmYEGTlmJCVgHjW1o23dxPwpVzdlWU229edp1AiLcHqA9A9hJiBT5kWqdnNV3jpd08Jipv_WgNtXTpLN4kIB8RDVuaiV2UTSiSlqIloMO0lHRrYT42pyrPjkAwgA4KlHvO424xz6IlP6zysUWrYjIZNelg4PViYz-7BT2w_Ych4OruY5pfmF465eTWin0UsAHYfQO0Sg6Qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FOK9V68qDi6NWc9PoSpJEpIJ10RemqLOjzsTETV0TGoCDKqB1JWsk2s6Fpn8GiFHLpiovb7fj7ti9H-iM7PofqaDtY0dSmjSqHvW_UvYNdP8MbTcAM4QVPPUvC2GcYKZCQ_3wfTXZ9zQ_2uZ2PMMzbuB2QuseomXA1ZAD44J7dlGWuUzvie-tp9id4j074qGzhL7Z5v25UU3DcORlCIz__kul-CfLJDTyrDLfKGRHFpOYh69KqIU75PGJlMYNKebsMN5mFQLQdfWERagm8zsjl04PzWXjitwmHgw-l-c-t6NZ9KtdO6EfM7MI4Ee2Cyq9wiPZ3rNlkCtiUfXsvAGaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xv9UVw4_4hD46pPM8fV_7k1Al9DxjRCRlhAxq4kjLPw0XLu2s0zbrvV55uXgUCitRxk1ODVZf8yjEMbHekW8DQbZVN2CRnz4-X81Tg_yFGIrQf0p9vbqdBkPE6ersxlo8w8doKvIWQ-iBEXC2JaMHRhnA_1jREBDaOh_SMIWw-FtDGEQe_pPLoG9sz-WRamoQ4A2z5DW1DQwKkrEHzuo9CgtjJfzt0zbAmxgMqKrUFpT9s62LKTrgtSgX_saRL591MMcLPl0z1yy0nIu4hgJjIV9v31VrxUM-d4dUmi5iHvK2YChkd_qns4w0Z-7JQxaRvApQyw_KnJQ3csowOAIbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hcaQ6JaVaRRw4aF9as8GsMkKfN7dH-WYFlopRQaX2BTjyzEOsaR5ozvOV1pMid3qXkm8FR9sb_Q4i4k58xmtuz3GpPrjcVM-WuGdGYSyCBAaVV1EMTkr7TVgZwQHz82kbD994kTf1IIrRDpeTT2NoHx-bSsMOUAip_uPYJbylVT6trKjedikVEdwukSHB_YrNF9xLMxxIaRADm2GrCZ3ieh2uOl0CLotduiIctKfFJloiBBz1z0n6-wMHjkA9OXU9MtPREAESEZQd5qd8BZPf36U1Fhh2m8pZ7GFWpBh3gB-Xd5U8fPn-m2SNWoT26eqCY0MZNiUFmZGbP5vtT5eDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WsUeGoFlg2t-pcrKuW4YYt0TwxA2bh1DHChXMXx-vNS_a8-HylEyC7olzik-E4IQ91B89GWDBaGs2yXNPdlJT4-8J--9JfqU489LUmnJ7koTl7uS4wKAkzEPvOPxnjQST4W8RYVuB5bDQDCmpEkU_ea5izzM7te-QL29bhxoXDNGSM88njQn5vNSBADxCYTl6f1OO3S_sbZzZtuPMRz6wLtgqeZpy8cbFrzCsHHAGgd0bTcBvNSknWe2M8WkCtj6g8T4vVOWGVydd4tLZq-npWJWLHAarFsDbnhBmXLqAvQsN7bVG2K9UJoZDYU5RnhHMzmEwNz36fAU3l5BACXC-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J8effj64dEdCKfQIz-pwKn_5r3aPJb6zmcPUuxdzxXsxNJ-siQUlFJTkxq58dPQpg16rX_KVdzABEunPXqcHtm6RQyP9QobvsifykqSxCix5l4GLWXMAMtBzvHx8zh-TLyaBxpZjC4yjP-M2MWaptrKLqu5Z446DPstopFvrf5qnui_folUrfuHu3pOtj-X5by-G4Dj7pKTEQTMtPCXtvLMDjd17LPcbqwoOajIf7Ku_3khYJn9ZiUQNiY6HWNf9xQKlR2u5yMvZRBcW4idHO2OfLg_AT3LK-sEdZAcuCrfdQEQZau0MQVGj5VoXB3B4U8RcOUR9KMrTctJjLBx3TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WzYvQOIIuA1g8oxA7wuVMJnB2WFnpDNvUfidnEOokqKhyzwI7Tq1wLLJtMDzLPGSJqH3x2xFaiCHlecZrzAF8hGYTCY5EJe2IyFBnZjmiXudGfHqGGzetxg-B9qeQp5ugCP8Ac9LUTDviJnjUsYAdmRFSG0Fl3TlMs1xWgygh1N-usifcWcaQQW_NPqFufyHia3rqurWiSFhenM8bDgNMi6tLhfoZDpiKnAYjUK29ufNLeioX9UH9dZXlKu7lPT8y1Ipukm57pmh-HkGt06XUrp-G8Ql-VMOqgqhOAPumBmCvUcwsWuxvw-WthotyaicNDUMKEUUWi2Czu1DQKra2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nY03Hb5AGNZ4Uac1WD1ABT57xE3Xql5Imntijvnov6zwVkPfxZbUgjRYeKa-fDwJI-qhCSsHQCV7MRJqA9dx_UsmSq9SZBrdXoOsVS3-lS9KeETxjDbAbkcKg-GHapAf_HgM3cUeSW0Rxn_HmQ_D7m8QZh-IvLSy1Z6DLcL4McA6gz8xzlWixoJnSZ3ZYyFbFcWdNe3s9omnHiG-bUSf_SFVZqwBr3Ueyo4zjTUwT0vEP383syaRmZZJf-uNBfRpgvl5JsD_ZRtB74KTc2jsGOfMP98xMuM97rNJdwSNDSSL80nJam20ZtD8BURt97zSr9U0VwnJW_h6c4FBHAKD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F38iB5B0Gcmj1Zq-RZjAtFrFHGp0ylQkljS2eZ9XIoRq8sVv78-uxmf7pqkxo0X9p0OfwrcU7ddthvvCHDz8wUanG-M8OST_bGRnq05zEylQ49lN63nydFzRHLxego4wrZCnHA2HM3S_kCKzF08pUf6UD4Ten1MWLnidWdhyGvNNDpKHvo9IwK82TY-yB-N9pYf2EeP9Fo2Yftil2VbXedng6zul7ss2J0DhBO9yAJjEtgbrMz9ikBZS5gydV3D2-vNxKoJcgZ3DdiYwMf3me-oFqsupoCEsl-nt4Cl2BVC-x0484Da75gmAgo_mfrvt1aX3NHJ7HxKUdZtF8HJeRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KnnP1cVUfYPZ8OM0HWk4zxHQhCaGwizZ3upzq2aGe9KbaXaDWnvc-f0bXg-UkOPTVVIaQJ7KZnkxvcD9kChsFuw4pyWpszoCXH8EB2bWAjX97kUh8RW72Uzd7x4raskl-PNcitmkRIyKHJVxXOULoanbDy8igkgmxLl6xANQOkFH8T5Usz8SvK1THZd3gi-01FJkc7DDiW3APNEr09xNNfX2jwMNbZ_aibzGqcuNrQrKqqpGkJZk0UwHivl7_gqhu830yW5YMBpkOAoYnzeuM7Fr8Hp_6JD4pQs7eDrhwcSBxzOOonRsbG4boVVMBVUY_1QMVxnlvHzg0aQb2HPCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XDxbJtync81pFTsWjMQpTNi0Xx27rZh1iPgBopgE_8NMVl7nesO9vNl5qjhrXvGZK1BbfcqAGchtsbIkolXNsl1WQc1d-y9VUJlSCw8V9-QPEOAWSDIZ9v6jzWddX9MTjIOWuJUeeY6pgUmVkT55O0LGjvombVEtTtXVYq4P4OPVRGxU3rPZ3b0ClpfH_n6Zgkwk1yY6_KTHVGbytdPL9aZQHhSSf6hFfyWkshyFHhADo8xDxzg5EoDLKYmNSkOiIEn0MtSvEN-zk-hZo1GyglufQSg7wgNsZ0KtYvRF-Bl4GJnSSMfNk0lRkbL1L_Lopgz_3jT3m6K9k_oTfV4e-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XtFUMIAuL0fjcIx5OYhHEhiM2y7C8tkDFrvAM8IUWxdRlhgrKgZgu_Q-Gnxb1c4czXqsgFPTZHXslXFsTl3S5XQhtuitUxCQku6cY9EJKkxEoTe16CuUlxFmwPmuMB3fHajzkURBYkNgh_qpZdi_vr_Jp3jTVBM7R_Kv-UWjTts-2jpQbg2cOZPm6Hb4WvOXp0nDufC8UpO9zP_FhIGTt_GhB6THrlHXANBfhLgPOLhNntWlx8f_hraIhfFWoo6AcnnnBkSmHC0_4KGL-vbKFOtsXXqOGJzCVSrw3uOu-gr6vrvS1ofnS4PC7WSr53R7m57Q-leRGK74KGN9tp8i8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DZAbnX1oTQz7EnN2ClsdvOohY7Iv19K2p4JB44JrHpssZ-L-sbLU8R5tr2twpUT6wI8mOaZIEumBISO--bKZelxodc0jvyQXPn4FLDEmz1WEjF-SKapLxy9WW45uQT-7Ok2qvdyrBtlYFhJa1h9jg28oL61nFdgYaX_4Ibqf1fcoYCyZ7E-rAUMtNKozBp5A3kKL7YLrtdyMdW9wxHcB047z2bDa08mbDdtV3f4Njn9pl6g4Au36D9tqaNEdMxQKL7gKw_MhrZyUXLl6oUif-WTfDqXgPIK_ggRedpbBn95K_DKJps55RrWvtX4Z-R8BdWge9lHRIGB97spq--fX-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UO8TmZbpj1Y2D5vTIB3fc9ujdQo9CIJmVmrnVu6wCpIQSBCln0Uf2uACOn0CQP-lk9tdcjvCYMhYlcy5fr63a8kfEs9KYZU8VIK4EnfZkreo3t3ZL5q01dUppYkwKd41EndHQqEFIN6cPvwLvjZzhUjrwLy-SIbDoUKRuViYUv4hLoK78XkvyZIZSRVw3dn8fUmzWMVjofwY-y43EvWjUw0pO4vEDqRj6rpOf2nHIdp7cERJH9I9xX1d3poLpm2WabgP0spI1jEvif7hqk4faCNvqVs8XTftPmWzIJZvc3o2XJAIdG7hxnp8ah3DlA3Jmn-sHlF3BZStDURlBDXZRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZyXhYya48rEWzBhnicf8Qvta4FmSuwdhUgKfo7kTs4aiGKdPyJIuuWQC43BcI60h5SCn8zWlpflceIZSQC24XShoUhUn6YpGgzRBMjC708_NvnFf6lq4naQDEXNwlDnAC55WBBnHMgEW52AKNkiGcB1umqhaTBuWXds2Z4B8YGgvpBEutInQRkG7BRV7d6J6iEKiFiy5T4Cg6_7rARCeLloJ82pJrWKxKgMCx1HMkUdrLNy1ymGHKD1UuLLaPdneKeg-3IgBwXJSq3hk9t_7rOw2K1wSM6hAE8aorYS2ZP4qU_l1DYsl_Li-7T5dmFJ_Oi5tn2Df5QcD9wwEuHSmVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PVrrnnC9_6kYuqtOqshhYhCWg_VkRGdM62S8an4J9knDMTG3hPTC5WgSh-oZGJZZT4-d2g4F4AhFD_vXOOpA7YzTgVSkczOeGzXJ3JhSbuXWzx_7m4W-IQxPbxHoZRn1eaVgJF-vCOkzlk3wCmbcVinBildwkwWyJ4hV49qQFYWVlpFf3fmkxbtBFGLlhIjGjHTIgSlvLoYOu-P83tzw7PbqNQukxuxGwa4rcpvIGnobMZCEXrWpfSyut_jbg8rGy0VgKri8RwgYfmKaJIJ-v6Sn4RcW9z4ERtTxHEoQWAz7rQMhXGpjgVy6X0-z7_5lzohBRGxurAH2PHXz2mXrEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ODqToUuYyB-07SmaI1ArsdDskfR9pr0gjdV8JHc3dQBMA7dvvTUxEGgFUDFPVuFr61gUU2k4IQvBaaYSRWEgHu1bfqET_PikM2YfC3li0wJiMjThdPNcIUp7TQW0yK1ALnK5yQv9uxsYzRsFJfjh9gn-LkR0jOSb9KWom-G_abealzS-yU8MxwlzMWOr88I9OlOkmdE3y7VAe7OqbOl0SA8YQbKAELJd-8JPjyHRRoYIyOhE5Ct2CyYT-tJ0slsL-dgUIjcWqXklMxzJeIJiHacK8UATpaXtjJpxetjSfBI70kOTJ-QVUz-WaNthFof-LI1I_ba13DrQz-81F-HBqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S0xFLDG-mz1MkbxQkxRudpi8_RC-n-88GCkVRhhGWCyATGdGRGR98D6FDzVck2gf9DPH3UYMzNMsysxgkoqe3a-s_MzU3xASqwpxWPaZTx8zSiFO9bgdRcbcWhBLyR__zB3b48kDpmE6hJBNDrUneEvuqAlF42JuP7NP8MJstcHu4S0nzfsZVdr2pqQY_fOXY8e1NxmY-Q4CxmrW1nF2J8C6nveRmbhc5Q80BxfL1_Mo5OCd5rl1Jo8T-dHFUgVPENh7xc97wZncn6Fgi8sAf20xUKnNg2OkF8m4ir94xrNwKeylcarTpWsVBfk5LQmjdC5zIQbCM4oeSg_UeqyixA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HL_2BjLmtufq-Z4ZzOUMoP6jpueBY5vX3iX6IWlcYzK6DtPZMJYX6RaMR60BoHlNORKMPtII8k6pmf2Yd_tc4RLaFb5AZmGTZzixAuefVj439P8Ic2p00VxQjTU7YdtcjOqEL7bx8XfEQX-Ey2_YQ2-u4NqJpZTg-_0qRYuAVSUTdL5lAHoj-72gO1Iyu4e5gjF2CUrGiaIMTVYMQK55VegaHnJzfvk9bKDtpu-gZbuJdqGgXgutCLz-mPbvDtzC1BtckMN1kjh8PAIhGZdQZppF932_SUVu4M0DCBwGeoVSbExOSm3B75NQVuNHi0OIbEPOSco6Le4do77ooIgsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jxwqMod6G_m5l6RWOW9-RsZ5vAXICFphAQMFpvEhFwJefpd6smXWD8353J69eX9YLSIbC5_YP312aJ3JKVbahFeejvyOmq0JgxDRGYSPafp7xXH9yXfg8rm41FHe0TZCS39LlrYHvwRutK2tt8zbo6PiHKJ0d06WkyHeeNjvSMcI14rDca9vawVeeZup-1gV6dcsPnfCypL7wCIlBB4VX4vYlsNtjVenojYZCLfzUS2zb-BCdOJKzDMYYYjLXU6bwIrNNfLjxEz8d1D7rDAf6aZrHS36LvvfX2D6P5Ih9NQXpyvlMQ99hZ8CoiHZ3PGdcYzodiPv42kg3ubzBA8EiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XDAV3CgpduX_B5n14o5hPhkLGL9K2tTDRJ-Cv88KGm6XoDCU9mbkTLZNMEw28UqUAVbZ7ovRgp1YhGAUA-P_A49kKn6lIxP3fjPhbaMcY_uUIPx2-CsZ_bGdJz_yoBrTq9OFtLLm20d9WCfiFLWUQA5ObhGFA1sCEi7PJ1s3KhlbVXmwMFyotkVSLnYKwNQAWgVcqM5udX_0ko9H4hVviZTM5s76IgcM2ZtGJiJkpMS-kVTZH4grruf2T90jgLiMEschycHGYot2qggYqRN0OD1wkMREJitCSFXvHqD8IQUZnySB06SQwDWI6KtakDAPGB0ZbXSSOIdU3LBj5i6dLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b8R1B3pH8rw5MND8twhxNMGWtbxigHWAOexsVucHij3DyTPHRZzBZO5Ykohfm94DpJOmvH0yDPJSf7fFsCgWusIb5lEx-R0SGgdF1rtu4gkMPO5m6q7drJqbOikID-9NYcQ0tghAyTTwN5_yiguSi1wWK9Gy_pph5JzcYn_gkSZopJR1Zj-cB7KmSGnR8oCAoyjdrzA_w49UU0U9IqLqmSzPX0ILD5j7hg7bv9fvf4o9lK5T0ozE79oLoK0aTMdmuE9ESrLiYCbm-0Om2ORt3GJK_ATVIlsVEslgI22OTb-0-Dnv0YxFnKmjMjOQeLXG4WG9mkBopdrr-scUvA19qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/endThbY3IEiCLYem-ebBvrGyxUZr9FBWAaWy1xKy7ncnR5ZXMFNGZgtR75Do-MYiDaL3Ok8bhIU6sURmAwmV90CTqnfFRjnxb7ljB5R6LMQYvYX8wpEsCcX484WsnmFvQoKtbEvfKEg-DZbK_IVKZ0wz7FtGr30MZB_s7ul_C4VeRPBzfnaw8iMRoQ4QqkZ-O21VAa5akPiOhQNdFBCQblaPwqqYWkdbXpEoPS0KeJZ_Woj-qKsGdqCguD8g2v9eW2tY9ZmOESvYBkxEF9QH-WrcxyhPk8HECaWvvxsbee23qceyBVTWf4nO26LSvmgHPOae0st-O-7IzZHKStgFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GYCEnPej9-OtA80a__yjUSAAyWhLGBNBXXezDA5nFQZQv452OXbOolNGDkoxdCW1-uY-NwTthaCrprowPRmxUbIWBu_v3UiykbfJ6ArsmGZlbExwAV4Em__1IInlm2366sgPmX7SlIg2gQjXSVNWnSrA_ZYhboNzGYRWexdsF-5lhhLgT7-daYK12PeCPJBsLO5XuJYyn4_rojnF2i_KfUasznC3hnENq4rJgumA6cvDN1jsU-2lqnSNtiot-uvdAgRwQxxTpV0r7SHMlFmrl8tXJzxHdlI4Cc8BymUHGdQyyjMCkLO7J-WDvaY898E51x-qf-ke56Eu2uNyb-qjhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qI2l6PygM7LUkbREwzmSy6_VIS8qGp0JHtffct-3dec9SPxlE67NN2_jYRYfTGEt6pXR9jKrYIDMIsTxTVvisc2JDYqxdEIhi_Ue3rfvH59bjTQWoLnJaXPfO0IjFFnFB_lOVBZYw0Ozgo-1vx4E5gIbztR3blr2C0cdR8XjEZewDN2uYRWQXPH64JYc-i3DkYGC98X4fYl1qe1NsOe9rTH34TzvsK1gZuLZ4HAIsQo_0Q2HwJlZYcMgUZhEuwi2PvjwZj4xLR2HhXuFBdX5tQcWlZMw7PWuqVLJex_k16SWC7BVROOkJJE4Kelr4o079tCu0pwOTPpaFw1wPQ_r1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iBPhIqo9BzxuzWonUK8soYc3wRmdkbNBZ5_SeIvFEDUxxRn2m9Yjx6pj_m6iGBGgXIIJLhpsfafGGAhAz37SJnX2iebhDVD2Kfhx4miOQEeX9QE6MlsHSnEH__485bJTQ1rXTFPmYJd80HnBfUvAmeTck9IBy65PHpOTAAp-3deuOTMXH0ofSCs4TsN09xNHvoJGvL6Z83kdO3gPDZ8oiZgagG6W6dtl4cbdNz2tYsBZHUKqiywGgP4-Bw13TScDNJ9FueaBlFKFdSAmAF9AM66Sa48-bhyu-p4ap3-_KW832ybcvP7h7O7S7jPOVT59pLIHIwKyFhiW61TNfT5nnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YmQJO7cmwQBoD1CA7Ut5RwpUDb8Sd2W9wQ9xieafKdPFCIiXpBNf7COms3Fb8OO4W3PtXgRlJcNgFJojFf6gtymda1UUsHTDAa6qa4RZ8i90pROJCS8GkCOs3PnX3PuyLEV5S0OJHuKEKVlYQ_zMvtpgvdomyPTnwP_RCde593A4qKLT8wHPMjPJjM6WzgJ5SzpYb_ieinZ9XkT8oroHIb57fqhpDmxtwTUSmYUOZ6RCzf2k0MUa820BQ9LwQ9N6s5OiVCMEQzYV0sbbTJgovEaTgCjCEwrzNVxfTsUb2Sk6z2PslrExedoK6z1eauO9rmfUeyH69zRurzmfIoE_5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v09WyjamqoRIo3QEa95Cy8G8mRIkAW-anNK09CH6v_kEqbjnGFqP6UXHTyJ5zU4bsND8AJ-zI8RtyPlLkLZL-OMNekUoMUKr8sR3ocFylWJRWUPLjPhLgr_QLTvGwgXRCVojjs8-Xkoshkv7YLqe3IUtRp7d1I3lteWGd2vEBQkSvvpvqLZ2NMmPyzdU9LfwUFyouzEsBf1j09FvzOeJ2a8nlvvRwiqT_BHmOV8ZI78s4CHsEv8ezEDiGmlN_dHRvC2v5UGX6xNWHSA11mRieepPiU4D_VAxQtmfPt53w01s14hoToqM0Pyj1JtwzzzXFsU4AQzo7XoAHkStAWmwWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/htYF-wW2KeUpLTmFa6O1Brh7HkFNKgaIIlR94XQKrCaI3zZmk8PRScdxxLANmUOMVSWsv26E0BurdjRGyepwloYMH1tJOxbo268vGn2SmI_J9zZg-YmSxgNsgJnmx5AFuOb1Lb4sB-MOFpdoDhkGdxDWdsXPdlnYjVfrNgUPvpnvzt1R-6coS5_l2L2rAiDt7EGbUuevcL1-rjulBUmO23C9NUIV9Jd2UFvWS9QRuNwcT99bHFgDpeKNd1wR_5OMI8x2TC7auw2hNRC6cZwU3zOTFw65FxicEvfMWpTMzy7xq9V2U5cxBgEobwKKXMVr0xebjIw3SecHcAXLti9-nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MWN6sjUKPeeRHraiUqlHxDm31UdDWk9YwbStWXigKsFcA4Z2PcQPrfFLjqbH_cEn2txHUeEdjIGz2eA3FFGbOkK13EGdjlqd3TaELly4mlHWs8OpDpKDmRDbK6iGEVUvEzfwMwqIYRmcL1AI6YnVHHsWlg-9ew1HbfFwYN3f8lbEfe43pYlD25-RaH18eMHrTXfGeml6SLimfBdYqOMYkH9GM0c2suFHj4QdSZZ0c6dbQrIfQjyC0vV1vljsdPA5mjhMeLg1nJZXJuu5cfG8y6_HhTbo5-UK0i8Ilbth1Hb9VdB_17osXPtxYPWbZDvpwwaVrc77AZdJYwbhTtA1rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/amsEBYflxFnkW0yEQnphwxPVRo907igBbY_-wiMuETC4IW4NGkYpzyedN03dJPOjcm3AW5iq5x5cTkhxcteLeP47kxEfTZupJ9GYquWPcS_3TbtL8Au1K2Wc6jXuLlSaNsDar3gb0CwXTXoyzfk_SJKBZs1xztCpcB6cC3AOnZg65L55DjMXTK_MY7ZJf_Fpnx4oeBZtMrjU0EqKbsWfG04zQNgMdlR488ktZLCni9OMhJwQUfIjvaHhxIZ1_WUL7dIG2nGdDpKzRdjViAmwTcZLhNulnLHqS3rMl9dTapNeBI8QwAQqQStOqsXQEEiMJh4eK2bPOdsLg-ckc8hMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tSWpOt78SB2zFPzIO1k8vafVyGilz27rQqoypDdI8hbmZCK-JMQF6vE__ACo9p-czrIMsCygohDpOJnDMs3DUHOYp0PoXAfH0HmA5TftWurubjk_h1zLPSjh8EWTG4QCIEah1wEG99QgCpomk1y63_RU1gGEoWv3VWFQeajwq1SK-qzVYt8Ir6L4to8DHV-6YTdUlnJQp4gsII7gANv13VdpLn8mAVbatEGe6Rsu7_terdhkSGlU_jEb1wntFdcht5sPi21r1EoRVeN9j5_EVNf1ZSICkNBnSYMrPG3FP-mBXOpAshUMPrAWylZYvXLZwrAhcYfXyNQd0li0v7r8hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8ammKxvBILNcr8PHrdzGGrLlCubtHaGk2J-CF-37_f690TDw7vcJt0NDvgm81UAUBwEbj4uzZEn03xCmz5cYvXYRA7pDJsV-Lz27JP0SfgfFc5rDkZotTaJypLFBHEFceyUseOXAO-s3ZhIru4gc0DZlkR2fvjvtcayUsu6hK_H22PBpigZ5iqcarBIfKfK22-B1kSaJadoQjNkfMfbk4blqcvs9FXA1-NkBDYYcortw9X7s_TK1MIQe0e9JTtPrvZ8zQC_szrR3yFSGf7OhKURYAlSXPqY8BSGTjdDPNqslqZgUegr7zpvJMQzGdk3Op0aZTQ28fLXxq_9ZIMp_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j5kE6aummBS0EPsBY-4dJbaRr-Mj1ueomGVlxTzFXxYQitiVRzJTnoaNRnznWj2IhHcz6j7fa_SwIoyTby94qqI66QYumOImdC7x6Nndrj6B0N8sEzkcHU5dDCH-73rjMJrylkcprqF5SQgq1sj3IALuo0ggtiG2iMTLE7dh1FfPhHvZ0UjVlIa0D4NpWHArugyD5OYgWl8iboX8vMtDAA24C_13paOkuCOdDFIufCDu-pMt_sXB0v_SUKIbYjzlWzyR-eJJ2aZZjbjjEbXu8tUJdjleBLz1aunltPJu74hvo92jwq3KqDqV7THtiX_RhLhXT5xV3dAoVzYzxbOS6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cKNC-u7duTb9BhEXd1BkeqT4iL8aFqMGCifit5yP6Ft2ck0cZsS4lK8vE33mCQ5QyRbmRpUDRuuUji1BckemJDNeu1FS-O4BCvXRfvRJuSPAUpUm4-uo8qx39L5BkLGiA8opVfkgpsabBqFn88w98wFfBc0ua16q3LqnZOwg_5g5WPNamUbrzaZH6qY-eBNtl1cX7wsHpYSLsocv6P3KU1MbTwjox_DikzCWi3tBc7egJoycUo0EpgbUidYAoUNbWF_ZnapZsqukR51qjNPbHbikmrgW2sklXFcZq4YS5P6zD16dm89KpD5XriM66v7c5eW6PZHbUNgLXobEwnNR1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X1UnVeppBRPbDQ4DDvzQVUyj7n9Lw7rcj3Dtp8hwSsSLRu-UKbqeQ8e5pXXwH1Bu6JRKbHyqUhZFPoabCZI5vtfbsnT-58TEvLsgkJ1aloI1C_fJHIbiNbaXLNECNvY54JCx-3Kp-02UUOrUP7Z0Dgnd5G32cuOuVwtAR0_EUlD2EhEp7bbVVJGz_kGfu-902wgIlK5Z3_XokOWdf9kixkNrHQoCU_cvUX7DyO5Bk7hWL_Cg9hPwk9srO0kDTLRjemGpmTwA5Umq5_eKlt49nhn1o3Plk0DmJupoSCRnLi346kIZTS-I7FhFot25HoUjzPE06i2qzHYIJkF58czOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VM-xhCDBDC8fy0JyViTluv07rkB3K--0GiMKjclFQomU7miyAoZzynfdgKMBWS2Ue5uixSslQhJxPGxvD0_toCYrppK66bqvGjNRuf4dKfY0ut7wvGSs-jh6JhZ7pgslx7pfAc8wWed8E4sQgS6lhLgeGuFnQ0enfPBqGumKb583q35Gzat9aSCMBzwVtWuICtGHDNqI9wa1PM5V4iRfoHh3QJGHWZL9rXrDv5XfJTCQ8Bsq007EKql4hD61bqf8emDpU_ki28l5wwVafOc2x-qIYDBYLsDaHqlOeYbM8uJB2P6yFc7ogyUhkklA5JO428Iqq98N8aC9e92lTlBeJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYOcxSPBIj8KBBWYMqKDrtdm7mfzzv0WioFRhfD61Uy7ThzVTi7DfM1bd8L-yM72gO1CUYbS1AkrHeN4iNS7jM2Bct-3ac1Dso1lNecma_GaaKzdAD4Kw3GDH6QwI7W8z64kWrbcgwG5N6FgnkMENF0EmiLPlhz_uomWE1D0Yd0cgvvcML5s9FmUO7SP8NTdWRunIZ3_HwEki6iD5o6D4i7nOTc-tdBuyiRDIHNxZ9oGCklv24Qiu5k4Me4Ei83ZRbsMPX0z2dVHWayXvhbr6evKWZ5GWBwJnuug5IsgSQENVv6aLwU0LVfFg5bmGBQaLTDn4g6TT07fRuhaXUcHrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uhrbuVEgREuCg1Sm2BkDn5NlrZ1oZ1RwtsjYOYRRCD9i3Qct1VcgxucRM_9wQDCMtZkxx8FU0C_eYVjoEsiB8zOFC6omkrqcJkF4pbCmYo8cMZdcxwaHEiYvt8h2tdU__ZHzGmSDMq7gWsrWlpsiLtTtsNczphlEpQB2BIlS4BQqiCUxmjE5htSYdmjn9QL-TozFKT7-_qoaQ56F4FF-FEQumUp7Zb6pfakfBFQPLn--_fFCI9YczzWdji1UJgyJUuhqs7gU993UPTRuEnci4Pr-u_P9YiaMfOcI9rASj1OFXsOdF_ktnnKHveX0UZI847h1n278fV8CLJiYupsQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YEmHVcpjpqlKVfA7lG4zFbNMOrSe4vd_w07EbXTmDtWytOoK_mHUjfoVbX9nqHq5lZFOsB0UQg0gi7TOyOUn6nAFj0rRNvvmJ85A8B6kYbDoPaO1nZAzXBWmjFxBV2X7nA2TjnSAS_ii9tL8TeLM2TAYdLrbng_hBi4ALvxSS-jVNMSK-eOaxTar_56Xv-SllB7aX3YyuHwP2BMhyqAUzyZxMJ93atD9mMlNduzjDXsOVyE350VYrtvAfBZSHeYZPhnE_AFuA7jTjEe3NsHo3S7eVg4vWJiWGk9Llmy_GUMqjc1kUXrj9h9WF4tbYMXwa9UC_opRInzZnEEmm2DdWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eJpVcwWOR8-vSN_jOi65ZG0s61Fl_X85fAj26_gFJEL0NZ_tBpdWMHFKNGKdhfUGm1AEnRUAM7hVZJR7jQrVKARfGSswD9ER7dkGe07AaI9GjGfTtVloIXcoDis0mpj-05JqmIrOYE5if9V7d37dl6DZxQpLisyh9fD-iz541t6_jS0Afjh1FrcNQQAow2es41hP5wF7_NL8_iqlcuSkwBkz6OVIEGkAKLlFaM4Re1y5ff689xt-tv6KxxBDpn_wejn4fqnRv-XOvyPtc1Gvgr1p5jSN6CtQpQaHNuDJgUOUeFVQy0jFBHlhgivLZr0VGExh9QFByGKHpxXrmbP5QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fax76ShZTjI3DpqttCttHVd0vAzL2YJmOMCxaxTj0z9-OG-cauJqxDx0w3xwFlr3W8xGrrelgNYEC0AvarRm4B6yPraUbuPvsx6IGsURi5bWi9efMnT0GkM0OYFJ5796DjWHiDbFkwdGb_lYH-stSXVzreHeFCqjN-ZFDVH4otYkSXxdqihFB1rxujbn12RUY66LKbBYLYyMUmBrofHNyvbbYKsLs6MSCVTUyBhWEXuww-Cep37D0yWOeRckiXQAK2t9jIXDdQ5Yvf_yuAdhWpDNOv7cchtyyhmzITHUT1RlSwUAVcD-r4Um_1APu_SO0WFqOSc9DowQvsgtlT77_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GEdTickSpc3uOlUaN-cyVKI4fZEXMd-Eq8ZXMXpx0cf_EOlkb9xDjp7nfE5Vx03ayU3DWD62Dobp0B_wzU4fvf2cxPhSHUz_d1TNJ_sc9XgbIKcHWmJ1h0s2nzBw3g5lHRgcPT0DERvOvAtxIinONRYkSCw5jsFYukQg4Dx4Em7W5f7sXyzBG0rnEhioUHiUTf-UXxLQuaWlinU4fA1HC2job_p1AuGbiCxFr3TOpbw_RaKUzj05EJ95ziO8Ds3QXsADP8wzUCDuP1IxhLHyyUDgNT8Yt6SekifELa-sbK0B-c-Hdu9TknWGkM6GaKAQNVx7Yo1Wc2ySKrmn04PtsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ffxia37o8eBekarOdo43S-ZLI-4krHnjf36-LexKj8g3xafWUpL3UcItE7tigWC2zHYdiEapPt8ODmBb-XNZrhwoqioH28-NgTXKs7rm88iYGLB5Pp2wGiSV4zhkvDvihPaSywQE1Ja7GhiT4mXAQF1wKJKqaxNP54WSZM-di6DZGl-jtmMcjqret630wvV8Qyf0dc7caAHYq2ka1hKLaxy8avBKpRmxR_N5qKmX6zOwiClPIeOWyfCnMGMmjA8lPjVEgzpLVVafLxUPN_El0-xLYKbDOXSkA7OsrH9hzuBp7jZ_QgWofOTmuA-Z8F6Go1QKOKRoPnxBbdvP6V0gZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aHz2ZhbFNilrL4wG67hOCJE4wVOWYxaiUFVid7XU6fyLydcuVqFwoP2MbmqImYeiUJXBdOwtV8O7JF11MKerqgzMly_FqhhPfwxiX3ftsIi-t1YulwVPF6gVXYvbMtFeNLOWIS_OYxULkqCkQV1ecpVyhwzScLJHyElSil3_Fbw1Gl79psHMOhqke4boMDP256bVPCMrCR3Re39MM8kwbH0_UL2TzoBd-ByxD6wT-KSdpE42c7JWv_OB1dDAJM8efiZSOYXdoEfsgxqWpu8RVpBPXW9Z_0Q6n5ipGhkn0gLeIJAyHWGUGfXAgNmIG746_93pjFo2YV7Au8aeQGkiew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U5LoN1lsx7IjLHSwiY5k1wglxYG6yIFvnAqxtDcH3hP6FsPG0IqEgulNeqKEA4ATrhRxaSP2g6b7SjRur57tnqY5kXDmviWXifn-SK7Qv16dwhjU8GWfZIsBT2wdLmRR2J8EtuKRdNaeTE4E2D8AkuHJ1a8fRfxnQ8iM7i8zFgKYttHmHFlU3a5Sw9Ec-XXoz6ARi_sMh8XjGfUemvScQLSu3XNAAgH_dJHEVrd5F-B4qpUVxDOmsvEuVNejt0oDbyzWsQj0_kaN1b3A85WH2rQb39m9Fv-hSvGNoD3LzoppWJN7FrFzBy16L-tj7I9Krm2376rGOENivbCMk7k0zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=bOnP8aOl2wBextQkGrp0uOYieWVwsjxuWhj8NFeniSBUCSECY2XoUahKogYnJDpZydPXN45EAUgq3O5tQQqvcSjJxqLz_qE_6wJZ5beTusGfGgKoDcdVqgMSALCyOPEtvN9VAjxs1ytiLRB4pnvBa2oEg0yQNh8PFWqbFttampNq6uzMXf3ddmbwi2FSJx6rhdJglOl7YJcU4DCiQFjCDwOBPUHi4nLmjJxzneDgGmPg0Tejk6sq8grQwU0sJMABSA5gJX6YRBPPwbeZh_coLU_KNzHyBcoglyGKLN52gciDUY4dTg4UbluQw29ny6O_8KqAlEXsskksA28U7ts0iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=bOnP8aOl2wBextQkGrp0uOYieWVwsjxuWhj8NFeniSBUCSECY2XoUahKogYnJDpZydPXN45EAUgq3O5tQQqvcSjJxqLz_qE_6wJZ5beTusGfGgKoDcdVqgMSALCyOPEtvN9VAjxs1ytiLRB4pnvBa2oEg0yQNh8PFWqbFttampNq6uzMXf3ddmbwi2FSJx6rhdJglOl7YJcU4DCiQFjCDwOBPUHi4nLmjJxzneDgGmPg0Tejk6sq8grQwU0sJMABSA5gJX6YRBPPwbeZh_coLU_KNzHyBcoglyGKLN52gciDUY4dTg4UbluQw29ny6O_8KqAlEXsskksA28U7ts0iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kT3aCA48Hrhk2nzKk3ipsDyolpcqKt1YUjdrUVTHbtKqZ0TeVAxSubXv2o24EhfodB4PdYK_COQyILFs5D9VFHd3LnqI2ktuYoV1BtbjNkbeF6O9CZV3qPQeaRh77cMwVKL59FDVtRfAsh8KkWQ7mGB73dae9GoQuGH7LRVVCmQeVic4_0schA_GCH-zCJQKfmktIIHLt9Ps8VTzewcgK6bYi-ceOu_V47fhIexG5c8tuoFEkaM9UqTFyEimJ0LXgElj6BQVQs0Wx9szTzMrzogwsNI-hIX-KetdOEP50A7xETVtuHS4azFKjW3AeYa2knz9TCy3PS4XLlrh1k1Q5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m4O7XvEJZ9yib8uWiFrzb14aE7gTQfFMya75t1ySAFuIKDqdlJtmEWNl1pU-YekLyEpqZ815bD2TeiTJDfVyRuyYSTdEQ5FzIqX3Kf-wdIgNqAwksNgUgkBPYHdA_-1iBHfedjDRkFj1oPF-yXPC9rAGHK5hZToSH0PpgBqGN5xehk3DU7PFbOggoRSWpGqsn4o3d6ibmgnVQZHWu5-WpsknnNuXepKNHrAlxD9q43tOhruLWXoccdYJSOEZHWtjS87NMIGAFhOvEn-MBUslUEgD6tCxZPr7wiTKlJc-asYiK7gWHeyZRjHL_QFJ13JjJYJ5tpIyu8bGwL5orYYS_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TGBglTcduiZ_ymV786vL7dsO0Ak2eeEUtd0WFDZK8ujOMj51YuyggnaiHiVjWMvcsrxzalA-hnZyOo16bjzge8f3c7-lSpzCRoxDEYOk0nZU88Tt_7ERpuLe0uLS25r-a77VHiVsQ9sfcWI2aOVyQ62dPtxCsOVz7HLUZFLZASI5zHuKShqSJSfH2SfjCRt7m5pyQSwqEhf1IXWq_i__R9wbj75b6KoMRO5OKJe5FGykljRluS3-vv-_d7egDWNTrO4zPKcFHebJKzMd3EY69VmUZEzf5xHnsCdyHDl_uVmPH7GXDWGV6xbObgjN-KAfnGI0AjQRmabGZ4njtDX19g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y_WEwwkf2nnymQRQoANG8bCLNP7U3kUcL9ItlnEVLfLIJJbGz9tk4gzILCHGbgNaMMwjs3K2WMNpZkCJoj8MVLXLPvAkpDZpTUP2Ue7ZfbotsP1Jc286Fq1LdrwDICLQObRIMHBoiEA_EO6MV4VC2Tw1y6kIa6cdRbLNBT3_U_C6C-M75Fb8mXMxYqIE8pW5qgx6dBDGdq29uPcp0y89WDYnXUdbzL6jjnqp2tfuDSSdapNJLG2mYrKbSxzqSxT2AycPup9jCZITPyiImkJWmm139rPL-F9z_3NqgtmLmOjcGkWldZD66AbeII0-rCojSYtlwKpNt8Wv-JjytrQ-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HNhlLp7C3Sl1RllV8YjAUgiO7FuwuB1B-8Ly1JeG90NwJKitnmsWcrRczt2QYT0SjLgkgaUUo_f7XJyJxbdDf8HXzi6jlTvOtnW2_MeP5xWw18ZPD-HOx5U-sZbqsQo7NkuEJaP2O9KyDioLryi7zg8L3sUEhab2Y7nvVBD3gx3weGdS1Z6O0KREjNjOugwn_-MG05hwWdAJ1_LOnUxMQmha4umzmYR4SemXyYjdO1B3u8NJJ0qIm5E9w7Rq5cGTaU3s5A2mlx5l8l18pslQus2XkVDKBTbq5K8LpChvP1_bdBSVR6pqJWnmKM124f4y8i2DoXugATYP7RXtzIrFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a3W797AXeULNit7yDcM_wfdeHNcny_xq9cLWwmHrOZxFqg16MuBHfIVEMJVmVEqaiEFNb3Gnk0arS3Rc0vxLUNy4RTFqToSgBpHhHsO6Fo66uxNC-8ifUTL4bZPdGdI30RVtbPy9h9hXjsaFSsyN45-aLSxnxDf78mqRtGNi3etnrUtTMGp6w9eZajQOc7rLVGSKYtEGc4GQXxbDRlAT_5Yd01lrCbT4XkJ2jniJOcf1yZiR755WYtdoxzYBZ9vWWc6_AIbH3XJp6t7HD0En5oCxKJvQQOLAgM6vfyxLp6OxHAzj2qu9Y7RkdXQoX4fTZmHrNXQffNtkSHGgAaC-Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/InbIXswsNl8IEvUzgiw0WzSOSyhmWJ6POpnmI08mMUSNwz5UjYwcu5RiWvTdNXuRdV5ibM4z1WbKuubHN3rFAs5Sw4I-1NElQByTBWWBCGZ_ylH19Gvykwc_dv8Wxxw76vTmVJ0tP6JUqfnR9AENxJmNuFXXDhlo5Xm1q26l_71S4qJhCfn6p0Ge03fuyFe5TkxL33svQa97gCLcEPEzn7PInUAbF_szU85AxC0mZ0tkuc7JIdyAiQ0Xsmml9LtXyjYsYFwSB23YxOs_bFU4TS4dIXbyUh3qVscgQvgt1poURBeypVpq-8P_sQygFFJ1vznA5c-XAaJXeh2z6XhXLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqy8Tazzl4ufNLET_DP4iMEmnCCQrR2-BVOKeI_ksVQTaG-GrsQ_W0i9WJwCUmmqtFMz5ZBT5vgCAh-OO5jXVcmue2LZlrFbAJSy55-hwb13ExyZHluflGe4ZetY2AZHfKVDoJgX30Ps5RTt0N52Q4OjxkMxqZkU8CgF0LNiRWNEWEGRc6y3Cd_MF9YCjYrATVKA604x1CzK7ktYTk6DVsTicUGiKtov3UdjSOvxpvGrg-o4DCSBtfTs9-7BNBofiwlyxc-_4vpr66Rl8BNGnsnd9QpnsDBKfzBIBiugSN7Lqv7R9klXYXWkGMfTgzSNmWY9ZW57JCa59JdsEVR3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJyiH6cX_jfVjD3byOYldmXjiN-zRm3F-qfqaccUflovLt5ZcEStSOeoJKLWhX39wGYut4gCdnt_Buj8NDRr-7w5kOndKcsIj3DqE6LREDrEOGxWHYwgdoXaNJQ9-9wp9BpTVnd3DPBhfDSvdCiSoZAMIfSJuE9YSAT6Djjg9Ph2Xr-Z_uxRnz47Hb6fAkM-guRmovjXqxFv7cYhVI54y7umxI0Hb17t9OmJ2I2hi3c8o9BhZD039YFc7-K3aCCwP-fQkgNdrB08yoEaRCSRJJHE-4YbHEmQuclXZgnatW9wepm8tJA1GNJ2ijgk8nDK7K5JZzb9wMOGv1Auugjj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UERdYnRq5nU9uZhpJKj9mSVigdrjx8wcekIAEixM_TYaRCS2sPP4FLuved44KBClrichLkS9Up97O5zxiOnK7dniexujv50auI2oOZpnr6seRT5vdmgq762Ff4L2v1y_ZgrcpT8iRq830HGy8HfesCZa5BwP6sdGI6fXmOql0tx48iUGizY8MH25cCz3OnfE3eEsOAPN4zZCUOZWJEI4T9v5vmlHzWrhHLwZijoQs99SB0zLYHZkPrY--BbYwctDKjOUDz0hLvrBMcD8PUrKnPga6YrIFfB0QN2xRevD0jQ345uvxzXYeQayyvDRLNtRBFVfpxqal6mIXcLCRqKvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYvG3tn7sCRtDauygtO3N7hYA8qAI5A9lOs3CyPeaByHDCCBmhtEwJ0Tdha2uWq9wpW_09BXiVzFLPN5-G8Sa7-ztefNHiuQlbIyQBVTGHZVBI1w02dOUW8Ndn9uw-_xLD56YTc05R87A3C59-WtMV5YFMadNUbn3fckvjzgswm3Riw85swSjRqnpnl2fyLTWDgCPuQ2IDtc_YCK4CDOlo240fUYiUlvAXbkQG8PbvWhh8VXkT_YLXnbSbX4vUyQMx0OsJhy32EtSUcOylCZQ7aYetyJ7xnCKFP_KQI6esaqnn_siKDG1cxonX5TDVHLhHv1E0Eo6-wZcU2jGklnhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qc7GumPYiVhSojuBlU5KsS-lL6xEi5n1UxtPKuRvCxW0ircI9b0eKfjS1S4BN8wUsRGAWYhL7JBilMZhG_oubIw_P3ObdkVY7OD3qgQJnqjoOTtadPYCjlzH14zqJQwjathJuVpyrLwvpBqOFqd-taHEES82WyYhnLkAUpM7fyAChqI9lNa1qMwrCqPUadwmIPPK3g32Cf_jBUsvjNFNVrLxeHEP-I7bTBZ3SkQ7_vnNyLINY4lB4iZdpSFsO9MpkAORfQVA7QECtk-BrLfWkiJl7LcqCZ-GzeNRZ5OtvSy8fbXgdMHDIcDTgXfefOEUd1g6KaAF-jDY4vzqt2oOQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iShg1TNt1IMkFUWCU-9k2PSXi6L2s6RVs1IGIp-SEsYOEKwaI-5_uGeEfQFsnLrVb_VwR5pFNVO7N4zs-RJ7KqamKvcsQmWNNWt8f4MTv1TkjuWg8TZlOyXcLEcNY5fwmu0ifwC4sMEMXVIYAJAWFu5VxXNREueAnR7DCsHi3YyYfBz17dRnBylRpiiLni3OrnxW7iisRKP8KTGtlpQwKKt4YAXLN2TtEZ5BwB45U6kg6lFiqCxiSJjMs9qUeeR8GszfQJHwlmPAbzRCEVckI4Sfcq0em3PJ_E-e-VZo3Ou3KrspyO_IVSrZpKVOFIrY_h9oxzgyz-eC3x7cmOGQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zafc_-Kv5xORVBVDhZrYb44kUSdaBE2T3w03saMv-xNfJixIiKVVO9SAxbQRM2rjybKKM26HyXcNFhJ5hiAvPJa1FD3JXHEDPBtvEAdQgnO2nntKUhzVYMTivzI-w8pSnF2kN6lyF5qOeYHtXrmOQi41oaGG3E9R2NVqeD5gGLWF8vu4fnXlSOlC6M0I7Xl-vbbbcv-fqnb3RV9HLnS4GwWDrIC8IUN3arBCKkZMA0RfGOcWJhu4LUDEmKWNlDp9Hylxnnf8lgAt5JwkKEeJRpPlEks3SOf1ocFlVuTUuf4nyz0jr1q5BEQScPKYUuxT6Yu3eclrWEOY5wexhfQ2iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q_cATyJ7UzdOzeFi7UVM-kwY3SHVpbcMvzonqhXzXmlh77WCdwb232gF31n-pDAxohLnJlxHBT5znV7nE07Ar7nETFHZSa3Y1U3mRXWKzLXvMfcOHkKdiMkjrHTx2fuVM9ERZWKfIFai-1w_cdcl_QEAqzFk7Th4-Bhqc5gX901lC7YhCf2EXs5xmvmE0x2ciIBklMWQaSWAw4wybUJF2264ZV0smI_BgKmSAlWojEOHEeD5l5-_sAYDXCj2zAhx_EMlJNB22Z2OITVW42dL5ZMpYYzMWWE6FLRd9i_rZvqWQW7Ry0RhBy1EY1boLFmEWgtil7aGQlZ6C9lE69RrnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zagm_plAMIotSddEGhDqte9Q4tHI4jKYzajM3kxYnZVSzR1SFzLRaTGI3OnxOuJKnRZPvWIvrpgDQnzTaAGrK79x-9S027wPwn6ngELk7qYwb0wyEoC4bl01tIapRfj1jtOxFudV0uI_EwDXhKeNcnogvI49e7rZtCPrqSmQgll8e6j55Dfs74m4OeoWX_p_tYCZRB6sZl4JVjEdJyG6GjTx_jR0tUjvTo1Vc1CnEerTl0xzvk5CSqK0E_No9eqGWwz9WzRbBkAs8lUtXJx_0zkvt4eYRRSL_NBuhwlxIYcn-O2kzl_EX37RDIYuuWFmv95U4icq0D3uCrDtmsXwbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uzjO6eSSef-Cfz9GRe13DTsijDdJ9Dt4V8lkE1qnGNoRlqlGAHuD6YziIOvkHyumnCq3hWHWdzO_Uyr1uwP7RxJ0fFsmTRa_kZY1Ps1pmSlOOrqq7cw_edeQyvVRuxk2G1EwGBeQx02_1JeMiBFDNtOo4jhbK1gxrch5AORgoUXZddaw3pm_zgR_MpAVC6R8K4ujHVqch4WA1OUj2gRnmzCxFgFlcIuNwrx4_GYV_HCr9f27jT840WegHdYyxItfBERw_Z4vfBTE6DJRvSapOjP55sifsjIwkIxuh2_WtIEZ8b4yK4NaFJjiAz5EqXlyMZLwh6tR8O9C4BJzO1bJig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EJbBD2_3L-Zn2dMb6uE6_RSh5jLm7Zs0sdv7pW1Jnm_ORun3iRC49mWCXEHRIijUjPeLyhlkZWCSfjn07OPQOZemcFmMh__PhVgSPxKq-zgHKtMd1KxDDQvSdqA-g48rheXiJqfbm0I5bBQipmxzv2HiWtvL2IbBmIuRfSbOhWH3KU9XEz9O6sU8Q11YtTCrxL4IoBYZ7AXO-aMtJUGJi22vFqJyYK3WJ3cKjETSynGCCMFBl7brzglF9Pf2N2RsueS1HQ1IZhoZJuZcNtQpJ7tHlj_LwT6HOa0QxzOU2Ft7p-G-sCWHwgJDYrgSDau0ArCdNX5IPVIAQQBAXDfhoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ui9B_1pqG9rTIKgwuadAkhQ23qJv4b5x22Enyvbk6HdxrjeCW6gpHwwbGwjQSZvAbqSmBDlqxdCFyAhrgCHWa9Cwt_ZAtzEh18QFXm4o4Tv2I_OGuPO2lz8Mt12Wlv4gl2NR9-VkbJ5j9OeBRbO1GEoYDiRiAg5LU-1XWusQzd_ZBAnsp9zhouBj131aSZB2reIAi6SPGZVZ0lZ8BZYUC1mNpuVpF-ORJCbKTZzYaypzwWCAMOkt7kvBpNnbF9IY1n3dw12Fhde5MFobkoIyhPQxVRuUPX9F8xyJ8hUgvQocaIghM_hE1A4b7FxyidnlQpO9rTIka1Q7jmYnrCvkEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L-AgFUZK-5aE-nZJ3_MU0u3NuGQiqTKd44zdqcVufJeZG60X7XgxkuTtBHR_-7cdgZ9rb7Eneua82bW-Rz4WA0hFswGua5HqoTVmsoqbMSyQh9-ASldmc_8xuJP3jg7PKCWUS-kDXw1OjJmbjNpT8MzTVEYuhWeUFOXRzXdnR4eQCQvVJK1gmLZgYb3ZmYf1JMS9TJEZqdWNPa5r_QEhD2o8FUS741ZtP1nYklc24RjKb_2snMgc6jO5vKlsYPEO8eWDXrH4QUQqhTri9gLHi3xqm9xe5CVXp3xa8ojcBdfBnagypvyhDGRFRPIpheOKgqXh4BzXNtQSdL-go5t_3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hwpgCLJSyLeziVXy8laj-HHXcT3PRtDQS49-Ba_FmqJtrykzW9yI97jzFuZDP0EPqCqI0Cxb4haPbAf_zhOEMFTGZvI-lGltSdxc7Vg_0KUaM5pUAPCBnr54STAV1xj-mpgaJeu2MVVm9cRvExOPSQN6W-Sdk4SNsSJHvWog1C2WUKPOSoPX-LgZ6SS0WxvzjoAKJ83mxWt-9mQlrDzxyc_TvNWxg-nKUoLuS1CEmhiLZWiDLxMv0o7cpDpUuPpBsCtaEUCueY3ux3vH1oH_C17v3Oy1xxyA1Wghm-AJ07N1k9TpFfUb5qLQaAVBE2xEU1yeEt4u9Ap7Txu2_tFNSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oic6Bw5iOBECmcwj0sNIlhZUCjgYseSp56MDptryND_3ntTxglcZYzjFmF1O_RmUh4QbiUJ1tpkhPY6Q7qqty3vkOBr5VX3mLtvw85UeMZyuz6rZWvht6EkjVGlPw1LQ7BH5hK5WRqYIuVZhC66stbBAX_ssiDU0ZwCRA8P-g1GokoxhbEY3ZtbDzLqDjmGikzgdPrYQBvZVMwjA0Qc4VLxQYM8BTWoWBh0wguz4UwAXARu0YLnDT7eL9rwmFX4fatGe3vX-KN6cr94WXIWJ87WcKM7Un3UxRMmuKU89248-csbAZn2BEM7Ou17DByzka09bRhiMaDpjXtKFEeKSXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uG3ggjaetGu9U0BK4oXnhFujKr2E8SQneBCZJasUMAEEV1cJRJrZocUiQu9IOGED9W9yuxNUvY2qv9ntikL-PUcViHgtibnZKKcIJpIy9dd60unykJqgB1bkFyCo4coGAYgwkFfE1c6orPgePwdgWUVI-Tsmc2AVN62V9q4jNTLdZC4jxpBXi9ih71Ad_5hs8AA-Hnunryqrt4lKkddlGJ12V0bg29lkfQz63uSr6b5F-d_guPW1hD2p2tlDDhQiza69AKIqOVAoztdk2Ygi5Fp3TGF4UhdkypbchvDF5Y9h6HtdR0Eo7ts0BuEI7sLGDRYChROHm2LgDfhMRxM0uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RuqyUwmxkMdMB-jd1gt9wR0aff3YvNTJ5vq56xiGaDbnFwgbV7kvCgXyXMnVPFN9lSPT2jR2AfFql85LfXLQNtfTfo7lLUWeF41Zbr01f5XlVuIjppYXktQwPdYJeDkxhR-OMu6s2IOsbxia01sFtU2jtQzYIy-O4wUUrdpcf1ifISb844KYahc8Pi61arpR-136lug8CaAD1GmTSE9aXLryJH4LZzQrrC23S68cHReNf9Vr5LfyaolLGCSU4FU7iQ_RP6nMum5w-CQx0YluiHLl9NWvuA-kIKsawu7JEuOMV2_q_aspje1IJ2N4V0tDSujIoOd_c46-LsibtDmBjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NVpv5JVV4qPSPsVkVr0oQAOqk1M_PBNhY5FK1184BfRMIGsp-ZePLIZcGEWTbl7xzjHckfu8hGvHLid1EkaIrBR-xbXcRGWBe-AZx_Qf0eZmeS4R0x-WP4vjPFJ8K1ixSUUrg5xUtoi2pNbGil4J5N4MmgCcapD4W-EmqobTgjVA38QavaKLFghwZUJgRZWyNWK2MKuRSe3eiE_QS0ifWFisXIbUSXmb4xQOJEJoEY9vX3ec2LmP5d6JFhBQBsH5kZc7BfPmMIanndHDYIu0iPuB5Gw0o4ExYdKyupfgUaxiG-7XmlQ04eLItcV8HlGdwx8Z6uEw_zwvGUANPBXrhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kFM6c-ydX_tHB6qWDBsCcBBFBDEuNY7nPm2EEhorz0o24E3vi2eLw1Ys-XpZLeawHS82Mpk2pMpqTqpFg5X4lbUqFka72jCcZFsG_xFixWBTj_8gp1h0DoxCy6yrvMVPZr2Wtcl0JPJxVOgQmH2FRd04PCgibY_MPd8XHDQ0cNAf2kAly1FfWAsRkYEtZmHQa_NuwomPjuMVYl1TRcmN4cyYyOYP1gW5cd2kRvaa9BJyH7SvCpM6tQDkIssp_akESLXfEV1B31lxxhKtaydhB2vSy_NBoqm51-_MygtuDBclrNlMOj3JvqyPaCBWc2LsyRMIzH2ezOEVvAmwloP_EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EBDNQIc1dg83Ln7iL_Pwgcif7s_r6jsRaPwHBBgWwtJjkGciSIBkUAuY2aT7Pdj8s5FkzV1ifDjCELC3BmQvq9uABA289-Xkbjj_47PMGtIdGHTsmQd1vp76kCZQfst91pqaqqMogp9uHF6F4SVD46Lmu7n2Dq7U9y-bwSLqydZyb5yaf-teA9HdidOjQppopnydbrh7IozcBhkc-m1ogztZEnMwDSCS_-HGxPwfHINKKdmomdyfi9AI0gBDiDxPkplyU74EWVhZvS6N4KL5s6d-aqbeOCJeHamtPNhusKoLVN75WXe5o18gN7NsUIcqz-0ss-YvGq_du-dCbYOPoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GAVXdPpwfc4kOmP6iqJUMGm16fiWm3bli9fv6E3kB1Tl6iIhvNVQ_60twLW1G-cSYBP0U7fb0fBPwVME4Zcrl2Ggb_57bVALZXsjwC3UOrP6swKvRGM1CvbhskRljyFgxGHnIR7SFW3WWn7iYQmP3K1IjOgHvsdHxRgFgHZD0RcEKqz8zdbscGBG18rwTn92iFa1eC2Q6hOSMCqsOzEiULs04YSpHRyyWIJ2JxrApfbkc2aqnQJUNXBbdXrGwa3OJPBTlN1myUwgON2xBbYAQoohdPy92jQxUWpm9xlDwhoKL9E-0ujFR6PVIMytf1LWT2pF-aP7eQVRrlU9SbJqIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lt7GTy-rg8cLqG0nYwg0pvTO4-bMYF0rTUStgH7HC9Blz0ulENW7OAULzauKREsTSnQM6rwKNcIlaCIrExEotJj-1NSw73l7duiGNM63fSdFcqHN3hBLKIjXhcVKW44vEMGsOosyXnntY6TupvVBfbulbYdDSN5MgI4togRioBOauxd2Ziw4v0OuHBco65cR4boefJUiQ62uzJ8V0x-UzkigxxhwvPSCNRZb1znzm2Lm7FqULZ2zi0xRvV2VukeWcHm7dJttNmXa2X-UXylg9rm0tyaPPoT-atOdv8bbKULveJcXM2Ww0G-X_WtTEOi3EnNqoAu823-r1GH_Axo2hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
