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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 16:29:26</div>
<hr>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6yyijCPMJs43eijmZxgy7RBL3OO0LKgRE_RyVa12dkyZkYe6untbcTIFYpOYt2H2M_K6deSD_lmtI7bXCbmpp5AM97jHKmNlVUu-K4K1VJq5F9TbLuwtGNgYojhbAqdZpl7t1ZVvwQtoev3nQMkBmb9PLeXnsv4zIgWx0W4JAXAMI58z7aCmInhVuM75w7S-Bmzxd_e4-lfwFOVhA3KQYu386OfTXhAa1CufURGLBDg6-uOCYX-u94KGi1VbRkIyvdQnUVrHFS-v3p9uMhOdvjnct_5wmFk_7FpuKKvpRAOZMyagdYa2QarXnpXb0cbWiq0rx5Q0oepb0O-Vqyi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 574 · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 689 · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is4lRS31TFv6ZsI0XxbT4p8GmP6yYH1kp-O0rbYxXHSa0rLHDvDF8UxqxTHIH35cEo-IHqEncTj5ItSAKyEqdzVRCswMPT0W1HfVY1vB2_E-maFaapYKlKbeSpOr7xD5rMn81etLkUNNyofpRFjnI9ZmYHyKXFXY2k12fmrs8W7pDVmliK5-EQ2dM9HqdQ2TeNXfjrs_Tz_Ti1huqU0B3lTojxumtlUz3cfguUUMAskL_Ef__s_JiqzBfO9h85v2FzpMXv_0DzAfOIq5SJiqK-36mxw9noyo6Wmm-tNKfzJwZL8Ji2CbtITbznlaXhrFcDvBWjlm-wHyril3TtvJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfzEKEOMtVC0JqRIThOQjbRO-BJ31hozbtHxUhH-7YB6hsiD-z4vXxTkkOjhCe0V6Dv2K4wlnPpnWpb52yUPmPhxY3kMddioIk1VxwUG5TAsXAWHvOzgvzyfiLIG57-ZNzoOuFRptOFZz54gdFSpwZMyAV-MBgZw_VPYKJOKaywJV3UZ9ig0VbAvkB7tbAGl9Fu6c8bzK7WltPx1hkXjnXtc5iyaRmC1PPpOZAvplZPrDE5U_I-FWWPsmVYb35ZS3bmS6r8if-W9fQI4cqKNtxry3HY9VjgUACI-MPIqi9BWnQW0pXCbu_o6j3hVDFaJG_e_g7IPhfzFDCMFe6VZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEn5M1L7UFjOYqsZT3278W-eWAbPj0N4FrrPxDNNiiRRAOAYk0hQ3KXpz0ycREJlOKm1PFHJQvDLE1KKNngeOuKXfi1dtdw0j9V0WBA5Nhu1CVRiOuWLjnnZWZDl3J7mflRvQSDAovFal-9D9FnlwlNkwoPK8FNOvj21XCBym3rPmh6kMI_jbPQOz3UvHGY5JALRfxw1bgcxQMsgwdUUoyMPpeyJbugfn27iOMnHM1oIrgIa1qoxW2rMDiry0pzsU9Gf6RuNbkARRvxQfWcvgcxpUj9hPr_xN8BUW7XxZz4PZziIb4pg2fjwxMWwD-VxKwLlpRxyDqT60XZpGfG1yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW0cXenF4RGDdYuiLEEbylBNtTCh0TepKDiuOx5Slo4aljcbknjGphmFo8rHVbuLCePi503vdQBRxgRBV4PxeVymKg-3benci7nC3M4VinOJ1_ENA9_l3N2re4xYbX8H74GUlu_NQsyuwEYqr_VSgf3d2aCxN_BqvNCG55QPQMWEL_TFOJMgE3p-GGxycuVO_GMPKtWb_84tC2Y_QuLF3_f5jQTn4ABNcpyCoMbH99DxgYe-buZyykvcsLXKAqe_xjt4dZ5nnPk33EyHbiCp8mbr6HrpwqAXvSvWfUIc8TEY5lU2vviteh-mSfh7uIz4imyvEkoGePxVYF9XswDjXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5JpVTrNmu9EBTDrhKkXP47zK0wCsbo4uZ-z6CRuV2lDntJExJxaAa_su49m3wNZ3kiRaD9p8MmdcYf0EWEGn0zHTriiDt2N4wBnAl-0QqiPa-4k6DHVyGDeTV_OAFhRf97YOpp-GVZHum_SXW4-ROQ5KjZFN-rvI5RSQo43LuGdKWTxOZhaThIaSH0kEAQRSHciNGrF-EysjMtpVisu3-qCYRupRJhEmVp69oySNq2YT-Dp4RmVDjWCMyq0zy0-KQ_vZVdVmeMvB8eHQYptxkUkKK79TXcIa_TNgKPTcMrANX8vjy6pUMjDUZICnHNHBHDbAWsXtNZsWYY_V5vtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrZnZAaOaR40EiSkAnVw3F99AA-gm2JR2aS1_A4VWVgsB8jIrgtJ3unllC_7JbJ2O2wsc7k0I27tyXkksC5k7waLhTT8HPdcDCnxOqu7mal4laDIY3_UAl22qcuZYki5DhhKsctscbt7v52-cXZyoPkOWeTbbUvZ2dmeB8ikDna2G9P_s1DrNO_ic3gP-iFo01OkmsmfOxMUsKx1JBt8Yu3l8IcM1yBKpnlewvNRG3d8PKqYpREOfI4Nv8GMy9SlKqmBAqPObkIsvc4Kf4f5i0wfuAzJQtiHNPL86qa3lOL3wRN9N9VUip1zVJ1zGqVXs6_J16_QZQdECC0vsBLECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=nHWavLCGGwy1-2eCNjgapXEK4mDpsYLO0S8Mu6JDHMlqFVUzQVbtY2kyUw2LQEIC6_sNIh9KMst3AE6O5zFUefmZK846iyG21HbDub-Xfjg7RatvqTDj83zUCZmHStaVY6hD3k6p3hbSScbiVfsjkje7MOD5ClIa3qbTFdo3qmpsjHErmjKzEh7wDYnP_1Pi1Vd4nirULbVoEsLpWVxQTNJ5oh1KihsKMOjWi-vzBghTfr1cxFMUVowJDtaFyIPjIY9YedkmgLIczDu60r9Xbq65SnOPzI9Mwo7LwZAkve1HfcLzgCh_vv4UacjUGlt7eUVEGHAeTcBZEnip1uKWzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=nHWavLCGGwy1-2eCNjgapXEK4mDpsYLO0S8Mu6JDHMlqFVUzQVbtY2kyUw2LQEIC6_sNIh9KMst3AE6O5zFUefmZK846iyG21HbDub-Xfjg7RatvqTDj83zUCZmHStaVY6hD3k6p3hbSScbiVfsjkje7MOD5ClIa3qbTFdo3qmpsjHErmjKzEh7wDYnP_1Pi1Vd4nirULbVoEsLpWVxQTNJ5oh1KihsKMOjWi-vzBghTfr1cxFMUVowJDtaFyIPjIY9YedkmgLIczDu60r9Xbq65SnOPzI9Mwo7LwZAkve1HfcLzgCh_vv4UacjUGlt7eUVEGHAeTcBZEnip1uKWzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=dC-MbcPtbwpUbsN7ZRUWyQwODbmefVpmCAR9sreXvPs5EfkqJkM92crAHavjhorErSjK3wj7-A4DKHCLNNLNFHcgcVAuiJUMN39-he2eqrUtNxHL1OQSnvc2KJ7LwgKDQ5TUXt0jJe0ubVBjxc4ffv4FfialpxgKTiXa_5QN6c279uUujn7NHWebYfA5HrVSNqmkzcJA_zHx9A91Fz_4_PssIPnIoqKyhBWUjLB6iqAvFt8zMO6Ya9sRQot0B2vly4RqKAZOKwEGhnjge5lav8DO9i5N5CZu7NvWf--dtyoGaojom2WdIExF7D0N2di_tp5Qy1zuxcoZ_qVr2EWvUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=dC-MbcPtbwpUbsN7ZRUWyQwODbmefVpmCAR9sreXvPs5EfkqJkM92crAHavjhorErSjK3wj7-A4DKHCLNNLNFHcgcVAuiJUMN39-he2eqrUtNxHL1OQSnvc2KJ7LwgKDQ5TUXt0jJe0ubVBjxc4ffv4FfialpxgKTiXa_5QN6c279uUujn7NHWebYfA5HrVSNqmkzcJA_zHx9A91Fz_4_PssIPnIoqKyhBWUjLB6iqAvFt8zMO6Ya9sRQot0B2vly4RqKAZOKwEGhnjge5lav8DO9i5N5CZu7NvWf--dtyoGaojom2WdIExF7D0N2di_tp5Qy1zuxcoZ_qVr2EWvUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1ifJ8uBiyeCfBC69WijJs2J3Wt8bml8Yd8Bjgrj1_nEsp8GPyK3rCQNPUl1oPkjkAr7vNGrtY0JkY5bWGe4Hu-1g7wDtccGOx75c6_qDpqriFtCcNiDUBX0HmYwY0JK-vpnpIJCUp2OeZeju8JKnmzrcnltNUFIJXsjx-VJzghHrPzFgd6zvs2Ncyy2RHTUg4P80VSWGWpGEtsbN12R0-2dQKZwKMPrym7W_oI9J1xTgHIaPC6Nf4JsjZokEneN5ZOxjd9RNmkfCmv2ekll1JQPCe8ihpTsXB3IxGSVLgErPbyF37HYj_XDmOvVrrBsI2WwREn2mUp_zHanPmLZuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=NWa8E9TnDCGVoMbd2cHHKrcv5LDArN-eSNJAIKyn2N5QSn1Y8vn1Mts7zxQ7I-xhrYHDf4JOu_Y7xXtD8XKGi8yMTAs_nVqrRhvuXppbPdiiCKBV8-vnOh3bCYmtCspcpFLllR9iQqLZONxVUFgAR4YwJd4oRa7W9Y7YfHyOd22ePVwQInuNSj2WonlN6TWfpQoeL-lCRNz2iDJmQa31fWDF6OrykQ4XrpV9TtZm9TeKpQN6a-AOyGW9u9MUDazMzSqseRgCnjceer0FIpsppFoYZYP5T5rx5bN8b6yKeF1xiLFmeR8vBdUb8zIgXABo_e-YUh033rRUNTDp7x0wqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=NWa8E9TnDCGVoMbd2cHHKrcv5LDArN-eSNJAIKyn2N5QSn1Y8vn1Mts7zxQ7I-xhrYHDf4JOu_Y7xXtD8XKGi8yMTAs_nVqrRhvuXppbPdiiCKBV8-vnOh3bCYmtCspcpFLllR9iQqLZONxVUFgAR4YwJd4oRa7W9Y7YfHyOd22ePVwQInuNSj2WonlN6TWfpQoeL-lCRNz2iDJmQa31fWDF6OrykQ4XrpV9TtZm9TeKpQN6a-AOyGW9u9MUDazMzSqseRgCnjceer0FIpsppFoYZYP5T5rx5bN8b6yKeF1xiLFmeR8vBdUb8zIgXABo_e-YUh033rRUNTDp7x0wqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOQo10lEb_TS70u8plPjWerO9jUpXYjS7W_CHJSsbAZyaPEa7z9Y_LaBgOVsTUkVetXJVvxpRLRq9m_niQocFhYved3gs_HPBE0WmWITe0Cbkh1ME9FH9aVhrO9NU3xHxcjPWyfGRrH7F8XYVN-gfqg-tjK38nzv8h4TI09tLSM_BoRxDyGKEHndQPDy66fZKVqDOi75dbNyCpbwOHf8mxboowlTYbdkaravpJn17ATyETLS0Pha7DpE_2ze0ZjzrMW9cEt0Q-SFdcANaDuSHIme1tASoXVRCvcxzlKelW_OTHJjWTgaSsoKgqwbdTb2X-eKOsxZjdOaRoK-CSpoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4NAIqytA9Pu3yCnqSsA3BzPV07BO5Y3empwt1Tg-X9A58cudITbbd9duhVXQrkWOTock3Bt88I4cR0NUL_SypHiflJ-Z5uDtx0yUttXqghPFLlTCrMxDDcsRnt14OOtrc1ZpHO7rhrgKoqHjPTm84NkSqQSRy5hGRDcDXHOr-BM1ycjs2x5kIRBS0R9w0Xc5bGVXv6Ezf-EpnriI2VRw9g_mtqUVBBKyjBKcB4QDb7lYj7xmH3AfDbSXzKI97iGc07MOQ76_qCHh3WvdMaER-SW24wX-6fLMcv13s2Czjq7bpxwcd4LUlmhwsx8AhgW2GIW2IUHWTSMyYaiUeRKRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcHHBNjZwsVYEdV2V6xsge_QbtJTrhHgU1uzMLIIvYsfY0VyXrt0BB7X4k2q-Kqjw4OJiPL73AL7_li8ZxjqpxQZYdUafNZXJYBt3Hk8JpOsZ9aKLB6v4Nm0-XU5HamhTnwLGjTglHp-9x4WeUqiGU7V6IYrJb4LTSS_MRoLQH-bIPco8ZSt6Gyd2m75V0sOtHLI-7iGwogCGCYqdltKFHtjHp8hFc6ERK6ZfDabtH220chR9L5memBvoCCPCoeZYYEChhtVFuNgF6oeVRpN6O4jNYq0-ibMMOHT77Dpg1CzHkmU3qT9W0hf_hN9iMeykgwTdp--KVQP1ZJH4Q2E4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXH2U1J4aQSLTyawM4uaBJxkJD-G4bXj8_jfbEN1X5A0d1-MoSPIEFxvgjHbjNOKuzkc5WCDPBM4n5CkGgsGlHagAtOTrsNAg-u4sQGMt7LRG4_QhhOGhHPul9E4L0f0nOU6Q5V6Gb6OsaD45AW4EfE2R6shXFwPF65X1ecDec4VH7R0pzHyp9H3IUF7QIZmg1D5vt29RijMNhf7HhVLv8wEtf6S3MLliIFMZs0iOMJksIziLbE4GwTEzuhG_JbERxvESyQR7nI1sATIB0XGsIAif8FF-StDy0MPnNtthRPZqMRWma8tOTsZ9cqgJ2CUG1AhPa8i52A9ytBr31TXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb8B8EyJO26aW68v-Iv2Y64aIeVJ7NNng0weQZPuf3W3yvLh9E6XFCd4T94elAPlevTSKlQEOYyRc8e_vRO2EDImdZye-4aOBRc7xCxsl9OYGAv4WYTXYJTFWVgS0nKbNf9tOWk8CcKPXMEPM8ekk3UJDuiHMIFsvPiFhz_1gEsjV9u5R6z9VqzgtI40l5IUSyCUuwoWAtwpL-4AYR4ZLxJjUweEqp_NV-37GeysrwBZhnxnZozT2QweVWb98e0oNkW_nKTgz0KJUicIPTgkJ8_axTa_ANFUohd6rrrnQ8ztL1Am9A_FoOcFya2_Oob655jSZXmFev3DrA4FFE5PRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCHvUggq1SluYrhccMLDb9ByTs0VIZy_-08fSz2cPaJCXYk6qYTSKPLJo1weMUJYsrnhAKNKHDG3QFrg_bUH2Ytts_xQ5rnoceCvPhAcg0b7dOwc9AEnE7mwV2cfHa0atJ3W-0QTdTwUOWy81_y6yAv9NIyf6K3X3kvrwAPPFtASj3r3xs45NyL0zc-wGlI0rqGhlR_XhyQ7A7VGLbDyRxa2VEGXIjU59GOdvtqtcMct9fr0AoWtGuqeFGN9A-247-C1tuS-OVORxeQbIjDVmyWonoQYDcMMG7rUbJTmNJDJkEJBiQ7hqYu5MUBrwMvBBSVBY66f0NzoZJew67-0lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNJxA1ZFnIAv9rmGFyazuMOBOyx80msdbBoqsvrc0SO8gTDhGcH9XdB9EEepdxZttMlANe2PawQ2XWT5XBqRHb9zniilkWRypP6QvPpmTMWUJqJZ2SniNfYD8PRb5ZZQQyaL7M6YX1jGyOkzCQ_AEAQ92Gj2acygk-WvhxovIiEHq5tsWrEGQwOJov2v6PnpdYP1WPtU_xzPRYlyr_pHJn96gP3N-wN5ntRhaUVZ59bR4l-CL3QKC7vkF5hRwFN2TtXkkWG-ihaDSNi1h1cuUh1oFkBBmOPX3V4CKDpNpA29erI0iGiTnl1Kb_iAF6Za3ntraVpY3tTtDTn5JF2btw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZCisRjayT54xGD9EnD-Y4r6BDzcqqlA0lLxLQLygOZ7k_X0VZSyWe4TsSye_vCpPBsbZUDY6ZIHWcSOqEoAObadBchYdpcNJZgCXmh3JlVJGiJVFjQgvyLxT2Mj_plM-PoRNS4EGG3oYHrOvy2rb9KtB-WdL1lMHRdXmIKReqm4Tdd9aM4QZDdfmTYFPq1kHlUk9PXvK-sW4gvgpw45Vtr7NXt5w7rZVY4ZPZrlUuZlI-x_w2nV-kl-fUjpG5rdyL3uncRNx03OEK3ydtivLdt2h0DURLHF-wpXI4dRhqPfzgrrRFGWUI7ZJxLs7XcyK2IbonsqZOV4SPzziWuTzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr3EQSV3mHWvHE2Y9SoZ2jhgtmkTFSdTfLIDRoH3LmwwyqedTCRwGiL0K05q5h5lyQIB70AwsDF_Ab_o3IBIK1E74kR2HESft27Fl_ZRJQ9rI62RocgN0LCC7rK5ApQd5F27VPX8kyzXFSiDMN4n3MsTjO-M9aZIZQFDqI6y7XYUW-8Qgulm9fkGsCqmp4dOvCorZa5ZS5t1DPDJiusBJjYsi7hyuqraQOTCisY0FA1xG933C440E_aGch7O_yxZF-4IQlDl7c4NhyDD17aVCF2fMK943qwnSIMPSthmiTRSthKqVOVagqoVRYD_IBC8XV_OpLsYHETf0OQQWgXFGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRnR2AXBtBSNnkOeafOOZrFK09KqC5g_yL_ReMB8jhLYBKuB_e4UUZKUuKjN5AJS3NM9ikRi0D1lzmt9iuiUjHs0CnsM8LHf3ct3FQUMc0ICnDL6F3EnXwsrQ7z1HaaIiXPnu6WbpCtJY6zXyrZUitlhsPyt-aG9Y3GckOHa7kEAUnQnOEIrgqPftKRVb58qL_ZC8Dl9dLWcVF5r94-h6QYsd3n9uiFxIGq0BCpHaBKa-Vn-hOEhWxbGwxTUNnizg92c_QdsRO_SSr7P6WIls08q4H_cI1b8UAm9bLkbWUuDumJqMRg0fghplhX0Ocad6pcMUp_pPggPyhoJUYT5bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN5_iFDv8OqWS_60c39A27hc6DcTLe6xMae5yoWyTNcjJwGoLJvw7zaiTMTrsRXJatn-T3jMyHDbtjsKd6gOXGKdsBIUhI5sn9pFPmrmVYQYPulqL6Z-B9WQ-2-Z6SMzk-zPM0SfXI6EvxvJc8iHnIJtbETGWZ4OiHXb5LnRpPPfDr7m3i8eM1P6_iFQgfSqJ16XdUSgc7Kx5QJZNW6XPEs9VyVxr45SnBe8tKDrjTF1sQae7bZ_u5zi525tvLJ5Qf6cMTeJVOx2yGAcgJgoqkNjdtAwAkXKRW7oqhGeJjmwdY7xO_cI0YQFQvly8q2eDrtCRdJkakuVSfa5QT6Apg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvmGFhtKDZTTo1BLPrKw-76w_7GMMkcLqdubQdUpIM3ukbHIGhKU9l_oCSdvtR1DIakQHte_8ls6aIutNDQDprTk7h4UgM8ceKsm-Sk1y5j9X9dNuhwA1rKtRMaXzcFJxXzo8rVZANOHomAHljfurv8lmNsGQvNk0dIPt_sImeCANuWYz-kezzDctYBOQwPwbs4qlmnEymzJYvnQbFEl9Do_jk6bX0X2WN2ybSsEg1S9aOubl1OXj5CoDgWrqBlYgCHSitptI7lpZwUKH_V9ZbSAXl3-YfPPrW13pALYjDIoVGbtZhQSJYsQB5DA0krwA9BWkYC6Ofz4vk2R6m_fUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=hm9VKiCcd4zWqJVd2_Yxwbpvp5zJXNObmVE6SwnV0Rl8LLj6sRBwbTXPNpfqkdFI6p4jcnxZoqL2xbNxVmd7isn6VLmr1_32WLEV1f8xaAbMgCyoqHODmu4CrSYssphLvfDAGj4f9EdA60bysdfSsFr0JkwonXGUCz_fXU4dprS-kHHvp3uv3oKrt7yfAT6aZqTmPJqtgCz1WHYZWaahyJqL-xMOM3L40-euTKOg3q0pzaDwCmhK5qIqlobqUThEx4Fk5MZjv50UDeYze4EtcAUUmSrhQtBmRZ-zCQHmKrKckvfyZKBb-n4J9Y1qR-va5efPmalNFRTjYPRT2JU8IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=hm9VKiCcd4zWqJVd2_Yxwbpvp5zJXNObmVE6SwnV0Rl8LLj6sRBwbTXPNpfqkdFI6p4jcnxZoqL2xbNxVmd7isn6VLmr1_32WLEV1f8xaAbMgCyoqHODmu4CrSYssphLvfDAGj4f9EdA60bysdfSsFr0JkwonXGUCz_fXU4dprS-kHHvp3uv3oKrt7yfAT6aZqTmPJqtgCz1WHYZWaahyJqL-xMOM3L40-euTKOg3q0pzaDwCmhK5qIqlobqUThEx4Fk5MZjv50UDeYze4EtcAUUmSrhQtBmRZ-zCQHmKrKckvfyZKBb-n4J9Y1qR-va5efPmalNFRTjYPRT2JU8IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxcaIbI-EiuXSINUyUAFg1jg5ZkhVOgCTk22wdZ4rfQfg4ql_UcKT0oT53utYHuUJpY7y-iG7a_J7ySmsGjLLmZzbyqaTJW5h9LGkTyDzHOwmlUO9dSwLAvwMzuvNoLhEh13m2emyH_fdndPy-QbOrkmlA7cZ-Q4vLSEOroin_93Pa73UNis7j4eJJjHq5540SzbO76YtgtXl6PyxjemKOUc9EqG_YgWkZWFBu7ZZRkAWeEI3U0seiqJD-xzTbFkjrfg40KWg11kjnjemWkCtTlA0MSs3wvv9tL8rd-Q8aiHeTMi3ruf-VjQ8zVRkCYYTH_07lCELROf3xKkWGS7FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=lCO1u3N61PmcTw9JUOtXWR8omR8T0UZMtQEM4Wfg1c35n-iB7MWvdnGvy1b9CZBpGdl5xHOUDjOqblbYWUd-QhNfqa688_vHzZ_EVI0JjyiUfQrsTkcdbURirLyrWXSkxsWqQT8po61jvtH6-X0IaPZyVltVH6TsB47YjH8q3DrN_q99GJjX_X-EHgDrJtZiTs0z5AV6zplxx4oEM7lW243D73SNB-4easZV0Vq_xWeyTvSggPouNl48kvuNZP-K_5wH5IWxm1NdU5qAUBVH4dLDLqXOYZYO5bD6zzPlNe42DfNlj7ApISeTctGxnlcSGaHrlPD6xpiMaxTnvW5LFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=lCO1u3N61PmcTw9JUOtXWR8omR8T0UZMtQEM4Wfg1c35n-iB7MWvdnGvy1b9CZBpGdl5xHOUDjOqblbYWUd-QhNfqa688_vHzZ_EVI0JjyiUfQrsTkcdbURirLyrWXSkxsWqQT8po61jvtH6-X0IaPZyVltVH6TsB47YjH8q3DrN_q99GJjX_X-EHgDrJtZiTs0z5AV6zplxx4oEM7lW243D73SNB-4easZV0Vq_xWeyTvSggPouNl48kvuNZP-K_5wH5IWxm1NdU5qAUBVH4dLDLqXOYZYO5bD6zzPlNe42DfNlj7ApISeTctGxnlcSGaHrlPD6xpiMaxTnvW5LFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv7Az7Z7gt2cnB3om-W6fB9UFwlyRTtRIp0YQ5ysRmlnqbZIOjkI2Qf_N3JdtY4hrjfgKaGBX04ebFbR8GpIGXDowUttq-xQgxIJ96Vooy0YI99_c-c_jbvshxIA31jpfUHOzg9zCuwf_cGu1EQON2beFzBUoYtip2h1iMNYFC_QF0OrDBaRZeg6ZIxGo7bcO-V2uHMxo3dPc_0SUfWLkt1JLV8Seo5qM_lC9RPXK5KLd4NWw6C8_0rdNrSQynERPbMPmhN7fWd9APiWHPSAm2GSqQ6qIh8mswKDZLIBoVSK7s1hVy9jA1-yjejal0yLP6iValtL0xv9Dk3JtgTn5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LydDnl0wdJeuKe7-V3UNmN0BegG0hDKGinvfXDc7o2BrxHNmg728SmsuTjG5jqfV4jZg1lJ9QWCtzyed4_soFAtyoMVLT1lsdnIrMW6Asbp9xTs6fZ7JKBjbAffLye_151xjDjtY0McWEN_-LifYInyYnpK6QMgt3deAmD8Qg3QQGOJmhl0LxusLPYuErAFjpux0dNd9lHhGwVZHs47XCm6p8Rt2kLK3KnEIuq3yBESMEKPG9dedbGf7sKyWO-T2juVqdXBtHA7cbEjaQGM2tfbG3rLtcnenMXebtR4gjvLOSayfpb0iFr7zu_CwZ3lfUcy2JDHtfjaXVEDqTCRSZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVLnGf2zPV3n9kmHpEZEz-GOdowMrossxyT4K-5qO10i3FwjrQxTC5m5HkHVWFNtXy7uujqpAi8Bh7YuoDcI6T4gTzQbY07Pewr4TH0n4pjml9ddysHygUSfSIlljdt5ag8o47aBfnI6XIBPdQlTrJ0M7IJNPb26Jpp2nv4vNB92yaxjxQ6mxUFLzue_oyfAXkXDk1M5hIJj7EYYDP-EZvyYNoPuJQZ74iRB3e_63dtQ_l5YzLvYDp1fAcTTxVL1JArsbJxxse9jFacDdOsefGZSfL9UThBwuscgsteFQ_qRKk6RGNGhBHhTdrHNHMJcjW2DYLQ5YUpDE0GPOjGy4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFFCDakPa44UvZ5PzTxuWGrNhegkh_wR6s9l212NbuMw17PYHs0ODIDBjGQtIR2ScufiVvbLbWEbYutVa5veElQpt0IayiHGAcDSbRPQzg4izrg9EMcGISffqNeflWWAn2zvRMQlhWhnrmkDKymroy5SiV7qnJvcMRoQN78-fLQLPgWHvTxPsvPKlOvnoLLVuZA_eByFJqQKtZXTf_eTGUBn9q2bs34yIWxftRr4RIPHiN149kNzMHiiJskwLZ4lyKfF195bzPcH2HNpZOljFsXF7rBkUCIKC2z6Lp9BuMchbKRIx0tuadRa8C9_8nb0ASNVrMIVbqDX3Of-ZhYnVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwCWP4AMvGZrHHNleDBEQ7M7Tx9f6FcHTJRoiKmdLeuDYu376mAiV57LUaDpLIIQUi6ZfL_AXV9l_epPDv6oZLOR9V3FGZKrtAJtvmNjQ3eEHa2TMmm4ukzfM8iDXJ3qvJRu4EA9aR7Eo2E3UainbqgWPa4XGOzfjIOXrS4HcdSj09jNoQjGTDLJbivi7asCkRbpSUA3FNihmnnG8jUXDwal0iaFDkjNATbJ5fAkcg68mZgl_m0GK-M8g1mtcqajrYDkv1bEUMuG0qUNKRPnPrT2c85evROMQRhRaj2D9GaXU9Z4GmQbI6p9TI4PXVRz_91QipFXslWqIzFFuBqcXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ3Vjo9r_FKN7ipU2CkwhoREuMXAdZCYQ_AR2zE-kBC5ro71-SJ_Tk8Xjk0t0775CDZ83ug7Y9RU24l843Izg3dNvbdoc-dfpC6Iauobh6vKfgET29sfcGLuwAMlYYBo5Bbpken0V70XE99RSMwU_wjhWwVf6-_UrQBjK0-qbduEKJX9pGwGGV_8cy-Me05B5lkOZWdGAU3P3aqn2nlMl0AQzk4mNrS_Ds32NDOZ1cIuLtZr7NMumCHUqTBSYg5yR6Jw9pc3BahPnQldH45_FbZf-uTvBZAecxMI9Rc_961EyvIdBJtAw8vJEAUs5hPyUSoing5-E4ULyIZFo1HY-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4TmmIG-GkvAnbm3AQjgcq8qbGdUQffDTahW2Z4-frmZ1mO3B-JDKG6YcK3xxipItw6Ry-VX0fv5J16Q4u5Jys6FzqzVNOETMOMBov8LlFHB8DRUNYDcxfBaZxDJetpXXAv57okuzeI0eQDF4gPIw-b17PW8RxAXZb5gQUxGFCANJxkw7uWno38NQ58zJX9Nj2AftcAJvYxtAW_O-A74pPaUTO2ctazaIm0beZcvDLp-A-zjezb_2YUMyCSTLxTRKIREbUfh6d2RmaREpTlkTjhPrPmVZKzCcYd1K_6RI3rL3cXn5WwgH2BIUpcP9cxbe02MUwZb4AnMbJyu-iCKbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKgWilkK-NrILr-iWBkXyOjLqrKTGv4PJwvG80WDp_1Qq8Tw_a1fPG11Ay9oPz_8ingrNBea7e5-J_wArvzc9pCLY-QnaPqypCqJAdsmjebDFVkpPbdtQOm2J6Pj3bmduJo_otpWVzmsguxSbqn0wify3KRkqxxuecDiB3qYx65XTpV0u6FG7Xz0ew3qA_ryFaPEe6sU0l-AWe_RZVsHFcFcVVeY1rMy5sJ1yIecuNwGaXAe4FVq_1DU0TmxyXsM-yi41R_1SGGonmlCsIYc4RF_eTdWDiuKwXYq_neimRjtx2oBKE15WwHlUbIw9EgzZQ2pr0EhHAh2gAnkvegq9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=M7XtimNHjkUnnNUF2W9USDLIuS5BbKHnP20kczaDHFrwcFFm9sbe997tn087hbtSrr5-UTXQuMg1RgUl0TrQwRJXZg6sFvX5NTqan0Esy0jlv4P8iFEw3jPJoluaec3WCNmPzAoICgHbUp-_1m3Ccrpb4w2YMTl-XGUYmhplrEwm95TqftwaUqYU_2dcIf3YTCnmLnaulvBEXRgN0c7twAaVNz1uzmSSJzhPJjVRkST3Gd9U2_JfZeNInfwWDsx-D3c4dDs8KJ49oDpgIe0FtLuJN-KPZeSaghluDHljR-0uwrKc7zmQZa6qSvxMgLD8HvBYspUFSxM2v5dUAV81zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=M7XtimNHjkUnnNUF2W9USDLIuS5BbKHnP20kczaDHFrwcFFm9sbe997tn087hbtSrr5-UTXQuMg1RgUl0TrQwRJXZg6sFvX5NTqan0Esy0jlv4P8iFEw3jPJoluaec3WCNmPzAoICgHbUp-_1m3Ccrpb4w2YMTl-XGUYmhplrEwm95TqftwaUqYU_2dcIf3YTCnmLnaulvBEXRgN0c7twAaVNz1uzmSSJzhPJjVRkST3Gd9U2_JfZeNInfwWDsx-D3c4dDs8KJ49oDpgIe0FtLuJN-KPZeSaghluDHljR-0uwrKc7zmQZa6qSvxMgLD8HvBYspUFSxM2v5dUAV81zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttDO-NRG9-NKgc99DW_DNtsJFpgNAP07OiOII0wpgF65GB6YA4LYwDk_2WZjiMzfdnYcG2i35Mf1vPsfMDnNsfZgphcS7kxahhgmVs4JlwUd18OA5A8briHlL7UiNQ6LxxahqVC59YHgEe7Tdp-mzXR979-MWAkC4NORVJAVdXZh66ni4vji7M871SQx9NiupEMiEi7e4DfrnyfuqWFuFVVWgUYBG3LIl4HxtVURz4C_-1cjXyxMrUIt1IOiDVfBeE4Uq3bLYt8uDZ7abkXPmtnrMt5hOONqI9JZQmQBuLkh6YfRG02pEfbrPspo1cktzAxEbl2r6N9YGpyaZt2h1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=flj4e4EtvUfphgWEGaiEw3xcgnn80TbbSbTCrxV7KwLCTE1VVT28ls7aC2pOePFUEs6CXgMFPaSstBnLfTsOS9g4yQ2uBL_OWxsks5eAA18bDU-tqFHYk0OgP5N8VHd2UXKQVpMBn3nTzKYd8TtPGSAv1cFiR0buWTSmBaZOLlR-Df5QOml_qq586KAcmVYYRYpwdLhOws07p5OruhiN_g0kOBz0RuFVM05JiG-OdCaH4rrXaFzoW-njHgBDVAIwj-1kkskDV0SgrsH_jEbRIFSCmBMhzFdErkfpWMfYSp5QFErkiF_u3GJHZiAYbz6AbchZ6RSNfPAEyVi7S80X2lgimAI00wlsxhTFFiGZ4x8JoB1SD0If8uI9ofiqgw_SGwub--POpev2JzsdFMZEtmHK8O6B0mgiWBJOjn-6Z6p_Ix1s4vj1mB1PHgWmCR350QtAf_0gN3Eoi2CtdpLaHa310bnbhwBsUfhY1PK1uhiJNkH4lJgndCLJBqLpO4SZzUPwzIpugdHyzH_6-TgaJRsYou0NJEd-mtexlK5J4OVqedHmMboJ_F18-FdsT1u7teBdJBXqC0MnCR5W72468MAehzFGphQUdOiy9nDAigtqd-fYTXI41pVPLtXd2pu2ntnUNsTOwReGenU5nf7DaxKdB1NYpvDLZTaB2LSUNA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=flj4e4EtvUfphgWEGaiEw3xcgnn80TbbSbTCrxV7KwLCTE1VVT28ls7aC2pOePFUEs6CXgMFPaSstBnLfTsOS9g4yQ2uBL_OWxsks5eAA18bDU-tqFHYk0OgP5N8VHd2UXKQVpMBn3nTzKYd8TtPGSAv1cFiR0buWTSmBaZOLlR-Df5QOml_qq586KAcmVYYRYpwdLhOws07p5OruhiN_g0kOBz0RuFVM05JiG-OdCaH4rrXaFzoW-njHgBDVAIwj-1kkskDV0SgrsH_jEbRIFSCmBMhzFdErkfpWMfYSp5QFErkiF_u3GJHZiAYbz6AbchZ6RSNfPAEyVi7S80X2lgimAI00wlsxhTFFiGZ4x8JoB1SD0If8uI9ofiqgw_SGwub--POpev2JzsdFMZEtmHK8O6B0mgiWBJOjn-6Z6p_Ix1s4vj1mB1PHgWmCR350QtAf_0gN3Eoi2CtdpLaHa310bnbhwBsUfhY1PK1uhiJNkH4lJgndCLJBqLpO4SZzUPwzIpugdHyzH_6-TgaJRsYou0NJEd-mtexlK5J4OVqedHmMboJ_F18-FdsT1u7teBdJBXqC0MnCR5W72468MAehzFGphQUdOiy9nDAigtqd-fYTXI41pVPLtXd2pu2ntnUNsTOwReGenU5nf7DaxKdB1NYpvDLZTaB2LSUNA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCxH-o3QXpeqebB1a4xI7dM-y44qMNZ6y-xsfM0Wr3p616SuHqYQ4_iFI6rYct5Eg0AUOEHuktI6piIjoSoh_NFPjiE0_gxSYCxDZKt2gKQaG5haP0eI83Uwtuz3NvGlyEb3Nqxf8m5ZCWjLKVicdIah0Cl5c7Lp1tj5lIXSq4vDjkZSzJJTtaVbm4zHW18VhrIRFVp01db6HXNsN2Bj4xo8RZOZbGvT4aUYjxAS8VyQvn29zogRe6nQMO0JHiCdRmWTiqVvLgnvGjdhC-hP662hcWW9bTI0STFwTcnhzO0zt69Pdq3V_qeiuae7szWmH64dhTm9FOkmEDmwVvRw8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUz4_6K23nm1Xy7ig5NRqgmkUKtMiWnUWb8qlA4AOEnB9MQ116yY4OCL4Mhr0ftiJ-INTBvmAfr0ygtMg82g88hO67jaOY-RIdZhLGBPfdTleUb2_xKhPqigUXQR57skGGSgGi3p4UoZZh8bob325Cyc0X6HmAs472melC7hVkqNgK5uhPh9M0bknaqvzFgfnKmbu6qe8Gyp6uLD5iBsHS1ON_QebFLfOzivkB3SjeAuzY38XIBI7Q4d3ADiOMi8qRwUBjz7GYDOdH_zpGx-jMAWsC94fIzB3H1W74BlpxzpHDbmVnvxiJih6dEWGpD2KQq_aWN6hXgOOggr3ETM-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urTgIlMFJsHlPgEVDoGVK9ZMbmTTBFWvJIgCWYq5kMnTD7zglSLyPug2LMuv5HnDXZaUTC-ldRNEIHY7g7KLse3dlTUzdSo2bVvBCxqJyI2xmK36TJz-hl3MAjIgwKQcVq2iMITCBk5N8k3qgxC1bIo8Jk7axzPfB_GTSH7W90lTc98SwLADkp9fr2H9o3WKduAXisTrLwPIA7LTm6WT7oW2ZIXTIY4hoPbvEdJc0x97otlbXIWVUkMfcFKyKQrprmibIIOeLgFw03uSX1O5EVfWB2plXnI2-s7xpEB1FMQYf5ZSI516HJ5AshNLmt-2q9DQcwn82DA9P0QUBj60Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fY8Ox3BkXEcQ2WIN5ADijliISDt9fQB6pOJ-SDb5zTFu7XPV11u8q6YRsGJmu-iIlx4Ct8gxfS7u30azA_ZJCdJqxnyFYMVHdCyTuRRPMGAZa8NaT6eWQYwd0j9_gEFbnocmX8Bcxf4HzkzZ2qGgN-O1JH6cLN2t-NhtXGVgoMkUHho5wRsiF-EuoLlyBG6nwh1OHWJPVVLIgss5qH2N6twOjEd52StBolxz3xVf5ENs1BtcAbZAYsEmgXejnzwNTghbtp0fL6i7sHW9w_IC8Am0yV3KnqrlnON5HVNQNY5BCI4E5NrWfhOD4WgWuTxi0mpwMQ8z_z8jwC-4opBRSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=q9TIxtUoa4w9MYy5RMWctuWebv6Uq70HFAfAyQ1nrmzfxyo-4m0vSORToQtluRsUYXr7ZSCs-mt_MgLV2yLH9DnMe7fAwk_6AGL2_woGR1hqFqFCQxdM4dZDpENzOw9BpmBFpV2LGCHYa2Y0dFW_6qR7c2c0p95J0eTgWL1dBQHvqqMDzUcbhC5gaIVlxUUrG1jpH2gjEKsJlFUDSlUgneOnD0uDJbCbSu8U2z5lrL1mSqwnV5NYsZeu84dEhyCcPta1JcJp4_HK2vRqk6W24UZiXxFeCVbl9FlgfQAxMI5GU8Xw8CCXrb5NfpqCfY1iopR3O4MVnodHIAxolA-WPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=q9TIxtUoa4w9MYy5RMWctuWebv6Uq70HFAfAyQ1nrmzfxyo-4m0vSORToQtluRsUYXr7ZSCs-mt_MgLV2yLH9DnMe7fAwk_6AGL2_woGR1hqFqFCQxdM4dZDpENzOw9BpmBFpV2LGCHYa2Y0dFW_6qR7c2c0p95J0eTgWL1dBQHvqqMDzUcbhC5gaIVlxUUrG1jpH2gjEKsJlFUDSlUgneOnD0uDJbCbSu8U2z5lrL1mSqwnV5NYsZeu84dEhyCcPta1JcJp4_HK2vRqk6W24UZiXxFeCVbl9FlgfQAxMI5GU8Xw8CCXrb5NfpqCfY1iopR3O4MVnodHIAxolA-WPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/je5tT-aJ7R1HPlFJcjBdf1uvnvqel8VC5r-bZLsfXiaTkcP-5jM5or_Gi5o9-aSQ-6hU2FwOTROIkySd-QSm1EJ1Qc_ad_eGsocQtMOe9kpP-f6pUVMq7sc_SCNIyxQpQZ7V9EFN4JUr4YoRP8YKfQ8VSdssSky6ES5BlLLvCKxHw6ER-m3dH_V9WsPcCXiVX81_uOq3pJAcR0OXsr91g_ykpodnXPB3rF6vsPCHkFhh8cu7SwITkyW-F-xA-h_Xsee3IwzezLH870XbBFuMaleja8cQ9XeG4svfydFxn57nVOgbIGMZMz_d6ELUulqx74-pKzYLNSbX0_x0RlCnmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1S1kSKPS8IZBBrIeRHv4Imr1bhdFF4Ll94e8yWCunhUjGy_paj1COPWchqOxwNbbw3L63QZwW1KfX1zpq6UqEVpZymY0nAURdqPqBimIBCweI35DGpleIx6c3tnzlXfgmO_mwuDg-WeY11HGGOsseLEZVNOnfM50DAUAZP2zJ-oxM8R8rKl3VQP2wxXtN4cuumL_IktXojClPTVEO9LjzUENQ8_1LUPicPy6njKrqTsO4YArCGE8sBsHV3-mDnw1bOzGpkV085BgFeN8sJQn2vIAOyPE-IeztgSK4FgXutmjtBUXjioeOZQoboSDAaaqvJhsDiFyfom4g0quBA6Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
