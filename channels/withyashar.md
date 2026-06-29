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
<img src="https://cdn4.telesco.pe/file/g2nn3WqY8y9A5w94Pqvx0RsUMtDBqLpDALBHluUUFbrowJBh6AjiPYn5aTdfFb_LcgS3L3_1XrWLPgy5CFWBDWUIMiagYvpdbKaExRzOfCTCVqqkjCkQTYFBpF-4LKLASFjGtiECvCXnD_hF97n2atcji7yL9FKhR3XOjCS8kY5YMOe3kK8fchlvmhDyjTLiU6DTgYuFXInV-uqBeKegRZwpmz4Q8rcl3_1Cxi6mGg7b0Ju_mDjlWepbQqN6uoaCSvZKC22Gkat0s5g4_FlgUVRhU0TeP-WljddVMvFw4qJeTXfQnXwXKi8ruXpgZrGJUjGSvCJRqnBHyNlJM0seCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 332K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 08:38:32</div>
<hr>

<div class="tg-post" id="msg-16126">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124ea90741.mp4?token=lR63zzwPsSyaLGbj8xh0t0HFW9cfaETWeJpvrBM4IkiiCtPHE5hkIbKTJBq6AhwK4Pv4hcitIfd5Q_XM7UX7OiIGIJ1w55thVslDwiVeBVN41OQ830dDdJNLNjkEEjZvXbu-e5pJzyJcDNUlUtquaCwOxILLmKMKOfx4YkFkLwX9Dfeoi5sFIU_PQCa4zWQ5qRr350vrod-LlzYTXjxE3LPQp9wdThHvcz701zoELjvE0Z5M0LVNrD4X9eB0cntHAB6mQNlcxpYaS5ogzAhyNuqvCQqGYpfhjqTtz8FUc9IOYKSIuHer6yXutoiwNsERnUpolefsIWFyCWp9gN_4wjZ0SBgpjbnLjrQLH1hGehOVDi3cbDyM_h0ePLnuFIs8VQCA-UjeJNzdJphB6iWrQjFaNeUOWTvBHeiYFKmQUBao9ErKEZ3SGGliWSnGAXyejQXqLbLMLkNSoCAFHzFls2laskFQa3tzm6NR2lDWUybjiq1E-sTDLmVFgvTLlrEUvWvpW3xI0MIL7lvjo5x0YhEfl7vDwUJBA4yOgYBqQFk8zO4rU-yPxtQFv8jD46UWxR-wp5mnf5TT-KXHkdvu4xjUnJtg895FEGl3ddWOfTJbU8yzSQ544KiodK1HLDgtuIZh13QihIhBUlf9a6-DBU4F4Va5qVHuRyozNKv09PI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124ea90741.mp4?token=lR63zzwPsSyaLGbj8xh0t0HFW9cfaETWeJpvrBM4IkiiCtPHE5hkIbKTJBq6AhwK4Pv4hcitIfd5Q_XM7UX7OiIGIJ1w55thVslDwiVeBVN41OQ830dDdJNLNjkEEjZvXbu-e5pJzyJcDNUlUtquaCwOxILLmKMKOfx4YkFkLwX9Dfeoi5sFIU_PQCa4zWQ5qRr350vrod-LlzYTXjxE3LPQp9wdThHvcz701zoELjvE0Z5M0LVNrD4X9eB0cntHAB6mQNlcxpYaS5ogzAhyNuqvCQqGYpfhjqTtz8FUc9IOYKSIuHer6yXutoiwNsERnUpolefsIWFyCWp9gN_4wjZ0SBgpjbnLjrQLH1hGehOVDi3cbDyM_h0ePLnuFIs8VQCA-UjeJNzdJphB6iWrQjFaNeUOWTvBHeiYFKmQUBao9ErKEZ3SGGliWSnGAXyejQXqLbLMLkNSoCAFHzFls2laskFQa3tzm6NR2lDWUybjiq1E-sTDLmVFgvTLlrEUvWvpW3xI0MIL7lvjo5x0YhEfl7vDwUJBA4yOgYBqQFk8zO4rU-yPxtQFv8jD46UWxR-wp5mnf5TT-KXHkdvu4xjUnJtg895FEGl3ddWOfTJbU8yzSQ544KiodK1HLDgtuIZh13QihIhBUlf9a6-DBU4F4Va5qVHuRyozNKv09PI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلیل آخرینم باش…
@withyashar</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/16126" target="_blank">📅 02:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16125">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سناتور جان کندی : ایران الان مثل یک پیرمرد خیلی پیر است که توانایی گرفتن سرماخوردگی را ندارد. ما آنها را به شدت تضعیف کرده‌ایم. نباید تسلیم شویم
برای من عدم توافق قابل قبول است؛ توافق بد قابل قبول نیست.
در پایان یک دوره زمانی معقول، ۶۰ روز یا هر چه که باشد، فکر می‌کنم باید دوباره وارد شویم و دوباره مثل گربه‌زن با آنها برخورد کنیم
باید آنها را بخوریم و استخوان‌ها را روی زمین تف کنیم
@withyashar
آخرش حرف منو میزنه منظورش اینه گربه گیرشون کنیم‌
😂
😂
😂</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/16125" target="_blank">📅 01:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16124">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/16124" target="_blank">📅 01:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16123">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📩
درخواست همکاری  اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:  نام یا لغب نوع فعالیت / حوزه کاری: سابقه کاری: آدرس لینکدین: (خیلی خوبه باشه) آدرس اینستاگرام: (اختیاری) آیدی…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/16123" target="_blank">📅 01:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16122">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه‌های افغانستان گزارش دادند پاکستان چند نقطه را در ولایت‌های کنر، پکتیا و پکتیکا هدف قرار داده است.
هم‌زمان، پاکستان اعلام کرد مواضعی را در مناطق مرزی با افغانستان هدف گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/16122" target="_blank">📅 01:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16121">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c21113c23.mp4?token=YpGQqbNu_aU1P9w8iI-dayPX285VymzE05DgFR8ghP8tiJ464J61kJ4-DGGw1BV9iI93t_59GY74vim-vCm9pbcQPGiDu4MiaGYtl47YSjOchhg7ewILFPwxK_waZM9iS2E2x78GiwtBvxBZ2AsOPIqxNQ34PjeG8ca18o5eobmpd_2-Ca6r1NcHIFJ7jlXW5Th8Ykl6mQKDjRRcrWwau96aZbHSpN8Vm_Ka-E3JoEFveSkO8KkoLvSY9RtIHIsVWrZ8F1y1hjbX4LBoBnB7ZqzHYWJXMccFsYDbHsR3NNy5nL7TTedZKmHOHtke4xGpTLERiFrwnNojdxJuMavtBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c21113c23.mp4?token=YpGQqbNu_aU1P9w8iI-dayPX285VymzE05DgFR8ghP8tiJ464J61kJ4-DGGw1BV9iI93t_59GY74vim-vCm9pbcQPGiDu4MiaGYtl47YSjOchhg7ewILFPwxK_waZM9iS2E2x78GiwtBvxBZ2AsOPIqxNQ34PjeG8ca18o5eobmpd_2-Ca6r1NcHIFJ7jlXW5Th8Ykl6mQKDjRRcrWwau96aZbHSpN8Vm_Ka-E3JoEFveSkO8KkoLvSY9RtIHIsVWrZ8F1y1hjbX4LBoBnB7ZqzHYWJXMccFsYDbHsR3NNy5nL7TTedZKmHOHtke4xGpTLERiFrwnNojdxJuMavtBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل فیلمی از انفجار تونل در منطقه مجدل، جنوب لبنان، منتشر کرد. ارتش اسرائیل اعلام کرد که این نیروها تونلی را که در واقع یک مجتمع زیرزمینی ساخته شده با استفاده از دانش و فناوری رژیم ایران بود، منهدم کردند. در داخل تونل صدها سلاح و چهار سکوی پرتاب به سمت خاک اسرائیل وجود داشت.
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/16121" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16120">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت کشور بحرین: در پی حمله ایران، یک ساختمان مسکونی در منطقه المحرق آسیب دید، اما هیچ خسارت انسانی در پی نداشت.       @withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/16120" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16119">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک منبع آگاه از مذاکرات گفت که قرار بود مذاکرات سه‌شنبه در ابتدا در سوئیس برای رسیدگی به برنامه هسته‌ای ایران برگزار شود. تشدید تنش‌ها آنها را به مکان دیگری منتقل کرد و دوباره بر تنگه هرمز متمرکز شد.  به گفته یک مقام آمریکایی و یک منبع آگاه، انتظار می‌رود…</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/16119" target="_blank">📅 00:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16118">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبرگزاری اردن: سپاه به دنبال ترور یکی از فرماندهان سنتکام بود که موفق نشد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/16118" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16117">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">من مشکل جدی فیزیکی‌ برام پیش اومده کمک خواستم ! همین ! کلت زیر گلو کسی نزاشتم که ! جم کنید مسخره بازی رو</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/16117" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16115">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اکسیوس: ایالات متحده و ایران توافق کردند حملات را متوقف کنند و در طول هفته آینده دیدار کنند، این را منابع آمریکایی به من اطلاع دادند. گزارش من در این موضوع @withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/16115" target="_blank">📅 00:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16114">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبرنگار اسرائیلی: ایران تونل‌های عظیمی در جنوب لبنان ساخته است.
مقادیر مواد منفجره‌ای که ارتش اسرائیل به این منطقه پمپاژ می‌کند، بیشتر از هر چیزی است که در تمام جبهه‌های جنگ وجود داشته است
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/16114" target="_blank">📅 23:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16113">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اکسیوس: ایالات متحده و ایران توافق کردند حملات را متوقف کنند و در طول هفته آینده دیدار کنند، این را منابع آمریکایی به من اطلاع دادند. گزارش من در این موضوع
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/16113" target="_blank">📅 23:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16112">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📩
درخواست همکاری
اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:
نام یا لغب
نوع فعالیت / حوزه کاری:
سابقه کاری:
آدرس لینکدین:
(خیلی خوبه باشه)
آدرس اینستاگرام:
(اختیاری)
آیدی تلگرام:*
(الزامی)
توضیحات:
لطفاً تخصص‌ها، مهارت‌ها، سوابق و توانایی‌های خود را به‌صورت مختصر معرفی کنید.
لطفاً اطلاعات را فقط برای دایرکت همین چنل ارسال کنید
ادمین (خبری، بازار های مالی،گیم،موزیک، ورزشی)
برنامه نویس
و کسی که بتونه ویکیپدیا بیاره بالا
ویدیو ساز فقط با هوش مصنوعی
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/16112" target="_blank">📅 23:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16111">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اتاق جنگ با یاشار : الان جریان اینه که اسرائیل میخواد تونلهایی که حزبالله با کمک ایران ساخته رو منفجر کنه و برای این کار از دو برابر مواد منفجره معمول میخواد استفاده کنه که کاملاً نابود بشن. در نتیجه هشدار دادن به مردم شمال اسرائیل که شما ممکنه حتی یک زلزله…</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/16111" target="_blank">📅 23:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16110">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتاق جنگ با یاشار : الان جریان اینه که اسرائیل میخواد تونلهایی که حزبالله با کمک ایران ساخته رو منفجر کنه و برای این کار از دو برابر مواد منفجره معمول میخواد استفاده کنه که کاملاً نابود بشن. در نتیجه هشدار دادن به مردم شمال اسرائیل که شما ممکنه حتی یک زلزله خفیف رو احساس کنید. از سمت دیگه حزب الله اخطار داده که با این کار تنشها تشدید خواهد شد. خواهیم دید چه میشود.
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16110" target="_blank">📅 23:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16109">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نخست‌وزیر بنیامین نتانیاهو و وزیر دفاع اسرائیل کاتز در بیانیه‌ای مشترک: "در چارچوب عملیات «پایان جمله»، ارتش اسرائیل اکنون زیرساخت تروریسم زیرزمینی حزب‌الله را در منطقه روستای مجدل زون در جنوب لبنان نابود کرد. اسرائیل پیشاپیش آمریکا را مطلع کرده است"
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/16109" target="_blank">📅 23:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16108">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کانال ۱۴ ، جنجال در کابینه: به دیوید زینی، رئیس شین بت، دستور داده شد تا تحقیقات در مورد نشت عملیات «غرش شیران» به اخبار کانال ۱۲ را (علیرغم مخالفت مشاور حقوقی) پیش ببرد.
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16108" target="_blank">📅 23:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16107">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فضائلی، عضو دفتر حفظ و نشر آثار آیت الله خامنه ای: امروز قرار بود مذاکرات فنی برگزار شود که ایران آن را لغو کرد و شرکت نکرد که دلیل این امر درگیری‌های این چند شب گذشته بود و دلیل دیگر این است که منتظر اجرای برخی شروط هستند که مثلا امکان برداشت پول‌های بلوکه شده است یا خیر
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16107" target="_blank">📅 23:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16106">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش ها از رهگیری چند موشک برفراز اردن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/16106" target="_blank">📅 23:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16105">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزارت خارجه اسرائیل :
شادی مردم ایران از حذف تیم جمهوری اسلامی یک چیز را نشان میدهد: انزجار و بیزاری مردم از چیزی که به رژیم مربوط میشود
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/16105" target="_blank">📅 23:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16104">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هم اکنون اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/16104" target="_blank">📅 22:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16103">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یک مقام ارشد دولت ترامپ امروز به رسانه‌ها اعلام کرد که مذاکرات میان آمریکا و ایران که قرار است آخر هفته جاری در سوئیس برگزار شود، همچنان طبق برنامه انجام خواهد شد
این اظهارات، گزارش پیشین روزنامه وال‌استریت ژورنال را رد می‌کند؛ گزارشی که مدعی شده بود این مذاکرات به دلیل دور جدید حملات متقابل ایران و آمریکا در منطقه خلیج فارس به تعویق افتاده است.
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/16103" target="_blank">📅 22:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16102">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0003b579.mp4?token=J8tL1YkeEVg2p9p2GlkQiF_Yg7JALuAMHwhKssdh9UQ79CKF3Wu6vnceIcn4BTotfZWyPKYnZKq6o67FdgSykZgpUED1hPoKUMMJHqTTjyEZ8rvzuOXGaUhyxsasVn614VvY85RR3k6s7-8-Dk2j68fJWnpmIxwWWj0HORf6AGpaUz2xwjBr4yG7wpZMpGaGshSxuMDADAyT89u3GxjhCFUQQzFhlWaxZ6dcXZRS6Q8Wi3T-JzZo-x0_2rU7pF-7JxcxII6LXkO-7DxZQh8N5lE40tHvYuPHaQq7E5HuMpN4p1oEuhEMcVLGy7AjN22G-WUgAuU0rNhtrlQwo4yaJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0003b579.mp4?token=J8tL1YkeEVg2p9p2GlkQiF_Yg7JALuAMHwhKssdh9UQ79CKF3Wu6vnceIcn4BTotfZWyPKYnZKq6o67FdgSykZgpUED1hPoKUMMJHqTTjyEZ8rvzuOXGaUhyxsasVn614VvY85RR3k6s7-8-Dk2j68fJWnpmIxwWWj0HORf6AGpaUz2xwjBr4yG7wpZMpGaGshSxuMDADAyT89u3GxjhCFUQQzFhlWaxZ6dcXZRS6Q8Wi3T-JzZo-x0_2rU7pF-7JxcxII6LXkO-7DxZQh8N5lE40tHvYuPHaQq7E5HuMpN4p1oEuhEMcVLGy7AjN22G-WUgAuU0rNhtrlQwo4yaJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار ۱۷۵،۰۰۰
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/16102" target="_blank">📅 22:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16100">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/16100" target="_blank">📅 22:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16099">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">والانیوز عبری
: اسرائیل در حال آماده شدن برای احتمال حمله مستقیم ایران است، پس از امضای توافق لبنان و اسرائیل
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/16099" target="_blank">📅 22:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16098">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">امروز تولد ۵۵ سالگی ایلان ماسک، ثروتمندترین فرد جهان هست
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16098" target="_blank">📅 22:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16097">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دیدبان اتاق جنگ : هواپیمای c 130  هرکولس ارتش نشست مهرآباد
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/16097" target="_blank">📅 22:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16096">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارشاتی از شلیک موشک‌ از ایران به سمت اردن @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16096" target="_blank">📅 22:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16095">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارشاتی از شلیک موشک‌ از ایران به سمت اردن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16095" target="_blank">📅 21:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16094">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">افزایش حالت آماده‌باش در اسرائیل به دلیل نگرانی از پرتاب موشک از ایران
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/16094" target="_blank">📅 21:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16093">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920d7be6f9.mp4?token=h38IvEjjFuzfzdND6tradKz8VpKJCnQ2vCUC_S64SgEDNP65fG4nIQpKVRkxUnvUPEAhbtuZgldVM1tFEnUe-khRvf-HXKdxbR1HvKsr9MAGhFT28cE19HMdmQQAI7HVC3ly1r_vdm6LNqOVT23lyiDnxe-Q_OGe2UYAGbpP_h3cB2fBOCGz90N6SIXeaeDadbgE4PDW_2OVEe0H-fkAyRuATQwcJR3SFbXZu9eF3lWZ8betc22xr13CyXcIfTRSDgMNlItxjzTOFncL6tz_QTzjuR6SbE9K1vbpLtCouPQWQGBLA1Vm8lPWLXna7E2-sZR47uDPDKnP-TLE1hlGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920d7be6f9.mp4?token=h38IvEjjFuzfzdND6tradKz8VpKJCnQ2vCUC_S64SgEDNP65fG4nIQpKVRkxUnvUPEAhbtuZgldVM1tFEnUe-khRvf-HXKdxbR1HvKsr9MAGhFT28cE19HMdmQQAI7HVC3ly1r_vdm6LNqOVT23lyiDnxe-Q_OGe2UYAGbpP_h3cB2fBOCGz90N6SIXeaeDadbgE4PDW_2OVEe0H-fkAyRuATQwcJR3SFbXZu9eF3lWZ8betc22xr13CyXcIfTRSDgMNlItxjzTOFncL6tz_QTzjuR6SbE9K1vbpLtCouPQWQGBLA1Vm8lPWLXna7E2-sZR47uDPDKnP-TLE1hlGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل:
اگر ایران فکر کنه ترامپ قراره در برابر ادامه حمله به کشتی‌های بین‌المللی دست روی دست بزاره، کاملاً در اشتباهه؛ چون همین چند شب اخیر نشون داد که این کارها رو بی‌پاسخ نمی‌ذاره.
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16093" target="_blank">📅 21:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16092">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به گزارش i24NEWS، ایران هر شب حداقل شش پهپاد را به سمت کشتی‌های تجاری در تنگه هرمز پرتاب می‌کند که برخی از این پهپادها توسط ارتش ایالات متحده رهگیری شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16092" target="_blank">📅 21:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تایید خبر توسط ایران: مذاکرات به دلیل حمله آمریکا به ایران لغو شده است  @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16091" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16090">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شبکه ۱۲ عبری:
توافق میان اسرائیل و لبنان که متن کامل آن، از جمله در وب‌سایت وزارت خارجه آمریکا، منتشر شده است، دارای یک
پیوست امنیتی محرمانه
نیز بوده که همچنان طبقه‌بندی‌شده باقی مانده است. دلیل اصلی محرمانه ماندن این پیوست، درخواست صریح دولت لبنان عنوان شده است.
هیچ‌گونه عقب‌نشینی خودکار و زمان‌بندی‌شده‌ای وجود نخواهد داشت
؛ بلکه هرگونه عقب‌نشینی یا اجرای تعهدات، بر اساس میزان موفقیت در میدان و ارزیابی نتایج عملی انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16090" target="_blank">📅 20:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16089">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وال استریت ژورنال: مذاکراتی که قرار بود این هفته بین واشنگتن و تهران در سوئیس برگزار شود، پس از تبادل حملات دیشب متوقف شد. @withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16089" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16088">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اکسیوس: اسرائیل و لبنان به این نتیجه رسیدن که برای جلوگیری از دخالت جمهوری اسلامی باید توافق کنن.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16088" target="_blank">📅 19:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16087">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هم اکنون نیروهای زمینی سپاه مواضع گروه کرد در کردستان عراق را با توپخانه هدف قرار دادند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16087" target="_blank">📅 19:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16086">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وال استریت ژورنال: مذاکراتی که قرار بود این هفته بین واشنگتن و تهران در سوئیس برگزار شود، پس از تبادل حملات دیشب متوقف شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/16086" target="_blank">📅 19:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16085" target="_blank">📅 19:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16084">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دلار و تتر ۱۷۲،۵۰۰
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/16084" target="_blank">📅 19:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">طالبان افزایش قیمت اینترنت را ممنوع کرد
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16083" target="_blank">📅 19:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">https://t.me/boost/withyashar
این بوستو بترکونین ایموجی اضافه کنم
😕</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/withyashar/16082" target="_blank">📅 18:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16081">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مجتبی خامنه‌ای بیانیه‌ای منتشر کرد که در آن خواستار اصلاحات گسترده قضایی، اقدام سختگیرانه‌تر علیه فساد و ادامه پیگیری پرونده‌های حقوقی درباره جنایات جنگی آمریکا و اسرائیل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/16081" target="_blank">📅 18:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16080">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba88b4582.mp4?token=YF0sBFA2BsZfRNYJUApRIp2lQI3nGn5LgLxBJdVP1hB3Hx0bMysUrLpWkDZ4kQrG3kLIhFFB4Yz4V15DevrJAmakJuQ-0hEe6N6a1FIaXsbXh7HaczHvmz92Z4Ar2BbtyKMw_vRTzqnKlJRkurnbZOmLyFTWBE1rVtV-5EmcgBUp-rsFzCNXiVIZXu_M3G5E7tltkrwGV3-rlCVfCHETV7BrpDlOCFIyx4FkfmlC2VV2r0mxWqkgdn5eUQxckH8Qf-LtNZF3mTRjuLlIxIO9VmG2dtnp5CtScPc2ZZl3CwZGCUVqpNP6P3grcsagdKkzwKYFlJBrfKMTMtlPC9uYLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba88b4582.mp4?token=YF0sBFA2BsZfRNYJUApRIp2lQI3nGn5LgLxBJdVP1hB3Hx0bMysUrLpWkDZ4kQrG3kLIhFFB4Yz4V15DevrJAmakJuQ-0hEe6N6a1FIaXsbXh7HaczHvmz92Z4Ar2BbtyKMw_vRTzqnKlJRkurnbZOmLyFTWBE1rVtV-5EmcgBUp-rsFzCNXiVIZXu_M3G5E7tltkrwGV3-rlCVfCHETV7BrpDlOCFIyx4FkfmlC2VV2r0mxWqkgdn5eUQxckH8Qf-LtNZF3mTRjuLlIxIO9VmG2dtnp5CtScPc2ZZl3CwZGCUVqpNP6P3grcsagdKkzwKYFlJBrfKMTMtlPC9uYLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما: تا پیروزی کامل بر دشمن باید جنگ کنیم؛
جمشیدی، کارشناس صداوسیما: جنگ نیمه کاره به صلاح نیست؛ باید به نقطه بازدارندگی مطلق؛ سلطه و تفوق برسیم؛
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16080" target="_blank">📅 18:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16079">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبرگزاری رسمی عراق: کارزار نخست‌وزیر برای تعقیب و بازداشت متهمان به فساد ادامه دارد، تا کنون 47 نفر از نمایندگان و مقام‌های دولتی به اتهام فساد بازداشت شده‌اند. @withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16079" target="_blank">📅 18:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16078">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بنابر اعلام منابع میدانی،در محور پیرانشهر به مهاباد درگیری بین رژیم و گروه کرد ها رخ داده
درگیری در اطراف روستای گاگش در محدوده مهاباد رخ داده و طبق اطلاعات منابع میدانی عامل این حمله گروهک کرد پژاک عنوان شده
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16078" target="_blank">📅 18:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16077">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/16077" target="_blank">📅 18:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16076">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سخنگوی ارتش ایران : ما برنامه‌های جدی در دو حوزه داریم: تولید داخلی و تأمین تجهیزات پیشرفته از کشورهای دوست.ما قطعاً در روزهای آینده به سیستم‌های پیشرفته‌تری مجهز خواهیم شد.
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/16076" target="_blank">📅 18:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16075">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ادعای کانال ۱۴ اسرائیل: در توافقنامه هیچ جدول زمانی برای خروج وجود ندارد و هیچ چیزی اسرائیل را به آن ملزم نمی‌کند.
در واقع این یک توافقنامه بسیار خوب است، اما حزب‌الله از این بابت عصبانی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/16075" target="_blank">📅 17:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16074">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فارس: جمهوری اسلامی در دوران گذار به نظم جدید جهانی، چاره‌ای جز ساخت بمب اتم نداره تا گزینه نظامی علیه کشور از روی میز برداشته بشه.
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/16074" target="_blank">📅 17:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16073">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فارس: ۶۲ نماینده مجلس که که پیش‌تر اعلام کرده بودند روز یکشنبه مقابل مجلس حضور خواهند یافت، برنامه را لغو کردند
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16073" target="_blank">📅 17:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حقیقت : نیروهای امنیتی عراق یک عملیات بزرگ ضد فساد اجرا کردند این عملیات در منطقه امنیتی «سبز بغداد» انجام شد چندین مقام سیاسی، نماینده پارلمان و مسئول دولتی بازداشت شدند برخی گزارش‌ها می‌گویند تعداد بازداشت‌ها بین ۷ تا بیش از ۱۰ نفر بوده و در برخی منابع غیررسمی…</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/16072" target="_blank">📅 17:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16071">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گاردین و افشای سندی محرمانه؛ خیز «هیات صلح» ترامپ برای کسب مصونیت مطلق قضایی در غزه
پیش‌نویس قطعنامه‌ای که به دست روزنامه «گاردین» رسیده نشان می‌دهد «هیات صلح» مورد حمایت سازمان ملل که دونالد ترامپ اوایل سال جاری میلادی برای اداره غزه تشکیل داد در پی اعطای مصونیت حقوقیِ گسترده‌ به خود است.
به گزارش گاردین، متن به‌کاررفته در پیش‌نویس همچنین به این نهاد اجازه می‌دهد تا اموال عمومی در غزه را «به‌طور رایگان» در اختیار بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16071" target="_blank">📅 16:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16070">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس:
ممکن است ترامپ به زودی دامنه جنگ را تشدید کند و تفاهم نامه با ایران را پاره کند
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16070" target="_blank">📅 16:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16069">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حقیقت : نیروهای امنیتی عراق یک
عملیات بزرگ ضد فساد
اجرا کردند
این عملیات در
منطقه امنیتی «سبز بغداد»
انجام شد
چندین مقام سیاسی، نماینده پارلمان و مسئول دولتی بازداشت شدند
برخی گزارش‌ها می‌گویند تعداد بازداشت‌ها بین ۷ تا بیش از ۱۰ نفر بوده و در برخی منابع غیررسمی عددهای بالاتر هم گفته شده
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16069" target="_blank">📅 16:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16068">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رئیس جمهور و نخست وزیر عراق دیشب کودتا کردن هم یک خبر فیک نیوزه !!!</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/16068" target="_blank">📅 16:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16067">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پست ترامپ مبنی بر‌ اینکه مسی بهترین بازیکنه فیک نیوز هست !</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/16067" target="_blank">📅 16:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16066">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">زلزله مازندران
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16066" target="_blank">📅 16:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16065">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">زلزله مازندران
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16065" target="_blank">📅 16:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16064">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فایننشال تایمز به نقل از یک دیپلمات گزارش داد که میانجی‌ها در حال انجام گفت‌وگو با طرف‌های درگیر [ایران و آمریکا] هستند تا تلاش کنند تنش‌ها را کاهش دهند.
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/16064" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16063">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هاآرتص: سامانه‌های دفاعی اسرائیلی به قطر و عربستان سعودی فروخته شده‌اند؛ با وجود اینکه هیچ‌یک از این دو کشور روابط دیپلماتیک رسمی با اسرائیل ندارند
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/16063" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16062">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اولین پارکینگ ‌پناهگاه تهران به پایان رسید
شهردار منطقه ۱۰: ساخت اولین پارکینگ پناهگاه تهران در یکی از مناطق پرجمعیت و پرتراکم تهران به اتمام رسید و بزودی بهره‌برداری از آن آغاز می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16062" target="_blank">📅 13:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عراقچی رفته عراق ستاد مشترک تشکیل داده برای تشییع جنازه !   عراقچی : جنازه علی خامنه‌ای در بغداد، کاظمین، کربلا و نجف تشییع میشه @withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/16061" target="_blank">📅 13:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16060">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عراقچی رفته عراق ستاد مشترک تشکیل داده برای تشییع جنازه !
عراقچی
: جنازه علی خامنه‌ای در بغداد، کاظمین، کربلا و نجف تشییع میشه
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16060" target="_blank">📅 13:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16059">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KILgQQfqpfiV-SnrN6QzUScNOupdYrYRG-05eM7WCNTSoFPN7NJM528DtNazx99OdRkZ8AWF6aX8bvCk-lDrLGJ_quTHQIPnBokKO-nc-NrUAEnFKp4mR6FTNLrxWrNo-vWMz4eJ1dbwC26X4dZ5ZGvOxcB4eHMf2eoyeZjqBZmE5y_sh8jBj1YsSZp6cso8-dFYElBYry0MVnDFTUBsG7OHQGNbw2XuJf96jhmQKeFUmLVsz4lAAFe6SK5OLWouKn-w5XXjCHC8vqDD-lvgmAgS1HWP0HDgoSDgyoGlBGqHdB0o8iBqCmKYNsIQ3dNdZ9KlnlD1l5NAXYlGEQ5ISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری خواهر جاویدنام
صهبا رشتیان
،
داور بین‌المللی
که در اعتراضات دی ماه، جونشو اهدا کرد.
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16059" target="_blank">📅 12:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16058">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoZefPS-hGGdiLY7kbwk2Su3-CdiyHGPS49tilwRIuC7kj1z1A9VBW0wqNOKNVk5ckLURbJu8Rvhmd8O2mBBOlBd_GpRULWUS_K9CLGF9zF7_1s6m2-VNq4iESFa0gbw_eQXgFfhyrHDYjLRKDp7ZqEhanTwn2xa-4fpFlNN7xAD8fbujM6_yQZj3Nr_681PvNpUJXshaOnm6FD8qPsaC66Avd35UucQ27nqZlNz46-Z0Yp6ZM3JjRJKVfSQdyZ5fPPVDeEf61TLRUnpe70swJ1Oh76OCxYBoRVJ5OcHuv5PLN4f0rYCZtKFRrYw7fISC6EApKbTNtCb5w-4PzeB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16058" target="_blank">📅 12:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16057">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">در ساعت ۲۰:۳۰ هفتم تیر ۱۳۶۰ ( دقیق ۴۵ سال پیش و همین روز یکشنبه ) جلسه‌ای در سالن اجتماعات دفتر مرکزی حزب جمهوری اسلامی واقع در محله سرچشمه تهران و در جلسه‌ای که برای بررسی انتخابات ریاست جمهوری آینده برگزار می‌شد، بمبگزاری با ۲ بمب رخ داد که منجر به کشته‌شدن ۷٣ نفر از وزرای دولت، نمایندگان مجلس شورای اسلامی و اعضای حزب جمهوری اسلامی شد. سید محمد بهشتی رئیس قوه قضائیه و دبیرکل حزب جمهوری اسلامی از جمله کشته‌شدگان بود.
میدان هفتم تیر در تهران، به عنوان یادبود این حادثه نام‌گذاری شده است.
توسط سازمان مجاهدین خلق ایران و عامل انفجار ، محمدرضا کلاهی بود
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16057" target="_blank">📅 11:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16056">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16056" target="_blank">📅 11:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16055">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzAgiqxcgMY7RAnZhpWTUlW8hE5DdFLdU4k7zAd-Zo9XFKIShTPkmA0LgBKuCv_ymBWpeu8rK4XlLZTefhrcBsbnepFDuuh1MN5meHZ7itIEzfHyuzh0ERRFztR3WKH1ecZwEVjBoNY5XnVrQGAdDmDLytvNWKpBUkTnBVq1Vk3W1k0c1fTDsKikAsG6XUafxbW6PdLreQfatg45CdRQVsmLzsYuyL2a3YxwMIUnVeSE0Zc4NCVb2tN3fKQyav2BHZdfaCCB0yqG_9p7Rk9ZR16BIu65oXidEygNo1DHvXmvMWbghLMPyyhj_76k45JU30BFcj3rxkUd69W9q_1PBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیر اینگونه عجیب رقم خورد تا چهره میثاقی بشه تراپی
- ساعت 00:30 اومد گفت اقا غنا کرواسی رو ببره رفتیم مرحله بعد؛ نتیجه؟ غنا بازیو باخت
- ساعت 03:30 اومد گفت اقا این دفعه ازبکستان نبازه ما صعود کردیم؛ نتیجه؟ ازبکستان بازیو باخت
- ساعت 05:30 اومد گفت اقا این بازی برنده داشته باشه ما تو جام می مونیم؛ نتیجه؟ بازی مساوی شد
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16055" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16054">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">1$ Tether = 171,000 Toman
@withyashar
🚨</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/16054" target="_blank">📅 10:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16053">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه هنوز برات عجیبه پس این کد رو ببین ، تیم جمهوری اسلامی   ۳مسابقه + ۳تساوی + ۳امتیاز + ۳گل زده + ۳گل خورده  + ۳گل مردود = ۱۸ , که میشه روز ا‌ول کشتار جاوید نام ها  درجواب رامین و قلعه نویی و اون کفتار شغال شلیل زاده  که قرار بود به جنازه…</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16053" target="_blank">📅 10:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16052">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVDOoh3xLBfWmDgdPfZ9WatuDPK-O2Xz9Rn05biitXMU3CS6SXWaE4uUsdu0y7Ap4blGO6nYjNADRsmjBr_dkQddb19DWp442WvOfP1tC3Ca5O1AK-CqeWsrK7aEHgw1GApVTNPnxisXMNKZz6zE6JuesNQFhh0h8Omwx8ItXaBMWaIMZ0qv9H27Y9GfKFyJYkpixQeXquSMnW0t163Loo4uWcpFLgPPrjU3HcwbysheYAfuNjZjIHaTO2gzAHUhIyrRgilyIUAn8Cqu6CUwEf_kFk3S9tOi3l0-_5zeUSKlUQVpzUtnwrGEY0fiL6e3bXJ-Wbljr2ytM7zJ3COKZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله هوایی ارتش اسرائیل به الخیام در  جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16052" target="_blank">📅 10:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16051">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه هنوز برات عجیبه پس این کد رو ببین ، تیم جمهوری اسلامی
۳مسابقه
+
۳تساوی
+
۳امتیاز
+
۳گل زده
+
۳گل خورده
+
۳گل مردود
= ۱۸ , که میشه روز ا‌ول کشتار جاوید نام ها
درجواب رامین و قلعه نویی و اون کفتار شغال شلیل زاده  که قرار بود به جنازه رهبرش تقدیم کنه
@withyashar
اگه شما نمیدونید ما میدونیم واسه چیه ویا اینکه چرا خدا باهاتون سازگار نیست
پاینده ایران</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/16051" target="_blank">📅 10:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16050">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7Z_fZvhj2ANBUEBdvwG3rSl1CGB1YfOYLNj_wzxo5w0frdA0hzmGVbfLgMSLLfvfPdZCbwdiqY9iBXhbg9m7YS2N36JLJk32e9mV5HJ_hG8r8YjXKWvP7Q5ADsObV0JgFCI_EmZwG7xeayz3MTQxy6dZKoDRVR7iyKASRr3PIgIrOzxsgrIUL1CIoxKralwyWqAIMS8FK4f8S--TONsicyzL7hm9cSgttgNEig-DxlMQznK6TTy0mYqnu6Mn3yUzf-7fRloMTiVYXcSe0IE_LRgbFAdqGXzbG4BbxLRy8kpLkNixB-F4rzPdilPf1yCOnS9e3tqLUsRcy3fI8z6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت کشور بحرین: در پی حمله ایران، یک ساختمان مسکونی در منطقه المحرق آسیب دید، اما هیچ خسارت انسانی در پی نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/16050" target="_blank">📅 10:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16049">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اتاق جنگ با یاشار : صعود تیم جمهوری اسلامی رو به فرودگاه إمام لعنت الله تبریک عرض میکنم
😂
😂
😂
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16049" target="_blank">📅 10:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16048">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اتریش و الجزیره هم ۳ بر ۳ شدن تیم ملا حذف شد
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/16048" target="_blank">📅 09:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16047">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5328c12b8e.mp4?token=MClT3D1FJJU32TMNAQym38bSoRbi74V2EsDrKRoqh08uxSuTWKQ1DL5Ez4esggHBMrUHgxhxtg9oPm36pmE7TG1Iv5Fh51fNcnArPOeEEhm_QPGrm2O2Xlneh6bdmKVdyTzKc0Askx7n-Bz26qIoq5KVlrwpLQ8xEzQMPIHxj6qFLVQL4x5yvTbfe-Lfh4KDaTQwMvK3RpbZHEErqh2-HbSbh6y1OI5Cu_iph_Da33CpnreZbIkLLEec3gV3cHHVy1Hj9IzApWKVI77xlOuaORlLIHjhMdCtRjeuEaH2uoqoeq1_Qbb8Sqzd4I7q3jEJjRxXm_q5ewPANbMMgqvXaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5328c12b8e.mp4?token=MClT3D1FJJU32TMNAQym38bSoRbi74V2EsDrKRoqh08uxSuTWKQ1DL5Ez4esggHBMrUHgxhxtg9oPm36pmE7TG1Iv5Fh51fNcnArPOeEEhm_QPGrm2O2Xlneh6bdmKVdyTzKc0Askx7n-Bz26qIoq5KVlrwpLQ8xEzQMPIHxj6qFLVQL4x5yvTbfe-Lfh4KDaTQwMvK3RpbZHEErqh2-HbSbh6y1OI5Cu_iph_Da33CpnreZbIkLLEec3gV3cHHVy1Hj9IzApWKVI77xlOuaORlLIHjhMdCtRjeuEaH2uoqoeq1_Qbb8Sqzd4I7q3jEJjRxXm_q5ewPANbMMgqvXaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات هوایی ساعات آغازین امروز آمریکا به زیرساختهای رژیم
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16047" target="_blank">📅 09:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16046">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ارتش اسرائیل: عبدالرحمن ماهر زیاده، فرمانده هسته النخبه در حماس، را کشتیم.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16046" target="_blank">📅 09:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16045">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرنگار العربیه: عباس عراقیچی، وزیر خارجه ایران وارد بغداد شد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16045" target="_blank">📅 09:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16044">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گل دوم کنگو توسط مایله در دقیقه 78
🇺🇿
ازبکستان 1
🇨🇩
کنگو 2  با این نتیجه دومین شانس تیک ملا هم از بین میرود  و فقط یک جون دارد @withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16044" target="_blank">📅 04:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16043">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صدا های انفجار مانند از بوشهر ، یا داره میزنه یا میخوره ، یه خبری هست
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16043" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16042">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حمله‌های متعدد ازبکستان روی دروازه کنگو  ازبکستان
1️⃣
-
0️⃣
کنگو  با این نتیجه تیم ملی صعود میکند
🚨
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16042" target="_blank">📅 04:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16041">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZsK1HuLYTwbxGjeoNh3apu3Xky0avIEul-abPvjj2kZAbnf-s2YUS9Zq0bF9DmWD7tvtEqYljW4Ip-9i42IAqHvIC9l_DcpUH0Woid0yexIfVaLG3r3j6zeXQM9qcldbTpO_SuXsCT1ERHSeMjDirK5PuwZ-kvzfUwtk9uwAYuxsxhI9hxQvjeQHAd61QvQyK6l0e60_622LeFzpfW6vuODDZ8hLKsE5ULW6AAM5F4y7uZomt-EjFhjJUuPWKVagmjk8-JEuzD3c682VOmKB-CyJx5ENuNcrRy6XqvidoiG5Q_ZWKEeuyJ7KyvC1o4ZXZ_tzA4pD2YmqqwPdiFnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک شیء ناشناس در آسمان بحرین در حال پرواز است.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16041" target="_blank">📅 04:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16040">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی در بیانیه‌ای اعلام کرد نیروهای دریایی و هوافضای این نهاد، در پاسخ به آنچه «تجاوزهای اخیر آمریکا» عنوان شده، عملیاتی مشترک با استفاده از موشک‌های بالستیک و پهپاد علیه چند هدف نظامی انجام داده‌اند.
در این بیانیه ادعا شده است که در ساعات اولیه بامداد یکشنبه، چند زیرساخت مرتبط با نیروهای آمریکایی در منطقه از جمله در کویت و بحرین هدف قرار گرفته و «منهدم» شده‌اند. همچنین به حملاتی از سوی آمریکا به برخی نقاط ساحلی ایران اشاره و تأکید شده است که در آینده برخورد با کشتی‌های متخلف در تنگه هرمز با شدت بیشتری انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16040" target="_blank">📅 04:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16038">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">موشک‌ها در آسمان بحرین در حال پرواز هستند و پدافند هوایی نیز درگیر شده
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/16038" target="_blank">📅 03:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16037">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اطراف بندرعباس شهر تازیانپ روستای خونسرخ صدای چندین انفجار ، قشنگ لرزید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/16037" target="_blank">📅 03:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16036">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حمله‌ای جدید این بار با موشک در بحرین.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16036" target="_blank">📅 03:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16035">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16035" target="_blank">📅 03:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16034">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پدافند کویت فعال شده
چندین انفجار شنیده شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16034" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16033">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">صدای آژیر هشدار در کویت
برخی گزارش‌های تاییدنشده از فعال شدن آژیر هشدار در کویت حکایت دارند.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16033" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16032">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16032" target="_blank">📅 03:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16031">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش رسانه‌های خبری رژیم حاکی است که پایگاه هوایی «شیخ عیسی» در بحرین هدف حمله پهپادی قرار گرفته است
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16031" target="_blank">📅 03:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16030">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ در تروث: هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران، و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!  بسیار محتمل است که آن‌ها هرگز درس نگیرند!  ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار…</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16030" target="_blank">📅 02:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxgMNUbZiuGN5Rov_F9eytUfF8ePBbxsv3tJvy8bcpBvKu3fx4mjhAlHUWYR_iAvYh0KwS3AkxBgEjGxfsgbchDZHuMBwJl8PggoWsEySFXy80nxM2b-hZygx1j74KpE8feonykHjIKhgnK_TKQU6dTeY1IY0iv0LDAOKwcNq3CDBcrYtBos4cLsTO6ZakRbbivIFl39ve5NLpk7PawPsHBPOK6dhKgDZPLxldwhiSSWUrkKW5fyoTcSUktQs_G4h7nXqUUkbdz-6cu02DSVYdCdGrdWWe08XhnQicdlANkYA7P2iCVGOQFeJ75VekIVninsBp0pBsJQX4QmK-R2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران، و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/16029" target="_blank">📅 02:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/16028" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">صداوسیما : جزئیات عملیات امشب رزمندگان نیروی دریایی سپاه علیه متجاوزان آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/16027" target="_blank">📅 02:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صداوسیما:  شناورهایی قصد داشتند از مسیرهای غیرقانونی و ناایمن جنوب تنگه هرمز عبور کنند که نیروی دریایی سپاه پاسداران با آن‌ها برخورد کرده بود
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/16026" target="_blank">📅 02:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وال‌استریت ژورنال : یک پهپاد ایرانی به نفتکشی حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز اصابت کرد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/16025" target="_blank">📅 02:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/16024" target="_blank">📅 02:18 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
