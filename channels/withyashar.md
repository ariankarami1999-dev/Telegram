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
<img src="https://cdn4.telesco.pe/file/kCat4hp4X8SibgNgSZm4boPvNKWrcga-qN_PotTX_zRRI0e58PyPf9buS2iBV55ohbTa0Auq8T0ntWmPBD5iQV_I__OVm2BP3h0POV9DlPYHUkdHSpX23tAMZ9Pu4vDbcFGDtkgvkaHF7KelWVtw3ih8tav6kBnK0IaC-8n23f4_MA4qt9FypNW7hND0ShSLP0TjVSxfL7uRJkxvCobUsR2TL3kIB3ppU2j-Vv08ZtzNreWpwTaP0NEesx7uagd9sJoLnJytW0RzGZxwcstbcrAKSF337d70mYiPP1TFpuu5ApNYsdhENUAYB_un1Nk1UohkGSMgEHqV4hzdkCreLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 22:23:15</div>
<hr>

<div class="tg-post" id="msg-19589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صدا وسیما :
عصر امروز ارتش آمریکا با پرتاب دو‌ موشک به یک تانکر ال پی جی که از سمت دریای عمان قصد ورود به منطقه را داشت این تانکر را به تصور اینکه قصد انتقال گاز ایران را داشته مورد اصابت قرار داد و با کشتن دو نفر از خدمه و ایراد خسارت به موتور خانه آن کشتی، آن را متوقف کرد
@WarRoom</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/19589" target="_blank">📅 22:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیویورک تایمز: ترامپ امروز با مشاوران ارشد خود درباره تشدید حملات علیه ایران دیدار کرد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/19588" target="_blank">📅 21:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پست جدید کلیک کنید
https://www.instagram.com/reel/DbL3e_Ioe9s/?igsh=ODB2Y3BzZGJoMHUz
کپشن : ⁨ اتاق جنگ با یاشار : برای دوستان سردرگم شاید یکی از بهترین مثالها برای ماجرایی که برای ملت ما پیش اومده، فیلم گنج قارون باشه. مردمی که با ثروتی بی‌انتها خودکشی کردن. و حالا، آمریکا و اسرائیل، او را از رودخانه نجات داده و دوباره به خانه آوردند. خواستم یکبار دیگر این فیلم رو برید دوباره نگاه کنید هم صحنه های بسیار زیبای آن زمان هم برخورد و فرهنگ مردوم با هم… که در آن زمان ما کجا بودیم. سکانس هتل هیلتون هم فراموش نشدنی است. حالا پاشو و شادی کن و مبارزه کن. گنج قارون در انتظار شماست. خواستم یکبار دیگر یادآوری کنم کی هستی و کجایی تا بلندشین تاریخ سازی کنید و از این حال دربیاین!⁩</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/19587" target="_blank">📅 21:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14728b7ed2.mp4?token=L1oGlPr7yhUgFv_SJvqNFzXLh6xqpUdTO85KVsljWe1mF5duLcYDHaNV1kvItnC8DHAyv6kWFCIE23HkyUomdeAcKbKNkooB28QoIamrTJd2K4iJehx0YtTEYTNevtdxWAc5bWUfj8-3hwtZSxihF75F6N_SKJYpuuMP6Rlsa0l1LxdelHmls7VLSGGdJt5j3PwnmN-8uCRyDZGoXddJyIIOuUC3x9lfAH8KJQbYlDE6N3JaJoYvoUbFKGnNOZI0RilQr62YVbY6XS_MSvwPC42TopRw9FIZifhyGKD5onneGBA-TK80Hyg923jtGLYGDGAiSzpjIlUvOP0HpAYjCIIMhwneDNx8zuawAdy-wEkHMXVOeNsn0fdtv6FBLq1nxgkiZt6r073-uFSPMgFStC2pKhnBYYq_het2A6a_QavZKbHkNd7Im_YbRQLAVMC4tmrLgxXqNQeZEEB5jascqP4A_SYkVMJ3K1mRX4_xahwWYyUMXz2CJOv43QmRP44LI1R2dCXVmVu6hEKBtsvWqjlJlfn2iTVU7QMCyE3zdjGnkIKoZmkswWWx3cyKaPZ1qsC4Qx2SVkGu6fGLrvjU0Y33t4otgiGkbuZuZ7LoIeU0ujISH1_W1uMpM4scdoD7C7G0YAmmPcNil_CQ0LvrCUbOnhgfT_Hx4KnKDU17Tmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14728b7ed2.mp4?token=L1oGlPr7yhUgFv_SJvqNFzXLh6xqpUdTO85KVsljWe1mF5duLcYDHaNV1kvItnC8DHAyv6kWFCIE23HkyUomdeAcKbKNkooB28QoIamrTJd2K4iJehx0YtTEYTNevtdxWAc5bWUfj8-3hwtZSxihF75F6N_SKJYpuuMP6Rlsa0l1LxdelHmls7VLSGGdJt5j3PwnmN-8uCRyDZGoXddJyIIOuUC3x9lfAH8KJQbYlDE6N3JaJoYvoUbFKGnNOZI0RilQr62YVbY6XS_MSvwPC42TopRw9FIZifhyGKD5onneGBA-TK80Hyg923jtGLYGDGAiSzpjIlUvOP0HpAYjCIIMhwneDNx8zuawAdy-wEkHMXVOeNsn0fdtv6FBLq1nxgkiZt6r073-uFSPMgFStC2pKhnBYYq_het2A6a_QavZKbHkNd7Im_YbRQLAVMC4tmrLgxXqNQeZEEB5jascqP4A_SYkVMJ3K1mRX4_xahwWYyUMXz2CJOv43QmRP44LI1R2dCXVmVu6hEKBtsvWqjlJlfn2iTVU7QMCyE3zdjGnkIKoZmkswWWx3cyKaPZ1qsC4Qx2SVkGu6fGLrvjU0Y33t4otgiGkbuZuZ7LoIeU0ujISH1_W1uMpM4scdoD7C7G0YAmmPcNil_CQ0LvrCUbOnhgfT_Hx4KnKDU17Tmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فشن شو کالکشن تابستانی بی بی
کت واک نمونه کارهای ۲۰۲۶/۲۰۲۷
@WarRoom</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/19586" target="_blank">📅 21:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19585">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9wFPydCmRgIRpJAD1MGzqOlEzGyCTGxJCOOnFPMsyNVcu4iI-ka04yXVbyHJ3ej1EGj6aVCi7p7UuKvNLLEl9XtoxIUvv5-PsfXkY9z8nNKluc22d1vItHI6WtnRtShbpAtoc67VLPr4T3XdBdsi-WTSM1bvXzU2rrILncDMw19A1JYdnZwsKTxMEdLCTHvuxjaMs9TysBRXOvLDjUD5s0eOmVW2E-vsF7savbFCNGR-wgwnc7qoNmxxkl4YY_uQPX4UwLB1mnJvJIVu_FU7-9DaIHGZcPwWuy288WMcNWhpu4zzPR83mybAet7f5rO5tdT3h73oJuLXGgpJvjnNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی درگذشت
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/19585" target="_blank">📅 20:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فرودگاه بن گوریون اعلام کرد که فرودگاه به طور معمول فعالیت می‌کند و توقف موقت پروازها به دلیل انجام تعمیرات و نگهداری معمول باند فرودگاه است، که از قبل برنامه‌ریزی شده بود. انتظار می‌رود پروازها ساعت ۱۱ شب از سر گرفته شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/19584" target="_blank">📅 20:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دونالد ترامپ اعلام کرد اتحادیه اروپا با جریمه‌های سنگین علیه شرکت‌های بزرگ فناوری آمریکا مانند اپل، متا، آمازون و گوگل، به‌طور مستقیم شرکت‌های آمریکایی را هدف قرار داده و این اقدامات را «غیرقانونی» و «تبعیض‌آمیز» خواند. او گفت جریمه‌های گوگل اکنون از ۱۸ میلیارد دلار فراتر رفته و آمریکا دیگر اجازه نخواهد داد اروپا از شرکت‌ها و مالیات‌دهندگان آمریکایی سوءاستفاده کند. ترامپ از آغاز فوری تحقیقات تجاری بر اساس «بخش ۳۰۱» علیه اتحادیه اروپا خبر داد و هشدار داد که این اقدام می‌تواند به اعمال تعرفه‌های سنگین و دیگر اقدامات تلافی‌جویانه منجر شود و اروپا بهای سنگینی برای این رفتار خواهد پرداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/19583" target="_blank">📅 20:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19582">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjmpZLI9ECr8FCf1sVlVbAsxvwLz2EC48R7yWIfSeAaHbJTObzQmd5OyOBDZdL7HOZDZx62KUhiwj5ywJXWD6pqDpcgkzi7DSJvtOa-bEO0uPQ7Y7tW6e_UvwA4mWEHIBrenBLB6qvm6LkvxDraFHABiQmv4XTeXkxl8ifsdrTsEj6KqSxcec_-AiTwIYd5j9YBcNpkwAHX4avlXaV4HfKZRgWPQ_neoxI_ODZqeAsCuLYGug-zAYppuFciWLpf5ifYTWh5ENQ9b8FzxHNdQcnZBYEIK4vd-o_uUoIsEwXNYQA3dOPkns6udM_lalOzjJ6IZGzpcrxPY2PZCjrlZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/19582" target="_blank">📅 20:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19581">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وال‌استریت ژورنال: بحرین و کویت به‌طور محرمانه جنگنده‌های خود را برای حمله به اهدافی در داخل ایران اعزام کردند؛ این نخستین اقدام تلافی‌جویانه مستقیم آن‌ها علیه تهران بود. در این حملات، انبارهای پهپاد و موشک هدف قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19581" target="_blank">📅 20:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19580">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مطابق گزارش‌های خبرگزاری آکسیوس، به گفته منابع، واشنگتن از متحدان خود خواسته است تا کشتی‌های پاکسازی مین و پهپادها را برای کمک به تأمین امنیت مسیرهای حمل و نقل ارسال کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19580" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آکسیوس:ایالات متحده و بریتانیا در حال برنامه‌ریزی برای برگزاری یک کنفرانس بین‌المللی درباره تنگه هرمز هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19579" target="_blank">📅 19:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19578">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVooiAhgx7ibFIcd3oYgB3MOUN3xHCyXkWVO7Nvoz2_K6--1fO2r3KbBHnJi3RLM4zLPYwIl1vP8JmyrPrsU_Op9HbCjbYVOrtb3KXN0gdGZxa0wRhuA-OH3EFZG_KbIfHYbOZdwu7cbSdkT5t3YUqor_f0RKTRaNXuRlRWXsBj3xMo3KGekjBe70n3zbwreICb1J8wLQuGeXjYs-z2JQHPOKU-kGUg5M8GUmbyFMB1bqK_bsQLNGh3el9BccTx78t93oFbZXMogh1PvwT35Lh2wdQhWTuY5nln86VhXWdH21k3cfdPWcLKQkxFlqD_3M6Y-evS2mw4JewcltBOvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در مورد فروش سلاح های روسیه و چین به ایران:
رئیس جمهور شی، در دیدار اخیرمان در پکن، چین، به من گفتند که تحت هیچ شرایطی، سلاح به جمهوری اسلامی ایران نخواهند داد یا نفروشند – و این اظهار نظر شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم و علاوه بر این، من نیز خدمات بسیار بزرگی به او ارائه می‌دهم.
به همین ترتیب، رئیس جمهور پوتین، با وجود جنگ وحشتناکی که در اوکراین در جریان است (رابطه همچنان مانند رابطه با رئیس جمهور زلنسکی است)، به من گفتند که سلاح به ایران نخواهند فروخت. او درک می‌کند که من سلاح به اوکراین نمی‌فروشم، بلکه به کشورهای ناتو می‌فروشم. آنها قیمت کامل را پرداخت می‌کنند و من نمی‌دانم این سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به نظر من، دو کشور بزرگ که مردم اغلب در مورد آنها در رابطه با ایران صحبت می‌کنند، در این موضوع دخیل نیستند. اگر دخیل بودند، این امر برای آنها بسیار بد بود – قطعاً به نفع آنها نبود.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19578" target="_blank">📅 18:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19577">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو دوشنبه آینده عازم واشنگتن می‌شود
دفتر نتانیاهو اعلام کرد نخست‌وزیر این دوشنبه اینده به دعوت ترامپ عازم واشنگتن خواهد شد.نتانیاهو روز سه شنبه در کاخ سفید با ترامپ دیدار می‌کند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19577" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19576">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ae83427d.mp4?token=ByVbEHlBvuikwrIbOWTrF-kkMQ9JEPR3jY4ROgNXyOZsYxnWkDwrGlCAB_hsuYWJW5jrUYsc3Lem8vNCU3-KDmIMZJ8bidUMZMs_xJ6v8ws73ONVVRxcLw9fiEjm6gKApUPqcEInoN0oKDsg3IJfmKG8cbyo8WzYXexMiNf3BgU3M7KdqkP4kGeCL3YEL0Ug7bKyqgHTy9lj0qrMm7OyaFZ0TgqoB5wMPeKAfrN6N_U5HoozqBpeaLY6WQgNc-UVWROr_DeWbdYmoTGru18oZgdDuwxMtkxZUTZepbRyfvSWHsEwWf-FAi2Kg6D69DRhxD4ew5WszVoseE3m8cz3_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ae83427d.mp4?token=ByVbEHlBvuikwrIbOWTrF-kkMQ9JEPR3jY4ROgNXyOZsYxnWkDwrGlCAB_hsuYWJW5jrUYsc3Lem8vNCU3-KDmIMZJ8bidUMZMs_xJ6v8ws73ONVVRxcLw9fiEjm6gKApUPqcEInoN0oKDsg3IJfmKG8cbyo8WzYXexMiNf3BgU3M7KdqkP4kGeCL3YEL0Ug7bKyqgHTy9lj0qrMm7OyaFZ0TgqoB5wMPeKAfrN6N_U5HoozqBpeaLY6WQgNc-UVWROr_DeWbdYmoTGru18oZgdDuwxMtkxZUTZepbRyfvSWHsEwWf-FAi2Kg6D69DRhxD4ew5WszVoseE3m8cz3_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از خواهرهای عزیزمان، دیدبان اتاق جنگ، همین الان فیلم بسیار مهمی را برای من فرستاد؛ یک اسکادران اف۳۵ (۱۲ عدد) همین الان از مهم ‌ترین پایگاه نظامی امریکا در انگلستان  RAF Lakenheath  به سمت خاورمیانه حرکت کردند، او الان این فیلم را در کمبریج حدود 25 تا 30 مایلی این پایگاه مهم نظامی ضبط و برایم ارسال کرده
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19576" target="_blank">📅 18:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فعال شدن آلارم حمله موشکی/پهپادی در کویت
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19574" target="_blank">📅 17:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عراقچی: ما آتش‌بس موقت را نخواهیم پذیرفت و تا زمانی که خواسته‌های ما در مورد تنگه هرمز محقق نشود، این موضوع مطرح نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19573" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سناتور سابق نیروی دریایی، تیم شیهی، او دستبند  دوستش که توسط بمب جمهوری اسلامی کشته شده بود، بالا گرفت و سخنرانی تندی در صحن سنا در مورد ایران انجام داد و تحسین همگان را برانگیخت. بازتاب این سخنرانی بی نظیر بود.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19572" target="_blank">📅 17:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند ستاد فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد نیروهای این فرماندهی، سیزدهمین شب پیاپی حملات به ایران را در ساعت ۹:۰۰ شب چهارشنبه ۲۳ ژوئیه به وقت شرق آمریکا (ET)، (ساعت ۰۴:۳۰ بامداد پنجشنبه…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19571" target="_blank">📅 16:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هاآرتص: نتانیاهو در تلاش است اسرائیل را وارد حمله به ایران کند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19570" target="_blank">📅 16:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0647ce42a6.mp4?token=fhLUCf9yve5HvPRrL6ZFP-hihHBKAcT2Oa0Ec1bMayBH3u5ZbM2vgzhe1KSv3vAXLypk-rUIzmeK5Uh1IngVR5Vfuw3VtQn-blBOZR1bjdnmpayU4U8_M4lbpdozNKvC3hza-zoEzB_Tagyd-ev03bkvI6BhnmYQw2eZYzwAjqrUh2izPSpL60dZk1Sbmk9IEugEC10dK5jH7UqbM-IJ5RcpwmJdiTXVuVxmYwp4BNO0ypd3YEsiagrOrdeq0YOG-KRUVxZuHqaH2odM6eQMrGQh4kxJLSVPC2Z1QXgOKDmvQIK6hpmWYvAA0bz3n8kqYcb4KXoNiXNxzz9qTKkr6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0647ce42a6.mp4?token=fhLUCf9yve5HvPRrL6ZFP-hihHBKAcT2Oa0Ec1bMayBH3u5ZbM2vgzhe1KSv3vAXLypk-rUIzmeK5Uh1IngVR5Vfuw3VtQn-blBOZR1bjdnmpayU4U8_M4lbpdozNKvC3hza-zoEzB_Tagyd-ev03bkvI6BhnmYQw2eZYzwAjqrUh2izPSpL60dZk1Sbmk9IEugEC10dK5jH7UqbM-IJ5RcpwmJdiTXVuVxmYwp4BNO0ypd3YEsiagrOrdeq0YOG-KRUVxZuHqaH2odM6eQMrGQh4kxJLSVPC2Z1QXgOKDmvQIK6hpmWYvAA0bz3n8kqYcb4KXoNiXNxzz9qTKkr6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار جدید جاسک ۱۵:۴۳
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19569" target="_blank">📅 16:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش ۳ انفجار‌ در‌ قشم
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19568" target="_blank">📅 15:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش انفجار ‌در جاسک دوباره الان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19567" target="_blank">📅 15:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e32e551.mp4?token=OvChLU2evE2PjZPppLoy7n1cwRKy7lMRdbVgbSGB5jQfCq86BjlN-ajghGGIO435Jvdwwa8zCHWAfBZ4y0BCQXd_qMhN1Zmi58a4pb_hPYkf5-5lYwTMtSVfQE7oW9czeiLPIrbTr0hb6TKefg84tg-2lvu3j9qakUr0UsUVx9FQRs5mCm4xU8yPkBcsJy9JbPQ1WOzoUjS9C_zE_sCAlW9rnq0oM0LLKx91CpIN5dOU-EQHgQomIr6JFAeZNdTe1nkvs6r8HLiVH9yJh6M_fa8yN8CgO88gGeWsZxzyUCexBHOJF2cKytsf-Ccn3uveTi6A3takWy6R3ZedYqCOhEmPsZF0ykWKq7qiiG-F_qg-LRbJffiyVcC3HaYv7CvfgcCNG49CcBMG53MZVDhM4i_3XUOEXgfcS-hVXBm-EayReFVo3e7iVa1Nb44UbM6YsukCtqdxBB97qeSEsm82bOtH9pGQbEbldIFgrh12iMJKdSNqYVuK9CjfEzgITOivDoZ7X3xRmOMkshiFrB_FsrEq69r5-9EkPxKxsGH_JZ0Qpl8tU0c2lA73LhOaUPThhQotc00ZyPPAdh3Io8FJ3fvuFLS2gh4M90A6pCGQRrGTzK9I22uxItdI86VNLEHQsnu5HnAmi66G9AJc4uHd9kB1rrMRSRFe-6VNOSpW0ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e32e551.mp4?token=OvChLU2evE2PjZPppLoy7n1cwRKy7lMRdbVgbSGB5jQfCq86BjlN-ajghGGIO435Jvdwwa8zCHWAfBZ4y0BCQXd_qMhN1Zmi58a4pb_hPYkf5-5lYwTMtSVfQE7oW9czeiLPIrbTr0hb6TKefg84tg-2lvu3j9qakUr0UsUVx9FQRs5mCm4xU8yPkBcsJy9JbPQ1WOzoUjS9C_zE_sCAlW9rnq0oM0LLKx91CpIN5dOU-EQHgQomIr6JFAeZNdTe1nkvs6r8HLiVH9yJh6M_fa8yN8CgO88gGeWsZxzyUCexBHOJF2cKytsf-Ccn3uveTi6A3takWy6R3ZedYqCOhEmPsZF0ykWKq7qiiG-F_qg-LRbJffiyVcC3HaYv7CvfgcCNG49CcBMG53MZVDhM4i_3XUOEXgfcS-hVXBm-EayReFVo3e7iVa1Nb44UbM6YsukCtqdxBB97qeSEsm82bOtH9pGQbEbldIFgrh12iMJKdSNqYVuK9CjfEzgITOivDoZ7X3xRmOMkshiFrB_FsrEq69r5-9EkPxKxsGH_JZ0Qpl8tU0c2lA73LhOaUPThhQotc00ZyPPAdh3Io8FJ3fvuFLS2gh4M90A6pCGQRrGTzK9I22uxItdI86VNLEHQsnu5HnAmi66G9AJc4uHd9kB1rrMRSRFe-6VNOSpW0ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله جاسک ساعت ۲:۳۰ دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19566" target="_blank">📅 15:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آمریکا: ترکیه شرایط دریافت جنگنده‌های F35 را ندارد
وزارت خارجه آمریکا در نامه‌ای به کنگره اعلام کرد ترکیه به دلیل ادامه نگهداری سامانه S400 روسی و برآورده نکردن الزامات قانونی، واجد شرایط دریافت جنگنده‌های F35 یا بازگشت به این برنامه نیست. واشینگتن در عین توصیف ترکیه به عنوان یکی از متحدان مهم ناتو، تأکید کرد در حوزه‌های دارای منافع مشترک با آنکارا همکاری خواهد کرد، اما در برابر اقداماتی که با منافع آمریکا در تضاد باشد واکنش نشان می‌دهد. این نامه همچنین ضمن قدردانی از نقش ترکیه در کمک به آتش‌بس غزه، نسبت به ادامه فعالیت شبکه‌های مالی گروه تروریستی حماس از خاک ترکیه ابراز نگرانی کرد و اعلام کرد آمریکا به هدف قرار دادن تأمین کنندگان مالی این گروه ادامه خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19565" target="_blank">📅 15:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش ارسالی : سلام.ساعت 14:30 دو انفجار در اسکله جاسک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19564" target="_blank">📅 14:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19563">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1uQq2AOIU56kPF0gfZQqDEbRMmwWW0pCqR431M3qn2q4-i1zFzuYSjgYsKZ8ioMZMOXusWVLgU2k3IYjBtINQB_adTKl8YUUyj9r8j7AmgjlgKV7sXMa6v6Z4Geww9B8LasSKBzq-hUElJr3i4a_rfQJDNPFK5BsDpYBtWad8cHyDxTizUfFi38FOd2mU-Bq7VWMACZuGaxo0xg68UjiZNJb8iHbXP_ZwNCWUfgaZQspFv3ztzeil6QYzaiqj-8RRKfGKjiALvZwTI3SUSOAN-Vfpepr7Oo9qReK6ujLwsEmcda1M-CvuQggJ5Bq16dTyCxvXCSFLQ8WzY8r5Eh1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی نقاط مورد هدف قرار گرفته در سیزده روز اخیر تا این لحظه.
@WarRoom
💥
💥
💥</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19563" target="_blank">📅 14:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19562">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سپاه در‌ بیانیه ۵۰ : ما یک پایگاه در کویت و برج کنترل نیروی دریایی پنجم در بحرین را مورد حمله قرار دادیم.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19562" target="_blank">📅 14:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19561">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ka4wKt_puKyFJjVlvDZnPJcR69xGDHTi6ai9Ktp6KM01dqruQ6P2ENkIuBmxJqmTkdMggUVbK9mnrgs6wX1ypCqnA1xRa7fNMMB_f6lUcpsDUkK26gUu8w8TQbcIaLsEA1dLJMLTpi1kXQRHAetqhhKfz3kmyOeeuzZCc83JIEftAeKlMoqrNVTtHeMZEiJsqJbycuy0cDYbJ62k5P0DvhjRkwizOBVLniB8-CGuGWW6dUZnf6hNU3Ffnnxu6gy87n3zF2DDwBZUVvU8ogKzG9dAk5a_bPQtP1cq5nA6mgzHWyqBBCYa4mpus5heQTwWBJ8M3ku52PSKGCxyO-E90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو هواپیمای مخوف جنگ الکترونیک EA-37B کامپاس کال دو، مقر انگلستان را ترک کرده و به سمت خاورمیانه در حرکت هستند. اگر بوداپست هستید، آسمان را نگاه کنید و عکس بفرستید.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19561" target="_blank">📅 13:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19560">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وال استریت ژورنال:  ترامپ در مورد ایران بیشتر به گزینه نظامی رو آورده و فعلا پلنی برای مذاکره با سران ایران نداره.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19560" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19559">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3197bdc163.mp4?token=RFNIwefaUrD0hT2Yg8jFiFsJzWiGQZDmjL4sjvtIlP9c7Nf_CmgNWKak_r868bU5LbdJw9UP6E6NDiw_iQWDM_oje53WDUzEFadwlALB7vcLtuAmc78D7usXWqIMMrfKeFX_N_zFPDmAhnvlrA_jRr_wIf2ZQdSJsJ1imnAEjm0rn9cLaKCr5NejkfVNPmmCt8kkU6LJrT6Tp0JhqBJHcQEoO5rvsFH_0ZdBRT8BJn5k7KhzooRWj8WskqnuPX_QVS5LvYeYGnQyWZGwu8ImFhWfdihP67zG_dE3ChpoFuwPXzbb5UubLU-3JgbuLnEe0Gsywgepz3VYfMuDpgRwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3197bdc163.mp4?token=RFNIwefaUrD0hT2Yg8jFiFsJzWiGQZDmjL4sjvtIlP9c7Nf_CmgNWKak_r868bU5LbdJw9UP6E6NDiw_iQWDM_oje53WDUzEFadwlALB7vcLtuAmc78D7usXWqIMMrfKeFX_N_zFPDmAhnvlrA_jRr_wIf2ZQdSJsJ1imnAEjm0rn9cLaKCr5NejkfVNPmmCt8kkU6LJrT6Tp0JhqBJHcQEoO5rvsFH_0ZdBRT8BJn5k7KhzooRWj8WskqnuPX_QVS5LvYeYGnQyWZGwu8ImFhWfdihP67zG_dE3ChpoFuwPXzbb5UubLU-3JgbuLnEe0Gsywgepz3VYfMuDpgRwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از خارک و نابودی 4 بالگرد آگوستا وستلند 109 متعلق به شرکت هلیکوپتری خلیج فارس که آنجا پروازهای امدادی و گشتی انجام میدادند.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19559" target="_blank">📅 13:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19558">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvUL6rS_jP7kQZs5-LRdz7WKFxraSGXw3i7Fk2KG9DzjizuQIWlo-xQgr0eIGeD-2y1p5QoRfpBTx3lJvQgFIbNB32MdlVCGAg1B5dm1azz40UsfcYXI4jOy-udN3nLevjOGQ6B-l5S9gCMZ6N4jPmW7tYABbBnTBALGVEb3N-HQl7kJ3hlc9HOCrdW19_6h_7MBcbeUOXgjcurF1-yi6I-mgr01IlcC8YGX4oe_TqaLdykXq2DFsQ6uq5XVvMZC2hvJJG4NTEXskK2wKmw-IEjxYD3c59_5g8cMSWfOlXyNZFI6DGV8RKvWzvcKkqmi7LPQ6Tt4EzEpG6kzpDip4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیروزآباد فارس الان
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19558" target="_blank">📅 12:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19557">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏جیک تورکس، خبرنگار ارشد کاخ سفید و نیوزمکس، نوشت که به اطلاعاتی دسترسی دارد که بسیاری از افراد از آن بی‌خبرند و با اطمینان کامل می‌گوید آمریکا برای شکست رژیم جمهوری اسلامی برنامه دارد. او افزود کارشناسان از آنچه رخ خواهد داد شگفت‌زده می‌شوند و سپس وانمود می‌کنند از ابتدا همه‌چیز را می‌دانستند.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19557" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19556">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1807f6b87b.mp4?token=ZSWwC9mXVCCZ1eplMAPZxN9RQ1jEPGS9rIOKzV_9DHRYwHAF4mhY2CoXvQsRPGkFO3WLGJDKHm4BZl1mEbZorDctNdAlrlZ7-ojVGc67C6JzOO3C4auQbjXHOZ-0L0RAM_eu5jpqkCapUTOLBQtRmYzHdzd3MyNdeMjWzO21om5NMdJQCjLfoIlijFx64SoEuGUSOSLMbxETHT89Xb2D69TKrjZGt7pNkxZuZi-CtaO-VEXf5acFawpu9PJmPpfp7tNB668Czah-u6oZxSkkv6gj7un5mmVGHtVfBfBtrm-wt0xwItyTahz0JBsf6sYkQGhCWz7dCHgHlUDPIMTsVJh-k9-1EhdWf4PlxAwRl70J8V8yoQPI8tBieieTT1bKJV1u-CmS1kL7zzelDfRLvSG6eQSUnCiXUhHxzdNwVL3mZgzhS9RiGdOBdgpcpgUZ1gUyUVhde0PhIs1ZI4f1yHogqjDBC029U3CblCAvz7UBVZ6C2H5EhhkMJNi_t-hPJmjgQyf4E-910ZeFim07PbTtULxk-I2jsvrlDGjzP2b1Zdai5twkBqAm98zUQMIojVURASd_Ffa3E8mrOlQEdf4NOSRCKY4xq6P3dBFczIDqR-B1JvBuv9wf1a0JnSMbHeYZScgpJnHoMM0MN35jNPj7GIs8RvZRkEpA6LFBGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1807f6b87b.mp4?token=ZSWwC9mXVCCZ1eplMAPZxN9RQ1jEPGS9rIOKzV_9DHRYwHAF4mhY2CoXvQsRPGkFO3WLGJDKHm4BZl1mEbZorDctNdAlrlZ7-ojVGc67C6JzOO3C4auQbjXHOZ-0L0RAM_eu5jpqkCapUTOLBQtRmYzHdzd3MyNdeMjWzO21om5NMdJQCjLfoIlijFx64SoEuGUSOSLMbxETHT89Xb2D69TKrjZGt7pNkxZuZi-CtaO-VEXf5acFawpu9PJmPpfp7tNB668Czah-u6oZxSkkv6gj7un5mmVGHtVfBfBtrm-wt0xwItyTahz0JBsf6sYkQGhCWz7dCHgHlUDPIMTsVJh-k9-1EhdWf4PlxAwRl70J8V8yoQPI8tBieieTT1bKJV1u-CmS1kL7zzelDfRLvSG6eQSUnCiXUhHxzdNwVL3mZgzhS9RiGdOBdgpcpgUZ1gUyUVhde0PhIs1ZI4f1yHogqjDBC029U3CblCAvz7UBVZ6C2H5EhhkMJNi_t-hPJmjgQyf4E-910ZeFim07PbTtULxk-I2jsvrlDGjzP2b1Zdai5twkBqAm98zUQMIojVURASd_Ffa3E8mrOlQEdf4NOSRCKY4xq6P3dBFczIDqR-B1JvBuv9wf1a0JnSMbHeYZScgpJnHoMM0MN35jNPj7GIs8RvZRkEpA6LFBGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهر خودرو خلیج فارس در اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19556" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19554">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بن غفیر وزیر امنیت ملی اسرائیل: به ازای هر یهودی که دشمن می‌کشد، دشمن باید متحمل از دست دادن زمین‌ها و خانه‌ها شود. من خواستار صدور دستوراتی به ارتش برای تخریب خانه‌های تروریست‌ها و حامیان آن‌ها خواهم بود. @WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19554" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19553">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بن غفیر وزیر امنیت ملی اسرائیل: به ازای هر یهودی که دشمن می‌کشد، دشمن باید متحمل از دست دادن زمین‌ها و خانه‌ها شود. من خواستار صدور دستوراتی به ارتش برای تخریب خانه‌های تروریست‌ها و حامیان آن‌ها خواهم بود.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19553" target="_blank">📅 11:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19552">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رسانه های داخلی : ارتش آمریکا امروز با موشک، مقر نیروی دریایی سپاه پاسداران انقلاب اسلامی را در منطقه زیباکنار، در سواحل دریای خزر در شمال کشور، مورد حمله قرار داد. خساراتی در این منطقه وارد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19552" target="_blank">📅 11:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19551">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سپاه تروریستی که جدیدأ با اسم ارتش جمهوری اسلامی فعالیت میکند اعلام کرد که با استفاده از پهپادهای "آرش"، انبارهای تجهیزات ارتش آمریکا را در پایگاه العدری، و همچنین پادگان‌های نیروها در دوحه و تعدادی از مواضع را در پایگاه عریفجان در کویت هم اکنون مورد هدف قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19551" target="_blank">📅 11:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19550">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتاق جنگ با یاشار : ده‌ها هواپیمای باری نیروی هوایی ایالات متحده (سی-۱۷ و دیگر هواپیماهای سنگین) امروز از پایگاه‌های اروپایی به خاورمیانه پرواز می‌کنند.  این یک "پل هوایی" تمام عیار است که بعد از جنگ۴۰روزه دوباره فعال شده. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19550" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19549">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqejSnp8RvTpJDmh21OdutWFP0sAy_8aY8MkpGjXZ8H26rWZBCfw1wfFp4RmD7wfPv3qHqUaElwud2hg3IjqfZf4ACxISTW6Jq8pA0W4AxNQ8vU2bapLqZ3HxKhsSfHbp1v5tsp8gd_n6BURU6RSuHwW0iECUva2ovKJcHOOJv-BlubksJNULwrPPDsTRbODc1H_PLEYW3VxYYnQCHsgV5yOj85JbJz_5SRSIEESKXNkLJNjmbgIVyu3TLUIkwyXhmjOq7ZfdxuQ4ffJA4uaXB2UR-D9vEuniqBuA52oGmC3NBNcUQUJvIqUM0n2ArcdXT42hYdmKZMDulM9TC_57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته، دو فروند بمب‌افکن
B-1B Lancer
از پایگاه
RAF Fairford
بریتانیا تقریباً همان مسیر پروازی مأموریت
«HEINZ»
را که چند روز پیش انجام شده بود، تکرار کردند.
در این مأموریت، یکی از بمب‌افکن‌ها تا منطقه تحت
(CENTCOM)
پیش رفت، اما هواپیمای دوم حدود
۶ ساعت
پرواز کرد و سپس به پایگاه خود بازگشت.
بمب‌افکن اصلی به بمب‌های
JDAM
(بمب هدایت‌شونده ماهواره‌ای که بمب‌های معمولی را به سلاح‌های دقیق تبدیل می‌کند)
مجهز بوده است.
ترکیب مأموریت بمب‌افکن (Mission LXIV):
B-1B “PURDY30”
با شماره 86-0107 و لقب
Dragon Slayer
(اژدهاکش)
B-1B “PURDY31”
با شماره 86-0138 و لقب
Seek and Destroy
(جستجو و نابودی)
دو فروند هواپیمای سوخت‌رسان
KC-135R
با شناسه‌های
BOBBY14
و
BOBBY16
که از
LROP
(محل استقرار عملیاتی بلندبرد)
مأموریت را پشتیبانی کردند.</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19549" target="_blank">📅 10:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19548">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e7b5aa30.mp4?token=WMv7cFXFpVRKs3VzfvB4cZOvXob_mvZ7jU036TISsjZYbU41xl2vkgQkzfWe6hvxTLrFmyj38UrnzKi4YbEhCHV0RmhUc23RKtTxoOXrh5Kd56iI956Em4qleKFGQ3xKR9qPBtenLOjEkcImUtm_ggEfVpxP-7PHHK27cI41hyUjBc1Ce9h38sVFaGYPfnKonU89JTxMtxkKyzPI6bM89EHUtd3f3fXqPlPQhfW3pWabI2buGQDXwC4KEB4CQ3aYhdvt8gEr2AFnCOSse8Mii_TShRxVPVlSJORn6Tyzm5XEDvy8sKqeGmBTBTVGo3VGV8zczzhD6szXxcf4DPy2gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e7b5aa30.mp4?token=WMv7cFXFpVRKs3VzfvB4cZOvXob_mvZ7jU036TISsjZYbU41xl2vkgQkzfWe6hvxTLrFmyj38UrnzKi4YbEhCHV0RmhUc23RKtTxoOXrh5Kd56iI956Em4qleKFGQ3xKR9qPBtenLOjEkcImUtm_ggEfVpxP-7PHHK27cI41hyUjBc1Ce9h38sVFaGYPfnKonU89JTxMtxkKyzPI6bM89EHUtd3f3fXqPlPQhfW3pWabI2buGQDXwC4KEB4CQ3aYhdvt8gEr2AFnCOSse8Mii_TShRxVPVlSJORn6Tyzm5XEDvy8sKqeGmBTBTVGo3VGV8zczzhD6szXxcf4DPy2gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند
ستاد فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد نیروهای این فرماندهی،
سیزدهمین شب پیاپی حملات به ایران
را
در ساعت ۹:۰۰ شب چهارشنبه ۲۳ ژوئیه به وقت شرق آمریکا (ET)
،
(ساعت ۰۴:۳۰ بامداد پنجشنبه ۲۴ ژوئیه به وقت ایران / ۲ مرداد ۱۴۰۵)
با موفقیت به پایان رساندند.
به گفته سنتکام، در این عملیات
مراکز فرماندهی نظامی، انبارهای نگهداری پهپاد، شبکه‌های ارتباطی، سایت‌های پایش و دیده‌بانی ساحلی و توانمندی‌های دریایی ایران
هدف قرار گرفتند تا تهدیدی که ایران علیه دریانوردان غیرنظامی و کشتی‌های تجاری عبوری از
تنگه هرمز
ایجاد می‌کند، بیش از پیش کاهش یابد
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/19548" target="_blank">📅 04:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19547">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فعال‌سازی پدافند شرق تهران
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/19547" target="_blank">📅 03:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19546">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش انفجار جاسک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/19546" target="_blank">📅 03:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19545">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مدیرکل مدیریت بحران استانداری هرمزگان:
در پی حمله ارتش آمریکا به محله تپه‌الله‌اکبر بندرعباس، یک تیر برق دچار شکستگی شده و پارگی سیم برق نیز در محل حادثه رخ داده است.
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/19545" target="_blank">📅 03:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19544">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کامنت برای سنتکام
😩</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19544" target="_blank">📅 03:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19543">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کنارک رو زدن
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19543" target="_blank">📅 03:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19542">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUaP2Xu3_bWjN4PjFVBh5-CDCAjwumFlixbATK_Q-4I78Y2eXAf1iNS3HPXlZMANlZ6okPXGRknQQSCnZfQDYjc71kcZ-G4UMhHjVJ25LLQx-F0b9nO8KT1Gl6riZOrFbour5Bs-AQ31F3p0Y_xh6Di8jLgHWmvagwDQOCpzikHBDPn4vEoEK1B9sXJHaFmumj36o5qfHWdDt__Nu2Vebv9li8HYKv9KERdayREs50Mgf3Ozt2i-s0C3ph8fspX3Cw9Fjozl222mo0qx71uutMEN5pcZV-R66g7Wn4Ifi90hjTcqQUMXBXaVxtLg6XqUNWc2ZnsxjQUu5PtMJXWnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش صدای انفجار خرم آباد لرستان @WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19542" target="_blank">📅 03:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19541">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش صدای انفجار خرم آباد لرستان
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19541" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19540">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2dd8c2f68.mp4?token=VCct3Yb-ahCVRnFEih7afoT2B1HHGnUb7tE9Nl_dMSy-WUyhYcSu-iJqFTKgkionTzvb8vlL57sUEoykJuwCg4ycjTGYUBrqNz5EqJIcS1NdvORfIbKWIBlT-EI-XTL7G4tPDllkE-UcAR4ycNlHC1B1ZJSU_XxZpc-SK2QFeizGaTyOuc31nBwSvQ4Q4yXt9gmAbWAxLmCdHFFAvbORvtIiKq7ZnLKmFmcGyrNuc38lMjzBd_uGzcobmoKq-6pjNZJRTbr6HTlhvX-PrdWuACTalEPv1udhu3WXw2Yp875PkFQEnRUYtsfZwl5QHoNzbcopx5gSKHxFnhqDbQXPWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2dd8c2f68.mp4?token=VCct3Yb-ahCVRnFEih7afoT2B1HHGnUb7tE9Nl_dMSy-WUyhYcSu-iJqFTKgkionTzvb8vlL57sUEoykJuwCg4ycjTGYUBrqNz5EqJIcS1NdvORfIbKWIBlT-EI-XTL7G4tPDllkE-UcAR4ycNlHC1B1ZJSU_XxZpc-SK2QFeizGaTyOuc31nBwSvQ4Q4yXt9gmAbWAxLmCdHFFAvbORvtIiKq7ZnLKmFmcGyrNuc38lMjzBd_uGzcobmoKq-6pjNZJRTbr6HTlhvX-PrdWuACTalEPv1udhu3WXw2Yp875PkFQEnRUYtsfZwl5QHoNzbcopx5gSKHxFnhqDbQXPWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19540" target="_blank">📅 03:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19539">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19539" target="_blank">📅 03:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19538">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش انفجار چابهار
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19538" target="_blank">📅 03:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19535">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88de0012c3.mp4?token=Hy25yT3MJMe7T4DDK3XsdtNuXrtvl-oxlUWbWQdc-gEgFZRgQMK3laYz8QOcJOQFmt5sNexsrqiM8E6LTj02WoG21AuBkG3IxyDwrqOs5RbHp9g-vZ6snRIwpWdY6ma856_skBWLC85fETPFwZZt5wVwVuOPj3MiJbn4UozM8Uh9UvjoZhrMX9fmQ-ZL2Jtig512N8KfbEa4gz9PXTWMgrjijrw-8jwTQEBQY46ZneJY5ZonB0dN_YXHUxs9kTWgq3H4PrtcOkeuWJc5N1kJgahxxsumehl_rKdfFqY6CeWmDo_2M_DmFbH6qpwrEfH64XlcKHCUsZ5jH63rbARABA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88de0012c3.mp4?token=Hy25yT3MJMe7T4DDK3XsdtNuXrtvl-oxlUWbWQdc-gEgFZRgQMK3laYz8QOcJOQFmt5sNexsrqiM8E6LTj02WoG21AuBkG3IxyDwrqOs5RbHp9g-vZ6snRIwpWdY6ma856_skBWLC85fETPFwZZt5wVwVuOPj3MiJbn4UozM8Uh9UvjoZhrMX9fmQ-ZL2Jtig512N8KfbEa4gz9PXTWMgrjijrw-8jwTQEBQY46ZneJY5ZonB0dN_YXHUxs9kTWgq3H4PrtcOkeuWJc5N1kJgahxxsumehl_rKdfFqY6CeWmDo_2M_DmFbH6qpwrEfH64XlcKHCUsZ5jH63rbARABA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19535" target="_blank">📅 03:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19533">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کانال ۱۴ : طرح‌های احتیاطی و تخلیه اضطراری وزارت امور خارجه ایالات متحده در سراسر جهان پس از تهدیدهای رئیس جمهور ترامپ مبنی بر حمله شدید به تأسیسات هسته‌ای مستحکم کوه پیکاکس ایران منتشر شد. از آنجا که این مجموعه در اعماق سنگ‌های سخت دفن شده است، تحلیلگران دفاعی می‌گویند واشنگتن در صورت هدف قرار گرفتن این سایت با استفاده از سلاح‌های غیرمتعارف، خود را برای انتقام شدید نظامی ایران یا حملات تروریستی آماده می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19533" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19532">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش انفجار قشمممم
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19532" target="_blank">📅 02:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19531">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734a91582b.mp4?token=c_IbFyfAZKLOjobVh00knDS1FV5sdk-YWjfNsSsStimdW3dJo9P2JKh2gUVzunGvCq4RgKqRHRZLzSZ-Aap1X55MfjzHFTrB3aswkYF0Kz43vv4C1S5sj79ORnqECKjORtXWoCz1a4md6gHIacFwJcgFzIEzcnXXJ7wAJqGqg5Tb7iBvkBv2r1pRQOHPkG0V3wroNYsHDEb1TLlQG85LSmqI1_Js3BaeNh2nkCO_9n1PB9mGhKFwTQL0zi2MOa80eqvZ0qkzg85NZG9C6SfOvqEjfSMjXlcVrc8xneagh1wQa1hjt4c3bYMOpECAs0oBNbli_tUS6yqGvzm_n0QLxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734a91582b.mp4?token=c_IbFyfAZKLOjobVh00knDS1FV5sdk-YWjfNsSsStimdW3dJo9P2JKh2gUVzunGvCq4RgKqRHRZLzSZ-Aap1X55MfjzHFTrB3aswkYF0Kz43vv4C1S5sj79ORnqECKjORtXWoCz1a4md6gHIacFwJcgFzIEzcnXXJ7wAJqGqg5Tb7iBvkBv2r1pRQOHPkG0V3wroNYsHDEb1TLlQG85LSmqI1_Js3BaeNh2nkCO_9n1PB9mGhKFwTQL0zi2MOa80eqvZ0qkzg85NZG9C6SfOvqEjfSMjXlcVrc8xneagh1wQa1hjt4c3bYMOpECAs0oBNbli_tUS6yqGvzm_n0QLxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز کل شهر شد دود
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19531" target="_blank">📅 02:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19525">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1d891257.mp4?token=eHC8Rl6JKLNpel6ATcYQVis2RtfjYa_Y3A2YxX3Cup1TBD-mF0p_GqTDQTlZKGoUp536EGoYC8JDuRGXGN92r9vQkyaI5oSckm9Jo2Uqq3YuHlLbhGktBnCR-c2ntaRBnf1nROdgm5N4xewHXQGbY4sqJHoCkVRLAksOkX5FsO6nQ9cqAF5di5M-29mW3bIgeWIMvEbOPMRAS001EZfa_4excMVriW4Dv6p6U3OKOIrv0JW5ySbGR6-hyAXyleMuRubGVW3MKo81R5AehmZwPDQCRsGc44tI54pDQvjVZoR7BUNVGrA6DcMvw4OBs3TwQc1Wh0nhU5QQ2jHULl40Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1d891257.mp4?token=eHC8Rl6JKLNpel6ATcYQVis2RtfjYa_Y3A2YxX3Cup1TBD-mF0p_GqTDQTlZKGoUp536EGoYC8JDuRGXGN92r9vQkyaI5oSckm9Jo2Uqq3YuHlLbhGktBnCR-c2ntaRBnf1nROdgm5N4xewHXQGbY4sqJHoCkVRLAksOkX5FsO6nQ9cqAF5di5M-29mW3bIgeWIMvEbOPMRAS001EZfa_4excMVriW4Dv6p6U3OKOIrv0JW5ySbGR6-hyAXyleMuRubGVW3MKo81R5AehmZwPDQCRsGc44tI54pDQvjVZoR7BUNVGrA6DcMvw4OBs3TwQc1Wh0nhU5QQ2jHULl40Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم های اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19525" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19524">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سنتکام : شب ۱۳ هم شروع شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19524" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19523">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19523" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19522">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بندر عباس شروع شد
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19522" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19521">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMX_FSSQL-00hKXn22iNnscjH1KksLlAYsL7ixnEoCraq51R4eWU1UnhojZTxVtld64n7GN1RwUgD-FO7alHDFhA7Eu_i83z0diw_ht-WnC3rNqdFUkgXOyHsSMmh7xNS3gvCoR5YiTVDScU8R8gfcczJ3NITKfxpLH5QdVZyPrj9InWsJq3aIQneTNr-GnvrRgn9rlFgdjHicsuoFMORrPIo-LAUuAwYR4X4Ot_r-KOQxLYuCUxpUtVAQinZM9YD8p9q16MTa-lmdpNW-is66LdsJBhz3v5ZrBv1u3xnGFo86KfA_s49ljRJynC17cAvz3-Cky20zQuWs_Lv6uQCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : بمباران اهواز توسط هواپیمای بمب افکن B-1
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19521" target="_blank">📅 02:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19520">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19520" target="_blank">📅 02:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19519">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19519" target="_blank">📅 02:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19518">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اتاق جنگ با یاشار : سرطان  حتما تا اخر ببینید و نظرتون رو کامنت کنید میخونم کارای اداری یادتون نره مخصوصا اد تو استوری و ریشیر  https://www.instagram.com/reel/DbJowDnR54h/?igsh=MW0yMnB5cG5pa2FyNQ==</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19518" target="_blank">📅 02:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19517">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19517" target="_blank">📅 02:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19516">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اهواز‌ ادامه داره همچنان….</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19516" target="_blank">📅 02:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19515">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اهواز انفجار ها زیاد بود حتی‌ بیشتر از ۱۰ عدد گزارش شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19515" target="_blank">📅 02:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19514">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">۳ انفجار مهیب اهواز
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19514" target="_blank">📅 02:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19513">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اهوازمممم زدن بدددددم زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19513" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19512">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">صدای انفجار رگبرای قشم
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19512" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19511">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19511" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19510">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شروع شدددددد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19510" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19509">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال ۱۴ : ارتش ایران، ستاد ارتش کویت را هدف قرار داد. این اقدام پس از ادعاهای ایران مبنی بر اینکه نیروهای کویتی مستقر در این پایگاه، پیش از این گذرگاه مرزی شلمچه را هدف قرار داده بودند، صورت می‌گیرد. اخبار تکمیلی متعاقباً اعلام خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19509" target="_blank">📅 02:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19508">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d7eae30c1.mp4?token=hYDyVnVWZTQtF-6HHl2Gm7E_AEgAHccIxGcz3VUkwGMXIIJA4O4tWDScxoI3cpFU8lWjDDPw59-t34XIxr2U8WF2OHlRpNgnE-rlTDYEnv6K8rY2zHC9Wlw6BPDY6Zfpu5P7aaV80KRlFAz9Ob5TBY0MgiG_hmiWnvfgdav_TZBH7fEazrU4RpBT67qhF1pgShTNkjWULGAj4dzmynEZF4IR7i66nrfg1iQ9sNH0jd_ax7WE2B8ctJuzwi7-maP6vleCMcPvOx_rBYUnYzZPJ_gY13XtbLsn6q2nZMs2RA_GE2CjGevae1ffBnefuUWxEXucl2ER2aoM9SFQCSG2nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d7eae30c1.mp4?token=hYDyVnVWZTQtF-6HHl2Gm7E_AEgAHccIxGcz3VUkwGMXIIJA4O4tWDScxoI3cpFU8lWjDDPw59-t34XIxr2U8WF2OHlRpNgnE-rlTDYEnv6K8rY2zHC9Wlw6BPDY6Zfpu5P7aaV80KRlFAz9Ob5TBY0MgiG_hmiWnvfgdav_TZBH7fEazrU4RpBT67qhF1pgShTNkjWULGAj4dzmynEZF4IR7i66nrfg1iQ9sNH0jd_ax7WE2B8ctJuzwi7-maP6vleCMcPvOx_rBYUnYzZPJ_gY13XtbLsn6q2nZMs2RA_GE2CjGevae1ffBnefuUWxEXucl2ER2aoM9SFQCSG2nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط شیء پرنده ناشناس در قشم
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19508" target="_blank">📅 02:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19507">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q57VJ9bRBJufqz2jpt9PWz5R9l6KoDBTBS03s4hKtKlE22QUWFWSNjv7sukxlU3wc6QXiu1tyt7BAMxS6U79zLOGjYivGLUFFDX2CMLaCctRVNhUs1y2SDMjghpoKrTxJsO_zIP7L6R6xpJSVYshaUl9tvjfUenVHPYZbsFdSiLfU6HIqkGKtJXkd5DiZ81auKLYPtnxtBJgA1PB7iIZshPy3ExehDlmYlJAeJ3IbYV7bLtCuBn5vb3DSX1U_evCKbeHpqbyKZ3KgnLG5VL1KFwt2ayprBxpZ4jx8_uf9r50eu-0cxJ1TNIwFzAah4E24Z3Yi-gYo4aBH5nJGZnYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث
:
از این لحظه به بعد، هرگونه خسارتی که به کشتی‌ها، کالاها یا هر چیزی مرتبط با آن‌ها وارد شود، از طریق وجوه متعلق به ایران که در حال حاضر در اختیار ایالات متحده قرار دارد جبران خواهد شد.
ممکن است این خسارت‌ها قابل‌توجه باشند، اما با وجود این، این اقدام عادلانه و درست است و باید انجام شود.
از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19507" target="_blank">📅 01:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19506">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19506" target="_blank">📅 01:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19505">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برمیگردم
😉
من جنگامو کردم که اومدم اتاق جنگ</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19505" target="_blank">📅 01:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19504">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQWBEYVGWw-JADpU01SR5Rnah_1vp4HWzlPR0TAPkuRnVJVZ-LYyyh2w1-2xnwNHVzwSfohPtbzuzpiBrou47F5WV4VYNqo5_jqz6ZCpERLPge5xkyFtKjHtbvaqy0BTj5zrKWr95NPbdsdAEJ3DDPuxj0N5Olg9TpAA4XhnjmCNv-8NG0KnBhlhV1PWz1ITdsG8h2GDU0hDTGAXSpS-sCAZpGTc-Fjz8jB-v6L9UqUB4uPTGWm7ZReynH_EuLO9QaO4qT29OycD5lEIbtwQcNqcsnQyZ6DwsJ8psC0RnBcoBZiHrBwjOOUcFlgHNBsB2bGUxkRfXHnIs39rkpjfmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : سرطان
حتما تا اخر ببینید و نظرتون رو کامنت کنید میخونم
کارای اداری یادتون نره مخصوصا اد تو استوری و ریشیر
https://www.instagram.com/reel/DbJowDnR54h/?igsh=MW0yMnB5cG5pa2FyNQ==</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19504" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19503">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش انفجار های شدید و پیاپی در تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19503" target="_blank">📅 01:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19502">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پرتاب موشک‌های کروز ضدکشتی به سمت تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19502" target="_blank">📅 00:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19501">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نیویورک تایمز:نخست‌وزیر عراق، در جریان سفر خود به تهران، پیشنهادی را ارائه کرده بود مبنی بر برقراری آتش‌بس بین ایران و ایالات متحده
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19501" target="_blank">📅 00:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19500">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ایران به پاکستان هشدار داده است:درصورت وقوع هرگونه حمله تروریستی علیه ایران، با تمام توان و قدرت خود دست به اقدام تلافی‌جویانه خواهد زد
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19500" target="_blank">📅 00:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19499">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال ۱۳ عبری: نهادهای اطلاعاتی غرب بر این باورند که ممکن است ایران آغازگر اقدام علیه اسرائیل باشد
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19499" target="_blank">📅 00:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19498">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd98bed83.mp4?token=u_f01H_TJUCisO16071cOSFtPuJdT__LHcD6LXVCR1sn1cVBfw6-_IIyhcMMTFuwyZVC-OFGcNJR7mKaMMS1TTM_hoLZIJZqujrWE68CKUycWfDQr-wEWgQf0DoserZf0sxjQo59wkAhxnHK9dAC1ds1rNe05cc15kIWqKX5UI34xC76Bi1wK4J7AUVIEuEyvSbBLKo739HjJv-79sC3qisLJXCZDKMrQ1cuUii0OWzUKFeMlZfPRAHvmAaqZCd12NgFKJLYN2dj3Q944Kb4YzTVwoLk300YzYgi14FQxLi72PUGZkXhCiCfSTGLSweNsy-t4AI1p9qqNRlIEa30Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd98bed83.mp4?token=u_f01H_TJUCisO16071cOSFtPuJdT__LHcD6LXVCR1sn1cVBfw6-_IIyhcMMTFuwyZVC-OFGcNJR7mKaMMS1TTM_hoLZIJZqujrWE68CKUycWfDQr-wEWgQf0DoserZf0sxjQo59wkAhxnHK9dAC1ds1rNe05cc15kIWqKX5UI34xC76Bi1wK4J7AUVIEuEyvSbBLKo739HjJv-79sC3qisLJXCZDKMrQ1cuUii0OWzUKFeMlZfPRAHvmAaqZCd12NgFKJLYN2dj3Q944Kb4YzTVwoLk300YzYgi14FQxLi72PUGZkXhCiCfSTGLSweNsy-t4AI1p9qqNRlIEa30Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ده‌ها هواپیمای باری نیروی هوایی ایالات متحده (سی-۱۷ و دیگر هواپیماهای سنگین) امروز از پایگاه‌های اروپایی به خاورمیانه پرواز می‌کنند.
این یک "پل هوایی" تمام عیار است که بعد از جنگ۴۰روزه دوباره فعال شده.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19498" target="_blank">📅 00:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19497">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رسانه های عراقی : در حال حاضر، هواپیماهای جنگنده آمریکایی بر فراز عراق پرواز می‌کنند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19497" target="_blank">📅 00:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19496">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارشهای مبنی بر دو موشک آمریکایی در نزدیکی روستای مسن در جزیره قشم اصابت کردند.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19496" target="_blank">📅 00:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19495">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19495" target="_blank">📅 00:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19494">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19494" target="_blank">📅 00:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19493">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیویورک پست : روز چهارشنبه، یک حمله دیگر از سوی ایران توانست سامانه‌های پدافند هوایی آمریکا را نفوذ کرده و به یک انبار سلاح در نزدیکی همان پایگاهی اصابت کند که سه سرباز آمریکایی در آن در اردن کشته شدند. این حمله منجر به انفجار شد و در نتیجه، یک "ابر قارچ" شکل گرفت.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19493" target="_blank">📅 00:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19492">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مقامات ایران آخرین پیشنهاد ارائه شده از سوی میانجی‌ها رو هم قبول نکردن.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19492" target="_blank">📅 23:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19491">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Tether = 194,850 Toman
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19491" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19490">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آلارم حمله موشکی روی موبایل های کویت اومد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19490" target="_blank">📅 23:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19489">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">از اهواز ۳ موشک با صدای مهیب زدن سمت کویت
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19489" target="_blank">📅 23:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19488">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbfb1bbbe.mp4?token=PVpNuBZnhvfLdCDrUQJ6q8P9W2r6pv2bQCZjjG8bdJ0scq3uQ8kOxueGawyCrQwbRx13sH43IGaKLgTsQVa-jwbWTIIlhQIauoJbePNtfFPqRWFdWNbETEHrH7vee7pjXrDyLOcB_9HHNBqBsj_ehBRjW1UrTWR7QlWonshQr3zaB5yrMqumZHogf_E8YW5LTCEwQL87FueGO-BBoeruFtkHTeS6jCwPoNpuwdzPwGiokkE1NLxMb09G4tcceSMDdXt-UsYYqXJbbnUEzsdhCNqb7LbPSPkZNtemihrdbKhTno_07c8FHeDApY-qtccv6IkdCYiQPrRl98vUoNWzwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbfb1bbbe.mp4?token=PVpNuBZnhvfLdCDrUQJ6q8P9W2r6pv2bQCZjjG8bdJ0scq3uQ8kOxueGawyCrQwbRx13sH43IGaKLgTsQVa-jwbWTIIlhQIauoJbePNtfFPqRWFdWNbETEHrH7vee7pjXrDyLOcB_9HHNBqBsj_ehBRjW1UrTWR7QlWonshQr3zaB5yrMqumZHogf_E8YW5LTCEwQL87FueGO-BBoeruFtkHTeS6jCwPoNpuwdzPwGiokkE1NLxMb09G4tcceSMDdXt-UsYYqXJbbnUEzsdhCNqb7LbPSPkZNtemihrdbKhTno_07c8FHeDApY-qtccv6IkdCYiQPrRl98vUoNWzwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون کیش
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19488" target="_blank">📅 23:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19487">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: ایران دیگر ارتش ندارد، فقط افرادی باهوش و آقای ماکرون(رئیس جمهور فرانسه) را دارد، اما همچنان سطح مشخصی از توانایی‌ها را حفظ کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19487" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19486">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07325a864.mp4?token=WRr8j7iNsC-Qs64irF0GrXx8JeGbN-aIPYjAq-DOPouEd_zdQuxit2OOeGRE6GA40bvknxnTjMtBolHx4poqsOUgb-G2ocbKEJN2tjxSBgit-L1sfgA6woR9tYUjGlAjR6MB3iPkI4tVn3CXJ5k54kQdoNr6mI3z6asr_IdFB_IoEAinGtsvvoCR4XrTc27D_e1-457vmyvdXrjbGJ9r1MAk1g28sYI6EbF5HD99Yg0rQbOFcBiSILD2ip79ppv1Xjv4BHsl0PQ2hV_PVtQ5nCMzXtKaHwa-maO6fTHwf2sAMi6n4FUR0ua9CZAPCN2rNYwr3w6-aeTv88ITVcQLfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07325a864.mp4?token=WRr8j7iNsC-Qs64irF0GrXx8JeGbN-aIPYjAq-DOPouEd_zdQuxit2OOeGRE6GA40bvknxnTjMtBolHx4poqsOUgb-G2ocbKEJN2tjxSBgit-L1sfgA6woR9tYUjGlAjR6MB3iPkI4tVn3CXJ5k54kQdoNr6mI3z6asr_IdFB_IoEAinGtsvvoCR4XrTc27D_e1-457vmyvdXrjbGJ9r1MAk1g28sYI6EbF5HD99Yg0rQbOFcBiSILD2ip79ppv1Xjv4BHsl0PQ2hV_PVtQ5nCMzXtKaHwa-maO6fTHwf2sAMi6n4FUR0ua9CZAPCN2rNYwr3w6-aeTv88ITVcQLfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ،: «
ما در برابر جمهوری اسلامی ایران خیلی خوب عمل می‌کنیم، ما فوق‌العاده خوب عمل می‌کنیم
»
«آنها دوست دارند کاری انجام دهند، اما من می‌گویم که هنوز آماده نیستند.»
«آنها به چیزهای بیشتری از این دست نیاز دارند. آنها نیات شومی دارند.»
«جنگ ایران بهتر از آنچه هر کسی انتظار داشت، پیش می‌رود.»
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19486" target="_blank">📅 22:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19485">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1c7f0727d.mp4?token=CTp3mv9iYQaA265G83iM84b6VB--6kOATlNkE97w5mykoTYHqziTybmhjcnyhqh6PUToXTFrKm7yeZmHUupv-3JplwafImwJoseOuo0urieUI9gGZ9gPBQh3cxeiznFV7NbavhAPVX0_xusFwBhqTg1x3RPkVH9_IC4eSEE4N5-9DMPh7mPhJ_v-3-CyhBVa6lVT2oZwPeYjFPeqgdESUvZbJP8REkaDuMWUfARL78UVco8nDdcXnefDRM9JMnHtm0x24FoD91f3eG2wa8GZwRMe2Twv2EIOMvaRWlKZPupiSbkqKYH2v6hSAYKUQx2Nxcm50g6CfwvWY5eDzN2nLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1c7f0727d.mp4?token=CTp3mv9iYQaA265G83iM84b6VB--6kOATlNkE97w5mykoTYHqziTybmhjcnyhqh6PUToXTFrKm7yeZmHUupv-3JplwafImwJoseOuo0urieUI9gGZ9gPBQh3cxeiznFV7NbavhAPVX0_xusFwBhqTg1x3RPkVH9_IC4eSEE4N5-9DMPh7mPhJ_v-3-CyhBVa6lVT2oZwPeYjFPeqgdESUvZbJP8REkaDuMWUfARL78UVco8nDdcXnefDRM9JMnHtm0x24FoD91f3eG2wa8GZwRMe2Twv2EIOMvaRWlKZPupiSbkqKYH2v6hSAYKUQx2Nxcm50g6CfwvWY5eDzN2nLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران هیچ نیروی نظامی ندارد.
آنها هیچ چیز دیگری ندارند جز اینکه شرور و باهوش هستند و هنوز هم توانایی‌هایی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19485" target="_blank">📅 22:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19484">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed657c044.mp4?token=ZRsSQMVtF3veD_ICiEttBOZKinnz67nV_Xa8O5_CXUWk06ZpItTmFApm4YS49dUr0bwdb62PuOuWfNzKn6pk84XncH-E09r1BsaCwkaJmvYvpG1jFE8VtsPQRgPRIO2FwVmahY_XCglEOmlRUkaivijS-zh_S487d7cUizgNifTfvrfPxIYwT2oGy9X5Vm7FRqCpNQLgc97u9vUscD7iD4IqPRqfpbbw1O9VCaU6c0R63QYfC_uyqHw0lsbMzCmqcdLjnVStND5tgXoBDEzVd9hA7NkQEVJu-nOPUvfVF7IvezXD7_FfgzvVryBGTyHneQMnL0BtogW5_PagYlEDUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed657c044.mp4?token=ZRsSQMVtF3veD_ICiEttBOZKinnz67nV_Xa8O5_CXUWk06ZpItTmFApm4YS49dUr0bwdb62PuOuWfNzKn6pk84XncH-E09r1BsaCwkaJmvYvpG1jFE8VtsPQRgPRIO2FwVmahY_XCglEOmlRUkaivijS-zh_S487d7cUizgNifTfvrfPxIYwT2oGy9X5Vm7FRqCpNQLgc97u9vUscD7iD4IqPRqfpbbw1O9VCaU6c0R63QYfC_uyqHw0lsbMzCmqcdLjnVStND5tgXoBDEzVd9hA7NkQEVJu-nOPUvfVF7IvezXD7_FfgzvVryBGTyHneQMnL0BtogW5_PagYlEDUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام  : از زمان از سرگیری محاصره دریایی علیه ایران در نه روز پیش، سنتکام ۱۲ کشتی تجاری را تغییر مسیر داده و ۱ کشتی را از کار انداخته است تا از ورود یا خروج کشتی‌ها به بنادر یا مناطق ساحلی ایران جلوگیری کند.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19484" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19483">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شبکه12 اسرائیل : مقامات آمریکایی به همتایان خود در اسرائیل، آماده‌باش ابلاغ کردند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19483" target="_blank">📅 22:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19482">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">منابع عربی: کره شمالی در حال تخلیه سفارت خود در تهران است.
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19482" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19481">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش کامل فاکس نیوز با موضوع حمله به قلب انرژی ایران که امروز بیشترین دایرکت و درخواست رو در مورد این گزارش داده بودید. ویدیو کامل به همراه زیرنویس فارسی.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19481" target="_blank">📅 21:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USb6SaJY52wmGDkEmuJBiOiMrd8UIJzaHJeKBiZTuXMwsT77sgbxurbFUqpnDlC_T7dJ-95BXQ1V3Or3H1njp5I-x4MDJrtrxRGpjF5kjbcIvPTexkqMdPtiLrCbyjR396229p7JdzEy3t1uaWwZ16Epry9heztenovDpCScQDwvhC4S7-YaAjQThKfm94-4tfADO2nCcwm-qxQX5aQAbb549ptcyvRebkLLJwYYsZXgVyLCrUalVi5degoyQmDrwkXo45vuVQ8ZMenCfryMcuBQuKhyMi3H4WIhpkudtNtrQtavIGOaSoJ851A2-R7_qfGtuicFk5xmD7lgBGmkhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون؛ نفس های آخر رژیم
،
استقرار
موشک ذوالفقار در میدان آزادی
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19480" target="_blank">📅 21:15 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
