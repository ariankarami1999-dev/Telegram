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
<img src="https://cdn4.telesco.pe/file/UtH2I92lfk5ugLHHd0UGRuJHNly02HUwNOlICNEIazy0WmodVyW1N0ZVPKzL5IiRh6T-85wQzjZ3_GmE78mU8hLn-ZRn_lF9OIpM2l6p2gCjiiEzsWmyBtP5_nlYH4ZtbknYMkt82dhCIXDpYVUZKSdOogMJyJt8tctnkRbESVdqdRx4LxT3NcT2afzZk4nSnpABycr20ZQrE6ZXYFd6MZDK5YgwCsOaEIf1wPe-sajipBzk2EE9ZB29nf4LBeekBG_n77ZzZksHzmrOoDb5TAGaY16qV28Y3XXae3V9pNNdUDzmYqDc8fjPPB3m-NZLAtDbIzwBtaaA0Go6yfzMng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-140796">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfgWwQLICTcjQmmXO9fmcNh-6NSA9-p1Jm9Z8eP6F-rbvyq_NmXaO3R1VZJV2cqtzMd7gNitMOCiPurdY3-qh8QpBMS8KmB7mNlQY50m7GwProOa2tTfmScwHMlf9BcppuicStq0d3R77-7z1nD2RVjrIjL3vk9CyOiyrXDE7LrfwPjA0wQMJnR_77AIllCWxNi_nbXzxcl6GwyWcuAtXGkustNwm0BR0dopIgbRmcpOW0_Lyg57hIs2uPMQQIejr6ck6YQuTMdQGDLN-3vk9SNMAYOsjJfEsfs4wUvrqu-JrYkXShgXQyYiyajSI9hFniOtjDy2CIl5mUyAwlKXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 738 · <a href="https://t.me/SorkhTimes/140796" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140795">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD2VbV6R-8Lak9X4tLiZfRa1gSm--GT1kk-9933uLJGCM1lIC5W2tIrNQsI_0l2QMIv0D_79vcAOfafjaB0uBmvgXgNLCxArZMGxmDS-ZSGbpA87HZR55qRU9XkBAzJOCmiIxYURi3pqMsPHxNJMI-DrgY4xobd9eBakANkviAIaHzVBF6mNhW9jXQRyC9oPiZCkpiAYzOT2pNDHlPByp8VyCf7d_wkQeT8rNhYNqMSktOIwYO011QRe3C7o4P3QZUHM6wFeCC6rUgl9pu0cK1JVn04tnmPdS78Q9qkizK1eNBTOTnlzBL95lMG4MzjFGBdfblbhi-0hlZm9Wl7i3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیشب در بازی دوستانه بین کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردند و گفتن بقیه بازی رو وقتی انجام میدیم که فلسطین آزاد بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/SorkhTimes/140795" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140794">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/140794" target="_blank">📅 16:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140793">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO4elTNkFyB6HE9Xoj4P3ezYMY3SU6XkaySk7YdQGQpklcau9kpr8Vcao2PqpOHEFvl27xD8tDgaylh8Vwq_bpkYK8J-d2PPJUTt2DeeNTvHhRBIBCpMgUAY09K-dgD3onMoeTVr1SYMDw6jPIER1KpkwfiAGF3zkN9c0ct3rTCVr2WXbbjr8SkJwEaooO8qRi8XZzHPQTYezC2dRv333wLO65w229v_0kaM_MQWHUjWjAX45-jDZnu9xe81c4PI9aL7Ns7xe01HcJMfNKbXiST1hKVEC1cJsQj3bfnUmQ_83N3z8Lg4nvRNbUaty28PJFcF1K_n-TIFXkUXfXB6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🔴
در یازدهمین سالگرد درگذشت هادی نوروزی کاپیتان فقید پرسپولیس، یاد و خاطر این بازیکن در دیدار امید پرسپولیس و سیاه جامگان زنده نگه داشته شد.
🔺
پیراهن شماره ۲۴ هادی نوروزی در دستان هانی نوروزی فرزند هادی و بازیکن تیم امید پرسپولیس در عکس تیمی پیش از بازی.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/140793" target="_blank">📅 16:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140792">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g03-1NLnHx-OR2UQQ5BDMMNkvNJllatVUUgpsSQfgffsg6ysTAR5yDfNSHtYE8a8oFIGDv1jiZDEid3OXRSIxOP6-noxuIrnMk8D_Az0t9p4A0XjJ5M0YFkMmCF8yCQkYWjB62m-0igYGvqb4dqlu2wcn0SG_Pl1WCgELO6dWX_SjILCQ52eNGYTreCcK4J3r9z4Tgplsl01cz8gnwpbPDI7GUjGDbWt3whmBldA_Vlg5eGZ4JC5BJAslEWXQZMzfkZC3BibU6LoxbF2DjNOb3rmjtq60g4F20brtYpyRWgILdsVi2q8WpmXW-jKz5E1MA3HvNbA8f7d-sUGLZPrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
Germany -
❤️
Serbia
⏰
Tonight 22:15
🏟
Allianz Arena
🇪🇺
آلمان بعد از ۱-۱ مقابل هلند و شکست ۰-۱ برابر یونان هنوز زیر نظر کلوپ به برد نرسیده و مهم‌ترین مشکلش تبدیل مالکیت و برتری میدانی به موقعیت‌های باکیفیت است. صربستان هم شرایط خوبی ندارد؛ در دو بازی ابتدایی لیگ ملت‌ها مقابل یونان و هلند شکست خورده و با صفر امتیاز قعرنشین گروه است. از نظر تاکتیکی، انتظار می‌رود صربستان عقب‌تر بازی کند و فضای کمی بین خطوط بدهد؛ خود کلوپ هم روی همین موضوع تأکید کرده و گفته شکستن دفاع فشرده برای آلمان چالش اصلی خواهد بود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/140792" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140791">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/140791" target="_blank">📅 14:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140790">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
✅
تیوی بیفوما که بدلیل مسائل سیاسی دعوت تیم ملی کنگو را رد کرده بود دقایقی پیش برای حضور در تمرینات پرسپولیس وارد ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SorkhTimes/140790" target="_blank">📅 14:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140789">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
🇬🇭
کارلوس کی روش بعد از باخت خانگی ۴-۲ غنا جلو گامبیا سیکش از تیم ملی غنا زده شد و باید دنبال تیم ملی جدید بگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/140789" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140788">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/140788" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140787">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🗣
سرگیف و بیفوما هردو در تمرینات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140787" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140786">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
قطبی یک قدم تا بازگشت به فوتبال ایران؛ مذاکره ادامه دارد  •
✔️
✔️
مدیر برنامه افشین قطبی اعلام کرد مذاکرات با فدراسیون فوتبال ادامه دارد و دو طرف در حال توافق بر سر شروط همکاری هستند. طبق مذاکرات انجام‌شده، قطبی قرار است مدیر فنی تیم‌های پایه و سرمربی تیم امید…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/140786" target="_blank">📅 13:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140785">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
محمد نصرتی درباره حضور دنیس اکرت در جام جهانی: آقای قلعه‌نویی، با دعوت از اکرت در حق یکسری بازیکن جوان اجحاف کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/140785" target="_blank">📅 13:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140784">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/140784" target="_blank">📅 12:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140783">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
فووووووووووووووری
❌
محمد مهدی محبی مصدوم نشده و اصلا مصدوم نیست. امیر قلعه نویی دیشب با هماهنگی قبلی برای توجیه شکست های پیاپی به محبی ستاره تیمش اعلام کرده باید تا دقیقه ۳۰ مصدوم بشه و تعویض بشه تا فشار رسانه ها کمتر بشه و این یک حربه از سوی قلعه نویی…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/140783" target="_blank">📅 12:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140782">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
میلاد سورگی: از باشگاه بزرگ پرسپولیس ممنونم که باعث شد من به فوتبال معرفی شوم و به تیم ملی برسم. امیدوارم روزی به عنوان ستاره به پرسپولیس برگردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/140782" target="_blank">📅 11:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140781">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🗞
لیست بازیکنانی که قلعه‌نویی ازشون ناراضیه و شاید دیگه دعوت نکنه:
❌
محمدمهدی محبی
❌
صالح حردانی
❌
سامان فلاح
❌
احسان حاج‌صفی
❌
حسین حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140781" target="_blank">📅 09:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140780">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/140780" target="_blank">📅 09:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140779">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
پیگیری‌ها از مسئولان باشگاه پرسپولیس نشان می‌دهد که هیچ پیشنهاد رسمی از سوی باشگاه‌های خارجی، چه از قطر و چه از سایر کشورها، برای جذب محمد عمری به باشگاه پرسپولیس ارائه نشده است و بحث جدایی این بازیکن صحت ندارد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/140779" target="_blank">📅 09:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140778">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/140778" target="_blank">📅 09:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140777">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/140777" target="_blank">📅 09:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140776">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم./فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/140776" target="_blank">📅 09:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140775">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRSptN5ckDuU_RGiR2BEBdnUhybcjH1Rgy5pGKK9ZElN0wS0dw3VNCN2CC3XNRhwhOyjG70UaVxRg7JVD1BzKebSzGN4zrbb8ej5JIgBPMCW-XCm_cuF9YYzkt4nnRGx7XVfUjN8iWxA4DMf49wUNQN63rxjNV86UDQPg261RpMaKlML1GxjrQV888IoCHBDbdDmpic33D1UU7y92Gl0QJOwgjrbIUm67oopmVKjCuv0Nw4Yr58r8LF4702AyA6pSmU4LU0UPZwNWBZOml4zF0PlTB1DNL-BOsekfc_bDE9Kvzh7ll8HGGF3Puhp1SZDyDJ3xCsKN_S_IYLcZ-cwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/140775" target="_blank">📅 08:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140774">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FE-7JsGXAmQIgM3sFQAOMHZ38M-VmYttHJjgcHGzwgbtUR0-C5TpveqJ4q47WM1pJK-jHM8vSEAa4jO0sp9kjnuaiegW0q_3FZqA-PzQ01oNEFnL4IM52PpQcrV6c_xfrGFQV-yRPXW2x5HDYpQaIFb0ztruPmajgRozmgNbOru8X0qVfdJ4bM6xiDfYd0REXX0lZIBMVubTmlX4wNDxAWcaiVPeEdF52tpC5J5LE49eHFZkocfE6crG2KPQo3sEuKS6fQIeCVBYqk6OAWu2NntAVqgJ7ZUW_4OorPoWJEgb6_Cd_ehgN2msRIsz2AqM_lzuNknmrMr2VScuAhQwXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبِ سنگین فوتبال؛ چند تقابل با پتانسیل غافلگیری
🔥
⚡️
⚽️
ژاپن و اکوادور شروع‌کننده بازی‌های فردا؛ کنداکتور فرداشب پر از تضادِ ضریب و احتماله؛ جایی که بعضی انتخاب‌ها از همان ابتدا جهت مشخصی دارند و بعضی‌ها تا دقیقه آخر قابل پیش‌بینی نیستند. آلمان و نروژ روی کاغذ دست بالاتر را دارند؛ پرتغال، هلند و اتریش اما وارد بازی‌هایی می‌شوند که یک اتفاق می‌تواند همه‌چیز را جابه‌جا کند. فرداشب، عددها حرف می‌زنند؛ زمین تصمیم می‌گیرد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140774" target="_blank">📅 01:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140773">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140773" target="_blank">📅 01:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140772">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
فرهیختگان : دقیقه ۲۷ قلعه‌نویی خواسته حاج صفی بیاد تو بازی تا رکورددار تیم ملی بشه و به محبی گفته یجوری بیوفت زمین که انگار مصدوم شدی وگرنه مصدوم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140772" target="_blank">📅 00:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140771">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140771" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140770">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIeEhF_g__myiahiSsrK3YFasijyTqz_R4iRnpCCf8dKpX6R3Mvnz3iOvehkm9hV4UYx3SdS4yhCTGoHfCKuZnMNye8ZeHOifEj-t2w86k0u4nzbja_ZXVQjjg0sB6vxOYoP0u-FBQ6ie3k8eoyJXWJ8kEeWGCqVEinzhkut6h0LuMWvJAv9daLMIwOPSABlCOCiaEm9-ZdCwiEmORD4xPhE-HtpGg0223EPkkjgCim9t0ReHZltC6VHDx7Jo6dRYRYI3v2qXhRHmdV9UA_AE8XA02NdZ5KklnyspjPDZFkxMB12nn8mGOTeCkspRPx9ou0bCz29z1a8v_Y7S1BeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
عالیشاه در خانه
❌
دیدار تدارکاتی روز جمعه میان پرسپولیس و گل‌گهر در ورزشگاه شهید کاظمی فرصت خوبی برای قدردانی از کاپیتان سابق پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140770" target="_blank">📅 23:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140769">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
لحظه گل ثانیه پایانی جوانان پرسپولیس مقابل پارسیان توسط محمدامین قرنجیک
👍
👍
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140769" target="_blank">📅 23:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140768">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c458bfa09b.mp4?token=q1pA-SsKFVHwHt_PC21HVHtGOOZeCByvepP2ilieC3B0L4BMA7dNbzFg9Pj-HJQEgTSBtvW9yfQtcX6-4TdbIqN_PDYlRniP0bMRv1mMfm_YnMdv8bHB4EUgX5iHBlsppfszwfvuryYFmqfx6vbkPxrqRAGFnDdwGuZbcaPdPF6-WwvX3a0sybgi1Iop0EQmkKsA47Zx91tAxyL0ouAgISTP8mj2zYI-H4gAXivEuA1V3oXvHhT559zPDR62ccUq9oKynPBIkShJ6gNTqLPbBAbJaSPBp1p90nYhRbIzDDb5zBRSp2RaaMhbPNRwazX2pZ-LZBhhj0_6VVzECYxFrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c458bfa09b.mp4?token=q1pA-SsKFVHwHt_PC21HVHtGOOZeCByvepP2ilieC3B0L4BMA7dNbzFg9Pj-HJQEgTSBtvW9yfQtcX6-4TdbIqN_PDYlRniP0bMRv1mMfm_YnMdv8bHB4EUgX5iHBlsppfszwfvuryYFmqfx6vbkPxrqRAGFnDdwGuZbcaPdPF6-WwvX3a0sybgi1Iop0EQmkKsA47Zx91tAxyL0ouAgISTP8mj2zYI-H4gAXivEuA1V3oXvHhT559zPDR62ccUq9oKynPBIkShJ6gNTqLPbBAbJaSPBp1p90nYhRbIzDDb5zBRSp2RaaMhbPNRwazX2pZ-LZBhhj0_6VVzECYxFrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بالاخره گداوند رو‌ بردن سربازی
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140768" target="_blank">📅 23:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140767">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca8ba9d21.mp4?token=IUYu6nUqaJWrzF9Ulntt1ynej6_yCghFD8h46yAINVpIb8a3Thz5KYTp2A71XPzAe8LRB_sIvkqDyGZCcjQ3flNM10z_OYsTn_W8X0N4bFuXAuuErv1GSyx_i2JcBpUR6CVwfYcAfu25fDfeN3WMFWI0E9-62xcOWchHAo5uuXcUueEg6NiwnaKW8TTfL36t-jWamsV2zxiLG3IciPWOrQB1E3aVBV6ZHKp7iBjgziVJuq5q6JqFX7EnG6eSHeEQPPB725ApqE0wH4hhCHDs3nZDRO7qBOV0WjF9F0l_pogIyVLHUUF_vASk9aEzQJxj2zmz1pf6X7jVQdSKVT-sNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca8ba9d21.mp4?token=IUYu6nUqaJWrzF9Ulntt1ynej6_yCghFD8h46yAINVpIb8a3Thz5KYTp2A71XPzAe8LRB_sIvkqDyGZCcjQ3flNM10z_OYsTn_W8X0N4bFuXAuuErv1GSyx_i2JcBpUR6CVwfYcAfu25fDfeN3WMFWI0E9-62xcOWchHAo5uuXcUueEg6NiwnaKW8TTfL36t-jWamsV2zxiLG3IciPWOrQB1E3aVBV6ZHKp7iBjgziVJuq5q6JqFX7EnG6eSHeEQPPB725ApqE0wH4hhCHDs3nZDRO7qBOV0WjF9F0l_pogIyVLHUUF_vASk9aEzQJxj2zmz1pf6X7jVQdSKVT-sNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دلداری خیابانی به بیرانوند قبل خدمت رفتن
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140767" target="_blank">📅 23:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140766">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxwxnHnlI1rtgGfcngK62FRwv5m2QU61Y619popQq1hzsCwhij6nRbpenXKjSJSzTXKJq3Rc-RvY9Nx00NWXrLohtdvDqPhynKxqbz3-mW_zK0vr7tuW8OG26k3B549qEKRpMpZi5Z4YI0LIkkLKtmXiC6xLG_NaSwpFc3TUSreD3bIblsmKc5XMYg5Gbz-_5EpNxOIew0Ts9QDjGYLPPcPQavUV3nJOwpDX30UPNskvtQLfflXuG0iOaxpX8djWiGc9kYYF9G464QzPbUazhvEpGLuktlOvEJcsafZLtokwOvPksogG6z5qxvZgcoABxCP4ddYAhAuDa3cJJsOqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🤍
قلعه‌نویی: اشتباهات و نتایج اخیر رو می‌پذیرم و مسئولیت فنی تیم با من است. برنامه تیم رو دوباره بررسی می‌کنیم و در انتخاب بازیکنان، تاکتیک و آماده‌‌‌سازی تغییراتی میدیم.
⚪
می‌خواهم تیم ملی رو حتی بهتر از قبل بسازم و از مردم می‌خواهم فرصت بدن انتقادها رو می‌پذیرم اما تسلیم نمیشم!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140766" target="_blank">📅 23:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140765">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE2yGyySFIU9yw1O-HD5_8cHl8w0YSMWtghMt8n0-C4Do-le-am0w9UVQ7YhSh2zse7H0sK3n7nklw8en898EB9N-5LDIgM3WdQzrYjqJ6dcgMeWuXAQgv-4cISDd586qQy_ocNBX6OXTNN-XDw3Fcs5BO_3cHdFRL5hwzd7iEIXkMC79EK-T3S_FG7MH9UZifpy8uV3uaX8RZ-YNPchUfzkv156UKX7mNufC_6rIaXhPGmRfklMgDW8_s9IFFTvkW4ZCGWXKWibNXpWht1SWgh5tmnA72H5atWN0hc7m0orQAXpHDcdnjdTaGOpSu8CF_7L1oVKyFfA053szYXrzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140765" target="_blank">📅 23:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140764">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
کریستیانو رونالدو امروز برای سومین روز متوالی در تمرین تیم ملی پرتغال حاضر نشد و طبق گزارش رسانه‌های پرتغالی و اسپانیایی، اردوی تیم را ترک کرده است. این اتفاق پس از اظهارات ژسوس درباره غیبت رونالدو مقابل دانمارک رخ داده و برخی رسانه‌ها احتمال بازگشت او…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140764" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140763">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140763" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140762">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامپ: جمهوری اسلامی‌ هیچ پولی براش نمونده؛ برای همین فشار آورده که توافق کنه و رفع محاصره بشه. وگرنه چه نیازی به توافق دارن که پیشنهاد میفرستن؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140762" target="_blank">📅 21:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140761">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
🇵🇹
👤
رونالدو اردوی پرتغال را ترک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140761" target="_blank">📅 21:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140760">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg6B_NEmIXvxMW7LaXp5Y5ST5xlxPZFxym55emo1N3FOCXduRdfeyVQ2cdb6i640fXpXxQ37zOJpxuy96BD0nhOijPaWwoCDWIB383EsYJNXIb7WtaXUvjHv8D0yw_U95ne4nTyg0OkLHkK28qrShEmu-BJanQv1qZXSR-mLDyM3ONyBjLGF8ECbxl8bopzjScAOwrg8cvFD24yQUytq20Bre9u8Cfn7kTeScbznD_lacIevQWMi9GdazxbiHFL1gG4niScpP8kYLiFe-B5_4KmGu8ZbtkoVRdMnkdNJrgTNsUDmVDG96dS6_dHwsAQFGpDfN_ey_w9TyrG6yV-p8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
👤
رونالدو اردوی پرتغال را ترک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTime
s</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140760" target="_blank">📅 21:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140759">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtI9AJZNuSgO1ddjwpYfbC1q1DHf0Slc5JnYOiehKtxJQJE1w0T2NyC_3JGJioG0S_v1I0JfK5Y5lC3iUyFF5igIP2AlmAzrA6wxnoYL5k6gx6dt5xMO3l9GKluCur9xchsffurKCTCsHMRkZiZxs7FMHo0CX4G-zZJa4kd5vVDz2g_7ZvW5ehm7bsw18cR1vJtWiVYdhKVz8miE-oumPQl47y392zV6Q2HMS45USUwKqKIQXAdvRtQ-XBoCXEZIQuWinDZzor6PzZ9pRP-S_mVONbKIo1ICfPHF8E9-f5ZwmIrzMgAJBf6ZL8wQ2N4g_kv70GAtKkPnAgnGa3-02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نزول فوتبال ایران به رده ۲۳ جهان
▫️
تیم ملی فوتبال ایران با شکست مقابل ازبکستان و روسیه، در جدیدترین رده‌بندی فیفا یک پله سقوط کرد و به رتبه بیست‌وسوم جهان رسید؛ جایگاهی که در سه سال اخیر بی‌سابقه بوده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140759" target="_blank">📅 21:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140758">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShVI-sgHtecVeDu70pG9f34-Lbm94Ci_vKzeEFyIhQh9ncTVWs8dom84_C3bj_8sao4jC4_tEHhnjrfdrRhBRJWXKvpF_-Gn5fdsA0h6RFsbm1hy3ZyEKuTaSm_aYxdnsLXxD_AE89isNpGGwluUATTMCgADXZ1XeyRIeFXXJ6SvR79CjW98NZ81tSWqmWOwsLnYckrsMswbva5phhpsJm062Fv2eZw8-Rl1fLex1Drjnd3gfEk9VKpTl7_djL0ZB3zbKuPTdZmJ0aip45fE0VFrl9Nn0_JyHVHnGAwq7yRNY8LQPqLT0Wc-c42hPFWT9TddgmeyvWzAE9jSTpld_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🩸
لیست مصدومان باشگاه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140758" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140757">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
مذاکرات مدیران باشگاه پرسپولیس برای جذب فرهان جعفری ستاره ملوان ادامه دارد و اتفاق خاصی رخ ندهد این ستاره به زودی راهی پرسپولیس خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140757" target="_blank">📅 21:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140756">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4n336jjmlnGNStiLRwvj5wmSI6VtFowWqNbhdH1iKhG9OPqfCFwdZqjSQ1xwlmZYKTcAO2gDryIXIrjimTU-YjhthboddtjZdsLbHt5d1GnFWXZmjXCiqu2_h8sh_7_Y9UNeNdJxKBKa9Hs21-be_mNqLmlilz-lddAa7zmTi4rYjI-umKhuQNN9NMJN6tfT3_Izeb_I75afA_OuKZRNJR6p6TpEH1e_yrUu_xXF9fSeN7Jps9AoIWHCQTtkbiaCghOrYOXp9i-ClkERFQC-0icHieKSPAHOqKONlH8fETboLxRbeAV1sgchiE5K39J7K7pQ2XNYI1q-A7Xpr0WPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
وقتشه پوکرو حرفه‌ای بازی کنی!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140756" target="_blank">📅 20:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140755">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEJYSLfE6iv1L2wxFx3jhcCV86s527y9aOHz_WyFd-fuf0HddZbDkMALzr-1EGv_wheIDt4vQ6jhBA33pzReXv3ucwHNuIyOQbCk1BwAqdHmhXGre9auEXq9JRWa9xvW0z5NiAeaUn1hYDN0rY6upka3wtvTcW9anw5VOc6lHFsW30pvrtcHAl1cwe98LY0tuwIhh4-0PmaGlKP7y--7BwxFfnYcOkEEPieNUHogm5janbNnA5CCUkaeqDpXCCh5TVrhy3KXew07y5hZrDw5DM6BgoL-Kh3v2-21vMSQi0OClX4MyxD1FCK8GbgQbZC6qA-r8XOafvHXg4lrVX7sXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
والیبال به میرزایی رسید!
🔴
با حکم احد میرزایی؛ رضا صفایی سرمربی تیم والیبال پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140755" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140754">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
تیمداری مجدد پرسپولیس در والیبال پس از سال ها
❌
❌
تیم والیبال پرسپولیس تهران در گروه چهارم رقابت های دسته یک کشور با تیم‌های طلایی‌پوشان ورامین، نیروی زمینی تهران، بوعلی قم، مقاومت شهرداری تبریز، سروقامتان ارومیه، بنیس شبستر تبریز و روژمیوه زریبار مریوان…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140754" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140753">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140753" target="_blank">📅 16:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140752">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140752" target="_blank">📅 16:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140751">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140751" target="_blank">📅 16:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140750">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140750" target="_blank">📅 16:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140749">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140749" target="_blank">📅 16:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140748">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=tRUz7HzSCGTEtFHx0-mjOsJ3-u34__cX4C5RZtRRORsWSiYJMYWq5pxy3hLmSUSURn7nC3x7q8lkevZQq-0kLC4iDy2xqw7gZ-6anC8igh3NUUyvs9hQk0-evRxGxAL2CBWhkokp_P7iU43VG1EqbciMFLqxMmhNoWa5DsbG_G8BNkAnFr_mzECv2TxQWwVEVKurMqWGMh_qB6xBI3ltCv9e8TYL_F-hTZG-VnbRaKnH987mevM7O7mTxqEOnhly00tDfq9G7bp5FlfJlrWINdsKN26T9jn_3olZ5dUe9rfjmIsv3lEmHwixavncpFR0ZvsCYtUXp8NH-RLbmNYv6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=tRUz7HzSCGTEtFHx0-mjOsJ3-u34__cX4C5RZtRRORsWSiYJMYWq5pxy3hLmSUSURn7nC3x7q8lkevZQq-0kLC4iDy2xqw7gZ-6anC8igh3NUUyvs9hQk0-evRxGxAL2CBWhkokp_P7iU43VG1EqbciMFLqxMmhNoWa5DsbG_G8BNkAnFr_mzECv2TxQWwVEVKurMqWGMh_qB6xBI3ltCv9e8TYL_F-hTZG-VnbRaKnH987mevM7O7mTxqEOnhly00tDfq9G7bp5FlfJlrWINdsKN26T9jn_3olZ5dUe9rfjmIsv3lEmHwixavncpFR0ZvsCYtUXp8NH-RLbmNYv6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ملی‌پوشان فوتبال ایران پس از برگزاری دیدار تدارکاتی برابر روسیه وارد ایران شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140748" target="_blank">📅 16:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140747">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140747" target="_blank">📅 15:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140746">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq7zRpIYL9cGvE9-ytl_aQTT3VgdrDEaJI152KJ5AVKt7gR1ucy6MKQ3IIdErLlyjc3aenDcrTf0b8QYN6w96Ga0NzUajYq9YBh6XUJ1S0fTWyuTePtlMEAeiGBDVS_LqJSixc-hEyf_KxAooxrH9h1PicABZhcDqCenHiH8BmYELEmgAKGNMcGqsV_whgLgypBM_Sx2X0mrC4sDZCTa-87jczTbsOKHhr1KgRqq8s1b1PmwpxTXXPVJm0wZFOJ_lLv946fot_klSLAxd0Ar8DZOWpoxESW2la_CMKAEk9oX9RmuK0V_dN_aK7U0utHlWdlNI3x-2uIYt4csrYOhyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
اگه درآینده جنگ رخ بده و بیش از 90 روز طول بکشه بازیکن میتونه یه اخطاره 30 روزه به مدیریت باشگاه‌بده و بعدش‌هم توافقی قراردادش رو فسخ کنه اما اگه جنگ کمتر از 90 روز باشه بازیکنان خارجی باشگاه‌ها حق هییییچگونه فسخی ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140746" target="_blank">📅 14:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140745">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140745" target="_blank">📅 14:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140744">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭕️
⭕️
ابوالفضل رزاق پور مدافع چپ تیم فولاد: از پرسپولیس آفر دریافت‌کرده‌ام‌اگه دو باشگاه به توافق کامل برسن درنیم‌فصل راهی این باشگاه خواهم شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140744" target="_blank">📅 14:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140743">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی  امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :  پ.ن تارتار به شدت راضیه از یاسین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140743" target="_blank">📅 14:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140742">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
بازگشت دنیل گرا به تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140742" target="_blank">📅 14:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140741">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5j6FqxcyvRmtmOeNCX7NzW3kxPj1HqTCPs5cr4edWv_azFAJHSJSLlL2QE3bxid2WczaV6ZxGG6qfgg7B2L9RqiHRHhXCabh40w0PSCNKfYzrdqcbdAPjsIo57_sMYLfJGOKoQK7FZ4DaVVVzF3ZuWYENpmob5VVgIBox7uHp9SRLFBMhH-PQoEHYueQXPpTkzpzjPhYOQU3-MSGWSzEUUpkPT2jr3n-NHIVx3AItJmW0BzWpX98pB1kLVm2nsmPIcxrsnkXWa3DqI5Nr9sR6rnKxW2rcft_2ba1FgNs2uqYPUpjJk84x4-DoLYt_1yDG4bbgYdmLs1fRGS_QWOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
🔵
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140741" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140740">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
آخرین وضعیت پرونده جادوگر فوتبال؛ تمام اموال نامشروع مصادره شد
🔄
🔄
رئیس کل دادگستری استان البرز:
❌
❌
در پی دستگیری و محاکمه شخصی که در محافل ورزشی به نام «جادوگر فوتبال» معروف بوده است؛ وی به اتهام «فعالیت تبلیغی انحرافی مغایر یا مخل به شرع از طریق ادعای واهی و کذب» به تحمل ۵ سال حبس و ضبط اموال نامشروع حاصل از جرم محکوم شد.
❌
❌
حدود ۶۶۰۰ دلار، بیش از ۲ هزار یورو، ۸۰ سکه تمام بهار آزادی، ۳ شمش طلا و مقادیری طلا و ۲ دستگاه خودرو تویوتا لندکروز و مرسدس بنز از متهم کشف شد.
✔️
✔️
متهم هم اکنون در حال تحمل پنج سال محکومیت حبس صادره است و کلیه آلات و ادوات مختلف مربوط به سحر و جادو که از متهم کشف شده بود هم معدوم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140740" target="_blank">📅 13:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140739">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
🏟
بازسازی زیرساخت‌های پرسپولیس
✔️
✔️
رختکن‌ها، چمن، نیمکت‌ها و سکوهای ورزشگاه شهید کاظمی بازسازی و بهسازی شدن. بازسازی کامل استخر درفشی‌فر هم تقریباً تمومه و قراره نیمه دوم مهرماه به بهره‌برداری برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140739" target="_blank">📅 13:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140738">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🤩
⚽
شاهکار پیمان حدادی در پرسپولیس؛ درآمدزایی ۱۳۶۵ میلیارد تومانی از پیراهن سرخ‌ها
❌
پیمان حدادی، مدیرعامل پرسپولیس، پس از پشت سر گذاشتن نقل‌وانتقالاتی موفق و پیروزی در پرونده‌های حقوقی باشگاه، حالا با یک دستاورد اقتصادی قابل‌توجه مورد توجه قرار گرفته است. بر…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140738" target="_blank">📅 11:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140737">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eyezfe0IBcjdPQSkw32jnx2xWfEtEZVEkdLDBjsjZwYXQ2VeFCGCT8FMauGIzNPQgv7d_Qyv1q-ExScQ-2aShoMY-yY3j369kXSeFGIorQdc1oh96g2FWIomVHsxAqPvqdUHxhLgVO0_dRELxImZtaR4Xy1LEERmCcuJhASwL3TEkwIrDuDTcoDpU65jwh66e8SKyP7Tvl8qxopJvnJc2OaAsiV2rmTwLbQPONwwo90CjpovprWtAX7gwSqY0I0rL2RR88BUeLwS6gEI1PB4y9glEzUO31NtMbv4W_HaiwVwyk8VJzBiWEVlDNQ1X-QC1kScVOfhKywHgv3K8niDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140737" target="_blank">📅 11:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140736">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3297ba87bf.mp4?token=rgEm3fNulS4kCIGZb3a9K2cA3gVFAbOHnGNk9LSPznJ6qv3rjQqNDvm73WxKBSdAmXKypOXFAgbBpA40phjL9cz_8YQPJr7RsfHVTGUqc5zavtHYIn9oDuZxlu4fsY1gUxkMXe3bFnHu0j5JPll3F3yYySxHLPz2wtgAWs4NM9NUILBmBPlKCLNlPBunJ3Ac2O9CCFyBzB7xDpIQqBbidMhodIX1XGZS1-gENH_iYY16MlDIWtOFhnKGncyl-_Saz1PN9qz4Jnzm7vq3CIj8TmQ4s98Y2yWQ9W0k9VX6BeKWOtN1OrD7lSwoDCWwIXe0M3Bnr1LSK7eJHbhzdPRvlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3297ba87bf.mp4?token=rgEm3fNulS4kCIGZb3a9K2cA3gVFAbOHnGNk9LSPznJ6qv3rjQqNDvm73WxKBSdAmXKypOXFAgbBpA40phjL9cz_8YQPJr7RsfHVTGUqc5zavtHYIn9oDuZxlu4fsY1gUxkMXe3bFnHu0j5JPll3F3yYySxHLPz2wtgAWs4NM9NUILBmBPlKCLNlPBunJ3Ac2O9CCFyBzB7xDpIQqBbidMhodIX1XGZS1-gENH_iYY16MlDIWtOFhnKGncyl-_Saz1PN9qz4Jnzm7vq3CIj8TmQ4s98Y2yWQ9W0k9VX6BeKWOtN1OrD7lSwoDCWwIXe0M3Bnr1LSK7eJHbhzdPRvlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۶ سال گذشت...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140736" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140735">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
مصدومیت دانیال ایری از ناحیه کشاله ران پا بوده و مداوا روش شروع شده تا بزودی به تمرینات برگرده؛ اما بعیده به بازی صنعت نفت برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140735" target="_blank">📅 10:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140734">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
🏥
دانیال ایری در بازی آخر تیم امید مصدوم شد؛ MRI کشیدگی عضلات لگن و بالای کشاله ران رو نشون داد. کادر پزشکی پرسپولیس هم درمان و فیزیوتراپی رو شروع کرده تا هرچه زودتر برگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140734" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140733">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
❌
گروهبان قندلی: از بازیکنانی که به آنها فضا دادیم اما نتونستن چیزی که مدنظر ما هست رو انجام بدن در اردوهای بعدی استفاده نخواهیم کرد
😁
✔️
✔️
این بازی ما رو یاد جام جهانی انداخت و سطحش در حد این رقابت‌ها بود. برای ما بسیار مفید بود هرچند از نتیجه ناراحت هستیم…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140733" target="_blank">📅 10:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140732">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
❌
گروهبان قندلی: از بازیکنانی که به آنها فضا دادیم اما نتونستن چیزی که مدنظر ما هست رو انجام بدن در اردوهای بعدی استفاده نخواهیم کرد
😁
✔️
✔️
این بازی ما رو یاد جام جهانی انداخت و سطحش در حد این رقابت‌ها بود. برای ما بسیار مفید بود هرچند از نتیجه ناراحت هستیم…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140732" target="_blank">📅 10:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140731">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLByMyoARZW4Vd72o5-gfqWozJV1P5yQjFaIzQKZvDopwpM66Dy-QjFbErBQDgBg3gQxv-B24DYR2h6lfiqXW1RGzl7TILSoBf_wls2MttoH1YgrT5yOzcPRzT9D7vL3Fh0y_i8Zz2hZwZTzgo0CGZYtZ6ttDYsvtuUUR2DSn9jAmCbpYGWYQwcxOMG3FDjZ9UO8dRuGCMYy456k66shMsdFTT7SVVGgFqOEZkqU2icqnh_RJFBDDgxejRPlnT8u3C9EO9z8MCy_--fMZgtCIIkWrfuF3tBrZEnoVfqZ98OSXcXrm1S7haOTpaTTJ_kexA1WIC771i8llPYBoj4iXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
حمله تند روزنامه‌های ورزشی به قلعه‌‌نویی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140731" target="_blank">📅 09:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140730">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSomjsAnMW1oynkj2S3O2gBxTrGqNNwp417MStcHI3qVux29LGVKZLFmPIG013ppQ4QF9A4U9HXB9SepR60svRfXAPtCUXrt_3vtUURDueOGljoZXejsYruMtjYsVOpKIqzwBwuIgtMgygZ_-WU3I_lHyXzgECoxOPQZaY5FfUGDA_zaut9_FR-6cPO4JZJL8xEps1akjhXtKpGgq4s8_vsQUMaEmpZAhgXp9KZXvtfFyi4SoY9zoxPGZjsgUBQE4a3yBiAfOWi1kMc_F-IRQJ-c1grfyF0sIfOUxtBuXTOywTCrPMVqvdSD1oUTvPAwZElFpo6yuMASztwnEADWTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140730" target="_blank">📅 09:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140729">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX-Ys9Woikj-RmH6qmdnS-ZWDuSh0JE9JWbgDuDhIMWUhfOsiqqIXMi_rxgcsUij0dtd562_6s6gu9sXdf-SKQrjtxtsFfuF6s5dvPVFpq7eJaJfPVmreHxdAfU7R3n0wsLDrOql85rIuVd6jmd7vSRx1Q0yb0YxkRLOPbmjPZ0tjoJVXICMQrlLfDwL_FRHZC8qA26HCISzuz1zm0627Ll0oz-YLZqi92fjLNB4x00v4B62By7N_5OXUpndmimUrctA5blv16Yk8seGWyISyVTPM-nCInk_OB0NOU3o4ItnyqWHA9Jd1JISbyk3G6gFKduGwB0LV_KqQSMTkdVXTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140729" target="_blank">📅 01:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140728">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1qCmzI5cKexJ3H3Z2It3d3A8qlXE_DB22eFg-1QOl2yl_QykOhBXpWhsAaambuR5XTDwHmHmfM3o-JmYDKgWyFErolWsOfEnD9PLkdxohyasvZNbvf9ZHAYx7KGxRi-TqGhsjgj3v_bVptkUAfTEYgxjxkdVWBgiC6qiric9yEHSrHG6YfgXOjitdRBo8ory6gaIt1dLAZidXhtFvSBvKtxkbhPe-zIoQ7sLRijn_SdxZzWT904KODcpuIZDoCD4FwgroYWAdowQwOi5RIkEBUbUmsuM-ZJ_eSUaMd7prKwoEDxRuaWMRnlKaiSDhBUOZVwn1MxVBHtBCXC-yPbOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
در تاریخ بنوسید تو فوتبال‌‌فاسد ایران قرار بوده استقلال جام رو بگیره بجاش ٧۵٠ هزاردلار طلبش از مهدی‌تاج رو بلاعوض کنن‌‌. پشت‌پرده درحال انجام بوده اما مخالفت شدید باشگاه‌ها این معامله کثیف پول با جام بهم میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140728" target="_blank">📅 00:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140727">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
#فوووووری
🖍
دانیال ایری به دلیل مصدومیت در تمرین امروز  سرخپوشان غایب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140727" target="_blank">📅 00:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140726">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏆
🏆
نتایج بازی های امشب:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140726" target="_blank">📅 00:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140725">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jku56pQ_z9YZ4EAUpaTxSbX-QRss-vO8_T8m8_cZiffpcAewCzvu1zIYIsT_jMJtylNakSUa81JGDZG_yM7JzQA7s3sojOVbpl1vy1TyqaTVuVDR3JIKBenfV_xyMCi4AL6NQ7jwxcl3k29QKwGquqHWmG1BOuX86iA6Pd5cjL6q_yREvowgyZnwuNVpD3UvK8mHBsCFX2D040WJTWLNS1Xvih-9D-EVE9SlXUyjnLdrua6CnBvePgn1rAcofpHBCuheHN-LpISyvaVIu_scd1HI59U6zfYnrQIcQicEXdQbDWxT6-8q-qbzt5mZRLeAEF332oUho3YExTL_C3e7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
نتایج بازی های امشب:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140725" target="_blank">📅 00:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140724">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140724" target="_blank">📅 00:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140723">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNSbctMoWxrv9mr8-C6R-pMqWaLgCPdqzcdpRL3qrZzvqDAw2IlfKQWhXe5F2oiJ-P2kHJL3Os6UWqXcwcjSRL8N1lEKsvB9zprZJbEXcSfV6z7UyaPa-8jsD_EDryv4rZ-dsO88jqEUdmR8WmpAHBKewuXGJgOUTK4yfhvUtNCYEHuUDgnt7Rlhwtwn8m62LknW92g1dJCGeFrKW8k2vAStU-Q1fiuGuDsSdv8zXLyy4FCLTJ4bPEx9y6axt56ssfhx_EG6CRoqocE50MI1PoT4ipiV90wRolr3DZoYaF8irXcGaGGuSURn-YuwPHuErZJ4u-eYEdvZoezwTTRA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
مدت قرارداد احتمالی جدید نیازمند با پرسپولیس مشخص شد
⚪️
⚪️
پیام نیازمند گلر پرسپولیس که اخیرا مذاکراتش را با این باشگاه برای تمدید قرارداد آغاز کرده طبق شنیده ها به توافقات نسبی دست یافته. طبق شنیده‌ها قرارداد جدید نیازمند با پرسپولیس 2 ساله خواهد بود و گلر فعلی سرخپوشان قرار است دو فصل دیگر نیز در جمع پرسپولیسی‌ها باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140723" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140722">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140722" target="_blank">📅 23:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140721">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWkyoG3m2QB0Ric2_J-mxGyRUZLL_I5cFvbuiUKTrZpcEG8kLUC5RLigG9MHsQx7tUHnZ1MDEnw04fQ_0JTP5iWmKseB-jrKhyULjvNhZ8xUis5-ZYmAtPUSMohoNrNZyUwgaYVO7Dle7-HvmaiRYDo-T7pgS-1nBSiG4iJXsf-Skq0rXSZPmZDD_uwlgRPhx7eiXokPT575d1e7lTgxqt4N4hgKTorklx-_H7unA3S1rDd5CGO2si3o2RMwGKhT5i5m1uaRpYytwhiGBNma_vyXZVUp7utXctgeAFiaid_RuCyAiHOIDCt9rtVCTjyCgX6G0XDN5bCYMxkEFKSS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
قرارداد ۱۳۶۵ میلیاردی پرسپولیس برای تبلیغات البسه
✔️
✔️
باشگاه پرسپولیس قراردادی به مبلغ ۱۳۶۵ میلیارد تومان برای تبلیغات بر روی البسه تیم‌های خود شامل بزرگسالان، رده‌های پایه و بانوان منعقد کرد.
✔️
✔️
این قرارداد برای فصل جاری جهت اطلاع عموم بر روی سایت کدال…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140721" target="_blank">📅 22:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140720">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg3PX4qk5cLSt0SwTpWUdGDKsEq_thx6U2KoZ4DywO9fW32LTPbP5dlpnDXlOhFZc2g8h6xDm78QF_9HKdF0QCfoMbvT5kfh9LwoDZkuMgfb81x5iyWYGMv4SdHkvkzdeoHsPJr9-W74j740qLgjxXnDOSL2v2xdHyj-BCUhAjTQCRSLDEvj5CFmqT1BRJhjW3MoypgWRrASFY5cmUgZUHvV09izFhO7WuXnar_sV53jtlg4nSxNcW1ozZMebn5I5pG-6RnxaxXaYfaNR3jshkXUewNWvL_La9ryD-QIXW3ThU4GgnegiW-0HhSkzEB1uW6Vz9Am-SgutDkCt-_FTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اگه پیام نیازمند نبود، فاجعه بازی انگلیس تکرار میشد؛ تفاوت دروازبان درجه یک با دروازبان معمولی اینجور جاها معلوم میشه
❤️
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140720" target="_blank">📅 22:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140719">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
لباس پرسپولیس عوض می‌شود
⚡️
⚡️
باشگاه پرسپولیس برای فصل جدید رقابت‌های فوتبال، در آستانه تغییر برند تولیدکننده البسه خود قرار دارد.
⚡️
⚡️
⚡️
برند «یوسف جامه» در فرایند مربوط به انتخاب تولیدکننده البسه باشگاه پرسپولیس، توانسته نظر کمیسیون معاملات باشگاه را جلب…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140719" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140718">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=iOAJHII-T5THZVisToeyDNV2bD-6GmwlEh6OGpAoX5Iydde6xP2ai--cqE24PqU-MkJ8TDHAeafFiswhV8AJZrU68V-TlDm3VDCwoa-06k9g1x0rljQz-duUGcUmfD-YmA2AyjhsIfetNv0lZ4u2_OPDvzBMTNrzEj7Wjvl6yQ7FM0BCdcstG8dnwhk0VLFh9BKMWH1Qg3w_kJ9iy-HL6Xskx4yN7gWjUudurxZtUosCwB7LMWLDNyy-G5Gz6pzdiuygKn-K04mRsvDDFBsMzBnrB1A1AcLVLIu2_nn8RPMcVmZ71vPryNN4xmUssyiGEJNKHcY-WEqAqLR8-DTGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=iOAJHII-T5THZVisToeyDNV2bD-6GmwlEh6OGpAoX5Iydde6xP2ai--cqE24PqU-MkJ8TDHAeafFiswhV8AJZrU68V-TlDm3VDCwoa-06k9g1x0rljQz-duUGcUmfD-YmA2AyjhsIfetNv0lZ4u2_OPDvzBMTNrzEj7Wjvl6yQ7FM0BCdcstG8dnwhk0VLFh9BKMWH1Qg3w_kJ9iy-HL6Xskx4yN7gWjUudurxZtUosCwB7LMWLDNyy-G5Gz6pzdiuygKn-K04mRsvDDFBsMzBnrB1A1AcLVLIu2_nn8RPMcVmZ71vPryNN4xmUssyiGEJNKHcY-WEqAqLR8-DTGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
درگیری شدید در بازی رده نوجوانان لیگ تهران میان تیم‌های کیسه و شاهین!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140718" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140717">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
پرسپولیس هنوز هیچ توافق یا مذاکره‌ای با اندونگ انجام نداده/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140717" target="_blank">📅 22:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140716">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
پایان  بازی روسیه 2 _ 0 ایران
✔️
✔️
یک نمایش ناامید کننده دیگر از تیم ملی/ با «مدل بازی متفاوت» هم باختیم!
❌
❌
در حالی که امیر قلعه‌نویی وعده داده بود تیم ملی با مدلی متفاوت برابر روسیه به میدان می‌رود اما نمایش تیم ملی همان همیشگی بود؛ نگران کننده و ناامید…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140716" target="_blank">📅 21:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66e4f7259.mp4?token=gxKRKR6nCBz79geaqfuMGmhXM8h8P0nPw4xweqCnVWMVBNoEcl-19oWWIUHMcu38fAds2lPKg2gzTxq8gjRjKjnX1olpUwA_EUroZuSFtCKZVoMymu2BRhLfgoIahvA_tHyOQBYoiIHUDSh12yh-K5IBjd_qdN7jaDSiNT-pB1SD52KZBlEKpKzH_BLSxlQwPjsxGOWs-Ju60s0_J4MU3QMkoWVJZmytiwXNJ5BJpWKpdSJ4l4zx0f_D-_D2KDtXG0G2VeKwrC0xT6FJxNcSEPbip8OR_mV58jzkVGmlicy_wCi3gHJVVfBF-7HRuOUNt8UnujUesdYbSsbocPlpKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66e4f7259.mp4?token=gxKRKR6nCBz79geaqfuMGmhXM8h8P0nPw4xweqCnVWMVBNoEcl-19oWWIUHMcu38fAds2lPKg2gzTxq8gjRjKjnX1olpUwA_EUroZuSFtCKZVoMymu2BRhLfgoIahvA_tHyOQBYoiIHUDSh12yh-K5IBjd_qdN7jaDSiNT-pB1SD52KZBlEKpKzH_BLSxlQwPjsxGOWs-Ju60s0_J4MU3QMkoWVJZmytiwXNJ5BJpWKpdSJ4l4zx0f_D-_D2KDtXG0G2VeKwrC0xT6FJxNcSEPbip8OR_mV58jzkVGmlicy_wCi3gHJVVfBF-7HRuOUNt8UnujUesdYbSsbocPlpKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140715" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
سومین سوپر سیو از پیام !!!
⬇
دمت گرم واقعا پیام جون
🔄
یه تنه جلوی آبروریزی رو گرفتی سلطان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140714" target="_blank">📅 21:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYrPMKCecvHDKcYi7QEDDM91XeJ8uvXrZsJ3pjdRxyPS0wCGPLxpKy6qNMOvdZIcrwq0dirE8TNeNzGXhzuW2m5UR2drmgNhomF1PzdHmgjeSK65vtsDqH54gtcj3yhRVpflCf9qwtW2VRsmZVPRWw-ubLjftYZD8YVblyMaDjCXBUpdQkeukeH1Y-TbApMS46_alRgxgOhuISu8_blWOYZG_bC3HoTtajnfHukypYlbWoquzyT50yp5aIlGHunvb2PVbq8WpJvmm6PYtgUYCAo8mIa_MdZdWDRD66sOSqavEcqKed56_R4cYNDSWnGSHZ-rbSgnddj5OXoS_mCqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140713" target="_blank">📅 21:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
آقای قلعه نوعی با ی خداحافظی کل ایران و خوشحال کن .....سومین گل هم از ازبکستان خوردیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140712" target="_blank">📅 21:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140711">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
❌
با دعوت احسان حاج‌صفی به اردوی تیم ملی این بازیکن در صورتی که مقابل ازبکستان و روسیه حتی یک دقیقه بازی کنه رکورددار بازی با پیراهن ایران خواهد بود و از علی دایی و جواد نکونام عبور خواهد کرد
✔️
جواد نکونام ـ 149 بازی ملی
✔️
علی دایی - 148 بازی ملی
✔️
احسان…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140711" target="_blank">📅 20:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140710">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140710" target="_blank">📅 20:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
کنعانی و علیپور به دیدار مقابل صنعت نفت نخواهند رسید/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140709" target="_blank">📅 20:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
✅
آقای قلعه نوعی با ی خداحافظی کل ایران و خوشحال کن .....سومین گل هم از ازبکستان خوردیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140708" target="_blank">📅 20:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=pm3ptgsxX06fOvys4d76Otinf3CHBYNmGZ1ys0nJwyTNTJDhtbzF5mENm4_cNC2P8V_2kyhrwn8abvET3lqNqoQhoB0siUerXIL0Fze14jlHtGk2WlxkbLY9Wyl4Hz7__8mx-ZwXI3Ka7cnP7vfTyvKhv1Njqd69d3E__cxPydcGD227rSbPDqTGFSUYqc0Nj4fpEA7lBtKmKDAOri5F3E3-3AIKZUG8hgBN1gyUh6vIxibghqcea8oOJCsYpn2QzX9CcyWE75WVG-csUEcA-l8_51I8ADmx9bJzFa1ebhBL43m0OszhPaqDPGeAlFDh5RLG7CXaHcFPzTDLwjCYiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=pm3ptgsxX06fOvys4d76Otinf3CHBYNmGZ1ys0nJwyTNTJDhtbzF5mENm4_cNC2P8V_2kyhrwn8abvET3lqNqoQhoB0siUerXIL0Fze14jlHtGk2WlxkbLY9Wyl4Hz7__8mx-ZwXI3Ka7cnP7vfTyvKhv1Njqd69d3E__cxPydcGD227rSbPDqTGFSUYqc0Nj4fpEA7lBtKmKDAOri5F3E3-3AIKZUG8hgBN1gyUh6vIxibghqcea8oOJCsYpn2QzX9CcyWE75WVG-csUEcA-l8_51I8ADmx9bJzFa1ebhBL43m0OszhPaqDPGeAlFDh5RLG7CXaHcFPzTDLwjCYiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇷🇺
گل دوم روسیه به ایران توسط گلوین در دقیقه ۳۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140707" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtb0f73Teh2ApYDlAT0KL8_kYV1GET8BPQ4kjxQATtQquuk70OJV-UhlbqNNBWuRavTk29MIksVxnT9SydxNmkCRpOt1YHxcf23RV-EZzL0pDOATnHrqS-5KgJQw7pppHbTTzwnPInm70FdmK_D9VePJ9z7ZIgflRWXz-Tdd0iWl5C0YkY-J8qrPrGgmH2yV_EiBKwFXS1l4IDB6LME4aoB8a8uPpgMEX4pHJZxp-PI0ngDKfr-Ebuglfy0S5zuqaIwuZwmlTvfkvqbIxKqlkmtk943ci_Cba1zOgwIlicTD72Iaq9YUjd-p6Kq4fW4cWtoP5y0zy-t7y0pazrd5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد ماتادورها و شطرنجی‌ها امشب در یک دوئل تماشایی!
🔥
⚡️
[
اسپانیا
🇪🇸
🆚
🇭🇷
کرواسی
]
⚽️
اسپانیا بعد از برد ۳-۲ مقابل انگلیس با ۵ برد متوالی وارد این بازی شده و در ۶ تقابل اخیرش با کرواسی ۴ برد داشته است. کرواسی هم در بازی اول ۲-۱ چک را برده، اما مقابل مالکیت و پرس اسپانیا احتمالاً بیشتر به انتقال سریع و ضدحمله تکیه می‌کند. باتوجه به روند دو تیم، سناریوی بازی نزدیک اما پرموقعیت محتمل است؛ اسپانیا از نظر خلق موقعیت دست بالاتر را دارد و یامال می‌تواند مهره کلیدی باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140706" target="_blank">📅 20:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140705" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be44fa519.mp4?token=Wl4dGaWRqOoAgTVEzTWvWMzdUejsrKRc836VoaC0s-RTQR2yIAPJrk0BVnQy5eL2tK5cDKpvdlgJmEoa2f-dGtw_51qiUp2w2iy_3cecvP13LK4WzG_NgJRvSnBKGcRXMpGH93dLM-swQUM7XBlxf4hjO1A5HwIlaC8v4lcrpNMKvKkzUhk67bzlkEnVd33_7AVuKN5X7xKd1irmWYvstH-x0ghRk1MOu9szuBLdErB5r7bCyVzo4ascmLCt52KEnCcuc9tS8g-DSLwEQwVC_3X2omOQtBFi0yGlJmiP_RaiSbACntawcQZhJWnauq82wIUDkXrPaDZ1f6GRZPmrkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be44fa519.mp4?token=Wl4dGaWRqOoAgTVEzTWvWMzdUejsrKRc836VoaC0s-RTQR2yIAPJrk0BVnQy5eL2tK5cDKpvdlgJmEoa2f-dGtw_51qiUp2w2iy_3cecvP13LK4WzG_NgJRvSnBKGcRXMpGH93dLM-swQUM7XBlxf4hjO1A5HwIlaC8v4lcrpNMKvKkzUhk67bzlkEnVd33_7AVuKN5X7xKd1irmWYvstH-x0ghRk1MOu9szuBLdErB5r7bCyVzo4ascmLCt52KEnCcuc9tS8g-DSLwEQwVC_3X2omOQtBFi0yGlJmiP_RaiSbACntawcQZhJWnauq82wIUDkXrPaDZ1f6GRZPmrkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140704" target="_blank">📅 20:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
تیم قلعه‌نویی گل اول از روسیه هم خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140703" target="_blank">📅 20:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a7b7886c.mp4?token=at5H4i8bZpqjcR1Ha5GAj0F_BUUk2ARf2G636vkNn10l65Al0nN-Y8fAUocM0ffkDwOsUTzjGCuZI7bJHGCP82Akxf-kEahCAcz8N4dd2nJz3bsOSFwG0AmDPk2bwglxxXRx37LDMzgjjvCzH06T7MSItxqZN87JNEndhkDmOaUoiT6R6-sbKez-MoXiZUv0xD00SRtKP2AsKDVHOatTii-2fy71YQuu6iP5Tr-J8sLxL29ewZY8dWw2srOyjBQ8uZNNk_fDGDQC3ybIZeb1VXFeD0Ng9vW8hOqj1nxx727Lq-RZG6IoO43WdHsKlP2F0rIs0IMCtYTtvIuf1dzOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a7b7886c.mp4?token=at5H4i8bZpqjcR1Ha5GAj0F_BUUk2ARf2G636vkNn10l65Al0nN-Y8fAUocM0ffkDwOsUTzjGCuZI7bJHGCP82Akxf-kEahCAcz8N4dd2nJz3bsOSFwG0AmDPk2bwglxxXRx37LDMzgjjvCzH06T7MSItxqZN87JNEndhkDmOaUoiT6R6-sbKez-MoXiZUv0xD00SRtKP2AsKDVHOatTii-2fy71YQuu6iP5Tr-J8sLxL29ewZY8dWw2srOyjBQ8uZNNk_fDGDQC3ybIZeb1VXFeD0Ng9vW8hOqj1nxx727Lq-RZG6IoO43WdHsKlP2F0rIs0IMCtYTtvIuf1dzOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم قلعه‌نویی گل اول از روسیه هم خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140702" target="_blank">📅 20:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140701" target="_blank">📅 19:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همه هواداران پرسپولیس از مدیران باشگاه عاجزانه تقاضا دارن تا ماجرای یاسر آسانی رو تا ته تهش پیش برن.
🔺
آخرش اینه که یه پولی میخواییم بدیم و رای هم صادر نشه به نفعمون، این همه پرونده بوده که هزینه کردیم و باختیم، اینم روش
🔺
دقیقا از روزی که فهمیدن…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140700" target="_blank">📅 19:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01dc83e8df.mp4?token=caZAVzyTxBhbYYlotkFIqzrIr9LNRhDGst7JuV7jSPkBE_h2POVFycw_GrWolkMF5KCMr55TWya_gB68AHmjEhBc7lRxNW_zvcGI3rPXnXSuS66UaaHX5eavgKBR_rbB6kUji7_07rD-91eKlFR054_80Doe3Stv55e0Ug4il5CBAUS-l2QrLXhtXZrhpnNVjHfUPpPov2GSWQKkE6ks2-segz5xQJSGCyKeDJ-9KhnaNKtM7vZKZ-Fvg3FHmATmh_n8KhqQALhXleCvTmzewKWYiSExC9EPHSkaIdNAwjv4OlFx7Ib0Q614gS6yzB_nYl2m5NrsQde6P5X6Aabg8melicF1BU-ca1xwp_4rtBL-BOiPz0s97SWC1YCq5Y13Q_m-Ha4bsFCIlOr-J0UsU-Wt46670s9GfdQEFbQrd7FyfNGrfvkiICyYwHxcbJl9rLYiHyoLaGGwJUnCHbcYoQtH3ClhrvUQyN3iRT8sE-mzoyIfV7RvD_GWoF5yvdt60-_q0sT098eFVWguItD7KjtrRLcSNyFCSFXB33TUBvhrLqae236jhBFSYF4_AWy99ScX1ABPf2GvX-M8hDrCzYnS4Cg8H5HgcDnKVz6TZYqyYm0DQAl7xoZtM6uO-_D7OeIpPFGOMssubqHN_L_0RcnfPeFpD406-IApPnPoTwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01dc83e8df.mp4?token=caZAVzyTxBhbYYlotkFIqzrIr9LNRhDGst7JuV7jSPkBE_h2POVFycw_GrWolkMF5KCMr55TWya_gB68AHmjEhBc7lRxNW_zvcGI3rPXnXSuS66UaaHX5eavgKBR_rbB6kUji7_07rD-91eKlFR054_80Doe3Stv55e0Ug4il5CBAUS-l2QrLXhtXZrhpnNVjHfUPpPov2GSWQKkE6ks2-segz5xQJSGCyKeDJ-9KhnaNKtM7vZKZ-Fvg3FHmATmh_n8KhqQALhXleCvTmzewKWYiSExC9EPHSkaIdNAwjv4OlFx7Ib0Q614gS6yzB_nYl2m5NrsQde6P5X6Aabg8melicF1BU-ca1xwp_4rtBL-BOiPz0s97SWC1YCq5Y13Q_m-Ha4bsFCIlOr-J0UsU-Wt46670s9GfdQEFbQrd7FyfNGrfvkiICyYwHxcbJl9rLYiHyoLaGGwJUnCHbcYoQtH3ClhrvUQyN3iRT8sE-mzoyIfV7RvD_GWoF5yvdt60-_q0sT098eFVWguItD7KjtrRLcSNyFCSFXB33TUBvhrLqae236jhBFSYF4_AWy99ScX1ABPf2GvX-M8hDrCzYnS4Cg8H5HgcDnKVz6TZYqyYm0DQAl7xoZtM6uO-_D7OeIpPFGOMssubqHN_L_0RcnfPeFpD406-IApPnPoTwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
🔴
حضور پیمان حدادی مدیرعامل باشگاه پرسپولیس در ایستگاه 88 خیابان پارک وی به مناسبت روز آتش نشان
🔴
مسئولان پرسپولیس در این دیدار ضمن خدا قوت به پرسنل این ایستگاه آتش نشانی با اهدای گل و یک پیراهن پرسپولیس از این قشر زحمت کش تقدیر کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140699" target="_blank">📅 18:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140698">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
ساعت بازی ایران و روسیه تغییر کرد
❌
❌
فدراسیون فوتبال روسیه از تغییر زمان آغاز دیدار دوستانه تیم ملی این کشور برابر ایران خبر داد.
❌
❌
تیم ملی فوتبال روسیه به هدایت والری کارپین، روز ۲۹ سپتامبر (۷ مهر) در شهر کازان به مصاف ایران خواهد رفت. سوت آغاز این مسابقه…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140698" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140697">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
🔴
🔴
رسمی/ صنعت‌نفت برابر مس پیروز اعلام شد
🔄
🔄
کمیته انضباطی فدراسیون فوتبال در پی عدم حضور تیم مس رفسنجان در دیدار پلی‌آف مقابل صنعت نفت آبادان، نتیجه بازی را ۳ بر صفر به سود صنعت نفت اعلام کرد. با این حکم، صنعت نفت به لیگ برتر صعود و مس رفسنجان به دسته پایین‌تر…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140697" target="_blank">📅 16:46 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
