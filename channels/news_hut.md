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
<img src="https://cdn4.telesco.pe/file/eGFEi3ORE3IVwqZ1fwZJWmaoi4ShnvAX42LasSw0K2gRsGpszqN1w4FMKLdOnNqhyTCABI_-2av5u46eCNddOpwz2y3hyHeKhGNRGXqufOwLUg8PtuE0jTVQQdEfL0AwDnCP468DmG6TRkSeWs2-EGwCw_5YnetNMqLMNhogOG5GTjHjd49eGu85fVwljVuupWiOYoYG7yq3cR4rrm-HTayYb4R0SYgm_M6ZtpGJSP30yHTW73r6c6LKE7hpsCEQH3AGm1m1SJsaZnzT9QlUtL2ye-dg0ZxtITU6TX72EArnK59Tjlh7T85z7VCtPobfF81i71ZmulAQ80Ro01MbtQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-72813">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=v88VspXX6Ex4T7pfG8po8Q1lMF-SM0OifVy31keKc8ppEKLbmBjTAgoII945sqrDDMnRCrVR-LcFx5_ChRUUZ52LDQlsrO4iTENfsCXmvE0khfD2u-rJSHoXv0PL1HOcFw0RrDd74ZvzhXx22wOfBLxdE5oPAwt6OvuyhVYzt57fBXEf4NW1qHFVN91uZsLIXXdRBoInlKPFYZEtsyAWtPrLFASceZPeTYd5zUwGoDsliOFh8b_L0PDtGY5wGlf2VP_duHNzB1jeBPPKxSMVQIb925VCCxySBVf9UDmzHbjpiqWuTuYeAcL9_Y8XbUU1G0k6GlBqP-U6-0Sh4PoLxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=v88VspXX6Ex4T7pfG8po8Q1lMF-SM0OifVy31keKc8ppEKLbmBjTAgoII945sqrDDMnRCrVR-LcFx5_ChRUUZ52LDQlsrO4iTENfsCXmvE0khfD2u-rJSHoXv0PL1HOcFw0RrDd74ZvzhXx22wOfBLxdE5oPAwt6OvuyhVYzt57fBXEf4NW1qHFVN91uZsLIXXdRBoInlKPFYZEtsyAWtPrLFASceZPeTYd5zUwGoDsliOFh8b_L0PDtGY5wGlf2VP_duHNzB1jeBPPKxSMVQIb925VCCxySBVf9UDmzHbjpiqWuTuYeAcL9_Y8XbUU1G0k6GlBqP-U6-0Sh4PoLxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا از لوکس ترین مدارس بالا شهر تهران که شهریه شون یک میلیارد تومنه!
@News_Hut</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/news_hut/72813" target="_blank">📅 10:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72812">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOBFr751XTFzVfQtraUnjd3ALowmMz_qsHHW9QhgCvZ0EaZMHe_N8z3SAnrvvvUj8pGeytuEMJR6X5DO8Wawj7PHRDkYs1coCX0v7JPgXXjdewZtWWxZnPXLz3sj7q2mwqdOL_5R-c_ipNEWdTudqBSdQaelCTZ7Lf0Y3sDOOD_YgoKKid2pB3v4qssHLHIVOcgusxclrKp5gFWFtsqF2Ep1Aue9yOOoWV5BTfxM3KPyFnFGpiJElicz8IBTcXC3GtXhyioXfp_9u1fnLZ_iXAv0ey7WDT1_BDAN_wOy4lXkiPEyu20sFXXXMU2fGaiyfVGQN9aZAWzON7iozC7yVYCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOBFr751XTFzVfQtraUnjd3ALowmMz_qsHHW9QhgCvZ0EaZMHe_N8z3SAnrvvvUj8pGeytuEMJR6X5DO8Wawj7PHRDkYs1coCX0v7JPgXXjdewZtWWxZnPXLz3sj7q2mwqdOL_5R-c_ipNEWdTudqBSdQaelCTZ7Lf0Y3sDOOD_YgoKKid2pB3v4qssHLHIVOcgusxclrKp5gFWFtsqF2Ep1Aue9yOOoWV5BTfxM3KPyFnFGpiJElicz8IBTcXC3GtXhyioXfp_9u1fnLZ_iXAv0ey7WDT1_BDAN_wOy4lXkiPEyu20sFXXXMU2fGaiyfVGQN9aZAWzON7iozC7yVYCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: خبر داری دلار شده ۲۷٠ تومن؟
یه خانم تو تجمعات: اره ولی ما بخاطر وطنمون اومدیم، اگه ما نبودیم دلار حتی گرون ترم میشد
@News_Hut</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/news_hut/72812" target="_blank">📅 09:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72811">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=qelGHxQo3PPa7r9jAvgoUl_SL-01MLTPkdc5yaootmFoqjf2nsTVHnxPqV1c0axghpCs8Az5EqbrwrPjS2_NR2D74NKyihVUUWsFqZ6wUzj0f9qDBJ9bmvGd37eXZRK690Yj4CNGAOX1kp6uGb8waMXSUXHp5lBbOf6M6vr_Gi8kQGp4-nHIE1ih0k7YSueMi8Kxn4uKSBewLPVsUJbPTjDOPaAczTGKDU_gLB2RBhs5r0YsY2DX6IPOTNtouIlV-t1wrJBYEqVLZoZOFBVVMd0HfPkMkNbJnnh8L59Hlx5HIdCXM0sExwueKAdKU_PrCs-o5qfzA0EIe7bNbrvwpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=qelGHxQo3PPa7r9jAvgoUl_SL-01MLTPkdc5yaootmFoqjf2nsTVHnxPqV1c0axghpCs8Az5EqbrwrPjS2_NR2D74NKyihVUUWsFqZ6wUzj0f9qDBJ9bmvGd37eXZRK690Yj4CNGAOX1kp6uGb8waMXSUXHp5lBbOf6M6vr_Gi8kQGp4-nHIE1ih0k7YSueMi8Kxn4uKSBewLPVsUJbPTjDOPaAczTGKDU_gLB2RBhs5r0YsY2DX6IPOTNtouIlV-t1wrJBYEqVLZoZOFBVVMd0HfPkMkNbJnnh8L59Hlx5HIdCXM0sExwueKAdKU_PrCs-o5qfzA0EIe7bNbrvwpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آجرلو عضو تیم مذاکره‌کننده:
بابا بالاخره یه جایی باید قبول کنیم یه‌سری از این تحلیل‌ها اشتباه از آب دراومده!
هرکی نظر متفاوتی داشت رو «خائن» و «وا داده» خطاب نکنید؛ وقتی می‌گفتید ادامه جنگ این‌طور میشه، اسنپ‌بک هیچ اثر اقتصادی نداره، نفت میره روی ۱۵۰ دلار یا با شکست ترامپ در انتخابات کنگره همه‌چیز تغییر می‌کنه، باید امروز جواب همون تحلیل‌ها رو بدید.
اینکه بگیم «ترامپ انتخابات کنگره رو ببازه، دموکرات‌ها جلوشو می‌گیرن» هم خیلی ساده‌انگارانه‌ست.
بین انتخابات تا شروع کنگره جدید چند ماه فاصله هست و رئیس‌جمهور آمریکا هم قدرت زیادی داره و می‌تونه سیاست‌هاشو دنبال کنه.
خلاصه اینکه تحلیل غلط، تحلیل غلطه؛ فرقی هم نمی‌کنه از طرف چه کسی گفته شده باشه. به‌جای توجیه و فحش دادن به بقیه، بهتره بعضی‌ها یک‌بار هم بابت پیش‌بینی‌های اشتباهشون پاسخگو باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/news_hut/72811" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72810">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/72810" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72809">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRFjE7Jl_QS6PCs-weqTPhgP1wzeA-DoLeOfv25e3k-fMyUpHUowOxnadgfk95OFHs2ygzAQk5RDyEHuXF7Esgmbgf4wOoKXkfva30ARzgDW6JEL_fCGu0YOUPynYiYLLjut3Yrcd54w8fRQKTShBkMsog75BFgxTjy7RanTuvk6drcr4EuPQDMA09RqoLFKDgPICApghBnxqcJV8N1kF9P7te8zxifxmtU1VyCWM910mGRsUYEpDx8eEyPYNoNQqnhatJkQqETJwYi0nlKIpOcbUM0ZGBrhtFTN-FPSGLGNjweQ4Mz1CAobpy6s0h1urMEkjdkCesf_y-nzZTK5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/72809" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=K9JL8MNgjqE9keW0mqrmaYk2RuVw5UXm_5Svv2hzBGrRnhRgyQZVl3D7SdmHObftIWKOF6ERt9E4gsw9pakG5lc8cfLXo5lkCw-SaHHZjv21NgECtiG7HXgUBURuZP3aUv6GoOg1XXvOk7TWSkfF0txbK0Lr0UdY5MYbUlSPWCYtP5hfFz3M53wF1-Iq_Q0OiQGM4-RvgIDJvHNglwe48m-D0aOtp9JIMyXtTUeb2beV-yQ7jxvclE_Rwu75Hujvg4sgKMhXhI4wcRFBDDZ7V-o3-ZmL-ep71IOlkFb5B4kCoRjashWXPRYmmJwDSois06dXx6jwAcZblmlh5GoKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=K9JL8MNgjqE9keW0mqrmaYk2RuVw5UXm_5Svv2hzBGrRnhRgyQZVl3D7SdmHObftIWKOF6ERt9E4gsw9pakG5lc8cfLXo5lkCw-SaHHZjv21NgECtiG7HXgUBURuZP3aUv6GoOg1XXvOk7TWSkfF0txbK0Lr0UdY5MYbUlSPWCYtP5hfFz3M53wF1-Iq_Q0OiQGM4-RvgIDJvHNglwe48m-D0aOtp9JIMyXtTUeb2beV-yQ7jxvclE_Rwu75Hujvg4sgKMhXhI4wcRFBDDZ7V-o3-ZmL-ep71IOlkFb5B4kCoRjashWXPRYmmJwDSois06dXx6jwAcZblmlh5GoKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئوها از شهر طاعون زده شلخوف در روسیه:
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72808" target="_blank">📅 01:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72807">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=dCHCns9y2nwaI95uaAGLiT8xjIXJILJjCtrdI6KRID4BW9tf2p84uTHUh_QbrTFiljmvfh2BhhgTRei9EaxYvggGlkOIxilg8W6HKeMJOTlUqnAOxImTBs6bnMJrB0MCUjtXxtAvgifHz0pfcPqWee_J4ORjULNjiEXoGXJ-m9r6mFxvSuP8FWlCnmkzyerdU6WcTrnGV_w0PAeicAZUz22s6Y1aeAb7JYp-4Vm5guTZYVMKyricn7FCjDdTZyW87kh0Mjt_xORbZXzCDKQFsosCPRPu0p0vDcdznMlj3j6mUo_dG3Z5fanwvc2gTOjGiis5iAb0tgmghqAxjhqhxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=dCHCns9y2nwaI95uaAGLiT8xjIXJILJjCtrdI6KRID4BW9tf2p84uTHUh_QbrTFiljmvfh2BhhgTRei9EaxYvggGlkOIxilg8W6HKeMJOTlUqnAOxImTBs6bnMJrB0MCUjtXxtAvgifHz0pfcPqWee_J4ORjULNjiEXoGXJ-m9r6mFxvSuP8FWlCnmkzyerdU6WcTrnGV_w0PAeicAZUz22s6Y1aeAb7JYp-4Vm5guTZYVMKyricn7FCjDdTZyW87kh0Mjt_xORbZXzCDKQFsosCPRPu0p0vDcdznMlj3j6mUo_dG3Z5fanwvc2gTOjGiis5iAb0tgmghqAxjhqhxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پشم ریزونی که ارتش یمن منتشر کرده که دارن با ماشین، حوثی‌هایی رو که در کنار ساحل گرفتار شدن و در حال مقاومتن رو زیر میگیرن و له میکنن:
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72807" target="_blank">📅 01:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e493def7.mp4?token=ri4nDYRKkKP1LPUE1_F_eVc0eV-UhDjkEV-c69VGiBMaJEEgEJqNmQzbZ1WfATymS_SndrrNItEOztLXcz1tBmuEQZWzCc5VosJLzhyAvNg10SF_czQNXX9420LHhkKvyx9pE1lSB-8bTW47kn4A3ZKvvvjv1G5LEdrQ3cqC_a9GffYUGi9YskgWGRn15fdeYOI5FoLhURxQcA2_jdK2F6qcbRfcW0CK1zIrZOxWKO4EgRR17GeBWuCgKzoIg0flL9juqpWnpZm7HuqJuLb801KEnXsirfF5z2b0i0hCHC06_0ICYASqEMiDpB6F5MYTxFslklS8VAaebXZIez_BEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e493def7.mp4?token=ri4nDYRKkKP1LPUE1_F_eVc0eV-UhDjkEV-c69VGiBMaJEEgEJqNmQzbZ1WfATymS_SndrrNItEOztLXcz1tBmuEQZWzCc5VosJLzhyAvNg10SF_czQNXX9420LHhkKvyx9pE1lSB-8bTW47kn4A3ZKvvvjv1G5LEdrQ3cqC_a9GffYUGi9YskgWGRn15fdeYOI5FoLhURxQcA2_jdK2F6qcbRfcW0CK1zIrZOxWKO4EgRR17GeBWuCgKzoIg0flL9juqpWnpZm7HuqJuLb801KEnXsirfF5z2b0i0hCHC06_0ICYASqEMiDpB6F5MYTxFslklS8VAaebXZIez_BEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان سخنرانی حسین رحیمی، رییس پلیس امنیت اقتصادی، درباره افزایش قیمت دلار، برق محل برگزاری سخنرانی قطع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72806" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72805">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmB0vjd_NG4JyI6clgOg9CU25DqPM-4HOUUQ-QciqEehymgSz6UmbsUlfznMtiHk3TkSoVI2R44Ak-ZF_0C0rP6P4cqX9EaTMNOmrKqbn-01U4vh0uZMWpGDKe-G6AV9S20uNbQMQbRt756UrQaonCJql9P6pMNyOwooqM2QLtKLvw3fAByW2VfQ0rbEPXtwjA_5x9oDQPeYEmt3zmSBbR65e7Fi0_e6P6NBXkvOfLBLs8jGSPO68D_0bFC689vjnRLYCn3u28QSMjf2mCwdq9h7NRPeYEp8VY1uDCtQuetUlfiN6_lUtry7S7E0pKBpS3pa0w-UZDzsYp_lFrn36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت درباره ایران:
«عملیات طرد اقتصادی» نتیجه داده؛ ارزش ریال به پایین‌ترین سطح تاریخی رسیده، ایران ماه گذشته هیچ نفت خامی برای بارگیری روی نفتکش‌ها نداشته و حتی یکی از مقام‌های ارشد امنیتی ایران هم گفته کشور در یکی از سخت‌ترین دوره‌های تاریخش قرار گرفته.
حکومت ایران در حالی مردم خودش را تحت فشار و رنج قرار می‌دهد که منابعش را صرف حمایت از تروریسم می‌کند و عملیات طرد اقتصادی تا زمانی که جمهوری اسلامی از تأمین مالی تروریسم و ساخت سلاح هسته‌ای دست نکشد، متوقف نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72805" target="_blank">📅 00:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72804">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=BUjjvXgSU9QODMebdy0YkP4GaoUg7S1YT30dmuVeGXsndBl6WNoxa8ceB1YJniUhzw-9eX4lvOkanrvqH7RgDFDdMMSmNYaZK-Q7kWbG7bzS7dHlvFHzhkhxvt6-nGQExN1sf67miOeYv5REsh2kXiIlCHqviU8z9Yi22e5hOALLFj3H0OhBOsZZmHujP3fiWgtnsxCFIJieyWf5C_MfgfxBTCxtOT9c2mPfcaLqpmUKGN3DUbvgXzDW4mJhYI0IYXdM9ln6vzboVjT8DYj0WUzSqnpFPOyG9fBx9xnZsc2dT3OifyRMlvMuIsS0eVFJQCs4p7yAxtG1LP_jhhWhUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=BUjjvXgSU9QODMebdy0YkP4GaoUg7S1YT30dmuVeGXsndBl6WNoxa8ceB1YJniUhzw-9eX4lvOkanrvqH7RgDFDdMMSmNYaZK-Q7kWbG7bzS7dHlvFHzhkhxvt6-nGQExN1sf67miOeYv5REsh2kXiIlCHqviU8z9Yi22e5hOALLFj3H0OhBOsZZmHujP3fiWgtnsxCFIJieyWf5C_MfgfxBTCxtOT9c2mPfcaLqpmUKGN3DUbvgXzDW4mJhYI0IYXdM9ln6vzboVjT8DYj0WUzSqnpFPOyG9fBx9xnZsc2dT3OifyRMlvMuIsS0eVFJQCs4p7yAxtG1LP_jhhWhUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ:من فکر میکنم ایران مسئول حمله به هواپیمای «فلای دبی»است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72804" target="_blank">📅 23:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72803">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
ما مقادیر بی‌سابقه‌ای نفت از تنگه هرمز خارج می‌کنیم. یکی از مشکلاتی که داریم این است که پالایشگاه‌های روسیه به‌شدت هدف حمله قرار می‌گیرند.
این یک مشکل است، اما اوضاع به‌خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72803" target="_blank">📅 23:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72802">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سؤال: آیا نگران شیوع طاعون در روسیه هستید؟
ترامپ: این بیماری‌ای است که قبلاً قادر به مهار آن بودیم؛ اما به نحوی، آن میکروب‌ها قوی‌تر و هوشمندتر شده‌اند. آن‌ها مثل یک ارتش هستند. ما به روسیه کمک خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72802" target="_blank">📅 23:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72801">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=HfhJWEkVc66VoCp9lRUBkGOdhwx3LXCZMG3kYf50XiPMhe9xtKVsQQ3INgcFYy8h2AFQyz5GGWdZuezPD3ghcr5qSLuTXrZQIx80LCnWgCyeVOwfrIRKd86wTBQgszBzunYChSFIcBr96qbnq1GmFk6_kpH8g6-bIVL1A6HPfu_1DuezjlDzRX3ON2C-026fmlqDq4oynWK7k190yVXjJBMGstA5c66pnr3QP-ORtxzp2mt-FOl1alklyt5IwGjYpyZ2g0syqLSdC3DdWwgsUFZTXH3I5AafD3vlf1k6YMeA5BWsFK8ELR37sGLWF9sGKnFvZ9Bzw8C8m-rq5T40kGuITsYJJUjWu-r7BHLwfQhYeBSy4GtiIfp3lAs0zBBw79EkA5Qc0gBIj5KnohyAXLZIlCcli_UeA0msXoXoDTexTruGQpoJIMbHpOW6bRg0TbpU_EhhI78zrFdOhvtis-TGXEvkaG4Y0vnSkVswyOfCRm5QZbXILumh2lucNP8tR7ArPSnyXMHvCpVkWllmEpfG9IRO82Uzf7f5buV2wU9-IVNAi4D8E-4Ifv9_BxGT8isdJlK_xr3sSmiy-IuVLHrDDNiS6WWBzTJL0obfpJJJE66sn2yQjzDOvYhmIGOqlVGNVM4P84AwCL1wrYXlsK93FWBe86-NXVjwlYDM8oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=HfhJWEkVc66VoCp9lRUBkGOdhwx3LXCZMG3kYf50XiPMhe9xtKVsQQ3INgcFYy8h2AFQyz5GGWdZuezPD3ghcr5qSLuTXrZQIx80LCnWgCyeVOwfrIRKd86wTBQgszBzunYChSFIcBr96qbnq1GmFk6_kpH8g6-bIVL1A6HPfu_1DuezjlDzRX3ON2C-026fmlqDq4oynWK7k190yVXjJBMGstA5c66pnr3QP-ORtxzp2mt-FOl1alklyt5IwGjYpyZ2g0syqLSdC3DdWwgsUFZTXH3I5AafD3vlf1k6YMeA5BWsFK8ELR37sGLWF9sGKnFvZ9Bzw8C8m-rq5T40kGuITsYJJUjWu-r7BHLwfQhYeBSy4GtiIfp3lAs0zBBw79EkA5Qc0gBIj5KnohyAXLZIlCcli_UeA0msXoXoDTexTruGQpoJIMbHpOW6bRg0TbpU_EhhI78zrFdOhvtis-TGXEvkaG4Y0vnSkVswyOfCRm5QZbXILumh2lucNP8tR7ArPSnyXMHvCpVkWllmEpfG9IRO82Uzf7f5buV2wU9-IVNAi4D8E-4Ifv9_BxGT8isdJlK_xr3sSmiy-IuVLHrDDNiS6WWBzTJL0obfpJJJE66sn2yQjzDOvYhmIGOqlVGNVM4P84AwCL1wrYXlsK93FWBe86-NXVjwlYDM8oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آن چه تهدیدی بود که باعث شد آن هواپیماها را از بریتانیا خارج کنید؟
ترامپ: احتمال وجود تهدیدی را می‌دادیم؛ خب چرا باید آن‌ها را آنجا نگه می‌داشتم؟ با تهدیدی مواجه بودیم. ما کسانی را که آن تهدید را مطرح کردند، می‌شناسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72801" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72800">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=Da3P48FtVI3R-F05OA2gm4QL2_x83HBDlx8_Dlg1Gx5jWajiHgl-ETmP7Tgzq1kZkwK0xFpG4-YSyn4-bG5cz_ggGhoowZEnV3GRAtjbalVp9x6E60qo_aD6MuiSfqiuj8RzOmIxYe3cjFNYOWAkEiSqLr12vgeT01X2SU7LKDMoEgOCIxqjgxDhwdXlqRQMLK0MP0-EONi4egX-7TM8u2gVlsD0AGA5oufnl4jH7Rw3ahnvJqyO7UIMNH6sgAIIDLmUQaHzd_dsi4hlmp85vzqvs7tin4j5cmo07gKSVUP2TrOBND4mWL6PTEme04xOAtHplywaTJwbu5vXFZERow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=Da3P48FtVI3R-F05OA2gm4QL2_x83HBDlx8_Dlg1Gx5jWajiHgl-ETmP7Tgzq1kZkwK0xFpG4-YSyn4-bG5cz_ggGhoowZEnV3GRAtjbalVp9x6E60qo_aD6MuiSfqiuj8RzOmIxYe3cjFNYOWAkEiSqLr12vgeT01X2SU7LKDMoEgOCIxqjgxDhwdXlqRQMLK0MP0-EONi4egX-7TM8u2gVlsD0AGA5oufnl4jH7Rw3ahnvJqyO7UIMNH6sgAIIDLmUQaHzd_dsi4hlmp85vzqvs7tin4j5cmo07gKSVUP2TrOBND4mWL6PTEme04xOAtHplywaTJwbu5vXFZERow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا فکر می‌کنید این خطر وجود دارد که ایران پهپادهای رزمی وارد بریتانیا کرده باشد؟
ترامپ: نمی‌توانم چنین چیزی به شما بگویم. اگر دست به چنین کاری زده باشند، بهای سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72800" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72799">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=RcbmuQdkhXAMCr8ml0AJ1GCB4yDJqkrbYctr6HG-Oe041Xf6qIwI8PneQOUch3JlCPLJ71YpBDYiDm_bWtpPYAVr28OuUsq_cNuJ2F2UCHos4b1T-lJvRW2A4d6tOFiw8tfe2HQPSGFrSXbDkRb55XiRagpo5rS-YIu9MDH912_o2UGu33UrrppG55dmWVU2FOonqAQ-ZCVtjbjGk6Kpt-obscoBL_B02qfgQS3bg2TFoJsm73JqCf8RlCcHTpG881_fR9gTNiFy1l5J4j1FjcMo5wK-6yhFEst2fjS6wAS4hjRZA160VsdNaqZ3swfa4lsFqB6CLhJxMKfQEeDciA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=RcbmuQdkhXAMCr8ml0AJ1GCB4yDJqkrbYctr6HG-Oe041Xf6qIwI8PneQOUch3JlCPLJ71YpBDYiDm_bWtpPYAVr28OuUsq_cNuJ2F2UCHos4b1T-lJvRW2A4d6tOFiw8tfe2HQPSGFrSXbDkRb55XiRagpo5rS-YIu9MDH912_o2UGu33UrrppG55dmWVU2FOonqAQ-ZCVtjbjGk6Kpt-obscoBL_B02qfgQS3bg2TFoJsm73JqCf8RlCcHTpG881_fR9gTNiFy1l5J4j1FjcMo5wK-6yhFEst2fjS6wAS4hjRZA160VsdNaqZ3swfa4lsFqB6CLhJxMKfQEeDciA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:نظر شما درباره ضدحمله عربستان و یمن علیه حوثی‌ها چیست؟
ترامپ: همه چیز به خوبی پیش خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72799" target="_blank">📅 23:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72798">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=WUJBZLS1qki8jkOCs5hBLflFeEIJipz0fx5AQJL7NqFyBdEoFpBok5ffi6iuWlrcRwpU1SL8v_orqF1jcU6m755S6pxok6kMAXR8ezud7noRilSP-81mLzYYfzvzKORkL4FRZm20BgFQHyJYeqCPEacQVLlF2vKarlTNgKk3zQlAOF85Xk81Z6p9BDppHxyYIO4kvc4GAGLbskKXB-bwlH3vCxolI1Hf0oiy43-t5aHPagbd2oBeceeYFCW-NZoAu_4d99fQl-Uh-HpMO2XC-5ti2d8H6PhHxb6O8ENaCRlVSlur7U94aGkdj_VyT386txj9SE45-xGnzLPry8xka1x-H-f0R-KqRWsoxkzDdd_UVyi3_LKW7nRKkF0cFCW7BlcrVH4kptd-srOUgzxkgm3L-YeHl2bGED1f9NJ9vrxe1_TI4vo9jscPXXJdwG1X2ekR3KHpvrfkBnjwLJGHyBT-FncoeXSHOc5ro5knZDy4-WROUeyhhqrU8-7x-HldfxJ02Gn6p2EMOKXbBqJghiGQu-ellEKQ12ECbDTXiMpH-R1Neqx1BTkDbbAlxgz5iSuDPBL2uI6pM1UZCqZ-vuJKtl-RfiW-wc1rqWj4XLe99IfYCeyT9VYdoKdBGJ0cSsohDT1sKQGoMbQuMBSr0aUoWD0Jh4Au1sM8YVCpFjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=WUJBZLS1qki8jkOCs5hBLflFeEIJipz0fx5AQJL7NqFyBdEoFpBok5ffi6iuWlrcRwpU1SL8v_orqF1jcU6m755S6pxok6kMAXR8ezud7noRilSP-81mLzYYfzvzKORkL4FRZm20BgFQHyJYeqCPEacQVLlF2vKarlTNgKk3zQlAOF85Xk81Z6p9BDppHxyYIO4kvc4GAGLbskKXB-bwlH3vCxolI1Hf0oiy43-t5aHPagbd2oBeceeYFCW-NZoAu_4d99fQl-Uh-HpMO2XC-5ti2d8H6PhHxb6O8ENaCRlVSlur7U94aGkdj_VyT386txj9SE45-xGnzLPry8xka1x-H-f0R-KqRWsoxkzDdd_UVyi3_LKW7nRKkF0cFCW7BlcrVH4kptd-srOUgzxkgm3L-YeHl2bGED1f9NJ9vrxe1_TI4vo9jscPXXJdwG1X2ekR3KHpvrfkBnjwLJGHyBT-FncoeXSHOc5ro5knZDy4-WROUeyhhqrU8-7x-HldfxJ02Gn6p2EMOKXbBqJghiGQu-ellEKQ12ECbDTXiMpH-R1Neqx1BTkDbbAlxgz5iSuDPBL2uI6pM1UZCqZ-vuJKtl-RfiW-wc1rqWj4XLe99IfYCeyT9VYdoKdBGJ0cSsohDT1sKQGoMbQuMBSr0aUoWD0Jh4Au1sM8YVCpFjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا تهدید خاصی وجود داشت که باعث شد آن بمب‌افکن‌ها را از بریتانیا فراخوانید؟
ترامپ: بله، فکر می‌کنم بتوان چنین گفت. پرواز آن‌ها تصادفی نبود؛ تهدیدهایی در کار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72798" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72797">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449cc78904.mp4?token=ZdJZMlt-JijejDO7NkvGd_TxMfcB4zIUDvXY-M_tb3eyAlydoN8bVtPGvtPKqZpHPqFuK_bA3-kreh8-nkd4eV7F8ugqTWhWRPXCeo6SP9KXthE8tlyedSbh2iLCs1g79Rt4GIbSO3vCZP4hV0DTKuFgLZbe_5xC7uecy_1-qJdICt2GuHnFneITAn2sVScn8Rh7UFGifQ6gPpskG2b-MGW58V-s6QMpJC0u4oim_kMnf7WuXj_oeH3Rb7GyrFaHqwKdJ9ari471O0aR8cyzL3qY3Ie7dnKcfPMTOZdb49gAX4D66S0l-zE2YXAEq5dkNZkG50RAQDyAeQB9otvPHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449cc78904.mp4?token=ZdJZMlt-JijejDO7NkvGd_TxMfcB4zIUDvXY-M_tb3eyAlydoN8bVtPGvtPKqZpHPqFuK_bA3-kreh8-nkd4eV7F8ugqTWhWRPXCeo6SP9KXthE8tlyedSbh2iLCs1g79Rt4GIbSO3vCZP4hV0DTKuFgLZbe_5xC7uecy_1-qJdICt2GuHnFneITAn2sVScn8Rh7UFGifQ6gPpskG2b-MGW58V-s6QMpJC0u4oim_kMnf7WuXj_oeH3Rb7GyrFaHqwKdJ9ari471O0aR8cyzL3qY3Ie7dnKcfPMTOZdb49gAX4D66S0l-zE2YXAEq5dkNZkG50RAQDyAeQB9otvPHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در میدان آزادی (میان اقبال) سنندج از این کوماندو‌ها رونمایی کردن برای مردم! امیدوارم این فیلم رو هیچ وقت ترامپ نبینه چون بعدش قراره دیگه شبا آرامش نداشته باشه
😂
یه ساختمون چند طبقه رو ۱ دقیقه طول کشید تا برسن پایینش! از پله‌ها میومدن زودتر می‌رسیدن
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72797" target="_blank">📅 23:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72796">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=giuSN9M_kpQCWv4I8vEaJsvFJhNXUcvRr5cpBRNYeoLwUhR-FBnsK9N_2boMCzulpZVFGU3_s1fv9J84oTmkZfWg2T46dNJClDsWlHB4p9YZoigCViJEHLXXkXav3IdV9PFWCK3W1yfs5BaiFFdHmpYWMmRXSWoSzDF0jU3o6iIZQoWdY95e4vVOf_BENwIStukLdcwDp3dEAnmIPE9l0i31EqCAwRoK1YjumNUV9bIS7GYJey93iKtX_E7MYmV0qcclV4U_q2PjRe5uQnp_qSVk6LlLTPFkRwlC6ixTM60ZBA7HZLG5f-nEFnXKCjZRNUMBd_C4eMaQ2Fr_PkdzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=giuSN9M_kpQCWv4I8vEaJsvFJhNXUcvRr5cpBRNYeoLwUhR-FBnsK9N_2boMCzulpZVFGU3_s1fv9J84oTmkZfWg2T46dNJClDsWlHB4p9YZoigCViJEHLXXkXav3IdV9PFWCK3W1yfs5BaiFFdHmpYWMmRXSWoSzDF0jU3o6iIZQoWdY95e4vVOf_BENwIStukLdcwDp3dEAnmIPE9l0i31EqCAwRoK1YjumNUV9bIS7GYJey93iKtX_E7MYmV0qcclV4U_q2PjRe5uQnp_qSVk6LlLTPFkRwlC6ixTM60ZBA7HZLG5f-nEFnXKCjZRNUMBd_C4eMaQ2Fr_PkdzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شامگاه شنبه ۱۱مهر۱۴۰۵؛لحظه برخورد صاعقه با برج میلاد:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72796" target="_blank">📅 22:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72795">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=Xg3_DFIimTTSOgnSrzqhj3CKZBY6eqbNE3tPox0TbLzB-5vLmLCZl1sAsOSr8jU8MbldEqq1Uz7nBlXCdlDwxAXAy6uPl42ucaWvW-cpswfAX7lXqG1aJ8eAYyY6I-IJ3SP_WvSqqmlHEuh29Q0qNqsIf9xFwkb4f3GUr-i5pxwZmsEodAz2WDX2uT600b3G5YCwnQk7Dj1pG51ySyHF7OlSG9OnCsztQKTlkZQ0EIn4-iN24vunycbPJjgN0H6tb39QzAVgy08WJHZDnjtq4F6RCu-GSQQqZ9Qdc0PVaFOw9PM7o2y6HZ-kJe3ITrce3Euao6kgM9ig5j2b6htOFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=Xg3_DFIimTTSOgnSrzqhj3CKZBY6eqbNE3tPox0TbLzB-5vLmLCZl1sAsOSr8jU8MbldEqq1Uz7nBlXCdlDwxAXAy6uPl42ucaWvW-cpswfAX7lXqG1aJ8eAYyY6I-IJ3SP_WvSqqmlHEuh29Q0qNqsIf9xFwkb4f3GUr-i5pxwZmsEodAz2WDX2uT600b3G5YCwnQk7Dj1pG51ySyHF7OlSG9OnCsztQKTlkZQ0EIn4-iN24vunycbPJjgN0H6tb39QzAVgy08WJHZDnjtq4F6RCu-GSQQqZ9Qdc0PVaFOw9PM7o2y6HZ-kJe3ITrce3Euao6kgM9ig5j2b6htOFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: اخراج ما از آمریکا مثل اخراج تیم برنده از المپیکه!
پس خبر درست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72795" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72794">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=PUcEA0i-MYR1_ec4epANSrl14qaiZlOTHwKOK-vodbU1UmuyrnFjfx2z97uqlBH__ihEzq9hQaQjh3tg1SNguWRhpBaqniBnOVqLkiRWJXdEcOBEjHIiH4muEsln-u3C9TSEw63JGvlOuro7v4s6TLTw3L__zIvc_DZnfC8EAanD_oP-AYH5XiDYOpq-n5bzSzgv15Jo_Zh8HCsyM82fJbvcTsPynR8ZpUlkAKz9qQz6vxl5z8uwWpQghgPuDXz8OaCE2n-Bprn2gBgNhsReJhYYUFOIlGrXZvK_W_caFNqzs7tEnsNv62nsm0EkJtUXUPWN0gQiA73_FsHHAkbX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=PUcEA0i-MYR1_ec4epANSrl14qaiZlOTHwKOK-vodbU1UmuyrnFjfx2z97uqlBH__ihEzq9hQaQjh3tg1SNguWRhpBaqniBnOVqLkiRWJXdEcOBEjHIiH4muEsln-u3C9TSEw63JGvlOuro7v4s6TLTw3L__zIvc_DZnfC8EAanD_oP-AYH5XiDYOpq-n5bzSzgv15Jo_Zh8HCsyM82fJbvcTsPynR8ZpUlkAKz9qQz6vxl5z8uwWpQghgPuDXz8OaCE2n-Bprn2gBgNhsReJhYYUFOIlGrXZvK_W_caFNqzs7tEnsNv62nsm0EkJtUXUPWN0gQiA73_FsHHAkbX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آقای آتش‌نشان در مورد ساخت پلاک مشخصات برای دانش آموزان:
امروز رفتم یه دبیرستان دخترانه برای کنترل مسائل امنیتی بین حرفامون با مسئولین مدرسه متوجه شدم که دارن برای دانش آموزان پلاک مشخصات فردی درست میکنن مثل همونایی که زمان جنگ استفاده میشد؛
از این پلاک‌ها که زمان جنگ سربازها مینداختن دور گردنشون که اگه بر اثر بمب و موشک چهره‌شون دیگه قابل شناسایی نبود، از رو پلاک شخص رو تشخیص بدن..
وقتی پرسیدم برای چیه؟ گفتن نمیدونیم فقط از بالا دستور گرفتیم و مشخصات فردی دانش آموز رو دادیم تا براشون درست کنن!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72794" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72793">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unmr_ge4zKI1yBvHZlfOGpJZGMVjsqke3FFqv_9uJZ8aUiI5SoxjexZzFO1uVset4HeLCIPp6Ybw6CI8zRKJ5sNuf8vSxBWwwAFzylxWxFu56skFqp4behyjaAJoV-Vi3K5q-ZC80vPI-y1HgQls0Ruj-7hJIKYf5rcGYIf5Uirp26JKoDWmkDqpEirIyM2iUmbjKEqV26Rwoq2_JCAmN6Xq74n7pgjDe6cJ3a_IIsi3BiZTkwSG7aRXTRgaw-qPQDVk3WBzdtlzizgV13qGgROrygo-BIRfONQsZwBFefhLR8toE4QXNxJd6_bAkgERkoMehwh_TJl4vKtf62ZDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
آنچه باعث افزایش قیمت بنزین می‌شود دیگر تنگه هرمز نیست — چرا که اکنون حجم بی‌سابقه‌ای از نفت (بشکه) تقریباً به‌صورت روزانه(از تنگه هرمز)عرضه می‌شود
.
بلکه مسئله «پالایشگاه‌ها»ست؛ جایی که پالایشگاه‌های روسیه توسط اوکراین منفجر می‌شوند و پالایشگاه‌های ما در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط «دموکرات‌های احمق» تعطیل می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72793" target="_blank">📅 20:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72792">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902f67b684.mp4?token=SQf3A_PTHjal1mIgZrHKa6fjebj7QPPsLrTnJlFjSUC1t67wtWrgtoMMcJXiGTqy1cQih-oGdJXsMNCYC1_VVyTqV9rWqLkCIziNlxObuv9nQa8JYFZx4pzb22gFMg7N228GNs60T7B2zxCrfzSlLVtqGtnuzHi0sx_lh8J_O4v9Mftw6T0LOuoBOLzI8HPJYQCOYB729GJpWi-Kee7SCj7Pmj-VhZ5LghuKmDtq7Z0ndY0DmmQeHG3Tsm7dxAcRdwgpffM-jMls6Dmg2dbBfv6p6HMqXmLrKQvK71PtLkvZuuTsGYnwIrdMYEIpHD0jMks2HgInFnJncRNGkWJBZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902f67b684.mp4?token=SQf3A_PTHjal1mIgZrHKa6fjebj7QPPsLrTnJlFjSUC1t67wtWrgtoMMcJXiGTqy1cQih-oGdJXsMNCYC1_VVyTqV9rWqLkCIziNlxObuv9nQa8JYFZx4pzb22gFMg7N228GNs60T7B2zxCrfzSlLVtqGtnuzHi0sx_lh8J_O4v9Mftw6T0LOuoBOLzI8HPJYQCOYB729GJpWi-Kee7SCj7Pmj-VhZ5LghuKmDtq7Z0ndY0DmmQeHG3Tsm7dxAcRdwgpffM-jMls6Dmg2dbBfv6p6HMqXmLrKQvK71PtLkvZuuTsGYnwIrdMYEIpHD0jMks2HgInFnJncRNGkWJBZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا توانایی خودشو توی بسکتبال هم نشون داد و تقریبا همه توپاشو سه امتیازی وارد سبد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72792" target="_blank">📅 20:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72791">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=DLdWEpJzFCvGf29TfrvSOQCYia688RXPdhGL90rRz8hyfz5v3wC1VPK2KDVedjP35GkixJ3LA-9L9kHQy4sKaFxyZ3XBEwpCSBkRmPaovkpV72lPtd6rUOqw3EB9NDaDvDMsEpVFWZ7ip1t75ELo7YTsxVgVroqcUAbJL-arzO1nOi_chOTmyTag0vUUVagF64KGT62fPL7MT_R4huxmT8oGmxeGgvsznu_1zSlG4yfodjtO9YHeyySLasjQw18v_AVVV6DJzcY9Nx-6CjuwBZH0gCgiHaAEvzK5SBuZAOKQIMZfsLX7a2oj5iPADf5q4a3Fuw9EVChbU5ZZ6dpo7wvNPqml1TB0BKx427e9FE_nNIQvCbnzD9AkumeaNHiONTNmCY_21Hlq2NOGeBzKQlQ_KlyMAG1H4NoeP1YXY0yeumELf3VK-m8rMM0_Ab9S5nsiQneyWfn5MfhVhsyb0ngBi5K-L0UYq3NzVzbRxskNLv_Ayq8fVz3_w-XuP_hCbIDMJv0UCic6r2LU5TfoyfUg3R8BYgRxkk67QfIpFRDHwM4QgFMKWwGJuqc4Ltlk4yYyHI2kiwxho_KzVPdgpr3vBeZ7tDkNuLAh0pVoh_RnGTraBKY1P8CFBmZNt8SHc4NXAg-FmMia5aUuGNhbOLsKk3u_nyyJmpKfQrsxpJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=DLdWEpJzFCvGf29TfrvSOQCYia688RXPdhGL90rRz8hyfz5v3wC1VPK2KDVedjP35GkixJ3LA-9L9kHQy4sKaFxyZ3XBEwpCSBkRmPaovkpV72lPtd6rUOqw3EB9NDaDvDMsEpVFWZ7ip1t75ELo7YTsxVgVroqcUAbJL-arzO1nOi_chOTmyTag0vUUVagF64KGT62fPL7MT_R4huxmT8oGmxeGgvsznu_1zSlG4yfodjtO9YHeyySLasjQw18v_AVVV6DJzcY9Nx-6CjuwBZH0gCgiHaAEvzK5SBuZAOKQIMZfsLX7a2oj5iPADf5q4a3Fuw9EVChbU5ZZ6dpo7wvNPqml1TB0BKx427e9FE_nNIQvCbnzD9AkumeaNHiONTNmCY_21Hlq2NOGeBzKQlQ_KlyMAG1H4NoeP1YXY0yeumELf3VK-m8rMM0_Ab9S5nsiQneyWfn5MfhVhsyb0ngBi5K-L0UYq3NzVzbRxskNLv_Ayq8fVz3_w-XuP_hCbIDMJv0UCic6r2LU5TfoyfUg3R8BYgRxkk67QfIpFRDHwM4QgFMKWwGJuqc4Ltlk4yYyHI2kiwxho_KzVPdgpr3vBeZ7tDkNuLAh0pVoh_RnGTraBKY1P8CFBmZNt8SHc4NXAg-FmMia5aUuGNhbOLsKk3u_nyyJmpKfQrsxpJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره خروج هر ۱۲ فروند بمب‌افکن «بی-۱» (B-1) از پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford):
آنچه در آنجا شاهد بودید، اقدام وزیر دفاع برای محافظت از نیروهای ما بر مبنای احتیاطی مضاعف بود.
ما با اطمینان نسبی معتقدیم که ایرانی‌ها در پی انجام همان کاری هستند که حکومت ایران طی ۴۹ سال گذشته انجام داده است؛ یعنی ارتکاب اقدامات تروریستی علیه ایالات متحده و همچنین علیه بسیاری از افراد دیگر.
ما نهایت احتیاط را به خرج می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72791" target="_blank">📅 19:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72790">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMRUtVpSssXKddJ815powt2pM3APVTs5eIlY2qsvLw-7zgW-ailHmyCS8SW7IY4maMs8mmfvdzkMryVcZhGT9N-g-OQgc7qFOTqTD0ZMzOQ71jbW1LCa_AEESt38xmu_PldNxg8DYWDctPv60BG8UCsL7-YAAyfpNx_3HgZG70N5XUTpaO9GOoe00CQtnBZNYpQXu0UNoCYpAEE93hXQ6IP3t1bxfvujZclcb8LoCQHzhp6pEfIRT37xP3kANHGBoggW96iLaHFof7u_xxhlwD43h-4hda1hSR9GrbdtdEhsgeCi8ncK0yieLWohm7YqnxbDYXnZ9DNmz10_0K4yYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.
پوکت نخستین بندری است که این ناو از زمان ترک ایالات متحده در ماه مارس در آن پهلو می‌گیرد؛ قرار است کارکنان آن از ۴ تا ۹ اکتبر برای گشت‌وگذار، فعالیت‌های فرهنگی و برگزاری یک مسابقه فوتبال میان آمریکا و تایلند، در خشکی حضور یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72790" target="_blank">📅 19:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72789">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=QxL3s-Q0QxjTMFEcqWp7cg8BUtzKhT5GyyTMMn7s6RdWy3nCUg6Ca_egGVKtXfbgldMl21SxTQy3dYAxLyCtNs2ZLoxGHKZASrkSvbH01WQ9u0dnjliciEehcNOnWeL50o3mDM31mh8u8rjeqzN71cMcOFBMjOZBwTf_ys9lYqN44HR3wT91MaoxJKdQhVxC4zKB_j2KJLRVJrjJAklucv69q1eZzn8D2_iDGUCFZIYMPJQlBqvPUQEtT-F97Gbx05U0jkb4oB7OOYuXc-kDEb_YejZz7YgWs8Zk_178L1XAdt4i7xLF8elnN6l4l1MSi5Euj00VkitMoe54VQvN_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=QxL3s-Q0QxjTMFEcqWp7cg8BUtzKhT5GyyTMMn7s6RdWy3nCUg6Ca_egGVKtXfbgldMl21SxTQy3dYAxLyCtNs2ZLoxGHKZASrkSvbH01WQ9u0dnjliciEehcNOnWeL50o3mDM31mh8u8rjeqzN71cMcOFBMjOZBwTf_ys9lYqN44HR3wT91MaoxJKdQhVxC4zKB_j2KJLRVJrjJAklucv69q1eZzn8D2_iDGUCFZIYMPJQlBqvPUQEtT-F97Gbx05U0jkb4oB7OOYuXc-kDEb_YejZz7YgWs8Zk_178L1XAdt4i7xLF8elnN6l4l1MSi5Euj00VkitMoe54VQvN_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)  تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72789" target="_blank">📅 18:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72788">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)
تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون از دست می‌ره (کنترل شهر مهم تعز همچنان به دست حوثی‌هاست)
#hjAly‌</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72788" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72787">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حوثی ها دو موشک را به سمت منطقه ای که تحت کنترل نیروهای دولتی یمن بود شلیک کردند.
در همین حال خبرنگار شبکه العربیه در حال آماده‌سازی برای پخش زنده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72787" target="_blank">📅 18:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72786">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crQrINOsqdz3mOHl3ddlXHzMIEWho8qdF_HMwbARIRBChwbZVzAZcjiq2nIkkV_MA5UBAYWkZOGts_wNxYMJjsRfa9EL4KzxigHzbiY8Ivv43HYCDLC_4AaVVMYP4x7dBz3i3FknzvBmc8u4mzZGSuMi8hN4jkKPDYq3aDhmWdaYD5KeMAwVzF5BEN7_Gf0Wc3vcSFEnmy21O7aN2337Bz0mbLLOzXbU09JTErcnEB5f_R21AvrnN67fOzqFuggsRpujq6_O2AkXzjjEk-sVEM2JnBmZNwgASQfJuymkd3VU9d3FrjsMy0HsIpoSaldvGiljaQsdWJ8pZVw3IYedIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛
مشاوران ارشد امنیت ملی ترامپ نشستی محرمانه و چندساعته را در «کمپ دیوید» برگزار کردند تا درباره احتمال جنگ با ایران و درگیری میان عربستان سعودی و حوثی‌ها در یمن گفتگو کنند.
ریاست این نشست بر عهده معاون رئیس‌جمهور، ونس، بود و مارکو روبیو، پیت هگسث، استیو ویتکاف، جان رتکلیف (رئیس سیا)، ژنرال دن کین و اسکات بسنت (وزیر خزانه‌داری) نیز در آن حضور داشتند.
یک مقام آمریکایی اظهار داشت که در این جلسه درباره مسائل عمده خاورمیانه «تصمیم‌گیری شد یا دست‌کم بحث‌های عمیقی صورت گرفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72786" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72785">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72785" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72785" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72784">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaH8oI4A7bW_Fn_iOpCPmoZYl8q1tqWBaPNxyeBrMwCOCrZ-1e5lV2Q8qakRMjZYhOLkKWmzzkuEzgRGsVJO6in63uNjtoLuLtmptBsPbR9Wywuc1AR1yYHek0i27hlJqkHq3mR5QjsDuuivpZoNw9Y7uPrXsPZiJKNNq4-yy81Sn35N6bHGcaV-Vzu3A6C1Fi9WzieNMZx3ZC8FCJZId7ZE5RZDGQLT_zoMD54jiQDh6gulnwmC89PSmdcMr0gusMhKt5vkFEn2XSylm_2gvKvlS-VyGHVjKYWxFtM9k9BcUSsvi8pNW1N5uxPQGESJN3Cemis8FPpheoWmXLj0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز بلژیک
🆚
فرانسه را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بلژیک: ۳ برد، ۲ شکست و ۱۰ گل زده
فرانسه: ۲ برد، ۱ تساوی، ۲ شکست و ۷ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72784" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72782">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=kCxHKeFtyD3exLNmBLbDPuaieM-v5NjVcIYXZr0ApGUlO3nWOL6pIteQ1QUDTibs0QiVv4dsQpusLKPOjh9r8_1yo6PVYpjriznsgdSSO_58w-lRO-5lsvK-RQADgGtxJJ0hLG0btb0dyqdacsxcwc35YlNRNJfSU9EQZhrElpd_znRhUpK9BSR3BYvtuvgqqiBDZcEMBhXhj0dGTCkzt7jPzpoiIzhaI_MI7-bX_lRQ6Y4U9csL0f_GzMBU5AHI4d0fv4IgcD3BDFl3t7MFQpr0kOXXzv8VzfMu9yJNDq7qwTCHuVmJ9eGU_RjtcXz0x3MPjrJyuhpW_RUPRqaXPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=kCxHKeFtyD3exLNmBLbDPuaieM-v5NjVcIYXZr0ApGUlO3nWOL6pIteQ1QUDTibs0QiVv4dsQpusLKPOjh9r8_1yo6PVYpjriznsgdSSO_58w-lRO-5lsvK-RQADgGtxJJ0hLG0btb0dyqdacsxcwc35YlNRNJfSU9EQZhrElpd_znRhUpK9BSR3BYvtuvgqqiBDZcEMBhXhj0dGTCkzt7jPzpoiIzhaI_MI7-bX_lRQ6Y4U9csL0f_GzMBU5AHI4d0fv4IgcD3BDFl3t7MFQpr0kOXXzv8VzfMu9yJNDq7qwTCHuVmJ9eGU_RjtcXz0x3MPjrJyuhpW_RUPRqaXPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جنجالی کوچک‌زاده مجلس :
کدام کارمند و مردم عادی پول دارد ۲/۵ میلیارد تومان بدهد ده هزار دلار بخرد، این پول زیر متکای امثال همتی و دزد‌ها و اطرافیانش میرود.
آقای قالیباف، چرا مملکت اینطوری شده که راننده رفسنجانی هر کاری می‌خواهد در این کشور می‌کند؟
طرح جدید بانک مرکزی؛
هر ایرانیِ بالای 18 سال می‌تونه تا 10 هزاردلار (۲ میلیارد و ۷۰۰ میلیون تومن) از بانک بخره!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72782" target="_blank">📅 17:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72781">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=VL_WkK8jjAGqWinQml6_1lvZC9mpug9YCH0-2Sm349Zj-6HZTHLroFTg3wrguGMzKL9cd_QZ5ubpKttOJDQiyB0-EP4UNerjcSaIOWKeFNxib1yK_oDjNoPayIvLP85V5wKw6uaxv7BkvsGSzW_OZMOMhnkQHLGbI4yB54KUcUpMh6SO9eD92Ig3bpXLdKWPoqEvwm-1dS8BKOFsFemEMx-X4jX3x6RZWz3z6JUIjNEm9wI5r29w3_5m3qEw2ZxG460WTLDm5b58Eay-a16ATyizeyRgnVbc74fSIO0Oe2v8ju3_6rddLuktWhl5kkM9WJt9f2fX9bTwZfAYu0iX17G398jv5NhgJtZla8idDUYKUxJOTvqMetPu9hAIzNY6qKH9Y77p-ePgL0xac_HBidXp5pvn6a2PL63neVk0EAwQXuFjvLREO6V57ipZpEm1nN-u-vOq7tX4gJTsW7myOmnUQl97R2DCXVZ7bmW8SQgyR83Cxx-PmwaMe-b1JmVd-xDkIHq_pAczLV8Wvzdd3Hn2Dp_ORY9MPcXTI1iAGOTyXm95D_1nWfIGVsWmY7XJ8_aAz6E7vfMJUJ3GRM8AEQuX7Xx-RFfKgAYanR819w9KrWLGN2gsxny6CpnMnm6GrcIsvE8H0ppekmMoPQL-tS-msMY64cvuJAzzsQW9kQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=VL_WkK8jjAGqWinQml6_1lvZC9mpug9YCH0-2Sm349Zj-6HZTHLroFTg3wrguGMzKL9cd_QZ5ubpKttOJDQiyB0-EP4UNerjcSaIOWKeFNxib1yK_oDjNoPayIvLP85V5wKw6uaxv7BkvsGSzW_OZMOMhnkQHLGbI4yB54KUcUpMh6SO9eD92Ig3bpXLdKWPoqEvwm-1dS8BKOFsFemEMx-X4jX3x6RZWz3z6JUIjNEm9wI5r29w3_5m3qEw2ZxG460WTLDm5b58Eay-a16ATyizeyRgnVbc74fSIO0Oe2v8ju3_6rddLuktWhl5kkM9WJt9f2fX9bTwZfAYu0iX17G398jv5NhgJtZla8idDUYKUxJOTvqMetPu9hAIzNY6qKH9Y77p-ePgL0xac_HBidXp5pvn6a2PL63neVk0EAwQXuFjvLREO6V57ipZpEm1nN-u-vOq7tX4gJTsW7myOmnUQl97R2DCXVZ7bmW8SQgyR83Cxx-PmwaMe-b1JmVd-xDkIHq_pAczLV8Wvzdd3Hn2Dp_ORY9MPcXTI1iAGOTyXm95D_1nWfIGVsWmY7XJ8_aAz6E7vfMJUJ3GRM8AEQuX7Xx-RFfKgAYanR819w9KrWLGN2gsxny6CpnMnm6GrcIsvE8H0ppekmMoPQL-tS-msMY64cvuJAzzsQW9kQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: چرا بمب‌افکن‌های آمریکایی پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) را ترک کردند؟
روبیو:
مشاهده چرخش نیروها و جابه‌جایی تجهیزات، امر غیرمعمولی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72781" target="_blank">📅 17:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72780">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=s6fbKzWD3tFPIplWY3wBOGX12Eus_BRICBHzcFDXsQJ2wJ_jq5Am8zGHmnZrvAjKPkOo5lV6qSMet4pA1UeYUenNvzS7467ZxslroDBOgoIk8roxV8vao6aflQqOBqlkE4lPgalotlw3hCxO-_aOkDrWH5_XWJ_hyCC7Iv5nvE8JfUKylwtWEtLtQnQvAVtZgNAxAPrX1KbfTvPYItlfSN_j3KglFSgzpUq0TWZ5srOk1bdYP9gwkxAaiJkFMf5yMnctQcQvqHeFBtaHGRPRw2-N3M-6Bi2k-Es19zity1k-ixB2GyKhnA8uXuq6pgvsmWo9OjoR9JBEbi3PAiYuXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=s6fbKzWD3tFPIplWY3wBOGX12Eus_BRICBHzcFDXsQJ2wJ_jq5Am8zGHmnZrvAjKPkOo5lV6qSMet4pA1UeYUenNvzS7467ZxslroDBOgoIk8roxV8vao6aflQqOBqlkE4lPgalotlw3hCxO-_aOkDrWH5_XWJ_hyCC7Iv5nvE8JfUKylwtWEtLtQnQvAVtZgNAxAPrX1KbfTvPYItlfSN_j3KglFSgzpUq0TWZ5srOk1bdYP9gwkxAaiJkFMf5yMnctQcQvqHeFBtaHGRPRw2-N3M-6Bi2k-Es19zity1k-ixB2GyKhnA8uXuq6pgvsmWo9OjoR9JBEbi3PAiYuXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آترینا فرحمند رتبه یک کنکور تجربی ۴۰۴، پارسال همین موقع:
دخترا خیلی خفن‌تر از پسران، من مطمئنم رتبه یک کنکور تجربی سال بعدم دختره.
نتیجه:
توی کنکور تجربی امسال از ۱۰ نفر برتر، ۹ تاشون پسرن و رتبه یک هم پسر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72780" target="_blank">📅 17:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72779">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=iVIN_pYP7hCgxJRebRlSVLCOVniLmR3Jpnjf-h3kJx6wOSeepg5wA9yRlUSyHoL39ZFedLfI9xDkhyeFy1FDmosvowAxwDy_WBLvFF2FlrRr_bPBcTnKtC-Y-QErUvXPCCf8KYFTR9BZXiPSyRwjfghn0F154GXNn3zbNhSI0BVtWkDZ0AYfIqXQVMxDzSWSEwpvaXp7kEePZ8OlvX2E6LJ2-T7rP49t0Hs2ST9zBmjvfS8-143wEdwKioup3--aUi39x5_4W-Eo0xHwmxguNQ0q2tBNZqEY9DvVl8-5anOUF8n5drhacbqcaCaeJYfT-sYyK5qmwh5frxHhCBTySJ8k09wgMf8hXHPILRBJAIh44bqXB-NoIso-K4dgc0qYelc_67KZ-qE--ED5azFi1GMNwKlA0IlJgHKVEyYK3j1Fo_p_xQfKuDlC2Lbd4bq88kfGi-7uwnWQa8yWGDIuxQhcM2ysfQ6C51jVv3ueTqxr7Hi4TuKZZtp-LFOgH7BisbFQZbO5iQfHvCd_Zu99LfgpNwm6fsNyrc7G1SrVJdGVZqnFOJFL5rEfzoNsUUcHbq5OH1X3RCr-ekagIZlcCfrVlpaekGKD2DNDIYX4yrzjSNNFNm2sIOMmdqZ5lNSDsss95xuK7y1iQjzpvxWsNEGSqhqlziJk6Z4gMQbz-fs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=iVIN_pYP7hCgxJRebRlSVLCOVniLmR3Jpnjf-h3kJx6wOSeepg5wA9yRlUSyHoL39ZFedLfI9xDkhyeFy1FDmosvowAxwDy_WBLvFF2FlrRr_bPBcTnKtC-Y-QErUvXPCCf8KYFTR9BZXiPSyRwjfghn0F154GXNn3zbNhSI0BVtWkDZ0AYfIqXQVMxDzSWSEwpvaXp7kEePZ8OlvX2E6LJ2-T7rP49t0Hs2ST9zBmjvfS8-143wEdwKioup3--aUi39x5_4W-Eo0xHwmxguNQ0q2tBNZqEY9DvVl8-5anOUF8n5drhacbqcaCaeJYfT-sYyK5qmwh5frxHhCBTySJ8k09wgMf8hXHPILRBJAIh44bqXB-NoIso-K4dgc0qYelc_67KZ-qE--ED5azFi1GMNwKlA0IlJgHKVEyYK3j1Fo_p_xQfKuDlC2Lbd4bq88kfGi-7uwnWQa8yWGDIuxQhcM2ysfQ6C51jVv3ueTqxr7Hi4TuKZZtp-LFOgH7BisbFQZbO5iQfHvCd_Zu99LfgpNwm6fsNyrc7G1SrVJdGVZqnFOJFL5rEfzoNsUUcHbq5OH1X3RCr-ekagIZlcCfrVlpaekGKD2DNDIYX4yrzjSNNFNm2sIOMmdqZ5lNSDsss95xuK7y1iQjzpvxWsNEGSqhqlziJk6Z4gMQbz-fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا می‌توانید آخرین وضعیت مورد مشکوک به طاعون در روسیه را به ما بگویید؟
مارکو روبیو: ما به‌دقت وضعیت را زیر نظر داریم. فکر نمی‌کنم این مسئله جای نگرانی داشته باشد، اما نیازمند توجه و تمرکز است و ما نیز همین کار را انجام می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72779" target="_blank">📅 16:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72778">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a15378585.mp4?token=uAuvo9mTESrDD6OgoZtmZQGPYUXEDn3l_DpkcoZa0ygz8SFC8EJ0zkV2If8iv7z5UBIP-LxWBFPncEW8BUGfNg3mWS0HDtVaf7dGk9nF5yiJLJumhB6d4cnllk_D2Q6YQXoFaGFqvpk5hK98JPaoiIkH4BZCPuVokxOCKh-O-wrq3V8vPdrWgDIKK1-ekCrsDaGoJWauqagHbtAZD_Ud5fxfC61MCyM9QuH8hTyCVPYkcVtI291VMBGL6qQnfJUMZNYiDr3JGZy4AUJLyi4y9qnP6nnEMaPOK8e-_ATivf4g7xIVgGlOu3G50H97iZaJGyLDgNRM_AmMmZD70aEDV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a15378585.mp4?token=uAuvo9mTESrDD6OgoZtmZQGPYUXEDn3l_DpkcoZa0ygz8SFC8EJ0zkV2If8iv7z5UBIP-LxWBFPncEW8BUGfNg3mWS0HDtVaf7dGk9nF5yiJLJumhB6d4cnllk_D2Q6YQXoFaGFqvpk5hK98JPaoiIkH4BZCPuVokxOCKh-O-wrq3V8vPdrWgDIKK1-ekCrsDaGoJWauqagHbtAZD_Ud5fxfC61MCyM9QuH8hTyCVPYkcVtI291VMBGL6qQnfJUMZNYiDr3JGZy4AUJLyi4y9qnP6nnEMaPOK8e-_ATivf4g7xIVgGlOu3G50H97iZaJGyLDgNRM_AmMmZD70aEDV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره یمن:
به‌نظر من، سعودی‌ها و نیروهای یمنی به‌وضوح مخالف آن هستند که حوثی‌ها کنترل آن منطقه نزدیک به تنگه را در دست داشته باشند.
این منطقه در پی تهاجم حوثی‌ها به تصرف آن‌ها درآمده بود و اقدام کنونی، واکنشی متقابل به آن است. ما انتظار چنین اتفاقی را داشتیم و همین هم رخ داد.
سعودی‌ها هدف حملات حوثی‌ها قرار گرفته و متوجه تهدید ناشی از آن هستند؛ از این رو، حق دارند که از خود دفاع کنند.
نیروهای یمنی تلاش خواهند کرد تا مناطقی را که از آنجا بیرون رانده شده بودند، بازپس گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72778" target="_blank">📅 16:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72774">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=mUGEm8qkuo7EDXulXxG0NBlp8GvzGN50I2EZHMmev-6-AeSkCuShOo4njIi2UMxRGWTkBouUFSwcx4ISfm1BIh33Rv0fu9m_dPp-7WEBZ-xUwTyiGuFFrmTvtj2ECu-4gysIFy5mXOxH_5X90OKSn-CLd-AMygQvuIFkRiL89_vhMEnkvUMaDq5D8iVE-AK0QdDe5WC1IHmgtBwG5gnukNFBnqcAjrqfBlMgKsHLGBwPkg-h6r3d9D7kevOv0_O2bwZZA_-o4PLFtdWuWzDQjfJcar822XIwUJtQJ62idc4NgKb8PQay7-i4jBq_42c1tu8GCUqDX-7LvGp4OmR7UwQtFOdQBrxN1CnW-jyKi96XTtVR0xl68cPM_Z3I89bi_00W206q3Yvnr-YwYKHqOdiDdz2VqxCLaSBmzpWHJAVAGFHI0tC77vY2nWkNRrvSKxRiEPMtpbYuOx8XIW6sC-KBo6eZ9MaUIIwcWD3psiFHLVhSKhjT0x4iNDFqZZFvVJunjVHILSuT2u-rBQNzvARUmB7Ua_QjwtY0gzCKHYj6RJszjpzEa4YE_gs9Nk7_PTMgxGrQips4zRmfUfAbn6_cMOqHVXZ4q96LNjnoLKU2tXYq9IsW7RIbdg36cbnC6rBAOfDJeyBm-YN-CKLmT6Fnh8j7XfoF62KswGJqQ0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=mUGEm8qkuo7EDXulXxG0NBlp8GvzGN50I2EZHMmev-6-AeSkCuShOo4njIi2UMxRGWTkBouUFSwcx4ISfm1BIh33Rv0fu9m_dPp-7WEBZ-xUwTyiGuFFrmTvtj2ECu-4gysIFy5mXOxH_5X90OKSn-CLd-AMygQvuIFkRiL89_vhMEnkvUMaDq5D8iVE-AK0QdDe5WC1IHmgtBwG5gnukNFBnqcAjrqfBlMgKsHLGBwPkg-h6r3d9D7kevOv0_O2bwZZA_-o4PLFtdWuWzDQjfJcar822XIwUJtQJ62idc4NgKb8PQay7-i4jBq_42c1tu8GCUqDX-7LvGp4OmR7UwQtFOdQBrxN1CnW-jyKi96XTtVR0xl68cPM_Z3I89bi_00W206q3Yvnr-YwYKHqOdiDdz2VqxCLaSBmzpWHJAVAGFHI0tC77vY2nWkNRrvSKxRiEPMtpbYuOx8XIW6sC-KBo6eZ9MaUIIwcWD3psiFHLVhSKhjT0x4iNDFqZZFvVJunjVHILSuT2u-rBQNzvARUmB7Ua_QjwtY0gzCKHYj6RJszjpzEa4YE_gs9Nk7_PTMgxGrQips4zRmfUfAbn6_cMOqHVXZ4q96LNjnoLKU2tXYq9IsW7RIbdg36cbnC6rBAOfDJeyBm-YN-CKLmT6Fnh8j7XfoF62KswGJqQ0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دولت ائتلاف مردمی یمن می‌گوید نیروهایش باب المندب و فرودگاه ذباب را طی یک ضدحمله با پشتیبانی هوایی سنگین عربستان سعودی از حوثی‌ها (انصارالله) بازپس گرفته‌اند.
سرهنگ ماجد النزیلی، سخنگوی ارتش، گفت که تیپ‌های غول‌های جنوبی و نیروهای سپر ملی، این مناطق را به عنوان بخشی از عملیات «فجر یمن» ایمن کرده‌اند.
نیروهای تحت حمایت عربستان سعودی در حال پیشروی به سمت مخا هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72774" target="_blank">📅 16:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72773">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=GKPSROKvgZW5aFlEcP7KMqVpPLXhVocXKgSuOEEG86yEbcj_syTrbhc3EP2DNtK-3Iokqxe8UfysLTkwI4zIsq3BTvlvEZOCaEPxxLVVL78ZgtkluI35GFoFpyBBqssBSl5sFPvprgtumdk52_RBrOxkyt94VmxylzTtNLS3JlwgFxXgq6BWYWdr24uxqJ2PG8FagPAO6QGeXAgdLaWKSIbhzpt_e5TRBvPaLOU5nqcFP3uV4M_RbCrBGusYjbHU02LIcTe0HGYQCDc8_Mlq1XFqJUOMTrgdxzjThpHu4ngN_znVWNrBClJNFNNEm-InUjk57vwrn1pQI1bpoc3d1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=GKPSROKvgZW5aFlEcP7KMqVpPLXhVocXKgSuOEEG86yEbcj_syTrbhc3EP2DNtK-3Iokqxe8UfysLTkwI4zIsq3BTvlvEZOCaEPxxLVVL78ZgtkluI35GFoFpyBBqssBSl5sFPvprgtumdk52_RBrOxkyt94VmxylzTtNLS3JlwgFxXgq6BWYWdr24uxqJ2PG8FagPAO6QGeXAgdLaWKSIbhzpt_e5TRBvPaLOU5nqcFP3uV4M_RbCrBGusYjbHU02LIcTe0HGYQCDc8_Mlq1XFqJUOMTrgdxzjThpHu4ngN_znVWNrBClJNFNNEm-InUjk57vwrn1pQI1bpoc3d1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات خلبان هواپیمایی زاگرس در خصوص نبود رادار و تاخیر پرواز
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72773" target="_blank">📅 16:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72772">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=mP8wnKprHT6L4_e0v8c6r65m1KJSJa1Ctv29VZr0kzk6Q0Sch9R6427iyFN5gLeNUEWlUF_QsFfI9eqte2SZuc2BUij6omwQ5D2AETDz08uJlBTmmDeO5ri25JXo5rWCOuYmYlT5EPX7tGDgVyJdc-GMV7Bjpo3TkrvaV0jbZdFXuVIcomfnQ0PCo88rfFADlQ2zLwzA_fmiVQi8MyhFsR4CDZ9LBG3UVD5hVwY7EPbfBxtxqtKm4za-DCFveeenk3DccaIAPlFBB6IHr43lP-ak-Rm-jUXYHI_IzK5_JoCxMOk3Nd2teoPLLB05kvmr_Tx27dycX0Br8cMtfl06-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=mP8wnKprHT6L4_e0v8c6r65m1KJSJa1Ctv29VZr0kzk6Q0Sch9R6427iyFN5gLeNUEWlUF_QsFfI9eqte2SZuc2BUij6omwQ5D2AETDz08uJlBTmmDeO5ri25JXo5rWCOuYmYlT5EPX7tGDgVyJdc-GMV7Bjpo3TkrvaV0jbZdFXuVIcomfnQ0PCo88rfFADlQ2zLwzA_fmiVQi8MyhFsR4CDZ9LBG3UVD5hVwY7EPbfBxtxqtKm4za-DCFveeenk3DccaIAPlFBB6IHr43lP-ak-Rm-jUXYHI_IzK5_JoCxMOk3Nd2teoPLLB05kvmr_Tx27dycX0Br8cMtfl06-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی پویش جانفدا: در میان ثبت‌نام‌کنندگان افرادی هستن که اقامت آمریکا دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72772" target="_blank">📅 15:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72771">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=n4qNHRjgfnfZA2DnyqBE2HGmwCzCN-XOLZclniK4sa3vy43soLb3QnqJEQs2KppZ7d06cPS9yduDKYFFaUea27uNblZ6gRPptq-ipJJy_4P1MIcAljIqWtzNb0CFM8zMKrd1GW8Bnn6wQe_zFu7DAAbf6cAp55d9uYalWxxxwBaoJWmVF9s3PxrjEKc-nGj75dXpoffADGToNQC98p5J0844L_ZeFPisvlivGX8Sfnt-24MPy2EYpaM6rdltRYHIYI1VxpC9M5SvGhxyCDhaK-JE0md-vqw_EbExwgAayG-fawWw6menz4Jjku2gJ6hVeItbkbqmdMR_kh-DjxMygA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=n4qNHRjgfnfZA2DnyqBE2HGmwCzCN-XOLZclniK4sa3vy43soLb3QnqJEQs2KppZ7d06cPS9yduDKYFFaUea27uNblZ6gRPptq-ipJJy_4P1MIcAljIqWtzNb0CFM8zMKrd1GW8Bnn6wQe_zFu7DAAbf6cAp55d9uYalWxxxwBaoJWmVF9s3PxrjEKc-nGj75dXpoffADGToNQC98p5J0844L_ZeFPisvlivGX8Sfnt-24MPy2EYpaM6rdltRYHIYI1VxpC9M5SvGhxyCDhaK-JE0md-vqw_EbExwgAayG-fawWw6menz4Jjku2gJ6hVeItbkbqmdMR_kh-DjxMygA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاظمی وزیر آموزش و پرورش:
ما در آموزش و پرورش تمام هم و غم خودمون رو به کار خواهیم گرفت تا اقامه نماز کنیم در تمام مدارس کشور بدون استثنا.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72771" target="_blank">📅 15:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72770">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPQxukFTzdtFAfUo4qzaMluWsaql9J3_pECdh-1MH_Ova3T1L3vLddD590-4u5sQxbULrXfUManQreT3TpC9XPxQBGk8RHZT6AQgxVwHRrzW8nhk3KK_BJ0eA00vaBbWF1pJEGNZI1yTLfJiMBBO2bZfkBX3-4cncgcMkIguZKeHUL8xl8ozFdTvUn55cXkHl38XhhQVOvpqt-SJhRUFZd6Mg4RGjR020O56lK6g-pXyR-ANcbZ7dyg2JHPDEWqJ4XpC1vsR3RHBwQ74iiHYGhQrJDbAXbRYIJld4PfQkED2Pd06WuIPoNeX7rfHCmeBkTh4-KVjYc1ATXNzwHUdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۱۱ مایل دریایی شمال «خصب» در عمان، از سوی سپاه پاسداران مورد خطاب قرار گرفت و به آن هشدار داده شد که در صورت عدم تغییر مسیر و بازگشت، هدف قرار خواهد گرفت.
نفتکش مذکور از این دستور پیروی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72770" target="_blank">📅 14:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72769">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cywGAoB4CyLTPTy36oEAMZKZDVHYRE91K7P95biJfDy3unJ_NczbvEc4VTppt5EgSwbHbmSLKSzE3FNoLe1RT18dECtU0QSHBdEqcC286aprpwivnS6SoraSUPhpc8sFMj5uDERYpwSmfgVvO1NPdnil5FkOQfU4P20NQsu_noX9gK70fScHNqbCpMetfF0ztLtrKFBvAGyLvaSaxRVsDbUDQ_yBZDZDHQZR2mkqlLduinMFXqfAV---f6Ve4jUWRKNfDT7yuakD3pgG0SpUgdlBwV9IJVnCeXV16JEQuq1efyvEL4fcfxefcDdb__YsOFA60KUgMTXfUSWpJqmsIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار در روسیه؛ قرنطینه نزدیک به ۲۰۰ نفر پس از مرگ کارمند مؤسسه ضدطاعون؛
در پی مرگ یک کارمند ۲۸ ساله مؤسسه تحقیقات ضدطاعون در منطقه ایرکوتسک، حدود ۱۹۷ نفر از افراد در تماس با او تحت مراقبت قرار گرفته‌اند و برخی مراکز درمانی نیز محدودیت‌های قرنطینه‌ای اعمال کرده‌اند.
با وجود انتشار گزارش هایی درباره نشت طاعون از آزمایشگاه، مقام‌های روسیه تاکنون ابتلا به طاعون یا وقوع حادثه آزمایشگاهی را تأیید نکرده‌اند و علت مرگ را ذات‌الریه با علت نامشخص اعلام کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72769" target="_blank">📅 13:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یکی از طرفداران پروپاقرص رونالدو:)))
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72768" target="_blank">📅 13:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مسلمانان در انگلیس با برگزاری تجمعی خواستار حکومت اسلامی در این کشور شدند.
جمهوری اسلامی بریتانیا!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72767" target="_blank">📅 13:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72766">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=LgyD0okAI5hTFJ383USNic1CO3lQrqSy69OuAS1AAnIOBtKKwko5uftLEQT2_g4HZG-0furYXZyiuDdWLrs2oqDe6HeXQbl7tCP4htCS9jjNFfg8zaRhqcupEON8NO9PO3Bllp-gWcnIQgDtXRVwLdx6VoZffVU9WAg8DP6-W_1iDmuFuq3EWcqNB8m_-vQCGeOfd2lYUyJghiMDAng0CvQeeZq6MjbGfd2J-F-UI7Cm0pndHFI-xTLnP4xkXkyFTxT6aHFWkzmS35qUZOrf14cs-TTVuDsi_Iw3lEaQUyibQTGpNzf9dY-IVYwMs59m4g0lyQiClGwXbzsUB8QCwFVDiRwkCy7adHZjUL5Er-mWqkT2_3YrqsUmPb06w-JsCl2Z-OPxL23uuousmI4EWM2CZusIBOtoSt5KN2gsCJ1qHncH5_Mv1RmDfYyoTbCY7pYkDIYY0IpFnIH9MR8snpZRR9xHHW4EpfnJMhSeS9TXC4vU6am2f5dx0NG28Il7A5yoHImsKqkUIbqCS9QWoaZewg-xqio2zkYRykJZAtuNWUuO-VYfQz_xJ9u9TSS9_Z1KChudMpUw7HwF83QhJI5LDlE5-4s9EwJGwC-p6aeuAevXnTUn_1CXKWKA_KocloC1d9tHVKxrSgAoeKG-EbK4W8F7D7UcWkuzC7Oa5c0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=LgyD0okAI5hTFJ383USNic1CO3lQrqSy69OuAS1AAnIOBtKKwko5uftLEQT2_g4HZG-0furYXZyiuDdWLrs2oqDe6HeXQbl7tCP4htCS9jjNFfg8zaRhqcupEON8NO9PO3Bllp-gWcnIQgDtXRVwLdx6VoZffVU9WAg8DP6-W_1iDmuFuq3EWcqNB8m_-vQCGeOfd2lYUyJghiMDAng0CvQeeZq6MjbGfd2J-F-UI7Cm0pndHFI-xTLnP4xkXkyFTxT6aHFWkzmS35qUZOrf14cs-TTVuDsi_Iw3lEaQUyibQTGpNzf9dY-IVYwMs59m4g0lyQiClGwXbzsUB8QCwFVDiRwkCy7adHZjUL5Er-mWqkT2_3YrqsUmPb06w-JsCl2Z-OPxL23uuousmI4EWM2CZusIBOtoSt5KN2gsCJ1qHncH5_Mv1RmDfYyoTbCY7pYkDIYY0IpFnIH9MR8snpZRR9xHHW4EpfnJMhSeS9TXC4vU6am2f5dx0NG28Il7A5yoHImsKqkUIbqCS9QWoaZewg-xqio2zkYRykJZAtuNWUuO-VYfQz_xJ9u9TSS9_Z1KChudMpUw7HwF83QhJI5LDlE5-4s9EwJGwC-p6aeuAevXnTUn_1CXKWKA_KocloC1d9tHVKxrSgAoeKG-EbK4W8F7D7UcWkuzC7Oa5c0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای دولتی یمن مورد حمایت عربستان سعودی اعلام کردند که کنترل تنگه باب‌المندب را به دست گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72766" target="_blank">📅 12:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72765">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfzwjkBPOBQvs2s3D1g-2En2w3jew-jl5uzEMImm9GG8lRdUfr_tiykvw5Kg_RdCS3D8pOMW_YmsqAyA08NdxbCq1z9340VFgBUIBfcei15mc7H0Znx9VtC5bAzAAEvExQdeqGlJVGGQ1cJE3bKR0tAkr6snl-MPhQSvOGwVtJ59ekjDGsArOZpU0vZw6-rD9DsqwwterGpmnZo1OOnikLfX5el4_4Izl-OCFLe5knk2bfOPTScbHttBUEVL0WB0sh0i0C210tMyY-m_pl41ePgjwjO_LgicOCH8cJGRZ5HJu7kuprH0CH5s4Rj33zd0so0kjl_mqbE5-vQ-vUHvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72765" target="_blank">📅 11:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72761">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=EbuduhHrGz_KyXZJaorsAls1DkG4lhO1Xn-m2gm8L7hKX4fryFLyB52QP2HyT6vubw9sIRfOCv-aa35nCzdGiauOVjT3nVWKPJM_P26BP2ZrcZsoWEd0ZORITpsLvAB3UJE1-ecmnVBT77SkS15kojo_k3fF_mwnSeCIDbYDGMS815w9A0qYbNkyy8ZGWnucN2ByyU76c5kLjeuqstOBGEcPNJfu4QR7Y7Fdhvy2BVD-0jAPq7wmyPEw3G7Idaatv6xfQzQHQ5lgu_go_R9PdkM9sqp8wWXFp519wRESZiiP3kvPH_7WxCH0MCco1MADxBb8nMUq7CwZT0KkUwY8qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=EbuduhHrGz_KyXZJaorsAls1DkG4lhO1Xn-m2gm8L7hKX4fryFLyB52QP2HyT6vubw9sIRfOCv-aa35nCzdGiauOVjT3nVWKPJM_P26BP2ZrcZsoWEd0ZORITpsLvAB3UJE1-ecmnVBT77SkS15kojo_k3fF_mwnSeCIDbYDGMS815w9A0qYbNkyy8ZGWnucN2ByyU76c5kLjeuqstOBGEcPNJfu4QR7Y7Fdhvy2BVD-0jAPq7wmyPEw3G7Idaatv6xfQzQHQ5lgu_go_R9PdkM9sqp8wWXFp519wRESZiiP3kvPH_7WxCH0MCco1MADxBb8nMUq7CwZT0KkUwY8qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72761" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72760">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72760" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72759">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oy2VZ6EHa48LKBtRlFTPc84wkhoWABqXtK3QIrQn7lLDKkn1-4JS5lMN1q9PVu8NpUyn3-_tSk7xxVhweDQXZJNx6UnZ87G9nXxlOL5bC7CZ6FXiztMMG0LcRScVfRYb7fMAq08BZI_lq7M6z5bGkZsGbo_Q5SQFPexpr3S8bsKiZsgJEGLUMEBT4WslO2pbFHozYHTlhFUVj_0tBU0CSYsNbZmEoDRrWWgNIFn_mY78yJF6yXBUPRh6J75wlEoQHybECICJw2LN3Jb8aWfM1H8tpOmpBTylIsRUTDImbp7bjqgsuZUtAKMZRhWNzyT8yw7IM5ACEICe_A6_rwbFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
فرانسه
ترکیه
🆚
ایتالیا
لهستان
🆚
بوسنی
سوئد
🆚
رومانی
نیوزیلند
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72759" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72758">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=QSCHpKbQGxg7pEqknLjxxRgMPQZGiFHvaPqOD2bnuhzMknKHsCLzP3XKmE6N9NUfGsmPVRBNitqeyl8M1uaJTpfdG9Hr3vGX8hKJZUJiSD6TqVmFCDJFfjWHUcf1Cwz98JGR2uE2yMDsQFHQekFXq5zliEmg_UPoOETuo0mYq5NrmcqSPQR63LNKvizBGozomPVzcaJGV15BF_3mTp_HRstAN4HiGcZqSOfOUm_9NcuPiwrcFcseAYxAQTTUnyzr3bGsWe6Uza_hgdin17dVpFYuPOBSEo6L9oxImWM82PYS1oVXeLDQzL9JhCEq7Lm77dTbRdC8Ury4TXdDLoZXkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=QSCHpKbQGxg7pEqknLjxxRgMPQZGiFHvaPqOD2bnuhzMknKHsCLzP3XKmE6N9NUfGsmPVRBNitqeyl8M1uaJTpfdG9Hr3vGX8hKJZUJiSD6TqVmFCDJFfjWHUcf1Cwz98JGR2uE2yMDsQFHQekFXq5zliEmg_UPoOETuo0mYq5NrmcqSPQR63LNKvizBGozomPVzcaJGV15BF_3mTp_HRstAN4HiGcZqSOfOUm_9NcuPiwrcFcseAYxAQTTUnyzr3bGsWe6Uza_hgdin17dVpFYuPOBSEo6L9oxImWM82PYS1oVXeLDQzL9JhCEq7Lm77dTbRdC8Ury4TXdDLoZXkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
جنگی که توی راهه، آخرین جنگ ترامپ با جمهوری اسلامی خواهد بود!
اما به قدری این جنگ شدید و گسترده‌اس، که جنگ ۱۲ و ۴۰ روزه، پیشش یه شوخیه!
شدت بمبارون‌ها خیلی شدیدتر خواهد بود، کشورای بیشتری درگیر میشن و این نبرد آخره!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72758" target="_blank">📅 11:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72757">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=M63rcixEVrWcV2jjlFRtcv60P-PC0eMFG51AwGLZzzyBf9bB2B-vBj7DRDmdiVGnLsl9o-Uy0ohKX16bxPXu1eazeK12jH6GmQe7IeUJzBxULrEHcewBn85tVKLrPulW6F8I_KXZeN-GmJaNXVm1suDsMv8tePkVGz3lwVxDOYez2uHZQGuBDX3XPJg9Gf2il50JRxDzaJAfS_vC3mji39l-VsGlYgzAyxXVJ5DlboBKKhomKfAMETGLUVSFbMZc7AhqNvQxqmPfGRIHMQlKLr-OQbRcMbmmYmzLm6V0CHYL0g8sdyYwkM4PjDSeK2inF0FmXj4sEtmLm49LuVVdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=M63rcixEVrWcV2jjlFRtcv60P-PC0eMFG51AwGLZzzyBf9bB2B-vBj7DRDmdiVGnLsl9o-Uy0ohKX16bxPXu1eazeK12jH6GmQe7IeUJzBxULrEHcewBn85tVKLrPulW6F8I_KXZeN-GmJaNXVm1suDsMv8tePkVGz3lwVxDOYez2uHZQGuBDX3XPJg9Gf2il50JRxDzaJAfS_vC3mji39l-VsGlYgzAyxXVJ5DlboBKKhomKfAMETGLUVSFbMZc7AhqNvQxqmPfGRIHMQlKLr-OQbRcMbmmYmzLm6V0CHYL0g8sdyYwkM4PjDSeK2inF0FmXj4sEtmLm49LuVVdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره یه دختر تن فروش: یه دفعه یه سید بهم گفت بیا رابطه داشته باشیم، فقط تو زود بیا چون ممکنه خانمم بیاد خونه.
رفتیم تو اتاق و شروع کرد صیغه خوندن، هر چی قرآن، آیت الکرسی، تابلو و کتاب دعا بود برعکس کرد و گفت زشته، گناه داره.
یه دفعه وسط عملیات زنش اومد، گفت سید زودباش درو باز کن خیس شدم زیر بارون، سیدم بهم گفت تو فقط چادر بنداز سرت شروع کن نماز خوندن.
خانمش اومد به سید گفت این کیه؟ برگشت گفت این خانم مسافر بود، اومد گفت نمازم داره قضا میشه، میتونم خونه شما بخونم؟ منم آوردمش نماز بخونه.
آخرشم خانمش بهم چایی داد و کلی پذیرایی کرد و رفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72757" target="_blank">📅 10:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72756">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=LxyBb7EqSGTw95Ze9tjKoM_Q2_zRYpqZATzcQHoT8chyKo-4FkfDYBzgf7aWSQAyli_ZvMaDu4Q_vnJrk444mLmgX-7pd28zTMyMmxTBt5FXrAC-v9RHUcBK1uJ-mMvYJGxBOwpjAva6f7d8Xr3CY8rzeR4KD4o3qABU1ob0WX9VdWD9kmrAG-G41EVKAC7pDWQpKqSKD3bF9gHfwUhqrUO4NJwqJSLFWRp0kmgpzIe2vcxRfJ1I1M9Yc2uoZBk-g3FhOJnSbHoQgt1zGOKXLqcqcPOf7HEt5SUYiYttvtVEg6PMyHOVsLkBpNl_IPubvy8-cUCYaWWlTpMmDLS59w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=LxyBb7EqSGTw95Ze9tjKoM_Q2_zRYpqZATzcQHoT8chyKo-4FkfDYBzgf7aWSQAyli_ZvMaDu4Q_vnJrk444mLmgX-7pd28zTMyMmxTBt5FXrAC-v9RHUcBK1uJ-mMvYJGxBOwpjAva6f7d8Xr3CY8rzeR4KD4o3qABU1ob0WX9VdWD9kmrAG-G41EVKAC7pDWQpKqSKD3bF9gHfwUhqrUO4NJwqJSLFWRp0kmgpzIe2vcxRfJ1I1M9Yc2uoZBk-g3FhOJnSbHoQgt1zGOKXLqcqcPOf7HEt5SUYiYttvtVEg6PMyHOVsLkBpNl_IPubvy8-cUCYaWWlTpMmDLS59w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه عراقی :
به حضرت عباس اگه بگن بین پسرات و جمهوری اسلامی یکیو حذف کن میگم بچه هامو حذف کنید تا فدای جمهوری اسلامی بشن
ایران از بچه هامم ارزش بیشتری داره
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72756" target="_blank">📅 10:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72755">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=hd80LlRVmHn5KAtA_un5O--HWLtuRaGzEsHwCrFvUme9jrRZn4eLgLkNAJzU8EodEx39lvxjPgksvwyjMEqlY98W-BYE-Dhf20QctJmgo52MmbqEihRm2wQa81H8j-O-sMLAXg95jOqOq9milz5KAieL-8oqSYUCBDvPnMyDDyrmNX711Hs1oIkueXZMI975XduWN-bwDvT3hD9d_wVRjVvSosSqcHCx9CCY6hrj0HT2QK9hzCdx6xf77YDqBp_VZLRbJVrPRgQ2YnrlCSZ3itcRZjJQcxj06OnUGPj7gRGPSTFs0nFf7I2SwZk5B6ZSyrJ9Ynj_NDPgzjDMdWkSNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=hd80LlRVmHn5KAtA_un5O--HWLtuRaGzEsHwCrFvUme9jrRZn4eLgLkNAJzU8EodEx39lvxjPgksvwyjMEqlY98W-BYE-Dhf20QctJmgo52MmbqEihRm2wQa81H8j-O-sMLAXg95jOqOq9milz5KAieL-8oqSYUCBDvPnMyDDyrmNX711Hs1oIkueXZMI975XduWN-bwDvT3hD9d_wVRjVvSosSqcHCx9CCY6hrj0HT2QK9hzCdx6xf77YDqBp_VZLRbJVrPRgQ2YnrlCSZ3itcRZjJQcxj06OnUGPj7gRGPSTFs0nFf7I2SwZk5B6ZSyrJ9Ynj_NDPgzjDMdWkSNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار :
از آقا مجتبی (خامنه‌ای) چخبر؟
حداد عادل پدر زنِ مجتبی خامنه‌ای :
سلام میرسونن...انشاالله خوبن...همیشه...خوبن الحمدالله
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72755" target="_blank">📅 09:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72754">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e173a359.mp4?token=JxluhMZLxVMHeI5rjSmfIkHXqv1Iah_cla1E6YIkzzWIDfTnO2yoamCW7Snm4YxJhxHWU17Q4pQmWSW80y4wJtdIeoViGn9RV0FpVs2mu2ROyUyBMUqBuZxyqD8EhCvhaXAs_7gMCxiGo0l3bJY4xPFkUB26VqVEbq_DGcvsvk0GUKfwI0PcjqHgw6gRawSvm0rgkbu2u-06-emixlAHuURc4K-CCVnudDHbzPdBekCwycEw634nriqkldneJqvQarz9riwqx9dhrAzjV8dZPrJOeXT9gJOLMyC7bpNQoBi_wgVrXyMXZDBEp1UI6Hw4JqlLR76gKjDbCjin2GJArQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e173a359.mp4?token=JxluhMZLxVMHeI5rjSmfIkHXqv1Iah_cla1E6YIkzzWIDfTnO2yoamCW7Snm4YxJhxHWU17Q4pQmWSW80y4wJtdIeoViGn9RV0FpVs2mu2ROyUyBMUqBuZxyqD8EhCvhaXAs_7gMCxiGo0l3bJY4xPFkUB26VqVEbq_DGcvsvk0GUKfwI0PcjqHgw6gRawSvm0rgkbu2u-06-emixlAHuURc4K-CCVnudDHbzPdBekCwycEw634nriqkldneJqvQarz9riwqx9dhrAzjV8dZPrJOeXT9gJOLMyC7bpNQoBi_wgVrXyMXZDBEp1UI6Hw4JqlLR76gKjDbCjin2GJArQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حاشیه ختم خواهر عباس عراقچی، وزیر اقتصاد از پاسخگویی درباره وضعیت فروپاشی اقتصادی و کاهش ارزش ریال فرار کرد و خبرنگاران را به همتی، رئیس بانک مرکزی، حواله داد و همتی هم بدون پاسخگویی فرار کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72754" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72753">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72753" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72753" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72752">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEk0NL9jPB5wBxa8VGQBd7KmpFxuPyEZWu-0JmI_CF-hY6XsmwiwTdOgQKlj2Nm1mxkH2OJAKTHKNYh1WisJdB-wys79f9D3JhXNfX0btbWKrTT7KEr-wLYvs_XC2OeNM13nLUC88g63e8YXD3PQebVwyiQ7gYDLVLGZg9YXauNoIpkux-Pb6Uh7kxYwOJM3OuXTm0uTIo46LYT5rQIy7b7qU43MHrKT_XjDBljAxiUN0I3EhBlNf-gTMISThkU2SVeX-FsPqX-nwANU9HiKitqLmZvplOZgtuNxqwa_oVN0TsHZdBQ49o9cMLlSAWj97mNN_TblMO83us05Acj1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72752" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72751">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MY3t79AO46dQLVpoStj5UJvn26ZLsd03k89a09KWInga4FHzoPLQwD4HTI6Xftkb0QGadFIq7pfNpzpd5RrUeuiRN8-IpNRdey1JuWX5kpmFKXfINL6qoUF1REgxKw2m9POVsvtl2UFb8ZxkVpvInWUyI1wHSxZY7_qzPorYdHWPZQynw5MEjPmbxpoN-YlQYk0aFAum1nUnBILglOLnmTWDDGd0mF9b1imbZrxVhRJx8gbNWH3vOH50b-mYIscba8DAeeirAe52OxoKNxAkx0xHgCqsRLuHTu1laBimzoSNbQGzjqAhDkp0xJrLcilY_Gr35_CsJiP9TQkJEz5OLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقامات آمریکایی گزارش داد که بمب‌افکن‌های راهبردی «بی-۱بی لنسر» (B-1B Lancer) در حال خروج از پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) هستند؛ این اقدام به دلیل نگرانی‌های امنیتی و در پی دریافت اطلاعاتی مبنی بر وجود طرحی از سوی ایران برای حمله به این بمب‌افکن‌ها در پایگاه مذکور و کشتن کارکنان آن صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72751" target="_blank">📅 01:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72749">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5pGFPTN91KKZkGjFc3JBg3oCYjFQy_QVLFJbrVs1XtwLYq0W5uARNzbad1k_yhDjTmS1ibv7Lg_rq56AAY17yEnVrDdFg6pQE0Y3wy3YDt9Qd1Sy-vshrDF1j-i9cF77bFcmkdU40o10fnVK8fWUfEKW36iVBtzhseqWSxCujfuEB8Fn19L6LOo71Q6hkq4FMRLSx24RIQEI8nvi--zjPRH3-_bfAX7sR7TBuuk_MP9iMGncI3Ve7uLjCc2kVYma66-3iEp0em21H3PWPTbiK1Q7GemL6sxTFheHX7bId-tZGLXxlYFtW3wazzK-1wmGoMYI9kdRbd3mkPjqpwEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cef955dd4.mp4?token=k0XHTzx5mYB2lmriUWEhwUm1PPpg1s1y7K_yLeHF1T9Drj5YM7r3iHbDScUU2D2u31S_7M8HKozOjaQcG8KiYF-rB1Z0_2JDys-cmqFtaQIt9CW9EI8FC78BLNqHrEAUsgwQy2pI6gFrGD-yuRPrLafEYGzTFI4i2MV34DC5hB1e0uQJsrotBHqUxJ4Co0T4KtWB8jaR8WTlO04WqoAccCpkk373dz95aKK3BSZzkUsOmKXyqxR4jE33j8hoAXmt4lUyqM_YE7qcYdml4lzNwunT9WudQg2yRsb8GlsxTd_eyILNjaMeYKFEESsHyf8rHbTBpv0rmle8rpc4l0QY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cef955dd4.mp4?token=k0XHTzx5mYB2lmriUWEhwUm1PPpg1s1y7K_yLeHF1T9Drj5YM7r3iHbDScUU2D2u31S_7M8HKozOjaQcG8KiYF-rB1Z0_2JDys-cmqFtaQIt9CW9EI8FC78BLNqHrEAUsgwQy2pI6gFrGD-yuRPrLafEYGzTFI4i2MV34DC5hB1e0uQJsrotBHqUxJ4Co0T4KtWB8jaR8WTlO04WqoAccCpkk373dz95aKK3BSZzkUsOmKXyqxR4jE33j8hoAXmt4lUyqM_YE7qcYdml4lzNwunT9WudQg2yRsb8GlsxTd_eyILNjaMeYKFEESsHyf8rHbTBpv0rmle8rpc4l0QY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام
علیرضا سپاهی، از معترضان بازداشت‌شده در جریان اعتراضات دی‌ماه ۱۴۰۴(پرونده میدان علیخانی اصفهان)، به سلول انفرادی زندان دستگرد اصفهان منتقل شده و خانواده او برای آخرین ملاقات فراخوانده شده‌اند.
وکیل علیرضا سپاهی نیز انتقال موکلش به انفرادی و اطلاع خانواده برای آخرین ملاقات را تأیید کرده است.
بر اساس گزارش ها دختری که عاشق علیرضا بوده گفته آرزو دارم باهاش ازدواج کنم و امشب در زندان خطبه عقدشون تلفنی خونده شده
💔
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72749" target="_blank">📅 01:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72748">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLVIRV-0tkqgKCapL03_eT7EbLbT1s7dTP8tonl_Y7EyGMZYs67Pt64S06zpgATO0yvcwBOsfr50xg1Qd8QObbVT8F-sLk0IE8UbDt-5nQWcBcVZH2_R6-FYQLJqk6BQk7qoPdjih-JZcYKxM6ejBUEdECpbPLpiUb4vd2P0RJa9ey8Pc6o51ODB-vNMz3sdeNCU45onSOk7O3sNiFjhex4V9ng4vjOqy9N6oy0h0AGmGfEAnYfizMorhWCCAXQqBKiz9dc_kEpNIS5yBDJMzgode8hgk1IPZP87swMmDIl5vvCFSo0yL90XaAUT3RNlbyy-iFfNtgORSf2sh8z5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید صفحه یوتیوب امیر تتلو:
امروز دادستان و رئیس کل دادگستری صحبت‌های خوبی با تتلو داشتن و اگه گزارش خوبی هم رد کنن، امیرتتلو فردا آزاد میشه و به استقبالش میریم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72748" target="_blank">📅 00:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72747">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72747" target="_blank">📅 00:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72746">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=t_OG9TmK5_Q9bf9yJS2HAjEWe9XIl7MlpYCpWqLXA_YdcWabv6eVJXvOxFqV_D-ecr2_WxUpGi3DIzqCdbtt65FLm9fXvNQG00bqMtq0FGjQrsGn0H-3L_jilAu__ZWEaaIbvs-4pasneSjt6rK5zYTAQ1JMQQie49MMErWY8HYxnkIDNgLib8eLb_ScDlHsn9AfB35OlCB-5WwtS0c6EMt_tlbMw5_Hj9jcY-qkp9L3ski5mRLf0bcSMdvHChfRl2zRwcwUHw0scgDtQc5pxc2-eL-WUSHAk58-99RebiPmbsIJ-BWdb50HlAL90Umaeciltu6LnU3YUhiwBEx0NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=t_OG9TmK5_Q9bf9yJS2HAjEWe9XIl7MlpYCpWqLXA_YdcWabv6eVJXvOxFqV_D-ecr2_WxUpGi3DIzqCdbtt65FLm9fXvNQG00bqMtq0FGjQrsGn0H-3L_jilAu__ZWEaaIbvs-4pasneSjt6rK5zYTAQ1JMQQie49MMErWY8HYxnkIDNgLib8eLb_ScDlHsn9AfB35OlCB-5WwtS0c6EMt_tlbMw5_Hj9jcY-qkp9L3ski5mRLf0bcSMdvHChfRl2zRwcwUHw0scgDtQc5pxc2-eL-WUSHAk58-99RebiPmbsIJ-BWdb50HlAL90Umaeciltu6LnU3YUhiwBEx0NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای عجیب در تجمعات شبانه: حسن روحانی در یک سفر استانی دستور داد برای دستشویی‌اش کولر نصب کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72746" target="_blank">📅 23:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72745">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673e09822.mp4?token=jUBiSCYfSFEGG-Ng3ERDsz_-Zu3PE5aGy3lCg1R1KaOzyDMxA6uenztkbHexL9W9NobMV-7qW9S61H_cy8DIjH0LWVQnpAoxP1s1ltqaweqvaa0AjaaEncbSiFd-6F5uXYpkG6siRzjAQzK_QJUGJrszVKHp1M1bBQd82yQSlHMv55ZQqa811FmOJHuZE6o4rpGUa3SMQdQweezQ-VMEAQtSTQqD-ZegcjDdaA1_IGU-fkj27HtnSfn6Rg4eByiUTcrucZN7ozb_2hqUhJIdhrAH8zdMwbcHHH6AD4lnG0JmCNx3Ur4UegMlGxaslBElcuEyOgl6l8EZ0YkyHoooag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673e09822.mp4?token=jUBiSCYfSFEGG-Ng3ERDsz_-Zu3PE5aGy3lCg1R1KaOzyDMxA6uenztkbHexL9W9NobMV-7qW9S61H_cy8DIjH0LWVQnpAoxP1s1ltqaweqvaa0AjaaEncbSiFd-6F5uXYpkG6siRzjAQzK_QJUGJrszVKHp1M1bBQd82yQSlHMv55ZQqa811FmOJHuZE6o4rpGUa3SMQdQweezQ-VMEAQtSTQqD-ZegcjDdaA1_IGU-fkj27HtnSfn6Rg4eByiUTcrucZN7ozb_2hqUhJIdhrAH8zdMwbcHHH6AD4lnG0JmCNx3Ur4UegMlGxaslBElcuEyOgl6l8EZ0YkyHoooag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سیل اخیرِ گرگان، یه
موش
برای اینکه جونشو نجات بده، این شکلی داشت تلاش می‌کرد...!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72745" target="_blank">📅 23:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72744">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=MEJEPqLoxYsWoGn99EoqLFrIu995HuFPS0ErusrMdzt31TVM66jq5O-w6rj_7qWa7nHaV7XIt8bcvtm8fQfZBnHYyPZiO_3dRa_eush0vY4mXkdQaQ1TLfS9i-JV_hf9_PAAEGV4vuCc183Avr1dU9d5pjIHE4vM6a0uLNN1eAi0KEL6BUoIGRJv0ikzCIfCeABhOW0YxLsKOSCek3iVtoATWMadSVGuCq_ObFXE3rXEjzqav5fHRjDwLzYDAebFcAOxONTOFDzdARVmZO6BPNBCvk7n9qNFRB03ZnShSpmt4sS9A6Xx5EOxl-hTDlVBLvMK0TkA-makNyOMKhCKow3M72cF4HnqZkEmmstDnCkmG5h8sW1FhtEYgg_QI1SGoaK6QDzZU04l_MTx74XKFj3nPtuuWK9YS9wZL8hKCqjB6kSeYUfhwb3k-SLnSA9N-4Qjn_3gHqSGLHu7ltfX0_f48IUM2yCvg5hPwY5gi0Ced1M9AMcDzeRO29vrAC_DxdcQRv2q3pLGeW6mdkDApUYZ6VNdEq9J6v3RLO2YjuyAKi0D5DDTROJ-yHzOzgHFCZRyVkAgioWuNdgUNpprwqad7wyOLJQ3yVWSdK88SWq_gTO9HhdjBI_sbNCgDIwfK9ziaISW_tFIUAJ-WPU_kZzROG-yxuTWuLnVLqb2d7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=MEJEPqLoxYsWoGn99EoqLFrIu995HuFPS0ErusrMdzt31TVM66jq5O-w6rj_7qWa7nHaV7XIt8bcvtm8fQfZBnHYyPZiO_3dRa_eush0vY4mXkdQaQ1TLfS9i-JV_hf9_PAAEGV4vuCc183Avr1dU9d5pjIHE4vM6a0uLNN1eAi0KEL6BUoIGRJv0ikzCIfCeABhOW0YxLsKOSCek3iVtoATWMadSVGuCq_ObFXE3rXEjzqav5fHRjDwLzYDAebFcAOxONTOFDzdARVmZO6BPNBCvk7n9qNFRB03ZnShSpmt4sS9A6Xx5EOxl-hTDlVBLvMK0TkA-makNyOMKhCKow3M72cF4HnqZkEmmstDnCkmG5h8sW1FhtEYgg_QI1SGoaK6QDzZU04l_MTx74XKFj3nPtuuWK9YS9wZL8hKCqjB6kSeYUfhwb3k-SLnSA9N-4Qjn_3gHqSGLHu7ltfX0_f48IUM2yCvg5hPwY5gi0Ced1M9AMcDzeRO29vrAC_DxdcQRv2q3pLGeW6mdkDApUYZ6VNdEq9J6v3RLO2YjuyAKi0D5DDTROJ-yHzOzgHFCZRyVkAgioWuNdgUNpprwqad7wyOLJQ3yVWSdK88SWq_gTO9HhdjBI_sbNCgDIwfK9ziaISW_tFIUAJ-WPU_kZzROG-yxuTWuLnVLqb2d7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک جانفدایان در اصفهان، سازماندهی اراذل و اوباش با قمه و شمشیر و چاقو!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72744" target="_blank">📅 22:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72743">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4s9MG3yLWVB0BJUrVLNiOfnMEDGOJmNYMdkr8r-ZQ8y45GsHlH69lleOjIqbiIqmSoHhpJ1b6usj4xK3uva-veUeJGC9Fro7dRWZm9HgBiq8exBB5S83-CKzzjCIjDINDK5gGo5qvLzKGXW2vkwBbG9YwfhCiSLIqOupfinUTNDrz_Hr4-A7T3OeMTcqzFg3wjmn6iyzCXQOFJiH5-hQq_cEyFcKGDgeiKDkhYp_R81pincjhz_iRDl_HBjFbbvObQIGFc2atYpn7P076-m4Pn4CiIV7vD7ck_xjFy0jsOLH4h0PUbsO9aiVP5mcjm4W716Sss6W_9VNn7VRPEmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از خود به همراه پنگوئن‌ها در گرینلند منتشر کرد.
پنگوئن‌ها در گرینلند زندگی نمی‌کنند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72743" target="_blank">📅 21:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72742">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم   @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72742" target="_blank">📅 21:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72741">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72741" target="_blank">📅 21:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72740">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=aGWs8Zj1ESQHcvNDd1HENzYmrkHS6CqNQJi38Y_Hkjf3niFxQrf0CjQKmv2ik4CajtTVr_U8KSF7jrgefDc0QrZ-ItuqyfWv6M65_8gw0hfL4X8V6sj4iVmahepKgLdlU_malqaquWW2RHsfcnlaiCoN8TO3hCspr4ypj24HrjkMxbdLO-jQLZIVQkN5Q1WnVF041o85cXPU6uuiVxAeHBVMOB5R4Vr00sUwdKOh98wjkVQawsYx98WXf5ZdXX3nDrU9koWvBEwRTSAluQjvko2Z-mHM5Ze0ZB4xrbqCSGXlUBTo_tDEoJEHIzBCiMAh8hQS_2Cx2WXcdwE17vFZtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=aGWs8Zj1ESQHcvNDd1HENzYmrkHS6CqNQJi38Y_Hkjf3niFxQrf0CjQKmv2ik4CajtTVr_U8KSF7jrgefDc0QrZ-ItuqyfWv6M65_8gw0hfL4X8V6sj4iVmahepKgLdlU_malqaquWW2RHsfcnlaiCoN8TO3hCspr4ypj24HrjkMxbdLO-jQLZIVQkN5Q1WnVF041o85cXPU6uuiVxAeHBVMOB5R4Vr00sUwdKOh98wjkVQawsYx98WXf5ZdXX3nDrU9koWvBEwRTSAluQjvko2Z-mHM5Ze0ZB4xrbqCSGXlUBTo_tDEoJEHIzBCiMAh8hQS_2Cx2WXcdwE17vFZtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک کنند؛ بدین ترتیب، دیگر هیچ بمب‌افکن راهبردی‌ای در «آر.ای.اف فیرفورد» حضور نخواهد داشت.
پنیک نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/72740" target="_blank">📅 20:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72739">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDiqPx5qTi6WIAG4Z30XAvW0qaKqr4i-ob7VbBIRcCRqKwewg3s4kk3hHqe-zjTx9r6iOA2o2aQDQ-g8cUTkLh9-EfpABK6ksOkGfnWstg3UbWc6ORazdHwZX_iRFjtbGvXqszrAfHypMAzQbPvijN5Z1TUK2MEsSV7PmIsULvlkVYhj5iVtwydw1ZTnJSii9_3vTuUklOKi5vys63OcKKw9tcLbKNHfzamYks3L6D6Fb9qIK5YODxiVSZB866XiLs2WLz7UcCe2O8AekInizCVACrW8OEHHimmDkeKb3Ja29LHY2MFW1g0zwpMkcVMQULfc2X-Th13ipduHmEnPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72739" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72736">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=Auu9gaK3fiptykzef35-xVmrGpUGqyct-lJ7wajacyp0VvP453xcrzaGi8hAlmm1xS4v_znkgMAG2YWhyDW0E1qenAW7xPFik2UtGiNdlAnDgQW70mT8_8GDwRNgcFP2rHlseyBj51wIRRpgAOp3M9b-YJZRMG7G9Hp9o0DpAxKAkXH37GyEjaeV3SMXAkq20B5BRIH9SSc_jZiQzbcFwsBCweFIykNgOc3DvYJzGuyHk7AieSGvhmeDjBdHJUx9ZCF8fJ5Sp9rqnzqjBSg8Hwmc85Fb3YP5Yfl3BCIi-KikPhfVJwx7m6CDXYqcwkmXPTqqS_KchW0SpdFMpJTpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=Auu9gaK3fiptykzef35-xVmrGpUGqyct-lJ7wajacyp0VvP453xcrzaGi8hAlmm1xS4v_znkgMAG2YWhyDW0E1qenAW7xPFik2UtGiNdlAnDgQW70mT8_8GDwRNgcFP2rHlseyBj51wIRRpgAOp3M9b-YJZRMG7G9Hp9o0DpAxKAkXH37GyEjaeV3SMXAkq20B5BRIH9SSc_jZiQzbcFwsBCweFIykNgOc3DvYJzGuyHk7AieSGvhmeDjBdHJUx9ZCF8fJ5Sp9rqnzqjBSg8Hwmc85Fb3YP5Yfl3BCIi-KikPhfVJwx7m6CDXYqcwkmXPTqqS_KchW0SpdFMpJTpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رتبه یک کنکور تجربی همین‌جوری داره بین موسسه‌های کنکوری دست به دست میشه و تو همشون میگه که من از بچگی اینجا بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72736" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72735">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112f06092b.mp4?token=RXdXo0rnAZy91i0e3hqqNjAdg-OM8OFitvvg8khLX1y74z8l-WZcb8oj09_iovG8aD9Ze6MFoLI32V8xLfFVvDUVslLITZzxVjdZSe2xW9oqBhjug3X7CFALvlwN3kNmOAFkgC5AMQKBgLbVKfHddKDw6y-jvQOt2A59N-XGaeujVjCcEUgwXhm4l84w8xuWzXruwwuI9jVgw08rhRXACSXW7Mp1mthhRnSg7h6AkIQ5vB9_QrJyiuBfDv82XuK3roabnz9KXlHMEHhx5XmDx5OFfCDffKYRsq2o1Qtc-fDgzaKO5O4G_XMc4Vn9m5qOMh6kdy-1JoqP9DHkaXQu-BYVtxItHovKOYGsJm487s1bUAytop56fIYZ2ywvqORyCEVIPO90uz4oQo3dT9tBbT4DvU5sdc-4Fa7lLvUI5PoMQtFDb0ExYPnR-FEsujgO9I0e650EgCKLvl2MfFzONnTk6OtU1Y7NIF2T9nct1JucWJdf39mlmzZb20FZwKmietb73d2HNCiOtCNYZRxII8jFDOy8WIJQ_cwB001eTt5BQDoRFiEEl-kfIPF2uCc_vWnoCDAqmJ7OLQlHheb9GsyUIdnzeyvW7n1z2ZRwYdvSqKRjdWtAfjPxgbLl5FRgwxVIYc9vp1kpl1r2uywteiX0aKxIdK_VuydYr7MKvI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112f06092b.mp4?token=RXdXo0rnAZy91i0e3hqqNjAdg-OM8OFitvvg8khLX1y74z8l-WZcb8oj09_iovG8aD9Ze6MFoLI32V8xLfFVvDUVslLITZzxVjdZSe2xW9oqBhjug3X7CFALvlwN3kNmOAFkgC5AMQKBgLbVKfHddKDw6y-jvQOt2A59N-XGaeujVjCcEUgwXhm4l84w8xuWzXruwwuI9jVgw08rhRXACSXW7Mp1mthhRnSg7h6AkIQ5vB9_QrJyiuBfDv82XuK3roabnz9KXlHMEHhx5XmDx5OFfCDffKYRsq2o1Qtc-fDgzaKO5O4G_XMc4Vn9m5qOMh6kdy-1JoqP9DHkaXQu-BYVtxItHovKOYGsJm487s1bUAytop56fIYZ2ywvqORyCEVIPO90uz4oQo3dT9tBbT4DvU5sdc-4Fa7lLvUI5PoMQtFDb0ExYPnR-FEsujgO9I0e650EgCKLvl2MfFzONnTk6OtU1Y7NIF2T9nct1JucWJdf39mlmzZb20FZwKmietb73d2HNCiOtCNYZRxII8jFDOy8WIJQ_cwB001eTt5BQDoRFiEEl-kfIPF2uCc_vWnoCDAqmJ7OLQlHheb9GsyUIdnzeyvW7n1z2ZRwYdvSqKRjdWtAfjPxgbLl5FRgwxVIYc9vp1kpl1r2uywteiX0aKxIdK_VuydYr7MKvI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه محمدرضا پهلوی:
"همیشه تلاش میشود ایرانِ دوران من با بهترین دموکراسی‌های جهان مقایسه شود، ایرادی هم به آن ندارم.
اما درباره اینها (ج.ا) که چنین قتل‌عام میکنند همه می‌گویند بگذارید درک‌شان کنیم، بالاخره اسلام وضع ویژه‌ای دارد، در حالیکه آنچه اینها (ج.ا) می‌کنند، در تناقض با اسلام است.
حتی در لیبرال‌ترین محافل، دوران من با بی‌نقص‌ترین دموکراسی‌ها قیاس می‌شود اما به اینها که می‌رسد می‌گویند بگذارید درک‌شان کنیم، اجازه دهید با آنها دیالوگ برقرار کنیم.
این چیزی است که برای من قابل درک نیست."
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72735" target="_blank">📅 19:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72734">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=Oz-zVYNbRtDluh8jnUOPtpO0NcYoLJMuZOYRUlUV18eCnqSBHg26bxT-krKlzqgwjGxAWUSQXuYCblj0aT-iCHzIg28w5X3TedtEgE-HQODpj3Zop1xoXSIIkENDy6pQ660VnBG7otHS1Gb9I4qdqZJSBzZsG-3WZbcXQsesYVDba-fMP_3iXxytOmAwQrIzGJWLw0VqG8iRQpBt22ll40-WqLngBAR3p4IJRVrjwtuKPwS6sdm7rQ9_JR9AHXXfJzGbCFy90LB6lWMEe9xoBAzqOzdYn6iOSrDmVjsMnVzKvj8DSvXHAEZEOophQXw0VGPCZ-HJZZYtb09Az8wFiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=Oz-zVYNbRtDluh8jnUOPtpO0NcYoLJMuZOYRUlUV18eCnqSBHg26bxT-krKlzqgwjGxAWUSQXuYCblj0aT-iCHzIg28w5X3TedtEgE-HQODpj3Zop1xoXSIIkENDy6pQ660VnBG7otHS1Gb9I4qdqZJSBzZsG-3WZbcXQsesYVDba-fMP_3iXxytOmAwQrIzGJWLw0VqG8iRQpBt22ll40-WqLngBAR3p4IJRVrjwtuKPwS6sdm7rQ9_JR9AHXXfJzGbCFy90LB6lWMEe9xoBAzqOzdYn6iOSrDmVjsMnVzKvj8DSvXHAEZEOophQXw0VGPCZ-HJZZYtb09Az8wFiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های عربستان سعودی مقر نیروهای خودی را بعد از اینکه به تصرف حوثی ها درآمد، در تعز یمن بمباران کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72734" target="_blank">📅 18:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72733">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ9qshcRc3yJ-7QuoVXEJDxQPsQ4hl-DDKnpYCSAc_vuGCETZ92z6REKvd82tzXYIMFY7JqsSan1TsNC0MjkLop7uFtzaL0TrFnwtIQ3GMqGOmoykjqTqXYwRVJ1llUegVgO6rUkPmxj0vDzNKcFXYhGn_igtHqtBJ7JNjALGvKIF5TFC80gVZ7J2-OGpY1ZoTZZLPskCHVlCrDY1ZmLy6vGuPmecoPWBHISggibJu14blYopQgRQS47xECccCZkZzGHZjwW_SMXuyduQgCBzYHWcnE-wXUn6i8L7F6MQD1qwOhNGc-HmJmVTX_EjPK3vug31LujjRVFDHFx_OCp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده با ارائه کمک‌های اطلاعاتی و پشتیبانی در تعیین اهداف، از عملیات تهاجمی تحت حمایت عربستان علیه حوثی‌ها پشتیبانی می‌کند، اما به‌طور مستقیم در نبرد مشارکت ندارد.
شاهزاده خالد بن سلمان، وزیر دفاع عربستان، از پیت هگسث، وزیر دفاع آمریکا، درخواست انجام حملات هوایی کرد؛ اما مقامات آمریکایی اعلام کردند که واشنگتن فعلاً قصد انجام «اقدام نظامی مستقیم» (عملیات کینتیک) را ندارد.
گزارش‌ها حاکی از آن است که فرماندهی مرکزی ایالات متحده (سنتکام) با انجام این حملات مخالف بوده و یمن را عاملی می‌داند که تمرکز آمریکا بر ایران را منحرف می‌کند.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72733" target="_blank">📅 18:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72732">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=qXnlqX_0I6l5eSbXc_nTLwYMS-Hcsx5jmdTyW4X-vXkagGD05MXyCvV3SUrTJXQ8HgZOx6aNu65Zo1PquzfmPF2YS0Q39d-3g6kRzYyMYWE0XIMmHQrvWNJglxHMRb1IJuG1jNqvMVaKgxyjU0pzvk9JdwYE8J0kMd5HYe2co8leN9ZeOq8MsDqgbZkdP-xIqnFhcVf4ClZwYL-YzzZja-bNYbL23kU_URGaRNe5BqonBIrigAnMZeUX5V7DuKe36DXKAmBjcB2M9ws9DFMLUe9cwI3-_gcR9eSK0zaabjCSFh0Hv-ItRBGpZZZnKu96NB_mwCw-h3ksTQvnVkEV6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=qXnlqX_0I6l5eSbXc_nTLwYMS-Hcsx5jmdTyW4X-vXkagGD05MXyCvV3SUrTJXQ8HgZOx6aNu65Zo1PquzfmPF2YS0Q39d-3g6kRzYyMYWE0XIMmHQrvWNJglxHMRb1IJuG1jNqvMVaKgxyjU0pzvk9JdwYE8J0kMd5HYe2co8leN9ZeOq8MsDqgbZkdP-xIqnFhcVf4ClZwYL-YzzZja-bNYbL23kU_URGaRNe5BqonBIrigAnMZeUX5V7DuKe36DXKAmBjcB2M9ws9DFMLUe9cwI3-_gcR9eSK0zaabjCSFh0Hv-ItRBGpZZZnKu96NB_mwCw-h3ksTQvnVkEV6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
در جریان این جنگ به این نتیجه رسیدیم که قطعاً باید برد موشک‌های خود را به ۱۰۰۰ کیلومتر افزایش دهیم، زیرا دشمن در حال حاضر در فاصله‌ای دورتر از سواحل ما مستقر است.
اکنون در این مسیر گام برداشته‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72732" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72731">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72731" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72731" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72730">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvHpw09HjdChP1sK4mn2_98kjOiTq_WSo1o16rctGexdOEhvYyc7Uj-S3x1oTj8-ha10qTAccEx8y2EoF5pJfBTY8NqTSKL6wQ6bsoFqeA9mofnMiSKassX-YoWqPLKV4p5D2TdcKQWSwbKsAmXPuqWn7f45HinoBjd9mbTVUaxW6eQAohil_A6pe2MhNSUM3-ZUwYb0PESo8UdeVY8a5npPRKt2eJDDAdrHF1hS8tLIXmyhprGFPyX3ad8ccYBmq5HgY-eniw77xMJHzBlyyvw1IcSZudSj-O4xSBnT8ANGGL_TObDRuyh3pw-Mfhz5nkXi86olDHTXDxfyVVbAew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز نروژ
🆚
پرتغال را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
نروژ: ۲ برد، ۳ شکست و ۸ گل زده
پرتغال: ۴ برد، ۱ شکست و ۹ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72730" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9tyv7pCRPXjBTMN-5SmRKhKnfS1hl-ZQTqcSDLoqbvD5gDLmRBOLa-KDFBoblZBIfk2JeLA6LetSoDzrtha7Vme856T5lu9gtejz4Q_baMeTIdeYe3cEqkmZWtF8ZbYfvpZAX03Cvcybr_s9mgmuMzU3UzDaWHXss1FUVa_QGmmmXzN6avh7B-v71tUIyPUMFhxyLVtbc2Haonl1WIlskg0Q11DhCxlppvK6T-hxz3OAKjv0Ci4s-OWrHHN1d75fhC1BaOKWRuhbNgVbUEx1ras9iV1ntp1kvLn6Z-QBvR3p64lVl8YIcOueOASuK8idkcLSHf-4r2lTXRWykJUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0214da517f.mp4?token=DRZ1MAQFMbqCzHPYYQx0r7P8yycvLuYA2EEuLtUZOUmOLrcuTASezyej2siF3yoyuqyGCyNg0Zww2LBLBUa_DjvZcgR81rhYwZOyMUdFNQCBoNaI-NJ76dW07lru73bHh27uFTDQNcNMp0E1Qw7bdtzr_SnAGsWch45XzCwZtcTHQwBVMLFoAppNRie25G6BOZwbbEl8mrG3hgv3y9HLZ31qDNhPK_CCPal_TeVKV0XhNnx2cJtZU-w8PTWiYLXjAETVJluVOkw8wUeDiD-SGx6k_y1Cc9FwX_hctPI47ETEVYq6Qk77Vmz1J1NS4VMwOKQtWkjVmine8IYjq7cRmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0214da517f.mp4?token=DRZ1MAQFMbqCzHPYYQx0r7P8yycvLuYA2EEuLtUZOUmOLrcuTASezyej2siF3yoyuqyGCyNg0Zww2LBLBUa_DjvZcgR81rhYwZOyMUdFNQCBoNaI-NJ76dW07lru73bHh27uFTDQNcNMp0E1Qw7bdtzr_SnAGsWch45XzCwZtcTHQwBVMLFoAppNRie25G6BOZwbbEl8mrG3hgv3y9HLZ31qDNhPK_CCPal_TeVKV0XhNnx2cJtZU-w8PTWiYLXjAETVJluVOkw8wUeDiD-SGx6k_y1Cc9FwX_hctPI47ETEVYq6Qk77Vmz1J1NS4VMwOKQtWkjVmine8IYjq7cRmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظر می‌رسد نیروهای انصارالله موفق شده‌اند کنترل منطقه «البرقانی» در شمال «الصفیه» و در محور جنوبی تعز را به دست بگیرند.
در ویدئویی که منتشر شده، نیروهای حوثی هنگام ورود به خانه «سلطان البرکانی»، رئیس پارلمان شورای رهبری ریاست‌جمهوری یمن (PLC)، و تصرف آن دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72727" target="_blank">📅 17:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=DXYfpi59PZ59TopZ3d8_b6RnUAAVEsHE7PVAMrVDB5dNMHTUSDDnbS8YKO2knx8rBw2RK3IKckOEKU2J0Kp7_Kg6tZm65Kc4QefFHBeUrd2VUb7Xrm30hENM4p3lP7VO5GGxGPXoPXXRVL3-7ab5TAdRldfXmFeS8asqngsz1GGZpM8Hul0cHNUx8ojBTbBCS5yhVCxT2hoXENirO2f1-wAbIvtYbLrBc8KXYER6ZgXQBk_7eSWC7bKmpL4L9EBCOxcu7OkQRnqpKn9OhORQvPH6q1dsBa4nOKBx-yu_3pVX0OvIZGTZ6gpVNK2aCMQnF6qgWODZ-SMvsAGGbwnm9Tdq43gScrTVYaifh7JlE1hGpIBK6WqoLOwdwEmgRLzF_ylEwpmKB8KJhHpzznSTW82JDAaacFwtbwGCaGzmGwgmfFDiEI24LB5W_4JENeBXthBK1qDcBHIdzeKes9rDok-LNHzmNWpPvQhgmTXCHG-stGb3901jOZ1cKyV-xNoZEIKaHtpUicCASROMgDV2E5yd0yzmSC-mw1z-4wTcT6wYiZrhK0jn7n3jXFrDxw384dePU_z5QUXoN0Ys-5qfa_ynSokyjHTdZ5CEkK7ZrQykrv-k7cy7jikZKHPC71u037PouplqSajVI3thiK7fFKoFRjKZtpODtB4vRyR9_k0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=DXYfpi59PZ59TopZ3d8_b6RnUAAVEsHE7PVAMrVDB5dNMHTUSDDnbS8YKO2knx8rBw2RK3IKckOEKU2J0Kp7_Kg6tZm65Kc4QefFHBeUrd2VUb7Xrm30hENM4p3lP7VO5GGxGPXoPXXRVL3-7ab5TAdRldfXmFeS8asqngsz1GGZpM8Hul0cHNUx8ojBTbBCS5yhVCxT2hoXENirO2f1-wAbIvtYbLrBc8KXYER6ZgXQBk_7eSWC7bKmpL4L9EBCOxcu7OkQRnqpKn9OhORQvPH6q1dsBa4nOKBx-yu_3pVX0OvIZGTZ6gpVNK2aCMQnF6qgWODZ-SMvsAGGbwnm9Tdq43gScrTVYaifh7JlE1hGpIBK6WqoLOwdwEmgRLzF_ylEwpmKB8KJhHpzznSTW82JDAaacFwtbwGCaGzmGwgmfFDiEI24LB5W_4JENeBXthBK1qDcBHIdzeKes9rDok-LNHzmNWpPvQhgmTXCHG-stGb3901jOZ1cKyV-xNoZEIKaHtpUicCASROMgDV2E5yd0yzmSC-mw1z-4wTcT6wYiZrhK0jn7n3jXFrDxw384dePU_z5QUXoN0Ys-5qfa_ynSokyjHTdZ5CEkK7ZrQykrv-k7cy7jikZKHPC71u037PouplqSajVI3thiK7fFKoFRjKZtpODtB4vRyR9_k0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛رشاد العلیمی، رئیس «شورای رهبری ریاست‌جمهوری» (PLC) یمن که مورد حمایت عربستان سعودی است، از آغاز عملیات نظامی تمام‌عیار در تمامی جبهه‌ها برای بازپس‌گیری مناطق تحت کنترل حوثی‌ها (انصارالله) و احیای حاکمیت این شورا در سراسر کشور خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72726" target="_blank">📅 17:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=TCytwg1CooRze4v1jinAfnKnQc1TJuycVzqJFgVe5Ti_bJQzm95HCjD_oyw8vpdSbhh9-81K0nw-Iyl3_YztfWeOm_k7I9-44w8_12SwVaFQx-H_zYW3XTW5tIf44emxDiHOZeMXskZVQyPiJ8QeLtvWsnsoRqhcp2vZoGq26XaC7OiF-egHHTIg8AGlYpEeEvOmpMot0J0eMIZ81SibeQxeLU6j_3PEsNbzi7H_ZwksFH4YO8pgdUtoF5X5fktgAn5CX_Pv3SowGVs8ZL6jXdskiIhebjkUJz8pQTi2LQKZMExMtgZmzfW35WCn6B8JKChoYwNdpa4UIZGdBhhR4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=TCytwg1CooRze4v1jinAfnKnQc1TJuycVzqJFgVe5Ti_bJQzm95HCjD_oyw8vpdSbhh9-81K0nw-Iyl3_YztfWeOm_k7I9-44w8_12SwVaFQx-H_zYW3XTW5tIf44emxDiHOZeMXskZVQyPiJ8QeLtvWsnsoRqhcp2vZoGq26XaC7OiF-egHHTIg8AGlYpEeEvOmpMot0J0eMIZ81SibeQxeLU6j_3PEsNbzi7H_ZwksFH4YO8pgdUtoF5X5fktgAn5CX_Pv3SowGVs8ZL6jXdskiIhebjkUJz8pQTi2LQKZMExMtgZmzfW35WCn6B8JKChoYwNdpa4UIZGdBhhR4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پای رپر ها هم به تجمعات شبانه باز شده:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72725" target="_blank">📅 17:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72724">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=VhFGHncqqE24bZoTLPfJ0tiW92lgibC2UvdZg8G8eu_KiQvmwerSUKytnGzo91nG4MtAgpHlvmEyp51ad0D5Awlkl_V4cIwFr1yRRPj-Vw1AUV7-u7iRi2xYp0J_xRYGw8a_STsUMISR2iS84vOdIbM7bXkz741SeHKSUF3TjrgaHAuba_re7idlrKMyaFDgC5plNXmUpxJwn3EnxwMCl5Lxe3DjErPwFxGdFT3ackh-Fh4lBfyAaqNWgw9qARGOYfJZXx0d49IrGePhMrbsveSu3j1cw00E1RBdgDBU3H8JAFo1EHqy_5jIb-d5j3xOIbGN5OYVehjuavnB4CZgwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=VhFGHncqqE24bZoTLPfJ0tiW92lgibC2UvdZg8G8eu_KiQvmwerSUKytnGzo91nG4MtAgpHlvmEyp51ad0D5Awlkl_V4cIwFr1yRRPj-Vw1AUV7-u7iRi2xYp0J_xRYGw8a_STsUMISR2iS84vOdIbM7bXkz741SeHKSUF3TjrgaHAuba_re7idlrKMyaFDgC5plNXmUpxJwn3EnxwMCl5Lxe3DjErPwFxGdFT3ackh-Fh4lBfyAaqNWgw9qARGOYfJZXx0d49IrGePhMrbsveSu3j1cw00E1RBdgDBU3H8JAFo1EHqy_5jIb-d5j3xOIbGN5OYVehjuavnB4CZgwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه داشت از حس و حالِ ناراحت پسرش تو روز اول مهر فیلم می‌گرفت که یهو یه مرده اومد و این شاهکار رو گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72724" target="_blank">📅 16:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=t2PbXhItdVNdqIZ7jXlF2MgNiXj-rwGlHy6V462HnSYYYWatly6pcM7ikh51GHUKoPYnIeJZkJgGvsUHZn3kKuRjGBE601vES8Fba5hnsevJU8RS16ynwuQDEB2EY5PBcU-5IHXWqTemoMqFmnLJSlFM4etUvnu0Gl56Im347ZQ-M4EjvFqipOEObQjcESAR9R_CiP1xg8AJKWF0DW45LwX9EezU7DfqQu7ORbBzoo_dWDIEj2SQ6VHCqgk-0V0URfxMpx5ocPUQhYmAYJK4ZD7fb6gl5sanoGL86ML625vz6hT8Gb4uD2ghtUwUb2RJvYBpLsUGIN0b6kLN33GSZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=t2PbXhItdVNdqIZ7jXlF2MgNiXj-rwGlHy6V462HnSYYYWatly6pcM7ikh51GHUKoPYnIeJZkJgGvsUHZn3kKuRjGBE601vES8Fba5hnsevJU8RS16ynwuQDEB2EY5PBcU-5IHXWqTemoMqFmnLJSlFM4etUvnu0Gl56Im347ZQ-M4EjvFqipOEObQjcESAR9R_CiP1xg8AJKWF0DW45LwX9EezU7DfqQu7ORbBzoo_dWDIEj2SQ6VHCqgk-0V0URfxMpx5ocPUQhYmAYJK4ZD7fb6gl5sanoGL86ML625vz6hT8Gb4uD2ghtUwUb2RJvYBpLsUGIN0b6kLN33GSZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مکزیک  یه گزارشگر داشت از وضعیت خرابیِ کنار جاده گزارش تهیه میکرد که همون لحظه یه ماشین لیز میخوره و تصمیم میگیره گزارشگر و فیلمبردار رو با دیوار یکی کنه :
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72723" target="_blank">📅 15:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72722">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=tpF734tR3kN8P9KrDVKU9CKi_KuKlacqfFOu6SjNGu5PRqjEwyhDmTEoGVz5bkhxlNBoEfXEpWqszGaXJ6pI2zsymedP4DMmdntyr74kOSWvaVBAmVAAZc_tsmWo63p9EQgm1fDKNG0LR42-MXPWM8KHEviQYpyIraNyKY3_dfibRw5snSN4CGB3mwp2Q26zgDsCPGezuK3dBfzGJuQSe5evuKZEHi6XJOVAphRYlGTZgxiRSCFtsFnx7JTQXiX4d06Da0CnsLsUHP-JCodXVKlvW84q-qgdWExMyyb_VlHsWDch_fmMJ6M6Ye-nTaqkU-3DqozphDTmCpdjxqHX7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=tpF734tR3kN8P9KrDVKU9CKi_KuKlacqfFOu6SjNGu5PRqjEwyhDmTEoGVz5bkhxlNBoEfXEpWqszGaXJ6pI2zsymedP4DMmdntyr74kOSWvaVBAmVAAZc_tsmWo63p9EQgm1fDKNG0LR42-MXPWM8KHEviQYpyIraNyKY3_dfibRw5snSN4CGB3mwp2Q26zgDsCPGezuK3dBfzGJuQSe5evuKZEHi6XJOVAphRYlGTZgxiRSCFtsFnx7JTQXiX4d06Da0CnsLsUHP-JCodXVKlvW84q-qgdWExMyyb_VlHsWDch_fmMJ6M6Ye-nTaqkU-3DqozphDTmCpdjxqHX7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فریادهای مهدی کوچک‌زاده نماینده مجلس بر سر همتی رئیس بانک مرکزی؛
کوچک‌زاده:
مملکت را دارند به آمریکا میفروشند.
«به خدا اگر از جهنم به خاطر کوتاهی‌هایی که در حق شما مردم کردم نمی‌ترسیدم، امروز خودم را جلوی بانک مرکزی آتش می‌زدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72722" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26538e463.mp4?token=DYsFC0QMuJdaYYklzhGd8hp4X7wejhKFEGD6UybfLD60o7GHNoLwtNIxS-1TRwGr2NeW-2qc38-DRcFwAZD6Ep65yzcC7iVXkuMAGVAkreJ3yeM5-eFPadIKhledRMPmOHjKOAHYFReqXCk5etFHbqnOBoax56p_sQPdOYrgp1iyzzbqr_61shYMyUiChPLTOLO8FtsgMTXrnDC7-iP0yM-MxAFJA5E-bFcr9jg18H7CJHt3EY2-3wjwgvMf4jucGLbcTe0Atpy7nQrhPcbVqJmCpKeH0JNwIVjueobwV-ejzdLupS4ucqpGYx5iz4fh6q3DDz8cAlDYxXHLqKSgVSSEVLC2WE9pxysOOs_SZqW1IliozLivMOvcDcy1xUBud7FB1m9EtupNsVZbGRWojmAmxSxDNMzrSthdEmo4nyh0gXnkgjC1xrf649XVpfYj4FTWF8ZQGHVa4DJn9EhvpC9I7ovX6YE3-5Tv_UmZwJlCy4V4LE1kUZ1jB9ba6wbmLdmhOGS0BSxHO8pXo5-x7HIZWVm8rF7Kc-wv88UWvl4HaoJbR35dlfE1cdH_zI4Zz6JBF76zjvNBXhJFsSZI9YNNT5m5ytiJqcvSPQJcwpgYRv1f20LFGDiWYjCYVVj6BoRAqJ3yMuf5ECUoRB4IGbaLbS7qmziiQdIrYIUmsVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26538e463.mp4?token=DYsFC0QMuJdaYYklzhGd8hp4X7wejhKFEGD6UybfLD60o7GHNoLwtNIxS-1TRwGr2NeW-2qc38-DRcFwAZD6Ep65yzcC7iVXkuMAGVAkreJ3yeM5-eFPadIKhledRMPmOHjKOAHYFReqXCk5etFHbqnOBoax56p_sQPdOYrgp1iyzzbqr_61shYMyUiChPLTOLO8FtsgMTXrnDC7-iP0yM-MxAFJA5E-bFcr9jg18H7CJHt3EY2-3wjwgvMf4jucGLbcTe0Atpy7nQrhPcbVqJmCpKeH0JNwIVjueobwV-ejzdLupS4ucqpGYx5iz4fh6q3DDz8cAlDYxXHLqKSgVSSEVLC2WE9pxysOOs_SZqW1IliozLivMOvcDcy1xUBud7FB1m9EtupNsVZbGRWojmAmxSxDNMzrSthdEmo4nyh0gXnkgjC1xrf649XVpfYj4FTWF8ZQGHVa4DJn9EhvpC9I7ovX6YE3-5Tv_UmZwJlCy4V4LE1kUZ1jB9ba6wbmLdmhOGS0BSxHO8pXo5-x7HIZWVm8rF7Kc-wv88UWvl4HaoJbR35dlfE1cdH_zI4Zz6JBF76zjvNBXhJFsSZI9YNNT5m5ytiJqcvSPQJcwpgYRv1f20LFGDiWYjCYVVj6BoRAqJ3yMuf5ECUoRB4IGbaLbS7qmziiQdIrYIUmsVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من با کیم جونگ‌اون، رهبر کره شمالی، رابطه بسیار خوبی دارم.
وقتی طرف مقابل ۱۱۲ موشک هسته‌ای در اختیار دارد، خوب است که با هم کنار بیاییم.
اما تفاوت اینجاست: ایران هرگز موشک هسته‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72721" target="_blank">📅 14:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72720">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=W3R8H_bafETnNugNf47JF_Sg3keWcwJqT9fXSkKyZb1m3aILQYzycYOlSUx3R8g_rNxGNCQWj9p-KfO-cwdNeDBm9hSpx8a2F9dvtPwYL34kingfPCdc3gp2ozJKVo5MMiKOQ-wIgfAg9g8QEuTMOMVkWCfcm66Jr8XhNnMJm6UjvN9mrLIFSqCq2P_v16RYqWnNbZB-5cg3aY9ID1LES5wXDHvrjQUEr8oUcsQZYkQssuk7QO_ZUoqGIxGFTs-IrOzD2x08rwHb6ZxYRqTnoWDSlf5N0_Jeew7CUSrWfrQPRHuuibAMQBgK591e9cqNjoj83dCWddOEO-RgLAwuDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=W3R8H_bafETnNugNf47JF_Sg3keWcwJqT9fXSkKyZb1m3aILQYzycYOlSUx3R8g_rNxGNCQWj9p-KfO-cwdNeDBm9hSpx8a2F9dvtPwYL34kingfPCdc3gp2ozJKVo5MMiKOQ-wIgfAg9g8QEuTMOMVkWCfcm66Jr8XhNnMJm6UjvN9mrLIFSqCq2P_v16RYqWnNbZB-5cg3aY9ID1LES5wXDHvrjQUEr8oUcsQZYkQssuk7QO_ZUoqGIxGFTs-IrOzD2x08rwHb6ZxYRqTnoWDSlf5N0_Jeew7CUSrWfrQPRHuuibAMQBgK591e9cqNjoj83dCWddOEO-RgLAwuDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی :
بحث‌ها پیرامون خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) در محافل سیاسی ایران بسیار جدی است و وزارت امور خارجه به تصمیم مراجع ذی‌صلاح پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72720" target="_blank">📅 14:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72719">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=HGPy6QXs2DZxgi3feAujR6x6pVQOJmxZ9iozmfTbEDN00X9LMFoG5yKsKjmXZdqZaWKWPZUVeQB9mamIXN6Dm4mWwYiEjv0XUsnVWTSVL6nIczqUFv1Vc4lnRAIrsSW_vAgZCxgzhgH0EnXdReHc9VK6tqZQao2o83J2QUfOVrUUNHCVi2JjFN1YW9MR6HLF1N3kaO6WWYSY4facofT4icdmT-JAhIeAv_QKMH_HK6nC0zggYlxmQiLacfoj_HiMUR0M5v8ldVj5UoVAaZq7npx5bKfmnDEQxMqL0yUI2kHUOIj6vNjVidYzA2N8g0tcDyAHodiHqXU7ACgEfYCM1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=HGPy6QXs2DZxgi3feAujR6x6pVQOJmxZ9iozmfTbEDN00X9LMFoG5yKsKjmXZdqZaWKWPZUVeQB9mamIXN6Dm4mWwYiEjv0XUsnVWTSVL6nIczqUFv1Vc4lnRAIrsSW_vAgZCxgzhgH0EnXdReHc9VK6tqZQao2o83J2QUfOVrUUNHCVi2JjFN1YW9MR6HLF1N3kaO6WWYSY4facofT4icdmT-JAhIeAv_QKMH_HK6nC0zggYlxmQiLacfoj_HiMUR0M5v8ldVj5UoVAaZq7npx5bKfmnDEQxMqL0yUI2kHUOIj6vNjVidYzA2N8g0tcDyAHodiHqXU7ACgEfYCM1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکشنبه ۱۲مهرماه۱۴۰۵؛آتش‌سوزی در پاساژ خلیج‌فارس عسلویه به دلایلی نامعلوم:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72719" target="_blank">📅 14:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72718">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OE6PIZE8RUJVZ7901_mlo3pw2WaDKEsNjQPQnYZzPcmuT23of-Vx1t9pR7cJgifOKxr4OIj7Tta7BVbEvLh2zQGuFDgw67McdDYGzMtZu9KdDTWlWpRzXcvpXzeyMe0u9c-4eR5si6EFe5-fItWQTykn8K6vKyPPMXyGgeRBjhCmEoNbuFPJ_ObkYYTbBhe5z5ZHxO3kTjVE-u-t28_6Ea1L2qVpwZ5Uy6IY5Wone9TCDblFI0zkT1ofGMYIwx15yvWXtIuDHmNq1Xn7rFKdhta4aPkP13xtKBkXnURvRdIh3zqDleIDgglwB-ZrVbPMFSMUwOpVsSeb6SBu5z7Vfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران _ نجف که قبل از محاصره هوایی حوالی ۱۲ تا ۱۹میلیون تومان بود ، دوباره برقرار شده اما بیش از دوبرابر رفته رو قیمت و شده ۳۰ تا ۳۸ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72718" target="_blank">📅 13:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72717">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=k0ed1GMBLWjg0jr9d9N2u-bSrmI9m5AEpr7Y2Id1FydzPbQXiy0yhbVRukTXwHzxHI4xMA-jOXSt-HzSGEGUiKiHB4Q3LVbKmIR5hgISW9IFuC1qVv3dlIdr8ykpDl3TX-r5CK4UK8duKHEanv3Fof4ZdqpNz21fsxM-g_PL-CbbmCLFkAi7vqoEnibUytGVZFPEYVX7yq8m6y_QCED54wL8SYMYJoFLMsiuv00GPFW9WETB3iZNTzUdXrKgNnQXH8jYDuDjD-NWN5Ax60WdYItEqo6F05PQmb8Kef4M75SzIlpHXRv5NYtkHWCTevlsFIn9HDUxJQiPUnZVDi_Ueg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=k0ed1GMBLWjg0jr9d9N2u-bSrmI9m5AEpr7Y2Id1FydzPbQXiy0yhbVRukTXwHzxHI4xMA-jOXSt-HzSGEGUiKiHB4Q3LVbKmIR5hgISW9IFuC1qVv3dlIdr8ykpDl3TX-r5CK4UK8duKHEanv3Fof4ZdqpNz21fsxM-g_PL-CbbmCLFkAi7vqoEnibUytGVZFPEYVX7yq8m6y_QCED54wL8SYMYJoFLMsiuv00GPFW9WETB3iZNTzUdXrKgNnQXH8jYDuDjD-NWN5Ax60WdYItEqo6F05PQmb8Kef4M75SzIlpHXRv5NYtkHWCTevlsFIn9HDUxJQiPUnZVDi_Ueg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش روسیه به پل شمالی در کی‌یف حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72717" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72716">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=d6q-zmb9YTipfwOh8Mbn9XV9d7xt-wmnwsDu_gQcxi_ksoIukQ3kkVTsmGytEJLbT64sSdrzMdltZkSq4e99AcUGLDKDLskCvCFHV8c1cgxLOQM6Dg1huHhNPhbc50gfxP-O-IAYmDsA1mKn8oYgPrUQTih-We9re6bL-LQibmENvo-YQCQsXGfyy6j0Rz_j3cL6ZU0oQAg6MHWJat6zu7Sa-ML4HHStMc9DMpRbrRKdcYv7-ZArxRL_zCLdhXHwRdNdG_oRdRvrtklsUGZzwXsH3nmEMPs4iwkHI-c1jT92i2ZmAlUAZnHbuLesASUkkpxeoVfMygcSjuec18H1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=d6q-zmb9YTipfwOh8Mbn9XV9d7xt-wmnwsDu_gQcxi_ksoIukQ3kkVTsmGytEJLbT64sSdrzMdltZkSq4e99AcUGLDKDLskCvCFHV8c1cgxLOQM6Dg1huHhNPhbc50gfxP-O-IAYmDsA1mKn8oYgPrUQTih-We9re6bL-LQibmENvo-YQCQsXGfyy6j0Rz_j3cL6ZU0oQAg6MHWJat6zu7Sa-ML4HHStMc9DMpRbrRKdcYv7-ZArxRL_zCLdhXHwRdNdG_oRdRvrtklsUGZzwXsH3nmEMPs4iwkHI-c1jT92i2ZmAlUAZnHbuLesASUkkpxeoVfMygcSjuec18H1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حرکتی شاهکار نگهبانای ی شرکت رفتن با سلاح برنو بالن هواشناسی رو زدن و بعد زنگ زدن به سپاه گفتن پهپاد آمریکایی رو زدیم بیاید همین الان جایزمونو بدید
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72716" target="_blank">📅 12:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72715">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دلار ۲۷۱.۰۰۰تومان
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72715" target="_blank">📅 12:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72714">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da8647691.mp4?token=iT4aOGioXZ6Iwwj2P1A9NCHZ22p-OFmtsUyTLHYw7RXIXXCLuqKT30W44gBEdNDeFhMKjc_TQ-G-fY9kjh01EuMGCBPPaj4H8NnbIQc0Z6DzfzDmZuQ-gpx7rFBdWBj2D_BtskGe6AoVhzm244ZcjD2_U1JRtF1XzAYeioOLMek1Mj2SkT4zO7XisEOJhWvjYV9jVsinySKUke82LCpeTS3njprDc7kwkM4q-0-YkxPGd1E6JoqGwT0-etXCaYRKZS5CwQwsG7vSgEzX98OntLEUQ_j3ALhyLrgX1OsAF2OcqDcoedWhFP1kkvBj47wp1Fiz_usGWaa4VDjLqgtpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da8647691.mp4?token=iT4aOGioXZ6Iwwj2P1A9NCHZ22p-OFmtsUyTLHYw7RXIXXCLuqKT30W44gBEdNDeFhMKjc_TQ-G-fY9kjh01EuMGCBPPaj4H8NnbIQc0Z6DzfzDmZuQ-gpx7rFBdWBj2D_BtskGe6AoVhzm244ZcjD2_U1JRtF1XzAYeioOLMek1Mj2SkT4zO7XisEOJhWvjYV9jVsinySKUke82LCpeTS3njprDc7kwkM4q-0-YkxPGd1E6JoqGwT0-etXCaYRKZS5CwQwsG7vSgEzX98OntLEUQ_j3ALhyLrgX1OsAF2OcqDcoedWhFP1kkvBj47wp1Fiz_usGWaa4VDjLqgtpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت بر سر قبر علی خامنه‌ای، علیه مسئولان نظام شعاردادند؛
«گرانی رو آوردن، سازش کنن با دشمن»
«مفسد اقتصادی، سرباز آمریکایی»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72714" target="_blank">📅 11:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72713">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7J3DEXjCFcSXJfDCtIFka9OwrogEWAmdUc-LPAatRAPjpsBy-dZXY5dz1vezQ8crmigC16Z7NbUAIIoWqxnnDvtyRhh7L3ejIAKksrCRvAdJ0IhdCqvyyYWFrdDsfABGiakO6fQYrGIJDtwgV4Nf4UiTLCLlswFuG0BuhQ_pyzhCnLWh3MzhfwTikYljT5lxRfN5yFIvGFoy0TUZiHfgHJfeEHN5c0U4bkWolF_v0gU-62qCQw2eKRyuI8gV2vjY608YxxGAOvWOWPtGR5eszkjbTeEnhewsvxDSM4sDzkoi5iYIFJ1862St2_QVDGw_Zjb0OHRFsepmtJ8ifH8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72713" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72712">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72712" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72711">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZEr3wib2frKqVVYQTKIp4Y0Y4laa2CSR-atlX6I_nkv33LxeCHn1HpOOzP1vvea9V2mDMxoOV964Upy5RO53iQzM7qK7w4bcdTEmJpzGenS1JdkY1tuBOKZWyHRdVROa-6dwOyZ3vGdjjQQFdJB7q7rESbKRI_O2yeMTZSzv9RhHaBe3oyb2OXUmfMOdvu-9B1dIqN2kWCHf9KWv169t9qyxDCk6sDI2sx06XMfubXY5aBohSPuQC5cuvqzcBIS9RMoSsRDGNTvglzIfDHk0nDvgpOSLkRJJydmsYSt5ZUtCFANXIFTaRPabQhQrBIUwaZSakQWRTQgfniNnHcbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
یونان
صربستان
🆚
هلند
نروژ
🆚
پرتغال
دانمارک
🆚
ولز
آفریقای جنوبی
🆚
مصر
مالی
🆚
مراکش
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72711" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72710">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=ZMdVQ9ZMjNyPJfnmbRrgAvBXkY_QAt5eduJnq5u4-y5SEStCuw8ECGGGHlDpNDn0GsNaELrX8rt8chhA4c9rSbKItu4SobAP8z-OhXepwEBkqKz_NZNr4khvxP4cBuaMrTtoGxACxMEmaP4bWgFYPBWW4AKGr3jzqAz02s4rfnF-_KuJmH-n9sOn_MH4bjXntoA7gwgyQj9fgkTZVrqwME8_C7AoqDpCJk_1Plego3xPgLaUoXDrArDSca-CmGsQfz0QvMBaNdi9MM9CZtWdLhz-DNrS1l_WjZm7bhxjJdzJXo0l0SNEO1p3ddMDvHnvyFESoXbZDcCIumdHZRPH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=ZMdVQ9ZMjNyPJfnmbRrgAvBXkY_QAt5eduJnq5u4-y5SEStCuw8ECGGGHlDpNDn0GsNaELrX8rt8chhA4c9rSbKItu4SobAP8z-OhXepwEBkqKz_NZNr4khvxP4cBuaMrTtoGxACxMEmaP4bWgFYPBWW4AKGr3jzqAz02s4rfnF-_KuJmH-n9sOn_MH4bjXntoA7gwgyQj9fgkTZVrqwME8_C7AoqDpCJk_1Plego3xPgLaUoXDrArDSca-CmGsQfz0QvMBaNdi9MM9CZtWdLhz-DNrS1l_WjZm7bhxjJdzJXo0l0SNEO1p3ddMDvHnvyFESoXbZDcCIumdHZRPH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابایی، رئیس کمیسیون اجتماعی مجلس:
می‌خوایم حقوقِ کارمندان دولت رو 5 الی 10 میلیون تومن افزایش بدیم!
قراره «فوق‌العاده خاص کارکنان» تو کوتاه‌ترین زمان ممکن و با امتیاز 2 هزار تا 20 هزار واسه کارمندان اجرا بشه.
این افزایش از اول شهریور محاسبه میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72710" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72709">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=UZtShaXJhMBM51QazfJEmDUeMI3XpZcF6pznvXuNhuqt4wpSgJTQs_3aqA258swgH0kRJKbTHCFDhQCWSZnVdjG63CBdWNRHcTfYxb1pYAp3x_6f5T8TvsH24Jb0npFeEripq-NP62fIuig_HxnA0SUz31kOTa_mYejHtI-YSPCkOimXJVgYETu3djurBkPCWg7ofsDuwK2zSs1rXKy6HqXfP8ezW8NyBk_TwfZTUNlCrB6Pok0ulVNa4ne0UsHQXiSnUVOnV0X-DGtz3WvRUJ3tqEFWh93Rj8NZ4I7iOawFnSuSyOGd1Jdpogyo8zLsarhC3vbM4ACiunIo1t_XRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=UZtShaXJhMBM51QazfJEmDUeMI3XpZcF6pznvXuNhuqt4wpSgJTQs_3aqA258swgH0kRJKbTHCFDhQCWSZnVdjG63CBdWNRHcTfYxb1pYAp3x_6f5T8TvsH24Jb0npFeEripq-NP62fIuig_HxnA0SUz31kOTa_mYejHtI-YSPCkOimXJVgYETu3djurBkPCWg7ofsDuwK2zSs1rXKy6HqXfP8ezW8NyBk_TwfZTUNlCrB6Pok0ulVNa4ne0UsHQXiSnUVOnV0X-DGtz3WvRUJ3tqEFWh93Rj8NZ4I7iOawFnSuSyOGd1Jdpogyo8zLsarhC3vbM4ACiunIo1t_XRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانوم 15 ساله به‌خاطر اینکه هر هفته پریود میشده به دکتر مراجعه میکنه تا بفهمه مشکلش چیه؛
بعد از اینکه معاینه میشه، دکترا متوجه میشن ایشون دو تا دهانه رحم و دو تا سوراخ واژن داره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72709" target="_blank">📅 11:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72708">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=h_4YXlz3-O3nBLsr7lRSTZyi6aXQZae-8dUuf6YkQLdkkhKZzJsD_ilJMvXXyVmw1faBgle2Foh4JgSSRuncjMrM8Eycy6DfaANOpVExyYXNYvslfYDelFUf6DQkwIFU1fRa4n3T7MwdOmS-flFcxJaSd29bp9xqzX6FFGiNXR7j6MlNlH4jVkhW7t4gchYk4j-Lmo1S8iHLkzoZAZYJz0EObrhjPvXeudr_xsZvbNqvYsnqbPIR_AjBhM5IqzEsLQlJo-kzPBntxYlvkHXXQNERDq7kngeGyNeu3gwYM02XOnkbeh-3915jOLPOU0VR2-HPOG1C_o6Yc6xW3Zgpvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=h_4YXlz3-O3nBLsr7lRSTZyi6aXQZae-8dUuf6YkQLdkkhKZzJsD_ilJMvXXyVmw1faBgle2Foh4JgSSRuncjMrM8Eycy6DfaANOpVExyYXNYvslfYDelFUf6DQkwIFU1fRa4n3T7MwdOmS-flFcxJaSd29bp9xqzX6FFGiNXR7j6MlNlH4jVkhW7t4gchYk4j-Lmo1S8iHLkzoZAZYJz0EObrhjPvXeudr_xsZvbNqvYsnqbPIR_AjBhM5IqzEsLQlJo-kzPBntxYlvkHXXQNERDq7kngeGyNeu3gwYM02XOnkbeh-3915jOLPOU0VR2-HPOG1C_o6Yc6xW3Zgpvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:‌ حتی اگر بمب اتم بخوریم باز هم نابود نمی‌شویم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72708" target="_blank">📅 10:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72707">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=ZAWNk7gaPwL9y9HHylk_bCJZCJzpXVCKBKu08zJmlTcd9WMsXRsIW6_LABCUD86KY_sxgRKrMjT3rUxXKqhzkK_Mzhj7LAadL79u4niYGqrPRchOF6UVWONDGYAHWC02N_vTyD6q6-mYq-WUY5sxan-EJnQEa8_vTsiYBki5OULdSCy5bwBkFphM4dl7BTObjzfZ3hAfTWax0OZbDU94asPG3GV1ZOl_0pXIldBZ1eRJHyZzP1TZjpatsZ73vbXfKCb5gyoKHmn0zrPao1ZlBX9khZU9UK0BGaIb1EgSaXRUv4nQVBk-gc18BK-_kbgHJAykIUykGsmXxoFPRBryJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=ZAWNk7gaPwL9y9HHylk_bCJZCJzpXVCKBKu08zJmlTcd9WMsXRsIW6_LABCUD86KY_sxgRKrMjT3rUxXKqhzkK_Mzhj7LAadL79u4niYGqrPRchOF6UVWONDGYAHWC02N_vTyD6q6-mYq-WUY5sxan-EJnQEa8_vTsiYBki5OULdSCy5bwBkFphM4dl7BTObjzfZ3hAfTWax0OZbDU94asPG3GV1ZOl_0pXIldBZ1eRJHyZzP1TZjpatsZ73vbXfKCb5gyoKHmn0zrPao1ZlBX9khZU9UK0BGaIb1EgSaXRUv4nQVBk-gc18BK-_kbgHJAykIUykGsmXxoFPRBryJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه این مدرسه اس
پس ما کجا میرفتیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72707" target="_blank">📅 10:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72706">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8589525917.mp4?token=CyVAmy-W-E5NnImnO_d8tdiw__5ClXPB3k-c217kTKZORvvugq-OmUO8dx4wj_GHsv6ktpSrC2yg1Z2ZiwLN2Ar2vt_YRrNfmcGwunSaNIPXkvKtVd4hbPB2O5e38x2tHhwJRos7u5gq9PwAUaZ-bL8wCHTVN8gBNL8l9lU1dUUxzdf5449Zi8E1XGM5-lXUA2gbE4lWgwHdwNS5ST6ix_wkgklzwL8fNn3WXJj7666kmtNtsZ8hj0f5XV2xbgw7vAoH33jQM353ZcTMXWI0IbtPT_EGfLN-TnCO4AulpA9n89mCQNwayC189t_PewBWewm8_KFnZT88EDJOWhfvPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8589525917.mp4?token=CyVAmy-W-E5NnImnO_d8tdiw__5ClXPB3k-c217kTKZORvvugq-OmUO8dx4wj_GHsv6ktpSrC2yg1Z2ZiwLN2Ar2vt_YRrNfmcGwunSaNIPXkvKtVd4hbPB2O5e38x2tHhwJRos7u5gq9PwAUaZ-bL8wCHTVN8gBNL8l9lU1dUUxzdf5449Zi8E1XGM5-lXUA2gbE4lWgwHdwNS5ST6ix_wkgklzwL8fNn3WXJj7666kmtNtsZ8hj0f5XV2xbgw7vAoH33jQM353ZcTMXWI0IbtPT_EGfLN-TnCO4AulpA9n89mCQNwayC189t_PewBWewm8_KFnZT88EDJOWhfvPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش‌هایی از کرج، از جمله باغستان و جهانشهر، روز شنبه ۱۱ مهرماه ۱۴۰۵، پس از بارش شدید باران سیل جاری شد و خسارات نسبتا زیادی به شهروندان وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72706" target="_blank">📅 09:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72705">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=uBnKc_phbFjSDwsFfcJQjz5s3ZQIIrRlLG1keamHvHWk-exxfFT6ai28ZPhpTvE_d4C211CAU46Mh6RLgMCSnS_6E3EKzAjb2DVa7V29u2Xen-v1sdI9wYZGEBUpCoPrZDuRDW2D5a4HBT55cK9UVbc76JVPIjZXYb5Ifj3fFYp7zR9uYWB6PptOCwbJ8AKIbEKgrJ5HPShEAefxFVwyYM0XrWpoew7INzbTcGD_5BXPDka0n-Qda_yeo4W0PAzosROXiJaVf2wavXH3dIXmGAe8LxfKIFVQDHZuqoRjim6eE0Gvu4Tse9MSB16blXCudTUeNquKf9Qz6l_eqNtl1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=uBnKc_phbFjSDwsFfcJQjz5s3ZQIIrRlLG1keamHvHWk-exxfFT6ai28ZPhpTvE_d4C211CAU46Mh6RLgMCSnS_6E3EKzAjb2DVa7V29u2Xen-v1sdI9wYZGEBUpCoPrZDuRDW2D5a4HBT55cK9UVbc76JVPIjZXYb5Ifj3fFYp7zR9uYWB6PptOCwbJ8AKIbEKgrJ5HPShEAefxFVwyYM0XrWpoew7INzbTcGD_5BXPDka0n-Qda_yeo4W0PAzosROXiJaVf2wavXH3dIXmGAe8LxfKIFVQDHZuqoRjim6eE0Gvu4Tse9MSB16blXCudTUeNquKf9Qz6l_eqNtl1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خراتیان، کارشناس صداوسیما: چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است!
مجری صداوسیما: چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید و بعد به سراغ ما بیایید
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72705" target="_blank">📅 09:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72704">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72704" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72703">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZUZXbveaGGq7X-vsCT2frzfKIsvFYalFsX39jFOsrp_IeRefJVshivng5SyW_JtW18dxn6j3jayBm2F5JK6EGPOtSzKipfDAbPNRkhBnqGkccU2cikqN08ZPrZLievHhCMmUVHZ5W6zITZacdqUV7YXc10QLPR2qRoF_IWCumd2I1MkUeaWFgZ3pbls9zCfJvt8OzFx3_mOXllP9_9KshRLB1wnLVNEKqmNWPuy4prVwN2xvPcF2hzmO4H5Q-hG79kRaZEYyytn5pOJ14VRztYQckVMDwbUO__zP6bm1uIi7O0d6HxBOXE9FZ1rJ8Rt2gmjQX6MoPm_ATI-AuNtIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72703" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72702">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2d851559.mp4?token=Qkf2igdCOAn-1QuMLtGFjYO_r8x0LuAW5QgMKgthnE35Dwe11gXL_0WkOkr71IcAyhkGaN4gGN-1tvnV0wShYzGmskbflkzoHACtd2IkTp0wmWfWYuNd7ZtdbWIJVKAE7d5vJnlDRc332V9JQ0Gd9m6SJiXNb_uSlr9zhkqBf1RYiPlvRRJlCYm_QZCFub74yxuX0rN7Zmrs37IcPov6Pwt9y9ogO9BN8tXGH0ZStU45sd60eXoXM2c3D74kKg5a8UZOUk7ChTP9KLt9_C4a1dh5MOSg-G2l6QUyCgtY44vIYafX9iCE9-cpTHf2sV3XPi4MaT7Yr47v17XRNEtwnw0a0jvBvuPalxvXt_5PtnFvPeKeuNoEiRvhe0Ht2-HiFwEYqbH7vnMTO5S9ZgFjQYoBimVGFCaUPXaY3mKzOL8S9MOd605vHlFBB7EoBTg3bl_eY3Yh1QEq4YY1E6GBNmhGZaCxKWFiwtCktfFLDB9Pz3P00gPNYy0mQaGH4o-qSX8OtKsqpLssIXs7yV1rywSB6yt-ENRo1dX6qab_nGBOu-KhSpS7Kb4svyLLKjAwzh3byfzcXOeJVf2fwomolFtjDPZC8ZHDArPC6ijJ6FdCjRV3E5Ex4_x7NEhzJo6QomjgnW5nivm4uUCyoRJfLuPawfEoO8q6JQAspC_Quvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2d851559.mp4?token=Qkf2igdCOAn-1QuMLtGFjYO_r8x0LuAW5QgMKgthnE35Dwe11gXL_0WkOkr71IcAyhkGaN4gGN-1tvnV0wShYzGmskbflkzoHACtd2IkTp0wmWfWYuNd7ZtdbWIJVKAE7d5vJnlDRc332V9JQ0Gd9m6SJiXNb_uSlr9zhkqBf1RYiPlvRRJlCYm_QZCFub74yxuX0rN7Zmrs37IcPov6Pwt9y9ogO9BN8tXGH0ZStU45sd60eXoXM2c3D74kKg5a8UZOUk7ChTP9KLt9_C4a1dh5MOSg-G2l6QUyCgtY44vIYafX9iCE9-cpTHf2sV3XPi4MaT7Yr47v17XRNEtwnw0a0jvBvuPalxvXt_5PtnFvPeKeuNoEiRvhe0Ht2-HiFwEYqbH7vnMTO5S9ZgFjQYoBimVGFCaUPXaY3mKzOL8S9MOd605vHlFBB7EoBTg3bl_eY3Yh1QEq4YY1E6GBNmhGZaCxKWFiwtCktfFLDB9Pz3P00gPNYy0mQaGH4o-qSX8OtKsqpLssIXs7yV1rywSB6yt-ENRo1dX6qab_nGBOu-KhSpS7Kb4svyLLKjAwzh3byfzcXOeJVf2fwomolFtjDPZC8ZHDArPC6ijJ6FdCjRV3E5Ex4_x7NEhzJo6QomjgnW5nivm4uUCyoRJfLuPawfEoO8q6JQAspC_Quvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفنگداران دریایی ایالات متحده در حال سوخت‌رسانی به یک فروند هواگرد «ام‌وی-۲۲ آسپری» (MV-22 Osprey) در خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72702" target="_blank">📅 01:49 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
