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
<img src="https://cdn4.telesco.pe/file/Py7d37P_lWbJdXDeHznNzZFpF_wXoohNAQu7m-lCcR20Sk25vvC8efamAj8lvFrbIdqW8E9MVsL6unOZ4j4dCIYvShqUOtlasIux7pA6oV85Ryobzwh2Pp-IUHLNmL7LBnsLys9fAleYS1UqzjNwIQW-lUgDO5bnK0jPYUjwbjCn0_B4UGvu32yyrnxivkmbzJ3HqxKS2IJTuzHqwtwLN6Y6VVSdj_FBqP6rGnO7huJAUXx_xd94yCSzeQW_Ac_bebDQgVJLPruFJ8304ZxuglUpBokFEWaPX6ezTXq4JkQa0nuYP7k8hF678IkammBBIY_zZnC-rPm5alJLz3ZH7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 447K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 08:19:33</div>
<hr>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اتاق جنگ با یاشار : کره جنوبی جفت کرد !
رویترز: کره جنوبی در حال آماده‌سازی برای اعزام نیروهای نظامی به تنگه هرمز است
؛
رسانه‌های محلی کره جنوبی با استناد به منابع نظامی و دولتی گزارش داده‌اند که این نیروها برای حمایت از
آزادی کشتیرانی (امکان عبور ایمن و آزاد کشتی‌ها)
در تنگه هرمز مستقر خواهند شد و سئول قصد دارد آنها را
پیش از پایان سال
اعزام کند. این تصمیم در حالی مطرح شده که دونالد ترامپ،
رئیس‌جمهور آمریکا، در ماه اوت اعلام کرده بود در حال کاهش همکاری نظامی با کره جنوبی است
؛ بخشی از دلیل این تصمیم، به گفته او، خودداری سئول از کمک به واشنگتن در جنگ علیه ایران بوده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/withyashar/22263" target="_blank">📅 04:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اعلیحضرت همایون شاهنشاه آریامهر محمدرضا پهلوی
: هیچوقت به زندگی فعلی خود قانع نباشید و همیشه دنبال بهتر کردن زندگی خود باشید.
@WarRoom</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/withyashar/22262" target="_blank">📅 03:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: اتحادیه اروپا رسماً به کارزار انزوای اقتصادی علیه ایران پیوست و ما از موضع قاطع و به‌موقع آن قدردانی می‌کنیم. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/22261" target="_blank">📅 03:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رویترز :
یک بات‌نت (شبکه‌ای از رایانه‌های آلوده) به نام
«سلیتی»
که از سال ۲۰۰۳ فعال بود و طی هشت سال گذشته برای سرقت ارز دیجیتال نیز استفاده می‌شد، در عملیات مشترک آمریکا و اروپا از کار انداخته شد. این شبکه بیش از
۱۵ هزار رایانه آلوده
داشت و برای سرقت رمزارز، ارسال هرزنامه و حملات سایبری استفاده می‌شد. هم‌زمان، کمیسیون معاملات آتی کالای آمریکا از دادگاه خواست شکایت
سی‌ام‌ای گروپ
درباره معاملات پرپچوال رمزارزی (قراردادهای بدون تاریخ انقضا) را رد کند. همچنین وزارت دادگستری آمریکا اعلام کرد
بیش از ۵۶۰ هزار دلار رمزارز متعلق به حماس (گروه اسلام‌گرای فلسطینی)
را که برای تأمین مالی این گروه در نظر گرفته شده بود، توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/22260" target="_blank">📅 03:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چندین پرتاب موشک/پهپاد به سمت تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/22259" target="_blank">📅 03:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: اتحادیه اروپا رسماً به کارزار انزوای اقتصادی علیه ایران پیوست و ما از موضع قاطع و به‌موقع آن قدردانی می‌کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/22258" target="_blank">📅 03:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ارتش این کشور شبکه زیرزمینی راهبردی حزب‌الله در منطقه تپه علی‌الطاهر را به‌طور کامل پاکسازی کرده ,
نیروهای لشکر ۳۶ کنترل عملیاتی منطقه را در سطح زمین و زیر زمین به دست گرفته‌اند؛ در این شبکه‌ها اتاق‌های فرماندهی، انبارهای سلاح و امکانات اقامت طولانی‌مدت کشف شده و برخی نیروهای
نیروهای
حزب‌الله و سپاه
حاضر در این محل
کشته یا متواری
شده‌اند.
این زیرساخت زیرزمینی که به گفته اسرائیل طی حدود دو دهه با تأمین مالی و برنامه‌ریزی ایران ساخته شده، همچنان در حال منهدم شدن است
@WarRoom</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/22257" target="_blank">📅 02:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دیدبان اتاق جنگ سیریک :  امشب تنگه خیلی صدا میاد از ساعت ۱۱ تا الان بالایی ۱۵ صدا اومده ، کمی پیش پرتاب موشک انجام دادن ولی الان از تنگه یه صدای مهیب اومد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/22256" target="_blank">📅 02:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f2f2934c.mp4?token=kh2zQmkIKIYvgUj_cOJK5S9D6fgnEKhE9h1R1aZZV5s4IFWDf30zHcdXCZvJyqUo3FFSkmMKy5R636JIfGoIE3tFaqtS3FKDlQ6ucHvNppYZfqNnSvPp60oLhteR0-z9978VVoR1hYS-eEG__PitkeJdelkJqxrjEbQJOxW3jImVL5RY_lsSYR16S6RFEmh4hSwjwcLedu1QnAEzT5Mgks64DdxASvnGslx3oNQf1xhR5O74nZjnATIbnFLj-p-AtZH4ezcEiQvSHx6vgGsUs4bMxgRahgoO_FKPGGFvcveZLvDEXcVvXq7Xl62wyWCW167WvL5OtdRZhSh7Mr6tDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f2f2934c.mp4?token=kh2zQmkIKIYvgUj_cOJK5S9D6fgnEKhE9h1R1aZZV5s4IFWDf30zHcdXCZvJyqUo3FFSkmMKy5R636JIfGoIE3tFaqtS3FKDlQ6ucHvNppYZfqNnSvPp60oLhteR0-z9978VVoR1hYS-eEG__PitkeJdelkJqxrjEbQJOxW3jImVL5RY_lsSYR16S6RFEmh4hSwjwcLedu1QnAEzT5Mgks64DdxASvnGslx3oNQf1xhR5O74nZjnATIbnFLj-p-AtZH4ezcEiQvSHx6vgGsUs4bMxgRahgoO_FKPGGFvcveZLvDEXcVvXq7Xl62wyWCW167WvL5OtdRZhSh7Mr6tDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی غرب تهران چیتگر
@WarRoom</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/22255" target="_blank">📅 02:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22254">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb363544dd.mp4?token=P8GwI6XERhkdJmqG-0jukvxXKE6OrFKmvEpWtMoJBSCVq520rVvZLv9YdYxlu8SionWdpx0YwH8K-mJs-NgWYbupUXeVoEsbe3bWiPdwWXAZ0j1-FSVqjLx_VC-zOJlMOsUElAA-jnRtEKswsAM42jUQ1sWUw5zmV_NidMVXoy2Nj8_Bo59kcr8koNKv6KZ3mKXZ4Ti1igOkNj8iVVo_zUZ9eVJiO-y7sIyxGpZzVtSWO3XWf-_8fqnZXbnu3zIFZqwCcjICkCfI4vyrmCiynYMiSISHOVFrRw6uSx39wCDPvxOj_TMCCRZx7edRS3SuZmAX1mpLr8nylPKr7AQEriRoSc0NC_OZXzNYGVXCnVVIE9YPP7DUzbDzW0vnNo0ITHB6xdTFLq7C0bszVw_hyIJdE_zhR1ASEDqWi6OfLvTtghdTvLNmgpB91NPywNKnHSLfTWD-4Z240UADRdIPaXkmo0QGkiatGwXEqW8lz3asPdx8Ke4WYa6Fu8vtraTB-z9sOuiLmFKW9W7Jp7I-UcGjRTYD_IOLJaaeONUgJs8UjbESD4DDH4avCSmIPrItsZ-7Nx7MYsh5YXhiuoQTbrCFATr_mZTsTX4nw6TGsitigJ2BP-ScDStey39bMMZa7vTff7MZMMtLIvPN9YMUibBrBGEFMVsF3QSLRULtRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb363544dd.mp4?token=P8GwI6XERhkdJmqG-0jukvxXKE6OrFKmvEpWtMoJBSCVq520rVvZLv9YdYxlu8SionWdpx0YwH8K-mJs-NgWYbupUXeVoEsbe3bWiPdwWXAZ0j1-FSVqjLx_VC-zOJlMOsUElAA-jnRtEKswsAM42jUQ1sWUw5zmV_NidMVXoy2Nj8_Bo59kcr8koNKv6KZ3mKXZ4Ti1igOkNj8iVVo_zUZ9eVJiO-y7sIyxGpZzVtSWO3XWf-_8fqnZXbnu3zIFZqwCcjICkCfI4vyrmCiynYMiSISHOVFrRw6uSx39wCDPvxOj_TMCCRZx7edRS3SuZmAX1mpLr8nylPKr7AQEriRoSc0NC_OZXzNYGVXCnVVIE9YPP7DUzbDzW0vnNo0ITHB6xdTFLq7C0bszVw_hyIJdE_zhR1ASEDqWi6OfLvTtghdTvLNmgpB91NPywNKnHSLfTWD-4Z240UADRdIPaXkmo0QGkiatGwXEqW8lz3asPdx8Ke4WYa6Fu8vtraTB-z9sOuiLmFKW9W7Jp7I-UcGjRTYD_IOLJaaeONUgJs8UjbESD4DDH4avCSmIPrItsZ-7Nx7MYsh5YXhiuoQTbrCFATr_mZTsTX4nw6TGsitigJ2BP-ScDStey39bMMZa7vTff7MZMMtLIvPN9YMUibBrBGEFMVsF3QSLRULtRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی در آسمان شهریار
@WarRoom</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/22254" target="_blank">📅 02:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/22253" target="_blank">📅 01:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق جنگ با یاشار: قوه قضائیه جمهوری اسلامی حکم اعدام شاهزاده رضا پهلوی را صادر کرد!
جمهوری اسلامی در تازه‌ترین اقدام خود علیه
شاهزاده رضا پهلوی
، پرونده‌ای با اتهام‌هایی از جمله «افساد فی‌الارض»، جاسوسی و همکاری با دولت‌های متخاصم تشکیل داده ؛ اقدامی که یادآور سابقه جمهوری اسلامی در تهدید و صدور احکام علیه مخالفان خارج از کشور است.
سلمان رشدی
؛ در سال ۱۳۶۷، روح‌الله خمینی فتوای قتل نویسنده بریتانیایی را صادر کرد و برای سال‌ها جمهوری اسلامی در تعقیب او بود، اما رشدی زنده ماند و به فعالیت خود ادامه داد.
دونالد ترامپ و بنیامین نتانیاهو
نیز بارها هدف تهدید به قتل و مجازات قرار گرفته‌اند و در
تجمعات حکومتی جمهوری اسلامی، عروسک‌های آنها را به چوبه‌های دار آویزان کرده‌اند
؛ هم‌زمان مقام‌های حکومتی نیز بارها از مجازات و اعدام آنها سخن گفته‌اند. حالا شاهزاده
رضا پهلوی
نیز به این فهرست اضافه شده است و نشان از مسیر درست ایشان و ترس حکومت از وی دارد ؛ فهرستی که از
ترامپ، نتانیاهو
تا
سلمان رشدی و اکنون با شاهزاده رضا پهلوی
امتداد پیدا می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/22252" target="_blank">📅 01:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دستور پنتاگون برای تغییر نام جنگ علیه ایران
شبکه خبری CBS به ایمیلی از نیروی هوایی آمریکا در ۷ اوت دست یافته که نشان می‌دهد پنتاگون دستور داده نیروهای آمریکایی دیگر برای اشاره به عملیات جاری علیه ایران از عنوان «عملیات خشم حماسی» استفاده نکنند و به‌جای آن عبارت «عملیات برون‌مرزی در حوزه مسئولیت فرماندهی مرکزی آمریکا» را به کار ببرند. پنتاگون اعلام کرده «عملیات خشم حماسی» رسماً در ۵ مه پایان یافته بود؛ همان روزی که مارکو روبیو نیز پایان آن را اعلام کرد. با این حال، عملیات نظامی آمریکا علیه ایران پس از آن ادامه داشته و دیگر تحت این عنوان ثبت نمی‌شود. در ژوئیه نیز ارتش آمریکا ابتدا چهار نظامی کشته‌شده در عملیات‌های مرتبط با ایران را زیر عنوان «خشم حماسی» ثبت کرد، اما بعداً آنها را در دسته «عملیات برون‌مرزی» قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/22251" target="_blank">📅 01:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرگزاری صداوسیما: ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید مقامات لبنانی نرسیده است
@WarRoom
خوب کسی اون منطقه زنده نمونده که بگه
😆</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/22250" target="_blank">📅 01:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓜𝓪𝓱𝓭𝓲</strong></div>
<div class="tg-text">دوباره فعال شد پدافند غرب</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/22249" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnasrin</strong></div>
<div class="tg-text">ما اكباتانيم همينجور صداي پدافند و شليك مياد</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/22248" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan</strong></div>
<div class="tg-text">سلام داداش سمت شهر قدس ساعت های ۱۲ و  خورده ای شروع شد به شلیک پدافند چند دقیقه قطع میشد باز فعال میشد تا چند دقیقه پیش هم بود ، ۴ دقیقه پیش هم یه صدایی مثل پهباد شاهد بود اما نمیدونم واقعا پهباد بود یا هواپیما با ارتفاع پایین داشت پرواز میکرد چون فرودگاه مهرآباد هم هست اینجا اما خیلی صداش شبیه پهباد بود و بعد ۵ ثانیه قطع شد انگار که قطع بشه شاید سقوط کرد اگر هواپیما بود انقدر سریع صداش قطع نمیشد فکر کنم یه پهباد بود</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/22247" target="_blank">📅 01:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromamirali</strong></div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/22246" target="_blank">📅 01:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein</strong></div>
<div class="tg-text">داداش سمت غرب (شهرقدس ) یه چی اومد انگار سقوط میکرد
نمی‌دونم چی بود عین هواپیما یا پهپادی ک داره سقوط می‌کنه</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/22245" target="_blank">📅 01:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامیرشون🪐</strong></div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/22244" target="_blank">📅 01:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پدافند غرب تهران فعال شد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/22243" target="_blank">📅 01:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامیرشون🪐</strong></div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/22242" target="_blank">📅 01:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">BTC = 82000$
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/22241" target="_blank">📅 01:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ: اگه ایالات متحده همین امروز از جنگ علیه ایران خارج بشه بازسازی این کشور ۴۵ سال طول میکشه
@WarRoom</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/22240" target="_blank">📅 01:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/22239" target="_blank">📅 00:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/22238" target="_blank">📅 00:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/22237" target="_blank">📅 00:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/22236" target="_blank">📅 00:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/22235" target="_blank">📅 00:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22234">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldkTIjSATU7SYD4OnUi81FCb6in1d6F_PHF5jMoI1JQBECacxGEAFcFYsf9RVZcEpgzjwdWtLgxGyNvD1dogSN9LhjcynQVofWQQT-z4Dw4tmbpbkwNI-hZxKWmZzZtS4sCLeqvWGcaXDIZ09mWo6ECTsJFPp0bbSro5ZR8BSokwPVViK4_Av0ZpaEvow3PqgfKZKvhJghNykE4z3u5KPbSDqd_fCN4Y4ERwABxZTXLr_TVYBFOs4_JyT-WTIh01DwUPk4KVuLAcXwu1Cm924oZne5saBlVWzK1l_xw0CHhYApBVlPykxb1swAbYKqMW91QZeQo5bW7vZF3GTwxH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست : FBI وارد ماجرا شد بعد از آن که
شیرین سعیدی
، استاد اخراج شده دانشگاه آرکانزاس و حامی جمهوری اسلامی، پس از افشای اتهام سرقت علمی و حمایت از حکومت ایران، لادن بازرگان، فعال مخالف جمهوری اسلامی، را در X تهدید کرد که «با یک ارتش» به سراغ او خواهد رفت و اضافه کرد « کاری با تو خواهیم کرد که در تاریخ ثبت شود.» . او همچنین تهدید کرده قبر برادر اعدام‌شده بازرگان در کشتار ۱۳۶۷ را پیدا کرده و روی آن «رقص» خواهد کرد. سعیدی در سال ۲۰۲۵ نیز با استفاده از سربرگ دانشگاه آرکانزاس، نامه‌ای در حمایت از حمید نوری، مقام سابق زندان‌های ایران که در سوئد به‌دلیل نقش در کشتار ۱۳۶۷ محکوم شده بود، ارائه کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/22234" target="_blank">📅 00:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/22233" target="_blank">📅 00:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXwxoCO715ampefmbyr1vJlqvSLoxv4esPyAZLTRbeJ6OQzMEot83kY8iaxD2LN950K_LybhV06sIabBPeVZeynVsJbcHrZozmsamfFOd1UyGpF8tyb6tYrw6Sm6EkV1nlbG0Xy3S9LTJ-shJagNz-ySHll8T51FbLkCFz2lW7LIuRsXH1-Or_LMIwkm-6Tv6W2f6ywKXfCF1vyoAaGsgvFeKywMamCLrhZwFporTLxy0792eRouMNVy_Vjanr7KpAQvP4GBVBg2Moyl_ZXHBYORLGbP4E4bnmpd3h7SkVwVU6Q7tZZ8XFqtgEjeAtmPxPRxD-7SPeX9HtCQDyi_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی نفت‌کش "مرجان" متعلق به ترکیه، از تنگه هرمز عبور کرد و از مسیری استفاده نمود که توسط ایران تعیین شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/22232" target="_blank">📅 00:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22231">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو: ارتفاعات علی‌الطاهر لبنان دیگر تهدیدی برای ما نیست!
وی همچنین گفت که نظامیان اسرائیل، شمار زیادی از «شبه‌نظامیان» را در این منطقه از بین برده‌اند. ارتش اسرائیل ساعتی قبل اعلام کرد که به‌صورت عملیاتی بر زیرساخت‌های وابسته به حزب‌الله در ارتفاعات «علی الطاهر» در جنوب لبنان مسلط شده است
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22231" target="_blank">📅 23:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وای نت عبری : حملات نیروهای دفاعی اسرائیل در المنصوری در منطقه صور، در وادی السلوقی و در زوطر الشرقیه در جنوب لبنان در حال انجام است
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22230" target="_blank">📅 23:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گاردین : رئیس سیا در سفر به روسیه از مسکو خواسته حمایت خود از تهران را کاهش دهد
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22229" target="_blank">📅 23:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ارتش اسرائیل : عملیات پاکسازی دو تونل زیرزمینی حزب‌الله در ارتفاعات علی‌الطاهر در جنوب لبنان به پایان رسیده و اکنون در حال خنثی‌سازی این زیرساخت‌ها هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22228" target="_blank">📅 23:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22227">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سنتکام : از دیروز فقط یک دشت کردیم ، مجبورش کردیم دور بزنه برگرده
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی
مسیر ۸۷ فروند کشتی تجاری را تغییر داده‌اند
، ۳ فروند را غیرفعال کرده‌اند و ۲ فروند را بازرسی کرده‌اند تا از رعایت مقررات پس از تشدید محاصره بنادر ایران اطمینان حاصل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22227" target="_blank">📅 23:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتاق جنگ با یاشار : گزارشهای زیادی دارم از شلیک کوتاه پدافند شرق و همچنین بعد از مدتی پدافند غرب تهران . فکر کنم بی‌بی پهپادهای شناسایی را برای رصد تحرکات تهران اعزام کرده است. مسأله ای که خود رژیم نیز بارها به حضور پهپادهای شناسایی آمریکایی/اسرائیلی در آسمان پایتخت اعتراف کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22226" target="_blank">📅 23:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏ کانال ۱۴ اسرائیل : پاکستان و قطر طی دو هفته گذشته دو بار از ترامپ خواسته‌اند بخشی از دارایی‌های مسدودشده ایران را برای کمک به کاهش تنش آزاد کند، اما ترامپ هر دو درخواست را رد کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22225" target="_blank">📅 23:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جی دی ونس : اگر به ترکیه، آذربایجان، قطر، امارات متحده عربی و عربستان سعودی نگاه کنید و به طور کلی به سراسر جهان بنگرید، در واقع شاهد تعداد زیادی از کشورها هستیم که گاهی اوقات حاضر به بیان علنی این موضوع نیستند، اما در پشت پرده کارهای بسیار خوبی انجام می‌دهند تا به ما کمک کنند تا اطمینان حاصل کنیم که ایرانیان به دلیل شلیک به کشتی‌های تجاری، مجازات شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22224" target="_blank">📅 22:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جی دی ونس: ما می‌توانیم منطقه را ترک کنیم، اما کشورهای عربی حاشیه خلیج‌فارس به ما می‌گویند این بدترین اتفاق ممکن است, با وجود اختلافات سیاسی ما با چین، آنها مایل به همکاری با ما برای اعمال فشار بر ایرانی‌ها هستند
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22223" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22222" target="_blank">📅 22:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22221">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJY0IVBIiRri9l57k_9tUcS2XJJCjy0uq4zZVCfoUJa0O5I8--zlbiH6TsAv2VRnUn7FXS6AYjUeyTZtuJsIMGY7F3GI-8zKbkrFkhzgEY4VzAYQggKzZIgvQ9gWd53heZ1FX8nwK4BrFa2ybhAid9buwOz_WfdHSl5Y40auk3DglftGcLgce3b65dsS5SVDq0TwflONEl8opYcBIcwRApzTcPFn3VCEkYnHz2WSHc8zFWs9bdtLp5gBKoZVFP9YQPs5HXIwIZsG5SZ5PfgP_0eYNAk4-OMCn1cgur0gV5U-lDXncj46lloeAebF49j_ezv-3g8yzD7hN_RhXGVZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
🙌🏾</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22221" target="_blank">📅 22:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نه قزه، نه لبنان، جانم فدای ایران.
عراق، سوریه، لبنان، فدای ایران.
شلیک به قلب دشمنان
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22220" target="_blank">📅 22:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22219" target="_blank">📅 22:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جی دی
ونس: ما تا زمانی که ایران از شلیک به کشتی‌ها دست نکشد، با آن مذاکره نخواهیم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22218" target="_blank">📅 22:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22217" target="_blank">📅 22:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22216" target="_blank">📅 22:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22215">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/22215" target="_blank">📅 22:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/22214" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال ۱۴ اسرائیل : ارتش اسرائیل با غلبه بر هشدارهای صریح تهران، شبکه استراتژیک زیرزمینی حزب‌الله در رشته کوه علی الطاهر را با موفقیت پاکسازی کرد. تمام تروریست‌های حزب‌الله و مربیان سپاه پاسداران از بین رفته یا مجبور به فرار شده‌اند.
تخریب این دژ اکنون در حال انجام است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22213" target="_blank">📅 21:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22212">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">لحظاتی پیش یک مقام ارشد سیاسی اسرائیل به شبکه 14 این کشور اعلام کرد:
ما نشانه های جدی مشاهده میکنیم از آمادگی ایران برای حمله موشکی به اسرائیل.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/22212" target="_blank">📅 21:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2759f740dd.mp4?token=bgTrHG8O3CwRgDKCVyX54uYQTL4sYh7r54IBAeboQj5nlS54shTPPwX_Nt5wFTv2qp4pKZtxY5svRsu3cn4SWDSASeQC7FZ_TMv6SILQKYJQes7zZVxK4J0LUUmmfBKA2QGZuBZJyz30SOHfxmzOO_xN1ei1iSc5VW_jiR5VGFFAx6SDy3Jc_1E8r0e43KMJp0z7fO-j35T67opNM0-4iF555lQNW2QRKqes4bcUrmQu5PAcMiCD2IRKvpOd8e2EutQLh5AVTGx29sx5SQdiajuFMbquSuXMa8dBr7b8DtiXs6aeAt5JG3-A3UancpSrVP3E6ioHeASqIXRprAZBTJM83hJ64r323lytRCZZHIUMzj1HKg_7SHtDD1UzQQqn-Gi0NuQVmBst4NKzhGhtIIO7SHCDuk-lXQGVmpX1ypg-P57rz2Q6zD3qorAby4OFgGHFCPiub3dFxEWuMTdHDJ-1H3DmMiHCvP61yzG1xNzn2tyW-Y-tiKABdZwgccFCcTqanudItEUReh3WPRH0pJvkK0UOiC7KUOSubLFu2pUgM4foePn4Z9ClJOCqNgVXivuNNHfSX5P1THbxyMOtsqy2qxL92Xj9Fzpoh8Rg1CtV6oKTXGLiFsd3TyKgns38zQoPIrdbIzJ1xN7MTFEUs3TEmJH2z2x1yEwXR0PW7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2759f740dd.mp4?token=bgTrHG8O3CwRgDKCVyX54uYQTL4sYh7r54IBAeboQj5nlS54shTPPwX_Nt5wFTv2qp4pKZtxY5svRsu3cn4SWDSASeQC7FZ_TMv6SILQKYJQes7zZVxK4J0LUUmmfBKA2QGZuBZJyz30SOHfxmzOO_xN1ei1iSc5VW_jiR5VGFFAx6SDy3Jc_1E8r0e43KMJp0z7fO-j35T67opNM0-4iF555lQNW2QRKqes4bcUrmQu5PAcMiCD2IRKvpOd8e2EutQLh5AVTGx29sx5SQdiajuFMbquSuXMa8dBr7b8DtiXs6aeAt5JG3-A3UancpSrVP3E6ioHeASqIXRprAZBTJM83hJ64r323lytRCZZHIUMzj1HKg_7SHtDD1UzQQqn-Gi0NuQVmBst4NKzhGhtIIO7SHCDuk-lXQGVmpX1ypg-P57rz2Q6zD3qorAby4OFgGHFCPiub3dFxEWuMTdHDJ-1H3DmMiHCvP61yzG1xNzn2tyW-Y-tiKABdZwgccFCcTqanudItEUReh3WPRH0pJvkK0UOiC7KUOSubLFu2pUgM4foePn4Z9ClJOCqNgVXivuNNHfSX5P1THbxyMOtsqy2qxL92Xj9Fzpoh8Rg1CtV6oKTXGLiFsd3TyKgns38zQoPIrdbIzJ1xN7MTFEUs3TEmJH2z2x1yEwXR0PW7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره حمله به یک مراسم عروسی در اوایل این هفته که ایران می‌گوید چند کشته و ده‌ها زخمی بر جا گذاشته، آیا گزارشی به شما رسیده و آیا آمریکا مسئول آن بوده است؟
جی.‌دی. ونس: از این موضوع اطلاع دارم و سنتکام در حال بررسی آن است. من هم گزارش‌های عمومی رسانه‌ها را دیده‌ام، اما درباره روایت رسانه‌های دولتی ایران از وقایع این درگیری تردید جدی دارم. با اطمینان می‌گویم آمریکا برخلاف سپاه پاسداران، هرگز غیرنظامیان را عمداً هدف قرار نمی‌دهد و چنین کاری را نه انجام داده و نه انجام خواهد داد. البته در جنگ ممکن است اشتباهاتی رخ دهد، اما درباره این حادثه هنوز اطلاعات کافی نداریم و بررسی کامل و همه‌جانبه آن ادامه دارد. برای ما مهم است که حقیقت را بدانیم و اگر اشتباهی از سوی نیروهای آمریکایی رخ داده باشد، آن را بررسی کرده و از آن برای جلوگیری از تکرار اشتباهات درس می‌گیریم
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/22211" target="_blank">📅 21:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ارتش اسرائیل: طی ساعات گذشته به کنترل عملیاتی ارتفاعات «علی‌الطاهر» در جنوب لبنان دست یافتیم و دو مسیر از زیرساخت‌های زیرزمینی حزب‌الله در این منطقه را پاکسازی کردیم. عملیات برای خنثی‌سازی تونل‌ها و تأسیسات زیرزمینی حزب‌الله همچنان ادامه دارد.
علی‌الطاهر
؛ منطقه‌ای راهبردی در نزدیکی نبطیه که حدود ۱۵ کیلومتر با مرز اسرائیل فاصله دارد و حزب‌الله و سپاه در زیر آن شبکه‌ای از تونل‌ها، مراکز فرماندهی و انبارهای تسلیحاتی ایجاد کرده اند.
ایران پیش تر اعلام کرده بود در صورت حمله به این مجتمع زیر زمینی در جنوب لبنان که نیرو های سپاه نیز در آن حضور دارند شدیداً به اسرائیل حمله خواهد کرد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/22210" target="_blank">📅 21:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/188d3827bd.mp4?token=cx7DDYMJHBbxpo-fD-fiIPOl1yw2HzwQg3v7YykL51ueF8U6w6kr1hFgRC61sbNEjP5MoeErmw8_adTePfw0Qcyel51u4gyYV3KqqwHBQld1nS5cWDWxs52HH4NJOhlDpX3COvv057IEjScVDUDdcfBKFmj-1myt5oJNANfjQ9P_mKqQGStXTkCS_e3O1FYXcJt524HWKIzc2OfrNUSVGq_7U15ibyvVjzpgLmJ_rYq9VE5JqAE92LM_W02fb8HogdbIcZBygvJWytQNyZZ8zhkAx0svbfhVJ_yoCOPKP-Vvoz9cRa4tJK8d3O1YhhkmwBXVMicNNPR8HBM9yRffUUDFcOV1EoplQ3No2Hjhp8yhSvLiygkUj0q4QubffyniLeguRGO55evj8KCVZHr7WoRNa0Guw7nyCteVaO-oljD00RbX1pJm5plWBq2s25XyxUoW6ZBP031ASImMSKxuNSvKlOuOqeCQcc7kXihxPrVCzLCNeWr--Ggby0ClMLIaXcaz-BUQ9W_Z-RddRb2nkFxwK1tSKQqW6QumERW9O6aev37lwFhs5Argn0iUl6-VFZp2Z4kp0rkREMAsjKt_RZLhkQ1Vbm6su1ZguTDwg3mMod5MJrJQDU_dU5ktKlLRSrjn1d2tPSj5Ud6ulS0HYRgsqnhjOs9yepsNOKjctQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/188d3827bd.mp4?token=cx7DDYMJHBbxpo-fD-fiIPOl1yw2HzwQg3v7YykL51ueF8U6w6kr1hFgRC61sbNEjP5MoeErmw8_adTePfw0Qcyel51u4gyYV3KqqwHBQld1nS5cWDWxs52HH4NJOhlDpX3COvv057IEjScVDUDdcfBKFmj-1myt5oJNANfjQ9P_mKqQGStXTkCS_e3O1FYXcJt524HWKIzc2OfrNUSVGq_7U15ibyvVjzpgLmJ_rYq9VE5JqAE92LM_W02fb8HogdbIcZBygvJWytQNyZZ8zhkAx0svbfhVJ_yoCOPKP-Vvoz9cRa4tJK8d3O1YhhkmwBXVMicNNPR8HBM9yRffUUDFcOV1EoplQ3No2Hjhp8yhSvLiygkUj0q4QubffyniLeguRGO55evj8KCVZHr7WoRNa0Guw7nyCteVaO-oljD00RbX1pJm5plWBq2s25XyxUoW6ZBP031ASImMSKxuNSvKlOuOqeCQcc7kXihxPrVCzLCNeWr--Ggby0ClMLIaXcaz-BUQ9W_Z-RddRb2nkFxwK1tSKQqW6QumERW9O6aev37lwFhs5Argn0iUl6-VFZp2Z4kp0rkREMAsjKt_RZLhkQ1Vbm6su1ZguTDwg3mMod5MJrJQDU_dU5ktKlLRSrjn1d2tPSj5Ud6ulS0HYRgsqnhjOs9yepsNOKjctQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو، درباره جمهوری اسلامی: ما با تهدید نابودی از سوی رژیمی مواجه بودیم که می‌خواست با استفاده از بمب‌های هسته‌ای ما را نابود کند. من به توانایی ما برای از بین بردن این تهدید برای همیشه، یعنی سرنگونی این رژیم، اطمینان دارم. این مأموریت محوری همچنان پیش روی ما قرار دارد، اما نزدیک است؛ غیرممکن نیست و در دسترس است. آنها بی‌دلیل از حمله به ما اجتناب نمی‌کنند؛ آنها به همه حمله می‌کنند، فقط به ما نه، چون از قدرت ما، نیروی بازوی ما و اراده ما آگاهند. من به دشمنانمان به‌طور کلی می‌گویم: با ما بازی نکنید. اگر چیزی آموخته‌اید، با ما بازی نکنید. ما قدرت، اراده و وحدت درونی لازم برای غلبه بر شما را داریم
@WarRoom
فقط عرق خوری‌آخرش
😂
🍷</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/22209" target="_blank">📅 21:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از اطراف تبریز ، حتما به کمپ کورد های عراق
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/22208" target="_blank">📅 20:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5m8E040Tx4DNHqLcpRJEQHmquMeRt1CXR0wyhanoAkAc-t-tTSwbh3mSsbdLEcKxZkyujMiHK9JILu5zZDi9LiXU_cafmc8JA4VbsF8cB4yigGWYSluSz1bYX-MoxgUbLSnu0VcQ0iDcgby2mbrAhokP896lr0exaHqhzpu4TF-nAZ2l25rOTgFdYjhv8BHqM4WZuf-lTFM9l-YhwkZaMQK7oGgnBgKx2MvcmoX_cTI31YatvP3QKEfV0whaWMqMIkcUGQZChOQHX_8YBbfHYnnT0b9oe3G7jwh0q-TTo2VgWunzpRMqjOZGKv3ir4VqXzljL1m7aMDSEIIpCQ7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا : امیر یاریاب، فرمانده عملیات سایبری فرماندهی سایبری-الکترونیکی سپاه پاسداران (IRGC-CEC) است. او در این سمت، گروه‌های سایبری مخرب وابسته به سپاه، از جمله «شهید همت» و «شهید شوشتری» را برای هدف قرار دادن زیرساخت‌های حیاتی آمریکا هدایت می‌کند. ما برای اطلاعاتی که به شناسایی یا یافتن یاریاب و افراد یا گروه‌های مرتبط با این عملیات‌های سایبری منجر شود، تا
۱۰ میلیون دلار پاداش
تعیین کرده این.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22207" target="_blank">📅 20:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کانال 14 عبری: افزایش قابل توجهی در سطح آمادگی و هوشیاری در داخل اسرائیل، با توجه به احتمال از سرگیری درگیری‌های نظامی مستقیم با ایران، مشاهده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/22206" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090e602491.mp4?token=XTN-86W5S7RLYX1MTMUhtm5LXNAwk7wefJISgEEet2oL5IbfeuaDo7o8bv_d1pXIWK17ob0xalS_oO8yqZGpwLI2hND5-69hDIAHz5s_AIrW_uJdhTl41ZUJjVT0OK19z5EG9xJkXD1Id1hNihNHH6Ld7BhCCBIus05w0QyyO88BcGwH9voYflifoK9FVQyPjvXxsPTVe9x6_JtQki5AbzxKeWtO_flpPtLxkJZP5PWtNl6_pRvD-NsPwoft7QVfTme1ZlppZMz8mcH8lUtJHkpHtVJB2skXb02EyND8THP1N4RZZPchiGqFIveuuj5mP4ZnIkZtsTZwiY4-DtWEQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090e602491.mp4?token=XTN-86W5S7RLYX1MTMUhtm5LXNAwk7wefJISgEEet2oL5IbfeuaDo7o8bv_d1pXIWK17ob0xalS_oO8yqZGpwLI2hND5-69hDIAHz5s_AIrW_uJdhTl41ZUJjVT0OK19z5EG9xJkXD1Id1hNihNHH6Ld7BhCCBIus05w0QyyO88BcGwH9voYflifoK9FVQyPjvXxsPTVe9x6_JtQki5AbzxKeWtO_flpPtLxkJZP5PWtNl6_pRvD-NsPwoft7QVfTme1ZlppZMz8mcH8lUtJHkpHtVJB2skXb02EyND8THP1N4RZZPchiGqFIveuuj5mP4ZnIkZtsTZwiY4-DtWEQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره بریتانیا : کشور شما خوب پیش نمی‌رود.
فراموش نکنید که درصد بالایی از نفت خود را از تنگه هرمز دریافت می‌کنید.
و شما برای کمک به من آنجا نبودید. کشور شما برای کمک به من آنجا نبود!
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22205" target="_blank">📅 20:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22203">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نیویورک‌پست: عمان به‌طور محرمانه پیشنهاد ایران برای دریافت هزینه از کشتی‌های عبوری از تنگه هرمز را رد کرده است. به گفته یک مقام ارشد منطقه‌ای، مسقط حتی با دریافت هزینه‌های داوطلبانه برای خدمات زیست‌محیطی و امنیتی نیز موافقت نکرده و این پیشنهاد برخلاف ادعای پیشین سپاه پاسداران، هنوز به توافق نهایی تبدیل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22203" target="_blank">📅 20:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اتاق جنگ با یاشار : نتانیاهو داره هر روز رژیم رو انگول می‌کنه و صحبت از تغییر رژیم می‌کنه بعدم جنوب لبنان رو میکوبه سفت
💥
😂
خواهیم دید چه خواهد شد @WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22202" target="_blank">📅 19:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22201">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اتاق جنگ با یاشار : نتانیاهو داره هر روز رژیم رو انگول می‌کنه و صحبت از تغییر رژیم می‌کنه بعدم جنوب لبنان رو میکوبه سفت
💥
😂
خواهیم دید چه خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22201" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو: "ما اطمینان داریم که قادر به سرنگونی نظام ایرانی هستیم. این وظیفه اصلی است و به زودی به انجام خواهد رسید."
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22200" target="_blank">📅 19:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22199" target="_blank">📅 19:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">@WarRoom
جنگ خاموش ؟</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22198" target="_blank">📅 19:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22197" target="_blank">📅 19:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4N3WiLGrf5zugdQ5bTvImWqbR8Gb0qd_tXUovdseELyNou1PZvGo-hAgUGk6KQiByZgCGxjMPkfMT7eLoufhNC7tllCQAEfCyghAwg9AkZr-BS1dobzofutoPDhUb6rH6Pwo7lV1nziAbEIzJpqQb744aBf9au7n36pwXBe2rt6uO1EBsaSSlFQRcgl6h1Oi1sA8ePnrpdRZHlsFogkQHYQSmNL3hZF-GXgaRaBb8UBjCU5226JfxlVWp5kZKNxoE5VPzGL63AcDhazvjmZGJ-PlWRzDgRMkq1-nqdjujzqOHq4AAjUPhAO9if7DcVe6h71KngqXZ6vAce2BDBfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22196" target="_blank">📅 19:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش تایید نشده : یاشار پدرم تو نیروگاه برق همدان کار میکنه ,میگه نیروگاه برق ۴۰۰ کیلو ولت رو زدن ,حدود یک ساعت پیش تا دو ساعت , میخواستم باهاش تماس بگیرم ولی نمیشد الان زنگ زد گفت
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22195" target="_blank">📅 19:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMlVMEx5kSGJ8doV1LzCs-P3cBblOXGp6z0ZRGIDfmUQkG-Ur08hr0iuRvQ9VXGfOY8MQDcMmbYNfZ9h_a3RRh0QvxGrZhaZyKgvL89pAsYC5-lFDk_A_qXDTaw6MErzW2bU8gZam04qVUCQioRtkmTGOahDzajOejGOGJa3AHZqOaazngbSQnU6KMG4Zp2kNraZN5h__EHhQZKFg8YzHw5uzTsgi13oWFdo8hqF0fjQ-KG2CYr5BuzbUBHwtVj4oEa_FlRf1Dst-4kmVqnZekPD9rJFZ8F7asXkXgTt53-3Ytgw_vwMANpwRt1UvcJbA-1d3u0zhVgSIuCKaSdxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تبلیغ از طرف من نیست ! پولی ندید  بهش !</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22194" target="_blank">📅 19:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkC-01WwPM5QbEJdG7ufRT2hf6uL258R5Lj0Sa_jR0t8waRK4hZm3kaku6B0AbwiTsqbBDVDRjRJVZdI6-GlG0nr-Mq-DYJwnH1zr8AZiay1g6KGWwxkSjlTdyoA3pKkKbF7G1QRv2PSvm8lXN_yaHlfXFBVPhhLlsqmxb-UyfUoXcGojwGZxNrt6TlLdDMVmpOxG_JdS1ZyN4Ai92A1zNjgEFwNgdSmiMSapmhlGsYrcNWxLMSPtkH8TKCbUMEchfvFzF20CyicyzhgdpORiKblg-fev5UVwtcwVfvddiwjdm363EZsCZkKNQ3RE2aOXDPtfa4QFHWLBHp99thu6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای رسانه‌های خائن و پلیدی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کنند، باید گفت ما عملاً مقادیر نامحدودی مهمات درجه متوسط تا بالا در اختیار داریم؛ بسیار بیشتر از آنکه بتوانیم در این عملیات یا هر جنگ دیگری (که بسیار بعید است!) که به‌طور غیرمحتمل رخ دهد، مصرف کنیم. علاوه بر این، ما مهمات را در سطحی بی‌سابقه تولید می‌کنیم. ما در حال انباشته‌سازی و آمادگی برای هرگونه سناریوی احتمالی هستیم. ما این مهمات را برای خودمان، یعنی ایالات متحده آمریکا، نگه می‌داریم نه برای فروش به دیگران؛ اما فروش به متحدان به‌زودی از سر گرفته خواهد شد. همچنین، لطفاً اعلام شود که دولت بایدن بسیار بیشتر از آنچه ما در ایران مصرف کرده‌ایم، مهمات را بدون هیچ هزینه‌ای به اوکراین اهدا کرد. صدها میلیارد دلار به اوکراین و ناتو به‌صورت رایگان داده شد؛ هزینه‌ای که اروپا می‌توانست پرداخت کند اگر تنها از آن‌ها درخواست می‌شد، اما ما آن مبلغ را مطالبه خواهیم کرد، اگرچه با تأخیر!
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22193" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22192">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6V0_Y7h5eLLCJEsRsAdoEHaW8IFEqTynuIREl2DPeGJ0ZwX2DXbdu4JqvJkTS1bm9vayEnllJ7c2i7OEcgt_lqxaW1PJRB68NnOxOemsYLwqicoIc0c1x2E3E8fF5fC5zp1ay3pN2T7zSYSVivtjXH2yKK2WwiKnM8Y8uqrxGlrdXxFPQYroRC_VEyZGZoDeQKxbPhX3iJjXQuONPV83bNquIbfTHC0nssBNZ_Ypk46kA3KXkyrh8-SwmtREy3OueEHijA-gxHwzSPLEiKlLYBsPn-KoSZ5xByLQMDDuKzyhz8PCPqrbUy7IBAyDA69i2O66SdrSGr8wg7qre69zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : مردم و رسانه‌هایی که مدام بر این موضوع تأکید می‌کنند که ما مهمات نداریم (و صددرصد اشتباه می‌کنند!) در واقع خائن هستند. آن‌ها این کار را می‌کنند زیرا ترجیح می‌دهند ایالات متحده در جنگی که به‌راحتی در حال پیروزی در آن هستیم شکست بخورد، تا اینکه ببینند من پیروز می‌شوم!
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22192" target="_blank">📅 18:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22191" target="_blank">📅 18:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اسرائیل نشنال نیوز : کانال ۷ عبری مدعی شد موشک‌های ایران به هتلی در اردن که افسران نظامی آمریکایی در آن اقامت داشتند اصابت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22190" target="_blank">📅 18:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75591b88.mp4?token=rzBeYKivz_Z5FL_bKh6xM7qm0kCZJXIU4oHLODlWLX1s0RMK1YDH7LWIVRJb2iBQ5QebhxRoQy_zEA8yPO46MArvGID0YEAJWiut2KXd_50Ypr4DyP5hdBHN1HmGQYb70qGNn3Ii8tMK5oA2kK7FK4dCK7_55kh6Bq72WMkjMWK3tjPmfPCYKq-5d9CVa6B24oDVXxWkvoGAfQhqSD6tEt0cqdYzRIZ2iQmwE9o2kpIJ3iGpg4ud8TACplj-1O0QqC_h9elzl1YKDnLBNVw_lACR2fuGLx3bFU13cCpbBhu1Nb8S50OhjxsIb28ycUg8ozMjHfwQXOwYj0AG4t8Q1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75591b88.mp4?token=rzBeYKivz_Z5FL_bKh6xM7qm0kCZJXIU4oHLODlWLX1s0RMK1YDH7LWIVRJb2iBQ5QebhxRoQy_zEA8yPO46MArvGID0YEAJWiut2KXd_50Ypr4DyP5hdBHN1HmGQYb70qGNn3Ii8tMK5oA2kK7FK4dCK7_55kh6Bq72WMkjMWK3tjPmfPCYKq-5d9CVa6B24oDVXxWkvoGAfQhqSD6tEt0cqdYzRIZ2iQmwE9o2kpIJ3iGpg4ud8TACplj-1O0QqC_h9elzl1YKDnLBNVw_lACR2fuGLx3bFU13cCpbBhu1Nb8S50OhjxsIb28ycUg8ozMjHfwQXOwYj0AG4t8Q1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی، با پشتیبانی تانک‌های مرکاوا، در حال پیشروی در جنوب لبنان هستند
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22189" target="_blank">📅 17:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مقام آمریکایی به خبرگزاری الجزیره گفت پایگاه‌های نظامی آمریکا در منطقه، از جمله پایگاه‌های این کشور در کویت، در جریان حملات تلافی‌جویانه شب گذشته ایران
هیچ‌گونه آسیبی ندیده و هدف حمله قرار نگرفته‌اند
. الجزیره پیش‌تر گزارش داده بود که ایران در واکنش به حملات آمریکا، موشک‌ها و پهپادهایی را به سمت اهدافی در کویت، بحرین، اردن و عراق شلیک کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22188" target="_blank">📅 17:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22187">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">در صورت ازسرگیری جنگ، ایران ۳ گزینه برای تشدید حملات در اختیار دارد
۱.
گسترش حملات به کشورهای عربی خلیج فارس
، از جمله هدف قرار دادن تأسیسات نفت و گاز، نیروگاه‌ها و تأسیسات آب‌شیرین‌کن؛ اقدامی که می‌تواند به افزایش شدید قیمت انرژی و آسیب به اقتصاد کشورهای منطقه منجر شود.
۲.
جلوگیری از خروج بیشتر نفت از منطقه
با تشدید فشار بر کشتیرانی و تنگه هرمز و تلاش برای متوقف کردن صادرات نفت از خلیج فارس.
۳.
گسترش حملات به منافع آمریکا و کشورهای غربی در خارج از منطقه
، از جمله حملات مستقیم یا غیرمستقیم به اهداف غربی.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22187" target="_blank">📅 17:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بلومبرگ: درگیری آمریکا و ایران به بن‌بست رسیده و هیچ نشانه‌ای از حل‌وفصل قریب‌الوقوع آن دیده نمی‌شود. در حالی که حملات متقابل ادامه دارد، تلاش‌های دیپلماتیک برای پایان دادن به درگیری پیشرفت قابل‌توجهی نداشته است. تهران همچنان از عقب‌نشینی از مواضع خود خودداری می‌کند و واشنگتن نیز فشار اقتصادی و نظامی را ادامه می‌دهد. هم‌زمان، دولت ترامپ در حال بررسی راه‌هایی برای مهار درگیری است، اما احتمال طولانی‌شدن جنگ همچنان جدی است. گزارش‌های امروز نیز نشان می‌دهد درگیری وارد مرحله‌ای فرسایشی شده و آمریکا حتی استقرار نیروهای خود در منطقه را تا سال ۲۰۲۷ تمدید کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22186" target="_blank">📅 17:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سخنگوی قرارگاه خاتم‌ الانبیا:
عملیات های تهاجمی علیه آمریکا ادامه خواهد داشت.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22185" target="_blank">📅 17:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOhyF6nPjZGQlPw1SZtkxJ-hMqe6GPujl4emvmLn7HSt2BYDDYVZRm4jhJn_9RBwgNGApLgWLBbX68Db6GablZVFJ8Dr86kCoGIzP6Jzw75tEtVGsRNqKEhuOiaCNU1WEyGTdBLmpiY6PxOOK1VAaJSRZosmpfUfwFPRoPplctqj2-ajzE38Up1EdG-V7ATS9ENAaKDt-mH3mdb85-TXh26XS1VngqcTda-BWvkXP30VzcRt_yE5Kg4Pk9VU_6LIHlCwFyxVx-TdQ-mM-mASCXxJUmMhSw2N5ZcX5phZCAmghG1tq19KMmZMpszTOLw8VJfyfkHjrSD0xQXUUElMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش اولیه تاییدنشده
از حمله به یک سایت در استان فارس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22184" target="_blank">📅 17:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c459a770c1.mp4?token=QTOoObTK53TPKydQkq_mrpuMoVGjSjB8Tn4lof_epjs9xHvNO-V6fyvDHK9st2POevdBzZ04lxkd72UTwao5ZxHGJTBQIlanV0bUyrap_82vC8p2tcy9MfVSfDwxAratjsXsZERPEmWawOtt1kJAPXUiJRVjBMDQhIYYiNKRMw9TA4fG_Od3vlpOCE-FSSXb7jAxzjA50wEOLps7TpQeBVtZxyboe452FxJPdO00ZDjvGia8jA1oNGUfb-12_VGGprE4HZFak_6Gek-_DyWATzpNkxjuG2gTTLV862Yjb74gztvz0qx1OIaj3kkbclbzHhBKVwpVi1dCj-gmYWpIXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c459a770c1.mp4?token=QTOoObTK53TPKydQkq_mrpuMoVGjSjB8Tn4lof_epjs9xHvNO-V6fyvDHK9st2POevdBzZ04lxkd72UTwao5ZxHGJTBQIlanV0bUyrap_82vC8p2tcy9MfVSfDwxAratjsXsZERPEmWawOtt1kJAPXUiJRVjBMDQhIYYiNKRMw9TA4fG_Od3vlpOCE-FSSXb7jAxzjA50wEOLps7TpQeBVtZxyboe452FxJPdO00ZDjvGia8jA1oNGUfb-12_VGGprE4HZFak_6Gek-_DyWATzpNkxjuG2gTTLV862Yjb74gztvz0qx1OIaj3kkbclbzHhBKVwpVi1dCj-gmYWpIXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدمه‌ ناو هواپیمابر آبراهام لینکلن ، به تایلند رسیدن و رفتن تا پس از یکسال در دریا بودن در خشکی عشقو حال کنن
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22183" target="_blank">📅 16:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">احمد وحیدی فرمانده سپاه: انتقام جان باختگان نبرد هرمز را می‌گیریم
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22182" target="_blank">📅 16:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLom_u9Xzr6OOZEa4recykpJlR-isQOXs2taEZn9ZJ2fvFTyW0Ldz7IZw5wlT5WlUmVsx49OVyxb4tZEYfKvZyKjMSQbI6TvZiwrimQRFfJYB-vi4vW3fSLZmrySxmu6UKfbwa-nOMKJPHvNm4cxwn7uMmiAw75TPEoJxN2szXbkKMi6qLQNvL08YUAAbWGGj5fawVdsvhnZHOdYtHiXFcmZG_M6DgZd_DVNfAqDlZ1hPxhWup7GTiLNl6jg0QyaY3wBlaz97As6B45EMnB5eOAauyOkeXqT1OT7xKtrQ6YvOmPAYLPeBKJURm_gyf-ZDJyiMqwW7scY5tOjC9asqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ۴ کشته شده هوا فضای سه پا ۱۱ شهریور ماه در کرمانشاه
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22181" target="_blank">📅 16:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بیانیه ارتش:در حملات اخیر آمریکا به ایران، که دو شب گذشته انجام شد،
3 خلبان نیروی هوایی ارتش و
6 نفر از پرسنل نیروی دریایی ارتش کشته شدند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22180" target="_blank">📅 16:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ویدیو از دیدبان اتاق جنگ از خمین
🚨
🚨
عراقی ها مردین بدزدین
😂
😂
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22179" target="_blank">📅 15:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from....</strong></div>
<div class="tg-text">چند بار دیگه بگی زارتان زورتان کارشون تمومه</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22178" target="_blank">📅 15:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22177">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-cPxal1WdOSqYmzHRXdhvAzQBCUARHlwVJGuG3LvZUTxOwTEl95uzNiZzP9M0ZIj-5I8v-AYnCj26QVc0iEe00rWSVx71G5uTd_x5z_HHl7S4r2fihxuyBiMa9TJFlz0XBO6npT_Y46G8CEDG87LqCKgNIYuzEKzC7jb94_3O0VNte5f-dgsMb2uu8e_0Ijyw9iNlSnBDiJ5LxCRpVdLnY0rz6AiW4Bkhlkln5zz6CYXUfjMouNzQDc5Kk7o8P0Y9yKL60A1ve8vWWF_Mi796iAHZ3dq2h6we9pYPCOy_kKDSd0CuPqZooV3ZaTg9pRD61Ge_8NQpalwSoCv5Dn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث: حجم نفت هرمز برگشته است!
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22177" target="_blank">📅 15:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22176">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpmK9-rqg12sVEVe7Srbs5iKur_57QTI92vVUFkOjKkCzs_5iWu6OYzAAfFLKd_1fNeMY-X3rhtq96AZ6ZAvlX8hzk7m2Po7Om7lHeQvp_E30J1yhX4JwAqrGRsrK-_gCtRLYykgNPOfjkCSaDSW6G-Sq-Ygd6jID3sFpJ3nNMaZndVDHKFepDkD0CgSrXeK-YOW3msPrP_fcPwmy9LD0qy1T9bjuUARQNpCi94anQSEDIWIr50xEQ3EQDk_LLPjSY-l-hnDB1B9Lf2Oia68BTrIsBo9J7fNxAjVEDsS2m-rYNjKIAiPlalbNZfMyn72vDqNZ1vfGvpmolm_e8TKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در واکنش به این گزارش نوشت:این عالی است!
واشنگتن‌پست: سوریه در حال تلاش برای تبدیل‌شدن به یک مسیر جایگزین برای انتقال نفت و کالا، در صورت ادامه اختلال در تنگه هرمز است. دمشق با تکیه بر موقعیت جغرافیایی خود و مسیرهای زمینی و بنادر مدیترانه، می‌خواهد از نیاز منطقه به مسیرهای جایگزین هرمز استفاده کند و به یک مرکز ترانزیتی مهم در خاورمیانه تبدیل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22176" target="_blank">📅 15:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22175" target="_blank">📅 14:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22174" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🫶</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22173" target="_blank">📅 13:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22172">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMo ya</strong></div>
<div class="tg-text">داش همین طوری الکی ویس بده فقط صداتو بشنویم</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22172" target="_blank">📅 13:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارتش ایران اعلام کرد که امروز صبح، امارات و کویت را هدف قرار داده است:
ما "سیستم‌های ارتباطی هوایی"، "انبار تجهیزات" و "پناهگاه‌های هواپیماهای جنگی" متعلق به ارتش تروریستی آمریکا را در پایگاه احمد الجابر در کویت، با موشک و پهپاد هدف قرار دادیم.علاوه بر این، پایگاه‌های استقرار نیروها و "سیستم‌های رادار" متعلق به ارتش آمریکا در امارات نیز مورد هدف قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22171" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نرخ دلار ۲۲۴،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار :نامعلوم ! تونستی بخر!
تتر ۲۲۲،۰۰۰ تومان (سقف تاریخی)
بیتکوین ۷۷،۹۵۹ $
انس جهانی طلا ۴،۴۳۴ $
نفت برنت  ۹۵،۲۹$
@WarRoom
🚨
🚨
🚨
🚨
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22170" target="_blank">📅 12:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f620a5c792.mp4?token=NV1_Q8pcqWw5rrIDx-bx9amBkBtf6hQN1sPo0aMozLXsuSNW_vvR_Xhem_Pfoay-urxCocTaCufJXKGSS-bY-ZSJyBvWVYa4QXLicJmsSWT0WoCYYewpiZnd88o_UQF8A759FIbb2ynO9GJrQoltnKf41oWPPuBXHRoEuMWWxz8r4FUTqND8T12pE_kBLHnJ2MXRgGk-weOMcszL-OnB_OiA9Z7MltDzLqOFVvyMrMcAKHalBhNPTLaCJcYI2J6NEkMYMg0tO5CfaWyX2pkLwtyN7Yuy6VFqR9mR05QeI7MWyNnJ0PlPHtS2yh-TZck2UPqOTQ5Yr_YjhjEzm24MfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f620a5c792.mp4?token=NV1_Q8pcqWw5rrIDx-bx9amBkBtf6hQN1sPo0aMozLXsuSNW_vvR_Xhem_Pfoay-urxCocTaCufJXKGSS-bY-ZSJyBvWVYa4QXLicJmsSWT0WoCYYewpiZnd88o_UQF8A759FIbb2ynO9GJrQoltnKf41oWPPuBXHRoEuMWWxz8r4FUTqND8T12pE_kBLHnJ2MXRgGk-weOMcszL-OnB_OiA9Z7MltDzLqOFVvyMrMcAKHalBhNPTLaCJcYI2J6NEkMYMg0tO5CfaWyX2pkLwtyN7Yuy6VFqR9mR05QeI7MWyNnJ0PlPHtS2yh-TZck2UPqOTQ5Yr_YjhjEzm24MfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خطاب به هگ‌ست در مورد ایران: شما شب گذشته کار بسیار خوبی در مورد ایران انجام دادید. شما آن‌ها را به شدت شکست دادید. بسیار عالی.
ما در این زمینه، به هر حال، پیروز می‌شویم. ما باید این را بگوییم، زیرا رسانه‌ها از گفتن آن خودداری می‌کنند.
با این حال، حتی روزنامه نیویورک تایمز هم گفت که ایران اخیراً وضعیت خوبی ندارد. این یک خبر تکان‌دهنده بود وقتی آن‌ها این را گفتند.
آن‌ها هیچ هواپیمایی، هیچ چیز مربوط به هواپیما یا کشتی ندارند. همه آن‌ها در اعماق دریا یا در انتهای باند فرودگاه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22169" target="_blank">📅 11:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رویترز به نقل از منابع: ایران به آمریکا هشدار داده است در صورت حمله اسرائیل به ارتفاعات «علی‌الطاهر» در جنوب لبنان، تهران با قدرت پاسخ خواهد داد. بر اساس این گزارش، نیروهایی از سپاه پاسداران در کنار نیروهای حزب‌الله در این منطقه و شبکه تونل‌های زیرزمینی آن حضور دارند. ایران هشدار داده هرگونه عملیات همه‌جانبه اسرائیل برای تصرف این ارتفاعات می‌تواند با پاسخ مستقیم و گسترده تهران روبه‌رو شود.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22168" target="_blank">📅 11:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش پرتاب ۴ پهپاد از سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22167" target="_blank">📅 11:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22166">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVGDfPmafGiWzhJXh8UMfIhULb2A7vNcgh9VhncQk6bjsLsqLfFrvdUt9F58ECCtGmtOOILRV4Hxt69BWf5Zow5H8D857SglIp4frMXj_xAQDNrL-o-UYA6LbsbWJ0bzIr11rsGQjDLlxYqGwc7F6oAUR1AU-07ZE_ieiwuok7crEadj_B7dxYzWyF-aoXTRFI_pig5dyPa_UQeHHfj8QoxwTjq1nsPOwumANOdwElUWr4jqgVaPzomqUvorqxyP6hh8hPZ9VD71PY5goixWHm3BV6vng93WiQlTB5wxowJeZ4HfgIlJyt3EJSX_wbLrOESf6JQ7HmxInSNTKZf51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوون دهه هشتادی ۲۳ ساله کرمانی
زمین خودش به ارزش ۹ میلیارد رو وقف مسجد جمکران کرد تا اونجا رو بسازن و معارف اهل بیت رو گسترش بدن.
@WarRoom
دیگه کرمان هم جنس خوب نیست و همش صنعتیه</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22166" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وال‌استریت ژورنال: پیت هگست، وزیر دفاع آمریکا، مأموریت و استقرار شماری از نیروهای آمریکایی در منطقه را تا سال آینده (۲۰۲۷) تمدید کرده است؛ اقدامی که نشان می‌دهد واشنگتن خود را برای ادامه درگیری با ایران و حفظ گزینه‌های نظامی بیشتر آماده می‌کند. در حال حاضر…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22165" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بر اساس گزارش رویترز، شماری از مقام‌های ارشد کاخ سفید در حال بررسی این احتمال هستند که پس از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر، در صورت ادامه درگیری و شکست تلاش‌های دیپلماتیک، اقدام نظامی علیه ایران را تشدید کنند. با این حال، دولت ترامپ در حال حاضر…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22164" target="_blank">📅 11:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رویترز هک شد
مالک خبرگزاری رویترز در بیانیه‌ای مطبوعاتی اعلام کرد یکی از واحدهایش با حادثه امنیت سایبری مواجه شده است.cاین حادثه امنیت سایبری در پلتفرم مدیریت پرونده‌های قضایی C-Track که برای مدیریت دیجیتالی پرونده‌ها و اسناد دادگاهی استفاده می‌شود، رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22163" target="_blank">📅 10:31 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
