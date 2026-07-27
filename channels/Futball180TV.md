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
<p>@Futball180TV • 👥 522K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 01:05:01</div>
<hr>

<div class="tg-post" id="msg-102109">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybq1YgKOGHULljLy9Qek0vILtHE98QARS4DjLwh7gm0cwh7q9jw7zKTiqanvTIKyIcQgg4z6NC_1YVcsXAZb8LaUPfjaG9WhaLewRFyClATUp46DUbghb8w9LJgB721redL5mX1JnH-E3nEt4mBxWw_XZ1rb_tRx-CX_GPz0AiQbNW0NQHaYyIsKz1EtAlfjbu2deCzbvGoeYYhvEc_SYUy240SHK5kLoeWk4yaSMjS_cFrE-mC7cBts-kVQ9zoWCzbDom4o0J1z1HCxEN0RMi2zzAymLW8E6oou4skMt6hF4ZYDz1dl2AhCgUoO_5MYfFazCKIeVCTVKtSCtz4k-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
‼️
لیست گران‌قیمت‌ترین نقل‌وانتقالات تاریخ که ۵ موردش مربوط به امسال هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/102109" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102108">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uox_YV19fAFDhI2049w9ibmGW1jnmNoY8ZivgNdSZ-sXojkWYFd7yXNc3vqm81j6b3-nSp4E4HrCQU_ORkuGVulZEbtrzJuMAEoOlpJEwXGlx600LZ0MLM2ZSQetoSylTD6VyjTJcaYGDgcWlccFN8locHJlgMTW353vavOeFwjLRWujwYaExtEPA3Fex1lz9dzMCLavy6Ut8vDbXbb9YjhJIINkDoKmIj8kulKypQXcniMe-DpLQhzPWHPUSbX9v7My60ZZfUaTBdJvsjca0dwhboMALIIO3Qliih8ZG6vFU4hTVv8vG1a9OWBEg68vsJf7toiK9nbFwAANUf7CFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پینی زهاوی ایجنت لواندوفسکی:
لوا برای اینکه بتونه برای بارسا بازی کنه قید 200 میلیون یورو رو زد، اون پیشنهاد سالانه 100 میلیون یورویی از عربستان داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/102108" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102107">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/102107" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102106">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ5PHv0NJ8x-JaOtIAdjT9RSDzY7WNb77cBAF1dMjyETgfYC92feMGQpOxMS_lXKYsihec4QaRvJ-TkWyu_UcZFhm0sadnayH9115ncPDhohaVoCuxxliutGvWtDfdS0G6b9zknSY-WroGjNEOmvUPDQfzYb6qQLQ_rV43PJbSFAXKMv77CEauwv0jf1dX8fCfmRCMtlLeFH-XEX0GPKF2CFGuJKHx5CdKziXXYvr_wa6tl5JjwdP_D8h4uwd7Y8-POrPXyLyezcVFbhHUZOkbyEepypdHhrDzjUq8QQronXn1wVWRCzL-fLXuiUYfFstB7XtAmjoZVnWKYdPn3l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤍
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فلوریان‌پلتنبرگ: رئال‌مادرید از علاقه آرسنال به وینیسیوس مطلع شده و اولین پیشنهاد رسمی خودش برای تمدید قرارداد رو تقدیم ستاره برزیلی خودش کرده. از طرفی آرسنال هم آماده ارائه اولین پیشنهاد خودش به رئال برای جذب وینیسیوس هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/102106" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102105">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvvtkGU0_NXASOWuTkYJIuuD0qA64xd6-Go08A6GmGpUtL_RLEn9Bec8IUtSVSCNUz9iTZdldWzGZzwqdoWV25jcZj0eko70uKXz4khNfLs3wgovEp1Yqc_J7Tt4Bp9uCngUii5QiJY5yOVseL6WDUDRTPnyaKC8WN9f6hnIcS0L3c3vyPX2KlybTnO9uxzNqpdc9ims-jG9QiOgBNBp_QEUzIrgraFgrMjyn1OYZyWTKVvAjIlHiQD5QsgkOSNE4qVoCAH_53UIaKe6BAAK_mNtIIQl-qbX1PM9jfEPhL5cGrwKMLvgXPj4L2pgtqzt3HMrnuE4lqC63usrrYKIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: باشگاه چلسی موفق به توافق شخصی با جردن هندرسون و دنی‌ولبک شده و بزودی باید شاهد عقد قرارداد با این دو بازیکن باتجربه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/102105" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102104">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHsMGu-BDLirHCGNBhJWcPLF2TQ_QYd3JR0Kx8bRKRve_NlkWq_22wnrR-9Hd-9ek6LMgfDhUZCsFfsv9HSyIyZHbj38Jf6UdADa_dzvrgemF9GFpVPQ15vVQPzeYAsN7lksBmmRoY3e7iByk5vS9S_r9Alau4zi6OWK7XHzVtrsBKjdpiVRK7HeGnhQPoVJKZWVocgoDtRoGk0_d5BH_wt5MGPQAyxb7hdG5w7CtB54L9bbUc8ISpWH6c7ecZqDB6ep0g0JK4hp6a_LfbFGAVelluEQXMjUDIRoB9H2S9ptaogy7Cn32lYpfwFlyEnqyQ0PsBb8XHQ1GYvLT9pBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇩🇪
فلوریان پلتنبرگ: هیچ توافقی تا این لحظه بین رئال‌مادرید و لایپزیگ درباره دیومانده صورت نگرفته اما مذاکرات به صورت فشرده از فردا ادامه پیدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/102104" target="_blank">📅 00:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102103">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFQKwf0uF94f8BBXeH1L2g2iyl8xPKQYn77uLysDb6a5XCCQlFV2XUeqqwQc_aqmPC50iKC7LggCdujJj1nqu7aBvYfo1H9mAeZ_PZzx6AmHodZ2t93uS9j_6NZeiunxB8jVqDpVto5BzQGkaRtX6IqID2umHOQJd02dqNtZm5cTfUbqOShIDILLS9PqXonpc_imtDykQ5eZX3KcGbKFN-YGbE4fFjLX2kghyeR7MzpJ_13v21mzsyUHZMsF0uS7bfMcaPnlb1VjjLcBaQnwYyjfr7kM02o7a2iwqRQ2U9WplxkHGGDEh4P2WUm8AivnO8f5DAIAvM3UmP6GsC2ZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: مورینیو درحال تلاش برای قانع کردن گونزالو گارسیا برای موندن در رئاله. مورینیو به این بازیکن قول داده که با وجود امباپه،‌ دقایق بازی مناسبی بهش میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/Futball180TV/102103" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102102">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1pBgSJc-uJ-Gd65vg0tlWcvXcHeLlaA2WItRT6_5ASqnmpNjPs68k2z60zuJ9v-CQdpWhH60SoOf0awZMDQyhk7v0j1t8y6AO3HaZpn6Fd_4vBH7kTfhNbHUe33CvsxBroCKNlsBh9r7vZjmU9j8I6qb623djEvxajbC_hxhBv1HrwT7YVuzrwaPn5rXGKVbOl3N4nU7yPumY1Y-MK_qOGuiPVRICyzEAtEpQB16FUr2OoX3pNvoLwOMRdPVo9Esp9bqxF1QfmqHp4xBqkoZCeVdvINKm2fwcE47QinbVAw8dWIw_50WCIy2VDmJKG27dmm_8f7xChyruiouJ0cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
لباس سوم فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/Futball180TV/102102" target="_blank">📅 00:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102101">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/Futball180TV/102101" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102100">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/102100" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102099">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RihQhs__3R7GtCRLZ3b7oMPC9lINxhNQhMF9mJMnLABW0L8mfatevxnZdMIKlvDk17YvIWyR2K9DaVerkxnkmynesqvuwL9j-_UF1Qg4AFgfDyPLxYG921XZ3ncMaYYqCYEQI1P78JXATLTz_I2dLCJGptwez5MK_upgy2Jr-a8z46pXRYlk2T6UcMNyQq2Ef6M_kdHrBWZGr9WJ5lnXVpvJraM4u_YVi1C9O-1xLcSIo9v0o8Jw3E2ycmFxS_JliIIuPDJmGotmF24QXWDISkCtnVI5Ub-A-wIoe9RNq_pZb0wXE-lysb0V-XQTgpY1Qc678CXCvwr4vCZcyGvpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
جان استونز به اینترمیلان
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102099" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102098">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLyqK6id4V-t-IWovRQDl42kjBRwU1XpkhRMwZ1K3lbuAOyUvdMLPd98yL0yCGr_DaC-vsbuEn_asR-HsBBBk38C35sRlvjz5Sn0KOgLXrdcdxotBJZBloUhFZscDGY4dSyHglg2VRBbJovTwJx7h7RthOKljyurVw9phyCMD-NW05Su9-TCcQ3d20Z-dR-SLGy8fG7lZ67yN51OP61OByyG5IhRijqLXwtclV2i-1QjN_1D-wkXyA3hcpV09Zv0mopNHlV2T_kTt9wIRTfBf2EFrRnepQM01Ho5wWM5yJX_qOQaKaajwiCZLL_ArBqOK6By6jKPjK8UDqyaUwJtEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندریک و خانومی و بچه‌شون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102098" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102097">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js9Ad0nTl9roSsP8ycnHHdeTI7xD30XLyHaElqGG_qosd-NuAezsmIBlxmzJBld3u9dwzb7SEPOyGAREylwsU2EFumvVWZ9S2tssDeDxUwdns89eOr-cJU-IzSBxBUVGsOYzTif7djIrSg-cbqS9bivho54B8NCAjcTIi_IXah2l2C8JQ5BTKnkwYGes7kgMmv1UBUDyKPbtPWY9EWqY1oNCTZIHLfvggi5T5HvpZBIerZiLm7sagS2lKjYAiOD96jDHLh-xJYQw7JnRtE4-Pjio7biBORvmPeIYihlrHPeGvqRu3CBfGc2PucZSN9ktrQ2arsyegj7WKLkrUKmDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
جیمز ترافورد از منچسترسیتی به لیدز یونایتد پیوست. جقی 3 بار ادیت زد تا تونست درست بنویسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102097" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA0yZU_bjYgQrcImRTOsVWQ48FvZ-2SGuTpGQHiBWo5QjXX706EhhPAhjAFi8IxpcKEZ-_ajRXxA_bgnO4yfGhrpXUfR3eRXbjEn-iAFesmsqAPrilRjH09DvhD991E_NnGvOl2vYHmSWDAdaSB3gt9GdCQXJFafjv7XHlOo20A8vdzZrTL5tTrNWKiHJLZw8VQ-w9e7Fz-K_qqoefJC7BKSFT1ur9k1FmM4IwD0aB3mjDYtOHIGY-JlqwpWV7BEe8C1Me25Wcjw-Bs26HNBWy2_gMPXEPlprzef8u6onNKowK_DTGkS9qyJTxLb9WvjBczO_wVEE6VaFZVkDFvL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW_cJnSrzYqdDbtD-fWJ-snZhQyYvQ7aYhm3IrigwJdcJg8O9pSK_x3UbXdLhxPbt9g90EMujuXWrPiWC5-BKigjPxpb9pfGePUyPCi-OJVgjxttWgsWtNID_M6l7m8NBkgkcij5bcZqdQk2gvTD8mJbuPEhvbUb47NCXBjuCvCtf4RaDq5B2vGLGUgxHY0Z5467vo_DY07Nbc2WIdLZhEOUbb_UEyZ4rpIEr4sJo7si_FafT-FELyLTKcHrs0tY1p0he9IJezkAoAamUJPJwYwtknQY1_fOO4LphkM2AHWzZcnoFyE5mOvcZSneLC1u_K_p88m8KFSmB0QsUHpgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQjs40IEYNXOK3vqVKyY0z3wsF8XCgxcxR2q0v0k-L-E5bVLa4J222RZJb30DyWo2fm8LaT9khDp93gAMl9IM2OWJV1OVyM95gUUeY0uqu7Z4_Tb0MR2sspmjkhDvmbrPTpIRifNKe1xahExr3eXyIwbdNGXeIcLQwhX90YMBHZfbkkB7WbjPk6pM3IjuIUAWFnk_uJM2xQOeDYFYfXNDf4TwfXIBj9CNVk7Ctd9zqFKqwu2y21RuU7X3by06BBycdE2gAbqswbKccUzKPAdQPY7-PjPwtFG7WwsW6AO43McBFm79eyio8fWNsiTBa7yTauRLAmeMiEPMWUWdmB7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZhcB9WE-W_-6ybd_nOwmeBA4C2JqGv8tzmRoHY1UkgZPRGRwYG8PmV7v1o3ElAqEGRW9hLLTYyPv9z7dJj7Qjt2d6Qea7zBQP4pus8imlGx6EtBzH65jdS10PxerdKlMQgLvuwD7vWFxLXrQMu_Vnz2VLF-3wt_HqqZVpof_OjHGtgpKzwC_Mw_G7heWjESKv3hggi1XtMRwnKBeliFidULWPSwPqwNpI_TgHCZFu3P7OEI_yajU31KLxry1diM4UHdKOjpcwKmHrgnSFG_e_xo7Ueno0iGfQojGDyuf8xvwH2Cp7qC2cGyYPVXucJ-iU_Ru4b-eEVE0jvyW6idLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEWTo3NM6WoKMVaB7-V02yR4uYUmmA83gSaZbx3nnbb5sXWskAL_QHouS61sg7krnybGkRdQrdcLLQHku7Bd1RKZGI_qx_LI1iGVZNOl46830Rf8CGZhiVwToZaPokA6NlBC7CjuaUQtsr3HuciyyX8Pkle3HlACjc2wcSsl5J1yyYKveduXLsWHvO5PMHMPt55qg2rW09I5t2EtZuV-sBFcOarBaXrBLQSgeqPI-MzXnNd2p7dvO0XxAZfC6Tw8GFrqpGfSJ7Mwh-hHhTq8bjqXD5rbje1g21AJw1kizhrPaIEU8_woTh3XVpRDuTA6rj5ODJbbMjSZ_0wPMsmGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dnu-JOERf7PjaUTIG0kaE5tfHOOAyFEiIKI3m2egDRWSqDnm8VFTKMJVRODTmbkNHUFV7qBDLwF10c2mf90K3iUk2gQq94DnMyCaQr6SCDMN6rVwyNFKkzukTogZZyMReALRk8GcIYHbrTm9kcsVO7spW9esfp-TVh3rQnv2O9zXDg5ExdB2_g4C9XmCjdCujkIJWQ8fJYhMT6Rb-UX5MmZycJ69ACeKMcSgRTNkWufedpu1Hr2VGmDYkKEUJouj_SDPgoEnRglwTb-ECxJjlcIWdIoUyV7OVn0615faUs9HzYUvK9IDgLrPayhfoeb0nxKTRYsfgnV-E213DaODiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbB8yRwn7hytYAYdczDSMLH4o26_b2obI01nd1CH8fSPFN7oBCDvMCezK3rVbXeApfcl_g-2Dyg43YuXkilhobHX3aPPo0Ytm8WmG4hkEhtkDNG1rJ4yQxbHgago3P7x9Bin49Yx_cnqSxQkwCB8kz99GNe5aTP4Ut1zRi51MPEmHE1JIP1jocPm5VIREYb9-un9cgTvvWusQFD9ZZhUAGuyy1flJzxJSlEjosTvCWqlckEcT7gvDlp09DhRcvpSx3y016VLR0FYXeSHPcojkUiIsPF2fMgR6_mTQYgR1pEo1HIJZv0Yb6D_vJ-ARifjkxtzudPqTOzKEgU9f2CTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjbNAPQeFj--i2Y5rCXYf0uihH2yGe_Qpn7ANUjDcRT0AgpVhqLFFxZFRf4aFlOSXvTvDz0_Yu7PTwWaMU0Zpa3Zml9TO9Z5rQrArhGxwsoLdwRPAPYW5UwwE3hB4YuraJehBXBbaNptGC_IrPbxwm_fHHfolIkvAr_cciw9D__KDijeZSf4gv2fES-KeIM0igK-e9YFnBdw0hjwsw-xTgfI5eC_ry1l54vnulyPtwibHFd-HYMC4S7kQg2hTSEvQNhu3AjuYhCfqGiYKF9YIrtub75_gkj-a10nl-edYk4RHsiczDSxfirQpjuTRu5-I8cp08EsJRnRlKxPt_6kTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVrJ8-aq1pyQFk_g7_eEVU9rQ4Nzt1kQkMz1TR8n6grFFIt068Ig02rD2UbXEUwWwdYr7OFSHe-lgDtYvVHm7PljbS4Qk5sXJfQeiJMEr1AdzjAkZuJabNLwZIOoPn-ZgL46ki4j3Dp1Z4jhPqIGrAgVPa6bbZmdeMY4C3NmkZrZm8GPdb5MigvGbQmYh01p3CyuIuEInOMRjKvhmy8gDU6ye1GVPtChM921n_wJvGcB4blBBDlpEms0OtcYHL-4y5iEc5_fraH7jGdGL802GTxyhAV6eedNppzZc-zif0tpNdT1OmTbtPIlJ8G6IYNFhSfdWgbXkcYLlWn1GZTHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWHam_NetwC-s1mGyBF2DzN-NLqZgmBoO_yCoRUcGiwkcAq69vNj7O0q_z6KERzCc3pfwoRyneassThyjjXvJmxnPbsGn_zh6ffb3xZIniVO9ljRTUFNAL_QC4CiwzpBdc9Ead4zjwIrjl-Ten3oG17oddLMtzw9MBRv8t7u691xSaKy1doKIFP4Lpp3AEn0Tkaa2KI61hFgCfQimDrB1LsYwxyKZFkJ8P-wpvEpVXSZT38Z5dxdBnmoiueVjuooA_hrq68rzt24kKOSuxPMV3GPjawfVMnVyk21kYABVGeGVreVOTREZQ28nfp3MTSzZxLPDJSTtX9mmj1RbBup9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBL75KG8JpU6hE0f1JJxiJjb1kdc5pvWRgnb4ViIP9k5P44oSqsZUDkIdyFm4VcELMUY4FV3VcIel_4VxHB1RR8u2wVOlYGfsIWT9cpiPXjuyJF1xCB4CHMkWCESeeu1Ks1go526cfgnqqZZSAdV-M1EUrd16aQhlms2koMt9HZSbOM6g7jI_45AKlk1guvOnxU9JMEa0V897doZRylJwXLjlk6W8noYZbQbypCiGrMWapZBSqmPn5vBotpVISZij5v4vkV_8SU7TlXPXsWQyM_NX8NJBhCzHKsF_0i_--IzuZtjTDN4AdwZq5KhPB8r_0k7QCWgwj1f0D1gdRQGJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgtSL0WLvMQSg0lxmyyuLbQifxL9SXDjROYRyBrARLeZNpz8Twte4wJBzSRU6Zm7b8IyEZrCKp4_KaUTHm4lEmtzs2WKEoAKkuE066KfNH8wzdo_OUqgbTPCEn-L5RRoFJa8OhAw8QHMIyn9wrAyA20iCeQmk1QAgcOZ9rb3cMc9fLEBKCtYq6l9ZldjXDx4f6y-woqWQdQVVzBMIkVyVt4djRGkT3tMaQjV9gAk5io6SU8jPnjVG8iNk3JlyARD_wCapfK2KWmSQry32NSd7-FRHmmjnr-UGsyIeNYJ-Z8xZW1IPfqUQwG7lAyoRsB1V0O1UF3DYNv0OFbQv3hgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⚽️
امار سه فصل اخیر جونیور کروپی که ظاهرا گزینه دوم بارسلونا در پست مهاجمه
جونیور کروپی ۲۰ ساله متولد فرانسه ، پا راست . پست اصلی پشت مهاجم ، مهاجم نوک هم میتونه بازی کنه.
💸
ارزش ترنسفرمارکت ۵۰ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdHG2lJTESeRDGSnFr0Fghgst4M0yjENYMN-NwMnPY59nuBQY-mP1XXCtdwYoYLCbaluSTH0P4yspzeyeC_jEA9v0kNVMiGem-YbawMHkuLHPDB3xZTg5xdUW9hnPz8LNx6Um1nfuz1g9dw3nOxyegJSOvnMUcGjDJcsfWDsGp0fDd3xrOMvoyayqVApJSLji-O7CuzpTUaPBpgSJhPJ5UAKttHiLhv9nmXf0Rrbcv0NxTf1MvzVIiaEe1MIS3OLr0xQkacz80otnqSq28hRGXlMmHMAkfUOCVDrGI1Xa0P44KqEsBcO6IaLDlRLvgIsWB1GncogBRG4Rofca2YIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7ooaVI_DvXbplMBM_mWIcSUaU5gp70ZrlGnwfejtpS3aK7AXhdlkoqIjZA5G6EpWHLT87iTRchVuHWurSY5KS-zAHwkynxPDzQsTT50lxCFUhzciut0Lu5135VCbMqFtNnDjX7h87VKefvmutT325_oJAeKgOUJd0UQImuNLZN_emiLSuYRVq1zc5bTt1VsiizA4ITp7lPzJB068tvnKqzmdOic4hZL1BaMvFSqfBP1_9jV0JKvzM_mfLu4uEINk6WYofq0L3lMIGvT-Z0Ust71L8k55HdCBU7MF9Hj5k1YNbKJdOSgzVyD_vgdxXdg9bPvjG6-ZH4g2SLrCsVjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru09_HfwE2SPkORjfDJSIa6ce_MJooCx5CijpBlTU0ZHmOCjLcYmEYnOkI_kZZQHvUdI7SFWTDoJCQo3VE08ae-UU8t0ADsHcYp3K_G2aO44KECshjiJSgTFm396yIukUVv1o2KDqRUu-iSGt1paqiri-Z_sUm5-ockCsHsEABPRXh04GtsdiJV85LNcJ2JdezcTaj2T-QbvKwvVYcd1CHM3tgh8DMLaFaKjaiFLJdt6POkNPGDO15SQShh6EJAEj_SfIzwAg1KDrG8emK9N2l4_J0nCa5vRAx5DWCsNFIe-q0b1gyfPFlfx296hza_hlmlk1t1TsuqbfvxWSmO3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czCXJ5f93YtMacoNjSm-GhMLzXLbzFewc8I0jdf4mkFTQxxgFycrXrj6KoqnqRYBE7SPsOQAECgY5-wEI39DY4iwMIhYCWPqrCK8TNqbx5QtJnvdZ1tCH6jF95p2xEwn6W17-PM8S-z7ZZd6RbUaMJepjdLqodPx8pygbz-WHhGTpttLNZaffrc-OvsMtY6VuZSLL_U53CGJ6VAYpapbkdWXDKlw9cZkL549WEjz7tOcZeOcmP0BzE6cG8khjnVTrI_T0PdOu4sCoJWN98j5zPJWWexiB5a3gBf5QR0ZDe1Ph9aN9by37kvRqZg_dgzWXCm3JeCmUXWDm9VTMK6moA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm6Igoe33qI_V3q03ogwEOWM5hwbKN6mSFLe4pvbYhYf4aiCEuJ9GzB6sAHojQ3U-QHy0ZuVfiGjLY-C1izF6AUuui6DIFjkNtjODxHZO0R9RC-eyR6m2alrUJ26mON6pRYdc8ytsJ4kK_jQd5wvAP17CcExk_MaW434dsWEMxAmPG_HxkJjlVqnKr90UlyL_A_7NBZZ86v-HR9SxJuSEyfKiXxvPDNxnf-KRPvK4niviJBGM85Hg6ZqgvSHdxifUiPQqD_lOYw-oAIql0P18_dbRu0RogJKW81Hf4-o1FRa0GPhH6ODAKyVuSiL3u3DKhUM-7LwzGSH3mlCqtqR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdANBG0UT5YHhq_refDmi7hg_DbiNfRTqZPssIOELD5rlsSlJPFdoIw4gSvmgWsRnopNEAWNrpgJQ8T3eLkfN9ys6OsfWWNemJTd2GPUkCRbPqxZcPO3xFMtyc10xVSxv-8hxdLwa5h27j4yq417K4oVlF8tLk9wJ6IZ8LJwVUm6pJafufmA5TGevCA4-MPEg5j2wJuFRJhuCsHBjK3VjAquHQiayRiBtM7rAwIbf8BhNKDSpGq_eX13oxPUELAgo-bs8VbhaEzhO9HHWyhpdZpaPCibeWhacC-hzso3qnGQ3P6iP2RNKLsExK0XHJ07zgkVmiIpWsPtDjgdoDAExQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102071">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy2JL5U7tDdGJ429KDWQN6otYVponUOQsSSt4YFQDa3WMOjQesB6O3QFKo75Pl81T2Vy4stjr6wtQLcCqmMfsibqIRNQiL2e41glUtvyL4y4VbYP58weK_Mbtp0oITBmBrnjqPcBzfNKeCmTWoP-l1xxDPuY8Gnhz11Obti-CFeznb2eBylt5RHERAeINU8C5tegaouWMCIi0uUGzPsl78DkfZefC5SVfF2WmAn1E8pqqA2a8dSz-aqUCsY_f-TIrxHLOVLqzBaEJByk8NoyEz0oShxeSkySE4vqR-L7RH__WNgnjj2D5aFF6f8DGSQAPaakwicVMoFxr3BkheWGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور دیومانده در تمرینات لایپزیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102071" target="_blank">📅 16:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102070">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=pn1QmsvtjTrok7mgIEovbSmLeX9yyJ_0JQTsxAtVWn9Zv-M3pZKEOHR7P4jqK7DvquMxQ3WY2JS16PtLIekMOF4fACjhapsf7XQ7YK-HX0CFf-Z7Y8HBtUQjj1iXd_bpTuh4kOYoMW0cHLgNxYOGVr-9ZjuOl4SVcTo_QqPQKs2rvo6wWTjnv7pWmR0uI8p-ZsOGvOPFfO9poXeYh_pW5R-61P1XkVdP04fssYWKAYRCgI60IF_cHNf9_gjZUShf-kdM4trwBScWSGO1XxPAVxh3lWmoCMGqvQaQJ549eR9eOKXhaMygYuTFc0FyzDvhbzOtofXXNPXzmvyWJNpRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=pn1QmsvtjTrok7mgIEovbSmLeX9yyJ_0JQTsxAtVWn9Zv-M3pZKEOHR7P4jqK7DvquMxQ3WY2JS16PtLIekMOF4fACjhapsf7XQ7YK-HX0CFf-Z7Y8HBtUQjj1iXd_bpTuh4kOYoMW0cHLgNxYOGVr-9ZjuOl4SVcTo_QqPQKs2rvo6wWTjnv7pWmR0uI8p-ZsOGvOPFfO9poXeYh_pW5R-61P1XkVdP04fssYWKAYRCgI60IF_cHNf9_gjZUShf-kdM4trwBScWSGO1XxPAVxh3lWmoCMGqvQaQJ549eR9eOKXhaMygYuTFc0FyzDvhbzOtofXXNPXzmvyWJNpRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
عاشقانه‌های رونالدو و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102070" target="_blank">📅 16:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orUoyUrhagI10YDYWkyYeyQMy0kGQj3JrY7QTNQcyFVnEdRXezLAoe-Qlxr3KNqhjG4OBO9U5jl80Q0arc3_7CB06Eswpr0FZqeGRnjdcw_avDn1p_a1TEQoio0yq0yVeed068kW4oZYmJKj7Um4U2Oq0hBmMSmTWjkAgckyCsLpvm0RLZ8zXY5GgkmSjPkywXSnQ3QlcdZEihnYq0H_tDuwaSmnAA7-F5Ry1rprmFu0Ro6IHkQLz7lM0_p-Dxo1q0qVHPkwtYUxpLbtK1DFMspu44SSZNvL1eNS_Cm3xQBBZ124VLWsyHYWILx9qTmUB2SXrSys3X0i_pDiV2QsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hz0DKsiVEbL-yb0JqYu3W4rWGK5xEjTRd5cyhUGbvHDXivqXiaFYxgZ3BXDKE_WKWZd_44ugE-aHwK3kpt9IlI2JuvexxCpnBFhz9NpQsFFci__hn1pSLcHtbvLqndhS_tWumEigkJM785xzz7eZni0uFB36vihBTPs8Mjq8p_NPN8M2q-_5lLy1ttjeZ2LJ1AOJRccTrQi0TrY90Uq5XhLFIi1QK00Z0vTxAyCq3aWlgLn_hLHhqbp3lg42_CHA6V3AgkQw7JD0L95qOMgiJR2QMa3bErIW_DgTBNts4vQqORYVFVBfd36deefieQkf6cUgCtVyl33fyw6XScEyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4D4XFOCDkFaGoVzJOqYAKtBUsi4pFNlCASqCmqlUqtZvFOngq5M33H7ZWE-Uu6wGnBtJB8aevnQYIcbYPzYKXDTghTMccZkEEuo9SZBKoaEazaVvEwE1pt-5afNaLGwIRdQnytryqka0WJFidRF21qZQrGYgp6_-JJjOR6YMyj18e-1uFBCo4sbKrbmuIetiG9s4TFpPDdv_eYJrBYb5JTesIheLMmv41cZEAgICGrxJes6OI9dDpKmPk_tfeRhKXmLSVG5qNj88kcVpKi5eUa2w8j7IOvuqyxmtU3aavJjHQRen5Kav049cV_E5n4Y7Kh5irTiPNVzJL5IIOYIRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32263398.mp4?token=H2_Q_-EuvdZbJwsLT8pf8Ag-5pgq3jNQs3stmOK0Bb9iYsJ8x6gRzyukvbOrakh3fyYll7SDZGpUwqVYPX_S6nJDPM-CSDiEAmu6XT_8HDhLC86AOcLeLGk_ZB1evlFoYFTbFWEINsMw6fOpaoBsfm0KIRBJHl59mbidcMLjLCxx5lIgJ0JEEAj4Lceqki1NT-qdrdOeu6OojUp9vVsg1Mu4C5iKMJGGgToSl84dGBNBgmKl-hCPqHlI12SMUyGzgFqWizYzJ6e6DdeRvu1or1L6DT3Y4tgCr4Ya9Y9qHltE7ahhNf4Lx8v2xHh6NMM3qZfg6khB2NymEKkZiIbFJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32263398.mp4?token=H2_Q_-EuvdZbJwsLT8pf8Ag-5pgq3jNQs3stmOK0Bb9iYsJ8x6gRzyukvbOrakh3fyYll7SDZGpUwqVYPX_S6nJDPM-CSDiEAmu6XT_8HDhLC86AOcLeLGk_ZB1evlFoYFTbFWEINsMw6fOpaoBsfm0KIRBJHl59mbidcMLjLCxx5lIgJ0JEEAj4Lceqki1NT-qdrdOeu6OojUp9vVsg1Mu4C5iKMJGGgToSl84dGBNBgmKl-hCPqHlI12SMUyGzgFqWizYzJ6e6DdeRvu1or1L6DT3Y4tgCr4Ya9Y9qHltE7ahhNf4Lx8v2xHh6NMM3qZfg6khB2NymEKkZiIbFJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزاله اکرمی بازیگر: رضا عنایتی کراش دوران نوجوانی‌ام بود
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lwl5GwU2_WPSyeLM1apW0RGYIAmjIzoaG4Y9cZECh5E8YhcZu2p_QJAwTHIefPEpGo93op2Y7ttC3Hjm7PJvTlo8PTEFT6fa7XkTXkBYkROryu5e7EHHSnrHA2G0XykKfv5iqQv-5_5s9rZ56B-aU7xvHiTWfU1vUte6m3ODBacuijZlYY1raeMXkU_Xy3kUcJ5GjEimO7KwJXH0Yzfh3Xqm62odUxpbX1GAhniR385L6ngj6a_KZpqEfOzthSCSzjoh5PvtUpzxoLM2FFt4vWL1l8nUA67zsgjgST0XmoCq3liUepDph3WatTu6QqW5qYxmPEqAmhHaBXioEP0i-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQUrjA11MZubmEyqcAn4iqMlwLNQvajPRbX9M_V7uKDvWYXrwECak709F4RRs0vntqirshjMv3V2OcMjQa2cvJGxJeKipBYXEdNA6dJSkmy0RP6-iIYJXmV2uCzrNEKCB189WM7_-FcS5w0NeUeo9tQ8zQebRmlq90c4KcvkdzVCnT5CgiGp15Uryn3uhGJMhbs76AJA4tw4FvJwCicuZCzjiwyEYO3H7aF034MWpsT8vdfdNR7UAuhSLXl2qutA96yT5SgUe_lXxo9ZOW2KzgglrDMrtZ_TmMw9VtdZCe9_MQsn1VDQQR5Ougj6OrBi-S55pM4nQYcmEjruynG2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sChJWF5oIqWhzwWNzfmoEAPh0zNCaca8H2dbM9QBESmABJVxkZlWLKFD-FtaWuTvmUeoNUG4zRx4oOlVMmUpX49nhFcTk3DqAR0SvAnJxmdZUCWb20-rhQTf-V8oft7SFWCL2_AZjGjqLp-_XZAkEQj6iGdg7A8v_-mmyCoIJsbKM2_IjZSTBRQm_yNpRMus1qnrlIjCX6FfdYatryUaWDSWwyxvMV9rIfftolJKGtke87OvNdR7CE54OlPNmizb76Pz5SnSK9G5A1SCyNqnPOSeGEhVX29zcZM5UMXXr39km8oSvZ0IPIbVjEaZfCSXoqByPKu19NKUdBV1qaxpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=Ppuw877SF89XUEkTsp5yrY81aPaMBifrt8rHcuxvTZp3r0UXwvxpiMfSZ6GMHhKGbM-95C1ekuse2FkHvBSbLe-NmQg8zV15Q1dgPtzIMvDDETN1zKhRPSBoWu9MePSRSbA8LmP2ciIe_H8BWEPql_PHNcj9jrc5tolXgHoeoDCmdY6st-TDGaOabJ8CcbSk-ubkecZhkLbBKCKMn0IRCdwmL8R8QXSFSWuyQyW2n8go1wu4IX6nV2Ux2oJZ8QMQKG0jsh5tD5ODYKvqaSInrELeEUdzKYYSCZTAuhX4PLuTyigECPVRsY5kSA0yBzR9LCuloNgDotolULFo3_RIzr1iVg1LCexEeKwlQx75jeezp0PgLPyVJDchwNJpR1sxYPmBe1_ZXTMZL9MRx9UH2D_AyLD4zYYrBDZTkNH2-b2MO6hJmngRZfMBL-9NIMHmqJ9mk08VaUoO0Opr5JkJE0fBxrnWYfgw-_NRTQqxC_gDHxV4a2-Afzlo6RAOjAyP0vKa21rdQRtZVmhk1O7ZvT7kf6DZqNGVbUQf6kta0nBlIUzlCN7luIX1ZB0I0aS-3T_dvHaTfGhxDtWLz56MpMhg65_77SOayEK8tYK7kBnRT0FWpary8MBBqjv1XdI5hIffOZXdnmSTUNRQQ0BL-_M11XHMkEttMYyqPsfMEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=Ppuw877SF89XUEkTsp5yrY81aPaMBifrt8rHcuxvTZp3r0UXwvxpiMfSZ6GMHhKGbM-95C1ekuse2FkHvBSbLe-NmQg8zV15Q1dgPtzIMvDDETN1zKhRPSBoWu9MePSRSbA8LmP2ciIe_H8BWEPql_PHNcj9jrc5tolXgHoeoDCmdY6st-TDGaOabJ8CcbSk-ubkecZhkLbBKCKMn0IRCdwmL8R8QXSFSWuyQyW2n8go1wu4IX6nV2Ux2oJZ8QMQKG0jsh5tD5ODYKvqaSInrELeEUdzKYYSCZTAuhX4PLuTyigECPVRsY5kSA0yBzR9LCuloNgDotolULFo3_RIzr1iVg1LCexEeKwlQx75jeezp0PgLPyVJDchwNJpR1sxYPmBe1_ZXTMZL9MRx9UH2D_AyLD4zYYrBDZTkNH2-b2MO6hJmngRZfMBL-9NIMHmqJ9mk08VaUoO0Opr5JkJE0fBxrnWYfgw-_NRTQqxC_gDHxV4a2-Afzlo6RAOjAyP0vKa21rdQRtZVmhk1O7ZvT7kf6DZqNGVbUQf6kta0nBlIUzlCN7luIX1ZB0I0aS-3T_dvHaTfGhxDtWLz56MpMhg65_77SOayEK8tYK7kBnRT0FWpary8MBBqjv1XdI5hIffOZXdnmSTUNRQQ0BL-_M11XHMkEttMYyqPsfMEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
درخشش‌های فصل‌گذشته لامین‌یامال در بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeInMLDRigYitoNFDVwW3JPzr1kZPr71byCgjKnxnKWhAMuQf9nRqOPTOWjUcgCO3CkTkuZ4cniDJPraCGD3Y8IyX9XiKFLJBTtlI28y_3wunQ4uJpg_845Vfh744neO13vLfpYFJKCV7s_3FVgVT2PUjdzmdOU0rgXXgxZkz_CBV_04ard2zTiRSjyKMj7hHIRagZBue4y1FO7hf0eq_9fOkcNWUjeYnIWSctkeZo8VTZ-qD43J4sLeC-zW7ys1tNRvPwVsEHBcqV_htFechxDXkdUUM5HMSn_jn5NwbClde0_nDlkqx_Cp9dIe-Rpqc1IqIOGwu3Xtb6jeplCVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102058">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLipo37XpQRJjMrnscnAYXoqEfri71pujDL5k7G6bl76kaqnvqlgACOqEYvfRbwBVHteqZirmXB053r1AaW2MPROLO9F60BSBzP677rU1X2kdbqyfqswCMFSSjDmLTjE3ONt4kQQIe_fWsBqNZ7XIoBLe9pqV2ld_i9ULo12ECr7lOGT3WgmY66ntFrxJ5glanmx3z1tebaAK4srROS9HRc060ropQRHNUQm2nPkseHBq5cWIA5T_P6kNCTrbewPlrwZ3fBrhXw30H4H9TccqgNyZnxW5DBrZRfrK04AYCnaXYy45pp01qDYwCSH-HhQ6EubzqrGhtWa3CwUgzcu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olfgU8RdiVcLsHfeiGMsAO7ClXoANC8-2Xranav4Wgk18KM5UfNlFBHX7Habs8zabT2ETZpab2eQIwVWKO2W1YOwl9-LJslyRgpp3PCUB5wINz0S4WirdASasMNUWnxBr-BmQ4raXwgxlerM_mrUsnFC2ZaKcJhYWBMgqBgG6RGtnxeHnwMCfIzYI_xxmkTlAkoaPLwLLLz8CksXCGEgfWEnnjTXnVyLN8tt_V8EueOCJxdbFt5xj6wMzbKs6f2at1jcUszFw1cfB9053c1LXatw3tz4kEslnAIxyPzxhptFQ9BnwPtfw9HBC_CxOWUcMGRK4ocYZ6EcTITxlavl9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
نیمار:
وقتی در پاری‌سن‌ژرمن بودیم، از مسی خواستم پنالتی‌ها را بزند، اما او گفت: "نه، من برای این کار اینجا نیستم. یا خودت بزن یا بده به امباپه." او حتی برای هیچ‌چیز هم بحث و جدل نمی‌کند. آدمی فوق‌العاده آرام و صلح‌طلب است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102058" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102057">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772e430691.mp4?token=F0BC6Rn68IXAmQmGl7X3vRtDKPltrJJEPjLV9FjIpZmDWgxTCvdPIjwJm30xZJ6nMKarmstcWa5LlqQR9BwfFnUDyyqDI3J7oSqi1KyCNGyUybIEXBnd6aa6FML45CGrInOefyqvWwxL5VHo7XKH897Z7ncilD8S2-yVQgV-NYXYPsmH0Sjf4zkpCdKUsNFqL4ibGDvqOXCeCtIYBzyog8LRc5uws8oKJ-6jz2hFftErev-iVpqzcfTBkifJk7ZSIU0iPjvsLq3daXlyqKyY2_F4MOG_yJZYih25vtv1fOfn3fxn0Rookbpcb2Hwj-zf4lao8aK-kOEGKbiPF1UkmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772e430691.mp4?token=F0BC6Rn68IXAmQmGl7X3vRtDKPltrJJEPjLV9FjIpZmDWgxTCvdPIjwJm30xZJ6nMKarmstcWa5LlqQR9BwfFnUDyyqDI3J7oSqi1KyCNGyUybIEXBnd6aa6FML45CGrInOefyqvWwxL5VHo7XKH897Z7ncilD8S2-yVQgV-NYXYPsmH0Sjf4zkpCdKUsNFqL4ibGDvqOXCeCtIYBzyog8LRc5uws8oKJ-6jz2hFftErev-iVpqzcfTBkifJk7ZSIU0iPjvsLq3daXlyqKyY2_F4MOG_yJZYih25vtv1fOfn3fxn0Rookbpcb2Hwj-zf4lao8aK-kOEGKbiPF1UkmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جامی که داری میرینی توش آرزوی خیلیاس پسر جان نکن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102057" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102056">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF-DoKQ1xjCfLvjdn6kaPyDiAXRmb3Wdo04SJxLadjs3YSGk5plLcSF98NFyCPA_z6HAEriegSrfCEwHnyr4-tfBClyxU-gmcqCr7xBGuYvfxlZTQm2eLEZ-5WYweR8dUC8auW9k2UvHDTTou041g_cqrUunqydzgXLaJ33Egff2EZ5i2IVl5_oCa0_xFTUDoo26Vn2WRJe7fTFlMKL30KdPIkaSdQPnuJN31enBGfDeaU4q79lvBh1w08Uz84H0ao4SQ0kzfPgAHoTfD5d_lwyuNhDSSg7H67cLQfqULLtOpAUmune8wfmfgY3HHN83dtt-cAbeHvBTMffhxdL4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
بنر هوادارای بوکاجونیورز برای تیم ملی آرژانتین:
ممنون بابت تمام این شادی‌ ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102056" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102055">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.  HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102055" target="_blank">📅 12:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3DfGa4Qbw5E9B3sAYpuZPCtytF5nH5xm3tfmGybREvGX0-mD6yAOTV5368nnTTN6-EnUnP_02fSonE3nQm8cDzsqBp1rDoB1_LL3bObjK55Pamg1mGuFNAhbjfvcKG41jxoX51a-z3gl8MkQv27IS-GJLVDnlMpgIwi0FNziDPBTKnXnCTwMQJfGpuocDr2XYfPXiMsMNWOb-MRqDRiZH2hhBU9NyENN8hVQQtRk3XiC5ynkxlvHq6rW9Vv_BY14lij3jr3gEsuqeogdkq_iFEOKWgYSIQ4QxkB_siwOTgF9EzYgpwvzn3qe1hrJtqEq7O8FBIh5vvLV2goiebfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8d8lriUFp1rWss4R0zSynVZg4vinY6WX1NpevjKlvtIHWNBLD38UQC5Ck-PkPz88jjVlFv7Vds-dS_ejmH75rhvnzmQ_qwQJhRmRtRijCaScunUw7e-2KqX9LXzXWlhUin7qcL5a4yIdw4qNa1-YEkCduJIFzl2xUjfN6qDDErGcH72zrwvTdWwpYAX_bUa2K2_qBQqvC6gYtvjWwm1wcIvWAnfGF2I-50pyEGPW7uWWUoi2JgYIMe_deWcWrS8CWKzvpTsIQ4OhFh13_bsBU1dQys_Mh6lvuXe0IXnFQ2Ty1mt7-J6Urn-mcgTo41zT1Dn52Z1WNWvG_ooQLhOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PE8iDWG-zbctYs5ZxyvxCDy7XJbUtmLTzSWn1niH0pPEAPLTe83HdI8RIVqpeqx-P2FSoS2ilddlUwaI_IDwHJnC1dIl8wd44qc_XtHWqc53BuRlhGVIpHXNbFSwW014NerwfmuFJXo-v06NZLE3SDZ9u970PjIugHPPWbxT4i9PS5iZaVvdUS6omFM4P9dFwem2U4RRJ-lLanTUpxNv3hDZbaEYvGYHg4iNGo88kh8FC8ZWvzqVYZxIoVCoXXqwKm-cQetTlatfSYBJsPAd3kS1Y3uQXZ13QWSvxo3Vzdvl7jBFYJGP8D6yaoEC3KAb-D8EoWq8pEobiZ3bB7Ifeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=CDO_NVhfQOpzqKpnLFJW_iF_eNeCJa9bXzcu6JUbG9rnoOFbyG4VSeXF6iZhWza5CNiRBM9N96u5UhGtMYbjwa6FDF7CkDEzVvZAlL9XeNS_BtqielsPxZDfDRACe4_wEUqbpkFjX1ucgJey0_naH-bKB7wWj1KWApo1CsKkGKPnNpRReXIyIjaM1JlFLeWUxxddKLHdCBR7mJ7A_rLfHWYUYBzw68aeOIEBKIfU800ED9pN3T4uJqYvgEY_T__meoiEQvJ0ZcYhqlt9wtvuuaP17meM0BWKZoKQBpSupz2RDM16Y-pqzIAG9AvDQovb2-kYssm3fnHp3IdDhrTvMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=CDO_NVhfQOpzqKpnLFJW_iF_eNeCJa9bXzcu6JUbG9rnoOFbyG4VSeXF6iZhWza5CNiRBM9N96u5UhGtMYbjwa6FDF7CkDEzVvZAlL9XeNS_BtqielsPxZDfDRACe4_wEUqbpkFjX1ucgJey0_naH-bKB7wWj1KWApo1CsKkGKPnNpRReXIyIjaM1JlFLeWUxxddKLHdCBR7mJ7A_rLfHWYUYBzw68aeOIEBKIfU800ED9pN3T4uJqYvgEY_T__meoiEQvJ0ZcYhqlt9wtvuuaP17meM0BWKZoKQBpSupz2RDM16Y-pqzIAG9AvDQovb2-kYssm3fnHp3IdDhrTvMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
🇧🇷
۱۵ سال از روزی که نیمار این گلو زد و پوشکاش گرفت گذشت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3s4wV5xWStfZvvEs34BAJ1OdF-0Y_m7mzd5tOKU5aNOD-frnGr189iLRJGi3pgnvW4SvGucg8skk5Md3oFVt79v5gpSsbRihILn4ViOiY9hgf4r6P2lAELnBa5xxkxecH8cvW70e9jj4ylMmA8Cq4FEdcQHrNQZMi2Vgo29KJGZVLHhyPrh32Bp5Z46JzeushXl-tB2IQSKOvzciOrgzY44uO-E3jkb4yMlmwP3idd9o9M0LLKr9f0fDOmS81aiLdMRvIGrIVJ12gGR9yBVYrfjhtpqb-qC_6kvw2crOlt-iAv9SDAZ02vAtMf3Pbd_Ty-UjBMfEuiFBOHovVcVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8QBgXraqA5lLO40ClZ5acf4MKhr40cK-2grPh9qvCJXGM1NQDHxuP2eYkxHvnKJXx3mBshUjp7fVQV5WUZnVpjVi6AQuDHmtoFvdkuTlpvuBfBRkBTHbeXaP0-ozVO0fseB8k-cyHKpfQ7n7kmP1Fj9yVoO34sC8kivTIhrDNc6hRt-mdUfF7TfdHkhi6fz0_C0NZ0JqWF0smGbCaefdrWqywpHZQLi_FJZA4uh-5WOPr5PfQe5E5R1rwYKA4NBVNQlGeN8BA2l8jkCjh6IC-z66gh-pLOHBSbiv00DWVG9kqK1Oyfp9x0jTX4MLaq2bZ6zwCtfs2CWlMql0_6DGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7slX5aeaXQKWwvk8DsAaMFuM1MIdBZ-ZRC3F5yoHlCaC-hrvtKjI9zxTU1hY74gYsTtVVSqdg62-OX9cKOd1sSAetx2Xt4cYF5KrC_Z6LI1Dzl4Z9TJToMJch4Dxz6qfzatM6XLMwW5LUBEB4EjdY_gXRB5CDVU72wrd2_sr83umEQmHmWrSErmDi-TZw2PmzuvnKLwatKPiYhdpOyjt89wi9AdOHtbKwdauWz7_PyN5wpB6NSpv543yttTs_N295l5v81eCvSZGuvx093d5jBDBxoAaynupeWnc4XXaxnQeJ67nD4un4llCZ_afOmOtx4jYoxVetZG82mr3emJMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxhVkqOK5a6TYklFx0wF8P_SS86z-F1Y3hQOcNXMIdtD8xRXGPpcZm4KZOhMICergzU6HQs30tEzKAf7ZsSlptUzhfLsScF-H9xiyCnUfHQ0qkOQAp4bfXFuBXjC95YcHHzUgp8VvnjnHAdsquEu0BrxgZhsFIqf2jzNVZ6WX2dK9vWSeMI85PMLb3cidYx4wXdQYc5FVt6R4Da50m0L00DFSwceBYWhJ_VPN_d3w0gwLe_RnZu2MDg92Z6HD_bUqlFi7I7u14AdyW5-N74N5mP2s6qHdpvZeOGyntG5L_LDbC9R4XC-RLD-LDycTMeJh9WcVcjBD9ZBqUKQtsxEuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NURNRsT6yszKkAxPVKnMXd7VA2CsUSUmxLXQ_Rc_U8vqLmP5lqJ9WVPoVH6BcQR4QpfK9r80jNLHDhLMSHx-UuTOuG58ALgxzPJqvMTRH2-uMLj-4yVrl6xwjGGdbl9IyR-Dwxri73aBC4rpRP5LAiRyixaDxEvqVhrAUyG7NKEcT_5ORPQ1TMJiq-SxiMzm9IjSfMxZdFtWI20ixDFima_bIJbOi59VKES7F2i2LouZ7JDPfRNx_09YQ5UL68e-bDl5K_8r9p-_iDdBlu9-so92E2VIZnzPc0wfl-M68sHEviUYqTubupmXBeGk52EX6nRgzvimD8sQWaJdvPhhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7WOLEUlVVpcj9MBRSa6hfLuTI7yg2J7FdredtZsCw2aECk91cVqTpNkxMKyR7_0VuzwDCXOo9VG7UPEROsWjNvA0ZfGaQZC-HZ8p20IufsdByl8n1y9TPnqd__0hfHIOKlbFc5rE3FFH-3Uk0JyKOoBnfztD01g5CbKQbEo6CJnI8u1HoLNVxZVYNucCnmLCbZ_gDzHlLE7FCZvKvAwUDrsuVFM95a8Ruii0lQPG-BB3397M9RAFX3heTGjRA8S7LgTQWTSr-PX9MQAkH8oDREyxhZwcH_izu7mNF1yGZth0ZlX11VCPLs7f6HgZNJBjJRb7ymytESqj2SI5RAUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو: پاریسن ژرمن تلاش میکنه بین رودری و رئال مادرید مشکل به وجود بیاره
‼️
🔺
🔻
پاریس از هایجک شدن دیومانده بسیار عصبانیه برا همین با رودری تماس گرفته تا اوضاع رو برای رئال مادرید سخت تر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k63cve5TA5AXQH6KEjpkdIJpEwEFtD2-6tFhXbRW_qnGLCbwt6hyLNewpOs-jcW7CJzfriaZtR-iroGYlTTHo_PEzCsfVCIdy7RUzvQWpPiiUQXxUlxbNJwuAISQsvY-kYWftu1T8j35d-TV6pJJ5ZeTEQgJEp_mLM0B_364biyzoSyyZyFIuWQ2Hpz66j-nY7RQ5_ZDMLD9IpZf9pFijdmcyulqS-oLJbWA3Nh7-Tgbiq0OovN1Km-UbtS8G_QNU7O-8CZdMFRAmPxEe7y6WFjNnAtwWwacOzlVEBgNUguFPh6bihdTtjuCr-QGt1sjgoS5Q03-m1EVGQ8xoZ31Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nupzd1iYnQp0TrZ7LkYBVE-o9yWJrAG-gTiX9Idq3JRdYskMW8f1EV0-kXK_NPeT8ANhU8ngBjxVC1xJEKj-n0EqTA8n7zx4JHRubLiB7SEF7hgo_TTz6CJAn1fqGtwK19ymsED3a9Rg70gcCbC91LBnMc3r9p7IoObBHZmBerlDU3BAu-NwC5EcXQlnX-hS3Ky-IqqglML6hW-tzpkESUspxc74N4_2eGSP9y-DjJ-9jO9WssDkHjLn0_bTjWrTCv3acW8bsx0v_-M7_GP2-6NmJvdmD3ZGTtFPpMqBRo_a7HY_2ZPgboXJXv2XpoZQUaz_3QrzH6xFKQ9OENfwUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTQKU5I-GgOAvd-2dLGqNFO0gJiTnhoJTw_PZ-viYd8tWr3-ZrQigiqX33vQO372Fcln0UKCZY94-yPgbRD67OaVZKx0_kMR829KJ3K5rUqZ0O8QBN9DnEIqcF5A85vdOg2k66TMLpuA-geAopfzEUhrjRjiNHttUZqJ7OngoFC6bkghEbnId44qjDe2BVcvoN6y7_4vTGl4uls0Z2fRWzutKgT7zmJODuIG7Ee0Opoj5m6euV_XZYf-EOfa57HKmmtb5vHmymikzbjb83-CTwG8AJuUlSEd_MOFe43XmaqpIp4HraBef6hGzbtLMG55HtPGCCfp9QDKcvne98Nfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fecTwxsOjSYhyz8xSp28Q0VFdHZjfRWZ_S4kp3hHkJcyF_Dv_naoLQy588RnGqURVYTvIbPKqeoriro0X6ta-UrP2pRriyF2haQZ78wFI3Dd2kMmuG7DLml3KP9v0oj3nspPe23d7ggD6IrJ23gn6WLX3DoD9SQEckHq83nPkyeCFt9Eyr01RbcQbTHxwy738pMVeYTnhzkyWA0msJ29tN4tVai1q4T25S2OwY0ZObWAFBOQ6tpdn4V8MPlTwgU34urG8C6zVIhEy9xwjTiyo3dzsDKLsqaZTFcmwJ_LA5vW8lGcjzhYow-7ICGp6YaIfDQXe5XcwCVM50KHNHY54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQPqKmlQf8_hig0tGrohNOrpahXQpZtI4ATRHMwXKlTnG7HaBDIsKcNM5HcQZnGlZt5kXLHEsmdp7xaG9tYa6KgN1sP9u3gHzGVHlVXQfZ6GE_YIS8Kin8Vdcu7LhOY6Zly_xSMfnd9BFC7PEe9i_MZCaplGRsngZvIU7G3aJds_GNDW3c7GliILLMfI9RHVY-akg677cMrY4Jm5Fv2MC74xV1gUHTPHl_Ala2niq_33fnCtKov3b9HmQld-Q6rVYp4DiUi5mp0nJ3zyZdLlolwozY6z_AkwZd9LXfpKHCQ56NQfBGK5_8OKzBR9qn3pCbWphC_krt90tXYWEIMD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe7O5MQs7AKgEsa8RZ1kQADpdkyRtPAJUzNegG2SJ7hMdUKJcQYbW7pLoMGMH-6DqK535jx_lmAD-P57q5b1GCBd1erws4T8ALDoP4BQI4qNBy7CnNVnzBLI3KZCxJ-I6EfnpGuRQtyA3egHpBKoLwdJ2LKFa4g1x3e0_RZ_Tk3W7vDibLlrE_oM6r26IGFXrmvoHcp4Kv215S_EbBn6Hc5ywlcgQ-iYVou5pPgRTO790Atz7lMVTlXFrauaRnepu57XA5myBzaKDzk3bKusD7Wf2djPR05wUo68S1uEm6rx7Tmg5qq8MMs_SSSyxncVg-6-7oEIWPtBQ1LrK384jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkGmd1p1MWvXkPke_m5BN4bFHhyTFF76-SE36nCZA2vo95ECERXfwBlRJZmwHAMkR7rTeX7lXm196YVBEfDHVAmMDK9lS5j_cw6Aew4xkbYvCzCiQc89bdiUlcFORy-0FhB25U_rEPZRRKnL3QQcXszgOPEsHMbfHuet1dfl2mnIElTd2oPMAV687R_l2Im3CKkWfUZNRbEq9hctq_chvjzxQTVuEqFAPp67MOKRrByqISCSEoQvHdgi-M--tvEOpU1QBq1bRFLZKuaPnqGa4IzbJZy73K1nXql9qcEEFbO-u3kCyz2UK7JmoyyxfA8OiFawA4gyEXwBZucK1423dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNPQZfDyKMHyCkPaIKJihhBEMJBwmdCWTlhQGAlp6mHdFFWSxlko5qyiHFai4gXFNRwWbmwWtCIyeibjzPkiDj8nvFzQlo0bssQgE2pNUjcQC-GRXZbCqTfLpIobQ-U0aFgDQf3cHs4l1dC6n9Vur607uPHflvv_zL4zV52x40vNQMSNfKDFoLuHLN2L5yReY3P3-XvrHTT6SL5ExnM-ZYh-kQMQwSgJRciY1o50cJPLj1xlbWO9kLWVrCexbc4MdqFF77cnBS076v-zxYg1cV5MoLudhmiLPWhtobvdzIgol8MAmhi4ChAN8p-B1Mj0tVJIs8RKGl5weM77BvZwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugJw_GxUef4EPAkBejojcBUKTSN1uLRVqp9YLdee5H6t4WRj5-fxfu-JSQ25eUVSCKzzVVnfnTFclE6vtdPC6TXmw6ya963cnS2WDJClC_LbjTN4HjZD8f4WMggNedlcVND8vI9-iWCOFj379BmdyufAQDsW1twfbyzf7MWQA87eEyVtqw5wfmj7KLG44SOcVprSLnRWZm0vFjjlodLpHIeaBnAt9m4peADO9DUlAdSGTWLCknj3pi-HvD_5UQrO6T1SuCRCfuquKWR_pdpf0K42CFPyM13sGUF5Htq9lsYtNo9oK6VG0gbgkXdnVOR-_1m_XepIYDfCoIbXZunelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBQg6iJENKcKoYjVVRiiTnPTOmoH2iTUtVXpt2g601_avt2Ja_L5vHsxcTBGfztE4mNYPFrbDqHuYXdjrohUpfszx-rXk8rLDcfnwulJAGiYWmgw0wUYLo6pi4mZYyVLGTSZKI1lEWdHKHU9Lje6_ENjAHMYtUz4gnhS2l_O-XX9jgFZc8Lf-tTa3MYJLKfDNYUsucktswdD-3RhjoVQQEz-Srn_7UEJUz7o7toTVH5FJChvkRSmR-JzHp06gUpqx05xjaAA_XalSj-MZ4lQiG3hImuElgk8Lewa-L6bDDLmjNmoygZyBgAAsoC9PZZd1wrI3XqwpvckRlVgPSRV6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzeGrCkGXjCVRK3to6XWHqs07O7jREMj0EjOc11QRn2ZcA8UAh1mVzwuVfKyOgNA-e2dd2WFI_wJKXUo5Ajh5lxJIZnKrm2RUJyvFPOfOiT3AkCsOf8bKDpd3jfHb1uG2kTyuBJz32whYKEryctVn79xxeM7RnB8Qo28QVwuz0pwKlwrnZxkQ-G8ACnkuUJFOD1Yh1hZimk2DrWm2unQpRWiN5Dk8_HnhWn0Kb2Ehgc37_fOBfBI0hmKtSxWXYg04WpMJwGPHOxgWp-Lw9BhDfAvRntrAbwVWyAWb9zFC3wcnmHW0qs2yVC4aG3dyprMBE0ShwA0ZJ4PWRMkLq_Myw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=qjsrCpdigxU7sDuFKs265hgZi5LgNisHfx_x8pY0q76hNr4CnbsWiEOVPWmKBnBkWGM9JDU0n6dpR4NVsebb50OQx-0tU4HT9iFq9pCSOhZAQn9Tsx89cN9ee5n-QMeaRXhwkQmVyMcGSF73Kttu-HYh9YE0U89zN6wCaPXb8Exhwhh8cCDn_m4dHXtnXXHPPzYXBYk1QOakAp83PY6w3V1R_MIhYsNsfZFbyuOCm_VUA9NrHomGHLgW974SMGgJSuS9v123Ek25hxoafouQtzmKMWDmg9IGW8WxtoO5mh_wZJceQ87ktKCJa2OaR8e_QYbr4Ly9kvTnT74wAC3Hyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=qjsrCpdigxU7sDuFKs265hgZi5LgNisHfx_x8pY0q76hNr4CnbsWiEOVPWmKBnBkWGM9JDU0n6dpR4NVsebb50OQx-0tU4HT9iFq9pCSOhZAQn9Tsx89cN9ee5n-QMeaRXhwkQmVyMcGSF73Kttu-HYh9YE0U89zN6wCaPXb8Exhwhh8cCDn_m4dHXtnXXHPPzYXBYk1QOakAp83PY6w3V1R_MIhYsNsfZFbyuOCm_VUA9NrHomGHLgW974SMGgJSuS9v123Ek25hxoafouQtzmKMWDmg9IGW8WxtoO5mh_wZJceQ87ktKCJa2OaR8e_QYbr4Ly9kvTnT74wAC3Hyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXdRgMDmxVJvBqh7xdzk2VkdmyZ0zRSfCxnsYL7spoUQiD_wTpiRI09A97iBGpx24FOMZHKfZfXurShYbW8P_Z9CAMh7zeeGUQ6dieaZVmselYcJq9zcxw0Nvk5tj1c9Axy6NXCrgHU4vt8WRDh1aTRUVXOdfo4ci7BEG5XFmMG27C9i0XXBNDmULNh0DvDsqVT9zMKI1txzF9z8IePl7smiPhf8NceICqzc6F4MMcHArzuk8GjeckWpG8sO0Cxyrc2xAOzg4Rs-7Nu2KkvrbQ9vtmvSlHW4BBHCH6EjjoXdjr1I-TrwkTW3VUF16Hu7Gng0Gi2RzaGnIO9gkY2nOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5xuglHRmGDac9Fd2BoFIVJ6qz2DThDAN7SsZZe4bHFclcv6xFdXlXIQs6SiMxM9QYI6jXQO2Xyb8MGSagCiD0Kf28_H3sSEIoi3KqveSHlMy1JbxgEozUaU3Knhte-ajQGnmgCvs41TwAB2MoeOZ86aavZBpyHSdEuke9Lv171449HWpx6e54nnHcm3Yy67CeaTUQRM7Iqs0j6XzGZQe9kb5ClQbuKaRZ_ipzEUYsQsnXu71gAtqyv5B2RsaY7zbTKhyp0j_PRAlWGp9DWNp19wu29rMZnxY3jDysIOJsTjNST0uPEqYSSCPqna9ViM89HR-0V0MozZX_okdL4VOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=F4OUG3BnkzAxVtGCl8EUU0AT6LlUjkAC1gfDwfU5MuC7EOR84T19CybD6M3o6OugAtnDxdieOv5sqJeC5Tc6gkLvZy2lYjsfiAykEqtj8XUglu594nb7paP9SD6xSN_NOTpS5Uy7Ppdkkm19bicVe5nCgR6CDkcIyCy9E_hXBhC3XLqmaZcMkVYk4VqxHUKjS9CpOg2d9N7Xp-L_TxYMIkgYfyhP5Z-m_RsP_1Y4KZDgpJ9uYeLjvUmbOh8jD2UxODD9-yCmR54vDOXhdbuB-54XpeQ7mv9F71B4Nh0K0Q8LgfmPFbgJdHyM1qp2J32JSdL9sVAia62RMux5Oe8r9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=F4OUG3BnkzAxVtGCl8EUU0AT6LlUjkAC1gfDwfU5MuC7EOR84T19CybD6M3o6OugAtnDxdieOv5sqJeC5Tc6gkLvZy2lYjsfiAykEqtj8XUglu594nb7paP9SD6xSN_NOTpS5Uy7Ppdkkm19bicVe5nCgR6CDkcIyCy9E_hXBhC3XLqmaZcMkVYk4VqxHUKjS9CpOg2d9N7Xp-L_TxYMIkgYfyhP5Z-m_RsP_1Y4KZDgpJ9uYeLjvUmbOh8jD2UxODD9-yCmR54vDOXhdbuB-54XpeQ7mv9F71B4Nh0K0Q8LgfmPFbgJdHyM1qp2J32JSdL9sVAia62RMux5Oe8r9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkbDrQU1hbEru9FGRqgU2BhMhdvJHj3W0DvxnSgXAUHT-BRdxd81bvovWOmpp52LCKoJjbmEP3etfDMI_ZUQyYQSOvXzNPuV-ediHmaVGBni5TH4WaDBzSUF9iWho955P2anI93K4CWPIkkEIQHhEmWNr_DjQGlLyEsxARhDW9nqjLOFPIHuBk6mBKc5ps6_rhZ1n0BxJ2ezjdIive9MKmhNrhtK8PuIlFTmReDmy19e-jm7Z46gyP4arddBharyT017YtJ2jjoiFcXR0ZSO-b3LE-31RQKSps1Xv8t-kHwxMTGT4gjpSnX6b_VsQEEvCXoXLWRi8IxF3Wj6t7Xthw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liAILh9Y2PZyWH68qF8ae4n7GGcbB5-MwuZj3t9a-jrXFp_IRW3_LKvH50nUDSZs7XtQkZ6T1_iylyDmyTn3zn-TUArbOOLoqCiO1ygsdNK8Bjfu7ETli12lGFGxY8SGslOIc0bwsqJ2JKyQop4NYrlMhpDzblEyaVtCxEFZGdeIoh5mig9e4bmqVp7WJHToEIhLjfwevr8_00dNLPL07lwUjQczN0x0QsV0S5c4QW2-Hh_fsLOt5wbiw6gG6gOGcI_HZxKh66kN3BkmkCvpYoAjkdILSeYL77XF4Lu3mMvOsCsBvuLNIOISeJhZNr03XZDCNYpIju8DrzsyqrQZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYDx_rb0EDxwNFRXCk1GOGr1jbAgjGim8smL6aDGHUaUtaPT95q5rwFCDWe85Cxfr-exx9kjHzlOd-NoPJgrf280o0keyBKDRsy_891ksoYAP0GJTZQkinR1DC03ATYM_EO31LCiQqdlW2UMTxmcbhGnnUmGnhljux3Bm4y2cbshYxRUPtPr8hiWtRoYEVj42nHTEgLY9LrIbgDTnMRzbN5q2CcdfmJt4G6ZLIw_CySIPehzFIj_zA3bTTo913fNHFHCoim1KfueyUzZH0kXmCvIhPPWZuvCm_M1MV1iXNm3P_EDHL5oZ3BWsM7bl3AWUXTe5TnZBuOGqJJbc_DPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VscsqPkB-5LcYvRVf2_w3utLp6GLwiPHnUra129nWzW_nIFGBakkD8itykOghGliO2sDTZSgMo_Yd2NQKxAPTmvQFV8A9VB9NvMIf3C6SZAz2IBlZ_benJizdImFshqRDtL2HW6qnhBIJazwiJT_YJYDgJ-x7uGMegTu6uXy--e28LfVqCZ6t-yS25IgIZxAnX8OwKc_NiQKFcMXiWqUAAH_SrAqyLjpkXfmfXWuADKuIzcEOiaSFK4t411usQfEDjkW4TE6_WgfO7GkJE8eHepX9bycAwZ66-0t3sfgXOAIPS_Kj6S9V4XgKpTCuYscnqG5iQjUrX13IZUM3A8ZsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RahOAK9qXkyj3-KRQo5OQ7zM39DDyAXKlCqs07QoE7_1CepQWOcyltN79qLDONiADdw-Vx0aBFm5OsxeUDWT0TTrn70QRzoukUEy9mjff520lkkKYWOmdQj392y_Uq8N7TSjSLoj4oOU50JxseTQOLbBbxN4if8sx6FVoZisDVvRJ5OZAutvQIyeF1iMxUzzwDaHjWDr5kHLzb5BJ52iFKUorzRXCltA0WUZHPpr4m4sNoilDmmU6QmWkhfN78YBNmhCe5cm2oIxGU10lbSpMFZ_c-5rPtjUX8ayUqClmRlzA0jQJmrb2oL4ZVV-5bXdwmQ3vcW5UkjOhGEQRjRgKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KECli47xtO19XOG41sA6LetNnwwrStJUhGYr5eZrhw-Jy_mhsvWl8c2B_OOkPJsoUv8ZJ35dmAFe6-_o9aeHK76xtkFOQ5xBrlVzXckDAURVk4bo_oJF5ebe9g3pUV47gukE7tAmTXjrE33iVbnMT_0B7qq3sd7NshsaKaSSj5QlysqPCTW8FymveDSDV2jR6Zm4HyEqu8rSjGAU8uWDHHhPZ4Z-3vlMcSuUWVrYyf_Re5p_WWGjTb_rQvwIGy4w8fr7FqFtV3iWGSuWec9v4TGgq09H0Xk-Bad3GLs0SEWqW30ieZzJgeuz8WtMtMkwZ8yVvRGgp7SSSBKwJYN_lwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KECli47xtO19XOG41sA6LetNnwwrStJUhGYr5eZrhw-Jy_mhsvWl8c2B_OOkPJsoUv8ZJ35dmAFe6-_o9aeHK76xtkFOQ5xBrlVzXckDAURVk4bo_oJF5ebe9g3pUV47gukE7tAmTXjrE33iVbnMT_0B7qq3sd7NshsaKaSSj5QlysqPCTW8FymveDSDV2jR6Zm4HyEqu8rSjGAU8uWDHHhPZ4Z-3vlMcSuUWVrYyf_Re5p_WWGjTb_rQvwIGy4w8fr7FqFtV3iWGSuWec9v4TGgq09H0Xk-Bad3GLs0SEWqW30ieZzJgeuz8WtMtMkwZ8yVvRGgp7SSSBKwJYN_lwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeJnCggPlyYK8oeRprcAMhJPA6B6yX6VvLujnrWy4swOHFQ8F_N3mIwWlneypvK34b8pXaIhj0QwYgj17rgrzSuGvz1ul8SjyNAJjkOe8MdbAP77zGAO94y7eyit5bg7ANW5rAxveHWn6YNVI2HJOn9zuODfrWupIMXkSdblWVREX6LLwolww3foCYmy6TRqaD2ZhXD6Va_KJBLLuKCNTyGuRbiYPSBM_Hb0d77LesYTCXGnxkxr4B6lSEw045HiM73tDF4ZasDJEP95ViG_GQxetgNJBAcv3f5XyQY_YcSbCUobesCLNrPrsBKdh2AROvmBUicN9nit5xSmoO1Q5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOxSGnHLAGwagAW2eAmwu1RvBg5D5WFGPlezvNe2h1MX83nTmrMkl7F_cGe8xvIGfyrU2ieSX-kwa3zyhIW0TOAs25vURRYfS9nJwpONR8Qd_a7vgAZGiGUr2jRh6ALnQBbCUY5z5hLeEWe-MjkclGgknJg2CJQk3driXbRvJ1_FsBcGC-e5SSnbu3q8J9JxXO5o7N1UzeiLtr2Ypg1yzl6OWak3ptZbE3nbh51ZOVezH2i523YnjlNijpfw4WSIw0AWERwuVXVopWkmJ6AjWJ4sJ7miSUO4uvfvATFWlRXYVo5d7yeFLuYSeruYrrlDcbMZQbzeBM4b8DTgrXgg_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHbzYVX0uYCEfykVdyRKjApZ_86ESLXyMmFSdY5hje2XEo70AGJYDMofz3IF13UL2a1vnFliOiHO0QUqXOTH7uQdwsFkQxXUbs1aSgCZHG9ne6w6RvxgKtfT5vHp3OxUjtHHGVUnu9Hzn_8syqQVy82geUyrBUTQ1JcH6HmhhH3qrSYD2NXg8eSQFxl2P_t79eqWGnKtiK5pGlBj2IWechI1AMcT-egZ3J2F8U44wpPOY59FZFoFX4vLBjVPJ1fmlSkt5iFQdO3l6heLDJGbSoAMiUwLsMN0a1QEAz0LmGTDvSrzz8zUepTDXwqYJYgmvE6-J3HhHrc6Tf79xpAPkTvvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHbzYVX0uYCEfykVdyRKjApZ_86ESLXyMmFSdY5hje2XEo70AGJYDMofz3IF13UL2a1vnFliOiHO0QUqXOTH7uQdwsFkQxXUbs1aSgCZHG9ne6w6RvxgKtfT5vHp3OxUjtHHGVUnu9Hzn_8syqQVy82geUyrBUTQ1JcH6HmhhH3qrSYD2NXg8eSQFxl2P_t79eqWGnKtiK5pGlBj2IWechI1AMcT-egZ3J2F8U44wpPOY59FZFoFX4vLBjVPJ1fmlSkt5iFQdO3l6heLDJGbSoAMiUwLsMN0a1QEAz0LmGTDvSrzz8zUepTDXwqYJYgmvE6-J3HhHrc6Tf79xpAPkTvvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJ3_EqWzzG1qVlC6a8tDNOLndKAajX9W2rlXlRy_Im-v6U3SWxcbChpD8kzgUKHa6lqH_Nza6g2l-TQlb6ZUSJg265sTrKEoLAceC4EhhEncFyShgA5Ggww312lJJY5XSOQBcd5vZ-AlpbLbDknF9PZxFSeiExDGvcjTQaN0oRLgwT70fcDzwtcqypJD7Nto9h3sPVomWTHHlh6Pgv5isBg1lfDGfLICKma1O1eeImrDxKigTPxRIJgCvv0Zmw66zPm_8lakKXW4EgKwBbi65PEZojFhVrVP24FG93DqdyTKIT2FYAl35HSU05vvj_byD7XbfszRTX3OBih6LdMX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1YFiFSzalImMRFmovdaHI1kMNYPIirdei2uXOtR_CSgodtaAo5YUrX67GyBogUzLperfeH0NaKBdlppavQ-4BhxbWe83-6Wx3gTqYno-Tlu2t05sMzSu6UaBAYoQaPSIY2icphvNpSoe6lZ77fk7zz7k-YwUDWVAlKE-1_UrewXuP4RwvMIuBfROYaibTDzNC7curHVkhsqyPK6RnUAYpaJ_H33fgUvrmEFJGqowiY1Jjh7gq7VCHTOigJCODia1EGzmXeafSMq3cbcP03nVZw1ZcTjLpm99IvXnxM79Y1-9NjztLv4c7rJlQUUZ3tr8M30x_EfnenRuB5Zz6Qwwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYDGqTZ_bY0kRnz1KP1K_nzjbosIJRb5-ufFv5PsO7NIYuSkVB98ZsGvv56qGeRKhUO2MVfBTQueTyEqcH3j4iEi1e24TxNQ32HWT6ArEiJxmk18RRSzPyHDlb2DmblYKvXYvt1sHBk0SkeFn7hDF2p95hrcaQq3YtNi9Qs4cbib-iVRR6A0lsVLuvfn9bGijBqkzPTzxlD8DuNvogD1QiGpN__csIKlW1tsQyQJgj6rHVgyATN4GuUuYg31_Ls-Z3BNV9OB_axF1y_WAFsgeZLzozF-FwghOHUfk13ZkdKdfGbUqeGgFBq2FC4iFE0eUJSDR8CoSHDNwqxj0tJAAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=uciHOdRSXSfAaYqx2zwVbLAo0o2O_PoIUWD5V0MBDZH2Fcl5D1I8AeCvJQuSZfX6fzqqB9Ku-usYNUC2jjO0K-IP49vIL2IaFQrFuaIdGksdtBcGnEgMfwA5S0Sp-50DxInrGHiOQY8NuO4EKKR-dkNSHMQJ2qlnCwYkGfQDY4wCLaJJyipLewEyrqCrSzbXnjpme2yQyS9uBb_FhulN7kcLyn8KLOafLX0plV5DGWplslpBNQYl2NuX_mmHNoAsuOrCY3U5-ONKDCspIJiRkZ6Idqk9lzVk-D2XhEKKjdIBCNuPCJMpKQ5ADnov8sRwSxIy_Gv1Kv5-rnnK3EWlJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=uciHOdRSXSfAaYqx2zwVbLAo0o2O_PoIUWD5V0MBDZH2Fcl5D1I8AeCvJQuSZfX6fzqqB9Ku-usYNUC2jjO0K-IP49vIL2IaFQrFuaIdGksdtBcGnEgMfwA5S0Sp-50DxInrGHiOQY8NuO4EKKR-dkNSHMQJ2qlnCwYkGfQDY4wCLaJJyipLewEyrqCrSzbXnjpme2yQyS9uBb_FhulN7kcLyn8KLOafLX0plV5DGWplslpBNQYl2NuX_mmHNoAsuOrCY3U5-ONKDCspIJiRkZ6Idqk9lzVk-D2XhEKKjdIBCNuPCJMpKQ5ADnov8sRwSxIy_Gv1Kv5-rnnK3EWlJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=V1Ke3C6NghSeiy_sPfmJ3wbOmvV14q_Lc7T-LCFfgj1SKKIW80eEGoxoDy5WuT8U_RCFu4bmjLEXp_3VBR4FufoGAlpsJB0diagE-wqncgOyzYLJ-nfb8XH7MUwnYW0vFfIKXQ7GgFLxlzgxoAdWk1fCtzVXf-it4-j6q3MvWoxXVI0EQ279OZNuumomobcJBF0viQjH4_RbkUaathovrwzQHprcIpn0nnq0dBFuCdI2VW5vG0kfXQbwzBFyQyU1VN-tjC6zvTYfhntylgMyWh8j7sDY-eSDtE5yeU1Oy5Z_fBdIu0RkaygHZo4Gaa0ooEJTDDVmVGyXBAguNe7Kc1SzMfmVewj51DIHafT8BELf1aWHYqJWaUIW29ZCOobACuXNRRFiH1WykSeCMt78cqTawIw7oPIkhR3Ps8pxD3RgBpX9u2M9_vJZECTejSOJsRa3v_TqRbYjb2DdRKYonxGCk89Yz8dL2t1neI9aGyeSPCPH4iGB94MJeYaI8_4wB1drHBzgarIdLoHmsV2OqN_gRKru6WKVxNtlwV2vLZHXFoJF3BeH5d_6JmDBSIVgAUxM0Hsai5qPFmsQyuzxTW8dAUcLe15rSQpucgyr3eZ1zL3kZMasN-wDBXNxpIxUApeO6lzj7-GNhaknHXHLuPXgAroY5Tehj3NCAEMRJ8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=V1Ke3C6NghSeiy_sPfmJ3wbOmvV14q_Lc7T-LCFfgj1SKKIW80eEGoxoDy5WuT8U_RCFu4bmjLEXp_3VBR4FufoGAlpsJB0diagE-wqncgOyzYLJ-nfb8XH7MUwnYW0vFfIKXQ7GgFLxlzgxoAdWk1fCtzVXf-it4-j6q3MvWoxXVI0EQ279OZNuumomobcJBF0viQjH4_RbkUaathovrwzQHprcIpn0nnq0dBFuCdI2VW5vG0kfXQbwzBFyQyU1VN-tjC6zvTYfhntylgMyWh8j7sDY-eSDtE5yeU1Oy5Z_fBdIu0RkaygHZo4Gaa0ooEJTDDVmVGyXBAguNe7Kc1SzMfmVewj51DIHafT8BELf1aWHYqJWaUIW29ZCOobACuXNRRFiH1WykSeCMt78cqTawIw7oPIkhR3Ps8pxD3RgBpX9u2M9_vJZECTejSOJsRa3v_TqRbYjb2DdRKYonxGCk89Yz8dL2t1neI9aGyeSPCPH4iGB94MJeYaI8_4wB1drHBzgarIdLoHmsV2OqN_gRKru6WKVxNtlwV2vLZHXFoJF3BeH5d_6JmDBSIVgAUxM0Hsai5qPFmsQyuzxTW8dAUcLe15rSQpucgyr3eZ1zL3kZMasN-wDBXNxpIxUApeO6lzj7-GNhaknHXHLuPXgAroY5Tehj3NCAEMRJ8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGBe-dx_wnw_-mdodbYY8b7obQRZcksyMYXo7QvdkUBhLWJr20HmuQBKgq0vLxOxa3Q93EO0yM2TMgg5B224GyILje2RYtT6H_azf1uq9ZugJ8PVysimmdVDSqM6XjkD0xvLnnMjNbw6dqR9qYAnOOTBAOGz_0ON9luXOaTKrHBQG3mS875mAduakDMErNL9Twe-SZtVgB1DQhsh-OcrOLM9EnaosBZPwDnztlWtJbEqX1m7VoQUwg1qDNAC6TmPMMFS3KYyh0jJSk-SatY-Lw1jZfZfzkdzx5bhdLj3DLK5GPwXaUnsNcknJrUgYkdJu-Oeb5JEZWYFilQpA3snhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mydp8VOA7-y3Iu0_f8vgzXJ6V_WDzJ8NuT9znaCJ12TlENyDgTiZCABXi8kp3rmTMlIL3q47xloaXMXRragzs9Lzy4Oz1X5SHKyHIbZ3PNWIEmrdWPzKXjXUcvbr1v_2LkyPEyJVIo2wbZfuLjAlun7aN7ksYZLopH3AlwMCBIcJ8vpJk2_mQ-9tU1hLUFjea1BYCpfg21k8ajFEWoXbJwSpV6Px-sW1qDduqG7r4ayOjnTPn7U_EWBrIFrMGtX7yHg-7_3l7XlG0mRdLsn4oNnPSCxjgW5XiDg5aRofh73wIgVHekbC2RnrKSYO5o-jibV32vZTsC-Xaw-M0hA1SkS0D2xbIJ51EeuMHDXfmc-bGq8RIwy1UMm_SXaz2MXS_oe1CWObPiyu4-zBmc5Zr2g6VZVoVfYszcqTD8Tj5T1Z9aH2WCJpAnB_BSTxzi1Y7dnYS_YBS2_6LsrgMUGrR3BjD-zhrToIhYmLfms_N0X9VZ9B4vffXObqpATHsH5RnxjZJZWjGJMv2X2XpVV8REaOXUshXrOoX8Ul8dOyj6KRSdQYOBNqcij6bcbrrqEUWF6SYrE9PtL8aGFJ2GDEyN5nqL8_0mmQghMSelqpevI10kfkK-dWJSyzt_OldoxepQk3-QLSWo805MkLWcrMf-qymtLlqISdTxx1y3x4fR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mydp8VOA7-y3Iu0_f8vgzXJ6V_WDzJ8NuT9znaCJ12TlENyDgTiZCABXi8kp3rmTMlIL3q47xloaXMXRragzs9Lzy4Oz1X5SHKyHIbZ3PNWIEmrdWPzKXjXUcvbr1v_2LkyPEyJVIo2wbZfuLjAlun7aN7ksYZLopH3AlwMCBIcJ8vpJk2_mQ-9tU1hLUFjea1BYCpfg21k8ajFEWoXbJwSpV6Px-sW1qDduqG7r4ayOjnTPn7U_EWBrIFrMGtX7yHg-7_3l7XlG0mRdLsn4oNnPSCxjgW5XiDg5aRofh73wIgVHekbC2RnrKSYO5o-jibV32vZTsC-Xaw-M0hA1SkS0D2xbIJ51EeuMHDXfmc-bGq8RIwy1UMm_SXaz2MXS_oe1CWObPiyu4-zBmc5Zr2g6VZVoVfYszcqTD8Tj5T1Z9aH2WCJpAnB_BSTxzi1Y7dnYS_YBS2_6LsrgMUGrR3BjD-zhrToIhYmLfms_N0X9VZ9B4vffXObqpATHsH5RnxjZJZWjGJMv2X2XpVV8REaOXUshXrOoX8Ul8dOyj6KRSdQYOBNqcij6bcbrrqEUWF6SYrE9PtL8aGFJ2GDEyN5nqL8_0mmQghMSelqpevI10kfkK-dWJSyzt_OldoxepQk3-QLSWo805MkLWcrMf-qymtLlqISdTxx1y3x4fR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJDSPVqY4OXeKKSHey6kqjzEWJiD9XZbPJBS03e7q3JxwUe6tkjAWOwYl7EH31O_XN2FXiS8QUlr91ADYVY__MTwKcr-N7RTnKze8EUL7xv0mXJnY4v0Jst2TiYxKASWErc-9pIripzh_RmKbRfVJqCJbVVz7JIDJSNGHuT1Uyjj_UmboIFG9n7C8n4irKLxa3EcdVpIN7cIeFntnupdffn1XMg7dPuuvfYNV309p9-fJETZUPSP5JRX6DEswUpeb4jYxmd6qhSeCyVrg-d2TMx-T7_zrMV68RkpaiIEAY0v-4xJovKHGjQFKZpMSBb3cPogG5nla1CKjL10xu6nXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNf-204xOJLwqV42_8wTC8-fWzubf04HRWEcKTlzQaJHJHhe3BrMncZsS1v-EiJOoMxeV_pbEhxHCHhuMALk_c0cU65RAqft9fxFDuNdkC6w02rQ5yE69r0tHp1pBRjAi_YswH5q4jeaWHOpIgdO2iadF2THiBaQhGAMMspD3mvjDko5W22gQ_axAL2jUwp-XFmvyi6qdhTwZJhTyXwWn0mT0pfELuAxqSuI9qwkdSNkpFvZGdHeTHt5N3gjZjCvNpTdEKl5AKt8UNsBeEq5H-emwENosHNQ1X3d8Erjyj52q8ASd-0ppwhXiyRjJdGImRdXldZg0v0D_vTvAJfiDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtPDjbQZDyRfNKPnEZA9Uhxvs656bvts5zempsGrRr1im-t0clxH38rSVpAsENQ-MYz9SAvCQcCyPWQ76Oc_LNPEDlq_grVVlOzdK5-aOjqyOnniBYCDCGaRtf8QmQ2yhR1frNb4plQ8T-4C-I6CyHbcXVaPbOBbhPIq-3_Wk2sE5gOc1kPtfeqIO163T60FVVToHYgosc8AeDzQ4ayfiEhE5QEj3qwvEMyXFi5-PbT1Yd9UcP7pGxnoB707qG_xjXv0XUt2sQWXKRgayAihM0S8KT1jSy9zjDTIWd0IMXplPqesoTt3H9EFKU6BbgoAASnUSjdsRDvoGAMhwhuB6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=Cnx6H6u4KSYs41AZ5XYNPpQcWFtSuS3jA7OMCCGeNSZkD_SZTOdxA4VLgYIYTS8tpxq5n7qxp2wYRqxH-SaxZbGQCS0bNaf5mDMFPfRq4IFBKMhMt8iSZY8miJ34aNVV8jbm34zINak6xLow_gdQBty4CyCKUnVXY0lLO4J8a12mju82V4Uvk5nGYCWylU7_SU0ywhCOHJ07EgjK6wFc_8T07qK7KKYQfmGyYrEty0V7hAsu_SK3rZaTF4bPBh8iKiNkcDTy3sP8NcY0KDsL1RLtEpVnKUTNCIwjgwK6ry9UABRpwcblVkzEwNholl4WqebAay0h4S5oVSU81a_hVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=Cnx6H6u4KSYs41AZ5XYNPpQcWFtSuS3jA7OMCCGeNSZkD_SZTOdxA4VLgYIYTS8tpxq5n7qxp2wYRqxH-SaxZbGQCS0bNaf5mDMFPfRq4IFBKMhMt8iSZY8miJ34aNVV8jbm34zINak6xLow_gdQBty4CyCKUnVXY0lLO4J8a12mju82V4Uvk5nGYCWylU7_SU0ywhCOHJ07EgjK6wFc_8T07qK7KKYQfmGyYrEty0V7hAsu_SK3rZaTF4bPBh8iKiNkcDTy3sP8NcY0KDsL1RLtEpVnKUTNCIwjgwK6ry9UABRpwcblVkzEwNholl4WqebAay0h4S5oVSU81a_hVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_aVWbJJ7thLErV0pYWqb3EamDPBTzHICbiJEMix7Li9H4c4GmAyR5qeGJxVdrcC-mlvuFgtbLQ2cwGAglX1JjwTEqqpA8tMg9_cE7o69Y4gSNLVYdlok3C2D94b6EdYuKWwB9VGc1lwqx76kQdJvmPtWX6bcnRwKY9YjjZ9xuLvz008Yx38AIQY9NLerAUTDXWpwDy25ONMgaIAY9diwUs2zZN3KA539MjC-9EntAHR0NA6pFaYhQpmm4gUzjRma7OhRObdDmYQxHx2QzejQ-U08EnAu-k5hegaNKm2mhx6ib9IZYkSC7cC97DOi1f_aUEm00b4Dj_1oWp9O5Vv8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBzI_wGKoXj-PHs6St13PEyTX3OW210JHGeLkHD4eBweKEPT6a0xEf3L7Pshkz5dX_KH2tmaGgKrB3w8Nu8igc8FcStM5WY4gVLtULfijUH00exzy_NfAaWcHwgkkIGgN10JvnPEOlNGy5_seIPsdcVSClygKZalwI0i0D9G6tj5jkVpjsu31ih3bRsOPsrNqbnew-2PRQZb8LWJte0wbvHmcj3X4hYSu9tDKCzIQRTk2XrJ-tq-CF84gO9pZeKZJkJ62MNqI94Iy7yN5nU4JWuSWRkGzDoAnAw-JrVnOLP98C2GwwhLOprj6GnwIPa3F9NvSJKApmXzxQiyP7AjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abbii1nIqUSz7imUJb78pVMKMhRKU80qVONmk8834Oj6ZqaiVDwZyMhidr99Ueri3fwK-nYCkd-WaGZEt6RZhYlfTpmk9wmZ4KKZcLOdq6WI1WQX8a_kC7hlrLlfkV02LLfsqQFqTqHw5ZvMqo3IKdvIWoI77PQK0pNmxF2f4kwtAwTabX_M-tV77vYJRCOBO6B3-w2xGJoU0aWYliXNU9pJHiYB3TCaE3p4m0qGFKXua2UEb2W1JI2at4XzUrJuoDzBqPClztxDxIYCLYR2ONgwOELyDqxcMf27GI15Xt4VRjJ6rn9sAONxo97r0wfvOr1r5z5imfYzAfNvINnxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=NrSal1JNmz31DzS33dafGr6QZE3wkwwfGGlm2HZtKwS5AMEYTF-NeqMU3pTnYV4_jJTGVu4iKFUThBmgtQk2WJszckhUKpp-Cnarpy98gEAXodpnMeFfEyqE3r-AqgtKd_f72GhvfGWAjOzyKkO7poClHVwbVjjuqFzvYk2osLrLHGvMQSwSfl_ztF-31UYv54UuxUeC0T4kgA8-L441sPm-lNXe8t4kO1JXjyL9KAxH_2t8ovgnv3V_HQfkyYcCwNrWOxjahPgQ8cyToNzKUDuv_ACa3oi36EDRGHGWZqMyogGJWJBNwdfgQ24xcNYvPuQ65HOxX2e_BI1VtvetXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=NrSal1JNmz31DzS33dafGr6QZE3wkwwfGGlm2HZtKwS5AMEYTF-NeqMU3pTnYV4_jJTGVu4iKFUThBmgtQk2WJszckhUKpp-Cnarpy98gEAXodpnMeFfEyqE3r-AqgtKd_f72GhvfGWAjOzyKkO7poClHVwbVjjuqFzvYk2osLrLHGvMQSwSfl_ztF-31UYv54UuxUeC0T4kgA8-L441sPm-lNXe8t4kO1JXjyL9KAxH_2t8ovgnv3V_HQfkyYcCwNrWOxjahPgQ8cyToNzKUDuv_ACa3oi36EDRGHGWZqMyogGJWJBNwdfgQ24xcNYvPuQ65HOxX2e_BI1VtvetXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=kWtOm1zOLYLJUsXd2vCfZw3N7zlcqor-Ha_XVFXeufh_SWGGrBPzVipUQ5KfZ2JifnhrhjWvb1ngG_1lVne92UBRIJJiyKXLsIRfU-nR1a5p4zJ4a1HO-jgY8PYMOjJJh7Ujs27qJ2QVp6Cv5woiolZRkuxy9ZMVlTLci8hMpKvcdPu79C7Fl7KR8AEDbW85aBZ_DZPDniA3eBJTwDWhIR-QZZLQAGqtzWs36ckWb1HlzGdFz-pnNZ0oNQodJjTp_lrxBA83shFluBeqadzEaz7bq-tIu_hSKmtCEIdTRrtrbo5LJ-6NicncPAhdh1BS7PgSeROCzT8RnNnrWweaCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=kWtOm1zOLYLJUsXd2vCfZw3N7zlcqor-Ha_XVFXeufh_SWGGrBPzVipUQ5KfZ2JifnhrhjWvb1ngG_1lVne92UBRIJJiyKXLsIRfU-nR1a5p4zJ4a1HO-jgY8PYMOjJJh7Ujs27qJ2QVp6Cv5woiolZRkuxy9ZMVlTLci8hMpKvcdPu79C7Fl7KR8AEDbW85aBZ_DZPDniA3eBJTwDWhIR-QZZLQAGqtzWs36ckWb1HlzGdFz-pnNZ0oNQodJjTp_lrxBA83shFluBeqadzEaz7bq-tIu_hSKmtCEIdTRrtrbo5LJ-6NicncPAhdh1BS7PgSeROCzT8RnNnrWweaCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=BQd9h1woFc-baBgNQZh2g5cCazClsoQ9b8vPdv0BJWWtwLInxS3pYexoRns3mmTOl2xJh04JUTh96WYBUy1cxL2ZSkvk7Lmwu6rHJRt6G2oHXIjkPvsUqzEfu0tBdcTzzAxAATrLExHpsa_cmSzKQzPBuBydj4NrsxnqC9E76t4DEU9S8-9YrA9ppnM8F7JTqmbE7p9WlJ_6jA4PgLSAfRxGCpIBUAt9-tu1JOvvVlbKg73WGvTmv8vS6VshK0pp7dsSUeQ6YRrqgWefyAF9tjQlhiu5AZMYY4VJux5DjdAwVFYDeNa5LynXiY_EKqKh4FvB0MmasOIHZMoDEYvNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=BQd9h1woFc-baBgNQZh2g5cCazClsoQ9b8vPdv0BJWWtwLInxS3pYexoRns3mmTOl2xJh04JUTh96WYBUy1cxL2ZSkvk7Lmwu6rHJRt6G2oHXIjkPvsUqzEfu0tBdcTzzAxAATrLExHpsa_cmSzKQzPBuBydj4NrsxnqC9E76t4DEU9S8-9YrA9ppnM8F7JTqmbE7p9WlJ_6jA4PgLSAfRxGCpIBUAt9-tu1JOvvVlbKg73WGvTmv8vS6VshK0pp7dsSUeQ6YRrqgWefyAF9tjQlhiu5AZMYY4VJux5DjdAwVFYDeNa5LynXiY_EKqKh4FvB0MmasOIHZMoDEYvNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTCUP4VhNjpztEoEiMdA4m9HApMiqiuRQWL-f8cKwoZmrrHCBjzsw3Ao7JXEaSneQmbVFV8OD7uqKnv4jSz-chCG_cymcrNJEOy_K7baMmwXEW6CgwY0PDYUjZeKlR6RNWckQlGs7gN0YptxJGruRenDXja-EBTiKhIB-SBiku0uhoGE6sWIpcTdxIJ-xVVqGikdg0AUPVB2HKXgf4HAWcOWelOcRHfnmgOGxjVwI2fB4SzzGemx8gsBZI2AUGWuoW20j7hZ03nqmvho8hh7OTmPeBuPTNwq33y5W5QAFo-lDaLzj8X7nA3pS2R8l3tekMhnVtMnadM_HDZHBkq3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنانی که با همسر یا پارتنر هم‌تیمی‌هاشون وارد رابطه شدن:
🇦🇷
مائورو ایکاردی و همسر مکسی لوپز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری و دوست‌دختر وین بریج
🇩🇪
مسوت اوزیل و دوست‌دختر کریستیان لِل
😀
تیبو کورتوا و دوست‌دختر کوین دی‌بروینه
👀
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=Ql7unZ-qmvF-2wis4AX0FWL1ArjttPYJWRPUAjkkc0h9vBndxv2dRy_hnhxzU1rTDZujMBkRpJhL5faObot2QGIrY8ahbYn5GxDmO4y6hJU_SGmqsPgtrOeYsQlV3S8V6rKLgAw6u4TlpcWtAG7_HP7cOfTQt5RFYSSVOByHqBAPvEN64svk-OdQ7VP4P-mB8r_vYAqLA-MUWm-d5A0XOAMCUMSIdHeATV6xnCfOZPpqmhp1EWtklZU7NOPbSINhrjote4K7m8mOuqtnwN4zKJgqyDTuGwQz0vfHcM9NifoONeY6eXOxXeYA8OYXxrVuWal_DlF6N7TXfyEjnNgPsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=Ql7unZ-qmvF-2wis4AX0FWL1ArjttPYJWRPUAjkkc0h9vBndxv2dRy_hnhxzU1rTDZujMBkRpJhL5faObot2QGIrY8ahbYn5GxDmO4y6hJU_SGmqsPgtrOeYsQlV3S8V6rKLgAw6u4TlpcWtAG7_HP7cOfTQt5RFYSSVOByHqBAPvEN64svk-OdQ7VP4P-mB8r_vYAqLA-MUWm-d5A0XOAMCUMSIdHeATV6xnCfOZPpqmhp1EWtklZU7NOPbSINhrjote4K7m8mOuqtnwN4zKJgqyDTuGwQz0vfHcM9NifoONeY6eXOxXeYA8OYXxrVuWal_DlF6N7TXfyEjnNgPsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
