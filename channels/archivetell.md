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
<img src="https://cdn4.telesco.pe/file/Y3N9kcrxboJjhxYax6XGfhlmQepLgyWgx_UZYObj66yVGaVDmin3X7unHjOHsdYmxsXl0065g8564OMykK7iHHFZ1OKTK30tw0Bm2U4I_F_y49mmmnYkv2BV_QSjD6i1lLyBWUUD9bDE7-AGRQADfwaArgAK9BqlAfIpfkN0cPhDiM9wobXTYz_7-AMJgaBQXAzO8IHKusQDGgvUAAbGDxLy1ZHTQNOi4rTKvl1kIGHnNyUwR7eL5PhXPb5AxzWxlhZtjW1-VnyZcTqSuOYWMk8sSENgXGFQYmXg_lR-P9AdeiOeR2hnf_F2KTQ0ISHhFrIoKce1Gjw69AxUrFDe6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 12:33:46</div>
<hr>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfzEKEOMtVC0JqRIThOQjbRO-BJ31hozbtHxUhH-7YB6hsiD-z4vXxTkkOjhCe0V6Dv2K4wlnPpnWpb52yUPmPhxY3kMddioIk1VxwUG5TAsXAWHvOzgvzyfiLIG57-ZNzoOuFRptOFZz54gdFSpwZMyAV-MBgZw_VPYKJOKaywJV3UZ9ig0VbAvkB7tbAGl9Fu6c8bzK7WltPx1hkXjnXtc5iyaRmC1PPpOZAvplZPrDE5U_I-FWWPsmVYb35ZS3bmS6r8if-W9fQI4cqKNtxry3HY9VjgUACI-MPIqi9BWnQW0pXCbu_o6j3hVDFaJG_e_g7IPhfzFDCMFe6VZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 619 · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 804 · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv_Raow5_fUvhc7rQR5Qc4iM--U04rlKcUabe92RW11EkBzrNBkEG5KX7tF1O1Dxfa1VwWmoX8BhWcnYwoZn6dxfoZUsuY6COOxL0soMabTn2hE2y5Pszm20SY0FezuG0jHmGJx9z3gqUMrw93iUlT0EXm3b9zIwbZ1UjrKw9sW9iImNIG3cqiH9l_HG1GasBcqtNm9-20GiN5_GQwySGICL8lIgo3RCzDFpZ6r2O2swXL2awIhSl6_PQmlZ34yw0j9DRVOjNwsfWYSK5huXpLs7xX9mMN2anYe8RQloM6irYa4ohpCGRoU4HEeHT286OnnJAPmbZCcGAZGThyiVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uunFJBJjRWx89KArICBjDLYgL09ot1moGy1QMZiQb2ZOKmwihc54E_FOla0zTZbEUqGhGbIJW7mAMg2IdrqG36m1FIZ5sZugiyOP6qIm6xJXseF0G0ZOBFbrsvteEFoZtJL-o3HzuA2wiry_4C-BKLIeW0EUJLchq7lxj5MXudBpf9le1nYxIV0yq_dj4GKLKi63hPuE-4ZkRBOCbEiXomtHkUR6Mr7vV6XXbxdbXTB4Jroc5ZEwayXzzEZ1osO8Jd50hRzfbgrEVGnyY_X90_loAOKlVYH2KASKUhF6F_fDQdzHqOCdP_dZa7wiyF38-1XADXtHagMh7n5qPb1q9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdPAltKC5mrffwBUJPfdW7PAlbDbLi1VmTdRJtys4oL4fP0KP7iEyEJgz7WahADfgt1thnweHZ-JItOFuGC14owcIx4JtsqyYPveB_XvfZB9wPdWzsZ0zvslf9j7vlg1MLIiQz3sX_QN52UJ74hH3Z3A32m0nmY-iH65K-aKge90wrCRrtdAlcrup9XgAOdJal4HQVC93_swCJDQmlozP7DWyEIr-i2gg77eIsvd7cnOVvE3r7XUubPfvElqBV_ck-xk3fpIzmXadDPUhRay-5xipmv1UHKABSi6HwYGrr4Rchd6auVPDMft0ZSaJmX8Du6mcRqDOKwdGo6x0YdB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQtCEb3QcGFQi5qSAuZwI0Xp4m9Ht7NLcxi-1kdfgZGN56oybeIThnjAykidTce_QlXpuL3MSwWVR2BYzwIXsTvrsaf5CgX6yrDL21HyQvrp4azzAX1RVbPFf-bbMNXG3mNbmdjrzSIbbv5OrOmD96ztv_s3EIDREXnWP0WJhCW5ivq28IkAfn5f75qSvKCuQRhHYaqS7HsbUQaovZ1ESMwkPcLhceQIyr_IZmlwLiDHXsO41JJ8ipcUDYu-14p8Wjt0Dim1tPYFvkQ0bvbDOJ05FMmtm-prhinSGd-NcrQJEMAMrEIGL3_rMN5frK1aJBMxT-HBrrddV1yn8ZJ9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmwPpVG61psAtQdwMHDeiVYAASq9Mi6tK3OXSI9ho5OTpAgLvBX8LpMbZgmBFPdCbGFMiT0Jb8dw6rUfe9iWWnlymXvftvCyK4vJuUiBdt8KbT2B3XHl3pc64mrEHOjo6r04Su0k_T3OR-KWaURUFZGBxGVwiUUBA5YWz64UV0eXJ5w-0xU2lqfyYLpYARO5J_I6xRWkmc6q7_VmR6nHucx8Kkp-VPeRQ8KyAfMhlXUyBPn1tJfvNSXUq_hp4G18t4DGRT55nULY7Ln5qKAs0iPsaBUWxTZNZFImlL41hQUjoj1ldVchxnjYPI7qTmeGdK_V43UI3UWK_sndc73k4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpdsq2fOFGZxYah_QBzHv1ejr8ZdyXBLr_CIwoN-u_sNUl4fL2a6Z70vmyaXrQ-yiO8SUqy-Ol9MWZOSdFG8dGxyujiz3mlUP6lBL9hXczW44ilonpBxvFNnY07VguKYGt8UDOAAESxtMewkNNC9HY1GzF8ZxpvCtQLxIVfcDdSpei7iRRDmXWpDg1CtzNSYzT86yE3nBDV0Vkzic5JZbzaybdK36SCoZzJplGai8YiQOnVksBdEQFTfOPlef2qJc9n0tWFIsedRtBn7hm6R00SDKzmGUknMCJAhPvqTLlx9LJgeqKaOWUIgQhgzBsGpMg2R2gNrycESweucsefUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCrCyluWT5t7TBl-8swQwSiu-_MnIH-86lRDrS3xrJDc6jbWzsgqoBlBtly3YhG0cA4yixBWW1QbM7gzpUBalWyky2UHv9k90632lNjBar35zQUF9TpTzy-dnssTXCmLyEolKKYQXdf7pKZG8QsSB_NdxEYsfJeN7YNS3tGPYFGcSh-GKwWSUy2AaYKKLOXKZSi3CcNN6kyttq7xQHOpwI4KSmnzX2W81jVOiZ9QHt9DL53rsrttMjme7dpCtRk-HYJrZVk493Nwi7j-ysVSzHZxxnxHpSAhg9zNKhvBezfmzA4tpHqL-oZWvkZuwFOzjLFB0OQcRuxlrSXQFbYJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS0R82oWZ_7rf481K9WB1kQ0r9PduUOUAEn1dfdbrhyh1Xsf7L49dY9plurOiAZTGm4ak__zLPH_7F2leRRv2cspGdmCwhMIrMjE3zwqQkADb_YQnKJc9MV8wdtRbBoxL8Nsa5l_LSmHVrEAekVBt-BrHXvEmb8UA93alOR2ihAhsRurKoEVNEdR3ouWzqLNPL7LeKIuzmK2XR-FPOBS4akkuMfrc7vsjm44k68dWBNqn19GzudcUcx52FripM7cpWGa8RVizWpeheN99gufGh9ibkqmpiK1LKSNkPsGyFPKIa6-KK2FC4cGsZ9nE4f8Tb-ppZyUD8uTZIRp1AXsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIc5ABrHhs6VsQM64JSIYwsUD0hOer6dfRgNTpRcaHTUMmwC5m-dt2GR8wjye69AOkAhqr7Mx1qtxacBh7qYdY3wvH2psylktOgoIU7EJaGfMiw2n0Ijfn9fuwvS4XgKHWS-cL-_KYeJI_BXKc6asWbDAUbCVbpj_mLwIsBuN-S57aY1I8hQEvZMuLHlV2QHDQ6N_BlK_YXa5vGddNm1GXd_zmAWk-rk988DgIi6JiHI-IfZiroLJQDrqycz6Bn1vDzSKW7QPINkQkd_iLYyoFKWSKvusZZg6-9UBYIpsrByX57R1H5QHxo1VDCjwi1w0Bs-ZOHYE8Lb4FpWX2xcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C87GmGCLe0Gl3euWN3yUvRcBm40X2EuAPvynMXSoBxolAaDBHCJZ7gXYBF3KHQIv_zXSk21HEfa0JjVlwl2Yz1GSxN9A2awprUcJkx-CB8etI2r9ldWlPTBJi0utFsQJcEVVB1UlTo3UPzavnFrg04x_0e-Gx2K1PXu2644uUUh3SLNS-K998mJt_nHgd8b_eiRuW4IrvtPTMhUTk1Ecyoyrv7Pky3yT-lXXtrjHB1ucH8MwWUeWF5q2DnkkZDzNPWMlfjd89QUqzLdRPGo46S5ZIwgk-pmwiiPClvXGrGQnAH0_DrgIedEOyr3ua8v49iwlAdTZk4SvICDfbRaI3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrZnZAaOaR40EiSkAnVw3F99AA-gm2JR2aS1_A4VWVgsB8jIrgtJ3unllC_7JbJ2O2wsc7k0I27tyXkksC5k7waLhTT8HPdcDCnxOqu7mal4laDIY3_UAl22qcuZYki5DhhKsctscbt7v52-cXZyoPkOWeTbbUvZ2dmeB8ikDna2G9P_s1DrNO_ic3gP-iFo01OkmsmfOxMUsKx1JBt8Yu3l8IcM1yBKpnlewvNRG3d8PKqYpREOfI4Nv8GMy9SlKqmBAqPObkIsvc4Kf4f5i0wfuAzJQtiHNPL86qa3lOL3wRN9N9VUip1zVJ1zGqVXs6_J16_QZQdECC0vsBLECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=CnFUNv8fkoH0VjJr3wh-bS3N4j0du4La874ytqMzuwg16flUOeCwNj9F1mcCIfHchTADFQp-fR1TGs4a-4KJsA8C2rPnrYt6sDe4aVw7Mffaex8xAOCFC6o04wAU-YW8ENlj6SH5LGx9bIIGyAUDsdeDdy_rGTDqZjv6Q2VmSgsIWWkpu08Lz1pieCbmSiA52oRz3ZQIuRjJbCcXk8Zpg_19a8KwvHe3QFXVmDk7EeFFz421qmbWXl8229UmiR5gpezsuVTkeSdLXWH98LKGFxwXlpqE387v5BFpWmnpPhB1q9xUp4Hf1B1hjed1HFsbhvMaihFn8qRcgfo0gqsIlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=CnFUNv8fkoH0VjJr3wh-bS3N4j0du4La874ytqMzuwg16flUOeCwNj9F1mcCIfHchTADFQp-fR1TGs4a-4KJsA8C2rPnrYt6sDe4aVw7Mffaex8xAOCFC6o04wAU-YW8ENlj6SH5LGx9bIIGyAUDsdeDdy_rGTDqZjv6Q2VmSgsIWWkpu08Lz1pieCbmSiA52oRz3ZQIuRjJbCcXk8Zpg_19a8KwvHe3QFXVmDk7EeFFz421qmbWXl8229UmiR5gpezsuVTkeSdLXWH98LKGFxwXlpqE387v5BFpWmnpPhB1q9xUp4Hf1B1hjed1HFsbhvMaihFn8qRcgfo0gqsIlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgBGuNmDrXv1cEFxVTxAmLj6fgNW7Zt86RiSYlC6AcERf3Zc1QDJsFwNl9o9ZTBRkae6nEZl3Yg_KJSRCzitd8fE5TNRlGaFeWW8B0sL7RdQt1F4bCMS7addlVtuvnOV4BSlpLUeArL-d3ifHqc37ud14HmpsG1W6VCPgFwkvyI0umuNH6OJiccnRw-Mwzhele7b1kK8tFh3IZ0Uhuuw3k0ZCeHuQktSG22Eu__VLDN3OPlg1eDbOB-LRWkb670fRXAYCLE0OP_7Xf7GolKGUA3y7XyDg1RisiwwD6hI6AgcousKv8LupL_-vLrkJyUxiJ9txciVVaHHZTQYc0sGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gtf31SVIUF_skd-sIbjS_sc_mMj0vARByJ8iZTIdc4RLJUJ7q64iD5xkMbXQfPZXtQYzkkwm-RY8BRcKedfUlowxITAf8lV_BTEGebXO0-V4-ywLxGJinSfouwWPr26bNhyMqjsqyG07O0jv24IO7meXhrBrGe6_0HVN1-OJYTU6T24Px_EThqOu8ySs1gVlV415tEc_yPzGm91Wr2JT3WhNVqH0LoLzNa7tOO1rdxpwlyXnzNv2hFYslD1aNSO3MmieckU1-CxPdFlqZV3nlYRI_BOvP3ARAeCijXyM1EvMQElsVywdgrbL2dhbfSfuUZihIxmppSOUUc4PeQsOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=GZ2jb38D6Rmys2NOqaDvwS5kpoh1Apj67A8c062hNWIEroRtVwgqFHbGLuRH15WvTPf1vFJlht8j2XvYHGZLvecQ8UeRRdAHKyVinNKaDzRqY6GdflnLNPtV7jl4OUsxZ0lzXmGFORqmu2t_NcPGd5Vzl2z4Zp1chD9VOVueUQPULqVsWJnJIhb3gbTgSk7kNkx6a77lCMB_jGP2gq2Pd2yIibhN2vVYlSkT_S-eWhJMRprxdWnaKqMwYWX3O7nM8NKbBlxk7OGF-aOHlFa5vSO4JfSWKybPJMpy6CBEbcn5HRdXQr-27TaSc0nBgjy7LaNXbRBIBAf3Tmg6Ftw8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=GZ2jb38D6Rmys2NOqaDvwS5kpoh1Apj67A8c062hNWIEroRtVwgqFHbGLuRH15WvTPf1vFJlht8j2XvYHGZLvecQ8UeRRdAHKyVinNKaDzRqY6GdflnLNPtV7jl4OUsxZ0lzXmGFORqmu2t_NcPGd5Vzl2z4Zp1chD9VOVueUQPULqVsWJnJIhb3gbTgSk7kNkx6a77lCMB_jGP2gq2Pd2yIibhN2vVYlSkT_S-eWhJMRprxdWnaKqMwYWX3O7nM8NKbBlxk7OGF-aOHlFa5vSO4JfSWKybPJMpy6CBEbcn5HRdXQr-27TaSc0nBgjy7LaNXbRBIBAf3Tmg6Ftw8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=qEkjn_AHB3jBPpgwr1vYJJuE7KCZoZuws-DAuKKI9dC7pHZghgRzTV8QwJLq2MIFOro-eMAS6UikSqxxkaEpllWpwWeuQmyS71h_SrvsRhL4Aiw2KueHdDMO8g82DuPRiQYmJchSeAbndvi6DVHWDlVAeubHJMiQwiZrdDuWRQKFHmSF7tGnEIaNp5Y8PuqcdWjCFq87KvI0mSxMR4VrFCLkGJIEjJuE29FLzSw2GqCulfVk3jh_9Gat-fY3FJlFPC_20klBEa-hlGy3xFu0WwI6Nk2G68q0e7RxGonOFQ8AOP5oRzc1gM8ojOG4FNR0zHFRWmIRlqmfbXNFgxq9lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=qEkjn_AHB3jBPpgwr1vYJJuE7KCZoZuws-DAuKKI9dC7pHZghgRzTV8QwJLq2MIFOro-eMAS6UikSqxxkaEpllWpwWeuQmyS71h_SrvsRhL4Aiw2KueHdDMO8g82DuPRiQYmJchSeAbndvi6DVHWDlVAeubHJMiQwiZrdDuWRQKFHmSF7tGnEIaNp5Y8PuqcdWjCFq87KvI0mSxMR4VrFCLkGJIEjJuE29FLzSw2GqCulfVk3jh_9Gat-fY3FJlFPC_20klBEa-hlGy3xFu0WwI6Nk2G68q0e7RxGonOFQ8AOP5oRzc1gM8ojOG4FNR0zHFRWmIRlqmfbXNFgxq9lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=qzmnTA5uImGJwgZw1FYVnKfwI6FjjrYfijv_D3XhtlMJ-_UjeGx3Vpj0ZHmaUB5rHRbRU9Czdc5zGOEQuYAh4I1xiay87bnQk7LjGE71LDLfpaqH0UOwe03tzPFOGrbkj4r3fxJqIa74y-sq3sp7CFmZijuJb_ySwk2LkQtD6tmONF96I7BwjmgiKAv668v18g2qi0oeALRoEDKQovbG-hF8i9idPs8D4jyb_Tp08-FU4MwVAwm910ryrM6lIFZwPZjIdhsM7Eryj14mkJdaQulQZvEWp5KoIBtQhwfYmod8yjjx8vRmI1QWTh_15B1jMbs21m2biFNkymkNtzAyFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=qzmnTA5uImGJwgZw1FYVnKfwI6FjjrYfijv_D3XhtlMJ-_UjeGx3Vpj0ZHmaUB5rHRbRU9Czdc5zGOEQuYAh4I1xiay87bnQk7LjGE71LDLfpaqH0UOwe03tzPFOGrbkj4r3fxJqIa74y-sq3sp7CFmZijuJb_ySwk2LkQtD6tmONF96I7BwjmgiKAv668v18g2qi0oeALRoEDKQovbG-hF8i9idPs8D4jyb_Tp08-FU4MwVAwm910ryrM6lIFZwPZjIdhsM7Eryj14mkJdaQulQZvEWp5KoIBtQhwfYmod8yjjx8vRmI1QWTh_15B1jMbs21m2biFNkymkNtzAyFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nhvu0oK7vd00sChNiVsLABpnWIJgQgv9nVqmmzALtRg9X4V4oVELJ5M4YQxd05N-GwDgpP4UBEdh9rno3XjbM2M36vbYPMDq8D9JVersYevecj3h9VIp_lb9A__SYe9MC4ToDeUkjEgk4uKijdd2jbPaDwfgGVm-MQ1H3wyx6nFGkAPszgsTldnhIUWHnTvJcFF4wp0M6aMb7q6oiiKNc0U9cPk9uAbES8Hb1hz5mlnMr3IRFnZAlDldLJnu5BfbeWbWAD4P8ObfChqE51MPeUh59OWGLdfme6igZCGcqlBT_g5iPeTqjQx4EmsN7y2h4DpOFs9Py0y0PHkYo52V7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=LIoIbUJGtsu0zmNND_9JSLr1lLT1RyFbzMYYG9q8IPAuuA8zPL_z_EvUv0CRWSOcvuRxzOhFmqbM6N2jIX_Wcd9wpt9k4X9a9DjHq-pqU5-V_6I7X3fUq2A0E1M2D60i5LluTpIifnN2060dPRh0xA3ZCYf2_VDZet3qojiaGqH28xkFkCbzMIEJwnZWY8C5FvU9rtwPZ_31Qo-_nAF8AVdpKe3EhF1piuounXq4D9EtoEKDGdc5HI1i_cH1FpFp1KHQApD0dJ9RdJY3vS0z_ag9OOq7dxpQuyQoxWP4zfQpgOq9kVycq5wIuIabsymL94wR86kuxjdHaDkUWKa0hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=LIoIbUJGtsu0zmNND_9JSLr1lLT1RyFbzMYYG9q8IPAuuA8zPL_z_EvUv0CRWSOcvuRxzOhFmqbM6N2jIX_Wcd9wpt9k4X9a9DjHq-pqU5-V_6I7X3fUq2A0E1M2D60i5LluTpIifnN2060dPRh0xA3ZCYf2_VDZet3qojiaGqH28xkFkCbzMIEJwnZWY8C5FvU9rtwPZ_31Qo-_nAF8AVdpKe3EhF1piuounXq4D9EtoEKDGdc5HI1i_cH1FpFp1KHQApD0dJ9RdJY3vS0z_ag9OOq7dxpQuyQoxWP4zfQpgOq9kVycq5wIuIabsymL94wR86kuxjdHaDkUWKa0hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMznChNnie-P_10SpV1oOhrMY8fzNsj1vKXrEHjhJwH4FmddtV-jIpq-Ffz20ZRFUlWaTGMtWlij1yDlrmmzRE0b3WLL8a7pruQrZiAPkwrNpqUt37dMCBo06M3GkyfxFuZnQEzAUwGqTpkzPcSRRkxhwLDHYri604KSSSDauLI6-U0T_tTjY8L7NzYurgs3LIUaZXA5H0J1l7aKF4NmZAlOPGrV0mqu2h68BxjV7zA0Op8QrfqqEuRA3QBdCIvT2IvZ7uUbICl4JVIHXshSGxqoQ8GaI_rJJceSFIUr-GuMY-hNYux8Hb6Y15KHOyiv41lDxUDovqex1ifxv4025w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOQo10lEb_TS70u8plPjWerO9jUpXYjS7W_CHJSsbAZyaPEa7z9Y_LaBgOVsTUkVetXJVvxpRLRq9m_niQocFhYved3gs_HPBE0WmWITe0Cbkh1ME9FH9aVhrO9NU3xHxcjPWyfGRrH7F8XYVN-gfqg-tjK38nzv8h4TI09tLSM_BoRxDyGKEHndQPDy66fZKVqDOi75dbNyCpbwOHf8mxboowlTYbdkaravpJn17ATyETLS0Pha7DpE_2ze0ZjzrMW9cEt0Q-SFdcANaDuSHIme1tASoXVRCvcxzlKelW_OTHJjWTgaSsoKgqwbdTb2X-eKOsxZjdOaRoK-CSpoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgCQVY341ciNcQQi5hR_5E6oSPymi0U0YQe-f9tL03-RYgXFlUzrX6CeZi9tiVzyRGDDsuMM95i-tdLXDRpCwcQF0dC-vmeDqLA6L5L4JxM2ftEeIRCtqGW3M0oAbEPf90vXEcVTUjBJAiTMzG92VUxujpQ1KV7-YUf0qBwP_CyVqi-1oiaSZWczDbAoCRchDCE7byihbALlLNebweOilumvp3xV1_jMoxRtgslbFPTTkyPdXMKhMr8tSQIC8bDwtlwAa6KrvAIqOScW-8DJ54JFfzxgaW6RaSIu-GY-RHejZ9gjzxOTYgQSmr1mXOrENz01oE_lvS4Zh_ZqQ3FiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sbj0OvjIV1tTH1C8Cw07eQe-fwzITZOYm2xyWMbf0g36E9c20PExb4zYVbrKSOpvstJslV3aCCZdSFF1JFQrdvggO80K7C50oAUXHDlYnwFfx4o8vtgSISKAPqIwh7BvK_mDVX_PFrXRyu-d9fhLI_OWwREKguGw7nyOBf-Wzto0w4Y_Ddbta6413X2X_EcebjSsvb7gusXNSwsHb7uRbRUOjnCgsp3SbV65qFa1VRyt5GFFzISNTLhq1gpgGeWRku3HJklP260QjCf2t4ydLahKb-_bZHn_EgI83qyMszESeTRWOvGf1IKTgWEtLYCYTTq1-dM4LYIxv_jm-lqVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peFx18xUKfpLuvNHhK8ImPn1_9_8SXHoQc4Owrc4vYKbydfARrFx1lhqOQnavTSskTaHapk2bMJXL94TK2_tpMm240bE__1gqnXSBGUez4cV4lRq8r0HbXKGr7QKdz4TrEcqoK6VnFvOAiISb6Cl4wtXeBdgjbl3QQYETQfIGSo8f8q03mIquBakETBeYpacrkAJfpOcjDskQL6Lz5nWvDT7ElOeSNmjhyCitt9RldsLFFrsJG9RoOhaH-r9YDXeIHkS87_kbsnJCHzSX9woQF3DzhzdswJe9DrfLWuvsD6livzp9UN4ovfAMAmdrQAZK1r2hQ90kmEBktMC4ATWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRUL228Di7crtj-6W5zwi7K6gKxhDVXdD6bbsL-bB0mYSIrOv9eXmIoMpnlvDUhQDEvqZHM8KEeAjF54kSWCGTEFfT3qsB3Q9kB5bpywW4yB7qWJlPQv00FspSxtOZIwRX-u7fIB3N1cek5BhqZbXuS6ympPNLLnCWTlt29ubUf1YyP7sz9hm6vdFHWHKI3ihLKDRC3T5lFwTU3WHkwmi1vEb7LXhwMpoOxA8hGFpaeZdHK0AVdbxWPARoLDPiMKEAOf4_fisykbTjy50FGio4Bzd9ULKoMBvMQZrFebAFbMAJ-XNZakSjmRUkSR97S9YIPh91P1rOMayMb-8WW3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-4GT08-sV72VtwgW9Hn_eNRwETcX0lCDTgpxbYPKGioC5fBSpFewLyc6uNRe6Nx_0kDbi-0nBFgmtmmXQY6QepPYWUTl5LM0JdnCgLM3z282Mqb-PxNMhT0h6wT7rrQdBCp6CW6na2ZFT_-xuNXm4LOKCD0R0CMhn4CcGOHW7Z9odZd3QwPCYQvAo04h_Q4bjK9Wz30ALEy_Zbq_3PUcF_XEGjLT-CNIU72XC909BNdG__wYQmJ3vH4WdfMPTzB76jXt0WVP8wI0pz9YeY1lwju-D9pg1CVX8JEj3n0oEA01fPZnTRWsD2l3I7rsv4PhcoiYgMx3w0ZV5TDeb8vIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXH2U1J4aQSLTyawM4uaBJxkJD-G4bXj8_jfbEN1X5A0d1-MoSPIEFxvgjHbjNOKuzkc5WCDPBM4n5CkGgsGlHagAtOTrsNAg-u4sQGMt7LRG4_QhhOGhHPul9E4L0f0nOU6Q5V6Gb6OsaD45AW4EfE2R6shXFwPF65X1ecDec4VH7R0pzHyp9H3IUF7QIZmg1D5vt29RijMNhf7HhVLv8wEtf6S3MLliIFMZs0iOMJksIziLbE4GwTEzuhG_JbERxvESyQR7nI1sATIB0XGsIAif8FF-StDy0MPnNtthRPZqMRWma8tOTsZ9cqgJ2CUG1AhPa8i52A9ytBr31TXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GESEXjxdGKVBRkBfgE_6GSIikKArSHY7CIGkyCxZaa-G4d0t5eeqTCtQOiACQHGFORdl-y0lZ9Am9BGq9Df4VeqsDCaHR4Mn0KdcpqWrboDidSOYgsrRK6ic3rLpuwyKpuZruLGHolTx0KWg88LVOH2kFIoflnl1wX25TP6DVOpKHaQvgx7cCoby5iK1goiJdhv0WBqyMUq3D3etuGSUkOJWMuR8bNlAs6Wlz_QOCXrD1PzYdUtmUIvmuJclGcWHXrWfbrFTM6sdKXoy0ZB1_vbrsnt1DmH3MqdH5ik9l3pCsg8mje_F89jSEkVzDrjyfUbWBzupDDvgcPCQ1J_bAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwFWn68kW2hMUQaP8s4WXh5-MwGaVMh45KA6Lxf_iE4VUZV-AezhwwG2GCNmZogz8qpvM_T6WgevwNEa1mBB1mmLjz9zGYk9KO_Yuw8ezZFax_JVLQvMo6pixAgBE_j63SzdlJ2Yqncj6nud35bmIbGW5vZNAiFy8t52lHQ-ACos33EJTsDTWotu6PjiChzE4HjH2Z-W0baph_gIcMPd0eLyjvwSdVCrGYWeFJMMzsrJ9EamVWjJdgdAHSDcEMONMiciqtyfNjYrV2h2sGvqcWLev0VHm2mQr18UOHSnSr806hAPucsMzGPAvFJVGOxVeh5dARBzJvuQbgPPeqzcsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4GYMYoq1iriwUgO5qonsbKPGEXyeqkVeY77y1E2AtlrFvyRatHW5BOaOpeoJ00S-tx4zFoVOj-s9oPv1oHch_L_9F29lbxE_XE9M6aPFJ2U-nS7akkpAbZm9pvoQWJ6FxE3Mh8ENZkn-6mJ6luOunzkulQKU87z7aNWXiHin7LyIWl6KzJEHVPGtM432dAmxp1gNWemg1cVukalTeLtFlVHEDH9XwkaGAcyr7way88T_fMr7-okU4xA3j3RC2m9UNQrhRWMTGbUR2XwfSAOYeIT63aiupl2vFSTzavxDzJubSHkykdJw1T7-ngcn5Jm9EowT4ltKb1LqpE79MrWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTLqGloNvpnw9tSSTiHZv6I75hNZEvSneVGDoje4o4btmu_olbQEp7KNZZW6MTKK_AfTuIBcHKd6fT1cd2QfE5a8ue6wgC9yBT8dwZ2RfyiFLPEnhtlI-N0G3M6CVJ8YN-zRM4f1pgA63cEY_SRk2pEc4exhNfktgQCL3fBzv7e_cHEDHERMe9ez37FI4Bf2ZIO0lqZ_FJXyW0FQvhyQpNkVNXxtcDQT5-JmJgd0Opi-La07pNFElISe0URppHH8PFeWI_2jVdRq9IvImcK53ZBIim-lC8oe9RhM1m-esHh6SQn2tbmPQ41izMHUYsiqIKv_rdh5WMGLFuUDkKe1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9uCBDhKcQuxALV2SJHImOAGy0pdo2_1SqXslSsaUuV3BHyWdO0L9Pn43B7vWjtMX44ZLdOusUccT6VA_7BgdxIhNYsJ9zc-jBIwNm3aQvJvJjgi0Z-zXERT9HAB5ABh1aZKIx-N2H7r3AGZCf0RHzfy0Xxnj0t5DLpW2txZCBGXv6iHkddy1h7yNxvegbJgv5FoDFvGUbOm3KG-tnWr_9F3E7FosKSZAyfQ0_wtV_8srncCrL93jiP97yTB0Be9cq-yogl-GTs_b_WGU90NdcnFDRpjeVOdhxKoKVvHPGn4Cd3gMQI5HeUMZ2bgmIeDrP03n4bccwACAqJrHx3lNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2htxbTgIblfOpCKPLqE-Nw2c-hIrVf2LDD1dccsQLLAgzO8qebWROItSqWj5CumncyHSPhH3fJdIEVeRtOfYYcw9GpNBVNjn0SG_dRuRZufOYDDWFFUf9A1JwKlVNv4h7iIRyYhN-uFuoGtwO_a25ROC_8zxuED5qoLXvVovtquOX3kF7-QCyos_ZuvDBCnYZoc8fJo85jd3G8gZj-1J_UzucZny2wbxvE9l0Bc5nSSCxI8ACy2GvXD7SvB7iuuh9PksnQdhxlK5_x1ceUyqYoOmyAhPrux3r4mSPDUU2osF57DIwI5Qlhl86CS1m6-_Ble9ivkyz2723cqPVMftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fegL96YYCEHN5Z_PVatKsQZqJJtYmpCYb3wz1SgduoR2DVRaFhzPfUoDD_6FhN0q5aJRik4YdZs08nPX_vFJ5TXJTbozlAcCfIEwz4KB_WZs9F9nxGXR1FH6iHeTC9SlHaDDl0e-5RmcoTbGk9lFABVC2s5gnCt-7_o-Xu8NpHzSIGCqLxEVGnV2mCnTbRUICZKWJgrYSuKdmyX39pm3mT0jySUIVjGcejLEp-6V8yYbVr5ihB3JK3K761eo2MK987f6h4KVZWfxNRNjIm3NVTKH--m-7fonaydzR4rWEqfcareRE8W8R44u0QqF7xQ3nADJ_5YpR_SkJFUCe4u3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAFbuqOT3U-t6xhCpzcuBbzwvH3au4qudS3tEPxv6YR7BwAKDreQijSM9mUNI7-6BLFnKXAFVexLqacDzobord_9ciTpVDeWGUYHk8oE58Me0vZS8lFX6CJqd35XY6ymPqkunMVz_3xfuyuzpaqbQjhEl0xIW1q4-8amGbWPGRAoeLeQ8YQ9JYNyU0-yfGLEfnr4dYkW_AaTNv9ob4IQk7NJPjVBrDheScYJoCilgETSa_kibh4eAQza1YHp058CzbgPlvKZZ5FaQ4DG554y1_9bs3Ot1yuALH7AbS8QT41AJR5nJkMwEGOzrH6CNennERIBSSBcJieX6_H8Hwjw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcW-jY1i03tupqBftG_SAoJNe2aNXJi5w1OJQboeJhMffWAOfatAedhe-9aDM7ZfTM4PWO-YopQuUoqQhp0oPtduaMKo6N0QwP44k3X-EzInRcKvJXOV2cizeWn-dabt5b0HAA03M75AI9Z8lnP-6ze65haf9iNTLbORSwysUsi-hbQXW8oMXPrzXQf_IbDfyy8Tltfgs9ESmlE4cIT62sQMo4xcNrkV_yhOABKIrM7mHVGZBo6VcDp4LPE2-ACqC8sQLr9fZi-bo40A6Iaz3BI4G75MsP_EAnHaKi3T2MrovHDxkQzXVUvz0bQh7QqNkT3QXVBqP7_pRrm0v7AqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqKa_c5bbnoyNiFp3VgGlFH4c7thw-KEpgi6RZAuf_fnb7Rrmy0M9WivN7YJzsvLcC2FSLN44N2dUK02IHgSGp_DJn4iFweK-CT-1yVx5-wjUYuEFzb_YNjDqBxEfgcutHQh1KDrHKtzG1F4aEUne54HnAQOaB2OnxrwWmv_gh9ebGMQxx4rM3WGfkG9VrRqbIyNL3xaiadVdUHEKK7N1O8yKI3WJJzabhdXNmdLnBM-xT2U_6oDyRvf2pOztoOo0Mplj5kndHY9SnyPgOcbxzXUXDdbzE80gTXwwELig9IXL-E2bNW4_kR2RVinWiPjoeBcIt2xbFVQS1ps2vH-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=ep7R9ASbk63uzicQ-dBq1WBjbhIJFWSxWmOfde7Xg5WyQdT7HkW_vGX_JDp-m9e8x6si30R57HvHXp8FrC4DmU2vAnj4SlHv5yrZYKXp_J_-zK2vhH-OqZtYIQvwKBMCbct6DUMaRKZDdq1vEcOtrWEyJooDToPyD6Hzbok5tKHsX9Bfbf1qsP_CIChLxyOyDbp4owjCqCSopFmfbXuAU89GoZ98DEuXxIRmV8w1_L3lhf--glV1W1PFjYiHIZusYUW4VYhelUlS8Us0QEOwY-md-xX_lAtDl80FqF4A-oxJP-s5iCt6LfTxhnRZ0e0QAE-VICkWYOo7qMIXTlFTbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=ep7R9ASbk63uzicQ-dBq1WBjbhIJFWSxWmOfde7Xg5WyQdT7HkW_vGX_JDp-m9e8x6si30R57HvHXp8FrC4DmU2vAnj4SlHv5yrZYKXp_J_-zK2vhH-OqZtYIQvwKBMCbct6DUMaRKZDdq1vEcOtrWEyJooDToPyD6Hzbok5tKHsX9Bfbf1qsP_CIChLxyOyDbp4owjCqCSopFmfbXuAU89GoZ98DEuXxIRmV8w1_L3lhf--glV1W1PFjYiHIZusYUW4VYhelUlS8Us0QEOwY-md-xX_lAtDl80FqF4A-oxJP-s5iCt6LfTxhnRZ0e0QAE-VICkWYOo7qMIXTlFTbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwG1ld0UU2ilkwlh65vckXTgpwBwsxrrmZGFeHa9FzqqxQfreyJ7j0cAaTdZNwbYH7wGJfHQC-KyeAxq1BY_7so2BSz_CfhamHyeHe9CXqi3kfEz7u1Qea6H_lXz7HS2ITwZ3grw95kD3kLTi7t-QhRthu0__Kn9Dt6Q0j2KaAEOE1XHyeFnw-V_Dxk5QIY7uhAq8_MgRG19zZvGkUdr50lnxurENg---gcVdPRphmDArUXmykGbbsE2mCTVoRLxqZaOALppGlkfj5foKBUfWOV7NZF98Itr8iq0MLpJcAAB7txWGNdsNql0URhwFsK95ojAIO6SFNCNlJ9QVk_rPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=nZgUfM4ULqgvodUsraqVcT7oLv2SRHqvtv8_rRHRU3brRfqb2LemEESBq2OFtH8BPsnQ6SBjZP0qK4g7n28oSBjMuvBDikJb4hujjZk1dm49F4GTjZLCs3OWNEoyWlddmaZI6qiBWGZoMvQbs40tBj387CnsmrtTjbDWVRzgaeK17lp_LOzxgBn7_UnbgA2uayo_pRT-5q7l8KytlPok0doQb0LOHI9oWeQUD-2CWVh8FpLpI3lPi9aLMf5Fwsqk5oo0SNyyYEw5TY4wp9n6zVbHPnWb9woZ_xutyXGlVNEIIdLsNkHWUcaIngWJYkRGS_OSBwZCiYQ01YHpD8hUtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=nZgUfM4ULqgvodUsraqVcT7oLv2SRHqvtv8_rRHRU3brRfqb2LemEESBq2OFtH8BPsnQ6SBjZP0qK4g7n28oSBjMuvBDikJb4hujjZk1dm49F4GTjZLCs3OWNEoyWlddmaZI6qiBWGZoMvQbs40tBj387CnsmrtTjbDWVRzgaeK17lp_LOzxgBn7_UnbgA2uayo_pRT-5q7l8KytlPok0doQb0LOHI9oWeQUD-2CWVh8FpLpI3lPi9aLMf5Fwsqk5oo0SNyyYEw5TY4wp9n6zVbHPnWb9woZ_xutyXGlVNEIIdLsNkHWUcaIngWJYkRGS_OSBwZCiYQ01YHpD8hUtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fizr24Llq7MkFEUGqHe2dUYXC7PvZXxrpxX0H_n43PgOMSHA0xWvhulOVto1U-w7aAiPWV-UG2ol2B7E-0yGqg4KM1ewFqz80f5DbdLAhvID9jjR0h8xp7j6f81o2PdgAezR6qm4tMuGqPJMZMx2ZllkUSXH1DNkJ-Cupunw6mES3wfy9YHWM64i_Q8b37n-lB5BW4yjKllZW7uD2b6Dfn0aCt08xIekkXhDYrAD8gAsccgPVsR3hMgWSf6eJczU_NwZ62AHtnQeoeRK8v8gQ6zEH0UrFIZVlSR8PxZiwyw2dpTZrpV2YEPslTZ9t-W280heHs_2EVMgAB76bCchKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVk-Xm1e2CqXKFiyjnYmdhbFlooPD8JrfL5Dxvwe_LDg0SjSLsqIOekvlHCA5SJthfoiODHiz3b_ar5UqDC4HhJ1xx0WvZi7XSzQ006RUAwhbHkQE1HdRfZ1yJI0u924fWbbGGCUAXnP7F4ZFvfT4uimZxcYB1BeC5p0VvfJNj5atjxuz2fDfyOo6Dt6n61tQKdUQ1XeLV5YkHkX9lC7YnnH90yq-57cxIDo4JUI0kFUnTr4c-WGd0r18I0mx1og_2K533mDE2Tyyx392Ums2cmJoK8jia4ksDpeT7CVBk3aU4BuGxXkvkaRnv-_IWwiBCRXVd_CcJCxoS3y5-2GWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jyuvPROnDo-JuJIEd3ZmDVrQ7LAiBYaZshQrSpEH1uEOdyoUh4Yczj7cSeuKjOiPrvdh-GCQtNjfA93MdrftqXIYOU9JClPFLrB0L_wYTK02OLhGjbCskHZIKNcZ-h8mMC9qq6-AhOYHJm4OWAxY4Vy4Jkh885qzVEuYZHf1PgKw8ssgv8pQpoScTtxdT34H-9ZXeNII6VhYB-7S2T1Cd6KgN8GqDiCe8t7Xzj7CPJ0cYXUk39IIqtF9UV75QmxpU3B_1y1cNwkYCg8414gYNxwk1qDdPO_aRIHFDauD5pahkp8tMiNqn3656yJh5whrvX3XqaVpKh1kT8_Asn600w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVLnGf2zPV3n9kmHpEZEz-GOdowMrossxyT4K-5qO10i3FwjrQxTC5m5HkHVWFNtXy7uujqpAi8Bh7YuoDcI6T4gTzQbY07Pewr4TH0n4pjml9ddysHygUSfSIlljdt5ag8o47aBfnI6XIBPdQlTrJ0M7IJNPb26Jpp2nv4vNB92yaxjxQ6mxUFLzue_oyfAXkXDk1M5hIJj7EYYDP-EZvyYNoPuJQZ74iRB3e_63dtQ_l5YzLvYDp1fAcTTxVL1JArsbJxxse9jFacDdOsefGZSfL9UThBwuscgsteFQ_qRKk6RGNGhBHhTdrHNHMJcjW2DYLQ5YUpDE0GPOjGy4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFFCDakPa44UvZ5PzTxuWGrNhegkh_wR6s9l212NbuMw17PYHs0ODIDBjGQtIR2ScufiVvbLbWEbYutVa5veElQpt0IayiHGAcDSbRPQzg4izrg9EMcGISffqNeflWWAn2zvRMQlhWhnrmkDKymroy5SiV7qnJvcMRoQN78-fLQLPgWHvTxPsvPKlOvnoLLVuZA_eByFJqQKtZXTf_eTGUBn9q2bs34yIWxftRr4RIPHiN149kNzMHiiJskwLZ4lyKfF195bzPcH2HNpZOljFsXF7rBkUCIKC2z6Lp9BuMchbKRIx0tuadRa8C9_8nb0ASNVrMIVbqDX3Of-ZhYnVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1SpqBera4EIevF-2KGl7ZtDk0c8oCApI2t7hD2htpKc9NNvm8AbBEJi2kJdcHXaxuJwtuWw4wNLYNfYA4avORiR5DJ9Gw0uG-K0Z8ajVn2ePaCVcUS8vp9rHJuaYh3QOIa-2mcl2OCfdFFPQiteJ9S7XzpnbLXRMgSgP9NN_hh5PYW1nt9dOFakklm9lV5WmO5OF5b0vq6pxZLfpsyMNmiRFeWPXoAhDCdJRJIXIvk0dORTjdKNC53-7WG0M6O974MKm6S11cVYqrCZKnkHw12pILnyga5tz1dbRL98xxSDm1IjUy1gcpBOWYH-Q1RSTB4GzXCA0bkHC_rbEgqrng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awv-6uhc0bEQVLomJd4j1KpekzIThhs2HxPZtQWkyOsDaXRSbSYyKvJOqF6Y4X0nadPFj-hhqVniDFIToEc1sF4w-AqgUNBtt7IvoSw0knIHqMLX_uIfLuptY0UQIF7mJISDrePZRpvEtosldXLLnJsR3fRH_aBFXEdq_vLwguek54BJGF-DjNFmQwTidr_3m3cNqgZFUZK-2o8PcZOPsfI0e21CqXZiq1IsWAlMtkUzao9Vvd6css2W-Ny90nnSBoPSp58Yw3AchBB-Zr7_JRFSF8UzGo3IPJwwa7H4D_5-DnEW62ZKFzv-aprfHTWzoR2T2E6jP01fPlGlnJFHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDkaInKMcOagtHapGq4q4SeTv6a6ky2_-0AW-_wQ_BD40s7G5mbiDEh6hkB3263oZptRlEtLIcFpujcWs0JwEs1A5_3ON8rXaxbEyQaey8AmOH815h7wNE6HuCdqQc9egeSHN1OUg_M9gOF_TCm4u8v5FnUP0WAQnScNwsN1oxAOWueZxLq6O8wHcmq3AaywZB752DayyO4h8diwh4U8ZP9L0C_a6kAzMe9TjlaELwd7Bjx8M1YH-N0MVia87wKvBYJHFmtM5hfa8jtFASzgn8r7i1sFnZndiKNI6ZzMqifKOum52uRpYYPdLta2KDJuwsfyR28KIUZn6-SKQ3crjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxc6Qqb8uI1X3teUNB_KjBnAvE36hiN9h0rlgIkfdLITHhu9dJ5Rbgf-KX-CVrCIOnEzLQCv_jHOxRch6tmXtRAud3kc-N8QUEyEhBHHxwGq1OpDUDB9iw-tBmM0Ub-oQ4gnz0qXb2w0__1rZ_TknQ_xOOypH2j4U73le3eMVAvDD-z_4MMO0HqLuWNafgbndltANn4jMnJVK-bWx7S3zIMU_Dmvf53M5j_mE_jZVT1-WKwyuD6vgr_GmMUcOclTEd9kiK49v9u2518i5446PlcAhVqQPHS0n3Zn_7zD7o4nK6pV_CFeE7RLT50kIwdMfcPHpuadXgBbIdyxAylTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDbZ4AWmTeQDeDnV7JhFj0usSZbsBSuhqw6QRTICcEWxQNuUTlp8oaRSbmxPNmHE94Sbj-IKSN8OXP1fx_Y8ZbXQR03SSbYzkh3kM5SIbYF9i4II7MPfWMokTauaE-lwtrzNNil6YQ5LsU0yB0b862HzyEgetDCxegOqGfFMnX0EC344w0I5J-YetJawwa1Iv6qNLwGJu9_SsqPI3qrPE8DmzC7OPQpbQqZIYJiHnyPKcrfTru0Gsm-gtPznhSMzzX-BlX7tcdhepIifEf9xePGwpkSMQPKoVLQd8ZJc3rN-CAwmRe472JqQAiOfhdNiQRklUg48l2Kl2-zL8Ps9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNka7Kg_axoq9JLMkCMtw1G4aGkP6QElJNtzKffUiEk46rzBN1jDSPriYm2qqmXKiZEZuyhjpVdhufVyF4wz68_nUrK-eQQlZOu3WZbHNGPmvFM2Do-Rl6IsvOoQAlVAfS2hrb25kvVVSxu4JlwxJsAkPpDXueXeHXmkSqGSywFUnuOa_s51dgt-DoBCP3aQs-NyqIcOQESbeNpyI_s9l6rVUSfXhHC2BeVlMJG47y4yLI3xGpTEoajcDow3hVH_rB7EIZWb7vsyt-DKsZQtjQ3nBc8NE58uuvFwJMzNy39MvwWHhYyszNDn10bki7Gmb9y94MOWRCAYNJDFJs8uhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0lSlnqF3FjyIARmyMmdpnbJdmj4XDY45ht8BJjcgtWrE59FA8kzMd-IpmaJFoXklVfk4TrU2LiREZa5jNozk2AkVOL0PUcGqMbheVi2PX8bbO7M6R26ySqj3JYQ7cVVJmJ_h3iTusD2rZfN0-oZuxRRpuOxoo_yjqCmKneiYiq0l3Tvs_18ttUffiOqPqE4191KrlKvewnwLpKaPcRb49lM0UKfhzZi548hy5VtJDvM_xN7bt_GxX_K0FKJlfBM-Fj2gyEQJ-G15rxo6fhzDcoyXMwwPsvIRThoMiInnS6-19MH0hdjKVYrcFiQ-lmbMydAAjk1sqpOYyNKSMBTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSpaCUvQ2M_zoeHt17k0R3b6MG3TveRJm78Ppe57jtVPWwl4e5sGqrtdHauksUdHLKQZSMojXnzMV8TPSrja1Z84zTVwh3NsF8ViTSyTDOmpLAr8SfI_U3IuK8YNLbpjSmxkktocPlWoN5oL3EdHZ5Xw-SUMs3GnCFxLEeu77mmkdrGAQ-bzt9xkrbtz3Bs5OoPF6SW09sO2aqE0tSN6IFRrdw82bRLbPxfTcJzyqir30byzbj6txnO_fWN7D1vvhODhkG6jtwZEbD9IGrvgzmB5ikyX_1ZBLWZgVr26xo7P8D3v8-rr6ar_whylP3VUBMG-e53xLIkGjg84X8vGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=WLNHHvkQU1itIOmYwNU7n5E55FEAVPcxdmhr0KkOCIkRuibjB5zSV5KGWlHn0smfzbyXhJYe7yUArtqzZWHmAvX4y3Kmx9ENqTjZCyvO1RsCEjAZQKfs-bJG1BGHu76fePp7MLFIf5QP4tPnQz66mzkHdKed_FABpQ8es_lJvyd7Wq2SPM9rOBxtdlRBx5fgbvw_FtAsNd-fNT-K_8cFOxEEZISikTF25YTOF_ZjJEpDXCosjCYpSctNOdXRRm1OM8Efix_M_FlVgr9ctznN647IDQZyH5boT8IfdQI4VnCzllhJH_Fk9VIlO8oXzEX2goCsX5S3sON_9yXBBsqoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=WLNHHvkQU1itIOmYwNU7n5E55FEAVPcxdmhr0KkOCIkRuibjB5zSV5KGWlHn0smfzbyXhJYe7yUArtqzZWHmAvX4y3Kmx9ENqTjZCyvO1RsCEjAZQKfs-bJG1BGHu76fePp7MLFIf5QP4tPnQz66mzkHdKed_FABpQ8es_lJvyd7Wq2SPM9rOBxtdlRBx5fgbvw_FtAsNd-fNT-K_8cFOxEEZISikTF25YTOF_ZjJEpDXCosjCYpSctNOdXRRm1OM8Efix_M_FlVgr9ctznN647IDQZyH5boT8IfdQI4VnCzllhJH_Fk9VIlO8oXzEX2goCsX5S3sON_9yXBBsqoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=qMZZABu90wCam5PlVgcgaYGhy8kjLjwsZvQ2OhoH7vlamr8B3WqhdjlG_KfBTuOYPSWTi91ed4M_ZtWQCgteP52c00oC-KDx86ABJnDNMpGVQIIcrCH-CR77Is2XsyNThhBkRbDvZlAAGJEoIJpLN_eE3K7WhMr4T_o9Nf4IhnmmLFD0icHbN2cDHfZdWMOMHwbKhmt9GdKStFjfNZDwUg74eDnliD1Sj93OFxkB7VrxX5S79RP9t_gwOBOW3RcKgK7lcoIEP5MjfDXz0mSL4ZfCH5uXN4xGQlaGVhiKl3TppsztgP3W-pvIhUE7XLVoJSOiqgi7O9ucjH8_peD1bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=qMZZABu90wCam5PlVgcgaYGhy8kjLjwsZvQ2OhoH7vlamr8B3WqhdjlG_KfBTuOYPSWTi91ed4M_ZtWQCgteP52c00oC-KDx86ABJnDNMpGVQIIcrCH-CR77Is2XsyNThhBkRbDvZlAAGJEoIJpLN_eE3K7WhMr4T_o9Nf4IhnmmLFD0icHbN2cDHfZdWMOMHwbKhmt9GdKStFjfNZDwUg74eDnliD1Sj93OFxkB7VrxX5S79RP9t_gwOBOW3RcKgK7lcoIEP5MjfDXz0mSL4ZfCH5uXN4xGQlaGVhiKl3TppsztgP3W-pvIhUE7XLVoJSOiqgi7O9ucjH8_peD1bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq09UYlr5608OCJlM2p0LrGS_N9n2iahbAuJCTYVxljTmD4jf2J8NSMGSaq1YU_YsA6Iz69ya_WGwHrK6gkfmUlGfdZJE99wD8Hs4wQ9B1lqCwzB-YYfa2pDlPR7XFSlFhHJ5qBIC91QpzoL1eVJ7tVPgldUIwQgfH18Z6lToLefIi_h0vLtXPpRd8PN5_ntqPrEMYfKjaPuWXfk1ceCfKnAJTDQXQ_6hwLbSFHjXnegdMtEhI01e3fGrKNVYmeZjitfMAR2PiViutPTVy6Fc3N8QIZMiSkiCxmmhRW9Eb2V5FgseyVzN1NTYednWwzZrfIQfRj2DrD7kn3BoJYU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5yTCdd0GXsjJs-HckGR03fxE3_gseXBrI045_rmFTMaG8Yyca4cZVyYtc7Hx6WIrcHTf6TOrrpB_bEtR46Hf7AB0TZYUhujZGZeyQzYAN6thQV2N90T9fx1aWt4styBhlkmTbR6ZH0Y9LszqMJdwkbl8QaSXWf5rwvzXKd72Zxt4nMXGFg0cGmqdXVItr5fy2Kj2EH74CLk7qwmvjWi6Glskv4Qb2N5UQYrS1Gzc6IDQtQJqEOOBGf2vQDnbnOD1-2ZpkBY3KgY6XvVcCoFVSX7BLQQQ7GSrhvIqv51axwT2srUJv_3Z59txc9WfDJz4WMQ3uY8cvsfGJq-YuTrHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF4OFIHu6u7NgUw-xyaKsIuHB6Rg4jF6wQolxskwg_bXQ9-Onvl5ZEinpGbOML8_G_Szba1DL3RItk4vCYAFkaRQr_C7AWgNIbcbsjxxuPucqogelC1Bd9-e6GO8FbN_tdpNPLD6ty6-1RovBCAfaqSXTZb8lfux_SxWWa_BdnpFxdnsuorw9mbSr-h4ZdpAywwIJ4ZMk37HR1suqQRvkxt_sree1NdRPF4vmZaXPtIev75dctaNPRvaEwAZSZKrmv7-1zN4TsNWOWJsbQ9WmKyAOJFeQSqXUvUdBrkLuuixOwTmVQZpnjaCpd5KuKb8enr-ynlAwVlvaqu0YjB6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=eu4COrXHflhbUrmxKjkamf5X1QTMI5sCv9TI2uP4VoEbvNJJjWw9OzrP62VWmm_eeGwsfkFg3bSInwZk2rlJL1BSqn6-LUsOI-HUlXR5884jffoPzZvkGjy3WJmboExzO2-2uKByFB9bv4MGZ6mPVe3MYfNIKndrAwIbZClXq9wcsjHRna0lks9AbnaEbAZmzLYqV9a2FWlPOD8UpnOsxtkr-9Mli0oTu7h5aJNDcHLhymC5pw9LkiokTmaNWFSEJz4z3jkv5CExVSTzTjAzr81UzSocoqN90hpIUNkHTsfSHI22U971ReTnkxe6M5K6IwCX8RaTO0L0Vj9T5dUdzqTo3TTn3prKRT_m7UIjhXDU3j30auH4TZf_sGdYmhu-d5qVFSfNHu3DKLJT9QYm7OunTd3KuLPBTqw-UVhWCj9XxS46-dMHfRsFQ6479wuIwDjJwtl3Iusqq4VS1sIlaIqxhiwpPutEMMS_BwG9DbadjJ6-woFjhf2_Xd4SSKFQlG-xq8hP9DhK5lPihRc35cx5p-T60VIHCOvIbhITHHc5CjyTobGte9muXgXg6t2V1DLUnLxqdkVf83OYCwPCxpsMC96IWfNJkB1o-vUzGrxyA-vzth_809t8NfZS3ey4PFTYdQWuVSkG_4Fe4Tk7WKVtgttJdJgVRnbPEdwEftA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=eu4COrXHflhbUrmxKjkamf5X1QTMI5sCv9TI2uP4VoEbvNJJjWw9OzrP62VWmm_eeGwsfkFg3bSInwZk2rlJL1BSqn6-LUsOI-HUlXR5884jffoPzZvkGjy3WJmboExzO2-2uKByFB9bv4MGZ6mPVe3MYfNIKndrAwIbZClXq9wcsjHRna0lks9AbnaEbAZmzLYqV9a2FWlPOD8UpnOsxtkr-9Mli0oTu7h5aJNDcHLhymC5pw9LkiokTmaNWFSEJz4z3jkv5CExVSTzTjAzr81UzSocoqN90hpIUNkHTsfSHI22U971ReTnkxe6M5K6IwCX8RaTO0L0Vj9T5dUdzqTo3TTn3prKRT_m7UIjhXDU3j30auH4TZf_sGdYmhu-d5qVFSfNHu3DKLJT9QYm7OunTd3KuLPBTqw-UVhWCj9XxS46-dMHfRsFQ6479wuIwDjJwtl3Iusqq4VS1sIlaIqxhiwpPutEMMS_BwG9DbadjJ6-woFjhf2_Xd4SSKFQlG-xq8hP9DhK5lPihRc35cx5p-T60VIHCOvIbhITHHc5CjyTobGte9muXgXg6t2V1DLUnLxqdkVf83OYCwPCxpsMC96IWfNJkB1o-vUzGrxyA-vzth_809t8NfZS3ey4PFTYdQWuVSkG_4Fe4Tk7WKVtgttJdJgVRnbPEdwEftA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCRSuYy4CuNdQ-LDbSRqKEm0bqcT5BqMQTDFjtV_rFWXNHEHYvG847SviCJXFKv-YGzfhXB-l4N3KoONicszlYgTv9AE1aUe83bSjnxLkMPN4qjI1K_MeoB7yeqHw_0vGFy5p4nfNpsS0TONwbEPjm5cYoSBrrbqrtvbAonWoCccMe3IN1WqJ2GPf7rL2nodxmXv1POtA7IrEs25aKVOr6m_hqpL7KIj_fjlbaUwFWWoEncpQUX3xIQwJSOlt80f-oR-pmChtDFntXRvHDULHOQoqLAgue0f3OpBWEgsGphb2lxj75BSKA5l3SifpA81uR8bBgdVtpbLUUORVg12sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMAJiw72CH4sPCZpqj6r11MPdMq_hgeHKyzkWFLwnmk9gPK_-YO4A2FZLzqoAOLPdBDvIBW-uf-n4uw6GvLRtT_nzQTgw57z7tHDCwnQagmsjVb02oI71FoUw8AVXneisatdzuc3bk2XKYqeyz0LNiqQUQhIgQ5LJcOWnW28wunBkiYkh_CdmIIu2BUlquie2bdQuTtyPJKzUHorFIGT8hKxClZJ-uVVxTm2hIpGnonGH07usH6-NjqAGJQVjVkaTF5Gw-dx_S9TLGMnmXKizUxy0M8FH244U9L0fMzgppYyqr2XwicA3tDWLkx8MQUUq7ZsK-ULPcPQ7XpLew_Pjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v76eBUr6g_5Zy7mWa2VNU--tC1s5SF9n_YXbRRu6aH2cugH1Un5Ijk6dD6pnRFesmI-RTdNkUfsAOC8Iaaf3PCVcNgOKgZk7wlNsmaHj9Bkr1_tzIES5dD5lKBQDMd9xOLB2PuN6IIkJl3n8itb7Gs4SUa__owXVboaAqUMufKyhP9S9Ge9RU-E_KCqDqXgNdtVjkU9r0NdFVpTsbj2pU4Y_p5FOXqhxMU1drdcuy4kThnG1db-RSOzXdzRwBUj1SfQdLxnMN0Mb34dF6ln1QacLWVusxwhetCsnSbogP3zjR0Vg6BNjZGtD4WE2ma-ejU_cm7evaAhyRT8jzLZJ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPBd5hNAOwogrxcfTcF3z91Tx5gV3QrmkuogwJvqtY3VHwx5V58jkMgkgSsRHcR2k3By69mpIdLPaZYZWSU9cAxuYMhoRsoKMKKtRlfNVDvR38rqGCtPlcgcSEi_HND6QP882QCqx1ooCw84505P6J_WNknEL5eKjaaKTzBLePPzFj0ZzZeQncJk5_-u8wQxAmFLToOvQKMmiIz5uHBbTCgy14u9ExPpaMhb86wKFPAORl8TNQs43n3XiK2D64KOeaRjoXCrvcUfKsKxYlJ-Ket5xSDEFFh78YEO8QNkLnT4eIgXuV9cpYvQUx8DRn6SBtXSmzXLmmDLAa8sF-FC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRYMGCL7d0T0kA1BFSWs5m_CuGFDKuf__kk1R6cwkOJQFO63eRRbFWaESr0tIWkCw6sYWfIxAU6AcNz8U8xnO-Z3Vx97u3B-y7GxQadYXIKieAMwY-242Os89OmVhOogmJwI76fyhD9ER0SYv78Q5yYN6r5DQmhe3yWXiD9EwhDqWhKzk_PXMqtpOYSqXBgIypmwloWmpp1g7jTbO1h7OjmmYQMDR--hT8HrHG5Hn_czcFmqA2IoY90qUWomYESiQYq8K4ngTkDLkBcC1oTrCpbRkfWv8RXS9nypfuVdz0jiP6g-FUXyNei1hLjJPhcwBJeMT0mPGJTqWOjskGXDqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8VhTcVwwGT3eWaprX5hitrEckH90ROoeqt5_DV7ZgPHjv7Vzo7-ENij9WUcpSsZsISXJm3TCFD_mfGR5hRSCK6ZR5h675e3m-DlVBgCG3xhrIotinlVQ45RjaebI9EB5ykPxqcMoFnvH64tUrW8_zww5HJ-HYhlSmzptKVklDNF9qRccP6M7o_OIy8v4CkvWoD3VaSRLAnsHFGDoPWqgXx6UJ_oZPuGGFpu5YyPelR391jpfiicHlbt4XJv9HQsPOWbU1QHT8vjt6VwLar_ck0rSpCbw62NqH3UbC4oRHbWNaUXd7A4EqlULTXEY7oKc6fcD1wYEHoROqkJ36WTdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=vnZuaxZ6aiCoSxHG7FduvZR5TChNQ8gjm1SKaq8W9bMB_9ioeSatnuM3-MbUDoBeVer46cwLub8uS3Wlf2wWRYop5K3Tqen5VsiVDEpmcoDQxCP4dV4E0InKEUV3GnKiWKkZGHAOh6ehm4c8IxorMTh8Qc4VWUk6DBCjxXhjyt0Qpl6uSq-Odydc99ZHXoHmIYkYABkjT4I1M1a-DX0qOa-lT-JwHbkkPXJNaT3NiVudcaq32j5r1nQhImF1nl-GOpUyduNZWSv76dOI7M1EoT7-lWPijNzQH7n7JlHOvyCx_LU9gK7TIgY7nHF1B3fUxWjNz318Wo-JlcUKyM2MqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=vnZuaxZ6aiCoSxHG7FduvZR5TChNQ8gjm1SKaq8W9bMB_9ioeSatnuM3-MbUDoBeVer46cwLub8uS3Wlf2wWRYop5K3Tqen5VsiVDEpmcoDQxCP4dV4E0InKEUV3GnKiWKkZGHAOh6ehm4c8IxorMTh8Qc4VWUk6DBCjxXhjyt0Qpl6uSq-Odydc99ZHXoHmIYkYABkjT4I1M1a-DX0qOa-lT-JwHbkkPXJNaT3NiVudcaq32j5r1nQhImF1nl-GOpUyduNZWSv76dOI7M1EoT7-lWPijNzQH7n7JlHOvyCx_LU9gK7TIgY7nHF1B3fUxWjNz318Wo-JlcUKyM2MqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aqt-bofxz_VmqHlv24IPKsd_Ljj_-A5R4m8SYrTTI9ngr0R13wICHdVb0WaD3JBgfB15GmlXB1sdk61EVI1IpFFr4NW8LQ582oDHKXoopq1nNIxE-3zLJDCTh_dCtKlEhf3hmz7A4gu4Jxnpt92f1KA5OR5uJZnrIJeMlCLFyyw-b7strpnhdD1zvi0qN93LydaOTuzRSaKX3jI_M_RT6Qiy3Thh_B5qVbBHgmwVmNjWNuQOT0_PxVGrmLLOT5fVWwmdfMWkZkgWPBZPpOoqmU1Pv96rBCkuAmbK4cSbni9IzGjE9m_YTanUW5Amtbl0cNzW97fSZolsLLkBW9J6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaMdoIY1mMl1r6VAbrAHeNyEpp42SB4vLtr4ZQ9JDnVLgeB5llN2wYq4hU4vlbVLqWjV7Z9lcJrXaydIIdDorSDUwAjyRwscwm4iiLM86GNhp9kNQAFzo1Lo4QqZfrbdQGH3CjxSRgBe770L8BR5MP0yK0OzPQVy7FeI92o_HWFjDapWMXr_EneGPKQor71kOwIW-pcEp8HR1DtAyXSM3dD04CdzN6WrbR5cDOsVJHlm_2NHkZsbSGcl_VuzZd_DMGY95UoHr_Ne2jXUsvWu6QzKbsCI6Rdy1QYD8S_nrAEXnOM_nWufyOCScr4hC5GyPAhZKOJKZ72T8S4UD9KtrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTPsBXT69sq5KpUfzgKLjngYX0sgCpaJIw66QaGKLraEx1EOy7d9NRLdNWgOY1HRyOAx5CMywSCtmciprPFj40oEkqUNrmzn5hagO6HjsScXtbU8enuLlvh0YfXtdlooHWGLPXwp2LJlqEvcxkmzgS2adpI4Jw_BaoVVV5ClGmSdXC1is75hWH8r8_x-wgt3yIZt79BAOnPzF39Fx1xBNtl9hbH6MYi9UoDMrN-YwwoyBLbTHmuwMUAK8UX0HVVoQgKLJ0uv154z7NguKlkYku5ehlW4Pup1OW2-9YaD_MSRw1LVcFIV2svvDkBfRiYSdndQ_OwWXrtkt0vjbIJlMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sezur2rvIWT1QcI8mvxktrX1OKXCg_bgryLAfJyzV0vLXaEXiEIotKqk39qoRRZNB8eP_rkpcu0vHAI3dtuGalE3ydUt0m85bMabqqcRrzzJtT3DUn2lLxauUt0hJqcImR8vy4HxlbaTZIzVlaZ77lv4qbqFGZH4zPd0qCBAPgIc7wWq-ZeWMAmvxeXd-fwpAZl3mQ8rA32CRb6fkKoVOdho9QrY8KbWQwMn7tl_j_mBAMTCmpocnRyL5DeFGZtO_BsBEQXiUzDCQ96A65xCWc95ayCR71S3CadsLs6HLtUexxDQH7WBHk92pnq5OLDwjHlJ-GwG0e1nP-JzrqUwww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 میلیون توکن برای دسترسی به API هوش منصوعی زیر
💥
🆓
Deepseek V4 Flash 0731 | Kimi k2.6 | MiniMax M2.7
✅
📌
Base URL :
https://hskyauefqcgbvgvxkluj.supabase.co/functions/v1/gonka
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTcvNGJH21XXH25jDpOe_ursod-X_yJ6qy9pnOgEoxVT0Jzb2ecyIB1oFTCgyKjevCYv0JgZzvwfP42Qw5RFMFcM-2Gq1-It2LZf-zjJLjD_AGu3AoYU4JqU63m7yGKXd_1--2qb25ekwjJVDDgPjjoEO1YacoWVC4feW-UQ9xPZ6sns1KE8eWJOFAC1syglRpFTnFa4sFQ5eVtFcsDGnvOJaeBZ-HqoDU73_O4M3w-PaJx7aQprQ4V7HyzmX2XhTF6YbpEcEj7Q5QW1GkBwJ1Pd1YPirudGWVyKtuQmuXzGDMUXkZpd2NpuZs_7u4E0RQt1L4F8TkA0ZLuOD30f4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwMRqqi_nnoFtMCcN2OKRFm3VO9mkd0bgvaKTCF7Bch_dyXpmir9bkxm8VRQ9k2u-yvsdrQhgpFZCMOOKgGmdet9Oi_Wb7jZfefq4jHm7QF-LAzuqTzcDmhRXY7swHMXV5po8bYellED1xT_9tSmlICnltHp86vAP51Y_h1qZecgiuLt9IktxYupy0T3fR28L_goOOCTdCQOzymuEoxFSougzCduYEpm6JftnbAtwkAv3bnZyTvrxAFxW4d7-M4j5ghiwpHMh1paOVvoyzSOak_4LOF6i6Er50dRUzj6FuRlPzSdDiRpJlcw0NvzFZoHr9hXv02pkjAqpW9BHXedTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
