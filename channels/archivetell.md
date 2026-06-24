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
<img src="https://cdn4.telesco.pe/file/NvxOPYZlJW4ifxtr8Id-S0qizuUcJoFSEg08z-hmOvdo7c6De-fM8LzC9nyXw6PGc_jnnj9drRcqczVWKvYcTBAzaxG05ByT06hzbUEJNGApRvZ585ZXfrga_NvBgtREXlsnKtzsUw7l2N97NhQVCczOZA-IZs3YfQKZ1xZftyhejHGxhACmD0Rc3KHekMdhQDwXVNfUssp3bDL-74Aot3jaW3870Dz4DkAKfwfQYZBIxyK6f7h4QXTGPWRFMuyoyBR0gXeVaCYvsTTVPUdPvPe-KUYcfzinRsb1THcm6j9RxaU5LRfHDXYY6e4BKauxXOAAx88ZKBgq_HrKxeSt5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.58K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 22:38:16</div>
<hr>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH_GY1yNSoiKmxqFlevsBHCyKIkFa7xfP_A8IjhBEACOYiipXlq6X6mCfY5EJcYJH9uVjx_3HtvuaVbscM0N2lzfJHRzQ9Jg_LEE6exi_8KeUL_KuJV2j90qvXt-0JIESaAQpO80QfMQqBwIvWlNU7P2JAPiO2-zg0bgXiruqciB-tn_j66FTtFoVeY1KCoAz99TqCo8UVhcHrWzsy7nA-44nz1vyKlg2GR62-nepnViDq_YTTwXAiamPNvLnzYikGO9OPPwuSk0u77xvy_Jfe2I8yTryjvTsokcil8sqP4BoRagJwC6ZvoYwe_qhAPpnU4qY9N1NhOcdzV99y6h5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
کتابخونه‌ای به وسعت ۱۱ هزار کتاب!  هوشمندانه جستجو کن و دنیای جدیدی از کتاب‌ها رو کشف کن.
✨
قابلیت‌ها:
•
📖
دسترسی به ۱۱ هزار کتاب با رتبه‌بندی و توصیه‌ها
•
🧠
جستجوی معنایی: «کتابی برای توسعه فردی» یا «متا فیزیک»
•
🔄
مشاهده نسخه‌های مشابه برای هر کتاب
•
🌟
مجموعه‌های پیشنهادی از افراد مشهور
•
📊
جمع‌آوری داده‌ها از کتابخانه‌ها، شبکه‌های اجتماعی و رسانه‌ها
🌐
Site
#کتاب
#کتابخوانی
#معرفی_کتاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 375 · <a href="https://t.me/archivetell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nE2u8w2so271uJSJJ4gKWqsd8FVvdMsZ2G1j7IA2xCV9yNtOxLPucqQ4LzwW7mtkEN2I10V1LhXLehONc2BJ1qEQWoNNfQs48v4Vs7Hvg2mtUPVOvh9FCiHCTg8SwrkY5D0IOqT7gmSlji0MJbA4XdHK1KUxsYTLjKJuVr8-RAawABWTRpJRQgbHFjYvRkrfIX_CZnZ016Udape4zaaSwZ1xVZspKh6LCdlTKD61Q8T2NzFDYvQh_CrstbNzbHVjjzQ9KMRS4bIKouqmgfCdmWtcJJsAHa0vm2io6nsJJSzWi0Dsrr9Vrx9dO5TuXTsJNOKlE-sesQaTMGDrOhUCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEsa7dQymtm8dllCqqk9GKNP_I11eLasAQai_z2GYb-0RrseSu5Jc2nfDGY7YGi2C2ELCaxQ-clSYcw2jj83Y6Gej57MDA3nqEgP4-8Rwvl88pbWrxLQx0eLOaA0KfwrhfS92ysHPu6hcBXFOfVxGyLF6Pcqv3s0a53571kpC0t04VMhjvGXVuWQiqSNmEPxiNJW4icB1qcbbeXC0J_RDknDPjVvWHwrMkOgKNyj915ZBTkh5KDGoIsNQJHy90eEjAtCjk0JjWSGxHggALB6LbjXedL3okvMPRX8Q3VpXxYprAP_x4bTxVkXC_Zu0NBjZyfxl5qqtvsq8cuQ-Ck-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRs_ejCH9zFXBgqskRzD3HZnQpjxvUYSi3BL8gWhV_NMrGxeuqjoe5pKUNmRkSmYEXK6Nw2EsKfKwIP73Ipc_5Zzk0bZH5jf8yhDfQENxkpDdWMuJHUXpU-vnr_f1APaMi1pGTZM4YxCXqUig0Dagfdxmhn1DZKAgRDXnN-fFwA7_al7G-MEIU0Yu-nXiH-Fyun7aG5KWXHA21exS0fwBvwJH1WT06X80aMK83jvEkTmUIKa4CY8IPNWDgSS32A2ue8tAIZj0B33rM1I1Brp8jOnL_6tIr9tIGKbZv5_trmthXvhFSONkXF-BAcUiFuK7chJbUNGsx7fDU7xV2YAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7_CxBGHgTMPmTtYNWsxjazIJv0rqy0mMjPzhqSNqc9Nagt3bOYd8YL4tJKwWUx86E5K4JpdHj6l1jt-BceJj12w1Vf5CJciPRou0w5hvZnkXBO7OyX3bQmxXIBcpHW-2ciLGVGfQ_oOct6YRz-rUzI4wMFQVHplP8tWgoS0GkHjVn-F5F3lCPx9GobMJNYNvAuep_ZXjwRTxq-tYRRmRioq6s4JnmRzzTvNJubx22_fzYoZLHJ1FhZBxRVzBUwO8D-Wmv4llc7tshsmkw6z8tt85MMO65tfR8JGAukY0wG_kGOlgAyFQs9MJ32KlNVrW6bHxSnNK0Z-DqspJ2ARmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🍿
نتفلیکس خود را بسازید — یک برنامه رایگان و متن‌باز برای تماشای فیلم‌ها، سریال‌ها و انیمه بدون تبلیغات مزاحم پیدا کردیم.
🔹
بسیار سریع‌تر از اکثر سرویس‌های مرورگر کار می‌کند.
🔹
امکان دانلود محتوا مستقیماً روی دستگاه را فراهم می‌کند.
🔹
از زیرنویس‌های فارسی پشتیبانی می‌کند.
🔹
بر اساس علایق شما توصیه‌ها و مجموعه‌هایی را ایجاد می‌کند.
🔹
برای راه‌اندازی فقط به یک توکن رایگان
TMDB
نیاز دارید که در چند دقیقه تهیه می‌شود.
🌐
GitHub
#OpenSource
#Streaming
#Entertainment
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 827 · <a href="https://t.me/archivetell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">worker.js</div>
  <div class="tg-doc-extra">23.5 KB</div>
</div>
<a href="https://t.me/archivetell/6535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سورس کد ربات تلگرامی برای چت با هوش مصنوعی بر بستر کلودفلر
🌐
ویژگی‌ها:
- گفتگو با مدل‌های GLM 5.2، Kimi k2.7، Gemma 4، GPT 4 و Llama
💬
- تولید تصویر با مدل‌های Lucid origin و Flux 2
🖼️
- تبدیل صدا و موزیک به متن با مدل whisper-large-v3-turbo
🎤
راهنمای اجرای این سورس در بخش کامنت های این پست ارائه شده است
👇
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/archivetell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
معرفی Save to Yaps؛ ابزاری برای ذخیره هوشمند و خصوصی مطالب وب!
🌐
✨
اگر از آن دسته افرادی هستید که همیشه ده‌ها تب (Tab) باز در مرورگر خود دارید، یا لینک‌های مهم را برای خود ایمیل می‌کنید و دیگر هرگز سراغشان نمی‌روید، افزونه
Save to Yaps
دقیقاً همان راهکاری است که نیاز دارید!
این افزونه یک "Web Clipper" فوق‌العاده است که هر صفحه وب را به یک یادداشت Markdown تمیز و خصوصی در کامپیوتر شخصی شما تبدیل می‌کند.
🔥
چرا Save to Yaps متفاوت است؟
*
تبدیل هوشمند محتوا:
مقالات را از شر تبلیغات، منوها، بنرها و پاپ‌آپ‌ها پاکسازی کرده و فقط متن اصلی را به عنوان یک یادداشت تمیز ذخیره می‌کند.
*
ذخیره سریع تصاویر:
با قابلیت Hover-to-save (نگه داشتن موس روی تصویر)، می‌توانید عکس‌ها را به سادگی به یادداشت‌های خود اضافه کنید.
*
حریم خصوصی مطلق (Private by Design):
برخلاف سرویس‌هایی مثل Pocket یا Evernote، در این ابزار هیچ اطلاعاتی به سرورهای ابری ارسال نمی‌شود. همه چیز به صورت محلی (Local) روی کامپیوتر شما ذخیره می‌شود.
*
کارکرد آفلاین:
حتی زمانی که به اینترنت دسترسی ندارید، می‌توانید یادداشت‌های خود را ذخیره و مدیریت کنید.
*
سازگاری:
روی تمام مرورگرهای مبتنی بر کرومیوم از جمله کروم، اج، بریو و آرک قابل نصب است.
💡
نحوه استفاده:
برای شروع، کافی است اپلیکیشن دسکتاپ رایگان Yaps (برای مک یا ویندوز) را از
اینجا
دریافت کنید، افزونه را روی مرورگر نصب کرده و با یک کلیک، مطالب مهم را به "Second Brain" یا همان پایگاه دانش شخصی خود منتقل کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#Yaps
#WebClipper
#Privacy
#Productivity
#Markdown
#KnowledgeManagement
#TechTools</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/archivetell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgIXCJNMBDI4LYQpMF8IWJMw4Tc2Jz0e41xBO90cnNIq7HNRo3ui4eMtqOMbQKFgl6sRv2IiqfSZopap4CF-gH41npOxIwMf04dRGQR8SmPPeIdP5C6Kg9Nx8paj5AXAdAk4VF9sO67KEdb_jmnDLrFsrKwW1LdVgoWGcR06ltEoXJwt4Qh-Irq_IOy38dKHYtxmqbN5pcdR5XETtuCACpprJSldXLH6BrB-miglFikZdsXAfa3liHzZ24usM3hIm7AOXgHFfJDLFqrPXpX-GgX-d9cokWIYxDXwP5LwPa6I_sL0CsStn7mqksa6avdMv5rzL6QWMiMVFfa7xTtNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش در سطح MIT و هاروارد رو رایگان تجربه کن!
🎓
بیش از ۱۷۰۰ دوره از بهترین دانشگاه‌های جهان حالا در دسترس شماست.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان به دوره‌های برتر جهانی
•
📚
شامل برنامه‌نویسی، ریاضیات، طراحی، کسب‌وکار، فلسفه و علوم دیگر
•
📹
محتوای کامل: ویدئو، جزوه، تمرین و امتحان
•
💡
مناسب برای یادگیری از صفر تا پیشرفته
•
🔸
یکی از بزرگترین آرشیوهای باز آموزشی
🌐
Site
#Education
#FreeCourses
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/archivetell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nesl6hQt_kjpem4gPdzq4Hh20lKFwDPF88aCMGKdWAnGAo_loJ90t6qi85zBLmMb72vN5Pp_VgSK3Z5TqRQGERCTtIHXuj23Zhmddn0knDBH5w64U2OffnZFS08yxIoHEkZLfubOcZCxsFpUSPSA7IVjZc-yB8zcDUfynCyi7z66Z3XGxbVbw796Db1oxsyHctXMoeMJ-KYgZjwIqY3FKBBuVEYPOt60jssmh9Cm9ZbNrrWhl5jwrXGEOnp-wf4jblUBKLiVac5I2QOSPUV__qnqqyr4f_THotWuozp06AisFai22Z_iZsfYYAWvLVqaUARuMSYGjAu7BJ1sc1CnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMa065v_ord40SXFvpTakpWWQyvkrZVfY14jy7tJ5nI-Mme_gUcIoZZUPvNruLYerYARH7e3f8XBRIuesbqYA8ueQs4t4Jtg_5MEOQA6i7BzfCBiVisBsuRwTyuuOCIquiAdEV4t6FBj6I1NkauqeOxe9G3_XGy9_u2mOMUIJwnEJA6S-eXiBLXR23hXd6cckZNN6ELUuMyoSFVZtBnF6s6eHymKak9kqAvjJWv6Iv054anXbI0Rcza1Y8JW_9xQ1lUbsRSrKExRlHdKsu4O2MNqEQAlocYBaunl3Y_lgLrRkEBH_pqsq2A_AcgboKBNfTx7QhKA-G4uIIeJ-Gm5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cs0Z_spBXVCJYbaMlIfzNDU9KznG7whT2bbZ25cfcHQpkyjup0UF6a_9RbP48ln04HLH3dowIfyqsPhu0bckGYtxBn845EH6l_QAuyNfiwBUcedMyz09mHS6WEGhPfWgaFSPpvT7akPHqzhfRcXWrDATGE7dw7kCuRAf1icrHSMwOi6e9WhG_5Ram3vgFWZx9kLE0bZg-Dn5_bqZcvPvWugBNF1VGaV1YzkaOocE60KgmCZh5h4EpokMjB0RWHmizXCBVQHBf_e3v4aQ_7rgofIxKPCoQjyAA-uYSRzkaLMltJLMW63DLuY_JqflxE19YcrdlJHvzBOQ1nDEVTg-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bglIVj9OzXIVRwXdhKcl9eoSuwekGGSEJK3mW97KxD6qLadItyZbii86qABSPILRqwSi0fCF3QInEE_BPWULxgMZ9BeDw_kMfOmIXajSObuXgCPYnmGN7T9t0zddiAQXaidxG_jIBp3pVljY1vbWBWWFQq0CU4TUK7lK4sTC0VicSXaem1j6KfW3xGYgoD7jwsP6nmTDr0jw63B9VmgwmtTtBiWXHjBe3lhDrcV6yoX5z0pfu6t0iUBdjs8fXgJPbAzZ7PShKfYQ80eUAnJi2vNDGkYDjxOqU7e1qWDxyn2lukpR7UYsD8w4QMm9Vg_NRwpp7QjBmreuJmLo9I3GoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOWe0FcWRpQ2mqKoEsSah6vQ9bjJh6vxy5SonXwDrCKNSN5PePjE7jHqriojggAfzC_locWRIS_u5ypeM8VRj6BSyeVPBcHEO2ScrJIAdoulavNQGDJ9MqnWkTLZdC6Jcd4df2u4EuE12FFOa_xOviz5sVynV40zT1l-vHCKvmiI_wufZ7DIo-ZgVg-IKSCeP_1GcQE8e3EPBJRJFewEbQSTmC8fHUVb49RbnOSNdK12RTkLl2M5B_0BWbEKAznGapfdZL-WVS_C0xl-vvsp_gjxXVB9CtlPv6k92QgWyC2dKCPYyqjHnb9oCgRcap-i4kKFfdfVytyIM-AEXDX6TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tqk1e1fP4PbO6yxq5QAHOLbRUm0w8a3TGONARczBffAiYWqiy6vBm-HBLuNWdHLlHCMULVdpE9dzx2HREN4U8dHVNFuyu0swf7mlMLlO1wGqssqLloSlFtAev-2rvdMyc-E9ulwfUM7_q8u0RELkmwe_I5n3ztrtJsFl4DHzloeMtYgy9iI9Kmaz7AtWGDtXiM_j1PRXuwPXla0D5v_k-7PbBTXkn-MFAxWl3PaUn2kf7rD9QR5ztyK_KScVCYifxGpQEiYrzpkQbFZL0Jm-yEGYRIqqaRy0jjqdyovhiFIoN336FFThBB5IHEhVY1Tdaoe4EpsTh5ouYO5Sgftysw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6cLgwyKW1GHk0WgbqAwyJlkWPRodzl9L0HSTc7SJvxSR-CIghPdRR099aA-LZ3XjVkx03WkIj0yQl7QrQoO-Ytf6OdzfQUYnecN4E804T0xYoKEib3pRYnxDqgptnIVdN56sUY5jhAqOIki_3W0yorfL5xXe10XxjOk5STTw8UbIPSo5LgLziSOlgaDbopQJPfi2HKNmy0NsygYG4Z0XAKycRfwSufHvNhc1RGcthmgpEL0if7LPNX6P0f4ZsaRYIoADPi4-gHY53nhOJiCQ2pZMsms_rbfPvdiUh68R9eKHSRphE8kZP0IRckOTdqW93pAfg6gOgbbVTTsTJrd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر تورنتی که بخوای رو پیدا کن!  با "EXT Torrents"، یک موتور جستجوی قدرتمند و رایگان، به دنیایی از محتوا دسترسی پیدا کنید.
✨
قابلیت‌ها:
•
🔹
آرشیو عظیمی از فیلم، سریال، انیمه، موسیقی، بازی و نرم‌افزار
•
⚡
جستجوی سریع و دقیق با کلمات کلیدی
•
📂
مرور دسته‌بندی شده و رتبه‌بندی محبوب
•
🔗
پشتیبانی از کپی مستقیم مگنت و دانلود فایل تورنت
•
🆓
رابط کاربری ساده و بدون نیاز به ثبت‌نام
🌐
Site
#Torrent
#SearchEngine
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
معرفی winpodx؛ اجرای اپلیکیشن‌های ویندوز در کانتینرهای لینوکس!
🐧
✨
اگر نیاز دارید برنامه‌های ویندوزی را در محیط لینوکس اجرا کنید اما نمی‌خواهید درگیر سنگینی و کندی ماشین‌های مجازی (VM) شوید،
winpodx
راه‌حل جایگزین و هوشمندانه شماست. این ابزار به شما اجازه می‌دهد برنامه‌های ویندوزی را درون کانتینرهای ایزوله در لینوکس اجرا کنید.
🔥
ویژگی‌های کلیدی:
*
بدون نیاز به ماشین مجازی:
اجرای مستقیم و ایزوله در کانتینر با عملکرد بسیار بالاتر.
*
پشتیبانی منعطف:
اجرای نسخه‌های مختلف ویندوز در محیط کانتینری.
*
توسعه‌یافته با Python:
ابزاری سبک و قابل سفارشی‌سازی برای سناریوهای مختلف.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#winpodx
#Linux
#Windows
#Docker
#Python
#Containers
#DevOps
#OpenSource</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
معرفی AI Website Cloner Template
این پروژه یک قالب حرفه‌ای برای
تبدیل هر وب‌سایتی به کد مدرن (Next.js 16 + React 19 + Tailwind)
با کمک ایجنت‌های هوش مصنوعی است.
قابلیت‌ها:
*
مهندسی معکوس هوشمند:
تحلیل سایت، استخراج توکن‌های طراحی (رنگ، فونت) و ساخت کامپوننت‌های دقیق.
*
سازگاری بالا:
پشتیبانی از ایجنت‌های معروف مثل Claude Code، Cursor، Windsurf و Gemini.
*
تکنولوژی روز:
خروجی تمیز با Tailwind CSS v4 و استانداردهای strict TypeScript.
کاربرد:
بازسازی پروژه‌های قدیمی خود یا یادگیری نحوه ساخت کامپوننت‌های پیچیده وب‌سایت‌های حرفه‌ای.
🔗
مشاهده در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=XqGZvlUOu-BgUT6yzJ2UFX4rOnBHgqL4eXQREb692hoFBgmQcHcgD5KBCTvXFm7eNzg69bztKISrETD9WJTXBpXMQ3KdS8x0lSJjB2_8cloxFVPFVQx1LnXIANqylwfmSCsmriFewfgowx9f22d3yVb5LRGqqbTnB15dUlElADNpqE1pi-EQ7KHLq3tI3OPc-sLg-PCmjO6MLweA6aK83rag-1RjICEgCn3Zk2xCGVhJgjzcVgJqUXNHGVtlAaPhBUiw8ACB1xgZJmPz7mfa3O1RWTmODJeBbej_0qpClycWvueTbZIZx6GELySWRy9pDib4zvY0PkNwiYpdE04dOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=XqGZvlUOu-BgUT6yzJ2UFX4rOnBHgqL4eXQREb692hoFBgmQcHcgD5KBCTvXFm7eNzg69bztKISrETD9WJTXBpXMQ3KdS8x0lSJjB2_8cloxFVPFVQx1LnXIANqylwfmSCsmriFewfgowx9f22d3yVb5LRGqqbTnB15dUlElADNpqE1pi-EQ7KHLq3tI3OPc-sLg-PCmjO6MLweA6aK83rag-1RjICEgCn3Zk2xCGVhJgjzcVgJqUXNHGVtlAaPhBUiw8ACB1xgZJmPz7mfa3O1RWTmODJeBbej_0qpClycWvueTbZIZx6GELySWRy9pDib4zvY0PkNwiYpdE04dOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡
یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده.
این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway
را فراهم می‌کند.
از طریق خود ربات می‌توانید:
✅
پنل موردنظر خود را بسازید
✅
مصرف و وضعیت منابع را مشاهده کنید
✅
دامنه شخصی خود را برای پروژه متصل کنید
✅
آی‌پی تمیز را مستقیماً از طریق ربات دریافت کنید
هدف 𝗥𝗘𝗡 ایجاد یک روند ساده‌تر و خودکار برای مدیریت پروژه‌ها و سرویس‌هاست.
🤖
ربات
💻
سورس پروژه
━━━━━━━━━━━━━━
👨‍💻
توسعه داده شده توسط 𝗔𝘀𝘀𝗔
دوستان اضافه کنم اگر رندر شما ساسپند شد اکانت رو حذف کنید و دوباره با همون ایمیل یا گیت هابی که داشتین ثبت نام کنین مصرفتون ریست میشه
برای حمایت از پروژه star بدین
❤️
(در گیتهاب ترجیحا
😂
)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVR4XEjDzdRdjcvGQLJGPAjmry0EVKRiOtci4X75xm2Xqpnpw_vtHGu-3BU8dk8bn-beeb7VzL0IshUmHTCUzbcmmpd5coF_PK2uqoZwfCTsXrtDHLJGjvgTrMiyc8sS9rnzYtsnEkzLoYgRscq_TM4N8xjWwfk6PHGHwjumTQgtkYuoPdLXsZ99FnIrpMtZREFJP5qKFLAPpbGvJfAQiN6xF0d8Ly3mLd-OGLw3ivcn6q3U0tVFwRUPx4Q0pvTsoHDhYktO20_xFWOLqlgYJ2Zi0_VlnrbsKOYwalBORLVka5hshcBl_NEx6dnGZC7fpuGNI_1pnVt4ZZ5IoeLhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی shadPS4؛ سریع‌ترین شبیه‌ساز کنسول پلی‌استیشن ۴ برای کامپیوتر!
🎮
✨
اگر به دنبال اجرای بازی‌های PS4 روی سیستم خود هستید، پروژه
shadPS4
یکی از فعال‌ترین و سریع‌ترین پروژه‌های متن‌باز (Open-Source) در دنیای شبیه‌سازی است که با زبان C++ نوشته شده و با سرعت خیره‌کننده‌ای در حال پیشرفت است.
🔥
چرا shadPS4 در حال حاضر ترند شده است؟
1️⃣
توسعه روزانه:
این شبیه‌ساز تقریباً هر روز آپدیت می‌شود و بیلد‌های جدیدی برای سازگاری با بازی‌های بیشتر منتشر می‌کند.
2️⃣
پشتیبانی چندپلتفرمی:
به راحتی روی
ویندوز
،
لینوکس
و
macOS
اجرا می‌شود.
3️⃣
رشد سریع:
در تاریخ اخیر شبیه‌سازهای کنسول، shadPS4 سریع‌ترین روند بلوغ و افزایش سازگاری با بازی‌های بزرگ (Major Titles) را داشته است.
4️⃣
جامعه کاربری فعال:
با بیش از ۳۱ هزار ستاره در گیت‌هاب، این پروژه به یکی از محبوب‌ترین ابزارهای گیمینگ در اکوسیستم متن‌باز تبدیل شده است.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#PS4
#Emulator
#Gaming
#OpenSource
#Github
#Cplusplus
#RetroGaming</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚀
معرفی OpenSERP؛ دسترسی رایگان به API موتورهای جستجو (جایگزین SerpAPI)!
🌐
✨
اگه برای پروژه‌های هوش مصنوعی، سئو (SEO) یا اتوماسیون خودتون به دیتای موتورهای جستجو نیاز دارید و نمی‌خواید هزینه‌های سنگین برای خرید API بپردازید، ابزار
OpenSERP
دقیقاً همون چیزیه که دنبالشید! این پروژه متن‌باز (Open-Source) دسترسی کاملاً رایگان به نتایج Google, Yandex, Bing, Baidu, DuckDuckGo و Ecosia رو از طریق API فراهم می‌کنه.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
بهترین جایگزین سلف‌هاست:
یک جایگزین رایگان و قدرتمند (Self-Hosted) برای سرویس‌های پولی و معروفی مثل SerpAPI, DataForSEO و Tavily.
2️⃣
خروجی مارک‌داون (Markdown):
قابلیت استخراج دیتا از سایت‌ها و نمایش نتایج جستجو به فرمت Markdown (که برای پروژه‌های RAG، ایجنت‌های هوش مصنوعی و LLMها یک ویژگی طلایی محسوب می‌شه).
3️⃣
جستجوی ترکیبی (Megasearch):
این قابلیت به شما اجازه می‌ده تا یک کوئری رو به‌طور همزمان در تمام موتورهای جستجو سرچ کنید و نتایج تجمیع‌شده رو تحویل بگیرید.
4️⃣
کاربردی برای همه:
ابزاری بی‌نظیر برای متخصصین سئو، توسعه‌دهندگان، برنامه‌نویسان وب‌اسکریپینگ و فعالان حوزه هوش مصنوعی.
⚙️
این ابزار رو هم می‌تونید خودتون هاست کنید و هم از نسخه تحت وب و آماده‌ی اون استفاده کنید.
🔗
لینک مخزن گیت‌هاب
🔗
نسخه آماده و تحت وب
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenSERP
#API
#SEO
#WebScraping
#LLM
#RAG
#OpenSource
#Github
#Tools</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚀
آموزش دریافت یک ماه اشتراک رایگان Duolingo Super!
🦉
✨
اگه از برنامه دولینگو برای یادگیری زبان استفاده می‌کنید، الان می‌تونید با یه ترفند خیلی ساده و جذاب، یک ماه اشتراک پریمیوم (Super) این برنامه رو کاملاً رایگان دریافت کنید و از شر تبلیغات و محدودیت‌های جون (Heart) خلاص بشید!
🔥
مراحل دریافت اشتراک:
1️⃣
نصب اپلیکیشن:
ابتدا
اپلیکیشن Webtoon
را دانلود کرده و یک اکانت جدید در آن بسازید.
2️⃣
جستجو:
در نوار جستجوی برنامه، عبارت
Duo Leveling
را سرچ کنید (این کمیک مشترک دولینگو و وبتون است).
3️⃣
اسکرول کردن:
سه قسمت (اپیزود) از این کمیک را باز کنید. (اصلاً نیازی به خواندن نیست، فقط کافیه صفحات را تا انتها به پایین اسکرول کنید!).
4️⃣
دریافت کد:
بلافاصله بعد از انجام این کار، یک کد فعال‌سازی رایگان Duolingo Super به شما داده می‌شود.
👏
5️⃣
فعال‌سازی:
حالا وارد لینک زیر بشید، وارد اکانت دولینگوی خودتون بشید و کد را وارد (Redeem) کنید:
🔗
ورود
🎉
تبریک! اشتراک یک‌ماهه شما فعال شد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Duolingo
#DuolingoSuper
#Webtoon
#FreeAccount
#LanguageLearning
#Tricks
#Education</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
تبدیل عکس شما به مینی‌فیگور واقعی لگو (LEGO) با هوش مصنوعی!
🧱
✨
دوست دارید بدانید اگر یک کاراکتر لگو بودید چه شکلی می‌شدید؟ با استفاده از تولیدکننده‌های تصویر هوش مصنوعی و یک پرامپت (دستور) مهندسی‌شده، می‌توانید هر عکسی را به یک رندر سه‌بعدی و فوق‌العاده جذاب از مینی‌فیگور لگو تبدیل کنید!
🔥
ویژگی‌های این استایل جذاب:
1️⃣
حفظ هویت و جزئیات:
لباس‌ها، مدل مو، رنگ مو، حالت چهره و حتی اکسسوری‌ها کاملاً شبیه عکس اصلی شما بازسازی می‌شوند.
2️⃣
رندر فوق‌واقع‌گرایانه (Photorealistic):
اعمال بافت پلاستیک براق لگو، درزهای قالب‌گیری و نورپردازی استودیویی که باعث می‌شود تصویر کاملاً شبیه یک اسباب‌بازی واقعی به نظر برسد.
3️⃣
رعایت دقیق تناسبات:
سر استوانه‌ای، دست‌های گیره‌ای کلاسیک و بدن بلوکی شکلِ استاندارد لگو.
👇
پرامپت (دستور) برای استفاده در Midjourney یا DALL-E 3:
کافی است عکس خود را در هوش مصنوعی آپلود کنید و دستور زیر را به آن بدهید:
>
Turn the person in the uploaded image into a realistic LEGO minifigure, preserving their individuality, clothing, hairstyle, hair color, facial expression, and accessories as much as possible. The character must match the proportions of a LEGO minifigure: a cylindrical head, simple facial features, a blocky torso with printed clothing details, standard LEGO arms and hands, and a molded plastic hairpiece. Use realistic LEGO plastic texture with a glossy sheen, molded seams, and studio lighting. Plain white background, full body photorealistic 3D render from head to toe.
💡
نکته کاربردی:
این ترفند برای ساخت عکس پروفایل‌های بامزه، آواتارهای تیمی و پست‌های خلاقانه شبکه‌های اجتماعی بی‌نظیر است!
🔵
@ArchiveTell
| Bachelor
⚡️
#LEGO
#AI
#Midjourney
#DALLE3
#Prompt
#PromptEngineering
#3DRender
#Avatar</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kcxw_Y2ycXcHX8TQplLmVWA39GSa1lCUyyPceIXSPwmKnhVwYXQEdx8aNu1KWDLRqB-PI7Z6qig9Q6rgQ7u_pon3JvhTywoMsAql3AJ1V8u516wxtEAYJN-X2w54Mx0rBVSDbi-W5rbzZ6dd1caKm9q9dhjJ7DyFCOc5YcueWt2iWhZ2BNWoxmv-JFIPZMfvKqH0CR8mP1eZaOM-nMWjsCEuve-nYZXDCFdKkknrJE4YnWnnzVDjHn6F2kTLL4jfmh6T6GjD-xPU4DIlADyC5Cj5QsscqgcTq1Ij1FTzo43svDv9tC4FRXJHP1-zKESZaJdwWmgeBG_9cQWfAzRWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی پریمیوم با مرورگر tabbit
🤯
ChatGPT 5.5 Pro
Gemini 3.5 Flash
Claude Opus 4.8
و بیشتر
در دسترس برای
macOS
و
ویندوز
مرورگر را نصب کنید و استفاده از جدیدترین مدل‌های هوش مصنوعی را به صورت رایگان شروع کنید!
🌐
Site
#Ai
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_QBFlQPqDVLZjhYtPcNLHt55dOVpqdaEB-B-2SW2luI76jckJTLDY-m5vYgXubOKXOkp88_dfMxvQ6t0Swql7bqmTM9K59tKOCIZikQjDSOe6QL7587Eodn08WitLRrfZaHmujKct2X5fwKkZNH1pKqk4L7-_DrfqFVQ3ajutes7atlrx4RW1vWM_ActvCNC0mXGETswKCePOlK4ESugUeQJJdgKfrWNgTvVU7CT1lv5JL_xaCZdadSKcz8Ne0brz0OwW7h5Oi5kahbs61cnlwvBzEHiBTUSlIXC0ejPeOyjgXWVecAQVaIT_x7ch5OqSVdEG8ojmZzTJJF7sdPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها مدل Qwythos-9B-Claude-Mythos-5 را معرفی کردند که بر پایه Qwen3.5-9B است و قابلیت پردازش ۱ میلیون توکن را دارد!
🤯
✨
قابلیت‌ها:
•
🧠
تنظیم دقیق بر اساس ترکیبی از Claude Mythos و Claude Fable.
•
📚
پنجره متنی گسترده تا ۱,۰۰۰,۰۰۰ توکن!
•
🌐
انتشار کاملاً متن‌باز
•
✍️
همه‌کاره برای کار با متن، کد و اسناد طولانی.
🌐
Site
#OpenSource
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVses_N0aib0oMzqoE5G-76kWvpSjp8fSBzD7Cm6C1n1iKZuJjeYaT25CvJZ92mdAlKSwCJ5Ct5siQHBjUS5wXF6X0l2YdM5FEnwKG4YU5f5J61vx5rglyGHsypzk63L0kPBGzGGN9ZGQpLopxxADQ52sHrL_0bQXRiAWWI4mfLlQNw5nd_A826KRJ2jH9YSJVacJ65kOR31FBVDr3rnkM58y1rMoIcKxRMhjj4h8qML3F9rEN_oKWsHF4A2QyLQ-6FsHCCO9f5RkZcXXZU4JaPKp6re4JpgEYibVnqVeZtC0--As88D8yP0iC7BlTt1UBWvpGP4Vx1H_OcuZpHbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=IFvmsu74h2kh0xYumy4mxbbAkCPVg9rS01-k-fiZQJdDk7-hhd31ueLrhHy1NPXxwQgOR6xMnEzAfnvcEfJOOo1CqQG7hrJCRvA1L0iV8beZ_lI_eWiEXA7U5TF1iPRRQgUxxqnaKtqOGG5QIpsnLOEbmms8lMkhFnsFGuIfVEbsaZNroFuF06myxvTMNBiIO4Sh8Rxd6XgKCDEnX2u5mfvwuWipXgiE_3YNkZVgF3vtnxqP0-d4if22UTR5CiFt-EOXEQdxh_2jb67A1itUjpNvr8XormThHEhP7MddKl3--XBJy0FYMQNOkj8c48zjERFOwObFRRaVJ8oZUGAdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=IFvmsu74h2kh0xYumy4mxbbAkCPVg9rS01-k-fiZQJdDk7-hhd31ueLrhHy1NPXxwQgOR6xMnEzAfnvcEfJOOo1CqQG7hrJCRvA1L0iV8beZ_lI_eWiEXA7U5TF1iPRRQgUxxqnaKtqOGG5QIpsnLOEbmms8lMkhFnsFGuIfVEbsaZNroFuF06myxvTMNBiIO4Sh8Rxd6XgKCDEnX2u5mfvwuWipXgiE_3YNkZVgF3vtnxqP0-d4if22UTR5CiFt-EOXEQdxh_2jb67A1itUjpNvr8XormThHEhP7MddKl3--XBJy0FYMQNOkj8c48zjERFOwObFRRaVJ8oZUGAdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗿
افزونه Caveman پرامپت‌ها و پاسخ‌های هوش مصنوعی را فشرده می‌کند
به‌طور خودکار کلمات اضافی را از درخواست‌ها و پاسخ‌ها حذف می‌کند و در عین حال معنی را حفظ می‌کند. با ChatGPT، Claude و Gemini کار می‌کند.
نویسنده ادعا می‌کند که این افزونه می‌تواند مصرف توکن‌ها را تا ۷۵٪ کاهش دهد. ایده ساده است: کلمات کمتر یعنی هزینه کمتر، و معنی باقی می‌ماند.
🌐
افزونه
#Caveman
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚀
معرفی Firecrawl؛ قدرتمندترین API برای جستجو، استخراج و تعامل با وب در مقیاس بزرگ!
🔥
✨
اگه توسعه‌دهنده، محقق هوش مصنوعی یا دیتا ساینتیست هستید و نیاز دارید اطلاعات سایت‌ها (حتی سایت‌های پیچیده و مبتنی بر جاوا اسکریپت) رو برای مدل‌های زبانی (LLM) یا دیتابیس خودتون استخراج کنید، پروژه
Firecrawl
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید!
🔥
امکانات بی‌نظیر این ابزار:
1️⃣
استخراج هوشمند (Scrape):
تبدیل هر URL به فرمت‌های تر و تمیز مثل Markdown، HTML، اسکرین‌شات یا JSON ساختاریافته در سریع‌ترین زمان ممکن (میانگین ۳.۴ ثانیه).
2️⃣
پوشش ۹۶ درصدی وب:
به راحتی از پس سایت‌های سنگین JS-heavy برمی‌آید.
3️⃣
خزش و نقشه‌برداری (Crawl & Map):
کشف آنی تمام لینک‌های یک سایت و استخراج کل صفحات آن فقط با یک درخواست (Single Request) یا به صورت گروهی (Batch).
4️⃣
عامل هوش مصنوعی (Agent & Interact):
فقط کافیه به زبان ساده توصیف کنید چه دیتایی نیاز دارید تا Agent این ابزار سایت رو بگرده، باهاش تعامل کنه و دیتای مورد نظر رو جمع‌آوری کنه.
5️⃣
متن‌باز و خوش‌ساخت:
هم به صورت سلف‌هاست (Open-Source) و هم سرویس ابری قابل استفاده است و پکیج‌های آماده برای Python و Node.js دارد.
🔗
لینک سایت رسمی:
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Firecrawl
#WebScraping
#API
#AI
#OpenSource
#Github
#Python
#Nodejs
#DeveloperTools</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=m78DW0eT45aJ2cU8svFjMgp9V20j_mspKTSFBooWXyuctnijdOsVlUgBGYkPa3C7bGHbVA_igV-ozDhvk-s4SJC720ij4oKLWnHhbHeDqwKvC-GCNk7nF5y-vzgwFWCgG2LMCBkv9kXO3fm4VvAQ5oG-p_9ncyJDDHB1FgCQxgsaGNDgvOWaMY3hig6nlvNVE7JhSkvJKYsK4VlloRme_FYj__3Ljff6UzPOFhpD_ecNIyfegSzCNmQQx_qiD2evYKZYc79mK2heALmTztD_VRu_y4TfgrKsnbQMUqs33q1hiVJPd-5VpFHT8fVINUgfVaedMhBXxjDIYiprTidlNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=m78DW0eT45aJ2cU8svFjMgp9V20j_mspKTSFBooWXyuctnijdOsVlUgBGYkPa3C7bGHbVA_igV-ozDhvk-s4SJC720ij4oKLWnHhbHeDqwKvC-GCNk7nF5y-vzgwFWCgG2LMCBkv9kXO3fm4VvAQ5oG-p_9ncyJDDHB1FgCQxgsaGNDgvOWaMY3hig6nlvNVE7JhSkvJKYsK4VlloRme_FYj__3Ljff6UzPOFhpD_ecNIyfegSzCNmQQx_qiD2evYKZYc79mK2heALmTztD_VRu_y4TfgrKsnbQMUqs33q1hiVJPd-5VpFHT8fVINUgfVaedMhBXxjDIYiprTidlNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی KanaiAI؛ چیدمان مجازی مبلمان در خانه شما بدون نیاز به حدس و گمان!
🛋
✨
اگه از اندازه‌گیری‌های دستی و خسته‌کننده برای خرید مبل و وسایل دکوراسیون کلافه شدید،
KanaiAI
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار هوش مصنوعی به شما نشون می‌ده که هر وسیله‌ای دقیقاً چطور در فضای خانه شما قرار می‌گیره.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
مدل‌سازی دقیق:
اسکنر هوشمند این سرویس، یک مدل کاملاً دقیق و سه‌بعدی از اتاق یا محیط خانه شما می‌سازد.
2️⃣
خداحافظی با متر و اندازه‌گیری:
دیگه نیازی به محاسبات و درگیری با ابعاد نیست؛ هوش مصنوعی خودش پارامترهای وسایل مورد نظرتون رو با فضای خالی اتاق تطبیق می‌ده.
3️⃣
تجسم واقعی پیش از خرید:
مبلمان و وسایل جدید را قبل از اینکه پولی بابتشان پرداخت کنید، مستقیماً در دکوراسیون منزل خود ببینید!
🔗
لینک ورود به سایت
🔵
@ArchiveTell
| Bachelor
⚡️
#KanaiAI
#AI
#InteriorDesign
#TechNews
#SmartHome
#Architecture</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8B1dJkr6rIJQg-AXiEX0IO37GxaJdWK7xAZEzcMvGabMNBiUrjDU4qu5wUWv95eTzY8mto-RaodRLqo6MGQoZkJvNSNiNKRzENrzgXTw5_rwq-Ly5lspnwkYHHeseUqrEK3vdhE47kdxIZEIEMJFQ9K8q8rPzfGSwliViOtEF7ZWDGTJV0t_zDwCvuHLky6p7mfTElfOtSByMrPCyRH3DO1lwfXhEDWhZ3eJYHEDed2IrW3yxr-krqoH6Rpuf_NlGOReaTxKe5Groysh6PR8dGzecxYj9Qg4mX2qLiTY5wohgJeCQkgqPlynWk0rGuJc2P91dcrahtJTQznkZYsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
Navidrome — اسپاتیفای شخصی خودت رو بساز!
سرور موسیقی رایگان و متن‌باز که کامپیوترت رو به یک مرکز پخش موسیقی خصوصی تبدیل می‌کنه.
☁️
✨
چرا عالیه:
•
🏠
رایانه شخصی = مرکز موسیقی خصوصی
•
📱
دسترسی از هر دستگاه: اندروید، iOS، وب، پلیرها
•
☁️
پشتیبانی از فضای ابری — لازم نیست PC همیشه روشن باشه
•
🍓
اجرا روی سخت‌افزار ضعیف
•
🎚️
کنترل کامل — بدون سانسور، بدون محدودیت
•
💸
کاملاً رایگان — بدون اشتراک
🌐
Site
#Navidrome
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=nSPzcVer7UYxh1u2WFnWM6mgse0KkVMa_iWVms8mhf7Es4OiDea6IYJ-r8Qj5lwzYN6H2ImbKO7TiRanlDth8qkJGbTf03gpcveMUJzULMAqvVbght80TAs2M3InfShuA8llP8LUOIiEbYmbzI9HiFycxHYLxQtZK0alKhUbOPFGLc0cxPxRvh4MxnaaEKS2PRqqLnqoAfIl6ZGSfiXOOiSsdHShZrkuR97yQAzZtuceSX_FEuIyf2B2ZnWRS0HM5ZcAicNPTFtCf8IpdCBf4iTrfdyWuCr52hToZVEpb6EW9hp7L0mUGs1THDOp3wMwArg_Sj-gae6uZeDv3clGDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=nSPzcVer7UYxh1u2WFnWM6mgse0KkVMa_iWVms8mhf7Es4OiDea6IYJ-r8Qj5lwzYN6H2ImbKO7TiRanlDth8qkJGbTf03gpcveMUJzULMAqvVbght80TAs2M3InfShuA8llP8LUOIiEbYmbzI9HiFycxHYLxQtZK0alKhUbOPFGLc0cxPxRvh4MxnaaEKS2PRqqLnqoAfIl6ZGSfiXOOiSsdHShZrkuR97yQAzZtuceSX_FEuIyf2B2ZnWRS0HM5ZcAicNPTFtCf8IpdCBf4iTrfdyWuCr52hToZVEpb6EW9hp7L0mUGs1THDOp3wMwArg_Sj-gae6uZeDv3clGDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
OpenScreen — ضبط صفحه نمایش، سینمایی و حرفه‌ای
✨
قابلیت‌ها:
•
🖱
حرکت روان و طبیعی موس
•
🎨
پس‌زمینه شیک و حرفه‌ای
•
✏️
ویرایشگر داخلی: زوم، سایه، گرد کردن گوشه‌ها
•
💻
سازگار با ویندوز و مک‌اواس
•
💸
رایگان و متن‌باز — رقبا ماهی ۲۰$ می‌گیرند!
🌐
Site
#OpenScreen
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPh67XHkShKMe2KmjVdzGgACs4ziaClpcv8Yw4zcbVWFIi73hW4Tf6Id0SQPIWpzXZarncuXJ0d1J_EON9UEunTNjXkBrRRLGftL1rkN3mp_iRtY2MsBxrwKyg9uAq5dNMSzTkFY4fiQYGcMS3Zu0eoKmyCHvCrYJheFg9Uf-K1BYQsCRZaql5mQCUO4XL-U2pxVi0ecQBg7Q27jlepLX6RNyUWuQoFuZlAECT05PVF7vYQR-BMHdMpi3nP0xrMzvn_KKdEvr-vmXaxHk9sHiitMH_wyxmHGE8hmI-MF6wevI1kzePQwgiT_GXzRutaJpuVbnfHuFyUU9NhcWYzOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_8TrbLwQGdzSLuFCkec30Jfy5YRRZpTbuVD9Uo_1VQOa9BLfwvpm8IHoiAptSch_aNv8vfIY9dF1HqN0p2_x8s7ZyxXTU_DFwViMnNBt-mMJk2TPP_YM9uWCkh7C-K9pjjMHQ3bVuSClJ3kTMuRpvkbcLE-H8HMCnmVo5vMLaWCC12Z9uGATO05v_zfkq-HoSDjPBw0SwLULzNtF5pG78ZsV2JEyWVVWk0NeSS6mt2raF0XzXsqt0GyHgKEnDK3sz-VOuZ0HBbfbHMa7M_1f14ieNKWnEwoKlVe_7z6C0tmfuO_F1BelXKA--zqz4DU-zutCdi_82_UEy8hnMU33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗂
PostKeeper
این افزونه توییتر یا X را به آرشیو شخصی شما تبدیل می‌کند
✨
قابلیت‌ها:
•
🔹
خروجی پست‌ها، لایک‌ها، بوک‌مارک‌ها و لیست‌ها
•
📥
دانلود فایل‌های ساختاریافته برای پشتیبان و مرجع
•
🔒
آرشیو محلی و خصوصی روی دستگاه خودتان
•
🧭
جستجو و دسترسی آسان به تاریخچه حساب
•
🛠
متن‌باز با تمرکز بر حریم خصوصی
🌐
سایت
🌐
افزونه
#Twitter
#X
#OpenSource
#Privacy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGfAIA64aEG6E6wapLXw9cPB8WzOy1Aj5EonfGBjFAbWsn7YnJWS9oISc0mO2Bu90NreveAlM3UFkfy53Mb3IRNrKGNai0k2YHz4alQ2TZ1fwpmQgVoWGRjX29jRqtNSRQmJC4c5crc32aEqZ_EtzpGlMrJuH1RW0y6LLgvC337wqA5LtGdeaxBF_gj0l7zwzych6Cqq--Y5U_6mXTFzil1xElzM9ghu0rwrdjupVeThjFecskZc93zQuo9pFpasI3IQIvq6XaXDeSGuEBwg2y3ZJZs9XIpX6m7Px18IqxMQjLJTQvYMhyJUVoYQ11F5htaE2yTrBg8kVHU1mQ8Ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
80 کریدیت رایگان برای دسترسی به برترین مدل‌های جهان مثل Opus، Fable و GPT
✨
همین حالا وارد سایت
kie.ai
شوید
📝
ثبت‌نام کنید و از امکانات فوق‌العاده آن لذت ببرید
🔑
همچنین می‌توانید API Key اختصاصی دریافت کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSCnZ9Hmb14yEdLtph1n40ZR2gP1GAtGk74E3nXRX4F4mDlgvW9fr6ddyHAcvO9mN5LsNaisM9Zhlh7xcega25I3-jZHSZPrJTdGUuJkGOCyG2lNh6uPtv0_ecftBpELw_GNgDoMyyevKz1pmP1aCmGM_SSB-D4vdvO0IeGlCgp4-WUqmRBZa_W8CVHvCKocxDikiklKjHSsJuodW4SzJg7uvlLdoPwL0-ZxiKeNYAIU_tOCddZtaoWtSVU5PFjMcv0cmD4TJCF_MGxb7itTGkYw-chXSFXdaAOhn0G_Ht7qbpXtDR7Dpzg3ZZi4HFrxoMclwlSPikv0jUrRKcvirg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=Sj1F7bbAXNS1KU41sqUK_D2SkztztbS81HQHINue-AwF0i_R8gYWdaoHLUtBC2XLQYq_W2RWv0fsGu_5nx5MaWt22c1s7cvbPE7yoJqd_pKf-qRZMp-lDLr4GbAje22WCaqvc1SGrvNJSH2OFX0YpAaWF28irpofGxtNoVSp0alu-WO5KPQ4N0an7F9l_xQbZ52XZRrc944fG6MENXBu0aD6_tnjvQiJSg84HSvR69J7pWRsJ6MRhruLaN04KE7qnJGRP_ku2zrpkzIHfqooNJF843sBZoOq2DyqjrHuUa8djb5horC6I4YCCxzYHVy0ImzshUck3ZYMndeWWdRpDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=Sj1F7bbAXNS1KU41sqUK_D2SkztztbS81HQHINue-AwF0i_R8gYWdaoHLUtBC2XLQYq_W2RWv0fsGu_5nx5MaWt22c1s7cvbPE7yoJqd_pKf-qRZMp-lDLr4GbAje22WCaqvc1SGrvNJSH2OFX0YpAaWF28irpofGxtNoVSp0alu-WO5KPQ4N0an7F9l_xQbZ52XZRrc944fG6MENXBu0aD6_tnjvQiJSg84HSvR69J7pWRsJ6MRhruLaN04KE7qnJGRP_ku2zrpkzIHfqooNJF843sBZoOq2DyqjrHuUa8djb5horC6I4YCCxzYHVy0ImzshUck3ZYMndeWWdRpDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">MagicVideoAI
تبدیل متن به ویدیو
🔥
شرکت ByteDance (تیک‌تاک) ابزار جدیدی برای تبدیل متن به ویدیو ارائه کرده است .
این مدل از نظر پارامترها از Pika 1.0 و Stable Diffusion-XT پیشی گرفته و ویدیوهای فوق‌العاده‌ای بر اساس متن تولید می‌کند.
🌐
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa0KWvN1j5BHnQdY9-46e0zFElE3IRm6I-coRLBMFy-cHpzNE8C6Z-bL3wPEqWSPaxIev7AmpZenai3v8OvlXBBi_taX_COaR6eXGmq6kfeE39g9QU5Tq9tdsh58ZqLz1Qw1qqoZOZhtlEVU6-oCcFA15wSqUMi2PldRRWH3FBVAx-gMNEGKljliNg_uiQvasg4bqZ5P0rJMkq9bUDh_6sr-ZQIj7V7f5RakzoGLqS-my0I2yQKLWNzz0RODxshg8hc2TNU1_sg6P4zQeOFHInCZgAgZf4UF5q4GAtwCz5jePQmwum_6UOAM5bQoxMP26-22STBGdYmzIcJksExzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام
Sakana Fugu
رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک پلتفرم هماهنگ‌کننده چندعاملی (Multi-Agent) است که در قالب یک API واحد (سازگار با فرمت OpenAI) ارائه می‌شود.
🔥
ویژگی‌های شگفت‌انگیز این سیستم:
1️⃣
دو نسخه متفاوت:
نسخه
Fugu Mini
(با تمرکز بر تاخیر بسیار کم و سرعت بالا) و نسخه
Fugu Ultra
(برای پردازش تسک‌های فوق‌العاده سنگین و پیچیده).
2️⃣
معماری کاملاً پویا (Dynamic):
برخلاف سیستم‌های قبلی که نقش‌های ایجنت‌ها از پیش تعیین می‌شد، هسته Fugu یک مدل زبان سبک و خودران است که بسته به میزان سختی تسک، مدل‌های «کارگر» (Worker) را به‌طور خودکار فراخوانی کرده و کار را بین آن‌ها تقسیم می‌کند.
3️⃣
خوداصلاحی و Test-Time Scaling:
این سیستم قابلیت بازگشتی (Recursive) دارد؛ یعنی می‌تواند خروجی‌های قبلی خود را بخواند، اشتباهاتش را تشخیص دهد و یک گردش کار جدید برای اصلاح آن‌ها ایجاد کند.
4️⃣
پادشاهی در بنچمارک‌ها:
نسخه
Fugu Ultra
در تست‌های به‌شدت سخت استدلال و کدنویسی طوفان به پا کرده است! این مدل در تست‌های GPQAD (۹۵.۱)، LCBv6 (۹۳.۲) و SWEPro (۵۴.۲) توانسته مدل‌های پرچمداری مثل
GPT-5.4
،
Gemini 3.1
و
Claude Opus 4.6
را به‌طور کامل شکست دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#SakanaAI
#Fugu
#MultiAgent
#AI
#GPT
#Gemini
#Claude
#TechNews</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
معرفی یک راهنمای جامع و فوق‌العاده برای یادگیری زبان انگلیسی!
🇬🇧
✨
اگه دنبال یه نقشه راه اصولی، متفاوت و البته رایگان برای تقویت زبان انگلیسی می‌گردید، ریپازیتوری
English-level-up-tips
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید. این راهنما با یه رویکرد قدم‌به‌قدم، یادگیری زبان رو از یه غول ترسناک به یه پروسه لذت‌بخش و طبیعی تبدیل می‌کنه!
🔥
ویژگی‌های برجسته این راهنما:
1️⃣
پوشش تمامی مهارت‌ها:
از درک مطلب و دایره لغات گرفته تا لیسنینگ، ریدینگ، اسپیکینگ و رایتینگ؛ همه‌چیز در این آموزش گنجانده شده.
2️⃣
یادگیری با قدرت هوش مصنوعی:
یکی از جذاب‌ترین بخش‌های این راهنما، آموزش نحوه استفاده از ابزارهای هوش مصنوعی مثل
ChatGPT
و
Gemini
برای تسریع و بهبود فرآیند یادگیریه.
🤖
3️⃣
مناسب برای همه سطوح:
فرقی نمی‌کنه مبتدی هستید یا پیشرفته، دانشجو هستید یا یک متخصص؛ این مخزن ترفندهای جذابی برای همه داره.
4️⃣
جامعه کاربری پویا:
یک مسیر ساختاریافته که به شما یاد می‌ده یادگیری زبان یک مسیر پیوسته است، نه یک مقصد نهایی!
🔗
لینک مخزن در گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#English
#Learning
#Github
#AI
#ChatGPT
#Gemini
#Roadmap
#Education</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qO7RKZaOO3oefhv3neuRtQEK7KGalOk5eHdipn9HvbB7jzPFG18684ka4b1k5_fhf3jlX5XkNWAfq--YpdI_3GbmH3S7ipjCOvMnVTBEtKU-cLa9n4OdZwXdHyIBzsA6WCM27Y81tk0FaOEFSd-MWWIJ_smIYGoDQcFgXgjO8rDVAsM3Z1qfX0LVWsbA_w78VE3Tjrjh_hineE0FOdGB613Y_ycG_4VJOHyhfHH6eLJanDe3pi0ASLUgp9bdfxQFl_SlhnbcewkRw0RVB_mk0Se-bwO75fI4iLfbYT6j7G35WLhaduAssr1AU65p9FMSwxxdz-85Q88gRDb0YvW8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
ساخت آرشیو اینترنتی شخصی
ابزاری به نام Monolith می‌تواند کل سایت‌ها را در یک فایل HTML مستقل ذخیره کند.
دیگه نیازی نیست نگران باشید که مقاله، دستورالعمل یا مستندات مورد نیاز روزی ناپدید شوند.
✨
قابلیت‌ها:
•
🔹
ذخیره کل صفحه در یک فایل HTML مستقل
•
🖼
نگهداری تصاویر، استایل‌ها و منابع صفحه
•
⚡️
استفاده ساده بدون تنظیمات پیچیده
•
🛠
اجرا روی ویندوز، لینوکس و مک‌اواس
•
📦
رایگان و متن‌باز
🌐
GitHub
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚀
معرفی OpenPencil؛ رقیب متن‌باز و رایگان فیگما مجهز به هوش مصنوعی!
🎨
✨
اگه به دنبال یک ابزار طراحی جایگزین هستید که هزینه‌ای براتون نداشته باشه، با
OpenPencil
آشنا بشید! این ویرایشگر طراحیِ متن‌باز (Open-Source) با قابلیت‌های شگفت‌انگیز هوش مصنوعی منتشر شده و تمام ابزارهای پولی رو به چالش کشیده.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
پشتیبانی از فایل‌های فیگما:
می‌تونید فایل‌های با فرمت
.fig
رو مستقیماً توش باز و ویرایش کنید.
2️⃣
اجرای محلی (Local):
کاملاً آفلاین و روی سیستم شخصی شما اجرا می‌شه، بنابراین حریم خصوصی پروژه‌هاتون کاملاً حفظ می‌شه.
3️⃣
دستیار هوشمند (Agentic AI):
دارای قابلیت‌ها و ایجنت‌های هوش مصنوعی داخلی برای کمک به پروسه طراحی.
4️⃣
خروجی مستقیم کد (جادوی فرانت‌اند!):
طرح‌های شما رو با یک کلیک به کدهای تمیز و آماده‌ی
Tailwind
و
JSX
تبدیل می‌کنه!
⚛️
5️⃣
یکپارچگی عالی:
قابلیت اتصال و هماهنگی کامل با ابزارهای برنامه‌نویسی محبوبی مثل Claude Code و Cursor.
🔗
لینک دریافت پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenPencil
#AI
#Figma
#Design
#OpenSource
#Tailwind
#JSX
#FrontEnd
#DeveloperTools</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📰
خلاصه اخبار مهم سایبری و تکنولوژی هفته:
🚨
✨
🔹
آمریکا و توقیف AI:
دولت آمریکا برای اولین بار در تاریخ، انتشار یک مدل هوش مصنوعی (
Claude Fable 5
) را به دلیل خطرات امنیت ملی ممنوع کرد.
🔹
هک بانکی در ایران:
یک حمله سایبری سنگین، سیستم ۴ بانک ایرانی را فلج کرد.
🔹
شنود تلگرام:
پاول دورف اپراتور بزرگ هندی (Reliance) را به رهگیری ترافیک کاربران تلگرام متهم کرد.
🔹
خطای مرگبار هوش مصنوعی:
یک سیستم AI در برزیل با رد درخواست بستری اورژانسی، باعث مرگ یک بیمار شد.
🔹
فریب موتورهای جستجو:
محققان ثابت کردند موتورهای جستجوی پیشرفته AI به‌راحتی با یک کامنت هدفمند در ردیت (Reddit) فریب می‌خورند!
🔹
ابطال گواهی‌های SSL:
شرکت GlobalSign به دلیل تحریم‌ها، گواهی امنیتی هزاران سایت روسی را باطل کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#CyberNews
#AI
#Telegram
#Security</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚀
معرفی Prompts.chat؛ خفن‌ترین و جامع‌ترین کتابخانه پرامپت برای هوش مصنوعی!
🤖
✨
اگه می‌خواید از مدل‌های هوش مصنوعی (مثل ChatGPT، Claude، Gemini، Llama، Mistral و...) خروجی‌های تخصصی و بی‌نقص بگیرید، سایت
Prompts.chat
کامل‌ترین مرجع برای شماست!
🔥
چه چیزهایی تو این سایت پیدا می‌شه؟
1️⃣
قالب‌های آماده و کاربردی:
نیاز به نوشتن یه رزومه‌ی حرفه‌ای دارید؟ یا می‌خواید یه قرارداد پیچیده رو تحلیل کنید؟ پرامپتِ آمادش دقیقاً همینجاست.
2️⃣
پوشش تمام نیازها:
از ایده‌پردازی برای کسب‌وکار و تولید محتوای مارکتینگ گرفته تا خلاصه‌نویسی دروس و برنامه‌ریزی تمرینات ورزشی.
3️⃣
خروجی‌های سطح متخصص:
با استفاده از این پرامپت‌های مهندسی‌شده، هوش مصنوعی طوری جواب می‌ده که انگار یه متخصص حرفه‌ای اون متن رو نوشته!
🏆
اعتبار این مجموعه چقدره؟
این فقط یه لیست ساده نیست! این دیتاسِت
رتبه اول بیشترین لایک در Hugging Face
رو داره، بیش از ۴۰ بار در مقالات علمی معتبر بهش ارجاع (Citation) داده شده و حتی در رسانه‌های بزرگی مثل Forbes و دانشگاه‌های تراز اولی مثل هاروارد و کلمبیا هم ازش نام برده شده!
🔗
لینک ورود به مرجع پرامپت‌ها
🔵
@ArchiveTell
| Bachelor
⚡️
#Prompts
#AI
#ChatGPT
#Claude
#Gemini
#HuggingFace
#Tools
#Productivity</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚀
معرفی Upscayl؛ افزایش بی‌نظیر کیفیت تصاویر با قدرت هوش مصنوعی!
🖼
✨
اگه عکس‌های بی‌کیفیت، تار یا سایز کوچکی دارید و می‌خواید رزولوشن اون‌ها رو بدون افت کیفیت به شدت بالا ببرید،
Upscayl
دقیقاً همون ابزاریه که نیاز دارید! این نرم‌افزار کاملاً رایگان و متن‌باز (Open-Source) با استفاده از پیشرفته‌ترین مدل‌های هوش مصنوعی، معجزه می‌کنه.
🔥
ویژگی‌های کلیدی:
1️⃣
پردازش گروهی (Batch Processing):
می‌تونید یه پوشه پر از عکس رو بهش بدید تا همه رو با هم و به صورت خودکار باکیفیت کنه.
2️⃣
افزایش وضوح و شارپنس:
رفع تاری، نویز و پیکسلی بودن عکس‌ها به طبیعی‌ترین شکل ممکن.
3️⃣
مدل‌های سفارشی:
امکان اضافه کردن و استفاده از مدل‌های هوش مصنوعی دلخواه برای رسیدن به بهترین نتیجه ممکن.
4️⃣
پشتیبانی کامل:
سازگاری با سیستم‌عامل‌های ویندوز، لینوکس و مک‌اواس (macOS).
⚙️
نکات فنی:
* این برنامه با زبان قدرتمند TypeScript توسعه داده شده است.
* برای اجرای پردازش‌های این ابزار، سیستم شما به یک کارت گرافیک (GPU) سازگار با Vulkan 1.3 نیاز دارد.
🔗
لینک دریافت و گیت‌هاب پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#Upscayl
#AI
#OpenSource
#ImageUpscaling
#Tools
#TypeScript
#Github</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If0XrLCHtyjFcAEXjglKaagD-490rjrXUm3C04rCQjwKivqRqitZBmSwqvPrhtidI7u8T4g6TJwdaXhXeD1I-GiVMnVwJDHaOF7C8SVSLIWUIeNBAkSMDyyeKEARr0Jb5UxzzFbayGsz3KJz-M_Tnk0Pio5Jh6T-JciPgf196m-Aj_0wmCyg3LnUJc5ICmK6hpYL5CP5rgjRdftces4u3BKy7luGUCUoYsHpkFY1VA64q3byndrCE4xMN64oOzXu74MK7Uz63G1fumvsKCIgUlABVQ8oh0bFLLYCyDBtrElWPAB9Zv-QhVLC6H9NvMETC7VXTwDkIZhxLTZPkneB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcXo1R7x57dup8VvmvlxLikSjnGz6o2F6sRwgc2yDQZ9fy0hle6NjlQOeddH5CwK79w_2FpmgPMP_t6lQ3vMOozaVUspvcMRgoKLxdxMPeDUzGlM4dR508KAn4JJ4qMNznn5Jr7DvX-P220XvSv3rQk7Y50RdsLoq47W9nREPMbnVxGt8OXv-igVkkgWG7DHvFxS0P0_FlZpDibi-L5IrMFsAg11qTfvwIo1ID_Usq4mOU5ADJSuo4vL_NkID4z7GAxYsftoYXCbFGmrdIgsiQH-fyqesTNuj_hl_8M3KHpyRuDcHBxUVBsDPjkOJVPYsPaUh6hsllzkjNL8ivxDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
معرفی Lift؛ هوش مصنوعی رایگان برای استخراج و پارس کردن فایل‌های PDF!
📄
✨
تیم Datalab به‌تازگی مدل هوش مصنوعی قدرتمندی به نام
Lift
رو منتشر کرده که می‌تونه داده‌ها و اطلاعات رو از فایل‌های PDF و تصاویر بخونه و در نهایت یک خروجی کاملاً ساختاریافته و تمیز با فرمت
JSON
بهتون تحویل بده.
🔥
ویژگی‌های کلیدی و برجسته:
1️⃣
دقت و کیفیت شگفت‌انگیز:
توسعه‌دهندگان این مدل ادعا می‌کنن که کیفیت خروجی Lift به‌شدت نزدیک به مدل قدرتمند Gemini Flash هست و از خیلی از مدل‌های متن‌باز (Open-Source) فعلی بهتر و دقیق‌تر عمل می‌کنه.
2️⃣
خروجی ساختاریافته (JSON):
این مدل دقیقاً خوراک برنامه‌نویس‌هاست! داده‌های خام، جداول و متن‌های به‌هم‌ریخته رو می‌گیره و یه دیتای مرتب و آماده‌ی استفاده تحویل می‌ده.
3️⃣
کاملاً رایگان و در دسترس:
این شبکه عصبی صددرصد رایگان و متن‌باز منتشر شده و می‌تونید بدون هیچ هزینه‌ای ازش تو پروژه‌هاتون استفاده کنید.
🔗
لینک‌های دسترسی و دانلود:
گیت‌هاب پروژه
مدل در هاگینگ‌فیس
🔵
@ArchiveTell
| Bachelor
⚡️
#Lift
#AI
#PDF
#JSON
#OpenSource
#DataExtraction
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVF1S9iXIF0_nPevV88Bbz9FVEPmUCMAUIi63286VSQW6o2i5uW8zsbmdi3vSH5tcBpk1DdNG1IV5BoQjOA-ILU6I4viNUxBaDV6EazDxPSWzHkov5MgoyU4zP9P2rrELlqqVHbWVG40c5b2liwJkObo3u-9EXiUD-TjIIHdSZqEu8Z0HfszQC2yLYlI5k3CqVMqLoCfn8aTN11W1XhXudPADbHvq4SE6Z83xfb_JubWhK5itEofB4ty-RlI0xQEqbsgiAbibYHXF2aKVPKfZS_0cqnnmaxF_QxryXQ-27SAyxMdMpLedv6-ln_kl6vdg5wp3B5ILAB3x4KfwLd9YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
مدل Gemini 3.5 Pro احتمالاً ۹ تیر (۳۰ ژوئن) منتشر می‌شود!
🚀
✨
🔹
شایعات داغ:
کاربران شبکه X پیش‌بینی می‌کنند که این مدل قدرتمند دقیقاً در آخرین روز از مهلت وعده داده‌شده توسط مدیرعامل گوگل (۳۰ ژوئن) منتشر شود.
🔹
سوتی عجیب گوگل:
در حین آماده‌سازی بک‌اند برای این آپدیت جدید، رابط کاربری تحت وب Gemini باگ داده و اشتباهاً پاپ‌آپ معرفی نسخه‌های قدیمی (2.0) رو برای کاربران نمایش داده!
🔹
نتیجه‌گیری:
این گاف فنی نشون داد که نسخه وب جمنای هنوز پر از کدهای قدیمی (Legacy) و باگ‌های پیش‌پاافتادست.
🔵
@ArchiveTell
| Bachelor
⚡️
#Gemini
#Google
#AI
#TechNews</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
معرفی WinScript؛ ابزار قدرتمند و متن‌باز برای شخصی‌سازی و بهینه‌سازی ویندوز!
🛠
✨
اگه دنبال یه ابزار سبک، ساده و متن‌باز (Open-Source) برای شخصی‌سازی، سبک‌سازی و افزایش سرعت ویندوزتون هستید،
WinScript
رو از دست ندید. این برنامه به شما اجازه می‌ده اسکریپت‌های اختصاصی خودتون رو برای ویندوز بسازید و روی هر سیستمی که دوست دارید اجرا کنید!
نحوه کار:
خیلی سادست! تو رابط کاربری برنامه، تیک قابلیت‌هایی که می‌خواید حذف یا بهینه‌سازی بشن رو می‌زنید، یه اسکریپت آماده تحویل می‌گیرید و هر زمان که خواستید اون رو روی سیستم خودتون یا هر سیستم دیگه‌ای اجرا می‌کنید.
🔥
امکانات و ویژگی‌های کلیدی:
1️⃣
حذف برنامه‌های اضافی (Debloat):
پاک کردن اپلیکیشن‌های پیش‌فرض و مزاحم ویندوز مثل Copilot، Edge، OneDrive و سایر نرم‌افزارهای غیرضروری (Bloatware).
2️⃣
حفظ حریم خصوصی:
غیرفعال کردن کامل تله‌متری (ردیابی اطلاعات) ویندوز و برنامه‌های شخص ثالث، و مسدود کردن دسترسی و جمع‌آوری داده‌ها.
3️⃣
بهینه‌سازی فوق‌العاده:
تغییر وضعیت سرویس‌های پس‌زمینه به حالت دستی (Manual) برای آزادسازی منابع سیستم، تنظیم DNS و پاک‌سازی فایل‌های موقت (Temp).
4️⃣
نصب سریع نرم‌افزارها:
امکان نصب گروهی و یک‌کلیکه‌ی تمام برنامه‌های مورد نیازتون با استفاده از ابزار قدرتمند Chocolatey.
⚠️
نکات مهم پیش از اجرا:
* اسکریپت تولیدشده حتماً باید با دسترسی ادمین (Run as Administrator) اجرا بشه.
* چون این ابزار تنظیمات ریشه‌ای سیستم رو تغییر می‌ده، ممکنه آنتی‌ویروس (Windows Defender) بهش گیر بده که این یک هشدار اشتباه (False Positive) است. با توجه به متن‌باز بودن پروژه، خیالتون از بابت امنیت راحت باشه.
⚙️
سازگاری:
ویندوز ۱۰ و ویندوز ۱۱ (کاملاً رایگان - لایسنس GPL-3.0)
🔗
لینک دانلود / گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#WinScript
#Windows
#Windows11
#Optimization
#Debloat
#Privacy
#OpenSource</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKC_SReqqIS4l7HX8mHvC5X5fCx0botlVhT_TT5jMv60qxwRE6JDaofN_iunhmQ5YPpGGllZHcZ2hjlIpnpoQtmTTAEHH8zZ6ooJJ_YdI6wZCB7moiv5kMqaHaRhajf2o7dElM1KWTqz7lzjpOtogBsMybJTqX7nAT0E0-byfsznV6zVh9ju-bdfz1YR2kyWY-kaHN3hBSx4RSVw8D9WRPfx4V-LdFpt6QHI2NzyLcz3q4BAhWkzo-iEhhZZC3eLuuFM_dkjHlav0LYYz5rbEvhkHj0uduxIzXB8t9Rj0yg1JRJxA3-675bwVeDqO4Km12mMjn_Q5cL5R8iFWqlnDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با GeoSpy AI می‌توانید محل احتمالی ثبت یک عکس را از روی جزئیات تصویر پیدا کنید.
•
🔹
تحلیل جزئیات عکس و مقایسه با تصاویر آنلاین
•
📍
ارائه مکان‌های احتمالی همراه با مختصات
•
🎯
مرتب‌سازی نتایج بر اساس احتمال تطابق
•
🏞
دقت بالاتر در مناظر طبیعی و معماری خاص
🔗
لینک:
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UItG_Rxn9no2ifyGidYnttVtclM4RHv4RD1IrZrBnEH_BxvjOGin9V6O_SSkeTm1oQy3giPR0pkkkW4-D-c7Ocy4BScaMNhRGuvm_Hv904qRm08G1T7MQltpCoU_PDqI2CceI5yCg4VK5fvQe7z8wnUO6pXcbuM6jNIuNq8Q1C5ZAVvkCRx-t0S8EJjySAdxpnWHmw8hgwPCIJbparDZE_L9YSpyDreL5E0QBJK_tha9Ssw-UbFQVfNasan5PuqOsXqBdRQmsneDygdg2ykY2h4m_AAG6VnrT-LhHrq9T3hTBu50FSC9PrwntK5qzX9qJeyC1oCn0x4z7e6QI-Ujqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی کاملاً رایگان به مدل‌های هوش مصنوعی با Unlimited AI!
🤖
✨
اگه دنبال یه راه بی‌دردسر و مجانی برای استفاده از مدل‌های هوش مصنوعی هستید، سایت
Unlimited AI
دقیقاً همون چیزیه که نیاز دارید!
🔗
لینک‌های دسترسی سریع:
🌐
وب‌سایت اصلی:
🛠
اسکریپت واسط (Transfer API):
اگه برنامه‌نویس هستید و می‌خواید این سرویس رو به پروژه‌هاتون متصل کنید و ازش خروجی API بگیرید، این ریپازیتوری
گیت‌هاب
کارتون رو راه می‌اندازه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#FreeAI
#API
#Tools
#Github</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=iasLFR_2uCYF5ML3XqicrQxBCEYmGapxzyk28fBQdqcMoI_Q61-U1hqHLtKBSVdS7AeBs7xA9GtrTSeEBRJXsKn_Op-g_E0I0kgYDSGn9SRtfW_PJwPsHpwfWmBunhLZLay2kOKfO1tp5d-CxuxQY6BEoXNNOQeG7SeUPiE8zaQdHtxWhtYwlCFoId2udA5y--otYLwj_UNPrHVq2PtwSIoaoAMR3htSpfky01QtBRYp5k69tCbLaUMdoGK0KhxN3KbL8wEH9u1sbAYha_qtQCxxCRIwt0VmtSvmoiZp8Vy826E6aD4qHGtxa-1y-t_6ev0QF94YJH6ixcsZe7UcwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=iasLFR_2uCYF5ML3XqicrQxBCEYmGapxzyk28fBQdqcMoI_Q61-U1hqHLtKBSVdS7AeBs7xA9GtrTSeEBRJXsKn_Op-g_E0I0kgYDSGn9SRtfW_PJwPsHpwfWmBunhLZLay2kOKfO1tp5d-CxuxQY6BEoXNNOQeG7SeUPiE8zaQdHtxWhtYwlCFoId2udA5y--otYLwj_UNPrHVq2PtwSIoaoAMR3htSpfky01QtBRYp5k69tCbLaUMdoGK0KhxN3KbL8wEH9u1sbAYha_qtQCxxCRIwt0VmtSvmoiZp8Vy826E6aD4qHGtxa-1y-t_6ev0QF94YJH6ixcsZe7UcwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوشی‌تان را به کنسول رترو تبدیل کنید؛ صدها بازی کلاسیک مستقیم در مرورگر.
•
🕹
بازی‌های PS1، Game Boy، Sega و پلتفرم‌های نوستالژیک
•
⚡️
بدون نصب، حساب کاربری یا اشتراک
•
📱
💻
قابل اجرا روی موبایل و کامپیوتر
•
🎮
پشتیبانی از گیم‌پد
•
🆓
رایگان و آماده اجرا
🔗
لینک:
Site
#Gaming
#Retro
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tbp1mRmlZa-yjpPhMCiAp1GqjGvlX8ZvS78Db1adp6dUJvriIB0vb6bS6GPppkxtQjY-j0JAvmuZfV1-TgypmLJyii46c0ysEZQJfwTh9YQV1o6W1WQH1gOpNflzSifcKm9VUE_UJ2S5-Vyw7GJc83Trm0DyGWUNo2TUxhT67agv0xil70gPbZSLYjA3MAuPfE_J6fwwR3VPE7imp9wiPo6La2GbRTO0U5hCB0Wf774QdbDY7kNKTO3LkZBtht3QDOX4wzcilTuWwXbxi3UDvjNS28Seg_v00ai2tBN5h9uf-ejO2Uuk_E3liavwuG1SwaDT2_zuz4UPG-Z4hRPkbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به API مدل DeepSeek-V4-Flash تا ۲۸ ژوئن!
🤖
✨
یه فرصت بی‌نظیر! می‌تونید مدل جدید و فوق‌سریع DeepSeek رو تا ۲۸ ژوئن (۷ تیر) از طریق API کاملاً رایگان دریافت کنید و بدون پرداخت هیچ هزینه‌ای برای توکن‌ها، پروژه‌هاتون رو باهاش پیش ببرید.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
تولید کد و اتوماسیون:
ایده‌آل برای کدنویسی و سناریوهای عامل‌محور (Agentic).
2️⃣
تحلیل و تسک‌های فنی:
عملکرد عالی در تحلیل داده‌ها، تولید محتوای متنی و حل مسائل تکنیکال.
3️⃣
پروتوتایپینگ سریع:
تست سریع ایده‌ها و ساخت نمونه‌های اولیه بدون هیچ نگرانی بابت هزینه‌های API.
4️⃣
پروژه‌های خلاقانه:
خوراکِ آزمایش و پیاده‌سازی روی ربات‌ها، سرورهای بازی و سایر پروژه‌های خاص و غیرمعمول.
🔗
لینک دریافت رایگان
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#API
#AI
#Free
#DeveloperTools
#LLM</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6C4JzMXVmw0pkLMaOjbHnxQby8_nUgGJP61CVWX2FEAooiu2PW6EIvPyhY1_gqC0B21AdxUYU7ta_hOYQaXYazxEj0i9xbVqmGiNOD0eUyHpCjYQ7Gl5VgrW7oMGzDz-dMYjSGOpzAEBazYXzK7UuYmU1I869_OZH1d6ay9wgp60ynB1xKa9_-KCOMwIHtc59P3n1Cid4b2U2CNTJg5huELUoP0c7jHPcJ2awmL2WzoMllrzliBNOjL6L15_pULakOBEaiVmIrdAKqTja6BMI9I_QYWO2KUtSS747uh4noRq_PiJGUuQPfv2v82puwdU4hTXfHW2TrHgnU5ezlp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت یک ماه اشتراک پلاس رایگان پلتفرم HotGen AI!
🤩
✨
اگه به دنبال استفاده از قوی‌ترین مدل‌های تولید عکس و ویدیوی هوش مصنوعی هستید، الان می‌تونید اکانت پلاس پلتفرم
HotGen
رو به مدت یک ماه کاملاً رایگان دریافت کنید!
🔥
مدل‌های قدرتمندی که براتون باز می‌شن:
>
🔹
Seedance 2.0
>
🔹
Kling 3.0
>
🔹
Google Veo 3.1
>
🔹
WAN
🛠
مراحل دریافت (بدون نیاز به شماره و کارت بانکی):
1️⃣
وارد سایت
https://hotgen.ai
بشید.
2️⃣
خیلی راحت با اکانت گوگل ثبت‌نام کنید.
3️⃣
توی داشبورد کاربری‌تون، بخش
Tasks
رو باز کنید.
4️⃣
هر ۶ تسک ساده رو انجام بدید (ساخت یک عکس، ساخت یک ویدیو، اشتراک‌گذاری و غیره).
تمام! اشتراک پلاس شما به‌صورت خودکار فعال می‌شه.
✅
🎁
با این اشتراک چی می‌گیرید؟
به مدت ۳۰ روز، سقف محدودیت‌های تولید ویدیو و تصویر برای شما به‌شدت افزایش پیدا می‌کنه و می‌تونید از بهترین مدل‌های روز دنیا با بالاترین ظرفیت استفاده کنید.
(البته جمع کردن توکن به این راحتی نیست. زاییده شدم
😂
، الان تست کردم)
🔵
@ArchiveTell
| Bachelor
⚡️
#HotGen
#AI
#Free
#Kling
#GoogleVeo
#VideoGeneration</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
معرفی Remnawave؛ پنل مدیریت پروکسی قدرتمند و مدرن مبتنی بر Xray-core!
🌊
✨
اگه دنبال یه ابزار حرفه‌ای برای مدیریت زیرساخت پروکسی می‌گردید،
Remnawave
با تمرکز روی سادگی و راحتی کاربر طراحی شده است. این پنل به شما اجازه می‌ده نودها، کاربران و اشتراک‌ها رو در یک رابط کاربری وب بسیار تمیز و به‌صورت یکپارچه مدیریت کنید.
تمام بخش‌های این پروژه (بک‌اند، فرانت‌اند و نود) کاملاً با TypeScript و با استفاده از فریم‌ورک‌های NestJS و React توسعه داده شده است.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
معماری ماژولار و بهینه:
دیتابیس، پنل وب و صفحه اشتراک (Sub Page) کاملاً قابل تفکیک هستند. یکی از بهترین قابلیت‌ها اینه که حتی اگه پنل شما آفلاین بشه، نودها بدون مشکل به کارشون ادامه می‌دن!
2️⃣
مدیریت حرفه‌ای کاربران:
تعیین محدودیت ترافیک، فیلترها و قابلیت جذابِ محدود کردن اتصال به دستگاه‌های خاص از طریق شناسه سخت‌افزار (HWID).
3️⃣
مانیتورینگ و امنیت بالا:
مانیتورینگ لحظه‌ای ترافیک کاربران و نودها، پشتیبانی از ورود با اکانت تلگرام (OAuth)، احراز هویت دو مرحله‌ای (2FA) و هماهنگی کامل با Cloudflare Zero Trust.
4️⃣
امکانات ویژه:
تولید انواع فرمت اشتراک (مثل Mihomo و Sing-box)، پشتیبانی از وب‌هوک (Webhook) برای کاربران و نودها و ابزار داخلی برای اعتبارسنجی کانفیگ‌های Xray.
﻿
⚙️
حداقل سیستم مورد نیاز:
برای نصب این سیستم قدرتمند (از طریق داکر)، به
۲ گیگابایت رم
،
۲ هسته پردازنده
و
۲۰ گیگابایت فضای ذخیره‌سازی
نیاز دارید.
🔗
لینک‌های دسترسی سریع:
داکیومنت
گیت‌هاب
داکر هاب
کامیونیتی
🔵
@ArchiveTell
| Bachelor
⚡️
#Remnawave
#Xray
#Proxy
#VPN
#OpenSource
#TypeScript
#Tools</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJep8DciTh5bok_ispoOF4C9FnvFNry6K301TEnltM9YuXhA0I3tqqgEdSLgXR52jzEwACFwx-DcIvkuBhsXraBmj79QtfvM57DsTsiEviaRcyp9boRBEgyEoZMcjiu73PX2B-tUzPazZU3P0wzGsTMBsGoXfeoiequuy0kJFCcYea69UhnZuYgh-oXEiu8jkwASvv_vkiK3yQeY_H-BNZ0f9f78MPhRNMwoHcHoRJhdLep9TGXlENmxims0yLcNX7U_wXeRQL55W3uRp3NDzEGbdakHE5GJNiIKZwEoQHt5e5tx93jY9SyKrVtotgSGQ7Aju8b9rkWLwNgJs2p9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
یک کتابخانه رایگان از پرامپت‌های Nano Banana برای ساخت تصویر با
AI Studio
منتشر شده است.
✨
قابلیت‌ها:
•
🔹
پوشش سناریوهای متنوع برای تولید تصویر
•
⚡️
قابل استفاده رایگان در AI Studio
•
🗂
دسته‌بندی منظم و جستجوی سریع
•
🔄
به‌روزرسانی مداوم با پرامپت‌های جدید
🔗
لینک:
Site
#AI
#Prompts
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚀
معرفی Ladder؛ عبور از پی‌وال‌ها و خواندن رایگان مقالات پولی با یک کلیک!
🔓
✨
🔥
🔥
🔥
اگه برای خوندن مقالات، اخبار یا کتاب‌های معتبر تو سایت‌های خارجی با درخواست خرید اشتراک و صفحه‌های پرداخت (Paywall) مواجه می‌شید، ابزار
Ladder
این مشکل رو برای همیشه حل کرده! این سرویس با شبیه‌سازی رفتار بات‌های موتور جستجو، بهتون اجازه می‌ده محدودیت‌های هزاران سایت رو دور بزنید.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
دسترسی نامحدود:
باز کردن مقالات پولی و ویژه در سایت‌های معتبر علمی و خبری مثل WSJ, NYT, Bloomberg, The Atlantic, Nature, Science, The Lancet و کلی سایت دیگه.
2️⃣
وب‌گردی بدون مزاحم:
حذف خودکار تمامی تبلیغات، بنرهای پاپ‌آپ، ترکرها (ردیاب‌ها) و اسکریپت‌های اضافی، تا یک تجربه مطالعه تمیز و راحت داشته باشید.
3️⃣
نصب و اجرای منعطف:
می‌تونید این ابزار رو روی سرور شخصی خودتون (Self-hosted) یا حتی به‌صورت لوکال روی سیستم (PC) نصب و اجرا کنید.
🔗
لینک دریافت ابزار
🔵
@ArchiveTell
| Bachelor
⚡️
#Ladder
#Paywall
#Bypass
#Articles
#Tools
#OpenSource</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNTzCd2vK1f93U_CJo3zTAk5y_Ag1ozoZzO5uAJGL0-DXJsHoHScQvLHhlIRLIzvUTHaqfBI_Y-ixseKDhndSukx-fG6PwiQc9z654brXW2FsvE5N57pMH6GLREcZC4ZP04FBT86WbjQmXAefflP23SN2mP2RnLZLAu8OVKvnTLT7ABVkwae6WYdoJCbnNAEBI8nRgMzp63ytFGQgvbqU48YLjvp-8Q1YnwNCrT3t__c1dvkJL1KzgSvoL1YCwxi_AII40P4A_NVWHJ21VvIIDSMm4jDAZtQpEUUhFSxyfG_7LtfZmiXeLKehkXDBzJ8QTbKUWqjSNAZEyXFO1fyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
بازی‌های کلاسیک کنسولی را مستقیم داخل مرورگر اجرا کنید؛ بدون نصب و دردسر.
✨
قابلیت‌ها:
•
🎮
شبیه‌سازی کنسول‌های Nintendo، Atari، Sega و دیگر پلتفرم‌های قدیمی
•
⚡
انتخاب بازی و اجرای سریع از داخل سایت
•
📦
امکان آپلود فایل ROM برای بازی‌های دلخواه
•
☁️
همگام‌سازی ذخیره‌ها با فضای ابری بین دستگاه‌ها
🔗
لینک:
Site
#Gaming
#RetroGames
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎬
معرفی OpenMontage؛ استودیوی شخصی و هوشمند شما برای ساخت ویدیو!
🚀
✨
اگه تدوین ویدیو بلد نیستید اما ایده‌های جذابی تو سرتون دارید، ابزار جدید و متن‌باز
OpenMontage
دقیقاً برای شماست! این هوش مصنوعی خفن، فقط با خوندن توضیحات ساده‌ی شما، یک ویدیوی کامل و حرفه‌ای تحویلتون می‌ده.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
صفر تا صد اتوماتیک:
از ایده و سناریونویسی گرفته تا پیدا کردن متریال (عکس، ویدیو، موزیک)، صداگذاری و تدوین نهایی رو خودش انجام می‌ده.
2️⃣
الهام‌گیری از یوتیوب:
فقط کافیه لینک یه ویدیوی یوتیوب رو بهش بدید تا سبک، ریتم و حال‌وهوای اون رو تحلیل کنه و یه ویدیوی جدید با همون فرمون براتون بسازه!
3️⃣
اتصال به ابزارهای مختلف:
این سیستم به ده‌ها هوش مصنوعی دیگه (برای تولید عکس، صدا و موسیقی استوک) وصل می‌شه تا باکیفیت‌ترین خروجی رو بهتون بده.
این ابزار کار رو برای تولیدکنندگان محتوا، معلم‌ها و هرکسی که می‌خواد بدون دردسر ویدیو بسازه، به‌شدت راحت کرده!
🔗
لینک ابزار (گیت‌هاب)
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenMontage
#Video
#AI
#ContentCreator
#Tools</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZUjtKnu2S4X8zAE9Om_YVTiRJQZUUd4bGuaQQ6Jl46Y0DCMDAS8D_MQsyU3p0LoJ7mPNdms3M45A_YSk778HhGKll_Q4ctI918q9O7tIDU97-7AR3M5vDHkpfUESLdCc16BV1z-q9KNKhUR3EqS958f8a84z7acR46s32FAVLDf65o96XtPqVt2CU31DQ-G-ls3O0xEBK5Kp2PVSBsrBhTcJdSyeXAVkxSrYGXJwOAPJtAtnlZ5QwWUGo1Y1M0xFOwX7H7L34X3aI0QJnwZr90LxrYo6R1DGY38d8uY1-15GH5clTsQtT0cQ-lspmr6AYnFsvs5AYDFcHV6aFiL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJtaAoLIQknR6qwA6ZdmsYHAkqs-m2IDdZ-KFiONz5mZKAXPZLjj9QbkQbMsXlDmybZiodegMbnVlhrHrOn_1Wr8grsfCJJ625vgiqylzs3C1EGOtyiaV1yDMS2OpX9Yba5_1aNLCxywWlXZQK2d-hFO-P9o_SilnXKwadgFvOQBXFUxfJCjiMx_2-n-lQQTMPTVcZ_5WhrzZOrJdQ0ew_s41U-uKLavtLEpD7Q61Po4TwlGRhkKpCNVKBG2zwsCgS9j5Et4Ts7RUHem0nSK4qtQwcI3Lr--pMDfHbrGhv8mtIb5aJ_1SdzuoKcEvSmbDtOD4MLoEFVH96jmUmKqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKOyb2vVdcwsurjA7wKDctWYx44yINyUiUUR27WTAv-STRuyOmPFPWDlNTbaKTKh7V4QWy46MQBUbmW8rdYGWpIrWKI8_Q4BIu3bEKrHcOMxiQrUMHnJw3J8KJf7AEE4z_XfGxlAR8tPlRU65IGtMAJHcmJKFASsDcVjL9Xyij9yluPPAUoXH9LWUVtRj4v54MPVKfVSTObwlX5OY4FiCr2pDvg2AH-8L29sCasKpRKEvyizYUrsfbnsbFQDOdy7ns0m0CwRCoc6GfKUp6Ussfr7Fu1sGbkHVmuoiakBnhevSnv4HuHepUe-cpE6c9nbukwv-1t3STAyTVvwMaqUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2rgSyYLfo_a4M2Ww6ht4NP4S6gQ9Wgi_NNNYFfvqATP2Lo9nmOktrC1PfBt0Ygh4b1pS8AVhodpWw6d_JasDGcLWNAUlV3g3ECKUyLYqM6Hl_f4M1wsi8oehxjYR_51JgMyo6YP_i45lsup2zmemSbWfbrnk4HmDr1qM6lZYH7WprAP_eRyu_gz5RvGpXiHUZQDQtMcaZc_0yEYjVxB16Zz7WGUtcY6mH2XwVpk1pgE3LHnVjmqAKomknqx7WhJPcwK6zhkAphLdJNQKqwJL5UUmWhZ7O67-Vzg65eYTvJQ5CpjgWeWUdmzEohWsbVz99qB5m6l69lf0SRx0_691A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Splayer
پخش‌کننده موسیقی متن‌باز با قابلیت دانلود از یوتیوب و اتصال به اسپاتیفای
🎵
✨
قابلیت‌ها:
•
🔹
پخش فایل‌های محلی و مدیریت موسیقی‌ها
•
⚡
دانلود صوت و ویدئو از YouTube
•
🛠️
واردکردن پلی‌لیست‌های Spotify
•
🎧
متن همگام‌شده آهنگ‌ها، پادکست و کتاب صوتی
•
🎚️
اکولایزر پنج‌باند، ویژوالایزر و ویرایشگر صوتی
•
🎨
شخصی‌سازی تم و رابط کاربری
🔗
لینک:
GitHub
#OpenSource
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚀
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
تبدیل سایت به اپلیکیشن: هر سایتی که فکرش رو بکنید (مثل ChatGPT، یوتوب، ایکس/توییتر، اسپاتیفای، دیسکورد و...) رو به یک برنامه دسکتاپ مجزا تبدیل می‌کنه.
2️⃣
حجم فوق‌العاده کم: برنامه‌های ساخته‌شده با این ابزار تا ۲۰ برابر کمتر از اپلیکیشن‌های سنگین مبتنی بر Electron فضا اشغال می‌کنن.
3️⃣
سایز مینیاتوری: میانگین حجم هر اپلیکیشنی که باهاش می‌سازید فقط حدود ۱۰ مگابایته!
4️⃣
مصرف بهینه منابع: به لطف استفاده از قدرت زبان Rust و فریم‌ورک Tauri، مصرف رم سیستم به طرز چشمگیری کاهش پیدا می‌کنه.
5️⃣
پشتیبانی کامل: این ابزار کاملاً رایگانه و روی ویندوز، مک (macOS) و لینوکس بدون مشکل کار می‌کنه.</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSDqz_dcEX6QxdMV5qTXBdxW2ykzaQojWhJELuQI1I1A8fJ7Y5Z1k5PWEawQvFkIRacZEGhExa6Hh_IApEL2y65KLSn2PXuxR7yFeiGZPzofEUrdkMUEA1mb8LnGWVwbEL3IXGT0jngD0VPKZ5plwlaZxBKeQNUOuOo08tCQcSo1iJ1jd5RHk_QMIiIv_p3gGTzeGaoibxaUFCYAlm9fk3YqSJJIjaLzxljbAPW7-4nPXw-mg_jv6htjPfPSRW7bY41lP10eU3kKeEwgCA2U1X2PPxEraC9s8dqGNUT5GIv7cc5Rq2fJ89ycm80IqFqN-_TWRvutoL0dbTiK-lml2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYZSsk6cJXTnsvWrLAMbwtvLgL2m6RPMHiXO-SnMM-20khFEQFVVheB6UCqk8ZRWlnzMMXd5f7lf9g9vseGo9x0fPJ8KiDf2qq3mNhlz0JDVe3dCBRhRmu2JkIFXmgKK4sCwKToRm3Shr0dOmUBsw6jbsF34XhNzCyUrO8-4jsS-62GpV-lLruHMuqfoPdukCJYHgPOUZGovXsiHta4w1vJiIPqWyXKSilX0uKOB0KhNbEoQRNrroxpUf2y3R8EBWeFxGzmp_1wy5nfWTM7v93m58wqHSJ3EZUkQBVDyvuFYJ7Eh21u6erFcEwfxPGUAZdL_QDmTwi55Z7qSzd-hCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SeuRINSVAbQoNDqOuLVDfoa9c9GnKYGkcWeRvNgrDSkUiMKcjwXofYO5YQyWnPZXHgQLCyiWpf_tQPpj2SWw0vGyGLLUXS3vkI23rBQVTzV80bvkj_n0Zms33u-wvpaKyW3Jg11EXhCX1n6KJsYMj1C9CuJMfvh1yhox66BBODPqURkaELc1G-JXIUjwbs0rkLxdp1_HlEnEK-YJrwzWMCF3GBNgY1YSBaF0qUUBqFXtskdoITcr0FKtqND3dn_E8c1Q02_ljWh6-uObJCtJijgpoJ2LCU0XbjoO_rsXEFKCrk6r0p4siR_XJ1sH0caftT0kg1kldlRQxlzOd6UBEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BaiAD8RhJh6bNOXio-dcNVFw4dbaZb3lCwxcAmRkwqrYSjrSH1fql2FM0DtJ2NB4xz1YQg8NqEFDdosDsmj3ffmEcrcHVqtjUdBki2Ukdxe_c2LxwAD1fWuo_B1rgCK5Inm1qYP7mAC-t9cqUiFZzsUOzMEkFLDo1qApSQI2ukc0oXPoY1KOAM6u_U3W5XLGLb7OnGBTDxJ2W5GD6cRZV4ehx-vOf2Ih64PlSQ1kyqXqdfO_7qScKH6ZjMAIb8oR2EUDK7PHb2N3pCpsPcwc9_4Ae2FPzmqKy9VDq3Ix2Gv1t1x2JWB_jssM3MBuO0vSNor6C2Qsg9eyB58Kuj2ASg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=Dpl5gnAnRrUsw7ROxj8z9IOXpW3j_w-o99s84AAB59nJnxZ7JUS0kvtbCrF9TzTWZM-8BdqWUik0eClCwUIgqn8AJKFope5wXVD-xE5ipaCLaJbg9hMShRrxtzEUM0Id9LFgjxCYqmwWp2hdLSvnhTe6EMM5APFHwSTOXmcMDCKr2PzEBr4bMeR7SKyxijArBLTWrO5zz4VYa0nKEkvQ9KO_rvSb75j2cpVM83uoi9CG1-vgNWj6Bio72yPHtPSIZ3MFsIb9j3dr-HR03DzHvQBea-9hZtoNRsSPmVuykJcEY8tBMhxLftU9-SKyY-mx4BWtkk4MRgfxrK3INymaHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=Dpl5gnAnRrUsw7ROxj8z9IOXpW3j_w-o99s84AAB59nJnxZ7JUS0kvtbCrF9TzTWZM-8BdqWUik0eClCwUIgqn8AJKFope5wXVD-xE5ipaCLaJbg9hMShRrxtzEUM0Id9LFgjxCYqmwWp2hdLSvnhTe6EMM5APFHwSTOXmcMDCKr2PzEBr4bMeR7SKyxijArBLTWrO5zz4VYa0nKEkvQ9KO_rvSb75j2cpVM83uoi9CG1-vgNWj6Bio72yPHtPSIZ3MFsIb9j3dr-HR03DzHvQBea-9hZtoNRsSPmVuykJcEY8tBMhxLftU9-SKyY-mx4BWtkk4MRgfxrK3INymaHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با Pake هر وب‌سایتی را به برنامه دسکتاپ سبک تبدیل کنید
یک پروژه متن‌باز برای ساخت اپ دسکتاپ از سرویس‌های وب مثل ChatGPT، YouTube، Spotify و Discord و ... است.
✨
قابلیت‌ها:
•
🔹
تبدیل هر وب‌سایت به اپ جداگانه
•
⚡️
اجرای سریع‌تر و مصرف رم کمتر
•
🛠
ساخته‌شده با Rust و Tauri
•
📦
خروجی کم‌حجم، معمولاً چند مگابایت
•
💻
پشتیبانی از Windows، macOS و Linux
🔗
لینک:
GitHub
#OpenSource
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
ترامپ: شرکت Anthropic دیگه تهدید امنیت ملی نیست!
🤖
✨
به گزارش Axios، دونالد ترامپ بعد از دیدار با «داریو آمودی» (مدیرعامل شرکت Anthropic) در حاشیه اجلاس G7 اعلام کرد که دیگه این غول هوش مصنوعی (سازنده مدل‌های Claude) رو یک تهدید امنیتی برای آمریکا نمی‌دونه!
🔥
جزئیات و حواشی این توافق:
1️⃣
ریشه اختلاف:
قبلاً سر آسیب‌پذیری و باگ‌های خطرناک «جیلبریک» (Jailbreak) تو مدل‌های
Claude Fable 5
و
Claude Mythos 5
اختلاف شدیدی بین دولت آمریکا و این شرکت پیش اومده بود.
2️⃣
اقدامات قبلی دولت:
وزارت بازرگانی آمریکا تو ۱۲ ژوئن محدودیت‌های شدیدی اعمال کرده بود تا دسترسی تکنسین‌های خارجی به این مدل‌ها محدود بشه.
3️⃣
همکاری و چارچوب جدید:
الان Anthropic با درخواست‌های اصلاحی دولت کاملاً راه اومده و کاخ سفید به همراه چند نهاد امنیتی در حال تدوین یک چارچوب فنی دقیق برای ارزیابی خطرات مدل‌های هوش مصنوعی هستن.
﻿
⚙️
سیاست کلی آمریکا در قبال AI:
ترامپ تاکید کرده که هدف اصلی، حفظ برتری بی‌چون‌وچرای آمریکا تو رقابت هوش مصنوعی با چینه و اصلاً قصد نداره با بستن یا تصاحب شرکت‌های داخلی، جلوی رشد این صنعت رو بگیره. البته این رو هم اضافه کرده که در شرایط اضطراری، از استفاده از قوانین سخت‌گیرانه نظارتی (مثل قانون تولید دفاعی) چشم‌پوشی نخواهد کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#Claude
#AI
#USA
#TechNews
#Security</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6fLORB0JGq8clB3uPHflfMdO0eHNIDaieQnkbPlNxHzAUElp4yRF7pbgsA8FO3HYsxO2B0-9aSlpBQvoXG8wIpDSEKF1KXHI1hBqdOVgHH1yZV8JDo2Ws6o3IHox8v5T5ilK2VXW-xjAJerXFlWvvyB1CNHTkCPUhZWcy94MYx7OSdYjHoU7BZj4-_A6kby8aqzdDIRfJt6Xz2WlUFQdhPKOXqqE9EQkT3VPWhBdK5oACEDu833ajOlTrMS0hWIR0I_PdIaWO2wd-aTwonS0nxh2yyPU9RTPYaDTUqj9hjOVEQHf-GOopoly0_AuvRl9TlDmKAATe9d90U1xrX1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">KillerPDF
جایگزین متن‌باز و سبک برای Adobe Acrobat
📄
✨
ویژگی‌ها:
•
🪶
مخصوص ویندوز 10/11 با حجم حدود ۶ مگابایت
•
✏️
ویرایش متن داخل PDF
•
🔗
ترکیب چند فایل PDF
•
📑
استخراج صفحات انتخابی
•
🖊️
نقاشی و افزودن امضا
•
🔒
اجرای کاملاً محلی، رایگان و بدون تبلیغات
🔗
لینک:
GitHub
#OpenSource
#PDF
#Windows
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
مدل جدید Janus Pro از DeepSeek منتشر شد؛ پیشتازی در تولید تصویر!
🎨
✨
استارتاپ هوش مصنوعی چینی DeepSeek به‌تازگی گزارش فنی مدل متن‌باز جدیدش به نام
Janus-Pro-7B
رو منتشر کرده. بر اساس بنچمارک‌ها، این مدل در زمینه تبدیل متن به تصویر (Text-to-Image) تونسته عملکردی بهتر از رقبای قدرتمندی مثل DALL-E 3 (از OpenAI) و Stable Diffusion از خودش نشون بده!
این مدل در واقع نسخه ارتقایافته مدل Janus هست که اواخر سال گذشته معرفی شده بود.
🔥
ویژگی‌ها و بهبودهای کلیدی:
1️⃣
کیفیت و پایداری بالاتر:
با بهینه‌سازی فرآیند آموزش، ارتقای کیفیت داده‌ها و بزرگ‌تر شدن سایز مدل، جزئیات و پایداری تصاویر به‌شدت بهبود پیدا کرده.
2️⃣
تغذیه با داده‌های غنی:
در این نسخه از ۷۲ میلیون تصویر ساخته‌شده (Synthetic) باکیفیت در کنار داده‌های واقعی استفاده شده که خروجی‌ها بصری بسیار جذاب‌تری رو تولید می‌کنه.
3️⃣
مدل ۷ میلیارد پارامتری:
این مدل با ۷ میلیارد پارامتر، درک بسیار بهتری از دستورات (پرامپت‌ها) داره و سرعت و دقت تولید تصویر رو به سطح جدیدی رسونده.
📉
تاثیر دیپ‌سیک بر بازار تکنولوژی:
جالبه بدونید اپلیکیشن دستیار DeepSeek (مبتنی بر مدل قدرتمند V3) اخیراً رتبه اول اپلیکیشن‌های رایگان اپ‌استور آمریکا رو فتح کرده!
موفقیت‌های خیره‌کننده دیپ‌سیک و صدرنشینی مدل V3 تو جدول مدل‌های متن‌باز، حتی باعث شد تا سهام غول‌هایی مثل Nvidia و Oracle در روز دوشنبه با افت مواجه بشه. (شرکت‌های OpenAI و Stability AI هنوز به این خبر واکنشی نشون ندادن).
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#JanusPro
#AI
#DALL_E
#StableDiffusion
#TechNews</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNwxyly-5EPIR6MGf1Y1506t9UbC23ue2UPvIi7R8uYrxf8vw73LZdYQ9ipoRy5KqehG8FEjw36apCJKtIsGFxyUEmqYuqBFS2K4wixyfcB0salIm8hv80WxVeYB6VZB8l7HItOtflqHR_qJKhv03FgvtMCuGs2KMbdshqPBk2zowLuNgHDzZ4-7KV8mfV57yvsY_L-vc_TDrGnZd0oZcZK9MUFSq9ln33jrvnEpVwfthUMffxiL-KcgF67ifrirEbLmvSnjxdlnKDaSvGkZUb5QMyYurmJ1fOj8BhlJfenmOO-nbKwfMBjHytbJC-xPwk-7W0jIMaJNA2R7NtchtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJ7jV6nL3j7nkNeOSEMiB69jT5sgxWHr5RWQSARgCY44F9scvss3H1-Rr3xuIxeKwl1zKmk5KwkOpEdAjWbBW6pnhOD6LwHWFo7kg5REKZYOI3cVp1HIJiF50RM2RgeQFYTr7BUfu5ljXk3fYO9qOrX761jB5P2SjfHbw9MzynPrUFCjb9ieLNNDFi5ZT4LuhQciKAulAel5Nl1TUMGC1AGuvbuwKpw3lvXccaJR4wpZjfOgG3XxLXPEJb7WMtus7KAdeU9bZ8OJIP6rIgA_scVkk9TUFbenZ3Y-6LiqZDJd8fO0W0xjBK5LOhJUzHO4vgz5LT9cFZD5frtFe-EtNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDDElGZVxtmiDCwxhhteCWhHCX14JaWH8rSkxiuWNpFCpqORdRMpj7bmbF3Xhj8-JAH_pfIGi7BX7QdtQ9EU9YXQ5tK25JtKjEXCoI3A8RHqN8Jdx06gSlAZ1Cr2dvrKDj1yXGAOMHkg776qhFpNVzb1VFA9rj_tAPwhtUqotMZgu9fpa113Zde_9XOb4QPYFJxiO5LKO0z1pFVVA3xgFvKDHhhbg-8BLptl7o_5KpCUILEiNcz_kcL5GCGBJM9ByPhaIsSL0cujXkoQP5Fh6BtIYfyVJH1xRtGMCLG4slau9ak8qic9Uyj2p_JfQ8FcXgfzzBGKE5lrABph6PffKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی BleachBit؛ ابزار قدرتمند، رایگان و متن‌باز برای پاکسازی سیستم!
🧹
✨
اگه به دنبال یه ابزار امن و کاملاً رایگان برای بهینه‌سازی و پاکسازی سیستم‌عاملتون (چه ویندوز، چه لینوکس) هستید، BleachBit یکی از بهترین گزینه‌ها برای حفظ حریم خصوصی شماست!
این ابزار با حذف فایل‌های اضافی، کش مرورگرها، کوکی‌ها، فایل‌های موقت (Temp) و لاگ‌های سیستم، هم فضای هارد دیسک رو آزاد می‌کنه و هم ردپای دیجیتالیتون رو به حداقل می‌رسونه.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
خرد کردن فایل‌ها (File Shredding):
حذف دائمی و غیرقابل بازیابی فایل‌های حساس.
2️⃣
پاکسازی فضای خالی (Wipe Free Space):
پاک کردن کامل فضای خالی دیسک برای جلوگیری از ریکاوری اطلاعات قدیمی.
3️⃣
بهینه‌سازی دیتابیس‌ها:
فشرده‌سازی دیتابیس برنامه‌ها برای افزایش سرعت و عملکرد سیستم.
4️⃣
امکانات حرفه‌ای:
پشتیبانی از خط فرمان (CLI) برای اتوماسیون، اجرای پرتابل (بدون نیاز به نصب) و امکان تعریف رول‌های (Rules) اختصاصی برای پاکسازی.
🔗
لینک وب‌سایت و دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
#BleachBit
#OpenSource
#Linux
#Windows
#Privacy
#Tools</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🌐
ارتباطات آفلاین، امن و غیرمتمرکز با Nomad Network (نسخه ۱.۲.۰)
🔗
لینک گیت‌هاب
پلتفرم
Nomad Network
پلتفرمی برای ساخت شبکه‌های مش آفلاین با رمزنگاری قدرتمند، محرمانگی پیشرو و حریم خصوصی است.
✨
ویژگی‌ها:
>
🔹
کنترل ۱۰۰ درصدی:
بدون ثبت‌نام، قوانین یا وابستگی به سرورهای متمرکز.
>
🔹
تکنولوژی LXMF و Reticulum:
مسیریابی همتا‌به‌همتا (P2P) و زیرساخت مش رمزنگاری‌شده.
>
🔹
انعطاف‌پذیری بستر:
اجرا روی امواج رادیویی تا کابل‌های نوری.
مناسب برای دور زدن محدودیت‌ها و ساخت شبکه‌های محلی ایزوله.
🔵
@ArchiveTell
| Bachelor
⚡️
#LXMF
#P2P
#Reticulum
#NomadNetwork
#Mesh
#MeshNetwork</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=lA5zV8ODe7ZOtUyfP0287cqKNeRNTGJpD7AlltE0LoEZlCRYymQQPuWBsGtbLhCKTUuBxida81IMWKEn9_dPbJz3Kd9n9x_j2qsxZXLP2nliJitsjYtx3Xf6ToG0EFzFtYTzKpyMwFZigplsSyYcQQXkC_LvkR2i3meHeFT-MzrmDNGpR90q0zzFQ1fDAyY2xV1bJDOzV3l72H4CSAHdULFhqm8stN76Fe1e3uQZarY5Ek46S4BMaUbBj9f-v8uJ8-jkWnq5W_QPkrXwypRzCnTTr9X35Fd8TTGoiQFdpMcv0_xGJiuJofNA37c-Ax7Ps3G6Hxus0CVBfqT_JOqNmILBoVfPZtmVzIAvkgXTHrAmxtK7dvMuocB1rwi23lN9IhV8LFoxB30f1AOlBk8sNZHcZvEua2X6f-ofcdmMEXj_xs4-CSb0wM963lO5payCqArL_P7i3gPtuk0A6X3ZFgfFYSUL8JSPge4C5utOjWn74lEmaV2VqQF0VIB6exr61bFtPNCevWi0Jm9NuuLh3g5j9ZyhM3-bRqvDHcGGfg9SFQbxoXJYLHIawWIyq1mH5H-RNuoZ5e4R8AqUTQ_h2CJjXiZUfOQz-MW8fhr1BbodAofD_Cgea-pIi5snfLScPtMsCHv5HO35IeU9rsIueyufcnTqZ7JBfOGO_JcLLMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=lA5zV8ODe7ZOtUyfP0287cqKNeRNTGJpD7AlltE0LoEZlCRYymQQPuWBsGtbLhCKTUuBxida81IMWKEn9_dPbJz3Kd9n9x_j2qsxZXLP2nliJitsjYtx3Xf6ToG0EFzFtYTzKpyMwFZigplsSyYcQQXkC_LvkR2i3meHeFT-MzrmDNGpR90q0zzFQ1fDAyY2xV1bJDOzV3l72H4CSAHdULFhqm8stN76Fe1e3uQZarY5Ek46S4BMaUbBj9f-v8uJ8-jkWnq5W_QPkrXwypRzCnTTr9X35Fd8TTGoiQFdpMcv0_xGJiuJofNA37c-Ax7Ps3G6Hxus0CVBfqT_JOqNmILBoVfPZtmVzIAvkgXTHrAmxtK7dvMuocB1rwi23lN9IhV8LFoxB30f1AOlBk8sNZHcZvEua2X6f-ofcdmMEXj_xs4-CSb0wM963lO5payCqArL_P7i3gPtuk0A6X3ZFgfFYSUL8JSPge4C5utOjWn74lEmaV2VqQF0VIB6exr61bFtPNCevWi0Jm9NuuLh3g5j9ZyhM3-bRqvDHcGGfg9SFQbxoXJYLHIawWIyq1mH5H-RNuoZ5e4R8AqUTQ_h2CJjXiZUfOQz-MW8fhr1BbodAofD_Cgea-pIi5snfLScPtMsCHv5HO35IeU9rsIueyufcnTqZ7JBfOGO_JcLLMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Palmier Pro
ویرایشگر ویدیو نوآورانه و رایگان که با هوش مصنوعی کنترل می‌شود
📹
•
🔹
اتصال مستقیم Claude، Cursor و Codex از طریق MCP
•
🔹
برش، تنظیم ریتم، صداگذاری و افکت‌گذاری خودکار
•
🔹
درک رابط کاربری توسط AI بدون تنظیمات اضافه
•
🔹
ابزارهای جانبی برای تولید تصویر و ویدیو
🌐
Site
#AI
#VideoEditing
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT0tvxJPz04NrwPAltc2F9YNXrvJ5WF1QAO2hOCbdGHSMlERKq5m1JSUVN4ZAW81buwTjtf1PfVEwWD01sLP6L5h5jUArUyjUz1KL-KJCvUnpsWCwpdNA39ib8vZMibO-9M7_Y-J6Rro8O5Yh5tlJpRcBhXbkK5gRzQGQO0trnTG9DkzxJakxSyQAxIxy2bOtKX5O5G2VktrGaudMXo0PbHjGr47XKyaSpPPtChLKnEKVsJMaKBjW0tFQGuugX5hZOGE112btW_LkWzicGuhD03S21i6GgMabNLXSyy1CSuVYIalzm1moSImJ2mZaVsdQs6XN5aOBO7yb2qQucZJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE5TEuorCRghF3Oj_TrH_u2auNHA5iyEMWhcbEABvngbl1P6X0XgA-wEkZvHBjGfTNd3VRQCcKAv97B4BUhIITVoXMx38Mr8T7A2IrHNllZ7ViBdmaRrG9P5G8o17ra6KSuB6iCrsm1qTtGoOGHQX_KfcRzmVl61c3JO8w7CBPVlu_2MTwjV0d-RSnGy44XPnr8AWbPkqfAgjKWGBSH6xooycy6SvsZl50fsq3j9ur5kFIam8NRwyCUCbQRlxKnM4n5YNW_inS3qJwWg9LkFoN7jFXeY5ILEPcRTL_MXcyktMeobJtXtQXZbVVl05bv3tky_KKOls2OzJ2lbH2aEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
آموزش استفاده از مدل‌های قدرتمند GLM در ابزار Claude Code!
💻
✨
اگر از Claude Code (ابزار برنامه‌نویسی محبوب مبتنی بر ترمینال) استفاده می‌کنید، الان می‌تونید با اتصال به پلتفرم Z.AI، مدل‌های بی‌نظیر سری GLM (به‌ویژه نسخه جدید
GLM-5.2
با کانتکست خارق‌العاده ۱ میلیون توکنی) رو جایگزین مدل‌های پیش‌فرض کنید!
🛠
مراحل راه‌اندازی سریع:
1️⃣
نصب Claude Code:
(نیاز به نصب Node.js 18+)
تو ترمینال وارد کنید:
npm install -g @anthropic-ai/claude-code
2️⃣
تنظیم API و متغیرها:
تو سایت
Z.AI
ثبت‌نام کنید و کلید API بگیرید. برای سیستم‌عامل‌های مک و لینوکس فقط کافیه اسکریپت زیر رو اجرا کنید تا همه‌چیز خودکار تنظیم بشه:
curl -O "https://cdn.bigmodel.cn/install/claude_code_zai_env.sh" && bash ./claude_code_zai_env.sh
(برای ویندوز باید متغیرهای
ANTHROPIC_AUTH_TOKEN
و
ANTHROPIC_BASE_URL
رو دستی توی سیستم ست کنید).
🔥
ارتقا به مدل ۱ میلیون توکنی (GLM-5.2):
به‌طور پیش‌فرض کلود کد روی مدل
GLM-4.7
تنظیم می‌شه. اما برای استفاده از نسخه
GLM-5.2[1m]
، فایل
~/.claude/settings.json
رو باز کنید و این مقادیر رو به بخش
env
اضافه کنید:
"CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000"
"ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2[1m]"
"ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2[1m]"
⚙️
نکته حرفه‌ای در مورد قدرت استدلال (Effort):
با دستور
/effort
داخل محیط کلود کد می‌تونید قدرت تفکر رو تعیین کنید. اگه این گزینه رو روی
max
یا
ultracode
بذارید، مستقیماً به استدلال سطح Max در مدل GLM-5.2 متصل می‌شه که برای حل باگ‌ها و تسک‌های پیچیده عالیه.
💰
هزینه‌ها چطوره؟
استفاده از مدل GLM-5.2 تو ساعات اوج ترافیک (۱۴:۰۰ تا ۱۸:۰۰ به وقت پکن / ۰۹:۳۰ تا ۱۳:۳۰ به وقت ایران) ضریب ۳ برابر داره، اما تو ساعات غیرپیک (به‌عنوان آفر ویژه تا آخر سپتامبر) فقط با ضریب ۱ محاسبه می‌شه!
🔵
@ArchiveTell
| Bachelor
⚡️
#Ai
#Claude
#GLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_CrsNbKQUz31BleifMG76JMFc0fkUgzBA5dxaq5r4IMNPYC5yPlO-IbZTMFdEyd3W1gGleKO-Q4J5w0VDpBhPR8WOrAT0_a4jhsrS8TrnkHAQ7SBrwWbpcAYQd8ZMRW8I-Ydh_zopPTX4FelwwhCLJfFdIBIMkK0WQRy5rMi3k3_Thu8w1nYzNz7HyCaxIri4sz93memuZstTBG0ascs1-zC7Hs3b6DXv84nkhPRleyJSDV134Otx6LNmbLfYWDup7n_ZAvzjVyc1TVCt3mTZsxh0hILLVkXKCkHotwOIrelrbp28Xc0xS5u6sO89FdMwFQo5XsXgS5Kul6xQbHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎯
پروژه Universal Android Debloater
📝
این ابزار یه رابط کاربری گرافیکی (GUI) کراس‌پلتفرمِ نوشته‌شده با زبان
Rust
هست که با استفاده از ADB به شما اجازه می‌ده گوشی‌های اندرویدی
روت‌نشده
رو دی‌بلوت کنید (برنامه‌های اضافی و پیش‌فرض سیستم رو حذف کنید). نتیجه این کار؟ بهبود چشمگیر حریم خصوصی، امنیت و افزایش عمر باتری دستگاه شما!
──────────────────────────────
این پروژه متن‌باز (Open-Source) در واقع فورکی از نسخه اصلی Universal Android Debloater است که با تمرکز ویژه روی افزایش امنیت، سرعت و بهینه‌سازی مصرف حافظه توسعه داده شده و با حذف اپلیکیشن‌های غیرضروری، سطح حمله (Attack Surface) رو به حداقل می‌رسونه.
✨
ویژگی‌های کلیدی:
🔹
رابط کاربری ساده، روان و کاربرپسند
🔹
دارای یک لیست جامع و کامل از پکیج‌های سیستمی
🔹
قابلیت دی‌بلوت کردن دستگاه (حتی بدون نیاز به کامپیوتر)
🔹
دارای ویکی (Wiki) و مستندات کامل شامل آموزش راه‌اندازی، راهنمای استفاده و نحوه بیلد گرفتن از سورس‌کد
🛠
از نگاه فنی:
این برنامه با استفاده از زبان Rust و کتابخانه گرافیکی Iced ساخته شده تا تجربه‌ای بدون لگ و یکپارچه رو ارائه بده. از نظر حریم خصوصی هم خیالتون راحت باشه؛ هیچ دیتا یا اطلاعات کاربری جمع‌آوری یا ارسال نمی‌شه و تنها ارتباط خارجی برنامه، درخواست‌های (GET) به گیت‌هاب برای دریافت لیست پکیج‌ها و بررسی آپدیت‌هاست.
چه کاربر مبتدی باشید چه یک متخصص فنی، اگه می‌خواید گوشی‌تون رو بهینه‌سازی کنید، این ابزار یکی از بهترین گزینه‌هاست.
💡
حرف آخر:
با این ابزار، کنترل کامل عملکرد و امنیت گوشی اندرویدی‌تون رو دوباره به دست بگیرید!
──────────────────────────────
🔵
@ArchiveTell
| Bachelor
⚡️
#Github</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPsqPcbvCPOT96mkCAiztr606VeKSsX0_FAFWOqQnEVWS50lkJbYESUT_ftqJzr9jBq4iW2lY9OUqKkhKO579FMnrY1PFtJAkbO0rCHnh41NSiHum5c-Asb6gpqn1M01qevG0cCG87pHuFybyJ3ZMoFiHHbo_OU1i8oA5AHykct8WZ2xborzWOpZUox5PxqJ2vYcPVvylXfaRX76g71fWnWNBn3fdPkYqs7F2ht7mdXwVSAeGP7pFz20FkdBi_6m3bP74fp_BwGaGEacBuTfTYgKXbfT4J6I_tMTRtwmXw3srrPLo64nDUq3TmnxjRF5aqkWQ579XDc84SgbjqbF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دانلود کامل ویدیوهای یوتیوب + ویرایش فوری بدون افت کیفیت
🎬
یک توسعه‌دهنده دانلودر شخصی خودش را متن‌باز منتشر کرده؛ ابزاری ساده برای دانلود و ادیت سریع ویدیوها.
✨
قابلیت‌ها:
•
🔹
دانلود ویدیو با کیفیت اصلی
•
✂️
برش، چسباندن و تقسیم ویدیو داخل برنامه
•
💻
اجرای کاملاً محلی روی سیستم
•
🆓
رایگان و متن‌باز
•
🧩
رابط کاربری ساده و کاربرپسند
GitHub
#OpenSource
#YouTube
#Downloader
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚀
آموزش اجرای GPT 5.5 xhigh در Codex روی ترمینال (کاملاً رایگان)
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال
(
به
ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro git curl wget nano tar -y
3⃣
دسترسی به حافظه
termux-setup-storage
4⃣
نصب Ubuntu
proot-distro install ubuntu
5⃣
ورود به Ubuntu
proot-distro login ubuntu
6⃣
آپدیت Ubuntu
apt update && apt upgrade -y
7⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
8⃣
نصب Node.js
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
9⃣
نصب Codex
npm install -g @openai/codex
🔟
تنظیمات Codex
mkdir -p ~/.codex
cat > ~/.codex/config.toml <<'EOF' model = "gpt-5.5" model_provider = "freemodel" preferred_auth_method = "apikey" model_reasoning_effort = "high" disable_response_storage = true
[model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses" env_key = "OPENAI_API_KEY" EOF
🔘
تنظیم API Key
echo 'export OPENAI_API_KEY="کلیدتو اینجا بزار"' >> ~/.bashrc source ~/.bashrc
▶️
اجرای Codex
( با فیلترشکن خوب وارد شوید )
codex
✨
حالا Codex روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4VTB-2s9Vd3RHzcnHV_DJi2UNid7zTtd3rgOn2vuFE4Y6fV9GKAE0YD972I8UGRlkMGz4F2JzkZnWOgHqTQznG_7_y1fEITjORCyBAPWI1HT8MocPmWEMukC08K-6l7sCTkC950TyzThjOW9cPFF3qjLTZU6HPu_p8d8uI_xC3J1pwvy-tYhkDNOZAk7AWy0fjwP5cwPdsBvEBAbCNpggBfPi0GYCPJIiWVCl_YYO_T7PDFRrF20PhwepnQOlMHCOc2_apbPRbeXdwmmMi_V7KUC0sxipLgCIN_RP6wkog5iTuAkPSUni1mJYUUQTzGxXPKrAZ3q2QnXP_0M4NBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💻
ایده داری ولی حوصله نصب ابزار و دردسرهای راه‌اندازی رو نداری؟
🚀
Replit
یه محیط برنامه‌نویسی آنلاین با AI داخلیه که می‌تونی مستقیم از مرورگر پروژه‌هات رو بسازی.
✨
امکانات:
• کدنویسی با کمک AI
🤖
• ساخت سایت، ربات و اپلیکیشن
🌐
• اجرا و هاست پروژه‌ها در همان محیط
⚡
• بدون نیاز به سیستم قوی یا تنظیمات پیچیده
🔧
برای شروع سریع پروژه‌های شخصی، استارتاپی یا AI گزینه جالبیه
👀
🔗
سایت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZToYpCxXPaEuxZA2Rn9eFU4p6Ewv-HbIZ8hv45cnSjhVXuX3Q-8MQS2p-HuL_Zaqn4RT9xoShefelaB4pY-eSN7out2RsmQrf0jwEdYcpSNuEaLuKkSAq9Sm7xsHTNlk2JZm3MtpmLP2hocZgyvMCoBkdu9qXQPgr1ZYuZs6wu1W8SjZldIUph3rsSN0xHVefNWwuEqOgoImDQzivUNMJ-CMTBkcBFa5wb3XLQPynSjYDk8gZ0ZWW3tBlMooNTFA_fJucH--C6MzSs_PYXjWme5RBk08xmVXBWxqb3f-ujvvpahLdPdfhMDS-ThTitscZET_2PaUMCkrOyvgFVwQZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دسترسی رایگان به Claude OPUS 4.8 و GPT 5.5 + دریافت ۷,۲۰۰ اعتبار!
💯
🤩
پلتفرم
Gumloop.com
یک رابط کاربری چت حرفه‌ای با قابلیت اتصال به سرویس‌های مختلفه. جالب اینجاست که این شرکت به‌تازگی ۵۰ میلیون دلار هم سرمایه جذب کرده!
مراحل دقیق دریافت اعتبار:
🔹
از طریق حساب گوگل یا مایکروسافت (OAuth) ثبت‌نام کنید.
🔹
در مراحل ثبت‌نام اولیه، به سوالات پاسخ بدید و هر گزینه‌ای که می‌تونید رو انتخاب کنید.
🔹
وقتی به بخش اتصال سرویس‌ها رسیدید، Apify، Semrush و Reducto رو انتخاب کنید (هیچ‌کدوم نیازی به لاگین ندارن).
🔹
اتصال به Slack رو اسکیپ (Skip) کنید و نادیده بگیرید.
🔹
اگه مراحل رو درست برید، حداقل
۷,۲۰۰ اعتبار
به حسابتون اضافه می‌شه!(که مال من نشد
😂
)
🤖
مدل‌های هوش مصنوعی موجود در پلتفرم:
Opus 4.6 تا 4.8، GPT 5.3 Codex، GPT 5.4، GPT 5.5، Gemini 3 Flash، Gemini 3.1 Pro، Gemini 3.5 Flash، DeepSeek V4 Flash & Pro و Kimi K2.6.
❌
در هیچ‌کدوم از این مراحل نیازی به وارد کردن کارت بانکی (Credit Card) نیست.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 Ultra در Claude Code رو ترمینال ( کاملا رایگان )
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://cc.freemodel.dev",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا Claude Code روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_p9DvoNDJn95rYb-210arJcGDFGl5GsBqz6zcM-GLOcHHY2GOZmnmJKV7Jip6PDW8A4iWTMRh1w5wGSu554L06IwFcvU4QuvJC0Lij_LKt-iBsb9AMj6ubL4sf6soXnc0i2olYKZp1wXZ1hn6OyndSGCNL8TIdjP5Uh-SowfDSTRQjLSSn9b1G7rEhYTN0Jkc7XcSnHmqOgK3DctpH8fJb1sNFNOSwLLfW9_ES24mJNYf9JRO4jjLOK7VDbJrokM9WIAlwACeMs49ggBZcSBa1KyJE-gBAbssIg-8ErYfbr11vXGv5tlW09XFLGzeJq98vjcuaC5K0TybR4ifbf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ دلار اعتبار رایگان OPUS 4.8 و GPT 5.5
🔥
🌐
ثبت نام
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=DM5TS6TeSAoSBpMMKDdS-IYn4nRlUfr3PtR4JBd06ShnR4qZvRuDVJrwHUzxuRltY8f-xvQYTIXWsWrqLlD6BnOxdsqBcFt3d6xIb3xvNGcrKgs-UCtijFGATJnfDYdMyLxngZOldaKHw8Q7lwKY59wkqcrucmOyEIzdLVnvZvBnDBN4SINsxcWVF6cinoCwNbO2X3w-5jktRqNkHerpewBfZWz8mKNnJnwrDA_k5hAl3i35bYVUZk7muHrGoG-bf2G6gkC2J4e19dzg7q82zP-_qPrD1QjGqWpPg0iVVc0TZpZtOPDqoMUD0xudefxSVTK4A1loLh6UMCp94cJZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=DM5TS6TeSAoSBpMMKDdS-IYn4nRlUfr3PtR4JBd06ShnR4qZvRuDVJrwHUzxuRltY8f-xvQYTIXWsWrqLlD6BnOxdsqBcFt3d6xIb3xvNGcrKgs-UCtijFGATJnfDYdMyLxngZOldaKHw8Q7lwKY59wkqcrucmOyEIzdLVnvZvBnDBN4SINsxcWVF6cinoCwNbO2X3w-5jktRqNkHerpewBfZWz8mKNnJnwrDA_k5hAl3i35bYVUZk7muHrGoG-bf2G6gkC2J4e19dzg7q82zP-_qPrD1QjGqWpPg0iVVc0TZpZtOPDqoMUD0xudefxSVTK4A1loLh6UMCp94cJZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
Open Design
یه نسخه اوپن‌سورس از Claude Designه که واقعاً به درد می‌خوره
😮‍💨
باهاش می‌تونی از روی یه پرامپت، سایت، دک، تصویر یا حتی موشن بسازی و بعد همون‌جا توی محیط امن ویرایشش کنی.
✨
چیزای مهمش:
• 150 تا design system آماده
• 260+ پلاگین
• پشتیبانی از Claude، Codex، Gemini، Copilot و بقیه
• خروجی HTML / PDF / PPTX / MP4
• همه‌چی لوکال و بدون قفل شدن به یه سرویس خاص
خلاصه اینکه: یه ابزار جدی برای طراحی با AI، نه فقط یه چت‌بات دیگه
👀
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✨
ویندوزتو سریع‌تر کن با Sparkle
🧹
یه ابزار رایگان و اوپن‌سورس برای بهینه‌سازی ویندوز
• پاک‌سازی و سبک کردن ویندوز (debloat)
• بهینه‌سازی سیستم با یه کلیک
• مدیریت DNS
• نصب برنامه‌ها با Winget / Chocolatey
• حذف فایل‌های اضافی و junk
• بکاپ و ریستور تنظیمات سیستم
🚀
همه‌چی تو یه داشبورد ساده و مدرن
🔗
GitHub
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🧠
AI OS
سیستم عامل هوش مصنوعی لینوکس
👇
یه سیستم‌عامل ساختن که بهش میگی چی کار کنه، خودش واقعاً انجام میده
🤖
🔒
HAL (امنیت):
• کار ساده → خودکار
• کار حساس → تایید می‌خواد
• سیستم → بدون اجازه دست نمی‌زنه
📁
دیتاها لوکال می‌مونه + حتی آفلاین هم کار می‌کنه
خلاصه
👇
دیگه چت‌بات نیست… یه OS هست که کار می‌کنه
🔥
🔗
Github
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚡️
Gemini
داره می‌ره سمت ساخت ویدیو با چهره خودت!
یعنی یه عکس از خودت می‌دی و بعدش می‌تونه ویدیوهایی بسازه که انگار خودت داخلش هستی.
فعلاً این قابلیت دست یه سری تسترهاست، ولی اگه عمومی بشه، تولید ویدیو با AI یه سطح جدید می‌ره
🚀
#AI
#Gemini
#Tech
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EO0MaMWX1DnfuO85972CGObCYYO4O1JSV-ZjtS-M8J6FkIbz7WQ7geU9XX6uJZ9EZj6RgHXlJpZIGMT6EAm2yTNcGjJIbQQ4806r8Y6-Asq1MWMTZ_wfALzi-jjvkE-K2JsvZquex4Ive75316CWclo9YcqcYXuJLI9MW3ggHVlWbEl2_RSQFDS3ol_kBVCRWpbvwdBDWZcixLZP4fL06npehnXFXMeyefwoYrthH4C0y7btx6EJHYeQdcFSbrhtyrGldG8J1lU7XUY44yfqclQc14PDPp6DhbPz85WFFA1urAhoE3VBZtk6ICfcbzIa5Ne0nLPPlHRdnulQrTohgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍎
اجرای macOS روی کامپیوتر معمولی بدون راهنماهای پیچیده و تنظیمات دستی — علاقه‌مندان اسکریپتی ساخته‌اند که نصب سیستم را خودکار می‌کند.
🔹
نسخه‌های macOS از High Sierra تا Sequoia را پشتیبانی می‌کند.
🔹
روی پردازنده‌های Intel و AMD کار می‌کند.
🔹
به‌صورت خودکار ماشین مجازی را ایجاد و تنظیم می‌کند.
🔹
کمک می‌کند محیطی برای Xcode، Logic Pro، Final Cut Pro و نرم‌افزارهای دیگر اپل به سرعت راه‌اندازی شود.
🔹
به‌طور منظم به‌روزرسانی و پشتیبانی می‌شود.
▶️
دستور نصب:
/bin/bash -c "$(curl -fsSL https://install.osx-proxmox.com)"
GitHub
#OpenSource
#macOS
#Proxmox
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌐
DigitalPlat FreeDomain
راهی برای گرفتن دامنه رایگان
این
پروژه به شما اجازه می‌دهد بدون هزینه، برای سایت یا پروژه‌تان دامنه بگیرید و سریع راه‌اندازی کنید.
✨
🔹
دامنه‌های رایگان فعلی:
• .DPDNS.ORG
• .US.KG
• .QZZ.IO
• .XX.KG
• .QD.JE
📊
طبق اعلام پروژه، تا الان بیش از ۵۰۰ هزار دامنه ثبت شده و مدیریت همه‌چیز از طریق داشبورد آنلاین انجام می‌شود.
🔗
ثبت دامنه و راهنما
#Domain
#FreeDomain
#Web
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ایپی 188.114.97.6، تنها ip واقعا تمیز کلودفلرِ ایرانسل دوباره باز شده، بقیه ip ها رو alpn-1.1 (وبسوکت) محدودیت شدید آپلود دارند، در نتیجه پنل های bpb و ... رو اونها قابل استفاده نیست و فقط XHTTP رو سایر ip ها قابل استفاده است.
///
ولی علاوه بر
188.114.97.6
که مستقیم بدون نیاز به چیزی وصل میشه، رو بعضی ip ها مثل
104.17.121.43
نیز فرگمنت باعث میشه که محدودیت آپلود برداشته بشه و اون ip قابل استفاده باشه، تنظیمات زیادی برای فرگمنت کار میکنه به طور مثال در حال حاضر میتونید از:
"ip": "104.17.121.43",
///
"packets": "tlshello",
"length": "1",
"interval": "0"
استفاده کنید.
///
تمام مطالب بالا راجع به ایرانسل (و بعضی نت های دیگر در برخی مناطق) میباشد، و رو بیشتر نت های دیگر محدودیتی وجود ندارد و اکثر ip های کلودفلر به طور مستقیم قابل استفاده اند.</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQJtIkKemOoCINRgZSfEKA5J27jlVKER7OsUTWC_tk2RaX-Uyyux9BFEddfse3UL3WvXe-UatYJjy9X_mtfW1kXivARATGZk5Pymbv2UIp6JbQAg6SZ3nTM9PxsXcvjiKJosmSTDFrcib27TycXxjZ1LfwhQAMvhL1abVPDrTk8UKTPF1dfA453ssvgg3SPszBe6W6UeFlOT-2xRR225fkSkBmtUrwsZ3OoebZOz5Xh2GQ7cbmwOE8PhOQwvefUiBaXRJeNj7p_QyZXAcGtVoxTNb_OjCi8azvcyqbZZ5ZOFa62ZKNyiKxU3xEA2sQiKWCdjIvNLNUZyy41ZAGpnng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡️
برنامه Sandboxie؛ اجرای امن برنامه‌ها در محیط ایزوله ویندوز
اگر می‌خواهید نرم‌افزارهای ناشناس، فایل‌های مشکوک یا مرورگر خود را بدون دسترسی مستقیم به سیستم اصلی اجرا کنید، Sandboxie یکی از قدیمی‌ترین و قدرتمندترین ابزارهای Sandbox برای ویندوز است.
✨
امکانات مهم:
🔹
اجرای برنامه‌ها در محیط کاملاً ایزوله
🔹
جلوگیری از تغییر دائمی فایل‌ها و رجیستری ویندوز
🔹
ساخت تعداد نامحدود Sandbox
🔹
فایروال اختصاصی برای هر Sandbox
🔹
محدودسازی دسترسی به اینترنت، کلیپ‌بورد و فایل‌های سیستم
🔹
محافظت در برابر اسکرین‌شات و نشت اطلاعات
🔹
پشتیبانی از مرور امن وب و تست فایل‌های ناشناس
🔹
متن‌باز و رایگان
برنامه Sandboxie از سال ۲۰۰۴ توسعه داده می‌شود و امروزه به‌عنوان یکی از محبوب‌ترین ابزارهای امنیتی ویندوز برای تحلیل فایل‌ها، تست نرم‌افزارها و افزایش حریم خصوصی شناخته می‌شود.
🔗
Github
#Windows
#CyberSecurity
#Sandboxie
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxDGHX2cWGvKhA6XuBfgTygICVPLAhq5RUHE6mS9tfxkUNpkt3kumhWuFDukfffvORhPnlHmjlYqg4i3-Zw8ubXN5BrZ_LQoee9Hi71DfWyyUReAYoIjf41BUhHh7YTYusseQuOd8XnNkLKpyvGCzyMQdgWXewbiDxN4AhuVlBU_gpm0zFz-mwwxtF9v308ihwUIYFJHgzHRd4slM-lgSljBqtGNRNMXr2EPccp_KD1FNMrHZKzIA8eVm43QbxBlWveFzWWs7ktGvFAMsLx9Y6caxceNg4NMPGQw-If8ZBaE7YgZt_EPFvpkIBBuhU224HDQ3PkmaWDeox0vJfP2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏬
دانلود ویدیو، موسیقی و پلی‌لیست‌ها بدون تبلیغات، اشتراک‌ها و مبدل‌های آنلاین مشکوک
یک رابط کاربری مناسب برای ابزار افسانه‌ای yt-dlp پیدا کردیم
🔥
قابلیت‌ها:
🔹
دانلود ویدیو از بیش از ۱۰۰۰ پلتفرم محبوب.
🔹
پشتیبانی از کیفیت تا 8K و صدای بدون افت کیفیت.
🔹
قابلیت دانلود کل پلی‌لیست‌ها، کانال‌ها و زیرنویس‌ها.
🔹
امکان قرار دادن ده‌ها فایل در صف دانلود.
🔹
به‌صورت خودکار مرتب‌سازی و تغییر نام دانلودها بر اساس قالب‌ها.
🔹
اجرای محلی روی کامپیوتر شما.
🔹
پشتیبانی از ویندوز، لینوکس و مک‌اواس.
GitHub
#OpenSource
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSp0iyPtYVLaFdZ13MlvpJjodDzAUoRtPSZJbX4pxjZMlmazITtPtnz0BVCR8JUwBOqztoj01yAuQ6LPs4_Cs2kSEHQGPVdf1XQJ0RwbinTjNzD3ckzFepka5hZim6RU87xMZ-lWUYBPF6xjzQwQjxAPU4pzF6OwGWmpKq5lvrwqMysu31LQ0X3bVGAKW6qNoSiV2Ms9qow1yt3sHWPCT_UuBTzSklXxRc2MJwSf98F61z7DoxkCL3hdrepFoRK_PP9jTIvvZh1qArr7kBioGySN1sQEXGLGEcTapJ3V4NUAnXw0JBtDecyuQz_UhdJmotadXjY9W-vGkvmScGw-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTo-tfbwsfdKA5A0HysoLmLFHAaj1nCiQo3eXQzpG41DU8-BDOYn9KlXdGlctdeOm1a-gnJeJy9bhTEkCiSz0GUZITJBAQ0XjL8qpgvRjZYYtQhMHx1GOdZa9ZzK-ATqwCKT4lvvFUtKpzgbw1pkD0-oCjxvu6NO9VBmQOo9IpxuK_likOu53VMhGK3W3T9N60RUyjTBCExkrHJ0F5y9t8q1m8RMl5CY6fsfyuowh1wF0bw_Dtcl-GxbKSmuU_WTbH4xvWTFK7dW4MzoZM-TTwyLWQl5qJM7znOARKD1W0jmn6ep4OniLe6mqhuzOrcfVPrF0CwxVCAgOVi7t-Idaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل Cursor در حال توسعه یک مدل جدید با 1.5 تریلیون پارامتر است!
⚡️
نکات مهم:
🔹
از صفر آموزش داده شده و نسخه ارتقایافته مدل‌های قبلی نیست.
🔹
گفته می‌شود برای آموزش آن از حدود 100 هزار کارت گرافیک H100 استفاده شده.
🔹
علاوه بر کدنویسی، از Agentهای هوش مصنوعی برای مستندسازی و مدیریت تسک‌ها پشتیبانی می‌کند.
📅
طبق گزارش‌ها، این مدل طی چند هفته آینده معرفی خواهد شد.
#Cursor
#AI
#Coding
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBXMFUhftJpHNgN3nM19yhLBsjfi6F5qF9IOUvNcrzr9alT9s7RtLNAnAnQyaggfZHun8cs4xdMg0htFNJENRqeywHTyMOef3EcxQyJfYQx0OvvWuQf6odd657KIiPYtZD5KWt_dkxYNsklmAoYI36xBouF5ooCD0W3svVInJFqE_H7tRKoV-qkAG2muc_QtXqViH76rqxA05wPUuGd3h2fiMR0lfeYXmnDUOr64GPoHDduKRJS5kmLMuHD-mQ5IX-e7Imvs1FZhb0LPdR6XofApD0RzJU-LT7tnrv8eGkgIssye7KXfaUxtgshOmaREHVS4rrth1WWP0oKsg-gi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeCLI2--KNudestVybSyUjmD6Yz1zt3w2__VVgokrBwqHrPu3WM6TxVmeqa_92aj-N2k_T-9mzYZ94rbXprQ1KCadnhvF5atoATS0byhJBLYCxMHz7aJ4vludDp73k3Q7QcZd4ybGIdubj_HrjjqrJiYOb0M7HQHAboM_sz3cNS8tStl4vw13NiPPe76W2hPEkwzPy7Q9DBisXi8G-T3-_7wf0qxzkQFWIlV2DfGlFruzCF-x50oPs72Q4znD-tPTRxMPNHIGPggVahoijFPgY0ka0uDpB-9So7bQtl8lV-hMSDTv8YadMFM4YS-9SRpWkKcRzpHASE6RrAEwOk92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQsMog9Ib55JwmcNpQSAj-8qvV70FeP0BNxuya6D13L_W7awzgT55UCuSGlzJy7UBqQTruvsVjHkO0ubA8J9Vija9fsaCYKzIOZtOkJ9O-4WAvf_bf584UtC0jao8qIGT363KTuCT1jo5NofPzItS9SonjqS_vTgpYZfTv7HZvFUlaQ4O20KclW2vt0tDSJyO-aDlPLUltePEuAqkQ7T3AscSVlF85duS5gXLf7b8p-krEGUIgV9DtxKqMKbV0WC3iH40vc810OJlnW9LQbvR5-FedwdKbfRlVensT4NGLFasQRUlSoclMxW9swG1MDFqu2iiEeYnCnBWrDH2bZUcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fh6UzHylGYA9RZjYTIPGLYmWRUO3rslN9dwQap0ONN4bY4HYKrCHQeojX3g0da6fzyZ7UspHpXveJdV5xGNkpLnZjCMYJuw1y_kM1k4xzfWC-ImNnvml9AGVUkJJVpBIQjhsOBoclQC8zi7axygGS1ygpTvlWv59zT_lBpKOM3ROfNvEMt3Ekt6gjV30Lsab2SNMhf4DCmXoIwurwlIwRpscRtCHJzK0n3FTiMtDn_P1IQzTCyzcTCbMCS0A8Z8bz2YuI3rkqraNmudUvYR9OgaeNyvud2qPMj046hoPRdrJUsyqKRcSSMMp8hfxUpDnFFSOLhbVgnnMsOWmvWPS9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqeSq64iRZDasjLw5LY6MrCJEe0Uc5XfciGADambhsWPpdQ0xCma2WevgFpwQ3G0txlwIK73OM0PF720rVSMOElgPcPf9WCF0qz3GUMkjPGtNsKQO2m23rwd-v0W8y3jyU4S-9apEkpUD7FC2lcUmDD3pbYr1JojfZB_FbVf7_thIzkrEvCpIZN_aCRf-A4-Q3TXPfVyKWdyRbX71EHDrbPAW2mkomGOdmjeXG4NhCo0hWmKiZ_bo6DiVHlUKaEI8fM83jhbl_WhRObjGAKZE_ZoUhwwnBbhjqJMEGOcEPs8l9PRn3SysegqVCCm7r9IJ1ONXcm4RCSuHBvf3eU59Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رقیب رایگان Suno پیدا شد
🔥
StableDAW
یک استودیوی هوش مصنوعی برای ساخت موسیقی روی کامپیوتر شماست
✨
قابلیت‌ها:
•
🔹
تولید موسیقی بدون نیاز به اشتراک
•
⚡
ساخت ترک با پرامپت متنی یا ملودی خوانده‌شده
•
🛠️
ویرایش دستی ترک‌ها با رابطی شبیه FL Studio
•
🎹
پشتیبانی از MIDI، سازها و استخراج نت‌ها
•
💻
اجرای محلی روی کامپیوتر با سرعت بالا
🔗
لینک
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">sadra.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">همین الان ساختم
نامحدوده
تست بکنید به احتمال زیاد وصل باشه برای بعضی مناطق
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌐
ابزار متن‌باز
CF-IP-Scanner
برای پیدا کردن سریع‌ترین IPهای Cloudflare منتشر شد.
این پروژه با اسکن رنج‌های Cloudflare، بهترین IPها را بر اساس پینگ و پایداری اتصال پیدا می‌کند تا در ابزارهایی مثل
Xray، V2Ray، VLESS و Trojan
استفاده شوند.
⚡️
قابلیت‌ها:
🔹
اسکن خودکار IPهای Cloudflare
🔹
نمایش پینگ و نرخ موفقیت اتصال
🔹
مرتب‌سازی نتایج بر اساس سرعت
🔹
خروجی گرفتن از لیست IPها
🔹
اجرای کامل روی ویندوز بدون نیاز به نصب وابستگی اضافی
📈
اگر با افت سرعت یا ناپایداری اتصال مواجه هستید، این ابزار می‌تواند برای پیدا کردن IPهای بهتر مفید باشد.
🔗
Github
#Cloudflare
#Xray
#V2Ray
#OpenSource
#Network
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚠️
همراه اول بسته نامحدود شبانه که لیمیت سرعت از ۶۰ گیگ به بعد داشت رو حذف کرده
✔️
بسته های حجمی شبانه آورده
🌐
100GB
💳
49,000T
🌐
200GB
💳
69,000T
🌐
300GB:
💳
99,000T
👍
خوبیش اینه لیمیت سرعت نداره
💵
کد دستوری خرید :
💎
*1000*252#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🤖
ابزاری جالب برای اتصال دستیارهای هوش مصنوعی به شبکه‌های اجتماعی و سایت‌های محتوایی!
با این پروژه می‌توانید به مدل‌هایی مثل
Claude Code، Codex و OpenClaw
اجازه دهید در سایت‌هایی مانند YouTube، Bilibili، Xiaohongshu و LinkedIn جستجو و اطلاعات جمع‌آوری کنند.
✨
کاربردها:
🔹
بررسی نظرات کاربران درباره محصولات
🔹
جستجوی فرصت‌های شغلی در LinkedIn
🔹
جمع‌آوری و تحلیل محتوای شبکه‌های اجتماعی
🔹
تحقیق و بررسی بازار با کمک AI
⚡️
گزینه‌ای کاربردی برای توسعه‌دهندگان، پژوهشگران و کاربران حرفه‌ای هوش مصنوعی.
🔗
Github
#AI
#ClaudeCode
#Codex
#LinkedIn
#YouTube
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG8aL5rUQRUHvluM-24mCh2YY1B_REzQMdMXuWLKYVNdzbRn-tVZvpRamAOp5QQ9agvuXJNDIaoR5cb_q_39kez8cDMImWlrhxGKyRcjc2A033ScyfuJWWzKmN7oYZTbNJOJiYfkI8gz8cop49kFy_170BMZgAU6UO4kmPTX1wrUF71pwadUbIyUsK62JM2XsJhkmnqwDytVJGbZfjUj5f0kRy-Kn2Q14dn-_t9g8gnPFS9QMGt5S9DyWX3vET5Sf2J4l5sdT8qkbKs9ODqLFqBSAIBJjkZ7MN4y3ip21meO4xLVi5pk78ZJ2P-FVaYEdZuE0vGs2CATLeZNZ03Jfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnrYmAXSNJJ-d-Z-UtoryI-dqPCds88vom9GwZrIDyFd4BUv-BQvs6trD0d6Zt6DLaT0YYlDtwepMolL-ChHvaSTs5bqhp34YF3nfqN20TCH3gO5NkPlICOs1M0EPuTtRP1zIyXAcwjHD_Qcm-C_UJe0olBk_IME75T9itIwFTrXBX641v32W9f_nAqpY2OksvVMiWf1yffaJn2uaGWA-iUUMH3Yugpds60zqfp3uzbc-g4hhwkxfAPRPS53WOEMVVyDPMtwKq1kHKawgiWXl2qgpuoeZ5ucqyEgzeeKjmcTY8F-aXnDzfHwjxLH2vrfSsDPPIj8AzzGpvL27kTisg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtNXJczL7cGSmEJ_UYyVAbHomWQmXzHD5EMwSonXuIiFNSg-MIo89j2QXRT02jzti_5lKFVpFjScBx4dBiSjC96yHaRLX3OSBBuN5vvW33DZ2w0-AU2fs9XOkb8mbRKh9oZvCulC1puOo0Yh_rCl1xqOr3k6HjpjhGI6NvXS0qQwsCBMsJWfrjESaryRPfgODus0Dw7fvEVEfBVOO6qpkOsN3qQ99Mj85NQdCkaEgI-ee6KtMLL1Q6yk8ZvZKwwrbRtyN8iNQzJR2pxrUohFmF43eTkywegJPDtQyT9mRnJRrvlSOdckWn48hdqGLzILhDheLoOWFy-4_4DTJjxRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rztl1mC_3lCtW1mnRLBB5Le8Iw9d25W65Z1X7QOtuIF6zLwSLukASnECvIzzC5lgnV5uileGnwECRcsrrAKdo2a6rLOOLTRNr4GpjOQWID0dBcZyV1oI0yWfyGHSyd2dJ65W1WNyLVcJ4oVw5TUAUh_DeHfq0B6qACHZJHyOXuv_cLBZb3Deq0OC5HrKz347LhqCTvWkl26tJ4Z7QcqT0-x-rpWkz_7Rt0YNnAxGMcLu5L6noPH0uTMgSZVt7TdmGV4on9zqOqrGHnLUFz2QTNgURWpw3TCGcBKvmSt7tY7u7oqdCLWLbgql-iPgIXKTnlLIa-WcGrnR96Zp-1zFuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=HHZruUmmPixMVOWI1bVpjGHos-ryL-0MmHOTsYuvOCCFAo-MaKlZFVlxGZ43KF5M_FDRcxbs3mL9ofezlgfzMcyIMp45Bsz0idPuIJy4KAxO1-6MZwXuYXFI9jhWH2HCeIbJYwOTJmBgt5Fw5YdITzqkAK704XNfsmqz2zon1Orh0t5OFoVODFaHq_EVxclnIWBPc209WDSaosoiJgVhKrK858TsZd4pttd2-XozlkfBafQ6Z6QPLmmQZPLhQTOzQHa8GFi1VGayOxutle1w2SoWtvexdMRGC-LIrgLmBf91J3oXK_l93UEgdqzRhWkJkv9EMVy6v-tIDidVVdyBAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=HHZruUmmPixMVOWI1bVpjGHos-ryL-0MmHOTsYuvOCCFAo-MaKlZFVlxGZ43KF5M_FDRcxbs3mL9ofezlgfzMcyIMp45Bsz0idPuIJy4KAxO1-6MZwXuYXFI9jhWH2HCeIbJYwOTJmBgt5Fw5YdITzqkAK704XNfsmqz2zon1Orh0t5OFoVODFaHq_EVxclnIWBPc209WDSaosoiJgVhKrK858TsZd4pttd2-XozlkfBafQ6Z6QPLmmQZPLhQTOzQHa8GFi1VGayOxutle1w2SoWtvexdMRGC-LIrgLmBf91J3oXK_l93UEgdqzRhWkJkv9EMVy6v-tIDidVVdyBAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
Fable 5
اکنون به صورت رایگان روی کامپیوتر شما در دسترس است.
توسعه‌دهندگان نسخه ویژه Gemma 4 Composer 2.5 را منتشر کردند که با داده‌های استدلال دقیق آموزش دیده است.
🔹
تمرکز اصلی بر کدنویسی، تحلیل و درخواست‌های پیچیده است.
🔹
کاملاً به صورت محلی و بدون نیاز به اشتراک یا API کار می‌کند.
🔹
در قالب GGUF برای Ollama، LM Studio، llama.cpp و سایر ابزارهای محبوب در دسترس است.
دانلود این شاهکار
#Fable
#Ai
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🛢
نفت خام:
81.5$
|
دلار: 159,050 تومان
🕰
بروزرسانی - 26 خرداد 1405 - 03:04
🪙
قیمت لحظه ای رمز ارزهای پرمخاطب:
🟢
BTC:
$66,152.52
(+1.00%)
🟢
ETH:
$1,786.95
(+3.76%)
🟢
BNB:
$615.87
(+0.07%)
🟢
XRP:
$1.24
(+4.98%)
🟢
SOL:
$73.79
(+4.37%)
🔴
TRX:
$0.32
(-0.41%)
🔴
DOGE:
$0.09
(-0.86%)
🔴
ADA:
$0.18
(-0.05%)
🟢
PAXG (Gold):
$4,304.90
(+0.65%)
🚮
قیمت ارزهای تلگرامی:
🔴
TON:
$1.71
(-2.06%)
🔴
NOT:
$0.000448
(-7.03%)
🔴
DOGS:
$0.000044
(-1.64%)
🔴
HMSTR:
$0.000158
(-6.08%)
🟢
EVAA:
$1.258452
(+88.39%)
🟢
X:
$0.000012
(+3.86%)
🟢
MAJOR:
$0.035791
(+2.66%)
🔴
PX:
$0.017240
(-0.23%)
🔴
STON:
$0.578778
(-0.88%)
🟢
REDO:
$0.077989
(+10.89%)
🔴
UTYA:
$0.019192
(-7.00%)
🔴
DUST:
$0.000175
(-2.63%)
🟢
TONNEL:
$0.627903
(+4.80%)
🟢
FISH:
$0.005469
(+1.74%)
🟡
قیمت طلا و نقره:
🌍
انس طلا (دلار):
4,335.20$
🌍
انس نقره (دلار):
70.01$
💰
طلا ۱۸ عیار (هر گرم):
16,296,900
تومان
💰
طلا ۲۴ عیار (هر گرم):
21,729,000
تومان
🥇
سکه گرمی:
25,500,000
تومان
🥇
ربع سکه:
47,620,000
تومان
🥇
نیم سکه:
85,960,000
تومان
🥇
سکه بهار آزادی:
163,625,000
تومان
🥇
سکه امامی:
167,010,000
تومان
🥈
گرم نقره ۹۹۹:
377,140
تومان
🛢
قیمت نفت:
🇺🇸
نفت WTI (تگزاس):
81.5$
(+1%)
🇬🇧
نفت Brent (برنت):
83.7$
(+0%)
#دلار
#طلا
#نفت
🫀
نبض بازار در دستان شماست...
‌</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-text">بچه ها شرمنده یه خبر باید بدم بهتون
من تحقیقاتم از سایت render بر اساس هوش مصنوعی بود الان شخصا سایت و قوانین رو چک کردم
مثل اینکه bandwidth رو ۵ گیگ میده اما پروژه اولی خودم تا ۲۵ گیگ مصرف بعد ساسپند کرد البته این هم بگم من کانفیگ پخش کرده بودم و تقریبا سه روزه داره دست به دست می‌چرخه با کاربر بالا
الان هم کد بهینه تر شده کمتر گیره
خلاصه که شرمنده بازم درباره اطلاعات من احمق برای اطمینان هم از جمنای هم از Claude هم پرسیدم
😑
💔
البته اگر قبلاً ورسل زده باشین میدونین که اون سقف زیاد مهم نیست و اگر شخصی مصرف کنید و ترافیک عجیب رد ندین کم کم برای شما تا ۴۰ گیگ میره بعد ساسپند می‌کنه
ورسل به اون بزرگی با هابیش ۳۰۰ گیگ رد دادم حالا این رندر که چیزی نیس
😂
بگم که ریلوی سقفش همون ۷۰ گیگه
و اینکه اگر ساسپند شدین فوقش با ایمیل فیک ثبت نام کنید و یکی دیگه بسازید بیشتر از ۵ دقیقه کار نداره
بازم عذر میخوام باید شخصا تحقیق میکردم</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs_is3IbqOICjzWo_Nj_fJxba3GJsTCLaxjVRkmrQZYwbLT_oB47NJtAIGf79rB88QrpijFXriPNkauF5K8EK8AEGEGJgpEuBY2i2sCllixLYlsWGKG12tO4LVt88J5dZqP4bFCEr1JJ2L3tAKQSLOrHDxxdN3j9n_6POk6ZK_4f9n2cX9L01LUwhokYXOD9nU0P-hQVKTwIMhY4wxtb5XAIN5h10vpqKm-bROhTWclYxFuIx9Oz9H3p1sNdXW_da3vBQr4fARmuNgFqr3yHtqAB_p0Abc_6dnwLfYGQh86cCujO3AFJUcDk1cUxfLc2beWs9OJtPpPyILDFUQz2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
