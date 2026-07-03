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
<img src="https://cdn4.telesco.pe/file/mgzIaRFKm8wMeUjTm1qxqOIdDl7drRjMsJ1QY1i0SDiPQbLQBrcKxOa7yosgVX8t-OjglsyddFXjcX-5qNom7TAkojOKXPF-U99Dd4891be_wStEpEK4A4ncoJp--WbdVQ4TVG20xRQh5GwkESlVEE47W0JGCLCNF42fVz2dgaK7YZPHJaJe-IDx0JD_EIplI7Oz3SPU9ASRAoqkGyR-dJxFKMcO-NUs-Gz40pZznnZTnQ8DSz1ROdwbAusq7iJU3J_YkbnxG1pDtOxk7Is0dAWv3VwBSTq83EpD3z5tYhpLXq0Ni9UCv7BR4pTh_GF1vAB5ewdmZdxtjy-jvl9OxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhisperInHeaven</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 01:28:00</div>
<hr>

<div class="tg-post" id="msg-1100">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=NINkl-i6kEkSWZgzaygwcTGmj8ixWuj_AtqTH79dcaZhP-8ZYmjI49xILmlympbIUHmsV4wtyiKZdDx5e8yRFyt7u4fUC8iY59ERub52ztRTU_vaDFjljH9vXUrlcRWSn-q8dPlKrX3epzOFwJji2mfIJKQBJKzFO2j4iUenMHbdagql_PVQy5iyNGd8nzX_TkHpMPw9uHF3Z8OISb672URKxAnTfvBzCcflI4OxA_ezmSWJf2Rn0OJHNMD3FJMJvkGcgCIz6XbKIMbiD18f9c5KF49Q03bi6OENwzftEDdLStN4wREwO1W3gaSeyl55nMGlvfCYT-zbQVtxIRcTEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=NINkl-i6kEkSWZgzaygwcTGmj8ixWuj_AtqTH79dcaZhP-8ZYmjI49xILmlympbIUHmsV4wtyiKZdDx5e8yRFyt7u4fUC8iY59ERub52ztRTU_vaDFjljH9vXUrlcRWSn-q8dPlKrX3epzOFwJji2mfIJKQBJKzFO2j4iUenMHbdagql_PVQy5iyNGd8nzX_TkHpMPw9uHF3Z8OISb672URKxAnTfvBzCcflI4OxA_ezmSWJf2Rn0OJHNMD3FJMJvkGcgCIz6XbKIMbiD18f9c5KF49Q03bi6OENwzftEDdLStN4wREwO1W3gaSeyl55nMGlvfCYT-zbQVtxIRcTEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://www.youtube.com/watch?v=Z069VNFAgAc
ایجاد بی‌نهایت آدرس ایمیل با یک دامنه روی کلودفلر
📧
آیا می‌دانستید می‌توانید با استفاده از قابلیت Email Routing در ، بی‌نهایت ایمیل شخصی‌سازی‌شده برای دامنه خود بسازید و همه آن‌ها را در یک صندوق دریافت مدیریت کنید؟
در این ویدیو، نحوه راه‌اندازی این سیستم کاربردی را یاد می‌گیرید که برای مدیریت بهتر ایمیل‌ها و جلوگیری از اسپم عالی است.
@whitedns</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/whitedns/1100" target="_blank">📅 17:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1099">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🛡
ویدیو آموزش استفاده از WhiteDNS Scanner
+
WhiteDNS VPN
https://youtu.be/N5hKuWXp37w
با استفاده از اسکنر WhiteDNS می‌تونید آی‌پی‌های تمیز و مناسب Cloudflare رو پیدا کنید، تست سرعت بگیرید، خروجی دقیق بگیرید و بعد از آی‌پی‌های سالم برای اتصال بهتر داخل اپ WhiteDNS VPN استفاده کنید.
در این آموزش یاد می‌گیرید:
- دانلود و نصب WhiteDNS Scanner
- اسکن IP و CIDR
- پیدا کردن IPهای تمیز Cloudflare
- تست سرعت و کیفیت آی‌پی‌ها
- استفاده از خروجی اسکنر
- دانلود و راه‌اندازی WhiteDNS VPN
- اتصال رایگان با گوشی موبایل
- انتخاب IP مناسب برای اتصال پایدارتر
📹
ویدیو
https://youtu.be/N5hKuWXp37w
📥
دانلود WhiteDNS Scanner
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.4
📱
دانلود اپ WhiteDNS VPN
https://t.me/whitedns/1072
📢
کانال تلگرام WhiteDNS
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/whitedns/1099" target="_blank">📅 15:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1098">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔭
برای دوستانی که می‌خوان سرور شخصی خودشون رو راه‌اندازی کنن، کیفیت VPSهای این سایت واقعاً خوبه:
https://yottasrc.com
چند نکته مهم:
* شماره و کشور ایران رو قبول می‌کنه
* پرداخت با ارز دیجیتال داره، روی شبکه‌های مختلف
* آی‌پی‌های سرورها کیفیت خیلی خوبی دارن
* پورت ۱۰ گیگابیت ارائه می‌ده، که برای سرعت و پایداری واقعاً مهمه
* لوکیشن‌های متنوعی هم داره
برای ساخت سرور شخصی، VPN، DNS یا تست‌های فنی، گزینه‌ی خیلی مناسبیه.
منبع
@WhiteDNS</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1098" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1097">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1097" target="_blank">📅 14:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1096">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsulhJ9FcBLbZAPTDbbzLAveXT3HWs3WxhuWasAlSh1CFqRXQZmDtGOq28GuEVX2LcDST9rK-Ujjb3pJ2mWPiXeV0424R3xbjillUo8A1re4OJExfq60t1qIoiJhVK-MmkUOBFsOrxaABo3xdZMpi1s-XaOvG8rXV2VoXTMoBy81paRsjsUmwpEz6Xd_0EHN0gRyvyZeT8mzLR7EXzGnMMhb8oSMCf-nSp1JN1u7AnL3G3n-dm91IXHkicwgtXT_2bhZrI4ZpQz7uEzxqqm9een9FDzjGzOzvR9jKmAsqg08UOXJxRN_G64ir6bhiMP6TpDSJh4RbFW2bd38JJWNyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1096" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1095">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1095" target="_blank">📅 05:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1094">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1094" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1093">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/whitedns/1093" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1088">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop  منتشر شد
👆
👆
👆
👆</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1088" target="_blank">📅 11:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1082">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1082" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/whitedns/1082" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1081">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adTqdo4jcTnUoEzEd8hgC2Q0_v_mWxXHtpxuCcOlz5nZNySSGLGXhvvUjn1tQUq7wazHcOB-FFLxfzg204sUbWMuiY--xxwJmHe2q8o3_E0Hi6crwggAoWXNRd2ESEWhjhYghCa1CGuao7vNNoXeHnMxdMnYPn4F2ORwy-FwFSXLheW-pyQp4JDPn0nmmGDdJnn-1Zm2Xm4VRd2A1DkGuxDCtx7LHuL5il07nqEHGbtX3HhvPos8oGvHgHnlrY7Zd2OzXs7Zzg-7UPSemgy4A8Vq1SOi3Pk7a5xHF9Vo1h0qZ4Las4tYz69zrGpDkMiOZzal_Hr5G_jhj1aVYMylrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/whitedns/1081" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1080">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1080" target="_blank">📅 04:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1079">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkeNrZgS7x9culPvgQs-HwNbyi3AyU5CMKvDDkGOYnUra7x8RDzCWkJqq5UW1NhEmBZ_z1D6XkUCkbf8QFhto5OmJZOHgFbdYE-rvZlePAyUUkCUp8HYPdXXGAFlovceKGxlyZNYf2BJS6o0K2iRyv5WkbpwWw0bsFomiyHggoo0yN19c_4WFcZfvni5kLGkZlKdPfyRqjS3cu8gAKPfGiq8HEMw5uxskTIGKY6nw5NT_ST0b0EfANjYp9h6pHErwKoKo1YmokCXzWYI1sgXpLUH3lDQZVaq2_vYkAmMRTDYPsndeB3bZqqCv7AEDwDOgvC3XgBaJSIC-eJGN9RMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
ورژن جدید WhiteDNS Desktop تقریبا آماده شده
در این ورژن همان وی‌پی‌ان داخل اپ اندروید
برای ویندوز، مک و لینوکس قابل دسترسی خواهد بود.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1079" target="_blank">📅 16:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1077">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/whitedns/1077" target="_blank">📅 03:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1076">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnMxzZ9KIiZdkekKJrz4IUoRA4ebXOaPAcVy220JukA5GuPSSjZ-Rr6qjAmdmn2HDXfDW7RW-ScYAsCZwlCKONS-cwoBp7KnPbfqcWGzDmd0NRu6g-uZbxLWYXyCuMHJu07VuWCFIBuLRQRKfiHRJ6GlLycEYdOwLgjRXDvce9eWOJy_gopSNJGZdwtJCIsddmmXCpDmxykL6mXd3dYzy-0AWjOoGTjG107rdlsukYOsy4Jo67HIcVpbrKdNoUDou0BaBxNpGjp1v5Yj3eKRSv3McrREo_A99fPda9WtCDaUYrbe2IKZHyZQdLVFJuQAWZA8GY_HpEchKJEVf7IAxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.4
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/whitedns/1076" target="_blank">📅 03:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1074">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1074" target="_blank">📅 17:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1073">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ie439pRPlktavYGswCKNS3wAuXG0oYmwa4dSud-BLJ-yIif3nO8Dks-HQv6UPVNUR7nRpT86MDzV9ckCPb_tznIydUaWwgq8FdtZ2hjYTgcPFrpK-sQbDeTpRy2sSUOJqOKKIuQ5gde9Agl_ZqwO14iODKsGaWGmW-V3lQIae1BThxtUKR3vUP-c47NqEY2IPbe8TQmZXOgpNFUX1wPl96YOTFl_DbvAepjVLVtBrQeUAZzdh25HmiM1RDk7zIA8jYtpn9rGLaZEjRmMChxtEErFC1yQZf7IwWf96KSUT_iCTUbhthUEYhEScjOHI-cf6DY5di36UnC1KgVGG9lXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شد
😎
۷۰۰ اتصال موفق در ۳۰دقیقه گذشته.
ممنون از همه دوستان که کمک ما تست کردند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1073" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1068">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1068" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/whitedns/1068" target="_blank">📅 15:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1062">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.6 منتشر شد
👆</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1062" target="_blank">📅 13:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1057">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1057" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/1057" target="_blank">📅 12:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1056">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPtbAh_chHUEFmBF5v-7mfS-6nAmQqwoOtJfUz8-_7_MnibFe7292ysgwY1kXmppnje-BlWzM4Jx3KGuYajgnVTai89PtnjpqDArANW5y0gv7R8vnH3BkPN0BwZ8mj2IF8p6Yzc_qtJ_BDgwIInn_Q7uDIbhHEXvh0ek57I728UX7zbWfIO5b1AaRJvOvZygkmp4Eqb9zQwiulos3tXAVQ78ykiCT-A9zwS67tdGkgRjecoS_BcyYEue-iWAdnkTW99dQ6K9lO2YTXirWYdqUjcBxlR3KWtta6zcVEEcURG4u8XucN3XcfZd0VBVBaAUfQIcjxkFvOrbogzBjkNrAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.6 منتشر شد
با مشکلاتی که دیروز برامون پیش اومد، فرصت این رو پیدا کردیم همزمان با درست کردن مشکل کردن اسکنر  ها، روی سرعت اتصال هارو هم بهتر کنیم و تا شاید کاربر های بیشتری بتونن بدوم IP Fronting وصل بشن.
🌈
در این ورژن، سرعت اتصال شما با اختلاف زیادی بهتر شده
🌈
اپ پایدار تر از همیشه هستش.
🌈
اپ از نظر ظاهری بهتر شده.
🌈
مشکل اتصال و نمایش کشور اشتباه حل شده.
نتیجه اتصال و سرعت خودتون رو زیر همین
پست بهمون بگید
ممنون از همراهی شما
@WhiteDNS</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1056" target="_blank">📅 12:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1055">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🛡
سلام به همه دوستان عزیز
بابت اختلالی که امروز توی سرویس WhiteDNS VPN پیش اومد واقعاً عذرخواهی می‌کنیم.
متأسفانه یه مشکل فنی برای سرورها ایجاد شده بود که باعث شد بعضی از اتصال‌ها درست کار نکنن. خوشبختانه مشکل برطرف شده و سرورها دوباره در دسترس هستن.
برای اینکه لیست جدید سرورها داخل اپ براتون آپدیت بشه، یکی از این کارها رو انجام بدید:
• یک‌بار دیتای اپ WhiteDNS VPN رو پاک کنید.
• یا اپ رو حذف و دوباره نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا اپ خودش تنظیمات جدید رو از سرور بگیره.
شاید سرعت کانکت شدن کمی پایینتر آمده باشد اما به زودی اون مورد هم حل میکنیم.
ممنون از صبوری و همراهی‌تون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1055" target="_blank">📅 08:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1054">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/whitedns/1054" target="_blank">📅 13:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1052">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یکی از اولین آدم‌هایی که از این پروژه حمایت کرد،
ویکی‌تجربه
بود. زمانی که اینجا فقط حدود ۱۰۰۰ نفر بودیم.
شاید خودشون هیچ‌وقت ندونن، ولی با به اشتراک گذاشتن پروژه، یکی از کسایی بودن که به ما انگیزه دادن ادامه بدم. بعضی وقتا یه حمایت کوچیک، بیشتر از چیزی که فکر می‌کنیم روی مسیر یه نفر تاثیر می‌ذاره.
خیلی وقته دیگه خبری ازشون نیست. حتی دیدم دامنه سایتشون هم تمدید نشده.
کار درست انجام دادن توی ایران سخته. درست موندن و باوجدان زندگی کردن هم سخت‌تر.
من حتی این عزیز رو از نزدیک نمی‌شناسم و اسم واقعیشون رو هم نمی‌دونم، ولی همیشه قدردان لطفشون بودم.
امیدوارم هرجا هستن، سالم باشن و حال دلشون خوب باشه.
🥲</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/whitedns/1052" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1051">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J6e4RaKlCjhvjLmBgYmHv37_ozriH9dFrazCd3o4FWpo8BbEi5CPs0npsO4OTs5rhfgPCacLM_1Xmm8TdX2I0R1smvPmQMvieqPLjp3r62pLEQIDFzC2QjIBA8VTdVMgo8x8PmsK4xf0Ky6kQ1CC8eTIP7zYtjX9qgSrWuQgbxtKUrekmo9xSJ9C4qONb0i1pY847yYKriCoPHD-DvhYWXJSeQlBkr1RLcZVS_NCdUL7IYpZlMzv9vFSWO_tjZdghne0VLjOT3Zx__NYY3rIW-TdAwINOcw7TjlSy5_vk0gtfzrOX36lzqMw9InQM9nS1_iLcK4UcOBgGxqYyCl4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1051" target="_blank">📅 16:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1050">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">↗️
تعداد کانکشن ها موفق WhiteDNS VPN به ۱۰،۰۰۰ کانکشن روزانه رسیده .
✍️
در حال حاظر تمرکز اصلی ما روی اضافه کردن وی‌پی‌ان به نسخه ورژن ویندوز، مک و لینوکس هستش.
✍️
مواردی گزارش DNS Leak توی کانکشن‌ها داشتیم. درحال آماده کردن سیستمی هستیم که علاوه بر تست‌های سرعت، امنیت و پایداری، تست DNS Leak  هم از کانفیگ ها گرفته بشه.
ممنون از همگی
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/whitedns/1050" target="_blank">📅 10:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1049">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-poll">
<h4>📊 به ورژن جدید  WhiteDNS VPN تونستید وصل بشید؟</h4>
<ul>
<li>✓ آره</li>
<li>✓ نه</li>
<li>✓ ویندوز یا IOS استفاده میکنم</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/whitedns/1049" target="_blank">📅 13:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1043">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/whitedns/1043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/whitedns/1043" target="_blank">📅 02:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1042">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/whitedns/1042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/whitedns/1042" target="_blank">📅 18:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1041">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/whitedns/1041" target="_blank">📅 18:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1039">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.5 منتشر شد
👆</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/whitedns/1039" target="_blank">📅 09:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1034">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.5-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1034" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/whitedns/1034" target="_blank">📅 08:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1033">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntnSC0X96CI8mrtpB_nIZLV5NYX09q1_WPGbIV-x3CY6gAhnFm3UDImIVlHZyHy8FNYx-tnMN6_eAi61Fozyllr7W10nf5EsOSIWShfP0OAuPS9vWFIOvkRvkwz1bFfRsmXOhv_CbgWim1BIbou47fJHcrrGrkFf2Mwj_QEFTcvQ5dyP9ZwSmrb85DSVJkktt6LFFDfNtRWCW6fDBfkhz64FUIMS2pjT6Bl3gui726PAF5JG8eeNeob_6rytGThyaXlLO89Yj4HsA2tRb0hD8XiuIcn5qjw1AwfMskBAaWDc3UKaogBCBYBVQ53onhKCKEumseYzHeK6EwbS0GGgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.5 منتشر شد
توی این نسخه چند تغییر مهم داشتیم تا اتصال راحت‌تر، سریع‌تر و قابل‌کنترل‌تر بشه:
• موتور اصلی اپ از XRay به Mihomo تغییر کرده
• تم دارک به اپ اضافه شده
• امکان اضافه کردن تا۵ آی‌پی تمی در بخش IP Fronting
• رفع مشکل «کانکت میشه ولی چیزی لود نمیکنه»
• اتصال سریع‌تر بعد از قطع شدن، با استفاده از کش
• اضافه شدن دکمه Refresh برای گرفتن کانکشن جدید و شاید بهتر
• نمایش سرعت دانلود و آپلود
• نمایش آی‌پی‌ای که در حال حاضر به آن متصل هستید
اگر برای اتصال مشکل دارید، احتمالاً باید برای خودتون آی‌پی تمیز اسکن کنید و داخل بخش IP Fronting قرار بدید.
تیم ما همچنان در حال تست و بهتر کردن اپه تا اتصال پایدارتر و ساده‌تری داشته باشید.
ممنون که همراه WhiteDNS هستید
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/whitedns/1033" target="_blank">📅 08:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1032">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان
👋
بچه‌های تیم به صورت مداوم در حال اسکن و بررسی IPها هستن تا همیشه بهترین و تمیزترین IPها داخل اپ در دسترس باشه و شما کمتر درگیر اسکن کردن و پیدا کردن کانفیگ مناسب بشید.
هدف ما اینه که تا جای ممکن فقط اپ رو باز کنید، یک دکمه بزنید و متصل بشید.
اگر فکر می‌کنید قابلیت یا امکانی هست که می‌تونه تجربه استفاده از اپ رو بهتر کنه، حتماً زیر همین پست برامون بنویسید. اگر با مسیر و هدف کلی اپ هم‌خوانی داشته باشه، با کمال میل بررسی و به لیست توسعه اضافه می‌کنیم.
ممنون از همراهی همیشگی شما
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/whitedns/1032" target="_blank">📅 13:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1031">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1031" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1030">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/whitedns/1030" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1029">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/whitedns/1029" target="_blank">📅 13:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1027">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/whitedns/1027" target="_blank">📅 15:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1022">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/whitedns/1022" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/whitedns/1022" target="_blank">📅 15:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1021">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyUtav93X3SCQBprZsQoRrq-jNJoCwjQvrc2MiUxW0oxXHCwSs1-3wc9BhSM3IHCMckGGzAyc9pug-5bnOqfvfNSgEdXLEOzaZNtMQJ_ocZet7BQ4oC0sEHuONOEnSgg89n-9s4g9xKmDCHvscS7xk5mp2u1vNrhhkNEiOTr0K_pIUkDJYCxCD30eKlGmWczsvSe3GWbuRlvTx1wVBXYYiQfuOu0wcN9NrhiUDWiBhU93mTBWyYzTD71KKWw70OHkvfstUp-afjfeF_QBFyqzjwsnJUepUPCWVNHgDDcbXXxi4Mu1KvUuPnJLSVdCIqvmDheB1khhL1c_TGIvzW2-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/whitedns/1021" target="_blank">📅 15:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1020">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/whitedns/1020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/1020" target="_blank">📅 14:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1019">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VklT88RJoe6yQ4Fcc1tDrjMUWXGaHo4fSXgskT-zq3KFNMUeIQL6s008-dVpgm8X3nWWSFay8iVuCciJNTfykAETjmuqf53_lsZgd87xQg01fRUO8iGdVQRfQN-AExMOOnxuWTRMoW0cjDFWva4PovL10O15S8pXmFJ2IVL4Wpn42MML_KHtxUQ4nBku3pc8dl5fiTqKiR5he8KO3_Um2uJCBzZ5o9_U7D5mo2Vt26QE4Mc0ZoWWnXLmdPznypd-sIG9A-hvHlNPPm87OjU2N_Ufm_Bj10izKkZ5SrLXN88b92kRq8uZv5XcSLGl_yN7qQ5nsT_FScmiY0u08n41cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/whitedns/1019" target="_blank">📅 14:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1018">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-1.2.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/whitedns/1018" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌎
آپدیت جدید WhiteDNS BPB V1.2.0
در این نسخه مشکل ورود با Cloudflare برای بعضی کاربران رفع شد.
قبلا بعد از انتخاب WhiteDNS BPB در مرحله برگشت از مرورگر، گاهی برنامه پیام خطا می‌داد که کد ورود آماده نیست.
از این نسخه، برنامه لینک برگشت Cloudflare را نگه می‌دارد و بعد از تمام شدن بررسی قبلی، ورود را درست کامل می‌کند.
✍️
نتیجه:
ورود با Cloudflare پایدارتر شده و احتمال خطای برگشت از مرورگر خیلی کمتر است.
روش استفاده تغییری نکرده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/whitedns/1018" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1017">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخدماتی حامد📱</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آموزش (1).mp4</div>
  <div class="tg-doc-extra">15.1 MB</div>
</div>
<a href="https://t.me/whitedns/1017" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش ساخت پنل BPB بوسیله برنامه
WhiteDNS BPB
😎
😎
😎
ارسالی ادمین am
❤️
برنامه نصبی مورد نیاز
👉
سلام برای ساخت پنل به این نکات دقت نمایید قبل از ساخت پنل شما به یک اکانت کلادفلر که تایید شده باشه نیاز دارید.
بعد از انجام آن وارد برنامه white dns bpb بشید به بخش dasburd  برید .
گزینه connect cladflarرا بزنید تا گزینه sing in cladflarنمایش داده بشود روی اون ضربه بزنید تا صفحه مرورگر داخلی گوشی باز بشود در نهایت با زدن گزینه ابی رنگ  در تصویر اکانت ایجاد می گردد .
بعد از اون دو گزینه نمایش داده میشه که شما باید برنامه white dns bpb رو انتخاب کنید سپس به تب bpb deployment برید و گزینه  create  رو بزنید تا پنل ایجاد بشه یک نکته دیگر که مهم هست .
اگر در حالت عادی به ارور برخورد کردید با یک vpn روشن وارد پنل بشید یا نت خودتان رو تغییر بدهید تا به پنل وارد شوید باقی مواردش مانند پنل bpb می باشد .
در صورتی که خواستید می توانید ایپی تمیز برای پنل خودتان قرار بدهید و از آن در کلاینت های خودتان استفاده نمایید.
@whitedns
❤️
اشتراک گذاری یادتون نره
🌈
‌‌
@hamedvpns
☑️
لایک   |   Like
👍
❤️
اشتراک بزارین   |   Share
⭐</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/whitedns/1017" target="_blank">📅 03:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1016">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/whitedns/1016" target="_blank">📅 05:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1015">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 66K · <a href="https://t.me/whitedns/1015" target="_blank">📅 04:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1005">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">برای این ساب، ما هر ۳۰ دقیقه بیشتر از ۲۵۰هزار کانفیگ رو بهشون وصل میشیم، تست دسترسی، امنیت و سرعت میگیریم و بهترین هاشون رو تو ساب قرار میدیم. که خروجی بین ۲۰۰ تا ۵۰۰ کانفیگ میشه.
تمام این کانفیگ ها قابلیت این رو دارند که از Cloudflare IP هم براشون استفاده کنید.
بروزرسانی فقط برای این ساب جدید نیست. تمام آدرس های قبلی هم بروز میشن و همین محتوی رو دارند.
اگر ساب براتون اررور میده، احتمالا آدرسش رو فیلتر کردند. اولین بار با وی‌پی‌ان ساب رو وارد کنید.
ممنون</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/whitedns/1005" target="_blank">📅 10:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1004">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستان عزیز WhiteDNS
🤍
ساب جدید WhiteDNS برای اپلیکیشن‌های مختلف آماده است.
برای اپ‌های زیر از این لینک استفاده کنید:
💠
ClashMi, Clash Party, FlClash, Karing
https://sub.whitedns.shop/sub/mihomo.yaml
💠
V2Box, V2Ray, WhiteDNS Desktop App ....
https://sub.whitedns.shop/sub/base64.txt
آموزش استفاده از Clash Party را هم می‌توانید از این ویدیو ببینید:
https://www.youtube.com/watch?v=gMFH88yRghg
این ساب شامل حدود ۵۰۰ کانفیگ پرسرعت Cloudflare Proxy شده است که به‌صورت مداوم بررسی و به‌روزرسانی می‌شوند.
پیشنهاد ما این است که اگر از اپ‌های Clash-based مثل Clash Party، FlClash، ClashMi یا Karing استفاده می‌کنید، حتماً لینک Mihomo را اضافه کنید تا بهترین نتیجه را بگیرید.
@WhiteDNS
برای اینترنت آزادتر، پایدارتر و قابل‌استفاده‌تر
🤍</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/whitedns/1004" target="_blank">📅 05:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1003">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kDm-JBz7Mz55Nr7cqORbMpTmHIi1Rcbw6SjJIyfQfEOVTtr2-jZ9beeOG4ogkwSC_mpF9y8hmunVrLsvkwkGPHaRf64KK3g-B_HGetbr13teRrH9J1ZGlqmLKog4dA04SYqMsQXE5-wYVIDBYqHOKcr9gkdLLX0HyL9VqdlQjAMJiFfAs1rQ8x1dfLX2GpD5x3nyfqjdPfnEQBNf0RG0Ntj_OYfHpi3QT__AjAEwyoiJ5hGHwhp7wbU50YB_d5I1IKmXv1OIDxMLroWyrkVKkl8z0WH55u-g0v27vVIMz3xMLUQ8r4Yx1OHlOygJtwq6DOQUfpfPCkIVySIfi5evFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما با این مدل افراد به نظرتون باید چیکار کنیم ؟</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/whitedns/1003" target="_blank">📅 19:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1002">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آموزش کوتاه استفاده از :   WhiteDns BPB  1.1.0
📱
📡
@whitedns
🔗
✨</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/whitedns/1002" target="_blank">📅 15:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1001">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">White DNS
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1001" target="_blank">📅 14:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1000">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1000" target="_blank">📅 14:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-999">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/2df17bf874.mp4?token=hBNaEhbjKFQHdT1FE8jP6xSTviCm2AxkcI86s4dfi5bY6_euedr-8wc8haVCPhiCzNm-80h-uAA2ASQKhSNCuQRVr_Px8upjW0hDio9kCVjoIWq_x3xQnkuC-Q1YwFbRdn_Y_zgtO3QH6y99CTQ2o4L6bW0bn_E2H2Yr6Vq8cMGVuaTc1Neak_za9v1C5inRkkhypzyaOeFY-FKKnhRpqsJ3WmlcnEsucbledbN4BxpmlKy-XHaKD5j4USy73v0mcYBkX5YF6nHSmNxCpvbFMPDJ1oT1b3V-qmdJ9qrPx9AYvT0CsVae6t9ldaX-SbbI096YDE9k8wYa5As9DWoJKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/2df17bf874.mp4?token=hBNaEhbjKFQHdT1FE8jP6xSTviCm2AxkcI86s4dfi5bY6_euedr-8wc8haVCPhiCzNm-80h-uAA2ASQKhSNCuQRVr_Px8upjW0hDio9kCVjoIWq_x3xQnkuC-Q1YwFbRdn_Y_zgtO3QH6y99CTQ2o4L6bW0bn_E2H2Yr6Vq8cMGVuaTc1Neak_za9v1C5inRkkhypzyaOeFY-FKKnhRpqsJ3WmlcnEsucbledbN4BxpmlKy-XHaKD5j4USy73v0mcYBkX5YF6nHSmNxCpvbFMPDJ1oT1b3V-qmdJ9qrPx9AYvT0CsVae6t9ldaX-SbbI096YDE9k8wYa5As9DWoJKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡
@whitedns
🔗
✨</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/whitedns/999" target="_blank">📅 14:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-997">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">WhiteDNS-BPB-v1.1.0.apk</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/whitedns/997" target="_blank">📅 13:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-996">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/whitedns/996" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه ۱.۱.۰ اپلیکیشن WhiteDNS BPB
در این نسخه مشکل وارد شدن به
پنل  Cloudflare برای دوستانی که ارور داشتند حل شده.
پست اول هم آپدریت شد به این ورژن. پس اگر اول لود رو دانلود کردید دیگه نگران این ورژن نباشید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/whitedns/996" target="_blank">📅 13:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-995">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوستان سلام :
تذکر !
مشکلات سخت افزاری و نرم افزاری گوشی شما فقط و و فقط توسط خودتون باید رفع بشه ، چون ما نمی‌تونیم کاری بکنیم ، مطمئن بشید گوشی شما آپدیت هست و مشکلات نرم افزاری و سخت افزاری ندارد
موارد زیر را حتما برای whitedns bpb رعایت کنید
۱.مرورگر دیفالت گوشی را روی فایرفاکس(که پیشنهاد ما هست ) تنظیم کنید و از مرورگرهای ناشناخته گوشی های مخصوصا چینی استفاده نکنید ،چون بسیاری از این مرورگرها مشکلات امنیتی داره و وبسایت های معتبر مثل کلادفلر به درستی اجازه دسترسی به اونها نمیده
۲.فایرفاکس را باز کنید ، توی کلادفلر login کنید ،
نکته : ایمیل شما حتما باید وریفای شده باشد
۳.حالا وارد اپلیکیشن whitedns bpb بشید و شروع به نصب پنل کنید و ادامه ماجرا ....
در صورتی که به خطا برخوردید اپلیکیشن را uninstall کنید و مراحل بالا را از اول انجام بدید
ارادت
تیم whitedns</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/995" target="_blank">📅 13:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-994">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/whitedns/994" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 73K · <a href="https://t.me/whitedns/994" target="_blank">📅 12:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-992">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4UHniSBWTTMcbrZpTEh7Jh2kl6nPtpNZUCQlNrfJbs1q9mLbrlNqoOY49EUPNJiXEIY1YVqYUcbLUQIdhc-LrxIAjQPHNL1hn4rQp6qo9Aw_2NstTTcsuB39xpkeEQic_UHv8MXqlITWp1a_a3OfDV13s6eKP0-9qKFoL5Yk10MpZpPBV07sNH7ly1nEsqMbV0GjFEUgalgcWkLhw8xdZax8MU8fS55hmJ-Sj2WXTD8yXD07Bk9AEagPIDdVdcS3YKEXa7TaGS55ixF4hGVxPzAN9IkXd5mN1MEm3GetyQoR55ZQhEE2l8yhUduGroR0TMjas103-HAHPW-Tvv3Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/whitedns/992" target="_blank">📅 12:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-991">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">در حال حاضر بیش از ۵ هزار نفر به صورت رایگان از WhiteDNS VPN استفاده می‌کنند و به اینترنت متصل هستند.
شاید این عدد در نگاه اول خیلی بزرگ به نظر نرسد، اما برای ما ارزش فوق‌العاده‌ای دارد. هر کدام از این اتصال‌ها یعنی یک نفر توانسته راحت‌تر و رایگان به اینترنت دسترسی داشته باشد.
از تمام کسانی که در این مسیر کنار ما بودند، تست کردند، باگ گزارش دادند و از پروژه حمایت کردند صمیمانه تشکر می‌کنیم.
❤️
دم همگی گرم</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/whitedns/991" target="_blank">📅 18:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-990">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugr0hWjQClIGPw4rb0UKB-ZdouEQjOrKy6J9d3xYhEOo0DU76fn_gDKeJU1fMAFpEHbR0ozkAElN3kPf8cO1X7NAO4q47KKnTRHB1duExKgu9g2CLZ1wpr7qvuwLr63NETLXFu5Unw0eVRz1HsdpYwB8xFHakqpYBn-zM-QRZ5CP3BYdJ873uUk-zGdJh4ZeCwv12eMiVW8eo5JqmuTRX_fUN3DVfPZOROMqMC4OT7E0OkNpL50zItaYlfd4l53T8pnZZHiJyA6O--BiCjx2yGwFIZnAygQrCeEDECgKvz3HU3wIg-E8YiCCNFAOtg8K4Rt9HLPijuXbVO4Uy99Rew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
در حال انجام تست‌های نهایی WhiteDNS BPB هستیم.
این همان نسخه‌ای است که در تست‌های اولیه بازخوردهای فوق‌العاده‌ای از کاربران دریافت کرد و برای بسیاری از افراد عملکرد بسیار خوبی داشت.
به دلیل محدودیت‌ها و قوانین Cloudflare، امکان ارائه عمومی این سرویس به شکل ساده و مستقیم برای همه کاربران وجود نداشت. اما حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.
نگران پیچیدگی راه‌اندازی هم نباشید؛ همه چیز تا جای ممکن ساده شده و آموزش ویدیویی کامل نیز داخل خود اپلیکیشن در دسترس خواهد بود.
منتظر انتشار نسخه عمومی باشید.
🔥</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/whitedns/990" target="_blank">📅 18:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-989">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ما از روز اول قطعی اینترنت فقط شنیدیم
《اینستاگرام لود میشه؟!》یا《اینستاگرام لود نمیشه؟!》 یا 《اینستاگرام لود شد》
🤣
تنها معیار و ملاک سرعت لود اینستاگرام بده
🫠</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/whitedns/989" target="_blank">📅 13:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/whitedns/984" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/whitedns/984" target="_blank">📅 09:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnpdKt_ksJPCXsAXkGZU2UAvyWS2aBJY6Z5dtDY9p0DarjqomYdUVtO2Zu-pjSexQ8v5cJyRlkl9ZA6_L_tS86PALsAV6NHvWdX13m_W_30fRWOALlGyJZlDVHAl1M8cjTY3Ka2lvgkVPYz_jCe-7UMuaWDWwpBYcRwSSZazErbvCB71geJ23atYj7oK7ZrGimnStY1OKqlEJUVcjKEvqmzJ-zEHI_w7EPE2x6LyTT5XX7exRx07rLgwQJTBtrxcUvfI5HZF3_77PnMQs7ExqYa0PQcZMPkiwPIAU72vOf-m3WoF6MQOqT1p5cWvm_ixDbqVCpzGD4GCnNdBlDJUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-dSq2AHYt4ValWrcDE7dBGjuTk30HHy1l9fprQOBKGIkSo5fZ3Uqvs4qqWxTnEEdUZ7dV0kkktylsZ3l_ZdK5F5YEYbLBtnEIP21HOhR-_klNbHr4RrA456hucNOXZDkASC0yQpVKQBLjICrzHp12QtaVQvkeJon4sxlt5hZNb-U4ngUBnEmbHOFu1d1LdaE43dyRLpzcAz-1Eo8Zst7FbrsGCycxCI1bOVKUHg0uIUes-1n50e_5rtsqsr5Ied1iT9K9MoW2a0Lb8g3tyT3zPcdU-kKSOJYVXX_3r_WTZMhyLBQ_Q40_YIirpsSxykFZiho_i58Hr20Weqegtqhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYs-4QIYiISugpJ6uG0bstyhsPKrFKEeibrFdIszRt3xFM5vH8igAZMjkMvZ2JWUMKgylrieluSUgBO8_9u0kyIYKS371gDzfMOY4UD-x6tCWo6WeFIyCzthUGRDuxPAB7yGZNNuJztTjY94vwqYmPIDK4lycejT7Dn37HrAahxM8ihLpJcre0VhQEEMBJafIsscoyOQjCzTsAGmwunc_yJZ1wkAmQ4Fx_njbP3GxZo7N5IJnxQu2L-921DH6DAq4ez8THW8XQrNbf0kZvD8mma1XJbzHBHZYo4o3zP-nfAUeLAy31h7xBoHp6DynbaKmr8d8JUjpNzhTsZP_6en9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎉
نسخه 0.0.3 اپلیکیشن WhiteDNS VPN منتشر شد
در این نسخه چند قابلیت مهم به اپلیکیشن اضافه شده است:
✅
انتخاب لوکیشن برای اتصال
✅
انتخاب اپلیکیشن‌هایی که باید از VPN استفاده کنند. Split Tunneling
برای بهترین عملکرد، پیشنهاد می‌کنیم هنگام اتصال از گزینه Auto استفاده کنید. در این حالت اپلیکیشن به‌صورت هوشمند بهترین لوکیشن را بر اساس شرایط شبکه شما انتخاب می‌کند تا اتصال پایدارتر و سریع‌تری داشته باشید.
از همراهی و بازخوردهای ارزشمند شما ممنونیم
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/whitedns/981" target="_blank">📅 09:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-980">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">داریم روی یک اپ جدید کار میکنیم به اسم WhiteDNS BPB که پروسه ساخت، مدیریت و وصل شدن به کانفیگ های BPB رو برای شما ها راحت تر می‌کنه
🔥</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/whitedns/980" target="_blank">📅 15:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-979">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-poll">
<h4>📊 آیا به نسخه جدید WhiteDNS VPN وصل شدید؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
<li>✓ آیفون/دستکتاپ دارم.</li>
</ul>
</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/whitedns/979" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">لطفا تست کنید، نتیجه اتصال یا شاید تست سرعت خودتون رو برای ما زیر همین پست بفرستید.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/whitedns/978" target="_blank">📅 12:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-973">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/whitedns/973" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/whitedns/973" target="_blank">📅 12:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-972">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">همچنین در مورد اپلیکیشن WhiteDNS VPN، باید بگوییم که در حال حاضر تمام تمرکز تیم ما روی توسعه و آماده‌سازی این سرویس قرار دارد.
در طول ماه‌های گذشته، با کمک گزارش‌ها، بازخوردها و تست‌های ارزشمند شما، توانسته‌ایم به یک معماری پایدار و مقیاس‌پذیر برای این پروژه دست پیدا کنیم. این تجربه به ما کمک کرده تا نیازهای واقعی کاربران ایرانی را بهتر بشناسیم و راهکارهای مؤثرتری برای آن‌ها طراحی کنیم.
هدف ما تنها ساخت یک VPN دیگر نیست؛ بلکه تلاش می‌کنیم سرویسی را ارائه دهیم که از ابتدا با در نظر گرفتن شرایط اینترنت ایران، پایداری، سادگی استفاده و تجربه کاربری مناسب طراحی شده باشد.
همچنین تمامی سرویس‌های مبتنی بر DNS ما در حال حاضر در وضعیت پایدار و آماده‌به‌کار قرار دارند تا در صورت بروز اختلالات گسترده یا محدودیت‌های اینترنتی، بتوانیم در کوتاه‌ترین زمان ممکن مجدداً این سرویس‌ها را در اختیار کاربران قرار دهیم.
از همراهی، صبوری و حمایت شما سپاسگزاریم.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/whitedns/972" target="_blank">📅 08:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-971">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سلام خدمت همراهان عزیز
🌹
ساب‌های WhiteDNS شامل باکیفیت‌ترین کانفیگ‌های عمومی هستند که در سطح اینترنت منتشر شده‌اند. تیم ما هر ۳۰ دقیقه یک‌بار بیش از ۲۵۰ هزار کانفیگ را مجدداً بررسی می‌کند، از آن‌ها تست سرعت و پایداری می‌گیرد و در نهایت تنها حدود ۲۰۰ کانفیگ برتر را در اختیار کاربران قرار می‌دهد.
با این حال، لطفاً در نظر داشته باشید که تمامی این کانفیگ‌ها عمومی هستند و توسط WhiteDNS میزبانی نمی‌شوند. ما تلاش می‌کنیم کانفیگ‌های انتخاب‌شده از نظر کیفیت، پایداری و امنیت در بهترین وضعیت ممکن باشند، اما هیچ‌گونه تضمینی در خصوص زیرساخت، عملکرد سرورهای میزبان این کانفیگ‌ها وجود ندارد.
هدف ما ارائه بهترین گزینه‌های عمومی موجود و کمک به دسترسی آزاد به اینترنت برای کاربران است.
با احترام
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/971" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-970">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستان عزیز، ممنون از گزارش هاتون.
لینک ساب که از دسترس خارج شده بود درست شده و میتونید ازش دوباره استفاده کنید.
https://sub.whitedns.one/sub/mihomo.yaml
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/970" target="_blank">📅 08:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-969">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzWF4FwiwsquQZWT1fmbTl0Ju354sP2pVNMGgYcyqAIfZ1zgQ6Mjpo4Y0MGOe_TAjPH0AsN8Qtmy4VyY4SsuG9SbQB9zeiz22PPZI6q_KGMBiOeoWEdQOzV8tTdl4ltI_kA0rRW0PkDDBS0nd92XgR-gLhNxKHwV2jtiWn-vpdJ-90vXk82A0OE5x7gprxLa7X9WFVcAA9GNeRTqjdasd0Qckw3uApvVNPKYtdC_aCB4NLSqm9bsUW_4VxFSXE0OAVx48LNxhs-QchbOzuI0DKwbN2pt7LLSRNoX6gRGZmWuGLLSPFNPCrRNowCtNheF57I-6LILYDHxcGg_CM_sBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/969" target="_blank">📅 04:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-968">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiFI7BgkV1X5lEpBrfM89qVHb9ah6WVP67fyNHpcxv1YGJzYyiNeB14SrlTFq1YRevwXRYHh6qYgaQHQxfKbIp41CWRibPCwlO5epc6479_ZzM_q95VOKxfZ03AZ6o1MNFOkXtnKLCvoCbzncToAuCQifTalbS1Iq-1bAHN9CBu-JaIJrQ1HM29ihe3qUA8zs3otFpPp7LDHh-qR5aY7fbOaMIFxcNGbp3T6P25YaTR3BQkYRxEP89da0Xr4TLOhl-Mjz9gnLVOeyv4in2lAmisUT54l81OogbXtFUk_fzw29j4xSemZul05iLVd-mXIizs1q2YNxnPwItMe-vmHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/whitedns/968" target="_blank">📅 13:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-967">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این دومین نسخه تست همگانی اپلیکیشن WhiteDNS VPN میباشد.
لطفا تجربه، سرعت و مشکلات خودتون رو زیر این پست برای ما بفرستید.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/whitedns/967" target="_blank">📅 13:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-963">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-vpn-arm64-v8a-v.0.0.1.apk</div>
  <div class="tg-doc-extra">30 MB</div>
</div>
<a href="https://t.me/whitedns/963" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
نسخه جدید اپ آماده شده
در این ورژن شاید اتصال شما کمی کندتر انجام شود.
ما در حال تلاش هستیم تا در ورژن های بعدی سرویس بهتری ارایه کنیم.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/whitedns/963" target="_blank">📅 13:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-962">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ما راه حل رو داریم، اپ مناسب رو هم ساختیم. حالا فقط باید باهم تست کنیم تا به نتیجه نهایی برسیم.
به زودی ورژن جدید رو منتشر خواهیم کرد
❤️
ممنون از همراهی شما</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/whitedns/962" target="_blank">📅 09:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-961">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">همراهان عزیز سلام
ممنون از تست شما. همونطور که بهتون گفتم این ورژن نسخه تست هستش و ما در حال حاضر به یک مشکل فنی برخوردیم.
به زودی اپ را آپدیت میکنیم.
ممنون از همکاری و گزارش های شما.</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/whitedns/961" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-960">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چنل یوتیوب مارو سابسکرایب کنید که یکسری آموزش هارو از این به بعد اونجا به اشتراک میگذاریم
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/whitedns/960" target="_blank">📅 08:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-959">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این اولین ورژن اپ وی‌پی‌ان WhiteDNS هستش.
در ورژن های بعدی تغییرات بیشتری ایجاد خواهد شد اما سادگی اپ به همین شکل خواهد ماند.
پشت این سادگی پیچیدگی و تست های زیادی درحال انجام شدن هستش که همه پشت داکمه ساده اتصال پنهان شده.
لطفا توجه داشته باشید که در این ورژن شما محدودیت روزی ۱گیگابات استفاده را دارید.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/whitedns/959" target="_blank">📅 07:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-958">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">لطفا هر موفقیت در اتصال،‌ مشکل و یا نظری رو با ما به اشتراک بگذارید.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/whitedns/958" target="_blank">📅 07:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-954">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-vpn-arm64-v8a.apk</div>
  <div class="tg-doc-extra">30 MB</div>
</div>
<a href="https://t.me/whitedns/954" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/whitedns/954" target="_blank">📅 07:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-953">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3gNdx34TCMib5ak7fR0PepOY8hTmEwiDL-AEZuWNOvW3VHzy6PwdBdCkkr689VOP9bLOEPf9d9LvAcOC7cPW_yd2MEizFs_TNHxY_g9pO81peZe-ZQskW9UiWg9y7RPlXGfwzFhb6n67BimwLkD5Ui6IU4uruo0wMMJM3fCjTaTN4Cnp14vKr6W1rMnN6cwt8sfnNpfBMastBcPUB37hzL8D2D6qp7smKHbcCcGLR1UiY0l_F9HL3oLtzeRT7ZcfyVQfnaFhRCKCqo4yq46WrmHh0UGfrzt3G1ImllkIqDS4kgXhmhxKJRciBPqJmfzwtamjNXTktcErJgqw-UyXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شروع تست پایلوت سرویس WhiteDNS VPN
نسخه تست عمومی اپلیکیشن whiteDNS VPN برای کاربران آماده است.
لطفا توجه داشته باشید که این مرحله صرفا برای تست جمعی است و سرویس ممکن است در هر زمان، بدون اطلاع قبلی، متوقف یا با اختلال مواجه شود.
هدف ما از این مرحله، بررسی عملکرد سرویس در شرایط واقعی، دریافت بازخورد کاربران و بهبود کیفیت نسخه‌های بعدی است.
در روزهای آینده نسخه‌های جدیدی منتشر خواهیم کرد و به‌روزرسانی‌ها به‌صورت مرحله‌ای در دسترس قرار می‌گیرند.
در این نسخه، محدودیت استفاده ۱گیگ  مصرف دانلود+آپلود در ۲۴ساعت اعمال شده است.
از همراهی، صبوری و بازخوردهای شما سپاسگزاریم.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/whitedns/953" target="_blank">📅 07:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آدرس جدید ساب WhiteDNS با بیش از ۲۵۰۰ کانفیگ تست شده و با سرعت بالا.
https://sub.whitedns.one/sub/mihomo.yaml
لینک های قبلی هم قابل استفاده هستند.
نرم‌افزار های پیشنهادی برای استفاده
iOS
:
Clash Mi
Android
:
FlClash
Desktop
:
Clash Party
|
FlClash
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/whitedns/952" target="_blank">📅 05:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-951">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سلام خدمت همه دوستان   پنل ثنایی در ورژن آخر تغییراتی انجام داده که باعث خراب شدن WhiteDNS Wizard شده.   بعد از گزارش های شما، ما این مشکل رو برطرف کردیم و ورژن جدید whiteDNS Wizard از گیت‌هاب ما قابل دسترسی میباشد.   https://github.com/iampedii/WhiteDNS-…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/whitedns/951" target="_blank">📅 04:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-949">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1KVHgXpAxEYCR2Gmxy-BC8zgPlch8FRYR82ywTarsNBP6FFCP7FHjVtGPk7tQUP1OSwVE7qexs-tFDSI699IfcA3Wx_z8Tls0UmZu-1hiFd2GiPzy2ttPylc1yCiUuSe24NUDSotybr4yyoBprLcrbwOevGeezR2yyeJ-K1CLvj8ZCi3nIy1-XHZ0zzsqgRpzKaA9n6OtL_TNnzWet-qf4k4espUIUYCF5wZrU3jXh71p_qK5ckXZcJr4VdVx859BSdiPFADPBRtNxNvWllD-nX5CxBhalkIUlZ6Y5ZUBB_xvpVyB9DVwYW2QMKgpQi1_ex_QJRrpzi3PGcDlvoQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
پنل ثنایی در ورژن آخر تغییراتی انجام داده که باعث خراب شدن WhiteDNS Wizard شده.
بعد از گزارش های شما، ما این مشکل رو برطرف کردیم و ورژن جدید whiteDNS Wizard از گیت‌هاب ما قابل دسترسی میباشد.
https://github.com/iampedii/WhiteDNS-Wizard/releases/tag/v1.2.0</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/whitedns/949" target="_blank">📅 16:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-948">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⏯️
ویدیو آموزش استفاده از WhiteDNS Wizard و نصب و راه‌اندازی کامل و اتوماتیک پنل ثنایی
https://youtu.be/rxxlNXLcaqU</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/whitedns/948" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-947">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/whitedns/947" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-945">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یکی از کاربر های گروه لطف کرده یک ویدیو خیلی کامل و خودمونی از نحوه استفاده از اپ WhiteDNS  درست کرده.
پیشنهاد میکنم تا وضعیت مناسبه دانلودش کنید.
ممنون از همراهی شما
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/whitedns/945" target="_blank">📅 07:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-940">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/whitedns/940" target="_blank">📅 05:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاوید نامان ایران(Bamdad)</strong></div>
<div class="tg-text">#کانفیگ
#دی_ان_اس
#وایت_دی_ان_اس
#مستر_دی_ان_اس
انکریپشن کی:
aaf4b6-@JavidnamanIran-aaf4b6fff
c.namad.xyz
c.irdmc.com
c.bamak.xyz
c.javidnaman.com
c.jnir.my
c.igoii.org</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/whitedns/939" target="_blank">📅 05:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ابزار WhiteDNS  برای ساده‌تر کردن راه‌اندازی و مدیریت سرورهای شخصی،  با نام  WhiteDNS Wizard آماده شده است.  هدف WhiteDNS این است که کاربران بتوانند بدون نیاز به دانش فنی درباره تنظیمات سرور، DNS، اینباندها، اوتباندها، گواهی‌ها و پنل‌های مدیریتی، سرور خود…</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/whitedns/938" target="_blank">📅 09:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سلام خدمت دوستان عزیز،  ما سرورها رو آپدیت کردیم و با همکاری جدیدی که شروع شده، از این به بعد ساب‌ها رو مرتب با کانکشن‌های جدید و تازه‌تر رفرش می‌کنیم تا کیفیت اتصال بهتر و پایدارتر بشه.  اگر این دامنه‌ها هم فیلتر بشن، لینک‌های جدید ساب رو براتون می‌سازیم…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/whitedns/937" target="_blank">📅 09:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سلام به همه دوستان عزیز
در حال حاضر گروه ما هدف یک‌سری حملات از سوی ربات‌ها و برخی افراد مخرب قرار گرفته است. این حساب‌ها در حال ارسال تصاویر و ویدئوهای نامناسب و پورنوگرافی هستند.
تیم WhiteDNS به‌صورت مستمر در حال مانیتور کردن گروه، شناسایی و مسدودسازی این حساب‌ها و ربات‌ها است تا محیط گروه برای همه اعضا امن و مناسب باقی بماند.
از صبر و همکاری شما سپاسگزاریم.
با احترام
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/whitedns/936" target="_blank">📅 17:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سلام خدمت دوستان عزیز،  ما سرورها رو آپدیت کردیم و با همکاری جدیدی که شروع شده، از این به بعد ساب‌ها رو مرتب با کانکشن‌های جدید و تازه‌تر رفرش می‌کنیم تا کیفیت اتصال بهتر و پایدارتر بشه.  اگر این دامنه‌ها هم فیلتر بشن، لینک‌های جدید ساب رو براتون می‌سازیم…</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/whitedns/935" target="_blank">📅 08:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M22N56auDz4mwtnnFta9outR1Wmch4M0VVdVz1WjOKedRRUZ-7XKwLPHRZ5STNi7IFC1Njum_9kEJCbXndZDI4hjfhuYncJW-H_wNTo22p5mBRlM1zI3gax3-OVX2-YwHvAaYFzQaoACAAMx91fVuc2mhjFz2XI_0m8Gyfg8Cz9OScDLyp2YQrRcNZAAVbRFgLVYv7FOSL_CLYG-rQtbP1iQJzv1KQCJSz_FRF0ahv7568KraOz-x5rsfcB7HyxLBsynmsVGSpay-d0HLUol94k6M390r4kCaeagM6Er4JMQzcGFWFACkgFgfsJrfmnjb5ixG5OWfaF0rv-KwJs-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار WhiteDNS  برای ساده‌تر کردن راه‌اندازی و مدیریت سرورهای شخصی،  با نام  WhiteDNS Wizard آماده شده است.
هدف WhiteDNS این است که کاربران بتوانند بدون نیاز به دانش فنی درباره تنظیمات سرور، DNS، اینباندها، اوتباندها، گواهی‌ها و پنل‌های مدیریتی، سرور خود را به صورت خودکار و یکپارچه آماده استفاده کنند.
با این ابزار کافی است اطلاعات اولیه مثل دامنه، سرور و دسترسی Cloudflare را وارد کنید. WhiteDNS به صورت خودکار رکوردهای DNS را تنظیم می‌کند، ساختار مورد نیاز روی سرور را آماده می‌کند، اینباندها و اوتباندهای لازم را می‌سازد، گواهی‌های مورد نیاز را مدیریت می‌کند و در پایان لینک‌های اتصال آماده را در اختیار شما قرار می‌دهد.
تمام مراحل به شکلی طراحی شده‌اند که کاربر نیازی به درگیر شدن با جزئیات پیچیده کانفیگ سرور نداشته باشد. هدف ما این است که راه‌اندازی یک سرور شخصی، از مرحله اتصال دامنه تا دریافت کانفیگ‌های نهایی، تا حد ممکن ساده، سریع و قابل فهم شود.
WhiteDNS برای کسانی ساخته شده که می‌خواهند کنترل سرور خودشان را داشته باشند، اما نمی‌خواهند زمان زیادی صرف یادگیری تنظیمات فنی، خطاهای رایج، مدیریت DNS یا ساخت دستی کانفیگ‌ها کنند.
این پروژه قدمی دیگر در مسیر ما برای آسان‌تر کردن دسترسی به ابزارهای کاربردی، مستقل و قابل مدیریت برای کاربران است.
https://github.com/iampedii/WhiteDNS-Wizard/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/whitedns/934" target="_blank">📅 19:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سلام خدمت دوستان عزیز،
ما سرورها رو آپدیت کردیم و با همکاری جدیدی که شروع شده، از این به بعد ساب‌ها رو مرتب با کانکشن‌های جدید و تازه‌تر رفرش می‌کنیم تا کیفیت اتصال بهتر و پایدارتر بشه.
اگر این دامنه‌ها هم فیلتر بشن، لینک‌های جدید ساب رو براتون می‌سازیم و منتشر می‌کنیم.
لطفاً این لینک‌ها رو تست کنید و نتیجه رو در کامنت‌ها بگید. اگر لینکی فیلتر بود یا مشکل داشت، اطلاع بدید تا جایگزین کنیم.
لینک ساب برای Clash Party / Mi Clash / FLClash:
https://sub.iampedi4.live/sub/mihomo.yaml
لینک ساب برای اپ‌های V2Ray:
https://sub.iampedi4.live/sub/base64.txt
آموزش استفاده از FlClash
آموزش استفاده از Clash Party
ممنون از همراهی شما
🤍
محتوای همه‌ی ساب‌ها یکی هست و فقط دامنه‌های جدید اضافه شده‌اند، چون دامنه‌ی قبلی فیلتر شده بود.
ساب گیتهاب فعلا آپدیت نخواهد شد.</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/whitedns/933" target="_blank">📅 18:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوستان عزیز WhiteDNS
🔥
اگر از WhiteDNS Sub استفاده می‌کنید و اخیراً احساس کردید کیفیت بعضی از کانکشن‌ها افت کرده، لطفاً بدونید که موضوع در حال پیگیریه.
ما در حال بررسی و بهبود وضعیت کانکشن‌ها هستیم و به‌زودی یک کانفیگ های بروز رو منتشر می‌کنیم.
خوشبختانه همکار هایی پیدا کردیم که می‌توانند در این مسیر کنار ما باشند و کمک کنند تا کیفیت و پایداری سرویس بهتر باشه.
به‌زودی آپدیت جدید روی Subscription قرار می‌گیره و اطلاع‌رسانی می‌کنیم.
ممنون از صبر، همراهی و حمایت همیشگی‌تون
🤍
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/whitedns/932" target="_blank">📅 14:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">در ادامه فیلتر شدن دامنه ما، دامنه جدید برای ساب آماده کردیم.
محتوی همه ساب ها یکی هستش، فقط دامنه جدید اضافه کردیم چون قبلی فیلتر شده.
تا فردا هم فیلتر کنن
(
🖕
)
ما لینک ساب جدید میسازیم  براتون
لطفا این رو تست کنید و نتیجه رو در کامنت ها بگید. اگر فیلتر بود یکی دیگه میسازیم.
🔥
لینک ساب جدید
https://sub.iampedi2.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/whitedns/931" target="_blank">📅 05:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دوستان و همراهان عزیز، سلام
🌺
لطفاً چند لحظه وقت بگذارید و این پیام مهم را در خصوص
نحوه ارتباط با ادمین‌ها
مطالعه کنید.
آیدی ادمین که در توضیحات (بایو) کانال قرار داده شده،
فقط و فقط
برای موارد خاص زیر است:
🔸
گزارش تخلفات
🔸
پیشنهادات همکاری در زمینه‌های مختلف
⚠️
لطفاً به این نکات توجه ویژه داشته باشید:
۱.
سوالات خود را در گروه بپرسید:
تمامی سوالات و مشکلات فنی باید فقط در
گروه‌های ما
مطرح شوند. لطفاً از ارسال پیام خصوصی (پی‌وی) به ادمین‌ها خودداری کنید. ما تیم پشتیبانی مجزایی نداریم که بتواند روزانه به صدها پیام خصوصی به‌صورت تک‌به‌تک پاسخ دهد.
۲.
توقع پاسخگویی در موارد نامربوط:
متاسفانه روزانه پیام‌های بی‌ربط زیادی دریافت می‌کنیم و در کمال تعجب، برخی از دوستان در صورت عدم دریافت پاسخ شاکی شده و حتی تهدید می‌کنند!
برای روشن شدن موضوع، به طور مثال
موارد زیر در تخصص ما نیست
و از پاسخگویی به آن‌ها در پیام خصوصی معذوریم:
❌
رفع مشکلات کامپیوتر، موبایل و یا خرابی مودم خانگی شما (برای این موارد به متخصصین شهر خود مراجعه کنید).
❌
مشاوره برای خرید تجهیزات سخت‌افزاری (مثل قطعی کابل شبکه و اینکه چه کابلی بخرید).
❌
آموزش خرید رمزارز و معرفی صرافی‌های مناسب.
❌
و هزاران مورد نامربوط دیگر که خارج از حوزه فعالیت ماست.
🙏
خواهشمندیم با رعایت این موارد، از ارسال پیام‌های خارج از موضوع به ادمین‌ها جداً خودداری فرمایید تا بتوانیم در موارد ضروری پاسخگوی شما عزیزان باشیم.
از درک و همراهی شما سپاسگزاریم
🌹</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/whitedns/929" target="_blank">📅 16:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⚠️
⚠️
⚠️
#موقت
⚠️
هر پیام اضافه، سؤال، بحث یا محتوایی غیر از نام سرور زیر این پست، باعث بن شدن خواهد شد.   سلام به همه دوستان عزیز  برای بررسی وضعیت اتصال، نیاز داریم یک تست همگانی انجام بدیم تا مشخص بشه در حال حاضر کدام متدها و سرورها برای شما وصل هستند. …</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/whitedns/927" target="_blank">📅 08:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚠️
⚠️
⚠️
#موقت
⚠️
هر پیام اضافه، سؤال، بحث یا محتوایی غیر از نام سرور زیر این پست، باعث بن شدن خواهد شد.
سلام به همه دوستان عزیز
برای بررسی وضعیت اتصال، نیاز داریم یک تست همگانی انجام بدیم تا مشخص بشه در حال حاضر کدام متدها و سرورها برای شما وصل هستند.
لطفاً قبل از تست، ساب خودتون رو یک‌بار Refresh / Update کنید.
برای شرکت در این تست:
به سابسکریپشن WhiteDNS وصل باشید.
داخل اپلیکیشن موبایل یا کامپیوتر وارد بخش Logs / لاگ‌ها شوید.
نام سروری که به آن وصل شده‌اید را زیر همین پست برای ما ارسال کنید.
لطفاً فقط نام سرور را ارسال کنید.
اگر نمی‌دانید دقیقاً باید چه کاری انجام دهید، مشکلی نیست؛ می‌توانید در این تست شرکت نکنید.
ممنون از همکاری شما
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/whitedns/926" target="_blank">📅 07:58 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
