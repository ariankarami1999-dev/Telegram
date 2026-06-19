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
<img src="https://cdn4.telesco.pe/file/AElUrNWtgkCqAD_xVxtRc8Q7hI1uMJ_wPNavRma7NTMJl7AKkJKNIE1ERABi3FYBA8AhOWVYAAkHtBj7EiOAWH1VJbcfOuiwDPMP3BMFg3kOvz9EKdUPT45nVRo9bJ17Cz1RGtNrOcac1UcUuMUkmPKXaMsrnMwcoh6sAZrv-Y-Ra7bZCmcpmFPTJwrXI1Isb1xvMryh-e2EvdTMhDvDjNR47ox_ZUa00r0riHBX_srrnCS_KG6FGPRsuNvlRhtd4dzHLaXSB5eNPCws_G8y37V-zidk5Tq-6GDV0OOyYxKUcC7wpBXfD_LEL7fdYYR6TQDoA51ilFVv27MDhti62Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 09:01:53</div>
<hr>

<div class="tg-post" id="msg-17767">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شریعتمداری:   مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/17767" target="_blank">📅 23:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شریعتمداری:
مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/17766" target="_blank">📅 22:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17765">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoojJtV5mV_Tn7HyFHIP7rUyIbnIUW8e-AdO2AOsSS8chM_6S5s5rY8_j3M68DjlMwhv1xzX4k2-TBO4Kl1BGqxJX38P04Mri7CrUg8FW5RCfDrFDoCFXgC6yovC2WGkuPpN2MUNVTOIurJTx5QvDuN0BZqMAws9SCBBxH8dvOcl7vpsN4U3P-fQ5HUZo4JmZ1wBolyBgRFJqEkuOVTMDAZrzvsybAbZPR1G-e85XhqGoq8bhZihCTP4rpVxZYo0oG8OgPR9bO8qqchDipIR67EEVp7AzI7eE3PSYbEERPtHRCjVQ0j9eOG8wchBrcIPXRTytaypTs5Ks6pN1hvLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر از چکیده پیام رهبری</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/17765" target="_blank">📅 22:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">چه کسی گمان می‌کرد روزی این امضای موزگونه زیر برگه ای بخورد که امضای ابوایوانکا هم روبروش باشد؟!  سبحان الله !</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/17764" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17763">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ :  «اگر به نتیجه برسد، من اعتبارش را می‌گیرم. اگر به نتیجه نرسد، جی‌دی را مقصر می‌دانم.»   «بهتر است مراقب باشی، جی‌دی!»  «او هواپیمایش را برمی‌گرداند و از اینجا گم می‌شود.»</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/17763" target="_blank">📅 22:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17762">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">متن کامل پیام رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
🔹
بسم‌ الله‌ الرّحمن ‌الرّحیم
ملّت پرشور و باوفای ایران
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این مرحله، مسئولین امر، از سر دلسوزی و با حُسن نظر، تلاش‌های زیادی را به‌عمل آوردند و البته این رئیس‌جمهور آمریکا بود که از روی استیصال، از انواع اهرم‌ها برای این امر استفاده می‌کرد.
🔹
بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت حقوق ملّت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه‌ی آن را صادر نمودم‌. ایشان همچنین تصریح کرده‌اند که اگر طرف آمریکایی بخواهد زیاده‌خواهی کند زیر بار آن نخواهند رفت. از این لحظه، ما یعنی شما ملت سرافراز و این خادم ناچیز، منتظر تحقّق شروط گفته‌شده خواهیم بود. امّا بدیهی است مذاکرات حضوری که در آینده برقرار خواهد شد، به معنی پذیرش نظر دشمن نخواهد بود. امیدواریم که دعای خیر سرورمان عجّل‌الله‌تعالی‌فرجه‌الشّریف انواع نصرت‌ها و فتوحات، برای ملّت باشرف ایران به ارمغان آورد.
🔹
والسّلام علیکم و رحمة الله و برکاته
✍
سید مجتبی حسینی خامنه‌ای
🗓
۲۸/خرداد/۱۴۰۵</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/17762" target="_blank">📅 21:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17761">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/17761" target="_blank">📅 20:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17760">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده:   ناو‌های نیروی دریایی ایالات متحده برای اطمینان از رعایت تمام مفاد توافق‌نامه در منطقه باقی خواهند ماند.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/17760" target="_blank">📅 20:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17759">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده:
ناو‌های نیروی دریایی ایالات متحده برای اطمینان از رعایت تمام مفاد توافق‌نامه در منطقه باقی خواهند ماند.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17759" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17758">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-poll">
<h4>📊 در عصر مدرن، کدام کشور زیرساخت‌های نظامی زیرزمینی را به یک استراتژی ملی تبدیل کرد؟</h4>
<ul>
<li>✓ آلمان</li>
<li>✓ سوییس</li>
<li>✓ کره شمالی</li>
<li>✓ سوئد</li>
</ul>
</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/17758" target="_blank">📅 20:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17757">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیام بسیار مهم رهبر معظم انقلاب حضرت ایت الله خامنه‌ای مدظله‌العالی درخصوص تفاهم پایان جنگ خطاب به ملت ایران تا ساعتی دیگر منتشر خواهد شد</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/17757" target="_blank">📅 20:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17756">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ونس در مورد ایران و موشک‌ها:   ما انتظار داریم که به عنوان بخشی از توافق نهایی، ایران موشک‌هایی که کل جهان را تهدید می‌کنند، نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/17756" target="_blank">📅 20:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17755">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ونس در مورد ایران و موشک‌ها:
ما انتظار داریم که به عنوان بخشی از توافق نهایی، ایران موشک‌هایی که کل جهان را تهدید می‌کنند، نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/17755" target="_blank">📅 20:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17754">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فایننشال تایمز:
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌ های بلوکه‌ شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/17754" target="_blank">📅 20:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17753">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آفند زرهی سنگین حاجی فتل به جوان دانشمند بمال صداوسیما
نابودش کرد !</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17753" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17752">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ فاش کرد که حملات و بمباران‌های ایالات متحده بیش از ۱ تریلیون دلار به ایران خسارت وارد کرده است.  «بازسازی آنها ۱۵ تا ۲۰ سال طول می‌کشد. بنابراین باید خودشان رفتار کنند. اگر رفتار خوبی نداشته باشند، دوباره ضربه می‌خورند.»  ترامپ همچنین تأیید کرد که ایالات…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/17752" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17751">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fnhx9TcKbhZ5ZLur5DoAJBl4a5f0Zn58-EJDlORyADtHT3slyOYYlL8bGmGtps7AQq1IuUdmEAGKJbb5bGGydxWAfyjpMWWuvhe3S3hE3LVJQX16zpsxLVYKeRoc-dCUyHP8Xw614jOCf4RoUFYCWnxbWFUF0eo6v7eTliDI1FpownOOLObzJ85yo0aYD5z9Jt4cnWxGQsOZji1S7Rr-pxI0VBLpIaWxT6g4wuxu95eafMVMa3x_zINwxsN2Rw94SUdOsWFQ0l03FA8nnQRoR29Rl-UiZf0AyGu-UMSPf546SxPkH3bSQNZ8iRjUNAd-Ryhl45IoSd0W9xR_qdm0yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی کانالهای ارزشی این عکس را منتشر کرده اند و نتیجه گرفته اند انتخاب این مدل و رنگ لباس از سوی پزشکیان نمیتواند اتفاقی باشد!
سبحان الله!</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/17751" target="_blank">📅 19:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17750">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وضعیت مسکو پس از حملات سنگین پهپادی اوکراینیها به تاسیسات انرژی</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/17750" target="_blank">📅 19:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17749">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نمودارهای برگرفته از سایت شرطبندی Polymarket نشان‌دهنده سقوط چشمگیر شانس‌های انتخاباتی بنیامین نتانیاهو در ماه‌های اخیر است.   خط زرد (احتمال نتانیاهو به عنوان نخست‌وزیر بعدی) از حدود ۵۰-۶۰٪ در فوریه با نوسانات اولیه به اوج می‌رسد، اما از اواخر مارس با شروع…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/17749" target="_blank">📅 17:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17748">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/17748" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بی‌بیِ بی‌چاره!   نتانیاهوی بی‌چاره! چی فکر می‌کرد، چی شد! این سزای کسی است که گمان می‌کند با زور اسلحه و کشتار به هر هدفی می‌توان دست یافت! تازه این اول بیچارگی اوست. در انتخابات پاییز امسال شاید حزب او بتواند یکی-دو کرسی نمایندگی بیش از دیگر احزاب در پارلمان…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17748" target="_blank">📅 17:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17747">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">برخی گمان می‌کنند رفتن نتانیاهو یعنی پایان قطعی جنگ اسراییل ضد ایران و محور مقاومت.   توهم محض است. دیدگاهم را در یک صوتی مفصل با شما به اشتراک خواهم گذاشت.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17747" target="_blank">📅 17:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17746">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فیصل بن فرحان آل سعود، وزیر خارجه عربستان:
«حمله ایران به پادشاهی و کشورهای شورای همکاری خلیج فارس، اعتماد متقابل را سلب کرد.
پس از تفاهم پکن و آغاز روند عادی‌سازی روابط، ما در آستانه گشایش همکاری‌های اقتصادی بودیم، اما اکنون عقب‌نشینی کرده‌ایم.
پیش از هر بحثی درباره سرمایه‌گذاری یا همکاری، باید درباره بازسازی اعتماد و رابطه گفتگو کنیم؛ این مسئله برای بسیاری از کشورهای شورای همکاری نیز صادق است.»</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17746" target="_blank">📅 13:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17745">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm7GSMRCDDNJaf4CrxBQulADjlpH49NvzVnz-3zP3oqpiE9gxcOEjuJuP-3E66foC07qjFpZntrnvtll5z_iMWTRl82yhs3fL55NwAnRBaFfIldoyFFh37njePxf_LDKBMXovhatWShdtBoMx46kDCGos8zdjoQh0tq_oUPeiqkm4P6HRIQGjJikCu8EBWyfSWblUjmBECQrAVkdTC8QRHNtmgJ4KIkOTlNot3hMX77wgeOrKnGf6XjEAZNBtnzc0u8dhYzbFxw1RTwPP9Ju5CDHIj7FL6Nb0ypZOWREj5HWtBpvHBaeoWyN_9gS0ejk9Gzlk43gZ9vFxTyw0EmdmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل نقشه منطقه حائل در جنوب لبنان را منتشر کرد
ارتش اسرائیل نقشه‌ای منتشر کرد که نشان می‌دهد منطقه امنیتی آن تقریباً ۱۰ کیلومتر به داخل خاک لبنان گسترش یافته است، جایی که نیروها به عملیات برای حذف تهدیدات و حفاظت از ساکنان شمال اسرائیل ادامه می‌دهند</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17745" target="_blank">📅 13:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17744">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17744" target="_blank">📅 13:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17743">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‎روزنامه اکونومیک تایمز  هند و روسیه توافق کردند تا نسخه پیشرفته تر موشک «Brahmos» را در تیراژ بالا تولید کنند.  در جنگ اخیر هند و پاکستان، این موشک بهترین ابزار هندی ها بود و بر خلاف نبردهای هوایی، مایه جبران مافات برای ارتش هند شد.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17743" target="_blank">📅 12:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17742">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رئیس بانک ملی سوئیس: مشخص نیست کاهش تنش در خاورمیانه دائمی باشد یا خیر</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17742" target="_blank">📅 12:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17741">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رئیس بانک ملی سوئیس: مشخص نیست کاهش تنش در خاورمیانه دائمی باشد یا خیر</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17741" target="_blank">📅 12:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17740">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اینها مواردی است که اسراییل را به سمت یک راهکار نهایی پایدار منطقه ای بوم پایه  — بجای آویزان شدن از غرب (و خصوصا آمریکا) — می برد و کریدور داوود و پیمان موسوم به کوروش و … در چنین بستری معنا می یابد.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17740" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17739">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVLEA1InwTsGWMGXd6o39Oo9jgtPSj_8ViRxBGLdy6z7XCkX3fx4Sr_QVpnyu14ot7gvspJS4q8IzFLwhDLTDEfVDyVP1sDZeKfnB_w6bVoDhFXTh-dFxSBo5XUO2T868zZPj-OBo93GCNNndc5zhg3mYStEh2CdHN9RtJWXwbAMC5dzMRoBf2o9ojBhRGFEUDYyepi9C2Nr5OaCvDN-lORmRAn4-s8PkwIAgCybZiGl6siOV30lSQAidVWcij31lFjCNhpwgaIiM-PhlDHzSa5Ab23BOdoZZax7uel9a1M5lFA643xSaYcPbQra47w4klUCydzZX2vQuAHkR27tHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت مسکو پس از حملات سنگین پهپادی اوکراینیها به تاسیسات انرژی</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17739" target="_blank">📅 12:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17738">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ولی انصافا اگر همه این مواردی که قالیباف می‌گوید در توافقنامه با آمریکا از سوی ترامپ امضا شده باشد امتیازات بزرگی برای جمهوری اسلامی ایران است.  بحدی این امتیازات زیاد است که آدم فکر می‌کند یا جمهوری اسلامی سلاح هسته ای دارد یا چند نسخه از فیلم های مستهجن…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17738" target="_blank">📅 12:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17737">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxIpVXcdD9a9wuOxhGbxdVPdBVHln7dbDt_APtxl97sdT79yx99IYrF-WQDXYxo9hIDYslIfhtu7i_GRkSRp1Y7n9uckthwns9P60Ux2XprThb4-p6GrnZDVBXvaMn5bTzuWorbFtAaANqGnsoZ_RwrlAX0-3JCXy5lZUYRBrsGHnkVhMwZ4krzsAqHhhNqlL7PdResM30I3tGdNzvHstYtO5uMnAL7VpESflissEYIrJYZ-dzg9xk25h67HjGR29ZNZKuLzt1JR9OtN_m95TRdkw2Ebh6oAJRo5tfmiulXDI99SdeBWaSe1RIJTopUyA9qsmPlhtVlCO0ATaoRQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی گمان می‌کرد روزی این امضای موزگونه زیر برگه ای بخورد که امضای ابوایوانکا هم روبروش باشد؟!  سبحان الله !</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17737" target="_blank">📅 11:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17736">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو: اسرائیل به بند لبنان در توافق ایران و آمریکا پایبند نیست!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17736" target="_blank">📅 11:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17735">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در هر مقاله اش ۸ سوال از خودش میپرسد آخرش هم نتیجه ای می‌گیرد که معلوم نیست اساسا چه ربطی به سوال های بی پاسخ ش دارد</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17735" target="_blank">📅 11:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17734">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd5QMaO6vwe9Enjrs_YYwVXk59tLAZ9NfS_r2D-mNfbz8GI9ei3y1LEsqn3hHVqdlanMo44U1wRJjnacVuN57xCnIy344Hil9n2dMd-YIjo_I1ldVr1or1InYYhqzkZq7xzltJVs07cguZn8p5HUfO2Vfyq7quxNUNuwO1_n5LfHdyBWbnXw10TCzyamct21HoXswZsQ0qffr7TXJiRRymv13bVqsadiSzTY3Idz3fpu_hZTPx79BwbmHut48Ji5liggOiECvM89-VqU6TJJSUtDmysSrlvSUnRdoRBNhL67WMSW5ZarSexOhoTC3sUzo1CtMmeD8FuvNzeGpATQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پرزیدنت پوزیده مثل موزی است که بخواهد ماهیگیری کند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/17734" target="_blank">📅 07:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به عنوان بخشی از بند عدم مداخله در امور داخلی ایران، رئیس‌جمهور ترامپ توافق شفاهی داده که دیگر بیانیه‌های حمایتی از «اعتراض‌کنندگان» ایرانی صادر نکند، دستگاه‌های ارتباطی ارسال نکند، یا به آن‌ها سلاح ندهد</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17733" target="_blank">📅 01:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17732">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ایالات متحده آمریکا متعهد می‌شود که بلافاصله پس از امضای این تفاهم‌نامه تا زمان لغو تحریم‌ها، وزارت خزانه‌داری ایالات متحده معافیت‌های لازم را برای صادرات نفت خام ایران، محصولات نفتی و مشتقات آن و همه خدمات مرتبط شامل معاملات بانکی، بیمه، حمل‌ونقل و غیره صادر کند.
ایالات متحده آمریکا متعهد می‌شود که وجوه و دارایی‌های مسدود یا محدودشدهٔ جمهوری اسلامی ایران را بلافاصله پس از اجرای این تفاهم‌نامه به طور کامل در اختیار قرار دهد.
ایالات متحده آمریکا و جمهوری اسلامی ایران در طول مذاکرات بر رویه‌های مربوط به آزادسازی این وجوه توافق خواهند کرد. این وجوه، چه در حساب اصلی باقی بمانند یا منتقل شوند، باید به طور کامل قابل استفاده برای پرداخت به هر ذی‌نفع نهایی که بانک مرکزی جمهوری اسلامی ایران تعیین می‌کند، باشند. ایالات متحده آمریکا متعهد می‌شود همه مجوزها و اجازه‌های لازم را صادر کند.
ایالات متحده آمریکا و جمهوری اسلامی ایران توافق دارند که یک سازوکار اجرایی برای نظارت بر اجرای موفق این تفاهم‌نامه و رعایت آیندهٔ توافق نهایی ایجاد شود.
پس از امضای این تفاهم‌نامه و مشروط به آغاز اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این تفاهم‌نامه و ادامهٔ اجرای این اقدامات، ایالات متحده آمریکا و جمهوری اسلامی ایران مذاکرات مربوط به توافق نهایی را صرفاً دربارهٔ سایر بندها آغاز خواهند کرد.
توافق نهایی توسط قطعنامهٔ الزام‌آور شورای امنیت سازمان ملل متحد تأیید خواهد شد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17732" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17731">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">متن توافقنامه به روایت فارین پالیسی:
تفاهم اسلام‌آباد بین ایالات متحده آمریکا و جمهوری اسلامی ایران
ایالات متحده آمریکا و جمهوری اسلامی ایران و متحدان‌شان در جنگ فعلی، با امضای این تفاهم‌نامه، خاتمهٔ فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله لبنان، را اعلام می‌کنند و از این لحظه به بعد متعهد می‌شوند که هیچ جنگ یا عملیات نظامی علیه یکدیگر آغاز نکنند، از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند و تمامیت ارضی و حاکمیت لبنان را تضمین نمایند. توافق نهایی، خاتمهٔ دائمی جنگ در همه جبهه‌ها از جمله لبنان و سایر مفاد این بند را تأیید خواهد کرد.
ایالات متحده آمریکا و جمهوری اسلامی ایران متعهد می‌شوند که حاکمیت و تمامیت ارضی یکدیگر را محترم بشمارند و از دخالت در امور داخلی یکدیگر پرهیز کنند.
ایالات متحده آمریکا و جمهوری اسلامی ایران متعهد می‌شوند که ظرف حداکثر ۶۰ روز (قابل تمدید با توافق متقابل) مذاکره کرده و به توافق نهایی دست یابند.
بلافاصله پس از امضای این تفاهم‌نامه، ایالات متحده آمریکا شروع به برداشتن محاصرهٔ دریایی خود و هرگونه اختلال یا مانع علیه جمهوری اسلامی ایران خواهد کرد و محاصرهٔ دریایی را ظرف ۳۰ روز به طور کامل پایان خواهد داد. در این دوره، تردد کشتی‌ها متناسب با تعداد تردد پیش از جنگ که توسط جمهوری اسلامی ایران بازگردانده می‌شود، خواهد بود. ایالات متحده آمریکا همچنین متعهد می‌شود نیروهای خود را ظرف ۳۰ روز پس از توافق نهایی از نزدیکی جمهوری اسلامی ایران خارج کند.
پس از امضای این تفاهم‌نامه، جمهوری اسلامی ایران با به‌کارگیری بهترین تلاش‌های خود، تمهیدات لازم را برای عبور ایمن کشتی‌های تجاری بدون دریافت هیچ هزینه‌ای به مدت ۶۰ روز از خلیج فارس به دریای عمان و بالعکس فراهم خواهد کرد. تردد کشتی‌های تجاری فوراً آغاز می‌شود و با توجه به نیاز به رفع موانع فنی و نظامی و مین‌زدایی توسط جمهوری اسلامی ایران، ظرف ۳۰ روز به طور کامل برقرار خواهد شد. جمهوری اسلامی ایران با سلطان‌نشین عمان گفتگو خواهد کرد تا ادارهٔ آینده و خدمات دریایی در تنگهٔ هرمز را، با مشورت سایر کشورهای ساحلی خلیج فارس و در چارچوب حقوق بین‌الملل و حقوق حاکمیتی کشورهای ساحلی تنگهٔ هرمز، تعیین نماید.
ایالات متحده آمریکا متعهد می‌شود که همراه با شرکای منطقه‌ای، طرح قطعی و مورد توافق متقابل با حداقل ۳۰۰ میلیارد دلار برای بازسازی و توسعهٔ اقتصادی جمهوری اسلامی ایران تهیه کند. سازوکار اجرای این طرح به عنوان بخشی از توافق نهایی ظرف ۶۰ روز نهایی خواهد شد. همه مجوزها، معافیت‌ها و اجازه‌های لازم برای انجام معاملات مالی مرتبط توسط ایالات متحده آمریکا صادر خواهد شد.
ایالات متحده آمریکا متعهد می‌شود که همه انواع تحریم‌ها علیه جمهوری اسلامی ایران شامل قطعنامه‌های شورای امنیت سازمان ملل متحد، قطعنامه‌های هیئت مدیرهٔ آژانس بین‌المللی انرژی اتمی و همه تحریم‌های یک‌جانبهٔ آمریکا (اولیه و ثانویه) را طبق برنامهٔ زمانی مورد توافق، به عنوان بخشی از توافق نهایی لغو کند.
جمهوری اسلامی ایران و ایالات متحده آمریکا اهمیت حیاتی مسئلهٔ لغو تحریم‌های فوق را درک کرده و عزم خود را برای رسیدگی فوری به این موضوعات در مذاکرات به منظور دستیابی به توافق متقابل اعلام می‌دارند.
جمهوری اسلامی ایران مجدداً تأیید می‌کند که سلاح هسته‌ای تولید یا توسعه نخواهد داد.
ایالات متحده آمریکا و جمهوری اسلامی ایران توافق کرده‌اند که وضعیت مواد غنی‌شدهٔ ذخیره‌شده را طبق سازوکاری که به صورت متقابل توافق خواهد شد و مطابق با برنامهٔ زمانی ذکرشده در بند هفت، حل و فصل کنند؛ به‌گونه‌ای که حداقل روش، رقیق‌سازی در محل تحت نظارت آژانس بین‌المللی انرژی اتمی باشد. دو طرف همچنین توافق کرده‌اند که مسئلهٔ غنی‌سازی و سایر موضوعات مورد توافق مرتبط با نیازهای هسته‌ای جمهوری اسلامی ایران را بر اساس چارچوب رضایت‌بخشی که در توافق نهایی مورد توافق قرار می‌گیرد، مورد بحث قرار دهند. توافق نهایی مفاد این بند را تأیید خواهد کرد.
ایالات متحده آمریکا و جمهوری اسلامی ایران اهمیت حیاتی مسائل هسته‌ای فوق را درک کرده و قصد خود را برای رسیدگی فوری به این مسائل در مذاکرات ابراز می‌دارند.
تا زمان دستیابی به توافق نهایی، ایالات متحده آمریکا و جمهوری اسلامی ایران توافق دارند که وضعیت موجود را حفظ کنند. جمهوری اسلامی ایران وضعیت فعلی برنامهٔ هسته‌ای خود را حفظ خواهد کرد و ایالات متحده آمریکا هیچ تحریم جدیدی اعمال نخواهد کرد و نیروهای اضافی در منطقه مستقر نخواهد کرد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17731" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یاد فلیم اخراجی ها افتادم که امین حیایی آن پسره برادر کمند امیرسلیمانی را اسکل کرده بود!  یک تاس به او داده بود میگفت بریز اگر 1 تا 5 آمد بازنده ای و باید پول بدهی و اگر 6 آمد برنده ای. بعد امیرسلیمانی پرسید اگر برنده شدم چی؟!   امین حیایی گفت اگر برنده شدی…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/17730" target="_blank">📅 01:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">من دقیقا نمیفهمم روی چه چیزی به جز پایان موقت ۶۰ روزه جنگ توافق شده؟!
لبنان؟! تنگه هرمز؟! موشکی؟! نیابتی؟!</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17729" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17728">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ: ما در مورد موشک‌های بالستیک و نیابتی‌های تروریستی صحبت خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17728" target="_blank">📅 01:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17727">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">به نظر شما هم مجموع اعداد از ۱۰۰ درصد بیشتر می‌شود یا من اشتباه میکنم؟!</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17727" target="_blank">📅 01:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17726">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv2kovl3xlksENAS2iAG4Ff3-uU78yaOgtzK6Q2gw8AY-Ae8q_CX1eR4LhD5UZKY-Ihs6VQ7cQrjCohrx6O5F0psehMoJsaidGpKUqxDXFRXFFGgZ0pB86zuI0J-oJhviJYNRTZmGuBBm9Vp87pYQHCuYG78rEXvJMHVX662CC_brs5UOruAKji8600EmjiQF2zuuOEPpuumRxunhBY4mL_cIbk4tP_r-XXgngPSbsmExWp-Pf7VLv8axqjvGpfMiUcjztMIfVKXIuUlj9WXh517wkvqwuPR2QbW1wrp3sDVZ4VZu6Ng9R69_oT4TULhT6McN-qSdiQuGLiSFOJcAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر شما هم مجموع اعداد از ۱۰۰ درصد بیشتر می‌شود یا من اشتباه میکنم؟!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17726" target="_blank">📅 01:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17725">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ولی انصافا اگر همه این مواردی که قالیباف می‌گوید در توافقنامه با آمریکا از سوی ترامپ امضا شده باشد امتیازات بزرگی برای جمهوری اسلامی ایران است.  بحدی این امتیازات زیاد است که آدم فکر می‌کند یا جمهوری اسلامی سلاح هسته ای دارد یا چند نسخه از فیلم های مستهجن…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17725" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17724">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-poll">
<h4>📊 کدام طرف پیروز مذاکرات است؟!</h4>
<ul>
<li>✓ ایران</li>
<li>✓ آمریکا</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17724" target="_blank">📅 01:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17723">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رئیس مجلس شورای اسلامی ایران، قالیباف:  تأکید می‌کنم که تنگه هرمز هرگز به وضعیت قبلی خود باز نخواهد گشت.  ایران حق دارد هزینه‌های عبور را تحمیل کند. تفاهم‌نامه پیش‌بینی می‌کند که ایران و عمان در مورد چگونگی توافق آتش‌بس گفتگو کنند.  ما دستورالعمل‌هایی از رهبر…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17723" target="_blank">📅 01:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17722">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خون خواهی رهبر شهید یعنی آزادی قدس!</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17722" target="_blank">📅 01:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17721">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">قالیباف:   هر جا دشمن تعهدات خود را انجام ندهد، شمشیر ما آماده است و با منطق قدرت، آمریکایی‌ها را درک خواهیم کرد.  «من دیپلمات نیستم، اما بسیار خوب می‌دانم چگونه به آمریکا بفهمانم که چه کاری را باید انجام دهد.»</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17721" target="_blank">📅 01:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17720">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی:
🔸️
همین حالا که با شما صحبت می‌کنم، متن یادداشت تفاهم اسلام‌آباد احتمالاً توسط رؤسای جمهور ایران و آمریکا امضا شده است.
🔹️
قرار بر این شده که یادداشت تفاهم به صورت دیجیتال امضا شود؛ وقتی یادداشت تفاهم توسط رؤسای جمهور دو کشور امضا شود، نقض آن هزینه بالاتری خواهد داشت.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17720" target="_blank">📅 01:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17719">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قالیباف:
هر جا دشمن تعهدات خود را انجام ندهد، شمشیر ما آماده است و با منطق قدرت، آمریکایی‌ها را درک خواهیم کرد.
«من دیپلمات نیستم، اما بسیار خوب می‌دانم چگونه به آمریکا بفهمانم که چه کاری را باید انجام دهد.»</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17719" target="_blank">📅 00:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17718">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رئیس مجلس شورای اسلامی ایران، قالیباف:
تأکید می‌کنم که تنگه هرمز هرگز به وضعیت قبلی خود باز نخواهد گشت.
ایران حق دارد هزینه‌های عبور را تحمیل کند. تفاهم‌نامه پیش‌بینی می‌کند که ایران و عمان در مورد چگونگی توافق آتش‌بس گفتگو کنند.
ما دستورالعمل‌هایی از رهبر انقلاب اسلامی داریم و وظیفه ما این است که در این مذاکرات برای اجرای این دستورالعمل‌ها تلاش کنیم.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17718" target="_blank">📅 00:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17717">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قالیباف: ما آمریکا و اسرائیل را از نظر نظامی شکست دادیم، حتی با اینکه آنها از جمله قدرت‌های برتر جهان بودند   «ما اجازه ندادیم آنها به اهدافی که هنگام شروع جنگ اعلام کردند، دست یابند»</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17717" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17716">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قالیباف: ما آمریکا و اسرائیل را از نظر نظامی شکست دادیم، حتی با اینکه آنها از جمله قدرت‌های برتر جهان بودند
«ما اجازه ندادیم آنها به اهدافی که هنگام شروع جنگ اعلام کردند، دست یابند»</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17716" target="_blank">📅 23:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17715">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaJAwa3OV9dAJonYNLabsqVs0Rv5uaH5aM6ZxCrli5Q3jw_b9IT9a3oE6Rtte4FTiw8j1NIG4DKoqmAuDbFjk6VGx_bLvfnzTJxMGtznD8dK4G6_DYTNHO5StGvQEH6guq_z1apKtjkdage-wyI0gDLKInbtD13IGpH-6TAdB7PMdRXN0oxgXNcrAlv1vxIQQbt9iSmEc91I3nhn9UD6Qwm9EfbwFhmwUuNApNOcOwLkNIoCc5estJtH1WqEJEI9JFQtFPfbqCDzlqEJ-G1zknEbTTPQulpJQqtvnnlzve7VD9Zy3NlI51p48mmtlsf308MGuhjhuNsvlkoXrsVLnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوزیشنی که 3 دقیقه پیش از انتشار صورتجلسه فومسی پیشنهاد شد.  بشدت هاوکیش موضع گیری کردند و آفتابه را روی کله زرد گرفتند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17715" target="_blank">📅 23:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17714">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ می‌گوید احتمالاً نیروی دریایی ایالات متحده را برای «مدتی» در خلیج عمان نزدیک تنگه هرمز نگه خواهد داشت.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17714" target="_blank">📅 22:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17713">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ می‌گوید احتمالاً نیروی دریایی ایالات متحده را برای «مدتی» در خلیج عمان نزدیک تنگه هرمز نگه خواهد داشت.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17713" target="_blank">📅 22:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17712">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">— یک مقام کاخ سفید:
«ایران باید فعالیت‌های حزب‌الله را محدود کند و هر حمله‌ای از سوی این گروه با یک پاسخ مستقیم اسرائیلی روبرو خواهد شد».</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17712" target="_blank">📅 22:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17711">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پوزیشنی که 3 دقیقه پیش از انتشار صورتجلسه فومسی پیشنهاد شد.  بشدت هاوکیش موضع گیری کردند و آفتابه را روی کله زرد گرفتند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17711" target="_blank">📅 21:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17710">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7rEJWc-ycl_vM0DGpG5sxx6bAT0UGqj4Iw0B_D8OjPTOqBiXx69BpU2RoK-pJGfluR9fYU9VAaQqDMsRsAuT79Ldx7ruOMa1EAryX95ZZYA3TsvxsG1ejcH1jQuWhiv--pHqsW--dXkcjYn-DqfDGqUGJR27YPFOP-MRzfdQEr6M0SCqUOF49DIbZ0dkZal6VTU5hiA5g5PHhtilBezr9p_fzY8voikZMr0A1s6eBh15i4-8OKKeapEzdQs4B76Djx5JCyV_R7Tw4g4ksCrg6EHAo045NFFm0eCcXIx2PGMpAv0qRZJjqAFHOaGS_95eeAnQb8VHGuwFsVhwPc06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوزیشنی که 3 دقیقه پیش از انتشار صورتجلسه فومسی پیشنهاد شد.
بشدت هاوکیش موضع گیری کردند و آفتابه را روی کله زرد گرفتند.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17710" target="_blank">📅 21:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزارت امور خارجه ایران:
«لبنان سه بار در یادداشت تفاهم ذکر شده است و جنگ باید در همه جبهه‌ها، به ویژه در لبنان، پایان یابد.»
یادداشت تفاهم بر احترام به حاکمیت لبنان تأکید کرده است و حضور ارتش اسرائیل با این موضوع در تضاد است. اشغال مداوم جنوب لبنان توسط اسرائیل نقض یادداشت تفاهم است و ما اقدامات لازم را انجام خواهیم داد.»</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17709" target="_blank">📅 21:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17708">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزارت امور خارجه ایران:
در حال بررسی امضای تفاهم‌نامه از راه دور بین روسای جمهور دو کشور هستیم</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17708" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17707">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfaTY35-dI4tt2nLlyqqz0JQMePmPxtvdYtzj9UskbYfyhOSFAww2r70MsQM1Cs67zM0WLcwf4H7pm2yF9fQ-EvarkRKNn7L7zqc8swkMyQA_2SOIdwtzJ8ZQZms7pPmLHMw8Yap5fbTzeYxtcrT46I1b9Q-rn6D7nNghPKNwAL1aEBRTc8u9itOTYYkvtfzZULWjpPbo6z9xgfAEsrLzi2qHL5bqot3HHoF1SEQ5HoJt15GDwzU23mkKcxZax7o4BrL8ZPz4n2eRMrsgfyLlLjEG2zhPoQJAN_H6Y24of6X4QOSX3FvpsQSAOqf4bEzEzsUW1FtdGBuihtklh9EWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج از دور باطل
✍🏻
مهدی خراتیان، مدیر اندیشکده احیای سیاست  ‌تغییر در ژئوپولتیک شیعه، عقیم‌سازی حزب‌الله، تضعیف بازدارندگی شبکه‌ای ایران و درنهایت تمهید برای دور بعدی حملات گسترده به خاک ایران، تصمیم قطعی اسراییل است.   نتانیاهو با محاسبه مهار کامل تهران…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17707" target="_blank">📅 21:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17706">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این مدل اجبار قهری برای عقد توافقنامه عملاً یک نوع Duress است و پیمانی که در چنین شرایطی امضاء بشود بعداً میتواند براحتی لغو بشود.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17706" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17705">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ترامپ:   دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17705" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17704">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ :
«اگر به نتیجه برسد، من اعتبارش را می‌گیرم. اگر به نتیجه نرسد، جی‌دی را مقصر می‌دانم.»
«بهتر است مراقب باشی، جی‌دی!»
«او هواپیمایش را برمی‌گرداند و از اینجا گم می‌شود.»</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17704" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17703">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مقام ارشد آمریکایی درباره متن  رسمی تفاهم‌نامه ایران   -ما شاهد توقف تلاش‌های ایران برای قطع تردد در تنگه هرمز پیش از  امضا هستیم  - ایران اعلام کرده است که ذخایر اورانیوم غنی‌شده خود را نابود خواهد کرد و نحوه انجام این کار  - اگر به توافق نهایی برسیم و اگر…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17703" target="_blank">📅 20:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17702">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقام ارشد آمریکایی درباره متن
رسمی تفاهم‌نامه ایران
-ما شاهد توقف تلاش‌های ایران برای قطع تردد در تنگه هرمز پیش از
امضا هستیم
- ایران اعلام کرده است که ذخایر اورانیوم غنی‌شده خود را نابود خواهد کرد و نحوه انجام این کار
- اگر به توافق نهایی برسیم و اگر ایران رفتار کند، اجازه لغو تحریم‌ها را خواهیم داد
- ایران موافقت می‌کند که حداقل ذخایر اورانیوم غنی‌شده خود را از طریق رقیق‌سازی از بین ببرد
- توالی مراحل توافق‌شده موضوع مهمی در مذاکرات آینده با ایران خواهد بود
- پس از مسئله هسته‌ای، در مورد تأمین مالی نیروهای نیابتی بحث خواهیم کرد
- جلسه این آخر هفته در سوئیس برای بررسی چگونگی پیشرفت مذاکرات با ایران "حیاتی" خواهد بود
- ما کارهایی را برای ایجاد اعتماد انجام خواهیم داد و خواهیم دید که آیا می‌توانیم به توافق برسیم
- نتانیاهو درخواست نسخه‌ای از تفاهم‌نامه نکرده است
- اگر نتوانیم به توافق برسیم، ترامپ از استفاده از ابزارهای خود نمی‌ترسد
- تماس بسیار مداومی با اسرائیل داشته‌ایم
- تفاهم‌نامه امضا شده است اما هر یک از طرفین می‌توانند تا زمان حصول توافق الزام‌آور، از آن خارج بشوند</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17702" target="_blank">📅 20:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17701">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خب خدا را شکر نشست خبری بی پدر تمام شد….
به همه توهین کرد، از سعودی و ایرانی تا اروپایی و افغان!</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17701" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17700">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ درباره حماس:
آنها وقتی به دنیا می آیند یک مسلسل در دستشان است.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17700" target="_blank">📅 20:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نقش پنهان امارات در جنگ شامل ده‌ها حمله به ایران   به گزارش وال استریت ژورنال، امارات متحده عربی ده‌ها حمله هوایی علیه ایران را از روزهای اولیه جنگ آغاز کرد و تا روز پس از اعلام آتش‌بس ادامه داد،  درگیری عمیق‌تری که تاکنون در کمپین هوایی تحت رهبری ایالات متحده…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17699" target="_blank">📅 20:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17698">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ فاش کرد که حملات و بمباران‌های ایالات متحده بیش از ۱ تریلیون دلار به ایران خسارت وارد کرده است.
«بازسازی آنها ۱۵ تا ۲۰ سال طول می‌کشد. بنابراین باید خودشان رفتار کنند. اگر رفتار خوبی نداشته باشند، دوباره ضربه می‌خورند.»
ترامپ همچنین تأیید کرد که ایالات متحده حتی یک دلار هم برای بازسازی به آنها نخواهد داد.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17698" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17697">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: ما در مورد موشک‌های بالستیک و نیابتی‌های تروریستی صحبت خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17697" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ: ما در مورد موشک‌های بالستیک و نیابتی‌های تروریستی صحبت خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17696" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏
ترامپ:
دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17695" target="_blank">📅 19:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اینکه با جنگنده باستانی اف-۵ که بزور نسل ۳ است و همان زمانی که نو هم بود عملکرد خوبی نداشت بتوانی به پایگاه نیرومندترین ارتش جهان آسیب بزنی را فقط با هنر خلبان ایرانی می‌توان توجیه کرد.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17694" target="_blank">📅 19:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگر ایلان ماسک یک تریلیون دلار از دارایی‌هایش را از دست بدهد، همچنان ثروتمندترین فرد جهان خواهد بود.
سبحان الله!</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17693" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17692">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایالات متحده، ایران و میانجی‌ها در حال بحث درباره برگزاری امضای یادداشت تفاهم هستند که در حال حاضر برای جمعه برنامه‌ریزی شده است، و ممکن است همین چهارشنبه برگزار شود، طبق گفته یک دیپلمات از یکی از کشورهای میانجی و یک منبع دوم آشنا با مذاکرات - Axios|</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17692" target="_blank">📅 18:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17691">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ایالات متحده، ایران و میانجی‌ها در حال بحث درباره برگزاری امضای یادداشت تفاهم هستند که در حال حاضر برای جمعه برنامه‌ریزی شده است، و ممکن است همین چهارشنبه برگزار شود، طبق گفته یک دیپلمات از یکی از کشورهای میانجی و یک منبع دوم آشنا با مذاکرات - Axios|</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17691" target="_blank">📅 18:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17690">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aaa93f21f.mp4?token=MOg_wZBNGI-vUtbjpRzn5UHOtCoe0EfjnfTbFBcBVwci8EjdCE-EOjgUEzREKZuxVXQ6hRcxfaz0ctfdKRv3jkXlX7ATFWFeCOzaWWvnn0rKHvkO1YyBZYdMik4LtzC0p3PsF2ujXW0IMkBD4B_KbXVr89V7IblrXOWPXYz4Pmsua6LiMOlhKtLBKAri69hASADhovSOt48ZSXTwpcPmPb6DD4Fp8KbXXF_FZR19waEaxsqFLDebTWFVc-Tz7LKLCYAZfnGqptImPvjlLimH0o7db1YHT6ZEIm1NN0WOIVBcHmG_NO9dWxdxn1OKhU8H4LFL5YOsXO2nzDxwxQ6e4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aaa93f21f.mp4?token=MOg_wZBNGI-vUtbjpRzn5UHOtCoe0EfjnfTbFBcBVwci8EjdCE-EOjgUEzREKZuxVXQ6hRcxfaz0ctfdKRv3jkXlX7ATFWFeCOzaWWvnn0rKHvkO1YyBZYdMik4LtzC0p3PsF2ujXW0IMkBD4B_KbXVr89V7IblrXOWPXYz4Pmsua6LiMOlhKtLBKAri69hASADhovSOt48ZSXTwpcPmPb6DD4Fp8KbXXF_FZR19waEaxsqFLDebTWFVc-Tz7LKLCYAZfnGqptImPvjlLimH0o7db1YHT6ZEIm1NN0WOIVBcHmG_NO9dWxdxn1OKhU8H4LFL5YOsXO2nzDxwxQ6e4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">—  ترامپ درباره مودی نخست وزیر هند:  «او زیباترین مرد است. او مثل فرشته است. اما در واقع، او یک قاتل است.»</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17690" target="_blank">📅 18:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17689">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl66I68tmjWlD1_ZdeoYlfpoMpW37I_YSpUzw7ZBDi8do2FMi0jA9Xx-MdNot-i735RSCJqKuwcrJoNlh-qEuFPCgkY9KmBI_yOk7cUIiCKekxZRvZ6heqSj2vw1zVn_4CYBc9FoM_9XM3TM8VG6Z8ti1yaJ63fONXUQ3jV-aknBY_nikwr8WeX6a_Aen3NRfxPNnYy6fZ3l3-so5fkpmMksHcWyeHijDB6g8BbKeINhtNl1qiiUQ5r7urQVi_b8b7j55xnsP992wEhD2Wmjt7nO0HbloZVWOibz8PbItyM7WzhTHtwyKRAZTYHFeIWYUzUOsJhemY0m9zU5a2D4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">—  ترامپ درباره مودی نخست وزیر هند:  «او زیباترین مرد است. او مثل فرشته است. اما در واقع، او یک قاتل است.»</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17689" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17688">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">—  ترامپ درباره مودی نخست وزیر هند:
«او زیباترین مرد است. او مثل فرشته است. اما در واقع، او یک قاتل است.»</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17688" target="_blank">📅 18:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">موجودی نفت به کمترین سطح بحرانی در بزرگترین مرکز ذخیره‌سازی ایالات متحده سقوط کرد.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17687" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQxYMfe3JJWXCAX_XBZmHe-Ptm2FQyc9dSzfBBxkAJRB-MWacgeyeAYt4bKpSJC9NephnRxAhI-IyT4p8eGHSwlXndI5VVL-spZsAN3dq_MDwDODYh_RyIpRf6kzJaJaXxRZNs-TsplldAwb6_neKU4p1EgVaTrsoiLoMIowWZVhX4iErIOxlxuO7Sj7HNgXrpzVhzqAxy1A3GCQqgwcPZKF44DqNIq2UsS9CagLSmIE_xvMvgnqN-lA5KpvqBvU_wXFI-kuGewvCbP-abt5Pm1g2efjKDLhV6cmyCeNks3e52cs9hOK1nOtq0aY9U7jM-HaR68QuXp85UerQInodQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفوگرافی موسسه مطالعات جنگ از ابهامات و اختلاف روایات بندهای توافقنامه ایران و آمریکا</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17686" target="_blank">📅 17:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔹
سفر هیات ایرانی به ژنو لغو شد</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17685" target="_blank">📅 17:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17684">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">توصیه ام به شیربچه های دیپلماتمان این است که اصلا حضوری به ژنو نروند و به همان امضای الکترونیک بسنده کنند!  واقعا یک خودکار یا خودنویس حتی اگر از طلا هم باشد به احتمال لواط زوری با این ماموت کله زرد نمی ارزد  سبحان الله!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17684" target="_blank">📅 17:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17683">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ونس ترنس:   طرف پاکستانی از ما خواست که متن کامل یادداشت تفاهم را برای مدتی منتشر نکنیم.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17683" target="_blank">📅 16:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17682">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ونس ترنس:
طرف پاکستانی از ما خواست که متن کامل یادداشت تفاهم را برای مدتی منتشر نکنیم.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17682" target="_blank">📅 16:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17681">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تشدید حملات اسراییل در جنوب لبنان و تصرف شهرک الحدثه!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17681" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17680">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عراقچی گل!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17680" target="_blank">📅 16:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17679">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حاج عباس حتی زبان بدنش هم کلاس درس است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17679" target="_blank">📅 16:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17678">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">توصیه ام به شیربچه های دیپلماتمان این است که اصلا حضوری به ژنو نروند و به همان امضای الکترونیک بسنده کنند!  واقعا یک خودکار یا خودنویس حتی اگر از طلا هم باشد به احتمال لواط زوری با این ماموت کله زرد نمی ارزد  سبحان الله!</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17678" target="_blank">📅 16:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17677">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ می‌گوید در هتلی با رئیس‌جمهور مصر ملاقات کرده و آنها «عمیقا عاشق هم شده‌اند»</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17677" target="_blank">📅 16:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17676">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ می‌گوید در هتلی با رئیس‌جمهور مصر ملاقات کرده و آنها «عمیقا عاشق هم شده‌اند»</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17676" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17675">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چرا قطر بقای خود را مدیون جمهوری اسلامی است؟  ترامپ در سفر اخیرش گفته بود:  ایران به دلیل وجود امیر قطر، خیلی خوش شانس است. امیر قطر در حال مبارزه برای دست یابی به توافق هسته ای با ایران و عدم حمله به این کشور است. ایران خوش شانس است که امیری در قطر دارد که…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17675" target="_blank">📅 15:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17674">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbDi0-Bg9s1zsG1ajkfvgmR_Sq4OePpMlZ4y4pBrNNkeBuOZHMibCA7CvveoO2JtevUcvJn5iAq_SV9_iXPosCv9MGuPt9YDbEVFkvLkTVYsPePgu1-TTdPgIu3KZQ1dyynbNmQnMJS-X1-WjOtT4e0oLb3MQoSA1OORGQTWYtcfbCth0oBS6KTlbD0MvUKpT_FPAY79_GRsmi0cCt6dq5LxrQOPtDy1oMg5stx0mA4Civ5OYCGW6rNFigYLgNi8WYeZkanAhELlymTmuQnqZIiJV2gmMRELn72mMHdznk4dv9QJpivmu-xIk8suITWlkrOplLfvnxAXiq2dEwAvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی کانالهای ایرانی خبر داده اند که قطری ها برای راضی کردن ویتکاف و کوشنر جهت فشار بر ترامپ برای پرهیز از جنگ دوباره و امضای توافق، یک هتل نیمه کاره 5-ستاره در دوحه را به این دو نفر هدیه داده اند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17674" target="_blank">📅 15:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17673">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ:   ایالات متحده صندوقی برای سرمایه‌گذاری در ایران ندارد  تفاهم‌نامه ایران نهایی نیست  اگر آنچه می‌بینم را پسندیدم، دوباره حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17673" target="_blank">📅 15:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17672">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ:
ایالات متحده صندوقی برای سرمایه‌گذاری در ایران ندارد
تفاهم‌نامه ایران نهایی نیست
اگر آنچه می‌بینم را پسندیدم، دوباره حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17672" target="_blank">📅 14:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17671">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔵
پاول دوروف ؛ مالک تلگرام
:
دولت بریتانیا می‌خواهد استفاده از شبکه‌های اجتماعی را برای کودکان زیر ۱۶ سال ممنوع کند.
اما ممنوع کردن شبکه‌های اجتماعی برای کودکان فقط آن‌ها را در معرض خطر بیشتری قرار می‌دهد.
آن‌ها مجبور خواهند شد از VPN استفاده کنند و به محتوای غیرقانونی بسیار بدتری دسترسی پیدا کنند.
ما قبلاً این را دیده‌ایم.
وقتی دولت روسیه تلگرام را ممنوع کرد، ۹۵٪ نوجوانان روسی همچنان از آن استفاده کردند. آن‌ها فقط به VPN منتقل شدند. همین‌طور در ایران</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17671" target="_blank">📅 13:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17670">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMeRvYDV2l5B5aY-V-3ne2ZEBBB-V020ajuKAdBXqKbtKXjGnz28M8Rb39OenH-xJZSvOir9TwlRL1Z-SiBCmn0oykE2HyIJHGPupH6adjKZzj8aMFe42SWAowpkSlNnJO7ZLkShmBLyIX8k4tz-zl8iQSAZ1YgzfqrWP4flSNV7NyoPBrUdSE5IiAKfOygjVFPon8Rp0DqBZZr0jb0Ta2n9gkis_0jeg2q1-xug8R48_1vJbaf953-ZKgqB4gCfEmjV42CSi9eJj220iHQeA3gUQgZJ8xqdznHYmZbuwRDi7JerEU-o6gPx6MUCiLBd_BqfY41W_62UO3c0v2aidQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای باری نظامی امارات در پایگاه نواتیم اسرائیل فرود آمد
در ۱۵ ژوئن ۲۰۲۶، یک هواپیمای باری ایلوشین Il-76TD متعلق به امارات از ابوظبی به پایگاه هوایی نواتیم اسرائیل پرواز کرد. این پرواز از حریم هوایی عربستان عبور کرد.
این رویداد، نشانه‌ای از همکاری نظامی رو به گسترش و عمیق‌تر امارات و اسرائیل در برابر تهدید موشکی و پهپادی ایران است. پایگاه نواتیم یکی از مراکز کلیدی نیروی هوایی اسرائیل است.
گزارش‌ها همچنین حاکی از استقرار سیستم
گنبد آهنین
اسرائیل و پرسنل نظامی آن در امارات پس از حملات ایران است. این پرواز احتمالاً برای انتقال تجهیزات، مهمات یا لوازم پشتیبانی دفاع موشکی انجام شده.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17670" target="_blank">📅 12:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17669">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نمودارهای برگرفته از سایت شرطبندی Polymarket نشان‌دهنده سقوط چشمگیر شانس‌های انتخاباتی بنیامین نتانیاهو در ماه‌های اخیر است.   خط زرد (احتمال نتانیاهو به عنوان نخست‌وزیر بعدی) از حدود ۵۰-۶۰٪ در فوریه با نوسانات اولیه به اوج می‌رسد، اما از اواخر مارس با شروع…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17669" target="_blank">📅 12:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17668">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bj3Za4adQhXY7-5zwdtbVYWTq3ihe58DsHvirw6KT8FLOuQ_9dcBQqjbdpOVeh_8x7HyAiBp2-17fE_ChVq_W1VXsZT-27aLxdZoku-mTi4bVj8JUBitJDaE1pOMgZr_05sAtxN_AFV8gyNxYVZ0xUYqBK2zgXI8Wt46Jq5zKAqQFm3v7t1E9vugFRNMZVRu6JzwR93E4LG1OsIuFNK47PLq_YSohTRxBrirsFJB9Kjdef1o7D8y66YdayBIenuiWptqmwgxKg9dN5kP2boUDoH9fXgGT3SZQfAG3T1h5Sr8Z6I_4f1CBXnMJpkpb28Jc2o5HitCLnvEDkB55zfK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودارهای برگرفته از سایت شرطبندی Polymarket نشان‌دهنده سقوط چشمگیر شانس‌های انتخاباتی بنیامین نتانیاهو در ماه‌های اخیر است.
خط زرد (احتمال نتانیاهو به عنوان نخست‌وزیر بعدی) از حدود ۵۰-۶۰٪ در فوریه با نوسانات اولیه به اوج می‌رسد، اما از اواخر مارس با شروع یا تشدید درگیری‌های مرتبط با جنگ ایران، به شدت افت کرده و به حدود ۲۵-۳۰٪ در ژوئن رسیده است.
این سقوط با منطقه زمانی خاکستری “جنگ ایران” همخوانی دارد که از اواخر فوریه تا ژوئن را پوشش می‌دهد.
در مقابل، خط آبی نفتالی بنت (حدود ۲۰-۴۰٪) نوسان داشته اما اخیراً پایدارتر است. خط سبز گادی ایزنکوت از نزدیک صفر شروع کرده، به تدریج افزایش یافته و در ژوئن به حدود ۳۵٪ رسیده و حتی از نتانیاهو پیشی گرفته است.
این روند نشان‌دهنده نارضایتی عمومی اسرائیلی‌ها از نتیجه جنگ ایران است؛ افکار عمومی معتقدند اهداف اصلی (مانند نابودی کامل برنامه هسته‌ای و نیابتی هایش) محقق نشده و این امر به ضرر نتانیاهو تمام شده است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17668" target="_blank">📅 11:20 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
