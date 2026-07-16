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
<img src="https://cdn4.telesco.pe/file/nxOSqF6MzDnUKIhKnHivr2272bdGx28iIT8wj0212QsFFG5ynhpYVWTyLba7WcZFMOcJn6LBkcyq2jSBgyHDKH8p0YH65oyUUNQtVHZw7CrV5VNhIzphEM05AqEPHlHooxIJZAnHU2N6QBts9wCqiBaEIm77UsLl2oWu0IM5y5vf8tLZw0QwFbDMcBeH3Kaj2MxbBxABA8N_neN0URIp1bsZIwk0VJs6CzbeJcmYUk9wWuCyPkvm0GymA2na0HFI038eKB2vaOCPhW-rI6tst9JwIoNvP4l82OMUgtv52nYv5k4jGuZf1t5iDZ-VU-S-OC2pDksYDGz3FVHJErWqxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.3K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 04:26:11</div>
<hr>

<div class="tg-post" id="msg-18811">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">منوچهر متکی:  باید برویم پایگاه های آمریکایی ها در منطقه را تصرف کنیم و بعدش صد نفر از سربازان شان را اسیر کنیم بیاوریم ایران!</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/SBoxxx/18811" target="_blank">📅 03:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18810">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: ایران یک شهروند  امریکایی را آزاد کرد، متشکرم!!
«ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در دوران «ریاست‌جمهوری» جو بایدن خواب‌آلود به‌طور ناعادلانه بازداشت شده بود، اجازه داد تا آن کشور را ترک کند. او اکنون در امنیت خارج از ایران و در شرایط خوبی است. ایالات متحده آمریکا از این اقدامِ مبتنی بر حسن نیت ایران قدردانی می‌کند!»</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/SBoxxx/18810" target="_blank">📅 02:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18809">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کما اینکه خراب کردن چیزی خیلی ساده تر از ساختن آن است.</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SBoxxx/18809" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18808">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ونس :   با توجه به سهولت هدف قرار دادن کشتی ها با پهپادهای ارزان قیمت، امنیت ناوبری به تنهایی با استفاده از ابزار نظامی بسیار دشوار است.</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SBoxxx/18808" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18807">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ونس :
با توجه به سهولت هدف قرار دادن کشتی ها با پهپادهای ارزان قیمت، امنیت ناوبری به تنهایی با استفاده از ابزار نظامی بسیار دشوار است.</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SBoxxx/18807" target="_blank">📅 02:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18806">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مجلس نمایندگان ایالات متحده با قاطعیت پیشنهادی مبنی بر قطع ۳.۳ میلیارد دلار کمک نظامی به اسرائیل را رد کرد (۳۱۴ به ۱۰۴).</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SBoxxx/18806" target="_blank">📅 02:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18805">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">7 جوان ارتشی پرپر شده در حمله دیشب آمریکا به سیستان و بلوچستان!</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/18805" target="_blank">📅 01:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18804">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIZB2B6Sn9d1s7-wj6HWAmLf1ubraiuuZpOX8KBPdOrhUgEEJfUc4EEi97-16YSiHYuNgVIkpgn2oYPw2MNfVlYyZrzZwsYfggA8sylEcnZ_6gQh62CmMcYlU2mdP0QXTOsoXZ4UV4Z65XPa5i05IiC1ZF_KFss4kPMKagwrZXQCbU85cGCu0BtuhvEHPIUCAwEW9A1j7d159qyu11rM_ATkfEPQwNvQG8t8RI1fnlojl-HO0Y8gbJPdtSRgVz_2dj47izav9K9KpVABTK8Oih7Eha7Fqa0SYtqWL74yaIMZZ86ur5QjYo7McRy310u_mPSrVn_n-Y5YmTTofpvmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💙
💙
💙</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/18804" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18803">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جی دی ونس:  اگر من یک انسان باشم و با یک روح شرور روبرو شوم، شاید فکر کنم یک دیو است.</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/18803" target="_blank">📅 00:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18802">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جی دی ونس:
اگر من یک انسان باشم و با یک روح شرور روبرو شوم، شاید فکر کنم یک دیو است.</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/18802" target="_blank">📅 00:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18801">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
ایران به زودی شکست میخورد</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/18801" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18800">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آمریکا به عنوان «پاداش» حمایت از جنگ علیه ایران، به امارات متحده عربی دسترسی ممتاز به فناوری پیشرفته هوش مصنوعی اعطا کرد.
ابوظبی اکنون می‌تواند فناوری پیشرفته‌ای را خریداری کند که در دسترس هیچ کشور غرب آسیا، از جمله اسرائیل یا عربستان سعودی، نیست.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/18800" target="_blank">📅 23:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18799">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">محمد مرندی:
در همین حال، اردوغان همچنان نفت ارزان قیمت باکو را به شریک تجاری خود، نتانیاهو، منتقل می‌کند.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/18799" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18798">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دیدگاه ونس درباره اسرائیل:
من فراتر از کوچک‌ترین شک می‌دانم که افرادی در دولت اسرائیل وجود داشته‌اند که سعی در تغییر آن سیاست داشته‌اند زیرا می‌خواهند عملیات نظامی را ادامه دهند.
برخی افراد در سیستم آن‌ها، فراتر از کوچک‌ترین شک، وجود دارند که دستکاری کرده و سعی در تغییر افکار عمومی آمریکایی دارند تا جنگ را برای همیشه ادامه دهند.
دوباره، نه به سمت هیچ هدفی، بلکه فقط برای همیشه.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/18798" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18797">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حملات سنگین به اهواز !</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18797" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18796">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سنتکام:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات خود را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند. تنگه هرمز یک آبراه بین‌المللی حیاتی برای تجارت جهانی است.
ارتش ایالات متحده در حال محاسبه مسئولیت ایران است، طبق دستور رئیس ستاد فرماندهی.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18796" target="_blank">📅 22:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18795">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حمله ایران به اربیل</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/18795" target="_blank">📅 22:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18794">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قبلاً هم گفته ام که پیش‌زمینه سخنان دونالد ترامپ درباره «تهدید کمونیسم» را باید بیش از آنکه در واقعیت سیاسی امروز آمریکا جست‌وجو کرد، در ادبیات سیاسی محافظه‌کاران این کشور و تلاش او برای پیوند زدن خود با میراث رونالد ریگان دید. از منظر علوم سیاسی، کمونیسم…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/18794" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18793">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18793" target="_blank">📅 22:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18792">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم  باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم  محمدباقر قالیباف در بیاینه تبینی خطاب به مردم عزیز ایران:   این روزها که دوباره آتش…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18792" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18791">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قالیباف:
باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم
باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم
محمدباقر قالیباف در بیاینه تبینی خطاب
به مردم عزیز ایران:
این روزها که دوباره آتش جنگ شعله ورتر شده سوالاتی در بین مردم و گروه‌های مختلف پرسیده می‌شود و هرکس به فراخور نگاه خود به آن پاسخ می‌دهد. آیا ما به دنبال جنگ هستیم؟ آیا جنگ و سایه جنگ پایان می‌یابد؟ آیا با مذاکره می‌توانیم به اهداف خود برسیم؟ وقتی با آمریکای بدعهد طرفیم اساسا مذاکره چه فایده‌ای دارد؟ و در نهایت موضوع مهم این است که چگونه حق خود را بگیریم و پیروز این جنگ باشیم؟
اگر با نگاه منافع ملی، امنیت ملی و به‌دور از نگاه جناحی به این موضوع بنگریم می‌توانیم به پاسخ‌های صریح، روشن و دقیق دست پیدا کنیم. اول باید بدانیم ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است.
دوم، همان‌طور که قبلا نیز بارها گفته‌ام، آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست. پس نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد.
لذا راهی جز تکیه بر توان خود و قوی شدن نداریم.سوم، مقاومت یکپارچه ملت ایران و نیروهای مسلح ما، این نقشه شوم دشمن در جنگ  40روزه را باطل و آن‌ها را مجبور به درخواست آتش‌بس و انجام مذاکره کرد ولی حتماً راهبرد غلط آن‌ها را عوض نکرده است. آمریکا همیشه خوی استکباری دارد و هیچ‌گاه ایران قوی را نمی‌پذیرد.
با این فرض‌ها باید پاسخ سوالات بالا را داد.ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم. در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18791" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18790">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXDKCq6H0HNtMD2SbwsYZ4Nk5nCmaP_fwRWRS5RW219-5IqXCKbOmbsKPVIALYY5UTERxcNxniy9tNL41XQXmiLI6UErqcB2_Ih8IGbaSijifjq3NmSRtapqMttPcLc6291KsODxq-pkTNastuckvdI1h-O4AdQnAdihLj-lHQpNhmqkQc6LFs81ENcrrRjwuTg7tNd4wMZJMCt2k_pOWmQXojwTHRKnzPO89MpHARQw7wRhvbxcrROdU3RfdvdFVDzYGBpGvawghJ_cHbC1cO_FwLlwfswNEnrXKHcf0OUQxqxeZuG8v1wLhslFdrC7r2TUR7Q8jdsbfVyY7OY4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در آخرین افشای مالی سالانه خود گزارش داد که در سال ۲۰۲۵ حداقل ۱.۴ میلیارد دلار از کسب‌وکارهای مربوط به ارزهای دیجیتال و میم‌کوین‌ها درآمد داشته است. ارزهای دیجیتال به‌وضوح بزرگ‌ترین منبع درآمد او بوده‌اند.   این گزارش همچنین نشان داد که او ۲۶…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/18790" target="_blank">📅 20:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18789">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به گزارش یک مقام ایرانی ناشناس، ایران یک پیام خصوصی به جِی. دی. ونس، معاون رئیس‌جمهور، ارسال کرد و در آن، جارد کوشنر و استیو ویتکوف را به سوءاستفاده از اطلاعات محرمانه حاصل از مذاکرات بین آمریکا و ایران برای کسب منافع مالی و انتشار اطلاعات متهم کرد.
دولت ترامپ به صراحت این ادعا را رد کرد و این اتهامات را نادرست خواند.
منبع: Drop Site News</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/18789" target="_blank">📅 20:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18788">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gladUh9lHJxF3ZKF71rpKSfKk7J-C2fFjsKOR0wRZv7eXdXSJqR3FZQuBhLE8sUWW5JKFY1miPJnZDss1QBZeStSFHnqvZhufFYI_NDousR-VSWmqaItbWg1FrhJx5fataG4n83ORb_93DxRhIVWs6tplOri4EFN9OZJk8iKfnM-X5yZs5MselHKzQewKY1aVPmznj2Dpj3U_fjE6Q6JRCcw-xDVT4iqivzSQ5HGkNJotuPJzQcE5uuUpjU_ZqifE0BXSyKYrXFt6_O66fsbrzQqRVp5QM4QLYWXzvjIKakFteQkrAny7UqfqQp2Sv2LCKVdh_yp1DquANKDpllMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:   چندین انفجار در بمپور و چابهار شنیده شد، علت نامشخص است</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18788" target="_blank">📅 20:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18787">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUVxRe7lLSDJrs7Q84FneAgfaeQUUrCKl8SZRqQWXEBIYIZcfXmKXAQupydxG2P07N7a7QJrjI4e2P6gRln4vO1JkA47w28jhalDgdanGco_NTmbKBQ0FZzAesxnvhxu98w2nBBNiGVEVbW8fDXxLnrNE0I68iuVEjVM0eOYzR4UoS1RvKW9npYHTOT9GLlbLoTbwEffAMeMZ4VXHVhoPCjUqnR-SQo2wS1mu7PF9f4-RB6iv4P6otCN6WkLLQvP7nMmJrtsCaP_yL5ikWzN0XUH6eOtbsXIQFyR35Snld78yctJfIUNJeGhCWXWIWBRQM5L5g0ElmJ6F7ffhgUWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18787" target="_blank">📅 20:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18785">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حمله به کویت</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/18785" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18784">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک تبعه ترکیه مبتلا به اسکیزوفرنی در مرکز شهر درسدن تصادف کرد، اما هیچ‌کس را نکشت یا مجروح نکرد. پلیس آلمان به سمت او شلیک کرد و او اکنون در بازداشت به سر می‌برد.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18784" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18783">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مثل اینکه یمنی ها در باب المندب فعال شده اند.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/18783" target="_blank">📅 19:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18782">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">و از این جالب تر این است که نسل کشی یهودیان توسط نازیها در جنگ جهانی دوم به کلی الهام گرفته از نسل کشی ارمنی‌ها در جنگ جهانی اول توسط ترکان عثمانی بود.  اسناد بسیاری در این حوزه وجود دارد.  حالا نوه آن خونریزهای نسل کش آمده از خطر نسل کشی می‌گوید!</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/18782" target="_blank">📅 19:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18781">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران:
نیروهای مسلح جمهوری اسلامی ایران نشان داده‌اند که هرگونه تجاوز به خاک ایران، قطعاً با پاسخ متقابل مواجه خواهد شد.
در حال حاضر، برنامه‌ای برای مذاکره نداریم و تمرکز ما بر دفاع است.
موافقت‌نامه همکاری، مجموعه‌ای از تعهدات متقابل است و در صورت نقض این تعهدات توسط طرف دیگر، ما نیز از اجرای تعهدات خود خودداری خواهیم کرد.
این یک اصل است و در آینده نیز از همین مسیر پیروی خواهد شد.
منبع: تسنیم</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/18781" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18780">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و تا زمان انتشار گزارش PPI بعید است حرکت صعودی خاصی در طلا و دیگر دارایی های روبروی دلار داشته باشیم.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18780" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18779">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو روز یکشنبه به ایالات متحده سفر خواهد کرد و روز دوشنبه با ترامپ دیدار خواهد داشت..
روزنامه "هایوم" اسرائیل
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/18779" target="_blank">📅 18:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18778">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرنگار: آیا رئیس‌جمهور الشرع (جولانی) برای شما تعهداتی در مورد کمک به حزب‌الله در لبنان داد؟  ترامپ: بله، او این کار را کرد.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18778" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18777">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانال ۱۴ اسرائیل مدعی شد ترامپ و مقامات ارشد آمریکایی طرح عملیات گسترده‌ای در تهران و شهرهای بزرگ ایران را بررسی کردند و تصمیم بر گسترش آتش دارند.  تا پیش از این عملیات های نظامی محدود به اهدافی در جنوب ایران بود.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18777" target="_blank">📅 18:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18776">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6MF9iQM7hd7KWNJuucK2A2YbNaNZunnkVtk_g-IsvMthVGnXTiDnIPouSXZ1oEP-DYnXIoSuyDH02WQFfmekYAEPPVkWEpXyRi1gwcQvf2S-SWdBAr3Xt5H_un0QdOGx4aVGA9-vl4wHKcOK9kMocxOFy12NFl8vX35u2DrPDGgLoE2t2niquxpAUXrpP-LJhnWLp_cJU3R0qVnWRJuMVB2sISZcPLInDO2aOWwk4veMOAJ7fwvL2izGKIgiXbVZ5Ok-9rlujDT_R82scs28qgoo6kQBtpaxvK3VPTc38e37AKYja0hignPNuSl0zQmUcJdpT-xnSR2X6tAGg4k8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل مدعی شد ترامپ و مقامات ارشد آمریکایی طرح عملیات گسترده‌ای در تهران و شهرهای بزرگ ایران را بررسی کردند و تصمیم بر گسترش آتش دارند.
تا پیش از این عملیات های نظامی محدود به اهدافی در جنوب ایران بود.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18776" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18775">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به نظر می‌رسد حشدالشعبی هم …</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18775" target="_blank">📅 17:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18774">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18774" target="_blank">📅 17:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18773">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ولایتمدار، عضو کمیسیون امنیت ملی:
به‌زودی دولایه از مسئولان آمریکا و اسرائیل را قصاص می‌کنیم
مردم نیز خود را برای تحمل شرایط سخت آماده کنند</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18773" target="_blank">📅 17:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18771">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKEvu868P17te8DZZgBO3t9D2Uv7-alKzxrVJk8PDAXKN6gS6J_qnFZ0uU95YBP7GoHgFmb29eu0-m6oBdkPaTxls3UTtC3bHKjjsiEpK6c4f9Xl93DYpP2SzCCJwDfNIhtiu_3CI2Ia1VbK6QaCw8Q8QorGRcgQJunmvRObaWydUZsp4nm7aHrrUNgSRUJr7duwgyp5Fsyaamm_pQOmXAA2YXUBJO2eAUZ872r7Jv4m0cc67-HUS8BWyQL9UMlNkI3gL0aNZ8UJfC3utNtVpBOV5vnIkbsJdLcF2YMYBLQK3UcO3oiteZewcvgE2LkgcMUT0vgC5i3XRwdmP7vf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mffTS6ACCPmwVjdbWwUy_uaIfm7btQzHBsOdKlSdv2LdSMJs-_lQ5PfzEpDYXPhHaHnqLPc-X5XahzsPIKeXpF5ZpMX_Jm43SblZvyZPmZ5_02J3CjHYVsaxyi5N5Iptmx84eqD5QytX0SAN146QXK4sXWGDZvzrip2hf9ar5vChXyB5qp2jRXa_8iFuik1o_1wKwH6lyd7zIdt4P2dnnhh57Rf1PDDFKV_RcqO8yJT8tV7-kIeTRtI530aU-BcZwJPf0odcNz7YNboMGW_OMyylg_jIyEO11KqrL9GvTX_sSGy_szTRDFU_UIuwndqTWEd8IXo2wmAKjHlY7_cxDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لینک نشست امروز با نیما  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18771" target="_blank">📅 15:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18770">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIptvv7yifLH_y-NftoNnS83-e65MVqW2NM9UteEWpWOgn0hE7c_kVdKZnyaj4KG4MiQKWCPbVPMFEXDxE0a-Fi_gAbgvjzFMdxDVuwD4Tql798-NHTu-dFYs-2BXAqd412iL_gtK_H1Zn9bt4XVl231Bo3v9EhaG-J-sq5AGuP7PuFk93N-DRERzckwYPYrz7cGh0cg4n2mOMzMeNVfqQYMTjD41oVEb6lJmesXEpYImffqHo2vudieU7JSJMV1fji1DUYLN8N9W5bl9FPrcyxCmEa2OUJpU3uzYao55N7ENbN3vwpZFZv77NtRobrwdTWQ-B58Qsy1gR8iWic85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک
نشست امروز با نیما
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18770" target="_blank">📅 15:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18769">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qg2sOrtNienOxSmv2zm3sO1_EsiBi4SAJD8KmeHiHVw_sbLOte3Ggt02u1SYcYeX7rVHFDOHhflE3wPruf5av31MgHuMbbL723eypaortRJb0WHF_JVK54I6bmDyuJj7JYOZU0aHlyLQ5AjHyIVcNIZVpwQtUb7QDV1QUmyvvqsJo9HzL4qu1psmErHDK6OWyWeVA9RBm0PgHExOCLilf_mR9A157YVJye0dEhqN-D_3NTLeH23__k1RDCKNaZKTDKzbzE83dmVo0IJoHLMrE5qMJRsRqEe54GSYUMnZlEeH7_B8alfIzxx9w6HMWRtoUvaLzDSlgw_oKy5af8llAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خریدهای تسلیحاتی اشتباه ارمنستان — بخش ۱  این تحلیل توسط یک کارشناس نظامی روس نوشته شده و لزوما همه اش مورد تایید من نیست.  گفتن اینکه وضعیت استراتژیک ارمنستان نامطمئن است، دست کم گرفتن مشکل بزرگی است که ارمنستان با آن درگیر است. این کشور کوچک عملاً توسط دشمنان…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18769" target="_blank">📅 14:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجار در شیراز !</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18768" target="_blank">📅 13:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c67f12a39a.mp4?token=HxvCSyJRws5Wnlc2yKcxgbVGSzj66PoCUAX6f2tke5IE3xEjiej3lnMoAxYuHEm3mLZ7RycZfvziBwBXAv8N_kaBMxEiQSzUHIRjMYD_eh6St8ysnyu7MVSGWC54kJrMw9Y3pCRYgUvNPW2t-2mpm2rbkQmXuG74sw0aG0vN1fOeHHwlGEqrlbjMFbSSD2CeZPNXfKEckPGS-fUdmifQt1XrIVpufiSqc2-pjRH2mDh2h2Fnf9ulkQwkrjnO6_0-nhW8WoWvzYMxIbVKEIaRFbqj24hvMAUA387TwcgpduNiL7swyfwY4ETN6JEqxaO7dzhR12zNoP54YgIZaajQYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c67f12a39a.mp4?token=HxvCSyJRws5Wnlc2yKcxgbVGSzj66PoCUAX6f2tke5IE3xEjiej3lnMoAxYuHEm3mLZ7RycZfvziBwBXAv8N_kaBMxEiQSzUHIRjMYD_eh6St8ysnyu7MVSGWC54kJrMw9Y3pCRYgUvNPW2t-2mpm2rbkQmXuG74sw0aG0vN1fOeHHwlGEqrlbjMFbSSD2CeZPNXfKEckPGS-fUdmifQt1XrIVpufiSqc2-pjRH2mDh2h2Fnf9ulkQwkrjnO6_0-nhW8WoWvzYMxIbVKEIaRFbqj24hvMAUA387TwcgpduNiL7swyfwY4ETN6JEqxaO7dzhR12zNoP54YgIZaajQYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18767" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18766">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">منوچهر متکی:  باید برویم پایگاه های آمریکایی ها در منطقه را تصرف کنیم و بعدش صد نفر از سربازان شان را اسیر کنیم بیاوریم ایران!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18766" target="_blank">📅 13:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18765">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18765" target="_blank">📅 13:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18764">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aex-UDhtemjlqwA6JBodgiOdt-b-uDnjGqtjjK9J6R37RV0CZT9jbL07TcEyRqejZrFFa_LWHYmRmE72qQEaLat6svLBqOXiFWf4JGuVkN86RgYe41bVGlyIUxhz13sjqHy2ABOWMNZBBgcKxUZa4dQyC54n-nYadyiA3EAxCLG1lsakZc3CL3SnerkYuWg_HLvVBiNCF_RcjceVPMeBFeGhgrgADx28wLWquc_mBsDuCdNq580B-lr2puCDI2dmQSrEQkG_oKjL7lS07sA1Vky57BpXI6ShQH44yuD_YV9xw31Hi8wo17ROwOKVsDaq-owKnpji3gBp3RMUD9HXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جنجال شدید در بالکان به وجود آمده. پس از آنکه وزیر صربستانی، سِنیژانا پاونوویچ، گفت که اگر جای اسلوبودان میلوشوویچ بود، پاکسازی قومی در کوزوو را انجام می‌داد.  وزیر امور اداری و خودگردانی محلی، در یک مصاحبه تلویزیونی روز دوشنبه (شبکه تلویزیونی کوریر)، گفت:…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18764" target="_blank">📅 13:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18763">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک جنجال شدید در بالکان به وجود آمده. پس از آنکه وزیر صربستانی، سِنیژانا پاونوویچ، گفت که اگر جای اسلوبودان میلوشوویچ بود، پاکسازی قومی در کوزوو را انجام می‌داد.
وزیر امور اداری و خودگردانی محلی، در یک مصاحبه تلویزیونی روز دوشنبه (شبکه تلویزیونی کوریر)، گفت:
"اگر جای اسلوبودان میلوشوویچ بودم، در سال ۱۹۹۸، پاکسازی قومی را در کوزوو انجام می‌دادم. این سخت‌ترین بیانیه‌ای است که تا به حال بیان کرده‌ام."
وزیر کشور کوزوو، ژلال سوهلا، دیروز گفت:
"من تصمیمی را امضا کرده‌ام که بر اساس آن، سِنیژانا پاونوویچ، شخص ناخوشایند اعلام شده است. ورود او به کوزوو و عبور از خاک جمهوری کوزوو به طور دائم ممنوع خواهد بود."
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18763" target="_blank">📅 12:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18762">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دقیقاً چه مدل آمادگی مدنظر هست لطفاً قید بفرمایید.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18762" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18761">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18761" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18760">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">محمدجواد لاریجانی:
مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18760" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18759">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntYDpLnoRuT9oWhEVl63pLNa0ZLE5zBODXGLhkCFcKddP70HqsI_NAxLFpOioEEGB3nbmPh0be5OCijthu5VDK0I464Fbtz6HC_T4jzF6WKX3UWqEtqyxsnNZSFpHuCTgQQ8E1-tis1xaUQKX8Zq-8H-gIg5l4Mebh9scnSSFgV1ALBdbZIo9_DDEQzfmXseqpwcAqLWV-JY3lF0Hqr-ZyVYySYfb_f76UUcPh7Svav1XacJqEKyw-ZyC7oCwd8CdEJ2Ie2e3mNQcFMYwGyj_QZVUU58DFCvUwv8lumXGPBPXfLkdV9pgfpcBxGHM5k7V4P8AAAIxpyBf9Bn2Phb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و تا زمان انتشار گزارش PPI بعید است حرکت صعودی خاصی در طلا و دیگر دارایی های روبروی دلار داشته باشیم.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18759" target="_blank">📅 11:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18758">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔔
#دلار
تهران =
187,000
#تتر
(تومان) = 186,340</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18758" target="_blank">📅 11:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18757">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:
ما امشب به شدت به آن‌ها ضربه خواهیم زد، فردا شب به شدت به آن‌ها ضربه خواهیم زد، و شب بعد نیز به شدت به آن‌ها ضربه خواهیم زد.
و سپس، هفته آینده اوضاع برای آن‌ها واقعاً بد می‌شود زیرا هفته آینده نوبت نیروگاه‌ها و پل‌ها می‌رسد.
ما تمام نیروگاه‌ها و پل‌های آن‌ها را از کار می‌اندازیم.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18757" target="_blank">📅 02:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18756">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزارت امور خارجه آمریکا: وظایف مرزی و گمرکی درمسیر TRIPP  تحت کنترل ارمنستان باقی خواهد ماند.   وزارت امور خارجه ایالات متحده در مورد مقررات اتحادیه اقتصادی اوراسیا در مسیر TRIPP اعلام کرد، تمام وظایف امنیتی مرزی و گمرکی تحت کنترل ارمنستان باقی خواهد ماند.…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18756" target="_blank">📅 00:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18755">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ارمنستان به اظهارات ترکیه درباره « کریدور زنگزور» واکنش نشان داد و گفت کریدور بنام زنگزور وجود ندارد  وزیر مدیریت سرزمینی و زیرساخت‌های ارمنستان داوید هوداتیان در مصاحبه با «آرمن‌پرس» به اظهارات اخیر وزیر حمل‌ونقل و زیرساخت‌های ترکیه درباره اینکه به اصطلاح…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18755" target="_blank">📅 00:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18754">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فارس:
چندین انفجار در بمپور و چابهار شنیده شد، علت نامشخص است</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18754" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18753">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدیده‌بان سرمایه</strong></div>
<div class="tg-text">⚠️
۲ مجمع، ۲ شرکت، ۱ آدرس، ۱ سهامدار عمده: آقای زنوزی
📍
آدرس مجمع
#خبنیان
استان آذربایجان شرقی، شهر اسکو، دهستان شورکات جنوبی، روستای سرین‌دیزج، خیابان آزادی، جاده
تبریز - جزیره اسلامی
، پلاک ۰
📍
آدرس مجمع
#درپاد
استان آذربایجان شرقی، شهر اسکو، دهستان شورکات جنوبی، روستای سرین‌دیزج، خیابان آزادی، جاده
تبریز - جزیره اسلامی
، پلاک ۰
این دیگر «محل برگزاری مجمع» نیست؛ این یعنی بردن مجمع به جایی که هرچه کمتر دیده شود، بهتر.
🏛
شرکت بورسی قرار نیست مجمع عمومی را در نقطه‌ای برگزار کند که سهامدار برای رسیدن به آن، از شهر رد شود، به دهستان برسد و آخر سر در روستا دنبال حق مالکیتش بگردد. مجمع عمومی، عمومی است؛ نه جلسه خصوصی سهامدار عمده، نه مراسمی دور از دسترس برای خلوت کردن سالن.
🚧
وقتی آدرس مجمع از شهر عبور می‌کند و به دهستان و روستا می‌رسد، دیگر سخت است کسی باور کند هدف، تسهیل حضور سهامدار بوده. این مدل انتخاب محل، بیشتر از آنکه احترام به حق حضور باشد، شبیه مهندسی غیبت است؛ یعنی مجمع را می‌بری جایی که کمتر کسی برسد، کمتر کسی سؤال بپرسد و کمتر کسی مزاحم تصمیمات از پیش چیده‌شده شود.
📅
آن هم در تاریخ
۳۱ تیر
؛ درست در اوج فصل مجامع. یعنی هم‌زمانیِ شلوغ، آدرسِ دور، و برای
#خبنیان
حتی نبودِ صورت‌های مالی حسابرسی‌شده روی کدال. یعنی محدودسازی سهامدار، هم از مسیر جغرافیا، هم از مسیر اطلاعات.
📉
این دیگر فقط بی‌نظمی نیست؛ بی‌اعتنایی صریح به حق نظارت سهامدار است. سهامدار را هم به نقطه‌ای پرت می‌فرستند که رسیدن به آن سخت باشد، هم گزارش را در مهلت قانونی روی کدال نمی‌گذارند.
🔁
وقتی در
#درپاد
و
#خبنیان
الگو یکی است، آدرس یکی است، مدل رفتار یکی است و سهامدار عمده هم به یک منشأ مشخص یعنی آقای زنوزی برمی‌گردد، دیگر نمی‌شود این شباهت‌ها را تصادفی دید. این بیشتر شبیه یک الگوی حکمرانی است: استفاده از بورس برای پول و اعتبارش، بدون پذیرش شفافیت، پاسخگویی و دسترسی‌پذیری.
⛔
اگر قرار است سهامدار برای حضور در مجمع، هم با آدرس بجنگد، هم با نبود گزارش حسابرسی‌شده، دیگر اسم این را نباید «برگزاری مجمع» گذاشت؛ اسم درستش بی‌اثر کردن حق مالکیت سهامدار است.
🆔
@FinancialmketAnalysis</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18753" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18752">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">محاصره آمریکا بر ایران دوباره به صورت رسمی آغاز شد.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18752" target="_blank">📅 23:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18751">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سپاه پاسداران :
اگر آمریکا به «اقدامات شرورانه» خود ادامه دهد، «یک قطره» نفت یا گاز از منطقه خارج نخواهد شد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18751" target="_blank">📅 22:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18749">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی:   اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18749" target="_blank">📅 22:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18748">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHx2He-lS5KyIBFR2zDk_EyY9wvcnY_xka5N_QAfrl4ugAL5OyTriyg_wi7hjNucrodO1VXC4EgJDS6e59DKpeZ1IzStYR5Yam82N4ZEWX3mVKnfg2Wk1alsJ7QSZOfSJ6IaLZSKtSiktzqXpdFcbQ53NERpAjjcMRQi7g2RWOG3qeu9_NKbhGqs7bNSA_LX-el_Tnwy-XNAHZQtzAefx86r3qi4YOdEZSeGtWoeVALSOClQ6AyZofeEV9Og_Yoj4qnXZovsCT-8JbMti9aogdYJLX17NU-8j4aygEg3fSMzQExiJqoWanhMxUDuijixCfEF4jnciSNE_oxDC_OvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید مرندی:
برای چند هفته دولت ترامپ در حال تدارک حملات هوایی گسترده و تهاجم زمینی به ایران با حمایت چندین کشور عربی است و  ایران بی‌سروصدا خود را برای یک رویارویی بزرگ آماده کرده است.
در صورت آغاز چنین عملیاتی، آن حکومت های عرب خلیج فارس دوام نخواهند آورد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18748" target="_blank">📅 22:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18747">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">موشک ایرانی پر از منور بر فراز بحرین!  این منورها پدافند موشکی را فریب می‌دهند تا با شلیک های پیاپی، ذخایر موشکی شان دچار فرسایش بشود.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18747" target="_blank">📅 21:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18746">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یک مقام آمریکایی تأیید کرد که نیروهای آمریکایی در حال حاضر در ایران حملات هوایی انجام می‌دهند.
شبکه ABC|</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18746" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18745">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پایگاه شیخ عیسی و ناوگان پنجم آمریکا در بحرین در معرض حملات موشکی شدید قرار گرفته‌اند
خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18745" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18744">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ به نتانیاهو دستور داد نیروهای خود را از سوریه و لبنان خارج کند - آکسیوس</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18744" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18743">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52c0b59bc.mp4?token=FAr26Wd44vOMAFW0CNcL_w8fPaKOjE7bEiPwbfKwGSHsVCZu7i49Nwi7Cb13CXY5-5gNWywEZOgiAztkl3Itfm145S1n9Ubet53Pyal5TxBRN0iVfeCLKe1TEGwtrVy18d3GIgOtQqLAvQpKLBz5tHdLfGZH39HBBaErXvzVg2piXy1yrKxvmcKXI_jl0uoXNvp62jVS26HKPWT3DsN2Za0JBPiavHCKJvVHOW1wiam4IoaljV53EyNRI9DgGXyzRhgPAtPnh9bTkSpuzzllEf2-9DPY6XeJAaSTmhCDUiCWK4Q_eGXTEmqcD-PLB0GD27yXDROv-wP8pkgLoCAIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52c0b59bc.mp4?token=FAr26Wd44vOMAFW0CNcL_w8fPaKOjE7bEiPwbfKwGSHsVCZu7i49Nwi7Cb13CXY5-5gNWywEZOgiAztkl3Itfm145S1n9Ubet53Pyal5TxBRN0iVfeCLKe1TEGwtrVy18d3GIgOtQqLAvQpKLBz5tHdLfGZH39HBBaErXvzVg2piXy1yrKxvmcKXI_jl0uoXNvp62jVS26HKPWT3DsN2Za0JBPiavHCKJvVHOW1wiam4IoaljV53EyNRI9DgGXyzRhgPAtPnh9bTkSpuzzllEf2-9DPY6XeJAaSTmhCDUiCWK4Q_eGXTEmqcD-PLB0GD27yXDROv-wP8pkgLoCAIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موشک ایرانی پر از منور بر فراز بحرین!
این منورها پدافند موشکی را فریب می‌دهند تا با شلیک های پیاپی، ذخایر موشکی شان دچار فرسایش بشود.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18743" target="_blank">📅 21:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18742">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599f22b724.mp4?token=qsfHiJdOu4brIq2k9BN_mi5Z6vnMBXbQPsI43JTNK7YAQDeK8Q2PMRX4ace-rudELb2SdZXZwPa3EOBoAwMCXn3KerxqK7wRL4HLuSjZZNJn9ZbMsWqZMneGpjjhkJN1VIqQ0U-oiT4arbwj18AYDv0lOncEx93smnnqZglktEeAbo1-oTHck3w1BqFjG8eyrFZc5hzxcFzzda1ZNdpc8MDOFY0XUA06tlseeXHyowfwHfUiDZT7px5a3L79vDtehzhLzFyYtH8AbLvR_POU-C3jivarZZdTcFijYfSLtYmpys_6M0J1hm_5zMJiz4-f1XwYpFo6O2y8zFugxW7ytg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599f22b724.mp4?token=qsfHiJdOu4brIq2k9BN_mi5Z6vnMBXbQPsI43JTNK7YAQDeK8Q2PMRX4ace-rudELb2SdZXZwPa3EOBoAwMCXn3KerxqK7wRL4HLuSjZZNJn9ZbMsWqZMneGpjjhkJN1VIqQ0U-oiT4arbwj18AYDv0lOncEx93smnnqZglktEeAbo1-oTHck3w1BqFjG8eyrFZc5hzxcFzzda1ZNdpc8MDOFY0XUA06tlseeXHyowfwHfUiDZT7px5a3L79vDtehzhLzFyYtH8AbLvR_POU-C3jivarZZdTcFijYfSLtYmpys_6M0J1hm_5zMJiz4-f1XwYpFo6O2y8zFugxW7ytg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دیگر چه کوفتی است در شیراز ؟!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18742" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18741">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به نظر می‌رسد حشدالشعبی هم …</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18741" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18740">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:
به نظر من، و این ممکن است برایتان عجیب باشد، اما خاورمیانه در حال متحد شدن است.
ما در حال از بین بردن زورگوی خاورمیانه هستیم.
ایران، زورگوی خاورمیانه بود. آنها به عراق زور می‌گفتند. آنها به هر کشوری زور می‌گفتند. در سراسر خاورمیانه، ترس وجود داشت.
دیگر هیچ ترسی وجود ندارد.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18740" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18739">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مهر نیوز با استناد به منابع خبری گزارش می‌دهد که رژیم اسرائیل حملات خود به جنوب لبنان را ادامه داده و آتش‌بس را نقض کرده است</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18739" target="_blank">📅 19:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18738">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18738" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18737">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:  او جوان و خوش‌تیپ است.  من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18737" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18736">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8fda31b18.mp4?token=tajZOqWNSU2_rsNIEwiDY9BQD7tmgHFsxBESzcM6supTcdULSgRHMnJwzmE5-wPmee03EEGBp-QH1xhqSpNV5UnLgBf7d6qovFzPswdUNPX1BcJL3SQeWbzk-3AC4YJFVKj6QFalbt0GVGAR2JkAFJnmfZ-dGTt7o4mjUBzbXlNawKvutb6VS2Nj6LRQAZpyaEuNVBNnS4iDdp3LfaodJwxF-lGzBMdieNMr0oRUVfTXUZjZzZnbFx2rgf_MzUM3R1VfaSGSjSHwVbp7SVcgWV0uSwJ8arg-tPYRKwkeFaYKdmdSx0sI47yvkk15GGm5Bz42I-t-6KgOsMTojkuJKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8fda31b18.mp4?token=tajZOqWNSU2_rsNIEwiDY9BQD7tmgHFsxBESzcM6supTcdULSgRHMnJwzmE5-wPmee03EEGBp-QH1xhqSpNV5UnLgBf7d6qovFzPswdUNPX1BcJL3SQeWbzk-3AC4YJFVKj6QFalbt0GVGAR2JkAFJnmfZ-dGTt7o4mjUBzbXlNawKvutb6VS2Nj6LRQAZpyaEuNVBNnS4iDdp3LfaodJwxF-lGzBMdieNMr0oRUVfTXUZjZzZnbFx2rgf_MzUM3R1VfaSGSjSHwVbp7SVcgWV0uSwJ8arg-tPYRKwkeFaYKdmdSx0sI47yvkk15GGm5Bz42I-t-6KgOsMTojkuJKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:
او جوان و خوش‌تیپ است.
من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18736" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18735">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارهای شدید در جنوب ایران و شمال کویت!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18735" target="_blank">📅 19:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18734">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به گزارش‌ها، حداقل چهار موشک بالستیک ایرانی شب گذشته پایگاه هوایی پادشاه فیصل در اردن را هدف قرار دادند.
گزارشهای تصویری نشان می‌دهند که سامانه‌های پدافند هوایی نتوانستند این موشک‌ها را رهگیری کنند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18734" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18733">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارهای شدید در جنوب ایران و شمال کویت!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18733" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18732">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ:  نفت مانند گذشته بی‌سابقه‌ای در جریان است. تنگه هرمز به روی همه کشتی‌ها به جز ایران باز است - به دلیل رهبری دروغگو، خشن و بدخواه آنها که آنها را در مسیر نابودی کامل قرار می‌دهد.  ما محاصره کامل خواهیم داشت، اما فقط کشتی‌هایی که به بنادر ایران می‌آیند…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18732" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18731">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Msd0pIHMH8IB9nkEEg7FNQ2t3xyjAt5zc1A-MxrEp4UDB6CuaILywaZl3QVJfRUgcTQMxZMj3px9wFFnNQeZYjlylXUWFLV_Kq8QjjGUa-hB5z_TOWLzYgYW31oT7yMI1AkTUszUYOWWpDCGHYfKnNNWdgIs8b3YupVDqwLSkHiNqLbSYXQ2olXVXGOeI6PVNbO5WmPycSMIQrnB8NYPeFwm1EeavbKeJdXQdPxLrS9HGLMQMefpvHFQrly2HwuyUkLtsotBJ4qF32-faDLc_fprbyjc4BvNFLK7yOKKB8SJTJtqEa8uV7APL_tnSotpSbq011C_XUd47VdErgYy8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18731" target="_blank">📅 19:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18730">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هدف قرار گرفتن یک تانکر نفتی که پرچم لیبریا را به اهتزاز درآورده و متعلق به امارات است.  3 نفر از خدمه کشتی در میان مفقودین هستند</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18730" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18729">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هدف قرار گرفتن یک تانکر نفتی که پرچم لیبریا را به اهتزاز درآورده و متعلق به امارات است.
3 نفر از خدمه کشتی در میان مفقودین هستند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18729" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18728">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:
نفت مانند گذشته بی‌سابقه‌ای در جریان است. تنگه هرمز به روی همه کشتی‌ها به جز ایران باز است - به دلیل رهبری دروغگو، خشن و بدخواه آنها که آنها را در مسیر نابودی کامل قرار می‌دهد.
ما محاصره کامل خواهیم داشت، اما فقط کشتی‌هایی که به بنادر ایران می‌آیند و برمی‌گردند، یا هر چیزی را که مربوط به محموله‌های ایرانی است، حمل می‌کنند.
من تصمیم گرفته‌ام هزینه بازپرداخت ۲۰ درصدی ایالات متحده را با معاملات تجاری و سرمایه‌گذاری که کشورهای مختلف خلیج فارس در ایالات متحده انجام خواهند داد، جایگزین کنم. این سرمایه‌گذاری‌ها عظیم خواهند بود.
روزهایی که ایران صدها هزار نفر را می‌کشت، به پایان رسیده است و از همه مهمتر، ایران هرگز سلاح هسته‌ای نخواهد داشت!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18728" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18727">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آیا چین آماده دوره پسا-پوتین در روسیه می شود؟!  به نوشته وال استریت ژورنال، چین به آرامی روابطی را در داخل روسیه ایجاد می‌کند که فراتر از پوتین است و با مقامات و نخبگانی ارتباط برقرار می‌کند که پس از رفتن او، آینده این کشور را شکل خواهند داد.  روسیه هم متوجه…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18727" target="_blank">📅 15:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18726">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZqJpvFx8ubUGPyZhpHFtYlVCod9_4OK9-7KVcO77HWEZNw-M2dSZilnwCpFHggPvlZtOF9UDFFgo06QwvWpdbujIsM1bouY_nfXr53vV-P0WwP9AqvMJFePRux7Jfai744-K7Ye9XA8lxT6NpJ4Ai-vlgwzIczQf0S3BN7MLtEULcytxTpZlVEEjSbx3zW38wpV6XqpfxSF7y0RoEUSUHLHuGqSWJxrK-nHlgxAcHSvQWkWxr88yjUBq9efDT7RyZLBhglk0zTizcFT1bTOsUqmKZeH2XQQpOhlOpBK_CfzSFrpG-WhrrItMMusQLXFr1f54NpdZ8pukcEk30jZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا چین آماده دوره پسا-پوتین در روسیه می شود؟!
به نوشته وال استریت ژورنال، چین به آرامی روابطی را در داخل روسیه ایجاد می‌کند که فراتر از پوتین است و با مقامات و نخبگانی ارتباط برقرار می‌کند که پس از رفتن او، آینده این کشور را شکل خواهند داد.
روسیه هم متوجه تلاش‌های جاسوسی فزاینده چین در میان مقامات دولتی رده میانی شده است، اما مسکو تمایلی به مطرح کردن این موضوع با پکن ندارد، زیرا از آسیب رساندن به این رابطه می‌ترسد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18726" target="_blank">📅 15:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18725">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شهادت ۳ نفر در شهرستان حاجی‌آباد بندرعباس
🔹
بر اساس پیگیری‌های خبرنگار تسنیم از استانداری هرمزگان، حمله به مناطق غیرنظامی در غرب بندرعباس و شهرستان حاجی‌آباد تأیید شد.
🔹
در روستای سیدجوذر به یک ساختمان محیط زیست حمله شده که ۳ نفر به شهادت رسیدند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18725" target="_blank">📅 14:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18724">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk1qAOqBzdJ5ZWmfuGAzQgrZC2KkusdHi7iVH-gr5H1v8UgCnwJpdj7ICthcxicDST6wq4BNHtd_tEhrZoJAZZdrDeB21yG3OFd-q9HxebyonnIaSAs09DRr-ESBX5ZB083ELq4JAzXUhqYFFqiJtV-_cVshhY7wElYJWHaE9rdMgHeBGVgPbQ0UcLvRwiF4bJR_UdeSR8rgYiTryxth8kA3QWxH29UfdxhZo5jmfv7BmB1hF0MTnXVguMJIzgsCUsFXFeAPEV2uUONrT7awP-1oLjIo2rFRTo5MbD4ilUMsbBMiiCiypodTuv3j9f-Rku6t3yuWjzsubiLUJA-8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی که دیشب به ترامپ توصیه کرده بود برود نگهبان قبر لیندسی گراهام بشود، همان دیشب از هیات رییسه کمیسیون امنیت ملی مجلس کنار گذاشته شد!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18724" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18723">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پاکستان از عربستان وام گرفته تا بدهی اش به امارات را بدهد!  مستراح گدایان!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18723" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18722">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بر اساس گزارش‌های رسانه‌های دولتی ایران، حملات هوایی آمریکا به چهار نقطه در شهر بوشهر، ایران، انجام شد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18722" target="_blank">📅 14:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18721">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ضربه قایقهای انتحاری آمریکا به تاسیسات صنایع دریایی مواردی را آشکار کرد. ارتفاع قایق نهایت 2.5-3m باشد که رادارها سطحی توام با کلاتر دریایی کمی دیرتر قایق را میگیرند اما  باز هم چندین کیلومتر فرصت دارند (رادارهای پر ارتفاع؟).از آن سو ج.ا مدیریت شبکه محور روی عبور قایقهای خودی ندارد، میتواند با آنها اشتباه بگیرد.
نظارت آمریکاییها با پهپاد از آسمان، گشتیهای سپاه را هم تحت رصد دارد که با یک عملیات شبکه محور از میان چند جزیره ایرانی به خوبی عبور کرده و خود را به سادگی به بطن صنایع دریایی رسانده است. در موقعیت شبهای بحرانی احتمالا گشتی ها سپاه و نظارت انسانی ساحلی هم کاهش می‌یابد، زیرا ریسک عملیاتی بالایی با توجه به تسلط هوایی آمریکاییها وجود دارد. در کل شکست عملیاتی جدی بود و رخنه‌های بزرگی را آشکار کرد.
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18721" target="_blank">📅 13:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18720">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">توییت سازمان اطلاعات سپاه!  به تاریخ ها دقت کنید؛ مشخصاً راهبرد سپاه این است که این تاریخ های حساس برای آمریکایی ها خالی از جنگ نباشد.  از همین تقویمی که در پست ریپلای شده قرار دادم استفاده شده است.  11 ژوئن = تاریخ آغاز جام جهانی 3 نوامبر = انتخابات مجالس…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18720" target="_blank">📅 13:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18719">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18719" target="_blank">📅 13:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18718">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ney8vR_hUFzfJkZcvT4gBxFFONaYHBHoj8x_pX_9CmRmKYy1FnTK08ty4pi20bKk56tBHq8CxL5gRE1cBxTwNv3giv1Xnw4fNy5u82gAM-JIvpjDQnHYuZsZ02IGiAWf8MQ1J9bQzweQkCAlm4ftOge23n9Y2NH82E48aWb8pePEPvAMFmrCCJpxBuaAobYw709yfX4QAXaMh5WYMls9tdkaJ39-VJnDr4CPK0CwN5xSIo3PlxnWd26tReGCQbNRH77jCATWY2yH1S-2h73hKqodHwBl_uMmqmBv7c9rI3-3l8mfTJrMOLdRftnGYxYcDvnvs7PpM3mr48BGnU1deg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی قرار دارد.
با توجه به انتشار خبر کلیدی تورم، اساساً این ساعات برای معامله مناسب نیست.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18718" target="_blank">📅 12:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18717">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 7
سه شنبه 14 جولای 2026</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18717" target="_blank">📅 12:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18716">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی:   اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18716" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18715">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یک نفر دایرکت داده خدا لعنتشان کند؛ دیشب ‌پیک اول را زده بودم برق رفت همه جا تاریک شد فکر کردم کور شده ام!</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18715" target="_blank">📅 10:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18714">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزارت دفاع امارات:   در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18714" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18713">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزارت دفاع امارات:   در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18713" target="_blank">📅 02:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18712">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزارت دفاع امارات:
در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/18712" target="_blank">📅 02:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18711">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گزارشگر: شما ماه‌هاست که ایران را بمباران می‌کنید. آیا این وضعیت عادی جدید است؟
ترامپ: ما ۱۹ سال در ویتنام بودیم در حالی که فقط ۴ ماه است که ما اینجا هستیم.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18711" target="_blank">📅 02:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18710">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ادعای وزارت دفاع امارات:
دو نفتکش اماراتی در مسیر جنوبی تنگه هرمز با دو فروند موشک کروز ایرانی هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18710" target="_blank">📅 02:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18709">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قطعی برق در دمای 40 درجه به نظرم خیلی زیبنده ابرقدرت 4 دنیا نیست ولی خب.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/18709" target="_blank">📅 01:26 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
