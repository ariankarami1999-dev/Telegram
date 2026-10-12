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
<img src="https://cdn4.telesco.pe/file/c6jDA7oCxujPTFyqkEY6q03e8wj-kl6GB-RqIqMEdA9XHrEfTlWyt0TGwvccepL_c3_jemkPbHlC8j-ConfxZhvJLAV_yV0k3MzEL5woUYgVTbD3sJMRS9eVGtkVQupyObw-K5KEMKJPdA5M4xz3GYBM4VMHBZGKDaLpFIm27zv3lcCO0HaXkzyOSH1mbqNS8ZFkxGOAhr9CeZQkkbQJ59Zruni6dOYUyMZ318RKQ1DODnmS0npVUKS0yOVuwj_i6TY2GKub8n_OqXL9M02yXateqYZQUhD-scbw1Mzssl3EHnzYLLQBZjKEHKgPiQQiPpzizUPQ_jWb1YeQAmNkLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 495K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ممکن است آمریکا در تلاش باشد ایران را به حمله اول تحریک کند
آلن ایر، عضو سابق تیم مذاکره کننده آمریکا نوشت: ممکن است آمریکا در تلاش باشد ایران را به حمله اول تحریک کند. احتمال انجام دور دیگری از حملات آمریکا علیه ایران بسیار زیاد است‌. با انتقال تجهیزات و نیروهای نظامی بیشتر آمریکا به منطقه و انتشار گزارش‌هایی درباره فعالیت هواپیماهای اسرائیلی در نزدیکی حریم هوایی عراق، این احتمال وجود دارد که  واشنگتن عمداً در حال آزمودن آستانه تحمل تهران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/withyashar/25502" target="_blank">📅 20:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25501">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امانی ، سفیر پیشین رژیم در لبنان : قرار بود پیجرها بررسی شود و برای همین عملیات را زودتر اجرا کردند
@WarRoom</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/25501" target="_blank">📅 20:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYYKh0ZeUwG65re8YSEkBq_PUaM7fUU0m0DlzecCkCV9XTJvs9ph14Jcps_BE5j2LxGl3ewBP0X74hHE9sPMkGCft15oHkMUd9EiPD_n9ZfEbL1TbpFVoL0hQ8gmxaLCqFLaUOe3lc6NAkOkHAuYUPMj0BD2jn2AeRCfwZnQ-gcbIxWkLRkKhJ9Gr5vgxdUOpGrPcj5zaFfuYXvqZ8VXP1LD1fUBS6VsYnHQP8t7s142CI--UgvSuGT5vuMep-F4O0q3vwCDP8h639wbZtbW-MC3o-oI1oWxWvvEKQ82hpPcEvGsK7-hJUxpz1gdDYwUW0EhXOUYzZNttIugGmg71A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث، وضعیت ۱۵۹ کشتی نیروی دریایی جمهوری اسلامی. در زمان ترامپ : کف دریا در زمان دیگر رئیس‌جمهورها: روی آب.
@WarRoom</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/25500" target="_blank">📅 20:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بریتانیا، روح‌الله بازقندی (رئیس پیشین اداره ضدجاسوسی سازمان اطلاعات سپاه پاسداران) و شهرام علیرضا تمرزاده جکی را به دلیل اتهامات مربوط به مشارکت در فعالیت‌های اطلاعاتی سپاه پاسداران انقلاب اسلامی و توطئه‌هایی که افراد یا دارایی‌ها در بریتانیا و سایر کشورها را هدف قرار داده‌اند، تحریم کرد.
‌اندی برنهام در سخنرانی خود در مجلس عوام بریتانیا راسمأ اعلام کرد ارزیابی‌ها نشان می‌دهد که حمله به پایگاه هوایی فیرفورد به در ایران هماهنگ شده و هدایت آن به طور قطع توسط سپاه صورت گرفته است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/25499" target="_blank">📅 19:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بیانیه ۲۹ کشور از جمله انگلیس و آمریکا: ما یافته‌ های بریتانیا را درباره دست داشتن ایران در حادثه پایگاه فیرفورد تأیید می‌کنیم. حملات ایران، حملات سایبری و فعالیت‌ های ترکیبی آن را محکوم می‌کنیم. واقعه فیرفورد آمادگی سپاه پاسداران را برای انجام حملات فرامرزی نشان می‌دهد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/25498" target="_blank">📅 19:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر امور خارجه بریتانیا: ما دو شهروند ایرانی را در فهرست تحریم‌ها قرار دادیم، زیرا آن‌ها در فعالیت‌های خصمانه به نمایندگی از رژیم [ایران] نقش داشته‌اند.تلاش‌های ایران برای تضعیف امنیت بریتانیا و متحدانش از طریق شبکه‌های جنایی و گروه‌های خود، غیرقابل قبول است. ما با هیچ تهدیدی علیه خاک خود مدارا نخواهیم کرد و سفیر ایران را احضار کردیم تا این پیام را به او منتقل کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/25497" target="_blank">📅 18:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آسوشیتدپرس: رسانه‌های وابسته به حوثی‌ها مدعی شدند حملات هوایی به دو منطقه در صنعا، پایتخت یمن، یک کشته و ۱۲ زخمی بر جا گذاشته است؛ از جمله در یک کارخانه نمک و یک منطقه مسکونی. حوثی‌ها عربستان را مسئول این حملات معرفی کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/25496" target="_blank">📅 18:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز، درباره حادثه امنیتی در مرز لبنان :
«در غم سنگین خانواده پسری که در جریان یک گردش در نزدیکی مرز شمالی، بر اثر انفجار جان خود را از دست داد، شریک هستم و برای همه مجروحان آرزوی بهبودی سریع و کامل دارم.
@WarRoom</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/25495" target="_blank">📅 18:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تتر و دلار ۲۶۱،۰۰۰ تومان
🔻
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/25494" target="_blank">📅 18:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5f3a421c.mp4?token=ltYC9xwuCi0RDLgbDwZDbel7g1mBdk9tdm3CJs5erd4daeVvzD7trQO0DbBDcTm99VhHjyxxBnk0y6DFXtcis5ySoGJdPkSu3Sl4NRelZoVIEnMZ32M6yL1L8IianNmnykGiOKuZK-RxPIE1KtX9uSG3aeiaYoOJzEgbLBNygIlcXD_Otj0wNnXvyBf6WpUsaMdBQoYERimVar646ooJvX56Ha6KQp91_HpMTeDD_i2N1zW2THbCZoVoUmYCBlbLeZa0J_-gUKSQxWvXfJxVLX5fSfQtlP-EOxAjVgNiyXjSfZZAM1yuFqmhxCEbqHcOpNISmLIIeLKL6iGtjY076g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5f3a421c.mp4?token=ltYC9xwuCi0RDLgbDwZDbel7g1mBdk9tdm3CJs5erd4daeVvzD7trQO0DbBDcTm99VhHjyxxBnk0y6DFXtcis5ySoGJdPkSu3Sl4NRelZoVIEnMZ32M6yL1L8IianNmnykGiOKuZK-RxPIE1KtX9uSG3aeiaYoOJzEgbLBNygIlcXD_Otj0wNnXvyBf6WpUsaMdBQoYERimVar646ooJvX56Ha6KQp91_HpMTeDD_i2N1zW2THbCZoVoUmYCBlbLeZa0J_-gUKSQxWvXfJxVLX5fSfQtlP-EOxAjVgNiyXjSfZZAM1yuFqmhxCEbqHcOpNISmLIIeLKL6iGtjY076g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی تروریستی سپاه اعلام کرد طی دو روز گذشته، سومین نفتکش بزرگ را در تنگه هرمز هدف قرار داده که در پی آن، کشتی دچار آتش‌سوزی شده است.، این نفتکش هنگام تلاش برای خروج غیرمجاز از تنگه هرمز، سامانه ناوبری خود را خاموش کرده و با وجود چندین بار هشدار، به مسیرش ادامه داده است
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/25493" target="_blank">📅 17:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چندین پرتاب موشک بالستیک از شهر های : یزد، اصفهان و کرمانشاه گزارش شده است. به نظر میرسد تمرینی و برای بازدارندکی و رخ نمایی توان باشد
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/25492" target="_blank">📅 17:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25491">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d4c1ebf1.mp4?token=tkkzkxywEeLqDdK1YbJ4efStmZF3n8KrDnCaxjUqHps6BdvWbUS7pFowQ_t0EbE-wf9Wr501Vaf5jfjMIlq_ZdoQo-WGvpEilRqUjLfKP5m1Tg51KYkjHzEo_98x-y4Uv18u5OcjeQwf4Hkt7koAjsDlEom6u1x6PpPhjJHoxPec-g0ojOdA9fhzQssWhR8Caii2hmIWG3rQ7n3SsD-pQei2vGHJI8xiFi2AAl-viRvNmCivNXgC8hZVmyN0bp8c38UsQ7chBZR58NygsCvmp-8y7-FhQcdjnlJzRucL9_dWq4-lrzVaDZXe0WB_V1O67sPp4DXaIg-EPMeKbsTMlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d4c1ebf1.mp4?token=tkkzkxywEeLqDdK1YbJ4efStmZF3n8KrDnCaxjUqHps6BdvWbUS7pFowQ_t0EbE-wf9Wr501Vaf5jfjMIlq_ZdoQo-WGvpEilRqUjLfKP5m1Tg51KYkjHzEo_98x-y4Uv18u5OcjeQwf4Hkt7koAjsDlEom6u1x6PpPhjJHoxPec-g0ojOdA9fhzQssWhR8Caii2hmIWG3rQ7n3SsD-pQei2vGHJI8xiFi2AAl-viRvNmCivNXgC8hZVmyN0bp8c38UsQ7chBZR58NygsCvmp-8y7-FhQcdjnlJzRucL9_dWq4-lrzVaDZXe0WB_V1O67sPp4DXaIg-EPMeKbsTMlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک جانسون: همه منتظر نتیجه انتخابات آمریکا هستند
حاکمان ایرانی‌ها این دوره انتخاباتی را زیر نظر دارند و می‌خواهند به رئیس‌جمهور و چهره سیاسی او آسیب بزنند و فکر می‌کنم این موضوع عامل مهمی در ماجراست.
پس از انتخابات، فکر می‌کنم وارد مرحله‌ای کاملاً متفاوت خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/25491" target="_blank">📅 17:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ایران برای دست‌یابی به سلاح هسته‌ای تلاش می‌کند، اما ما رژیم حاکم بر ایران را سرنگون خواهیم کرد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/25490" target="_blank">📅 16:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بیست دانش‌آموز کوهنورد بر اثر انفجار یک مهمات عمل‌نکرده در نزدیکی مرز شمالی اسرائیل مجروح شدند. به گفته سازمان «مگن دیوید آدوم»، یک کشته و حال دو نفر دیگر نیز وخیم گزارش شده است. پدر یکی از کودکان مجروح چنین روایت کرد: «این گروه کوهنوردی مربوط به دانش‌آموزان مقطع راهنمایی بود و بچه‌ها آسیب دیدند. لطفاً برایشان دعا کنید؛ این مهم‌ترین مسئله است. این اردو برنامه‌ریزی و تأیید شده بود و همه هماهنگی‌ها انجام گرفته بود؛ تمام والدین فرم‌های مربوطه را امضا کرده بودند. متأسفانه مهمات عمل‌نکرده‌ای در منطقه وجود دارد و به نظر می‌رسد فردی به‌طور تصادفی با یکی از آن‌ها تماس پیدا کرده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/25489" target="_blank">📅 16:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حیوانات باغ‌وحش دزفول دزدیده شدند ,
فرمانده انتظامی دزفول از دستگیری چهار سارق و دو مالخر در کمتر از ۴۸ ساعت خبر داد.
این افراد چند رأس بز کوهی کمیاب را از باغ‌وحش دز سرقت کرده بودند.
در بازرسی از مخفیگاه متهمان، ۶ رأس بز کوهی کشف شد که یکی از آن‌ها سلاخی شده بود. پنج رأس بز کوهی نیز به باغ‌وحش بازگردانده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/25488" target="_blank">📅 16:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcOGKYpZXdJzYAi_CmEAZWfVOpNFlKH9W9OkJHfPo0Ev-mULVXqiAxUdfcuUHmw1fJ2HwKeYxROeS1NQZYX_S7qok_E41qCxCVIuWT5FKJSgZhuYMgu8qjMULS46HQuQ79R18vpu_hIIsUdezRi2msOcXkNND5rwO7UyH-xdQXn49S4__mKi3eQ8ffgqcr8SwskD4_HLie8prURGyeC29HFNqikQzVjabgPHflY033PaGLQuJtutzgIK-6s0uf5rWjEzth3wCs1Sfr8OXTA7SoRcZMFHqBihrNted2Wiumn7iUJ_OKnCFRL5OMNU6iqLrHHA-A-fwNP-FhTv7HX_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ چینی نشان می‌دهند که ناو آبی‌ـ‌خاکی
یواس‌اس میکین آیلند (LHD-8)
در کنار یک ناو ترابری آبی‌ـ‌خاکی از کلاس سن‌آنتونیو، در پایگاه مشترک پرل هاربر–هیکم در هاوایی پهلو گرفته
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/25486" target="_blank">📅 15:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7-QoqzmAPQ2cKfrHtXNEcujmKtlRXU0aP_FhO7Z9fjZ2UhABjRS1x0ax-U8SBYF2p6VCdea61xlITnkkcpZZTgDaqCm6DUoX9KDHO4-FJcyP6lbzh23AkBUClYv5naauZxqHnKlc2SGVSbsBtXxM8DuQ8Ze9l_a4ltLwC66uWet6XAWIVU7RWmoODFynQ7XZQlQfCAw0hlr4S15swi7wNGeRy2n-T8T3qn_RGgHsDH8zCPGhLfnCZPIYSPlA4gOWeAkSTqJc3Fty-2xcDVXpozeQIpPZx59A6KjBrXH-07DVy4agQkpv6qBy1_00W_Xv6I85Cu6VzKeBJx6u46Ygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ فروند پی۸ پوسایدون در حال حرکت و انجام مأموریت در ابتدای دریای عمان نشانه‌ای از جابه‌جایی یا تغییر موقعیت یکی از دو گروه نظامی:
گروه آبی ـ خاکی آبی‌خاکی (ARG) یا گروه ضربت ناو هواپیمابر (CSG)
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/25485" target="_blank">📅 15:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCUZGNEz_N3LCnDUyN6D56s4FkMbh4OcpfoyQyagdLzT38aNmK9WQefWqkYNgKua_WI-z0k8EOjmeYWBPXDmPNUfOrc9FBrFXTMEvcQr9q63JyxbLg9twxor9a3Ujy7d3WrCxk326wVfGt4qgbhTx3pI12OWx6Trc2OVpa9osh8rz38dOwYdPkxZZe-AQulYbDKASYobllngLWlZ8gStU4Oo4WRKwEShJmVCgTWn0ow_XE1KdUUA52Wytkj3AW1riRYIOAS24Aq2xzRK356A2f1ds54d8AM1O8SYYFrOfGCEAhiK2NCc16SnoJ8vuclbdynVfWJLjjYt0stYvPsa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تصویر از مهرداد اخلاقی کتابچی، وزیر پیشنهادی دفاع و پشتیبانی نیروهای مسلح
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/25484" target="_blank">📅 15:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرگزاری معاریو: برآورد نهادهای امنیتی نشون میده اگر ایران [به اسرائیل] حمله نکنه رویارویی به بعد از انتخابات موکول خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25483" target="_blank">📅 14:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏رابرت ای. هال، استاد دانشگاه استنفورد و مایکل وودفورد، استاد دانشگاه کلمبیا، برنده جایزه نوبل اقتصاد سال ۲۰۲۶ شدند. این دو نفر در تحقیقات خود نشان داده‌اند که برای درک تحولات اقتصاد کلان، نمی‌توان تنها به شاخص‌هایی مانند تورم، تولید و مصرف تکیه کرد، بلکه باید رفتار و تصمیم‌گیری خانوارها و بنگاه‌های اقتصادی را نیز در نظر گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25481" target="_blank">📅 14:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25480">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏سخنگوی کرملین گفت که اگر اوکراین واقعا خواهان برگزاری انتخابات باشد، روسیه در روز انتخابات هیچ حمله‌ای به اوکراین انجام نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25480" target="_blank">📅 14:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کانال ۱۳ اسرائیل : نتانیاهو شب گذشته در نشستی اضطراری با مقام‌های ارشد امنیتی ،حمله نظامی به ایران را بررسی کرد
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25479" target="_blank">📅 14:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ایفدانا، رسانه رسمی سازمان غذا و دارو: مهدی پیرصالحی، رئیس سازمان غذا و دارو، اعلام کرد مشکل انتقال دارو از هند به ایران ناشی از محدودیت‌های حمل‌ونقل در شرایط جنگی بوده است. به گفته او، به پروازهای ایرانی در برخی مسیرها اجازه پرواز داده نمی‌شد و اختلال در مسیرهای دریایی نیز انتقال محموله‌ها را دشوار کرده بود. او تأکید کرد که هند در زمینه تأمین و فروش دارو همکاری مناسبی با ایران داشته است؛ بنابراین، نسبت دادن مشکل صرفاً به مخالفت هند با ارسال دارو، با توضیحات رسمی سازمان غذا و دارو مطابقت ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25478" target="_blank">📅 13:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MccqteT8mHOO0oeDIGV9yc5hnbnBreK2hmalCGzSuDaOD_nZFaiVEolmKA6P7V_p5uNl9NjgQL2fDin7ZHBX3jdUBiiVtPpXoYHuxl5ATjetxBrwJo3HzU6VvM9qZjX5-gG6tbERS65OkpdNBwrSsKAaEBlwkFWNR4EYS916B0L2dcK108BOp1RRyFy6hW6QUpLmMyvzOkGn7QMFY6TDHi2yLp-C0mWlU4NEFX9Z6fE-OSB4TIqdsCooeqRLJB0o8esnWeLuvKBwlaVFVcTNmpKvHHZ2tvHVj2jl1D11PDPtUb8YDSgY-lheBd5hZbPsyNINR74sQunXXCoodomRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : تصویر ماهواره‌ای نمایی از تأسیسات موشکی قم را با حدود ۵۰۰ زاغه ذخیره‌سازی مهمات نشان می‌دهد.
این سازه‌های برآمده پناهگاه‌های ضدبمب بتنی موسوم به «ایگلو» هستند. هر واحد بتنی زیر تلی از خاک بومی پوشانده شده است. دهانه‌های مستطیلی خاکستری در تصویر، ورودی کامیون‌ها و تجهیزات لجستیکی هستند.فواصل منظم این سازه‌ها مانع از انفجار زنجیره‌ای بر اثر حمله می‌شود . پوشش ضخیم خاکی تخریب ناشی از ترکش و ضربات هوایی را به حداقل می‌رساند . این انبارها محل ذخیره کلاهک‌ها، سوخت جامد و راکت‌ها هستند. تمام این زاغه‌ها از طریق شبکه جاده‌ای اختصاصی به شهرهای موشکی زیرزمینی کوهستان متصل می‌شوند.
لوکیشن ها :
‏34.893496,50.788559
‏34.906500,50.793314
‏34.900907,50.811569
‏34.921643,50.801991
‏34.931112,50.749336
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25477" target="_blank">📅 12:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فایننس‌فیدز : قیمت بیت‌کوین در معاملات امروز تا این لحظه حدود ۸۳٬۷۷۰ دلار بود و در ۲۴ ساعت گذشته حدود ۰٫۷۳ درصد رشد داشت. صندوق‌های اسپات بیت‌کوین آمریکا در جمعه ۹ اکتبر ۲۱٫۱ میلیون دلار ورود خالص سرمایه ثبت کردند؛ این رقم پس از خروج ۲۴۴٫۱ میلیون دلاری روز پنجشنبه به دست آمد. بااین‌حال، در کل هفته ۵ تا ۹ اکتبر، صندوق‌های بیت‌کوین حدود ۶۷۸٫۹ میلیون دلار خروج خالص سرمایه داشتند. بنابراین، ورود سرمایه روز جمعه هنوز برای تأیید بازگشت تقاضای نهادی کافی نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25476" target="_blank">📅 12:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای برای یک نفت‌کش در نزدیکی لنگرگاه «صحار» در عمان دریافت کرده است. پس از تأیید اصابت یک پهپاد (UAV) به نفت‌کش، UKMTO ماهیت این حادثه را به «حمله» تغییر داد. مقامات محلی در حال همکاری برای…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25475" target="_blank">📅 12:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">لحظه ‎صادر کردن دستور یک حمله تلافی‌جویانه قاطع علیه حوثی‌ها توسط محمد بن سلمان، ولیعهد عربستان سعودی @WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25474" target="_blank">📅 12:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این آقا امروز به‌خاطر جوابی که در مناظره‌اش با نامزد دموکراتها داد ستاره شده. یعنی حتی حریفش
سناتور کوری بوکر (دموکرات)
هم چنانکه در آخر این کلیپ می‌بینید مات و مبهوت ماند و میگوید «واو»
مجری مناظره : اگر رئیس‌جمهور با شما تماس بگیرد و بگوید: «هر کاری بخواهی برایت انجام می‌دهم؛ در مورد ایران چه کار کنم؟» پاسخ شما چیست؟
جاستین مورفی، نامزد جمهوری‌خواه مجلس سنای آمریکا از نیوجرسی
: کار را تمام کنید. این جنگ را به شکلی مثبت به پایان برسانید. نمی‌توانیم تا نیمه راه پیش برویم و بعد تصمیم بگیریم که دیگر نمی‌خواهیم این کار را ادامه دهیم.سپاه پاسداران سازمانی تروریستی و افراطی است که مردم ایران را از تاریخ و زندگی شایسته محروم کرده و با قتل، تجاوز، شکنجه، ترور و حمایت از تروریسم، به‌ویژه در خاورمیانه، به مردم منطقه و جهان آسیب رسانده است. من در کودکی شاهد حمله تروریست‌های اسلام‌گرای افراطی به سفارت آمریکا در نوامبر ۱۹۷۹ و گروگان‌گیری ۵۲ آمریکایی به مدت ۴۴۴ روز بودم. از آن زمان، سپاه جز صدور تروریسم، خشونت و سرکوب کاری نکرده است. چهار دهه کافی است؛ مردم ایران به‌اندازه کافی رنج کشیده‌اند و وقت آن رسیده که این وضعیت پایان یابد.
و من به آقای رئیس‌جمهور می‌گویم:
کلاه کابویی‌تان را بر سر بگذارید، وارد میدان شوید، یه درِکونی حسابی به آنها بزنید و این کار را تمام کنید؛ آن هم به‌درستی!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25473" target="_blank">📅 11:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPo4MyKepGn4ZEUIWXvPSCxG69UG28nwOH6Gu9P1RpyQXHZ-VesBHR7XzuO17Kiv6SvJt0zac6a3BeUbfe3whnSZUJe_ByBvn8uNF3z7Ar4f-obLq457BEccsa5HvEVAnip-Jlq8tW7Lw2_M_qPQXbWf3aYgJPXmWDKpmKlCDV7GsFMrT3thmaVCGqRiUcgA4poFzSldNlqOoYSgAOz-pyxu14H0p7HioB6D0Vw1_XzzOtwIw80Xhc552og6_gZqJ0OftULyAv0LPav3iIBB5J76AzX4guQyeLKdhZy3X-eYNXBut9XV94ENbFoLDGagby8HFgUQcnXf2Qmeta_4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگر تحرکات هواپیماهای عملیات ویژه آمریکا: خبر بد برای جمهوری اسلامی؛ ادعا شده چند فروند هواپیمای عملیات ویژه MC-130J Commando II آمریکا، معروف به «شوالیه‌های خاموش»، صبح امروز در فرودگاهی مشاهده شده‌اند. نیروی هوایی آمریکا تنها ۱۰ فروند از این هواپیماها را در اختیار دارد. این هواپیماها قرار بود در آوریل ۲۰۲۶ در مأموریتی محرمانه برای بازیابی و انتقال محموله اورانیوم غنی‌شده ایران، با نفوذ به عمق خاک ایران و فرود در شهرهای شهرضا و کوشک نصرت، مشارکت کنند. این هواپیماها به رادار پیشرفته پرواز در ارتفاع پایین مجهز هستند و احتمال داده شده است که به‌زودی در نزدیکی ایران مستقر شوند؛ با این حال، وی تأکید کرد که محل فعلی این هواپیماها و مقصدشان را فاش نخواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25472" target="_blank">📅 10:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اسحاق هرتزوگ، رئیس‌جمهور اسرائیل، در کنفرانس «مردم کشور» که به میزبانی «وای‌نت» (Ynet) و روزنامه «یدیعوت آحارونوت» برگزار شد، اظهار داشت که اگر انتخابات به نتیجه‌ای قاطع منجر نشود، «تمام تلاش خود را برای جلوگیری از تکرار انتخابات به کار خواهم بست. باید بدانیم که چالش‌های ملی ما بسیار عظیم هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25471" target="_blank">📅 10:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روزنامه ژاپنی «آساهی شیمبون» گزارش داد: ناو هواپیمابر هسته‌ای که قرار است از «یوکوسوکا» در ژاپن بازدید کند، ناو «یو‌اس‌اس تئودور روزولت» (CVN-71) و گروه ضربت همراه آن است.
این ناو احتمالاً طی ۵ تا ۶ روز آینده، یعنی در بازه زمانی ۱۵ تا ۲۰ اکتبر، وارد منطقه خواهد شد.
پیش‌تر در مطلبی که در ادامه آمده است، تاریخ ورود این ناو بین ۱۰ تا ۱۴ اکتبر اعلام شده بود؛ اما اکنون به دلیل شرایط نامساعد جوی ناشی از طوفان‌های «نولو» (Nolo) و «کوگوما» (Koguma)، ورود آن با تأخیر مواجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25470" target="_blank">📅 09:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25469">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/300e6c2aa9.mp4?token=vMs-fXygc-ZF63mGD9-CkHNhnrvkv2yFTfGUKy2wPXIRXgXLGw_Uvyr0D9ar8wAjEspxjb7gC92uSVcRC5h1i2gTQnRzswNk7Aq4sDbZF4Rca_iDzFYdQTxEoJOP39YcWBoYKOHpPJVvJ1qQfZphhu83WyaEj1JLfpj45cvT9cphUnbvBpcej4tXR5C9xtG1VuCzWqLHFaWucNp9e0KW1fBU5AleucPnu1k3v-flS7gAgRPMP5L_J9dj0BQOzg4w1rxW9SXA22aCrjECDoWzQJqK6KDQXgJHawbkwxAyI70ayRKXzyqPRjzzqFDZuJh2dzecPyBHF3hrwA-VtOFoRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/300e6c2aa9.mp4?token=vMs-fXygc-ZF63mGD9-CkHNhnrvkv2yFTfGUKy2wPXIRXgXLGw_Uvyr0D9ar8wAjEspxjb7gC92uSVcRC5h1i2gTQnRzswNk7Aq4sDbZF4Rca_iDzFYdQTxEoJOP39YcWBoYKOHpPJVvJ1qQfZphhu83WyaEj1JLfpj45cvT9cphUnbvBpcej4tXR5C9xtG1VuCzWqLHFaWucNp9e0KW1fBU5AleucPnu1k3v-flS7gAgRPMP5L_J9dj0BQOzg4w1rxW9SXA22aCrjECDoWzQJqK6KDQXgJHawbkwxAyI70ayRKXzyqPRjzzqFDZuJh2dzecPyBHF3hrwA-VtOFoRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور دارلین گراهام (خواهر لیندسی): اسرائیل متحد بسیار قدرتمندی است و من کاملاً معتقدم که باید در کنار آن بایستیم. همان کسانی که می‌خواهند به اسرائیل آسیب بزنند و به آن حمله کنند، به سراغ ما هم خواهند آمد. تروریست‌هایی که به دستیابی به سلاح هسته‌ای نزدیک…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25469" target="_blank">📅 09:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e3e3beb9e.mp4?token=Ja5J6CbrxhOuEezcg8Cs_yubUPTT1EuWWbxWccf8a7AMzD9fhRN0ciHmvjy0NRyV3lxjzWRhPqCE-gRXKJhbUcJkDmUgyEy4DNR00MASA4ElFSZMekoWWyP0zj6dQyFW0-Fs_DZu8Vh8iTQaDexGGY_i_6Q_GOFVjrJawLJ-2kQ7p3liSJYOQaJFI6DtsT3ftXb8YT3STUlkPLVNYy3QUPwaVD-iFYHAocxWPBLHB8fYmWJcoRIV2ES_eGGU0UQxzDP08ZO8kqTaDM_4v5EGBMuCkm1OmF6Xom6_vNsEyf1m1slQdcuEnYUmHs9lZODLRpmPZggscWMT7opLoo9JAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e3e3beb9e.mp4?token=Ja5J6CbrxhOuEezcg8Cs_yubUPTT1EuWWbxWccf8a7AMzD9fhRN0ciHmvjy0NRyV3lxjzWRhPqCE-gRXKJhbUcJkDmUgyEy4DNR00MASA4ElFSZMekoWWyP0zj6dQyFW0-Fs_DZu8Vh8iTQaDexGGY_i_6Q_GOFVjrJawLJ-2kQ7p3liSJYOQaJFI6DtsT3ftXb8YT3STUlkPLVNYy3QUPwaVD-iFYHAocxWPBLHB8fYmWJcoRIV2ES_eGGU0UQxzDP08ZO8kqTaDM_4v5EGBMuCkm1OmF6Xom6_vNsEyf1m1slQdcuEnYUmHs9lZODLRpmPZggscWMT7opLoo9JAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمای‌ نزدیک از‌ نفتکشی که در اطراف تنگه هرمز با مین دریایی برخورد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25468" target="_blank">📅 09:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25467" target="_blank">📅 09:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ9B0yqVb5RKkpXWJAqMw_C74xcKaIKkiM512RzMMCXrZHv1m6OFCwe9ndt67tvIEkb9NCuNpwP0WUDVv3cQBN6JxnhmPkKwkcG03ZOjOFceNIDk8YuA-Bo3IH5gS9Pz42Y9GMB3p-itFnzZ0RJk9gsstNhVRgMR8R3QbwQn2Rr8afuJHPp1ENfbi5AmR89Ygw8ahf0XOBoxfGwO-l95uu7mdsaEjp-9rBLna63Khk6zxWXHg3lyFJ2cLV2OElDqCYKbNBfQHj7uBFQMrHVvQLHFoU5x94mJcvo6UIAXR6SeKMGVq3IoIkex3mvUUNjC7ez3yuGf0Qligwm5P8KNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز: ارتش آمریکا راهنمای شناسایی تصویری (تهدید را بشناس) را برای کمک به سربازان آمریکایی در شناسایی نیروهای ارتش ایران ، منتشر کرده است. این راهنما شامل تصاویر یونیفرم‌ها، علائم درجه و تجهیزات نظامی ایران، از جمله سلاح‌های کلاشینکف، تفنگ مصاف ۲ و نارنجک‌انداز آرپی‌جی ۷ و… است
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25466" target="_blank">📅 09:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شبکه ۱۳ : ترامپ و نتانیاهو طی هفته‌های اخیر، در پی گزارش‌ها درباره بازسازی کارخانه‌های موشکی و پهپادی در ایران ، گفت‌وگوهای فوری داشته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25465" target="_blank">📅 04:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hK03Xg2VoRicEURmoFqTwMIVQ2AlVLsX7-NYofaH02RMmMK2SuA2Eee1QrZ72NWJ3SPQT9eQdPKSu1mvQK_ZVFa6xDecA-NWCgYmYArsq-GjofDs9b-D5CfnHhi3L3MZPp8AQGb2fG8ziPYAljjnQeqlh4eRvRM-R4w11u1pHDnUp63UsiPrUOIvXyGdJQnNSlgLJdAWwLawOn1LEV3vszUwb7gLe_E1G7BtR9l9EieE6q_7hU6h10g72fOBJe6cBXHj3o7kpdZATwZUj7RVkhO-SAEJKgXBkbmRcvkzT3IJTdm5q5n2poR9dy7IRXSqmwxN4mDy-i7dhzk7_MvZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله افراد مسلح به پاسگاه مورتان در بخش پارود شهرستان راسک و درگیری شدید با نیروهای مستقر در پاسگاه گزارش شده است. بر اساس اطلاعات اولیه، درگیری از دقایقی پیش آغاز شده و دو طرف به تبادل آتش پرداخته‌اند؛ تاکنون جزئیاتی درباره تلفات احتمالی یا وضعیت نیروهای پاسگاه منتشر نشده و هویت و وابستگی مهاجمان نیز مشخص نیست. این حادثه در حالی رخ می‌دهد که طی روزهای اخیر چندین مورد درگیری و حادثه امنیتی در سیستان‌وبلوچستان، از جمله زاهدان، سراوان و ایرانشهر، گزارش شده است. جمعه گذشته نیز سرهنگ زن نصرت افتخاری پودینه، معاون فرهنگی و اجتماعی فرماندهی انتظامی استان، در انفجار بمب کنار جاده‌ای در محور چشمه‌زیارت زاهدان کشته شد؛ جبهه مبارزین مردمی مسئولیت آن حمله را برعهده گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25464" target="_blank">📅 03:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a2b70e41.mp4?token=ulRHHvIYJf_sObIwGFNtElhqdxsI9tKTB0TX0TpQYTj-zBo7HueiDaIO1y6UVO2frMclyId-wDDxAcbOFm6-ZGTA5lLQGzo_yM7lm-ImKmHjbEZzDwmOMDjcTpqG3m5Cm_ZmFPqJbI5d2sQ2fe_pvLf76RoaU_fB09Ijua7SYUfBDymzwRqkyAJfgqJ8ombZIgPb0FUSy0KqtXDcDEaPvld5t0ATcPEZrwH3ALjmuBbbFU6x2fSCc28gOFQorWyco5hvoF-uUYIW9OmJIFJxif-fvKp5zxOr0aqXKjsoAKXHhxnuX5e9owMXOXTnNOAI9V7JbkxmnNsJU57UpF_UFjW7_DcToQ6wVZTI8-ThIPdXv-UkugAPnRuI7JSF55Rmg1myPReM1-uWu9QOtqvDzQkVPvOsQmglHjlEAlYtCqDa_aUUZDixxxdjLEWIblrx2W2p5OrJVslRox1KgoDTcsRrX3F1Z-ejHTOYfGzeZCLBVW5uSzIAeKUBYV6uNFm36J_cPsNY4cBhxw3_iy2P89Qw6ruTeDs_gYgd1OdR3tADvp0x1eahU8MvO-6VRs5L8_Z_mHWPFPpdJHWqzvvixHSc8LuK6Tu0ilUCMaIyoEq001QrViqEvpcwjJ3MS5i18aSayryoaWPtwEev1Nc-Ngtf93_F0Q-E_7LRNMTX48I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a2b70e41.mp4?token=ulRHHvIYJf_sObIwGFNtElhqdxsI9tKTB0TX0TpQYTj-zBo7HueiDaIO1y6UVO2frMclyId-wDDxAcbOFm6-ZGTA5lLQGzo_yM7lm-ImKmHjbEZzDwmOMDjcTpqG3m5Cm_ZmFPqJbI5d2sQ2fe_pvLf76RoaU_fB09Ijua7SYUfBDymzwRqkyAJfgqJ8ombZIgPb0FUSy0KqtXDcDEaPvld5t0ATcPEZrwH3ALjmuBbbFU6x2fSCc28gOFQorWyco5hvoF-uUYIW9OmJIFJxif-fvKp5zxOr0aqXKjsoAKXHhxnuX5e9owMXOXTnNOAI9V7JbkxmnNsJU57UpF_UFjW7_DcToQ6wVZTI8-ThIPdXv-UkugAPnRuI7JSF55Rmg1myPReM1-uWu9QOtqvDzQkVPvOsQmglHjlEAlYtCqDa_aUUZDixxxdjLEWIblrx2W2p5OrJVslRox1KgoDTcsRrX3F1Z-ejHTOYfGzeZCLBVW5uSzIAeKUBYV6uNFm36J_cPsNY4cBhxw3_iy2P89Qw6ruTeDs_gYgd1OdR3tADvp0x1eahU8MvO-6VRs5L8_Z_mHWPFPpdJHWqzvvixHSc8LuK6Tu0ilUCMaIyoEq001QrViqEvpcwjJ3MS5i18aSayryoaWPtwEev1Nc-Ngtf93_F0Q-E_7LRNMTX48I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور دارلین گراهام (خواهر لیندسی): اسرائیل متحد بسیار قدرتمندی است و من کاملاً معتقدم که باید در کنار آن بایستیم. همان کسانی که می‌خواهند به اسرائیل آسیب بزنند و به آن حمله کنند، به سراغ ما هم خواهند آمد. تروریست‌هایی که به دستیابی به سلاح هسته‌ای نزدیک شده‌اند،( جمهوری اسلامی ) به آمریکا هم خواهند آمد. بنابراین، باید از قوی‌ترین متحد خود در خاورمیانه حمایت کنیم؛ نگران دموکرات‌های سوسیالیست هستم؛ زیرا در ۷ اکتبر، زمانی که حماس بیش از هزار اسرائیلی را کشت، دموکرات‌ها در خیابان‌های نیویورک به‌خاطر کشته شدن این افراد جشن گرفتند. حماس گروهی بی‌رحم و شرور است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25463" target="_blank">📅 03:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">طبق گزارشات دقایقی پیش یک نفتکش در مسیر جنوبی با پرچم هند در تنگه هرمز توسط سپاه هدف قرار گرفت؛ دو نفر از خدمه مفقود شده‌اند و ٩ نفر دیگر نجات یافته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25462" target="_blank">📅 02:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25461">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faSyzEWDZaI2yAe8M3nYnxZSRMftaJxDgykLshyVLLMoyXnM3pYdx_UX4MEg4SBEeFYBUQ8_AGQFhofaJGY0xNU7RgUQC7C8NB1NTlLVUl_57Mo6MEc2gY3V_VPMmxvuaqTn0g5ALAmLArf454YGtFCh_0VcNGTuBw0vJd3pX83GqWP7rjnrIsVyjLBuT-T-OMndXD5aKwNlzl7YIrl_Tc3u1dqfgAUzAoGkx1_Ra6ZwrI9EnBb3bkBcw-d6CSlGnVfSuvaLKXl6BZPxt0aBwGjbeck16qi69rQUWsZyQsUiD83IL1CX6cHO-22QFLGPQ1qJwxWLAQpx-5lMuC5RBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با بازشدن مارکت ها قیمت نفت برنت به ۱۰۵ دلار افزایش یافت
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25461" target="_blank">📅 02:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZXLtLDYeE1ECnNx0RTEcfrjjM_gVr7tDXzDoFtRhG22vsxku9s1FgaEkd0NAJ9GgEgsV7vVuVUO6MGFvFbAN_5cTRrDUKV7HH2yPKKqWo0_f6DtG3EImXg2P37aNkw4MKa5_6Lxtr1lM582VkXbDsoKTDV0s7dhCU4SRkqr3RuepNBCfSYcRkRTdcPCV_Ufj3pKjPtjlO8vVGoTGVF6eA3fyHU3Vl3GibyrrzX9JayS_4gki6NTAm1MfSdmIQ1g8E6GU-GSE8RrYymxCUN5PHB_2QTo0de0XTB5IgYcvNbQx8yFkcUpb_hDbdVCAvcvJds9B0ODXZYgQWiF1Fo4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطمه مهاجرانی، سخنگوی دولت : پروژه ایجاد ترس از ایران و تضعیف روابط این کشور با جهان، «افسانه‌ای است که دشمنان ترویج می‌کنند» @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25460" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYDq2l-xIYeu28v6Jyl2-bdScmzUQRKepcQlEnU4IrzNpWUnfy3jBujlqFnRXWoahqv95hRIYUHKqfPp89-_EwD7jZWpC2n6oCxiq6LudOnCd5JofaX33EL9J2CJSfqesYC2PpNtR8ZKOwwU3dOOdJhNImj2FwbGX7Z6selcuw_yAwWv-DF25ARbY4gNAyTkrOULtZoNO2ZAL8Dt_7otJhYRa9DZih3SnEMn9kJbr5Jo0ZiN80-StwafiWC4ovdnUs7KRmpwAUR4dmnoNXGBas_kLc7vSD5pgT8aILEHUQtclpLqy3MzU_U1gchwiv0yklbXAgSOgH84oySluHnQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند جنگنده چندمنظوره F-15 نیروی هوایی ایالات متحده (USAF) در حال پرواز تمرینی حمله به ایران بر فراز عراق مشاهده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25459" target="_blank">📅 01:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25458">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyYAiN4oyNbjh8zMFr8mFMaaFlVWFUKHDofnouYjglDF2Y3sjU0cugaCMivkY3f6WR-4v1C7bLGFrtAgJFx9UFaEBHfatvCU6PoDblyXVDVhDX42oLybupK1fa5iKKE5HPXfVzSWk32dq3rkcjztdyf_pf3FibrbPck6n9GJsS-8RxeI9jDSi0-FH345PYa3vrC04O1tdNc4fC_eH0pzPkdUbN5-_mgb3nMGzRtufhr1Dp7NofP7K5_iFLvsaA9tnWafR_LI0vAOAy2tdNjBNzhxLIaYNElze8ZW_gbHnW5UJp8WUnv8A83QNtmEdR3GbGaeGKeeOL5bQktJjDPUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای برای یک نفت‌کش در نزدیکی لنگرگاه «صحار» در عمان دریافت کرده است.
پس از تأیید اصابت یک پهپاد (UAV) به نفت‌کش، UKMTO ماهیت این حادثه را به «حمله» تغییر داد. مقامات محلی در حال همکاری برای تخلیه خدمه هستند؛ با این حال، در زمان این به‌روزرسانی، اطلاعاتی درباره میزان خسارات و پیامدهای زیست‌محیطی در دست نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25458" target="_blank">📅 00:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گنده‌گوز منطقه کنترل بخشهای زیاد و جاده‌های سیستان و بلوچستان رو از دست داده
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25457" target="_blank">📅 00:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ممجواد ظریف : هرجور شده باید با آمریکا توافق کنیم. حتی اگر عین قرارداد ترکمنچای یه جایی رو هم بدیم.«ترکمنچای امضا‌شد چون بقا درخطر بود»
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25456" target="_blank">📅 00:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترابری نظامی وحشتناک آمریکا از ۲۴ ساعت گذشته تا همین الان الان. شما فقط سرانگشتی حساب کن، اگه اینا خالی بخوان برن بیان، میلیون‌ها دلار هزینه داره. ترامپ بیست دلاری رو چند بار چک می‌کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25454" target="_blank">📅 00:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فایننشال تایمز : آمریکا تهدید کرده که جریان تسلیحات به اوکراین را از طریق مکانیسم PURL متوقف خواهد کرد.
این مکانیسمی است که در آن اروپایی‌ها از بودجه خود برای خرید تسلیحات آمریکایی که به کی‌یف ارسال می‌شود، هزینه می‌کنند. واشنگتن هیچ هزینه‌ای در این زمینه پرداخت نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25453" target="_blank">📅 00:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فیلم لحظه برخورد موشک بالستیک گروه تروریست حوثی‌ها (انصارالله) به ترمینال ۳ فرودگاه بین‌المللی ملک خالد ریاض در روز گذشته را نشان می‌دهد
این حمله تا الان ۱۳ کشته و بیش از ۳۰۰ زخمی برجای گذاشته
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25451" target="_blank">📅 23:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک مقام کاخ سفید به اکسیوس : ترامپ واقعاً عصبانی است. او احساس می‌کند زلنسکی آمریکا را بدیهی فرض می‌کند و قدر حمایت‌های آن را نمی‌داند.
استیو ویتکاف و جرد کوشنر هم سفر برنامه‌ریزی‌شده خود به مسکو را به تعویق انداخته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25450" target="_blank">📅 23:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNK1LXJ_ziwGaltx1Io4OYaDynm1lYHSD6ZNLgi539tN_Adz84oPSuEIrn-ruXFcEv7hnhUav3ehOaROlxCbTRNiRrs8IKlqq1Iwwo-VfFwMAdvInZpE6J1HEiGrbe6GmIWtBV1E3vGItlcHrXbg0EpHxJ0xLFelAf3SALHYhdWQzXUuRqtyYO7z6SysUI9H9-w7R0RkPv1IqmaOe5PWLeonPCslpMF6LV0C2DH-pue_o68-BLNbRdCiYQ3946tgFWjzxLgXGbs24Gz54aS3L0Zu3nIamepzxCf-V--UGCWqH1v4xkkpjpT30vLQZZOYvb_d7gulh-Zof8ODT7ELtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جنگ حتمی سوم، سخنگوی گروه تروریستی سپاه با انتشار تصویری در شبکه ایکس نوشت «ما منتظریم»
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25449" target="_blank">📅 23:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25448" target="_blank">📅 23:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ورود گسترده هواپیماهای نظامی آمریکا به اروپا برای پشتیبانی حمله احتمالی
نیروی هوایی ایالات متحده در حال انتقال گسترده هواپیماهای سوخت‌رسان و ترابری نظامی از خاک اصلی آمریکا به پایگاه‌های اروپایی است.
حدود ۲۰ فروند از این هواپیماها طی ۴۸ ساعت گذشته به این پایگاه‌ها رسیده‌اند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25447" target="_blank">📅 23:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آسوشیتدپرس ، بن‌بست مذاکرات ایران و آمریکا؛ تهران پاسخ واشینگتن را ناکافی دانست:
محسن رضایی اعلام کرد پاسخ اخیر آمریکا به پیشنهاد ایران برای پایان جنگ، خواسته‌های تهران را تأمین نمی‌کند و واشینگتن باید موضع خود را درباره موارد مبهم روشن کند. به گفته او، آمریکا برخی از هفت شرط ایران را پذیرفته، اما وضعیت سایر شروط مشخص نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25446" target="_blank">📅 23:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کاظم دستکج ، غریب‌آبادی: اقدامات کنترلی ایران در تنگه هرمز تا زمانی ادامه می‌یابد که آمریکا به این نتیجه برسد راه‌حل مسائل موجود نظامی نیست. به گفته او، ایران در حال پیگیری ثبت تفاهم با عمان در سازمان بین‌المللی دریانوردی است؛ اما این تفاهم به معنای بازگشایی فوری تنگه هرمز نیست و ایران تا زمان اجرای تعهدات آمریکا، خود را ملزم به بازگشایی این آبراه نمی‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25445" target="_blank">📅 23:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjqMJ-8YSNCamqXNhXNZ6HB_I9cH6gzQ8SttTIzyNOYvPbcYDhsDfO6giP7agPl3qYoFwpjV07QN4DYaMHE_WTIZiyVyg9Ryu_whix0_J-effDm_GKwxTHObFlTMBXth15I5V3U-po8UaXfN2O3s_rz0y1yRkZt2k94vtKE_xGIeF2WGb4b7DxTn9RMRnMCdMkxw8ckZ0zQ1Jbxtvpq7r8EHH2oiAFn525Z_0hR1urenGYTrQWx-3eA_2BKqKSamokIEhIAXERid1XPhcxjRUIanhtkTGEnBNEPf4qy0MRJ8W9SD0BNBhmCC1B5grypO2n4ABv4vDF8lzrCDNO4Vgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمایش موشکی دقایقی پیش
سپاه پاسداران در این چند روز آزمایشهای موشکی و تستهای پدافند خود را بیشتر کرده تا بازدارندگی را ایجاد کند و هم از عملکرد خود اطمینام داشته باشد چون میداند که جنگ سوم حتمی است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25444" target="_blank">📅 22:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ادعای شبکه ۱۳ اسرائیل:
نتانیاهو امشب پس از اظهارات ترامپ درباره احتمال ازسرگیری حملات به ایران، رایزنی‌های امنیتی برگزار می‌کند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25443" target="_blank">📅 22:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرگزاری رژیم تسنیم از رصد پرواز هواپیماهای نظامی آمریکا در آسمان عراق خبر داد و مدعی شد پنج فروند سوخت‌رسان KC-135، دو جنگنده F-16 و دو جنگنده F-35 در این پروازها حضور داشته‌اند. این پروازها از پایگاه‌هایی در اردن و اسرائیل انجام شده‌اند و در حال تمرین حمله به ایران میباشند
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25442" target="_blank">📅 22:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ برای کنترل مارکت است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25441" target="_blank">📅 22:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5xrqTltbEHPiOd2rwY66iFma26soS1cyWnVUWvGIEhQkyWPmFXYfbYd3hmXZxfQZMEepAbeV7dzb4kvDu0TaCpoJviXXtM0Cgp49iTtJKqP5bDOAvEKT-dD77xVfKmr_Cj7GUOKxASF4pLgxABADVUGinZGGHD8ZnXOw4adxPIm1qbvTOMk0fBFh1WxWs6XBvFTxddKr7s2da_O_HbE4dvavldb6k--7WWz83IKshhPaq07WyeK_OJvBS0yueJOtE5XNGd_KMFZbhL5h4_nEk9M2r8M-ELMWYjaW8xN9qsE4Qm8PpyX5LOQoQZYCbr1kgieGfuNeDKj8UQIykSe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرمشهر
😁
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25440" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnONm0QIEJ4nNHlcdTtQ6ajr0tJ4sHhFjlkz_LZTHwmYM7slHjEGo5qCfCV5bfTUXIe1726m6mPB5Nn25bJxu7l0FqXQicNy6kRqZj4muk1aiPxpd0DeSB1UqIFM98PhE5E1oEBmoPB-NqdKCfCJL4fI9zHlxSgsyxyiFu_EFq1ZzonW__dd_hSWLvELj0sEzbLzJysBZeyLp9BtNySP8w2VvTPlMPAZfezO0rz7Fo8TDoK5ZbknI8cflo7FmFvovoFCM4u8u2blmQa8Qu_UaqePMuWbx46sDj7ejtqUM3qqnvQVeWY83CnEBZZEqpe1nwmDIyu1ezG8biWEzwxKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تبلیغ فیکه مراقب باشید ، فقط هی روش الکی کلیک کنید اعتبارش بره کار دیگه انجام ندید
🤣
🙌🏾
⚠️</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25439" target="_blank">📅 22:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
گزارشی درباره وقوع حادثه‌ای برای یک نفتکش در نزدیکی بندر صحار عمان دریافت شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25438" target="_blank">📅 22:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فایننشال تایمز: به دلیل حملات یمن، مدیران ارشد شرکت‌های نفتی شروع به ترک کنفرانس جهانی نفت (WPC) کرده‌اند که قرار است در ریاض برگزار شود.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25437" target="_blank">📅 21:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25436">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db3e49ede.mp4?token=N1QPqqQiKAyMEZhJ7zY2CGsYqdYQYsgQIZh7i8uMkoD0q6bSAMysAHQfwRv5BsPdujPX6EObYe7XRZgi4O1wR-DBTtvxIELjpyCZ7VBTDea9qV2px_V50Vd_8J8jQbSS9Y_14DnYj3pW69pJwZZ-Ya_2_CzwDWI6f7FooUrArauKOYp5DmpE9AoOPc7zd1nutTVIiMQWlqyf0jmKqNJht9Thaa32Mc1dPpxZLCjFGobDZunyS78nJ8FgIHN9SLx3cGIBfnoM-sWQBA9pr8nI10h7vVQ4KP-zGCGC-fLLwg8tDVnhflF8bUs06pRX6-laas8uYILGcVI3EA_zrXF23A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db3e49ede.mp4?token=N1QPqqQiKAyMEZhJ7zY2CGsYqdYQYsgQIZh7i8uMkoD0q6bSAMysAHQfwRv5BsPdujPX6EObYe7XRZgi4O1wR-DBTtvxIELjpyCZ7VBTDea9qV2px_V50Vd_8J8jQbSS9Y_14DnYj3pW69pJwZZ-Ya_2_CzwDWI6f7FooUrArauKOYp5DmpE9AoOPc7zd1nutTVIiMQWlqyf0jmKqNJht9Thaa32Mc1dPpxZLCjFGobDZunyS78nJ8FgIHN9SLx3cGIBfnoM-sWQBA9pr8nI10h7vVQ4KP-zGCGC-fLLwg8tDVnhflF8bUs06pRX6-laas8uYILGcVI3EA_zrXF23A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفت‌کش منتشر کرده است؛ نفت‌کشی که به گفته این نیرو، در تنگه هرمز هدف برخورد مین دریایی قرار گرفته است. @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25436" target="_blank">📅 21:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کانال ۱۵ اسرائیل : تحولی در تحقیقات مربوط به پرواز تروریستی: سفارت مالدیو اعلام کرد که دو خلبای دیگر شرکت "فلای دبی" دستگیر شده‌اند. به احتمال زیاد، این دو نفر در همان ساختمان با کمک خلبان تروریست زندگی می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25435" target="_blank">📅 21:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f5401b52.mp4?token=NwvP_ByxEnysdej2brOEvuR_40aLMQD8EhrD1_1YUODvmdqFC2N1GPr1HV1YnN-vAJmvCznnbYbcoH-Js7YcnrDm8-UE0mCXBHSxLdzvmbRhAvkCGJOMq0J1AslV32hWUkawgGHSDBsV-ccCFFoRSNoynb9r52UV9Rkpc_a7GV5cqthgBhhZKPlyrW4dhTReM_pgJTl3aEd5Jo2_l-TM2c7B7UNZMLX7YD5sBPGCCq1Gh4yiqLQYkfin0g9R5_t_M9A9M807u9A_om9rO--XCXcGMRxz09H42XN1QorRTx1NDfIEUHznS2lwMv4Fr5_lweuAXNWCQZ6cDpGn-HmihQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f5401b52.mp4?token=NwvP_ByxEnysdej2brOEvuR_40aLMQD8EhrD1_1YUODvmdqFC2N1GPr1HV1YnN-vAJmvCznnbYbcoH-Js7YcnrDm8-UE0mCXBHSxLdzvmbRhAvkCGJOMq0J1AslV32hWUkawgGHSDBsV-ccCFFoRSNoynb9r52UV9Rkpc_a7GV5cqthgBhhZKPlyrW4dhTReM_pgJTl3aEd5Jo2_l-TM2c7B7UNZMLX7YD5sBPGCCq1Gh4yiqLQYkfin0g9R5_t_M9A9M807u9A_om9rO--XCXcGMRxz09H42XN1QorRTx1NDfIEUHznS2lwMv4Fr5_lweuAXNWCQZ6cDpGn-HmihQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روباه قطبی ، ممجواد ظریف : هر کسی که هنوز فکر می‌کند سلاح‌های هسته‌ای می‌توانند بازدارندگی ایجاد کنند، کافی است به اسرائیل نگاه کند. به اسرائیل در طول یک سال و نیم گذشته نگاه کنید.
بله، اسرائیل غزه را ویران کرد، اما آیا سلاح‌های هسته‌ای از اسرائیل محافظت کردند؟ آیا سلاح‌های هسته‌ای از فروپاشی اتحاد جماهیر شوروی جلوگیری کردند؟ اتحاد جماهیر شوروی بزرگترین زرادخانه هسته‌ای را در اختیار داشت.
علاوه بر این، ما به اندازه کافی اورانیوم برای ساخت یک سلاح هسته‌ای نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25434" target="_blank">📅 21:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نبرد سرنوشت‌ساز برای بازپس‌گیری باب‌المندب از حوثی‌ها
دولت یمن‌ امشب اعلام کرد نیروهای دولتی با حمایت ائتلاف به رهبری عربستان، پس از بازپس‌گیری ذوباب و مواضع راهبردی اطراف آن و قطع مسیر ارتباطی با المخا، به‌سوی کنترل تنگه راهبردی باب‌المندب پیشروی می‌کنند. دولت یمن این عملیات را مرحله‌ای سرنوشت‌ساز برای بازپس‌گیری حاکمیت بر سراسر کشور و پایان دادن به کنترل حوثی‌ها دانست. همچنین حملات حوثی‌ها به فرودگاه بین‌المللی عدن و فرودگاه‌ها و تأسیسات غیرنظامی عربستان را محکوم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25433" target="_blank">📅 20:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25432">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کابینه امنیتی اسرائیل : امشب (یکشنبه شب) جلسه‌ای با محوریت بررسی اوضاع در چند جبهه از جمله لبنان، سوریه، غزه و ایران تشکیل خواهدشد @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25432" target="_blank">📅 20:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdhaopKFiaBaFjCzoA0PT2EFWnTN5EU5JGv_xXS4xKx08PUxxNSOpdRIgosWfKo9V8Ig-nH0feO_yH_ReLkjw0N_jrnnYcYXQn8NYpVMnHrbfXBKRrkC4LbuumeRO-ml7FobcUI7gU_K-MoR26alASdNVp0K1awJAg249j0C9e-YiJOORGBqrnzmdugDND-O4bQ5irkf8PRmhzyyse91JF2hWetSCc2Q_IeI804YVLK7lFWkZdO6hHHZByHdE0DJ7AOHK79x371pTKXeH4cRfFjENgaiVWJHnpuIVrfDjGkephpvYq66E9042T-xgsE7ku2SEqLkVKQG8C8r2_3Kyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های رژیم : زینب ابوطالبی مجری جنجالی «مملکت مال حزب‌اللهی هاست، هر کس نمی‌خواهد جمع کند از ایران برود»، از کشور رفت
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25431" target="_blank">📅 20:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کابینه امنیتی اسرائیل : امشب (یکشنبه شب) جلسه‌ای با محوریت بررسی اوضاع در چند جبهه از جمله لبنان، سوریه، غزه و ایران تشکیل خواهدشد @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25430" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2HjL_iClb1UGqCjzr6xV2PtAcHXGWvihxS3XPIjBExqRvFBWQes61Lx-Ad-8Sk4gzG4Znk71RZatoWp73qIS5HAO88rBjg95_zZTqd5YwDy2z8Dmuw8Gzg26IXJERtvXtvif5eDHT4t5q58YevPzF2KAPyPesOVPnpNLrFo55OPgP0FgTAzx_ey6dSxjxCPPFnSBTawA3KCyJTyEGTHtnI6HpSZAqT6T15Vr-o3YeN9Cw-YDbjIxdtEm114lxC6In4LNPguqp2jAk4SqJX7LhHOuadffYgpmROWUGd63S-SeV-D4KnYSLHF6AcXAV1IxpGeSQ0_VEtt_Ucp9i4xSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی ، کج بند : می‌توانستیم تنگه هرمز را کاملاً ببندیم، اما به دلایل انسان‌دوستانه این کار را نکردیم
اگه دوباره جنگ بشه اینبار به تاسیسات هوش مصنوعی و دارایی های ایلان ماسک تو منطقه هم حمله میکنیم
تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25429" target="_blank">📅 20:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کابینه امنیتی اسرائیل : امشب (یکشنبه شب) جلسه‌ای با محوریت بررسی اوضاع در چند جبهه از جمله لبنان، سوریه، غزه و ایران تشکیل خواهدشد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25428" target="_blank">📅 20:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y15FTE4ohCdVSCToq1vlcjqKixJaqubjstmraEtekxp9TtIDQPN6BV81koqtTqxMqVMAcgi_8YBjRwrbbKCRsARn_qFob5P5cJ5NK0yg4TrUMO02FI_bHiGaYzvMek8N1c7p-9JvbTWPHvJI9BX7j2g4nQuyPhgmSwAI9bIHAUN3AGtdZv-zsQ5YLyZ-276H1DXnEeX7SirAf4PplRiH3bmv-uvzN5s40ZwnNjhZwIkqgR0AtSVYF-XFbLGvqXG0P9sDf1VK9W4YNQPv6gYaAuwMQ6eP2j-0gIwHrQiTWkIotXY2olgJYFGKPo-gjHwV-8amBwHd73Azg7mJhqg2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ملوانان نیروی دریایی آمریکا در حال انجام تعمیر و نگهداری جنگنده اف/ای-۱۸ سوپر هورنت روی ناو هواپیمابر «یواس‌اس جورج واشنگتن» (CVN-73) هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25427" target="_blank">📅 20:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شاهزاده رضا پهلوی: «حمله وحشتناک به فرودگاه ملک خالد در ریاض، تازه‌ترین نشانه آن است که رژیم تهران هرگز به دنبال صلح نخواهد بود. از سال ۱۹۷۹، جمهوری اسلامی چه مستقیم و چه از طریق نیروهای نیابتی خود، علیه عربستان جنگ به راه انداخته و به دنبال بی‌ثباتی بوده است. به ملک سلمان، محمد بن سلمان و مردم عربستان به‌خاطر جان‌باختگان این حمله تروریستی تسلیت می‌گویم. کارزار آشوب حوثی‌ها زمانی پایان می‌یابد که ایران آزاد شود و روابط دوستانه میان دو کشورمان از سر گرفته شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25426" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">روسیه: شمار کارکنان روس‌اتم در نیروگاه هسته‌ای بوشهر به ۱۳۵ نفر رسید
الکسی لیخاچف، مدیرعامل شرکت دولتی روس‌اتم، اعلام کرد با بازگشت ۹ نیروی دیگر برای انجام تعمیرات برنامه‌ریزی‌شده واحد اول نیروگاه بوشهر، شمار کارکنان فنی و مهندسی این شرکت در محل نیروگاه به ۱۳۵ نفر رسیده است. این نیروها در واحد فعال و دو واحد در حال ساخت بوشهر فعالیت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25425" target="_blank">📅 20:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسکات بسنت: ما بخش عمده‌ای از موشک‌ها و پهپادهای ایران را نابود کرده‌ایم و ۸۵ تا ۹۰ درصد توانایی این کشور برای بازسازی و تولید مجدد آن‌ها را از بین برده‌ایم. کارگران در حال حاضر سر کار حاضر نمی‌شوند، ایران به بازار دلار دسترسی ندارد و برای جبران مشکلات مالی…</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25424" target="_blank">📅 20:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: ما پس از یک سال کارزار فشار حداکثری، اکنون وارد کارزار انزوای مطلق ایران شده‌ایم و هدفمان قطع ارتباط این کشور با جهان خارج است. تا روز گذشته، حدود ۱.۲ میلیارد بشکه نفت برای آمریکا از منطقه خارج شده، درحالی‌که سهم ایران صفر…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25423" target="_blank">📅 20:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: ما پس از یک سال کارزار فشار حداکثری، اکنون وارد کارزار انزوای مطلق ایران شده‌ایم و هدفمان قطع ارتباط این کشور با جهان خارج است. تا روز گذشته، حدود ۱.۲ میلیارد بشکه نفت برای آمریکا از منطقه خارج شده، درحالی‌که سهم ایران صفر بوده است. ایران اکنون هیچ نفتی روی آب ندارد و با جریان نقدینگی منفی مواجه است. ما خدمات هوایی ایران به جهان را قطع کرده‌ایم. مقام‌های جمهوری اسلامی دیگر نمی‌توانند به بستگانشان در لندن، دوستانشان در پاریس یا پولشان در سوئیس دسترسی داشته باشند. فشارها را از طریق توقیف رمزارزها و متوقف‌کردن کشتی‌های ایران ادامه می‌دهیم. ایران کنترل تنگه هرمز را در اختیار ندارد؛ پهپادهایش را هر شب به پرواز درمی‌آورد، اما توان راداری ندارد و گاهی به کشتی‌ها آسیب می‌زند، درحالی‌که کشتی‌ها همچنان عبور می‌کنند.
@WarRoom
ویدیو کامل ۱۲ دقیقه ، متن ۱/۳</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25422" target="_blank">📅 20:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25421">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سازمان هواپیمایی عربستان سعودی تأیید کرد که فرودگاه بین‌المللی «ملک خالد» در ریاض عصر امروز هدف حمله جدیدی قرار گرفته است.
دیروز ترمینال ۳ و امروز ترمینال ۴  این فرودگاه مورد هدف قرار گرفته
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25421" target="_blank">📅 20:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فایننشال تایمز به نقل از مقامات ۵ سازمان اطلاعاتی اروپایی گزارش داد روسیه در حال گسترش برنامه‌های ترور مدیران ارشد صنایع دفاعی، به‌ویژه تأمین‌کنندگان پهپاد برای اوکراین است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25420" target="_blank">📅 19:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyOyvfk8B3it4NLMpyi7Qw9SBcSuAAAfTyj5df0pWKSS4lErc0okv-tLuwtDkCkJFUrKjYFJTI9oAaT2IVRPsdNplhL3YL3S-F_5Y_zKsGOQK1f24lUq2CGRZPyY-_gMQr8fTHo3rIQPC0Vpqx5PwbkLqhPess11Lr3EnNFF7fRD-ksKad354w6sHrERfHw_RXHygsLCioUt38hdJg9PwQYWR1Z9GZ7we26uzf7W-kcerlSLHM9csXTkFm2V__-DLYokMMZI1XDZOTGR5C9CReVF-6L5ABfXEfpNoe7EGZ56Nbv3mvCXlcSf8SLILy--EAUObW7ceCugItA59AdSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: «از همین لحظه، آتش‌بس انرژی در جنگ روسیه و اوکراین برقرار است. هر دو طرف موافقت کرده‌اند. آن را نقض نکنید! از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25419" target="_blank">📅 19:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c92b0af8e.mp4?token=ZThUXY8qJrfcmV1pG1o1f_SE_U9O_wzTZ8SsNLk27HIlIFQTjlRzk8OjZ_G45LrXNVOpUHP9qzLrK0uz9uJoE4yThda9-3OuqQAK5Ksm0iAx4wCWdpn1nZslYST13bAeZIrOeynjLPGSIspRnsgdJW_WH3k1TADUE-MdhEfipKy8Jw0aJMR2oW5QvGvhYj0GOfqWreVUafGyxq1Vu54z3ybrv93uona8CsVRn8paFNYLfspmOWl6IlyO5bBFkdJsJl5cdmwqDrHYLsc0N4ebz9cvyRUO256Rp-D7Ws9dYrp82UAs32bg2Bon8rrdhrdNZjDq-MS2sCpqb0lxFqe1MB4MZVZCwUze83RF-Uh-PP0hC8owDjZFrWdqc2EGr32KJtzOXp5U2ylJmiwldbx5DEHSYPLxn3FRVY3Q9YPvvolt14C72CYd8u1KQ8orrJJ4gUxxlfw9LTxkZiIAwGP9hJO2HK9QPzUmtOoihw1st_TFiWMxgiBIXR3F6g7NFPYqCi4lOM46YIhHS-zc_gD0WsBucDDHlGnClKLeXhPleqhwJLg5des3CfK9aTAETbcZ-FBcQoFHdLrh6ZvLkFEWKWOoeShTgHnDnDfPnS9GABqiMbcIu0pNTmlQyo9GQ_q_-rpH49V2Kjezobg_mVDA9xqulUdzTk9u4q9q8E34crI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c92b0af8e.mp4?token=ZThUXY8qJrfcmV1pG1o1f_SE_U9O_wzTZ8SsNLk27HIlIFQTjlRzk8OjZ_G45LrXNVOpUHP9qzLrK0uz9uJoE4yThda9-3OuqQAK5Ksm0iAx4wCWdpn1nZslYST13bAeZIrOeynjLPGSIspRnsgdJW_WH3k1TADUE-MdhEfipKy8Jw0aJMR2oW5QvGvhYj0GOfqWreVUafGyxq1Vu54z3ybrv93uona8CsVRn8paFNYLfspmOWl6IlyO5bBFkdJsJl5cdmwqDrHYLsc0N4ebz9cvyRUO256Rp-D7Ws9dYrp82UAs32bg2Bon8rrdhrdNZjDq-MS2sCpqb0lxFqe1MB4MZVZCwUze83RF-Uh-PP0hC8owDjZFrWdqc2EGr32KJtzOXp5U2ylJmiwldbx5DEHSYPLxn3FRVY3Q9YPvvolt14C72CYd8u1KQ8orrJJ4gUxxlfw9LTxkZiIAwGP9hJO2HK9QPzUmtOoihw1st_TFiWMxgiBIXR3F6g7NFPYqCi4lOM46YIhHS-zc_gD0WsBucDDHlGnClKLeXhPleqhwJLg5des3CfK9aTAETbcZ-FBcQoFHdLrh6ZvLkFEWKWOoeShTgHnDnDfPnS9GABqiMbcIu0pNTmlQyo9GQ_q_-rpH49V2Kjezobg_mVDA9xqulUdzTk9u4q9q8E34crI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل: ترامپ توافق بد را نمی‌پذیرد. او کار این رژیم را تمام میکند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25418" target="_blank">📅 16:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش اسرائیل و سازمان «شین‌بت» اعلام کردند که طی ۲۴ ساعت گذشته، زیرساخت‌های حماس را در سراسر نوار غزه منهدم کرده‌اند. از جمله این زیرساخت‌های منهدم‌شده می‌توان به یک مرکز فرماندهی و دیده‌بانی در منطقه «درج-تفاح»، یک سکوی پرتاب راکت و سه انبار تسلیحات اشاره کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25417" target="_blank">📅 16:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چند آبگرمکن گازوئیلی و پیکنیکی گازی به سمت تنگه پرتاب شد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25416" target="_blank">📅 16:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul_rjCu5LqwuotA2xQtb-4gNZ1_RDbI_ndDUeLpkw-kpqUuULyFdsxfavjShiOHn77CLMD8jiGxkrT3-1Buw0g1D77FlUYXaw2ERyE1fyfzcNGOVA9JxbggyOKRDvvsww1XjR1UPBA1tyjM9DOrX_hHvsyio8fMiNvojtrds3PUEjnq2Bg4zjDuv7AwpMzU7kdgtS4m-ZBqXtBe4FxlsByFKfcighL1TJm9xsargoSVMaTc4DvyOiqwYy0nc7KZkEfWouNWYq6LsuIcMyZaCBreGczZXwPAS4eV5ci_-n9skMY4OMT5U50bgwWGpnQDtL6lZ-TFToNynXga4IfQt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلان ماسک : با ترامپ موافقم وقتشه اوکراین یه رهبر جدید داشته باشه.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25415" target="_blank">📅 16:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDDt75-K4pzXhAMMm2TnBzhdHnb1xrRh4Gmin_IoSVc8x7YxPjXdYz2wQxrWEEGNTEMU6YsDKkqKm-Ccv7BgE0mlWyO2-dyWQSxDeRoltf-W7kRuEt_NkBXkg-bSqHfnwORgmXv6QHxvSwboVL0VXNiPrzM08H1sG_nqnQgKa2MEQv0e5Dw2SdUy92ETa9QoeRw2FuRGs_CgxLnqFOyCHCSQL0jilTk9cj5us6kYVHHqKIG1vtyGXMRcW64RU7fmiyJEwv2bs42DyXVCOp1Jb4YvrLKdrWov4a34Jtvz7yUzbyaEqXVkAL4fqw7OAmRJExuxDDdsi-rMQma43j8EGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامبیز حسینی‌ مجری‌ اینترنشنال ، مریم رجوی را در پلتفرم ایکس(توییتر سابق) فالو کرد
@WarRoom
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25414" target="_blank">📅 15:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرنگار رویترز: آمریکا ممکن است نیروهای نخبه را برای عملیات های خاص قبل از شروع جنگ در ایران مستقر کرده باشد
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25413" target="_blank">📅 15:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb45997b4.mp4?token=WTd_7RxxQNLrwrZ8BKTCM2igiZatoomffY2O4aIWhBHUcbsJ-JTpgzBQ2-MOHwZktz-4n-qwSVW1QTwhx4CekAw7Ox3-0pWMEhFmTOhhwGSWzjbsgP2Hr8Wgpzt_X2SA5pLCDfM9ZCUTuzOViv8rgPIENQhtpuQzwq5ZkmUNyLMa4urhZVerOCtn3pO4FbHZ6DRU0lIVgKCBQs3fGPihNyFXD4OEjFIWnSxR3PsAsxBmOr2lj4Ls_gCiRCgvwa5DFOpQhE5-KJBhQO2lRk1n3AYMO2uWQAVJc-PHALCC5_EHJlDpVJeqOPebxDK22oBhYCQiN7wp1PDwa0ml2WnyuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb45997b4.mp4?token=WTd_7RxxQNLrwrZ8BKTCM2igiZatoomffY2O4aIWhBHUcbsJ-JTpgzBQ2-MOHwZktz-4n-qwSVW1QTwhx4CekAw7Ox3-0pWMEhFmTOhhwGSWzjbsgP2Hr8Wgpzt_X2SA5pLCDfM9ZCUTuzOViv8rgPIENQhtpuQzwq5ZkmUNyLMa4urhZVerOCtn3pO4FbHZ6DRU0lIVgKCBQs3fGPihNyFXD4OEjFIWnSxR3PsAsxBmOr2lj4Ls_gCiRCgvwa5DFOpQhE5-KJBhQO2lRk1n3AYMO2uWQAVJc-PHALCC5_EHJlDpVJeqOPebxDK22oBhYCQiN7wp1PDwa0ml2WnyuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تنگه هرمز یک کشتی در آتش میسوزد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25412" target="_blank">📅 15:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3515553bf.mp4?token=cpAYv7MM9wfjz3WstOqYdU4DUxBj5Lk2N_sfjwWzDKyIKEzjfo5BeNu5-wdI4EFM-a_76w3iZszId6biKIACsbnk6-Kdlc8FMFBSJfcBHN-4YNw57lo2AU7_ax2B2z1LW7yaajZSeRhCUIquXWAv2Jgtd5mtIQSrhbsoMNHk4g56nuQsOYSsIiXbF9448ksU_Uw3uWdbnGLuWG_eqR1PuPBTCCHcUQ4nTQmMa3SQFB5qCVgI8a1Nb6pCugUJuB0IREIE-GtPnzVO6mGSYXZeoXWv8VMmpG2IGa-uPeuGHJmB4gKOcZDGlx3sXvWarP46oDcK3qneobaPugPAvKTDPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3515553bf.mp4?token=cpAYv7MM9wfjz3WstOqYdU4DUxBj5Lk2N_sfjwWzDKyIKEzjfo5BeNu5-wdI4EFM-a_76w3iZszId6biKIACsbnk6-Kdlc8FMFBSJfcBHN-4YNw57lo2AU7_ax2B2z1LW7yaajZSeRhCUIquXWAv2Jgtd5mtIQSrhbsoMNHk4g56nuQsOYSsIiXbF9448ksU_Uw3uWdbnGLuWG_eqR1PuPBTCCHcUQ4nTQmMa3SQFB5qCVgI8a1Nb6pCugUJuB0IREIE-GtPnzVO6mGSYXZeoXWv8VMmpG2IGa-uPeuGHJmB4gKOcZDGlx3sXvWarP46oDcK3qneobaPugPAvKTDPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ‎صادر کردن دستور یک حمله تلافی‌جویانه قاطع علیه حوثی‌ها توسط محمد بن سلمان، ولیعهد عربستان سعودی
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25411" target="_blank">📅 15:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: منافع‌مان را یا با دیپلماسی می‌گیریم یا با نبرد. اگر منافع ما در دیپلماسی به دست آید، چه بهتر. صنعت هسته‌ای ریشه در ایران دارد و نمی‌تواند با ضربه از بین برود؛ متاسفانه دشمن این را هنوز هم نفهمیده.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/25410" target="_blank">📅 14:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a78cb2396.mp4?token=Iegu5orD3RbCtcuLGl5SytQz_SK71mNM-eupLCievn4hYoq3lCK36m935FBq_O762tiSxcjfMn12zZWENWwBSEUbTZJ1vE-7NbPd9fFWLbt03JBOaBMqE02mI8nU0S1AEVr2GEe31t6t0WueoB8geT9SMMxytaUyiiBbdm1PVsCR3fdfzy9gLdgP34Tf5EwvmbRmOf6KfGwuJu5Ray7c2Ocy0qYtXeWqey74mHXrRYBdR_0nFWJixlrzXT1HRipncEF1mp9c7hXurLKT-gX6iCHul3vZwZtcyuhd1gXITLcis-DycjR0aegeoIU9P8eSBfQ5k8ybypOJ4Pw5xVFdWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a78cb2396.mp4?token=Iegu5orD3RbCtcuLGl5SytQz_SK71mNM-eupLCievn4hYoq3lCK36m935FBq_O762tiSxcjfMn12zZWENWwBSEUbTZJ1vE-7NbPd9fFWLbt03JBOaBMqE02mI8nU0S1AEVr2GEe31t6t0WueoB8geT9SMMxytaUyiiBbdm1PVsCR3fdfzy9gLdgP34Tf5EwvmbRmOf6KfGwuJu5Ray7c2Ocy0qYtXeWqey74mHXrRYBdR_0nFWJixlrzXT1HRipncEF1mp9c7hXurLKT-gX6iCHul3vZwZtcyuhd1gXITLcis-DycjR0aegeoIU9P8eSBfQ5k8ybypOJ4Pw5xVFdWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: حله … اشکالی نداره این موضوع منو آرام می‌کنه،  آن‌ها احتمالاً پیش از انتخابات کمی بیشتر داستان درست کنند ، چون فکر می‌کنند این کاراشون به ضرر ما تمام می‌شه . ما می‌توانیم خیلی سریع به این داستان پایان بدیم باورشون نمیشه چقدر تمیز کارشون تموم میشه . آن‌ها نمی‌دانند من چقدر با آن‌ها خوب تا کردم؛ نمی‌دانند چقدر تازه باهاشون با ملایمت رفتار کردم
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/25409" target="_blank">📅 13:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bv1tghjuQIFDbpAEEwX3lGaamycwJyTO1y5Zmd2UN3W8nHeqRtsBwwMORILFl3mnvWyn6W7kaJRX9JiDBMyN4nOGdJvEpwxF7uxsPd84G-Igd8UG_UCclZwWFLRPewQSE7N14MWn9SuO8RlWB2ej3U3vCCttJeb7084jvrZcJ8khVwyi-XXEVGOwDUbFFJVtRcO0xz5USHj2qw7rcz773JS3kPykC2iyWIV0UblMHK0suKVGnFJzywpslCIf4cMHvPI-HSvPBQUPlwTYOikQ3FxIOJJPo0yE-Y5ka8n1-oj8pvtVHwPbX1syFJW3jK43PK7JLbkvd73PUw1wYoqD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eac6TNFVm6Vw2afEn_B59OOeqgjaFHMb3zDebqayRtTES_uPNcDGnv9UtwNB1FdvBpaqnkMUJyIiJf7JpoWG27KbGhZb9yAH2qawzsbntwejvt-GTlo0Zjx-xYuNSN9Rcwxo7lEg1WOKNrlgkJtVw4xZlP4-YFsJeox1pnmvl0hsjV07HykS9e9tfEQ6hTAPX8ElU3t_ZtGPf0oUeVIEG9GtSTpmS1q1FQDvzQJapezmFjLJKfeJHMunlEZtLhOaHv7KH0bpRMhzKghAOf33ujpnvBzUeUtb84Ps9-OF7i86tqj8_ebDE2iFv5kzYJV7Kqkg1I2N1IC_GHSnrqxSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXL3tH8hG_JDu7gp21CUma2eaYtSbQyAFKs_bYZlF1KBeya6Z3GCEHfZkxU23EMSLtIxZEeRxd03UYhWM1zcSZLueBuCnM6wN8Dxa-QAEj68nwGxVrLSDBxK2DVAtM7nzvKN2LTwAVShWyFVC2wwEayNsqZP2mzz_VJUla6JeByHi4ZRlXfX7oYGc9DUiFZ1DSn9VN3KifOBDX2DMpUXh_hNedZxpJ9M1vto_PwrovC9OGq6jdbz8wIiY_1xSEpsGODeVoeGH2kTKZm7JbN7E---29cPC2NgxtbzXxgGi9XqeQc7z6Ml2h6mEP9E2YVPEZAkKcOO96Mo_9PWFo7aNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آسمان تهران ، آبگرمکن رو کات دار زدن
😂
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/25405" target="_blank">📅 12:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارشهای بسیار از‌ پرتاب آبگرمکن از اطراف تهران/کرج
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25404" target="_blank">📅 12:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محمدمهدی هاشمی، نویسنده روزنامه خراسان نزدیک به ممباقر قالیباف ، در یادداشتی که امروز، منتشر شد، مدعی شد با بررسی تحولات و اظهارات هفته گذشته ترامپ و روبیو می‌توان نتیجه گرفت که
آمریکا و اسرائیل تصمیم خود را برای آغاز دور بعدی جنگ گرفته‌اند
. او نوشت تبادل پیام‌ها میان تهران و واشنگتن نیز احتمالاً تا پیش از درگیری بعدی تأثیر ملموسی نخواهد داشت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/25403" target="_blank">📅 12:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25402">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-2vRJpLhO5ADJyijtcZX91Pb2CXC7K8Lj3aj7EVKk51MwDlsI_xJCE6mAiyuTIpmT3zVRiXAmUsDHIXYOsWacc0QQ-cSvVoKmsYoVwODQfesgSLXeAYTEqsTwhGMN2NYrUVTCdjtn_qPXEh5rSsJZy4ZNmBx2OrBFC3bdiSUbK1M3vre8pIAyvnhbDrBDWECyJ_DyNcz41xM7-WdHxwgpSCpxGl8KRVoAikm-iX-Innw1mboI6UEi3fswIIXMFMYwwecXVqmJ1ZjLxICel9nBWbA4OIfQ5IM_pIi-7YA9NhFLc4RMocZhNweNRKClGGDikiZzTxWTvh8kxzGdT9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی دختر بر تمام دختران ایران زمین خجسته باد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/25402" target="_blank">📅 12:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOyy9Wx8Tk09CipbA40mMxz05P4eC7oBHfnwC90YV6abTdEDC4GHqGJKgrllKJmyLH75kVqaVc1FUxTserJIvrRlSliuwLXGaU2yMDV_OBD0uZ2NU_PU2iBEfNZK_a493Tifjzqgc8AhVsClPxE1_BbjmSJUPLoL4gwMuc9suShd8QnKCxTPo9Fs3eoE9fcOUPjgz_rU0dmIjS9LmtM9BXr7L86Kam0PJdwRunuR_X7TYGeBQIQIsZ6QHpURJd0tXRs4FQilaHJLdNgq94ejfcNrwxi9zbW82sZM_T48e_3rh8NJqnl474rf5SywG-OIY0NPYi5nr3I6mkq2PeRHmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود یک ساعت پیش، چندین انفجار در نزدیکی کوه صفه در اصفهان، واقع در مرکز ایران، شنیده شد.علت این انفجارها هنوز مشخص نیست؛ با این حال، بگم که این کوه محل استقرار بسیاری از پرتابگرهای موشکی رژیم هم است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25401" target="_blank">📅 11:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پزشکیان : اگر ما ایرانیان کنار هم باشیم، نمی توانند ما را بشکنند و به ما آسیب بزنند
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25400" target="_blank">📅 11:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2f5a8ccb.mp4?token=SQkFfNpCl6va7B3C_N3AWMn3VOv2pF51OIbQ8frhI3dLhm0czYPgdlG2Vz4PDzS-oIiU0GDNQBQKz44C01nEy26L2CEqM780ofydQkBQhqiOZUm2zGghwtZk-7u6RT9Y8jWuPxA6zWXXj2ydFIdIrWxbpfBWPLhFy2KFak2xtbRfjLXObkLAiUo1MB7WzP66pYfw9xIDl-z6TC3aA5k_zZYJVEDGLHHpDRF_-JB5HnBJzcv-8htRGJ92ol9mHUHD1Mb3tEzQhf1OkAuXsRRWIRlbfErWbKC02s_XGAVAB3szs9HczZ1qjLbDcLulaw1qwXCsRCn6jfJuhDDoYDMefw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2f5a8ccb.mp4?token=SQkFfNpCl6va7B3C_N3AWMn3VOv2pF51OIbQ8frhI3dLhm0czYPgdlG2Vz4PDzS-oIiU0GDNQBQKz44C01nEy26L2CEqM780ofydQkBQhqiOZUm2zGghwtZk-7u6RT9Y8jWuPxA6zWXXj2ydFIdIrWxbpfBWPLhFy2KFak2xtbRfjLXObkLAiUo1MB7WzP66pYfw9xIDl-z6TC3aA5k_zZYJVEDGLHHpDRF_-JB5HnBJzcv-8htRGJ92ol9mHUHD1Mb3tEzQhf1OkAuXsRRWIRlbfErWbKC02s_XGAVAB3szs9HczZ1qjLbDcLulaw1qwXCsRCn6jfJuhDDoYDMefw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: قبلاً هم گفتم که باید برای خاموش کردن آتش به ایران حمله کنیم . ما با یک مشکل جدی روبه‌رو هستیم؛ با دولتی بسیار شرور که رتبه اول جهان در حمایت از تروریسم را دارد. نمی‌توان چنین سلاحی را در اختیار آن‌ها گذاشت؛ آن‌ها بدون هیچ تردیدی از آن استفاده خواهند کرد. می‌دانید، خیلی‌ها حاضر به استفاده از چنین سلاحی نیستند، اما آنها…
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25399" target="_blank">📅 10:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_5MidSxuWUzCWVpSQ8BJH3G7cPEWqPT-6rwJBvvih1NRSmr1rRL8XywO2jp1DGVur3oXV4QmHRGOWS0JHPU4AXDYSWs0MVbIybdrR_pFhpp_d8Wmc4HqU9kvdvqAdrEUTGe7bpiamtKJrv0sKOmnn3RY990amlWTscuUeHQsk78DP4V4l5tY5Nxta6Wf0aRa5bmQHD9ax4ejrmk0hjfpL6wnITkEQSy17Spne3MaarwpBDM-EDowiSaeUBAYjo5AIvEdwlql0bVzkn_cIw0XTSG1cHHU8zVIvOGk5pzORdAyyGmHak-687QZ8i-fQ8ynHllMm2h_e6HvqdcbgvZ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطمه مهاجرانی، سخنگوی دولت : پروژه ایجاد ترس از ایران و تضعیف روابط این کشور با جهان، «افسانه‌ای است که دشمنان ترویج می‌کنند»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25398" target="_blank">📅 10:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce60ee997d.mp4?token=m1tY2uDqlL75Z1toG27ZfGaZq0XbzDlBLV_bd56PXG49q-VxWFLP3W3ILzC-AMlHz20cR0ikQmKAOW9sjILrAiHwwZcvVeNUzAtOKFLMzwI83HDeBHRilwUyIW6GbO4kPkA1tZ7IydGEVNnrV8BuXLKM3w6qRyUhsFlvtj4uyjsj7EsbzKsG17q9ix1dDXt8VlVVCj99vLrX7F-44JCcs66NakC669-uPu4KNOlJac3wM_U5G4VNEP25pAo_RnD-UPX2J90MCkvtix-eRnLhZNxvpNhwx_rOJEcG5d0qgRps12zYxU9YSj3Iq5ivADufpQAswCFmq9YBGG-QTpvaEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce60ee997d.mp4?token=m1tY2uDqlL75Z1toG27ZfGaZq0XbzDlBLV_bd56PXG49q-VxWFLP3W3ILzC-AMlHz20cR0ikQmKAOW9sjILrAiHwwZcvVeNUzAtOKFLMzwI83HDeBHRilwUyIW6GbO4kPkA1tZ7IydGEVNnrV8BuXLKM3w6qRyUhsFlvtj4uyjsj7EsbzKsG17q9ix1dDXt8VlVVCj99vLrX7F-44JCcs66NakC669-uPu4KNOlJac3wM_U5G4VNEP25pAo_RnD-UPX2J90MCkvtix-eRnLhZNxvpNhwx_rOJEcG5d0qgRps12zYxU9YSj3Iq5ivADufpQAswCFmq9YBGG-QTpvaEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره حمله مرگبار حوثی‌ها به فرودگاه ریاض چه نظری دارید؟
ترامپ: به‌نظرم وحشتناک است
خبرنگار: آیا آمریکا را وارد این درگیری خواهید کرد؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25397" target="_blank">📅 10:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سازمان حقوق بشر کارون: بیش از ۱۰ کارگر متخصص و بومی شرکت پتروپارس در هویزه، پس از اعتراض به اخراج و تمدیدنشدن قراردادهای کاری خود، به ۷۴ ضربه شلاق تعزیری و پرداخت ۲۰۰ میلیون ریال جریمه نقدی (۲۰ میلیون تومان) محکوم شده‌اند. به گزارش این سازمان، حکم شلاق اجرا شده است. این کارگران که در پروژه توسعه میدان نفتی آزادگان جنوبی سابقه فعالیت داشتند، پس از تجمع اعتراضی با شکایت شرکت و پیگیری قضایی روبه‌رو شدند. حکم در ۱۳ تیر ۱۴۰۵ صادر شده و کارگران همچنان خواستار بازگشت به کار هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25396" target="_blank">📅 09:58 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
