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
<img src="https://cdn4.telesco.pe/file/brXB60FjS3BZY9TZbHFrX1raRACsh4KzFgryTQ7uGkFymfjfxs2WaJ3vOIX-uoplUtjIPWCtFf8EVNsWDvdPOcC6MNGN_pO2ScWWVV79AtemOhAvSLMt6faPuqZ-evioaXDdU-zI9nGHI-r40k-7cyYOXGbDZ5Yf6qVxTmGxyCN-2x_m2dEO_zgt9QhUrT8x6O39Oov0v7DqNaDlCAJKc8yHob-UEO3wRFfsW28_8k4yKFIUywn4rdiuVj2GMLayYZOzo5VizwU1ps6puqTZz5EEft_VPNghJ2jO_haEy-6mCr-CbLALCZK2HhSL2Lqfx3kZhRyifEHREvjRmgymZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.86M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-460963">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
العربیه: اسرائیل در ۲ حملۀ هوایی، مجددا منطقۀ نبطیه‌فوقا در جنوب لبنان را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/farsna/460963" target="_blank">📅 21:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460962">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRSa0rbGbRyzzVm9-GDvMcvNOFNARFpgkboFG0hc1kMfGyZnEKQ5WkSc6X5-xLVYO9Fba3p7CQREtl4U3T1XJv4vWwuzPNGjwfShWCURof_Ri7lfwn9wfPexSrXeDoSKh7TR8VdtmILc7qpVaREJaLu5Q4ZIitXGSdLCEkPaSs_gqbPZpz-CSmAWLYjLidhSFtsOE0Iodc0D0nsWA3Dr_wMSr5EgLn0KoTijPT0GUlKaj_K1gQ9n79AtqoFKIt-Ghppg7fbL3STzI5-q6si_83_5kxC-XKVTt--RAo9tDzArwEnwKQXstZ8i-jPjp6SEhZyqLlAL9jb9xds0Luz3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت کندی اینترنت در ساعات گذشته
🔹
مدیرعامل شرکت ارتباطات زیرساخت، علت کندی و اختلال اینترنت در چند ساعت گذشته را «قطع فیبر نوری در ارمنستان» اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/460962" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460961">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تحریم انگلیس و فرانسه علیه رژیم صهیونیستی
🔹
وزرای خارجه ۱۲ کشور غربی با صدور بیانیه‌ای مشترک اعمال محدودیت‌های تجاری بر کالاهای تولیدشده در شهرک‌های غیرقانونی اسرائیل در کرانهٔ باختری را اعلام کردند.
🔹
این کشورها شامل انگلیس، کانادا، فرانسه، دانمارک، فنلاند، ایسلند، ایرلند، نروژ، لهستان، پرتغال، اسپانیا و سوئد هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/460961" target="_blank">📅 21:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460960">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
مردم به امر رهبر خود همچنان در میدان حاضر هستند
@Farsna</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/460960" target="_blank">📅 21:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460959">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s95O_T_a7ecnW53_YveZT8gqAQ4iLVFTZtYKuM_ErwWr_Vbjv0VdjEQWwtnyHmbR2SzMQEWFlF0JVVItRL7FfOGSksT4-B3ga-vezjMqZPBTnYJ2Z--OWvUq-NuquGOM88ZT3n9CMDqzu9ejw6NyZiX8iv-CS7xNGL-yDPM_uiodXN0fJll-_ecC-7sGjUePn4_dE7JfP8PigXimON2hUsrGo9ekvHKinK5H6TTdNwy9fw0lDj5F97LMUfpcTnwcloLEmsfzrzmzcFLeo8T_F0kMiruXBLAqgBOg5xd_BKqWnDS3bRpT8_3YDJLtMAhgSjD2smgEgHgiwcyqJh-n0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بلوف ونزوئلایی ترامپ مضحکه شد
🔹
کاربران مجازی با انتشار کلیپی برنامهٔ ذخیره‌سازی آمریکا با نفت ونزوئلا را نشدنی و وقت تلف‌کردن عنوان کردند.
🔹
برخلاف برنامهٔ ادعایی ترامپ مبنی‌بر پرکردن ذخایر آمریکا با نفت ونزوئلا، کارشناسان می‌گویند ذخایر استراتژیک ایالات…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/460959" target="_blank">📅 21:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460958">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c071e6554.mp4?token=aTBwUQ0VsHGsjLePFq6TCf1fmWAJGagvG8UoqRSl_78-94luWnut2PRLtrSPZtoq-5zC9DCCCOWzCudDx3P41XLxAzATYnQRPzhobcoZ01RrYI2UWwswOxM9qxAUPlCCT0jyyvxD73vlMfqoRGwNe32qCO7qr9SzNKfsHznbZzmxElQ2RehZXSIaNymrKWqWLy0HqP6Xbre9QQ9t8JYR-YZiUKNvQ3XJA6JUxu2LKk3JefLWs-4tM2Doekgk6_POz0HemkwXcoT4nHQZ0mHQ5cN19TFKYqgV6dTDmQD_ohZc1ZkJh1DmVIMGhOPvjsLoRlM4e04c8AetXyotNQODHr3IcCMj_CqKUBHVCrzA46PFBrPbRWMgc5FEzBNtiYrgHMCmD4kspn-CzDp3zfHPTx5Z0jzNNkFOyauissJSRBZ4DybAVrMKQWyHnYD3SkFnpIuacYj95BMpfVscuCxWKtPbEolZ6DuUWEYGpZSIsAIFXl9PboEGk_kiFLlVzDYS2dbkCeuhr2rpQUBhbThahY6VrRCUdBRJTpBmGbGWThJFRfjJbjfxbequ3UUzaN4TS-kvxaO4iCrOUq_aqqhOySNXm0BaAQAmJWtmpyw5HdtBQPYXLf11GD7-BDX0yTvtnqSonCiOeCNiULkuVxHUkjmDUsQ5ypWwNAyf1FStPZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c071e6554.mp4?token=aTBwUQ0VsHGsjLePFq6TCf1fmWAJGagvG8UoqRSl_78-94luWnut2PRLtrSPZtoq-5zC9DCCCOWzCudDx3P41XLxAzATYnQRPzhobcoZ01RrYI2UWwswOxM9qxAUPlCCT0jyyvxD73vlMfqoRGwNe32qCO7qr9SzNKfsHznbZzmxElQ2RehZXSIaNymrKWqWLy0HqP6Xbre9QQ9t8JYR-YZiUKNvQ3XJA6JUxu2LKk3JefLWs-4tM2Doekgk6_POz0HemkwXcoT4nHQZ0mHQ5cN19TFKYqgV6dTDmQD_ohZc1ZkJh1DmVIMGhOPvjsLoRlM4e04c8AetXyotNQODHr3IcCMj_CqKUBHVCrzA46PFBrPbRWMgc5FEzBNtiYrgHMCmD4kspn-CzDp3zfHPTx5Z0jzNNkFOyauissJSRBZ4DybAVrMKQWyHnYD3SkFnpIuacYj95BMpfVscuCxWKtPbEolZ6DuUWEYGpZSIsAIFXl9PboEGk_kiFLlVzDYS2dbkCeuhr2rpQUBhbThahY6VrRCUdBRJTpBmGbGWThJFRfjJbjfxbequ3UUzaN4TS-kvxaO4iCrOUq_aqqhOySNXm0BaAQAmJWtmpyw5HdtBQPYXLf11GD7-BDX0yTvtnqSonCiOeCNiULkuVxHUkjmDUsQ5ypWwNAyf1FStPZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال زودهنگام شمال کشور از پاییز و دردسرهایی که به‌وجود آمد
@Farsna</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/460958" target="_blank">📅 20:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460957">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jR6kkqFHVNErF56mPwccP2zST1Zf0K5j5Ykfv4qLMxbJirtltqYsoetJO1RTT8XKbYlMaKT3RRy6s8uhESlxQ7os4MDwkUQcjm0zA9__tgc9W10jEL5EpMhkuPC1rvKHv3_ZR4W-XZda7-HJhIUSagM59Zt3X31Ku0pSYLnut0hXMIMBMJmpzdCwVz8AEa-fLwlr-_hJJLbWQSTcbRvgim2OJfTtuF9fvwjwuwYyqO0WzrLX7gWYKAhDpuZILws7QSQi4L-luPstJLl4zFcumllwsqkQR1IDjzwAw2QhNTiw4s7eiSgr_3wBPCL2QMTGbxtz5gS59qH8h6IR-8t_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی ریاست جمهوری : دوران صرفا «شرکت‌سازی» تمام شد؛ فناوری باید به بازار و ثروت برسد
🔹
حسین افشین، معاون علمی رئیس‌جمهور، در نشست شورای اقتصاد دانش‌بنیان خراسان شمالی
از تغییر رویکرد معاونت علمی در حمایت از زیست‌بوم دانش‌بنیان خبر داد.
🔹
او تأکید کرد حمایت‌ها دیگر صرفاً بر افزایش تعداد شرکت‌ها و توسعه کمی متمرکز نیست و باید به سمت
شکل‌گیری زنجیره‌های ارزش و بازارسازی برای فناوری
حرکت کند.
🔹
به گفته افشین، ظرفیت‌های علمی و صنعتی باید از مرحله پژوهش و فناوری عبور کرده و به
تولید، صادرات و خلق ثروت
منجر شوند.
🔹
در این رویکرد، اتصال
شرکت‌های دانش‌بنیان به دانشگاه، صنایع بزرگ، بخش خصوصی و بازار
برای رشد شرکت‌ها و بالابردن سقف اقتصاد دانش‌بنیان کشور در اولویت قرار دارد.
🔹
پیام معاون علمی روشن است:
زیست‌بوم دانش‌بنیان با تعداد شرکت‌ها بزرگ نمی‌شود؛ با رشد شرکت‌ها، ساخت زنجیره ارزش و تبدیل فناوری به بازار و ثروت بزرگ می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/460957" target="_blank">📅 20:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460956">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | Moallem.ins</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEYwMdggIm3Hmx8Q-B3BlPrvuymPmwTMhvS__XlZYPzNgz1oV_abyQNEFJHehiE5OYQ2jVhH0KWvGr3CG7TOzqJfTHxJa9gRJc8x0kgCTl3jbhi0GAF83y4vd52w6eStvA488i47d2e5yu6rurZn1nmzjbK1YDzXVs2XiuFsTVQXEQtZJFYU_k59oeA-1o38-EynEgGOBXwDRC9QH_opunTZ1lZj9BaHpKrmXHgAsgu_JG2jcvCVu0aIEREXhekYfpsjmPVHqPCaGIYjgWmevr6ZUfC14b4sSN-YBaPmPR8qEAY5zoq3APIv97VkrzYSFmSBZNV9Ysue5rYOZTC_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میدانی بیمه معلم در مناطق سیل‌زده
مازندران آغاز فوری ارزیابی خسارت و تسریع در پرداخت به سیل‌زده‌گان
🔹
در پی وقوع بارش‌های شدید و  طوفان‌های پیاپی و جاری‌شدن سیلاب در بخش‌هایی از استان مازندران، بیمه معلم ضمن ابراز همدردی عمیق با هم‌وطنان و آسیب‌دیدگان این حادثه، بلافاصله تیم‌های تخصصی ارزیابی خسارت خود را برای رسیدگی فوری به وضعیت بیمه‌گزاران به کانون‌های آسیب‌دیده اعزام کرد.
🔹
به گزارش روابط‌عمومی بیمه معلم، به‌دنبال ورود سامانه بارشی ناپایدار و وقوع طوفان‌ها و سیلاب‌های اخیر که منجر به آب‌گرفتگی معابر و خسارت به برخی از منازل مسکونی، واحدهای تجاری، مراکز آموزشی و زیرساخت‌های منطقه شد، بیمه معلم به‌عنوان بیمه‌گر پیشرو و حامی جامعه فرهنگیان و عموم شهروندان، با تشکیل فوری ستاد مدیریت بحران، اقدامات ویژه‌ای را جهت حمایت همه‌جانبه از آسیب‌دیدگان آغاز کرده است.
🔹
بر اساس این گزارش، با ابلاغ دستور ویژه مدیرعامل بیمه معلم به سرپرست استان مازندران، کلیه کارشناسان و تیم‌های ارزیاب خسارت بیمه معلم به حالت آماده‌باش کامل درآمده‌اند و عملیات پایش میدانی، بازدید از اماکن خسارت‌دیده و تشکیل پرونده‌های خسارت از نخستین ساعات پس از فروکش نسبی آب با جدیت در حال انجام است.
🔹
علیرضا بزرگمهر، مدیر مجتمع ساری بیمه معلم، با تشریح آخرین وضعیت اقدامات میدانی اظهار داشت: اولویت اساسی ما در این شرایط بحرانی، ایجاد امنیت‌خاطر و ایجاد آرامش در بیمه‌گزاران است تا ارزیابی و پرداخت خسارات در کوتاه‌ترین زمان ممکن صورت پذیرد و مبالغ غرامت به حساب حادثه‌دیدگان، مدارس و مراکز تحت پوشش واریز شود.
🔹
او افزود: بیمه معلم از تمامی دارندگان بیمه‌نامه‌های این شرکت که در اثر سیل و طوفان دچار خسارت شده‌اند خواهشمند است برای تسریع در اعزام کارشناس و تشکیل پرونده با مراجعه حضوری یا ارتباط تلفنی با شعبه سرپرستی و شبکه نمایندگی‌های بیمه معلم در سراسر استان مازندران اقدام کنند.
🔹
بیمه معلم در راستای تعهدات حرفه‌ای و ایفای رسالت مسئولیت اجتماعی خود، تا برآورد نهایی، تسویه کامل خسارات و بازگشت شرایط به حالت عادی، تمام‌قد در کنار مردم شریف مازندران و جامعه معزز فرهنگیان کشور خواهد بود.
#بیمه_معلم
#ارزیابی_خسارت
#سیل_مازندران
سایت
|
بله
|
اینستاگرام
|
تلگرام</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/460956" target="_blank">📅 20:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460955">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/460955" target="_blank">📅 20:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460954">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b2d16efa.mp4?token=m0_Tf8tRGHHci_mhxJpOBV0UIAYuRnODdRTtmFD6gcaZ9qadUVcUgG7sRCYKL2XIkdDHd1BXzYD4w54idsflta6KyLYRMQZ2cASi9XRXi9LcwgoCO181B5DX17KtXYESdoOwN545I6DryD04yYsFp1goQnust5AprQc-u4MkvCj1P6vTQ7geNxrJmoiMXFYuxtop3fidG5vTyu2UK-mKxkHpIPXmDELIHa6zsCkpQnESE2dlMlwlppj5Y8gF25y--PbX12jnlq0nHv1P0XTaHsDlGnu4vmtjI7EaHg34vU-pKbw2e3giq046ADqrYad26o68VtPkZ1SteCZ5nxZihw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b2d16efa.mp4?token=m0_Tf8tRGHHci_mhxJpOBV0UIAYuRnODdRTtmFD6gcaZ9qadUVcUgG7sRCYKL2XIkdDHd1BXzYD4w54idsflta6KyLYRMQZ2cASi9XRXi9LcwgoCO181B5DX17KtXYESdoOwN545I6DryD04yYsFp1goQnust5AprQc-u4MkvCj1P6vTQ7geNxrJmoiMXFYuxtop3fidG5vTyu2UK-mKxkHpIPXmDELIHa6zsCkpQnESE2dlMlwlppj5Y8gF25y--PbX12jnlq0nHv1P0XTaHsDlGnu4vmtjI7EaHg34vU-pKbw2e3giq046ADqrYad26o68VtPkZ1SteCZ5nxZihw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شکار یک پهپاد آمریکایی بر فراز تنگهٔ هرمز
🔹
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق کشور شناسایی شد و هدف قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/460954" target="_blank">📅 20:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460953">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در منطقۀ جیزان عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/460953" target="_blank">📅 20:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jldxZmyJ8SwIvk85lNv5WAqouPBbSiP9buWGZ4kFkHEDXKSSiYMLztKeVjqAsyY8btL0VqUHByxY7lMZ8HlInS133o08PbD46gU7MzHZjp-VEjO1t2HcDHJAfWgBAZU0NnN2pcNPKU9CYUzNGM7vyn0975humI9HhxSZf4zd-Yy_bddbFpECaFGt9WtNZGe4UGIOD1kh7bN7hswNIs6Kxn4DaCDW5ZNz2xPSphEmX_K2SCibeoORR51amMyJS-wjJm6Ri3auVtNwBFYdCdi42eOPwub3u9fELoQ6f3dfj36_8ir0bEG1ep6pjifuQON_R8-6uHeN_rysqnm3IgOs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر راهبردی نفت آمریکا باز هم کم شد
🔹
درحالی‌که قیمت نفت امروز به مرز ۱۰۰ دلار  رسید، آمار جدید ذخایر راهبردی نفت آمریکا که لحظاتی پیش منتشر شد نشان می‌دهد که این ذخایر ۱.۲ میلیون بشکه دیگر کاهش یافته و به ۲۸۵ میلیون بشکه رسیده.
🔹
با بسته شدن تنگه هرمز، ۲۵ هفته است که ترامپ هر روز بخشی از ذخایر نفت خود را روانۀ بازار می‌کند تا قیمت نفت را کنترل کند.
🔹
میزان این ذخایر از عدد بحرانی ۳۰۰ میلیون بشکه هم عبور کرده و درحال نزدیک‌شدن به کف عملیاتی ۲۷۰ میلیون بشکه است.
🔹
کاهش میزان ذخایر راهبردی نفت آمریکا درحالی است که قیمت بنزین در آمریکا به ۴.۱۵ دلار رسیده و قیمت گازوئیل هم رکورد شکسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/460951" target="_blank">📅 20:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460950">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در منطقۀ جیزان عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/460950" target="_blank">📅 20:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/460949" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpCk0nlkXrHeOCg2bqq75gapqrE6L4kxO5B12Cg4L7_qaLgVQKIG0O3mY21MYCoq82fuaPW4n2AW9wqAZKB-AWPGS8fqgdjNbiGA3k-JL3fWm8gLJ1IRge0tPeYMqUmlFc8BmPwmK8ewpc3WK5xVctx4SHqZLSlVZTFdEXIoQL7CySjmPboEHlaE6KJ3vLz2EtZUhyldYa5llSYNY-H9oLWrDXghn5dUozVcLsxdxPi1Q4StbBreEok5DQi7YtAS0FzpT-BD2wrQyVbeXghnnWbiH_btECHgijbPFjMQhxqEgPhfc0qCAK04Sp4769GqzExaPFr85Rt2FantkC7CiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توران در انتظار تکمیل دیوار نجات یوزهای ایران
🔹
وقوع تصادفات در جاده ترانزیتی تهران ـ مشهد که از حاشیه پارک ملی توران عبور می‌کند، طی یک دهه گذشته جان ۱۳ یوزپلنگ ایرانی را گرفته است؛ آماری که با توجه به شناسایی تنها ۲۷ یوز در کشور، بار دیگر خطر جاده‌ها برای…</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/460948" target="_blank">📅 19:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTjbd1U-5atIx1cf5Z94TlWsQJwNCizq29JWbrd6dRSBv9J2iRs7BFr07oT7rXMhzRrFDMjhUtRdZrgodMkio5XM9pAdv7ijOMa-op8SMP3zFihcNj_OV-l6liHI2x5cHcTy0LMRM2h19uPT1mSi0L3N-blGgLAzLyyCPk89tHXSsP-RlmMv8dYV8MOMwXXGpg4HbANc5y8b1ySPbBRBJ5jb9ouZ234Jl4HmWFhHJv1TGDr6XQZRTWMsNzSuIdBGt2F8Z2yofzf3Ctva5wkpQrgCKQDQcBuzOlq7pRk9LQAavJl4J2Zx3lbhgPUU4e1EZzu5KP8f6OVdlmO9M_ozyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sG1gf86hxFPSq2OnjT6gEWGFt4y_TG3ar8TXf7j4k5cqziiBhP9Z9Nk0_XvSEge2xG043auD1iG3VBUtueYjwWIyJXIpjVKhK22kIo0X8EHtWW9oV0OsgbAMMSxZiwIuqHT1NR35hdkoZoe3nddeMh-EDpxhPTwhDWFz-MMc3cNOSVEWunvzELNgSPjYaOpzTVySmgAN12CRc5Q2g9IFrfjQe79qwEQ3gllCKhUJib484qKvBp3E-6xicV4b7_nPw0cWW3i7-6lSYeafBaj38tgKglQFQN_MV7R9A_LpEvyN1cSBRNh34xpizWYvKhHIyNE6W1I-_pxrCk5EDWkXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SgtA2sEgTe_4vNfAWFuF_P9n_aMkoIkmfFReemvnjIUbevvPHTOC9rDqtUWzWhnm89tpxp02hq527eudPf484CwjuhzeTJlA39Z3QjQi9vHGPQicHpxfIAaAQjtD2NVs1g3PNTdWwfVtnKU4lDflt0X5hyDszwxKF22zgMn0eCgsib_VMPU9lgxNVJehKWesV7Jw3YzylH6-WcaTTllT7CPuzQ7AGbo21rbeBNNBz0dLDitwdsJWqfKdX143JRgN8CvAHzzjY0JF8sv8Krsy3clsW__hBmaxFqUWfCzGCv2y3oKinZxHfrO8_eUqhsVn49KYtxHg0J0B4o7I1fm3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VttPJb7ThNAb-Fl6UKVFhRnkCEd-FU1OE5mjCjGCNh2SpFXBekym7zGt4HO5Wm9uzhsA2AwzP0N2Seqb4yqCuNyqpkAmqcbMnbykLmDughoS0QZOWULsW-ESSIrdBSYHsjZUJ6DyfnRHON4LufgN_AWJl3Z-Qwv7I2Tf8cfOUMGujc7J4jJ5b57HMkK5vO6jFk5lo5zYiBt8akt4eOrsGfWNzAWiFgC21D_AiwafrIGOlgmR8kh04UfRiGeol8Ic6KofZlEUkNVr0jVVwEKQ-7O9dpoxH-XqsIw67HxSn2QS8Ad1Tk3-xm1WE4VsWj6L6y9YJ6Hw27pBvXYkTH6L-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DS8EbnMnx4f0p_S2XcxAs5Kja4j7BsQttGOUz6IabV2-lbltoazxJ1XRDXfi2zIpwSQ1gq0aBXMHOaAZgdjsTNXKI2WO8R7yr6WRP2qnGfIHYnXrbRjFz6OrSRrqy5S3c5ZXH9DRK2WUswzvvSmcHxi8H9S0Y0IRIhlOCo8ngK6zM5VE_vsr3r8--rvCcwOqsFg6iFXf8KsKVOUW5eNjsvFpcnmCsvsZN3pEYvNCXOAwqGej5C297IbEWXLnV9df1_ct0lHwxUh2ZVOOW_dRpIVcknMbjstSVy3CqRPdFx3UejKO6bd5H3G-KpGz0eFaXEKlZ5SYpdwwwns0l3IzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmL0ouM0Rv6M3bNtfQdAUpHI3Qw1OaMY4vYPKkg4swuL-kD8Ffw3EG5IAGNPe6qCOmBWfPmhHAjVENC_9EO9IRuEJWsd95Ifdn7mHccO0A3XfLOlp3pFuc_5smbvT2Ne5HVPYm5i8Hr3tPdCgON_V7S51usGIkjQ8JKqZLseUExI_u2s6hr--UPukeKsaD8ih7B3RPkROwb3UV_iYpH4kb-rBfPlgTOvwpB1epT76DjMR0Qk7RIZcCf4WSYWzr2NhYplkgmR_MFcddb7gPjcDfEVwk1xmhf-KHyCFd7SWftH8rT5Q19RSYlTZkgQeeCW7vAkLYI8MVLO_TXV7_jEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RneVSQpyIX-tP4gbQVKKkkNVbzH1GC5AQ4oF8GY5Dw5SoDNYnpDItqCD_EJrInIA_fvG8MlnbwulQ6Kh3u5viQD5vDDrQNvYullLaQKvDNl1hVm1AVKYLp4d6T8GX9GOxzR4VxaYYvbhrKukoAFTh0ECmFwBgq7vVb4aHzlH5BRUoCtpnlR8TMYwNMCMTaREuobKt7f6NGLgjHh1dQ5QpjE0kpTWnrgTStm3eUXWli8d2j0st7AiGoApxX_jk_pQBS2jwuEaEGVOC37wYmIQupo795qw_NBI9ETQqNF6NMNs59OhbPZzD_fH3TXX_ZstV3oJSno9QeQVtzGGQXqTlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین دیدار هیئت دولت با رهبر شهید انقلاب در ۱۶ شهریور ۱۴۰۴
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/460941" target="_blank">📅 19:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/396413856f.mp4?token=HyFY-bno63vOIfzXQkr2frKEpDsS9eXuLKpEI5z8S14MG3Upys9gbQ87EJtYikwp3tSj1rnJ2-xuQmvaIsdYH6Wm1x9XQIn8nxV3RAcPgzmvu5rx1tP8g_1Y6nzW3GUKFymbnCaVS4SIxJdC6z5Yc3e-Cznu5LvBS_O1g3Os3bPdjR-1TB2nqEuEW3HGUZkEIEsdkLJT-jCA-OccuCrJLpAx_X-hYZpwxZ7GU03qLh-aSfXz74GOUcp3CyGy90CkcSlWwRdtdgsl6xiSx3Bm4L_1GOVgpVJC2BEHCripLksaF8_z5MGdFDQtGUtTV9z7igjylKSVC9hBhpPzrNuaPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/396413856f.mp4?token=HyFY-bno63vOIfzXQkr2frKEpDsS9eXuLKpEI5z8S14MG3Upys9gbQ87EJtYikwp3tSj1rnJ2-xuQmvaIsdYH6Wm1x9XQIn8nxV3RAcPgzmvu5rx1tP8g_1Y6nzW3GUKFymbnCaVS4SIxJdC6z5Yc3e-Cznu5LvBS_O1g3Os3bPdjR-1TB2nqEuEW3HGUZkEIEsdkLJT-jCA-OccuCrJLpAx_X-hYZpwxZ7GU03qLh-aSfXz74GOUcp3CyGy90CkcSlWwRdtdgsl6xiSx3Bm4L_1GOVgpVJC2BEHCripLksaF8_z5MGdFDQtGUtTV9z7igjylKSVC9hBhpPzrNuaPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نادر محمدی برای سومین بار به شکل خاص و آکروباتیک در لیگ دسته اول روسیه پاس گل داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/460940" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsTiQwLO4qRrgupUo7prnm3TdW_JZ_FlTdYbDnZziYCMCSbjCpCEKSk8R9XXKsgSkUbQeAOXP548Ytc5hqIjsZXsWhT9i4VluD_Fk8-ZUks3gqZ0TswsShgzPoUzypKkVZIeVITweauDgzCdksfv40Siq26qoVEZtZwXTGzMvocUJPRyj2hDWdrjUvNX818tbhBwnIfQLMq44B1C7SdRgsHJToZajw8NFAlOr7PJE8BPZ22qnwYzNfm66Cn9GD366Lb13xOHocp80zqRW9xhBIUlIPZYPjryMayrxdDkEWEpOIIsMc37sFKlJhgs7XEaohB2OU8QtCetNAeYRnjuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران و روسیه نیروگاه‌ هسته‌ای جدید می‌سازند
🔹
به خبرگزاری تاس روسیه، مدیرعامل شرکت روس‌اتم گفته روسیه برنامه‌هایی برای ساخت واحدهای نیروگاهی جدید و نیروگاه‌های هسته‌ای کوچک در ایران دارد.
🔸
نیروگاه اتمی بوشهر محصول کار مشترک ایران و روسیه است که از دهه ۹۰ تاکنون ۱۰۲۴ مگاوات برق اتمی برای ایران تولید می‌کند.
🔸
هم اکنون فاز ۲ و ۳ نیروگاه اتمی بوشهر با مشارکت روسیه و به ظرفیت بیش از ۲ هزار مگاوات درحال ساخت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/460939" target="_blank">📅 19:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سهمیۀ مازاد سوخت تاکسی‌های اینترنتی تا ۳۰۰ لیتر افزایش می‌یابد
🔹
مدیرعامل شرکت پالایش و پخش فرآورده‌های نفتی: تا سقف ۳۰۰ لیتر سهمیۀ مازاد سوخت با نرخ سوم بر مبنای پیمایش به ناوگان فعال در سکوهای اینترنتی اختصاص داده می‌شود.
🔹
این تاکسی‌ها با اولویت‌دهی مبتنی بر میزان فعالیت، به‌صورت رایگان به نسل جدید خودروهای دوگانه‌سوز تبدیل می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/460938" target="_blank">📅 19:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس دانشگاه سمنان: شایعۀ تعرض دانشجویان عراقی، دروغ بزرگ است
🔹
رئیس دانشگاه سمنان: بامداد دوشنبه میان چند دانشجوی عراقی و ۳ رهگذر، شامل یک زن و دو مرد درگیری رخ داده و به زد و خورد منجر شده است.
🔹
براساس گزارشاتی که در اختیار پلیس است، آن ۳ نفر حالت عادی نداشته‌اند و از نظر رفتاری در شرایط غیرعادی به سر می‌بردند.
🔹
سپس حدود ۱۰۰ تا ۱۵۰ نفر از مردم محلی و رهگذران در محل تجمع کردند و شعارهایی نیز سر داده شد که ارتباطی با اصل حادثه نداشت. در این شعارها نیز واژه یا عبارتی دال بر وقوع تعرض وجود نداشته است.
🔹
در این حادثه هیچ‌گونه توهین، اهانت و تعدی از سوی دانشجویان عراقی صورت نگرفته است.
🔹
عوامل دخیل در حادثه شناسایی و در اختیار نیروی انتظامی قرار گرفته‌اند و با دستور مقام قضایی، روند تشکیل پرونده درحال پیگیری است.
🔹
پس از این اتفاق، برخی در فضای مجازی سناریویی تحت عنوان تعرض مطرح کردند که این چیزی جز یک دروغ بزرگ نبود. اصلا چنین چیزی رخ نداده است؛ این حادثه یک نزاع خیابانی بوده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/460937" target="_blank">📅 19:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXPTCtoq5PcsFlhIt2sUx8WB36duQnIb1uwRJMRAZgGqCChp5dkrM2Lobuc-oh8avfXlyy_bQr9yzlMllBHOwS1hdrErlIGMXUjX-OjumNS_AmAC-RZ9b8tPCj9OeZ9sMnzxxR2J_Bo5k-1UbQTOed8ToIGdvuJGjO74d5sJordb1DDqUe5mMpYibNPD3bepwVCMZSfMUs4xDzNZFEeaFiWqo3HU_BFzkrjP76IrDTit6dujOSRIqscliRxLlhD6dDIY3-B4n4HdhakCASZm2SnKddXLgAp9ogsdBBmeZW47enC4sdpiF1nSInnrrzKdkhAzbQpkWP5WOFghIuZEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
دوربینت را انتخاب کن، حقیقت را روایت کن
مجیدمردانیان، پیشکسوت عکاسی خبری : «عکاس انتخاب می‌کند چه چیزی دیده شود؛ اما هرگز حقیقت را قیچی نمی‌کند.»
امروز هر کسی در جایی که ایستاده است مانند سرباز پای لانچر برای کشورش می‌جنگد؛ از دانشجو و معلم گرفته تا آن کارگر پای دستگاه اما هر کدام سلاح مخصوص خود را دارد.
اینجا اما آدم‌هایی هستند که برای گم‌نشدن حقیقت می‌جنگند.
دانشکده رسانه خبرگزاری فارس با رشته عکاسی خبری (کاردانی و کارشناسی)، تو را به روایت‌گری لحظه‌ها می‌رساند.
اینجا آموزش با تجربه، گفت‌وگو و فعالیت عملی در باشگاه خبرنگاران «توانا» همراه است.
🔹
بدون کنکور | مدرک معتبر | اساتید باتجربه  | معرفی به بازار کار رسانه
🔹
ظرفیت محدود – زودتر اقدام کن
📲
ثبت‌نام: عدد ۱۴به ۵۰۰۰۱۰۱۴
🌐
سایت ثبت نام :
futurix.ir/go/rxDxXO
🔹
مرکز آموزش علمی کاربردی خبرگزاری فارس
🔹</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/460936" target="_blank">📅 19:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460935">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
تصاویری از حملۀ هوایی عربستان به یک زندان در استان الجوف یمن
🔹
به گفتۀ منابع یمنی ۳۵ زندانی همچنان زیر آوار هستند. @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/460935" target="_blank">📅 19:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460934">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d4c57458.mp4?token=f-VwdH77EqsYZZ4jVx4BxO7zCmXEMuhTYsINcws1_ONpKXhQFcmLVSMAVw3I1h9sRXGDcsKv_a46tgWUHGdjoRTfFhS_41JWrG7VfJdKOKzZlT7gEzXwPGVYRdJXW7XvkTnZsK_kzkBKpkQn4C4IEPNZEhOFpwOy8cfNDVD3is-Uxk7d7Y1Qc14TN2QN00zGSW9j_8MhwqbB5i7a1KSood4ODPoubdAQrpHwM6yHTzRLetP_RtggIQ_iFhp9T22LBYdhdwJhqeM9CT441Q32d0Jut_v-UcG3E1acQh834spylWEY_OR9YT_HikbRC2YCp00wKs1mBBaK00BzoKVvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d4c57458.mp4?token=f-VwdH77EqsYZZ4jVx4BxO7zCmXEMuhTYsINcws1_ONpKXhQFcmLVSMAVw3I1h9sRXGDcsKv_a46tgWUHGdjoRTfFhS_41JWrG7VfJdKOKzZlT7gEzXwPGVYRdJXW7XvkTnZsK_kzkBKpkQn4C4IEPNZEhOFpwOy8cfNDVD3is-Uxk7d7Y1Qc14TN2QN00zGSW9j_8MhwqbB5i7a1KSood4ODPoubdAQrpHwM6yHTzRLetP_RtggIQ_iFhp9T22LBYdhdwJhqeM9CT441Q32d0Jut_v-UcG3E1acQh834spylWEY_OR9YT_HikbRC2YCp00wKs1mBBaK00BzoKVvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۳۱۳ هزار جان‌فدا در تهران
🔹
رزمایش بزرگ مردمی «جان‌فدایان ایران» با حضور ۳۱۳ هزار نفر از نیروهای مردمی، بسیج، سپاه و انتظامی جمعه ۲۷ شهریورماه در پایتخت برگزار می‌شود.
🔸
علاقه‌مندان برای ثبت‌نام و حضور در این رزمایش می‌توانند به مساجد و پایگاه‌های مقاومت مراجعه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/460934" target="_blank">📅 18:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460933">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شمال تهران در انتظار رگبار و رعدوبرق
🔹
هواشناسی استان تهران: وقوع رگبار و رعدوبرق، وزش باد شدید موقتی و احتمال تگرگ و سیلاب در ارتفاعات شمالی و شمال‌غربی استان به‌ویژه میگون، اوشان، فشم، شمال لواسان و شمیرانات پیش‌بینی شده است.
🔹
در شهرستان‌های پردیس، فیروزکوه و دماوند نیز در برخی ساعات بارش باران، گاهی به شکل رگبار و رعدوبرق همراه با وزش باد شدید پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/460933" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460932">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWoQzhhJx2iWViIHzSrabhuG_coUBNDw8JWWdTSn8ZIq8T7AE7k2mUSDe8tO-uhoQgeTpvhu7fT8MS8KN00Ekr3smDHWA8vaeofr2BczV1LCz-QnZoxOj0B37nxMPTaLl7Xflp3kANnJo6oCqsdGeZt5XUmYoX1_R5VQKnL-Z0XNk4MC-slTcrdG7LH10Qb2l-nmIKPI4AD6bteK7NcLjhj5ffiQzZEtoOK-FfbAL0o0llpf9ihz3NdEDpkr1Xb2UfqIsOzRiAjLm_IryBCUkXPuBi0yC8WxybNwXS-0mjv6EpkaW1OQUNAP9PAi1ubBuosz-snrL5XEsHkonDYcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور از تنگه هرمز منوط به پرداخت تعرفه و غرامت جنگی شد
🔹
سخنگوی کمیسیون امنیت ملی: در ادامۀ بررسی طرح «اقدام راهبردی امنیت تنگه هرمز»، موارد زیر به تصویب نمایندگان رسید:
🔹
الزام اخذ بیمه و ضمانت‌نامۀ بانکی
🔹
پرداخت تعرفه‌های بیمه‌ای و خدماتی
🔹
پرداخت غرامت توسط…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460932" target="_blank">📅 18:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460931">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
وزارت خزانه‌داری آمریکا امروز نام یک فرد و ۳۵ شرکت را به بهانه ارتباط با ایران در فهرست تحریم‌های ضدایرانی قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/460931" target="_blank">📅 18:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460930">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vh1RorIADoO80UIp8hkzVv-PxtiTCnV83z7qc8HT3b9xa9ZitR7JT52g8EXdb_oxlqfl-_Shl__j49xjzx8PX4kWPXNeaaarnejXsmlHyxUSZbh981oXd1Ks-V-tvJpPO_YJVoLGEPbmKxzp0jafdJ9dJnNeC_ANR4HPssFid59RCpetxoiJeEXzjZB4cjtLWD_1XYYSBH4qANGkp91AgYoltjGa8bcr-RaczbDo9xCLcrR8kozv9iqU39laS9JNIwGmyalPESAYL7nBU4nsA-BTkcmexNOPd3_SVigIC_FmqZVCs812HDcQ8pB7O_De-Sv5m8J0QMFUKYGo2MKUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار یک زیرسطحی هوشمند آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه : یکی از مدرن ترین زیردریایی‌های هوشمند و بدون سرنشین ارتش تروریست آمریکا را در ورودی تنگه هرمز به دام انداختیم.
🔸
این زیر سطحی هوشمند از جدیدترین تکنولوژی‌ها در حوزۀ زیرسطحی در دنیا برخوردار…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460930" target="_blank">📅 18:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460928">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQNIhl_tM2LM-2ClAdmGF_-YBbY9xQ77XPri6Aw0SOWSTEtXuNgTMMY7fnArFSE6y8IW2rcAlYFZJ7iwSt2WLfCacKI-hpHaqcNHovTJuXsC5tkk5foqHPDTV_TD-CPoLta8oc5urrDeFlhBp56A7n2yUrdxh4tElGDrQ6c-T319gnhGvQHry9V2WzTjGbf0YMPW1egKEB6iQkGxP4R2BaLnQM6rFb2ZqyRFCJEoqOA7eK6Liq2wFqgh4KGGogKzzQgn-NOp7HJmQAj_KmemZbSJNp0fcDVjG-joe3Jx1Zo_zOhvQXxGTM0HdAyG-mbpa0MD2ydrAo5i4I9p5R1BWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار یک زیرسطحی هوشمند آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه : یکی از مدرن ترین زیردریایی‌های هوشمند و بدون سرنشین ارتش تروریست آمریکا را در ورودی تنگه هرمز به دام انداختیم.
🔸
این زیر سطحی هوشمند از جدیدترین تکنولوژی‌ها در حوزۀ زیرسطحی در دنیا برخوردار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
🔹
این زیرسطحی اکنون به غنیمت گرفته شده و تا ساعاتی دیگر تصاویر آن منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460928" target="_blank">📅 18:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460927">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌ حملات هوایی عربستان همزمان با پیشروی نیروهای یمنی در استان تعز
🔹
منابع یمنی از وقوع درگیری‌های شدید میان نیروهای ارتش و انصارالله یمن با مزدوران وابسته به ریاض در شهرستان «الوزاعیه» در جنوب غرب استان تعز خبر دادند.
🔹
برخی منابع نوشته‌اند که «نیروهای یمنی…</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/460927" target="_blank">📅 18:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460926">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
وزارت خزانه‌داری آمریکا امروز نام یک فرد و ۳۵ شرکت را به بهانه ارتباط با ایران در فهرست تحریم‌های ضدایرانی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460926" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460925">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4e36440b.mp4?token=stM_wfx6aTaGs1Ha8ceLHxQuyh1viBFeCUbyMx0SITzPPCRFoJ3ZlPwRtvdjoEqSLZiJ6nMaLI8C4C5q3GfgGPZnCy-7qnPsBFNG5q-FId5Q1xgEcB5SCOZilT_QPTvEn1B5qOxNNLitDmjOgoZIeVDd_lXe3ef0Tn65zV84nkd0GTu6hwGGWTSMyDwTBcnGEpCPHZGuQ-_mDw-OakuDgYr3g7xgZoGZy796Ats9LH0Z6bl32Flb55MFnH5ZkwazgBTVPQt7NGj-RcR2dtomYxzP082QpuVSAEPquXolrdKq7mwGN-ky8q_ADUgROgGGqnP4fMK6TCtydUvD7o24gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4e36440b.mp4?token=stM_wfx6aTaGs1Ha8ceLHxQuyh1viBFeCUbyMx0SITzPPCRFoJ3ZlPwRtvdjoEqSLZiJ6nMaLI8C4C5q3GfgGPZnCy-7qnPsBFNG5q-FId5Q1xgEcB5SCOZilT_QPTvEn1B5qOxNNLitDmjOgoZIeVDd_lXe3ef0Tn65zV84nkd0GTu6hwGGWTSMyDwTBcnGEpCPHZGuQ-_mDw-OakuDgYr3g7xgZoGZy796Ats9LH0Z6bl32Flb55MFnH5ZkwazgBTVPQt7NGj-RcR2dtomYxzP082QpuVSAEPquXolrdKq7mwGN-ky8q_ADUgROgGGqnP4fMK6TCtydUvD7o24gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهدی خراتیان: جریان نرمالیزاسیون سندروم دکمه صلح دارند و فکر می‌کنند اگر بروند و درباره همه‌چیز مذاکره کننده آمریکا دست از سر ایران بر می‌دارد
🔹
حتی می‌گویند تنگۀ هرمز چه فایده‌ای دارد، بی‌سواد هم هستند. هیچ آدم عاقلی این حرف را نمی‌زند که اینها می‌زنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460925" target="_blank">📅 17:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460924">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By9ztQmL_Uc0Xwa-7pPQbOO3dx8RYvmg__DxciqISMm7-B9XlBNdA6LT66xnvNtWSeQEkVl1Enmp7LsOxLAJvqIrkkp4YTCQhxSsLYbAKGl600hDP1bNyDsH07GmXVJP76BCtVubhUuphk7sr1ioUsdz_uHUPzNDxmJ8aVmNU_fxQYSP363BT-z82BWnBxjdTTsqQN6GHbCAalE-q3iXK91t76VVKJ5amKmcr8adcS-zH_61dGGA1mfbtaUeX7LxdFcnSgcFBzr7OukCTZc50Gw7WfZ5_JQG4R5eImb8Qa_vfgqzvAiez3j2FUzp7THgQu6ixuuS31B1aueGkPKHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نشست امروز سران قوا به میزبانی رئیس‌جمهور
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/460924" target="_blank">📅 17:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460923">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-uaceRCmEQbxHAWUAVBrqMrY9fcGeVnal7Up3L-7sldb1xzNJHLNgkqyOpE_7tlP5J-9O0DOFznNyWZ7ZxqmMjQzVryCRvVe-i9u6G4fo4BxrDjrN6uaikrVEF3sMK2RPy5e_dZOX6qpOzUdo287ihW1X8CpdrDyrEAjETi7hOQsHJtG56EYV6Gr9BWrZUvppwU4R69hOO8dXs3Yp4zsLWax3XFlwKVs9S5u52_eM53pudG3G4Y3UTUjuMrmA-alUGXg1jP5jRNGB5dxIwgcyBXG1AuzOXNsPShjPuX6FIf13mm-DDDXO2crp6mb1lXYo7_CCsVZ2mvQkWMxW1wPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور عالی فرمانده هوافضای سپاه: در شرایط پایدار تولید موشک و پهپاد هستیم
🔹
سردار بلالی: امروز قدرت نظام جمهوری اسلامی از لحاظ موشکی و پهپادی پایدار و دائمی است.
🔹
اگر دور کشور ما را دیوار بتنی و سیم‌خاردار بکشند، نمی‌توانند جلوی تولید موشک و پهپاد ما را  بگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/460923" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460922">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_3esF4yjNwsa4oFEr2zlQUm_jpBesKva4PDL6VRIzUAWyLdvfhwWJPpIWTl6ZISgTDh3E0aScNu2Zx-x2_LmSdTRWefybXIC35jvsRDWc2lc6SL8-bQMDCAWkmmWFsjbmVC5wz23De7AdG2tVnHqVUDQ6cSfB2k8_SNTMralDl39_nuWvCNR_HqZcTVz4uVQh4z69MHDcIxFyJlOIETWYZ2Md-ZC74Cmk_9_iheLvW3-SBx4ujewwvCkd--BM-9qATTUWMN28UDuf2S13mzYHI30KmeayMz3YM3_WDdyjKHCbtgskWclBEBlOGqIoGWAUn1Dgmmn5K4hC2FCuF5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرداخت خسارت اثاثیۀ منزل به آسیب‌دیدگان جنگ از شنبه
🔹
رئیس کل بیمه مرکزی: با توجه به اتمام کارشناسی و ارزیابی خسارت حادثه‌دیدگان جنگ ۱۲ روزه و جنگ رمضان، پرداخت خسارت از شنبه توسط شرکت بیمه ایران آغاز خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/460922" target="_blank">📅 17:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460921">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPUgo_5tbQ_NqqU7G6aEsSZa5Xak163UTJlx7Y3vkUOL4RysYv7FtyYwXRyZGZPgNVAXrOhMIkRBdZxoJvJrTYaSIydsF1e2arZWnHvMb2kZRur3PwgJh03YLtLMReJ4_qu71FVnxoiN4oqA0JGRuMtUvWiSwCFydTQMAUi5Fv039uP6iCZpaqsf3bz_w0pY-IknZMe6K0kR2Ww61_d8ZfClPfwG67K67Cn3soq0RWhXlh97StevG8vKf5vx1uVIvxreW1ftfJXbZbUkxIzHnruCKGC6AVn3Soxy6D3I_sy1er3mpF24HVqVjjgpKDFHqmZYPqeKiR_SqWJLv2FcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: با ساخت‌وسازهای غیرمجاز در عرصه‌های طبیعی قاطعانه برخورد شود
🔹
با قاطعیت با هر اقدام فراقانونی که به محیط‌زیست و منابع طبیعی آسیب می‌زند، برخورد شود تا بستر برای بارگذاری‌های جمعیتی غیرضروری فراهم نشود.
🔹
تملک اراضی و مشخص شدن حریم، پیش از اقدام اجرایی برای احداث جاده و خطوط ریلی انجام شود و هیچ‌گونه مجوز ساخت‌وسازی تا محدودۀ حریم مشخص، صادر نشود.
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/460921" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460919">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7708c5f418.mp4?token=ooVfRwL53v56SIdv9kamx-MWbRwTntz2dco0f-5Ilv1598lkTtx1KEmU_pHQ6YxQ93vUc2vkPfYbKuBR6LVd5Ld9M8XYMeLbRXb_wuE3KzYUG8S0fsE4BFd84d7_Nc76i9pg3kCy2ZLtaJ4mKFJKXS_SPBMhyaXUcXYggv4rKxU64VVsF2rNsPdw7o5bvObOBkvuhrqCIUH_nyK6rx7dShprKPhA1O3x43F0HGKLLw9PzPdTahvXIi4ahYLZ7C4uwgKuCVyUA5DBHG39UUYndHLYr6G5fonYv0WZ1PTZfhDx7uZvVT8mTVQ2xK6Sleu4bgBLESdTMulfIsgqZf9BAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7708c5f418.mp4?token=ooVfRwL53v56SIdv9kamx-MWbRwTntz2dco0f-5Ilv1598lkTtx1KEmU_pHQ6YxQ93vUc2vkPfYbKuBR6LVd5Ld9M8XYMeLbRXb_wuE3KzYUG8S0fsE4BFd84d7_Nc76i9pg3kCy2ZLtaJ4mKFJKXS_SPBMhyaXUcXYggv4rKxU64VVsF2rNsPdw7o5bvObOBkvuhrqCIUH_nyK6rx7dShprKPhA1O3x43F0HGKLLw9PzPdTahvXIi4ahYLZ7C4uwgKuCVyUA5DBHG39UUYndHLYr6G5fonYv0WZ1PTZfhDx7uZvVT8mTVQ2xK6Sleu4bgBLESdTMulfIsgqZf9BAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌گرفتگی منازل در پی بارش و طوفان شدید در مازندران @Farsna - Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/460919" target="_blank">📅 17:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460914">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihPNWc-za5ydUvfwO6gx-ocNxuTY_Ym0tIm_jmFVchpJIcFu2j5vhAy_q2uHc24RhKAA6PcJyhHYFZHocCv4qnxkR2MIve5IkXk89tEvL8tBtEHvvKeSnyCVs_s89cTsR7FpYPYFI1K7nVs7qDKeXNPbUgNuO4GrJsIAocCmgtTE6lBN2_Qv3Phbc6QVSrXVTlCriSF2ksx7uIe7dMKHp4Zt2gJM4HPjeqgilhqU78PxfhP9IYXD7_ARHULo8ssPsF-PqEXi_5ng0sEz19ybSsJFZRWyLLfoK7KT7DifBf2T04tf1uJ8px3iowSs4_9Q5nuGdVb5ZWp2xssPfTOiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjyIz20rk5QjQTJ0EuQhyR5C9wQMmZLjwxYD5dztfouWPPX9MX5JDnmce-jAR8jI9I4-vAIAKHM6N5yAdOrnlv_dtUoNMWphfqLpeHuxiEjnUutMrwe4XtwH8668aEvODTeDOR9vxt7F5tZJk8jwcpQJVbd2OxYz278cfKXO-AatMQX2mjw9tRL43pwxNozgQoa2rf1Ed5EmnL6RCPrKSs9hWuclqwobPI0ZkTE6Z8Y_TuYHlgICV_FR2pX6kHmExGvIMIKs0YlW7bK94KZFTrBgG9B-8bWuUcVHVDjOiSJ6Jwfqb9v_0XVJ5hO8hin4ZveAAqKGjaK2WkhwQ-afYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffP7YPlSiHmP_8Um6WrKIuClngSYLmrGbecG7LwDJD0-2Ps-XG04mE9zhF8H_m_EBVE2BAeuT0tocoYsmYYAZNH2yIYCit3xEX7KIpxUVrd16f7pCXDt9e8KVbu5lfHpyltI9UZeHDZ1g96d0dL8HT3NQiocmBCqnAXndrLmJT7pElZcknadN5kQhTBBpqwP0tSBjI-HrVb64UEM_GbiaJ3PWT9jzV2tA8aZtSTJuL5OGwMYfCaWRYb9kdcJB9N2fLcAKgsYGkrP3iGFAbnUph-9I9PMVi5GNcicM5ptNRPcPr2hszOqczq6-6_dj_C0B0dGLt97kLeQYbNbLk3EIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XlN3DqpbY_A19861LI79rNXlrV22sGkDkDLfce2URYw_mqn7dea5p-9EgwZAAb26dXX5UL-mFDU2zOr2TuApARAxNuMWTf4jOd3DqUcbbusNVkwVay6etGHGzILgMmOCh8IKninLNRbb0NrwhYPNmje-sXYhBccHc878epUJe7Jg6aUpkYpw-E97tjD_RepneivjGwGQZVwRlealtbpDNq24nmLzFYk69Sj4iuxy4MgbqYwCwOkJvN0yMUw2XTVN8z6vdK6AFw5YkiWHSM_Ew4Mxb9a3P80QDwv9jXQQEb-IeW0UHSiSQtimNWbK6n7VJAxOqx4ExNqluZciSMIDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j78lKUa7wSDCBLWvuwzXR0FThP4F0BIFkvzywp6zt1_C3T2-7uhMd7vd_kTZdDkRCWyKIeRKXchAd0rl5kn2DSN4OCneeqqBhc14bCJbGaz8EfFZcd4j8lvHPvhcwtpYXfiAd5UwxopjX0ObGNip0J3hXAC5jRGrB8qKdKZXE_gPwWTQisT3xo54pBdLf-f0H5c86EdHNCqP-h2-Gt1NsU_TCZjcVZk-dOAQb9JYZlBQw8wIfrw_h_LiFiRbxwdKFRoyf8x07dl7a8n9ZHXEBllNWJ2npmbSp7w9mRJT3ydhDN3kywSFLDgMAbFfzQUcunTAS3of23qKlgvfPSgGqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس بسیج اساتید: از ما نخواهید که بسیج ساکت باشد
🔹
هر مسئول اجرایی که در راستای اهداف انقلاب حرکت کند، باید بسیج را «نِعمَ‌العَون» بداند؛ ما حاضریم برای مسئولی که در راستای اهداف نظام حرکت می‌کند، پادویی کنیم و به او کمک کنیم، اما اگر مسئولی در این مسیر حرکت…</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/460914" target="_blank">📅 17:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460913">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFTsIf8uFWZWC9OE-13Iwppq9L6xgf82wxbPAbRwvqLh9PaPvdh5Q0CXOpQfiyF3_H1Qo3s5ceD2iLS118bgleASeLR0sx-gP1CGpK4P-CZZ-vnJE3d3kevuU6HqsNqvVdjExw_FcKbqzMVbTUm2PC2V0exqveL7mLF_-yu3VJZco4xovnQr8zQNTSh2TIPLrnLwsmwT3rHiIeXUJhjchBK79XDvvUlPma1VRb37ikVcc6GX4yzLn9xLsZexgEN8-GovWhfY23c9nPL1PwO0dHaYfMjrE13euihiJvMw8kohkE1S8ml_yurBEoAe_7dD0ZqdU0gOZvMlKk-nFBcgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قالیباف: دولت و مجلس مصمم به افزایش کالابرگ، مخصوصاً برای دهک‌های ضعیف جامعه هستیم و در اولین فرصت اجرایی می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/460913" target="_blank">📅 16:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMiBIOpJbapHviAgiFfEnyj-8Jc9Tvqds5rOk37R5Lyc3s8L1hnhmTcvv0mGeUsmZkKpWCutGmW-g1isMBNb72W2a1Qc4tUJpinVA1128D4qnDGt3aSve53IbnBs7qG1rPDT2DXknX9gxxM8d73Lejv1xpVw4rSAI1UfPKjIkhtuHcBJdKh-fHRS1mJJIyCBTsH_Nw_DE85n8KfmZVmrNiKL4YkAtIKVu1rQRp8IX3uOcj4BO0Wi6IPbhymK2YT59huaPsVISk84_tqNMqIQ2wybx2qhpZbsmLyOHGg_Sw7Ak510QgOUvl5iorWKdBBrSdMrUAwgZLh7MJmtc4ln3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب، حردانی را از استقلال کنار گذاشت
⚽️
بختیاری‌زاده: تا زمانی که من سرمربی باشم حردانی دیگر در استقلال جایی نخواهد داشت.
⚽️
او  فقط به خاطر صحنه ضربه ایستگاهی در دربی کنار گذاشته نشده و از اول فصل ۳ بار به خاطر بی‌نظمی به او تذکر دادم. @Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/460912" target="_blank">📅 16:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کندوان مسدود
می‌شود
🔹
پلیس‌راه مازندران: از ساعت ۱۳:۴۵ مسیر شمال به جنوب جادهٔ کندوان مسدود شده و از ساعت ۱۷ به‌دلیل وقوع بارش سیل‌آسا و احتمال ریزش تخته‌سنگ‌ها به‌طور کامل بسته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/460911" target="_blank">📅 16:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460909">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEk16Re6GjVwf05d8DycFYg3QleHpPR0LAoPPs-fRGDEyGFul-0ALjXiMq_L2YO_yjGnTfwXiVlnOGZD0fTLV15-A1mZu0Q_4GfOWszOdZ1HT5dlCwJ79Dt5tchHyVKCBkOcsW37o-Xu2sHG2f9DiACP2QuLWVvbPL5KJOhibIXLlWjWURNL1MExrHJnZ5xDgqqXgjsVgMrE3PFDjUU2AwnJIaTBfcEhT3Uo9yS0hqZvMrEYC5hBStY-rck5r75EjXhr6Sja9ELGSGWWihCzEyNut4DePNJxm15HMkxRxf7D4LHc9ANjzytw9fW_-LobRvbgR10OTEznv7YVlrWAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2LU5_9OSeCZt4e7vPF-ZkDtzl02S15AFSCaX5Y2rUPIhoZ1g6sg-q58cLsQAui9vCyuN_vYaxLwd86s356rkH82Eq_ffTh--oEWO8NB9rBMmtFaVBTSz-U1omdBjtNttdGQ__4sH2dVAUSLZKBvth3ewggCpyc1QeZ0ybZ5CX-pmXLUUgnUpCRub8W0rwEU-D1sacQdLsfrrTIUgz4xJxLtOFDjnMRkqbkIbE1OrEIRbHssNxdKzLiVunsdprfgs2EspiZaHgIWzuQsAfbtFfGta7QFER6Ua0iQgwFQxsH91FydmNYs8lRExLgdG0SZ2SaUvPqZvvATluF1AWDMJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پایگاه هوایی خمیس‌مشیط</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/460909" target="_blank">📅 16:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460908">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV5oZBwtFUtH4GTJMg5zF8ZeyylKXFNEaG5g8O32hS5xVN2Li9WGVWg6oGLpbZf8y8t9NgzvYx__151S9DCcCgN4vp703D-dckSvPG4P9fxwh5ENsmHkyU-4GmScaRP1lRGV_LErckdrFXzgw0SjRYN6a8QbqiwaiYqBslthkUT1FlgarnIl1tOjS_YaIAANkm0usiKF8bdlVf9izxeTEuJ1m5T69ieb5PwgER6dB-mebb30j0b7b5H_xRChJD3fWuWEfnipa7NJJownC6cTQ63LyLDoYc5F60vY0ea5E5nDKEMCCxcetAiAghYtVJVhKmouykjnnQF3qUIppAJG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۶۷۰ کارت سوخت غیرمجاز در مریوان
🔹
فرمانده انتظامی مریوان: در بازرسی از چند جایگاه سوخت، ۶۷۰ کارت سوخت غیرمجاز کشف شد؛ از این کارت‌ها ۱۶۴ هزار لیتر سوخت غیرمجاز عرضه شد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/460908" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460907">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
۴ حملهٔ هوایی رژیم سعودی به مرکز یمن
🔹
شبکه المسیره از ۴ حمله هوایی جنگنده‌های سعودی به شهرستان «الجوبه» در استان مأرب خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/460907" target="_blank">📅 16:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460906">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
شکار
یک پهپاد آمریکایی بر فراز تنگهٔ هرمز
🔹
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق کشور شناسایی شد و هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460906" target="_blank">📅 16:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460905">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
شاه کسی را نکشت؟
🔹
مردم پاسخ این سوال را می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460905" target="_blank">📅 15:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460904">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy0dv2neVxwbuwu3hnbyJPLpN8VjKc9p7H-CPlrrHYel7ALQg6G2DMslX9Adz8Ma_ZJQbS3VkMAZuXnfLmtB8CRGhuuHzLWeRWRaaMNwvgDdK2IKjmWFd439e-rKGYHoPqDEIB4saM_HXIJy7BfkmJU3WlsM6OLYLWz_0S_iUAkOjbwFGrx1-vbQbCrGiWYSM2AxrC3pR4Z0aRhldhGowylV9vG_MbTCTOBra5xdhh72a1XDaCvHQUDmHtwquHQu4Fy-SkJFUktSogaVAG-SI22uVySq4qo5hp6rXUy7PXwU7wn2-dHAm27gyk1nM6g2XCb3rB9hD0zmX_Oe8_ln7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: روز بدون خودرو برای دستگاه‌های دولتی اجرا می‌شود
🔹
با توجه به ضرورت مدیریت مصرف بنزین و اصلاح الگوی مصرف سوخت، تمامی دستگاه‌های دولتی یک روز در هفته را به‌عنوان «روز بدون خودرو» برای کارکنان در دستور کار قرار دهند.
🔹
توسعۀ دورکاری و کاهش سفر‌های غیرضروری…</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/460904" target="_blank">📅 15:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460903">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bezWsNBMoeOP3GH4BqwleEsu8xHqRuy_9nJfGh3FfIdP1VNmIx7pLFq6caPHlg-fqq6Iq6ch2Sy_FkB8CIKPRnIXb8U2y1Jp0vukBzQO-xNMKLtFZEVrIChdewYaJlD9MW8doVog2_Ecu4iQZXRToYazPahIzearVC1TN3eWknAnxKK_0FxUdsVSvvr8QjOBuK_jdGHot2yRuKQcSnnQnfInUuCsNm5sHRrdHtw2gOS_82QU1ZKj1dsYr0GozlS8bpci_p6QAtjehayQceCh4wFG5Up7Ql4xvBraM2TfqxMxvnDEf-G5QSBqUcP-LMcY2t9PIuEGAnNxYDA76CsEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فرمانده بسیج در راسک به‌شهادت رسید
🔹
پاسدار عبدالرئوف اسحاقی، ساکن پراهین گواش راسک و فرماندهٔ حوزهٔ شهید فدایی پارود، امروز درپی تیراندازی افراد ناشناس به‌شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/460903" target="_blank">📅 15:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460902">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1d0866b8.mp4?token=J2QZ32BCeeUC67FKulq7Ml_6V6nUDE_Ezh8Qtn9Q3D0Cb-JmxKeKqUajt6lbRpHRJmnvbvMmfud7gZjQ5MRJBTR20eXV-RwfSRpKGH2dAbMk3FMjnXAhM3U5AFWNH4gU90Rd1KVZK77VATfPASlV2iTDSYgLWHymvwhkU9LorQBtoQDT2Lk-vrnY2AxuMdIgtLNNpxssroEMG0jYzAqQ7mToFB3JA9b4VAV3VpnzakJbao0KTTQ_Zf1nVPSwLLSsxKCiq8YYcCuU8Ok3ht9gzKx44rJ_wnbr3Y9u1JbqZCxiInuxJL4veNBJWPr-AuSpI8C4ymOuNLy65p72vDfUuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1d0866b8.mp4?token=J2QZ32BCeeUC67FKulq7Ml_6V6nUDE_Ezh8Qtn9Q3D0Cb-JmxKeKqUajt6lbRpHRJmnvbvMmfud7gZjQ5MRJBTR20eXV-RwfSRpKGH2dAbMk3FMjnXAhM3U5AFWNH4gU90Rd1KVZK77VATfPASlV2iTDSYgLWHymvwhkU9LorQBtoQDT2Lk-vrnY2AxuMdIgtLNNpxssroEMG0jYzAqQ7mToFB3JA9b4VAV3VpnzakJbao0KTTQ_Zf1nVPSwLLSsxKCiq8YYcCuU8Ok3ht9gzKx44rJ_wnbr3Y9u1JbqZCxiInuxJL4veNBJWPr-AuSpI8C4ymOuNLy65p72vDfUuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرمیتا بابا، این همونه که بهت میگفتم؛ این آمریکاست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/460902" target="_blank">📅 15:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460901">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm-dmjefWug_ZdzT0reh3bdU_xQFzmA1S3R2n5GRod5-ZpJu6kHHPzzMrCzA14Z-4P0yNfQC9dr1xhGiWnFx6FBtlpPeTthsEURUwweL2NbgvJhOn97zRn9DHJ_DZG_vzolL8asbfCC0uf9_MqN7vFhdyuFRcAFPhqPrIg-T0O_JitOHmkzI9KvgfCfBqjVtyHMRgataBr59Uii4_tsuDSDbsbocDQAQxOp5vS6TvJqNBpAUqYOT_pIiw9F91iSjykj8oHOe6ghVEVvZ9lBG0OmjVC2I_GNlzZf8a9pIHJhyE-HtFqaDQQqwahbmT4dMV7Zb8nfYRiyzk7nlliRSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری
همزمان با تثبیت کنترل تاپیکو بر پالایشگاه نفت ستاره صورت گرفت
✅
قانعی‌فرد با حکم شهیدی‌پور مدیرعامل شرکت نفت ستاره خلیج فارس شد
🔸
همزمان با تثبیت کنترل شرکت سرمایه‌گذاری نفت، گاز و پتروشیمی تأمین (تاپیکو) بر پالایشگاه نفت ستاره خلیج فارس، وحید قانعی‌فرد با حکم روح‌الله شهیدی‌پور، مدیرعامل تاپیکو به عنوان مدیرعامل شرکت نفت ستاره خلیج فارس منصوب شد.
🔸
قانعی‌فرد در یکسال گذشته نیز مدیرعامل این شرکت بوده و در ۱۰ سال‌ فعالیت خود در این مجموعه پالایشگاهی، مسئولیت‌های مدیریتی متعددی از جمله قائم‌مقام مدیرعامل، معاون برنامه‌ریزی و توسعه و مدیر مهندسی را بر عهده داشته است.
🔸
وی دارای مدرک کارشناسی مهندسی نفت از دانشگاه صنعت نفت و کارشناسی ارشد مهندسی شیمی از دانشگاه شهید باهنر کرمان است.
🔸
انتصاب مدیرعامل جدید نفت ستاره خلیج فارس در حالی انجام شده  که این پالایشگاه به عنوان مهم‌ترین مجموعه‌ پالایشی کشور، نقشی راهبردی در زنجیره تأمین و تولید فرآورده‌های نفتی کشور دارد.
🔶
صلاحیت‌های علمی، تخصصی و مدیریتی  قانعی‌فرد در فرآیندهای ارزیابی و شایسته‌گزینی تاپیکو در بالاترین سطح مورد تأیید قرار گرفته است.
@tappico1381</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/460901" target="_blank">📅 15:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Minab - LV - Eslah3-1080 (2).mp4</div>
  <div class="tg-doc-extra">118.6 MB</div>
</div>
<a href="https://t.me/farsna/460900" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📣
میناب؛ در قاب روایتی جامع
▫️
«بانک جامع اطلاعات میناب» راه‌اندازی شده است؛ این پایگاه مرجعی برای گردآوری اسناد، اخبار، روایت‌ها و آثار مرتبط با واقعه مدرسه میناب است؛ جایی برای جمع‌آوری خبرها، گزارش‌ها، تصاویر، فیلم‌ها، روایت‌ها و آثار فرهنگی و هنری مرتبط با این واقعه.
▫️
اگر خبرنگارید و گزارشی از میناب منتشر کرده‌اید، هنرمندید و اثری خلق کرده‌اید، از خانواده شهدا هستید یا روایتی از میناب و آنچه بر آن گذشته دارید، آن را با دیگران به اشتراک بگذارید.
بیایید با هم این آرشیو را کامل کنیم و بخشی از حافظه میناب را برای امروز و آینده ثبت کنیم.
🌐
www.minabmemory.ir</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/460900" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه سرمد sarmad Insurance</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awr9BQ-k_SqNQIsVPOq2l9Q3i21ic1N0oRl0tBiwi_X-D7Ux1p7xpb6fxi8foQADny-Au8MCVV40XbcOcQUVmzeut8Hi9r6JiCpy05h6xLuPIdp6LBZX7oQNyT0G8SgkiDuJjlhKm3YmCN1BQYVYeTYWf0pBH7IVgK4zHfjNErhbk9cFfSQkjoE2ZJ9NsMTUrRgvg0aiupAxMMvm_D0eYPZ40G1YY_Doqztp3S9u1DrBxKf-U1McI125bYaB9Xm8tR9zKEtWwVhw0ZkoZZu3jWq8EseQZ-nFne4y2mxn5CZaVLgupSn3biVfQgeVGuCAckeNim24TwdXHyjqvioUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ثبت افزایش سرمایه ۴۰ درصدی بیمه سرمد در مراجع قانونی
✅
به گزارش روابط عمومی بیمه سرمد، در راستای برنامه‌های راهبردی شرکت و با هدف تقویت ساختار مالی، افزایش سرمایه بیمه سرمد از مبلغ ۱۰ هزار میلیارد ریال با ۴۰ درصد افزایش به ۱۴ هزار میلیارد ریال از محل آورده نقدی سهامداران، با موفقیت در مراجع قانونی به ثبت رسید.
⬅️
این افزایش سرمایه ۴ هزار میلیارد ریالی که نتیجه پیگیری‌های مستمر هیئت مدیره شرکت و همدلی سهامداران است، بیمه سرمد را وارد فصل تازه‌ای از فعالیت در بازار بیمه کشور کرد. این اقدام، با هدف حفظ و ارتقای نسبت توانگری مالی، افزایش ظرفیت نگهداری مجاز و ارتقای توان شرکت در قبولی ریسک‌های کلان صورت گرفته است.
⬅️
این افزایش سرمایه، نه تنها پشتوانه‌ای محکم برای ایفای تعهدات در قبال بیمه‌گزاران است، بلکه امکان توسعه پرتفوی شرکت و ورود به بازارهای جدید را بیش از پیش فراهم می‌کند. با افزایش توان مالی، بیمه سرمد قادر خواهد بود ریسک‌های بزرگ‌تر و متنوع‌تری را پوشش دهد که نتیجه مستقیم آن، افزایش قدرت چانه‌زنی در بازار و ارتقای سودآوری در بلندمدت خواهد بود.
🔗
افزایش سرمایه ۴۰ درصدی بیمه سرمد
🆔
بیمه سرمد، تکیه‌گاه مطمئن
🆔
✅
@Sarmad_insco
☎️
1516</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/460899" target="_blank">📅 15:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460898">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/460898" target="_blank">📅 15:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460897">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3EztrAioN778H8tkHRnHcVxeVjbodgexp-5l5VadRXO8FLQ5Bg8bVECbJEUy2NbjtjlJNEaWkITOzaIqwF2PG39khykmihHN_nvUfG6-vO0i_OoEFNIFkad9MCPhEAQCBCgXYYjuHK64jhgljXqXgxrSgb_U2wZWX14pT0Fm7P4-3Tjap6XBxyxcLtO6ZEf46JwfWr9cD2z1UA6_ngz1EX0xanFlHBSZImFtQZpCDGFPBF8LvsajCZ7a6MDiPBNW4dlTxY47SmY86DU4XePPTPXIN0DHaz_OiZC-erU9QAlzXjltiiyKLPPtmR52tZ7D-F_e1SJ46YBMRhH0ykz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عزیزی ادعاهای ترامپ را با هوش مصنوعی به سخره گرفت
🔹
رئیس کمیسیون امنیت ملی مجلس با بازنشر تروث ترامپ که در آن ادعای پیروزی در جنگ با ایران کرده بود از هوش مصنوعی پرسید: ترامپ تاکنون چندبار رسماً مدعی پیروزی در جنگ با ایران شده است؟
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/460897" target="_blank">📅 15:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460892">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdcuFhcnZdqoNnEGKAVhJIUrwxJtCvRksCo3eRDetHkGiGbvxRnkZDYTGWG0UKTfGDDYjKp_Zke_myhl7fB-39vhs5m23ZsefSX3qKsCNWRXxR-rKwZAioprqUb5e61VyR4AlNqMTqeb9hmkUyD91yXroynnuowM3RbY00y89FHQgQ2T83w2B2d03q64Fu5I9bF-BKmU3Un8lNWigot_HzBaUr7NO1C59JVoN7jrRrpgZwiSNXvv-Gj0s38IcEZ3KcotXVzNkRyIT0iMhsjLyHUUIufp-rsqwF8oxpe0xyMUub-nuvW6zVYO8iK93xHWtK1j-STJDPwah3xSVsgI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1yeLNhprImx9QPV5zMTgdU-ZUNUDz6ciMz6CBytyv-XB4SrS1uxgJ068lJflumExgo4tM3b791qUqUbqOJeGtzaD-aq--OTnGdZPIMYrL-4LA0H7uNfWC2w8VcHFJQCqcL7L8K3JPdlBXLer-Ny6S0pEyU5oH6wLwyHtjWs6ZJGWAqNF8hscJzhTXOxCWdWD7blCkpHPD37RTyhcbCaXjZj7Hlos216V2iNeVfUKRkr4xKHLJ9kiOZiHqYYG1mCQQTImcTnn5kVsYpNJtPufdjCKcIUhd34IyrV08QQK7EOeuS1-z_8BscfjbPRFu7G_1d-z_EM7xIUQo5jdxcSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwOacFj4mAMef5CArKHaPi9V8qbcukzgmPTdqM-goXnyFzQTBh6XuzU3rUjelJ483sT9mNk0_mwFWiaus48s7GW-9PtLZTzZKKQSf-zrEAfqzodm-0neqI0U4huppvIPIGGTVaMtXyxB1Gt8GjzPZD-qMkCeaRqoCetNE1w-cMbgjhH4YzPVSnBApIqy6kL7yEK0c4HR5zOPdkFTzZSQzyP3p7GAx5ugHoL8QSSQj4ux8vXxUXfTn2pxg86ToGhSimWdK_nxiU7QVTp-lWg7YmVKLSBq0Bf15d86ZJkXW8BOo-08310rn7OisWMCQHlqTlpk8kpoo5lRzYFCQBemgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFecXrIHeIlEtsmETE8bYe1W4JhPt_DAHClhQP_EqMQadgB7lZfr2PJ2n9udo347xo582Z7o5E_DqRRqh6sbXi5pAVrU-90bHZ3S7cx1_yYQR90pMihmMoqu92oRRcvcRM9Zz2pITELgdJgMp_cRPlCsBRBALHlz2O8_4kHUYCY1cihYaYlGAu6q_WPNbzXg2vjGYvi-RYGQoC_qPHC1zHk9iv54-cPCGmqmDQaUR1nDZKLIhZNvJU0S1_2ESXs0OB6-yiXGL_8q3a1wFrVVhdW8rcS2_51MMKpWyC4BuWvybf2AW8hX_L-ntuK0ocmMUCITOHLTKcU2xrg0uET6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLQvMzXUnya479336VNUnR4SQ9s5Hib4mIQ17MaL-hin-lWuV7L8QjJABIW9RGZo1dP_SzK1n4nFWZMkp-8IRzYdYSmZ9kvpMTIPL67AnSOfPb1bI4v5pxeuN_IN2AN5E2RelTiC94OHLjl0RnfMbV8uRKKP-WeHenbVBG3XNboIFHmpe7_bB676AzVifAV1jOosvRGOq_H1ftJ4QQrIelhJ4eU21e4SgXQkTzXYdMVwoJ0U9OSRl-T7odO_uH8nBaLVCg7Ls0Yq_eOJFBEr02rnVWJYOxK6YAiOuOsRHoFVgvExUFWd1SSK6E3uZmd1bt1raRJ-txw8U88HMbAN6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: تعداد زیادی از تراستی‌ها کارشان را درست انجام داده‌اند و فقط برخی از آن‌ها تخلف انجام داده‌اند
🔹
کاظمی: بدهی ارزی تراستی‌ها حدود ۱۱ میلیارد یورو است که ۶۸ پرونده برای آن‌ها تشکیل و برای ۴۹ نفر قرار جلب به دادرسی صادر شده است. ۲۲ نفر بازداشت…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/460892" target="_blank">📅 15:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460891">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/211a9d8eca.mp4?token=rSclPNoCpSqcBnnnszWpcVy4on5QfdDzbKJKVHJcxllUhKNVKesQYeR7g36_aZ-5uXiYZ2UPWEgrY436Lx0-c-QSQ5-XsBOLCKE_cRgxlaCEg1t40l9dMNEHc42RaXxZw-ZrcRxg6cm4eu3Lq-YjWbkgtpbdq3fLSf8D3m0ZPKjfwJbNl11hqVjzQFcREmhJ77vZ0xNS8k7b2ZkU_eVxcJkUPrt3bQ39i59qGmkaXof_673KY-GUckxT3scaEAIejgTxZ84YnBujE9OAbOK95hxOp-L0VwBi-uDOD1rsHbtO-rOSXR-YPtNxBOm3cj4sqFdVXfvmThKXY0oBiZcXyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/211a9d8eca.mp4?token=rSclPNoCpSqcBnnnszWpcVy4on5QfdDzbKJKVHJcxllUhKNVKesQYeR7g36_aZ-5uXiYZ2UPWEgrY436Lx0-c-QSQ5-XsBOLCKE_cRgxlaCEg1t40l9dMNEHc42RaXxZw-ZrcRxg6cm4eu3Lq-YjWbkgtpbdq3fLSf8D3m0ZPKjfwJbNl11hqVjzQFcREmhJ77vZ0xNS8k7b2ZkU_eVxcJkUPrt3bQ39i59qGmkaXof_673KY-GUckxT3scaEAIejgTxZ84YnBujE9OAbOK95hxOp-L0VwBi-uDOD1rsHbtO-rOSXR-YPtNxBOm3cj4sqFdVXfvmThKXY0oBiZcXyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی ایران، آمریکا را دچار سردرگمی راهبردی کرده است
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/460891" target="_blank">📅 15:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460890">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3569284e9.mp4?token=snYDusVtYGUFz2uo-UEOYUX7ooP5hSelad-LgvwwZKZ6W8Yr8HnqtuU2qssibE-Poh6XT2uOflTmfXGm7LNFUsVZheJmna6F8oMdmAN7A4Z1fOr6HxqH6jzHRcydKFctX7dGr5zAqNMfBpe8LWbMXj8m9p8fbG_rpm74RqDct6xo7nWrBjeGWTw_M4bEaQaiIEw8sHBbiaSoeT2X46IibpRcvkclfEMlGKHAdQIw1kcHv4p3LdTF3vs9eClm7rpkQzUCy3w_DkllfSH9KVHhyXB6Av7DKBZqdHS7WCoUx3pKRkUYtRgJa4WIsLnY6U_U6oB9JAsG72JfvcsrOCXxoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3569284e9.mp4?token=snYDusVtYGUFz2uo-UEOYUX7ooP5hSelad-LgvwwZKZ6W8Yr8HnqtuU2qssibE-Poh6XT2uOflTmfXGm7LNFUsVZheJmna6F8oMdmAN7A4Z1fOr6HxqH6jzHRcydKFctX7dGr5zAqNMfBpe8LWbMXj8m9p8fbG_rpm74RqDct6xo7nWrBjeGWTw_M4bEaQaiIEw8sHBbiaSoeT2X46IibpRcvkclfEMlGKHAdQIw1kcHv4p3LdTF3vs9eClm7rpkQzUCy3w_DkllfSH9KVHhyXB6Av7DKBZqdHS7WCoUx3pKRkUYtRgJa4WIsLnY6U_U6oB9JAsG72JfvcsrOCXxoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جهش قیمت نفت بازارهای جهانی را به‌لرزه درآورد
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/460890" target="_blank">📅 15:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460889">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a98160603.mp4?token=nIA9YJ1liWO_1hBpm3QxsWEZ_LgMcOKK7sv8sT_606Mzx4j2x6Z-DyvVblix9k90wmS0UXr21Mjp_RwZOVkqp28olJGs1mZjUBUK1k7YDo0wgKacCg8ZsDLVOM-3X1QVNbygYxepJqyMhuEWICk3HlzQG9QVqOdz4HgJWo3qXiw-bvpCzByigVikhc25nvOcsNveI04kVmYkOlgNyHTORLYBSZCnTmWh0P-4XGnLzVwbonu66s-lOmzGLo2onoUeiRieTGvVJ676BFiiHfB_nK4_SP6V9dEvz5-6h-Ji-zEzjN7BiflKQF-ac3MCsJ9suMiRBajYz-DBXV9rJCyMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a98160603.mp4?token=nIA9YJ1liWO_1hBpm3QxsWEZ_LgMcOKK7sv8sT_606Mzx4j2x6Z-DyvVblix9k90wmS0UXr21Mjp_RwZOVkqp28olJGs1mZjUBUK1k7YDo0wgKacCg8ZsDLVOM-3X1QVNbygYxepJqyMhuEWICk3HlzQG9QVqOdz4HgJWo3qXiw-bvpCzByigVikhc25nvOcsNveI04kVmYkOlgNyHTORLYBSZCnTmWh0P-4XGnLzVwbonu66s-lOmzGLo2onoUeiRieTGvVJ676BFiiHfB_nK4_SP6V9dEvz5-6h-Ji-zEzjN7BiflKQF-ac3MCsJ9suMiRBajYz-DBXV9rJCyMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون‌اول رئیس‌جمهور با مراجع تقلید در قم دیدار کرد
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/460889" target="_blank">📅 14:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460888">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68b576c33.mp4?token=B6ZYUre728czCKkCaX2N0VuJxsasn8MXhgk-Au1MhO72R3-f6Xp9y5-26HDVrVKbLGd4asyZrlMBU2yto1yRf954BMY1drE2DGLedHg1mD-o0lBFjCC9iGxzuhtBQIMDnsPocP5V3LV06Sv3yQx42jBftcY70ZcxmmB4iNJGedDjpRXA--xRE7Kg67RMlEm0BDIzw_vuoKfur2VIFfAf9BLet72LmAA5NqC05C1e2FC1hcXIdwwTOnYvw_wYbZNnp5abhz6Bdt0cGdFZH6j0SLv-TgOlP1yZKUb7lQxsPEg5HY8Bv5hV-i8YBOZXOOodQErzdxOSLXVlP9S0mVJFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68b576c33.mp4?token=B6ZYUre728czCKkCaX2N0VuJxsasn8MXhgk-Au1MhO72R3-f6Xp9y5-26HDVrVKbLGd4asyZrlMBU2yto1yRf954BMY1drE2DGLedHg1mD-o0lBFjCC9iGxzuhtBQIMDnsPocP5V3LV06Sv3yQx42jBftcY70ZcxmmB4iNJGedDjpRXA--xRE7Kg67RMlEm0BDIzw_vuoKfur2VIFfAf9BLet72LmAA5NqC05C1e2FC1hcXIdwwTOnYvw_wYbZNnp5abhz6Bdt0cGdFZH6j0SLv-TgOlP1yZKUb7lQxsPEg5HY8Bv5hV-i8YBOZXOOodQErzdxOSLXVlP9S0mVJFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتتاح کارخانهٔ ریسندگی با سرمایه‌گذاری ۴ همت در
قم
🔹
این مجموعه که با حضور معاون‌اول رئیس‌جمهور افتتاح شد، با مساحت ۹ هکتار زمینهٔ اشتغال ۲۵۰ نفر را فراهم کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/460888" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460887">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d48a6aa307.mp4?token=TADKoWE73rWTCDihSv3mpqwzR6-sx90vvAUGN6KCt5-FOJouiDIYv3IFxMBOdqeiIccoQ0Ya20oZFoTkKo-ejtUK3eBb1QP9hGQo2C34OI_77b0CaIlOmFAgAOV7fJN06jZk6c0AjNCmFI5fKPwiNDpwuOyKTHZVvzt8E5OLSADAAgE8YoII_4Nyn6ctbRd5L59lyX3OTJGDerB8LxKRYV8uMn3jkrdDb1_IGJyRlCsMqAFwgQc3vQ8iETlgr8QKXwiTivNkTI2jnWHVi1q3xXQPEkZu-VWNRTkrdaqtbG9sEfPJi561q4Bkn7SzGOOa8WeNmDr47BlxLF-irpfiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d48a6aa307.mp4?token=TADKoWE73rWTCDihSv3mpqwzR6-sx90vvAUGN6KCt5-FOJouiDIYv3IFxMBOdqeiIccoQ0Ya20oZFoTkKo-ejtUK3eBb1QP9hGQo2C34OI_77b0CaIlOmFAgAOV7fJN06jZk6c0AjNCmFI5fKPwiNDpwuOyKTHZVvzt8E5OLSADAAgE8YoII_4Nyn6ctbRd5L59lyX3OTJGDerB8LxKRYV8uMn3jkrdDb1_IGJyRlCsMqAFwgQc3vQ8iETlgr8QKXwiTivNkTI2jnWHVi1q3xXQPEkZu-VWNRTkrdaqtbG9sEfPJi561q4Bkn7SzGOOa8WeNmDr47BlxLF-irpfiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: ساخت قطعهٔ ۱۱ پارس جنوبی برای تولید گاز شدت گرفته است
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/460887" target="_blank">📅 14:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460886">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">موافقت نخست‌وزیر جدید انگلیس با تداوم همکاری‌های نظامی با آمریکا در جنگ علیه ایران
🔹
بلومبرگ: نخست‌وزیر جدید انگلیس، استفاده از پایگاه‌های نظامی این کشور توسط آمریکا برای آن‌چه لندن «حملات دفاعی» علیه ایران می‌نامد را تأیید کرده است.
🔹
این اقدام ادامهٔ سیاست…</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/460886" target="_blank">📅 14:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460885">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb975e0e.mp4?token=BwhYHUy0S6lgihzqB_8DR29SdTjxCo8RQ2Yy_n6ckB4owpKr9rGiGvPQnX0Q7Kdi--xmp30pE_FAUrI3tybVP460tBjYnJOoCMcRvN_YalQKdi2U_1UO4oP5C7l3UcsRL9X98y_KGfRul_I5aDTmC6NhrRaY0a9fEs1N5Pzu42fbxWqteIiGCf8xu1x_xfKen4LOs9V3rwK1FhbIIAanqib79OB3we9ncIgTMlAXAve68OqaPQ6-JXnf9jiQky3mosfuWtVUwYcEOXpTqHMDUPiHry9gDWP9YSH3ne78KKj8-x950DQa5_7dZ-WoHbEE5spVR5hHkEzvb3qp56TCGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb975e0e.mp4?token=BwhYHUy0S6lgihzqB_8DR29SdTjxCo8RQ2Yy_n6ckB4owpKr9rGiGvPQnX0Q7Kdi--xmp30pE_FAUrI3tybVP460tBjYnJOoCMcRvN_YalQKdi2U_1UO4oP5C7l3UcsRL9X98y_KGfRul_I5aDTmC6NhrRaY0a9fEs1N5Pzu42fbxWqteIiGCf8xu1x_xfKen4LOs9V3rwK1FhbIIAanqib79OB3we9ncIgTMlAXAve68OqaPQ6-JXnf9jiQky3mosfuWtVUwYcEOXpTqHMDUPiHry9gDWP9YSH3ne78KKj8-x950DQa5_7dZ-WoHbEE5spVR5hHkEzvb3qp56TCGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رایزنی‌های وزیر اقتصاد در روسیه برای
توسعهٔ
روابط تجاری
🔹
وزیر اقتصاد: توافق‌هایی با روس‌ها انجام شده که می‌تواند گشایش‌های تازه‌ای ایجاد کرده و تاب‌آوری ایران در برابر تحریم و فشار را افزایش دهد.
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/460885" target="_blank">📅 14:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460884">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed4cZj2WxypHq31znxMWFVTudyrNBkoxarMI5pz9_OWYdN9V8mtVg2jzwqj_sEdfhbPhSnGMSbhDM-qenNDl_vOy6N8FSTbFHHNi2i6L4MfOIbbLmXdG_AL-dxb0Pwy2SImBOO78RBrmCZQinNlM6XQe8Ud7fLWpIVV4jK93nvrbAxoMCDN38i_vb_mVLEcjL2Zm8jVf3t2uBPXl-WCB12b8JaUNSRL8ypXYvAW7d_tf3avjVRKOU_v6CyU0oYexPE_4a5y1qtF9IP6JhmfLBuOyFF5znoRzdcUVjtvEgE-vrVNbAoGwtNiXH4hlUZIW7eZcam2cqLlgmC2brB65vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان غذا و دارو: واکسن آنفلوآنزا هنوز توزیع نشده؛ واکسن چمدانی نخرید!
🔹
سازمان غذا و دارو اعلام کرد: واکسن‌های استاندارد آنفلوآنزا از مهرماه وارد کشور و توزیع می‌شود؛ با این حال، در حال حاضر برخی دلالان اقدام به توزیع واکسن‌های چمدانی در میان مردم می‌کنند که بدون رعایت زنجیره سرد و نظارت‌های کیفی، در بازار سیاه با قیمت‌های گزاف عرضه می‌شود.
🔹
قائم‌مقام رئیس هیئت‌مدیرهٔ نظام‌پزشکی تهران هم دراین‌باره گفته: واکسن یک فرآوردهٔ بسیار حساس است و برای حفظ اثربخشی آن، رعایت کامل زنجیرهٔ سرد از زمان تولید تا زمان مصرف ضروری است. در صورتی که شرایط نگهداری و دمای مناسب واکسن در طول مسیر رعایت نشود، نمی‌توان از اثربخشی آن اطمینان داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/460884" target="_blank">📅 14:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460883">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f6d0bb2e.mp4?token=J2A5BILV4jbc6P91Ye5IlP3HkMxiIguRjiZ0XSxc2yI77avzT6pbJIBGRTgo7feDeR_mDJIW_4DLKMt5-N_xPiZp5hk55xyuHsSipykUIvyVq6036YPaAT8jbgXOZ5RUzQJLGC9JarghTl-us-RPNPqdZPxylRhKu5AN9hnAMmEuSbtlPePK6rEy0D-kJT_LH5VTxMEtyivQNHLvYQ7Fda9OMvBiu5YIhAzQc9U2HUlScrB2JLGJQ_hSco9Y-AHD4oNDjMNjZKgcYrm6Pzg97mEIdssj6i66moplJnXw5y_PKibqkT0aCGn5CRw15EOaEXvX594q4P95LCmAMlZgDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f6d0bb2e.mp4?token=J2A5BILV4jbc6P91Ye5IlP3HkMxiIguRjiZ0XSxc2yI77avzT6pbJIBGRTgo7feDeR_mDJIW_4DLKMt5-N_xPiZp5hk55xyuHsSipykUIvyVq6036YPaAT8jbgXOZ5RUzQJLGC9JarghTl-us-RPNPqdZPxylRhKu5AN9hnAMmEuSbtlPePK6rEy0D-kJT_LH5VTxMEtyivQNHLvYQ7Fda9OMvBiu5YIhAzQc9U2HUlScrB2JLGJQ_hSco9Y-AHD4oNDjMNjZKgcYrm6Pzg97mEIdssj6i66moplJnXw5y_PKibqkT0aCGn5CRw15EOaEXvX594q4P95LCmAMlZgDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانشین فرمانده سپاه: نیروهای مسلح ایران کاملا بر تنگهٔ هرمز مسلط هستند
🔹
رزمندگان اسلام با آمادگی کامل در مناطق جنوبی و جزایر خلیج فارس مستقر بوده و اقتدار جمهوری اسلامی ایران را بر آبراه حیاتی تنگهٔ هرمز اعمال می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/460883" target="_blank">📅 14:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460882">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1XoXMHAN1gVZv_BN9XeZ3vq1Cw91vK5-t9MzplOVca_Zx6UIoaelA4DvqtauoOy4wffD5VdSjNGK_76PSbp-nfY93IVa54e-2CID6K982T8LknzACUzw0PukUQSqTp26Ki3Gkv2t5FcUGLcRj8qXIg_BeYMQhF9h8BlmxPSfW6BftLDbaj8Pwf4WaZlfCbTnmfbLJwOPH-ixyUl74EZ0HYQhBsRu6cL1O7ZRBMEioITsgWj4tkXqW3LgEYsIUbz7cFcHEH8EWHviLrFVwdZ6L1vk5UGCRV1R4aY6DKK9zb693lCzmjrtEor9saNOl03HRv_8yMziU5y86xUpmDM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلمب ۴ تالار عروسی در لرستان به‌دلیل تیراندازی
🔹
دادستان لرستان: درپی تیراندازی‌های غیرمجاز در برخی تالارهای پذیرایی، ضمن پلمب ۴ واحد متخلف، عاملان اصلی این تیراندازی‌ها بازداشت شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/460882" target="_blank">📅 14:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460881">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb104c959.mp4?token=Qfjw-EGfYmioNK39n_UV-EaD1EqyllLytdPZwvsPCwEelSNgzM7M9NKYsdC8Z5yzcyX08LSihrweEe42RlKvKWBtxOerYfBFKqokvCg0PCHRNbj7q3o7Dczu3rmj4UbExKYNm5zWVOARXLgKgP1HkuepivM_UAMaXywM1svdU9vC8WrqWcXmfQqlp9i99ijjY-geOgMlLA3UW3y7veOZcMgbNIEnQUYCqmQK-y5nL6qnHR6tgGmyvtbtMGePWYJP_4vYMN1ozLGEJq_ViRlL5wvE_Irh7N0mfzxp7gsYDAv1fDaErKRemVS4hw4em6j1Ui2nhej9hOIeQF6A5LOtbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb104c959.mp4?token=Qfjw-EGfYmioNK39n_UV-EaD1EqyllLytdPZwvsPCwEelSNgzM7M9NKYsdC8Z5yzcyX08LSihrweEe42RlKvKWBtxOerYfBFKqokvCg0PCHRNbj7q3o7Dczu3rmj4UbExKYNm5zWVOARXLgKgP1HkuepivM_UAMaXywM1svdU9vC8WrqWcXmfQqlp9i99ijjY-geOgMlLA3UW3y7veOZcMgbNIEnQUYCqmQK-y5nL6qnHR6tgGmyvtbtMGePWYJP_4vYMN1ozLGEJq_ViRlL5wvE_Irh7N0mfzxp7gsYDAv1fDaErKRemVS4hw4em6j1Ui2nhej9hOIeQF6A5LOtbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: تعداد مشترکان متصل به فیبر نوری به ۲ میلیون نفر رسیده
🔹
توسعۀ فیبر نوری در کشور با سرعت خوبی درحال انجام است. مصداق آن هم آنجایی است که در ابتدای دولت چهاردهم تعداد مشترکینی که متصل به فیبر نوری بودند زیر ۴۰۰ هزار نفر بوده، اما  امروز بالای…</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/460881" target="_blank">📅 14:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460880">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
۴ حملهٔ هوایی رژیم سعودی به مرکز یمن
🔹
شبکه المسیره از ۴ حمله هوایی جنگنده‌های سعودی به شهرستان «الجوبه» در استان مأرب خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/460880" target="_blank">📅 14:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460879">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54be1ec368.mp4?token=txEfUmSEz9SOGQKWwfsD8Sf761imu4YspgcjgEvBEsQUJ2iJJh4QzMafkCqoD1hFxXGd1TKNRvhGhOcoBDtiPohd4I3g9vORXvj7mVYYb5OcIRcKM4FZCnItK-2SndYK1YaEqv_mwJK3CWfF2qhAMJHMVG4QuuZBqOr-PC2oZ7LVJUWujKaT2D1PkA029y-f6dnBEBA3vafMidhGx3UEz32sHctAx0qD21FPsCsImFTIjepk-KUKvh2Xm-wT8H9-ERS4mgtPvouoPxQ_Vks8dEP6QvDc6Llxa7Qrb50kRAHAuQF_PGhIL4aq8KVnC3KvFIoLFSzQf7wu1PnphX1XBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54be1ec368.mp4?token=txEfUmSEz9SOGQKWwfsD8Sf761imu4YspgcjgEvBEsQUJ2iJJh4QzMafkCqoD1hFxXGd1TKNRvhGhOcoBDtiPohd4I3g9vORXvj7mVYYb5OcIRcKM4FZCnItK-2SndYK1YaEqv_mwJK3CWfF2qhAMJHMVG4QuuZBqOr-PC2oZ7LVJUWujKaT2D1PkA029y-f6dnBEBA3vafMidhGx3UEz32sHctAx0qD21FPsCsImFTIjepk-KUKvh2Xm-wT8H9-ERS4mgtPvouoPxQ_Vks8dEP6QvDc6Llxa7Qrb50kRAHAuQF_PGhIL4aq8KVnC3KvFIoLFSzQf7wu1PnphX1XBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارت زرد مجلس به وزیر ارتباطات
🔹
در جلسۀ امروز صحن علنی، سوال علی جعفری‌آذر از وزیر ارتباطات و فناوری اطلاعات با موضوع پوشش‌دهی ضعیف تلفن در جاده‌ها و روستاها، بسته‌های اینترنتی بی‌کیفیت، بلاتکلیفی بازنشستگان مخابرات، رهاشدگی فضای مجازی و بحران تلفن ثابت مطرح…</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/460879" target="_blank">📅 14:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460878">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1KaO-AD2UanqTwhmvZMpSaRSPUI3BnE_iKrfUmDH4idwuaTJmeeywmGxe8K7Dnx5NCoSVAMhx4q19Q72wv_Tmb3nQ3goARXaFwRB2qNfO8Q5K-kUGzIWjIrH1VrGGJh1FsVaIDUCqxwQvjK9Vq2QdLCL_SI0wrDeiTxoAx54ZpG6Bs2ZHRLsKfzdrObP3PjODkilYH-1fYr5BI4nIhU3-bJMBDEWKSAzhFUhOEcmHr1b5autS9-tJ6SU4HBwwxaXhUvXZ0-RBRYZwR2MnDxR6i36efuR5NoWVijwOaJc0jUwQGxdQ5CquXfBEFjlPg9rTtUxEXqj2ET6ZTrP_Q3jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار هواشناسی برای ۱۵ استان ایران
🔹
هواشناسی: برای ۱۵ استان کشور هشدار هواشناسی صادره شده است؛ در برخی مناطق رگبار، رعدوبرق، وزش باد شدید و گردوخاک پیش‌بینی می‌شود.
🔹
همچنین برای بخش‌هایی از گیلان، مازندران، غرب گلستان، کرمان، جنوب سیستان‌وبلوچستان و ارتفاعات هرمزگان هشدار نارنجی صادر شده و احتمال سیلابی‌شدن مسیل‌ها و طغیان رودخانه‌ها وجود دارد.
🔹
در نیمهٔ شمالی کشور کاهش دما پیش‌بینی شده و دریای خزر در ۳ روز آینده مواج خواهد بود.
🔹
در تهران نیز امروز آسمان نیمه‌ابری است و در برخی ساعات رگبار، رعدوبرق، وزش باد شدید و گردوخاک پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/460878" target="_blank">📅 13:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460871">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HC_TWc2bwt7JDA1th-uLf7xEY3YBesRi5UPvMwx79UpzHjABWP_bYK_zC9KfWzhfbEHg33x6lOnZh9CRWpGf1Z-P7MzpOvwJ1egd1nZoofkCuIzZdzwd6TPS5T2dedSoU2LcM82ts8v_3h68eu8OkJ-EiQnPjWa-R7kZ4X__K5JtwCQHqQq9W1xyUQcaU9yTlbheAtb1Qu-nkD5vevPo9kPeLkZmPPEKkLfgbwzzisE4veFElShbq3N4XC0mDDQ-Gzye_wEOktAO9baNLjvJFHY5-coZkPvN8PruZTIcreEI9dSrAJcoEXzy481lM_adRIdVoaqkO9132CWEomkHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5Wa4lNq68FFlIywuBD0nwvwlqX9K3LD_a3d2oQE713HSx7SSllsOhBVPot0uWY_sC_LgMrM5r3DCIFMJ2scKU8XPItBxY18l9KVXySg6JnWJAyaLNiD2fMWIHLJd2xtKTH4YUDyhMcAcAqmt0aYzn4iUNnAuxvM9-21aeC0dqi6CE0rzS7FgkpGk1JUSEG5l7FaHB7Lu52r6Dq5lcrYrA2F5pGmI7vYYzYFGNASypa8YYS-j9AAiDCvh8xyENNyWp5otQLZ8-FEgU12UqlTtnPTVS621IRHCtwBjVb0zqQmWAoZGGC1V-LVPkUa2wK_ZFHFwd8LfnkMdnCxoQ-qsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J03rUds65wOOVATD26Ta0IXzzxrsq3qvhFHyU5Sirw8H_FQ0Fpl-D1qV8obIHV0lfnNm-jqbRUhJjp43Sy2lgx3GzdRuKbXv19LsPUy6XAC5O0ttyC6map3Q8SCDTpmAY6oOJ7xwDBCZRBnhHc0zvDZxWjk21_4bAwmH1seeLfgfC8WplXA-tGZhM8X54tgwHuz3-1Qa4h4ZZWKwEA-4f6o--UqStJevRyMrggU-biulvWCjUYEEVxpLxHCEbB_RLcn2GnW0nwozkvWzebB37kWyZmmRgP_2aGQuJpcrVzHwL5SjfuL6QgPgfbTXgc5p8vUqcIvvOlx6dhatrXup-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anVU1CLdwiptaoH1_uMzi5GDFUqO7mqOiplQ5MRHk0vyGaSyVNBN4h7STT67uIcsCLCuhWOfWmaxsydRAbBPXUQLVDL4z3kiaiEaahsTb5m2wfLOgFofkDFXNe815pSA2X3eiWrlvtDWTO9g_EEPjot0RHQ54aLi23oA42uiQhXF7m3CbQPCxad8z7jmyaL6pkddN0Pwmpw2eZWxSE_2eT7yZ1lMkbQyVftbVZvwviHzNU-UILdp0zc6LHZb-psZdJPuIMX3kW3G44P7O3MuCH9RcbQsz1z-Izu4hxWHodh4PJsmrhOGvXdmosYDYMnWVJ78LXD21r_Fl_cm9iDHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCYduqncxAZ3yl8GCQ6mu4o0cYZoHbVfR0SAkWdyL3BsWCdd-DpUHG0qR3S-EoA2TvfEW3I_PjT9jXhK9LM6CyQ34YOFgl7_UOl2XroLJ-NxVIYZGfyNZEugLAcm4NItv9-SjxWv6Rz-3cycSsow4qOg_in2Xndgy3xNn4NmFxrT75bKszQIRj_vyy-hUThaiL6avjqqyCn6R-YE6FVElEcBOhbprHVgeYuRH4KoDlg5sqh3-BSJ1lvKtHLeWCrzXpxQQLbOq0RasctPs7W5yOhCBw0n2y6Uw3rBZ8cZ3L18sdrmmHd7JakzDkk0aE-v0__0pcNX6QHoUSYP31LMKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQXfilMSBJ51EIzTnsz0UGyaNeE57WJALmvrRL_lsSkh-pPblC67ce3YxFbrhNJ9Z2ZLdKVHEyNoKDNM1WPE2zSjJX7jZQyoiiJO2AhO4-rliMl0y8GqV2cIT5M25sGjgS0XLm5EiCCgRkbtqvOYDbu1w1ztcBbr5K84HafZY7Hqk15oSbchNEgb2gPZ2jn_KTcC-aSUujk0c0-GHVXF0LhHF7F3qLY05lStulJ2HU4BFCMholrcAQ8l6swFmVpTeyzjLxDjdaE8aYelrmolyMWpxWnMNQkttBJRQweFq8-ozTc89tZHpiWJeQuL006IhHbOy-lLyDoYVSpTJ5PGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6LQqSEBf-KXbpv8hGe0b-TsXk5AIWAe9Fm7l8EIHjxxq6SEwDQBER39XT01S5e2V5dBBx2UUSe0hdaHMNEgVcUcr7TO9paM-AxTkukLlfl_VDTnrl8ilzuMhHWsD0QwIw9xg45Ctp3j8XzLhGCvC7mEDq7jNJ9_-sSfrw3oeC44icjrmZrZkzxaiPhJ0eKKX9Z_MhVaJ6-in8qta2txk8e8bqCGOWnI6Ell2F4HzCtuhSZVgWrhQhrE6XDIHlyAqBzDsU3SLdhyWkese9wLHGskivAtciXDU5yJldravDVnlEaORDhTBbdrxZ_ShaqfH5XBJ95vTeWJ9Ugs1VdNcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: ظرفیت حوزه‌های علمیۀ بانوان باید در خدمت حل مسائل فرهنگی و اجتماعی قرار گیرد
🔹
در بررسی ناهنجاری‌ها و نارسایی‌های امروز جامعه، باید سهم و مسئولیت خود را نیز مورد توجه قرار دهیم؛ چرا که مسجد، مدرسه و دانشگاه در اختیار ما بوده است، اما نتوانسته‌ایم از این ظرفیت‌ها برای انتقال صحیح و مؤثر مفاهیم و معارف دینی بهره بگیریم.
🔹
باید ظرفیت‌های موجود در جامعه، به‌ویژه ظرفیت بانوان و نهادهای دینی و اجتماعی، به شکلی هدفمند و مسئله‌محور در خدمت حل مشکلات مردم قرار گیرد و از این سرمایه اجتماعی برای ارتقای کیفیت حکمرانی و تقویت انسجام اجتماعی بهره گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/460871" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460870">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4_N0PAZGUDtC4yUPN-DLSO17Sqd5UBMG1X2w75mYPuV4GbsHQmzPf8sxWt2uLIZF3CwJV8U-1Q_pM_tAFdAdQeWfUyXzmP5LLp3UFEGeYKyDWcn6hl_uh40ekoCVu1uHQmJo8ZunMunN0DYm66KAsKHWZfqsxMtqQEQO-fdrKUCq-iB4XyVIEV2YjNoC8UnbC7VTCYBitfHV4Pv2d9k71xccCUNcqYZjhCqcR7qcssm0hWlX5fSwiofN565gAeQ__FJFLfQaInbjiAMNt6XE8iZRK_xsYxA81tK_nr9hj5RAIOlYD7K6pKyucsT4uukT9B_rx869ugIxe9bk2Y5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بسیج اساتید: علاج کشور در هتل‌های وین و اتریش نیست
🔹
میرسامان پیشوایی: دروازه‌های نظامی و اقتصادی کشور از طریق علم و فناوری گشوده می‌شود و علاج کشور در هتل‌های وین و اتریش و این موارد نیست؛ بنابراین نباید علاج کشور را آنجا جست‌وجو کنیم.
🔹
علاج کشور در…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/460870" target="_blank">📅 13:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460869">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQnlbzr_4JCGGPQVM0VNIw1sucuuezPirnreg4L9io9qLLgGoo3S_zF_AcZy5LGIpT4L0KXHyAme1F0oGjAaWKBzTLksuTGjLasw1caf3A2gbSi1SiszkvfDg0FlU6J_tHCOl8Fp1aYI0gkEcPrBCSufSbyUHh6KS8HxWi-4zGdVK9RBLdpzqWTVvkgOTViKoa7VYEGKTojdXRsRr7Q17PpKe8gpoY59Qq4nvB8fAg6BVgzjxTXXekLzr-OTxX5IEy9GP3CYH9dEfw967kAzolSD7eUlCXimR5Zo5eu9YO1iU2SyFBK8WFdBStRg9KRH9LgkbzMnM9maHic3sV9mRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس سازمان بسیج: ان‌شاء‌الله امسال ورود ما به دانشگاه با جشن پیروزی مقابل آمریکا و اسرائیل باشد.  @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/460869" target="_blank">📅 13:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460868">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4zxCszgeCTTHUPmNVnAMPegqKcueElLLj00MIRvOGjGvbpGOM73Pk_LXOnNGFDiHLP99pLbwjz83bSuxHHbThz1I7o1dDvRFyCHqmh7jg0SecwuJ0tYSzcdZGSXyjuSgAWUMx6NUOcgHOHEKB7j2sdZnv73oiQoN449Dv9nlVuOYxlHFXCSGHuZ2JVFBU_9959FqVz4LpjNGhzatMTseqXhyeXQubguAbTPJhpoMxYP72H2cXthB_EmohemUReiNv5xEMk1MYi0JS9nUH3dfAXEvNxhTz2Hg-KFnfJkJx4sCE-mNWLcHQiKzOGn4hHX2I5Zflm8o25bUejerAy57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در تماس با همتای ژاپنی: وضعیت منطقه به‌دلیل نقض‌عهد آمریکاست
🔹
وزیر خارجهٔ ایران در تماس با وزیر خارجهٔ ژاپن مسئولیت وضعیت تنش کنونی در منطقه را متوجه نقض تأسف‌بار تعهدات آمریکا در چهارچوب تفاهم‌نامهٔ اسلام‌آباد دانست و گفت: «راه‌حل ساده است؛ بازگشت و پایبندی طرف آمریکایی به تعهدات و امضای خود در تفاهم‌نامه زمینه را برای بازگشت به وضعیت عادی فراهم خواهد کرد».
🔹
عراقچی همچنین با تشریح آخرین وضعیت مذاکرات ایران و عمان دربارهٔ تنگهٔ هرمز از پیشرفت قابل‌توجه گفت‌وگوهای دو کشور برای تعیین یک مسیر موقت تردد در تنگه خبر داد.
🔹
موتگی، وزیر خارجهٔ ژاپن هم با ابراز نگرانی از تشدید تنش‌ها در منطقه، بر ضرورت تداوم رایزنی‌ها و هماهنگی‌های دیپلماتیک میان کشورهای منطقه و کشورهای ذی‌نفع با هدف برقراری امنیت در منطقه و تردد آزاد و ایمن در تنگهٔ هرمز تأکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/460868" target="_blank">📅 13:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460867">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b40c83147e.mp4?token=lcX2-93C2sd8kmP62UpwDr78UyApZN2P8DrHH_va2HgACDDa-NBhvxACN-7T967EZfH5_lUa2x8by1RwqHi1eea1zrd1Qb4zjenh6-Q-l6DZeYC0tR4A5PAweKWSRFx52V7W82LB1ZeifEsDDNkKaRVx8rnBmglqYLlgZnhvDlddxdTNsk6EexIUMr1HdV760d-F5Llh2NZvPxbUKMMPipa22w81nAvWYs0AmZrslsHsnqau50rEFHIxRJThtDmrFZe-UtHF-_NqcWJXX6pMZfN85XoyWsiMA8juwp20iMQ0wjNZfpACuqs2Hg96s2nzGS5-XW4CSXS7ub31qY_ivg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b40c83147e.mp4?token=lcX2-93C2sd8kmP62UpwDr78UyApZN2P8DrHH_va2HgACDDa-NBhvxACN-7T967EZfH5_lUa2x8by1RwqHi1eea1zrd1Qb4zjenh6-Q-l6DZeYC0tR4A5PAweKWSRFx52V7W82LB1ZeifEsDDNkKaRVx8rnBmglqYLlgZnhvDlddxdTNsk6EexIUMr1HdV760d-F5Llh2NZvPxbUKMMPipa22w81nAvWYs0AmZrslsHsnqau50rEFHIxRJThtDmrFZe-UtHF-_NqcWJXX6pMZfN85XoyWsiMA8juwp20iMQ0wjNZfpACuqs2Hg96s2nzGS5-XW4CSXS7ub31qY_ivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طائب: هر استاد یک بسیجی و هر کارمند یک بسیجی را باید شکل بدهیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/460867" target="_blank">📅 13:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460866">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVQxFBL5a6TxBSAVVW81bdDAauzWXGOjA2suJXnv7w5nfUAK4cRFhn_8cX3A5yjD9u_tuPtcxonYeZKbTi5WmoMi3NxjY3jfXS6BPcnbbjrkhWo7DSusUbIqV7tXqIAJxgNL8Z6PCh2-P-kBqDdJe-y4u_y_4hDHdsijbSHDhP48QCgzOLjCOBz76jFj8n2fetymqpfnA7gby0vIEpukW85X8e7ZNDI6ogFpw4IjK0Dp2wpRFTm45Zgyb--uET6BUADIEmsVAlser9vpUPDum_m2aAeZ7y98pyZvnCKWI7_UFEToSjTKMzGLJcOoVjC439IzBIwpKsdY5RpfBlwB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: ایران تا پشیمانی کامل متجاوزان، با قوت به مقاومت ادامه خواهد داد
.
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/460866" target="_blank">📅 13:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460865">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31884a3da2.mp4?token=N87CvP-GTTYxDl7BRG_mm-utGonxEsKWvw0JhNu7-vkxBMMjgSCqlwfxQQja_4ePRhORA-bz0XuWH9hvp8eJfX_bAxSxSJimcw1Xp7d4rTzFug6J2AcCibd9YS9fmGhV_RlVPnBTQRc16VTNlycHpuJAZpYclONiqKXtlwBn4LF4oO-EbRRzYsjzZQsGaMnqkhFWKDpa_qpndfxPKHe8SUrpiZqqrJhHuxwXd0gYTZgwkrq_HtcSpkrKiwfGFLQAQNZH2vwM-k_PaaqY2yvtC36e8QVQabzGtfvd8iTI6MyUYjn9jNkRuTE3civP8DId4Uc0dju-zJI6bw4BrM1vMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31884a3da2.mp4?token=N87CvP-GTTYxDl7BRG_mm-utGonxEsKWvw0JhNu7-vkxBMMjgSCqlwfxQQja_4ePRhORA-bz0XuWH9hvp8eJfX_bAxSxSJimcw1Xp7d4rTzFug6J2AcCibd9YS9fmGhV_RlVPnBTQRc16VTNlycHpuJAZpYclONiqKXtlwBn4LF4oO-EbRRzYsjzZQsGaMnqkhFWKDpa_qpndfxPKHe8SUrpiZqqrJhHuxwXd0gYTZgwkrq_HtcSpkrKiwfGFLQAQNZH2vwM-k_PaaqY2yvtC36e8QVQabzGtfvd8iTI6MyUYjn9jNkRuTE3civP8DId4Uc0dju-zJI6bw4BrM1vMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بسیج خطاب به ترامپ: اگر نیروی دریایی ایران را از بین بردی، چرا هنوز در تنگۀ هرمز می‌جنگی؟
🔹
طائب: دولت آمریکا باید به مردم خود بابت راه‌اندازی جنگ با ایران پاسخ دهد.
🔹
طبق نظرسنجی‌های صورت‌گرفته در آمریکا، ۶۰ درصد مردم معتقدند راه‌اندازی این…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/460865" target="_blank">📅 12:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460864">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7010c9344f.mp4?token=gqP71Xj1HZHKrxI63lqxyH2erZ6jwb9IxinLj1qEO5fhgvNTTYQ_pYv1caG4dRkYjB-MZuFz6-Er7Hn26PzAAK-1jZzlQQZ-530heJ84Vyg0x2w_eULZtIqan0qBTEk5ACHIjHzL2Ik5v-Hprs6Gx8cZK6wjHMvaAiheSyzO6dZpNyP8d1yR_Zv3d68X7krDcYrRzTqIFNDN0qTWPZZSdYkZ14porPPcm_7Gu_EfAjn68YUdS9IG_rpQMpj9e9WJ0VcsdWGVSYQAoXvNM3vumWFeLFvaXuiZhdfKIAcrdYPXyiXxtJW0jKPkM8kBYSgIdeCj-yWfBr25uEV_petWEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7010c9344f.mp4?token=gqP71Xj1HZHKrxI63lqxyH2erZ6jwb9IxinLj1qEO5fhgvNTTYQ_pYv1caG4dRkYjB-MZuFz6-Er7Hn26PzAAK-1jZzlQQZ-530heJ84Vyg0x2w_eULZtIqan0qBTEk5ACHIjHzL2Ik5v-Hprs6Gx8cZK6wjHMvaAiheSyzO6dZpNyP8d1yR_Zv3d68X7krDcYrRzTqIFNDN0qTWPZZSdYkZ14porPPcm_7Gu_EfAjn68YUdS9IG_rpQMpj9e9WJ0VcsdWGVSYQAoXvNM3vumWFeLFvaXuiZhdfKIAcrdYPXyiXxtJW0jKPkM8kBYSgIdeCj-yWfBr25uEV_petWEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بسیج خطاب به ترامپ: اگر نیروی دریایی ایران را از بین بردی، چرا هنوز در تنگۀ هرمز می‌جنگی؟
🔹
طائب: دولت آمریکا باید به مردم خود بابت راه‌اندازی جنگ با ایران پاسخ دهد.
🔹
طبق نظرسنجی‌های صورت‌گرفته در آمریکا، ۶۰ درصد مردم معتقدند راه‌اندازی این جنگ ارزشی نداشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/460864" target="_blank">📅 12:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460863">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8ZFWDX2boJP4I6mGwEvLz-VpA9xR9OvUJ6IXOdswuGQk66lr_e_hLKcVctdR32jGioDaUz8sTSNXQLPtryUao-1qAOKKb5kqCr4dvX9dbFxpb2iIxxsUdXiMf54h7w8pJY-Hf5hevCxtNmpTalL2pzrK-QNne3jYFo3xvp97bBdHq5fxjcbBq5BRytSMSWU-rHCJVRMq4K1uPWoV8l-29F5pBX0KfrlVvs3pTlfumAK_qCe3sjlLLpIVmdYNbgNgARUGSxo5ewD5Y7LF2A3cYIfc9LsZB6HxGqsV48K4WgQiB44yN2jfkgV-tLuuhaXvOIx-X6Kt5aZ-tKSQsrCbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس امروز را ۷ میلیونی تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با افزایش ۱۶۷ هزار واحدی به ۷ میلیون و ۷۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/460863" target="_blank">📅 12:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc7b914dd.mp4?token=ecu86_GkuzxAV_yax-OgX3tGT7MelLZI1RbSwCB-Z_XQFGQsZnbhe1A7knurV1nddJ27oDAGN6FZNMWOpLbAwrNHv_363hE9lrBg7s9etJ0B_0JAx_DGfp0ezHP9cipV2uR3aOFOMrDlsPSUWbteewrDV7SzCPT15vgZAl8crZYJli6DMXPY7R_uLgU0ZlcUKH0pErz7gZ5WofpxaXWtgoPNu8DkTwIznx-lgrkhf5fZDrG9KNuBnSdo5xGUtiO9zevMqd6D_p1ujB1YtfShmWfHn9OeS3ZuZ-fyeECFvZYgWuYgD75CWXfegHXrrnEWEROxv0JF82OipDxklc5Isg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc7b914dd.mp4?token=ecu86_GkuzxAV_yax-OgX3tGT7MelLZI1RbSwCB-Z_XQFGQsZnbhe1A7knurV1nddJ27oDAGN6FZNMWOpLbAwrNHv_363hE9lrBg7s9etJ0B_0JAx_DGfp0ezHP9cipV2uR3aOFOMrDlsPSUWbteewrDV7SzCPT15vgZAl8crZYJli6DMXPY7R_uLgU0ZlcUKH0pErz7gZ5WofpxaXWtgoPNu8DkTwIznx-lgrkhf5fZDrG9KNuBnSdo5xGUtiO9zevMqd6D_p1ujB1YtfShmWfHn9OeS3ZuZ-fyeECFvZYgWuYgD75CWXfegHXrrnEWEROxv0JF82OipDxklc5Isg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاده هراز پس از ریزش سنگین کوه در محدودۀ آب‌اسک بازگشایی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/460861" target="_blank">📅 12:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291f3357ba.mp4?token=F3ghmF-NkVmsYvt_ulkl1u8fGJ7u2nSjGlRglXF0rfWxfLJ27y7CUum2YJT102_ArIJzjV-ny157zE43x3QG2bX6bG6pA0PTVMskzbutME7GySc9hkhk2sdX_9fqwweASdD4UEGvxg46LZgi2dKxhajGIbuU0TW09Cu_Ad9wk5ztYWKfxooV-2sirbWd_i211EGRYLQYQsG4mk6fQ5G6UNPSWF4AGMGdXhV_nMj3DoR7Ut3jkp0J1NMqcPR5Y3phPioalzwaz8Zz1jSdhGtyLJiyq7zhNeTndEha7jNKy433vhyMemC4di8GL0t2UmHFc1b4ntjungEKkgmKHFB79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291f3357ba.mp4?token=F3ghmF-NkVmsYvt_ulkl1u8fGJ7u2nSjGlRglXF0rfWxfLJ27y7CUum2YJT102_ArIJzjV-ny157zE43x3QG2bX6bG6pA0PTVMskzbutME7GySc9hkhk2sdX_9fqwweASdD4UEGvxg46LZgi2dKxhajGIbuU0TW09Cu_Ad9wk5ztYWKfxooV-2sirbWd_i211EGRYLQYQsG4mk6fQ5G6UNPSWF4AGMGdXhV_nMj3DoR7Ut3jkp0J1NMqcPR5Y3phPioalzwaz8Zz1jSdhGtyLJiyq7zhNeTndEha7jNKy433vhyMemC4di8GL0t2UmHFc1b4ntjungEKkgmKHFB79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای اولین بار قرارگاه مشترک مبارزه با گران‌فروشی و احتکار در سطح ملی و استان‌ها شکل گرفته و با این موارد قاطعانه برخورد می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460860" target="_blank">📅 11:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cfb970427.mp4?token=najBNT0rANKxuDfHUZPDZL3XqXiXLUCksjjhVtRneb5CC5cudQHIlN6Ylhql2BFRhRV_zU0QUoRGxL7KfBnLYmznofzKMmUAo_aWz4r6-ID59UOtWtK5sS48Su-ciAFO52FZMVQ5x0QF8xTvoRpKPZOWHxqIvg4bQXO1sBx53rd2PT91xmlfa7bM1bKuou_8iOGPyUuRdcVUbu_j4i0ikzPQ9t0eQXrty2UF4iSQYAPnEBabhscUTxwbW4G_4vpb8dZMW6LDTUkz3XOJgAvFG_mGY3rmT67b63k5M3BE17QG_19ulwy8PlOtW0nN546zqCiZ_S7LTklBPeTmo1DSlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cfb970427.mp4?token=najBNT0rANKxuDfHUZPDZL3XqXiXLUCksjjhVtRneb5CC5cudQHIlN6Ylhql2BFRhRV_zU0QUoRGxL7KfBnLYmznofzKMmUAo_aWz4r6-ID59UOtWtK5sS48Su-ciAFO52FZMVQ5x0QF8xTvoRpKPZOWHxqIvg4bQXO1sBx53rd2PT91xmlfa7bM1bKuou_8iOGPyUuRdcVUbu_j4i0ikzPQ9t0eQXrty2UF4iSQYAPnEBabhscUTxwbW4G_4vpb8dZMW6LDTUkz3XOJgAvFG_mGY3rmT67b63k5M3BE17QG_19ulwy8PlOtW0nN546zqCiZ_S7LTklBPeTmo1DSlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: در رسیدگی به پرونده‌های دی‌ماه تمام حقوق متهم رعایت می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/460859" target="_blank">📅 11:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460858">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee10be90c9.mp4?token=ezwtflkqY7wz8EF98ZK8BARcMsxksUtL0u0oIECeYoyc-mnMo4IqB6k03BRc6arS1m86fTl_-jpmllX0iCCwiKDAmMrvb_oVwa80FybOHYjaFcWnsce5Bx1221wiMpz2aS7aNWXE3RMGcVo1Ikzl8k1aZ0X9vBRDhoXMpSmLRMLX-Nlldw7Htzqv0bbXo2BvjTpf13Y3IAJ6B6cvP4aQKB12_N9o5Hv9WHLalsqoqk3WCL5s0hHeg4Zb8-zMfVnPlwlJEewtLzyIUU58AkdL4akszBBWHTL_98rSJuAYPclfIDdtcPfStDSoKaZxW5hFbBOpfSnbJZ_-JBKJKvT7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee10be90c9.mp4?token=ezwtflkqY7wz8EF98ZK8BARcMsxksUtL0u0oIECeYoyc-mnMo4IqB6k03BRc6arS1m86fTl_-jpmllX0iCCwiKDAmMrvb_oVwa80FybOHYjaFcWnsce5Bx1221wiMpz2aS7aNWXE3RMGcVo1Ikzl8k1aZ0X9vBRDhoXMpSmLRMLX-Nlldw7Htzqv0bbXo2BvjTpf13Y3IAJ6B6cvP4aQKB12_N9o5Hv9WHLalsqoqk3WCL5s0hHeg4Zb8-zMfVnPlwlJEewtLzyIUU58AkdL4akszBBWHTL_98rSJuAYPclfIDdtcPfStDSoKaZxW5hFbBOpfSnbJZ_-JBKJKvT7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: پروندهٔ فرداموتور ۹ هزار خودروی تحویل‌نشده دارد که بخشی از آن در حال ترخیص است.  @Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/460858" target="_blank">📅 11:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460857">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c66a69a8.mp4?token=I_Jslu0LKyGyopSuNLlHsAilIdYMMka0YQ-YV5oVSmagzQ-qF3ubfmcpF5h8F95pNTk9ppIWgEKHHO075_ZqDD_iglE7u1KuzNNes0NGrhwMrh3nXldi4thbOWLVZFdyFIpMM928WfDinVMlTGjFOdLR8yxp4eo3j3A1Zqf1istysfgbnhQnW1Tr_4ID2yvCo6-h9F9-GZZocT2EvvkPx9bSEcv1sQSRmsXokHwIBZGAfaDMvn5uLvnBGG1gfDXIIvMIluhG0ZNBvi6JuYkd7Q_mf70Gz4q6QEGxJwzuBkOUjYL-UcVu2yNTfIk0JW509QMHr_t95p-2W-ZK-XHSBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c66a69a8.mp4?token=I_Jslu0LKyGyopSuNLlHsAilIdYMMka0YQ-YV5oVSmagzQ-qF3ubfmcpF5h8F95pNTk9ppIWgEKHHO075_ZqDD_iglE7u1KuzNNes0NGrhwMrh3nXldi4thbOWLVZFdyFIpMM928WfDinVMlTGjFOdLR8yxp4eo3j3A1Zqf1istysfgbnhQnW1Tr_4ID2yvCo6-h9F9-GZZocT2EvvkPx9bSEcv1sQSRmsXokHwIBZGAfaDMvn5uLvnBGG1gfDXIIvMIluhG0ZNBvi6JuYkd7Q_mf70Gz4q6QEGxJwzuBkOUjYL-UcVu2yNTfIk0JW509QMHr_t95p-2W-ZK-XHSBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: محمدباقر خرازی در بازداشت است و پرونده‌اش هنوز به مرحلهٔ صدور کیفرخواست و حکم نرسیده است.  @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/460857" target="_blank">📅 11:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460856">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf6253d754.mp4?token=baL-u5c-a9bk36oskyLgvj7HXg9-TQRIwdec2q-bbiEsacriUWRFELCrM5SW2mVIcTpkXzcecWyrRLbcPqq56wH34ncLRLf2CVxFqCKS4A4s2xMWGYHKCeyU0c3zj339jm9Y9ZQCqUtyLuOvQHD1v2YynaqmBJqiuJcRTx1Cu1pm01UFILoD_LPXA-vMh5BnGHQmFT7WURn4Nx7OGDHQM7QAECFgmMOZEcO6rTalvREDwtmng37EfowWPjNsWbaVf6tez8i9PYvw-7J-4kVSOgBJYTojnsB0DBXRai825aTqDOEF5X1pqeYMC-SbDzB8Qnv1VVy0tfcH8Sr7RnAS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf6253d754.mp4?token=baL-u5c-a9bk36oskyLgvj7HXg9-TQRIwdec2q-bbiEsacriUWRFELCrM5SW2mVIcTpkXzcecWyrRLbcPqq56wH34ncLRLf2CVxFqCKS4A4s2xMWGYHKCeyU0c3zj339jm9Y9ZQCqUtyLuOvQHD1v2YynaqmBJqiuJcRTx1Cu1pm01UFILoD_LPXA-vMh5BnGHQmFT7WURn4Nx7OGDHQM7QAECFgmMOZEcO6rTalvREDwtmng37EfowWPjNsWbaVf6tez8i9PYvw-7J-4kVSOgBJYTojnsB0DBXRai825aTqDOEF5X1pqeYMC-SbDzB8Qnv1VVy0tfcH8Sr7RnAS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای مقابلهٔ هوشمند با فرار از دِین، سامانهٔ سهام طراحی شده و تاریخچهٔ نقل‌وانتقالات مشخص است.  @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/460856" target="_blank">📅 11:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460855">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e3d77ad5.mp4?token=dWR1OgO07btQSwf6EbE0B4AW7sOkUoFAh42qpgB3ZCIPoWd7PQH4ISnl26WfQwFo8AtOczHJiabjZPlDZsRQ1l3LcbxgWrZi8YqGn9iUM-mpVFoj-bBxCB9sQ3i-j5MsnFJpiz6eS5ZGBlV-_t2J_NTOgMe1YgtqolzBU2RXE45zsnM-yqJpDvdBUHjsjY6RyVKwH4hAOvUGxbutmgeT8j_ouKyeZfF2PsVtXTebDVJE093qUbCI3ml1p862U8scCMfZ-AqS9XU24j94Y5HyWITZ1XJ04S9zgktNtF85muIJqPcjeD7VHLQwMdXQgwCrn72wvscQQc2JzELqJLNfoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e3d77ad5.mp4?token=dWR1OgO07btQSwf6EbE0B4AW7sOkUoFAh42qpgB3ZCIPoWd7PQH4ISnl26WfQwFo8AtOczHJiabjZPlDZsRQ1l3LcbxgWrZi8YqGn9iUM-mpVFoj-bBxCB9sQ3i-j5MsnFJpiz6eS5ZGBlV-_t2J_NTOgMe1YgtqolzBU2RXE45zsnM-yqJpDvdBUHjsjY6RyVKwH4hAOvUGxbutmgeT8j_ouKyeZfF2PsVtXTebDVJE093qUbCI3ml1p862U8scCMfZ-AqS9XU24j94Y5HyWITZ1XJ04S9zgktNtF85muIJqPcjeD7VHLQwMdXQgwCrn72wvscQQc2JzELqJLNfoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: تلاش می‌کنیم با رویکرد صلح و نگاه مددکاری به حل‌وفصل پرونده‌های مالی کمک کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/460855" target="_blank">📅 11:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460854">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a6d40fc.mp4?token=LsY8bdTQqJZsBzS6YYbuIUNufixnUw1xpN6kyOI2S3SPZGEjRV9ZH_EFVhM9Kd4W9MO7ET7eZGremYxmo5edR2XxBuAyUaeYBxUt_oSStnQB7kkza3a9gIXHjfUwaqlNWUNTXk9lhvIFqqQms7QrJOFM39OU5VzRFWbctkMpiNIs1F0rEVUJrjBqUn-lfmBgGnWwVj0E7Cfwbh9YrZ_aDKn4n54X9ohk9DyUCR96BjXHvk3CGdqMKlVE62dznj_-XgWVzUMrDml2wPp4eSrUrNuP49zx_6ecaHSJC9MwDKIs2aNWLAfjGX4j0zVS4fVtBkRUaXySYc-3jBANlBnK8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a6d40fc.mp4?token=LsY8bdTQqJZsBzS6YYbuIUNufixnUw1xpN6kyOI2S3SPZGEjRV9ZH_EFVhM9Kd4W9MO7ET7eZGremYxmo5edR2XxBuAyUaeYBxUt_oSStnQB7kkza3a9gIXHjfUwaqlNWUNTXk9lhvIFqqQms7QrJOFM39OU5VzRFWbctkMpiNIs1F0rEVUJrjBqUn-lfmBgGnWwVj0E7Cfwbh9YrZ_aDKn4n54X9ohk9DyUCR96BjXHvk3CGdqMKlVE62dznj_-XgWVzUMrDml2wPp4eSrUrNuP49zx_6ecaHSJC9MwDKIs2aNWLAfjGX4j0zVS4fVtBkRUaXySYc-3jBANlBnK8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: در قانون آیین دادرسی کیفری ماده‌ای پیشنهاد شده که رؤسای دادگستری‌ها هم بتوانند بر وضعیت زندانی‌ها نظارت کنند.  @Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/460854" target="_blank">📅 11:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSz8PKA-XqdG5-ESsTJCl3SFG72Rz5kj9RiAqSlWEenjLOU1Ikz1U5rSvxZSAPgs6xXHJVLsRQqtYCNd_8851lVrZIOiHhytas9PVkvNK3a3RRVN3ZBB6eP3O92GNL2r5KZV8Wa3YKwRVjXx2M4rQFoWqV1purb6V3YxGulI9OfU7GxNRJtt6fHsrTopDQePiUyY6hDEUlY1w5MIzj7jxFjBZ4QzncNkJMbpC5Txt9MWzDmn7wbPQ1DbpnuAnfvUEZTIuk_VuRbD5zD1PQvh31QrwQwFo4oPr91rDgNYB-TS79tuprgvQ4XZsHFvBuRU7XUMQvGgjOsZh82uReJSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حملات یمن آرامکو را به تعطیلی کشاند
🔹
وزارت انرژی عربستان اعلام کرد حملات بامداد امروز یمن به تأسیسات انرژی در جنوب این کشور، موجب آتش‌سوزی و توقف موقت فعالیت برخی تأسیسات شده است.
🔹
در این حملات، پالایشگاه آرامکو در ابها هدف قرار گرفت و همزمان گزارش‌هایی…</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/460853" target="_blank">📅 11:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fcfb4550f.mp4?token=bkAVV_EM7MHh1F-Ec_W0Bfk53QlR7eXmURhkfgt1Bp8h7ar0TUvRGYWZzr_dmQlmSnZtCCZiWuc7Udpom66vsAIzUKzdS871yJgWbR95WQTmIbzyAqp_s4Weu4LThvodcP6-KZ5O69hXzJMwiEBGG2m_V68fPtkhEcqUTxELj1EUTx9bMOKmnPAEo0J7uDXT1L1l_lLMOAHbm7D7tXhcIOV1RH8dry7XJ8PQlEmsp82Rn-nXu0S9aVQhalNB0kEddrffLMGWPpmI2OM56-vl44Vv5bD6ZiWQ7CYU1k1ORKYbk6zmRHi5zmqybAfRIeS0MJiyGXDFKaOPS6GxJVTB5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fcfb4550f.mp4?token=bkAVV_EM7MHh1F-Ec_W0Bfk53QlR7eXmURhkfgt1Bp8h7ar0TUvRGYWZzr_dmQlmSnZtCCZiWuc7Udpom66vsAIzUKzdS871yJgWbR95WQTmIbzyAqp_s4Weu4LThvodcP6-KZ5O69hXzJMwiEBGG2m_V68fPtkhEcqUTxELj1EUTx9bMOKmnPAEo0J7uDXT1L1l_lLMOAHbm7D7tXhcIOV1RH8dry7XJ8PQlEmsp82Rn-nXu0S9aVQhalNB0kEddrffLMGWPpmI2OM56-vl44Vv5bD6ZiWQ7CYU1k1ORKYbk6zmRHi5zmqybAfRIeS0MJiyGXDFKaOPS6GxJVTB5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای وطن‌فروشان پروندهٔ قضایی تشکیل شده و برای بعضی کیفرخواست و حکم هم صادر شده
🔹
حجم اموال این حوزه بسیار زیاد است و تجمیع آن طول می‌کشد. @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/460852" target="_blank">📅 11:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1738a6d5.mp4?token=HMwJuVUp43G4xpxmpbRCrO9wgW2sJWPIrmmeQSMcSnUPmT_CFvI_R8NDHTaXzFldTljejth7QW8iXDah2Sojsu-5wBouQKRquh4fMOJIXD_IJ9dXjK_xBnZn91HetxuGv7HP0evS4Qve_to-PsY8YukVPDdQK0swh7pr1NqLIGdZ8Phez9bEGjPHLM_NYC7nJjQ_So7uRQQxaBiqWeKH2e25pJ-8UGOFS5jXPkazwFOUhht4Y9d1xmkOaP_h5T8PDCcrnL38C7__FLTMtlHWEMbmyDOuzwhifAzBHZLBs-QP6QzxIAa7GMyFzdPsO0AZB2GwSMjG4WIyr7oqnO1yBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1738a6d5.mp4?token=HMwJuVUp43G4xpxmpbRCrO9wgW2sJWPIrmmeQSMcSnUPmT_CFvI_R8NDHTaXzFldTljejth7QW8iXDah2Sojsu-5wBouQKRquh4fMOJIXD_IJ9dXjK_xBnZn91HetxuGv7HP0evS4Qve_to-PsY8YukVPDdQK0swh7pr1NqLIGdZ8Phez9bEGjPHLM_NYC7nJjQ_So7uRQQxaBiqWeKH2e25pJ-8UGOFS5jXPkazwFOUhht4Y9d1xmkOaP_h5T8PDCcrnL38C7__FLTMtlHWEMbmyDOuzwhifAzBHZLBs-QP6QzxIAa7GMyFzdPsO0AZB2GwSMjG4WIyr7oqnO1yBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای وطن‌فروشان پروندهٔ قضایی تشکیل شده و برای بعضی کیفرخواست و حکم هم صادر شده
🔹
حجم اموال این حوزه بسیار زیاد است و تجمیع آن طول می‌کشد.
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/460851" target="_blank">📅 10:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460850">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf30da4a1.mp4?token=f5u3-vCAwJbVQTBmuzXKw7nqc8otYjnKSHu1WWk_VEKo57n-XuC7yt_qRgvqUzyVR__9zfEpcf6gDSimFcgOjxVyhRKc-nHU4LBYQeXse1cGpgcHZUYZbBlOLdw9yEv1RLxXU_c1SF5iKv6t0DfX2wNkytBzmAsMJktxvpDy5gIkolPrwpnQntSQx5BslO5REf-n6MnU_uw1cL9mpm-9bQMGWcgVW49nKA5RsvOnzSYo3karK6XEsinHdGKXr1ud7dTXGKrcd6Qjk3KQXAPBP6O7n_oEQPQF817HLBOGpMrdiL15mjK7Ci9nlPhHHuuPGeZ-C6qEbXA1-M46YdcdAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf30da4a1.mp4?token=f5u3-vCAwJbVQTBmuzXKw7nqc8otYjnKSHu1WWk_VEKo57n-XuC7yt_qRgvqUzyVR__9zfEpcf6gDSimFcgOjxVyhRKc-nHU4LBYQeXse1cGpgcHZUYZbBlOLdw9yEv1RLxXU_c1SF5iKv6t0DfX2wNkytBzmAsMJktxvpDy5gIkolPrwpnQntSQx5BslO5REf-n6MnU_uw1cL9mpm-9bQMGWcgVW49nKA5RsvOnzSYo3karK6XEsinHdGKXr1ud7dTXGKrcd6Qjk3KQXAPBP6O7n_oEQPQF817HLBOGpMrdiL15mjK7Ci9nlPhHHuuPGeZ-C6qEbXA1-M46YdcdAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای راهبردی روابط خارجی: مذاکره گره‌گشای همۀ مشکلات نیست
🔹
فیروزآبادی: دیدگاه و نظریۀ بعضی از دوستان این است که ظاهراً همۀ مشکلات را می‌شود با گفت‌وگو و مذاکره حل کرد.
🔹
اینکه همیشه فکر کنیم همه‌چیز در هر حالی می‌تواند این‌گونه حل شود و با این روش عمل کرد، از قدیم در روابط بین‌الملل مورد نقد بوده و الان هم مورد نقد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/460850" target="_blank">📅 10:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460849">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyM7KQDVeE-_DlC9ReyDlFA6doCfo9HxaMm0oATApRuGvQwJLOtJcD8ZlnQ9jEu2qBNt2VlR8zisjjbQ5uqpem0jPMxr2N-bG2AwSdobrx1fCh6dH3ijzy3V6w6A3EcdTI8aNC1J7toVEnCYexijirw1lKybWFO6SR2WMdRjW-BcQ6dnbEnA6tbjWXtF_AzvwYEtyp5TSNQHDfY9dr53T2PhbVIa1I2-69kpnWwfgw52s_onG0cjKfKwS2yHm8Q6Sh55ax1T60gT7Kv20f700dY7eah3M_Kh7ZuGvCWZYiSiMuIRkKWB7q_eDjp4bM6tgiqgTMEx58RHYeOyUxK5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده به مجلس بازگشت
🔹
در نشست صبح امروز مجلس به ریاست نیکزاد، برای نخستین‌بار پس از جنگ رمضان، جلسه به‌صورت زنده از رادیو فرهنگ پخش ‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/460849" target="_blank">📅 10:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460848">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b357690a.mp4?token=Qw2MoYN3e7A89aopzySRD6tn7-2EalcDMACB5L1TMRmYr0HYqAOyg8Xf9_Ft3RnZBtQW8eN6aeys7yv_mjWe9bcRMTR9KTiqmOQe2oryoTi-WYhPrivWedL8PllyeZR9iABDXQONaiUkJIYSab2liPsSB8Q8ONN_K-cXe84YemKARk_7KYNvzKh0NZBIKJdUCluUj9BkESylqwHWiM2AxW5BZqrlp_tR8RhC865kNnMF-nhNe5KLpxbWZo34OJTuMxE0n3_QRQJX0DFplxRjnA-BMU9AYgMxqKUvs3CpJiZCkIBDn58vEDqtRKUjLQRN-_M0YMyi4jTLozkCToYgRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b357690a.mp4?token=Qw2MoYN3e7A89aopzySRD6tn7-2EalcDMACB5L1TMRmYr0HYqAOyg8Xf9_Ft3RnZBtQW8eN6aeys7yv_mjWe9bcRMTR9KTiqmOQe2oryoTi-WYhPrivWedL8PllyeZR9iABDXQONaiUkJIYSab2liPsSB8Q8ONN_K-cXe84YemKARk_7KYNvzKh0NZBIKJdUCluUj9BkESylqwHWiM2AxW5BZqrlp_tR8RhC865kNnMF-nhNe5KLpxbWZo34OJTuMxE0n3_QRQJX0DFplxRjnA-BMU9AYgMxqKUvs3CpJiZCkIBDn58vEDqtRKUjLQRN-_M0YMyi4jTLozkCToYgRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رویکرد جدید نفت ایران در برابر دولت ترامپ
🔹
معاون تلفیقی شرکت ملی نفت: در مواجهه با رویکرد خصمانۀ دولت آمریکا و شرایط خاص حاکم بر کشور، افزایش تاب‌آوری در بخش‌های تولید، توزیع داخلی و صادرات به اولویت نخست شرکت ملی نفت تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/460848" target="_blank">📅 10:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460847">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544e56f81f.mp4?token=KaUDauG_QfD7lP3m83HjbBBstk18Mhe_qspJBqKgM6QDRg6wSer6lDYDRERQ5FdCglmWYI9L69ck5FtjNw1tDRxC36lsygnbrHlQ_xM-3NZn5DKfduYSKmv3XON_ob4ThUrVDFEA4fG5XJEoQp1sLBk911P2mSwKIVfLA3_gCIFMSdn3pDkaaqFXvIzGScIB4l_2cx2baB9p7kN-QcrvRnHLEEKziMV8XdrAFMohIRGmNWmmvNEG9lmxL5XthHzn9fKEsIF8_5GXw-bL7agHbS_srIaLcvtdczZ9mBFVXORaBCJuxe5BFhMUZ_v6lh1lh4RloehILReUwCqRR6A9aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544e56f81f.mp4?token=KaUDauG_QfD7lP3m83HjbBBstk18Mhe_qspJBqKgM6QDRg6wSer6lDYDRERQ5FdCglmWYI9L69ck5FtjNw1tDRxC36lsygnbrHlQ_xM-3NZn5DKfduYSKmv3XON_ob4ThUrVDFEA4fG5XJEoQp1sLBk911P2mSwKIVfLA3_gCIFMSdn3pDkaaqFXvIzGScIB4l_2cx2baB9p7kN-QcrvRnHLEEKziMV8XdrAFMohIRGmNWmmvNEG9lmxL5XthHzn9fKEsIF8_5GXw-bL7agHbS_srIaLcvtdczZ9mBFVXORaBCJuxe5BFhMUZ_v6lh1lh4RloehILReUwCqRR6A9aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارت زرد مجلس به وزیر ارتباطات
🔹
در جلسۀ امروز صحن علنی، سوال علی جعفری‌آذر از وزیر ارتباطات و فناوری اطلاعات با موضوع پوشش‌دهی ضعیف تلفن در جاده‌ها و روستاها، بسته‌های اینترنتی بی‌کیفیت، بلاتکلیفی بازنشستگان مخابرات، رهاشدگی فضای مجازی و بحران تلفن ثابت مطرح شد که نمایندگان از پاسخ ستار هاشمی قانع نشدند و به او کارت زرد دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/460847" target="_blank">📅 10:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460845">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251a5a71b3.mp4?token=FWGSv_5Fs5RMJA1Usa58f7yw6849JQhLS8wBngGxMWISm-oTHyDzROnyUaVFsSAvJze9oCL45VzU8D9Q_qplqKIPjh538Vg50YkqCL4ohV8nffPt4hZoSWuSGG8fD-QEKxGWcefgb-_WzuDU2BIO0Fy9i-IeLJvFTZ7kvnySHgYVNKqZeo7sJUrtR2Qkqb1iSv2G98mt9rUykEI_Xp3dKLSjJcLin4r71HZgXUVljju0rQ1m3TBa2ukw6VycVP7N2u_t7LUvQBNZpXmGSaQ1fGALAAP8MeDNySc3uM3a-ejfWGdv1ZjbV40qk1jy_1it9kpBApEgl9W0ZNp6OIC27g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251a5a71b3.mp4?token=FWGSv_5Fs5RMJA1Usa58f7yw6849JQhLS8wBngGxMWISm-oTHyDzROnyUaVFsSAvJze9oCL45VzU8D9Q_qplqKIPjh538Vg50YkqCL4ohV8nffPt4hZoSWuSGG8fD-QEKxGWcefgb-_WzuDU2BIO0Fy9i-IeLJvFTZ7kvnySHgYVNKqZeo7sJUrtR2Qkqb1iSv2G98mt9rUykEI_Xp3dKLSjJcLin4r71HZgXUVljju0rQ1m3TBa2ukw6VycVP7N2u_t7LUvQBNZpXmGSaQ1fGALAAP8MeDNySc3uM3a-ejfWGdv1ZjbV40qk1jy_1it9kpBApEgl9W0ZNp6OIC27g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات یمن آرامکو را به تعطیلی کشاند
🔹
وزارت انرژی عربستان اعلام کرد حملات بامداد امروز یمن به تأسیسات انرژی در جنوب این کشور، موجب آتش‌سوزی و توقف موقت فعالیت برخی تأسیسات شده است.
🔹
در این حملات، پالایشگاه آرامکو در ابها هدف قرار گرفت و همزمان گزارش‌هایی از اصابت به فرودگاه ابها و شنیده‌شدن انفجار در مناطق جنوبی عربستان منتشر شد.
🔸
این حمله سومین حمله به تأسیسات نفتی عربستان در کمتر از ۴۸ ساعت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/460845" target="_blank">📅 10:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460844">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/efa5317854.mp4?token=R5AaikFeSJVByyQutVfAOcfIVe0J8F7uS3Ni1PL4b6R-cq-rcXSNt55wUzd46gLT6L8_4KUUV2uMaRs8FEQTQq3zYKJgZ9uvJUhJaXvS79AxLT9zQgcmCY9II2YWJ1tf4lmJaO9y_LoQvnpZtan556np8FzaPUe13ylu02hFARn_7m33mXnPzUVE8wYFIsYBuLIZVUGf13L8uoH5kAJrJ3V1Y6717CKKV2ilO0O-NsZxPvl-Bc37IigmHtmjvwR2tzI_EGF719IoTn1WHI3GBJjSz4PbhecgwbTB7HYiYVorTw7ZwRVpoQi0wzd4c7oB2ixIjzcttwfLK7pb0tMqWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/efa5317854.mp4?token=R5AaikFeSJVByyQutVfAOcfIVe0J8F7uS3Ni1PL4b6R-cq-rcXSNt55wUzd46gLT6L8_4KUUV2uMaRs8FEQTQq3zYKJgZ9uvJUhJaXvS79AxLT9zQgcmCY9II2YWJ1tf4lmJaO9y_LoQvnpZtan556np8FzaPUe13ylu02hFARn_7m33mXnPzUVE8wYFIsYBuLIZVUGf13L8uoH5kAJrJ3V1Y6717CKKV2ilO0O-NsZxPvl-Bc37IigmHtmjvwR2tzI_EGF719IoTn1WHI3GBJjSz4PbhecgwbTB7HYiYVorTw7ZwRVpoQi0wzd4c7oB2ixIjzcttwfLK7pb0tMqWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست جالب بهروز رهبری‌فرد از همسرش در «پانتولیگ»؛ «می‌خوای بری خرید، کارت منو با خودت نبر!»
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/460844" target="_blank">📅 10:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460843">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-text">📊
🙏
یکه‌تازی «وتجارت» در بازار کارمزدها ادامه دارد
✅
بانک تجارت در پنج‌ماهه نخست سال ۱۴۰۵ با عبور هوشمندانه از الگوی سنتی درآمدزایی و ثبت جهش‌های معنادار آماری نسبت به مدت مشابه سال قبل، فصل نوینی از استقرار بانکداری مدرن را رقم زد:
🟢
رشد ۵۷ درصدی درآمدهای عملیاتی
🟢
افزایش ۷۰ درصدی درآمدهای کارمزدی
🟢
رشد ۶۰ درصدی خالص درآمد عملیاتی
🟢
افزایش ۶۴ درصدی منابع
🟢
رشد ۶۱ درصدی تسهیلات
🟢
جهش ۱۹۸ درصدی سپرده‌های ارزی
🟢
افزایش ۱۴۲ درصدی تسهیلات ارزی
رشد درآمدهای کارمزدی، توسعه فعالیت‌های ارزی، افزایش منابع جاری و تنوع‌بخشی به سبد درآمدی، نشان می‌دهد بانک تجارت در حال حرکت از الگوی سنتی درآمدزایی به سمت بانکداری خدمات‌محور و مدرن است؛ مدلی که در آن، رابطه مؤثر با مشتری و ارائه خدمات متنوع، به موتور جدید خلق ارزش و سودآوری تبدیل می‌شود.
📌
بانکداری به نفع همه؛ به سبک تجارت
🌐
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/460843" target="_blank">📅 10:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460842">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/460842" target="_blank">📅 10:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460841">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Q3feZVWYeb2_gcsowhXuIIexKglc4AqngKB244fTepcU5zBLnbnUnNp-N9hl0Myf-Y_4v6SEgihCxVGOrxYUotLWtStVV5YLHDNfSUbuDJh7I7WIGXMD__fjoqKqvY-4EY-m5b7P0HOSrENcDsR_YXLxdbDHwvQAyIZiyNuW-tKDhAKGrmIcSkhw1zS2BG3ED9wx7rdclMnYYyI-WY15kWM1D2HpgfS4rE0P3CiLYrTRp3izOnBTHBcSM_ki5gau_x28AHid0pBjUuv2U_q5kC03BZbEfoyPD_KEa5CUEqKQ9AlpBJmg1a11_kN0EwjCAKL4t27KhLxHmwXBY0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تصویب یک فوریت بررسی لایحهٔ تداوم حمل‌ونقل عمومی رایگان در تهران
🔹
یک فوریت لایحهٔ تداوم رایگان‌بودن حمل‌ونقل عمومی در تهران، امروز با حداکثر آرای موافق اعضای شورای شهر تصویب شد.
🔹
رئیس شورای شهر با اشاره به اینکه «تصویب یک فوریت لایحه می‌تواند زمینهٔ ادامهٔ…</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/460841" target="_blank">📅 09:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460840">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMwRneig66eTA2QJZPQbzZTYcQgrmZSq0cLmR9ALEruUqfmkkKxX6vHd5dIrkjZ4mx14AZ_YuHlAFTEQU0qsiGREdPdTBdInoegwnOBPisTqKq80m7ufmrVwjKA0ZaV8UN-b-XFzW9X4w60HiYHqnlQRmjUzKD0YhWirll693Gocx5UujjTVJFI_C40CHBYu4IuHHCIPqn0QTrdLgncQVVaijIRCI7RXsDrk_GyRUD6PJfYrcmOqP9_EM7KyKLHL-wMPhZoMMo9Ner8sfpLCJNDdV1Yex4xVGQ3rd9RXNHD8FosA1HONtzPM6xgyOyESzeGSYqOdARIinhdwp1oMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/460840" target="_blank">📅 09:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460839">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LInDRTKVGDDP1jFtVD-GUC3JMoEmpCQrjfYceunghI5XBGDAu6jZ36dXG5k3PwcPSdRdd6oyJsAZXoSoudxPQE6Mq7MPhvVl8UQXilCEoNsUpTwm5p4hVRP7mKMGFvSWj0W0zPsZIB_gThU6jEtjBoMLnZCBY_7qCz7iQzisrp-D3vPD7O5i_BDicMiiNXKXbPgIPUiOOOWsG_K0_DSDhHz-6aySKCxH1oBv8-WeRHYheE2KkMt3NcOd89UoUTsn10etkuANwXXwSx2JPyr3YFqydMdgR1VQXMryKpXkgxUe-vehpYJhKQ4lmPgHiEYoZmK2m23FSBS1UANxK8pMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای «بانک» مخصوص جنگنده‌ها
🔹
«بانک زدن» یعنی
خواباندن جنگنده روی یک بال برای تغییر مسیر و گردش
؛ مانوری که در پرواز ارتفاع پایین، مهارت و دقت بالایی می‌طلبد.
🔹
«بانک زدن» یعنی
خواباندن جنگنده روی یک بال برای تغییر مسیر و گردش
؛ مانوری که اجرای آن در ارتفاع پایین به مهارت و دقت بالای خلبان نیاز دارد.
🔹
در
جنگ ۴۰ روزه
خلبانان ایرانی نیز در مأموریت‌های رزمی از این تکنیک استفاده کردند؛ از جمله خلبانان F-5 که در عملیات حمله به کمپ بوهرینگ، بخش‌هایی از مسیر را در ارتفاع بسیار پایین طی کردند.
🔹
اهمیت «بانک» زمانی بیشتر می‌شود که جنگنده در ارتفاع پایین پرواز می‌کند؛ جایی که خلبان باید در زمانی کوتاه مسیر جنگنده را تغییر دهد و همزمان فاصله خود با زمین را کنترل کند.
«بانک زدن» چگونه انجام می‌شود و چه نقشی در پرواز رزمی دارد؟
🔗
اینجا
بخوانید
@Farspolitics</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/460839" target="_blank">📅 09:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460838">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPJRCB3wH4EcdFnkzkkoYlAxpjgUqE6ZEU1dQ37Y3Q_UghhLEvMliXPpck9wgx82tXLwIidumj3FrKG808hHHRn4wX3Et-7N5nGxXxFd_xtKopSk1evGlWHj2wr8Jb8J6rMpvzV2mohbddY4S3JQXDwSyL7smJM2USakcktMg3FMgX1mW7_ancBlj3iQ4KUok6wjazdaJl9oE8bKr4FPNsb0sXzD0Oyyi8ybSkU8SDsXrgOL5BZrOKHouq3lBMJgeBv3d177UMdm63yM9ghK1rs3HfhIShcoKhGRm4j6P4BNKSkztWo8oDExmQ7Q6D-fRT6LSsdmSEyeuS5x--sAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۷ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش ۱۷۶ هزار واحدی به رکورد تاریخی ۷ میلیون و ۸۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/460838" target="_blank">📅 09:29 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
