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
<img src="https://cdn1.telesco.pe/file/Jds4-Io9qVtXUK2l-nEwbPA35045DmRN0HtujKSroms2MyRFTB7MXMGjTNrBs7RG3ry6D8V4EmtqEWPAmjdyIua1wIBMInf4FV2jlfl5kJiHKHSu0lfItb7sNX1_ZTS5PMpsi6O_InH0alQVq5x_Vki5_xpYeOFyqI7CSwvCKD9eX1LK-NGww0KfGHVbjg4ByweA_T6VMTemysnCauTdK7AVCenw1Jp_YZDTYz-W1QcTeHeunEb-97NLXuk9kjPijIoXhqSK1x3sYVgRq4sI79-fPe4iIrI7cKChSzZULh26IqWCnEA1VVKH2oOARhNzLe4LCxus1rFi1tfOtHgtWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.39M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی می‌گن. اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جوری که می‌خواستم به خودم نشون داده بشن می‌گذارم.ممنون از حمایت‌های ماهانهvhdo.nl/patreonیا گاهانهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 03:10:30</div>
<hr>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGV_rl36el1bsFqJt4WMrwzkZ_cL5eXHS5lcw-nVI7KlOE3JoUs4mosT_jThUKErRDdc0w8nhX-7RvQdPEWk1JrAUgk_BUoBP6MN2r0l9_TywTzdaPIGh1kOK7yT-auCOHJXPxooLS0X3udFMl30Ca3b40sFZxOHZXN61wtniW6WkfwmWaGfzrEXUVs6hA-h2a6Je5S4zjyvlQy3EWAAAvgap-ULbET9l-LnqB4EcaxGV2ajOHxeAiaS9JwMlAzz16EmDhzN9Cqpqpbhwu2KzKTeeDuy15H2XX_J7fJPf3jmXRCxF_hAzcuj4xNDGFqSa9lFcNSuWoAJyvSaxaa-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای ائتلاف تحت رهبری سعودی اعلام کرد که پدافند هوایی این کشور موفق شده است آتش موشک‌های ورودی از یمن را با موفقیت رهگیری و منهدم کند.
دوشنبه شب، ۲۰ مهر دقایقی پس از ارسال پیامک هشدار تهدید هوایی به تلفن همراه ساکنان، چندین انفجار مهیب پایتخت عربستان سعودی، ریاض، را لرزاند که به احتمال زیاد ناشی از عملکرد همین موشک‌های رهگیر پدافند در انهدام پرتابه‌ها بوده است. سازمان دفاع مدنی عربستان سعودی حدود ۱۰ دقیقه پس از اعلام وضعیت هشدار، به شهروندان اطلاع داد که خطر رفع شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/VahidOnline/78704" target="_blank">📅 22:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qCBLgebvsf67Tq3n4XwkUZM6WzHpteBUp6IzX4BXQUZigWLkYCfgg_3wViyEllOljNK9BN7mLloPtgNh_701SZcCkcPhXXEwnk1OMmWmjtM9WfiLdHf91XZMNJLfeEgIaVCso8vSKb4n5J48oDG-mX5gD6g7rtOD3JoMGu8e_2y1E4nbk9qQpscVkGNl58DM0paDWQYUajQdPNtH2df8sp4ZLBsiWy6IYPDedT-xb2qEsx1Hjm0KVJtp4Z5afsvUuSMbuejpNcblLAJXOuSQpJzRt_lpgvmPRqzpbT6ojA4RCdQAkXxoBI5g8g74JCAX8TscSGidl_Sbnb-C7iWmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی با تأخیر از وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک منبع تأییدشده گزارش داده است که یک نفتکش حامل نفت خام هنگام خروج از تنگه هرمز، هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
مقام‌های مسئول در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/VahidOnline/78703" target="_blank">📅 22:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HniOXcDj2Y5u_gZxHm7fAuLNYswXyqsqhtnxTOM0cazUY5rCi0QPwWjVPH76pSZgBkAkxlnHXqPrY486AIlkpdu6Dn7IEKJllElbXEIIUUdPK0ED6R02UIbXGOliowo7UOP_UMSy04M79hoJvqvXyNLlD6ljU7iIDzwJxefO2gXYKyGsXYUpp1lM9gPipydv4KB4o87qxLNO36h1hjaF_zRBs4OZffoPCglzq3CpMShime8uqu8O2k8ueldzAmcSpMBlsBzp-4TuRfviRhjlCt67DBcwKSUDapHGm13o7J-k9DmYprdncyt5tLU-8ZpneehBwSNaXaIb65xo2sn_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیران خارجه ایالات متحده، بریتانیا، استرالیا، کانادا و ۲۳ کشور دیگر با انتشار بیانیه‌ای مشترک، فعالیت‌های خصمانه جمهوری اسلامی ایران در خارج از مرزها را به شدت محکوم کردند.
این بیانیه روز دوشنبه ۲۰ مهر، پس از آن صادر شد که اندی برنهام، نخست‌وزیر بریتانیا، اعلام کرد حادثه امنیتی اخیر در پایگاه هوایی فیرفورد در انگلستان «تقریبا به طور قطع» توسط سپاه پاسداران انقلاب اسلامی هدایت شده است.
کشورهای امضاکننده این بیانیه با اشاره به ماجرای پایگاه فیرفورد و سایر حملات اخیر علیه جوامع یهودی، روزنامه‌نگاران ایرانی و منافع ایالات متحده در اروپا، تاکید کردند که استفاده جمهوری اسلامی ایران از حملات خشونت‌آمیز، توطئه‌های مرگبار، آتش‌سوزی عمدی، خرابکاری و عملیات سایبری غیرقابل قبول است. آن‌ها هشدار دادند که هرگونه تلاش برای تهدید، ارعاب یا آسیب رساندن به افراد در خاک این کشورها با اقدام قاطع قانونی مواجه خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/78702" target="_blank">📅 21:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac0389fe6d.mp4?token=qazHE7CGgpfcdDjtGnxvuEpwKkU7Qk_U1OEU_hyF1HkQDrvZMK1iA8oc84NVcqlk04UtCrCTvckqDe7xzmA8AtqRl5NhqMSkB3xw57m5pcPxeIDTqfMUFrIvmtGYLYZYinq4HAMAoZ28kff5IFMqzRzPnigvHMHWoWFtwjct-lLVml55lomrzlwAJ5aLybR1efial8123T9cp7FF1YJ7QdOAoDvKPkh_so8LsXYYek75-seGlwrSUvrcTAWahh8mh5WFWUfk2soMrcGOMC_suuNOP6ELWEc8wqJ7XnZ-cWkZJRPv6zMUm3hTBHlwmg2tUCBIYk_USvlO9MGEtGWXWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac0389fe6d.mp4?token=qazHE7CGgpfcdDjtGnxvuEpwKkU7Qk_U1OEU_hyF1HkQDrvZMK1iA8oc84NVcqlk04UtCrCTvckqDe7xzmA8AtqRl5NhqMSkB3xw57m5pcPxeIDTqfMUFrIvmtGYLYZYinq4HAMAoZ28kff5IFMqzRzPnigvHMHWoWFtwjct-lLVml55lomrzlwAJ5aLybR1efial8123T9cp7FF1YJ7QdOAoDvKPkh_so8LsXYYek75-seGlwrSUvrcTAWahh8mh5WFWUfk2soMrcGOMC_suuNOP6ELWEc8wqJ7XnZ-cWkZJRPv6zMUm3hTBHlwmg2tUCBIYk_USvlO9MGEtGWXWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر بریتانیا روز دوشنبه ۲۰ مهر گفت طرح مشکوکی که پایگاه هوایی «آرای‌اف فرفورد» در بریتانیا را هدف قرار داده بود، «به احتمال بسیار زیاد» در ایران هماهنگ شده و قریب به یقین زیر نظر سپاه پاسداران انقلاب اسلامی هدایت شده است.
اندی برنهام در سخنانی در پارلمان گفت: «ما این تهدیدها را در خاک خود تحمل نخواهیم کرد. با استفاده ایران از شبکه‌های جنایتکار برخورد قاطع خواهیم کرد، با به‌کارگیری همهٔ اختیارات‌مان، این شبکه‌ها و منابع مالی آن‌ها را هدف قرار می‌دهیم و تحریم‌های بیشتری اعمال خواهیم کرد تا توان ایران و سپاه پاسداران برای آسیب‌رساندن به ما محدود شود».
اد میلیبند، وزیر خارجه بریتانیا، نیز خبر داد که در واکنش به این اقدام، سفیر جمهوری اسلامی ایران در لندن به وزارت خارجه احضار شده است.
پلیس بریتانیا روز یکشنبه پنجم مهر پنج مرد را در نزدیکی پایگاه هوایی «فِرفورد» در جنوب غربی این کشور به ظن ارتکاب جرایم مرتبط با مواد منفجره و تروریسم بازداشت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/78701" target="_blank">📅 20:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78700">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAB11-yb6VcHdte7e4oQa9zxUliXobElnqvhfZyuUEW9CvX658ArXLziTh8UHYG0eIEO9in-mBGL556bqnsUhLgRTd2y-CurqwxMdIuUF71da1baYng5YZmYJIxOFxLfjwILKj7KnKeTQDP2_047iQ4JZPWrJlgHIAiJSvO0pQxN8JOA3s7RPWfeM-fgA_S75g4AugaxE8NIKf8go73b3ObV0AJTFp1mPstTafABD7yQCxw2uyNu-3_dwVr2P_OuNU-LaI0NO7PS0LU-MToUM_tm9EE7MnKtkeb2VTb9zhVzh5IN3oozrFXg680JMJBMkP2n-g-wvrgu4KmGX9o0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، درباره حادثه پایگاه هوایی فرفورد، دوشنبه ۲۰ مهر گفت که به احتمال زیاد این اقدام در ایران هماهنگ شده و به دستور سپاه پاسداران انجام شده است.
نخست‌وزیر بریتانیا در واکنش به این حادثه اعلام کرد که دولت این کشور تحریم‌های بیشتری علیه جمهوری اسلامی اعمال خواهد کرد.
بریتانیا در تازه‌ترین بسته تحریمی علیه جمهوری اسلامی، دو شهروند ایرانی را به اتهام دست داشتن در فعالیت‌های خصمانه، از جمله جاسوسی و مشارکت در تهدید یا طراحی حملات علیه افراد در خارج از ایران، تحریم کرد.
دولت بریتانیا روح‌الله بازقندی و شهرام علیرضا تمرزاده جکی را به فهرست تحریم‌های خود اضافه کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/78700" target="_blank">📅 18:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78699">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHLaaSfcAbNBwz8NfHxq3EG_NEpVHZHk8Kl_1EZhzzWdPuisyNpNpUKESyEiUZY3KByRHxsEIc-ckUbggZExGBNpdWY9iefL9JR5kdwsnKxCrRLz71OwYUKL0OHcsOFyDkWWAs-OMU3-UBDrte7X99P7KuCJSth2VzMPu1tSg2EfdrcAAPaUYOVJThNIU9-gC8ujbBtwKJLKfwa4_OgH2sY65vBSERiqC960nsMHT8hI-JQC3dLuxbZ8HrRsqKAaeCMB3nkBdcXnkTnOMqkVMSULjcs_Qvcys-xi181i4hiPs2Xo_vDvx1Z5joj4bs-GFUGKT3epoRLE1zCyuCyA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز دوشنبه ۲۰ مهر گزارش داد در پی حملات حوثی‌های مورد حمایت جمهوری اسلامی به فرودگاه ریاض، چند شرکت هواپیمایی بین‌المللی پروازهای خود به عربستان سعودی را لغو یا تعلیق کرده‌اند.
بر اساس این گزارش، ایرفرانس-کی‌ال‌ام تعلیق پروازهای رفت‌وبرگشت ریاض را تا ۹ آبان تمدید کرده و گروه لوفت‌هانزا نیز تمامی پروازهای خود به این شهر را تا ۲۴ مهر لغو کرده است.
شرکت هواپیمایی اتحاد تمامی پروازهای خود به عربستان سعودی را تا ۲۱ مهر و شرکت هندی ایندیگو پروازهای ریاض و دمام را تا ۲۳ مهر تعلیق کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78699" target="_blank">📅 17:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rz56sdKT6GnTP4PzPtAvgaixfZz7wQWsEUD_lauBADWKd9RncuGPN6jaguHh2xfbqf3Zp73vp49NQ9-HY1cdhceJMpfOiz8TtiJ_swjLsd4Z1Yw1yh2eR0vOdSgcJUZXr9EEMOzDpp5YfGhivoKskX0jowJErv6TMEEJr50Atmmx0C5kGFQQnc6CxiI5IIQiIwctRmkRrxs5vwwYL0rIXJPH1E8FnHgRGyOfE59NFFYpnldF9b49pZLkM1uSJiriKpVOHp4n1-b5ttY0gS1nuXSiM3fVCgrhMo6nlWEKR8n7uWQL427kEewsc5jn2vQdR48MzBEJb18IQ1tIAqfhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rOwuax9l59H4BBoRKeDITd0L8_kldN4dfr84gbWDb-dzr1BKj7GoNfA6ONcApyLnrS4Xdxxt3zUMOk8onC9AGRMwq3X7skA8Vk1_Vt_xDZLLq3hPiRA5ncLc7nlG-cN1l5O5f6sesnhwd9TMnqRjKse35NIZHl_bKVOeZIkRx-KnwpW2PjpytwQOOxUoUimEINao_4bdJPKbCjFmHZsUTSqax1E9pbyqr3qOz-sEMPVE3hWgJ_0t_eCnTFrnPTXgeMEQE9XpWWwSiSGkGYz2kKKAOPQuEOHwJ0LxkiHwhBmDWKfxaWvUbmqhd9QDEPSPgqJs_UMmQYt2O4AHpspZeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی می‌گوید که روز دوشنبه یک «عضو» گروه جیش‌العدل را اعدام کرده است.
میزان، خبرگزاری قوه قضائیه، می‌گوید که عمر درستاران به اتهام «بغی» (قیام مسلحانه) و عضویت در جیش‌العدل محاکمه و به اعدام محکوم شده بود.
میزان می‌گوید برخی از اتهامات آقای دستاران مربوط به حملاتی است که به مقر انتظامی شهرستان راسک، مقر سپاه شهرستان راسک، پایگاه پارود، و مقر‌های نظامی در فروردین سال ۱۴۰۳ در شهرستان چابهار صورت گرفته است.
به ادعای این خبرگزاری، تهیه محل اسکان اعضای گروه، تسهیل ورود این افراد به کشور، جابجایی تیم‌های عملیاتی برای انجام حملات مسلحانه، تهیه مهمات و سلاح و شناسایی مقرهای نظامی از جملات اقدامات عمر درستاران بوده است.
به گفته فعالان حقوق بشر عمر درستاران، ۲۷ ساله و اهل روستای چراغان شهرستان راسک در سیستان و بلوچستان و از طلاب مدرسه دینی شهر پیشین و از شاگردان سابق مولوی نقشبنید بوده است و از فرودین ماه سال ۱۴۰۳ در ایران زندانی شده بود.
تعداد احکام مجازات اعدام و اجرای آن در ایران از دی‌ماه ۱۴۰۴ به‌شدت افزایش یافته است. موارد اعدام به جرایم امنیتی هم بسیار بیشتر از سال‌های گذشته برآورد می‌شود.
@
VahidOnLive
, @
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78697" target="_blank">📅 17:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78695">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eD_xsGg78FRa4NIyzdp3cIpr50FSESQ_Ez_wtKbwgNmfQQ209uQ9f4EHQBGrgZDRGfB7Fi8nkpIufbl7j4gKTl__nSZ4Q8spTayPhgEMInFytXH5cRRVOF7arfB44zCb19acWv3p79o-riZfKloxiuYnXofG9ht1yA1IMRiEwoFL9acP_qf6SMQSuZhGaadolCRT6Y06w0WtaH6C8yBy08xUnRV2Dtq1ztRm6ThI7HysHpgMMOeNeVtlLERcbu3VoLWLMvObq0j5kly0smtdgKfQSU9gxdWHp1vM8scsTb_4pRizQrFkkZPjCoSpaSqmVbLeWPpomJyVDlpIRI7jVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1281277307.mp4?token=GBOIZAN9szFUtogiEw8r8CJbcgGXsgymHLd75cDGUpFmNT6AJPYgXqituGKVeenl_lNzqddusD2107N7pCY83O5oK49P3RMq0vqp3yvfCdqa82K8Yq7GUUWEKuJoFl9M_r7v-9UqtuCGggeSHV75N7csZyQKes8RKER_NtwGyddKDr-6gYxjrKl-mMb47T8lPdoHvBrylbYOU9xOGVLb8q8-e8IItPR4ZNhAedNKAyFqiWJcbvwpsV6FuRfR66g_9zAiKj60e-Q3iHgZ2ULmLP42imyXNgXz6Sqovs-rXAxIbXxP68ZjsjFz-Ny2W1m8TJhr_3mKwy24244ufSb_mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1281277307.mp4?token=GBOIZAN9szFUtogiEw8r8CJbcgGXsgymHLd75cDGUpFmNT6AJPYgXqituGKVeenl_lNzqddusD2107N7pCY83O5oK49P3RMq0vqp3yvfCdqa82K8Yq7GUUWEKuJoFl9M_r7v-9UqtuCGggeSHV75N7csZyQKes8RKER_NtwGyddKDr-6gYxjrKl-mMb47T8lPdoHvBrylbYOU9xOGVLb8q8-e8IItPR4ZNhAedNKAyFqiWJcbvwpsV6FuRfR66g_9zAiKj60e-Q3iHgZ2ULmLP42imyXNgXz6Sqovs-rXAxIbXxP68ZjsjFz-Ny2W1m8TJhr_3mKwy24244ufSb_mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO)  با صدور هشداری فوری از «حمله پهپادی» علیه یک نفتکش در نزدیکی لنگرگاه بندر صحار در عمان خبر داد.
بر اساس به‌روزرسانی این نهاد نظارتی، این رویداد پس از تایید اصابت مستقیم یک پهپاد به این نفتکش، رسما به‌عنوان «حمله» طبقه‌بندی شده است.
بنابر این گزارش، مقام‌های محلی عمان در حال کمک به تخلیه خدمه کشتی هستند، اما تا زمان انتشار این اطلاعیه، ارزیابی دقیقی از میزان خسارات وارده، تلفات احتمالی و اثرات زیست‌محیطی آن در دست نیست.
@
VahidOOnLine
روابط عمومی نیروی دریایی سپاه پاسداران با انتشار اطلاعیه‌ای از انفجار و آتش‌سوزی یک نفتکش خبر داد و اعلام کرد: «یک نفتکش از نوع شاتل با ۷۵۰ هزار بشکه نفت خام، بی‌توجه به هشدارها و اخطارهای نیروی دریایی سپاه تلاش نمود از مسیر غیرمجاز عبور کند که به مین دریایی برخورد و دچار انفجار و آتش‌سوزی شدید شد.»
بنابر گزارش خبرگزاری فارس، این سومین نفتکشی است که طی روزهای اخیر در اثر برخورد با مین‌های دریایی به دلیل «نقض هشدارها و تردد در مسیرهای تعیین‌نشده» دچار آتش‌سوزی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78695" target="_blank">📅 00:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW60eqeROtZc-JcwW3TIllBwGq8WPHmg3b-gtC8WkNFSCe9b19mGJglxkSrE24aWKWXwsfoHVXLl3zP0X0NjbRrHlDL1Hs45OfNX-crCsXrKwnBl9LUZY67bPMvm2Z_TH1hHwjq5-oZWC6wQtGzoWwRGDOrLMX13g99TbNGxT-nqcAZjC1QEG68XDiSmFaTAhxp_quLKDsA8pFwUrgskXvnG8JH_PYXsBk-Zv-14heKKzVvdX-LfF2Cyz0csmeXv12Whpakbm7hX5z7izA9cc9OHa3B0giYOnp7DlAxhjrDV1BR1JN-vxz0gKx-kgf7gf8lRnG_q2991Pm0nZIj4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه ریاض روز یکشنبه ۱۹ مهر بار دیگر هدف قرار گرفت.
ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد که یک «پرتابه ناشناس» فرودگاه بین‌المللی ریاض را هدف قرار داده است.
ترکی المالکی، سخنگوی ائتلاف، گفت این پرتابه به پایانه ۴ فرودگاه بین‌المللی ملک خالد اصابت کرد و موجب آتش‌سوزی شد.
این در حالی است که حمله موشکی روز گذشته به فرودگاه بین‌المللی ریاض که حوثی‌های یمن پس از ساعت‌ها تنها به طور تلویحی مسئولیت آن را پذیرفتند دست‌کم ۱۲ کشته و بیش از ۳۰۰ مجروح برجا گذاشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78694" target="_blank">📅 19:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KrOggzitj7fl58uN3q_0aDqWyREpB7aS2cqr_J8URl0UVscWTGIOppXNpsPzXkPGvxEPd7mFA3W2vgHJhefI6MiJjhlJMvPQoCOhdlLAhPkHKHohCdjGQWeeLTYJNNkI-fiPSg1eDE5QYd4SkjYlLxRaN2BWFHU5OSI3CIPM7YVrrBXN8MfHFH8vtf-0vofymXcax-HyCpui9XJhatOXW2hWIXVFEN7s0CIoWxe--jjtWH8hZqeUUx1lLtmZqFRZhbSFm9QNujaLPY7IwOYJVYy2uZyd2wErTxUP4RZhPRVG-AXvif9Ir0IikXjkpOclsFABPu9p7jrnu8_KdLVmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3ec7037002.mp4?token=MjRymeXuJjUSIL3NyJAdvmKC43F9ZBt1Zsql2jwKs56JdpuW_Bl4wkP5rM6gRNqeUP1XPIVfVPxIcaHDtZG4a775-AkfM6y63CzeGw-yjWhurX698__ALHRGdoesVnKY7fjcTQBkxaoCCBO8uWz5-6ny76A_w1uBYcp14NaMdN2yCXiRLCVYDmCp6tvIWi6if2XXaFB_LMavZo6_U4PtUTj8IvMJwVA7lttjb0PRNefuEZEGzlTKGobBrHnNwLLjtOXe7ZYKuVLxFLQm3FEUtI_KI2cTNazu33HVi-EvRU9-498uVJ3lAF_5pM_mArKHlFuOFSkURa_T2NzFClYrxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3ec7037002.mp4?token=MjRymeXuJjUSIL3NyJAdvmKC43F9ZBt1Zsql2jwKs56JdpuW_Bl4wkP5rM6gRNqeUP1XPIVfVPxIcaHDtZG4a775-AkfM6y63CzeGw-yjWhurX698__ALHRGdoesVnKY7fjcTQBkxaoCCBO8uWz5-6ny76A_w1uBYcp14NaMdN2yCXiRLCVYDmCp6tvIWi6if2XXaFB_LMavZo6_U4PtUTj8IvMJwVA7lttjb0PRNefuEZEGzlTKGobBrHnNwLLjtOXe7ZYKuVLxFLQm3FEUtI_KI2cTNazu33HVi-EvRU9-498uVJ3lAF_5pM_mArKHlFuOFSkURa_T2NzFClYrxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا
گزارش
کرده است که یک نفتکش در حال عبور از تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفته است.
براساس این گزارش‌ها این نفتکش در حال خروج از تنگه هرمز بوده و «از ناحیه سمت چپ» مورد اصابت قرار گرفته است.
مرکز عملیات تجارت دریایی بریتانیا همچنین گفته این اصابت به کشتی آسیب رسانده، اما تمامی خدمه در سلامت کامل هستند و هیچ‌گونه پیامد زیست‌محیطی نیز گزارش نشده است.
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از منابع خبری گزارش داد که یک کشتی در مسیر جنوبی تنگه هرمز بر اثر اصابت یک پرتابه دچار آتش‌سوزی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78692" target="_blank">📅 18:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twiYY4Ktq54Q7nL621nN3GgGZJgMMppefvzWapv-bDmCMRYI-gTi7RpThsQXAJ4cAPLdeFC1D6fD39c6CEd6kbPVbx7TztIWIsxYyEv2Bk_uxW8OHvGkmnGyxg5_i7wADTZLfZvuuSpiWlrV2iuFE3wJodLs3x3WbjXyKOWh_qztimSJxdHnvDp1VxwD-FWz8jeXFsdvHx0om-jCPSeTY-N1ucLzidNoCWOoVRxph7n_Uld04HWI4WzlPmoKqs7cmdDtYjvAuBnkXGWe_tUJXzGp0SeocEu99mDy6qHRZcKK-0kdy3RaEJbBOWqR33yF19SDogkakbiToGje2HCTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرزاد شهبازی، از وکلای متهمان پرونده «میدان علیخانی اصفهان» و وکیل علیرضا سپاهی، با رد روایت رسانه‌های حکومتی اعلام کرده است اتهام قتل ماموران انتظامی به هیچ‌یک از متهمان این پرونده تفهیم نشده و دادگاه نیز به این اتهام رسیدگی نکرده است. تاکنون پنج نفر از متهمان این پرونده اعدام شده‌اند و هفت نفر دیگر در خطر اعدام قرار دارند.
اظهارات این وکیل در واکنش به انتشار مصاحبه‌ای در رسانه‌های حکومتی مطرح شده است که در آن زنی، معرفی‌شده به‌عنوان همسر یکی از مأموران کشته‌شده، متهمان را به قتل و سوزاندن ماموران متهم می‌کند. انتشار این مصاحبه پس از افزایش انتقادها از اجرای احکام اعدام، به‌ویژه اعدام علیرضا سپاهی، صورت گرفته است.
شهبازی همچنین حضور این زن در محل اجرای اعدام‌ها را زیر سوال برده و پرسیده است وقتی موضوع پرونده قصاص و حق شخصی نبوده، بر چه مبنایی به او اجازه حضور در محل اجرای حکم داده شده است.
شهبازی روز شنبه ۱۸ مهر ۱۴۰۵ در پیامی در اینستاگرام نوشت: «به هیچ عنوان اتهام قتل برای هیچ‌یک از متهمان پرونده میدان علیخانی و میدان شهدا تفهیم نشده است.»
او تأکید کرد موضوع «سوزاندن ماموران در راستای قتل عمد» نه در دادگاه رسیدگی شده و نه از اتهام‌های مطرح‌شده در رای بوده است.
شهبازی علت ورود نکردن دادگاه انقلاب به موضوع قتل را نداشتن صلاحیت رسیدگی به این اتهام عنوان کرده است.
پرونده میدان علیخانی پس از کشته‌شدن چهار مامور یگان ویژه در جریان اعتراضات ۱۸ دی ۱۴۰۴ در اصفهان تشکیل شد. رسانه‌های حکومتی پیش‌تر ویدیوهایی از اعترافات متهمان در بازجویی‌ها، بازسازی صحنه و جلسات محاکمه در شعبه اول دادگاه انقلاب اصفهان منتشر کرده‌اند؛ اعترافاتی که نهادهای حقوق‌بشری آن‌ها را اجباری و فاقد اعتبار می‌دانند.
علیرضا سپاهی بامداد دوشنبه ۱۳ مهر اعدام شد. مای ساتو، گزارشگر ویژه سازمان ملل در امور حقوق بشر ایران، در واکنش به اجرای حکم، از نگرانی‌های جدی درباره شکنجه متهمان و رعایت‌نشدن دادرسی عادلانه در این پرونده خبر داده بود. به گفته ساتو، حکم در حالی اجرا شد که وکیل سپاهی همچنان برای رسیدگی دوباره به پرونده تلاش می‌کرد.
سپاهی پیش‌تر نیز در آستانه اعدام در ملأعام قرار گرفته بود، اما پس از حمله قلبی به بیمارستان منتقل شد. در همان شب، شهروندان برای جلوگیری از اجرای احکام تا سپیده‌دم در میدان علیخانی ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78691" target="_blank">📅 16:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCT7N8wxdZMgCU3o22OJZJ0IyEaxJrJHpuoVYRyPX34WSG8KFFeytRCEXeWDKayjni2o0_DLfNjwBPDD7WfrHE3PXrJmoWHVBWN4vVgA4Hy5skYOO-xmN1Q_H4e9nmvXt8u6bkAgRe3gL3NZz_e_OdyQU2QsGf4mESOzvQr73YjDrZn7qR80AM7fQgKHiO3gAXbjnCFBGuhydolbpbX-JBGnzxMqn4-qa26AWEJvXO9sPx1MVIV0KBzhJBxwNUslniLDZAcL4t1mOiLlDtL29aX8iXVKZv13OSNuXHctezKzt2JMomPxA6SBUgxAyuD_d2a5rC_Cn3z3G5Ekox1-Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان مدیریت بحران ایران اعلام کرد در سیلاب و رعد و برق پنج استان کشور هفت نفر جان باختند و دو نفر مفقود شدند.
به اعلام این سازمان، دو مفقود در استان گلستان ناپدید شده‌اند.
در شهرستان سوادکوه شمالی استان مازندران دو پل کاملاً از بین رفت. آب‌گرفتگی در معابر و خانه‌های این شهرستان گزارش شد و شماری خودرو در آب ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78690" target="_blank">📅 16:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78689">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u2DkhZzGEi6LLw8TeRpGqGqOZJRqr4dvC7Z2qHx7fEqsus_bKFDvkNEHMt6bExG9e5GLOkfVTAz8XQFKvkBY3xpr2paycnj5ny7r0wSz6SfMqv1Ysz2MYE8k9LU0PiaaPaH3QlNfewrCdOsa2t5QCh_2oqKDM65PUap4LHJnmppDgbYh82Iv6pv7UfNMkSqLYWMmFXM8PTVOPsXJbUGQ_LOxmldBv2k1oxnOo0iM92lT2VYN-n88ELZGcHgC5Riat-oL13B85xBE1iTYk5roiqG5WUTVnK5Oe5vfXM8NocvkNpvF8e4rlwSfFBCVFT-v3pVMJ1-keOav-7b24y9prA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی از اعدام یک مرد به اتهام قتل یک مامور نیروی انتظامی در بندرعباس خبر داد.
این مامور نیروی انتظامی رضا احترامی و مأمور یگان امداد شهرستان بندرعباس معرفی شده است.
متهم نیز پیش‌تر با نام «دانیال» معرفی شده و ادعا شده بود که این قتل چهار سال پیش هنگام درگیری با قاچاقچیان سوخت، بر اثر زیر گرفته شدن با خودرویی که مرد اعدام‌شده رانندگی آن را بر عهده داشت، روی داد.
شنبه نیز دستگاه قضایی جمهوری اسلامی از اعدام جابر خسروی، زندانی محکوم به قصاص در پرونده قتل یک مأمور انتظامی خبر داد.
این پرونده به حادثه‌ای در بیمارستان ولایت دامغان در ۱۱ شهریور ۱۴۰۱ بازمی‌گردد؛ حادثه‌ای که بنا بر ادعای مقام‌های قضایی، در جریان آن سلاح مأمور انتظامی گرفته شد و او بر اثر اصابت دو گلوله جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78689" target="_blank">📅 16:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/igVb1hd6nDClyK75KoZJshB_7-9juAF51QkWDt__9yWRJ60jebZ-DjVfcyv7jO_HqetHrZQbcYnu95jFNVLgrnAox1-JlTEPMWpZ3BhnqHfQC-lo0ARGZWXhXvgqNbiDIOyb1Yuoi_yNG_WhSIfTDwKLlYqYsZ6IFksmOF1oymK1UcGe1p-7ANk4E0t0ZR9eExyG7UrZmJ5deeYJwa2-86iTXnaW-1BiTJiLIqoz48RPrWA3SZTCpr3h_kEiIUPPBtknB-xnuSXrRvOODXrjccvyZdaLjXtWoiYr0_kgxMtC_BBKZbxp8wJIvzL9wO8f2yHA1w4Vk0IMyclBzDRK0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی در بیانیه‌ای گفت حمله روز شنبه ۱۸ مهر به فرودگاه بین‌المللی ملک خالد در ریاض، ۱۲ کشته و ۳۰۹ زخمی بر جای گذاشته است.
بر اساس این بیانیه که بامداد یکشنبه ۱۹ مهر صادر شد، چهار نفر از کشته‌شدگان شهروند عربستان سعودی و هشت نفر دیگر اتباع خارجی، شامل دو بنگلادشی، یک آمریکایی، یک مصری، یک اردنی، یک سوری، یک فلسطینی و یک سودانی هستند.
این سازمان همچنین اعلام کرد که شرایط سلامتی شماری از زخمی‌ها وخیم است.
به گفته سازمان هواپیمایی کشوری عربستان سعودی، تمامی مجروحان در چندین بیمارستان تحت مراقبت‌های پزشکی لازم قرار دارند.
در این بیانیه همچنین آمده است که حمله به فرودگاه بین‌المللی ملک خالد خسارات مالی و مادی نیز به همراه داشته و ارزیابی میزان این خسارات همچنان ادامه دارد.
حمله روز شنبه سومین حمله این هفته شورشیان حوثی مورد حمایت جمهوری اسلامی در یمن به فرودگاه بین‌المللی ریاض بود. شورشیان حوثی مسئولیت حمله را بر عهده گرفتند. حوثی‌ها همسو با تلاش‌های جمهوری اسلامی برای ناامن کردن تنگه هرمز، سعی کرده‌اند به کشتی‌ها در تنگه باب‌المندب که دریای سرخ را به خلیج عدن و اقیانوس هند متصل می‌کند و یک تنگه حیاتی به‌شمار می‌رود حمله کنند.
طبق گزارش‌ها روز شنبه، مسیر تمامی پروازها از ریاض تغییر داده شد و فعالیت‌های فرودگاه به‌طور موقت متوقف شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78688" target="_blank">📅 03:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78687">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LwIMP1cFrPfZRVt7f4FquhEEB64mxVEb9Ds67eK6vqlQjP6ztplusCIeTCVlaUeIfU2vDKuKjZEoEWY7bRsCN8cMTV1PInV1E15W1YhzwZr9CElK8CfCMn2vp00I-dCQLQ-pYhEPYoSlj0pcMIsLzKdx9UdtwaGxd-XvE-OdHBAmIZsLo6WXMkvlKUCJL5wiM00sgR0feKMFS6a5CicNqvnCcdi91saNmK-endvQiNUdGoRZl8No9Nb4v9-LSxbCLK2T0-bmlU374NMkMRwoQfS9XEEw1OLFORYa7rRKFXfwuaGK25cUtCh0JMedOBtLc2Vr5BYINxmJ48o2IS8fMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
سازمان عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
ناخدای یک نفتکش که در حال خروج از تنگه هرمز بوده، گزارش داده است که یک پرتابه ناشناس به سمت چپ کشتی برخورد کرده و باعث آتش‌سوزی در آن شده است.
بر اساس گزارش‌ها، خدمه کشتی در سلامت هستند. در زمان انتشار این گزارش، میزان خسارات و پیامدهای زیست‌محیطی حادثه مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78687" target="_blank">📅 01:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78686">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU3aC_D8qH-yrX8IVjMyMiyOjR7WIPjheWvJDaroeCbWNseux5ZthbEXT_JRuy1N4_rCIJyXgnRHD3fyq48amIuVu7ZtpCTtvFg7x4uoE2ULmZtA4V2eQEPmEWqF69pTkIKe861b_G2gjKNslB0beMEceQmEmdzySCnV-opve5vlEkxRqYKpzGP734q3KQ3dOWlbJEs6-aw0r4sLNuChw6gKeCL4x8jflUAl_Q9KztLB-xuzMbcc44ijjPYknO4G-HJoxXEbiRUDqqkYuNg9XKZNmz7W8EN6WyUoGxzmcppDQv0bJII9LV8peHVpmrwLjQTkTPQpBuvrW8GcZM4Vng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، روز شنبه، طی سخنرانی در ایالت تنسی درباره ایران گفت: «اوضاع تا حدی آرام شده است. آن‌ها احتمالا پیش از انتخابات دست به اقدامات اضافه‌ای می‌زنند و فکر می‌کنند این اقدامات به ما آسیب می‌زند، اما ما می‌توانیم این ماجرا را خیلی سریع تمام کنیم.» او در ادامه افزود: «آن‌ها اصلا نمی‌دانند من چقدر با آن‌ها خوب رفتار کرده‌ام. واقعا خبر ندارند که چقدر با آن‌ها مهربان و با مدارا بوده‌ام.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78686" target="_blank">📅 01:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78685">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcdec5c24b.mp4?token=EEEkm4-JSMIar1aBpD4Z_lLpEzi771in7i8xz0H1cn9rw1kfUR627GkMs5KF6eU2OOOkTiQK387FCk409WKkog6x8rR4fcTzOG2MsUW2cFHNT-QZhumXd5espdkA67crMntcm4h4Plqnd8YCIo-0hMk-FsvqkgxgwG_yOKCgv-MULBHq91wNDrD-cPNzOfUteJ1ymYKPwzKWpMdBmfB8Fgm6t0ltpPW4YauuwcpoIqBqvdBlgX094r6ckZfmw4PH2jpj1Qy-f1SOR8zHoQUu9Bh9xwxc9znXxqyT5xIybrOn8UZKD0FpueEyH-ZcNW49Ll7ctTvHYHiwg0MTiGdstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcdec5c24b.mp4?token=EEEkm4-JSMIar1aBpD4Z_lLpEzi771in7i8xz0H1cn9rw1kfUR627GkMs5KF6eU2OOOkTiQK387FCk409WKkog6x8rR4fcTzOG2MsUW2cFHNT-QZhumXd5espdkA67crMntcm4h4Plqnd8YCIo-0hMk-FsvqkgxgwG_yOKCgv-MULBHq91wNDrD-cPNzOfUteJ1ymYKPwzKWpMdBmfB8Fgm6t0ltpPW4YauuwcpoIqBqvdBlgX094r6ckZfmw4PH2jpj1Qy-f1SOR8zHoQUu9Bh9xwxc9znXxqyT5xIybrOn8UZKD0FpueEyH-ZcNW49Ll7ctTvHYHiwg0MTiGdstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز شنبه ۱۸ مهر تأیید کرد که در پی حمله به فرودگاه بین‌المللی ملک خالد در ریاض و زخمی شدن شماری از افراد، فعالیت این فرودگاه متوقف شده است.
دونالد ترامپ، رئیس‌جمهور آمریکا، در واکنش گفته است که از این حمله مطلع شده و درباره آن تصمیم خواهد گرفت.
دونالد ترامپ در جمع خبرنگاران و در پاسخ به این سؤال که آیا آمریکا به جنگ عربستان سعودی با حوثی‌ها خواهد پیوست، گفت: «ممکن است. این موضوع را بررسی خواهیم کرد. ما تازه از حمله اخیر مطلع شده‌ایم. تصمیم‌گیری خواهیم کرد. خیلی سریع اقدام می‌کنیم.»
پیش‌تر برخی رسانه‌ها خبر داده بودند که حکومت ریاض از آمریکا خواسته حوثی‌ها را هدف حملات نظامی قرار دهد.
پایگاه خبری اکسیوس یک هفته پیش گزارش داد که شماری از بلندپایه‌ترین مقام‌های امنیت ملی دولت دونالد ترامپ روز جمعه در نشستی چندساعته و اعلام‌نشده در کمپ دیوید، درباره گام‌های بعدی آمریکا در جنگ ایران و همچنین درگیری عربستان سعودی با حوثی‌های یمن گفت‌وگو کرده‌اند.
با وجود تأیید رسمی وقوع حمله و زخمی شدن افراد، مقام‌های عربستان هنوز شمار دقیق مجروحان و میزان خسارت واردشده به فرودگاه را اعلام نکرده‌اند.
حوثی‌های مورد حمایت جمهوری اسلامی نیز تا زمان انتشار این گزارش مسئولیت حملهٔ روز شنبه را بر عهده نگرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78685" target="_blank">📅 22:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9492aa3856.mp4?token=ayax0ztXauqFMjlpBvhbarup4OHzof0es3gH0Q2KyjKYv9miKsQi6tZ1mSD6TjNYTmh3ioosa2lGHgM5_leCrjBkwMdfGmpDbhDTZgDsRhLoRmp-f2ebexZ73GSrauFHIFg0y5UfKkkm5x1PVQfiiHzqXwTx7j_o4OVsvtQ9Kt21i09ZVpLk2Ra8PsrfFB8K4-VASoloRfOpyluzGsOKmWAGx7-vvUlKg20JvaLfVrMB0TlVlqSc4g6CIQWtYepz6cAUmQYlEFT0O5vAn5o7J-0L3yEAyG7c9_FGN_VPm7pcAgbCSdEWJewYRdZIRIrkkMaXfVTWLO548zLtOMMx4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9492aa3856.mp4?token=ayax0ztXauqFMjlpBvhbarup4OHzof0es3gH0Q2KyjKYv9miKsQi6tZ1mSD6TjNYTmh3ioosa2lGHgM5_leCrjBkwMdfGmpDbhDTZgDsRhLoRmp-f2ebexZ73GSrauFHIFg0y5UfKkkm5x1PVQfiiHzqXwTx7j_o4OVsvtQ9Kt21i09ZVpLk2Ra8PsrfFB8K4-VASoloRfOpyluzGsOKmWAGx7-vvUlKg20JvaLfVrMB0TlVlqSc4g6CIQWtYepz6cAUmQYlEFT0O5vAn5o7J-0L3yEAyG7c9_FGN_VPm7pcAgbCSdEWJewYRdZIRIrkkMaXfVTWLO548zLtOMMx4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از هو شدن اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران منتشر شده است.
این اتفاق شامگاه جمعه ۱۷ مهر، هنگامی رخ داد که بقائی برای سخنرانی پشت میکروفون قرار گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78684" target="_blank">📅 20:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78683">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54a079f69b.mp4?token=TGhLPicc4exImQQOFMkFLOaMMQfZbYeffFtISGCzebIGJoy3YoJwZejXcdVQfpIa20Xc9v0QwBJVb1ZgLYDtaZLVWQa3yPOvHAVTND4XJHkfXu5yxfBIZDq3IoSVSYtuYnUX7GxdzWKvJV8LIQZ5pcB9epghPpq69RknL7KKyJnxE-VvDsgsC648h73yyndVVlew3mG4Sh61kdjPa6OXDZGPHlo2Vezt82yo0YDSd5SkDDNhIbS5jO4BZHLqWbuSTUSXawsxvgLpSI8b_dWUS9WxkYaSa6Lx-27zPpQLy8v3-QriovEshYG2Q3d2bLbB4QzrOV3CvoYTxB_4WNdxkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54a079f69b.mp4?token=TGhLPicc4exImQQOFMkFLOaMMQfZbYeffFtISGCzebIGJoy3YoJwZejXcdVQfpIa20Xc9v0QwBJVb1ZgLYDtaZLVWQa3yPOvHAVTND4XJHkfXu5yxfBIZDq3IoSVSYtuYnUX7GxdzWKvJV8LIQZ5pcB9epghPpq69RknL7KKyJnxE-VvDsgsC648h73yyndVVlew3mG4Sh61kdjPa6OXDZGPHlo2Vezt82yo0YDSd5SkDDNhIbS5jO4BZHLqWbuSTUSXawsxvgLpSI8b_dWUS9WxkYaSa6Lx-27zPpQLy8v3-QriovEshYG2Q3d2bLbB4QzrOV3CvoYTxB_4WNdxkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز شنبه ۱۸ مهر تأیید کرد که در پی حمله به فرودگاه بین‌المللی ملک خالد در ریاض و زخمی شدن شماری از افراد، فعالیت این فرودگاه متوقف شده است.
یک منبع دیپلماتیک به خبرگزاری فرانسه گفته است که حوثی‌های یمن حدود ساعت سه بعدازظهر به وقت محلی با موشک به این فرودگاه حمله کرده‌اند. بر اساس گزارش‌های اولیه، ده‌ها نفر در این حمله زخمی شده‌اند.
روزنامهٔ وال‌استریت جورنال نیز به نقل از مقام‌های سعودی گزارش داد که موشک‌های شلیک‌شده از سوی حوثی‌ها مستقیماً به ترمینال شمارهٔ سه فرودگاه اصابت کرده‌اند.
یک منبع بیمارستانی به خبرگزاری فرانسه گفته است که پنج نفر از مجروحان در بخش مراقبت‌های ویژه بستری شده‌اند. یکی از شاهدان عینی نیز گفته است هنگام حضور در گیت ۴۰۳ ترمینال پروازهای داخلی، شاهد اصابت موشک به محدودهٔ گیت ۴۰۱ و زخمی شدن مسافران بوده است.
این شاهد به خبرگزاری فرانسه گفت: «دیدم که گیت ۴۰۱ هدف قرار گرفت و افرادی جلوی چشمانم زخمی شدند. همه فرار می‌کردند.»
حملهٔ روز شنبه در حالی رخ داد که فرودگاه ریاض پیش‌تر نیز در روزهای چهارشنبه و پنج‌شنبه هدف حملات حوثی‌ها قرار گرفته بود. این حملات در مجموع چهار کشته و چندین زخمی بر جای گذاشت و به یک فروند هواپیمای مسافربری شرکت سعودی آسیب جدی وارد کرد.
سه شهروند سعودی، از جمله یک خلبان، در حملات روز پنج‌شنبه و یک شهروند سودانی در حملهٔ چهارشنبه کشته شدند. حوثی‌ها مسئولیت این حملات را پذیرفته‌اند.
تشدید حملات موشکی به عربستان در پی ازسرگیری درگیری‌های گسترده میان حوثی‌ها و نیروهای دولت مورد حمایت ریاض در یمن صورت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78683" target="_blank">📅 20:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZlfDlBSkNdRs3TjHT0Qt5daA6jTr1gK__LhsJFf8Zu2vl_ESavoUfS3we5ighg52tonOvO5bv9VZaMPu-H4VQXCO1XX9_XyzSI2bb4zzmwfAVBSrw-f0Ly1pPQlC0BZ69kAYDQsAJcB9qZv1OqbOs_iI3xOA8GTKAod1lDNliMNCLho-VkJh3jBr5da9Fqoarjkc6ZdZWkhAO4YNYF-gXSTm5Otsd7dC6_zpRi4Z5Qz9r-3nKRQVrJF1bNX3tg3t6H43IIrPOqqXWCtQOPw20SwoxCi_nB8gXmaGM4U7rBJH9LGmChJ4DaP42G6ehsTPE9-nCyofvcVD0-C99S63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ کرملین اعلام کرد ولادیمیر پوتین، رییس‌جمهور روسیه، با هماهنگی مسعود پزشکیان، دیدگاه تهران درباره راه‌حل احتمالی پایان جنگ با آمریکا را به دونالد ترامپ منتقل کرده است. هم‌زمان، مسکو از ادامه مذاکرات غیر مستقیم تهران و واشنگتن حمایت کرده و گفته پیشنهاد انتقال اورانیوم با غنای بالای ایران به روسیه همچنان روی میز است.
@
VahidHeadline
در همون انتقال به
توافق گازوئیل
رسیدند؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78682" target="_blank">📅 19:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jFqhFVqbBG0Nf4jvnvfbBj7tgdHwZQkaB0aUv1LEZnuxo6FoY0Rp-pykebMlRadZwUTI3nkWR0JeCZN5mibxb-jW8VsJpFT-7dc5PXp2b-js0z5Wr8roRMCrWvNYlT56myQYlX8zOpmZ0J_JVLq-RYoavilFoV7m1hdb5IEntq5NOFBK3DwC67Yogk948Be_wq_5z2y7LMP6y_ldZA5y89Ji7YULLbWI-0uFaK3bKuc_eQHlsPhclQ_i-0CePYlkn8L9nda4yqU2rnu3J2nTZdpOupAanNQohUS-CoVV43WjSK2u9hy0tqW9GbCbXTXCdLEXlbUqp9P9Nb4qWzI80w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه فعالان حقوق بشر در ایران در گزارشی به مناسبت روز جهانی مبارزه با مجازات اعدام اعلام کرد طی یک سال گذشته، دو هزار و سه نفر در ایران اعدام شدند که دست‌کم ۶۹ نفر از آنان با اتهام‌های سیاسی و امنیتی روبه‌رو بودند.
شمار اعدام‌ها در این دوره نسبت به دوره مشابه پیشین حدود ۲۹ درصد افزایش یافته و از هزار و ۵۵۳ نفر به دو هزار و سه نفر رسیده است؛ بالاترین رقم ثبت‌شده در ۱۰ دوره گزارش‌دهی.
بر اساس آمار این گزارش، شمار اعدام‌ها از ۵۰۵ نفر در دوره ۲۰۱۶–۲۰۱۷ به دو هزار و سه نفر در دوره ۲۰۲۵–۲۰۲۶ رسیده است.
در تفکیک اعدام‌ها بر اساس نوع اتهام، ۵۷٫۵۶ درصد مربوط به قتل و ۳۶٫۲۵ درصد مربوط به جرایم مواد مخدر بوده است. سایر اعدام‌ها با اتهام‌های سیاسی و امنیتی، تجاوز، محاربه غیرسیاسی، فساد فی‌الارض، جرایم اقتصادی یا اتهام‌های نامشخص ثبت شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78681" target="_blank">📅 19:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78680">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6008e28bbf.mp4?token=WnnwI_4ledGGZ6IFS8nV7qlCLkkt3g_GYOG9NW2ohSzHVEDvGM7PQkynHIihgoP-NuWKqGuu--vJF3jQ-BRyF9DV9ylSkHEnaKktPd7rTrZbkLGPLzrAgweY6X69s1pJCt-73n2QrMSOBdFyCQrU8cu7qKq78q6eQ9Autd8POcpBieAmoN0H10G7G_AVBF3uMPc6aSBsLlSunCxfzB4tlqJqq5KDfgLz9u86B7IyGZvXYdVUsboMz-Q1CYzNi7tpH1kp5sm_yTahM6qBubu1HC4YjFDlMDielzWkbNvFn__PvhczPFHMAqZfHbL4KjXdEuF_v9QVgVHm7lJub4Evcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6008e28bbf.mp4?token=WnnwI_4ledGGZ6IFS8nV7qlCLkkt3g_GYOG9NW2ohSzHVEDvGM7PQkynHIihgoP-NuWKqGuu--vJF3jQ-BRyF9DV9ylSkHEnaKktPd7rTrZbkLGPLzrAgweY6X69s1pJCt-73n2QrMSOBdFyCQrU8cu7qKq78q6eQ9Autd8POcpBieAmoN0H10G7G_AVBF3uMPc6aSBsLlSunCxfzB4tlqJqq5KDfgLz9u86B7IyGZvXYdVUsboMz-Q1CYzNi7tpH1kp5sm_yTahM6qBubu1HC4YjFDlMDielzWkbNvFn__PvhczPFHMAqZfHbL4KjXdEuF_v9QVgVHm7lJub4Evcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، طی سخنرانی در ایالت نیویورک اعلام کرد: «مسئله ایران به هر ترتیبی که شده، خیلی زود حل خواهد شد. یا آن‌ها همه‌چیز را به ما می‌دهند، یا دیگر اصلا وجود نخواهند داشت. خودشان هم این را به خوبی می‌دانند.»
او همچنین با اشاره به بحران اقتصادی عمیق در ایران و تسلط نظامی ایالات متحده بر منطقه تاکید کرد:
«ایران در ورطه بزرگی گرفتار شده، از تورم ۳۰۰ درصدی رنج می‌برد و هیچ پولی ندارد، تا جایی که ارتش و نیروهای پلیس آن حقوق دریافت نمی‌کنند. ایران هرگز به سلاح هسته‌ای دست نخواهد یافت و ممانعت از دستیابی آن‌ها به این سلاح دلیلی بود که ما را وادار به رفتن به آنجا کرد.»
ترامپ در ادامه افزود: «به لطف ارتش ایالات متحده اکنون کنترل کامل تنگه هرمز را در دست داریم و امروز حجم نفتی که از این تنگه عبور می‌کند حتی از دوران پیش از جنگ هم بیشتر است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78680" target="_blank">📅 07:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78679">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpyZw8_y-tQO25AI52IIQVMD1EPt1AegZc-t0gWbgO7s2BagO2Y_YEnozvi_GQaFqaCDSSCTKfKuETNJJoZUmPLFZaELqJv2-FQsdiNxKzOH96wzbtkKRPvnao4uZeqBeOErS6Nu00vqEkEptUJgb8mEkcfHCIRtJ-yr_1QvobmzwEhCE7cbZCGtr9qI8MCELEHzuimthdnyNBphDF9NXpB2YB6ITI3Db0xGeYcEFNrU2LsyR0_0ou7osqa_WyeiicoKMBQkHgini6atzOVWEEe7ddU1tAOq9ktnYnkX1F6NtvBG2eO82DxD_N2p6ZzR4tNer_sD3FX-IUe4BJTzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در شبکه اجتماعی تروث سوشال اعلام کرد کنترل کامل آمریکا بر تنگه هرمز، همراه با توافق تازه واشینگتن و مسکو برای عرضه میلیون‌ها تن گازوئیل روسیه به بازار جهانی، باعث کاهش سریع و چشمگیر قیمت این سوخت خواهد شد.
ترامپ گفت پس از گفت‌وگو با ولادیمیر پوتین، رییس‌جمهوری روسیه، توافق شده است که مسکو بلافاصله بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و جهان عرضه کند و ۵۰۰ هزار تن دیگر نیز در ماه نوامبر تحویل دهد.
به گفته او، روسیه پس از آن یک میلیون تن گازوئیل دیگر به بازار عرضه خواهد کرد و با توجه به وضعیت پالایشگاه‌های این کشور، سه میلیون تن دیگر نیز در مدت کوتاهی تحویل خواهد داد.
رییس‌جمهوری آمریکا گفت کنترل کامل تنگه هرمز از سوی واشینگتن و افزایش عرضه گازوئیل روسیه، قیمت این سوخت را برای مصرف‌کنندگان آمریکایی و دیگر کشورهای جهان به‌سرعت کاهش خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/78679" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=IavL0e9pLBhBD103l50MIHCHYNgCdMxlCq4BLMoxP4Uchl-khh6bLtvTiqOAvJK5oXS3EEwUb6Rp5uumDoLm1ksW_VAKaraL0r9UHoMBKTLWbkKhJ8TTCyGE6gESGPmYhlT9GrWSGeZwZthfK0LGge2OGO3_tHOODuHFUcAzrbB_WVKw8_5NHTblXShMKHvNVxN77M39R1CVUtGhdgalb7mO-wcWX2qQM-Yg1eaR-KeruIfC7iWonxOAgmPRlV8xm8Ck00JJGyd6FuQbyUVOgfPLN40eFAytcMRKfHfWSl_BvQGGua4qA-wL0tuxnMIk-cNJ0c4tB-FHu56Sdrh1Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=IavL0e9pLBhBD103l50MIHCHYNgCdMxlCq4BLMoxP4Uchl-khh6bLtvTiqOAvJK5oXS3EEwUb6Rp5uumDoLm1ksW_VAKaraL0r9UHoMBKTLWbkKhJ8TTCyGE6gESGPmYhlT9GrWSGeZwZthfK0LGge2OGO3_tHOODuHFUcAzrbB_WVKw8_5NHTblXShMKHvNVxN77M39R1CVUtGhdgalb7mO-wcWX2qQM-Yg1eaR-KeruIfC7iWonxOAgmPRlV8xm8Ck00JJGyd6FuQbyUVOgfPLN40eFAytcMRKfHfWSl_BvQGGua4qA-wL0tuxnMIk-cNJ0c4tB-FHu56Sdrh1Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره صداهایی که نمی‌دونم این بار هم آتش‌بازی بوده یا چی:
سلام وحید جان شرق تهران صدای پدافند و انفجار ممتد
صدای یک انفجار و بعد چندتا پدافند شرق تهران
وحید تهرانپارس صدای انفجار شدید بعد ضد هوایی الان ساعت ۸/۳۰
صدای شبیه پدافند یا تیراندازی در تهرانپارس شرق تهران
سلام وحید جان خوبی
پدافند تهرانپارس 5 مین  کار کرد ساعت  ۸:۳۰ دقیقه شب
وحید جان شرق تهران صدای تیر اندازی اومد الان
دود هم دیده میشه تو اسمون.
آپدیت:
دو ساعت بعد دوباره شرق تهران:
صدایی شبیه به تیراندازی در محله مجیدیه
ساعت ۱۰:۴۰ دقیقه ۱۷ مهر
چند دقیقه بعد: دوباره اومد این سری انگار رگبار بود
سلام ساعت ۲۲:۴۷ صدای تیراندازی چندین بار. مجیدیه شمالی‌
چند دقیقه بعد: الان هم دوباره اومد
صدای پدافند شرق تهران
سلام وحید جان
صدای پدافند همچنان پست سر هم
مجیدیه
صدای پدافند
مجیدیه
سمت مجیدیه تهران صدای تیر اندازی و پدافند میاد
صدای پدافند میاد
دولت کلاهدوز
سلام وحيدجان سمت اختياريه صداي پدافند مياد ساعت٢٢:٥٧
صدا پدافند سمت پاسداران
چند بار شلیک ساعت ۲۲:۵۷
سلام صدای تیر اندازی شمال شرق تهران ۱ دقیقه ممتد اومد الان قطع شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/78677" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78675">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pxhk5_-0RU7fcq-7-ZmLxp6CpsgGdtBgmLXRO4AQcZKIxdjm5iVQ4sosoJD4eQ_s5YBENxsQKGBx3-K4WuNNXFpgPjU543R1moIuXLNLpVGjC5bMqu9IHY0FnY2W3IcfGrmNBmYAKbYo6w366W1fBN5oq9E4O1MDyYITTp3DMWJ79ycfsTZEV3ld-NLIjgI8Sek5IOu9GztkA1OZ0eeuOU4kl_x9agsTbqHqJSZrM4-OXPDUhQ_Yiyv6LLv5EhwVSDmiS9sS5PwvqkQ9HWjv8Yiu5NbPC0t9flpj23vjxE06qD-exICwpGOJmSdRRtjG9DMS6Sw3dkEF57Ix3PYBFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f20c8d9bec.mp4?token=GNZ7d0UBCU3p2oO0N7z2N8spZ3FtwjPHNNILrAQJ9V6rgERXpQ0yNWi7N9NkY2PV9wHPh8UbibDou1nTCMGDFOd-qMGLfyQE1n6gBQ8BgOgyASVV3OST6Q44UNNRXcGWph9Y_8GlcAm2B1ZSUvuWIPr7EmwdmeTWXsSLuCoC7xmjN5O9D3l-U96ZwuxQQPsX_cNP2Ax54ogE0SWYmN9wlR9WbkpC2MXYKSrQg11NxBfAFCN5XbqZQAEfJpZCs8M_uqSz1vVGQb5TAWvI853WJSZTBcs9fNT8jD5IbQGnBLdDRyXn8VTyHskWqj41QhvS7dCIlSAfbn2vqcgamAB0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f20c8d9bec.mp4?token=GNZ7d0UBCU3p2oO0N7z2N8spZ3FtwjPHNNILrAQJ9V6rgERXpQ0yNWi7N9NkY2PV9wHPh8UbibDou1nTCMGDFOd-qMGLfyQE1n6gBQ8BgOgyASVV3OST6Q44UNNRXcGWph9Y_8GlcAm2B1ZSUvuWIPr7EmwdmeTWXsSLuCoC7xmjN5O9D3l-U96ZwuxQQPsX_cNP2Ax54ogE0SWYmN9wlR9WbkpC2MXYKSrQg11NxBfAFCN5XbqZQAEfJpZCs8M_uqSz1vVGQb5TAWvI853WJSZTBcs9fNT8jD5IbQGnBLdDRyXn8VTyHskWqj41QhvS7dCIlSAfbn2vqcgamAB0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت اگر حکومت ایران به سلاح هسته‌ای دست می‌یافت، ممکن بود پس از حمله به اسرائیل و دیگر نقاط خاورمیانه، کشورهای اروپایی و شهرهایی مانند لس‌آنجلس و سن‌دیگو در آمریکا را نیز هدف قرار دهد.
ترامپ جمعه ۱۷ مهر در مراسم روز کلمبوس در کاخ سفید گفت جمهوری اسلامی پیش از حمله بمب‌افکن‌های بی‌۲ آمریکا، تنها دو تا سه هفته تا دستیابی به سلاح هسته‌ای فاصله داشت.
او گفت در صورت دستیابی جمهوری اسلامی به این سلاح، حکومت ایران به‌سرعت از آن استفاده می‌کرد و ابتدا اسرائیل و سپس دیگر نقاط خاورمیانه را هدف قرار می‌داد.
رییس‌جمهوری آمریکا افزود کشورهای اروپایی احتمالا پیش از آمریکا در معرض چنین حمله‌ای قرار می‌گرفتند و شهرهای لس‌آنجلس و سن‌دیگو نیز می‌توانستند از اهداف احتمالی باشند.
ترامپ گفت: «دیگر لازم نیست نگران این موضوع باشیم. آن‌ها به سلاح هسته‌ای دست نخواهند یافت.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۱۷ مهرماه در مراسم روز کریستف کلمب در کاخ سفید، با اشاره به درگیری‌های نظامی با جمهوری اسلامی گفت که این وضعیت به‌زودی پایان می‌یابد و قیمت سوخت نیز به‌شدت کاهش خواهد یافت.
ترامپ در سخنانش با اشاره به عملیات نظامی آمریکا علیه ایران گفت: «ما مانع دستیابی ایران به سلاح هسته‌ای شدیم.» او افزود که پایان درگیری‌ها از راه‌های مختلف امکان‌پذیر است و تاکید کرد: «به هر شکلی، این وضعیت خیلی زود پایان خواهد یافت.»
رئیس‌جمهوری آمریکا همچنین درباره توان نظامی جمهوری اسلامی گفت: «آن‌ها نه نیروی نظامی دارند، نه نیروی دریایی، نه نیروی هوایی و نه تجهیزات پدافند هوایی.» او در ادامه با اشاره به محاصره دریایی اعلام کرد که آمریکا مسیر عبور کشتی‌ها را مسدود کرده است.
این اظهارات در شرایطی مطرح می‌شود که واشینگتن هم‌زمان با ادامه فشارهای اقتصادی علیه جمهوری اسلامی، محدودیت‌های دریایی و تحریم‌های مرتبط با صادرات نفت ایران را دنبال می‌کند. تنگه هرمز نیز به یکی از محورهای اصلی تنش‌های نظامی و اقتصادی میان دو کشور تبدیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78675" target="_blank">📅 20:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qs1n7s0e3Y3YtzSOhZf0cqIIJIHt_ORhiuWFyMJyEmkfRb_yWN8fIMOWVgzCO7tgN6bufPo4hZ0LePXAdL7_a2X6pXDq4xnVJkkEmxIYhxJ_HEN8_XQA9k53syJ4wrkwUhQpUhkzZpNJaQG0Px2L6iLatvqr8TL05jkCq7PsHDh4T0-6p-4qPhr_8xDXseunza3mOYp5-7dtIX8QB8VIagK4lDV9rtMXrUkoO_Z856NCoPQ4DFfLka5P2DCpcxQHwIXapTNqXt7t6-9pbCJF1UwsV1Epl6GQwfxxNUu6MeP1nCDY0q8LTp8693fjM5Ffq2JkVQCdGYLq4QhvmgQlQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صداوسیما با انتشار گزارشی اولیه، از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان سیستان‌ و بلوچستان خبر داد و نوشت در این حادثه نصرت افتخاری، معاون اجتماعی انتظامی استان سیستان و بلوچستان، در منطقه چشمه زیارت زاهدان کشته شد.
این منبع نوشت عامل اصلی بمب‌گذاری هنگام فرار کشته شد.
خبرگزاری فارس، رسانه وابسته به سپاه پاسداران نیز گزارش داد این حادثه در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان رخ داده و چند نیروی پلیس در جریان آن دچار جراحت شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78674" target="_blank">📅 18:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HT8UtjJry293UKpV1sUx7m9jya7S6weoLdgpzJfsmPF7mqHQOkrxd2CDJlWqMkZUMHKL2ywqnZ4AvHx6AZUAhhIi8uCIuLtH5C6BC5epGgFPo8k1uOr6LkJ62Oh7o12QWEkeyMy0eVbQ1WBzrhmt_7KTJwys-twFT64_AZVu8rgJusXpjt29owvUShNGnVaDz_9PcjoQNVfHmrZIfSqNAWspI-VJuJET15OWfxgRFef3F2xytJ7_FMWfmOhEXj_Kz4eiq1rJV5rxmKGNiIlia17bZc3SSmg9GmpRTRRj3IhVPTTH7HVdnFzKWnHW1BIUXHFdIZ9lsRm4RS23yO4rxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران،  اعلام کرد یک کشتی حامل گاز مایع به‌نام «ان‌وی سان‌شاین»، متعلق به شرکت نات‌ویت را هنگام عبور از جنوب تنگه هرمز هدف قرار داده است.
سپاه پاسداران اعلام کرد این کشتی در حال عبور از مسیری «غیرقانونی» بود و پس از اصابت، موتورخانه و سامانه رانش آن دچار آتش‌سوزی گسترده شد.
نیروی دریایی سپاه همچنین اعلام کرد کنترل تنگه هرمز را در اختیار دارد و اجازه حضور نیروهای نظامی آمریکا در این منطقه را نخواهد داد.
سپاه پاسداران در این بیانیه اعلام کرد شرکت‌های کشتیرانی که با آمریکا همکاری کنند، با تحریم و اقدامات تنبیهی علیه شناورهای خود روبه‌رو خواهند شد.
بر اساس این بیانیه، سپاه از این پس برخورد با شناورهایی را که از مسیرهای غیرمجاز عبور کنند، به تنگه هرمز محدود نخواهد کرد و این کشتی‌ها را در سراسر منطقه هدف اقدامات تنبیهی قرار خواهد داد.
@
VahidOOnLine
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)، روز جمعه ۱۷ مهر، با انتشار هشدار جدیدی اعلام کرد که حادثه‌ای در ۱۳ مایل دریایی غرب راس‌الخیمه در امارات متحده عربی رخ داده است.
بر اساس گزارش‌های دریافتی از منابع مختلف، این شناور مورد اصابت یک پرتابه ناشناس قرار گرفته که منجر به بروز حریق شده است؛ آتش‌سوزی مذکور تاکنون مهار و خاموش شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78673" target="_blank">📅 16:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvoCR4cBugN4uGCiEhu6tODFl83brU7cPHSZjXMuXbsxQuJFLWVoFjT7CvGhtJ9BdKY1o7Lc-I839D6s2nWKY7Wh4qpXynfFKdullGraas_wOsp6VWc1RbzG1MCz2QZmuuUhh_0wqBEZ0nD93w4xDzJkFKImb6dtvZIOqXtnprsV1gWTLdKiv9V8uDE2yWA1jpGt5940H-hUlO7EM5vxYImGg1O9l7O_BihBpMq_mjv1MdD4P8zHoymWFI30Dv1v7EPqfXBk93UKKtTxQ1BSMXMtRoWyWZuhJJhztjTQBDF7S7jtIcjxUYD5eQ7Jb7ELqVXQcgXxtLcJo3Tp-0gbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه‌های نیویورک‌تایمز و وال‌استریت ژورنال در گزارش‌هایی از بررسی گزینه‌های تازهٔ حمله به ایران در دولت آمریکا و تقویت حضور نظامی این کشور در خاورمیانه خبر داده‌اند.
این گزارش‌ها در حالی منتشر شده‌اند که دونالد ترامپ، رئیس‌جمهور آمریکا، روز پنج‌شنبه ۱۶ مهر اعلام کرد ایالات متحده پیش از انتخابات میان‌دوره‌ای سوم نوامبر به ایران حمله نخواهد کرد.
نیویورک‌تایمز به نقل از مقام‌های آمریکایی گزارش داده است که ارتش ایالات متحده در حال تدارک گزینه‌هایی برای ازسرگیری عملیات رزمی گسترده علیه ایران است و پنتاگون به دستور آقای ترامپ طرح‌هایی را برای حمله به زرادخانه‌های پهپادی و موشکی، تأسیسات انرژی و دیگر مراکز نظامی ایران تدوین کرده است.
به گفتهٔ مقام‌هایی که با این روزنامه گفت‌وگو کرده‌اند، تیم امنیت ملی رئیس‌جمهور آمریکا و پنتاگون در ماه‌های اخیر پنج پیشنهاد برای انجام عملیات‌های بزرگ علیه ایران یا حوثی‌های یمن به او ارائه کرده‌اند، اما آقای ترامپ هر بار این طرح‌ها را رد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78672" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyQPwN0QxxT78CloJWRWnCqjqi9eb7WNQNMvGdHHbjviIwVhsWAHhI2tNkv6pjnDoMzakZ_F3_rgrjr2TBqv80PQdyzNgvdia4ab4F_4xg4wpG9Tp153V-pbADnK3KIAoo5mF3458DNsr3KezDX4whskla4cX4fQitgB-Jk3is82rNTDxfmjm9hV5VyX2cCWoD0aC9SE20F_l8kfVuKKVUEZeoW09OjR_2JnEUbgNZvAB_7DaOzVpcYUWr7CVcNiMuwx6ICXCDq7wMhI-DoH3P0cH1GzJSxbQXLyf-rACUPDp-WXQnmqzrywKcuCKNcArfqz2RGqmwc1J20IDB9nZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت اوپن‌ای‌آی اعلام کرد حساب‌های کاربری مرتبط با یک عملیات نفوذ رسانه‌ای با منشأ ایران را مسدود کرده است؛ عملیاتی که در آن، گردانندگان با استفاده از چت‌جی‌پی‌تی و هویت‌های جعلی روزنامه‌نگاری، نزدیک به ۱۰۰ مقاله درباره جنگ ایران و آمریکا را در حدود ۱۲ رسانه اینترنتی در کشورهای مختلف منتشر یا بازنشر کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78671" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JO455a_XNSm7lDHS4zpK5H_zRl2lKW4BFclI5V-PnEp3JzdHYHrd9KoOTeTMUOysKhxd4nYaCoo9rD4dEDETeo3Y-c5a132w3kFEPlfj4L3o-QalFi1md_yF4vqWWXlUa9PnnXGEE4Rt4SRbX9SutF0VEtOD0AJ1k4Ecb3u0ofay9qGItArgKtiY8cEG2DZK57oPNhmioR4yJqK7Qe5upvbwJ93GhykpO3xC91dAhQNB__wHZWj6c3A13XF5N1uXBdtIFeeCvEkRJF02c3eSbym2K1NND1psvT7_U9Se5xBuo0tYF8NHDvdUEFoB2vEkEAe1zaaaxPAt71ghw1SneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد واشینگتن احتمالا تا پایان هفته حدود یک میلیارد دلار دارایی رمزارزی مرتبط با جمهوری اسلامی را مصادره خواهد کرد.
بسنت گفت دولت دونالد ترامپ کارزار «فشار حداکثری» علیه جمهوری اسلامی را به کارزار «انزوای کامل» تبدیل کرده است.
به گفته او، این سیاست علاوه بر محدودیت‌های مالی، مسیرهای دریایی، هوایی و زمینی ارتباط ایران با خارج از کشور را نیز در بر می‌گیرد.
وزیر خزانه‌داری آمریکا گفت امارات متحده عربی و عمان در اجرای این سیاست با واشینگتن همکاری می‌کنند و دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن مسیرهای زمینی ورود و خروج از ایران است.
@
VahidOOnLine
اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتقاد از سفرهای خارجی مقام‌های جمهوری اسلامی گفت اعضای سپاه پاسداران دیگر نمی‌توانند برای دیدن «جراح پلاستیک خود در لندن، معشوقه‌هایشان در پاریس و پول‌هایشان در ژنو» به خارج از ایران سفر کنند.
بسنت در ادامه گفت: «اگر جمهوری اسلامی را دوست دارند، حالا همان‌جا گیر افتاده‌اند و می‌توانند از آن لذت ببرند.»
وزیر خزانه‌داری آمریکا گفت سیاست دولت دونالد ترامپ برای منزوی کردن جمهوری اسلامی، فراتر از تحریم‌های مالی است و محدود کردن سفر مقام‌های حکومتی به خارج از کشور نیز بخشی از این برنامه به شمار می‌رود.
او همچنین با استناد به گزارش اخیر نیویورک‌تایمز گفت اقدامات دولت آمریکا باعث ایجاد نگرانی و آشفتگی در میان اعضای سپاه پاسداران شده است.
بسنت افزود اقداماتی که واشینگتن علیه جمهوری اسلامی انجام داده، پیش از این سابقه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78670" target="_blank">📅 16:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a954e7da9.mp4?token=eLoOYNmfx_h9xbvDDiIzLsMelMrNpAunhRt55TRWHDf0-kkPVmHD3BYFjyO2eZu8eP5GjK85A7JZperC6IRO1YfGoNLau2BiS0S4yzZmJgnj_NmQUrIjSNjI2WgvOqRCQrTqkDv89t3e0XiXrSvY5oPk2YrLDSVaMbJSUCKhW8kvH_9G9NTBE1t7GC3h1YtkeO499dPlVMn2wqon477n6jY8Lvt9OdE5nqLeJzFiRyV3fH98IYqUS_qeXKWvQ7me3O8j9juXOCH5FKDi8zYI395AWwlJOncbfPloADeBlalpY1CTD-SJB4oijUDtU4Hec88ZF7cjeVYQzXNkcMBqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a954e7da9.mp4?token=eLoOYNmfx_h9xbvDDiIzLsMelMrNpAunhRt55TRWHDf0-kkPVmHD3BYFjyO2eZu8eP5GjK85A7JZperC6IRO1YfGoNLau2BiS0S4yzZmJgnj_NmQUrIjSNjI2WgvOqRCQrTqkDv89t3e0XiXrSvY5oPk2YrLDSVaMbJSUCKhW8kvH_9G9NTBE1t7GC3h1YtkeO499dPlVMn2wqon477n6jY8Lvt9OdE5nqLeJzFiRyV3fH98IYqUS_qeXKWvQ7me3O8j9juXOCH5FKDi8zYI395AWwlJOncbfPloADeBlalpY1CTD-SJB4oijUDtU4Hec88ZF7cjeVYQzXNkcMBqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان روز پنج‌شنبه ۸ اکتبر (۱۶ مهر)، با ولادیمیر پوتین، رئیس‌جمهور روسیه، دیدار و گفت‌وگو کرد.
این دیدار در ترکمنستان و در حاشیه دو نشست «کشورهای ساحلی دریای خزر» و «سران کشورهای مستقل مشترک‌المنافع» صورت گرفت.
پوتین در این دیدار خطاب به پزشکیان گفت «ما می‌دانیم که ایران تلاش‌های واقعی برای پایان دادن به این درگیری انجام می‌دهد؛ درگیری‌ای که ایران در آغاز آن هیچ تقصیری ندارد.»
پزشکیان هم در این دیدار به پوتین گفت «هر بار که [با آمریکا] گفت‌وگو می‌کنیم، دوباره حمله می‌کنند، ولی ما از میز مذاکره و گفت‌وگو کنار نخواهیم کشید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78669" target="_blank">📅 16:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D2RKAZqRg1yduScDA7XlX0L4a0Un8NiR8Geveailgdl4JhqgEVdSAKnzJd3REh_c1WMCPq99cOZ-GKMGR6sDPQ9fM7ndQjiiLwYLdFynTtody3wtcpWwNZtqZ3dsvpymscHV-KWt1InE3KvSoz0-hh73eVi7h7iNhzQfUFOADwh3nyBdc42-QaitPlmJAeE2bKS7pSgg6HESvDoNz_BMEYoIJdYKHg5yMNudVxZuNU_dxUZUUBH9csujYNBUrlM6iUwsq31AKq3xrQ1cqXoysgax74IGHPX2F3Du-ZsTdk0y0MWo76GFm0Sjm025QUnasn4NUV6DO2E4tajHHaSoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JJViDrZatKN1WB0QQX5hMjP-E0jGq4ag77WZvXAWvoPgSqM54gH348gWcj7iF_UtySk4i7qlBy26ZVdl773wwCTwmNIjOM1uGbh_G5-hlO_qoNWQ6UIV4yye8LR5czmr7Vr3-93i5_LrrB2e_sVyr9s0jnxm7QbcPHEw6L-h4ZGUO8TCRGOST6hZ7CgozG7feWYZyzsjw7H_TblaZVgUc23Lg9pW7yD9xOm4c2IC1Ma-zzYP835H5A8Sx_kj3vHeQ5TMvw54BmLgaKMwRyufDLAz4l8pFty7JmK7AVnwson3iubk0cG9sR-D3IkmBEcgJzUJDtG9ItO-LP4JR4bEiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی در بیانیه‌ای جمعه ۱۷ مهر اعلام کرد که در پی دو حمله به فرودگاه بین‌المللی ملک خالد ریاض در روز پنجشنبه، سه شهروند این کشور کشته و شماری از شهروندان سعودی و اتباع خارجی زخمی شدند.
بر اساس این گزارش، در حمله نخست، تاسیسات فرودگاه و در حمله دوم، یکی از هواپیماهای شرکت هواپیمایی سعودی هدف قرار گرفت.
این سازمان اعلام کرد پس از این دو حمله، فعالیت فرودگاه از سر گرفته شد و تردد پروازها به حالت عادی بازگشت.
شرکت هواپیمایی سعودی نیز اعلام کرد که یکی از کارکنان این شرکت در میان کشته‌شدگان بوده و یکی از هواپیماهای آن هنگام توقف روی زمین در فرودگاه آسیب دیده است.
سازمان هواپیمایی کشوری عربستان سعودی همچنین اعلام کرد که فعالیت‌های عملیاتی فرودگاه بین‌المللی ملک خالد از سر گرفته شده و تردد هوایی در این فرودگاه به حالت عادی بازگشته است.
@
VahidOOnLine
شرکت هواپیمایی سعودی (السعودیه) اعلام کرد کاپیتان حمود علی الکثامی، خلبان این شرکت، روز پنجشنبه ۱۶ مهر ماه در حادثه فرودگاه بین‌المللی ملک خالد در ریاض جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78667" target="_blank">📅 16:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgioLSFTGTyzTebuaMauRT0YoUHfy6E9Cgsv7c1lQBYsPWZ3sr2_PiMRpq29Bpjbccq5vrcJ3DzaLkr1PHpis8E6FW1IH_7CUmVuf7OGaez0WwQRMoYBYbXz1n__Dxj1i03rEXbPRfBBlWQtOhP3U1CG9hcGmIllzu_WgjeymfFxYsXkR0GOEIjZEsuojNcv-ksr-x0CWDf2UktMTtG5e71DIGi0HyuQKEjItXQBrvgAnAw4DKEvuTKTrOXKHyuDC0YSb-IHYUUzaiCdXzQt6sNohQEAz57w646jZ25IuB9tbE_qWDV6yNzRoSVAXi4aCvVe9qBMJFqx2L334Vtaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی از کشته شدن رئیس پلیس پیشگیری شهرستان فاریاب در استان کرمان بر اثر تیراندازی افراد مسلح خبر دادند. این حادثه در حالی رخ داده که طی دو روز گذشته چندین حمله مسلحانه دیگر علیه نیروهای نظامی و انتظامی جمهوری اسلامی در مناطق جنوب شرقی ایران گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78666" target="_blank">📅 16:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z9sIsIezRErzIRF6GmkYW7SY5YBKZlXrPv2ZsHS7Qa00NUFGSCz4Mg6_KzBmrbsVybtwL2dLj9-MA1mwcehjuq25NACVBkaKDjKnnoW9HpDQLn4mf28R1_hZSDXoJzc-MLqVQp5mLr8mb7Vh9GEUVhyz-XrBan6VohmMvgS81HA4EnyhLsTQi1fpJJH1P_TJpYD0es6S4vcMpttJPUEycFO1lqzJkd_uwjwQXXCmanrL_myYSqJc7PcyZzG3yesl1MIyM_YfIOfhCaT-ajJoVkqfDU2BJiLNlrsHGFIPbetHx7-aDKrC8BdrfDbMpeC7wrLEOwG0sfigMkW3PK-o9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترانه و رومینا رحیمی، دو خواهر بازداشت‌شده در جریان اعتراضات دی‌ماه ۱۴۰۴ و از متهمان پرونده موسوم به «میدان شهدای اصفهان»، در زندان دولت‌آباد این شهر به سر می‌برند.
ترانه رحیمی در مرحله بدوی به اعدام و ۱۱ سال حبس و رومینا رحیمی به ۳۶ سال حبس محکوم شده‌اند. وکلای آنان به این احکام در دیوان عالی کشور اعتراض کرده‌اند.
#ترانه_رحیمی
#رومینا_رحیمی
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78665" target="_blank">📅 16:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnpi00bKRSioWFuNFz_tTdzeZHETWzmq8V7zyUW2iexx4Kvde4bh1csLx2D4qfie8Qc8VD-0r3ldHZ8AvCQsNAjkE73EjhscatJ4_dR0Hxu6H1lTgMKh2LcjqKI-m-2HFO8JkOpTY9iMd-wxV0F82X3y0nVjZFlJtx8QABP6ni3tsVD23PcrWpAU1t_IZzIQSys6snujzjt_cn4uk1A1aCglhHMK4O1veo33ntN6zU9GK1kDRiqphymPRLW1Pg8Mo3r6fxaprKmDAZDBgLCL5HwyhlmZFz7vQ3ADCbPvlbDmOoHNmesA1lv3yofsxdWhmhK6ZrszuOFBz8ZxAHYoaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رسانه‌های جعلی و ساختگی دارند تلاش می‌کنند این‌طور وانمود کنند که من از دشمن دعوت می‌کنم سن‌دیگو و لس‌آنجلس را بمباران کند، در حالی که آنچه واقعاً درباره‌اش صحبت می‌کردم این بود که افزایش موقت قیمت بنزین، بهای ناچیزی است که باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای پرداخت کرد. و اگر می‌خواهید بدانید بهای سنگین واقعی چیست، می‌توانید تصور کنید اگر آن‌ها سن‌دیگو و/یا لس‌آنجلس را بمباران کنند، چه اتفاقی خواهد افتاد؟
تنها کاری که من کردم، مقایسه پرداخت مبلغی کمی بیشتر برای بنزین، آن هم برای مدتی کوتاه، با بمباران شهرهای بزرگ ما بود.
همه این را می‌دانستند، رسانه‌های جعلی هم می‌دانستند، اما همچنان بیرون می‌آیند و می‌گویند که من از دشمن می‌خواهم دو شهری را که عاشقشان هستم بمباران کند.
«حرف‌های من کاملاً روشن است، اما این‌ها آدم‌های پستی هستند و فکر می‌کنند می‌توانند مدام اخبار جعلی منتشر کنند و قسر در بروند!»
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78664" target="_blank">📅 23:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aXFpCFQxnu-u0x58iZDW6dHFmqCEcDio2zsJNsLhLTHY4HHWSMUXIJdq5scoeA2qLsKjaYnENsv8tbzTJ-Hs-qp6ZNnBkXsf7TNxAWtRhcj-Aw-FXeG5RsgP2r6LzoVzQFXPB6IHQkJU2CLXAm-vdHXT4QPQG3SeANUWJ7LQkSpKRlS9auu2ztaqCIAsBVcqURZ02ut_mCrgQ2SPPmZv_-E41mY1HKegD9GbpXa2Lhj0KqMu8_nKdEUe9mCvLYilsjt-agYqUC_1XSjqlzUN8bJZ470oZMAMQBMqMrE2rLKLRqL80_PpzjoG-VTJq6L-ZEQpCCsRIGGVKz66leOpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات در جریان است، پیش از انتخابات حمله نمی‌کنیم
ترجمه ماشین:
ما در حال انجام گفت‌وگوهای سازنده‌ای با جمهوری اسلامی ایران هستیم. می‌خواهم برای همه روشن کنم که اگرچه ایران هم از نظر اقتصادی و هم از نظر نظامی در وضعیت بسیار بدی قرار دارد و اگرچه محاصره همچنان با تمام قدرت برقرار خواهد ماند، در حالی که نفت با حجم بی‌سابقه‌ای از تنگه هرمز عبور می‌کند (تنها دیشب ۲۲ میلیون بشکه، بدون اینکه حتی یک بشکه از ایران آمده باشد یا به مقصد ایران برود!)، ما تا پیش از انتخابات میان‌دوره‌ای که قرار است روز ۳ نوامبر در ایالات متحده برگزار شود، در هیچ زمانی به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!
پرزیدنت دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78663" target="_blank">📅 20:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78662">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b534ce975d.mp4?token=mUHXlRsuqv0vMvm2EBhoUJwZRIBxJ775xlScv35mmdpoHJE87P0rOsHip48Kvnq2I9_fDAjFxJeicJj9jNwxufDQUOph4lz9_B6XvRTIqpyVXiDHyBZA_NwFhz-argiBxpGd5STif0ltJlDYhOsGET1dJhgBq8D0cSohOHPdFYmb3654xDjRwUSpHAbJx9b693bL6FhJKJJXbMzVoQ-CQjzj5vwMOIqtndv_uxwcorYeLvkKKzMjIKGbTE-YtT--rt_swnv0EBsNNBBB2Y0KgbSWUaZwyHa3fm9Jd88khXF4q96kDHEul2CadmZrpdAbFaWSHeKIUYYTFAUw2hcGCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b534ce975d.mp4?token=mUHXlRsuqv0vMvm2EBhoUJwZRIBxJ775xlScv35mmdpoHJE87P0rOsHip48Kvnq2I9_fDAjFxJeicJj9jNwxufDQUOph4lz9_B6XvRTIqpyVXiDHyBZA_NwFhz-argiBxpGd5STif0ltJlDYhOsGET1dJhgBq8D0cSohOHPdFYmb3654xDjRwUSpHAbJx9b693bL6FhJKJJXbMzVoQ-CQjzj5vwMOIqtndv_uxwcorYeLvkKKzMjIKGbTE-YtT--rt_swnv0EBsNNBBB2Y0KgbSWUaZwyHa3fm9Jd88khXF4q96kDHEul2CadmZrpdAbFaWSHeKIUYYTFAUw2hcGCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ گفت: «من باید در مورد ایران اقدام می‌کردم، چون آنها به سلاح هسته‌ای دست پیدا می‌کردند و آن وقت می‌فهمیدید مشکل یعنی چه.»
رئیس‌جمهوری آمریکا در ادامه با اشاره به احتمال حمله موشکی ایران به شهرهای آمریکا گفت: «ببینیم اگر آنها روزی به لس‌آنجلس یا سن‌دیگو حمله می‌کردند، چه اتفاقی می‌افتاد. این دو شهر به دلیل موقعیت جغرافیایی‌شان بیشتر مطرح هستند و منظور من حمله موشکی است.»
ترامپ افزود: «اگر چنین اتفاقی می‌افتاد، وحشتناک بود. بگذارید لس‌آنجلس یا شهری مانند سن‌دیگو را هدف قرار دهند. بگذارید یکی از شهرهای بزرگ ما را هدف حمله قرار دهند. آن وقت است که می‌فهمید مشکل واقعی چیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78662" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78661">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgWN15uwIJNgZOXDFDop2dJtrkvmh2Rzpk8OwItwNmoJIBc5OYf-X1VfZcSD67_eV6ry4ycBDO8Ak6G8aKghQZ6qxAAkoFjA8y904HNlCb53hbAnJvxuqjxPgxmegg6wV7EK-2FkZ62AgxnFvRbu3EWtNz1ZjLInTzf50Mj7ww5_iR-KqBHcbxli3cxYLm6sQGrMk--OChaIg3ZMxm2ByoqRxAjXlfb7YhsQ_JZFn-hDk9Qck6nBz3WDel70QbL2k8fIaJWaO7nNkscSyglzqOdFifG7ZQUxW1MtvM7Jnm9pJFTd3M-5yOC5eoNcjXuUKNprKLjfus9Xr_LSQa_toA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز پنج‌شنبه ۱۶ مهر گزارش داد شرکت هواپیمایی لوفت‌هانزای آلمان پروازهای خود به ریاض را تا ۲۴ مهر و ایر ایندیا پروازهای خود به مقصد و از مبدا پایتخت عربستان سعودی را تا ۱۸ مهر لغو کرده‌اند.
این تصمیم همزمان با تشدید حملات حوثی‌های یمن مورد حمایت جمهوری اسلامی به فرودگاه‌ها و زیرساخت‌های عربستان سعودی اعلام شد.
حوثی‌ها اعلام کردند فرودگاه بین‌المللی ملک خالد در ریاض را با موشک بالستیک هدف قرار داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78661" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/he4UBr7xsg0Bv_3BpIzV2NShlo5yqDN99ew4TkiF3cT3qi0Aorc4fNkJCg4_j8Gu2asoA2VHmMvV71boOlM0icB7sOAVZFmJgVDvD6JLmaff2wGh6NeaAPheN-S0to-EkKiUwnURqaTfZA2oh9LLa8OWOCxMvqOJ-WEZT-rCWElV4Tig5IiHK1YyDlsxeRmo05rn_pOExQuzd6K_V8Bw-I7eRru5TrO77w3urQncYQ5Y-VX03dZlEm44kxM7ySqoSGzHXVbIr_eZ5Q-Y4DZJnfiVLcAEymsoETdefh6tvl6J0qUR8K9xOqlTBeVlcQrUTePvL5EovFTNcJ12iqYp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارگارت همیلتون، دانشمند آمریکایی و از پیشگامان مهندسی نرم‌افزار که نقش مهمی در فرود نخستین فضانوردان آمریکایی بر سطح ماه داشت، در ۹۰ سالگی درگذشت. او رهبری گروهی از متخصصان را بر عهده داشت که نرم‌افزارهای مورد استفاده در ماموریت‌های فضایی آپولوی ناسا را طراحی و توسعه دادند.
موسسه فناوری ماساچوست (MIT) با تایید درگذشت همیلتون اعلام کرد که او روز چهارشنبه هشتم مهرماه ۱۴۰۵، برابر با ۳۰ سپتامبر ۲۰۲۶، از دنیا رفته است. این موسسه در بیانیه‌ای، همیلتون را از پیشگامان علوم کامپیوتر توصیف کرد که پیش از فراگیر شدن حرفه مهندسی نرم‌افزار، در توسعه این حوزه نقش مهمی داشت.
همیلتون از سال ۱۹۵۹ تا اواسط دهه ۱۹۷۰ در موسسه فناوری ماساچوست فعالیت می‌کرد و مدیریت بخش مهندسی نرم‌افزار را بر عهده داشت. گروه تحت مدیریت او نرم‌افزارهای هدایت و کنترل فضاپیمای آپولو ۱۱ را طراحی کرد که در فرود تاریخی نیل آرمسترانگ و باز آلدرین بر ماه در سال ۱۹۶۹ نقش تعیین‌کننده‌ای داشتند.
در جریان این ماموریت، رایانه فضاپیما لحظاتی پیش از فرود با مشکل پردازش بیش از ظرفیت روبه‌رو شد، اما نرم‌افزار طراحی‌شده توسط گروه همیلتون توانست با اولویت‌بندی وظایف، عملیات فرود را ادامه دهد.
باراک اوباما، رئیس‌جمهوری پیشین آمریکا، در سال ۲۰۱۶ به پاس دستاوردهای علمی همیلتون و نقش او در پیشرفت فناوری فضایی، نشان آزادی ریاست‌جمهوری را به او اهدا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78660" target="_blank">📅 19:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4QinoJwYiyuzNolUMEd9Elyy7tZU0KfnavwuydCDYEti4s_I7TjXfh-FuU7B_mJCWamp8zeOkZJ_qK3qy5vXVP_jdEzHt-aSmX6JAkNda4U1U2FpB15V2YMWmH3PqY3Gttu2HcLTyO44dSB-dhLqeFW_gmLFlqDY42SGXYtG_egCNpXIMvzBSPzJNwg6_uGrj7u00XZa7M_DQATW8g4ND7FpeObpgD2h6uikPnTDe3prBtuTy5rabwFP8o6VBBTwLI6UhCUn390OX5zuR_bkP_p0PLRt6dBiyESR43bhRes7WLo86el3bGHnDLaXcL56x3OqwCWge6ax5hN6_Y6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی در چارچوب طرحی به ارزش حدود ۲۱ میلیارد دلار، توسعه میدان نفتی مرجان را برای افزایش ظرفیت تولید نفت و فرآوری گاز دنبال می‌کند؛ میدانی مشترک با ایران که بخش ایرانی آن «فروزان» نام دارد. براساس گزارش مرکز داده‌های باز ایران، عربستان روزانه حدود ۷۳ میلیون مترمکعب گاز از این میدان برداشت می‌کند، در حالی که ایران از بخش خود گازی تولید نمی‌کند.
در تازه‌ترین مرحله توسعه مرجان، شرکت نفت عربستان، آرامکو، قراردادی با شرکت آمریکایی «کی‌بی‌آر» برای نوسازی تاسیسات این میدان امضا کرده است. کی‌بی‌آر روز سه‌شنبه ۱۴ مهر ۱۴۰۵ اعلام کرد خدمات مهندسی و اجرای پروژه را برای تاسیسات فرآوری، فشرده‌سازی گاز و زیرساخت‌های برق مرجان ارائه خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78659" target="_blank">📅 15:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78658">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAgC81Wfs5gQIsvx0wI0Eh-IXyW6V2w3aunOYFcGAC8eoH2HYPBVvrREZMtiv3t-0ABaeJua_7NhXEjlP7Vk_mqs5nTpRW7koctSWzdQ629zoYepIRHzdUExgJOiDM71o8mdi9HXG_aRWBIuTd4gmKk-CEE4hvjNeohpfhO-pz1nnyyD4wjp1zAvpmKpzP6ZF69yV9Wv1VX3sHXlt9ysvapOAEWJefYbNlpvrCNOME0XGgjVn3OFR2sPqITl2Dxy8JfWBHdA94pO23eoSq3Gv4ICG3tZqEg5hYTedGDqT8jxobZ4N3QiuFV4dpVTeSvQX-M__swEseGtNh24joalow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز، روز پنجشنبه ۱۶ مهر ماه، گزارش داد شمار کشتی‌هایی که از تنگه هرمز عبور می‌کنند، پس از افزایش حملات به نفتکش‌ها در هفته گذشته، به پایین‌ترین سطح در بیش از دو ماه گذشته رسیده است.
رویترز بر اساس داده‌ها و تحلیل‌های شرکت تحلیل کپلر گزارش کرد، روز سه‌شنبه فقط ۷ کشتی تجاری از تنگه هرمز عبور کردند که پایین‌ترین رقم از اول مردادماه تاکنون محسوب می‌شود.
عبور نفت خام از این تنگه نیز با کاهش ۲۷ درصدی نسبت به بالاترین سطح زمان جنگ در هفته قبل، به دست‌کم ۱۰.۱ میلیون بشکه در روز رسید که معادل ۷۴ درصد سطح پیش از جنگ است.
به گفته تحلیلگران کپلر، بخش عمده این کاهش به انتقال محموله‌ها از کشتی به کشتی در دریای عمان مربوط می‌شود.
به گزارش رویترز، با این حال، صادرات از سواحل دریای عمان و دریای سرخ به ۶.۷ میلیون بشکه در روز افزایش یافت، رقمی بیش از دو برابر سطح پیش از جنگ که به جبران کاهش عرضه از طریق تنگه هرمز کمک کرد.
داده‌های کپلر نشان می‌دهد تعداد کشتی‌های عبوری روز چهارشنبه به ۱۰ عدد افزایش یافت، اما همچنان بسیار کمتر از بیش از ۲۰ کشتی در روزهای یکشنبه و دوشنبه بود.
این گزارش پس از آن منتشر می‌شود که حملات به نفتکش‌های عبوری از تنگه هرمز در هفته گذشته به بالاترین میزان هفتگی از زمان آغاز جنگ ایران رسید. پیش از آغاز جنگ در نهم اسفند سال گذشته، روزانه حدود ۱۲۵ کشتی تجاری بزرگ شامل نفتکش‌ها، کشتی‌های حامل گاز، کشتی‌های فله‌بر و کشتی‌های کانتینری از تنگه هرمز عبور می‌کردند.
همزمان، دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنحشنبه نموداری در شبکه اجتماعی تروث سوشال منتشر کرد که نشان می‌دهد سطح تردد نفت از تنگه هرمز به میزان پیش از جنگ آمریکا و اسرائیل علیه ایران بازگشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78658" target="_blank">📅 15:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78657">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeeKFv9CdTyorubtSeofGQaq5ExrjSiar7Ed6tdZNT2YaB88n8x6T4jm73YrIzzpDksgnb6Sb14j_Fqc7-MIAhgcYKcUgojxhhYEwim12nczlfoHtg8sBBxv9l7kHytGq_WSR-yov_I5vPFKWSw05Gmb8AH4xH2sDUwKTPbU64Pv6IqYzq9zfelW-botnxZ78fjazge_8-M1HtDDHvqz6yRcTQrn-4gv5OOogpdQh1p_DXFlc73BdUBGKdkrDAIbcti_OJEZA9KqAbc9DbbXfJ5TMlfPb8MYQEac4slpOodRlwSYlnJ4mXRy2w4kJqm4TnHC6mm3Y8za24zS2rjnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی حمله افراد مسلح ناشناس به ستاد فرماندهی انتظامی شهرستان گلشن در سیستان‌وبلوچستان، نیروی انتظامی وقوع انفجار و تیراندازی در این منطقه را تایید کرد. هم‌زمان، ارتش جمهوری اسلامی از کشته‌شدن یک نفر و زخمی‌شدن سه نفر دیگر در حمله‌ای جداگانه به مینی‌بوس حامل کارکنان ارتش در زاهدان خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78657" target="_blank">📅 15:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DS8FHIvAdUWO4D8--GsIHUPBrkLcoqCkGvheN9VuuLYf321NkgAkkbIH37JPqEKCZscSnjZlAWWdco40_oq1-9_opiR370n32YgzjPBmyKkM4XjWtCnEgyvxCw_4A24r7WBIMBw9biZHb4ynlS5yLgTrVjwImSTZcn6emLBHaG8-EfKPer168gx51JOQFB-w6rWjRWWi4uo4fs6ikIuy1fnzDH8LQaM4Y-By1U2xRgkVqYNQZ3gqMD5oEwd4UPGOFOUa5iGgLrsQDevy_GvRpwGJV9oysgyZLarreuJIarhnuPfbRsZsr9WJCD_zl4aRYuDqGzSvyOULCSjEkdRGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز
پنج‌شنبه ۱۶ مهر در گزارشی تحقیقی بر اساس گفت‌وگو با بیش از ۷۵ کارشناس حقوق بشر، وکیل و شهروند ایرانی نوشت ایران پس از اعتراضات دی‌ماه شاهد شدیدترین سرکوب چند دهه اخیر از سوی جمهوری اسلامی است.
به نوشته رویترز، دستگاه‌های امنیتی و قضایی جمهوری اسلامی با همکاری صداوسیمای حکومتی، از طریق اعدام‌های شتاب‌زده، محاکمه‌های غیرعلنی، پیگردهای قضایی گسترده و انتشار اعترافات اجباری، در پی ایجاد فضای ترس و خاموش کردن مخالفان هستند.
بر اساس این گزارش، از ۲۸ اسفند ۱۴۰۴ تاکنون دست‌کم ۳۴ نفر از افرادی که در ارتباط با اعتراضات دی‌ماه بازداشت شده بودند، اعدام شده‌اند. پنج نفر از آن‌ها تنها در ۱۰ روز گذشته اعدام شدند. در مقابل، طی چهار سال پس از اعتراضات ۱۴۰۱، در مجموع ۱۵ نفر در ارتباط با آن اعتراضات اعدام شدند.
رویترز همچنین گزارش داد مقام‌های امنیتی ارمنستان در ماه مه به گروهی از معترضان ایرانی درباره تهدیدهای جدی علیه جانشان هشدار دادند و از آن‌ها خواستند برای حفظ امنیت خود و خانواده‌هایشان این کشور را ترک کنند.
اشکان، معترض ایرانی ۳۰ ساله که در جلسه با مقام‌های امنیتی ارمنستان حضور داشت، گفت به آن‌ها هشدار داده شد افرادی احتمالا برای ربودن، ترور یا آسیب رساندن به آن‌ها اعزام شده‌اند. رویترز نوشت روایت او را با گفته‌های معترض دیگری که در همان جلسه حضور داشت و فایل صوتی آن جلسه تطبیق داده است.
رویترز همچنین نوشت نهادهای امنیتی جمهوری اسلامی با تهدید خانواده‌های مخالفان ساکن خارج از کشور در داخل ایران، لغو گذرنامه‌ها و خودداری از ارائه خدمات کنسولی، فشار بر منتقدان را به خارج از مرزهای ایران گسترش داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78656" target="_blank">📅 15:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJBdBlhBw_-Uaub8i3Ns-hcI_1B1K6CFTT0pI6qMDWuyBpPjpF3NyWDS6rsGz43MyqpcSMF4WjDEOl8YcqENoHbSFrdXuq77deOK_9i7C90frjY1clsvMskqNvM5AEFv4JfzCBXrrlZy6cUrA9uQzbqyllX_uMK2g_R1stDD_uTPo3gaBUEuO3PNlXZjFKAWM-i1tpLeeAu-4h6WJ1kC38JM2MJkf9RRY9SBCM1XxZPYIfd1tTPz0P2Nx5VMecV7-f2JZRMcc-sim0eafQWAv1vIyrypz_ZEUcmmsumYZWBDlRsVbnmU1yj_i0r2rPEVLBU0aV1vyVwys7BlrpjjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، بامداد پنجشنبه ۱۶ مهر در سخنرانی در ایالت تگزاس درباره جنگ با ایران گفت این جنگ «خیلی زود» پایان خواهد یافت و ایران را «کشوری شکست‌خورده» توصیف کرد.
ترامپ گفت: «وقتی این جنگ تمام شود که خیلی زود خواهد بود، آن‌ها یک کشور شکست‌خورده‌اند، کمی رمق برایشان مانده، اما نه زیاد.»
او همچنین با اشاره به نفت عبوری از تنگه هرمز گفت این نفت در سراسر جهان توزیع می‌شود و بار دیگر بر نقش آمریکا در انتقال نفت از این مسیر تاکید کرد.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا در جریان یک گردهمایی انتخاباتی در تگزاس گفت «ما به زودی از ایران خارج می‌شویم و قیمت نفت هم مثل سنگ پایین می‌آید.»
او گفت افزایش بهای نفت ارزش جلوگیری از دستیابی ایران به سلاح هسته‌ای را دارد.
رئیس‌جمهور آمریکا همچنین در مورد احتمال دستیابی به یک توافق با ایران گفت: فکر می‌کنم این توافق واقعاً چیزی است که می‌خواهم انجام دهم، اما آیا آن‌ها حاضرند برای متوقف کردن برنامه هسته‌ایشان چیزی به ما پیشنهاد دهند؟ و ما قطعاً هرگز اجازه نخواهیم داد ایران سلاح هسته‌ای داشته باشد.
آقای ترامپ همچنین با تکرار سخنان جنجالی چند روز گذشته‌اش در مورد حمله فرضی ایران به لس‌انجلس و سن‌دیگو گفت: «همین چند روز پیش گفتم: بگذارید موشکی به سن‌دیگو یا لس‌آنجلس اصابت کند... بگذارید به سن‌دیگو یا لس‌آنجلس حمله کنند تا شاهد اتفاقات ناگوار باشید... ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما از شهرهایمان محافظت می‌کنیم. ما از کشورمان محافظت می‌کنیم. ما اجازه نمی‌دهیم چنین چیزی رخ دهد.»
این سومین سفر دونالد ترامپ در طول یک ماه گذشته به تگزاس برای تبلیغ نامزدهای جمهوری‌خواه محسوب می‌شود؛ نامزدهایی که در تلاش برای حفظ کنترل کنگره، اکنون با رقابت‌های انتخاباتی میان‌دوره‌ایِ به‌طور غیرمنتظره‌ای فشرده روبرو هستند.
ترامپ در ورزشگاهی مملو از جمعیت در سن‌آنتونیو سخنرانی کرد تا از کن پکستون، نامزد جمهوری‌خواه سنا در این ایالت حمایت کند که در رقابتی تنگاتنگ با جیمز تالاریکو، رقیب دموکرات خود، قرار دارد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78655" target="_blank">📅 05:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHl4Zc0sa9EnX4j-YZ0UvUz16lz0WbrCrSH4q-AuddSlqefXevDrG_J2yniwTFwHOnVgCevskiGIm9Ngll7BlUaUfNWVEVfr6ZreGQBur-3O7Q-ymt7KLLnYn1dfCIkwU3QKWYTmhnzhZMAaWgHcav-gEFjuECSa0zdvzboiWVlNK4qTa9hYj0gY47KKhQw7dxFDyaGQ9m2ONZqSTb0BLMhFbBF3kkGBH9lpjTwh1gCniESXCWNLsqKDs8wPsmkTvrpsS7Xbc1DH9GOnMqUahfwdTvB5j8w1HFQJsfexlFRCpFu75j2xnf4w93Tibhp4a_7tCrSHqxiLf0oF64_BuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رسانه آمریکایی گزارش کرده‌اند که پنتاگون برای حمله احتمالی مجدد به ایران طی روزهای آتی آماده می‌شود.
سایت خبری اکسیوس به نقل از مقام‌های آمریکایی گزارش کرده طی روزهای اخیر پنتاگون با صدور دستورالعملی از سنتکام (فرماندهی مرکزی آمریکا در منطقه خاورمیانه) خواسته روند آمادگی خود را برای از سرگیری عملیات رزمی عمده علیه ایران تکمیل کند.
همچنین مجله آتلانتیک هم در گزارشی اختصاصی به نقل از دو مقام آمریکایی نوشته کاخ سفید از پنتاگون خواسته است تا گزینه‌هایی برای حمله به اهداف ایرانی تدوین کند که امکان اجرای آن‌ها پیش از انتخابات میان‌دوره‌ای وجود داشته باشد.
به گزارش آتلانتیک، دونالد ترامپ مشتاق است پیش از انتخابات، قیمت بنزین را کاهش دهد و به پیشرفتی عمده در مناقشه با ایران برسد.
به گزارش اکسیوس، دستورالعمل پنتاگون شامل تاریخ مشخصی برای آغاز حملات نبود و دونالد ترامپ هنوز تصمیم نهایی را اتخاذ نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78654" target="_blank">📅 05:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZQcO6iV3Sd5EycU3hXeD8Be2yGqRgjCLzbppnLGrMpMqkmNMMDMdaE3k7A9PPTA_UVXv9p-jz3ZRIo2IL-U_gv99U4ksLE-GSaZdG18GtFamkiF0gEpvtSuhKUfj5dcfsbyd3wduNPIqPGGlrcE-ZYXxIc8W8MbbMF9SRwgD5LizuA4uml4h9CN9BuXkjNJnBBPCKout55LrqsJ7PiLvPpXtuSCajFfKMQBqf0lnsjBQnUnhG335-cTjaG29mpO6HlihAANfYKJhDACE4HeSBuDLorsszJhPqkkFHTx376y5kQytmjK_zsI_FaejVGdAlBPT5XqP2ivjgAkcHwTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ارتش آمریکا، سنتکام، بامداد پنجشنبه ۱۶ مهر با انتشار پیامی در اکس، اظهارات یکی از فرماندهان سپاه پاسداران درباره بسته بودن تنگه هرمز و کنترل کامل ایران بر آن را «نادرست» خواند.
سنتکام اعلام کرد تردد کشتی‌های حامل کالاهای تجاری و محموله‌های انرژی، از جمله ۲۰ میلیون بشکه نفت خام، در تنگه هرمز جریان دارد و افزود: «ایالات متحده و شرکای منطقه‌ای به‌وضوح کنترل تنگه را در اختیار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78653" target="_blank">📅 02:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T6_m89VMvoFmgcnmLfA5HPHl-sWLTXtZ5IrLFQfCnOK0VO6TVfMHAbxE9qBIgEOh7Lbv53N705JuosqVJgCYdRMC9a8Xj5_veNB5s5JePPj505u35xtYNJ6SzRXaC2gjw5yJ-yXLrbzd-eJhFNDh9e8eoVWEh7Y4Fb6FI5D5peNTKHg9jBUk5J0pqRpd8hx3Qr22ce6jNKzHQpaxFtZQFGhqq_MFr6DOoOdGcYRygX_DCOkttvHdFeQQLltrBRdeSHSD4u7QnuBMsax-BdTllyhEc0aU27kTXgpzLZsGHOuVsxjkgqLqO9RDmzD4fWkwct4iqtBPgAL1ljnKt1EZog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات تجارت دریایی بریتانیا: در حمله به یک نفتکش در شمال قطر خسارت جانی گزارش شده است
سازمان عملیات تجارت دریایی بریتانیا شامگاه چهارشنبه ۱۵ مهر اعلام کرد یک نفتکش در آب‌های شمال قطر، در ۵۱ مایلی مدینه‌الشمال، با چند پرتابه هدف قرار گرفت.
بر اساس اعلام این سازمان، در این حمله تلفات جانی گزارش شده، اما هنوز جزییاتی درباره شمار کشته‌ها یا مجروحان منتشر نشده است. مقام‌ها در حال بررسی حادثه‌اند و از کشتی‌های منطقه خواسته شده با احتیاط تردد کرده و هرگونه فعالیت مشکوک را گزارش کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78652" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1230VGbpPpP37ldAYADfMRoVFbGcqgFAx7o2SwO8Xpi9bAoVAH2E5GgXNfzaV0smi0zzFrdb-u9L6RJH_SD6_PlheOfNpGJgxmkvYYrLHk1QMKvoSKqclnJ2RWk2_o2AOjQwWvy66smPXyWUN-PZJ7BSSZy1cAvEwhje0RGdXlKMn7JVoa_-OeLs_S3wRcB6WVtMJQIFaX18jCXf3QdRy8AcrOYQ5Di6lf1xetD76-poQRs7FbXbd6pZGkYj2SdknIhG-zlANI-2fWxQq1K7qPDbm7aiWIl3_BLLsP_S20J7kVm5cTQEy7haB65_ZVqGPNHFC5YYgPFza9HaL5plg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع مطلع به خبرگزاری رویترز گفته‌اند جمهوری اسلامی ماه گذشته ۲۰۰ میلیون دلار در اختیار حزب‌الله لبنان قرار داده است تا این گروه به خانواده‌های لبنانی آواره‌شده در جنگ امسال با اسراییل کمک مالی کند.
بر اساس اطلاعات منابع رویترز، حزب‌الله قصد دارد در مرحله نخست به هر خانواده حدود سه هزار دلار کمک کند. اولویت با خانواده‌هایی خواهد بود که روستاهایشان ویران شده یا به دلیل حضور نیروهای اسراییلی در مناطق جنوبی لبنان امکان بازگشت به محل زندگی خود را ندارند.
یکی از منابع شمار این خانواده‌ها را حدود ۵۰ هزار خانواده اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78651" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIRHwSC7g7V6AnwAoTRYkVvL8cmmcrNasAy5KHfgrWnSF_X2kZrlXNcL0ROvGvZ0n11d-tKu3jUQ_fNMfzHunXR15zV0vsKnJPoMTniqbMDSQ_DHFupsuV0fm_TwFcjNkj5Q-XWsrtTNy4MsoRhsnlsZRCv1R4ADsJlp_k-kdc-L9rEIq4TkZ7iNeeyMKu99xEz1o3IbU781z_NTpJkl9FsL2ZbbcLmEHgTENKqO6KGGwp0IU2M7tRMIHtXvBIsBWBpidA4CaBEEq3NTt6iE-euvRmJsYUF-Ma6CShPIaRQCBzWjTy-PGd7_IWJbZmzZWvtKAJBTX855MIA4GjbWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهاره آقایی، وکیل دادگستری محبوس در زندان قرچک ورامین، به ۲۰ سال حبس محکوم شده است.
کانال تلگرامی شیرین عبادی
با اعلام این خبر، حمایت از معترضان دی‌ماه، حضور در مراسم چهلم سپهر شکری و کمک حقوقی به خانواده‌های دادخواه را از موارد مطرح‌شده در پرونده او عنوان کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78650" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIhLoFJV95W2pp4Lt4HM5wAIsrxoJyv7KVcqHDnEWy4Y02kDpGpe5K7gE_DKhPuvAnXk1zwNf8HODSZItYSofH4QmiAxeGNvdw_2LLQg0G1j6GfzK9jt6tbQoThZbWhWKvqCsdKNI7M-yKI9-A68SoRUW86-HcODwi6M33_S0TitQvsnJbICDk6_tleubBwWbiqvMmQ0ZBg1LYF973hXLbSWn7DFOtudlTMMukawZ6-t82FMWcjcB1QLDxGMpyo8ezWoomrbjb3t5_cd9vk85a4B-hMc9GsUetP75ds9xCeLBtH2r1z2rahazQrtpjq1BIJDt3o3rFmjpSxeXl3XQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده آمریکا، با انتشار پیامی در اکس و با لحنی کنایه‌آمیز نسبت به استعفای محسن پاک‌نژاد، وزیر نفت ایران نوشت: «ایران وزیر نفت جدیدی دارد. با توجه به اینکه از ۲۵ اوت تاکنون حتی یک بشکه نفت خام نیز توسط ایران بر روی هیچ شناوری بارگیری نشده است، این وزیر نفت دقیقا چه چیزی را مدیریت می‌کند؟» پیش از این، مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر ریاست جمهوری ایران اعلام کرد، پزشکیان پس از موافقیت با استعفای وزیر نفت، طی حکمی حمید بورد، مدیرعامل شرکت ملی نفت ایران را به عنوان سرپرست وزارت نفت منصوب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78649" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USJFmpSN4x30bz38yvibzXdr7lefyHmDYaVQdoQPJhKsCdS8G7A9uIrqBkj1EWI4OqualayG02wjSo3HN4UCh_dmTEbE8BRG6RiLDtqVbBH7YZH9Bwt6Db4Suxf53TbPUBxGrYkTE7U5ANYkx_CryKGieu2M4VKMfyhnHONzuHNnR3sJBjq-nvVIWGiWI3wbRj34HEKeMnY1zpMzi3S0CEMWWn-mWL3EnUuN9lQEf9cJ_ClMEITnooU_3_5V3pwFdI9CkHQUaAlP4azsCgoksL0VMfdytd4TiO0AJ2Kd-cXCRrTrGk-Rddj0DHUP1UT33XeoHIcLKitID0XNvWURzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام امید گودرزوند چگینی، معترض ۳۷ ساله، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ و محبوس در زندان چوبیندر قزوین، در مرحله تجدیدنظر تایید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78648" target="_blank">📅 17:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8gTi4UcaA5lERYQuhR38LKsocqC3Fo2kOKiOGhxU2XIhH9xxazre0G7Jwu0aOlTw5zWcLOV-atPSuYJbo_VQ0dvBUFLg1kqC7oik_CkzZBmPn2gPqJrDKkM4ijq8ApnIaCMyLFUUTRmjpH2igb_TIUTxVwWrm3LhFxPt7C-HKvrdkhA8lzIn0QjBy7vWLN1BOANBFo_tkq8ZmYujpc9V3YcU2cu4_6AhEum5X48-39RNBj0lQ3H-cfJ1zDgQa-xhA-7Z7jM-coQA_2lXJiBBgF-CojrLtARPTyzdND3wc51bsqvN38FpAW6guB8pAFDH9UWJQjtomTCFxw48kPoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20e0cac582.mp4?token=r2O3vgZhgmviIOsPk13nhPwzkjnkI-ILZ1GEmlwJqEUE6hNki3qu3PNuedKe1k1xcar5DLNrKCJiVQgXd6UL4sBqADWLmks-vZi-Pasp1zY3c9hrLc_OkNZnlZFMSz31WmWmlw2iJ2mnt-4SaoekTLv3SHNJwSfL_qOOj4MkZx7LufPZmQmRjgGUZM56gCvcJHA0svqj75-KeKSxqgKBhzs66W2p5tSk-32_HiYsmvruibl_S5jXhJAiRwR_Y17bNSDpVN8N5fEgfDhsr6kLZ5EkSdu2JUI-4ayTOUBptGED1PO8pa3PpeyyPoqZcPMnV89m1soIeiVZyokRSv7AgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20e0cac582.mp4?token=r2O3vgZhgmviIOsPk13nhPwzkjnkI-ILZ1GEmlwJqEUE6hNki3qu3PNuedKe1k1xcar5DLNrKCJiVQgXd6UL4sBqADWLmks-vZi-Pasp1zY3c9hrLc_OkNZnlZFMSz31WmWmlw2iJ2mnt-4SaoekTLv3SHNJwSfL_qOOj4MkZx7LufPZmQmRjgGUZM56gCvcJHA0svqj75-KeKSxqgKBhzs66W2p5tSk-32_HiYsmvruibl_S5jXhJAiRwR_Y17bNSDpVN8N5fEgfDhsr6kLZ5EkSdu2JUI-4ayTOUBptGED1PO8pa3PpeyyPoqZcPMnV89m1soIeiVZyokRSv7AgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید ایران فرصت‌های متعددی را برای دستیابی به توافقی دربارهٔ برنامه هسته‌ای خود با ایالات متحده از دست داده است.
او روز چهارشنبه ۱۵ مهر در یک نشست خبری مشترک با همتای یونانی خود در آتن گفت: «ایران فرصت‌های متعددی را برای رسیدن به توافق هسته‌ای با آمریکا از دست داده و همچنان مبالغ هنگفتی را صرف تروریسم، تسلیحات و حزب‌الله می‌کند.»
روبیو همچنین گفت ایران اکنون با اقتصادی رو به فروپاشی و تحریم‌های تازه روبه‌رو است و مسئولیت این وضعیت را متوجه «روحانیون تندرو شیعه حاکم بر ایران» دانست.
او گفت: «اقتصاد ایران در آستانهٔ رسیدن به وضعیتی است که از نظر وخامت، کمتر کشوری در جهان آن را تجربه کرده است و همهٔ این‌ها نتیجهٔ عملکرد روحانیون تندروی شیعه‌ای است که در آن کشور تصمیم‌گیری می‌کنند. آن‌ها هستند که مردم محروم ایران را به چنین وضعیتی دچار کرده‌اند.»
وزیر خارجه آمریکا همچنین با تکرار موضع واشینگتن دربارهٔ جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت دونالد ترامپ توان نظامی و بخش بزرگی از ظرفیت صنایع نظامی ایران را از میان برده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78646" target="_blank">📅 16:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lCO2s9z716qS5w_2ZXhnxK_b_ddgCivpumPebTiOogRlMfDQWiWiEkwfo4BhyiAgsm61I3Gz4AM7gYqfwawVfY0so_vASxhHQK3asZp-kmXSQJ1l4N6VGtLWoTxkOm0iEHwMjNLCIhAI6Cb2HY5pTDKIlHC1KPKtWrFP6BmlFiGpEFxzbdDZclY_vrBj4g1oKRn9vWSURVx2_J3lGOHtBfZpN63MNgetIwyNjIrUIoKAJMatiyDYTFl7QGrg_j0NqJI8Ws7qjpdXhcmruIeWOBHyRrAHrO5g9xoCDHA41YndS3HZd4sLRg4Cm8TRymyFYd6pq3Jk8Nyw_iD_PHYDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه خراسان نوشت که نجمه امینی، دختر ۲۳ ساله، به اتهام «سب‌النبی و توهین به ائمه معصومین» در فضای مجازی، از سوی شعبه ششم دادگاه کیفری یک خراسان رضوی به اعدام محکوم شده است.
امینی پیش‌تر در یک فایل صوتی از زندان وکیل‌آباد مشهد از صدور حکم اعدام برای خود خبر داده بود.
پس از انتشار این فایل صوتی، خبرگزاری فارس، وابسته به سپاه پاسداران، اعلام کرد که هنوز هیچ حکم قطعی برای نجمه امینی صادر نشده و دیوان نیز درباره پرونده او اعلام نظر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78645" target="_blank">📅 16:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dD3WNZV36BLYbq0bGrgNYqY7RxL8kMeZ9Hvpc46zH3W70em_KcccY3cyEh8HdFuVq0S6XndQ-WmkIOi1mrJIbPNIdVCf9hCRh6aW5bMsOCHlmISBZokRcuxIQFYbfWSJDGCFeUtt8Xrql3XUdWNUsiOenWO-nX7vucraXFFN6Aqj_AxLa2PiCwehDh1_Fxi234w5mGOEZxgzjoElx8boJqDZS8eJ3KaNmLofKNLkUTbXMPv1G4joSIuTlwwYcki47GLjYWGDLWe21SgJZPeINvPeUK57OQOg6k_AF6J50-Kek-3tw86MtwkDvt9KYSLFYXNVvZvr96FeU2zTaZ_4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران باید غنی‌سازی را عملاً کاهش دهد؛ میزان اختیارات پزشکیان و عراقچی روشن نیست
🔸
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، می‌گوید حکومت ایران برای پایان یافتن جنگ باید ظرفیت غنی‌سازی اورانیوم خود را به‌طور «معناداری» کاهش دهد و ایالات متحده در مذاکرات با جمهوری اسلامی، به وعده‌های لفظی بسنده نخواهد کرد و خواهان اقدام عملی تهران است.
🔸
آقای ونس در گفت‌وگو با خبرگزاری رویترز که بامداد چهارشنبه ۱۵ مهر منتشر شد، همچنین گفت ایالات متحده با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه، در تماس و مذاکره است، اما برای واشینگتن روشن نیست این دو مقام تا چه اندازه در ساختار فعلی قدرت ایران اختیار تصمیم‌گیری دارند.
🔸
اظهارات او در حالی مطرح می‌شود که تهران و واشینگتن طی هفته‌های اخیر پیشنهادهایی را برای پایان دادن به جنگ و بازگشایی کامل تنگه هرمز ردوبدل کرده‌اند، اما دو طرف همچنان بر سر دامنهٔ مذاکرات و مسئله هسته‌ای اختلاف اساسی دارند.
🔸
معاون رئیس‌جمهور آمریکا در پاسخ به پرسش رویترز دربارهٔ شرایط واشینگتن، خطاب به مقامات جمهوری اسلامی گفت: «اگر سلاح هسته‌ای نمی‌خواهید، پس چرا به سوخت غنی‌شدهٔ ۶۰ درصدی نیاز دارید؟ و اگر می‌خواهید تعهد خود را به نساختن سلاح هسته‌ای نشان دهید، سوخت با غنای بالا تولید نکنید. این یک مسئله بسیار پایه‌ای و تعیین‌کننده است.»
🔸
او افزود: «فکر می‌کنم اگر آن‌ها بخواهند تعهد خود را به نساختن سلاح هسته‌ای نشان دهند، باید در زمینهٔ ظرفیت غنی‌سازی خود اقدامی معنادار انجام دهند.»
🔸
آقای ونس در عین حال تأکید کرد که آمریکا همچنان برای رسیدن به توافق آمادگی دارد، اما چنین توافقی باید شامل امتیازهای مشخص و عملی از سوی ایران در زمینه برنامه هسته‌ای باشد.
🔸
او گفت: «ما قرار نیست حرف را با عمل معاوضه کنیم.»
🔸
این موضع با مواضعی که مقام‌های جمهوری اسلامی در روزهای اخیر اعلام کرده‌اند فاصلهٔ زیادی دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78644" target="_blank">📅 02:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=N04XYret8hLMqmwzU4AhnZXEFE-Zicw4FCY20e0N0DltWGEGRhyb7UfFw2yHXJMWu2an7F0tP2HIhAwLXvb6dmX97iiv0l0hHHXvoflxOi1c-Px6Nvxqm_2NmBp94ouwp5VS30Sgv1f9YW7OvLBvRLumgPCqOyAE4XrwX1u99CgUiCnPFijc3-VEFokmUoammulqkclHfg9Q8g0soKOIpBSSP3Iv1YmwfvhiJER3chdgDvQyt9xAIvz403h3vVCtXAz7XItaWKMDG0CMoD5x6YJfB4babwF3bWtPElL-fKj_v34Ysu8s1pY9ORb4lv8lFYN9uFQ_ifPqy6ET4LJMBAHow5YB4UEtAuqYPNBHMROaJaNlYQEI_9ziRkZEeBoBwqOiNY-wVmTEDVkalMIgF4qyGSrDOt3muv2_M5VzfggZP3SscUFuuTW060D4QjOj_IoHDajnnkyYlNwNCzFireO3CxYuIhPAm6ChEQXJ0r74AtBAhB0LokXJ7JReuOs6xuSiS-HJK64zKqhHUjR5myciSPKKzYkKAUwUh8vT1AtvyUvrzzQguOx1GwU6yC-Q_436zuGjX11DDNWq18tw9K0tf8nc7lTF-PEcVhA04ir0hpj_baMvtkxQcGtCwXJ_je8jrezVVJQv2WUvRRqjLIe6Unlr-v-2-okULsoda9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=N04XYret8hLMqmwzU4AhnZXEFE-Zicw4FCY20e0N0DltWGEGRhyb7UfFw2yHXJMWu2an7F0tP2HIhAwLXvb6dmX97iiv0l0hHHXvoflxOi1c-Px6Nvxqm_2NmBp94ouwp5VS30Sgv1f9YW7OvLBvRLumgPCqOyAE4XrwX1u99CgUiCnPFijc3-VEFokmUoammulqkclHfg9Q8g0soKOIpBSSP3Iv1YmwfvhiJER3chdgDvQyt9xAIvz403h3vVCtXAz7XItaWKMDG0CMoD5x6YJfB4babwF3bWtPElL-fKj_v34Ysu8s1pY9ORb4lv8lFYN9uFQ_ifPqy6ET4LJMBAHow5YB4UEtAuqYPNBHMROaJaNlYQEI_9ziRkZEeBoBwqOiNY-wVmTEDVkalMIgF4qyGSrDOt3muv2_M5VzfggZP3SscUFuuTW060D4QjOj_IoHDajnnkyYlNwNCzFireO3CxYuIhPAm6ChEQXJ0r74AtBAhB0LokXJ7JReuOs6xuSiS-HJK64zKqhHUjR5myciSPKKzYkKAUwUh8vT1AtvyUvrzzQguOx1GwU6yC-Q_436zuGjX11DDNWq18tw9K0tf8nc7lTF-PEcVhA04ir0hpj_baMvtkxQcGtCwXJ_je8jrezVVJQv2WUvRRqjLIe6Unlr-v-2-okULsoda9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ، به تشخیص و ترجمه ماشین:
ما در جمهوری اسلامی ایران خیلی خوب پیش می‌رویم؛ خیلی خوب. آن‌ها دیگر نیروی نظامی ندارند؛ نابود شده. همه‌چیزشان نابود شده و آن‌ها همان طرف شرور بودند؛ قلدر خاورمیانه بودند و دیگر چندان قلدر نیستند. اما هنوز باید کار را تمام کنیم و فقط مسئله این است که به کدام روش. می‌خواهیم این کار را به روش خوب انجام بدهیم یا به روش نه‌چندان خوب؟ خیلی زود خواهید فهمید.
وقتی به «دیوار فولادی» نگاه می‌کنم، همان کاری که ما انجام داده‌ایم و آن‌ها اسمش را محاصره گذاشته‌اند؛ من اسمش را «دیوار فولادی» می‌گذارم. حتی یک کشتی هم نتوانسته به ایران برسد. تنها کشتی‌هایی که عبور می‌کنند همان‌هایی هستند که ما اجازه عبورشان را می‌دهیم و این تأثیر بسیار بزرگی داشته است.
برای همین کشورشان از نظر مالی شکست خورده است. یک کشور شکست‌خورده‌اند؛ همه دارند کنار می‌کشند، همه دارند می‌روند. به نیروهای نظامی‌شان حقوق نمی‌دهند، به پلیس‌شان حقوق نمی‌دهند، به هیچ‌کس پول نمی‌دهند؛ اوضاعشان به‌هم‌ریخته است. اما هنوز باید کار را تمام کنیم.
نیروی دریایی ما پیشتاز است تا تضمین کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. و این همان چیزی است که همیشه گفته‌ایم: هرگز اتفاق نخواهد افتاد. هرگز اتفاق نخواهد افتاد. این دیگر یک امر انجام‌شده است.
ملوانان و هوانوردان دریایی بزرگ ما قهرمانانه جنگیده‌اند تا ارتش آن‌ها را نابود کنند. آن‌ها دیگر نیروی هوایی ندارند. نیروی هوایی‌شان از بین رفته است. نیروی دریایی‌شان از بین رفته است. آن‌ها ۱۵۹ کشتی دارند؛ همه‌شان همین حالا در اعماق دریا هستند، کف دریا افتاده‌اند. رادارشان از بین رفته است. تمام تجهیزات ضدهوایی‌شان از بین رفته است. ظرفیت تولید موشک و پهپاد آن‌ها به‌شدت کاهش یافته است. به‌زودی آن هم از بین می‌رود. دقیقاً می‌دانیم بقیه‌اش کجاست.
اقتصادشان ویران شده است. تورمی دارند که هیچ کشور دیگری در جهان ندارد. و آن مردی که چند روز پیش رفت، گفت: «من می‌روم چون کشورمان تمام شده.» این را گفت. نمی‌دانم. من هیچ‌چیز را قطعی فرض نمی‌کنم، اما اوضاعشان خوب نیست.
و به لطف مردان و زنان نیروهای مسلح آمریکا، ده‌ها تن از رهبران تروریست ایران از صحنه روزگار محو شده‌اند و مستقیم به دروازه‌های جهنم فرستاده شده‌اند. همان‌طور که می‌دانید، رهبرانشان رفته‌اند. گروه دوم رهبرانشان هم رفته‌اند. و بزرگ‌ترین مشکل من این است که هیچ‌کس نمی‌داند واقعاً چه کسی کشور را اداره می‌کند. هیچ‌کس نمی‌داند؛ شاید هم این چیز خوبی باشد. اما خامنه‌ای را یادتان هست؛ همه‌شان رفته‌اند و حالا ما اینجاییم.
ما داریم کارهایی انجام می‌دهیم که هیچ‌کس قبلاً انجام نداده است. مثلاً تکلیف این کشور باید خیلی وقت پیش روشن می‌شد. حالا ۵۱ سال است. قلدر خاورمیانه. این کار باید خیلی پیش به دست رؤسای جمهور یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم. همیشه ما هستیم. کشورهای دیگر باید خیلی وقت پیش این کار را می‌کردند، چون با گذشت زمان فقط بدتر شد.
اما ما کار را انجام دادیم و راستش مدام از رهبران جهان تماس دارم که خیلی از من تشکر می‌کنند. می‌گویم: «خب، کی می‌خواهید هزینه‌اش را بدهید؟» می‌گویند: «آقا، بابت این کار خوبی که کردید ممنونیم.» و من به آن‌ها می‌گویم: «عالی است. می‌خواهید چند کشتی بفرستید؟» می‌گویند: «آقا، ترجیح می‌دهم درگیر نشوم.» آن‌ها هیچ کشتی‌ای ندارند.
واقعاً داریم بار تمام دنیا را به دوش می‌کشیم. روی دوش ماست. و به یک معنا دوست داریم این کار را انجام بدهیم، چون خودمان قوی‌تر شده‌ایم و دیگران ضعیف‌تر شده‌اند. آن‌ها فقط ضعیف و ناکارآمد شده‌اند و ما کارهایی انجام می‌دهیم که هیچ‌کس دیگر، هیچ کشوری، هرگز نمی‌توانست انجام دهد.
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78643" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/141ace0942.mp4?token=CzPatUqSbFRolIYC5FAqqtGsYwXM8MFbsRAomF1d52zVb_xPXqwEOGXrm8wiWJVP6dGvHsBJCBkh4q8wLRMgb83Fe9Qu7jBJN2KoDHFTjsza2U6lzd14QpOJkac53MJpXgLsbQSZ8WpJgs5Ovk-LAtM12KME_F0zG09EfZ752rFbLlyQQAC19-dsb6XULcTNKDGKC4JXPyIpTfmasQjZ788X6XJrL477o5MEACABZMVI5H1HZ8iIgnjmzdatariLJ8C9fm3-YlAP00fkIj5n-1v-bXbYf-50Dnnqwj438TEjKJc4TZj8jE4P2ICGlubWUutrLovh9Dp9YRLkN-VBVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/141ace0942.mp4?token=CzPatUqSbFRolIYC5FAqqtGsYwXM8MFbsRAomF1d52zVb_xPXqwEOGXrm8wiWJVP6dGvHsBJCBkh4q8wLRMgb83Fe9Qu7jBJN2KoDHFTjsza2U6lzd14QpOJkac53MJpXgLsbQSZ8WpJgs5Ovk-LAtM12KME_F0zG09EfZ752rFbLlyQQAC19-dsb6XULcTNKDGKC4JXPyIpTfmasQjZ788X6XJrL477o5MEACABZMVI5H1HZ8iIgnjmzdatariLJ8C9fm3-YlAP00fkIj5n-1v-bXbYf-50Dnnqwj438TEjKJc4TZj8jE4P2ICGlubWUutrLovh9Dp9YRLkN-VBVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ یک کارمند ۲۸ ساله موسسه تحقیقات ضدطاعون در سیبری پس از ابتلا به بیماری که گمان می‌رود طاعون ریوی بوده باشد، موجب نگرانی‌هایی شده است.
بر اساس این گزارش‌ها، داریا شیپیلووای ۲۸ ساله در ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) به بیمارستانی در شهر شلخوف در منطقه ایرکوتسک منتقل شد و دو روز بعد درگذشت.
ده‌ها نفر که با این زن در تماس بوده‌اند قرنطینه شده و تحت نظر پزشکان قرار گرفته‌اند، اما مقام‌های روسیه می‌گویند تاکنون هیچ مدرکی پیدا نشده که نشان دهد مرگ او با عوامل بیماری‌زایی که در محل کارش با آنها سروکار داشته، مرتبط بوده است.
مقام‌های روسیه می‌گویند وضعیت تحت کنترل است و تاکنون مورد جدیدی از بیماری‌های عفونی مرتبط با این حادثه گزارش نشده است. با این حال، گزارش‌های تاییدنشده درباره احتمال ابتلای این زن به طاعون ریوی در شبکه‌های اجتماعی منتشر شده است.
مارکو روبیو، وزیر خارجه آمریکا، گفته است واشنگتن این موضوع را از نزدیک زیر نظر دارد اما در حال حاضر دلیلی برای نگرانی نمی‌بیند. دونالد ترامپ، رئیس‌جمهور آمریکا هم اعلام کرده که آماده کمک به روسیه است.
@
VahidHeadline
, @
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/78641" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JFHWGAXkrGvUlueLRuOQLict8_EUVCthVoQOpwaBFgbqHh51ClTfOP3eEYjqkD3k2dl90PABIx4X4R3JxVHmAL-_CZWT4kosS6ISBuCu7DE21gXkxevCP7w5bVj1c52LZdfBcbf73yworZTvFiwYZE8wMulBcqPG8wfFb-YQe40xV67s1Vspgy21fPecswtawr7BZsJf2JbAx0WXK73XXs5cbOgMuk3IVfG7xlW6jS4PlJpRWLsiqRKhVjhHPjVC5wEC2FSuIubcvXj4wKAvTwmvo6cpSc8fwyr-2K_VWpnxVgyOFG6GooDP3BIjJnmV8noXAVjacM7FAVkmPOA11A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: رسانه‌های دولتی ایران گزارش‌های نادرستی را منتشر کرده‌اند مبنی بر اینکه یک بالگرد MH-60R نیروی دریایی آمریکا، پس از اعلام وضعیت اضطراری در شب گذشته، در دریای سرخ سقوط کرده است.
✅
واقعیت: گزارش‌ها درباره سقوط یک بالگرد نیروی دریایی آمریکا در دریای سرخ صحت ندارند. همه هواگردها و نیروهای نظامی آمریکا در سراسر خاورمیانه در امنیت هستند و وضعیت همه آن‌ها مشخص است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78640" target="_blank">📅 16:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fSPpo-4q-SOYjAXuNlQqgTgFlepCgLxN8mlNJqFQutAHVUyTSG15_3V-q5pvIhpEO46i9cLh7q_LtsuktbuQCz3uavhdwdz6uZFh0ErHRdhU9oZmK5U6iDDV3F2D0BCB3-R0juUglooGBy-_rhm0H9sR0L_fNL8YFj1n55VCqqGuisXSGMGH__fxzFJpOIu4e1MU57bqxOVXN78z-7LMmpLOI0nu9RMoTM44Eibom7wbs0q-yCJsUyf6ABM6_WuvMZ1P2gv_nrbwkoKq0uCvDxcERQVY-xkg3WQTpbTT9wCMx82LSbqpXCT0sRlB2UlD5hoCf9mTF080ZRwKOB6UOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا بعدازظهر سه‌شنبه ۱۴ مهر اعلام کرد گزارشی با تاخیر درباره حادثه‌ای در تنگه هرمز در ۱۳ مهر دریافت کرده است.
بر اساس گزارش یک «منبع تاییدشده»، یک نفتکش هنگام خروج از تنگه هرمز هدف حمله قرار گرفت.
در این اطلاعیه به هویت نفتکش، عامل حمله یا میزان خسارت احتمالی اشاره‌ای نشده و سازمان عملیات تجارت دریایی بریتانیا اعلام کرده است مقام‌ها در حال بررسی این حادثه‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78639" target="_blank">📅 16:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJMRhw0JylqlVdTV5NQ3RZBOuKpqBhwnFqLLHZwA5Fhsiosu9FfFazbAD5aOeZ-1oS4R42piFbHaBIFKHWk0n3_5akVOzD7EAT7_oMHXrT_kIux1daA-Xj2XHhoVVwYu_Rwzn_2ngwJTXiG7E3VLj8EboW4oH5S6V0Nw_epPu3zVt_vAuPop5bPkNTBpodVnmPBtxZlN3d325QgFQqF3wV9TDkNPUtZIHV4nZcnoeUhSck4Aj8m_fDAGF6Qc_wCKs9v8zAbFBWbrv8BB3EEEucwYP1yWk8Ij0EP0rat4nzMctWrVHvjduaacIuBkLC2r8I0_0g0QuusVgd_fJfIDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز سه‌شنبه ۱۴ مهرماه اعلام کرد شامگاه دوشنبه، فرودگاه بین‌المللی ملک عبدالله بن عبدالعزیز در جازان و فرودگاه بین‌المللی نجران هدف حمله قرار گرفتند.
براساس این بیانیه، این حملات منجر به جراحت جزئی سه نفر و بروز خسارات مادی به فرودگاه‌ها شد.
شورشیان حوثی مورد حمایت جمهوری اسلامی دوشنبه از حمله به فرودگاه‌های عربستان سعودی خبر داده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78638" target="_blank">📅 16:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78637">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLQFCvZoDcgnJMJvpJMegFkkXHH08aZiJNKUOf3Y2PGBfy0b1ebkQOGdMUBC26OR9Q-vkUtcn9INAZCTcI7gfV2vUKY_OMjj27hlDP1rN3ZkzSEHDNl2EvQnCTL8gmKolOUIrB7UeMnw2gGKpIzs-HHW9JLIMa_l-RqcbgElTvND7gGehKb_yTHvVjsoDVCZmX7UAm8jEGONp9X8sgA2suuh6cbG_2UWHylDeZMw5Oh6M60o8ZY2t4ZwN5HLX_IDoWw56Fnr0K0dsqNoY-UbD-axhZqpETdo-m-o0rQnISo2wuEWefqmtn093n_ZxEFOr9iSd2PssXfs9qMy5bptPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ کشور قاره آمریکا در بیانیه‌ای که روز دوشنبه، ۱۳ مهرماه، منتشر شد «اقدامات تروریستی» جمهوری اسلامی و نیروهای نیابتی‌اش در نیمکره غربی را محکوم کردند.
در این بیانیه به «تلاش‌های خصمانه ایران و نیروهای نیابتی‌اش از جمله نقشه‌های مرگبار، تأمین غیرقانونی پول، مداخله سیاسی و فعالیت برای نفوذ خارجی» اشاره شده است.
این بیانیه اشاره می‌کند که هدف از این گونه اقدامات «تقویت شبکه‌های تروریستی، تضعیف فرایندهای قانونی یا دولتی و ضربه زدن به امنیت منطقه‌ای» است.
ایالات متحده، آرژانتین، کانادا، کلمبیا،‌ کستاریکا، جمهوری دومینیکن، گویان، پاراگوئه،‌ پرو، و ترینیداد و توباگو امضاکنندگان این بیانیه هستند.
این بیانیه پس از آن منتشر می‌شود که آمریکا و پاراگوئه در ماه سپتامبر گذشته به طور مشترک «نشست مقابله با تروریسم فراملی» را با هدف همکاری در نیمکره غربی علیه «فعالیت تروریستی» تهران برگزار کردند.
سال گذشته اکوادور که متحد آمریکا است سپاه پاسداران، حماس و حزب‌الله را سازمان‌های تروریستی اعلام کرد و آرژانتین نیز در بهمن‌ماه ۱۴۰۴ نیروی قدس سپاه پاسداران را در فهرست تروریستی قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78637" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Feil0DLA5d472qmfdUT_ptUfKdwkW9pBs_vcoLmNeA1EWKji1TxrS9nrL2kA_gNvxHxx30NAosyH208Q0LDQCfBU9hSqOVI-fce0G2C401H6IavwSoxC2_odaR5Mwor-A5ZUlBvefY75VRpaIMduQGsb6rj7J56oVNEM4k4GKmLZ8NXxAUdZGSo7FuEV-wexz3PMoRvbe07MCCn0AVwRzGbv29fuWWnvtWy8BH7lOOSb6GTVaqj9jJEtfhCCKLX5hIqI_T1DYOs_9lTyhBHJB9bkge3lIqXqaBimq5LVv1wJJEGtzcbAXPL_VrPFWpasZZ3Wnd8Y3HVQ91CnzZYlFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی عباسیان، ۳۸ ساله و ساکن شیروان، از سوی دادگاه انقلاب بجنورد به اعدام محکوم شده است.
یک منبع مطلع به ایران‌اینترنشنال گفت حکم اعدام عباسیان یکشنبه ۱۳ مهر در زندان شیروان به او ابلاغ شد.
هادی عباسیان در جریان اعتراضات دی ماه با انتشار ویدیوهایی از مردم خواسته بود در اعتراضات شرکت کنند.
تاکنون اتهام دقیق منجر به صدور حکم اعدام و مستندات دادگاه علیه عباسیان مشخص نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78636" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78635">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqvIRBNSS8HwterXNA4ytVtu34poUIB0gvdC1aMQxULcKzLkG3I468iAoqacPFLbc8snyMGEkgEX309YXSXD8brr93G6ZKchep15WSNMAedHq--Pr9MRcV8KM7tQ60IP4fDzn4QaVbRnRLfqvUwoKyFeiXQAcIsPMj2iRmQyGSxM16smryluNTro2F9C0odBvb_-zSqDzsXZdfzGGF5Jjbfp5nBFFx90QfeY3pEJX5kZ_6ykjJ3U2Ae-VUzHax9adbN689el0OpTvhPAw49WK--GpIlmGNgqFhXqab8xDcvUC3P4IkKo38NirRT3Yg-JZ9QBZfs7Tqx46xLj2OEQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر ایران از اجرای مخفیانه حکم اعدام «تورات محمدی»، شهروند ۴۲ ساله افغانستان، در زندان مرکزی کرج خبر داده است. او با اتهام «جاسوسی» به اعدام محکوم شده بود، اما مشخص نیست دستگاه قضایی جمهوری اسلامی او را به جاسوسی برای کدام کشور یا نهاد متهم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78635" target="_blank">📅 16:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bnIr5gXMrTJJMowqbyPu6OwT1NvI0Mq55MzsYVEc_s1CR2kKgjKspaHPA9nC3VJsfCg_KyjNqeseMiSmvyoXvBUa4VZHH3Wfb7GYquOuaenuDFzXxAMAJkPhEZgTQyxtLMVozWcCTf4dLjBRLHgzhsALvSDfCbJvetlrquqwOjWLXALwlaChUo20ZVDIU0SoeDPEygwOMZIXYlMV-blulW69wu3Esj2imRh68-IlOSEpg3JVX-Oenk1uug73lU_l9r68Qkx8igKV3uyZNW0beOrs7sD7_U1QqbuW0r87CGOvVPdmIj_ROh04zwhzOOaIPARQ7-t2UHXgBqbJii-_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UTaOV8_6SbvMpR-5Qo1uu609ABHaCz5-rJm_pw9Vt5xbdu2VWqM-rSZAF-r9VcPoRw0HdQDkq8WqIpH6HNG3cChG6Cj_dBnDOI9CIgHza2l8LGmgnNgv6DM0CVo-oaBqygCwq2gqyshqQILgeKrV9X-un_CewAiVanTRBCP4ykeKGuYBMWDEAlsX14OWY79EoxlGGjWSS_Nd1LUHOGF5zhv_1LD4DRbrGjiI4_dZ5dPAq6KWGhYhreMYKkFFx0guI8HmUBxjRNzqMyzqs7_EcaJXyA_w8ptOT74r_MEKuAR4Oq5he9xGKPPrTx9G_nZkOmw1ii2RoCIpBw_Awr7n7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده در پی دریافت اطلاعاتی درباره احتمال حمله پهپادی جمهوری اسلامی، ۱۲ فروند بمب‌افکن بی‌۱ را از پایگاه هوایی فرفورد، متعلق به نیروی هوایی سلطنتی بریتانیا، خارج کرد.
وال‌استریت ژورنال علت خروج این بمب‌افکن‌ها را «نگرانی‌های امنیتی درباره طرح‌های احتمالی حمله به پایگاه» عنوان کرده بود.
دونالد ترامپ، رییس‌جمهوری آمریکا، دوشنبه تایید کرد بمب‌افکن‌ها به دلیل تهدید امنیتی جمهوری اسلامی از این پایگاه خارج شدند.
این در حالی است که مارکو روبیو، وزیر خارجه آمریکا، ساعاتی پیش‌تر این انتقال را بخشی از جابه‌جایی‌های معمول نیروی هوایی توصیف کرده و گفته بود ارتباط مستقیمی با تهدید ایران نداشته است.
@
VahidOOnLine
روزنامه نیویورک تایمز در گزارشی اختصاصی به نقل از مقام‌های آمریکایی و بریتانیایی نوشته است که آمریکا پس از دریافت اطلاعات جدید درباره احتمال حمله پهپادی که گفته می‌شود سپاه پاسداران آن را طراحی کرده بود، به‌طور ناگهانی هر ۱۲ فروند بمب‌افکن بی-۱ نیروی هوایی آمریکا را از پایگاه هوایی «آرای‌اف فیرفورد» در جنوب انگلیس خارج کرد.
نیویورک تایمز به نقل از این مقام ها که درخواست کرده اند ناشناس باقی بمانند نوشته:‌ «حمله احتمالی بخشی از یک طرح پیچیده و چندمرحله‌ای ایران برای هدف قرار دادن هواپیماهای آمریکایی و کشتن شماری از چندصد نیروی آمریکایی مستقر در این پایگاه بوده است. به گفته آنها، تمام بمب‌افکن‌های آمریکایی در آخر هفته از پایگاه خارج شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78633" target="_blank">📅 08:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aGw1WRA2a3KtjZaoF8k5aolX_aY9Q_Z0QDgnF48MSkbjSmGzh27iNaOiZciJEje43viOCPZx3159PCaAVw_hZ9zm4lFhVKIaTVdin0MkWmKG2vuGeRQ7dSuboVrY4RyeWQyZ4gmhgLoJJHrq2MXVFSyeJrALybLsW9PTDI48yFbDpS_N0GkmyMGYZSvt6SBYW8pnQYV5J9pNeglzhpsAVShOfr3_WjO9OtO5Oq3lj7OXXLZ9VLyNvpmhjbDwu6rXbNVFyG2j5rCu5j4ot9U_4wVVtABGtiUmpYJ44v8z4EPvgXpF9J2CPpvWvJhWhgAFh-IB0dGBTfCE0YOBb0iDVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E9fJeXgqz2rTsVTaboLknJwqcCyfbiZPn3zCdry7yeDKhcHyl7wIDWKpk-aSxqCLxeMKpwGW16CZ5ChpJlZ28gsgIMCnZ9vj-rUlKMaXWKGOp-rtND4Y8mvVcUWWtMmLaD51fY3x03niyfj8eZQQzgpLf5zvQg8xEOGKTpfFIGBDrqp-IjEymi0YXpuE5M4Wv4iaZRQCilj5b0Hz5sz6zyGIGn4-8GFLI_vf9veMOvWmrL-OinqrpE38kzcThjjz-lSO3hnn--PEauc49Mr02NjnQhXXBAImQsIuwdfuWOW4xSnzOXJOy3F8JxEU9SN90Sz3UCAWVuIuVnW2x0e6Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در پاسخ به سوال خبرنگاران درباره حادثه امنیتی در نزدیکی پایگاه هوایی فرفورد بریتانیا اعلام کرد که ایران با این پرونده مرتبط است.
ترامپ درباره دلیل خروج هواپیماهای این کشور از پایگاه فرفورد گفت: «ما با یک تهدید مواجه بودیم و اگر قرار باشد ما را تهدید کنند، هواپیماها را جابه‌جا می‌کنیم. این اقدام تا حدی مشکل را برطرف می‌کند.»
رییس‌جمهوری آمریکا تاکید کرد: «ما افرادی را که این تهدید را طراحی کرده‌اند می‌شناسیم و آنها خودشان را با دردسر بزرگی روبه‌رو کرده‌اند.»
@
VahidOOnLine
ترامپ روز دوشنبه ۱۳ مهر در کاخ سفید و در پاسخ به این پرسش که آیا احتمال می‌دهد ایران پهپادهای رزمی را به بریتانیا منتقل کرده باشد، گفت: «نمی‌توانم این را به شما بگویم، اما اگر چنین کرده باشند، بهای سنگینی خواهند پرداخت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78631" target="_blank">📅 00:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=aW3RydbdgndVcfFlNp_ddgrnHUOMoLcnDbsgTSBwR1K3d9kRaAwd6XR8iKwGdH178jbrzpTZhLwmsKfoTAwAgQklAaQTKLAjQYil0AxzmMAQdG2o2ev1g9tFOfJCY9xXHo9-n5PZsT2aDZ_5tFgR8tfzrfM5wbNHMZh2hwYSGffvq0rNpw8gh1N80eidCoAcEJjoanMusHXy10dpxDhRtXclmOD4sYPW79yCzoNoE24Z4NHa9Alepd0D9W93coAu07Zg6TfIrqkKTJZRB5EcL6d8tSpPEUjVGr8J4jZRKcWyzVZjw2BaytI1z--t_pU0gx2ksjVjcEH4TsKrJDPYBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=aW3RydbdgndVcfFlNp_ddgrnHUOMoLcnDbsgTSBwR1K3d9kRaAwd6XR8iKwGdH178jbrzpTZhLwmsKfoTAwAgQklAaQTKLAjQYil0AxzmMAQdG2o2ev1g9tFOfJCY9xXHo9-n5PZsT2aDZ_5tFgR8tfzrfM5wbNHMZh2hwYSGffvq0rNpw8gh1N80eidCoAcEJjoanMusHXy10dpxDhRtXclmOD4sYPW79yCzoNoE24Z4NHa9Alepd0D9W93coAu07Zg6TfIrqkKTJZRB5EcL6d8tSpPEUjVGr8J4jZRKcWyzVZjw2BaytI1z--t_pU0gx2ksjVjcEH4TsKrJDPYBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ترک کاخ سفید، در پاسخ به سوال خبرنگار فاکس‌نیوز گفت: «شخصا باور دارم که ایران مسئول حمله تروریستی فلای‌دبی بوده است».
این اظهارات در حالی مطرح شد که جی‌دی ونس، معاون رئیس‌جمهوری آمریکا در همین روز به خبرنگاران گفت که هنوز مدرک مستدلی بر دخالت جمهوری اسلامی ایران در این حمله دریافت نکرده است.
در پرواز دبی به تل‌آویو که روز چهارشنبه انجام شد، کمک‌خلبان با حمله به خلبان اصلی تلاش کرد که هواپیما را با تمام سرنشینان که اکثریت آن‌ها اسرائیلی بودند، ساقط کند. این اقدام با واکنش به‌موقع خلبان و مسافران، خنثی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78629" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaxRk1536FJUCP7phKCjJ--Jm1XLhFgYbFobHuFXLN5waWHRYEBuIsaUrrHe48HjNXYadLXvmLUVtSdd3Qw8b7SDegxKfOFV56VzRtxLxwHy0kly_yTnfcGsI5vt71yVPge-IT0nMmn0s4tos0ClmnxxNbDH9sQFlS2XGE7vqqqEoGPicaSPxj8QLQTyyZ53M_RV-cNKyt0rG7FrgrEnHqdW4VJtDKqobPeuF3cCW4aBrkeiqzJm6ut6h1B2Mgqx09FFrVRAmfaNwQjSjPiXwUzHxk1z5QfWRggK-yFf36x6BD3ddUmHpzKcJFJKse3zCSVwjAmqiDVRMAbvZPjygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید آنچه باعث افزایش قیمت گازوئیل شده دیگر ربطی به تنگهٔ هرمز ندارد، چرا که به گفتهٔ او، اکنون مقادیر بی‌سابقه‌ای نفت تقریباً به‌صورت روزانه از این آبراه خارج می‌شود.
دونالد ترامپ روز دوشنبه ۱۳ مهر با انتشار پیامی در شبکه اجتماعی خود، تروث‌سوشال، افزایش قیمت گازوئیل را به «پالایشگاه‌ها» مرتبط دانست و نوشت: «پالایشگاه‌های روسیه توسط اوکراین هدف قرار می‌گیرند و پالایشگاه‌های ما که در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط "دمکرات‌های احمق" تعطیل می‌شوند».
اشاره رئیس‌جمهور آمریکا به گزارش‌هایی است که در روزهای اخیر از افزایش میزان خروج نفت از تنگهٔ هرمز منتشر شده است.
شرکت کپلر، ناظر بر کشتیرانی جهانی، روز ۱۳ مهر گفت که داده‌هایش نشان می‌دهد صادرات نفت خاورمیانه، بدون احتساب ایران، طی هفته گذشته، با وجود حملات به کشتی‌ها در تنگهٔ هرمز، از سطح پیش از جنگ فراتر رفته است.
با وجود افزایش میزان خروج نفت از تنگهٔ هرمز، قیمت جهانی نفت در محدوده ۱۰۰ دلار در هر بشکه باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78628" target="_blank">📅 21:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد روز دوشنبه ۱۳ مهر یک پ نفتکش در حال گذر از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.
بر اساس این گزارش، این حمله موجب بروز آتش‌سوزی در موتورخانه کشتی شده که خدمه در حال اطفای آن بوده‌اند. با این حال، سازمان تجارت دریایی بریتانیا تایید کرد که تا کنون هیچ‌گونه تلفات جانی یا خسارت زیست‌محیطی گزارش نشده است. تحقیقات در این زمینه ادامه دارد و به سایر شناورهای عبوری توصیه شده است با احتیاط کامل در منطقه تردد کنند.
@
VahidOOnLine
پیش‌تر:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز دوشنبه ۱۳ مهر، با انتشار اطلاعیه‌های رسمی، وقوع سه حادثه امنیتی جداگانه را در آب‌های تنگه هرمز و در تاریخ‌های ۱۱ و ۱۲ مهر تایید کرد. پیشتر خبرگزاریهای فارس از هدف قرار گرفتن یک نفتکش در روز شنبه خبر داده بود و روز یکشنبه نیز ایرنا از شنیده شدن صدای انفجار در حوالی جزیره قشم خبر داده و احتمال هدف قرار دادن «شناورهای متخلف» را مطرح کرده بود.
بر اساس هشدارهای رسمی UKMTO، روز شنبه یک نفتکش حامل نفت خام حین تردد در تنگه هرمز، هدف اصابت یک پرتابه ناشناس قرار گرفته است. روز یکشنبه نیز دو شناور شامل یک نفتکش حمل گاز مایع (LPG) و یک نفتکش دیگر حامل نفت خام که از سمت خلیج فارس وارد شده و در حال گذر از تنگه هرمز بودند، توسط پرتابه‌های ناشناس مورد اصابت قرار گرفتند.
سازمان UKMTO ضمن آغاز تحقیقات رسمی درباره این حملات، به تمامی شناورهای تجاری و نفتکش‌ها توصیه کرده است با احتیاط کامل از این منطقه راهبردی عبور کرده و هرگونه فعالیت مشکوک را فورا گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78626" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sfHkAjugU-MRdR5rshmiw9cp4Vn_CqFioMQpLzVlT1-LRrruPWB67bf-UBDTso9d0AQhmDGNQ-c45Tnb4BMOa29bK26Yf4yTdWJqTTktHBzPEHv1pnl1fAZbxW-_QECg-1MpMwPmn4OjAt9qWSSQvL34IsryR3Hu72_FRrEyKaVYo4hXctLWzFrtYIhZbqY9vOB5_ja459abryokHCS_QCmaYhQ08LYik5vN50pOZdndbTEUirzv0oqTYrfHglGYkzOw4kB54ypOD6DI1ZFK0rd9oIGcDVmnm1YptVVd8ISEVy64DBeLga_NqpdU42RsJoHIbZ-Z0r2E0vhjFUD16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا رئیسی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴ را اعدام کرد
- علیرضا رئیسی سحرگاه روز دوشنبه ۱۳ مهرماه همراه با علیرضا سپاهی، از دیگر بازداشت‌شدگان اعتراضاتدی ۱۴۰۴، در زندان دستگرد اصفهان اعدام شد.
- روز گذشته برخی منابع خبری از فراخوانده شدن خانواده علیرضا رئیسی به زندان دستگرد اصفهان خبر داده و گفته بودند این زندانی سیاسی برای اجرای حکم اعدام به سلول انفرادی منتقل شده است.
- علیرضا رئیسی فرزند دختر عموی جاویدنام رامین رئیسی از کشته‌شدگان اعتراضات دی۴۰۴ است. رامین رئیسی ۱۹ دی‌ماه با شلیک مأموران حکومتی در جریان سرکوب اعتراضات کشته شد. پیکر وی را ۲۸ دی‌ماه به خانواده تحویل دادند که در «باغ رضوان» اصفهان به خاک سپرده شد.
- علیرضا رئیسی روز پس از خاکسپاری رامین رئیسی بازداشت شد. خانواده علیرضا تا ۲۰ روز پس از بازداشت فرزندشان هیچ خبری از او نداشتند. او طی آن سه هفته زیر شدیدترین شکنجه‌ها و فشارها برای اعتراف اجباری علیه خود قرار داشته و حتی تهدید به تزریق آمپول هوا شده بود.
- علیرضا رئیسی و علیرضا سپاهی از متهمان پرونده «میدان علیخانی» اصفهان هستند که به اعتراضات شامگاه ۱۸ دی مرتبط است و نهادهای امنیتی مدعی کشته شدن چهار بسیجی و مأمور یگان ویژه در جریان این اعتراضات شدند.
- در پرونده «میدان علیخانی» ۱۲ شهروند به اعدام محکوم شدند. با اعدام علیرضا رئیسی و علیرضا سپاهی، شمار اعدام‌شدگان متهمان پرونده «میدان علیخانی» به هفت تن رسیده است.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78625" target="_blank">📅 16:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78624">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MDhlLp42JL2pCMlsbiQD47qilP0vLlTOLzglNcWeSZPGfmR9O1NEEuDtGpMtQdcyZ7C-VKqPw0fB6WswISi1DhglEtqENRAXMSyBls3bIhyAchr4Z200yBgzsd3wZ-ady3Cn60GTIS_5-IDLCI35gqV2Q0pas9VDrU4qF2ZmHOTJQSeztAo5qXQRUpCsEbvn5V8FbEes2oSn_FUDqDR33gdXUtoPw9zIVUNGvd9XgzXzL4zTDSxgCcS3xkMJq4HyYfqydJ302DUgEQ7AgJ_IFXgeyB-5-LMwc1fx-oL-OW6Ij15i4vNKP0DunDcW53N9vm8TdRbIcAMTfdi0lHmitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا سپاهی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴  را اعدام کرد
- خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام علیرضا سپاهی بادجانی، معروف به علیرضا سپاهی، در سحرگاه روز دوشنبه ۱۳ مهرماه ۱۴۰۵ در زندان دستگرد اصفهان خبر داد.
- وکیل علیرضا سپاهی روز گذشته با اعلام خبر فراخوانده شدن خانواده علیرضا سپاهی برای ملاقات با او و انتقال این زندانی به سلول انفرادی، از خطر اجرای حکم اعدام وی خبر داده بود.
- علیرضا سپاهی پیش از اعدام و به صورت تلفنی با نامزدش عقد کرد. مهشاد کشانی، دانشجوی ۲۲ ساله ساکن اصفهان، نیز در اعتراضات دی۴۰۴ بازداشت و به پنج سال حبس تعزیری محکوم شده و در زندان زنان دولت آباد اصفهان محبوس است.
- علیرضا سپاهی قرار بود سحرگاه سه‌شنبه ششم امرداد ۱۴۰۵ به همراه ابوالفضل سپاهی بادجانی -پسرعمویش- و امیرحسین صفری حسین‌آبادی در ملک شهر اصفهان و در ملاء عام اعدام شود اما پیش از اجرای حکم به علت استرس دچار سکته قلبی شد و اجرای حکم اعدام او عقب افتاد.
+- علیرضا سپاهی چهارمین شهروند بازداشت‌شده در اعتراضات دی۴۰۴ است که طی هفته گذشته و پس از صدور بیانیه ۴۶ کشور در محکومیت اعدام‌ها در ایران، احکام اعدام آنها اجرا شده است. سیاوش جمشیدی خیرآبادی شنبه ۱۱ مهرماه در شهرکرد و علی همتی سیستانی و مجید نیک‌اندیش روز چهارشنبه هشتم مهرماه در مشهد اعدام شدند.
- پرونده معروف به پرونده «میدان علیخانی» به اعتراضات شامگاه ۱۸ دی ۱۴۰۴ مرتبط است که در محدوده میدان علیخانی، میان ملک‌شهر و کاوه اصفهان رخ داد. نهادهای امنیتی جمهوری اسلامی مدعی شدند در جریان این اعتراضات چهار نیروی بسیج و یگان ویژه کشته شدند.
- با اعدام علیرضا سپاهی، شش متهم پرونده «میدان علیخانی» اعدام شدند. عرفان اسفندیاری و گل‌محمد محمدی ۲۸ تیرماه در زندان اعدام شدند. ابوالفضل سپاهی و امیرحسین صفری در تاریخ ششم امرداد در «میدان علیخانی» در ملاء عام به دار آویخته شدند و قائم حسینی نیز ۲۹ امرداد در زندان مرکزی اصفهان (دستگرد) اعدام شد.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78624" target="_blank">📅 16:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i0yiCifzjKVE5MXknUlaBn2HoI7ZdIz3yep7_vLAZU52x33cYtVqPYoQHYD7vu3-5kobiL7Eu7RZmf4Rqf6bAj6Ek66YA_ZXQTaPftOKMuSDkF46CcEUHrvsqY7wOeSWE5oUHGDOzFf1SVfetOzkr_kPJHMdxT4ay9O_3A_GN-l1YRjQKJ5yKrEfmf4Tr4wdQEdciw6NweMm3Kx2p836Xc75Wpkpsef0ljIPF9TyzyG6rMAlEmbZZyS0SsKYQO9dngi0THKxGs5uiX5l6nNtJQ7ZxQDx4cOsakgqL0gCKdsJ6-nuauTWspvydKLVMYCJM54L_4JttTFCHTOCq-A1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت ایران در پی افشا شدن توقف کامل بارگیری نفت خام کناره‌گیری کرد
معاون ارتباطات و اطلاع رسانی دفتر رئیس‌جمهور ایران روز یکشنبه ۱۲ مهر اعلام کرد که استعفای محسن پاک‌نژاد، وزیر نفت، مورد پذیرش مسعود پزشکیان قرار گرفت.
مهدی طباطبایی در شبکه ایکس نوشت که حمید بورد به به عنوان سرپرست وزارت نفت منصوب شده است. بورد به عنوان معاون وزیر و مدیرعامل شرکت ملی نفت ایران فعالیت می‌کرد.
کناره‌گیری پاک‌نژاد از وزارت نفت در حالی رخ داده که محاصره دریایی ایالات متحده علیه ایران که از ۲۳ تیر ماه دور دوم آن آغاز شده است، صادرات نفت ایران را به‌شدت کاهش داده است.
وزیر خزانه‌داری آمریکا روز نهم مهر اعلام کرد: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت هفته گذشته در گفت‌وگو با شبکه فاکس‌نیوز اعلام کرد برآورد دولت آمریکا این است که حدود ۱۵ میلیون بشکه نفت ایران همچنان در مسیر تحویل، عمدتاً به چین، قرار دارد و پس از تحویل این محموله‌ها تهران «چیزی برای تجارت در برابر هیچ چیز دیگری» نخواهد داشت.
محسن پاک‌نژاد ساعتی پیش از استعفا، بر اساس ویدئویی که رسانه‌های ایران منتشر کردند، گفت درآمد ناشی از نفت فروخته شده «وصول» می‌شود و این روند ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/78623" target="_blank">📅 21:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7IZSOC7V6tDLERfjhNT74AMfOo5_PJmvd_HseW6rF1pGu1hKEvfAVhVLT1uTqsEZbO1seXuYb9AjiZRfb_0wLDeaij94zW4rA9njEsmCbCj4z-7VYAnw_7Rrx1X8dgwtbNGPo0OOB9KpBTprK2jE0xIocZP5fWNtd3UkO7l1K7pkNk_oM47XKUWwSYbM4mk4LMNPvWOSfzV5seSwBLNUp0SkZjaz189T9q8Rq3orPSn7cpH7Wa92t3_ABC8g1-BPGPVvssKmGp-fuYYJyQjyOXa94LYTIsBBvOulrYuNzOSyOSK-nSq4BSl4Yd6ilnRiGYPw74TWC1YUObVtDF6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز و طلا در یکشنبه ۱۲ مهر همچنان در مسیر صعودی قرار دارد. قیمت دلار آمریکا با افزایش نسبت به روز گذشته به ۲۷۳ هزار و ۱۰۰ تومان رسیده است.
دلار در ساعت ۱۵ روز گذشته ۲۶۸ هزار و ۵۰۰ تومان بود و به این ترتیب در کمتر از یک روز ۴ هزار و ۶۰۰ تومان، معادل حدود ۱.۷ درصد افزایش قیمت داشته است.
یورو نیز از ۳۰۲ هزار و ۲۰۰ تومان به ۳۰۷ هزار و ۴۰۰ تومان رسیده و پوند انگلیس با افزایش از ۳۵۲ هزار به ۳۵۸ هزار تومان معامله می‌شود. درهم امارات نیز به ۷۴ هزار و ۳۵۰ تومان، یوآن چین به ۴۰ هزار و ۸۴۰ تومان و لیر ترکیه به ۵ هزار و ۶۴۰ تومان رسیده‌اند. قیمت تتر نیز ۲۷۱ هزار و ۶۰۰ تومان اعلام شده است.
در بازار طلا و سکه نیز روند افزایش قیمت ادامه دارد. بر اساس نرخ‌های منتشرشده امروز، هر گرم طلای ۱۸ عیار حدود ۲۶ میلیون و ۳۸۵ هزار تومان و سکه امامی حدود ۲۷۳ میلیون و ۸۳۰ هزار تومان معامله می‌شود. سکه امامی نسبت به نرخ ۲۷۰ میلیون و ۹۰۰ هزار تومانی روز گذشته حدود ۲ میلیون و ۹۳۰ هزار تومان افزایش داشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/78622" target="_blank">📅 15:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlyEv7-zREkAkLfvvT4vxA9czbTr3UArsamlu2MEdRL7ZT2ktx7Nc_jTWBKLaJpVORX5X3ZTAElq4xFPNm3g8CEg3pm-jY2GeuI8YM8VLwC6EhPH6DM9UeDj3MMoB93s8TjKznc31X9H1O3Id3dUcjUA6-Mkc2hP8KCo2eghJZGywMc0g67X8oGQD70nC69mzk1jNWirIVWUn2YMla5JK4cz_EUanlozLQo8KEgTMiMT1ikQHQL9-CxGmZ5nhItHD0zIHD9ykbAyfLjFR8VDKyz6xOCYqGqZtBemB8X_D0j1IBBsm1fyXz-93p4OJjEar2p2P9uW8iygVKCgc4tHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۱۲ مهر با اشاره به دیدارهایش با مقام‌های کشورهای منطقه گفت این رایزنی‌ها «بسیار موثر، محترمانه و دوستانه» بوده است.
او افزود: «ما مسیر جدیدی برای ایجاد اعتماد میان کشورهای همسایه و جمهوری اسلامی ایران آغاز کرده‌ایم و به‌خصوص در حوزه خلیج فارس، این مسیر را به خوبی طی می‌کنیم.»
وزیر امور خارجه جمهوری اسلامی همچنین گفت کشورهای حوزه خلیج فارس در این روند با ایران همراه هستند و به گفته او، «اراده مشترکی برای ایجاد صلح، ثبات و امنیت در منطقه خلیج فارس، با مشارکت خود کشورهای منطقه، شکل گرفته است که اکنون به‌طور جدی دنبال می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78621" target="_blank">📅 15:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AiMh9nAhBKWmLxr3ZeFB6A8u9ybyYd1riPKkgXgpMqeXnLUn0PoETe30nb_vOyxo7V_XAPFFRjGyA5DeJgdqMrFEhGI2xoNrQ3MDRrBUKL0dlsw3H-OXUZGkT2JxsYeubpC7SfCLPHsQ1ItlprA2HTy7tW6E_4ex6TgaNELoIncwKxS1M4BlQMHITCatU1VJ7HXKdXeYldbEf-sRYnZf3LKlbpQgf6mQLjbUa2a0oU6pV43KpfMrVHkEswH2fbKNTuX3FEJjMsXFLik-pqFV5X8K7cxZq4jwyjhhu517yrVr4Sj94Gw17o68SbKx4wAYk-MGSbZHKmPNBCOqjBepvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=BNc_QdYohEBES_mXmtta5f-Hlcpq80i-2PbX1Au6osg8v1BoMiQamHH6ZRpjU0cKiYtcJDFnGnUy-2VS3wQlFm6vdna8AvegdOnVkwqn1EXIiy8nZ7dBGHRUdPulMUKol6LzJuf3h-McQrAVOm62RRbgCL37yDjFbHFERm2OCbR1aKDKcT8kW-K1wS-TwLwCNvju4OUW1qXmHm6rm7sFQSKHSOwhTHfjCUo18fch4JYkWkW5KMhIuM7p2KL_IqoorQJA0t5moNR2x00418OGr0_VBI5bOX87-ATcB3gxFgYHw0ecFjId-igMBXqKFSY1ggkEYnE7RemU41Y_0B0UCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=BNc_QdYohEBES_mXmtta5f-Hlcpq80i-2PbX1Au6osg8v1BoMiQamHH6ZRpjU0cKiYtcJDFnGnUy-2VS3wQlFm6vdna8AvegdOnVkwqn1EXIiy8nZ7dBGHRUdPulMUKol6LzJuf3h-McQrAVOm62RRbgCL37yDjFbHFERm2OCbR1aKDKcT8kW-K1wS-TwLwCNvju4OUW1qXmHm6rm7sFQSKHSOwhTHfjCUo18fch4JYkWkW5KMhIuM7p2KL_IqoorQJA0t5moNR2x00418OGr0_VBI5bOX87-ATcB3gxFgYHw0ecFjId-igMBXqKFSY1ggkEYnE7RemU41Y_0B0UCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز شنبه، با اشاره به تحولات جاری میان تهران و واشنگتن به خبرنگاران اعلام کرد که به‌زودی درباره ایران تصمیم‌گیری خواهد کرد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه «ایران درهم کوبیده شده است» گفت: «تصمیمی است که درباره ایران خواهم گرفت. تنها مسئله این است که یا از راه آسان خواهد بود یا از راه سخت. ما این موضوع را یا از راه آسان حل می‌کنیم یا از راه سخت.» او در ادامه افزود: «ضمنا همان‌طور که می‌دانید، ایران عملا از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.»
@
VahidOOnLine
پیت هگست، وزیر دفاع آمریکا، روز شنبه، ۱۱ مهرماه، از پاسخ به سوال‌ها درباره اعزام ناو جدید خودداری، اما تأکید کرد که رئیس جمهور آمریکا «مصمم است» از دستیابی حکومت ایران به سلاح هسته‌ای جلوگیری کند.
هگست که روز شنبه با خبرنگاران سخن می‌گفت از پاسخ صریح به این پرسش که آیا جنگ با ایران تا پایان سال جاری میلادی، سه ماه دیگر، به سرانجام خواهد رسید خودداری کرد و تصمیم در این باره را با دونالد ترامپ دانست.
روز شنبه، چند رسانهٔ خبری آمریکا گزارش دادند که پنتاگون در حال اعزام ناوگروه ناو هواپیمابر «تئودور روزولت» و یک گروه آبی‌ـ‌خاکی تفنگداران دریایی به خاورمیانه است؛ اقدامی که در صورت اجرا شمار ناوهای هواپیمابر آمریکا در منطقه را به سه فروند می‌رساند.
وال‌استریت جورنال به نقل از مقام‌های آمریکایی بدون ذکر نام آنها نوشت این اعزام، همراه با گروه آبی‌ـ‌خاکی «ماکین آیلند»، بین ۹ تا ۱۰ هزار نیروی نظامی دیگر به منطقه می‌افزاید. به نوشته این روزنامه، «تئودور روزولت» به ناوهای هواپیمابر «جرج اچ. دبلیو. بوش» و «جرج واشینگتن» خواهد پیوست که در منطقه حضور دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78619" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/coA0MATqGNqYgxlsvEW8Kkb8pUO5wWOLQPaOGlCaFvM6aNTZZ2vTkM6YLd6-7GwjdN-tYgdM6_GBtP4PfG3vWCdCKrBRWAAVcOpR2xbk7xTE4FPxIFUUpXonxf-RjHyyoTATJIyb-Dzw0_PHytd-PzHTT9H_T3gO_MiBfCx351PZtAtgQe1DME2Bdr0oj2jmNNTOSfRJp_4kgsaJN3dheztWLGWD6mBMHKSt_ZTN7-n85GtkX51Bq6ztNx3w3sPevwyIILBzG9fjz3kEv9zrKqRVW5Im25cdT-ICe49trJOoGs0X7x6U2LGjAoprM86Cu4OGREPhkLt3vah_0QjZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FIUjCgdSpTmP1bzTIcdJEJSKIQsT941FFADPWjSMhbNUNr7hlS7JcUNeneizGHpKnNHQM8twNt2u0_CCzILq5FfHWMYaoZVpPWmS7zgcPpSh8zjn9v_fBgSdU2Mp3TJBDOvWMEX5WiTzxewA1f2tvtgZcDriB7MrcW8wQC9jYOlhpUrudOVwQrFM4C7vpWWUs_EpNFjunLhYdo_e2zKjvRenSngBTwLn_ledWe-Stw9DWwJzl0qicQ8nEvlw5uThSqihtJAZZrpACE1e8EFxXnzsuiovN6EeHUuThyDr7q5IHoOMBpygyhCUBB5-8dgYQUhDqFSHqIkSIlI-yWpyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0XYKM3WVqTebZ59FoPl7JKaHCZE2R8e15ehT06fvTGELRbTZ3XpQRpazpar5nueFAnni9ZEokA0gYgbRqdkJC4lgB9Rq5EI7P4J19CkIRXezoCfGrE_uM6oGGqk6oKdawjLHw-ziS8bgE0pAkaC80EwPniG2CmH4jiu9H0LXoP_-1qKpJygALvyQLFEEgc5oAaG4K0A7XsKFeQdV77MIbDG11PxptQZrV452TRAHn6lwvih2VkfOsaxjKWb-S26Y64LMDHtxzjXy2WvbeSuNhH3snhLxdJOkIw4ZOPG-3DlDGoyWGdL6IpXVM6FJ5ZWMP56svZVbp9ttEjvxeFUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YPcJKqToXd11f3ZkpGkLgLiQ7lJyO_YDGKX-SxLpIhhK9BYFU_Gmijj-gElyfMx2U5MQ6dvcGMqvGdygetvA28i9lPZDg07ZCDVpCOWZczfW6gdxXSx-sbLGh5hTz0GJeMCmaBC9-_bKX1DyKy45amPOnNASk-_rrDqoGa3dNgF-BEL0g0jmnAJ1pTOS3u_MORtc8sE5ykPsVvPhPbpY3h1_5LXXR0k2rqruzDDPfAJGEDudYWfNA4EgvUCPf41yoJw00-F3p3kEaJEM4cqSkahBDmuT5KEvRxBcqc06dh5X8XU0utXMQG2jpuU5m03Pp2f9_LPfYA5b7pdu4A5Brw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
صدور و تایید احکام اعدام برای سه زن در پرونده‌هایی با اتهامات امنیتی، نگرانی‌ها درباره استفاده گسترده‌تر از مجازات اعدام علیه بازداشت‌شدگان و متهمان پرونده‌های سیاسی و امنیتی را افزایش داده است.
🔸
محبوبه شعبانی در پرونده‌ای به اعدام محکوم شده که امدادرسانی و انتقال معترضان مجروح از جمله اقدامات منتسب به اوست. مژده هاشمی بازرگانی، که حکم اعدامش در دیوان عالی کشور تأیید شده، از شکنجه، اعتراف اجباری و محرومیت از وکیل انتخابی سخن گفته است. سودا ابراهیمی شمس‌آبادی نیز با اتهاماتی از جمله فعالیت رسانه‌ای و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور به اعدام محکوم شده است.
🔸
هر سه زن با خطر اجرای حکم اعدام روبه‌رو هستند.
@IranRights</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78615" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jayb0QWZVy7LA1grIyvV_XmgFBrzJ9AzUAJqHTkuqpAia14fC89oXTiN5__IqdtBlyDmoYrqbgHIMOYJN0onSahkiYwoOC7UcdQrB3mhbz8ODbXeu7wz_u89FYy6YTnn7BpdkPa0_I1KzkSum91ss2XZDKWg2CqMIwkj0bZBqsXgRhizJJpcikPvrdTWYKTOuO2Uv0cekdoe7nzyqoKMh41qrR687Krwz8GjET3auyDZiWCKq4koCxLpEAFngHtIXkZYHyBLvYAj4E3K-t2saeJr83Nps7sTe_Oel75Ujpp3Nc-s7WGBUTGVSTxvKSbJU8VfEH7JANcJQ10n-FiURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس روز شنبه یازدهم مهر از شنیده شدن صدای انفجار در تنگه هرمز و هدف گرفته شدن یک کشتی تجاری در مسیر عمان خبر داد.
فارس مدعی شد، نفتکش «اور وینست» که تحت اسکورت آمریکا قرار دارد، هنگام ورود به تنگه هرمز سامانه رهگیری خود را خاموش کرده بود. این خبرگزاری دولتی نوشت، این دومین هدف‌گیری یک نفتکش در تنگه هرمز در روز شنبه است.
این خبر پس از آن منتشر شد که خبرگزاری مهر ساعتی پیش از شنیده شدن صدای انفجارهایی از سمت دریا در جزیره قشم خبر داده بود و احتمال ارتباط این صداها با شلیک به «کشتی‌های متخلف در تنگه هرمز» را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78614" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwl431GSMba-MHDx8oIImslW3zyEbpXRSHtGAJk_zBOwaeTsYYHf5gPp_l84qiNVcyJx4TnN7wH9HbMPyiVyB7wzgvyFaiRFUQ9Y7BAWSqMRZMfzMyjFreCDUT222BltSDwfQD456huZPNHsEG8zKXEmkzs5y2OTeCgbpbX1lcYTSQeq9mtvoBG6UNwEJ0EmoSBONrryqD1qMyN1DU6QDsaTDGuZU9xnA32M2fPmWz56CPJMNNiu7kImtiCPhy8I48SaYFvnVdUYsSQKzOJBCZlyuYEqxJcWvadkGPcyjCTI0_d_QZK46pJauYLahzYSiGCaFnDTn_Y0sZqzmIHHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌هایی از شنیده‌شدن صدای چند انفجار در جزیره قشم در عصر شنبه ۱۱ مهرماه، خبرگزاری مهر نوشت این صداها مرتبط با اقداماتی در خلیج فارس و تنگه هرمز است.
این خبرگزاری بدون استناد به منابع رسمی نوشت «هیچ اصابت یا حادثه امنیتی در پهنه سرزمینی جزیره» رخ نداده است.
خبرگزاری مهر در عین حال این «احتمال» را مطرح کرد که صداهای انفجار شاید به «شلیک به کشتی‌ها» در تنگه هرمز مرتبط باشد.
این در حالی است که همزمان، تصاویر متعدد و گزارش‌هایی در شبکه‌های اجتماعی منتشر شده که یک قطعه بزرگ و استوانه‌ای‌شکل را در محدوده‌ای شهری در قشم نشان می‌دهد که ظاهر آن به بخشی از یک پرتابه نظامی-دفاعی شبیه است.
گزارش‌های تأییدنشدهٔ دیگری در شبکه‌های اجتماعی نیز حاکی است که پیش از سقوط این قطعه، صدای عملیات پدافندی و چند انفجار در قشم به گوش رسیده است.
مقام‌های رسمی تاکنون توضیحی دربارهٔ تصاویر منتشرشده و این حادثه در قشم ارائه نکرده‌اند و رادیوفردا نمی‌تواند جزئیات گزارش‌های منتشرشده را به‌طور مستقل تأیید کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78613" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uCKE1Q5Z0OKFzM70ZZIdgV38yKRjN60FyCFQUO3jEi-dgYdR6Q3Hof4iXvj-H457-YkbS8O5UIhupm_f8B_OaGL73KbIQr28TMzCwClgEVEPr1cJc7abMGQ6--V-ahinNH-qFZORQ5hWpB8P98nSOLew_c0kNsmi8OTnN4lSVGBeW9csMR0yFwbY1POXhvwS9RH5AymBNzFh_4LgPSYRIHP9HvjgHnFdrgUxPJRwoBd1bQ-Fx_j210g0WtrQhxEXcB6e2ghuzskph3qqsAuvLlAfDJPcky7loQQF80WPeIxY3h_mcwjaZYJgbUgl4z_Or3s_9ocWQlXjj-V2Jh2FdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از قشم  حدود ساعت ۱۶:۳۰:  صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم  همین الان قشم موشک شلیک کردن  16:34 دقیقه   وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن صداش خیلی وحشتناک بود معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد…</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/78612" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ0koY1jSBZDC7bwLiZ6uPysIzQx0RQW_7EQoysV5K_G2gKg48Vs6WTtegxzAeKpzjwjY9TSN6ODLoflcIqUNrfdFuj80Sn9wVeUdu7DINjyMMJ2va71KzdwmshJMN5Bqci1BQOe-NJpKgQWaN_Bt9HNH_6YpXN1Qu7pWqvSO0b9uaS-GEGPvaUyTtUcbW0l9iZXh5Y6gO_Q0Uod9ykvWddrSOUq1A5KS8EvnZr-7rPsW11YeeiqzY34-0ogeu726hNqej88g8KlrUUClI-gyPEDk9-ytAbpwTPHkClvzzea22_Uv1NRuKZVCgFiS_Nye4l3rtMCOewUe12O3ZOYbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند کاهش ارزش پول ملی ایران روز شنبه ۱۱ مهر ادامه یافت و بهای دلار آمریکا در بازار آزاد برای نخستین بار از مرز ۲۷۰ هزار تومان عبور کرد.
بر اساس نرخ‌های اعلام‌شده در ظهر شنبه، قیمت فروش دلار به حدود ۲۷۱ هزار تومان و یورو به بیش از ۳۰۵ هزار تومان رسید.
این در حالی است که روز پنج‌شنبه قیمت دلار در بازار آزاد حدود ۲۵۸ هزار تومان گزارش شده بود؛ به این ترتیب بهای دلار در فاصله دو روز بیش از ۱۳ هزار تومان، معادل حدود پنج درصد، افزایش یافته است.
افزایش قیمت ارزهای خارجی در حالی ادامه دارد که بانک مرکزی جمهوری اسلامی روز چهارشنبه از برنامه‌ریزی برای عرضهٔ دو میلیارد دلار اسکناس به بازار خبر داده بود.
قوه قضاییه نیز از برخورد با کانال‌ها و صفحاتی که آن‌ها را عامل «قیمت‌گذاری کاذب ارز» می‌خواند، خبر داده است.
اقتصاد ایران همزمان زیر فشار جنگ با آمریکا، تحریم‌ها و محدودیت‌های فزاینده بر تجارت خارجی ناشی از محاصره دریایی قرار دارد.
ارزش پول ملی ایران، از ۲۳ تیر، زمان آغاز محاصره دریایی آمریکا علیه ایران، تاکنون بیش از ۳۱ درصد کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78611" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSSABDx9ryIva55dsmyPDhKy2epeAjnx9tTepSsvlRaJMwL6GAn9-oKSynySd7VRW0UJGsN1Dke4l_W5-It3vFdWg4QeqX2JN-R2sE6lVdduPGRBdmEPEPBihlfJt0QyiFx9fGU1G4OG5kIEwU0gqlGP6YJ-SfmU-hv6RjyIw8o8HEd9o1nMjMSLrvDGx7OJXG-sKCCplzrCUOUAoYGXzJOsy7jPqYXkBZgtkS9NrhJupL52P8NFaRSfTgWLnTGmWEbLOeBKKssTSM1ltDHXQorIIgWtiy_Lhq946OaehX7wOumvnFN32CFZBJCFXU08OpAPLtWuTeS5N8ZtRsvmFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با رسانه آکسیوس،‌ با تاکید بر تاثیربخشی محاصره دریایی ایران اعلام کرد، ایران برای نخستین بار از زمان آغاز صادرات نفت، در هفته جاری هیچ نفتی برای بارگیری و انتقال از طریق دریا نخواهد داشت.
او همچنین با اشاره به کم اثر شدن نفود نیروهای مسلح جمهوری اسلامی در تنگه هرمز افزود، آمریکا عبور ۱.۱ میلیارد بشکه نفت از را از این آبراهه تسهیل کرده است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال منزوی کردن ایران «به شکلی بی‌سابقه» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78610" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw-j6DUUCgKsyt6iYfxGi9l_vrUMp_0jwbgedD5S7F11HGVY-QlQVPGSgKPyUKkDz0M_ICJSzR2hqIlroHAkOJddQGmVmQxACDUaNXXo3IW4qGa8zgGb7J6Q0btG_N9ooN6adi5HAAykUrYT4NzJCRfrC2LmqvnXIozFt2tZsHolHhP9zsKvTu2SyO0BbO4VSBpaGBwx3-BFkFIpQxY9hJeLyl0JzrQDdmEQTJSjX8sBIuP5s-gR8Pi69k9vwuHJ4oFh-wSKRHi9W2FYrVGzMKQK-hOac6upcdBhMUwsKdlFCMOVI6jhVoAGTCSO-GlJTAxpDlA_9mbAIkk7HIPOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا دو تبعه ایران را به برنامه‌ریزی برای حمله‌ای تروریستی علیه جامعه یهودیان منچستر متهم کرده است.
پلیس بریتانیا روز جمعه ۱۰ مهر ۱۴۰۵ این دو نفر را «سلام احمدیان»، ۳۶ ساله و ساکن لیورپول، و «رحمان صالحی»، ۳۴ ساله و ساکن سالفورد، معرفی کرد.
این دو نفر روز یکشنبه ۲۹ شهریور در منچستر بازداشت شدند و روز جمعه به اتهام انجام اقداماتی در راستای تدارک عملیات تروریستی تفهیم اتهام شدند.
قرار است احمدیان و صالحی روز شنبه ۱۱ مهر ۱۴۰۵ در دادگاه حاضر شوند.
پلیس می‌گوید این دو نفر برای پیشبرد توطئه ادعایی خود با فرد سومی در خارج از بریتانیا، که احتمالا در ایران حضور دارد، در تماس بوده‌اند.
به گفته پلیس، احمدیان و صالحی از طریق پیام‌رسان‌های رمزگذاری‌شده با این فرد درباره تهیه قطعات لازم برای ساخت یک بمب دست‌ساز گفت‌وگو کرده‌اند.
این دو نفر همچنین متهم شده‌اند که فایل‌های ویدیویی آموزش ساخت و مونتاژ بمب دریافت کرده، مایعات و تجهیزات مورد نیاز را تهیه کرده و برای شناسایی و بررسی اهداف احتمالی حمله از اینترنت استفاده کرده‌اند.
«ویکی ایوانز»، معاون دستیار کمیسر و هماهنگ‌کننده ارشد پلیس مبارزه با تروریسم بریتانیا، گفت این بازداشت‌ها نتیجه تحقیقات مشترک پلیس مبارزه با تروریسم و نهادهای امنیتی بوده و به خنثی‌شدن توطئه‌ای علیه جامعه یهودیان منچستر منجر شده است.
او اتهام‌های مطرح‌شده در این پرونده را «بسیار جدی» توصیف کرد.
این توطئه ادعایی هم‌زمان با اعیاد مقدس یهودیان، سالگرد حمله تروریستی سال گذشته به کنیسه «هیتون‌ پارک» و افزایش گزارش‌ها درباره حوادث یهو‌دستیزانه در سراسر بریتانیا خنثی شده است.
دولت بریتانیا دو روز پیش از اعلام این اتهام‌ها، جمهوری اسلامی را به دست داشتن در تلاش برای خرابکاری در پایگاه نیروی هوایی سلطنتی «فیرفورد» متهم کرده بود.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، روز چهارشنبه ۸ مهر ۱۴۰۵ در پاسخ به پرسشی درباره نقش ادعایی جمهوری اسلامی در حادثه امنیتی اطراف این پایگاه گفت واشینگتن در حال بررسی موضوع است.
پایگاه فیرفورد پیشتر در اختیار نیروهای آمریکایی برای انجام حملات علیه مواضع جمهوری اسلامی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78609" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qnC_DlOmGKbBrqJmBecgsqQJxTFhKIe1SfGgUP3Vuqrg_UhaFTLTnBCgFPquYKoQMfpoCZ1-5SFZ4CZJUuw8liIEKvIrozvYNmvhrXVyHm0wnvSKQEkQU7zh2ODCawmFC9jrods1SxMYB_ReI8vKv-R-s_GVbTp4jaF49LuLYtPsx0DBjxuK8ZVW3I4s1duPkzeEwazRvFjeF_ZIyE7WeLes5ca8AIIv9CAmC5xvqXMHcivecDRIjD3f27nS9Zx3_xZBZtqKwfDUv9lWZXhoD5o7PYt50EMeEgdjqF9A4jKrVNpHj79DLFsHoCxHOxAVTO_0xR8UsSsprrklIrlSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fkWYxuQDJl_DU7f182rYBjjiZ68oZfMLpwB99aJd3soNRFo5HI6De22j2IqrsYQNYcGYc45Lelu3j9qK2_MeDS8KFfxxtt6Ts1O3Rj5_IIQ87oC2lAZodz4mASNLj1w1e7ERIV02qlPGLoPO0C2XVw5I64cpWTc3Lowudfrz-DGMwa8mtQYqRNNI4c_28SGjHC_XUhORgcKBxDQZvSY4hNWfp6n7J25FjELksH9Gf-VVinon5tcpPIVfRSAc-XjbgA2X8nzVB7i_z3JmR1rf6sBzrlWqPYh7Nxrorl8EW3WdGSyKznIobUfngabqX5KjkSBnZVagJUNBzDhQTcuqag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: جمهوری اسلامی سقوط خواهد کرد و «روز آزادی» مردم ایران فرا خواهد رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مصاحبه‌ای اختصاصی با روزنامه دیلی‌میل که روز شنبه ۱۱ مهر منتشر شد، گفت که به اعتقاد او جمهوری اسلامی «سقوط خواهد کرد» و خطاب به مخالفان حکومت ایران گفت: «ایمان خود را از دست ندهید، روز آزادی شما فرا خواهد رسید.»
نتانیاهو در این گفتگو مدعی شد حکومت جمهوری اسلامی ایران در شرایط کنونی «بسیار ضعیف» شده و گفت محاصره آمریکا به رهبری دونالد ترامپ، سپاه پاسداران را به‌شدت تضعیف کرده است. او در عین حال تاکید کرد که سقوط حکومت ممکن است زمان ببرد.
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت اسرائیل با همکاری آمریکا، مانع دستیابی ایران به سلاح هسته‌ای شده است. نتانیاهو گفت: «اگر ایران اکنون سلاح هسته‌ای داشت، چه اتفاقی می‌افتاد؟» و افزود که جمهوری اسلامی همزمان در حال توسعه موشک‌های دوربرد است.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتقاد از سیاست دولت‌های غربی و به‌ویژه بریتانیا گفت آنها انتقادهای خود را بر اسرائیل متمرکز کرده‌اند، در حالی که به گفته او، تهدید جمهوری اسلامی و نیروهای نیابتی آن را نادیده می‌گیرند.
او خطاب به معترضان در بریتانیا پرسید چرا به جای اسرائیل، مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنند.
نتانیاهو گفت: «چیزی که به مردم بریتانیا می‌گویم این است: کجا هستید؟ کسانی که علیه ما اعتراض می‌کنند، چرا مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنید؟ چرا تمام زهر دولت بریتانیا متوجه آنها نمی‌شود؟»
او افزود: «چرا علیه جمهوری اسلامی جهت‌گیری نمی‌شود؟ چرا علیه نیروهای نیابتی آن نیست؟»
نخست‌وزیر اسرائیل همچنین دولت‌های غربی را متهم کرد که تهدید جمهوری اسلامی را به رسمیت نمی‌شناسند و گفت: «این حکومتی در ایران است که ده‌ها هزار نفر از شهروندان خود را کشته یا مجروح کرده است.»
او افزود جمهوری اسلامی اقتصاد غرب، منابع انرژی و آبراه‌های بین‌المللی را «خفه» می‌کند اما موج خشمی را که علیه اسرائیل وجود دارد، متوجه جمهوری اسلامی نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78607" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmrxPDfEcf4h5m1BALgCJfLpd9TQ621viSx_XJOwcdE87hGI0klQpfM40UgJqB4O430Gw5ZzApmVUy-9JHcE27wZCohThywcepyLbxudAm8J5NX1HXqaVVLJO8Ohc21rRQSIlSb2Fpr7mSAx2JAJsqyKYQr1i-E-z4io4kkJo9_h6bMkSxEvEIi_dfvfqmQjSe-9DsVimu3s68xQfNtPsgj1LUK4r1wPMraWZ1Z9RHW_byd1MGbtOG2dsKNuITfKsW_7EHBEoGCpT2kcLgg9NebgikPeTGmzsaw7IbQZU4g2Bk1u-37t6B_nN-ds9eu8ejOu5qIWcNnkLdIbjvJgXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تیراندازی مقابل ساختمان دادگستری مهاباد در روز شنبه ۱۱ مهر، یک نفر کشته و چهار نفر زخمی شدند.
امیررضا رسولیان، فرمانده انتظامی مهاباد، اعلام کردە  این تیراندازی مقابل در دادگستری این شهرستان رخ داده و در جریان آن یک نفر کشتە  و چهار نفر زخمی شده‌اند.
یک منبع مطلع به ایران‌وایر گفت فرد مهاجم که چند سال پیش فرزندش را از دست داده اعضای خانواده فردی را که او مسئول قتل فرزندش می‌دانسته و در حال حاضر به عنوان متهم در زندان تحمل حبس می‌کند هدف تیراندازی قرار داده است.
به گفته این منبع، مهاجم پس از تیراندازی توسط مأموران انتظامی در محل بازداشت شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78606" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EROLONvPqan0x7pUuCIeY-YIqCpzeVKJI5FfmVYD1nD17CSBa3Y23IHuEGP_5NGzXv67HhyhFrp9C-IK6ZqnQUHghl-1AIAUT1C8FpUt0UMX-DxjgJsvL6I9I4-bY7ov8bXVFg1ctAsEb15SiB90gVpq1NTkaoIjQ0wQ5Y5nhjAeVJOWvF5ZvZ0SNWjpuhRXP1GaAHEuTG5qohoiqIX6wg7l62Gan5596156Vi3f6ylQIO17uY0nq8l7WmYQzRNlPdrpqjlXfJS9QDdTMgDFSLZ-bva_HSMf8dySJlKhZ0jatRP3wngQN7hcXbHHZM9gf1EJL04g9aZVI1YPmR93Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز شنبه ۱۱ مهر از بازداشت ۳۱ نفر در شهرستان سیرجان در استان کرمان خبر داد و آنها را اعضای چهار «شبکه سازمان‌یافته خرابکاری خیابانی» معرفی کرد.
این وزارتخانه مدتی شد افراد بازداشت‌شده برای شرکت در «فراخوان‌های سراسری» سازماندهی شده و در حال تهیه کوکتل مولوتف و ابزار تخریب دوربین‌های شهری بوده‌اند.
وزارت اطلاعات همچنین این افراد را به دست داشتن در «آتش‌زدن فرمانداری، تخریب بانک‌ها و ساختمان‌های دولتی و حمله به مقر پلیس» در جریان رویدادهای دی‌ماه ۱۴۰۴ متهم کرد؛ رویدادهایی که در اطلاعیه این وزارتخانه از آنها با عنوان «کودتا» یاد شده است.
در این اطلاعیه جزئیاتی درباره هویت بازداشت‌شدگان یا مستندات مربوط به اتهام‌های مطرح‌شده ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78605" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGXnOnHohKOwGbRiA8IuJctEbtZ95J6No7HsCfvBLvg1dcFIiUxbAeqR27kiGRKpqvoKTvgRHhBFcSO-Feat8TwFkHBsQ51W7gShlI8ANjWDhAEQllQaAHUJuSp_VEpj2n6AXNO7g_wX5g-BfNsDbAXCBbRZ-sbG5i4Fwgrp4qNhQqAV02B7lrPUgPerQAupS7_XTl43Bnst4kUgyxD_9_-_OD5UMavHjGLH0QFlK5TtZV-SgFniqEeOE9WlrRQnb7BQQq3gRrJQgq4iIbFQRMhXML38wSV5BRXHpglzhvQyDXN-YOpS7Edge2SGfS15NCiKLrNaBU5GkM6rTbMLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام «سیاوش جمشیدی خیرآبادی»، از بازداشت‌شدگان اعتراضات سراسری دی۱۴۰۴، در بامداد شنبه ۱۱مهر۱۴۰۵ خبر داد.
قوه قضاییه همچنین ادعا کرده است که جمشیدی خیرآبادی شامگاه ۱۸ دی ۱۴۰۴ در خیابان ناصرخسرو شهرکرد به‌سوی ماموران تیراندازی کرده و سپس از محل گریخته است. براساس این روایت، او دو روز بعد، ۲۰ دی ۱۴۰۴، درحالی‌که یک قبضه سلاح کمری همراه داشت، بازداشت شد.
در اطلاعیه قوه قضاییه آمده است که حکم اعدام این معترض پس از تایید در دیوان عالی کشور اجرا شد. بااین‌حال، در این اطلاعیه توضیحی درباره زمان برگزاری دادگاه، روند دادرسی و دسترسی او به وکیل منتخب ارایه نشده است.
مقامات جمهوری اسلامی معترضان دی‌ماه ۱۴۰۴ را «کودتاگر» خوانده و آن‌ها را به ارتباط با آمریکا و اسراییل و تلاش برای ایجاد ناامنی متهم می‌کنند.
«مسعود پزشکیان»، رییس‌ دولت جمهوری اسلامی، نیز در سخنرانی اخیر خود در مجمع عمومی سازمان ملل مدعی شد که مردم ایران طی هفت ماه گذشته برای «دفاع از ایران» در خیابان‌ها حضور داشته‌اند.
او معترضان را افرادی توصیف کرد که به ادعای او، آمریکا و اسرائیل آن‌ها را «تهییج» و مسلح کرده بودند تا در داخل کشور ناامنی ایجاد کنند.
صدور و اجرای بسیاری از احکام سنگین علیه معترضان دی ماه از جمله احکام اعدام ذیل قوانین «تشدید مجازات جاسوسی» صورت می‌گیرد که از منظر حقوق‌دانان و فعالان حقوق بشر شامل موارد جدی‌ نقض حقوق متهم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78604" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پیام‌های دریافتی از قشم
حدود ساعت ۱۶:۳۰:
صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم
همین الان قشم موشک شلیک کردن
16:34 دقیقه
وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن
صداش خیلی وحشتناک بود
معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد بوددددد
قشم همین الان یه صدایی شد
سلام وحید جان چند دقیقه پیش یک موشک به سمت تنگه شلیک شد.
سلام وحید
دور و ور ساعت ۴:۳۰ جنگنده رد شد
سلام ساعت چهارو نیم بعداز ظهر امروز قشم  صدای جنگنده امد خیلی وحشتناک بود
[این پیام متفاوت هم بود که نمی‌د.ونم چقدر درسته. بعد از یک ساعت معلوم نشد صدای چی بود.]
قشم پدافند بالا نریمان و زدن
وحید
خیلی شدید بود صدا ها
معلوم نبود چی بود
رادار تازه ۳ روز بود درست کرده بودن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78603" target="_blank">📅 17:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78602">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=P3hY-K47P3knSujYXbmEa4Rrgljr-GENhhsimFI5fXxtERAD-Mm5LT3ppcPOiDiHNfdjHcY2KqMloetHuHDjfg1EkodKjq483E4RvgM6F5xIhRY5tgQnN65T5nR-2DahcEgPqfV-h4NYxuzv9lLQKLqlyQC348bPLoYPloITxDcIK8ubE5rJ5JAn1ESl7PNQO3TM2FhKipFGRqXn5jdnQBpQ0BbPal6y8KYrc6Hl7bqjDzJolx9piC3WZHU2aayP0DS9GOaRYDm110KHYfrE6fVnKyCpM11oF61Op-_oF5Fw0W8wukyRdkG5tkoiHxG893sXle2jIWpjV5nS6WjSBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=P3hY-K47P3knSujYXbmEa4Rrgljr-GENhhsimFI5fXxtERAD-Mm5LT3ppcPOiDiHNfdjHcY2KqMloetHuHDjfg1EkodKjq483E4RvgM6F5xIhRY5tgQnN65T5nR-2DahcEgPqfV-h4NYxuzv9lLQKLqlyQC348bPLoYPloITxDcIK8ubE5rJ5JAn1ESl7PNQO3TM2FhKipFGRqXn5jdnQBpQ0BbPal6y8KYrc6Hl7bqjDzJolx9piC3WZHU2aayP0DS9GOaRYDm110KHYfrE6fVnKyCpM11oF61Op-_oF5Fw0W8wukyRdkG5tkoiHxG893sXle2jIWpjV5nS6WjSBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز جمعه، در سخنرانی خود در آلاباما با اشاره به ضربات نظامی به ایران و انتقاد از برخی رسانه‌ها گفت:  آنها نمی‌خواهند موفقیت ما را ببینند. وقتی نیروی دریایی‌شان را منهدم کردیم، نیروی هوایی‌شان را از بین بردیم و چند ماه پیش ضربه‌ای مهلک به ایران زدیم، نیویورک‌تایمز و رسانه‌های جعلی می‌‌گفتند اوضاع ایران فوق‌العاده است. آنها همه‌چیزشان را از دست داده‌اند، از جمله رهبرانشان را.
او با تاکید بر خلأ رهبری در جمهوری اسلامی افزود: آن‌ها یک دور از رهبرانشان را از دست دادند، بعد دور دیگری را، و سپس نیمی از دسته سوم را. حتی یک دور رقابت راه انداختند که ببینند چه کسی حاضر است رهبر شود، اما هیچ شرکت‌کننده‌ای نبود و همه می‌گفتند من نمی‌خواهم.
بخشی از مشکل ما اکنون این است که اصلا نمی‌دانم باید با چه کسی طرف شوم. هیچ‌کس حاضر نیست رهبر باشد.
می‌گویم در ایران با چه کسی باید حرف بزنم؟ اما هیچ‌کس آن اطراف نیست.
در می‌زنیم، تق‌تق، ولی کسی در خانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/78602" target="_blank">📅 05:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bnNoMWcAGEf6GmGJjkDFsqkTpar5mgMq3Sv0Fqs9ge4Ihm9YNI0POuFOOfQsw6tpmKniDh_XkkhWYRUELLRnr6MLGnOarOO8z-sjfJP62gOAIzfCiNE5HUXHeCkblDW0FwFcTiMyZ8NG8Md-J7acNrTwqf7EfG7vVzF9yAlTWJaOgzTlxUfwKyqcHfrPbZDB4ttDjKmqq7-FuV3UvWNnyLAUHV2-FQxyWO3Zc2DcGUWHz6yAVRY-r0pkALEwzzMhCOYcD0iu0V1MaGycJFOfG-gPgJYSblmVPIQMfTUXGkBzvhctb1v4yeVW46IUqBOQ6bdvlVGzGnl8ij-2XIy-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D10Y4sBJUG7BIeCkWLL27xEAk7rTQ8QH1DCBuqpmk_Xj_9GGxPf7Qa9hkTJiimMvNAUHqJAATeUH0Bny3lMMHxQ8EtP1YJpuGG1i4hnaeRfurEBSgz3lHWvd_ltIw6mEhm6KkmNPsSycQrxV-GtpMUGbq9Qq_ebYXEu_MiIcryg8Zd6D5fs_qpCUafRZa3g7WrO2gl1DQEESSp6QWMaxcgv7y9eemo4Zc16QLpxZOWTYw06AS_0jyjHgalD8F760dVR1LVRoTpk6rTcebjr5n6LGE1yhVRcGm8SAr-fW_CdQ7RO0Sn2GJN--HKKUxx6oest8w-URE8Lyxj4l3S5cSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وکیل «الناز شاکردوست» اعلام کرد دادگاه تجدیدنظر استان تهران، حکم بدوی یک سال حبس تعزیری و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری علیه موکلش را تایید کرده است.
الناز شاکردوست، بازیگر سینما، به دلیل انتشار یک استوری مرتبط با اعتراضات دی ماه ۱۴۰۴ به دادگاه انقلاب احضار و به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیزی و دوسال محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/78600" target="_blank">📅 18:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=nUYTvrDBTkJLEmeX3Zf77Ki5MmQ42Po8pfo7N0VDbaqUo2noROh0JJ2yQvBopRu0YEtH8fzhPxCwhMmO77FoIxtuP70JHweT0QpwGEuj6qwykdvzRtboxiAZVcfE3478sV8GR8W9k4X2jcX0CpFxjnXbgvx4rbvqtJz4rUsqAZV5H5QFekcXj2Eyrep2Jm92lcg2E12dm1ILcBKVbTQydzaQwWPjkIauS_L1tc9aU-6lqpMArRDy9T9soy1sV1UyLvGcthI77Og2SgZmzANYOadC7AzdyJlmETUnVftni_kkBFBtmTjEIB_1DBHFvlhtwsOlCPG5Ao_Wdr1He5RlBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=nUYTvrDBTkJLEmeX3Zf77Ki5MmQ42Po8pfo7N0VDbaqUo2noROh0JJ2yQvBopRu0YEtH8fzhPxCwhMmO77FoIxtuP70JHweT0QpwGEuj6qwykdvzRtboxiAZVcfE3478sV8GR8W9k4X2jcX0CpFxjnXbgvx4rbvqtJz4rUsqAZV5H5QFekcXj2Eyrep2Jm92lcg2E12dm1ILcBKVbTQydzaQwWPjkIauS_L1tc9aU-6lqpMArRDy9T9soy1sV1UyLvGcthI77Og2SgZmzANYOadC7AzdyJlmETUnVftni_kkBFBtmTjEIB_1DBHFvlhtwsOlCPG5Ao_Wdr1He5RlBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه پنجشنبه نهم مهر ماه، ویدیویی در شبکه اجتماعی تروث سوشال منتشر کرد که حضور گسترده معترضان در جریان اعتراضات سراسری
دی ماه
در ایران را نشان می‌دهد.
در این ویدیو، معترضان شعار می‌دهند: «امسال سال خونه، سیدعلی سرنگونه»
realDonaldTrump
این ویدیو رو ۳۱ دسامبر ۲۰۲۵ ده‌ها اکانت عربی و اکانت‌های مرتبط به یک سازمان سیاسی خارج از کشور منتشر کرده بودند و گویا بیشترین توجه رو هم در اکانت این مسئول اسرائیلی گرفته بود که بارها ویدیوهایی با شرح اشتباه هم منتشر کرده:
GadbanWaleed
اون روزها خودم هم کلی ویدیوی مهم از شهرهای مختلف ایران منتشر کرده بودم ولی به درستی تاریخ این یکی شک داشتم که مربوط به اعتراض‌های ۱۴۰۱ باشه و نگذاشته بودمش. به ویژه اینکه منبع اولیه‌اش اکانت‌هایی بودند که همیشه کلی ویدیوی قدیمی رو هم با شرح نادرست بین ویدیوهای روز منتشر می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78599" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین باستانی Hossein Bastani</strong></div>
<div class="tg-text">🔻
معمای «تیم شش‌نفره» در حکومت ایران
مسعود پزشکیان اخیرا به «تیمی شش‌نفره» در حکومت ایران اشاره کرد که در مورد بحران جاری با آمریکا «اختیار دارند تصمیم بگیرند و تصمیمات با هماهنگی آنها اجرا می‌شود». به دنبال انتشار این اظهارات در مصاحبه با سی‌بی‌اس، رسانه‌های رسمی ایران روایت‌هایی را از ترکیب تیم شش‌نفره منتشر کرده‌اند که عمدتا در مورد پنج نفر مشابه و در مورد نفر ششم متفاوت بوده‌اند. بخش ثابت روایت‌ها اغلب بر رئیس‌جمهور، رئیس مجلس، دبیر شورای عالی امنیت ملی، رئیس ستاد کل نیروهای مسلح و فرمانده کل سپاه تمرکز داشته، هرچند نفر ششم را برخی رئیس قوه قضاییه و برخی وزیر خارجه دانسته‌اند.
اشاره مسعود پزشکیان به وجود این تیم، البته اهمیت داشت، ولی این اشاره نه اولین بار بود که صورت می‌گرفت و نه نشانه تحولی کلیدی در ساختار تصمیم‌گیری کلان، یا مثلا ایجاد نهادی با اهمیتی مشابه شورای عالی امنیت ملی بود.
در تیرماه گذشته، عباس عراقچی در مصاحبه‌ای با برنامه یوتیوبی «ماجرای جنگ» گفته بود چارچوب مذاکرات با آمریکا در شورایی تعیین می‌شود که به «کمیته شش‌نفره» معروف است. توضیحات او اما نشان می‌داد که جایگاه این کمیته پایین‌تر از شعام ـ شورای عالی امنیت ملی ـ و در حد یکی از کارگروه‌های داخلی آن است. عباس عراقچی در گفتگوی خود، مشخصا از کمیته‌ای «در داخل دبیرخانه» شعام سخن گفت که ابتدا «کمیته هسته‌ای» و سپس «کمیته مذاکره» نام گرفته و در نهایت به «کمیته شش‌نفره» معروف شده است. مطابق اظهارات او، این کمیته از مدت‌ها قبل از جنگ چهل‌روزه فعال بوده و در زمان‌های دبیری علی شمخانی و سپس علی لاریجانی در شعام، به‌ترتیب تحت مسئولیت این دو نفر فعالیت می‌کرده است.
البته روایت عباس عراقچی از قرار داشتن این کمیته زیر مسئولیت دبیر شورا، این ابهام را ایجاد می‌کرد که آیا ریاست آن، مانند شعام، با رئیس‌جمهور است یا اینکه سخن از جمعی شش‌نفره است که رئیس‌جمهور را شامل نمی‌شود، ولی جمع‌بندی‌های خود را به رئیس دولت ارائه می‌کند.
در هر صورت، عباس عراقچی تاکید داشت که تصمیم‌های کمیته باید «عینا مانند مصوبات شورای عالی می‌رفت، تایید می‌شد و بعد ابلاغ می‌شد»، که اشاره‌ای به لزوم تایید مصوبات از سوی رهبر جمهوری اسلامی به نظر می‌رسید. او همچنین، به این سوال که آیا تصویب آتش‌بس (موقت) در پایان جنگ چهل‌روزه «با نظر آقا مجتبی» بود یا نه، پاسخ مثبت داد، هرچند در مورد شیوه تصویب گفت: «ارتباط ما با کسانی بود که رابط بودند و مسائل از آن طریق منتقل شد.»
قابل تامل است که مسعود پزشکیان، که در مرداد ماه از دو نوبت دیدار با رهبر جدید جمهوری اسلامی خبر داده بود، در مصاحبه‌هایش در سفر آمریکا هم به همان دو مرتبه ملاقات خود با رهبر اشاره کرد، که نشان می‌داد دیدار جدیدی با مقام اول حکومت نداشته است.
به عبارت دیگر، با گذشت هفت ماه از رهبری مجتبی خامنه‌ای، ارتباط تیم‌های حکومتی با رهبر کماکان به حلقه «رابط» اتکا دارد که، در مورد آن حدس‌های متنوعی مطرح شده است. از جمله، گمانه‌زنی‌هایی که حسین طائب رئیس جدید سازمان بسیج را از افراد موثر این حلقه می‌دانند.
🔹
ادامه  مقاله در لینک زیر در دسترس است:
https://www.bbc.com/persian/articles/cr9dw7dvjxj1o
@HosseinBastaniChannel</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78598" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-hBuwATzvox_WjW3msBgdaJyuOvPW0yz9SRb7AThPBxB0KvD9L1Kh5EuaF_vOfBJxqo7xqjm1xFVObIfQV1QmSaPKLJ4i4ucAefp4N63VYfeRO1XLizU90H04NPAtLOcmwSgnMdJmQ82-0_zisXb3cCHIAUk-HPbk5rMawqJK_ThJ6MD8sQM9Qgq4DhtkOJDSKmZhf_JQdq_VfUH3pW-h5r-dlnJyV195Bd4WzX2TVPBvLVRl10YjST6hRKJrhpVpf63l0pIC_AaVzkDtwyOBKCgFyeO_8sFzg__5qxwtFvxvCc3BKZ-nXy8NelnAuZ6nTyeS1pfv4SpeNSzCiZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا می‌گوید ایران در ماه سپتامبر حتی یک محمولهٔ نفت خام هم بارگیری نکرده است. داده‌های شرکت‌های ردیابی نفتکش‌ها نیز نشان می‌دهد در این ماه هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت شامگاه پنج‌شنبه، نهم مهر، در شبکهٔ اجتماعی ایکس نوشت: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
این در حالی است که برآورد کپلر و ورتکسا از بارگیری نفت خام و میعانات ایران در ماه اوت حدود ۲۲۰ تا ۲۵۵ هزار بشکه در روز بود.
ایران همچنان مقداری نفت را که پیشتر بارگیری و در آب‌های آسیا ذخیره شده بود به خریداران چینی تحویل می‌دهد، اما این ذخایر بدون خروج محموله‌های تازه از ایران رو به کاهش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78597" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6mJefudEQoEx8QbmoyjnK9LJSaqUI87mSNuJNpa9i9FOChNBnoYnUS2SW8JSOAPPejIoth7NE50Zvf6y1JyDLMygAqrpdGu-l3zvXJUDXOtWNYpZ-4CXfXgKfH_JgIoU84mEyewamURtBA8mBViYc5zCW3JspgS7LOdwS7G1MhsRKDzTQl4ST7tlQL9wrhW36kS7vp8-kNMWd-wTmn692iY2_VPGiwdV8_2-2DB7SIpQ75-pnZGWdIGwJh1ajoL2SqhNbXrzSICJTUxbQqenlFWO7b8VyuRMDcUSHsQb7rEtNHdP4Ci7KzqAmdYS0pWGJNZ3lrGimDm7udkyNoFWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز جمعه دهم مهر ماه، از وقوع درگیری مسلحانه میان سپاه پاسداران و اعضای «یک گروه تروریستی» در یکی از روستاهای شهرستان راسک در جنوب سیستان و بلوچستان خبر داد.
تسنیم با اعلام این خبر افزود نیروهای سپاه «در حال پاکسازی منطقه و بررسی وضعیت» هستند.
همزمان خبرگزاری حکومتی فارس نیز از آغاز «اقدام عملیاتی» سپاه پاسداران از صبح جمعه در راسک خبر داده است.
این خبر در حالی منتشر می‌شود که روز پنجشنبه نیز قرارگاه قدس نیروی زمینی سپاه با انتشار ویدیویی از یک درگیری مسلحانه، از کشته شدن ۶ عضو یک «گروهک تروریستی تکفیری» در منطقه منزل‌آب زاهدان خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78596" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLF-sLXP6-sHy9pAeC-W7-9jcZMBgmbAS8DrnReMObph2b-fDsXteET0juOHjJFrbJcszyJjlGvSfRkBaNaViBRIifAxNIBDvIxhD8EUBwbBfyMO7Dnmitrf1x8KeM5CFl0Iif-3IeAbVSNm_9XnxL-7YweFb8qAZUJVfRKvVL-uPwClVlCsvO5q_fhsDm7bCjrfM9LgowBSSuZ1trvavOiCTuBsM5coGfI3a2FekOhf4JahbuXNUVNbXW-MSylrfvxyPdkypiSEn4sK8rxYo41Hm_H--MBcojCbn9mTDK7fCesE_UQQBe4ulUMr5eHzpU90XhixG4XtXzsRLrDp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در دو اظهارنظر تازه دربارهٔ ایران هشدار داد اگر مشخص شود تهران در حادثهٔ پرواز فلای‌دبی به مقصد اسرائیل دست داشته، «به‌شدت هدف قرار خواهد گرفت» و ساعاتی بعد بار دیگر گفت به اعتقاد او ایران «در آستانهٔ تسلیم‌شدن» است.
این اظهارات همزمان با ادامهٔ تحقیقات امارات متحده عربی دربارهٔ احتمال تروریستی بودن حادثهٔ پرواز فلای‌دبی و گزارش‌ها دربارهٔ تقویت حضور نظامی آمریکا در منطقه مطرح شده است.
رئیس‌جمهور آمریکا شامگاه پنج‌شنبه، نهم مهر، به وقت ایران، در پاسخ به پرسش خبرنگاران در کاخ سفید دربارهٔ احتمال ارتباط ایران با کمک‌خلبانی که به خلبان پرواز دبی به تل‌آویو حمله کرد، گفت: «بر اساس آن‌چه می‌شنوم، می‌گویم پاسخ مثبت است، اما همین حالا در حال بررسی آن هستیم.»
تاکنون هیچ مدرک علنی دربارهٔ ارتباط ایران با این حادثه منتشر نشده و تحقیقات دربارهٔ انگیزهٔ کمک‌خلبان ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78595" target="_blank">📅 16:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxPRDKmQy8JYECVpG8hjRU8T6TfRpyFFymvN9gdcZ8BOpDv2mFOnAm9XZxOIzypP36xsvXo0LjcPjcC5VVDmvHvLcglv2LbMfUHkGQTl1ifmh6HEQtG_cAsT1m-G57EDl6CSh_dTYlk-DgQsI3cfT5VZJxy9soIdkz6uyOtPg3Ow5YBdEZFJn8_CFHzV99O7Asktffj5E0mS0dsaU2_yu9wSqWEZ4eNSwpNGPZJGUKtsFJLjfxXJ2QvopWrUVRpg6Bz55KTYXLtvuR7AYAcN4vFdhAN_yQGNF8dqZeAFLVzuPkQm09S09AOd808kAOY8sPIhp0NBXYbIcvX05ST87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه شهروند اهل کرمانشاه، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در شعبه ۲۳ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌اند.
بر اساس اطلاعاتی که به سازمان حقوق بشر هانا رسیده، سیروان شعبانی، ۲۵ ساله، هنرمند و نوازنده و سرپرست یک ارکستر پاپ و سنتی، خسرو محمدی‌نیا و مسعود توشمالانی هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شوند.
هانا گزارش داده است که این سه نفر روز ۱۹ دی ۱۴۰۴، هم‌زمان با اعتراضات در اسلامشهر، از سوی نیروهای امنیتی بازداشت شدند و پس از آن مدتی در سلول انفرادی نگهداری شدند. بر اساس این گزارش، آنها پس از ماه‌ها نگهداری در شرایط انفرادی و آنچه هانا «اخذ اعترافات اجباری» خوانده، به زندان قزلحصار منتقل شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78594" target="_blank">📅 16:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIW7kXDeM3MLxnJwkODwR-FFgMuo47tpvZ9H3FPKvIrVa6ITAQvCCsxKkFdUboRt9CyWQ5BnXkPciWD9yQdpJKBLQcozdTN2IRORc_tcRtOvPUBGnRyEuyufC0jnJqobNmmgo7kOx4m14y1mDXepvtKvPvqqZxigZpl8yh0_5S8S-mPWxTEV5DX9d-j51RL7uI-oeI2TJfGGpPmOo2p4Oh2ReDxGQMPPGTKM2RrsUaGqiDpLy1RYWw-y6iLWb5Vwzj95Jw1mO0FDMJbVfPZU5YHj11FI1O4EBfEaqCLJt_DNU-1CnzQ2IugV9BkX8BKI6pG7buu00e0Z8bnyXriAPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
«عملیات تجارت دریایی بریتانیا» (UKMTO) گزارشی از یک منبع ثالث دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته و در پی آن آتش‌سوزی رخ داده است.
گزارش شده که خدمه در سلامت هستند. میزان خسارت و تأثیرات زیست‌محیطی در زمان انتشار این گزارش مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78593" target="_blank">📅 23:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LnNZRqX_4o221qBJ8acKdivIwJk17xztVsk9-l5oLfiMJJbCAq_qOG0H4EaM9COG_7VBAysQJyRKhrC6ULidnt9_HawAlK8Jfr8yNsHmBtU-RyU65tSyNodtAG04L625SjB5z2MHpEnZBWzIy4ogB3LM31RuX8aITUJc3Xqj3jnZVEdEjrE7ci7s7zUD89as2jzA-W2lAID-7o4OeWPmuRcGEx-7iXC5xRkU20MpuAaikxB8yOyFPJGtH1li5Wcy9ap1v_rR6vPz6CSlGUrMoYV5tZEiNmN9cxX5Ri9TBDjSMsHqLvwe0jFgWipyN-9ws3gWu-IYuXaRHKik63tQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78592" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nHbRXdOZzOg_NEQ44fjzKhCePl9DNgJSgidvMCJ-pQI6vXNlVsL5wOAVMPOZ19bCjOmiIQmV6_haY_27SKhRmpMsZO9zNSpWlKnFTcePSa05gFj8FKrpKUNBbpcvhcnmIqbLeY1-5ULX7I1eAmolsWk_4xH8-c184OympZUelqRU4L02qZxkgdkscZDFdSu_SQXRQJSWb2HHr99kF1jRP0AQky4uRmO77OGO7OZHbOaqjMrwldQQtLQaW2m4_gqYMjD9NZ16afpzdxZcafjuSm44oqTwJb25NAH8Ux4zAbVw5jll58qM7M93fxnJJ2HP9KOO9OTU8nreYG64qj6Gcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهوری آمریکا، در مصاحبه‌ای مفصل با مجله تایم گفت پیشنهاد اخیر جمهوری اسلامی برای پایان دادن به درگیری‌ها و بازگشایی تنگه هرمز را به دلیل «ناکافی» بودن آن رد کرده است، و افزود احتمال تشدید حملات نظامی آمریکا علیه جمهوری اسلامی را منتفی نمی‌داند. این مصاحبه ۶ مهر در کاخ سفید انجام و روز پنجشنبه ۹ مهر منتشر شد.
دونالد ترامپ در پاسخ به این پرسش که چرا درگیری نظامی با جمهوری اسلامی بر خلاف برآورد اولیه او وارد هفتمین ماه شده است، گفت پس از حمله بمب‌افکن‌های بی-۲ به تاسیسات هسته‌ای می‌توانست عملیات را متوقف کند، اما تصمیم گرفت «فراتر» برود تا حکومت ایران نتواند توانایی‌های خود را «به شکلی متفاوت» بازسازی کند.
او گفت: «توانایی هسته‌ای آنها را نابود کرده‌ام. نیروی دریایی‌شان را نابود کرده‌ام؛ ۱۵۹ کشتی در کف دریا هستند. نیروی هوایی‌شان را نابود کرده‌ام. همه هواپیماهایشان از بین رفته‌اند. رادارشان را نابود کرده‌ام.» رئیس جمهوری آمریکا همچنین گفت اقتصاد جمهوری اسلامی از بین رفته و تورم آن حدود ۳۰۰ درصد است.
ترامپ گفت آمریکا عملا کنترل تنگه هرمز را از جمهوری اسلامی گرفته است، و تاکید کرد شب پیش از مصاحبه حجم عبور نفت از این آبراه به بالاترین میزان تاریخی رسیده بود. داده‌های جدید نشان می‌دهد صادرات نفت خلیج فارس در روزهای اخیر به‌ شدت بهبود یافته و به سطوح متوسط سال ۲۰۲۵ بازگشته است.
در بخش دیگری از مصاحبه، خبرنگار تایم به اظهارات اخیر ترامپ درباره احتمال «نابودی ایران» اشاره کرد و پرسید آیا چنین اقدامی واقعا ممکن است. او پاسخ داد: «بله، این کار را خواهم کرد. ممکن است.»
هنگامی که خبرنگار درباره مردم غیرنظامی ایران پرسید، رئیس جمهوری به سرکوب اعتراضات اشاره کرد و گفت حکومت ایران طی ماه‌های اخیر بین ۷۲ هزار تا ۷۵ هزار نفر را کشته است.
ترامپ همچنین گفت از تصمیم خود برای مداخله نکردن مستقیم در جریان اعتراضات دی‌ماه پشیمان نیست، و عملکرد دولتش در قبال جمهوری اسلامی را «باورنکردنی» توصیف کرد.
او گفت ایران کشوری بسیار بزرگ‌تر و دورتر از ونزوئلا است، اما «نتیجه همان خواهد بود» و افزود: «آنها می‌خواهند توافق کنند.»
در پاسخ به پرسشی درباره علت رد پیشنهاد اخیر جمهوری اسلامی برای آتش‌بس، ترامپ گفت رژیم ایران پیشنهاد بازگشایی تنگه هرمز را مطرح کرد، اما شرایط آن «حتی نزدیک به کافی هم نبود.»
رویترز گزارش داده است پیشنهاد ارائه‌شده از طریق میانجی‌های قطری شامل پایان درگیری‌ها و بازگشایی تنگه هرمز در برابر رفع برخی فشارهای اقتصادی آمریکا و دسترسی رژیم ایران به دارایی‌های مسدودشده بود. مذاکرات غیرمستقیم همچنان ادامه دارد.
خبرنگار تایم سپس پرسید آیا دولت آمریکا پس از انتخابات میان‌دوره‌ای حملات به جمهوری اسلامی را افزایش خواهد داد. ترامپ پاسخ داد: «ممکن است.»
او از ارائه جزئیات خودداری کرد، اما گفت آمریکا طی شش ماه گذشته ذخایر تسلیحاتی خود را افزایش داده و شرکت‌های دفاعی با فعالیت شبانه‌روزی در حال گسترش تولید هستند.
رئیس جمهوری آمریکا در پایان مصاحبه هدف اصلی سیاست خود در قبال جمهوری اسلامی را جلوگیری از دستیابی آن به سلاح هسته‌ای دانست و گفت: «موضوع اصلی که همیشه مطرح می‌کنم این است که ایران نمی‌تواند یک قدرت هسته‌ای باشد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78591" target="_blank">📅 17:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfJjPM6RPfDAXlQbvva7uqcFR1owoI4XcsGrV0bVOqmhY-AdYHYAbcpTB3GFmBGDz7Te7flLwpTteakLViGkBwSyhrRuG11OarLWScSqwFadujsBwZTS2PtOUZnDy6r049I_SPyJvvdyWGFiTYTETXpcz6uN_pj_A7XI_KJbN6gqx3c0aZc4u8qwuAvFG3z4WWE8PAjasDqPLTARpESiuFLVM3HQQuPKD5yc3cA40U3Jw4j16YS1BMMv7PqFw-sEn-nTbnPdA6c2y8e1-pyK0SJeI3lwSTEK4c3uaXbWkyZXrt8jqwW1Rp6VxXufJ2aA8UgG_vRoGtQ3vJseGuPrDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد ایران روز پنج‌شنبه با افزایشی حدود ۱.۵ درصدی نسبت به روز گذشته به ۲۵۸ هزار و ۹۰۰ تومان اوج گرفت.
دلار آمریکا در مقابل ریال ایران طی یک هفته گذشته بیش از ۱۰ درصد، طی یک ماه گذشته بیش از ۲۰ درصد و از زمان آغاز جنگ حدود ۶۴ درصد جهش داشته است.
در بازه یک‌ساله نیز نرخ برابری دلار در مقابل ریال ایران تقریبا ۱۲۵ درصد رشد داشته است.
قیمت سکه امامی نیز در لحظه تنظیم این گزارش در بعد از ظهر پنج‌شنبه از ۲۶۰ میلیون تومان فراتر رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78590" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-BgV88FFrY0RLeeej6EJqO3J4VCGACM_0u5tJDFKj3Y50PN_ao2ZMEu6sIjbiOJWLjVj-wpohWWUMwKQHIiwkYdf3NO5Imuw4vqCtBXY0FxUeWVtgnu9zkPVmuOW7pnEL9ncOzBH2vmP4_BaemmlKyyxGHGj7i_vC5hXbdqcVEPb_6UR4kvnqnXlWX503yxcIyuMrn4vzzd0zfBP9J_7smcaw6sGD-z0SKXFFvNXlIrS5CHJGSoD2TZKnIQFP0D5s1fe4TLFmdFHO8BQZ-verLvgGUVT2RcWVTeOGZP2yhowaITlgppeP-RRzZRgYISpp9xBCXDC49XtsEmBKhz4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، در واکنش به اظهارات تازه «احسان حدادی»، رییس فدراسیون دوومیدانی جمهوری اسلامی، او را «بدنام‌ترین ورزشکار تاریخ ایران» خواند و نوشت که ورزشکاران جوان باید او را «عبرت» قرار دهند، نه الگو.
فرزانه فصیحی در متنی که در صفحه اینستاگرام خود منتشر کرد، خطاب به احسان حدادی نوشت: «در جهان موازی تو باید پشت میله‌های زندان می‌بودی و از هیچ حق شهروندی برخوردار نمی‌شدی، ولی چه کنیم که اینجا سرنوشت صدها و هزاران جوان پاک و معصوم رو هم سپردن دستت و حالا فاز نصیحت برداشتی.»
این واکنش پس از آن منتشر شد که احسان حدادی، چهارشنبه ۸مهر۱۴۰۵، در گفت‌وگو با وب‌سایت حکومتی «ورزش سه»، درباره ورزشکاران زن گفته بود: «با زنان دونده جلسه می‌گذارم و به آن‌ها می‌گویم تو می‌توانی مثل خیلی از ورزشکاران زن، مجازی شوی با ۳۰ هزار، ۵۰ هزار، ۳۰۰ هزار فالوئر، یا می‌توانی قهرمان شوی.»
فرزانه فصیحی همچنین با اشاره به «ریحانه مبینی»، «زهرا زارعی» و «فاطمه محیطی‌زاده»، از ورزشکاران زن دوومیدانی ایران، نوشت تصور این‌که آنها بخواهند از آموزش‌های احسان حدادی پیروی کنند، برای او «مثل کابوس» است.
او در ادامه خطاب به رییس فدراسیون دوومیدانی نوشته است: «شریف بودن ربطی به مدال و قهرمانی نداره. تو ثابت کردی با خورجینی از مدال هم می‌شه به قهقرا رفت و منفور یک ملت شد.»
اشاره فرزانه فصیحی به «پشت میله‌های زندان»، به پرونده قضایی احسان حدادی در دهه ۱۳۹۰ بازمی‌گردد. در آن پرونده اتهام تعرض و تجاوز جنسی علیه احسان حدادی مطرح شده بود و دادگاه نیز رای به زندان، تحمل شلاق و جزای نقدی داد. با این حال پرونده با دخالت نهادهای امنیتی مختومه شد.
در سال‌های اخیر برخی از زنان شاخص دوومیدانی ایران نیز کشور را ترک کرده‌اند. «الناز کمپانی»، رکورددار دوی ۶۰ متر با مانع ایران، از مهاجرت خود به آمریکا خبر داد و پیش از او «مریم طوسی»، رکورددار دوی ۲۰۰ متر داخل سالن زنان ایران، به آمریکا مهاجرت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78589" target="_blank">📅 17:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZKEWCgN9Uv3foDY7QCoNBQOMV9Gs9TSjOHVgOUJJRQ6bKgo_H2MMRbQUqO9THbyfHVRep3UTZTZTCOkMJtcY7qQPdPK9p5fR-8zlY_wddwAK0nLLbWdWsxz8OONnesSgbHsQt4FK2sgQgpYpEqIvCIRCytzJCEELYJT-FwuhYP8QYD2PykwgjyFt1RZLFTczJsN2bYLwfOYzGpoxDZsdWPP18vZK-ApUc1BN0CoebmPn85sSNUDd5KhR9-mfntPhxmOfwuKpgCH-We5AJEkuZhI7QO-uHgoH2tLVCU6La4p8avxG6K4mpsB2TDyPzSoMOZWpUYJXUMdy89k0HfbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان صادقی، بلاگر ۲۰ ساله و از بازداشت‌شدگان [اعتراضات دی ماه] در کاشان، به بیش از ۱۳ سال حبس تعزیری محکوم شده است.
او بابت اتهام «تبلیغ علیه نظام» به هفت ماه و ۱۶ روز حبس و بابت اتهام «انتشار محتوای مجرمانه برخلاف امنیت کشور» به ۱۲ سال و شش ماه و یک روز حبس تعزیری محکوم شده است.
«انتشار محتوای مجرمانه در رسانه‌ها و مطبوعات منتهی به هتک حرمت اشخاص» نیز از دیگر اتهام‌های مطرح‌شده در پرونده اوست.
ایمان صادقی ۱۱ بهمن‌ماه ۱۴۰۴ بازداشت و پس از آن به زندان کاشان منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78588" target="_blank">📅 17:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f8yDCIRpdfQJGk5H_z842MGCq9PzkWPd7CeWtbltjnzRo23Qqr9L0BF757huWW5FOTW-KUKHJrCEpv1aiELaK2P21GXNAsnlaz2WVn6nmEavQnjl9FClw3-yPrvZ_gSrK0kvkrCzaJXnlvYwmwYUHJhufxIVR3IZlutFBoTtSttQaMFRXlL62FLKwrc2TIurBOEV5dQSfs_uwQU_cxzcYtWD9jspdVGOGJ7Wf9ljxWvo4ZwKOTk3jNW9TVJtvwnx3kZgCVS6-V3ovVNspfqx51gT7JMnadbHGfyFIflWVWgwUk_M0rAuTOstIJtSxE9ZbyiQ05z3ghzEUH0CwEQ5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه شب، گزارش نیویورک‌پست از اظهارات اسکات بسنت، وزیر خزانه‌داری آمریکا را منتشر کرد که گفته است اقتصاد جمهوری اسلامی ایران، «ظرف دو هفته» هیچ‌چیزی برای تجارت نخواهد داشت.
محاصره دریایی بنادر ایران مانع آن شده است که جمهوری اسلامی از طریق دریا بتواند نفتی صادر کند. دلار آمریکا نیز در روزهای اخیر با سقوط خیره کننده ریال جمهوری اسلامی، رکوردهای تازه‌ای زده است.
آقای بسنت به فاکس‌نیوز گفت اقتصاد تحت محاصره جمهوری اسلامی ایران به‌زودی و پس از تحویل آخرین محموله‌های نفتی خود، در حدود دو هفته دیگر «چیزی برای مبادله» نخواهد داشت.
به نوشته نیویورک پست، بسنت در مصاحبه با فاکس‌نیوز ارزیابی کرد که جمهوری اسلامی به دلیل فروپاشی اقتصاد خود که با اجرای «عملیات طرد اقتصادی» شتاب گرفته، از روی درماندگی به‌شدت مشتاق توافق است و هشدار داد که مشکلات آن طی دو هفته آینده به شکل چشمگیری وخیم‌تر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78587" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
