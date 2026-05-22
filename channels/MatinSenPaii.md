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
<img src="https://cdn1.telesco.pe/file/vUHh-AuS3F_nr4PSd4YWYPGkk0Ryk67IQ-wQ1BiuDYraah_3npr8yDq3Cx7tC3bGAplGVL3QZ0qNUIZCanjwm3SZ1STL9Vht5LJnJcv6_AhFgYkEYu84ueTA4df1Bp1JC-u3aeCQb4JWvWbVBJ_Wtd74jfjMBhzFCRSQuvGSS3bZLZHEMtygW6wkp4WrF6A3hJQAqiRnYqxqrdp0P-8MrlWjmbTPQcn5PM44_Njpf4P6TXQUZpdfl4hoEUN16n2sDJz7ZfkYmUU1LlIzX9g0OSDUMxhQcgYKejZPUsTAenkuVVWVkkDB53SGaCgIdYuG9DJDpG3pdgRrdM0uhpESiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 145K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 22:54:31</div>
<hr>

<div class="tg-post" id="msg-3299">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آیپی ارسالی برای شیر و خورشید:
اقا سلام ایرانسل شیر و خورشید وصلم الان ۵ دقیقه زمان میخواد
5.160.13.85
2.16.53.11
2.16.53.50
167.82.48.223
2.16.221.37
167.82.48.223
151.101.192.223
2.16.19.136
172.237.127.6
2.21.2.104
185.200.232.43
2.23.168.7
2.23.169.111
151.101.128.223
185.200.232.25
2.23.169.105
185.200.232.24
2.23.169.105
2.16.53.50
2.16.53.11
185.200.232.50
185.200.232.42
95.101.133.42
151.101.128.223
2.23.168.254
2.16.19.136
2.23.168.213
2.23.168.144
151.101.192.223
2.23.169.12
2.23.168.174
185.200.232.11
2.23.168.254
2.23.169.111
2.23.168.174
2.23.168.213
2.23.168.213
2.23.168.174
185.200.232.43
185.200.232.43
2.23.168.144
2.23.169.42
2.23.168.144
185.200.232.43
104.103.65.5
2.23.168.7
172.234.159.58
172.234.159.58
172.234.159.58
172.234.199.15
172.234.199.15
172.234.199.15
184.84.221.34
2.23.41.22
﻿</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/MatinSenPaii/3299" target="_blank">📅 22:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اتصال به اینترنت آزاد با کمک گوگل درایو!
😮
🔥
آموزش متد جدید اسکیرک!
📣
برای این متد نیاز دارید به یه سرور لینوکسی ضعیف خارج کشور!
📹
لینک ویدیوی آموزشی روی یوتیوب
🔗
لینک ویدیوی‌ آموزشی از زیرساخت داخلی  (مدت زمان یک روز)(اختصاصی)
🔗
لینک ویدیوی آموزشی از…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/3298" target="_blank">📅 20:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">چیزی که می‌تونم بگم به اندازه‌ی قطعی اینترنت روی اعصاب و روان من اثر گذاشته، اختلال GPS هست
سه بار توی شهرهای مختلف گم شدم توی جاده تا الان</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/3297" target="_blank">📅 19:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizi’s Warm Corner((AZIZI)⚡️)</strong></div>
<div class="tg-text">اتصال به اینترنت آزاد با کمک گوگل درایو!
😮
🔥
آموزش متد جدید اسکیرک!
📣
برای این متد نیاز دارید به یه سرور لینوکسی ضعیف خارج کشور!
📹
لینک ویدیوی آموزشی روی یوتیوب
🔗
لینک ویدیوی‌ آموزشی از زیرساخت داخلی
(مدت زمان یک روز)(اختصاصی)
🔗
لینک ویدیوی آموزشی از زیرساخت داخلی دوم
(مدت زمان یک روز)
📱
گیت‌هاب پروژه اسکیرک
💳
حمایت مالی از من
🗣
اینترنت برای همه، یا هیچ‌کس!
🗣
@luluch_code
🏠
theazizi.ir</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/3296" target="_blank">📅 18:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کلا باگ پنل سنایی بود. از اون طرف باگ سایفون هم بود
متد ترکیبی یه روز کار کرد، تا دو روز بعدش هممون سر کار بودیم حتی با چند تا از بزرگان من صحبت می‌کردم نمی‌تونستیم بفهمیم چه خبر شده</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3295" target="_blank">📅 15:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/abafd93842.webm?token=O8ihMm7y8DdikbSrKXoM-K3Bpcaf6Nk4w8QaswHbJVU6PlGEug232x1WbRoJejatgXuDQWzdvRjG6YDOGYNcKV1VGPbwXBzu6mFyx5Yb0F85k9xmsPoeybuPC4ALD9jIk2YhU4wyTYk8pzMIb3w2pxgZk0P3QUQWT3jCX1fYZIPHFqy0WQJvWZq0JElPgyEYT3txxofVt86AfFSjuLvoWSDVaKR21IE9SkuBXoWs74gZSJATUh_IQbVLApHqBxW1895s-urQ038khoIxuRcUKpLhtTWwDxyC9M3QJcgLdV1Nfm3QR6layJFWWDzrEPIpxtSZcfu0unuC5EFXW2cHBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/abafd93842.webm?token=O8ihMm7y8DdikbSrKXoM-K3Bpcaf6Nk4w8QaswHbJVU6PlGEug232x1WbRoJejatgXuDQWzdvRjG6YDOGYNcKV1VGPbwXBzu6mFyx5Yb0F85k9xmsPoeybuPC4ALD9jIk2YhU4wyTYk8pzMIb3w2pxgZk0P3QUQWT3jCX1fYZIPHFqy0WQJvWZq0JElPgyEYT3txxofVt86AfFSjuLvoWSDVaKR21IE9SkuBXoWs74gZSJATUh_IQbVLApHqBxW1895s-urQ038khoIxuRcUKpLhtTWwDxyC9M3QJcgLdV1Nfm3QR6layJFWWDzrEPIpxtSZcfu0unuC5EFXW2cHBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3294" target="_blank">📅 15:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CiuPlRJ5B1mrSB3f1LurlEXYlhhyXehlWqVszQyrBFsHYh2D023QkUZfQQ0dvkTS1Ua_mPKcqiuA-AZWPvsOV6QSkhv8qQVU4YYJCD7Puihn-HicDjAuEYKPboB_jH6M_UzDtEz7tRktdAMIUeB9t-dMelJeIHYjq_ceotxUvdjldUEe3KQP2zy0AMKdQLjdWOb-buLhzle9S85ToNvtlexpbtWIJLhFpOqWB0smtQPFM0HmsLxL8wrW_SVEmibQeDSGaFZTcVUKH_yLw6Z3mdMXrwT-9lEqDS6mySMF_2lY59mGRZLrGy2Mg5nSDUMGn61NAxJrNR2dsyETpblsTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز، همونطور که عزیزانی که از زمان ترکیب با سایفون(اواخر اسفند) یادشون هست، این کار به ظاهر جادویی(!) باعث نمیشه از حجم کانفیگ جدیده مصرف بشه. بلکه همچنان از حجم کانفیگ پولیتون داره استفاده میشه. خواهشا همچین مطلب اشتباهی رو نشر ندید</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3293" target="_blank">📅 15:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PgNIJRY2OZAEew0HgpAsTALm5vrC-W9cQNESo4Kd5Ncp7F4F5IYAySDP-8QYy6_DRHm3_JLnyBDGTaT2O_W09752pM1ecAoDl44_mE4nbUkIuNErdOIKCA7Qk6Uj4ztAaKL92ygN3UB8bStDK8DP70gkTH2HMbgatgmkkec0NW6-pt46Sk-DpxMnfiFK8FEtMRhPuBzfQ7X7X78TcVFpBADHJ2GDZBDEZqnzsTFTjzLxLg749YbZ-lOPKbCJYT9uswcbwrtkPtl2a5sJLF1hRYBXbdxqf6ljaNdgv_i7Wz10mlSgnGZcoOnsZyyL2dk22s3kLl9HlqNLEgujClRkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز، همونطور که عزیزانی که از زمان ترکیب با سایفون(اواخر اسفند) یادشون هست، این کار
به ظاهر جادویی
(!) باعث نمیشه از حجم کانفیگ جدیده مصرف بشه. بلکه همچنان از حجم کانفیگ پولیتون داره استفاده میشه.
خواهشا همچین مطلب اشتباهی رو نشر ندید</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3292" target="_blank">📅 15:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3291">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه سری تک و توک هنوز بهم میگن که اسپوف وصله اما خب ۹۹ درصد بسته شده. روی سرورهای ایرانتون تست بگیرید
✅</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3291" target="_blank">📅 14:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3290">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YGzfQ8PB2CRxXjMlcrCZTf8Tp4kMTTWJQZ80E6pztJFPlRzA-db55bXuSUwiac7nIWFuOgWNSnWJ3DA28dwPHR2IJ6PBcHni9E_Gv_V-KcsUjOxlrhypqVvDCB1nJ3RCV1f1W-WBKL3DEA_rCo10twMw3GiX3CUgtmRmFNE5nytiKt1XRr7lqhsOqkL-SXROM-Y51PrXiDSJyAqeGfN7ZsUtx6pfRY3thizM8yHqiugGyN_lpeG5lPIiZbMP2rtaDbKvmqztM_RNwMSKSdQUayKvJLaA6lTI5VPqRwTWRnR6MLWvpf0WXi0Irl8hkySVLrewfgWQCiQ1rbvDKWTxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر آیپی تمیز کلودفلر داشته باشید، ۱- آدمای عادی(مثل من) می‌تونید با
https://youtu.be/svYBcv4bSzo
به صورت رایگان پنل ادج بسازید، و جای address هرکدوم از کانفیگا، اگر آیپی تمیزتون رو بذارید کار میکنه.
۲- کسایی که پنل دارید می‌تونید یه inbound وب سوکت(WS) یا Xhttp بسازید با هاست و sni روی دامنه‌ای که به آیپیتون point کنه و پروکسی کلودفلرش روشن باشه، و جای address، آیپی تمیزتون رو بذارید. این شکلی باید کار کنه</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3290" target="_blank">📅 14:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3289">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WEnFuK3_3txHVBN5NtkXh6iwvdaxDIPTrgHiF-6FnIioJfUSOa5geB4b8A88yG9kzQIf_0sJfGOyNpf4o_mU-Ut6a9ti1ZMIgnrb_cFv3UyUuI9FdC1i_0ajNP289s4oR7vbsRrl8ELZJKWnLLygkoCFu-Z81VE6IyRo4lnhnywsp61FfftL9KpMisVACrty7to5iibbDL1DXKCcSbYzoN5agSodDCcP04uqMeaA_X6IlctJ65ohIoGvNNd2Wun9YDSlSqWzWM0Cvjmrg-OkSR4cVym-Efrv2LkDhoJThRKL8LRlJjF2j8YUUiZvn8L8n39qiFf-D-212EomsRG9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری تک و توک هنوز بهم میگن که اسپوف وصله اما خب ۹۹ درصد بسته شده.
روی سرورهای ایرانتون تست بگیرید
✅</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3289" target="_blank">📅 11:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3288">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8A3h_ZDRelT3qVoSF5iQIPXidWfNA5CNWBFL6h4JL7HhvJgMkd5ZjIn9Bwbg0YRC5LrFOou127ZeADiTkFt-rQRCAATHAFiHTUdvSDHk9ZnMQYPkXOReW48wLDVp4-cVFYi-XQxFGilTkSwmHneBCawzdWnmv0tyQaPDgtk9l7Yr7oWf63xK4OehfGUqNoXxEpeWAJ9X9YCHM7BlRtIAxtdOdgL47LQBurjUtYI4-p-iGBzPHdvvT9acgxLIIgU4441yCzEg2M057EuOvYuMfEqMafVtnin_TWWh2itwc0ZLzL8akr5TcAX3yvJtqwOFsTouZ5ljI9OhTShfwCfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنین بود، افسانه‌ی شیر و خورشید
🫠</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3288" target="_blank">📅 23:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3287">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODY-Mq7SGMWm2F8EmgNnqsUfFbUJJkIWR-U0L_h2CF-LBOPfk9iCDEoqDlrYfTnGA_Gz1eWRrNZk5hGfqAU7eFbA1NQ-EkfxAPN22ZOLg5S-KGH5d9OlKeoJxMO0C7VT9YDPQQiUZAX7v-E_6GpU8aK_okhVMzBSAJgAac6C_q4MZRvexbJhU7yFbGRYqpfm9IrU5dw3rMKsWpPINkUXZ7inX9l_rjRKhiesoG1Cn4YUN9erwJK2Bb2E95kS9XqphilIGktiV9Q2kUk84_fJEi6vsS2y6iprCW-Qft4mVXNkOrKwc69KMChCn_Szrfr2SvPeZG--G6mE1TZIrz4cVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3287" target="_blank">📅 22:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نکته‌ی مهم راجب سرورهای StormDNS و MasterDNS که روی WhiteDNS استفاده می‌کنیم:
هر سرور و پورت 53، فقط ظرفیت 255 کانکشن رو داره و دامنه برای تعداد بالاتر باید لودبالانس(توزیع بار) بشه.
خلاصه اینکه اگر با سرورهای رایگان سرعت نسبتا پایینی رو تجربه می‌کنید، به خاطر تعداد بالای کانکشن روی اون سرور هستش. اگر سرور شخصی خودتون رو راه‌اندازی کنید(که آموزشش رو ضبط می‌کنم واستون) به هیچ وجه سرعت پایینی نخواهید داشت</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/MatinSenPaii/3286" target="_blank">📅 19:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نیاز داشتم روی هاست X ایرانی که اسمشو نمی‌برم یه سرویس بخرم
می‌گه دامنه می‌خواد
رفتم دامنه گرفتم
میگه فقط دامنه .ir قبوله
حالا رفتم از خودش دامنه گرفتم
میگه احراز هویت سطح 3 نداری توی ایرنیک
رفتم ایرنیک میگه سامانه هدا نصب کن داخلش احراز کن
سامانه هدا نصب کردم عکس قیافه الان منو با عکس ۱۵ سالگیم که روی کارت ملیم هست می‌خواد تطبیق بده و نمیتونه
میرم میبینم نوشته شماره پشتیبانی ۱۵۱۰ هست. حالا هرچی زنگ میزنیم هیچکس جواب نمیده
و دیدم هرچی دامین داشتم هم پریده نمیتونم تمدید کنم با اینکه پولشو ازم گرفتن
رسما دیوونه خونست</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3285" target="_blank">📅 19:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ورژن جدید WhiteDNS Desktop واقعا خفنه. الانم با سرور رایگان وصلم هر سؤالی هم دارید توی کانال تیم جواب داده شده: @WhiteDNS</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3284" target="_blank">📅 16:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3282">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m3xm0KCKHbIzOrVOleydp3QunXreSg5D4o8HtAK-LjhqNkmHjuXa1KCQ7XGGYRwVmOtQem8TS5sZT3FDsyg8-s8I3IfLFVeopN9q7DNymyXCmt_ZYaR2GWc7Edtu3m7LDDTZgRljAbc2wdfbEyiNXLA-jSUt_V3fI2cpMiEeppFcQgYQ6ZIi_rFpXZhJEZ5Ga95Kr5gLhBg64UX70qV_ZN2gAkVfk0k12OiadWQ0uOYB6jy0r9IjR1IWIljbRHgqLF_ficU15X1vANM9AVRYgEy88U-s8G3tscqkO0hOBdxxso9Z8-bbK-tqEMV7OkHXKcDFgldmAhr6zOTUPzV-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rBD-gZTsxu5sZjoVeQ-GwJit6Lf9raDji01jKmCVKPmRo5hT0dSbVmpbTwoWieHYCYA_4dlC0304PPZvaxEMUNrH4yKJC6-eIwQpI2_S2wfSNbpxcpt7kv0XJjFiu0Wge6nFPV0uP2kjbcT5GkyOz33_rykgElTDpPZwNNZc-CtSykFk_0Yv5AufsglH85KBMcnyqHoNpcviOaiVGF8Rao_5xZ8qEXHjR3_GUNEhurh2fbXBWbzG-w2m0ySg-8s_DLb5jboLbMswEeODJyjvcM_-PB-vRkg52tdbBjyrFI_yYRpFqtXYMcpIA-AgCZVZV6-508R9_oJDDJliiIHCaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن جدید WhiteDNS Desktop واقعا خفنه. الانم با سرور رایگان وصلم
هر سؤالی هم دارید توی کانال تیم جواب داده شده:
@WhiteDNS</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3282" target="_blank">📅 16:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3281">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اگر رایتل دارید و کسب کار ندارید با این حال اس ام اس پرو اومده جدی نگیریدش چون اول ازتون پول میگیرن، بسته فعال میشه و بعد از دوروز بسته قطع میشه با این بهانه که شما صاحب کسب و کار نیستید و پیامک اشتباهی اومده.
پولتونم برنمیگردونن.
این عین دیالوگی بود که با کارمند رایتل داشتم
✍️
شیوان</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3281" target="_blank">📅 16:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3280">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p29wHGZw3EitrKj_0CN7ZCeOi3dCCQ91bLXupCM3aLiIc_vpuNDPcgAiFHZ-0AN-SwwsypkHhiMsPhtu_S37Z0O7LG8H2t4qgrLXBZ-uN-OeRfFbvfx4N7l8whs6L0fzyCN8pWavF5cci9SipbVqfUQytZIqFh45P1jH96omHCZWoIQIW04PD8MH356cgynhqyWLTY2QLeA0qABg9hvsm6raULPp7ssbyNfALrA7IrEXlT1Aprsa5s6Im2O7oZ5zDCNrLUEeE2DQqtiuITT1ZHozYN6eh-F69r5AFD77qAjjkaKnNf0YNehdauK8Zjfsp2S2JiR9nJKmk3RlVZ6J8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنل‌های این چنینی هم دنبال گرفتن ویو هستن و مدام در حال نشر دادن اطلاعات غلطن. به حرفشون توجه نکنید.
الکی برگشته میگه حتما قبل از اتصال به یه اپلیکیشن IP های اپ رو چک کنید
😂
انگار مردم متخصص شبکه‌ان بشینن Wireshark بزنن پکت‌های شبکه رو رصد کنن. جمع کنید مسخره بازیهاتون رو
"از ابزارهای معتبر استفاده کنید"
چشم الان میرم اینترنت پرو میخرم جناب</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3280" target="_blank">📅 15:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3279">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KEvMoFj0ENj-Wu8ZiTbXEvG4Zms_qfnGXoMJwvoOajpIS4HuQwweZMzE0Y33kCekPRc7pOwctFQYwBJx4ezjMKKiQC7Y4jxGAQ0EQ_-whYRaOfcuhYx_DuS52TQ0Fy46T7hiP-ogzxictGir-YkSEZw9U8OPyNOOe08qnfwNX80yCFk8wiWhfXflSa49vLfcdlatqnFRfIUIcHCSjQcGgMBSO_7SDyelYhuRPuqOPDAXtBxApO2Ufhyibnxfd4HyAKYUN3GzcqGKQ5pZRZEcwpmrIUTGEjVL0Wb1XN-YGNENl249TWiha3tutmgizB8antm10r47uuqjKRw3-Ea2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها پروپاگاندای حکومته طبیعتا. یه مدتی هم ریخته بودن میگفتن SNI Spoofing امن نیست یه مدت هم میگفتن Npv امن نیست و...
کلا ما از این چیزا زیاد دیدیم. توجه نکنید.
اگر به من اعتماد دارید، حرف من رو گوش کنید و با خیال راحت استفاده کنید.</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/MatinSenPaii/3279" target="_blank">📅 15:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3278">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i6cZuIHuzIs_qAszWGSmuM5JJijqDhGQRiebLx3xAF50bcC09WIShDeXINgyKxjQwdfOXgr0XjMEY512MuMiY3ecicgsM6JprrA63Kk_6ZfJ47-59aAmyfG7ZL7CK7Q5t2SZmyj9y2xH9RHMmJAlZnaVXdrDT68PB4nmCYZdrFcSYXdbvljE3YlyGeZFpMRUWRaBkdsmdpU6IhRhltmE_Nzw2Ks06P9LWNmt_LcKOvx0sQatkwnFKEq97uO_g7sguFRWptHf4q9owi0wTYpjUV-xDpDPKov86s5DNpEm7cW5FxMOmiWGva5tNzHO_bGIfNoGsWFcV0OcYkTYcirYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیر و خورشید توسط یکی از افراد مورد اعتماد بنده نوشته شده و کدهاش هم به صورت متن‌باز، روی گیتهاب هست و میتونید برید مطالعه کنید:
https://github.com/shirokhorshid/shirokhorshid-android
این اپ هیچ چیز ناامنی نداره و یه فورک از سایفون هستش. اگر این اپ ناامن باشه، طبیعتا یعنی سایفون ناامنه. که خب درست نیست</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3278" target="_blank">📅 15:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3277">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KknUTlV7f0fmMK8TFRj8Fm042N7gXU0ohH1ju6eoAeoAuL5281tQw42kVwTLz9ssFg_IDodUH2E2sqPEtd1LaGhiykpvBPyMJHyQpOxCqzupHsc3k_UhT_BzAXc06vhnfYaoYRHhdn6Qh57BBtN0U-Byf-KL8Z8Ik-ISvC6fweaqA7d4vHYC-uGQ5WnM5u1mgVFinrlgMYnQMvVPo3iqGfQyLPlrvH5PFlCk2CiKMfrlUIArWhkWI3PkdZG3l953FPsNEMYd25uehYt2TXNpZj2_lEwovjcZGoO38gmYUIGjdstHiqydPFgZPpe8xtglZ8SrjSmG-I9-Mh8o7mVbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتباطات زیرساخت و سیستم DPI تمام ترافیک شما رو رصد میکنه. در این مقیاس شما نمیتونی بدون رانت و پارتی سروری پیدا کنی که بشه این حجم ترافیک از روش رد کرد. متد خاصی هم پیدا کنی، درجا میفهمن سرورتو به یک طریقی وصل کردی به خارج. کلا تانل زدن و سرور خریدن رو از سرتون بیرون کنید و با WhiteDNS و MHR و Goose و Skirk و مابقی متدهای رایگان وصل بشید. به محض اینکه بشه تانل زد یا روش کم هزینه‌ای پیدا بشه من بهتون آموزش میدم</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3277" target="_blank">📅 14:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3276">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اکثر وی‌پی‌ان فروش‌هایی که شما می‌بینید عمده میخرن به عنوان واسطه و مجدد به شما میفروشن. خودشون کاره‌ای نیستن. منظور من کسایی بودش که مستقیم سرورشون رو وایت می‌کنن از بالا و ترابایت ترابایت ترافیک رد می‌کنن</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3276" target="_blank">📅 14:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3275">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Matin SenPai
pinned «
متدهایی که در حال حاضر متصل هستن:  برای وقتی که گوگل وصله:  متد دانلود از یوتوب و رفع تحریم سرویس‌های گوگل پارت 1: https://t.me/MatinSenPaii/3151 پارت 2:  https://t.me/MatinSenPaii/3230   MHR-CFW: https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG  MHRV-RUST:…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3275" target="_blank">📅 13:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3274">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3274" target="_blank">📅 13:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3271">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NfUjnz-lRAdbQZ8sp5pWy3ugvctWww-o0OEhTj_7wC0NEtb54QGOAHBSClkP_dkSIovA4gwOCQdwqETzZLAarqqhuoObG0BcCScVbEZ-McKt7Sr_u90FejiSIXU2ojrt6m-m8vQkOJ-gU_Z3OuhP67Fm8kBj_1KdE1poEnOMNNA0vRF5iwBM0qAB7_rVAhxtl1iVBMK4HKLC93JBEwXHhAHv63Yvm-mu6kBvH4CUQLlcardqxEGEhJ5y6y4E8aPjynVaMONlS95vMNbr36rprCiB_w96rZPX79Xk6JUeTR9Yco5kc2UL3-b-XZzVvM05m-q90Sq2zFJj8k0tJmXdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oO6NyFqYjBTpMyBqeZXplQM-5urnJBcwxNNpYP6OxLX74TYlBg-8InYf55mBXoqLUUZhwIL7aVgNo870CzAj-iB2dEBdLEkjSIMJ8uMDi1Anw4ZGyOE8Z6KGvS67KHPj396EEfkda4MfHHZVyS9KIddKwr3ENbXPqg0twXRG264C1IWO7ZFQZcFHHpD0_R46Ac1E6SJYKZyzAgfuahwFUkcsFnF4h3bcMK--dyi8AbULZo6T1303bl2x6SnNrybQq3yM_seQxLDhXel68qzU23ZEZv78eXJnwupPTz2jSj8LtSEAHtdfTKGExYExdqD5ELUwpYoWDnvp4tCC0atNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ClZHrf9eGDgVjxxrBZimtY7IjgRepInz6jLm8d8AkUNLU8LrQgP4zoBkrpzqBoDynd45QA0PVALS-85NGIj6CeZZz6p1Iqnb_BoVXoTn0uFWbgk1h0Vgzx9Dp1hZmGDJxQLMk5ukm1KYlNddPoMNa6fUWKF2Q597u_d4RQaxGtVQo6_ds7XpQQj0S6uuny3_SSDUu5lVEoPz0xVUzNHn5aIbyjDOFrQhtGqYqKODQIC-jsWlZYYXE-Jxo91UBb70bbYOfHJgYruhhUdFV1fDxFwxD1Z0KPibHA2TN3oCZaQgZ7ogdPqTlQXYkmN4s8QqJk4NC_wIbJ0pFOFSbtXp1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان mitivpn این SNI Spoofing رو توی ده دقیقه از کار انداخت که VPN خودش رو بفروشه. کارشو تموم کنید
🔴</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/3271" target="_blank">📅 12:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3270">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن. دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه، تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
✍️
آمینواسید</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3270" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3269">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gKHeuvUGp7D4T_m2ZkMMFZv7Vupvw_0wf57c2jPyIpL9WGX70M3PBrO8hGF0BjVJm31AUBUkWl8N2ZPMFFjgJi6N4wU3o3EJevNMALvX-QNum8KqkmpYRcsCevMMkSah-AwUPPoYugGqJTbHKoeccHzObJOVyIIQiJP2vckf0mKlAlSxyxvlglJU-TuYyUWAznFSUDtt2mrF3FTbf1COiXOEeS4Sfxk8CMnKOUV_vTNCOdIVgdpX3Nxe10oBPYEg6I0dCCUnUwM4KUBOJddqVq_px1HiIBdzofmg0IspbaPQX0TZZ7NAKk3mnL74Z4aokyuPQTz7c87qzT1keHtlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر خرافات راجب شیر و خورشید شکل گرفت این یک هفته که فکر کنم کم کم یه فرقه‌ی جدید راه بیفته.
عزیزان تنها نکته‌ی مهم، اینه که چندتا از آیپی‌های CDN رو بذارید، و انقدر بزنید هواپیما و بردارید که روی Range شما باز بشه و بتونید متصل بشید به اپ.
اگر هم وصل میشه در حال حاضر، به هیچ وجه گوشی رو ری‌استارت نکنید یا حالت هواپیما نزنید</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3269" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3268">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IEBCpO-bx3ikMiA-sy62jbZt-_qFEt_N62fVgEUkK-Yug2km6E2cHUwjrNibCdUkB3UfaU2Kkzsuv7Gduf-EA1Cq7wdqIp8ols-T4SG4JT5iVWABXZaSj_B66R8cRKouHgzWYS3e4zaHEkvOtLCMpLp4v0bQEuo6LdQw8Stbd_ko2bJlBuuqUCCgllnHXngLE8PUuac5iYDCaJMCOBhmpOR0v8yxDR8d7n97u-NYp78zeacxvZnwYnc8uF6EwowtLVvjegFx2jPJLEghcCbcSvMNxTpc5rmOEBqLBuNT2CDKYzgeTCA-zlq6qOxC_2rU7g8FiOPLfX3q-akK2GVD5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت Spoof</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3268" target="_blank">📅 12:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3267">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">☠️
آموزش ساخت متد MHR با گوشی + کاهش مصرف ریکوئست های گوگل
⚡️
لینک‌های داخلی جهت دانلود: https://t.me/MatinSenPaii/2969  لینک پروژه اصلی: https://github.com/therealaleph/MasterHttpRelayVPN-RUST
⭐️
توی این ویدئو بهتون یاد میدم که چطوری متد MHR رو صفر تا صد…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/MatinSenPaii/3267" target="_blank">📅 11:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3266">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یک سری از گروه‌های ارسال کانفیگ و کمک و اینهایی که از سرتاسر تلگرام دیدم و خب نمیدونم مال کی هستن اکثرا، می‌ذارم خدمتتون توی پست بعد</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/3266" target="_blank">📅 11:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یک سری از گروه‌های ارسال کانفیگ و کمک و اینهایی که از سرتاسر تلگرام دیدم و خب نمیدونم مال کی هستن اکثرا، می‌ذارم خدمتتون توی پست بعد</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/3265" target="_blank">📅 10:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فقط چون علی جان تهدید کرد</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3264" target="_blank">📅 09:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/motrG5Y3q0EBYxtPcMzKMEzDvbwrN4X2not5OXiKRhLMs9ZRL5zI0tD3HcPGPnv0kkp3_3jZcTGMZe9tjhgaZqjV8D-ww3hXtpTAXbnQdEQwDzvCGV32OoAVm25hh6kt2JSUhnrxaF-dg7ZetJfmHN-qUKr-1oDJre_MTtN7ZrJ-cnqQKCLT_-xcCJCqIKpEoEdWlK8AUr-dHWHUjE2jqpQKkgRiBKoUjue0dwfSi2-HI4gVPujV0VbEk1DWzXkUsVSslcf9hqm2v5pvxa5IXYLD8e-Wf8-ORj9c1Zm9QsUwq-ACPron7lbvKXbVZMuGo6TNPQBkMh-NhyUbkO68FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کانال من نیست عزیزان من هم تبلیغش نمیکنم و تلگرام خودش اینها رو می‌ذاره. خواهش میکنم اسکم نشید</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3263" target="_blank">📅 09:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f0b6810cc.mp4?token=pVvgoArPfr8DNYCEp4iTino7EvmYW1G-c5_KtcJTeSPFAtMEU7tK77DYf2mNM1b6IkuD-TInsb39iyLmjVzoQQulvP52W2OieFXWYyXNCv9Ez39uzZZVxy52DNjOrPevUZ-jdQolPJrIdss1nfm0dw6CQ7mZu6ccJ-tjwEmeuBkgQDgJnDU7zZVWanjEWm6tI3KxdttQJgIrdcW-pUlKceFm39K9UaYB2Bs3338Wx89h85m8DQcDnS-8t_nSfgxzx1ekFyxr4IifnlOq7XokvRO5FLGJoe4j3fooyhYsdrmq95vPQ5C_uWDMFhyXZZDadCFQUhrrq4BeZnmmHKXIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f0b6810cc.mp4?token=pVvgoArPfr8DNYCEp4iTino7EvmYW1G-c5_KtcJTeSPFAtMEU7tK77DYf2mNM1b6IkuD-TInsb39iyLmjVzoQQulvP52W2OieFXWYyXNCv9Ez39uzZZVxy52DNjOrPevUZ-jdQolPJrIdss1nfm0dw6CQ7mZu6ccJ-tjwEmeuBkgQDgJnDU7zZVWanjEWm6tI3KxdttQJgIrdcW-pUlKceFm39K9UaYB2Bs3338Wx89h85m8DQcDnS-8t_nSfgxzx1ekFyxr4IifnlOq7XokvRO5FLGJoe4j3fooyhYsdrmq95vPQ5C_uWDMFhyXZZDadCFQUhrrq4BeZnmmHKXIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط چون علی جان تهدید کرد</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/3262" target="_blank">📅 09:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gD97Hyi4ohCr6AsfGo5lUCMjrsmd9wTTiVZGEu8sPrzr_Ui3A7wDbuCPBDYqwCQiOFWXUENYEYsZIXb5xCG0-aVynuoFauXFKKqeF0t9VinQL5ijOjjSxDNliTeQcb4IojxaWe0usOLswEPDC9FhhDBV28rFrfWYy_4YC-KmaloGnmCV9QNV6hzE_tXrS58J3XjFVYacGHXNJMAgq_Mx6q2rKmgvBQU9nFLS0ELIt2wnYEt3Oiu43WO0HBZcaIeGovYT1-4n8igerZgGXyicNd53DbDaFCnveJ1diLcLwYhb7Lfw0Ci2R9xHF3tTmH7pn302uY9gp8rZVpNPA7mjlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3261" target="_blank">📅 09:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3259">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبر بد اینکه hcaptcha.com رو بستن کلا.  خبر خوب اینکه مشخص شد متد هنوز در بسیاری از isp ها بسته نشده و صرفا کلودفلرو کلا قطعش میکنن یا میبرن پشت reverse-proxy.</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/3259" target="_blank">📅 08:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3258">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">خبر بد اینکه
hcaptcha.com
رو بستن کلا.
خبر خوب اینکه مشخص شد متد هنوز در بسیاری از isp ها بسته نشده و صرفا کلودفلرو کلا قطعش میکنن یا میبرن پشت reverse-proxy.</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3258" target="_blank">📅 08:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3257">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">متدهایی که در حال حاضر متصل هستن:
برای وقتی که گوگل وصله:
متد دانلود از یوتوب و رفع تحریم سرویس‌های گوگل پارت 1:
https://t.me/MatinSenPaii/3151
پارت 2:
https://t.me/MatinSenPaii/3230
MHR-CFW:
https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG
MHRV-RUST:
https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB
شیر و خورشید همچنان وصلن با آیپی‌ها:
https://t.me/MatinSenPaii/3247
متد اسکریک که شبیه به گوگل درایوه اما اون نیست:
https://t.me/ShahabSL/9223
برای وقتی گوگل هم قطعه:
WhiteDNS(برپایه MasterDNS و Storm):
https://t.me/MatinSenPaii/3130?single
کلا دیگه سمت dnstt و اسلیپ نرید مقابل Master و Storm به شدت اذیت میکنن سر ریزالور</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/3257" target="_blank">📅 07:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3256">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ppRGgrFYlSZ-3N3jBYsVzrBrd0zd3_dTlZR7ltNvvxYIiNPt_UNQghTJ5pq7F2JgmxqTshYePWcMg0RKvkqQRVCzYS9ORtkMI1PCDvhCrmHJflOzDTLVzuS0gkYeCBfuscI6g_DfdTgjSyQPXnshwEKMWAKjrJvtAAghQcqD5rQX7Ad3h7RVX3Pq7fsLT7rpCDO5TJpTumSaDplR89veOkMxBPwWKGz35HyzFrwO9gyMWsSnMgFKLXFggberF8smmlIHEOU_5m-aZKWTrjdcWY6dVkqtOZWWrBpNsEBfAJGWHniNncGLwA595E0hhISLd0v7-bjye_89WNTogalsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه از شوخی گذشت
😑</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3256" target="_blank">📅 07:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3255">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">و اینکه دوستم عزیزی ران‌تایم‌های برنامه‌نویسی مثل پایتون و راست و گولنگ و  تمام نسخه‌های ادیتور VScode و Notepad++ رو گذاشته اینجا برای هر سیستم عاملی:
https://dlhub.465978.ir.cdn.ir</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3255" target="_blank">📅 00:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3254">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">☠️
دانلود از یوتوب و Torrent با اینترنت ملی، به صورت نامحدود!(پارت2)  توجه: ابتدا باید قسمت اول این ویدئو(https://t.me/MatinSenPaii/3151) رو دیده باشید.  لینک داخلی: به زودی قرار میگیرد
⚡️
لینک پروژه عزیزی: https://github.com/TheGreatAzizi/AzuDL-GC2GD (با استار…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3254" target="_blank">📅 00:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3253">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">و اینکه اگر Spoof واستون وصله و نتتون اوکیه، حتما متدهای جایگزین رو ستاپ کنید واسه‌ی خودتون. از جمله:  برای وقتی گوگل وصله:   MHR-CFW: https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG  MHRV-RUST: https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB  برای وقتی…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3253" target="_blank">📅 00:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3252">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb36e0d0.mp4?token=VBLhXVLrIUDpyCZtnHol4Vph06q0WocEe1ISVkpoaHizejadlu7fbURcKZtf1A-9pScKKSqhkFHS9SI7YMtKalVUtle5KQSXkWfQH28-M3CLJ1YP1ZXRIMn_MyNTvDnJX_Gt_6MuO4OyUf4f_72gzgdSDFxsKhSRrz-ojR247_Ip69oym9-HBIbY3EZdIPThQXWeoQ35bC4GfKHOS062w-MGTlETb7Jhuv8d93VD96PailL8cVVgs7kP3GAXZL1Kj3W7RZmY5fQbXRejON6Z7vzHlH6vvffsACrhL7OHjRq7rpijHf932fwCzpxQgUpNxispS8kGg7w_S_ktrnt6Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb36e0d0.mp4?token=VBLhXVLrIUDpyCZtnHol4Vph06q0WocEe1ISVkpoaHizejadlu7fbURcKZtf1A-9pScKKSqhkFHS9SI7YMtKalVUtle5KQSXkWfQH28-M3CLJ1YP1ZXRIMn_MyNTvDnJX_Gt_6MuO4OyUf4f_72gzgdSDFxsKhSRrz-ojR247_Ip69oym9-HBIbY3EZdIPThQXWeoQ35bC4GfKHOS062w-MGTlETb7Jhuv8d93VD96PailL8cVVgs7kP3GAXZL1Kj3W7RZmY5fQbXRejON6Z7vzHlH6vvffsACrhL7OHjRq7rpijHf932fwCzpxQgUpNxispS8kGg7w_S_ktrnt6Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3252" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3251">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p1hdX8wAO_unCTsdwzyyAoVLObSMBo7VDvAynNO60q_OJYz97N3hQ9SluvY9CiPOKoRUvowo8_Dh7UcwYLwhf63jy3lWfYDimHa-Bvw7F9zA4faOEXJwUZEg6daZFCf9oV-okXG9rwJK-PcRSZBun5XABklBTPDwxRwcDsKNeWMIWZGJx9c0UmchczoYTgomCpfpH1bcUOx4CY35uNZY1KOGD6mcdczpvc8OBkk4FnxmkhK0xT46cRVt5hZiFf1gQwTmnupxljhqhH80mhcuAdN4hdBkxtIaSnjDf-1Xfx73MKrtQogJ1PlaeushgOlYYvLjuEHnkciqAeWSJP0P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدود کردن دسترسی اینترنت به اپلیکیشن‌های خاص بر روی ویندوز
این زخم رو من وقتی خوردم که با کانفیگ گیگی ۷۰۰ تومن اوایل جنگ ویندوزم تصمیم گرفت خودش رو آپدیت کنه و من وقتی فهمیدم که خیلی دیر شده بود:))
از طریق اپلیکیشن TunnelX، می‌تونید انتخاب کنید که به چه مسیرهایی روی ویندوزتون اینترنت بدید
با پشتیبانی از:
- WireGuard
- V2Ray / Xray
- OpenVPN
- l2tp
- SOCKS / HTTP Proxy
از اینجا می‌تونید این نرم‌افزار متن‌باز رو دانلود کنید:
https://github.com/MaxiFan/TunnelX/releases/latest
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3251" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3250">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">و اینکه اگر Spoof واستون وصله و نتتون اوکیه، حتما متدهای جایگزین رو ستاپ کنید واسه‌ی خودتون. از جمله:
برای وقتی گوگل وصله:
MHR-CFW:
https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG
MHRV-RUST:
https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB
برای وقتی گوگل هم قطعه:
WhiteDNS:
https://t.me/MatinSenPaii/3130?single
theFeed:
https://t.me/MatinSenPaii/3109</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/MatinSenPaii/3250" target="_blank">📅 21:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3249">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این متد ناامن نیست دوستان، بلکه امنیتش کاملاً کنترل‌شده و لوکاله. شاید توضیحات من باعث شده که فکر کنید ناامنه، و نگرانی شما از کلمه‌ی «MITM» منطقیه، چون خب MITM حمله‌ایه که هکر وسط ارتباط می‌شینه و ترافیک رو می‌خونه و یا تغییر می‌ده. اما اینجا MITM داخل دستگاه خود ما و با سرتیفیکیت خود شما انجام می‌شه، نه توسط شخص ثالث.</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/3249" target="_blank">📅 21:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3248">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QIfNl6eGKbTPydMQ9d3u7LuFdk89c2qS-83N-F6CfRxdcHPsZWEw8ks0cJDA_ZmekCWgGrTaHsgtBH5ShcsDrJ73SqOIGCuWNvLE40WYnexURInghi__QNpjayemoH0A4xnY9YbE9fSEb5HHh8mctX_xK359mDdHWlo6nYcTG1lDGAv_W-zrZUWtHO3SJX8mdTvO5STzxi5GXSm-EQ8SRdedgr8S9R2fmY_Q8beoM0OK82I7E7hyX3AbWWiPpqp0OAbMsg3Mi6IETReCXK8EDNE0M-Qks7jSsjQNPbeSxHQ042eQtJnBNFRJzqhAtxibmxZAz14yP09Ph43SYe6bsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">kharabam
:
[موقت]
شیروخورشید یا سایفون MahsaNG برید Connection Protocol رو بذارید رو Direct یا Normal تست کنید ببینید براتون وصل میشه یا نه.</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3248" target="_blank">📅 19:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3247">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یکی از دوستان فرستادن، برای شیر و خورشید بخش edge ip:
2.23.168.7
2.23.168.47
2.23.168.96
2.23.168.144
2.23.168.174
2.23.168.213
2.23.168.254
2.23.170.80
5.160.13.85
5.160.128.142
31.214.169.244
37.191.76.110
37.191.95.70
37.255.133.30
46.32.31.30
63.141.252.203
65.109.34.234
78.39.234.140
78.157.41.60
80.191.243.226
81.12.72.218
81.91.145.2
94.130.13.19
109.72.197.1
142.54.178.211
178.252.128.66
185.109.61.27
185.137.25.214
185.141.106.238
185.208.175.228
185.255.91.60</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/MatinSenPaii/3247" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3245">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03524e951f.mp4?token=q2MXVCEgiFtdQqyffz1QvLs5g7dVQgAIzvBMYec6587BKyU-9GRFpAO1r0F-o4wqACopQ1EdfumJcCiY6e6JQZr-ajWqxJIaWXkN00I5ULv2LQpS3uL7hDDmvu-TkY_0XZ5DR7zU-S9kUfS_VMwgBTBbXlPsc6lX4ZW7fdySQwG-fcn72H2vWfPvTgSU3WiFMTB53_AHRGjYw4PHQNqjnG2X10YirO4tsSxpbegq_NgEpCp-n6pibgRn9irtGSIapDEQn0mj6kCsIYuATF1EvWtDVTVdNMypvWpkVXy3V6_4eALHk__OuSqQ0ezV1xrfwvhXkKY5F_SDb69tJxDiIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03524e951f.mp4?token=q2MXVCEgiFtdQqyffz1QvLs5g7dVQgAIzvBMYec6587BKyU-9GRFpAO1r0F-o4wqACopQ1EdfumJcCiY6e6JQZr-ajWqxJIaWXkN00I5ULv2LQpS3uL7hDDmvu-TkY_0XZ5DR7zU-S9kUfS_VMwgBTBbXlPsc6lX4ZW7fdySQwG-fcn72H2vWfPvTgSU3WiFMTB53_AHRGjYw4PHQNqjnG2X10YirO4tsSxpbegq_NgEpCp-n6pibgRn9irtGSIapDEQn0mj6kCsIYuATF1EvWtDVTVdNMypvWpkVXy3V6_4eALHk__OuSqQ0ezV1xrfwvhXkKY5F_SDb69tJxDiIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون مقدار sni که دادم آموزشش برای شما که چطور وارد کنید
✅
(مقدار sni hostname کاملا متفاوته با ip)
نکته:ip حتما باید پیدا کنید hostname فقط واسه افزایش سرعت و پایداری هست
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3245" target="_blank">📅 19:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3241">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">31.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ویژه گوشی‌های 2020 به بالا</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3241" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3240">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromali</strong></div>
<div class="tg-text">شیر و خورشید هر ایپی اسکن میکردم نمیشد واقعا هر کاری میکردم وصل نمیشد
ولی نمیدونم چجوری از network checker ایپی اسکن کردم ۷ تا در اومد کار کرد واقعا</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3240" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QXOdY8nJYJGKd5MRfQtcPzqddyvn_56rmhMFH3K7WVH6Wkt-l9loCpZaTa6zs1eW01xl3Dmt8Kl6OigWO_vrd8f0nihlGv6QiTy2-umpXm7-G6tieQKl-Mn7m0WMMVhvqYfDvIeBqcboAwStK6_Xv5269anKIZ176b1k8NX6Wu_XBr0uRKoUSPxRQffyNS2zs8npPcehW85w9hhxXTOMWA2FFkIVo7kCTWqItRIc4PTHxoq2a4KDg0HMPKJUViOsBA64zPhAUGxqht8LdBZXFqrfvkH0DmVMEJJOaTFBvhqwMrE055zw_AeL9pgi9j4WLinuz7M5kdQZsg3inykq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h5XQWUFQtNz1nU1wnPiDr7UJHPmzUOtp7-2v69RFQjm5ktCKpixBCm7P8NpvAhc3qIVjNlQkcsuiIRopTQzYnbnq5DLTuiZqPcMpYnLwGz6HPXNSoQ9TWvEZCvWMrS3jBOIPHtybS-XMe0-DUZIo7YKgxY4AazH78CcECdWBe2AE53xVxRovRKIP7BVogXWebwhPsQxHyTbA6ZzTEOdMbB_EnzhjJz6DXs6bl486njx-piBA8jkP0Kraew79yo4iNysRT46gVjdvKtHtedyjsqbVq8tJmsohfzSy8Heu28lXecp5jGoSnW8OQMA4rEt_jjpX5P3JVE6j-IZi9GiF_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👑
داخل اپلیکیشن شیر و خورشید با sni های زیر که ir هستند میتونید متصل شید و شرایط نت رو بهینه تر کنید:  snapp.ir  varzesh3.com  digikala.com  telewebion.com  bmi.ir  aparat.com  لیست بروز میشه
✅
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/MatinSenPaii/3238" target="_blank">📅 19:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3237">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-text">👑
داخل اپلیکیشن شیر و خورشید با sni های زیر که ir هستند میتونید متصل شید و شرایط نت رو بهینه تر کنید:
snapp.ir
varzesh3.com
digikala.com
telewebion.com
bmi.ir
aparat.com
لیست بروز میشه
✅
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3237" target="_blank">📅 19:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3236">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FRDIXVI1Lt_EA9FGTWZh6O_BTeF5hs81VJgkpwf0bR7ZTxSkIHSawhnpAlVnDbv4tUc6Nsk6qJwzt807-KL2oIcOZzLWdUMZ6ynkBJiS3Zoxs1H1Am-M6THB7VbRIPCCLjRLlZhrgHuIYwVwpmjWv0yYoo14B2t1sWm72D_f6d92_jYFxe1NPEwjplK92HpDRTzvk0108Ixd8AIbUFwqwpsvC_i0c3dzFTzSGldW_10HhE9B2LvxzPZ_19qfzDvw6DTCQ2Io9wYhUCEu5awfQAGjElU87GKLZNyNu5Z9hbdnsDA4Ti7q7liUKm57ieKGJWYRiUdJcaS6Nqoh9Sk3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان من هیچکسی رو توی تلگرامم معرفی نکردم و این کانال‌ها خودشون پول میدن به تلگرام تبلیغ میذارن زیر کانال من توی توییتر هم اینجوری میان میگن
😭
😭
😭</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3236" target="_blank">📅 19:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3235">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3235" target="_blank">📅 19:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3234">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2NNJROA2FIHpHebn29Up9TdsoCLLbhjfexlVMj6cEJnddn6x2AJykB4CzFwROIJmM8VdVucua5SYVCYk1Det0Vu2LSfeDAqcbGQz6HGk8kqHFEtQU_C7EJoiJRJbA12l5FVzD0-LRW7CBPqwlPOXyACaSwXOTi99WnM-4BDX6vrFw6xXIWacB8F2eyClI_k5uPmxS-LrAURkFiUgNkO2reVm7JPmaJMnqqx1pAi6mxSruQH0lXCW0fmhf_GoUQKUkLFT-dS5Jka_q-ZWc2nytQo2nx70lejk7aUnlym6JRtBOriG_Nji8E9t2HUyIHuWNfQ2A7Zoqvhc9Vj6drSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعریف ساده MITM:  در یک حمله MITM، مهاجم خودش را بین دو طرف ارتباط (مثلاً شما و سرور بانک یا سایت مورد نظر) قرار می‌دهد. دو طرف فکر می‌کنند مستقیم با هم در ارتباط هستند، اما در واقع تمام ترافیک از دست مهاجم رد می‌شود. مهاجم می‌تواند: 1- شنود کند (ببیند چه…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3234" target="_blank">📅 18:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3233">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دلیل اینکه این ویدئو و ویدئوی پارت 1 اش رو توی یوتوب نذاشتم این بودش که MITM(Man In The Middle) یک نوع حمله‌ی سایبری هستش(که ما ازش داریم برای اتصال استفاده میکنیم) و دانلود از تورنت و یوتوب هم که غیرقانونیه
😂</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/3233" target="_blank">📅 18:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3232">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دلیل اینکه این ویدئو و ویدئوی پارت 1 اش رو توی یوتوب نذاشتم این بودش که MITM(Man In The Middle) یک نوع حمله‌ی سایبری هستش(که ما ازش داریم برای اتصال استفاده میکنیم) و دانلود از تورنت و یوتوب هم که غیرقانونیه
😂</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3232" target="_blank">📅 18:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3231">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چنان انرژی‌ای برد از من توی یه روز دوتا ویدئوی سنگین دادن که الان جنازه شدم</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3231" target="_blank">📅 18:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3230">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">☠️
دانلود از یوتوب و Torrent با اینترنت ملی، به صورت نامحدود!
(پارت2)
توجه: ابتدا باید قسمت اول این ویدئو(
https://t.me/MatinSenPaii/3151
) رو دیده باشید.
لینک داخلی: به زودی قرار میگیرد
⚡️
لینک پروژه عزیزی:
https://github.com/TheGreatAzizi/AzuDL-GC2GD
(با استار دادن بهش ازش حمایت کنید)
و روی گیت شخصی خودش(اگر گیتهاب در دسترس نبود):
https://git.theazizi.ir/TheAzizi/AzuDL-GC2GD/
لینک وبسایت RiceDrive(بخش ساده):
https://ricedrive.com/
لینک وبسایت کولب(بخش سخت):
https://colab.research.google.com/
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از دوتا وبسایت خاص، به طور نامحدود با ترکیب روش MITM از یوتوب و سایت‌های دیگه، دانلود کنید.
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
بخش اول
رو دیده باشید
✉️
تماشا در تلگرام
💰
دونیت</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3230" target="_blank">📅 18:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3229">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3229" target="_blank">📅 18:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3228">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ویدئوی بعدی دانلود با نت ملی از یوتوب هم در حال ادیته. امیدوارم که به کارتون بیادش اگر اسپوف قطع شد</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/MatinSenPaii/3228" target="_blank">📅 17:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3227">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این نسخه، با نسخه دسکتاپ قبلی کلا فرق میکنه و بازنویسی شده. نسخه‌ی قبلی رو حذف، و این نسخه رو نصب کنید.
ویژه‌ی مک و ویندوز</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/MatinSenPaii/3227" target="_blank">📅 16:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3223">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه WhiteDNS Desktop V1.0.0-beta2
✅
حل مشکل باز کردن در ورژن های قدیمی مک
✅
حل مشکل وصل نشدن و خطا بعد از ۴۵ ثانیه
✅
حل مشکل وارد کردن کانفیگ به صورت گروهی
✅
حل اضافه شدن دگه ذخیره برای ریزالور های سالم و. فعال به صورت جداگانه
✅
حل مشکل مشکی شدن صفحه در ویندوز
✅
اضافه شدن نسخه های لینوکس</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/3223" target="_blank">📅 16:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3222">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">☠️
آموزش روش جدید و قدرتمند SNI Spoofing - اتصال رایگان و بدون هزینه به اینترنت آزاد!  لینک داخلی(30 اردیبهشت): https://guardts.ir/f/9e2486ea4d04  دانلود فایل نرم افزار: https://t.me/MatinSenPaii/2617 آموزش edge tunnel روی کلودفلر: https://youtu.be/svYBcv4bSzo…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/3222" target="_blank">📅 16:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3221">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j5Qt6djbrS9l_cxmnJMH5zKaCjIGSlowoJBK7G7FwzRQ9yp9KonqGbgWN4h4rssc_v3Ng0edM1x8WFzfsUJuzacKNeaVTcb2TJ_oSSyR4099a0tZNLRivx0-MQp9IRkLUgY1LqOYpc03QHyfBtXmf0LfnoqsCAkv_wEPVRimevhTDDA-KVotruM6cTuECb80hHAhp9ty9ST3-liLv-kkSUCKoJuc0GvkP31AicSqy8sVdAGSMRBXihsuKNshGslv7pUUe1Nk2sVUHXi16cGMHd0LdaO5Jj0D-5vx4er5F9-GNv0fm3SO6Ek39MWV2R9yUXJ7nz2ItBiZUr3adj7uSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
😭
😭
😭
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/3221" target="_blank">📅 16:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3220">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترسناک‌ترین اسکرین‌شات ممکن</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3220" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3219">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FczACfmrqtqW5sjJOd8S_sThtToR-kcEbbXQ4JH-NucqV86QUwOOYscN_dfhFkUPU73XiE6L-YY2ZkWG4CL4Wd1VulMmD7ycS5XK5q2rhZenNhFzUVcRzfT2hZ-y3b91ppE34nwMnlv5bJ6fM16wfoFUZs_v1EpZAaaJvncTAApCh2DslqBq5ABb2ekA1evo3LwBhnqcYvCbY7WRWhW74cN3My2YDb1kj-mzjcbzm80-Mhso4hjBwwFvLvszDDmJNOzwB-unTzNQJp186fpXAM8ta3Fp1qaTKcw9EY8sdzhnTLIYDQXq33n2RNBDyx-_c7zW9qH4NebclowF6eISEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترسناک‌ترین اسکرین‌شات ممکن</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/3219" target="_blank">📅 16:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3218">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">آموزش اپلیکیشن Cloak برای کانکت شدن به کانفیگ‌های SNI Spoofing روی مک
با این روش هیچ نیازی به استفاده از ترمینال ندارید و خیلی ساده‌تر هست
و همچنین توضیحات راجع به شیر کردن کانفیگ‌ها با دیوایس‌های دیگه‌تون
این ویدیو باید تقریبا تمام مشکلات دوستان مک‌دار رو حل کنه
لینک دانلود داخلی ویدیو
گیت‌هاب اپلیکیشن Cloak
لینک دانلود داخلی اپلیکیشن Cloak
لیست کانفیگای جمع آوری شده توسط متین عزیز
نکته: برای اپلیکیشن‌هایی مثل تلگرام که سیستم پروکسی رو اتوماتیک نمی‌گیرن شاید لازم باشه یه پراکسی ساکس دستی روی پورتی که اپلیکیشن توی ویدیو بهتون می‌گه اضافه کنید
نکته ۲: متاسفانه این اپلیکیشن هنوز تانل نداره و ممکنه یه سری اپ‌ها که سیستم پروکسی رو نمی‌گیرن باهاش کار نکنن.  برای تانل پیشنهادمون همون استفاده از
Throne
هست
پی‌نوشت: عذرخواهی می‌کنم بخاطر کیفیت فوق‌العاده میکروفون :)))
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3218" target="_blank">📅 15:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3217">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔭
خب گویا GitHub دیروز یه بمب سنگرشکن(
😂
) امنیتی خورده. خودشون تو توییترشون اومدن جزئیات رو دادن. خلاصه‌ش اینه:
⚠️
یه اکستنشن آلوده‌ی VS Code نصب شده بوده رو دستگاه یه کارمندشون. این افزونه مثل یه تروجان عمل کرده و دسترسی به ریپازیتوری‌های داخلی گیت‌هاب داده. هکرها ادعا کردن حدود ۳۸۰۰ تا ریپو دزدیدن که گیت‌هاب هم می‌گه "تقریباً درسته". اما عمق فاجعه اینه که هکرها تونسته باشن به ریپوهای سازمانی و API key ها و غیره شرکت‌هایی که از گیتهاب استفاده میکنن، دسترسی پیدا کنن.
و خود کارمندهای گیت‌هاب هم در مقابل:
- سریع اکستنشن رو از marketplace وی‌اس کد برداشتن.
- دستگاه رو ایزوله کردن.
- کلیدها و سیکرت‌های مهم رو همون روز عوض کردن (rotate کردن).
- الان دارن لاگ‌ها رو می‌گردن، چک می‌کنن چیزی مونده باشه یا نه، و منتظر فعالیت بعدی هکرها هستن.
گیت‌هاب گفته فعلاً فقط ریپوهای داخلی لو رفته، نه کد مردم. قول دادن گزارش کامل‌تری رو بعداً ارائه بدن.
👋
چرا این خبر حسابی وایرال شده؟
- طنز تلخ: مایکروسافت/گیت‌هاب که خودشون VS Code و marketplace رو مدیریت می‌کنن، با یه افزونه مسموم هک شدن! و برنامه‌نویس‌ها توی توییتر و Reddit دارن می‌گن "ما سال‌هاست التماس می‌کردیم marketplace رو درست کنید، حالا خودتون خوردید!"
- ترس عمومی: نشون می‌ده حمله به supply chain developer tools چقدر خطرناکه. تو دیگه کدت رو هرچقدر امن نگه داری، اگه اکستنشن VS Codeت هک بشه، همه چی تمومه.
- مردم دارن می‌گن: "دیگه به هیچ اکستنشنی اعتماد نمی‌کنم"، "device protection لازمه"، "Self-Host و گیت‌لب بهتره تا گیتهاب" و اینها.
و نکته‌ی جالب توجه اینه که این جور حمله‌ها دارن تبدیل به یه روند می‌شن چون هکرها می‌دونن توسعه‌دهنده‌ها ابزارهای زیادی نصب می‌کنن و permission دسترسی‌شون به افزونه‌ها هم معمولاً بالاست.
این نشون می‌ده که حتی توی دنیای امروز، هیچ چیزی ۱۰۰٪ امن نیست
📚</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3217" target="_blank">📅 14:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3216">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سؤال: چرا نمیشه روی اندروید به تنهایی این متد رو راه انداخت؟
جواب: دقیقا مثل روش Paqet، اگر خاطرتون باشه متد SNI spoofing هم نیاز به دسترسی ادمین داره و برای همین باید گوشی اندروید، طی یه فرآیند پیچیده‌ای(که جز ضرر هیچی برای گوشی من و شما مردم عادی نداره)، Root بشه.
سر همین تا قطع نشده یه لپ تاپ ویندوزی‌ای گیر بیارید و انجامش بدید و استفاده کنید</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3216" target="_blank">📅 14:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو: https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3215" target="_blank">📅 13:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو:
https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری تنظیمات خاص، لوکیشن ثابت آمریکا بگیرید.
با تشکر از کاربر توییتر
Kharabam
که اون قضیه‌ی رجیستری رو یاد داد(توی ویدئو توضیح دادم)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
ابتدا ویدئوی اصلی SNI-Spoof رو باید دیده باشید و راه‌اندازی کرده باشید:
https://t.me/MatinSenPaii/3186
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/MatinSenPaii/3214" target="_blank">📅 13:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شاید دوستانی که تازه اومدن ندونن. اما رفقا من بارها از دی‌ماه که فعالیتم رو شروع کردم این قضیه گفتم.
من برنامه‌نویس بکند هستم اما متخصص شبکه نیستم. صرفا کامپیوتر رو دوست دارم و متدهایی که خودم یاد میگیرم رو سعی میکنم به زبان ساده واسه‌ی شما هم قرار بدم.
کار اصلی رو هم توسعه دهنده‌هایی که متخصص شبکه هستن و اون پشت دارن زحمت میکشن انجام میدن و من کوچیک همه‌شون هستم و تشکر بسیار زیاد دارم ازشون.
یک سری چیزها رو هم صرفا از سر کنجکاوی یاد میگیرم یا ترکیب کردن یه سری چیزا با همدیگه و صرفا محتواش رو ضبط میکنم و می‌ذارم
❤️
کانال یوتوبم هم قبل از دی‌ماه موضوعش انیمه و مانگا ژاپنی بود
😕</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3213" target="_blank">📅 13:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هردوتا ویدئو(دانلود با نت ملی از یوتوب(بدون روبیکا و بله) و ارورهای رایج و ثابت کردن لوکیشن sni-spoof) رو ضبط کردم، منتها چون گفتم SNI ممکنه قطع بشه، اونو زودتر ادیت میکنم و میذارم. ویدئو یوتوب هم بعدش ادیت میکنم و قرار میدم واستون(همون که دنباله‌ی روش MITM بود)</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/MatinSenPaii/3212" target="_blank">📅 12:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر اینترنت نداشتیم الان که اسپوف وصل شده موندیم با اینهمه اینترنت چیکار بکنیم:))</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3211" target="_blank">📅 12:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3208">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امروز اگر برسم هم ویدئوی ادامه‌ی MITM رو داریم(سر یوتوب) و هم ویدئوی تغییر آیپی اسپوف برای گیم زدن</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/MatinSenPaii/3208" target="_blank">📅 09:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3207">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رفقا اسپوف همچنان وصل؟</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/MatinSenPaii/3207" target="_blank">📅 07:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3206">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDI5l7ziyIO75gFTztbHG2NKyBD-HoHsLZa43JvbmNhnEkLCG0bxa-l9csTdGGibt8IcuslFc6p6yXx_h_sZjs4XbYxh3Py1wFVwmXGmSxIWp49xHJHfeL-He20w8WxFj3ma8VvSvklqrzWWAn2JL49Yz2Zot8kdOhIn7P6Y6-EZ2Bm3C9We9FDvGSFqAMVNDvSMHHhZkhj47eeJtLl6kHpHb5yY-giXb0ixk3WD90v6ruwu-T1LmSzByGQpWk6wnKXg0Q9uSWW_xa0u5ly3mPVDtEf9lODgmkPEjjdin2LYeNLGvAPbLtKWuomP0Vbn9s3LmuWRnGmz2C3tQwL8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت رایگان برای یادگیری باگ بانتی :
vulnweb.inst.lk
@Linuxor</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/MatinSenPaii/3206" target="_blank">📅 23:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3205">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">خب این هم آموزش SNI Spoof برای مک.
فرآیندش برای ویندوز و لینوکس کاملاً مشابه هم هستش. فقط باید فایل اجرایی‌ای که برای sni spoof هستش رو مطابق سیستم‌عاملتون دانلود کنین.
فرقی هم نداره که از چه برنامه‌ای برای کانفیگ‌ها استفاده کنین.
لینک دانلود برنامه SNI Spoof برای مک و لینوکس
برنامه آپلود شده در تلگرام
لیست کانفیگای جمع آوری شده توسط متین عزیز.
کانفیگ JSON
لینک دانلود ویدئو بالا برای اینترنت ایران.
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3205" target="_blank">📅 22:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3204">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/MatinSenPaii/3204" target="_blank">📅 22:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3203">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AyUp8oSPX4i2fg5GwyYWPTs1L15GcrKdme6TCRw-nVNab2rzZVSltlud3_dlV_rRTpL2wzPapkGf9FM6CmW6FFM_py3zRyeS8rUIIUqceFULDd0uRqDbLvh7z6mauQEONsJCa6eDKuSOrLWbEax_JL0wuO9jBVWyEHHvHRfyw3xrNX0MVRJVSx9dtxNvwmROT3lgSzurMM_fpiLIG3L3RVqIpFfCgGnCt6SgrowC6YJR_Ka59tM53mGkV3AgP35Yq-puqxpnGFeLn_ioSUrOQtjQ2ZjEUc9O9nfzvoRfRlEzoQzQTBvOh8DdvH4DsrVKvC7QSK-xYnf_GZH4E1oygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ارور به علت پایین بودن ورژن ویندوزه</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/MatinSenPaii/3203" target="_blank">📅 21:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3202">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک سری آیپی‌های کلودفلر وایت شدن گویا.
اما اختلال زیاد دارن
میرن و میان
اسکنرها رو روشن کنید، با تایم‌اوت بالا. ببینم چه می‌کنید</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/MatinSenPaii/3202" target="_blank">📅 20:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3201">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه حسی بهم میگه حکومت یهو باز میکنه این متدها رو که ملت بپرن بسته اینترنت بخرن و مجدد قطع بشه، نمیدونم واقعا. قشنگ یه الگو شده
هر دو سه هفته یک بار یهو اسپوف یا یه متد خیلی راحت برای اتصال باز میشه و مجدداً بسته میشه. اعصاب خورد کن شده. نه دارن باز میکنن نه دارن میبندن</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/MatinSenPaii/3201" target="_blank">📅 20:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3200">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a_OszKu29_IBiBivBk1HMGuZNFHUMhfn4e3izpcTwv7GneXInLtgZGcB0jqe-Fn7X-PX6I3k624fFpM2K2BTbsC3ZR8myEiVUaLXCZchLqidlRxni8KKGHPLhHZCcfTod3fFXcqhRjz9kniKTkYk9Z_dkNODhac103JgoleVDmHZVhLQz8Cqca-ZqKDksZk8lUJ9SkXNjm-hiajwBu0ZTZzMbnCxesSrU5TvjOlN6F1-QToGHurEze37N1tHxfPohoMhvkZdzqtCIcrLV6WzhJlyQhTAI5sG6nMDNR6ihTfOAC3Dim5ihNmAHx0gAwPewhNSR8g6r5WjaPjAYuvT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر پنجره باز شد، و از کانفیگتون پینگ گرفتید، و -1 داد و اینجا هیچی ننوشت،
یا مجدد، WinError6 داد و بازم -1 گرفتید، یعنی اسپوف با این کانفیگ json(hcaptcha) روی اپراتور سرویس‌دهنده‌ی اینترنت شما بسته هستش</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/MatinSenPaii/3200" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3199">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آیپی‌ای که اینجا بهتون میده، صد درصد کار میکنه روی شیر و خورشید و MahsaNG
❤️</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/MatinSenPaii/3199" target="_blank">📅 17:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3198">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fM3UDTfQBhHFQ3GL5yWWQs4qgH5bretoz0GLZCgISQ9EtAhjjNWMusjevcxLJEOFRfmL0GNI7cCtEMDG2qYD0MFSCYiJxjSOS_nEtisUah8kQeBpBQ-Ywn4GVGgvkblTmnwGUW1qw2u9wtLmQikw6s80q-jzbn1nwYaF37Y7bT7RyIVwEAoBbk26nzqiqCDkxg36HDgcnsb3m3rSdYtTg4hqVUQJdYxaMPhweMyGU03zLsPZ_5dAn5BHQdS5Dw1tu-z7MBREsyzSX8NIXHCRjodOehrRV-rydMOJMomhIoX2RdTBDJhlYSt_qURObI_yx4F_GzMutn73CisvW-Mxbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ رو هم چک کنید، اسکنر برای Akamai و کاربردی برای شیر و خورشیده https://github.com/mirarr-app/network-checker</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/MatinSenPaii/3198" target="_blank">📅 17:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3195">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TGUL_mHnGjBh1pYMcpmLGzp2bcoxnRJLF0ooOYwmJOrrkMuKVIafDvDjlsHP7-KzlJZeLyDokbk3zj2xVoHCG1Eh5p6mxmnKu1xSEUQltqaAbYdDCGRb5x-yf5nHWt-KSKExARdXFVUWW-rMzUtr-QdCigpJXcGwyTQCRsiXpp-qGXH2Pb1-hllp8Mr14ZYSIxei9HxvtTe4OTuplHWP6-Oph9XeY19W-ku7frhug12zR1NBqrkpNTiVEVM_LZeXLrPNB7AzJAPqGbuz2hWTYJxevJUPwvBvUNJ5D_3g444XeYVeeOq5Jsd2RMR-lm5CyLIVmJ-_0um1KON5D7fJFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/MatinSenPaii/3195" target="_blank">📅 15:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3194">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دقت کنید، اگر خود Spoof لاگ داره
و V2ray هم لاگ داره اما پینگا -1 هستن همچنان
یعنی مشکل از اپراتوره. اپراتورتون رو عوض کنید و با هرچی سیمکارت توی خونه دارید تست کنید. روی اینترنت خونگی هم به کرات دیدم توی طیف وسیع‌تری پاسخگو هستش</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/MatinSenPaii/3194" target="_blank">📅 15:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3193">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/MatinSenPaii/3193" target="_blank">📅 14:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3192">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WdFE9zDIYaMgXO8Xc8ReVKl4WUbykSaKfHJK0iBYY_cSd2kwJnH7ED4phQVrEv7BFrE2kdURbfKLiDLzWEWq3hnx9wdzSvmgP-mmQUZH85-_y_75kNgOWa8TCqgYsKbyXSudBgyTeC2fabr8RnRIlzQqqsJ_ZXPtN-a03xfgwdV3XwgMGCXGATC-bXPPTlfV8PepeTVzsKr0elRbjpvlh8UlVDx-VLe3BJmrZadHjCwuiEkBglWIyj4scVRz1AftouvWzJBmo01W7Viv5WAzbVNstXN9X-TaXUc83gnbjnozyyB1_4fU-i54K10px3xkRL9Xsc175lf534QcjtOp5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا داریم قله‌های پیشرفت رو فتح میکنیم</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/MatinSenPaii/3192" target="_blank">📅 13:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3191">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یکی از دوستان گفتش که روی آسیاتک، خود hcaptcha پینگ نمیده اما کانفیگ‌ها وصلن روی Spoof
یعنی json شما باید همون hcaptcha باشه، خیلی عادی ران میکنید و پینگ میگیرید و بعدش کانفیگ‌ها بهتون پینگ میدن.
راهنمای کامل</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/MatinSenPaii/3191" target="_blank">📅 12:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3190">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a90f10d4b.mp4?token=liSSch7xQiFfnH0k6Ri6UpEIaTrJC3tAV5miaoGdoljTdAD_95fJGoLm0_RqF1VEmiJwJXUTpMbLkNMpOV14DAJMjDEb3FXPPysDB-Obhd9h67FuGuZCx_6q44fwYybKMvcoRHYw6B5pLGiYVJYrR8G-EHE__u44U6Fu8gC3oJXr-BIjiXsamm4abzoZcGr-CBlxOIL29GLEB8j7uMedgbH_YCkjyY90rjwM2-R4tIm16TA_BzXS3M48Z7wIKZatb05FhiCJvbkHQxnp7jB2PNQGzOq03SqMIq_W74vnWkzE6bvTygAZJODCywdTblK1RjALE1UpL_SAAQpHrEogtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a90f10d4b.mp4?token=liSSch7xQiFfnH0k6Ri6UpEIaTrJC3tAV5miaoGdoljTdAD_95fJGoLm0_RqF1VEmiJwJXUTpMbLkNMpOV14DAJMjDEb3FXPPysDB-Obhd9h67FuGuZCx_6q44fwYybKMvcoRHYw6B5pLGiYVJYrR8G-EHE__u44U6Fu8gC3oJXr-BIjiXsamm4abzoZcGr-CBlxOIL29GLEB8j7uMedgbH_YCkjyY90rjwM2-R4tIm16TA_BzXS3M48Z7wIKZatb05FhiCJvbkHQxnp7jB2PNQGzOq03SqMIq_W74vnWkzE6bvTygAZJODCywdTblK1RjALE1UpL_SAAQpHrEogtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/MatinSenPaii/3190" target="_blank">📅 11:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3189">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✍️
سؤالات متداول راجب SNI-Spoof:
1- ارور WinError2 میگیرم توی اپ؟
این ارور به این معنیه که شما نرم‌افزار رو با Run as Administor ران نکردید. اگر مطمئنید که این کار رو کردید و باز هم این اروره رو میگیرید، به سادگی یک بار ببندید و مجددا باز کنید.
2- ارور WinError6 میگیرم توی اپ؟
این طبیعیه کاملا. باید هم بگیرید. اصلا اگر این رو نگیرید یعنی کانفیگتون کار نمیکنه. همینجوری پشت سر هم تکرار میشه و این اوکیه. مشکلی هم نیست
3- پس اگر ارور WinError6 میگیرم یعنی وصله؟
نه لزوما. ممکنه همچنان Hcaptcha روی اپراتورتون بسته باشه. پینگ هم بده اما کانفیگا -1 بدن بهتون با اینکه WinError6 هم میگیرید. با اپراتور دیگه‌ای امتحان کنید.
4- اگر
Hcaptcha.com
بهم پینگ بده توی ترمینال یعنی وصله قطعا؟
نه لزوما. توی سؤال قبلی عرض کردم
5- اگر
Hcaptcha.com
بهم پینگ نده توی ترمینال یعنی قطعه و کار نمیکنه؟
نه لزوما. توی یه برهه‌ای Hcaptcha پینگ هم نمیداد اما وقتی با اپ پترنیها ران میکردیم، کانفیگ‌هامون پینگ میداد
6- با چه اپراتوری بهتر جواب میگیرم؟
منطقه به منطقه فرق داره. همراه اول به طور مثال یه جا وصله، یه جا قطع. اکثر اپراتورهایی که دیدم وصل باشن، ایرانسل و سامانتل و رایتل و فیبر مخابرات و مبین نت بودش و adsl خونگی
7- کی این متد رو میبندن؟
به قول یکی از بچه‌ها هروقت ثبت نام ایران‌خودرو تموم شد:))
اصلا مشخص نیست کی میبندن و چرا باز شده و...
اما تا وصل هستش کارهای ضروریتون رو برسید لطفا. آپدیت‌های سیستم عامل و...
فقط روی اندروید حواستون باشه سیستم عاملتون نیاز به لاگین نداشته باشه بعد از آپدیت
8- دقت کنید، اگر خود Spoof لاگ داره
و V2ray هم لاگ داره اما پینگا -1 هستن همچنان
یعنی مشکل از اپراتوره. اپراتورتون رو عوض کنید و با هرچی سیمکارت توی خونه دارید تست کنید. روی اینترنت خونگی هم به کرات دیدم توی طیف وسیع‌تری پاسخگو هستش
9- چرا نمیشه روی اندروید به تنهایی این متد رو راه انداخت؟
دقیقا مثل روش Paqet، اگر خاطرتون باشه متد SNI spoofing هم نیاز به دسترسی ادمین داره و برای همین باید گوشی اندروید، طی یه فرآیند پیچیده‌ای(که جز ضرر هیچی برای گوشی من و شما مردم عادی نداره)، Root بشه.
سر همین تا قطع نشده یه لپ تاپ ویندوزی‌ای گیر بیارید و انجامش بدید و استفاده کنید</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/MatinSenPaii/3189" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3188">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sM_yC7ocdTAilfSGp-foGS6TOLo1Hx3Qf8ef5ozBT_tsTAA7shmxEa__fZ0tp5ICJbaSO9XvFSrO072PWG9dxfm_BmifA7THFihAQfKjFGusmD8C17-iN6smBHxN3iLf4YIszIfFo0st8LuAk_AEinTCIYMLo0nWmLzdC_99Yvzo0qiPfDu9dbR7L3UZur7J2yuAxxAJAzdATvzeYo2SFByi2LcrnL7kTbD9MeA3N-OxFCPSnqL0DZBVbK7O-aFDoeTwq2m5wcLJ-sJfoZSHPSMvsHbfkG7bgf5ujlk2jcirh6FYoGX_tMued55Ou8FyRGrtFn0lZU7nJHa9T59Kqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)))))))))))))))))))</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/MatinSenPaii/3188" target="_blank">📅 10:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3187">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Matin SenPai
pinned «
⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:  1- آموزش پایه: https://t.me/MatinSenPaii/2627 2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید: https://t.me/MatinSenPaii/3168 3- و کانفیگ‌های این پست: https://t.me/MatinSenPaii/3183…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3187" target="_blank">📅 10:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3186">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شاید شبیه کلاهبردارا به نظر برسم اما می‌خوای نامحدود به اینترنت آزاد وصل بشیییییییی؟
😂</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/MatinSenPaii/3186" target="_blank">📅 10:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3184">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kqlY6GVE_XSGiEhNf3_k2ebWm-5UE7ZSm-Br2Sjuol_bOg47VFytxiEVdw9FgDdZuRnDEIylUIN9YddVSEOV0Cmz-rrb5FITFdKJile0xMJchLiK0MJ0AKDGEAlvUFN9MDV4-LXAZGqSc4xfJfYYiriPyWr4R-ubS76gN-nW9NtczSaRtMTZVj1zDygE4Pd-zHEk3xk0qTyCGBAPReZOuxFA8x3EwEKqaj09Y9RsuWH1uPDhb7TtNO1JcH_WYTespdKlT_6-OyiGjO7JMmu-bs_BgwKQV5-Au96oDMQwbj7AzcmLWMRltfT91mIXnnfB7bve87AQhuCV1eYrkyfGcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d2REzJZ9PEDszxXvIq3DunEi4KT5dTtm05PcdFS-K9mFi-jHJQVTKacmUxSqxhVITtMDbP66D9C6dHchmv5uoAiOQ8KEPsPxIC4e5r9k6QCA9weQr8yOBpZ9QRBLsRkfEnVLNHd1n13NRPuAPJmhZoyWicU1tNsPA6PA-Rv8tj2SEm2TjVvd7d7IFBEdT05_DWT6GxqxJZ0glJJYmtPZaYF8brYw_eKtU1ZTRpw5eOaI0ENODk6oII6qJhZs7P12zbVkJRD8heOIcwsxcy__HI8vsq-Rgd8bTwIdaxgIbnvjh7Qelo-036JbzQwSZnRyumymPLu1CarZX9KrjFBgCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاید شبیه کلاهبردارا به نظر برسم اما می‌خوای نامحدود به اینترنت آزاد وصل بشیییییییی؟
😂</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/MatinSenPaii/3184" target="_blank">📅 10:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3183">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/MatinSenPaii/3183" target="_blank">📅 10:11 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
