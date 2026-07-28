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
<img src="https://cdn5.telesco.pe/file/lKncEe7zBz7hl2UtJeuPpgnKfuCPXOwvPTzoD0p5IjFq_XCbCXF3ItbfU-zhpyNq1VYevMMacTHrKPV-IBEasGUU9c7oPmmEN5c8vlECoEuB6Xi59ViWFUrTMnXAb7RdruTqKGleeFoMlIHUSOyjv4MO_ffBvFJtxmsUq_yZXD9SoTs3kqLxi9mYM1VK15cd3GMddzAx0yG_B35h0QgFOd0zcucmXMJlfBF81guHVdob8vnnbZL-mGNV6HTpXe2LkXo0zdp-MbJpkc3SkCcCJ8mdu-hKTAob4OZGjS_OfiL4IEiVZNx3lpPJvl1azLkBEWAaSG2pefYKXa6n3EP-aQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 521K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 03:26:08</div>
<hr>

<div class="tg-post" id="msg-102112">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKgKfgjjf72kUuTdiL2qkES6Vo6NsJghQZ_UqxpWzqAfIKa9gMv9bnz4SMwr5mdPorlquVrxEgEP9C0TNkBz4BSW3hWkS01bfVRtpQFWtipFOD0GezoMKgCsf3dSRFbQwnn2JnuPsrEh_hQAZ-4pavRWJ0h35lQ5p-hCDj43_i8BnQzKbnCWSDT_ZbUXsLJPBpkutcACWBSz1zUp-WeZ6NbD5NQz8SgXiCGfL3m3RiZiiPgGezMXfpph8yJPF10JLlCqs1LH0XkeXD8kTfBcK1mTwRXYOI6jrY3jQAnbxOxQTvXi_ieAK8u4uqVuPNHGQcc5PskquYhuZ0BkuVk26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوووووری
از رومانو: پرز مجوز مذاکره و عقد قرارداد با رودری رو تا امروز صادر نکرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/Futball180TV/102112" target="_blank">📅 02:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102111">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N02JxZEPcBmz5_mtfLPLOTZ4_45hzww0zn0_V01eBrLW0_zdNxPpK_T9aOuhdI8ausEe2cYt9EeE13AUCi0RHN_GX8rr_jaO2SF1qOqwFmWs1WbpBOOX0HCVoFn7h0wmcPw6iw4BLYuIxTBqsqvBYl0IZBeU7gAmq8rzG1mo9gTz3tIMZPsj-xBS_a-ue9m3EcW5e1guLdo51nFDg6mvN0GdMZhk8C9Rg0EBknhQ2JlQnHy012Sx4buUlvyOCGEldUGTTx6OJwR7exJfV3SNEC7o2oBPFHJZV-uMdD_PjMpBhqtLwcC0pGZx5naryTPV2LWlaz4UpIMsyxT08vCuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇹
افشاگری پائولو مالدینی از وضعیت وخیم فوتبال ایتالیا و دلایل استعفایش:
یکی از بزرگترین اشتباهاتم این بود که اصلاً این سمت را قبول کردم. سطح فوتبال ایتالیا به این حد سقوط کرده است، و دلیل آن فدراسیون است!
وقتی منصوب شدیم، فهرستی از سه نامزد برای تصدی سمت سرمربی تیم‌ملی تهیه کردیم. پپ گواردیولا بدون شک گزینه اول ما بود، در حالی که آندره‌آ پی‌رلو گزینه سوم ما بود.
ما مذاکرات خوبی با پپ داشتیم و به توافقی با او رسیدیم. با این حال، وقتی به فدراسیون اطلاع دادیم که به توافق رسیده‌ایم، به ما گفتند که نمی‌توانند هزینه دستمزد او را بپردازند و گفتند که باید گزینه‌ای ارزان‌تر پیدا کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/Futball180TV/102111" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102110">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=CQCB61MtC2nAzGKWMNF9ajYK_pyaTyh9WFIGr6aENZtL-Tk3aX7c43GqmJAe6f9B3mPn8Nq23rC-NFr9D0KJTNgVsoNecl12-yZaDVuA-8RkFXKcSFmsWjVmVDxHBabAH_uBgUEdXctd4mVJcHorjkcb_aIKi_xBtzC96mHX2ySVZDLQnIcdMiECv9GHvEhVfrq8hLX-Z6DLbKal0_BZ1O7Zoeq7DaMuSwYMAqG-kIExqIsLTnAEJzw_xg0plMklTz3BhVWgn_Sbaj-0F6HKc6w9F6XLXNkLVduX59PP68WEgz1LvyISJoawUNp9CHSykf8lcMMhEVs-EpPc3IyAQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=CQCB61MtC2nAzGKWMNF9ajYK_pyaTyh9WFIGr6aENZtL-Tk3aX7c43GqmJAe6f9B3mPn8Nq23rC-NFr9D0KJTNgVsoNecl12-yZaDVuA-8RkFXKcSFmsWjVmVDxHBabAH_uBgUEdXctd4mVJcHorjkcb_aIKi_xBtzC96mHX2ySVZDLQnIcdMiECv9GHvEhVfrq8hLX-Z6DLbKal0_BZ1O7Zoeq7DaMuSwYMAqG-kIExqIsLTnAEJzw_xg0plMklTz3BhVWgn_Sbaj-0F6HKc6w9F6XLXNkLVduX59PP68WEgz1LvyISJoawUNp9CHSykf8lcMMhEVs-EpPc3IyAQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✨
روزی روزگاری ایوان زایتسف بزرگ و افسانه ای در خط سرویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/Futball180TV/102110" target="_blank">📅 01:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102109">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybq1YgKOGHULljLy9Qek0vILtHE98QARS4DjLwh7gm0cwh7q9jw7zKTiqanvTIKyIcQgg4z6NC_1YVcsXAZb8LaUPfjaG9WhaLewRFyClATUp46DUbghb8w9LJgB721redL5mX1JnH-E3nEt4mBxWw_XZ1rb_tRx-CX_GPz0AiQbNW0NQHaYyIsKz1EtAlfjbu2deCzbvGoeYYhvEc_SYUy240SHK5kLoeWk4yaSMjS_cFrE-mC7cBts-kVQ9zoWCzbDom4o0J1z1HCxEN0RMi2zzAymLW8E6oou4skMt6hF4ZYDz1dl2AhCgUoO_5MYfFazCKIeVCTVKtSCtz4k-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
‼️
لیست گران‌قیمت‌ترین نقل‌وانتقالات تاریخ که ۵ موردش مربوط به امسال هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102109" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102108">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uox_YV19fAFDhI2049w9ibmGW1jnmNoY8ZivgNdSZ-sXojkWYFd7yXNc3vqm81j6b3-nSp4E4HrCQU_ORkuGVulZEbtrzJuMAEoOlpJEwXGlx600LZ0MLM2ZSQetoSylTD6VyjTJcaYGDgcWlccFN8locHJlgMTW353vavOeFwjLRWujwYaExtEPA3Fex1lz9dzMCLavy6Ut8vDbXbb9YjhJIINkDoKmIj8kulKypQXcniMe-DpLQhzPWHPUSbX9v7My60ZZfUaTBdJvsjca0dwhboMALIIO3Qliih8ZG6vFU4hTVv8vG1a9OWBEg68vsJf7toiK9nbFwAANUf7CFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پینی زهاوی ایجنت لواندوفسکی:
لوا برای اینکه بتونه برای بارسا بازی کنه قید 200 میلیون یورو رو زد، اون پیشنهاد سالانه 100 میلیون یورویی از عربستان داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/102108" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102107">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/Futball180TV/102107" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102106">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ5PHv0NJ8x-JaOtIAdjT9RSDzY7WNb77cBAF1dMjyETgfYC92feMGQpOxMS_lXKYsihec4QaRvJ-TkWyu_UcZFhm0sadnayH9115ncPDhohaVoCuxxliutGvWtDfdS0G6b9zknSY-WroGjNEOmvUPDQfzYb6qQLQ_rV43PJbSFAXKMv77CEauwv0jf1dX8fCfmRCMtlLeFH-XEX0GPKF2CFGuJKHx5CdKziXXYvr_wa6tl5JjwdP_D8h4uwd7Y8-POrPXyLyezcVFbhHUZOkbyEepypdHhrDzjUq8QQronXn1wVWRCzL-fLXuiUYfFstB7XtAmjoZVnWKYdPn3l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤍
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فلوریان‌پلتنبرگ: رئال‌مادرید از علاقه آرسنال به وینیسیوس مطلع شده و اولین پیشنهاد رسمی خودش برای تمدید قرارداد رو تقدیم ستاره برزیلی خودش کرده. از طرفی آرسنال هم آماده ارائه اولین پیشنهاد خودش به رئال برای جذب وینیسیوس هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/102106" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102105">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvvtkGU0_NXASOWuTkYJIuuD0qA64xd6-Go08A6GmGpUtL_RLEn9Bec8IUtSVSCNUz9iTZdldWzGZzwqdoWV25jcZj0eko70uKXz4khNfLs3wgovEp1Yqc_J7Tt4Bp9uCngUii5QiJY5yOVseL6WDUDRTPnyaKC8WN9f6hnIcS0L3c3vyPX2KlybTnO9uxzNqpdc9ims-jG9QiOgBNBp_QEUzIrgraFgrMjyn1OYZyWTKVvAjIlHiQD5QsgkOSNE4qVoCAH_53UIaKe6BAAK_mNtIIQl-qbX1PM9jfEPhL5cGrwKMLvgXPj4L2pgtqzt3HMrnuE4lqC63usrrYKIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: باشگاه چلسی موفق به توافق شخصی با جردن هندرسون و دنی‌ولبک شده و بزودی باید شاهد عقد قرارداد با این دو بازیکن باتجربه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/102105" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102104">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHsMGu-BDLirHCGNBhJWcPLF2TQ_QYd3JR0Kx8bRKRve_NlkWq_22wnrR-9Hd-9ek6LMgfDhUZCsFfsv9HSyIyZHbj38Jf6UdADa_dzvrgemF9GFpVPQ15vVQPzeYAsN7lksBmmRoY3e7iByk5vS9S_r9Alau4zi6OWK7XHzVtrsBKjdpiVRK7HeGnhQPoVJKZWVocgoDtRoGk0_d5BH_wt5MGPQAyxb7hdG5w7CtB54L9bbUc8ISpWH6c7ecZqDB6ep0g0JK4hp6a_LfbFGAVelluEQXMjUDIRoB9H2S9ptaogy7Cn32lYpfwFlyEnqyQ0PsBb8XHQ1GYvLT9pBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇩🇪
فلوریان پلتنبرگ: هیچ توافقی تا این لحظه بین رئال‌مادرید و لایپزیگ درباره دیومانده صورت نگرفته اما مذاکرات به صورت فشرده از فردا ادامه پیدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102104" target="_blank">📅 00:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102103">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFQKwf0uF94f8BBXeH1L2g2iyl8xPKQYn77uLysDb6a5XCCQlFV2XUeqqwQc_aqmPC50iKC7LggCdujJj1nqu7aBvYfo1H9mAeZ_PZzx6AmHodZ2t93uS9j_6NZeiunxB8jVqDpVto5BzQGkaRtX6IqID2umHOQJd02dqNtZm5cTfUbqOShIDILLS9PqXonpc_imtDykQ5eZX3KcGbKFN-YGbE4fFjLX2kghyeR7MzpJ_13v21mzsyUHZMsF0uS7bfMcaPnlb1VjjLcBaQnwYyjfr7kM02o7a2iwqRQ2U9WplxkHGGDEh4P2WUm8AivnO8f5DAIAvM3UmP6GsC2ZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: مورینیو درحال تلاش برای قانع کردن گونزالو گارسیا برای موندن در رئاله. مورینیو به این بازیکن قول داده که با وجود امباپه،‌ دقایق بازی مناسبی بهش میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102103" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102102">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1pBgSJc-uJ-Gd65vg0tlWcvXcHeLlaA2WItRT6_5ASqnmpNjPs68k2z60zuJ9v-CQdpWhH60SoOf0awZMDQyhk7v0j1t8y6AO3HaZpn6Fd_4vBH7kTfhNbHUe33CvsxBroCKNlsBh9r7vZjmU9j8I6qb623djEvxajbC_hxhBv1HrwT7YVuzrwaPn5rXGKVbOl3N4nU7yPumY1Y-MK_qOGuiPVRICyzEAtEpQB16FUr2OoX3pNvoLwOMRdPVo9Esp9bqxF1QfmqHp4xBqkoZCeVdvINKm2fwcE47QinbVAw8dWIw_50WCIy2VDmJKG27dmm_8f7xChyruiouJ0cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
لباس سوم فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102102" target="_blank">📅 00:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102101">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=OSbmreKVuYIq341Bi_KdNRIt1afzru83MHVJFys9njlTfai6s9a0pqnOAiBY4Jdv73tiXy8bnil-9UUZsTyxncKeQqAc13g4Ef0r0A8BFvcx0-eYbSKMl8LxeVNv165wckmn79Wa_zO7FhbUuHkpSUaNq8dU_59wyO7tNox_ybXf-B3ZS9L1dq_V4kO-7ARrTB42GZxZtn6JnV2SyTzA1muZOOEVc3onPhXKxZv4fjfaH3bFMUpLaoY7O9j3lqYNKVCu-IW17HmC6g2du__03p1naux3wL8V3Qsmn03BSuCoa-Y4BdumQsE6uC0CQEiDpGjXwW3w6MC-z6ZKYpF-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=OSbmreKVuYIq341Bi_KdNRIt1afzru83MHVJFys9njlTfai6s9a0pqnOAiBY4Jdv73tiXy8bnil-9UUZsTyxncKeQqAc13g4Ef0r0A8BFvcx0-eYbSKMl8LxeVNv165wckmn79Wa_zO7FhbUuHkpSUaNq8dU_59wyO7tNox_ybXf-B3ZS9L1dq_V4kO-7ARrTB42GZxZtn6JnV2SyTzA1muZOOEVc3onPhXKxZv4fjfaH3bFMUpLaoY7O9j3lqYNKVCu-IW17HmC6g2du__03p1naux3wL8V3Qsmn03BSuCoa-Y4BdumQsE6uC0CQEiDpGjXwW3w6MC-z6ZKYpF-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تموم فینال هایی که بود
میرفت تو نسخه (پرایم) خودش
و تو اون نسخه دو تا وینسیوس و یامال رو میخورد.
شاید یکی از دلایل نتیجه نگرفتن آرژانتین مقابل اسپانیا هم نبود آنخل دیماریا بود..
🥃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102101" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102100">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل سیدنی لوپز به آرژانتین به عنوان بهترین گل جام جهانی انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102100" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102099">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RihQhs__3R7GtCRLZ3b7oMPC9lINxhNQhMF9mJMnLABW0L8mfatevxnZdMIKlvDk17YvIWyR2K9DaVerkxnkmynesqvuwL9j-_UF1Qg4AFgfDyPLxYG921XZ3ncMaYYqCYEQI1P78JXATLTz_I2dLCJGptwez5MK_upgy2Jr-a8z46pXRYlk2T6UcMNyQq2Ef6M_kdHrBWZGr9WJ5lnXVpvJraM4u_YVi1C9O-1xLcSIo9v0o8Jw3E2ycmFxS_JliIIuPDJmGotmF24QXWDISkCtnVI5Ub-A-wIoe9RNq_pZb0wXE-lysb0V-XQTgpY1Qc678CXCvwr4vCZcyGvpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
جان استونز به اینترمیلان
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102099" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102098">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLyqK6id4V-t-IWovRQDl42kjBRwU1XpkhRMwZ1K3lbuAOyUvdMLPd98yL0yCGr_DaC-vsbuEn_asR-HsBBBk38C35sRlvjz5Sn0KOgLXrdcdxotBJZBloUhFZscDGY4dSyHglg2VRBbJovTwJx7h7RthOKljyurVw9phyCMD-NW05Su9-TCcQ3d20Z-dR-SLGy8fG7lZ67yN51OP61OByyG5IhRijqLXwtclV2i-1QjN_1D-wkXyA3hcpV09Zv0mopNHlV2T_kTt9wIRTfBf2EFrRnepQM01Ho5wWM5yJX_qOQaKaajwiCZLL_ArBqOK6By6jKPjK8UDqyaUwJtEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندریک و خانومی و بچه‌شون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102098" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102097">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js9Ad0nTl9roSsP8ycnHHdeTI7xD30XLyHaElqGG_qosd-NuAezsmIBlxmzJBld3u9dwzb7SEPOyGAREylwsU2EFumvVWZ9S2tssDeDxUwdns89eOr-cJU-IzSBxBUVGsOYzTif7djIrSg-cbqS9bivho54B8NCAjcTIi_IXah2l2C8JQ5BTKnkwYGes7kgMmv1UBUDyKPbtPWY9EWqY1oNCTZIHLfvggi5T5HvpZBIerZiLm7sagS2lKjYAiOD96jDHLh-xJYQw7JnRtE4-Pjio7biBORvmPeIYihlrHPeGvqRu3CBfGc2PucZSN9ktrQ2arsyegj7WKLkrUKmDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
جیمز ترافورد از منچسترسیتی به لیدز یونایتد پیوست. جقی 3 بار ادیت زد تا تونست درست بنویسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102097" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA0yZU_bjYgQrcImRTOsVWQ48FvZ-2SGuTpGQHiBWo5QjXX706EhhPAhjAFi8IxpcKEZ-_ajRXxA_bgnO4yfGhrpXUfR3eRXbjEn-iAFesmsqAPrilRjH09DvhD991E_NnGvOl2vYHmSWDAdaSB3gt9GdCQXJFafjv7XHlOo20A8vdzZrTL5tTrNWKiHJLZw8VQ-w9e7Fz-K_qqoefJC7BKSFT1ur9k1FmM4IwD0aB3mjDYtOHIGY-JlqwpWV7BEe8C1Me25Wcjw-Bs26HNBWy2_gMPXEPlprzef8u6onNKowK_DTGkS9qyJTxLb9WvjBczO_wVEE6VaFZVkDFvL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW_cJnSrzYqdDbtD-fWJ-snZhQyYvQ7aYhm3IrigwJdcJg8O9pSK_x3UbXdLhxPbt9g90EMujuXWrPiWC5-BKigjPxpb9pfGePUyPCi-OJVgjxttWgsWtNID_M6l7m8NBkgkcij5bcZqdQk2gvTD8mJbuPEhvbUb47NCXBjuCvCtf4RaDq5B2vGLGUgxHY0Z5467vo_DY07Nbc2WIdLZhEOUbb_UEyZ4rpIEr4sJo7si_FafT-FELyLTKcHrs0tY1p0he9IJezkAoAamUJPJwYwtknQY1_fOO4LphkM2AHWzZcnoFyE5mOvcZSneLC1u_K_p88m8KFSmB0QsUHpgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQjs40IEYNXOK3vqVKyY0z3wsF8XCgxcxR2q0v0k-L-E5bVLa4J222RZJb30DyWo2fm8LaT9khDp93gAMl9IM2OWJV1OVyM95gUUeY0uqu7Z4_Tb0MR2sspmjkhDvmbrPTpIRifNKe1xahExr3eXyIwbdNGXeIcLQwhX90YMBHZfbkkB7WbjPk6pM3IjuIUAWFnk_uJM2xQOeDYFYfXNDf4TwfXIBj9CNVk7Ctd9zqFKqwu2y21RuU7X3by06BBycdE2gAbqswbKccUzKPAdQPY7-PjPwtFG7WwsW6AO43McBFm79eyio8fWNsiTBa7yTauRLAmeMiEPMWUWdmB7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZhcB9WE-W_-6ybd_nOwmeBA4C2JqGv8tzmRoHY1UkgZPRGRwYG8PmV7v1o3ElAqEGRW9hLLTYyPv9z7dJj7Qjt2d6Qea7zBQP4pus8imlGx6EtBzH65jdS10PxerdKlMQgLvuwD7vWFxLXrQMu_Vnz2VLF-3wt_HqqZVpof_OjHGtgpKzwC_Mw_G7heWjESKv3hggi1XtMRwnKBeliFidULWPSwPqwNpI_TgHCZFu3P7OEI_yajU31KLxry1diM4UHdKOjpcwKmHrgnSFG_e_xo7Ueno0iGfQojGDyuf8xvwH2Cp7qC2cGyYPVXucJ-iU_Ru4b-eEVE0jvyW6idLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEWTo3NM6WoKMVaB7-V02yR4uYUmmA83gSaZbx3nnbb5sXWskAL_QHouS61sg7krnybGkRdQrdcLLQHku7Bd1RKZGI_qx_LI1iGVZNOl46830Rf8CGZhiVwToZaPokA6NlBC7CjuaUQtsr3HuciyyX8Pkle3HlACjc2wcSsl5J1yyYKveduXLsWHvO5PMHMPt55qg2rW09I5t2EtZuV-sBFcOarBaXrBLQSgeqPI-MzXnNd2p7dvO0XxAZfC6Tw8GFrqpGfSJ7Mwh-hHhTq8bjqXD5rbje1g21AJw1kizhrPaIEU8_woTh3XVpRDuTA6rj5ODJbbMjSZ_0wPMsmGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dnu-JOERf7PjaUTIG0kaE5tfHOOAyFEiIKI3m2egDRWSqDnm8VFTKMJVRODTmbkNHUFV7qBDLwF10c2mf90K3iUk2gQq94DnMyCaQr6SCDMN6rVwyNFKkzukTogZZyMReALRk8GcIYHbrTm9kcsVO7spW9esfp-TVh3rQnv2O9zXDg5ExdB2_g4C9XmCjdCujkIJWQ8fJYhMT6Rb-UX5MmZycJ69ACeKMcSgRTNkWufedpu1Hr2VGmDYkKEUJouj_SDPgoEnRglwTb-ECxJjlcIWdIoUyV7OVn0615faUs9HzYUvK9IDgLrPayhfoeb0nxKTRYsfgnV-E213DaODiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbB8yRwn7hytYAYdczDSMLH4o26_b2obI01nd1CH8fSPFN7oBCDvMCezK3rVbXeApfcl_g-2Dyg43YuXkilhobHX3aPPo0Ytm8WmG4hkEhtkDNG1rJ4yQxbHgago3P7x9Bin49Yx_cnqSxQkwCB8kz99GNe5aTP4Ut1zRi51MPEmHE1JIP1jocPm5VIREYb9-un9cgTvvWusQFD9ZZhUAGuyy1flJzxJSlEjosTvCWqlckEcT7gvDlp09DhRcvpSx3y016VLR0FYXeSHPcojkUiIsPF2fMgR6_mTQYgR1pEo1HIJZv0Yb6D_vJ-ARifjkxtzudPqTOzKEgU9f2CTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjbNAPQeFj--i2Y5rCXYf0uihH2yGe_Qpn7ANUjDcRT0AgpVhqLFFxZFRf4aFlOSXvTvDz0_Yu7PTwWaMU0Zpa3Zml9TO9Z5rQrArhGxwsoLdwRPAPYW5UwwE3hB4YuraJehBXBbaNptGC_IrPbxwm_fHHfolIkvAr_cciw9D__KDijeZSf4gv2fES-KeIM0igK-e9YFnBdw0hjwsw-xTgfI5eC_ry1l54vnulyPtwibHFd-HYMC4S7kQg2hTSEvQNhu3AjuYhCfqGiYKF9YIrtub75_gkj-a10nl-edYk4RHsiczDSxfirQpjuTRu5-I8cp08EsJRnRlKxPt_6kTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn-iIxgdn3xOQ5LMuOInda-U7VGNDvvMDy_qMXGEzB1_Q2IoP35sV50kWdAPXqm2KATCyeXBAjNIfR450R93BTZVNn_le2_unW1UQDUPeA4yC5qpZaQI8_56fgzZ7uGKcix1dtkqG0S9AbeO2dpkKBsPiKKrnKU6kCER0xZbjYetsh0Ijrp3jhxWfXUWjnpWegYYhL7R0RUXWjxp90-n_FhzGv-bTAlUJo-SZt5QuYNgVANPEUM7rUC_Mm9qHgLvjlWwew49rOwKbEWvxunrHrioWr5LsPPrSsUVcneayvZoLcaMQt6UD-LFyi3ZxmSeS208DeXb8_xilJCMdgfDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCs_-goFoElTpjsMvrAR8BuCiboUKjgGn4NGIN4htI726mEGzunl6_9ROlIdBNKA1ED7NcQGbc89SSqBGfvOy7VeRyCmDI38k6Rj06fkCAhEfJC6nHpHj0DTVuO0m3wwAQzs4yultUR8M33RNsoi-Bw9gXZJ_HIMkQMMxMHyStQs7-rHmdYTCETBup4EUOst7JWtl5_mDA5NeRUG1m9lpBHAdvxuRhiALNrPRFEk8lnF5suRNYt9bj9XnoYywPe7Yy5xklhkK42xJNXSeN3JFjycuoUA32lhdiN9SC-4hGh7dnScj4TvTGqijGoAdKUy9vk2YoOHDggFiH82hEI4QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBL75KG8JpU6hE0f1JJxiJjb1kdc5pvWRgnb4ViIP9k5P44oSqsZUDkIdyFm4VcELMUY4FV3VcIel_4VxHB1RR8u2wVOlYGfsIWT9cpiPXjuyJF1xCB4CHMkWCESeeu1Ks1go526cfgnqqZZSAdV-M1EUrd16aQhlms2koMt9HZSbOM6g7jI_45AKlk1guvOnxU9JMEa0V897doZRylJwXLjlk6W8noYZbQbypCiGrMWapZBSqmPn5vBotpVISZij5v4vkV_8SU7TlXPXsWQyM_NX8NJBhCzHKsF_0i_--IzuZtjTDN4AdwZq5KhPB8r_0k7QCWgwj1f0D1gdRQGJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf1X15V1yQuVzBCNC8X3L3hvHx3CSFL8WLFkc58GG9ZVBr9CVvkwJCsxkwzaXxZuN7rqn4JjcbVzUSKWa9xQwEpZlWD-u5NqSLCAl9sgcA4IangocySCuNLsNMK8EqoRX0y5Nx_YrJ5yFASAP7FvYOtg30O0VOcq3trAnLRVxfoCQYK3dxPK1hjPTt_B_Q8IFOkal-UopS2X9ee_P3qrMRYld6tB8eWfQ_j7C-NLRfnu_U540SW_ZIJYC2zUPbS4_UAIYCg02D9wEs7WdOG7BdzU0euuxdMW0OAWrfQ8aK_ixIqOaGXGVJoYZv0EpyE5i9s1eqj7E__8T6wLH8aAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⚽️
امار سه فصل اخیر جونیور کروپی که ظاهرا گزینه دوم بارسلونا در پست مهاجمه
جونیور کروپی ۲۰ ساله متولد فرانسه ، پا راست . پست اصلی پشت مهاجم ، مهاجم نوک هم میتونه بازی کنه.
💸
ارزش ترنسفرمارکت ۵۰ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdHG2lJTESeRDGSnFr0Fghgst4M0yjENYMN-NwMnPY59nuBQY-mP1XXCtdwYoYLCbaluSTH0P4yspzeyeC_jEA9v0kNVMiGem-YbawMHkuLHPDB3xZTg5xdUW9hnPz8LNx6Um1nfuz1g9dw3nOxyegJSOvnMUcGjDJcsfWDsGp0fDd3xrOMvoyayqVApJSLji-O7CuzpTUaPBpgSJhPJ5UAKttHiLhv9nmXf0Rrbcv0NxTf1MvzVIiaEe1MIS3OLr0xQkacz80otnqSq28hRGXlMmHMAkfUOCVDrGI1Xa0P44KqEsBcO6IaLDlRLvgIsWB1GncogBRG4Rofca2YIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=PQYBlOVv5FVbRxT4VK9cbvr8mL22fodY4Qs5cuic0X-yCcvJNn5RilOCFUmlqwg-USnqvnEmpG4gyUE3OD61KXtKYQO-RkrPTtO7_CyvYmaLwy-qrcGOvRX71Fo-nnZYjXK5hzlSRAnKcM-3usKx8qVfsYJBKy70Em9BHubBXQrSSFL9Z17q4CsPepBx7s3vQ7mCT-zkBAKy3zupshg-1PDxnpkaXT3xM1ykaW5TmapshEhxYLgk_8sWIHwCuOHowY5svB9SEimEpSL5qzavZDLl5jOs7mda35_8DbnE_hqtl58QX5eW-S5fN2wi2BJUjtWQZch-tkIPP-l7LCKm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=PQYBlOVv5FVbRxT4VK9cbvr8mL22fodY4Qs5cuic0X-yCcvJNn5RilOCFUmlqwg-USnqvnEmpG4gyUE3OD61KXtKYQO-RkrPTtO7_CyvYmaLwy-qrcGOvRX71Fo-nnZYjXK5hzlSRAnKcM-3usKx8qVfsYJBKy70Em9BHubBXQrSSFL9Z17q4CsPepBx7s3vQ7mCT-zkBAKy3zupshg-1PDxnpkaXT3xM1ykaW5TmapshEhxYLgk_8sWIHwCuOHowY5svB9SEimEpSL5qzavZDLl5jOs7mda35_8DbnE_hqtl58QX5eW-S5fN2wi2BJUjtWQZch-tkIPP-l7LCKm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان کریر سرمربیگری دلافوئنته
از اخراج تو تیم دسته سومی‌ تا قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7ooaVI_DvXbplMBM_mWIcSUaU5gp70ZrlGnwfejtpS3aK7AXhdlkoqIjZA5G6EpWHLT87iTRchVuHWurSY5KS-zAHwkynxPDzQsTT50lxCFUhzciut0Lu5135VCbMqFtNnDjX7h87VKefvmutT325_oJAeKgOUJd0UQImuNLZN_emiLSuYRVq1zc5bTt1VsiizA4ITp7lPzJB068tvnKqzmdOic4hZL1BaMvFSqfBP1_9jV0JKvzM_mfLu4uEINk6WYofq0L3lMIGvT-Z0Ust71L8k55HdCBU7MF9Hj5k1YNbKJdOSgzVyD_vgdxXdg9bPvjG6-ZH4g2SLrCsVjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru09_HfwE2SPkORjfDJSIa6ce_MJooCx5CijpBlTU0ZHmOCjLcYmEYnOkI_kZZQHvUdI7SFWTDoJCQo3VE08ae-UU8t0ADsHcYp3K_G2aO44KECshjiJSgTFm396yIukUVv1o2KDqRUu-iSGt1paqiri-Z_sUm5-ockCsHsEABPRXh04GtsdiJV85LNcJ2JdezcTaj2T-QbvKwvVYcd1CHM3tgh8DMLaFaKjaiFLJdt6POkNPGDO15SQShh6EJAEj_SfIzwAg1KDrG8emK9N2l4_J0nCa5vRAx5DWCsNFIe-q0b1gyfPFlfx296hza_hlmlk1t1TsuqbfvxWSmO3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-kaq3X8DHKyHrA40cN3pXJsY5ko5nSUGUi9gCNpWgOSY-VL6A5nKjPCm9jcO_f6hq14bgKIUAt8PdZ1nsKUranF5Hr720D-8dg8GtBogKM0mqtWhX9oqAEsTOM3hqhU3ObtaxoI69wDapLLlJcRtmE6zaw6Qdvdcbqen43ysxkw-q-XvARaLSA7jKMSYpCb2A2X0lGxXUT8uSh6yIKOeGsTanaKlC8sP7mR_H8J-MRZKi6yVLlIGsqPm_Ad-9V9PBdv4I-7tagLf1GsW_cdeaNb0IWUh_z025yLsKJQp-wVi4N5U3FHkTlTUb3S9QVMPqte-M2luEeg03DD8cN9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی اسپورت
:
یک قانون جدید در فوتبال انگلیس در مورد مصدومیت‌های دروازه‌بان‌ها اعمال خواهد شد.
اگر داور اجازه دهد که کادر پزشکی وارد زمین بازی شود تا به دروازه‌بان مصدوم رسیدگی کند، مربی تیم 10 ثانیه فرصت خواهد داشت تا یک بازیکن از بازیکنان حاضر در زمین را انتخاب کند تا به مدت یک دقیقه از زمین خارج شود.
در صورتی که هیچ بازیکنی در طول 10 ثانیه انتخاب نشود، به طور خودکار کاپیتان تیم به مدت یک دقیقه (خروج موقت از زمین) انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLE5THPEjNFzyS6MBdKuXMoI0IFxLaDkEBYUnVobhk0DaUKXD_OPLlUUnYHEII95mMPEuZG7ulQP9rks7s3oQCs8QJpyEb9_jHEF72_z8-eirWjHDPJ5UGKYRqFBIwEiKDAlpSrAUPHAfQ0g0izkt6tbAGqZwHY_PdIZAN29QtZ-B1OWOFQh1dLFnRJmkJCgj_Z5VPdoTI7JdsgYXKGckvAYUtLgl0paYSg3JjU4QNJpJfq4VEmne9J1g5c2YZ_rPPxdymQs6cEceE4G-v1px-0-i_Q8LCN7804MusPbsBdlT_Nf8Ib3hgLBLwQDnbTyKOlLX0DLJ8mKN3M4Sbhnaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو:
‼️
بارسلونا با افراد نزدیک به کروپی وارد مذاکره شده.
⚠️
بارسلونا با بورنموث تماس گرفته تا درباره امکان جذب کروپی پرس‌وجو کنه. بارسا یه سری اطلاعات درباره شرایط بازیکن جمع کرده و چند تماس هم داشته تا وضعیتش رو بهتر بررسی کنه. کروپی بازیکنیه که داخل باشگاه بارسلونا خیلی مورد توجه قرار گرفته.
❌
البته این انتقال خیلی پیچیده‌ست؛ چون بورنموث نمی‌خواد تابستون امسال بازیکن رو بفروشه و منچسترسیتی هم بهش علاقه نشون داده. بنابراین، این معامله اصلا آسون نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7hT0ZAEGd1c_n6nEFg8KbNNdbX8FQOX6mEO3aMRH9PnZ0qybs1GOk15C3s5-BHW9FO_5evC8hAoyVtkamftKJkK6tXdJs-O-Uev_FVsRHo_DPZVVWZVYI7GxxMSkanf5Vw8uTQcSBcIYopvQF1nB-BJU7gv1mqLIbms3ZTC49mHKJkc3OSZ9sTHIyHtyNP943FnL3VbXzNFtg9osSclqNN_UH0WqM0tFBQA2cgjWrJo73pjc5_wLlgHyyu0noXoldD99NItxI_31XwVlvuXctpiUhJpbs-GWL_DYJk4N3lmNyuPWdacFgGBo32LlG3d7Sq88CccluDBGyAZDn1zLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فرانس فوتبال اعلام کرده که بردن توپ طلا حتی بدون کسب یک جام بزرگ تیمی هم امکان‌پذیره.
📊
این اتفاق برای این بازیکنان افتاده:
🔺
جورج وه‌آ در سال ۱۹۹۵
🔥
🔺
لوئیس فیگو در سال ۲۰۰۰
🔥
🔺
کریستیانو رونالدو در سال ۲۰۱۳
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czCXJ5f93YtMacoNjSm-GhMLzXLbzFewc8I0jdf4mkFTQxxgFycrXrj6KoqnqRYBE7SPsOQAECgY5-wEI39DY4iwMIhYCWPqrCK8TNqbx5QtJnvdZ1tCH6jF95p2xEwn6W17-PM8S-z7ZZd6RbUaMJepjdLqodPx8pygbz-WHhGTpttLNZaffrc-OvsMtY6VuZSLL_U53CGJ6VAYpapbkdWXDKlw9cZkL549WEjz7tOcZeOcmP0BzE6cG8khjnVTrI_T0PdOu4sCoJWN98j5zPJWWexiB5a3gBf5QR0ZDe1Ph9aN9by37kvRqZg_dgzWXCm3JeCmUXWDm9VTMK6moA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm6Igoe33qI_V3q03ogwEOWM5hwbKN6mSFLe4pvbYhYf4aiCEuJ9GzB6sAHojQ3U-QHy0ZuVfiGjLY-C1izF6AUuui6DIFjkNtjODxHZO0R9RC-eyR6m2alrUJ26mON6pRYdc8ytsJ4kK_jQd5wvAP17CcExk_MaW434dsWEMxAmPG_HxkJjlVqnKr90UlyL_A_7NBZZ86v-HR9SxJuSEyfKiXxvPDNxnf-KRPvK4niviJBGM85Hg6ZqgvSHdxifUiPQqD_lOYw-oAIql0P18_dbRu0RogJKW81Hf4-o1FRa0GPhH6ODAKyVuSiL3u3DKhUM-7LwzGSH3mlCqtqR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaK0Y-1ugRsOnORj-Hh_jUTfFg-8c-yyZnAMvBsNcEsjhCBcm8XwlQwQgfMVZX-MRKuQ5HhXnzkqtqdKTYQSZSh_BHGL_m1i08I6bqDQJWl64b4sExC-FjtNH63Kj0XvJeU7jrkEbP92Pxuzogy-k2dvnhqfTSKaT8ycw1HaCgxHvMlHgl1JY4ZJc2TIAibeCcphhktQztFtQAOxbbq61mceaYcQXZkIeQvj-v4OigANWO2rIQJzwxcaNZ3W79jNZm0WOXc2bdPLU07ynABsRuQ67UwaY3Gn6TWxOoDga8VXsoKEHbvOiDEChScaGTFUnuppaJfwwqCz-grBzI7VNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102071">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy2JL5U7tDdGJ429KDWQN6otYVponUOQsSSt4YFQDa3WMOjQesB6O3QFKo75Pl81T2Vy4stjr6wtQLcCqmMfsibqIRNQiL2e41glUtvyL4y4VbYP58weK_Mbtp0oITBmBrnjqPcBzfNKeCmTWoP-l1xxDPuY8Gnhz11Obti-CFeznb2eBylt5RHERAeINU8C5tegaouWMCIi0uUGzPsl78DkfZefC5SVfF2WmAn1E8pqqA2a8dSz-aqUCsY_f-TIrxHLOVLqzBaEJByk8NoyEz0oShxeSkySE4vqR-L7RH__WNgnjj2D5aFF6f8DGSQAPaakwicVMoFxr3BkheWGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور دیومانده در تمرینات لایپزیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102071" target="_blank">📅 16:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102070">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=lDxoO72zD9_IlJyAJne15zV-KBFKzokxJxTbFWioOc0ZEMQJ8L3eXRbbikuqscbNaj37Bgxf4E5HjQfdsOC7JgkTLGnIhutqjRLNaZ9i4-WaurcHJenwctSIDhY8kX16f7ZFw5bEPOvlvjCb4X56K2PGsyN7NeJxQWo06zoBXRTuWz8cqNOkYKejYCbvXiLRz6hONlSo4V0kni2aRQQRAIs9cXw50gNDW87nfTPvqlhb9iw_WoSq75CWvkJMlpYa2jPNP20g4l23vnlM2qbv7M_EeR-nibOSssybXX4TWZzdUFHRol5-QEnoJS_U2CefBvXyudLWS6s0MtwXjSXyAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=lDxoO72zD9_IlJyAJne15zV-KBFKzokxJxTbFWioOc0ZEMQJ8L3eXRbbikuqscbNaj37Bgxf4E5HjQfdsOC7JgkTLGnIhutqjRLNaZ9i4-WaurcHJenwctSIDhY8kX16f7ZFw5bEPOvlvjCb4X56K2PGsyN7NeJxQWo06zoBXRTuWz8cqNOkYKejYCbvXiLRz6hONlSo4V0kni2aRQQRAIs9cXw50gNDW87nfTPvqlhb9iw_WoSq75CWvkJMlpYa2jPNP20g4l23vnlM2qbv7M_EeR-nibOSssybXX4TWZzdUFHRol5-QEnoJS_U2CefBvXyudLWS6s0MtwXjSXyAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
عاشقانه‌های رونالدو و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102070" target="_blank">📅 16:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EIlrwTDRtln84APptTTq2ZvAH9Ka7P4vDnYb_-soyYT5kodqwzuNlWcdULa5Du-4QpT-9R7lhc4tN8GxOaIy0w5bL9xW5T2vuDN3EEBkyJlkqvdZ1_LrZJrFCzPP5uQweyztf4yD0GXMFInRc4kjuGI0Ko8KxgLTp5NfCO1xtkVRKno7JEE9LPROEnTsby5CsIwYW8bHtwx8fynBqLpfR4SZK9aCqEQzsgxP8LymltogdEDVH6K8hf5izsZQzCyqpGslxcmH0mQghwl3h0kvXRVXSraDINCpxilP-mme0CHYoAkq56c65c50Rn-MeRakKqG-7ki_iJLINqdDR8ph9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hvp5XFRUD3HOzAEXjxicoWP050BHxP63MNqc349yZXfQIMOn2CB_9yPENxSzd0G88uxulDPhHYdcNYqzX6w94XYyTbgwJeYWhJmr9FO-QwaRgYIlZWoQiIAGTV3ebzsgXJCPxSCUlL8UZ7KNCQuxeyFUwfZyO-MyqAX9huPyvaVIembpaGzhpAtxYReN3XNczV5Q2UYegv7zWr_g6-180_Qzr8Dbu3a--3fxl8zrD2LZ9kT4mKk4ppdKoNIgVJuie72QlqoMpwun10eej5TzuuxhUg9vFM7VLP4jq1J9IEf8bEl_s3Iz5DhAnOk_Sq5Qh7G6amu31-kNtJJA7Ha6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uV1FnfuVjZJynnPHJjBHysm382iFUMvEqxvkpzVCqjeRPBULTtLRvBNY1mxGPgxjW_J3WF0THGQhfakzP_29mZaUVIn1Yf7mnuhaSYuEewfuGaBSbYo4izaX7-GtGdHTMPW3a8AqIr-m1Ic8NlQzUkg-pqj_iN_-wyyhxFkZhtok155ucgihVYt2TwXs7hNpkcDE_bkzBvthVL3yz2ilCdD_syt6otJgBLmnT03jx-BATE7_dmt0x0r4JyLDJB4XV41r0DuyFBwsV859NCX0wZ4huJSN2FYg9xQFYXnNuX6LQvBmI3AgZ9rcrNGf7aILYlHsnRGfyKD8ax6YkblU2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32263398.mp4?token=IXoK2pDQHlT4EY8E7niodUdvYgPWdDyvP69gH_dwgETUl1itKJY7A0aAtTCdP7jBnxFRG51ML4DO0ksbq--m_HKlQEJZBxUNiuEgQ7DsB_8FS8oRLT_6pj-iaQziseUnr7l9xKGQyYwsOq1RsAt9BZ1KOBqDo41L2EGu0-aXwWftxk_DqMo_ivmVRLmYyniTqFKF3EEnfQtvvaNA7RTQeMTqYyKT4MHQZXDcufNCT6BjHYAbwjpX8cT1BbDWpnOfAc0yaI2xDZCtxX6-6dVdiVDAynD2hh_eWOIzuxt8YGDsBeAxY-Wg1918KRIL4NJdz7i0M4yhuavssSkfr77kFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32263398.mp4?token=IXoK2pDQHlT4EY8E7niodUdvYgPWdDyvP69gH_dwgETUl1itKJY7A0aAtTCdP7jBnxFRG51ML4DO0ksbq--m_HKlQEJZBxUNiuEgQ7DsB_8FS8oRLT_6pj-iaQziseUnr7l9xKGQyYwsOq1RsAt9BZ1KOBqDo41L2EGu0-aXwWftxk_DqMo_ivmVRLmYyniTqFKF3EEnfQtvvaNA7RTQeMTqYyKT4MHQZXDcufNCT6BjHYAbwjpX8cT1BbDWpnOfAc0yaI2xDZCtxX6-6dVdiVDAynD2hh_eWOIzuxt8YGDsBeAxY-Wg1918KRIL4NJdz7i0M4yhuavssSkfr77kFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزاله اکرمی بازیگر: رضا عنایتی کراش دوران نوجوانی‌ام بود
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TthiwOoHrX_l2CM2l-PAb8Rp5fAlaoWa7rzWXWnsWrcjZvxfy_MehO0vwH2s_E4UB-5ATAvEDPyfyGsOgp7jrgA3jpMDwMAou5aXSI9uiMJr1_RaZ3uBHx0j9_-GV9XBNRdR9lQ1XWtgnqvlDGHLzGa9YwHPOCnFFAeIUkpa7iNfxSW88oyZNDuM0bjTa2-GmJI-QSnKdRnlmLA_URSNYYLCtIdJytW5w6C7TPKDcRJzbncNFaCwb0lNCgCutmInjEItqKPj-EzKv5nKRTd-ePWYgBN89O8npHeFV3UkhfiAAxUpYmF8LRsleHtIE0OoO2v4HX2jFTlAZ3d8Xe7oQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gewSTfCrltUrI9O_jcsBL5pjUZCOEbe4kYoUfxCTOmLOgaopmEGsiwMv_XqNllk7qOzgchOPPySfef8Kmwmx7LASNkJhsJixirs_y7D2THXSmbaaMrLEXGxA1Y55xAJ89AcJakrKQnckPD6d4QmTrwiVotjZvFOz58Tp2fB51cTNg2XSnqIJ701Vc9xakPomq0tMR_RkP2Yx5wXiFT00A7w6NkA1TmaKA9OUwUYufKFB_0pnojA_vmQGsajUTBqazMnO-K6G27Y4CsccICR6Rgo53G_YVpjsm0KOTK343OMU9qcKYUeWBO9bX4YVIja-urf0B9aeKyP2Y_p5_Kejvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRm8qHadglU0CrtYGvPiRi1_4Qhi3mlc9bGUf3ILb8c7iXd9dyKDGEHq4TxtDcfZPhDzYAhT_WZdB1HyP3f2fXmrolf7e1dMCdcdNlhCAidcTw0PDT77H4tA0tJzkM6HY1XM2CPtG4u4MTQCoyy74L0ZoaaFAxI-_d--UUVNvMlBOrG53GDfPjl4EdpyRy3dz7uKG-nXql_XeYd4ZNGRTj_UmZTtPzTUYnWLVmujLeoudir4P5Uivt7a4qU4J1nyojob_g7YWD_y2rkb3pMce9pPW5NC4xQMvWRTfHSk2_DT7CI59KWO0uxEfCYv0aLPOoM8O2M6nxzcbKAGUTdt4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=oD-J7evEgAqxnUQfUSk1c_j413QieFiyJe_eRPaG9m_n3c4KMXv1B-pgWPwfFyEDYDTnnyFlWSKp8wV31XYFLLViFGoPNjx9-SpDdBgBOh0oyXZgdLlc_eWxHQ7moKu4s0cTMY92htiVwnB7OnW9ZplPKRj3vXPs6d9ZNOUUBKFgu9yLIMYSMie77mku7oLN8jcQQdDdGibdwaXqYuVxEqRtp7WiQZOctKT-4NUiyRuWuro4FYiXC4r_i0jzomClGEHmO3hhaoBK3MQRT7xusstF8Ycyj6n11_i0aS4-GHwJZYJOMHXhbB35RYchwFpySOEf8ANZCBLLLc8c5hq_Vio47YnXRNCy7Da8sUUJVT1Krl68AgNIh9mXtLsEywkM5of9xnZkNu3JvQypKRLyGgPD3bVA43zJHeILBYDlEmeQq0qWWWd2cAlOqZZeYqJhbwevw20gz6CFJgje3p_OxJpahlLxEtFRUNfLKgWbqaV_Cde6tzWxtBBU1JJMHHm5KZVHHku-ibC56X7xXut9IlZsKbXn1CATH4BrPs3tuKkjcmKjOiGPC5WnXx0dI3xT3znNIPuQlGpEdvNa7nlthB2wzqnX6BAaW9a7Ve905ebXhUgb2ipKYMTnQagrjzLfhrPMqyiWXtzwnBD3exEXUCNjxPmmr9ItkHOnZMxG5JE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=oD-J7evEgAqxnUQfUSk1c_j413QieFiyJe_eRPaG9m_n3c4KMXv1B-pgWPwfFyEDYDTnnyFlWSKp8wV31XYFLLViFGoPNjx9-SpDdBgBOh0oyXZgdLlc_eWxHQ7moKu4s0cTMY92htiVwnB7OnW9ZplPKRj3vXPs6d9ZNOUUBKFgu9yLIMYSMie77mku7oLN8jcQQdDdGibdwaXqYuVxEqRtp7WiQZOctKT-4NUiyRuWuro4FYiXC4r_i0jzomClGEHmO3hhaoBK3MQRT7xusstF8Ycyj6n11_i0aS4-GHwJZYJOMHXhbB35RYchwFpySOEf8ANZCBLLLc8c5hq_Vio47YnXRNCy7Da8sUUJVT1Krl68AgNIh9mXtLsEywkM5of9xnZkNu3JvQypKRLyGgPD3bVA43zJHeILBYDlEmeQq0qWWWd2cAlOqZZeYqJhbwevw20gz6CFJgje3p_OxJpahlLxEtFRUNfLKgWbqaV_Cde6tzWxtBBU1JJMHHm5KZVHHku-ibC56X7xXut9IlZsKbXn1CATH4BrPs3tuKkjcmKjOiGPC5WnXx0dI3xT3znNIPuQlGpEdvNa7nlthB2wzqnX6BAaW9a7Ve905ebXhUgb2ipKYMTnQagrjzLfhrPMqyiWXtzwnBD3exEXUCNjxPmmr9ItkHOnZMxG5JE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
درخشش‌های فصل‌گذشته لامین‌یامال در بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlJMw87aLSUWjTErZBBOAu_9CscK607mTI1OrUQmtjcxzHto1nGYKRrN-HB0E_7CCqREaiHl6kIaodrZzOfvh9Kp8zeC6R710URYohMyho1YgyETFMIheIfcwlm6-Ca4ix5_DXq3mhcBg2g3ZiFqYh2B--wBRy-zL6W8SkQVYABJl7rxbD6FvCOknVBrRmz2kwOH2X6iYZ_dLKGXObCXenZKo5Ec888Hs_q0fGm7g-DMghs_Zr33bb_Y8CKl1BZYscEoazCYBRvlr-bqk9vZAHX83UAHyl597kM1e_y2Y24CquApkjeqgxPYsHdKEKL6enznufy3NKSmdEZEjtq7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102058">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPs3-tBkLBw4hpmwRVRYuFOgw5deatBkxg00OcxGs5YbT-AnRBlaAn_CRaalbYn2GWXm9v-MTobXhA1kBBU3mb28iGSeIPI_z84Y8v1xSFOmNk1NFyFFLmEBP-_2RkoYtffKhBtzBxdUBIMCI9nDn_8EaPDS6nurTHBx0eClzoLQwjjWLKCW8wv86oeJU37lyVaW0HKxh6myo086s7EFSUyRpISXwwZnpqgMqJQdlexZyl3YnWBCc7OXrnzkSegQgjGzd5KVsvEvqu1FfkKFA3RZt2-6P-AkyGNy_WG-SsuJgm-NfJgcw8xzfpCTm2AZ4p7p_uF9j82QVhNQyNHWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olfgU8RdiVcLsHfeiGMsAO7ClXoANC8-2Xranav4Wgk18KM5UfNlFBHX7Habs8zabT2ETZpab2eQIwVWKO2W1YOwl9-LJslyRgpp3PCUB5wINz0S4WirdASasMNUWnxBr-BmQ4raXwgxlerM_mrUsnFC2ZaKcJhYWBMgqBgG6RGtnxeHnwMCfIzYI_xxmkTlAkoaPLwLLLz8CksXCGEgfWEnnjTXnVyLN8tt_V8EueOCJxdbFt5xj6wMzbKs6f2at1jcUszFw1cfB9053c1LXatw3tz4kEslnAIxyPzxhptFQ9BnwPtfw9HBC_CxOWUcMGRK4ocYZ6EcTITxlavl9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
نیمار:
وقتی در پاری‌سن‌ژرمن بودیم، از مسی خواستم پنالتی‌ها را بزند، اما او گفت: "نه، من برای این کار اینجا نیستم. یا خودت بزن یا بده به امباپه." او حتی برای هیچ‌چیز هم بحث و جدل نمی‌کند. آدمی فوق‌العاده آرام و صلح‌طلب است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102058" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102057">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772e430691.mp4?token=h813wLgmIkgBaKMvS10pkZrUyCTJCN33VfClZRfGxadswBQiS9jn6m0JvEPdS5Zcak4-3XYyrqG_oS9WUfuWp17BiF5EvfOUHPf7sRLJ4jPDQCs_s373WVBnsTK3VdFGWMcNW1JIKGq54Lf-YADrDhIukuNUIFgdixvcX6rbUN7pHDvF4cQWPaBlMMwfYQRE3myIILsXcTvqs0DIG99P5BDKgYzum6pCQthB_dEyOn3SW9VRqEumdUhEYbBMuZK2XGMAz6uSSkkmiZoGQ4J01G7cimKv1F4ajIz_ukJaFRJrK8tKpdMBLUD9lxnwLlAaPESG60uuaJA0bUyOvptrWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772e430691.mp4?token=h813wLgmIkgBaKMvS10pkZrUyCTJCN33VfClZRfGxadswBQiS9jn6m0JvEPdS5Zcak4-3XYyrqG_oS9WUfuWp17BiF5EvfOUHPf7sRLJ4jPDQCs_s373WVBnsTK3VdFGWMcNW1JIKGq54Lf-YADrDhIukuNUIFgdixvcX6rbUN7pHDvF4cQWPaBlMMwfYQRE3myIILsXcTvqs0DIG99P5BDKgYzum6pCQthB_dEyOn3SW9VRqEumdUhEYbBMuZK2XGMAz6uSSkkmiZoGQ4J01G7cimKv1F4ajIz_ukJaFRJrK8tKpdMBLUD9lxnwLlAaPESG60uuaJA0bUyOvptrWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جامی که داری میرینی توش آرزوی خیلیاس پسر جان نکن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102057" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102056">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdpzFs6xMoSr_SAqLz5qgJ3-RZ7hSbeEcjVTHS18ZFfPFNIpmBCty1bXlwtzZUre0CQGAZIf4ybSgmfIefvp1ezMc40erBfJIvTBRfRseZr9ywcS_Ky5ZXVWqItanblxFJL5BQegE8C7uFc8fm7xto5JourVdMzaRacC6DoIn58zyN1gV5kwvF66ZMJPG5XwMnOJmDySECo9FBJ2rOcHT_8fuBlS2aUsipKfBBFv_DQmyHNJuaC2g89uagBTWUJPtk6nzs-GQZgucLs-6SOfmmmqsGuPAjqwFgXbOWmej2slLgI2-TRLwq5ctH7Aqka4bAWi40j52_oqW4hh8XDl3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
بنر هوادارای بوکاجونیورز برای تیم ملی آرژانتین:
ممنون بابت تمام این شادی‌ ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102056" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102055">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.  HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102055" target="_blank">📅 12:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw6yF0978bWxS2jw6oXWU3bM0CwPM2p4fdMyiFIzDLa8DqlHAyIaN1zRdshBEsQ2rxR0Lv3apbWZxGFPie3Zav1cOyS-TYX3Ls90j-_AFqV9MWKmGahZ9hp1pX-asYCIYbBAwr1Gn1UFCSKsErl19m-8pTw4vr9n9xqQkyOR6hd0tr7HwwyiwgJXctrJgXvSVPBSQ68st7e7F6ex7esAYL-Ped3h8nMlq7V4qugAFc-jxWlZaLMDfmfGXV5p-5_BAJ9u1rDVdDi_rfvH4YM5L90k-mnubVKZYVuLxVsuhLaBBBdPEjG7UykEk0u0i-iSbOag-I1yTJm4cr02f7oD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0lAspfW13OQzIZS6xUCOx6t6Ytpe34ZDwTWz0jFp-a_WmE3UqDbcnLmEXPEBxUqnrviDdKJGQiYBuJdR6caaAHWRY3GL3QvVfcwuo9pzrwcfiZC6NMieNc3x41gBK63B63G_uk642GUpswpQK7REsj3vek_VwazvPR6eTpKkpTF1cfVrgpvAa6U_axVAh0ibXaABlyMjm1EXsComN1JewNmRAVUO3OC67wVoblRoaK9LVcVk3e8JhsUyR421AdIAyGMlC_7myvP66Pgj0dsR7TYzvHZtY_yM7RhE63Cc4kvam2bnfwne2euAydVBDLQtZKP_z4IXtDlHmRzgX3zyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvR9coBqJ8vbEEilT3nyAVpr2BcVVqFBCBjsRRKX5ogJ9ORP_swFqmeTO1xhBkLW2kv4Lhznmb2JWzweEgVsA5UVdMxDRYVZ8T3PGyaWynKHzVUuaeA1Waw3xhms6xwV8lrdI3cBLMdOZNiVaPzQiefSLmPRrc8XG_daya87oyt0iEOXQxDXJDWzqfmh_tpc38VxL-Z0q_-IyX81RTPLGnhAJw76xZlSRhwZ4qxGPz1xNKCpbEUBluSEhBE2VEyAxv_b-GFgKKbt7uarC35u73fMHOlFstFoRZ6c0TiHggew3Db4FiTb7L4g0LKW9Jy9RGY7s3_ifGnnsGW0fVRTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=e9PHhm8DJeEVdUg5UFAx9WY6d4oXdXLQjRF6Evv5U-q451YUvn7jKFXZeY8WvVWUOYeD9_nfAUJkGUxE7qX5U2RKm3FXOhJxhI_YZD2NU_72LnVskIcP4b5eFfzJCRf-sAyT2LysUH_yLG0VRVD4GSCZU3HNYsYqJk9hI_SabTBOBl8PGJgb4Txv_avwS-f3e_9k-qoVFIktTKCV94463fFIqVIkWhiW2N7NInyCvP8hYPCW7ZRUmu2hWRuEL10nnv4oa1dWB7ykb7Rq2QzAL-gCFU_lo2Y3yCRwpRdNjEURNwqfoH0MBN40LQXkOyb-TbTfQpht0YLkb9EtDntMHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=e9PHhm8DJeEVdUg5UFAx9WY6d4oXdXLQjRF6Evv5U-q451YUvn7jKFXZeY8WvVWUOYeD9_nfAUJkGUxE7qX5U2RKm3FXOhJxhI_YZD2NU_72LnVskIcP4b5eFfzJCRf-sAyT2LysUH_yLG0VRVD4GSCZU3HNYsYqJk9hI_SabTBOBl8PGJgb4Txv_avwS-f3e_9k-qoVFIktTKCV94463fFIqVIkWhiW2N7NInyCvP8hYPCW7ZRUmu2hWRuEL10nnv4oa1dWB7ykb7Rq2QzAL-gCFU_lo2Y3yCRwpRdNjEURNwqfoH0MBN40LQXkOyb-TbTfQpht0YLkb9EtDntMHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
🇧🇷
۱۵ سال از روزی که نیمار این گلو زد و پوشکاش گرفت گذشت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2TKZLbCsf4XPmKxk1gIPhrb73VAq05N72Hcf_LI34ZaxELtQ2ee3hkTPv3lB-2bpuObLLJWtAM-o2lUBprr3fztpWwAhEA7hQ_cCUfdaCwQuYwxSSU04Ks7W0JO60tkgI7M6rJfA2bKS2EGGS5iALn8e4k0jV_OTkmK4TAvX9cf5Ag3aowWtovKNVcUibfUZnyQ9j-XOvg5t_jtGTLvOgOg8xsigCgGgSh0AyMdKMg4RMn7OpOcOOSGJ2H6fOZqw0xD0vxVp12dc9kDrBIlPc9f_eW2lvd_yYXPaMkPTw9ZhLbo4BJ0PwnpzMnZx5cRR8L045d6sNQRVsDyYPaq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a6pMVXv728roeotwvd46DctPJ_63IMpPN8VOOu54VG60W4HAu6cvQhCJatgXNNVRnmKa1tDwz4cmpj-ZBr20wKZ3DvlKMW-OCtQQjnVGTYSxADgphPtcAcUDiR3m0_1I1o4r7LDcT4_v4WScBSdlIZT-iL3hsaqnCrwpsy4wQ3L3a-F6WKnG2_63ReXoWwm2f5VAAZLLzV2Skg5FynMXo7fm8SwVdAey1vfLuPWbkiX1zMDu7Z7I6Ai-7ktBlY2Kugm7DzGXYfBPJNxKZwjyF6Z8of23EGsg7qMg5WrIHz7_NAMkOrTs8R7Z9yPzlSYTPcZ3MGCK9APckSza5LS9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H36OMJk4javym8D34JOS8CE753Lr-3CxoqwcUgiw5BzaJu0JVbxliJ-KcLC6gUHI9aGiMCedo56Oe46YGbY08jYFuBBH-dT56eMAN5HWN11FEpwimshiyc06Str5woZg5fzq0Qqih5-0taKH7l-aAVVF5Ea0STe4vj8ZlZ1wGedLYwOy3OzARSlse1Y604FeUlhiZLUCmttjxnERIltB3NX0apR0TxJ2_ZOBrTDFxelFECI0vkWFjp4R8L6OCBoe5Xv7tHzHM7NO2XKRLevaior10VVwQm_AKs1GiR_LMurpbsrADm_MIl8-rxX7Gekcla4X8SUgyE3G8n1upbk0PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6xLAa1YxdQy4bpFXcDRq8ttahr9UnTTrWkT3OD0v74lSfa88c6JNwdcrbJrp80CsHTjBhGl__Dr2WAy2Nw_c346mTmlVTsrERUTiuUU2sQnNirKMv4HEdt6HEe7nLC5JEYZoID-TahSOl4wJOmW9aDDH074Qvel26AKaHX77UOF_O414Lg4CbJrAHLSyYGGc3YeHCyFrycXx_xHArutDDNakLho-fYSswT9drgSOc0aykqvK2tN3oZPtw6iZ7FbyugGNKOYpt7n8NbXBVGWvx2Ves-rMzBplUfRR5EO4yfjZiXu_P8UMsr95yBPVF-dDA-Li9gb7iVpcyDvpPkDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ypk8hof5mnkcPoMPmD8TzCJ2ibMgZ63hLEQAq1p9RthoSjG7wtYwhKd5XPDDUMJzbuUrIXTBU6sZRIZtO68ik_grT7syn8TCq2exUEk3IYsRTUQOhp-_eY449Ndgm2NxCqez7NjsW05JhLQj-8w46mMCxsbhLUYtgvin00iphleSgwIaVvxGxOJzAs_Exlrf-wxUTGi9C4iLJ3M3juMu2psw53sCc8vDURh8OUsjPPnlg7g_W4mkHfXCUiWQBFcnftxQv7DnC_87Zb7Xp3ckvsldqxfbeVuI7DSXPxb37oqWAlSVYnTtY2j4967JGAIRlyaEKlyh4qnuFt0xhMv7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXD9kFe2WJnd1W30ZIS3uWQRIINcIHaukeoFT0z88UVjR5nNoQ6iO7pjOVbg637ykMELnVA_fvurZYH3LyWIclKDDf6zPbVFE6pYnKDgS40FRgjimX6wdwVG1f47VMZXHKvedmE5-jPk6hCxT2AJ4D8-YlbqD0zzo1i8UXm88COzqSsrvnUivfV3SzF7wCAxAUzR8lNBBtAeYg_EoDgELUf2Efi6aYqnV0uWHeiJFM8lbOnumrJxkpNOQj7olqsFHIFiUVxH_wivMG50_INK-IbMlKWYceUD9XF2mGn5SIAhVz0LH3Nkb-JYlKmrnxuoxuwrcdDssuCOSpZ3RdiXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو: پاریسن ژرمن تلاش میکنه بین رودری و رئال مادرید مشکل به وجود بیاره
‼️
🔺
🔻
پاریس از هایجک شدن دیومانده بسیار عصبانیه برا همین با رودری تماس گرفته تا اوضاع رو برای رئال مادرید سخت تر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZLMrYbVZy2Ve7NsL6N-UA483_ALZIOOO6Uvng-0pzP2ilM4YLUI8fqH2Z0AmnqfntojBfSNXn4YJxwqUlKZ-Iub1h2OIaBLHRmc7sF6o3qo0H7teSYzscLKYbh3MFyaRa9lrkuT5G6indEi4u4xA8g6M4M9vUojy-wP5HUH3J7X22l-oGtdGaXyhHjypN1ITzfg_kb6_KKDxKMURFieHyIiZ0bXG7hkgtuHjBr6nwpOHfIDajgtYKZZKaSh-_sXQdzUzJTQA3Jpp-hx43NHb0_Q8bgDjs8EnqRyMsfvLp4qohOSQMsc5I5FvjyA0smnd0Kd1M2hDgzUWMheY81TQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3u1W7JKo_NAozeaYF7Jho9GDyCIdt5iY6vcWXLuAj7PHHomGVy9plP5XFW58i3akrmxdVIAdFEg5X-jXUBZKxe8GHXGiyQu7uSwEas9u1Y_eJowTIXyyFu4w9-qUL6OHem3JZEn6WzUuJ0qkcfAQXuNe4cOVxZX5RvetqoHnWO7_wgtXZF0iI0sCcnO1xFFkZLk3Znz3RQ60Ro6S73lqNyK6jGN6oLENpQKzzfCNd8JUgck2D_GH7bz6VXkuDJerWYz8Ta104ZtOyxh2Ka6nwaqnjaAqg8ICEAZESbInkzlvGvdZ6XqmTK4N_Sb9HU7l2ZRnQ344DfMViWdU4v-Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uf4bq8NEXElhsZ1Txrm94sE_Y-XnzSmAmPUI4laiHFaDgXArUmUTr_I1D133meTFk7v6vdgXNrA4ORYkZKeiNn10vtHP1gcFfqh_JFzE1y66q9xPGsEwtS4cAU03ffPS7RHt7JSG-k_hjzzlWk86mC6ZhUwolfCvWZuanFTsoDWj71Uysjg5-4Fq_0SvbweubBO_tBFz6tCb2wE8KbD3g11fFlCVbN0GWHeNUADYA_WNEzy5ncQLxWClpeiWFwjcEu-dcbY2JSDUEaLAnHRYhAumSBDwuj7Te8u8TqEeMibkXXGRo8MuNj4yx3_W0l9TM62RSK7-612NCGtF1DmFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6etZGocErfUisIU_-pp_YaAiofnc60IcckT5Fg2eMem56Z8jCb2c794s6hPWoloq6gnFuWuuFy-TiFafyi8TXEhVNL6Q67h-gepo4bjXnaVZ_JoreW3u6SmrLMWLvOOJAV-lIXk4YDG2DrYsiUSYjDtrF42czS38DjAKMDS7vuTHkYABoMz0uVa8HnRKgzjwXzoidVjPsdJy9S47NeKUcbcngcVYqGE8cF46ISCHx80shpoZ83oVpclie1EfRhG5nhGhiWtNyxoAqW4gEn41NzOLWzSXmMvqTzKsPUvaaoLkeQ09Ei777YqQwFrd1oKQgrX668c_kJioCVuuAhnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2xvjRyO5YjEnaloibPLRgecnK82pW7JSbe9LBd0D8jr6QaodnSkL8-aHzPfDtYogCc1TQhoytGLJIxcDVNsixl9j3CQLvpvFnWx8PfcQBndSisTfUtsa6Vycq7ATBjzGQTTePXSRiwUawAQYSZvybSGWDb0Q75qwCbVeSWEOO1fiMDaDZxrK1f4fg_i4RbMMuI8RrzeYFratFDQe1AujLu1DW9e87Pbj_fSLgdlNRUFYkYdAlPA8omWqf08RGVpGrJFJ-BtOVeJo7CDYbcvM3fpyg9JGRgHmfdRg_ZebyAp98Xi_A0svPdZ1ds8dmRdhEDL1NEVT1ypGhze0w39fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mO0Z7_RTc64oYz4uJvxc8tZHh8rzime6G3_3zEhTJ5y6yldXMehY5ONwqAWWjegjGX4O_Fr8k2T2Cg-mxpr3Q4M90FWnCxGKu__XeFepHveZ1dlveUsQCsgxWxmJ2JrRKGzb7cWFdDneZR2xLzIsX0JGvP0WgU9ypa7aLCsFEXWWNwc1D8LBce9c1uQ1zCiaDonT4KFElB7dErjA6ECYHWJ7EGugekJT65u6eZDBExeRxba-wNJiAxYSTmE8bB1K-90uYtsBFewvU54O_cT5Qy8FAgZ-hhlLFmo-cCtqIKOKi0SJKpYweefDhhG0FQx8HEKz20h8cAKdlxMPOvTXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkGmd1p1MWvXkPke_m5BN4bFHhyTFF76-SE36nCZA2vo95ECERXfwBlRJZmwHAMkR7rTeX7lXm196YVBEfDHVAmMDK9lS5j_cw6Aew4xkbYvCzCiQc89bdiUlcFORy-0FhB25U_rEPZRRKnL3QQcXszgOPEsHMbfHuet1dfl2mnIElTd2oPMAV687R_l2Im3CKkWfUZNRbEq9hctq_chvjzxQTVuEqFAPp67MOKRrByqISCSEoQvHdgi-M--tvEOpU1QBq1bRFLZKuaPnqGa4IzbJZy73K1nXql9qcEEFbO-u3kCyz2UK7JmoyyxfA8OiFawA4gyEXwBZucK1423dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWI8pPDry4h6WMW920G-ZRvjt6oEcPFoZhuhjWL5tZuA32jmn4IQteZs_HsMPkGzPjeP6d1TS-KV1GNIngvXkJ1pFAsPH8nQthwwqHBXSpv8Ws1PtkkTObcO1RCE2HI2wXKZeOYRj_t1aEyltzwi3Bah_05nTVgHgibUt9UWTSESMXtberi-29vCg-jDvPWick_KzhCt43dRXXobmxll9kyx9sF1htr_PD2i8Dx-7013L4hDtuk-CB5ao54yJh8B3tsxW662AbW6536rbmliEdYq1MY5_-ViA1wjnntahdTpcFGPSdKu0gopiWW2Gw_IzMua0If214dq5jZcXLWJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rDBNUBpq_QB7nSaMR8XngxW86H6WGf1PHTVv_zemKow20_qFyIuig4G92YkU1TThoVFfq2bhyqwfRqYPB_r7gG7veoJd9NKWN0c-RZ7gpXBp0_Y1IIxYot3iDjPHbI7lA7E-EB01IqkzGdsOCyaMMBEGBqQaE06s6UuxL3kldO52Yd2xBlz9VpUJ3MuvHuHMv8yGOPOWurTZZ9hTfUQ-rCyoKSw2YoII5bA1Q9yrlxzq_FjmKpeCUWr8IYOhzWjWjAGspTdQpl-VXO1QNVBo0GkNJWP1dl1g8745AL_SXYX5xqzuhYBCdedtQ-dgc7OcW-w85ONBEddtUaEWUpd4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcepxDcMFazwA3wQhNJwLrAHkLGcZFNIIl-_HSrFLv6m4NRCWQzSsabokIKrgfefhqpsXOYUk8rKMT7sn3yU4O9JU0knZvXLPT88q7ooV5MVQpTq-uIvmhPTJB2bROZmhJNWRWKowh80oKDqDMNRyH-KKzC3IyAnfhhG4jdiu9WjocBFbzUGBn_n93tNyW7UZNkz8pCTeq6e5GMQ8UPP5XKu4C4GduNNw90pXBciTdMMqbl25fmrUR-CQOaMJHc0FvolInBVHrWsrGp5sBS4eD8BBO2aM0qHJ9HsfluwsC1PR-PRjUc3Ocrrvv0YCUMxqh0XfOXikodD4Mx4Yg4WEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBYYHEjyrdAUDFTvQlcuqJ4NLyqzgWvl2ft6nrpfA-UOjKqnUoyXz2FilzeNK38BiBy3f42cd_iBG_n99ftr4vWDMoPdl0ZzNdIS9NfU26j7ZUFgvonWjcpgTMZrhKStFavPBfDWQixtwSOppwUXxIu87yrNiBwNnvR6mdT2CnZ7Zjsh9ArTTAaoIU2g_NZPpYLLiBCcg27qmPBXNcj7YWh2CdbprdgT9ETFXlKi4QdeD3bIWTgqx-FrZfeUjcGQjrs08W_VPLuZ5zFwjgr9cY0MAj3YSRpH0DFwM0JlLqJoWddzsJfdN_ZFdLmKiLInQXASnX2RbYvDVLuhKLcd4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=Pi-CfqgNPuQSkMewsKko-jV9-7SAeVq5bY6KYbRyT0S6i_GzSQwzFxh54ijZyIVpaPgKE4DEmXRAt5ZgYRwoyr4O3NkDCLCb5XfZMU3kgWt9xom92uyeKOig8TdsvL6I4NP0OnbodmkhSVDouJ6Y7HhxTDr9f0C96yxzkStm1ptqPM2uOisPW0lRlCxh1rzBPcxluTKD7XvlipnJgtj2O6l5cvFlT5mtvRph2d6SPriCr-wXKWp6XkIpkZQ-xnqctc0aQ6JyM_CbaZGvjmp3jzTv8GH-mKzIUYSa9lH3gJkn_PY6zCotFDg4UlIXl4V79Rqk2O4hM29Wzpa_MmDxzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=Pi-CfqgNPuQSkMewsKko-jV9-7SAeVq5bY6KYbRyT0S6i_GzSQwzFxh54ijZyIVpaPgKE4DEmXRAt5ZgYRwoyr4O3NkDCLCb5XfZMU3kgWt9xom92uyeKOig8TdsvL6I4NP0OnbodmkhSVDouJ6Y7HhxTDr9f0C96yxzkStm1ptqPM2uOisPW0lRlCxh1rzBPcxluTKD7XvlipnJgtj2O6l5cvFlT5mtvRph2d6SPriCr-wXKWp6XkIpkZQ-xnqctc0aQ6JyM_CbaZGvjmp3jzTv8GH-mKzIUYSa9lH3gJkn_PY6zCotFDg4UlIXl4V79Rqk2O4hM29Wzpa_MmDxzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iix5evPaGFy0KvtvnEeb0uxM-khEcuKhQxAnyaVr8_bOsz_TpjT7mQKxgl3sBcNXu0NLH8lRVfygwEwsO5cMEvGvjSf2etl0cNvEiqOriTfGHf4rHRecW7YXpadr6DdvaRl9g898oV0l5OVioP72ene5nps2g2aZsWEh_1v4yGRt7ShlXApf3thMXNrV7zPnWAqw9pUdAvkf2n8hd878Fm1UEUGMl8Gdl2SS9iurv6bfGXP8t-KlX2Mmgw9O6RrEerpm_rgDehGLs_2Kkf_1zsOKesgcbw9gXEhyeRKbfnyKrhWRZ8mT2BGLDoAktKNe2SvKdxXy3YxsJEqpYekEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKMoQTh4giLCWmcGyDct1QNoyLIT_IVCbzPfVOPIzdKLNDV8RFXnH5xv7bKqfw9cXJblZSW9yokRYyMfozCBzzPIlaQbg8vM4MVejDPwR8wiFkxcuzUgjkm3qpsfKScEb70_haXkXj2EN0WbosJQdolBV4eTTU9q2_0xR7SweOaBf7yi43E7LlzVum_kCs0eVBbotwBR31TIJ7yHhVbzR1Y9la1LtGbibbW1sxPylTwMUugohB1dPRBhTJGcM1_GglCmAQgK0axpZ9NDeLckVUtfZVXwTKfOi_yWYAC2GL347OTim93pMBpZk8dJlnxCmzKcf1W-r7PXMESS449L7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=G85o9vtoLe9Qo2vds21zxeAHxtYfeC6htJx9xlPUyqhrtCzxkUZgvWUcwCni2FiNHxSzxgQIEY18cbfEOJYs3xFN6Xq-L0P9dq3L-OIYckbj0IVc690EmrkxLgw_hSRwm6ScM3NqK_QeqC-zJDifmpy9t5dAjv7ts4rEXxrRLnHhtMTtkw_DHGFjnfmjVtustAwdTFKObFvol5pOT0AjexW5O_UZBVBB3Reaxma5xJep-gLSlgrfy1NfQYOWOZI71FtWzl5g8om9X4bF2YNtzsxCW7MfO49oeY_BvDVX6YDpXo-KY0CWS7rYmxOIUoVK3O2_PkzBrVFKrFbjVnFMmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=G85o9vtoLe9Qo2vds21zxeAHxtYfeC6htJx9xlPUyqhrtCzxkUZgvWUcwCni2FiNHxSzxgQIEY18cbfEOJYs3xFN6Xq-L0P9dq3L-OIYckbj0IVc690EmrkxLgw_hSRwm6ScM3NqK_QeqC-zJDifmpy9t5dAjv7ts4rEXxrRLnHhtMTtkw_DHGFjnfmjVtustAwdTFKObFvol5pOT0AjexW5O_UZBVBB3Reaxma5xJep-gLSlgrfy1NfQYOWOZI71FtWzl5g8om9X4bF2YNtzsxCW7MfO49oeY_BvDVX6YDpXo-KY0CWS7rYmxOIUoVK3O2_PkzBrVFKrFbjVnFMmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-0nZCyobJzdA_AOh1Knw_NM4XQmKWfF4OdjHU8zxOKvspieTk3bSPMH3OsAgDl0ah-HKoFTm04MQr0ErPA0b-bZv6IpM9MEaP-UOznNJ7Ls_QHWBmQsgVgdDkOhoY1PPGULwtwwKSBhhi0fy1JpfCAHjcHP4MK3aSZUsWUaAvkb2mseZvrRtmiQ9vvpG5sAvqTKwjXZourOFImDBx4MJNK7Gycb1Fm2nRstEg89u3t35aQI2lTDWRwHUL6FFIlB6qF03GyO4bLr_9Z2xkADIXS5tYhVQ2TEY9V7OXG8no3qAvn1hxiFr2qnNJvfR998uVGWTtvXgYBgmfuZxNKTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnmTc1XKYmbWy9yLAF5ShV_QHD2u8odXMF2-9ikyhTre60anVFpzxqL89hq_41QecPmscwvdL6BYZHK0TXyL4tebYSowlKs-HixvzRo6O_ROLIyu915hpCH-2Uj2yxoXqGx2XPFFDfzGje06of746k6sHB-1j3liTuPGojL-ocsMen8TpW1Rv2vfK8MxRsVzQ5iVTR8QSa1uMu73vwvRhsz9haCUK0TMssg-inNkS_xI3r0v6qkDULbB0yvYHFZDQNl_YE7PUmV-jnxYxCTNdkt1LX-LRwhQCftH0YhKhm5-exYTOhScAjXlet4gH3mKarWFKJH1trrh_YQL84OdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLZ9V9IjFq3Od5Bx_ERWcm1s7NiGx22e0jTAJHX3NHAWOEEpZwPpMzassCitY9_YlyBHLlgDzgrVaRmX5SeO0Mn-bR90hJMEtwhoRKIC2DLIDr41ZLdD5JU64cjfH6rxOe01UOK_6PJUj1D6aqLG6QLpY8nDGC-PNtg8Y5uCQIb0Xaj9GkeliAfqyIfXV4SZmVueyGX53RFOruwyXhPjq4aFLeMSQF98vGAMRKS82nluYFJt4fNPPDMmOd3s6kukgXiai2cXQ1--vLqKvabQMLINF_4NPNuEfekaFe7_7z7VEDnxgYXZCZ8WkDh8iDFapB4Pa7HKOCnGXr5lj071XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orqb23BZ9SygXMsPHEnw9G46kPC2_jUkppm-3ndssecJLLq96pQH0vL59Ofw7Q1lH6bQ7VlmJjpwqG-qMtT74c6YuMvVfqmFV4hBHQBmPv7scWRmNijP-shH3qmUxlErvDYOhyTC1X1L0pVCDVvyue-gnVQImp4sueKMx7WxyqIGQsr4sQMv5mLdrC3d_CjEBpDv0ZEDZuMB_aDxOot1BBGggoc9D-rk_QjC_VB_uqPua3XeU1tGvU0J7B6ZI1hDGxsoFzm5bS8XNkkBT2jArIpYUkh7TqWEXNmD0EJOLXDbiqr8GBh6SZSsMHE5HOIoscd3YzejI_D8E0wkDj49dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی
از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست.
𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=n5rCZYlj1FZiVHmgO4EqIqj6PKriVzr-zuCTsGT089N-rIw2lOucKDJod4HvTaZv-gkzYaZ06yGLT-g8GD87sJcwHycWnGSwv8EfYk0qJ5BqyVBVsOT1ph9t-lcLisrsveXCvIVJQqxGGoczIXFlXESZJB_7YVZmjw1kx6UIrGYvAOWlQMY2oPGeZA1HxVr2KsbHaw6aLH2orYKCF5TVz1GoM2p0cjA4bsGPHypMTRt1CWOyc7UiwFAy924DhUp5Wyq3uFdGLRzYbllXN-NKJl1n-ilhMfyZfQkQvNLdrB0H-nzpUtve8udMFr0wNv8hRhKvEZRkX7F_24d32crSNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=n5rCZYlj1FZiVHmgO4EqIqj6PKriVzr-zuCTsGT089N-rIw2lOucKDJod4HvTaZv-gkzYaZ06yGLT-g8GD87sJcwHycWnGSwv8EfYk0qJ5BqyVBVsOT1ph9t-lcLisrsveXCvIVJQqxGGoczIXFlXESZJB_7YVZmjw1kx6UIrGYvAOWlQMY2oPGeZA1HxVr2KsbHaw6aLH2orYKCF5TVz1GoM2p0cjA4bsGPHypMTRt1CWOyc7UiwFAy924DhUp5Wyq3uFdGLRzYbllXN-NKJl1n-ilhMfyZfQkQvNLdrB0H-nzpUtve8udMFr0wNv8hRhKvEZRkX7F_24d32crSNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF95AAaHZlXC1An2RkDTE6D9dMCVsKMrowT_A8GJvpoxEzhgKwaNvMHbk24YA59VplBqu9J4qS2zZFrzmQSM-rtaEXqGkgTZVgbh-exZHzFPr2RcwiUERxeQWL1KPMUzZH1knchTJHhw84hUssNXx02Gjxw2hBGtq-BrSRLz3Gxib23E2z43xqMC0cB867v9rnuPl8dN0Vg32cJVAEMqx090xjMjOUwI5qYtxIQgNhBPlN7pmFcS43h9b_bgsrJjmCCvHFMUOZVNXPIYHWVsB7V5AwP6QjpzkhQDLORuCpPDpu7ueq4bG4-MjbFKaOO-YJ_-2QMQNY6TRCHLBlnq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KFclgy95GUMSMaceOa_DPPnCnCvmatf6oJzyykgXiYaUAXCsCrbItv3Qjtfs9q5p2ycx23U3BxjCBOz_NIfrmcNxGqsRc8dPD8dBABkNN0UgJ_0PvwuHIqC-hgNDnqaVXKI1NLaFsOMh4Aig8GexYGGoHFLwF1KmJIMsWSuDAKWe58yeoyC5r9JiBA39Knj2RrSMTY3EwEP-GtKGiZwwrwS14Fb2T4CDgJJb57xVT0WOXTcbUOvwj-pB77t8I1n6XaSgDwKPDtUlRdmCo-Xusof37FmRIKCQTVRx1Zki6ozKs4kWhkmSvJ8RRHdUHr6viG4AKwsnxrky2skzU2-CXr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KFclgy95GUMSMaceOa_DPPnCnCvmatf6oJzyykgXiYaUAXCsCrbItv3Qjtfs9q5p2ycx23U3BxjCBOz_NIfrmcNxGqsRc8dPD8dBABkNN0UgJ_0PvwuHIqC-hgNDnqaVXKI1NLaFsOMh4Aig8GexYGGoHFLwF1KmJIMsWSuDAKWe58yeoyC5r9JiBA39Knj2RrSMTY3EwEP-GtKGiZwwrwS14Fb2T4CDgJJb57xVT0WOXTcbUOvwj-pB77t8I1n6XaSgDwKPDtUlRdmCo-Xusof37FmRIKCQTVRx1Zki6ozKs4kWhkmSvJ8RRHdUHr6viG4AKwsnxrky2skzU2-CXr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMcgOVgjmW6f9SenVx1TMheHYh-wVzjkGIOQBZK5OwToKAzYo5qT-0gTFHT9976rbScqoPUWPt93zYACys75C5MVJUE1exiGN3ryde9KZJR32BpJJjb_LZSsbmnhiwefjho2LqchoXsGjsQnx4RLaHQ5I6C7sXc_K72hmPTgd8SCJb5qryl18kK_ckqfNFfj3R2fVfNHlgmVdEslmMSS3W1UI3FZgxMMen6DBeO9NQxsucKlP10N58IBTZKB5TUP4bpAW7czfkYn_iz2Ea1NvQszb1CMNgWfcR1q82Q9VYd_3gqDUIE6WvRQ9kK0E0_4njjPrmXHL2reB-IpUjTNUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh2stxP_Wpa7gVyGaX3v606x131_iBUqal8bNNHh-Fj4_Er_0V9aKg3QnjVxwSY3FA5B937JjA1fIslVWlvEqokaWNTpMgcPUzBKqi1krGoYOItZZ4VDwiAyk0vWTpuiNWsMSjz45mHKEWPivFN9pbwiLyTk8RZWx33BWPQvIsGq0Zy6i_MCmsVirHkGMNnvMSbGRhBbjdpXPUu6_GYiJ1nhXI79HL19DzCAFUonFLQoVPb7jLejPgQ_0YJr57JU40ILM4BxCwDC5FRUBF-Qyh9U5F8Mywc2YwMHGGBRLGP71bNQXJq_Bf5MZv8Z8tD876q8mpVxJ-vOKjzwvZAWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHby6LShduopF2R2VA8gzHRAmYDLlq3T6NLslyRM2PevS8iCH58zN8SIP4RLO5GTuyIIqY5GmRCjPm2gcTbbtKe6kqZNIwePOg4FyamLNrVQLJMHlC8g0wBDOVR-Dt6PkOu2v2K6dgNTHRhoqFC5hfyM8ZjN4v16HYzL6zCBZYdFT_OGyOXjYmTPht0vyqH-wMGp5HG8HRuHMStm7FvUPDejZvbSQFzs7a10qryOuCG2HhdZJV3xa8aAlhkQoK8IaccLBZFOpcnY9CoMg5PuhO784UE3bMfbSpkdinGjiaBu4mSrpaQMCpWRVzA9PoX8mwbe0ePO4lQ7FUxggLp5ahtjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHby6LShduopF2R2VA8gzHRAmYDLlq3T6NLslyRM2PevS8iCH58zN8SIP4RLO5GTuyIIqY5GmRCjPm2gcTbbtKe6kqZNIwePOg4FyamLNrVQLJMHlC8g0wBDOVR-Dt6PkOu2v2K6dgNTHRhoqFC5hfyM8ZjN4v16HYzL6zCBZYdFT_OGyOXjYmTPht0vyqH-wMGp5HG8HRuHMStm7FvUPDejZvbSQFzs7a10qryOuCG2HhdZJV3xa8aAlhkQoK8IaccLBZFOpcnY9CoMg5PuhO784UE3bMfbSpkdinGjiaBu4mSrpaQMCpWRVzA9PoX8mwbe0ePO4lQ7FUxggLp5ahtjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJ3_EqWzzG1qVlC6a8tDNOLndKAajX9W2rlXlRy_Im-v6U3SWxcbChpD8kzgUKHa6lqH_Nza6g2l-TQlb6ZUSJg265sTrKEoLAceC4EhhEncFyShgA5Ggww312lJJY5XSOQBcd5vZ-AlpbLbDknF9PZxFSeiExDGvcjTQaN0oRLgwT70fcDzwtcqypJD7Nto9h3sPVomWTHHlh6Pgv5isBg1lfDGfLICKma1O1eeImrDxKigTPxRIJgCvv0Zmw66zPm_8lakKXW4EgKwBbi65PEZojFhVrVP24FG93DqdyTKIT2FYAl35HSU05vvj_byD7XbfszRTX3OBih6LdMX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thtaqPICPtGZhK9N0vL8kchd7uKVMnSBnQOk-tPrF_Hh-HPQdxDGQDFfZFpsyGFUPTnfevVxk2WPmT-l8DInfoiFe5Rh1xyRfAAl1i1Y6Ny3SatUoN7AZc9iQnbPA6-Cycoce6ZBiNoqaZoB2i8jcHHnfxjOH2lFPmYFw_gMSa854p50t_R2Z__pV5RUalZVAo1x7FB3L0Pc6EdrMY4TfB7i7eauZ-I1QuHZPguBiUK7sK1bfTHfc3VBfvF7tHziAWYEgfCs1S0zGe-GiAQ0T4031nGE8NabqLzjQM-fa8eChpLNSFleziCZDbkALO0PuBy7HUGB9ZZXYV6-AqX-NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0v7rG0_tXkP7VsB-m93j85TVyTxGznaDUz9Dc99qyQBZWscoLHd7W_q0SXiRZZuIGMSFrKsQWVz1y2Ob-5sbulKOp1WJTeOP9MhQ9eFnWI2v8yBxheL2gYM_bvTPDgrvOAIVICZJhIikGayLN2P3wcSCO_ai78TpQHhOM0NfhxxJQaq57vYaoCefE96kVw5nZzc3fpPl4IBBC-36rtQNOc-l8baRQ2Uj_kMwF7RdBTuAmTj_91OZCXaPrkocab5urfEKTmhgU0p_fU9RMGKWdE1BtqWaouNTEXZC5IOHjmtjkEYW422litc78MM7MyywQmR9gUwnZeMKZ1nXsKU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
گران‌ترین انتقال‌های تاریخ فوتبال با در نظر گرفتن تورم:
🥇
رونالدو: ۸۰ میلیون پوند → ۲۹۲ میلیون پوند
🥈
ادن هازارد: ۱۵۰ میلیون پوند → ۲۴۵ میلیون پوند
🥉
آلن شیرر: ۱۵ میلیون پوند → ۲۳۸ میلیون پوند
نیکولا آنلکا: ۲۳.۵ میلیون پوند → ۲۲۶ میلیون پوند
فیلیپه کوتینیو: ۱۴۲ میلیون پوند → ۲۱۷ میلیون پوند
پل گاسکوئین: ۵.۵ میلیون پوند → ۱۹۷ میلیون پوند
مارک اوورمارس: ۲۵ میلیون پوند → ۱۹۶ میلیون پوند
گرت بیل: ۸۶ میلیون پوند → ۱۹۲ میلیون پوند
استن کولیمور: ۸.۵ میلیون پوند → ۱۷۹ میلیون پوند
ریو فردیناند: ۳۰ میلیون پوند → ۱۷۵ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=PjbDEOogGcFKJ8WlimTLm4yckK4UMb2i7okMutPMUDTbnjdYknkQBlpwQwYI5eAE-hbkfOF4iB47srvvlMOHIGOkU5wGAjc66NSssjzkQPnzAh3CsXTELCF_C59oGz1qQS3QLapvNhEP1E2zlcGuxiQG59fn24QklaOSaMBmEQVTWEzQNlRU0SlJW-06QFOS0Li9y0CXmKAHrOGSOz6X-9ODiE8V4ne7CaVAGOLfE0O8isULttQAFIgrDF860u3Bp0Ylx4sS-osfiMi1vV200lPP7InpbXj3NmsvUvPb56-xMBBytbXdIXcIkdROKCD6m0ka2JL3kQIE_NyC-zhhnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=PjbDEOogGcFKJ8WlimTLm4yckK4UMb2i7okMutPMUDTbnjdYknkQBlpwQwYI5eAE-hbkfOF4iB47srvvlMOHIGOkU5wGAjc66NSssjzkQPnzAh3CsXTELCF_C59oGz1qQS3QLapvNhEP1E2zlcGuxiQG59fn24QklaOSaMBmEQVTWEzQNlRU0SlJW-06QFOS0Li9y0CXmKAHrOGSOz6X-9ODiE8V4ne7CaVAGOLfE0O8isULttQAFIgrDF860u3Bp0Ylx4sS-osfiMi1vV200lPP7InpbXj3NmsvUvPb56-xMBBytbXdIXcIkdROKCD6m0ka2JL3kQIE_NyC-zhhnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=Sv932URjBLY0lvqRt8D4Unv2CwLO1sRWWUpWS9mgens9O6gJl2kpnZzbclApDfTgl60Wn8wt4fvH-vigrXYHaTfKy2OvN7y3yibMTqpUQt_i4Nf_7lMIWNjMIQFT7qHudULmmYaujHnoDLsAbIFxjv8bV9cUhhYa8MDcYsT6EbIhqRNm3_ftgs5w09p-QDEogdNRCOdX_n96FLqYjCjWd3v47w8WL2PYg0Ca6dwiP04pfeEXeMr65UYwWPqiBDmp131K9zpZBqcxxYj0qEhRLuDI5CVteapBtKBdbrhRQqa2P-nTnndCqbNkZ67RfpgHfg3SsfgyRyAVW9yNk4a-VxEXuKj5RXSFCovr_WKNb33Rv1GnoGAyQ2K_JnjhHznkyzIM_-YspeppNVTTPUioJq7lOnjYb2UYMxOxNZUQ3QLRIP5PbYSZK30-iJ8lbu-sbcagxjstavYJyebzHKDGP1jMnzvQ9FDrY9kGSQTSjc2QrHau92xdCoAUhefnD1u3zPOVGCr4F2ipdYO-ksQFqZziM5QNGE0xxNrPLIxjfZm_j4aasGsthyf1XT7zmMbZW6haikQaS6Ylls9KH5KXuV8SyBgrGKgkaHhF2ZJdRcDmuyZJXH0Ztm6qba7Q4qTYPPvmuKY2vZh6XqSh1xfv_HlGjJkGZ2vhFll6q2tXxrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=Sv932URjBLY0lvqRt8D4Unv2CwLO1sRWWUpWS9mgens9O6gJl2kpnZzbclApDfTgl60Wn8wt4fvH-vigrXYHaTfKy2OvN7y3yibMTqpUQt_i4Nf_7lMIWNjMIQFT7qHudULmmYaujHnoDLsAbIFxjv8bV9cUhhYa8MDcYsT6EbIhqRNm3_ftgs5w09p-QDEogdNRCOdX_n96FLqYjCjWd3v47w8WL2PYg0Ca6dwiP04pfeEXeMr65UYwWPqiBDmp131K9zpZBqcxxYj0qEhRLuDI5CVteapBtKBdbrhRQqa2P-nTnndCqbNkZ67RfpgHfg3SsfgyRyAVW9yNk4a-VxEXuKj5RXSFCovr_WKNb33Rv1GnoGAyQ2K_JnjhHznkyzIM_-YspeppNVTTPUioJq7lOnjYb2UYMxOxNZUQ3QLRIP5PbYSZK30-iJ8lbu-sbcagxjstavYJyebzHKDGP1jMnzvQ9FDrY9kGSQTSjc2QrHau92xdCoAUhefnD1u3zPOVGCr4F2ipdYO-ksQFqZziM5QNGE0xxNrPLIxjfZm_j4aasGsthyf1XT7zmMbZW6haikQaS6Ylls9KH5KXuV8SyBgrGKgkaHhF2ZJdRcDmuyZJXH0Ztm6qba7Q4qTYPPvmuKY2vZh6XqSh1xfv_HlGjJkGZ2vhFll6q2tXxrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLytiXQlh9sXvbtLUZ-jOqSYI9AjoQqbPYKR1xEa052chTQ98Kxh1b2uqcfX00zYzQEuMBAC5B_xZmo_xSri1JF1N5Zp0DqdqfTCP2tWbmZvYZ2czX-gb89QkCn8rDu9jyDf0DzlDQQHsvMD1c1AHpSiNgAl2G_f-Ir-jODlyhX6keqSPQFSYuj0yXwh9lW2lj46LO2cqTllqaNSJnXHZhJdUyUnjcIYBVxOzR_leIJ5FG2mkf5DQjGCaI_S08OWiD-LR0ZAO8ZWPj6iPJQnipXEonrWxtFeOcDxN8cnl_Oj04u7mH5jRIbX0t--5QH3_L3LlsoAQb2TbAFV2LBEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mulPEaBKwKH7YbCYJv92JVzr1ZNYBBbzIYa-zF84Yr5MTimnZ_lJ8vySp4nDhvCEIMETq3ZXyvrzkwUqpVORRTDVwSI4WiZEeSPVQfCM0NwMYZq6ld8yACIhGb19OelemJI6t_leBoBwsPjWLfp68dYztc1QyyneNBW5-Irbv3aHMTYBKLWUOYTMichW9zYzhsEFoezJN1jFa_KN5gxL8pOY8dIXo1jfIf8kHqlpWvDNknT833QfyKIXwghPNc_oEKlDroHF0E37KGEeXFNfd0RyKMjaqkRUBXqehsFd3DqvhI3IAzKkaf__APwkXISA5yIVW3luiUTV5uSCl_Fhzkz16oul-lJj81DWS_hRkpqsSKgGUYLeI3uXt7afzt90xV6tc-I6ZEyRolgMUZtXkCFUd4lujgyCI4hbjdFSiD1dDMLR-UMyxgQK2N2PqMrSvZThm6VmfZIMTyE52BhN91lPqvzoZA-2ynHsUMXnhhNv0vqcA0BcsWsOAFDv4VOSL7NHitJCZYMAE1XGGDCSWgOWApM_VIpvdZvkLPedJWGQyRX_J23XVCxXbPflUc7ZJT0F74GVzuvGF9Vxkvd6VqBcn6ARsEEkcj5jUVY9UA9_1wUi-RvNTl_MCvRMmxYxzWVVmeyI25jbGbp-CE3z9QzXSCAGnU1ef_gFkEn0huI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mulPEaBKwKH7YbCYJv92JVzr1ZNYBBbzIYa-zF84Yr5MTimnZ_lJ8vySp4nDhvCEIMETq3ZXyvrzkwUqpVORRTDVwSI4WiZEeSPVQfCM0NwMYZq6ld8yACIhGb19OelemJI6t_leBoBwsPjWLfp68dYztc1QyyneNBW5-Irbv3aHMTYBKLWUOYTMichW9zYzhsEFoezJN1jFa_KN5gxL8pOY8dIXo1jfIf8kHqlpWvDNknT833QfyKIXwghPNc_oEKlDroHF0E37KGEeXFNfd0RyKMjaqkRUBXqehsFd3DqvhI3IAzKkaf__APwkXISA5yIVW3luiUTV5uSCl_Fhzkz16oul-lJj81DWS_hRkpqsSKgGUYLeI3uXt7afzt90xV6tc-I6ZEyRolgMUZtXkCFUd4lujgyCI4hbjdFSiD1dDMLR-UMyxgQK2N2PqMrSvZThm6VmfZIMTyE52BhN91lPqvzoZA-2ynHsUMXnhhNv0vqcA0BcsWsOAFDv4VOSL7NHitJCZYMAE1XGGDCSWgOWApM_VIpvdZvkLPedJWGQyRX_J23XVCxXbPflUc7ZJT0F74GVzuvGF9Vxkvd6VqBcn6ARsEEkcj5jUVY9UA9_1wUi-RvNTl_MCvRMmxYxzWVVmeyI25jbGbp-CE3z9QzXSCAGnU1ef_gFkEn0huI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9vxJU7M6T_G7EQHrTg3lRgnHdlr4RraLFczZhokqKrToEqCZNEm8rhx70bsIg2QplQNOjf1zTw6h3XVjSxoo_CJd59SBi7sWSjcqNYIobVC4_7dkxZeOApeP40J8aDyqe0S4yKojs-GsBsn1hAFYX61BnsqEZO9ymC3tIxFjXZPCATLf5NGTMReysnJmbFuyTO0vEnw6lJk9S5CCGo-ne8C-OZsRQ01xgNKrfmBh8wowrmCPu2kvt9dcWNvChw7MZ9Kb1JcI3B8WmfMNPrrENRZfj_-nNUPDH264plQMIV8odpdom5bVY4R6UvczNOpiXcbT7hWirXSDbB7onXPew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0QlBZvBzSTKyYwYJ8NpT8J5n-RHUCuEA29-pUdCKENI7zDFnUxMXpfZoMUs9QhgwUmIu7fvFDV9gtA0dOREafkjSsPn907PkraBSaV4Rki3Pumi_-qQrPHWrcpQIuXBELIvxvNbyqikX_5_XAkirA7aoG670foieb31PUNKQ9YFjVZjcO25pRUSIJLDzL4AhhXRHtsA28KqO4tCW33fcYfj74ZPldbFwirWMik20cK6GvpnJgCRQ2TtNYez7D-e970_45vPi6SRH4KlrltmUB7vxT8ipoD1tdoRCSu-ImmwmrsNNJYDEAIejE_H_gFy2Juedl7K6MwY9BqWLZqW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jtbu0mVgOm8G2Pf9diwYsDh-_jBKPMF1izJYFsLrZ1uc6MxMF3nBnfFhsCcP0VsRqbfiZkr326Bz1STWDrajrky8MpERlAb8ONhL5XXd9482p8d35vFXd8j9Kpc1OhpqDCL9rzOKN5bg6Dl9a2iNhHZpa7wt7OncugfuzkLa8hQx_19tEZkSdygaJ0MCvIqExsw_9u8L2nsoPcDnXYHcgRnbBrenUERsQ4xMxRM-o8Rxtc3WeUgbrlpRSFy9mwwWE3ycRxIboooNUcqfTqOj39bnh2Zvnlw8Mjl0H5jLx5msZifMbziCTHr_g7wxapR74e2UTmU2TfdX9U1ns5m2gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های وینیسیوس جونیور:
• 2021 —
🇧🇷
ماریا جولیا مازالی
• 2022 —
🇪🇸
اِستر اکسپوزیتو
• 2023 —
🇧🇷
لورنا ماریا
• 2024 —
🇧🇷
جولیا رودریگز
• 2025 —
🇧🇷
ویرجینیا فونسکا
• 2026 —
🇧🇷
ویرجینیا فونسکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=UvjFZylgU1SpJm0_RnKENF5Rm1sW35SVoZa0jpnLhuVyfC-iINZjv-GAGm4LtVQwnMngJwJiV4Mdau1auzU7iRUp4oDDPyRK-010ZEUj5SXs9RNx8uKTFwJcXpcNkiMXIZ4rvTpoKJuOcXQ056iVVJSLE7gFRSsc5kCBDj47bsUPaE-a183oaQ5KaT2d_9_DRMJ1YSFWeAGy2g3u8UJR4uSnfXM7xP_5QxnCifP9C83yfQfX1hpuHNwMdgfTs1OGiL_gLYUOG-hfG1R3otGrlunGhfD2WYpv3Js0a0f_RGwZePAzK6VMArgF92NWTo4CBtZvQACuu6vdky7b-pOZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=UvjFZylgU1SpJm0_RnKENF5Rm1sW35SVoZa0jpnLhuVyfC-iINZjv-GAGm4LtVQwnMngJwJiV4Mdau1auzU7iRUp4oDDPyRK-010ZEUj5SXs9RNx8uKTFwJcXpcNkiMXIZ4rvTpoKJuOcXQ056iVVJSLE7gFRSsc5kCBDj47bsUPaE-a183oaQ5KaT2d_9_DRMJ1YSFWeAGy2g3u8UJR4uSnfXM7xP_5QxnCifP9C83yfQfX1hpuHNwMdgfTs1OGiL_gLYUOG-hfG1R3otGrlunGhfD2WYpv3Js0a0f_RGwZePAzK6VMArgF92NWTo4CBtZvQACuu6vdky7b-pOZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEuZSBx-Fwn4M0lUzjTgGhGVppBQ4KI3KxunP5XrYV4ZNru6TyZGn9EM2FGMwR93rQ7UTvVLGqtY1aIG7f35wtfsNsZ_0_wjjzVJDO__Rb91WoPs_qy9LdsNsUTqJZxSrvQm8yXqCOfzJKuh-TcW3ZxceSBiP1_a6R-_3oopyhLVwJN7vAO1kkHbpKRXWdgmk9xEah3n59t2d7v32NR8TkIiEcv7RObCC2e4eVWkoc5lKn1yKaxA_8701PwyP_5LWOQvUVzjXS0uXBo3QHDHJkkplrbBADGgrBiSfWIUNZkW0qBwijIz2_Rqc21ENS8I1kLy18dWle1388-q8oAdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇪🇸
رقبای احتمالی رئال‌مادرید در سید یک UCL که با دو تیم از این تیم‌های در تصویر بازی میکنه
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8YfW2k2E-Uz3xZvtFz_AakMarXvI-N3VVJt8lpX9N-L-Tti6utO1ky0riFNKty5tKPjtWDAKz5X26fxYs52NkWBwVer_IKspcmQqUAOHlVy4b0Lm8aq040A3U9K1p9bBg3T_e1cRG5B6IM8yXIOZgR_1EgnlnjR6FSqHYDZ6Gdi_NaO4K6FgTfLQbiFscQ5iCV5usTvvftIpi-AtHV4JZrrdRtlw5rDDXgIuXTQJi-VECvvn3afjAtCE-evKy-kQVQbIIsgVkNmt3meRnxQQw4hAdKrBRjkp0stOSo4bz9eVFQLIirF3lmHlboiDdkZhEZYLojabzPcFPbfeYnhbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpk8-Cql9N6E63BEFEnl5F-eVhSWch6_K5rXbqkRB4EYgdGDP4fghJdQ2n3ZMckUBdAG_2O2Gk_SqMe-NcY1g3nBR7X6C91LrMU8vglAPLRrK7WLtCTxbiMa_T4BwK9D9zOsqknHaDjjQsTwBnjybWLswsBbn1Jb14S6lLbY_lJ5FVOl2z-nZA5Fk_XYQhIej7UvOoIzwlygbuZCfp9-7NkkN35uhpQyJwfE6K1zWnKW-Oe34lyfeIiTeU5U0W9MlN8siXckMzy8MTdDefX43IFb-Rq7g5Udmjp7IsI3bnBQbtBPr-CNEhjE7S_YEWcB4YZ6-DoRcXsAMOMOsZbtqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=UsgcpRqPdf0AGKZeQ8YBjSrkFfnT-6QxFIIIsxkwQNxFWFPUUdYk0yTkmnwtFm9L2xwTpOJkut47T7n6KMIvvW2M5wEbDGSkdDe9JI3KdNzRe60gQwdtfu_0SUpg1PQedMsaCIa1QykhwEsx1a-cD9RNOGkcoxsMz_801CVdFMtTHPBSgDANWjjwMqRv9Ze-yZYYDUAYfbn5zPprKEDmEEQWoLYOijeGaW2fmFHe4fJ407JTQt3cO7tLgj8PeFRt_J2gCRY9vTvtSyqlJeYRWXDxPGjhpkbk3SYfgyvZ0ECH-3RTlVPb3h_CnMiCe9KoYB3RD3twucMqgcmTVmQafQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=UsgcpRqPdf0AGKZeQ8YBjSrkFfnT-6QxFIIIsxkwQNxFWFPUUdYk0yTkmnwtFm9L2xwTpOJkut47T7n6KMIvvW2M5wEbDGSkdDe9JI3KdNzRe60gQwdtfu_0SUpg1PQedMsaCIa1QykhwEsx1a-cD9RNOGkcoxsMz_801CVdFMtTHPBSgDANWjjwMqRv9Ze-yZYYDUAYfbn5zPprKEDmEEQWoLYOijeGaW2fmFHe4fJ407JTQt3cO7tLgj8PeFRt_J2gCRY9vTvtSyqlJeYRWXDxPGjhpkbk3SYfgyvZ0ECH-3RTlVPb3h_CnMiCe9KoYB3RD3twucMqgcmTVmQafQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=H3hFgIqLgkmHcizok1g20nvUdo8f9KrtMMNJxA-_4B4Z8glsY_liqv0Ye_4GMgwYm8O4XRHgolCVSb4NqY8xloJOZ3BNw0rKg5HFv6Ic2YrHJw_CpNrzzVIyoxwLkfRVZgYncD5z51lMjjTGSTZqNwSdz_prJ4vkmYo_U9_uWQ6JmNbEKFMKbm9-dVQQeW9mVlgiyN50xwssONc2JLPh-ny4QZaZXD7G844Wusb3BXXIcKxDkYSPIYJ8nj7x2A0nqQKLg1SPdsErLuslQLDEMWpteoWLrTFJ9EJk0Pp3V8TVhKgqLRwYLgLCFdIHz4XhEedtbvEn6AJMXzSjUKQNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=H3hFgIqLgkmHcizok1g20nvUdo8f9KrtMMNJxA-_4B4Z8glsY_liqv0Ye_4GMgwYm8O4XRHgolCVSb4NqY8xloJOZ3BNw0rKg5HFv6Ic2YrHJw_CpNrzzVIyoxwLkfRVZgYncD5z51lMjjTGSTZqNwSdz_prJ4vkmYo_U9_uWQ6JmNbEKFMKbm9-dVQQeW9mVlgiyN50xwssONc2JLPh-ny4QZaZXD7G844Wusb3BXXIcKxDkYSPIYJ8nj7x2A0nqQKLg1SPdsErLuslQLDEMWpteoWLrTFJ9EJk0Pp3V8TVhKgqLRwYLgLCFdIHz4XhEedtbvEn6AJMXzSjUKQNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
