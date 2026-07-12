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
<img src="https://cdn4.telesco.pe/file/UDUjZCxEYhgiYZMUeWG8W-S_ysJIOgaIXakVCKpCIOTmV-qFNsYVBytL7mRsskgJyI6ZZZKWGQUhauM8ajkzKqyeYFJY-GJHCDy9dLezbJqh8CkOYJQTN3HwEcIWwI6eVNbVMoE9cFr7--dfRaszgJGnGN-ha5gfIclv7oscYFjk0Ro3YwPMp65iirTc6pDUUukR9w9F3--lWDfZjYONs3YP18e58HfLRUlI0LvKU7RNs7ltAmPT1tO_X2VwBH5Hyj0Ph0uYYDwaBDN8lZiRl60VL_k8bIDtzTIwgN9GxM61kNs4VEaEBKB-S912pIFwKG8x2XC-HVcqwrZCNS710g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.8K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 15:41:54</div>
<hr>

<div class="tg-post" id="msg-6902">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMjKL7PgPzqklZvwhP-bOWLX6hawxrJ2tbUVpcd3e7IxXFNbV27RWkchDdesYp00VZ-FLWQOyPTMhvyH5TJiZ5P-OSKFYCZ8wNZYQrQYKJqd9T4mTnxpxCdakW2L5XJPGQt3tKtonC_U3E2BySuun2tgw7uS6WB5C1yO7gqc46Ht9ksLK13ASqmGjtIuNs4KZrIM3s5BS1wpc4RZCZdxMi9OnOUvojIIiU8esLiF6UnmZdmkzTqwvs9jLzlyNWwWQEBLn3h85Cg9RmLDl9Lpm7Gdrz-AGXvEAHdZxm1khJAZMYR9qNeLsp2M349Y6_u0LXTI1Hn7DvRxJ0beRPXZwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
معرفی ‌Gitea⁩؛ جایگزینِ سبک و قدرتمندِ ‌GitHub⁩ برای میزبانیِ شخصی!
🛠
‏با ‌Gitea⁩ می‌توانید در عرض چند دقیقه، سرویسِ گیتِ اختصاصی خودتان را راه‌اندازی کنید. این پلتفرم با وجودِ سادگی، بسیار منعطف است و اجازه می‌دهد به راحتی پروژه‌هایتان را از ‌GitHub⁩ یا ‌Bitbucket⁩ به محیطِ امنِ خودتان منتقل کنید.
‏
✨
ویژگی‌ها:
‏‌
🔹
فوق‌العاده سبک: یک باینریِ واحد که حتی روی سخت‌افزارهای محدود هم کار می‌کند.
‏‌
🔹
سازگاری کامل: پشتیبانی از ‌GitHub Actions⁩ برای اتوماسیونِ حرفه‌ای.
‏‌
🔹
نصبِ سریع: راه‌اندازیِ بی‌دردسر از طریق ‌Docker⁩ و پشتیبانی از دیتابیس‌های مختلف.
🔹
همه‌کاره: شاملِ مدیریتِ تسک‌ها، ویکی، رجیستریِ پکیج و ابزارهای ‌CI/CD⁩.
لینک گیت هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 525 · <a href="https://t.me/ArchiveTell/6902" target="_blank">📅 14:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6901">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjREPYIhigO-RJE-qF5ehNvValeawG40_nGn4ng3F17YBe7HhVXBDByXb6m2Ls8qcQ4KRrnEN00ZKLncYGGcu-qcFEd57vG14HEqpEINN8xkxa4GwuRaKvLlw9YYyuiAWlDGcLQJqRy08-YgwpcbJdz22Zm38ISsDT0G_Bdh9JRdoAMvLTxYZBfZFtJQieXt4dlV_YpsNgQlGIIoRFP8Co6s_FylR-PsaZZdM5_6aHO3Yzkcg6mh3S5x_QDWk5FS4DpqoPn58RmOzHrXe9UG_R__cTT9DphuK6RgT9rQd3YmLuSX2gi6WTBLIbp1SCSyvruolL7NYUdMaFngSisQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📁
فایل منیجر قدرتمند Fast File Explorer؛ جایگزین قاتل برای Windows Explorer!
اگر از کندی سرچ فایل‌ها در ویندوز خسته شده‌اید، این ابزار سریع‌ترین روش برای پیدا کردن فایل‌هاست.
🔥
ویژگی‌های مهم:
🔍
سرعت استثنایی:
سرچ فوق‌سریع که فایل‌ها را در چند ثانیه پیدا می‌کند (بسیار سریع‌تر از جستجوی پیش‌فرض ویندوز).
🌐
امکانات شبکه و امنیت:
اتصال مستقیم به سرورهای ریموت و بررسی سلامت داده‌ها با هش‌های MD5 و SHA.
👁
پیش‌نمایش در لحظه:
نمایش محتوای فایل‌ها و داکیومنت‌ها مستقیماً داخل رابط کاربری برنامه، بدون نیاز به باز کردن آن‌ها.
🖥
چندپلتفرمی:
کاملاً رایگان و قابل اجرا روی ویندوز، لینوکس و مک.
🔗
[
لینک دانلود
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/ArchiveTell/6901" target="_blank">📅 13:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6900">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یه توضیحی که مدت‌ها تو دلم مونده بود
راستش قصد نداشتم وارد حاشیه بشم، ولی بعضی چیزها وقتی گفته نشن، فقط آدم رو اذیت می‌کنن. حس کردم بهتره تجربه‌ی خودم رو بگم تا بقیه هم در جریان باشن.
ادمین
نتلیفای
و
زئوس
در واقع دوست ما بود...
زمانی که هنوز کانالی نداشت، عضو کانال ما بود. ادمینش بود. از کارهاش حمایت کردیم، پروژه‌هاش رو معرفی کردیم، کانفیگ در اختیارش گذاشتیم و هر جا تونستیم کمکش کردیم. حتی وقتی کانال خودش رو راه انداخت، پست‌هاش رو تو همین کانال فوروارد می‌کرد و طبیعتاً بخشی از ممبرها هم به سمت کانالش رفتن. بابت زحمتی که برای پروژه‌هاش کشید همیشه براش احترام قائل بودم.
اما چیزی که ناراحتم کرد، این بود که این حمایت هیچ‌وقت دوطرفه نبود.
- برای راحت‌تر شدن کار کاربران، با کمک یک دولوپر اپلیکیشن نتلیفای رو ساختیم، اما حتی حاضر نشد نصبش کنه و از همون اول گفت «اپ به چه درد می‌خوره؟» در حالی که هدف فقط ساده‌تر شدن استفاده برای کاربرها بود.
- بعداً یکی از دوستان، یک فورک تمیز و کامل از کانفیگ‌جنریتورش منتشر کرد. درخواست شد داخل کانالش معرفی کنه، اما قبول نکرد. در نهایت خودم اون پروژه رو توی کانال معرفی کردم.
- خودم هم چند بار پروژه‌ش رو فورک کردم و قابلیت‌هایی بهش اضافه کردم و تو توضیحات ازش قدردانی کردم اما برخوردش بیشتر تمسخر و بی‌اهمیتی بود. در حالی که پروژه
Open Source
بود. اگر قرار نیست کسی مشارکت کنه، خب می‌شد پروژه رو کلوزسورس نگه داشت.
- آخرین مورد هم مربوط به اسکنر IP بود. برای معرفی پروژه بهش پیام دادم، اما انقدر برخوردش سرد و آزاردهنده بود که واقعاً حالم گرفته شد. یه بار گفت «مطلب مرتبط نیست»، یه بار گفت «تبلیغ نمی‌کنم». در حالی که این ابزار به نظرم برای جامعه کاربری مفید بود و صرفاً برای کمک به اکوسیستم ساخته شده بود، نه تبلیغات شخصی.
چیزی که برام عجیبه اینه که از همه انتظار حمایت برای مطرح شدن پنل و پروژه‌هاش وجود داره، اما وقتی نوبت به حمایت از دیگران می‌رسه، اون نگاه دیده نمی‌شه.
این متن برای تخریب کسی نیست؛ فقط تجربه شخصی من از همکاری و حمایتیه که انتظار داشتم متقابل باشه، اما نبود...</div>
<div class="tg-footer">👁️ 715 · <a href="https://t.me/ArchiveTell/6900" target="_blank">📅 13:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6892">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FK9v3DqcvcMVZwcAfG212xd1TIKg5oowW-ngVZAl_9kgBUpHVn0uA3sDV1KPCOEP9rrjcGMTUek_SI5Lf7FyeHZU11hYLibGA4w46Rc-OJ151_TWdI3lFGM14YhHsYayWjROs_dyAKHEncAxsydsJF__57GyYLeGcOF1qa8oN_JOZGfcxzuOhSM4JLjZlQ2653lDhleQDSVf-HNJNNqZABn4IAm1hS9yBi3Jy3t1M0WQrGKYW9908d36x2PjQPnEeewofnYH4m5YBzr8KbpMv_IVmbcwxm5iHYRh12kaaA_RoBd239yjkBPY7u006x0T9Q7FR7_RN4Y3Uxwz7U82dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dljmThUnFhE9oeh-MofW5q545fy2l8gAIXL3sBfM2RxMSfGOqrKxqk6nTYaEhEJLuGv9KxQAQJBJxiyPlCYugns64hJEziCg9eFJIaHSan97U4fKiUH91Ifdxmbvmz5jQiMcVOdXHDQLi22wpasXGqGWhjCWI1IngUvjGkg4fyBGzeP-fXbFMO5zpUuP7mWPcYQbblUp0JRHU2IgIIPliY2h9e3BYeNcfla5bNSfouGHnt0tra6BCGYgP4sHGq5fvwRnHn-g1kTDKM39sjZaaHrGgnZkX_LrxGjqEWFoMHc6VZiOmgtRuSUtOBbN8uxRB1bKgolu92GFPkJ51BtHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O21hzphQQVnMVLVm-R8OMMsL7C7rhv5dRrwWSdPM7sxo3QiHp4gJBDk4gjAnEpY9tYfdgDyJQYG_cSt7UqKphvlANMRDD_Zzr8A6zU11y72ibwJoeAwuX9Et5a4hfpBw7zPb8mg85ATjjLdFWIbOc5tw_RFNMlZeC7kJMeOQ8yShLb2K3p2yLK8kJOY9h6WsDYMpO2tOJHbxAQmPuWxlxD27Y5MpWIOSjhXZGvI0939fC3ybe6JtqnDLuRfRz8xetgxhY_huV2UokJfzDRuPLPOF8dLiv9RcCgPErNj1nxiUqtS8Wt49P6QsvXmFI9yqwvmiIJRjP4E2mu922jlbZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/se8dR5BjGaGdXDwJV6qKIGhX-mVu6UhOhGuoenQCp1nZzo4nHhkqd4VJ27ENUXqZxo42sOL54-v71A9A2091v06qRNVleNZ1Jiz3MvfMp9JTddycCsFkP_XErXoh7dMr2kkue5AOfreQjkicQu1j_b1mGubVhpN7_1_cxCk1brDNyTHLDnSaSE9oCcsAaPfkWl5QFey__G7TcfDY_lLuV7FTL84I4EFqElc9Hhae2heVWjJlIV3LhhcoebZZFahYtTkemCCB6AXPmuetvzqSfSi_wry9eNpGaCMYhcXWUyvBvgYZ7Kong5j5v415Kt88hCiymwGebVe7m4r8SKD2gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/ArchiveTell/6892" target="_blank">📅 13:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6887">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سایت‌های Torrent برای دانلود مدل‌های LLM
1.
https://ckpt.cc/
2.
https://huggingbay.xyz/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/ArchiveTell/6887" target="_blank">📅 12:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6886">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏
🚀
معرفی ‌VoiceTypr⁩؛ تایپ صوتیِ هوشمند و کاملاً آفلاین!
🎙
✨
( از زبان فارسی پشتیبانی میکنه )
‏این ابزارِ فوق‌العاده دقیقاً مثل یک دستیارِ شخصی روی سیستم‌عاملِ شما عمل می‌کنه، کافیه دکمه‌ی میانبر رو بزنید و شروع به صحبت کنید تا متن‌تون دقیقاً همون‌جایی که نشانگرِ موس هست، ظاهر بشه.
‏
🔥
ویژگی‌ها:
🔹
حریم خصوصی مطلق: پردازش‌ها کاملاً آفلاین انجام می‌شه و هیچ داده‌ای از سیستم شما خارج نمی‌شه.
‏‌
🔹
سرعتِ بی‌نظیر: به لطفِ بهینه‌سازی‌های سخت‌افزاری، حتی روی سیستم‌های معمولی هم مثل برق و باد کار می‌کنه.
🔹
‏ پشتیبانی گسترده: بیش از ۹۹ زبانِ مختلف رو پوشش می‌ده تا هیچ محدودیتی نداشته باشید.( شامل زبان فارسی)
🔹
‏ یکپارچگی عالی: قابلیتِ درجِ مستقیمِ متن در هر نرم‌افزاری که باهاش کار می‌کنید.
گیت هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/ArchiveTell/6886" target="_blank">📅 11:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6885">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🛡️
؛ungoogled-chromium؛ کرومیوم بدون وابستگی‌های گوگل
اگر به دنبال یک مرورگر سریع، سبک و نزدیک به تجربه اصلی Chromium هستید اما نمی‌خواهید ارتباطات غیرضروری با سرویس‌های گوگل داشته باشید، ungoogled-chromium یکی از گزینه‌های جذاب است.
✨
ویژگی‌های مهم:
🔹
حذف وابستگی‌ها و سرویس‌های اختصاصی گوگل
🔹
کاهش درخواست‌های پس‌زمینه به دامنه‌های گوگل
🔹
حذف کدهای مربوط به سرویس‌های گوگل
🔹
تمرکز بیشتر روی حریم خصوصی، شفافیت و کنترل کاربر
🔹
حفظ ظاهر و تجربه نزدیک به Chromium اصلی
🔹
امکان شخصی‌سازی بیشتر با فلگ‌ها و تنظیمات اضافی
این پروژه در واقع همان Chromium است، اما با تغییراتی برای کسانی که می‌خواهند کنترل بیشتری روی مرورگر خود داشته باشند.
📌
مناسب برای:
✅
کاربران علاقه‌مند به حریم خصوصی
✅
کسانی که مرورگر سبک و بدون سرویس‌های اضافی می‌خواهند
✅
کاربران لینوکس، ویندوز و macOS که دنبال جایگزین Chromium هستند
🔗
پروژه متن‌باز
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 978 · <a href="https://t.me/ArchiveTell/6885" target="_blank">📅 11:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
؛Archive Scanner v1.0.3 منتشر شد!  جدیدترین نسخه‌ی Archive Scanner با بهبودهای مهم در دقت، سرعت و امکانات منتشر شده است.
✨
تغییرات مهم:
⚡️
اصلاح کامل تست سرعت دانلود (اندازه‌گیری دقیق‌تر و عبور از فیلترینگ SNI)
📤
اضافه شدن تست سرعت آپلود برای هر IP
🤖
ساخت…</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/ArchiveTell/6884" target="_blank">📅 11:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6883">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ایپی تمیز کلودفلر
مخابرات
104.19.2.34
104.18.135.100
172.67.80.2
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/ArchiveTell/6883" target="_blank">📅 11:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6881">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شاید من ی مدتی دور باشم
بقیه دوستان هستند
حالم این روزا، حال خوبی نیست
💔
مثل حال عقاب بی‌پرواز</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6881" target="_blank">📅 00:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6880">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
آموزش کامل SillyTavern + اتصال API شخصی + استفاده از شخصیت‌های آماده سلام رفقا!
👋
اگر API شخصی داری (مثل OpenRouter، OpenAI، Groq، DeepSeek یا هر سرویس OpenAI-Compatible)، با SillyTavern می‌تونی از شخصیت‌های آماده استفاده کنی و تجربه‌ای بسیار حرفه‌ای‌تر…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6880" target="_blank">📅 23:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6879">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
آموزش کامل SillyTavern + اتصال API شخصی + استفاده از شخصیت‌های آماده
سلام رفقا!
👋
اگر API شخصی داری (مثل OpenRouter، OpenAI، Groq، DeepSeek یا هر سرویس OpenAI-Compatible)، با
SillyTavern
می‌تونی از شخصیت‌های آماده استفاده کنی و تجربه‌ای بسیار حرفه‌ای‌تر از بسیاری از سرویس‌های چت هوش مصنوعی داشته باشی.
🚀
۱) نصب SillyTavern
۱.
آخرین نسخه
Node.js LTS
را نصب کنید.
۲.
آخرین نسخه SillyTavern را از صفحه Releases دریافت کنید:
https://github.com/SillyTavern/SillyTavern/releases
۳.
فایل را استخراج کنید.
۴.
فایل
Start.bat
را اجرا کنید.
۵.
مرورگر به‌صورت خودکار باز می‌شود. اگر نشد، این آدرس را باز کنید:
http://localhost:8000
👤
۲) دانلود شخصیت‌های آماده
یکی از بهترین منابع کارت شخصیت:
https://chub.ai
می‌توانید عباراتی مثل این‌ها را جستجو کنید:
girlfriend
romance
friend
assistant
waifu
anime
fantasy
کارت دلخواه را دانلود کنید.
کارت‌های شخصیت شامل اطلاعاتی مثل شخصیت، پیام آغازین، نمونه مکالمه و تنظیمات نقش‌آفرینی هستند.
📥
۳) وارد کردن کارت به SillyTavern
وارد بخش
Characters
شوید.
روی
Import Character
کلیک کنید.
فایل PNG یا JSON کارت را انتخاب کنید.
یا فایل را مستقیماً داخل برنامه Drag & Drop کنید.
🔌
۴) اتصال API شخصی
از منوی
API Connections
وارد تنظیمات شوید.
تنظیمات:
API Type
Chat Completion
Source
OpenAI Compatible
سپس اطلاعات API خود را وارد کنید.
نمونه Base URL:
OpenRouter
https://openrouter.ai/api/v1
OpenAI
https://api.openai.com/v1
Groq
https://api.groq.com/openai/v1
DeepSeek
https://api.deepseek.com/v1
سپس:
API Key
مدل (Model)
را وارد کرده و روی
Connect
بزنید.
اگر اتصال سبز شد، همه چیز آماده است.
💬
۵) شروع گفتگو
شخصیت موردنظر را انتخاب کنید و گفتگو را آغاز کنید.
کیفیت پاسخ‌ها بیشتر به
مدل هوش مصنوعی
و
کیفیت کارت شخصیت
بستگی دارد، نه خود SillyTavern.
⚙️
تنظیمات پیشنهادی
Temperature:
0.8 - 1.0
Context Size:
تا جای ممکن بیشتر (در صورت پشتیبانی مدل)
Streaming:
روشن
System Prompt:
متناسب با کاربرد خود تنظیم کنید.
💡
نکات
✅
از کارت‌های با دانلود و امتیاز بالا استفاده کنید.
✅
هر API سازگار با استاندارد
OpenAI-Compatible
معمولاً در SillyTavern قابل استفاده است.
✅
مدل‌های مختلف رفتار متفاوتی دارند؛ چند مدل را امتحان کنید تا بهترین نتیجه را بگیرید.(ممکنه یه مدل اصن جواب نده!)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6879" target="_blank">📅 23:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6878">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✨
وگا — دستیار هوش مصنوعی تلگرام
قدرتمندترین ربات هوش مصنوعی فارسی، برای پیوی، گروه و کانال شما!
🚀
━━━━━━━━━━━━━━
🧠
مدل‌های هوش مصنوعی
از بین قوی‌ترین مدل‌های دنیا، مدل دلخواهت رو برای چت انتخاب کن:
-
🧠
Claude Opus 4.8
-
🔮
Claude Sonnet 4.6
-
🐋
Deepseek 4 Pro
-
🐉
Qwen 3.6
-
💎
GLM 5.2
-
🍃
Gemma 4
-
🦙
Llama 4
-
🚀
GPT-4
-
🧬
Minimax M3
-
🐬
Mimo 2.5
━━━━━━━━━━━━━━
📢
فعال‌سازی در کانال شما
وگا رو زیر پست‌های کانالت فعال کن! کافیه ربات در کانال و گپ متصل به آن ادمین بشه تا زیر هر پست، کامنتی کوتاه و جذاب بذاره — دقیقاً مثل کانال آرشیو تل.
🔍
جستجوی زندهٔ وب
پاسخ‌های به‌روز و دقیق، برگرفته از جدیدترین منابع اینترنتی.
🔗
خواندن لینک‌ها و مخازن گیت‌هاب
لینک بفرست تا محتوای صفحه رو بخونه؛ ریپازیتوری‌های GitHub رو هم مستقیم آنالیز می‌کنه.
📦
👁
تحلیل عکس، ویدیو و PDF
عکس، ویدیو، فایل PDF و فایل صوتی رو می‌بینه، می‌شنوه و به‌طور کامل تحلیل می‌کنه.
━━━━━━━━━━━━━━
📰
اخبار روز
گزیده‌ای از تازه‌ترین اخبار در سه دسته: سیاسی ,  ورزشی , تکنولوژی — با به‌روزرسانی 5 ساعته.
🧮
حل سوالات درسی و علمی
سوال درسی یا علمیت رو به‌صورت متن یا عکس بفرست وگا با استفاده از به‌روزترین منابع، پاسخی کوتاه، دقیق و کامل می‌ده.
❄️
قیمت لحظه‌ای ارز و طلا
قیمت زنده رو در لحظه با نمایش اخرین تغییرات در روز بگیر
━━━━━━━━━━━━━━
📚
وگا ویکی
دستیاری هوشمند برای پرسش‌وپاسخ: سوال‌های عمومی رو خودش جواب می‌ده و برای موضوعات دانشنامه‌ای مقالهٔ مرتبط از ویکی‌پدیای فارسی رو پیدا و بررسی می‌کنه و بر اساس اون پاسخ می‌ده و لینک مقاله رو هم می‌پذیره.
👨‍💻
وگا کد
ابزاری حرفه‌ای برای کدنویسی، مجهز به مدل‌های GLM 5.2، Deepseek 4 Pro و Minimax M3.
همچنین:
🎨
ساخت عکس
🎙
ویس‌چت
🔤
تبدیل صدا به متن و برعکس
🌐
ترجمه به هر زبان
━━━━━━━━━━━━━━
📢
@ArchiveTell
-
@VegaEnter</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6878" target="_blank">📅 22:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6876">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5uzdfP6sTjm-eNXJaqgk2v5HNCXJta-QWhVsKI08GO9rLi-FyEKKmkIMIvK_T70L9nam-O3fjbDUcXMk949wGJNiD6OAZmf-lVk4ei6EIKRyIk6K3gMH5IN1jxRq2nk8q3TrOwmX51Ppq7wWDf4_rY7qXFFFvCgGaaPByrsNcZRZONmlMLmDo3ustQ-DfDuRLZLkE5R1WNRHFlDu7UIEvXDZPMy4GmCPaewjqEsyn7H9j6ZyjcbNnKIpVcSGifU2_RlZA0aB0ZUWcdWtOWwO1cu_e4-FiVTtVIv8OIeaUY-O-xbQelsCnjBXMBqJsqhKlBiwDoCSsKq9lMzl0R59g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77ed13056.mp4?token=n6uHo9ii2zMZU1UCmAdwlEjmDUvQbq5E-zs-S4ZiKR0oV-U0ClDO_QK42WsQ7znLCLD-Pan3MmKBMrl5kED9o_RDAgYOQp4gFy2g6Ov-0GkXKqegdlIhFnl0SNLc5h_e_5ruj1uxFBQLhQgGqvwPW5Xe-kOisl9y1DEOohec3YfPDloq7siIFAYjp65JGaJ92mmkiPGTz43u-HUtmxgta3gLaMMVhYJiDmAt7eVsGwuN8CtOFzyWZFlFsuwVpCD8wh9KG3ebiVFVCPjw2JXejFQnrN6_bsP2W_7vI72bEHquH32gRa6T0UkN9m9xro4MaIKcVkc5IX0YgTSlE75QCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77ed13056.mp4?token=n6uHo9ii2zMZU1UCmAdwlEjmDUvQbq5E-zs-S4ZiKR0oV-U0ClDO_QK42WsQ7znLCLD-Pan3MmKBMrl5kED9o_RDAgYOQp4gFy2g6Ov-0GkXKqegdlIhFnl0SNLc5h_e_5ruj1uxFBQLhQgGqvwPW5Xe-kOisl9y1DEOohec3YfPDloq7siIFAYjp65JGaJ92mmkiPGTz43u-HUtmxgta3gLaMMVhYJiDmAt7eVsGwuN8CtOFzyWZFlFsuwVpCD8wh9KG3ebiVFVCPjw2JXejFQnrN6_bsP2W_7vI72bEHquH32gRa6T0UkN9m9xro4MaIKcVkc5IX0YgTSlE75QCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی Hugging Bay؛ دنیای مدل‌های هوش مصنوعی، یک‌جا کنار هم!
🏴‍☠️
✨
دنبال یه مدل AI خاص برای پروژه‌ات هستی ولی بین صدها مخزن و لینک مختلف گم میشی؟ پیدا کردن بهترین LLM، مدل ویدیویی یا حتی Agent مناسب واقعاً می‌تونه وقت‌گیر باشه.
؛Hugging Bay مثل یه Torrent Tracker برای دنیای هوش مصنوعیه که انواع مدل‌های اوپن سورس و حتی مدل‌های منتشرشده رو یکجا جمع کرده. جذاب‌ترین بخشش هم جستجوی هوشمنده؛ فقط نیازت رو به زبان طبیعی بنویس تا بهترین مدل رو بهت پیشنهاد بده.
🔥
ویژگی‌ها:
1️⃣
جستجوی هوشمند: پیدا کردن مدل‌ها با زبان طبیعی مثل «بهترین Embedding Model برای RAG».
2️⃣
آرشیو کامل: دسترسی به LLMها، مدل های ویدئو و صدا و AI Agents در یک مکان.
3️⃣
؛Semantic Re-ranking: نتایج جستجو بر اساس مفهوم و کیفیت، نه فقط کلمات کلیدی.
4️⃣
مناسب توسعه‌دهنده‌ها: پیدا کردن سریع مدل مناسب برای پروژه‌های تجاری یا شخصی.
5️⃣
؛Open-Source Friendly: مرجع جذاب برای کشف و دانلود مدل‌های متن‌باز.
🔗
https://huggingbay.xyz/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6876" target="_blank">📅 21:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6875">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌐
کامپیوترت رو به یک هات‌اسپات حرفه‌ای تبدیل کن!
با MyPublicWiFi می‌تونی لپ‌تاپ یا کامپیوتر ویندوزی‌ات رو به یک Wi-Fi Hotspot تبدیل کنی و اینترنت رو با موبایل، لپ‌تاپ و سایر دستگاه‌ها به اشتراک بذاری.
✨
ویژگی‌ها:
🌍
اشتراک‌گذاری اینترنت از طریق Wi-Fi، LAN، VPN، مودم USB و...
🔓
اشتراک‌گذاری اتصال VPN با دستگاه‌های متصل
👥
نمایش و مدیریت دستگاه‌های متصل
🛡️
امنیت با رمزنگاری WPA2 و فایروال داخلی
🚫
مسدودسازی سایت‌ها، سرویس‌ها و برنامه‌های خاص
📶
مدیریت پهنای باند، فیلتر تبلیغات و جلوگیری از Torrent
🏨
ساخت صفحه ورود (Captive Portal) مانند هتل‌ها و کافی‌شاپ‌ها
⚡
اجرای خودکار هات‌اسپات پس از روشن شدن ویندوز
💡
یک ابزار رایگان، سبک و کاربردی برای خانه، محل کار، دانشگاه و سفر.
🔗
دانلود:
https://mypublicwifi.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6875" target="_blank">📅 20:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6874">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">100 گیگابایت از خیر گرامی
😛
❤️
محمدامین
vless://86cf09aa-80b7-431f-a1eb-7b95c2b8f122@amin.sylixteam.ir:8443?encryption=none&extra=%7B%22mode%22%3A%22auto%22%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22xmux%22%3A%7B%22cMaxReuseTimes%22%3A0%2C%22hKeepAlivePeriod%22%3A30%2C%22hMaxRequestTimes%22%3A%222000-2300%22%2C%22hMaxReusableSecs%22%3A%221800-3000%22%2C%22maxConnections%22%3A%2216%22%7D%7D&fp=chrome&host=amin.sylixteam.ir&mode=auto&path=%2Fccc&pbk=v6EuCPV1jYoSkTYuZ3G98xQE_DECYRvaBKZslRWgLCI&security=reality&sid=6ce858de1459bfe5&sni=www.samsung.com&spx=%2FQf36mL3kluzRLYn&type=xhttp&x_padding_bytes=100-1000#Download-Free-100GB
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6874" target="_blank">📅 20:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6873">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این قسمت Fragment تو برنامه V2rayng و... رو ور برین بهتر میشه اینترنت
در کل ریده شده
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6873" target="_blank">📅 20:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6871">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtl_VLNjDtgUlWMzYXX37Z0GAbJa3yfFAFjLvF5gF4ir9qCf6XOg3V75K1DrKWwKWTX0jzsl4NRPdwDJBciAkcZuHNzGwmfrcK9uje91qLR7Edt5yUgW8sPWCMKnzw8rz4Iv3PnsE4Tub7xDAh5vr0aJaDWoBc3XVxMSLHd06lKTi-FFh4Ay5I5fXWOuOXRqHsyBo4FoyYjpU2ClSL8gF1oDzNYgko4hkqzSelRQQ9H3UHRxLx9ioFgp_nMbmYB_rFoYiqT-GNpBDKWiRe01-5GUJ7nndOj2r4neoK8UwUQ6LwIlraP24r28kHs883gHkSU3bPOWjLqfrEtHwxYrLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📚
معرفی ‌CheatReader⁩؛ دستیار مطالعه در محیط کار!
🤫
📖
‏‌CheatReader⁩ یک ابزار عالی برای مطالعه در محیط کار است. با استفاده از این ابزار، می‌توانید کتاب یا رمان مورد علاقه‌تان را در یک پنجره شناور در گوشه دسکتاپ پین کنید و همزمان به کارهای اصلی‌تان برسید.
‏
🔥
ویژگی‌ها:
‏‌1⁩️⃣ پنجره شناور برای مطالعه در محیط کار
‏‌2⁩️⃣ حالت‌های متنوع مطالعه، از جمله حالت شفاف و نمایش تک‌خطی
‏‌3⁩️⃣ پشتیبانی از فرمت‌های مختلف، از جمله ‌TXT⁩، ‌EPUB⁩، ‌PDF⁩، ‌DOCX⁩ و غیره
‏‌4⁩️⃣ شخصی‌سازی، از جمله تنظیم فونت و جستجوی متن
‏
⚙️
مشخصات:
‏• پلتفرم: ویندوز، مک، لینوکس
‏• منبع: رایگان و متن‌باز
‏
🔗
لینک پروژه: ‌
http://github.com/yaoyao2mm/cheatreader
⁩
──────────────────────────────
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6871" target="_blank">📅 17:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6870">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxWlGYFJ-NC0rJBtvXJ0E1BF_Va9JXLBGOwkKEENtyo-hctAW2MbG2kzNz2kjVxB5CbMu4uiUuFdxcduzIXUNJN5BIWGrOvshrVmK2mfMNaq_Px5tDD9Tkkdaq1Dl2OvsGkgW2plkdf4C3LT65L-KUST-tvOedx-z2vEbB0Qhs0W52U_v3ilh6xjzafZho7e7X5RsZtdTEdVOAZ3npr6MhxaPBrXmFqHii1f5wcPN65l5_aMpNa9ZBkaXuUVEXWzSGWv7FKuoKEYRHDzmOTV_gXecsR6vo8Y-8i8rGdAh1SaY4AA7NGgHgQInsVM6KNOs9C8hpEPdKsd8FA7Yg4mBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡️
فورت (Fort)
🔥
یک فایروال (Firewall) قدرتمند و متن‌باز برای سیستم‌عامل ویندوز است که با کنترل ترافیک ورودی و خروجی شبکه، امنیت سیستم را افزایش می‌دهد.
✨
امکانات کلیدی:
🔹
کنترل و فیلتر کردن ترافیک شبکه برای برنامه‌ها و سرویس‌های مختلف
🔹
ایجاد و مدیریت قوانین اختصاصی برای دسترسی برنامه‌ها به اینترنت
🔹
مانیتورینگ لحظه‌ای فعالیت‌های شبکه و نمایش جزئیات اتصالات
🔹
سبک، رایگان و دارای رابط کاربری ساده
🔗
https://github.com/tnodir/fort
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6870" target="_blank">📅 16:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6868">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎬
آرشیو رایگان فیلم و سریال بدون سانسور
اگر دنبال یک مرجع برای تماشا و دانلود فیلم و سریال هستید،
PunkMovie
یکی از گزینه‌های خوب است.
✅
ویژگی‌ها: • آرشیو بزرگ از فیلم و سریال‌های خارجی • نسخه‌های
بدون سانسور
• به‌روزرسانی سریع با انتشار قسمت‌ها و فیلم‌های جدید • امکان تماشای آنلاین و دانلود • اپلیکیشن اختصاصی اندروید
🔗
لینک:
https://punkmovie.top
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6868" target="_blank">📅 15:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6867">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚡️
آپدیت Archive Scanner v1.0.1
🔧
تست سرعت دانلود درست شد (حل مشکل فیلترینگ SNI) — برای همه، بدون تنظیمات
📤
تست سرعت آپلود اضافه شد
🤖
ساخت خودکار Worker آپلود با یک کلیک (بدون نیاز به خروج از اپ)
🚀
سریع‌تر و کم‌مصرف‌تر  https://github.com/ArchiveTell/archive…</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6867" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6865">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfPE3rv-KLrUsNNjS1hdMp4JXdD4_JmTgEEkUEjfZrp41tTpAWtgovqnrSLtH41E18Rs4qdcsAiaphINdlGjh0xwSeNMIyUOOLHwRekvH_bNsYn6FljuU_0AmbQsE66_mHr3ykteJTaLuDRDBjcim2Tfju_ZeSyUviBFY9v1Of3t5VTqjIIFD4IpH0LuxCrCt-3f53st-eTatZOIQt5jIn8JPU3TETT0RiLFIkDZzvFfpw7pRBeXqqG6USWxkOB7ZVJqPp6tfnZdZnDNaLXbwpoUq3zhg_L6twVtETnAfHj0N4RautOsjTtvBYfs716NIVCkarMHxtz1Eu2xb8cn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPLtcvSp3ExlAhKeb1sNnC1jAtI0ZuZv_CrXnw7aff3qxchqK5nn8DM-rb3jl5n5yv6ORnmDxHnqVWPFcmmyqnw1bqFVVdDBnQ3UpGQ4HGhXLxleeh_hGdRr5kYg0b42UHx8g1BNuZo3l3yo7r8AKyLcFFBXQ-AMgsT-6wHHZYAAU2bnbRPIvG-rh7pbJDvZwdSRkmXOqZnuqwPhCwZ6PS73PGA27Id4r3NuURO4ffmetQ6WSZQ3cpb_ddMGTZFbsL90o-6YL6DgBj6gBBzRdY-L7d-AA55qBTvkkdCaG0rGwlRrUxKym8MvdmauYlDp1d-MUVt9olZJfPJqAnPafQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
آپدیت Archive Scanner v1.0.1
🔧
تست سرعت دانلود درست شد (حل مشکل فیلترینگ SNI) — برای همه، بدون تنظیمات
📤
تست سرعت آپلود اضافه شد
🤖
ساخت خودکار Worker آپلود با یک کلیک (بدون نیاز به خروج از اپ)
🚀
سریع‌تر و کم‌مصرف‌تر  https://github.com/ArchiveTell/archive…</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6865" target="_blank">📅 13:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6864">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6864" target="_blank">📅 13:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6863">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📡
وای‌فای؛ دوربین نامرئی آینده؟
محققان نشان داده‌اند روترهای جدید Wi-Fi با کمک هوش مصنوعی می‌توانند تغییرات امواج را تحلیل کنند و بدون نیاز به گوشی یا وسیله همراه، حضور و حتی هویت افراد را تشخیص دهند.
🧠
این فناوری برای خانه‌های هوشمند و امنیت کاربرد دارد، اما می‌تواند نگرانی‌های جدی درباره حریم خصوصی و ردیابی افراد ایجاد کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6863" target="_blank">📅 13:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6862">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9ePg1RkhdrdDMY0guAKqcI6XAAd58w8Nf_QXHrSl-yL4znEAKhjO7Zke1HBdN0mJ646UthWnM5u9HC1A1RWa89TLIVMdLnCaITsa2ovn_vBpySqe7uMHkur2Y72q526M2kxJhVvotOQtuO8bDufCq-eqYDleMI9AAwbu6dGqkQY0LuovLlCVNXHhGMcaSA9O87unq8vyhziXpnNCCC_iI6Mb3GpZt-H4ynAa4DDeyZTw38StaOvQsfqkNO4Kao8Gx-DNhrkf-0ekZIzYb5WCzQmXVXum-TR1kwFy7B9jhqe8tD6og4Xz5sA_Tx8RPj9rChUzZLxX04MsJ_tg6L_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📦
‌RepoStore⁩: فروشگاه اپلیکیشن‌های گیت‌هاب از راه رسید!
🚀
‏دیگه نیازی نیست برای پیدا کردن پروژه‌های جذاب در گیت‌هاب، ساعت‌ها در مخازن مختلف جستجو کنید.
‌RepoStore⁩
دقیقاً مثل یک پلی‌استور اختصاصی برای گیت‌هاب عمل می‌کند.
‏
🌟
چرا باید از آن استفاده کنید؟
‏•
تجربه کاربری آشنا:
محیطی مشابه فروشگاه‌های رسمی که کار با آن بسیار ساده است.
‏•
مدیریت هوشمند:
نصب و آپدیت مستقیم اپلیکیشن‌ها بدون درگیری با فایل‌های ‌APK⁩ پراکنده.
‏•
شفافیت کامل:
امتیازها و تعداد ستاره‌های گیت‌هاب مستقیماً نمایش داده می‌شوند تا بهترین ابزارها را بشناسید.
‏•
دسترسی آزاد:
کاملاً رایگان و متمرکز بر پروژه‌های متن‌باز.
🔗
https://github.com/samyak2403/RepoStore
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6862" target="_blank">📅 13:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6861">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6861" target="_blank">📅 13:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6860">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ArchiveTel
pinned «
🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6860" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6859">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Tr - infinity.npvt</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6859" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">روز خوبیو توی این دوران سخت براتون ارزو میکنم
😜
🥰
Password :
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6859" target="_blank">📅 05:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6858">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔥
دریافت API رایگان بدون ثبت‌نام! اگر برای پروژه‌ها یا ربات‌های خود به یک API رایگان نیاز دارید، این سایت می‌تواند گزینه جالبی باشد.  ؛Dahl Inference بدون نیاز به ثبت‌نام، تنها با چند کلیک یک API Key در اختیارتان قرار می‌دهد که می‌توانید از آن برای استفاده…</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6858" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6857">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔥
دریافت API رایگان بدون ثبت‌نام!
اگر برای پروژه‌ها یا ربات‌های خود به یک
API رایگان
نیاز دارید، این سایت می‌تواند گزینه جالبی باشد.
؛
Dahl Inference
بدون نیاز به ثبت‌نام، تنها با چند کلیک یک
API Key
در اختیارتان قرار می‌دهد که می‌توانید از آن برای استفاده از مدل‌های مختلف هوش مصنوعی استفاده کنید.
ویژگی‌ها:
• بدون نیاز به ساخت حساب • دریافت فوری API Key • دسترسی به مدل‌های مختلف • مناسب برای تست، توسعه و پروژه‌های شخصی
هر کلید 100 میلیون توکن رایگان میده
😁
🔗
دریافت API:
https://inference.dahl.global/chatKeys#models
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6857" target="_blank">📅 01:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6856">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">؛
🎨
Lake: اپلیکیشن آرامش‌بخش رنگ‌آمیزی برای بزرگسالان
اگر بعد از یک روز پرمشغله دنبال راهی برای استراحت و دور شدن از استرس هستید،
Lake
یکی از بهترین گزینه‌هاست.
این اپلیکیشن مجموعه بزرگی از طرح‌های رنگ‌آمیزی را که توسط هنرمندان واقعی طراحی شده‌اند در اختیارتان قرار می‌دهد. از
مناظر و طبیعت
گرفته تا
معماری، دکوراسیون، حیوانات و پرتره
، برای هر سلیقه‌ای طرحی پیدا می‌شود.
✨
امکانات: •
🖌️
صدها طرح باکیفیت •
🎯
حالت هوشمند برای جلوگیری از خروج رنگ از خطوط •
🎨
ابزارها و پالت‌های رنگ متنوع
🆓
کلی طرح رایگان برای شروع
اگر به دنبال یک سرگرمی ساده و آرامش‌بخش هستید، Lake ارزش امتحان کردن را دارد.
نکته: فعلا فقط برای آیفون در دسترسه
🔗
سایت:
https://lakecoloring.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6856" target="_blank">📅 01:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6854">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlA5myIcB9DvCdCk86uFyzC1F_yIFvlaPYc0OOMYoh_6A9m1BpbMEQpHVY3C1LCpw6XIDWXDcaHM7EGBf4KvLSLz1pi2PRf4SF59G2KzkEpie6zbKkKvKlb7bh9FI3jE0zzp6hFL5NsrRETgi0P7fA_7q7O0H0LDxz5W8gdXREdAJXzwc8LmqRqezx_IPerG9RV0KzndZ03fMihe1M5E7MGPyWpXC3E_GDS1hkWHcztpJyCk3QjK2BpBDEpTL3R106do8BL9qn3hnjfBskQpMU2eVX5cuWD1Vlgdfy6FKc1UqqoSf1BqUOmYfL5Gn0iWasUKa3ijlHeG56H2uvNZEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYRAXXK4wXFAzztkHWjSxykyRdoYN-evpRG05SS7Xs7AfBiDyszDXUrQJmFOO0ko2V3eAq88caPD27PafLwP226FzgbOLWp8iob61zuK6D9Mpe_gv71H2Rd2Us_jGLm-F8vV8IS2GnRLjgDzVs_Jxh4T-_D-l0KSigZO_cOPXoObCgITyLbO83rP5WpB663VTovdPNn0THI6TpNxL0m_0l6t6hVwgbXhEr5mzeyj31DfE136W5zTeyXuMzbAPmjhcm874VxKdMZSMvDaftAVlL7B41KhrQ-7v1XLy5eY3NaL7Q8ZBbHVvwQKorqBImF0k8xso_w-mtE2zHNJf9KYjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6854" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6853">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0
(اسکنر آیپی تمیز کلودفلر)
به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر کنم. امروز با افتخار نسخه اول
Archive Scanner
را به شما تقدیم می‌کنم.
🔥
قابلیت‌های فنی و تخصصی:
✅
اسکن پیشرفته SNI + TLS:
ما به پینگ ساده اکتفا نکردیم! با شبیه‌سازی کامل TLS Handshake، آی‌پی‌هایی را پیدا می‌کنیم که "واقعاً" کار می‌کنند.
⚡️
سرعتِ خیره‌کننده:
طراحی‌شده برای اسکن‌های فوق‌سریع که زمان شما را هدر نمی‌دهد.
🎯
حذف هوشمندِ آی‌پی‌های مرده (Dead-End Elimination):
فیلتر کردنِ آی‌پی‌هایی که پورتشان باز است اما عملاً ترافیک را رد نمی‌کنند.
✨
طراحی مهندسی‌شده:
طراحی و توسعه کامل توسط
Bachelor
⚡️
با تمرکز بر UI/UX مدرن (Material Design 3).
🛠
شفافیت و آینده پروژه:
من تمام تلاشم را کرده‌ام تا این نسخه در پایدارترین حالت ممکن باشد، اما چون در ابتدای مسیر هستیم (v1.0.0)، ممکن است باگ‌های جزئی وجود داشته باشد. من متعهد هستم که در آپدیت‌های بعدی این موارد را سریعاً برطرف کنم.
💡
خبر خوب:
این نسخه از
آپدیت درون‌برنامه‌ای (In-App Update)
پشتیبانی می‌کند؛ بنابراین به محض انتشار نسخه جدید، شما باخبر خواهید شد و نیاز به دانلودِ دستیِ مجدد نخواهید داشت.
📥
لینک دانلود مستقیم (گیت‌هاب)
این اپلیکیشن حاصل روزها تلاش مستمر من برای ارتقای استانداردهای جامعه شبکه است. اگر باگی دیدید، حتماً اطلاع دهید تا در آپدیت‌های آینده برطرف شود.</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6853" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6847">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdivJEpkpA55-kcQse_O6YNN--LnBihW-r4VStIK-6Zv5m5gB9Ux1fI90B_U7zXTLKIyBbWfM6fC-1aJ1BrUR8CYDG0WdAdJHYh9dmqrl-loEKK-nHtw-r9xfF94nYrmJ2-I_Xp1VBcVwUOrVoMqNTrmQ091DoTE4Aeg5w8d01CjTwiqixD4IjEhCRadbpmGBeb9papv1L3aQ5Qol25jfRkCMi78QRJxXb9MqNLM8uZpYWy3wsbKnNg5VR1TCp6na6utWpU6mhBRjBvr6rrkD048wgrJKAZ1lIy7wHGTjoVISRVJ0b5KHYz62bv4hYNu0ppQ2VgY4qOtLVSi2Lejtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
‏
🎮
آیا ‌GTA 6⁩ زودتر از موعد به کامپیوترها می‌آید؟**
🖥️
🔥
‏شاید غیرممکن به نظر برسد، اما توسعه‌دهندگان امولاتور ‌SharpEmu⁩ در حال برداشتن قدم‌های بزرگی برای اجرای بازی‌های ‌PS5⁩ روی ویندوز هستند!
🛠️
‏
✅
چه اتفاقی افتاده؟
‏تیم سازنده موفق شده بازی سنگین ‌Demon's Souls⁩ را تا مرحله لودینگ و صفحه اصلی روی کامپیوتر اجرا کند. این یعنی معماری ‌PS5⁩ در حال رمزگشایی است.
‏اگر این روند با همین سرعت پیش برود، برخی امیدوارند که بتوانند ‌GTA 6⁩ را قبل از انتشار رسمی نسخه ‌PC⁩، از طریق این شبیه‌ساز روی سیستم‌های قدرتمند تجربه کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6847" target="_blank">📅 22:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6846">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚀
۱۰۰۰ اعتبار رایگان در Flashloop برای ساخت ویدیوهای هوش مصنوعی!
🎥
اگر به ساخت ویدیو با هوش مصنوعی علاقه دارید، می‌توانید با ثبت‌نام در Flashloop، ۱۰۰۰ اعتبار رایگان دریافت کنید.
مراحل دریافت اعتبار:
1️⃣
وارد سایت شوید:
https://www.flashloop.app
2️⃣
با حساب گوگل (یا سایر روش‌ها) ثبت‌نام کنید.
3️⃣
هنگام ثبت‌نام یا در بخش مربوطه، کد زیر را وارد کنید:
Z36ZT9
🎉
با وارد کردن این کد، ۱۰۰۰ اعتبار رایگان به حساب شما اضافه می‌شود.
با Flashloop می‌توانید انواع ویدیوهای AI در سبک‌های مختلف تولید کنید و از ابزارهای ویرایش و افکت‌های متنوع آن استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6846" target="_blank">📅 20:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6845">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQiG9_Nha8zqB7lnle2J1V_hYPV4Kk0Xe1Nx5Jz59vCDIlI8yx4GK1bJqoSytrmT5KY3xpl-1cgwZrR0HmGUs9kHPa92fTDWjWRYu6eqF02bKhbLVVxZnhKaw3YZXMD1t-1zQt-14RQ9tXLrf-MMtRtMZ8qiH9sMQFwJSknjBXgnAlQf_tB6nDdWYB9UDroWlfc8meRpJo54HAcGh-OjhPacwkMBuFy-3i5d26C6DO4Sr8GILt9F6K0XzrP0IVrdLqWW1DhRD0j0i5GuDFxqMkAgIwOeD__2edht29EIRxUu0W7RlHCMQ2zzBr5KIMjqA8ZAab2wQ9LZWYGqheedHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐧
GameShell
GameShell
یک پروژه
متن‌باز
برای یادگیری دستورات لینوکس و
Bash
است که به‌جای آموزش سنتی، مفاهیم را در قالب مراحل و مأموریت‌های تعاملی آموزش می‌دهد
🔹
اگر قصد دارید کار با ترمینال و دستورات لینوکس را به‌صورت عملی و سرگرم‌کننده یاد بگیرید،
GameShell
می‌تواند نقطه شروع مناسبی باشد
◾️
🔺
GitHub
✔️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6845" target="_blank">📅 20:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6844">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نامحدود
🫡
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprMWRCT21PQjRvcWk3VW1wMzdhMWJR@82.38.31.189:8080#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6844" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نامحدود
🔥
vmess://771a590c-5eac-5732-b796-17251132f8d2@47.83.221.185:80?encryption=auto&security=none&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6843" target="_blank">📅 18:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6842">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏
💎
گنجینه‌ای از ۱۰,۰۰۰ پرامپت طلایی!
🍌
✨
‏اگر به دنبال خلق تصاویر خیره‌کننده با هوش مصنوعی هستید، این مخزن دقیقاً همان چیزی است که نیاز دارید!
🎨
🚀
‏
✅
ویژگی‌های این مجموعه:
🔹
بیش از ۱۰ هزار پرامپت منتخب و تست‌شده
‏
🔹
بهینه‌شده برای
‌Nano Banana Pro (Google Gemini)⁩
‏
🔹
سازگاری کامل با ۸ مدل برتر دنیا (از جمله ‌Midjourney⁩، ‌DALL-E⁩ و ‌Flux)⁩
‏
🔹
همراه با پیش‌نمایش تصاویر برای درک بهتر خروجی
‏
🔹
کاملاً متن‌باز (‌Open Source)⁩ و رایگان
‏
🔗
https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6842" target="_blank">📅 16:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6841">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416755798a.mp4?token=dKX4FIrtWTGPARXSBwbZ8Rz3eZQc9OcDJDBuqiq4Bx1Pvausq0QoABZXY7bikrS_yK_hiUkAoHzOYS_sCqhYr_I23BkK1CZrI-Qth5i5dhwNqAFiFowqFa5IF8de-MRQfqm2UECrBiO_0P5tkV5vGErU4ZbXbfQSe7ZrwIqTaWahsqQrQymvV7v951BjpVHaAmP73769njcEPv2uyirLqNJUkk5D-j6qv-J33wfiRwWuokdSr1yIEKcK4LM1qQlJa2NoJ7RP9-U-C_MNqX5kSKRGheBej9vdAHh_iXIVUwT3ryBjsPSKHAMVvmU7tz6q6IR0gxaE-FVpT1CZDainlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416755798a.mp4?token=dKX4FIrtWTGPARXSBwbZ8Rz3eZQc9OcDJDBuqiq4Bx1Pvausq0QoABZXY7bikrS_yK_hiUkAoHzOYS_sCqhYr_I23BkK1CZrI-Qth5i5dhwNqAFiFowqFa5IF8de-MRQfqm2UECrBiO_0P5tkV5vGErU4ZbXbfQSe7ZrwIqTaWahsqQrQymvV7v951BjpVHaAmP73769njcEPv2uyirLqNJUkk5D-j6qv-J33wfiRwWuokdSr1yIEKcK4LM1qQlJa2NoJ7RP9-U-C_MNqX5kSKRGheBej9vdAHh_iXIVUwT3ryBjsPSKHAMVvmU7tz6q6IR0gxaE-FVpT1CZDainlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
؛Traycer Desktop App منتشر شد!
رایگان، متن‌باز و ساخته‌شده برای AI Orchestration.
✨
قابلیت‌های جدید:
• استفاده از اشتراک‌های فعلی مثل Claude، Codex، Opencode و...
• ارتباط Agent-to-Agent و Loops
• ؛Workspaceهای دائمی با Tab و Sub-tab
• اشتراک‌گذاری Taskها و همکاری با اعضای تیم
امروز دیگر توانایی مدل‌های هوش مصنوعی چالش اصلی نیست.
چالش واقعی، ساخت محیطی است که Agentها بتوانند به‌صورت هماهنگ با هم کار کنند، حافظه مشترک داشته باشند و از هر جایی ادامه‌ی کار را از سر بگیرند.
؛Traycer دقیقاً برای حل همین مسئله ساخته شده است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6841" target="_blank">📅 15:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6839">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
تبدیل Qwen Chat به API رایگان!
اگر همیشه دوست داشتید از
Qwen
داخل پروژه‌ها، ربات‌ها یا برنامه‌های خود استفاده کنید، این پروژه دقیقاً برای همین ساخته شده است.
؛
FreeQwenApi
سایت
Qwen Chat
را به یک
API رایگان و سازگار با OpenAI
تبدیل می‌کند؛ یعنی می‌توانید بدون تغییر زیاد در کد، از مدل‌های Qwen داخل پروژه‌های خود استفاده کنید.
✨
قابلیت‌ها
✅
تبدیل Qwen Chat به API
✅
سازگار با OpenAI API
✅
پشتیبانی از Streaming
✅
پشتیبانی از فایل، تصویر و Web Search (در مدل‌های پشتیبانی‌شده)
✅
قابل استفاده در Open WebUI، LobeChat، Dify، Claude Code و...
🛠️
آموزش راه‌اندازی
1️⃣
پروژه را دانلود کنید
git clone https://github.com/y13sint/FreeQwenApi cd FreeQwenApi
2️⃣
وابستگی‌ها را نصب کنید
npm install
3️⃣
پروژه را اجرا کنید
npm start
4️⃣
وارد حساب Qwen شوید
توکن (Session Token) اکانت Qwen خود را داخل پروژه قرار دهید؛ از این به بعد می‌توانید از Qwen مثل یک API معمولی استفاده کنید.
⚠️
این پروژه API جدیدی ایجاد نمی‌کند؛ بلکه از دسترسی رایگان حساب Qwen شما استفاده کرده و آن را به یک API سازگار با OpenAI تبدیل می‌کند.
🔗
GitHub:
https://github.com/y13sint/FreeQwenApi
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6839" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6838">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">vless://c44c7433-5460-4269-a7de-0af05e27a48f@64.90.7.33:8080?type=kcp&headerType=none&seed=SwbMceiT2H&security=none#%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86
نامحدود
اگه دیدید قطع شد ip فیلتر شده
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6838" target="_blank">📅 14:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6837">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK2kPcqhDN4L63JnpCdiZ-mJ7fZzSHXp3CAR1dXenO8NXrQVko-sFZFYNEuTzMFlSKfgigBepu40-ZTkknRq1sjJEK5zqHPxFtoHiKn-5rHrLftv73_Ha866jhm0ODQpQnBXiEISHRsD9Mw9GBIE_-O7BnrYQy9NucXfnA2sFUWWNQpKS9yGVI1U4LhNyNFnG-EsdGXirMyEcQG2TNY_Nwrx8mOwNk8DGsBDDzjmqbYbNcDf_G7tG7pfc7fRlUU3ZEeKKRz5-wTZPuiOwLdAK2jdWTajGSTdTRjqRLf68FH5R9w04v2b8Kw3RMQryYmTQcZVYAYpNK7TfRlidCPXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
یک ابزار جذاب برای کار با ویدیو!
معرفی Frame؛ رابط گرافیکی بومی برای FFmpeg ساخته‌شده با Rust
🦀
؛FFmpeg فوق‌العاده قدرتمنده، اما کار با خط فرمانش برای خیلی‌ها سخت است. Frame همان قدرت را با یک رابط ساده و زیبا در اختیار می‌گذارد.
🔥
امکانات:
⚡
ارتقای کیفیت تصویر با AI (Real-ESRGAN)
🚀
شتاب‌دهی سخت‌افزاری (Apple Silicon و NVIDIA)
📦
مدیریت چند پردازش همزمان
🔒
کاملاً لوکال؛ بدون تله‌متری و بدون نیاز به حساب کاربری
💻
پشتیبانی از macOS، Windows و Linux
﻿
یک انتخاب عالی برای کسانی که با تبدیل، فشرده‌سازی و پردازش ویدیو سروکار دارند.
🎥
github.com/66HEX/frame
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6837" target="_blank">📅 04:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6836">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
؛Grok 4.5 رایگان شد!
مدل جدید کدنویسی Grok 4.5 از xAI برای مدت محدودی به‌صورت رایگان در ابزارهای Agent قابل استفاده است.
✨
ویژگی‌ها:
🧠
پنجره متنی 500K برای پروژه‌های بزرگ
⚡️
مناسب برای Agentهای کدنویسی و جلسات طولانی
🔌
سازگار با Hermes، Aider، OpenCode، Cline، Claude Code و تمام ابزارهای سازگار با OpenAI API
⚙️
راه‌اندازی در کمتر از ۲ دقیقه:
curl -fsSL https://x.ai/cli/install.sh | bash
سپس:
• آدرس
localhost:8000/v1
را به ابزار خود معرفی کنید.
• مدل grok-4.5 را انتخاب کنید.
• یا از API Key در کنسول xAI با آدرس پایه
https://api.x.ai/v1
استفاده کنید.
⚠️
این دسترسی محدود و موقتی است و شامل Rate Limit می‌شود. (شاید ۱۲ ساعت مونده باشه ازش) (تست نشده)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6836" target="_blank">📅 04:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6835">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bikx5HopDY100gvtdIvVeV1d7RiV-CwqPYy_ASw5k3wt5CPRTznXv0MwFT9m051wfECminu1yTVQ4oqa7g6HeEQCmf8oBuVp-EqFjgQXDyXuhoWOigzf332gtr5oD0QlcVkKARzO7c1XGIhnAUkQ0PebGvm4VO4oprT2oewd1qzeXxMg95SNmViTOhJ603GcUccDGtjrx_y6qcb3jC5_49Su128s6v8w-sD2r_vmHiBpcAbYkV-tYLx9-TSAh68g37EMdlg2oM2mN0XQoARm8yjFSCzXexcwY_bvDgRfVzpUPDezPMhph-RS-PGusrb7BBE8QzRxKnjvQFx6HlhAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧭
؛MBCompass؛ قطب‌نما و مسیریاب متن‌باز برای اندروید
یک اپلیکیشن سبک و رایگان برای طبیعت‌گردی، کوهنوردی و استفاده روزمره؛ بدون تبلیغات، بدون ردیابی و بدون وابستگی به سرویس‌های گوگل.
✨
امکانات:
🧭
قطب‌نمای دقیق (شمال مغناطیسی و واقعی)
📍
نمایش موقعیت لحظه‌ای روی OpenStreetMap
🗺️
پشتیبانی از نقشه‌های آفلاین و آنلاین
🥾
ضبط مسیر و خروجی GPX
🔋
حجم کم (~۲ مگابایت) و مصرف باتری پایین
🔒
بدون تبلیغات، بدون جمع‌آوری داده‌های شخصی
یک گزینه عالی برای علاقه‌مندان به سفر، طبیعت‌گردی و مسیر‌یابی.
🌿
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6835" target="_blank">📅 03:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6833">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter وارد سایت Agentrouter شوید با حساب Github ثبت‌نام کنید بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key وارد سایت شوید…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6833" target="_blank">📅 00:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6831">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lW5ZoK363ID64dvUEIYaiRuw_gdi2hS_HnA9gFRIt0jASurHQB5-V0mjy9NLQuFfyVS0nqSSnk_vanvHPLHoVm0tBCcqV9EzQ_5CgN76kpJD4efGzeyl7vgFXDlNczr3lWOcaerYS57WCNRcNe-O0LRAjwQYB_l1Dvf7qUaMYrPUCA0no_OooLUZWXiSS32R_F8Jlkhi7bigZzCNylYxrIP3uK-apJpigoc0yGYKnBDFUMtP8ynteAZ4UJb1hz1pjaCIkLIJP6IiKXPSVxA0YTte_1QGDwTIGo5ubcfY6eUoziY-EUa5Os1mCqAubx7otVZ6N0F426CNAiKxNwynlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
🚀
؛Cloudflare Drop؛ انتشار سایت در چند ثانیه!
کافی است پوشه پروژه‌تان را داخل مرورگر Drag & Drop کنید تا سایت فوراً روی شبکه Cloudflare منتشر شود.
✨
ویژگی‌ها:
⚡
بدون نیاز به ثبت‌نام
🌍
دسترسی جهانی با تأخیر بسیار کم
📁
مناسب برای دمو، نمونه‌کار و پروژه‌های آزمایشی
⏳
نسخه‌های بدون حساب تا ۶۰ دقیقه فعال می‌مانند و سپس حذف می‌شوند؛ با ثبت‌نام می‌توانید آن‌ها را دائمی کنید.
https://cloudflare.com/drop/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6831" target="_blank">📅 00:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6829">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRt79JuOvv9i8ceHFtIR_FdBL9NjAPQCdD0sOAGvK1Zjre33Y0uRmqIrrwQHFSnjib6Y4c7qJMB3fzA3bVxDqLu61hucGkT2jrf_hnqeV2Su6c3zX2QupSVoL4yGeI2IIMQU6Vv6YyjiK9CyxIONo4gimoX7Fd5Y3A5PC4p4aRtMi1IiZUvol19UxBE-UgUKICV-uc9mH-0YT3KbVLwYpmh_0j-cpi4twkzrCLNS26_bBhrGPuYSr3ftWrNlZhwI9qk1xIMnyZnKe8V8ZaQtRZiWpCaPBmXjFSZSO6DEz4wlct5ydNERBlrbR4bZ_y1qjlcszfe6lIDrm48uvLsycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6829" target="_blank">📅 23:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6828">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🧩
؛CanvasMind | ساخت و استقرار ورک‌فلوهای AI با بوم بصری
✨
یه ابزار متن‌باز و Low-Code برای طراحی و اجرای ورک‌فلوهای هوش مصنوعی! دیگه فقط دمو نیست، مستقیم به پروژه قابل استقرار تبدیلش کن
🚀
⚡
ویژگی‌ها:
🎨
بوم گرافیکی با Drag & Drop
🔀
شرط، حلقه و منطق کنترلی
💻
اجرا محلی یا از راه دور via SSH
🤖
دستیار هوشمند داخلی
🚀
خروجی CLI، API، Docker و Server
🔗
https://github.com/buyaka/canvasmind
#هوش_مصنوعی
#LowCode
#ورک‌فلو
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6828" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6827">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">📱
💿
؛EtchDroid؛ ساخت فلش بوتیبل با گوشی اندروید
اگر کامپیوتر در دسترس ندارید، EtchDroid به شما اجازه می‌دهد فایل‌های ISO سیستم‌عامل‌های لینوکسی را مستقیماً از طریق گوشی روی فلش USB رایت کنید و یک فلش بوتیبل بسازید.
✨
ویژگی‌ها:
🔹
متن‌باز و رایگان
🔹
پشتیبانی از اکثر توزیع‌های لینوکس و Raspberry Pi
🔹
مناسب برای مواقعی که سیستم بالا نمی‌آید و فقط گوشی در دسترس است
⚠️
این برنامه از ISO رسمی ویندوز و فایل‌های DMG مک پشتیبانی نمی‌کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6827" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6826">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🤖
؛Cogny | دستیار هوش مصنوعی بازاریابی
✨
یه ابزار فوق‌العاده که بازاریابی رو با هوش مصنوعی انجام میده! سئو، تبلیغات، تحلیل رقبا و کلی کار دیگه
🚀
⚡
ویژگی‌ها:
🎯
سئو و بهینه‌سازی محتوا
📊
تحلیل کمپین‌های تبلیغاتی
🔍
آنالیز رقبا و بازار
✍️
تولید متن تبلیغاتی
📈
اتصال به ۱۳ کانال بازاریابی
💻
کار با Claude، Cursor و Codex
💰
رایگان برای شروع · ۹ دلار برای استفاده نامحدود
🔗
https://cogny.com
#هوش_مصنوعی
#بازاریابی
#سئو
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6826" target="_blank">📅 21:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6825">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoA6GHI188jiKtxya1xk9a4S4hm_nX00n8WuCFhR1-9wDwbzn9PH1QTpv6SkC0t-NkwiOJeHB_xCEdNZmtWLTGEGxV2O7OFBrtJ4DGw7a4nrtbWgRNFD4VGaMpVv5dPhkxFYaK1GlY9Xt__BtGI8hMxrMbr6HoiLW3frbRWJxoCJ6Orz--nl9kkUCjxFW2yj4DXzJNxzZ6ix6GS_cmw8Ka4r8Tyb3b6TYnhcSA0LrasmzHeZ9JV-5Om4OlBYNRLdll3BLfRHxrKI0ojYaAYsJLQ647t3uaZaJZyZKg-2w9OZ7vyzOtJ3OtAIV8-HX9yx7nSuEsmQcBnrxREmKK524w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6825" target="_blank">📅 20:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6824">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">104.17.14.0
104.25.49.102
ایپی تمیز کلودفلر
تست کنین
❤️
با لایک و دیسلایک و کامنت اعلام کنین
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6824" target="_blank">📅 20:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6821">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzF_LueWGoeuFJj0y82RemAHCy2FcAe3J1jdH3GaJ3TYDPi-uobsDUucTTjebBySKFMfOqqq3adF5Oqhbms-R-BENmW4CnF4IaMbZX3PomYZ01Ef227PKbgykwUGMfDyVMIl5m6B2X-EsZxea71IFm746KlPVa3xibdBYL8IvERYqjlhwrFlJiM32ojmEVY2fh9TijxdNA9nxy9U8tOWMG2l6SlkAJAn78ArZCCg88LdkwG3ea9qrDzxgfJVSLmlzx80xfICsLx1TUp_lhUa2-pCSUJ8ACLu_7Pap9HaobpQbIXCOYvqlVpMJ0RzaqFTGkb3zaT7N_GiiOheOIbH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfHImfecdoFY4E2bchvLl4BGiJPEMyp71N7Kx2BN3sxXqUTeDtw102WgkGxxATX47_AZ7710PBgxD1RkCn3J9NSsIwsvLx8aWn6owPn2hCn5midKM6qoTX2OEUHCnLWW4UIdJno3wW_Xc84PplicT21NjJn73xMRwf9o-DClHvkOsjjJNaV9p6idH7XYClUkF5sn9gfzCwtrdeFMiBXQZSycrCofyAV5wpBDisb6o2f4iyosZSAEzhefoeynWd2b6aKXSDpECkZnRlMsSMB15s9x6UvGrwp4aOMBOlX4djqNxVruFw70cf3LGo2ZF6mDhw54sPMFQyal3LYGNeNggQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏‌
Imgfree⁩: ابزار رایگان تولید تصویر و ویدیو با هوش مصنوعی
🤖
‏
🌐
پلتفرمی که مدل‌های پیشرفته هوش مصنوعی مانند ‌‌Midjourney⁩، ‌GPT-Image⁩ ، ‌Kling⁩ ، Nano Banana و Flux را گرد هم آورده است
📈
‏
✨
تولید تصویر و ویدیو بدون نیاز به تنظیمات پیچیده
📺
‏
🔗
لینک: ‌
https://www.imgfree.co
⁩
‏
💻
دسترسی رایگان و نامحدود برای تولید محتوای با کیفیت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6821" target="_blank">📅 19:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6820">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB27B3iSGNc4_9sjazh-RjEzr1d73irsv-Ml6SCF-OuCcJiZGOD5EkdRYHk3_nO5CKnxkzzrMkGLpu--NQ9J0VPAzSveayZDudk3tS_J9mMndw7vQAfMkOBJu7Bgkxp4V1kgMzh310qPU6Y-M1tXrzQgVfGpSxvp-3JR2Sj-U9Us2lRi8YIsg4ZNd0HffJpN59C-_DpAVdWsL5CAdWXbatBammX_bF7F1xX_jm5uZt8T4yPV5IoliijDFkbVxVYn_g5IBIQ72_6dn9uVri9iMFZeWeFwORBn8X-FMPh83l6DlNYQzCHqWZW95O3ue5GjyBj9TSdqb6umDuWzCqe_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛
🎬
CapCut Web؛ ادیت ویدیو با هوش مصنوعی
اگر تولید محتوا می‌کنید یا برای شبکه‌های اجتماعی ویدیو می‌سازید،
CapCut Web
یکی از کامل‌ترین ابزارهای آنلاین برای تدوین سریع و حرفه‌ای است.
با قابلیت‌های هوش مصنوعی این پلتفرم می‌توانید:
•
🪄
حذف خودکار پس‌زمینه و نویز صدا
•
📝
ساخت زیرنویس خودکار (حتی برای فارسی)
•
✂️
تبدیل ویدیوهای طولانی به کلیپ‌های کوتاه مناسب ریلز و شورتز
•
🎨
استفاده از افکت‌ها، قالب‌ها و ابزارهای هوشمند ادیت
🔗
سایت:
https://www.capcut.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6820" target="_blank">📅 18:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6819">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌐
دانلود کامل هر وب‌سایت با Website Downloader
اگر می‌خواهید یک وب‌سایت را برای استفاده آفلاین یا بررسی کدهای آن دانلود کنید(فرانت اند)،
Website Downloader
ابزار مناسبی است.
✨
قابلیت‌ها: •
📥
دانلود کامل
HTML، CSS، JavaScript، تصاویر و فونت‌ها
•
🔗
بازنویسی لینک‌ها برای اجرای آفلاین •
📦
خروجی به‌صورت فایل ZIP •
⚡
متن‌باز با لایسنس MIT
این ابزار برای
کلون کردن سایت‌ها، تهیه نسخه آفلاین و یادگیری ساختار پروژه‌های وب
بسیار کاربردی است.
🔗
GitHub
:
https://github.com/AhmadIbrahiim/Website-downloader
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6819" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6818">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=s_-hDdWlNKCWzuN0F4W3F2L8cGUl9vrvJ_o_WZ8ZWjuN3UXNg0bI_5OM04355-J7d8POX7EYQ9qeYtzII38uhPgiz5qPGS7NCnw2GWGx9pEli5V-tHnAYs8dUXlozbHA-Kjzirs72f3E6mo9-oM1UNKY7t85FP8qfEkkZ16tjvQ3YsTOFE5jl1t8PqXFutAjCPtBoJhFaLIKRpf2k5SZGjcVLqkytV5a3GNVtR6zppnWbw5vipVRTq0IwfrNp6nn22JOKFkfGAhpzvXb51WFulVFdY_sQqjBfBGAfUdkNfkpqBZOlB8k9l6DUkQt-jtyJwNk5s41vyvrQR3ky1Jwsppp9MG7l3p4W3_iUg-zZnpnUM1LoFyHbefGCXKHOeA10McsqqCEVk9WU-sUGnTMmBSnH0Vf1o2gEKCsKUryW-xL58NOI32flE1z1sFnrEHn60Grh1Zjw4Nkan4C3jcdtRp-D1_vzelA6zPaqRa8uV9U3IUGuCHw7wkQ2s0WOGEsIl4qBseCMlJ9huxuYcsMpA9CjziqKtOxO8FhYZ2JIxTtYLdY6hG6znupYEu1nPkQjHWXa3hpL_G079ERrT_vaz2Ei-7YNMZEClyS3-M76NM9szrbZITHIi9-5O8v__2Dgut3VFQVJmWO72F5tamNFcWikOQEt3x99R26QIIkqSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=s_-hDdWlNKCWzuN0F4W3F2L8cGUl9vrvJ_o_WZ8ZWjuN3UXNg0bI_5OM04355-J7d8POX7EYQ9qeYtzII38uhPgiz5qPGS7NCnw2GWGx9pEli5V-tHnAYs8dUXlozbHA-Kjzirs72f3E6mo9-oM1UNKY7t85FP8qfEkkZ16tjvQ3YsTOFE5jl1t8PqXFutAjCPtBoJhFaLIKRpf2k5SZGjcVLqkytV5a3GNVtR6zppnWbw5vipVRTq0IwfrNp6nn22JOKFkfGAhpzvXb51WFulVFdY_sQqjBfBGAfUdkNfkpqBZOlB8k9l6DUkQt-jtyJwNk5s41vyvrQR3ky1Jwsppp9MG7l3p4W3_iUg-zZnpnUM1LoFyHbefGCXKHOeA10McsqqCEVk9WU-sUGnTMmBSnH0Vf1o2gEKCsKUryW-xL58NOI32flE1z1sFnrEHn60Grh1Zjw4Nkan4C3jcdtRp-D1_vzelA6zPaqRa8uV9U3IUGuCHw7wkQ2s0WOGEsIl4qBseCMlJ9huxuYcsMpA9CjziqKtOxO8FhYZ2JIxTtYLdY6hG6znupYEu1nPkQjHWXa3hpL_G079ERrT_vaz2Ei-7YNMZEClyS3-M76NM9szrbZITHIi9-5O8v__2Dgut3VFQVJmWO72F5tamNFcWikOQEt3x99R26QIIkqSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌎
نقشه آینده زمین برای زندگی!
‏این پروژه خیلی جالب و مهمه! یه نقشه تعاملی به نام ‌Farmland Atlas⁩ ساخته شده که پیش‌بینی می‌کنه مناطق مختلف زمین چقدر برای زندگی مناسب خواهند بود تا سال ‌2100⁩.
🤔
‏این پلتفرم با تحلیل بیش از ‌5⁩ میلیون نقطه، چندین سناریو رو بررسی می‌کنه، از خوش‌بینانه تا بدبینانه. برای هر مکان، پیش‌بینی آب و هوا، ارزیابی کیفیت منابع آب، وضعیت خاک و خطرات اجتماعی رو هم در نظر می‌گیره.
🌟
🔗
https://farmlandatlas.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6818" target="_blank">📅 14:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6817">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">📊
معرفی ابزار CodexBar
اگر از
Claude Code، OpenAI Codex، Cursor، Gemini، OpenRouter، GitHub Copilot
یا سایر ابزارهای AI استفاده می‌کنید، احتمالاً بارها با محدودیت استفاده یا تمام شدن سهمیه مواجه شده‌اید.
؛
CodexBar
یک ابزار متن‌باز برای macOS است که تمام این اطلاعات را مستقیماً در نوار منو نمایش می‌دهد تا همیشه بدانید چقدر از سهمیه‌تان باقی مانده است.
ویژگی‌ها:
• نمایش میزان استفاده و سهمیه باقی‌مانده
• نمایش زمان دقیق ریست شدن محدودیت‌ها
• پشتیبانی از Claude، Codex، Cursor، Gemini، OpenRouter، GitHub Copilot، Groq، Deepgram، MiniMax،
z.ai
و ده‌ها سرویس دیگر
• نمایش هزینه، اعتبار و میزان مصرف API در سرویس‌های پشتیبانی‌شده
• نمایش وضعیت آنلاین سرویس‌ها و اختلالات احتمالی
• حالت تجمیعی برای مدیریت چندین سرویس از یک پنل
• بدون ذخیره رمز عبور؛ از نشست‌ها و لاگین‌های موجود شما استفاده می‌کند.
🔗
GitHub:
https://github.com/steipete/CodexBar
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6817" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6816">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
چند ابزار متن‌باز و رایگان برای برنامه‌نویس‌ها و سازنده‌ها:
🎨
Text Effects
افکت‌های جذاب CSS برای طراحی متن و رابط وب.
📧
SESPulse
داشبورد متن‌باز برای مدیریت و بررسی ایمیل‌های Amazon SES.
🔎
API Finder
مخزن APIهای عمومی برای پیدا کردن سرویس‌های آماده.
🛡
Tirreno
فریم‌ورک امنیتی متن‌باز برای شناسایی رفتارهای مشکوک کاربران.
💻
OpenTUI
کتابخانه ساخت رابط‌های کاربری زیبا در ترمینال.
✨
ابزارهای کوچک، کاربردهای بزرگ برای ساخت سریع‌تر پروژه‌ها.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6816" target="_blank">📅 13:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6815">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://ac7e7b41-0dc0-4bec-a285-3266ecbb87c8@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6815" target="_blank">📅 13:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6814">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📸
ساخت عکس پرسنلی ۳×۴ با هوش مصنوعی
اگر یک عکس معمولی از خودتان دارید، می‌توانید با پرامپت زیر آن را به یک
عکس پرسنلی رسمی
تبدیل کنید.
✨
ویژگی‌ها:
✅
پس‌زمینه سفید یا خاکستری ساده
✅
نورپردازی طبیعی و یکنواخت
✅
حذف اشیای اضافی و اکسسوری‌ها
✅
افزایش کیفیت و وضوح تصویر
✅
مناسب برای عکس پرسنلی و پاسپورت
📝
Prompt:
Convert this photo into a professional ID/passport photo.
- Neutral plain background (light gray or white, evenly lit, no texture).
- Centered face and shoulders visible, crop from top of head to chest.
- Natural skin tone, balanced lighting, no shadows.
- Neutral facial expression (slight smile allowed).
- Professional look, no accessories (remove hats, sunglasses, background objects).
- Enhance sharpness and clarity.
- High resolution, suitable for official use.
💡
برای بهترین نتیجه، یک عکس با نور مناسب و کیفیت خوب به مدل بدهید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6814" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6813">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📄
olmOCR | تبدیل هوشمند PDF به Markdown با هوش مصنوعی
یک ابزار متن‌باز برای تبدیل فایل‌های PDF، PNG و JPEG به متن و Markdown تمیز با حفظ ساختار اسناد؛ مناسب برای مقالات، کتاب‌ها و فایل‌های اسکن‌شده.
🚀
⚡
ویژگی‌ها:
📝
تبدیل PDF و تصاویر به Markdown خوانا
📊
پشتیبانی از جدول‌ها، فرمول‌ها، دست‌خط و قالب‌بندی‌های پیچیده
🧹
حذف خودکار هدر و فوتر صفحات
📚
حفظ ترتیب طبیعی متن حتی در اسناد چندستونه و دارای شکل
⚡
دقت بالا با پشتیبانی از پردازش محلی یا سرورهای vLLM
🔓
متن‌باز با لایسنس Apache 2.0
🔗
https://github.com/allenai/olmocr
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6813" target="_blank">📅 10:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6812">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">؛
🛠️
OfficeCLI؛ هوش مصنوعی برای Word، Excel و PowerPoint
؛
OfficeCLI
یک ابزار متن‌باز جدید است که به دستیارهای هوش مصنوعی امکان کار مستقیم با فایل‌های
Word، Excel و PowerPoint
را می‌دهد.
✨
قابلیت‌ها: •
📄
ساخت و ویرایش اسناد Word •
📊
ایجاد و تحلیل فایل‌های Excel •
📽️
ساخت و ویرایش ارائه‌های PowerPoint •
✅
بررسی و اصلاح خودکار خروجی‌ها
نکته جالب اینکه
بدون نیاز به نصب Microsoft Office
کار می‌کند و از محیط‌هایی مثل
Claude Code، Cursor و Codex
نیز پشتیبانی می‌کند.
🔗
GitHub:
https://github.com/iOfficeAI/OfficeCLI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6812" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6809">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=Gi1r9uON_xFA5oxs_ZRPqlphXXKS_cCbgmDM-quzYJIicGUIlwOF6RieajHlw4xjApexirzGK8QYWZk_Vr6QFQxZtcJFAuyCj7ad0zJgPUDo2egSGghCsREKjnhhSJw-2RpTDqNjHuU-2CGiT-xljm-Xy9CWtxkr2x_avAVfA77Q2Q7jU-WNnds9lUD-B4ZbyMKfphUGmQFVXZyX1m64D7MtMoBXOtIH16076zwmRZpjwZ2ljCx-quI6OjWu9VIqwlW8Oa0gxLwiavUBDLGCmlgkLR9_rm5PMGdrjiHBJ2YgYgzB8GvgcSKmBnS4qO08dY1nhr25X7lABfhP6-JVGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=Gi1r9uON_xFA5oxs_ZRPqlphXXKS_cCbgmDM-quzYJIicGUIlwOF6RieajHlw4xjApexirzGK8QYWZk_Vr6QFQxZtcJFAuyCj7ad0zJgPUDo2egSGghCsREKjnhhSJw-2RpTDqNjHuU-2CGiT-xljm-Xy9CWtxkr2x_avAVfA77Q2Q7jU-WNnds9lUD-B4ZbyMKfphUGmQFVXZyX1m64D7MtMoBXOtIH16076zwmRZpjwZ2ljCx-quI6OjWu9VIqwlW8Oa0gxLwiavUBDLGCmlgkLR9_rm5PMGdrjiHBJ2YgYgzB8GvgcSKmBnS4qO08dY1nhr25X7lABfhP6-JVGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">؛‌OpenAI⁩ مدل جدید ‌GPT-Live-1⁩ رو معرفی کرده که مکالمات صوتی با هوش مصنوعی رو به سطح جدیدی می‌بره!
🎙️
‏این مدل میتونه تغییر لحن بده، بخنده و حتی وقتی که کاربر ناگهان حرفش رو قطع می‌کنه، طبیعی‌تر واکنش نشون بده
🗣️
‏و اما یه قابلیت خیلی جالب دیگه: میتونه به صورت آنی به حرف‌های کاربر واکنش نشون بده و حتی به عنوان مترجم همزمان کار کنه!
🌎
‏همین حالا از طریق ‌
ChatGPT Voice⁩
قابل دسترسه!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6809" target="_blank">📅 08:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎯
RankGrow | دستیار هوش مصنوعی برای سئو
ابزاری هوشمند که با اتصال به Google Search Console، مشکلات سئوی سایت را شناسایی کرده و لیستی از مهم‌ترین کارهایی که باید انجام دهید را ارائه می‌دهد.
🚀
⚡
ویژگی‌ها:
📊
اتصال مستقیم به Google Search Console
🤖
۷ دستیار تخصصی هوش مصنوعی برای سئو
📝
پیشنهاد بهبود محتوا، لینک‌سازی و سئوی فنی
🎯
لیست اولویت‌بندی‌شده از کارهای ضروری SEO
📈
تحلیل رقبا و کشف فرصت‌های رشد
🎁
۵ اعتبار رایگان برای شروع (بدون نیاز به کارت بانکی)
🔗
https://rankgrow.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6808" target="_blank">📅 07:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کد نویسی رایگان با ابزار هوش مصنوعی FREEBUFF
💻
ابتدا به
سایت
بروید و اکانت بسازید سپس ابزار را اجرا کنید
🚀
— نصب آسان با دستور npm install -g freebuff
🛠️
— بدون نیاز به کلید، کارت یا اشتراک ماهانه
🆓
— مدل‌های پیشرفته از جمله DeepSeek V4 pro و Mimo 2.5 pro و Minimax M3
🧠
— دارای یک وب سایت برای تولید و استقرار برنامه‌ها به صورت رایگان
🌐
کد نویسی خود را با هوش مصنوعی و به صورت رایگان انجام دهید!
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6807" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6806">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎉
Claude Opus 4.8 رایگان در
Supercode (فقط یک روز)
به مناسبت لانچ Supercode در Product Hunt، این ابزار دسترسی رایگان یک‌روزه به مدل Claude Opus 4.8 را برای همه کاربران فراهم کرده است.
🚀
⚡
جزئیات:
🆓
دسترسی رایگان به Claude Opus 4.8 برای یک روز
🤖
استفاده از AI Agent در ترمینال
💻
مناسب برای کدنویسی، توسعه و مدیریت پروژه‌ها
📈
؛Supercode
تاکنون به بیش از ۹,۵۰۰ دانلود، ۸۲ ستاره GitHub و ۲۲۰ کاربر رسیده است.
اگر قصد دارید Supercode را امتحان کنید، امروز بهترین فرصت است.
🔗
https://supercode.sh
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6806" target="_blank">📅 02:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6798" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6797">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اقا سرعتی slipnet رو اپدیت کنید
😁
😁</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6797" target="_blank">📅 00:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎬
FreeCut | تدوین ویدیو با هوش مصنوعی
یک ابزار متن‌باز که با کمک مدل‌های هوش مصنوعی، ویدیوهای خام را به‌صورت خودکار تدوین می‌کند؛ بدون نیاز به API پولی.
🚀
⚡
ویژگی‌ها:
✂️
حذف مکث‌ها، تپق‌ها و بخش‌های اضافی
🎨
اصلاح رنگ خودکار و افزودن زیرنویس
🎥
ساخت انیمیشن و افکت‌های تصویری
🧠
پشتیبانی از Whisper محلی (بدون API Key)
💻
سازگار با Claude Code، Codex و سایر AI Agentها
🔗
https://github.com/Moh4696/freecut
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6796" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6795" target="_blank">📅 23:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromlocalhost(Yousef Taheri)</strong></div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6794" target="_blank">📅 23:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMv3S6JI7oYcekYhVnfDXnLLmezflZ4N0Vd8bGoC4HNErakDZRv08GelQtpyOg-5zGy-lvJONSgw-K4VIAuTN1MNrEmT_K7s8RuBwZf65-I4r03hu1vbZ7dMGLCPVARIO4LoTS_4amAfnnNwMMrSRIL9Pia1WPDzu3Oa-EUrZGj_WwhAdeprSMK3ADbfypQxPVe47XOMUyI-Z7xyjD62hHpIp9v4PFZjbVlApcoWZIPeugip4RtCjfFr7qV7zj0MKEJPNXOlwm9B0_2Hp6yUjejCFJlfXP3kg_cwh3cPUwOeWW1BItg_H61C2k1b7TtPjhN9PaEi24O-CL7XcFA_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Grok 4.5 منتشر شد
⚡️
این نسخه محصولی ویژه از ایلان ماسک است که به‌طور خاص برای برنامه‌نویسی و توسعه‌ی ربات‌ها طراحی شده است.
نکات مهم:
• این مدل به طور مشترک با شرکت Cursor توسعه داده شده و با استفاده از داده‌های واقعی میلیون‌ها برنامه‌نویس آموزش داده شده است.
• سرعت بسیار بالا: 80 توکن در ثانیه.
• قیمت بسیار مناسب: 4 برابر ارزان‌تر از Opus 4.8.
در حال حاضر، به صورت
رایگان
در Cursor و Grok Build در دسترس است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6793" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#اختصاصی
شبیه‌سازهای پلی‌استیشن
🎮
PS1:
duckstation.org
PS2:
pcsx2.net
PS3:
rpcs3.net
PS4:
shadps4.net
PSP:
ppsspp.org
PSV:
vita3k.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6791" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://878fa338-f275-4bf6-93ea-ef47d8865f59@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6790" target="_blank">📅 19:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=VJ1Kc9lqvAhkOAtdJDrg9tG3beE6_1MBgDuCe_ygyrU68SIidW_1d99w2uGBieKw3I3mZSwKCOPF_mzYJV-E7kHALBE3nONxdut6gGJJQSyb4F-CVnAWzmG4CtpniP1hEBSJDxxM4uKy1FMepzvqsN5XAgVOtJRlHQ8Jbl-hFf31G3mVBXFGkQHSO25nFTB9JSO_t6AdMkaKbVlVxLlfhzPO1jqRkaiR_3yMnmFnS7oU14tNwQHDp7u9hZTlGURZ3W_ev-jfBwkK5Up9b1AnLtAnzrkgjJDB1vptFTAKMjxvWUpLIzZS7osD-U-F_qFeDreSDtUdfWEOpRBTsgibw4k-AkicpvfN99MNAmqrk-2HJIskgkZv6WilBP1tY1lOD30k0Zi0FlQ3rxBL05M_L1pRrcmjc_5bvXR5lVmzVCwT5UWlV_OW72ovN0afw-ICXft94D74wrzJz93D0PE-QHDYNFyCzQUmQsCQvjzDtpPkeU68OUhF9kYq2WUNEooRTJRQjKggYMjlkcjRbwKcti7piDdUh9q3a8jn94XBIf7Hm-I_o_BBQdGm3fv7Ud8XM6HmcAGrvd0FvIbBhRLmc3g-Nuad1BCWw4HIOCFsCEHIEM5rdl4fdEBldRmuZQpvdKPmiuH5GaJKSg2Eqf8ZCOXC80eurTch3G0wvNLcO9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=VJ1Kc9lqvAhkOAtdJDrg9tG3beE6_1MBgDuCe_ygyrU68SIidW_1d99w2uGBieKw3I3mZSwKCOPF_mzYJV-E7kHALBE3nONxdut6gGJJQSyb4F-CVnAWzmG4CtpniP1hEBSJDxxM4uKy1FMepzvqsN5XAgVOtJRlHQ8Jbl-hFf31G3mVBXFGkQHSO25nFTB9JSO_t6AdMkaKbVlVxLlfhzPO1jqRkaiR_3yMnmFnS7oU14tNwQHDp7u9hZTlGURZ3W_ev-jfBwkK5Up9b1AnLtAnzrkgjJDB1vptFTAKMjxvWUpLIzZS7osD-U-F_qFeDreSDtUdfWEOpRBTsgibw4k-AkicpvfN99MNAmqrk-2HJIskgkZv6WilBP1tY1lOD30k0Zi0FlQ3rxBL05M_L1pRrcmjc_5bvXR5lVmzVCwT5UWlV_OW72ovN0afw-ICXft94D74wrzJz93D0PE-QHDYNFyCzQUmQsCQvjzDtpPkeU68OUhF9kYq2WUNEooRTJRQjKggYMjlkcjRbwKcti7piDdUh9q3a8jn94XBIf7Hm-I_o_BBQdGm3fv7Ud8XM6HmcAGrvd0FvIbBhRLmc3g-Nuad1BCWw4HIOCFsCEHIEM5rdl4fdEBldRmuZQpvdKPmiuH5GaJKSg2Eqf8ZCOXC80eurTch3G0wvNLcO9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چینی‌ها یک "غول" جدید برای تولید تصاویر معرفی کردند: Seedream 5.0 Pro.
ویژگی‌های این ابزار:
🔹
ویرایش لایه‌ای تصاویر
📦
‏
🔹
ترکیب چندین تصویر در یک طرح کلی
📚
‏
🔹
تنظیمات جداگانه برای سبک هر شیء
🎨
‏
🔹
ویرایش محلی مناطق انتخابی
🔍
‏
🔹
تغییر تصاویر بر اساس دستورات متنی
📝
‏
🔹
تطابق دقیق‌تر خروجی با درخواست
📊
‏
🔹
بهبود عملکرد در کار با متن داخل تصاویر
📚
‏
🔹
تولید اینفوگرافیک، نمودارها و سایر مواد بصری
📊
‏
نسخه ‌Lite⁩ رایگان در ‌
Higgsfield⁩
و ‌
Dreamina⁩
قابل آزمایشه
📦
👀
‏نسخه ‌Pro⁩ از طریق ‌API⁩ در دسترسه
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6788" target="_blank">📅 19:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLk4Q7gClVjnYUPWy_E-9B64AsVhailxlWP1r1cyZ-mfGK2RYGfmD7y9asu7d--uqF3M-4eajdPYtI5Lgqo0nwuE1Ux5gRAWHEKe78T0oLjYmtPglh_hYW0keE8PPUx_si_5vhSTAsbsP5bSHf4RN_xlyN0aNTowp-4Scg_3TCiqIosDfAd-EMuzMwobM-gsK-x7BxLOG-SNZClIVHBSm9SoRg6xBNXtFK6rq88eY8EBg5MKuV8X4cINtYJ5KBY7XHtSIzhaMZDJ9ENl6SoF5x8jIE56bHynVkSShetggQuIUVXBxGcZecJySdm3twB5Z5N290-Vb7p4rOOdZH-H8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرورگر
DuckDuckGo
در جدیدترین به‌روزرسانی خود قابلیتی اضافه کرده که امکان
حذف تبلیغات ویدیوهای یوتیوب
را فراهم می‌کند
🌐
این ویژگی با استفاده از فیلترهای
uBlock Origin
کار می‌کند. هرچند ممکن است در برخی مواقع
زمان بارگذاری
یا
بافر شدن
ویدیوها کمی بیشتر شود، اما در عوض می‌تواند تجربه‌ای بدون
تبلیغات
و روان‌تر هنگام تماشای ویدیوهای یوتیوب ارائه د
هد
😎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6787" target="_blank">📅 18:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎥
Recordly | ضبط و ویرایش حرفه‌ای صفحه‌نمایش
✨
یک نرم‌افزار متن‌باز برای ضبط صفحه نمایش که ابزارهای ویرایش را هم در خودش دارد؛ مناسب ساخت ویدیوهای آموزشی، دمو و معرفی محصول.
🚀
⚡
ویژگی‌ها:
🎬
ضبط صفحه، پنجره و صدا
🖱️
زوم خودکار، افکت‌های موس و حباب وب‌کم
✂️
تایم‌لاین ویرایش، برش و افزودن متن
📤
خروجی MP4 و GIF
💻
پشتیبانی از ویندوز، لینوکس و macOS
🔗
https://github.com/webadderallorg/Recordly
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6786" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6785">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🛡
Dangerzone | تبدیل فایل‌های خطرناک به PDF امن
یک ابزار متن‌باز برای باز کردن امن فایل‌های مشکوک مثل PDF، فایل‌های آفیس و تصاویر؛ بدون نیاز به اعتماد به فایل اصلی.
🛡
⚡️
نحوه کار:
🗂
فایل داخل یک محیط ایزوله (Sandbox) پردازش می‌شود
🖼
محتوا به پیکسل تبدیل شده و دوباره به PDF جدید ساخته می‌شود
🚫
کدهای مخفی و عناصر فعال فایل اصلی حذف می‌شوند
✨
پشتیبانی از:
📄
PDF
📝
Word / Excel / PowerPoint
🖼
فرمت‌های تصویری مختلف
💻
قابل استفاده در:
Windows | macOS | Linux
📎
https://github.com/freedomofpress/dangerzone
🐍
زبان: Python
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6785" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm4n3evfo5rI1iuCW9BwSsEWJ-i54hHb_bz-uIp4KX4y_x-nCEvXXrtL4ibF9TpnDMSgGL47apLQnzjz9vHc2qC97anJ8mpi4ouAIBL6Zci4JsEUkt-8jT-7an1XnJCpwrEYhVv3OyqSllfeX01NZApFEa5bC7FF9XcJKYlPWR0qGUiKfqd24uO2fLd_FiUOtq_AmQxd17lxAA1IfoH7JLcXxDTHJCjAM7geLgocQLV8YGK2rDe6ya7VPfBJXQ2DGRvpr376e6U9AV6KOaCMClKbu5KxcrvqvN88JmrChgOR6Vl_D_c0cs0JE_EqAyQJMVac2CJ-1txqJHw8RZbpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SubFarsiPro v5.0
📹
این ابزار، یک دستیار حرفه‌ای، پرسرعت و متن‌باز برای استخراج زیرنویس از ویدیوها و ترجمه دقیق اون‌ها به زبان فارسی (با لحن طبیعی و محاوره‌ای) هست
GitHub
🐱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6783" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📊
دنبال معتبرترین رتبه‌بندی مدل‌های هوش مصنوعی هستی؟
اگر می‌خواهی عملکرد واقعی مدل‌های هوش مصنوعی را مقایسه کنی، این دو سایت را از دست نده:
🌐
Artificial Analysis
📈
یکی از کامل‌ترین لیدربوردها برای مقایسه مدل‌ها از نظر کیفیت، سرعت، هزینه، کدنویسی و ده‌ها بنچمارک معتبر.
🔗
https://artificialanalysis.ai
💻
DeepSWE
🧑‍💻
یکی از بهترین بنچمارک‌ها برای سنجش توانایی برنامه‌نویسی مدل‌ها با استفاده از پروژه‌های واقعی و جدید، نه سؤالات قدیمی و حفظ‌شده.
🔗
https://deepswe.datacurve.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6782" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6780" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ارسالی یکی از یوزرای گل
👇</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6779" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6778" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
دسترسی رایگان به هوش مصنوعی قدرتمند Fable 5
اگر دنبال تست مدل‌های پیشرفته هوش مصنوعی برای
برنامه‌نویسی، تحلیل و کارهای پیچیده
هستید، این روش می‌تواند جالب باشد.
🌐
پلتفرم
Tasklet.ai
امکان استفاده محدود رایگان از این مدل را فراهم کرده:
✅
۵۶۰۰ کردیت ماهانه
✅
۳۰۰ کردیت روزانه
✅
مناسب برای تست و استفاده‌های روزمره
📌
روش استفاده:
1️⃣
با ایمیل ثبت‌نام کنید
2️⃣
وارد پنل شوید
3️⃣
از بخش انتخاب مدل،
Fable 5
را انتخاب کنید
هر بار کردیتتون تموم شد میتونید اکانت جدید بزنید
🤝🏻
لینک
🔗
:
Tasklet.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6777" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🗂
نام‌گذاری هوشمند فایل‌ها با هوش مصنوعی (
Renamer.ai
)
پایانی برای کابوس فایل‌های بی‌نام‌و‌نشان مثل
Scan_001.pdf
. این ابزار به جای تغییر ساده متنِ اسم فایل، محتوای متنی و تصویری داخل آن را آنالیز کرده و نام‌های دقیق و جستجوپذیر پیشنهاد می‌دهد.
🔥
ویژگی‌های مهم:
*
🧠
درک محتوای فایل:
استخراج فاکتورها، تاریخ‌ها، نام شرکت‌ها و موضوعات داخل اسناد، تصاویر، اکسل و PDF به کمک فناوری OCR.
*
📸
سیستم پیش‌نمایش:
امکان بررسی و تایید اسامی پیشنهادی قبل از اعمال نهایی روی سیستم برای جلوگیری از خطا.
*
📂
پوشه جادویی (Magic Folders):
مانیتور خودکار پوشه‌های انتخابی (مثل Downloads) و نام‌گذاری آنی و اتوماتیک فایل‌های جدید.
*
⚠️
نکته:
نسخه رایگان محدود به ۲۵ فایل در ماه است. همچنین به دلیل پردازش ابری، بهتر است برای اسناد فوق‌محرمانه و اطلاعات حساس مالی استفاده نشود.
🔗
لینک وب‌سایت ابزار
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6776" target="_blank">📅 12:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌐
وب‌گردی و انجام خودکار کارها با هوش مصنوعی (Browser Use)
یک فریم‌ورک اوپن‌سورس (پایتون) که مرورگر شما رو در اختیار مدل‌های هوش مصنوعی (مثل GPT و Claude) قرار میده تا کارهای اینترنتی رو دقیقاً مثل یک انسان براتون انجام بدن.
🔥
ویژگی‌های مهم:
🤖
اجرای خودکار وظایف:
کافیه با زبان طبیعی بهش دستور بدید (مثلاً "این فرم استخدام رو با اطلاعات رزومه من پر کن" یا "این لیست رو به سبد خریدم اضافه کن").
🧠
پشتیبانی از انواع LLMها:
کاملاً سازگار با مدل‌های معروف و حتی مدل‌های آفلاین/لوکال.
💻
ابزار CLI حرفه‌ای:
قابلیت اتصال مستقیم و راحت به ایجنت‌های کدنویسی.
⚡️
جایگزین مدرن:
بدون نیاز به درگیری با ابزارهای قدیمی مثل سلنیوم، خودش با المان‌های سایت تعامل می‌کنه.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6775" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaC0HA4b1Wl0HYQnXIRSoWY3-Vg6iTF6ARpLWQcg4NbSOR4qfmfpIpxjrdYkDJVkHjiJNEi835jworiQ9v7sEeXeRqItzmxsddwYkC-6NWKomEM9wG9r0vFdTaD7cy8cuB1TvmnEWni9dxItBYbbpWoxRbnnbCz2iN-mjYotX-hV-xDQpZceZbAkPhBzVLYjTay-JOwhkoPA4aznm79qTuU9s9EXNQ0bahXzRs7_co9M8An4AUdrYOzzteGZPCYjbK6uPbIi_NHM-v9ge0Q6xwEC9HEiks2dDrFZlAX9HbtL_zn4LH9D2rAdmOVBnLaTHKTJjh9UlMcbNhN-cUAQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
معرفی Google Flow
این سایت جدیدی نیست ولی خب بعضی دوستان دیدم نمیشناسنش گفتم معرفیش کنم
😁
اگه دنبال یه ابزار رایگان و قدرتمند برای ساخت تصویر با هوش مصنوعی هستی،
Google Flow
یکی از بهترین گزینه‌هاست.
ویژگی‌ها:
✨
تولید تصاویر با مدل‌های
NanoBanana 2
و
NanoBanana Pro
🖼️
ویرایش تصاویر (چه ساخته‌شده و چه آپلودی) با پرامپت
🪙
ساخت تصویر با
۰ سکه
(رایگان)
📚
امکان ساخت همزمان چند تصویر و ادامه ویرایش روی بهترین نتیجه
🎥
قابلیت تولید ویدیو (با محدودیت بیشتر)
📌
لینک:
https://labs.google/fx/tools/flow
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6774" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6773">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQFzSMyEEIM0m-h9EghVQ08_yX1lwlH14W3AQhcR-bkZrPWFp3yAlVM-e4cp64DcP4ZilNMLXhfYvAPLQy6l2KP_dMc_ezY5tUhej8tygjeDlOo6D2dpWL36aHH05tvZ480G71BahlRYbOMhBm7OrxjapMyG6-K87k7ONBjIuPzx43qK1IAOsMJCkA9on1zdxLlSH8M8PTXaJcJPgcwVDoTpVHr2O1cONsrCpX2rl0EP_jX-PNR_KtyUqc_neUQwRG7VjU5XTT_xMg40hckYGDDyWN7HsFNRHkHEe_i6A1Nt9GpYj8hcsZx2ZWtWt9QN5sgB2nO3LLYJgHl-YdZ4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
WLLPR | ژنراتور والپیپرهای مینیمال
اگه از والپیپرهای تکراری خسته شدی، با
WLLPR
می‌تونی توی چند ثانیه والپیپرهای مینیمال و جذاب بسازی؛ اونم دقیقاً با رنگ و استایلی که دوست داری.
🎨
⚡
ویژگی‌ها:
• ساخت والپیپر برای
📱
موبایل و
🖥
دسکتاپ (4K)
• انتخاب رنگ، طرح و استایل دلخواه
• تولید نامحدود والپیپر با یک کلیک
• هماهنگ شدن رنگ رابط کاربری گوشی با والپیپر در بسیاری از گوشی‌های اندرویدی
🌐
لینک سایت:
https://bypedroneres.github.io/ai/
➖
➖
➖
➖
➖
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6773" target="_blank">📅 10:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6772">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKfcFDxJ7NOUmxx6bZ7KPe8MxugzoiaaIJp-arJZM87dL4heglWgZF2c-YeA4s2zjg-5bKiTzQpbQ9qr9vHIJJe1UGRVsUloO1vhWwupAvJ6yJ__-iSuBDvg2rHy-IULIDeib99jY9OmWA-912RLa6e5X5jr7GZlxhvld7yYbpCI7tEwRzbvpNjQZbc8UcZsO7xi1wUHKx8X4wVdX0zLPcGL467ig0-syokXtKJ1XO3NETZbzmZ9l4zHz18oaU_4AC4fPf-AeBUzkSSK1iddNC53PcGZ66vkee_Bi5fjkQlcrn704p75DhsOY-xDwKKjpBiS_sozDuKbT-CM7s3lJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت OpenAI
نسخه‌ی GPT-5.6 را برای Sol، Terra و Luna از فردا راه‌اندازی می‌کند!
🚀
دسترسی زودهنگام از همین حالا برای کاربران در سراسر جهان فراهم شده، می‌توانید با خیال راحت وارد شوید و آن را بررسی کنید.
🌍
🔍
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6772" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZAEX6QOZ-rSlOT5E-fGrpK2u0Nc9G1uegOYUqHTOWF6zb9Enqu9jXHUjQLpGouuZusmNPENCtVFoVNK7dFFnPp3JK9NoA0FeZdesWE2FAty1O8Xjz_NBibAbyOJHitkECfO03VNjEyB_Shs-DZDGuM9fnOvy14sJ9WTSOn6pj4Wu7o-S_VeA8lUlw38MtMVjjWNBE55GAEL0HnXVI0Zv4wW_n6olfhyg1LroTf7nGxF1MnQ3o3NHkhL3LC9pNeC7Q1-zHiy8nIkTWYsIYdrp4NlD93-AJCuK6Lk4qlaCYhmZicFtj6has4WEJJiVCJYNH6EuAMjgrgDY51h2RPFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Constrict ناجی شما در فشرده‌سازی ویدیو!
📹
- ویدیو را آپلود کنید و اندازه مورد نظر را انتخاب کنید.
- بدون نیاز به سرویس‌های آنلاین و دستکاری‌های پیچیده در کدگذاری.
ساده، سریع و کاربردی!
https://github.com/Wartybix/Constrict
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6771" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbjfyo2C0wNLBPZSe4G2-WR19EWEq6GSOVXhyG0MbQuLZfvyIAssoibTksnJqEe9s0w_TO4VzhR456I0Ym2SUQcythAp43Urtsd4dPCiX2gGVCtorfTjNM-Px5AzGzNm-AwgqpEbwZDwH3O-Jov56vdz0-RF1AZiTwJ7IclotQdilv5a38yFjMMJjrysjmvIMlO9G_LUx1kgVqiydvLaiy-Hbdnus4AyQr1vE1RGXS1E-4S0d7XVRcxyuxRovmxTbwxIk4uTD5eeX6sVE1_5MfqFStia3cO0vIawuBpSrKfgmKxstw64oh6_JbbNzvy1NA4nGh03_go1GVLxicj-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تحلیل ویدیوهای یوتیوب، تیک‌تاک و فایل‌های محلی با هوش مصنوعی
؛
Claude Video
یک ابزار متن‌باز است که امکان تحلیل ویدیوها را برای دستیارهای هوش مصنوعی فراهم می‌کند. کافی است لینک یک ویدیو یا فایل محلی را به آن بدهید تا فریم‌های تصویر و متن گفتار را استخراج کرده و در اختیار مدل قرار دهد؛ سپس می‌توانید درباره محتوای ویدیو سؤال بپرسید یا خلاصه آن را دریافت کنید.
⚡️
ویژگی‌های کلیدی:
-
🎬
پشتیبانی از ویدیوهای
YouTube، TikTok، X، Instagram، Loom
و صدها وب‌سایت دیگر
-
📂
تحلیل فایل‌های محلی مانند
MP4، MOV، MKV
و
WebM
-
🖼
استخراج خودکار فریم‌های مهم و متن گفتار (Transcript)
-
🧠
امکان پرسش درباره بخش‌های خاص ویدیو، خلاصه‌سازی و تحلیل محتوای تصویری
-
🤖
سازگار با
Claude Code، Claude Web، Codex
و ابزارهای مشابه
-
🔓
متن‌باز با
لایسنس MIT
🔗
گیت‌هاب پروژه:
https://github.com/bradautomates/claude-video
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6770" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">#Android
#Gaming
🎮
MuMuPlayer 6.0 منتشر شد
نسخه جدید شبیه‌ساز اندروید MuMuPlayer با تمرکز بر عملکرد بهتر و سازگاری بیشتر برای اجرای بازی‌های اندرویدی عرضه شد.
ویژگی‌های جدید:
•
🤖
پشتیبانی هم‌زمان از Android 12 و Android 15
•
🚀
عملکرد روان‌تر و FPS بالاتر
•
🖥
بهبود اجرای چندین Instance
•
🎯
سازگاری بیشتر با بازی‌های جدید
•
⚡
ارتقا بدون از دست رفتن تنظیمات و Macroها
مناسب برای اجرای بازی‌هایی مانند Roblox، استفاده از چند حساب کاربری و تست برنامه‌ها روی نسخه‌های مختلف اندروید.
🔗
https://www.mumuplayer.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6769" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLSMGsKE8ZlC6AFwUp-r09hESK3sFidOMlGvHW7KaxaQouTTpiv1ntah9X6Z9bSxkLqT_O_Nacvb9-DaZ62YY63CMg2ZiTVoabUfGUmW81rzDbErRpgmisENWQKpRnJL0UEL9BTBt5XLQSebzvuFYdgGKCj-QlZVqAa2XkEklL5It_1QAiiUlNODGb7lmXhf9OldjTxYYzBPmojTTOjHBJsaNFU54boeZPPcqmTfLQF_SQpEwmJCEqtUtsBWHJuz3epIGJVFMd4HlKpFzD6m7jq0IdcYt8n7JHu1sbLegEGeAUrx_2RztXJJBnKawFn55Vt-LvsbK9ozc3PHyduK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
یادگیری شخصی با هوش مصنوعی
موضوع رو بهش بده؛ بر اساس سطح و درک شما آموزش می‌سازه.
✅
آموزش مرحله‌به‌مرحله
✅
امکان پرسیدن سؤال حین آموزش
✅
مناسب هر سطحی
🔗
https://peras.app/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6768" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
🎁
100 هزار توکن رایگان ( 3 روزه )
‏دسترسی به مدل‌های زیر و صدها مدل دیگر برای کدنویسی :
🔹
‌GLM-5.2⁩
🔹
‌Qwythos⁩
🔹
‌Deepseek 4 pro⁩
🔹
‌Kimi k2.7⁩
🔹
‌Minimax M3⁩
🔹
‌Mimo 2.5⁩
‏
💡
ویژگی خاص:
امکان استفاده از مدل‌های ترکیبی ساخته‌شده توسط کاربران (مثل ترکیب ‌Qwen + Fable)⁩
🔗
‌featherless.ai
⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6767" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN18FCvUBuqWUxAlZ5Pg7f-I4dKBGBM6Sy2QSWueS5nuza-UJ_ZeCkOA7rD8_IVygynUKwbkVj_2B8IEvddmk1fMdwXDB87hVC-q8m3SR6eC0qn00W4Kk8q15w8W85yub2Ys7Xnd5hXKCy4M7sxaK8wuIKCW29K8IE2ofBugAe6y48zExz0UpLrSnTmz7Tm2XeQNoni1B604ErPSR0Ip0lEXyx1ylD_r4ebRsndbovJP4_w-DNtTvquLWq3WpQa6nPTdytawZTyEz8FaPrEUg7GvQy9A9ya6vgco4HxWTn-CLJxkIGpc-ryCxF1XAtoSum4m-eG_Xb74S-4UpbXJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
PixelRAG
یک پروژه متن‌باز برای Visual RAG که به‌جای متن، اسناد، صفحات وب و PDFها را به اسکرین‌شات تبدیل می‌کند و جستجو را بر اساس محتوای بصری انجام می‌دهد؛ بنابراین جدول‌ها، نمودارها و چیدمان صفحه حفظ می‌شوند.
ویژگی‌ها:
•
🖼
جستجوی مبتنی بر تصویر صفحات
•
📄
پشتیبانی از وب، PDF و تصاویر
•
🤖
سازگار با مدل‌های چندوجهی (Vision)
•
⚡
ابزار CLI برای ساخت و جستجوی ایندکس
•
🌍
API و نسخه دمو آماده استفاده
🔗
https://github.com/StarTrail-org/PixelRAG
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6765" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔐
VoidAuth
یک سرویس متن‌باز برای
SSO
و مدیریت کاربران در محیط‌های Self-Hosted.
ویژگی‌ها:
•
🌐
OIDC Provider
•
📖
LDAP Server
•
👥
مدیریت کاربران و گروه‌ها
•
🔑
MFA
و
Passkeys
•
📨
دعوت و ثبت‌نام کاربران
•
🎨
شخصی‌سازی رابط کاربری
•
🔒
رمزنگاری داده‌ها (
PostgreSQL
/
SQLite
)
⚠️
هنوز Audit امنیتی نشده؛ برای Production با بررسی کافی استفاده کنید.
🔗
https://github.com/voidauth/voidauth
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6764" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🖼
جستجوی معکوس تصویر با TinEye
اگر می‌خواهید منبع اصلی یک تصویر را پیدا کنید، نسخه‌های باکیفیت‌تر آن را ببینید یا وب‌سایت‌هایی که از آن استفاده کرده‌اند را پیدا کنید،
TinEye
یکی از بهترین موتورهای جستجوی معکوس تصویر است.
⚡️
قابلیت‌ها:
-
🔍
جستجو با آپلود تصویر یا وارد کردن لینک آن
-
🌐
پیدا کردن صفحات وبی که تصویر در آن‌ها منتشر شده است
-
🖼
شناسایی نسخه‌های ویرایش‌شده، برش‌خورده یا تغییر اندازه‌یافته
-
📈
مرتب‌سازی نتایج بر اساس اولین انتشار، جدیدترین، بزرگ‌ترین یا بیشترین تغییر
-
🔒
حفظ حریم خصوصی؛ تصاویر آپلودشده ذخیره یا ایندکس نمی‌شوند. TTinEye+1
🔗
وب‌سایت:
https://tineye.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6763" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6762">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2qIR7Zh1bnQ46JC-dnldX_XsDIO6MLsHc32Lp53xD0xPjiSgnetU87-xhIr0Ibc7Gi3LHMiMdIGL8l8KlRUELvj_N28x5GD8QDv9B7lUs6zjFMwd_mmXaWrcEggvklbo6_Vpvt_ThENwd3e16rejOXYAlrrtuAD_DzYD_enUb7-YmPrE-zE2IwGyhy5YBp4kzhcvx5mN4mLaqqzIRD1CvUNeAr6W5FmT_1JH2uIUUnscrc1PvrCBJX4gJtutl0QrxamDiXXodaCTNoRNeqnW9Xj6nAE5ZFUVhou2hEs_58eXp3w3X1-uNEkAGIghxS1Z0h-BZUb63F-uy0c5vnpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تولید صدا با Pocket TTS روی پردازنده معمولی (CPU)
این ابزار یک مدل
تبدیل متن به گفتار (TTS)
بسیار سبک با
۱۰۰ میلیون پارامتر
است که بدون نیاز به
GPU
، پرداخت هزینه
API
یا وابستگی به سرویس‌های ابری اجرا می‌شود.
⚡️
ویژگی‌های کلیدی:
-
🚀
تولید اولین بخش صدا در حدود
۲۰۰ میلی‌ثانیه
و تا
۶ برابر سریع‌تر از زمان واقعی
روی پردازنده‌های مک.
-
🎙
امکان
شبیه‌سازی صدا (Voice Cloning)
تنها با یک نمونه صدای
۵ ثانیه‌ای
.
-
🌍
پشتیبانی پیش‌فرض از
۶ زبان
: انگلیسی، فرانسوی، آلمانی، پرتغالی، ایتالیایی و اسپانیایی.
-
🔓
کاملاً
متن‌باز (Open Source)
با
لایسنس MIT
و آموزش‌دیده فقط با داده‌های عمومی.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6762" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXW3ry40l4t5ZHl49va46fctpdrkX8EblOqHntRk3d6S9fr7WC5T6Oqbh3dnOiWsRjyAhyg3IcEw-20yAQZzBs6bfaw7O_t2QwDmEtGlOWeQpK9FupfDmWHQuISgk_RdQPeBbJsFPji3J_tcG6fXEq6zcUPVIHHYr35GtcXpuhiJep32zPOzvYoxJXPOAcr56e7Or-BByxNtgf2_KcyIIJ_X0EHCvEpMqtXZ15Yex38PvmLnMM9x0gFihXRej8JpsRKQnlamCTwTya4V-vI4Kosx4Ze6GtHMpuJxruTK-Y528Hi5Z9Q-3y63icqa0-raMSE81zkwSxNw6loLQK-N2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به دنیای تکنولوژی، لینوکس، شبکه، سرور و ابزارای خفن علاقه‌مندین، یه سر به کانال لوکال هاست بزنین
توی localhost کلی آموزش، نکته کاربردی و تجربه واقعی از کار با سیستم‌ها هست. خلاصه هر چی از دل پروژه‌ها درمیاد، باهاتون به اشتراک می‌ذاره!
🅰
t.me/localhost_ir</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6761" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
