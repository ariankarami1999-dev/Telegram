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
<img src="https://cdn4.telesco.pe/file/JzTTUbvcODRElHB6mqxVtr5M-zb0m6b2628DqRrHgBUIyveZQ2muFMyUOvjzm5YUF4kCm0ZiTNvhdt7IZLfUsUI1h2TWuTF5qarq7hRqmPCUJ_g4w6-NAOQ-5q0_RVRrAqTLRkiOXjudy1WCSfsXsKtVRIOyXCfRaqQxX7yUJjd8fU6fEtgQRVLHb_Zs3WXgRX12ag8JfJgyqPFKNPRrhALBCQPK_S4ZqYWPaxeJaRu70xJOL6J0IHJd6ROvAUtqJJmJSR4AYdnmN0acNzlRQXMfm3z38DjQarkm9xI2zBHAkO0HbsoloYZSVxQ0Ws2tzcZQ8M1nUF3Z2RkeMeV92Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 451K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 02:20:54</div>
<hr>

<div class="tg-post" id="msg-30393">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCb2CsaErRkGTkpfc_woMBGqXnlNtNz8_JUQkaTjURUOQ5ukS9SBMTLWMR55mzcHKhAGFNDZzHTkuwhXN1hhIDaLNBPl_3PSQR7wv8PGpwG3AQOo9Y-O1xU86zvRt3NZL-U7BvFOElLbG5l6v_GddSboOur5lcPZDLetxCPMBmbSlL9eXee5TayRXSKQj50Yz7HCP2RvYLPEp7HZtcnqDGoY6PMm4TVqnrfNWoayejJBQ0aDlruZrQhm5LvtLe5vS_EsCoU-zeiDE4Vt4XVWRyxPVNkufffFy2Wzzp1FvrJC7TcLrVqKbzAMVcegXpkMfVqKS0Hts41n4nh4Yg-Izw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه بدونید ازبکستان بعد از 6 بازی و 5 ماه بالاخره طعم پیروزی در یک مسابقه رو چشید. این‌بازی‌های‌دوستانه تاثیر زیادی رورنکینگ بندی فیفا داره. باتوجه به برد قاطع‌کره و ژاپن‌به‌احتمال فراوان در رنکینگ جدید چند پله سقوط خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/30393" target="_blank">📅 01:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=PRNVCF1p-abuqvO3V0vs6WZ4wUhbFB7JGYAUeQzc_oiWbJ2xzYQjNH0KJfCC8bhtRzn_mj5fH0w67rNOQCJs27hS394KvBa1CTBkYxTCq-42JTP8aEqh7JdVQSor84pg22X06xUBrDwkSoXRU97xVKYT7gpeR2P4uYbpZis0zZubBS7gQeleVLyJfcsF2iBVCf4Ta4L_kya_Mk3q7xsz1YxofUW9pPmRyWTmWWtvGG2PUE_m7bFl1xvJT5CtfIu-fP3De7b07sRMW5lJDDLtgjy6lBiWY51xdvTgJEFAr31jssOkUYYHimi8EsvCs-f72GaouvYnan2Y63H9MLrmZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=PRNVCF1p-abuqvO3V0vs6WZ4wUhbFB7JGYAUeQzc_oiWbJ2xzYQjNH0KJfCC8bhtRzn_mj5fH0w67rNOQCJs27hS394KvBa1CTBkYxTCq-42JTP8aEqh7JdVQSor84pg22X06xUBrDwkSoXRU97xVKYT7gpeR2P4uYbpZis0zZubBS7gQeleVLyJfcsF2iBVCf4Ta4L_kya_Mk3q7xsz1YxofUW9pPmRyWTmWWtvGG2PUE_m7bFl1xvJT5CtfIu-fP3De7b07sRMW5lJDDLtgjy6lBiWY51xdvTgJEFAr31jssOkUYYHimi8EsvCs-f72GaouvYnan2Y63H9MLrmZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/30392" target="_blank">📅 01:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30390">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZTu1aDrn1_zD5DNGSKJ-Qszko5khD9uQ_nVNXerA6sS5PKLdKqqx4MyBUy0r1QYdh1G-stMYEu_T5bVfrkYZrDNJt--pZ--jVCFBgwzf98DbT29y1IYvNcUiJq_eF7Wb960l7BWv8HuY8pBaL3VtccvLs2uvzQjTm6DvKFCvJ6K9TULpOC2EjYm1mKXl1rEkJWg7Uy6GOC4hNgdbilyAeoCPiGwivD7UugB-lTJdzDwH-mwGHLPNrClr7-SXWOGEggxO2dcaLY6i-k9cLqFti7pcai4GY03o3-4Cd2YeHYqednHjUV_VlFEPnxyjzbIrjw8RhXWVTD0Xj7t6JfEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/30390" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30389">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er0wu2m5jmPMJWgKVQN8O15ZudXdz9cyHDfKmGoBh_RGSt_lvaJ2WB0Fov0jytiIGi7VkyHM5GL-a60ivxYbs4DPkGTz2MnkGxpSiruCvBG_UBBLpvEjmkbm-nWFBOuMiejJNFndEnnW1iXNQ1cePuIfraFbdRYiFJDgqjpIF_IGsIYRBy4bXTghry173f3zgzzeMv8SnkqVQB-k90yeSLyq-FtAlmZJY9P3h5czYWkxPbDa2dugVpdjyYRtyoExTUaCu39e2b6K0W0y_YSXfAWZxinxHUPyw6bjKTwg8ag7hTuA2vlpsdPaVUFdJDnresyLt9akEJePS6ntW4hZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
ازتقسیم‌امتیازات در تقابل هلند و آلمان تا برد سه‌گله ژاپن و کره جنوبی در شب شکست سه‌گله شاگردان امیر قلعه‌نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/30389" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30388">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY_VW2mq_9vSjgY5Fiod44GgCmijQnH8xZgGBas4Sh6AwP8e9JP30rw1YeMwZFl8UV2kQIIcQ18CyJXXpdV_RgFTXcMDl-LEo6_AzYyHxJDD990InudQcAnWTqnOO3k6RhFq862YB8spc7js6SCu7HyTV6R7TPlj-PZP4JEAU36fnqxKe_eZKrkj02vCM3RQwBHYagWoT6NQrWH8Yl46MX21-y13BGGgGbRK_ufHf2OIFh-qRv_SGGW_tUphCNloydKTDMWsBKgQxI4Bl--1eDrd2Zy-8QRDnfQgRiNrIrGSC17HRMkIfKsxHk159rvuy62LFRbnErYxt70Jp2pi_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
تجربه ای متفاوت از شرط بندی میکس
💎
دو برابر شارژ بیشتر ویژه روزهای دوشنبه و جمعه
💎
🤩
🤩
🤩
🤩
بانس میکس شگفت انگیز یکبت تا سقف 30.000.000 ریال
💎
🤩
🤩
🤩
🤩
پیش‌بینی رایگان برای کاربرانی که هنوز موفق به برداشت نشده‌اند
💰
برداشت راحت و سریع با ووچر و ارزهای دیجیتال با بالاترین نرخ دلار
💎
🤩
🤩
🤩
فری‌بت هدیه هر بار واریز با ارزهای دیجیتال
👀
این فرصت ویژه رو از دست ندید و شانس برد شدن شرط میکس را بیشتر کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
p 2
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/30388" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30387">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9M-NvHIAfgxJcesyfiPlDflTCn7Eks7ZOW5iQyHBs-YXm_vB0tFYkqWiZ7J6aQWecqDv_XtiSAzukMWlrKOZ2M45MeNyGXuPDyNPzYCWKyKCzgeNRV3QpOGnQb27w6fUC9LSt8glt8MSXGXWtuVAjLkOkucLEvU0DcFJL_X8Wvs7NRKxJxMsy57eSzoJPqjWRLVmXDrdyla0YmMWxy7fk-A9GEx7wtS0UO5G4MsxSqrD7Jfl1HC6_mw-Q26dzrLRDcnm8RuZO7kbypp-FmpfXal-sWxE3eHD8eoYI_oMSOz0AzSZD2nB-lzJhJns7XCN63zO5xmqFBcu1BOcgPmzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق‌شنیده‌های رسانه پرشیانا؛ دو ایجنت نزدیک به علی تاجرنیا رئیس هیات مدیره تیم استقلال از صبح امروز تماس‌های خود را با مامه تیام ستاره 33 ساله سابق آبی‌ها آغازکرده‌‌اند تا در صورت عدم موافقت فابیو آبرئو برای‌اومدن‌به‌ایران بلافاصله مامه تیام رو…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/30387" target="_blank">📅 00:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30386">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKSTfSmYupj6HJP7Gzhys3N2p-Zn9xHCQERMevGNmN_nzHyrQzaYRMrgCkpqm4JcipvMgAL9lTMKwWiZBnTp44JFFGZKb9N4lR3dXx-nFjWRm6BnSwo7q2nxvCF7BRptEBgrCntyN9NyRu_x8L3Zft-8eIkYIaBIuV6uY5ZBwAgnSmm-r87YC7vyWZUkpR9VVWHYulhypwS3NC9vV_iswRjYqcrnxiWj2LqU3Dgyj27mcQ0Sw1983Lmp9WkBSSbIjex43RbJbqXmOlfjCpfNHfuWTgeNriGL4D13M7FVFCakl3lOKq0VhKSoP3TJSrwO3994Bjc8Fn1O9PX98MerrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/30386" target="_blank">📅 00:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30385">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7oXx3UkcfDpet8tWhe78QoQbwOsN-pfJ7hj8ZKj5Fa3lT0FsKITKqSTv62hahzJqBCPI8jCDlorhgocoYB4OiEmZxsKEdiA9RpWGixa2mtSfjsb2ZIeDvwdwmPYIDrk0DaJU-hvaN1xv1rCkL4KSsngPufAxf_MYKmR4qV5nQeyUBhvmWT4918StIKFFmdlLnDpuDkt2noUllSfHM0H8oczSDmxI74z_pYGfOUnp8EdAMTH_rXgwG7ca7CjBEAK3qwUL_UmipTNuf0Zwi6jB6bjlAYhMl2Q3zL7oSkMW8yRdOULNKgQFJbCk0NR1UI1oK8FgsJXREMXJhrLpNEYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/30385" target="_blank">📅 00:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30384">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4Fw8Mr0FADAR-_x3eClw85nf2Q4BTN1qbok-lzwXoRQbMgIiq_rjvAkn9iA8EWQE6YiAYMsDuoJ0XIOyS6ZthddFOZXYVySN8R3LMEPAzkVQU_6FdMWxDK2LhRSeDxX3nrOlHRABMktE9T8bjK_KibdlbkQg9_9AmbG5pVBycsRNzOOqZMb3sZPjyMF0dZ-5v94t10mM-4ynxZAsFkd7EdocJhsjRFtuYA2n4alSABGElV1x_7jra3rAZIilEzh1kZYJv_-ZF5cdf3RyogjsNihnlDkDmzJpJOt-EYqvGgSLQF3lnWIOmrtWfL_KWgkwPcIZ-b023hJr0BQBKfHWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/30384" target="_blank">📅 00:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30383">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dx9hT-DIskCD9Os1hwYGa-17b1C-q5QUDGpTRBrrWVdJI0WEcZC9KOjoIsLZWxc9z_QlXaTzPEnd6MrHR3PlWElVERC0SMnBbxFx9czfGX-9Jy9REujl7Afq8D8wg6DEyK_wPzDgFkxXvUb5jg0N0C7nsGa8UcEoAwNVjGLyuBmR3yN3vVhMX-RAakWY0q5bVsSgev2a8fUFxt76TYiJVrxPl-sgHlOhPhJz7-LRm3iQFOLx6gamYYLb0mqpHtvqm5rWUdILpLdjZk4Dku63P83rdbwMTqNHm8Sl1KVYmDe4fIbGlO9-zqLtaiCyblZw3evYQYwQF17qGxMJz8dMwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/30383" target="_blank">📅 23:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=bFZRxr7Y21UEZXp8LwRxjkf9gkZJAzAmoqbVHK2o-Hal8mmPgELHTb47rBhOXRh_6ZtxU-s6OIsU6-xts6yIxtDiQ-tyKYjQjn3Og9gLAdjBQsIvFxLB1C4_bKR1vY0qyKNjbH4xSe9yu075ssDX3uK8TvJR2lXV4_cScUuhZJU7zQGuY79vOm51aymsAy5bIV5j5qj6W5bsKXLafZsiYIaitwb3fg-PeQxUZ3pdoo_OtZHozL-iQNIJIQtHSaj-QbYk8QvwWiV2uDs8tonK0ryZdjWD8FIzy7KmUAf61AIjqsUEEfnFyDEqiBWVIh9TsuslBkMPVIlTMjCsWLqi0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=bFZRxr7Y21UEZXp8LwRxjkf9gkZJAzAmoqbVHK2o-Hal8mmPgELHTb47rBhOXRh_6ZtxU-s6OIsU6-xts6yIxtDiQ-tyKYjQjn3Og9gLAdjBQsIvFxLB1C4_bKR1vY0qyKNjbH4xSe9yu075ssDX3uK8TvJR2lXV4_cScUuhZJU7zQGuY79vOm51aymsAy5bIV5j5qj6W5bsKXLafZsiYIaitwb3fg-PeQxUZ3pdoo_OtZHozL-iQNIJIQtHSaj-QbYk8QvwWiV2uDs8tonK0ryZdjWD8FIzy7KmUAf61AIjqsUEEfnFyDEqiBWVIh9TsuslBkMPVIlTMjCsWLqi0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/30381" target="_blank">📅 23:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL9cl_FGBV7PRqN7nQIX85NUxgvZJQbip8-kouF-YfyebZzxAflzddXYLPFTm6pb5Qa8GGKc9p6wcq0bQ0fGhPPK5GPn1gL8JDoz4RzBm5004LGtqsG6kV_m0Qbpp8o7O7Akg1kT6akWRR8-zcoVgT6xwYBGCXFLkvauUERGT4ElCIBvoBv3tY_LB1un6O6NYGkvZtKFprN7cXmvkaK8hMKRq099AKbv0hMaU7k183cPvpJT3ZfPL_m9rBR9ABmjk7R1O8UsH3dQGLXyBRcw88rbopLphKu4SeTeiTtAk_Ow95ckyE1JUIG2SHilbTFh05wf2i_hrbDV_qwXd_JOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع میانی رئال مادرید از ناحیه رباط زانوی دچار مصدومیت شده و ممکنه چند هفته روبه دلیل مصدومیت از دست بده. مدافعان تیم رئال مادرید در حال حاضر: هویسن، آسنسیو و رودیگر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/30380" target="_blank">📅 23:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNBlR9F0xX_JjC-RBepkYxjpTFe9O_OJvTK_AV36-0AY25SvinMr5PQgNlWbIFQjLKxTI5TmhpvEpcZuJznzL3b40L0AC3Pmg4dJ3WR2oF7nCNjZlRR0AskMBj0p9PztkgNW7BXQZx3Ps6XlC7eD3zThUkDcEU4Wr98Jlme9TFnEH1hhgIYmswkWjzOFAIKpUmPr5TNVpS_3hG8rNO4A5so4sp-Eaniy7XhoPxVyq_x3zwI5tacIxC3-IGXJedbK0RW0H6lOde0Cw-0TxsOpL6gsvnOQNuC7xbLGJRkP7FXXPpVvs0CBy9EMDtCNYUzEEsJvjwCxUPMTMwd_4HBDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اختلاف برگ ریزون دستمزد مردان و زنان در مستطیل سبز؛ دستمزد کریس رونالدو در النصر 142 برابر بیشتر از گرانقیمت ترین بازیکن دز لیگ بانوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/30379" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jfq6OhzvSw8wTS4qomGjeFtXQnYzDujszurUXsz0QexeHTJR-NU-F_KkjLxAKS0Fiec3V0OH3FICMLPcZI6yl8dTWbdvWZqIj6jJPdHkv4gamSIgggA50JceMClAimOt0jQGOGWnRuCrptaVXncZ8btUBzsAKjahX9aoBwYBm6Z2MxhNEzMsW32XIo0G4yY_vynF3PpXzvh0yjL2fitmwUVxjkUsHbKYX-vlIXtBLt6Cgiibyo9yRPnQ6ucSjSC9X-OwxBPpPUOZc54MIwp3_H-oHIU9xstvka-RdZUIxU2otO3MtIzVdjn9nERVv5jPVu_cUunYVqhWLHI_Wapg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/30378" target="_blank">📅 22:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LV-DIeZPX9Qr0xselYuAV4kMBEjc75UF15kLwmIKZhat4xmafsA8dGQ3ZfXM3sKhbF_VO1VaTFF70EWc4rSNCxfozQG4T5TB1A-CxSoFG8XvVHoK_m6BMYeFcjUUr3JvptBEHzXVnk_bz4psoRzg48JHbcDMTLSOB-RQsOqwqsa0rx__J0Z9lY3-8vR8ZwDdyJis5XRrdMMpu5a5otyhSDHFccWGpbT0rle2zmXOyM8xdpJomqzD9YIWkXrVGIfst7RrUmuRt7lwE3zjKtAPze0x6vUVCRKlMF1qzcvtNRaO2ywHl-lg125RAcJrk9d0fymiX_E-Xkt2a21KK1PxNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LV-DIeZPX9Qr0xselYuAV4kMBEjc75UF15kLwmIKZhat4xmafsA8dGQ3ZfXM3sKhbF_VO1VaTFF70EWc4rSNCxfozQG4T5TB1A-CxSoFG8XvVHoK_m6BMYeFcjUUr3JvptBEHzXVnk_bz4psoRzg48JHbcDMTLSOB-RQsOqwqsa0rx__J0Z9lY3-8vR8ZwDdyJis5XRrdMMpu5a5otyhSDHFccWGpbT0rle2zmXOyM8xdpJomqzD9YIWkXrVGIfst7RrUmuRt7lwE3zjKtAPze0x6vUVCRKlMF1qzcvtNRaO2ywHl-lg125RAcJrk9d0fymiX_E-Xkt2a21KK1PxNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/30377" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30375">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgR7HrGbpOejtW7ZD6tf-UxRZ6NMzd-n6_cpioPbT-yH09vZtihfxi1D6EafhiaJKrx1caaZfvlxGn88ViSg36GRX3ojhcaHVicqOqxpF6qTUQiSQGmvaULbI95JGb9AkHY320wmSG8xNuTfD4zmiEA-wQsoASzfARvHu_5d5xFM3jE9ppuc5SthrHnE7BxQvBU8pzbKc2j3ky2mwCvMEMUvTHn8zv_gHE9ONRCaiYdLwC2iduZ7VzKV8tsytGi9wckFO0fmVqmui3Q5BlKRZWA_GHSn0LmzAj86r13XOndh-CyCxf0Qu9ZG9Ksl3s2spM3qdPgDiUMIl5iucakWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmNq1WxsIrt4QZu5ffQy0rtbKtWNCOLaAISLd-LNGhxQGS6Oq7zB_hdTEkDUbnmVX7ctfos5Bq1-KvTaSy6e6Qn7-aMw-_T75x1F-kByK4u2d5qkWHxyVeHUk8jMSJMotTMzo6-Z3hOSkgYMjb9I4fNmKuW03xoFmkWI3QtHTY90Yt0S5CVYPu-Ov14lP9ghKOak3oHazhYCK3bbyplOQrN3NSPovEQweTtZI_hJvJ-f0P8SY85dGK_kbvUuDeuFdqDf6FaCt93MdgpU5aCc0jlA5tkWZn_TXZqCtD08WTsTonOLVZ9uumW-MrGy6gN5MhY9GKBjK-wZYjedUJx9vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/30375" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30374">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebtVD3PLOh8JjVuwgv2_Wl65R0EP1IJc1OZVs_pbLbhZGsz6a2f2KzffaFZD7aGAXdi01Ay3dKg95YF01qfxEoW-_fuNsn2oTZEGw7l83W1LN147_wzlKPrVLo6JEHKXZRd8KB6deTMT5uvDVrNKLCPNPLZm_ETseufHET8NfBz0xtpzRnCt6viLCdmk9rL_Ox-QtU8SolrOs10ubEUWCbcM4Q9ePF8wRtLSL45oL86CjDlxYHkWzT0yH_KyZxFsH_oig5m5KsJgv9KkpigK0QZvNFDkjVZHfgtMkL9X6zi7KFB6PGF1r6BiFfI9JgLeyQf6JDppCLAqk1z1YqFRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ گزینه اول باشگاه استقلال برای تقویت خط‌حمله‌آبی‌ها فابیو آبرئو33ساله است اما درصورت عدم‌موافقت فابیوبرای‌اومدن به ایران در این شرایط خاص؛ گزینه‌مدیریت‌مامه تیام است که‌رابطه نزدیکی با حمید مریخ ایجنت یاسر آسانی نیز داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/30374" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30373">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-E0Wx1YjQxEd5bS-juW7W_Anvz8So-yVbMgZQ4K0Gx8cGLz_BOUMqzsQGE1TSY7aOrekiry31CgS6y_nSQdT4tw9LAZrLHy7Q3O0rFZ6OAUupqsyV8OlQjfJhXUypDm_3k7fyw33wRgVuqAGqX83XP55y3AXr-nBqKBsm7sRKFVowgTmlfL5nxb05ZvFLNM2DNa9xpfiFz-KuyFY81KguXp4MYLvN-UvjAr__rVIv62EZFivH3t8Cg8QVcj88ybtlN5SClBTnYQx86cJu8U0f_MPMY8dHwyrOtmdpxsDihmxTqv7i3DdqqN_hUAOIbVp3aEwjH1lcelpNci8Ol9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جذاب‌ترین‌مسابقات‌ملی دراین فیفادی؛ به هیچ عنوان این هشت مسابقه دیدنی رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30373" target="_blank">📅 21:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30372">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏀
پرتاب‌های دیدنی مژده نظری ستاره تیم بستکبال بانوان ایران؛ با دوستاش شرط بست 200 دلار برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30372" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30371">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30371" target="_blank">📅 21:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30370">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
گل‌های تیم ملی ازبکستان در بازی امشب مقابل تیم‌ایران به این شکل زده شد؛
گل اول روی پاس گل دیدنی احسان‌ حاج‌صفی37ساله، گل‌دوم پنالتی دادن بیرانوند34ساله، گل سوم فضای خالی شجاع خلیل زاده 37 ساله به بازیکنان تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30370" target="_blank">📅 20:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30369">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlWiI0FId_ShYZTKuxLfVdUalazaHyncb__aXci6Jdnus7Irwprmewx36DafzgsJSWkRjL6HCHLBbrsa7gSHNG-0hm-tAFvSd7Hwm5gXaA86wnX3TFN0TZrF0ijVXc_vC30Cmg73FygI12rCxgakKku1yCR66oxR7AhDan7Bii3KNc38hBZoNUuJXydseY6t2DxxpuKCGcj2zmj8E75eKjhtDy37KrJA_0PzlTu_LftFoxdRK8T0vtXJ7nvy1xgm5HK3FRabBadAfPfnj5TNEtuuQHl-Q_L9E6cx0ZSWJC5YSBh1ImqLEA2JczqojlRVHz62kyv2ywPGdhC5hIWJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در روز پیروزی ژاپن و کره مقابل حریفان خود؛ شاگردان قلعه سه تا از ازبکستان خوردند. این نتایج بازی‌های دوستانه تاثیر زیادی رو رنکینگ بندی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30369" target="_blank">📅 20:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30368">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30368" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30367">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bl62C0F0IwQN6Nzu6XY6zJbSQ0ihIL41QNHSS7nsu6Dy8_lgMHJ0Y0dAMZsx04LF-3ZpmaSYWn0rRkK6Yxfthj86a28k-Dw928F0DvKSGfvNH2D04NUNrBhCt9wSeZIo5ZZODiWFJvv404CpTgLA-v86IYIYoiwe0Oq2UaPraNNA_n8ha9643rNs_qHq_PQPZn7sqohqzFdUTNwQVEuzyaqW23yPD4IqEdGWJdRckaBQc44TlfB9rcOGB4Cp40fkJD49sEHY7nyAEqCVF1Yd9saaA4SmaLHQSy_bTM6TaDjpEaZgjxD5TEAz9XsHf_ezLL-ZntDii2M-uAFP48k7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30367" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30366">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyDkcHjDveWSBHp8V35pJwld7VVpKBn0yKdhhNCw4pHqQ4v_XuztKmcOWNboKqICwgZzLXVZ7ruaHi-6X9dqqcF4ilDxmBsILCdwkyhEC1NtbczElJqQkh_cr04576ZIsoskcOS1PEatVEYbdwtu5fniQpW7SoaY1D2mGuYtg3bQSVUqqMOTT8TmX16exuO6oabounmOFOtEzX8P5VtzmN1xaLdYGkgbRJII45jHA5VTTayl2OTEIISHcpY3boOe9rKhEKnmWUtqJu1sDZtWOoh7YlT3TpdHgHWWn8CewXx16nHOPrINtdeDk-hFaOp0gcxH73CXqAxs1MwxedoXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/30366" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30365">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CahFP-Efb--p4qAR6W5QU-3o5oOiuEuMnRAq1J5E010f2IKs2j-0lGbwy1zbEvFrak7vxrz9o5MqoCdZmpVzg5K8DX-nUaaJIf10CfB2i2pxMzz7g4PO2tyfBukBy35zJIbkccI_j5EUC8v2u_0bcISh98LsWp3ahOCAtSfNg2CXRwj-OzIedd0tpwP2yr2SgGFeh08WL2S-Co1m6jovi-MhxV4Wk0LNs5-7E7rKuWYXbfFQLkigu-GrEd7rkZunGOMBBTRvToWDyyfEeMgAeGv6rd2-29ksdb3C9f0tNRdtCjik6fHdayom-iPMYF0RoY7hdpWaDdUw6GdPOo3Y_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g2
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30365" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30364">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfGYeMqI3Z-mL4n6gGlY1cWR-FatlXr0oSCf3J31QOfiv3bZ6-FtqPwoGr-hD3yHLMIKh5AeoZ2cGPmInRGw3LIAQJ9doBaoZbwMnWGsvOM8O5XDLuEIRZ5kuB3IQHtG_ntSHgO85iRaINnaSf5tuzhx79IZRuV_-1aB0_LLganFncHg18LIhxd6-NbipiJwso7XxrPAkvtVOo29-EGc7NIDZQW-HnKSPmQt7zkpFCZaDBAgM5IurnkolD0YBrSySaM2lANlh_B4wEOyE47XEwscq-6v3t54SfMFHPMizGUYJxwSgzarnCNGKoxaayz6xDWYMiDr6pyeBdD6Anedqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
حسرت ژنرال در پیروزی برابر ازبک‌ها؛ گل سوم ازبکستان به ایران توسط نورچائف در دقیقه 95
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/30364" target="_blank">📅 19:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30363">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=pLECY5iY8C57fdU-jzb6Ls1WPSjQhjfu_uPO9atYVyvMm1lUJcSVODCz-kN0rYuDvBeXV_iTrfTz2b0hmihcQLVKAricHR2y7_RiNWf8WBTnAB1tBanuY0bLEOrYl1ghHp5Qb-H7s3Kurww8uT3rh7zAkW4PRH6QC9qkPhruQKTQv0bvG1LDYseD3rpN5NV5RkL4QZCLp-nV74MrcBWftVQ9yQN-vT-w7OLUQ7RD5_Y3BBN5Kv9PQVxyL3RQtEwCRQYD59peFGi-flTCsUEhDLtWEEpIaFW_nMBfm5BB4jFjvBPcmuZ7c53DYNpnp2X-m2ObRNEfeFcXqbcxtCWUsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=pLECY5iY8C57fdU-jzb6Ls1WPSjQhjfu_uPO9atYVyvMm1lUJcSVODCz-kN0rYuDvBeXV_iTrfTz2b0hmihcQLVKAricHR2y7_RiNWf8WBTnAB1tBanuY0bLEOrYl1ghHp5Qb-H7s3Kurww8uT3rh7zAkW4PRH6QC9qkPhruQKTQv0bvG1LDYseD3rpN5NV5RkL4QZCLp-nV74MrcBWftVQ9yQN-vT-w7OLUQ7RD5_Y3BBN5Kv9PQVxyL3RQtEwCRQYD59peFGi-flTCsUEhDLtWEEpIaFW_nMBfm5BB4jFjvBPcmuZ7c53DYNpnp2X-m2ObRNEfeFcXqbcxtCWUsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
🇺🇿
شاگردان قلعه نویی دومی رو خوردند؛ گل دوم ایران به ازبکستان شومورودوف در دقیقه 58
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/30363" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30362">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8DmfS0p1e0eqDAjX6f3L3PbzGbQWm0DCHQw3lYHJQfYaZU-EL2LK6bfsQBzwq277nM6WMTMmXqUVz1DJI71w_CVeWWLW1v9HeE0IUlCJqdTwCgji-n1isQGLrI9dyTQTjSYi8Yin8QpfIImaJFyd7X2D5sWEn-PvxEruTI-MYTlJ4OflJoNdJoLGeLEAKFmP8FPOsl-sMBwGpz0_No5dDGi7clo6oF1s03X97M3nRjYeRqd1W24EDp1nZyQRfuyogONK0H23qgLSzI7B4ckgHuSB7UgsbraLND_rcFz1frhMjeTlY9QVxnT-NG-e8Ye3Kr0n9c-FuPFTjjVOlo54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30362" target="_blank">📅 19:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30361">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401621b710.mp4?token=GdEE62e6LyayvXVG4SycWIuGSTt_tfufq9q6j_mnFxiVxCWPuce0ht6gGHHHlMq1INn0IrWmnA-IIrEi8iJ1ZqqnQ9KKZWDjFqWfpP2ONXKQiZnxDs7qN6hnkj8aWnR0o7hw2RKpQrhCYUrwfe3235UYD46cJLJgQz-NdEHpBv8W1ajRAL2p__777a_1CRELQVT00ZUyTVO7unU0Va3kACF4ay07iRhYGNaMP1Lr33AE1ZJx3Cpy7LSStnhUd45AuMy4YAsHhmixsmre0CAeEh3Mokry85TuVG_I35BW3n-C4olRZ7Pz-mA6UBdqKZXl4wyHCS7XDzzb5eS69jO54g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401621b710.mp4?token=GdEE62e6LyayvXVG4SycWIuGSTt_tfufq9q6j_mnFxiVxCWPuce0ht6gGHHHlMq1INn0IrWmnA-IIrEi8iJ1ZqqnQ9KKZWDjFqWfpP2ONXKQiZnxDs7qN6hnkj8aWnR0o7hw2RKpQrhCYUrwfe3235UYD46cJLJgQz-NdEHpBv8W1ajRAL2p__777a_1CRELQVT00ZUyTVO7unU0Va3kACF4ay07iRhYGNaMP1Lr33AE1ZJx3Cpy7LSStnhUd45AuMy4YAsHhmixsmre0CAeEh3Mokry85TuVG_I35BW3n-C4olRZ7Pz-mA6UBdqKZXl4wyHCS7XDzzb5eS69jO54g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
کاشته دیدنی ستاره 36 ساله ایران؛ گل اول تیم ملی ایران به ازبکستان توسط رامین رضاییان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30361" target="_blank">📅 18:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30360">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=H67f-grpHFTMQ6NFgSYypc55L--t-i3vX2MQVa2qZpNbEXQ7MF8jjiDBPHrOXt2p9CYbZa6Al-u6W8mLozsA7LL1BU343GOsncDe14rOkMLescVum6J6ltrQRfkgEfQ1UoFHUEWbHgpL4Y8n5jDySL3Mdk0BqXbzoAy1PJkuNAb6h_zh01lVGywNUDprlDZQXiDxKFIZTzYYrew3bRWX0SIFkis9Dht2HSHbllrmGM0v0Vw46jhPtlB-vwuxbPpSldXASq9Xme5PTyUb5Zo_r-vnKkLineXiXU3S_YYYwhkUs76xr8ol57BvKCuoLsB6hTgu3UfSlywePo1-Psk5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=H67f-grpHFTMQ6NFgSYypc55L--t-i3vX2MQVa2qZpNbEXQ7MF8jjiDBPHrOXt2p9CYbZa6Al-u6W8mLozsA7LL1BU343GOsncDe14rOkMLescVum6J6ltrQRfkgEfQ1UoFHUEWbHgpL4Y8n5jDySL3Mdk0BqXbzoAy1PJkuNAb6h_zh01lVGywNUDprlDZQXiDxKFIZTzYYrew3bRWX0SIFkis9Dht2HSHbllrmGM0v0Vw46jhPtlB-vwuxbPpSldXASq9Xme5PTyUb5Zo_r-vnKkLineXiXU3S_YYYwhkUs76xr8ol57BvKCuoLsB6hTgu3UfSlywePo1-Psk5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30360" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30359">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK6Bqorp6N8pAgRrmFcvh4vWCBLada4WVbX-EKnmYFVdClBrGM3opnRuwGT6XLBQijgwz63-t_9DzAw2C2pCLenpaCQ9H8lblpMdyc6CLNMYK74baHYFPHJznbCcYOFTHMEPcm1RHY2-c52y-i9UtjFj8SRcTG1NWqAfcDGLoIbWWLhLc_8ydJCyoNBR2eT4mZYc0Fk9HK01YWD338yRkSlo5unqq-DrwCUEz3LASDhZR82F89we94AiNEEkotxGCCCNSLEzQzuRsUwyq2BsmykNaGKBQHnjyksA10wzpegiQdoD9hG9mMYxebB2shAfj06hGgf-yVTcdiBbbaSnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30359" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30358">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=XoiNzG29mhNLH9IJ-sgM6pVNNWRQiOsi2vW4qY4ZAUEDAuSh_dtM6bSrQzdY461hn9OoEMAsiNHXMzUJEmUq2r0u_7uWSO5o1EfnQkMieRL66kpDmh0chPtSHWmK9Ky7F1AYs0Ejwmgxq7Ds-HvypNOi-8IS4xlytBolt1i38jyFBijXlxxwIV2mfpv558UCnw9Nw92LUb_f1F_Y8fUgM0ckkUcZltG4xTP4zaVU-yimOgYyeVN0Re-NeO3XUEVPuxE4o5-3mjVYzGQX0INXcMY_HlsniMSW8mdPSw3O5dtlYwHfTdRGPyOa5NwVFUYPczU2x8qB20pD-rTeceEAZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=XoiNzG29mhNLH9IJ-sgM6pVNNWRQiOsi2vW4qY4ZAUEDAuSh_dtM6bSrQzdY461hn9OoEMAsiNHXMzUJEmUq2r0u_7uWSO5o1EfnQkMieRL66kpDmh0chPtSHWmK9Ky7F1AYs0Ejwmgxq7Ds-HvypNOi-8IS4xlytBolt1i38jyFBijXlxxwIV2mfpv558UCnw9Nw92LUb_f1F_Y8fUgM0ckkUcZltG4xTP4zaVU-yimOgYyeVN0Re-NeO3XUEVPuxE4o5-3mjVYzGQX0INXcMY_HlsniMSW8mdPSw3O5dtlYwHfTdRGPyOa5NwVFUYPczU2x8qB20pD-rTeceEAZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30358" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30357">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=KwrZdLPbTe4H1SUYd--K-WQ66Fq_ktRFZiZxD6O_SWOJBmBCSfZ1SzfyzqN37C27tcuSpbTKdrEJfjQheZZWegZxhsI3BRkfTQqO8Y0f8KT59jFZjNgTENFMhBt9ummVodr96wK1YC9lwXrQg3ty55IUp5FLo1nbGZzl_ntvA20hjgW9lZsz_1XfMYIlnyPX6qLMoTvj3Jk73PJDRCbBFRw__1dRuNtdwiKnqw9ScfU01IbdlbCOAHvWrGzUVqyCH4ExhqSppGkX3OZnefT4mdCWzbJkg9oG4rMruWdQPfthawZh96kTw2TDfEDE8tv4MxIOLO1MWs2Tz9yc7zZY4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=KwrZdLPbTe4H1SUYd--K-WQ66Fq_ktRFZiZxD6O_SWOJBmBCSfZ1SzfyzqN37C27tcuSpbTKdrEJfjQheZZWegZxhsI3BRkfTQqO8Y0f8KT59jFZjNgTENFMhBt9ummVodr96wK1YC9lwXrQg3ty55IUp5FLo1nbGZzl_ntvA20hjgW9lZsz_1XfMYIlnyPX6qLMoTvj3Jk73PJDRCbBFRw__1dRuNtdwiKnqw9ScfU01IbdlbCOAHvWrGzUVqyCH4ExhqSppGkX3OZnefT4mdCWzbJkg9oG4rMruWdQPfthawZh96kTw2TDfEDE8tv4MxIOLO1MWs2Tz9yc7zZY4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های‌ بامزه عادل‌ فردوسی‌پور با لهجه های مختلف اللهیارصیادمنش‌فوق‌ستاره‌ایرانی لخ پوزنان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30357" target="_blank">📅 16:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30356">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC7VuNo2YjuJOh7E_NCUOWTrKj-at4lL6zbEaU0tMJ1sPINdbHD8qz7dMHmvyuBs4T1BIYTj5RHrzbJuNMorSWbMDjYlWUDcEPQ1m_2Dg3RaWRkQwCzVW7Pe46U40irvNTIT7ZbEfjsrcVCL4mXYMP2uLxaHd7UJsa16Ye56L2hh41VAP-Ud1Fg3BjsOTkDfXfV7AVPH3uQZ4WVYbmPfe1YsfaKrmm1mJvpplRCx6UNem0bjUBi5RgRtITTwgZy25oVWH3HVYx-_Hzz1nh7HjNVTB9vYv1v71ba_Gj6AqLe1taecAAJWN9H8yDjdnOWO3QuXfQP5U3kD7Wmdpfot-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال قصدداره که برای پایان دادن به حواشی پیوستن بیرانوند به‌این‌تیم؛ قرارداد حبیب فرعباسی گلر28ساله خود را در نیم فصل به مدت دو فصل دیگرتمدیدکند. محمد خلیفه دیگر دروازه‌بان 22 ساله نیم فصل به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30356" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30355">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9LmcpZun5H_AE9mzqVR2p2Uo1LL0AP5dNcKWfUQRUxnox5pc4x0xpekNeKP99XLiKfuN1MBGpRxn0aJFLsBBdrQ0f-0dTHJlBjaiR9ZqPWmPv4EUT2XjLWL6kUmraTEMweAUkMydIx5jnTfl74opRO9755S7hEL5oMMuwEY-rJBOsxnPnqhlDfSmVlt6KjPPL2U0W7CWUAP_01pZRER18eRrPCNqtCZUjKCCD3-PJRxKqxJ64aGy5hICIQ4ZV6rWMCHrnf13o4CzWY3etDjgsLa24Qz3eErbAB832bDO0KM8y8dpwu8iPxtxVp-Br3VND_O5QwrkBRxJnDu75VP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30355" target="_blank">📅 16:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30354">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=VF8R1kcwF80K-L4aITLTEASqRMEcRmxUhnGm3IdvCyKKW9YFArv4hGVcer91ptrh7fwqDywkJU-zIIOD6AFELZ_hpMIsp09Wmlm1vcm27dXcYBVZqnBf6TWW_MXrgvlmmjTZGy6N2xZao5b_DNOhnBMmYE3UyAwiPxlZQ6IsLFsQZ-0B35e9PeLuOka9Gx9LFLC6BUSpp7aZDNh4vgnzb4yNRNZMAswPdXZomuaKEdRLl8aYGJPFE-hMZX-JPrfgxwwTzAmZdlFTED5BUENML_K5heOJJG8UstGwn3BbtbfUmf5V8iRTw4yUNBb0YLAgTf2jGGvgOLZ-BBU9vY5D2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=VF8R1kcwF80K-L4aITLTEASqRMEcRmxUhnGm3IdvCyKKW9YFArv4hGVcer91ptrh7fwqDywkJU-zIIOD6AFELZ_hpMIsp09Wmlm1vcm27dXcYBVZqnBf6TWW_MXrgvlmmjTZGy6N2xZao5b_DNOhnBMmYE3UyAwiPxlZQ6IsLFsQZ-0B35e9PeLuOka9Gx9LFLC6BUSpp7aZDNh4vgnzb4yNRNZMAswPdXZomuaKEdRLl8aYGJPFE-hMZX-JPrfgxwwTzAmZdlFTED5BUENML_K5heOJJG8UstGwn3BbtbfUmf5V8iRTw4yUNBb0YLAgTf2jGGvgOLZ-BBU9vY5D2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛ خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30354" target="_blank">📅 16:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30353">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30353" target="_blank">📅 16:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30352">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogSbrcjZh5Sy-QJwC5RyA72NA9_0n3UOPj-SZyiUmv7tiXZAa2OCeCH3cOpB-iF_mX0rFTY1Xie8tmiESW2jW6rUs3AQMBxGt229zrHLYqiZRFxBZksihqcYy2CdKxRJ5ju52jZcqZ5pGIc3sWOcD1Z2Fch6YG4NtegLFLJ7qRbQrD0IFkeoBqePo_aFwJuBHXyQyyOAdWe09N-Tkgp74XwcY5gM7or0Tvi_E4U4XQNeKyAFiBF-MsTzXnz9O3_9tQwWcqF-ZkISySUF3Z3VSORLcbusNJM0Iamq6LxoaJfV5Ba8Td_Br-i2yHOUezocGfXwCg7wUMWvvEZ8hMG5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30352" target="_blank">📅 16:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30351">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCpapDqbWBQJeiraQc2tH-hAAVRuX4YzANYL5OPazFzhaQ3SrivIYA9pdQ8WzSVh0ckSURuT5hkoSOOiUgD0g6ZOJHD838EONBHl5CbSgtQQuTBnHvIcsiW5dc1TQnQntUiXE7U3hYbjP_ruQN29vV8vFh39MhV6sUAgHJ8YC67leQtTX3mnDtuQmgoIMaUPUYXYjzPaHvLDOVvGXahQZFBH05SDLCSaTomO64doHfHtGqwmJjpDhou840K0PN08f04EK5zWIG4GLx8xW5cl_3LQR3oVFfgyxz6D0Ye_uxN53QNjCy5KlklEVzPKB5CMryvB3OvYrv4_q7nLxJMq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره:
من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم منطقی به نظر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30351" target="_blank">📅 15:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30350">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A57RYLGqEV-MX9eKoGVxSBBgTwYpHWZbgXHcGcOxqwKzP-1JYlP_MMSussjaXRkicd7p1-HCBsN0sfPUxRAtmsp5S1zY7kdOn3tNFH_faxFaaB3SRzCJxDS1it0oN91ijIw4ZfOazOhXfw37C61q0LEVCPXDyULD9SNPY5Q58RZpc-ObZjgDO4maTtfMYI3Q884UXZgg-C7o5nNOU1B68WF-GVHDFb0EUZ4e4Qwp15VnaVgrTI7C-aKYs0Ie6IbWm42GJH-ovUjiYq4cEbSy3wnH-M4zF3MRUFx0ghSUij6chuUMAGWjVINpKir8CbNTQxKx_oR4wK0NWGd0G4z9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گروه‌بندی‌ فصل‌ جدید لیگ ملت‌های اروپا که از امشب استارت خواهدشد. این فیفادی با فیفادی های قبلی خیلی‌فرق‌میکنه. تقابل‌های جذاب یورگن کلوپ، زین زیدان، توماس توخل در پیش خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30350" target="_blank">📅 15:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30349">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPGPTlRPbLFRvQeLY6Ig9HCjbsmokBJlneRWLliF2VvcomPL0nsA5JotEp_jyyqWIRnnM-lImLd2mb5XhBjmaCLuCqdvolPWy6wjuuuO6asjbMssqaVV5XqKdSx7qkWH_1jO51XgjbBZc0ppepxvBSOcE_6oioNmWuU8IKvP3kl9eZDrjo5Zru3FRkjYdcss_zvcTx0Vspb48gRQdwhjwgmLSlkDByraMQWYV9BIBGtgIUh4Yo1uglhEf6fNl9Ret6ts92BiHOqsBUwcvLRVfcYMk4rArBdDubRXztIKx6J23aT27knMi6s4xGHRiF1mJ9nWKrSgNnF1OWZLvek4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30349" target="_blank">📅 15:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30348">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Qr9r0m6tf5g0lvcZVcyFKsFkK1YTcQOs_oYbGlT5EvK-tySPFaPsgBullrduVlvTAXIoyUpnLP66_3PyoGoSawNc7t_3Jnx4JG0pgIagilAePXCbS2X6mLwR5fZOcY0Dn_GkQ2-5C8Y0KY1MSIwTlH8mN0OzyjB6WDIa1kv0IMBm6U335eKILnEjycNRuYbSkCiSL8qT0A2AzcElxMKCEZ-Ukas8EhnCb4yfQlFlgcFinBt7_qPnD9dX7WUkg2K9bF8wHIJI09PEZpSXd41lvTMAs796ntjJpbyd66ON8plLndVUGWQUlls8S0O1VtNQkRiJSXonuiGGc7_pH9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30348" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30346">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3LIYguDFK42BRzU5TlwvXXLuC3Tz3P1UCNNE-Jo_vAIurQHuFh-kmhyf7tJs4XjAzzDKQilXEGav3E1Pl0qWQsaa2FqTMI97ROmB0Vp33ohAEzi2pMwzvGXzyPo_YWLBi4htmdIuD7xkG9ZCw_pBQvtRTBi-EnAasxhXmkQqRopmi1nXLqUL-3mDgLVdk0hvu96LLyL-asZZ0-wPXNyCxpcFWZIf2tMnK1t13ZO9C9682RY3WVOeI34ciT6MZwhB3T8JeGkUfcYOfdcjaRHsvjIBBcgRxoqh4kUc9mznQakrgP5BSOJ3arrYsAa0QoMBeYwf4_sS6ETykJmGgrzIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره‌کننده‌وفوق‌العاده کریس رونالدو در سن 32 سالگی‌مقابل‌تیم‌های‌اروپایی در چمپیوکزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30346" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30345">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ft67o6_JyNJBVqq81AYE38__37wKcw99jiP_O3QUBAYp4sqDVoxHRD-ty6NGQWe_o5TCBsT0vhGa3LcSRVmS7-4q-rCukcr0eSHMYyHyCblHBcfr2mS-eB0_BojY_tBjEY4oLeT99hWdxCZaXEyUy7SaHXyFgBFkcbRv6_4MGP6PvF_lKn2YaWx2_nm49kVUAim4JFR8NifnIhfYNmc9W6t7B2_rM-qDyXpTz5rC2L5n2mHP62pkw41jJJU4EsTYalsyA8BvAysxuQxp3a3TfyxSp6JpNdWTOOUEnk7HkC92Aq_1pgJocmI0WwRBYKS5CoT4guYr_bnu2eqdIbETfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعود بنیادیفر بعنوان داور وسط با کمک بهمن عبداللهی و فرهاد مروجی نماینده‌های ایران در جام ملت‌های آسیا 2027 هستن. علیرضا فغانی هم به عنوان نماینده کشور استرالیا حضور داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/30345" target="_blank">📅 14:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30344">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kImhB8l5yhIB5xhx22Uyw1-rETSup4beDHGq-tTGxi7_idLQagCQv1oSV3oAiqtGYw_wPp4nIJZ4NUAiux5MpbwpN4j7I_ksLFfTyUOGXl0JaC-a-VPlQyQIFVa0TrurlvB_kZPZW_I_eEbbJxbzqKTZ6b0HRHITZIm2-v-8vF4TZqp_HZHD8KoZeaslePywsrLxTD_Huwxx3_iKjkB9d9PbNNi_YUayOq8Iu1a9xcDRQ71rALr0KZKsiuhwhdstEtPVlQiUER1M6nfUps82AOQklMKdan-btdJpb2s9aj4k28IvHLP8C5bfC35nLhKe1Knf_qpnHyKatO9VCQGZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدیه اندونگ برای‌عقدقرارداد 2 ساله با باشگاه تراکتور درخواست دستمزد سالانه یک میلیون دلار کرده و اعلام کرده هیچ مشکلی برای بازگشت به ایران ندارد و حاضر است با تراکتور قرارداد ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30344" target="_blank">📅 13:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30343">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxNxfVuH0Z3MhzY9OTu9HQfWt_ft_tIxj4aDw-GElXjq0rpLrme5ko_Ce6p133U239tDLPZV2pnYBTZymB-Rlb7CU-d_NtBil8SCZo2DxecZ-XVDxz_Pe9afwaKD8nq6KYflm0LMWzNbA3TV13TZbzJnvOkQRYEVLsujBPtQM-7cY5WJ5AjIHxDSFI0Ze84r8Yg5lk-zlv11Oi_-PEPnNKM_0md1tiMWJiliN0hdRHGb7FT8nCoqj6AqMIUxdNtz7ECqKbJkr2k80OjOBHvCuVgZ4-IWRVLx9oiIt_ALRf43WS9kwgSpf2UNLnnuwKj_RvFkaQwqXcEh2Pm-1Pwq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
تیپ و استایل متفاوت بازیکنان تیم ملی فرانسه برای اومدن به‌اردوی‌تیم‌ملی این کشور برای فیفادی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30343" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30342">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXHQI3rwzIVntOE2VYiT9qfmG_nSOYt88_ZLwh78t2A2BstfV_PGwe-CnJhwQCP2dsZdnPKwHEsYb4L0Pdc4NyGypZcKFjZvZOZWHdme5NWFOTnKrHA_zPPsd9hkPXYpmBs44XIZTXVsXdiUnrCwRQZWcMD3AH9kAgyOEISOcUZnR46czSB6z8-e9oqQDfnuQoX3TUcEcdR06TbrBpS7xCH1PZ1BES3QlF_lQnPErd4OaPvDPS7u8Uwd3MMtWpteGNgKU83F0WKwDdJiJEMRv8DdRffjAoVY9-y7q12sxLQgZ7iYBFhNBD18i_2tx32C-u5y69Rg856W3re4nvI4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30342" target="_blank">📅 12:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30341">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdp4qWhbV19fq0xJqzGD5KrnJ_dEbWmBV-yAq2R2TzRrmu7GJ-bkrqNgZ9HJ_5K5bgfDoIT5zGV-ZmKhOXr0gXfdIaMe3Dz1vBSnr047K29pnMm42caBt89jTzTfWSYYgq6l_oHxn0dC6HSk2BBxzYwU30PDfgGtjG_TlQPCI6MORfuXbqL5f8IN8cfnvYqRkrC1jWs21X67EvgAfNDz4u4eh6S3ZVzmmC-PXB4cwT_HmnAfipgbqqpwbWgjI7k6GRnXOmCFxQA3pRqzkYM3-g2TP4TxFeujBnO-PjOzbg2Tz156lnVvSXz65ebaHV3Qe8LUO4NJN7eqF9_9gmFCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئالیا:
چهارتا مربی عوض کردیم این همه بازیکن جذب کردیم پس‌مشکل تیم چیه چرا نتیجه نمیگیره. مشکل تیم از نگاه کارشناسان و پیشکسوتان رئال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30341" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30339">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvL0fVMbd3rBp8i0S6p50QEWfiEwZypOfGu54OKyuNoSetYSrxH15CI_xG2LsueuBwAsiwBf0t3gSjSsBlLtQ0WQO6mWZk0WSuDb9cXgmo7Gbt-aw-wkkIPK6JGXFNZ7ZkNzcT44hQLzj2ZUdPUsfxge6QjCeO7bSkL8Y4KzsBK715WYsJ6JOaKA8r4t0mmc-MWcAwUYZi9Z9Iw_5sjLHLHlL83EblTFMwhkW1cT1uZ-f62kuVUAUvUf49E1GODeEdGtRW-aysG9amQa8TiGMe1X9OI59Yrq4lOKsJgKa5WpbSpiaRkkxdjKYUa4GtbqjvrDHiXdWzM7ftIpIT7kNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛ تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30339" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30338">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-8gQYirwy62f_37GxM_Oe1JRtjCMDj2fM5yyovrfxDPTrTf6Xnm6cPCLg5kQc3EFRTYBgKwu0vDWa56BSbo5eoBOCkAJ3l0kGjMekAvhz_MvFyZTZ8P5uLCl9JRaNjhV1H8wWr8WfgXqimUApmagSNeQ0BweDRQsrcihqiF50PjLj2k2vNlQ1sMtjp9FSyX_vwSwrPDCWqzebKMjuaP53Ed6h2rFEefXsNIwsS1oD3KI2-h-71jS91KJ1spd3zqmfccJ2CfmgRrfSQcMMwEq63wnuQli6sgYEGx1KhYsO9WBsmn8Z6nUc6gtiM6kq1Ss5hjchKJFCfMBEdelUcOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛
تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30338" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30337">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P24_0pES5NMJNJboSXm57oWSzXIo8eCyfjjvWAS_Ar-ogSqgA8kTfsuvvtpWEIaA_EoW24OUvdl-UL4gBhNwulBWS-1FdHfUfsYpFGKta-Au9OK1tjYSo6jowcVndbRuyKQ-Tu36yPcSi7HqxVUHO7IkxzkwcYqJFJ2qtNvhp6FZd6sOqgIVdy_UtGKb5JHH0H3I3jmZCmcR8DjyI90syzFBANDYfBbFxbR5WsrjpJiGeXwPqK8HmOxR5KpLb1sYb4366iqKnV21Tyo2CetNhivddBhrHgIvnx2AaW9wT1qHoa6dkTkv1O4s-XNhMGj-YH0n-OyyfmkUcblc8yFTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رونالدو 101 بازی بعنوان کاپیتان تیم رئال بازی‌کرد که رئال هیچکدوم ازون بازیا رو نباخت‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30337" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30336">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPvIfhgN8voHYeKwT1VVnIxyhHiv6w3UzCgDrZugUmduLl6rKOIi36l4ee8HInKPYvw9SgJ2hegSxkybe5xTlNxe9XZ2ssg-YP31BeFGNT1fz2xgKbW61Hfvch924daqCvRI0ghrQyv7TcP4X4atk-wthPdpWVUzCsx7H6dV1HxOmCmH0WLCSktpzklAKW7kcQfFDYVZ5Hof-L0lnjCPgmysDugsGwEmvRwmhypK7ugcaOfu7_D6vGdCQtujoaZh95YhbcOFOVwUzXubIn0YqHUMqPnXJqYsdXfcFpl3y2sqr5cQghZNCZ97Dwt_RlNzxe3ghU0qqzeMqWwbHUx07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
میدونی تو این اوضاع بد اقتصادی تنها راه رسیدن به آرزوهات چیه
💵
💵
💵
🔥
سریع تو کانال زیر عضو شو تا با استفاده از
فرمهای آنالیز شده توسط یه تیم کاملا حرفه ای
یه قدم به آرزوهات نزدیکتر بشی
🔥
⚠️
توجه داشته باشید که تو این کانال به
اعضای خودشون همیشه‌هدیه‌ی جبران
خسارت به صورت کاملا رایگان داده میشه
⚠️
✔️
پس سریع عضو بشین چون عضویت
محدود میباشد
⬇️
⬇️
⬇️
⬇️
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30336" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30335">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw2DgXT2vSL2XfM6E1HlRrsOQhKdFkRye9SgNANgO5Az3a7LM0OgpYmmmccgp7MHypNI-U7MryHhXnIF4pogkqTYa_3QU8VBQqP0eE5fzioDMe04kfPXB1IHImnkfwp9k6Q1D2MYLbsnLbDe5GsyEi4EimaIur4jysghTXupGAimvX7z7M8DTzI_1CzsrdwnkZ1Mbjms_llsadG5-MtXzrTsROyZJL0Y4FrdfcTIBKiOJJ1-l4D8r-TWoRd_DljRF4-S9zXHQnZJsCrB5h1XrH-LkTaWXQbOWg3z0i7R90Smu9-n2UF_ChRhXr8etsdED6T3patXtVWtYq6nShxRBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سابق سپهر حیدری: من زیاد اهل فوتبال دنبال کردن نیستم اما در حال حاضر بهترین بازیکن ایران چه ازنظرفنی چه شخصیتی رامین رضاییانه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30335" target="_blank">📅 11:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBydeWceUXqW-5Hw_wKD3hyhCqasWTkBa4BSPSLjtuNVuhz0vP3k9TwF1zJNMvm0CymLK0HQq_OoX7m-0n3BX-mIDq_sv0NtwpsaCvlJDReihrUlNqblIK5yhHZz7-vyyexcWrSDDr0-YwnwIm2wTT3gUdblZXY7swU4pNedTZnl0B97TAJCVZ5xSqs7gqXmrVJPOq7IqISn27XblSBjM4D9WTOftWp28IpnLCV_1jUAyrPN-Q6s2zECdwN3pFqtI3e5dYO_tkzQ8Y5wvH9AmyFh1ih0kqwjTn-1kSrmAnB42tO1cPnQktc4XgSQdEMkOZi31Rpx_hgQgd4Lugkxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعد از عدم علاقه مدیریت باشگاه استقلال به برگردوندن دیدیه اندونگ به جمع آبی‌ها بخاطر مدیر برنامه پر حاشیه اش؛ حالا از تبریز خبر میرسه که ایجنت اندونگ این بازیکن 32 ساله رو به مدیریت و کادر فنی باشگاه تراکتور پیشنهاد داده تا درصورت توافق با این باشگاه…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30334" target="_blank">📅 11:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30333">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=BUUl3gelzyRu1uzbScPkIcnR9SqIy7GICiL0Vx_iFX1PZfgk1M_ks_XPXeVTNYl5h9g6FAkNkWUBPIDXY8QZUlzP9ZIsCtaCvoo2E79OS1SNY3p2f7ug5c7v0zeKxFWY0f1qmxAmfQ0G0gmiOhuEychSrm1qy2pCYXH1d-36EEp-edMWdlU-US0Im2JKGKNbnXKwQVweArbRUCLzS67FQ94QrRl_Sqf5ZkCJo552eEk1qsqu0uGDcvt6_-BpOdstxe7sea58ZAJovrb5DEcdGoplZC9NTq9rBSeIdKpYB0qx9GfHmoOhZUL3Hu0-ZTZMXjxizoHLwhAZNKPxhxkB5LIOmXxN_6zOgrP72LM8dkFNXLNyGXoVGibRl8_K8BVa-V-KLg2QAEW0ecg-uGgNeZ4v5CacP-Oi7_rApcpmSIXk5YHXR5CfA6Rm1qBBbFH9B7TU4XWFPfInBCKOgGLgLFrro8BZuoR-kuOmIvYGaZNGnB1ciVLVw1_xLSqy_z8MbuBkmSxziHcBMHKEzZDMMg0FRchgpWyhTiomvUoBQTje7WtIQ25gVU-zS9gEf9_tx2-t9-ht7t9MVrKMifYD_dEhYIGNT1ZFadkLbgPVSOjv-0lAbT2A5ifGZGfxdElnZ2wOl2YhX3buLJhAHCYfVJmi2QQap0pi-EoWRI3L5mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=BUUl3gelzyRu1uzbScPkIcnR9SqIy7GICiL0Vx_iFX1PZfgk1M_ks_XPXeVTNYl5h9g6FAkNkWUBPIDXY8QZUlzP9ZIsCtaCvoo2E79OS1SNY3p2f7ug5c7v0zeKxFWY0f1qmxAmfQ0G0gmiOhuEychSrm1qy2pCYXH1d-36EEp-edMWdlU-US0Im2JKGKNbnXKwQVweArbRUCLzS67FQ94QrRl_Sqf5ZkCJo552eEk1qsqu0uGDcvt6_-BpOdstxe7sea58ZAJovrb5DEcdGoplZC9NTq9rBSeIdKpYB0qx9GfHmoOhZUL3Hu0-ZTZMXjxizoHLwhAZNKPxhxkB5LIOmXxN_6zOgrP72LM8dkFNXLNyGXoVGibRl8_K8BVa-V-KLg2QAEW0ecg-uGgNeZ4v5CacP-Oi7_rApcpmSIXk5YHXR5CfA6Rm1qBBbFH9B7TU4XWFPfInBCKOgGLgLFrro8BZuoR-kuOmIvYGaZNGnB1ciVLVw1_xLSqy_z8MbuBkmSxziHcBMHKEzZDMMg0FRchgpWyhTiomvUoBQTje7WtIQ25gVU-zS9gEf9_tx2-t9-ht7t9MVrKMifYD_dEhYIGNT1ZFadkLbgPVSOjv-0lAbT2A5ifGZGfxdElnZ2wOl2YhX3buLJhAHCYfVJmi2QQap0pi-EoWRI3L5mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری درخصوص دعوت‌نشدن برخی از ستار‌ه های ایرانی به اردوی تیم‌ملی توسط امیر قلعه نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30333" target="_blank">📅 10:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f00468324.mp4?token=D1VW7CTrgX__VunShBmtNYuiZKr1uzebmAaPLTqYk4wtDzSxJGbJfp3Xj-62R-P_RgKNdgIVFH8CyRO0iELUN1OpVlPrFzY08rgY1Xh2yZf6FehdqVaJ36ol1pfnJwoB1alsJvqYkzwUxnTwtZhR--ufx93f7lxwdQQZw9rJ8dpxe7q2Yp3rTBHZBGEe8lPZgfwGdLV3ufLIlaYUKaQZJWYrMfg-e12h4fVkGr9CQQ06tokuRRnpNxjRV_C1xbgJETcBAMfmAzlGEM3ie1kARPNyCpPch5Z7EFUJf-k7C4g8NdRFZQoRj4tf_uvbR8_a7Uy1OSQQFO1P6E77g6yqUB42ZUqAaLJWfniMMMt66DqGZTMJ5ZHJWHn7WU-gq1r7lg8-hjyxxmP-L89fKPtFep2rCh4bN2z78i9lyYax1KOoURs0dio-aMSwaN0rTL6cO39W5IuH4SPRxy32IoUGRqMq4Qj1UEt-KkKpGkAlShk-qjWLEwdN0oQwJN6Lp6V2ZNERjHiOnBlsEvK6N8NQik7BAwA5DHC0nUZjcS00Z4CONLBNWrQ6fXx-EtR7IYsl4gNl2EDVF4klvegH9kcmlY0wMEKjl7ti7eTbS6W1fI7Wanpm7ygWk7rNvKvGEA6m7NCs6TjQM5NmcnEn_YBmLtvSSlIldFva8P8Ytd_ge0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f00468324.mp4?token=D1VW7CTrgX__VunShBmtNYuiZKr1uzebmAaPLTqYk4wtDzSxJGbJfp3Xj-62R-P_RgKNdgIVFH8CyRO0iELUN1OpVlPrFzY08rgY1Xh2yZf6FehdqVaJ36ol1pfnJwoB1alsJvqYkzwUxnTwtZhR--ufx93f7lxwdQQZw9rJ8dpxe7q2Yp3rTBHZBGEe8lPZgfwGdLV3ufLIlaYUKaQZJWYrMfg-e12h4fVkGr9CQQ06tokuRRnpNxjRV_C1xbgJETcBAMfmAzlGEM3ie1kARPNyCpPch5Z7EFUJf-k7C4g8NdRFZQoRj4tf_uvbR8_a7Uy1OSQQFO1P6E77g6yqUB42ZUqAaLJWfniMMMt66DqGZTMJ5ZHJWHn7WU-gq1r7lg8-hjyxxmP-L89fKPtFep2rCh4bN2z78i9lyYax1KOoURs0dio-aMSwaN0rTL6cO39W5IuH4SPRxy32IoUGRqMq4Qj1UEt-KkKpGkAlShk-qjWLEwdN0oQwJN6Lp6V2ZNERjHiOnBlsEvK6N8NQik7BAwA5DHC0nUZjcS00Z4CONLBNWrQ6fXx-EtR7IYsl4gNl2EDVF4klvegH9kcmlY0wMEKjl7ti7eTbS6W1fI7Wanpm7ygWk7rNvKvGEA6m7NCs6TjQM5NmcnEn_YBmLtvSSlIldFva8P8Ytd_ge0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های محمد احمدزاده سرمربی‌سابق ملوان درباره سختی‌های عجیبی که در زندگی‌اش کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30332" target="_blank">📅 10:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30330">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYXAL_o8U0U2lNcnXN4JX_D623pxaLWxIWnMtqnCyfh4o2T4mcj5LkIMM0ozpx9jdUI_2bH3G9S61C1WccDn2P77M9kzkaQz6pPVEy1sAwiKgrbZBSHXh7neyU7r3G_Jp7xP0MnnKSXIcATTpBSHT04wR2xVNlnsjK90xz5mrzMhpOCXeBcdywP_dOzTqp0GOF56AoMMv1j0jwRbu91EYekdRNh2A7VNqY5tMnoG8dBWp5YpcVCBOeKiSmxqIkluFfBxPSurBHVQrpzXMyzCvSoV1BxG6RD6n2xkPmJTDQLnUPqKAQW_rCDMAmTzVGt4zMTgXhfS_vzT5NDD7suw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8OsJzMexfPTsP990pKMSZ9sUIztK7u-xbDXG-kAV5-vT0SVYKczaEHXyQgZOBOvN1UKGpPPpHr54hzqWqzldM-z-K34WYGbiHrBU12NSqRiB0n36caquLrepNsEZL82l_jU7-OpgkzprBDo2h9g-tLMpvZjJ_myUiFcesNP7gsBpS6F6V-q436CS01iTg63MC8vN4cUPw6jgAKLOZKhHO4_8H5J1QqTSux3xoMI1zYRwBDhqQCYH4z2cH6ef0qKw1z-p2Ith8qO8PQpqg5dypChJKV9KNE9V_qkUMH2UkxvuUw6RTu9vHBmDhUcSUnNxOFZfXuPVrCT16qrs__z8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
فلش بک به سال 2012 زمانی که:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد 85 گل به ثمر رسوند.
🔵
پی اس جی 86 گل به ثمر رسوند.
🔵
چلسی 87 گل به ثمر رسوند.
🟡
دورتموند 88 گل به ثمر رسوند.
🇦🇷
مسی به تنهایی 91 گل به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30330" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30329">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=akwDeo9SKfnPnGLeGRT7qKAUnTN_LJwS88txxdS2NlTUc_3Nc1p1ImqrTTHDzufOe8V5Apk0FTVfmXsiewoZYZ2MxmlGIIuGO8DqdY7RRi_F4DHg7Ir7v4LqQJNc3jad2EQ6Ay9EQPxVdMP9uQCiIZd2eMLoIGt1TSu_Ai4xlGyESiUJ8mxhq0bDlYhfScXs6u9uB2mse64PGV3N_ofT0DfBMjCZpYQ1z-0VH_LpdI269IZ0ktrLmc00carXNIGmK-QGMyjYmajL_zTY_aB84B_m0bOp9YSbLaUWTOWXS6Lhoq6ir1CcthgybuWR4X3_SWeQK0IS7OB4W-OzRLTTFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=akwDeo9SKfnPnGLeGRT7qKAUnTN_LJwS88txxdS2NlTUc_3Nc1p1ImqrTTHDzufOe8V5Apk0FTVfmXsiewoZYZ2MxmlGIIuGO8DqdY7RRi_F4DHg7Ir7v4LqQJNc3jad2EQ6Ay9EQPxVdMP9uQCiIZd2eMLoIGt1TSu_Ai4xlGyESiUJ8mxhq0bDlYhfScXs6u9uB2mse64PGV3N_ofT0DfBMjCZpYQ1z-0VH_LpdI269IZ0ktrLmc00carXNIGmK-QGMyjYmajL_zTY_aB84B_m0bOp9YSbLaUWTOWXS6Lhoq6ir1CcthgybuWR4X3_SWeQK0IS7OB4W-OzRLTTFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30329" target="_blank">📅 09:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUYL-tURJK8aa-EqW3dVXCX2Mce_fmOxo__vJlE7OCO3AikIL1vKTpauqnqZbzJRq3bE84pqQlCHaLJwmlRZzB_5toD83wHlSqYixYGsMlSaPPrL904vN_UFheps3dVOBMOh11nUAOhilK-lm5Yey7pBPOQstd4Un23mCMoP1rvoWLykaHo04kEFZhbcWKsJM8V2rgv8kBKFRGyQ-LAWXtCoExOonhiilSinucgFDKvYtJwvor40K66QNz4QNAHdcrP--HsHSquaO4-H3DLkrbFmc-YdhqTtcBa871VRcsLP2Czmj95EqwkFrV8p7068p4Q7mJMo6HjDKG2g2LQx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب ستاره‌هایی که علی رغم درخشش خیره کننده در دوران حرفه ای خود توپ طلا نبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30328" target="_blank">📅 09:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30327">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK1tqY83ERrWlrGZb2KaTNvN8qcEdwrC-nDb9LMMiW3gWBqIaf32AcpyMzrqbKJfRpk6mriNPQR2UXKgnFK8acieKxOsuWnruxMmtsorMl1jfmJCOGfO8N6Od4UG926PA8yc2CqVIYf80ehgpCJ2mfB34CHC4190ReuG8-loZJZFxYDuwNwc7-9FOCkr9qlZIbDEMhZ6qje4OG8P09Gi26zOSR5jQxZ7buu8L1a0AGMh9C2JC_yFZ21W-JszDUCoJLFjHKv1EJqoMg52Df9GiByHk4TgolyW1QhPDKses8EwG8OQv4qujRdwXdHQxw-jMqnCjqPnbVWwr_9iFrn_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30327" target="_blank">📅 01:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30325">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMb_pjXCdZZ7fgN86uazWQsNWV6-yN-AMtLPv7hRC-GeZVYWVujXwFFQB39qZrJ73uAs0sm47H_MPLV2LwsDtwkLFDZTHyRsudcZHdlJDdd4ss_4dIWOWqjRgsyAd996W0PlO3NNvloEPEcjvHb8gxXxG26illxVQRQgBmGaHAW7d9nyUcTQbA7IjsaOOk1_L0BuRP8eTrm9fGB0sLVTN0svXeSjHuvLEI4BPpvl8-axgXy-2Ixp01guWZjFTHuCnzef-DC_buB1cQ3xhNoD8BdwMAeRvlyqeShfla_2l1gs3oy__UqzwestYJgbKMVGYoVQa9sPeLK93Kj-21Wnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTuP0QmXIt63tw9n-UhkoaR_grQKi35Y6hyxXyJHfASLyjDpHCoYzWYKh8hJvBhuGjv32IFB3IF26dZFx7reOdPUmLH_sof_VovCUKVboC3xxI8XFObiE6OPZmVsPFuempsPdAQi2pY8GtnkrMlh7iVrl0JWbR61nv0xqifKrbNVNwrgjYOnS9qhJTpEDPknSyp5zC0Wsu_doeJ5-UrlSaD0HMEKRvw-lCFbllZN9eCrmXovZS2gPDkm06fojrZXVxQsckdMecwqtgkCC0nPrsjCfT2Qzuc-vOd1cx7seYdesvJ9n1_nqT6lc47T7x8G5rJuRmk5RUCA_9rjXQHvxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آخرین رنکینگ بندی تیم‌ های ملی پیش از شروع مسابقات‌فیفادی؛ اسپانیا بر دنیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30325" target="_blank">📅 01:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30324">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=j6-SpSC5u7Pcw8EL4GSDHiHMYFUKKZfNBh82SdlrZ1j57dwAAC-JvwkIJllJJpOmYYxgcEYjmy4yfA660MDcQfWaZyeLq768Xx3K4Zgqgks7tD6CIg_wx8Y9JdMJ7sZzCRZHDF_46L--b-Vn9POv8sh6Szwed4iiwW5_aD9mO97CY6QMLJB_NkiC94Sbyv3oY64j0vRgSprlvO9rQl1OgTV1BduIG4eGmVNO1hcVCYKaJ7HOfqcGqBi01wnMunCaZOH4rKMvzRNWivPd8DHkq_ZF5D-lIisuI0QYCVOJNvSjp8sXCpjtaZqBTX3rU8YntKpZ-vOJO5p_0ONRm1J1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=j6-SpSC5u7Pcw8EL4GSDHiHMYFUKKZfNBh82SdlrZ1j57dwAAC-JvwkIJllJJpOmYYxgcEYjmy4yfA660MDcQfWaZyeLq768Xx3K4Zgqgks7tD6CIg_wx8Y9JdMJ7sZzCRZHDF_46L--b-Vn9POv8sh6Szwed4iiwW5_aD9mO97CY6QMLJB_NkiC94Sbyv3oY64j0vRgSprlvO9rQl1OgTV1BduIG4eGmVNO1hcVCYKaJ7HOfqcGqBi01wnMunCaZOH4rKMvzRNWivPd8DHkq_ZF5D-lIisuI0QYCVOJNvSjp8sXCpjtaZqBTX3rU8YntKpZ-vOJO5p_0ONRm1J1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل فردوسی درباره زندگی سخت یان دیومانده ستاره 19 ساله رئال مادرید در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30324" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30323">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=pyyNN7QjNjSMVEOWRZub2rhn2IOmsKR4-55bHpKr8W56tpGZ-CKdkm6Sz1J8sos_VxI-hw9TUoLEfRJ5LKNiSwkp-kfv607wX0kU7OIT4oj8c7ReNHDuzmF5evg_XhUiwNvQwzrXRqa9cDsGLT2MVsWX13BH79sPKHBDzbaz65q5D_evf-FNNYxt_RNDf-FSBzN8l_ETkMIlKIBAVf0YGnedHhToF8m1XtEh4po5m-8kUkpF3w6Ix9FmGM8ZFyaifHKDoStoJhdc0n_QIoFyFAHCL5LNgzqUh-cit7-RmBA97syhC1XYe2wpG6dt365Y3JjJpM9_CpqeuFyEN7TRBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=pyyNN7QjNjSMVEOWRZub2rhn2IOmsKR4-55bHpKr8W56tpGZ-CKdkm6Sz1J8sos_VxI-hw9TUoLEfRJ5LKNiSwkp-kfv607wX0kU7OIT4oj8c7ReNHDuzmF5evg_XhUiwNvQwzrXRqa9cDsGLT2MVsWX13BH79sPKHBDzbaz65q5D_evf-FNNYxt_RNDf-FSBzN8l_ETkMIlKIBAVf0YGnedHhToF8m1XtEh4po5m-8kUkpF3w6Ix9FmGM8ZFyaifHKDoStoJhdc0n_QIoFyFAHCL5LNgzqUh-cit7-RmBA97syhC1XYe2wpG6dt365Y3JjJpM9_CpqeuFyEN7TRBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چالش‌عجیب‌وغریب‌امیرحسین‌قیاسی در قسمت دوم برنامه جدیدش با خوردن آبلیمو با غلظت بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30323" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-cMcN2BkqOwmkkXuqAkWBoX1pwCiQWiDEr5Ehz45curz0KKGUuFBHfBEX3n8Mpm3CtDxhpgUtupmZwlk56IvQqjilu1E1T_7YZq8dJTNkhRxxx4CHrHa6bz5S2IolHPjPf_ahwxWF6FTwt-oODI6bzMk3wq4cF8M__CqfQJRrhIRVSwX-Rpi3jNbtz5hWU5VD2a4Kcsw6PwnZXf68u9jknwPFEBISmhSElbmJ44HDrKynylLjlh3ThO5BiexgvtIt4Sfir1kJo_FjLB3MDBBXaxNLg1hoo-HGjhHf8ZSKDD-ci1eCHw4jw1soUPEddMyQj3V442m63JM6mK2D6Axg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30321" target="_blank">📅 00:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30319">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2ptmYKSq6P7h_I_10Ebt-dOHmP3GbTKGl1pDe9vncRd3vMOnYH76G5dlEV3s2Po7NoqSjngWo-q4yq5mxhloQeCmE53dxUOhBCgYuyK20e8m_6x_DTtDZZDoHA5ARrYAy2fkE8vCFgsRly7KyLctJvRL4-uonJypl3gcSwSo2Ase5to9CXIOYAE5QEwVKSERseXdPg2fB24TljHsYpvnL9ND9AFhzAeWnO83rQGo_MiuNCIvQocpVwWRnMRiH9sWAPdR6M4ObjJJolHIHFeObwJYuYylY-pX7RFjUrce4lvKaK_ads0uDXITvrnFoxvjUvrrYwQsRSne8mm71CtoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30319" target="_blank">📅 00:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30318">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFTFsLHaUYtRFm98J0k-Vu6zvt6tWDjiS1ao7yjyRQyws13epv1IeY11wqi9liizThYn4Fka-FuI_akL0iBNepG9KkrUKQ403DC1sXXR5awgJWtcDLACgbB_lVmQVSA0VfNhLf1wJ0k7n3-R69QABdZSb3he27zYlF6tVH66kBG_S6_Xf5leI9H7KCcDsJpF6FJBLTv7jzObSszA5pT2332BTb43ZsZ7pEcEaP14rIECBFIiC1TLC8ErA1DINgH9Sf_wnB0NhSm4oaOhJOehn3q23EgxAkXxGgu6EveLm2kP_e0JuJcwitZfcTw0wDbQ4rKippj6R_0vf3Ix4lbLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌‌‌‌‌‌تنهادیداردیروز؛
شکست‌مفتضحانه تیم امید مقابل کره و حذف درمرحله‌گروهی بازی‌های آسیایی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30318" target="_blank">📅 00:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30317">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpN7v3qlYmp1LqD5M154qOb2rKaz3saeAfMupHa0BUKyebazoS2IorvZ5ON2Nmpo08fKlJkg_DiTOL6QV9bC5MvGv6G9vP1ePYixgnwDuLwaEZi8V8A802_dbIwwjoCq6LzRVJ5k9NAGieys9ThQiUQTK0QIp0BDlKw1UvxRfIy9P5a4dOp-3Z2r07Ly6_Qcerc-Do7O2llu98ieq4KerjX3sCc92lvzTfx49FIb_cV_EHs-ewHN-Sc6DHcsGvSEFeYkWglZczlzq9I6VJ21dILOWZ90TkNJf9fNn1MGIom42xJ8xqsFj0qPUKewFlxTSBKBnUDggySimw0vP_64rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30317" target="_blank">📅 00:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30316">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=Ipxc7Axij0-6_QX0MeUhoLJd_y1QO3cgcHVBI3wFVszRZp9PYrRkZsO1rlqSJ4Vqc-l353iDJM0_-LuYiHvoC2F2xQN_q1FSi_MrB9O7IntTzH5974HTGbrYa4sJHT4A0wJIVt-ys56b_MpJSLCCxIORcQ3UGTzWk-EIBRdF_AO6KHe27eSNlzgpAaXWhMOcKRdrHPmvFFr1CDZP_4jzf1WtrpxxkbNoQ0sQLknJruyI6yKEbrVTUOVNFm4hR0fgJn3n9xh65mW6mKENFA12QY-bxmaN7e4vnEs0TIL9aVEnymnqTxKpwMF0o9puFbC9m5Sih7u7beTLLLPho5-1yzSMW00svzc6UWaZdCkotNzvVZzbOqPBZJjy8KRwPUpXTT6awzX63lIPSnqXx2YsRgp6iQOHYqY_VA_CJkW1Dn3afbFW62IfCNG07AG-5T6VngIqsW2Fa04tSGKUKLs-nCzJFXNaQ8dLMvDzu_fD8LGK6cXpWkk8b0XB-kwKn4nMXt7NEgm2wKxmUSVir8n2ws1QVUjla_PTcyo-84Id_CXh2d0GygLNrXmJxiKlpv6gzZhQ9Z_fGxf48oCTqSEqcfMyL--xSkxUg_IVSA_X71zAeEpKL-vgCEU1fufGLEb_XVSC8Hd1cguT336yVDImNr0TL12Ib7usO2Ll7yCTD-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=Ipxc7Axij0-6_QX0MeUhoLJd_y1QO3cgcHVBI3wFVszRZp9PYrRkZsO1rlqSJ4Vqc-l353iDJM0_-LuYiHvoC2F2xQN_q1FSi_MrB9O7IntTzH5974HTGbrYa4sJHT4A0wJIVt-ys56b_MpJSLCCxIORcQ3UGTzWk-EIBRdF_AO6KHe27eSNlzgpAaXWhMOcKRdrHPmvFFr1CDZP_4jzf1WtrpxxkbNoQ0sQLknJruyI6yKEbrVTUOVNFm4hR0fgJn3n9xh65mW6mKENFA12QY-bxmaN7e4vnEs0TIL9aVEnymnqTxKpwMF0o9puFbC9m5Sih7u7beTLLLPho5-1yzSMW00svzc6UWaZdCkotNzvVZzbOqPBZJjy8KRwPUpXTT6awzX63lIPSnqXx2YsRgp6iQOHYqY_VA_CJkW1Dn3afbFW62IfCNG07AG-5T6VngIqsW2Fa04tSGKUKLs-nCzJFXNaQ8dLMvDzu_fD8LGK6cXpWkk8b0XB-kwKn4nMXt7NEgm2wKxmUSVir8n2ws1QVUjla_PTcyo-84Id_CXh2d0GygLNrXmJxiKlpv6gzZhQ9Z_fGxf48oCTqSEqcfMyL--xSkxUg_IVSA_X71zAeEpKL-vgCEU1fufGLEb_XVSC8Hd1cguT336yVDImNr0TL12Ib7usO2Ll7yCTD-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برای اولین بار در 47 سال اخیر، یک ژیمناستیک‌ کار زن ایرانی درمسابقات‌آسیایی شرکت کرد. هنگامه هادیانی؛ ایشون درمسابقات رتبه خوب 13 ام گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30316" target="_blank">📅 23:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6r-yJ0SycjgTGGrkxxGuIHkudevolCCX5mkZOKbV43A_tbYw-_IEpTJerfFrHwhRD2jZJ6OTIshIbFCCQihRodYwIDcnoFxTUmL90Ut0M-7sOALepHeCVcZJepqKHrXKqThHpRO0V0m5oXUr4K6AyDu-Z-C4BFfhZiIw26xQa9M2eZtd3n2za18P97JG_EYDuuEDGG4Jh-niXzn87E49XwMIE7jJJl7fqgRnTxxGIof5pQmKP-gFeaem0ZjEcUmsh4x5CpU-WNnW3p571uezsm4uBJ8VyJuuy3hy0yj_xem5ab5jCaV-MPmU7_tcTDYX99buhyt1I2iI2oPy3kf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
صحبت‌های کریس‌رونالدو کاپیتان پرتغالی النصر درباره زدن هزار گل زده در کل دوران فوتبالی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30315" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30314">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc5K0AY3rp-dcoB62k3T7S4mboZu_GSI50P52HSwCKY_i5I8mHEOyit8cM9D_7dDkxohD_FTgMr_bEQsfRr90M12sDZtHwaAOh6Xq0_qvKsDtvIx4b26UxzoUBu37BsERigpCiCSl-jTl9VVHItZ6xpQtCn62FBIKJs2LbzL58nO8nF3AyY-JdQh3liycucCCxi5gapP-M7EdztamFBjR1PSm3L38rqFWW8uod_7DRSLinq2ehWFJMRNVAD9I55617_RLEl8qrKyrxHYHf5diQnHReN3HxWjB9PoyPevLzcShyVJFZ4eaQusR46w0--evtRdkXCiHYx6aYwCJ-Uswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30314" target="_blank">📅 23:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp8rP-j-GedsPBUCafJB2zI3tanmbFR_3RpJXdTLb3kG5OjjT_g_8At4AFIxB0vYCldNgiI9EW2RB_KXTm0JQvEjK6yQbqiVURjbTIkdC4TDCtAs6mqMJ32X9eCnolsOekoM38iQ0DwwBe8WDMHIgSuOuZdhyU-o5vtJZHyDkDOGOg7QxMXG3NRWFrPIT2qLGHlK0NmowtaCUuHwBROGOJSG2mPJcf6_LXPITEtMkKF6ukMPuWz8bEIyAGO_WpFv-zFFrfbO1G67QoHxcVNlLmXTEFJytLTEBslYVCI-1kg6LsMxcUXhvZlPqAH3cDoVfyEbo-SJ_eB_mHiOPXIAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال: باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30312" target="_blank">📅 22:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd-UdvP62et8lZVQc0outzrqngnDZ7vD8WB9wwDpiErjT_ri-OU7iJIxXndR8FkviQFCD1u6MYIAPd2ta1_QuujBrIdqmLxS--Ju2yvYPLqU-LPYzISuLzH9qshMaKg4JBZkHzFSLkPghR1GpK6Ugl-X_WV2KDH4j_qbHOWJcuOmtzVUFX6Jy2aa4LX__BZ9Fz5wiCHt5YhJS_ZvDs6wS5NNTed1jg9DU3oouFvTusEZDSE1xYqJjo_syGP5uNHOgRmCBFAMKZmyExASwggFd81uKcmQjVMGd6_mW5neRBcCsHjlNLvscE0H0QOKPSY5uvRGwubbGJmdbnba_U_vGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30311" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=DxtxTc_tWTsCLx9HYCaWHXjxUtEodG25KRyWRYSFKZdotYBbkYYW2w1hUUdylnRuiSxXVYAtPfFHthE2omAWz5xazt4FaKjJDDDoSwkRD6Qv1M272_S68RsipSyT3xsuWnqRcL2MhiMD8KNwhW4G7MYNEVxL2D4xCwmChjlihA4IJvthuXfTWyLoVdbhLwo0PQmsPxzoRmzST-2f5opr588vlIjOaahtVATFl4YwX8nh-XYkQ_Lmx_sTdmMMXUrgidApWlZ7eZKS0vF0SbI0wGU1TftAvLJ__WylLWJSjl9g2oHwDRpGEcD12gAE55AFqH9c1kP6n2kD84PzrS3zoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=DxtxTc_tWTsCLx9HYCaWHXjxUtEodG25KRyWRYSFKZdotYBbkYYW2w1hUUdylnRuiSxXVYAtPfFHthE2omAWz5xazt4FaKjJDDDoSwkRD6Qv1M272_S68RsipSyT3xsuWnqRcL2MhiMD8KNwhW4G7MYNEVxL2D4xCwmChjlihA4IJvthuXfTWyLoVdbhLwo0PQmsPxzoRmzST-2f5opr588vlIjOaahtVATFl4YwX8nh-XYkQ_Lmx_sTdmMMXUrgidApWlZ7eZKS0vF0SbI0wGU1TftAvLJ__WylLWJSjl9g2oHwDRpGEcD12gAE55AFqH9c1kP6n2kD84PzrS3zoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های خسرو حیدری کاپیتان‌سابق تیم ملی و باشگاه استقلال درباره حضورش در سریال پژمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30310" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30308">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4uh_g8H8cBRG-ZanQ9D8D6PvgInwBQR-kSsV-hU0SDCYddZmrnagrJ4dF-NhNgVj3J4GVufP0cK2h_ZhKk98BKMqMMdYG60Bu4xOiTrk2ibdXlUaYV9EotW-Nto9Xf9tjtP1rA8DvDWGxQYkUphHx91KfB5I-6WJwt7JZc0In0yx5FlJOvrjDETgKS922Y-PbM1dcFMjHucQ1t3-s9DqhpKgGW0_O-pcSveg-1dFraeT-1daSkaFQDkX7BF7OHRXOqKgJkcfnzkhh6QqttTz9U-MFuB9N0YoY5xYxrOMJiQAOLD4nq9fhkD8FTmS7ClcDo2SL00aeQFpFEt-GkL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرامریک‌اوبامیانگ‌مهاجم37ساله‌لاکرونیا امشب به‌این‌ شکل گل پنجم خود را در فصل جدید لالیگا به ثمر رساند. انگیزه‌وچارچوب شناسی‌اش‌خیلی قویه. این 414 ام گل کل دوران حرفه‌ای اوبامیانگ یود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30308" target="_blank">📅 21:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30307">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=albdQXrahwrpO6baxXkBwhXfP0Mp8QCGxhM4EKsMg1_CRYUWzTacvj1UYOnb58N3qFF2K-Lj816NQ6AetAgSmluPisIjCggV1zLPR1bGtPrt5MS99gggSaHDTnT8DdsLg8YOBt9gAG3FAnhF7iBohp7AFtDnk6D-nd9eZ7vHQ7k1wnBrVjlROMQWpxY1H1V5bY9eBGoh6RAsJWbih4mmshEYXIsonAh0ShXitAnGGRsbxuwLwADf_nAMn80Q1JEyk1v4HCQG9DzhD0S_O5Al8v-28rnwWVJ-q0TtL8jMy48hYy2thuBHWdtnW0NJHaKemPScV9ey744PSB_qXsLY9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=albdQXrahwrpO6baxXkBwhXfP0Mp8QCGxhM4EKsMg1_CRYUWzTacvj1UYOnb58N3qFF2K-Lj816NQ6AetAgSmluPisIjCggV1zLPR1bGtPrt5MS99gggSaHDTnT8DdsLg8YOBt9gAG3FAnhF7iBohp7AFtDnk6D-nd9eZ7vHQ7k1wnBrVjlROMQWpxY1H1V5bY9eBGoh6RAsJWbih4mmshEYXIsonAh0ShXitAnGGRsbxuwLwADf_nAMn80Q1JEyk1v4HCQG9DzhD0S_O5Al8v-28rnwWVJ-q0TtL8jMy48hYy2thuBHWdtnW0NJHaKemPScV9ey744PSB_qXsLY9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس رونالدو: ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30307" target="_blank">📅 21:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30306">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDfaai-l-6Z4M7l9lROu7FqAKIMlAyDIaoxt9jUcBDupfDOFDImyJ-9hgIP9bprqBbLNH5w9VEWKc7f596FWyQHww30qXjzV0tN5u6ZWuiID-JYwQ240QBotshVV0apM_qr9nCvRyDDqHtaEMplLlu_LrexKR_6RaWymqezztKvoHFr0G9qKqght8Pkebz_hjI0W16lZACKS0Vvr6f_HXRuizaYNKeoh6HQ86UjKuQebKwmaAJ45KAhPQNZ_n21c52cH_5MoUh0tMXird7D1O5Mvd19D4t-PeyvcRZs2svsYApn4jRBeyoYtHO_BG-5wNd2xux5ym9yB_VYGzTLzDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بهترین شروع مهاجمان بارسا در تاریخ؛ رافینیا با ثبت ۱۴ گل و ۳ پاس‌گل مجموع ۱۷ مشارکت در گل درفصل ۲۰۲۶ یکی‌ازخفن‌ترین شروع‌های تاریخ بارسا روبه نام خود ثبت کرده و مستقیماً پشت سر شاهکار لئو مسی در فصل ۲۰۱۱ با ۱۸ مشارکت ایستاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30306" target="_blank">📅 21:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30305">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuMa4c0SziMzVg7yCX8eK5sqDzlKaMHlU9YWCTzVAR4btTU7g4dVeoA__ywvqRl51Hw24vaD4kWKTMZLJ0QcuaB1un_v46wZr5aAaOG846EVpLqZotBfAC_HMlzNq4TTA_HKbnZRfZuC2zJhNAN8EpEP7tTFuAHu-WlIW7GWFiGGr3w3TDIJyyC2ifmSqoodAXjMSindDLNve7aXzcYL6p6wz4rAnxpyLlR3TpwP9rjRzcS0bMhyW_tTs1sWZinODpHCVig4EXBQWiidJmwkM2-G6gaZFXa7kUXqhGdLZyKhGFumd1E_IZeXyTRVLbhUu9wpqLVKYYPnCEWHr8bnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو:
ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30305" target="_blank">📅 20:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30304">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
موزیک‌ویدیوجدید ابوطالب حسینی با بیت کاگان منتشر شد. خیلی‌خوب‌میخونه لامصب حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30304" target="_blank">📅 20:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30303">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=k8L2Rip1Z0kbV_n8AvUPquz-nobmJV-13Iubcxw5LaTfLLKGHgQ3EuuauOhuz2vHVCgyxn3UwZSmIHLyCuT6E_fOJWZs6rkvekM0czIbwJmZjTJOnqGBaUcBgaX1cG5VMvdHl85ncViayH2xGDdlDtKQugE-p4uvmGZ3Q_2QAP9rrY9gAj7m3ORRdL8OL_eEsZiS5BlLqRsv1WN-s8s4p3t0PmtkZaeyoqvIx6VC2tvCVnJ-Rmh96OG537SdFiX56i3zlPnwmkoDv85btrbD_2dPOMGxxS5L3FUXRDDMPqXsOkHYLA8eAQlYQlIxJP2capknoX0rSYs9ZMyPQZRbLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=k8L2Rip1Z0kbV_n8AvUPquz-nobmJV-13Iubcxw5LaTfLLKGHgQ3EuuauOhuz2vHVCgyxn3UwZSmIHLyCuT6E_fOJWZs6rkvekM0czIbwJmZjTJOnqGBaUcBgaX1cG5VMvdHl85ncViayH2xGDdlDtKQugE-p4uvmGZ3Q_2QAP9rrY9gAj7m3ORRdL8OL_eEsZiS5BlLqRsv1WN-s8s4p3t0PmtkZaeyoqvIx6VC2tvCVnJ-Rmh96OG537SdFiX56i3zlPnwmkoDv85btrbD_2dPOMGxxS5L3FUXRDDMPqXsOkHYLA8eAQlYQlIxJP2capknoX0rSYs9ZMyPQZRbLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30303" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30302">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=pEw81mwa4txh4wIanOY7OPtPKJ9x0hBiyuKf85ourmp0Wg2Pf4iz2ff2QCAD4Qy6cNE2Dl1uFdXEhm-CpdM4UBfX-V73ZFrVKEas_taiIkBID5eTi65t-TNyu5DPuRWfgLH_UPIPbB2d3OZVhmNVfx98MQ2Vo_-NtynwmhJrzo0Sesu8DRSHrun1l-KdcTZgotYj5UBX5RTXzJI9BzekSZW0ELkWjNXLiRxNxLsVokVgnQZZBGL2kf3hHW-d9ZhkXn-fT5pnURd6c9hOX2gWC3f7PPuueGjs6IHd7AIkAndXVLS7Xrk78N3O1KtXvyVlfw0D_GWojJZ40rhgiSevLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=pEw81mwa4txh4wIanOY7OPtPKJ9x0hBiyuKf85ourmp0Wg2Pf4iz2ff2QCAD4Qy6cNE2Dl1uFdXEhm-CpdM4UBfX-V73ZFrVKEas_taiIkBID5eTi65t-TNyu5DPuRWfgLH_UPIPbB2d3OZVhmNVfx98MQ2Vo_-NtynwmhJrzo0Sesu8DRSHrun1l-KdcTZgotYj5UBX5RTXzJI9BzekSZW0ELkWjNXLiRxNxLsVokVgnQZZBGL2kf3hHW-d9ZhkXn-fT5pnURd6c9hOX2gWC3f7PPuueGjs6IHd7AIkAndXVLS7Xrk78N3O1KtXvyVlfw0D_GWojJZ40rhgiSevLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره مهدی مهدوی کیا از قرارداد یک میلیون پوندی اش با تاتنهام که بخاطر سربازی او لغو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30302" target="_blank">📅 20:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30301">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=IDlpA9hUxk0tvs9JtjHVJd38IjKmSaYzgqgL6ybWYBz0oz6s1pCcn6pvOFKTIpwrywtru3cYeAehBqefsc5lV_U7tC0HRbp6Q6LCDZ2z18ZC4G4FnxUrkOhTs5A3ZrxnuXtR21_Yyx2UnPkCtN_UXq-rYFS5mY7ODb9SJB2qNGUQIQIWT8jh_u0hfOzR3VgMWNfmvBS8Q7cB_Kw6VApK6_PQtcSx695e1h2oceTlax4J-G_jvP3roedbx1dJi8oo1zgZpwpsTZgXgttlK6B6n-g_MbVmKjBOFe4_19xSp0W_vy-PCN40KwdnA75qZQIUMxSh8hSmWmuqkG9sKYeZjr-YHeVhWm5dzLDUlOtriU1nxFcw9_z6ub8xHBp8osZBVE3hn-e-d6enoYtMxmjRwofiDv5ulD7V-n0fmY8amL2nzi8cOtCXxaWkJtt8m51Fdz5ONznBLjWKUV6gmII4QykmbP24dFTp-YbG3VLBdxi1mZEEVJb0cEV-UqWAlseHasA89eqC6BK-5jGGfpIOKyGoPW6siR-IxG1Fbpu2E-SiNwaIwULd4XKNrKquvE93rgmZJUXUh8tElK7Co_kSJagpolZfYNlz4buzMuMNmtDs8GzSO1gWVFym39kUvNrtxjHMsIwzdj98ZYvMeXPFmQFU5QaOs8ybb57GzBa_M_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=IDlpA9hUxk0tvs9JtjHVJd38IjKmSaYzgqgL6ybWYBz0oz6s1pCcn6pvOFKTIpwrywtru3cYeAehBqefsc5lV_U7tC0HRbp6Q6LCDZ2z18ZC4G4FnxUrkOhTs5A3ZrxnuXtR21_Yyx2UnPkCtN_UXq-rYFS5mY7ODb9SJB2qNGUQIQIWT8jh_u0hfOzR3VgMWNfmvBS8Q7cB_Kw6VApK6_PQtcSx695e1h2oceTlax4J-G_jvP3roedbx1dJi8oo1zgZpwpsTZgXgttlK6B6n-g_MbVmKjBOFe4_19xSp0W_vy-PCN40KwdnA75qZQIUMxSh8hSmWmuqkG9sKYeZjr-YHeVhWm5dzLDUlOtriU1nxFcw9_z6ub8xHBp8osZBVE3hn-e-d6enoYtMxmjRwofiDv5ulD7V-n0fmY8amL2nzi8cOtCXxaWkJtt8m51Fdz5ONznBLjWKUV6gmII4QykmbP24dFTp-YbG3VLBdxi1mZEEVJb0cEV-UqWAlseHasA89eqC6BK-5jGGfpIOKyGoPW6siR-IxG1Fbpu2E-SiNwaIwULd4XKNrKquvE93rgmZJUXUh8tElK7Co_kSJagpolZfYNlz4buzMuMNmtDs8GzSO1gWVFym39kUvNrtxjHMsIwzdj98ZYvMeXPFmQFU5QaOs8ybb57GzBa_M_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنالیز دیدار هفته‌قبل دوتیم اتلتیکومادرید و رئال مادرید؛ ژوزه مورینیو به‌این‌شکل‌بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30301" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30300">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErYLt2pdHgcr4Ft9Pd3ZrTKwqiWiX0QE0J4CugWAOU5Dkylupb4iWCNyyJCttSEQyCTOkofJpP6flT5zTz-Ffq2JdSvhq250TN7LVE0rbBtTGRm6Wz7MeDE1PJ6Rlpm3SKWve8_23kbl4qNuF_TADhzKhvWVp0GtKW3IavbFMiPWaWYEWu-TaJd_2_wlcZxzldv6IzP9lCjJ6tMoA6X2SiO9wZjj2sWlAT0GT-qULSOASYyCCOg013URhk-ZE4BJ04Uv_LfB3xoYxavviHNEcHRXQzLbwtf5PPfPYUSbp-emhrbT6O1GarWk158j1TdNT1wH4S8AV6_oxzy24vGhXeVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErYLt2pdHgcr4Ft9Pd3ZrTKwqiWiX0QE0J4CugWAOU5Dkylupb4iWCNyyJCttSEQyCTOkofJpP6flT5zTz-Ffq2JdSvhq250TN7LVE0rbBtTGRm6Wz7MeDE1PJ6Rlpm3SKWve8_23kbl4qNuF_TADhzKhvWVp0GtKW3IavbFMiPWaWYEWu-TaJd_2_wlcZxzldv6IzP9lCjJ6tMoA6X2SiO9wZjj2sWlAT0GT-qULSOASYyCCOg013URhk-ZE4BJ04Uv_LfB3xoYxavviHNEcHRXQzLbwtf5PPfPYUSbp-emhrbT6O1GarWk158j1TdNT1wH4S8AV6_oxzy24vGhXeVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 88 روز از این‌ویدیو تاریخی از خوشحالی مجریان شبکه دو روی آنتن زنده صداوسیما گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30300" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30298">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qshsqlELeuMpS3IyOJNepiBV1I_N9l_CFQvUVdBW6wTUncZpPm2y1K8Oym2i1Y71-mudqczs6aqL2yiXQOqalvdrk0SndQr92PD2Qnx3KbjerBY6QBLeQD1KiowHDYTA_oTit_OsiVnX1Hu8jPT64VmzswPHSF91W2AkHdIYB_9ETnRDpiukx0-xGK2QRjnumnkj8aTEHEau1LtYcVK2oY5waf5HIfYk5hCF2c7sC50jWIdvqThjntd7Cbw4ulVTxXmIKNWL1R-KLw0W9aJEuDKH8LEpbjZ8S3tqow0BjRzcBlPbp-hyuoyOnN_07CjUGR_n02n1Al1nAERGrBB8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادگل‌های کریس رونالدو و لیونل مسی قبل از جام جهانی 2026 با بعد از این جام تا به این لحظه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30298" target="_blank">📅 19:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30297">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pp4p1TZAlTOWiHAYf3vPKu49BXlQ3Dc9Gjs96DTMx9X29utZXJ0YYLPqWM-BfsZQHINDqbnVGDtgYKq2deWMvveTA4mtQvFpHqgoVHBSZb2dOGS_InNd6iiXcuLdQJF5SEivXfiP3KIe4ObtKfkYXqEXhPHU_2dkzHJYHtgchmEfw98R5ntiR2jG0IEJFu-TEithM0LR4kOzwGYvnqOnD43FRpCS8wCLzXQ4X7dcmqEjgVT3zg1QDlnOPsDzqbWLJPtNPNgYlUf-53_56nFDXT0VufInNh9rPUbrcnUP6EerEn2h_sxyaEFHj5LATMIqZ0Wu1Hi836CRekhyVukcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30297" target="_blank">📅 19:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30296">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kofr618pGY1AX1JzWvE93NX3zZQuYxy2JN6A9MN-jTKPgKjmcFJ6i5FStYx_czBh-7rl7wqqiU3reosgzeMZW5uSHplcd26FrjtV6c8ww7YWNXlT38l3ebzRwF2QOp_HFR6H00sy4ZVq55j9oBTI-AS5EeMzIOzXs1Jey35bvLb5mwZSD-lp5GNG3d9jcmoFjTIPcjaXY4-u0CcHy0jYqSYGzLnwWVU-hSGBaSkCktsFIvN8gkh_w-cI1-TwfH4SFveVkdLDlRqzHeV2O9ekAbBa7GR-cRH_Vei_ud5Fp5quN6I8uS44iXltHWtu8VHUngWoyVaLNlffiz6Oni7Cgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30296" target="_blank">📅 18:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30295">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnXGZumr2rM58Zt6n93KqjRBOwZf7MSN1ZZKASU_7--4UfQ6lnvr7vYmhds35d9qE22uyAwcw9WoCX-GdswnvNankCOFBdurjLl4ZScdCD57blIs_NF6je799N3zsDWaJ4zV1d7_n8aUGC_uQF0qsxvsTKEyHS8QXhdABTA1KSr_ASEMyubEY3UK2KxxIXCiEqaexgTYwHQC4JHv4dt1C3wQ_s4mGM_WGwCYoTKD3ApjTieCD6na3ywOXB3y5D3s6ZQCcoqW1FbdIWaNIYDEAqEUQSUUu2BiAKM1Pi-ATT2UXpsRWCGBcM94wnfpCHAhh3N4tGQdOiJnkL7q5gs2MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30295" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30294">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=j7r4Ju0OqgJHIPVCsBBN_nPTZP7bTXiKiM_VCvgoDVc8oS4rJyrpUlsD8L5_r0EA1KIhD6Q-X9lXMqJuuRry4jadXcS0cLwoWj_ydjdZQReXlTP2swKPtEGrqNIsK0KZRGVNG5CcIr0abYa6Lsl7_paZEMuBTtZesNMgf-BorrJIfPLmuNkFvtgmvRIIdIYBjIHqFyUQMNklgiBu1GHYD-tawHHKTMPfdwrx3AlW6J9HtAveYgtfw5pg9hTU7VntsSv7Q6KUubRwETdEQkJod0KjmZpWs7IveetXKzD58_ebCR348U6gO7B_GStFxUJArjdZHc-58rcbvOP5TbPaqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=j7r4Ju0OqgJHIPVCsBBN_nPTZP7bTXiKiM_VCvgoDVc8oS4rJyrpUlsD8L5_r0EA1KIhD6Q-X9lXMqJuuRry4jadXcS0cLwoWj_ydjdZQReXlTP2swKPtEGrqNIsK0KZRGVNG5CcIr0abYa6Lsl7_paZEMuBTtZesNMgf-BorrJIfPLmuNkFvtgmvRIIdIYBjIHqFyUQMNklgiBu1GHYD-tawHHKTMPfdwrx3AlW6J9HtAveYgtfw5pg9hTU7VntsSv7Q6KUubRwETdEQkJod0KjmZpWs7IveetXKzD58_ebCR348U6gO7B_GStFxUJArjdZHc-58rcbvOP5TbPaqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛
خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30294" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30293">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=jP9iaMq3uVonlYNISgHviAaJD_LStnHpiZh2H8cM5c_kbCziX0pyam9NcapaIBSmabNnS6F-xvWIT4OCoRCQtuXcV5s2BRKfTbIWKoWpsqM_qP3F7jW8ky5M-MItXPPjHV8eF8VwmsjgvgE-oiY2RRVNDw-w2uJFI1U_7EDkZTzRAqCLiHFThlsckxYR4fdUz0nxMpqwbobQY2yRUWMP7J9v-P7IQ6K8auWlZq95hFrAE3x8WQTArH1V8oo7laSlyRiALXafRqARwUZxIkRhc28aOxW9NtrLoSx3g1lBJFFXFyx_luarY7QGpl8bzaWeO764-EXgPbeAwn9gs5fvsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=jP9iaMq3uVonlYNISgHviAaJD_LStnHpiZh2H8cM5c_kbCziX0pyam9NcapaIBSmabNnS6F-xvWIT4OCoRCQtuXcV5s2BRKfTbIWKoWpsqM_qP3F7jW8ky5M-MItXPPjHV8eF8VwmsjgvgE-oiY2RRVNDw-w2uJFI1U_7EDkZTzRAqCLiHFThlsckxYR4fdUz0nxMpqwbobQY2yRUWMP7J9v-P7IQ6K8auWlZq95hFrAE3x8WQTArH1V8oo7laSlyRiALXafRqARwUZxIkRhc28aOxW9NtrLoSx3g1lBJFFXFyx_luarY7QGpl8bzaWeO764-EXgPbeAwn9gs5fvsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 3.5 سال از این‌گفتگوی تاریخی علی فتح الله زاده با محمدحسین میثاقی روآنتن زنده گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30293" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30292">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBmDwIh1qQ6idn2Dw9kHHQ8pGuiaL1so_YXp6yr6QfQDtoxQt73SgYdIoRMGUBRiGnytMeAbiwVxLL43JLzYOvL9fwVWZvQxsH43_LpFCE40zhkFxmfzMD56SkQrXvdJOZiOSDvaVzzGihvDBN-b7NhFHBlTd29yF3Tz_TugRsvoEaH6cq3a7ePObHvah8zgOftvlwMQ4fSIM87fDz9kz9QrGpxoEXCLO8ehNf7JVrRT7IcfanfIfYRWIxNCrjXWEI7SbUKX4NFztbYlAs1sxrHrSuB8N98NBSorkroSDX8vd0OpPT73Onr0YFuJryACqnd7E8bVUsenKOYLGOqAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی، ستاره‌ی پاریس، با رد اتهام تجاوز، مدعی است که این پرونده یک سناریوی ساختگی و ارتباط آنها فقط در حد بوسیدن بوده‌ است. در حالی که شاکی بر ادعای خود پافشاری می‌کند، وکلای حکیمی می‌گویند امتناع او از انجام تست DNA و بررسی گوشی، نشان‌دهنده‌ی دروغین…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30292" target="_blank">📅 16:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30291">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxEDvVbf1v6IEvrB2kJSuMsIYNWYdmiU71OkBkTgG3DCTjrCTKOOU3hhINE1xGZefh1Q74KzSOOFECIB6J_v_9B8ak4W8bvd9x6lR_MrvvKVX4QMtvva5V3GipPNyp_hUQljQ0BJ70517NpfULu0Xp_bRGsZroU0tdMZ5Eggw6e6hTl7BTH6BEthWbjNZMsMISYEeG6aHVjL1GSp5sitNfIfBxU9p6n55TKfpK7asZX30eneImTh1u4_DIaWjAF6Ktu-O5FjAY-FVRzIcNCNiyyChHWFoTcCgD8dkTfrm1YjjeJlsLGloeOg8mH1G0Vzi1KRBt18VKenSrWX-YL5hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30291" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30290">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ql9CmfSISZiRiS_Zw5s46LgGqf6Z_URZjMOAd3TQ2dNzHwyu-Em18riHOiGCnCWpip_jEYfBQQc_yiFONxXaIInFyl_cV7c9Um3piUw9JoTpeexld7EnsSQlEVPV0LZpCXQXZhMTjkRml3TCitWE3prwM3mhxbIBCxBNzCJDpd4ikn882CekMCPdLgPTUd57YBILUqIAiAaOiYbfKLsdbdk1ntw5Ws_XEdF6vSA_TgG1MRO6a7XCaRjoq94cJEnPVOb6IOoekWUAYEbMY6cxFVpkkkNhQvFN-MkP4C_n98a4qw2UZyMjcbD-xjqyEXKTpD20-oepo0fSZBDABgp1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ظرف24ساعت‌آتی رستم‌آشورماتف، جلال الدین ماشاریپوف و یاسر آسانی 3 بازیکن خارجی استقلال برای حضور در تمرینات آبی‌ها و دیدار حساس مقابل تیم تراکتور در هفته هشتم وارد ایران خواهند شد.
🔴
اوستون‌اورونوف و مارکوباکیچ دوبازیکن خارجی تیم پرسپولیس نیز تا پایان هفته وارد تهران میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30290" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-UFjE74rQTQD3gAzVw6AqqvjBaLzZAwklOTIpM6LI6Aq9pr90K2v4pxl8KHpk5JMQPbOnZ-0_bXpKihWZVJ_Y0R-RryyoL_1MEwtuxbAvcdSqCLRK6UKPTjH8BoLaqNgpTtpFWsXfdHmEbZUoU-TCYjxvDJ1DSm87DXMLviWBCm9V-DFOl5ZN3K0Cn1NvaA-y2aTOdA6pqZw4uUaKHUpZdjRrRYK5qMhuFKaqRJ3JtZKXB5WEXUfYnsvTndICx_Hi8OiugRlO8J8xr6lc4UAXyrCWHUSF-RqgVEaAPg_JNsDfCYYamzEVbkNz_Jh1iPbXHnifAhiADD4CJNUKKh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تیم پلی استیشن ایران در فینال بازی‌های آسیایی مالزی رو دو بر یک شکست داد و قهرمان شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30289" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6xeP5chuqBFD6kvoPxpWCC4SmbRXe5Xz8imWPSKypwxA7SwaDRpLetLrAxvTRdcoek695k9t-HJXALwf7X1a2JhvKpzgIES_Y96GkoicId4J6rqhORkcj7gNOQtrU_-z0lio-_T4of2ANoDZvqZuCrhg6xLDm6FQQwm03Tw_ufB5b4lFXkr6MZs1xvj9_0xAdAP3qkAK3TeDIA5uZOFs6xzxuiZIVwzAQmgooJKFoIuCLYdni-KsFVnqs2pDqsdkIhxvXecLEbcpjGknHlIjZ8GaEb-JmfuqbSq6jTBqwyGGKLS-XO9pb-9hwSxntvMJSy07lmsxWFmTVPFWss98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه.تعدادگل‌های‌کریس‌رونالدو با مجموع گل‌ های رافینیا،امباپه و هالند درکل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30288" target="_blank">📅 14:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PK4UBzP_xKyHnpMhvMtQLArGNOPHRY800jdhRe6WhXexKmAGXVyTbSpnBQK3MOxDiJGBHhVXK1G1ZVDK24CQP0Ox7OUWZv2HVbB6HaeVmmahMttM2TJx8lQFhziD_V1UihosDOopcvz63vJ2liKV-gdLvaRcZ5_BpOCkQ6ouCr9e_iQaXUp1vz8w9TFn3qg5sUpt9gqbE9CXJXIbcW72WNj0qbNL9bCwB_UlIcSm9qq7OgLnMSAXw7GeCcdVzTKeSOkosnHfRGLNYc9Kmlg6qZ6BfsBqaF6dUSR00Jiis2si3BoeGPZifmX-gwxsgFvdhBgQT-dnF6528-yGkAlGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛ لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30287" target="_blank">📅 14:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30286">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTRXSli2PniUJm0Y5pGFUnhxC8Wgz8CS0HsOnxVpWRQWuvoTRtunkpCZXQ--T59T1RVIdRYkO3FluDE_QnzBta15uMCOQ9hUnZYESUv7tPw4Nx-LYBchTw53sfzPXSlf_Ql3fDVDp4WI0HrIZtaZBnb9yrlkPko0HYgExpMOgNQ8dppyiPhIRk5-mGo6OM2XP2DNFHw7Sgc1eXDuIsNzywfUNoOP7LpUnLlo-T5x1EG3ViuAVhso_rKdd6nW4YhtizD63_-RdW3G-uiKg5r0nShop6IOuJ7D0esrFTBeZMburPuZcyt8OLyBg0i4wgCgeNa7Osh_yfA3fRDum2_mxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30286" target="_blank">📅 14:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30285">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXocrBee_fhFSEk8AzdxHY4oafNyMHsMc0vrApKwt4hvkOMK_-iY9hjodmi9Dt8Kx484ygEsldNYxxWLMWbRh8CEwFvbMnfo6Vr90zc2cGydjDLXm5hXHSqdoevybSPDBlX0wxRlbb4PZgJ7nij8-Lq6kaDTbjZxQAC2AVgHxT7Jl2cAXcbLxZSSNtiLB3zEumYBqXAjFUyb_II7-34PphkqGI_2VADPjOEfoCYfr4yaaR1dTrjwWNuixQaeW9eZ0NTmhOfr0JF5gCX17u4phN1KNLoXPrgNikGQLNAREBFy1NF_mXE-gvA-nqFV3-X0rxAgdv86ht_l1pxSavgUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇳🇱
تیجانی ریندرز ستاره هلندی تیم القادسیه:
نمیخوام وقتی فوتبالم تموم بشه باز کار کنم به همین خاطر تصمیم گرفتم به عربستان بیایم در کنار کیفیت بالای لیگ این کشور آن‌ ها دستمزد بسیار بالایی رو به من دادند که زندگی خودم و کل خانواده ام رو تا آخر عمر تامین میکنه و نوه‌هام بی دغدغه میتونند بهترین زندگی داشته باشند. یک‌سوم‌رقمی که باشگاه محترم القادسیه به من پرداخت میکنه هیچ باشگاه اروپایی پرداخت نمیکنه. از انتخابم بسیار خوشحال هستم و میخواهم سال‌ها در لیگ حرفه‌ای عربستان باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30285" target="_blank">📅 14:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30284">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1454042688.mp4?token=DM-Nm5nFnZJTvca5E3FoYBWLqPmxZWz9u69q_p13bbJPWMFutGS9RraZ0v9Yo0VRwls6XwMKbDwUDVvFnmWvhQEH6tpwV4FaMYl1VgvQkMBGIy4VpQRGzOLMksECkWW2iwAHY7FRAGpwa8hvRSHRAqsvlFrHnq65G2lgngE4PK_l2OZe7bUxQL-tE3Q1bliZZbFSmaCd1ToI7B6CiizkLFaTLPDoGI5lJQOBjk9CTBFop5uN5U_GWeLXZVjf_Qy3zbrIloH7jUvbgT1Ia46ClK8bNC3Yfn4_-Rcc77hY5Yyot-mFC0wssxue3ugQ-TUJadtiQKaxwWq9iibqwa9ngg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1454042688.mp4?token=DM-Nm5nFnZJTvca5E3FoYBWLqPmxZWz9u69q_p13bbJPWMFutGS9RraZ0v9Yo0VRwls6XwMKbDwUDVvFnmWvhQEH6tpwV4FaMYl1VgvQkMBGIy4VpQRGzOLMksECkWW2iwAHY7FRAGpwa8hvRSHRAqsvlFrHnq65G2lgngE4PK_l2OZe7bUxQL-tE3Q1bliZZbFSmaCd1ToI7B6CiizkLFaTLPDoGI5lJQOBjk9CTBFop5uN5U_GWeLXZVjf_Qy3zbrIloH7jUvbgT1Ia46ClK8bNC3Yfn4_-Rcc77hY5Yyot-mFC0wssxue3ugQ-TUJadtiQKaxwWq9iibqwa9ngg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنایه‌گزارشگر به قلعه‌نویی و حسین عبدی بعد از شکست مفتضحانه مقابل کره شمالی در بازی امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30284" target="_blank">📅 13:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30283">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30283" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30282">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=ND31SQxy9o8m5hT4K24npppDTL66tBrPjLhwIVI_v6jP24NSaeEhrSYBYJt38yiOxN10wL5tLii2AQfLq2PsT3u5h9H4J5onQCTGtXuEl98MFg7dqDEXocLMZUVRuH_rVHWcBZ_hy2JB3m4bfT9LVqiAGxp686gucvPvhYQOiWqPnqCHy5rZGRg_2f8aORHMA4TYeF2p2h2wwNrqKnaGa_p_GjKjZSm-ZqFZgvwZ8cVZB0y8CbFHxGbDPcucONSU781-eWtDWIY3DYEbuxH5HuhXHQfEZ9SUbYOJUrWa8-bLYUY_PVjHSiov8jkYaBIepJdy-CfEC5vGWmUGd6c9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=ND31SQxy9o8m5hT4K24npppDTL66tBrPjLhwIVI_v6jP24NSaeEhrSYBYJt38yiOxN10wL5tLii2AQfLq2PsT3u5h9H4J5onQCTGtXuEl98MFg7dqDEXocLMZUVRuH_rVHWcBZ_hy2JB3m4bfT9LVqiAGxp686gucvPvhYQOiWqPnqCHy5rZGRg_2f8aORHMA4TYeF2p2h2wwNrqKnaGa_p_GjKjZSm-ZqFZgvwZ8cVZB0y8CbFHxGbDPcucONSU781-eWtDWIY3DYEbuxH5HuhXHQfEZ9SUbYOJUrWa8-bLYUY_PVjHSiov8jkYaBIepJdy-CfEC5vGWmUGd6c9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانی بیخیال هوش مصنوعی نیست؛
این چه سمیه که از مریم‌امیرجلالی و حمیدلولایی ساختین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30282" target="_blank">📅 13:08 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
