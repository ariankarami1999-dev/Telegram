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
<img src="https://cdn4.telesco.pe/file/Kk6zki0WAcTQH4lrISgtfPA8VutdwbqykJx-bZhBubUujfcBmzthiU4JZT5B9h3aOflFpk-lM5L7O2bWA4oRBCmq4YKngJlJvOl8W34wUMqirm0GSm_WuOBXivBx0fQnjodfS2amdTNxfHDE-ReRpZQHLAsM5kLfq_lER3GktdXTfMXTnACo3wKNp1eneo6i9ATUGry_kF-mJUxLzxypRcTmscCJjv_IsFGOiXkQOOyHtSoGVM3BSKuYxd67Yw6hEXEZvTLpDYjGVSABZkdG4hfd8hbnaezcmWALMFPETl342Y3BYHz4wUFGOlbjNqBb8sZsrg3Sd1unUySRKqXaTQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 963K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 09:59:18</div>
<hr>

<div class="tg-post" id="msg-124970">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2n4rSzShUWerYea6_kE2IjdMJdqYWfKLWaeOfl3VJ923i9f0HGXB16ZkKH8UdQXwHu7zXktNYGNxixzhWydJeoblOX709DYqKBeM_9l6aHHfzNGWJjv0wqTCAqwSa32v8B-x8ofWedd4ezj6UqRW_e5RObX5bRNY8-NBFwdb_KTUZnOpcuu2qA5HXD7mLAagVsGA8sz3z-3MsK_m0G4-dI2bFbWzptbdxpoV_lH6Qsx1GUnL5Qycfur8_vBXv9PjAYcL1aCsipd2RcBTf9NMd5Lg1LiqRtc7Ijsd2k3Q3920m4vI0FPv0pe0g_fYkGRsMFj85FtGL5icyfW0vmxYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اپل برای رونمایی از نسل بعدی سیستم‌ عامل موبایل خود آماده می‌شود. بر اساس اعلام رسمی، iOS 27 کمتر از چهار روز دیگر در WWDC 2026 معرفی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/124970" target="_blank">📅 09:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124969">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کاتز: اسرائیل این آزادی عمل را دارد که با حمایت آمریکا در پاسخ به هرگونه آتش‌سوزی به سمت شهرک‌ها یا اسرائیل، به بیروت حمله کند
🔴
حضور ارتش ما در منطقه امنیتی شامل منطقه قلعه بوفورت می‌شود و ساکنان از بازگشت به آنجا منع شده‌اند
🔴
یک منطقه غیرنظامی در جنوب رودخانه لیتانی ایجاد خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/124969" target="_blank">📅 09:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124967">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=JGpcVPbqY6IJ6gOy3Aps6Ofv-NIQ9xBGrX_ZHcaMhMPIHUvBbz_gxzi3LCHJ_90Dm23rzpNPhqKksF22DMH0GG6t1bINiBouVyxWLi4RvT5u9uGtfxspvv_huya4_uBL_S65RocTNd-jWO_taxZOxcsCFDMYDPnx-Nx4sbfiLto39pY56lQRcADzmaGLmi8y5eWqjvrz6JIlQZ8K3oMM2aIPZc2rpyE1T5qaAII3ULfOGoJ1wwmtFea3a2fd3eQOy07-qw4WWlVQhRPZklJLCdGkCe5dcD1hfbAdiY17Dkrws-lWD7mkpKLMP1Wk9h6mTwL3-75w0t1jaMFX5CAdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=JGpcVPbqY6IJ6gOy3Aps6Ofv-NIQ9xBGrX_ZHcaMhMPIHUvBbz_gxzi3LCHJ_90Dm23rzpNPhqKksF22DMH0GG6t1bINiBouVyxWLi4RvT5u9uGtfxspvv_huya4_uBL_S65RocTNd-jWO_taxZOxcsCFDMYDPnx-Nx4sbfiLto39pY56lQRcADzmaGLmi8y5eWqjvrz6JIlQZ8K3oMM2aIPZc2rpyE1T5qaAII3ULfOGoJ1wwmtFea3a2fd3eQOy07-qw4WWlVQhRPZklJLCdGkCe5dcD1hfbAdiY17Dkrws-lWD7mkpKLMP1Wk9h6mTwL3-75w0t1jaMFX5CAdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیده شدن دونالد ترامپ در یکی از پارک های شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/alonews/124967" target="_blank">📅 09:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124966">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: به هدف قرار دادن زیرساخت های حزب الله در لبنان ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/124966" target="_blank">📅 09:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124965">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رافائل گروسی» مدیرکل آژانس بین‌المللی انرژی اتمی در سفر به ریاض با «عبدالعزیز بن سلمان» وزیر انرژی عربستان سعودی دیدار و در مورد پیشرفت این کشور در برنامه هسته‌ای غیرنظامی ریاض گفت‌و‌گو کرد.
🔴
گروسی در صفحه شخصی خود در شبکه اجتماعی ایکس نوشت: «برای من مهم است که در عربستان سعودی باشم، زیرا ریاض در حال پیشبرد برنامه هسته‌ای غیرنظامی خود است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/alonews/124965" target="_blank">📅 09:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124964">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کاهش قیمت نفت با امیدواری به آتش‌بس لبنان و اسرائیل و خوشبینی به پیشرفت مذاکرات ایران و امریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/alonews/124964" target="_blank">📅 09:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124963">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزارت امور خارجه فرانسه با انتشار بیانیه‌ای همبستگی کامل پاریس را با کویت و بحرین اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/124963" target="_blank">📅 09:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124961">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gtWtXOwjn-pWIWD36xqVZrt6qcrkvYjRzibAcISSSaxpk9uwSv27aXtTtcD8j6qMIy3Kmw-jjO9l42pUMdJQa0sT6jDkPkKTF30St1hh2QbYpiMUZdHf0ub-wCLhSY7cGDhn2gnLz0uv4UcUPOsZm4--L9XSJHdZSKzJChxDXrRoRIvm5i9DjvErHDyq1PyJjYUcPCsVpGFhGBxKtRByVZYq3c8hhdjjtOnDplpY397t-EA2Le4SuT2NubT8OYY3CO-Z4eFGx4DHcQmYbT4Vw0a8rNIvLZ75FQikbiZLyVr2kNZgNmJQTdlqnLu78Ke51B7HJM_i2gRXSzlq5evhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JC_2O1m5DWlrfL83ZDic8CtEGdZQg9QM2K4DBSiYv90Bi7VZFv-ZXqawmuqCGd7Himg7-bTxKRoxz2HCXPk7WGO5w7esKRXKL7qeaAewfQF_OaJH3iE90a8_KlCADnqwsJ3dthlh1P1TzvDYY-v0rcAw09m_Z4Eyc5kQRI9d4P2OIb8vtIXQQko8FWQxqno7YHqsgQ6thyvkp1RcOwH4lAfz-DkBpdaQReT7XpO3xh3A3WyI2rmcd2YsTEAFRJH1XTpO218bjXQAk9coemLOpe8KisamrSDy7Bs10ml1T1r4lExxSj7govdkI9vI5SuXqTW7lmwVzpStZrmgHJxR7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا به درخواست نماینده تگزاس، واکین کاسترو، برای پاسخ به این سوال که آیا اسرائیل سلاح هسته‌ای دارد یا خیر، پاسخ داد.
🔴
وزارت امور خارجه پاسخ داد: «ما شما را به دولت اسرائیل برای سوالاتتان درباره توانمندی‌های اسرائیل ارجاع می‌دهیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124961" target="_blank">📅 09:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124960">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
محمود قماطی، نایب‌رئیس شورای سیاسی حزب‌الله: تمام تلاش‌های آمریکا و اسرائیل با شکست مواجه خواهد شد.
🔴
رویارویی ادامه دارد و مقاومت در برابر تجاوز اسرائیل همچنان پابرجاست.
🔴
آمریکا و اسرائیل هیچ حقی در مورد سلاح‌های مقاومت ندارند، زیرا این یک موضوع داخلی لبنان است که ما در مورد آن توافق داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/124960" target="_blank">📅 09:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124959">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بن گویر وزیر امنیت ملی اسرائیل:
آتش بس با لبنان یک اشتباه بزرگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/124959" target="_blank">📅 09:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124958">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C394ezS25KYoCyzgQpSyFkq5AEQlW9VquyEh3sp8p2EwZEBwi2nweeLOciRpKXKEOZYheA2QM1hMq8CGdsjVBbekFrBoIdb5d1IT11d0dg2eV5J1AwZaHJBkQqUgWlqKx_gO47kyC_h5FZowmV0SW1N8OdZiilx4Xqwq8jI3FkZpJiIHzSfPoDuGG_OelNRcvpUqW46Wg0byC2BYR10DSbQMapMhT7ktN2KeKaMwt2Bl9fkkm1Rj7O_koe52XakRyhiNy7j1dpLLr9D_Mz4kW4ir5iIpPeGwUDx2yx3_l_rErd-QFMkEryb2Vkk6IQbVQkGdk34iiB9UlCuCFpb8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست در مورد مذاکرات ایران و آمریکا: هر دو طرف به آرامی به سمت توافقی حرکت می‌کنند که ممکن است پایدار نباشد. آنها طوری رفتار می‌کنند که انگار این توافق دائمی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/124958" target="_blank">📅 09:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124957">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwwgA6ONak1wX1lTegIraseJpVwEj8V3cU0SRM9heBurJXoakSLoYw5DBV0-TGNtZNsAGQrVUrkDLQ1KggjCQ7mMYKPy3CqXnDK3CR5ei84uporhABiRhrDCbvR8BmOQ8pBMUg8F33us0aogkeaIj1mCuVVX2_17PaSlSqIrqFALyKvJiLe-l5bXPIm34JCTG05VId_XjV5A6xYPIfB_Nh3Ls6Mlb-vGnTJKwiqZQGN7P4SB_kQHMruY9Xf7eBxKOx1dQtINMxEBgaZi3sZ8QzQwPrIh2YUN5vW3paJc1kJn03huTb8aSyQXeMa0sv2r1QmiwuuubLQFe2a1gDWDbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال تایمز: همزمان با جنگ آمریکا علیه ایران و اختلال در عرضه انرژی، ذخایر نفت آمریکا به پایین‌ترین سطح از ۲۰۰۴ رسید و در صورت بسته ماندن تنگه هرمز، احتمال افزایش قیمت نفت تا ۲۰۰ دلار وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/124957" target="_blank">📅 09:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAKvO-M_e2wsF9pT7US4ziYRJ2QKQkd-NypJk2MOc0nC93_5zpK2Dgv27UqdMIKQHHG7V12PAPHOjMG_q2NuBcEWM4thIEymGM6mBeNy9-my2HSF0eH4OAt35Zl5B9E8hsYRKJjvNrs-Gp0jo1FDseYGwwotie3llVqp2jtiZ6z12BUa2oqX3z2XjAgK5r7gy7NLv5K4OV3wPNFzRhVWg23Jz2A1dXxjBTeLFRFEFfSByNx0QIQUBXjnDzK-_eIyRpk3GTVJaI7GtiVZDqnGuIQakbBaZpHxZbKGhy4zmmg-8XAA4diJ0WwvV4sPni1nCwjmOvHcymELqm0U72Qvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت کوین برای اولین بار از ۲۴ فوریه به زیر ۶۳٬۰۰۰ دلار سقوط کرده است
🔴
بیش از ۱.۱ میلیارد دلار موقعیت‌های اهرمی ارز دیجیتال در ۲۴ ساعت گذشته نقد شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/124956" target="_blank">📅 09:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T07PDJGb6ceTGiqbW5am_0ajVKftxEuKafkGbthJTTN3Ll7nwT3V79Sw6DqCuDSPpjwGcBLRezhlBjwSKKpubgqiM-j1Nnxz3GiIojEz4pdGQLdonpaJEx-bhREhExt-RYTofLcLnuZDfn_CI7N14NqjgTWg4WSEprYlvu34R53P_yPeEkR5KY5N7dnaVUWvhI5MfM1edZAeWwSCuSjL7TIuPomHatrflZcVUcPwt4tFxQ_wg1HzwNdGFWXBERqXQk9tZDKlVCmykofYy8n2etm_BqSaJID2VHtigGTUnYLtF9IyUWhQxr9QlaRlzk00gs0pql8ASfZopcpx8c34Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: مقامات آمریکایی گفتند حملات مکرر تهران فشار بر ترامپ را افزایش داده و در مورد دوام آتش بس در درازمدت تردید ایجاد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/124955" target="_blank">📅 09:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
معاریو به نقل از یک مقام امنیتی اسرائیلی: ما یک پنجره عملیاتی برای انجام مأموریت در بیروت داشتیم، اما بیانیه نتانیاهو و کاتس آن را بست.
🔴
ما می‌توانیم در صور و صیدا آزادانه عمل کنیم، اما بیروت تابع محدودیت‌ها است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/124954" target="_blank">📅 09:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2c8a0e05.mp4?token=geeoxj3WPIY2QC4iVfG4aQ-neD7ROroaPNnltAFVjtAR2uMYITmc1kcaft5MTXX6RgntBtZ1GsgL7mVEUR3XMbUbNkzT8lOwILj2gay6LU-K9ER1C1dJOSUokr3MB7gal0iheX7QAETevwgVH90m1MzwjlQCx7zqOBQQkkOZX4tGB0MGU4KNZW_8c9swyTwBH5h0-YyTcMRNAKCLZqgoMr3m7iFgUz2oOEYJL7Y2Zli2iPoLzJ41hE45YYmxyFf-_Rmm8ztP5o92LORTwCKTyVLLAdMG5Y7zHNgOemAdRgrJgjNbnJBedrOr-Oc3Bn1WfnShHvaRW4yG--f_K8r5tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2c8a0e05.mp4?token=geeoxj3WPIY2QC4iVfG4aQ-neD7ROroaPNnltAFVjtAR2uMYITmc1kcaft5MTXX6RgntBtZ1GsgL7mVEUR3XMbUbNkzT8lOwILj2gay6LU-K9ER1C1dJOSUokr3MB7gal0iheX7QAETevwgVH90m1MzwjlQCx7zqOBQQkkOZX4tGB0MGU4KNZW_8c9swyTwBH5h0-YyTcMRNAKCLZqgoMr3m7iFgUz2oOEYJL7Y2Zli2iPoLzJ41hE45YYmxyFf-_Rmm8ztP5o92LORTwCKTyVLLAdMG5Y7zHNgOemAdRgrJgjNbnJBedrOr-Oc3Bn1WfnShHvaRW4yG--f_K8r5tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای با وضوح بالاتر از خسارات وارده به یکی از پناهگاه‌های پهپاد/هواگرد در پایگاه آمریکایی علی‌السالم کویت در پی حملات موشکی سپاه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/124953" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124952">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V621jpC0U-_6zYjmwFodu3gWt0kf5bTQS9n-ppk5QHQ-0Fou6PjdpTGVfB-pQcFZkkyKHcf6UfkJoDM4mOHTKJnw3hT5Zte-qICKIkVC8DlMUO0aF_VOs4xyTS1ZPXYipy7QYvr0zgiHM6HRA3Tx0m5N5v6v9o2p90HR_r9HBMm4IA7STAGMWnagXiFCFFfs8U7RmiIKmeECfQ6I3kmN36EU0gS9_dFm-9QWJ64FrShjI45UlhcEAKAK1tBqzllvFUp1F_pwLJE2UX0D3Qph6wKru4V7g2IUW_LNInoozlQiIK0qitE9uv2ZWAToJRD7thBn_TUoj87aRygno_kvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۲۰۰,۰۰۰,۰۰۰,۰۰۰ دلار از ارزش بازار رمزارزها در ۲۴ ساعت گذشته کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/124952" target="_blank">📅 09:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سی‌ان‌ان گزارش داد ترامپ به مشاوران خود اعلام کرده است هیچ توافقی را که شامل ارائه بودجه مستقیم ایالات متحده به ایران باشد، امضا نخواهد کرد.
🔴
این در حالی است که بحث‌هایی درباره ایجاد صندوقی برای واگذاری میلیاردها دلار به ایران پس از دستیابی به توافق نهایی مطرح شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/124951" target="_blank">📅 09:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
تصاویر مربوط به اصابت پهپاد انتحاری به فرودگاه کویت از دید دوربین‌های مداربسته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/124950" target="_blank">📅 09:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a81b6cc9.mp4?token=CIjW3VlmiBLSZroH0-uo4VqRmD41SF4ivLk4gCuk_UA0yztlJwhzDW_9EUn0X-z8uw85U5G5kJEUFJP5WHTs--vPSaZ6GtJHC1nufmpzLvFBZVj1XqSodBgvm_8qrxw0GGgssx7AFMkDd2rmIOfp7XZnjtJGF-s9VBMLGGlbg__nk8GZGIB58etiZxFs-EX5BC-Dauj98k527WEzbWnMY63wl40TPA0SIvTFl8TDhdo18h9pUsXD6R5kejLRbScuRPXgVyd6lxY5GTV3MgbBe3-0jM_jp-GjqAOBpHEK-dXKxVx6XDqAIlr6CXjK_blA328eeEpjyjYb_kPCdwxIiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a81b6cc9.mp4?token=CIjW3VlmiBLSZroH0-uo4VqRmD41SF4ivLk4gCuk_UA0yztlJwhzDW_9EUn0X-z8uw85U5G5kJEUFJP5WHTs--vPSaZ6GtJHC1nufmpzLvFBZVj1XqSodBgvm_8qrxw0GGgssx7AFMkDd2rmIOfp7XZnjtJGF-s9VBMLGGlbg__nk8GZGIB58etiZxFs-EX5BC-Dauj98k527WEzbWnMY63wl40TPA0SIvTFl8TDhdo18h9pUsXD6R5kejLRbScuRPXgVyd6lxY5GTV3MgbBe3-0jM_jp-GjqAOBpHEK-dXKxVx6XDqAIlr6CXjK_blA328eeEpjyjYb_kPCdwxIiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض به حمایت آمریکا از اسرائیل در جلسه استماع وزیر امورخارجه آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/124949" target="_blank">📅 09:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
العربیه: ایران و آمریکا به توافق موقت ۴ مرحله‌ای نزدیک شده‌اند
🔴
از تثبیت آتش‌بس و امنیت در تنگه هرمز تا کاهش محدود تحریم‌ها و سپس بحث غنی‌سازی اورانیوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/124948" target="_blank">📅 09:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkYFKnZBOI09B_29-IFQ23cUOCbvx6WWay4fowzwQqoSDrYBxFtMX4zlSmuIiPvptfazYt5HaelMyI5Ep3DyHD-6U3SoRKM60pbeaPNVbEyiUmKPNn838P0S5Iq5wX16B_ZD_fWTeflLbsHum5EtpM7dj4HNxEZLwep8Sz6B2fKVouDV6JUq22DZ3A76jmbghviT5CbNZEOvoEp26ISPcTqg392rJJBYZ-_Ff4pOekVhn-Vj83cMRVsVy4RTHlXZMBYOCslk6erK_4WLEX3SRSUdvBj2Hd-bixskinBC8izbQeiHOfGU2_VFIirTYusz1dE2o3aqLDQAtJQHaq0Cpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: کمک امام زمان باعث شد جنگ ۴۰روزه رو ببریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/124947" target="_blank">📅 07:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81fe9bbd02.mp4?token=NUorB3T_uoUJW84pFiEYcC-d-Tm3Fyfhlw3gHGdKN9FxIN3NSOP0CVKgG5V_mEQhmfaSQSZkcTokmfaCxM9bNS3iDQ9Ai1E7h78zc8Qt_1QL-lrhzZIJIjMmEX0NtpkBOu51KWBv0T-iXNPiMjtiozDw6We9t_wYDA6MAiJLx0HBLHJJqrI0FpgUHYTI3FDGrXss0XTUaj0Bp-OSaIl1Efrz-TwPwBf3EDGyGdz7jaVIwZzR7mumMwULLOu3AtzfXvVPIHDxXcIQ_UbYej11XcCItJ-BWxA14V7DCo_2LuTl7ppBJ0qcNZEx0rFZftSuVXlUv5YuKiYC74LwVw5vpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81fe9bbd02.mp4?token=NUorB3T_uoUJW84pFiEYcC-d-Tm3Fyfhlw3gHGdKN9FxIN3NSOP0CVKgG5V_mEQhmfaSQSZkcTokmfaCxM9bNS3iDQ9Ai1E7h78zc8Qt_1QL-lrhzZIJIjMmEX0NtpkBOu51KWBv0T-iXNPiMjtiozDw6We9t_wYDA6MAiJLx0HBLHJJqrI0FpgUHYTI3FDGrXss0XTUaj0Bp-OSaIl1Efrz-TwPwBf3EDGyGdz7jaVIwZzR7mumMwULLOu3AtzfXvVPIHDxXcIQ_UbYej11XcCItJ-BWxA14V7DCo_2LuTl7ppBJ0qcNZEx0rFZftSuVXlUv5YuKiYC74LwVw5vpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه برخورد یک پهپاد انتحاری به فرودگاه بین‌المللی کویت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/124946" target="_blank">📅 07:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnfOmyVBuFWADmPWlnZRgYdk8yY22QZdzEkZ9F6AXfA3KC8t-wKTyHm8MQNQJIMnEkUoSDQkQs6LwQyBb2szKgrtRi5zOct9tiRoVDnNONbiG60IRXrOKQq-BSeKwchy9gkQ47RsdgRF70cSiD-1n2h2Rz8zGhxL55odqOPx4rTc3mHPdNeVwX2saarxcx1xSO-GW_V01xvHSTrLAp0ZmkwoLCL2k_O616hPVTgpY8IJVA5-dppn52XBlmpaxyeFAYfowRxfggwMnOKENjKErM5ndnthqT2BebI1kA71MJlui5YuytFca0Cp-8v9Cw6MTVsNcqNaI90JzRorw8p8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
📈
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/124945" target="_blank">📅 01:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
🔴
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
🔴
با این حال، این اولین رای موفق…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/124944" target="_blank">📅 01:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=P_AADa0x9kZZRdQY_V8Ezyq93-N399fkGVHtMzQcXee8Eb9yhqG2mFaLCpntcV7Uwndh824J91Kvpm_Ka48Hg2U3WlFX9GexeOQNtrRXn_0ecMkCqKl7LNoFzal_W80QG94cfjlveD4ocMKxeXrFZreLeE0DI0_tol4sNmepNpEedIv9s2RcVNFGnwtRHaTqAyJSstglX6RY3hA9Yx4E_Q5Is2X6nfVNvbbb7UioddbLZh_oMu4-CMPMVoehSI-UIX9h7mNCqG6sM4cn76VDB_dKSwnI-TjaX6J_jYWq14NHIKna2x2lzvmjhMsq47ZznpRE_SCo7WFA1ggDEDvIaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=P_AADa0x9kZZRdQY_V8Ezyq93-N399fkGVHtMzQcXee8Eb9yhqG2mFaLCpntcV7Uwndh824J91Kvpm_Ka48Hg2U3WlFX9GexeOQNtrRXn_0ecMkCqKl7LNoFzal_W80QG94cfjlveD4ocMKxeXrFZreLeE0DI0_tol4sNmepNpEedIv9s2RcVNFGnwtRHaTqAyJSstglX6RY3hA9Yx4E_Q5Is2X6nfVNvbbb7UioddbLZh_oMu4-CMPMVoehSI-UIX9h7mNCqG6sM4cn76VDB_dKSwnI-TjaX6J_jYWq14NHIKna2x2lzvmjhMsq47ZznpRE_SCo7WFA1ggDEDvIaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
🔴
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
🔴
با این حال، این اولین رای موفق مجلس نمایندگان است که قدرت‌های جنگی کنگره را در مورد جنگ ایران تأیید می‌کند و اقدام نظامی آینده بدون تأیید کنگره را محدود می‌سازد.
🔴
چهار جمهوری‌خواه به نفع آن رای دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/124943" target="_blank">📅 01:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYUr7DSJC6G98aur_6uoiyAGKK0lkrGtGUbPt2Gnf2rJ78Ur004Fw7jW2tZMqJ8HIIn08zQcRZnXBnFD9pBMMP4YqpU8bcWFOi2p48IdgQi7PAUHN0pWUcLFT5-CYt6So6eaObJ0pClvSMT5F6WJ9mC2R3W38Zyhj0aOQSLBNdJOmYvKEwVQAaQ4YAS4K_JCFhyR_-RfpLjEdu4eOJQJOfAsJrYV8nR-ox3HUCHRajXPLeZH59yUq-epIw0FXJBSCNdmqXKtq6NsROtxAlouo1Z4ac71BwSXzdtYF-XtoLfn0Y7f_mWHAB4Yv9_TIz42z57Dt6podcxduQa0RDZsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
🔴
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
🔴
‏ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/124942" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=KZHngr_809L_QBlFOBZEOBGVuN2dNif25X8WBvQeFJuCGRdkSJtDvJiBTvYe1DYGn8X-yYe5SXLqQOpm8KYKALyVEPjDPCa4V-JL2k3y4cM4evPKwG1EeJgTspICe-BbfVoEDPB7vW_1ucUQcytiZVVvu7CF__cxAH-jSUtutfT5_4-PYDzEDKvryCD4LiYXsSGjUpC_MRJvkoF_RMwKWO1g2PhuVtRRi-m_ZuBdTQjI4wS0FqPc16PDGvmivrUYbHjXJg3mif-JDeL6wypvrfrwhn21xolOXmByOCJRZoBpqJ-K-rFSxvoPnOIoHl75d0jKwAkmwaLoKsKgaciGvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=KZHngr_809L_QBlFOBZEOBGVuN2dNif25X8WBvQeFJuCGRdkSJtDvJiBTvYe1DYGn8X-yYe5SXLqQOpm8KYKALyVEPjDPCa4V-JL2k3y4cM4evPKwG1EeJgTspICe-BbfVoEDPB7vW_1ucUQcytiZVVvu7CF__cxAH-jSUtutfT5_4-PYDzEDKvryCD4LiYXsSGjUpC_MRJvkoF_RMwKWO1g2PhuVtRRi-m_ZuBdTQjI4wS0FqPc16PDGvmivrUYbHjXJg3mif-JDeL6wypvrfrwhn21xolOXmByOCJRZoBpqJ-K-rFSxvoPnOIoHl75d0jKwAkmwaLoKsKgaciGvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌ای آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در ۱فروردین
🔴
موج انفجار رو فقط ببینید
‼️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/124941" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=puiyJn0e3LLSrtw3vJkAbpAzipFC4A2rlWR2kYuRhaDB7IHig6kt5hXQofkdQLxu85AVr46kpOsUcQyyRM9Ve39E-Y4sW3M0-Kj6tpk_hCvxuGZtJA8lyuXkcc7FKD4jMXHeHlxIqdMge7QxcPcxDeq-AYipWrT46CwLR6aZYVxrLIcA8dsy4aS_-8vtorRGZNrH5JiMtS4oGr81PPemN0_sWhFWQU1NC1MvVugjIUP8XuTXPmVvq0C_JiO3ODH1gWmWmzpgfP6reek6iB6B3oM_U1rCu8sPtni_i1Jk4IIcsujPUUyYy1UVv5VyiRdyeVsECmF0TDjN-MNLSC7WAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=puiyJn0e3LLSrtw3vJkAbpAzipFC4A2rlWR2kYuRhaDB7IHig6kt5hXQofkdQLxu85AVr46kpOsUcQyyRM9Ve39E-Y4sW3M0-Kj6tpk_hCvxuGZtJA8lyuXkcc7FKD4jMXHeHlxIqdMge7QxcPcxDeq-AYipWrT46CwLR6aZYVxrLIcA8dsy4aS_-8vtorRGZNrH5JiMtS4oGr81PPemN0_sWhFWQU1NC1MvVugjIUP8XuTXPmVvq0C_JiO3ODH1gWmWmzpgfP6reek6iB6B3oM_U1rCu8sPtni_i1Jk4IIcsujPUUyYy1UVv5VyiRdyeVsECmF0TDjN-MNLSC7WAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهبازی مجری محبوب صدا و سیما: من سالم هستم و خبر تجاوز گروپ به من کاملا کذبه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/124940" target="_blank">📅 00:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAYhhodljLYwYklSrbp3AREZjIyw-nlDGryNcIT9dDe51j29cjfpth6tm8SqbjuM5o9FjfoCxUxJXXV9gu-dJ8WWbkflciRolzsqApjuZahnasynO95oTEVEC-HwuLfJYqVLRKBn9SimqJbwi8qwoUA4PEmN9jBM7jTh9VOlQXgMaJ04IANT521XwKk8zSM2p74fxx2cZZ4TtwNULmfjIMWJfLKM_cPE_SqTTxuokaoEv7QIq7E-oRfXQ1JZGtUbGJ6aMkA2zvtnjs_OXH3AVWz9aALSk9i4vK3FCKivOtwMxOQ_OITc51GdJgR7xu40WWmb8EPXrPtFarJWCaEboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهبازی مجری محبوب صدا و سیما: من سالم هستم و خبر تجاوز گروپ به من کاملا کذبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/124939" target="_blank">📅 00:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56e67aaa9.mp4?token=QPB23qxExPa928Ldwpg2pSzZibA0QerRmGSI2wHMTE3gKujR67prXX1V3lwuhQ8aRjMXbbITDUm9dFcZF4atq2ZuNzJ-_bdlyTXyMhR31ir1mL5Rju6IAAkm-lWebK6Yu_AOta6XDU-0tLujvDaP3pskwT_RdjXDguB2hAHNPOzSF47gS904ayX3NbGLS91OEBigKoeWIL7l_5cYqT2ijMt9bH78LpGeI3V3YTLFVRlNLceZeOKXZBispYBpzTCNQ2W4I7jVt0r9a0DLZ6DACV6jf2pD5hlAx8fAgG_OTxUiio04tGiH4xu0ZklcPe19oRAvDK0Tt_VjYGP2hBRoBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56e67aaa9.mp4?token=QPB23qxExPa928Ldwpg2pSzZibA0QerRmGSI2wHMTE3gKujR67prXX1V3lwuhQ8aRjMXbbITDUm9dFcZF4atq2ZuNzJ-_bdlyTXyMhR31ir1mL5Rju6IAAkm-lWebK6Yu_AOta6XDU-0tLujvDaP3pskwT_RdjXDguB2hAHNPOzSF47gS904ayX3NbGLS91OEBigKoeWIL7l_5cYqT2ijMt9bH78LpGeI3V3YTLFVRlNLceZeOKXZBispYBpzTCNQ2W4I7jVt0r9a0DLZ6DACV6jf2pD5hlAx8fAgG_OTxUiio04tGiH4xu0ZklcPe19oRAvDK0Tt_VjYGP2hBRoBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمعات شبانه تلفات داد
‼️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/124938" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/124937" target="_blank">📅 00:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6d857c4c.mp4?token=iY8G6ihDphwky3d92J601_9QhHb_sA33bHES0IeocaJSQ2Tiy0za1Ili6Glqu8JmD54gS4F7a88pKPGKptkAd_vjKt97dj1krPD5cZ11WQ8W-RTPdT0MrvYFdHF-UiUdvbeHUqNOl9gWGc1oMeKEACboipp2OCzTNP8gTDywoYHXIe4Gdk8ecNeJds3HPswc544ZSVn45JXbc7HKtRBOkvesgv4DKBbl4x4D3fGBEDEH1crvM123F4whnVl7au7b59sTLxwA01N54mztFLEBGgF0W-JIUjl6_vR2QFBIaVzgE5fzYWY1YofEHeUltIPxiaUTljSASjERhw0V2dj5Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6d857c4c.mp4?token=iY8G6ihDphwky3d92J601_9QhHb_sA33bHES0IeocaJSQ2Tiy0za1Ili6Glqu8JmD54gS4F7a88pKPGKptkAd_vjKt97dj1krPD5cZ11WQ8W-RTPdT0MrvYFdHF-UiUdvbeHUqNOl9gWGc1oMeKEACboipp2OCzTNP8gTDywoYHXIe4Gdk8ecNeJds3HPswc544ZSVn45JXbc7HKtRBOkvesgv4DKBbl4x4D3fGBEDEH1crvM123F4whnVl7au7b59sTLxwA01N54mztFLEBGgF0W-JIUjl6_vR2QFBIaVzgE5fzYWY1YofEHeUltIPxiaUTljSASjERhw0V2dj5Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آلمان برای اولین بار در تاریخ مدرن خود در کسب کرسی شورای امنیت سازمان ملل شکست خورد و تنها ۱۰۴ رای دریافت کرد.
🔴
به جای آن، پرتغال و اتریش انتخاب شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/124936" target="_blank">📅 00:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
منابع العربیه: پیشرفت‌هایی در مذاکرات لبنان و اسرائیل حاصل شده است، اما هنوز توافق دائمی به دست نیامده است
🔴
اختلاف بر سر سلاح‌های حزب‌الله همچنان مانع اصلی هرگونه توافق بلندمدت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/124935" target="_blank">📅 00:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: ما طبق توافقی که با ایران در حال مذاکره است، ذخایر اورانیوم با غنای بالای ایران را دریافت خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/124934" target="_blank">📅 00:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31569798c8.mp4?token=MvpLrcQzRcWlTwTdwQeB50vgWa1H812xWOGUJzvYUdMJQ43xmBkXNf6Gh5sOKcuV1MGzjunkEPdvp_4HWPG6uQbs1-mX6-s2TiKnArH2hY99wWyR3ewJvC8F2cW07hETooIMtGn3oXnc1SJ7OgBKaXLXVCuiTE9fcF2F7kLrxOFWxU8hfj4W3DuuBzU_EprvRRteQfjJ-CUEI5aihnE-DzXDjmBlOrOviFVR7ech_4ZQgeiwaxdy_FvYP-rgzWToWNRayJjs4dhQBXtGGRw7U9s57mm4XIloGGVmhCQH3vNlodLI75J5wa_IbQcHpwVlzPwrGu5XXsjL5LKuKTU0yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31569798c8.mp4?token=MvpLrcQzRcWlTwTdwQeB50vgWa1H812xWOGUJzvYUdMJQ43xmBkXNf6Gh5sOKcuV1MGzjunkEPdvp_4HWPG6uQbs1-mX6-s2TiKnArH2hY99wWyR3ewJvC8F2cW07hETooIMtGn3oXnc1SJ7OgBKaXLXVCuiTE9fcF2F7kLrxOFWxU8hfj4W3DuuBzU_EprvRRteQfjJ-CUEI5aihnE-DzXDjmBlOrOviFVR7ech_4ZQgeiwaxdy_FvYP-rgzWToWNRayJjs4dhQBXtGGRw7U9s57mm4XIloGGVmhCQH3vNlodLI75J5wa_IbQcHpwVlzPwrGu5XXsjL5LKuKTU0yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : تنگه هرمز فوراً باز می‌شه وقتی من یادداشت تفاهم رو با ایران امضا کنم
🔴
تنگه هرمز باز خواهد شد، مین‌روب‌هامون اونجاست
🔴
زیر آب هستن، خیلی خوبن، تکنولوژی‌شون فوق‌العاده‌ست
🔴
ما مین‌ها رو جمع کردیم، بیشترش رو پاکسازی کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/124933" target="_blank">📅 00:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124932">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49eac4e09.mp4?token=lB9oGaXeAdj8cMc4g96iyEP08HEYvu_9Ph6cPoKItiUR4_FAzCR8DDE49Y8brVXJqB_OLNoHmm-QE2alBBsT0Yc5mhhQ47u9K5hq8eTf4HEXW7cdyufvF6P0Rgtl17SfZLpozTeKb8vn94rHzA9p4xcP0VFYQ2UaX-nTE6KYl7DRpi2_Qlb1MVLFN116jN9TjXSJtGwb9xG49Yfm-UcBz-tbYk51qYqdvdzmQlYZPDBcBnkD7jLL5LiGXozyomD15wEi-MCt3TjObFsm7xXBz2zUo4i-YSQt9yWkGCz0-vGoRXChRJnU-buYz4wKtsJdc4x0yeoTixv6YqWHx7Aetw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49eac4e09.mp4?token=lB9oGaXeAdj8cMc4g96iyEP08HEYvu_9Ph6cPoKItiUR4_FAzCR8DDE49Y8brVXJqB_OLNoHmm-QE2alBBsT0Yc5mhhQ47u9K5hq8eTf4HEXW7cdyufvF6P0Rgtl17SfZLpozTeKb8vn94rHzA9p4xcP0VFYQ2UaX-nTE6KYl7DRpi2_Qlb1MVLFN116jN9TjXSJtGwb9xG49Yfm-UcBz-tbYk51qYqdvdzmQlYZPDBcBnkD7jLL5LiGXozyomD15wEi-MCt3TjObFsm7xXBz2zUo4i-YSQt9yWkGCz0-vGoRXChRJnU-buYz4wKtsJdc4x0yeoTixv6YqWHx7Aetw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اگه توافق ایران نتیجه بده، شاید مردم بتونن شروع کنن به ساخت آپارتمان‌ها و ساختمان‌های اداری تو ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/124932" target="_blank">📅 00:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124931">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ درمورد ایران: ایران یک مشکل واقعی برای جهان است و نه فقط برای منطقه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/124931" target="_blank">📅 00:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7717fa1eef.mp4?token=AdKzx89ZKwyxNI9viBwfMozfI3IdNdJC_eEgseht0FwMsT9VqrQ-LLi4FvC4qa4UIHdUrb5ATHae4lMhwwFUYha6LsGo8uaI09WNc4hHSN1pRLIH8WAfDufXB9rrPzxqJDOp8J5I5PaYDIhBJDhwyhylvTOZVvpEf1omC_VTq_ACSId46_HOsbftviXvpg0wEQmoZMHKkBDeHbokwFu8687fGl77KfShoMwXB8jmJiHm_tOfj66fVsLL7F-C3M7w9JFT8t6a36fkj0RXtTeVRE6YEVOj5OeH8RJb6puwDbGqJEp8Yq8mNedYSEsUayYwwKb3J9xautXmoj2Vuz-HJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7717fa1eef.mp4?token=AdKzx89ZKwyxNI9viBwfMozfI3IdNdJC_eEgseht0FwMsT9VqrQ-LLi4FvC4qa4UIHdUrb5ATHae4lMhwwFUYha6LsGo8uaI09WNc4hHSN1pRLIH8WAfDufXB9rrPzxqJDOp8J5I5PaYDIhBJDhwyhylvTOZVvpEf1omC_VTq_ACSId46_HOsbftviXvpg0wEQmoZMHKkBDeHbokwFu8687fGl77KfShoMwXB8jmJiHm_tOfj66fVsLL7F-C3M7w9JFT8t6a36fkj0RXtTeVRE6YEVOj5OeH8RJb6puwDbGqJEp8Yq8mNedYSEsUayYwwKb3J9xautXmoj2Vuz-HJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:در آن بخش از جهان، آتش‌بس زمانی است که شما به شکلی معتدل‌تر تیراندازی می‌کنید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/124930" target="_blank">📅 00:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: توافق فعلی، در صورت حصول با ایران، نقطه مقابل توافق قبلی امضا شده توسط اوباما خواهد بود.
🔴
محاصره ایران شاید شدیدترین باشد و نتایج آن بسیار قابل توجه است.
🔴
این توافق مورد انتظار مانع از دستیابی ایران به سلاح هسته‌ای خواهد شد و تنگه هرمز پس از امضا به سرعت بازگشایی خواهد شد
🔴
می‌خواهم موضوع بازگشایی تنگه هرمز را از خصومت‌ها و تحولات جاری در لبنان جدا کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/124929" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ: سی‌ان‌ان یک سازمان بسیار فاسد است، با یک خبرنگار فاسد که درست آنجا ایستاده است. هرگز لبخند نمی‌زند. زنی جوان و زیبا، هرگز لبخند نمی‌زند. من هرگز لبخندی بر صورتش نمی‌بینم. او را می‌بینم که با نفرت در چشمانش ایستاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/124928" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124927">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: آتش‌بس در لبنان با آتش‌بس در سایر نقاط جهان متفاوت است
🔴
اگر توافق کتبی امکان‌پذیر باشد، ما آن را ترجیح می‌دهیم.
🔴
ایران موافقت کرد که ما وارد شویم و اورانیوم غنی‌شده را بیرون بیاوریم اما سپس موافقت نکردند.
🔴
نیروهای ما آماده‌اند، اما بهترین گزینه رسیدن به توافقی با ایران است که بدون کشتن همه، به همان نتیجه برسد.
🔴
ما برای اولین بار با حزب‌الله صحبت کردیم و آنها موافقت کردند که به اسرائیل شلیک نکنند
🔴
ایران علاوه بر اسرائیل، به ۵ کشور در منطقه موشک پرتاب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/124927" target="_blank">📅 00:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124926">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها به امضای اسناد نزدیک هستند. اما برای رقص تانگو دو نفر لازم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/124926" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124925">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ : شی‌جین پینگ برای چین خوبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/124925" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124924">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=ZJO0udzzctW6Ose3YlP8NPgE_84b0rsFT-eS9j3ok__NihoZ52SybFR_cgG3bkDathIe2fDkwZitVEpXMHGhM-i1NtzxAxCKhvOd1_0dkA0TNFb1hqg1siIqzrHMNBFj5ssDKufcSni5w5Cj1cKsbK2n3Nfgswp04thgPzIjtAtz9DLcoOqXxVKktHMzn-x6M8PtfMy6HG1JG9p0SxBjHdzxNzOyO3Y979NL_kgqI0PQ-96xB0jxyhpZO4a2BHcdMAUZFC7F_bmU5iy9zTatzuUNu0u9-p5zipx3Pwr2jEkjP-YuCiQoFtyx6Q11JeRJyhnnWNAeQYWLGaaintwIHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=ZJO0udzzctW6Ose3YlP8NPgE_84b0rsFT-eS9j3ok__NihoZ52SybFR_cgG3bkDathIe2fDkwZitVEpXMHGhM-i1NtzxAxCKhvOd1_0dkA0TNFb1hqg1siIqzrHMNBFj5ssDKufcSni5w5Cj1cKsbK2n3Nfgswp04thgPzIjtAtz9DLcoOqXxVKktHMzn-x6M8PtfMy6HG1JG9p0SxBjHdzxNzOyO3Y979NL_kgqI0PQ-96xB0jxyhpZO4a2BHcdMAUZFC7F_bmU5iy9zTatzuUNu0u9-p5zipx3Pwr2jEkjP-YuCiQoFtyx6Q11JeRJyhnnWNAeQYWLGaaintwIHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : آتش‌بس رو چطور تعریف می‌کنید؟
🔴
ترامپ : تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/124924" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124923">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae195d9e59.mp4?token=pU_yuEKUaF7gudOhEpACUi3IM387USMV682YUzsQzPaFgTYKqcfm22jVVa3Dv2yzzSx0GI2Qk4zeBwKBZpj3ytqxXgy6vA2TA1kn8SvYRp6DOm8w9iaXdOjEP0uQ1Zz3IJQc42Lz98POozzo8uoufhcMZ_w9wVCxwDU9QDuPG9swQ4I4yJDnRV1O-CtIsdEjdDWOc2NKXwuoZjrhqaBOczykX1RO8udeoXsGi2GDCHx4eacqYL1zkeDVzcIsiufsOqRifulqFgnAYnnyhyCpttzSs2hp4PuYEoCALHFfTDHsDyH9G3lBXQcbQ6syJLJFIOJfxCALBx9R9oo2YNagTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae195d9e59.mp4?token=pU_yuEKUaF7gudOhEpACUi3IM387USMV682YUzsQzPaFgTYKqcfm22jVVa3Dv2yzzSx0GI2Qk4zeBwKBZpj3ytqxXgy6vA2TA1kn8SvYRp6DOm8w9iaXdOjEP0uQ1Zz3IJQc42Lz98POozzo8uoufhcMZ_w9wVCxwDU9QDuPG9swQ4I4yJDnRV1O-CtIsdEjdDWOc2NKXwuoZjrhqaBOczykX1RO8udeoXsGi2GDCHx4eacqYL1zkeDVzcIsiufsOqRifulqFgnAYnnyhyCpttzSs2hp4PuYEoCALHFfTDHsDyH9G3lBXQcbQ6syJLJFIOJfxCALBx9R9oo2YNagTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : با توجه به حملات ایران به کویت، آتش‌بس با ایران هنوز سر جاشه؟
🔴
ترامپ : ببین، برای هر چیزی یه دلیلی هست. ما شب قبلش بهشون حسابی ضربه زدیم، حتی دیشب هم همین کارو کردیم.
🔴
(بقیه حرفاش به خاطر مشکل صدا قطع شد)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/124923" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124922">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: ترجیح می‌دهم ایران را نابود نکنم، ما میتوانیم ۲ تا ۳ هفته دیگر ادامه دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/124922" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124921">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ: پریشب و دیشب به ایران حمله کردیم، ضربه خیلی محکمی به آنها زدیم
🔴
شنیده‌ام مذاکرات با ایران خیلی خوب پیش می‌رود، اگر توافقی با ایران حاصل شود، می‌تواند آخر هفته انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/124921" target="_blank">📅 23:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124920">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJ5ZfBj_xWSxM0nyw06ntTauAxGD8ybUxm6C6C4Xqqc996Dx7CVHN0helTeqJoUAcaDzdr8N6-MNoqjoW9_9y8TEzizGS6pTPDqekckXqZEnwDeG4YcPsq8yCTL-c5AYC32g57duynDBQdjDUehdy9ol3RkMgXOFuSw_ij1QQI7hRDRZ6DRqEx4fg09REZgXxBtEEhE5jblGe-W5X44vOiFt6hEB77u1xP1MFCH1lLE4TMEvh5wZrhiClv8jD5OvblylM6f_HxihMIsWk9AZqa6sb6Vcdd5DfhpKkVJmXQn7eOr6I24absHntx4HQ-XmPljCp15K9ZT_yReoXuk70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتریوم به زیر 1,800 دلار سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/124920" target="_blank">📅 23:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124919">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نیروی دریایی ارتش ویدیویی منتشر کرد که نشان میدهد موشک‌های ضد کشتی به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک شده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/124919" target="_blank">📅 23:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
گفت و گوی ترامپ با امیر قطر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/124918" target="_blank">📅 23:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu5mdFzM52o11ilF5oidPuu0oxdZ0XNcA10M0z7HZPSaOzr0mLA8R2m43Es5ES-MOrqAOFdM-pVUQCKJGvKuNLMLZwkLqbnPFWnXC9u3GXju-DDU40NrJbuWKjVw4CUAoLjJGCUu_-cVtAcEOpQpnqRhIO4S6uIEzpAVR_KkBLoc9-VVfY09AHQ-ou_UnhSkOdK1iGvMNhPwDU-ej8NggzfvN24CCuO9R7GyM2fYMiQpveZa7ETuDG9RjJH1PS_uq2Tn2-T0TDmfI5u8wjW53ZF10ETV40uohV15Zg2X4q4XJQ6RbOiuZQQ0jmLmgyszsatyHQujvMsR7XCmNcYl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای واشینگتن تایمز: دفتر بازرس کل وزارت دفاع آمریکا در حال بررسی عملیات خشم حماسی، کمپین ایالات متحده علیه ایران برای از بین بردن تهدید هسته‌ای تهران، است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/124917" target="_blank">📅 23:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124916">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQtLAkZZx3_8uApRHhWm0cG6-hy3msXYNoTioLsXnrEaFonkQ7Kaw1IMgEdvnh6o14KZwZUTX-w5hdfg28K96yPx1GF2WKp7njuedh1Pn9chdSrUBGlskt9ygyahV-O4tPgXSv365vLiGyQtrLU_jBFep7i4kxc9Et9JuKZpB64uxgjXUyBIKQtLJgAZDYgE_ST2O3v4kHBWkt6SglmIWwjg17X2ALhZl3Q6LQ5MplxQJWmgN5JAHahRXi4t19SHhRi_jbpXLm6yTiqA0APo_PD_plb7hLLXg0hFfc2N2CF7HRv02M5Wxv3U8d1FLvZFoLfnTJz9ggW-CnunT6ZiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: ترامپ مدعی شد ایران موافقت کرده که سلاح هسته‌ای نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/124916" target="_blank">📅 23:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124915">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQUwg1GV-jeBbU8AW9O87ggWYJLl415Ll3b7B1DPRsyoQJyZrxnI9ek46DjPLPbymImQkO-o7vvBUeC8HHmqXvhdn1RwO6Y5-_p7R6X1HxBizDmPrMt-ZWT_0KFX2iqZJgzkWOGyiNBWEbkKKSHVjmI5DykY_T1S53cP1MkBXkx0KXdfiT9qmOLXpmCBXSlea2S_JpYd4bGJbg2LmzX3ITolLKRlgJpW0cIDa6ozc4icECT6jRZA-aC_Aa7CmS3pGAuxfjESK1oH8lV-ZNCrKLuiCP21pBD7RlKFGp3Ydlejhds-9HKnFssNmLySjK3LaWpVA-wuskXzp84Ffe1Lvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من بلافاصله پس از رویداد UFC در کاخ سفید به اجلاس G7 در فرانسه خواهم رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/124915" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
صدای انفجار در بحرین واربیل واقع در اقلیم کردستان عراق شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/124914" target="_blank">📅 23:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سخنگوی سازمان بهداشت جهانی:
ما در کشف وسعت شیوع ابولا در جمهوری دموکراتیک کنگو بسیار دیر عمل کردیم
🔴
نوع جدید ابولا به واکسن‌های قبلی پاسخ نمی‌دهد و ما در حال تلاش برای یافتن راه‌حلی برای آن هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/124913" target="_blank">📅 23:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزارت دفاع: با تمام توان در مسیر تقویت بنیه دفاعی کشور، توسعه فناوری‌های راهبردی، پر کردن هرچه بیشتر دست نیروهای مسلح و صیانت از امنیت، استقلال و تمامیت ارضی جمهوری اسلامی ایران گام برخواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/124912" target="_blank">📅 23:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/124911" target="_blank">📅 23:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124910">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cL8e0yEI5zZh85UAPezglKly4vvdJxd_Sdmtlke0JQTg2wDV6jWFQD56y-tlofHI9SLWCxrKu562MzJliT6JJuRh8wvRGEbfl0M8DyO8xzkE35Xe1be8BBShOAlpElH08iWUVdcTMzXl_p8O4Qsj6Ea0UmLepjaOw22jzHVQ3onYuY9tYdICPfdLpKluaLgrtdEio72o8k7NNCmk4XTjaEtzmJ2_QMCcfbCwlBK68-CyfI1-tPoJ4dofAwOVQ6J1_rpUPaWwQjsQ9muNgahR6QEPNxKWPxhRa9KFllyaWRkc_ELw3Udyv1tcpmvs4gCVru3lD4KzBIVgPQZQx0HQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/124910" target="_blank">📅 23:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزارت کشور بحرین به دلیل خطر احتمالی آژیر خطر را فعال کرد و از شهروندان خواست به نزدیک‌ترین مکان امن بروند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/124909" target="_blank">📅 23:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHIRUgqu-2o9KbTZeK0PQ-td97iqVQ9zoZNrlTP0Hb61XDMT8UGy_XwMnCg975IZef0XfaFqJqftWosza28WRIjG59DIUKw9sZCSXLrbOmfJGqM-yUak274U3Ni3QN8Zz0VLIUKv75qM0B_RUKOIZBq243WYmTVt_gFeZqLwtwu4UgrnliO9XY8Hpp3U7BJ_TtUxAADGq2NuAqW_jynumbLklUNvwxU70l0Hyiy1hd6yN2D6bwqCoG1nQPBdANOmkPYeKAPVtcZouJVDRB-jvgUrMcoA-vJbrEoVZXvjxDI6LIKgbrsFGRvayTPhxxNJyZiMwKRyBV7wKy-qnWwIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس:  یک مقام آمریکایی گفت مذاکرات اسرائیل و لبنان با میانجیگری ایالات متحده هنوز در وزارت امور خارجه ادامه دارد.
🔴
این مقام آمریکایی ادعا کرد: «مذاکرات به کندی آغاز شد اما سپس پیشرفت قابل توجهی در مورد یک طرح عملیاتی حاصل شد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/124908" target="_blank">📅 23:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
صدای انفجار در بحرین واربیل واقع در اقلیم کردستان عراق شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/124907" target="_blank">📅 23:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نیروی دریایی ارتش ویدیویی منتشر کرد که نشان میدهد موشک‌های ضد کشتی به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک شده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/124906" target="_blank">📅 22:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سخنگوی سپاه: تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/124905" target="_blank">📅 22:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghEI1FFi5mRIjgUhep69pUpXwBzwQP46x4o4K1of_-TfvlfB_QDpBWeo8WSCrGoD4VOZcVi0_6zxZO99Z4OubBCLc-F8dUPahwTgT2CcLw3MesxEbhvaeS1bWdr3xAPlNY8ZdZLPrwLWYg_HYqam8efKj6aX1R0gak1TF4FAuIIJTA5S_BsFyuQVZWQ5Hzx2mCkJib6X5SElXbBUiRas5EOreOe5mb8XLeIOU7ZDQDBprC7z7F0M9AqEG766ziiqvaJpC_kPkYlXr_4o-xbXVGuJaYXZ5imPh1o6uj_qNExL5VYB4TdRDezv8vkggvckLAiMBNf_d2ifruZ_40ladQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌‌ان‌ان : غرامت مالی یکی از اصلی‌ترین گره‌ها و نقاط اختلاف توی توافق با ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/124904" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cfe5e8eca.mp4?token=lOjPK095h5_goA2NWgXVV6xA8vZXTOLu3xXMoJnLBMiHBNuvbmkXKTMz1USO8i5ZrjCtfhXZfBW5LOqLlEuhs_xOelgZhr8wpAcWiL46HzGg2eaYZnYsyAE0pvViu-KQGrDkDL0FPF7tzfLMSDQ-6zAq4Qfq4f4xmaacfpuJgJX5bbPTpkB5SKhxrR5gbFAHvtws5WwvcIDRv9iM1V6hc5zezfTfaEL8dGNUwM5eS9WZOoIjlFtctNU7VS_MhN8KIemwWdEzgk7YUQutHecnOqS5qmi5W_lHKWCE2JpJkbROC1t2C0fj372tIUSnqDo7PIzj1-PYVaCkikw8QB4kWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cfe5e8eca.mp4?token=lOjPK095h5_goA2NWgXVV6xA8vZXTOLu3xXMoJnLBMiHBNuvbmkXKTMz1USO8i5ZrjCtfhXZfBW5LOqLlEuhs_xOelgZhr8wpAcWiL46HzGg2eaYZnYsyAE0pvViu-KQGrDkDL0FPF7tzfLMSDQ-6zAq4Qfq4f4xmaacfpuJgJX5bbPTpkB5SKhxrR5gbFAHvtws5WwvcIDRv9iM1V6hc5zezfTfaEL8dGNUwM5eS9WZOoIjlFtctNU7VS_MhN8KIemwWdEzgk7YUQutHecnOqS5qmi5W_lHKWCE2JpJkbROC1t2C0fj372tIUSnqDo7PIzj1-PYVaCkikw8QB4kWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی ارتش ویدیویی منتشر کرد که نشان میدهد موشک‌های ضد کشتی به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/124903" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فارس:
نیروی دریایی ایران چند ساعت پیش یک «مرکز فرماندهی و کنترل» ارتش آمریکا را روی یک ناوشکن آمریکایی که قصد داشت به آب‌های ایران در دریای عمان نزدیک شود، هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/124902" target="_blank">📅 22:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عراقچی: لبنان در این جنگی که توسط آمریکا و اسرائیل به ما تحمیل شد هزینه داده است و ما هرگز مردم لبنان را فراموش نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/124901" target="_blank">📅 22:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHTIWlL2JUX-WZIp_T_Nac10iO0Y0Od1qRtKalf5c5xm65lMIYmL9Zyl4RlILxzRRjuk94_TPZIeQNpILzV94STTCr6NcXwyR8yKPSFoGm-ybUUIiRELVM4gJ8FPwWI_IVBx7gdZnotOyIwaH7-y9-QopIvNPQLIKsJIvAAPAdfHp56pO2xO_x5IZZffhaPEvGCmv5tWoBTxCepqb8ONN_xHbx4xeXGIKfztH_gk4yZ7i9Uwol6mgIc2ClWorrzbLXT6v2MPB5Fw1kQb8WJ9Qf-HhU8yzkHntZNMKwjChw9s6QPc-xMEIFR3W16w9RY6GW4LlrO0wTP9nBnUGNdm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تاج: ویزای آمریکا را هنوز نگرفتیم
‌
فیفا گفت در نوع خودش خاص است که ویزا صادر نشده است.
اگر در مکزیک حاضر نمی شدیم برای رفتن به کمپ تیم ملی در آمریکا به مشکل می خوردیم.
به دو نفر از اعضای تیم ویزا داده نشده است
@AloSport</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/124900" target="_blank">📅 22:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124899">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">💔
جاویدنام شایان شکاری ۲۰ساله از رشت
🔴
‏توی کوچه با موتورهاشون این بچه رو دوره کردن و با گلوله به کلیه و لگنش شلیک کردن، بعد انتقال به بیمارستان ولیعصر و عدم پذیرش توسط بیمارستان به بیمارستان رسول اکرم منتقلش کردن اما در اثر شدت خون ریزی ناشی از پارگی عروق و شریان اصلی رگ جاویدنام شد.
🔴
دانشجو، ورزشکار، عضو تیم ملی تکواندو نوجوانان ایران و دارنده ی مدال نقره ی آسیا
🤔
عرزشی حرام زاده این تروریست بود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/124899" target="_blank">📅 22:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
عراقچی: ترامپ اگر عاقل باشد، هرگز به جنگ باز نخواهد گشت
🔴
اگر ترامپ با عقلانیت حکومت کند، هرگز به جنگ باز نخواهد گشت.
🔴
پایان جنگ در اختیار دشمن نیست و هرگز نخواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/124898" target="_blank">📅 22:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo_b9kEuklqLpDq1eNKCGMak87Zy6MVgXXATOW9Sqx4khpa6Z4gh68beD282Atol6tOt6Hm1ncrmSRF25twwsEyUwQGC7DYll2vbGt5LzCZa8qtDrlmsoMeZNUcEMI8raSCAh62_OlsztdE9MtHOZu6i2yP8JEwq318TrqUkDFUAe9AAJY-3QiKiucQPPFeUSXd5lJtpWimupoQKq9vtg5Y-QlTsMpXLQrE8slsLTNx6uaGNGIFACGqHK6Eh9DpmgrozEKybQQcd61uddhlg-rJmZBy0nO8JgGCArz_sAOOXl4NEHfiIiQDto8qUocmSbySNGk5TuHgO2b-8OAw0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/124897" target="_blank">📅 22:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
عراقچی: وضعیت نظامی ما اکنون بسیار بهتر است؛ چراکه توانمندی‌هایی ایجاد کرده‌ایم که در زمان جنگ در اختیار نداشتیم و صنایع نظامی ما به شکل چشمگیری فعال شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/124896" target="_blank">📅 22:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عراقچی: تماس ها با طرف آمریکایی قطع نشده ولی خب پیشرفتی هم حاصل نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/124895" target="_blank">📅 22:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
عراقچی: آنچه جنگ را در دو روز گذشته متوقف کرد، در درجه اول توانایی مقاومت لبنان و توان نیروهای مسلح در ایران بود.
🔴
در زمان حمله نیروهای اسرائیلی حومه جنوبی بیروت، موضع قاطعی اتخاذ کردیم و نیروهای مسلح آماده پاسخگویی شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/124894" target="_blank">📅 21:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
عراقچی: لبنان را کشوری برادر و دوست می‌دانیم.
🔴
ایران هرگز به دنبال مداخله در سیاست داخلی لبنان نبوده است.
🔴
ما دیدگاه‌ها و ملاحظاتی داشتیم که آن‌ها را بیان کردیم و حزب‌الله بخش مهمی از ساختار سیاسی لبنان است.
🔴
در آتش‌بس، از نخست‌وزیر پاکستان خواستم که عبارت «به‌ویژه لبنان» را در هنگام توقف جنگ در همه جبهه‌ها درج کند
🔴
امروز در مذاکراتی هستیم که برای دستیابی به یک یادداشت تفاهم با آمریکا انجام می دهیم که اولین مورد آن پایان جنگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/124893" target="_blank">📅 21:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679be3bc8a.mp4?token=en0c8qCxHPHDa4UquQvTJK-udpz3n7q09Kb1F6Dh-rE17j9QYjPtLn9Rg985QhCRAEkzz73FRjVGQSUl89Zd0khMffRAOTgcKk7EvqwG_7q8jkQ1mKjeStpSxFSE3NfTJJqj_J6MSjFmUQP6hwfJDaUmjp-6ALtDG4n7BbbZat54XRL1suWj_WJ-WhmZGXrP4i0NyOwlWVJW_RjcuhKKxsQQmvwrtFK3NIRmMeWlW5XL2-af9Km59Qm_R1pWqghesF3Tqft-HrTaadsZXOY8JNHiNsa7_owjko0v32uTEPK2psTeqj4KLOCgBznAv0n9NaVbf02tPAWCJ3LeQfzSMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679be3bc8a.mp4?token=en0c8qCxHPHDa4UquQvTJK-udpz3n7q09Kb1F6Dh-rE17j9QYjPtLn9Rg985QhCRAEkzz73FRjVGQSUl89Zd0khMffRAOTgcKk7EvqwG_7q8jkQ1mKjeStpSxFSE3NfTJJqj_J6MSjFmUQP6hwfJDaUmjp-6ALtDG4n7BbbZat54XRL1suWj_WJ-WhmZGXrP4i0NyOwlWVJW_RjcuhKKxsQQmvwrtFK3NIRmMeWlW5XL2-af9Km59Qm_R1pWqghesF3Tqft-HrTaadsZXOY8JNHiNsa7_owjko0v32uTEPK2psTeqj4KLOCgBznAv0n9NaVbf02tPAWCJ3LeQfzSMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده مک‌براید: فرض می‌کنم می‌دانید گرینلند بخشی از دانمارک است؟
🔴
مارکو روبیو: فعلاً همینطور است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/124892" target="_blank">📅 21:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / کانال 12 اسرائیل :ایران پیامی به آمریکا فرستاد که هر حمله‌ای به بیروت منجر به شلیک ده‌ها موشک به اسرائیل خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/124891" target="_blank">📅 21:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی سپاه: تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/124890" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
روسیه: ایران بارها اعلام کرده در پی سلاح اتمی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/124889" target="_blank">📅 21:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb6a3f5f2.mp4?token=dll2s2toZa92HBN9AEt5WotMyzfCBBpw6ukr-LmItKmARcWygOpTbZS-BvCdZZ5y--3J9G-vlxVV2YaF6AZW2MiTd--W7xl0bq971-BhX1dSEVmOavalz1BdHm0k09OSeY-1yPt4BtwCBrgMbd81aMEe88b8Bc_zuILDyVckjijVnp3a8c94ujFnLS8PQQI10GdthJTle8Jv3dQEzGicidc33suXoeEB7kgTAVVctBTwm7ZdSCnUDFOsSXGSm0xGbjRwpGQkZgxwnUz0wPfbbwz5VVnVtv4LEaAwTVXVLxo4z1VXIgN2FrmDId1xIByWcBR6MqcdjEy0V4ajRZtY4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb6a3f5f2.mp4?token=dll2s2toZa92HBN9AEt5WotMyzfCBBpw6ukr-LmItKmARcWygOpTbZS-BvCdZZ5y--3J9G-vlxVV2YaF6AZW2MiTd--W7xl0bq971-BhX1dSEVmOavalz1BdHm0k09OSeY-1yPt4BtwCBrgMbd81aMEe88b8Bc_zuILDyVckjijVnp3a8c94ujFnLS8PQQI10GdthJTle8Jv3dQEzGicidc33suXoeEB7kgTAVVctBTwm7ZdSCnUDFOsSXGSm0xGbjRwpGQkZgxwnUz0wPfbbwz5VVnVtv4LEaAwTVXVLxo4z1VXIgN2FrmDId1xIByWcBR6MqcdjEy0V4ajRZtY4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیرو زمینی اسرائیل تصاویری از تخریب یکی از روستای های جنوب لبنان منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/124888" target="_blank">📅 21:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
جروزالم پست: کویت پس از حمله جمهوری اسلامی به فرودگاه کویت، دو دیپلمات ایرانی را از کشور اخراج و کاردار تهران را احضار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/124887" target="_blank">📅 21:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ccd72fe8.mp4?token=ABvxaspZ4AoPH2mo6ktnh-dB5jv1dkcSiOkS3GmdHxwIbACWXMZyUCMSzlG6tP3hD3p5sDbaYrjUJ4KGQduJblDXBJAKcrCXvaNMLQHAe0MRC7GDcB-LRUOxOB6wj0Hj41mi2EUz38e2x7ZTB1ApyRY2PUpmqm3_5p8KpQzKeDwDBm0xRemrhXvu2FukICgGZ5cXr736Obuc7gaGh9X-RS2qZtbu2HEjnmDFsPAlbjoiQzAXExFNZ4JANyrsV3Hz-bYV7pdPO-rd8dc-UjbQcNrjFlT2DzoDWa-_KQgSbZtxdqgy33NY9xX6odOx_fGcYH3UIGTCaxV9cDjr4-cxeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ccd72fe8.mp4?token=ABvxaspZ4AoPH2mo6ktnh-dB5jv1dkcSiOkS3GmdHxwIbACWXMZyUCMSzlG6tP3hD3p5sDbaYrjUJ4KGQduJblDXBJAKcrCXvaNMLQHAe0MRC7GDcB-LRUOxOB6wj0Hj41mi2EUz38e2x7ZTB1ApyRY2PUpmqm3_5p8KpQzKeDwDBm0xRemrhXvu2FukICgGZ5cXr736Obuc7gaGh9X-RS2qZtbu2HEjnmDFsPAlbjoiQzAXExFNZ4JANyrsV3Hz-bYV7pdPO-rd8dc-UjbQcNrjFlT2DzoDWa-_KQgSbZtxdqgy33NY9xX6odOx_fGcYH3UIGTCaxV9cDjr4-cxeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خودش را یکی از برترین نوابغ تاریخ آمریکا نامید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/124886" target="_blank">📅 21:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGTkM62xjTr-5rnFu1d897uxDNoYM4df91OKBnRcCP6yVAnNrLsMnctsdqglk1tleBjFcPhLhlyKR3DU6qooijeWZ8Uxc2Gon3-oC_h-vyuit6LHpLY0fDERTRMPJGos77gTiZcry2nOdJLGamN0q53oWSCFNDInlP-Y2hQ5aU1QIGJTEj11IrNijAUn9SFwCDLt-oJ5gQHpiMMKEmE4dXrFpwJMHrumtOKuvs22sUWz9SAb9qQ2iv1K_Tc9SUUNIIBispk_jPg-2PhH-LGH6X3z3bpGMgzqoojCMA4J9GB7q1iB0ZHjTrDdE7LZvxc0NsBfnOXjVAcKSzxWoTc2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دست‌کم ۴ فروند تانکر سوخت‌رسان نیروی هوایی آمریکا اکنون از تل‌آویو و پایگاه هوایی شاهزاده سلطان در عربستان سعودی به سمت خلیج فارس در حال حرکت هستند. قرار است این هواپیماها به دو تانکر دیگر که هم‌اکنون در منطقه فعال‌اند، در کنار یک فروند آواکس E-3B نیروی هوایی آمریکا ملحق شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/124885" target="_blank">📅 21:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ: غنی سازی 60 درصدی ایران هیچ توجیهی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124884" target="_blank">📅 21:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
عضو تیم رسانه‌ای در تیم مذاکره‌کننده ایران: دلیل عدم موفقیت مرحله اول مذاکرات اسلام‌آباد، امتناع ایران از ورود به مذاکرات هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/124883" target="_blank">📅 21:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124882">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2ff479d5.mp4?token=oOI2pW62YTEYmpehU5U_vzGbWu0MeR4G6jM6osTHOcXFnREjPP5RL8YerN80uYyQ3de6bWf5zWTSNJFgzg8F5UhVn28m7aDZ1d52ThFCkXSNwl1xMlfs5GCRnTdV9I4l3Am8ImpeQmd_LbmjyjojB8tayFKDytcwpK8qpxlAjqLQg1qu7i9KZ5Aaf4hMzygFPeRM3me4CtQ8T6WhuGpx7VS1kGmLGvpuurOtb4dWFWtFTM6mT0eYducXsFtBIzqW94olkn3nselPLAXX4OXq9BDYptbUp2YlCwOxWC9Nf2FVw1dbUGB5TV9SvluaLDqEKvcvm6Or6ABk6_ZtFIbecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2ff479d5.mp4?token=oOI2pW62YTEYmpehU5U_vzGbWu0MeR4G6jM6osTHOcXFnREjPP5RL8YerN80uYyQ3de6bWf5zWTSNJFgzg8F5UhVn28m7aDZ1d52ThFCkXSNwl1xMlfs5GCRnTdV9I4l3Am8ImpeQmd_LbmjyjojB8tayFKDytcwpK8qpxlAjqLQg1qu7i9KZ5Aaf4hMzygFPeRM3me4CtQ8T6WhuGpx7VS1kGmLGvpuurOtb4dWFWtFTM6mT0eYducXsFtBIzqW94olkn3nselPLAXX4OXq9BDYptbUp2YlCwOxWC9Nf2FVw1dbUGB5TV9SvluaLDqEKvcvm6Or6ABk6_ZtFIbecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیامدهای سقوط هلیکوپتر نیروی دریایی سلطنتی در دوون اوایل صبح امروز.
🔴
سه نفر از پرسنل نیروی دریایی سلطنتی بریتانیا در جریان سقوط هلیکوپتر حین یک تمرین آموزشی جان خود را از دست دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/124882" target="_blank">📅 21:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124881">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2236543d19.mp4?token=qiQMLkBfkz0y0uRRdjKup1fRADTLngw2NO5vbn9Xe5gFZffwxD4dATRJyoPzttyIvrE5LPMHwPdOLhmfFseSp3gsWwtX8x59Ex_6QEatWLFQljgKJ0rdcyJRpQyR0nsjU93zaaCp-jgpANRzIWpxyU-2n9qh_x8FNESTi4zvNsTY0d9VXUBNZ0xO-bRdFEtdmHfxW42iyMQ2tAzE9n2IRD8eqzOwXMdABSquo5IYrnFwvT1ApGeHeSWTK8Nx13RLyxUADal0j_t1-778chTAUICGwUa7qMOpfKAeZXgTJo13BiGzwbM2LYKHYYjoz8pFbBGAMxLnoCFdiandLjWXCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2236543d19.mp4?token=qiQMLkBfkz0y0uRRdjKup1fRADTLngw2NO5vbn9Xe5gFZffwxD4dATRJyoPzttyIvrE5LPMHwPdOLhmfFseSp3gsWwtX8x59Ex_6QEatWLFQljgKJ0rdcyJRpQyR0nsjU93zaaCp-jgpANRzIWpxyU-2n9qh_x8FNESTi4zvNsTY0d9VXUBNZ0xO-bRdFEtdmHfxW42iyMQ2tAzE9n2IRD8eqzOwXMdABSquo5IYrnFwvT1ApGeHeSWTK8Nx13RLyxUADal0j_t1-778chTAUICGwUa7qMOpfKAeZXgTJo13BiGzwbM2LYKHYYjoz8pFbBGAMxLnoCFdiandLjWXCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون| رعد و برق در غرب استان تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/124881" target="_blank">📅 21:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124880">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فاکس نیوز:  «جمشید غومی»، مدیرعامل یک شرکت فناوری در ایالت کالیفرنیا، به اتهام تأمین تجهیزات برای برنامه‌های هسته‌ای و نظامی ایران بازداشت شد؛ وزارت دادگستری آمریکا این خبر را اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/124880" target="_blank">📅 20:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124879">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نتانیاهو : با هم انجام دادیم، تو نزدیکی و همکاری‌ای که قبلاً هرگز نداشتیم
🔴
باید دوباره بگم، رئیس‌جمهور ترامپ بهترین دوست اسرائیل بوده که تا حالا داشتیم؛
🔴
هیچ‌وقت چنین دوستی تو کاخ سفید نداشتیم، او از همه جلو زده، و این شراکت خیلی قوی
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/124879" target="_blank">📅 20:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124878">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc68640c6.mp4?token=Fompo1x1qfjh9-6cfqOcinCY_gj4NNuRnkHUipJQI3nZMw_vu3zkV_22qhznm-aHW7fvOQe8L4VAKVenBGjRtNDnS2zscPSN6lZB2XTVrkUa3-f55wpB6RfeCilUbGNt71fSzAIEfkhmuTbw9bNByR50AB98kjnQfCVRF7qLIAaHb4UdfBEALWk-e193cobum-hpVyGfJSrM2Bif1rXQ2M2oa0kiN1fLj6i2A95XrqsrpBbyqpIESf7qyxcpAgyIKf0K0MK8glr69H7rnb1FuZDO-oJMZ86OVLkrJjwkUNuNoz5FOJKiCCMbW6WFmdtKFvSEUGK9G8u9rSAm0N1Omw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc68640c6.mp4?token=Fompo1x1qfjh9-6cfqOcinCY_gj4NNuRnkHUipJQI3nZMw_vu3zkV_22qhznm-aHW7fvOQe8L4VAKVenBGjRtNDnS2zscPSN6lZB2XTVrkUa3-f55wpB6RfeCilUbGNt71fSzAIEfkhmuTbw9bNByR50AB98kjnQfCVRF7qLIAaHb4UdfBEALWk-e193cobum-hpVyGfJSrM2Bif1rXQ2M2oa0kiN1fLj6i2A95XrqsrpBbyqpIESf7qyxcpAgyIKf0K0MK8glr69H7rnb1FuZDO-oJMZ86OVLkrJjwkUNuNoz5FOJKiCCMbW6WFmdtKFvSEUGK9G8u9rSAm0N1Omw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : با هم انجام دادیم، تو نزدیکی و همکاری‌ای که قبلاً هرگز نداشتیم
🔴
باید دوباره بگم، رئیس‌جمهور ترامپ بهترین دوست اسرائیل بوده که تا حالا داشتیم؛
🔴
هیچ‌وقت چنین دوستی تو کاخ سفید نداشتیم، او از همه جلو زده، و این شراکت خیلی قوی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/124878" target="_blank">📅 20:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124876">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvS3_lLr5dhEPBRFtfMaims3lEzC8veMpCPUFgcZe9Ik_z_hrSWqc8kj7xMMeWOEGUHVV5McvwTrxtQJdbBRa4ky2w71p2IA_5qmHPKVB_nWEcXrTjNZs3ctit7ejdzJyY-jILPWZkPGGQloWM_2ztB4pumfTnMj7u0bidAbn8VyyEsyAsYKON2c0HblwEhDtlY6iqv7_r7dINyrHYGyn4bdOzfK1g-YKDDw1AZlvKZDIN5Fva8NcO22QAjfKrUra0KRFUqy97IDfU-NvkooFaSpNV1Y91yQixrFoDCBNgAm3ckFzy0KbugujTdb4m8GN-cO4wh7eghYVxj9HgCLpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194eb7223c.mp4?token=VLVWK7rVKolP1Y-lCP1fsFptcK17SUSinvYshLOWLRptwn56FBZdWWneJuOBsEKZP64omg84VLHCBuHFsPI2GQ8hIzlXcMuwoHnF0pf2VEyHKPoeOUPwefvLVOSQDsHdWsLYYCYMQ0YAEYc-_nU2rR4dDb9NwOSDtqhWtXgH7hxttEnCE6oWv55rL6AtXDYCmoR1Joga0-O3aPREUFei31stVNx4wETxsN8KHYN5HjDYk5usRSUGmMSmTO5Z5-BxIyLiH0up-B8-F5t6GlzjYqKKcE6Yf03TSI5AMPsQVsHmQ1lUACrqGOWn8_oa3l2RMHWkZkvLn5McaT49qFwXVBcFFdzIjeA5UwCdj5EqcEBPfrLG0ksakTWqg3iI-HW9dsdMsZKXPeiSO06T8nh3Tld_xKyeJCgnSi0y6s3Rc2HGI0UXAHHheBMaKWXV1HM2pv1my2Oi51hYSK-GwsQmC2mbNBT2BYi02YkvkhgUtwh4_Zl03TymRBg36wwxljuAjLMDoY7x2MVUHAxYx7AisSgfLPyC3Hku2qxjVU3D_Bk9XK4sAV26M3GOkG20GRTW-EqrMsIC-RVdlFQXTFGTkcjqRoXAUgJjfp_EWvyoi2opcqx8f9zDrFqdNPgVoR_BHGJx-51N2KTI8ebCci4vgkAmCBhvE7AY9DO-rN6smQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194eb7223c.mp4?token=VLVWK7rVKolP1Y-lCP1fsFptcK17SUSinvYshLOWLRptwn56FBZdWWneJuOBsEKZP64omg84VLHCBuHFsPI2GQ8hIzlXcMuwoHnF0pf2VEyHKPoeOUPwefvLVOSQDsHdWsLYYCYMQ0YAEYc-_nU2rR4dDb9NwOSDtqhWtXgH7hxttEnCE6oWv55rL6AtXDYCmoR1Joga0-O3aPREUFei31stVNx4wETxsN8KHYN5HjDYk5usRSUGmMSmTO5Z5-BxIyLiH0up-B8-F5t6GlzjYqKKcE6Yf03TSI5AMPsQVsHmQ1lUACrqGOWn8_oa3l2RMHWkZkvLn5McaT49qFwXVBcFFdzIjeA5UwCdj5EqcEBPfrLG0ksakTWqg3iI-HW9dsdMsZKXPeiSO06T8nh3Tld_xKyeJCgnSi0y6s3Rc2HGI0UXAHHheBMaKWXV1HM2pv1my2Oi51hYSK-GwsQmC2mbNBT2BYi02YkvkhgUtwh4_Zl03TymRBg36wwxljuAjLMDoY7x2MVUHAxYx7AisSgfLPyC3Hku2qxjVU3D_Bk9XK4sAV26M3GOkG20GRTW-EqrMsIC-RVdlFQXTFGTkcjqRoXAUgJjfp_EWvyoi2opcqx8f9zDrFqdNPgVoR_BHGJx-51N2KTI8ebCci4vgkAmCBhvE7AY9DO-rN6smQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام سید داوود امامی میبدی ۳۹ ساله، ۱۸ دی ، میبد یزد
🔴
علیرغم تلاش رژیم برای تصاحب مرگ او بخاطر مذهبی بودنش، خانواده اجازه ندادند تا این اتفاق بیفتد.
🤔
عرزشی حرام زاده، غیرتت رو دادای، شرفت رو دادی، دینت رو دادی که اسلحه بگیری به سمت مردم خودت
✅
@AloNews</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124876" target="_blank">📅 20:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزارت امور خارجه انگلیس امروز چهارشنبه به بهانه ورود یک پهپاد روسی به رومانی اعلام کرد که سفیر روسیه را احضار کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124874" target="_blank">📅 20:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبرگزاری فارس، به نقل از مذاکره‌کنندها :  ما هیچ توافقی رو قبول نمی‌کنیم که لبنان نادیده گرفته بشه یا از معادله حذف بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/124873" target="_blank">📅 20:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05cf1b4b47.mp4?token=DRVxmkG742-_Uc7LIplu5DmNqSVpASDH_mUml7BfuNYjNmEPIgaqXxvd6nR-FTNU5OC5771R2sT_QS9SozEUcY0L8jz3AlIwvYBzhFpfWOc0kNtuD4oeDEeyuDszjjU5yVuwkIrdHN3obgN9NcAgFR5FHpRtMbfajR6gy8azVIlZJTqbm_uB1biIWCrStl4cEgyhxRQ3XqNUnAVdtm3nv4shBPiRZCFTTgd87XkF5l1FHmlyj7S3Ub_HZMxZfp0iLiahhOtDRJzJYTt7Iy0p-kuaKo7T3-2fZdEO-B1wSg7XbXFzQbeNNFswhUkwNXSDhkalyPSOBtMbTID1aIY3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05cf1b4b47.mp4?token=DRVxmkG742-_Uc7LIplu5DmNqSVpASDH_mUml7BfuNYjNmEPIgaqXxvd6nR-FTNU5OC5771R2sT_QS9SozEUcY0L8jz3AlIwvYBzhFpfWOc0kNtuD4oeDEeyuDszjjU5yVuwkIrdHN3obgN9NcAgFR5FHpRtMbfajR6gy8azVIlZJTqbm_uB1biIWCrStl4cEgyhxRQ3XqNUnAVdtm3nv4shBPiRZCFTTgd87XkF5l1FHmlyj7S3Ub_HZMxZfp0iLiahhOtDRJzJYTt7Iy0p-kuaKo7T3-2fZdEO-B1wSg7XbXFzQbeNNFswhUkwNXSDhkalyPSOBtMbTID1aIY3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : اسرائیل آمادست، آمریکا هم آمادست، ایران داره با آتیش بازی می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/124872" target="_blank">📅 20:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نتانیاهو : ما با مردم ایران دشمنی نداریم، ما با این آیت‌الله‌ها طرف هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/124871" target="_blank">📅 20:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124870">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
روبیو: گفتگوها با ایران درباره غنی‌سازی اورانیوم و بحث ذخایر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/alonews/124870" target="_blank">📅 20:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124869">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: رابطه من با نتانیاهو عالی است و در مورد مسئله لبنان بین ما توافق وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124869" target="_blank">📅 20:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124868">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مقامات اسرائیلی: تخمین زده می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/124868" target="_blank">📅 20:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124867">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiPLgWX_HdO8eZGX7OH8Lk3cIbYilaKqqdnEJFmqQFULXCBJ2yUUMyz085F99AMIjc-Yhu_I38PDZvgEUOqBYE7K8gsi0HzaqSzJF41cyn171XdyIOXToVwSZi7NEa6agDkpjn8p39hfCw466MqXzOTC2TtQDp0lV5VlQIUTxpM9Z44h3BURzPeTckuPTp2iG1NgS2sTV3CsBoR4bJ0hkEijww_L54gxnpXn7QpHRhPEe08OhRnO3ZACPHJ9Hmk3JdC10F6_iYV0HY1tlZJDZdy-no-XrDZhiIgLZwmLT7qvsT-uYAdIh-zXoS5DPGG7tVWbTcEWHw-b6Ij3eVk9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیری‌ابیانه: نتانیاهو فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد!
🔴
علت جنگ آمریکا علیه ایران این است که نتانیاهو علیه ترامپ آتو دارد و فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد و نتانیاهو این را اهرم فشار علیه ترامپ قرار داده تا هر کاری اسرائیل می‌خواهد، آمریکا انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124867" target="_blank">📅 20:30 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
