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
<img src="https://cdn4.telesco.pe/file/Kqrw2d3HeKeAT43vrt5UezAERteLlF-rCB0pYoIw-c7Q1qXHWyzfMhGCeSgQaMKstOqVwp-SmZlcqYUh1NDYKX5ceuwe9I5XP4jHhURtNo2iyocUQWzD8CFP8DUEEJOKNtHpp1PxFmKcdzmJB_f9Y8tJgv2-aZUbX_oEjPwhZ-k2ckyZR7STAkGRDGv7utTudeDGSCua0FvMBgzEwdWfAj2Q2L8j6S_dlD2sBevTbTKV3kWluSb8o4c4BoNcC_z8veBKFiqghPt4lNs4lFwkwfjgSsZoDDHIouUZZ0GsFlnrw7tjfr72cXMY0wkCmxQwVz0YQgpokU9LT-ONX6rACQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 05:04:34</div>
<hr>

<div class="tg-post" id="msg-141163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FG_Yo0PhsrQ4PyzraQqALvNIn5CvNFUFxEGEVqVap61pSXJyqC_ksnCStpN8z42doikyjV6BOA-_eW1wbzsoQ3uNOYx-j9y0lvJXXXW199ZRSbUlV4CjzDUbuo9W7Ht4h5ZWfYjdzBokqFB9OmCjYkHUR06c3GXwKDclBftvbG3jU2LkhCXbTbT97YYT00C7Vo8GNyLf9I_MfpP18TVZiR15vX61UvsV7gcW4zlmuhWIfG0EDb2WQ8qBKe0DrqwhiiipNDdtCEcvcBZsFZaqDWovmyQdYF5Nft96Ajr4Ql-Fgxr0okFkhqe9YCOCfjjrFjAof_plNXEEs02JY-Stng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/141163" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
استوری کنایه‌آمیز شجاع خلیل‌زاده به بیرانوند: تمام حقوق خود را گرفته‌ایم و از زنوزی متشکریم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SorkhTimes/141162" target="_blank">📅 00:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J71hw2fp_b0KDp6rFNr4MR88ZDsR_MFNKfBkhLufDETNBVZ-G56tF_nyNyGSN2NqMxlapJ3ehFOo-B3Qx6LfBw64MofVuJjAROonvbk6snFRKTfqSoNxXGKT-iXaH4OITVDLICWxjmEQuCCyY9RcelSLocpvyEyWTihdmYZ31m99sQmx5Kqu2b2HdWujmU3rHPboLgev8h51tJBoq1UCqlobGmASJsgk4s_XFQpwR00_Ee6chXNKeFNQNb_VimdEJLrd5Mfh81aAB1zX_z-xDNRyifxAncnAjE3SUL_NzjVx7Tzi0tmrXHzDFBJjLjDUnWZtZj70ov8B_nKb7D2CBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
بیرانوند تا الان عضو 5 باشگاه بوده که در هر 5 باشگاه به مشکل خورده و از اونجا به شکل غیر حرفه ای جدا شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/141161" target="_blank">📅 00:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141160">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/141160" target="_blank">📅 00:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141159">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZb4l61EvaDwc1PvHRUqlBzsLGRDbNFaLkajHOXJlXQlA_9kXrnYwoAabhgFIJ-XE51Fof1ksjKSspeug5K7bVvC37pm6sNr0PYLKwDpna3xvI_zG9e8DODFbPJhKrSTDq4biDhtZGW2jK0TWZP_mdw10v9Q8pOGEDCy3wtgoKplpr4Tjr17W3emO7ZUGtF_9VwlOzv6uQmgA_WhUTL6zRKZDSN1HzPe-8ykK2BvuYQ8ASbe6-fmG510wlfS82txyRe16syp8WKrvqHs4o3XI01W-56eHAJX2Uy6UylPdAsgV3NPDMb0NuKE-B2TugG7-2K2qAxChqJ8pSckSj8I_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/141159" target="_blank">📅 00:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141158">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
استوری کنایه‌آمیز شجاع خلیل‌زاده به بیرانوند: تمام حقوق خود را گرفته‌ایم و از زنوزی متشکریم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/141158" target="_blank">📅 00:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141157">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwxrGLGKdq-NYRFubEW7daRTBVqwi417h-AwaQf4z0phTDYSmGVlsZGFPP9lFMHrbyfDcHP3pfrCgv7qvZUDN-D2u9YWDfEZiK1D0wb8fH6J45SHGeiVAZgtX22nV3PNKFUDD8ouYju9q0X8pFD3taGAXcI3S-nZx1uzA2rlb07kUbRHtwqL_epOt5oIWTL9tCn3_PuiT5vsHXlY_b_cAn5i2BZTLPywj0f2vYBlkEL9C8wy0nbc45MMO3HBynB2J2ylBLfe8Lh93bfr9kE8guo1Hyy3Bm5Xiz2qtbhCrYTPP55ewagUEiR_x45Ci3Oe9g51e-zJFCF4jk1EF3VQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/141157" target="_blank">📅 00:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141155">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOnXxJrHTSwHcszg_PKiJM17NVTkCPRu3rEw7eqmcWm-QZj7qpkp_S5a34NkFGIgdnsbvkAVjQUuRgIA6_yA3X103afHgaJ5-_9wgOmoCvuTwtOwaA0uztmfBPtCuFo8Rk1hAoKm5mEmIhu27ZhrMJ4HkjQvvbT2NTwHUAVWNp6jxKI6IdGXmGwROFhHmQ0QHlp24nEpAQf0I0g5cccNkeVzp7an-EkP0ZP8pCT1M2VWwXYgBKT-ZRiiSRGmzOQjNZAR7QGQd9V_HSA7n7aoCewowDLe7JLeVjG-cOZsGTr6XsOHTrMRamJiMn3YOW-3LJWqeVIdH1dHazqyAmY_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/141155" target="_blank">📅 23:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141154">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
22 پرسپولیسی برای بازی مقابل صنعت نفت وارد اردو شدند / یک نفر فردا خط خواهد خورد!
🔴
1_پیام نیازمند
🔴
2_امیررضا رفیعی
🔴
3_امیرحسین طاهری
🔴
4_ابوالفضل جلالی
🔴
5_محمد مهدی زارع
🔴
6_حسین ابرقویی نژاد
🔴
7_مجید عیدی
🔴
8_مهدی تیکدری
🔴
9_پوریا لطیفی فر
❗
10_محمد‌…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/141154" target="_blank">📅 23:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141153">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
22 پرسپولیسی برای بازی مقابل صنعت نفت وارد اردو شدند / یک نفر فردا خط خواهد خورد!
🔴
1_پیام نیازمند
🔴
2_امیررضا رفیعی
🔴
3_امیرحسین طاهری
🔴
4_ابوالفضل جلالی
🔴
5_محمد مهدی زارع
🔴
6_حسین ابرقویی نژاد
🔴
7_مجید عیدی
🔴
8_مهدی تیکدری
🔴
9_پوریا لطیفی فر
❗
10_محمد‌…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/141153" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141152">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭕️
⭕️
مارکو باکیچ و دنیل گرا از لیست بازی فردا خط خورند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/141152" target="_blank">📅 22:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141151">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
باکیچ و لطیفی‌فر شانس برابری برای حضور در ترکیب فیکس پرسپولیس مقابل صنعت نفت دارن و تارتار هنوز تصمیم نهایی خودشو نگرفته/ایران‌ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/141151" target="_blank">📅 22:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141150">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ci7EQb3gKVIr6p-CKybruRT_0qaDXVUkhM7MNMsy71uTfVlvOR37qWc-Wgg5sm5Zptp508kYuj3e7HQz8BcCBqy0omz1t1aVVTdCV60alysDTndxEnALd30EityY_cPLqQQEDML4JHFjpim8x4Is-ZbqWR_fCZxC6_tWjSF-4vpq6ahlmLI1YvfsMLKMKkpU8aCvM1zOwm2hqSv0zhVZmfscahpy6cl01VrcCi5hHzM-YmlTx9_NRPwA00BywCB6EeJ7cbR7zVYrs9LBoRuYcND0uluc3b2KFe6cPgu7B1cnhRr1_DcxSgReGohDihvo3iViU-TTVXRqjbLzTcnUNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کنایه حجت‌کریمی به کم‌‌‌فروشی سرباز
✅
مدیر تراکتور گفته گلی که بیرانوند خورد باید از کارشناسان راجع‌بهش پرسید‌. منظورش این اشتباهه‌ فاحشه که توپ از زیر دستش رفت‌‌. به‌نظر میاد به کم‌فروشی بیرانوند و گمانه‌زنی رفتنش به استقلال اشاره کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/141150" target="_blank">📅 22:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141149">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
حجت موتوری: همه بازیکن ها 8 درصد گرفتند ولی بیرانوند 35 درصد گرفته
😂
✔️
بیرانوند گوه خورده میخواد بره استقلال بعد خدمت سربازی هم با ما قرارداد داره
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/141149" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141148">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
جواد نکونام به دلیل مصاحبه دروغ، بیرانوند رو اخراج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/141148" target="_blank">📅 22:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141147">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
⛔️
👀
پرسپولیس ب که قرار بود به سیدجلال سپرده شود، احتمالا با محسن بنگر وارد رقابت‌های دسته دوم لیگ آزادگان می شود...
‼️
🟥
به گزارش هفت ورزشی، پرسپولیس که دنبال خرید امتیاز برای راه‌اندازی تیم دوم بود، سرانجام امتیاز پادیاب خلخال را خرید‌.
گفته می‌شد هدایت پرسپولیس ب به سیدجلال حسینی سپرده می‌شود اما گویا باشگاه شرایطی دارد که مورد پسند سیدجلال نیست.
‼️
برابر با شنیده‌های ما سرمربی فقط حق دارد ۵ بازیکن برای تیم جذب کند که این پنج بازیکن هم از کانال مورد نظر باشگاه وارد تیم می‌شوند. بقیه بازیکنان را هم خود باشگاه به خدمت می‌گیرد.
انگار محسن بنگر این شرایط را پذیرفته و ظرف ۴۸ ساعت آینده به عنوان سرمربی تیم دوم پرسپولیس برای حضور در رقابت‌های دسته دوم لیگ آزادگان معرفی می‌شود.
‼️
راست یا دروغش گردن راوی که می‌گوید پرسپولیس امتیاز تیم پادیاب خلخال را گرانتر از قیمت عرف بازار خریداری کرده است. در خرید این امتیاز یکی از اعضای هیات مدیره که اهل استان‌های آذری زبان است نقش داشت.
همچنین رد پای یک عضو هیات رییسه فدراسیون فوتبال در این ماجرا دیده می شود، همان شخصی که یک دور مشاور مدیرعامل باشگاه بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/141147" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141146">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
بیرانوند هم ظاهراً از همین حالا خودش را در استقلال می‌بیند! برای همین بدون نگرانی علیه زنوزی و مدیران تراکتور مصاحبه می‌کند. خودش هم از سربازی و بازیکن آزاد شدن حرف زده؛ انگار تصمیمش را برای آینده گرفته و دیگر نگرانی چندانی بابت واکنش مدیران باشگاه ندارد.…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/141146" target="_blank">📅 21:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141145">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
❌
❌
❌
❌
❌
از سوی دیگر، گزارش‌های تأییدنشده از کاهش شدید پروازهای هواپیمایی آتا حکایت دارند؛ شرکتی که گفته می‌شود در سال‌های گذشته روزانه ۵۰ تا ۷۰ پرواز داشت و حالا تعداد پروازهایش به چند مورد رسیده است. اگر این آمار درست باشد، می‌تواند زنگ خطری درباره وضعیت اقتصادی…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/141145" target="_blank">📅 21:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141144">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭕️
⭕️
⭕️
زنوزی هم بالاخره طعم تلخ داشتن بیرانوند را چشید!
❌
❌
سرانجام نوبت به زنوزی و مدیران تراکتور رسید تا طعم گس داشتن علیرضا بیرانوند را تجربه کنند؛ همان مصاحبه‌ها، همان گلایه‌های مالی و همان کنایه‌هایی که پیش‌تر مدیران پرسپولیس بارها با آن مواجه شده بودند.…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/141144" target="_blank">📅 21:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141143">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
⭕️
⭕️
زنوزی هم بالاخره طعم تلخ داشتن بیرانوند را چشید!
❌
❌
سرانجام نوبت به زنوزی و مدیران تراکتور رسید تا طعم گس داشتن علیرضا بیرانوند را تجربه کنند؛ همان مصاحبه‌ها، همان گلایه‌های مالی و همان کنایه‌هایی که پیش‌تر مدیران پرسپولیس بارها با آن مواجه شده بودند.
❗
❗
اما این بار ماجرا خیلی زود به برخورد انضباطی رسید و جواد نکونام پس از مصاحبه جنجالی بیرانوند، او را از تیم کنار گذاشت و باشگاه نیز رسماً اعلام کرد که این بازیکن در اختیار کمیته انضباطی قرار گرفته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/141143" target="_blank">📅 21:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141142">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭕️
⭕️
با اعلام باشگاه تراکتور، علیرضا بیرانوند به دلیل مصاحبه بعد از بازی با استقلال از این تیم کنار گذاشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/141142" target="_blank">📅 21:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141141">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
خلیل‌زاده اومده استوری گذاشته از مدیرعامل تشکر کرده و پشت بیرانوند رو خالی کرده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/141141" target="_blank">📅 21:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141140">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✅
مصاحبه بیرانوند:
✖️
اکثر بازیکنان می دانند که این جام ملتها آخرین جام ملتهای آنها است و باید یک کاری انجام دهند/ از آقای زنوزی خواهش می کنم به داد بازیکنان تراکتور برسد/ چندتا بازی دیگر نیم فصل تمام می شود اما بازیکنان تیم ما فقط 7 درصد پول گرفته اند/ تراکتور…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/141140" target="_blank">📅 21:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141139">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
⭕️
با اعلام باشگاه تراکتور، علیرضا بیرانوند به دلیل مصاحبه بعد از بازی با استقلال از این تیم کنار گذاشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/141139" target="_blank">📅 21:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141138">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/141138" target="_blank">📅 21:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141137">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/141137" target="_blank">📅 21:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141136">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8lO041t6jFiEjwJRN8Fpe6MG5-6pgzGZm8RTOIvGA5c5wlTM2eP3O61wSwtWBIKBlQ_U6I3DnRP8YDfp3LIKfTZD33S0qjGKin5GCBIjhPhHYrP8L8m6jfeyIeKMekzWyL3RItDmWHYHDxe31E7tJAhHIW9jkSPtl2mYX3HcUgGrltynM0p9Gn2iQcQOybQthsSd3Wlx5E7vmhxwyKskW0KYanV9fTtjMlGbI-pzSde3kMnZsSGDOutCl8ick0uybsm7-A_kddgQ_2btcYLA1noonbQwrxTml9sFLydVcKCqUKPvll_ARIjWnuTJDNTj1U4rjxY1zee0g5an4Psww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Sepahan -
🟡
Fajr Sepasi
⏰
Today 18:45
🏟
Naghshe Jahan
🔵
سپاهان از نظر کیفیت فنی، مالکیت توپ و قدرت هجومی دست بالاتر را دارد و در خانه می‌تواند فشار بیشتری روی فجر ایجاد کند. فجرسپاسی احتمالاً با دفاع فشرده و انتقال‌های سریع بازی می‌کند و تلاشش بیشتر روی بستن فضاها خواهد بود. باتوجه به تفاوت کیفیت دو تیم، سپاهان شانس بیشتری برای کنترل جریان بازی و ساخت موقعیت‌های خطرناک دارد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/141136" target="_blank">📅 21:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141135">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚽️
جدول لیگ برتر فوتبال ایران پس از پایان بازی‌های روز اول هفته هشتم
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/141135" target="_blank">📅 21:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141133">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjT-da62viiiMYHyGIsL4jAonw74xKVXp49RFHfD4_zIBf4o_y6ZKV63Yo3RIU72vdABqkxqjpcB_YGvv4giwhQ2y1k-PYquxOtlrLxMe-DYCHqunMRf3zKGgRqhFUA6D9GnX3kKVYmaSASWMsxHMyTwq1glspcyZWRrOhd0_5Hjq2d1DXhnJnRs5qbwywP0U5bsjYaGBpNat7nZg5dV0v_84guYNARTVj34wPrPUgarLduWW_Auetn6_E7PC195j1Ath28F8diCZkU8ExNqKyDLt7K2ZyWzaRV86j-MIsO2JZ8GV9NSShGokWddI4YYCtsjMKJA5AFGtZApHHQK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول لیگ برتر فوتبال ایران پس از پایان بازی‌های روز اول هفته هشتم
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/141133" target="_blank">📅 21:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141132">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❤️
🎙
علیرضا بیرانوند: امروز ام آر آی کتفم را برای نظام وظیفه فرستادم/ به هیچ عنوان درخواست معافیت پزشکی نکرده ام
🔴
نظام وظیفه اعلام کرد عکس کتف مصدومیت را بفرس که من هم فرستادم
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/141132" target="_blank">📅 21:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141131">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
وارد فیفادی شدیم، شخصا از فیفادی نفرت دارم چون پرسپولیس لذت دیگه‌ای داره برام
❌
میشد که قبل از فیفادی یک برد دیگه و یک بازی دلچسب دیگه از تیم محبوبمون ببینیم اما کارشکنی‌ها جلوی برد دلچسبمون رو گرفت..
❌
دم تک تک بازیکنامون و کادر فنیمون گرم که کاری…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/141131" target="_blank">📅 21:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
تارتار: تعطیلی ۵۰ روزه لیگ منطقی نیست؛ حداقل تو این مدت جام حذفی رو برگزار کنید، حتی بدون ملی‌پوش‌ها. بازیکن‌ها هم باید برای تمدید قرارداد با پرسپولیس جلو بیان، چون پرسپولیس تیم بزرگیه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/141129" target="_blank">📅 20:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141128">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: خیالتون راحت باشه. قبل انتخابات کنگره(۱۲ آبان) به ایران حمله نمی‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/141128" target="_blank">📅 20:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141127">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aee740782.mp4?token=hfpRhgoFc8cP0puMPuzMhu1NV32UccgfUfCW1Jx54MnohI1b8mJDmBiqFIjWzoCpx5CdLzrCwYkTrj8SX70lnV5JC8ZKPotH9PAa2LBZUel-ydYvHK7wX0wT6eZ7BCm0xRp4dDSW20JY5Mj7KRCc6m40SOJLHKbaQ9xe602EgXGOvy6yHRtuuUz5Aq1j19gC9O2ZKGiSznp_hecYVjPVoN3rRCkAE8rXM0SyL3KPxkOyq7nUFyNl2byqHa10F2k6RpYOSGGdDV9qQgmbKWZ67P5BHYxEdFf97tU0WgPWP1kmC0CgAoX4FUHnOKGKTvMeq9CuHD4f3Ahs3WYIA3BWSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aee740782.mp4?token=hfpRhgoFc8cP0puMPuzMhu1NV32UccgfUfCW1Jx54MnohI1b8mJDmBiqFIjWzoCpx5CdLzrCwYkTrj8SX70lnV5JC8ZKPotH9PAa2LBZUel-ydYvHK7wX0wT6eZ7BCm0xRp4dDSW20JY5Mj7KRCc6m40SOJLHKbaQ9xe602EgXGOvy6yHRtuuUz5Aq1j19gC9O2ZKGiSznp_hecYVjPVoN3rRCkAE8rXM0SyL3KPxkOyq7nUFyNl2byqHa10F2k6RpYOSGGdDV9qQgmbKWZ67P5BHYxEdFf97tU0WgPWP1kmC0CgAoX4FUHnOKGKTvMeq9CuHD4f3Ahs3WYIA3BWSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🟡
ی سوپر گل دیگه هم ببینیم
✔️
گل شیشم‌ سپاهان‌ به فجر سپاسی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/141127" target="_blank">📅 20:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45eaeb8981.mp4?token=M67M8JcZZ0F7wijOmlVX_TGHXTpfO3NniBAzv4y8GJy46xAH-EfqzRbdGdGACeRxYWJrPiHRJ8ovNxPn2NrbTJPd9dadQ9ByFFY9jceY26jgRRbHQJHVmnReliPgzqDqbcjaYvOKGbmF-Y-KToGXr5p8qCzGgvUl7cGePOiEKNYPuIggmanyf1sOCBKVdC0Qm6fkH-cg7d53GigKdxyiLXcZ42MKPjLWEiLailrujVdNwGSv3fL7SVM5pj7Rsq3tYzbOg4U7OuenGS-AYPlSgtQ4EofZx9B9Kng6Wek597rBenXWsL0Vd8U9v1odbf7APSyY23evOXL1cDn6ymYrjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45eaeb8981.mp4?token=M67M8JcZZ0F7wijOmlVX_TGHXTpfO3NniBAzv4y8GJy46xAH-EfqzRbdGdGACeRxYWJrPiHRJ8ovNxPn2NrbTJPd9dadQ9ByFFY9jceY26jgRRbHQJHVmnReliPgzqDqbcjaYvOKGbmF-Y-KToGXr5p8qCzGgvUl7cGePOiEKNYPuIggmanyf1sOCBKVdC0Qm6fkH-cg7d53GigKdxyiLXcZ42MKPjLWEiLailrujVdNwGSv3fL7SVM5pj7Rsq3tYzbOg4U7OuenGS-AYPlSgtQ4EofZx9B9Kng6Wek597rBenXWsL0Vd8U9v1odbf7APSyY23evOXL1cDn6ymYrjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سوپرگل عجیب غریب بازیکن فولاد به مس شهربابک
😐
🔥
🍃
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/141126" target="_blank">📅 20:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141125">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a34de23e.mp4?token=PkXoPaSIrkYMfOvzOSu6bvQh6TP-9mBXBXeInM1o2v_okhOKFkxfGGQeT0c68MvFFUwRgkbFednNRj3fwGKCaLT6Z3uS5hgiiHZlS1ulNDnaJkAykDDJJlDp4hCRYE-V4JF2zO-nYIPUmWEAWF1shSkk56qbPLpsmWGIHTPXz1y3XCz2JRGYr8wOV3u4gwZY3-H1rcaoLnjpqDBax1_kxlCxJo07GXItAiZOPA5UoJGm9FuK7JISRk0jYyOmmw_6GztX_NwBoA5U_psFLqiinmsHGCGwGMoVQJHSxa9S8OW9N5_LbaN6dTeZXdgeK6AlqoDPHq2ml1P046awhGSnWykCa7t6YQOGWYCh-PC8uE9NP6XsIq9CpweUjY79WYrkyR5J9CQ137IqhKeuogLQbF_JbGbLYVbdILZF-WJJBg4MZz2HrGK9TBrg9EYOGsSEu75cjZkzpQXBDRbspatHLZ6jb3woDxn0sN2a_YCL_1dqV-JkmdBuLUYaQ3Mod8Wrkr8T2X2ZIcYeqapLyr6QVbyNT7brwWREva9L9QGqSpaVMbQU3II5UdvXc0DwVuwc_uW0mXpGxpVrWOWO_Qb0MOw2D6pf9UXVOfTh9fxikTzRKwYU3TM6_7Hpjn0wUtt7ZzlBYMyBOP2G_l-TlzLwMq7B4HHYIx0Q95tw2FEvBUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a34de23e.mp4?token=PkXoPaSIrkYMfOvzOSu6bvQh6TP-9mBXBXeInM1o2v_okhOKFkxfGGQeT0c68MvFFUwRgkbFednNRj3fwGKCaLT6Z3uS5hgiiHZlS1ulNDnaJkAykDDJJlDp4hCRYE-V4JF2zO-nYIPUmWEAWF1shSkk56qbPLpsmWGIHTPXz1y3XCz2JRGYr8wOV3u4gwZY3-H1rcaoLnjpqDBax1_kxlCxJo07GXItAiZOPA5UoJGm9FuK7JISRk0jYyOmmw_6GztX_NwBoA5U_psFLqiinmsHGCGwGMoVQJHSxa9S8OW9N5_LbaN6dTeZXdgeK6AlqoDPHq2ml1P046awhGSnWykCa7t6YQOGWYCh-PC8uE9NP6XsIq9CpweUjY79WYrkyR5J9CQ137IqhKeuogLQbF_JbGbLYVbdILZF-WJJBg4MZz2HrGK9TBrg9EYOGsSEu75cjZkzpQXBDRbspatHLZ6jb3woDxn0sN2a_YCL_1dqV-JkmdBuLUYaQ3Mod8Wrkr8T2X2ZIcYeqapLyr6QVbyNT7brwWREva9L9QGqSpaVMbQU3II5UdvXc0DwVuwc_uW0mXpGxpVrWOWO_Qb0MOw2D6pf9UXVOfTh9fxikTzRKwYU3TM6_7Hpjn0wUtt7ZzlBYMyBOP2G_l-TlzLwMq7B4HHYIx0Q95tw2FEvBUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
🎙
علیرضا بیرانوند: امروز ام آر آی کتفم را برای نظام وظیفه فرستادم/ به هیچ عنوان درخواست معافیت پزشکی نکرده ام
🔴
نظام وظیفه اعلام کرد عکس کتف مصدومیت را بفرس که من هم فرستادم
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/141125" target="_blank">📅 20:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141124">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: خیالتون راحت باشه. قبل انتخابات کنگره(۱۲ آبان) به ایران حمله نمی‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/141124" target="_blank">📅 20:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
🚨
دونالدترامپ رسما اعلام کردکه تاقبل انتخابات که ۲۵ روز دیگر شروع میشه به ایران حمله نخواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/141123" target="_blank">📅 20:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-nL5pSr3t4vh1bfMbirfAKvzz7z5gbzvZnnzHgR8CFIBcYtiHk2D0rWevrcQeAGFct3vydChZ8uvyz03guZf5s7DQ7D80cCooedvumtsalmJwkP2dT8Q2Zs2pStzAZL0FharWo6eUph0VBg4NxD9pIVmeqriOzl6TzsdljQ30RP_2oAvPRfBUnNUa3O5VafiOVMVlojiVpxR6cXv6Rl1KuHU56NWo6ltjzMCyIdo7tREkGEu-zVQcBUZxoiI0MXb4LEYdbrpmny7gsXnc08-bCL-7wUd5rOiglwAQYPKg8aV0ndsXVlAYzI2pmHSG_RYTsClXIifnLg1D0ap8f7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
🚨
دونالدترامپ رسما اعلام کردکه تاقبل انتخابات که ۲۵ روز دیگر شروع میشه به ایران حمله نخواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/141122" target="_blank">📅 20:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
حجت کریمی مدیرعامل تراکتور : آسانی مقابل ما بازی کنه قطعا شکایت میکنیم و پرونده رو به دادگاه عالی ورزش میبریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/141121" target="_blank">📅 20:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
فووووووووری گفته میشه که مصدومیت یاسر آسانی جدیه و ۷ هفته نیست
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/141120" target="_blank">📅 19:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
یاسر آسانی مصدوم شد و با گریه از زمین بازی خارج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/141119" target="_blank">📅 19:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b64ca5d3.mp4?token=o-fblcuhAWSxkNkh5o9LVnHSafJMWAUE2Dp8VKzEmv-hWgkGvXnPqOJt2qYPRVXsRq8PyYbnRtusyLKljeU76wgkLcB5ZpiS4AbbZJPivlnIeLxHT8JpBZsK7uQhGLK3IrWRtmfR2NW9fzFOrAxd4dWiw2eXuGkpIVs0bCrYfqyp4wDzfs_SwTSF85JwNMDAztRhKDMRbA26_5W2WwVYcAr6HrRMAHSkQQmMBY2L8bkGNci5GOHOe5nH4I5LpLp-541G18-NXpl8XwqCUIhEmdjjNAayL95rjMUgIG4bp-qCC17M8XZGJpuMag7G1uO2jIP1J5d3PGU4L8j-rLNE2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b64ca5d3.mp4?token=o-fblcuhAWSxkNkh5o9LVnHSafJMWAUE2Dp8VKzEmv-hWgkGvXnPqOJt2qYPRVXsRq8PyYbnRtusyLKljeU76wgkLcB5ZpiS4AbbZJPivlnIeLxHT8JpBZsK7uQhGLK3IrWRtmfR2NW9fzFOrAxd4dWiw2eXuGkpIVs0bCrYfqyp4wDzfs_SwTSF85JwNMDAztRhKDMRbA26_5W2WwVYcAr6HrRMAHSkQQmMBY2L8bkGNci5GOHOe5nH4I5LpLp-541G18-NXpl8XwqCUIhEmdjjNAayL95rjMUgIG4bp-qCC17M8XZGJpuMag7G1uO2jIP1J5d3PGU4L8j-rLNE2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اعتراض مغانلو به نکونام بابت تعویضش پرت میکنه کاپشنش رو نیمکت
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/141118" target="_blank">📅 19:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hemymzQiuRRCtv6Ra7dHFYozWCebUDtY54N78c17Lxhj_-8DxGlDtRa3y_va6V8vcnp1gkRZSkRVvRDHDj8Gnf42VmDBeMq-AunPlMRMsIPVCWgXAcmTijC9peXzvnYQSSkSt7faQ1wF8otcEeIJer_jBKMh8gXfNe4VMROUfUOMDfh-0iZAEzrb6MJSVou9i7D4JP-SHACLjnGPrXlIrs3K8-SokZPefGmnaoJuMo8FVwAV2kLgX65ZSeH2BPshKMlxsHKb8MH7RA1dz9GZdXzbCxxfdo0uGOG4Doe9VfXxa5MPim1P5DoOvNS_p-OPZjsCkwfS5qJ79xxNzLySCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصاویری از آخرین تمرین پرسپولیس پیش از دیدار فردا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/141117" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
یاسر آسانی مصدوم شد و با گریه از زمین بازی خارج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/141116" target="_blank">📅 18:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141115">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
کیسه نیمه اول و یک بر صفر برد و خداییش تراکتور هیچی نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141115" target="_blank">📅 18:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141114">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ساعت 17 بازی ترتر و کیسه شروع میشه ..بهترین نتیجه برای ما از نظر شما چیه ...مساوی یا باخت هر کدوم تیما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141114" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141113">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
حجت کریمی مدیرعامل تراکتور : آسانی مقابل ما بازی کنه قطعا شکایت میکنیم و پرونده رو به دادگاه عالی ورزش میبریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/141113" target="_blank">📅 16:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141112">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e84fd67a.mp4?token=vIU4Vq6706_N5otebR9Y4LdD8PyZiS82qLL7RyzRID-wgWfB_0GbIwKv0oFD8vcDG40UETLd4UzVxobXPUNxwHAJojjX250UCSxnbDakogCikRUTMQGW56c7OG17FuzLHjhz5TH8yLcD9zg0OZsI6veSVP9VvQ0AAQxoOj8YFUwhsOcQZcimStBPJI0GKQXkv7LjGVrTUWMeOEQDVsSb95FB8uNlt85LKTMr5Q7Zfc2HdRH0GUdzV_0TPhQHK-8TwnteZ95fbRKnHNSelwm_l18N4SW2cnyNXPXgf2rsIyUpymx18dZeLCh6mrqiiRt4Q45HRrdGLQbjNMkt_HVPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e84fd67a.mp4?token=vIU4Vq6706_N5otebR9Y4LdD8PyZiS82qLL7RyzRID-wgWfB_0GbIwKv0oFD8vcDG40UETLd4UzVxobXPUNxwHAJojjX250UCSxnbDakogCikRUTMQGW56c7OG17FuzLHjhz5TH8yLcD9zg0OZsI6veSVP9VvQ0AAQxoOj8YFUwhsOcQZcimStBPJI0GKQXkv7LjGVrTUWMeOEQDVsSb95FB8uNlt85LKTMr5Q7Zfc2HdRH0GUdzV_0TPhQHK-8TwnteZ95fbRKnHNSelwm_l18N4SW2cnyNXPXgf2rsIyUpymx18dZeLCh6mrqiiRt4Q45HRrdGLQbjNMkt_HVPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حال و هوای سکوهای ورزشگاه یادگار امام (ره) تبریز در فاصله کمتر از پانزده دقیقه تا آغاز بازی تراکتور و استقلال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/141112" target="_blank">📅 16:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141111">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
بازی شروع نشده تراکتور از استقلال شکایت کرد
🚨
حجت کریمی نامه زده به پلیس مهاجرت و گفته رستم و ماشا و آسانی مجوز کار ندارن و حضورشون تو تبریز غیرقانونیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/141111" target="_blank">📅 16:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141110">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
حجت کریمی مدیرعامل تراکتور : آسانی مقابل ما بازی کنه قطعا شکایت میکنیم و پرونده رو به دادگاه عالی ورزش میبریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/141110" target="_blank">📅 16:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141109">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
یاسر آسانی گفته بود بمیرم هم از استقلال نمیرم ولی رفته خودش به حمید مریخ که ممنوع‌الکار هم هست، مندیت داده که شخصا با پرسپولیس بشینه و مذاکره رسمی کنه.
❌
با این ۲تا برگه که فاش شده، یاسر آسانی قطعا فسخ کرده و تایید هم‌شده. حالا هی شکایت‌ها رو رد کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/141109" target="_blank">📅 16:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141108">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
اعلام زمان نشست خبری تارتار پیش از بازی با نفت آبادان
❌
❌
زمان و مکان نشست خبری پیش از دیدار تیم‌های پرسپولیس و نفت آبادان مشخص شد. بر این اساس، نشست خبری سرمربیان دو تیم، فردا در هتل المپیک و طبق برنامه زمانی زیر برگزار خواهد شد:  • ساعت ۱۴:۳۰، محمد نوری…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/141108" target="_blank">📅 16:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141107">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
واکنش مهدی تارتار به دزدیده شدن گوشی همراهش : انتظارم این است که با دزدها برخورد شود/ کسی که همه دارو ندارش در گوشی باشد به راحتی دزدها می برند/ تمام خاطراتم در گوشی بود و رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/141107" target="_blank">📅 15:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141106">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
تارتار: تعطیلی ۵۰ روزه لیگ منطقی نیست؛ حداقل تو این مدت جام حذفی رو برگزار کنید، حتی بدون ملی‌پوش‌ها. بازیکن‌ها هم باید برای تمدید قرارداد با پرسپولیس جلو بیان، چون پرسپولیس تیم بزرگیه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/141106" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141105">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
نامه ای از یاسر آسانی که نشان می‌دهد وی به مدیربرنامه های خود مندیت داده است تا با پرسپولیس مذاکره کند
🚨
🚨
همچنین در نامه ارسالی به تاریخ فسخ اشاره شده است و این یعنی آسانی با استقلال فسخ انجام داده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/141105" target="_blank">📅 15:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141104">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
مهدی تارتار: این قدر کار در پرسپولیس سخت است و باید زمان گذاشت که نتوانیم در مورد تیم های دیگر حرف بزنیم
🚨
در مورد تیم امید باید بگویم یکی از بهترین نسل های خود را سوزاندیم. نتایج و کیفیت بازی فاجعه بود و در همین حد حرف میزنم چون فردا بازی مهم داریم
🚨
تیم…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/141104" target="_blank">📅 15:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141103">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
مهدی تارتار: ما قبل از تعطیلات شرایط خوبی داشتیم اما تعطیلی به دلیل نبود بچه ها به ما ضربه زد. بازیکنان شناخت خوبی از کادرفنی و ما از آنها پیدا کردیم. فکر نمی کنم به جز مصدومیت یکی دو بازیکن مشکل دیگری نداریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/141103" target="_blank">📅 15:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141102">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
تاتار: به فدراسیون فوتبال نامه زدیم که حاضریم بدون ملی پوشان بازی کنیم/ 50 روز تعطیلی هیچ چیزی به فوتبال ما اضافه نمی کند به غیر از تفریح و مسافرت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/141102" target="_blank">📅 15:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141101">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
اعلام زمان نشست خبری تارتار پیش از بازی با نفت آبادان
❌
❌
زمان و مکان نشست خبری پیش از دیدار تیم‌های پرسپولیس و نفت آبادان مشخص شد. بر این اساس، نشست خبری سرمربیان دو تیم، فردا در هتل المپیک و طبق برنامه زمانی زیر برگزار خواهد شد:  • ساعت ۱۴:۳۰، محمد نوری…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/141101" target="_blank">📅 15:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141100">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
دو بند مهم از هفت بند نوتیس ارسالی توسط آسانی به شرح زیر است
👇
🔻
ماده ۲ - دلیل فسخ
✖️
✖️
این فسخ بر مبنای نقض اساسی تعهدات قراردادی باشگاه از جمله عدم پرداخت حقوق و مطالبات قراردادی معوق و نقض شرایط و توافقات مقرر در قرارداد صورت می‌گیرد.
🔻
ماده ۴ - آزادی بازیکن
✖️
✖️
از تاریخ لازم الاجرا شدن فسخ بازیکن از تعهدات ورزشی و کاری قراردادی خود در قبال باشگاه فوتبال استقلال آزاد خواهد شد، مشروط به رعایت تعهداتی که طبق قرارداد پس از فسخ نیز معتبر باقی می مانند.
🚨
حال با تمامی این تفاسیر می‌توان با قاطعیت نوشت فسخ آسانی با استقلال رسما اتفاق افتاده و طبق تاریخ ارسال نوتیس فسخ، فسخ قرارداد و پس از آن مندیت آسانی به مدیربرنامه های خود برای مذاکره با پرسپولیس این فسخ در فیفا نیز ثبت شده است!!!!! مگر‌ این که باشگاه استقلال بتواند خلاف این مسائل را ثابت کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/141100" target="_blank">📅 14:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141099">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
۱۰ روز پیش از مندیتی که آسانی برای مذاکره با پرسپولیس به مریخ داده بود خبر دادیم و امروز این سند مهم منتشر شد
🔥
✅
نامه فسخ
✅
نامه مندیت
✅
استوری عضو هیأت‌مدیره شون
✅
مصاحبه‌های تاجرنیا
✅
اینها همه سند قرارداد مجدد استقلال با آسانیه
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/141099" target="_blank">📅 14:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141098">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
نامه ای از یاسر آسانی که نشان می‌دهد وی به مدیربرنامه های خود مندیت داده است تا با پرسپولیس مذاکره کند
🚨
🚨
همچنین در نامه ارسالی به تاریخ فسخ اشاره شده است و این یعنی آسانی با استقلال فسخ انجام داده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/141098" target="_blank">📅 14:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141097">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
نامه ای از یاسر آسانی که نشان می‌دهد وی به مدیربرنامه های خود مندیت داده است تا با پرسپولیس مذاکره کند
🚨
🚨
همچنین در نامه ارسالی به تاریخ فسخ اشاره شده است و این یعنی آسانی با استقلال فسخ انجام داده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/141097" target="_blank">📅 14:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141096">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-nmqR40Q7Y5n1YJsyEGHYQVY0aynXzM-lBkCWOh700wp7S4P6ieh1ESAlbaP5XIhpQZ_JfJsmaei1NByYJmYEnYVYigzHYveK2myuMWAUaiXXmmQvFfGM2laqfZzR2ZPalAYxJqbpm_ygJmu2VMzxKUtaG7MbjuK3WZZV55PRDwaRmjxrLEPu_lj1xKosQtNDhS2Hf3dDCmXudXc5fx3aQdxpjsuVCR0xk3dKyHMJIU9n5zGEVduniY2oCRiH06KbqQU45E36bHiawmrlRFhEhXz1m4xo-dpe4ZMjLsPTDM9KcFy8V01rRCxs_yqks_X-tN5zhMfJ2rtn8L2_Fbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووووری
✍️
حسین پنبه کار:
🔔
اگر لابی گری‌ و زد و بند های عجیبی در داخل صورت نگیرد ، یاسر آسانی حداقل ۶ ماه از فوتبال محروم و تیم استقلال هم ۲ پنجره نقل و انتقالات محروم خواهد شد.ضمن اینکه کسر‌ امتیاز و سقوط به دسته پایین تر هم میتواند شامل شود
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/141096" target="_blank">📅 14:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141095">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kg_1p1oPY4qA67X8a1KwCpOuAFOkjB0JuC2WkiUYnhdztl4_wfhDIAuUFRnDeHqppSO5kBkk_m7JUnwddgmqGXHePXz6KBxsmIl1OwIw9lanWEbSwQGLmLJUmi-qpNa6UDob7CFYs1KuMgN7Lw6joWNVkoJ8hJK9N1LMVLgJ-C9OkExpmKAwfCZ0Eg6-L5hWpvYry9RD4spsxDHaRvfjauGIALc6YoBUBT22EJ0cpVIn3gW2Bw4lsXxN3WT_U3i3SuQsXhV9a8yff9eLCaQMeWgsR3rSMfw-D5eRa1YW9jYFgNzK4SxH__jj21qHZ9ujWDx1j2oNlQRaDb23mrzIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد صدرنشین‌ها؛ تراکتور و استقلال برای یک شب سرنوشت‌ساز در تبریز!
🔥
⚡️
[
تراکتور
🔴
🆚
🔵
استقلال
]
⚽️
تراکتور با تکیه بر مالکیت و فشار در نیمه حریف، به‌دنبال کنترل ریتم بازی و ساخت موقعیت از کناره‌هاست. استقلال در انتقال‌های سریع و ضدحملات خطرناک‌تر است و اگر فضا پشت مدافعان تراکتور ایجاد شود، می‌تواند ضربه بزند.
سناریوی محتمل: بازی نزدیک و فیزیکی با حاشیه کم برای اشتباه؛ مساوی یا برد خفیف تراکتور محتمل‌تر به نظر می‌رسد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/141095" target="_blank">📅 13:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
«رسول باختر»کارشناس حقوقی فوتبال:  کسری طاهری چهار ماه محروم میشه اما نتیجه مسابقه تغییری نمیکنه. سپاهان هم یک پنجره نقل و انتقالاتی محروم خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/141094" target="_blank">📅 13:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/141093" target="_blank">📅 13:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔄
🔄
🔄
در پرونده شکایت سینا اسدبیگی از باشگاه پرسپولیس؛ این باشگاه به پرداخت مبلغ 14 میلیارد ریال بابت اصل خواسته و مبلغ 539 میلیون ریال بابت هزینه دادرسی در حق خواهان محکوم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/141092" target="_blank">📅 13:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
بیرانوند به کمیسیون پزشکی رفت؛ در انتظار اعلام وضعیت نهایی
🖍
علیرضا بیرانوند، دروازه‌بان تراکتور، روز گذشته در نخستین جلسه کمیسیون پزشکی در تبریز حاضر شد.
🖍
بیرانوند که به دلیل خالکوبی به کمیسیون پزشکی اعصاب و روان نظام پزشکی ارجاع شده، همچنین برای بررسی…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/141091" target="_blank">📅 13:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔵
رسمی؛ رضا شکاری به پیکان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/141090" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqKROSiYYMCGRhqfTePkwasQF_Kx4DlHTZdm-xZbNb5O1uYiYMlcGIx6SrBxFpYHFLPuMO1UHUwe6krTdRHIQtCqWJyPZo4_bP2pGZ0XBvBD6E4nnbg9b2hiGAKYDss_sCEiNVbegMQTa-oniK8GiGtC7KMhWxv6Mj5zVvOlnDXJJpyy0Vt074OV72m-XUG1TvhtGezy4gLPvfqT8hFwX1n2WdCxiJhc-Ret5L6piFAEfvBJ0vuBDZzpR_vJUhDlp9vXnpWc5SekVT7LWrWUVx13RU32FihvY_1-xF3GswUPP19_h-a0cmKWRx0-lUgE2ph8gJr9uYaF5zSwpVKb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
9 بازیکن جدیدی که وارد تیم بزرگسالان پرسپولیس شدند
🔴
1-
شاهین کیادلیری دفاع وسط 20 ساله
🔴
2-
امیرحسین طاهری دفاع راست 19 ساله
🔴
3-
آرتین محمدی هافبک دفاعی 19 ساله
🔴
4-
محمدرضا میرشفیعیان دفاع چپ 21 ساله
🔴
5-
طاها نژادخیر هافبک وسط 18 ساله
⚪️
6-
ارشیا محمدآبادی وینگر چپ 19 ساله
🔴
7-
محمد بزرگی وینگر راست 19 ساله
⚪️
8-
محمد مومنی مهاجم 20 ساله
⚪️
9-
امیررضا سینیکایی مهاجم 19 ساله
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/141089" target="_blank">📅 12:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141088">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
فووووووووووووری از ورزش سه
✖️
جام قهرمانی دوره بیست و پنجم لیگ برتر فوتبال ایران به شهدای میناب اهدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/141088" target="_blank">📅 12:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141087">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/141087" target="_blank">📅 12:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141086">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📊
فکت: پرسپولیس در تاریخ خود در خانه به صنعت نفت نباخته است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/141086" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141085">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGmFlRSQb7-juCZSyAkPLwpfONwU-PYzTgBNOOdNf49Ti08qn2A-yu3Jqcz0OAvPLdvuoB_SOGDqg1VLoeDdHlp7GZrDqjyYFvY6ubwy0gAsFtGiD3kG_mnN46fl_oxOuUqlVN41uw8aQAGX8tboyj_wF2hPFBuKLO4BZOpPuuGlyJsqbyVXUAZSoasIXaU_oHzFt7jV8Ihhr1dtijKnB3jFIu7ixh2gj8Uua3Ae0_Kq6xWxR76v0JE36Pg-d4n_UOaIyH0WRr1hiIiG9X0ImVA03wZNCxHA8-Sk4kBnlP9Odp9-eohMikN4Mp6B_Co64295aqEQFY-UstSGr2lyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
◀️
مجوز خارج شدن امتیاز باشگاه پادیاب خلخال از استان صادر نشده و باشگاه پرسپولیس برای خرید امتیاز این باشگاه با مانع روبرو شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141085" target="_blank">📅 10:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141084">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAtUzj2hiztgx1wMf7MAW79HYFE897b-RxFZ1eKrLA1Lp_Zdhjwx1UBgLk1LRGp7uWg29cX1RbcNJWxe-LpYotR9xQB8TKuXkYaQPSz5HdGiA1uNpexVHJDSnzQsKUbXlnCI7_pemJZS6egkiYyxZZtOMU7ih3GyCBN8-dg9o7L9Z61flDP7XHuS7ntKmRbMLtkOSxWSpgL24ra-QKtegwvbY_EkaCzS1QaCm7WdDefdTiBQDU0NXouLPnuGGPm4Qbvvn1GSPMzscToDVGDTrW570wCaP7zutCppqeV4pKC-OaLN1CpKa9AJ7L8k4SCW7Znqf3TBuwHJrH2Ff9y7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
◀️
سقوط تیم ملی پس از ۲ شکست اخیر
⚪️
فیفا امروز رده‌بندی جدید تیم‌های ملی را منتشر کرد که ایران با یک پله سقوط در رده ۲۳ جهان و دوم آسیا قرار گرفت.
⚪️
ژاپن، بهترین تیم آسیا در رده ۱۷ جهان قرار دارد و استرالیا هم با ۲ پله صعود به رده ۲۶ جهان رسیده تا به ایران نزدیک شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/141084" target="_blank">📅 10:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141083">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqyiTwevBliDDYJVmXAJFYRER3O1zEVsh-erU8wJ3l8SjjEFuIZFpBKMah8hrDhWrksGVjyCWZcubfynabtbx5ZJtdR_JfozqO3qOwp0dHnk1C6t4L1H01veKFH6oe8jugbV9LYWq69yGkgFJ9xOjSqD_3FO4Gu29ZO-Xb0cQ59Exq4ZeQg_kRbMmtkG86f3VLtGWG_2rp8_RIKuCp25iSJ5XcuPFySbhnEpslHcqg4BOiRt9UAr8NO3qnVT63ov025bbr4YCYfX7HibM-oarmluQm39Q2OoWAsjbLA-QH1uXpUFEB-5PUeIAdtD-MjpUNa7YJIBDXbvm5Hg4_FlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هفته‌ی هشتم لیگ خلیج‌فارس ایران
🔥
⚽️
هفته‌‌ی هشتم با چند تقابل نزدیک و کم‌ریسک از نظر گل آغاز می‌شود؛ تیم‌ها بعد از وقفه فیفادی معمولاً با احتیاط بیشتری وارد بازی می‌شوند و جزئیات تاکتیکی می‌تواند تعیین‌کننده باشد. تراکتورِ صدرنشین با خط دفاعی بسیار قدرتمندش مقابل استقلالِ بدون شکست قرار می‌گیرد و این دیدار می‌تواند یکی از فشرده‌ترین بازی‌های فصل باشد. در سمت دیگر، سپاهان برای تثبیت جایگاهش به دنبال پیروزی برابر فجر است و فولاد هم در خانه شانس خوبی برای کنترل بازی مقابل مس شهر بابک دارد.
سناریوی محتمل: بازی‌های فردا بیشتر به سمت نتایج نزدیک، نیمه‌های اول محتاطانه و تعداد گل پایین تمایل دارند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/141083" target="_blank">📅 02:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141082">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
فارس: مجوز خروج پادیاب خلخال از استانش صادر نشده و همین موضوع باعث منتفی شدن این انتقال شده.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141082" target="_blank">📅 23:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141081">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
هیئت ورزش و جوانان اردبیل با فروش پادیاب خلخال به پرسپولیس مخالفت کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/141081" target="_blank">📅 23:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141080">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FemMDH7Y2pEtO17Ey85VuPrCv4XnaX_Y61ACpwr-5lWSu_quyegY7Ee_Y8Z8aC7x7CywfgP5wfpoyNxmXaVTqMlg2a8S9q2n82obW_2_O8Pj1YxG9MHU-rG7ftI4UCLxZZlswdhoeyPG5C-jZ7pwLwCqrUZfZXrz8g10SeZeXD1-vDcdQmNr2jbqIRg_AxiS7k0NMnj37-bsBBP-8WKv5BW43mzCpJSX1nBg70L-_wOd4LcWmS8gsYOg5pKcv_8v1qVsLAhUmuwsWkaQItZRntNoE0kw--_9cjRG2ieFAFQpwOIJRx5r27o-fOebvnMDtK2_9uONV9s3C-4z2aoI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فکت: پرسپولیس در تاریخ خود در خانه به صنعت نفت نباخته است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141080" target="_blank">📅 23:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qm9CUcoXhZIxL1DemBsj1_4Afj4IVVBAw56XZy_v09XyaR_WvdCcRRe0gl7mSXyRsWeSZpWpmp3xoAL_J_Dsy_1cZ6TKVrLOVBfna7Oh9H1prvx-U5RceSEa9S-4hQslSWTV5RuVDE_pC2wAAmTwjWaaTDlAXVNxrB99eRNFAFKDimWJmkbmaG1fL4-VAPMJWj15ToXqe1Rk7r0Zyj7WUY6Qyo9SdNIZkFGKDL1ZlJG8uiTnm2WnIB5BSg2vBvrtg9a1NHIQC4yfVlv1Yqo0mO5a4AdZ0MR-LUD9OLlS6bEtNyQaqjndrVoSHUk12aNZElY3JBKtL17ffdVjVKdhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
طرفداری
:
✔️
پرسپولیس در صورت ناکامی در جذب محمد قربانی و استقلال در صورت نرسیدن به محمدجواد حسین‌نژاد، ممکن است برای جذب دهقان هافبک الوحده اقدام کنند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141079" target="_blank">📅 23:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
امتیاز پادیاب خلخال به پرسپولیس واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/141078" target="_blank">📅 23:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or_hXzC6Miu-Ie-_i8X1wcrgaEWai4-mQFXyNRgpi-bmlyqrvB3IVd0O1ArkKq8ZLnR3QRVmMmnv3z4_872kzWnjy5mr46JWgeUAuGs3u12mWPJNvwKOiLiEq22TGsYTL58uCCALtA1jxH8KudHwFxST4dKaEsXRmPnJVw3RqRIRZ_lXTWdGd3ZhjoQJ_K7dkjcjkwHBgH19eko74o7wRWYZLhiYAa3pzo0mrPTUV0Tt57q1Dm8MP6Gk37vrphVoWUZ381pyPaxMDvBvdF9hTnbEvUocC1tdeDHED_wFDrswmJeUfjxEeShzIHL7jAngTMnzySlsOu-r-LPHlxbY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
❤️
بیرانوند صبح دیروز به کمیسیون پزشکی اعصاب و روان به دلیل داشتن خالکوبی رفت، همچنین دستی که از ناحیه تاندونش مشکل داره MRI گرفت تا ببینه نتیجه‌اش چی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141077" target="_blank">📅 23:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9zlbCauaO85HP6w6XHHO99bqaPYGUlnCMR3IVW5ZlTJLq8-UkRaF4-FbrL7i5QzvL0v4i4CoKIHnQ8rOh0j-1fAA-EK0vx8zCiPHXr_33N34c6yzGyI_b-3ym-SVyOq72nD68MCcCnmK3yTk2XSux5rBlyZJVKMaXViHd9RJU8JDpbQ2kaQN4CHi7XIgWBWf6pgvPNfoTrL7BNPmbjrYo8iSy5E7xSkhfxj8dyXYzmFrKff5DO3IE7YNodtWt1VxEzko_WJTWeOnqlzu6Nvksoy-1CBEzVK_f1B8SyC58w7gy24OL0Q6nfVxBC1FuULUIdY5jS5F7nPEVP2skdhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#یادآوری
✅
✅
استقلالی‌ها بزرگترین خیانتکاران به‌منافع‌ملی هستن حالا اینا به ما پنداخلاقی از منافع‌ملی میدن
✅
✅
سال ۹۹‌ معاون‌استقلال مستقیماً به النصری‌ها خوراک میداد برای حذف پرسپولیس‌، صدای واعظ‌آشتیانی دراومد از این خیانت‌
⬆
⬆
ما مثل شما نه‌خوراک میدیم نه خیانت میکنیم از راه قانون ۳ امتیاز دربی رو ازتون میگیریم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/141076" target="_blank">📅 22:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
پرسپولیس و دانیل گرا بر سر فسخ قرارداد به توافق نرسیدن/فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141075" target="_blank">📅 22:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💥
#فوووووری  | #غیررسمی
🖍
یحیی گلمحمدی قراردادشو با دهوک عراق فسخ کرد و در استانه سرمربیگری تیم ملی امید قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141074" target="_blank">📅 22:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎙
🇦🇷
لیونل مسی: غمگین‌ترین روز فوتبالم است
✖️
✖️
امروز احساسات زیادی دارم، اما اولین کسی که به او فکر می‌کنم پدرم است.چیزی جز تشکر از این پیراهن برایم نمانده. ۲۰ سال، حتی در سخت‌ترین لحظات، هرگز دست از جنگیدن، تلاش کردن، تمام توانم را گذاشتن و خواستنِ حضور در…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141073" target="_blank">📅 22:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141072">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFlUciPxGE7bpsbCTSjPBZqWp5z34VLrV18xmYw5RfcYUWRSzgBl0UWqSPqHFMbxtvmtS9CbSF28zdwFjHdcutVTSS7F4iehNjvn7KTTH16lLPMl7YP8k4VN0mD6REJK-UPsRp-OSSx9CWfYTgmbjWBgL9RL3OjSv9KhL_bXDwgMj2WvqP6LF_UHAsNblDZ4oMgyXkeyfkY7qvDWkN6iYh6sNRp4HyPue-eMynAGI1Z5IeEhzCnPr9_2E1hJJaggzzKUQ-bUzHDL0YK2Zd65_hZ-1y_hUjFLO9shH3kvpY_9e6G2Vz-vV5MFF5N63Q5RrbBU_WIHd94kPL88Y-OhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام زمان نشست خبری تارتار پیش از بازی با نفت آبادان
❌
❌
زمان و مکان نشست خبری پیش از دیدار تیم‌های پرسپولیس و نفت آبادان مشخص شد. بر این اساس، نشست خبری سرمربیان دو تیم، فردا در هتل المپیک و طبق برنامه زمانی زیر برگزار خواهد شد:
• ساعت ۱۴:۳۰، محمد نوری سرمربی نفت آبادان
• ساعت ۱۴:۴۵، مهدی تارتار سرمربی پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141072" target="_blank">📅 21:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuJ1Y8U_7bOZD9iBPIF7-9HFJWLonrcLx3dsjYUJiugMJ7im3gSOB9c8FzJcC4bkAKYSqe3435Nk27YZi3pgxKymJndFsnC80q9OR97ZTWWrk7cr49T0y8UNVH1tCKjiwYeGZMvvafOtFRfflI0GugxbN69CskgLH7h5ErUQvrf0KIyS5VWLGf4tSidm0Y8Ra3a8DQDNb-LEJ6c6yy7EAFD21bloTV6rT2oCLZSZb8R_otjb70cfTjpvW4Qbalu06OwWqjEbVeFyRkmtcGAiuJahbcJPcpboUTLOZRJp5JhDKyoLMutFtnnpBytDeLM7dsGd9Ar4ut-tQLWQEMSunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری از تمرین امروز تیم پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/141071" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
رامین رضاییان دیدار مقابل پرسپولیس را از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/141070" target="_blank">📅 21:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79fbb819f6.mp4?token=QqHNQFoIRY8dVr5Uh1TsvL-dJUyT0z5P-AndGMdud0saRvgscmFRlF-feIqYEl0W6-HIJiYhknYESt4zD9CxjCIouUfcKVi0UjdETxIYdyrEShgzKaj3s4LXkvPfX0A1Sz3yVyKWJ_0wtDwLeVYaqaNxUM0m8nhRZlNobyYrT6fKd4rvojtbjv-kuijSg8zSZtVHyYRxkZ0JBNNNZ3k5tVHSJYQ9F-f7jYHW3xlhOhU0a99FxsejHUa7guOcTM7xMvC8MqBjQ_OFMlLtaVKlCCHkkQITUVp3Cb6QokQ4pnkwfR_T3DCdTy7cLFkbt9Zsr1fCcIYUH2vqUC_tDaO2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79fbb819f6.mp4?token=QqHNQFoIRY8dVr5Uh1TsvL-dJUyT0z5P-AndGMdud0saRvgscmFRlF-feIqYEl0W6-HIJiYhknYESt4zD9CxjCIouUfcKVi0UjdETxIYdyrEShgzKaj3s4LXkvPfX0A1Sz3yVyKWJ_0wtDwLeVYaqaNxUM0m8nhRZlNobyYrT6fKd4rvojtbjv-kuijSg8zSZtVHyYRxkZ0JBNNNZ3k5tVHSJYQ9F-f7jYHW3xlhOhU0a99FxsejHUa7guOcTM7xMvC8MqBjQ_OFMlLtaVKlCCHkkQITUVp3Cb6QokQ4pnkwfR_T3DCdTy7cLFkbt9Zsr1fCcIYUH2vqUC_tDaO2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل برتری تاجیکستان مقابل چین در بازی دوستانه توسط وحدت هنانوف، بازیکن سابق پرسپولیس و سپاهان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/141069" target="_blank">📅 20:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
با اعلام جواد نکونام، سرمربی تراکتور؛ مهدی هاشمی نژاد وینگر این تیم به بازی فردا مقابل استقلال رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/141068" target="_blank">📅 20:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
✅
احتمالاً در صورت غیبت کنعانی و علیپور، یکی از بین اورونوف و خدابنده‌لو کاپیتان پرسپولیس مقابل نفت آبادان میشه؛ بعد از اون هم پیام نیازمند بازوبند رو میبنده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/141067" target="_blank">📅 20:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV-mvUsEk5K6K1PqLcS4iMwMfRoMMBGcxv8-wv9DTnZhJQI5f1OLHnUgfRVScdeqIuc29FDfHlx4w-Tu103WFTXM1RlYdb5O1-2-AOQTtMEV--xDAxj9znhpeTC2gMgkagv2CXfAzkvIcnFTJklMuaWYVMKuRGx4ozZVLtj6FAFQJpfhvLIbfD51-UYjr_2tFEvkBoc_ri16ECd-x5Bgstf1G-XQL3c-mHMARYL-eass2mb-5EImT1VHX-hfWcEaB5-jaEDVUWCuRhcS1weHdkX677Hy8AKm1c98S_o3hft1aVXtSEkbOSDlT1OdOT4zEzyWuTWu4jhWWTuI3QN6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت‌ نود
🔵
کازینو آنلاین
اسپورت‌ نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت‌ نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/141066" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/141065" target="_blank">📅 20:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trw5TyWEBs2r5oBMCmY0lqlXNiNOkwfnP4Z_-23zmC_YMal5ZGM9o7g0DYmN_dgBkFP08rfrsmzRKBG-TfrSkOysai4jnTP2PSxC5TunA7V67LcaOUecsej03vH7dHMdxr-0m6eJGtSxcik5ccF_Mq2lZDz4tiJGOHv4qfOxU39kxSsnWm6_jpwUBWlyxIhcroJj674iIDTDjygpEbWK0pWCpacKz2oTwdyjPx2UmQ1Em6trb7UQuZmfoX_1hhh6DBKLl7HkQL6jXSfti7-5Zh_m03OJARunO7xewfkgV1rl2dQ1kHh54P9D16Ae0JlL9pu6yKZArscSzx6sowWtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
حضور پرسپولیس در رقابت‌های فوتبال ساحلی بانوان
❌
❌
باشگاه پرسپولیس با خرید امتیاز یک تیم، فعالیت رسمی خود را در رشته فوتبال ساحلی بانوان در لیگ برتر تهران آغاز خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/141064" target="_blank">📅 19:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3LBB6ZLypxSzYgzno0qCDX6uDZTmCjEt22VLcFngD8l_vXgeL2vHdr-wQSsbq43aBRrS3f50P0LN4u2Fd_o2aZaRTADImW8pen9nthLIzpfD2aEj5lEqlIBAA0zlz4CH7q6RoAPRaG-8BpacpiGou8UOjmfPSo_8mOCCVJTlzwAhDVcAs7TT3Z8bVZQHeRX-nkAtcYFd4AGYyRU7IrnpgqW4TEZBN5DFl6cx1HgFLtxKs7uP-sZaXS5XRjAE2buPjqZEkKoStgRlKHI6McWBrF3EKn50kh2NjsDG5WdoRkP9j36TkqrwcZXP_lBIdOpfzkeOP7P6pGkzseBUlFSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽
سیدجلال حسینی سرمربی تیم دوم پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/141063" target="_blank">📅 19:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141062">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
بازگشت سیدجلال به پرسپولیس!
🚨
اگر اتفاق خاصی نیفتد سیدجلال حسینی به عنوان سرمربی تیم دوم پرسپولیس فعالیت خود در فوتبال را ادامه خواهد داد.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/141062" target="_blank">📅 17:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141061">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWREwVApDu4SuTOno1MFSkuO2GAynjIo4gdgeaYZYKq2587ERIcabeffU1vlo7BlE9oX3GjRRgD_F60O6KKOjJg6hOfSVHHdqf3fguTo2QOonf_Bn6P5wgyeQvxCAj-IuE17H3b67nPExdnojTWsiEzND-kldP5b6WDJJ-4zgqwsMfBujzDofEJ_2VGSrTBzOot8AUeen-O3uXE81L5VbEvi_yBuJIHhET8MZJ3ZNbo9okJO5R3pHvl_re-yISlWkHyb_yg95lKriscAEJk-N4wC4zKurgdIUXSnRXf68cTYD-GdkiRNGGrB2nM2SEZZ5lc9gArbKmSb3mnpv3_FLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
❤️
بیرانوند صبح دیروز به کمیسیون پزشکی اعصاب و روان به دلیل داشتن خالکوبی رفت، همچنین دستی که از ناحیه تاندونش مشکل داره MRI گرفت تا ببینه نتیجه‌اش چی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141061" target="_blank">📅 16:44 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
