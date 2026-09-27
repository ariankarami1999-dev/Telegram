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
<img src="https://cdn5.telesco.pe/file/OwJvX0qkJAvfvhOpb0ew87cBa_4SpIi7yaCzriPcO5SkFfk6SZHC35N-sDdMzOSL9jHRlUpDmNcOuzRJqR1OlkfwJAOLP1MWuHnZ4MFXaefMMtkaZb7DacrdIXWEwbRUIXc9QJjiMCD7_GKHl3UHpf9gaXK7HNGdgn3t2zbg9UNxghPAP7exxPKrSjhPdwuqcpavWtY5Ga5_5TmqLVnnIbKaN3GjGXc1SccYV_bHQcWg8uz0xVXNBr-HeIXy2-n2-yQ44KOkf5q6GBwEszimiuBWA7wK-C0qY6xR-JppcjzByVN1DQ9ZgQFeXWuvJ50A-WofYWdSUSmgk0xT6nfOdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 398K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 00:08:05</div>
<hr>

<div class="tg-post" id="msg-107394">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQFGuzUwcGPrhIgQ-EOUM4E5m6ONoVtAd0O568mdXfe2h_O0jn7psxI32xqsVWHbhZiLQMv2wjEQh1xs5HSUHbTf5Qr9cbO_T0WBqaw4V6iFmZGWUJQsSrdNdLf0HkZoixSFzU6dzseTOXtBU-hmeoYYrHcb7P5rOAa7H57oU_JC03MTAOcSPwhLZXIvYPtSyRprUJZB8AiivelgpHcSnpSla-lFpNJQ667JaowUnrPOxQecNQ2iiLQYCGgTGsFZ5gYgEeFT1H8NqVA9_vIWU9yk6nBKCgrakH9Sdnq_wKGgLjbkZfmYdmbmwjuRsfgYPmTu2Dbuk09s7mgBjk3s5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/107394" target="_blank">📅 23:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107393">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt_VBf1TCj_PljqQTOBgs9KOQ6-SvePMAwVe5f277wAYoU3CFJGmSBk3CbEeYOvEgIjImaSBCqHXcvABJCHLy81OElp3Z7vXkoexZ8jJ959AZ5y7_OY-YVWLr_zlJqzfFV9dQsxt8WzcUwzW-FztlObigKZIBtt1Kfg4BBCBgBw2afrJgwejtMZlTBuGled9B8h2KwS9_aZNghOx_KR5BWi2PKORE7dyTCMa-uOH6mc2AR_8ysYuP-o3tH_U_HvUW5w6HIlg3eYdcOyiYpQsOAJQDGIhDM7pv83TLlOZwslIVZX02ZQQMqdz5IgaJTYi6XP-xDz-mLbFXY0B5dsThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه…</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/Futball180TV/107393" target="_blank">📅 22:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107392">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arug7IbFiFOiMSxgk2Yea6QWVKTpfOg80q-QKA52aQdZ-a26OgSZ2yiFQ2suBedKAYJiH96W6NyLzpAuq5CRUjlNk7J7pFdyjy8chMh6mTQFgiZoumZsyU6SyjGjXrbox15thPXDwekr9lRtiBzdKSlClVMXArM_svPREBozeljY4JvXZdLqy-mZ-duKfaHnKAXzl6odyts2PHEWY7rXSXoh6i3hPwELYtE4LU9IGDQfqxhSaVIsnluCYasYYPPDV8AvbJpCe--5nHGGlhlN5n1MuVGZjJGe94NtJwxr8Q2ROwVUa4RhuT2ldCN8FE1jWH_VigoxYbLj1M2edE8b4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
امیرمهدی علوی سخنگوی فدراسیون فوتبال: من نمی‌دانم چه کسی به علی‌تاجرنیا گفته که جام قهرمانی را به استقلال می‌دهیم. هیچ‌ بحثی در این زمینه شکل نگرفته و صحبت‌های مدیر استقلال برای نمایش است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/107392" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107391">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8aLanV-w6ordvVmL2dKOLbRikHbs6KJlsxNGnPq7Nd28eIXFFXM9ZQ6aCjbqFLC43yGrwhUNta33HJ2OqVU8_I-fuho9wIqsXQKKLZK7DxMJ8icVVBCl-BiosW1QGiilwCZUVY7PYOCF3mqqftY8yD3pw2eZ80FzFzG7ZJHJfaboRZYZXqrmql9B3Fz8hAyy65baxKle1jZLohct_cP9Uy-_G26T9TTzzrREKmVx8AoN7fS31J9p9cVXHc8Vv7Q4V6_n0rRHXF4FYWibZjh9BtH3zzG40XC1OgM00S6UUcRLU2sjF8ab10doJOxoL7DeInK_pHX2avQDxrdGVW4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107391" target="_blank">📅 21:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107390">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImDK21RBbe_wCAoF_WntuLLCvYsDWCnvW1uV6s-BsA1hy3vtq9sWa3eRdZIX2nQfG3NQ9TKvn-9a7t97cwSlaW27bFii2VeaKsU4w29UNfDUxOTAnNfJ1omSrMVdqXiqRVFOr0yxf7c-uFfVc8C-eJc0WGbspgiD846JX3uHErONjqsxaItXh1sUy6x7kSojUullL1Qba996ftpcE3Ds2w7B28EMi06I7mirU9aocR7DAiPLP4n4xeceBkB85kSsm6Wc4QjZOFmaTR-WR38zZsqdi6srTIClS_0r0lCVD5_7g60PWrMatwZ2uNC7ROw0rbMTcUJJ139MU8sTFPhGog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
رونالدو روی نیمکت پرتغال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107390" target="_blank">📅 21:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107389">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=qFsTgEBh6LHN0GoQFc8BK18_fwBVSSDghE_qDCg74NKOkfcn5TAoeRKHgk--6kcZPOrX2gDnNfRxqt0DptI4_nag_kmPZiDj9JAYuTnR3dUtWOIjEduMs1Bl1U7torv8YZKp49PXNqL1Lbon7wp8djo0HtQlIq7-jjVU4CA4OjgNKpNsQpShwEUYVwO8eCZFIj88rxDuc80tDrD6bjZJi9kTRV3ohGd22H7BqoxrhF5M-mwB4Z31OqczQHK2cHGFdupAULwhh267LMlUpgff8hFCRGebnwQewOj1CdRKl7xGY01OC7rw7nnFJ_3bsJDciW7zx3HkTFC268koURnrmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=qFsTgEBh6LHN0GoQFc8BK18_fwBVSSDghE_qDCg74NKOkfcn5TAoeRKHgk--6kcZPOrX2gDnNfRxqt0DptI4_nag_kmPZiDj9JAYuTnR3dUtWOIjEduMs1Bl1U7torv8YZKp49PXNqL1Lbon7wp8djo0HtQlIq7-jjVU4CA4OjgNKpNsQpShwEUYVwO8eCZFIj88rxDuc80tDrD6bjZJi9kTRV3ohGd22H7BqoxrhF5M-mwB4Z31OqczQHK2cHGFdupAULwhh267LMlUpgff8hFCRGebnwQewOj1CdRKl7xGY01OC7rw7nnFJ_3bsJDciW7zx3HkTFC268koURnrmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقاد شدید مجتبی جباری از داریوش شجاعیان!
مجتبی جباری، سرمربی جزیره قشم، بعد از تساوی برابر فرد البرز، به انتقاد از رفتار داریوش شجاعیان که در دقایق پایانی بازی در نقش یک مربی به جباری مشاوره می داد، پرداخت و مدعی شد هیچ بازیکنی حق ندارد در کار فنی دخالت کند. جباری همچنین خاطرنشان کرد حتما با شجاعیان برخورد می کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107389" target="_blank">📅 21:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107388">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dki54LLhNgsGEBkfbczU6qqE3X_aY-GeuEkelfErAVrz8q1CIZl55Q3815n27mCN-9L4aLdl5DKIKxt-fEw0h6wV0wytKSnXxeYQiFkxcHC2PZy-3Fdinu1rmJo4rIgUVItr75hp911HzQJzBDP1h4CXrAZgLVa9PlFaRQT9KoBF8BMs17D2MycRliTzZ_u2rLZfuccGcoAWY_RgcnhK8UI9qfcCtbAEUfjhP8IdWCh2uKz-3a0DCDK1w1OUcnRtmUjgZMNR7misP233b5xtBpBsKFlrGPlLeK9xkl4_5cnhSsud6Dt6gYri_9m63RUu-x0b098WkpSnGPbgB3FFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
استوری تتلو گونه‌ای رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107388" target="_blank">📅 21:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107387">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaCZ7ChLAo0GJuJ4luyxCQNJrIq5CvMY39svKDyCWBZY8STwyys9xDtSHSV29TZkEqkT4QcvsgyIKu-s5tSNOi1owqQrLBSyoCbQOGKOcMRMRbct5FukvyzpEu70ncER3k6eExiXAdPbSMSrwFW-NYk_bllnrqQcF2nTmzLf91AurmITDHqCFq8SBvb3ZtCvUmyAERq5wkejZPuovzDMfTtARfJ5-zvpbk2iVq0n3XTtwkyjDBaksnFDeHTBFN6tjSHBrubqFk559HZXBuiWkIS-1qiIpOfbAN2WquUJA6UIEGNb8FFK8tDe-fOhTd_HLYx-yyth6KS5lSJmAk0ugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه چند سالیه رویه جدیدی در فوتبال حاکم شده و بعضی تیما دوست دارن بدون مسابقه جام ببرن و حتی فاتح مهم‌ترین عنوان ورزشی در طول یک سال بشن. جالب اینکه درباره عدالت هم صحبت می‌کنن اما در روز روشن چنین ادعایی رو به زبان میارن.
🔻
یک باشگاه میاد به زور و با زیرفشار گذاشتن فدراسیون و لابی کردن، باعث و بانی برگزاری یک تورنمنت سه جانبه میشه و دیگری میگه جام رو به ما بدید! معلومه چکار دارید می‌کنید؟ البته من دلیل این تلاش رو می‌دونم. هزینه‌های بسیار گزاف و چند همتی و خارج از قاعده‌ای انجام شده که برای توجیه آن‌ها باید هرطور شده یک جام بیاوریم حتی اگه تیم‌های شایسته‌تری وجود داشته باشن!
🔻
به هرحال در خیابان منیریه در شکل های مختلف و در سایزهای مختلف زیاده. اگه دوست دارن می‌تونن حتی با هزینه من برای خودشون جام بگیرن و روی پوسترشون بزنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107387" target="_blank">📅 20:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107386">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc500f316.mp4?token=rIA56L5J2tSdrVf7DhdRVsw_2Lymr05kTmPJz45UbCMl78TwZvdQt3CDxs11gWYt9THB0iP0sQHeC0zkRsQiuFs1Ph6dZnKNNG_cv_6iUFJxx7vyJfmZW2tnvI_ExuWOcA80oOgfZwH0vSS4EnomQU9FjFgY6PdKLTuLTHzvSeB7n_VBAtBcoxlW_FJ5hxgNSc2ERSz660QvdSI0QxJQGFCm4u574QVBFR0hCAzWvS6b2RYPMItWfQ9p97xCaein_pinumQ7UsEs_CALKLqfwmrf6HxQotXkMr9tPF21P12pKcW3QYnt1hOi7L9I1zwVFP0K9yCLAHOg698Xj-6iXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc500f316.mp4?token=rIA56L5J2tSdrVf7DhdRVsw_2Lymr05kTmPJz45UbCMl78TwZvdQt3CDxs11gWYt9THB0iP0sQHeC0zkRsQiuFs1Ph6dZnKNNG_cv_6iUFJxx7vyJfmZW2tnvI_ExuWOcA80oOgfZwH0vSS4EnomQU9FjFgY6PdKLTuLTHzvSeB7n_VBAtBcoxlW_FJ5hxgNSc2ERSz660QvdSI0QxJQGFCm4u574QVBFR0hCAzWvS6b2RYPMItWfQ9p97xCaein_pinumQ7UsEs_CALKLqfwmrf6HxQotXkMr9tPF21P12pKcW3QYnt1hOi7L9I1zwVFP0K9yCLAHOg698Xj-6iXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباه وحشتناک ووزینیا بهترین گلر جام جهانی مقابل مالی در لیگ ملت ‌های آفریقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107386" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107385">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce2bef5a1.mp4?token=iJQzNaaVNWWOYZd5V0RQVNSkT31GS_jghZl3JIRIaZASYl2sK9PiL7s1KIsRuCTOKKx4v0WjlVLktr--CMluc298m5u8r3sgIhdqW4a6mAceZu410pAsd7GLbZbG0iYB6v0FyRBCfYOQH0hSI7lwFPSafSRfIMbX7fDmq7rhuoy3-EmHKREfpO2xDz92kWR8Rh5W2vHXgObbVI9KQF1yO_vEhVWcFhd6aCmU8hfDpuCLHv5bAThwsjsHmUF3dX_rI46HAzm_cmX4E42xVRiRYY8Pz0r6yfXYsM3UpMhmoJsGfxe_d2RVv5PdCbFNa_q0yJxWJ_UWVtdGh1eSjQILVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce2bef5a1.mp4?token=iJQzNaaVNWWOYZd5V0RQVNSkT31GS_jghZl3JIRIaZASYl2sK9PiL7s1KIsRuCTOKKx4v0WjlVLktr--CMluc298m5u8r3sgIhdqW4a6mAceZu410pAsd7GLbZbG0iYB6v0FyRBCfYOQH0hSI7lwFPSafSRfIMbX7fDmq7rhuoy3-EmHKREfpO2xDz92kWR8Rh5W2vHXgObbVI9KQF1yO_vEhVWcFhd6aCmU8hfDpuCLHv5bAThwsjsHmUF3dX_rI46HAzm_cmX4E42xVRiRYY8Pz0r6yfXYsM3UpMhmoJsGfxe_d2RVv5PdCbFNa_q0yJxWJ_UWVtdGh1eSjQILVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی برنامه نداره ...
وقتی حمید استیلی میخواست برای فرهاد مجیدی
در تیم ملی امید دستیار ایرانی بگیره ولی مورد قبولش
قرار نگرفت ، در ادامه به مجیدی میگن چطور مربی ایرانی
برنامه نداره ؟ امیر قلعه نویی رو براش مثال زدن اونم گفت
که اصلا قلعه نویی برنامه ای نداره
حالا برگردیم به مصاحبه کاناوارو سرمربی ازبکستان !
که گفت تاکتیک ایران فقط ضربه آزاد و کرنر هست
چرا قلعه نویی باید ماندگار باشه ؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107385" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107384">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd8f68cc2.mp4?token=c8KkTjpJTswy9PXhuBN8AN4S5SxvYpwO1tQcSE5TzCuzKhfTGyAnmMSN2kTFGSTqGhI3a0aU1r1kUeuEXdp5h8bFboo907JdMauy2tsoHAJKpPwedr2X40Msew4ZfQZ6k8TPuRLXbQfSyrceFBi3xOvx7bkc_7DnwHh9R3S1ULc2JVFuun_JJesPAFox4xBin2ddVLLUJadgOAR0NRtuFs47RikaU__6oIvSSAGU1x-wZW7rDy1BEkk9muN2ysNYmUWeTmFMdgGg9aHOIz91ZQVR2O-VZETrPlwarw7YmKtDWc66rMdJYFVrkIK5rWRbDjTxF4FzoVTb7Cf_vouf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd8f68cc2.mp4?token=c8KkTjpJTswy9PXhuBN8AN4S5SxvYpwO1tQcSE5TzCuzKhfTGyAnmMSN2kTFGSTqGhI3a0aU1r1kUeuEXdp5h8bFboo907JdMauy2tsoHAJKpPwedr2X40Msew4ZfQZ6k8TPuRLXbQfSyrceFBi3xOvx7bkc_7DnwHh9R3S1ULc2JVFuun_JJesPAFox4xBin2ddVLLUJadgOAR0NRtuFs47RikaU__6oIvSSAGU1x-wZW7rDy1BEkk9muN2ysNYmUWeTmFMdgGg9aHOIz91ZQVR2O-VZETrPlwarw7YmKtDWc66rMdJYFVrkIK5rWRbDjTxF4FzoVTb7Cf_vouf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
وزیر خزانه‌داری آمریکا: اقتصاد ایران تا دو هفته دیگه نابود می‌شه
چون اونا فقط ۱۵ میلیون بشکه نفت روی آب دارن و بعد از انتقالشون به چین، هیچ‌چیزی براشون نمی‌مونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107384" target="_blank">📅 19:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107383">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f6084ad3.mp4?token=jz19gJahTw1aWQ11AFNy458SCPwOVa_Ekt_c_VE_Bc6TAFvYFqqS6elXtZCNykx9WIDzYvO0zcVZJdTMOfa9PQ-EJa6dv0TrWOxCdAO2zjHNEyTLJucw1Q6ZJR3ZGgKMS4YtuKKmWx0V-6eXvvqW08EhJ46PVI9CztMdcBCiZmPO_BzImlIYWXLkKxJG2P-maf7_NDA3DzbfW2RCP6e2wnCnvuY3vdyNXR9qccZFBUO3JCCfbGSpilr2ayQiUf9umoVwIigCauE1MFQPdi9TgBBAZLWemVcC_5AO7rJYSPFJq5MCeQpTBzmXd2ZWmpSZmPOwNIMG0G9hsMplVyVZLjZuXdRhjZugX5qQ81PQJMAsy8r-9Mkufy5C0XusQMk0DA0LC7EwzQx-X8m7UW-3gH3ST0j9Ywjl8zLZzQ8MpTuef87PvSLt0VBFQXBC1avUPeLGwYK4dReWmoAPb2E1PFED6Ar093ujBOk1LcRmhrw_Af-N88VpGRcy__cPb-3yTbWYpPQkqV67p-RDiBzSXYPPS5SBJgi1gHuVVdlCctGD-LU01YeODlC2wW3m8tMJk9WNosc169No7TPaiR8BYJznUWwrV9DmSZn_pwBxe5X1fz48nEJJRPcLyKAXKXfBPatoJT-jH0MKqKAvnLluOS46jThZGApbnNivznuPbWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f6084ad3.mp4?token=jz19gJahTw1aWQ11AFNy458SCPwOVa_Ekt_c_VE_Bc6TAFvYFqqS6elXtZCNykx9WIDzYvO0zcVZJdTMOfa9PQ-EJa6dv0TrWOxCdAO2zjHNEyTLJucw1Q6ZJR3ZGgKMS4YtuKKmWx0V-6eXvvqW08EhJ46PVI9CztMdcBCiZmPO_BzImlIYWXLkKxJG2P-maf7_NDA3DzbfW2RCP6e2wnCnvuY3vdyNXR9qccZFBUO3JCCfbGSpilr2ayQiUf9umoVwIigCauE1MFQPdi9TgBBAZLWemVcC_5AO7rJYSPFJq5MCeQpTBzmXd2ZWmpSZmPOwNIMG0G9hsMplVyVZLjZuXdRhjZugX5qQ81PQJMAsy8r-9Mkufy5C0XusQMk0DA0LC7EwzQx-X8m7UW-3gH3ST0j9Ywjl8zLZzQ8MpTuef87PvSLt0VBFQXBC1avUPeLGwYK4dReWmoAPb2E1PFED6Ar093ujBOk1LcRmhrw_Af-N88VpGRcy__cPb-3yTbWYpPQkqV67p-RDiBzSXYPPS5SBJgi1gHuVVdlCctGD-LU01YeODlC2wW3m8tMJk9WNosc169No7TPaiR8BYJznUWwrV9DmSZn_pwBxe5X1fz48nEJJRPcLyKAXKXfBPatoJT-jH0MKqKAvnLluOS46jThZGApbnNivznuPbWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
تقلید صدای باحال از گزارشگران مراکز استان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107383" target="_blank">📅 19:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107382">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/464a64d711.mp4?token=Z8Iphd5etdqb6qU_HrF2hN5nTxxnAtjR4Ts3t9SX24GqXPllRKx8JHgRSVsJhg0lAc7TKEUwxeppWohdM0dXoBlEPLaAnqdi2FyVlmM6lDe_I90lpDUqbMB944tsxtRSAHUpbFt2G-DlNev6wMdMlo9GJpfFT_BZY8BRQQB9j7Ezxj_HzdJiBk1eTPCPfYN-jzN02Tn-wi28yxtyAKekyPUwsJcW9sDr0OOYz2-hafrsinxoodumZKudXkvMwEFdx0ntJvMky5vQL7Oeb8C283vZ7rGSC0YCS1aKknPvz0IfQnZTFKaS3FL21ai5HoSFeLX1dgE0AuOI_smZJb4sBnkaag1j6ETMuYhrmn41_81bgQeyrItcOq8pxYRjP45GJb_35UtBfi0aZ5Ox8ffxNvzKhxwZCFK8klHvUWpFPepXGyPwzy5xZUI2e4FChvMlRFO3dv1UnsBpm2ihhEOT1GkHMoH4yEt-qEO7oHanlmpU9JZ5YdYDfY3EXEzsj-tf7RuKffotHbERrlgSATgBoaH3uj3a_78t5XnjHlFJsg2HnSZx6UJ1f2w26uJTN6eGLQWC3UbKncJdoYPMpp1l_es6EYULjspPuNn85kXPJmA70jg3N6C646HxUXxtvvPZ_S6XLpvHe8HBXJf__-DHAL-be9TTwbDTiIno-A6TxJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/464a64d711.mp4?token=Z8Iphd5etdqb6qU_HrF2hN5nTxxnAtjR4Ts3t9SX24GqXPllRKx8JHgRSVsJhg0lAc7TKEUwxeppWohdM0dXoBlEPLaAnqdi2FyVlmM6lDe_I90lpDUqbMB944tsxtRSAHUpbFt2G-DlNev6wMdMlo9GJpfFT_BZY8BRQQB9j7Ezxj_HzdJiBk1eTPCPfYN-jzN02Tn-wi28yxtyAKekyPUwsJcW9sDr0OOYz2-hafrsinxoodumZKudXkvMwEFdx0ntJvMky5vQL7Oeb8C283vZ7rGSC0YCS1aKknPvz0IfQnZTFKaS3FL21ai5HoSFeLX1dgE0AuOI_smZJb4sBnkaag1j6ETMuYhrmn41_81bgQeyrItcOq8pxYRjP45GJb_35UtBfi0aZ5Ox8ffxNvzKhxwZCFK8klHvUWpFPepXGyPwzy5xZUI2e4FChvMlRFO3dv1UnsBpm2ihhEOT1GkHMoH4yEt-qEO7oHanlmpU9JZ5YdYDfY3EXEzsj-tf7RuKffotHbERrlgSATgBoaH3uj3a_78t5XnjHlFJsg2HnSZx6UJ1f2w26uJTN6eGLQWC3UbKncJdoYPMpp1l_es6EYULjspPuNn85kXPJmA70jg3N6C646HxUXxtvvPZ_S6XLpvHe8HBXJf__-DHAL-be9TTwbDTiIno-A6TxJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⚪️
⚽️
چرا تیم امید همیشه ناکام است؟ این ۱۴۰ ثانیه از فرهاد مجیدی را گوش کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107382" target="_blank">📅 18:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107381">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107381" target="_blank">📅 18:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107380">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h1C5bR3fa4-wv_NT6_ZJvxSQYVJPc2M5td2QbWFtH7BdciJEPqmj0ncPGP-gKHIJ9ctgxgnqpqurJ8Ie3n6a8GFd01RvD4mLYKAdXYKiXn-N0ED3Mq1rqCmFpIuTVSzse8Q9CVcE6WnHQ7gEReBeT1GI5Gi-1v7yKJNdFWb0zBy1XyQ0bViF_ddSW1oGFkpRkcpy6q7JBRHxwAsl3MkBqp1Wewpsgkp27DJhO4I8mNbSYsfMdeoCU7dj55Mqqdq0_MCRJnZ8_0oEkzlA0GyIhF0Yvpfz8o5NCvsJQ7SZigbjYVNvvhM9hXZ0r14Mc-vEXlp2A3qbALgxdJBTeDGlbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107380" target="_blank">📅 18:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107379">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36187cd975.mp4?token=BdKyDJTEpfHt0NYp36L4N1PIk63pwH6K6FL1VYZ6QobZV_0r9gEm1VwN8XTJ35ZkZxpmoMD47s54MuGI5Tj3ydBTUsi1Y1ZKCOWCBbHa2wR610xygSFFv7Ws2_j5geMilGeK4Q6-lBwPwHpUoT2Ztu4MFJJRerJbCXf2LNbrItl_dMPMai2UKC6fZQFEg3cdxbpW2yzvFZvFKGXoIqrhzU8KzXeg7RSEh_HoRmobK6VhI3F1MlNFiZoSzYEJjRmg9_4UYQMchaLSIv60ZkrKyUpyTX744SjLpR49wYrC1DEgUPlU8cmtRvFw8cnjhq9TEvj1V_3ohwIMGecUj4PaHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36187cd975.mp4?token=BdKyDJTEpfHt0NYp36L4N1PIk63pwH6K6FL1VYZ6QobZV_0r9gEm1VwN8XTJ35ZkZxpmoMD47s54MuGI5Tj3ydBTUsi1Y1ZKCOWCBbHa2wR610xygSFFv7Ws2_j5geMilGeK4Q6-lBwPwHpUoT2Ztu4MFJJRerJbCXf2LNbrItl_dMPMai2UKC6fZQFEg3cdxbpW2yzvFZvFKGXoIqrhzU8KzXeg7RSEh_HoRmobK6VhI3F1MlNFiZoSzYEJjRmg9_4UYQMchaLSIv60ZkrKyUpyTX744SjLpR49wYrC1DEgUPlU8cmtRvFw8cnjhq9TEvj1V_3ohwIMGecUj4PaHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇮🇷
محکومیت ۴۰۰ هزار دلاری استقلال در پرونده کاریله؛ آیا تاجرنیا طبق وعده ای که قبلا روی آنتن زنده تلویزیون داده بود، مطبش را برای پرداخت این جریمه می‌فروشد؟ آیا دیگر اعضای وقت هیات مدیره، طبق گفته تاجرنیا از جیبشان این خسارت تقریبا ۹۳ میلیارد تومانی را می‌پردازند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107379" target="_blank">📅 18:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107378">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea1431c1f.mp4?token=RFNGde9Qa6eMcy2gfcIGBSFncvwpMeKf0F_3_FKYzP-rL4ZiDPGGcnA3DZ_ODx61r6q-7RYC9B1u4ulglZINuOMoY8fWkJe6Ys4Bx3DCJzIDw2XZKd3b_hPLswqg6kpVPjcS--fmM-wwC9GXpsT4aDNkVPoVb-rDNziqXuea8o54Nx-W6u62XcYqxn28ue5Em6u1WJnqr7tuq2WgHS-BkDli0EJQxPD6yRLkZacPdALPsl5f-aq5mtYZ1znal_c9j7fc6CEmpMmLlPX3ze5_rEghe6qGvBRVnpmrXdMCc7eOapKcjrTtRYCpp97-7k3w8r4cZMo6tCJ2s8jpah-T-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea1431c1f.mp4?token=RFNGde9Qa6eMcy2gfcIGBSFncvwpMeKf0F_3_FKYzP-rL4ZiDPGGcnA3DZ_ODx61r6q-7RYC9B1u4ulglZINuOMoY8fWkJe6Ys4Bx3DCJzIDw2XZKd3b_hPLswqg6kpVPjcS--fmM-wwC9GXpsT4aDNkVPoVb-rDNziqXuea8o54Nx-W6u62XcYqxn28ue5Em6u1WJnqr7tuq2WgHS-BkDli0EJQxPD6yRLkZacPdALPsl5f-aq5mtYZ1znal_c9j7fc6CEmpMmLlPX3ze5_rEghe6qGvBRVnpmrXdMCc7eOapKcjrTtRYCpp97-7k3w8r4cZMo6tCJ2s8jpah-T-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
درگیری شدید سوبوسلای و بازیکنان حریف در بازی اخیر مجارستان مقابل اوکراین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107378" target="_blank">📅 18:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107377">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49852d72a.mp4?token=EN8mY1K_g4kA-0r1hJmvrdZtT9VCFk-dmjC1x8NjYrgbH2IMKQkIEN649roDtOupc_8Gxt6T_CUKtEbM9WFZiPMCFb_uEQthEX329aws71Mrlwrci2AinJROtPNlhvPSPeiLrSu3rXinIEovyhU97k6fsIreghicu3BLRwj2WyoEh4-_7k3ukLh27ERO9dITZLIN_FG19fHHlUF5abOPrBVnZWMJP3UN9eXdXEPWvy6sBFVdYdqxq6Nmdw1RSEYOyyEM3Athoe0gCo_faA4S2Ue0JixXTuIItqQmKrSrQdONJe6IHft1HngH1K8QX4Ge3t7A_kNsQGyZRQSjgkUyVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49852d72a.mp4?token=EN8mY1K_g4kA-0r1hJmvrdZtT9VCFk-dmjC1x8NjYrgbH2IMKQkIEN649roDtOupc_8Gxt6T_CUKtEbM9WFZiPMCFb_uEQthEX329aws71Mrlwrci2AinJROtPNlhvPSPeiLrSu3rXinIEovyhU97k6fsIreghicu3BLRwj2WyoEh4-_7k3ukLh27ERO9dITZLIN_FG19fHHlUF5abOPrBVnZWMJP3UN9eXdXEPWvy6sBFVdYdqxq6Nmdw1RSEYOyyEM3Athoe0gCo_faA4S2Ue0JixXTuIItqQmKrSrQdONJe6IHft1HngH1K8QX4Ge3t7A_kNsQGyZRQSjgkUyVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
گریه‌های آرش‌افشین بازیکن سابق استقلال: نتونستم پول خوبی از فوتبال در بیارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107377" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107376">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81597ceff.mp4?token=P_SwknzcaxoGAz0tliHy12cau9jv1O0en6bdH5PDTw4dISk0ouJqSIZXXNwWUgzZZ7frxzQrGqXD0a__kjM6zzx9TNXZLwUBrXj2_sqzA19t1Y6rrHK9pxlngnAxaMVqZBk5GU7wncvKoWHvc1BEDWRT2NKvHS2MfVFpUb6IedDuDFZi8ZzgaXRXxuG0A20eBkLZaTT0KHzkCnOK-NgMkhjiHmTCosdTcqOqrYPyFnoQxZyiObUXYzwH9sLvUBrofwNYd-OMwcLiUbgcB20V6CTRh6ozLe9FZJeSB_hZpKd-2Ds_XMBEBtdhDHdKxS2mEp7mHzSxJl5xRlLem3qupA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81597ceff.mp4?token=P_SwknzcaxoGAz0tliHy12cau9jv1O0en6bdH5PDTw4dISk0ouJqSIZXXNwWUgzZZ7frxzQrGqXD0a__kjM6zzx9TNXZLwUBrXj2_sqzA19t1Y6rrHK9pxlngnAxaMVqZBk5GU7wncvKoWHvc1BEDWRT2NKvHS2MfVFpUb6IedDuDFZi8ZzgaXRXxuG0A20eBkLZaTT0KHzkCnOK-NgMkhjiHmTCosdTcqOqrYPyFnoQxZyiObUXYzwH9sLvUBrofwNYd-OMwcLiUbgcB20V6CTRh6ozLe9FZJeSB_hZpKd-2Ds_XMBEBtdhDHdKxS2mEp7mHzSxJl5xRlLem3qupA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
⚽️
افشاگری حجت‌کریمی عضو هیئت رئیسه فدراسیون: قلعه‌نویی قرارداد ۴ ساله می‌خواست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107376" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107375">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=k762ipX5iUAETAmAHeh-zQB-RCl8ZngCE7daZCMapBLU6eT_32QKolJLgvlIUABjSaZ5F0heMt6-5LnHLGzKQv5ekttT6cvWb1NId951xcHNeII95KzpfsjV7Z1LBih_fJF0_tPSNf5cxt0Km3vFrEynJyHX-JwS4WTccie1AZ0HJ4qGPDqA_gB0B_bBZ9QlvsdsMgb7brcb--71n1qYei_RtPHdxENbyXMRI_8Mmd1JtxyPlYrM2wAUsEdwjLi9faOl7sebD0j2Gty7TAAc--8LRi1JDagQcWpS1_MHCZ2UFI57fNHdv0-jhcr1cGErICnVwSuj6veAfMuOVeNStg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=k762ipX5iUAETAmAHeh-zQB-RCl8ZngCE7daZCMapBLU6eT_32QKolJLgvlIUABjSaZ5F0heMt6-5LnHLGzKQv5ekttT6cvWb1NId951xcHNeII95KzpfsjV7Z1LBih_fJF0_tPSNf5cxt0Km3vFrEynJyHX-JwS4WTccie1AZ0HJ4qGPDqA_gB0B_bBZ9QlvsdsMgb7brcb--71n1qYei_RtPHdxENbyXMRI_8Mmd1JtxyPlYrM2wAUsEdwjLi9faOl7sebD0j2Gty7TAAc--8LRi1JDagQcWpS1_MHCZ2UFI57fNHdv0-jhcr1cGErICnVwSuj6veAfMuOVeNStg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبرد دو هیولا از دو نسل! امشب در اسلوی نروژ.
🔥
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107375" target="_blank">📅 16:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107374">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119aac7582.mp4?token=M6ZGrSzvOlIcxN4nUDyYFM0YcsryLV7-3Ac93ECVggz-ZMKvj_8HRkw8W7E5KU0I5ecmg-zpwyJxzhqIYexrXJK8gn2yo0h0df3Ji-LssVyOvbzm-LMbkZGpwkFTB29FSv3TsixCoslbgGdJwmc-yj4kPlMsgcyGQRcsSDPsFnH5XC6bGKc6KO5FEbw1E7v5sMoSrO_DP9-CAJAvnACbDRFKeWwqL2KK-rZ77WomndkaIYQ2FG8I9t4UanpEuoSeCVMg6oH5qfdp1VR8xscXsqirKBfv0CP-VN0JIUoa4fgqhELLScJsxZxihRAJztLbPiq5Q4OPvAp1_8GO0Qa4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119aac7582.mp4?token=M6ZGrSzvOlIcxN4nUDyYFM0YcsryLV7-3Ac93ECVggz-ZMKvj_8HRkw8W7E5KU0I5ecmg-zpwyJxzhqIYexrXJK8gn2yo0h0df3Ji-LssVyOvbzm-LMbkZGpwkFTB29FSv3TsixCoslbgGdJwmc-yj4kPlMsgcyGQRcsSDPsFnH5XC6bGKc6KO5FEbw1E7v5sMoSrO_DP9-CAJAvnACbDRFKeWwqL2KK-rZ77WomndkaIYQ2FG8I9t4UanpEuoSeCVMg6oH5qfdp1VR8xscXsqirKBfv0CP-VN0JIUoa4fgqhELLScJsxZxihRAJztLbPiq5Q4OPvAp1_8GO0Qa4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دو بازی، دو گزارش، یک تفاوت عجیب!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107374" target="_blank">📅 16:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107373">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM6PyoJ2mv1SHLrDgAR8C_vDhVJ68oeAWeuToFDIWWPe7Mutk2SQE1-sVlVZx83tm8mTOsI3zyW0gGlcdThJ8u5LS9KZtBN29Okp0SxalW2J7kTP5WZoxhp24Sz7Xu2e_wm4ARJGneJAhgwrX-TB5HwfCuvOjnxTWv37354CmrJ7HEPlFON5r7eLsvpGCyO-I65wGA_FYRbGiHc7EReAVyf9JxwkA-82dQjGMoWkGxk4Wzg455vrJSmXoBeVuJkvEoUinK9ruGKk9UFzJVoXP8PIwl_v81p5DsFJTLkD_kuUbfqwMi2hIr7TjVqvcZ2ZV6kBBkLMCcEtMu7GgqItIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گاتزتا | روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتا قرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی هم یه قرارداد با الجزیره امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو!
هردوی این باشگاه ها متعلق به شیخ منصوره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107373" target="_blank">📅 15:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107372">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c9c45d7.mp4?token=b1jSAwk6-rTlVZmsEl9XcQ0ZvF1zBsc36OC34PreewmfQzqwqChT8PUQuG8gKhNUhjiuqwXQ54K1BHX8buBwKahAMNa_nQVznfO0jAr2ibLvjKJTCbI3blhuqQsINzfJPOlheXn9_TVurzV-gBQXWmBAkqq3EBGJyRfdAeSRHaJHdmLZnbzeiz4eORVrMmUWkPC1NMIaGnxtpHblMedZW1wjsUKBEOTJobhcNaaTDbo56i3EYmkBxYTEaZmm5C2gqJSuAb4XyFaaysxHCqj_dBF14EV5dn8Qa5_XOts0Rtb9OJ_CbgQfbrBMB34ibaaLjiYle6I4KXTzJ2higXfk4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c9c45d7.mp4?token=b1jSAwk6-rTlVZmsEl9XcQ0ZvF1zBsc36OC34PreewmfQzqwqChT8PUQuG8gKhNUhjiuqwXQ54K1BHX8buBwKahAMNa_nQVznfO0jAr2ibLvjKJTCbI3blhuqQsINzfJPOlheXn9_TVurzV-gBQXWmBAkqq3EBGJyRfdAeSRHaJHdmLZnbzeiz4eORVrMmUWkPC1NMIaGnxtpHblMedZW1wjsUKBEOTJobhcNaaTDbo56i3EYmkBxYTEaZmm5C2gqJSuAb4XyFaaysxHCqj_dBF14EV5dn8Qa5_XOts0Rtb9OJ_CbgQfbrBMB34ibaaLjiYle6I4KXTzJ2higXfk4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
یامال: این توپ طلای ما رو بدید بریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107372" target="_blank">📅 15:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107371">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c98790b5.mp4?token=h_mHWRIoydC3sPX83Ibexth-3EIL3mXQrm6KHU4limDe7F9gtGY9hhf5e86h-QvhmaWkkH5bWIzbJWu9mI_RAZSdoKL4Ki5Wjs2_6h7g4Ocn1zNydW33Agh9CuPavAcfN2d4zA0OOyveDH-F8Cj0lq6i21Ug8xXNkFViCjQg-w5HSIqb0ioNpPjMy_LWo_LaW6KSt6byuLXcKXFvIJ6yK5FfboPS-E5wovzdrYbDHg7SAShTAs6NhzKJ1kWHKgdLyTy68lrBlt1Bfkf_oiWvP7943fXy7fWQOL15JTFNcuE0BIWzUNAPGsCoXMGjcl-YdjexOLag11NEygvI9lM33Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c98790b5.mp4?token=h_mHWRIoydC3sPX83Ibexth-3EIL3mXQrm6KHU4limDe7F9gtGY9hhf5e86h-QvhmaWkkH5bWIzbJWu9mI_RAZSdoKL4Ki5Wjs2_6h7g4Ocn1zNydW33Agh9CuPavAcfN2d4zA0OOyveDH-F8Cj0lq6i21Ug8xXNkFViCjQg-w5HSIqb0ioNpPjMy_LWo_LaW6KSt6byuLXcKXFvIJ6yK5FfboPS-E5wovzdrYbDHg7SAShTAs6NhzKJ1kWHKgdLyTy68lrBlt1Bfkf_oiWvP7943fXy7fWQOL15JTFNcuE0BIWzUNAPGsCoXMGjcl-YdjexOLag11NEygvI9lM33Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پنالتی که هری‌کین در تقابل مستقیم با یامال از دست داد تا سرنوشت بازی دیشب تغییر کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107371" target="_blank">📅 14:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107370">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb8643-yIqhfBp4XVH7VBg6a3sTf9vRIN2yC7YGLBWUDij7r4LlfjZKhC6KZabbaFOQKJMw7lvgxnujhvRy0iatABhKeFbBpcFt42_xSf4xfg9YfgWdHn951LACP-06rOhffBJ3YvK_2MsknlfFMFGXHuT9cVfE9iOTSaexdM7KqIMifkQ5lhiJdBZ-jG7zRWXHif7S23Z4yhVvzCQHfBj6WnloR73LgKNd4bA6nB0nX6Cc57fh1xqM3LKekEyXa3O_bDp8qjotMJqnTOy1otoev1x-5jEm5VLgSDPb5N6LHY3zlwa41vmuE-VqREvmsbSuHno9ip2kdAIaB2_Zyug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پریشب نبرد منتخب آفریقا و منتخب ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107370" target="_blank">📅 14:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107369">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VV5fbwxYe7tf0MX0ARYpEAsrxixBC8nlTQ5jFWvGEu_8g6PF5l_F1ndwLhi6pq089FEuXuhdIB1czylaMz0mDOCwcpY9bY_8kzbU515ASj0ykds_9Hupg7xzExDAqlnkLyWJajSA6xXlcSNbITp4Bya4R-AYMFApC5rtETmEg-_JydFG_la684rMeVCQFv9bELO6dthY3B5rmMAUDIvBcXFsezTqP7ybleNXzYj0gGNh-Vx0JwTPpVFo_bQkO-4tU16WK1jIlqEKh0_9v3QGOk7tNdM05cMFX8Y-97Kl_UgxZjLoObxFHK-FffqQMgfeMHB5WSa3KJ10NXaQooIowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇪🇸
برخی رسانه‌های اسپانیایی گفتن که اگه سیتی محکوم بشه،‌ ممکنه هالند درخواست جدایی بده و با توجه به نیاز بارسا به مهاجم نوک، این بازیکن گزینه اول کاتالان‌ها میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107369" target="_blank">📅 14:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107368">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t96aphotdODBeZi4G1AawWYpO82yMGMdr0tnrMHsKgt-aTGeppaCV1kJ0cVzA7PzikFw2Ue7TF9N1AS-UusGYxWAnzOL50NMhHcuXwiKzq9HD0py-H03AUI0tDtFP4LMW5hwapD_w7QJccTLqNeEjzyBoqhCK7PRbVVGdLkmFdBbeffQd_2VtFFmA5krRpiuH-9nAfRHbBf77xZ9SW-rhQ1sRCrBsedPqAVoU37hiUIvcmCeOls18be7gsNTsTAqsbbgEio5UGobwhRTCKZkh6MzuDLlEL9odD4UnnwMNARZh3aPRzDbd8J6__H805ZXhKcSfMtEHNjtMMd-HdQxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇧🇷
نتایج ضعیف برزیل آنجلوتی در مقایسه با سرمربی اسبق سلسائو در بازی‌های دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107368" target="_blank">📅 13:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107367">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEV_tQ3CBnn2R-0bIK_fB0FYIfZ8abBGLiIHtOmDLlIpRU18KjMJRWltNhkKdpKNelEXXH0D38sgd7ZnNcIDR8FQJl22IfxFOSodhxFT-K64QcuQ4HoIsoZtFBIQ4eCTe4Wvu_zqp-h8z7dpUQngDAQ9Seq8Pys68j0a-0Ey3EX64xlQGOlJlEFCh3rI7oq08HCiyIGTiSqVYKTVwrZto_maFRCVG3PAh3zAvTQK8pLYdSLyOX5kIuotiYL2IKXTOROaR67mqmur0_s9OLjMbgNCT0AcF1Ffdo1EuZ9Ql_9IBIyZ5VrA7agOQ97uDR53jy44nlzOUhKb1exHnkLoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
اعتراض تند عضو هیئت مدیره پرسپولیس به شایعه قهرمانی فصل‌گذشته استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107367" target="_blank">📅 13:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107366">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d99adabc.mp4?token=bx1xaaF_otYvodMMD6g63INiLc2_2y8gQCLgCDzOeZGRCefdaDllzK-OW3niMUXGzohey0cS0XywOATV2hVdK2tXM_0IkdqGh0u-guZug5ei7uK8Sny9kSNRlXb3Gj-Zx8GuftRMZNEvdKwqjJmBsM_X8C48k99Zp-kYwfPlMJpRrwZ-j4bGrzQ9Yqa2bqzU5sZw9BdJovj-5ICvNF7hV_K2JiuV6Ajdy-Wukt7LfH5vwPZAft3x4rHnPuMZaZX8R7zvwr-ro2caCwmCTY2j3pTOMhMjm-wnZb-JhkGaz5Dp2SVuU8gnqSyASt3ysMnZ2MrQUgMvlotUUXtQGOlTQUn6MPD6ljX3pEmGQ-1K4HYH_hQ40N0KcUguFbA8ZrTSxAoLjLBChyGUZw-1SIWiHVJM6--27rZJi_ZIsgz0flipe0CHQtk1GX-m8yt7wMlVwh_GygYEv-BzvWKxk82d9dcPUWKYdIFTRS5cL9-pLQ8Oczc4p43iq_poDNZ-xJehpOvcXjfWqHqg8UTn8vAWdaMqszCm9iK55-hbg3ZAjGGkyoP61ZqiPePdn-kwVdWEeOLypWKczhrxJdZfRWD83JiJTE_FHpYZHS88PcNeEqk7fjkgbu5VTOf2M8sNXRjeJqQ53yXg07JPSu4of9KauJBFl20FrY_r8DGzPSXkKog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d99adabc.mp4?token=bx1xaaF_otYvodMMD6g63INiLc2_2y8gQCLgCDzOeZGRCefdaDllzK-OW3niMUXGzohey0cS0XywOATV2hVdK2tXM_0IkdqGh0u-guZug5ei7uK8Sny9kSNRlXb3Gj-Zx8GuftRMZNEvdKwqjJmBsM_X8C48k99Zp-kYwfPlMJpRrwZ-j4bGrzQ9Yqa2bqzU5sZw9BdJovj-5ICvNF7hV_K2JiuV6Ajdy-Wukt7LfH5vwPZAft3x4rHnPuMZaZX8R7zvwr-ro2caCwmCTY2j3pTOMhMjm-wnZb-JhkGaz5Dp2SVuU8gnqSyASt3ysMnZ2MrQUgMvlotUUXtQGOlTQUn6MPD6ljX3pEmGQ-1K4HYH_hQ40N0KcUguFbA8ZrTSxAoLjLBChyGUZw-1SIWiHVJM6--27rZJi_ZIsgz0flipe0CHQtk1GX-m8yt7wMlVwh_GygYEv-BzvWKxk82d9dcPUWKYdIFTRS5cL9-pLQ8Oczc4p43iq_poDNZ-xJehpOvcXjfWqHqg8UTn8vAWdaMqszCm9iK55-hbg3ZAjGGkyoP61ZqiPePdn-kwVdWEeOLypWKczhrxJdZfRWD83JiJTE_FHpYZHS88PcNeEqk7fjkgbu5VTOf2M8sNXRjeJqQ53yXg07JPSu4of9KauJBFl20FrY_r8DGzPSXkKog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
على تاجرنيا مدیرعامل استقلال: بیرانوند برای آمدن به استقلال پیام فرستاده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107366" target="_blank">📅 13:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107365">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1582f31111.mp4?token=BESxIK3uAic1BUoxkx-0F2nNBOv1QH6di46U4FkOuKj_8QrfXbhfPLNCdg75A2YVl2k5NJ2VdqstGylDI4puFzgEwqdypXQ9Wi1S8GGgY4Cys8o8nF3sOPpZjOTlKKScvNh4rWHQgKeRPVJsc6q8ib-HlWax4b1pfQBmDxSKI2v5ns9TBpgwhGWnSY0gGYN6qtVLYPlWspJwV9NCDZP5JFZEWQNMYH0BUhx2Lmmpsnn-lrNKg216SKP0At9ITp5VTBInEyBayrZflZTJ6tgIfRIrs-T3ALAoXColCDcV8eFucDyPJHe3qMpMGuAn1ipQdy1jWlYBrfjbmX4KppzBAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1582f31111.mp4?token=BESxIK3uAic1BUoxkx-0F2nNBOv1QH6di46U4FkOuKj_8QrfXbhfPLNCdg75A2YVl2k5NJ2VdqstGylDI4puFzgEwqdypXQ9Wi1S8GGgY4Cys8o8nF3sOPpZjOTlKKScvNh4rWHQgKeRPVJsc6q8ib-HlWax4b1pfQBmDxSKI2v5ns9TBpgwhGWnSY0gGYN6qtVLYPlWspJwV9NCDZP5JFZEWQNMYH0BUhx2Lmmpsnn-lrNKg216SKP0At9ITp5VTBInEyBayrZflZTJ6tgIfRIrs-T3ALAoXColCDcV8eFucDyPJHe3qMpMGuAn1ipQdy1jWlYBrfjbmX4KppzBAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری‌که بازیکنان آلمان از یورگن‌کلوپ حساب میبرن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107365" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107364">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8b1d7243.mp4?token=sVGjE6FQ5UG6LucerQ_1sPU1YM9R5wzLtlzcmrVgKszFdUotZGEN8_V5tpQfVnRaMNWDCZsfMPFaLQGVm7M0QYbZX13nZX-5kTf-WgjtEyMCFc8WIEWAIYA00GyLCwlHUrAX0o3SS8StM7mIRmPSgDFkOOSV6My-7O-wCJCIIksd8mU-fblpNkVazW8Mbur5nG__N3n1TIU9XkckLpM0Oil7mM3EpUP8C6wPMtTv-oqIUo2ZJCtiERmdLABZX8r0O_UXxXE_nWona0CX3h7EkG9uWEuMXk1xnsoTTpSEe0E9qoBa4ydHx3Fk7JFMwgPa4crdQonz8yqZk-9vWwo3qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8b1d7243.mp4?token=sVGjE6FQ5UG6LucerQ_1sPU1YM9R5wzLtlzcmrVgKszFdUotZGEN8_V5tpQfVnRaMNWDCZsfMPFaLQGVm7M0QYbZX13nZX-5kTf-WgjtEyMCFc8WIEWAIYA00GyLCwlHUrAX0o3SS8StM7mIRmPSgDFkOOSV6My-7O-wCJCIIksd8mU-fblpNkVazW8Mbur5nG__N3n1TIU9XkckLpM0Oil7mM3EpUP8C6wPMtTv-oqIUo2ZJCtiERmdLABZX8r0O_UXxXE_nWona0CX3h7EkG9uWEuMXk1xnsoTTpSEe0E9qoBa4ydHx3Fk7JFMwgPa4crdQonz8yqZk-9vWwo3qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
❌
تاجرنیا: در پرونده توهین دسته‌جمعی هواداران پرسپولیس می‌خواستیم به دادگاه CAS شکایت کنیم که شخص آقای مهدی تاج به من زنگ زد و گفت از پرسپولیس شکایت نکن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107364" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107363">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107363" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107362">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAYvDbDzFubBlmOPaXMlv_0zo_Ub9MlUrgVW1ZjTyxeN2g2HFT6B2GVI8rcv-AK5I_3W3q5siJYiN8dBddkPvqmyj0P0RrV9KozPvv5dh7wMX4wWdcyBhgEpMinb8L1mRsQlz1dWGNLVy9tR5jjU12IxMWitXjnKzmHoQ1d-ubm86X9caNZjx8A6aZc6YEdIVemquNENiiJ62E0o1nC5Sxn5aLu2G7tcH1z5W6cdzMd4fwYvu7QyOsU3ZAelbhlMi9_uL8mSy683N0wTkeE2wRvwrpoMWI-4Wm5c_E8amBeOh7-9K-04Dkb4W-O49Ssr2dlT1POHe9f_7k6jX8wrqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
پرتغال
🆚
نروژ
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۸ گل زده
نروژ: ۳ برد، ۲ شکست و ۹ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107362" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107361">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6292835767.mp4?token=PbboC04g31qrPokSefmMgz6qCt4COT57V_IBJkU7kCWVpZ6VN61oaLOY4nDBvjigeucM3fqE1-tVPBeKjgSxBhP92gyHW_DaN9DpO9XFOsCA9jcyEODQ64uvVvJ3koJwuNHjSj7S_6rFGEiQ6hJhYZYnn8GDYXtcnz8JMxXHZKs9StMMJVIvBkNeh2qy9nBar9PWNUta5Q_C8jSN4dXsSrT5Y2UfO28bBSUB2MW6IdrcGGvpMA2wD5oc9Zq4FJ3RrfpThp5SE1bQ0rlVyf2BDOK99q2lZ5mQfGb2zAM0r1rU8rQVhQDjGd1V551fUSbQmCoSA3_0nhGojADqtv6AMoPIe6NEIEou_klYpcr4M-GfgSFScwa3vs5StsTb0aHsRUQOQpu3tw4ix6LrHxNXO1tYWNLfqCv8dKPdykGkv8fC7dS5DgLVLQD1HFU-okrs-VYnoMFSY4a-B6uESdP9IurGrZEiMw_MFDIKtiose8yEaEt5Oz9NZMn3PFSAxX029-is4SJ2dDQCaRUHbCnGznyFK3Mw0MaSd2oDm8rNXVQ1ZD185j5PxGGqWrjylaGLdrAjnUMgisBkWQ1UvfWG_N5nIYZSAg8ThDZwZ00mjbg2mMyYnn8-4EpFfTGLkoySpNm-pt1EriosyxgKXeH8uYf5KLPmUtoYjLH0G57l2Bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6292835767.mp4?token=PbboC04g31qrPokSefmMgz6qCt4COT57V_IBJkU7kCWVpZ6VN61oaLOY4nDBvjigeucM3fqE1-tVPBeKjgSxBhP92gyHW_DaN9DpO9XFOsCA9jcyEODQ64uvVvJ3koJwuNHjSj7S_6rFGEiQ6hJhYZYnn8GDYXtcnz8JMxXHZKs9StMMJVIvBkNeh2qy9nBar9PWNUta5Q_C8jSN4dXsSrT5Y2UfO28bBSUB2MW6IdrcGGvpMA2wD5oc9Zq4FJ3RrfpThp5SE1bQ0rlVyf2BDOK99q2lZ5mQfGb2zAM0r1rU8rQVhQDjGd1V551fUSbQmCoSA3_0nhGojADqtv6AMoPIe6NEIEou_klYpcr4M-GfgSFScwa3vs5StsTb0aHsRUQOQpu3tw4ix6LrHxNXO1tYWNLfqCv8dKPdykGkv8fC7dS5DgLVLQD1HFU-okrs-VYnoMFSY4a-B6uESdP9IurGrZEiMw_MFDIKtiose8yEaEt5Oz9NZMn3PFSAxX029-is4SJ2dDQCaRUHbCnGznyFK3Mw0MaSd2oDm8rNXVQ1ZD185j5PxGGqWrjylaGLdrAjnUMgisBkWQ1UvfWG_N5nIYZSAg8ThDZwZ00mjbg2mMyYnn8-4EpFfTGLkoySpNm-pt1EriosyxgKXeH8uYf5KLPmUtoYjLH0G57l2Bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل‌های زده شده با ضربه‌سر رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107361" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107360">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psD62gi5zYgQ2Ki3oM557QKUKTwJs9ZXiMcpMXAb4OdA0DbJlze1n8Gi53CbxJ6d4mokO-Tq3CTjkgykPKZHswmVNa7b6au9oSyf-D55njIPB9JDXE8jBVTI-jFfdo0NTdw8G1QWF3UoKllhSf-W6948scG8dOuBc5gEnFWxhMzt6aFk5MO6U-RUoryXEUnF9cnKLqhSb5IziJQAQpBKlm7jVFZtw8LYkIARAa9uQkAOuSJuZnDZAG1OsQSn3XziZxCUc1ovUYQNr2yXTu0I4YtOC2BPOfNeEDgkJadqQio8Xcog75dpTW5zQrIbrg4oonvqwhVoKqtHmc68ZzsKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107360" target="_blank">📅 11:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107359">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMYVmU4qDodYn0UNNlPcfhKo-ijfs523CEMCoCXIdZ-0myE_H1dnYub8LRZg2twKNJj6Iu7QOFp8KZL8TUphwGX4tPCCCqc7CrnToZDitBWQ4G19wo3mejWUKYQW11wGahMMIngcM_emRdWLqd_zY1SqMU_UNbf0E_4wY9mXlP_x0hQSAThLQDXF3ZcZQJAgDNSNp05Xoez-nOedaF5D1aoS6MjE7tNoTYomfG3vAPdRLQ8ul4y3GjjjXTYDb5rdOEhgY7Zyuv_8cFY58PGZ45SnflpvDrs8Fqs0rLKSW4jdXq-5lcVSwdzNQZlz5wpyGlJZFSP-DMVBM2MC_sCvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
لیست محبوبان و مغضوبان امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107359" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107358">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184858d60e.mp4?token=NmJD8Y8ZzoCnlOsNN21N-qYJgbVNAwfJ0InsNVUFp6ycrwBG0_hHZjExOTT0Z6xDsMp1lANyXTb5PoFqUbkv-Z0wi9vEgy9NgeBYjyrvqIfiYZfj78j_jNaP0e-S6uxkhKujYlu8m9swcak9HTD52jzDanmGHkzhXopNtKscv0-d3Ucu8Sy-Wo0ZSIw3dFfUPTcDHqR5OKv71AdsjMG0IffbFZddnWb-P8i0Uk_spcIVoPasQXoiX-DgMf7fi2VYHLTdiB50bjgBjGzoqIbtwNQ_oYXfQ5pN6ORiJluXBW2HKEvNkU30cgLDZoK9Oa8qTRnwdS104y9i5FMNMYj16oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184858d60e.mp4?token=NmJD8Y8ZzoCnlOsNN21N-qYJgbVNAwfJ0InsNVUFp6ycrwBG0_hHZjExOTT0Z6xDsMp1lANyXTb5PoFqUbkv-Z0wi9vEgy9NgeBYjyrvqIfiYZfj78j_jNaP0e-S6uxkhKujYlu8m9swcak9HTD52jzDanmGHkzhXopNtKscv0-d3Ucu8Sy-Wo0ZSIw3dFfUPTcDHqR5OKv71AdsjMG0IffbFZddnWb-P8i0Uk_spcIVoPasQXoiX-DgMf7fi2VYHLTdiB50bjgBjGzoqIbtwNQ_oYXfQ5pN6ORiJluXBW2HKEvNkU30cgLDZoK9Oa8qTRnwdS104y9i5FMNMYj16oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
به‌مناسبت عملکرد قلعه‌نویی یادی کنیم از این افشاگری تاریخی محمد مایلی‌کهن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107358" target="_blank">📅 11:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107357">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f1db9d0d.mp4?token=uJLrPWa1qgh5fPF8KJQRGf7q_BGQuq6_hzmD7_Xwp3fhAQMsxBNtgaIeCVWq7QyFHBU90Q5dNCcVfeX-oT_ubzJIitcL7wWw9J6wVDd5XzGaJcn_NiumVw10RQcQAIX_P_R2PU6LS00pf2uqclsgPYNwgVBqbEpAqfsYrbW3Ck3JGITE8Kfsq62Wi7vTHqskRrpJEeYphcqgEdWpZg9vZ4ZLtsyZs19Rbg_ihcHZG8Taf6N_wJRUTKSL1qEwXKrsTXEBFP3lYLCLajZ7oQJ6GUcpsbjLXI7ewgpoOeGFqQfvFct9cD-i-weNEbgI1sVxyIEeN1MCGEHibJ7AoO8viQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f1db9d0d.mp4?token=uJLrPWa1qgh5fPF8KJQRGf7q_BGQuq6_hzmD7_Xwp3fhAQMsxBNtgaIeCVWq7QyFHBU90Q5dNCcVfeX-oT_ubzJIitcL7wWw9J6wVDd5XzGaJcn_NiumVw10RQcQAIX_P_R2PU6LS00pf2uqclsgPYNwgVBqbEpAqfsYrbW3Ck3JGITE8Kfsq62Wi7vTHqskRrpJEeYphcqgEdWpZg9vZ4ZLtsyZs19Rbg_ihcHZG8Taf6N_wJRUTKSL1qEwXKrsTXEBFP3lYLCLajZ7oQJ6GUcpsbjLXI7ewgpoOeGFqQfvFct9cD-i-weNEbgI1sVxyIEeN1MCGEHibJ7AoO8viQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
سوپرگل‌های بازیکنان ایرانی در تاریخ به چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107357" target="_blank">📅 10:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107356">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805925ad6b.mp4?token=GugWogvlmZV3eYxmLCMdvkcNjhVVTBa58JNaMOS_fp31bV7RlGcfDPe07btYWOH070hF6f9VQOZGw4lT5sCsh8M7qouy20JMqjazMHjHx1pWB9Z2KRAkK4xIy8TQ6b2foRR5Ou5VjMnGneFwUPc4cHq5Vv-bTWmmYnDLMgeZMVDN5589mu3Q7SMRZz3D5Uezp5wS2vO8ajH8ku_R3GixC4yfuyjo--Zj5kbm4BTCWuAbiAl_tbOTguTynr0s2RY7XweeWE-XhYMmx9dXpgQjEv4wMh0oSIaR_nPSqbM6Bz0EvAxQTvSJv96vaT6hQon7be8xElpG6qASBP1F3wZq1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805925ad6b.mp4?token=GugWogvlmZV3eYxmLCMdvkcNjhVVTBa58JNaMOS_fp31bV7RlGcfDPe07btYWOH070hF6f9VQOZGw4lT5sCsh8M7qouy20JMqjazMHjHx1pWB9Z2KRAkK4xIy8TQ6b2foRR5Ou5VjMnGneFwUPc4cHq5Vv-bTWmmYnDLMgeZMVDN5589mu3Q7SMRZz3D5Uezp5wS2vO8ajH8ku_R3GixC4yfuyjo--Zj5kbm4BTCWuAbiAl_tbOTguTynr0s2RY7XweeWE-XhYMmx9dXpgQjEv4wMh0oSIaR_nPSqbM6Bz0EvAxQTvSJv96vaT6hQon7be8xElpG6qASBP1F3wZq1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
سکانس‌جالب و وایرال شده از مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107356" target="_blank">📅 10:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107355">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
⚔️
برخی از لحظات خشونت دیگو کاستا ستاره سابق چلسی و اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107355" target="_blank">📅 09:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107354">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUlw5ZekvoL6kKMu012FrF2n0FoT3CqsvYzmRXfiT4kaRZLvm7OCXDNvPjOa1-me7plobyOV130Usox6NJKjpFXgA4Q2NN18YJZwEpFiaxYeDfPzi-Q98Zft-LaqQOYlakRxBsCYZLxvvEKxSxGgyeZ2sT2cAdjiMrakczBX2cN0Ufckuj5t1ZlwKbnahfDEUW-tpXmEjvytWfJDGkjBU83BAZIn_SuiLbC03W9_epxdN7Qy7uxBKWFWSWjTPJekR8bVRE6rraNn50QqlBMSmTc5hf1DCtWArnLaH6LUetENZJpL7WKKreX8qk1-HPogE0kZILig082ay6QCDQG3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
ضعیف‌ترین عملکرد‌های تاریخ رونالدو در‌ پرتغال که بازی مقابل ولز در جایگاه دوم قرار گرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107354" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107353">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc355e5eb.mp4?token=g_W40jbL5a7Lrj_J3iLos-bR0m7CJQNk9r352z84s4lMkKxJMZxZEm7IrY39y9YzH-ZwxfnXo45XJc2k050uGlYxqlB_MXVvYQrtiafC54lcyyWJHkQnxdDBjdxYmhC_iGgKZbQ7A7EoOtHC54P6TyoOCOXK-xqI3X0PP2hp8fmuNr2LQ9ayyTFrc9DSoJhAoI3HWo1eP6LU_nSbL5nYUZJWyPgpms8J2lMRf-I4EDLLuAKXoXVEbLFfRNwE5aVRwvFYUODYMI-QBF300fr0psjr4_27IKoNjKqI5AaEA9ez0_Nf3rXmxOHfaOPRJYgkhruXcGdTp3RO2l89g307-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc355e5eb.mp4?token=g_W40jbL5a7Lrj_J3iLos-bR0m7CJQNk9r352z84s4lMkKxJMZxZEm7IrY39y9YzH-ZwxfnXo45XJc2k050uGlYxqlB_MXVvYQrtiafC54lcyyWJHkQnxdDBjdxYmhC_iGgKZbQ7A7EoOtHC54P6TyoOCOXK-xqI3X0PP2hp8fmuNr2LQ9ayyTFrc9DSoJhAoI3HWo1eP6LU_nSbL5nYUZJWyPgpms8J2lMRf-I4EDLLuAKXoXVEbLFfRNwE5aVRwvFYUODYMI-QBF300fr0psjr4_27IKoNjKqI5AaEA9ez0_Nf3rXmxOHfaOPRJYgkhruXcGdTp3RO2l89g307-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
آیت نوری مدافع سیتیزن‌ها تو بازی الجزایر مقابل زامبیا از دستور کادر فنی برای گرم کردن خودداری کرده و به همین خاطر از اردوی تیم ملی الجزایر اخراج شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107353" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107352">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e5fa478dc.mp4?token=r-YQUN1t7hA1VCZ-dw6JLh6f8vu7HTZPqw9f0ojUZaTxmipwLDrHETatjf4E833MjYmA_ztpjgevpQ_U6clX-oOF9Phok-yvk75pQg0i3D9-L8QlmUUBf7LnIaYLsRcf074vi41VsG7ClyyXcqk0n-qM3O1Veka_9JuW50D7npX5VwRl9tBdKH3xZT4fIFX3gQNDnJzSa4Ohh6V1X2WS_HIs2ZlZbgV_rJmS_12V5AWPx6odAJpsvpET4d2XX6UlQuBgQ0nM22WCqnDhWQLk7VjT9ssBrROgwMpMif761gDtlo47YWU7k5v9TqrxPW9tN4ulVZccJYdNHbQ4-NlBUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e5fa478dc.mp4?token=r-YQUN1t7hA1VCZ-dw6JLh6f8vu7HTZPqw9f0ojUZaTxmipwLDrHETatjf4E833MjYmA_ztpjgevpQ_U6clX-oOF9Phok-yvk75pQg0i3D9-L8QlmUUBf7LnIaYLsRcf074vi41VsG7ClyyXcqk0n-qM3O1Veka_9JuW50D7npX5VwRl9tBdKH3xZT4fIFX3gQNDnJzSa4Ohh6V1X2WS_HIs2ZlZbgV_rJmS_12V5AWPx6odAJpsvpET4d2XX6UlQuBgQ0nM22WCqnDhWQLk7VjT9ssBrROgwMpMif761gDtlo47YWU7k5v9TqrxPW9tN4ulVZccJYdNHbQ4-NlBUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حجت کریمی: قطعا انتخاب سردار آزمون در ایران، تراکتور است. به هیچ عنوان دنبال جذب اوستون اورونوف نیستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107352" target="_blank">📅 08:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107349">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn5yYQGBcq-OU7b1_i1sizJYdTFd1c71kYmWXshzmMsNGplIQ5hF-xhIbyZUYvtIQLzrOi0OPj90Jm93nnOK_22MPqXHjR1b6kNsDNMvynBLF4HwyYnDT_IaH5R7BOofueEfpNGbZeyQvDe9SlzFq_z0Clx1LwtZBTXpRYo_DwqvuZidxagYxcD3FFtcIO4KbzW05xbmlcrZkwiayPI3Pc1YpuJ6uPtXJ8XkwRkMSqrSThIV08S7Xa8rRoIxS8LuKdSBGpTgz5L3Fl3NNYYnyoOBABf4X3A2X-ZoGpeTT3XHOn6GE8VnrhkrpqFKYSRDwVWtyhlYkilvwhXP73Id2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گوگل رسما ایرانیا رو تحریم کرد و از این به بعد مردم ایران دیگه نمیتونن حساب جدید جیمیل بسازن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107349" target="_blank">📅 00:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107348">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q929dFC8TvUw28mfwYdb6qAntmtyaMKfnOQbyi7Mrn0kyGI6RmSYf9xSH_5J7alfwH-oZI-fgN43I8UcDBmZtKOcKjip26NpLu0n7i5otaJMD__JfZlYwCZYJrEssSgIsip01jgexJf89bIlDSJkoMxfE6WlOojpQ72qeRuXDg9hH2r9t1tUnTf-cbCK_k3bsNAoQOzIcuRlVGhXPwE9pTX4YC1ZtO9hRD79Bx5MKWJZ3pe4198oqoBJYGtecSdXDlESw4KnW8MiVYAaz1Vrk0mblz2JghF9dRi9sVilt0q32CTtO8_fAPwZd_6eCPj1S6f5MZ28l4ETK3b2FLxz3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
🇪🇸
فابیان رویز تا به امروز هیچ بازی‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
🔻
51 بازی؛ 36 برد‏؛ 15 تساوی؛ 0 باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107348" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107347">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇪🇸
🚑
رئال‌مادرید اعلام کرد که ابراهیم کوناته دچار مصدومیت شده و مدتی از میادین دور خواهد بود. به گزارش برخی منابع، این بازیکن به دیدار ۱۰ اکتبر مقابل ویارئال خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107347" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107346">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCYZJHcV7oTq7eik8E6Xv8-5-YTT9KggUD3Na8AqBZ5fBzoy6FSwTQ0WmS98mKB6NyasUyrNQhL6QJU0sNGgLGMMlWznc59QAKNC_UqHRU6JF5t_rjjyecbnGdqsDzduB5V5SOYi0bNGM1xdp1fBwlqcKX8LnGN3eSm8dqwMsiATEFKYndrDYFyd499ib0roC-vTSEANIYw_6b7QcDM0pS4JrKBDNUo7MiIFWbbLD-zjVTwTw8ntjTG_n8tlD5dBG1py9VsQvjfLI2wbqsnpcZoJHP-Yon7oG0JpG5uVO9gjmYkRKnQMUi3TwFD4kWqt1mhrOkxHc1kIT2T9FgGsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
طولانی‌ترین روند عدم شکست در تاریخ تیم‌های ملی:
‏42 مسابقه —
🇲🇦
مراکش [2023 و 2026]
‏39 مسابقه —
🇪🇸
اسپانیا [2024 و ادامه دارد]
😳
🔥
‏37 مسابقه —
🇮🇹
ایتالیا [2018 و 2021]
‏36 مسابقه —
🇦🇷
آرژانتین [2019 و 2022]
‏35 مسابقه —
🇩🇿
الجزایر [2018 و 2021]
‏35 مسابقه —
🇪🇸
اسپانیا [2007 و 2009].
‏35 مسابقه —
🇧🇷
برزیل [1993 و 1996].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107346" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107345">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmhK4klmx_MlEku5b9Qcr5BZJyu37gWJDK3QbrEeMaKjqit5XP8TAVqvdC3X34yDAq8Yy3bnI9ePeJhIX53W24T3pSBcYrEbaX0im7dUo__-lnCEoZWfon7OSbnQ_IN9bITOL84PSRMS1jHANHIZCDq-zMInmsRhQw7-LJMvokO8ImzPnTGW_gLmJmnx8AKTQU5d2Agnigh165RVjCvE2Ws1fKCgXV_ir-gaeii5nF2aRORJ7z9uVR1ZDkcdAiDO42_7T3Kr5-TAiRXXrqfrT0mucCqzDCQ7BU8zaUBq1qOW-rRiOmHO2DJERHN74vJm-4ddpwabllLqO2YG4Sq0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇭🇷
کرواسی در شب درخشش لوکا مودریچ ۴۱ ساله مقابل جمهوری چک به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107345" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107344">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QydXyGVzykIZT2UBrYT78cuCqUvwDtfUkJ8P81Rre7EIh2RlWpszV8sggaKcXe_4XNdRmZ9ioNjh5ZCzeYZTgQSX15p1JOq7JJWThDybZDN4rKW82r36SHhfOY2zbAH0wCDGSsFKNyaVOsSVGPz8BW20dOLuqTYqWiyQVnIwUDLt98jgepigEJaKM5XGlfA3MGYRCmxjei4XaAwWIUzDmONPqd0VLzsgYqHHAhqBB04ZchuGVYvQL0m6LyhGoNzhEdw74aN1FLAokwn69T-XfowEG1ej8BNgcBcvtRW3doz_2fpcwm_SKbX7goRZVcfVTA7nz2FTGEvySG_5lxqmhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ‌ملت‌های اروپا؛ قهرمان جهان در لندن انگلیس را از پا در آورد؛ یامال بازهم ارزش خودش را در زمین نشان داد!
🇪🇸
اسپانیا
3️⃣
-
2️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107344" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107343">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494ff796bb.mp4?token=F-5OufYh3seaMXU6QsuXqbDV2oCyHhk_0OzPpvboK4F0lfqwfk9kt-b_QPnV97QrabR9KDwzmgcymEmJh2egEmVK9L0EfUxklXfIrGOcpoG8KEaJdhizDJizQgSHI6KB_LDLRhALgkWaIvmti9ZBhKLF5IJGpYpzu9rWSVXxtMOvp_C-ivn757hnDFEM4Na9cU4G0XlQbmuF4slzxuhJT0G116V81lPOsdlpxb76nIoJHM9AK-QbmVSbgJNWbuLmaRLox8bqiaz9beAHUzf0MJyPz1Lw6YUBj1wDhGo7hFIf13Y_dFMXQBqORekQRPwgGp-ZmfZo930suzK3jyRvJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494ff796bb.mp4?token=F-5OufYh3seaMXU6QsuXqbDV2oCyHhk_0OzPpvboK4F0lfqwfk9kt-b_QPnV97QrabR9KDwzmgcymEmJh2egEmVK9L0EfUxklXfIrGOcpoG8KEaJdhizDJizQgSHI6KB_LDLRhALgkWaIvmti9ZBhKLF5IJGpYpzu9rWSVXxtMOvp_C-ivn757hnDFEM4Na9cU4G0XlQbmuF4slzxuhJT0G116V81lPOsdlpxb76nIoJHM9AK-QbmVSbgJNWbuLmaRLox8bqiaz9beAHUzf0MJyPz1Lw6YUBj1wDhGo7hFIf13Y_dFMXQBqORekQRPwgGp-ZmfZo930suzK3jyRvJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم اسپانیا به انگلیس توسط اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107343" target="_blank">📅 23:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107342">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اویارزابالللللل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107342" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107341">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلگلگلگلگلگ سوم اسپانیا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107341" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107340">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0a10c6d7.mp4?token=DhyFmvRYipv16bY1ciNQW62sK1skXW7L2LnEw3LYvtWhWUXnfw_0Rbvdb10HYh0aiclH2N7qYrUQ4MbwkzJ7Y9iGcRsEwEub8ahb24WvcI9TAaHXcEOFEzoq1cvqm-6ZIUrzCesjKMtxTi6iFXVmvogmMxiIvenZeDMuw5B8sEdkHiORhY88YOrD7zNY5xrnDJcDdbDijsljz3aemBv9sA4QFaECKUcpHGUHwMpiy0n5AQxojuTxh57YuCMlbPJoNFie9L4thvoh_nKkwNZpUtPXrDi1nQS-UuGJvWF9H8kIOgg5GMYGSyfzzRSKaQUqiLuGfLgyRaYG6tHBrbfxIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0a10c6d7.mp4?token=DhyFmvRYipv16bY1ciNQW62sK1skXW7L2LnEw3LYvtWhWUXnfw_0Rbvdb10HYh0aiclH2N7qYrUQ4MbwkzJ7Y9iGcRsEwEub8ahb24WvcI9TAaHXcEOFEzoq1cvqm-6ZIUrzCesjKMtxTi6iFXVmvogmMxiIvenZeDMuw5B8sEdkHiORhY88YOrD7zNY5xrnDJcDdbDijsljz3aemBv9sA4QFaECKUcpHGUHwMpiy0n5AQxojuTxh57YuCMlbPJoNFie9L4thvoh_nKkwNZpUtPXrDi1nQS-UuGJvWF9H8kIOgg5GMYGSyfzzRSKaQUqiLuGfLgyRaYG6tHBrbfxIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی اسپانیا توسط الکس بائنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107340" target="_blank">📅 23:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107339">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed28ae0d69.mp4?token=T-A19b9dxfXr8UoPZewfMgXBzmB4y0xFktUkkCxMZb5OYPJA0t30S7T7GIyXX8nVrSYEQpjRCUw9H2Jajfa2wdS3p9zd-6I0isc_8sGZox7ZxUXQnxhTeysa1CFcNgRkMNy9zTdAHXrE9Js3coaHefUGB-Fyra4DjaEedTBSQMW9QqCTG5FpZswhGr3Xp8OQgkxKMY8OS9huFfuUD7HAWJZIkzD8TDUAl4vtDPfYTbn3rTZS1A2XOjtnjwBAngwWCD7_2CTMADy9MvEp30jc4JsS-Tx7I3wHwZhNMumfdYFF9Io_Gdse_eo1jOwUsPT08FJeIF0DNuAtoGc3UxdwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed28ae0d69.mp4?token=T-A19b9dxfXr8UoPZewfMgXBzmB4y0xFktUkkCxMZb5OYPJA0t30S7T7GIyXX8nVrSYEQpjRCUw9H2Jajfa2wdS3p9zd-6I0isc_8sGZox7ZxUXQnxhTeysa1CFcNgRkMNy9zTdAHXrE9Js3coaHefUGB-Fyra4DjaEedTBSQMW9QqCTG5FpZswhGr3Xp8OQgkxKMY8OS9huFfuUD7HAWJZIkzD8TDUAl4vtDPfYTbn3rTZS1A2XOjtnjwBAngwWCD7_2CTMADy9MvEp30jc4JsS-Tx7I3wHwZhNMumfdYFF9Io_Gdse_eo1jOwUsPT08FJeIF0DNuAtoGc3UxdwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به اسپانیا با گل بخودی کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107339" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107338">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8bcae065f2.mp4?token=r8DkNYJkrCEhPkdR-yZRyJNbwzL4cT1rGuXTdYkRw_OAdVA9bADNRx1Xm3Aq96cbyvDALXl7o3mhIYRyJzUsKVuXvANxMEdftIR9roVLSzX_uba4ADLqiPbIKrIXbxiH_kjeC3thch_WkJFMatIXGsjPOsNPdH914vNalD6PVQzqjEinBcF5oP6ghqcdl02XXhL1YQrNsupGNP3C0v_WaCSJWWcbA5F8XMMQX-aKuhwNrjnFFgwFQPogcO0AO6NxYuviPAVqEgDM8M4n31yHA5meib85DC7rHZxqKqgz1FJnxe6Bp4hoUux4QkdMz2YSi_09hQAc2Y3AbvNaU7LAHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8bcae065f2.mp4?token=r8DkNYJkrCEhPkdR-yZRyJNbwzL4cT1rGuXTdYkRw_OAdVA9bADNRx1Xm3Aq96cbyvDALXl7o3mhIYRyJzUsKVuXvANxMEdftIR9roVLSzX_uba4ADLqiPbIKrIXbxiH_kjeC3thch_WkJFMatIXGsjPOsNPdH914vNalD6PVQzqjEinBcF5oP6ghqcdl02XXhL1YQrNsupGNP3C0v_WaCSJWWcbA5F8XMMQX-aKuhwNrjnFFgwFQPogcO0AO6NxYuviPAVqEgDM8M4n31yHA5meib85DC7rHZxqKqgz1FJnxe6Bp4hoUux4QkdMz2YSi_09hQAc2Y3AbvNaU7LAHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول انگلیس به اسپانیا توسط گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107338" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107337">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107337" target="_blank">📅 22:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107336">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=r3bIiPlTKB3QR6B8gzVEuHRRWH_d8TtfvRnnmMGf3XqfZ5BUwozKzgqbl16rKyM3l0O41u30YmO4qqwlR2NqA9sEtzTvYVuQQmcaWY5oz_Dr8pdW-yNvR4dCmvORsg9qA9BAr9CcwN8z1FFqw2lTX-y269S_9AmlwLtm3fKpgt01tZURih64PfQHojAtatVUzXzpHCpLwexD2hDmQfruXJ0oPGDHa4Mb9fSVbBowEYKlLaFIHpTEq8c9T20zzyw1Zg0dq3f7n7o21iWhwYqgazN4WKIHhjdYiKiVAVA9WznF9UBmPm0whfXsRJVMIl1dfSuhXvzR9ke96du9V_8fZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=r3bIiPlTKB3QR6B8gzVEuHRRWH_d8TtfvRnnmMGf3XqfZ5BUwozKzgqbl16rKyM3l0O41u30YmO4qqwlR2NqA9sEtzTvYVuQQmcaWY5oz_Dr8pdW-yNvR4dCmvORsg9qA9BAr9CcwN8z1FFqw2lTX-y269S_9AmlwLtm3fKpgt01tZURih64PfQHojAtatVUzXzpHCpLwexD2hDmQfruXJ0oPGDHa4Mb9fSVbBowEYKlLaFIHpTEq8c9T20zzyw1Zg0dq3f7n7o21iWhwYqgazN4WKIHhjdYiKiVAVA9WznF9UBmPm0whfXsRJVMIl1dfSuhXvzR9ke96du9V_8fZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول اسپانیا به انگلیس توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107336" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107335">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسپانیا ییککککککککک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107335" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107334">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لامین‌یامال زددددددد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107334" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107333">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107333" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107332">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXZnFTzROBVzBxPNVGdeDUeUrfVS87nwQSQCWRxVbvV-oIS73ito-zz149H_E6Pwnb8GwIa8vsSEMkvUF9NCu0Yd5jCU8CBpjnVslRELyQtb5IoO-vwzjPibIQBpn5j90WH33uj0Q-kqF4HjGkfwHTXSK1hcVjekW3FiuA5KZaEBKE4FfacqAZaDfbQkkhA8y8aaGEZYFqDEIlJfpZlaTR2MEEw3kfTg4pQzyIB8S9_BNeqCNcr1y-M_wMClO2BYOnlutEooZo-K2d62OhFp1EZqSYh6E-9TxjkpF5dVRcrjTyKVabJxJDfBlN_ZHDZuADbYeqw2GY1UY5kAfJYpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107332" target="_blank">📅 22:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107331">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇮🇷
تاجرنیا مدیرعامل استقلال: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا میگویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107331" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107330">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbjqjTxwOgaax8pfMrGRUvXGY2S3kjxUg-Mvyw6Dv-1qd8yJs8sbtQF5DzlWTOixn5fte_SRjaIL6HFPbzLYGHFUUnCbzM2UV6Dd-1aGncxy7MD-ColG49FrsQu3g5s8kx5EKzwXpDfzVfHInY3C4ENyPPqWAUG3JWf1SLBu7NmhkxVK1bX34xprU_S5i5G0d604jPzEnWlFUOYxJOoo_8oYTNXK54IcH4NBDFWGeYLHqpuPVOD4Hn6f6-nDHx1Xu-evdOYS5lpYSBP1Jm6lfWvWopubTyWatzTSUrv_wsPEanTLcyo09YXCc27iVJ4Ja6cpHj74QYyBFh4tzF1TMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107330" target="_blank">📅 21:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107329">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jny2-6-2HnNxpDVRbX98MykqtAUdOXf2zHZQ1VgHua6pNkNtp8gpMoy6y676omo8KWpDdbcordcOhG0AYRzIW1LKdf52kX_C6n7zw1apIRvTqkxykQusg7F9fTDaa6hhowjBuqPTEF-Xh9M_Wm6GAAhAKzmpG-dueRCPGVl1siJ7cz0yAcvttqG-wJeTQ_IbBYhg2XID98qxKnZYphX0hJrEFjxfEYPdpGeT2PCzhfTjOfoZ7XnRfJuwpzNHUZ5Cww2hKpZcOHxlotHGFdYlJa4BKY87c_1bqGAcpq7dUF1lZya52DN4hnkRvlmEI7tvtLWkAgXp3RY-qS9BMo1-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آمار تقابل‌های بین انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107329" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107328">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVlRcpzfr9p4toQJlk5-Pll1l9XR_mh2WswGZzW_7FKUy8g6vktjIQxBZD1HaDa8SYpSKv6h8CNrvnkCQvj0ayH8gK43MQhYptax-opuq_clhtixIMAQP1MbUu1VHk1EG2DGS9mStoU7NE6ykCP6JOYzubATtgVGoNPIkzVFEZNuqQLiFvniWgazIlR1cUnNxPqyTYOxj5kQ43Y4z0L6G7gYYIl7ENMNpXScF6_1NqtmSlOS26KM98tit22kMUG-x5DaH1cm_HhRnRPGmFH-eVgNzs8SIYdJCNB4U6deqW0o-JwQUGMeNu9ryhmAHo_-vXNHP-ZCiqJixJLb98UiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107328" target="_blank">📅 20:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107327">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/591cd9489f.mp4?token=cRMt2cOpwd264Kael26Ir3VQNSppy1C3m7CgRfB0QETWX2BQvu9DKfqdIqnpuXBMJI0LQ99qGc60XBDN848hlgNazSMqsZNcPdvGJkjxSzDTEwj2zVpM5spuUgGrbgp92se2sFaoybHXK7DgYPMgZFlekpPjXnRyid_RDwiLyzSUa-2UVf9LgyN7y3jb2IP40e7il4giRGTGM51b0dXu-mi52vTVptSmJ9rqL8pv6IeM3pMq1MEyV7UOgOagcgsui9-rdI0FUuXB_-7vG8MVAixko00oNC-pxkf0o_GyHY5FJC8FYMQ0060kkIGBjAFLf5wOCwO0SRYt0cKLo8s6gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/591cd9489f.mp4?token=cRMt2cOpwd264Kael26Ir3VQNSppy1C3m7CgRfB0QETWX2BQvu9DKfqdIqnpuXBMJI0LQ99qGc60XBDN848hlgNazSMqsZNcPdvGJkjxSzDTEwj2zVpM5spuUgGrbgp92se2sFaoybHXK7DgYPMgZFlekpPjXnRyid_RDwiLyzSUa-2UVf9LgyN7y3jb2IP40e7il4giRGTGM51b0dXu-mi52vTVptSmJ9rqL8pv6IeM3pMq1MEyV7UOgOagcgsui9-rdI0FUuXB_-7vG8MVAixko00oNC-pxkf0o_GyHY5FJC8FYMQ0060kkIGBjAFLf5wOCwO0SRYt0cKLo8s6gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
توصیه عادل به بچه های کنکوری
😮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107324">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6482y70qTC_t1r1sI8vneG7PFhCOrTfmdEcH-y_eY4rpdIug9Sv5Vo0vnX8RhUr3rVVh3TtWO8D0gPRgopqII1JfuAb15mX2zHEMfDPkyswlZjjYUIt8PQmMtQUvU35P8XzuYs27p3JmooaENiKTMjETUn8jlCbK8F7AGFSNee00fnYZ7BD0iJ2KQFaE2gC-SKq7Wqm3T-tv3X_IEKQjqzaK075LKUt-Vj4OmMXroyqrYnKYaXDHWEmCwcqq8gVDMjZ8pkHlROnkjr5_dM9ng5WDPPMrwSOphEyQKeXWC7GY7BNzeOdADiW8EfRACIGp9dozUv-q-5_tOpx2hHFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👤
علیرضا دبیر: چطور مهدی مهدوی‌کیا با یک گل به آمریکا از سربازی معاف می‌شود؟ حالا هم علیرضا بیرانوند بخاطر مهار پنالتی رونالدو باید از خدمت سربازی معاف شود و هرکاری از دستم بر بیاید برایش انجام خواهد داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107323">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=eTz5IHcpi6OgnxJJDMlh4PYldNUH0ZQleSZ3Bk11OyMU60CQiEXPNkda0MKat5B4bbVljVwlbvcqZXBVaA-HX5Loe-rYHbCcHBMKM3AoLAcbQXXHmWrmnxZ-6BSUECSytKDD9diDnHndMN9v2QvDi6IQM9LriG4Bw585OGTF3daxolL0dIx3xojGS8hxsncnDfnx8tzDpwRQFxPwsWEzC2Tuk7qhmRbTu2MY---lO7dFNlQXRB4k6OmULyqzXC1akPRnarpHP15QiEe67QS--7uHIA2ZDgodAAHtJ06fI7-RlH14uJ0erKsVolzt6egEVHJ0pDrHDwsf5mIISdrKhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=eTz5IHcpi6OgnxJJDMlh4PYldNUH0ZQleSZ3Bk11OyMU60CQiEXPNkda0MKat5B4bbVljVwlbvcqZXBVaA-HX5Loe-rYHbCcHBMKM3AoLAcbQXXHmWrmnxZ-6BSUECSytKDD9diDnHndMN9v2QvDi6IQM9LriG4Bw585OGTF3daxolL0dIx3xojGS8hxsncnDfnx8tzDpwRQFxPwsWEzC2Tuk7qhmRbTu2MY---lO7dFNlQXRB4k6OmULyqzXC1akPRnarpHP15QiEe67QS--7uHIA2ZDgodAAHtJ06fI7-RlH14uJ0erKsVolzt6egEVHJ0pDrHDwsf5mIISdrKhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
عصبانیت‌شدید یاسرجلالی آنالیزور فوتبال از وضعیت وخیم تیم‌ملی با قلعه‌نویی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107323" target="_blank">📅 20:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107322">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🇪🇸
بعد از تست‌های پزشکی مشخص شد که کیلیان‌امباپه حدود دو هفته از میادین دور خواهد بود و مشکل خاصی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107322" target="_blank">📅 20:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107321">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=dbFdYdA7Ca9qm3iM2LmgS3mu22jCPF-E6GUlQx7nRfEZC66oaeik8txj9IqF0M47pl1uGwVIX-qA9hOg8aVtufs6h1_WGPXABOVhUVngEIunmVJiYL0QxnH4bqlwcTnff5TrN41o_cDu_42nywiVKqcA0LPM1FuFGYn3kkNfKOhmjMwRrkAxdY8Kryh7AwWxPw3fTziX2tSjZexp221dHzIZHmCVp2m7UIPTZkyhFEt0l14s99mJXx41f-wQBuGvZjrebNh4YrYhQ4tfefdVrh55Nzmn3YwTOZjPdkqUfi1y6aIdCC7wCFjxKD0GYgUHe7XBZo3AiqmTFlcXNdoPKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=dbFdYdA7Ca9qm3iM2LmgS3mu22jCPF-E6GUlQx7nRfEZC66oaeik8txj9IqF0M47pl1uGwVIX-qA9hOg8aVtufs6h1_WGPXABOVhUVngEIunmVJiYL0QxnH4bqlwcTnff5TrN41o_cDu_42nywiVKqcA0LPM1FuFGYn3kkNfKOhmjMwRrkAxdY8Kryh7AwWxPw3fTziX2tSjZexp221dHzIZHmCVp2m7UIPTZkyhFEt0l14s99mJXx41f-wQBuGvZjrebNh4YrYhQ4tfefdVrh55Nzmn3YwTOZjPdkqUfi1y6aIdCC7wCFjxKD0GYgUHe7XBZo3AiqmTFlcXNdoPKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تو مسابقات کبدی بانوان در ناگویا، کاپیتان ایران حریف رو گرفت عین گوسفند پرت کرد اونور :))
بعدش خودشم زد تو سرش بابت حرکتش
😂
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107321" target="_blank">📅 20:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107320">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=pvANh51r-U8zCwaTruwL5I8cu6ecJl1s8XLqP1mz4L8N964v7bfd93Rr5whKqrD4c7KXxBRCUDv8DzGzv75OCgnuW26BJdOy6v4TOoiSkeuvWgWuWZeI-1rQVKM1IkGPgxwPLHxNI8VqaFcI4RAFrYB3kYC-bWr5N_WbG76xxJZm4lG6Mop7sSX9qN5bVL9zRb7pxIv7a8AEWw8q5FNrca8KNjEWOaG9HNiXCg_fTKdK5EEJNy9qo4SBPsGxV6KYk5KkslPRl1DPuOVU_HUX40oQMI-6CIrsrHA7poMseYqX7aMx-_rmg7f1qV2r08d88Ox0mwXPWnOBgSJ7212fPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=pvANh51r-U8zCwaTruwL5I8cu6ecJl1s8XLqP1mz4L8N964v7bfd93Rr5whKqrD4c7KXxBRCUDv8DzGzv75OCgnuW26BJdOy6v4TOoiSkeuvWgWuWZeI-1rQVKM1IkGPgxwPLHxNI8VqaFcI4RAFrYB3kYC-bWr5N_WbG76xxJZm4lG6Mop7sSX9qN5bVL9zRb7pxIv7a8AEWw8q5FNrca8KNjEWOaG9HNiXCg_fTKdK5EEJNy9qo4SBPsGxV6KYk5KkslPRl1DPuOVU_HUX40oQMI-6CIrsrHA7poMseYqX7aMx-_rmg7f1qV2r08d88Ox0mwXPWnOBgSJ7212fPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
حمید مطهری سرمربی فولاد خوزستان: دوست دارم یاسر آسانی بازیکن من باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107320" target="_blank">📅 19:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107319">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=s1HUFdqsOncnQANK3W_u34LUbMIjXfSjIWuuPsqzvUEK_U7KibZ_HOVs-p2OSh1cDFjSJrG8bDsY3VzlhZA3yhyWsR8kFV0PpMLNfUkDIgJF9KIbdZ9Boc7whB7Dp-z3gJBVDVJy_tFJ1o0_vWOlfj9_tn9ctT1mwsRijXe6gGGiWb8nXPJoAyt6-GjweJQVAoMpGuqbl15jojJxYplgMfbot-XJ9ttmP5MrFOZXXYdrIv9Mc7SdKeY5N7N44FWqosec5AR2yhKdmEbOV04VJ88SrG8e36IuS1Li6PCN3rjammGLT1RA6NLp0JU9iHRvJWAQ65a6v1qF8aH8pFkN7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=s1HUFdqsOncnQANK3W_u34LUbMIjXfSjIWuuPsqzvUEK_U7KibZ_HOVs-p2OSh1cDFjSJrG8bDsY3VzlhZA3yhyWsR8kFV0PpMLNfUkDIgJF9KIbdZ9Boc7whB7Dp-z3gJBVDVJy_tFJ1o0_vWOlfj9_tn9ctT1mwsRijXe6gGGiWb8nXPJoAyt6-GjweJQVAoMpGuqbl15jojJxYplgMfbot-XJ9ttmP5MrFOZXXYdrIv9Mc7SdKeY5N7N44FWqosec5AR2yhKdmEbOV04VJ88SrG8e36IuS1Li6PCN3rjammGLT1RA6NLp0JU9iHRvJWAQ65a6v1qF8aH8pFkN7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇧🇷
عصبانیت رافینیا بدلیل عملکرد ضعیف وینیسیوس در بازی مقابل استرالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107319" target="_blank">📅 19:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107318">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5Wmza4hkyD3TLgxyZQJ7FoFrI-K0VzHB-9ZOdTKd6WzlAIjFUjfxohTW4XcU-vuxztK9DKXWJoC_xWsBIYSrr2g6T_HWtES3f3mowj8Kluvrn85r3j3WfKDWnh_WKu8I6qBnjaovqVj-rowEeGSCjrJyC0dBYjpV6_FJ0HfoPvW11Nm6Tf_BIMXc5gFK4M6WLDrytPtk8MAoAyNfum5Pm4gVS4EN8Ynx_NMjAJMwB1xg028OP-Zt9ToLhc-lJiXW8jxe0nahgbOlG0xhFgV4pSUHlJepeKB3bLS1birX-FAqTFIxkgTHbgdTJO_Vo0d5yuLF6liqJg_C600q1EUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پیام‌تبریک مالک باشگاه استقلال به مناسبت سالگرد تاسیس آبی‌پوشان پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107318" target="_blank">📅 19:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107317">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMNWQX-ndtYYL19vpfubYeQHlBwIuM_aqR1JWR3HOSMoaoOrCnCxQh1yFLW-8zxb4jTRhKKi78PAEGb94uKs6TMx9fFhtm8pXHtzjcglRMNR8fWAaIDqrOopqnUEcZhuIIAkt1JPaZ6gvNYpVpDk3X6_QwNWGNZ9cZI-xYgp8r_MimvkeJEEch1zIQanewSqpqUnvJWO6Nv_ZuYkX01NU9VrHz6H-zpkcgNiLIPcwFJMUw58CH_7tzx1KnUhhOsKhgdbCvCiRJMMFZNe-RxZH99y_F0rEmxCoDlp4f2hzfYTtEAjFF__S4_N94TwsbOeKpnu26HReVGFp1b6-ba00A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چند روز پیش موقع آغاز سال تحصیلی تو تهران، تو یه مهدکودک مربی از بچه ها پرسید شغل باباتون چیه یه پسر ۶ ساله برای اینکه جلوی بقیه بچه ها لاتی پر کنه بلند شد گفت بابام سرقت می‌کنه تو خونمون اسلحه ام داریم
🔻
مربی میره به پلیس میگه پلیس میریزه تو خونه این پسر بچه میبینه چندین اسلحه تو خونه دارن و پدر این بچه، رئیس یک باند سرقت مسلحانه از منازل مسکونیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107317" target="_blank">📅 19:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107316">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgxtGhdeKv00AgbiKN1fiYcaITRdjYf6ERA7OqXFAY3RAiWdCA2sEGaI37Urb4rrTngIeqEgP6bpzcyZMj21_7qCpk8_8nVBvTL5ozSKmi52RJCFTjSFtWMJ0gAYcTE5_nvtzhkHclUYSj0mhP3unHWh5u432H36y4Eov_rwGu5rcwMZvPq13xmW0m-3YYGdy-FRxcfqNjU4wG4yNr88dbmxtXWUTGXwXmVqb8IVyh4EA4uO4E2WhDS8QqN5-H1mesfOILbNl0qYT43FcqPhizmuuJ2UgQ3mr1KIy-lEhgJI_3ZvyWubTAYio5784XeYfDi2i1BY6ampSWzU0yx1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
تیم منتخب انگلیس و اسپانیا از دید هو اسکورد به بهانه بازی حساس و دیدنی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107316" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107313">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=hMDdNCchLMXPZ_5HnRSQkVmQwYxeaL2zn4CiWBFcjvFVB4POu_bn6pVXU_On1r6B3hUe2sKQiKql6tsJY1bsCehvrprZ_OGjCk-r9dGWpgYEAOB_BcvGd6OWQsRQtZJhYk_tctRayhiTlf_K5sLs7ivzj5Fmw4WtCRpLwqR8mOMXqlQTKmcrzpUAtHNDhvAy6CP8_7UUPqhjP618tLX3ZiGgOBirfeMv9exfOS7Lx9mE6n176y7IY8xuFfY-9VRC73MpNa33vq0ovj9s703ZFRAr6-BQ6fAyVKokVkVFSSbF5yjNaIPOQvYAkOtY6Lqph3zuV9XyHRq-6csH4s6hzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=hMDdNCchLMXPZ_5HnRSQkVmQwYxeaL2zn4CiWBFcjvFVB4POu_bn6pVXU_On1r6B3hUe2sKQiKql6tsJY1bsCehvrprZ_OGjCk-r9dGWpgYEAOB_BcvGd6OWQsRQtZJhYk_tctRayhiTlf_K5sLs7ivzj5Fmw4WtCRpLwqR8mOMXqlQTKmcrzpUAtHNDhvAy6CP8_7UUPqhjP618tLX3ZiGgOBirfeMv9exfOS7Lx9mE6n176y7IY8xuFfY-9VRC73MpNa33vq0ovj9s703ZFRAr6-BQ6fAyVKokVkVFSSbF5yjNaIPOQvYAkOtY6Lqph3zuV9XyHRq-6csH4s6hzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
گزارش جالب توجه گزارشگر مهمترین مسابقه هفته دوم لیگ زنان بین استقلال و خاتون‌بم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107313" target="_blank">📅 18:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107312">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me7_G4VEEWklPfuuMnm74-u-TZtCahXCvHPDnwkmTH1mxd_TcfTK5qSjkyNKUrGES8kvyqb1s4tBgSR4nc7i2SmfazEoRnYXhwHyGI0gzqWXKsfb0_z2m2QE2GvZ-DWP2yFajmejhQrUi0PkN2J1t-07QY-BoDVTKfWfez7RcvikjWDB9FfSPlBVLgBccmCOEA7XAOfb_UQ2CWR3FKyrAl5HOTf3Q2Gp6Nu6bLJUna16jcK4A-EYvwmKEVi5NfFFS7hsidUCX1w0a6-GFXybQ8TxTaad3qc_PFc8M0yEqJCC0_XSu_V4ueL3SH0XAtXy7zSM0OH3Qvc5IFjhDdXduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودری ستاره سابق سیتیزن‌ها: آنچه ما در این سال‌ها انجام دادیم قابل سلب کردن نیست. قدرت و سیطره تاریخی سیتی در لیگ‌‌برتر هرگز با رای دادگاه از بین نخواهد رفت و قهرمانی‌هایی که کسب کردیم در عین شایستگی بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107312" target="_blank">📅 18:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107311">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2v62iw5pYo0jz-TVVZVw1411K-6YkoV4la4Dy0HXt1k2-2Zf1-VB_Nko2tlJzhcl8_eEP_W8C5pyiSjCR0NTtQ6HapP4ePiCXp4EdlN57GMrv_ouV2WIhBBGj4A0pwsoVS9L52QTh1bFeCZwWgO0aEu7bz4uIlNwTKiv8RZhBL3LpAv3qMaFefPQTXy5h7hL9fsnnmKL05BQKgxm7KHQs4COl4r5sytbssyPejsmskjmhKHA_UpQAy57vLjNSU_1rL1Toqk06qM3mQsYKj6EV1_bHPJ2ySEh8PKxS1QUq570J8lEG1nQy92mgHvmbmyW-ZEt_z3_SopmNEQaZZaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
لامین یامال ستاره بارسلونا:
🔻
من برای پول فوتبال بازی نمی‌کنم، چون دوستش دارم بازی می‌کنم!
🔻
بازیکنانی که وسواس گل زدن یا پاس گل دادن دارن از بازی لذت نمی‌برن.
🔻
من برای خوشگذرونی بازی می‌کنم؛ برای دریبل زدن، برای بازی با یک یا دو ضربه، برای اینکه به هم‌تیمی‌ای که هنوز گلی نزده کمک کنم تا گل بزنه؛ من برای شادی بازی می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107311" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107310">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
⭕️
⭕️
🇺🇸
ترامپ: پیشنهاد ۷ بندی ایران را رد کرده و اصلا مورد پسندم نیست
🔻
ایران خواهان توافق است و من هم از توافق خوشم می‌آید، اما این پیشنهاد غیرقابل قبول است. ایران خواهان بازگشایی فوری تنگه هرمز است زیرا متحمل خسارات سنگینی شده است. من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم زیرا متحمل ضررهای بزرگی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107310" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107309">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YB2WoENNcA8Kafn5hUVacSM8j6HmzIOTyOd_-tQl3rzREo16SF0N-CLWiFNAHAaYk4W9sNiWQbIP3GAmdeaakVHilSuL6g8QjqMNd6XJAqAk6-vKxojOuoWVhNPp5bQKMOqQlQ5swasyU9YTn5qiCcXwEZXZLDGvDwKshAZFUu3COUob1C0P_KpH7nPuMGxbw39j615Nzn6LXxBSceUx_hChWBskzPSWky0Prm-oxWtXG67sAAVkl4GIJD1iIp_rKBGb2lXB_id0qcyrsk6ruYAC1rCSsUMhuLQpSKjtL7YNDVPE7HmVNf94ckMy6ShXs0qKGfFBrdauWwUHz9HYRwxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YB2WoENNcA8Kafn5hUVacSM8j6HmzIOTyOd_-tQl3rzREo16SF0N-CLWiFNAHAaYk4W9sNiWQbIP3GAmdeaakVHilSuL6g8QjqMNd6XJAqAk6-vKxojOuoWVhNPp5bQKMOqQlQ5swasyU9YTn5qiCcXwEZXZLDGvDwKshAZFUu3COUob1C0P_KpH7nPuMGxbw39j615Nzn6LXxBSceUx_hChWBskzPSWky0Prm-oxWtXG67sAAVkl4GIJD1iIp_rKBGb2lXB_id0qcyrsk6ruYAC1rCSsUMhuLQpSKjtL7YNDVPE7HmVNf94ckMy6ShXs0qKGfFBrdauWwUHz9HYRwxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از روزی که رونالدو نتونست مثل قبل بدوه و هتریک کنه، موتور تیم ملی پرتغال از کار افتاد!⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107309" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=gH3a5U4FYB9GFsFpGT4KEQzITdWF9GlziKGSMeE6M7iYEcOKaiF2XEHJwJNqkK9S-AHHeUHV692moGkOuJUk8NLHx3j56s9--aaOHVZ9CSOlUiQ1iACGsfJ7muTncluFGpqdhdDtfHQfybH9JBnVdzVQRY2S4WClq991pHpqwFfcppDL37rjWjlN8gXPkxnkkMgAGh-xCcdTFHBFvDD_ZEl-qm08D9TfQSknyu1L_SgHN_6qfRNuLMbOE66WF_afIgmTFDS4Wa8ukxosPOymK5CvnYr6GDqx0cNBrXEP6h6huDPTKKb5wBp5BOqNd4sb6FeNaTP-Uz_WoyqmIWbN9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=gH3a5U4FYB9GFsFpGT4KEQzITdWF9GlziKGSMeE6M7iYEcOKaiF2XEHJwJNqkK9S-AHHeUHV692moGkOuJUk8NLHx3j56s9--aaOHVZ9CSOlUiQ1iACGsfJ7muTncluFGpqdhdDtfHQfybH9JBnVdzVQRY2S4WClq991pHpqwFfcppDL37rjWjlN8gXPkxnkkMgAGh-xCcdTFHBFvDD_ZEl-qm08D9TfQSknyu1L_SgHN_6qfRNuLMbOE66WF_afIgmTFDS4Wa8ukxosPOymK5CvnYr6GDqx0cNBrXEP6h6huDPTKKb5wBp5BOqNd4sb6FeNaTP-Uz_WoyqmIWbN9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ابراهیم‌شکوری دستیار حسین‌عبدی بعد حذف از آسیا، از ژاپن برای خودش آیفون ۱۸ آورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107308" target="_blank">📅 16:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107307">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275c393efd.mp4?token=SLp24AD_-x9h9iuqBqc0IDZbqxc5b2_XrYxCq5xqRJiThpUoGJeufrikev_KmTbB3x7549SJZBi6Nm3CnUuLEtyldxuieLPgmIL6--xhELquruwmkx4Ym145TD6DDm_fJkREEo1xCTLA7T_kWw5pg_GkkqtPSIbyWoonRZdP4zSADTcD9rlWmpmdpkpUoLP2TRn6u31tG_Oa9xceIfHGdY5J6QPk6gwfzEwWPHg3P8PfAQO2CqufUyAreRd4MpJLaJxrFLvLmB63-GqWCqN_6bf4p201cRbIVA2U9lNTMhEqkYgrAn-XplS3kHj5Wd4nstCe0c0JnYIYOfY-0XDfyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275c393efd.mp4?token=SLp24AD_-x9h9iuqBqc0IDZbqxc5b2_XrYxCq5xqRJiThpUoGJeufrikev_KmTbB3x7549SJZBi6Nm3CnUuLEtyldxuieLPgmIL6--xhELquruwmkx4Ym145TD6DDm_fJkREEo1xCTLA7T_kWw5pg_GkkqtPSIbyWoonRZdP4zSADTcD9rlWmpmdpkpUoLP2TRn6u31tG_Oa9xceIfHGdY5J6QPk6gwfzEwWPHg3P8PfAQO2CqufUyAreRd4MpJLaJxrFLvLmB63-GqWCqN_6bf4p201cRbIVA2U9lNTMhEqkYgrAn-XplS3kHj5Wd4nstCe0c0JnYIYOfY-0XDfyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❌
آنجلوتی بازهم به رافینیا استراحت نداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107307" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107306">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXdRaZ2L42emCUmRFI21PuU1HBNmMkAP-II3GoALVuM4odg_tUsIPB7rdjkq6BWVgTx0jeFfDRLWCdecT5-him5blhyM5MD7MidS6yb-WTNlSdSXv8mu01GM7JPu-byRyeTTRL8j-OdIAmqE6f3KtOS8YT6pNsllJ5SvsVjdXITwI6ziW58NyUnZmcW_ydbaX8s67BITuX2mStbXHI1-eSeZrsOtXY2rr6hrrh-uIu-dtoJ8xMPODaMmn1RwxOUrJzOIXbRMlA1dPKSDxRboMd7vLrGHbKTb1XURSUNSLiyhJXQIws2X9JI7azuA8XOnvdjyCJZCZ0SCcwi8x-7DqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
🇮🇪
چند بازیکن تیم‌ملی ایرلند از بازی مقابل اسرائیل انصراف دادن و گفتن که مقابل این کشور بازی نمیکنن. در صورتی که این اعتصاب گسترده‌تر بشه و ایرلند وارد زمین نشه، اسرائیل برنده بازی معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107306" target="_blank">📅 16:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=Jo-a4lAXql3WY4QNLmvYahIMPuDSqQVrdMDKBq8OpvlchyNaeH9cJF5YR7scpox-hjA1lc2uvlDV3PbIpdk5oPRbAVfVSPg_T6vUWoLWP8Oa3Y982X7DXAXOsLxOSxKlFtTbeci--16Gj4ia8gIVGca_0voL-dihnGF5yTbrnFXcSGn-cA1J86PkPzKpt3w5yUNhe9rbTXreZ96iZazj1za6bbfU4qvi4S77JS_aYmIs-tNtGA5XBei2FE_nqviAoaKWkmQv-1lZ-HCojMFnvm6erGPhA0sU0dWv50I5ygv5YZVnUtcAGlUlrMvbaFXCVbXSV2RK01XHgXedlb83f6ojlYeKU5l6SWvCUTyl4ZrdiBHmoZmsK4crklIu96z53OqFBLQj1eDYl8xXtuMAcTRKc8SEUpmVu7G32Qy-eHxrYBleZpDLDqvQS87ox1g1WTFIMp83uj2gxfw0-qYU-fpS93EaoTWmPohztxnlNqb7W_u9mtHnVvM5c9aCEBa3ypURGjy9nv27keWq3GAtoovkJ5kYA9V97Cwf2HRiEnABVZU-P6S2vtN6j0lc5isC5YhoSLFYywYjjK9glhJmOZjdoCgqfDXutKjp4VIFm6zVlaSGiptV1O-4O6Cw7u2Xcaim3MdbhcS5-Ikkgmc5iDYKPa-rUPp6dpJUJM6BDtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=Jo-a4lAXql3WY4QNLmvYahIMPuDSqQVrdMDKBq8OpvlchyNaeH9cJF5YR7scpox-hjA1lc2uvlDV3PbIpdk5oPRbAVfVSPg_T6vUWoLWP8Oa3Y982X7DXAXOsLxOSxKlFtTbeci--16Gj4ia8gIVGca_0voL-dihnGF5yTbrnFXcSGn-cA1J86PkPzKpt3w5yUNhe9rbTXreZ96iZazj1za6bbfU4qvi4S77JS_aYmIs-tNtGA5XBei2FE_nqviAoaKWkmQv-1lZ-HCojMFnvm6erGPhA0sU0dWv50I5ygv5YZVnUtcAGlUlrMvbaFXCVbXSV2RK01XHgXedlb83f6ojlYeKU5l6SWvCUTyl4ZrdiBHmoZmsK4crklIu96z53OqFBLQj1eDYl8xXtuMAcTRKc8SEUpmVu7G32Qy-eHxrYBleZpDLDqvQS87ox1g1WTFIMp83uj2gxfw0-qYU-fpS93EaoTWmPohztxnlNqb7W_u9mtHnVvM5c9aCEBa3ypURGjy9nv27keWq3GAtoovkJ5kYA9V97Cwf2HRiEnABVZU-P6S2vtN6j0lc5isC5YhoSLFYywYjjK9glhJmOZjdoCgqfDXutKjp4VIFm6zVlaSGiptV1O-4O6Cw7u2Xcaim3MdbhcS5-Ikkgmc5iDYKPa-rUPp6dpJUJM6BDtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107305" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107304">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=F2ukqOhSL2SU0EvtqsQy5BqUnwJctrRhv-ad-Na-B8GUQIe9_BVi4fqlBKCvlBLLuRGVg9wfyp0SUWohLInh0s8NazwC67Fzdp-i3xK357fvJNLSpA7lOi13wl31sjpoCNhVe4VMHcsP1qsAtA-rFQeeDbmUrADT3BJsX71YT9r2N1oAivkH8arC8gKXtgRRjCohJFEE6d9wMogKrLe3-cFF2vuCrY8U2bOeAURsQv4pZC7pT3bI-KxkpoLo6mHMai4y1rMPcNq2NuXSKG03HAT1nwHyBSpItVjSIRYZsXD-k321E8-y2QP87cq7PUjzgQmBd4_HIgKOesJfVrc8Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=F2ukqOhSL2SU0EvtqsQy5BqUnwJctrRhv-ad-Na-B8GUQIe9_BVi4fqlBKCvlBLLuRGVg9wfyp0SUWohLInh0s8NazwC67Fzdp-i3xK357fvJNLSpA7lOi13wl31sjpoCNhVe4VMHcsP1qsAtA-rFQeeDbmUrADT3BJsX71YT9r2N1oAivkH8arC8gKXtgRRjCohJFEE6d9wMogKrLe3-cFF2vuCrY8U2bOeAURsQv4pZC7pT3bI-KxkpoLo6mHMai4y1rMPcNq2NuXSKG03HAT1nwHyBSpItVjSIRYZsXD-k321E8-y2QP87cq7PUjzgQmBd4_HIgKOesJfVrc8Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
حسن پاجانی، قهرمان مسابقات ورزش‌های الکترونیک (بازی efootball) بازی‌های آسیایی ۲۰۲۶ ناگویا: دلیل قهرمان شدنم اینه که یه سال و نیمه ایران نیستم و اینترنت بهتری دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107304" target="_blank">📅 15:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=XzlTBG8ZxJtlCXI9eWNw0hVAarL3mlYnETRClJ0UODABf997Sl_IrFQ8HK0WZRlF15ZWs1iwJE7908Bs14KUlfwz7mflTLZRyCchMTEDvipmcr1Dk0-i1yntAOime6rqiIBKexG4rK5DbSs1dOf5JuWgm9NT1Lbl3qFFnKNTCG9wapGGjJ7CQNn3VL9TKmT0LpB34dDMh_HnqMQwlhGD2Q8IsoXYStm1xjNregDaRLjDjNSTs3VG1NQy4f-sS9MOvXTIOtKh_5xBB_0_mwSzgFWu7A600MXZgLprarGbzMprVnuk_ymOuIJEizxTiKQRygXP3aQa2Wa-fGNCdltSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=XzlTBG8ZxJtlCXI9eWNw0hVAarL3mlYnETRClJ0UODABf997Sl_IrFQ8HK0WZRlF15ZWs1iwJE7908Bs14KUlfwz7mflTLZRyCchMTEDvipmcr1Dk0-i1yntAOime6rqiIBKexG4rK5DbSs1dOf5JuWgm9NT1Lbl3qFFnKNTCG9wapGGjJ7CQNn3VL9TKmT0LpB34dDMh_HnqMQwlhGD2Q8IsoXYStm1xjNregDaRLjDjNSTs3VG1NQy4f-sS9MOvXTIOtKh_5xBB_0_mwSzgFWu7A600MXZgLprarGbzMprVnuk_ymOuIJEizxTiKQRygXP3aQa2Wa-fGNCdltSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
هانی رامبد: امسال سال‌بسیار سختی بود اما برای آینده تمام تلاشم را برای گرفتن ویزا ورزشکاران ایرانی برای حضور در مسترالمپیا انجام می‌دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107303" target="_blank">📅 14:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWHChU65je2KN5yIzfeLw7jq0ipLC5ahQhRW54GDqFQQj5iGxgZ-LKWZZ0_0hv61nP9I8BrPWnn1MVEhVqBwBMuz1WAt3rLR8dxY3Y1A_kwd5vYKUJoZZcczZIxyJ2AQtruW6ORK0bdec0mu5J2WvSb9trVEIABENsQZu9-ZUT221_UETyQntuj31E4W7k1UAUazmyEvKdrhwYGQqiISzqQ-uVyNe3Dz-wR7-72-l49Mzje00WVwaW7L7HwCludLzvWGJYVcrkNtvhyTJLCGIdNYygaSMrkePSzbyS-ToTS0sCOPu5kuv9djsxgGMEHmGbqu6VXLDHLLOFNwBd4Hof6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWHChU65je2KN5yIzfeLw7jq0ipLC5ahQhRW54GDqFQQj5iGxgZ-LKWZZ0_0hv61nP9I8BrPWnn1MVEhVqBwBMuz1WAt3rLR8dxY3Y1A_kwd5vYKUJoZZcczZIxyJ2AQtruW6ORK0bdec0mu5J2WvSb9trVEIABENsQZu9-ZUT221_UETyQntuj31E4W7k1UAUazmyEvKdrhwYGQqiISzqQ-uVyNe3Dz-wR7-72-l49Mzje00WVwaW7L7HwCludLzvWGJYVcrkNtvhyTJLCGIdNYygaSMrkePSzbyS-ToTS0sCOPu5kuv9djsxgGMEHmGbqu6VXLDHLLOFNwBd4Hof6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
هری کین یا لامین یامال؟ تفاوت فوتبال انگلیس و اسپانیا؟ وضعیت جود بلینگام؟ مقایسه توخل و فلیک؟⁣
✔️
جواب همه سوالات با آنتونی گوردون در مصاحبه پیش از بازی انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107302" target="_blank">📅 14:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e44add616.mp4?token=P5Dfe_xYuOOzd18OF4F-xwINWX_8EeHq3K2ULAJQfi-NlTn2gM_nUWu2NVE9xlvw61yLH3xS2PRfk0ekO9-QG1u0BIx6UZ2XAzmF5YyUy866HT1d1ot_6UY3quOMUTmQlGz7aua3MHzaUu-QFSYzK3388kcCMnZzqFjqLLp99lau9VBJWpBCCEx-S9457b3LcRGJlfs_PsTbl3qPmipECoQ8fhLrcrZka0Po97kjeesX0X-7C21JCZPk7g7_gEeeqh1hj8ef4gJQR5dtKzxaU-AJKQw7c4WoQQjm4gH8D7eKRZWwf2EM0TeyaHUz2fv7PL7lxNhLVS-5ggN5Ln2lvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e44add616.mp4?token=P5Dfe_xYuOOzd18OF4F-xwINWX_8EeHq3K2ULAJQfi-NlTn2gM_nUWu2NVE9xlvw61yLH3xS2PRfk0ekO9-QG1u0BIx6UZ2XAzmF5YyUy866HT1d1ot_6UY3quOMUTmQlGz7aua3MHzaUu-QFSYzK3388kcCMnZzqFjqLLp99lau9VBJWpBCCEx-S9457b3LcRGJlfs_PsTbl3qPmipECoQ8fhLrcrZka0Po97kjeesX0X-7C21JCZPk7g7_gEeeqh1hj8ef4gJQR5dtKzxaU-AJKQw7c4WoQQjm4gH8D7eKRZWwf2EM0TeyaHUz2fv7PL7lxNhLVS-5ggN5Ln2lvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بیرانوند سر صحنه پنالتی بازی با ازبکستان به چه چیزی داشت فکر میکرد؟
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107301" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=B4haGfdH0xz8_dYsMVQMzY7q2JIstnwQjstnUZJb6m-2ttFeHQ5Sp4g-G7017oAGTVwv0cQmf01qG_LJesYlSAjAHQE8-VWO5FKlPYdbiqLs6GfhS8TtXokWEs8dJBRrwJ3MHz3PGv8yADGg5eskc6yWrVNVfSanHusNn8p46F3E3nBmfBZutvu7xJxWS3EKyxhnsvkgWp4CPTbfShh2eJRfCbHuxLbwf11mpfPQhVVVFGMMe72Jks5tPFQuDGOCIzZn01KoIuNYAyc0PzlaZHwpVjGNxL2SMQ-g405hkbQJIS4lY0D8FJOY2ZdhaRHfesDiMticgaPuZYtuZuSl0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=B4haGfdH0xz8_dYsMVQMzY7q2JIstnwQjstnUZJb6m-2ttFeHQ5Sp4g-G7017oAGTVwv0cQmf01qG_LJesYlSAjAHQE8-VWO5FKlPYdbiqLs6GfhS8TtXokWEs8dJBRrwJ3MHz3PGv8yADGg5eskc6yWrVNVfSanHusNn8p46F3E3nBmfBZutvu7xJxWS3EKyxhnsvkgWp4CPTbfShh2eJRfCbHuxLbwf11mpfPQhVVVFGMMe72Jks5tPFQuDGOCIzZn01KoIuNYAyc0PzlaZHwpVjGNxL2SMQ-g405hkbQJIS4lY0D8FJOY2ZdhaRHfesDiMticgaPuZYtuZuSl0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کری خوانی های عجیب هندی‌ها برای ایران؛ لحظات پایانی فینال کبدی مسابقات ناگویا و قهرمانی هند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107300" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107299">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6boLjZ7wyF8yo8VSjWsdBtP92mtEGMfai4Td6GjrOV7vRtQ6ny7VVjXbZMv81JgMnBlPDKibQFgelsWnTb8bf1dmNICtDli2k7rf8i_FipBvQz5W7TE8fGVlsTbj3-U2cEFxLCAov6oTs8nRt1SHp7BwzSlqmbZAuGJEfwwXHWrS1taOwYkaDr49XDs-zish9DrxZLwJY0VF0caUXaJ3j9SUSfwDvrtIBZKkeKb9w1lMDhTF8dQknk0IuQ8mwqvDP2I1tFBiPz6_JYB4lVpdEnmpgBlmxQlv7sgT5IeSBNKx15tFjb76VEtVdZzsRfDDMbIYItwM7dcm5SWZTAtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
تو حرم مشهد این آقا صد میلیون چک نذر کرد و انداخته تو ضریح واسه شفای زنش؛ حالا بعد یه مدت اومده رفته بالای ضریح میگه زنم مرده تا پولم رو پس ندید پایین نمیام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107299" target="_blank">📅 13:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107298">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=UuhBzoqR_B9BNqGav-cv42VStsbNmPcyD-Ih4PAPqShIsGVWYsW5dnb044cVJ1moyGIGO0x-4pevW3o9DEepFU80v2yxb47b3dHR4rVExAe97-hQb8M19JZA7creVwUZ91LaNNhfLyFH5AUpi8F4TYVaOcwLr6vAcROkcohNc8wpRHwqAdskN1VybjQfgoRB6CfwbT8nfsitCVvl3VYn-y8fO0Sie_qyNLL3pT0WNB5EX-SmSyrLCcV23oINRcc05DA42dxdVBVS00-H0dSki4y-cJszkMyZe_c9sedtbUr0l_l3XNBtBwNXRyYR3NHft6ZiRJRy3vEDEpT9UmtxNw7hafyzMgggTwVyNCpf6inBjbZGnZQbI6ixvoNHyfT0UmU0Cd0OXCqqEUDCbI6Xa094UgLIBbCkQYIGRGEu_2cdYr2YOYLGkjIYAzSh2RPxb2WDH10kxOUXZcmAO7XnkRdAg-2rgqgen_b0P0ijM4cJuY1Ozk9uGLLSqHmNi8ZKiwGNWcreMR8K7bZyjknOY0T47-aM18NIr03X7VCyYjPz2LIJUYZF-PyCQLFhl4DqjDZTXUO9w0RcHov393C0WnpSLjvBvNS9D3HFkE6Zx3UgbJN3SsEDkN2PrJIXmCiAU0MnARq-kq0NpoGMYaa8FCO7_sbtHKiBlGY22AxGqYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=UuhBzoqR_B9BNqGav-cv42VStsbNmPcyD-Ih4PAPqShIsGVWYsW5dnb044cVJ1moyGIGO0x-4pevW3o9DEepFU80v2yxb47b3dHR4rVExAe97-hQb8M19JZA7creVwUZ91LaNNhfLyFH5AUpi8F4TYVaOcwLr6vAcROkcohNc8wpRHwqAdskN1VybjQfgoRB6CfwbT8nfsitCVvl3VYn-y8fO0Sie_qyNLL3pT0WNB5EX-SmSyrLCcV23oINRcc05DA42dxdVBVS00-H0dSki4y-cJszkMyZe_c9sedtbUr0l_l3XNBtBwNXRyYR3NHft6ZiRJRy3vEDEpT9UmtxNw7hafyzMgggTwVyNCpf6inBjbZGnZQbI6ixvoNHyfT0UmU0Cd0OXCqqEUDCbI6Xa094UgLIBbCkQYIGRGEu_2cdYr2YOYLGkjIYAzSh2RPxb2WDH10kxOUXZcmAO7XnkRdAg-2rgqgen_b0P0ijM4cJuY1Ozk9uGLLSqHmNi8ZKiwGNWcreMR8K7bZyjknOY0T47-aM18NIr03X7VCyYjPz2LIJUYZF-PyCQLFhl4DqjDZTXUO9w0RcHov393C0WnpSLjvBvNS9D3HFkE6Zx3UgbJN3SsEDkN2PrJIXmCiAU0MnARq-kq0NpoGMYaa8FCO7_sbtHKiBlGY22AxGqYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیز دربی مادرید: چرا رئال به گل نرسید؟
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107298" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=lx0Jh1EyPGSFHOVeHNnhu0pp6ZW5WPN2lctKR0XwUJMwIriM20ndXYW04EFbpsh4r5W8GAKHVdUK8zzNyRqcgRMTwliBBrIAxTV1gtdxp49ZxaO0W1fa7oOjBrUd_znr1W3fDTpIxm0qWKHAbI_p_kazW91ZwlH3YmS7U3Qjz9SPcQRezjyD3s1nzgWdlqi97eKILU66Tz0FwUi6L4ifjDG3ysTRrvRUXKPUxPAS3gz6whW8MhCdEduiTqzk1H_rDAK7wLPrgHFlg3earoSSiJJuYXx_Z6DgKCbDRzyhVxLFQtW0OXx13NOXqw5AeqCOLPE3ZEDpRDDl9YVk8lGmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=lx0Jh1EyPGSFHOVeHNnhu0pp6ZW5WPN2lctKR0XwUJMwIriM20ndXYW04EFbpsh4r5W8GAKHVdUK8zzNyRqcgRMTwliBBrIAxTV1gtdxp49ZxaO0W1fa7oOjBrUd_znr1W3fDTpIxm0qWKHAbI_p_kazW91ZwlH3YmS7U3Qjz9SPcQRezjyD3s1nzgWdlqi97eKILU66Tz0FwUi6L4ifjDG3ysTRrvRUXKPUxPAS3gz6whW8MhCdEduiTqzk1H_rDAK7wLPrgHFlg3earoSSiJJuYXx_Z6DgKCbDRzyhVxLFQtW0OXx13NOXqw5AeqCOLPE3ZEDpRDDl9YVk8lGmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
دبیر: تراکتور برای من هیچ فرقی با استقلال و پرسپولیس ندارد
مراسم امضای تفاهم‌نامه همکاری باشگاه تراکتور و فدراسیون کشتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107297" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107296">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it2FlTwjiFa3Ea_4KXiKOeBxjaBNypCNYNCKQJobYJbr4sRVGSrUVT-o7J9gryJhE9bF3AvahhtBX1TGemSFmJuoyKXnmCAAPp_hxQlFrzXqar0NTZcO2c951VD2xfW5CtI-R--Fdoub2RiN27l-wgtth0Dnz2IY_21DJahfXs_H60klx91nz-wpsiQsJsBRAWKR5NTbUFpXVf2ExxqyBZHl0oKrgAgjCGMekhYrjbhLII37BH8VBCoRCytmhryVf12DDS0rJj5BjDCnR-zcVHBJT5eR8XdP41Csb0NgBmrbmH5hLqcedL0ITtBXITEJQDY25s5y5UEP1H4aMfbpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
👀
همسر سابق سپهر حیدری درباره رامین رضاییان: ایشون بااختلاف چه از نظر فنی چه ازنظر اخلاقی‌بهترین‌بازیکن حال حاضر فوتبال ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107296" target="_blank">📅 13:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107295">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3OjErQwEX_mBgk4g2vv7i-t8PyBNHIXvc7PaSzz8qs2O-g9VUOVyvTwUWAYBjyXZp4drmIPmNyuCR1dWhuvfXLO07fmTmMKhJVTgfKXyR5yQWgmP0rjY6-xSH9kRTYo5HhDEnx6NUySuTy3qtgYEnTtVZyNgBsVr9lWKJe9ekYmAg_3TOvPlnGAl_wrKuFDTolgQKjqIwdJUYfhqbG7eqZwvpew7SiFyjktKIeFxxu0JHzBd56sEeVgr5tZD2i3IchH_DplbEbbv-RI4sYk-_zXDiB1h5ZcboA77u4lGBjehuKAIEfctzBmm4WTdv9uNstE5NJA-12tGHFQTpKBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر قهرمانی‌های‌سیتی گرفته بشه نتیجش میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107295" target="_blank">📅 13:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107292">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=oaPmTJoSgZ0_gyoLotPnARPewnE-Is2_sUpB-VJPhwr4F_zjPNwNP_vwXFY5JRqlSpWIbkdXqkyn3CA8gJq-TnxNxMrbxIgseSa2-YAeHqNnwzFJWc_kM1_4SH0nsdmZ4A5HspX1DtDhg3OCME1RRpuzOhrZhKH4MTlDSK_V2PbI9nTTaYbgPmZcecVDN-NIs4_3TFgsWIH9wlOdtZvntHv97tJ6_xDNPBq6jTkeoqNm61PFXsbHiUpkeT1dRVXfc4hYRTKC-Wg05rFKvNfHTymHoIL9R45QoDNwSAm5nLY1CAV5SxdaFdKKfwubofEBR5CF6S_rXVHy_Abqtg9ZnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=oaPmTJoSgZ0_gyoLotPnARPewnE-Is2_sUpB-VJPhwr4F_zjPNwNP_vwXFY5JRqlSpWIbkdXqkyn3CA8gJq-TnxNxMrbxIgseSa2-YAeHqNnwzFJWc_kM1_4SH0nsdmZ4A5HspX1DtDhg3OCME1RRpuzOhrZhKH4MTlDSK_V2PbI9nTTaYbgPmZcecVDN-NIs4_3TFgsWIH9wlOdtZvntHv97tJ6_xDNPBq6jTkeoqNm61PFXsbHiUpkeT1dRVXfc4hYRTKC-Wg05rFKvNfHTymHoIL9R45QoDNwSAm5nLY1CAV5SxdaFdKKfwubofEBR5CF6S_rXVHy_Abqtg9ZnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
👀
بهزاد داداش‌زاده بازهم یک ادعای جنجالی داشته و گفته که مجید جلالی جادوگر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107292" target="_blank">📅 12:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=i1VtkMScwYfhUjlmSk9Zd8iXUxf7StDN5mEKpLQGSRoABnoMIVq7T_r4cgwH2PPoF6CQhmiVTIhUV-X9IaCX8pdGGkKoukXUrid91DrqStjQUP0CDR3vYsDWRYoefUfncPgR46mMmCtLq9DAYi-YX70o8ED4tekVN8kLcH2Z_0XuoOeN1HVatPZd35f3tALTp3OIvNFNOi2fH98k9iOlYX_7CLWahbXwifx6T5jcvkdnuEJASMlcEK5Y2Nfagzl9fh0BT0opMWuwxgUkIKS_7trwTBD5FlofIF1w7yieIZJwgDy4ngSrcCSoezogpwqcBZ4LWNbIQSNIM3_WuhQl9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=i1VtkMScwYfhUjlmSk9Zd8iXUxf7StDN5mEKpLQGSRoABnoMIVq7T_r4cgwH2PPoF6CQhmiVTIhUV-X9IaCX8pdGGkKoukXUrid91DrqStjQUP0CDR3vYsDWRYoefUfncPgR46mMmCtLq9DAYi-YX70o8ED4tekVN8kLcH2Z_0XuoOeN1HVatPZd35f3tALTp3OIvNFNOi2fH98k9iOlYX_7CLWahbXwifx6T5jcvkdnuEJASMlcEK5Y2Nfagzl9fh0BT0opMWuwxgUkIKS_7trwTBD5FlofIF1w7yieIZJwgDy4ngSrcCSoezogpwqcBZ4LWNbIQSNIM3_WuhQl9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
گوشه‌ای از نمایش‌جذاب هلند زیر نظر ژاوی در اولین مسابقه رسمی مقابل آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107291" target="_blank">📅 12:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107290">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b671734a24.mp4?token=oTGVXkFTO48AmKDEoba8Ptrs77SdZPd2DxEsUibe00_raFooHX3o3xOABf8cGWGSG4n2msCWoM4L6SMStn4WydvdlBUKlsSVHf1TZ7ytkcS2hXbAPaui5y2-flbUoZYo99gz8gfm9vks5MUxAmx9fdOuVNiCcPzanwQOx6OPFpYs2SOyVvmVyrld7tMAH8nSrgU2O-Z8d1GXESZZjbhI5K76eQHF9Ab2ktrSjOUdk0GCSGooHV94NZgWhuURwDM2wpujYB9DqQnpsxgr-fpKcy2RGAPBew63lrsO0WlItL_jLyN3Vle_pOCUFoiDgaQ4gHb1Ius94BPFWsIcms9bqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b671734a24.mp4?token=oTGVXkFTO48AmKDEoba8Ptrs77SdZPd2DxEsUibe00_raFooHX3o3xOABf8cGWGSG4n2msCWoM4L6SMStn4WydvdlBUKlsSVHf1TZ7ytkcS2hXbAPaui5y2-flbUoZYo99gz8gfm9vks5MUxAmx9fdOuVNiCcPzanwQOx6OPFpYs2SOyVvmVyrld7tMAH8nSrgU2O-Z8d1GXESZZjbhI5K76eQHF9Ab2ktrSjOUdk0GCSGooHV94NZgWhuURwDM2wpujYB9DqQnpsxgr-fpKcy2RGAPBew63lrsO0WlItL_jLyN3Vle_pOCUFoiDgaQ4gHb1Ius94BPFWsIcms9bqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت ریدمان کریم‌آدیمی در بازی مقابل هلند که حسابی اعصاب کلوپ بهم ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107290" target="_blank">📅 11:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107289">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107289" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107288">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=eoARkI--2eZOV-ReRCCezvqn9hpz97zB7NT5aBrVPx5L4-v4c8bRdy3-3hhtDixceNtkUI2vOe3cE6ZtiZ2eoMsV3ydz-m9VVdL5Cn8Pb8_6IOv0mN9UH-79nHyirW6e9R5hl1qtSlJdHkXhectc0hxMrZ1u8TnaOoc2uizt5b365sjCg5XC_aMnjCVP4JANDlBNJmQ7FZHArqkN080mF1GSCynWap_X01L6rNIyEEfdJ_d8tgPNWPHDgyTlGgU_Nm02nuIlAPOI7Rios0OuD7UcM4_ZWYnXE2VONzrAGdY_Jb58_H9Tjdny1K9_g36grogbPcdBIu-fg91fHzqn8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=eoARkI--2eZOV-ReRCCezvqn9hpz97zB7NT5aBrVPx5L4-v4c8bRdy3-3hhtDixceNtkUI2vOe3cE6ZtiZ2eoMsV3ydz-m9VVdL5Cn8Pb8_6IOv0mN9UH-79nHyirW6e9R5hl1qtSlJdHkXhectc0hxMrZ1u8TnaOoc2uizt5b365sjCg5XC_aMnjCVP4JANDlBNJmQ7FZHArqkN080mF1GSCynWap_X01L6rNIyEEfdJ_d8tgPNWPHDgyTlGgU_Nm02nuIlAPOI7Rios0OuD7UcM4_ZWYnXE2VONzrAGdY_Jb58_H9Tjdny1K9_g36grogbPcdBIu-fg91fHzqn8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
کنایه حسین‌گودرزی بازیکن استقلال به ماجرای سربازی نرفتن علیرضا بیرانوند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107288" target="_blank">📅 11:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107287">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=HHKc2iHxPoeUt-txb4m_J-jXshaB3WIyv2rBtmuy7H-J2bzh1dwlg8ae7X32RB4vezFLecH8ASB1bnxhykszo-mtdY9X3u9i1e47OlL0I4VAfeuoWS6ZL2kYuKKxZTIHla66rknvIfsoPFZslu8RPFo1RVCVp8p7KoyMq3VByh17aM8kkJSSphozxslpv6_8YuqVz-AZNZoa-kXChNpQg9e4XKcZQXI1RQVCOo9olI_NfDx7mLhQL1t63mVgKxbAnMUSJK7cLtMEgDGWj_FJGLgVvRD7v0nY3FJcW-9vJmfNArt3wg9SpMxd8bMIhz1AEnmPuXvGRYC6FeYjrVEUGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=HHKc2iHxPoeUt-txb4m_J-jXshaB3WIyv2rBtmuy7H-J2bzh1dwlg8ae7X32RB4vezFLecH8ASB1bnxhykszo-mtdY9X3u9i1e47OlL0I4VAfeuoWS6ZL2kYuKKxZTIHla66rknvIfsoPFZslu8RPFo1RVCVp8p7KoyMq3VByh17aM8kkJSSphozxslpv6_8YuqVz-AZNZoa-kXChNpQg9e4XKcZQXI1RQVCOo9olI_NfDx7mLhQL1t63mVgKxbAnMUSJK7cLtMEgDGWj_FJGLgVvRD7v0nY3FJcW-9vJmfNArt3wg9SpMxd8bMIhz1AEnmPuXvGRYC6FeYjrVEUGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب کریستیانو از تاریخ تولد هم‌تیمییش در تیم ملی پرتغال
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107287" target="_blank">📅 11:05 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
