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
<img src="https://cdn4.telesco.pe/file/nbbBaaOK-_Xcv8Fwpww0mLzgRB8IVc7fE-SLb-TwzHtdOh-G_vxkmb0Gqe5A2UEzUXc7dKONVJ_WpudzduCChle0oMQXEIYlmUr2Zzu8Qh8Tr9AzD8bJwfkLBnnWaNh45goOb_sQS1JWhY1LMs8-cONHZD1objzBvr95vz4drhLifCZrw9SDsH3R5zx0LbfeNt2WdBNB4u7ct0U6RWQNLBQDm2joimOS3nkK87CSW0oeCpddZd9F8ItsztI7qzvn37EHp6pLsKC73Vc1N0bigSa6mezxVIilic4N7pZm_m7CMeaT94GvFhhyAmdA36ENUlvminILR7SnltU7vs212w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 175K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 17:57:44</div>
<hr>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAo6dBuR26LzYtVao7vZ58w8yzPFVNOZ-Kdk7OfeuUd5R9KrZXgZnTB2hjJQiX1S95BjH44g4-fbbj8ZxAWZdeV5jvZRkiOTnfcFSX3MopbcM_Bqe0t5Uav6aYsFsaMPEJPYyKynGgsBURS0WOttkntC9Md_h1d62-PmURuwv_SCgpwPF9IctKuF-Xoq183sJvlc-nfVxC4Tc9HAcompRc6F5lH3g3hdppPDRiqz4qa9X43VpVhxNANMWQBmFDJUuFsSfIkD6_PsJZcFGskCfoyfYCNWpfRQnU4aKpqX4TWbQZkEbYsAH3TTNhxS9lJiPaeVmXll8WigwaBBLD0avA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هفته اول بازی های تیم ملی توی لیگ ملت های والیبال
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/funhiphop/76903" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry1XI0YKVHrfysBFTiGMCIbd1vIULvVvNRhUPXN4LfaD5MZFoTk1xp5VsBZ-Zt60mlZwqJyQP1NdHZkit7tTi5s3tUTZpU8AIEN3NCpVbFB_AW757wXYeZ7_jjuNSKMNa-jc4fxlzgcikxZQr2OS0S8ArShGiTNwnDKiZeIig2hk7C3v46K7whPYgQsf8pzgFTMHaLMvrJqumvlkkMN1WgmLc4c2rQGlEbXEqMy1HFn3ZoqSBaG7A8xPaKCeCbXV1fmASKNr5ye3XRPIpyXbr8miH-z062exYioUv9-5SJesD9KDGMRvFa-AP8y0D--FB_bvLf6buNm8mKLFnNTU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام رونالدو فن یادته سر این بازی چقد مسی رو مسخره کردی؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/funhiphop/76902" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/76901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/funhiphop/76901" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76900">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGv2dg5t81dVk4MeeTc6sSO5VqQs0gb0GNVqk_lMx0g28j8GFfxNjq98Iv__E3XDdeoDaF-8FJ10ec0sb9VwpJm8zWYb8knersR8cRHy2B6c7ONimpZptjN5GuUaF8vjmv_n-Rx8zKbr5Nv0aXtlgpih_dl7y_osG2MS1Kbff7CuGdsgk6aVZlVvprSDkFTrRnmGdmhda_fHOeqR2Ydul340Ap61T1xVxfdj1SklqK6ZGSqf7UnuzaPL2ublW4vK1Qsl5cMSDQa0jDOURF0cli2Fd61-b4w8lwUiM635aLixpGa4UcT03CcKoAmOyPskBw0hn3hUoDKg6m-cZDk-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g15
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/funhiphop/76900" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">راستی یاسینی هنوز تو زیرزمینه یا بالاخره فرار کرد؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/funhiphop/76899" target="_blank">📅 16:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76898">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5lO7jQq_iO9Q4ZpJ6KTTL9upOsF-NAu_rZRWpFWjjoD5NXtTQ2y5XMSkuQpeeGnfroMegkKXzReaQVJRptwBQ-ejN47XtKFOhxylyXe9QiKckCz-mxs25lFkr0ipirP7M_duSzrfpNpP-dyU7Mf7E01hzKgJgxZ_A8Th5nDY9PayA5qzo6VE9SV_hsO564E0QdBO7GY98IsSz2S0EqMbN0HfX2dfPfyyV_2kFVOVOahXKDGtU68j-ZUw0KJUz8jSNLC9NRcibdORsDkV7UqfkHOuYOizB7KOh_vc4KcR96bpLzVu_5Wmf1y49JcvyHdyUa1yZRFiitvYP_LGOnAWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید ملکه جدید فرانسه بزودی قراره گلشیفته فراهانی بازیگر ایرانی بشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/funhiphop/76898" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/funhiphop/76897" target="_blank">📅 14:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUmPXyAk7XI5Vmfo1q9I7VfIJ6l3IlQG_Xqw8xWVlReCzJGj8hQhKkOsJ26Yz7pc0uXTp9ZPdWNbIhRK5TRtZ_UVrg4r3MBN7bVHzKxaawvZB1zIRniKN9v2R7pZ6wo-pSApzB8xd44mhClIy5ZA6gOz8CSVJy4tK6Y5t95rXjBmH2MrPP5793GoErhuBeHkcTp04xxIeQLy-SU-SAo86TMrPtkRMEHVpTswsbSX5WfWV_XdJMkMtkmfJhzlFZ0BRH7ULk0HmwVPZ1-wDotdHleOS3_CF2SHaMyeoYv6gFGL_vISrlkW7-lTHvdokzzUzg6xSNSqtRxEkVfgmvYTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/funhiphop/76896" target="_blank">📅 14:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نزدن رعد و برقه نترسید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/funhiphop/76895" target="_blank">📅 14:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اسرائیل جنایتکار حملات خودش رو به جنوب لبنان دوباره آغاز کرده، خواسته این مردم حمله به صهیونیست های کثیف و حمایت از برادران لبنانی ماست، لطفا بزنید، لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/76894" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وای اگر قالیشاه حکم جهادم دهد.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76893" target="_blank">📅 13:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-U4ZfRm68pC6ZdN7Hazm45ypBvJAHXyPkl3xggf_rw0GbrHIfkkXrl-cIbVI7dTB5akcT0mtnewdZCxhnYunHbh-gYaVcfEfCtXC8Rrq-jlI_HR_6iqPzvIgAYmf-LXKJJbqvooVlvma5_vS_wdDnIQ7uAV1Br-Zvn8zWPQlrxMF_4TqQcAYu83DptKvPePaLip3_bd9XG9LK0pwW0BR9cPcuEHYG7xNenXKEqdQe_X7zZxzu7cMNLSl4KIa22U9yWcRxI8JcXqYP62U7bgb37ZGrEVwAdPFiB1GuMs8sXKAtBbGmiPQoK89sPmx1_8ztOid-7iO6z1cmmoHwF9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76892" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مرکز ملی فضای مجازی:
طبق بررسی های فنی و ارزیابی‌ های عملیاتی که انجام دادیم، قطع اینترنت الکی بوده همچین تاثیر معناداری روی خنثی‌ سازی حملات سایبری پیشرفته نداشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76891" target="_blank">📅 13:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=G5qwebDaz34cK0wQwS50t0gScbTIv0uYBPmFAZKFb6OzWhrxJy9CDcShU4fy0Hm60Kz6G-7jwMFUgPXV75lyeBbQodqcJnmVQU4NqRxnByaPs2wVwifG25mQGBk59i7FI15T9ASCO95kC9HsrgV6dVZCzCTK9tsPLlxhkFBW87Vv3Zeph5cxMpqPUHw6n9pX5kyXaseK35kaAhU_J_4VflRyfbUeFNoSBvGMwoadkGQ64ziXnU-osMXXg3vzPPmmiEkI5Ka1xbM0wTYa5atTaBJnvQkXCdeSHnDIiQJ7xpbm61hWg62FE0WGjtyFuLEiEUWLLd4oN1tV5NQERFdyTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=G5qwebDaz34cK0wQwS50t0gScbTIv0uYBPmFAZKFb6OzWhrxJy9CDcShU4fy0Hm60Kz6G-7jwMFUgPXV75lyeBbQodqcJnmVQU4NqRxnByaPs2wVwifG25mQGBk59i7FI15T9ASCO95kC9HsrgV6dVZCzCTK9tsPLlxhkFBW87Vv3Zeph5cxMpqPUHw6n9pX5kyXaseK35kaAhU_J_4VflRyfbUeFNoSBvGMwoadkGQ64ziXnU-osMXXg3vzPPmmiEkI5Ka1xbM0wTYa5atTaBJnvQkXCdeSHnDIiQJ7xpbm61hWg62FE0WGjtyFuLEiEUWLLd4oN1tV5NQERFdyTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه اوه جنگ داخلی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76890" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تون 1.5 دلار شد
Make Pavel Mom Great Again
#MPMGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76889" target="_blank">📅 12:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تو هند 4 تا دختر یه پسرو دزدیدن بردن بهش تجاوز کردن.
پسره الان رفته برا باکرگیش شکایت کرده.
دخترا هم دستگیر شدن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76888" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ممه های دوسدختر صادن کو</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76887" target="_blank">📅 11:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhFlm_V-JzAmdYGZD_rMwF4ojPDhgaBHeV27J_U9gJ5JMW3iZh-C60vGFpkbsWD2ryU86p5ams6uPEchwrJJ3qkIk905-5VMCvbetjvGwo3HoZ73c5ykcpoINUXW-6hXBD9WnyeQVRI6R-RMoenpgn22Om4YQsKs7xBbew8bLkeQgjh1hcNEYtpCFcS7fc0Rpjlsk2cVW8QM2RLC6BZ-Fo-Mhmvr14RsaLuIah23LMlHnDsB9AOOQlrYR9CBuMQACASG7AIH4AI-y-K-amI-ucIMBE_AuIQLeaVS3xzaQbxGEOMXoq03YIA6pt5wHI4pDbIGq3pI7ogaYF_1JwU_cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چالش حدس پا.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76886" target="_blank">📅 11:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3rjGyimQlhK0fNNs9NmcHaSITvYMrfcd34U1C-7mq_g_VZTetlRRjVBuKj6eIbqlSVhoiDYunCCScSgGyJFsUfOtX2_noIbhjRawvItrtBGtwcKZVS3fw859v95NOlKYvb30hthpy9ACKKAWic6GBypWX_n5z4V2eGlEgSHym2r6EediqyztaJ7kM42E2X5LTMPUAeUGyPt9L-G6jxXVcj4ITWlxtFEsanwfTroM1Y6QR3xLkxU68ijnvQyTbW4hKxvwjSNaS1OISMr8lTGGo2OzjV5ZKt_zpC3cTz7WJGkmq0qPlA9BreTKDnajFJ4cD-DsmWyHqHleLWrnuSCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون سوال شده باشه که کنعانی زادگان چرا انقد مادرج چیز یعنی موفق و بازیکن خوبیه، باید خدمتتون عرض کنم مربی خوب داشتن تمام ماجراس.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76884" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbvqzce0SDSQu6WH3IT0tlkoHrCJgZqE-sUrg5CCTWJmtBrUw4BH7eAW9BvakLfmkd4Y5zWM7Rc0DHMQbgZQMBd2Uhnf_sGyWNUaV87RzAuGVVAjcoqoWyhGtg2sKKQOfvkqnSrLHsAci4cV7oKY9xcToXv90fHbiVkppblwYafWEfWbtDJEoelFqsoG4-GpD6sOWLAk0de4mdctkrk9W3ca0PXlIPVWAxayYhnyY6jI5ocVIHlbX-CxC_uv1CzOnmUgAmlReC-co37YZvR2mCOPrxs2GC1wgrW8XzvpgeFc9rLw-Sd8kGu9__Mizzt-JMbwRooZlT5yZXkb1l5yLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفیق حسین رحمتی بودن مزایای خودشو هم داره
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76883" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxaNAjqv85y0EjULkD6v5YdmPIGNCN64kl_kTsIsszHCEPFZ-pvPnAoiFwRKPAMb-SSfsJL8zPjteLgSjb8OGD0ZAgf7QWivCHFqZffvg49zY9uGSiUf5zHHe4imi7qJV36H5cjRlsFlWNPwFQbp5WGMdG7XRvOpfrGzVVHypVMQKqrM3B9NF9ThiSaC_Xp5C5WwUhki14lMqNVNdkNm6oHSu6Fek_HbcMlmMAZfXuldND8Vnpdeb3XXoQGUdAmwvHiq_SgdA0aYea5p2GYinWBGKNJjHSO2l7b-Y1gvOYIWRYmRZV2hOdA5ddelTRNKNexbKZeV4im17Yc1GwEXbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
شیلی در
۱۰
دیدار اخیر خود،
چهار
برد و
دو
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر شیلی
۲
.
۵
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب:
۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
👍
ورود به سایت با فیلترشکن
R15
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76882" target="_blank">📅 09:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ولی همیشه داغه نفس اژدها  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76881" target="_blank">📅 09:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXOcZn4rkXmRdmkUoP1XnVvEGAMyc4e6w9WiObPDQlz9XnBAiUpkv9YcZn_H3Mug4XLkrUVW9f-WIo3s2Dd7YAa1GmD9Nb9EJGuBZdFAjnSlHdKZm7pLQuLSzK93Ej6yRiRU6nBBEHkJ94b3HJMSjiGOCN3KckVw5K26knqUY6AAnjKznxvarWVohH473-J_ymo1PAIsNaX-wjhVfOAsDw1F3jPJCCcxW6OxSed07QU9z344kPDoaPdigPlgtc5nAKi7YC08PYS6jtGPB_ZiPGJgow9gUysapK8I0jP3i8gURpmmvyqMOSpGdleXhx_xw3r3jVpEcsjWyOy0e7SJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی همیشه داغه نفس اژدها
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76880" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4rVkGLIIwh7yphtqSLZp-j4hzgBVyZpQ0YyOuNcem1VPZ7DG9tEVrYVAzo7Gph3qFFUEsB7n8tiWbNuQdzCyA7czh7PChDjMHqk-HeUN_j-XZhbd7N3NNZk0QSqzKNm5DpcC6c2f-ArqPGOzTOxW4BROdQageMQ8MKCaaJGolbdLcY2y4jBpH7swFUtm3eC0yLC5fm10U1sYs3t4x16vAo5Chqyt2bzL7nIkSniUaVU51jOekLs1M7xhn02Pdfyr9F9W7lxJL4ZxNW3spFuvY-hny0wHxEMQhxoBzi-crNfxUraw5CHqlu-aqB7HjiwWBWhqTfU3yeVPqz5dP9rMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبی که با آلبوم جدید Blok3 شروع شه تا شب باید بخوابی سرجات افسردگی بکشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76879" target="_blank">📅 08:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">لری جانسون افسر سابق سیا و تحلیلگر امنیتی مدعی شده از یک منبع آگاه اطلاعاتی دریافت کرده که نشان می‌دهد ایران به کلاهک هسته‌ای دست یافته است!
به گفته او و پپه اسکوبار، پس از حملات اخیر آمریکا به قشم و بندرعباس، شورای عالی امنیت ملی ایران تصمیم به فعال‌سازی «بازدارندگی نهایی» گرفته است.
ایران از طریق نخست‌وزیر پاکستان یک اولتیماتوم سه‌مرحله‌ای به آمریکا ارسال کرده که مرحله سوم آن، انفجار یک کلاهک هسته‌ای در خاک ایران برای اثبات توان هسته‌ای کشور است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76876" target="_blank">📅 02:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HedsQBAn7G5zs-z1zxiqvs-Pxsim7slPEV2DM5W7neJGrcBfUBqpZa64bpwq67VwBEsj5hZCA-VfScUqoG4xLE_NY2cg5BcD1ELON_SpFkmTxpEw5egpZqAJfsnxq9DjZwCcWiv_gevgaXhPF-TQPEn0OmIgrUcyz6Q6-IY6651CQCSuFo1bZW92ZxTaGxU9Z0zmHKAQj0efrDCj72a8l17JuXFD1izDuK3SY0cK2SU7-0pfKb4uwzPmuqP5WGK9qc6lTBnxPW-f_TKhWzJc1pk8Ahks5gRAA2TKKw1X6dJRuquEry4MnkGrm_6zUpEuhxqD9OhbaKOvSjLK4LqDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفعه‌ی قبلی که این اتاق جنگ اسرائیل از این دلقک بازیا درآورد فرداش ترامپ
پست گذاشت
که همه‌چی آماده بود می‌خواستم فردا حمله کنما ولی ببخشید لب‌های عاصم منیر مهم تره.
الان باز اتاق جنگ اسرائیل دلقک بازیش گل کرده و خواهیم دید این دفعه چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76875" target="_blank">📅 02:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">برای بیانیه نیاز به اشتراک Plus دارید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76874" target="_blank">📅 01:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۲۵ بهمن ۱۴۰۴  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76873" target="_blank">📅 01:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artists: Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title: FIFA WORLD CUP 2026  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76872" target="_blank">📅 01:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUEgmZXR4A-y6KOyKOcmIsDEn_nho8w6Aarw2xzn5MgKlj7FlaH6K4zG89S4TKfbJ2hQ5fo74_38KlvBxphP6ASBDNaWS2sPIDmvqW8dK3999_O8tC12XvusWsoC9eZr9nlmpLICfXPwNHNjztUjffamjAhzz7s8VG_DyhCtzz-KRAKNTGHIR476K5wP0iWEMo_f-dxZw8AabYaYxXz9wUo-uQA3avKJ9trxjR0PcU7sNbhQQPKXUMojBItqgPZSOGosux-A-vGGYue3l3uv5dajo-41SVMhzRN4tda7hdWdFzClNWgfbT6ncI5D1UJH4hDxqDRWo6mTkFqcUNb7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artists:
Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title:
FIFA WORLD CUP 2026
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76871" target="_blank">📅 01:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu0kPQJqlXlVMMOlp_WCy-beCCR-dochU_6kl5EHTk4IEHrMQZy51aAYG5p6R2NMwRCrp-6MLvhTt6_NeuT-4DH7jREmSs9hjKNaJKDeOhmcGnEmOC7n0jsgSuoWUUXcfrTDjdngnUOswbkX8RJthfGun0glfay93HsKTOgmMFrrs1HZK9_hY_2v-0qfHmbUQKZ2RIK2VZgLCTX_0-dJ7NxR-l4J00WrsOmJP1JxV7Q5e8kmdclipQtCmJbzyi4MkKFx7Y4fSVrCoxh-n4ExjFwhS8UnJ7p67Xhx0ftgT_-kcNnqEw8Z8UjNazm2WJhu_76STJJLQcdhfPKG9KcXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم. خبرنگار: شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟ ترامپ:  خب من…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76870" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76869" target="_blank">📅 00:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:
من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم.
خبرنگار:
شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟
ترامپ:
خب من قطعا فرد مورد علاقه او نیستم، اما احتمالاً او یک فرد حرفه‌ای است و آداب حرفه‌ای رفتار کردن را می‌داند.
او در برخی محافل شهرت بسیار خوبی دارد، در واقع.
برخی افراد درباره‌اش بد می‌گویند، اما خیلی‌ها درباره من هم بد می‌گویند که نادرست است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76868" target="_blank">📅 00:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ: جنگ را یا از طریق مذاکره با ایران یا از راه دیگر پیروز خواهیم شد، اما قطعا پیروز خواهیم شد
ما سایت‌های هسته‌ای ایران را از فضا رصد می‌کنیم و هرکس به آن‌ها نزدیک شود، همانطور که باید با آنها برخورد می‌کنیم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76867" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76865">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLA6jxe-WZ7ZywawUTH5rH52yR29mPaJornxOoew-9f9WDm20BtOjoEvx29nUIl0R1J8wDhYB9FTYFDxQnZ-hfSvfWkTjaNODjmY93Qqr8C7uP6DMwOCu8PSfOUrRo8CTr9Sqe3_u2ZSwPLMPYQaFcb42AhomHPwlc5WZsCRXKo0tqg4kTYizEgi6sTlFQzv7dVBkoHCqVzC2Btq6mOWRiSyMsyIizUDypeLQqlcvrH8zKeb1ZaUSwDiyqZLxuvxWX7YXoc0NwHMMIHHjHSfBIxj1OZq81SQhrdRu5QGgcmKohEXD8BE3XprJXu4nUq6oWGO5vwXb1d5JlmjJRSd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلن نامحدود فروش باز شد به شدت محدود
🥚
هم براى ايفون هم براى اندرويد
🍏
🤖
600
تا اکانت شارژ شد
📣
قیمت آف شدید خورد
🏧
فقط و فقط تا پایان ظهر قیمت 397/000  هزارتومان
( )
➡️
حداقل خرید به علت محدودیت درگاه (
٣٩٧
/
000
) میباشد
💓
جهت خرید ریالی از ربات زیر
❤️
@V2boxinobot
اينم تخفيف امروز
💓
تضمين بازگشت وجه
➡️
➡️
➡️
بدون يكـ ثانيه قطعى
👍
اپليكيشن تخصصى
🤖
🍏
💻
اكانت  ٣١ روزه تكـ كاربر
✅
📣
:
@v2boxino</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76865" target="_blank">📅 23:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76864">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه طهلیل ریز بریم
آمریکا تنها یک شب بعد از هشدار دادن به شهروندانش حمله رو شروع نمیکنه
در نتیجه حداقل تا جمعه هفته آینده خبری نخواهد بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76864" target="_blank">📅 23:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟ فردا چن شنبس  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76863" target="_blank">📅 23:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟
فردا چن شنبس
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76862" target="_blank">📅 23:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76861">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76861" target="_blank">📅 23:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76860" target="_blank">📅 22:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76859" target="_blank">📅 22:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76858">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH3bMYOGmfFFXv5c9w5VLfbPrIqC3JHYS3SU-6ANYyZU1YQCsPdCuqmzRSG6Ly3VIxgUyrFer0nO1utuwpe68pGzxBXLhpnO6Dt8JpwWR8adACbtXAJinb0hz2kLOV2U099JBaBH1eaO4Vaeia4MzRT9YlPe2GDmg_Uy6fygoOqjtfQF7hV2_YsZOT2jIeOwJPjgXZMAHMqZNr5bU4pTCIKGZ2jEnWzIq0tcKEXNXJo2p113rmHxKNpdfwzJNmOqlZ4X9L8QG-CESZYawmPjl3kXwpDDJwGuO-6dxURuQOvHlCs3v0DZm3SIkmowfZ5xaMXaUHTMzKNu9s3Brm85SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76858" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بخاطر وجود بزرگترین تهدید علیه جمهوری اسلامی یعنی پوریا پوتک  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76856" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76855">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد پورنهاب بخاطر داشتن سوپر فیلتر شد  این وسط نمیدونم یوتوب برای چی فیلتر شد    @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76855" target="_blank">📅 22:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76854">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد
اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد
پورنهاب بخاطر داشتن سوپر فیلتر شد
این وسط نمیدونم یوتوب برای چی فیلتر شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76854" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYkfhW0duR7YoOZ1bI936VOKLE8TO15St7Rqp-i7ISet-V33DQ9Q6l0libMLmroD_T_Y75waRwAVLYr1O766uKtbo4GaqqFc2NFr_FiN8obrk2-wzt88VyQV6pwIL5oaMTBOI1eXqItV8hfWXhk7DeXPjagp7a_vvcbY9C7P4RttqsM6jgsP-LMgbBvzaPmPcKmP_Mnfjj-4Au1Erz77IOLuL7CmYbmkXO-oHQ_g7LRFmRQdMr4HtckzrLMJoVnWwTxLPq4IV18o9kyT_ZiQ4qtlXJghMsYgAFm_JclkU5SvwsBV99louBIue36AjzW2dMkAMMaRbCpyuoq2_tt_lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76853" target="_blank">📅 22:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJKlDkV0LU6uSXZ8FAfUF2Lny-a2Sa0w5Q77Ing9wbE3ZGXctHTar8adxwKwtfLRFxUSXXpJUCxNDkzkZEBX_3CMuoOvQfLLYoaIuehJQZpdw_Z1IRjEOaXm0ihzfZ4KObAzKsNN86g5r6EO_N8zcgEIG-eHQXmigm3QT--R6vpb1z70UNMXmFwH0zr2iNo3zQ07BGZNxEV-ZZ2XJW6x2wLWrg5eKiPx6-fLaXfKSMd_gYb5gbDdidP4YNhNDAayChNrhn5f3Tr-I-i3R07WsrxbiKlKrnCzbtZuJQSomgJNUEBl0h-J6pYhUFXEg1ADsNVKASa3Dp97v4EFRu4C-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسکش تحت تعقیبیما
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76852" target="_blank">📅 21:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07e570681.mp4?token=QMG-GYYNvrE-FMCr78ojqTEmPd-V6Q_BvzuJfYTJ96pG_KFh_FVuWMKR6o8KhZzRpITGJRm4ijQdfqQEXPvA01iYw_pKhfcuH_o0dW2WjD7zGeujRYZEBs0hi8IN0_rlt-n2uteeP8cLcEQY0vInc0SvmWrO13kgfWB-v7hKJlKvll079w75KQo3TEONUPkBulFlPtCkvJ1JUZIs3mEuuUKZq-3uG5riB1hzwNLt9pdWlUZ1r6cSWiR6vMPWn1u1lISM9ttduqByyL26kXdb1X_7e_df89uV8bHByGAkGv29iocYPi3n0i2gceW41mp0OiVWoZokYFjM8PEIAp8PnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07e570681.mp4?token=QMG-GYYNvrE-FMCr78ojqTEmPd-V6Q_BvzuJfYTJ96pG_KFh_FVuWMKR6o8KhZzRpITGJRm4ijQdfqQEXPvA01iYw_pKhfcuH_o0dW2WjD7zGeujRYZEBs0hi8IN0_rlt-n2uteeP8cLcEQY0vInc0SvmWrO13kgfWB-v7hKJlKvll079w75KQo3TEONUPkBulFlPtCkvJ1JUZIs3mEuuUKZq-3uG5riB1hzwNLt9pdWlUZ1r6cSWiR6vMPWn1u1lISM9ttduqByyL26kXdb1X_7e_df89uV8bHByGAkGv29iocYPi3n0i2gceW41mp0OiVWoZokYFjM8PEIAp8PnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر جدید عصر یخبندان ۶
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76851" target="_blank">📅 21:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🛍
قیمت به گیگی 8 هزار تومان کاهش پیدا کرد
🛍
حراج ویژه تا پایان امشب
⭐️
💎
30G-295
💎
50G-470
💎
70G-590
💎
100G-800
🤩
لود بالانس شده و مولتی آیپی
🤩
🤩
بدون ضریب و محدودیت کاربر
🤩
🔴
ظرفیت به شدت محدود هست
💬
خرید
🚀
کانال مشتریان</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76850" target="_blank">📅 21:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شهر صور در جنوب لبنان بمباران شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76849" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ژنرال محسن رضایی:
از این به بعد آقای ترامپ را باید روی ویلچر ببرند که بتونه آمریکا را اداره کنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76848" target="_blank">📅 19:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2HVN2cjqxebKmsMc-GalUwnJq-27Z6jncbRW19Rh979n38EmxTZajHOK9EEos9JYxqN67ya-ZvPW9kKz1Nit6ziVaMpCA-ZFzMlvEz5_UduuHqe-1bbFCyMHeZeEG8S_a5mzIoS63VrO3q197KqrXr0TJcvUyniY6gQXT9iibyECSS1hrY-uQwNCh_a0qpEcZZhDWUXBRlRVRYwk9zNuFGkTv4Txpm-GFr1wz_SbzoeMc7paxujzC4jE4S707CsRMi-0UiYbo_yAGYXuZEugwkgG1LSjVkrq_ib1TYSMXhe9SlSR-U0Bq7uAd_OPmPztyjDaIfK61ngLkdVn2WM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۷ سال پیش در چنین روزی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76847" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyEFqLZRSxyrn1AvP_N4GwsNKZd9sz6hDtH2R0LzGGsI5OD5jRYK_wh5oc-cAhjODNHyLJ7p8U4hz0TykGgE8TMTlwYkdkt6HMr3nbo77p_M5mPA75EhNLFgyHKLOCTOFyBWafVaDuqhDODiCN6g2wICxe_Eer3diyVvLabuBtSrzAJIz1Ruvqzk5SS5WyUeqOT-sUG-SVK_90taxo0HOJhjpIEytzgU0KEG_6axLxUlmT-B0xfTe3Eh5rBJ03KO0eoDclVufLczQwedM9SMi6-ikOkaf48JwhGbArXB2XJMNG9jMcpnbBq3R4WDyRKXtjIyNHp_PGYyARtBa8urjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :  @Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76845" target="_blank">📅 18:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76844">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حاجی کاکولدی چیزی هستی این کارارو میکنی؟
- اولین سوالم از حصین وقتی حضوری دیدمش.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76844" target="_blank">📅 18:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=Mw3mwJTTWLv28jrcXcVMi9A6Op1e4wIAZcj3miJm-9tcTkn3oW-44ymBbLxeDUIBxuQcrrwuN1XoV3JNejyDkX9vidJzdU5qfPLbzOkDBa8jBG4gBPS72k-Db7syCbyyxVWgRiDvYhlLApOQVyj6tuVhRrCRCOBu67vALK4X6wcAubABQD_bdsPej5kYDC-PlyM8aPmJKipHvBAnL8KpozquOa3h8ALywMuvYt0YG76aIv8LEi3gZyodfScSW5s8P2DoEOW3_Gko9IFSNfmOaCZoTbcr8LqfjB29QkJ4KX2YVatQ4eBcsUOC-7lxaLhq3zkqXtazKFKIDygFGL9nZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=Mw3mwJTTWLv28jrcXcVMi9A6Op1e4wIAZcj3miJm-9tcTkn3oW-44ymBbLxeDUIBxuQcrrwuN1XoV3JNejyDkX9vidJzdU5qfPLbzOkDBa8jBG4gBPS72k-Db7syCbyyxVWgRiDvYhlLApOQVyj6tuVhRrCRCOBu67vALK4X6wcAubABQD_bdsPej5kYDC-PlyM8aPmJKipHvBAnL8KpozquOa3h8ALywMuvYt0YG76aIv8LEi3gZyodfScSW5s8P2DoEOW3_Gko9IFSNfmOaCZoTbcr8LqfjB29QkJ4KX2YVatQ4eBcsUOC-7lxaLhq3zkqXtazKFKIDygFGL9nZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آه فدایی آروم تر
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76843" target="_blank">📅 17:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76842">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=PDhJVidjlhlelfJu4H1DqEVEN32QlgqJWJdmy6Pejw1CqXOTnWs-dC3mR07cMzGWFhd6qp20DhmeoZXZIPgFddECkVfBgb-0s8EbalgMdYAwBAbyanWKuQmo1QQstSGMkk6ygrm6IhGBThpfvCn_Kl8111qCvp0O_G5YOhc0UDse3VPZf2xjXGWKGb7VdRuEa6Sn6miubU7_lLrqQMSze2dJZCWSK9paXqoNoVJz28k78CRhq8QoqFdHLjSzOiXOgRLrV0l3yVozefv7ZSLKPhsCTyl9ysKSKObcNrOGcpcFtVWweKCu0TqdcDQuJ71AlD2J1_sqVoEqllGgWMkj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=PDhJVidjlhlelfJu4H1DqEVEN32QlgqJWJdmy6Pejw1CqXOTnWs-dC3mR07cMzGWFhd6qp20DhmeoZXZIPgFddECkVfBgb-0s8EbalgMdYAwBAbyanWKuQmo1QQstSGMkk6ygrm6IhGBThpfvCn_Kl8111qCvp0O_G5YOhc0UDse3VPZf2xjXGWKGb7VdRuEa6Sn6miubU7_lLrqQMSze2dJZCWSK9paXqoNoVJz28k78CRhq8QoqFdHLjSzOiXOgRLrV0l3yVozefv7ZSLKPhsCTyl9ysKSKObcNrOGcpcFtVWweKCu0TqdcDQuJ71AlD2J1_sqVoEqllGgWMkj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76842" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76841">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">اگ دنبال یه سایت با هدایا خفن و کاربردی هستی اینجارو از دست نده
🎁
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/funhiphop/76841" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76839">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=p4eKDWhs4Qjp3SKf2p4COLQZAVqE1JQ6x9rkB6h7bMBDmGNU817jRUD32JVC2D4n3y5ba-QU26uET7JSPorxFlo2a3aJqX10Nmz1yJf9gmWcD3iOSxkm-FRwNafox472-yNhWXfB5BZHqmAiuevqULDHhKnoF-SG7_fPNZX_r9z7EcI7Wb994DXzGal6M-mMf84i-xfKo6qEso9PtcxqoEXgK10PDjR1fJM1EgH3-rMxCBQFeE9M2e4afSeYp_odVn8jxwyMb6-vRO4faHWMPu5e2FFLhIi900TPjzFFS6449Oz1MGlz3SJcgR20XJdFqvaC0OzxRJ8M2SMkA8ToYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=p4eKDWhs4Qjp3SKf2p4COLQZAVqE1JQ6x9rkB6h7bMBDmGNU817jRUD32JVC2D4n3y5ba-QU26uET7JSPorxFlo2a3aJqX10Nmz1yJf9gmWcD3iOSxkm-FRwNafox472-yNhWXfB5BZHqmAiuevqULDHhKnoF-SG7_fPNZX_r9z7EcI7Wb994DXzGal6M-mMf84i-xfKo6qEso9PtcxqoEXgK10PDjR1fJM1EgH3-rMxCBQFeE9M2e4afSeYp_odVn8jxwyMb6-vRO4faHWMPu5e2FFLhIi900TPjzFFS6449Oz1MGlz3SJcgR20XJdFqvaC0OzxRJ8M2SMkA8ToYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرایدی که پرچم حزب الله داشت با موتوری که پرچم جمهوری اسلامی داشت تصادف کردن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76839" target="_blank">📅 17:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76838">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گروه هکری حنظله، وابسته به سپاه پاسداران انقلاب اسلامی:
امروز صبح یکی از مدیران ارشد موساد مرتبط با ایران رو با بمب تو ماشینش کشتیم ولی احتمال می‌دیم دشمن مثل همیشه جرئت بیان واقعیت رو نداشته باشه و تکذیبش کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76838" target="_blank">📅 16:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76837">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اسپاتیفای تست کنید بدون فیلترشکن میاد بالا</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76837" target="_blank">📅 16:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76835">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZGphazEZAwVfTTIG7af_iiuUs66QKEjaVFyKYgr0IUrt18jZnSHFHFwUlgUDEValoO6njlMp-OUpZOPJtqkQEzttX4VsUsybuCFIwG4_xl0ZJx7B78Rp8sxUaRPvUDEc4RnjZngHyy_33XDj6UfBoMi5ZQucCUa_s-KNvVKDsC39lvyyDNo7TJdPhwMj1r1y0UoORmglERjfLfBkXmU8YLKs_niliP5Vl4kES5L5DryEm7pXlZb8B-ElxcGFmR-wd_OjsbgDwP03kKTOIGd5RelxEoJBWlrz2AfueKCQ3IXwxSceExu0QJluhedJYAzKXQH6oC4k3Ql23fFt3dK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتی داشت مینوشت سپاهیاوووو یه همچین حسی داشته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76835" target="_blank">📅 15:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">https://t.me/+nm4DbCzoFJVkOGRh
https://t.me/+nm4DbCzoFJVkOGRh
ی جغ مهمون ما
💋
دیگه لازم نیست برای جغ ب سایت های پورن و فیلم های مورده و قدیمی بری
🫦
تو این گپ با تصویر کار و زنده ارضا میشی
🥰</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76833" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یاااوووو</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76832" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پروفسور سید عباس عراقچی در مصاحبه با المیادین:
در لحظه شهادت رهبری، من نیز در دفتر ایشان بودم که مورد حمله قرار گرفت اما به صورت معجزه آسایی قسمتی که من در آن بودم مورد حمله قرار نگرفت و سالم ماند.
من آنجا بودم تا در جلسه به ایشان اطلاع بدهم که با توجه به مذاکرات روز قبل از آن، احتمال جنگ بسیار بالا رفته که متاسفانه این توفیق نصیبم نشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76831" target="_blank">📅 15:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">امین منیجر داره هد میزنه میگه میووو</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76830" target="_blank">📅 14:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ی دور از کص خوند ی دور از موش خوند، ی دور از سپاه خوند، ی دور از بسیجیای محلشون خوند
آخرشم گفت گذشته ی هرکس به خودش مربوطه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76829" target="_blank">📅 14:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدونالد ترامپ</strong></div>
<div class="tg-text">ویناک بهم گفت نابغه</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76828" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.  YouTube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76826" target="_blank">📅 14:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رضا پیشرو نسل جدید</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76824" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عجب سمیه
😂
😂</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76823" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76822">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPBo7FPImupdtSgjXSsfqhGP_mO7UghC88jhV1DTG--rKblC9aT-8vTtjL7qCIrVo-WUoSZj7v2gYbVJHuDI8YZaf0CqdXww0-fT11rSa_XxyQHgsQRDebohUXUnKa-686FOD5yNosPF9r0TYy15pyM5OwuKpzjNApPqRo4qSBJBtBZ76ewFLe-tVwxpOLGsmN48P-v8POLlTvwtsl0ZQO9vwMjRl3-GBqoOqDc0OMSRId9EWCil0sLifPoYJhbvW096ixRg8zPxMXG1AZRqTW0dSVthsQfPr2AjzaEO4e6wc3oPrRqKwDXuBGstmyfrDK76ddj3TDwjEE2q92FBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.
YouTube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76822" target="_blank">📅 14:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQSUM6i5aiSZQgdDJnZIIeH9bGHQ17LEDwujUyq4SRZYSjx49JQIGb6SKIJ_rfBDNH1OUGqou6_wvc6n9hcBTxPPsZr9e2gyeG9p-zNVgYL7esdMf1Ib7Q_R1DxmoeCPtApruYbxMSJx6iKrSIQdPO4fI5Qr2c_uzDu-oVIO1s6QiAcNzU-ZvgBF-u-w5-P_oARk2iLyunO21bNrMs_Pox2smMC3QiGQzVDVAGLmu1zv8m8HDqKBsrWDaP4R7MDpVMpU9_9NPH0KcNq6RuBpkEkz5TvV0i73vkLkRPowsJGZEqGEZdj60jHutgEeScGOB5M5Hj1TiT8gWWhF1g3uLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید دالکوس اعظم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76821" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76820" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/funhiphop/76819" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76819" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76816">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw2s5DVT-48DGYQfCwz-2NECRB4lJ3Te5cfdc8yAwTXvFn-j8EsQZsDU1lzT9E5TFFfRIG0MfNn0Sy4bhQnMqkg0qVwnqNoFrLozlqtx79jdEIPg8S-IGqgb0cMorZ-qVGrXvzA5CoQeC9HYttLBe32SoA9yL_GymzQs6QsrbSQXMUPCx9j4pxlytkHB_JOA1SKfnkIXZRNKtxhUzmWjOvpXcrHNqBT7B5Xrd0wJPABhD8oPPOrRgNp7jJX5tA6PhYUBfshRg0-v3CzjvWKgxiD7wNGquOPPw4DBTjTlMvygUKR7wpO4BDAE5E6lxPQzglPs4iig_dIZw6Mzksk5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76816" target="_blank">📅 12:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76815">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76815" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76814">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76814" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تون مادرجنده از ترامپ غیرقابل پیشبینی تره  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76813" target="_blank">📅 12:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این مدگل چیشد حاجی زندس؟</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76812" target="_blank">📅 12:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYcO-X0CtFLm1bAQ7nLEeu0RvTeYEhwK2yqrJV5uL9uxFlp_75gbDodFWSYVG80b4u2tZIlGi8oSUGPzhrFmZ3kNMmbIq--3Y1EZ7EtqjKcKIH1qkUk6SiKbhjwmNQwEgc51cnpwfbEEctJiPUn_uJYIqhmIcKPZT0lvky6YiBAcKdwTeIEH5VAJ7OtRjnKXOJwb_8yr9HfM9V8bAZBt70BX1YyPtPZRZk5fC6XwR0OfiYIUjdpDWilrlpArcG9WoXHUXZRXR2vANf96lnEUF36vvOfP5crr5QpIYnsW0HdW3RTPj7wDIcz8Wi26__XcoEugM46vxI5YzkZ6VzicwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه رپفارسی با دمبل 5 کیلویی داره بدنو میسازه؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76811" target="_blank">📅 11:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=YAraBoOWUznqu59S5MpSv34mzy9GMl02jyAIF-PXztEwuE3-6n5EyqdiNzl2gzeuPz4fqB1USSjKWDuLSTgDPvPI6ZzYyDJZn11GMAyT-5-vysqOrFBXgnYm_TfFwCY8qJWqNu1whqicvBROibWxMGn318U6P6R-Qt-Gvk7LR4ePlzNw-pBUr8QNtCnEPu1v93oNfhhsA7tnREjmWvlndr4c79m5AQfDQNWxIMHQjm2l7SzXyn7gW-Gi3Gk7CODPwM4t7AoLRcD1RHqhBas0fr-q1v_EMan54rAZhgCqqgOkQuYGk0KtPJEODvE8D0mjbrwvkRqq794CmZCETjNE5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=YAraBoOWUznqu59S5MpSv34mzy9GMl02jyAIF-PXztEwuE3-6n5EyqdiNzl2gzeuPz4fqB1USSjKWDuLSTgDPvPI6ZzYyDJZn11GMAyT-5-vysqOrFBXgnYm_TfFwCY8qJWqNu1whqicvBROibWxMGn318U6P6R-Qt-Gvk7LR4ePlzNw-pBUr8QNtCnEPu1v93oNfhhsA7tnREjmWvlndr4c79m5AQfDQNWxIMHQjm2l7SzXyn7gW-Gi3Gk7CODPwM4t7AoLRcD1RHqhBas0fr-q1v_EMan54rAZhgCqqgOkQuYGk0KtPJEODvE8D0mjbrwvkRqq794CmZCETjNE5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط 7 روز تا شروع جام‌جهانی مونده.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76810" target="_blank">📅 10:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFNdKeCJe32e4jUoVCu0Sqgsp5a7Lr7tfajj_hfLgWRutXqzqgmJH2nyxm0kYCB3kaXGgL9nB7emN45Qz-ImOwzLJB6jy_i5JhOPPfzgPhRP-U8Aw4G-CISpFdxGGabNvyhSQFJ8jB7L5QqFatrHj-tDrEKO6j0gMJD1L801qt0mDJLTRlEJ-BknaVBD_Vpf8CzPRs5qBC740qSIAq5VsKW3WZxyoqF1TPwiXq7cHHIKNLQx1ROegEVMXtxA3o0MOxLFYUChsUbpf4srIIQyOufnwgOBGpa4-67v3_nmG9wG8cTcOOhOCk1jZsJ0AKXyI5mM-arzB02noK0Tf96A0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیبیلاتو نزنیا آقایی، عصبی میشم
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76809" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ به طور خصوصی به دستیارانش گفته است که در صورت
کشته شدن
سربازان آمریکایی توسط سپاه، «
ممکن است
» آتش‌بس با ایران را پایان دهد
.
بی‌میلی ترامپ به شروع مجدد جنگ نشان می‌دهد که ممکن است حاضر باشد برای جلوگیری از یک درگیری گسترده‌تر در خاورمیانه، درگیری‌های کوچک‌تر را برای هفته‌ها یا حتی ماه‌ها تحمل کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76806" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آمریکا و اسرائیل و لبنان امشب یه توافق کردن که توش هیچ حرفی از عقب نشینی ارتش اسرائیل از خاک لبنان زده نشده و اسرائیل گفته اگر حزب الله حمله یا خطر ایجاد کنه ما هم براش می‌کنیم.
در عوض لبنان قبول کرد که حزب الله رو به عنوان دشمن متخاصم بشناسه و خلع سلاحش کنه و اعلام کنه که دولت لبنان هیچ مشکلی با اسرائیل نداره.
آمریکا هم قبول کرد تو خلع سلاح کردن حزب الله به ارتش لبنان کمک کنه و ارتشش رو تقویت کنه.
خلاصه که سه طرف به توافق رسیدن بریزن سر حزب الله، اگه محمد باقر شاه هم قبول کنه میشه شروع پایان حزب الله رو اعلام کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76805" target="_blank">📅 02:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=KPV-FqXeTM31HGfalm-JIIm41cQ09jHDzG2NMauoPVT3mTENjC1GC9o6H2-nkreI-7zXxGZAJRfb14pfbNsM74AR9e6j8MiDIv3j250pgFw-MukXy1OCYnbyJKIH3oMr0T9TuZFGIzedFJQHFr6Np8I4NplqOicSoYPfFeojuCRDK7cuT-o4tu5tWLMjArFRhSYXphunA_oIghyIyD-Sl51rP8dvKWXZFzOTtRpubjk1SLZnyxc1Z3isu1pDJ0PbHqHyVnj1anFrA6qnToPHN5Cv-Hqb3j3Dj-8ydBUF_Z_7zJyfpyBBIqFO6dbtoOMxCSgui0RsBb8rX8YB03FGnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=KPV-FqXeTM31HGfalm-JIIm41cQ09jHDzG2NMauoPVT3mTENjC1GC9o6H2-nkreI-7zXxGZAJRfb14pfbNsM74AR9e6j8MiDIv3j250pgFw-MukXy1OCYnbyJKIH3oMr0T9TuZFGIzedFJQHFr6Np8I4NplqOicSoYPfFeojuCRDK7cuT-o4tu5tWLMjArFRhSYXphunA_oIghyIyD-Sl51rP8dvKWXZFzOTtRpubjk1SLZnyxc1Z3isu1pDJ0PbHqHyVnj1anFrA6qnToPHN5Cv-Hqb3j3Dj-8ydBUF_Z_7zJyfpyBBIqFO6dbtoOMxCSgui0RsBb8rX8YB03FGnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستیار ترامپ و معاون رئیس دفتر کاخ سفید یه گیف ساعت شنی توییت کرده.
رئیس کمیسیون امنیت ملی مجلس ایران هم زیر ۲۴ ساعت بک داده و یه فیلم از یه موشک ایرانی توییت کرده و نوشته:
خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76804" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.  رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76803" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.
رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76802" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انریکه ریکلمه رقیب انتخاباتی پرز گفته اگه پیروز بشه در انتخابات هالند و رودری رو میاره رئال و حتی کیت این فصل رئال هم آورد که پشتش نوشته بود هالند و میگفت همه چی آمادست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76801" target="_blank">📅 00:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=Nmp3Q37xzoWCmypgPfJ3cPy7oVAKeLrKJOYb7oNNzSidHtIC0NRVM6pyOEuWUCZh89RIdObjm6FELEEL3kUU8pxSnlbjN_B1YWM-Wt3c-VjdoYYoyQ2XQ7nmjT5Nu6IHfyQiUXL1SWIvOECedlGS8CQnQtJvco9C_DB7XB6nXEOLP3lzRGmiTsNWNVLSLc_u46lvwRs7fQ9BMy_rWdB5JM1OWDkY1WIQkAxQ-7njdhYkB-WonuLGvh1Fl7UthKHkhoI3iOQlYHOvzLWG-7lJ3qzbG1wrUaL7Z13BLZnbzpKi5Hur1uyS0Yfq_WJQeIUUlSL7N17Z3w3xjzlGw1URBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=Nmp3Q37xzoWCmypgPfJ3cPy7oVAKeLrKJOYb7oNNzSidHtIC0NRVM6pyOEuWUCZh89RIdObjm6FELEEL3kUU8pxSnlbjN_B1YWM-Wt3c-VjdoYYoyQ2XQ7nmjT5Nu6IHfyQiUXL1SWIvOECedlGS8CQnQtJvco9C_DB7XB6nXEOLP3lzRGmiTsNWNVLSLc_u46lvwRs7fQ9BMy_rWdB5JM1OWDkY1WIQkAxQ-7njdhYkB-WonuLGvh1Fl7UthKHkhoI3iOQlYHOvzLWG-7lJ3qzbG1wrUaL7Z13BLZnbzpKi5Hur1uyS0Yfq_WJQeIUUlSL7N17Z3w3xjzlGw1URBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل اینکه خوشش اومده  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76800" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1_fg-5O2C54pPiy1_Pte7kq0iTwI-2HJPW5GYkr-jz7XFSAxitrAIsHwTFwbypk0gys5JdwcTnGdwOPZ9B4u2ntm6Q1xMxX0Ld4bHqVSnc-Um3NeerTVOZ2RblCHFQegQ8OJ04aWe1kqqcxyEGRbF9CRhE65H1rr71ECEuhDjv7mgd6vXtwjJkpZlOfsRNJ6v2TtYWUBU8oZHEbq95KbU4B1jDIt3ACKw8c3RRIQvGRyUJ8XslKQoYZJPW4YETHjsKBvYjVtUeGn2Dj5ER5-cif-6h0J-nV5fdcMdtFLmBUEcScugxU8iHPKOjBPS8HO-VX3bGVOoXM3NM2D2P2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه خوشش اومده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76799" target="_blank">📅 00:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ
چند روز پیش اولین بار بود که با حزب‌الله صحبت کردیم.
قبل از آن اصلا تصور نمی‌کردیم آن‌ها توانایی صحبت کردن هم داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76798" target="_blank">📅 00:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ب‍  غ‍     درباره حملات دیشب سپاه به کشورهای منطقه: خب، می‌دانید، برای هر چیزی دلیلی وجود دارد، و ما قبل از آن به شدت به آنها ضربه زده بودیم و آنها کمی تحریک شده بودند، بنابراین آنها کمی پاسخ دادند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76797" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ درمورد خاورمیانه: در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76796" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ درمورد خاورمیانه:
در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76795" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez2MeNMwJy2KYL45dTiz4pCwcYDucM-svbKKeb09paJmrCe_VOavKEMj177vQgqO8ezXQx9SbPvFMS-uzXPvxzXWNepbbQscSCQOu-xe3u0nzCsAZiu_cFq9ELajI2CMEN2sDGf-BBEgoupwfvNXOKO6GOiaPtY5QtiW89FWwyOMLsqsKHlNODX_rNYjeK55Qb4RUZdOzcn54GR06HhPe3T5e3t7KGqwqJnlDW8LuSVZWs27AZSIcxRfoxU3R4pyVI6InoGVTM8ZVZeyMwRwVQ2hCRZuigz8ZxTv9RcTQKjTHpI_mCbt7NJuorZz5DYEQqTA1r-IHGYEx9ciTpj3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر گادپوری نه نه چیز فاز و نولو درست بزنی هیچی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76794" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHiZznwBAQ8gvTG4WzaqtQTVK7x9-iMt1aiWts0aNsxzNmFxXzvEXmnMW5GpYIDZ8aWKw0_BT6HEzfMExXtzJcaHR2GAMC1yrCrIPN8_-L15UYSVvHA4l3ebDfvODHstIASqfM6vCVg8_3QEjskCQM8ddUPO5vk8W4oRIEzKEejpWa3lCqn0vtGi6AWpXrOjfQrF3jiQPRji_8KKFF6LCdrZEPr5uAbo_h4ZKOT5YKnd7-NV6MbKrirGdAcjaXyTvQMnFr3iulCBZpV4cdvcZyi6qFoy-IG9JvpGm3Kqu89Xm7hrX83ZHJ21BIjeh8F08lt3s4I39QUr_U9NB_snYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اینترنت بدون دردسر با RAYA
🚀
📣
توجه 10%تخفیف تا پایان امروز
📣
⚡
سرعت فوق‌العاده
🔒
امنیت و پایداری بالا
🌍
سرورهای پرسرعت و بدون قطعی
📱
مناسب بازی، استریم و استفاده روزمره
لیست قیمتی سرور ویژه
RAYA
👑
بدون محدودیت کاربر
👑
پشتیبانی تا روز آخر اشتراک
👑
دارای لینک ساب برای مدیریت حجم
⚡️
لیست قیمت RAYA
⚡️
🔹
10GB — 150 تومان
🔹
20GB — 300 تومان
🔹
30GB — 450 تومان
🔹
50GB — 750 تومان
🔹
نامحدود ماهانه — توافقی / ویژه
━━━━━━━━━━━━━━━
📢
مزایای عضویت در کانال RAYA:
✅
دریافت کانفیگ‌های بروز
✅
پشتیبانی سریع
✅
اطلاع‌رسانی لحظه‌ای
✅
آموزش و ترفندهای کاربردی
✅
امکان تست رایگان
🎁
همین الان عضو شو و آنلاین بمون!
📲
لینک کانال در بیو / دایرکت / کامنت‌ها
#RAYA
#فیلترشکن
#VPN
#پرسرعت
#اینترنت
#تلگرام
@RayaVPNChannel</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76793" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=GHL-kfRhJZzwXRBwn28onChnLxtfoCbzKOMiePC3ul6nX9BLWSD6VPP3aWTAQnprlStvu0Tr3gcl4QrXQbHXQU9-l4PHC91M36ChoEMtsISZFsL7YPQQXGTJs7JWv3_ysAtckM_Ym2rgTruq_s02ouiP0Ojr6jrfLalDfSvqUfi2smWqeqGadUdlITe-C0RJmXHHdqMcXFMW6288yoM_6gXffOKZvahGWeKrH8Xj4GBVwYx8uiFofAQmYOhzGvp3-BPZbf8S1rQcrOntOsB93hxNQFYDrTs0CSZj4m4lcKoJxVuEzusB9ZgE15e7tYiIwC4UD_OEXC2NCxb6R_qAmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=GHL-kfRhJZzwXRBwn28onChnLxtfoCbzKOMiePC3ul6nX9BLWSD6VPP3aWTAQnprlStvu0Tr3gcl4QrXQbHXQU9-l4PHC91M36ChoEMtsISZFsL7YPQQXGTJs7JWv3_ysAtckM_Ym2rgTruq_s02ouiP0Ojr6jrfLalDfSvqUfi2smWqeqGadUdlITe-C0RJmXHHdqMcXFMW6288yoM_6gXffOKZvahGWeKrH8Xj4GBVwYx8uiFofAQmYOhzGvp3-BPZbf8S1rQcrOntOsB93hxNQFYDrTs0CSZj4m4lcKoJxVuEzusB9ZgE15e7tYiIwC4UD_OEXC2NCxb6R_qAmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس:
ساعاتی پیش،
نیروی دریایی ارتش، مرکز فرماندهی و کنترل عملیات‌های ارتش آمریکا علیه کشورمان را به صورت مستقیم هدف قرار داد.
ساعاتی قبل و درپی اقدامات تجاوزکارانه، نقض مقررات تنگهٔ هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی ارتش جمهوری اسلامی ایران، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی که قصد نزدیک‌شدن به آب‌های جمهوری اسلامی ایران در دریای عمان را داشت، هدف قرار داد.
نیروی دریایی ارتش، با تمام توان، دشمن جنایتکار و متجاوز آمریکایی-صهیونیستی را رصد می‌کند و انتقام خون پاک شهدای سرافراز ناوشکن دنا را به شدیدترین وجه خواهد گرفت و با هرگونه شرارت، در کمترین زمان ممکن برخورد خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76792" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76790" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76789" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مقامات اسرائیلی:
«برآورد می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76788" target="_blank">📅 21:34 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
