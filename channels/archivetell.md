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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 20:55:17</div>
<hr>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 498 · <a href="https://t.me/archivetell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 872 · <a href="https://t.me/archivetell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 994 · <a href="https://t.me/archivetell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/archivetell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nesl6hQt_kjpem4gPdzq4Hh20lKFwDPF88aCMGKdWAnGAo_loJ90t6qi85zBLmMb72vN5Pp_VgSK3Z5TqRQGERCTtIHXuj23Zhmddn0knDBH5w64U2OffnZFS08yxIoHEkZLfubOcZCxsFpUSPSA7IVjZc-yB8zcDUfynCyi7z66Z3XGxbVbw796Db1oxsyHctXMoeMJ-KYgZjwIqY3FKBBuVEYPOt60jssmh9Cm9ZbNrrWhl5jwrXGEOnp-wf4jblUBKLiVac5I2QOSPUV__qnqqyr4f_THotWuozp06AisFai22Z_iZsfYYAWvLVqaUARuMSYGjAu7BJ1sc1CnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMa065v_ord40SXFvpTakpWWQyvkrZVfY14jy7tJ5nI-Mme_gUcIoZZUPvNruLYerYARH7e3f8XBRIuesbqYA8ueQs4t4Jtg_5MEOQA6i7BzfCBiVisBsuRwTyuuOCIquiAdEV4t6FBj6I1NkauqeOxe9G3_XGy9_u2mOMUIJwnEJA6S-eXiBLXR23hXd6cckZNN6ELUuMyoSFVZtBnF6s6eHymKak9kqAvjJWv6Iv054anXbI0Rcza1Y8JW_9xQ1lUbsRSrKExRlHdKsu4O2MNqEQAlocYBaunl3Y_lgLrRkEBH_pqsq2A_AcgboKBNfTx7QhKA-G4uIIeJ-Gm5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cs0Z_spBXVCJYbaMlIfzNDU9KznG7whT2bbZ25cfcHQpkyjup0UF6a_9RbP48ln04HLH3dowIfyqsPhu0bckGYtxBn845EH6l_QAuyNfiwBUcedMyz09mHS6WEGhPfWgaFSPpvT7akPHqzhfRcXWrDATGE7dw7kCuRAf1icrHSMwOi6e9WhG_5Ram3vgFWZx9kLE0bZg-Dn5_bqZcvPvWugBNF1VGaV1YzkaOocE60KgmCZh5h4EpokMjB0RWHmizXCBVQHBf_e3v4aQ_7rgofIxKPCoQjyAA-uYSRzkaLMltJLMW63DLuY_JqflxE19YcrdlJHvzBOQ1nDEVTg-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bglIVj9OzXIVRwXdhKcl9eoSuwekGGSEJK3mW97KxD6qLadItyZbii86qABSPILRqwSi0fCF3QInEE_BPWULxgMZ9BeDw_kMfOmIXajSObuXgCPYnmGN7T9t0zddiAQXaidxG_jIBp3pVljY1vbWBWWFQq0CU4TUK7lK4sTC0VicSXaem1j6KfW3xGYgoD7jwsP6nmTDr0jw63B9VmgwmtTtBiWXHjBe3lhDrcV6yoX5z0pfu6t0iUBdjs8fXgJPbAzZ7PShKfYQ80eUAnJi2vNDGkYDjxOqU7e1qWDxyn2lukpR7UYsD8w4QMm9Vg_NRwpp7QjBmreuJmLo9I3GoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOWe0FcWRpQ2mqKoEsSah6vQ9bjJh6vxy5SonXwDrCKNSN5PePjE7jHqriojggAfzC_locWRIS_u5ypeM8VRj6BSyeVPBcHEO2ScrJIAdoulavNQGDJ9MqnWkTLZdC6Jcd4df2u4EuE12FFOa_xOviz5sVynV40zT1l-vHCKvmiI_wufZ7DIo-ZgVg-IKSCeP_1GcQE8e3EPBJRJFewEbQSTmC8fHUVb49RbnOSNdK12RTkLl2M5B_0BWbEKAznGapfdZL-WVS_C0xl-vvsp_gjxXVB9CtlPv6k92QgWyC2dKCPYyqjHnb9oCgRcap-i4kKFfdfVytyIM-AEXDX6TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tqk1e1fP4PbO6yxq5QAHOLbRUm0w8a3TGONARczBffAiYWqiy6vBm-HBLuNWdHLlHCMULVdpE9dzx2HREN4U8dHVNFuyu0swf7mlMLlO1wGqssqLloSlFtAev-2rvdMyc-E9ulwfUM7_q8u0RELkmwe_I5n3ztrtJsFl4DHzloeMtYgy9iI9Kmaz7AtWGDtXiM_j1PRXuwPXla0D5v_k-7PbBTXkn-MFAxWl3PaUn2kf7rD9QR5ztyK_KScVCYifxGpQEiYrzpkQbFZL0Jm-yEGYRIqqaRy0jjqdyovhiFIoN336FFThBB5IHEhVY1Tdaoe4EpsTh5ouYO5Sgftysw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyFbuYYHCk4Y02zqUd65LOCJWF4nHiSaDjKOh3NuCw0gZp3vlmvP7F8PNeM1L7IM-DffbPHFzQUzd-DLUj9R1M-SDUzYVDtEzou1Hd69yGrFDbkkz9znvDyn08Qpk8lA6Q3HgBRH7EIFVkLFZDN-jOw5P37BaqYAW6e9qd5nPH05v15cI4E_xq-4TZALqGQTUHH7yukwfTha5sU0xN9FKuQKksRkxwk81m-ywtB0f5W2gCGJsDqMWzJbMcSV1tB2w0yu_paAJXRxVxPoqVOnVDgcGH23JUBIaWPjZgMnSVGcACtNQUNNnVLrb_AIpieboNSxQ365Mh-EsZSd0wukJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-lTD3fDePWZ00nvDzWNfWx2fiTNq2bYjve0MtlqdsXiObrQwNCNrMYzrHTeq4a62xJ56_p7ElY6wEHvXPZgexC0ffvwP-Ng86cQwUElGMtoW_Kf-GAS3LzKmP27o0XMwg8IhiG7GmSj7K0ZNxu4Z7Xt7iBRlHyClmY4P-2fSiDuQ6IfZIjE8yWDD5eL1umTD9WQ-YqCei7QtAzT-mQzvev091MaTyBgPqTcSQKpgouHUHxMRMZOYvQVUSdu2zHDtFGxx4PqJp8YAU1WraDB9276fZZVm1kIYhpn04EA1GZ9BzoQ7SabMFZqT8JXb72ouyPmBbIKGZGx5cxZQPBNsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXzlOJXmvSnZbNr8zHsty2Mw5YTHMGamhfcGRIsNPxHtVHGXCAJXM71YH5YhOLNfnSuLLhz8q5k2fHKKsDMNK3C-L7JUu3RR35OfqBlBaDYg_1BJACoDFljJc1z6AJjFzQjdORF8T0vETZCvZ0yggyXc56lmEaTjfLSdouH6lISPsr8AmoQcLCkgiMbP2un5DmKEK_R7cCm_fqN0JZWXhyTf_gxPAntOh1LrxphDCrWCthIcuiPGKDXyYDy0rzkxIPKzjesQMvYs-3wZqpNl_O7NXdRkxrhBZHi3iiW7remqkPcJ8Dq2dqdyMwvZpiJ6fBAuRpwJpbMWQ8q94w0bwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8Mht2dJ_AP8CkDLNXVq8wC2RkxUWvtdDMDU0-5jlOF2uSdUCEcytQN2od-cBaEDtQiLrQ-XL_dD_Y0tcOfgHhGkivGSWpHZd_01aPY6TdiCdNg-kq75KFF0CuQlDyD7u2fajKfoGSo0HhMzOXCyhbG-xiagaqXcxQ-JobRpUvY_xqr3L3b92Lq3zloSCGWnuBtCiuLJ1nFiIqVmH1FguGy1XhS79Pwx-4rUqyZ_tYQOmOALbdXUC5103FVjkUPH_MJLAYnZprBlWm6_Ay8LSoqGqxRiru8dcOlijsbuNUkaLSZT3Bqv7Q67bMhBuhTI3FE3Lsd381Re2YbKzswXag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=D-tQno1-iaubkB7mgMrNrxwCcWcmPsFgNEKfWEKfycfJZFAxpUNVzDqzKAXyC1fqfyORMrX-KM2AOh3xBV_qicj3xIUKvIFaVaLiRjTdYFrj4FGZnR17bQNJgYt_0K5Jm_LdUWPBCZAdnAf8JpSEIp4Loskf63Ao45XbVbkH9oa10l9ZliM0cpkm-uOf6j1cOeQC9NPb2Uj0n0f0PW8vgws74NBmt3iBlDzUMsanZZ9ZMPEIdMy_agnJX9QQBGWQ_UBb-uwPnklBHtFRaPaY-dWSgcVH-za3Nhl-5QQGtvU2EWLmPjbPG1Sgnjcb1fbVbUg069z6nZLr6DB8dqirwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=D-tQno1-iaubkB7mgMrNrxwCcWcmPsFgNEKfWEKfycfJZFAxpUNVzDqzKAXyC1fqfyORMrX-KM2AOh3xBV_qicj3xIUKvIFaVaLiRjTdYFrj4FGZnR17bQNJgYt_0K5Jm_LdUWPBCZAdnAf8JpSEIp4Loskf63Ao45XbVbkH9oa10l9ZliM0cpkm-uOf6j1cOeQC9NPb2Uj0n0f0PW8vgws74NBmt3iBlDzUMsanZZ9ZMPEIdMy_agnJX9QQBGWQ_UBb-uwPnklBHtFRaPaY-dWSgcVH-za3Nhl-5QQGtvU2EWLmPjbPG1Sgnjcb1fbVbUg069z6nZLr6DB8dqirwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=fIZCryu_4uUM97Cyd_yLy-6GI7gvYf-FsSOZUfvSjB4-23NUFRJpXCJMKMrTcsMkNMWPxuWQZcl16p7MvfD5F8cMuqToYYlXumvGiPT-lvjrwpgpeBTirsQaQJU_v3mq60ZdnzpnVO5I40ht0YaOxzsQKL0Y-hCDZWt1kySmNVZSyOaPNnAYEwkVODkD99YxgSELpQ2VyNL5-QIbNNemchGiCYlz0HMeCqBQqZwUpT9PgcwcUxsEHrp_K5Azn7djHVLT0y5z-duqncEzk71E0dNIXZ5sovF6u2j2bJYiyxqwKUNRap7vg6vEbxqSklz6l0-SnJuJ2bXQj1vcqmZapQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=fIZCryu_4uUM97Cyd_yLy-6GI7gvYf-FsSOZUfvSjB4-23NUFRJpXCJMKMrTcsMkNMWPxuWQZcl16p7MvfD5F8cMuqToYYlXumvGiPT-lvjrwpgpeBTirsQaQJU_v3mq60ZdnzpnVO5I40ht0YaOxzsQKL0Y-hCDZWt1kySmNVZSyOaPNnAYEwkVODkD99YxgSELpQ2VyNL5-QIbNNemchGiCYlz0HMeCqBQqZwUpT9PgcwcUxsEHrp_K5Azn7djHVLT0y5z-duqncEzk71E0dNIXZ5sovF6u2j2bJYiyxqwKUNRap7vg6vEbxqSklz6l0-SnJuJ2bXQj1vcqmZapQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhA-BOazNTTCwMcmrj62w7gIpO5v8XtNMyGNVJHt1OWm6THzgSvrYe5lQ_3rUVe23hSpoLy3ggB28GX3CuLYsYKCYDCDFNa0cQkunE_lb2LRYd9sf8LUdXNL0Qex-iTas-iuK-_nN0Isq6Y-XL0x7uaSSCfVxcKZkHKQ1BKSQ-FVLDhhRrdi-wISnYTVW9tlOJiuHxu8_AUijVwTdBM3LLzezqLyaTKq8-XXs-hP6nb4YfTDkX6poYilKKQ72lX7cl1udgfrHjqSO2sKfer4A2cHC3yezUhSvuIn5uKlmKwakFtlunm9n4TSE6MT8ZhgkAk_63PvTAKJia0nsHkIlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=Q_dAgZ52O6jdW0R_QCsDbHNq_uSJ9Q8cXpGeis9Cy--az1skyq3RXAK7Sq7HPcsmZeYTQm8G4JPad9n_lwjB1Wx7pQLbbQVKihmy0bXJ9HMLfRUKBaHRwWZfX-Ckc9nHiPvNAuo9EHHIhf402btOR11-XVp2rXS4eOamYIvTKlTIwFbE-LThmPPLcmJerweSwCo_09pgklhOx4rFlt34pkqVUCp6eZS67YZI_fTWnaooNUipiS73K0W1AuhahYOpSMEEVvQKpueq-5uWurOgRdt-ztW5_0VwmgGiRimOcgYmEbKNEfHg0koG8lFaHdsgGNQcY4_M50xWWBqR5ol98w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=Q_dAgZ52O6jdW0R_QCsDbHNq_uSJ9Q8cXpGeis9Cy--az1skyq3RXAK7Sq7HPcsmZeYTQm8G4JPad9n_lwjB1Wx7pQLbbQVKihmy0bXJ9HMLfRUKBaHRwWZfX-Ckc9nHiPvNAuo9EHHIhf402btOR11-XVp2rXS4eOamYIvTKlTIwFbE-LThmPPLcmJerweSwCo_09pgklhOx4rFlt34pkqVUCp6eZS67YZI_fTWnaooNUipiS73K0W1AuhahYOpSMEEVvQKpueq-5uWurOgRdt-ztW5_0VwmgGiRimOcgYmEbKNEfHg0koG8lFaHdsgGNQcY4_M50xWWBqR5ol98w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltf_f6FRJU2PgfgnfN8Z340FzdV0UmVfGS7egyn_dlk35KSEMIIKRaZ2d1RN7QzRia29n-nsgK0isM8BDkyEGC37Xb_t6Pc22wCRCyeHXc_d0BP-Z_08ZQs1zjgp_05i1XdNEBFPA2DnlGZI9e4fheNC0I_eGej773_sKELv-KHhKfpcHT9abMCiwceLp86sbw2i-kGqRi-DI2NiGfLO8flqEG3Xi4tTYQi0L4jG-RzXNbEKdhUAgVSW8dQPyTli_r7XeHOg8S7Srk2iVkbMMoDKyP18SjbWwaCKu5dZ1A1T4RRybt4N8MCuNY1MMdbzwmUxeJ5brB7-T2V38hLbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5KF6__XNbwOJYChCockm6T8E4t-6c8Lb8MYgrp_LTLDbvALqRj0ufVB2STJwnkPCaoIsbVlJUJDP0HH56xr3socEMgw5M565sVwrOqHeFlc_TcdkCxI0IgYPfK7zqluX6--DHqu-Fp5PbowjRsEc6puFwzNxziAcIV1KYsKZhUy0YvGsdljv2XhAwYPgtDfqQvduyCpZLKMXBOMHawdHi6X-2Gm7w27X_AMEerA254E_l18kmCIdNsGG5V5V017AFJL7YaEVt8_gM6P_kMXS9xmJjHx0tMYmeZFlylqhyK6XOtDKqufw3PxEjyULKXRusOfmmg45Wn4TtAemSFvWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPm9iLl3hWahFCH9xp3yvzrIIgXBXtq9adbAWqz-_o9ParCPWBmOZmToXp1uEcN17vqSuUgfa-rf-us88qCi3R7hyhrK_d-txJpO--0-3xUZC52pLgF4203Xu7DFR3CGG30bXKgCDJL4JMMKPG6_h9IuYG3jXsRvLyq5RTnSFoa2jnKK1OG8QVUkx_8fbfBHk1n5n7LX5sjf59afJUsiVJD9fEep5Mir2r8RiE7nsHszOKyq2T7J3raDXQTTkwIHDcIdbXFYse9hOI641-gnuPUMNx5AoQL8E31RgCc4cvxbQiKwlGPW_OSID5Ug8wO7PGPq-O6pIhhp8KmGlGOgyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI2CBTNw7sRoOFqspsXVXuyutJMLnRkGhKXivdn5uB_OqGNbgqZgcIaxUH2hAJUPdr7i8N4AXcNH5T_Fd49PsFH0AIgx_TGLWk8jVWQ3nh6v8N2_SgvRVUgRwz-tzY2FBWfEe8ZGzw9Gk7vShB81cUo8o6PtlEy5FXh_GukTc45RQ4hVfBy9AZQXjmUdKUu8TmtLo2Aibv7kCjGtWDvRurI3Otu-bcVI0YRMQF-WEBxkMiQpB0rZ8FaR8EaQWD8MLFhTI5ZSagFwicoZ8SBS5QoWY4inTk33_0pV26s1ddxCJG0XSdOtOg6OR7Epv389aADEffMumX8fBCnB_QOiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=DLcHDd0lcv5DqS3k5nRHh6nWpPaSfXUgcytfhPCrrwr31Wnkz8grnwRl7kG4EC1M0P8yHBwz7Fs8-q9BokDTcO4i1J0OgjUaPKIAiuliuE-Owg6kC0zR-1ZdvlQF8E1Y0Iy6Pz5AQbS1pvUkBm273LqbY1qo3g1gcaqttjBZ3L_gNAA3HJx6qQhKCY6KH2fnSZBa2lGwrHH9K1cFZLvSTmLWQ5P5Hoo77Zc4f1iwVFuEVryjz0l2gM4IzoibnFfSIRzbuNe4HGFcD_xf7UwYWuzGGG_AdjSwXfD3uM-Kz_8ZQIkeW5Ud6N7G8w2MUWcMa9vLVDsRJUgblMZdfUAt_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=DLcHDd0lcv5DqS3k5nRHh6nWpPaSfXUgcytfhPCrrwr31Wnkz8grnwRl7kG4EC1M0P8yHBwz7Fs8-q9BokDTcO4i1J0OgjUaPKIAiuliuE-Owg6kC0zR-1ZdvlQF8E1Y0Iy6Pz5AQbS1pvUkBm273LqbY1qo3g1gcaqttjBZ3L_gNAA3HJx6qQhKCY6KH2fnSZBa2lGwrHH9K1cFZLvSTmLWQ5P5Hoo77Zc4f1iwVFuEVryjz0l2gM4IzoibnFfSIRzbuNe4HGFcD_xf7UwYWuzGGG_AdjSwXfD3uM-Kz_8ZQIkeW5Ud6N7G8w2MUWcMa9vLVDsRJUgblMZdfUAt_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPz-zk6K0jbl6Dbgl3HGS-pYeIv7o4Yvi3HeVivIx6eBZgYVNrz8D0DzTuJAeRUhECMRxEMcoh_zaNGM13Ivt75r_a1amx4W4YqSwEo0dR8UFIXDPXlIBih43sIKSeRxXEsX6bh1KzJ9h4x4yy0eTOGo3C0sbfz7vofhfheLEBtCiOrIl8sM33EBIUrrrspjGmt_7a33a0o-RewYmDcvmuKJRZAwuEukw5ikkwCthh4V7XMWEu8pfuvkQ5D56awIv3Bz78frmgnD9u4Hd-4dWVGW6weA0HTqSiG-7d1bPWB2HnxbAvg-xTo624gWVmMV8vjSaQFsPEVzUKFEbZJLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4nKVV67RMCvQioiRTasRROXp7pUPvWmz69POM9vEqGUUe65712bKU_suNPGJbVUP9fv3bfKje4-2iMUJoWnpHK1a3xG-c_8h1Vu8fmm5GwciAcr56J-6km3Wwmzk8GqYzioxsUcQNwpUpo34-O0B10oTttzx0yqGVF7V1nY8xtRuhqhObSg_0zbwKxIL4k9I9YksC33yLKSVsQM4St4tbHlZQuxVxUWmB_O-fr_MUNwMITiP6zpUZGqntCDoZienvng6TpjQLhx7p6ly-GvFGByYwuNnq9UwU-fRGFOt63qwDatC5m91Os4pDEwrQGIZvLr0ep7eIhu_3Yc32SWHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOOg3kaiE0qv89VMWKxizeF3lppwkmPio_AM4VrWopHSFABWTBFWNBMFzNBcfcgZFVB_ReEWZoi1nnL30C6C1GErXKNiFrkVv1qX2FZhqaJJFsw-d9krsxtAbY7jxcT3cEQ1C8uWXx8XeKPzBbhuuXCJu3BRH71Ck0-pUs08Km33iNEtxnApwhCuXMpAHyiuNvDVBJ_2_ZxoSyOUF_xvcVBiR4If_DYo7uSk2nb5PibOfNKaRm9aSw2OY1diLLYhv9HIck9Qc8zZ6OWbc6UooAgiwD3YYkb9bNBxdQ5KZxYxS0Y83s3dgyKxCGavNyTTC8-t6-W2SELVGAGYUnnDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNiryNV-5zJT921DlAMXXxrYuL_PRNUlDRpVn3ptBHooD0ePZynx32zC2OWWd-ieFy2A3ShoarNrtkJ-HVwG1Enx6-YBCk3-jF-UO-w9SeMl0NG0eZ6Reacz6q9frTXIWPqN_F_F7QK-46keLvCDZp5PEx999p7yv2DRO_pJ2Xql2v3m9DQrmbZGhvgxYZQXZva3D1im5c3t9K6yoBLO717Uz_CD_eBneF0dzPl5ZEpA9wbX9a06T1xy30-mzsbPxDG8_omPKrS9UI6NTikntfAtv1e8JP8PQHGAzoY0l46MRU4jS6cA7_zfooB8SURgz0wpipY8nJkMCZZeuuwdBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur6uGh0iLZ0goJIuA1BlgNfekPOlHA6ObvxxNNnVo514JUmJ8VOAc2rTisSXRd1XC_dkWSOabbMLc8oGLVzQtmBJsAhox9YEusEa95-0Z35fXNk-nCdQH7cXPyqnKddsBEzpUzHaFqhrQflQOEobEdiBgTZhzirXMEMOTKMIPjDQVKqCsRI6fN_HIekb8LR9JEd1WLznRZaoqAGwi0zBGtzZujJDGRZ_q6F7uVAqFnbFitPcVSosyNbb6Qyc2So40xsQTN6w3iaPeTBGTM1oQieaIcuv24TuvupSXm65Btn_Hud67rW4rptO3leJD-0g8tnJoSgSbolqPy4uOVdvQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v435ewt19Z3LDXiV26m0pp047zjiRdfb_I-9FxV20BHdl6DxsbN7B89j14XZqftFYjaOu252c-nb1ZIfg_4PJgCmLpgo8ML2asMEJ07YpqvJeLC20YT4cwr84KvWHz2m_Z4mtBtNbWdjqUsEVO8T6bw2rvt_M5PtkhWSpFseepJgfg-BPdxazKPCRWnBTRMC5yaAI5BoOZYjfkPODjFp7jS96QrCHl8W4olCuCMV85IxczDHuSS76YwPuPKqEN26XOK-16oqSDbgPSz3ZA0S_DtcUL87Mn_Sj80ad9QZK_2Xkoya1zx-9Z7iVGEvrbvS_o-i-cSCSsM6DrQ5KPm47Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7a2nppxNNqJJ0jBQ2Akd9NaJz9S8pCn4ZDvCT542ZQDC51QwCksIoAJiv12ZstrgaLGANnziHP1g-IinYWZpAMsnLe1DQaa2fSQXBEBXQegRFlOPnO1ZxDkAVaXWL5pmTpNdiwX0mdfg-7lA_sEr4iiFBnODPngDnkxFnZYGk8tghriKgxo6IThXc_kgKYOnkbpmqJPa4roroAPyPFa-OkMuKXkbcCAxRR2U8cI3RrC-i7TtCRxQKMa9CWB-MK5Xag92oF5fnCHZxJ4ZUHlgYa7tUwKsTDHx6NfZP8EhQeL8u3fYmfCqXxZV2CcxxsQuD13jucc6sWaenKOKrIxzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=L76b0_CWNrGy3UHbzmDFEh0N0o4wUYx8qXiKE2iqbr5kyXunT8PySXo84sKV18_9DzM74z9P2NCjaTk8e6SfOA2xVX20FRAGFhMjvea6w99EqhaqKIntqv-P4ItjZ19jdmSyrFSFII3ZBp1Ff91U8Fy6z2_tN6L9NQl4V23ZnEhe2J8avfWNdNwlxRrp6Ep40oS1G22Xz6njKoD9YJMoK0HODzNOwHoTH8HJqRLG5gCKSVei9_n4qVrt3yqSw9inZhJRCi-MQirpjGeeIvAtjRXlHB0RX1WCa12iQGNQ_Gk31U4_jVVuMY4BXqSkQs1QU7TkFCwp65noyj-fTr_k8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=L76b0_CWNrGy3UHbzmDFEh0N0o4wUYx8qXiKE2iqbr5kyXunT8PySXo84sKV18_9DzM74z9P2NCjaTk8e6SfOA2xVX20FRAGFhMjvea6w99EqhaqKIntqv-P4ItjZ19jdmSyrFSFII3ZBp1Ff91U8Fy6z2_tN6L9NQl4V23ZnEhe2J8avfWNdNwlxRrp6Ep40oS1G22Xz6njKoD9YJMoK0HODzNOwHoTH8HJqRLG5gCKSVei9_n4qVrt3yqSw9inZhJRCi-MQirpjGeeIvAtjRXlHB0RX1WCa12iQGNQ_Gk31U4_jVVuMY4BXqSkQs1QU7TkFCwp65noyj-fTr_k8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVWOKSJMh4zdRFRLwCzdWNZnJAZcTYu8H0n-KVLMJJ8XJRG2UhA6mslao87U-OqAg7zXx_0SLcLqMUeWIbUn5XtogOJiQtE5xCoK_hZ-g1NYS7UjjhyNyOWXTieYQq71ddP9m9YqDPDxW-uCisyn2kFxGuRZh7GvCaYJ77ombiJancOAjqIwXCbfVb3k9nHlAVqqndG89DATRmLnAHp5I328MQ4VJR9cMLIPmnEOCAFaG5tVKeo-HadxMJTy2qA1xsPKNRXZX4bf_8rOWFLYaZSXcej-LfL691AwyQo4-EnNzKj5ZCiG93AI6KbZsETa3Jo4SX-lujDTgJYAaQeqtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGvItzIsL9nqgXQ__aaDjICJizpaJCVpOq8iSMioxm0ShmiIiq2amyPtj01iH__qqWKWNO-69_9ifOLAt0I9j_gmlgRGJ98EjnTXQjRBiwxFFO1U-Y7RDSyj-ZAbBwOLEWeE3P8JdCcSzocY7nkAPFdmQ2e8K1TxtGChE_jv-aTpHgJcV1bH1j4sKBYQJWu9LNukfopZ47L8lROh96wt3pXx2RoaR-lfQuSi3ffTlcbEmQ7CHM-PvKI3tjrPto_qpcsw0V8XDTi1ikBJq4Lzt_cyrAqJFwI4KMOUk93R-pRGBVYPK2WmCUCbAgefnAadL3JUdKwrN2DX_EjCmdlKPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsX8_7BNWZK2dTaOJvfxkwcxM80AcuG9Un7Axn_GF3EH1910LhG6qZVst8zOKVEORo-F2DXZf3xdjRuUP_lBdhv4LcfvSTsN7LI18a-lBwpEvoTjdTYs2hRk8hyTQTlFQGIW1wM_uveXilk_3M0hvgbKESzb6DQ3z7LB8JJpMerbdWbE9dvjpnjApveUFmmZZHU96Do6loJA_8ltKu9i76P00SxqxBYzAALiR2rq5B1kgCG791rB1n6NueHavJwaPCHHgdmOrLLnqzKv-uMpU2INn1IGZkxmTwFJazdoI3ObfkAyjZOva9UDkxa8BPkah4OZbpfPB4CDANRZ8pj5Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiCL1LTq9OeOnuZQ9x95E3sXxKU3zWYSJPtFeuHL2HbPoPY9oZF-cr_2czLXHVzGYqPY3DRgM-gJCq_P9laUcFUr-m2w5HmJYDryTjpLuJwVYKRL4iVQYnaI1RH0MR7M6q2qrceE2I42D-MPNsKNv_oz23ORbm0vLaR_0OW21p25_jrMChyULldTqxpdJOeaKNgTbdP7twtqdMcKJs_QInGFI-51_gjcqMZ-uSAUWmqRw6UFVav9L27qwDp5-KQxd4J1OTbUNo2OWiSHtULL74TQGZmR2QN2Huv4cZYNgdQ0eHK-lSP9ub3DrULSIZkA6bB1JDlKA4MmTwOM2OfFDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTwM0gjv75iuX497MbkrKl-9pWyFCOtDTvMiQvH-061KW8TvSfXj2OCA19SGU76VMO1CrjN0xjxPCNxuXd-FuO-zufxNxRT4WPRL2_MQ-MIHWveAlCO18jv31IWGSJs0N1E32RcGjo_MlL8fuKzK9OV4ulhUpJ0ouBk_kSD9Ny0IlR04a2fJwOjhYwjrk8zB2xaTR-Gab6CDkldoniIuHhqusfuYoYXC_VKrYcN7R0-oFrCQFq1lRaFVPz-oSoms9VlWDmFWpO7ZGdXGM_j0ka9UTlvP6DN1QVN_zmgCCbRICdIGZsghY9uetBiNiPuSrMgwIBJPrDYOzbOInrsS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5YsttX6im6wS5ymDWzjgYu6e-7RSiKy5XMJD5FnK35w7OgYvZrtUjU23bp40k0B1dtMiEoIfZ7WhadJhGvDe1F7qAiHVfbziwRpYB7Kib6xMv_wIjJpv2jdeHEpQCgd-MQHNsMg1ac-H5ttoryM_z1D58MPzt8lNPV3PhFAIL9X_kz8F6b2z2mmQ8n81Kdkpk69x5Z98CGYEB08JtWidbupAkA8g4Fz2Jt_MvDBxvadBX-PwQ5cdW6O0S8PC2l1DigCwS6cM8B18XgswMluRxGSnl8gGX2L8o4oM0OBtI0FrLuUrPK597ZMoAiD6Rmw2oHbePrJSIlC3GpE_mSl7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7rwlwd50aIP4l93SNKY75FONC6d5ttwR-aL5hKCJuXBNs373B4KIpG0TMrxRgOM244Z0t4HOnr9Ab2gYoHGlvqIUYGX3o83llMjR2QO2jPb8HKpKTS_zYNsTVfXjh5hXHXdGq7uNDOfmSNVsyrHc2vW3QDjAa9qO-sL7qokKAW3pHpK6xLyQt4LAs5rU18sUEVqz4OIycp26k6UnrMYCZtYAO5kxLr_N9XfiDVeIvCQ0XBi4KxF6PlKn5TmdQjQM8Kb5cztHQbF-Ut9wwxmS0eSe_pJTM38caTM-gfAeD7RfN87r3nboOsQ5cMfxGJYq3Dz66rhLlMbkTTGj8uTBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZIcsAkL-a7jop0Hv0L8-asVcRUagXbpXwPjAIfBRJrRo4kNyeaKCNX4BXQAxhLPNutsI9rLT7BK7cvhs1WEQkmfaeH2wuc2gDVQcyQsYHmgz0xEKJAB9LMcfKp9AntKNBsHJ7vCpazY7LvEMAKJoFUyLKOhhCVJP6xUZwgMFgikFa81Izb90_-KeEfeHNTQg8_EnpSW4OkVlfuMe9gjP0BAz2RtC-8alstXgmm3zGLlNNJ4a9XRByrNTZBs0jh2kjoCN8CmgQu5f1v2sB2LuiIjIdorUKCMzeBVf5Jh2DyOsaV9JvhliyGHtIiV7qC_PPxmJlYg34cj7I6tvSqNbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFXgTnQ4QVUIK8o2P8wk5ta8SQ5hr4EPauoGxkN2C9MFu2GB5WhwL9orb5cplhGZVw6XWQSYfphM0Keh_dRaetlmzj78BdQLMbpJnnHaOKMVubC1wBTU8iGyXGgAZncloNxAmOzEXKV3pAwAHVzIIQ9AabBS1cdUE2jYXxuMnq3bkO4sHRAdy0p3qt7tmPFcu-0aOatx5sfuIDjBK29hir8O_dSDw91wfvqwZ-YY4tXVecYt0aQKVj-L_rM-LXBax_y4QqXWTCIU_Uk9nRKAFwivjdVHdJLnjtUYdmDa4e02ylcvI1idJ79gV2kwDuGhigFnV0qPR7xw3GpSPv_Rkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-D3eUX6kTLu1d-AAZ255RHzzJd2Ad2CATIUF9ab2eMvIrFcN7D1MhImeb3DAOIQYAQmpEtOlyKCkAeVPfbxqdvUwJqq3DjjeycIwtpAzdMQdy7EYYawgE-NqyJpsSCT22cliHbRP8jnexkR2g--sO_np81-9LEfg0rHPtShAkM1i1_VYsUcFxao927ATYcevyvaeqyCC94mWvRKKavK-jBCNHS2CRvBvpilwBGk0LzUkbuSgfw1G75gu_JuOeb8DDTLaHZjOxSQvdAy7B9IWnzOzCoO-bdMwt_1FWnEuXR-gENZfPlkQ7kFqvR-e_s8H6OuuH7cNco0YlwYuEXWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zxe7rlt9wYXFPT9nF8NIQoOUJmkBFeggj9Nw2M4TMOUq4DQtu-KTaJezW3X2hs8_086nezXgnVI9vp46wgy3LJzBsM5VQRRlClc0lcWq1HpwX6jwfBB7dWe3UM3qIqbpqWsddvoqY_l2zN-lRPqvMY-43rCpJqJInYoCoGsdEAcFJYeeyohIQPaKXUJsGKuUcnCi2A0aXpgDi1VTpcV9KtvLCsSTne2RU7xd_L-pHhVJ7ERuC59bckEomd26KhjybyfCvjd_z2zlR3_2CgFSS3bQdze7SIBGC_HLn8zjrQPR-r56gD405qgn7v4Vh69AX2m4Jx2LD6mNNp3_r6QjQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfQpuuFsNPqAvMU9oLVB5Q08ehydD59v6tLElbKF4IHgXqLmGz1_c8IX5UYvM1a12Y8NpjqJezn3w-jnMSl1BJI3BB5mRY3bj7Fr_FgMTQh-qFN9Pw0E93d32QqZv4BiMma-gNdyTIfTduHgUdZArwCWYA-4kRQX5vDToRBRhk77qkojKRgrtnSddsPhif_QwT-1p3FGxnpSDoBI8FBD3ucMgVZdOCDEOfLK7ml91i6chpx6yyAEpaXLBQq0F9uuL_RF4uS_RVUbpBVX44kLdIyo0tXooADVMJk-fcAYnn0zwrBf6lTpqfM_KH1VKrxg82bD91kvXVmxDi3_eyaYQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=vV-rF13l5wPLjOU7OTKnrKyDT3kvdXTiIoA7aYJb4XhaMnfD6YwRDOEXbmImzj-5pvSEj6J8cvRYjFDYjQPx_o8f2r6aMeYurLVzoxPECPPZW0R4wfPiB-93l4ct-Q5PMx7eEw-fRidVlvKeaaK5QeIs1QCvRpXoVJmbrbm9LLzz8o-zJ_vlmq7ZM-0flN06YEfOAHau3k38AaDSuFE3gyRP5t3pthd-3zZd1sBMB9m8yHsCZxuIjtnf3eH5ROu55Tq04JhO7KlCmvYPqKB-PtYF06eEA4pFI5DTUsHbneIxrjBy1NvTfMve1d-Zwajhz-A7gyyNAa3l6KjLIpfQhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=vV-rF13l5wPLjOU7OTKnrKyDT3kvdXTiIoA7aYJb4XhaMnfD6YwRDOEXbmImzj-5pvSEj6J8cvRYjFDYjQPx_o8f2r6aMeYurLVzoxPECPPZW0R4wfPiB-93l4ct-Q5PMx7eEw-fRidVlvKeaaK5QeIs1QCvRpXoVJmbrbm9LLzz8o-zJ_vlmq7ZM-0flN06YEfOAHau3k38AaDSuFE3gyRP5t3pthd-3zZd1sBMB9m8yHsCZxuIjtnf3eH5ROu55Tq04JhO7KlCmvYPqKB-PtYF06eEA4pFI5DTUsHbneIxrjBy1NvTfMve1d-Zwajhz-A7gyyNAa3l6KjLIpfQhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfM9cqwqYzvZvTBkUsrN0a187Niso9lNQFZvz13MgIIiHY8Bqnchxc4n5hCYcL1HTN39x27x_MtcNZck4DVHSgFQ9dLMaOyoVibkQ_cMqMoAPgPkZ6wgykpS7vBv20JQXI-DmeNi8zmvxOu30IFwJ0bS5ve1euj4x4QjCCW9VkX16R4d_67w4vC5RPHbkqKKGCaLxFTAy_ZyB0CTocYumby3pzs4bid7fmHmt0o9hM2fqEhvoQnPyGZYcGFHWenO_2HaFaZdVXj2aDQaKHrg9Aq2JcocsJdvj6PxtCr9khfA8Z7YrbY7P9KLEWbfkCc2rR79lwtndgdfsfS9PSw4CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2cNDpp7aVJO3LeKlWnQrCrsTLcblb6dhwZ2zoQYVrfNAJfJt6xRsd87auEyi8fS81aFbv-fI2sptcrVGNURtAI8W98Fg8OeokAtq7_KpeUz9_Djy4znBotbOz8pYynOKzkwpG4HvxR4iJjkMJNbnMNBiQV_piojyRJcfIwU6p7jvJ6_aDFPb0j0eKK1i3TkroAiG_cVmG6ryxeiuCI8fuMoRjMA4sbQBnz0PtuBMlCZbIlSvjdaI5g-JQ7ejANrx4CGCNn5PnJSM6SWPWDNBOwUx4oa7K5h_07S9_S9wOgzkNEQg-pQjEhJ6UErz7JAyMMpkKklcIZMT7gB5xI6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ew5CbDNkMfW3Yeo6MONnhaycX9xJlbfLjbBUkMzYo8mKDkkjAG680W6yYQd4DnL1qPY3R9hCuh7rQ7OoYBSBNIdwm9jpdn-0elaBfWiv40WqE5jAj4bUmTnu3xBmKIrgVoLmi8cV3TsJKPGQmdvRBi26zan2u3Q9kbyGh4PEx9TQUE9IaeMFEfy-1ifsP5KL9PEQfTT4zqkRVOj35aWWrvjBsYmwCnZkYAd1yQwIlevxDOuxT1h-hBpk6S8YPB21QVhftLV-OicnIwjdI0fEVzV7oSB5uVbNvMybwN-GtYBzHp_tOjiOzuRnRppFl8wAB8lWLkYD-2V7vWZT6ksBRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6p4Ev3KPjKphdIErysf_R2n--k0ZhfBKOm41Wq-RQ8SPhU3_sNF2gDpmxwr7hW5VptiF13D1CeVJ2A-aWe6K08sVmK9RY715x2v8tlG7mwEIHxQUgEsR3fpe9SfRgyHquwYSa5LemxYb73JdijfYqVrD_0h7Z8veDkEOCFccRQWrfbPjEdDzZYE0MISLNOQlRzjrAjNnbCMXnFFyeH-mcGNyZuf9n5F--BKpFObjMyDzOtC_cQEk_S0eRRGRk0uowjI3XJngMxs7bl204gciZ0Q2_1ySmsFQCDgHNry7q3bix_uU15-imZipXlLdWLio9lciJtE5vNkouMfr7D2ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzrQeFFTpU6Q8mmzzzBkrwjkMd5PBQI6gqD2hCvaPwSVSM1E2XORsC8GakyazpVT2uAk99xDDQLqFInkHvajxuSfmjXK4gdb5couP2AYXtDgoHyJDoPL8WY6K_IT4_3-jw-mNgIo1js5UNImkKwc8VIFYEhCUjyGXjBwlNW7dv3-yVhOdFnX3npI0RW_YTwfdA1A8jHLshnHkb-RqtvfzSATXDYJ5R_pOgA5JqPSZMk_iaKafNcQudiIVV9iMzgT0wJhg-3EkF11BkgfADOIHTQTwKtnm-qE32hOJ-43ZpKmkgeAbj1w7gQB4ibQeJPewFGe1ofgjtWTIHbosPs0qfp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzrQeFFTpU6Q8mmzzzBkrwjkMd5PBQI6gqD2hCvaPwSVSM1E2XORsC8GakyazpVT2uAk99xDDQLqFInkHvajxuSfmjXK4gdb5couP2AYXtDgoHyJDoPL8WY6K_IT4_3-jw-mNgIo1js5UNImkKwc8VIFYEhCUjyGXjBwlNW7dv3-yVhOdFnX3npI0RW_YTwfdA1A8jHLshnHkb-RqtvfzSATXDYJ5R_pOgA5JqPSZMk_iaKafNcQudiIVV9iMzgT0wJhg-3EkF11BkgfADOIHTQTwKtnm-qE32hOJ-43ZpKmkgeAbj1w7gQB4ibQeJPewFGe1ofgjtWTIHbosPs0qfp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yctw9hMfxeYU6KEX2v1K6UGULDvKl_jbSXocjpKWGdzB5mE8dEys-syGFFP7yMt8Di3U8eQopPS0aHZR2wQtKrB9SS6B4xk9KCdic4kL1OaLlA-6KjWl8XKTnLJ35iUBiBAzrjGroI6sNGE9wjFqnbQbEAsv8acAa8ZMAjbhhdO3NygkbOGMW1yrbDiEMI6zBNZRF4JlX-Qw5VmuCqn6bCqVZLPuM3Nav8DfE634LwGmeHKydHo5cviEmord1cJfX6bvg4Gbvib8s7QU_NkoZoHs6cVUXctBy-p93YG-gXIGG3Hb23I2f2ldHQ36c8hsbj63M7N-BP5bWSYZAOn65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zfgy4NknyrC1kyrymnuG0kamuj0k2n8JDOm_4FIcMkWqI659H8JsOX9eY8hfzGhMusLaQ9iJZruYS23RscFFKC4REZLBwzVpuuJ5z0czFsedjdNrZA8CT-UUWKIHQsAvmxWXaXOMaF3cSDPvl12URDqqs741h1NOQpyXNHkI21SzwsPFU9zCMJZpVk7abFF_xBN1ovaLGk-YftkkbvMOU0JLQRd2xpP9pYKin9Nbtqk4nn1EEYy7o0eCX0qiWpWKwWStSZz9mTA-M-TrHf7NO_OIWhksiH5s4foQu_ruWnL0tq2W9Hf8mtPo2DiJfZDK1cObr6g5k_8wpj8iDe_hqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj3m1ywG3xamxgWRU2xPCuZC8jz68FnGZP-PGhgWqIi-DPZP85flFt8llfsRaeO52O9Hos4OcIRbW2GKsDW2pNi-Q22j-gAkavaIqQPXEgrHWKMCZW6_uu1pRoFNKRn6Yz9mJCgIGVcPS16PWkkHTDFK5GS4V06G2G-9aRAOgvG7zUbAVb6Ra9Sba4m1J6XmxGAHg1NgAyNm8PUMzSGFBPY57Z7aGO2m6TSvoGEE08h6KK-UY_fcF50j-Oe7J2AjNi5o-67Cugj8KZAbC89OjAxBOy7bsMbG3wKdTGJ1AVnzJqh8A-EH4NSIXCzOykLEupyoJH3P0SZKDRhWouslFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikTCClJDobV_nkv1Gusb1W3bollYncx6RNsZQr7WphrIY3VGW9Nn6Yz9qOXAsqNleVtlB2VvHwUVznXMUu3nGtgg4XYzAKoQ2OFf277roA-rJVO61zafah9pLL5heQLWAGyp7nB4RtWZjKmTqAjJrFs7zdLjjBM2bPvDNQ0pzowyDkoIgmuUHnNHJ0OVbtRZ-RQ4KZi9ga_abQoNH9v_VRVu0oBIPI1yBXO5OeyIbsFiibH_Vi1GSb3JKoeVYAs47QnT4q98XtQ98wLbUXubUV3pwrOLunyRoKkI44b8Vu3ZQGqleYMSm0Dm0ox0B8CbPK5W_KZsohsCQH4wwSX0Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ8oWM3rSi_jbSaHgUPJArPz-U_NBFBvcy2792VgbJEl7XBsmhxnod1uENFSINc0TyKVpyVv-eJIVaECZlZYjwMALpD6clSwGfKZTd36a1KO13sXWAeLOWS8SNgbuawaq9qwecRr2psGKtPzyHBy925pN6TO7D59wY15_YAJdnfHFJyVK3n3avPhfxe0kC3HOtTY-VMbl_nMz5aCK8-iDDQQv_5iKLj1N0XiWaF4N73fED-TYy7nDdgUu8XSajmH46I6MXiHI3nLy4cCUZP2mB7tVyfRBA1q3tJNatW_ihvyT2nZhh26dTIgCnXJeDFP3BS38uSxzMWAFISHNgA0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rctK_eq9fpiYH5HC5vXYFAOu-QlxDWEn9ZH_qIzjv0_IvDfq3GAKtmKqYR_nUYej85Pjf_wGYhOY4Fo2lyNvdy280P2gFDzM7WR-RHrC2SbLzDeZZz30Kb7sB4HS_PEMbZHXTqBLS9vpbpZLEByVc-gU2QWqfdTSsKjLDtJx1dTptMs9kLxUdRxeoqljSrxDQWpVckpVA5jCnpNhiZ3aJFLeI-W5HTjMPOCOB8QsT3vjaghGgpnyC8MVaVj_a9xsgxmNanmD6K4RKTSpW9o96LFkCtChwndLzoranejmpg_YFRDORHPIGOaTQpLGkJYsE3MEFPGX-q8gevIvAqZboQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sp7bmhB4ppUPqw9wTkV6lGG7pHXzMRMlXIYHcwQnM0pAWKl1QXii83kdj-qQgz1wvpf6dPCCcePhpYzuBzh7g2BpPqOVv4dq84X-pzR1qkqPavFxB_1RAm8BzQnRR9Brv2N_j6gRxrA3oJX12ezehf6gbZjwEGlBowaoT0cqoK7XH-rD7WG4m-0_OlDECdRkYguf8hXxxs6NTmuzEScbuHBf6WuVEzmRNzMEUelPyszO1_OnsPMX9K0bPjtZ23Z6mZrb6NSirUne8YKRHll82Rn0_IsfuJxV0w3eDJf4J97vSC4L_W9R_GNR-Y5CgG2hYzzDUPrRy7nX3I11WlV_qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=tuKevQEJRiwI0eFtmziwghep5mIgcgt5gxZYZCi0Ogu-eBG_sDEhEERt3g2J68d7P8AJQIoyOXbMWjWVu_x1vEm-AH8fIEzjaQfvJJf8hEkQ3xLvVv2CKqs_AE9AiLKHWciI7r7bBMe2PPLgYqLftkYas-rNpqNVtW1bq-OUc1AOCRaqRfCWhINR3hHVX2Ts-oWGKInoNqUg3S8SYSoZYO2V-yNFk0ZS8Icetj03bsoSs0VybyiA0kqbmKAfHYZV8HeB7NA6Y8UlkIh9rR2CTIFmqX_Ya1Z_BAuKEteUL3vkra0k4ojGe7-bBQcKs40RXiA3G9Ql_qSIwp6JrA1JnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=tuKevQEJRiwI0eFtmziwghep5mIgcgt5gxZYZCi0Ogu-eBG_sDEhEERt3g2J68d7P8AJQIoyOXbMWjWVu_x1vEm-AH8fIEzjaQfvJJf8hEkQ3xLvVv2CKqs_AE9AiLKHWciI7r7bBMe2PPLgYqLftkYas-rNpqNVtW1bq-OUc1AOCRaqRfCWhINR3hHVX2Ts-oWGKInoNqUg3S8SYSoZYO2V-yNFk0ZS8Icetj03bsoSs0VybyiA0kqbmKAfHYZV8HeB7NA6Y8UlkIh9rR2CTIFmqX_Ya1Z_BAuKEteUL3vkra0k4ojGe7-bBQcKs40RXiA3G9Ql_qSIwp6JrA1JnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgS-4vc0lx8JPtV1pFh1lU3eIf7wbuQmyFIIGOF5ZJ6yfN0HaVnW9Ub3Yjp-8NNhDm5Xls6eZM5al0T6EnZ7r1vKpVBCkpMz5Ewcx0EF8soNScj78H0rpOlzwbI_3RgmoTavgSwzS6YjLTA6PxCs1PEYkN6mJTxDXKW2Q8j3Egvui7xBzxiV_iB6WWHplUwrziPlvapphKLbnqSmGB2TO8U9i0FJspRt_FX0YwC5OOo-kVxJFZitKabfIZW0WcpkhgkbnP17eEpJPL0YfDovO6CChl2Rtlmn26GW9k9WTMGmZFz84u_uQq6nY_yb69Waum8Y9uYtnZ0IA8lZR1g7Pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5HWwG07ahjdIUGFNzypWLitIv_oQtC11mKVDkmVa3z8peQ_yXKHnyPZrw1Lc0EsXDNBlOn2_ll_imSXQOWVyL5PT9OEwBDbapSfkremIX0OJGjGekEHIVHYisyuxFGyxGkmOUu3aOAx6-Bhgt4YMgvjoSwrtUk2dAGZc62UcimyyFSfQVXU3mnJFkGhDwwmPh8ZDS7I-v-w4qTbv_5n7c1-7pifim93gkprPLSZic13F9Xl8or5ns-PB6lQfRxHSEkbro0PeokIpfTTj4Rmv4HAeQPdcnDKjNzDZozh6zfhaYbV97F5rFsImNcCu7hgw2iQhh3Qg1KMZR6agkCmYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgbd83-xyo5-amIkOZE61Yiaq2oVQQ9CfP8kNbjsDVyCFVrE7A2uJNF6sHXQ3e6WrgMbePeiig_LOXDgFcySRUxiT__z8FPB4ZiNWbPq59srj0vuJYjuGw0LTpbTfswEjEICroRpBjqOe-5apQQqiy5p8AG2YfSj9_FvQwZukKVuXMHPFttK0VzlpGTalTm23zSbelasxpDUoSSeOYhQBp2WlvzHREw_1ZlOrXD-ynOXphdVUiC2BtdPYYl3wMJuQWzoPc0krMxY8OAlSBpuzRIxX8cwILgZ0Scmzi8RmIa0gKNJ925xCmVLshr9ni8qbgL-KC-L9_oG8EJT7umi9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv7APvFkCEVPsCA7KDAkU6IaOopNepRNaGH48AVYuiI_GzqqZG0te1oaPtL3Q-alPjgYXn-S9jbmPG4Pyg3d0CSEzh1C8K-7IWCRrcqFUKWV5uJSXUvprhCjdkorxVMvN-NWdDW2BdVfkD59KNQma_orOb617f44-l1PWmTgrBRH8yIQR2Hru5mQBNhqQv56VMl2mI0iqlCY1z4DG0NGlKwB-OeZrYIjriIQCXZfthwbNhZYS2VXtpTuKfPQHnnEHsm45SzjFsqGxFMowHSW28w2Rak5SFDlJFIV_9JKTXWGrjssESch8KH2I_oodFw9EHI28yFwqTL4d3wo7zGkzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMZ0_C1bTncQk8RofnDq6EsrdmF40UdBdtsROTMVLBQN7FrDgIXqOuIxfhVBNe-aBZtWVMDhc1D4OKVfK8_L3MVKZUKczdWS2j9oBLvl-M-l9nY_na_1m-hpbxjt5a2m_t8jYgWz0Pe2qytz__r0Fe1pJuqaPvUG_DaS_82naeXtsRJbQ7nesnbtwIPNdtWqxsgHpYjvWp21vS6dw_IfEtzzjppcuT9DmdFTgueGfjcEE-l5mNWqblt4QBd2mtVCJooID8xOgYq6qiNw0tKoybcnXh5Lz_xsJj5aVTBsyfaXpasjd-b3baAQVfvLAVD9Y6xUjV5OjPePHTHdZd8lZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xr-JB_hfjxau4TIdH6UjvJPNpNWP8x1XuDMIiaOuAXiXAk61QF0h5xThmhNAgilRgqUTgiS1uZEkvzGTIbSZGvmVK-AldE7vDxJyd5V0FzIR8_Osp6P75AzrTG8iHKgyGH9sa5VKUuzWEHToNPkiugJfJPWl69QnzFQV7edfdHECvmNxdiB9P5MmSFdXCnR2OABend5LUChbYH7-Qhftgc0spHkXnm1XOZyBGrjeJI_1k0xtKBL4Q-FL8_Y1ALXrssM2TW4uozY_C7SR0kakqkhgza5VpmnJalY9GXPyPUGjy2xydYEh_IYeO3LZIwQ-mQ5ZNqlcCXdDt7QROToKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRoYRrz3lsSfMEKISBcjVJG5yGGM4-rbLtreKBP-HT6d43ip5q2j3EvX7y0VMOvwWIGKvpi5mtQYZXnc6_0y2J7DcZ9PKGdvmSnaess0jDZz7Od-svMkR_Mq95gN30b1yab5Jk01PAbohD3XDe4n5lSC2XghnI-LpBh3T8D6ukHEasYQb3_lSwh2haBHqplZOQrU_Oa95U68_3tp7wTYzN4uV0rJzlhEDjaEoRUuBDgAdo6qDyX_SS42xQJ8Sq5_YYNgjXrIyeV5J2LGoBq3BDbrtA7knXPLDstUmub70Gb94dLm65X0dyEBBH-VbpSkyabl-lll_u-7JqPwmxV-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lazZXQrzw9oThqlEjEG-k7WqN50TZfyJA-zknbdEF3bcvCv4TRkLLcU7yLR3pPajFIqONh7Gjp87aSoApDWu5lBrJSKt5GMyxChXshkkjeWtffdPWY3_vdZe7JrV5cG3iTO-GNHI9yW3SldP3kP218z8DcEQYkUW4-c7hWINJ_-jaaIFPzh9qzBWRrYnqJ63-uYUjb5eLwCgeE4DBmtFBgoVdPXJA9i6tdODMkSLvc2pSvgnbCYP7urFDsddnPlgwLCqEFt4_4o1fregATY-2RQ-T6ldntYKPkKqrZCAEFdAyZY8MZeb9B28o-3Tr-wPjNhfUNxqExrGWdoBwlCYqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjNwoXxqt0yxYyCbnvpdsYmQI4Yl09WHn8S8dKT8WDkKzHFzdNoBk8yRknx-v4-ZHFus3NgQKYXIeEWMnwA65sKBhq0JoUe7hhLsDYLh66jT51xc9RhcV_o0Y3ViibF_RyHOHfMuEWGTUZuz9CA3ClT1RiylhBWimVJQ8ul8I1b0aRv8D01k0S1vIcvTc4RRetFMYdG2lyX7P4hHDZeoMP9ZlcU-XlpGzF_KMb6Rrmfug-WqZzhkQb9Yp-bXZI2cyb-ExfBXJDBwGFgIxC1MhMkpQFvXRKMvY7WOhdcZ1yZ5-wSS0uqMmr3LV2flL_LZzpw_JUSBXxq93ze8Vrcu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ExZORn922JIC1UddODzQvatc-K8mmN0qDGAmu1XOovfdCmJtXka0uwTdvIZSMjAdmr0TmOncPu5sX9zQWywwyVILqzgAUv_RN7EGBf2cgGA7ebfG61wpZC3iN5a6YxoNfbGDVAnewccRsD__oqlFdlVK_XsqFT-xRqE7P9Jpa-AyBbEwzfXzsnXR0WxbTXaZxQ2Y2GuYQuV8V7vXyYRlsbOZ0MFhCPQ7RclHHIve5wVlK8nSyRpNxrFfpdLgK9wAU-dI-Q2xqc-V5GmB9W-BM52u1wepjAA0HlIcGrIqmhwI7Q1FcbfHzv-LM3-UwoZZBcUpH_sxnS3XnPKhmR0FoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHjq1IrQDO0ZiUFunwMCZV-g7M8hl_ukCn7k9WDhL9NMKsotd8IVXG6SDIMPdDRULf5lBVkZCuVrIgW3--ScTDHbpX-wdImR25S3cBAWaP9EygbTaahYq_DCDLlOfMYkyrQsvgpmMUtN8FSDK8TR_VfkLdokFKTsPIP2qdxGSF_tnUCvTOvnja_e1e-5wI951qyf5A_xzjy733KStdv9b4l-c437bS2AOCoSOqOZ36BBlzdzlbX95k7y1Grw6sDoQHgJtvGWFvMTtXs4OCZVkQ3vyGhhYoVfiN8mK3ijNT9SgCH6W1O0_SFEy2ywnYvLLyUBO0rvia3JrVc3wFNO0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2h94VqI615Tua44CLkAwcwqj9GjT6SXlkpJA6_nWfOANOTQ3R0VtXVuLgaDydF0EhbVe1jz-QzkzKs3zCRdNjDTB0b5-DwQresxjtDGa55E2vDZn0LZ_H3lbOtfnzo7bM1QdiopbcDhvDEKIIZcX_Icox3TaS02hcmZU4oVVs-dyqEK7KbcTm4c_OTOA3nt5yaSVGgq8fc3_kgyhnPkj2MrlYD_X-fzdT35w8opr1rw6tku3PpLAmMwqBN8kO0vqy9inegKJnZnQBrfKBQWVgLuzwwR3EK6CgKcHHsUwMJO00--QadPlw34TNWuMwBqg3Qf6H4UZxx6z8H6kjkTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYIRS7keWRna9JDrjsLKpSaEVxKdXgV274AqU7MPEhKN2NQluwn5G-UeAVKSPd4beCsxAbgZ4yiqk_A6QwM4JeioupLJnmouFlhvAnylK-YgwgLNeaWK-1W9Oh0HBk8bBltdHRFEu3qgI0QkPqfwinSsZ17rn0e501qwDuza2TJ-jlUef9tGph47h-WL-KBE7pKYNfUEcVGOraB0ygSqLDSv_nPtqThgum1nJMATeSvswDplxsoj0hR9Y9eW4HieAmfXHPBXEripbKYmH_TxWHPViqONB9AsjDEmuIPCoOo46Id0_R456ITvb4vJ9gXrWfLrPzf8rbPY6ZOELhxh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4J-MZAKsQyJdgsNl3E47ZGMf1L1nn7E-LQJ-e4NrGE5BzaKW-G77rps8c8pLa-oXu5OxPiT1UE1OBtKp6JeZp20cgJllLHFV7K9y1P94R1zfl1QFSdD-i20MjxfKVgWw8VqhCxH2wSyE66q8DdqusKO_wOgEeYo0KINvqiWai8f5xv9MvFc6y-d130DStKd-GafAZ11GmoWTfQdJH0NuIQ5WqgcmFdgVelA7PcAdzzRcsJoBvSWAA_Gos6AN4D_ukvTLZE6tjjFmVqJDMKlpHlGYCplmJuAZoEiCsciqzoRgPJVqp8ppWCg9erkmg-KPpyla_FrqSJOIXzqjtWpEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=DTR-iNc_73c2J7OGX_sqyIejhuIWSRGEIighPJ8tbskSBYJUrUef1dtdTHAKRt5FTi371JFbKbTDv58LaQoieIU5D1VWw6p4g-AOc9BjixoB_r0fRP3r-S4B6zY4QOOkCAKrr8etlfKiWlkNRCv3S5SIqL3l_a0Z8x_FFNyvyAGnUPLS0ULah0BvKoh9Dw3wDEghdYSiRuZGZts3x610oNEDI9qTznCotnjll2u3eaaNE5V2U7ciVRaxzbzA5h378iguHoqwkkIX6rhx4Pf0B2LF_RoVi3RW5k9R5LjrLwzDuhOvZZzPZ72E_XRGJDEdARSTNfYGeZgGv63eC0cP4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=DTR-iNc_73c2J7OGX_sqyIejhuIWSRGEIighPJ8tbskSBYJUrUef1dtdTHAKRt5FTi371JFbKbTDv58LaQoieIU5D1VWw6p4g-AOc9BjixoB_r0fRP3r-S4B6zY4QOOkCAKrr8etlfKiWlkNRCv3S5SIqL3l_a0Z8x_FFNyvyAGnUPLS0ULah0BvKoh9Dw3wDEghdYSiRuZGZts3x610oNEDI9qTznCotnjll2u3eaaNE5V2U7ciVRaxzbzA5h378iguHoqwkkIX6rhx4Pf0B2LF_RoVi3RW5k9R5LjrLwzDuhOvZZzPZ72E_XRGJDEdARSTNfYGeZgGv63eC0cP4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VieVhdgNfd-NpKM8iofCwAcjHGpOcH8V-RX2JJjfEmjreJBEOzSikf3wG378TD4EgXyKOw5YZ8y825V84VHjXMs1OWf6BH6YwgHJu4BZGS-oJvgBnk_L3j8JwDQ9zEc1ef3r822cz3XU-J_2gNRjFBvFNKsq6ql3-u1YugeZtVj__BNCvc_vVfNMoyWSJXNF1w0xadV-ad2_U6BsvfaWr1QsuA4fq6SNaOOlJGxgkC1JxVAasqtfWlBDW4fO5r9IpNW3cd6ySDZGyCM4OVedheropB4rJM8ALFL9qGC6et71nQvMkxIH9mJUk0ec8KNC9StuUQBsU6fV8bONX0QsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
