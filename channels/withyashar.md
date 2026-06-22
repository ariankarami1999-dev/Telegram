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
<img src="https://cdn4.telesco.pe/file/OAtRwfBPnuWo4pdzCy9VN8C1k5h2rWPorbTgAyQ6zsMdyH1Dzi_uT6L36UnVZ0ItQfayvM1rKjwvjVY_6EEHTUhKqPC5F-V9GGN7ZmUdL-9oIgVG4D0zRLuWbmq4QHyb1yTWjoVdJ7L14XNDv80iyj9R48C2xHpF5qFZy2aKdiEbqmqNkn7fGi0lLJU_YUWJB-o9HbaK4u9asBkIosmFSu2HyctLKNbYhm3Vx_yI-BlXZ2KhnrPEawdhTz49Q7vtN-0ZabGyxPrTqA-V7GaFbSN4bhd8BMHIYWxK0pRrgBdO3y3Zaf3Z6Qb8QdOGS3Lkr9mar8JM4ZWSG-lVd2D62Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-15624">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fe556e38.mp4?token=TlPb2OymtsBAo9mjxrTX62tw0d3p_ZLZpMXEtsYwpb2UpzUSWsN6xJ61k5myb6W2U-BUeOtkjZJByAF9WSf1GbW0aAY9Q7B6pR4ANHEfOetbjZRt54FRsYz2blNq08hgRBq-CiV2phJrTo7_ZkrO-mX_foJZgLotRMUBh50pjCTeyxwRydn32TSdf4UoO-tPwx8HtgJqrnZCnXkv1NPDeHqqN1ZjXtizOvFAl9lz22OD1elRvbHET5353t9Alj3VVrVX_1j0N5t0H1I5y97DRyVoB8v5tY3rvpXAJZ4VB8UZ3SOzZnI6LbIE697rQ3rfc3PqVCnr8bbTMdnPfDnVKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fe556e38.mp4?token=TlPb2OymtsBAo9mjxrTX62tw0d3p_ZLZpMXEtsYwpb2UpzUSWsN6xJ61k5myb6W2U-BUeOtkjZJByAF9WSf1GbW0aAY9Q7B6pR4ANHEfOetbjZRt54FRsYz2blNq08hgRBq-CiV2phJrTo7_ZkrO-mX_foJZgLotRMUBh50pjCTeyxwRydn32TSdf4UoO-tPwx8HtgJqrnZCnXkv1NPDeHqqN1ZjXtizOvFAl9lz22OD1elRvbHET5353t9Alj3VVrVX_1j0N5t0H1I5y97DRyVoB8v5tY3rvpXAJZ4VB8UZ3SOzZnI6LbIE697rQ3rfc3PqVCnr8bbTMdnPfDnVKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با تقلید از ترامپ دم توالت هواپیما
: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشاله در این گفتگوها به نتیجه نهایی می‌رسد و تا به نتیجه نرسد، رهایشان نخواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/withyashar/15624" target="_blank">📅 21:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15623">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOf-Nq-xoyFwcYCX3kWzE_JGbxiNmhupVqe-kF8SLKSRfYu-J0Z2z26RUqWPXeH-uAqHwbg2Sh1r94Tzbkt8YZgtMrbWlG_GyVyYPTA9mLJ1cVW3vNcNeaUbKJ67kMm-pLhfjH_6W7CZ-DAHSOBCky8Rjyof0VAA635zut6F28oyz-ze_6My3GxK9kivroijWX6hu5JoSFTqUd2ATN0IHZqI35thLN_cRmqBOB0zHEUR8-BYmehuSa0iSirErGZWR3kMcPVGq7UlYopBt7Rel1KsXC5JAMCcHhD0hqOyBr00uB7Anleet6Xg10MWreYR1G3CBD4LRfsZ0TrQDzjfcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : همه کاملاً آگاه هستند که ایران برای تضمین «صداقت هسته‌ای» در آینده، با بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد. رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/withyashar/15623" target="_blank">📅 20:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شبکه 14 اسرائیل که به نتانیاهو نزدیکه، مدعی شده ایران از یک «سلاح الکترومغناطیسی با فرکانس پایین» برای تأثیر گذاشتن روی تصمیم‌های ترامپ استفاده می‌کنه!
می‌دانم این حرف طوری به نظر می‌رسد که انگار از یک فیلم علمی‌تخیلی آمده، اما واقعاً وجود دارد و همین حالا هم در حال استفاده است , این امواج رو داخل مغز ترامپ فرستادن. رفتار رئیس‌جمهور به‌وضوح تغییر کرده. چیزی شبیه تله‌پاتیه، اما از نوع الکترومغناطیسی.
روسیه این فناوری رو داره، چین هم داره و ایران هم بهش دست پیدا کرده.
باور کنید یا نه، از من خواسته‌اند این کار را انجام دهم و من هم روی آن کار می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/withyashar/15622" target="_blank">📅 20:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15621">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مرندی: ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید
@withyashar</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/withyashar/15621" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15620">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شاهزاده رضا پهلوی در اکس : در حالی که فیفا تلاش می‌کند پرچم شیر و خورشید را از ورزشگاه‌ها دور نگه دارد، هزاران ایرانی در ورزشگاه سوفای ثابت کردند که نماد واقعی ایران را نمی‌توان ممنوع کرد.
دفتر شاهزاده پهلوی افزود صدای مخالفان جمهوری اسلامی در جام جهانی بیش از هر زمان دیگری شنیده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/15620" target="_blank">📅 18:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15619">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تکذیب تعهد جدید هسته‌ای از سوی بقائی
سخنگوی وزارت امور خارجه:
تعامل ایران با آژانس بین‌المللی انرژی اتمی طبق روال جاری و منطبق با مصوبات قانونی ادامه می‌یابد.
بنا بر اعلام منابع مطلع، در مذاکرات ۱۸ ساعته دیروز در سوئیس، هیچ مذاکره‌ای درباره پرونده هسته‌ای انجام نشده و تعهد جدیدی از سوی ایران پذیرفته نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/15619" target="_blank">📅 18:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15618">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">طبق اخبار درز کرده این معافیت تحریمی نفت ایران در ازای بازرسی آژانس از تأسیسات هسته‌ای ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/15618" target="_blank">📅 18:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15617">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نتانیاهو: تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/15617" target="_blank">📅 17:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15616">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده رسماً معافیت تحریم ۶۰ روزه‌ای برای نفت، محصولات پتروشیمی و گاز ایران صادر کرده است
این معافیت اکنون تا ۲۱ اوت معتبر است و ممکن است تا زمانی که مذاکرات ادامه دارد و توافق نهایی حاصل شود، تمدید شود.
@withyashar</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/15616" target="_blank">📅 17:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15615">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDw1c30AeJACZj4sX_qSXMvQwJDB4SE6Botdydgqjs1TV3dCK7YQJvj0HJJ2bjVQjQ2dVFQyJqf2TVqNcl3MuDFVwNxnR_BzZOUQmII1wWISwZ1Vi4xP-J7cjXRVE1RsYNz-REwuLNHXZxqwal68o9c1r-IXLtPFV0ddu9dJp_cazFbuP27ToHWiQzAhybzbypTVFr_zEzZPS8n99-4rvZ_vgC_KSHGkZsCHRJvzR9a-V5CNttAwMBnwZj2LnLVNVYdpkZ-vuDVYnSGqFLeJtCCuTFEkifQv4jalzEXKuFORnIx3x7o9Y7ho-vUf6TBxxdW1i34o3qCdTI_xllbZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بمباران توپخانه اسرائیل منطقه المشعع منصوری و منطقه بیوت السیاد در جنوب لبنان را هدف قرار داده است.‌‌
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/15615" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15614">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فاکس نیوز: ایران متعهد شده است که به آژانس بین المللی انرژی اتمی و بازرسانش اجازه دهد تا به ایران بازگردند تا بر روی مکان یابی و برچیدن تاسیسات هسته ای کلیدی کار کنند.
معاون رئیس جمهور ونس توانست به چارچوبی دست یابد که از بودجه مسدود شده ایران برای خرید محصولات کشاورزی آمریکا برای ایران استفاده کند و این محصولات شامل سویا، ذرت و گندم آمریکایی است.
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/15614" target="_blank">📅 17:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15613">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">العربیه:وزارت خزانه‌داری آمریکا مجوز عمومی‌ای صادر کرد که اجازه می‌دهد واردات نفت خام ایران به مدت دو ماه انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/15613" target="_blank">📅 16:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15612">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">طوفان در راه تهران
سازمان مدیریت بحران: مناطق نیمهٔ جنوبی، غربی، مرکزی و ارتفاعات تهران در معرض وزش بادهای شدید و گاهی بسیار شدید قرار دارند و احتمال وقوع طوفان در این مناطق از اواخر امروز تا روز پنجشنبه بسیار زیاد است.
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/15612" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15611">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72fc6efcdb.mp4?token=VXX-pK-e8Uq1MHAk1pwN088Z8QXNJCSxlnBDDRgMtYpULGgIiIc8eUcWMCONMEpYR7b6HYGUv_DEruQlqm4Taylr2vitdrv63VNz1MK2-_NoEWFuqG1QaDCCOiyD0fltMRabbHAhkHcRcV-iOHEQOjwIJkEKfqvcUv3w-ag7sZYCCuMe99GwbLoCzTcD4e9ES7cBuMoRt8lcBqIyvJNtrhOMtSuEAs30qQpH1MBBiUmfDhRy0ksPSF9EdY_rI__A5o_uJSh_mwVwEPW4coVEDWCwz9_bXUTlwBphM4IZPfPlQ052ZgRD_eMdS7m3Ysuqf8Lrbr8JV8fpp6M_ztKhlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72fc6efcdb.mp4?token=VXX-pK-e8Uq1MHAk1pwN088Z8QXNJCSxlnBDDRgMtYpULGgIiIc8eUcWMCONMEpYR7b6HYGUv_DEruQlqm4Taylr2vitdrv63VNz1MK2-_NoEWFuqG1QaDCCOiyD0fltMRabbHAhkHcRcV-iOHEQOjwIJkEKfqvcUv3w-ag7sZYCCuMe99GwbLoCzTcD4e9ES7cBuMoRt8lcBqIyvJNtrhOMtSuEAs30qQpH1MBBiUmfDhRy0ksPSF9EdY_rI__A5o_uJSh_mwVwEPW4coVEDWCwz9_bXUTlwBphM4IZPfPlQ052ZgRD_eMdS7m3Ysuqf8Lrbr8JV8fpp6M_ztKhlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک قابل مشاهده در تنگه هرمز نشان می‌دهد که حداقل ۲۴ کشتی در ۲۴ ساعت گذشته عبور کرده‌اند که همه آنها به جز یک کشتی با استفاده از طرح تفکیک ترافیک ایران قابل مشاهده بودند. به احتمال زیاد تعداد عبور و مرورها بیشتر از آنچه نشان داده شده است ، زیرا بعضی کشتی‌ها سیستم شناسایی خودکار خود را برای عبور خاموش  می کنند
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/15611" target="_blank">📅 16:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15610">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">معاون رئیس جمهور آمریکا ونس: ایران با ورود بازرسان هسته‌ای در این هفته موافقت کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/15610" target="_blank">📅 16:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15609">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLDi6UnW8u74sx-GyFl6y5m9rp7H-jG09FZn8n4bJTtWpbDAQYAnUCa4r7ToQRvEgFozUlsXlj7_11se7mExyj4SVQLt039wF344xXC19uBk34JhqFSZeP2V0iasG7fD3V2wzhsn6MGhsWtS0K4Ocz2fOTgG-iVr7R9dhz1saJWcM39DQB7Q-1g4bEGMB_aXDsMGYOJy1zdk-J2qRTUwxq6dGuyVlPOOS8RneSga_PvYoE841BrGVKxEZSlXlAtpXL4-x1TZGIX6eFMHEvGOuZf0IWj0uz47Y-2YBFWTP_rePKQcTOjqMG3Oti3TGpydnHChz_5VM1O7-U2wi5ljAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : یا هر روز به جون هم میفتیم و به هم فحش میدیم و جونیمون میره یا همه باهم متحد میشیم و این وضعیت رو تموم میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/15609" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15608">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d6b1d15d.mp4?token=dz5SZbN-1imxK6xofvL0_JiLo8Wl7WanfD_uaY4M2tudpdLkVvlYZyNc39-gHy8G-WQY-GHpFR84CMpf8-SsCD7ToYG8i2ZImULYrsCQ5caPQ9_2e_k_QpcDsA-V0UE-vYdrS1yXotnHw5SD75tUKFlXQkCQ6Zm935tiVAr71g8SdsIOT_ZSPUIYI1FcwJ5a7-mN4YjL6ROa8_iPJDCcVR96cbLtpuo0e7q20kTm-Y70dSiTgsSsyWzqKtvF-YM4mijdLt0ozfjWK3H9Oj7GTAp8ZxhItOc6XvKKnbc1yOOHsQXZAqGbgEPh4_HobpSfhMe1FlCQI0zc1FwfHXubvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d6b1d15d.mp4?token=dz5SZbN-1imxK6xofvL0_JiLo8Wl7WanfD_uaY4M2tudpdLkVvlYZyNc39-gHy8G-WQY-GHpFR84CMpf8-SsCD7ToYG8i2ZImULYrsCQ5caPQ9_2e_k_QpcDsA-V0UE-vYdrS1yXotnHw5SD75tUKFlXQkCQ6Zm935tiVAr71g8SdsIOT_ZSPUIYI1FcwJ5a7-mN4YjL6ROa8_iPJDCcVR96cbLtpuo0e7q20kTm-Y70dSiTgsSsyWzqKtvF-YM4mijdLt0ozfjWK3H9Oj7GTAp8ZxhItOc6XvKKnbc1yOOHsQXZAqGbgEPh4_HobpSfhMe1FlCQI0zc1FwfHXubvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی : یا در مجلس را باز می کنند یا جلوی مجلس جلسه برگزار می کنیم مردمم ببینند
@withyashar
🤣</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/15608" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15607">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوحه: دیدار وزرای خارجه قطر و فرانسه در سوئیس با محوریت مذاکرات ایران و آمریکا
هدف از این گفت‌وگوها دستیابی به راهکار‌هایی برای حل مسائل باقی مانده است
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/15607" target="_blank">📅 15:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15606">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جی دی ونس: معامله نهایی، خانه است. ما فونداسیون را بنا نهادیم. ما خانه را نساخته‌ایم، اما فونداسیون موفقی بنا نهادیم. @withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/15606" target="_blank">📅 15:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15605">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ:
اگر پول‌های بلوکه شده ایران رو هم بخوایم آزاد کنیم شرایط رو جوری فراهم میکنیم که کشاورزان و تولید کننده‌های داخلی آمریکا سود کنند و مواد خریداری شده به دست مردم ایران برسه نه تروریست‌ها!
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/15605" target="_blank">📅 15:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15604">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/15604" target="_blank">📅 15:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15603">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جی دی ونس: معامله نهایی، خانه است. ما فونداسیون را بنا نهادیم. ما خانه را نساخته‌ایم، اما فونداسیون موفقی بنا نهادیم.
@withyashar</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/15603" target="_blank">📅 15:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15602">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس جمهوری ایالات متحده: به آمریکا بازمی‌گردم، اما تیم‌های فنی به کار خود در سوئیس ادامه خواهند داد. پایه‌های لازم برای دستیابی به یک توافق نهایی با ایران را بنا کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/15602" target="_blank">📅 15:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15601">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عضو کمیسیون اقتصادی مجلس :
ملی، صادرات، تجارت و توسعه صادرات که هک شده بودن تا دو هفته دیگه وصل میشن
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/15601" target="_blank">📅 15:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15600">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ونس دوباره تهدید کرد: اگر صلح در منطقه اتفاق نیفتد رئیس جمهور ترامپ همچنان گزینه‌های زیادی در اختیار دارد
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/15600" target="_blank">📅 15:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15599">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ونس: به ایرانی‌ها گفتیم که وقتی شما حرف‌های بیخود می‌زنید نمی‌توانید انتظار داشته باشید که رئیس‌جمهور آمریکا پاسخی ندهد
👨‍💻
ایرانی‌ها تهدید کردند که مذاکره را ترک می‌کنند ولی نرفتند و تیم فنی آنها در حال حاضر در حال کار هستند
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/15599" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15598">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جولانی : در صورت دستور ترامپ، ده ها هزار نیرو رزمی متخصص جنگ شهری برای نابودی کامل حزب الله وارد لبنان خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/15598" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15597">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ونس: «باید سازوکاری وجود داشته باشد که اگر حزب‌الله شلیک کرد یا اسرائیل پاسخ داد، ما با هم صحبت کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/15597" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15596">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">معاون رئیس جمهور آمریکا ونس: ایران با ورود بازرسان هسته‌ای در این هفته موافقت کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/15596" target="_blank">📅 14:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15595">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر به الجزیره گفتند: این یادداشت تفاهم نیازمند تلاش‌های زیادی با شرکای ما در پاکستان، با حمایت منطقه‌ای، بود.
@withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/15595" target="_blank">📅 14:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15594">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جی دی ونس همکنون در سوئیس :  دیروز روز خیلی خیلی خوبی بود.  ما پیشرفت خیلی خوبی داشتیم.  ما دقیقاً کاری را که می‌خواستیم انجام دهیم، انجام دادیم. @withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/15594" target="_blank">📅 14:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15593">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8ab5474c.mp4?token=dyEcwMM8P4-zG16fAoy7y5LjP_mQkUX9fr99dG2uekjL6Lw94uYUfpdn8f1q2tWsFvIn_-QQ_M6LT7nkoy-_GfC8BMhIc56bCax7s6rN2SCnDoWTWC9V_JvrFfmhK_CYWOY_JJflkJO0Wq-dzOoUw3x6SQdYeaIwTsdRNIkdZi61MVqgdQgmdbCf-BSVmlgIPcuAielQgkEVwSnATJ1X-I2p0iEVVl942Fi9lrlWn-oexRILMEQDs8fqNNSMSgEsiFMYgzLGOUtJ2VZSnYaJyKKuGn58rvjR2UyAbhAQIB69afWO6tcV4B8MPBgSN_wcLussCnBTi_bjIXtC-mzEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8ab5474c.mp4?token=dyEcwMM8P4-zG16fAoy7y5LjP_mQkUX9fr99dG2uekjL6Lw94uYUfpdn8f1q2tWsFvIn_-QQ_M6LT7nkoy-_GfC8BMhIc56bCax7s6rN2SCnDoWTWC9V_JvrFfmhK_CYWOY_JJflkJO0Wq-dzOoUw3x6SQdYeaIwTsdRNIkdZi61MVqgdQgmdbCf-BSVmlgIPcuAielQgkEVwSnATJ1X-I2p0iEVVl942Fi9lrlWn-oexRILMEQDs8fqNNSMSgEsiFMYgzLGOUtJ2VZSnYaJyKKuGn58rvjR2UyAbhAQIB69afWO6tcV4B8MPBgSN_wcLussCnBTi_bjIXtC-mzEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس همکنون در سوئیس :
دیروز روز خیلی خیلی خوبی بود.
ما پیشرفت خیلی خوبی داشتیم.
ما دقیقاً کاری را که می‌خواستیم انجام دهیم، انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/15593" target="_blank">📅 14:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15592">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ادعای سی‌ان‌ان : اجرای تفاهم‌نامه میان تهران و واشینگتن به مسیر صحیح خود بازگشته و تنگه هرمز برای دریانوردی باز است
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/15592" target="_blank">📅 14:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15591">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزیر امور خارجه اسرائیل: قصد عقب نشینی از جنوب لبنان را نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/15591" target="_blank">📅 14:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15590">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">المیادین:پزشکیان فردا به اسلام آباد می‌رود
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/15590" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15589">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b3269c0c.mp4?token=Nh89I0Q3CV1agRcKSRCHtMoEnL9zOhPL_Ks4PHxjC0q0YqE2z46t6V9w0uqlBMlgskMOC5UyIrqksvGL2eCrg7d2tmKxe8JOYuInYOWp1Cgw8I530OAbByNxbshzqTdig0CHUDIyc_3eC8plll67n4S2ZVzjbrTU6uvezEbps6AvydMbtDyUX4p8XQcWpPqQd8Wnk2BOs_5v4yrPqyNLR88Fdddz88kzEom0vYiSBL0ceve5UK-f23NxS_MC8GMcVbd6-Ly-X_018vehl9yvjrTaIPFUsKiF1gchkYjAxczommo9S1_sNb5PP9cV2tF8WPQJ2xR6GxYdw7QWkUpHrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b3269c0c.mp4?token=Nh89I0Q3CV1agRcKSRCHtMoEnL9zOhPL_Ks4PHxjC0q0YqE2z46t6V9w0uqlBMlgskMOC5UyIrqksvGL2eCrg7d2tmKxe8JOYuInYOWp1Cgw8I530OAbByNxbshzqTdig0CHUDIyc_3eC8plll67n4S2ZVzjbrTU6uvezEbps6AvydMbtDyUX4p8XQcWpPqQd8Wnk2BOs_5v4yrPqyNLR88Fdddz88kzEom0vYiSBL0ceve5UK-f23NxS_MC8GMcVbd6-Ly-X_018vehl9yvjrTaIPFUsKiF1gchkYjAxczommo9S1_sNb5PP9cV2tF8WPQJ2xR6GxYdw7QWkUpHrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️ بازسازی پل b-1 کرج
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/15589" target="_blank">📅 13:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15588">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">همتی رئیس کل بانک مرکزی: مقرر شد اوفک معافیت تحریم‌های فروش نفت ایران را صادر کند
بر اساس بند ۱۱ تفاهمنامه ایران و امریکا معافیت (Waiver) باید صادر می‌شد که مقرر شد توسط اوفک عملیاتی شود .البته صادرات نفت ما هم اکنون درجریان است ولی از این پس بدون هزینه های جانبی تحریم خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/15588" target="_blank">📅 13:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15587">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سی‌ان‌ان، به نقل از یک منبع اسرائیلی: اسرائیل در حال بررسی اعلام عقب‌نشینی نمادین از سرزمین‌های اشغالی خود در جنوب لبنان است.
اعلام عقب‌نشینی نمادین به عنوان بخشی از مذاکرات پیش‌بینی‌شده در این هفته صورت می‌گیرد.
@withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/15587" target="_blank">📅 13:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15586">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9abae6608.mp4?token=HrcTImhDHp0HJYHzT_w2CKd5ufPI_bLKd1XpESCQrzjq4DHYJts9YdPyJnpeiD2cNE9fMy91pynp0XciAnwHnpcwFa4HK1p_abCOvCppITYok2UY3rOiTqEGGf9G274mYrgueXyov9mXdaXeDy7f8K5pV-ZuMPuoVpR4P71nMz3XX_vS7SRijkimrAMqlwQRKkzNfyfm7Lpnvt31-R2XKHJOUd3QLd041ijFHqZKEgiRTTDezJMfRdRtzGEs2NVknwnUt_B0g6thiBgZpvQODiWpLBaLTY_oG9MTsKhWndtmf0Y8X961eSYaW2QSfr87Ew8Idp669eWC_eMQ9E35Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9abae6608.mp4?token=HrcTImhDHp0HJYHzT_w2CKd5ufPI_bLKd1XpESCQrzjq4DHYJts9YdPyJnpeiD2cNE9fMy91pynp0XciAnwHnpcwFa4HK1p_abCOvCppITYok2UY3rOiTqEGGf9G274mYrgueXyov9mXdaXeDy7f8K5pV-ZuMPuoVpR4P71nMz3XX_vS7SRijkimrAMqlwQRKkzNfyfm7Lpnvt31-R2XKHJOUd3QLd041ijFHqZKEgiRTTDezJMfRdRtzGEs2NVknwnUt_B0g6thiBgZpvQODiWpLBaLTY_oG9MTsKhWndtmf0Y8X961eSYaW2QSfr87Ew8Idp669eWC_eMQ9E35Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مجلس شورای اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15586" target="_blank">📅 13:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15585">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ایتا رو زدن
پیامرسان «ایتا» دقایقی پیش از دسترس خارج شده است.
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/15585" target="_blank">📅 12:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15584">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qprZS1Sc-o-YNJuYG5Eg2E3sgBK8QLy3exSaZdexvso3zQ3ZGL_6qxXOUKyA9ZMOJxZRJXidUdgzQDizeMKQHRGGpIDdqGIqXsWoUb5KUDXp_nPtgmIglmFHtzVR-ge-oiKKepV8RbNnZ2PuU2rCKltGU64XaqrUTJcuDQJ6SiUmRUcEld0XjP3Y4DZLoEaaj9hldTgSIzvqqDSykFc8Vk3oMo7wTylfRs7jCigGIulDs4GkWwHm11fYoS0LBjc2Ci7XHV3Q94KMCbuBOwcSo4HfXuHWDlRDjkQ2QCzS0gjh1EObW64DplkQT2OJ6lOSOswBgYKznE9cmuidZglbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم غریب‌آبادی دیپلمات ارشد جمهوری اسلامی و از چهره‌های شناخته‌شده پرونده هسته‌ای ایران است. او اهل علی آباد گلستان است و در سال‌های گذشته سفیر ایران در هلند، نماینده ایران در آژانس بین‌المللی انرژی اتمی در وین، معاون بین‌الملل قوه قضائیه و دبیر ستاد حقوق بشر بوده است. اکنون معاون حقوقی و بین‌الملل وزارت امور خارجه و از اعضای اصلی تیم‌های مذاکره و پیگیری پرونده‌های بین‌المللی ایران است. لقب «کاظم دستکج» را کاربران فضای مجازی پس از انتشار ویدئویی از او در یک نشست بین‌المللی رویش گذاشتند؛ در آن ویدئو گفته می‌شد خودنویسی را از روی میز برداشته است، این ماجرا به یک شوخی و کنایه سیاسی در شبکه‌های اجتماعی تبدیل شده
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/15584" target="_blank">📅 12:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15583">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX-FMvSpWJJ9sAy3wQDrJSxOAZksJLJYyaDslCFebsjLXJRpZx2tlfASK9YgoLal1BYJZe9s5t1N2rA1KBM2CcKl1o75OWx-zHCbJPmDkje12wr3cCXOeTZH-YitxQ2GUrDjCRHvi8SfCGNEgBmdd5l69AUrAcjrhgP1FhFXjJcZ9WDnPmOC5bWHS_2loGlC_K70CEEq1tcA_0kowbRvOdzFx8K58epqWpCHPwBO2HYhDwodczMHSM5_o6r3koV3KX3NG_2OcFdGj4nMEAEGLp6lLZnRyejzcPxL59RDE54vhTe8hRJEzuKgQBISMSXIlgoYnzjkqwyeSIqQiyDEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هیئت جمهوری اسلامی (همه بجز کاظم دست کج) زوریخ را به مقصد تهران ترک کرد
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/15583" target="_blank">📅 12:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15582">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd0c99669.mp4?token=L05SSq7ea9ZGpq2-rIZ23TBsLTIbpKlM2a4CKyKoylAghWNb0fyNsSb_qvpGtsiVfgTHtd2_-Xy0wxUAPse-a_HN7tLP5Pei6k_tewSZZUjwsXc6zX2H4ddP0RP8tp2mQqQVNETom-BLYPSGrD4_JLhGvoaFdrSwJwdTEvKEhAYg7zTC8zcbKVyNALpcxO2lnsovzPlI9Og3JG9WWx0zx-eCr0BPsk2Ry5G7iA0Rfj3vBx8ZrhChdUCKItyu_qA-OaxWRUOMkxHnk1ZhrKIA1IEDvmwSTPq5GSix8dmU98iC8hU_lubQnQKfDJkx-gBvXLk3y4Ec7Ut9FZ0GPkIa1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd0c99669.mp4?token=L05SSq7ea9ZGpq2-rIZ23TBsLTIbpKlM2a4CKyKoylAghWNb0fyNsSb_qvpGtsiVfgTHtd2_-Xy0wxUAPse-a_HN7tLP5Pei6k_tewSZZUjwsXc6zX2H4ddP0RP8tp2mQqQVNETom-BLYPSGrD4_JLhGvoaFdrSwJwdTEvKEhAYg7zTC8zcbKVyNALpcxO2lnsovzPlI9Og3JG9WWx0zx-eCr0BPsk2Ry5G7iA0Rfj3vBx8ZrhChdUCKItyu_qA-OaxWRUOMkxHnk1ZhrKIA1IEDvmwSTPq5GSix8dmU98iC8hU_lubQnQKfDJkx-gBvXLk3y4Ec7Ut9FZ0GPkIa1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیر استارمر از سمت نخست وزیری استعفا داد
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/15582" target="_blank">📅 12:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15581">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرنگار الجزیره: یادداشت تفاهمی بین ایران و قطر در مورد اجرای آزادسازی دارایی‌های مسدود شده ایران امضا شد.
وزارت خزانه‌داری ایالات متحده (OFAC) معافیت‌هایی را برای نفت و پتروشیمی به مدت ۶۰ روز صادر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/15581" target="_blank">📅 12:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15580">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزیر اقتصاد جمهوری اسلامی : آزادسازی پول های بلوکه شده آغاز شده و بانک مرکزی اقدامات لازم رو برای دریافت پول فراهم کرده
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/15580" target="_blank">📅 12:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15579">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">@withyashar
وضعیت</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15579" target="_blank">📅 11:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15578">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA GH</strong></div>
<div class="tg-text">دارند مین‌های دریایی خنسا میکنم آمریکایی هاااا</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/15578" target="_blank">📅 11:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15577">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS H A Y A N</strong></div>
<div class="tg-text">الان یکی دیگه اومد دوباره پسر
بزن بزنه فکر کنم</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/15577" target="_blank">📅 11:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15576">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اتاق جنگ با شما : دو بار صدا اومد
از تو تنگه بود ، بگو کنترل شده تو آب نیست ، یه خبری شده حتما
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/15576" target="_blank">📅 11:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15575">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حتما تنگه باز دعوا شده
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/15575" target="_blank">📅 11:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15574">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صدای انفجار در قشم و بندر عباس شنیده شد
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/15574" target="_blank">📅 11:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15573">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgv6wL3MseOwyaxjsffS42KX-U3j2K_Ze7JmPjnoUysR6CQnwXOS3YoyekI-EmGX2Rq-ZolVFbHnnj3NTAkGX0OIlhFhYbFdYGk8Wn9k0boWE2gPPUDBbXnhtco59E9at2W4Ie1hJ6qim8Q1WZPCetuF8L4--KT3yvkpaXZhxg8Dw4brvm9lpaS8X92fwZkOs8RGHKBU4VGK9tXquG7JvB_J3vcr1n5XJZ9xxDlNgJzHpdJ_5lavQCPdpDol3HhIXXOuYpoOfyUNNCqZd_gIM7AImek2PipTn_gimSm1xKAPQpYJUMtrEaCz9h68PaPPukGAupmXdxMEJMu4IrYADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام و جاسوسی E3A با رادار آواکس ناتو دوباره در ترکیه بلند شده. این هواپیما طبق الگوی منظم همیشه قبل از اتفاقات مهم برمیخیزد. قبل از ترور قاسم سلیمانی، قبل از جنگ دوازده روزه، قبل از جنگ چهل روزه و حالا دوباره پیدایش شده. معمولاً حدود دوازده تا بیست و پنج روز قبل از حمله اصلی، جنگ حتمی است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15573" target="_blank">📅 11:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15572">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس: مقامات ایرانی هنوز نرفتن و مذاکرات همچنان ادامه داره. @withyashar یاشار : این باراک درست نمیشناسه اون که مونده کاظم دست کجه
😂
صبر کرده همه برن سالن رو خالی کنه</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/15572" target="_blank">📅 11:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15571">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آنچه در سوئیس گذشت، به نقل از یک منبع نزدیک به تیم مذاکره کننده ایرانی
یک منبع نزدیک به تیم مذاکره کننده ایرانی:
مذاکرات هیات اصلی ایران در سوئیس پایان یافته است، با این حال کارشناسان همچنان در سوئیس هستند و روند اجرای تفاهمنامه را پیگیری می‌کنند.
تا این لحظه مذاکراتی درباره هسته‌ای صورت نگرفته و ایران منتظر تحقق بند 13 است. تا زمانی که بند 13 محقق نشود، در واقع زمان آغاز مذاکرات هسته‌ای فرانرسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/15571" target="_blank">📅 11:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15570">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هیئت مذاکره کننده جمهوری اسلامی، بعداز 18 ساعت مذاکره، سوئیس رو به مقصد تهران ترک کردن.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/15570" target="_blank">📅 11:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15569">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHp48QschpkGaZlPF1eq2aDaMYJotikZV70dk9YDLQd5yXdr2IzYNuFuc-w_PtAc0aZ59h46TjyRYK2lOpZrTJBgVH4L0ciZPsgvc8-BoWMSF_TQMWHrZ_OVTTOZwP5NUBembLJIi3T0nltPR9GD_JIFmXXVUQLpGJN9KRZpKuC26Q8qxyFR9Vim7sF6hLAbu3qJ-vonhb50f7Lx1ZgX9tpZXrZj5lX8uzV3d-clmaBLBi82JfvNa4meJjn2U6FG0vIdAWiiqhqsSRshCyti33TxLCtQnjcp20Zd2mOcDOXNyu3RxISopCw8rMvMKAU9MCEkwNF_hMC7bcEaIa8WOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی عجیبی که نخست وزیر قطر، محمد بن عبدالرحمن بن جاسم آل ثانی بدون دقت، در کنار جی دی ونس، معاون رئیس جمهور ایالات متحده، و جرد کوشنر، داماد رئیس جمهور ترامپ، منتشر کرده است
@withyashar
یاشار : اما چرا جی دی ونس از یک کارت هوشمند امنیتی وزارت دفاع آمریکا CAC با هویت یک زن که  مسلما سطح دسترسی امنیتی و سازمانی متفاوتی دارد استفاده می‌کند؟</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/15569" target="_blank">📅 11:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15568">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرنگار آکسیوس: عراقچی نوشت ایران معافیت‌هایی برای صادرات نفت و محصولات پتروشیمی دریافت کرده و برخی از دارایی‌های مسدود شده آزاد شده‌اند.
مقامات آمریکایی این موضوع را تأیید نکرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/15568" target="_blank">📅 10:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15567">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرنگار آسوشیتدپرس گزارش داد، میانجیگران می‌گویند مذاکرات سطح بالای ایران و آمریکا در سوئیس به پایان رسیده است؛ مذاکرات فنی برای دستیابی به توافق نهایی جنگ ایران ادامه خواهد یافت.
همچنين این خبرنگار به نقل از وزیر خارجه ایران اعلام کرد «میانجیگری پاکستان و قطر پیشرفت بزرگی برای پایان دادن به جنگ لبنان به همراه داشته است.»
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/15567" target="_blank">📅 10:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15566">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تانکر ترکرز : ایران از پانزدهم ژوئن سال ۲۰۲۶، بالغ بر ۳۶ میلیون بشکه نفت خام صادر کرده است همچنین معادل همین میزان  به صورت محموله‌های شناور در نفتکش‌های مستقر در آب‌های سرزمینی ایران ذخیره شده است
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15566" target="_blank">📅 10:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15565">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJcFbz2FZ-RNJWpRKlkpR1esd15byV8p3XtkmiaI2hAlH3efiKzwPASMqHoP_Ln2XpfuzzwGjKSV1iUl2NlTJ-fAF3ettfLlf7QCeri_csoe5atOM2vNy3jdXwZOgdUS-S-kDvseq6DZkVaOhrmE6SgKSweN2gT4J1LBrfja4Kn0Q57tt-LvEAZxCtFnWnt7Vwg9kDm4BVouMHDZmjuRwHjkTR1kK9h4Mhv-1Xv6RoLxhbSztUwNeMsEQZt067IZ0U8fMrxB5ocbbvw1U-D6cP3Rct80-mzkZzOLq3TC4x8cbziZ861m5O9qw3mbA9Y2By7X852SmmLN4IOOMCtEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران دیشب رکورد پیرترین ترکیب تاریخ جام های جهانی رو با ۳۲ سال ۱۹۱ روز شکست.
رکورد تا قبل از این دست آلمان در جام جهانی ۱۹۹۸ بود.
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15565" target="_blank">📅 10:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15564">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سناتور گراهام: به لبنان و مردم لبنان می‌گویم "کمک در راه است."
حزب‌الله مدت زیادی کشور شما را به وحشت انداخته و تحت فشار قرار داده است. این وضعیت در آستانه پایان یافتن است.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/15564" target="_blank">📅 09:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15563">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزارت کشور قطر:
در انفجار یکی از کارخانه‌های منطقه صنعتی «رأس لفان»، ۵۴ نفر مصدوم و ۱۸ تن مفقود شدند.
این حادثه ناشی از یک نقص فنی در حین عملیات بهره‌برداری بوده.
هیچ‌گونه نشت مواد که خطری برای سلامت افراد داشته باشد، رخ نداده
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15563" target="_blank">📅 08:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15562">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVp_JFLSrU02PZAeFWyrVggJoNL713zTeuJD9wvKoSQSBAt4LDlx3WepHmD7cxeP34qeu93_taGGTH4HAGIQlxeN3q4TA8SWR_PioLybTK_xecaXR9ldwciSvurX-Y8ZiMkpKynpRt-FWRAFbcCN5GigLThheTR2NoilV4oyhG1md_KW8ngqPPqqcFPBV9qWdXxsGdKpYycL3QLXSBLNVk5qFcZpdbnGzQjsQ-g6tXDxq2agEiTNMwVPiqmi6uXIeKeDSaqwjrtE6zOk-1ivT2LhxaVBp0vQuUrwStzBc8pBtGgL3WLZJ6DTVUm4Ueu83eBeiVqNf4-Goe5VvGwlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه پوشش اخبار نیویورک‌تایمزِ فاسد و در حال فروپاشی درباره ایرانِ بسیار آسیب‌خورده و فلج‌شده، از طریق «حقایق» جعلی و ساختگی، به باور من «جنایت علیه کشور» است. من تمام گزارش‌های کذب و بی‌معنی آن‌ها را به شکایت چند میلیارد دلاری خودم علیه آن‌ها اضافه خواهم کرد. آن‌ها مجرم هستند! رئیس‌جمهور DJT
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/15562" target="_blank">📅 02:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15561">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗮𝗯𝗼𝗹𝗳𝗮𝘇𝗹</strong></div>
<div class="tg-text">درود عمو یاشار یه سوال ناراحت کننده و کلی داشتم چرا انقدر کشور ما خیانت کار زیاد داشته تو کل تاریخش</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/15561" target="_blank">📅 01:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15560">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9800d55ebe.mp4?token=TUCacj_jbF2lDpgGAL6wiqMaBEo5dxihczc2v_GZdut6vuMiFMBQqfvrheiYwmE02JTiPRpwjPKnCdLVdzog8vnmz3vXPRE2AMP96_wD_bX8dCO0wqHMfyD5cA5LZtVhB1VLP4AcRZL72XjEUnIgf7P-LYm6c7W7Dz9PEW1pKXGGd3a0ckFrdFK0YlhuG5Yz6abARYrh-v-TVYdkp7SI1cqi_N2iUsUtSJu4M25KAToALVvzP4lv71L0Yr_QmQdNf8_HUNgpZgkxBFCi9sIJzQyGMtc9yDr9RY1hdz7hNzdq3MtQuBiebf_5uBKrd6ci-Ugxiy1gtyaJW_jzw9BvFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9800d55ebe.mp4?token=TUCacj_jbF2lDpgGAL6wiqMaBEo5dxihczc2v_GZdut6vuMiFMBQqfvrheiYwmE02JTiPRpwjPKnCdLVdzog8vnmz3vXPRE2AMP96_wD_bX8dCO0wqHMfyD5cA5LZtVhB1VLP4AcRZL72XjEUnIgf7P-LYm6c7W7Dz9PEW1pKXGGd3a0ckFrdFK0YlhuG5Yz6abARYrh-v-TVYdkp7SI1cqi_N2iUsUtSJu4M25KAToALVvzP4lv71L0Yr_QmQdNf8_HUNgpZgkxBFCi9sIJzQyGMtc9yDr9RY1hdz7hNzdq3MtQuBiebf_5uBKrd6ci-Ugxiy1gtyaJW_jzw9BvFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیگه مشخصه من چی بگم !
🍑
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15560" target="_blank">📅 01:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15559">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW8-BI2bX2Lvd2ssInmGml1w8wKgOZw9ZdZuPHUtipHd6YUs6c5ePRuNkvrjcrLDgwAAZHZTcRT030PN_DyfX-pJJ2lREFUgbKHQjIssCpzQTduRVKCE30VCgNMdhKO05AVLhzeh79G3dYmK8uaaqAgO_ifdwiUfl66ftBF9nDzlweFxs2TzuLjtns4uK5jv-l2iRpEu5J1LaUFgoObK5_WZybUeaOlpuhyiBHuBgvm3ZzJzn7Vxw-j2jhI6cz1c0_xCU5rd0z4UdxQQkLD7OmKLwSB4IeRXsmAKUaM5QwWC9dK5cPMLAtBnR7bUXLcPNkZ07wPXf9HlVnKWEZSloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زلاتان پرسیدن نظرت راجع به بازی ایران و بلژیک چیه؟ گفت:
نیمه اول نزدیک بود بخوابم
نیمه دوم واقعاً خوابیدم
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15559" target="_blank">📅 01:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15558">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خب مجوز عبور کشتی های بلژیک صادر شد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15558" target="_blank">📅 00:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15557">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پایان بازی و مساوی در‌جام جهانی مساوی ها
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15557" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15556">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3fhjspMUYUWLle2115gGAZfawMVJJoRNT698n-SjT3MwL0A0ALpmmLj8tzXeaQIamcfyFg10yc9Fo54BGVTbHWGDaxqIJPPRP-FSIO36zc72am-vtPHAH_-sUlllY-fx-iX0lJgKz2_UiMYKBkayWK3jLrcpR-LAsa-i9vT1HihOGmY_d0SC2CMET-aRwiAHFecT7RfYJc5hVt3o9d0zZmW578AnnmUHyFX4KoXVELyB0DrKEOL-tm6BmCJtRR5SZAPDSbCHXO72wz_TWk7kL4YlNMQjy6dG7tQaOR7Xm6G-rAxdFgloqfc6ILpe_kCS4PFrRAOrDl7hp4SwkBkTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عنوان خبرها در نیویورک‌تایمزِ فاسد و در حال فروپاشی: «پس از تقریباً ۴ ماه جنگ چه چیزی تغییر کرد؟ تحلیلگران می‌گویند تقریباً هیچ.» واقعاً؟ نیروی نظامی آن‌ها نابود شده، نیروی دریایی آن‌ها از بین رفته، نیروی هوایی آن‌ها نابود شده، پلتفرم‌های پرتاب، موشک‌ها، پهپادها و تولید همین‌ها، تقریباً کاملاً از بین رفته‌اند، دو گروه برتر از رهبران آن‌ها از بین رفته‌اند، تورم آن‌ها به ۲۵۰٪ رسیده، اقتصاد آن‌ها شکسته شده، سربازان آن‌ها مزد خود را دریافت نمی‌کنند، تنگه هرمز باز است، نفت به شدت در جریان است، و بازار سهام و اشتغال آمریکا در اوج رکورد قرار دارد. این چیزی است که تغییر کرده، شما سگ‌های فاسد و غیراخلاقی، و بیشتر از این هم!!!
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15556" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15555">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آکسیوس از قول یک دیپلمات آمریکایی:
مذاکرات بین تیم‌های فنی ادامه خواهد یافت و آنها احتمالاً برای ادامه کار خود در سوئیس باقی خواهند ماند.
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/15555" target="_blank">📅 00:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15554">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بلژیک
❌
موزامبیک
✅
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15554" target="_blank">📅 00:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15553">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یکی از بازیکنان بلژیک کارت قرمز گرفت درنتیجه باید ده نفره بازی را ادامه بدهند
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15553" target="_blank">📅 00:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15552">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcfc7af55.mp4?token=dIcJ38ycHi7gWX10LQNARSZcPekrtl2uHt9KyvwS4rFFftk-_vbrilsG-da5DPjxmKc47P0Wl3ptOGEOzbTii4oSn18fc9fP1sCP76l4tLjy8Rnni__MG2WjkduBvz_jYnOoYPWqETsl8cRyEomwJtnulC4ViZ2Oqw-NoOLtiGjBcl2NWNLoqjYBn9TZSzZLmFJjDZl3091tsCNJtOcI5_yx0m3-oiI8GpvLBU-SrdeaNfY8CdK7Xad4vVYVN33Atrx8UDHdkAAmTAyaSNnUBOoNdnP1Du02pJ9ApBMautKo0gxsQDI0hDbVqn0uBvXB3dlvEYJSEnmOWbac5aE0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcfc7af55.mp4?token=dIcJ38ycHi7gWX10LQNARSZcPekrtl2uHt9KyvwS4rFFftk-_vbrilsG-da5DPjxmKc47P0Wl3ptOGEOzbTii4oSn18fc9fP1sCP76l4tLjy8Rnni__MG2WjkduBvz_jYnOoYPWqETsl8cRyEomwJtnulC4ViZ2Oqw-NoOLtiGjBcl2NWNLoqjYBn9TZSzZLmFJjDZl3091tsCNJtOcI5_yx0m3-oiI8GpvLBU-SrdeaNfY8CdK7Xad4vVYVN33Atrx8UDHdkAAmTAyaSNnUBOoNdnP1Du02pJ9ApBMautKo0gxsQDI0hDbVqn0uBvXB3dlvEYJSEnmOWbac5aE0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرس تی وی: هیئت ایرانی پس از پایان یافتن مذاکرات چهارجانبه، محل مذاکرات را ترک کرد
یاشار : این ویدیو نزدیک به ساعت یازده شب تهران در زوریخ سوئیس گرفته شده، در نتیجه نشان می‌دهد که تیم در همان زمان محل مذاکرات را ترک کرد و دیگر ادامه نداد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15552" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15551">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb0602203.mp4?token=hgjbgVPalX-lPJn_pl1TMiFI9mA-dDT078GzSaJt_uBpszaY4OBnD1Hc96xYOKLRpISUUZVCeSz7e7BP1D_a6hk9UAk9lcGKT9f0YXfIszH8TLpsAhx9kqu-zUUst931oJyEYtwWjZytwEqtb-M499JyNEqoWVxbDKMdT8S5FcfQZs4goygRvzh5DPaxu7AJWiI1AdX5n4c3YI672ngL0z8eJTv3DYjBKaosP_ZT7RWwNKOww7X0-wxnIoQ1aorhNrOM_7rR4O4btNKEqaXoyYqiz1bNmURcsFVXe2-3_w6JoFtE1oOs86qO_yJIIAwffVuGwsxdGKWe7DQ2plGOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb0602203.mp4?token=hgjbgVPalX-lPJn_pl1TMiFI9mA-dDT078GzSaJt_uBpszaY4OBnD1Hc96xYOKLRpISUUZVCeSz7e7BP1D_a6hk9UAk9lcGKT9f0YXfIszH8TLpsAhx9kqu-zUUst931oJyEYtwWjZytwEqtb-M499JyNEqoWVxbDKMdT8S5FcfQZs4goygRvzh5DPaxu7AJWiI1AdX5n4c3YI672ngL0z8eJTv3DYjBKaosP_ZT7RWwNKOww7X0-wxnIoQ1aorhNrOM_7rR4O4btNKEqaXoyYqiz1bNmURcsFVXe2-3_w6JoFtE1oOs86qO_yJIIAwffVuGwsxdGKWe7DQ2plGOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که شروع انفجار را نشان می‌دهد، در این ویدیو می‌توانید صدای شخصی را بشنوید که در مورد محل انفجار می‌پرسد و سپس با «لوسیل؟» پاسخ داده می‌شود، لوسیل در ۷۰ کیلومتری رأس لفان قرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/15551" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15550">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLofZ7DzRKDVLZZ8r1A8J7kNKRktIDpFyF3xZezaAkhmVloY1kxXqzRzdcdJZ9uIp6bF8k-puD1NI-DTCuPPFf7lE7lkqYxL5nMXG8llyzmFip98ijgaa3oVFJlhi_dtupUjNxcr58IBqWJYGIC0BauVsM3JOiseDEhxCiJAeoL_mIBWkcF28l-DfSAllk2urA472oj79vePX81al74cH8RqsiuwAjmRRdAwHP8v5SsnGcNcByQs1bPpNFTJzkvQhUsSZVHvZsr5zCxp47lH4Hjar-jHlle7R9WNXEH-jyFOryyrXahfGLhnpwAAX2m0kYHk3UzkYIiShMbm-Nsi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایتالیا و نخست وزیرش پس از صرف تریلیون‌ها دلار برای ناتو، حتی فکرش را هم نمی‌کنند که درگیر جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آنها شوند. دهه‌هاست که ما از آنها دفاع می‌کنیم، اما وقتی مورد آزمایش قرار می‌گیرند، آنها آنجا نیستند تا از ما و بقیه جهان دفاع کنند. خوب نیست!
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/15550" target="_blank">📅 23:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15549">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHqRn0gZxd9s6nxgZYJUkMYfmNkTpKQHN7BYKQUCSd_8zRKYTJXO1L4cIdjhIwCR5GZvhxttZcbjBaipgqJhkdWKzQTdmcNNDPyIAZTNx6EA98VATMUQtVPNVTLy7op_42HHX_NV3_iLHpYC1VifrDmUvyms4NuJrzjxOfLxj2zL3b8Gus0KdiFTBrPt41pRSSzWIjJCfD7UHgAACyqjHqNFGDwbHUMhhFRF1uWnnrMcNmONrB9JT183GSu1UkVtIppwDNZNUmoubNeFtsz-qBSnxy1mCuq75Im9QoehlATnInfbRjBwgZ4Svn86zHqI49OpPMdOUAfVR1NsJ9_iIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتشسوزی عظیمی در مجتمع گازی راس الفان، در حومه دوحه، پایتخت قطر، رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/15549" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15548">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گویا تیم بلژیک رو هم جادو جنبل کردنش…
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/15548" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15547">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گویا استادیوم همه دوگانه سوز هستند
🤣
@withyashar
صحنه گل آفساید</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/15547" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15546">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گل قبول نشد افساید شد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/15546" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گل برای جمهوری اسقاطی
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/15545" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8752439b38.mp4?token=CdcZOwX5p1_51Iz_JWCLD2hrQxBYWsYuMVktLlQv2SUyQpUbgeW9D8H6S_tN0eEfsx2gzmIEuiDKx2Pc2mp_c2Pgv5FgRHgnNQGQmn6qSkA80wzGOYRoaS68aPhiTFFNifuFQf86k8hg_bMeQypdgAoNZc5P5MQOLZ7AyTvw6AHVZx2ijicZSMVnNU_suIDUulhVJncg62b1HDev07KGsBUhOdKgpVOCLeE0qnWp5091FFp_zx9j6A5Cae5jZ7QQtEsvPbS8DTx9rx-v22036cAiqZVf_rYxijLUk1si2Id8GDG9QLp76JWj2PCTbAYo1Iiy9uxB5KKu9M6RHyassYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8752439b38.mp4?token=CdcZOwX5p1_51Iz_JWCLD2hrQxBYWsYuMVktLlQv2SUyQpUbgeW9D8H6S_tN0eEfsx2gzmIEuiDKx2Pc2mp_c2Pgv5FgRHgnNQGQmn6qSkA80wzGOYRoaS68aPhiTFFNifuFQf86k8hg_bMeQypdgAoNZc5P5MQOLZ7AyTvw6AHVZx2ijicZSMVnNU_suIDUulhVJncg62b1HDev07KGsBUhOdKgpVOCLeE0qnWp5091FFp_zx9j6A5Cae5jZ7QQtEsvPbS8DTx9rx-v22036cAiqZVf_rYxijLUk1si2Id8GDG9QLp76JWj2PCTbAYo1Iiy9uxB5KKu9M6RHyassYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمارش معکوس و شروع بازی
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/15544" target="_blank">📅 22:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بنیامین نتانیاهو: به من گفتند وارد رفح نشو، شدم؛ گفتند به حزب‌الله حمله نکن، ما به حزب‌الله حمله کردیم، گفتند با ایران مقابله نکن، ما با ایران مقابله کردیم
من نماینده منافع اسرائیل هستم، نه آمریکا
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15543" target="_blank">📅 22:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15542">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/414dee64a9.mp4?token=HODuXkBp5hu52va2-Sho26CiDsTeL9F8FEjC1Cs2lEozyVBhswey-6rxXwp9wy60bVTVM-jl2iDL4c6hzH85EG2xfxgAIYrok2yZDom12BsYM4OmxhSWcnAhTBgPS99SatrqXQYG7Fy1uBVT9pZmvaBteglmNNCqvAxNttfR4A9NxZn66PMpOd3hWL3ZcQgxLRZz5B_NNd9ZM_ZAoPM_kHc7EfiEtHev8f9GDtIpPuimVCCp_OIMakftrk_qSP_G-AtD6oLC53RUnVD25OZnJ1LmeS2nbb9kSRK9HaN5QXHw4x1AVTKXBNJgRHjBz2XQdNDHNNCl26V5hYzH-jgVYEwBhkfJ8VBEgyWUd3miHsZuTifQNb8qB3uV-pGK4Xh8m-N0OZvEWZ1Yqb1Oy7R-fA3jt7adqFm0OUDam73vM30FQr-IwVm-MoJJrVwqU6xystnidTO6fSy0dpbierousqQUQ5_BWBQUQ3SlrsRavJTlw8vGS1Z8dr9gnQ-GI27gMog5uj6273c_xf7NjCkMCnc3zpUxDYnPz14qB7HAuuuVEOWWpBhQquAcViFymzCy0bfIJyi-B1qwMyVmmX4xY9FA9rTM_ExnubTB5cEEWvBtkNjOjw92Rc3RJDENGlj96hI19t73Rn6DNlqMQ62sBGHjSRQnJgW4Xb3lEcMl-jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/414dee64a9.mp4?token=HODuXkBp5hu52va2-Sho26CiDsTeL9F8FEjC1Cs2lEozyVBhswey-6rxXwp9wy60bVTVM-jl2iDL4c6hzH85EG2xfxgAIYrok2yZDom12BsYM4OmxhSWcnAhTBgPS99SatrqXQYG7Fy1uBVT9pZmvaBteglmNNCqvAxNttfR4A9NxZn66PMpOd3hWL3ZcQgxLRZz5B_NNd9ZM_ZAoPM_kHc7EfiEtHev8f9GDtIpPuimVCCp_OIMakftrk_qSP_G-AtD6oLC53RUnVD25OZnJ1LmeS2nbb9kSRK9HaN5QXHw4x1AVTKXBNJgRHjBz2XQdNDHNNCl26V5hYzH-jgVYEwBhkfJ8VBEgyWUd3miHsZuTifQNb8qB3uV-pGK4Xh8m-N0OZvEWZ1Yqb1Oy7R-fA3jt7adqFm0OUDam73vM30FQr-IwVm-MoJJrVwqU6xystnidTO6fSy0dpbierousqQUQ5_BWBQUQ3SlrsRavJTlw8vGS1Z8dr9gnQ-GI27gMog5uj6273c_xf7NjCkMCnc3zpUxDYnPz14qB7HAuuuVEOWWpBhQquAcViFymzCy0bfIJyi-B1qwMyVmmX4xY9FA9rTM_ExnubTB5cEEWvBtkNjOjw92Rc3RJDENGlj96hI19t73Rn6DNlqMQ62sBGHjSRQnJgW4Xb3lEcMl-jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون دیدبان اتاق ورزش در تهرانجلس
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/15542" target="_blank">📅 22:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371017822d.mp4?token=NY2Xb6a9Q7rxfRPYwu7naohfEzLgmJ75VJ0SiXVP4y_mvSHLPVlG_Fgy8P_g4Ugscgyx6fMq3Wa2DMcekN23jEYNSmuF7VwSv1JPNRwM7ctep3g6fesGU2raCTldYJnffzjtR3UIsRdu17Hca8LhqeqzHayxZeXu0clPbFpYuMi6ZZlY8deAipDt0iN_Jxf8AjUUXwzhFQmquegyjjP8QPKeI5_Uduof5Lf6bwrWQludS_tPqxRBgFAseohobuCaYb9Q783yUyjfb4REcypRVjgIHfz2XHHbAaYemhlrsm78LSbv2xgKd3hy3KcFvamKCpnxTYYfrQ5rMTM8Ed2jsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371017822d.mp4?token=NY2Xb6a9Q7rxfRPYwu7naohfEzLgmJ75VJ0SiXVP4y_mvSHLPVlG_Fgy8P_g4Ugscgyx6fMq3Wa2DMcekN23jEYNSmuF7VwSv1JPNRwM7ctep3g6fesGU2raCTldYJnffzjtR3UIsRdu17Hca8LhqeqzHayxZeXu0clPbFpYuMi6ZZlY8deAipDt0iN_Jxf8AjUUXwzhFQmquegyjjP8QPKeI5_Uduof5Lf6bwrWQludS_tPqxRBgFAseohobuCaYb9Q783yUyjfb4REcypRVjgIHfz2XHHbAaYemhlrsm78LSbv2xgKd3hy3KcFvamKCpnxTYYfrQ5rMTM8Ed2jsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران: «فکر می‌کنم ما شرایط لازم برای سقوط رژیم ایران را ایجاد کرده‌ایم.»
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15541" target="_blank">📅 22:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15540" target="_blank">📅 21:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c2572e3b3.mp4?token=OO6LLwdZZnNwxNaiN7W6jg7jlFfRH0K_hqGZ1eJz6i0fDL7QUGZ56QDg33fpauSK33xaQAEu-s5_Px60oADR1iwGGKDZkGdkBOu3sAUHP9IhnCSl2YCraSF1IlAnypIHJnV-xtqY292bKqvPu3RtlfZYeFtAcnOuUtBc3Qs7XUP50mcjOI6rdQrSxxLE3qWpSe_thQgqu9g8U2Q27p-AmwuC2jafQmxCRve_GKuqXeVMooED3InLTDR3MataweQQYI7ImeiYwa_YTjnwzdaR4OapYjLZT61-SGY56tCO4gSXu7Q3DwtMQ7CvBgP_fcNA0NDQ1tS_vBgpkFjumqZ4Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c2572e3b3.mp4?token=OO6LLwdZZnNwxNaiN7W6jg7jlFfRH0K_hqGZ1eJz6i0fDL7QUGZ56QDg33fpauSK33xaQAEu-s5_Px60oADR1iwGGKDZkGdkBOu3sAUHP9IhnCSl2YCraSF1IlAnypIHJnV-xtqY292bKqvPu3RtlfZYeFtAcnOuUtBc3Qs7XUP50mcjOI6rdQrSxxLE3qWpSe_thQgqu9g8U2Q27p-AmwuC2jafQmxCRve_GKuqXeVMooED3InLTDR3MataweQQYI7ImeiYwa_YTjnwzdaR4OapYjLZT61-SGY56tCO4gSXu7Q3DwtMQ7CvBgP_fcNA0NDQ1tS_vBgpkFjumqZ4Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : در آمریکا می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد.
و در اسرائیل می‌گویند من هر کاری را که او بخواهد انجام می‌دهم.
هیچ‌کدام درست نیست. ما رهبران کشورهایی مستقل و با افتخار هستیم.
من نماینده منافع اسرائیل هستم.
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/15539" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">المیادین: هیات ایرانی تا زمانی که ترامپ عذرخواهی نکنه و اسرائیل از جنوب لبنان عقب نشینی کنه، به مذاکرات برنمیگردن
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15538" target="_blank">📅 21:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWKrAngVVv8vKFduV12Wjqxhh4Ggzq80O4RpbsT2vz4tUiyn204Krv47F_dKal6m7hJ0eyo_jepRr2eE23RrwiPnnZYXY-HcgXzdzdf1y-aSQRm6lZU-7nLdTAOD-tcwz_a3ShpEQGbKS1bgxNGbQCn1BXz8Z-8yZnHRATfdL3l2as_LQPbFaqKLFRxGD4TTSVof-w-Fy0X8XHBkiE1Imq7s999JXbbAErn-YktwxCpMbFi-vS1N3bhKj9UHBC_II6tJ-3oJ7pE_Rl14rKOvjaMq1p7AlF04x-85NMbNi5CUNR3SSWgfbspidDshGnIEnN8kyeqJGEAXfj_sMOBPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل و شین بت: یکی از تروریست‌هایی که کودکی به نام «یاگیل یاکوف» را در ۷ اکتبر از «کیبوتص نیر اوز» ربوده بودند را همکنون به هلاکت رساندند
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/15537" target="_blank">📅 21:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نکات فنی ارائه شده توسط قلعه نویی به تیم @withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15536" target="_blank">📅 21:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeonSuf7Yb-7u5cK_phABUSqpei8mW6SDQ4BANOGsw0BlQJwIUBmfQOGOj_YBbLf31HSHPpWpDNd5SBVBVpVAFfm21AUa9lO9RGqYDIcdp_k2n7_YIlFXiPUSGwo0J78dcCpegJmDILLxDqnbUpyOt_Vwc6CTkTbxh7IwiUKdp8vd7TpaCZKWw-mMhx1-79fcfvxA5SXpx6vroEWSDbZhCisW-GAQa_IDh0mzZePUxEOrbuU72YKgos17ZXh4XMmC5gASdYFxhNi3fzB7rd62qvuX9qcUhto92U1NR6B_dDlw6VmHBDIpLpyGXDYtndrzXZBPVfx6Jn67UGL4msPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکات فنی ارائه شده توسط قلعه نویی به تیم
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15535" target="_blank">📅 21:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال ۱۴ اسرائیل: قطر و پاکستان از ترامپ خواستند تا پیامی‌برای کاهش تنش تنظیم کند
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15534" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">منابع «العربیه» اطلاع دادند هیئت مذاکره‌کننده ایرانی در سوئیس به محل اقامت‌شان بازگشتند اما گفت‌وگوها از کانال‌های غیررسمی ادامه دارد. @withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/15533" target="_blank">📅 20:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">منابع «العربیه» اطلاع دادند هیئت مذاکره‌کننده ایرانی در سوئیس به محل اقامت‌شان بازگشتند اما گفت‌وگوها از کانال‌های غیررسمی ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/15532" target="_blank">📅 20:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15531">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کاظم دست کج : لوکیشن هتل رو یکی بفرسته بدم وانتی
😂
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/15531" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15530">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هیئت ایرانی : به جون مادرمون تو هتل زیر پتو هستیم داریم کامنت میخونیم
😂
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15530" target="_blank">📅 20:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15529">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس:
مقامات ایرانی هنوز نرفتن و مذاکرات همچنان ادامه داره.
@withyashar
یاشار : این باراک درست نمیشناسه اون که مونده کاظم دست کجه
😂
صبر کرده همه برن سالن رو خالی کنه</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/15529" target="_blank">📅 20:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15528">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عربستان
0️⃣
-
4️⃣
اسپانیا
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15528" target="_blank">📅 20:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15527">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایرنا: هیأت ایران پس از دیدار با هیأت قطری به‌عنوان یکی از طرف‌های میانجی، ساختمان محل مذاکرات را ترک کرده
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/15527" target="_blank">📅 20:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15526">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سناتور جمهوری‌خواه نزدیک به ترامپ:
مذاکرات با ایران به توافق منجر نخواهد شد،
راه حل دیپلماتیک با ایران شکست خواهد خورد.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/15526" target="_blank">📅 20:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15525">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فارس : هیئت مذاکره‌کننده جمهوری اسلامی هم‌اکنون در هتل محل اقامت حضور دارد
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15525" target="_blank">📅 20:32 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
