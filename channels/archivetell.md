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
<p>@archivetell • 👥 9.59K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 15:47:36</div>
<hr>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nesl6hQt_kjpem4gPdzq4Hh20lKFwDPF88aCMGKdWAnGAo_loJ90t6qi85zBLmMb72vN5Pp_VgSK3Z5TqRQGERCTtIHXuj23Zhmddn0knDBH5w64U2OffnZFS08yxIoHEkZLfubOcZCxsFpUSPSA7IVjZc-yB8zcDUfynCyi7z66Z3XGxbVbw796Db1oxsyHctXMoeMJ-KYgZjwIqY3FKBBuVEYPOt60jssmh9Cm9ZbNrrWhl5jwrXGEOnp-wf4jblUBKLiVac5I2QOSPUV__qnqqyr4f_THotWuozp06AisFai22Z_iZsfYYAWvLVqaUARuMSYGjAu7BJ1sc1CnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMa065v_ord40SXFvpTakpWWQyvkrZVfY14jy7tJ5nI-Mme_gUcIoZZUPvNruLYerYARH7e3f8XBRIuesbqYA8ueQs4t4Jtg_5MEOQA6i7BzfCBiVisBsuRwTyuuOCIquiAdEV4t6FBj6I1NkauqeOxe9G3_XGy9_u2mOMUIJwnEJA6S-eXiBLXR23hXd6cckZNN6ELUuMyoSFVZtBnF6s6eHymKak9kqAvjJWv6Iv054anXbI0Rcza1Y8JW_9xQ1lUbsRSrKExRlHdKsu4O2MNqEQAlocYBaunl3Y_lgLrRkEBH_pqsq2A_AcgboKBNfTx7QhKA-G4uIIeJ-Gm5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cs0Z_spBXVCJYbaMlIfzNDU9KznG7whT2bbZ25cfcHQpkyjup0UF6a_9RbP48ln04HLH3dowIfyqsPhu0bckGYtxBn845EH6l_QAuyNfiwBUcedMyz09mHS6WEGhPfWgaFSPpvT7akPHqzhfRcXWrDATGE7dw7kCuRAf1icrHSMwOi6e9WhG_5Ram3vgFWZx9kLE0bZg-Dn5_bqZcvPvWugBNF1VGaV1YzkaOocE60KgmCZh5h4EpokMjB0RWHmizXCBVQHBf_e3v4aQ_7rgofIxKPCoQjyAA-uYSRzkaLMltJLMW63DLuY_JqflxE19YcrdlJHvzBOQ1nDEVTg-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bglIVj9OzXIVRwXdhKcl9eoSuwekGGSEJK3mW97KxD6qLadItyZbii86qABSPILRqwSi0fCF3QInEE_BPWULxgMZ9BeDw_kMfOmIXajSObuXgCPYnmGN7T9t0zddiAQXaidxG_jIBp3pVljY1vbWBWWFQq0CU4TUK7lK4sTC0VicSXaem1j6KfW3xGYgoD7jwsP6nmTDr0jw63B9VmgwmtTtBiWXHjBe3lhDrcV6yoX5z0pfu6t0iUBdjs8fXgJPbAzZ7PShKfYQ80eUAnJi2vNDGkYDjxOqU7e1qWDxyn2lukpR7UYsD8w4QMm9Vg_NRwpp7QjBmreuJmLo9I3GoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOWe0FcWRpQ2mqKoEsSah6vQ9bjJh6vxy5SonXwDrCKNSN5PePjE7jHqriojggAfzC_locWRIS_u5ypeM8VRj6BSyeVPBcHEO2ScrJIAdoulavNQGDJ9MqnWkTLZdC6Jcd4df2u4EuE12FFOa_xOviz5sVynV40zT1l-vHCKvmiI_wufZ7DIo-ZgVg-IKSCeP_1GcQE8e3EPBJRJFewEbQSTmC8fHUVb49RbnOSNdK12RTkLl2M5B_0BWbEKAznGapfdZL-WVS_C0xl-vvsp_gjxXVB9CtlPv6k92QgWyC2dKCPYyqjHnb9oCgRcap-i4kKFfdfVytyIM-AEXDX6TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tqk1e1fP4PbO6yxq5QAHOLbRUm0w8a3TGONARczBffAiYWqiy6vBm-HBLuNWdHLlHCMULVdpE9dzx2HREN4U8dHVNFuyu0swf7mlMLlO1wGqssqLloSlFtAev-2rvdMyc-E9ulwfUM7_q8u0RELkmwe_I5n3ztrtJsFl4DHzloeMtYgy9iI9Kmaz7AtWGDtXiM_j1PRXuwPXla0D5v_k-7PbBTXkn-MFAxWl3PaUn2kf7rD9QR5ztyK_KScVCYifxGpQEiYrzpkQbFZL0Jm-yEGYRIqqaRy0jjqdyovhiFIoN336FFThBB5IHEhVY1Tdaoe4EpsTh5ouYO5Sgftysw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 756 · <a href="https://t.me/archivetell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/archivetell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/archivetell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C81-BqqjwKobxUFPXJDlB4nws0cbZfu5DPJPvRITTw4rRfE1pPnRjGocUgWnm1CxlMMS-2Aq4Qy7icq-dDBR1n3s3HJ12xgkSPAyRdhLNPwc57JP4qfiZNX1RTujNiISt87jgDP7BGFjx0zu4ofkJB31yQIdphA3i6HgSm4I0h2jX8nZ8Gl54t8J4Q5JEf3YBZweDOtGDxW28wA0dYx886BE8yu0jTwJu21hA_oBZTA6jE908IMcjYMxCQ7gi91xqMrxWmdkoN05h-s44qPtwS1Bei_vZ2YNo9KIdSlJipV21pAb0h6ygHigyNXKVLfyF4_bxz6tz6Lo0SG5j69fTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuEkLOjH1QKG_kjA0DVOf2mmyvQCTShb6Sm13VD_wANa2cjXs-HrFw6SbQ2MI_7rgyIlecY6ClcwjgOyStwKuk0RLJA1qGKkaUxaAXCfQ4fWpxS4elGaX-rfIQy3mOyc5UUAqEMvW5YcU_T7pgoanoNqq7JejzcFTmVZVKD4DBqURm0JrLqzlKRmeemlXl_Rv7jwPlIjfTdW2OkuSSAc5_cjdctczZEVxwfRmWmZr_iVR7FwxCuB7xeBRP-Gce9yy_-3mSKbeMaITId9CEWvm_QeTKdYtTmrxyIANqT9LLSa_yycAf20F6_TsWm7IcHTI4bQZXu_HefNT0hB0-Sm6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVtAbYwAK6ZcLrq2KavtGsR5oQwlD4dDASrDoZ2vDuNSwE07-KyzCVxaT1bb16B_CiwtaDMDecFK1XVJ6LpssO0Qo0NMGWbfxDhbF23r8PqonzMj1I7Qu1O1ON7XBNRU5FxuPbM5iooBP2BsnLO2gx9EXCcSf6w83Zsfj6A3ylN0cWon1mqDkwSZ18ZnhsTyemCcFDJ8xyjKY84T5ZPTgOJldMcfAbpI_-aeQoCIlJePjloSZNQ1BUMcGo7vRpw-C-X2AkCNYNUv260P6r5gUxfxRbt2tYMWDUe7DCRG2_hV7QxluhCHFv3PJhdS1--Pf0-dPO2Mpoub7VcqGGYgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=hvFul4MZKayhIFBrutZ8GKorbLL2Vo6v4qmdRg8xpj3gCT39VKVahj3ZO5mN0jjI1L236DjO5t0RmbAwUTXXv9YEnH_fIdlItCO7K9D8HtyfWOTjAPxqdOVCW-6yMRQxRiWwwZgiE654Ultjdsiua3wqus12TUhR6FlLNVKVkyNYe9Gs0aCY1IxqRXfP9NIiDM03PllmR9ftMMR9Wn_otorsxqGThs4pVY0tyf5KG6qrdX2KtLbP9IJsURUlg4iI0z8lWBym_EzGV6i7ANzXkryHugq3DunyKP6m841OHIT-RjgE4P61ZiTjxoPj9RXCWLL1jcHdEHBWv9qdULWL-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=hvFul4MZKayhIFBrutZ8GKorbLL2Vo6v4qmdRg8xpj3gCT39VKVahj3ZO5mN0jjI1L236DjO5t0RmbAwUTXXv9YEnH_fIdlItCO7K9D8HtyfWOTjAPxqdOVCW-6yMRQxRiWwwZgiE654Ultjdsiua3wqus12TUhR6FlLNVKVkyNYe9Gs0aCY1IxqRXfP9NIiDM03PllmR9ftMMR9Wn_otorsxqGThs4pVY0tyf5KG6qrdX2KtLbP9IJsURUlg4iI0z8lWBym_EzGV6i7ANzXkryHugq3DunyKP6m841OHIT-RjgE4P61ZiTjxoPj9RXCWLL1jcHdEHBWv9qdULWL-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH7AttVWzu8f1dMcZs-Gbb6vkdgRQRT90srW4YxpI1qGZGURIo2zIiUAWnyHOluy0gwoqAh-LMb9mc4t2WMZkJCOr1dGkLzJHa_mMHFYE3Q8EjWNQ1k9mGdN_lPrdYsxIHd1kM4zWqmIOpLLx-3qFPRbM0MBab814EjecbNewEnVitIYWNgyGhXicWhPakkceoFrfOm8OsKVLeuT8jAGZgLsKJ6o-UzWs000XnogXbEHCYBBXur_lKVGdMPK-gkWPIQIXAKOBKYZEtfm3RQTSP2IH93WhfqMrVfo6DPKg8IXgii6hAh_-gMbC4F4kSDn7tWf7wkLGM6Wn6ueMM9gRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=YR4i06l2Ys3xentg_VlDidYmHi8jJzDZ60hLFeoQuhNJXEiXHaFUWgWujAm6gXwHUyX6miQQggWKKhT3KB9iWJqN_o0836YFjeDoRIRuhuaCheCRMsNvHbvRQaghOhEPJ5hibjOrAws6bUzAuwrzLcqohphrGHXH8bMBd4CkzwFOoaWqTEioVEV_3xTpKAZSqo4_rXiawdFev5UEc3k8hVlGyGF1ra9O-UEsGw7yPQQ53KZ2QZyyzbjZqYOh9o8u_VwzxyOPYBg_l571yWakzt1XN8ErSmr4qc7bfTzOa0379ZQV-_mJoupGiS1llw89bbMR99hRrx-O57uDNfdwDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=YR4i06l2Ys3xentg_VlDidYmHi8jJzDZ60hLFeoQuhNJXEiXHaFUWgWujAm6gXwHUyX6miQQggWKKhT3KB9iWJqN_o0836YFjeDoRIRuhuaCheCRMsNvHbvRQaghOhEPJ5hibjOrAws6bUzAuwrzLcqohphrGHXH8bMBd4CkzwFOoaWqTEioVEV_3xTpKAZSqo4_rXiawdFev5UEc3k8hVlGyGF1ra9O-UEsGw7yPQQ53KZ2QZyyzbjZqYOh9o8u_VwzxyOPYBg_l571yWakzt1XN8ErSmr4qc7bfTzOa0379ZQV-_mJoupGiS1llw89bbMR99hRrx-O57uDNfdwDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLbz64HE-EHDE9sDFfR8Ra2CnuGXCmtEUZknYAG7MZfLWJSy6Pa3lDbx8G0EkMgqG-pcu47yYsjk_b9zuk0PI0FBsaZ7dPCtar8wDCp0RyMCOH4vnvqOLhvk5beuyfDogwhm_5y8bFFAxt0_PtvER9BHZKkU4G93Us2arTSjJKPaJqLqwybmy6d24eq7Ij8tcS2yul_clBXJEXXIx2fp-03SuR-lxa1EM7DC9sy7go62VeKq1J2ENavp0Zrxc-zya_HnSMUEqqjd1-lDWva1YgFinr6-WJzO_ZHw8nwKQiMnCgGo3Qurrw1wYYNx8LteZESYfsbFL6dNmSuuRg4FJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viKJMg5n0_9s09p68gnKeXx9cAugAs2vo3ewgk49Zt6KkIcORxk9cB2xWy5HdR_ZzZxnbM2mMSUmczQNmxFK22pqlJ9fp_BY1KC51VSa7erbSRWk7J8WUWLXYgPViCHrX1KZIxYGfoQ44Kt763_7pD3e7bP_D7iDBI1HGjlrrN_3JP-EKB4reCYue8WPkNZmYNIC6sEjYPeMg8ZCC-vXHsb8pSq09soS1T0dlawGImiVw6abAUhqEgowr0XwXngV_0cKttmMTqS_Rk5SDyCFxhbBJQWlwUijnL_2yGJKJpG7PAOIHUxFVO6--MkLnA9oJdPPJqhmk5l8SgIcLUfGlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v03m7ioWnq9cTWDxA0LJAkEywttFICCL9fp-_xhmwN8AWIM1jdAqrh7Yh46TqkkhE_gJl3L7Y60Bn22-0BxMBwhRulX4aHNe1yi4re_7yVSq6PXjwQFpYe2TYkmtrmoE1gboAbwmIfbn77x0-p5utX7bUxi3RAA6lakjPaBJ1RRMC9XWYi0iXurXZ2o764W6LGP9Zt3Y0kkxGzQMysxUbuqoPRLrlSYzlUjzdB-pJ6Rmn7oKTE1byTabxjaoiZtkr49V0XgFP9Yr4zecdzeie5Takjzkyv7WwYIBXRVfK3aqU2ZFhtYOSpfFo3W4j-_nW_-6KEoo1lJQSpStaKdbMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-ZbdVPXMGWYfjv2Qlsnps6D994lurN-gjUQMFUhBKqtnKoKIFV77P3_pRhhkPQ-NY0AX5ajWLMPYQVATHa36r-ikjjgHBuchZsOQpof5kNmY01bfh0QtVbe5-Dbox0AuWW0KjBqfOJOE9U-j1xQBI0tIQ76R87cHzSh5AOqb1SuVgvozZyE6X5iwQSY-B9VqG1CaEHSmZur0xCJ9yaiHP61HiXeTDStdSlCvus6MNOiNkXrsUelqdzwGi8CqbGv0vIs8ta0p5_MsHhtuHqybyy-gqYL41lswEhM0qHAPrjR4_y_i2hIqrve5A78owoP8wMA_b9ImrsFkC8O0nNPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-OaBlywkXu2wTBgVjxvArzHxrtLJXzaSlewSR2Fd281smLKfArwi0dd9lq87eMT9Ec-QKNR8inh8tODXo6eg_Sn6s1FmxDgid0grfeEi8YmxdwR0WuyAmcDb7p35f_Qy15KQxQECXe69DuCNVMK8oRdonzpBJlBfOPSudJ_kv8eP_L6JoEagwq-W4A5BU5gDCPW703jXW-GA8SMpsCthA7zLRzJFFhW7vfM9HUm_-RTg6aUi11aq3rFVwtD1bfAsaoh5RLL-_8hpilaRR_9iDDytQDGfjR5U8aRQjRGdSd3h-W_9ERhM762bzaZxZlvVrRtRNxPmw5FauAxXK13sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zim58tRgflM7kJXWsjP9WXf95dVElAIxnhoImuSfELwNLy4Wa9RH6ns1YyeU6fCX6CkkzyRfIceFt-f2a0zHgetzesq1PVNa7T39pwL_mshqSEuIxUbNX8ECaE4-IVHNDsmPKMnWBt3i_FmbD5hxiq_MnlcDK3vaszs_c-US3uQum0etAYr0iiWGwtVizxnKMxFkYpvIdDs5PRIL2Ywwmc6JPIIwp8-hGxN49ZY2cF56Yi-4wLt4IUDnxyLoCX9cNrW1YlCoGnz6DRBqX96qCdDZb2e5WFQPJ7CNrmRTi5tr68zMqU-cY5Rh-C5x_IhKMSZv2B08LEayDGlDoorKIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eexc6k07nUFlbTH0OC4YQW2xHt6sSq_o7mNV8-B1OW4tou5Zj9GkDUj4RXgny15gbfbXSRoMGqFZpiT3GJyj7o9HozM764K9GQhg9cV6RGgNhFpqGW1aPaNYwgwwGIlceKz_gXzMWksSaeddZ7s1nuVOe6sQNvrUuDJ9-oR0_l0UxLcAvjM32Ei05pFiqXJ1tLiCcTi6HsufGwDGvZeau3C7pTnejsIMznkblfXbEw-NP9bWAw7AqjQGRVyr23NPxOfbQ2OAdokQW0Mmpke-5jLn4A_j4xMp-gS1kdcQrmkwDraLzwPenAi-W3XvbP2Zg381us1l1UTCghRpISUE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUBjdZLq5jMAgow1jr4KIPPC7E07sZRLZAJ9CqNCOFGGMgyqufke-9a7p0vxHT2X520GC-JoN6DXWJm6y-d_LXXm9bQzM9XIQFS25R5NLoVXuV_McCMGRn7zSp3drBHlMs-JuAmZWIZOmLy1MoS-Ic_FKxCAeEk2-nG2DExws6gDQJ_cn6FmFxaI33yb3fY6ktSUJp3HUmdFxbeM71-N3Ds6mIaAPtR51jhZjBmj2nIWc5ozs0h3v8zPL16RSe6rAqBUEIjIIR1PfoBUSxA5kHTwivmoXqlrKalMrQP58-y74dsf167aS3L26jZtZNFy82wiBvsWBr92cWzm0oG-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKXQhnY7anniYBo-wHe_bowtJwugoiXnQj4nWg1Z2eIpyarB-V1EoUjpn7rvH8yBqOiKb2TtEIiol2BzyE1N2nO-BdGbbP9ntJUeVJK2J9GFqU7ZwtySf5_Co1gWNmy_Wr-qhAwv227WGEyoK55kJrT2Y_yEZW6VML5u9nnZgyb73ldWo_AsMDqi_Aw7YXcCRoAkIwn1kURmmDAYNTIB6OALiiD8gLmTHJNTHqzWYlKf626y3RU7RJvy2pg8ga6WL17YB7uaDo8Gsx_nRy5Fo-eXQLc02ENJQxHIzp6iSMjWaitc8VWWmPul6DqwgjvC1Y-ZIQIFFA0Sg_yx0v9Spw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxoziGCuLaWPAMCDARjPglsdS2zbVCjHz5SAfq7_BX8J-wy6FyDEstC7QEuR6BjuMDjTXKRGI729PpN0n7HZh_vxVEWEv0NM6Vu1OcCQvSf2uvL-8rCHTgiXiw8EuwGl5vKlLgCFze58w25JZ_1DHlj61WDsJ5z_Cxt9wIfPsYNoaXiEXiK9vUGyMB5xm6KXlWw2kQ-D7gg1ns38WpZ4e3pEraf4Ti8CBO69rsbaHV9heCkx01k93AYZnpLzq4BGqYID_MhkTuXsKFtaVWlAcguLk-X1aO5QI6Y1UyRmGsibu4cVsnN1Pfir69qzejG0crhGYgE4ZgQMBO37Kv1bgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-A2dxrUeLAs5576E8VmvTGm37OkhJV2THjpf93nPkTEvEYoxlUdh3KpnPjG8pkdXqbDMv3gieMybmU3DCAp9Wp3G8cxVL4_BcJuiK-d2SJx3xv_oHsj395Gx9dRRnobgpfC27KfUILQ5bf-Ty7ADZG5o3i0B41EQk5u-_-i7Ki2F5tfdKHJOEc9cT3wgn96_LBhYnmI_VSSdkjgeSC1OKbKB9LoDoc6qzpfslwdIFZj-GID16G6LlvOaN5M_EKndf7qrc8jxamAbdzXQ7Pm_kpKEQOVmznbDuwOqMraYW458rUIyXHbbAWGncjTw6eZlCMowsJrVWESfUHHLsPrOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=VOAACdR8upL18E70rYa6gGsiAyEDrCoDOEL9xO0NCIQVRoMVKLBsmPkbG6UeLoxvK8RDK2IhYATUtDUdjToFeV-H9OMRl7MrVvXMG4JNi6GXqpq2niZhQc-iAQIhW3YNlgbiU0ZhvHBJAAR_34apSuF7qUx9Y7rDFP3RWn1GZfgFZmabwVt9ztIG5YOERKgM_VcMYtSBdGI197jOJZh9sJt-7xj-qSu1bkKKD7DNW-N_qhXmk7sOxZ3bUB9ZcGwamVKSb4RXYRLyD9OTP-DBOKTzhvyuSdUBOOFyv07wkzyClx2NsPoOEiKEtOa2Ovhxa7ghn5GeH1jClp9WmsJoKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=VOAACdR8upL18E70rYa6gGsiAyEDrCoDOEL9xO0NCIQVRoMVKLBsmPkbG6UeLoxvK8RDK2IhYATUtDUdjToFeV-H9OMRl7MrVvXMG4JNi6GXqpq2niZhQc-iAQIhW3YNlgbiU0ZhvHBJAAR_34apSuF7qUx9Y7rDFP3RWn1GZfgFZmabwVt9ztIG5YOERKgM_VcMYtSBdGI197jOJZh9sJt-7xj-qSu1bkKKD7DNW-N_qhXmk7sOxZ3bUB9ZcGwamVKSb4RXYRLyD9OTP-DBOKTzhvyuSdUBOOFyv07wkzyClx2NsPoOEiKEtOa2Ovhxa7ghn5GeH1jClp9WmsJoKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohv0rmgpCLR5tXKiYMS8taPmOk8cKwfMmZbcHeEyoRUv_i9T7FmXoeHdnuifb9fNq_7g5iM0cXZmdZ-U-C6YQF2aEfnS1f_6sx6kE1JmSUZey9m494ySso2lfriT0QgSzZJY129iNvyD7rSRK7Y43kCiCFAywYas11uem462cvLoAn8tLxKNfKW8oeLIH7E0AhhUActh5beWPbNmLBuLQBcu66K-JvdlL3tx9POYXDgVFO2ONZy2BMjVPBK6_hmlkcSyrbOhOFsRTxgjVMxe6zPA7NXpwUrFNQiz8WX75UcH1TZFME-GWHJiwnkYNhFmHuyJETCJQ9CzlU8YENxZVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIU4d_6pnF2IzrE39kibzm1zG2kZKvMMh4kcf6nIVD5svLdaZB8eGBaDgI2YAfJp4YlZhE6OHoDVuJA6E9Ks5Qg9wGenVF51BYtcGGiZ23g4j3TWloL_mKqOl_g_2JD3YsxL62vzFPEZdyKol7ct6jHeWaOS1oL1x00ev-yBGT5oELzClSsUX5lWNpXbOuRUo56nTLnfYC1eUxuf0E1YMmBeYUS4I6ax9kQSB6aQs8xXXc2uZK87IDeBskjm2o5EfTvrISSaztbQCjng1Xl_Ew3VthHptpbQqypiOv7e9I5AAw8rVqQruFlpi0ZIGNo3G6MNGoQhLko0sY5NxqJN8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQHqObg0Jp6MvbGgMQWLEdAPm9oAVdkgwFDFyQvDm7A2N9RchkH5IcKjwzeptCorbTbwpsxLwSdX0EaEibiEunCI3KZUI758UGU5toWclu9YduxVlP6qIp77VOF-sET60X0V6m8vehF3hm92lErx2KhA-9pBUr7uyNVsM8pj9SjTgzZjPdlBkiJpq5rAf6vWkc0eQGYIM6P0g4bwz1ikuJkSr5KeSM0q5lHAqqEMptsxdPtLElHzjDMe5r-HWzngMn5Det2akvvXsKxfsB8bJ9uoZZcFnLt9_lyokkXMY2LBsJ2eE44j8rjBrll4YDVL3h0cmSfO0EzpwU9wI8qj0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhcfUgt_SJ8LJzLF-OechZWvrUK3glNyMtmXkbOC5ENUd9WsHAK5IeB-2X9IlCSCbD-3tEaGdu0zxhDsNohBqKzusw8IZ3ZK3gZj_96r2ZRr0h2qyny-xvldE2GwNGIjt9gPusuj5iG-NCjwxHN0K3RRXCzTenanOkZzj0aE1estdDdp7TxID3QrDD3s9wYdDYWujnBCTbS1fZ4Sg3UiUc438t_xZnxWhZxQyJW3se-Yz8JfW0BiNgUK9E38whsOWkseBi8u6ArUwObdaTHRcp2B0qBKtBKZfTFkJKSd0reXYfccydob6uvy-XSfEeS6oXrLeSgNtzjR7vPbHZQwYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRbu8SQO-gEVOsjiB8FHMmSgAfyMIVqjLZDiI4bD5bzX-61svGIhdpyAplK2dg-CL6TTSu-Ho5ZVUtk9FgDtlE52P6tZkbWi8Mvh8u_vYP1lm4YVCuJ6qJstQB-rtdqJD_zZMU3hA8StIz267Qu10HecqR65hNNrfK62l4FuVGxW8O5Nc37F7caGqSTL4RdfAe7Y_LYNI6TfRWW81SO4MAiTrXP1QW0xL1xBBoWhmfMq1fu_zBMlJBQxudsm_xRX0CKtAfURFmZNnGLFaQucXQCF363V8inxropO7nDe4qAoDjL-JKp5faOKvHMmtfQ0TTlDisPA99I3EzgpmtOCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShaevYaRbFSOI0NDDG5nUEqK2ei-AWyBxngOFqErCQ33Ltu90z9cpdwJ7DNMESsIwE1jSnyXMFXrgfEJVi7LXNqS-_19ibEuxDM3UfRwbgZnPHsudQ8ZfNldYlcEN0soYYZzzbwS5iglbUAifuZ_ITdq31SNbHjiMsr9hBpnOeJq3ci9RC5gDZ5_M3tl262RcLXruSwU_ELyiby6ISRHZNKFAaehowCO3bab-tz0HJT1FraBBfs40HxMoMgc_x5onfaoGLuhR28mLiL5LxzQo85VHO0QOYmrgGuDFDjJIJDa3jxEP6dqrb1Ui0zXtRWf4k3qPwFZZtv7teVLp9pieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/blbrF9W-9sJt__Ei2jjBnTuWIkdvyQIYUzt-6a78W5S1AuPtCT6v2FHLGaDqOmR7jcNCCzep7k-y8K330v2PW5P0HHd-oehiiFYCA2GoW-staXtudYKenYoov8qi-nGoUVdsReqv4MciFb8DbbtXEG255xk7g5bmLFq0vtTGXJbTFnOAU5SCl1qQBBwvFNo3dl98UQeAAxmdBNpvCWF66SLZfo34KNzlpsQgIfL5Qve8C-xQ9ZCfHr2NyKafRC_HYj0I2BdhodQ0auvEb_8hjzKtHrJpeIUK1u4HF1W3YhhNTcVQaK-HSR5Q4_rVipZuwnb8079WA03hk8NWqkIUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0PG7W4-SqyYh7L_F1KFK0tZQcx4fXO0F8QnqdZGjcs5rdK6VLEUMQWpmjHMc0xIvFM2sL0RctEIrOxYjc5RiBhntzRTnlQXVcZl32-3LOtkVkKxDfmH1rtWG65OEI3hdRsmeDuLhJCpHz17k3gPrjem8Czk9nRVmfNb1Q3CwvGWGako4tgAqwFbaSh1fAyMdpnvvHMw6L1KYUEAZiOCfqHJ7nXV8SSIfwMkXnrM7mCATIFVYdZFYs-poGcsKcMG-9d68skgWBlQcIvxtLp11ChzXA-f5t5F35IWmUwkCltK0WeaOtqCbw5u1KEgeUBAfdhdxmaF4Sdnog5_-vYkvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5auEIMP3P4epbWjv7JOmsqdh2_kTRdMK5DXAF4kQ32JrofBVP81VNYuVauchG6qAVnf9T_j73cAberEGKCsurqYtBDapB70altoOc1fDqiuXn7l0fedpVUYDvrD52T_YgpCfNO9QqYQ6z0W0Nu0Xq0ml4uw2kMwr2Ve7pF5WPyTYeRfpmc07ROa-ZhDLJrLH0FiwnAPlSiTnK288bZy8n-UotmzWSLJI_Xb3o_nrKbT4Xj2L6wAvP2PO3HRGp9Tpb--E90_9H2yXe3ud8wiMpSPT1l2YNyTTj9qmY3nP8wIR5zhjkBQL0WT37HWTNFgQV4uWTT1ew5exa5TyVkbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wl4sVZTNJ1Kauih71QNOhmfdcgCevUkhkVrcWwSUdxHA0Mglw6CfFFb93YXHcRUPY2YDScTD840P8C1pd-GywDMN4krdN7rOBo6O-zJxzZoT2cDXUC4sg4dZO0h5SCszyA34_G3gZX4rPIsSvtt1EuE7cvozKzhOTmLjUgCFICaIUxgbS8SK0b8Eh16ki2qrsN6Yb45LLkexMDTboNp-HMnEZM0JG78As1VDSXWiprQceDlLQND8fod3vfHVIPyVwOiBk2YjMrGunp55VNHnR21dWGDej5oLcV4GYixtv_5Q86mFBgM6o8ixgu5QgmnC_E-iO9Cvdkuib3yjn0l4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXQgbaxuCZ-et4p-55RXPvEzS04BsyHBMuoo1VXvvGmR_I1yDln6vuO-wpg5cbIO6WniAbZ64ln8xRiEXI9tG0id9gzUpSlFuY3pyLzUpog2JjLH70BWS23pnUSxGokHTDK_jvyupgXt4gUhZx-0g2QrIWhA_h2_dGKu01wyLVISR-Z-G6KaHzvTPpOFL7ZjWo_pGJSUkwphqZL7stVqTnLQOJI7cTLCQnfYi6NBNSZnBe9gSXKiApcUiHSgiEryU0_BIhyq5FdXhg1RA0UsB1pYHpWkPXQV7kntdyNPpsKf4clSRZX3w_8IIVMcngmp-35B2xCjy6VJTfqv5AsC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3d80NJ5Yz-HC68O1OkF-TinWWJ5Wj4HYqJUcUTxjJB1DIzbxwJfDpEuEeRTurKpbTfgu0VZfMFyHu35rqncApW_KG09JMwx9Vt02UAKe-NCE_MCvAydAH10YFUxeECkhMaFNdJrLW0rUkbLWhvWfzK3qdz-x2Ff86WRu4B1MuYnB8tQ-pJMNDi7JVJHgzjHAKmv56q9y9UedZzwdqUvrxZfKBHop9IWfyZIE6vgrN-4LWLLYkf08o0QY5dgSeCWzLKdhajF00Ar5TBO0zqBPEqvAINuA2DzTikIbay3qsQJ790e2lK0-z6QxVoLhW_vINCCju3BxiVRTedt1PQvaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=Rjs0igXqzFrH6JGEdwcw19EACEj2fp81coLYFLLZs6dRPfthpDKWw0JeIOZYdh-3Pa2ZqwiGusuwdzGFXmJ46qMrjnhg6N4rITY5aIUCR35279i2uu7e_SfKAUc6PbHqN9iH_v3RvumM6dxFebskUpcKMItUnSIF5BHN_UmnudU5BkCpxIrh-0kLtHsWKxHMH77U2ruXq1jM03nr7CV4Ifc9IhFGzOnVcp-TQA0rlCeROUbAqtYGktFW16OCz3yc0JACKleaIsOdk7yISu3fLfxkX9j5m6Q18OBz0rDujWV-j6T0-ItnU7MC6YX0ok7keIIfB0KelgkxfZxwIGuJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=Rjs0igXqzFrH6JGEdwcw19EACEj2fp81coLYFLLZs6dRPfthpDKWw0JeIOZYdh-3Pa2ZqwiGusuwdzGFXmJ46qMrjnhg6N4rITY5aIUCR35279i2uu7e_SfKAUc6PbHqN9iH_v3RvumM6dxFebskUpcKMItUnSIF5BHN_UmnudU5BkCpxIrh-0kLtHsWKxHMH77U2ruXq1jM03nr7CV4Ifc9IhFGzOnVcp-TQA0rlCeROUbAqtYGktFW16OCz3yc0JACKleaIsOdk7yISu3fLfxkX9j5m6Q18OBz0rDujWV-j6T0-ItnU7MC6YX0ok7keIIfB0KelgkxfZxwIGuJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9bdX0P_hkIZJy0F3twy8_XmF4Be0Hc5eWJG1iRLAeJR7XQNFTQPzIrrhXOQFTmhJii4sleTYnPh2ESVg-PUjjaYMvAjuLHdGu3ThWQ3qpoZHGMd0Cp2KVEcxZtFfR3aQ5IXUu8Pjt4JaHxHUFa4iXe5VqDQGUnqBValZcZ1rRhkGrKd9VdwZXcfGOKISJfpYlxzhI8CV68b_CLqw7WyBv-8qSzUlHH-XfMmk6ooA1uaoNO53w5z-HZUaLnOdSSkAPXSpSoqqUDK6V14LQLhaZ9whzJTTeXJdVh0s1KTI9Uaf5FCZP1wBGwlG4ov59CCj_nyNhmR3Ad-w7c4O3_o7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHByOIggSmMwWHg7U8I5Ub9nFg5NKd_vgb894no8-vAGc_DDtRwQLPrvZ0dRLkBFNN6ka8t8llPh026H4cFSihi3Zmv48qcT_eHHULUPCNCcmCTBtF0cY23JLPvkbB2s7woIRvcZlddLSlqwwM19nJZNmizBfMOnLseKwaxUP5cFSjyPw2Ftg9Bs8TBvY6Oo51h2kj1qzBjp2UOUq1Kk5eLsKCspGnk-BTighi9YwGN6xS4204o2sZUo8Grp6MjQdg1b4ZvPf4WeRthMbCnMEA8a8Ee8n0LFcE9cI_jfTIpzklCLvNPkSSi8xxViTKXo0Y0h7Psi-R_IBnUMG1nr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F91IYUW83WPKYEhoHhnLAvzI11Dx_PTk4Fns3Gr-kTQDH26PdHkCtTwpUTHXvYHHEoeTxyo_tE4f4Ot8_2anCtB1_r1FV9mycKitE8PA-iOYFXuQLQjX8JFD0Elcx7h-pba6s7LYgs9zlXYcDqebzqOCZNOUQQFEihXf301z-kY0Ue8v6hIYw8IynW211kweD1dMG4ykt-nZ7a4GBkgA-YgKM_BDbUlzvPMnSoIPML194c8TzmVggXtEjtzK-f4u1YW48n3Nhh4CmBxsrQUnHDiMetrAqP5T1JpzkC91_wpGwpHgvWgYMA6ZxhSz6xIQFuouxtpxCbfdDDPooFI0_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4TjvDgwvfx6BinK8sRleQYM621AvxsFb_AdD-sQkLmTYoC8PADzPVBtH9Z2FuJbOj0Eq6LGQOdfiIy_Btz2N5CQ4ocFC4Yyrtb-ktYP1KH9SIwIgxH72HyUnax1DyUI2sWEa6_-rjeNYVBnBselgavvo0wC0BYANzEIloDkhblDtiLgZQAoyQYbltYgdgSZROrlf4k_wxHsIqGG3k4-QbsM2UNCXniNEAzeOZ6XdxnL_iNVQbzvdbRmV-XuzjJVMIh5ouXeCN--51MpiWsFJbFrA25U5AYS2Pasoc641rHbbg5yKjocD1R6CHPNvsg6gxGF12RFMnDKIITGD5cOkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=lA5zV8ODe7ZOtUyfP0287cqKNeRNTGJpD7AlltE0LoEZlCRYymQQPuWBsGtbLhCKTUuBxida81IMWKEn9_dPbJz3Kd9n9x_j2qsxZXLP2nliJitsjYtx3Xf6ToG0EFzFtYTzKpyMwFZigplsSyYcQQXkC_LvkR2i3meHeFT-MzrmDNGpR90q0zzFQ1fDAyY2xV1bJDOzV3l72H4CSAHdULFhqm8stN76Fe1e3uQZarY5Ek46S4BMaUbBj9f-v8uJ8-jkWnq5W_QPkrXwypRzCnTTr9X35Fd8TTGoiQFdpMcv0_xGJiuJofNA37c-Ax7Ps3G6Hxus0CVBfqT_JOqNmHUK2pTUeBbeOEl05nRuouOhFyJ2tCVVEEvrc5QeIto3wbOWNAUumc6ioBfbs4SEZuwa0n_v01gcZQJZxwtl2VlL4syM0b3p1VCnADo5OT2awi50S60Xi-CoXxTl9M3Z2mm0DtysRp4LF3YmXfrJxsGcxKvJe_IdMumlUM8p3JeP8onYi6Hn6pJu2U5AxCUCuBchCEXqnOV7YmofTbzOnsjjobcZHQ5WqAolsNp9Tw6Dyn2GhsxMLpTNkNiq4sIDYc2_GC1W_Bnh2NUkjf9DUVhyrJnrlJbyDiUwA3dC1Dq_8Mp2lPSGLGjmL1KhAZnoFuOeu80NfigfFpUb9OKXumI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=lA5zV8ODe7ZOtUyfP0287cqKNeRNTGJpD7AlltE0LoEZlCRYymQQPuWBsGtbLhCKTUuBxida81IMWKEn9_dPbJz3Kd9n9x_j2qsxZXLP2nliJitsjYtx3Xf6ToG0EFzFtYTzKpyMwFZigplsSyYcQQXkC_LvkR2i3meHeFT-MzrmDNGpR90q0zzFQ1fDAyY2xV1bJDOzV3l72H4CSAHdULFhqm8stN76Fe1e3uQZarY5Ek46S4BMaUbBj9f-v8uJ8-jkWnq5W_QPkrXwypRzCnTTr9X35Fd8TTGoiQFdpMcv0_xGJiuJofNA37c-Ax7Ps3G6Hxus0CVBfqT_JOqNmHUK2pTUeBbeOEl05nRuouOhFyJ2tCVVEEvrc5QeIto3wbOWNAUumc6ioBfbs4SEZuwa0n_v01gcZQJZxwtl2VlL4syM0b3p1VCnADo5OT2awi50S60Xi-CoXxTl9M3Z2mm0DtysRp4LF3YmXfrJxsGcxKvJe_IdMumlUM8p3JeP8onYi6Hn6pJu2U5AxCUCuBchCEXqnOV7YmofTbzOnsjjobcZHQ5WqAolsNp9Tw6Dyn2GhsxMLpTNkNiq4sIDYc2_GC1W_Bnh2NUkjf9DUVhyrJnrlJbyDiUwA3dC1Dq_8Mp2lPSGLGjmL1KhAZnoFuOeu80NfigfFpUb9OKXumI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKQYF3PTDEpwCz4IeId1Iagm8OClZP3pHkfTE1Y2z-2o0ZtXUa6lyUcyfRk9n_nP-gNAbhenlI_dAzKiLJlGPMk8ISLZksjRZ9y3bvybGdcKA1HTLuoa0j3wc0DtLWVNKr5QVa7Wr-eMIWF1uNbtYDdT4cz5TW8AVTnns1EkA0ywcjVXuhdZt1JvOgUhUP413Qpzaq2nIkX6Nlxk4he4ox9TwcG_qOecpyL-rzCuAV0eu1tN1MZP6DJAr955lL7LU9G7el8a-EgjjNQz2zE2AJEGy9dXGeZ-oRY5QL12jlGExuqLJ5MGIRYhAHmUIbI-uAOPrGx51Qp2e56AN9Xh-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg9yVLpJIDuFSdnQgR5FCzsXbIF_YX5bn1BTQxhxRB2PMDeNZrG2ZnDKPtNnIQpdHARzLveOR1xV1Bxf-BWacAxCdQ_hmVSmpS7pWpjHP5AQOVwftR2irT8kRbq8N0TQ5Cotsc7ngsJBkY46VWvmgX1bgR_EoVgTpQROdW7-62cNacNaVz5JGJuhcfvx9CUZE8cWTtRiqRPaFZkMRDFCL5_mwOjZlW9_B9zL3b2j7PYoX9frZ_kcxFOM5qnz-XclZ7KKOPK9ETPDakn4lLGK0iSz3g-CtRG4n9Xqs8UdTnb9nciWAbV_RfEAh_MXGTRZ7gcTyDrj1g_HSOwQLa3MXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMoTLFeDyPUibXLOQIkWqwA-NLtbWw4Qll8DyOM_PDt_DVwOn9F7sQbhYB31PMMHxUmaH84_C4q9YZ-l5X-cYNWOnDURRTigg4LDmpZudJ2UdbwgRDwYLK7fI6tfDbIoczcqbbQYYW370Pum0vH44_u62Qay1vNXMDAeXl52z4PcdtlE_JtxllWDo_Xe3jCMYo2v0MuhdEhx3783ANV0tLWv3ZMGvYp2-16HYRjFn9siz7zG3jEsJb7ybF6WHbbWbni4t8ZIciP1ACpz4bZYWthtfg2hbpO31XImZ8dndj0F7M50ciIC2AZLreRdmUb5bYsiXfnbWC12PBiutCENuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY5ULj61CMrIQRNTEeLp6J8yA6-v1O6-jzGS0xcKRd9dxPfuMw5Yx35Ixoz9ta6JWoTT1ECzfZFI0nE4XIu7Agj3kX-BOr4UV2cAJQtTyMXnD3uTOBYXkjN0Qt0qEGLdBIgOkNnkWafgK0GGAR_aD-X6r97JGYsPd_BCIlBaIRg_F9f7fOlPrdErofKsHUr545P3d2YhxYxXpds89W8iesC_pWCWRpYXNE3ZR5QkJiA3oS0AohSr9sEfBYx_u7UTGyctkkEF7dAXV5iVHProD11d_NsSVyGvY6eFThhFLggtd4_OiKRB_ntlau3aEWbJXSI9Q2WkihiAfBa8OeONUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR2EOzTTRYt1Rz5A17ibAgxwZrFByUCbh0FIQATbLI-LRJ_dr7HT30vSnqJwyjvdIyp-MVCcnk7jgcKef-d42D7FQOyibeVGmU9fIrJXfRcq4TQJgN5uaaNeBBB9kw32ReGKBH6DYEj5_wxBt_p6xVva6YCdatH37Rjdp_zwotYYrrxbKkGeYeQg8dY0pKaRXVlmx-c3ZSyMjEre3Z35h09GYOG0Al9WT_9NHeur_Cw2_m3TEBXGS9AymW-zGS_QUXeE04u6qs5v_ZNP_7-hAjboz7U5nzntZvTF9okX4DV0yW2CL46zxTMXeX_qDJtfoXWvqCvxaofSoxNNnJaPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgRBJ1YMe-35fKE7NN0H-Ly8-d4-GqQAqT0yHS9iDgeKSdPcK-d-G_8kg6rZ0_LdEU3b9jFX8h88X7f-XDcJoJY2Vo961UzNUU9HoyvXugnxDULa_y44F_A6-L51_Tac5oMsQG9LKNl5Y_4i5f0HFePRPyaJ5kyQYszcd6Ka0mFjulw2hlv3FSsA4RtecZdMq92de0dfSoHkALB7p1j-tA9Rh6XjsNsvFQ2qt07hnsAZEZCLiKdstcgScMRAc5BH9ARC7rshPDPzA1uRWcT9lWoJNRa_g-SiRU4ibToYMktZKigO3RJbZxxrMoJ2Aj26hYEtjS2CtTF46hwGO2zsbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou4g7T37bupnM8bk9MUogHAAAtC56Fy2uof4G-SraWiji8YGxxSbj0mhrZIIEH6GgtKr3ZMkjSTtWouRjF2U1iohybsyWloIdz7H9Bw0DexESu2BYrDEv2kmQwV6pq37FRnLlYjpyL0FdF6at2D4bmOVY4IcG7HaRN066sVG-H0yslLUjrt7fq-X6tYyI6tbmgVqIlrGlIxaW0Ekl8JDctydpdk7rzxAAcYquOrNXOrNsp_wRBNqayoicogt2EhQQPKWphgKljOAslTa75hIjH7EJG1ng6AasViqoqMDjOUqyYgOJNRFCcXqC250onKNm4iHIEd0CBVKsgCabTuDgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=FFqQcx0BlAxH5eHWfF7BQm8gCfd8BYtdPNfaTz0zDLpRzmyCYVDuGV1p9z50y0DW0UsTT1yg1SlnoAGcfYaAeZYK-btUrj9L_HA_lWlAH7VRYst5T-Za8vO8C2gw2CQZtVCSBZ5KmoTw28oO3yzMMFtgQx54lwHER4U7wGdxq8rMNlsSDNlVLNDECnCY_ToJasTdVzY3LHNMDUPoB-fisgwbkHNmWvrYpDqfiCr6VjjhsDVnheQzYOVDGsLq60_1G0cCUOFvVKcnmBBznBng-5ioqm5v_096qFMj4L3rNqysO3h0KQnbDt4rg7Ai99ERM2DyPGrAWYRPtVjptAkptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=FFqQcx0BlAxH5eHWfF7BQm8gCfd8BYtdPNfaTz0zDLpRzmyCYVDuGV1p9z50y0DW0UsTT1yg1SlnoAGcfYaAeZYK-btUrj9L_HA_lWlAH7VRYst5T-Za8vO8C2gw2CQZtVCSBZ5KmoTw28oO3yzMMFtgQx54lwHER4U7wGdxq8rMNlsSDNlVLNDECnCY_ToJasTdVzY3LHNMDUPoB-fisgwbkHNmWvrYpDqfiCr6VjjhsDVnheQzYOVDGsLq60_1G0cCUOFvVKcnmBBznBng-5ioqm5v_096qFMj4L3rNqysO3h0KQnbDt4rg7Ai99ERM2DyPGrAWYRPtVjptAkptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyT_Oubp0Hngi49WIrdJ0pK2ai5j8mw9NXOLNl986JwNyozJYLFXvKYsWUCdqdUIl5cr500THFoYBClmlAsT4VysrGtHcjil5c8phl1moCiHNolOOjCEWW1d4ckSfTMxtVJLGPbChLsAHOAgdNKTwXGLbVkoH9_VuwQq3ZQPnLoBUTiETFKJwEykd-PlIP1YQVKyfuqcARtUYtaqP77XMOSVUl9mtClNPrbKB0VGTIR7Iyu4Pc02C2o0Gx70-Uh3LW5-lSL0EbIyzYsOcHROzaVHSkSQ2dUVLPcTQo_EHorD40RmNumZL1VUC83Pf7ppkAlhyOnAyb9t04sSZuBHWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YftBpEWk5SPhrJGl_cyocB360abjJcn4z_sXPYJZznDzyKETfpseu06z-jAHCxOtkk9W2ZUJ46esBa8cDa7KWYKv08ON_o0Q3aIyFyaxwS4XyHEMTOTKsaTxAsxnfe3wvBV2vaC_V7ilyVY87LBCSIBmWOUsZOPG7i1_J9TiFcMmqg8n0RhRS1jgYP5ktD7ioenfu9nQ3ZgnFZgGvpwC7WMjTE8PUdDastwNv0buWWywRLXiD5togd6SFHxXUzNXTy616Ur_oQ_9kjDM8Y1yhnmBtLRIIw0uWpXqB6P89d5_gdiUcr99j4LhVZ5-ixbOnxfCwX1kMBx7re76JLsyCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odO6wH5BrRk1lADyL-WttN51CICivJHmNl66N3QychoZY1kTghccqm7zxDVkVq4tygUe4Cv5yIPmt4bzeA7hj810mFN_plqb08-mWktXTD7LYh1lwLoSU9MYeMRwV0uuxdDue_H8C6hVuPMDuW3QbUm9XBiKJKaNg9cCMKU2H-wdaJS6wweP_s97zNrbiGi_DX4CYjg3EFoS-0pt1z4JAcbNcKTNgfgCdVOtMHAan4uu0esanWG1dV7DzY4mSylLdpBH81y40XMT-j4NryTPZfRxj82eBG3vUX3l5djXISogYeE1kJMvYaGIpQ080XsQayjC4AfJxKXKC4-Gw1-JwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNu09rnTVPxvzLme2R92Oc1ww-6KPwLq5CzH9DlkBZRSP0SwZycKdvWMSpKTAFXrCVlDO2Ekm0r2vDgz990G1I2pDLBdhAWwNLjJWy7fUUB-BFw-L-XUI-5gt3Uig5yS1k0Kl_x7OjJnRFiur7nhLc1jy5BWuH5Q6UqFlb26n-NxhKKDMRUV7oFWPlpKsO2ceX_RjXes0CsmcVVeSO9NHIpyEMK4y_Z5VkN_IzygDfVSYNdXltOObPEkarp6ctrthDQ0qZIVShXJ9lkd0GJoPX8oalTZ0aFQS7tmFrhTquMjsDLC-WF6jzMidKdZqggsClFuHd9NQW_5w60VLiep8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOIqlCjllM765bY-2B8yjEudgc90VuzZkgrv1sP81Iqqw-jAsN8ClNI6rksbGwqkRbarxIc73YDFmeYVHTTlFuGhG9d1nQvv7LGopqSzKFX6ZTMu4zbZ6socSkR9zgeNPxwXP5hAq-W5KnlOYmiNkxRnSw7smi21Rd-YGDzannl5PwpTh2M48A7UI6wLxQHPZVcDbhm6biswaeH5hMKk_7kCdKNU9vYXmLk34dS3I3enTmAMlrCqrQ1Zefpa0gPqrtdeo1tlUmUMTdKlA70ODk3Y9sOfX_pB4QiOFTm_Pjy_FTuqSm9iA_hlDAZoHukfaxt4tLF4-unSL8udtOHWxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pivFDgOR9xiQVce2IkujclQ2qXfHSJ-XQmytER-L3BVPgR0aQuFg4ExP7DEE6MPrLxKl2EprhWHmg1ZFPmez0OgsCv91a5HLY09KGrbRNfRnDbXQww7lD9wzb1ggGO16E6q8yviS0ixeFalkGMgrXKAILOoy0Ww40DuxVq6OwwUhwNnWqKrlYCgyukisZ2DL1ZkiatPZDHsLBLDJsB0yy_FKDoAgchJeKd1wDnfXSizQVwKgZRyQL9YHOh3dAbGJ6cvGkZJe3KWmWYGQjvMauOT7L21FC64sM8QqIYZUOc0EYEqRzqnBMUv7U5IpDCL-d7_2m0_eI3TgugqnTz5_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucayDjPNo99Hp-FZ46961vZDcZAyaxKpdZm0q-hn2lusaD_alezQwSz7caxAqpnzDtzKA_PVKKMuuCD2pPgTrHQKgnO0D3SjXEDPflhzTbkMpS_E_M-__LlmvkOXlpl7XxHLCSFbZpZxHe5xxP5AyLaJ0KhPktDOlzrrFrQTqjYVBhAIq42xGyWoP8YCtuaU4ZwyH4yb5Coduc6QxYwDKAjTobYE5RaLV3PnCXkC9-TTjpSb3_yLYCzHTf3zYs6qo2ZBiohggjuaoRGQuD79Wg3phNelEas7pwDQp2g9gYriyBgBqAtDVncDjNTueLqxsKkvCueWTvHNKZU2fLCE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2-KY63fzOfCBRUUheLTFaK3oPZON3srnAdh0B3y53mwHJrrFdUYHKvsY9Xc2lXVBLpZaptpGn6zdI06-Yynz7opH_ci_uloTTz7axRyFgVfZuAlXAq0yaR7_73DvF_w9dvSmmu6SWOV2OhadwzHYrKKMYJvEM81JWykKvA3qCe8hrP6HVTYtjbGuM-XTCVCBA6JJLd6PrBxbHCshiW5qJhRaeJc7pLk8K2WJebOeNnhyv3z7_U7rKv7CJ7vYGWi-CS1C9PqDU2hzv_l9V5Q9oLnXbcZLV6GtXK49aelSjJjdOsDokDSYNavXDCuP8Ex7rKaHVMq9ztV58idAzywxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqudJe4keowP1enAPcF6mYFhjPGYJ-BePqmc6QfeWaUFoUyz8HbWXKSVch4b-LI_OcfoLeEcA2-2AjRPihkcmjCuvOdw8Y8jtDPTC1XwMnfbQXcPHa_ejtRzwgrh20lIyGcGg_9vpwZa_ygvMP2fkhuRr5cBksTsAVBh26min87CdDVdLq3SS_16T2eIWrGX2jAAgiw5GZ0KpaMaeMW5OqZQOfaz6iZEmoxKyWZVcMuA-yMHWbvq5R4uJ3g5vCWJmt2tHY8fVjYVhMK_Wsjy19MkVprWF-W2fmGrefxu6L4WEvTTTAn9ToldViG21UDK7rdeYlpgODT5e4DpIY7btg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4INZ7Yevb109Kcc8k0Un3NdjY7UmJsh6FtJKn6wpGOzS_kH3A4YkaDXm2fgUxFGv1HpcdhFfeVVr1shsuysMFILNzxE5ZZaGlCYkwWwBPdUGmVludF7k8JLicUk0Nzny4LcaWh1JT1HIQ3QLudbWtlVfRTsMqrjU-jfKNtuGQRO-cdVcZwQdbjj6v4uobu6LR9tAAE2F4583X0GuQv1TXluvvm7nth8JsgeLTHq0ayuzSxIYLMCERvPTlY5174qG_kjh0WjMcMJ6-UHHT1jc2RtqYFROTvEaqqt0CYjLGaJ3nT5lUNqSTjnB34A9HnsnoIAmhH7xt3v_w8ky6RLIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WuFoWiHHMljgDd6Bm-cLFZzdOFFwEQUrFlvr7Q_eyJtUNKOzMB6Btj8pMsgto9C-tZbwC-RjeQMge9rfW__vWliTL5ARXBTPIMO1JejgD_9OmTBi8JJeWBCJog0Byi1efx_rhj7mQcoE9gGcQfvz1jKG-GFOt2Hop468AxVlVJ3VN8eHtRbomFT3vdWlJs5cG5tS8Lzc8kz7N5UMMYacu9Kx6b__XHEnZ6y1M0qRlj7Z_Z4z8CKCGEnSRC3K9YBhsDVp7vggojDLuCLaQ5HzoTkMS3qFs1nnLiDmOtHpE13n77AcihP55dkgcBmslIHF_7n_mmocGhvvFCTHRpQX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_MkzbKoPPFmF-mBD0U56xd5ba17rbPXqjNDSFJSl4pcc2aZA2O0LElSdwsZVpHQeXvpVlDogYEYq5EdXwJRN3lDcPZYTWbNC3QDchLbYB4gQBIS4ZMYMvrFdy-wPHbOUdW0T8RenTMIZ7SM5OX-J2Y597AOzP1sO1Eh_AHiN1TJqiIhjbUtIgMqgz7j5Tc6oh3rInIh9-EztOsUSlPkQ4DzEEPsacdwxNxH-KabwaYt4CzEbPILskrYBcRpBnUQfJc2QjOzhq0lShrvMS-nNkqyn4FtcJjWO7Hx4eI1Wi8xR3SntRot5dh_bx6lYzgQdBmjQn_2WgF1dj7TVkFRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hq91SNUb02eqFyWyneS8S_NZ6WuqBWDfR5uF82w74xW1fH_M90_iT-j_SGwAIH1ka75pY-1UEVu0oGfJfLyrythATZ1RZvr537rvpbk54BgzMffVrADQmbrVKGX5dA8vZgY_6bayGcPn0uHpHUjFYXaKVEmyzc-vaP0mTHQJwB4y99kx0yKbaIVUKyrpKNWe-mK8UmhvMrexerHV8myAHIsqsbPWIyfvTmw_cZXYm_-DChXtb41KeC8B6LGqEWbN8PVU-LLRJOiTopZSfx_7C_HeqAgl168q7vi71mJcZJqvw9XRHfMxtSON7koQiCedZvYp7b_0XeevqPPr4bzSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzAYmlLiYV97nDF7YYXftZvGdjVQIdCsrb8HXhOEngbUymXascSZ_GKwJtAyZi-Z0y0UOmaUimlomVlqVAWBykrmekOEOccfmiNRkmkRNi_2sDHWYZ3nCuFc6oS2DHARhgljFZV17ptFiAt_r2O_OOmvUPZs4GRn-LdY4DBpcLgCL7_ZZkBrCPimGPlryU-XmoZBofPplVh-XIKKybdA1FYisYlbojtzlYdC8mBuCP7-NfC3y_zS14MoDp1rg0m3RJhV3aeIB6gJNGNldETFwfwhlH36L7sb_D_FkTjsqRcMhpOfWWguEZeWi9kwrv1Nk2w3iu_-ApydOkVVIaKMrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=l8mK2Ed_4gEn0nOh33yhGp7f0CnWXAtPnVNb46HayINuMXGSs2_mWwdbW9ZVsPZyuXw_wWniTFneIWHGyvtlQ-y2BANQHRA9VdPCH0StHd3oshOsBvscGfCyXNI4aKrvqxwCZX_yUHb1kGwl7zWXBHVpLQmsOrKe0HsqRZXcP5cj9TBinNZ_5ESa1IL77l2nMsBNoKKYN596rZPoUPQCU3lN54oSsm8f5nd5REsLW9pflDlbJ_mI5hgwiSf1TrCPw2gIKSyzN3mbMmeCt-MyFyXq0qQ924-LlGZEwsnO-AAfgmIQ2_UL_q6ojp-6byZDRTzWbQxQi0q1JxOPcStrPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=l8mK2Ed_4gEn0nOh33yhGp7f0CnWXAtPnVNb46HayINuMXGSs2_mWwdbW9ZVsPZyuXw_wWniTFneIWHGyvtlQ-y2BANQHRA9VdPCH0StHd3oshOsBvscGfCyXNI4aKrvqxwCZX_yUHb1kGwl7zWXBHVpLQmsOrKe0HsqRZXcP5cj9TBinNZ_5ESa1IL77l2nMsBNoKKYN596rZPoUPQCU3lN54oSsm8f5nd5REsLW9pflDlbJ_mI5hgwiSf1TrCPw2gIKSyzN3mbMmeCt-MyFyXq0qQ924-LlGZEwsnO-AAfgmIQ2_UL_q6ojp-6byZDRTzWbQxQi0q1JxOPcStrPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTzAUBT4u5vQtLdCRAJGEmInPiHgWCE18BRQj9hWft6LONeorL-tZGlLjJyhwG9mVFESgwA61dyVTqqaPlKTKPlhm1-a6fJoSuB5zHvpRWucDUQPKcYsKUhavsAy7DWm5_t21Y5iyJ4sbVGWuJSQCp1rVt1abBvrUDJPOE2k7mRPtFD_Ze7vJrMXOJvmY6PMvJlYPpIFyE0RT05WLlBZvT-FWYVmGRhkwQZzWGw7d_5YK-E7t68f6NPYWmIAYooudBLTe8CsIbttvh-s509GkcbgyZPUsGLW_tT_i9IAAL0UzeKind9c2VRs79m6VKhVDT-xpddTuqjhPmoEY5X29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=SCCZRrQoOiNUMcGNkjyl00X_Xbr6tCJDwJeYbQKHvnbAqfkOyxGuZrQLnyPqlbQ_pA5BvGRzJBq6eB1UcvUOHe-FoQ3tCZRhnoo82DWA4n65yuh9V1y6pviF7S9HoMlD707SZXvNb3EIR9KKlnDpYjQ_Dt6E5s6EEf59YrDahYDL9X_0h0uhogin88yH31dHmZ5P_yK4F-vUVeRzZW9o0gMr-8oaJcslfiz58QexemhBpLE16fj1oOkBPazSm2E640JNHjarNN4LtpaFhR3qK9z29aVozSsVKQj0xfcl0nyai3jk1XP4vRAzDk6xVjwgeaBdJ8uCMRd0s_I9RinqRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=SCCZRrQoOiNUMcGNkjyl00X_Xbr6tCJDwJeYbQKHvnbAqfkOyxGuZrQLnyPqlbQ_pA5BvGRzJBq6eB1UcvUOHe-FoQ3tCZRhnoo82DWA4n65yuh9V1y6pviF7S9HoMlD707SZXvNb3EIR9KKlnDpYjQ_Dt6E5s6EEf59YrDahYDL9X_0h0uhogin88yH31dHmZ5P_yK4F-vUVeRzZW9o0gMr-8oaJcslfiz58QexemhBpLE16fj1oOkBPazSm2E640JNHjarNN4LtpaFhR3qK9z29aVozSsVKQj0xfcl0nyai3jk1XP4vRAzDk6xVjwgeaBdJ8uCMRd0s_I9RinqRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک پروژه متن‌باز جذاب برای ساخت ارائه با کمک هوش مصنوعی!
دیگه لازم نیست ساعت‌ها برای ساخت اسلاید وقت بذارید؛ این ابزار رو می‌تونید روی سیستم خودتون اجرا کنید و با هر مدل هوش مصنوعی دلخواه، پرزنت حرفه‌ای بسازید.
✨
ویژگی‌ها:
🔹
پشتیبانی از OpenAI، Gemini، Claude، Ollama و مدل‌های دیگه
🔹
ساخت ارائه از روی متن، فایل و اسناد
🔹
قالب‌ها و تم‌های قابل شخصی‌سازی
🔹
اجرای کامل روی سیستم شخصی
🔹
رایگان و متن‌باز
🎓
مناسب دانشجوها، مدرس‌ها، پژوهشگرها و هر کسی که زیاد ارائه می‌سازه.
🔗
Github
#OpenSource
#AI
#Presentation
#Productivity
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌍
افزونه Local Translator
؛
افزونه‌ای متن‌باز برای ترجمه صفحات وب بدون ارسال داده‌ها به سرورهای خارجی.
💡
اگر دنبال جایگزینی سبک و خصوصی برای مترجم‌های آنلاین هستید، ارزش امتحان کردن را دارد.
🔹
ترجمه کامل صفحات یا بخش‌های انتخابی متن
🔹
استفاده از Translation API داخلی Chrome
🔹
حفظ حریم خصوصی؛ پردازش روی دستگاه کاربر
🔹
دو حالت نمایش: جایگزینی متن یا نمایش ترجمه زیر متن اصلی
🔹
ذخیره خودکار تنظیمات و فعال‌سازی خودکار
📎
GitHub
#Chrome
#Translation
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
