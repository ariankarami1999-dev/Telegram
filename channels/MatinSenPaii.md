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
<img src="https://cdn1.telesco.pe/file/aEC37PnoxOPuq-UUphTpSuVweXPHqUcNcC0I17bVu7-vyIV29edZ1KdCKR6hjULyW6ndciwCV1cj4Lid7J-_jCo9dskKc55U2-ebq1y8o2bJ189snVdEJkvnJhrr3yPyEraK2fSsL-lwg7Q2Zockn5UFY9oqELepvORGQwaca5jDFIxS7Fv9Cc6QrCejHDfhV0iq7RW6OBUi1Kef_HziElYlam-UG7ucCwuxldAvKZtYBQ-80L7gmIiKyOlM34_vAMR1VrnUY1ejgnu876LCk0677toznkpYXkoUV4ByLYTH7AWdNM1mFbc_yCQEjj_8hlyMRbnbuQqQNp598X5-kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 160K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 07:27:51</div>
<hr>

<div class="tg-post" id="msg-4014">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nz_Pscwo3BgQ-BAUOFO3uXYNiJcq3eek4tCvYvxx_ChlEw5uZsQHVTAxyi70kB-iWoU-ILJVqHxtvMESY2Pxjo1rbWcqivfunVW1uk0P5xc_l6a5r4TNt7c3wBwHlhp2gGeCehLzvdvTDhym2fRteJm7hkSRmjVoua4UVk22MqGxNwDCEOmlgWIQGfKkFfwNjXNpiPQTpDpRy081lr7FxKUH3pmpNrTOfyCJpYzqp7CC_aYn0PJYJRjhR4FxofVcg3SvvDnZZM39sS8OGCFM59DfiCJpklVFbE6o-ZXe2D4ZUts0HtH2w6S6Q34XdD9EprfU6cI1289OSTvv-jZE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:  سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه برنامه‌ریزی…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/MatinSenPaii/4014" target="_blank">📅 02:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4013">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خلاصه‌سازی ترانسکریپت YouTube</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/MatinSenPaii/4013" target="_blank">📅 00:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4012">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QxG6nNZHIibIysY4nRgBHpC5XI-ftPOXTE1Eg0Xe7R4EXGa7PurKSHfu44Y-Wqs7E6n12TMMlSWwuw0qaRfiO_ys0r_GeRtyJ9qAY56KBlcIwCHSMBUkCWiooegcBp59EZ9Q2bWNV8KJeciuGb1YBR4xrO0s1fdoQEbQl7_Z2E1xzjVzHLMgbCzrrlbWKN4aKsT6OUKt_NKsdJ-SEoGugpzzGXbwN_veK04uMXwLrV0jRLck1Zgofvvm9X9bgOuegseFeCs9uE_NEc7lnNobiCZIUOiLw0Ynq-r-ffJiiSjeUPH2AmRJb_HfhAEyFC-gQU4RVWcDn8Ts0uTsRpCC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:
سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون
اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه
برنامه‌ریزی cron job برای وظایف تکراری
مدیریت فایل‌ها (خواندن، نوشتن، جستجو، ویرایش، patch)
💻
توسعه نرم‌افزار
ساختاردهی کامل پروژه، کدنویسی و ریفکتور
گردش کار PR (branch، commit، open، review، merge)
توسعه مبتنی بر تست، دیباگ، بررسی کد
ساخت و اجرای پروژه‌ها (Python، Node.js و غیره)
🌐
وب و تحقیق
مرور وب، scrape صفحات و جستجو
فراخوانی API، تعامل با GitHub، Airtable، Notion، Google Workspace
جستجوی مقالات علمی در arXiv
مانیتور کردن وبلاگ‌ها و فیدهای RSS
🎨
خلاقیت و مدیا
تولید ASCII art، دیاگرام‌های معماری، اینفوگرافیک
ساخت پروتوتایپ HTML، انیمیشن‌های p5.js
تحلیل تصویر، تبدیل متن به گفتار
خلاصه‌سازی ترانسکریپت YouTube
🤖
Agent های خودمختار
تفویض زیروظایف به subagent های پس‌زمینه برای کار موازی
راه‌اندازی Codex/Claude Code برای وظایف تخصصی کدنویسی
📋
بهره‌وری
حافظه پایدار (یادآوری ترجیحات بین session ها)
سیستم Skill (ذخیره workflow های قابل استفاده مجدد)
یادداشت‌برداری با Obsidian
کنترل خانه هوشمند (Philips Hue)</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/MatinSenPaii/4012" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4011">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون https://t.me/MatinSenPaii/3990 ، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/MatinSenPaii/4011" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4010">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اپلیکیشنش متاسفانه پر از باگه اصلا Custom Url به درستی نمیگیره، سرچش بعضی وقتا خرابه و...
البته خودشون هم گفته بودن فاز تست هست هنوز
درود بر CLI</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/MatinSenPaii/4010" target="_blank">📅 00:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4008">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o5jkev_jxjdWUvPNhcZdrG3hPRpz9ZJwejxU--rxYBM7VCWVtXsVXmnMmU8aaU5qdMBPN2PlH-cK9uOs_8mh2ebAqoeIY1p1UtmjHhfpoNUzkbDYRakQ88nMooPQLWSE68DAGB-ZTprP_XFFGJL-wj7VLRBwUS1K02H__dCC_WNLY1oydFJzvyv8UOqqWQJFz5DPGglgAuIPt6XU-BuX1jBIoR0v3JxyCgW0GpDZNBD2yQwmy5eqdJCDA9Wu5V43lgQoxG7CXlyTsYIbpibMzaSHtXvUHV8QsKMZ6-2b1pBWSrd-nlmUEXH4y8MdWGSyfK2Rqog_teyzlnULTjbj7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gL64ZEMJJLnQ3LxIa29Bo-_BUgCJuyIGVRfavB-AzL0NrfikhsSOBnbu8_6F7zsS5Zo1XX4SvNctwaPOejkBiM6y-0YZpQFyovgi13nmpn3lLYdW9v2qYAnUV12GYvgpP3HAzr-U5KkRCOdjRkH7iffcYRfcHxJP5fiwvmGG6V18qHUTgy15GwKpUho2qT8tF8MNcQnxGCWt41udL4iJt1niy-75yZBWQwcBYlmk-_sXlFJGu43MH1D_4MWWqo58LHe_7fCDm1J98Z_w32E-5H7Bgzd5wGJB77ywCWqwn-gyvhl_NXIfq0IJn_Po4N-HJ7cEREfrTlUmOkZNLAUE6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون
https://t.me/MatinSenPaii/3990
، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/MatinSenPaii/4008" target="_blank">📅 00:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4007">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حالا ای کاش قیمت سخت‌افزار پایین میومد یه کم
😢</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4007" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4006">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjwAmULcexwCZMRbjiZuTDCjV2mo_tRphE8MtwJmuRkLkaF-8N2wD7FslxIUjNT0gyZ5dooQs2CVm9B81RbOyUGwpbAakhh09nV0AEPTz5dAbVZZvbsTUGLSQd1ZQDX8EhC370SskAkJ8M6EpRL4MwWBrXo_N4Pu1lYQV1Lil0BwVB-wAoosJHFi01vQoi_nf-_XrJUDZw9igt70pYvpsmg-L6XUz3geBoJqzPjlOyAX_WUIKwnpuwt6srt8LfgT-IJ7CCCWQs4sCDwxpBgOPFgh6tVO2zfm8MzdRZQZGKg3YMgPzXQvSZ68UqnmW4ow9k_gNP9syYfDwdNHT_Sokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تراشه هوش مصنوعی اختصاصی OpenAI با همکاری برادکام معرفی شد
شرکت OpenAI با همکاری برادکام از نخستین تراشه اختصاصی خود با نام Jalapeño  رونمایی کرد. این تراشه که از نوع ASIC است، به‌طور ویژه برای فرایند استنتاج و اجرای ابزارهای هوش مصنوعی مانند ChatGPT طراحی شده تا سرعت و پایداری خدمات را افزایش دهد و دسترسی کاربران را تسهیل کند. OpenAI می‌گوید فرایند طراحی این تراشه را طی ۹ ماه به پایان رسانده است.
خالق ChatGPT که پیش از این یکی از بزرگ‌ترین خریداران پردازنده‌های انویدیا بود، به‌دلیل رشد تقاضا تصمیم به توسعه پشته فناوری اختصاصی خود گرفته است. نمونه فیزیکی تراشه Jalapeño هم‌اکنون تحویل OpenAI شده و انتظار می‌رود استقرار اولیه این شتاب‌دهنده‌های هوش مصنوعی تا پایان سال ۲۰۲۶ آغاز شود تا زیرساختی کارآمدتر و ارزان‌تر برای آینده هوش مصنوعی فراهم شود.
✍️
دیجیاتو</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4006" target="_blank">📅 22:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4003">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4003" target="_blank">📅 21:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4002">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">توییتر هم دیدم چند نفر گفته بودن اما گویا منطقه‌ایه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4002" target="_blank">📅 19:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4001">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانفیگای کلودفلر روی ایرانسل واقعا دارن بد کار می‌کنن</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4001" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4000">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tUVJAdwKtfUBRrIFchN0QnBO-pGLnQygyRDYNBwRScIm195AQgbYaHPQaBgup1siMLKl7Xql0-AoINsN5MDuz3o6xkiYX0uWB8he_Ph2xYHTMZw6lrf0oGyefF7LgqUG5-jdwUPqdRUFsyrWVU3C21_hee223uCDuZ_X-r4UL5M-vngTbvBuP7sQbdQD0ZRtdghNP2Fp5mmygUbhFoQtVJOauTLuu0KkNlGVgkbjkkb7ftjmedo05Vq-rL0E0nH5YwBAQ5Zd0iGLJlOJhDFTSWuI8c_Vwybc7tTev6mQljsLrs8aKP-JTAJHAVXSgErvBFdLehOmO8dMvj72vOyPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس رو هم دارم نصب می‌کنم، به نظر خیلی چیز خفنی میاد. به زودی تست میکنم و ازش یه کم کار میکشم و نظرمو میگم</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4000" target="_blank">📅 19:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3999">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟  یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/3999" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3998">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3998" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/3998" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3997">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/3997" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3996">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برای دور زدن تحریم‌های اندروید استودیو، قبلا هزارتا پشتک وارو میزدیم. همزمان Shecan میزدیم و پروکسی و وی پی ان
🤣
اما الان با پروکسیفایر که وسطای این ویدئو
https://t.me/MatinSenPaii/3372
آموزش داده بودم، به راحتی هرچی نیاز داشتم با کانفیگ‌های کلودفلر دانلود کردم. با pdanet+ هم میتونید دور بزنید</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/3996" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3995">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">برای یه کاری دارم اندروید استودیو نصب می‌کنم و از الان گریه‌ام گرفته
😭
خداحافظ جای خالی روی لپ تاپ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/3995" target="_blank">📅 17:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3994">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:  برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید. برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/3994" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3993">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:
برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید.
برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.
بعدش روی آیکن مربع (سمت چپ فیلد Name و آیکن سنجاق) بزنین تا همه رکورد‌ها رو  انتخاب کنه و بعد پاک کنین همه رو.
اینکارو که کردید برگردید توی قسمت overview  و روی Review on Blocked Content page → بزنین.
توی صفحه بعدی روی آیکن سه نقطه بزنین و گزینه Request Review رو بزنین و I have removed the content. رو انتخاب کنین و بعد روی Request review بزنین.
یکم بعدش باید آنبلاک بشه دامینتون.
هرموقع که آنبلاک شد برگردید تو قسمت Dns Records و روی گزینه Import بزنین و اون خروجی‌ای که دفعه قبلی اکسپورت کرده بودن رو این سری import کنین که راحت همه رکوردهاتون برگردن.
احتمالش زیاده که مشکلتون حل بشه و دامینتون برگرده.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/3993" target="_blank">📅 15:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3992">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">از اینجا مستقیم میتونید برید سراغ آفر دیپ‌سیک رایگان اگه گیج شدید:
https://www.openmodel.ai/event</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/3992" target="_blank">📅 15:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3991">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/3991" target="_blank">📅 15:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3990">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uTX9LyLQqkVoS7dwIYcHSRSSeczILY4gSGk34bLF1RL334hLWVHnd0IUmlcwZmALo7b1v_NQB-s6UXJkLD2Q8hknuIdYEBqAII8tOgodHxva3oV7TIqoGzIzVJOn2ewdFNuj3tHcZ9BaYb2oE4lKzy---BdhmIujLkoJluXIqwE2FL_snw77LYCQdThfxck_8bUKq1swoXs9auARFwRaAT31WYB__3I0FbxC7UrNxBGfK373HKZFtvNiD5RpQ_vFlSCPmfDUH60kijAPE9hB2wHPEAWOMUYTYbBPWVp1Iq5Z7tm0UJhNRSmEdVJYoKOzZ9DU3VnpOXClRR3FFvGH_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده
https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/3990" target="_blank">📅 14:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3989">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OiRW-a2oqooP5t3gr8oKllEJ-tFViHqQPU27S0EMbDjo9FM9Uty56Ljr2a3a0zcSUArXRVVwDVxT3o6S1laNxOx7lloC8EkctVmoyewAsK-6Hwiz8Kb-18LqAY_3HDBA6BzgsQ3lFVMUtQoMT3-8hBL8mOPW1zGFneopqEJBup7bGtJ93FP17Q4Kdmf6tUbxze08WpfJfzzTOXQ8u2ev47_kK-snizWMVNdZOGkJh2NzBQFde1KLFqE6vuJfI1XjR9_WiX7PRwU8m-x0vB_xS7Xg8s5ybRDldDUQcsPPELbVk05Yjaa8KXYIyxqbclzTeXNi9A2AxrDDL6NGFSOk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..    Site 1: retrogames.onl‎ Site 2: retrogames.cc   @Linuxor ~ fireabusefyan</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/3989" target="_blank">📅 14:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3988">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8v7qlbFDGSzwhWwaOiMv2c-hITDyi1pQZ5ByvP2MxkN18xhv8nVDnwCjr-faVwPB3TAEvDQPzPaJhjTuveGqL27j-CyEVnQKwhyajbe1OGO567dJYV0YAN-kewES-nUQKi8Bo-V9-cRlFgE-9c7AKNpgYA7KTFAY0UwAhTK8ApOO_qmdm6oQGzxB--WJ8FQc76Wp786Lv2uqi2YxSvdaWVLaPD-D88xnwRVaMRW-iqAKa8rhWNrsfE_yAJxuttdTDCZHEMHyZHn4n1odY43w7CBzyMmqSthhmMRkb7i1s0WR6iMJa5FXH_riSMSkK0RCTXGCHXvP4t3gYTSY474nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..
Site 1:
retrogames.onl
‎
Site 2:
retrogames.cc
@Linuxor
~ fireabusefyan</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/3988" target="_blank">📅 14:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3987">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده
اول باید چک کنی آب وصله بعد کارتو بکنی وگرنه ممکنه گیر کنی
✍️
ادوارد وانیلی</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/3987" target="_blank">📅 13:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3986">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gobjThbazPehRzCTzRWD85LyigKaEpy-AyGi-I2PajJq2Rgfk3PSqZwmx1utJE-UdELXpfS35IUqWopw39hn0YQOM-cEuuXOidvO6vWuSrUifHsDph-ShMWiaA3-7e6eS37m9_nOy5SWbX1-cnRPROEM6yFtqTHSobsXQuBePMlZ_R_jrDTn5TdY5epUVqAQB9R1vq5sGR8QGCOwkmEOGUfFaHeBfm_yq1ui8O3i892MBt2mz2zW00d2USnofJqlWIIp67XDCaRJvwGmrdptKdiVKs0MpKg8nY-WqjvpWtdWSUGWXtpZUk47mytvHtqeEQ986iElen_eYUU6atHmGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید که توی توییتر یا جای دیگه، ننویسه عکستون توسط هوش مصنوعی ساخته شده(نمیدونم چرا برای خودم رو مخه) می‌تونید یک بار اون عکس رو توی save message تلگرامتون بفرستید، سیوش کنید مجددا که متادیتا پاک بشه و اونوقت اگه پستش کنید اینو نمی‌نویسه</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/3986" target="_blank">📅 11:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3985">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CcSkV9xCBQcgScyFEzDWxCSs4qw1Awr3-NPksnY6ywe-4alxB8T1HvFya0Orh8bKdaLZadccphH-N1mVcWNQQdQlyoOopm7LrBCdqInhOm9UNDNZm_ndCsYHy9-08mvAMO8l9b4dQPsTFjcrN61DJmn3mA7oX84PYyNNrUfXEc518lzNKcuewNpRvUxblXcB_KwEBPrcRWC7PQalFJq9iGCU8aLi_Zb_K9sSjaChaX1nQf_k3dSVBn44-zUGcpYojh5K_1LhIHvHzZkZAO1Eawdo-yIej07k2_EyVuCsbXFZzRoX7ZKmUwFQ3x4ips-N6Hhx4_OG6syb4jTprQvkyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیستم بانکداری و کریپتو رسما تبدیل به طویله شده</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3985" target="_blank">📅 17:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3984">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/3984" target="_blank">📅 17:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3983">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/3983" target="_blank">📅 17:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3982">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Iwana Proxy_1.0.apk</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/3982" target="_blank">📅 15:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3981">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIwana?</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Iwana Proxy_1.0.apk</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔰
Iwana Proxy v1.0.0
با این اپلیکیشن میتونید به سریعترین پروکسی مناسب اینترنتتون متصل بشید
✅
آدرس گیت هاب پروژه↓ (اگر استارز بزنید و بازخورد بدین اونجا ممنون میشم :))
https://github.com/Iwanian/Iwana-Proxy
مثل همهٔ اپ ها نصب میشه، ولی خب
آموزش نصب ایوانا پروکسی
@I_w_a_n_a</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3981" target="_blank">📅 15:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3977">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">با تشکر همه‌ی بچه‌هایی که PR زدن و مشارکت کردن توی پروژه تا به الآن</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/3977" target="_blank">📅 15:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3975">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bx0lmCxGW5MNs1PCBKQrzwplZW55A9ykgpJUZagOWjOcldnRJ_BjZTsglLZgTmsagQug7WtOc30P16c9YasCfegnZS4tGMuHZbBYW0aKEd5TqvIDMVAPBsM8qGiRgnNNHxJXv3A4pHAzfWI4866GV1khvjnYaGsko_ePbjwGdNcM2K3SulV9JDr6Fs1Sf_GoYTuOzOXQzqgPRSHtZ63VZcivAMpJFAAb0PZtcVLw6hZvilTrDSiPeMHpeZiWaQdHqJJbjh5wYV22dXpcJnCNmXYgh8JHpwllcnj5j7du12vK40_UE4cDeZ2BIfjZPQxhENHYpBwYGlKzy_tYerUPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qUbmD4hQvetWUO05D3zsInQWgIJRtQ4DvSPNAjFiu83OvaFhGXdtXC6PgLNz6yiAabxz-Yh77Q8kvr9gAcJQms0iPWnSloS_z3DhGkij2F6gcdt_ab3e9iIqygGx-65qnXPah8bKpH-17Nt_KBP38dQSCAGNQDN0PRizwicStq_g4G3wEAhrbVhJDRP7xswBy2p1QAlB8W2lcswcyifatg-XpwGm93LhPxx8lvVmzJZ1vz6kEYuDZKXDywmiojqMiSVGMsE8XYbMX1usxa_85nPJ4yTk-BmwEppMOMeGnQ6EwdBfIks1HtUYUe22e3ly_yqlg_9Sj7PCVOhiAr0bIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متوجه شدم که SenPaiScanner تا الان بیش از 60 هزار بار دانلود شده
سایتش رو هم
Samim
معرفی کرد. می‌تونید آمار هر پروژه‌ای که خواستید رو چک کنید:
https://github-release-stats.ghostbyte.dev/</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/3975" target="_blank">📅 15:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3974">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/3974" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3973">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بانک‌های ملت و کشاورزی هم Came to the party</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/3973" target="_blank">📅 13:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3972">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3972" target="_blank">📅 11:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3970">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GrJEUvJshKwJcKP4VB5GP-FTwjxphZ2joQPubT53yZtR8pBj--rQt8ySq7F-Vgw8P-QDGh5cJwCTO33_vPhAtquyXTbtQhM422NrE4i2eHxPnJ68G4nhNj6QbSZCcSW2WDuonWzDXR-cKT8saF36QvFYi52lZS31pG3wgy3T7WVVvWBYWVCyC5JCxqk_jaaFggw2-xRMEpqPrMJYEv0-dqW4lg8yd7Hk_fEyNC2DEPD9k_2sZ_I-vIjRcoGDjN3PzMW-kQ4iEb0nSAmXw1l_Ghr0o6tTZMmxYeaN4YTxk9d3sW-jLSxHDycnBm8CavclMaYzqDeqMsyLzOLh0anggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/um6xV0nLDsxI0DY9uNzx2rTEmZ4GOor309g9bkpQQNnIpAPs90HZZLslyEPz_qcbMcS5IwbcSg0PVp4Vaq3xklyXmIDs68fwLSf_L6j-vmTsbrj8jLI0fJ4nEewo6RbYaVp7vAwc2I-_r0W6NUvenuBPCUUcoNy49hFyXCNHRzui1QDaz4pIclF6SqYt09HWDqtA3F4u2OVoMeSh2BxsmitwPu2v_gm7rIpN9-2p7wBEZfLNNb0tYfrz4bi_2tJc4m9NvakPWKmgyuNHYfJ_srStnJDUyWxHjYFEOEu6FtWCB_EobjvAMhlqTs5LcBXVSPW7P0kuu8cleBHCEDW4EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس اول: یه سیستم که تقریبا همه‌ی گیم‌های پی سی رو بالا میاره با بهترین کیفیت(عکس از
glock saint
)
عکس دوم: لپ تاپ tuf a16 ایسوس که اون هم خیلی از گیم‌ها رو بالا میاره به راحتی.
و طبیعتا با لپ تاپ شما هزارتا کار دیگه می‌تونی بکنی که با Steam OS نمی‌تونی</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3970" target="_blank">📅 21:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3968">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OFswHtIRnuiTWZjnZLL5eMuu97gMyd7MlhEcbMKakF-IXOc4blOGz6yc1p-IVW4r47WHA6QSY7nvNVYluRzoEgaGcfskEH13wzsBHfobhKOQXbAYdAmuEBcplqipv6qHN-NIXs6GL4L4eyWgtCGzkDUTenBYu-DKmrHXLjkw-TmoJKg7_A3KipGwURMPNxOF4Uukg4zQ6w2CKGqL68BAap9FltSgVCJx1yjq5IHKntyxXmO11M1r3yXTXRcqDj4MWgs3iiOVwowi0ksnw76jFUqQwHxNjzsQTqFeyhMhnU3QetrPArtJDxIj-ASnA4KS1RzJ8oHdwckVXp2I52t1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sfYwGMuqxca64eb-Dy3AE2BOuvV_1AQkppqG-WvbKIKdD3jTV7iemzQGFyzy6LxIE5Svxu0I5jxtIUou7znYdF791L275vTbXTaagNuxxcVVpprIqQ7Hx5pfi9Psa-kqKGVX8E9kBv_N8nr-OVmUGcbQodoEJuSZfKTIKvh--q1DvS16kQjrovNfM-szOL9k9iKdbdmIHbG8aF60IO2RqhjtY9cgBXYsKhgwDq7i0ktkVJt32r3f-VG4Sf5NiYR0BdXkwMIaH93Ee1lGmQnxWjqGskB_-bFkiqMgObctd0NR13Cu5wmGfKAHfbaXcEUv5dENDbi9vw59M4mj3vQnjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنسول استیم ماشین معرفی شد، با قیمت پایه ۱۰۰۰ دلار!! تازه دسته هم نداره باید جداگونه حدود ۱۰۰ دلار واسش پول بدین
🤣
تازه پلی‌استیشن ۵ پرو با اون همه دبدبه و کبکبه قیمتش ۹۰۰ دلاره
نسخه معمولی ۵۰۰-۶۰۰ دلار
خب خارجیا می‌تونن با هزار دلار سیستم اولترا خفن ببندن؛ حتی می‌تونن یه لپ تاپ tuf a16 ایسوس بخرن.
چیزی که دیدم، کاربرا هم توی ردیت به شدت ناراضی بودن و انتظار قیمت زیر ۷۰۰(با دسته) داشتن.
میگن که به خاطر قیمت رم و... هست که انقدر گرون عرضه کردن، اما هنوز هم در عجبم از قیمتش</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3968" target="_blank">📅 21:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3967">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه سری آموزش راجب ایجنت‌های کدنویسی قرار بود داشته باشیم به زودی، منتها لپ تاپ لولاش شکست و دادم تعمیر کنن
😳
رسید دستم ضبط می‌کنم</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3967" target="_blank">📅 17:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3966">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from᯽マティ️️ン先輩</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=CWFz3hG8F8hBQcytE67qQg__dtTlI2_LBKj_mMNp1OLte7ihGMJijwQ1xElw45JUJhU2ytkhJFlukLAKenoR5jd8-NWLtVGDXkfgrfDADKOSEQyDLfg4-ZfZReXp_tw2kUqyoLvi5ZKKUE_GMCsaCD92h2dj5789BE44F7CF5juPPd4ox7GAeXE3hHZoAoxsF1mwP08v__ytZfQQRW3yJuCZ-otnewVi8WECw8oN13fZ91AMoD5EaxeoUGsVc5pvIWgHpivpJAx5ibQhxdaUJvNUQueyi5zz83J30yYZErF3vk-4299J2zFMDijxRwbUtcwQRxezXpzR5eLU-GWYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=CWFz3hG8F8hBQcytE67qQg__dtTlI2_LBKj_mMNp1OLte7ihGMJijwQ1xElw45JUJhU2ytkhJFlukLAKenoR5jd8-NWLtVGDXkfgrfDADKOSEQyDLfg4-ZfZReXp_tw2kUqyoLvi5ZKKUE_GMCsaCD92h2dj5789BE44F7CF5juPPd4ox7GAeXE3hHZoAoxsF1mwP08v__ytZfQQRW3yJuCZ-otnewVi8WECw8oN13fZ91AMoD5EaxeoUGsVc5pvIWgHpivpJAx5ibQhxdaUJvNUQueyi5zz83J30yYZErF3vk-4299J2zFMDijxRwbUtcwQRxezXpzR5eLU-GWYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر سعی کرد عملکرد و هزینه‌ی GLM 5.2 Vs. Opus 4.8 رو مقایسه کنه. و با هر دوشون با یه پرامپت یکسان، توی یه فایل Html، یه بازی Backrooms بسازه.
نتیجه‌اش جالب بود. این هم پرامپتیه که استفاده کرده:
Act as a senior game developer. Build a technically impressive Backrooms horror game in a single self-contained HTML file. Embed all CSS and JavaScript, no external libraries. Raycaster (DDA) with textured walls plus floor/ceiling casting, 480x270 internal buffer upscaled with image-rendering: pixelated, infinite 16x16 chunks from value-noise/fBm with a guaranteed open street grid, procedural textures. WASD + mouse look, F flashlight, Esc releases pointer lock. Dynamic fluorescent lighting ON by default (never hard to see), warm yellow fog, vignette/grain/subtle VHS, Web Audio hum + fluorescent whine + footsteps. Psychological horror, dread over jumpscares: footsteps behind you that stop when you turn, lights that flicker then settle, a far silhouette that vanishes, rare spatial anomalies, randomized timers with cooldowns, slow escalation. Save position to localStorage. Return only the complete HTML.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3966" target="_blank">📅 08:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3965">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">امیدوارم جای بهتری باشی الان...</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3965" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3964">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/3964" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3963">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:  https://yout…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3963" target="_blank">📅 20:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3962">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:
https://youtu.be/CPrePbvbbic</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3962" target="_blank">📅 20:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3961">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W44r76YpkY_e3qMji3b9QVqxXc_Sk6G0Qe3AtS28oIAzwtFpn1uYQ72Fwv3-zxHyMdpfA6az18ijukwApYaMgQ45LmJYYnEAH3yKQtEDi19e79rRYGSSEd1gFEUNXEIaC4UNmiw3DDnI0ij5UKi2n61vb2bqQQRHVdhuw2KBJDyjCsuwIJWbkcGAC9r6TIoCVwRzZmP4bjFNmSWrx8K2Ge7PJvzbpyJsxhtuUQcyC5eutAVaA415SApJs2W_rY97kNh_ztkcb-VHLzyLncdkSJTgA_CV4LFpQvkvYpxrA6QFvR8wImSQf9zBWISdH9B82KK-0APhmg7UssTX1i_-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
نسخه‌ ۲.۲.۱ BPB Wizard منتشر شد.
۱. قابلیت اضافه کردن چند اکانت کلادفلر به Wizard اضافه شد. این قابلیت برای بچه‌هایی که اهدا میکنن و تعداد زیادی اکانت دارن خیلی کاربردیه.
۲. اسکریپت نصب خودکار برای macOS هم از این به بعد قابل استفاده هست.
✍️
بیا پایین بچه
آموزش استفاده از ویزارد رو قبلا ضبط کردم:
https://youtu.be/uCRKnrQEQYU</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3961" target="_blank">📅 14:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3960">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا...
پروژه نهان که قبلا متین معرفی کرد رو محصول داداشم دکی واسه دسترسی رایگان به اینترنت آزاد با روش ورکر رو بلدید دیگه؟
حالا میشه آسون تر حتی واسه کسایی که مبتدی و هیچ ایده ای ندارن هم ساخت با کمک ربات:
@itsyebekhebot
شما وارد ربات میشید ساخت پنل نهان رو میزنید وارد سایت کلودفلر میشید و طبق راهنمای کامل پیش میرید و ظرف دودقیقه حتی کمتر با کمترین اطلاع و دانش از ورکر یا هر چیز سخت دیگه ای فیلترشکن رایگان خودتون رو بسازید به صورت رایگان
❗️
نکته:از بات ایمیل فیک هم داخل کلودفلر میتونید استفاده کنید:
@TempMail_org_bot
هر جا هم گیر کردید بهتره که به من پیم بدید
😆
آموزش ساخت پنل نهان
@yebekhe
👑
@xsparvin
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/3960" target="_blank">📅 12:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3959">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">اگه میخواین بدون VPN، به سایت
x.com
(یا توییتر سابق) دسترسی پیدا کنید، کافیه این گام‌ها رو طی کنید:
1️⃣
وارد این مسیر بشید:
C:\\Windows\\System32\\drivers\\etc
2️⃣
فایل
hosts
رو با Notepad باز کنید
3️⃣
انتهای فایل، این خطوط رو اضافه کنید:
104.19.229.21 abs.twimg.com
104.19.229.21 x.com
104.19.229.21 ads-api.x.com
104.19.229.21 pbs.twimg.com
104.19.229.21 api.x.com
میتونید بجای استفاده از 104.19.229.21، هر IP مربوط به cloudflare که تمیز هست، استفاده کنید
4️⃣
فایل رو ذخیره کنید
5️⃣
مرورگرهاتون رو ببندید و دوباره باز کنید و
x.com
رو جستجو کنید (بسته شرایط اینترنت‌تون، ممکنه مجبور بشید که چند بار صفحه رو reload کنید
⚠️
توجه داشته باشید که در این روش، ممکنه
x.com
(یا توییتر سابق)، شما رو با IP خودتون شناسایی کنه، چون که شما بدون سرور واسطه ممکنه متصل بشید (به
این دلیل
از کلمه‌ی "ممکنه" استفاده کردم).</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3959" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3958">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وقتی اینترنت گوشی رو Share کرده بودم برای لپ تاپ، بدون VPN، بهم آپلود 0.02 مگابیت میداد. اما همین رو وقتی با کابل و PdaNet+ اینترنتش رو share کردم، سرعتش شد 2 مگابیت. یعنی صد برابر
امتحان کنید شما هم، شاید همین اتفاق واستون افتاده باشه</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/3958" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3957">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rp-82dwr1qGB0CoHodyZ-PMJEJ8GtUQ2W9-EHciVT2r7U_LQvaHScdZCPzU8Uoy-1FkMlCSPiqCpJm4WTcrRflFG-8ROL_onCzv_zzIz4VbyNfSDBwcvm-wuCVsFzEXnPwYp4qTAHe1C9hqxrTXViKPOsl8zYE7sGuumg3z-8SligXSElzaeZmmVcpVGnbOXD7vHfqBfLo5GupYAqIPbWJrhPv-Mvs5HpL7U4p3BSmTnNybYOC1Lv51R5zenZaPDXu2ivKJAR3p5j9HNiLQpzGmfsii-MiovHN5NhmRkQKdjI3rN6KScvHTR9ogFRqPTEJWHPe60H3cbDGX-8qo_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل در حال آماده‌سازی یک «ارتقای مغزی» بزرگ برای هوش مصنوعی خود است.
تصور کنید یک کارمند بسیار باهوش دارید که گاهی در کارهای طولانی «تنبلی» می‌کند یا برخی جزئیات تصویری را خوب نمی‌بیند؛ حالا نسخه 3.5 قرار است مثل یک متخصص ارشد عمل کند که نه تنها چشمان تیزبینی دارد (درک بصری قوی)، بلکه می‌تواند مستقیماً نقشه‌های مهندسی و کدهای ظاهری وب‌سایت (SVG) را طراحی کند. این ابزار برای کسانی که می‌خواهند از یک ایده خام به یک محصول دیجیتال واقعی برسند، حیاتی است. اهمیت آن در این است که فاصله بین «فکر کردن» و «ساختن» را به حداقل می‌رساند، هرچند که احتمالاً برای این هوشِ برتر، باید هزینه بیشتری بپردازید و با قوانین سخت‌گیرانه‌تری (فیلترهای امنیتی) کنار بیایید.
نشانه‌های فنی در زیرساخت‌های گوگل تایید می‌کند که Gemini 3.5 Pro در یک قدمی عرضه جهانی قرار دارد.
این مدل که به عنوان پاسخی به نیاز بازار برای «هوش عملیاتی» شناخته می‌شود، بر سه محور اصلی متمرکز است:
تقویت بینایی ماشین
استدلال چندوجهی (درک همزمان متن، تصویر و صوت)
جهش در تولید کدهای گرافیکی مانند SVG (فرمت برداری برای طراحی وب)
گوگل در این نسخه، «دقت جراحی» را جایگزین «تنبلی مدل» (تمایل هوش مصنوعی به کوتاه کردن پاسخ‌ها در وظایف طولانی) کرده است.
با این حال، این پیشرفت بدون هزینه نیست؛ گزارش‌ها حاکی از آن است که کاربران با یک «قیمت گزاف» روبرو خواهند شد که این ابزار را از دسترس عموم به سمت بخش‌های تخصصی سوق می‌دهد.
همچنین، اعمال فیلترهای محتوایی شدیدتر، نشان‌دهنده هراس گوگل از سوءاستفاده‌های احتمالی است. در واقع، گوگل در حال بومی‌سازی مفهوم «شاگرد اولِ سخت‌گیر» در دنیای سیلیکون است؛ مدلی که همه چیز را می‌بیند و می‌سازد، اما تنها در چارچوبی که معمارانش تعیین کرده‌اند و با هزینه‌ای که هر کسی توان پرداختش را ندارد.
✍️
Gratomic AI Bot</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3957" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3956">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کافیه یه آیپی تمیز بذارید توی بخش Advanced, ip fronting
زیر ۲ ثانیه کانکت میشه</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3956" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3955">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3955" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3950">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3950" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3949">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJWhru6sLM9XfgyQFiWRGZMvDbjhkkohQPhRc4XYM2DRYkibjtoudghVGwRydIvW4rMnqO4HdRJ_dtKGjJoI5CHFGPGeSu52bbFENzpbxEh58R5QzWSUXF9VAmr4HG3BDGUtZTB4W5I8trqOBLEQMp9VZ8QHV8H9tE2Z9z5XrYyDHgijE2h2i4JtpOk5ctKYndiAk022b3yjtrD9rkL5G6oLtmZUDvmuF1PZXq7K9MUTKFGQIjmjhzoQaLvzYmk5UiaWbXgAI-ZpMlSmmKkUkE3W4LeTdczBWbAfsCCv4j8piS_a2DAic1OoRgAozbI4sYnEmKNiehqyGRdNLhes5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه
• ظاهر اپلیکیشن تغییر کرده
• امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.
• پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.
• با کمک یکی از بچه های گروه، یکسری از مشکلات امنیتی اپلیکین رفع شده.
💬
اگر براتون وصل نمیشه، فقط و فقط مشکل از شبکه شما هستش. آی پی تمیز پیدا کنید و داخل فیلد IP Fronting قرار بدید و براتون کار میوفته.
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/3949" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3948">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3948" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3947">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q1qQd7f_8LXsdTkklkMJYTYdBnjRQy10uaBeYgW8_nSkAIbw7P5fpTLfE5m1DwSTjKQHD7eFIJoYyYDjy3zMoT8opMPIPATajU6bLH_YRbcRr4sRelIDIUAlcwJ0U6R_lSgRwzI_GiyyJpFBND3efjtvv64RD4cdmrX9di6Qkk_MSj1QAOQS04GScfufvPS1zQPXgFXtj8-pcB4rA_ouKw9w722zMXbuSfKUxYzJE-3wHzY3kERApM2pXav0dG7jM6SUUrMQ2p_cfOv5McXQ6jrrHp4vrrtJdMcI4RctUaStmstjN8rWCpvT0m4n-hm4suYqXYFB8qUr-qeSLRgW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3947" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">✍️
دوستان برای جلوگیری از هرگونه سردرگمی، ما در حال حاضر سه اپلیکیشن مختلف داریم:
🛡
۱. WhiteDNS Application
این اپلیکیشن بر پایه‌ی MasterDNS ساخته شده و مخصوص زمان‌هایی است که فیلترینگ و اختلالات اینترنت خیلی شدید می‌شود.
در شرایط عادی فعلاً کاربرد خاصی برای استفاده روزمره ندارد.
🛡
۲. WhiteDNS VPN
این یک اپلیکیشن ساده‌ی VPN برای کاربران اندروید است.
اگر فقط می‌خواهید راحت وصل شوید، این گزینه برای شماست.
🛡
۳. WhiteDNS BPB
این اپلیکیشن برای ساخت و راه‌اندازی BPB روی گوشی اندروید است.
یعنی بیشتر برای کسانی است که می‌خواهند خودشان یک پنل BPB بسازند و مدیریت کنند.
🛡
۴. WhiteDNS Installer Bot
آیدی بات:
@WhiteDNS_installer_bot
در این بات می‌توانید کارهای زیر را انجام دهید:
• نصب MasterDNS Server
• دریافت لیست IPهای سفید Cloudflare
• دریافت کانفیگ رایگان VLESS
• تبدیل کانفیگ‌های خودتان به کانفیگ‌هایی که پشت IPهای سفید Cloudflare قرار می‌گیرند
🛡
۵. WhiteDNS Installer Wizard
لینک گیت‌هاب:
https://github.com/iampedii/WhiteDNS-Wizard
این ابزار برای کانفیگ خودکار سرور شخصی شما استفاده می‌شود.
با استفاده از آن می‌توانید سرور خودتان را همراه با پنل شخصی 3X-UI راه‌اندازی و تنظیم کنید.
❤️
یک نکته مهم:
اینکه اسم برند ما WhiteDNS است، به این معنی نیست که همه‌ی سرویس‌ها و اپلیکیشن‌هایی که می‌سازیم حتماً بر پایه DNS هستند.
ما از اسم WhiteDNS به عنوان نام برند استفاده می‌کنیم، اما راهکارهایی که ارائه می‌دهیم می‌توانند VPN، BPB، MasterDNS یا تکنولوژی‌های دیگر باشند.
@WhiteDNS
🌎</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WWtQgXxqdgTbDK5T_RgNbA9yf6KTuXbBD0tU3z8_FDC6RPNOh8cDQrRbsviFuZHuCigXJBzBWQPoQ9AVjiY16h0zeKnfOd0qc7EURaw72c-iLQfpELkaOLkYfIwG8eMc3I2viePXEtscy2iDWk2oMx2MJtAMFBsU-8dLhY8U38KrCuWdUrOHqsvj_-Xa91ydw0z7-JH1fNaF2TO02kwJ27oMEY5GAP8nvzWdkiXQg8LGKuVuFffBl-hOkqGRuppUOgLsggfjGT_xuyFPWp8hAQ8BoKr0TjU1RPLwFCwjMSEEe6jV77wtExOhMTg531vN5Hv0uCap4I4vyHtY8ABUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OodBJN4PRbmCqjPhKSsdZ2kZyvTRbOxJFM1uk_r7GjP7kHHuZBFumWcyPYu_ydvZyNMWBCnGg0CgKmwoNfEtWoEBSH3dl7KGUcFZVnCpgHMvYMoXy14OwiQXOrZX2xIPu48psBXtVYKxk_VDwkuPXaVbw8hKHwWZ8MCB0MpD8OafvioTvwKCsSKuBzA9EberPDM9teLZRS3ek5cxB4qUh2vbskf4LalUw-Yz9mYGaBsvBxf5VqAw_wExdIxJl9zKz7JV64qO6x2OPriMQnWDrvVizwzItVA-4bj25q1W8-IPw0RuBxVgF0Di5nUSTHGoz8CvM5wDe4YD7GjsdgfeNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3943">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز
❤️
در چند روز گذشته متوجه شدیم که بعضی افراد و کانال‌ها، به جای همکاری و ساختن، مسیر تخریب و سوءاستفاده را انتخاب کرده‌اند.
این افراد که ظاهراً در فضای اینترنت آزاد و کانال‌های مشابه فعالیت می‌کنند، برای جذب مخاطب بیشتر حاضرند هر کاری انجام دهند؛ حتی اگر نتیجه‌ی کارشان آسیب‌زدن به پروژه‌هایی باشد که با زحمت و هدف کمک به کاربران ساخته شده‌اند.
چند روز پیش اپلیکیشن WhiteDNS VPN را معرفی کردیم؛ اپلیکیشنی که هدفش این است کاربران بدون نیاز به تنظیمات پیچیده، فقط با زدن یک دکمه به بهترین کانفیگ‌های آماده و تست‌شده‌ی ما وصل شوند.
اما متأسفانه برخی کانال‌ها شروع کرده‌اند به استخراج کانفیگ‌های داخل اپلیکیشن و انتشار آن‌ها خارج از برنامه.
دوست عزیز، اگر مسئله فقط بستن مسیر دسترسی شما بود، ما ده‌ها راه برای رمزنگاری، تغییر مدل درخواست‌ها و محدود کردن این رفتارها بلد بودیم. اما شرایط اینترنت آزاد و محدودیت‌هایی که کاربران با آن درگیرند باعث شده ما تا حد ممکن ساده، باز و قابل استفاده طراحی کنیم.
مشکل اینجاست که همین رفتارهای مخرب در گذشته به پروژه‌های خوب و ارزشمندی مثل Slipnet ضربه زد. وقتی هر ابزار مفیدی به جای حمایت، هدف استخراج، کپی و سوءاستفاده قرار بگیرد، در نهایت انگیزه و امکان ادامه دادن از بین می‌رود.
واقعاً هدف چیست؟ آن کانفیگی که با زحمت استخراج می‌کنید، همان چیزی است که بخش زیادی از آن در لینک‌های ساب ما هم وجود دارد. چیزی که روزانه هزاران نفر را متصل نگه می‌دارد فقط یک لیست کانفیگ نیست؛ پشت آن اسکنرها، تست سرعت، بررسی مداوم، فیلتر کردن کانفیگ‌های خراب و یک سیستم کامل قرار دارد.
ما این ابزارها را در مدت کوتاهی، با انرژی و فشار زیاد ساختیم تا به کاربران کمک کنیم. لطفاً به جای تخریب، کپی‌برداری و گرفتن انگیزه‌ی تیم، سازنده باشید.
ما از نقد، همکاری و حتی پیشنهادهای جدی استقبال می‌کنیم؛ اما سوءاستفاده از ابزارهایی که برای کمک عمومی ساخته شده‌اند، نه کمکی به اینترنت آزاد می‌کند و نه به کاربران.
اجازه بدهید این مسیر ادامه پیدا کند.
✍️
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3941">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">تیم داشته باشم، دوست دارم از خودِ شما کمک بگیرم. اگر دانشجو یا دانش‌آموز هستید و مهارت ترجمه دارید، این می‌تواند یک
کار نیمه‌وقت منعطف
برای شما باشد تا در ازای کمک به ترجمه و ادیت، درآمد کسب کنید. آیا این مدل همکاری برایتان جذاب است؟
هدف من این است:
سریع‌تر به محتوای آموزشی مورد نظرتان برسید.
هزینه‌ها برای هر نفر ناچیز باشد (پول یک قهوه!).
بالاترین کیفیتِ ممکن (ترجمه انسانی) را تحویل بگیرید.
یک زنجیره همکاری برای دوستانی که دنبال کار نیمه‌وقت هستند ایجاد کنیم.
هر پیشنهادی در مورد نحوه قیمت‌گذاری، فرمت‌ها و اجرای بهتر دارید، در کامنت‌ها بنویسید.
من تک‌تک نظرات شما را می‌خوانم تا بهترین مدل را برای شروع استارت بزنیم.
این فرصتی است که با هم یک کتابخانه آموزشیِ قدرتمند بسازیم!</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxsmvqTs-OaBJXUlGnngWIOBFRQxlJ7538EF_E1HpyOqGHsTqBrNz5TRvsCw_yrxTkoGzZhQwMUaVnLiIC5BU4uFVeP2ybfJZfbrDtOFOwyLa1ZvhGY-HvTmYe1tftVRcoSONlyQufdQoTvwsyLf-4e61o5rf_gia1doVwJxjCuRDtXpUGX6-m-BJSVpY0zmBbJJeMK9mgZzouFVuh9ocRv1GvULk7gKQX6JMl3riNaNDuhIYkrhQHx1ZjQqaBQA5K3YCDZqFFhNX8jvnJi4GOxKK9GBbAkbeYdbtSGXMf3F3WirJdHNEpVe1Ohnzwu4ARp3vPvEEoTy11U_pJ7eZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی، یک پیشنهاد ویژه برای دسترسی بهتر به محتوای آموزشی!
همان‌طور که می‌دانید، درخواست برای ترجمه و زیرنویس کردن ویدیوهای یوتیوب، یودمی و کورسرا زیاد است. از آنجایی که کیفیت و دقت برای من خط قرمز است، فرآیند آماده‌سازی ویدیوها (ساخت زیرنویس، ترجمه دقیق و ادیت) بسیار زمان‌بر است.
برای حل این چالش، قصد دارم یک
«کانال مستقل»
برای مدیریت درخواست‌های شما راه‌اندازی کنم تا با مدل
«مشارکت جمعی» (Crowdfunding)
، ویدیوها را به صورت عمومی و با کیفیت بالا آماده کنیم. در این مدل، به جای اینکه یک نفر هزینه کامل را بدهد، با مشارکت چند نفر، ویدیو برای همه آزاد می‌شود.
اما قبل از شروع، می‌خواهم «شما» تصمیم‌گیرنده باشید.
برای اینکه این سیستم عادلانه و دقیق باشد، دوست دارم در مورد جزئیات زیر در کامنت‌ها با هم صحبت کنیم:
مدل هزینه‌کرد:
به نظرتان چه مبلغی برای «مشارکت جمعی» منطقی است؟ (پیشنهاد شما برای ویدیوهای زیر یک ساعت و بالای یک ساعت چیست؟)
فرمت خروجی:
ترجیح می‌دهید فایل زیرنویس (SRT) را جداگانه دریافت کنید یا ویدیویِ چسبیده شده (Hardsub) که آماده پخش است؟
یک فرصت برای شما:
اگر تعداد درخواست‌ها زیاد شود و نیاز به</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LYkPO31Dl-Da7NDACGYxjyvWEw-pR6CtzRTqQXSLEoY6fVXdwIJinNIX-RaoBX8osXGsjYFUchef92Zb9b3fgGsXhCSJgdn2v0iJauWHUXQtzWol7Wsn6_matjjoBqr2RYn62hCGmza4N0ekhY3xk9YQWrSg-I1CJ0RJTZgMyez8Fvsy0KEBkpIneI97NwS6J2556pxZMI7N6o6V-vuHkertfj3nMc1hp5OpWlIBquHJPk5VMjI_IuCCzxN9l9G1P1lnWcXev9h-htfN_fQxq0_2_YGFWMVZ9nsUtS6iKQQxR7hSqxkZZaNW0yIqRp6FKnxWUYqWlhgZhT931aj3ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uek92Bbpt2lDJT4TjJPMmggojwTh2aOqvqGqn-Neh3x7HMK9eObHSkxLxBkDDFctdZlKrbvL8qxSUqozNaJfieMTYQbswW3dXYioZxGyw1XDYSUezNfVYnGdT9OOzvAZUDg6ECJxrEU2XQj4rIo09B36wpGc2GfRQAovPKMp8D6_eBGyhz9_FgMNaL7bgsyeWt4MXPXdx2w1J73gEGAhy-5tg_WKByYS0i4dRuw3OKY5yAuRBJJEmU4VWdcEgSJQ00KFWRRZuGTb1MMDs3Ze6WZQyvqE8448XSzU9txe6sIUYNby4sor5RIT908coWN6eMBSlb2Grui-n5TFFWCahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
بدون دانش برنامه‌نویسی و کاملا رایگان، اپلیکیشن اندروید بساز! (فعلا اپلیکیشن ساده
😁
)
⚡️
لینک‌های استفاده شده توی ویدئو:
1- خود AiStudio گوگل:
https://aistudio.google.com
2- پرامپت ساز ریک:
https://chatgpt.com/g/g-6a319e2a22648191836468df375a3763-prmpt-sz-ndrwyd
⭐️
توی این ویدئو:
1- بهتون نشون میدم که چطوری می‌تونید از یه پرامپت ساده، یه اپلیکیشن ساده با تم دلخواه تحویل بگیرید
📲
2- توی مرورگر، Emulator اندروید بالا میاریم و با اپلیکیشنمون کار می‌کنیم
🏆
3- و در نهایت، اپلیکیشن رو مستقیم روی گوشیمون نصب می‌کنیم!
📱
🤎
اسپانسر ویدئو:
خانه EB، خیریه حمایت از کودکان مبتلا به ای‌بی و بیماران پروانه‌ای:
https://ebhome.ngo
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kTdcAzRZUBtw3uPVNpmT5wt8dj2DiOm96gVvS8wX2t9Jaqt5Rqs-a_mUniUXG9dD-ad21k03-76y0RWmStNApHU5lgaymIVNt_gUgCEEU5ys9CvFrvFHdRdueBLF-g2jctQyMOPVIm1CgjG9KKJriWG7t3zkk8hnLhbquhy_ZCKk8vPN-s1mpOecpthDDk6B7FHhkamfXq-5dNYeiHR1ECLGrhuOk4T_n5f_koLq152QAqGlzHVJ2VSLTm1b6QePSm1uoF8ZbMVhZ0O3ay8-cjNwHkWZckKuCSZGZIHBjCAvlNiuRZbnctwjkLFSuKPJu9NIlZK9_stJLR4zIeLIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DvWcNxiML1koOLRVHs3ZVqlsCEoMxCvhvTP4pqfYKqh7txvl0Y5DnjhS2ziTAAXK-fmnHFHlPJUXzD9ctUATbVOvTPOUzJueYvlAdq7J5Ijvo2ujMvBSQCRtgoWGJC82c43WFqF_hu1QbbGs1tZL3yhk1Rpv6BcWEEaSNz6-EgJ6Z7VHno7zkoqm1ucXgt_p6z9JDkfKCZjyb8Hjx_V4_P14u-B_s3eOQBFljSmoSnzxmLZWKuxEZXmtHLqlguqQjJfb9gnbu9ajDtv3xHElorMFy2Rgknk5d7VDu3rCXd64Sl8yTmcrQJ33YPY1kbavvVm5g6Lps6iVU9P5HMRQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z7bQ7hWWi1Eo_y2pQ9BRYTT3sbKqiC02lGLGvXLF4CP86OZWuWD4NpMI_SROlYh5DdUTci_FpvCAczbY1oXgBq6-QxWbIESTPHJ1u6INu5cLnZGxUgHaFW8HjWS6l3UZhIcOmXZhEevOq8tc5md0GNxlZl6xgoCk9qdaaLnU9Q29eojp8ixEq4ZngKXbWoSyKdZkQP5nEJkUjK4a_Na5oW5N0W9XJX26gZHIqt7rsh_kaR7XpTz_1xOHVS2u-GL6YU07B7h_x1iA8OX5nUmtKr51uQUJ5aLGIMu-ufEZUslrJiEbK8XQjVoHzqc4TbdCY0ic7LdR-VsGELaXZsPZHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3926">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W7VfGjvz7DCNDPmrbGCffuCJdM-wYfaPlp_bZIouzoZkQ-FvZOQNSroIxr9224-_j0xq3y18a78xhNHfB0rz0cwwbTBDTzFO9-W8fhEUkjMHwTWHq1od1jbH3wF5TCiwHy-NKeCeIbyWWJh4eh73g8bU16UsaOy3d3NHetNL_kHDsaUbntmoRay3E7Nzjp5xynZO9tqf3a-b6hawpIjYZckOL9uqXK6X_yG0D09qVuu5ZMGmIw0Slv6WazHWFzNvKofKsxk13-Id0dm9EEfc_kiiAA_EGcxAIJth02zrFKK9h4P8_fZtzhFeHYEs8gfotyLdcp7LLnkBePU--euJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/huFC1Jk4c0uXuK7lCto1lDRRqj9cluEGVUt-RSSlopPbGBqHjfvCaedESoRFJyHWRmPNJ5p8Zz0pWYXOWpKrA9xMFvSsaEHV9RdjMy6TpkGn4Dhpr6gmNYhGrUahdujjCcoADwWdoG9Wz4rkPKnWG56xF1UWbuaouCm_KIiG9d0bzJ4iLPwSoUDF7rjHRBE5P1pjigJGHVeM7ATotvZkuqgYZff13MCqmndp5dPugKpA04tT4PVkwztOwsgC6WUtSrUVOWCPJcU40oW42zKaspsKSIVRFCvsXRKCEi9VyrEHabKDhVWlHJGX03inNZLZcDTwirt4-rSTNTsWarH3_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s96eiISeXYOt18Q0bQ5lI9i54GrzoVo7zixv8fswo8X-bMdhn-LK52Ws8jJG22SMwBGBocMZ8f2kIrbTs0lztdogkC994sZkZINF72NK_6dSZxtLag969cjH0VF8NnMO4aPkyk43QgVKc5G_HNdLqw3ro-WnIRRrlzoAd7I4FnKUQX2Mu2LbV909OW7dp7jzjGl9nfSxmMqIPc2N3Cu9-MBDICg2y8eJwT0bvELKp3BYrbV1omdi_z57gxscPrXlabuK8nY_XZr-84pEZsztWolhUR0YIquylvRBIq74NNxmwBwDIpmHpV9SWC87rOLvm794h1HnGrRqoS9PQ2dfZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQ7jr5fOTvmdi9C8SnqtQUaBsp1hOrnLgFmOS3i7AojDKExsxgxEwXASsyQGKczJcBlGzw_-w7CBI57Ni4dEyuyFJ6b2B9yhQPVKALI4oFYnOzntQKRBhhx-LPE75v9a0W5PscIcweq9qivEwclEZzbg1hy47_EIxXkoNYUpfGA4wOUh2i2T0rib1U8YtR5bW1g9di1PtWxHDgZOWcEeGOx_z4Uxwn3UA_zCeNkMraAXsz4nn3NcAf95FAnRGCcrHpa3zEu7r3qKQFPPFHHXzlJJg8JzrJhqMm3ndg62zcVth-Y6uKd0MyO0zDHres8LgiLPBcITBTu2ov_70lvDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtfyromWsDt1wsvR4Jcl-gX-BCLSAy8hpEB_elzOD2eAjDWHgIObhla4UCqR51AOpq3j2WZD1kHKMnQOoCEim1KoaTa9NzWjKJgUB0xxmkiM4l9n4skJ5tEf89pbdZNq65zBfomQK9SnttcvP4dMpbQ9DirLGupCgqQ_nsMEmfwvUjAT29njtV8vkF90lH0AygMDfQIXMzDilOvTzfjhShHd7COPO2nQR1FeaRmUmdMQfUtD9WJw7i4sFOTF7FfPzY6VeDuwoC0go2jd3SCl_o8CRSiylSsrMViV0xKTIUFLRwkNmDJ5eKJsL03taXdiTNRRiXWDI0PgjRJIeTawXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iuNpZ81zbr5Ek83NppOkmhl3b5C3heYSWzDlgRzEr6ARYiHxPfwZMhliLMmNw7eG7uOF49S1VCGXBGR2YZatUOeWfbQSw0gcBvoRb5g9GMOd2bXQvm1Np7djQoTLFbbtSLscND6P1VQcAFBt5aXBwmck4zaEVA2C0qVhiyt9grFI7GJdN8ratyRfANnBMWnMigCaMJPNTYQsLAraLuZLaw5WwU3RhaTWpDGZC1C3HpMwt0E-mkgZkY0FwojBqx0-jKi5zwLYtefPt1MQEe1Y-Pj_85ZNC5-TQ-28VpDDkcfSMLM2RQCgb3W2Bhp4Ef7UohZtFs0otsJLkXjGdJkIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaIdTblUgZ7xypSNWcLfD_Nnv0G0FY_tDVcQ7EWle3YQvuRzdmtYbS29oSStlrl8mCfl6W5JevK-mWBQQB9OWXAkQw1-6zaXdYg9zNOn0mB5LvNC-C7X4X1dm6wq2JowMbPtlWV5xGYIApbGbPSTmj60BC38DHaew5P2io7bmJi9mZaZEJJcPcxmCGWJCmiBywCtXZP8soxS-3X_0b6lchgvXcNCSlVZyMDHjnSfrZe2yHCf-oXUvab6DNpxAPL8yL1hyCkpjDU7jBXQEtEfrS1buPHe7Uk8L-nj4RecQpBpb-uH0ATQc1mZcU-93FgZN9PDFlx4dY1KJHENxG47wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vl5ubumEeAP-CHhp3HOQYTiFx3_gW-fskzqxJb1ZLWi3hMJIIbWpYU3QYT94R3L6DyKHODlfpZ_foAKEh-TIaW6FGbeH7qn6ZqT9ZQLlLCy_YIQoVnu8D8ykoXecVpIlAE3m_8R5Fcoe8vWfih_kmNLF_GAJ4G094dA_Z1kbCvs2WZONWq1f_8aH0l1uifeftTyjHcqlyTiTLa1vVMf25Hmt8LeG_EAFX16uQfL48WQZj-RmnON4FtBcF6X1QCT-vxcHF_6bVo7wUFPh3-fgqyhv60GkrRTCNA5X11u9ix0t547eg4dLXDemXDJ3-RcNaE0cQ1D0gKkp7-2f8sWdqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی نهان:
https://github.com/itsyebekhe/nahan
لینک اسکنر:
https://github.com/MatinSenPai/SenPaiScanner
لینک ربات ProxyIP یـ‌بـ‌خـ:
t.me/nahanproxyipbot
لینک ویدئوی اندروید:
https://youtu.be/2otJfXgNWCM
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل نهان
2- اتصال به ربات تلگرام و api کلودفلر
3- ساخت کاربر و مدیریتشون
4- رفع مشکل وارد نشدن ساب در  V2rayNG و ارور 1031 و 1101
5- اسکن آیپی تمیز با اسکنر SenPaiScanner
6- پیدا کردن و تنظیم ProxyIP بر اساس کشور یا بر اساس سرعت اتصال(توی ویدئو نشون دادم چقدر سرعتم بالا رفت برای دانلود)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از
YeBeKHe
عزیز
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(نسخه باکیفیت‌تر)
💰
دونیت</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی نسخه اولیه WhiteDNS BPB
نسخه اولیه اپلیکیشن WhiteDNS BPB منتشر شد.
این برنامه برای کسانی ساخته شده که می‌خواهند پنل BPB خودشان را راحت‌تر روی Cloudflare راه‌اندازی و مدیریت کنند، بدون اینکه لازم باشد همه مراحل را دستی و پیچیده انجام بدهند.
با این اپ می‌توانید:
✅
به حساب Cloudflare خود وصل شوید
✅
پنل BPB جدید بسازید
✅
پنل‌های ساخته‌شده را داخل خود اپ ببینید و مدیریت کنید
✅
پنل BPB را با مرورگر داخلی اپ باز کنید
✅
لینک‌های سابسکریپشن مختلف پنل را ببینید
✅
سابسکریپشن‌ها را کپی یا مستقیم وارد بخش VPN کنید
✅
کانفیگ‌ها را تست کنید
✅
از داخل اپ به VPN وصل شوید
✅
لاگ‌ها و وضعیت اتصال را بررسی کنید
در این نسخه تلاش شده همه چیز ساده و مرحله‌به‌مرحله باشد؛ از اتصال Cloudflare گرفته تا ساخت پنل، گرفتن سابسکریپشن و اتصال VPN.
اپلیکیشن هنوز در نسخه اولیه است، پس ممکن است در بعضی دستگاه‌ها یا شرایط خاص نیاز به بهبود داشته باشد. اگر مشکلی دیدید یا پیشنهادی داشتید، خوشحال می‌شویم گزارش کنید تا نسخه‌های بعدی بهتر و کامل‌تر شوند.
WhiteDNS BPB v1.0.0
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HchccK5zt3nY-KizhUgxycNsji0nXkXdA9WOorEHzQ4-Y6AWUjZmOnC9IOehM5mxmbWSqw486xIxAjvA_1tmxYQILturvvxSLdq7OxxTTXWHGu-4C3eYFctcQckO4D6dW8SLeUD5rKwX10edGPNmalu5HpirBo835yaE0nSVwutDlvBoA5xlWqvCP8Rr7boZTqu_pm0R_9RjLsfSWna3ngXJ5sIalvBbYrnHKwPeizbaxD5lZtCpZYp5V3gmnUYG1BVcDOq0O5EO3zN3Z8F6tTUKtrYtJgvLQvmA_JF6zzVJIe6SznTIzxuOEYPy6KRrwtMOO5-ZAHl5cXMu2_rR0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ra2l_o1BsGMT7otfu2gLLi9uK2x9eTPh6U1tqOXxXV-p202Q3W_UxcBh7WegPqOiPMp9EOdJgpa6Xenfh0l2qoUkbFjN3a78yn9fgRoyxWHw39xCF0a_6Dl9zLa4gk6_BNmsTeLcwF9DY8turR4tQemfs2ILRpNWQTUBFssYTgbyVbBHMDhCrY2lc4e7U-N-wJYHicSb5WN90YPPqi2f265G4rdjW2ZuYoRWLPfKqvFECKxQ_HkqqbQN11EuR2ir1w5eHvW06BEgRLQ2BMntoteruWcPzsGyyM-FV7JAi2c2P5l80fPHj3vslHznhBQjytFhRUfYgSQAjDQLj1bRTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jzt1Kb6iT7IeS0YQGxLX6bJGuIZTnWb7OX-Cly01dIQfIk7XQH2h6uQRku9Nui5lUQus6lSr6B5RryhtIM7nX_-SZSnyV_Szr9o2BONjOueVZy_Zj3VkBs2s1vK-QefY1p0LEeQWf56xF6ioTddwV6rpbNaJIjUCybwk5_04RER3T1mNeBlq7ECr2AlO1wxwmKeSNNkm2rb1FuYtCcZjTJfKJYw8az_kkLmLiRHNnWF_z__gcrzpaAtF86bkdFcyzcEdfgFxIR2Cj5ESeFCGKl93rfph3Dczcr9AYnJz--qYzFXLuYbINhkOSSNleSVlOmGBZP2NV4OTmRbALor3jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uh3E8CXQ1frX9t5hP8PzdATJ_lc2jSEkKynKushIObQOwVzU-FTmyrRcQ3Bpugiabet8HdBf6KSxOuQ8DdbZ6b3PKOXeNCd9OIihW1k92XTEuojRegkwlkx_DYRCu2AMsvMuFVyoDb-Rmw6FN6Q5BDT6x7oaC45ZyNehfi-0s8xERKRJlcXS4gbF_XH2G3kpJVKZFlRnpPA1pUSIhQtZo813kKpX6uoBQISfNAwtVFmr18U7noz-QyvkHWNY69Mg5OibTenpZbDMV5wN5K6roZX04h0PLvLvMQ61PQnal3692UmKLoqXM9J81i-H4BniSKow_3T0GqTX75PFQpLBxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FAjKfxe9sFYmegynA_4eJIfLpVd70svMHdRrF9q0Ji8ICihWXKCwODe8Mxhgzj4p1f-BN_ayt6-i5XNtytgMGJw-0Nyity5CvmbSpCkTpa__2qGThepwGRfd4SAWhL9La-8W9lYF5xvqxquT_kwEQ5OHzSzvb1cnlcqSbWrKogxzfClFqd2JvpdhFWARRCmrkDkbecPi_nqL9jWPw9MeDRMe7t1coB0OmBiWJQisELcTHy_Eu4uU2epkILAqJgLQvv-0npR2ePCaJ2C_hqRm3P0ER3s2oqT9Sta56-DRNakAXVDAnIy_eAgVdNDOVLU4eKo_cEKFGmF5aLVnZQSFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rr3r6VuSKp1Nt3THtwjkjDYZdhZMVfK_ndPr1Vlj1uKjyEsigs_f1SUJuvoohw5agFtuGNROrZFlMQTrmRj91ysuJ7HD3pRNG7vOD3z2P1O0CI4lZgNSXXJ2ZoQSKACoGd9znOeyhswKKBGcurEhwMA2_Ev8LgETs62S9KJ38wUN1ao6RYbUQM_5qeoTOcQdzpuaeB1TP-Qx8fQRDwamR-_zsNcqUYnXfXqcDMF1jAjZPCiQ_urAiZ7IB1a0Ljjw-nSMlp79o6c5oECTnBjDbifxxWAqX6R-Wu0i4fgY-TJgmDVo9JgSc5xjkINHywp9I7v8rMCuCUn2WVsJlsUeSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3qlZQ4fCgXZpnDdq5lpLGLrNZ_Xudoh-jkuRKpjvLLSJ8ZGG4FyxQzCze0aKTVH1zr3vgVx1Qpa9ga4ghPZOvkY6B4_NzXInTC_en57RKws7NM70qBD18Yrqsw_y8F8z7FtiT1gwCsqWYXtLN46sfRq9KNDYSyiNIGT2XYler9kc_2PBAvy0SjAA6FEzyrmhvoleOjKIY9cEO6WsjTrHWUEkzhiy2zfumojWSYPua5qBPjyhfl8u0BHuzpHnW71Iydd7fvqMTuzsoesCv8LwZkyOBkGbPreDxPZ9kMAkENuV0BYinuys56em7J8dJjU5ScVm7-ROJQvAxVaMdrXZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/clJrgbLnmVB0LyNAmUSgH5oQ-VPSYN5foP87Mex9HptJLg35jvR1_bdqM634yQijQgbwQeGLm5MVM-yP0n7VkqU8Wz8PqsV64ae0Rci-iEV2CV6tpfgntQkNXgvTM7dP7qGen1A2j1kKYCgvG0BFnenwSm3PG3PnYnW7SvHQpsDKzD72xCVxwHSLAs_RmdaPzRqKbAq2xtqSFRDOFDcvQZHbcYGj9XSXIS09HlLoQdi7pptuFVQ_xHFASR65noPQlvhBrU1GBp7HfBj6k6PPb42bhBX0UZ-vkLY_hm6HpwqAZbQqr6qjkAY1gE3xQFc1Trex696uwqGnZmaGifqLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tzx7_eqzXERIk1m1lZrclIBwuOOJHgS1dkpC3BAqOkiivDq9IYX51dpgrSXPrCyO2Gb7PXwvKP-Y-3WO0Utqh1ZiqG5aPbayNAO1FRjDl9101LSY5LF-cIxLIFEzOnIepuNT0HGwb8DPWb1oJs7YGNqCznj54QAPys0aWjop1atiWaQfDBEA-YYkxBxvUcAASpzDq72EY-_8ggUsQHR6C7TtPul-yvzX48OyUXgQT5I5aGxcCFrQoic1mebMDie80UioliilQxtbYcDQlUIbURXzdqWNSTkVGFZDzo1dJlg1yYZ-mbM9BEJIaEwsS-gjNEw41-fBIEpCtXKfUoLa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dLdUl5-Yk8ecKTT3o6bWE7RQsWuNug2BsKscQ-DnjqCZWd-JRf0Ggj4zukDgRrkDqCpwkRPZQqOGtroD2P0YEo_7HeLYNyrqdqTztqhpBevJVkB4f90OhxOa3KEtOwYubWPnlkrDGg_aQ-Gmr7uDZYDNqaxuKWe3WBsjmVadkhUDROGdZVZACoWGBKXkfjpl_xhZlRzh7nPLLOtMY5gSxGW4nbvy0biA7GbxcmLx7VrP1Pwo-ibw53oSVMkd2DoEk__bJy6-jZTXn_aGLep05QUk8E8L3Rsdr_zy0JQ4hUyfQD_NLn0nChv65DfMZFIBV2-8OSlYD1RwKxKF27uTjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErXsyslfBbUKtaT5bJZUFGpYRpj788YQEbm3OS2_TMXfKimcsBsOkkqsZxikQxXyfPel7fsoWmS_Zw6QuGh_WFSwjtYccGqWO5KvLMF3VXjR__hJQ2Sr8Rt1pkN-2O4QvDpv2LlWhNHtGxmTqZ7sv8cq4YmHrL_nZB0NzzHuPc9jSsd_QVCaAp_KSw9EaUZsEVA7BP5Hh1Y7ySYwIks-COPQKt6CEmbCsY9pXlZ9AQu57_OjDIVnati1bRkWq4BeibojPAfmUbuTMeqRnPUn-6bqxsnp6MEvxvcIFsxJ6vDG_-P_1O_O-JrljEq-O-kIak971ZxdL8g4JuJ6m6L5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
