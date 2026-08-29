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
<img src="https://cdn4.telesco.pe/file/h2tjply15PTLXzwr7pu0qEV957XkvB22ZlnthkrZF9BawlCuhHm6kYYYq6bwozCTHCU1uBV9ZbMCa5Wxh50_ThHC-UpWTT4A1t76eSTguaF-wTfYVDrXV4X4hJcnnlYjJHQl4WRE5sebln5j2mvGPZ6V8pzLFeZaC2PM6MebgjdkKsNme626Q4RRQHE18pFZ127LBIBP2DOArjhlydEoNPiHZmsVAR4WkAGvrwFUL1Cu098W4NOw6nohbhmb-fyb8bwxqRo-_1FL3Ho3AntLHdwOHyLFCD1T7k0RSYK94mu1yr9tzy6CBbgM5ReAvLu1ar0SvlCKqDcU41gh18RseA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-458855">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ موعود رسولان</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/farsna/458855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
خبر آمده پشت خبر، شده بتکده زیر و زبر
🔹
نماهنگ موعود رسولان با صدای حنیف طاهری
@Farsna</div>
<div class="tg-footer">👁️ 659 · <a href="https://t.me/farsna/458855" target="_blank">📅 19:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نتایج امتحانات نهایی اعلام شد
🔹
آموزش‌وپرورش: نتایج اولیهٔ آزمون‌های نهایی پایه‌های یازدهم و دوازدهم اعلام شد. دانش‌آموزان و متقاضیان ایجاد یا ترمیم سابقه تحصیلی می‌توانند نتایج خود را در سامانه مربوط یا از طریق مدرسه مشاهده کنند.
🔹
از زمان اعلام نتایج، ۷۲ ساعت برای ثبت اعتراض و درخواست بررسی مجدد فرصت وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/farsna/458854" target="_blank">📅 18:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">دیوار چین مانع فینالیست شدن زنان والیبال ایران شد
تیم ملی والیبال زنان در مرحله نیمه‌نهایی رقابت‌های قهرمانی آسیا و کسب سهمیه المپیک لس‌آنجلس مقابل چین ۳ بر صفر شکست خورد. ایران با امتیازهای ۲۵ بر ۲۲، ۲۵ بر ۱۲ و ۲۵ بر ۱۹ نتیجه را واگذار کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/farsna/458853" target="_blank">📅 18:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458852">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e45864b05.mp4?token=Y0J0qcZUaQUSFw-ztOZt8o5iO4QZCMtJKQet6z5klunvUmv3IPUGIJzQSIJSh7XO44-H9QygrTrDUR5LyjHEPjlqcNXL_GOC3ARAKH1z28tkBsrAGirGoeM926L3YWbI2jVrPuKUpr5S1lyUjoAvlYhlY7qmXJMlX_s4QcH8rqXsbIZfsbaT7lCJu_jQJqauKLYNyXYcef24nGxWDTlpsHgYtwevuLG1oLz7fIsyXpXk3QJTH4GLXfPe00pT_fCIREgrkCT8ohKAs3wtFxP8xo1iYH6NIrE8fcX3uoY8O2QAh7qQ0_3oo6x9hXGQqzzOP4hAEm3KEs2BuyMGQIZTWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e45864b05.mp4?token=Y0J0qcZUaQUSFw-ztOZt8o5iO4QZCMtJKQet6z5klunvUmv3IPUGIJzQSIJSh7XO44-H9QygrTrDUR5LyjHEPjlqcNXL_GOC3ARAKH1z28tkBsrAGirGoeM926L3YWbI2jVrPuKUpr5S1lyUjoAvlYhlY7qmXJMlX_s4QcH8rqXsbIZfsbaT7lCJu_jQJqauKLYNyXYcef24nGxWDTlpsHgYtwevuLG1oLz7fIsyXpXk3QJTH4GLXfPe00pT_fCIREgrkCT8ohKAs3wtFxP8xo1iYH6NIrE8fcX3uoY8O2QAh7qQ0_3oo6x9hXGQqzzOP4hAEm3KEs2BuyMGQIZTWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: اسنپ گاز در راه است
🔹
همان‌طور که پلتفرم‌های حمل‌ونقل توانستند ساختار سنتی این حوزه را تغییر دهند، در حوزه گاز نیز می‌توان از ظرفیت اقتصاد پلتفرمی برای افزایش بهره‌وری استفاده کرد.
🔹
تا روز گذشته ۱۰۲ قرارداد تجاری در ۲۹ استان کشور منعقد شده که برخی از این قراردادها به‌صورت مشترک میان چند استان بسته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/458852" target="_blank">📅 18:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458850">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba4a21fbd.mp4?token=sGn3rSah-jsRl_kUYvC1k0NWJy6JIFchjwy6TULtm4AcG-qLpdN_YtitUaYsI0jvOkhWoYYTY9ifaloIOYNFV3CShhHHeG8wTzatA1wESjazdzw78b_enmlHveqzG6Mqwu_1B-J9IwEg-UC_4muRClSuCthmtp4tmCJA6gjvKqe5fvGf5gRHgvVCvxcR6yRb3qF0KCD_83jBBOk2c1g_-Xd1OEv69juInkzZC9oHTRDoeBs4HxaHjsjkn9h1gZ9g0A1RyzfNhzOU9faEpdhtdp6WQah5wdLWsLvbxD7wb6iP0-fF67mQeGQZkAgleyxLNBG6LqbLC6Qbrqo1hBmHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba4a21fbd.mp4?token=sGn3rSah-jsRl_kUYvC1k0NWJy6JIFchjwy6TULtm4AcG-qLpdN_YtitUaYsI0jvOkhWoYYTY9ifaloIOYNFV3CShhHHeG8wTzatA1wESjazdzw78b_enmlHveqzG6Mqwu_1B-J9IwEg-UC_4muRClSuCthmtp4tmCJA6gjvKqe5fvGf5gRHgvVCvxcR6yRb3qF0KCD_83jBBOk2c1g_-Xd1OEv69juInkzZC9oHTRDoeBs4HxaHjsjkn9h1gZ9g0A1RyzfNhzOU9faEpdhtdp6WQah5wdLWsLvbxD7wb6iP0-fF67mQeGQZkAgleyxLNBG6LqbLC6Qbrqo1hBmHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان ثبت احوال: تا ۲۰ روز آینده «کیف هویت من» که شامل خدمات بدون مدرک هویتی است در سامانۀ سهیم برای همۀ مردم بارگزاری می شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/458850" target="_blank">📅 18:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458849">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00b02f4a4.mp4?token=s-eMtXniAItMyH_Hv46w7zL7Gmm9Z7VkmK7ia9vwJlPYc_b-UX6NP7bjGO38t0OeJmUuvriMR4SDKKZ5Tq4G_3BRN8disRzkA6_wfpn4gG7F3dRAszF-gswND8xNhGogJ1kWIexYz3NjRoTbFJ_Ume9CwjyH2Kw0mV0iB7GhCBcUt-HDs775y6cZUIK0IRMtL1O5wAXqWiOyB7iH2xKse_eu5tEt9EH8oR1sG7W_Im7nEaXvacdG5wRrjCdcysZHCNRbsPwjuhOCBG1AmFuF7fO8r10L64C0SQ7B7M80E1ZPwqaGgieBWwDLVIiqE_EvxEhMXbAW1XskReW9aROtbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00b02f4a4.mp4?token=s-eMtXniAItMyH_Hv46w7zL7Gmm9Z7VkmK7ia9vwJlPYc_b-UX6NP7bjGO38t0OeJmUuvriMR4SDKKZ5Tq4G_3BRN8disRzkA6_wfpn4gG7F3dRAszF-gswND8xNhGogJ1kWIexYz3NjRoTbFJ_Ume9CwjyH2Kw0mV0iB7GhCBcUt-HDs775y6cZUIK0IRMtL1O5wAXqWiOyB7iH2xKse_eu5tEt9EH8oR1sG7W_Im7nEaXvacdG5wRrjCdcysZHCNRbsPwjuhOCBG1AmFuF7fO8r10L64C0SQ7B7M80E1ZPwqaGgieBWwDLVIiqE_EvxEhMXbAW1XskReW9aROtbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ اخیر به جهان اسلام درس ایستادگی دادند
🔹
اینکه مردم ایران در مقابل ظلم ایستادند،  درسی است که در جنگ اخیر به جهان اسلام دادند؛ مردم ایران ۴۰ روز در مقابل بزرگ‌ترین ارتش ظاهری دنیا، در حالی که ارتش‌ها و کشورهای دیگری نیز در کنار آن…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/458849" target="_blank">📅 17:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458848">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d96339666f.mp4?token=jenteTuh8PHQ5qTnN5xvFpjI7guiYXuvyjJ5AUBWlV4IHzD7UwyLb6qUltNzwKAONV95lz6WYif0ouB_ZaC8aYeYgiiGoz0L9H9gPtUTpZZX-kylbRrW5KgwUx3HuOrVGbnxXz7aWsiHvRTQvfrbphUXW2zqxqYMG25-tSRprzXIgEOM_72U3sM9pWPiYWNSkDi-G1gAh-1ZMK_6KWMbOuB3XWRKv0JdeLG1db0NPf_DlQ5mXYkWZQ2Mbkr0wjUgVYMRmXHi3JS83cc9l15QGvGg2oKgPo7mvz-qag77fRUrXhVpppd_CyuU9L2a7iU_REYyTupDUXNMncGeDpXnvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d96339666f.mp4?token=jenteTuh8PHQ5qTnN5xvFpjI7guiYXuvyjJ5AUBWlV4IHzD7UwyLb6qUltNzwKAONV95lz6WYif0ouB_ZaC8aYeYgiiGoz0L9H9gPtUTpZZX-kylbRrW5KgwUx3HuOrVGbnxXz7aWsiHvRTQvfrbphUXW2zqxqYMG25-tSRprzXIgEOM_72U3sM9pWPiYWNSkDi-G1gAh-1ZMK_6KWMbOuB3XWRKv0JdeLG1db0NPf_DlQ5mXYkWZQ2Mbkr0wjUgVYMRmXHi3JS83cc9l15QGvGg2oKgPo7mvz-qag77fRUrXhVpppd_CyuU9L2a7iU_REYyTupDUXNMncGeDpXnvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ اخیر به جهان اسلام درس ایستادگی دادند
🔹
اینکه مردم ایران در مقابل ظلم ایستادند،  درسی است که در جنگ اخیر به جهان اسلام دادند؛ مردم ایران ۴۰ روز در مقابل بزرگ‌ترین ارتش ظاهری دنیا، در حالی که ارتش‌ها و کشورهای دیگری نیز در کنار آن قرار داشتند و از آن حمایت و پشتیبانی می‌کردند، ایستادند. این مقاومت یک شگفتی بود و مردم ایران با ایستادگی خود درس بزرگی به همه دنیا دادند.
🔹
وحدت جهان اسلام را در هر شرایطی دنبال خواهیم کرد. عربستان، مصر، ترکیه، پاکستان و دیگر کشورهای اسلامی، خانواده بزرگ جهان اسلام را تشکیل می‌دهند.
🔹
اختلافات وجود دارد و حتی ممکن است اختلافات جدی با کشورهای اسلامی داشته باشیم، اما باید همۀ این اختلافات را کنار بگذاریم تا جهان اسلام بتواند در برابر زیاده‌خواهی قدرت‌های بزرگ بایستد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/458848" target="_blank">📅 17:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458847">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
تصاویر بالگرد چینی از  سرچشمه سیلاب مرگبار در مرز چین و نپال
🔹
یک بالگرد چینی خود را به نقطه‌ای رساند که در آن
یک یخچال طبیعی فروپاشیده و حجم عظیمی از آب آزاد شده بود
.
🔸
این حجم آب با حرکت به سمت نپال، خسارات گسترده‌ای بر جای گذاشت.
این پدیده که به آن
GLOF (سیلاب ناشی از طغیان دریاچه یخچالی)
گفته می‌شود، یکی از خطرناک‌ترین پیامدهای ذوب و ناپایداری یخچال‌های طبیعی در مناطق کوهستانی است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/458847" target="_blank">📅 17:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458846">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhwWhbnacqHzjb4CObCGNiso97Wa5Yq00Vd9m8QOUAf363FPOLLg2K31-v8eKggHOdVArpBY8nu3tCf-jyvWSwSfatAmQ4IRxfa4OX3a24w1zXPLDXVeaojHphkU5CKvOxaZAGgbLQ_PHDkyg8bcFxYRYlmSUF0V0D9R7caTZoTk99P0CoDW_rpe-bzaoGGe4xw-FnwKjhZr-IEQMVFLhD7sHwYbrrNifg_4fwCcNU6ZMLSHmwtPAK-Wiz1S99KuR2Z0Jde5BBswpI11qdEe5LUxPXxDeh0Ue_3Ow6PCphAPEqBu48nYy2ISdnzUzOzM7_U2q0W9fDA1MuXoygIY2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموس اقتصادی ترامپ تحت فشار جنگ ایران
🔹
رئیس فدرال رزرو آمریکا می‌گوید که تورم همچنان بیش‌از حد بالاست و احتمالاً بانک مرکزی در ماه‌های آینده مجبور خواهد شد برای کاهش آن، نرخ بهره را افزایش دهد.
🔹
حساب امریکن اکونومی نوشته است که «نرخ بهره ناموس ترامپ است» و افزایش آن یک عقب‌نشینی بزرگ از سوی او محسوب می‌شود.
🔹
هم‌اکنون آمریکا تحت فشار شدید افزایش نرخ بهرهٔ اوراق قرضهٔ خزانه‌داری قرار گرفته و سقوط ین در ژاپن نیز بر این فشار اضافه می‌کند.
🔸
روند طی‌شده درحال‌حاضر مشابه اتفاقات پیش‌از بحران مالی بزرگ ۲۰۰۸ آمریکا است.
🔹
طبق ادعای بلومبرگ در ماه گذشته، ورود غیرمحاسبه‌شدهٔ آمریکا به جنگ ایران فشار اقتصادی بر پارامترهای اقتصاد کلان ایالات متحده را به‌طرز قابل‌توجهی افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/458846" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458845">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGWCLZoiPOdFMgB40SBJdNilSDDbl_E4QD3T4-rjP4iklcU3H9MvLTZuC52UW31UVQWmWL0ziPochSMPwEEdjVnjkFj79sjlX3ej4sY1ch4dZZM4v8o36yuDZxR5b7laFTJ7XHMK_pkDtL42t0lk468M2AGRdhSyRLRlc32_qfeAxZr18Ed9d4moim2yCb-3IE4EjKpGEmeoex8Piq4SyWxRha56z44Qiz7OTh54IKvvCpNtr8E4HTpVXT1Zg5FV1OIn2WdvcQA0g-5t7SFvlXyOmnGnAFAtArDzDNBzxm9nWz0ODYkP4i-nbui3ltlZyaaDjXb05qL08SazgUv53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفر ول کن؛ روایتی از یک اظهارنظر جنجالی و پاسخ به آن
🔹
ساعاتی پس از آنکه محمدجعفر قائم‌پناه، معاون اجرایی رئیس‌جمهور، در اظهارنظری بحث‌برانگیز درباره توقف غنی‌سازی هسته‌ای صحبت کرد، واکنش‌های گسترده‌ای در فضای سیاسی کشور شکل گرفت.
🔹
این اظهارات که با جمله…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/458845" target="_blank">📅 17:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458843">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiM3q9hnYioplrIcidjzzeYCzTf6DTn2AbhKI63XLFPuO3n7C8OK3Komy7wuIZ2tTn8OOfatAzd7LVCok_wfhiFnS4193QM9IhqfLZKZt7jt_d3LokbXqa1uXnSEUHhpjsZzOb6sU6r8_9E1hRwGxKvSoplh0Bj_kj8o62Bwo-TMokZeGw9vxhx-ek0FC7hzJZ3jg9aJoYcXPZC6_kTWmyxsAqbCqaxzFU5KSpYOfpiH9DJCsXsIPNwLp9ekFN2kxqtEU95y5k3n52ch3Tcs99188xGDlVj6yvbwe-UkMXX3drEu67bviM2Ap4Oi-0u2fk5t9m1d9IKQpwzRctLQCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cn1IZAuOmswCOdiMRMeghu1FUmywfTgn3W9BXp_iPzSu8BCHpT3v-pDKYksxJvM0f8do7lAkPOm0Bw_ECgUQyQe3ZydoML-u4p_LxGyj1OOcdtU990J_mFBukErBHKBH5Q0P7O6Rto4hGGai4sNRiWuunhOA2jkeQfsNASFuHPyvENk3M_bu0BNP0vJc-VckDRyvJJtArHy5K7MHULioeGpmo6LiAnRIUM2xUSN2x5N4b2HUVUr7gAs546JfUDZritBupnGe5WljKXGbSkXJ1-KbVUK162uetGosM4yw5vUIBmj75OVkgUP9-5cbMQ5SE-0ifUwbbJikJdRCWDssYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو حملۀ هوایی اسرائیل در جنوب لبنان
🔹
منابع لبنانی بعدازظهر امروز از ۲ حمله هوایی رژیم صهیونیستی به شهرک المنصوری و همچنین یک حمله هوایی به منطقه وادی الحجیر در جنوب این کشور خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/458843" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458842">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سرکردهٔ شبکه تراستی با بدهی ۷۰ هزار میلیارد تومانی دستگیر شد
🔹
مرکز اطلاع‌رسانی پلیس اعلام کرد «الف.ل»، از سرکردگان شبکه تراستی که طی سال‌های گذشته مبادرت به دریافت ارز حاصل از صادرات کرده بود، توسط کارآگاهان پلیس امنیت اقتصادی فراجا شناسایی و دستگیر شد.
🔹
براساس اعلام پلیس، بدهی این فرد به شبکه بانکی کشور ۳۰۰ میلیون یورو، معادل بیش از ۷۰ هزار میلیارد تومان است.
🔹
این فرد تاکنون از اجرای تعهدات خود امتناع کرده و متواری بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/458842" target="_blank">📅 17:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458841">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJqpTMFaUUxkqm8mFoImJxLQCltEZPDffYpk4aUFjhpMjhoiwALmJFZVnamzlRJPnLlBrbQI31mS6ppd-4fV6XJa0HhNqJYJWNugjM19rIa-qOdr5_WCCxlQfKcFryhfVaOmNFvysFLgPGsFqzmIV-S70t68vEJ3QkjSeVp9ks3M4Lir5DQqDAhxaI37iSqfay4s_mQgKmR0Gr23eInN2Abo0BAm4EZJ7SoZIpapZ54-QfePzjE8nRLPVH-Hd2yi34FoZ-lbpd0N6V9ZX4jGxt15_SFwDJXt5El87V07FuUCklblqaUaaeH7ta4TYY-BtEgM-YDzFOuRk8iqOzcIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که ترامپ از آن می‌ترسید، سرش آمد
🔹
جیمی کارتر، رئیس‌جمهور ۴ دهه پیش آمریکا بود که ترامپ با تمسخر ضعف‌هایش، برای خود در انتخابات رای می‌خرید و می‌گفت که نمی‌خواهد شبیه او باشد. دو ضعف بزرگ کارتر که در تاریخ آمریکا از آن یاد می‌شود، عبارت‌اند از: «شکست در جنگ با ایران و تورم برای مردم آمریکا.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/458841" target="_blank">📅 16:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458840">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHLlFKBzJJZSArPr2AtFeH1X8RYpueAUULjnwS-Q0SskVc1cjgX6YO1rrcwR8HbgVWXvqIf-gz5BqYpvFrKrQkLJYJK30UGZ5CmG57D4udqq_-_tP7xn5vyNiRelomcN7QylzhPazMJU2Gm2G-q5QqigFR2AtgDTubShWo6ict1vAuj_L4U_HqcqWczvN1p3HyIQPOlvdOcmNon0D17_0ufT5IStNL9XSUhn2cmcOWkgwA2HB65OElis4j4yUkrfy4ZLf4zeK4oBbjG8PaRejOaYghdOha--DZMLjYDu85jbxgrXciITDrYyDVolpRulNkF5iTvGazxGiKaS95biKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف ۲۸۰۰ مگاوات برق غیرمجاز در کشور
🔹
توانیر: اوج بار مصرف برق در تابستان امسال نسبت به پیش‌بینی‌ها ۳ درصد کاهش یافت و حدود ۲۸۰۰ مگاوات مصرف غیرمجاز از شبکهٔ برق کشور حذف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/458840" target="_blank">📅 16:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458839">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قالیباف: ثمرۀ وحدت چشاندن طعم شکست به دشمن بود
🔹
پیام رئیس‌مجلس به‌مناسبت هفتۀ وحدت: ایران اسلامی، سرزمین همزیستی برادرانه اقوام و مذاهب است امروز وحدت شیعه و سنی در ایران، نه یک شعار مناسبتی، بلکه یکی از پایه‌های اقتدار ملی و یکی از سرمایه‌های بزرگ امنیت و پیشرفت کشور است که نمونه بارز تحقق آن در جنگ های تحمیلی اول و دوم و سوم و ایستادگی همه ی مذاهب و ادیان در چارچوب ایران عزیز در مقابل دشمن بیگانه و خونخوار بود.
🔹
تحولات سال‌های اخیر در منطقه نشان داده که ملت‌ها و دولت‌های مسلمان، بیش از گذشته به این حقیقت پی برده‌اند که قدرت‌های بیگانه و دشمنان اسلام، نه قادرند برای ملت‌های منطقه امنیت پایدار فراهم کنند و نه اساساً اراده‌ای برای تحقق چنین امنیتی دارند.
🔹
امنیتی که بر حضور و دخالت قدرت‌های فرامنطقه‌ای بنا شود، امنیتی شکننده و وابسته است، اما امنیتی که بر اراده ملت‌های مسلمان و همکاری برادرانه کشورهای منطقه استوار باشد، می‌تواند پایدار، عزتمند و ماندگار باشد.
🔹
امروز نشانه‌های این بیداری را می‌توان در شکل‌گیری پیمان‌ها، همکاری‌ها و ترتیبات جدید منطقه‌ای مشاهده کرد. پیمان‌ها و ترتیبات جدید منطقه‌ای می‌تواند نوید بخش آغاز مرحله‌ای تازه باشد که همسایگان مسلمان به جای بیگانگان بر ظرفیت های خود تکیه کنند و به جای رقابت‌های فرساینده، مسیر همکاری و برادری را برگزینند.
🔹
ثمرۀ وحدت بین مسلمانان به‌ویژه در تحولات اخیر، چشاندن طعم شکست به دشمن و پیروزی‌های پی در پی با عقب راندن استکبار از مواضع و رویاپردازی‌های خود بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/458839" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458836">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDlU53zqoQI7g0re8GGKTIGrQc4pMoSBb5BJTPI6-YQbh7GbGw9SuF4e1u-iPRuG_l2038bHWMuNwGHg3E8fxkHfq82ZLdF-1bICsB2BZ6CwFxSOb6G-149GzjHp4rROozdbUSdB_2pzR3O0_fJj0WOnY_4n2YxArhwFxwftLk5_qoI7slJZpErijd9D1u45ApDyNSy5j2yOmLyl79VC30hybWadsPF7jL7MgsvtgSlYnpbg8GFBcxZ5dGWNlKUI0GEXHMGsrGnCv-YE1cA0O2i6KJj-A6IWM22c7eVpoBzte-8vEsgwZCp1SIULVT2Dm6ZG6xaoQNiRC6ZUqMHCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjSAsmFOc1l5ByO8YyUj_pRDY371O_axk0ursrlgC5PtvH3d2X2YmSBs_sJiQgh-TEIhyhDMVc0JSxHpK-pMrW8oYkL1cuknV1oWuou8CoscJsY617PJ_n1X_0VTH5N1B1B0ivMHqBOubF0pek9BNIJIUMjPypEERxDVWcAxvabqLkpFiIiGzZrqjetLijhBKcT_QBQtOVrtdvmNPgwnFcT5wAdhPKNlXMwShxznCFdTKo36FkDSjqMPdsP_C5jtF9P_IraWQtkBl9ssVBV3uxY-yRJSf3sah9by4qPTxYSw7rGnvPTZIOG0kXCP-LMjVx9N518hL0fAnM5zSa6YSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9WacwXSs0-QO-TC9_vls688Z2sAMiplXA5ZpUNTXCvvrZ_ZRonuAwXLOnULwpT0-5VJM0ylKg-_Qyr9D3boOc5U50OWrjNwV_ng4Q_0JRUQilw3WA7q_d8Ihbljqy6cuMV2ga39oJ-kf-KNwADy-F7Hwe1pvB6mDk7ZhgtSqTH46e-l2-RmAt0_PUNRLrs5TRaYZcXe3VBhsmAXFVljYNTg9yQtEZJq9l6L59W3fcIMZhPX6oTcxbcLEz-tfHiG3Skuyi4tjqS06f2OcMgHz56Dab03A5i6BDTOrRj_onnPGGYWRkcCj5emtLZ6JxChIlfb6HXujHNnMrF6UwCwLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
مطالبات مردم از دولت چهاردهم در سال ۱۴۰۵ چه تغییراتی داشته است؟
@Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/458836" target="_blank">📅 16:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458835">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هراز و کندوان یک‌طرفه می‌شوند
🔹
پلیس‌راه مازندران: ساعت ۱۵ مسیر جنوب به شمال آزاد‌راه تهران-شمال و جادهٔ کندوان مسدود شده و از حدود ساعت ۱۷:۳۰ از خروجی مرزن‌آباد به‌سمت جنوب یک‌طرفه خواهد شد؛ جادهٔ هراز نیز به‌صورت مقطعی یک‌طرفه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/458835" target="_blank">📅 16:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458834">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دو حملۀ هوایی اسرائیل در جنوب لبنان
🔹
منابع لبنانی بعدازظهر امروز از ۲ حمله هوایی رژیم صهیونیستی به شهرک المنصوری و همچنین یک حمله هوایی به منطقه وادی الحجیر در جنوب این کشور خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/458834" target="_blank">📅 16:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458833">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5EurF7KslyaqTzIpv4Zy-0sdEqTJHUmj32DvAUHgW47TaCIEMTG5i_x4CK20Vmfq75GK7f2r5Y95cIIaoVJAPAQfXRU8f8_u8I1GpldcCZlurZkfot5dd9bI01343UU80ClnYKfHCqy3fH6FNFFWm18w-K0xJrIOn9D1zcqAbjo4hVv-csEKs-EuqTsLBVBxc61qW-fl2kik0wOa4bOWsHJTAPjU-N4T3urLd6H9pzSZhnf4z3yXh-JZuRSYFIY43k3jMaP78qO3tPl8tHVAjw6zd-exASh_GTmieC076hrOcjjoqCxhnrMbgWI1BnGgZXgouYbqgSb_g3t9NYyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران از سه‌شنبه خنک می‌شود
🔹
هواشناسی استان تهران: از روز سه‌شنبه شاهد روند کاهش دمای هوا خواهیم بود که این روند تا پایان هفته ماندگار خواهد بود؛ تا روز دوشنبه وزش باد نسبتاً شدید خواهیم داشت.
🔹
احتمالا بارش‌های پاییز امسال در کشور بیشتر از نرمال پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/458833" target="_blank">📅 16:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458832">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJGf4ZEZyBEM7LDPOw2EwTopeP43p82WOJGrPFjZvRYM7JeCYJGkbHew-fJSXuc3rtmHtPxkCgc9t3y5DHyRW1Dn-UplnyGq4NXh4_94jb4XCVwkHkjh04eh9my5QYN9tkJkOcJFMdwVThzxNp0I_hkPVf1MXEcMFOe0wA_qCToeXAHAzSmknSx9eweuIB22NAmAY2BNswT3EfwS0J96Eooac3xJflzpbUNm2DKqb_J5KcJR51o76W1GrT-c6rZyCXMnr_TzU8IhqTVl3BbtvjNpk7RltbXA_7smdXQThCujwDC3zUleiLxAOzQ3yiULxA5y39PFtVI2Ke41gEaGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: از ساختن قدرت دفاعی ایران دست نخواهیم کشید
🔹
سردار ابن‌الرضا: از ساختن قدرت دفاعی ایران دست نخواهیم کشید و برای تحقق ایران قوی، از هیچ تلاش و مجاهدتی دریغ نخواهیم کرد.
🔹
جنگ‌های تحمیلی اخیر به ما نشان داد که ایران قوی، ایران همیشه آماده است؛ ایرانی که باید همواره توان خود را افزایش دهد و برای تهدیدهای امروز و فردا آماده باشد.
🔹
ما در این میدان آموختیم که نباید به داشته‌های امروز اکتفا کرد؛ باید هر روز و بدون وقفه قدرت‌افزایی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/458832" target="_blank">📅 16:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458831">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab0b30a060.mp4?token=HDdXqeTwnN8f2RaFinywZHElIeHL0HQGcZCZuEVdtzdLsHHMTk-Z_1WHgVnEA0QqApGyt5VqXEcxXaKOYtNn2OfW8yA-XzXt0C_gibOcc2fxWfGJb3xjIVVSb8EibkKhaxwi8eO1nK8z3Czx1yfHC2_i12GqIwmxNONmmEbpiplPqZ__41Rc-7fg4XJrYtMksVje95eUAcz4AHS6w9oijW7itSNiwmS6bzNANJziXaCUwH2CzfUpRNvfFKO9feskTe4SHoIUTyggW50woKzJ6F92GVNAevTK1_AU9P1QDxb7-8mRaDvezo1-MjKV_qa3dZzc2U2P-81lZSbw-2FnB3pKbcyK3iAlRho5J69LLgg-wXit-dUfwIKpjTtry1uPeQbPuVLKgbpWzvTBffBEnkHXuxnFAMfUKnVWzxc8RKGTzkrsIpMFuJ_0Ygm_k5AppmCuSoqJS7VFsvgKLU_EsBIol1csPfQefsD-fgocFPlp78TLJTmJN1uvVaGfgbtwsyE8s2XExoXKPnH8GBZQ6NWtofPxFotEKVP20nNFg42UAI6za1Q2rE352ODW7KAhbmhjpqq9E2_ics-xInbIBplTywAuI3CSKbJi0iQRBFiHliAqWcSwcRGgYXPxuOPFE-zxD82o0TyKKR22EZehWHYkCm4oVkuaVlu1wES7brM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab0b30a060.mp4?token=HDdXqeTwnN8f2RaFinywZHElIeHL0HQGcZCZuEVdtzdLsHHMTk-Z_1WHgVnEA0QqApGyt5VqXEcxXaKOYtNn2OfW8yA-XzXt0C_gibOcc2fxWfGJb3xjIVVSb8EibkKhaxwi8eO1nK8z3Czx1yfHC2_i12GqIwmxNONmmEbpiplPqZ__41Rc-7fg4XJrYtMksVje95eUAcz4AHS6w9oijW7itSNiwmS6bzNANJziXaCUwH2CzfUpRNvfFKO9feskTe4SHoIUTyggW50woKzJ6F92GVNAevTK1_AU9P1QDxb7-8mRaDvezo1-MjKV_qa3dZzc2U2P-81lZSbw-2FnB3pKbcyK3iAlRho5J69LLgg-wXit-dUfwIKpjTtry1uPeQbPuVLKgbpWzvTBffBEnkHXuxnFAMfUKnVWzxc8RKGTzkrsIpMFuJ_0Ygm_k5AppmCuSoqJS7VFsvgKLU_EsBIol1csPfQefsD-fgocFPlp78TLJTmJN1uvVaGfgbtwsyE8s2XExoXKPnH8GBZQ6NWtofPxFotEKVP20nNFg42UAI6za1Q2rE352ODW7KAhbmhjpqq9E2_ics-xInbIBplTywAuI3CSKbJi0iQRBFiHliAqWcSwcRGgYXPxuOPFE-zxD82o0TyKKR22EZehWHYkCm4oVkuaVlu1wES7brM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قائم‌مقام اعتماد ملی: مدیریت رهبر شهید عامل جهش ایران در عرصۀ نظامی بود
🔹
گرامی‌مقدم: اگر امروز در این نقطه ایستاده‌ایم که توانسته‌ایم مقاومت جانانه‌ای داشته باشیم، به این دلیل است که با علم روز پیش رفته‌ایم؛ چراکه کسی که دانش سرعت و دقت را داشته باشد، برنده جنگ‌هاست. و این دستاورد، جز با مدیریت دقیق آقای شهید محقق نمی‌شد.
🔹
زمانی که شهید حاجی‌زاده اعلام می‌کرد به دستاوردهای بزرگی در صنعت موشک‌سازی، سوپرسونیک و هایپرسونیک دست پیدا کرده‌ایم، برای من اصلاً جای ابهام نبود. بسیاری از افرادی که از این مسائل اطلاع داشتند، می‌گفتند با توجه به تلاش‌هایی که نیروهای نظامی در ارتش و سایر بخش‌ها انجام می‌دهند، این مدیریت شخص آقای خامنه‌ای بوده که به‌عنوان فرمانده کل قوا، این مسیر را هدایت کرده است.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/458831" target="_blank">📅 15:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458830">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvuHMrSCPWWLzaG3Bmfs8kZ3_swfIImzI83ntESnTrM7RFAhc7oIQHYZ1FqTgkJnqQrKFdSsU5iJAzNACp8dy8VCGQW2ehN7xT4EExg68hKM2inAOyPel49c63bCYFMDzppNcwbTT4KkBjFMroMVoZjm0JFCus0ute9ji96r8od54Tl_YJxACe1Esygw1rRaaN0oRmYiPqiG4rhMJSYD0BRpYadpay-TCLkWm7OZ4QawvRK8GKAiRSIsIRJGv8JtRNqdqtffPO4zJKEvo5wW471yrLIt6op9yxEjHAHj5AXXnr5Rlo6fnjltIphlkqzofDugZv3aAy1Uf6ORO53Fzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تپش قلب و سرگیجه در تابستان نشانهٔ چیست؟
🔹
کم‌آبی بدن در روزهای گرم تابستان می‌تواند با علائمی مانند سردرد، خستگی، خشکی دهان، سرگیجه و تپش قلب همراه باشد و در صورت بی‌توجهی به وضعیت خطرناک برسد.
🔹
کارشناسان توصیه می‌کنند فرد دچار کم‌آبی به محیط خنک منتقل شده و در صورت هوشیاری، مایعات و ترجیحا محلول‌های الکترولیت را به‌تدریج مصرف کند.
🔹
برای پیشگیری نیز مصرف کافی مایعات، پوشیدن لباس‌های خنک و روشن، مصرف میوه و سبزیجات آبدار و پرهیز از تابش مستقیم آفتاب توصیه می‌شود.
🔹
در صورت استفراغ مداوم یا گیجی شدید باید فورا با اورژانس ۱۱۵ تماس گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/458830" target="_blank">📅 15:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458829">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1014363f0.mp4?token=bwBayn395G5uy-vwMm8Eei5GpTsRg8Wn6YQQJW3Jt96kpvpK3LJfjZCM1k_Qw8ih84jd4o4Ufm65fAxjCDHPHJcCEUEx0PQQvI2ralB57fdMRT0tMA8jtzQiCQUyVJSaW-Xjg-2Vrn2RGkTc9wfhZXto-ZTpU6kFqALKVwgeSTPEZyeQYtxOjKFyXeEmFP2eP4kEGf-2rL8d-jZ_vkDAqRSqpvy_TK2cz0eSvumrkSgU1ixvix7gwdWYbt9NG5amoCsHy47szBh0bmcTfIMoTVqpzdC0uIGzEunSMBDwV0TowLteExIqNukBpIHmGPPaG0Dxh_zzaGBqz277DLrw95rTteuEErFgohdTohLEcXP0yMBt0B1GWFUWrLDtYMcYfp2uKqrcmPE74kiEnjlXWXtQ65vijlMI_SmF4xHfK3Sppz1eKnuKrRvPTWX8k2OaeQDCB8ZjmnWYagPccJbugrGSR1lGUZVfivYvunHOyZT03-unS71EnghfmxGO8ecjxUB3xw9PRXqTL7HNoOZCaiTR-F3yPphVzJ8j8qMBn1dd6omXDJrUm8esaKkP8qhScG6Vn5Nv97i4oAB_-yOKvu5rUiJtTj05hVxGJV3VzcoXHAXHFnosK_uCk0xFZEN_EOIJi91D5Wbh46iJ_ttmTa45GORmYY-PDYntXEgJN5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1014363f0.mp4?token=bwBayn395G5uy-vwMm8Eei5GpTsRg8Wn6YQQJW3Jt96kpvpK3LJfjZCM1k_Qw8ih84jd4o4Ufm65fAxjCDHPHJcCEUEx0PQQvI2ralB57fdMRT0tMA8jtzQiCQUyVJSaW-Xjg-2Vrn2RGkTc9wfhZXto-ZTpU6kFqALKVwgeSTPEZyeQYtxOjKFyXeEmFP2eP4kEGf-2rL8d-jZ_vkDAqRSqpvy_TK2cz0eSvumrkSgU1ixvix7gwdWYbt9NG5amoCsHy47szBh0bmcTfIMoTVqpzdC0uIGzEunSMBDwV0TowLteExIqNukBpIHmGPPaG0Dxh_zzaGBqz277DLrw95rTteuEErFgohdTohLEcXP0yMBt0B1GWFUWrLDtYMcYfp2uKqrcmPE74kiEnjlXWXtQ65vijlMI_SmF4xHfK3Sppz1eKnuKrRvPTWX8k2OaeQDCB8ZjmnWYagPccJbugrGSR1lGUZVfivYvunHOyZT03-unS71EnghfmxGO8ecjxUB3xw9PRXqTL7HNoOZCaiTR-F3yPphVzJ8j8qMBn1dd6omXDJrUm8esaKkP8qhScG6Vn5Nv97i4oAB_-yOKvu5rUiJtTj05hVxGJV3VzcoXHAXHFnosK_uCk0xFZEN_EOIJi91D5Wbh46iJ_ttmTa45GORmYY-PDYntXEgJN5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تومُخ‌ترین پیامکی که برات اومده چی بوده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/458829" target="_blank">📅 15:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458828">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انهدام یک تیم تروریستی در سراوان
🔹
نیروی زمینی سپاه: یک تیم تروریستی که قصد انجام اقدامات تروریستی بر روی اهداف از پیش تعیین‌شده در جنوب سیستان‌وبلوچستان را داشت، به‌محض ورود به منطقه مورد ضربه قاطع قرار گرفت که منجربه هلاکت یک نفر و دستگیری ۶ نفر اعضا و پشتیبانان این تیم شد.
🔹
از این تیم ۲۰ بسته مواد انفجاری به‌همراه متعلقات انفجاری، تعداد زیادی سلاح جنگی به‌همراه مهمات و وسایل ارتباطی استارلینک کشف گردید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/458828" target="_blank">📅 15:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458827">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNRSGnjhUcXfv_hpa_uaOY6hmkdVfsrzUBUjw_Jx4eQuDXrGF4mTCYiJJ_CLqYpjpWuCosShxKiRBEtoSW4kbMAs8dDxLhI-nf7ydX4LpKzU0K5cS-49sCSBhvmN5SkrxN6S86YBUWHjkVHcq5-EOcCoVh6aomevgwexRvQeyWXESoxzSzqITYLG5qMVATTcRiQCZbD_p0xDLNc-7toFnzfxCVf6NfV_pEmGMh66h7XQ5iMuYtlJnuMGNf_kCJy1NpXKKXI2Jz9NoJ7gWJov7MObQpggn77y-Onzai6uN5UiR9-Hyyk_S2oPyo-0snE2FYiAIfY47nRwxM1rWtiYow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید گوشت قرمز به ۳۷ هزار تُن کاهش یافت
🔹
براساس اعلام مرکز آمار ایران، در تیر امسال حدود ۳۷ هزار و ۳۱۲ تن گوشت قرمز در کشتارگاه‌های رسمی کشور عرضه شد که نسبت به تیر سال گذشته ۶ درصد کاهش داشته است.
🔹
گوشت گاو و گوساله با ۲۱ هزار و ۶۹۹ تن و سهم ۵۸.۱ درصدی بیشترین میزان تولید را به خود اختصاص داده و پس‌از آن گوشت گوسفند و بره با ۱۲ هزار و ۲۳۴ تن قرار دارد.
🔹
عرضهٔ گوشت قرمز در کشتارگاه‌های رسمی در تیر نسبت به خرداد نیز حدود ۹ درصد کاهش داشته است؛ البته بخشی‌از کشتار دام، به‌ویژه دام سبک، خارج از کشتارگاه‌های رسمی انجام می‌شود و در این آمار لحاظ نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/458827" target="_blank">📅 14:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458826">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-YpgFp9M_mflw0MK4irJaSvDGcwJw97dV8W76IC3ZAHgZKjqDfp1WOXCiA-ytabvgtIQL12CHVh46Dc0QDQUnZ-3VXFKDHOg4GpO4zG3aMu3st7AM-s6em352P_zi6AAfQ8C3PmbOridJrKj2ovZVJFDHgYRsHiJATgPabiXGr2xsLJTX_8bVAw5-4Qj1UuyGYnGf-J9huYqGGaSCOXLOcfiV2Q6A5pM2mqI57xbYnkCnang496e_Fdaw-m6aaadvmlTOAQrVYCucyZ-pVKde2R8LkTBPB8uyhpfT19pJNRpHhAzzxnKYdJMXisC65suBHww8avGE7dH8cZi6skow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت نام در دانشکده خبرگزاری فارس
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
کاهش هزینه های تحصیل با کار و تولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
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
پذیرش پس از مصاحبه و استعدادسنجی
🔹
ظرفیت محدود است!
🔹
مرکز آموزش علمی کاربردی خبرگزاری فارس
🔹</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/458826" target="_blank">📅 14:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458824">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l41nlIrA7-PpMOwyyOAawzkh5Ip_5TV5IS79lMwkOoiOsxdhw7MrDluYYlKEFF3m1stL3eOlJCc0hAEUDYucA57XkIrsNSfpWbfn7DqwjRqIqGdcF018f3qdZsykd50voRF_z7GzsxVP4rOTb8B0aQzwGnr2WYzqsAjB8MLhdrOx1D6P_PCCEXH5s0_2pIY43XC-bCOG-MMd6SrfCAPl7iPqdqIlzGZetNbk4Jv87Mx7IBFWX4f7wGCoqHkU8o5oO2g2kRXIEpDBRGwMeYPJwTPfTmOut7yRWMjJW84pd2GG4gJ5lCTtepld-fCNJUFpW6uE8vbrKxYTTReaj60SCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJOAjDktCZgUPg0Fw9EJTX3dfYRW-79dMvilwS3n2nICps47kifdbV_EDUB7LxEBcMK2dNYw3IcexN7dB1Xu1fVbsYs5fl5jMfkVBwOqe7pa3hnXCXOoM0ORXvS95nxI3TsyHlW0w81o1L1emAPE1b35y3q0jlzsgy1ss8HT30-PeU2HzupxU5g304ZAgk_t7Me_9Zs9m49v434tfk1moT8OpX4xYyvYtIPLFZ96j8wxgmIfNJ7L6kdc9Upfv24ZTKoKSx-Rmg2IBvxMd1w4Rxz83oQlBT3YIQSo2NmXHEGPWXIEeCf3DS5zg9XEnkqBq-do5sMJguJlszXWPkmRsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تاوان جنگ با ایران برای ترامپ؛ دموکرات‌ها در مسیر فتح کنگره
🔹
در فاصله ۶۶ روز تا انتخابات میان‌دوره‌ای آمریکا، برآوردها از شانس بالای دموکرات‌ها برای پس گرفتن مجلس نمایندگان و رقابت نزدیک بر سر سنا حکایت دارد.
🔹
بر اساس برآورد زنده بازار پیش‌بینی Kalshi، دموکرات‌ها در حال حاضر ۸۵ درصد شانس دارند کنترل مجلس نمایندگان آمریکا را در انتخابات میان‌دوره‌ای امسال کنگره به دست بگیرند، در حالی که جمهوری‌خواهان تنها ۱۵ درصد شانس دارند.
🔹
این بازار در حالی که ۶۶ روز تا انتخابات میان‌دوره‌ای کنگره باقی مانده، ترکیب احتمالی مجلس نمایندگان را ۲۳۱ کرسی برای دموکرات‌ها در برابر ۱۹۸ کرسی برای جمهوری‌خواهان تخمین می‌زند. انتخابات مجلس نمایندگان شامل ۴۳۵ کرسی است و برای کسب اکثریت به ۲۱۸ کرسی نیاز است.
🔹
بازار پیش‌بینی Kalshi در خصوص انتخابات سنا، شانس جمهوری‌خواهان برای حفظ کنترل خود بر این مجلس را در انتخابات میان‌دوره‌ای ۲۰۲۶، ۵۳ درصد برآورد می‌کند، در حالی که دموکرات‌ها ۴۷ درصد شانس دارند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/458824" target="_blank">📅 14:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458823">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799a878717.mp4?token=k7b7tOwk4E81IAw_6GwNRxtjDtJz6Dz5Hm2rwNXvIXGjcZ6Mza2qTpRPm6RsM1-uw-_C3VXy_7SOD-DSE1WyT3dK8VvJ8YKlgHbut28gEyzkc87BaLyHGa0X6J7z-lat9kFya31Leg9xMpiMScoo6KiF8XTcUWQkLcMiZSOT6u13nwlraRmazUOXg7k_0FjGeFj8UPugEvAyph9m006Y-0XdsfrSGATlTPvMAUU1a18NiVMhM8Eby68CHlD9Ot3jixG_LWMbncuJ6T2R_oIRsY42bnGE7m1nkDSKtqya0U8OYgcIWpHWa_7dNGfznn6x_4iwzYm2LAK6Q4kyZC8NGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799a878717.mp4?token=k7b7tOwk4E81IAw_6GwNRxtjDtJz6Dz5Hm2rwNXvIXGjcZ6Mza2qTpRPm6RsM1-uw-_C3VXy_7SOD-DSE1WyT3dK8VvJ8YKlgHbut28gEyzkc87BaLyHGa0X6J7z-lat9kFya31Leg9xMpiMScoo6KiF8XTcUWQkLcMiZSOT6u13nwlraRmazUOXg7k_0FjGeFj8UPugEvAyph9m006Y-0XdsfrSGATlTPvMAUU1a18NiVMhM8Eby68CHlD9Ot3jixG_LWMbncuJ6T2R_oIRsY42bnGE7m1nkDSKtqya0U8OYgcIWpHWa_7dNGfznn6x_4iwzYm2LAK6Q4kyZC8NGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: برق صنایع نباید قطع شود
🔹
برای عبور موفق از فصل زمستان و مدیریت چالش‌های ناشی از ناترازی انرژی‌، ‌‌باید به گونه‌ای مدیریت کنیم که چرخه صنعت کشور بچرخد و در عین حال آب، برق و گاز مورد نیاز صنایع تأمین شود.
🔹
تأکید کرده‌ام که اگر لازم شد برق دولت را…</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/458823" target="_blank">📅 14:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458820">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E6TqO40oqG95SyBUSBSfJN-7DwlzJ0MiF_1tt2M0CTDeBXIR13-QUycgiRkIcNdVppFNSJQk602lIK8Y3ZipwL0Gczza2Mn-ZZyicXd9QTVfTNGUQ9sScXk-HyMuorxwWaK440B24NJQGeMWjdCqJ82EttQtoJoaHm5j1UQYY2Kcu9i52kxpYVn5LU7J39iqOVXC-HViaGH-6QFQkhKkoG0h0OjsiKv-vIoRmLy76tLmMzejGPxpDj8w4GgiLruGtfmoUT9eMjiQ5fYjXWtC_Mnbl5cf7izxwe2KzkdglfVmd1LEkaDax-MSCM_gEi1A7oE8scHYi3qZqmsq_VV43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYC9S7Ehgm6jFNh4FVXXZwMoAAaTJrCeK28i7NkBtwtsy2v63PbK36odc8V_DgiWl8rCuF4KPftwifISoaKzgeSmd1H-4ROubelpZnwUZj6jUQfo4Wzr2FKWF1cYZHxm2XERw2plPcdOUZhqAYMc3Du5qBsA9p1cHzBFCVVN6DbUa-XqoEdq18NNGZOAaY1Uxtmt3f7UVttbyB5q6FDFcK-46u3QZVRMwIVUbx37w0HXzavtr4Hgvpmn_u9o9ENDL3Apd8GD24gneLW5CKKsQNNYvtHwnk1dkgmx3L2sRIuJFnIeixK6Bo2o1jAh_w6a9uFZn2PwSg4xtYIuW2ALaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVM43j46Xjl9xNEoZQRVqCUuO2Q7Qjb6t0ZwiNRZOfmAbWRNV_KPY97s3_6WXNXcKJJqKl_EUctvrltpGRH_4Gopc02-XFLr0mvp58cRmWqeIuF05VuudlVKgeayZ6czZQieqqH2GKIex-_1TUBB2S5cb6oSQGqSoenZJrweUUqkTPkRh_355_UoreflmkJVuxfxVJqs6tBMrctfHTKI0toz969JrB19P2iN1dta_81V2mZNxKTMIDSD08CKO7t2QItKrbpbYJ5NrfBsgV9oFCg5zWclcJNfepn7hOrc_q6_TyeBibMsy7onkT_6Tm3rTlvMNyOHaOe6u0FzCznBEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پل B16 البرز به بهره‌برداری رسید
🔸
این پل بخشی‌از شاهراه حیاتی ارتباطی میان پایتخت و پهنهٔ گسترده‌ای از استان‌های غربی و شمالی کشور است.
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/458820" target="_blank">📅 14:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458819">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhwDi5XxgEE708AHtm45gtAHX6D9zl4H8gMF8vzGo_L6n4BGifcBYsar5g7BlTuxT0jrnQqZNCbrpS4Oy8c3p701Qg1IvzpB28vi4vcPcWJdW-n1SDxIt9iEgsrTWg5GPow45_mzK_jMGkhS-X-V4Kumtyrl0uxXd0FQJIj7kEcHJ_pKJhTjz6SMQZVpd-V-yzaZ9ch2yTjwMVfHdEd_PzDg5PMnvXGwZn3RwstYVA9Eyd5Zjc8z1J5czPLY4FiFuPBqfYEpxcNH8iwHgB9qTOhBy6Z9bO3R2cpWIJK47Gbcn5jZXsLdNmnxMtV-yYmIk6MlVaHX29uYAmdlCU4YRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فصبا»؛ از انبار تا ۲۰ همت درآمد / استراتژی کلیدی صبا فولاد
مدیریت هوشمندانه موجودی انبار و بهره‌گیری از فرصت‌های رشد نرخ فروش بریکت آهن اسفنجی (رسیده به ۳۶.۷ میلیون تومان)، «صبا فولاد خلیج فارس» را در مسیر دستیابی به درآمد ۲۰ همتی در نیمه دوم سال قرار داده است. این استراتژی، سودآوری ۷۳ تومانی به ازای هر سهم را با P/E فوروارد ۳ تضمین می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/458819" target="_blank">📅 14:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458818">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXZy6izOMlSbQKUZ8fb0GOTsGbSjrFlEAK3hVL7CJQl-tMnSoHNvxD4qVCe3ISPSGDiXQQjONtFFzddTBnB8zqE2Jtsn2PWoFWW0BVktpSGRU4c21q6aaQoGH1Tj7BaN378_-7YjBAfQoY45uqc65xKPqmyVMHSGBCFzVuxoDzaLoqB3J9SVljDaxPJIVOKKYpCiSlBb8v07c8SaamjqsUj1GVj_lYMH2CNDgzeTSygbfnozB4DnVE7F5naj3EmItmBp7ZVyuufXNk6So0O7nbz7J10nUIujpjxQZ8001_ZeLiBDWqn4Ps0ey21hz_XThpPkibnKhMzuRAScXrWtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❇️
سالن مبله برای ختم
❇️
❇️
همایش های آموزشی
❇️
🔹
۷۰۰ صندلی
🔸
پارکینگ وسیع
🔹
تهیه بسته پذیرایی
🔸
هماهنگی واعظ و مداح
🔹
گل مصنوعی به نفع خیریه
🔸
سرو ناهار و شام در سالن
🔹
فیلمبرداری مراسم و صوت با کیفیت
🔸
دسترسی آسان به بزرگراه
شهید همت، شهید حکیم، شهید فهمیده(کرج)
📲
۰۹۱۰۲۲۷۷۱۹۹
☎️
۰۲۱۴۴۰۰۴۰۴۰
📣
امکان رزرو شبستان مسجد
📌
آدرس مسجد
🔻
فلکه دوم صادقیه،بزرگراه شهید اشرفی اصفهانی ره ، جنب بوستان صبا
🎥
فیلم سالن اجتماعات
🔸
مسجدجامع‌امام‌سجاد(علیه السلام)</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/458818" target="_blank">📅 14:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458817">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/458817" target="_blank">📅 14:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458816">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
مهمانی بزرگ امت احمد در سنندج برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/458816" target="_blank">📅 14:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458815">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1e6c44c2.mp4?token=M3NY985A2fZcaDwjN7rbt4cvEv9tsZtjB4mom8tUOb57a2wfYalaT9A31YAVgHl1vvyc_3UjHGsKKjM0ZAnkvR1WyLaCggbefWYMymYIactyjBkupF33LlpDYg7jolJXnD10A-V0rG-40NP5ZMCN1-GVQMt-8l--gajXOw9E_qdnuxovPFO_EWqrDu5NXnWcLQB2Ty2WoFH5oH1ty7SwoYLL32kLDiVEwgfmAI1YhXlD6fs-8yrYm5FBmXBrerBeZWgaGdTqUP1KgvifQ2orC4vNNETSW_qGabUvFLW0WtFsXQFJtZUAay7Ri6YSeJqBsY2W97-EnUjnDkKnzaWkQoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1e6c44c2.mp4?token=M3NY985A2fZcaDwjN7rbt4cvEv9tsZtjB4mom8tUOb57a2wfYalaT9A31YAVgHl1vvyc_3UjHGsKKjM0ZAnkvR1WyLaCggbefWYMymYIactyjBkupF33LlpDYg7jolJXnD10A-V0rG-40NP5ZMCN1-GVQMt-8l--gajXOw9E_qdnuxovPFO_EWqrDu5NXnWcLQB2Ty2WoFH5oH1ty7SwoYLL32kLDiVEwgfmAI1YhXlD6fs-8yrYm5FBmXBrerBeZWgaGdTqUP1KgvifQ2orC4vNNETSW_qGabUvFLW0WtFsXQFJtZUAay7Ri6YSeJqBsY2W97-EnUjnDkKnzaWkQoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درگیری محیط‌بانان با شکارچیان مسلح در تنگ‌صیاد چهارمحال‌وبختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/458815" target="_blank">📅 13:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458814">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNIbW5vzENTezJnQ-I8vro1zdaCgkpNggHbP3tQlp9b3OUelwNZnrW55A1W9TkLIEWQqcUFeEj2z53D0k-8I9S_mqsVMG6e1kQ0_XDKtFRkKBEkF59d7-IgkdMIeyi8QzNfZEEJbQrvK68X3Y2Hi9ijg_dSJ2BuydcKydU9VzgDcw8eNMCl-5Pm4kFJQj49Ei1khXlSEKzf8uKL8y3uGLt7tYPUOdYnb7_tW1_h_wpkiKc4RtiJMkHVF27VjevtYBv_ssn5o00bjcqu0wcc-T1fGcwZ2_05Vdvb6sP7MG4KaLWdVOUu8cNMYcFtBqAKDObjKTyKNK5bE4VTBCvamlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: برق صنایع نباید قطع شود
🔹
برای عبور موفق از فصل زمستان و مدیریت چالش‌های ناشی از ناترازی انرژی‌، ‌‌باید به گونه‌ای مدیریت کنیم که چرخه صنعت کشور بچرخد و در عین حال آب، برق و گاز مورد نیاز صنایع تأمین شود.
🔹
تأکید کرده‌ام که اگر لازم شد برق دولت را قطع کنید، اما برق صنایع نباید قطع شود. باید با قدرت مسیر مدیریت مصرف را دنبال کنیم و مدیریت مصرف انرژی را از خود دولت و دستگاه‌های دولتی آغاز کنیم.
🔹
یکی از برنامه‌های دولت برای کاهش ناترازی انرژی در فصل زمستان را ادغام فعالیت، دورکاری و ساماندهی برخی ساختمان‌ها و ادارات دولتی و انتقال ظرفیت انرژی آزادشده به بخش تولید و صنعت تا زمان عبور از پیک مصرف انرژی است.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/458814" target="_blank">📅 13:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458813">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlOWO9ExG39_0T7gfmF1elTzHGk3tFy-5_6CtjKY1wI9PhrNncDBNTUHq-2i4uOtxcSXiEveilC4QdR8w5icTEunKOFAWCKDGEqh5JpzLdentft6Y_InzEeohYyrIqCh7rtXx85hjYJO_o2tXnOHcShw97ZB0vMEThFAbMlErUlq-NnTMGJJMo_dRLeDOJxZ2SRSICBxOmtWsZ9lG4Gyh4xluQZkMYIhDL-cM45eKD3_UA4vDM28_j2wYCjYOhYLBnYK4_0REWZsR-zSKcRaxAi5kd_EyH8w6hvINLH9VajQ1NrgdqKICLzKARCnrnKQ1DJnepPi7sOKAsY3KoLfzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا مسیر عمانی تنگهٔ هرمز را لایروبی کرد؟
🔹
ادعای لایروبی مخفیانهٔ یک کریدور جدید در سمت عمانی تنگهٔ هرمز برای عبور نفتکش‌های بزرگ توسط یک حساب کاربری در ایکس، با تصاویر ماهواره‌ای و شواهد فنی هم‌خوانی ندارد.
🔹
بررسی تصاویر نشان می‌دهد مسیر مورد ادعا پیش‌از جنگ نیز محل عبور کشتی‌ها بوده و تصویر استنادشده نیز مربوط به ۱۱ ژوئیه است؛ بنابراین نمی‌توان آن را نشانهٔ ایجاد یک مسیر جدید دانست.
🔹
از نظر فنی نیز لایروبی چنین آبراهی در جنوب هرمز به‌دلیل ساختار پیچیدهٔ زمین‌شناسی و عمق زیاد، عملیاتی پیچیده و پرهزینه خواهد بود.
🔹
نفتکش مشاهده‌شده در تصاویر نیز الزاماً VLCC نیست و ابعاد آن بیشتر با نفتکش‌های کلاس LR1 مطابقت دارد؛ بنابراین عبور آن به‌تنهایی اثبات‌کنندهٔ ایجاد یک کریدور جدید نیست.
🔹
از سوی دیگر، اگر این مسیر قرار بود برای انتقال میلیون‌ها بشکه نفت به‌طور گسترده استفاده شود، باید ترافیک مستمر نفتکش‌ها در تصاویر ماهواره‌ای دیده می‌شد؛ درحالی‌که چنین الگویی تاکنون مشاهده نشده است.
🔹
برآیند شواهد این است که احتمالاً یک مسیر دریایی قدیمی در جنوب هرمز با استفاده از داده‌های دقیق ناوبری و هدایت حرفه‌ای دوباره مورد استفاده قرار گرفته، نه اینکه کریدور جدیدی مخفیانه لایروبی شده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/458813" target="_blank">📅 13:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458812">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2718d57d55.mp4?token=N5EHzXzdvgmu7bQCV0LB7nrfEGAW8NrGNBjoLG5z0YMeC3eFmCOdKH15hACv0FXJdh4y59WuqjrX6hpHlLliYPtseap4D-kYDtrrta01kWjon6PbRbzsoEuqTfwhixpQJ7vRLtdb1Nm1oWG0ta0oGqSHcwkoZK0dDrs1XFeFv8YMCpOHN-qh7wJktGSxcwBYHpeEYyaNrCOxGCnFYycwlO3-OiJmP_SdEBydZzpXWf4BZThsfpbIKaZ1QUozTq4UIOluzfCd41W4mPXlSysfnm9o3rAsNioXSgJiEWhlfvSw9ZPuUDiHZ_-P51YzWvmjarSoPmrvw3ydY6gQZHuqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2718d57d55.mp4?token=N5EHzXzdvgmu7bQCV0LB7nrfEGAW8NrGNBjoLG5z0YMeC3eFmCOdKH15hACv0FXJdh4y59WuqjrX6hpHlLliYPtseap4D-kYDtrrta01kWjon6PbRbzsoEuqTfwhixpQJ7vRLtdb1Nm1oWG0ta0oGqSHcwkoZK0dDrs1XFeFv8YMCpOHN-qh7wJktGSxcwBYHpeEYyaNrCOxGCnFYycwlO3-OiJmP_SdEBydZzpXWf4BZThsfpbIKaZ1QUozTq4UIOluzfCd41W4mPXlSysfnm9o3rAsNioXSgJiEWhlfvSw9ZPuUDiHZ_-P51YzWvmjarSoPmrvw3ydY6gQZHuqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهای گران توهمات ترامپ؛ از ۱۰۰ میلیارد دلار ضرر تا بحران معیشتی در آمریکا
نماینده کنگره آمریکا: شش ماه پس از ماجراجویی ترامپ در ایران: ۱۰۰ میلیارد دلار دود شد، هزینه‌های زندگی سر به فلک کشیده است!
مردم آمریکا توان پرداخت هزینه‌های اقلام اولیه خوراکی، کرایه مسکن و درمان خود را ندارند.
@Fars_plus</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/458812" target="_blank">📅 13:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458811">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWJV2Qh_YVlYhQA_SfsD8t7_toHGY6uPgeaV6WCG1CC_YObZZr_YzNW7RgEx0m9F0SzgcAVUz2v9nBv1q9BGuhh7UMAgSJIrEbh3mfQP5tq0lATnj1UtXRmCVaWHgRJSrkFKj5UQsdGI43fInhuT9uSJ713Dtiml04EvPa4b_wJJyTghWZAPXjECTRSGbvP7jnoe7cbTSOZDS9EekUl67drYKVX1usBZaX0AJ7xHa9dceJsSbvlclk0-YAOw62uTkDBRLwpDcgTiHTXjAyuB-i-OZPJLsQ8odJitY85_Epu9E_mRADDB16qmDStZs6GXvzb1vAcHXH0JwWuPnZKfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار کرمی: ملت ایران از هیچ قدرتی واهمه ندارد
🔹
فرمانده نیروی زمینی سپاه:  امروز همه آزادی‌خواهان دنیا، حتی مسیحی‌ها، به ملت ایران افتخار می‌کنند.
🔹
ملتی که مقابل ظلم و این همه جنایت ایستاده است و از هیچ قدرتی هم واهمه ندارد.
🔹
آمریکا در جنگ ۱۲ روزه درخواست آتش‌بس کرد و پای میز مذاکره آمدند، اما زیر میز مذاکره زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/458811" target="_blank">📅 13:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458810">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5HGaGJuOqSIKUQMbASS-BEjzyXrSzMUXzvmHCIisZPLBXq-0Kl7Ljczd_mLsGafoBsE8J0hzIcXnXaVEqZL7nmT0kJOy93nmPR90Q1jEA4wLqSgpcyv6o3u1BixvVqISA5afXPwFfxnrXbXvQ46GY_jjAYSKp3tgeuHAP5cDppvMzTuuT3zS6-faPO5yggRm00_HCrdb2gLoOpEr_vveeDPvsGhTJnnPII2f_gkFGRrf4aNRBL15u0zdVan-2UpEhzawGutwMj5t2B0NHcPamPseOMps-ZFyOQqzjicDHmWs62iJFr1nmEqfgX7GKEPjXLMx9Q9cVuMzYrQnnTWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا علی کریمی علیه رضا پهلوی و سلطنت‌طلبان شمشیر کشید؟
🔹
ماجرای درگیری علی کریمی و رضا پهلوی در شرایطی علنی شده که بخشی از حامیان جریان سلطنت‌طلب، پس از ماه‌ها امید بستن به تغییر شرایط سیاسی ایران، اکنون با واقعیتی متفاوت از آنچه در فضای مجازی برای خود ساخته…</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/458810" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458809">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33990e412b.mp4?token=Kf7G0nGF-G_3H4L_2ndfpqHHGbB5zzE3WCjunImi-Xq6DCOYEhbRuh1XRfeXzS4Ffz8n4SxflP9J3wMPyMJ-eltUO3zlxRe-UI-YFca8uIZ-t9BmZe3AG-8qfTqT8YRoOq4Ry4451QaGEPvugCDqAyAsi8EcmKbmD7SKoDAgOoHOCFx_RWOEo3R_Viz573IROqQjnfi5MmVlzoYFnLqsY9TH9k6ji3-w3niELnYZACU3rX2e5iezKZ9Mu5V2Y_I-DsG52mTNHP7b0sXZ0KQuloo-d0hqZmW-ZbI8aJ8r0MT9kHtyRE6M2uf_WtZgtxMBttjzsHvDsQYA4Rto8eNw3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33990e412b.mp4?token=Kf7G0nGF-G_3H4L_2ndfpqHHGbB5zzE3WCjunImi-Xq6DCOYEhbRuh1XRfeXzS4Ffz8n4SxflP9J3wMPyMJ-eltUO3zlxRe-UI-YFca8uIZ-t9BmZe3AG-8qfTqT8YRoOq4Ry4451QaGEPvugCDqAyAsi8EcmKbmD7SKoDAgOoHOCFx_RWOEo3R_Viz573IROqQjnfi5MmVlzoYFnLqsY9TH9k6ji3-w3niELnYZACU3rX2e5iezKZ9Mu5V2Y_I-DsG52mTNHP7b0sXZ0KQuloo-d0hqZmW-ZbI8aJ8r0MT9kHtyRE6M2uf_WtZgtxMBttjzsHvDsQYA4Rto8eNw3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گاردین: جنگ فاجعه‌بار و ویرانگر ترامپ در ایران، نیروی دریایی آمریکا را ورشکسته کرده!
🔹
بن میسیلاس، مجری شبکهٔ آمریکایی «میداس تاچ»: این جنگ اکنون نیروی دریایی آمریکا را مجبور کرده برای تأمین هزینه‌های عملیات‌های رزمی، مستقیماً از حقوق خود ملوانان و منابع مالی دیگر برداشت کند. گاردین این گزارش را با استناد به اسناد داخلی جدید پنتاگون منتشر کرده است.
🔹
یکی از افسران سابق ارتش آمریکا که اکنون برای یک شرکت پیمانکار نیروی دریایی کار می‌کند، به گاردین گفته که «کارشان تمام است. تمام تسلیحاتشان را شلیک کرده‌اند. همهٔ کشتی‌هایشان را فرسوده و مستهلک کرده‌اند. پولشان هم تمام شده است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/458809" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458808">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌ بیانیۀ هیئت دولت در پاسداشت رهنمودهای حکیمانۀ رهبر معظم انقلاب
🔹
پیام امیدبخش و سرشار از لطف و هدایت‌های حکیمانۀ حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای (مدظله‌العالی) رهبر معظم انقلاب اسلامی به‌مناسبت هفتۀ دولت و هم‌زمانی مبارک آن با ایام ولادت با سعادت پیامبر…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/458808" target="_blank">📅 12:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458807">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
سخنگوی فراجا: دیشب با دستگیری ۲ نفر دیگر از عوامل دخیل در پرونده حمیدرضا رجب‌زاده، قاتل و کلیه مباشرین دستگیر شده‌اند و در اختیار مرجع قضایی قرار گرفته‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/458807" target="_blank">📅 12:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458806">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU2KVjhRx9fWISCBN0HGNAGvqAZqpoAquQhcqyzbFcOL2cdO73bvaia82HpbK3QrvUjSmPjOgKDSSI3bHtco5MJOWBW8ZvL_cXQjfyrsnwbkxSZmhbAkha3hPexQLcVEYOtLgNzdHFIfGAAqASEr4O0JQe4VdArBIKNUdoUjC1ytO1P1DcoHq5NuE6AlrsQ_Iknj5QmEoQoJhBHiVm9diQWwx4MCtQ7cqSJBgAN8_K-NvbFlTjnyKFyf_INpo6lEaGIevv4cN45to6Xxunx--pl7q5uR5NZY7dkYjO1rQux8a5amUjvYXUkN-vSNFG5SjYBCsAHbiUtB3bQ3vdvLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس هفته را ۶ و نیم میلیونی شروع کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۰ هزار واحدی به ۶ میلیون و ۵۱۶ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/458806" target="_blank">📅 12:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458805">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7343df84a7.mp4?token=hysPhR2RKcQEinwnUuUlxJ5Xv2JN4_rTRXlUdytkJLn4ePpntK4Im6bkGo9a4uYnihO9ItmQ7cYeOSZbeINu-FpQtUF--_vM5wrz9KmXCeMC54DJLp-N_zrPn_ni3bBQ1bNwxdbafu8L8Gos6S0pECnW4SSZiXkoA9qYOcR458F7Kns2Ik5HAEhwoKXfhSnPB1-dCyCF__1_dhva7-Qed-BKgvNYWb5kNZECfQbJfvt8l8engY5GYFh628FH0Q6HBHmrCG-OrmNHSQWSGcYj48HRUTVpRu1JQpWLDAb8BHXheP7lOLG10VBRb7dQG4ujtKnjGrQQKZS1Wx1l_-XOxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7343df84a7.mp4?token=hysPhR2RKcQEinwnUuUlxJ5Xv2JN4_rTRXlUdytkJLn4ePpntK4Im6bkGo9a4uYnihO9ItmQ7cYeOSZbeINu-FpQtUF--_vM5wrz9KmXCeMC54DJLp-N_zrPn_ni3bBQ1bNwxdbafu8L8Gos6S0pECnW4SSZiXkoA9qYOcR458F7Kns2Ik5HAEhwoKXfhSnPB1-dCyCF__1_dhva7-Qed-BKgvNYWb5kNZECfQbJfvt8l8engY5GYFh628FH0Q6HBHmrCG-OrmNHSQWSGcYj48HRUTVpRu1JQpWLDAb8BHXheP7lOLG10VBRb7dQG4ujtKnjGrQQKZS1Wx1l_-XOxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه از موشک قاره‌پیمای جدید رونمایی کرد
🔹
روسیه با آزمایش موفق یک موشک بالستیک قاره‌پیما، قدرت موشکی خود را به‌رخ کی‌یف و هم‌پیمانان غربی آن کشید. وزارت دفاع روسیه اعلام کرد کلاهک آزمایشی از پایگاه فضایی پلستسک در شمال روسیه پرتاب شد و پس‌از طی مسیری به میدان آموزشی کورا در شبه‌جزیره کامچاتکا در خاور دور رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/458805" target="_blank">📅 12:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBgGB1DfpvK75ffuCwEfyQsTDin4QSJvP-lsCl4xYN9NxqsE7y511kzxby3TBBZVH0zCti2EmYfF1AwEIpSZXeJqcUL6FI8ZOUxUrQC-bA9820lOwp8CptEQc7wyGGmKt_4BcOgCGm85m9JskfRGH3DFbF3mfUP-NTve7I7ZUSD0CgBfKOyZ3YvfFg7yhTeiYfh0d9KuBljP8-eJs0BHDFV0jtUqJcUz2toQG1OBlWuyr1ljrjJKoD0oxrsEDJDOJLSozWqCmQb7WZRZbk7BneVVG6mqY-pz-YDL33iviPlBqzKx34V_cbDs7zezZsW_BIidZSpqnYwnASAlobe_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0Hw56lA0K9vh_QvEGmtCQ71-Y8TnAEZV3qv714y7pv3Su6zBaQozYXsr5T6F-ABepeo5nfGTNWKM671cMNe1-ID-c3BV_LqAJLZ87N6dmL888IHjrl_0GBwxCqOCFn8s6AVeYiR7ZmciQqUDBgac1lTBPsT95mC-jq3zXVzNNRuJeup2EyX04HLOghbTkXoMSW3mPca9optRsvMqOMOpOZD_aAQwM_GyeBpiYGqN72X4JbmI7_WWs0n24o0FLfnFZxVdmhuzY9De5KYBWojm8u-eDXftrhrclK17qmmj8S7VTTi625wQ8I_TZTWn3vX4w38BTxzwSkvW_tM_bncjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJ-96M1KIuZKI6ikXvvUHppelhBpHz6yUhiTGbqXsK7h0KFHKIRYDOuedBWb2w0lvVv3HeJqJA52jK250PSMWFBYXzvyqtiLgiBLf_qxRjTSmRPwzKZG66DL9-PO2pmD1qebNeepjYhbRmN6spU_5gN_SgKXl1400qFRTh9GufekAzzkjVJG65c3iYEsb_Ax9Nwl11t2LCF5U-ojpHmKAwKkEMvkffWl0-WCLzHksBRiMK7JBmor8FICjHNlOI3ZVMFpGuuge-XB9M4UUi_QGPVWMEujpdM-0AYOl1UCv-BR3EZLp0l28fUwzcWNo799J_IwJXTUIjzD9QVsHAnHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMqcY_a0U8aIMlOsN9R8o7dRDalq5WvhID-WuxSj15GTXyxxT5O8Vzphp1AEI3X2T9ukHdEwds4NHqFXKw-MszwkFfwlQEOR4Viyz8LZayhqeF6qyLXFLfGF0v72YUtwEKrbfjtucPWDK8rHJHRo9cdhQuo6O6lH8lBP4ZjeP4O4xRiaY_ZeMUYRXSrfjJzSXhVakFgErgqX6ZKJJuUzY-CfuX4XfU_KkN-DgT4t7TUGk008GTlY_G76P2iRiJLCNZ2zm5E_7E1PqvAXxLGHP5RaKsp21sCAutX_uL0mRLyXBKpa8dFowRLs347UvFVve65ciEQUGmV8dyx3Nru8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjy5lKDN-xJ7RTag9situeSw2Z6h2wVoNZzRjJU_JFZ0n-DtSvaqm8cuoLXTYvH1cbhBLFXwVogGcDvQTREqMnbUprpDGjOTKcPmtOTGe0jc7DAQ8nph9dYtPI1dZpyq2_FW1OIGL9BJKmC_fw6N2g11tLzqWEVd94vaPb9mNL7rn_LRhTS6oqgKEupSGPGyKngBLBIgSUUWrktyodpHuzf2kpv03H3KuGGhvdv2ZjEYlc2-4NISOwTNHig2_fvZPmp3dSWY5Dr-TRwSS8wZvvbEbVjYC-nguvV9SpT_bo55MOcZ4Gg_xSmGVh6IOFfod949j70Hcr5kNseYFnak7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcHBB13mM8t_WeQMuCsvO2XaWi8owP65WbVuc-iRbgkmHBlV-igfisGFadrmA_f09uqCdNwg_e5WSFvBpJo5cIBieZfnZ3v4I7Gc899mqGZwTQmztHP0PsojrWpWr6EoHFSY5GSJWe046Oaw3gLtM5rClzRNBqs65hCp4kEZC4caHBsqSf3S2kUXS4STa9SM9LxLLZmt04FAxDlf6_XypNT5PNExBbDUbIRrNkR14857v7Uzw6rY9ySYSfJ__HMbOX_MDJtZZwZKtrwfuZzyj3dlLddrLD0Rkd_Nf_VPraZQbhtlizxvFJmR7RAaf3FtmTHehRVK2Pnt8PjqwF6P0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTbaYnghgXUgQit_7nv5Lko4LJi3k_eJRGB5JsNIebiXYa51kosYn5NYLDtKKB-BCyimgMNf3O_RBdbs6rreoCJom9ODsoPU4nYz1dqVi7HdjAyCuCxnRKOFh4MyaisJMm7Iy12wMUsV_UvK7QYZKSACawMxT5nkmk3pikpAtmL7BcUVzrAdmunfORNdeqR5BFRh5AjrzygUPKsbfz5BGyJAKpUNynNNcm9HWndSCgnoHbHdzPcbFxdobZkPAee6-xiuNbVuEUVLP4gEaj54VIwWBUuCBxt03pvu6ByheoB0WFf9IeQxkPQ0B4q0lSt_xx-5YzMsHJ4nJWLHeXHjrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آن‌سوی زیبای دریاچهٔ ارومیه
عکس:
حمید اکبری
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/458798" target="_blank">📅 12:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458797">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c157c514b.mp4?token=BdyxViJF4u2cU0HhxErbTFoWLeXu_s1fEJfOfVWznjWSGspBUaJFNNn1xJd-2Ta93tbvN3ayL6zlEIiYD1FiphWLs-3jZXDUxbB7H-VaWeZ8rNowZ73HmdXDbDlvef5uN-AJr9VTcdK5yAVVY5gutgevA3vFu_opMRBEEwxMANLSavT_4nr3Q5jNUPhZ-IkkYK8Zoq2kTihdd1AOpPVP4i77iVOXdEnyMkII_-QDfAIcuUmmkeBxSm2XQD1KuG05CajrG39TAbY5a79ivyGa_wYyYPKXihE-qsi0_peX74yyc-ERcKMm8esw7t7EHCuuzzffiHPhkth9WCOH7DTqWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c157c514b.mp4?token=BdyxViJF4u2cU0HhxErbTFoWLeXu_s1fEJfOfVWznjWSGspBUaJFNNn1xJd-2Ta93tbvN3ayL6zlEIiYD1FiphWLs-3jZXDUxbB7H-VaWeZ8rNowZ73HmdXDbDlvef5uN-AJr9VTcdK5yAVVY5gutgevA3vFu_opMRBEEwxMANLSavT_4nr3Q5jNUPhZ-IkkYK8Zoq2kTihdd1AOpPVP4i77iVOXdEnyMkII_-QDfAIcuUmmkeBxSm2XQD1KuG05CajrG39TAbY5a79ivyGa_wYyYPKXihE-qsi0_peX74yyc-ERcKMm8esw7t7EHCuuzzffiHPhkth9WCOH7DTqWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امیرالمومنین(ع) مهیای سالروز ولادت پیامبر اکرم(ص) شد
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/458797" target="_blank">📅 11:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458796">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فرمانداری کنارک: احتمال شنیدن صدای انفجارهای ناشی از انهدام مهمات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/458796" target="_blank">📅 11:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458795">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHGwTDuoFzGiZCfLSYk7HDwH3alGdjrPkAJXEaxsa1rNRJyIvIc1Gpwt2PaXfhUBXmQ-_3PnbXQFoB7H-L_vLEcH0rjf5hsVFvIfkSe2v62YhzactQDYUddXQf91yRbgEMCH0W_RFugoxIc-x7wN9LW6_nTTDm7cz1185L2NKYwW-02NSrqc7QPjO_A8A6hkATO5TGpW0U8nAlAT75steChq11DLfMJgcvltGXOUDWMSzSQzlnyqAjNSRZ7KzuNs-z_gPvs-72BdYw1U4W8RWFzuR4UF9EMqCLaZdOfhbFKdsO-m1cfVJ0VEWY8tE5-EL06AvmmUwQPrjba2lIdU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر راه: بیش‌از ۳۰ هزار نفر از عصر امروز خانه‌دار می‌شوند  @Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/458795" target="_blank">📅 11:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458794">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAEMQLlNfplVTq16ntJqQGEVpsCZ8-yi_Y5oqgnVICTB0RV0vMqFAeHL1kbn1QnmcmYHfRjc72P1JJ0VNXzkoPJ_2BRbysnNHwZ8W5BK_50oRqVu9gFpGmyiADNxUwiuONUHzramsIsiM83Z6N8CXLYC4fCjlA3S0XWvvp40bumGqZBMa0ikADy6-wajsjocZkbt0tFvLH3Txx1zB9FeYiYB-8-tcVxUcawaHl2W4f7zlKSw-4aiJhMSuBud0QEUerBYWNFLKVm0DG0dFfMRor3Fy9dOkKGfU7UnISdLz1Z-9qU83y21U04jM7eVR99iLs0gyaBFIxT4f4h3vg0UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
زمان‌بندی انتخاب واحد تکمیلی نیم‌سال اول دانشگاه آزاد اعلام شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/458794" target="_blank">📅 11:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XnCbxCa_6gglLqpv5RlI4xOi-CSa307zQ7ch5IvAc1mUO3vHIm5s10qso8kf6ogXAd0wIbuaMeuaqd3Bt9kAfpCTgH7nG2hXXQQziMnFI--4trOATXFFm1lt7XR3aHRhEiUdbul5AbGi315yPrJIaDuBZrxeMaAdFSdaP5-OzKl0VKTapHkiyu8TM5mjg0SWfcj6dQjjAoawYtIgx8G8rukuGeyBSsR-IJUNwidD5BgI-JmK_8H8m_ztKqy1274Bb8Cf5sYg9QNSdzb1LOwMf4wLTbTrbGxfvmVnExev2P-p1h7SgPj37ur2RCnc-xKBKbao43qytLXoJ9We87sr8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7E3oZLz2q2J0GviDblLL_ALVtmq0JH1Mj0SWXB-6XEfzhpxy9a9HmIesbCjcBEBUw3_z0nCx_wTVFWPcARktyn5FS-iiW4zyCVFDLC0u3NS9HX1vNoaYQ0tWdG-aN0yOrGigax5aVY5uwEKDn5n4gc_dhLVPnIOmBCMQPjaJiw0hp7ZYSfled35YIIYxoph76D_vK3VSTLAC9NbCh2o_H8JMn7Ysie68RrQsWeIvgDCRs1bCIHwqO6cD8hi26vIfJg8OjR-ILZVCMQtgMUSCWZVsH5ZOAv6In9v3ebTL6Gps8A4QH0_AQXiLlb3QvlpEQ7Ek_kZspeWNc4ICMWHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhh6Xxf2MZL86QnSv9Z0JGM2LcF6K4NLypSp4mZYRsvLIqLVtKDD_Bv1DMEGI9lACWNDLHzjAWZz28Qo7BBl2R9t7N2X6nzNA4ac_tvCZZtORIDqYqPWxElLRZq1VkiFsFZTDoDfvirsudwcNiMGxtMxm5LHIwq9pMGt_b_b_JXStTTYM7j46_YonvNYtDBr3pcWMA8Yrg6Ne8mrmerIEDteA0bIJbItl7hbPc1gSEWHY9FrP-d23-Ti-7bXYO5ohYvdPCDq9oM_1LA21aFSjxCKJolRKK-HteQaA51VlYIaKaEQQXebzQhlp3LNAZgj89WRU4kLu7hj6LwgsCCXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3Aun2GVxCA-_1PXrkUf2RmjP6wbqJrBNjAxcjoL-XGk08vOPfXzSX7lsqeci_UPxOkatLZ7dVQJN-mqx7wfoUEuQJoSCDkteqIoGe77-zj1AXtrfHsWV3KPC2gz4mSvcgK0mj_ifigPOb5CZdjYbnwGrMzdzDIGXlIsxyyraYOTGR7yLV3h_akEcwwbjDkUf1g0NnO8R0YJGXF8LwSHxUZtS3KVj8toKbo-Rzr_u08FM15ewxuJQQhy2nZwkl0TWRhivg2vZnsyaGJn4GGm4Z8u2ZBvK92fHFmx3Vlo6m2flwfTfueFMn8eCjbQLpuqPQEwUvGLKgensKGl7dvyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOl99RIq5_dXYalUUeN7O90GF-4wYyI8ShMpqTzngjF0V4Z5On4pVq5wU7WI4HzuxcxSIGJEaYT3JnPCpUbijCiMRTVwlbt9YZAQqmf6dJx9HEBjbVb-iG5UomPyuOoSRufBRUdHYerk9g3mY_yW28nP2v9ad8j_NXHkImxhv8B4q0iude35avFC2rb6Yc-K1x5vmnmOAeMkvzgVo1RcdyCG-IWsG-weTGRZFm3cMCl-DMoriuXk15dQ9vkBsVRUUSZwYOk0K92aT89OuD1i5AhGT5mvLTTyHmbJ0-g0MVMQl0rLIpQ6zR9HobMysiUhgAOv2kg_eF5rlMwNatwxHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibTDIX3sNlWxznqnxHEG5S5Y6UrTnBHqw0q60jdCbINqyC1KTQzMwN-JM1meleH8K2vHTC7DI5AZ1vxyC-dqIOlJJzFA3sWhVvFRzdS6SefWMFzbkRT4PXRruEBHl7MK7jxJBFMHkNV-PopclhyiSzP2iCV3va37i2GX3hRmCIe3M6LjQiVvVIvBkZm1o9JICCdxHkC6l_usRa2Q4YH6UvTOk3N_D3j9dfvKH-b-iWElQcn5twea-rUoGEs1pj1GdAFaFZNNm_R8YNu0G5zzNNckU619rtZdn07yNmg8wzD8gqaRS927zDyBEX6Ijy8Y-FQ4qt2FVmhHopWC4L_XNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTk5ZB_zf1B0P1_gn_62PSElt2vKFORWawOfW6jLbmnqR6eKkJtJnViMwpwMQOMsdEKrewVJVIa41d8BT6CM1AtUlQAvNGJ6TUvl8u8XyeNz6rpiz8IvlIujZDasgdkjwty58WsEA1trS8bjWG1OyLxUT2zoOWSqEVM1EcKZJP5fd65Z14mRhXYGFGYJ7Gh6A7FP93rHm5AhuDZVp_bLCcagU6GCwpowulbqgUkgCnfLg1rLblXXXCQhmLG6HNiadXEZ0QkD8EwLtZgukKuwUv8Yc1hTFjl5sgkiinJH--ycF-JUjcLEWsu3liN7QS2J-R6Z_e_BlTQTlNO7QqBXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pNy88lmGml5Yrp201pQQeCmX32ScKJNI2cxX1-1dZWuwcfcZId2CkupBYM2gNdTcRNXrZVjat9wpY0ZaYoqHFYkfj0O93HdXZ0pc1Ah3o8Ay132ZbbP9qviJdWkbMLj_onE7aRUasmcrwUtrI_1eeiFwLFJCTTAHYSOD0IaEFTZ4tAcXEXVAuRUbxpvnlUGsSIbAO6U-igO3ECLQKY3Zyw48RF-9S5AlnhiFKeTFda6S4Ky85NheDGMv_ExogDfBLPh8ISUNuUAhTWJ428ArIsLfjBKd5VnAjevc3_QT1-nfV-GScUgHiYT8xSYqRIKbqz5FM4Mq17ZUxD8bZ0o1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqD21iWsymti8gkZC-JzY0fQhgrRQbbBvWB4YDVMN9skbyGFe3jmtjuiFdrqNLuAJ0GkOmlNGP1uL7xtfHo_AMVUt4EgTZ5QxczDG4tcWafRXGya4BwKnB_HFeHPjLo7SKaIWWHbDWn0FuNvoB2zBNd1JT-eCGEgxuSIt8KW44E9r6wvBppc2nJTiVRB6hNsfn5BQ9UwGv2JrPCcdlL6Db7nk5heyZ298VBsZXpM63qUeC2iJJsNQLIjAZvoqrPLptZQUo2ovRdUBBQqlFuymniNNqk0SfxexKuB1MElB6cKRsHWCVVEeNYwE0ExDs-HqSURNzA-HBhMHyNkWqZ-UA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc9f325fb.mp4?token=FuwqNxOWPTEf0sD_wJWc-_R2f51xP-fPSiynpBPQlMO0ZWp71Uap2a99VRZTo5goFn75ublDb1MLeOl13u7n2iq1bJJQBLMqze1pXFEEi4bY2Y6KcskR8y3ip15hKiDOwhT_YHcezeWnMAYrMVjNvpCFs9sdT5iGbS8QCLvOWHAwm8Ee19zJ89e0aPRX7099VLbQ0Eks-ZEsmZRlWKibSJNJwpUowBp-OOzyGWHBehGjw5u4SdrYIHS5H5vsDjrB8QcyHEanillVO91VLjts4cdW9nFdOCyE-e2i9_2oM1Qn-WOA92VzL4cROvdhEhPvuToTtmhFiFYntPqBiHTpAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc9f325fb.mp4?token=FuwqNxOWPTEf0sD_wJWc-_R2f51xP-fPSiynpBPQlMO0ZWp71Uap2a99VRZTo5goFn75ublDb1MLeOl13u7n2iq1bJJQBLMqze1pXFEEi4bY2Y6KcskR8y3ip15hKiDOwhT_YHcezeWnMAYrMVjNvpCFs9sdT5iGbS8QCLvOWHAwm8Ee19zJ89e0aPRX7099VLbQ0Eks-ZEsmZRlWKibSJNJwpUowBp-OOzyGWHBehGjw5u4SdrYIHS5H5vsDjrB8QcyHEanillVO91VLjts4cdW9nFdOCyE-e2i9_2oM1Qn-WOA92VzL4cROvdhEhPvuToTtmhFiFYntPqBiHTpAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
چرا سرآشپز برنامه مهمی است
روایتی از دلایل موفقیت برنامه محبوب شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/458784" target="_blank">📅 11:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRSToXCtv1brGOTng9BvjGxjNg8Rgtjid6QPfv6GzhvHrrUisEeTLdaW0kVaWnaLo4VBVJKIi6t1ipxmxW0Zb2bOKpnvzX7cd9h2F9jO7QDQ64rSvGO6ynf5eA0bmbURXq4reqHkdgC0oJIV3-zcNGku4srrRtDcND7x7G_OpBKwnnXWqUYDFU9XRcFDgY-SQjKnsFBgeR9h1kjcHQy7nET5cvCvfAM7lE8KavlEOcU-_DdjCWQ2WaFwuFF1DJW9TtSEuHZIJ0RpIFpaimhZ--tIwZKkSEflB1RszDYYylNV26NNwzbFfonNFdCihTPrLWqNFBVQkOxgy03dhnQwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تشکر ویژه وزیر امور اقتصادی و دارایی از بانک تجارت به عنوان تامین کننده اصلی بازسازی فازهای ۴ و ۵ پالایشگاه سوم پارس جنوبی
🙏
وزیر امور اقتصادی و دارایی در بازدید از فازهای آسیب دیده پالایشگاه سوم پارس جنوبی در عسلویه ضمن ابراز رضایت از فرایند و سرعت بازسازی از حمایت بانک تجارت به‌عنوان بازوی قدرتمند بازسازی پروژه‌های صنعتی در کشور تقدیر کرد.
💠
دکتر سید علی مدنی زاده در ادامه سفر یک روزه خود به استان بوشهر که همزمان با هفته دولت انجام شد از فارهای ۴ و ۵ پالایشگاه سوم پارس جنوبی که در جنگ رمضان دچار آسیب‌های جدی شده بودند بازدید کرد.
🔗
وزیر اقتصاد در جریان این بازدید گفت: از همه مجموعه های حامی بازسازی پارس جنوبی به ویژه بانک تجارت تشکر می‌کنم که به‌عنوان تامین کننده اصلی مالی بازسازی به‌خوبی به‌تعهدات خود عمل کرده است.
👈
بانک تجارت به‌عنوان حامی و تامین کننده اصلی بازسازی پروژه فازهای ۴ و ۵ از جمله فازهای میدان گازی پارس جنوبی است.
🌐
مشروح خبر
👉
✔️
" اقتصاد برای همه - سازندگی نوین با مشارکت مردم "
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
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/458783" target="_blank">📅 11:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/458782" target="_blank">📅 11:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A92b24sB_IJyb1fGSA2Myix2hWcrD4ezIb0CmyUAJqNAgf_tcOZO48eI48bcCPG0DWhD02c-VxN7AvG5GylYLZhCba_qo4phpMr94qpF5-MNPcnAIe6bvvt3k6KjA-s6-qXC-sNDUAXz3RLuU6vkI591CvlIz8edJNMbDEV7OCB7LJ8rx_970K1IxkThLYERuIlIYiZLF0vKmjX-L91cQMu-bnbyXI_HrCxKw6dqjLmFNgm2e2VL7wywMM72XB3wxFjmM7N3MweNLsPUtJvW-1l0_-fsN5bkT3C_nQcBD20ep7Xgz7pM4x9O7l-AEP-gkM1qNn04L5ejX29DPEloQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تارتار در پی ترکیب برنده برای دیدار با ملوان
⚽️
پرسپولیس امروز در شرایطی مقابل ملوان قرار می‌گیرد که پس از شکست مقابل تراکتور، کسب امتیاز در این مسابقه برایش اهمیت ویژه‌ای دارد.
⚽️
سرخپوشان در ۳ بازی گذشته با ۳ ترکیب نسبتا متفاوت وارد زمین شده‌اند و به نظر می‌رسد این روند در بازی با ملوان نیز می‌تواند ادامه داشته باشد.
⚽️
طبق اطلاع خبرنگار فارس سرمربی برای انتخاب ترکیب اصلی، عملکرد بازیکنان در تمرینات روزهای گذشته را به دقت زیر نظر دارد؛ یکی از فاکتورهای مهم، اطلاعات ثبت‌شده توسط GPS است.
⚽️
این سیستم میزان و نوع حرکات بازیکنان، مسافت طی‌شده و شدت فعالیت آنها در تمرینات را مشخص می‌کند و تارتار نیز برای ارزیابی شرایط بدنی بازیکنان و انتخاب ترکیب اصلی از این داده‌ها استفاده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/458781" target="_blank">📅 11:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3d466698.mp4?token=Vbl8QRxuHI2KM4EOkRtiQyOM6PFtfDRgzKKGCWww5iH_Mq1PPMD1yXmubLP1E1x6s-HxCPotZc63HWgLx5OaCDK9Gj7-6nB57XOqZG_xIpqUz_zjHIxClcRIQym6nCD0zeVzJEQfMcIUzAVu6j1b95XtdsGFbUTu_rfP3AM_Fd9fgo6fdrpB4d12WJGGh882Ii-s50td5b2_zTtsLJSZwuvYbBKcJxAZTa7UDMcLZcq3o0evjkvwK1Lf_5b_SMK5JGN6XHmeGE_7RHW8xG6d7wDoJBaAoP50W2i-E-AHo18mSdFPu2iI8XivayAWGh-9hg6DQdbG7J55tH5llQmxhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3d466698.mp4?token=Vbl8QRxuHI2KM4EOkRtiQyOM6PFtfDRgzKKGCWww5iH_Mq1PPMD1yXmubLP1E1x6s-HxCPotZc63HWgLx5OaCDK9Gj7-6nB57XOqZG_xIpqUz_zjHIxClcRIQym6nCD0zeVzJEQfMcIUzAVu6j1b95XtdsGFbUTu_rfP3AM_Fd9fgo6fdrpB4d12WJGGh882Ii-s50td5b2_zTtsLJSZwuvYbBKcJxAZTa7UDMcLZcq3o0evjkvwK1Lf_5b_SMK5JGN6XHmeGE_7RHW8xG6d7wDoJBaAoP50W2i-E-AHo18mSdFPu2iI8XivayAWGh-9hg6DQdbG7J55tH5llQmxhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
نیروی دریایی سپاه: تسلط رزمندگان اسلام بر تنگۀ هرمز کاملا قاطع است
🔹
اظهارات مقامات آمریکایی در مورد باز بودن تنگۀ هرمز دروغی آشکار و تنها به قصد کنترل قیمت نفت و سرپوش گذاشتن بر شکست‌های خود می‌باشد‌.
🔹
تسلط رزمندگان اسلام بر این آبراه راهبردی کاملا قاطع…</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/458780" target="_blank">📅 11:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhirDaB9JeQnqIJSmaV-SxH4dP_hrCV3ENHfPtIVjX94olnAAtwPHuU1LHVSlAPX8vTmxN_VXI_TBYrUHwgYFerx7sxXnmNfAIyscR4fM7-iKNF0j9DCGq5oe7uiiAP6ib7yRwuagu10jZJQdNwm4Kf5ctOkLuMI6AYpxR1tJ9gL88MzL-dDv_flmONXXgNn9wu-nqnShGPdjn04Q4t36JZ84AXJGQXipkHMBqkaXXT9JciOujOuHnAjmevcwuBxohvoOpONpl0XAXkvmJCM8YMoB3-6JlZFEAcZcDXUkUe9M6lEWOoeZnfmadNUmKvfbSQzTjYsuIXGNTGwlusdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید حوالهٔ ارز در مرکز مبادله اعلام شد
🔹
دلار: ۱۵۸،۴۸۰ تومان
🔹
یورو: ۱۸۳،۸۰۹ تومان
🔹
درهم: ۴۳،۱۵۳ تومان
🔹
یوآن: ۲۳،۵۵۷ تومان
🔹
روبل: ۱،۸۵۱ تومان
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/458779" target="_blank">📅 11:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d383b33183.mp4?token=gvusO54pzAUIga0bhoIgyb8baO2oP2Bt6KkLZoMuQ5aNzjHVlNxfYBo-xfurTc7pwIoaOrlxeIJlocnsNzLQ_2gUUnRzdsbWy4HJrFiOevm2k6Q3P6aVyfoPO7IbclAHdTToOwoqZSaSSLVy1pMNEr89B5y_N0re3cxFb9NgdU6_mC9kW6QzT5jHXWid-LJV25IOJ_kgSE-VaJbRJsW5W-wp285poOVcRaoT-TKy2Y6yaLWL5ZRMVMYxrI31KBZeWiAzgYvxZCyO5ntol19L7TU23BH_s1QRmAB7xEZmKWyQOjdyeo0QlriifbBK5csR5iBOzBZW9zwWiq8vcP9AxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d383b33183.mp4?token=gvusO54pzAUIga0bhoIgyb8baO2oP2Bt6KkLZoMuQ5aNzjHVlNxfYBo-xfurTc7pwIoaOrlxeIJlocnsNzLQ_2gUUnRzdsbWy4HJrFiOevm2k6Q3P6aVyfoPO7IbclAHdTToOwoqZSaSSLVy1pMNEr89B5y_N0re3cxFb9NgdU6_mC9kW6QzT5jHXWid-LJV25IOJ_kgSE-VaJbRJsW5W-wp285poOVcRaoT-TKy2Y6yaLWL5ZRMVMYxrI31KBZeWiAzgYvxZCyO5ntol19L7TU23BH_s1QRmAB7xEZmKWyQOjdyeo0QlriifbBK5csR5iBOzBZW9zwWiq8vcP9AxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فروپاشی روانی نظامی صهیونیست مقابل کنست
🔹
یک نظامی ذخیرهٔ اسرائیلی ۵۰ ساله به‌نام «آوی آرسنو» دیشب پس‌از ۳۰۰ کیلومتر پیاده‌روی از ایلات به قدس اشغالی رسید تا مقابل پارلمان این رژیم دست به تحصن بزند.
🔹
او که بیش از ۲ سال در غزه بوده، این اقدام را علیه بی‌توجهی به نظامیان مبتلا به اختلالات روانی انجام داده و گفته: نظامیان مبتلا به مشکلات روانی، به حال خود رها شده‌اند.
🔹
تصاویری از او درحالی‌که مقابل کنست گریه می‌کرد و توانایی ایستادن نداشت، منتشر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/458778" target="_blank">📅 11:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuCkZyN0Ea_J2yOK7pRRpLhIVgfgHRGLAidd4CD4ZYVJsUtHnYcdRMsrit0_7w4pQjwWl8t7qARpu5pj3SFC3DKJ_f-H2UH44wgNW0m-B0twsUiLjN_dOWGsdyNGGt_5MKSrpQGoweTgXHMFc6UaInqnkhye0_o_ewa1nCzc1a6geXWCVhFLAcWYqPwSnVwOV0TunPgFv0ldWyOqdk2Wl7oJawiNAYFuFPqCNMLN--GQJH2JM7rOHCo6iFvCGH4KvpMOlFjfmc8rbj_C4QKaTfpJ4edWwQDBWMOzCKkgo6Q9xtKJ4sxUnFL3X8G1cG5Z0ASRLvdvRJOPLlqkOR6K5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست «ایران قربانی تروریسم؛ روایت داغ‌های ماندگار» برگزار می‌شود
🔹
همزمان با روز ملی مبارزه با تروریسم، نشست «ایران قربانی تروریسم؛ روایت داغ‌های ماندگار» با حضور جمعی از خانواده‌های معظم شهدای ترور، فعالین حقوق بشر و برخی مستندسازان و نویسندگان آثار مکتوب در حوزه تروریسم، به همت بنیاد هابیلیان برگزار می‌شود.
🔹
این نشست با هدف بازخوانی جنایت‌های تروریستی علیه ملت ایران، تبیین ابعاد و آثار تروریسم و روایتگری خانواده‌های شهدای ترور از داغ‌های ماندگار آنان برگزار خواهد شد.
🔹
این مراسم روز دوشنبه ۹ شهریورماه از ساعت ۹ تا ۱۱ در تهران، برگزار خواهد شد و در حاشیه این مراسم نیز آیین افتتاح دفتر بنیاد هابیلیان در تهران برگزار می‌شود.
🔹
حضور خانواده‌های شهدای ترور در این نشست، فرصتی برای شنیدن روایت‌های دست‌اول از قربانیان تروریسم و یادآوری این حقیقت است که آثار تروریسم، تنها به لحظه وقوع یک جنایت محدود نمی‌شود و سال‌ها در زندگی خانواده‌های قربانیان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/458777" target="_blank">📅 11:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f77bf3f03.mp4?token=i4aijSECyrBrFANv24l0VRfK8rNkDwH7dMHSXLnIBgIj8CoipnFomqakAyMnp7UgLTkyhsv4P3dMF3Fewy_rgQwoN9oIUXmSfV2RN2y-9xecZfXG_F74QDvto_wNBeccfkRzXe_8u-xLTNRCvwJ17mdPe0hvVIOM7k-cwTOBhEehZc1swKSnCBfxWFkDi1kalhuamErvW4-KuWyxgQeLs4vDaQGMniXcZf46Gmp7hE4rarbKh2nSW4qtQB7dk-UrXuwKNm0Ilmb2zO0wOURQsDNKtPFggYfEAYBEIBGf16HT80pdp_t8aFXRM6lmyUJCn1tYRSF6GZfV9ph8E8WDwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f77bf3f03.mp4?token=i4aijSECyrBrFANv24l0VRfK8rNkDwH7dMHSXLnIBgIj8CoipnFomqakAyMnp7UgLTkyhsv4P3dMF3Fewy_rgQwoN9oIUXmSfV2RN2y-9xecZfXG_F74QDvto_wNBeccfkRzXe_8u-xLTNRCvwJ17mdPe0hvVIOM7k-cwTOBhEehZc1swKSnCBfxWFkDi1kalhuamErvW4-KuWyxgQeLs4vDaQGMniXcZf46Gmp7hE4rarbKh2nSW4qtQB7dk-UrXuwKNm0Ilmb2zO0wOURQsDNKtPFggYfEAYBEIBGf16HT80pdp_t8aFXRM6lmyUJCn1tYRSF6GZfV9ph8E8WDwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیمه‌ٔ عمری که هیچ پولی بابت آن پرداخت نمی‌کنید
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/458776" target="_blank">📅 11:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWVGFU33wAoiyJyesCx3MUG2BxeR2w8Ijm5Tolo_nKPqBMs0Pc2dL8UNeimgJqnQWjF5_AZ_90EGKqyxky-5oQXT2tXR9GoPZAXVaIwerzg_kjTFnvMiovUE98T6ZqNimtTMmbiOuu1JomqJnzrne4pNJVC2aMu7AGVONrA56vWOH-TZgIE6L8_hl-2H_nvdg9HHRH99ZT1w9IScnOLT4QGXxcUqLeW5BSXM5IFkLjDadI6tFspPatJ-bNzCYHWcyzwu21mx5CyeVQsmkq8svmiIiqp6qxea2Wq_2OO5BHE2OO2HGyY9KOpt3i8jy3lMuONY2v8qMP-DPz8810dcsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل ارتش: مقتدرانه در برابر دشمنان ایستاده‌ایم
🔹
دشمن تلاش کرد توان موشکی و پهپادی ایران را از بین ببرد، اما موشک‌ها و پهپادهای نیروهای مسلح تا آخرین لحظه با شدت هر چه تمام‌تر به‌سمت دشمنان شلیک شد.
🔹
در منطق نظامی، طرف مهاجم و متجاوز، زمانی پیروز میدان محسوب می‌شود که به اهداف خود دست پیدا کند، اما در جنگ تدافعی، ناکام گذاشتن دشمن از دستیابی به اهدافش، به معنای پیروزی مدافع است.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/458775" target="_blank">📅 10:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/784e0ffb8e.mp4?token=a326ONnxokZzMVvT58fIuZyrFSJJpz8mU6Zd8x0uzGUyDN_wkiqjX5TBAlocYLGve-9VHePF82tGhtfGO3R9vZrYP9wHbM1vQSUoT8oONO_5GfI8RKuFbXm53sooblpWabIoFMel1saRPtUz89efRWoJb-1kHAtadBn09q4ct5Xr7tXMsfOfURjuM8U092iilJVPE1kuS2zXAbfyWBojl42zfWRwBpz39FeGj3NbiJGryMbg2pAlNQUSCCFciupLfgI7cJcMOZk35VjwW11wgLh-u7BMNbkAcMIHFlaO7FnWUUin4Dk6jDJXGhb02ZB8XmJiHjjNQ5M7xcY-28ZxyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/784e0ffb8e.mp4?token=a326ONnxokZzMVvT58fIuZyrFSJJpz8mU6Zd8x0uzGUyDN_wkiqjX5TBAlocYLGve-9VHePF82tGhtfGO3R9vZrYP9wHbM1vQSUoT8oONO_5GfI8RKuFbXm53sooblpWabIoFMel1saRPtUz89efRWoJb-1kHAtadBn09q4ct5Xr7tXMsfOfURjuM8U092iilJVPE1kuS2zXAbfyWBojl42zfWRwBpz39FeGj3NbiJGryMbg2pAlNQUSCCFciupLfgI7cJcMOZk35VjwW11wgLh-u7BMNbkAcMIHFlaO7FnWUUin4Dk6jDJXGhb02ZB8XmJiHjjNQ5M7xcY-28ZxyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شکست سیاست فشار حداکثری آمریکا علیه ایران و بی‌نتیجه ماندن بیش از ۳ هزار تحریم برای وادار کردن ایران به تسلیم سیاسی از زبان پژوهشگر روابط بین‌الملل
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/458774" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458772">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uz0MBI5Ub7h2dp83eEQ7oA_6sz0jUiF0q1pcxACI-ce27m1Euq_Ve6oO5P_nktfvnKHP8bmG9BUNatgqBgqMgzdY9LOv8eBhaq_HzSJnZ1hsSRMglQxHPSpLn85zRXMOnmzUBReAdszSfCNMEjDWzrfAeW43nFrzwOyTO8UHtJ9IKeMTK9X827_FL-k-4HJukAs2bjLB3RsPd5DcF8yrMqORzCMApGo4YDo4qw7VfEjl3BWuwS4V_IA7FYSm6fmYewu_ARAvVk1oa52M8Zm55WgeaS4RtruKuAyT0LZ9MPdHS_EnuTozcYdNsUUNfDcwYJO5w3R25EdGv_zufFaetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۵۰ تُن تخم مرغ احتکارشده در قم
🔹
جانشین فرمانده انتظامی قم: در بازرسی از یک انبار، ۵۰ تن تخم مرغ احتکارشده به‌ارزش ۱۳ میلیارد تومان کشف و یک نفر دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/458772" target="_blank">📅 10:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e424e4f6eb.mp4?token=PMPlLAu_5vkQG3GW_feVdeBOH5XGebpfs5AJhSkXtnEA8KHY7zE8ZxwIGslMAATYmkHySHtQLlwgAx_nDMI6sya551_sCIlDTcD536BQ72GFwCE7az2epVd-og4f6BWl0C20P8t0AeY6ygaA7QVTBUtsioX4TWIO_uAJ_jSbdEHYrnIG5LIdEuoq2yP4fYvchtc8qY7eCA2Htdd-rnUr81IkMkwRemKEt9Ue4NuZ25AhkM5k3hzWofjE-80L6_ZBIjWNXKCRHlGQbDfsO6ekVTR6T_EpLe7TJYp39YHQEfQ3iqyVE_wi6UaqweK3ur7wUEK3HexIPYEABhlGpoIPZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e424e4f6eb.mp4?token=PMPlLAu_5vkQG3GW_feVdeBOH5XGebpfs5AJhSkXtnEA8KHY7zE8ZxwIGslMAATYmkHySHtQLlwgAx_nDMI6sya551_sCIlDTcD536BQ72GFwCE7az2epVd-og4f6BWl0C20P8t0AeY6ygaA7QVTBUtsioX4TWIO_uAJ_jSbdEHYrnIG5LIdEuoq2yP4fYvchtc8qY7eCA2Htdd-rnUr81IkMkwRemKEt9Ue4NuZ25AhkM5k3hzWofjE-80L6_ZBIjWNXKCRHlGQbDfsO6ekVTR6T_EpLe7TJYp39YHQEfQ3iqyVE_wi6UaqweK3ur7wUEK3HexIPYEABhlGpoIPZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ جوان ارتشی ناو لاوان پس‌از ۶ ماه دوری از وطن به میهن بازگشتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/458771" target="_blank">📅 10:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458770">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/458770" target="_blank">📅 09:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458769">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe883ba3ac.mp4?token=gBdwtNKOig1DKWtpA8pybMFTjiwx4OMGjm5QA-YWMPve-k8KACBsft-8xIUU1SbuF-FxVJjEGn74RjqSPxfpt3_SYfG0kYvEX84jcLWsqBQu3dfAjKKTLhckf0QTy7GzYheETcFxy9ZkUYdDYrvQ3we3too4LD0g58Pj-F70LwL8IgOvn_DTt2A9KwCTgsCLgDRwWMTsm_SGW7hXb6hT-bxDPxKKIlD6cXrk4p0cZdB8uo0yXf0LaRub84aSlWrru0dpGZq0Sk_TF1eWrPejNtVWq9_8agmFfyDMlr9YFjvKDvBatStM4hqkvicH0zJk5OEM4vX37Vm6WW3aaTaJFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe883ba3ac.mp4?token=gBdwtNKOig1DKWtpA8pybMFTjiwx4OMGjm5QA-YWMPve-k8KACBsft-8xIUU1SbuF-FxVJjEGn74RjqSPxfpt3_SYfG0kYvEX84jcLWsqBQu3dfAjKKTLhckf0QTy7GzYheETcFxy9ZkUYdDYrvQ3we3too4LD0g58Pj-F70LwL8IgOvn_DTt2A9KwCTgsCLgDRwWMTsm_SGW7hXb6hT-bxDPxKKIlD6cXrk4p0cZdB8uo0yXf0LaRub84aSlWrru0dpGZq0Sk_TF1eWrPejNtVWq9_8agmFfyDMlr9YFjvKDvBatStM4hqkvicH0zJk5OEM4vX37Vm6WW3aaTaJFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: در این جنگ موشک‌های ما امتحان خود را به خوبی پس دادند و به خوبی از کشور دفاع کردند.
🔹
یک نکتۀ مهم ثابت شد؛ هر آنچه در داخل کشور تولید شده بود، بهترین کارایی را داشت.  @Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/458769" target="_blank">📅 09:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458768">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4912e94ccc.mp4?token=GcbgFji0x51rL-d8PdG_5ELG-brhM08jm-3EQ2pqIBAHbUGkhPRiCCeKQrJ8AZcaPTTqII-a8uEgmGYRgq5idx53ewV1-aDyHYO8tIiPBSuSF1N5gHMsTZI7guRFmqlF-kU_iXhd8O08yUDfyrOrkU_rWAXosZrsPAjCT6KGZ0VrFtbjOBPl8pYncnWrOJgn47_VnN3EfvP1GgHr3bn9t98-7RvhYcXmtLN-2L1Fd2Sk9Rm33M6qWvmVqQXUjuRFyikY2psLUzUq1or7-fyn30N1BTXwJWQ1F9LDleyahqBoFHaSaliAL6zahr1eYJA1HuWKh4tEemfMv0Llo6e3GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4912e94ccc.mp4?token=GcbgFji0x51rL-d8PdG_5ELG-brhM08jm-3EQ2pqIBAHbUGkhPRiCCeKQrJ8AZcaPTTqII-a8uEgmGYRgq5idx53ewV1-aDyHYO8tIiPBSuSF1N5gHMsTZI7guRFmqlF-kU_iXhd8O08yUDfyrOrkU_rWAXosZrsPAjCT6KGZ0VrFtbjOBPl8pYncnWrOJgn47_VnN3EfvP1GgHr3bn9t98-7RvhYcXmtLN-2L1Fd2Sk9Rm33M6qWvmVqQXUjuRFyikY2psLUzUq1or7-fyn30N1BTXwJWQ1F9LDleyahqBoFHaSaliAL6zahr1eYJA1HuWKh4tEemfMv0Llo6e3GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پل‌های آسیب‌دیدهٔ هرمزگان در چه وضعیتی هستند؟
🔹
راهداری هرمزگان: پل بزرگ گچین کاملا نصب شده و درحال انجام آسفالت آن هستیم؛ پل کهورستان نیز تقریبا به پایان رسیده و در همین هفته بازگشایی می‌شود.
🔹
مابقی پل‌ها نیز که اکنون تردد در کنار گذر آنها در جریان است، تا پایان شهریور به‌اتمام خواهند رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/458768" target="_blank">📅 09:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458761">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwBHnNmL4VnBR2U9b_s-8Ocbkq5Cxvu-uqD3zaE1nBJToyjQfxCGv86Ibhk8EmgkLyaa3_BOeNPteMvTQ7FGv4j4vb0uUOFxmnvA28GQ8vUJayEpWpA4nWAA6zn4WnbrSE_nUFUeu8J0gKnaABlxC0JDJP8U86rLtHcBf5lpqgdQrffUbLEZ2hwzddjeU1xgXf2Hu9r2zNf96YLdNHGbydiSmzuATFCkkSseGfU06h4tQ-XX-ypxmWE_fCSL4f_VVyWFE08_3_x6yEe_uGZ-ETaxyB3Fl4ZpcdDlmtndWOLoJooYoSNm8hSynalU5KuTvr-ulKDUyXqVroQ0WirmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-B8icxdCt0jOCHkk532wHboDVvO6PPuDF0EbGyi5UrKBbhSzgZ7f8jtCSmuMWdXyzPspDUjO2XUYLAlRjCI9T6DziUW4CPWcQZkBxi7S0KzEBBQ0GtDu2dWa25buFXtDMaAvx3Esr2ggXECf_6Ix3i6GXUQGxPp_95boy8QrR-tQqg5tFLrVC_bykSODvlr9RN5peTyBFwvOLdgy0KsOwTsqlPHkHgIIqLHsqQgt07Ps0o6yhGW6eUISSGnJFdam_wCmthVPhMXsEDrZZH6Td5ytuOxsdgcDDC1JBm48NL5Qg6zO9HLPMHtwzl3HyMz56d6HSIQYP7Uq8fHrxrFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lkP5DqT2ocmeKc2EwM6_gG9HS8Lm9n7kVISqFlMJ8FmKhNJDUlBlJH2ifKlOw0iBTYd4yxN6zgvcYG3jFMRVQ7JgfVXEAKzKrP2PSQj76-vWU3LNtO4RzsZ9_9dw830wmYJwFQvgCRkvGOIVtwN4pCefZxy18zuW_aSLwuA0puJdrdOeDzR4m7XC6e3i94oeEoaGNjEsA1t2koPHXYSwF8UbzThrLUkSiEywksn83Gy5UZbZQM7PZK9fLkw7EZB00OyjT5SP2tkVH_1afnF9cPRwNQzrjD1Pi53-IxkcCBhbP2x8t3UMs7LhmWZbKnaW_hfQ6PSFtOr8Okbg_gpNJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uPQXPCVWvhDN_-T33Zt2GPmR57EBAHrSgBalsL-YI7LMq-EoTtp1Em4cUM_xhLzz9ObBp6cm-vCTCxx2eOLE-hOApGh0uDeGSOcPU4TjkcQqfD-ax_s16zDYy71BurWdzoeKeKf5Lgeb75xXuyCTskc53_8tcBzIm8jDzKiQD-2Z3YFygmkGcAgRgsJRvXtnV3b8Kh6ZuMFY7DNmlrJ5VO4gROd3l11CTTfw_48F8uk8661mHav09_3J3Rer3ylzNiCLKQxas65qyrqaoLk_WbnsXImPVN7RELMl93lnCeRHSvuFsKqFkFx1WdRAc4fAgq7OZbqU0JBfx1AWD_tGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPF1BIO9HAQTTv4XyGVfUH35ZTq2ikmLLA80OrLD32wBLxwsEbe5h_pzFVyS2o_HqN-KS8Gs3iUiYjxjGIWbnM0kmlXNUlx3niq9nMw9kqt3o6Mk8wtb3PrM_xs5WGZ5r7HxgIVvU1joKrJVCj8hPoYqB_cvEY4zo7XG8nSx4xIZ4iKAkbtqrapmWVXE5vD9wM2MyUZBVpO-oyhNbGXf11GNj_yAFBneeTMWEDdsbvVrgWDcf2xdZtXhdo2GJtmt_rIyQ8AnzOkBVFOWCrYolXal9wBNwS1obfj2rONNF7rGYEEHach91DgjrplQPyMLRprv2a8vyOjxMs56zp1Wsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mw9Zwi1iGCFUUc8soBvGhhE7LX1LBF30k_BEOqwVeFA3bdvGzR9LWKcJ37NaPMGG4STiMPdQaSRBO9HTM1Mh1qeAdSMcgaaVHan7JMDJOWgCWq9oTXhthkY693-kV83Z2A6NNEQ8oHPCE_bo7Mp-yO3juc97asvCANhaP9hdCZ-9ios8jkdmHy7LGR98uhKLcfesj12kZMLRTRsSMvs2I0P3PlgkX752oP58z1Kz-O5icbsQ-VJfMm82wVGAQRR91Dl4xFbi5lIaNsu33TuTx_iiR9spS1-Cn_FXuc0x_eMrWqLuMpZhz3e7xeX4woVuR1LIhrAEcuiMrZw4T_L7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IszVy71h0eg4z4pCf-gpiRy-1eJGcBP9JfUY4bVhVIVo2d9D2mRDgYeKgMmhMIqs-DL5ce9pr6yJmlN-AV8aTk3EyX5IDoQrV8808ojBooSMTEaI50EqhzgvT0mpwJbRJk_VOJJiSTLMdptE5Z5ZAsPI0JnbKiYXnv_i-vpdLk0rYwJr_2UPJR_wKSZa0atEmqG1FeNBk1chdlMNAgchlsrX-956_DeJ-j_Q-vgoBUf-eGX7WUuL7uivQ5O8Zx83u9U2ozJ2WJkr4Kqq-owVT3yLsYIyt0ZczXYUs1ybIEhJgDJpsP4fAqZBLQaKU8Y9I6Nn25sB8V6CvyS72le26g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات کاراتهٔ قهرمانی دختران کشور در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/458761" target="_blank">📅 09:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458760">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5nXOWl9-kUaIBNKruLsp_mg-IP-fnvYsNQczQHJ_9AXnTg78uHNplX5i_StJtMDo-GfjMxRlNsbazcFsOe2ocJTdv984W31Xz02T7IMddXvZtYnc9OTi1QKb_pCleXX3PpUVk6S_Id7pphMJhasJ06Jg0LsRsrWg39UNjebMIpcc0Kc08e3-K0-l4FK2NcXdvUfdb5SHFFxyEX_Y0Ki2wvSeaOcdFAqcrzwqRkujZFMrPQ4I-ob28WuT21N34KqtuspSVxFN6nGS194XS3X0snMR8OY5Nlp8QYunXefN7tI96baITzNFGN8GnykZRjoLNOrw_w42yK5kvPlbOW6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنوعیت شنا در دریای مازندران
🔹
استانداری مازندران: به‌دلیل مواج‌شدن دریا، شنا، قایقرانی و صیادی در دریای مازندران تا عصر فردا ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/458760" target="_blank">📅 09:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458759">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
آخرین اقدامات دستگاه قضایی در پیگیری جنایات آمریکا در جنگ تحمیلی  @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/458759" target="_blank">📅 08:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458758">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0FnzwkC4-zdzh48DTslcPDeue2KwcVq2iZuCTZ5yDNC9lFCJB-mIX7HM9zSJFYPWk92twA2rWdLWfp7ruWfalttmpFXvawAz4jcuHvu8DIzQ4kuN0b0zpH5CVYEYhvJ2Gfo7Bqyfsi7Jv-SIyBppVecRhY1LrW4H3guT9GaPKxtTp_qzWkomzndEI1xSdGkqsn-Ib4ykjoGbomjSX3RuTCvk85svshSF3QUaTCiT2SCgQwAxxejaqDwzwOGAQk4klBBUdpkT7bTNR-v0W48i6cY3XNOnz9P9FvHse9gRLN4-fZE96JHjtYc0_dQQ_XAgQ6mxJEXKL-zZwg-4sHHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اژه‌ای: پیام رهبر انقلاب نقشه‌راه همهٔ کارگزاران نظام است
🔹
پیام روشنگرانهٔ رهبری معظم انقلاب به‌مناسبت هفتهٔ دولت، به‌مثابه یک نقشه‌راه برای همهٔ کارگزاران و خدمتگزاران به نظام و مردم است.
🔹
تحکیم وحدت ملی و پرهیز و احتراز از هر آنچه مایه و عاملِ انشقاق و افتراق است، یک ضرورت حتمی و قطعی است.
🔹
تمسک به حبل‌المتین ولایت، تنها راه عبور سرافرازانه از گردنه‌های سخت تاریخی است. ما در این مسیر پرفراز و نشیب، هرگونه تشتت و اختلاف‌افکنی را پس می‌زنیم؛ در منطق انقلابی ما، پیوند میان امت و امامت، سدی نفوذناپذیر در برابر جنگ ترکیبی دشمن است.
🔹
نکتهٔ مهم دیگر که در پیام ثاقب معظم‌له مندرج است، ضرورت اجتناب از ضعیف‌نمایی و تبلیغ و برجسته‌سازی کاستی‌هاست. قطعاً و حتماً باید نقاط ضعف را دید و برطرف کرد؛ لکن نباید در جایی که دشمن غدّار و مکار کمین کرده، برایش خوراک جنگ روانی تدارک دید و موجبات یأس و انفعال جبهه خودی را فراهم کرد.
🔹
نقد دلسوزانه و خیرخواهانه، آری؛ سیاه‌نمایی و تزریق سم ناامیدی به پیکرهٔ جامعه، هرگز!
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/458758" target="_blank">📅 08:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458757">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‍‌  رهبر معظم انقلاب: گاه بیان صادقانه ضعف‌های خود در وقتی که دشمن به روحیّه نیاز دارد، کمک بزرگی به او است
🔹
هفته‌ی اوّل شهریور هر سال، مناسبتی است برای پرداختن به خدمات دولت جمهوری اسلامی ایران. امسال دولت جمهوری اسلامی ایران مفتخر است که ایّام هفته‌ی دولت،…</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/458757" target="_blank">📅 08:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6ada826a.mp4?token=lkElxHviGnJdRnLJATS6ROuiowVqoAJFcoVQpyT5n8FQCuyllCpo4cMfE9UniIYUj-3fpQlcx5RDO6LcvOKCbQKc9UxY2r-LXVxD-9GkVXCooYmlW1BFQoUPErhxrFGLlsheqot8x-Jg9yK_lD83Z10fUm7dqx_gJPDVGsZF_mG6LlmyePclqlXebj3D3IAbHQTzFUGfStopORDyxMBHsZzZLTnvZ54Y36fO9ul7bktEiSnDR2FxYbHFNK_YehZfw2STKL0No1QoCj2WcXWGaM8Z229i3jmMWk5M2WnvhxzYCh2fNDRAl3o2iCfiUDO8iJtH9ACV-a7GovkGbg03rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6ada826a.mp4?token=lkElxHviGnJdRnLJATS6ROuiowVqoAJFcoVQpyT5n8FQCuyllCpo4cMfE9UniIYUj-3fpQlcx5RDO6LcvOKCbQKc9UxY2r-LXVxD-9GkVXCooYmlW1BFQoUPErhxrFGLlsheqot8x-Jg9yK_lD83Z10fUm7dqx_gJPDVGsZF_mG6LlmyePclqlXebj3D3IAbHQTzFUGfStopORDyxMBHsZzZLTnvZ54Y36fO9ul7bktEiSnDR2FxYbHFNK_YehZfw2STKL0No1QoCj2WcXWGaM8Z229i3jmMWk5M2WnvhxzYCh2fNDRAl3o2iCfiUDO8iJtH9ACV-a7GovkGbg03rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلفات سیل ویرانگر نپال به ۴۶۹ نفر افزایش یافت؛ ۱۵۰۰ نفر مفقود
🔹
پلیس نپال از افزایش شمار قربانیان سیل ویرانگر در دامنه‌های هیمالیا در مرز این کشور با چین به ۴۶۹ نفر خبر داد و اعلام کرد جستجو در میان گل و لای و آوار ناشی از سیل و رانش زمین برای پیدا کردن…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/458756" target="_blank">📅 07:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458755">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1G_uiM2rJFFEEPxRipcI1fFuNBspnDIlWRJQp17cCo6dkFWjKf9yGZkjhJL7_q2feKZGggoAym7PtGZayN0kSBt59LKIR-pbHVIkuOvP8YxpUj_knk5uLmgHQ5Dnt_bPxAHnUWpZ6aBEHHv1v19XwRUr6mgb5hOpDPf4apW5IeMUBzkPUlv_dg07h0zTJS2u17Uix4G9Nnqtvedsp9KApePsIYLWz3TkZQU8K0FjEYhp2OtCZiRWZ8MB8fjd6moHlqeF85UDp35tBSwjA67EhBqxa86cHNK_KfgbeegmAVkvRfUk2qABEPwBjcMRVBKtDERDgPmPitQgvEdGS76Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول نفت آمد؛ مخارج دلاری دولت تا دی‌ماه تامین شد
🔹
طبق اطلاعات کسب‌شده از وزارت نفت، ۷.۵ میلیارد دلار ارز نفتی مرتبط با فروش ۴ ماه اول سال در اختیار بانک مرکزی قرار گرفته است.
🔹
این رقم ۱.۵ برابر درآمد نفتی در ۴ ماه اول سال قبل است.
🔹
طبق روند بلندمدت هزینه‌های…</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/458755" target="_blank">📅 07:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458754">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در چگنی لرستان
🔹
فرماندهی انتظامی لرستان: عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده در محدودۀ شهرستان چگنی طی ساعات ۱۰ الی ۱۴ انجام خواهد شد.
🔹
شنیده‌شدن صدای انفجار در بازۀ زمانی اعلام شده، صرفاً مربوط به این عملیات کنترل‌شده بوده و جای هیچ‌گونه نگرانی برای شهروندان وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/458754" target="_blank">📅 07:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458753">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VydKff7BOJmx7ZOx3Duq-ZTAlufygJJVWvm27pLjRyZih42h1GuOkOikD3QyF5SyGr8m6HecMMWXGDb6A08JIbB4u3SFuqL0AC0pg6shULHiy29HXKdvF77OXIP_dkUcESX5fieiVuQrsBF3Fsin0SOkzpU8YCSy0xwueyaZjiB85N_y2CxDP-qsT24MtoV4ewof3YueFBgr9W0mHSLcRC8Mc3tuFKunOesce9z8Y7TqpYWp2KcDGASLPSQZJ1EPOBMFZCNin76s1pIxllHKwjzm8Y5u8pJbSUXts7YB-S-nV-mqFe6HfONXW51gxFtr04blFe8MMN_Mg1zuWS8zbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال کشور از دوشنبه پاییزی می‌شود
🔹
هواشناسی: انتظار می‌رود از دوشنبه و سه‌شنبه، هوای خنک بر بخش‌های گسترده‌ای از کشور حاکم شود. این افت دما به‌گونه‌ای است که بسیاری از نقاط کشور دمایی کمتر از حد نرمال را تجربه خواهند کرد.
🔹
همچنین پیش‌بینی می‌شود شرایط جوی و دمایی در نواحی سردسیر شمال‌غرب و شمال کشور، حال‌وهوایی «شبه‌پاییزی» به خود بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/458753" target="_blank">📅 06:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458752">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d5ce90ea.mp4?token=REyCM6mwZ13vvcz0MsTnPI6lC7h6QG8ziIt3WnnqGBg1UqIMMeT_UE0x0IKZCK1OuGIERdJnX_Aw03Kp4I-MBuFZF3JDQ35GUYK2FMXNU7lXfxLZcYem8k9EGmwJvzqc4Ajy_plBdzKgwLm_fd-YuO4o1nE9C66TbUTqEOTkEF87NDe2STWtoDE_6SrFBHpPDwMjk5JWXG3tM2jIZ9frdeviuN7y3aRhJLyh_9vQDeXUpUSNnjGdEQMPQMnfEYtd-xNNq1cpqZEZEPEsZIKPo0y-oz_fdc4xIzI-udyEsqTSmnUAU_vmPKveZBzUU-gYaYJu62YY23vq5P_v1wS9Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d5ce90ea.mp4?token=REyCM6mwZ13vvcz0MsTnPI6lC7h6QG8ziIt3WnnqGBg1UqIMMeT_UE0x0IKZCK1OuGIERdJnX_Aw03Kp4I-MBuFZF3JDQ35GUYK2FMXNU7lXfxLZcYem8k9EGmwJvzqc4Ajy_plBdzKgwLm_fd-YuO4o1nE9C66TbUTqEOTkEF87NDe2STWtoDE_6SrFBHpPDwMjk5JWXG3tM2jIZ9frdeviuN7y3aRhJLyh_9vQDeXUpUSNnjGdEQMPQMnfEYtd-xNNq1cpqZEZEPEsZIKPo0y-oz_fdc4xIzI-udyEsqTSmnUAU_vmPKveZBzUU-gYaYJu62YY23vq5P_v1wS9Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای زائران مزار نورانی رهبر شهید انقلاب؛ ساعتی پیش
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/458752" target="_blank">📅 06:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458750">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m69dSEPNxLFFF1Au5dvuzsAmUrGoeOZLTzUuI3LjoEFXFYvkhRnt0ldx5A0lrpE72a7OKGvpSlsU9BU-sznSAsTrkraJDiSRx2Xhuy-mgZzPmD0fv06_XtHq1UPrcG6GN3cvNBkSfvDWddNxqR4NHgU4Qzh0ck7tIJTyQparlnJ6Md6EEG2E_XF3ntmxemfYqxkzyOzhX16quB5gSJdBehNCiddRZqNLVTwYbSZNQ-IhaVxXPn8GzjuCexrviT5vc9mFQUEfAMzYkORs0mK5s6jPwuCIzqAlHH7P147y0ZNSnxEUkYAdX7n4M6O57TtQqchzciWF7B7mERt4feB_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXWnBV6X58h39o0j9_hbx8M68_lhhmAMxCiTNHIi75nQgy0sG5iFD0jcy6ro-8YdXj2TLBns6KDwkUpNqS5MzhxRpLwQwuUIo-AHB8ShiTxgO7q4xsHF2L-KeOrg_EJUyxvl3pUkcE2jeW_hOzIZZShN_m3wlw1UoDys2PoiZZ-Xmx6-jXiOktBGQFUbainZoIV8rKULtJoaQmogS9mHvfGSF9N5WzfBVpBS5-Q59lpb-MqAiSoZUNg8bYmoSvJwFa5Af-qacYerVgA8EcOwskClOphY5FK8EG-xn8tVj7dbUl90bOQ014494vnEY8YgGQm-Bb6dc4_mJdHow1nylA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی امواج، پیکر نگهبانان خزر را بازمی‌گردانند
🔹
فوک خزری نگهبان سلامت اکوسیستم خزر بار دیگر دو پیکر بی‌جان خود را به ساحل بابلسر سپرد تا نشان دهد که توازن حیات در این منطقه بیش از هر زمان دیگری در لبۀ پرتگاه قرار دارد.
🔸
با کشف این دو لاشۀ جدید، آمار مرگ‌ومیر فوک‌های خزری در سال جاری به عدد نگران‌کنندۀ ۲۷ رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458750" target="_blank">📅 05:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458749">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSRVJFWW80EyIv4OGFnt9alQqTcfEYsIG5XgebejfghOtVC6L_zJ0qyKzmJNxCsbub4yTPjoPInt7HdwJdnmbRcHq0a_0z76lGtWYVUmwXEQ5XALsMWg1PnwFx-lsYGLCkf7_YWwfiTh1jZHfJMym7yCPwamuRP4XIVNizTBmYRCbaaKt-JzzmEp0Va_vnEwP6afzrV4H8JVgfKQuQl9q7-fnIHPJpmsyY1YlgkL7i3WdGR_QGFbeUOBomGaArpnn6mnnLumHt1_OXlJ7ufKtyC1lKsjuwVPJw_ql_6QTgLoGpwTAzQ6WSojGmOLFhVSOiiRMtQT8fogVllzBvEhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروازۀ نجات تجارت ایران در آزمون کاسپین
🔹
در شرایطی که اختلال در مسیرهای جنوبی و افزایش نااطمینانی پیرامون تنگۀ هرمز، تجارت خارجی ایران از بنادر جنوبی کشور را با اختلال مواجه کرده، نگاه‌ها به سمت شمال کشور و ظرفیت‌های دریای کاسپین دوخته شده است.
🔹
در این میان، شکل‌گیری آنچه برخی کارشناسان از آن با عنوان «اکسپرس خزر» یاد می‌کنند، اهمیت ویژه‌ای پیدا کرده است؛ مسیری که می‌تواند ایران را از طریق بنادر شمالی به روسیه و سپس به شبکۀ حمل‌ونقل اوراسیا متصل کند و بخشی از نیاز کشور به مسیرهای جنوبی را پوشش دهد.
🔹
از سوی دیگر، خزر می‌تواند به مسیر مهمی برای واردات کالاهای اساسی، غلات، نهاده‌های کشاورزی، چوب و مواد اولیه از روسیه و قزاقستان و در مقابل، صادرات محصولات کشاورزی، صنعتی و ساختمانی ایران تبدیل شود.
🔸
بنابراین در شرایط فعلی، اولویت باید تکمیل مطالعات و بررسی همه‌جانبۀ سند و نه تسریع در تصویب آن باشد.
🔸
چراکه آزمون واقعی خزر برای ایران فقط این نیست که چه میزان آب یا بستر در اختیار کشور قرار می‌گیرد؛ آزمون بزرگ‌تر این است که چه میزان تجارت، ترانزیت و ارزش اقتصادی از این دریا نصیب ایران خواهد شد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458749" target="_blank">📅 04:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458748">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc7c0c7eb5.mp4?token=GezJzLDZRTY2YJ_M2WIQ-RO6GjhkORRAmi4RDCF2wAkL1oLPZmZz9J33HOZGTXBKa5Wwi_6ijIfP7wq9h-R7jnNFA-WC8b4SGG3SDOn-riwSZ1BpovzQ9_0XRqiHPY-vaKlYxUkd80ygQIRAHtOKpGslmYgicu5kTdP2PxOvxF50QVh69daBIbiA1zELXSonq54L9KIjTHwH-Al3zr29HeWQRIAkEjJ-_J3pEywEFuSGtmCbKJPuiWf5XR29KqPKGQzUelZ4n8xelZrDj4H2h6Hdtdunsf59ZUWWPzjAEV92D-T-jc0ax1L64X9M-j4_T9Gb3pbctb3nB2fDikWhnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc7c0c7eb5.mp4?token=GezJzLDZRTY2YJ_M2WIQ-RO6GjhkORRAmi4RDCF2wAkL1oLPZmZz9J33HOZGTXBKa5Wwi_6ijIfP7wq9h-R7jnNFA-WC8b4SGG3SDOn-riwSZ1BpovzQ9_0XRqiHPY-vaKlYxUkd80ygQIRAHtOKpGslmYgicu5kTdP2PxOvxF50QVh69daBIbiA1zELXSonq54L9KIjTHwH-Al3zr29HeWQRIAkEjJ-_J3pEywEFuSGtmCbKJPuiWf5XR29KqPKGQzUelZ4n8xelZrDj4H2h6Hdtdunsf59ZUWWPzjAEV92D-T-jc0ax1L64X9M-j4_T9Gb3pbctb3nB2fDikWhnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امیرالمؤمنین(ع) در آستانهٔ میلاد پیامبر(ص) گل‌آرایی شد  @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/458748" target="_blank">📅 03:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458747">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrHoGox8ayQSlke8vj-8H2NzToHg3uxYQ2dCscOFdQCeznx-g7iSueEORWAlOqMC1SEVspWL3878LBL4SseQtIXAKz5OA9sBlR7J-xlvMkU4LNKyumPtQAS_qyeN-OHI0CA4UA1DTwl9SESB2ZJpONDV_Cr_LoKm8J8HQRkaoySn2Oj4PU4V4xnTnoYb_67EYUFiKMnErcGxFdVMoon9nAovQL6h4UsVD_-Vj0tXDndedMafjEokOn5o8DsRPCYYkZNUb8XW5dL-rdO3xN-hk0BIO7VH2IqBCLc7wvdjKtcwyPykMCSfjbClq6Pf2TwSkENQJHVazQOuGXl0S-jtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایدۀ عجیب چینی‌ها برای ساخت عضله
🔹
پژوهشگران چینی روشی آزمایشی برای ساخت بافت عضلانی در بدن توسعه داده‌اند که به‌جای پیوند مستقیم یک تکه عضله، سلول‌های عضلانی را به بدن تزریق می‌کند.
🔹
آزمایش‌های اولیه روی موش‌ها نشان داده این سلول‌ها می‌توانند در بدن سازمان‌دهی شوند و به بافتی شبیه عضله تبدیل شوند.
🔹
نکتۀ مهم این است که پژوهشگران تنها به افزایش حجم عضله توجه نکرده‌اند؛ آنها بررسی کرده‌اند که آیا بافت ایجادشده می‌تواند مانند عضله طبیعی فعالیت کند و موادی موسوم به مایوکاین‌ها ترشح کند یا خیر.
🔹
آزمایش‌های انجام‌شده روی موش‌ها نتایج امیدوارکننده‌ای نشان داده‌اند و در برخی مدل‌ها، این پیوندهای عضلانی با بهبود وضعیت عضلات و بعضی شاخص‌های متابولیک همراه بوده‌اند. همین مسئله ایدۀ استفاده از بافت عضلانی به‌عنوان نوعی «عضلۀ قابل تزریق» را مطرح کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/458747" target="_blank">📅 03:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458746">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biV2YorEsv_z2XHJFZS3vjMHHVXGtdthdEvFJHyyN3uP8ceEcyfwFRV2duUFz12-4d8ns6DHQZV7DeIuiBz2_QoEhStsXTFP-3b4xMVahZMsYcGRFw3Pu2MnW2DIO-4vxORlD-MQXaWvXJFdwp8l1W3u3cyoa_Ze6O1t0pKvpKXijcgH-mhpsq7suFs6WdfbjC50fsFccETbZpcadXV6a3D3R4DnW_XWP0K-4LF_2xu1ib3r2kYPWIIeBgf_-CX8SDiFhY9whdHnOcwOMzFU9Ayt_88WJOFHjXwETCmUPZ-EzjgzuPJsOvinaP5EUxbAr8WRpv83ldYhBlDWI8d80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداردهای خودرو از ۸۵ به ۱۲۲ مورد افزایش یافت
🔹
رئیس سازمان ملی استاندارد ایران: استانداردهای خودرویی در اوایل امسال بازنگری و تعداد آن‌ها از ۸۵ به ۱۲۲ افزایش یافت تا با کشورهای جهان هم‌تراز شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/458746" target="_blank">📅 03:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458745">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3bn-1hClKCjOXP5OGKqGgvusTpAI8HpFKAzuZqRd5VLaRioMlgiya9Z8gUFMmJs0IATDVUuqzn9gnKlRPsP-KPTQ5SoeTRQFdv6F-UpXOB4vYsJmU7PzwT_hGhg_Podzy9-N8U8GbjKrZoLYKBtm6XsNGKqiaALx0O0sGIWZH9JFVgTMyvpgKGY6JKvy_YfM4Y4omy_BgrcPpRf5dWM8Lcdw_MdBZ0OVeNRaLKnRX3TAL2g5wxhCQiecmMG8KVHuXxO4N4jLzuA5kHIb7rRPwAZAC6hMocaUzIWA5wO1q2wXDniYxRqKv-Ivf0ez-omE6pPoAdUNlnzo-poSNTs-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: «بزرگ‌ترین قرارداد نفتی تاریخ» را با ونزوئلا امضا کردیم
🔹
رئیس‌جمهور آمریکا، مدعی شد واشنگتن و ونزوئلا به توافقی تاریخی برای کنترل بخش عمده‌ای از ذخایر نفت این کشور دست یافته‌اند؛ ادعایی که هنوز از سوی مقامات کاراکاس تایید نشده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/458745" target="_blank">📅 02:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458744">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4pqZdmqKzaFbiuNXKAQZAryrX_g_Z2VuP2RwtT9NFnWzyOIaqBgs72nrdOfIF1yEjL842oo5caxawQMMVqfzuLFw_pkmJtTgjoQRP-EgIxwTzG0Ee_shzRjQuTViO7G8lNul7oDCTmTdH3sBN6DKGYEcQkJfvJbaFigvre9lD9_jHEi5YFSm7WuCTs7uIesTPxZExxhL9OsaChkKy8Pv1bpchusR-9JOGGftZGpjmmhTNqfPVI4FYxZNR0sYIhK25wHOvUvPdYQgXaJKDpSEdD9ty6qnXGH_J0GCIswkMChxpferDyjS93Q3Ls4nrsE-WYVNcOfKN4_ZGb84uY84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ آمریکا به دنبال جانشینی ترامپ
🔹
شبکۀ ان‌بی‌سی نیوز به نقل از دو منبع مطلع اعلام کرد پیت هگزث، وزیر جنگ آمریکا در بین نزدیکان خود احتمال نامزدی در انتخابات ریاست‌جمهوری ۲۰۲۸ را مطرح کرده است؛ البته این تصمیم هنوز نهایی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458744" target="_blank">📅 02:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458739">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANEdBqGSbGcga3w7ajwo3t1zdUZehAQx7XCDZnG72IbGF-NuZ0J4rL2FDJz1WoiNP1DUujzbHK4hwr6r36P3zLyk56nEAVbmQoPzsYSxNIjiqVqqHJhMCA77EROmcpqDfGk09ReA-OkxzHyeJ7mKt1wRNQgsnU8qHhOzN07ixkYGvveYrHPn6jjjy_cqSDQzQT614J9zBImnXSTlFn5SQRSWGlePJj2GMShMEdpRDkhCZ_iMyzJsoHeDVPMa_cSeJ_28ST6g_w5TFgJuAlT7eKkRZeZZi8C_dPNx43WCDkIdi1sIhbW7Nh5Ri4IpuLY9YzWSm_-R6P8rYU1kCcSPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pNtp2ilq_LNSwpDdmN7ZMqOrJUvdTFG_hpdkv_jM6Ng-flTkyhWnRBIsQJTXqRDLfNdmTgeWi5L3ZJZxNMVAkNnqALlD9DfoeMFxnuO7qYTVL1W6GM_E-bedrOmX788XRn-z_NO43AAUPLw7rpr3pzsQSGnDqZeJElZTRTQtUIMQvlWVhtA9t0H-vvwJk2soIXYjXmP2DpKdgHzyB6iEDN0QjLZyIvpCN8UDxbJQDTZ3AgSWdYJ4BAiERyoAo6kMNdSyLZTnPv1XOgYjKNMwzh4Tc17-DhXGA1Q-Tce-8WR9ijWja-B-Ec_uCgZ13A-azt5SnfyvEdSGcCQR3lRgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AppmNJhUuw5BCkU8O8o4M8CRc5I79eEuMvyhaY77jzUKOHu7ZjL3WerU6ahYJRPD7JHvcK9DmReOAzCa0FPlUbNIOrMO7BAKpA_uli7DU5hDeURCKJMx231Qd83yBe58z65Ujs-i-LjsOZykv5q6pgA7y6QZqwPAwcGhj6fwteATwQhvp7iwHrMjdU1RPHZlXDCRjfRRg9rCZTCB14gaUZNT_dv9ChM4cMCQJaHd-UVEgVqMmFF9WXxfzPQHtfLeYNGqSVZP0YBE9jPeSEOrLQ1SXErn34ifOB2OlOVoLNxMJQPc7pHv2Jb-NrUzAJ3XNEqFv5ZhP3FfR8iJtqzlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l57inzlGwEPtkpNwJLS1n-RF6yOSSAaFQKY9C_CCu0HJeGNq6w87R7iHH13dhiJb2mLcf8IV62-eVQGjCuWh_yK6c85AUw3vjlRa6SL9S5wTY0w_Pes4y7g8MStYqH6dijkURl9PO7TmPDMUPwvDZ4gGdVZREjubTIJphZP-HtEyMmywKjVczNHk8rndWBnpwk6Fvw7xtK81Kez9iNShQihJJlouFcQiiZc_3p8k7eEvmRV1L1M3ihx4TSR2ykT9ABhAIlSK1rpG3AQUemM9to94GShf7oUqzbg672VVcUtBJ9ZWjzlNJuQnZIBbwItkhNSWJGIIgPJXNNQXIqc2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5dzD7zd1ZauHQj31XFuL0asSFNcKnAYiHO80VHcM5bylJf6LLQ8JG9TqVhLN3ipBPZtOlBPnX8lwE1CjSAK3fFpOd8u_DZxfUd-C7IfqZe_vF349DrotQksWCY1KJq6jk0tsrvFUD1A25M1h-way3y1wER2O7gbF7kPxCfU8kO0G9I-6GQV9He02umG5yT_9X1yexwX8qqqmMZvNM4HjAIe6SdLAddL-hSz-YsJ9K8W3V9bCAjS6ogVRGfT52ichS5vBFc1VQdsgDn9BxvJ0w17T02jLuTbiKTGj7n3D7vGhWHK0txKTBUWJuILcjXDUAKCPJZgLjM2tRxwqDb_gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع با پیکر مطهر شهید مدافع وطن در بجنورد
🔹
بسیجی شهید علی‌اصغر نورانی در حین گشت رزمی دفاعی در منطقۀ جنوب شرق کشور، به درجۀ رفیع شهادت نائل آمد.
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/458739" target="_blank">📅 01:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458738">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4b069905.mp4?token=ceL5UO6jEvM88KsAQbjINJ5lMFVvaveJ7swtazLEkNBlpNhyg8Kq_aLSGZOG7Lv8P2aG2EFK5sFMopD1URPOqePit9uZlraLtbyrCIBX1NZPvXWAypHTJNv72cOpBWToImqsd3ivT6u-JZOHODUAhmdvuHmlSIZHNxYTDnc4CaHS-FGsU6Zc13pda2FvnAzbaBkmU3lzFcawu2Dx5G0zXuLx1d2dZW3WmnmJV3txpkkV_b3GyG_Sznd0WLE_JtB0PzFNo3OFFVefoJOiswf-iZKE3uQ_Zw3Um5rps_jOTWKER2m1u54zxJ2JqM8zsT5zBmxAU3Wz_Dw38_c-sZmlaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4b069905.mp4?token=ceL5UO6jEvM88KsAQbjINJ5lMFVvaveJ7swtazLEkNBlpNhyg8Kq_aLSGZOG7Lv8P2aG2EFK5sFMopD1URPOqePit9uZlraLtbyrCIBX1NZPvXWAypHTJNv72cOpBWToImqsd3ivT6u-JZOHODUAhmdvuHmlSIZHNxYTDnc4CaHS-FGsU6Zc13pda2FvnAzbaBkmU3lzFcawu2Dx5G0zXuLx1d2dZW3WmnmJV3txpkkV_b3GyG_Sznd0WLE_JtB0PzFNo3OFFVefoJOiswf-iZKE3uQ_Zw3Um5rps_jOTWKER2m1u54zxJ2JqM8zsT5zBmxAU3Wz_Dw38_c-sZmlaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کریستوفر هلالی، روزنامه‌نگار و تحلیلگر آمریکایی: ایران پس از این جنگ به‌عنوان یک ابرقدرت مهم در منطقه ظهور کرده است.
🔹
کشورهای حاشیۀ خلیج‌فارس حالا بیش از گذشته می‌دانند که ایران یک قدرت منطقه‌ای است که نمی‌توان آن را با زور کنار زد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458738" target="_blank">📅 01:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458737">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c8c594a9.mp4?token=DdftoKB3uw-pCo7fFlKOBZVxAzMFSB0G4z9-GtsZuFJnEE0aUrmV4mikkltC5PP5WPBXYgsqrnivbI1ONxlugeJDDtPXMOMCgp3GdQ31QXSP7Qd4iiv2Mryqi7KIayag__DymlsDrpOyh6Vh0CNaiW4Io_k5GFKT0gLw_d2l47jn0Cp3VwVKbNCRhh3PlIlr82z8lB2HyUbvx2mGb76Ab9_oxeNedBRshH1Z25uCIpcdPfOPXEgQuhOdK26pvqi5hxxVZ38JVbve41BmqDusEQ2M9rbJZjYjytawO4mlAcKND8GLMcW0EIWXW2tpvtnxg3b5v2EXcm-Xl89Qw4LrCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c8c594a9.mp4?token=DdftoKB3uw-pCo7fFlKOBZVxAzMFSB0G4z9-GtsZuFJnEE0aUrmV4mikkltC5PP5WPBXYgsqrnivbI1ONxlugeJDDtPXMOMCgp3GdQ31QXSP7Qd4iiv2Mryqi7KIayag__DymlsDrpOyh6Vh0CNaiW4Io_k5GFKT0gLw_d2l47jn0Cp3VwVKbNCRhh3PlIlr82z8lB2HyUbvx2mGb76Ab9_oxeNedBRshH1Z25uCIpcdPfOPXEgQuhOdK26pvqi5hxxVZ38JVbve41BmqDusEQ2M9rbJZjYjytawO4mlAcKND8GLMcW0EIWXW2tpvtnxg3b5v2EXcm-Xl89Qw4LrCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: علیرغم فشارها، با قدرت رو‌ به جلو در حرکت هستیم
🔹
دولت را با ناترازی‌های زیادی تحویل گرفتیم که همه لبۀ پرتگاه بودند.
🔹
دشمن بی‌حساب حمله نکرد. با این وضعیت کشور باید بهم می‌ریخت؛ اما با مشارکت مردم و رهبری رهبر شهید و مقام معظم رهبری، ما ماندیم…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458737" target="_blank">📅 01:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458736">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbbc03c349.mp4?token=Xap0r8i7gt5PJhOmc45O13R0sxlDTxXpe1sPnH66VvEzbFq_Vf2O-RX2W2k9NLm472MyzJEX5bLr0EAYGHv7iBr4LkbC7EyKTCZpxXn-m-5h5Ubg_faFxQn6gIfG20-MqY9KLZdjkBAu-lGVozPidaO8-ExBydFfpgXbqpbdNUASWC5ZhJJQVT9f8i8W6-aIdHRyqVXDeAaiuI_OktiNMt2CzZf-yE587F2gTy5BGQvXl2gK-UHyYU9FQn-kp7XJJu0pOUuBY28f_NNLuCAY7GhwA0VDJqyKAlIDaG-uK6Vo8QysmroXbMJFAQi1vrTP4DJFnxwp1rSKaFqawaeDZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbbc03c349.mp4?token=Xap0r8i7gt5PJhOmc45O13R0sxlDTxXpe1sPnH66VvEzbFq_Vf2O-RX2W2k9NLm472MyzJEX5bLr0EAYGHv7iBr4LkbC7EyKTCZpxXn-m-5h5Ubg_faFxQn6gIfG20-MqY9KLZdjkBAu-lGVozPidaO8-ExBydFfpgXbqpbdNUASWC5ZhJJQVT9f8i8W6-aIdHRyqVXDeAaiuI_OktiNMt2CzZf-yE587F2gTy5BGQvXl2gK-UHyYU9FQn-kp7XJJu0pOUuBY28f_NNLuCAY7GhwA0VDJqyKAlIDaG-uK6Vo8QysmroXbMJFAQi1vrTP4DJFnxwp1rSKaFqawaeDZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برنامۀ دولت برای تأمین مسکن اقشار مختلف مردم چیست؟
🔹
پزشکیان: با مشارکت مردمی می‌توانیم مشکلات محرومین را تا حدود زیادی حل کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458736" target="_blank">📅 01:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458735">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c249723ebc.mp4?token=rhDTBKHuPcVTUt9fOAkyvYJMM6rE3Z2hqkrzDGI2jtAObi5pSNHNgA4NWkWh9cjAzJJapyrscUNzog4_6S-eD5laW3Cbill29YkEYjWeFEW8NFb7jTRnd0TaEtN5lENjhITe94s9F6USqy6oMrMbPTJ4aUm8OqML3r6SnnVVAEKpmEcerk9KRljo5Vt0aN6uKIWkMq1eGIyvt4uC5dUmU8BS0zf2AIZdKJFtLhImNWDy87s5j1CWk7kD3Nz2jNSr_4V8CbM-bggtIDjdVJgUsVwQ8Cw2fdl5mg1upRr4SgL7BVzZBaHDBtumUgNIhYGFhZLW_ziBAtQxByZ6BSxdrY82Ao6gVkMNfWDnRI7koSDYt3NbELXDhe0mjV5ELCW8OqXTo6FIttozRyjeZN3XxdJXEQiMX4DY7X46l9jh9-1y_OEKpmmQIHbWxv5vWuDNAsTTPyCe3u3xweyWfjU1l18Fkk4pvmn9YxDWw7JdSlityht_qzPwMeKlY6UwWj5NoezCf7m_Kx8mI7uUAz1Xm0_eqiqoxdlaN_v0iCP689ao4AEZD2DAwUPUB4CV88CwMPPkFAofitWK-s_ztTXtOzpBWSweHmd1DDLOJAIXsDd-Tz2Mgx5zxmRe9lPQwyNa6D9QKbEJFTWFIcL0teviUqRxyvU4EjtgVi3LCfTuG00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c249723ebc.mp4?token=rhDTBKHuPcVTUt9fOAkyvYJMM6rE3Z2hqkrzDGI2jtAObi5pSNHNgA4NWkWh9cjAzJJapyrscUNzog4_6S-eD5laW3Cbill29YkEYjWeFEW8NFb7jTRnd0TaEtN5lENjhITe94s9F6USqy6oMrMbPTJ4aUm8OqML3r6SnnVVAEKpmEcerk9KRljo5Vt0aN6uKIWkMq1eGIyvt4uC5dUmU8BS0zf2AIZdKJFtLhImNWDy87s5j1CWk7kD3Nz2jNSr_4V8CbM-bggtIDjdVJgUsVwQ8Cw2fdl5mg1upRr4SgL7BVzZBaHDBtumUgNIhYGFhZLW_ziBAtQxByZ6BSxdrY82Ao6gVkMNfWDnRI7koSDYt3NbELXDhe0mjV5ELCW8OqXTo6FIttozRyjeZN3XxdJXEQiMX4DY7X46l9jh9-1y_OEKpmmQIHbWxv5vWuDNAsTTPyCe3u3xweyWfjU1l18Fkk4pvmn9YxDWw7JdSlityht_qzPwMeKlY6UwWj5NoezCf7m_Kx8mI7uUAz1Xm0_eqiqoxdlaN_v0iCP689ao4AEZD2DAwUPUB4CV88CwMPPkFAofitWK-s_ztTXtOzpBWSweHmd1DDLOJAIXsDd-Tz2Mgx5zxmRe9lPQwyNa6D9QKbEJFTWFIcL0teviUqRxyvU4EjtgVi3LCfTuG00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور: به‌جای گیر دادن به هم، نواقص هم را برطرف کنیم. من به تنهایی نمی‌توانم مملکت را درست کنم اما باهم می‌توانیم. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/458735" target="_blank">📅 00:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458734">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5f0f13f6.mp4?token=blO9qKTYMlBgsy34FK_F-HNjNGNJQNCvC7lqQHJtNEEPl7_0dUJGK7CGdxpmTB5A6Aj0n8NDCrhD9leZTnImFRkhMPcL3bDmqUoim6xCvBi4mozn6vepOJA6qlup_IhV7zYWVADbd6Mv2kaIzTI1UHkkCrzw3NGBuQddLv6sdLTb03HOQpW2L6icFkQWBj0-ZX0-PX7qALwtySKifCXPf8PivaXh9rnryHjGzu_VFwdJnEn7DhiT17j8dzFLi_vob8gG7DrsMaHxrxLsDmOnplWNLXHhAykwNdmynQifqkJJi_JDiz0-U1lV7IIbk_tuq4ij5Lcdw0Sdujk04XEfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5f0f13f6.mp4?token=blO9qKTYMlBgsy34FK_F-HNjNGNJQNCvC7lqQHJtNEEPl7_0dUJGK7CGdxpmTB5A6Aj0n8NDCrhD9leZTnImFRkhMPcL3bDmqUoim6xCvBi4mozn6vepOJA6qlup_IhV7zYWVADbd6Mv2kaIzTI1UHkkCrzw3NGBuQddLv6sdLTb03HOQpW2L6icFkQWBj0-ZX0-PX7qALwtySKifCXPf8PivaXh9rnryHjGzu_VFwdJnEn7DhiT17j8dzFLi_vob8gG7DrsMaHxrxLsDmOnplWNLXHhAykwNdmynQifqkJJi_JDiz0-U1lV7IIbk_tuq4ij5Lcdw0Sdujk04XEfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلیل اجرا نشدن طرح پزشک خانواده از زبان رئیس‌جمهور @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458734" target="_blank">📅 00:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458733">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6d2108a7.mp4?token=Qw3VSEQoy7p_VDm7scMKjdIhHfZC7gkECr1FavDIz7u5sqWvfe4dzpwtsEW2sNnx12v7hmR3NyuqB7tqpxpUkF7HCyYBGex7PjQPfdg-xgqO7z1sKymdyHBU0vSUjx1VbnaoOTTYa7eqMlbEYaqZa5F5JIH80IkWljDEBM8HvmU_KQxza2UceZEI3V3jLKaTr1qLfoqY9TEqJJ-6PhJDFsSUR-eo_VXGwqFSbqBKmrZzjQc7wbIGg88aaxQq-rWXTk8xRHbyJBoC534ViE4Gk1ChTP_gRD0faXw-oE9nhXQIXRCqjB9A-0vaD9PxKIbvgIuxI_87zvfsqKEdljhD90X652fQ82n-MaREtUmDN_swY1hMkoSI01cMi4gpt5vK-CjbM9IAhTJYcDbhP72cDgiqrhoXCduG3LDsNqAX1ZJByNDl6dBukPu27brpUSembfIq5edV3O6j-r1ZHUHTb5fitCZWx8VYroRFNox-qig4XPb9hK29RyOiueuf8XFxpgvcXog0PYrSy3iEbwTYNYBr9YRRnLY_Vm4UWUmGR_6xdrrsdLxTG1Mm9o5qVh9k6oemAZa5WwogJXms7H-xD525CyrXKjuBfFZcJi5xJwi2-hymyVRWFyVNSc7k8MD39txV_flaImjZt0TBwC06yEIV9UGcKJy9tTYC9TayA6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6d2108a7.mp4?token=Qw3VSEQoy7p_VDm7scMKjdIhHfZC7gkECr1FavDIz7u5sqWvfe4dzpwtsEW2sNnx12v7hmR3NyuqB7tqpxpUkF7HCyYBGex7PjQPfdg-xgqO7z1sKymdyHBU0vSUjx1VbnaoOTTYa7eqMlbEYaqZa5F5JIH80IkWljDEBM8HvmU_KQxza2UceZEI3V3jLKaTr1qLfoqY9TEqJJ-6PhJDFsSUR-eo_VXGwqFSbqBKmrZzjQc7wbIGg88aaxQq-rWXTk8xRHbyJBoC534ViE4Gk1ChTP_gRD0faXw-oE9nhXQIXRCqjB9A-0vaD9PxKIbvgIuxI_87zvfsqKEdljhD90X652fQ82n-MaREtUmDN_swY1hMkoSI01cMi4gpt5vK-CjbM9IAhTJYcDbhP72cDgiqrhoXCduG3LDsNqAX1ZJByNDl6dBukPu27brpUSembfIq5edV3O6j-r1ZHUHTb5fitCZWx8VYroRFNox-qig4XPb9hK29RyOiueuf8XFxpgvcXog0PYrSy3iEbwTYNYBr9YRRnLY_Vm4UWUmGR_6xdrrsdLxTG1Mm9o5qVh9k6oemAZa5WwogJXms7H-xD525CyrXKjuBfFZcJi5xJwi2-hymyVRWFyVNSc7k8MD39txV_flaImjZt0TBwC06yEIV9UGcKJy9tTYC9TayA6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید مدیران ناکارآمد شرکت‌ها را برکنار کنیم
🔹
برای مدیریت کشور به افراد کارآمد نیاز داریم، نه لزوماً رفقای خودمان. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458733" target="_blank">📅 00:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458732">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c231b724b.mp4?token=lHBNmRpGkCLJDvuxCIWcIfSv0Ehdpg3hgTNNyF3IonkCQsMMErkxDwPy8Ab5HK29IcfJswIvPYvtrKkdaoBr-2czVHvILQIvr1arv1gL1tL5JintjVcXqQV9Dk_NdtXdKGDog_nkfDaWzk1ZVhEh9OTejDyETkcy9IJU95KRfBX9mFUf8mT74CZ_C2OL_XVPCbVr6V0ms9SEPekh0OqXqeXLDFm6Hgw0qcMHWjHAE2QFPpM_TcvtvRyoWVYCTVL-5GAeTQw1Mc3g6avhHNZxn6vfK0k5umnPuXQiJmoCDU2ZrjS4q2VN8bul87jlxlSGiwgvZDboIHsWiCXYC3IKLwZsEnDWMf2Hm22jR1PvG1ORNxppMAUuabDb3pMc_dy5bTi-m9pWs_5p9yvOzh8Wv8aeXokpPIOk9boSStFIWsouqjiKpD4iNe0oPqYBNziFxxUu_P-8XC6GX1n4P21f_al8Zk73Qr_LIj5rQPivNDWLA5S_NTr4xManQZic0vbNLx_Y3t10IGw0LuuJ6mL_iYoQ1dDKXVL6pfCJfQznencmFCYUmPa4JhBWVvDQeWzZnLQsU64JqKADPfEGuMl5LcOPUP5fRLTV9l-ujbwO7TwVNHJHOvZXu9d5Pv8iJuDAYY_Ii8_t5Opsb4RCCbFkQjnsLSPm4LmjR8i2MqgXZ6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c231b724b.mp4?token=lHBNmRpGkCLJDvuxCIWcIfSv0Ehdpg3hgTNNyF3IonkCQsMMErkxDwPy8Ab5HK29IcfJswIvPYvtrKkdaoBr-2czVHvILQIvr1arv1gL1tL5JintjVcXqQV9Dk_NdtXdKGDog_nkfDaWzk1ZVhEh9OTejDyETkcy9IJU95KRfBX9mFUf8mT74CZ_C2OL_XVPCbVr6V0ms9SEPekh0OqXqeXLDFm6Hgw0qcMHWjHAE2QFPpM_TcvtvRyoWVYCTVL-5GAeTQw1Mc3g6avhHNZxn6vfK0k5umnPuXQiJmoCDU2ZrjS4q2VN8bul87jlxlSGiwgvZDboIHsWiCXYC3IKLwZsEnDWMf2Hm22jR1PvG1ORNxppMAUuabDb3pMc_dy5bTi-m9pWs_5p9yvOzh8Wv8aeXokpPIOk9boSStFIWsouqjiKpD4iNe0oPqYBNziFxxUu_P-8XC6GX1n4P21f_al8Zk73Qr_LIj5rQPivNDWLA5S_NTr4xManQZic0vbNLx_Y3t10IGw0LuuJ6mL_iYoQ1dDKXVL6pfCJfQznencmFCYUmPa4JhBWVvDQeWzZnLQsU64JqKADPfEGuMl5LcOPUP5fRLTV9l-ujbwO7TwVNHJHOvZXu9d5Pv8iJuDAYY_Ii8_t5Opsb4RCCbFkQjnsLSPm4LmjR8i2MqgXZ6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: به دنبال این هستیم که برخی از ادارات را دورکار کنیم
🔹
حقوق پرسنل را کم نمی‌کنیم اما مصرف سوخت و انرژی ما کاهش می‌یابد. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458732" target="_blank">📅 00:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b28c66f962.mp4?token=NH_svoSdJG_zGSf8K3gHP2c-nHkx8_UrE9nS55o3Qos9fb4J3fNXiMWk8Cg8BqwAHZAKRh2mnxkO85E0hOiR4n3ysyOX8uSddQPJDwFgVc2DIIA7id7ANk_XvJlsEmlpHFmXBbP2-Zh9mCBKQrW1HiPbtDRcDeyWpysXIJg_PV27tdJYecl-zP8BafpdJL0gE4k2cmlM3D-VPmls_2GW7IsvN5Yr5uAnq1OEUud9TGAHjH7Ze93HyCRatbpCRzgfFEeLzlqSXywOHVCOy9HuwUyDOpXfeQQGDwbTsNg6bLPXycDBDjxACTZ-B-rojoCA7QvuwYjHl1mpCM3VACNz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b28c66f962.mp4?token=NH_svoSdJG_zGSf8K3gHP2c-nHkx8_UrE9nS55o3Qos9fb4J3fNXiMWk8Cg8BqwAHZAKRh2mnxkO85E0hOiR4n3ysyOX8uSddQPJDwFgVc2DIIA7id7ANk_XvJlsEmlpHFmXBbP2-Zh9mCBKQrW1HiPbtDRcDeyWpysXIJg_PV27tdJYecl-zP8BafpdJL0gE4k2cmlM3D-VPmls_2GW7IsvN5Yr5uAnq1OEUud9TGAHjH7Ze93HyCRatbpCRzgfFEeLzlqSXywOHVCOy9HuwUyDOpXfeQQGDwbTsNg6bLPXycDBDjxACTZ-B-rojoCA7QvuwYjHl1mpCM3VACNz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: به جهان نشان دادیم که آمریکا و اسرائیل قادر به مقابله با موشک‌های ما نیستند
🔹
ما به خداوند متعال، مردم خود، توانمندی‌های داخلی و تسلیحاتی که با فناوری بومی توسعه داده‌ایم اتکا می‌کنیم؛ موشک‌هایی که آمریکا و رژیم صهیونیستی در مقابله با آنها ناتوان ماندند.…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458731" target="_blank">📅 00:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXVPyfZeruL2tjHFw5wCUrnOT86JRAM--jZ2tu0ahQIQY7DaTv1Z02iX2Z5bLxIC9FaR8vpPAGhw-AT96mY_RlmpsSIPqvEC0ET4JEmmXL1fFJq-dt9QOlWsUcmaUwHxbSqNyTl1hkqpuJqu0gDcgQJVkJGh8-qvMKhEzC46rmKev7oV_kIXmZlX7eUtkwmBkHJObKa9QyvRzGn94ZdbcBAwPTVAbNV_HKm3PBSpjAzRvHYytWDAcnV43CM_MeL1d5NWz_aGB-O-95VtLH99d3Ta1i9B8p2i9lieO5bBdqHmzbfRWOPIWmdLRuslcFMqwAy4yebTPY7KW9LDT7A8Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا قانون آفلاین است اما قانون‌شکنی آنلاین
🔹
روزبه‌روز بر تعداد برنامه‌هایی که در داخل کشور تولید و در فضای مجازی منتشر می‌شوند افزوده می‌شود؛ تولیداتی که گاه در محتوا، اجرا فاصله محسوسی با چارچوب‌های قانونی دارند و عمدتاً در فضای مجازی منتشر می‌شوند و گاه مرز میان سرگرمی و ابتذال را نیز کمرنگ می‌کنند.
🔹
مسئله فقط تولید و انتشار محتوای مجازی نیست. وقتی چنین فضایی بدون واکنش مؤثر ادامه پیدا می‌کند، برخی تولیدکنندگان حتی یک گام جلوتر رفته و همان الگو را به رویدادهای حضوری نیز تسری می‌دهند؛ گویی میان فضای رسمی و غیررسمی، مرزی برای اجرای قانون وجود ندارد.
🔗
سؤال اینجاست: آیا غیررسمی بودن بستر انتشار، می‌تواند به معنای معافیت از قانون باشد؟ از
اینجا
بخوانید.
@farsnart</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/458730" target="_blank">📅 00:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458729">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElUngpAwYoQrBxHe_YUoy4v_OpfDwdNJ-uiwp0njcsFO3wO0-tAiicWVcL9bEjbc81OISQ5klccTZV1pxoU-IN11J0uXCrZ5BMueK3ECvYWlX3qsQvnzH8R9vbDolW6m3SyxgnhiabK3RG9Y3tboNaGML2mQW3tJ9zGM388rjKvztAgnlzSXsEU7XxJMkfuGhxw9_0VcXLp7hrO2AuOtuAIzCWY1C1Bmab0zp1X_0TzQMEllz76h2-5F350NHJl5BNmty_iT9090VDuXocqq7V5fbfT10KYtdBsSfDOzPRCd_erg2Sa6tYH1tv2NI0Qgc02kq7NA2yox-lwygnq-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا پیشمرگه را هم رها کرد
🔹
شبکه بی‌بی‌سی به نقل از چهار منبع مطلع: دولت ترامپ در حال برنامه‌ریزی برای قطع کمک‌های نظامی به یکی از متحدان مهم آمریکا در خاورمیانه است؛ متحدی که اکنون هدف حملات گسترده ایران قرار گرفته است.
🔹
وزارت دفاع آمریکا در دیدارهای اخیر با مقام‌های اقلیم کردستان عراق اعلام کرده که دولت ترامپ قصد ندارد توافق امنیتی مربوط به ارائه کمک به نیروهای پیشمرگه کرد را که به‌زودی منقضی می‌شود، تمدید کند.
🔹
یروان سعید مدیر ابتکار جهانی کرد برای صلح، در دانشگاه آمریکایی گفته: آمریکا با قطع حمایت از کردها، آنها را رها می‌کند؛ کردهایی که برای کمک به آمریکایی‌ها در تحقق اهدافشان در عراق و خاورمیانه، هزینه و خون زیادی پرداختند.
🔸
مقام‌های کرد نگرانند که قطع این کمک‌ها به ایجاد خلأ امنیتی در اقلیم کردستان منجر شود و دست ایران را برای افزایش نفوذ در این منطقه بازتر کند. بر اساس این گزارش، از زمان آغاز جنگ آمریکا علیه ایران، تهران صدها موشک و پهپاد به سمت مناطق مختلف اقلیم کردستان عراق شلیک کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458729" target="_blank">📅 00:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458722">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZV7yspWu1RCaJffEWNB9BvMF7GgRwDf9voxcTAjuqiJGoR47v0T5YQaH5hvaFhu2UDB9uKXkGqzq9FIvm8oWDt_1vJ-UWDky5CicUhlUphDvgVWm0BvijgG3P8UQ4ms_lEVcbmy_CDO_VpL4hpij7ss37OYLW8KvqURkpe2IyFLyMaMpZjge31qbS-ur-fVngp8irAkWgQT_lsLie8TLqCUB-9ihGfxlV74zRmUu1FmskRixlh2c9XY1lklkCcZxEXFydGbfWXbPZMXNU0G8_PO5v1YtGXvcv3yi19aPSlj4ofnpso-b2_TNPW0K8XjcBSjeGb6GVLAUmTnMbvU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1omwHrSY2ERn21-kkE83ThkQB_zhCICuh53AgRI0uLaoPreReUse3QdynyxARNwD_1UNHtCkR3BuwCuziAqiKaQfIodMCAW_CuLBgXo42q0UixzBX01ronRxLUvCl_XqoXq5EgCzO_Mk2f4wU7LuoELtBmF_-xMvqsV_SMKpd_U76AcUUBFJeDbdG_0staLKvHNhc2ksZxLHZtAJ5d7PLA-mzUmJ--MUkUwmycP-sn002mriZEa_9mUr7pP39gqsHukhcCNH8bvNr3tRqDmdj0mSop0Y4cKSr11IgwuVBpx5GwFMR6fk3oGzEDEAG1vmj-NAO2-WSVpFHiBe4X3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOHe8Uk2CX3opvGibdvcjKe58ikGDuVAmX6IBTBDpZhSILX642yAM6KzbAiT55DLOGrrEFnwwUYQ7X-3pnVlkBi1-2z8keFuhfL3OEefmlZ8fsz6bgn9vZzf_OdaAc5oIafjzwPXdI4If2HfiBgrA9x-H8hPk7RU-WivPWOm4fxKJdbWDdIgbWcvd3kPDbBQiRPseq2RFRKY-PfGPgA9DwNJsAnlbwS5XU5bYVriai5ocuj2zocqyTZEFKFS51diHk7q7NpFcIAZ8SEEyzZZVULHXTeSyp6gwJQoI8EZ4Ye4zIHUxYlBx8uaiaaqGRuh3eUsWahliwmLGa0fXTiKPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gxD2YVvg1opbxZZa8yZ-2kMIYv2CFM7HbsV6Witbz5v9pm0iF0LvWNWp8QZA0cze0SWjU5jHzC33akmBZBfBylzBp_QD0Pjolil0_XJ9USPqFP5MDs7X10KVDVFMxZXVP14YAMO45JT_EGaHQac2KmjTtDdCyLT75LjNfLfOlQlNiA_eU8qdU-oOYqvFMpZ8e0t0zsmr0m3GMovM8FbSaGT-EZPOnVJu4D2ZiDAIP946kqhj4TaLw-WsyIEuQSHh0TsRuNcbqn9hQchH1Mq76RhWnlXQpRy4u78vYDmOjPfKjD44m2yyZaQXODkxUxwtkLO0l7nSdF9Hv5XmNMH0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7msgYk0j3jK_I6Ysa4wtmBlq22xrphCdS2WiHYH8-b9TWBMzztJfcSwTcR29AKVamBKrb0uy68ICKvF0CoTbhRlTSS1R1Ad3WPbkJfjeKZlgZswYZ2lVCuPbKWFV9ExC8q87U-EYuN98yiGqyJFvaAKgVRampF-6JRtxrs9XqwDNcl_bhVBz1XM71CGo_RqaexsxcPWMTU9S4zGd_qjqcnXN8sx9XyRZAaU8vZF_xjk9NWAGYeF8J3lj_XZLkrObYqsStF1jIRb8zqZEuJsZRsGO0wPnNOLTaZe6kr-pOKEur69ZsyiztZFkl9-toO-G7zBESgTdv6QO2K0wK36jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pw6cLL8-iqiVN26TRg5g0-SUCjojxznbMrnqxiVfLLBLfkuciZbd-vEOtQPNwR2RzjpvGwMUhgTej2RPXTH5D2qDukSpAb3RQzOcCcc707bA_7mrKmQ23cBrzRKhFdMlj76VQzysiCKPrkPeNKM-P7QodFDZttl2lB3UyEy3Ctglf7aXNEMMzJwZJCcU7bMtqLVjVAmfS0X9KXavVskaVa-PI95f7s1_JaIdnArHS1mKP_6ymXArtHAOJC34NxiHCBxdgBL0UbljxqhQQR5pZ3FouOw_Obb16wxnhRaY-Nr2Du1mMYy_0nPSQ7HKX3W7JGWiIOjXheeyQPc_UKSfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQzpqVqN0sLbCizp9gvpEXonSxMkxpZ-TmZaWJQ_OYnGIKXKi6WAF-sHCiHtJNm23Ii7zoADH_RBgCdHcD8pbiEX9eIYae8Rp6AONpPgAmjLTbNsMITNbD7CAa5X2OrzrYCPs3PVIiwm6djgbG_Me0Fh52V6iZSoGM9f15fZZsX1QffqlwPQsnqhXaxEOnNTkkjuTregEQrj2sd64mZTPcZJZa4KSYpP-t8t00R8-j8sxl29pbJG3wgILnVC5MA_SxPbELnGqP90lkwFqJat2Yjg_B3GcwI0GbMkJP_XzAVfl8t72xPJYJWI-Wz9WPHSuEX-ZbC3S4Oyc_U02xIYjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مهمانی امت احمد در سنندج
عکاس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458722" target="_blank">📅 00:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458721">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572fe77a52.mp4?token=uOtsUevPdjEOrC86YVnaknxIuXP_XMA7Jjk2sf-KRWlOMknBmv5OcypZR-mn4L7j634qhgaIr5JqiX_Qpyyh92Qjb1u_KKRrfmV3HKDSeRycfY966aHNG5h_fSagHhKLFXisWo7OM_Pj0Cmch1RZqmMI8PrKJC38pMiW9W_9M8LxKqYbqgItlDBOmFSUhFuU-W4_VcdSOk7vlQrzgOZdnQ-eiqMmgWwSyeihmt3DItBtNsDDmA7q69rMqmDpOqk4TLTzrkjuxP5fSDpW8hBf9BM01ZsBahBLrdVPcrDUV70AEAz9QzAjogqcafdhLEGgDXQkxIT3K7UCI8ilTISB9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572fe77a52.mp4?token=uOtsUevPdjEOrC86YVnaknxIuXP_XMA7Jjk2sf-KRWlOMknBmv5OcypZR-mn4L7j634qhgaIr5JqiX_Qpyyh92Qjb1u_KKRrfmV3HKDSeRycfY966aHNG5h_fSagHhKLFXisWo7OM_Pj0Cmch1RZqmMI8PrKJC38pMiW9W_9M8LxKqYbqgItlDBOmFSUhFuU-W4_VcdSOk7vlQrzgOZdnQ-eiqMmgWwSyeihmt3DItBtNsDDmA7q69rMqmDpOqk4TLTzrkjuxP5fSDpW8hBf9BM01ZsBahBLrdVPcrDUV70AEAz9QzAjogqcafdhLEGgDXQkxIT3K7UCI8ilTISB9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کالابرگ را برای برخی از دهک‌ها افزایش خواهیم داد
🔹
از اینکه نتوانستیم کالابرگ را افزایش دهیم، شرمندۀ مردم هستیم. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458721" target="_blank">📅 00:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458720">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f44195a3.mp4?token=niFQvyhDjmNhe1vvVhQpTQArTPccwBUDEYuEd8jReoi5q-8izNoAInF2VnuaTm5BlpwpGVyCeb8f7NFgmSwin9fb3z1aQFx4st03wrlYBUv0r8u6d2tQK4HSgfHyFdEdhGE3A2YRsag6olU296hfdO72NUnEGk672jHafjRdFElOGveNq6cnwxTjEHRYR_Lih6spRQ00Z-xYm5RmqofRa-cf2Hbz3_HiTYn44u1SHE9tnWPc9S0OIvDi77uGlmm7bfrUdmcR9N92wNtDVh1dVytT3S7q5jYw8mDaf8rlNl3EM483RT2D0B7n_rc9RCXFYSVTraeUxJW11U3Qwt8Z3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f44195a3.mp4?token=niFQvyhDjmNhe1vvVhQpTQArTPccwBUDEYuEd8jReoi5q-8izNoAInF2VnuaTm5BlpwpGVyCeb8f7NFgmSwin9fb3z1aQFx4st03wrlYBUv0r8u6d2tQK4HSgfHyFdEdhGE3A2YRsag6olU296hfdO72NUnEGk672jHafjRdFElOGveNq6cnwxTjEHRYR_Lih6spRQ00Z-xYm5RmqofRa-cf2Hbz3_HiTYn44u1SHE9tnWPc9S0OIvDi77uGlmm7bfrUdmcR9N92wNtDVh1dVytT3S7q5jYw8mDaf8rlNl3EM483RT2D0B7n_rc9RCXFYSVTraeUxJW11U3Qwt8Z3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر یک مقدار صرفه‌جویی کنیم، از بحران عبور می‌کنیم
🔹
برای زمستان به‌دنبال آن هستیم که گاز خانه‌ها قطع نشود اما مردم نیز باید مانند سال گذشته با کنترل مصرف انرژی ما را یاری کنند.
🔹
اولویت ما این است که چرخ صنعت بچرخد و تولید استمرار داشته باشد. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458720" target="_blank">📅 23:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458719">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTiFAb8WiPVrVOaodsODg8XiqVasp4i5QF4zUEe2qSEOEDxN_7HPL5PqI8XIvK51hElxlc3yoAA-bXXCeSaVf8tiFCEtT1fjWiQaUIdkQgvnXGq78wX4NQFtHjZcKBD-TS8NxKinwkyvbMJQvBCn4-Q4Jq4MDy6MVQmoG8BXdas8_DXHkHFMuRbY8vYPJzz-ZopKI-A53DxvLZMrVS67b35udDFHHB1TM3F8e2m-TL_1K5U7UTavTRZyNHYdKSwioMO1xaYYmaBf_dJD_DSecCwWpScdd-b3xC4QZGQP9yEtbkTX3XesCDxtHxU49eZtSqrYEgME1o-9RWQMiCZ6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: تاکیدات امروز رهبر معظم انقلاب روشن و غیرقابل تفسیر است‏
🔹
سرلشکر محسن رضایی: تأکید صریح رهبر معظم انقلاب بر پرهیز از «سخن ناامیدکننده»، «دوگانه‌سازی‌های موهوم» و اینکه «ارتکاب هرآنچه به ضرر انسجام اجتماعی باشد، ممنوع است»، برای همه یک راهبرد روشن و غیرقابل تفسیر است.
🔹
‏امروز وحدت ملی و انسجام اجتماعی یکی از بنیادی‌ترین مولفه‌های قدرت و امنیت ملی است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458719" target="_blank">📅 23:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458717">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JECFZ9FO_N_9N1miAVL_BNFCh2e3rlPwczcq6n_gwcHqpH27Y3UvVswlDa7fpeuqtOULLhZN8ky4LSawcK8Oinpz-kM7DBa8AJBHj87YdQ7TOyxnXyWqYvZVMjGV0MlDNcd0SyIsva1Ilcxs2cKqYOmDRvLpmUd6K0c9h69utaTFLWhkcH-IofKBxNvOPHnLC2IIqoOq_WDoqWPqtPRcPI7SOq5GOlJgdX9oQER95OdVfc_44IFKtWwLKcd7Juovkxmv0I80L1mda-fj5ft1gDnyP0wL9BIeNQlqPyI5wFjjrg8KHJh9YP3zhL1IiSd3073pMkONMOsuuZdGBuEHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نیروی دریایی سپاه: تسلط رزمندگان اسلام بر تنگۀ هرمز کاملا قاطع است
🔹
اظهارات مقامات آمریکایی در مورد باز بودن تنگۀ هرمز دروغی آشکار و تنها به قصد کنترل قیمت نفت و سرپوش گذاشتن بر شکست‌های خود می‌باشد‌.
🔹
تسلط رزمندگان اسلام بر این آبراه راهبردی کاملا قاطع است و با تمام قدرت و در کمال اقتدار تنگۀ هرمز بر روی تمامی کشتی‌هایی که بدون هماهنگی با جمهوری اسلامی ایران قصد تردد دارند مسدود است.
🔹
به ملت عزیز، شجاع و مبعوث شده ایران اسلامی اطمینان می‌دهیم این روند تا پایان شرارت‌های ارتش تروریستی آمریکا علیه کشور عزیزمان و اجرای تعهدات مقرر ادامه خواهد يافت.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/458717" target="_blank">📅 23:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458716">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea0fc875b.mp4?token=lYPwjFxWZA7aHDDbbmZN7zGsFTTGTKvojkMSPh6nE2QjBWWX-yld_-nFaDFy5gcW35dsE_Y7PyKds0AvczEaZUfSJl8BX4pQ2JV9qM7JX3BZCg546j97nRe2pitTcYridO42QMsPyJqydA-2aPVkAQpRV1a5rVqBiRs3JPN7Sfvw-wglrJGe2TEvCdd-YIe2pvdp4mmyy5fGQySvYewVWYpjOulEWTKlm2lyulXpGfymBbX5f8JCkZdr6KoO2nYh1d0EDh15TMjA52XYCQYWssguIp5zwUdP_B1gOmVLRhiDIX7w5xK1_drMjF7x4AlSHsGGO5bmI8aSJ_Ta7eP4lDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea0fc875b.mp4?token=lYPwjFxWZA7aHDDbbmZN7zGsFTTGTKvojkMSPh6nE2QjBWWX-yld_-nFaDFy5gcW35dsE_Y7PyKds0AvczEaZUfSJl8BX4pQ2JV9qM7JX3BZCg546j97nRe2pitTcYridO42QMsPyJqydA-2aPVkAQpRV1a5rVqBiRs3JPN7Sfvw-wglrJGe2TEvCdd-YIe2pvdp4mmyy5fGQySvYewVWYpjOulEWTKlm2lyulXpGfymBbX5f8JCkZdr6KoO2nYh1d0EDh15TMjA52XYCQYWssguIp5zwUdP_B1gOmVLRhiDIX7w5xK1_drMjF7x4AlSHsGGO5bmI8aSJ_Ta7eP4lDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: می‌توانیم با رفتار جهادی مشکلات‌مان را حل کنیم
🔹
کم‌شدن خاموشی‌ها با وجود اثرات جنگ، ناترازی و کمبود آب‌ در سدها، حاصل مدیریت بود. @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/458716" target="_blank">📅 23:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458715">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68193682c3.mp4?token=V1XwrqSOaK0RPpMDsS5ROQ8kpxnzYSnHUFL-ZU4stKhwlrf1JZ0lwz5T1cERW68r5zWoVzZFjVPUn0alPbCkAgsLu1HxyrCBIsDsR6cKfuiKWvS68fpUR-ng-r6B74Fp4qGkQJwdgv9gkGDSs6TrDlfTUymN46gvo7NCuuftBW69PhhdRshizt4yPsqK6E7kzvTsdTCCRoESq8m3_8zLFLxjJUV96PG9ZU12LYukEGQSaER1R137SYmzSefFyBOTlrXlkPBxtRVmtzCscPuNGKBbVdt_VT4kQFOcz32FxnIedxC_k5t7aA-MFfnc8Z8aamejWHWDB0MYfkx-UfU35w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68193682c3.mp4?token=V1XwrqSOaK0RPpMDsS5ROQ8kpxnzYSnHUFL-ZU4stKhwlrf1JZ0lwz5T1cERW68r5zWoVzZFjVPUn0alPbCkAgsLu1HxyrCBIsDsR6cKfuiKWvS68fpUR-ng-r6B74Fp4qGkQJwdgv9gkGDSs6TrDlfTUymN46gvo7NCuuftBW69PhhdRshizt4yPsqK6E7kzvTsdTCCRoESq8m3_8zLFLxjJUV96PG9ZU12LYukEGQSaER1R137SYmzSefFyBOTlrXlkPBxtRVmtzCscPuNGKBbVdt_VT4kQFOcz32FxnIedxC_k5t7aA-MFfnc8Z8aamejWHWDB0MYfkx-UfU35w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۱۸۱ مردم کرمان با عطر بیعت و رنگ انتقام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/458715" target="_blank">📅 23:47 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
