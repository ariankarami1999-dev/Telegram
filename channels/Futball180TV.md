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
<img src="https://cdn5.telesco.pe/file/azStJDTFKUSNZkWUALg_zugCGkUySLRdgeTgKzlE7R8oCOp5WZ1gNsKtQkZYrIAvC94oCQdQLCdVa2QDrnNnvYFtbD1qtrX3DV6sVtRukGsrT3Tuy-Z9XFX4OA0ocfc-2V9x5Qqnht_-NKvErhMHitUpLz7Q1ijfi5fMgQuH8mDqwINJhsbWE9oFv4lEFEwknpsZERVhUUO0pjmrPdVp7v1AoIViCfIIdNjxxlCYaxXsHLpQzaAXomXlyOAaY3HA8abqIfwhYb5lDZ1Kew3TwDLmwHsmCdkrvAVeBbprKtX-dOHXop0g3soItUznqNZUs2TTFZk29Ly7SkxLQgPz7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 549K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 05:21:29</div>
<hr>

<div class="tg-post" id="msg-101404">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3R0EXmPwpD3G_Ue1tPHM5nKKlGPj2ZrRkZsU_kZYuHh60Eun0k6UgnNykpeOYQrhVFlPyFbk8FWdny2xWyao9_YxsE9nfV4-_u6Ha6xAdStMXwKKAsTQshvNubJZlneyTH3GMGzOyPRvVaOpjWG-10J9Xr5R20uzayvoJVrzYVp2qshNapvvYw57fJ9iJWR6F8OEXDhpuFcOVZxsjlF_JftxifQF5BgrYp54KaeRlNUqe7imDxoNt1PCuvylT2AAmIFFhaVu8yWrR4-vNRSaR3qyqDdglhkxYIgdpDXFnhBXmlc8axWKXu6U8aIhi5pEWqqaqw8BQk8nvBrWZ79eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
فوری از هرنان کاستیو، خبرنگار آرژانتینی:
لیونل مسی به هم‌تیمی‌هایش گفته که فینال جام جهانی، آخرین بازی او با پیراهن تیم ملی آرژانتین بوده.
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/Futball180TV/101404" target="_blank">📅 03:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvyewI5ixQmqRX7NKfZv90GAp7pIVabUdetDf99rP9HmA5jZohN3lBuUI0lGlGxd_QZCXl0P1v2nNJl2h1J0COt38etQrpJqb591HkPpwrtnl55soPyBv87SSFRtfYxgQH5GsD-WjjQG9dfg8pVqQK_YATEMjFwfLgDAKILOekB8lV8c78QV6iLo59B5lSq78kTlRJgswEslUc_yLqeVujz5OTufK9q7FO-4RZnF2hqDyTpog9iYDArryrVIeDgw8929IeSZYaXDB0SP_-pr3IMasEMHMnoN35_lpcaWfM_bxP2Tf_kicyNlYBdr4OAGcHNOp6mLmOZbvnqxgiwVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
||
آمار و دستاوردهای ارلینگ هالند در دوران فوتبالش به مناسبت تولد 26 سالگی‌ غول نروژی:
🏟️
[419] بازی
⚽️
[359] گل
🔴
[66] پاس گل
🏆
لیگ برتر انگلیس [2 بار]
🏆
لیگ قهرمانان اروپا [1 بار]
🏆
جام باشگاه‌های جهان [1 بار]
🏆
جام حذفی انگلیس [2 بار]
🎖
کارابائو کاپ [1 بار]
🏆
سوپر کاپ اروپا [1 بار]
🏆
جام حذفی آلمان [1 بار]
🎖
جام خیریه [1 بار]
🏆
لیگ اتریش [1 بار]
🏆
جام اتریش [1 بار]
🏆
جام اطلس [1 بار]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/101403" target="_blank">📅 02:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzeXIoV6UxCPplFkxZ1hde8Zsh-2ka7TfHTBYjb8LZVYtX0ShV86n5c7bL55yAdNHCKSlbgEJAlGATrLeoQdkMaU1qNwXLrekbXMaqD6Cd1Rb8r0u8Zh70z_4_KdvIkeJflNBfT_UM3tMMdo4fmFxmVsiKEQhglCq3gOASNHC4qYe7jAucnK3yF_INvBOxSPDPJWQztmI-vxJYRM004kbvJp65IsAtni-S811Kvd881pPFrwBbsnHI5jrErMAiGqeMso_W95l1bjJwA6EKr4er5tn4j1uYWtvPEcsaNq1Mv3Dy4OfirFpHnh6KWsd8zIp7Eh0Dlr1a2sbXZV9CvlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
گلوبو برزیل: ترکیب بدترین بازیکنای مطرح جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/101402" target="_blank">📅 02:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور:
افتخار می‌کنم دایی و باقری با یک تماس آمدند؛ یک ریال به هیچ میهمانی پول ندادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101401" target="_blank">📅 02:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzoJINYBMS4dm5CKx9MnrnR8BPL7sfVjIkjm63_gWapR4nIFBKLNFgd4pbhIY0lHEboRHmTEszj5DG1vn92IO3ilozJ87lzWrcP7QsJlE0gnneWszEqX0q1Ozm6ECLiAR6eOzlFyKY_UwGVWcIwn9KALnPxb8H7n7u2colGvFqfjEhMm_j6COlqFowCecd5KzG3k2ZGHz3O4rNYH0rMsyaZ_afB-aTSRmzGmXIvn9S_FEprsiPhvWFzwn-wFR6wjf7u6OwwEwM3ZfHjiYRxTGVvsN3hA3E3ULm9lKbkpVnxtNhhb6As0_Y7ThHjCrdtDByHySjV8VLy6tkY_E3pVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/101400" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/101399" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB63G7uwgaIwLENKyzAs0RxNEbww2GgeFci45S7OYN3mwM4_P1CJoIJ1nIsgM2EmisXi4iS7r2v1k0ecG61i9lIkmD6em09kwaObLDO5z-UcDsKmK-6CH0_-HEVQlAYnCDSHc-TnWrNlKBCykHRFRLvFqnC71KHLEQ4ewLT3UzrnQqGlZGUfjNVtCVBfxX3NqnV7y7qb4mY_ozzx2gh7c7nD--qccXYPdrS1FsJSNqIDfec2eNfWZUVA1dXkoRxa6HnFT5Qlczd9ZOzlafjVOQkrNqzcP5AHuqwUGzM-7pk8L9yj2N7fkOOJ2SjjBV2yA_L1bOqtpKb6OdVxffg4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101398" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e202619a75.mp4?token=ESnzJg99IThEJ3xn_lisVFnyi8cMRj8ca93cPYWaMewnGk-v_1naB7qgb56NKvcPiI6a4G2BDHstDlUKzz-d_Vt-9e_6rGoZGgHEtQr8fIF9jV37l-ijnJ4JyndXqolotwqskNFEUCB2nl5YkS3UUt30mdgWhIGUoH9zNzxxM7yCzZ808hli5zrtWol7eYrgd0mrrRpoIn4-PfEG1wltSTu5z17tv0sb5Usk3ClxuB9i-1mTNG7iD9b2pZNY7ACQelyJV5ivfDZ6n76gULN_gm-hu8MnMOlZx2D0mg6DpKGMqD9G5XpIfhidip2cwj2P6grPWyRZy91K-bJ0PV_jOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e202619a75.mp4?token=ESnzJg99IThEJ3xn_lisVFnyi8cMRj8ca93cPYWaMewnGk-v_1naB7qgb56NKvcPiI6a4G2BDHstDlUKzz-d_Vt-9e_6rGoZGgHEtQr8fIF9jV37l-ijnJ4JyndXqolotwqskNFEUCB2nl5YkS3UUt30mdgWhIGUoH9zNzxxM7yCzZ808hli5zrtWol7eYrgd0mrrRpoIn4-PfEG1wltSTu5z17tv0sb5Usk3ClxuB9i-1mTNG7iD9b2pZNY7ACQelyJV5ivfDZ6n76gULN_gm-hu8MnMOlZx2D0mg6DpKGMqD9G5XpIfhidip2cwj2P6grPWyRZy91K-bJ0PV_jOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور در ادامه: من بله قربان گو نبودم، نخواهم بود و نخواهم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/101397" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101396">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piLJNNk7Zbu9fZg8OQj5X9_c8DuXIjBMx8SMWhZ_Xs7IuzjJ9U-F3XpS2ax-AVFPklcrsukDp4W9uC1OZVi0rFx810TA5nM-88U2jjA25_mjruCfXfg1keXrY_7OvSsBJREnRyciRh6idZNjHbDLeseKyP5BzZPLbzdeMzwuDw4kLBDarF8GC941hKoq1TOQ9AvvH86xcZGCy4DjiU_R-59RJyN00ztopddEeuE9KfdAF6euXT1O4TSIOXdAuB0QPylDxMfCPjmstMFlw26IOHMH8WqsXtnddwglqqa-Afo4jqPZlRLWEUVJiNMVVGa6W0frOdXL6NczjcFov71RfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر قهرمانی اسپانیا
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101396" target="_blank">📅 01:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=k134COIgGO5zKkB5W9VmCZgpVA-i__PmKqsJcopaPMD724Ocf7o2SjGdpWn75_X8kJFlDGVqkeEZIkmqbimKGhrik_Mt4_tsNP-ayB9xmxv4gKnQCR1D-ja7uV63pqZLI2EIR8GrKM7au9nrBF19cd-R-c3RS6SEozaRk4SVaHGPnUcUYn0Sbpj-TQxDhF9THNm2nFmKomlZFc4YRs6sDC1fE0pSoPpeWtliotc1CGfP9OZYKpiqDtYjWK_tqh8gGvAdNZ145NlnNvLsY9YUqwE6CFwfk8cMpjov9DJHxot2-tA8GTrIHQHAv-gzsbVlBwK4DhyFVaXz8OIZ5rY3og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=k134COIgGO5zKkB5W9VmCZgpVA-i__PmKqsJcopaPMD724Ocf7o2SjGdpWn75_X8kJFlDGVqkeEZIkmqbimKGhrik_Mt4_tsNP-ayB9xmxv4gKnQCR1D-ja7uV63pqZLI2EIR8GrKM7au9nrBF19cd-R-c3RS6SEozaRk4SVaHGPnUcUYn0Sbpj-TQxDhF9THNm2nFmKomlZFc4YRs6sDC1fE0pSoPpeWtliotc1CGfP9OZYKpiqDtYjWK_tqh8gGvAdNZ145NlnNvLsY9YUqwE6CFwfk8cMpjov9DJHxot2-tA8GTrIHQHAv-gzsbVlBwK4DhyFVaXz8OIZ5rY3og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/101395" target="_blank">📅 01:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
👍
بغض عادل از صحبت‌های حاج‌رضایی: جایگاه اجتماعی با پول خریدنی نیست. در آخر، تن شریف باقی می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101394" target="_blank">📅 01:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101393">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_yGSMGE3yDwYxQXCiTmPTVFSWUnsyucEy342YJONZvM0bziSBAscGd1Y_pBSornjiCGAa3olgBLWi_0psoxZa_kiodYSsBrknPtuays_R4JvuW_goUeOw0TSD0w4TrwBZgJk1zrG6FQ3Pezpm1C96E8fOrNo_uVV2vjlN8Jm0H4k2CN2LRwk5SxnxOe3O0wGsrwND4ZejVr4QdKk6u6ZikTDiG7EV-wz8F3M502dBpBhih7yfUkN5kPrDTeWEuHhhmgfNstuDLobJ2X6ChjQPK9vPbq5FnF8GkiHJK78APJmDbCpk2czKFhce0rmsA_kssY615FCyOoDjWbtoTwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101393" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101392">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ4Uw6cKs7zoqB7R-s12UzxUNeHFUbWDBfpUqwmE7UonsgrD3uRx6i7HuYC-croQneOAVGQXysWKIA0jNZ1L5_4hw0Qijy9QF8VPbE6yjYfSuY7y3QIUeD0Y5XmPB2dtPFt3TBqbsUAqur28mRbjJT3zbnBY1WfUoF8_t6z8rcqTOZjLEoEJTfnKf71y96pXzz8abGjqohsBvPLVXB-urmHRgsQCYVNiFpd8acDd-o2fZu9apZjfhwBm4CclcM-4QnMQG1-bRrof8cP0SXBnZ6OpzYN_MsLvHJKii_ttZ_bsEPb1NbtjvXKxHFHLZnhlu22x8NT4UK2vjbHSzq_q4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
دی مارتزیو: لوکا مودریچ و میلان در مراحل پایانی تمدید قرارداد هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101392" target="_blank">📅 01:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101391">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gen3bXcTbluuLUVuVIR0CguPv3Cj5XQlLCE0MuoR5zO7R5HK_fHlhinle7gj-QCzkzNmSuvBSnRzzo9RA5Uj5Oy-D9eY4NvJ8aKC3QQoC1Fm_FIACQd4_3ptnYMI7p-KrWEfW4IFozLwuIU8W73DzfnHQB-_cr9TfKhiVN5sayqTkvjCSUuQmG-4yTDfgruWkoVph66PtdqldalcpuNivuHL__VMqDPWpElL7fgAo27x04dxLQYyZKRTN2WiPN3LlgR8HzRMrWrY5oq8cXugfWWzJFdij-76UQI-LaUIVbtVBLj_zyf7CFYSiqV9_AgQTqYj3FACxvWW15dMup5PYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کیت جدید اسپانیا با دو ستاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101391" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=njJEW6_s1cZDYgRFca1QPZj85ZwJcEbvCGR-bMn41R2DDT123L6clH3OxXuypPsGZxnYgxu5TnaFWKblBbU-embztgtniwEHqSFyNZporGB8-7p5HA6nFLRFbz32EHRXQZmwRaY8qamHIablMkrRpN_rb170Lv4Xf-pocUUFRpdWENPjHLgE6Hyjcy9TRHUztuTOhxRJcQvb7a9tPgLEtM8ruRQBiCXkJ35G0l_ayFjkoXFZl_HnjCVOawnhCgsOPxGmYcYyqz3gLM76Dx8YoYBTcOxqvq3iyJQiBYPFgtnhonr1XzOfxN42g4s4K2OFKxSrdnBb8znGR9ZJ0_Wc6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=njJEW6_s1cZDYgRFca1QPZj85ZwJcEbvCGR-bMn41R2DDT123L6clH3OxXuypPsGZxnYgxu5TnaFWKblBbU-embztgtniwEHqSFyNZporGB8-7p5HA6nFLRFbz32EHRXQZmwRaY8qamHIablMkrRpN_rb170Lv4Xf-pocUUFRpdWENPjHLgE6Hyjcy9TRHUztuTOhxRJcQvb7a9tPgLEtM8ruRQBiCXkJ35G0l_ayFjkoXFZl_HnjCVOawnhCgsOPxGmYcYyqz3gLM76Dx8YoYBTcOxqvq3iyJQiBYPFgtnhonr1XzOfxN42g4s4K2OFKxSrdnBb8znGR9ZJ0_Wc6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با صدای معروفش در جشن قهرمانی
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101390" target="_blank">📅 01:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار در شیراز و اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101389" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101388" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7IQTrKTjkF0JVSGs1PIr1fEOSvaqwO8H6yF8jWbdt72fTBX967FeEKzzIMHK1zmVFJE1J2e5ynlKkEc9UIpAe5IKPQ8SYZbtGFbKhKCoXdngr5mbNya4l-3UBpZYXdNY_sQ8L1jzmIcm8L1SglpnzHcI5NNdGwvXKf5Spt-FG8I4N3YR0esc7pPLPymvvJ0wfkt76M_2jiQsoh5M-Egie0Ysbnf84hN0RZIEialFmAj2IpVWbxoN5e-5VCRRcgRBw4ViG2QZvYm_VKnCWcjqJCBZphNI8a7eSaF9zbe_F6Z9u7S_ACys_tVGWG9CoqYNxjjoZP9_8Q4Ep57VMG1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تی‌ان‌تی اسپورت: فینالیسیما بین اسپانیا و آرژانتین در ماه نوامبر برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101387" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr5JdO_Ax3qMF-XBQqtT-ViCprHSS5hCsXzhmJ-ls5aF1co5ug31G_wSUhUxhrFby67TlKuIpu_4tKZ3p-pDdUtqTBgDcu3EQsfUEF_BBEo0OMTTyROyTHpGOP2AeTUwQ7UQfbTJt_tIsYSGfzAtwTnsQTp54KtO8f4xexy8mC89duCUwnCxmxgHdKNIlJA70mWPIIoxjq-g3UtrIe5yS-ZlKZwqNdeAJy8m8EYOhF_HvOqku7v5ivJHGK_Q8sEtQ7Rqh-PhGLTQMHuHuSaJf6xpjM2ipLekQPfumbjgZu3JV4b7DoCkjzxcAwYL1vsVmXk_ywDPJMSv8fyS5fq92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
#فکت
؛ پشماتون از معجزه خط دفاعی اسپانیا بریزه که اونای سیمون در کل جام‌جهانی 10 تا سیو داشته و کلا هم یه گل خورده درحالیکه مارتینز فقط در فینال مقابل اسپانیا 11 تا سیو داشته
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101386" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nrq8i3UpOD4hbP0PwWEVdHFGLOsS8pzw6hD1-6nJOsac3eTXwBF3ob0vw-pn-Zu9fuK5fIXuGCPA_pSZGhOwpuHljbXs6sL6Li_gI8291YgTdr-TSEVQSJ3LFUX7yKQADJ0JxbZWV8UbevpIzkz7BaFCBpf6OjxHW5pfmuk8IaKALbvs6CM-KoExpzwjG5seyxLTh2GqGP2q5EUX9Uhfj3yMLVwkPxLwMSeRIXFKlp0oqo3bJSWg9Ohls19Lxep2-X69vbCWzgOU4iH86p9VrCSqiQfHOOazRSTT3PrLv8UaLbL_wM3DKLorWfocEsGhCFFZ_gkc60K1djdlB5xa0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تو جشن قهرمانی اسپانیا
😂
😂
😂
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101385" target="_blank">📅 00:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101384">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K8C7kCDP22LRSm2PnSlW7Qot7qqx4GL9R21yMndq6zl39ctsdvQQ_rF3kklL-xwFjqopha6sdXxtNdINeCvSMBGJJFNLrkZc7ss7BbNDO3EKv-ckuP_Hha2HHRYvHaputKIDomqHtKGwYaPUh0_g8VTfMxi0eCV2JUcluLN5ZXMXRx6YSjPYBk-vnWBHAewwUnmUckMOR1I7oCW9nN1NiOCRnnWpkPC65w0-NMH0ghHcroxV1zdFUuwr4CoonKL1OAIAIkMDH64XMurkYA2xn8K7Ecp0Xymw2kLS_WIoCb2sGC5X4qdAmmxvcbBNSPsUqqpE-BzY1p93Fb9py7g-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا با کیت اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101384" target="_blank">📅 00:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101383">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2968949297.mp4?token=bZirzDcv7uGSczfx-5Q_dw3ci11_y76_ZcwZSB8EReGH_w6eXoCPVmqeLXnyzfxJcfAmJO8cduy_i07lU3NdqYm1MjQwvwrxAhUK40CStUQtXOqXPYKuYgpz0oUfHEln_ZCzYZ07xC3mU4QryB7YfGKqpE7tkjSmLDofJRqoQtjrTBPbVOCJ_9wKfYOwQeLKLOe6dbxXKA4Vk9dsk9HtytY7MA7zg6oilGBg7scW6ASwa_kXqt3_75vM_Eemnr3dtxvhqW04dCAODf5nvvr3CzNaAn3jFopbYRHtJYuBDOI2qY88I3-AjONXsiAD2lB_CRKR98CqM0fo81dg3SNBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2968949297.mp4?token=bZirzDcv7uGSczfx-5Q_dw3ci11_y76_ZcwZSB8EReGH_w6eXoCPVmqeLXnyzfxJcfAmJO8cduy_i07lU3NdqYm1MjQwvwrxAhUK40CStUQtXOqXPYKuYgpz0oUfHEln_ZCzYZ07xC3mU4QryB7YfGKqpE7tkjSmLDofJRqoQtjrTBPbVOCJ_9wKfYOwQeLKLOe6dbxXKA4Vk9dsk9HtytY7MA7zg6oilGBg7scW6ASwa_kXqt3_75vM_Eemnr3dtxvhqW04dCAODf5nvvr3CzNaAn3jFopbYRHtJYuBDOI2qY88I3-AjONXsiAD2lB_CRKR98CqM0fo81dg3SNBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101383" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101382">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=eusWOCBBqCFw_yvngF-mBlTRrVK3Dji6A10fJf8tbtr5Mt28fcHDfkDaDdl_ZYHB_ADr1xWR8B5AX4ahjHqUzJf8VxIGEz--iyA7gSj1r90MwE4AUwln_TM9jfZdlnWHUfAVq4LiLJk5ljOWDw28hJNd3LKRobg7GyzKnawZW2ry9cv0wn7iMoPF7WuGHAkdPF3GeVk6xohphhoc8Q7g_RL1wIOTu3_JBTbP5NHCThvuDagT_1BkE7RnmX5-yONXMgGWVguQcuS81xRKbvfzQisX9wG0cBNxmjft3PfMahpstwny4lcT1u_Zng2QIckV9W_R0cVFqSRyYuyn8p3U0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=eusWOCBBqCFw_yvngF-mBlTRrVK3Dji6A10fJf8tbtr5Mt28fcHDfkDaDdl_ZYHB_ADr1xWR8B5AX4ahjHqUzJf8VxIGEz--iyA7gSj1r90MwE4AUwln_TM9jfZdlnWHUfAVq4LiLJk5ljOWDw28hJNd3LKRobg7GyzKnawZW2ry9cv0wn7iMoPF7WuGHAkdPF3GeVk6xohphhoc8Q7g_RL1wIOTu3_JBTbP5NHCThvuDagT_1BkE7RnmX5-yONXMgGWVguQcuS81xRKbvfzQisX9wG0cBNxmjft3PfMahpstwny4lcT1u_Zng2QIckV9W_R0cVFqSRyYuyn8p3U0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال با آهنگ معروفش رفت بالای استیج
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101382" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101381">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101381" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101380">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=lCRmxPv9L9Jk-oPx6YbXZavKAaJGT4qX8GfMp5mtv_U4AEJGNCVkcMoiN41frOBjNPKbhJefTCZjjFMV7Prg3fA77NdgpsDwO8pst7W9jw32WSYwy9iiwx2-FEB_JAFdDW6MUc8cdklrk0TdEQnJMyUIwr5pULFCQU1wsuvziFuE_-HWTlhAfU4y0v8cgHIXY4TKCgJGlR6CRVBeEvhMwHjRDXvcjmU4vRpBwHYJOFTvqGRKvsHJO2ska7r69g-QxTsT080MLuGDyFbd2lhNez-ekOTkns0g3y9mnoWRSTiqyN8TDmD_GL0w0rY8ZR7pTCKlH35G8NO7WP5z-8_Jkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=lCRmxPv9L9Jk-oPx6YbXZavKAaJGT4qX8GfMp5mtv_U4AEJGNCVkcMoiN41frOBjNPKbhJefTCZjjFMV7Prg3fA77NdgpsDwO8pst7W9jw32WSYwy9iiwx2-FEB_JAFdDW6MUc8cdklrk0TdEQnJMyUIwr5pULFCQU1wsuvziFuE_-HWTlhAfU4y0v8cgHIXY4TKCgJGlR6CRVBeEvhMwHjRDXvcjmU4vRpBwHYJOFTvqGRKvsHJO2ska7r69g-QxTsT080MLuGDyFbd2lhNez-ekOTkns0g3y9mnoWRSTiqyN8TDmD_GL0w0rY8ZR7pTCKlH35G8NO7WP5z-8_Jkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
قلعه نویی: آمده ام بگویم شرمنده مردم ایران هستم می توانستیم مردم را بیشتر خوشحال کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101380" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101379">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpD9DB4_v0MEWLjZbLwYG9K0F0sOZeLSVsVdrmi39BrG7pQ3XxAhl4hfG-MTAXa9IVg7uWHVyLZ4XWQdjnX2D2-gqf4gkWg_-6T37QrHdHMvIPVPNM1mxVHn3njSwdulm2e3k5oLc8ZXa21lnEkfWiPEhVZB7B4kI2jxPhXktqWBqmMEgCOPvsEGyFaR0iloFvTUY9uhOJvDnG2m5RInrMPDER3QP939RcrQa8D3G9ZkXgHNYI8aO9wzlSjF9ns_ukQ-T1KB_mESjO909k5DZ59Verj0bLG6hbrrec8A14otlhn33yWDn22Hu3F09NcDmGEofcE3EqFTDJv3RfLq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به گفته آاس نزدیک به 1.8 میلیون نفر در جشن قهرمانی اسپانیا حاضر بودن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101379" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101378">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=iCbc1gUAEb-5HBmerjrCMumwLr1yAWKvD8Hom4X5VBP-trjWZyUu4xd46L-yyZi3tlE2qeslhDIqP71hB3UgC9y5bqorcQ9_CYMGYDcdZGsAuIv0tJYUNw6q7GF0YTdEZ-wjcfwZuiemqWmvk-2yQkVEg0sGMEtYEl-8n8KO9ojee6SFYX4ER5e5TA2AroObwCJowhmelLV7IWtt24HKz7DPFW2IA0R2BFhH5bq50AJ7de4C2nqv_EA8MY3ZMGDJTYr8Jg-idJew2fYIyfBwWA4-nCRsBrJJ-isnyi4swbvTN-Mr7QSc4tWSxNtenDPNhlD2DAxxYU79oaCQ6ZSCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=iCbc1gUAEb-5HBmerjrCMumwLr1yAWKvD8Hom4X5VBP-trjWZyUu4xd46L-yyZi3tlE2qeslhDIqP71hB3UgC9y5bqorcQ9_CYMGYDcdZGsAuIv0tJYUNw6q7GF0YTdEZ-wjcfwZuiemqWmvk-2yQkVEg0sGMEtYEl-8n8KO9ojee6SFYX4ER5e5TA2AroObwCJowhmelLV7IWtt24HKz7DPFW2IA0R2BFhH5bq50AJ7de4C2nqv_EA8MY3ZMGDJTYr8Jg-idJew2fYIyfBwWA4-nCRsBrJJ-isnyi4swbvTN-Mr7QSc4tWSxNtenDPNhlD2DAxxYU79oaCQ6ZSCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قلعه نویی: در همه جای دنیا انتقاد از سرمربی تیم ملی وجود دارد اما آنجا حسادت و عقده گشایی ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101378" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101377">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUzALSS1B2nkYkPqQ2xegD1QqyNF8KcOModCcHJJkZuRVX1fnaUtBmly0VINPAhUzhka1MCwZOBHqfAmSYougfqZkn4aYIBXGrvDgWtb9BS1U53Tz3CFK3twbTksiBMtiKocqxjOcxdnlaiU7PW2thnf1_dm9or4TiHfBgrNXFPIUS5557gJuksz-ccB3_H7v1JZ9V4eYjyQtyNu2gl7km8Iw_n2upPtGSJvM9PgZNgNz7qTP3osx6bxn4_pZ85u0aBijTTpX0IlA9kCpFtAiLJObDQwRir8nYWzaxtUwGRsm3pyVrBeXR4Sb-wTTUFTgltnSSpSVzeIxAiykwjoVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان دوران به صورت قرضی از النصر راهی بنفیکا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101377" target="_blank">📅 23:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101373">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QswE5Y1_rlsrCTn2bgk8Ci6WsXGwCGwBNVYevzuJ0AR0LrD7ANcmbEi-T3S5AVKYKfZmZqDoGTLspwm98aB58nvA06SvOsDJ43HH1GkwCOOtyIpQnfWtgads3Zs-EO8T8Mrh6MUwPtl89FXl7c7Wbv9EUoE-tv-BkEYul3bQutQezUCN0MmhR-SE_0mxDUAbL6-WTFjUPnMI7a2N2B6fCkjv4XzLSBHBCvxy5w6sgDhqPIR0T7TzZqSBfQhjmNbgb1v72fUCSQDFJL9xvmagQQqZim3Ju5Ip2NSWQvmWvkU1zAH_2ZzJskqKmsLoIQzCinWcBBnoFXHDdRbXedNYXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNL9PVZ81WihKbtOxMyhF7XCAVjdjtV1zqzQV5Z2kYlhTuGuO2QaKS2YSF97aV-pfy_usVAFyow-R9_mZkyfaLd0uy-GVm3OxhicdHZAws5j8WRYxUruTbuaZrNurd_h4Qj7BeTqyBPAr7TXiosL2KGZT1yXL0GUnIEnhN4_BKO20kX9nei0IfhWFpOGJsUru9wiUpPI_DRrTR383qVR3z7KDOuR90fkaPUG2KB5iXgVxWgku-aPy7cOuYcTLxFVtYQLSoEytAXtTL_GAfR3Fd8L7CWzdbJoypXRRuZffncJKyTSf4KaNA_0mJXbvH9kw_tfs4YscMIy2CCG0vm51g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQqeVOeE_2AQEVCT4ncPdwUvo6TxUAs1hGzs5YDqsUvR7WgJIoeEMYJLp0ylM4UUAuqK8Muj4l24n9BJhVRvYGrLcgh4FfSWJvFbGBREHa0Zw5EgxiLcJRD5S1a4qN-EOd024b9QCdq4eQMDWf_QIlrBQs-Un4SS8jCl1fqcT5IAjkArwpbLQfQO-N_5_8EauC44DhDZ9FoqoTxLPDPiBLw_tFq0sZiAp40V6zIJW0T_8Jfkowb99ossZT0DhKGjEZWnXhhupZyUqUu35HdMN1sQH9qfJB8qPn97vd9KlyzfsSA1rj0QusD1v3JA7yMBf405_nwf9oU4jwhjGRVlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ka4TvXcK4KdygJaopuc8TjdKuo_1c9pv6dIkdxCdWm5pwmAfjf5XBbOCqL2rj_WyqO5mosVmY_mAR3Cy1NeF9zbYh7Ku0yCPb1aFy3KTDcbcue0V1KUrwyuUxegQ2HahHTbjKt62YphMmjcAzxC4eOmtCt2uKg1QsapR8dHJRUZVd81Mi7cpF6gsWg3k9ioz7BjpoWGhNebG_4pHbK5KlyGiL2tcyyGTY0fqKe61RpZwchVMMXVd4F9Xm7FVqirlC-wX37uiXy6AyJmeo8U8jQaUNSQ0CDL8YOhfBhM5mTSODy08noDaNoCJQJRldGec_luMdckwv34P8dX92u7mnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
| اولین تمرین منچستر سیتی تحت هدایت انزو مارسکای ایتالیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101373" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101372">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtfqNpnD8G2mS1rkV9-vCU2u1efj9LrmkGxG8yddPWwQDpX3u3czvKa8ULB4AWs_wpsMgT1oDhCfWxoFF996qsnR8PTwjbgt6q-VsWxFDcN3fdkLWs-W1Xh78MDwd70cxtcXfQkbU5AE8w90bu1tkBNW5wKItEWg_RMtseFm-5fwpv050slPBgyEXJhNOENQKhIPtWTt3ex1owHIrHPOW3Jid--fzdCdU1y0uWpfXMIgOEkHyo5N2DD-9CUv73M1zZ3zF01zbZc0vpgEatmcx1tX3zK2-dLe6V8XcEH9up1XVNtn9L0R0cM4YBhGDcu4WdXxufYHP1zIgkxh9LHFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:  رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101372" target="_blank">📅 23:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101371">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9632195436.mp4?token=JUDGRyO-vBC2HSsoCtVoNkoLeJyKgqIUyfyoiVsBs1XaSgUNca4ZI0wO6p6CELpDpvN0tqurlHBOiCw8nUynZ76dT0vEw5z24se2CL_UgTJCUkL5pmxn5AkxtSEWDRyw3lTvGIgXoItAQ2nXdzBYYNV07FSgku8Ih1Y-0CpbXyIAVsjRCys2RA9DuBgV2FiBmO_L07Eivu6ANYatPUDPkgyX9Sa90nXeWdzd3PwrVr55gzyEneN6Lr0StD5jBULDGqPUNAPtKrpBomirhISYpp79MK7qXS-5rKg6S-zMKsT4-CQC2hoAJjRWhJDX50e7GoKBv2k7JEN4RoPgViv6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9632195436.mp4?token=JUDGRyO-vBC2HSsoCtVoNkoLeJyKgqIUyfyoiVsBs1XaSgUNca4ZI0wO6p6CELpDpvN0tqurlHBOiCw8nUynZ76dT0vEw5z24se2CL_UgTJCUkL5pmxn5AkxtSEWDRyw3lTvGIgXoItAQ2nXdzBYYNV07FSgku8Ih1Y-0CpbXyIAVsjRCys2RA9DuBgV2FiBmO_L07Eivu6ANYatPUDPkgyX9Sa90nXeWdzd3PwrVr55gzyEneN6Lr0StD5jBULDGqPUNAPtKrpBomirhISYpp79MK7qXS-5rKg6S-zMKsT4-CQC2hoAJjRWhJDX50e7GoKBv2k7JEN4RoPgViv6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
تاجگذاری لامین‌یامال در شهر مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101371" target="_blank">📅 22:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101370">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iONPs1BNy2UgAXBbnb3Sy5-rjzXLppeQZIF0sfsD_XRaqwSRgRbZAnE0LHkpbl28G0WUC5mdX8mzjNPpWJJrGbpzUagSUpbp2VwsJl7xKnu3p6-7FjF1NMECGucZLfjN4XhQEVFCwBuywgg0JWouzJZC5mI4O-H5NsRMVd4daBhdoj_CaN77m7Cn2RdSRQ14i7xp8FZRWM_gACKBbd1CrCgXX4dpuu5BqvdCokHyUFNyXqTXI8KuVz1HyDNvvuYkhTp2e09AYNtscfY-NJcF3rUKxFszuoFg2_-90dWuEyq_2Z_LFafZsfP1wo1NJlGo6WonZF_lAzgZqPSFPGBUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال این بنرو از یه هوادار تو جشن قهرمانی امروز اسپانیا گرفته که روش نوشته شده:«هفتمین دورهٔ مسابقات ولادا دل آنیو (یه تورنومنت بوکس بین آدمای معروف)، بین پاردس و گاوی.»
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101370" target="_blank">📅 22:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101369">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇹
🔴
فابریزیو رومانو:
🔻
منچستر یونایتد این تابستان به مارکوس رشفورد فرصت جدیدی خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101369" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101368">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZKjgyi2NKSoWHmq6YyNDzXpQnunLtV8CuK9tyjACdIFvPpDx37Q2rMPgFDGTX6nSS-6DP4wPzRyOiXX3gqAk2qDulF9XhrXSXCwKSVHSuz0_GlfaTR_sBH5bbCIQJr4OXzv5Jnp1q0yml_ExN7ou1OIvSe6daPyqUoEy6FSCMotoFmq1arL-57PnzV08eAO9IQ0jrXb1-ZzJiTymaPzOJccpGSFPLRBIdueY7g8baw7NozBI1z46b6AALLwURuAxNIIqvzW_18zowF-LbykL0LGmHJsG7-07X1O_js-65lR2Zqq6QR-sgSiudprig_IC_b_jTQfrAN_kyfhpQlsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:
رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101368" target="_blank">📅 22:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101367">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgdJtRapxOvi5RlcqUHKRxJCSsfXzczx9BLz69JYDUTzkznY3flwszVecSrUQFYaulVlCfeUe6i1LcIZjbrP0Tlz8FnQOF0Nbs3w_6_evFzEP2YE8ppgF0jS1GMjX8A8u6BGVLaVcFybmJVW_4qFC4qhHe2OCb5NaGjPKtZyBz467AV_i712Na_uFqX0JJDkPDyNqHcMEfAIPp-tKU7WQHnVHW94cOU37lT4nFnFXd7rCXVix4CRM-SqfgLCeCV8bGZHZdM6xlSPTNeF-7njTnLTBW2Ia0T8y_NJQrC_p6FbDPlgVPNjhCGB45GRwbqOoZCiqoOoBzbrfpw1GBhdCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دزدی قهرمانانه لامین‌یامال از اسطوره مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101367" target="_blank">📅 22:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101366">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=bic7bgUoHREkG-suUVZG6OdvlDcaTtt7Za7SzzxWZTNoT8x4-_cykzU3ttD2_N5-tf5MuLvyVctC_0AvJoEnYXyqJ_j0akEPeNLrsUvbNGXho7C_XQXvjYonEu10WY-InIOldnugYAYvMfDDwh9HLFnhUS39smhxfDl7GyGPEWac6b1ieE6sT7tyQkx6ZIQGvb8PJrx-TWomyVIBxXJlupZUUvrCv_bDs8DU8kQyenegI1ON-KzI6Hsi9O5KctZrn6JqayYZXRzh9ol6kpI4xbKC-iskNxWum6mGGNIx9Q7j6XdKwMStDJGF9Q8c9nnWd9BaOxkYTl8AKEho-QsnZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=bic7bgUoHREkG-suUVZG6OdvlDcaTtt7Za7SzzxWZTNoT8x4-_cykzU3ttD2_N5-tf5MuLvyVctC_0AvJoEnYXyqJ_j0akEPeNLrsUvbNGXho7C_XQXvjYonEu10WY-InIOldnugYAYvMfDDwh9HLFnhUS39smhxfDl7GyGPEWac6b1ieE6sT7tyQkx6ZIQGvb8PJrx-TWomyVIBxXJlupZUUvrCv_bDs8DU8kQyenegI1ON-KzI6Hsi9O5KctZrn6JqayYZXRzh9ol6kpI4xbKC-iskNxWum6mGGNIx9Q7j6XdKwMStDJGF9Q8c9nnWd9BaOxkYTl8AKEho-QsnZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
کارلس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101366" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101365">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=KDDOJhE2RXYsevbVcsKlyEqbKhhYAykCKkAQZ-xZ3QxZLBltnSWwQSzH1i0i8tIRcqNo6IiR_e01d1r9DYR6zhM35Utx_7a6uukOwHISnkOzKYz6HCsLYjaCee2ZEmcmsaPufLCMt5S9_wrO5GBoQgEcjhRHmCqdjKDL4qbY_D5_G3BvR6EiLLJMxsYLvURKU_gXv3r4FnnQTiykrhVcqNKYRKjODLJ2gb2oNXxsyyF_96NirqCU-jH72C7QjetCuf8D_f7-TUHJAS2xupAtaNRztauCTAMTOO35ygudQrT_4wobl6UHbylBg3qZqCHyA_0ABS56YjKK9iE6QBG6JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=KDDOJhE2RXYsevbVcsKlyEqbKhhYAykCKkAQZ-xZ3QxZLBltnSWwQSzH1i0i8tIRcqNo6IiR_e01d1r9DYR6zhM35Utx_7a6uukOwHISnkOzKYz6HCsLYjaCee2ZEmcmsaPufLCMt5S9_wrO5GBoQgEcjhRHmCqdjKDL4qbY_D5_G3BvR6EiLLJMxsYLvURKU_gXv3r4FnnQTiykrhVcqNKYRKjODLJ2gb2oNXxsyyF_96NirqCU-jH72C7QjetCuf8D_f7-TUHJAS2xupAtaNRztauCTAMTOO35ygudQrT_4wobl6UHbylBg3qZqCHyA_0ABS56YjKK9iE6QBG6JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏆
پرنسس‌های اسپانیا بیشتر از اسطوره رونالدو دستشون به جام‌‌قهرمانی‌جهان خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101365" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101364">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgOKUuMaKvgGp8HSXCEMpvS24yJ-xzMKrPoMe6AFdlUtiwiddbb5BwdKeggK8lOvk3MPVTQlKsCNEGyutGBORQQifhP1T6xDkYhoP1BKGdP65yHR1yuXj78tZP6Hc6qmH-Dppc78bcgi_KZSSKSPRCm7kbWVQfliU3tq8NkxeoFTfENIPXfo6r7OYYUBqKOmYsznx3pl_kWJI5sCV12bCy4d428mnVi3Mj6woDTrQY1YQC2w1tRRDM0gChyxi6u5xeWbRUJksE1Xna8LQKrfLqtrjIe5RINa-JGAh49GnouIgD7YPsuWx0tYz8KKiR6ZVwMWRf0w6HM7lFCr9VHfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال 2010 خوان کاپدویلا دفاع چپ تیم ملی اسپانیا  قبل از بازی فینال سکه ای در چمن دفن کرد تا کمک کنه اسپانیا قهرمان  جام جهانی بشه.
🔻
شب گذشته به مارک کوکوریا گفت همون کار رو انجام بده چون هر دو دفاع چپن و کوکوریا هم این کار رو انجام داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101364" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101363">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnTFWPMMD5cYvzye2l3O39VSfLEk_d_iJjZl8_GWrDQUuX9DQ1FoSZ4qq7X50j46BtSKIgQ5Wj8w--MbL6Gja_SUQeRN8polKNmh389gTip7gLQ-RVEbgmtbl4YgGHc5YKYhb54EKBYxnASrP14gi9qOWiyeqZaXF7oSYpJYLvdTmB5Qz4yD6Vt3cKYDIGal2we2mZR22U7PD_ckZTxeMCoxljiDCCGTRr9cx-wlc1k_3BdpODlb6d8DwW86EEOWfhid3xYo6kSFaEvPLcnfKYoIWQ8DlLkoL8Z-ZrRUJ3Axebh4vByLo1fuucJk4GXDvYWZcKd0maBsyI_q8cSLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📸
مسی، اسطوره فوتبال، از طریق صفحه اینستاگرام خود:
🔺
"درد بسیار زیاد است و التیام این زخم زمان می‌برد. اما من تمام چیزهای خوب را نیز به یاد خواهم داشت... مسابقاتی که نتیجه را تغییر دادیم و تمام تلاش خود را به کار گرفتیم، و این خاطرات برای همیشه در ذهن باقی خواهند ماند. با حمایت یک کشور کامل، و در کنار تلاش و زحمات این تیم، ما دوباره به یکی از بهترین‌های جهان تبدیل شدیم.
🔻
امروز، درک آنچه انجام دادیم دشوار است، اما این تیم به فینال دو دوره متوالی جام جهانی رسید.
🔻
از صمیم قلبم، از تمام پیام‌ها و تبریک‌های شما سپاسگزارم. ما بار دیگر به عنوان یک کشور متحد بودیم و در کنار هم، افتخار بزرگی را به خاطر اینکه آرژانتینی هستیم، به اشتراک گذاشتیم.
🔺
همچنین، به اسپانیا بابت قهرمانی تبریک می‌گویم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101363" target="_blank">📅 21:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101362">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
😔
لیونل‌مسی در بدو ورود به آرژانتین: درد بسیار زیاد روحی را تجربه میکنم. زمان بسیار زیادی باید بگذرد تا درد من التیام یابد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101362" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101361">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqA3iDGDYvQbFLS7xvoAPntReAKEFCGCVVYjY3Q_SOnbRS_GdcdIIFeG9iGdtHjKVXoTGINEDjLjpNtFRJQE1yAuah9TF9f1Zzeht9QCHillw2OTEuqtFYLmpvFCLs_M5_-U-HC3FgKMt3vs5g5foBgD3uJEObCUC_bdMCjje-RQQROwqVcwffzv-nIR8ssm-ndP2lWQowCdk_rSBbprt8x-MwJllEWz4q69hLByBdlQLkHHA2awIM9tgubuAIhhqo_0JYrmCbyPsEQXA6PNtGyl0dakuXhoTgSAU8VGW0WxqUH8727bguAdq8u-eHUMjEZJWemmJv9PGNdZUPE7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🇪🇸
انتظاری‌که مردم از بازیکنان اسپانیا بعد قولشون درباره قهرمانی دارن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101361" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101360">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erWEaal7dLZ4wpBv_P1V-7yL3B9fEizht00EJmcN9Qf-6ebRUu6qeRzcGl3n4bh6fPBg5z3QgonftIZOeXvYROhDMJpuS6bY3gLcY4Tv3dj3LvqZYlKhgGterYN4OFvtpjYOBQXXPdiWdtdAzItW6y61XVoQPpeJD7QEjhsbUOTgmM8t94QxtRkLb5Hk3-TaE0hnLwr9qAPjzlwBNJ1KsZZwTyWU7N_jzAmw__mH0TxYIT8lt9dhFYsUY3Obpgwdn7BylhimMW8NRjj-caj-yN6ENjvn1Z2ldaQEfp_vfhGqUBSgsT3YXFexH7ZoRuJFVOzO0xEbHoMmnEeSBZln6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه قدیمی سرالکس فرگوسن: حمله خوب براتون پیروزی میاره، دفاع خوب براتون جام میاره!
🇪🇸
اسپانیا در جام جهانی:
🇨🇻
کیپ‌ورد - 0 گل خورده
🇸🇦
عربستان - 0 گل خورده
🇺🇾
اروگوئه - 0 گل خورده
🇦🇹
اتریش - 0 گل خورده
🇵🇹
پرتغال - 0 گل خورده
🇧🇪
بلژیک - 1 گل خورده
🇫🇷
فرانسه - 0 گل خورده
🇦🇷
آرژانتین - 0 گل خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101360" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101359">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZy9_CW90W9Juie4sBfKEFGdjH-OAYZmF5l1-4n7PLNYOnNp3T65D8aN2Kb-u_YdPj1RoinsxsTdSz3Pqk1Choxk__gyspYDa1b7KrhgOrxaZN66ssdA3Bky7y2m3SRm37jUdDP3ZYpsuBi7cj6Fwcpr6rtRc_UGt2Mpf1dOK0y_hAFhjnvFXUB_LTlrLWAfwjQ3DPtpiTYH4hU5UpXnryYREV30AbZ-H2Qvqo1fsCwRs5d7kPVbq3ii2ytsG4cfVgAM0dtIJkiLQbtu1fJ-6MEuVBdk7V-jx7Orsop9nxj-YDfzSo1brnp_KVxllXXH-utmKAqvY3avncuZl0PPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
‼️
کریستیانو رونالدو، یک ویدیو از یک شبکه اسپانیایی لایک کرده است که در آن درباره فیفا و آرژانتین صحبت می‌شود:
آرژانتین تیمی بود که باید حدود پنج مسابقه پیش از این از مسابقات حذف می‌شد، اگر کمک‌هایی که از فیفا دریافت کرد، نبود.
و فیفا یکی از فاسدترین سازمان‌ها در جهان است.
به همین دلیل، من اصلاً از آرژانتین نمی‌ترسم، بلکه از اینفانتینو (رئیس فیفا) بسیار می‌ترسم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101359" target="_blank">📅 20:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101358">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101358" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101357">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=eO_IMTt7TJaYskD_m8o5Mupyr6kRGy_rEN1KoPcJXVmSOR5h7K_2vzcyid2de2p4fgFz-1JQtbaKg_1Rf_CNwBs89qrTz1kLImtA3UCG-_3w6p9TiMmJP7Luf356NW8aWjdTfbSvqgRSH7PK_M6k-wqWseSqh_ixRO_uoPyREqPhVKz_9Rjb4ARH5fvlG-_c4IjsmrNkrw8AaXbAIrcQi41ZKTPZXUFqunIG14ORVh3GxwktAUZ5-zzCdVPSwG4hqGameBLC1Sar31KjT06voLmlDXzbuEPNWn8BvYUqkjEjHsrbBQB6rBAofsucBB4VXrJGbfDZfiWhrtMP36KLuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=eO_IMTt7TJaYskD_m8o5Mupyr6kRGy_rEN1KoPcJXVmSOR5h7K_2vzcyid2de2p4fgFz-1JQtbaKg_1Rf_CNwBs89qrTz1kLImtA3UCG-_3w6p9TiMmJP7Luf356NW8aWjdTfbSvqgRSH7PK_M6k-wqWseSqh_ixRO_uoPyREqPhVKz_9Rjb4ARH5fvlG-_c4IjsmrNkrw8AaXbAIrcQi41ZKTPZXUFqunIG14ORVh3GxwktAUZ5-zzCdVPSwG4hqGameBLC1Sar31KjT06voLmlDXzbuEPNWn8BvYUqkjEjHsrbBQB6rBAofsucBB4VXrJGbfDZfiWhrtMP36KLuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پایان دوران ستارگان دهه‌اخیر فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101357" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101356">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101356" target="_blank">📅 20:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101355">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgwqYn9GxntkU1Qts5-hQoKtxcwk2ynn09mdbmTY8na_VwN9fvhtxv2u8Rc4_3dUcfQ_BBgJvcbHPFVErtpT9WZl6vETqnnaqyBRcjnzZutT8HVEDXUI0lqq9Gq45nt5idGjteao9_RhgOjzni28MRYWJlh1w-x_ZEOhnS9oiKwfC6jKHEJNyIc7zRWSXbyDzqkrTtrc7YBHzOr-mnYopwlKWwC8KhAtzazO6wYtRAl24qLzqYPr4lkgCuk327z8dScZlVJdv_uKPPzs3OWil_Mm1y9vKmCdm5BAStLM8LuKZMKb6qGVlayIJaX2T-TU9GYTQmcnKtOF2QQnmRJwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این قتل را چندین برابر پرداخت خواهد کرد!
این دستورالعمل به پیت هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک نیروهای مسلح، و تمام فرماندهان ارشد نظامی ابلاغ شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101355" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101354">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=h3RJdax75POU9jPD8OO2e4Nn4q9ghH0PsfKpj-VSH56QCr7WsGmwvIjcL4LkBdGIP5SDNspwyLR-LK2vI2PqBf4UBBfbQXmAhPYXkQ2SoaVZg9PTq-a4CQA4I23KYDFxMfl-gYLMhE0_94JerwaEtzHu0WeA2prrfNs_Hq9RejfW4r3NhNFXeXKBl569TI7slY7lOOR-F1-E9-xGVy_09Hf66kIvmGziwXLcwNB_Qk9u_MWvbfUw_PkYftChg7E7GAJfc0aBfQLbDcdgusazwVxoIigR_KL7LTRntRYH85Sm67ME9eU68tJqG7D5WWC3bIobRn5fYIa6j9AvcjwhQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=h3RJdax75POU9jPD8OO2e4Nn4q9ghH0PsfKpj-VSH56QCr7WsGmwvIjcL4LkBdGIP5SDNspwyLR-LK2vI2PqBf4UBBfbQXmAhPYXkQ2SoaVZg9PTq-a4CQA4I23KYDFxMfl-gYLMhE0_94JerwaEtzHu0WeA2prrfNs_Hq9RejfW4r3NhNFXeXKBl569TI7slY7lOOR-F1-E9-xGVy_09Hf66kIvmGziwXLcwNB_Qk9u_MWvbfUw_PkYftChg7E7GAJfc0aBfQLbDcdgusazwVxoIigR_KL7LTRntRYH85Sm67ME9eU68tJqG7D5WWC3bIobRn5fYIa6j9AvcjwhQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لب‌بازی امباپه و اکسپوزیتو در میامی حین فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101354" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101353">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=uHmOi-DDSJ-lTAksk5bsmdiXcZfAiEtLW6bIDv70kl6CFWrYBcwXAZnK1jrVsn7wMgTF8_hI5C0Sye3jTfEFUZuMwXrBqk2yQlELBM-0aNVRMgN94zUVXQsLX2R6j_4RQ85UphFMARtoWzDsf9qiVur3zPYkLNi13t9w5OMZ-AvccxqPt66fyz9TKCiONzxWlCzQcCHLV9iL9UEbRgKe-bChDtQC1nMfPi1WGxX0myibuC2R6BkMY2aXsZya7KsVYdtVFqU_pUDHPFhJgEo22Pgu45SH81_tzU3RbZW9myEROPofcV8qakYeIdJr0vzeG-9Pey505xJNNDj3SwaVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=uHmOi-DDSJ-lTAksk5bsmdiXcZfAiEtLW6bIDv70kl6CFWrYBcwXAZnK1jrVsn7wMgTF8_hI5C0Sye3jTfEFUZuMwXrBqk2yQlELBM-0aNVRMgN94zUVXQsLX2R6j_4RQ85UphFMARtoWzDsf9qiVur3zPYkLNi13t9w5OMZ-AvccxqPt66fyz9TKCiONzxWlCzQcCHLV9iL9UEbRgKe-bChDtQC1nMfPi1WGxX0myibuC2R6BkMY2aXsZya7KsVYdtVFqU_pUDHPFhJgEo22Pgu45SH81_tzU3RbZW9myEROPofcV8qakYeIdJr0vzeG-9Pey505xJNNDj3SwaVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
صداوسیما مثلا دیشب اومده با ریوالدو داشته مصاحبه می‌کرده فقط چرا ننه ریوالدو مقنعه سرشه رو نمیفهمم
😢
😢
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101353" target="_blank">📅 20:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101351">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTNWKxXfavKiZwB2KzZnAz_RmiqQHyt2e6J0mrp9B27b0-ZkFxquros-cChCDiVABj-DGH8h7goaVaGz9gQg0hxZ9w95MyJwRxm5lCj6_Kvn5pUVLis7L2SVoobzz87Jupe1mSdcZkP4-DwTwudtAl0hopwxNL7kQy2f0NTZgr4KkZGZc72V1GWCAYeEB6HPRP688R8paRSnuTIO20zOcJ43ttyY7PJ92wL3YupSNDvAaL7bQN1RevsmAmwNBQRMjz9ceQEVzYscvW1hVwyaLG06v9ClPMFg8an1GIGZGpUQxlXXqyx9UDZXhTejJacFncRWfeYM7NHuv2uAorxnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjW_LbEK_80xS4A8T_-y0KrzxMR1o44sUmb1Rq7Lv8VlSaTysvI1bQm29f1KPfBrLDI7d8C3jHPPi4EoFEtNf6K2fFdjRi5ZHY8efkNBMc5EsDrm_HrFctqldiS2t1Layl7qmzEQAGSC2muiBRzTMGKyKn16QB3Xo9E4nE-jFd3DPP04zETJnKPum9k2XR2f4KMxbqrndzRGnoNSTFGsYndF30CgF1AHhKRSz0wDZGzxCWMIGhk550bRbA1dFts8xwcnsH5f1CS1bQbAcLVUBiHX5tR8pEHNXaW4q1RSYz3TF9hEi2QlnU7WnrYO1XlS7jtxBwo1HyC9Pji57zLYAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
اسپید، یوتیوبر معروف دیشب حین اجرا در اختتامیه جام جهانی مقابل چشم میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101351" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101350">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihd9VAeymAVA3M7ayDa72fImv1qC_B49ozgsR5LJ_IW_jxq9wbSanntTxQiye3u_GrZ-prxJ3ftzi1Zlh9gT5V9eYPpSJZR-MOmR4W_6k5ocUzrKmj-W9qcPnuzbNACBVJ9vQAbCVR7v8TVV_wpfJHgREFrGUVcAy6IFv7_oR43o6FmWvlLZ0kj6JnSCcki9YPgCXfX-48SVHA60ssiQBUfSjK28_afbVXcIrZUkJW3zwjv8YS1i8nyatprzvC9Uxas6U859yVzQHvk5HdnKVhuqrQKk0GvwTy_cAJgFg5fLHWmUqIkzLxmmR2RhrJs9jRkOl2tHZ4OBtxGjBPoIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین میزان حضور تماشاگر در یک دوره از تاریخ مسابقات جام جهانی
✔️
جام جهانی 2026: بیش از 6 میلیون تماشاگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101350" target="_blank">📅 19:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101349">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6626cfb5.mp4?token=R4v0zi2xtNLm4s5gIBvkpTNPh_EYu54lh_rczCyfN_rreJeUKA310fvKADLnKRS1PABHx8UiqCjQDQTjOEpOeWRJLgEIoMEyRbT6PWPP79QcR3MkAVrOEjwSnB6BGLNNVTadEU2oegP_DIsCkFfkW8dwuO_JkQCyyvgnFXo0X2TO0D3ZeHJFKN5NIP2vvqcVHh-fG8rLBHydJpkyW40Hx30OLJz_pb7HDq0HijEEtXDLLfRM9pAnocXTnDKUnOuexMj1JeD7HS-QFk1r_i-wzxZzqjWrhojc_wzoA3mbT3oA7snzLiQkqcNLwN7pcpIr8OvUSKhJ2eCSdUd_Wo_c8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6626cfb5.mp4?token=R4v0zi2xtNLm4s5gIBvkpTNPh_EYu54lh_rczCyfN_rreJeUKA310fvKADLnKRS1PABHx8UiqCjQDQTjOEpOeWRJLgEIoMEyRbT6PWPP79QcR3MkAVrOEjwSnB6BGLNNVTadEU2oegP_DIsCkFfkW8dwuO_JkQCyyvgnFXo0X2TO0D3ZeHJFKN5NIP2vvqcVHh-fG8rLBHydJpkyW40Hx30OLJz_pb7HDq0HijEEtXDLLfRM9pAnocXTnDKUnOuexMj1JeD7HS-QFk1r_i-wzxZzqjWrhojc_wzoA3mbT3oA7snzLiQkqcNLwN7pcpIr8OvUSKhJ2eCSdUd_Wo_c8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
هوادار تیم‌ملی اسپانیا بعد قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101349" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101348">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0058133a45.mp4?token=l0Bb06s1LMJ_4Cw9mMxHr6EhJTwulXvLRtFxEOe_jzB1-hPfEHgC0UQOJ1KRZgvp6ziIAKCKXZJ7q6VBghgRIvxdHLzm4kRhsObfdozgjSGYdZibKWDBLpj4v7nU4gEYlghPWAJDD1SaZemKQWhHzAhdULjH87FszNvenqu7yi5E5mOh9MvV6tgVYmoDLKRZb_t9oXzoN3MkHXwFmEHtZe0SQsiOoytaQjrq9oPZzIRXbZOjtA3cgo1_N9kUmCg3oNpnkJfUmhTfkBjJR8_l5cKhAx8489u5_Z5T28A5SjIvUnAb9EajYRLn5htxQjSG3dV2cC9WTelB_9jGkPbAsJTq0nLZ6ZalCw7JPMdDm_nuUTvJmn054ZyxtuRmYiNqiXNFKV7HJkA9vBcQdwbj6cKqY32XyWk4iukMYYbqUs44UY20h26sLTR8Ifx4FN2LTpNm093jVQmKOfhbFlXWKsBNpSjmGqB_tQEGKEUPoZGYiJzgmN8_2jukY0I2RyckGQfBFsy8n9hMcRHzU32cJSLVowXkrclUncRib1vgOXD3wYDttL72pDb9779QSu2sET_v8UdxsWgCiESCH28mkPKOImLzdemYGzB9kqN3L5ZORNfiS50zD24es7oEC8aicDdcyo5o37U84bL_ObqHMmS8ZwzJQVBoFuKCSr4ZA4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0058133a45.mp4?token=l0Bb06s1LMJ_4Cw9mMxHr6EhJTwulXvLRtFxEOe_jzB1-hPfEHgC0UQOJ1KRZgvp6ziIAKCKXZJ7q6VBghgRIvxdHLzm4kRhsObfdozgjSGYdZibKWDBLpj4v7nU4gEYlghPWAJDD1SaZemKQWhHzAhdULjH87FszNvenqu7yi5E5mOh9MvV6tgVYmoDLKRZb_t9oXzoN3MkHXwFmEHtZe0SQsiOoytaQjrq9oPZzIRXbZOjtA3cgo1_N9kUmCg3oNpnkJfUmhTfkBjJR8_l5cKhAx8489u5_Z5T28A5SjIvUnAb9EajYRLn5htxQjSG3dV2cC9WTelB_9jGkPbAsJTq0nLZ6ZalCw7JPMdDm_nuUTvJmn054ZyxtuRmYiNqiXNFKV7HJkA9vBcQdwbj6cKqY32XyWk4iukMYYbqUs44UY20h26sLTR8Ifx4FN2LTpNm093jVQmKOfhbFlXWKsBNpSjmGqB_tQEGKEUPoZGYiJzgmN8_2jukY0I2RyckGQfBFsy8n9hMcRHzU32cJSLVowXkrclUncRib1vgOXD3wYDttL72pDb9779QSu2sET_v8UdxsWgCiESCH28mkPKOImLzdemYGzB9kqN3L5ZORNfiS50zD24es7oEC8aicDdcyo5o37U84bL_ObqHMmS8ZwzJQVBoFuKCSr4ZA4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن باشکوه دیشب مردم مظلوم لبنان در بیروت برای قهرمانی اسپانیا
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101348" target="_blank">📅 19:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101346">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79908eeea2.mp4?token=YHmZ9S_rZ1B8Qmyalcp0D-MlMD7QWF1g2vo6-Fm93_cNfIaFiZoWrGfILKeiGg9wjuqEEguZPEH5XmC7VzZNg7QJigHSvNsrCl1kLJoy7dlYeDIgANcv3tlo5_1gAv5GJy3y8zqcPjlxSyPcrgRMboi7jdRTfpfLK3tGG3YyxwYyd2sK8T-b3-R2cKG5ovboijK5R2yDUmtAj3fIncUWG2Gsm9fK6Ma8AEy7vYR0PxentQ3Oc_yd1zAEuu49x_k7AUcIoiUQLwJkbbYXaxa3lBrthRtFGix2cHbJYeF0e2VtcS6U_aubGqSc5nAXgBScFcqtUMP1iBS3gXhEUTydkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79908eeea2.mp4?token=YHmZ9S_rZ1B8Qmyalcp0D-MlMD7QWF1g2vo6-Fm93_cNfIaFiZoWrGfILKeiGg9wjuqEEguZPEH5XmC7VzZNg7QJigHSvNsrCl1kLJoy7dlYeDIgANcv3tlo5_1gAv5GJy3y8zqcPjlxSyPcrgRMboi7jdRTfpfLK3tGG3YyxwYyd2sK8T-b3-R2cKG5ovboijK5R2yDUmtAj3fIncUWG2Gsm9fK6Ma8AEy7vYR0PxentQ3Oc_yd1zAEuu49x_k7AUcIoiUQLwJkbbYXaxa3lBrthRtFGix2cHbJYeF0e2VtcS6U_aubGqSc5nAXgBScFcqtUMP1iBS3gXhEUTydkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇺🇸
بخور بخور پرزیدنت در جایگاه ویژه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101346" target="_blank">📅 19:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101345">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpxY5W0MGfUGw-iKiVHTBGjm3job1Urk7-Vbf-nB-F09YbuaRg4fO8jt00Ml-sKyYnTHMdw4w1HJyxHun0OSRVMY_0NGI86X9UFYeEWdan5qd08mX1_RvULvqFGe954OUOEblTX_PB-nlwaHpiUkxQdPeEXbS2yTOwmoiLvBsN-W5VSuwjTtdrefkuLPTIkJC12Qo71XK7vj_3aGKOs4FwCnFSMbwlFRZbKWUK-ceKgiokfiZG66865DKf3ll-IQup8iRAfcyqpS_vL7YyXBJkcaAlpAxQnWWXzqZWvnmKBVsT8pjpkfDlrUBqFz5PbqiK1Ohrca7-aWyyZA71csgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با ۱۰ گل اقای گل این دوره جام جهانی هم شد. برای اولین بار دو جام پیاپی یک بازیکن اقای گل جام شد.
و برای اولین بار یک بازیکن در یک فصل آقای گل لیگ داخلیش، چمپیونزلیگ و جام جهانی شد.
عملکرد فردی: کم‌نظیر
عملکرد تیمی: فاجعه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101345" target="_blank">📅 19:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101344">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7RzI2d1ZKcvYhA35ifSYjsccFOzDsEQlTi61qROIjtI0_vpfCX2S5O-fMf01WaMAfctC0Qy_j5gClSPSR4M3B3BfkLEGrXrI8kAuUhxzM898Sa7-fQ3zPgI9eUT7BO3CrBRNUmjTEQg4BqTopdAj80z3CFfMKSSd962yPKf4x5ROTwNhpGZ3s2wkiN1fHGo1zJstSauFo-BI_bW9mOizkmOF0YDWM7iwJSDWsjDCbA1wuuk8YdErMt38IBbyHiXGKK4AvO0-P-DzOvZXWp_qT3VFMm3sto-r-p-Ib1whtZyIEdyaGN-i0BDhmlGf_LKCSHAU5iDacrnBhryfx9_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بایرن مونیخ از تمدید قرارداد لایمر تا سال 2029 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101344" target="_blank">📅 19:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101343">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773a69b961.mp4?token=vq7L2IUxLw8uDvJcJF1Gfa-GMwrM46yRuv68t7sMiCkaY1KZeF7ZlA-uX6vsIxubwgMKrNgj4VHR5jTAUfSVu8AAnriCerDQDBc0PpCjj8Nsz393E698LAMdaaUytbVNLJzPIG2StmQ753qcpKLurTOZBt6VfwYsJRtYC4S8BkPaWkO7sojn4hzLSdkolu-qTiIeVYB-thNspo4tcLgZAbUOpy41XXC2Pky_9djs0nNiIwJfhMAb31khsrxssSpXFCKRof2OaHszryQ9jr_8Zwj8GI429WYx009M3-YeeGzefNjH6PpbaozWzZf2_a4uVhfyVQWfPvXYeTD2IPnY2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773a69b961.mp4?token=vq7L2IUxLw8uDvJcJF1Gfa-GMwrM46yRuv68t7sMiCkaY1KZeF7ZlA-uX6vsIxubwgMKrNgj4VHR5jTAUfSVu8AAnriCerDQDBc0PpCjj8Nsz393E698LAMdaaUytbVNLJzPIG2StmQ753qcpKLurTOZBt6VfwYsJRtYC4S8BkPaWkO7sojn4hzLSdkolu-qTiIeVYB-thNspo4tcLgZAbUOpy41XXC2Pky_9djs0nNiIwJfhMAb31khsrxssSpXFCKRof2OaHszryQ9jr_8Zwj8GI429WYx009M3-YeeGzefNjH6PpbaozWzZf2_a4uVhfyVQWfPvXYeTD2IPnY2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های زیبای دلافوئنته درباره اسکالونی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101343" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101342">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G68M3RIw9KD3AXb1Lc8gmsZQ639SMUQM390gUkfRmFwHDxnCx5NRar34sOemTZ7jJwAZKrSEHCLNWP08GTDzemAc0wCROR4DTLHQs9VkTbIXyMlAytzf0iFRx2iQdsjVFpcf4lEIy3i5ne_E2m4pgbgZXjSBrzCertK5dbFmrzStli5Z7fUI-8YF_fQm_KoeICMSEYqMrcy2xW3e1aYCdHvDJtq8sK8yF35-sBPStADnnii21_t_ibUTp3AbtB7Lwr7_QKuOtZlaGEGmGafMPl-_CvTI9OQVafRswRpA2A43KBcwouwFXw5GFz9DBLLqt-WO_F0_lG9IYF30pBAuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
#فوووووری
؛ به نقل از منابع آرژانتینی، لیونل‌مسی تا امروز تصمیم به خداحافظی از دنیای ملی نگرفته و احتمال داره در کوپا ۲۰۲۸ نیز شرکت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101342" target="_blank">📅 18:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101341">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=BfIUuLNLA92Kh1NJ7PKRPwp3KocPmtmV9-sagmW1SuFPwLfnwGlUP7D_rlX1znIK6SsrgBkBU-MT0QpZHBAN819Z2wai7tkAGyPIEvJfwLbvkM1slvQJWdzjgjalpl2WD-3sqTjhLT9HVzW94zfbGkb0lym0QTeUwg5K07D54bGJTOTOoKn8A8bjZBfJ_5MTuHsGBwp9SWMZ4HLp8gfezdPkQ3egRU0QTF6tm9biooz0iTKDolEjcIQMHEgCNdFNsGcpx9iXBbbhH9UCoFwjysFKeqomEUE_5WZHJBFdCGsXWwSRDdv8B3X-593OKZ2TyMWAdNSN-lTe4Isn-wS8npVOf0uwWH6MgCLD3RMG1IBuKqRz13s6TQrNOk3NjhR8j1KedFFnJjd9ldwNae0pES0UKnrTe3C7uko0aGUTp-ODOXsxd3V7-X_WmpQd5r6TV5pI91Gxxu-5IX6uxn3VkrTb2s5FSb7bnBA2qWjsF6h-VkPmR6RaZG4t9C7veAao1n8P-2sRn_tyVCkr_ZEwUL7bu7kTbUyvcgJUGhDzfbRBd3bhVy_PuHE4ycYKns23sENntT1XA7lu2AxXzNtVtxe6rhq47JEgEu0MQqgitNMmiTMwSvQ1AO7GmXqv3lVdlJ4LEQjvXujPd7Jn-N5IY7mlUczqmU3uQqlTtOmNYrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=BfIUuLNLA92Kh1NJ7PKRPwp3KocPmtmV9-sagmW1SuFPwLfnwGlUP7D_rlX1znIK6SsrgBkBU-MT0QpZHBAN819Z2wai7tkAGyPIEvJfwLbvkM1slvQJWdzjgjalpl2WD-3sqTjhLT9HVzW94zfbGkb0lym0QTeUwg5K07D54bGJTOTOoKn8A8bjZBfJ_5MTuHsGBwp9SWMZ4HLp8gfezdPkQ3egRU0QTF6tm9biooz0iTKDolEjcIQMHEgCNdFNsGcpx9iXBbbhH9UCoFwjysFKeqomEUE_5WZHJBFdCGsXWwSRDdv8B3X-593OKZ2TyMWAdNSN-lTe4Isn-wS8npVOf0uwWH6MgCLD3RMG1IBuKqRz13s6TQrNOk3NjhR8j1KedFFnJjd9ldwNae0pES0UKnrTe3C7uko0aGUTp-ODOXsxd3V7-X_WmpQd5r6TV5pI91Gxxu-5IX6uxn3VkrTb2s5FSb7bnBA2qWjsF6h-VkPmR6RaZG4t9C7veAao1n8P-2sRn_tyVCkr_ZEwUL7bu7kTbUyvcgJUGhDzfbRBd3bhVy_PuHE4ycYKns23sENntT1XA7lu2AxXzNtVtxe6rhq47JEgEu0MQqgitNMmiTMwSvQ1AO7GmXqv3lVdlJ4LEQjvXujPd7Jn-N5IY7mlUczqmU3uQqlTtOmNYrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا اینقدر طرفدار داخلی داشته و‌ نمیدونستیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101341" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101340">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101340" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101339">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqAeqpakEXfXZyi8hDVpzBVcPeoITC3QJfEISaV1ez5czhwI-z1GpKp4kDQRYm4F3ge-jJosgNtSFuLFAzN2FdCucZa3I5QLRQfw5uQ7fSSv6LLeLlVP2QEKd-MxqoCvvCEItKli1m5pp6Hx_5Az2LuxpoZp3fUsRRz465IRub9JzHviHyldY3iEmjPZoQqGD-IfFFRLFF31CZc0_E1v0BB_yOa4QFB7yMcZC8zhjLydlpgk5YMkEOkaggEsQb_thwOTdOtXf3kSpKijXk2QxWr-NX-smSiJ3m7CNrynf_LE8smvrsEn5Fm0sLQMpCNBBorOh_NZS8rAFxDhxg47aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101339" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101338">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVYJ3MUDGMYPrAKBsC63S86dHjFhcPg6HSkvgfutWG7FMi0ldTDnqXebeHT29YnaDKmqhmAPzFXAEdVXQ2NWNtBPtIoS3hMrAlflulgxsVDl5p8N0bsWABan6UMJ8lAgIaEv34i6yK8Ks9wgkz8o8w1R1Kma215KkgLG-PGGfaDatVN1h2OXK2TlW1M9OsAFZF-puI0mhGpT_ykyXTGxecvIG1I8zo2c30ldh_Klt1zzgvZNDYobtRaLRzjK1dxf3gHFalbrvx95iNH_OaWx_l_2wX3RaLXXwoTPBclcL6gMhI5R6dVDtGmwQSfE-kj3RbzFQFEDhicj01AAUgDogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی براساس سایت آنالیز اپتا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101338" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101337">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3dJeErSzrmhYCJ1MMkBrIQNqUsNRusw0CuR5Itpx6x61ETCZS0nwQv39YWSHuZ8fAZPCY8q6oOTTXRdbBZi8gzNKLyrmdi_XQjL1rnpLvSiSx5s8mXMa0KjNSYEZpWxxxOLyTi0hxebxZtyzm4hdsdfuUSwnejj8Zw-m4QSgplVofNkC3dl6_HD29HnHCtoNxUbMbabmIoA9rFlAYlGHtheJ-rgMbOsq0KvCPNYPfBD12uF-5h7kYdw-zphpLSFl7klPFkV53Enwg6cccnvP_Qkh-23oHpTiX7JUKi-OJVGiusv4UNDeY3ij6HciC0eHH4fvtwa9Xe3tO3SeJ4bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتین:
انتظار می‌رود مارکوس رشفورد دوباره به ترکیب منچستریونایتد بازگردد. این بازیکن همچنان به بررسی پیشنهادهای دریافتی از بارسلونا، پاریس سن ژرمن، بایرن مونیخ یا رئال مادرید علاقه‌مند است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101337" target="_blank">📅 18:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101336">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXMFgh2MDo_6SvHFX9nJ6rThM4QNAsJYeFgObKgB-Dd-p27Z2d2Q37mD-wa_kGubdL_mKTJItmDfUxbwJYsh8Z9ejUXPCau2WpZbKOgUj117qc1EK_lZTSAPTyXneggfhiLea_tEW-vxjUmN1W9yMKtahBheyjVRANSsp-PzeumJHFrEmsEBq7g0KdOxzHLzI1MNOSex4CQAoElylXDnMVOCqnyJhoq474u7jFnKIGc-m-8AaQU0XYcpOs6jB8DBW_SaYb73xRchBlZ9iWI51BVSQPoV2Gy1BBdt0t2CwiMX5b7jA1Tu8g-oZwA5U1R8sjzYy7oOWWiXUGD52jA-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست لیورپول برای تور پیش‌فصل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101336" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101335">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5737427fd0.mp4?token=H1x4r2JIZ83tjmMYaSOq2labiYNcbl9F-fJHEim1J31O5JyIL2h8beD16DVU5yYm3WOvVUNACiF_7t6TFa3ps_ZVwMqv3yMDwLRmwhLhn3Pwe1PXq-6KPeipPf95Fe6UlhUK3oAgP42dabzvbsOjpZoEfaMiTjLcb2pFPCZq_wqYK0cJaf0tR1Uxy6hfcBpL4iCN50Trgea3VcCJei5BDRAhZ2Y0aeWC8TgWPRVG_Q99-ugrbqg1Qb2TYfPdOhqgc_m7fVhDdWJ7v1DJW0mKSxqq-gxYz3tXKBJeCiLiTPR3q2Or_MS1P2WFLp1cjq089Funz54LWBj-kEZenU-FvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5737427fd0.mp4?token=H1x4r2JIZ83tjmMYaSOq2labiYNcbl9F-fJHEim1J31O5JyIL2h8beD16DVU5yYm3WOvVUNACiF_7t6TFa3ps_ZVwMqv3yMDwLRmwhLhn3Pwe1PXq-6KPeipPf95Fe6UlhUK3oAgP42dabzvbsOjpZoEfaMiTjLcb2pFPCZq_wqYK0cJaf0tR1Uxy6hfcBpL4iCN50Trgea3VcCJei5BDRAhZ2Y0aeWC8TgWPRVG_Q99-ugrbqg1Qb2TYfPdOhqgc_m7fVhDdWJ7v1DJW0mKSxqq-gxYz3tXKBJeCiLiTPR3q2Or_MS1P2WFLp1cjq089Funz54LWBj-kEZenU-FvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ اسطوره های بچگیمون
❤️
🥲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101335" target="_blank">📅 18:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101334">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f8e9bfa.mp4?token=b-CQzggisS-LDjCFoC6AKZG1267H3sTjFR-naTxsaLAgauPw48Ct-1koBhXFpC8ufdkEjj5257XtqT0VQwNlcPOZZ0p6YFCMcTxuQncqLisrGDu1yoRGQuAe1D1xw_6uLn1n6fFNQBNobEK5K22NYS7mnwplQAcGw7oWr_YB1XndNvSKa29Il0NyJj7VkuBX620xxE7atneZpu2-sjW31YhKr2pK5pF0UlO7Fdl5m_VoLmc2WF86_ibvRJ9nqtkWd2jp3T4fKakPRLn6aHktiiXz55_Gq9M5JWcdmhXda2e8Q4Dr_PhEEzZl0ef1gE6Ps3qCghj3lzDvg3SxcDpKEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f8e9bfa.mp4?token=b-CQzggisS-LDjCFoC6AKZG1267H3sTjFR-naTxsaLAgauPw48Ct-1koBhXFpC8ufdkEjj5257XtqT0VQwNlcPOZZ0p6YFCMcTxuQncqLisrGDu1yoRGQuAe1D1xw_6uLn1n6fFNQBNobEK5K22NYS7mnwplQAcGw7oWr_YB1XndNvSKa29Il0NyJj7VkuBX620xxE7atneZpu2-sjW31YhKr2pK5pF0UlO7Fdl5m_VoLmc2WF86_ibvRJ9nqtkWd2jp3T4fKakPRLn6aHktiiXz55_Gq9M5JWcdmhXda2e8Q4Dr_PhEEzZl0ef1gE6Ps3qCghj3lzDvg3SxcDpKEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇪🇸
نیکو ویلیامز هم تصمیم گرفت که مدال قهرمانی جام‌جهانی رو به مادرش اهدا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101334" target="_blank">📅 17:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101333">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd0e4aba5.mp4?token=NzgCGFdcNn7J9D91cJU0IaY1oYhxNfAULBWHtlVCNXWgrBDtJkXG4RlPfn_Nbp62cWzXEN-iT3Wrjelor9Jtjao1XoSQNDSS7XXssaIbsEcxhzfRmgJOYrE4acLg_8twp2fyj0Eir7xWwDsTN9fMUVY4RRgb_D-c6Ipn3J957DniEp3YQIYZ1VT5-AKEeOn1kP1cNxjrnSTETIvZTPQKTuPx30DcGBWXy-iXA7G5ZMhl6xW1UT1uUsJslFQoUEofQzhvk901pR-hWLwnR7_rK7N27pdCGJ2y1KHZ1vWhzGa9OP-H2M_cSNpkMywXcOrXJ_iUaWbRdKpOEzfEmwZe9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd0e4aba5.mp4?token=NzgCGFdcNn7J9D91cJU0IaY1oYhxNfAULBWHtlVCNXWgrBDtJkXG4RlPfn_Nbp62cWzXEN-iT3Wrjelor9Jtjao1XoSQNDSS7XXssaIbsEcxhzfRmgJOYrE4acLg_8twp2fyj0Eir7xWwDsTN9fMUVY4RRgb_D-c6Ipn3J957DniEp3YQIYZ1VT5-AKEeOn1kP1cNxjrnSTETIvZTPQKTuPx30DcGBWXy-iXA7G5ZMhl6xW1UT1uUsJslFQoUEofQzhvk901pR-hWLwnR7_rK7N27pdCGJ2y1KHZ1vWhzGa9OP-H2M_cSNpkMywXcOrXJ_iUaWbRdKpOEzfEmwZe9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های لیونل‌مسی در حین تشویق تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101333" target="_blank">📅 17:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101332">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e0946a77a.mp4?token=vanV0WtR_K-hC-ydV-XQu_TvLZa80vecxE_zgmtw5z0Uw_DW3TeylSFWw_PY5SdP7jRb8vSiChOcVffiitrEjRD7q6sHnjoJhqYYs8nwjQSS35czeE71U7y69D-HlfM8Lv-26F1zEfIcth0FGhO-XEKPl0SOh862q-_uQX4HKehsyC8CL-wrkl-KNOdV5wZOkG8Hu8YSt8y-65Fw5TGdU-QdNJTIE0B5kPITAC1L7BbRA6VscVcbNj7HNmYUCydaVMiyMe8y5jLwMX48_05FvstnHnnIvAt89ZChqs6aYYwnUja1fTqcjQnsKPX4UeaVtUgDiBV1bw-s1BoewKHp9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e0946a77a.mp4?token=vanV0WtR_K-hC-ydV-XQu_TvLZa80vecxE_zgmtw5z0Uw_DW3TeylSFWw_PY5SdP7jRb8vSiChOcVffiitrEjRD7q6sHnjoJhqYYs8nwjQSS35czeE71U7y69D-HlfM8Lv-26F1zEfIcth0FGhO-XEKPl0SOh862q-_uQX4HKehsyC8CL-wrkl-KNOdV5wZOkG8Hu8YSt8y-65Fw5TGdU-QdNJTIE0B5kPITAC1L7BbRA6VscVcbNj7HNmYUCydaVMiyMe8y5jLwMX48_05FvstnHnnIvAt89ZChqs6aYYwnUja1fTqcjQnsKPX4UeaVtUgDiBV1bw-s1BoewKHp9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: کوکوریا و بعضی بازیکنا قول داده بودن بعد از قهرمانی تصویر صورت تو رو روی بدنشون تتو کنن⁣. نظرت در این باره چیه
🎙
دلافوئنته: کار اشتباهی کردن که قول دادن اما اونا به قولشون عمل میکنن چون آدمای متعهدین
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101332" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l48lGb-U6GyuRWLxu50Y6I0L8XfrhlCWx9WsG6Eeu-z7JeMj2br1-iomqA7aU32wAIz_J8qiJRAB6o6klYh9DZ6NXaufDJV5LIjdoZ9TznULTayzKE4NEka9juVLRrDe8S8k0uv1FHWi1gkD28B6zeSLwuj4mRKzw6iiS2Qm51Tir3DxDyuY-Fl8lO4ydCFytT5-dGp4Z_9JudprrEynblwWJ053wniFl1EQ1uq2zr4DiLa10lPRH74aUGJd_31ws5IespKKB6JE_A0lRsBDPXkJZ8S7BqgA7mJZhTJFOnUHQeV6GEDQAbq4FzoK597UlurhQTgA9-JdS-xWl8znyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسکای اسپورت:
فیفا تحقیقاتی را درباره رفتار بازیکنان آرژانتین پس از پایان مسابقه نهایی جام جهانی آغاز خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101331" target="_blank">📅 16:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3ec6d627.mp4?token=PBrJ_XBMr_xAEay_pk7GGocjyPplMpZ295F8BLBQ5zGETywLXB2_UK5ZHTDeVICyC3lg4SYq0k56jA9Zfi9j-PH1E9RjtK69SbqvRIlQbvmgsyD-5feBJySMV3BuHvY4vDnGklxACwmnJKXwr_DVQGb6lmwnBfwsdr9ZtjJkOD8cqPt8Ew44usdNhXNrTbgr6QiMnIIlIyn69ciNnasHy9woHaXWpWSkGZ76mIoAtg431PKgJBjXkVCuWTLVCAEiTvPh1Wa8DOJBP1_5pTFOMO5Am3uW7j6dH283zVDN0P2D8CuIq-mI758FyZGEWwwb_bNRTxZCvITUpMbW4iXDGIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3ec6d627.mp4?token=PBrJ_XBMr_xAEay_pk7GGocjyPplMpZ295F8BLBQ5zGETywLXB2_UK5ZHTDeVICyC3lg4SYq0k56jA9Zfi9j-PH1E9RjtK69SbqvRIlQbvmgsyD-5feBJySMV3BuHvY4vDnGklxACwmnJKXwr_DVQGb6lmwnBfwsdr9ZtjJkOD8cqPt8Ew44usdNhXNrTbgr6QiMnIIlIyn69ciNnasHy9woHaXWpWSkGZ76mIoAtg431PKgJBjXkVCuWTLVCAEiTvPh1Wa8DOJBP1_5pTFOMO5Am3uW7j6dH283zVDN0P2D8CuIq-mI758FyZGEWwwb_bNRTxZCvITUpMbW4iXDGIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت داداش یامال در بین ماموران امنیتی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101330" target="_blank">📅 16:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm5jb8dJhoxVn7HPZzu--pO-AxZX0Bdm-LtRMRk3TTlLFZcwiu9cf1R3WmXFLtbJF--LqQkYojY17d3hTWb4-j4Z6awzdb0SUF1nfAEg5xfGWtc2JaZbXDGiyGSOiAQFIBn55W4nVGSCBOOADybI0uz3AnmGDO1mZGrRRCrhhX8rpvPClMjAHmLZOv8A4A90x2psXJxDxx94rNbIu1cwn5XvjnlET_To1IN4n8cg7YVMwtwGc9j5sLNkr4Rw8AxRWV_WCewMatS7DNFTg9YyVu_zLsUhK9Sa87x5OsO-U3_gTqTGYOMh8vFB8t5EV_gR5ktLhfij90qpE2BUL8u2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
قهرمان جام‌جهانی به کشورش برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101329" target="_blank">📅 16:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHiwzNhCw6yeVIPPKdZ2tHdCaWa8J8vZ8VymxTtw3at5oJzvvQnhhQpn2NvTRDcuMDyFo8iNPWmUc6dosXIi-VxLsDU-XBRLJrTMloNgSUoiUau0QfuK-xHp5eOkvTyvJV5gqNc3TineI72yx_PW898S04INS7iY3ktWAdTcQPHb8kDNIg3fcuJxU4e9YI7m2B6nvpcFQWGcBt_U0l_NZH3o9XXfq9DW76vGYkZb4rI5xDvvF41wHA7jG2KsCtRPCW-ZhBMw6rhjA86ZzG_1ul7Tf-p2mGyGn0SF8VNqezEYCXSolOJ7No1DDY5hV0BUlWyzEHYcTrGAOWOA_16NyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
گاوی و بانو در مراسم دیشب فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101328" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101327">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvH0Yk-LNba1cBTjw7IPapivwsJJKzRi8ghuxYGyS-gP64_PENDj-PaOlx8-xx1ACg6QGonTLuohwCij5C_W68iuY6_qtF7nieY8VudHgdpcgeeGefnVzawK7x-zNZsaFbn-nKub0yACyykIgZqLOXJXTq7sLK4enF5aJDTfRjZCH9Ndaqpb17g9UOYnFFWTurAUObmMdEA_acWzrpJ2dgMMeIcpdHkocF-FOgvsTtkqXf4Xw_MCSjRRN_THnHpBMgZMoRRGcAz6RL8WqDFSAoNYevj1ys8-1AoVOIBUss039tJiowryWZS_ppB-d3QrrIULLdPav1pogb-fWSfLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رودی گارسیا از سرمربیگری تیم ملی بلژیک برکنار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101327" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101326">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be537ad6b8.mp4?token=I6_85CIJJ0sjr0M--7gQZ4Sq9sGMYQxaO6yN3QAomOW3nwVT3zvMpp5Wbc2O6xZIHR0oMBGfC9QtWs4xcu5khuJbNKNbFdZfjo1cf6yImqDyLgwHmZAlXL2yv4x-0fbrCmSVF-cHsgg_CAxebIk6ZGfUNcaoMpROpy1rsr0jWDx2giJ7NL4ONB1Ry7N_tFVHtTqkNJK-9pzqoORgZzwv224auUFuLkDCvOwWptew1Wr-bfBnW3lLmfxbi30KFevq-ZEvDlCPX2rSIJl3t7kqvlS2XSrF3Nm9w3SOq8gb19-0iEitMS4DaeDBcXoTIHJSwbHgIepgE2WF9iKw7yi3ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be537ad6b8.mp4?token=I6_85CIJJ0sjr0M--7gQZ4Sq9sGMYQxaO6yN3QAomOW3nwVT3zvMpp5Wbc2O6xZIHR0oMBGfC9QtWs4xcu5khuJbNKNbFdZfjo1cf6yImqDyLgwHmZAlXL2yv4x-0fbrCmSVF-cHsgg_CAxebIk6ZGfUNcaoMpROpy1rsr0jWDx2giJ7NL4ONB1Ry7N_tFVHtTqkNJK-9pzqoORgZzwv224auUFuLkDCvOwWptew1Wr-bfBnW3lLmfxbi30KFevq-ZEvDlCPX2rSIJl3t7kqvlS2XSrF3Nm9w3SOq8gb19-0iEitMS4DaeDBcXoTIHJSwbHgIepgE2WF9iKw7yi3ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خشن و اخراج انزو فرناندز از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101326" target="_blank">📅 16:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101325">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936d28a634.mp4?token=uE3fRWvN-z6S6vkVFXLEuE23kVhCSQwA9HgHhlPUfCcyLuiW6e00JeXpG6zp2UojvbmesYjB6VuBHw5dTixl43Lalx9ch2MYmIJ_zrlaF0XU__DuAI9dbskEirsM1ODJ6KBsXder6bRE9FGcfjJU8rgJ8nGJ-q7AfTXJP5Ry5PnG0f1FKFWuQnQEV_NrkrMt7ifwEOzDzw3ZdOhafkVcXH8TmzU1o1u3aHfKvDRd-vQ9HTSyQi3Xll8No2kUrQTfOOhCzqGQVTaGpomSbYS67cWQWHr2Z6LCIgEF05PRwR86UlMXyjYCwHnVgZoZRPqZEcLyY9xqpBy-Q_m2F76rig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936d28a634.mp4?token=uE3fRWvN-z6S6vkVFXLEuE23kVhCSQwA9HgHhlPUfCcyLuiW6e00JeXpG6zp2UojvbmesYjB6VuBHw5dTixl43Lalx9ch2MYmIJ_zrlaF0XU__DuAI9dbskEirsM1ODJ6KBsXder6bRE9FGcfjJU8rgJ8nGJ-q7AfTXJP5Ry5PnG0f1FKFWuQnQEV_NrkrMt7ifwEOzDzw3ZdOhafkVcXH8TmzU1o1u3aHfKvDRd-vQ9HTSyQi3Xll8No2kUrQTfOOhCzqGQVTaGpomSbYS67cWQWHr2Z6LCIgEF05PRwR86UlMXyjYCwHnVgZoZRPqZEcLyY9xqpBy-Q_m2F76rig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این ویدیو از تفاوت رفتار مسی و رونالدو از دیشب وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101325" target="_blank">📅 15:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101324">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjR5cErqI4co7g80sQ7G2LcAEd7ftRwAw4C4LkM0iMjxSZC-VroXpH59Y7aVh04MoOJaGE5fS8Mpfa3-zYB7aaT6JqA7EE4dkVl6llbbxPKCEFmpmrBwVHe6h-QnWsOjIsiAETYil7C5m0Vkx_md_xvXWvu49EqcS20B9j3Od9R0sgiC6Jm-8y2u4xANfzFE2GZcgtMoEUBZHDgzDe5MmhtEKpUNK2OUnzWWQ7daX9EnXG1imvNdJ3ctTecNJ1rlvH3r0k61gn590RSrS8GMn2nQ6zAxk89rG8to4f8g2s-5yFr8D8ewTbAmsqo38LP-nm2t9cObIDdi1XBhBLUmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مارک کوکوریا:
قهرمانی جام جهانی و انتقال به رئال مادرید؟ این یک تابستان بی‌نظیر است و من آن را تا پایان عمرم به یاد خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101324" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101323">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46470a010c.mp4?token=nIFQl6faqL-rxIg6Wt8BQSncS4yhFAUaNEZ7IcXNFdeirCdbEr-dG9tkWAN2IRFmQMiGekbptZ8Rimm0uIbPLKTyExnJFLm1E26xTv5tv1a7hcGsaWkXkcM85U3gnINILOah86Lv6u3CQrVG8b2OkOfMELqNoTfEFzsCXjx0jMRDdubswFkWBfFm2gpiLR77b7Y3GlePjPm1gzqbSRnAtPibNA8vUEnDH_srkyBKK2jN9lmZm4pfsQjQrsiJxCHEVdnyJxe76WahnoPjHPqxx3_ZNnDMI-2CkqB6GG1_q-iaHWoAYnaVDyg432m4b-e7YVML81ivAssRPM-oQBUdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46470a010c.mp4?token=nIFQl6faqL-rxIg6Wt8BQSncS4yhFAUaNEZ7IcXNFdeirCdbEr-dG9tkWAN2IRFmQMiGekbptZ8Rimm0uIbPLKTyExnJFLm1E26xTv5tv1a7hcGsaWkXkcM85U3gnINILOah86Lv6u3CQrVG8b2OkOfMELqNoTfEFzsCXjx0jMRDdubswFkWBfFm2gpiLR77b7Y3GlePjPm1gzqbSRnAtPibNA8vUEnDH_srkyBKK2jN9lmZm4pfsQjQrsiJxCHEVdnyJxe76WahnoPjHPqxx3_ZNnDMI-2CkqB6GG1_q-iaHWoAYnaVDyg432m4b-e7YVML81ivAssRPM-oQBUdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قهرمان یورو در ۱۷ سالگی
قهرمان جام‌جهانی در ۱۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101323" target="_blank">📅 15:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101322">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55be40ae63.mp4?token=kfNBRx6l6XUQ7qcw5wK0T7TqD62FBWrletdRZ0HtZqmJLNF6k7As1e9PP_ZHMUbL6IPpWNzq--hPe5E6gH48a1tKLx2TMqHFN5mmQuUZmS6_lyBYFTnDhD2tVSXvArNSmUVTYKcyaCIC_E2re4k64Wf5hudKk2aUVyO_9U3TBwgymdPtqeDK5DjlR8ow1qRMpN81teB4SxqENlXKsocJyaupADkX95nAF-20glLvfUyXroluCwk8Rk3sbRGgIae1kQ_LMoaGXbs5SDViAMRlgh1FbqCE-YduCDc9zmqBUW1KBwicWvMkqjRthTUfL3oeKOOv6P3FKLXAeNiHzMC1Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55be40ae63.mp4?token=kfNBRx6l6XUQ7qcw5wK0T7TqD62FBWrletdRZ0HtZqmJLNF6k7As1e9PP_ZHMUbL6IPpWNzq--hPe5E6gH48a1tKLx2TMqHFN5mmQuUZmS6_lyBYFTnDhD2tVSXvArNSmUVTYKcyaCIC_E2re4k64Wf5hudKk2aUVyO_9U3TBwgymdPtqeDK5DjlR8ow1qRMpN81teB4SxqENlXKsocJyaupADkX95nAF-20glLvfUyXroluCwk8Rk3sbRGgIae1kQ_LMoaGXbs5SDViAMRlgh1FbqCE-YduCDc9zmqBUW1KBwicWvMkqjRthTUfL3oeKOOv6P3FKLXAeNiHzMC1Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😐
چه ابهتی داره سرخیو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101322" target="_blank">📅 15:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101321">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhYGk8l8Oo73nnDxrfDudBXgRi2Trclfzqi_IzZ1VtIvlXWopSV1STB-PWLs1_xd8Eefb8sktzk_tlvGYZtCqKsmvn_rDtNWYCoP8Uxgc5gcabbv96AGYbB0ge_uSyKnjYOkvDVjNk3GJv-Yip6eXJWuoehDCBafo3WE8XKncf__rOUV1eW271CScPIBI-lee5gdWfCp3Ks4C5Lf93_EwF949FMfAxDiGfVZLMq29h_ANlXCke3yocl_y-hzEkg_IWx9EoDyG6kq_OkYV6RpHGGnxHQPw5rrTQP1rxEWyjqjjdN-KT8DUJfSrbnGV0TWccXwOad_MqCBUodKXCmt1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیونل مسی اولین فینال خود را با تیم ملی آرژانتین در غیاب دوستش، آنخل دی ماریا، باخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101321" target="_blank">📅 15:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101320">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYluZ0vx0s2DO6EPAPsarq6VuO2EIJ5bEAbKC1JmA5Z2gRIUChJUOr8KiD6OcModfcSm98hBUkAwymo7_I_CoVR_iIFEbBZh6rrGrHMrKtDKw2AzAcCpkiAsUESkfPrF82eTwcngpPGfQevQ4zDTRR4z4iliHaCqEjwL6EtRpPfj5nrTKvU-pLdbJ8-gxpuC7rhkfg5OBzW5toke9uGtMvNPROz1qfpNFC0QjkOYACWp9pCJefb9GJHP_2HdAdKMhKrCkq_Dkavfd2vDqoKrg2-CITQra2SM5FLgKWrQm_VO4mKdw4dHkAPXFj3bfO26gviwpvSOL2lmbUBfH3nLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دی مارتزیو:
پائولو مالدینی و لئوناردو با پپ گواردیولا ملاقات کردند و ایده سرمربیگری تیم ملی ایتالیا را به او ارائه کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101320" target="_blank">📅 15:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101319">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a4e613e2.mp4?token=rOcpLgqwU8rQpfnr8HCV-VsATSoPAxeVp2qRDyZGY10XyZPHCk79qpZFp4rWtUJabzOLNGCzw2vgzKpMUBemEEzAhMUdRklbj9neF9a8_1RlnqYG_JzuXW6E6G3VNLgXSVgshxhU1IPfjtvdlgIiHdbrDParvF1Y3m4ZmCtqDoHbdbEBITeDQS7q-imXHT_9yMM6McDjdwf5OELb1gb8kCUTvVB-DehzxWohypwmv5GLQKr9llQjyL5Pk_maIft-H6zkdyADHakXT44XoKU1UimTCkQE0t6oGQsBkwzLPwB1DRWkmnacww97_9jbiTasd55slZEeV3Ff9Da8Rrtf5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a4e613e2.mp4?token=rOcpLgqwU8rQpfnr8HCV-VsATSoPAxeVp2qRDyZGY10XyZPHCk79qpZFp4rWtUJabzOLNGCzw2vgzKpMUBemEEzAhMUdRklbj9neF9a8_1RlnqYG_JzuXW6E6G3VNLgXSVgshxhU1IPfjtvdlgIiHdbrDParvF1Y3m4ZmCtqDoHbdbEBITeDQS7q-imXHT_9yMM6McDjdwf5OELb1gb8kCUTvVB-DehzxWohypwmv5GLQKr9llQjyL5Pk_maIft-H6zkdyADHakXT44XoKU1UimTCkQE0t6oGQsBkwzLPwB1DRWkmnacww97_9jbiTasd55slZEeV3Ff9Da8Rrtf5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نمای هوایی دونالد ترامپ از استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101319" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101318">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TazVIcPH4KFqL9p4FxHzbaMQmesyEBS9N3d5lr6tTSDJ24rmJ4LJStg9OvHREAkYpVaQevH7m0AMS85JHn8cT6ZxuiWjU9AQaGgg3eYhep0yfCqBpVLHJeGpOMW4MZTe96wPKA1XL06GeLVAQ_rQohJj9rtw-J_el5c41j0z9PyPLMJYpmZUBTekOn2fLL2GV8qw_xuVHlUXq4XjEqlwZflogo8B_G7CoDCMk1eKdMqywzFSW7Ru0gvGLj17rOpepj4_ADRkTspJnHQl6DZGhL4vTelDQPFwRkYgSci5W6lAXtq2LvI8unVsyDYfdLfPrp1U_pviYW3HbsJakirWZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کیلیان امباپه در فصل 2025/2026:
کفش طلای جام جهانی
کفش طلای لیگ قهرمانان اروپا
کفش طلا لیگ اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101318" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101317">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101317" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101316">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfLDrFPYEwadg-Usz7lr-60poiqltJr_2QG0TpNEUQf7t3LP7wEvaz1Kvi96JRgFYvPJ41hPLHjahn1THAbKKiGcXtVcf_iNYWLibiaB2hDgZBVmFKPVcsR_HXsWW0MyfsaFAlLAbZxpR7f71ks7hW0KFZI_S-8bM45XZ8mGM5lGsOyLOECSMDOkZiv_IWhPnGb7sjT6NsIBFv22kCH5zVwEEvz2lJnflef1_QKiYlQHhc6Kk0u1yAI4pZ_1i__O-ltA8B-g2MEu9d-Luf3U8H9wdDEJO5Xk5zDRrY94NG_SrTKG2_Tbh2_wPBvJsXT8F1zxqIUDbPK2WnUL0L87HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101316" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101315">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=XP9bXLRBaac9d6yFo66Q3r7fhBnyDPXTHUxJXZUvQtEwA72asbK-PyEHss0VkDYA5PbZhZxO-drSSdxrlfwtZoqfDspx6C2ip1rpQGDIcmTWO7lItl6WhIWJ5xwkG11kLuRir155m7hVcoZg-uouES_zXBdK5bXjw2B5EHW2ygJJauAJ3TPrLgo_aRJmBIxCxnp5R8xuRX_xguZc_jT8gCLB4qNaSrAqV8RqQoGvx-mTo5H24X2W2RAilCitZVqoV8IYXvgaTTcfrejnx7n58QBProx3A-54jBNWS3oubJDq8xi_yWEfwv88YriCpKw-emhJ3Xhq5nsUsG1ZYC0FaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=XP9bXLRBaac9d6yFo66Q3r7fhBnyDPXTHUxJXZUvQtEwA72asbK-PyEHss0VkDYA5PbZhZxO-drSSdxrlfwtZoqfDspx6C2ip1rpQGDIcmTWO7lItl6WhIWJ5xwkG11kLuRir155m7hVcoZg-uouES_zXBdK5bXjw2B5EHW2ygJJauAJ3TPrLgo_aRJmBIxCxnp5R8xuRX_xguZc_jT8gCLB4qNaSrAqV8RqQoGvx-mTo5H24X2W2RAilCitZVqoV8IYXvgaTTcfrejnx7n58QBProx3A-54jBNWS3oubJDq8xi_yWEfwv88YriCpKw-emhJ3Xhq5nsUsG1ZYC0FaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ دیشب طبق معمول صحنه قهرمانی بازیکنان اسپانیا رو ول نمیداد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101315" target="_blank">📅 14:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101314">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=K4qYEn-Y1rMCW4oV9z-ejsowTlgQ5MZTL5xeIrMfwD1eZxe_yRuprSuGMwvqqj4LVqVZHCOemuTo6_VjJeioIqKD18WjSjwZxE51_a7N0draTl4t8bOPC-r5pLCaWN-XYwfkwHWDDtM3Y0kiynOpjCMbgofbTGylvPxGrI7dTil14Rbew7w8sYB8ycdi2zSKbbr9S8BZKpD78GRkSzUEe0DroJlsbxgZJ_Qed9oEB6pq5JqxgK2XRWSiRAotaAk0DRb5oqpUnRsbQ5ex13404PM91bUWyBO6tmG5JKnHE7QNV3ogWbH59t6SFMopBhzIIcQK9xOD-Gs0YcIxGidFVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=K4qYEn-Y1rMCW4oV9z-ejsowTlgQ5MZTL5xeIrMfwD1eZxe_yRuprSuGMwvqqj4LVqVZHCOemuTo6_VjJeioIqKD18WjSjwZxE51_a7N0draTl4t8bOPC-r5pLCaWN-XYwfkwHWDDtM3Y0kiynOpjCMbgofbTGylvPxGrI7dTil14Rbew7w8sYB8ycdi2zSKbbr9S8BZKpD78GRkSzUEe0DroJlsbxgZJ_Qed9oEB6pq5JqxgK2XRWSiRAotaAk0DRb5oqpUnRsbQ5ex13404PM91bUWyBO6tmG5JKnHE7QNV3ogWbH59t6SFMopBhzIIcQK9xOD-Gs0YcIxGidFVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🔥
وضعیت کریستیانو رونالدو هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101314" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101313">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=pebhQLkwwYrgA9yo90wpjlGIcYDxvFPrhfcDZypm6g_GBRZY2_oob_ExgFc7QLR07mQqVcden9herHSvMgpk65CvtZ-365-bZUM4fE8VufSWSMW2xtq3tamC50mDWN6z10QDktIEl8nKILm0RJuCbZ6MmJxHpiiAAwHl2Jx4RsgOncyXoxvvMaLpfArNX1ZQC07CV4aPeL93G1CJh-qhBybnX5_xbAqHVODAplFbAa9usBz4PGekst26ThShQxgXMGQ7tKBUn4L7xz_hEL9GGAkqi6Ll7yGhtdujG3OLsO2mh4UKGIqKVkUEL2xZrPi3enUyS83hsca_VTg0kR2xMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=pebhQLkwwYrgA9yo90wpjlGIcYDxvFPrhfcDZypm6g_GBRZY2_oob_ExgFc7QLR07mQqVcden9herHSvMgpk65CvtZ-365-bZUM4fE8VufSWSMW2xtq3tamC50mDWN6z10QDktIEl8nKILm0RJuCbZ6MmJxHpiiAAwHl2Jx4RsgOncyXoxvvMaLpfArNX1ZQC07CV4aPeL93G1CJh-qhBybnX5_xbAqHVODAplFbAa9usBz4PGekst26ThShQxgXMGQ7tKBUn4L7xz_hEL9GGAkqi6Ll7yGhtdujG3OLsO2mh4UKGIqKVkUEL2xZrPi3enUyS83hsca_VTg0kR2xMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
The end of an era..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101313" target="_blank">📅 14:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101310">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1YWGhespi7lPg_OV2esqF6UBwOKkokg9d2R6ZsUbdf2W-NVrJdUaBQ6BhPYgwL9heBDYD7-WyQjXX7uDR9CL1DFYT5sVt-JjF728iasAbHIsUaeTu8NWPVV5kuJKQ06TeRf79YqQk6vesGYNmAMCrfrP8gai7zqXqVyCZJkdYIngRON57fj6tcA3MRq9guItbrGCAMClBV-_UZvKNKgtahoUr8ngNiBG4sGNE7OoFcehuixMwOOQqjnfU8WpzVUTKvP_At8qow1vDDDPHZa1bGvsn0DK70gOALXA9aoglf4Da2VHd3YD24D5yMzhdkA7l3A86Mlj5U9Al2V4AVHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Clj1pDziUrWIaA9c-eMVmtWwdA4vq_LlNJGhEe8TrpwlVlvNLbXQr2LQbVzZzQmtR-FEY3WgeYxek9VhFzqjhVE0-OayFKSWm35y78Gao-tDCxat8xWD8dIGaqyCd3ykChwTMydSmfFDXWdQsBPU4JFQv5hIO7eOZs9hL99yaXDYfLGrt7WSSzZWm23_apmV9BFWGmqEnJwThdsI_b6LbFxaNS57ATR4KMJFg7dKPMntHtvF4GduabdFcN-YVLarRLfmbC4ngBTsRLv13Rzpzn2LWW4OpVim7ERjctDz7rmioS9qVVnNa_JibhOwqskgwxHn0zy7-t16Y5z7hS-Mmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHhp1GAoz_LtZkAwPH52biYsSU9Oo4nk4AVCyAvK8teH79yUtkDpi7itXhmC1zbJmnRMJGOsXFyTHUbktIwPgIMIu1MgzMY2JzdAN8CLAdRQ4kYe1IQLWgwieeK7UTj3A0rQn4hbrsPye0yBUPuwrnNMhnzo502AK1ixhZVCj2z67x_9Cg0b4Nn9oPATjuJTWaRl9TQQZPq5VoEbizOYPK2gDpuGNlTU_1OKP_cchPrfpfOH3ysbnPfbySOqukGda_vJklYceeh9uTWdC2dH4TVCzqax0dPz7rytNV8u7Hv537wfWyafTSd--vMwPM0PJCaYqcrDaBQ5jfiqJX3veQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😆
🔥
کوچولوی دیوانه رو داشته باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101310" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101309">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-WCJhWcI4_g-HPQ4CZW-07EGa3-TKmQE2b7gcwTIHl2vGYjprMaVtcIOCLzboUpE24XRnZXkN_zx8_tYL557Fd2SBRbBzvgz6s2j1CbtazueaYgGhtaY4kb8qd_eQCD3QQ4kabKgRgKGiWN5mHrwO3n4-rkTTuaba-FCvJbMawtkymQ07Y55ByxNjOucT4QHif7rIWhvP7U4S4vgw6vjv73KDek-eMwGs6AqZcgdzkzpzkDypBpMMNDSqQOT_8Wpz7RZahYe1oc5Xk_iQF08X3dUWGgj8OyeDLifsOgueD1Ti0IlSi8uYf8kUEkJTCVajcgdnOIrT1fIvz3I3DfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
😔
🏆
تنها 1420 روز (34,080ساعت) مانده به آغاز مسابقات جام‌جهانی 2030 فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101309" target="_blank">📅 14:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101308">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367be64c4e.mp4?token=v7DfxyL3iT2RRpf6FMhBd_oOX1abPBe6WcAmMRN9GSVq31zPnQBr8UiVf56KAJZWnMZ7i3DUlc56ce0HZF8YUvUCF4H_JrK7s5tJdszWmDjO4ubU1LqI_ugW5VOm2LOBL03mMt9CNwhqfTvBhk2lhWl6b5vxOcNjCat8PlQ4ohIs-FNBhnJiUakzUPhMnL8g5COKg47nPPJiMLHu_1BnorEKbYb2p3bCvnVXIaI6LWPDUZjtisiqJy0fwGI9cLn0c8BLm9weBPVySkbIcGwtVKZXDq8P1MxibCru8LYc0IMzLnkQojMetqiAZwRJclAmfzBFNglvot7B6UDwe5OhBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367be64c4e.mp4?token=v7DfxyL3iT2RRpf6FMhBd_oOX1abPBe6WcAmMRN9GSVq31zPnQBr8UiVf56KAJZWnMZ7i3DUlc56ce0HZF8YUvUCF4H_JrK7s5tJdszWmDjO4ubU1LqI_ugW5VOm2LOBL03mMt9CNwhqfTvBhk2lhWl6b5vxOcNjCat8PlQ4ohIs-FNBhnJiUakzUPhMnL8g5COKg47nPPJiMLHu_1BnorEKbYb2p3bCvnVXIaI6LWPDUZjtisiqJy0fwGI9cLn0c8BLm9weBPVySkbIcGwtVKZXDq8P1MxibCru8LYc0IMzLnkQojMetqiAZwRJclAmfzBFNglvot7B6UDwe5OhBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکیرا روی صحنه ورزشگاه، پیکه روی سکوها
و ساشا در حال تشویق مامانش، در حالی که شکیرا روی صحنه غوغا به پا کرده بود، پیکه از روی سکوها فینال رو تماشا می‌کرد. و ساشا هم با تمام انرژی مشغول تشویق مامانش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101308" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101307">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b927fa3e3a.mp4?token=OUWeUY5Gvv4zn6wfUqQNP0bQS4OlXJ3tKRSwqRlH-7fB1Jkp_nAeg94_4za61noUh_KxdeJG_hvCEH_WupBQmdpKciycbqeAPli6AwFLutHxcsUqkPqRCY8XgbuEDaq7LuwOaJlels94swrYDrD5MprvS5Q1yjVWJD9PHJCahgjtA03oxHdewoXwWA0MT55LpYDFJgnlwAus3Fr_dQoCRilcXNMSdcP8L_7tkKgV4gpxHb9chOfMICV8PSIOjcJqlGz0uJfOrzUFnynUcX71b_Dn4yOiQtcoINlI3ZDUzj8zp-GhbSfnFZja2AumxIhqZ4pGPrpQGd3CD4627CjBvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b927fa3e3a.mp4?token=OUWeUY5Gvv4zn6wfUqQNP0bQS4OlXJ3tKRSwqRlH-7fB1Jkp_nAeg94_4za61noUh_KxdeJG_hvCEH_WupBQmdpKciycbqeAPli6AwFLutHxcsUqkPqRCY8XgbuEDaq7LuwOaJlels94swrYDrD5MprvS5Q1yjVWJD9PHJCahgjtA03oxHdewoXwWA0MT55LpYDFJgnlwAus3Fr_dQoCRilcXNMSdcP8L_7tkKgV4gpxHb9chOfMICV8PSIOjcJqlGz0uJfOrzUFnynUcX71b_Dn4yOiQtcoINlI3ZDUzj8zp-GhbSfnFZja2AumxIhqZ4pGPrpQGd3CD4627CjBvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
اساطیر اسپانیا در هنگام گل‌اول به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101307" target="_blank">📅 13:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101306">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRI82NRiHVlBSUZ1cU_MvdH0P8c8gYk5fA0l6nx1j2y-E5Fhh7lZpWrio9_pcfCtn68k5IS7j-o8GdziofESJ1ZlEy2Hb17r0Lj0FF9C2lpQJiv6L67LrZhRMNjJESzrktV3iKkHV48vjhXOXof1Sl5qaw4x7HWMvuFq8ExylIUCOUgvrrUAjhP6wVXiym7RBNsy38L7SsVC0PF2AREueO2lHllu_MdAqbzHNk_LD34S22EZb9zQbe_uhrMxhongEV3JUheWmc8eRcbhkYz02jqWWTd5NfWrjWwRHOcC88XK-vedyeASff1GFoYlg1nqooXRP-M97cwBLbcbTjcHmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
رومانو:
رم در حال آماده شدن برای سومین پیشنهاد رسمی به وستهام برای جذب کرسنسیو سامرویل است.
پیشنهاد دوم به ارزش بیش از 45 میلیون یورو نیز از سوی وستهام رد شد اما رم قصد دارد امروز دوباره تلاش کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101306" target="_blank">📅 13:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101305">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cd4848c0.mp4?token=c92zZ0rok9sqEDf7oHlIkfm3q17iFz-2Y415QpO23UR35IruyDn6iWRRi5UEz0snXqQmmqmEsvXCJLNFrz8p5dixBxxsd8wlDpNQqiLCch-CLZL1c_XvlQAk0T8TPo6Buvk73Ya4BmfuNTPyq5-yoJfxQfbX__WJaVP9VwP2UahVUTJmcGl1SBqnP8GOgVlU4266gnpcO_gsBH946HYwzZw7J_VWFN0SELFq15XowiRmMFURSHERHrMF68RKdZXloEGWymdxrcu11Qpq2865sctjMXRO73pqrplSIilovAPwcXrFx6rGInsFpIN0b2FeG2i3gb8ewmcUI1SizlXqjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cd4848c0.mp4?token=c92zZ0rok9sqEDf7oHlIkfm3q17iFz-2Y415QpO23UR35IruyDn6iWRRi5UEz0snXqQmmqmEsvXCJLNFrz8p5dixBxxsd8wlDpNQqiLCch-CLZL1c_XvlQAk0T8TPo6Buvk73Ya4BmfuNTPyq5-yoJfxQfbX__WJaVP9VwP2UahVUTJmcGl1SBqnP8GOgVlU4266gnpcO_gsBH946HYwzZw7J_VWFN0SELFq15XowiRmMFURSHERHrMF68RKdZXloEGWymdxrcu11Qpq2865sctjMXRO73pqrplSIilovAPwcXrFx6rGInsFpIN0b2FeG2i3gb8ewmcUI1SizlXqjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
خداحافظی جواد خیابانی با مسی و میراث مارادونا با شعر مدونا: هرگز انتظار نداشتم اینگونه شود، برای من گریه نکن آرژانتین، حقیقت این است که من هرگز تو را ترک نکرده ام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101305" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101301">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fy9N7_Uii35UbrxVZqGvTumI5o-uK8XRBFDSllW_hliVRWlqJq73uX7NdHqSk7b61W2DSHXCPMF1hPl_aTTgp2BrLEJUruLOgIkyjAgPddQGhIxSygFkzAUtltYSQWrwdhFvvtG27-QSGSx_ze6OG8NXRlSeAnShOtA9mNbt5JtJ-9sS7pWXeIpbSGGJS1B1TRaOu26gXqsu-YlzjYas1YTBUaqMS84gQlTaB8OzPjMfdSjoCFmTozrHB3VNgBFc9NF1p1gDDhyHdoFf93pEUJ0cYz4BLN8X3frLaenr350Ya6fQThDgxZSQ9dAgBDzWHLepf2x-Es-7d17D_qiHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gu2sJkZjyTd3dYoAObce2aGeZeEfrEAH3T9q8hoIdYGet3MeUzGzoQAR5b3QWc_KZ5tbyh6hNC43ZMWZHZ_sjZr1_Qzp9lkUFX08gdfxBKTTIrouaP5Silalp5i9dNI7mxEggAHUnSQfyJWKZm8qTV7DAy0GmjHD4JXbEbU0bXAYUfGiRybpbmnqXyd2m8h__iK3DIcqwNw_kNNHYKholdD41ZoLL7IF_wJC7FlWlnJVB3M2qC3Y2LxbaacS4Kqo0cnNHTlXEVlJiyjskWrQJPi9lF55d0NGSQ35xDF6r84Nrty58Ut0wZVi3-VHfy9f6WLk7wnH0GOlAyuXt3AqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ET2PpQXSgbMSyBx3o-xrm2-zNLCEaXO45KN8B63hh4TwgBwtuKrvtFMQ05FXWhql0wwyrPJlRU1ly_0c85nTUZHJ9c54g3kFRsgp8egBBlUZ2KhtB4QkG-yaWRjYzTbKzjvJIAhgUpzbKCl1k7bW8u-drDzOeb_9StZ5C6QZHWL84MWnt3yff0hSs5XvoaF8N7ayeqamS6H1Lp_yCi7xU11t1LTpd2sKXzr5fFiQ_DX4lnxkrPwSZFph3wvjgdWqbdG-0DjBcBRY6uzgUKaC-eRRLkTg3pFJFN_x2myvNx0w760Qw9Qgj0QJZwylvkbIq-v9mSoLdjaFQyW_w-ZZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rs7iXvTcSjt2NGvg3uugcshx9ZqiUBNJe6UJoP2Jfli8SNZy2vvMqHf9LtXm_U6Ni491LcT32FHlg3DAEBAtvFX5kOjm7Y3s70us-xq6xmltuxnsUr5WeAr5YRkpuPsaOrkakmlGU33103nz17fIssqKL2LFrolMKcQCfJRsiAqZZC7Rt44EzdE7Brg9t8ubg7UYXMy34mexzpNOiAyEirZzSbUJzz4nUxkh2Ge0olUy9_56WaqP0qp3z254ZXOVmwIdZ5aiMMrsxXHnTIkl-H9nKk8RxCoBusD6KHbhORAd8SmLsvJon7SEaUeCTYekwveorrmUaMpTHm0M0uHE3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
👍
پائو کوبارسی ستاره ۱۹ ساله اسپانیا و زیدش بعد فینال دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101301" target="_blank">📅 13:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101300">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad81ee87a2.mp4?token=r7d6o_LoiNBgJ_j4uZmJEYn_nC3YN5Q3bECTC5NUqfzeCs5H_D2fq6RSFjrPQoMH5pH14x4zcPHy_6OTLBDp2E2N1csgsHyZwef7yH0yEHBo4Lcad86OZZrIVQ3N1n8xk1tAF2kS90qMGdPVzJ_nkYjf4cH8vi0YJSGDehYEKgeXUhFCk1Q0oNrdb2pKo_qcNufCl1RnRTZMAACY_prXnMhVNS8HZvWveMAGkc8_JsN38T9QkCnejyfCNReiU7XfvXafkBmY5zu9RL55-qziv1emNKfAG47PGFUIKigD32ZlBa9U7MA6RSMwxisblrovQuJhKnYRM_vaClyuwqWozQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad81ee87a2.mp4?token=r7d6o_LoiNBgJ_j4uZmJEYn_nC3YN5Q3bECTC5NUqfzeCs5H_D2fq6RSFjrPQoMH5pH14x4zcPHy_6OTLBDp2E2N1csgsHyZwef7yH0yEHBo4Lcad86OZZrIVQ3N1n8xk1tAF2kS90qMGdPVzJ_nkYjf4cH8vi0YJSGDehYEKgeXUhFCk1Q0oNrdb2pKo_qcNufCl1RnRTZMAACY_prXnMhVNS8HZvWveMAGkc8_JsN38T9QkCnejyfCNReiU7XfvXafkBmY5zu9RL55-qziv1emNKfAG47PGFUIKigD32ZlBa9U7MA6RSMwxisblrovQuJhKnYRM_vaClyuwqWozQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما با دیدن این ویدیو یاد چی میفتید؟
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101300" target="_blank">📅 12:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101299">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYMnNrDc7myNXJbGW3vETUbE0QNX6yGBxsFuHvDnNX6T2craLNDdWyUsFwmUqUKsvAbFUiy5qg3TPLLg193mZ3fSTWsbQtzvgWulai2J9w9WWlg1_BGbWnxVhek6HZg8Al3HEA6IiccckpP-BYKxEIwEEgOSZDTsSeCgCkFcgQLxh-LQNVYTIwoF_xSGjTJ-wQeS4aFZQF9Jn9vOivZUexVfacgRhcucUNVagvJrL_bhc_wNPAHuK_AQBg56UQQuGzIsTowTFvXGfsS3Vc3ieJQoX9W1GxuYUsXSoXn0gj3aMQnB3_YIYNJo3Uk3Bad8m2U8D17yHdExDNuG8II-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نوزادی مسی کونش رو شست
تو دوره نوجوونی کلی جام با بارسلونا برد
تو 16 سالگی قهرمان یورو شد
تو 19 سالگی جام جهانی رو برد
این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد
این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا ازش بخواد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101299" target="_blank">📅 12:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101298">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5934b1abe1.mp4?token=YzQtXwV8BK3DolGx1AcO5QFgTeuFHb2lEpHt93E9N-Q0Q-RG5ykEaP2MLNjOhgXH3FkA3FMYo3ENG8zhcRV3-WQGD34iLCBLL1brKtypFtmIFJeKMnHE4HnW1dqoPl5Bt5RBxUYMWZNfs6zdUrUm5nHiKsIPFzryWTSvXr2ReUkjnz6e0FVbqV7r8xbVdeUxVS5UhPQL46Pu5PifzovFQhmqGda032ikFN1QTRFE7Tsrb3qQCdzt9bdI2MlYQ30mhFZTUZKce6gK1_5Rs0OGVe7S9bs1SUDZPOp0oKCbP9wi50oNam6IQDRjuRvICNyJagrQkZc3PRAGFHMh_z6whRydexz3E7w2uHsA2rI9EimoLmd8JIvYIvDi9DGK2_cT9Zdqe67FfTaAk0PGSeSaNuV3cmTolHYJgtsOLucpWal_CsdZqfDsw4GFkKs5YobEPw0P65YAhLAvg4QYljUuwhhYSTxvTwMwRU4QXshP5QlfMuYdDTIjETlzOKjs2SnlVckT4FpZhOagFUwHWJTbakH-_58F7DcVyEA_VP2v3Z6cW8anf7areMS0Ebx1F4SPlyuoqDRc3cQ4ETfk00umFxxW8yDuULAHiOXl-xpPcDbgC8FjmrqdnOhNloXhKz_i4nWjhkEz5T2_2UZh9M2QfPn4gCpUR8WUF7yGkaiU_Rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5934b1abe1.mp4?token=YzQtXwV8BK3DolGx1AcO5QFgTeuFHb2lEpHt93E9N-Q0Q-RG5ykEaP2MLNjOhgXH3FkA3FMYo3ENG8zhcRV3-WQGD34iLCBLL1brKtypFtmIFJeKMnHE4HnW1dqoPl5Bt5RBxUYMWZNfs6zdUrUm5nHiKsIPFzryWTSvXr2ReUkjnz6e0FVbqV7r8xbVdeUxVS5UhPQL46Pu5PifzovFQhmqGda032ikFN1QTRFE7Tsrb3qQCdzt9bdI2MlYQ30mhFZTUZKce6gK1_5Rs0OGVe7S9bs1SUDZPOp0oKCbP9wi50oNam6IQDRjuRvICNyJagrQkZc3PRAGFHMh_z6whRydexz3E7w2uHsA2rI9EimoLmd8JIvYIvDi9DGK2_cT9Zdqe67FfTaAk0PGSeSaNuV3cmTolHYJgtsOLucpWal_CsdZqfDsw4GFkKs5YobEPw0P65YAhLAvg4QYljUuwhhYSTxvTwMwRU4QXshP5QlfMuYdDTIjETlzOKjs2SnlVckT4FpZhOagFUwHWJTbakH-_58F7DcVyEA_VP2v3Z6cW8anf7areMS0Ebx1F4SPlyuoqDRc3cQ4ETfk00umFxxW8yDuULAHiOXl-xpPcDbgC8FjmrqdnOhNloXhKz_i4nWjhkEz5T2_2UZh9M2QfPn4gCpUR8WUF7yGkaiU_Rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملاقات اسپید با گروه BTS در فینال
🙂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101298" target="_blank">📅 12:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101297">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242475ed92.mp4?token=X6qQh5QgMTVuG6BAVKmb7gCRF5roVdnofbn44K4FmcWZlR_EEsf1nH9Lerxqg23OaQthwQ2xi8RRGc2e75Zczp-aeI5b4VZZ8-rZFl7ll8gNLvZZgh6eYKq4fTuUcGCnWpQz8vf-lteDzTnSxPV2ybflG992uJvyLAPuYdsM7O8WpVVZW4ddG9XcFvU8a1NTEog9GJamXHP9oEpddB6Cp2S6BTswx5OTWHKU304Hg5eYLvk2xqQ4dwaV7X9C3N0ura1jiXwX_zVG8wUiiLvH5gGaYt0-7JRjFGXndsZA3sxqKodks4snMeE1Hi1_Fgo3l7PDKcX7AqMS879VnCsjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242475ed92.mp4?token=X6qQh5QgMTVuG6BAVKmb7gCRF5roVdnofbn44K4FmcWZlR_EEsf1nH9Lerxqg23OaQthwQ2xi8RRGc2e75Zczp-aeI5b4VZZ8-rZFl7ll8gNLvZZgh6eYKq4fTuUcGCnWpQz8vf-lteDzTnSxPV2ybflG992uJvyLAPuYdsM7O8WpVVZW4ddG9XcFvU8a1NTEog9GJamXHP9oEpddB6Cp2S6BTswx5OTWHKU304Hg5eYLvk2xqQ4dwaV7X9C3N0ura1jiXwX_zVG8wUiiLvH5gGaYt0-7JRjFGXndsZA3sxqKodks4snMeE1Hi1_Fgo3l7PDKcX7AqMS879VnCsjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با نایلون داره جام‌جهانی رو میبره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101297" target="_blank">📅 12:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101296">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c93fe59da.mp4?token=rODcweXEqosHo5Xt_dqnNj1gWFjPyLvJ9MDI4USMxrKF1czXZxpYBNuDICmWdRQiuzN29CxNQzEZkhYVk17BDWaT4-BJqPRTvQkm6RJEd7C5g_k0sy7c8oXJeljLLUIwmsHIiQ-_qzTPok-e8RXAjHS1vlIAPx5eqWe8y3Nh15NL9KG_BhCbPIbSq0ZfJQuPEiMyVIXDogwaDFZbBOVIZTs8HDu8R9LdU6u5wP1UuOy_QxbXW6sLLlwDCEpEC_3BntykEGmT7v14AyGGSWpAhMsZl4v0oFxqMmDzN7iH2taWIIQj0bwqpWZ77UuKLBX1b1_EnPkoEF9KxT6OaWC7KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c93fe59da.mp4?token=rODcweXEqosHo5Xt_dqnNj1gWFjPyLvJ9MDI4USMxrKF1czXZxpYBNuDICmWdRQiuzN29CxNQzEZkhYVk17BDWaT4-BJqPRTvQkm6RJEd7C5g_k0sy7c8oXJeljLLUIwmsHIiQ-_qzTPok-e8RXAjHS1vlIAPx5eqWe8y3Nh15NL9KG_BhCbPIbSq0ZfJQuPEiMyVIXDogwaDFZbBOVIZTs8HDu8R9LdU6u5wP1UuOy_QxbXW6sLLlwDCEpEC_3BntykEGmT7v14AyGGSWpAhMsZl4v0oFxqMmDzN7iH2taWIIQj0bwqpWZ77UuKLBX1b1_EnPkoEF9KxT6OaWC7KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
جملات عادل فردوسی‌پور درباره آخرین بازی لیونل‌مسی با لباس تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101296" target="_blank">📅 12:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101295">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE7FWcM0I8dJey0Nu7yIcqk9jBL0gNC-whKKhmR9TCnPXx84WvD_Q_2O3Twmeh2iVjj5DBp11FWZWceS-tm-dE8w7DNCw688IG3XrkmFZfmPUUyvzyU79U9iNYeJKZfKRHBkvMeMekmdUtPTawbKTyPqMsG6HHVWXBdyfYmpwSlvu9h1BLTIa3knFNwHovQJ1eYpTNUSLnqBKKpiaFsJgMJRGqFgayeYSK-l7OoaThrXE0qjlGhP0J_R4LTnfp7VMPt2FfBt9dSjQNmcUOi5-6gsf2xzH85-wR6tTxx-o42o2A0dRYfl8T6ORmxFOTC80Se1TLOSPEuoxN3KAyHZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
😢
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101295" target="_blank">📅 12:15 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
