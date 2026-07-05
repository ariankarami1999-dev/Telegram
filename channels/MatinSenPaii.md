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
<img src="https://cdn1.telesco.pe/file/ZeXry-49a_8b481VFgm2jv5OIaEh35a7LCeQiVPKKisVD3koZsqUQxBK0CnMIXVhmC_yqAhbKNqCGIcOC5kKJjA0M4BKzi2hlRkHvBwUp_UCh5qO8nq3bJ9WJ46Ty4y2d5gE5rq7HB1S3vSA_QY34OQN3rVpEJnXUITHPioMMMAUTsACq88n10fN1XhcW3VHMUUGxQgUjJ2nuOH87C3zuHqyZ-Z7BC-LvuXcmrxu3U5qEXiWpbADUc9G6XZfnhEdX_OLURnK28Ag9wdYxNQcZFPURLCfyvSl1HQXlK-vqXyuaAuFxXl8Sm8_m6SlSDVFw42DnivRVayREbhtqSFyfA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 159K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-4250">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4250" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/MatinSenPaii/4250" target="_blank">📅 21:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4249">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بهم یاد داد از این وبسایت‌ها برای جزوه‌ها و تحقیقاتم درست کنم</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/MatinSenPaii/4249" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4243">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BVDkHO_gTEwD7K-bX1R9rNhogVyIQRDnh4lHCzYHpS8jg5WxRnYMaF3Kw0b1MV4Z9mkH58NwsWYC4hxSX8clwrFO9H8oWiyOi9q_uRY3yt9GYx7InJT8TCsEkHDPOBWaeMtyifE-V6zP2vr0H_h9PG91OIAoay88YxSAXE1pszJEp6LeOHBSZEZVZILeFPFYb5Q7QYnfmIVYjTKBno4JtYtuIN-7fU0Nn5h7rtvoTrkvbaKlIDVX392nPVos5C6XaASsSu1ifSKu2AY5fH1qtM3FuE1JazrTkhcy2CymIJhg6tvwaC59aUopmvJHVbRqY6yV6yaAAcTkbQ4JSswjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IgtKoMGq-IdrW2h4keKS8H5JUl-perj2B6DCi6tBEwOu7DUKSiw9GFGmiDK1nBkbnbjQ1PJcdHIhS1G--2Z-_en91rOX1rTI8JQJUbmX6pu4gU_Yqfnjl4hxvFcjtuhhtH80Wgu8o7VffTHzIcx3ekcLxschyxJe6DOxiCgF05c6dliaMOuGrF0wjjmGQrUe6LMnibAIMA45xn3XFzjCzrrEXRSnC8dnVCe3T33PE0z1aW3a7p2XMkPkhrl6jb1-oT1QOamjvTgpuJQzmqBl3Jx6r8iccs2rlb1jMrF8M7MQVQfQO1UsD9fbSWRAZoeSZq30XH5P_GtlrJw2NGO8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RRCuSZ8S_uVdlqVuOYF5BLaETKN2xAwaC0iGf-mDqsRH7GQDoFOIlEnonZ9399CAz0SSkFLs0T3JhzfZ5LFNbYX67anHY64TvghZOYwJR4QUgc4ntlVSXPo2qFQSK4rm8QzdH6iDqaSTWieEMEr4pjwpRiM1EDcLKapebxYujFL8cqF5ZkPIgMXgDriuaxKX5m_05XlW5aiw5nXRK54UjWq9jvsdudwxO6Upn_j73CfhUW-SgiGS-hsGEVAUKZJNWMFwOlmGeubQWARjHp4Bqzpu0M6PAYlMSYQ0RLqE0fPMmrUtXxAnhx_gEx7-a-QtfSdISdTHRu_97uRSBylD0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HIt0KUPKG0yrBjN9S8tkHdKtZsrCQqa80UqCs19-4eckSJYyEkxIn6izNPmBSNKlKAQwCQmct7Y2oVQ0fdH_1zZxvgbTMdS64gYDGeeOrgwPurxioNL-MlXcT49KfF4MWKwRm8ZezS9G2w3nRJHtlsOhHGg3C4XLl8ooGSpbymZaBwtEBxG065LzJ5vRoGJKCgc116OclIgttSJ65rFnWYrArDNWA0UbyAtTsufHmHWnLX7lfIG5gibm9NOMpmCncS6Gpo8q-ZekY5buz97g6LQBC6YXH6e_Mta15UxTj7-QW9e3iezhTBwwB1NgiEJbI6sN4ysf57UcnOimLDhBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RmmbEWzLJxZCxjgT_Z8tSM5Vus9Fko_z68Lu9I4WV0SilnpAcXkBIkfQupl81uDJw8pvoCzAoOvCR3Qg7MKrpVdBipRLDuHCdc1dVgaqaUl14eGPNST0WoJfz9OIikm3_4lHt9rUmvlLLIWaDwpusfSWUn5215Urn1dLSMJpLfjBoQ_vuMph2y_bcucsp0v1mHZxzJAm3GfcM_o_Bbpuhy3oTXJXxht_VaJcaENxpKwvQzCeKoFu15cmVNlKf_tJW_RPEX_eCqWzsTwpBSTLEI35_K4Gne1XK_te9LJYt-c1h7xWDcMv_tbTnrfPS4RJrJaL96tEHOUVj1tmM4xxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LtOFf4sZZ3aQyjzskvK-fm4bJrvZC9zGBmqGLq50B-zHr3ARcTctGNGwJPniDUrvdWP3QMWDsje6RWp2-7CDAbsmfI-_-e2jnr_NBAYAw3e4Y5xOChyB42kb-qFrqrAJPy3GcA9EOqZ4X5_aWzHp8o3VlTPXmiRojVJLaCt1IOI_gTPIoIAZgWCdXxxUcPqMhx3aL4pmrjODbft6meACU3XiRpDuWQvuFVIXIn1h81ahDMl5tmFcTzU0B0h6Lpsmnw-uLIs3WoO1aO4TM0exzDwxs6CbLk8YjF3Ey8F-rUt1NhcHbky9Xu6Fpt-gI-6mU5LD5rJ_FlhmHGygMbu7Vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم مهسا توی آپدیت جدید، یه صفای حسابی به UI دادن
😁
اما UI کوچیکترین بخش اپ هست که عالی شده.
۱- هسته‌ی سایفون برای ایران بهینه شده و به راحتی تمام، وصل میشه(الان با همون پیام میدم)
۲- اسکنر قدرتمند اضافه شده برای اسکن آیپی cdn_fronting
۳- الان میتونید از سایفون+آیپی تمیزتون، کانفیگ بسازید. مثلا من اینو ساختم با لوکیشن آمریکا:
psiphon://?region=US&protocol=cdn_fronting&aggressive=ON&cdn_type=any&cdn_ips=
104.16.73.68
%2C104.18.180.6&cdn_sni=
pypi.org
&no_sni=false&skip_cert=true&proto_tls=true&proto_http=true&proto_quic=true&builtin=true#psiphon+2026-07-05+20%3A26%3A39
۴- یه منو کامل برای Chain کردن دوتا کانفیگ V2ray(مثلا یه کانفیگ آمریکا دارید که کار نمیکنه، یه کلودفلر دارید که کار میکنه. با کلودفلره وصل میشید به آمریکا و آمریکا VPN نهاییتون میشه)</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/MatinSenPaii/4243" target="_blank">📅 20:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4242">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کتاب کامپایلرها و طراحی زبان - Introduction to Compilers and Language Design
اگر دوست دارید بدونید زیر پوست زبان‌های برنامه‌نویسی چی می‌گذره و کامپایلرها چطوری کار می‌کنن، این کتاب آنلاین یه منبع رایگان و عالی برای شروع طراحی زبان و درک کامپایلرهاست. خوندنش برای عمیق‌تر شدن تو مفاهیم پایه‌ای سیستم‌ها خیلی بهتون کمک می‌کنه:
https://dthain.github.io/books/compiler/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/MatinSenPaii/4242" target="_blank">📅 20:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4241">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تعداد پنل‌های وی پی ان بر پایه‌ی کلودفلر کم کم از تعداد کاربرا بیشتر میشه
همشونم شبیه هستن تقریبا. زیاد فرقی ندارن با همدیگه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/MatinSenPaii/4241" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4240">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بالاخره کار مقدمات و آموزشا تمومه
کم کم توی ویدئوها میریم سمت ساختن پروژه‌های واقعی</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/MatinSenPaii/4240" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4239">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vk_CkLElxwmVP5zCJIaqZEiFdL_61cGpyM6UTrDSwNtgj7_OCB7ZQVZVmBfztWVKzMrRWtgKOSUnO9N3ksSu83urZsKUxTrVnEKt7loK3cb0f_GiKg3eXaofEgdb_qcchOa1h092_xfNr1zq9Z4x-cre0lF37oiFZxblz30Jh8JHBDz6QkUtXO8oc35GfKFOP5k656gBpbic3XcGkilH5yCAUOsPF6_WMJieCIPPRYOyG-UpArixpGBHOQgLMroowLSj66DtuMkc9Vtdr5Eh0opG-q4NKYOoPb4vXZgMsF3Kz6aNzLgCnEeWAJoh_2dtUw7GEZ5WphevnAtvORGuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز Hacker News رو چک کردم، یه سورس تو گیت‌هاب ترند شده که پرامپت‌ها و ساختار دقیقی که برای Design System با مدل Claude استفاده می‌شه رو افشا کرده. برای کسایی که می‌خوان از AI برای ساخت سریع UI کامپوننت‌های یکپارچه و سیستم‌دیزاین استفاده کنن، این ریپازیتوری عالیه. با دستور /learn بدیدش به هرمس و تمام.
گیتهاب پروژه:
https://github.com/Trystan-SA/claude-design-system-prompt
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/4239" target="_blank">📅 17:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4237">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QjOc-sfGVIh3A5_PSqTAS4FJgB-Qc6rNcO88nFO9NHKip9h_pJ2Wn8SXBUXJVhW4b6R4aB0WXsGcu3uvD3_Nr32JefCeoNW7Wb_neM3NyJSy1MJiXQXgJRtEiUcR_paiSCujhryQg6z_mhJde2F1TC99OVHMdwl-oVk-51GqbRxa7gtgmm7lrvrl0XLxUSAFhKOZb73iufLvK0PgIIlJADkLBQAByHd_ri9zyDsXBCb64k1qM-cmHHt0BU94Q0PdmMS0Y9FvyVzxAf_gXcbX0YdBrjzg56FQ_-DEZQZ_qiGrzoPQACBDMjiG3p3wKq1xAij8UI8d50N_P2DwdliNvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ulYQjpulIYc8SXjQg8W6vAFcqUkSjdJUw4obumk0673CEzxqYnPJWCkAP0C4n_LcCRHUqdbCOR5KJt2gEyJyUzo2oanz5f_gjBAOXymzElrL0f9v9qXjpDHP1RIL-oE_Ari2P2CxuiJ6etVmxACW9NkuY5l22ptAauZUQLsxsL446OnV5UB0sZ1FCqtm1GADChSbD-jOj8pEDULAkwc8Eo-p3Q8vNhVBGUm9JoCWOv1EvmGh45gJQjBM4rQzCjdweGkr4sBCCo9u5WRQElDJs9rf8jXpOUBpLpcDU3gkP0LE5s8afjyUo3l1eQ95n_jG778V8AznKZD4Or8dQQruHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سری از دوستان کامنت گذاشته بودنکه این api nara که پولیه و کردیت می‌خواد و فلان.
سایت Nara چندین تا مدل mimo داره
که همین الان یه اکانت جدید ساختم و مجدد تونستم با api key اش به mimo 2.5 وصل بشم
شما صد درصد از چیزی غیر از mimo 2.5 (mimo hermes , ...) استفاده کردید</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/4237" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-Commands-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات استفاده شده توی ویدئو، با توضیحات کامل
سایت ConEmu برای ترمینال:
https://github.com/ConEmu/ConEmu
سایت Nara برای API رایگان:
https://router.bynara.id</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z-jBAwQej8LnN2rXgevtfv7DQExYE1Kft_w49xE_V2bKnd8WKNPaI_sGWFyo6Z3SbPoERyqzoFF07LRfaIKOcx5r7RL36G1f4pYkOv1CZnf6DCkvKWZaL7zhHNu2wMeI_mhhpfKBrNZTGLujnt7g4ARvmhe79ad3KAnwm2szCMvSTx8dOovVrkqqAbcRP07pC1NXPDRQaWpD_N9rvU2_NEe7P6393ugIRcCvQ8s1lQvSNv5RnnMVwGewuAYzRMCLgdJwikuBDrYF47qk3SEKags4jI5uvqxTFFfLnrLSmLz4iD3VDiaGZWNTCsHxz1g9Zl0vpMkRU4b6ckl2RFhDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
مثل یه حرفه‌ای از Hermes استفاده کن! 47 دستور مخفی هرمس که باید یاد بگیری
⚡️
فایل خلاصه‌ی دستورات:
https://t.me/MatinSenPaii/4236
⭐️
چندتا از چیزهای باحالی که تو این ویدئو می‌بینید:
دستور
/learn
: با این دستور به هرمس یه داکیومنت یا سایت رو میدی، می‌خوندش و کامل یادش می‌گیره! دفعه بعد که سوال بپرسی از همون دیتایی که یاد گرفته بهت جواب میده. همینطور ازش یه Skill شخصی هم می‌سازه!
دستور
/goal
: یه هدف بلندمدت براش تعریف می‌کنی و اون توی کل پروسه‌ی توسعه یادش می‌مونه که باید به اون هدف پایبند باشه.
دستور
/snapshot
و
/rollback
: دقیقاً مثل سیو/لود کردن تو بازی‌ها. یه جای کار رو سیو می‌کنی، اگه هوش مصنوعی گند زد، با یه دکمه برمی‌گردی به قبل!
دستور
/yolo
: خاموش کردن ترمزهای امنیتی هرمس!
دستور
/suggestions
: اگه گیر کردی و نمی‌دونی قدم بعدی برای پروژه‌ات(یا زندگیت
😂
) چیه، اینو می‌زنی و خودش کارهای هوشمندانه‌ای که میشه انجام داد رو بهت پیشنهاد می‌ده
دستور
/moa
: ترکیب قدرت چندتا هوش مصنوعی با هم (Mixture of Agents) برای حل باگ‌های غیرممکن. با چندتا مدل موازی و یه مدل تهاجمی
دستور
/browser
و
/bg
: دور زدن محدودیت سرچ تمامی مرورگرها برای ایجنت با CDP (Chrome DevTools Protocol). این یکی فوق‌العادست
دستور
/pet
: این رو دیگه باید خودتون ببینید...
😂
بتمن رو تبدیل به ترمینال پت می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4233">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند.
اما اگر ظرفیت پذیرش در ما وجود نداشته باشد، توانایی درک حقیقت را نیز از دست می‌دهیم؛ به‌ویژه زمانی که حقیقت برخلاف باورهای ما باشد.
در نتیجه، از جایی که گاردهای شخصی و تعصبات وارد میدان می‌شوند، گفت‌وگوی علمی عملاً پایان می‌یابد. علم زمانی رشد می‌کند که ذهن، پیش از هر چیز، آماده شنیدن، اندیشیدن و پذیرش شواهد باشد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4233" target="_blank">📅 00:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4232">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=jzzYSGLGPXub-BaY8Mp-MZrWYCnAPfUgPyGUScBOtfWAQKr4-9j15zZXGDnQeIKQUH7IIiKGBmzc0oRaGmQomNecTaErrJA8bJcM2D-rOmegOXG13pojehjKOSccovXVPje4dqq_MHu5cgDiGLZrWGmg-ptQtuYe8n8uS1IQLYufCkCM20pdaepqPHbgmflRJu9aGoHxAGTBvNHNFcEHqfr3mgUFcI7RtopH6Fe41ew_sZL8x2RIIxCVi3Qlu9vw3HFnt7lj9L0PYiP_hPlehiQnWEgORkvqXcqbjUPBF4-t4Dwu-jPwWXq_IJRNLZ4hwLzu9qR9cIP3XTZB4kNVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=jzzYSGLGPXub-BaY8Mp-MZrWYCnAPfUgPyGUScBOtfWAQKr4-9j15zZXGDnQeIKQUH7IIiKGBmzc0oRaGmQomNecTaErrJA8bJcM2D-rOmegOXG13pojehjKOSccovXVPje4dqq_MHu5cgDiGLZrWGmg-ptQtuYe8n8uS1IQLYufCkCM20pdaepqPHbgmflRJu9aGoHxAGTBvNHNFcEHqfr3mgUFcI7RtopH6Fe41ew_sZL8x2RIIxCVi3Qlu9vw3HFnt7lj9L0PYiP_hPlehiQnWEgORkvqXcqbjUPBF4-t4Dwu-jPwWXq_IJRNLZ4hwLzu9qR9cIP3XTZB4kNVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون عجیب باشه ولی من خوشم میاد وسط ویدئو به ارور بخورم و بهتون نشون بدم که ارور ترس نداره و میشه خیلی راحت، راه جایگزین پیدا کرد
👍</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4232" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4231">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sDrDjDZMcEHX14JoODM9-uPmNh9oR57WKbzD2eHEeSZ4lslcPoP7ph5G1bYZgn-nM_M3aYdvOVzaC_DmEybvNm5zHoDjSDAX9OAhD49w7dxePOPuvFjPSC5J06xU6jLgbajqRB_h9OmAhjMMAfiOS3b9_wvB7Prxij1uQ_KW5dB09U0yzvo5WDBpki5tB6YVZnctb3I1s33AP4_KGyDB1h0Nrh1iSUd0Vnqcy57-DkWHFMjHBXm8sltX0X7W4-K8llKQyA9PzeGhQ198UihZqNFUuesroTwN8Z99L5qlacfUc_Dq4uPOlGkM-bJYaB2dz9nUZmdVwVoDY5b1-UX3Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.  با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4231" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4230">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oEb8Y4MmjjLrwQL7YFm92Kc1yidckN2QERDn90XweCtXIQD0gZaOOgC9h1iLXcT5v4lcu3xg5yHv_zQ6TXBd_AOgz_mdBI9-hlig7VZ_lOkq52liBzlTN_LijZIW6VxVxVEl06G5ivMbveroT7cNBa5Qo9b144TzP7YJEBeah5WlzZXKzGtNEyonG3qeBFv-gl3UO7AK-hxv8nlvruHCb1Rv71CQ1ifvD5Cuqq2M_EGJCCyC-c5_mNnPIcZdVMItY634h_CzCho-xosYRNwY2gPR0-abOOcc3xIqk7roi0KDxj4xB2spVrti8f5ATURfq1E1SOrkm2okYxiI3faXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.
با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4230" target="_blank">📅 22:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4229">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">روش فارسی نوشتن درست و حسابی بدون به هم ریختگی هم توی ترمینال یاد میدم توی ویدئو. که یکی از دوستان عزیز توییتری دیشب بهم یاد دادن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4229" target="_blank">📅 21:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4228">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">توی این ویدئو که دارم ادیتش میکنم، کلا با cli پیش رفتیم و از اپ دسکتاپ استفاده نکردم برای هرمس. علتش هم اینه که پروایدر شخصی اضافه کردن روش هنوز داستان داره و محیطش پر از باگه همچنان. با اینکه آپدیت هم کردم الان هنوز همونه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4228" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4227">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy  فیلترشکن قوی و پرسرعت برای تلگرام    https://www.youtube.com/watch?v=pyvB6VSPhwg   @WhiteDNS</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4227" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4220">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n35UXbLW6whoRfTDVinhkgcx3MMNYA5UBScXZ0AHOYUfcXVThhBDZp9NrlZKUjTRqmLeoz3YgqgEezWk3UwLn0atcbIifAaoKucm_ASiZlQkxGbxFLCS4_6ONy-aznpwIBJZdAptntsHyrs3A1PmNXoHM3w3MfENzj0R-Ezx5rm7rwNe-UFCAvYWrbrokvzYc-GYww_fPNAs349z2HqtNqRCexke5xGgv23A6uY8Im_HUqibIFOL0taHOha3cWMAhXBjk2cKE08K9f3yMI-isuUw4Ppa6SoVFHn1bvDn-Cil0hm2mQJhnku_vkdQ8j3I_4UjogcZKk9_Ix34JWCJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S8vru_y4C14dx5I5yEQMeLKyqv7bg6lC1UlQUipBTvMOjtcDiCqner35eVh53wpfiwsroSyhYg7h53pGK1aD5xzg9jrlFPrBd9ZfNUiDHmSDAAzVAfJ-bghqMkz_CNxm7RDmk-VUsKki6i8CBvFCf3QBb-ymFApv1kDwq1TfO3QYYv6eZ_Gkw9baZnZzidAPUfpI7esj3On9KzOlfCjHMb0rVuZHhZUfYD3nzjX4NQJUO_4sgFEyPF0O3HfddAO5FxCjrMCTyM5SPlzmwCkQcoaF-fpq-uBvLyVaAMuYwDJNiusJ9oFpQL_DxPyBCzZcJjXCaO4eYuQLnkZHB2vxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TGk4zCuYoPF_8XsYkoPSsGKZiD4Ue7zCwpZT0aSIHFT67PCCoUXqLJG0f2z0ElghVEQCXVbD7dyMyW8h_Af4CxP3LOHaBayvC4qS4wwEEfJAFJcLU2GmTcEZCUN7t_ATOLYFbG-_z1ZmCUf4D2YgyYwi-1iLag005RLEWdzvfEQomaZkDHmZHsAxtGkSIdIiuKNEMDPXzLl33Xc5jim0dpVyQ0SNDhQ3bvsm2jBqx_RmQNTRIKQAUHRJScd7PjTDJe_umky3T-mT-etf5Z4lUhO8Alp3V8QE9nEatPLgmOZexr6FhP7HSvH-4NpExSP_Vy524ZjirUJYITQT0XZKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pa0AMth82DeTJ8iHJnQZZxNFazjkByI_p2EvX-UVPPQGgtH2dV2Vf_eRNC67vvbnlMuBO0cTSbtQog6UKoBHwyD7UH0Nxp5grT9JxOxyGkxWODq5cj93bOCo4HqBb566wY-uRj7bNi27WX-hdZTuUZNv09HAV-c7PmOwgWII2RcMTGJ5y1n_6porYduhD-oKE4itSTdT2Ik54pWN5ZXzCRu4jE4l2ifqssfXqJ2FgnTx1IiPNjKti2qqyCctSzlD2iPlHce4M0DDg3Idk8we7gtISrwsuyfbCBVxHbQhc2ixfI_UvHXEA7PPLYd610GjUgAHgKXTA0Dqq7J55bhLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V_bMojndbludwb29x6jBlGgDzjG1XueKGnZQrrIyvA-WHGlMMUOGlxEGK3BtMZbtCrj0dNF7YFp0MxTOJfDLg7cafiCaBQBU0v2E27Z-9lPU1GPZbOFmqk8pT9d3GY2-bvwYiEskzsjxmeHF6KP4gCvO3cXauJrYDiOHypwh9og84EeLMjs-VBZZBxSUWNueLCWc73xzSLux3VloTyI0O44IJd7i8zFq8pKTmx_w86YF7GH0XbEyYzi34HtmyayBWx62L8tarIBGdEy3uGCqheTppDDz9wxtw235-mq0y5A_3pUDHqiWfL34bVMRiwzjJbFGzsRG-16RG0hjvCzBcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G3zUziBzeARceNwnmwnHENvZtHapw29w9XxHsTciP6qr6psfVJ-VlJ_NoHKK94TRiahGC461YDXJfCDBfe38E5K44ClTAEuxstspPCiaWcyizKUQTWSSzWVvsE9Jv8KHhGzL8N4OIlaAQfiH_gse_bH2tSveem5EwmcUEhfKBbxrv4DP3kx3q7DEwJc5dWBrKrd8_HCDx2Cvt6EO-NIncLv1DmJu1X77KlFjdfyKH1UX-paQYO_UcFEhra_R4Mjq0w8gicHY3XffHk0dj038vuLi1A6NI9eFyvNqhl3yEfrCUPJ83O7XFe2uFFDcbz4g1eChbnTl1ahpsM6loi_Jtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:  1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم،…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4220" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4219">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UJw1EU6tektlKsdANCvEyo5y0-9wcMgtpMdzcOvwmUFEuyOS5PWA8HkrlbAyEjt8iO-9xTm-z_GAVBQTfZAUXiuZSwIKsdTBU1w8Hl9SK2_br2Iw7Afp0V6LgVWCMEoz_x9NgD8WwVus0pa22SSUjUjMJIRIV68187bnf_zQ9zqpsdZcdb-FhIWO1Y1s6wQxrzY8eF4xaXzHn2p8Akh_vAbzNQ4gCI_fAYCyb2qN_TXCTElRGcmqYFo5G81-Z0mgVsKronFXiuxFvScBV_BqHvz_7XVugRXLgXk8JZlIOQ8dES-7IXMeOcF2HDxdnzE5VtbkVN60xMdVTSY7F4m-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:
1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم، بدون اعصاب‌خوردی و بدون زمان زیاد اون کاری که ما می‌خوایم رو انجام بده.
2- چیزی که من از ویدئوهای این دوستان عزیزمون فهمیدم توی یوتوب، اینه که میان با مدل Whisper و یه انجین شروع می‌کنن به کات زدن(که همون هم پر از اشکاله و نیاز به ادیت فراوان داره) و بعدش شروع می‌کنه با یه سری mcp و یا پلاگین کلاد کد که اونها هم اکثرا نیاز به api key پولی یا اشتراک دارن(کما اینکه خود کلاد کد هم نیاز به اشتراک داره) یا یه سری ها هم با Hyperframe، واستون موشن گرافیک می‌ذارن.
3- حتی همین موشن گرافیک‌ها و... هم باید قشنگ و دقیق بهش پرامپت بدید. این نیست که خودش متوجه بشه و این کار رو بکنه. همینطور توی این ویدئویی که تام‌نیلش رو گذاشتم، طرف برمیداره کلاد کد رو اگر درست یادم باشه با Opus 4.8 می‌ذاره روی Extera High effort که خب توکن بسیار زیادی هم می‌بره و فقط ۴۸ ثانیه‌ی اول ویدئو رو باهاش ادیت می‌زنه(بقیه‌اش رو داده ادیتورش
😂
خب مرد حسابی، واقعیت رو بگو دیگه. که مابقی ویدئو رو دادی ادیتور خودت ادیت بزنه)
4- هایپ اطراف برنامه‌نویسی هم زیاد بود، و تا حدودی تبدیل به واقعیت شد و الان ai سرعت برنامه‌نویسی رو بیشتر کرده. پس شاید بتونیم انتظار داشته باشیم توی آینده‌ی نزدیک، با هزینه‌ی کم و یه اشتراک معقول، زحمت ادیت رو از روی دوش ادیتورها برداره. ولی جایگزینی رو بعید می‌دونم</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4219" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4218">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کاربردش می‌تونه اینا باشه:
۱- وقتی دوست دارید هر چیزی رو بگید و در لحظه کامپیوترتون تایپ کنه
۲- یه ایجنت لایو با Hermes بسازید
۳- و کلا کاربرد عمومی. مخصوصا برای کسایی که disability حرکتی دارن و مثل خودم توان تایپ کردن زیاد رو ندارن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4218" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4217">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه. کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه. github.com/cjpais/handy‎  فقط کافیه شورتکات…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4217" target="_blank">📅 18:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4216">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQcOZ6Uxr3AuUSwZytk5ICysJhpL9dav2M71l58sYoItqOIUVXqaOdzDahgU_Vrnd_n7S4_nvfrCRufbaoAOgZmG1wdTK26iY-Pp29brJxR3SPjh7qGFWLfO7Zuhzk5LhAu9D6SDbAX5Wn2-hnQCWZluYxbEHrosUrFYEx3Iju9sosx6N23RXDXdQ76ERWlknQ1nNPs2cRST2saCHjbB7nykQwhk9Hs92N0hZwlgk9XHYjcbdtYR_gVQ5O5SLd0hmPr-N3SVHQTks9diGFsN_xs7isPmw8PjLxhEWVwX2hbh_7dsYtmKhOcMl3vKYLISOiSgnU51kwAhB6rw-Cl0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه.
کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه.
github.com/cjpais/handy
‎
فقط کافیه شورتکات رو نگه‌ دارید، صحبت کنید و رها کنید تا براتون تایپ کنه.
اگر دنبال یه ابزار STT بی‌دردسر و رایگان برای لینوکس، مک یا ویندوز هستید، حتماً تستش کنید.
✍️
apt_hq</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4216" target="_blank">📅 18:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4215">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/so8ySR3z6b8a9UBo0ZQx-ugS7DnrrLXEm5RKLSP9XsXydEWJP6QTmK97BJdNBFjVuGsWfSz9uAskGsEeNvcXNyQr8a0coZul-HS_2e4O-fz5Qf_cLiUH3wTgrRYjvUzFcg2s7QAmCzJaTPEfeDOEkQSHofYExunnHlKaLMeR3X70_nkQx6a8fupKimonXse7pbXxFlo3osY9qHprsEyEqADm4WTK-cnZ9yJFux50W_tZQcXGXq2Dku-KIhyslfsMczO_IAS-vrIrqNr93DjZiImZFR4eRukxhZRlQb57wWH-VGx2SR8gV-nNymRi00gii3M_Fyy6FNU8l8vcMTxsHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دادم برسه
3 ساعت و نیم شد ضبطش
😭
😭
از بس دستورات هرمس زیاد بود یا طول میکشید(کل ویدئو رو با api رایگان رفتم بدون سرور و... و واقعا هم خوب بود) و قلق داشت انقد شد
اما ادیتش کنم ۲۰-۳۰ دقیقه بیشتر نمیشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4215" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4214">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برای مثال کیوریتور (Curator) که توی ویدئو توضیحش میدم، یه جورایی کتابدار هرمسه که تو پس‌زمینه سیستم بی‌سروصدا کار می‌کنه.
و Skill هایی که خیلی وقته استفاده نکردید رو پیدا می‌کنه و آرشیو می‌کنه تا سیستم سنگین نشه.
ویدئو پره از اینجور دستورات و همه رو هم تک به تک انجام میدم و تست میکنم و صرفا روخوانی نیست</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4214" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هرمس قشنگ یه کارمند تمام وقته. ویدئویی که تا آخر شب می‌ذارم رو حتما ببینید، تا بتونید از تمام پتانسیلش استفاده کنید</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4213" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4212">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4212" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4211">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4211" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4210">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXPP6ZknaQLsXm4JHOl7Wbo4Ki7bTYGVYGJQoU_axv2vduJU604B7p4Ql5Si9wgfl34i1-hN4LxKXeB1FwRKLt8grmwB-is7AbFYUvaFyXBIG4pzVFEiR6vEWa6pEPewcCBYzKrRmib6fURiuZXM0ZJRKhjz_e7CvMrU95qdJZxBxW8rtGUdjHCzrvFOZDhdtwDR2MgewP7nYGpBz0A7Gn-CXAxQQucXS03ehF6QTpZqL2h_2s-QplAzglgIG-E7z0NhewXZlFABiZ-Zmnew8YbShi-OgBJzcm--DBVGrCIv4A9GcMht3gJbx2nKESTxgnEqGSYilP8tBtArQOyz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داستان، ایرانی بودن</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4210" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4207">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RMSSqCNStpA-VNiXG-F0eH4OPZKoAQJFgEtSP5SvnMDr6yHbkQXA1GvisWjzzCosOGyjHjAJt8qz09Bg3IkHam4qEZhK-i7IOX1cPukhaiJ9YTEcFyziHovwwjGmWcFaAQSmR7MNrPHGgdbCCe6B8nFWJ5jZMvGxUmGMsXMpArhchfotJ-7Y3mzS3YAdCt79IBx0MvWjj2ijFTJ3yIZ5mThfOFDsdbajFsjoLm956nTKDjhSuHq6cpv6m4i5idJw22atYAcx-jJn_n6djIprVBMAcNT7sca2uO3m6bpKYsOU4aJexXAyxgEMOzv_bw5b0tml-mF9yzUZkd6u9UXsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tSvgLMCKPW7eRKg9wKmC7U1AL-Irz65FFC5Ka4wa30nLX9R-k5dIYcBv3ZidQvsg5iQL0xg1sw4zXQDWg7EjEUZ31ZHLjs3_qVpL92nfRmOAUzWsVRIgOjkQUN_jmaMx0v0z3LCvMeVCVeAckUWVZ5y6PJLUGB1Ko10HSLFZPPdKQynxksShlCIn5b5K_z3ahEwpfOzB_E_eU-1KaqWgF7dzSwfB6ZIyinCI-y1aMlIdY-hopO062jXPKyhLQg-_doAZLvWYQY-z2jP7go-GYMXFK0dHi7YUcgHEcBD4nHguzBfObTxUZ1CbJuT9QRYmT5bJI9TX-_CEyicw2tGtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vaZWlMpYKkzNwaZUf3ZemM1dmc47SDdTrGDDqqw1gJW5N2jbrTMjHn97oc5LwikdHd_q6ZLaJAinHtbMkqYJSYiO7ADgpiYHzMtSn0DOYXXQFYC8EtYr2u2W3-xfxUOASi0rAqoQpeI00GYSQ-AvGrgWS49KmOQCrSUn05g3NJWIMltre5N1x6nSFz3IxReW35WEJdn38FIw0Ddx_K1Rr2KotNczCZjkqvNv_8x3LVX3FqkExGJ5tbjF2tYSPsHtf1cLJE5GRplen3c_AR1-GMvr3vkKU-2RrucesSsIPrIB519dCt1_hYRsuNUKNmy55JqoZ6ZsR6m7sq6vV5G93w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی Hermes اگر از دستور Compress استفاده کنید، به صورت دستی زمینه گفتگو رو فشرده می‌کنه و چیزهای به درد نخور رو حذف می‌کنه. هرچند خودش وقتی توی هر Session به 50 درصد ظرفیت برسه این کار رو انجام میده، ولی تأثیرش روی توکن مصرفی خیلی زیاده! همونطور که توی عکس دوم می‌بینید
💪
/compress
—> فشرده‌سازی معمولی کل تاریخچه.
/compress here
[N] —> فقط تا قبل از N پیام اخیر رو فشرده می‌کنه (N پیش‌فرض ۲). پیام‌های اخیر کاملاً دست‌نخورده می‌مونن (وقتی می‌خواید مرز فشرده‌سازی رو خودتون کنترل کنید).
/compress [موضوع خاص]
—> مثلاً /compress database schema — خلاصه‌کننده اولویت رو می‌ده به موضوع خاص (مثل schema دیتابیس) و بقیه چیزها رو یه خورده شدیدتر خلاصه می‌کنه. و محوریت حافظه‌ی Session حول همون موضوعی که گفتید می‌چرخه.
حالا شاید سؤال پیش بیاد، که متین آیا این قضیه، کاری به اون حافظه‌ی بلند مدت و حلقه‌ی یادگیری خود هرمس نداره؟
✉️
باید بگم که اتفاقا چرا. هرمس قبل از فشرده‌سازی، memory flush انجام می‌ده تا اطلاعات مهم از دست نره و توی حافظه‌ی بلند مدتش ذخیره می‌کنه. و این شکلیه که چیزی از قلم نمیفته!</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4207" target="_blank">📅 01:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4206">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=jwHwC6XfoH7uZBb9cRgGlwjFm-tCnpp2Y5xlALZ1GuOESd2-0JhSd3S17qQKDWGK8kWukX68sohwHsa5Ro_TID5eqx8HeQpfclfPwmrPzRZ4nvqOpQ8DptkF5WkLTBUcfafW059oQrz_meVUK5PmDRdSypEp9uIxa_pzjYJZtg3hCllpQtsCbUUtThpdaeAFcOj0WqAD-ivTz0kD4kSmLEPrVpRmE_tf6_D1wkrsrYq_4e_6xaCE9ZbsbJOBTiqqNNiou4cwJs9ttgtdSWYWLi7j4q-UxtBzfGt-i-IcJUsrfvHtblzcur0K6YL_4vKkIu7tMVbqAbFHCJvO5fOjKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=jwHwC6XfoH7uZBb9cRgGlwjFm-tCnpp2Y5xlALZ1GuOESd2-0JhSd3S17qQKDWGK8kWukX68sohwHsa5Ro_TID5eqx8HeQpfclfPwmrPzRZ4nvqOpQ8DptkF5WkLTBUcfafW059oQrz_meVUK5PmDRdSypEp9uIxa_pzjYJZtg3hCllpQtsCbUUtThpdaeAFcOj0WqAD-ivTz0kD4kSmLEPrVpRmE_tf6_D1wkrsrYq_4e_6xaCE9ZbsbJOBTiqqNNiou4cwJs9ttgtdSWYWLi7j4q-UxtBzfGt-i-IcJUsrfvHtblzcur0K6YL_4vKkIu7tMVbqAbFHCJvO5fOjKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی نهایت آدرس ایمیل با یک دامنه روی کلودفلر:
https://youtu.be/Z069VNFAgAc</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4206" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4205">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4205" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4204">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lHLq3U7wbE92hOCOPm3A4wgSxPLy3ILkCQDXcdzr4DTx6TJWee5i0wGU0BfU249gnNYjNycJybToA4MNRWVf80sj8eu_eSfLRXOkegoXrtiI2Z5fS213iFHOp9aAkCNtGJp4hSq2bdyfib2fpNi_mxRgB6MILA-LuLLvqYpkv8N0Em-BKD9hc7V0X-Qlw0OTaZ4tJu2zOZ8xtxB7vleThgdPT_nL6Ra5KSjeyHM4Axpg-CykzUJ5GrBEqq1AoWeHy-lgwjvtEAYImtw3jGnhyD3B_KQIgt-3KKeM3sqo6oi5PswL2MF12WPcKuQFdSHeNeM8iNDd9QXucLF7dJQI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia
وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4204" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4202">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/meitaJZfy7ejZn9uVGohQUlKG9oxMNCYrmkY_uL8sD7V5EGj5lz6glg5t4Yaw-TU9w5iK-5rELsWXHO8uBotbt6tJlKhhAXsZZtxmW9HKUC57OdmoH9utZCg0YTGkjk6tKUt50Yp3KtZccyc-QTKo9mwpXlKkTDFiYlsvjnpY5fYbqGEtUshAGyHhTTIriJLda6kFUeyCK5xM1n5fES1zvR9YpG6nwLqH5Kcyxd-3OT0-cGM7kQLo0SyyLDUh3x6X5zN7t8F4tKbKkl8S8AJYWuBzXnEV2oGkp6ZZtl1czxquSd8G2c3xZNdX_qICI6bOsxdmmn_E44QXrBSKkT2mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GOwzoi1MLESTZTh9svUwVahHjz_5qPjUD1E1ZFiGtlzSKoKO-xLp9VBJR53EQZaceakkiyvBlL2s13pGStn8t__Y_ny9WJuRq4Dc542aeh8-dDqY_LiksVPnhCdNKg5bINXDvyxKA7vlqCQ_wEHnr-mrK2bExP5yD4SV6BwNk_ymtu0PWGwAhWFOQSUdz36gLTYjimK7euAOOI5tQ0_Bf_Ep_Ad-3sl58NnfqN5BntxFRiAlNqdhgb97HuvnVKrmgM3Vzn6qpqcY6Y5D-GWWGcqcJJyQKHXncePY1wZy-AEJZjTZKSmTjcG3rt-0zjZWx5H4dtEpAF-1XkVrTtxxoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چیز بامزه‌ای نوشت اما پر باگ. دیشب GLM 5.2 برام دومی رو نوشته بود که کار می‌کرد همینو الان با sonnet-5 هم تست میکنم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4202" target="_blank">📅 17:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jQzpRtJjigCrXyQh2_OFka5h1mBXDw9aRkG7733y1uuyweYeVDz2cYx3Fdm5mD-F0YgX2RJdziQtDP4Q3ZgjmSrySBQqBGoVybqQLCnU8MmkrMeFg30vML1yZ3UJxxBoczzDlHKgsIoTLNMEVF-iKxSyH0TD9ebgAw3_owj2jgFBL42dsSycael3EDKmDki4Ht0vgwmUxZ5xKIgN7zWjdeAL6tM4EXNrICropIuzbvcaD_lBrPtMx-8WBMeZDi59C1_nBSqQDvr3ktVXIbdj-1cWiz2OLwqVDFOw3_7EciyI-gT6XFuWa_nmToFTcSP2epsr-QtsgoRiS0wDrAKIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aE6ye_x4OzdPsSXgcpzetHPE6kLikFw4XE8Ay2l5wg2-3DHEuKdICqSx1GpFjzYpKgYm67L5MtV5ivrH7E8qwb-JOQjt1XWUTCeEspILcp0ah6C0ILy5M7Org-4fUIiA36qCPq0xEvlz2pCm-HS1kqgHb3b7ljkvor6hJXP5K0oR716Sn9THdYIH82MQpPs7KGywoMLv6XSglTFl0xQHMrQq_gNTzSaFQ5olYlx9cU-ylwE1KDR8d2q0thaAP9or5b3lxP2VVtEXaNOkuv5wZmuRURV-ws3PJcLutqbd37s8Q9aet8pPIeVsir4WsgY-aVasqUWY2hhD_3uL67S68A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بریم ببینم با یه تسک گنگ و غلط غلوط چیکار میکنه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4200" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RZigGfIxOZhWLSPZQPQI1Tt4l7HmGSmZIId6iMuv_2-lrP5olTswqnQFzG3vTsEi7ZuNHMfn8cUT9-HLZ3LR_MjIP6HyHwWOXzv69ItaDujisEsyYafUW3RaK7O7FOUrlz5A_FUub9rI525MQJnqqNFQ-ORmGj_P1z--7HGYPF73pQ8iNxWAFyKWWH5rPapkTN0uiKUfMI6yEMOpEJ9BXC74Qmbp5kvPiUHmI3mSOwmdym-bgBuAlCrlpdWI5TjJ99_RUf4I5HtlJ6Xo7XyYgPyIK5JDDSrlCu2aa659GsbrG6Q_o6er8HZ60IqqvqcJ77-MO0g3gXB2uYAO9TigjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با chat.qwen.ai نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4199" target="_blank">📅 16:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HLGzCZWe4EOJUwWpYnIcKbbK8fjM-sLtTOvoBGx941NgUDz0zzmO-8366O1HcjP23MoxjcCiX_YSQsuJCcR2A5gPPRTw4QrMP1mKZkVdA5HxYUWNcOYcK4Su65QoXluFh-TjytbpyYfy3R-Wi-eOr5YnWzBeykVB_690qgzG4bFSzb9MVYVp76jKipUWAf6bkMKdza9lTOri3B9O_bHMToFLQHQknYC5vyQIx29HQGbaSg8j7DEmrnAtMMyd6Jw85cdG_RAjOr3zpFtqh5eoUIfL4EisTNGDTtvsGOwgBcaFi7yK8aM3LJA6tltgmVSyeCERiigzVttKhflb6rMGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با
chat.qwen.ai
نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه پروژه بسازه، مموری زیاد داره، عکس میسازه، فیلم میسازه، ریزنینگ قوی داره و برای هر سوالت یه لشکر ایجنت بسیج میکنه استفاده از واژه غیرتخصصی تحقیرآمیزه.
✍️
بوکانت</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4198" target="_blank">📅 16:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">توی مدلهای چینی طبق تجربه‌ای که روی هرمس داشتم، MiniMax m3 خیلی بهتر از Kimi 2.6 کار کرد واسم روی api انویدیا</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4197" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به قول یکی از بچه‌ها هر روز جوری با Claude کار می‌کنم که انگار روز آخرمه</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4196" target="_blank">📅 14:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4195" target="_blank">📅 13:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4194">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/adlrJdfaNLvNDjNYv03cGfAunZyDF_Ze3xL5-dkZMIDhQXvAi5WOha6CwP7QxdGY7v_pwQi1D4YPp8rp8kLWqfzO-q1LI45TK-FaPuJIfN6iRzpHhHCKtSWszT1bgnfCwfh1XfjJ9dCRYXtC0wy4EPmKCEZCjVTp-_mhk4NHgS0hwJF6WMnyAyhFWItz2Qp7ABvcdILBBp1brVl_L7Hm-2YEqW79fWwdmS8kfM7hXA-gdTN6ztgKxyFt3CwyCtt_Eu_H71jZnnqyZMqVR31NiLvO_-vRbtx2XQct6r9tcAfcHRgp4IXvPJEvO0gL5Sbxozu-5BC_Y2YqeGMI9UNaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4194" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ar2SsTAjYovaaisy4Gig2KgqnS6yJKuZZnp0iJqFVgxQzV9DUfP0w2QP7q8w9pz-q0EJi2s_oyMAoC2pjAK1cO8lKdM41oJlkp4qGChuNTJuspV37wFWBsXmy8-pGLAUN3AyU-lxaof3nqd5wXC_lNZ6I_E6TKVa69f4Z-8Gn3cBekXfsFa2Bp2K1pAG7jhEqGDgVfgn4DogbjwhNhaalogCij-iHQRwH4V3QmNX5rlxuyhx4w3PyDW5MYD5k0-7123qO1QZCUdQZ9lWdi8qWmAdn0_95ROuRBMuABFVRV7v2D2zg-2XaGyPLStub45Z37Yt0QFo0IuJjDsTb8s6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex
با هر ایمیل هم می‌تونید یه اکانت بسازید و...
بله خلاصه
🥰
اینم لینک نصبش:
https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4193" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4192">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">‏DoH HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4192" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4191">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN_ZEKPCSi0i87WtCISMaldP4BYBb1KPuwRAGn2G3YYOcIpNnLJg1YCv50qlfAx-D5UouhB-7ocSQuFKQ48N52RjszqjTWCY4-_hyp2avGAobaPFxtMhwGIIc_5kDw2vL-jsZg_G6Osp7lJxXPZKpMj2IEpCS0jcYRr754wbNKpsn_wInkwxA-rnr1cD2XRyOv15EW5RdPA1de33PYZMyD3-5ARnu3rG0X8Z-fY5vNNmmv41ugA8CQeKBCEAN3Ot34qzgYLMGmqgfeNrEFjLCHZysWaG1dtZFISIuEqorOPUuZINta1pWcHQxeZldWCMX_A3PEDKw29CmhW1wnCuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
DoH
HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده از endpointهای DoH، کش نتایج قبلی، fallback و حالت اضطراری، اتصال کاربر را پایدارتر و قابل‌اعتمادتر نگه دارد.
لینک دانلود برنامه:
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy/releases/latest
لینک پروژه
👇
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4191" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4190">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZlAZBmD9rXknYm8C9T26iRY2UshiVW7NJKTNURS2Qe-ejzOC4z-AxjY7XelvYEeZb_kgTSRBnaN0iO2OoQP8wfqrONqds4iwkc6X3tody0e43LKhRyEetUhSq68Km0L83GVscKNH00X7igiWaA7iLPFpF5SO-mhJwJnO5ch6kf2Fvmo1iAlUyYk1KTpIV-fQzhqMo0PbJ7hozUWhQsw7yGWQhlQ7L4ZMrB9fQQKKRf5spW5AOosmJq7EMpv8Mb8XIOoO3UpkFAZUtsSd5uQm4BdHryWvalFUus4161ZiQ9Jdyuiqh4w_VDYgasIh8b3esEl9GjkiQwqosSwoKqVM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از تلگرام برای ارتباط با ایجنت هرمس Hermes استفاده می‌کنید بهش بگید که تاپیک فعال کنه یا فرمان /topic بزنید. بعدش بهتون میگه که برو توی تنظیمات BotFather و گزینهThreaded Mode روشن کن بعد از اون برای هر موضوع میتونی یه تاپیک جدا باز کنی و ایجنت موضوعهای مختلف باهم قاطی نمیکنه
✍️
Hessamsh</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4190" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4189">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">برای هرمس، 1 هسته سی پی یو و 1 گیگ رم به عنوان Minimum کافیه. اما پیشنهاد میکنم 2 هسته - 2 گیگ رم باشه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4189" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4188">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nFGpvtH_cl0Y0STW1HI_z5UWyU5KOzhFB-dKv0gnyF1CNnyC2DSd_sAEOXjVJgaaV2bGpPcYFC_DCKxybG8iXjbfLEfNmQuSb-5k3JPn-Gi4POE_ty0gAio1H5H_54JYRQkOkjP4zrH_8HgfOJwvp-qy9R4HQak2Skv2fbnWzAjmVxswbGE4_LqH48UPwt-uZHDW3HnCuDe451LC65I_K7rJ0s60AezbejEwh70p3qT8b9DRSFuNrTbnYpjcv6OZ4IIormPf9BSFF6zuMEx_OhrGwfyP0lCoQh0RVThXIdKXD2lkRpeQk8IO-vyGnaXs7MXBFeAvRx7SyQriKOlgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4188" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GaLzomEsdBK07WDNYBmApeIXBiMYZjO0AObshbjNCLcYSDiHGWw72CVzyMwLUYloYUNCyzA6b2QRU410632b01LpmCKdrfjk_C2OBUPtSOTM041zvMHXbDRge2jZ9GOKtJYfDEvbLvbGAtZmy2bPH5VKFf9nIR_J597PEsQTAC9-mLyVjX3_AxM2YA9Q2gPp2qm3tfVE6jf2LISokuthEi5S31ewI3kZMXs2J-Mk6o9BOBeA_JdWHuXb4UGJnoTI3Zd1aos09b1ijiXT6E_gZwMTIzQcg1pjyF2DXJL0IHi-Vv6b4uKYq2UUC4yq_PfDUkN3M2YJd-iAVdvmWIC9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">886 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4178" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات نصب Hermes روی سیستم‌عامل‌های مختلف و سرور
سایت YottaSrc:
https://yottasrc.com/
سایت Netlen:
https://www.netlen.com.tr/
سایت Senko:
https://senko.digital/</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VQ63HqHQgjYaxCh0vIzOCqxaUof5mxlPU5Fo-aXtAKgbPHt8z3obgFeXPXaqNzdNsqCm8nZKP-VZRGH3IB61uibeZOwUR6Yu5kKd7HW8frhuEOtHF-sJ_S8P3_4Taa-KVyp9sCkpUjdHa3-u_5_EcI0PLUrvy5p5TUuE5vqjT5eUUPI1suTBhMAeeNM6psnQfBF-BN1GjabDRlGI-6I6p_28xZxtUL_QD7H1QmQqklIPUn0hjKpR0ujkmnjoQNCeWuag8BW-3sbqpgg7-E1gwjtyMHYs17DxH8QpgzP4gC6J5JUB68_BdZTRLiyZsoIudo05IZAh-NlvSL21ZnmGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو:
00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟
04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس)
13:47 نصب و راه‌ اندازی روی سرور لینوکسی
16:46 نصب 9Router روی سرور لینوکسی
18:10 استفاده از API و مدلهای رایگان قدرتمند Nvidia
21:20 دور زدن محدودیت دسترسی به API ها با Worker کلودفلر
22:40 استفاده از Endpoint 9Router بر روی لینوکس و ساخت Combo
24:31 اتصال Hermes به اکانت تلگرام( و واتس اپ و دیسکورد و...)
26:35 نوشتن یه کرون جاب کوچولو که هر 5 دقیقه قیمت بیت کوین رو بفرسته و تحلیل کنه
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DjTfp3Y8yp1r5IyuKo-axS328HoWZvoN8_qnhbVekuQZJeds2ODDyi1ExWfwF4cdUO1OeH_4Y_EZhAgGL86ORr3JYl_dvINUBZxkYC2Gezyr0cKYYL_E7mkOZNT9AWJrOmzeCS-X279HmVhu0SZsj0azwIGD7EoNuO5YEZOBICb5oZPNse_Jo2AKSmFxxqQusAUr0eIPlEzRhMGYTjx6WPItzHWXbCU_e_zdhX2_2nTwSO5FiX6pEQy2Neh8TEiFvfUqpejafnpUaOjWJzz52FWtj0J5VLrh7le5Kdfc8rSg-ohZFZneyARArdlyukATxagUbBW4zlkvjpogZHO4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jk5Cxqd0lGMNxvIQrvrFb7ZohJuFzqFMZjpoOKrCi3Rl49IGjCGB9QayuVE1nHmzZcKzDjCkklON-PnVK1SrAsOQkS75xGeD53hmYGbDjof04Gu6N7p5i35mrCsjV3m4hXvtzQ3O2CaXv98ItjcD-xH42az9o-cEA_UsVk13cvBcRKJ-PGrb11I9NA3YQYctAZBkI8DndUXqmnCmNEAeL5kcOTtyMDEN3bNHwPKuuJZO_hEfzRyT_CdEqwnyhw_U2yjqGxf074NTeBGJunkXgkvsEelt1U8dP7bOIHOOfxaU8Qe2ExkHMi9tZsthw6S8Lo44qVgNWwT8mSOOKV6KJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jJoAlUWx9QC6CQiJvwK77KssCaIk2BDj44fjwzivLrCkBpotpTR7eVpzYU35XOyfRq-lxWS0VQWDkkk4n0iKi53ezRkOmI2e0n22x0rqwjqlVhHEmFhHG_89-y3l1IYkGDhLH00-MftAOyU1JblkzyEbiKaZYEmEP2lprADpoYvMu9kfOJyXOOd8fnbEOoMKfoucu5t_D3SB3VereX_hqsrFSNTKkSHgKa6KnJWbl8JdPKEhv1EXn5ioyc_NCcEvSkp5pLl1mygCGLeS-K6iFUe3oTaqJf2HHdiPlvVk0hVu6_8xUs0bSJ9puKMUR5E06a3RwgOgbbB4jltaQ__ayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GMXqLF4BIKrsJk3dhS3RlbSkcR2RxFfzAU1Nw77uSwCmw6LHgwwh_SuthapEjec2i-xI_xwEIqHTtKzsXLVUX1sqDMGGiKvM9tHUo32iSn81HUepUtTm-g0w3r8ahlYI3m7qFVso76HjLN-9CCre2wD5hwacJykicbwJHnGi89FzQ9nUarU8vYoeCt8lp_BREk8ZvyRBzLZAVuJQ3RLnVpu8tijEs4-Z58w9TfUG5rnazOmOH3grgYuQPTPHxZvDqa3P8gT4tUts8muhuXS48SNAbc5iNtk92Teaq6VqNMx_XLebyxvSnC4Mi0DlsIc3Tu3KKcO4zheewiVgNXAdzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bs1M4VTOa2Yfbl_vgjPGvt4zfjkqWD2-AUZFragtNgSWIJQ8ENjrIJGk2Mj0tEYbTgtdGkxM94JUvoMocGKhfiIKWSyEQpopxtJMx1IIbXKinZHCKmAIb33BZpLzPY4R4mpnhLbUQB2puA2fx7bfqJbuXKKpAOUpvutShZ6UdXC4G5in8lTGpVbtVLoVtmmnEbE0ADoyfJAgL9R9qLyF_KT-Dn6VcJ0rod8tx8YtIVblriSFHvo_4ZeT623TR5GfNFJ49JD8Ii1fyQcy5iTtIsqtoz3SH7KtsNn-ema32LjFq_XUUSqf6x7JkRS7Ht9Pl6AF4lTMXzNxNajOeMBkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SOrCey4nMWlIZtAEcj04vX7j3VsMDi-QDPfeRd8uLoIAS7940FsGnJTxV4UsGYgjcUZbNAVGvHPdl1QLz3gmw9Dy_DkQ0BhWuoIgAijwVyNORAfZB02WD--VdRpWDHaLMeCA3whum7YznW7M8qDruYeNSubHGHV9CtGaCjvNtT0eEPNxBpeyHk9CMCitq2FEuHmEghE5bRdYkd0Q61oimvxS7uy18yf_-rTfgeFWvT3dhMdMztffYrihO-u62k_tGtwGS_NpudDzV8r8LpWX4rVkZ6vd5aMU7dlqvTe1tLIto3RqQjIJgkD9FCBvcmtyAQkOTDBb1cJC8zNKQK5-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XP7guezJQnxrD6FWUgVmVMIMqGmSBiLmKVk7VQvoUdv_acCQPHxmeXktV0YZm-PolEVi1cIf0qxzLH1fhtz6XPQibI7IqzlaO3JWhNqUATdKVQrG_s8OxcEs88EUOGmhVEwFo3o7qsHSOBWm_oUaoPIhcwKOluwoT_yYUq9L8huvOBtnGtZfIJcn2kiBaxpCUEPxTH_hj68wmjyOYSPbRdv4lQy0CXSdA4lmu2QOW7e5u-EtuqbDeKKMAQbrml0CwcsYBadO490lj85DsD0fC2vDlp-DbTl5duQARFnfLlf7yb3OZXuLZJrAzQH87r1z6OkdJprs9KANzniVCAX9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bg3n1FPygtaYuuZ6gDTAl0txF8uhifry8_s0LhZ1zYpsevObLWgli6r5cN3d8HtO6lA2V3xF0fGQvEqAomyQLsWlI9tadg1vaO5YYsQK_j-tbe-wWsTtwKUBNuV_VfbS9Li8Jvo7gTjhQbKjZm60Q3b8FPONiO7WGuQQ_TrvlUPCkM_X0mVe7093Y5uX8pkvmASskJ5H-KCgAdYMFfuF4OSlvTY2FpGh3jtitskNnWqSijS9Z6xb3BHlzfM4Zs7Q_vFxbbYC4dRw-9_uRRFFFP5c1J7qHJasAk1Kx24JE-Z-pZzF_r_SDKd-8sixIajOrsN4O-rfLKWZkG_-Gsed6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cAnzv3CeJIwbODML9udURtO2-KfTpw2S46WifJzwMXwB8INJH-SZWqSI_g20XuQvu0p66JKqkJpwSKNp0JWK7LHzVh1wHwnGPm9sa7lyM6i03gOBnnsCaFsCh0E6fycAYHHfo7k7O-l6PeHX-oA2MBXZ9AtLJWY5a7GNWSq1LlIWqsd-kLI8JUVNURBdUyPl34Uxl3L4iz1QlmzSIA0g49yB1GFP8FhqoYyDMTkbd8f3SUvj1HLyz_fGU9ZcAlHIgOflxoh38nKh1Sd0KBw0hE40zXA6I_NviJXEGJIAjwHMYz5uOfU-WcR1wnww3Yuf2w4XN--a7ihbLEf4YnKUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=wBgAZys5DV-zNuQDLRniZGVxzVKT6rsiEMJ2K-C9FEYS4qtu_0FKfWOMnzYuLzv_wMX2r9XDV2m7gD-0fyymKCbhfb4x9Wh_MzkVcVDXxqqJI5_eMAwVUWpA24twaHz7HKUNdGmCiwI4ZwBdpKnJ3-yHCibky_0SBDVfdGb99vWeI2M25DZ1rl3hH-IupSB2c1UPaUkyZZpvBF83nUBZLViOxkAsVfmYnGd7ADuGxzDLEXfjGpK57ZDNics0sNZ20w33fnadckBclWlTTewyHgrY5gnP1v2u10fv0TY_7svYe0F6n52VoEy-yHf2m0Yt2w9o9T7GPiuB-8NXSr60bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=wBgAZys5DV-zNuQDLRniZGVxzVKT6rsiEMJ2K-C9FEYS4qtu_0FKfWOMnzYuLzv_wMX2r9XDV2m7gD-0fyymKCbhfb4x9Wh_MzkVcVDXxqqJI5_eMAwVUWpA24twaHz7HKUNdGmCiwI4ZwBdpKnJ3-yHCibky_0SBDVfdGb99vWeI2M25DZ1rl3hH-IupSB2c1UPaUkyZZpvBF83nUBZLViOxkAsVfmYnGd7ADuGxzDLEXfjGpK57ZDNics0sNZ20w33fnadckBclWlTTewyHgrY5gnP1v2u10fv0TY_7svYe0F6n52VoEy-yHf2m0Yt2w9o9T7GPiuB-8NXSr60bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Anthropic از Claude Science رونمایی کرده که به صورت اختصاصی برای مراحل مختلف کارهای پژوهشی و علمی طراحی شده.
توی این نسخه محقق‌ها می‌تونن کدهایی که مدل می‌نویسه (Artifacts) رو به طور دقیق ردیابی کنن، محیط‌های اجرای کد رو بر اساس نیازشون همون‌جا بسازن، و جالب‌تر از همه، بیشتر از ۶۰ تا دیتابیس معتبر علمی رو مستقیم به کلود متصل کنن تا تحلیل‌ها روی داده‌های واقعیِ علمی انجام بشه. این نسخه فعلا تو حالت بتا در دسترسه.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9603918fce.mp4?token=A_HYuITq6wKCeQw69vpIrbx37Y77Y4gAOMUV0nkp0lRsz1_I6R-KQQ1uAKvK20jksTNI3owUZygHFaeAOgUpMxGnFsEdvPawyYdlWJXjpVK3uwz8DlIKZx5nUbbpkC5A85Q3qsE3gMFqPAznSYZlUOdqYcfM-lTMmdJWbTR_75KjyzRbhNWHEMOn39bBIHsQY4BMUVbLryuvhp_SXXszAtfBJ6ovgAdskecetbavd1qhjgzRWVG28Hyv-TZ_v-j1kUpkRo1L1HibjthQP4fTWXKGO2XYo5zkwcNa0fgqEdMyfTmpevrPg55_s_jHsyggVnz7_1wd6XZuHQU7GYADEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9603918fce.mp4?token=A_HYuITq6wKCeQw69vpIrbx37Y77Y4gAOMUV0nkp0lRsz1_I6R-KQQ1uAKvK20jksTNI3owUZygHFaeAOgUpMxGnFsEdvPawyYdlWJXjpVK3uwz8DlIKZx5nUbbpkC5A85Q3qsE3gMFqPAznSYZlUOdqYcfM-lTMmdJWbTR_75KjyzRbhNWHEMOn39bBIHsQY4BMUVbLryuvhp_SXXszAtfBJ6ovgAdskecetbavd1qhjgzRWVG28Hyv-TZ_v-j1kUpkRo1L1HibjthQP4fTWXKGO2XYo5zkwcNa0fgqEdMyfTmpevrPg55_s_jHsyggVnz7_1wd6XZuHQU7GYADEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه جدید Hermes Agent سرعت خوندن صفحات وب رو ۶۰ برابر بیشتر و هزینه مصرف توکن رو ۴۹ برابر کمتر کرده.
تیم توسعه‌دهنده‌اش، Nous Research،  با حذف پردازش‌های میانی کاری کردن که دیتای تمیز مستقیماً از بک‌اند به ایجنت برسه. همچنین برای صفحات طولانی و سنگین، داکیومنت‌ها اول روی سیستم کاربر ذخیره میشن و ایجنت به صورت صفحه‌بندی‌شده و فقط در صورت نیاز اطلاعات رو می‌خونه.
این تغییر یعنی کیفیت تحلیل و پردازش هیچ افتی نمی‌کنه، اما زمان و هزینه‌ای که بابتش صرف میشه به شکل چشم‌گیری کاهش پیدا کرده. و یکی از نقاط ضعفش یعنی مصرف زیاد توکن رو پوشش میده!
کم کم تیم Hermes داره یکی یکی مشکلات محصولش رو برطرف می‌کنه و امیدوارم همین شکلی جلو بره
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4147">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lN22jNZMmoeToiM9q32DoGv2B6dhYwilnPi1OUEO0tMhGaayh_XEZYBUttXo6sTo9UG3w2PlH1lc-G8irKUgOjMjZaLV-p_N_VqVetufPQuAA2yKND_KFSO1RK7qNKUMmsU-sGZlz--ziwTMWMDkD7nM1xr7PM0Zes7n3yVSu0dIZ5-KLPU1DsOoW7K4RjfkCDHVKfwMHf89kR1JKMVSEoePIsF1nmQWNkFgp9wuxV1fN-ScttBr0iUkFuxsRJLTAliHH2YNrzN0UvHk3SsfQY8WLEFuztEOvMxvZ2I9HkLCFKmgFBNFGt5Er_dBbsAYdj7xz8LxQJpnroCCUzh95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک منتشر شده توسط خود کلاد</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4147" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4146">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgqZ8YtOsDUbWVorIzaW7PYDhQTmJTIenQ26F9fNkLchGpDMcVUs_Qow4IhdIilS1VpR5Vronkni6NMTYMH9Ho1gzDHspjJU7-x_W2QZc6KyRHxVMPqvWDx-PvEbaAzsnIsXjRsUNBEBUjTnjjhos4CEhiaLUrQJl0LzqC22NlgeqLtov5-wJEZgUG552ZJbnNmNil95ZJ1Tm1zv0bpEinbcGH79LhRX94IeaS3KBg71j8wV9fx94txfG9KK9QlRWsf3zKKkwgqC59dqTteQE0kx7biOhrYrxPufjzK7jY6bQ_PlyBS8g7ztR7nVH3pOfQAX4yChNqJgjhUHWuUDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌ آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4146" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4145">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VsreFUkJX4YT-f0-L15E3beIAGqSFbnDxs257oQ2YbpGvBeK0loqI4MCxCiTdoAV-sdfQtfheNUNvvZ81CX48u5EtKF8EulxtgUwtjUFKvTB2wZEgvGLJYphyuPk6h2znslvTX5GpxhkfIW_dMAIQs8PryAExxsMwmYbcd4e8eXojtEIXSxutQ58QmEXxCqmNhagEXj9YVK2aZ8zt3RpcbU7RXZhRUAeqKKX4hHyjxPhTytuZBT-7qcrX5dte7CWvzhEfZWqhcG0kK-oMQR0hzP8pyBnW2tTzF6p-d4zgovn0tTSQ4eS-nV5d1fONe7wHroehVsRZ-yZwSwQickOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌
آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4145" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4144">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!  این ویدیو…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4144" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4143">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!
این ویدیو دقیقاً به شما یاد میده که:
✅
چطور کاراکترهای ثابت و باکیفیت طراحی کنید.
✅
چطور با استفاده از AI سناریو و موزیک مخصوص کودک بسازید.
✅
چطور انیمیشن‌ها رو با صدای کاراکترها لیپ‌سینک (همگام‌سازی لب) کنید.
اگر به دنبال یک بیزینس مدل جدید و پولساز در حوزه هوش مصنوعی هستید، این آموزش گام‌به‌گام رو از دست ندید.
ویدیو با حجم 300 مگابایت اپلود شده , از طریق نسخه دسکتاپ تلگرام میتونید با حجم کمتر دانلود کنید.
〰️
〰️
〰️
〰️
〰️
〰️
در صورتی که مایل بودید میتونید از لینک زیر دونیت کنیدتا قسمت های بعدی و موضوعات بیشتری پوشش داده شود.
🌎
donate.isega.ro
〰️
〰️
〰️
〰️
〰️
〰️
📽
زیرنویس فارسی
🌐
ترجمه این ویدیو با وب‌سایت
isega.ro
انجام شده — حتماً سر بزن!
📌
برای دیدن قسمت‌های بعدی کانال رو دنبال کن:
📺
🌐
@AiSegaro
🚀
هر روز یک قدم نزدیک‌تر به آینده‌ای هوشمند!
📤
بازنشر آزاد با</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4143" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4142">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZHS4OQIrnfdp10OqGfuCIMPfW0nIl-xU6CPShPMi4rmw2trh-byNiAQF1t1OLRmFHgvxj7UvGznocJ7TdpOJP-aKYx7f2-HWTaB8yrjqtJWUOjH5WkH1kLY8bStv8zCNBf3tMOJQKNMJ0CmLnyKlL48E4o5GkCi5waHyKVVYKHiCn3unZFAVEfpg5mmgGF8GelqZHbbPfFoJJ1PWWyep5inzq6OJIKslLCEAXM0BswIpzYnTFTxa2Y407MPFtkj4QQtMYCrqNsoDBwpYCt_pj3MVL45EG6v_n8Z_7yKIQ7ZEVuBKp_V5xyNOIH5dNpFBaPZRDjZ6tGd6oGDmgzIcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب یه قابلیتی آورده به اسم Ask پایین ویدئوها، که می‌تونید وسط ویدئو اگر جاییش رو متوجه نشدید از جمنای بپرسید
🎨
فعلا برای وب فعاله گویا</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4142" target="_blank">📅 21:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4140">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4140" target="_blank">📅 18:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4139">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4139" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4138">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انقدر برق رفت و اومد و نوسان داره روی محافظ میترسم لپ تاپ و همه چی بسوزه آخرش. آقا بیا قطع کن همون دو ساعتو، نخواستیم</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4138" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4137">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بیشترین درخواست توی یوتوب و توییتر ازم این بود که آروم تر صحبت کنم
😁
من فقط نمی‌خوام حوصله‌تون سر بره یا وقتتونو الکی بگیرم
اما از ویدئو بعدی سعی می‌کنم شمرده شمرده تر صحبت کنم</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4137" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4136">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sa7g41Q4GuZ13dWQTdNv9xFyTP2BHW7A9DBoYPIEvENltW6Ap08pBbf3XiWuLuWfdLKYW_uaFT3eJnPCsDbthLXFFiDiZgTEeZbEDQbf2i8Kw2u_hY9P8MIwGrgl2NDfmeLMahmBHgx35YnuCWHtAWtonZ7Rd5f_r9DVmITKH_KPmaSARjPFK2MUq9Zn_7PFnTO2tcvftwAVs8kaBnVR5azF-xXrkWEK8UZ46Y0ZIXlm71jTtV99UtFBk1GGzOR2T8M3UsYGyx83ZuUl6k4bFBm3KvhtudL-5yrih_hxOzEtNtziMKqTkr7LXcEoSrP-WD4lQXaY12Vr7jtJhWSYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد نسخه‌ی موبایل Hermes، من توی ساب‌ردیتش دیدم که یکی واسش نسخه اندروید ساخته و Pull Request زده روی گیتهاب(که کدش ادغام بشه) منتها هنوز، رسمی منتشر نشده</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4136" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4135">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4135" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WcbowNF0O87-gGC2fvh8Yg0cXhtOit2fyacXAuGpt0T81Oaj02QVXR33sIemp-m8KrZXXQ4fS7OzDIc_CJ-H4uDu-zEkVaAaTICz-8rr0J5-XV8F5BfXSTWlHDtMN2W7R2REnfK-8wglaWKgcv2qIk4hOrPaUOFwLR9t0ymQNrn4PsKc5yp0qhDUg-79M3X5_6vE6KhgQJBe0Yz0vh6CvEBsiAI1DSWAosAz6ZRykNEaUdqk1E9nh1O9QNHfIcNC4Zfx37SLa4mL9oBg7MoaPpdL8wpQ9SxPOV-eNP-OQloX1ndkqOT3m5OENJ8CNk3XsRjrZKYTn5Lyt_5vk5qJ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VRq3c6xNikm1PvuIU3bfcD2tUU-q5sn-cpeEQ1lNV6ld9gt9wgKlmVqmVgL-3RxHJQZ1IVhsqt-taSlgBKWMgrC3BAOjczQKuM39GYtb5nFTT_LpOkXOvSfRxKPTAZiskx_oYJjg-vjZ_jDvKvQwPh8leR5vlwznUNSCNhdObFgJBPVIgvKFCnleWBHgYjmvy19_6ixm6_3jF0qesi857pubSH5ExF_iaDYPdsVrFpZPrsA8oDOEiYiJ1TMF0Pc--zb7O7bLfF21Vw_j8gFVzsYt-6uGzfdh3yICn5MMTT4Wtpx5iC_g6qGF0QYQtW3r8ESpg7S1vn-YZDC9H-uJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QjXZZgqKC1ptvLjFl4xCbVxvTREH-pjS8WI3GhW896QMnJYi5DLDFWCjNUl9A2uX7AwIzksT81gK17YG2zsVwSVgeJCeyBriGc6Mrp-L1mjxi_QJ4fmhFLnoecJVRIXRivP1lQtdRhcFvZH3IbTluNsjAdJ6k-jXfYbltb6nu2LfBn12u-Ja2HXsCxRtYRIOoXjJGlv8YgrTeXIN93NExkSNgVeH5YR4Mhzoemhc0mHCXx8lTOLokzuMcVI9OcWK4LnF7Qp3KKwrElqkI13z9jwVrq8_cHF35amRm-tP679Pdkjq3ApszIMpxUBV70HwaClgvEjeQCRVN8615blx6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tghcQXoqVtlDfkjQiMy8-invkfUT13bAYby7zX0vVLIPUamWyYW8k8aRjp956a-ajvIgBDLQAyyKInxp2tDLypksdKlggNbr9CxE5ljd241xGAO5D2KqJaHj8GYfSltHBbX80SUgYYhc_v9Hq_54cudnYljnB2Q8FOuuiFVfymL_mVni4rRcW0DYNlXAKGUX5Vs2Deoa6etVknno3VAezxqpMWFKG-7A9bVOH9VrF-njT6pd47I8GOLphaUZPS_LHtTqDpK1p-N_-ZKM7uzxZVYiMS5LPFpl8LRnN2M9KWfVaGzvoh0BtcS5HuC-4NnSHVsu6xy1lK3iDAHSVoHvWQ.jpg" alt="photo" loading="lazy"/></div>
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
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=gXCEHnNPctO0bm58D8kUMkn7YSVfiVwPZ16PSHOiAOa9Uil4z_FR23-xuNygSseKpmWGo9AI7YGycZaqg6HtBfSgCAsV0N3pN003AaoDx-X_9np1ORBhZqwir2P-p_1ZuxN3N7wfuxtJy9VPGVZpfx4jA1t_4sTK0nQhKHJNLbCdCyZBAY7fIWExjsfHgw7LiMvi2zlwAmJudMpuBItLWe0t9cDqUDkVl7JCuNxAHqrEiGsMsnl34KEDWkaOK8VEBbuyENRaNxD8mKt8__ovoIwBeB1LJcmNfsvhLYZgUQ-gr7wPiTV2yi6JHI_VPcUz4mFtzVTB6D2cucRCnzEzGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=gXCEHnNPctO0bm58D8kUMkn7YSVfiVwPZ16PSHOiAOa9Uil4z_FR23-xuNygSseKpmWGo9AI7YGycZaqg6HtBfSgCAsV0N3pN003AaoDx-X_9np1ORBhZqwir2P-p_1ZuxN3N7wfuxtJy9VPGVZpfx4jA1t_4sTK0nQhKHJNLbCdCyZBAY7fIWExjsfHgw7LiMvi2zlwAmJudMpuBItLWe0t9cDqUDkVl7JCuNxAHqrEiGsMsnl34KEDWkaOK8VEBbuyENRaNxD8mKt8__ovoIwBeB1LJcmNfsvhLYZgUQ-gr7wPiTV2yi6JHI_VPcUz4mFtzVTB6D2cucRCnzEzGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NTl0afSgHSYJs0kJXlZrU2PYf_xnSK_Z7im4kke9jP9fYga8R4nrYygEdqVi-khuTq3u-qSCexeug_pIJs-xFGO5QumOs_jFY06I4_vKAJ8i9wbiYea4WF8iKn0N_q17MtTPLys_5XcRAJFvyLU8Evq_lCCY8UF6xIYHBeEsZsqwKjN80eG3W_zGrcBIIScGTCmerxeO24YIj6paYv3AMRhqkp6qfJWMdP8nDOe9TcaKgfn30zn8BtDII3H-w4o1Bb_uwNX8PZgroxNSinftGxAtAdBC6T38GqoXz60mxSoFmpuydZID9vHYoKj33FXjqnbgcnIX-8Vkdnv5WtxnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router:
https://9router.com/
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم
2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم
3- کلی API رایگان وصل می‌کنیم بهش
3.5- اگر تیک آبی توییتر داریم، به راحتی از گروک 4 و اگر جمنای پرو داریم، از AntiGravity استفاده می‌کنیم
4- از امکانات 9Router مثل Combo استفاده می‌کنیم و چندین هوش مصنوعی رو توی یه مدل فرضی کنار هم میاریم
5- به ChatBox و افزونه Cline وصلش می‌کنیم که هم بتونیم عادی چت کنیم، هم بتونیم کد بزنیم باهاش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگان و ساده‌ست و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
