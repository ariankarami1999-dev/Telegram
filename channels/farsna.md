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
<img src="https://cdn4.telesco.pe/file/HLv7bH59l9VFbpCr08YO69vzu6n8OiPzmxHf0ZjDPHl-GDRagle4VTSh3eKDyme5OxTsFFNQmHvvTSZMcKRzuL3prpBLRp5VzEttwo8Nej1qW2-L3RYMy-41Do66JAu5I7PXOuSxkAwtLy4ZeykgF_yCV5-nEE-lAapPjI3wg7hbXg4ge_wDpeYER9Y7zVUM2DWxqFrVzf1Xa0wgWdwZfSylD8QarapypDAca7VGEArnz5mI8umMXR17t4V23V9wQirTBVFF4sOqvQwoF_8-pVMX612NeDDPscIu0uE19YbGEKUkcxhPQXQlNsSN6Sd2qxYeZAcJdgYO4WhaGhPN5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 21:31:18</div>
<hr>

<div class="tg-post" id="msg-454638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgtYb4eSKKW-MS-o-a7uoVOtfjxB5ncLYULi0741J0Bx_HQGEX5CW6y5Z55-dv8Okpco3lKJSeFiGU2417ApidTVKoOgcJco7vNraTibTc9hYDi53nyCg87h2nRkYuTAdwMGIJsYQd5HYMW2MVaj63Q1M3PLopnzca0XPqMvAnckuAmZ7GcndGL54cGlzCTue9bVD2mh-Dc8GGHL_c-MOu_e37E0IBf3A2hV2-EkiPb_XRS7x6xO8ENdr28LcW-5ErpJaj8Su64dvxpPq9OiqJkSMaiSVJ7Zis59u4Sn87eZSuUSVCreL78JyGc4Tn7LwTE3eBRK9THYktZOaIsLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال‌های تاریخی بزرگ تلویزیون در راه‌اند
🔹
تلویزیون این روزها تولید مجموعه‌های تاریخی را با جدیت دنبال می‌کند. از پروژه‌های عظیمی مانند «سلمان فارسی» و «موسی کلیم‌الله» گرفته تا سریال‌هایی مانند «رئیسعلی»، «حماسه زاگرس»، «دیوار دفاعی»، «کارآگاه علوی»، «شکیب عیار» و «نگین ارباب» که هرکدام به بخشی از تاریخ ایران و جهان اسلام می‌پردازند.
🔹
اگر این آثار بتوانند شخصیت‌های تاریخی را باورپذیر و جذاب روایت کنند، شاید بار دیگر شاهد تکرار موفقیت سریال‌های ماندگاری مانند «مختارنامه»، «امام علی(ع)» و «یوسف پیامبر(ع)» باشیم.
🔗
اگر دوست دارید در مورد این سریال‌ها بیشتر بدانید،
اینجا
را بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/454638" target="_blank">📅 21:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454637">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e6ae32867.mp4?token=CuVe3lc8eBL_2PDfqColy1nVW21wR8IcsboXtDV1obLlANs4yIYLFesq3zLxz6AWau4uj0IW408DBAgZVHbkIt9oWsDnZbGgpROB-4iePKdKpBGM62k--JX_DPNPbB_AQgdpaWqNSz3656Alccwl8Hc8CNn6uwJQUbC--7FHvy49i4FbHDN56C4z0ukRWJlRbdrZsXHKvFafk3mvg72kB06UTqE6WSXRWwGp-R9ds1c_lurJug0EuMFloYqsuyaHLNjYTzyFEGpcoH_etMxX-4UwF4jauT9glNUlZw2HO-y1JsamGs7Wc857mXVpvs0VJoviTD8d9djdkP3gR0iZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e6ae32867.mp4?token=CuVe3lc8eBL_2PDfqColy1nVW21wR8IcsboXtDV1obLlANs4yIYLFesq3zLxz6AWau4uj0IW408DBAgZVHbkIt9oWsDnZbGgpROB-4iePKdKpBGM62k--JX_DPNPbB_AQgdpaWqNSz3656Alccwl8Hc8CNn6uwJQUbC--7FHvy49i4FbHDN56C4z0ukRWJlRbdrZsXHKvFafk3mvg72kB06UTqE6WSXRWwGp-R9ds1c_lurJug0EuMFloYqsuyaHLNjYTzyFEGpcoH_etMxX-4UwF4jauT9glNUlZw2HO-y1JsamGs7Wc857mXVpvs0VJoviTD8d9djdkP3gR0iZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بی‌بی‌سی و اینترنشنال چگونه بین خود تقسیم نقش کرده‌اند؟
@Farsna</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/454637" target="_blank">📅 21:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454636">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3f36ea27e.mp4?token=CRLzcOGUDDFf3FVFdrgt6YT7JXYBg5GLhFlPpyKUaqjnfAqwvyOOE5q9kSF4ctAMO6RMq-0vW19E6ojDLCwY8vNhM5M8BzDSnutFkEtekSy5QgVfuY6Zb6zkyPoEIx8kwEOpGLI1_IfcqMtok1O6Naf3T__wi1gejOkUbE62zkaxvRhZKEqXWNuXlQs-tkM6UJGHOUCPmJupbfBP5Pu8oZHlbyrUDcbEoLdrhIpx9p9cEd3FY2tSvnpOnvL6rHww102XzQKzwvKUl82g1ugipzJtext5_V3Q1YJJdUlrH70PjbSfiWHugmb9FITfL1uZ9E0mkJeOI2eflmrw_XkHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3f36ea27e.mp4?token=CRLzcOGUDDFf3FVFdrgt6YT7JXYBg5GLhFlPpyKUaqjnfAqwvyOOE5q9kSF4ctAMO6RMq-0vW19E6ojDLCwY8vNhM5M8BzDSnutFkEtekSy5QgVfuY6Zb6zkyPoEIx8kwEOpGLI1_IfcqMtok1O6Naf3T__wi1gejOkUbE62zkaxvRhZKEqXWNuXlQs-tkM6UJGHOUCPmJupbfBP5Pu8oZHlbyrUDcbEoLdrhIpx9p9cEd3FY2tSvnpOnvL6rHww102XzQKzwvKUl82g1ugipzJtext5_V3Q1YJJdUlrH70PjbSfiWHugmb9FITfL1uZ9E0mkJeOI2eflmrw_XkHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشیمانی پویانفر از برخورد با شهید لاریجانی در اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/454636" target="_blank">📅 21:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454635">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d32835d80d.mp4?token=n099wcwrqyrAfUbIYiGSGsVc7rZW-D5AH4bROA7hA7aFB_f34fsjnuDWiVnFhVm6TTWMtkSd176t2-AhLOPD1pUDjK4b1PrnUtiNMbMQQe5woPPN900enyeZZkEFVZpuO78hM49uwArELzL5_rYWnVqB_JDgHkx2p6Hv0Nwq_4fRrugyqqJzMRcgVGLz59hMsb0nWFFsp0JliBEQQ5cTE4JkDyCo4wD_xF7eJkGDB4XosU-G166h9_gtvgHiRxmfJh6vedQetCFq83jsl38qsjz6UO2KwUeIvxnlEFNCE3vo6o0opN-FHcC7T7Q89EiurWdPIryxWPRvhX4RiPqMIG7lLywTf3v_bLg28cBs0KsHAJ1j3rYiQd0cMnC-Ibu53B89vdcNydyVlZUffJSrE96UOZUbPYGEnL9zzACBP2oMFxN0KdBmGuuZ-UB50WTtwyaiRLwyo0q7fSYY3EzTDYq7NajVrOl7E5QrF88J8B6M89JpWfKUNoFWL4fiAaEkag7gvF5ZlKG1vDX3eM3yE8hkcyGPu3uie8l6vs3Ny6-yFS1MyeWQYpF1Dki7peAQi5qMBMhMdrdK-KyTlR92yugyFMuWqq_62WN9A9FVl2T8hfxGyE1PwrvLMDlL3oohSu8OchzJ09RMlqb4V2WkaBVbWNU25GXO4U2ha2_BhD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d32835d80d.mp4?token=n099wcwrqyrAfUbIYiGSGsVc7rZW-D5AH4bROA7hA7aFB_f34fsjnuDWiVnFhVm6TTWMtkSd176t2-AhLOPD1pUDjK4b1PrnUtiNMbMQQe5woPPN900enyeZZkEFVZpuO78hM49uwArELzL5_rYWnVqB_JDgHkx2p6Hv0Nwq_4fRrugyqqJzMRcgVGLz59hMsb0nWFFsp0JliBEQQ5cTE4JkDyCo4wD_xF7eJkGDB4XosU-G166h9_gtvgHiRxmfJh6vedQetCFq83jsl38qsjz6UO2KwUeIvxnlEFNCE3vo6o0opN-FHcC7T7Q89EiurWdPIryxWPRvhX4RiPqMIG7lLywTf3v_bLg28cBs0KsHAJ1j3rYiQd0cMnC-Ibu53B89vdcNydyVlZUffJSrE96UOZUbPYGEnL9zzACBP2oMFxN0KdBmGuuZ-UB50WTtwyaiRLwyo0q7fSYY3EzTDYq7NajVrOl7E5QrF88J8B6M89JpWfKUNoFWL4fiAaEkag7gvF5ZlKG1vDX3eM3yE8hkcyGPu3uie8l6vs3Ny6-yFS1MyeWQYpF1Dki7peAQi5qMBMhMdrdK-KyTlR92yugyFMuWqq_62WN9A9FVl2T8hfxGyE1PwrvLMDlL3oohSu8OchzJ09RMlqb4V2WkaBVbWNU25GXO4U2ha2_BhD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردمی که با تمام مشغله‌ها همچنان شب‌ها میدان‌داری می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/454635" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454634">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بازداشت عامل ارسال تصاویر پرتاب موشک به رسانه‌های معاند در یزد
🔹
دادستان یزد: شخصی که با تصویربرداری از لحظات پرتاب موشک‌های ایرانی، این تصاویر را برای رسانه‌های معاند ازجمله ‌اینترنشنال و یک کانال معروف معاند ارسال کرده بود، در یزد بازداشت شد.
🔹
با توجه به ارتکاب این اقدام در شرایط جنگی، امکان تشدید مجازات تا ۳ درجه وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/454634" target="_blank">📅 20:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454633">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi2xW7mK0Bf9HX6gi9zvVIC8cGHzOUlgEHKehM2_Tb7MLk7LOrscqJaRiScvnSAp68sUzLAbMQw-vtJUk6MtjCDXRLQqeMqZ-A2-U6AvpB91c4TUPtmeC5oz9ibW_VRGwZeksb7Nc9TbmFTyPTxGjPAIqtOWQcpB4ttCNjjIGMBuJc1b4floG4DaDuW8ZuwHPxGhIJIhOTRxBCgNAZ2RAZ92f1Wlq7BYqO296ZI4tznMhnutpV6NVH-UjLGBdFjozovadDrlvrG8uKtoJkXURugTd2F6snclcZi7-nU-VZU7M9w6sUN8zotK4RcOSkju-E_VJdu73VC5kGy7Cc0vxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایزنی وزرای خارجۀ آمریکا و انگلیس درباره ایران
🔹
وزارت خارجۀ آمریکا اعلام کرد که روبیو امروز با میلیبند، وزیر خارجۀ جدید انگلیس درباره مسائل پیرامون ایران گفت‌وگو کرده است.
🔹
طبق گزارش وزارت خارجۀ آمریکا ۲ طرف در این گفتوگو بر تعهد مشترک به عبور ایمن از تنگۀ هرمز و تضمین دستیابی‌نیافتن ایران به سلاح هسته‌ای تاکید کرده‌اند.
@Farsna
-
LinK</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/454633" target="_blank">📅 20:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454632">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌ غریب‌آبادی: موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد. @Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/454632" target="_blank">📅 20:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در محدودۀ جنوب اصفهان
🔹
سپاه استان اصفهان: فردا از ساعت ۸ صبح تا ۱۴ احتمال شنیده‌شدن صدای انفجار کنترل شده در محدوده صفه، سپاهان شهر و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/454631" target="_blank">📅 20:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌ غریب‌آبادی: طرح جدید به‌گونه‌ای خواهد بود که هم در مسیر ورود و هم در بخش‌هایی از مسیر خروج، کشتی‌ها از آب‌های ایران عبور خواهند کرد. @Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/454630" target="_blank">📅 20:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌ غریب آبادی: با اجرای تفاهم جدید، مسیرهای موقت در  تنگه هرمز بسته خواهد شد
🔹
برابر این تفاهم، مسیر شمالی که در نزدیک جزیره لارک ایجاد شده بود و مسیر جنوب که در آب‌های داخلی عمان است، بسته خواهند شد. @Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/454629" target="_blank">📅 20:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454628">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌ غریب‌آبادی: مسیر جدید در تنگه هرمز موقت است اما می‌تواند ۲ تا ۴ ماه یا بیشتر معتبر باشد.  @Farsna</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/454628" target="_blank">📅 20:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">معاون حقوقی وزارت خارجه: دخالت خارجی در تنگۀ هرمز را به هیچ‌وجه نخواهیم پذیرفت
🔹
تفاهم دربارۀ تنگۀ هرمز باید صرفاً بین ایران و عمان انجام شود و ما برای هیچ کشور دیگری حقی قائل نیستیم. @Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/454627" target="_blank">📅 20:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">معاون حقوقی وزارت خارجه: دخالت خارجی در تنگۀ هرمز را به هیچ‌وجه نخواهیم پذیرفت
🔹
تفاهم دربارۀ تنگۀ هرمز باید صرفاً بین ایران و عمان انجام شود و ما برای هیچ کشور دیگری حقی قائل نیستیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/454626" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476b901163.mp4?token=JcaT26qGRv2V_ZJ5UwYu6g4NqgOt0clQOho3jFpTdBdc3bLewQNo2t8F661SSDNua3qpJeeMYjHGtosHURJmS7b_h2LCqkBCs_C7gNml7gu7MD4OwXwLmjGaZr9U106FF60JkZ5b0gdS3rz58VYRxnzuexKn9eImSFVL5ayK3qEPElTPMG_ZJiTs3C29frPpLlvaSg0jyAMJnwxB3uZL6xaCh_sXPXEcozXBD1WNpt92UIlegB4WeJtLM75D5YjfAwZaO-JBX2Tp26FrUMsCq8ZLsChjEjh3YCTbIFk-tRCXLh-e4PiYTvsLBIkscPpm2xQHw66p4ATb3q8I8QV9nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476b901163.mp4?token=JcaT26qGRv2V_ZJ5UwYu6g4NqgOt0clQOho3jFpTdBdc3bLewQNo2t8F661SSDNua3qpJeeMYjHGtosHURJmS7b_h2LCqkBCs_C7gNml7gu7MD4OwXwLmjGaZr9U106FF60JkZ5b0gdS3rz58VYRxnzuexKn9eImSFVL5ayK3qEPElTPMG_ZJiTs3C29frPpLlvaSg0jyAMJnwxB3uZL6xaCh_sXPXEcozXBD1WNpt92UIlegB4WeJtLM75D5YjfAwZaO-JBX2Tp26FrUMsCq8ZLsChjEjh3YCTbIFk-tRCXLh-e4PiYTvsLBIkscPpm2xQHw66p4ATb3q8I8QV9nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده قرارگاه نجف اشرف سپاه: مرز سومار می‌تواند در سال‌های آینده پایانۀ اصلی تردد زائران شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/454625" target="_blank">📅 20:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454624">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-text">بحران عجیب کتاب‌های جعلی در آمازون
🔹
جین فریدمن، نویسنده و تحلیلگر صنعت نشر، به‌طور کاملاً اتفاقی متوجه شد چندین کتاب جدید به نام او در آمازون و گودریدز در حال فروش است؛ کتاب‌هایی که او هرگز ننوشته بود!
🔹
اما او تنها قربانی نبود؛ کشف کتاب‌های جعلی مشابه با نام «کارا سویشر»، خبرنگار سرشناس حوزه فناوری، نشان داد این کارخانه کتاب‌سازی دامنه قربانیان خود را گسترش داده است.
🔹
زمانی که فریدمن این کلاهبرداری را به آمازون گزارش داد، پاسخی دریافت کرد که مسیر این ماجرا را به یک بحران بزرگ‌تر تبدیل کرد.
اینجا
بخوانید
@FarsnaTech</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/454624" target="_blank">📅 20:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454623">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لغو چند تحریم عراق ربطی به تفاهم ایران ندارد/ برخی شروط بازشدن تنگه هرمز
🔹
یک منبع نزدیک به تیم مذاکره‌کننده: برخلاف برخی گمانه‌زنی‌ها و تبلیغات رسانه‌ای، لغو تعداد معدودی تحریم از جانب خزانه‌داری آمریکا، مرتبط با تعاملات دولت عراق با واشنگتن است و ارتباطی به تفاهم‌نامۀ ایران-آمریکا ندارد.
🔹
آمریکا با نقض تفاهم‌نامۀ اسلام‌آباد، روال‌مندشدن ترافیک تنگه را بر هم زد و علاوه بر حملات نظامی و ایجاد حصر دریایی، با لغو معافیت‌های صادرات نفت و پتروشیمی، مانع از در دسترس قرار گرفتن پول‌های بلوکه‌شدۀ ایران شد و بازگشت شرایط، منوط به برپایی تدابیر ایرانی در تنگۀ هرمز و عمل واقعی و عینی آمریکا به تعهدات خود است.
🔹
این منبع آگاه تأکید کرد که درصورت نهایی‌شدن تفاهم ایران با عمان، بازگشایی تنگۀ هرمز مستلزم ترتیبات جداگانه‌ای است که شامل انجام تعهدات آمریکا هم می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/454623" target="_blank">📅 20:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454622">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKzwAnqZatM-X5bbYBpVE1oMLJWrsQEqRNoC0Q2r3Se91x2yV2O5xKH5ixVSlnHNnG_NmOtfRaweMMf1hEIN8ntG_onI4t23DZbMWBj_w0sAwRRKed1_05RDXkRxjyakh2ngFetFR4Gg3cCXb1x2er9b3bUN0SdXXk2yyqytjquAOkMzRUvPp52UXRzACR809hwRfnD-fw0aFp_Ivra9mYNhM9xLGMlqtUuATUWDXBzTaNH5Jy1gWR-OFmxkRfc28IR2J-sMzjEYLqOkbzwPHehp3rCwJzigpT3eTfhE1nRiLmteKB53p_U6URf8JQn84hYWTMAPy-43p8_uYYlK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی انگلیس از وقوع حادثه برای یک نفتکش در فاصلۀ ۹۵ مایل از شهر عدن در غرب یمن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/454622" target="_blank">📅 19:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454618">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hP5BA83PoEHB_ap_zzKXK2h6rPGOSCHipiEulBMdhjneirilahv1gBHbr6e3IoKHvdIgPbH2MVl5DQ9mob8O54gBIqUDOwndOp95vGvKgSFGGn3O_GJN9WOjTEMM3p4pCL_ERUBMriWW6_UX46JCCmoXV_rB1PsAdD7K6H0mPXA4vhIiGI9LrwzvgMM4WoK3UbhDXPAmf8hDvpkbGLjxTgNcXvH57R8tqWpwclk0Q2hob88b5iXraztY79cqXFaMD_RRywxW-iJ1FoD1vBZArbPGhCj7wCH6gT7zczEEodz5fk8lQ0fGd7EzmcIswwU6f9WF_ymWQEMSqXsOoCFuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vSvGoHinRTB1_fJHCCQgCSXzcb7b2J7Fuy9UxLZLQfAwbacAYBNMlzqzgePDgcreHb1mT_C9kNzYl72k33ul0nlDhrofnjXGKQ9E1QdrPFZ29RShsE_HSexrJzfkp1gaqCAgfYOWg1LkTCt8-17qr8wh8u3U9XywJTV4Y-b6zB1-mj75xAI4JphoKf1MJqfODqIJjn2CYt3LcqIHITRx6JFb_0MG6s5GUGxDabZnOH5WapQRFrVDAyQk_2PvMoOInUfE8B25bZklAb65kY8soWRWNuhIVhuDGszwMJ__bnr4vUUfh0jV59GP_y2Ntya7C-IFvFWw5xwhYT9OFLWOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcfSBhfkn6Hh1I3xnFTPWJzusrNSkLUU6jdMQg_YiiRDJzILNMQMa965wur8-c7cqcL1eM_0ozIYHrJDiPZhGMSOE9VtV6awFRSWwm2aPAEinbSUZciH-2q96pzWTgLuratnkdSG4Bmn6NmpsxYR86LEITClxN5DAjDweYXG0S34UF3gkxJHmOJk6XJXazV9jmTePQ8_Wd3C5uLmvGyYnstbiSOwIZBsxdRHldOnXjiXu3Kl_R2vCoWq5v-aIz5enpOBmozFn1FmAbMXKmAaE61Bvw5x6fZ6H-EVN0dX87AdNsrEcQBZCGXpCTsfAszzjKKtA3MMJ9n6jNAY6Ke9lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4jX56c_sTUTXmHR-cqd9XAJfPCp0kZtIvTGva7XXGyliF6CptCE4MczwheU3X-KwiujnOmiHQ3e-nzMHkX6qGYgJ_JKLMzV-l6Oqrl2ynTgG5Lm18-vaw4sbCLDpc9HyAjttK70KYw2dGa68ULji7j0DpnDeNamiS8BBCKn9yCbXMY8cVUpJbbyK8CTc2GbEsn8NvgZ3PHDd0j2O0vqujtn8maMYhfZEF8XRSowTZrshDTvQ9oJmWz5Jrp-snbS5dLHbHnTlMfczJN3fv8eK2YGWP-FcZs7o3YBEvi1tICtDah10YT5UGiZe9hMTyVaZb4tjkcEvQkTM35XwYardg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید وزیر بهداشت از محل جنایت آمریکا در لامرد
🔹
ظفرقندی باحضور در شهرستان لامِرد فارس، از بیمارستان این شهرستان و محل اصابت موشک‌های امریکایی-صهیونی در مجموعه ورزشی مرد که منجر به شهادت ۲۱ نفر شد بازدید کرد.
عکس:
محسن نی‌دانی
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/454618" target="_blank">📅 19:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to8QcT2skVWz037DMuC4OiBZAB1Bj99eYAfgwd30aUy__GrH7gZb0Zx1CVMchkAZCsPJwGzvQXR-oxmQ0ZKSwUo1hLpIl6n4b45bJMCtlTaNGGgcYydwckB5vfktNIwtO6Z2Ghp24HVkzMCtVAOmRpyIPpCm7t167thp3JDJT6ef-wIk1DKBXtVchNjEiNnTtcIbYrZrpqcCJZrK8r-6dxD8iMRkOfWaijzKpZoH0YKtY8FXtiHGpGUzottHXbrJ24Z5B5ydEGHSASkQvTsDKUWiZ5xsiYuFJJaa_DgQ3ebfPLHvcjIRnd91aqIcFhUY_ZgsXmrrV64SVX956woDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: برنامه‌ای برای سفر به پاکستان و قطر در پایان هفته نداریم  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454616" target="_blank">📅 18:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سخنگوی وزارت خارجه: برنامه‌ای برای سفر به پاکستان و قطر در پایان هفته نداریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454615" target="_blank">📅 18:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454614">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1410fe62a.mp4?token=rYOUjHLVTpctQazveFFt1UlN5rBmkAp6BSHxz4AjNAW-GhEHndy3w8gxEzoq9e_3SAa1eLHjjviPZ8fP6BbYVBKzJ53KqJeACaOnuvy3mKdMGIFfdxGPCirseuNSV1dsKy8t3T9pU3TG33DmN39fNCLEXbv2UnkIn4VdzTv_IEYG38sa98FCsH0greSkWVVzXa5zZ0VRCzhbnSCldZuGeculnaNW26WnwtE4avRJOEkbXGM5wwMlVqt69J6kI4dFKnYLd5gok180DmZjYXQm-jwhq_HEKnemuUFMoV7FF_EyIhKhWLElq8_8ExhJEIlngpLZ-TbtNu_W1lecspKFZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1410fe62a.mp4?token=rYOUjHLVTpctQazveFFt1UlN5rBmkAp6BSHxz4AjNAW-GhEHndy3w8gxEzoq9e_3SAa1eLHjjviPZ8fP6BbYVBKzJ53KqJeACaOnuvy3mKdMGIFfdxGPCirseuNSV1dsKy8t3T9pU3TG33DmN39fNCLEXbv2UnkIn4VdzTv_IEYG38sa98FCsH0greSkWVVzXa5zZ0VRCzhbnSCldZuGeculnaNW26WnwtE4avRJOEkbXGM5wwMlVqt69J6kI4dFKnYLd5gok180DmZjYXQm-jwhq_HEKnemuUFMoV7FF_EyIhKhWLElq8_8ExhJEIlngpLZ-TbtNu_W1lecspKFZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیویورک‌تایمز از برنامۀ مخفیانۀ ایران برای فشار بر ترامپ می‌گوید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/454614" target="_blank">📅 18:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454613">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قیمت جدید بنزین سوپر در بورس انرژی ۸۴,۶۰۰ تومان تعیین شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454613" target="_blank">📅 18:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4np08KS3Z5eLW6NzCauyYjfphBCwNB0_R7BkIUGECa72i2f4arhQ7BDK1erznH7l9Y-3Crg6dtZjtccuCKX1XWFCGUEJ6mvnN8Cp7GkglIclHNjoZItt6QUQZ1RF1blZuEL0yV7V2pKGA8Gr4Bj5fzVrZ9kPi8Bzhhn0sjcGrH6aR-LLQN1Eu59_0gGa4I7G3wNv0Kvc_hKQIe_4JiP6P4bfbgVf4eX9U0vvAF3W1ASGPBIJbsUqW2pzFp6nVorbpEHRyQeE8C9xhyGgndilwBY5Fe2G5OFkv79sr7pTGGSVnOJUf7MwG20GscGCOe9Kfv7_sW4NhrigH2NNBsWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالیشاه به سیرجان می‌رود
⚽️
کاپیتان سابق پرسپولیس که پس از ۱۳ سال حضور از این تیم جدا شد، فصل آینده فوتبال خود را در سیرجان دنبال خواهد کرد.
⚽️
مذاکرات میان عالیشاه و مسئولان گل‌گهر به نتیجه رسیده و طرفین بر سر جزئیات قرارداد به توافق رسیده‌اند.  @Farsna…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454612" target="_blank">📅 18:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454611">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تحریم‌های ضدایرانی شرکت عراقی رفع شد
🔹
وزارت خزانه‌داری آمریکا تحریم شرکت هواپیمایی «فلای‌بغداد» و ۲ هواپیمای عراقی دیگر را لغو کرد.
🔸
براساس ادعای آمریکا این شرکت‌ها به‌دلیل ارتباط مدیران با ایران تحریم شده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454611" target="_blank">📅 18:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454610">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e740dea4f0.mp4?token=SRSJWIlrkbuyPsGhkMM1FRRuRt0Mh3t3LuvY5iadyRnedUaVE5mUJ0pgoee2UN0UENiJGvtapGype1rrTdlW1xOVSQ418bN5CL_jUgxOHQ0Z1ZwfHudLg0N80FDrMPsVglzzOmvPMYnL1lf8J3ILNUn0Y1_ZLcDhLFz1O4VP9_cQcrLoM-PiL0PtfWozO32g4N2sCrVhhhGQkjI85C7kE_VuMm2o4FGMXJsp1dMYcK4nuMhtEEoK28KiuHD635MFvwN3nnJXNgf0_SI8o5POLwDBinZYNITlHZe2gtSrD6VNkBrvVN2nwF34V17evcFZblELRLk-syADyUFxHubMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e740dea4f0.mp4?token=SRSJWIlrkbuyPsGhkMM1FRRuRt0Mh3t3LuvY5iadyRnedUaVE5mUJ0pgoee2UN0UENiJGvtapGype1rrTdlW1xOVSQ418bN5CL_jUgxOHQ0Z1ZwfHudLg0N80FDrMPsVglzzOmvPMYnL1lf8J3ILNUn0Y1_ZLcDhLFz1O4VP9_cQcrLoM-PiL0PtfWozO32g4N2sCrVhhhGQkjI85C7kE_VuMm2o4FGMXJsp1dMYcK4nuMhtEEoK28KiuHD635MFvwN3nnJXNgf0_SI8o5POLwDBinZYNITlHZe2gtSrD6VNkBrvVN2nwF34V17evcFZblELRLk-syADyUFxHubMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالاخره نردبان هم تسلیم ربات‌های انسان‌نما شد
🔹
شرکت «فیگِر» ویدئویی از ربات انسان‌نمای «فیگِر ۰۳» منتشر کرده که نشان می‌دهد این ربات می‌تواند بدون دخالت انسانی و به‌صورت خودکار از نردبان بالا برود.
🔹
بالارفتن از نردبان یکی از چالش‌های پیچیده در رباتیک محسوب می‌شود، زیرا به هماهنگی دقیق دست و پا، حفظ تعادل و درک لحظه‌ای محیط نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454610" target="_blank">📅 17:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4_6aZhJyvxinoRi278F-kH3wUjZZ1fChXXc4prw7HL9k-_GITyN2WtcxH4t8b_hfdK6y_u2NHaxj0tT_BGmwttIKx0_8NgRV8O74BjvzkNSmrS4kMGD9NdMOEDUNeIyQK8HD09i9uyXxjhbtxjdHbcUs8TgMiVmEpxfJVwtLrTt1v6iFaUtFfkWsj_FMUdXKt0t_ZE-5gFQHYK1eJXg8bI4EQIPKqSjgCjeQRDABZ7acmO6UybjUqmDsMUpy3-gOqWwT2U2ogJvp83gt5pX8wZ9aD_ZqTSQCKXy6Tj5fzfeHwFqxWS91a_cFLcZjGNjOT9Ac0In6Qfiy8V6516NXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان پرسپولیس از این تیم جدا شد
⚽️
با اعلام باشگاه پرسپولیس، امید عالیشاه کاپیتان چند فصل اخیر سرخ‌پوشان با توافقی دوجانبه از پرسپولیس جدا شد.
⚽️
همچنین میلاد سرلک هم به شکل توافقی از قرمزپوشان جدا شد و مجتبی فخریان هم به‌صورت قرضی به گل‌گهر پیوست. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454609" target="_blank">📅 17:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454608">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f3cf356d.mp4?token=vgxYyypBH5-pGX1QFtbB7WGodOi2Pycbs4WSici8HfdFQC_2q3TvRQN8qN187ViVRIeNy_2a_PjtYk7PHMAyYk5g3PL0OQinhlLNnZaDSC_Gtoo6xW67VVFQHqWSKGNcVs0J0wrD4pukzxyVdO9obNqBfRpS2tKwalK62RJue6ZResbnIJwa449nsoVmR6xfkN0UgpM98Y4QqqGQRwn6sLkXq5PaywCmsKUIh1XJhRnNrBBtAzWwtJUv0T2qbj-79EYAXLLw1FhhKKfA2X7huGV2IoQXMrGtYLcDD0tHf8J_caSB9JiDB5cnmo3nMT_TtqWCsJpeSagkZ8tiiBeNxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f3cf356d.mp4?token=vgxYyypBH5-pGX1QFtbB7WGodOi2Pycbs4WSici8HfdFQC_2q3TvRQN8qN187ViVRIeNy_2a_PjtYk7PHMAyYk5g3PL0OQinhlLNnZaDSC_Gtoo6xW67VVFQHqWSKGNcVs0J0wrD4pukzxyVdO9obNqBfRpS2tKwalK62RJue6ZResbnIJwa449nsoVmR6xfkN0UgpM98Y4QqqGQRwn6sLkXq5PaywCmsKUIh1XJhRnNrBBtAzWwtJUv0T2qbj-79EYAXLLw1FhhKKfA2X7huGV2IoQXMrGtYLcDD0tHf8J_caSB9JiDB5cnmo3nMT_TtqWCsJpeSagkZ8tiiBeNxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین دردسر والدین برای ثبت‌نام در مدارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454608" target="_blank">📅 17:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9Z_AYPcKIn4EAu3fwbX42SSAOyzYN4os-xSLyuaVCAMc2BH8aRw3z5-yxiLABiTtQMgZwPVVyqnxmo63fccB-9LFSqDEc5cle_N3NOKuIFEJtiCa36WhaxQkur6Nc9a4ZCnaKrHi82Ia5ppj2ErjNp5EkV5KHmhk5Pv7pKl-lMa6ww_BKCiTjvYEM9Zsr7wTXaJwk-jR4rcVauHENbmdFt4nOnh-YO6I8XvzXk4gi8WI_UmZptn8vtpf-uBwoyJ2LfV-nTFiuxtkEXbMcweDI5bGIe2hv5NV5s33NMFbPQ7JxfARade5zAZ6ZdTWf9be5L6TF7hhCYcQGMB1ZXjqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۰ میلیون دلار پرید؛ نامزدهای ضداسرائیلی پیشتاز انتخابات آمریکا
🔹
با وجود هزینه‌های سنگین لابی اسرائیل در آمریکا موسوم به «ایپک»، این نامزدهای مسلمان با مواضع ضدصهیونیستی بودند که توانستند از رقبای خود در مرحلهٔ مقدماتی انتخابات کنگرهٔ آمریکا پیشی بگیرند و پیروز این رقابت شوند.
🔹
«کمیتهٔ روابط عمومی آمریکا-اسرائیل» که به‌اختصار با نام ایپک (AIPAC) از آن یاد می‌شود، میلیون‌ها دلار را برای شکست «عبدل السید»، نامزد مسلمان و ضداسرائیلی ایالت میشیگان، هزینه کرد، اما در نهایت  نتوانست مانع پیروزی این پزشک در مرحلهٔ مقدماتی انتخابات مجلس سنا شود.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454607" target="_blank">📅 16:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454606">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qtkd7U_Cg_bbTXd5i9GUaAC7V4CVmPMHBVCeVTAHCu4bn4sD1qBhUNJmU7gUUpfoefmO1JOs7Cp4aem6uIwDPBLWA3FClm09GFh7LI49VlFaZvAXV48JmOQGSqVfFgYGpkErMONzfbr56wzZowP4hK_KnjNcZ6BtYSKQLhWEnCJcstZldeUzFVO1qKESyWGku1bw7eiFBzVfiW_B1W7XAtzW79CYlQ38S3EC_L6V4ANYMr-YW8CL9hJ6ybqVX9k7UdcLO4YZcl8aeRud6qJhg8jacRj8TUtCqVS9z5ZnSDRXBv8s8YNirkByybZOuJFNVVjwlfqS7GEUmnp0HZf9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق پرمصرف‌ها گران شد
🔹
درحالی‌که برخی مشترکان از افزایش محسوس هزینۀ برق در صورت حساب‌های تیرماه خبر می دهند، وزارت نیرو می‌گوید قیمت برق گران نشده و افزایش رقم قبوض ناشی از مصرف بالاتر از الگو است.
🔹
تعرفۀ برق فقط یک بار در سال و در اوایل اردیبهشت تغییر می‌کند و در روزهای اخیر هیچ تغییر قیمتی تازه‌ای در قبوض اعمال نشده است.
🔹
مقایسه صورت حساب‌های برق برخی مشترکان در تیر و خرداد امسال نشان می‌دهد هزینه مصرف برق سه تا چهار برابر گران‌شده یعنی اگر قبض برق مشترکی در خرداد ۱۰۰ هزار تومان بوده، در تیرماه به ۳۰۰ هزار تومان رسیده است.
🔹
معاون برق و انرژی وزارت نیرو می‌گوید اگر مصرف مشترک از الگوی تعیین شده بیشتر باشد، هزینۀ برق مشترک به صورت پلکانی و با ارقام بالاتر محاسبه می شود؛ اما مشترکانی که در محدوده الگوی مصرف قرار دارند، برق را با تعرفه یارانه‌ای دریافت می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454606" target="_blank">📅 16:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a494b0e4.mp4?token=cfICsEhtx_AcXSXKjzFz-OLEwslmeCqOJxSskQFtijDQaHbFLTTLIB25d74AV7_VQy2UXYTlsscUgk_7Ia95_2uz-Xi2W3Yfgqlp0G5CvMfT9JLMM3HgOqZZyuQ3jV89TeW6SQu7hb67oY2tAQTLTip2dRwF3XFnbkID6cFu4b7SPGW9LWR-GirmJHfhwsnfnA_i93HqYOpHEAzsIIFdk0c-aBT_dg3LQfj8TS1oqGr4fQMu9zp6pZ6E22qXH8Ham5W2gYGaf7V12LTQyttBgFb_bO8eOjETNpn4Oi-fPsAnnblhBqDPLS7PbgKZg__Xg-xhHSCrxR07IUSOvJIymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a494b0e4.mp4?token=cfICsEhtx_AcXSXKjzFz-OLEwslmeCqOJxSskQFtijDQaHbFLTTLIB25d74AV7_VQy2UXYTlsscUgk_7Ia95_2uz-Xi2W3Yfgqlp0G5CvMfT9JLMM3HgOqZZyuQ3jV89TeW6SQu7hb67oY2tAQTLTip2dRwF3XFnbkID6cFu4b7SPGW9LWR-GirmJHfhwsnfnA_i93HqYOpHEAzsIIFdk0c-aBT_dg3LQfj8TS1oqGr4fQMu9zp6pZ6E22qXH8Ham5W2gYGaf7V12LTQyttBgFb_bO8eOjETNpn4Oi-fPsAnnblhBqDPLS7PbgKZg__Xg-xhHSCrxR07IUSOvJIymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش حماس به زیاده‌خواهی نمایندۀ ترامپ در شورای صلح
🔸
ملادنوف رئیس شورای به اصطلاح صلح آمریکایی در دیدار با نتانیاهو مدعی شده بود که تا وقتی حماس به‌صورت کامل خلع سلاح نشود، نظامیان اشغالگر از نوار غزه خارج نمی‌شوند.
🔹
حماس نیز در واکنش به گزافه‌گویی وی اعلام…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454605" target="_blank">📅 16:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">باد شدید و گردوخاک در راه تهران
🔹
هواشناسی استان تهران: از عصر پنجشنبه وزش باد نسبتاً شدید به‌ویژه در ارتفاعات و مناطق جنوبی و غربی استان، همراه با خیزش گردوخاک پیش‌بینی می‌شود.
🔹
همچنین دمای هوای تهران در روزهای پنجشنبه و جمعه بین ۳ تا ۴ درجه کاهش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454604" target="_blank">📅 16:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454603">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2089c2005.mp4?token=O5E5GEIKHXqicguEIzYreP9XFqxuNPRKeLWLDgklmq7NGKLhbu7ekDnTmU3B1qVJrwh0aKYLsPS909Cz_q92Fxxbd0Qci_Gl43x7c4kztNEd8N7WqRb_JbmVR_Lzq1vMwUxMjuyjLJZmQy8BQP3ODlJij7taCs80l34Ju22Yhv46ZnAosEnEB6I72mV7ijISsYdfM7-W1BBnl-xiQ88fxLntpQjf2wSR--mj-Ghr09svcNvs5lcNT_iFtUrWdAvlquFISfYE-My2RkWXQrkn1QP6svOsqF8ZbLJ9tj0-9wR2UoNGp4n-sVM15JHg9FDXkY3iQsOXmH_KN8A82UIncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2089c2005.mp4?token=O5E5GEIKHXqicguEIzYreP9XFqxuNPRKeLWLDgklmq7NGKLhbu7ekDnTmU3B1qVJrwh0aKYLsPS909Cz_q92Fxxbd0Qci_Gl43x7c4kztNEd8N7WqRb_JbmVR_Lzq1vMwUxMjuyjLJZmQy8BQP3ODlJij7taCs80l34Ju22Yhv46ZnAosEnEB6I72mV7ijISsYdfM7-W1BBnl-xiQ88fxLntpQjf2wSR--mj-Ghr09svcNvs5lcNT_iFtUrWdAvlquFISfYE-My2RkWXQrkn1QP6svOsqF8ZbLJ9tj0-9wR2UoNGp4n-sVM15JHg9FDXkY3iQsOXmH_KN8A82UIncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعدالله زارعی: خون‌خواهی، فلسفۀ اصلی اربعین است و ایستادگی و خون‌خواهی در برابر جنایت، بخشی از این تفکر است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454603" target="_blank">📅 15:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454602">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24adfd0c64.mp4?token=fum4PpW9dGC2yC6Ubqk0EfiO00R2ATfm1o_xqXMpkUyRgmrZlB07-htEac8hSBwTUiW2jmGDuU4f7aGUTmbMahsumT28motnxcOXPBh2PM8tqLy9pBFPZxw1N5oLBeaOgbO4jMpiaWvrukv_v6uqBEjQzzDkGmzaUY0R7RqwWwxuVpnDerq_4NSdvpn2VdZVHvjTUkzLyKdhiu8-KaXfwY55ZQdgKDvGT3q9BrvjBeRlC8_5DY7DW0yeGhdj-c7hEMF-aPOMEZN9C66BunApFA50Ruqh9Bxh04AxsdFS4DiG9Bn4meJpHccMTfp2vog4rUlNCBgG2s7dl3b-O_n5CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24adfd0c64.mp4?token=fum4PpW9dGC2yC6Ubqk0EfiO00R2ATfm1o_xqXMpkUyRgmrZlB07-htEac8hSBwTUiW2jmGDuU4f7aGUTmbMahsumT28motnxcOXPBh2PM8tqLy9pBFPZxw1N5oLBeaOgbO4jMpiaWvrukv_v6uqBEjQzzDkGmzaUY0R7RqwWwxuVpnDerq_4NSdvpn2VdZVHvjTUkzLyKdhiu8-KaXfwY55ZQdgKDvGT3q9BrvjBeRlC8_5DY7DW0yeGhdj-c7hEMF-aPOMEZN9C66BunApFA50Ruqh9Bxh04AxsdFS4DiG9Bn4meJpHccMTfp2vog4rUlNCBgG2s7dl3b-O_n5CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهمان ویژۀ پیاده‌روی امسال اربعین
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454602" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454601">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777a24997c.mp4?token=gHtAVr9IsaTCHIl-UMfXJAhI17jiZtPICt4tkFMqvF1_b21oGuLb3Ubj68ARcGQu_098sfN4gQnajT2m0EpevXva6QRAn4FJjFlivJiKXG32I9LIfXt52_CKTjUvHDN0I7MnGRvGamZ2-7WmigyBf2OjcWvCvtK8WzTjxjcMkLoKaGMHNI8hGY57J7U_LP4CLTc2-fjE9BfsEX8TOV3T9vX_GYRPgqu1IjgyrIpAILJpLEe0QHb72QZZXLroIisSDKFT0tMEf5tTqUHR2B4VTLZ0DxgV1aQcjKKqCrRBzb-HIR-msiXFs-V-A9OWm6ArCyus4-Fz3LRp9GlKzoLqag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777a24997c.mp4?token=gHtAVr9IsaTCHIl-UMfXJAhI17jiZtPICt4tkFMqvF1_b21oGuLb3Ubj68ARcGQu_098sfN4gQnajT2m0EpevXva6QRAn4FJjFlivJiKXG32I9LIfXt52_CKTjUvHDN0I7MnGRvGamZ2-7WmigyBf2OjcWvCvtK8WzTjxjcMkLoKaGMHNI8hGY57J7U_LP4CLTc2-fjE9BfsEX8TOV3T9vX_GYRPgqu1IjgyrIpAILJpLEe0QHb72QZZXLroIisSDKFT0tMEf5tTqUHR2B4VTLZ0DxgV1aQcjKKqCrRBzb-HIR-msiXFs-V-A9OWm6ArCyus4-Fz3LRp9GlKzoLqag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صاعقه جان فوتبالیست تایلندی را گرفت
🔹
پلیس تایلند: سوفوان آوای دیروز پس از اصابت صاعقه به زمین ورزشگاه سانتی‌فاپ واقع در جنوب تایلند براثر شدت جراحات جان باخت.
🔹
۱۲ بازیکن دیگر نیز دچار مصدومیت و به بیمارستان منتقل شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454601" target="_blank">📅 15:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454600">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
رژیم صهیونیستی در ادامهٔ تجاوزات خود منطقه مشاع المنصوری در جنوب لبنان را هدف حملات توپخانه‌ای قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/454600" target="_blank">📅 15:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454599">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viHcOBLQHUJlIvGxv04tF2o_w3oXPMEV6o6JR4GWDGQQlCrPS2Jk6b1HDa7s3MGjK-U8kHdc8gx1PC-aF39MGwVsd8HIEm3A9A1d_L3NZOeAhs7RMBYO3XDFcmhcLLb_txHNmVhjv9r3_M6gIqGnveBeqbzJw9aQkUqO6T9BJ5pliHeSYPp63uFtbhaoDg8J0HSDLdt8UAVYQsrzP9Oi82__Q6UHakR1U4VfBJejJtRFGJKsi1DvQEZPDxrUSDBqSygSMMny1g5lcRG95tmVyJaR4fjX_nEjIcK5RQjyXV8fyxeiOwO1ECSX6FYilIvwEWjJdczCFY_SjdOw5oQ-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای یک کشتی در نزدیکی یمن
🔹
سازمان تجارت دریایی انگلیس: یک کشتی در آب‌های نزدیک یمن مورد حمله یک شناور بدون سرنشین قرار گرفت.
🔹
خدمۀ کشتی نجات یافتند اما گزارش شده که کشتی غرق شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454599" target="_blank">📅 15:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454598">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125d40ac9b.mp4?token=hKHddIAOxkY3XW1hJdPlYMDP28Onm8QM1Z4NIRHCZD-_KVfZGxI7uHhsMvDnvRjMbRhFQBwIueVNXQrVhIJYBSUmGFeK954OXT1KIY_IDz4KfcvV5OlJ_P0hMmY2bUrT2aqBXuiGUJm46Nyx8Jfd-4CryWi1wHzbQvf57QuTFQOm2QqI2g1xSgCTQ0qXhtxhcJk4g1v9cJxs3YeKHUaE3hHOAubN6dYhgTlJURIzuaAXspbTPD0B_XdGpCPdmAPHKJjtrakKOXX4ViLWpdbCLzW0HBMdYNNFWSL30DR4x6psmjQF7-fgdL2oZ_L03jbXR-MNMEx4-5-apLwmNORmqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125d40ac9b.mp4?token=hKHddIAOxkY3XW1hJdPlYMDP28Onm8QM1Z4NIRHCZD-_KVfZGxI7uHhsMvDnvRjMbRhFQBwIueVNXQrVhIJYBSUmGFeK954OXT1KIY_IDz4KfcvV5OlJ_P0hMmY2bUrT2aqBXuiGUJm46Nyx8Jfd-4CryWi1wHzbQvf57QuTFQOm2QqI2g1xSgCTQ0qXhtxhcJk4g1v9cJxs3YeKHUaE3hHOAubN6dYhgTlJURIzuaAXspbTPD0B_XdGpCPdmAPHKJjtrakKOXX4ViLWpdbCLzW0HBMdYNNFWSL30DR4x6psmjQF7-fgdL2oZ_L03jbXR-MNMEx4-5-apLwmNORmqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلالی که ۲۰ بازیکن در تیم‌های فوتبال ایران دارد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/454598" target="_blank">📅 15:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454597">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTcNdGUtCty_mkvRdy5e1ZaZlRQJU6fMcFEOKIF0qhVIfd02X5Q5XNcq9mlfeZ3oW9gOzg2AtF17u9jGoKoDi_ndcwacPMzmAtZCyD17FUqr0QcMWCCFmSTtlyFtcilOTJnzNKYe3Jtwww4WPAHhsM6YuXbbI3WDL6-DEEd58fAePeVfxJzSqeH7S3-bfkarNi6xNJhLgVf4N2sSI7HijUxJvDZlSMEfmJGAAlnWOnkfwoPVacTZEaVVZovdzymj0_cbw6RTOJkouGACto9-A3ZZLb4sQhmDFJNyccxeh3wITMp2UAaC8uxQc3mGj2eVirsaNfvsVf8Jz0a9NaX2GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کچاد» با رشد ۲۶ درصدی درآمد، جایگاه خود را تثبیت کرد
🔹
شرکت معدنی و صنعتی چادرملو (کچاد) در گزارش فعالیت ماهانه منتهی به ۳۱ تیر ۱۴۰۵، تصویری از تداوم ثبات عملیاتی و رشد درآمدی خود ارائه کرده است، گزارشی که نشان می‌دهد این شرکت در چهار ماه نخست سال مالی، ضمن حفظ سطح تولید در بخش‌های مختلف زنجیره فولاد، توانسته از بهبود نرخ فروش محصولات نیز بهره‌مند شود.
@Farsna
_
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454597" target="_blank">📅 15:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454596">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8GR2QS73xOfIkKczu3oQu9jKgrCmW7iE4fu8npbkPvxo2FHINwVLbtbGoV6RgxcMNMLZv9TUB_EH29FChDlX8iubUJWpyoe34SVcUF2jmrqh3mmqFdmW4cKo9Q3gCn8TAv7lFNG5t_6JzL1YkacssFB56BHbfxHW4KeTI7Av549XH8rlVoSYUIjcjqJ_7p4ixooyef-yylGGEn-TQ3f1Q2tbGlsM6j90a8vnIZLddm4tqgEQFb1B4LeLfCFlr4egt7ey--gGbHFZ9WZuyAZDFY6AuT8qGUBQyIyNmUpdC39_AX6PwwwP9InFU9BwDb2_PgNCHV2xZ9-mUAVqcHmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
جهش بیش از ۳۳ برابری سود خالص بانک رفاه کارگران در بهار ۱۴۰۵
🔹️
بانک رفاه کارگران بر پایه جدیدترین اطلاعات و صورت‌های مالی منتشرشده در سامانه کدال، در بهار سال جاری با ثبت رشد خیره‌کننده ۳۳۷۱ درصدی سود خالص، عملکردی درخشان از خود به نمایش گذاشت.
🔹️
بر اساس صورت‌های مالی مذکور، سود خالص این بانک در سه ماهه نخست سال جاری به رقمی بالغ بر ۲۲ هزار میلیارد ریال رسیده است که در مقایسه با دوره مشابه سال گذشته (حدود ۶۵۱ میلیارد ریال)، جهشی ۳۳ برابری را نشان می‌دهد.
🔹️
براساس گزارش کدال، درآمدهای تسهیلات اعطایی بانک نیز در این دوره با رشد ۵۳ درصدی به بیش از ۱۷۵ هزار میلیارد ریال رسیده است که نشان‌دهنده ارتقای توان تخصیص منابع و حمایت از بخش‌های تولیدی و اقتصادی کشور است.
🔹️
این جهش عملیاتی در حوزه اعطای تسهیلات، بیش از هر چیز بیانگر تمرکز راهبردی بانک رفاه کارگران بر ایفای نقش اثربخش در اقتصاد کلان کشور است. هدایت منابع مالی به سمت پروژه‌های پیشران و واحدهای تولیدی، علاوه بر تزریق نقدینگی به رگ‌های صنعت، گامی عملی در جهت تثبیت و ایجاد فرصت‌های شغلی جدید محسوب می‌شود.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/454596" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454595">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/454595" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454594">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
زخمی‌شدن نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های صهیونیستی از زخمی‌شدن چند نظامی صهیونیست در مجدل زون در جنوب لبنان پس‌از انفجار یک مین خبر دادند و اعلام کردند که نظامیان صهیونیست با بالگرد به بیمارستان‌ها انتقال یافتند. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454594" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454593">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlvNaDqIHPVU4VMuTarQIao5P9ZmF2Fmp7HoNvsRnvaB9-Ytzu2VA5gBrtO0y-LwnSuYTjKSlgcSHLTHjTlBzxzxKkUNPRGNLXAZdu4EJPZn0sKBiyY4zKzUHmTnDlbfWDD3JKoKwl8XAlikkXzn3ET_X610-XLEBC6pOybpTS6RsOl1ZwvY2WFby9DKoVmXfkmeA97aCBdSUHrzBfFGBePfubG90Oan_pJizHxjXJ6hp-qrRa7UgslUrfAXD93jEguBhit-NUIhq_p1QccD5LyjRvKqxL7uMmiXr1L9W0YOeXKm1RqgL4gska_R392vhlLSDuUMlA46ZXrpnyfu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامۀ امتحانات نهایی برگزارنشده پایۀ دوازدهم ۴ استان جنوبی
🔹
امتحانات نهایی برگزارنشده پایۀ دوازدهم استان‌های خوزستان، بوشهر، هرمزگان و سیستان‌وبلوچستان در روزهای ۱۵، ۱۷ و ۲۰ مردادماه برگزار می‌شود.
🔸
امتحانات نهایی پایه دوازدهم این استان‌ها که قرار بود از…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454593" target="_blank">📅 15:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454592">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c214d9363c.mp4?token=A4s6NOB-JDFLqmgMWwj78yKP0FkqanatFta3V3-MvpOEAt8GGxgcBP-H9maNT9F-sKuabZ98nmEG5W2u2H6TPhc_MsccjNSYhpC43Fsp8D0KokEyPkSkjQYpH6diGY0hI8Ycq2PmRpKFrOkWV_LDM5-oi7QXB_hG1OmeKtBfGmR-e_ZeZUomtyI4piVsV7ohlx5g5V1L8SZ71Dye8wkhbTFoUBVPKANpskYF49NFDlX2GB6vKn3hSCqywvl8-umqyu_vgcWeqiV1sM9f8F4WB1uSDKbwQydl9-gyF_wiF0f45bRJhMyMzIYVNWlfoeso0dcP2McAOo6m9lluIvDuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c214d9363c.mp4?token=A4s6NOB-JDFLqmgMWwj78yKP0FkqanatFta3V3-MvpOEAt8GGxgcBP-H9maNT9F-sKuabZ98nmEG5W2u2H6TPhc_MsccjNSYhpC43Fsp8D0KokEyPkSkjQYpH6diGY0hI8Ycq2PmRpKFrOkWV_LDM5-oi7QXB_hG1OmeKtBfGmR-e_ZeZUomtyI4piVsV7ohlx5g5V1L8SZ71Dye8wkhbTFoUBVPKANpskYF49NFDlX2GB6vKn3hSCqywvl8-umqyu_vgcWeqiV1sM9f8F4WB1uSDKbwQydl9-gyF_wiF0f45bRJhMyMzIYVNWlfoeso0dcP2McAOo6m9lluIvDuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگۀ هرمز بنزین‌دزدی در انگلیس را باب کرد
🔹
بحران انرژی در اروپا ابعاد تازه‌ای پیدا کرده. داده‌های تازه منتشرشده در اسکای‌نیوز عربی نشان می‌دهد از روز آغاز تجاوز نظامی آمریکا و اسرائیل علیه ایران روزانه به‌طور میانگین نزدیک به ۲۰۰ هزار پوند بنزین و گازوئیل…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454592" target="_blank">📅 14:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454591">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56430c1b36.mp4?token=ICMRaD9wnNCVtAVssHVbTHEz10ITi47FwIyGXWpVmgHIBLG_5dZK7iAZ2BuVGSBYb715y1do0BcRCaaFD0TE3Q8RrHk49Of8GebwYokTjHINBpEt17ZjzQjSob6E_ikewZnbO38lhCloZi0Ti0nOf4azgUpaFt8r1C-W8SSb8sUtS5S1kiN7_k9jyPynoHF5YZUniYBS3uX3gAjXald56a4QQvxjxCJQhlWU7IWg2mxiqvb2hsPty56ofbc-g5RNR5AZnGXqbLb8RSxtCx1ASZwQoV3ygZVUSkYl4Th-95BBqMbEOVfFM9lwCG6QvamF44tcxJxQ97YrUWCBsN7m1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56430c1b36.mp4?token=ICMRaD9wnNCVtAVssHVbTHEz10ITi47FwIyGXWpVmgHIBLG_5dZK7iAZ2BuVGSBYb715y1do0BcRCaaFD0TE3Q8RrHk49Of8GebwYokTjHINBpEt17ZjzQjSob6E_ikewZnbO38lhCloZi0Ti0nOf4azgUpaFt8r1C-W8SSb8sUtS5S1kiN7_k9jyPynoHF5YZUniYBS3uX3gAjXald56a4QQvxjxCJQhlWU7IWg2mxiqvb2hsPty56ofbc-g5RNR5AZnGXqbLb8RSxtCx1ASZwQoV3ygZVUSkYl4Th-95BBqMbEOVfFM9lwCG6QvamF44tcxJxQ97YrUWCBsN7m1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد اربعین: از ۳ میلیون و ۳۵۰ هزار زائر، ۲ میلیون و ۸۰۰ هزار نفر به کشور بازگشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454591" target="_blank">📅 14:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454590">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5168ee4e.mp4?token=qlb1kRJBlWFUqqh66QufiWu5aoN8iJtHbX46KyFuoRuQk6KaAWxnTnzwFz2fudjzrmo31D1Syyw1GJVhMLxmhpePvQhi2_H3r0lRIWPQH6qMCzALv0St2YzNS_2LHjzY2ZFmLhUrz13icKRcrOHZJLFeEpz13UtDxrYea2-A5fsyjbZhohOYV1aKkQoOp2KslH_ehKRiCZg-24dyJd7isMJrmkWS7KWjFNoF01x76aOy5jgeFodlBp86m5F82di58zCc3CYmpGG_7-SWln2kK1vd1DFcfr2v7O5NKk6n-APXUMc1Kp2B7jbap1FthiyVa4Wz-Z3GIza3WpLRaM5Adg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5168ee4e.mp4?token=qlb1kRJBlWFUqqh66QufiWu5aoN8iJtHbX46KyFuoRuQk6KaAWxnTnzwFz2fudjzrmo31D1Syyw1GJVhMLxmhpePvQhi2_H3r0lRIWPQH6qMCzALv0St2YzNS_2LHjzY2ZFmLhUrz13icKRcrOHZJLFeEpz13UtDxrYea2-A5fsyjbZhohOYV1aKkQoOp2KslH_ehKRiCZg-24dyJd7isMJrmkWS7KWjFNoF01x76aOy5jgeFodlBp86m5F82di58zCc3CYmpGG_7-SWln2kK1vd1DFcfr2v7O5NKk6n-APXUMc1Kp2B7jbap1FthiyVa4Wz-Z3GIza3WpLRaM5Adg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویری از پیکر شهید ۲ سالۀ جنایت آمریکا در قشم
🔹
سینا جعفری به‌همراه پدر و مادرش بامداد امروز در حملۀ آمریکای جنایتکار به قشم آسمانی شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454590" target="_blank">📅 14:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454589">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj-PgG1sKLnOtokKiEGPVaqeOqQgnockz0hGQN3laA8dL728kfMoflXrDsA_4rk48vUfHtu6FLMh-9aalCoi36w4xleGCJvohAGQe_-hnqmH-wWdGSk-G2JRCyfddZTXKa1CJIWh4DXdimQFdKWsDpE2mxAybzeqhTQ5qAEgsbf6Qi_J88xosFvrQceyrGL_ggqwj9cBuwCxQis7GujKRvGNzIZvUrqiQnay2ykLgDwBiD-iCC-JcUqvpRDwxFlKhRwwmyIGeNzkJAyLb1CSY2TCKQOG7fvCbWk25F9y5I4fvmMRjBlSTjH0WxDc29BOZ7mvDdj61UQZi3FxcNuRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنترل هرمز و گسترش جنگ؛ اهرم‌هایی که ترامپ را به بن‌بست کشاند
🔹
«کنترل بر تنگه هرمز»، «گسترش جنگ به منطقه» و «تهدید علیه زیرساخت‌های انرژی منطقه» تنها چند نمونه از اهرم‌های فشاری است که ایران در اختیار دارد؛ اهرم‌هایی که به اذعان کارشناسان غربی، هزینه‌های جنگ را برای دونالد ترامپ به شدت بالا برده و او را در «یک بن‌بست» به دام انداخته است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454589" target="_blank">📅 14:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454588">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
زخمی‌شدن نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های صهیونیستی از زخمی‌شدن چند نظامی صهیونیست در مجدل زون در جنوب لبنان پس‌از انفجار یک مین خبر دادند و اعلام کردند که نظامیان صهیونیست با بالگرد به بیمارستان‌ها انتقال یافتند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454588" target="_blank">📅 13:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454587">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پزشکیان: از هر تصمیم رهبران فلسطینی در روند مذاکرات حمایت می‌کنیم
🔹
رئیس‌جمهور در گفت‌وگوی تلفنی با رئیس دفتر سیاسی جنبش حماس: ایران از هر تدبیر، ابتکار و تصمیمی که رهبران فلسطینی در روند مذاکرات اتخاذ کنند، حمایت خواهد کرد.
🔹
به‌رغم تجاوزات اخیر رژیم صهیونیستی و آمریکا علیه خاک ایران و شرایط منطقه، مسئلۀ فلسطین همچنان جایگاه محوری خود را در سیاست خارجی ایران حفظ کرده و از نگاه مسئولان، سیاستگذاران و رهبر ایران دور نمانده و همچنان مسئلۀ نخست جهان اسلام به‌شمار می‌رود.
🔹
خلیل الحیه: ایران توانسته معادلات جدیدی در منطقه ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454587" target="_blank">📅 13:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454586">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d70982dd.mp4?token=N40fnmFOIQCnx9xXVTsEiTXrWqu1G3rPMZA6cp34jWKh1B0vG4HgttLbJS6Bds-Id6k4LsMQcqP2SQ_LkrojLOVoypOiYgW3HE4uegXQ-9UlxMT0WwF45_kRdR3ru2mRBPzPdSWYqYncEKQYqN3wyK3qQh_H6vClYirU4RBBy7IvWbp0W2RQrS97_WdAJEHYI1XgT_P0gb97fRUTd81ycBdAtFOqkpENlAKvEXxlOfiC5GZk_G_k0akdN522Mcw4fUhG2V1i08b5hYFppDftCQGoeF09T4OrFnV5N_Bts3YxppTbvOOPnh--pJDXCOVWPMjaXrmnm6Q5hUf56YuE-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d70982dd.mp4?token=N40fnmFOIQCnx9xXVTsEiTXrWqu1G3rPMZA6cp34jWKh1B0vG4HgttLbJS6Bds-Id6k4LsMQcqP2SQ_LkrojLOVoypOiYgW3HE4uegXQ-9UlxMT0WwF45_kRdR3ru2mRBPzPdSWYqYncEKQYqN3wyK3qQh_H6vClYirU4RBBy7IvWbp0W2RQrS97_WdAJEHYI1XgT_P0gb97fRUTd81ycBdAtFOqkpENlAKvEXxlOfiC5GZk_G_k0akdN522Mcw4fUhG2V1i08b5hYFppDftCQGoeF09T4OrFnV5N_Bts3YxppTbvOOPnh--pJDXCOVWPMjaXrmnm6Q5hUf56YuE-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خادمان اربعین غمگین از اتمام فصل عاشقی
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454586" target="_blank">📅 13:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454585">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa44218d82.mp4?token=HR5Ix6fEozuW2eeZ8e_9d1z4A7laIdHZEonRNnwyol3ZBULZ9YA53x3dUrE-5yF_KG5xO9eEg9gdClOUlw1b4N_q1jBGZoQytBa2hTAVkFojfSnN8CvbrmRXmqI0o0ysAzp-5HOfiitbZjjagNuQtCu_uOoAgYcrK-nTWiSSlV8HlbcWgqSKxZKigkBiVqGSqlcCas_DmyMJp5hZx3-1mJT7_MkmYnPPlEZ-NEb4RqiF1jrqTbEb2uiCRfZ6G8EjYFWDA0h_3gPljlBUOkVHzHdZ53w4nRGOHmSfQG6y7GzIIG0JHGnEjtAUsEzRxaJGzRH87Nc9NJWLPDDYkHQ24UDcJn0-9yUMz-AZ-jjPCNrnf2QjkzQCHvlMZ4zdXNLnSKXavWbBgetm5fWWYTCZeLzch2uDkragfhS30gyLaf_sE_Tv-s9Az3epaR6XSYewW_el3VeHwzGQ88p0SD0rW36OB_jys2VIMLTsGCM24c_0-_EfwN61hAqV2tzWC2_Ym3hTm3wBttekn-ih2yquoQQH_VtGv4QG_TbfE5nlVTiQUIHYd_a50bswz4yuFBLdBeAYNqdosmuD54SiglMw7EUB8f_yNs0YryROGTRIBYZUpQlLuN4gxOStyYAvhBYfL0rmBzAT0HyJd1k3z0WK87qmiPIb79hRqUSgudi7VVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa44218d82.mp4?token=HR5Ix6fEozuW2eeZ8e_9d1z4A7laIdHZEonRNnwyol3ZBULZ9YA53x3dUrE-5yF_KG5xO9eEg9gdClOUlw1b4N_q1jBGZoQytBa2hTAVkFojfSnN8CvbrmRXmqI0o0ysAzp-5HOfiitbZjjagNuQtCu_uOoAgYcrK-nTWiSSlV8HlbcWgqSKxZKigkBiVqGSqlcCas_DmyMJp5hZx3-1mJT7_MkmYnPPlEZ-NEb4RqiF1jrqTbEb2uiCRfZ6G8EjYFWDA0h_3gPljlBUOkVHzHdZ53w4nRGOHmSfQG6y7GzIIG0JHGnEjtAUsEzRxaJGzRH87Nc9NJWLPDDYkHQ24UDcJn0-9yUMz-AZ-jjPCNrnf2QjkzQCHvlMZ4zdXNLnSKXavWbBgetm5fWWYTCZeLzch2uDkragfhS30gyLaf_sE_Tv-s9Az3epaR6XSYewW_el3VeHwzGQ88p0SD0rW36OB_jys2VIMLTsGCM24c_0-_EfwN61hAqV2tzWC2_Ym3hTm3wBttekn-ih2yquoQQH_VtGv4QG_TbfE5nlVTiQUIHYd_a50bswz4yuFBLdBeAYNqdosmuD54SiglMw7EUB8f_yNs0YryROGTRIBYZUpQlLuN4gxOStyYAvhBYfL0rmBzAT0HyJd1k3z0WK87qmiPIb79hRqUSgudi7VVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری عامل تولید کلیپ جعلی اعتراض نوجوانان کشتی‌گیر به اعدام
🔹
این فرد با سوء استفاده از ویدیوی گرفته شده از تمرینات کشتی نوجوانان، بدون اینکه هیچ‌کدام از آنها اطلاعی داشته باشند، به‌عنوان اعتراض به اعدام تروریست‌های آشوب‌های اصفهان منتشر کرده بود.
🔸
پیش‌تر قوه قضائیه برای برخورد با هرگونه انتشار محتوا در خصوص سیاه‌نمایی و هم‌سویی با رسانه‌های دشمن در خصوص اعدام جنایتکاران اغتشاشات هشدار داده داده بود
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454585" target="_blank">📅 12:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454584">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guiTlD9gHWGCgBYmmTqhz1mKksRnCPlzfIzYjl8Mf54oK-9C_vzlIcGloVe2Rnt8-JZG7-kUma2AUll_ez2LqmCghI8CIwUB28QW3pvV-CuTiAZTKsoYcudf9Q5ovDeaE6_NXTcwAts21s4N-4yHGfluzNiX5llXZ9iXS6SfM527IGq345xZpNwfKfTnKDe8baAYZQeltnwZb81z6tkfOJcJL9maKlaRU-y6NqNIj__EqUhZ0rUd08JBjgyham2VtLpNMU28WpSDvXASGcNn40CIHoWx_Gu13pxbIYpuybfChVAyuE7_vguRZU3gZAOh6VWAOBP9yg-FiGIyuhIiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با عبور از ۵ میلیون و ۴۰۰ هزار واحد به قلهٔ تاریخی جدیدی رسید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۰ هزار واحدی به ۵ میلیون و ۴۰۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454584" target="_blank">📅 12:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454583">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شارژ مرحلهٔ جدید کالابرگ از پنجشنبه آغاز می‌شود
🔹
مرحلهٔ جدید طرح کالابرگ الکترونیکی از پنجشنبه با شارژ اعتبار مشمولانی که رقم آخر کد ملی آن‌ها ۰، ۱ یا ۲ است، آغاز می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454583" target="_blank">📅 12:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454582">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjwdP6YESZGCQbAIb4zIGEbkemlRtON605SnrGJB1uWTiXkBpxR30n7BJzsdjQfV_LOQRrsjV1LWlpx7ZoX0qcDwN0EYBn6dm3LQAJPhKrVTKpbGIJRKhK58uwwqicBfdraJ4zBZxkY_Mi0Q7wDAdVc7fV2iVckIv7dCh2HZo2hVFXcThH8X356-vM_4R9u_BBIGSSfrfMtxCpZzjWW1xSVJV3z6CYDryF1c1Wpn7MP3vKjiY25tBkPGpum6ryheBlxbZaIvybaGkQdaQ-Q12Q6efmYss9vk7cYpbJlP95Y6iPdG1JeC2Gj5yIS_on_JWhamAaSTMoWaJFt_GCClWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان همکاری استقلال و رضاییان
🔹
❌
باشگاه استقلال در بیانیه‌ای نوشت:
🗣
با توجه به مفاد قرارداد یک‌ساله رامین رضاییان و عدم پذیرش شرایط پیشنهادی باشگاه از سوی این بازیکن برای ادامه همکاری، همچنین با پایان یافتن مهلت تفاهم‌نامه فی‌مابین، باشگاه استقلال تصمیم به قطع همکاری با وی گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454582" target="_blank">📅 12:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454581">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837e4354bf.mp4?token=gjXKQ9IGwRwKRdQf3WmIA6gTCYE-J1y9GWOmi40-voBJh7Uvhxi86Tag3yKWpxeMm4z00hrvq53L3EptQNZK4BFSbrsWaUI_pHksc0GChNdlYi8zT7KU-phQdjxffJPjSZqKPwhdnmCGb64j36iMnThehV4lT_jq753XxEz5QRqmy8IrUVUOCIMN6SFAVMlyjH81WYxp8zIO7e9aYoj-4FcdxFwYXcBzjZtLX458Np-g0dZsJn9ehKgKI0aU7Q7AAKqTU82lc540oAfH4gnfx0wXZCzJC5ZZ51KjAMRuMixkC3u25gpeNc1ZUXIAVL3IYqgfY2gc06FK14tZkK1Wvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837e4354bf.mp4?token=gjXKQ9IGwRwKRdQf3WmIA6gTCYE-J1y9GWOmi40-voBJh7Uvhxi86Tag3yKWpxeMm4z00hrvq53L3EptQNZK4BFSbrsWaUI_pHksc0GChNdlYi8zT7KU-phQdjxffJPjSZqKPwhdnmCGb64j36iMnThehV4lT_jq753XxEz5QRqmy8IrUVUOCIMN6SFAVMlyjH81WYxp8zIO7e9aYoj-4FcdxFwYXcBzjZtLX458Np-g0dZsJn9ehKgKI0aU7Q7AAKqTU82lc540oAfH4gnfx0wXZCzJC5ZZ51KjAMRuMixkC3u25gpeNc1ZUXIAVL3IYqgfY2gc06FK14tZkK1Wvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار روس حاضر در مراسم اربعین: چیزی بیشتر به‌چشم می‌خورد زنده‌شدن فرهنگ خون‌خواهی شیعه و پرچم‌های قرمز انتقام است که مردم می‌گویند برای فرزند حسین(ع) و مرجع عالی‌قدرشان به‌دست گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454581" target="_blank">📅 12:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454580">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تمدید فرصت ثبت درخواست معافیت سربازی برای مشمولان دارای ۳ فرزند و بیشتر
🔹
سازمان وظیفهٔ عمومی اعلام کرد مهلت استفاده از معافیت خدمت سربازی برای مشمولان دارای ۳ و ۴ فرزند تا پایان سال ۱۴۰۷ تمدید شده است.
شرط سنی استفاده از این معافیت چیست؟
🔸
مشمولان دارای ۳ فرزند: حداقل ۴۰ سال سن.
🔹
مشمولان دارای ۴ فرزند و بیشتر: بدون محدودیت سنی.
🔹
مشمولان واجد شرایط می‌توانند با مراجعه به دفاتر پلیس +۱۰ در سراسر کشور، درخواست خود را ثبت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454580" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454579">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqpUs_eEmFg8DNgU_hb8vMGoHx0-FPFNZhUgMfBB2m2kcz_FtnIw806USwOpYcgYUVDnMGP1G0Mca_NYahWSaczR2sywWh2p0grPrbXsxXaJNT0D0fsn0frFEiji_N7pChmejgUk2xA2Hdt04_mZqni2y3nXGruHUVtDE4QoB2A58_jNQJlIjLMYWrl6DuaKi8Z3SH8cxzEFopqR5utHsYBV7IRsmHziix9bQgn5XscjOBakWDsERnwe1Uk-NHOoDhdCVEMn5Oz-5Wvd7jAuNzLfBWkTy-w8XtxqfzOYEn9qzmLSjZHmbCjGfYgyqtvUlhlZQW5wIX5VIQdR1Q1lkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
محمد صلاح بازیکن سابق لیورپول به ترابزون اسپور ترکیه پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454579" target="_blank">📅 11:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454578">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حساب‌ شرکت ملی نفت ایران بسته شد
🔹
کسب اطلاع فارس نشان می‌هد بانک دولتی صنعت‌ومعدن حساب‌های شرکت ملی نفت را به‌خاطر بدهی بست.
🔸
پیش از این وزارت خزانه‌داری آمریکا در قالب تحریم اقدام به محدودیت مالی برای شرکت ملی نفت کرده بود.
🔹
اقدام این بانک در شرایطی انجام می‌شود که طبق قانون بودجه بدهی‌های شرکت ملی نفت تا پایان سال ۱۴۰۵ امهال شده و این شرکت تا آخر اسفند برای بازپرداخت بدهی‌ها مهلت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454578" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454577">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqiRmHgWpzeCOnIvt0yEImYCuGgFu67Ar8XTj-GF2zPPKr1Vxcz-8OOlqxycpeQ3N2iHC-UrWJekkjpLCxTmhXBo8owuZxFyc5jY9_mkqz8600uERxzyLx02I0ZGgxOglSPjBqwcyFh4V22qo5iyz7rMw776WL4XyGw9in7Iu3Y6M41wH4WQmJUnpkXE_OxwWXMjpRlOz9X_N0Ia1EmhMZ6iWAkLkgu-TJeO-kydxIy--h6zgLy1Nne8fl3muh_rHIeq3O7hy2edN8iUhlwCZG7whYVIBGIVu7HnVw3abksaQkZ8yg1rj7zbAcTXJS-cRaGP8Ihh7S5fXWiI0m7dgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت پلیس اهل سنت بلوچ در ایرانشهر
🔹
نورالله ناروئی یکی از کارکنان بلوچ و اهل سنت پلیس که در جریان حمله و تیراندازی چند روز پیش به خودروی پلیس در ایرانشهر مجروح شده بود بر اثر شدت جراحات وارده به شهادت رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454577" target="_blank">📅 11:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454576">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c52fabc58.mp4?token=jzv6Aw_fGFKkc5QFyhHLK2fY2nJ0rNjI8rtss1CQcCOQE4G7DVjIow4wMQgpdovCQz9bJ0g_L9Uw3rUuQ_Yj03QsP7eoWqv-4I6qVRqsVNpORbdIbqSyT-cg59gcqIf8FLcc3hsHU5FTL9nhrWLIDQSegTjFc88Xhq1u4ILydBRKhKEYLovd7e6Ejqvxexlb97HOpYe6mCaqfE3cMvCxxh8IbVyA6D2arfy_0UMuPEfyNA2oFdoWqWZCGljSG3LQV79OThHcvXgwO1_GautYGzV4LYkDN6pUngBmZB4Q4nwyZcD92J3onU1dH0m8lJCe5WKEG102A8ArMMZM-vIK5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c52fabc58.mp4?token=jzv6Aw_fGFKkc5QFyhHLK2fY2nJ0rNjI8rtss1CQcCOQE4G7DVjIow4wMQgpdovCQz9bJ0g_L9Uw3rUuQ_Yj03QsP7eoWqv-4I6qVRqsVNpORbdIbqSyT-cg59gcqIf8FLcc3hsHU5FTL9nhrWLIDQSegTjFc88Xhq1u4ILydBRKhKEYLovd7e6Ejqvxexlb97HOpYe6mCaqfE3cMvCxxh8IbVyA6D2arfy_0UMuPEfyNA2oFdoWqWZCGljSG3LQV79OThHcvXgwO1_GautYGzV4LYkDN6pUngBmZB4Q4nwyZcD92J3onU1dH0m8lJCe5WKEG102A8ArMMZM-vIK5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی گسترده روسیه به کی‌یف
🔹
رسانه‌های اوکراینی بامداد چهارشنبه از وقوع چندین انفجار قدرتمند در پایتخت این کشور در پی اصابت حداقل ۳۰ موشک بالستیک روسی خبر دادند.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454576" target="_blank">📅 11:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454575">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23960fdf53.mp4?token=eTTeutDLFTTO5YapPyAul0fHneRVlsW7V3CBI12adcG-tOBfA3PP0pkzOZtmuI--O0F20CvThzGdnqWjiL9WyPDAVVjZ7xXlg1B9Nyh9E3PnWWcM_P4ohvhq0kUDB_ZOCSg-dHhO0AhhUyMX9ZVh4YjTtmyxhh0gbV06KVn5eW_dfsS3G8d1FVVbzIpHa65D7TMNLyFhptjtCOYS50ec_mYrm7zwuO-yVBSU5L7gNGXk4YyQKcOqVKC-Eeyly2T7g1F7ad8-FYeerXc1nas61vFVTk4ecYJI1m07yzr1ux6q3PnKfQT4lGQK7W_dIlBNeUPbXu8jTR3w1kVLP-gVRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23960fdf53.mp4?token=eTTeutDLFTTO5YapPyAul0fHneRVlsW7V3CBI12adcG-tOBfA3PP0pkzOZtmuI--O0F20CvThzGdnqWjiL9WyPDAVVjZ7xXlg1B9Nyh9E3PnWWcM_P4ohvhq0kUDB_ZOCSg-dHhO0AhhUyMX9ZVh4YjTtmyxhh0gbV06KVn5eW_dfsS3G8d1FVVbzIpHa65D7TMNLyFhptjtCOYS50ec_mYrm7zwuO-yVBSU5L7gNGXk4YyQKcOqVKC-Eeyly2T7g1F7ad8-FYeerXc1nas61vFVTk4ecYJI1m07yzr1ux6q3PnKfQT4lGQK7W_dIlBNeUPbXu8jTR3w1kVLP-gVRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار اروپایی: آنچه در کربلا می‌بینیم، میلیون‌ها نفرند که خواهان انتقام هستند. انتقام برای رهبر عالی‌مقامشان و کودکان میناب با کشتن ترامپ.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454575" target="_blank">📅 10:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454574">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU65Qcbf7Sdj2BzfeulP-Y_FlmazXTR1qYhd2wUyQhdEaiTqpLxKRYRMWZEshk7kY9jczkHl_Yv523ry4cJMyNTmDcYGk1-j3buT0mVxprtSNsRxa5pXDMwoDhqdKOt1nGv9BdUAIVmKJRrwO9er1hAsvKd_a985QI45sqvyrBtMrjd_i3hrbR0rbE4oxbyuM6idRSfydGNv7aIar_pRWmRwknY27Fky7oB5kJyHPhfl4gThwFzUwZ748bPtVgqtZvYnScJPfciQJzd0QPf1OEWyDAFEidpbgsgAQv7QDHUWokAnMJp7BATeG1QAuPB1dLsNoj3MyEba0r3eqAah-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: یک نفتکش سعودی را در منطقهٔ ینبع هدف قرار دادیم
🔹
یحیی سریع: در راستای اجرای ممنوعیت تردد دریایی برای دشمن سعودی، نیروهای مسلح یمن با لطف خداوند موفق به هدف‌قرار‌دادن نفتکش سعودی «وفا» شمال دریای سرخ، مقابل منطقه «ینبع» شدند.
🔹
این…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454574" target="_blank">📅 10:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در پاکدشت
🔹
روابط‌عمومی سپاه سیدالشهدا استان تهران: انهدام مهمات عمل‌نکردۀ تجاوز آمریکایی‌صهیونی در شهرستان پاکدشت تا ۱۶ امروز صورت می‌گیرد و جای نگرانی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454573" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b905e7a3f7.mp4?token=DviwatXppPsMsY30wpLCHPY6xl-7js6fY1Z8pcKAd8FK8vcmHHNc7gMYjjkVXhMNDb6_LKEGkD0k2wAWLYtYuAveu8TWJprFbm3taNsxUVkQTp810iht6QYepChkS4qd6kuNXFfhMP51t_3N83G6QdMCh0z96YbahdnkhIx091odW6ktHKbgdFevBeLT32F-GtMEDK2VdaUJYmON-RTOMI7jRXD60DT9RlVXdanmFbh28ylwYzRnmzADe16vhRFyXoLGJNozrFMrkNARYwcdO6dYESMgvy9q7__CYoPXe6-iWXsPM2UNqcD_xnD7Ay4hWQFVVx6kobLGlxclCxWmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b905e7a3f7.mp4?token=DviwatXppPsMsY30wpLCHPY6xl-7js6fY1Z8pcKAd8FK8vcmHHNc7gMYjjkVXhMNDb6_LKEGkD0k2wAWLYtYuAveu8TWJprFbm3taNsxUVkQTp810iht6QYepChkS4qd6kuNXFfhMP51t_3N83G6QdMCh0z96YbahdnkhIx091odW6ktHKbgdFevBeLT32F-GtMEDK2VdaUJYmON-RTOMI7jRXD60DT9RlVXdanmFbh28ylwYzRnmzADe16vhRFyXoLGJNozrFMrkNARYwcdO6dYESMgvy9q7__CYoPXe6-iWXsPM2UNqcD_xnD7Ay4hWQFVVx6kobLGlxclCxWmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صهیونیست: باید اقتصاد ایران را به زانو دربیاریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454572" target="_blank">📅 10:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfEN-zvHKVTrW-F9xR0Vcf4-bbJut1OGz921yGh4tzEdQtsFlAUVyv60NosUvGOhpeu_lCTYRMyMKCvYZWP7eN6noRw8IG4D43hqGRNxBfaMwfrEtNXiJCUhe1LD0Wt9V_qddYi8zGYt7c9bDftwyygT4R1oJ5hkK1pXpo7hSf-A-Yf-vZ00da8Hh8YAHcHcEUNqoDPYK4mS1FEvEsiO5KEeBjcrn7sj6HLn8Fg5iJPQqrcBoRIsd4dNqR1s4RBwPCxR4WUdHJMHORjFN4_hhSPKXf3HHbs2Q_2AvkpXd16EZ9zsRDVaP7rbJD1Fx2kb2EcPz1gHXh3lMGVpmlgYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: یک نفتکش سعودی را در منطقهٔ ینبع هدف قرار دادیم
🔹
یحیی سریع: در راستای اجرای ممنوعیت تردد دریایی برای دشمن سعودی، نیروهای مسلح یمن با لطف خداوند موفق به هدف‌قرار‌دادن نفتکش سعودی «وفا» شمال دریای سرخ، مقابل منطقه «ینبع» شدند.
🔹
این عملیات با استفاده از تعدادی موشک بالستیک انجام شد و با لطف خداوند، اصابت دقیقی صورت گرفت.
🔹
با انجام این عملیات، مجموع کشتی‌هایی که نیروهای ما از آغاز محاصرهٔ دریایی هدف قرار داده‌اند، به ۸ نفتکش سعودی رسید و مجموع کشتی‌هایی که از تردد آن‌ها جلوگیری شده به ۲۹ نفتکش سعودی می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454571" target="_blank">📅 10:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ec883c5b.mp4?token=u1RZOJcH9Ry2X0AU1mObV8LtlE5pHxQp7jefrPgUoibzQNM62RtBF7ll-OLA533qki_ue0jmwvvzc8JZo7QpjZnkYeEfEI-bc3eUw0-lsFoBR_RybtxqiVeG-ocJYHEkCLTCQnxWAHlJofSs0kFGFLK7JXndbaCBwEXrRTpVjgWbSoKPGlWXjB_ETgtOGN0lYwHQOqlRFiXxYKMdHVLcmdIc0UnhBJYc2pqwAxl53XuxoOxH2zuAOXYKOVYgwoeUKKTEs347p7i39rIbQof6oIKK9IKWjch__jZq99LOLHUddwoRXfAu7Ua3J3hF820hsbXe1-emPZBl_2Vdp6c08Yuzzfe3QOIGTrNghitDvwOg_Ey69i-mnUQklqtvZLEkROYTXMzUNJsBhZZpbZvuEIVGZmXbsoI3O_TxDCg8IJK6T22cDk5BqTAi3_Wxzh6Hy6xTsj9bHLXQwIwbTH89yVGLxbF2zc76QQL_y-EjsxVw-OTCPmx7yhAilD6XHDV4txKaUxVEYdItYUexB5ZEM1iFg4mH16zycVR25A1Q7UqGa4kGhLgn6hQo4fuHHDihKu_Q-ON3r8ozGzXWqZRmkuGpTRpaw43__Maw6_Ct-ksJ_WZYAnno1ssnlmNJK0wIfmIm2AfVyXbrk-4tUO-aNPc_Q6DEqyZRDClmY1bE9jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ec883c5b.mp4?token=u1RZOJcH9Ry2X0AU1mObV8LtlE5pHxQp7jefrPgUoibzQNM62RtBF7ll-OLA533qki_ue0jmwvvzc8JZo7QpjZnkYeEfEI-bc3eUw0-lsFoBR_RybtxqiVeG-ocJYHEkCLTCQnxWAHlJofSs0kFGFLK7JXndbaCBwEXrRTpVjgWbSoKPGlWXjB_ETgtOGN0lYwHQOqlRFiXxYKMdHVLcmdIc0UnhBJYc2pqwAxl53XuxoOxH2zuAOXYKOVYgwoeUKKTEs347p7i39rIbQof6oIKK9IKWjch__jZq99LOLHUddwoRXfAu7Ua3J3hF820hsbXe1-emPZBl_2Vdp6c08Yuzzfe3QOIGTrNghitDvwOg_Ey69i-mnUQklqtvZLEkROYTXMzUNJsBhZZpbZvuEIVGZmXbsoI3O_TxDCg8IJK6T22cDk5BqTAi3_Wxzh6Hy6xTsj9bHLXQwIwbTH89yVGLxbF2zc76QQL_y-EjsxVw-OTCPmx7yhAilD6XHDV4txKaUxVEYdItYUexB5ZEM1iFg4mH16zycVR25A1Q7UqGa4kGhLgn6hQo4fuHHDihKu_Q-ON3r8ozGzXWqZRmkuGpTRpaw43__Maw6_Ct-ksJ_WZYAnno1ssnlmNJK0wIfmIm2AfVyXbrk-4tUO-aNPc_Q6DEqyZRDClmY1bE9jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یوتیوبر معروف در انگلیس: افراد زیادی از سراسر جهان خودشان را به کربلا رسانده‌اند و یک چیز می‌خواهند؛ انتقام خون رهبر عالی‌قدرشان [امام] سیدعلی خامنه‌ای.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454570" target="_blank">📅 10:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/047db8a693.mp4?token=gM2A3qYi2sdpWB_Wecb_PUL9hbRVw5nlna7rxZqIEUn35cuxd6JOHXWooD28OGfErSTEbX36DK1rW-cGxuhEeln8Aw2YNU3tGCRFZexDM2rpmmwLpc1IFuEVYVpC7y3F29MhwisC1rDHdTOdL7lTALAaCL9WQ9VUAJNDjoUYme1iWM5b8n5D8T6c9lSjXziY1RIF5aM2Ctqa1DbzvL-IzBIAtUSdrMXVRrNyb6y4_n5OMdJi4tpGa5RX9K2Cu6nMSt3yiqvGA0NgfHTKF5vS2qywaSElMgZCCcQq1Wsr6aMqz5m6iShsFfbOnCqsn2280pCbHpNRFDt9q2LiH_-EYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/047db8a693.mp4?token=gM2A3qYi2sdpWB_Wecb_PUL9hbRVw5nlna7rxZqIEUn35cuxd6JOHXWooD28OGfErSTEbX36DK1rW-cGxuhEeln8Aw2YNU3tGCRFZexDM2rpmmwLpc1IFuEVYVpC7y3F29MhwisC1rDHdTOdL7lTALAaCL9WQ9VUAJNDjoUYme1iWM5b8n5D8T6c9lSjXziY1RIF5aM2Ctqa1DbzvL-IzBIAtUSdrMXVRrNyb6y4_n5OMdJi4tpGa5RX9K2Cu6nMSt3yiqvGA0NgfHTKF5vS2qywaSElMgZCCcQq1Wsr6aMqz5m6iShsFfbOnCqsn2280pCbHpNRFDt9q2LiH_-EYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تناقض‌گویی‌های ترامپ
🔹
کوثری، عضو کمیسیون امنیت ملی مجلس: ترامپ ۱۰۶ بار گفته ما ایران را شکست دادیم، ۹۵ بار گفته ما ایران را نابود کردیم، ۸۸ بار گفته توافق با ایران قریب‌الوقوع است.
🔹
او همچنین ۷۵ بار گفته تنگۀ هرمز باز است؛ اگر باز است چرا دوباره جنگ ۱۷…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454569" target="_blank">📅 10:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27bd2658b8.mp4?token=lFR7hTLgWDivoGCjfPuuPDsHhtlCOeLHOERHviCk5Br81AfMU1bYF-HX8v-qDn2oQ1lqUgBPqcDvXCTOYC0js-6xytHUO160Hnidb0OVM2OPCrVHOCLSrjFlEfiX4mPUxLEWdHEfRt1utUl58G6AWy_n1W9870Yb6XqgW9h5KDxJJ0hYcsKxrIXEHNhGddncTmmfszh4DxMOXLZEvRxPovEIuJ-fVtWxXAXaoGYQ7h-H_0o9Eul8wlOIYySNEfc16mxYesbP_dutE0SABKYzSD7zd-hSpyqBS_6GxmXPO6iCawOl1EWUU6UVaasSj-SQb7awxoCXwVQHyfNKCbWoOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27bd2658b8.mp4?token=lFR7hTLgWDivoGCjfPuuPDsHhtlCOeLHOERHviCk5Br81AfMU1bYF-HX8v-qDn2oQ1lqUgBPqcDvXCTOYC0js-6xytHUO160Hnidb0OVM2OPCrVHOCLSrjFlEfiX4mPUxLEWdHEfRt1utUl58G6AWy_n1W9870Yb6XqgW9h5KDxJJ0hYcsKxrIXEHNhGddncTmmfszh4DxMOXLZEvRxPovEIuJ-fVtWxXAXaoGYQ7h-H_0o9Eul8wlOIYySNEfc16mxYesbP_dutE0SABKYzSD7zd-hSpyqBS_6GxmXPO6iCawOl1EWUU6UVaasSj-SQb7awxoCXwVQHyfNKCbWoOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تناقض‌گویی‌های ترامپ
🔹
کوثری، عضو کمیسیون امنیت ملی مجلس: ترامپ ۱۰۶ بار گفته ما ایران را شکست دادیم، ۹۵ بار گفته ما ایران را نابود کردیم، ۸۸ بار گفته توافق با ایران قریب‌الوقوع است.
🔹
او همچنین ۷۵ بار گفته تنگۀ هرمز باز است؛ اگر باز است چرا دوباره جنگ ۱۷ روزۀ هرمز را راه انداختند؟
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454568" target="_blank">📅 10:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBZmfvaPd1IyZO8MzJROxkx5wx9p-11zzZH3UoTkGoxH--bSi2xYHqkO2z1c_6CIyZ2ejKKDDPTkUFroCxNjrgPMrMRCS9e4IF0WG5lk4UTq7-Caw6ZF7UCrgMceNqIq8MxvbRfVeB1LKMv-jUfJF-WTwRNRiJ5iz9S8clEq8KZQvpZqw88idshdsh8EHqOEcTJZp9HyGPG2dp0yZPjefXbY-w6qLpGTEhJmRgEilyI7YxC7gSogb5VcVGv2o0XfIbQ-eToC1BUhvqpHQ_IDsn0XQyaxd1hdOpuG25SAbD8c-cb33USpne356gSyx6xYPU5LT-ewV24O9w2Sy7sxIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده جدید مرزبانی کردستان معرفی شد
🔹
سردار احمدرضا حاتمی به‌عنوان فرمانده جدید مرزبانی استان کردستان معرفی شد. او پیش از این فرمانده مرزبانی استان گلستان بود.
🔹
استان کردستان به‌دلیل برخورداری از مرز مشترک با اقلیم کردستان عراق، از استان‌های راهبردی کشور در حوزه مرزبانی به‌شمار می‌رود و ارتقای امنیت پایدار، صیانت از مرزها و تسهیل ترددهای قانونی از مهم‌ترین مأموریت‌های مرزبانی در این منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454567" target="_blank">📅 09:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دادگاه شرکت تات‌موتور تاک با ۲۹۷۹ شاکی برگزار شد
🔹
دادگاه رسیدگی به پروندۀ شرکت خودرویی تات‌موتور تاک، با ۲۹۷۹ نفر شاکی و ۹ متهم حقیقی و حقوقی و ارزش مال برده شده هزار و ۴۹۸ میلیارد و ۵۵۶ میلیون تومان برگزار شد.
🔹
نمایندۀ دادستان شهرستان تاکستان: فعالیت شرکت از سال ۱۳۹۹ در قالب پیش‌فروش و پیش‌ثبت‌نام خودرو با وعدۀ تحویل خودرو با قیمتی پایین‌تر از نرخ کارخانه آغاز شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454566" target="_blank">📅 09:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رسیدگی به پروندۀ کلاهبرداری یک شرکت مهاجرتی با ۳۰۰ شاکی
🔹
دادستان تهران: در فرآیند رسیدگی به یک پروندۀ کلاهبرداری با موضوع مهاجرت ضمن پلمب شرکت متخلف، حدود ۲ همت از اموال آن در مرحلۀ تحقیقات قضایی توقیف شد.
🔹
میزان وجوه کلاهبرداری، حدود ۴ همت است. تعداد شکات پرونده تاکنون ۳۰۰ نفر و در حال افزایش است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454565" target="_blank">📅 09:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GObSlaSxTjsv1fE197UEVRsT5hHOJSJy_NdtoGyQx7fGi1xBDXVmtcaM7plPnlJqNzKOEXWosfDx4Qu9j5lRAsyhNTIkHu6IVCqeAtv6NtI_kR-GcQZzuWb2Hvs9vP0KAuguy8gKldzwaUfBxqJixLEzB96CPG0etMQjoFJtKryO9o3GkWiDJzR3xXxaDa-Umt45r1nB6t3PY59vwbowctSGH4uRzOp1hmiwZebJixWYjWS21BRhlrNzCXK0iLF4wiHA69ycJt1M9RTdVZDfwxN58cFL1KlatkCiDNVhOBGBDD4ApYIVwiL306rLY4XzPmnLxbHKBBEfPycNwIX8pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اولین‌بار اتوبوس عراقی زائران را به ایران آورد
🔹
مدیر گمرک مرز خسروی: امروز برای نخستین‌بار یک اتوبوس عراقی زائران اربعین را مبدأ کربلا و نجف بدون نیاز به جابه‌جایی از طریق مرز بین‌المللی خسروی به ایران آورد.
🔹
در ایام اربعین همچنین تشریفات خروج موقت ۱۱۰ دستگاه اتوبوس ایرانی از طریق گمرک مرز خسروی انجام شد و زائران با این ناوگان به عتبات عالیات اعزام شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/454564" target="_blank">📅 09:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شهادت پلیس اهل سنت بلوچ در ایرانشهر
🔹
نورالله ناروئی یکی از کارکنان بلوچ و اهل سنت پلیس که در جریان حمله و تیراندازی چند روز پیش به خودروی پلیس در ایرانشهر مجروح شده بود بر اثر شدت جراحات وارده به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454563" target="_blank">📅 09:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb1ae1ed3.mp4?token=Cj951YI8wShWfXv_KL9Lgq6aL8jqsupuaCCIsBxqBHTlcvDmdWFkoHCP3ahu3y1YTFhQ14IvdWW6WyIXH68oBWPRLf789yTj6xn_06_QqDZt7k_rU8BxcTlMHksApuPlUXyDIknFfFowYI5b_Dqreng3ByumGmBkgqzTQqyB3fCGpPXSwv6biq-C2H-LUGoPBc9RO3j18hiJP34l5rL5aWmJ-W2v-fTqACdzjtfqIfCwsSpAjv08f34H_BtyLGXjXhiKrqW2QzSgo0WXtENhhyw9oQyug8uhI22ss17n0qbt7RR0KGSSIL5PHfvo8GPaC-09gwYyhn0UiwwRuiWCcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb1ae1ed3.mp4?token=Cj951YI8wShWfXv_KL9Lgq6aL8jqsupuaCCIsBxqBHTlcvDmdWFkoHCP3ahu3y1YTFhQ14IvdWW6WyIXH68oBWPRLf789yTj6xn_06_QqDZt7k_rU8BxcTlMHksApuPlUXyDIknFfFowYI5b_Dqreng3ByumGmBkgqzTQqyB3fCGpPXSwv6biq-C2H-LUGoPBc9RO3j18hiJP34l5rL5aWmJ-W2v-fTqACdzjtfqIfCwsSpAjv08f34H_BtyLGXjXhiKrqW2QzSgo0WXtENhhyw9oQyug8uhI22ss17n0qbt7RR0KGSSIL5PHfvo8GPaC-09gwYyhn0UiwwRuiWCcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از امروز تا جمعه در مازندران و ارتفاعات البرز مرکزی بارندگی داریم
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/454562" target="_blank">📅 08:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار کنترل‌شده در اطراف یزد
🔹
سپاه الغدیر استان یزد از احتمال شنیده شدن صدای انفجار کنترل شده طی ساعات ۹ تا ۱۳ امروز در اطراف و محدودۀ خارج از شهر یزد خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/454561" target="_blank">📅 07:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D30po8C-mGyaDuwp9QiiVE--G1_UecFwNIi6yDfCwHr9ZA9-jWrz70BdRAgRpdKKAdQuNlqoZVWgltY8ScV_iDbbFVD5k-KzuFCBrQuA4uTg0Q8FkzzgSqzwULgkWEWVIyWS4IwLg58S4SqBZB865gNOlGS2WXKi9jFy7bJ2erUoukeQN5HqJJYT5i4BZVA3ClmqjSgwWbvI4UyJe6aGDH4_f7Ep0Q_D2wzmhr3YmgXZIpxT_BTPLrSTt429awWqCNyhwdVsvrJ4DQaD0gMw5jxmwLXqHe-ISxNX7fwAi8JTyrJZNA-KJdgz5nRLFCD9S1HTaMpHm6zqQD24TsOC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای پایتخت قابل‌قبول است
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای پایتخت امروز روی عدد ۸۹ قرار گرفته و در وضعیت قابل‌قبول است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/454560" target="_blank">📅 07:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBBU2XgAEk8THQFhSxfwgATiy6DIepmZCGdxAE1DQN80Q82z33TsCdHC9ggjriNXEVKKAgbW-kZEAWCjVKpg2yIgDyz3Yufrhd_XWfVgpopD6pic6zB_tAGKPmv9z-aLW7oNQMJc5a9FiX-iqb4cArgAhKMYvWWbHqya236hZPXrkW1zWfSkwNHAoPemIzI4ISyt259r4vAEjFiovdbNt9o1ElW2Iq8FDtMLONxSujP3bjO4FJx2Du09jzgmU1WwZSDFXimhSoq4LOZugkp__yIsV0EMBctKTeJXF6I685ECtW1zUgrw02H3euRcbFCB7G-_GUHExLyNfLPD_bCcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: ترامپ وعدۀ تسلیم ایران داد، تحقیر نصیبش شد
🔹
روزنامۀ فایننشال‌تایمز در گزارشی تحلیلی نوشت ترامپ که جنگ با ایران را با شعار «تسلیم بی‌قید و شرط» آغاز کرد، اکنون خود در موقعیت تحقیر استراتژیک گرفتار شده است.
🔹
رئیس‌جمهور آمریکا و دستیارانش در پنج ماه گذشته بیش از ده‌ها بار گفته‌اند که آمریکا «نزدیک» به توافق با ایران است. اما اگر از دل مذاکرات ایران و عمان توافقی بیرون بیاید، این توافق بسیار پایین‌تر از اهدافی خواهد بود که رئیس‌جمهور آمریکا هنگام آغاز این جنگ ترسیم کرده بود.
🔹
طبق گزارش فایننشال‌تایمز، از زمان حمله به ایران در ماه فوریه، خواسته‌های فوری ترامپ از فهرستی بلندبالا از امتیازات شامل برنامه هسته‌ای تهران، تولید موشک‌های بالستیک و حمایت از گروههای مقاومت منطقه به یک مورد کوچک رسیده است: اینکه ایران اجازه دهد تنگۀ هرمز به وضعیت پیش از جنگ بازگردد.
🔹
چیزی که به گفتۀ منتقدان، به‌خودی‌خود چیزی شبیه به یک تحقیر استراتژیک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/454559" target="_blank">📅 07:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9658f031bf.mp4?token=IJb5D2OW5LpNPFHniyFRrou1-ySreY_nJUYpip7SW7CS5Kz0gN4RLAm8zKbxXsIwYMLSTqgpsPDQ_VjE1n5KZwC93m7DwryxuNFzdyH4edqqqk3rlYppzE0MOHnEnegtdutXHIkvo76kVCLWzp5PonaZinqjV4Vxm1tWnFvhZg12NHOgVx8v7uBHm-FchQ5BIcEwBsjaR7LpdRgD2Xm2q97ZSgGrq3oFYRJbYycDrw20GUMU97auT2HYORGX0qteZoSDzfMY0w9rHXXjtcVUOVn__7mTPivKpYjTTelU9OcBu3l3oLRyaIFB7IrLBicEK5yDwD8DNln4_FJ64sUOFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9658f031bf.mp4?token=IJb5D2OW5LpNPFHniyFRrou1-ySreY_nJUYpip7SW7CS5Kz0gN4RLAm8zKbxXsIwYMLSTqgpsPDQ_VjE1n5KZwC93m7DwryxuNFzdyH4edqqqk3rlYppzE0MOHnEnegtdutXHIkvo76kVCLWzp5PonaZinqjV4Vxm1tWnFvhZg12NHOgVx8v7uBHm-FchQ5BIcEwBsjaR7LpdRgD2Xm2q97ZSgGrq3oFYRJbYycDrw20GUMU97auT2HYORGX0qteZoSDzfMY0w9rHXXjtcVUOVn__7mTPivKpYjTTelU9OcBu3l3oLRyaIFB7IrLBicEK5yDwD8DNln4_FJ64sUOFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با همین کارتان فرزندتان را بی‌نماز می‌کنید!
🎙
آیت‌الله حائری شیرازی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/454558" target="_blank">📅 06:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تهران از جمعه خنک‌تر می‌شود
🔹
بر اساس اعلام هواشناسی، امروز افزایش نسبی دما در استان تهران مورد انتظار است، اما روز جمعه کاهش نسبی دما رخ خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/454557" target="_blank">📅 05:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454555">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">برخاستن ستون‌های عظیم دود از بندر جبل‌علی دبی
🔹
رسانه‌های اماراتی با اشاره به شنیده‌شدن صدای حداقل ۷ انفجار در مدت ۲۰ دقیقه، ادعا کردند این حادثه شاید به‌دلیل مشکلات فنی باشد.  @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/454555" target="_blank">📅 03:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454554">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH-rczei-QTkv9aNdqcjoD_Z2b-b9NYE5RzgH8U9aKnf-P5OHlZXTdCUFTJSiRwTriAOpYzlG4tS1iKaIbjqjY55z0_sqrMh2JGPpOMK0iufW8vWNzcfFWvyIGiN8b7L7TMaw_ZmH3N8B0Ttf0jzWBEsCfQGDfRmxMN5tHXQZXY5EOXsjXIze3wwBb7mZ8fPEn3P_lQCGtDrPi4tB5DhDOMaGo5q_xaNPqfq81sivyW_TD33ZwlMEW0tQj6hLMImsr1kU0F09ZZr6Te8c11KANq_g8rea1wGiUxxZTSrO68JC9VLWeOD24L0RnJ0fg2MnKXBknhN-Ay7DtamCGVK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
انفجار در منطقۀ صنعتی «جبل‌علی» در دبی
🔴
منابع محلی از شنیده‌شدن صدای ۳ انفجار در سواحل امارات عربی متحده و آتش گرفتن یک انبار یا مخزن سوخت خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farsna/454554" target="_blank">📅 03:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454552">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufHTBbB8XFt-D8MtghigEhObeP61UXln-gJoLJ-M-FcrY-FxeLqOSCNza_d5_Xt6P7g5Hg1Aulsq7Dbk9SbShR7PTrBr2G0FPz8WNdIfL5I1F7vHTCzUZ9zYOThvL7Nt7YKLHnYF0fF1q18t4DGHf1YDfwvrPEmxwGvgRk26XB43G9lFN2wNu7v8jTD2lguDouaafTOYMETueri_DA6blYj7rQ04XyQYtqB0qIQKpKz78rOVfCdtbbBE5pSHXG_2_d38C31Y2vE895qzweZik8DWdg4uR42v6-AgGO6RCpqo9GPAW8IjZYJk3Qk-m0pFC30fhdUwbAT-3Y1m0DE8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1nUR0YKvrn4SmR0zwUUlJL0uAEZrzTRBVPy9HzKaXDVCJuv_5-jH71cAhwYeJCJ2i4btiqQXFkL7KcDn24mp-TMxxz8ALjvGHgl59264mFEzHJEiBbY1Nc6F3ZtWHMBR81iMizKlndJtjA1Mh21t3_xDpzNq5NVi7UDU1drQdtSsB_4RgI5ju7Ylqux4bmCW2drRzt8BDSvS8XcGnJgdkMYJf-uwRTETykx2pIyDsphdmTfay6fM0BmLEpkXtWilQ231JQU8V1H7_poqGb96tyxf3FmZWvdaHPwLyiu95bi15bb7hZKQRET7MmAjN9FpjTwenceF6IQtPMVJUu0Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
انفجار در منطقۀ صنعتی «جبل‌علی» در دبی
🔴
منابع محلی از شنیده‌شدن صدای ۳ انفجار در سواحل امارات عربی متحده و آتش گرفتن یک انبار یا مخزن سوخت خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/454552" target="_blank">📅 03:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454551">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
منابع خبری از حملۀ عربستان و وقوع چندین انفجار در صنعا، پایتخت یمن گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/454551" target="_blank">📅 02:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454550">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBW43EqictE70kuSRdfMWAetImAmEcPv_NnIlytGgS9wyXQzY8HUvKjjbSpFrs-6VjD7BEOFFIQBK2NNFoHZ1EzlAVXCc8nJktSnfXXWg6ZqI72L9LRksQS1PQHZ0D4vcn8p8QjRVPaKDptw8rI0M2xuDMcrh3XOaSpYvF9LkaIDeXEDrBKN8nQegpHFVlsYzcWThgpnin-xKrGQuJFzYCGOxgieKtvwnouPFjiIB8s85k8QrjRbp0go89FaSjVFo2KFcw5gP3HssUsTxoor0QvtxcapiYM-yCeTOHyGhwE_QBgOso1f5RUDoJFKByiGeRJG1EuJBsViUNsqasAEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار بی‌سابقۀ کشتی‌های سعودی از باب‌المندب
🔹
در حالی که عربستان سعودی از تشکیل ائتلافی از ۱۴ کشور برای حفاظت از باب‌المندب خبر داده، جدیدترین داده‌ها نشان می‌دهد که تردد کشتی‌های مرتبط با این کشور در این آبراه به پایین‌ترین سطح ثبت‌شده رسیده است.
🔹
بر اساس تحلیل شرکت بین‌المللی اطلاعات دریایی ویندوارد، میانگین روزانۀ تردد کشتی‌ها در تنگۀ باب‌المندب از حدود ۳۰ فروند به ۱۸ فروند کاهش یافته که نشان‌دهندۀ کاهش ۲۲ درصدی است. این کاهش در بخش نفتکش‌ها با افت ۳۹ درصدی همراه بوده است.
🔹
همچنین دست‌کم هشت نفتکش مرتبط با عربستان مسیر خود را تغییر داده و به مبدأ بازگشته‌اند.
🔹
در همین حال، شش نفتکش با پرچم عربستان به سمت دماغۀ امید‌نیک در آفریقای جنوبی منحرف شده‌اند تا از تنگه باب‌المندب عبور نکنند.
🔹
یک نفتکش عربستانی که از منطقۀ تایوان به مقصد بندر ینبع عربستان در حرکت بود، به دلیل تغییر مسیر از دماغۀ امیدنیک، زمان سفرش از ۲۴ روز به ۵۶ روز افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/454550" target="_blank">📅 02:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454547">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa13bb083.mp4?token=iyBOTDAr8pYFnyo4dGSJ1gLKDvrjDUpCcDtERwuyvrs7NSEHkIc_xtU1Kn2Lhgi9crY9745mdi90BzeIhSl7BWL7_IEIVo-buyh7ouQhAcGmQw8nRkmTlv0ocBOLsGgEL8WeI5rMAokfYRpBYNs87WcVCowTMzkalMqWGBRWyCzr_G8Ol8Yx5Or_6epmLiu0PQ3v783rXIX3LVm5x6AnJCp6puLFwqQGPuQJn1xBT2pAVXentbF7yqdCz2E7Ja1BxL_8sOeTGmLBGKLLNatMzVPfAibl58QKnBdHco5b5UdH38-FMOVWGv5u6DLaw0iQyHHSCxrX8jW1uyUf6EaTZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa13bb083.mp4?token=iyBOTDAr8pYFnyo4dGSJ1gLKDvrjDUpCcDtERwuyvrs7NSEHkIc_xtU1Kn2Lhgi9crY9745mdi90BzeIhSl7BWL7_IEIVo-buyh7ouQhAcGmQw8nRkmTlv0ocBOLsGgEL8WeI5rMAokfYRpBYNs87WcVCowTMzkalMqWGBRWyCzr_G8Ol8Yx5Or_6epmLiu0PQ3v783rXIX3LVm5x6AnJCp6puLFwqQGPuQJn1xBT2pAVXentbF7yqdCz2E7Ja1BxL_8sOeTGmLBGKLLNatMzVPfAibl58QKnBdHco5b5UdH38-FMOVWGv5u6DLaw0iQyHHSCxrX8jW1uyUf6EaTZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی گسترده روسیه به کی‌یف
🔹
رسانه‌های اوکراینی بامداد چهارشنبه از وقوع چندین انفجار قدرتمند در پایتخت این کشور در پی اصابت حداقل ۳۰ موشک بالستیک روسی خبر دادند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/454547" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454546">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCUaaHtvzwH9-nPolKC81cEHxRlZNIfcL3nAmlF3wZcOQxP-VPddTSsnKNm4Mf_cw7HJ9Vg71tl2AI29fasboT9X6RnLnx90_vdlwF3GS6cQaXpdaC5B8IwjeLYfG0tklwFryDcp51MHLS72_Y51vL8usF1a1KpxMd2ycteoWIcAAVlyFFfyqzhXTJuw7j6h2Tmv0xh6tLWJlGX1lx6Qyph7BppQ4mr38kQCKqO7x-6S7B_UZ0feJ4vSVXqo8OLVoYhQoSi8NszUG3TjhyJQnMADJZe1LgxrCaq3NkOWcQch7Dar5jlXG4EnWkvY2WDugm7Z9zsQ2D6V-QYMFDT6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روی ماه اتفاقی غیرمنتظره رخ می‌دهد
🔹
یک مرحله از موشک فالکون ۹ اسپیس‌ایکس پس از ماه‌ها سرگردانی در فضا، امروز به سطح ماه برخورد می‌کند.
🔹
این قطعۀ چند تنی که زمانی بخشی از یک مأموریت فضایی بود، حالا به یک آزمایش طبیعی تبدیل شده است.
🔹
در نگاه اول، سقوط یک قطعۀ بزرگ فلزی روی ماه ممکن است فقط یک برخورد تصادفی با یک جرم آسمانی به‌نظر برسد، اما این اتفاق برای پژوهشگران یک فرصت علمی کم‌سابقه است.
🔹
قرار است این موشک با سرعتی حدود ۸۷۰۰ کیلومتر بر ساعت به سطح ماه برخورد کند؛ سرعتی که انرژی عظیمی ایجاد خواهد کرد و احتمالاً دهانه‌ای تازه روی سطح ماه به وجود می‌آورد.
🔹
این برخورد در نزدیکی دهانۀ «آینشتین» در بخش دورتر از مرکز دید زمین رخ خواهد داد؛ منطقه‌ای که به دلیل شرایط خاص زمین‌شناسی خود، مورد توجه دانشمندان قرار دارد.
🔹
دانشمندان امیدوارند داده‌های این رویداد بتواند به طراحی بهتر مأموریت‌های آینده کمک کند؛ مأموریت‌هایی که قرار است انسان و تجهیزات بیشتری را به ماه بازگردانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/454546" target="_blank">📅 01:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454542">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8dlmA2u_MlMzw1IX4qicQVvbBsCrMYeTp9V8DLACKgaXpTW5Q8z3PvEvIVz97d9rz0WHjR-DdFPljQdRIN45oV1ean0s7FqJFpfCaIuzr9IK9cOHoY5OySyPuE5uCrTLuPpDeWtVqEgwZU1FKD5UapKs0Sxi7kFSg14bxAl9MIG2MsYKbwt5_zuytxvFuG5Nt375xCjsRdTs343xjle200j-ROfFbhe1mNr3Koz3sdAvq52Mydf4DIYT7bUr2LhQp3RCg9aC2ST95TvKnNx5AvcJPfCbQ9buSpWdqtOp37laGpZyL1ZkTlD8_aZB65tbS2BPg8X6FbBF4z1G_n1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRQYAL6CzoZL4dFzWiSSVsimoE7dsGKpq5_SY5-I36ZLd3Of4Z-Sd65BoHv8wEgx8oTzK0omaZRZ3oSEUtYhoSZ-OV66xV_qD87ehtRgwEGbF1oAWhr95EwbzVV2f1hl42lwcEhh0WV4G9w1zz9ip5JrO0FzQOfGwNOR3UZ-DNJEDS4dBS8wNkuOQffjLM5w0VCgpEN1SvWwJXHpNawqtfSjXqt8Tz23EuIyt2aPbC5PbagYeG2A6PzloKI642KGTXs2nBSND8mBLeEc2aMk6ZFKUtWr7oQHeyOPuR0Cn_lmFQD3_evu5bHZQ6zGvqTSZQFtnUvvoMmD4vXcxl4nDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lD4HApvYpZ0NCvE72SlZPdrShMtXVDiDJTXk5BE9OYW6zkubtxz-9iuL2TU387gKDioj3ixxBKvTVmGvuQiB0WVN6v3dWHGGC21JxEKWoSiDeGd0RuM5_-v-PoaCJFEZj1skM8nsZ8GteoN7mVml_vdKxNPJi1eoFguoY2u2z_s2duMwrXpI6yJ4cmnANv-A-rxq2xYSug4Mqa57uGIUnF0PAxpAhrrXvZotGTxpPXqX4jEIPJZTnB0hVz-KJtI0HU9cI5yDGTbzne3zUM3ZhkoTkDudOx6wWoWJvCktecuQ4bQTI3J8XjcPILDjbPqbSbD1oJ_A3xkGIiqPgzjpNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRi-4nTKODzwGtbwoLaGZaNGmMo5JFGJvDIhP_rynwL1JJWKD08vLx1cZ83PBVNhs_q5OEvX7ULQAqTe_6-LCQyhobV04YsJ1mSyUcxWot2C33iF05q58lzO90pg0MHcLqZpjlvU_5h32WjRoF_VVhBD8tDTywzgttGHJCQstGom8Dh4D2TlqJty5ZP3Aza5hB5JP0wTNOGelc5zAhpUMekHm_7BDdJ72l7NDOKOtQOS9g-es4_StMBTtR-YVu3XoVed83dlbXuV4xxwneZCdV3VpjKjba1kOoL_l8LxDUpRTLY0jEZXoGMP_Z04tPz_D-3zenM1xSeKwbqWP67QOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۱۴ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/454542" target="_blank">📅 01:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454534">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oeVbUSMly_6Dt_FJUA_mFdr1y4SxbJMSRNzjSQ_-vSDIzPIWhrULBnbxDxc37N4GvDdhJTZXOZ5X512pZF6KCPI7t_Y1qHQJ5O-IsZLaeC5WI2aM2ZnMhOI7QHOPuCHW1xDkQc-MZ8zmlQftdndfcwLFBeth-EdOGRe6VqiPb7BdtNXc3AadyGhbF3AIH2RPqwDwfCsZX30JbympMrmZmHTEgHkjqczozyX7ztZCe1_PSZox4oNkKslvV_MNLekIcEupkmpghfLr51SEFbg3kHrlTxjBPOV9zn_cGIJk1L5DA1U9bGUxvFVjk_pfYoMdYzO7zBBlYxLBINEdzXUTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L741TBQYxyXRzxBbKoPCFdFrXhW8yTCVCIPm51_xEEEo62TFV34qb4ccSyqFOqalZEtMIlcxFuVzdg1NPvnvFOsYpxo1zFv_W-mBUAWU7dALdUP-GyGQF3R8UZ5yBAqRxdOYzZHrXY1lEOQrcCjTrwe-DSAjRKyw3OxwMpzlbPdzSEInS5qpWLmLQSVezJTH7G7hpRteNobbC1JxwNsKVxBXvvULuiDosfDulGbMNG1KQ4uwzlztSzHyNzWahbwnB1FDZ5hzFsDCh-Ub06B58EwlA7BDkWKa5RC-F4kIdsgx6yFMIA6da9G7wnqG54sEqqRvrmX7Jlu-pidjB2z6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8q2uFf3XnV1BkLA9W0ILd_O_DNakbUi5bxgb1-TsXcBYv35GZoAvDCG7RjX-omPiYrG9M3Nna6t4Uv2JjcP-y6JdHXVQZFXCgeI9KaQe8ITgobzRHRlnZ66r7q2gJ9F8CQ5GrUb_Eogz3Z9SWw3FtyoHGHt0e_5NPxgAuQxkFHFNGODBjEbGOCB9kEMqEdXaKBZAhFATt2h1OmG8VfgENzYRY_kFhKDvjaqpO3xb0n66TQs4uc0-zIsk5ysHFK-JI4Pr8ggFjtlVEMH7f3ZJdgXiwT63yS6jPxVfb29zUk_JXypmgynnE_lnHNTrqYsSvaqq910udhk6GZI-YqEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uK6ywvDxf_FyrycxfyG2NqApGf4-D4kDoIx4nBQ7Uvs5AYad7r2teAxdHl9radakCeLiZzKyhA4N86T3oUg7JUY2eBgAAqsK-v-lhf_GnCKVBWOKeIoknUzEcTJ8oEm_4tX7nAsg2ayaSPc5jhpZsmuP8eUsGBdVswwKQXQQRXmdFZRTFJhIxpH9kdb58oKS5SxRQ8RLQzKq8W4rzf3SLOiJwF6rR7oN-ZMZypl0B55Mcpof3I61jTcgfwYsyR7FOS8ffXH1egvU0gh4_ou6slbxywsxK7QhtyLW7L0_ZLm8aOKo7zg2fhZnqDS7tToPkV5K-rXWHqKmsvwiQt8zqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knTAEUCrLCS14fDwZGryXufGrxPUWeNs474ccgu5k4b5GKjpqA5yzTGUqJlIJzyL_hDR9wzWhazttQE2MNu7ZQ9kBob03kqSDAKeqWAsUj4PCw6f8xFU3zsRXF2vIBQmhMmb90fAOk7N9QyqVrBZ83C2Itl6TOPPFAT8b2W1LaZ9iuXEGqYh_rp3g7D3XjMKo4L4X7lMQK87K8f9svDDGxwMpO8FM23sHaHd4I2t7RedFi_ePd1ch2WUJ08df3zjqe5k43Ed7gorfsVEJnGrlIP9BT19WiLs2Qhf1iQauUxVS6xVEFh8CIucC3lEvFtJ9-DUdB87mIsFgIcwzRNnHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcEfHMiuiR-JFBnUZju2q2a5bb1iuVgO0bI3SZOoocENKxqD0N9s2FdVWd7xX6X9Wa7v3BA8L9WSViL9omGvA9PwnkTb67jKvKU-I-eyVPnuG8lOvwW1EO1wAbcqKelVLdXPa4feo-MA1PYSQVmlB4A2Hs1gJBCCHklM9muenDI1XD3iyc9_4vZgToa5EJermAvcTa7ujQruaTct_lFMDC-_ElXODT2Ywo_Q-8HRDI_OTWwx5orc_v5oSya3HuI6RJBrSxin_fCawJJva7fCAIITd0w2AddR-jnz0u9-UtjcTtEqALONXM641t9QKaOlBIuoVIqL6D8kA0jD85LbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5O59xvH89jOf7DEo59W2BmyQ4PbiOajI2SSWWQT0BaJ0o2ex_iTDLMFxzUNr2vLNJ0OaaadFaGjERdKMEKEMK_OYf4vG-5ED2HbeA4xEvROvyUDbW3aUp5pS49s8UHuj_-l08NLJBE_BXkNKgi99ji-9GxUm1JrNW9_ZOad2x_aUlWCReTRvcUZrdT00V1H4Y4SHnU7yN4rPr7GTfYnPcC5AbNuHOTM5UPEFX46zXlT2ZPH_mHISk_0y5lqyLf6lPTKxbbNUYP9ttP6F5v43UyI-9le3NYEEgnKcl9ZiKu04XG9ZBD2zPybfY_M8QwsJl3etPpi9-HqvpFvRppMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ed_R-2cdiWzwppxTXH3lgHLWfwmHDWQP9KeWOE9sOZfbrsavezlTWiFd8e9ojDav9jP1MXO_E8x8Bh0Scf-KmJCiZO4DObbVaCs8Rcxs89XD_I5Ar0Ph0EMz_4hmZ44nDrvOz-GX5d9GTnRagYkbaNiwSbVvMgUJXFo1gAwuGmVqIJNhzZMAFh7OS4EjgnTPPWl_W7hbruKoro2nZAKP0uotJfSZ_nNYh20dV7X77uhjd1gPTODEbtiL4N188wl1cG0TbvNBkjk9CyIr60jskXQvOPc7J42avOt9VmtwerCSZdoR0VqprcnfZNqRTLKNj5X7s-QT_fJzhDNw5UyjMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454534" target="_blank">📅 01:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454533">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">منابع خبری از وقوع چندین انفجار شدید در کی‌یف، پایتخت اوکراین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/454533" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454532">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2b13B4yDV473u_1flr3vvoTnRsHkYySkbg4cxEpxFKLv3taHrL65x_k1aoRBQz_79N2OgX000qgBov3MaNKwrtdfCtfDAh6mhyt2oGRMSf-YYFJ9fX5NUEgCkWCocsv1zUE4_yOrIzIWPPeq_eu3kIhlCH3kp5WmRvD0Wp_-KZpr9b8sIYbChXMBQ5l2uQoTqAhyiS5P1n3Kg_iDuyuUeq9mhHZTDcMjppEVXDNjM-K66IVTao32zN3EKzgTvaUQKYh-asEsANAtXi6fp05tDhPPsupeYkCC5G3IvVbb27AO110mfHTU0Rz9d9tXyWecTproP_mHLCEIg1IVGPvjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: جنگ ایران، ۸۰ درصد موشک‌های تاد را مصرف کرد
🔹
منابع آمریکایی اعتراف کردند که حملات ایران به پایگاه‌های آمریکا در منطقه، باعث خالی‌شدن ۸۰ درصد ذخایر رهگیر سامانه‌های پدافندی «تاد» و همچنین نیمی از موشک‌های «پاتریوت» شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/454532" target="_blank">📅 01:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454531">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ادعای تحریک‌آمیز سنتکام دربارۀ مسیر جنوبی در تنگۀ هرمز
🔹
باوجود هشدارهای جمهوری اسلامی ایران دربارۀ هرگونه تلاش آمریکا برای بازکردن گذرگاه جدید در تنگۀ هرمز، سازمان تروریستی سنتکام ادعای تحریک‌آمیزی دربارۀ مسیری در جنوب این آبراه مطرح کرد.
🔹
سنتکام مدعی شد که مسیر جنوبی تنگۀ هرمز برای همۀ کشتی‌های تجاری که به‌دنبال عبور از این آبراه بین‌المللی هستند، آزاد و باز است.
🔹
همچنین این سازمان تروریستی ادعا کرد که طی سه ماه گذشته، نیروهای آمریکایی به بیش از یک هزار کشتی کمک کرده‌اند تا علی‌رغم حملات ایران، با موفقیت از این تنگه عبور کنند.
🔸
این درحالی است که تهران بارها به شناورهای تجاری در آب‌های جنوبی ایران هشدار داده که تنها مسیر عبور از تنگۀ هرمز، گذرگاه تعیین‌شده توسط ایران است و عبور از هر مسیر دیگری باعث وارد آمدن آسیب‌های جدی به این کشتی‌ها می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/454531" target="_blank">📅 00:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454530">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7UEZkXXiJJvSIywE77TLdGKsDlIHYFNi4Wl4bWXdcSUq-uU6ove5eXirBkpXaT85j1piGvAZ7jkqgh2oZiOwrd3f2Zw6vJGGwG9KuMyoBb_L-z7oAs0h8mkZ8XJ9WwoEzWldfIhn-VZd1TckJTQ33ObhpRX8ykMNliCabLppFq2KFMQZPZsLC2f4oDWap6FGW2SnAKY9ZC-wUuQS8yqiXUupviOpFeigPqnxBEo1odr8PydZM2eibzU4EztgLMW-h9rVTBscagOiG5HT_n1XlDH1cJeobvq8aUKU5jMUepN5BE1rSXi7jFajBatlvoSxPEBl9GyxBFRWpVLro5JiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ یمن به فرودگاه نجران در عربستان
🔹
سخنگوی نیروهای مسلح یمن: یک هدف حساس متعلق به دشمن سعودی در فرودگاه نجران با استفاده از پهپاد مورد اصابت قرار گرفت.
🔹
این عملیات در پاسخ به نقض حریم هوایی استان‌های صعده و حجه انجام شد.
🔹
به عربستان اطمینان می‌دهیم که…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/454530" target="_blank">📅 00:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454529">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f271b99a48.mp4?token=EyyH-dHFdyvMNSxBJxMkN0BBujRXcdWqp05GOKfnaLCPUVQTydkBsimr5VLMijLOcu2xhOF55GRjgXVj4OmhiN33twzRLG7mTaPNHkulm1U7QXk9FiJrfmUIYfCD-1WWnzdTtGi6dtLzSPAIO-jF7lQchzWV-XBAFDtKIXrSPj3kNyhorn3eXIICml-xCIwAgpKOLaNVl2S1bg9Cuhg3ue-M-TBbCA-I1mxQW5ExIpdMBA34Yo7lK7GSBycgeQrvFBm2zKMqdSBw4HmJkVWVqqEgjq00aJEtsWPxl02THEiWoeNou8i7fu8ExVVAHM40O-eE_Wqk__7RpYsSeTb0hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f271b99a48.mp4?token=EyyH-dHFdyvMNSxBJxMkN0BBujRXcdWqp05GOKfnaLCPUVQTydkBsimr5VLMijLOcu2xhOF55GRjgXVj4OmhiN33twzRLG7mTaPNHkulm1U7QXk9FiJrfmUIYfCD-1WWnzdTtGi6dtLzSPAIO-jF7lQchzWV-XBAFDtKIXrSPj3kNyhorn3eXIICml-xCIwAgpKOLaNVl2S1bg9Cuhg3ue-M-TBbCA-I1mxQW5ExIpdMBA34Yo7lK7GSBycgeQrvFBm2zKMqdSBw4HmJkVWVqqEgjq00aJEtsWPxl02THEiWoeNou8i7fu8ExVVAHM40O-eE_Wqk__7RpYsSeTb0hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج بازگشت زائران از مرز شلمچه در شام اربعین حسینی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/454529" target="_blank">📅 00:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454524">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSok_QUg6mLySRZECUP4hvfohaf8gOSFDqSxbR-tDX0hf_aDHqNpCobS6SCkHOjiH9JF5jIvlFuANFhw92ioneC32avbhpiqsivrRY5RG1hAGllr7A9PlkRNq0n6IGFzMHTzH1piPD-R65LBFN7rWGb8hAkFZMavD6CWoGlp5XnxS6eavII_UAQAFzmBNACL6tbB-FLgqmwySBs11t2IbECw-8v3VBYG-CCfbDCkK8s4oRKHT9RPC9ezdSP4Qro7UIG3Sc26Wf_Hqb0yoFFAi7DBnzSK0OrQsiojX-bffJzm888AjfwTftrlt-72MH-3mMQvWrrGjwaChei3PrwyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a7ccecab3.mp4?token=Xby5TcTzBdti365Di-Tqm5JUgnv-i4lSzZjUQceNvgSGAznaAMZTdlI13h1kmabLiZ3tBlw2CcCi70k1WOUssWJzpl-2t8aA3KLr9ljiARB4WWZgXAbjerNCPn2UMaD0LTUY-222STzj797At2qN5xw37aFZBUSt-QJ4kllFm8DRZzJhqeHulUaUEl53nAatf3fxJGY4zXm7gR0mX6OfctfXN__YSmFNeOh-PZsp7yY9ppC2-HXoGMJOKGtKPPR8fncIBveaTsvM1rvTrtVAa3NgoCnozqNagwZzc1EjmhZb5QZZEw-aoWf6MU70UhBnvck06BgixLJRYg2nTUVqKEFQDJhJIBWKTH6rU80xt2NWZORIbLemxClq0QE20YyNG7QHnXU6kAdrW1ASqCGVVb6SVb7dh8HVINvg1_8SCcfKSpUOHTCtTKyThscPKnBbTKq1eXRXfVym2PjY5ApU1U3ZApepUzMmX9XMy6EX-kZmBrTmrFBH_TdpzuyAvNEXpYW-VrrTDWF8QF05ehCiDambsLrxJG97Jr0Zx8pGfnhyTpmDGbgLEw5WnEbKU8zTXGhayxr5atphvj_QzFEZ8k_w3qcaELh2d4cijCtij0YGOz4UQC8c6-LNgK32_MMSsvRT7l7bisf1_XqPbqp0vT-LotNI69dZISER2o0dXdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a7ccecab3.mp4?token=Xby5TcTzBdti365Di-Tqm5JUgnv-i4lSzZjUQceNvgSGAznaAMZTdlI13h1kmabLiZ3tBlw2CcCi70k1WOUssWJzpl-2t8aA3KLr9ljiARB4WWZgXAbjerNCPn2UMaD0LTUY-222STzj797At2qN5xw37aFZBUSt-QJ4kllFm8DRZzJhqeHulUaUEl53nAatf3fxJGY4zXm7gR0mX6OfctfXN__YSmFNeOh-PZsp7yY9ppC2-HXoGMJOKGtKPPR8fncIBveaTsvM1rvTrtVAa3NgoCnozqNagwZzc1EjmhZb5QZZEw-aoWf6MU70UhBnvck06BgixLJRYg2nTUVqKEFQDJhJIBWKTH6rU80xt2NWZORIbLemxClq0QE20YyNG7QHnXU6kAdrW1ASqCGVVb6SVb7dh8HVINvg1_8SCcfKSpUOHTCtTKyThscPKnBbTKq1eXRXfVym2PjY5ApU1U3ZApepUzMmX9XMy6EX-kZmBrTmrFBH_TdpzuyAvNEXpYW-VrrTDWF8QF05ehCiDambsLrxJG97Jr0Zx8pGfnhyTpmDGbgLEw5WnEbKU8zTXGhayxr5atphvj_QzFEZ8k_w3qcaELh2d4cijCtij0YGOz4UQC8c6-LNgK32_MMSsvRT7l7bisf1_XqPbqp0vT-LotNI69dZISER2o0dXdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اربعین در کربلا امسال رنگ انتقام داشت
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/454524" target="_blank">📅 00:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454523">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad9637a9d.mp4?token=I66257Jq2MW2dbJOOtifI0HZ-32y9mo4BmmEuiDIpqjz1BFNSQqZJ-Gt-rJAobX0psw0SsoTl7_HGoAkJtytnoqhKfi2hq2fQMaBATz54ahpd44dtOfZhUMwPaz-6A9A1yyZ-vw8V77zpur9Q7s4k-TMPA2FxGcIVHjiQmAEHM29DP7YSsNP9qI-55hLoGI11vWyPaKxF915AV-vY6lNTmoUxqSzji0DFqSeXcTLAFecnsP6SHZzB3dRHeyebTxwPtQZ4tV7CdPRsIfDgWZbE2CyglzOLlSD8A33xn703WUlODZuOLxoWofLT1h9Hq1wCCnXZzzuTuJr-ywfUfhFVl6_hEAITsZmID1lVkUEMG_OLBVd66AhKVd8B36RmIJZ6zDW3aR9h8FY9ApxrKRA7j0ZuGTcivbFiisj-TskdHaUdvNiO6Q3tZbRYIUxHwzB9i65zcwf1bXNfzlK-bWrl4RvaQbHps_FcsHf73mVmJJLAhtobe84c9w03ChyQBnsX05dGMHaqYYQ_bF5LjzcvIoIOfzOVoyjPyhBnGr_DO6cCaKF5mIkEJm3P7gLDIKp0WD_routNav6pnIPLxTpcldQqVe15sro5faliqvTV7frp_nrdCYXXrV15MdAwKPgJP7NwWBj1EhdNjl0w-NntyYsZD9O6ecZU5wa77tmLs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad9637a9d.mp4?token=I66257Jq2MW2dbJOOtifI0HZ-32y9mo4BmmEuiDIpqjz1BFNSQqZJ-Gt-rJAobX0psw0SsoTl7_HGoAkJtytnoqhKfi2hq2fQMaBATz54ahpd44dtOfZhUMwPaz-6A9A1yyZ-vw8V77zpur9Q7s4k-TMPA2FxGcIVHjiQmAEHM29DP7YSsNP9qI-55hLoGI11vWyPaKxF915AV-vY6lNTmoUxqSzji0DFqSeXcTLAFecnsP6SHZzB3dRHeyebTxwPtQZ4tV7CdPRsIfDgWZbE2CyglzOLlSD8A33xn703WUlODZuOLxoWofLT1h9Hq1wCCnXZzzuTuJr-ywfUfhFVl6_hEAITsZmID1lVkUEMG_OLBVd66AhKVd8B36RmIJZ6zDW3aR9h8FY9ApxrKRA7j0ZuGTcivbFiisj-TskdHaUdvNiO6Q3tZbRYIUxHwzB9i65zcwf1bXNfzlK-bWrl4RvaQbHps_FcsHf73mVmJJLAhtobe84c9w03ChyQBnsX05dGMHaqYYQ_bF5LjzcvIoIOfzOVoyjPyhBnGr_DO6cCaKF5mIkEJm3P7gLDIKp0WD_routNav6pnIPLxTpcldQqVe15sro5faliqvTV7frp_nrdCYXXrV15MdAwKPgJP7NwWBj1EhdNjl0w-NntyYsZD9O6ecZU5wa77tmLs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حجت‌الاسلام رمضانی از نحوهٔ شهادت حضرت علی‌اصغر
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/454523" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454518">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmmrw-QUsC9i-SmJzWybEKWrjY75YFwSL2HESQV672Bbs9IiRGee5BqzOknkvcFeTg0oIijKIMCIXhtSDiTSeMO-3P1raJgXwie9X_P5ktATU_qXSiFt0Lp-SkGMbha4gpYy3MYKtmgNZKEUWmvHmwsEAKfksn9FkzX5CD3FMe-Vq4tRrR7QGNZrewDdPIWXiz47L45IHAKcxs0rQy9o7DBujwP3Qy2gejiflSbbAFB1ObqbHx67pOIK-10aMN-4j_QriAHBu4Ccmo--afIEN-c7mh6ULce4x1QpKJD3swLieKqwn3Yl_6O2JclOMDclfdiZkxT271tph4dJrzQc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9VmiFz7o_cw7XFgFw5BnDWa9zO2hpU77IwJowkhzJfb4A3RTi2rWo7yYzTBX1dFqA9KNbHcic9v7vbTYpYfZPF1MyvjaIcT6e1ZrdSvnOAabbuejZHTTF78t8TyYIl7DutVN53to9LHrdTPLqHj_E3g5u23uf9dk-2eoEp9atHmLUSrqBwLb23DroT4Kl3vKKZZAaOhP2gTyRITTWohofaZ8ZOqIkxPC7Uav_7sz7oLyj5lHTbitgeWxRAfjaZVaJV2TRmEw1-sTCPFNXZj4dhf8udXZJFccWW5OV96tZ_R3jF9oerivqb4Axmf-_nw6f9IlVjSF5aDauAupHmixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_zK9ha5jeSKfwjfUEKCdar2KifaEsS1-GhowuHWtx8uBJkATcaAHpqZOsHitUQB9hfjckmVQomCiOmlDuZQ3P7xyJLZ3wX77Zca9_gc7QPJXggmFW0tGjDdNxPE5ZKTpTmSRoNJJsvzAxoRklWUIPqQMiRpX7cWedxEYio9B25mxvKb8kBcVxqKKqQkOhEZsY969Se_dpm-q6AV3UEWVTYU2SQyx2fzt62ougBbO6ajuqFOX9RCwf6DMawWAmB8dQwcTp2MQnBAcmvyqW5zbfwqRX787eUTJUuQhkbvph2dNXyqA47i5t39WcSrkESfM7wagx-6qtwOGYNN0Zeb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AeC-lCg4Os8i9_JGwo7MUpN7dSbHVUZkIPA5qx4MYKrZV2YM1Pw0wLQXfRXTTMdoNcKbd7-zEc0W1piIXlKe90I11toceDmFnp7zhNTn6oZmNN87M_JmjmYKl_xoRBVeA_U91_SYv5LwkjMSa6jJC5ULyF0zgrJmATtBcZUpM9ixecJJwZrtL493D7GI3l40a1eDHadrlhZ42HRZ0na4huVlU5M19z039N-42csJswIz75Cc27gfu-dtJVLF8He-BiIxDdlXtTi2wjLsWeIyxr7esA-Ahg2iLVC2BFnzelheRb1C0ihWIgl2BOcwpbFwSMcguw6rlh4BdxvSK97OWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXebj5EfcBknW-R0QIluaGKDDd-IxXLqyEnJYvkDuPcnwPa2Jyi7-C8rlC1LGFI2ArUD4Ksy8OQREyvP6ZLawFH8dyweS54mnLwTSrWn7wB0Nsp4ZxFAzLkp5ZPqgX24kVRtmLP3xvb8AfRZPVYkZPVlVCLMiOUmQ3oX_gOfGtZ3hKSfz5LNbJD5MpqGTTBGhbTjxlZwnHzzurvyxf9yUhrwUCgI2Gj_U11v9ed85uMyzcPtxr1NHsyJj5iMlLx9h8dlUPMDEN4YnnQbzvoi3vmL9bNyMTtnQ8RUP1bbdXuq4gUEDh0U1hpwOMVnn5QJdjmpUIRgfISVjlgIYKMySQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیاده‌روی دلدادگان اربعین در بوشهر
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/454518" target="_blank">📅 23:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454517">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7022408df2.mp4?token=bYzAyKy6X1lwiNVELjyaSzg36thHLcnq-IRtqXFol4ilfepBGFirAc7rni3KmfXtG5WOCr-e29Yq_tklSoymOAE2FKL9secOKBRqyx3wkaVXKszoLBNY-naL68M6K_eRQsqyZ-BDuayICFWgw6HsDIZR54Z5BAirZ5s4xRovzjOhEaUL_QaMuxPzj2n6s9Bcx4Wch7PPa-FiEWoH1KKFxLQs574tNGQTX8p3a7gpMsH4M3_1tGMhSszV8mGSdZ0MgOTeRZijxfvJ3WCmzJCDJjRsmRYcP5J5smmuxu-M3uy0Fxpp670Bzah_Mx1RSScWBm5SCR2aonH2jomWkVo0vYkc6g6yW5AFlxmUDmBC0czcs_j8-u4h0AP0CZqKny9ZzucaBkB-7uHWlMxrhOUwXwtbT49sDkhEsZ5ZL-VzqtBiizDo7pcBistwR1I6enuk25AUP0fFZpRu1uqHVbItC6lSlLqItCUMkV78H-mn4riGtUzgAr1I2VfzwwbijAdA2u-YfKqEE7s_nbgqq_TdiW-fVYB1A5DKroFKOMMEPubSnWmrtjfVA-_y7XNaAqmOgME-X9xmAzJJZHAo3RxHZpb-DTxZ20OadyYdHv25d61yoWIkJx_-I3bBk4hk3nmjARo8ow9O0stpeewQJIEeRcoWwPzVvnGOnng0kfIHmfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7022408df2.mp4?token=bYzAyKy6X1lwiNVELjyaSzg36thHLcnq-IRtqXFol4ilfepBGFirAc7rni3KmfXtG5WOCr-e29Yq_tklSoymOAE2FKL9secOKBRqyx3wkaVXKszoLBNY-naL68M6K_eRQsqyZ-BDuayICFWgw6HsDIZR54Z5BAirZ5s4xRovzjOhEaUL_QaMuxPzj2n6s9Bcx4Wch7PPa-FiEWoH1KKFxLQs574tNGQTX8p3a7gpMsH4M3_1tGMhSszV8mGSdZ0MgOTeRZijxfvJ3WCmzJCDJjRsmRYcP5J5smmuxu-M3uy0Fxpp670Bzah_Mx1RSScWBm5SCR2aonH2jomWkVo0vYkc6g6yW5AFlxmUDmBC0czcs_j8-u4h0AP0CZqKny9ZzucaBkB-7uHWlMxrhOUwXwtbT49sDkhEsZ5ZL-VzqtBiizDo7pcBistwR1I6enuk25AUP0fFZpRu1uqHVbItC6lSlLqItCUMkV78H-mn4riGtUzgAr1I2VfzwwbijAdA2u-YfKqEE7s_nbgqq_TdiW-fVYB1A5DKroFKOMMEPubSnWmrtjfVA-_y7XNaAqmOgME-X9xmAzJJZHAo3RxHZpb-DTxZ20OadyYdHv25d61yoWIkJx_-I3bBk4hk3nmjARo8ow9O0stpeewQJIEeRcoWwPzVvnGOnng0kfIHmfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی سعید حدادیان به‌یاد رهبر شهید در محرم‌شهر
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/454517" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454511">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAxm2a0yz4O2OHTFQpt-WERt8vL_jU1rY5vXFDRYJS6qVX5nvTz7O7UTYGlrNYtYEQ7WL4XAHvRb6JZLdYcTKh8rVxp_HbOPfGy6WJcV7LX2QPx0s5S7ZdOw_39sa6YCyRq_Q5DhWBipoPbv82cGyqMkX5TygH-YaJWEDR3SPu5bT-nC9cQDT8ixkPz6YkPYiqAgZs37NbonMdu7Hj2MMQR7tEqaCRJCUlNHCP6H9DHb6h5a08Sdh4KyIoLKkZyuaxBk-R_SP3o3kO6QQzXSUL_dANUCeZDAKhIjqIjbrIk-VggxB6_rQSEF94bnV4RoEDs6md54dJK5Jpa63tIHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viglPJ17CPpQz3krSfBSwpi1oTuFB779kw0ZHYAllI3BvgtY8pedX-BSGoh0umlNu0OwYYkSUB3K8asX59EkEEmwruQrH-bDFzLN-vlF6Fxu1gIIptFkNw12P3M3lf5IL3D1wekbbKxSvmmulPk9Z3qpReGrHps3sihFWVF_1k6YcIgF_IZYZ0EQnpOX_sdvCiHqIlO5d5T246Fn6ito3BgJ3cW1JxuC8YBM3oOli1X62PbMDSUWJpAbub17ggtdUWYQ0S2YRt28Q0kFnBMp8o0wyZl-se6tRvW9GKNkeA37eOwlr_nYDlY-kA7IbfsHOfsiuZOG9AMZ0azRwvzotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOv2Ebr_IAET5BRr2QVbudet13OHpSB8ThxBhcwNpEZ82GQqL4pqyuAEjpR6j5prN9yN4Bn0Gm58_LEdT7IqKK9njwvZE2MUy2k1n85DUvCQx29ua7450oox6LhI_wJHDX4cdJoXY8KmLZ48XPyg73TztOn5PlDvnf8PJ3A1QllA_kIxFcIuo4syRpSll5wHpCLKoCqwr2LS17y8MHhmfvwIwMfzX50tuGytFG2-sj0QGkWgvwGodjuzXMGscEklmgFrc-WjW1YcTW3_vherW-c0MEzmCZsZevHuRx6vPI_v9ZT4fc7TFs1LWk4VnKrgEOhHSvUhKL05Wn4AlXONHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSIYkUjvZzngbCdxSIcwkd_nhiyl98mf7YQz9ebuMxAkHfDuDC0uFxOGt8k5vFPGvciXJNhsUzRKX-scQtlZXRChmbFNMR0EdNybNhcQQgKHcj00jcLYIamUipwBU9_EioSSSaihI5xqHeVhFhpQu5FG_RUm0gE54A3Lau6W0OgIL5bv5yv3uanxpum06k7EOnC24lpFKka2Bqj038c4TiOnyRJ-SRqZzZaVZ4-Kz4Fd29S-CaeYNO29qjoqeWYS9DYgf0iNoP2gQSTk3UZwvbWaSjuCvCUWEyxMR7wgPd5yZT1HXcUXVW_Jgb_KEc4PKyY9LLBv2xdxfT2CMhKx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvpwpKn-wqW5wO6GBK2BoMJaIVDuwhf29cq4KsOzoAKvwZG3YMwY17HwyaRNrESjZiVDF6oMYotsFubI2WpljHf636gnleAz0_EA2utId-5AXJIklnbdSW09ddSFoeXeP_l3GWQ9cZk9oRRz2lsXtH_D8jrY3BNV5tIvLK7EvwYtSzoLtC4d0DOB9js87Mx8AJ3Igmw1yOIU3I4XnLs53I-6Ee4usAtHQ_EHIzknPVUzPrfB-anufxCn0-UtvL-3NF_dq2YKqunFB11dCq-qwMBkv7liad7O07vlkjf_a9NFNoNe3qTHq_gtPieb5fjInbzzOL2TjQaTipQD5rC5Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff4717665.mp4?token=exYIbjrpRBrqZdVtgIweKeSajJg82VwVFNhqonurTGpSOdhfhGuzwGrJVqa5JdC5haO9U_5mj-crE_F1hIOAqlqXLnYmIaNf9RkySjwYEe2XD6agotzVe0lNGrwPUjts3vANlizg0fHrCLLuHxAk_K0YZ_rDW_2OfwUOf-B4azLPLq7zYtLqOLX6eucOBw86KXv_pygFjAL9fuvrF1MqX9-wFzJ-p3_9ajrdQyvsY7lCKj_vFeaePgRDl02axOpoAnFeo0Lgr_IMkfqLQ6CTFrRHM2qZoUTODglUPHUY3yseCNsck2pJwbRRk76uquecB55e74lPLz4mXo3NN8mbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff4717665.mp4?token=exYIbjrpRBrqZdVtgIweKeSajJg82VwVFNhqonurTGpSOdhfhGuzwGrJVqa5JdC5haO9U_5mj-crE_F1hIOAqlqXLnYmIaNf9RkySjwYEe2XD6agotzVe0lNGrwPUjts3vANlizg0fHrCLLuHxAk_K0YZ_rDW_2OfwUOf-B4azLPLq7zYtLqOLX6eucOBw86KXv_pygFjAL9fuvrF1MqX9-wFzJ-p3_9ajrdQyvsY7lCKj_vFeaePgRDl02axOpoAnFeo0Lgr_IMkfqLQ6CTFrRHM2qZoUTODglUPHUY3yseCNsck2pJwbRRk76uquecB55e74lPLz4mXo3NN8mbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انبوه پرچم‌های خون‌خواهی در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/454511" target="_blank">📅 22:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454510">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34667a08e3.mp4?token=bSlM7GRXwh4WGxywSHvGi3RDg2F_kHWwpFPhARzPGgqYKMvs4Ncv4mf3SmZH_YG8yIiNV-6rB9mPI0cb9YQ5JLJA0IFfP2nDr4tofb6QqB6Y01TxMys9L_pNbbbvx4Y6B3okOlzQ5ZVl3Yh7ZRx5pwQ6qwn_SZXJx3T9yYZ_l_66YKHGflbiSIEvhzsBVHi4276G7rRUYhPA-FF77A5imyebibCza0yXamrNI0XMAwnpYjJ5vIFxC87_o1B1J2BJD_GnOF_Cehw6ox1jFJLsFR4TB7BbaUAH0vKzBm9s3yzMzOiS0S0RaQFaApdwka2QIV0jdNuQe2w7LvYcpHUfNBnsIz_VSgfWnusqkBSXoPKK46e4clWFltDuozFkRoir97zGVPY6N_ZgrMf-4lfxsV1DrdtSXZmpcgkHcTmR7J8rKGlY5yPWVySePwMXYdryL8T3qeVQh2Gzw_1mle_BckftqsQLeeGxgs04uW0f4lNa8mm2-bmHpgmfoi08Z552KvmOOCB7ODNOabNOF4K4YUnh8NUzjTj4EK3GqDpiGHT5MoF6PKraCVPxzgeKnxa69MRlFM71-uGuQqX_2Hhw4nNP2Z24zcroHroEi1c9fOT65bZmYGxFQZ_yJ4wlQVyV4WKDy6EIyX6tmRtAnAmdnALaRKw-Fw4jJoI2F3nHhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34667a08e3.mp4?token=bSlM7GRXwh4WGxywSHvGi3RDg2F_kHWwpFPhARzPGgqYKMvs4Ncv4mf3SmZH_YG8yIiNV-6rB9mPI0cb9YQ5JLJA0IFfP2nDr4tofb6QqB6Y01TxMys9L_pNbbbvx4Y6B3okOlzQ5ZVl3Yh7ZRx5pwQ6qwn_SZXJx3T9yYZ_l_66YKHGflbiSIEvhzsBVHi4276G7rRUYhPA-FF77A5imyebibCza0yXamrNI0XMAwnpYjJ5vIFxC87_o1B1J2BJD_GnOF_Cehw6ox1jFJLsFR4TB7BbaUAH0vKzBm9s3yzMzOiS0S0RaQFaApdwka2QIV0jdNuQe2w7LvYcpHUfNBnsIz_VSgfWnusqkBSXoPKK46e4clWFltDuozFkRoir97zGVPY6N_ZgrMf-4lfxsV1DrdtSXZmpcgkHcTmR7J8rKGlY5yPWVySePwMXYdryL8T3qeVQh2Gzw_1mle_BckftqsQLeeGxgs04uW0f4lNa8mm2-bmHpgmfoi08Z552KvmOOCB7ODNOabNOF4K4YUnh8NUzjTj4EK3GqDpiGHT5MoF6PKraCVPxzgeKnxa69MRlFM71-uGuQqX_2Hhw4nNP2Z24zcroHroEi1c9fOT65bZmYGxFQZ_yJ4wlQVyV4WKDy6EIyX6tmRtAnAmdnALaRKw-Fw4jJoI2F3nHhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها از آخرین دیدار با آقای شهید می‌گویند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/454510" target="_blank">📅 21:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454509">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پرس تی‌وی: باوجود مانع‌تراشی آمریکا مذاکرات ایران و عمان در مورد کریدور تنگهٔ هرمز وارد مرحلهٔ جدیدی شده
🔹
شبکهٔ پرس تی‌وی به‌نقل از یک منبع آگاه گزارش کرد: مذاکرات ایران با عمان دربارهٔ ترتیبات آتی تنگهٔ هرمز از همان اولین روزهای بعداز آتش‌بس در ۱۹ فروردین…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/454509" target="_blank">📅 21:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454504">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCRKx7RCfIT4V7BlxN7ZTyHgJ1_YELEpW9D192D3KXiFrKFp4mplEmikTEOdZlW3fRcEcurS9cdH4WPpgx1oRIuQ4XqRLtvDpiY_od-62Ay8LJo3FPffkbBxTIDUdp_TZF-kJn3sCZj0R_0x34Z31J3GZcscxMbKoXVaYCuDkX7RsfODO3ehMR3ufLvw8y-pqk3ZnU8mtfdAg2F65hyJaTQ-9UUvgDdxRFrbf82SJ8x0A9UZn128lynBSQqBM7t4qIsZTHrj1wv9x3HaRvtJAqNlFah54Bon8jtHDnQI5_mzfDLw4fBQ5Yk1TVCdghvMdohtYd8TLSxJ0P0yjMwMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umV1OHXQj8IPyTU2QKAnNGb0sX2wUuROKbuhI_f3JDQtfX4GaGLiFs_UL6AXMrDRvLedA0U69k0J-Pi8czvhMIEiRWEZQsljFGOO6cmbzZWmyU9eycRoWoDY-22Cquc90R783ibMga_G7QpPZGk2x8VwuVRMTxX1SO4JCSDej7Td4_L_W4zc1Pfu2o2uG9vcE4Bt7Ucd4MMlJFnaCcu0FW1-6qL-xC2UbwfjN_xG-Ueb2JTHbhioCTfo2cNB_VfRhVSIlOwCryD4aFb7HNZSzsNs-RqDZWj_5D7CXiIVpEGbaZ_EHOAIc7UNLGfluEoVqkzJMzn6i0fWS2XM5oYVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYCUx_5GV2ZCNAmfU0DnJaSn-cVDhBP8lm7tCJewubPpVblwSLXvfuMmOD9Fk4UKn8o-fOX0KGwCAqzchk_iw-MBCEt_cWhFCs4nTXvk6uwgkmaDHv74r79fRUUBbMD2ACZ0glAJS62omNBpmTU0qqkSlDbKhinso34qKmXgfVcfwevlHijdlIdBgDs87Ck8pKSXNEblPF6h0OHZSsMhCmy3EvZCLW7toLXqS5NwkxLvue0YKUYLCkX5_r_OMeryAM8IxVa4610WWN0ZpiDAdU-iVTkziqUxhtYlFogMchFYCbnW9XrGamugxbgMU9sJuwu3M-MQll0uiJrSLsPpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmE4B7UnKLDfv_sJhA9GH2oT_ZeQ-WgnlhXfOP9PmrFUYzmpv-W_e-EXPAQTpFNuz5vYLS3pWMHzbjY2WkRdcp-fF5113YRYQO7_1-Lhc9jQHrZNX_qbCXHam-nSgvZrtoRC6rBOE8C-Sp5UxEqq3eKc8ajq-TjmKGkd-GJrL9YAjaxht-CRRmyfpfZpNskoz6tI8f8zgF0e0uNuOaHYJAeaYxgLWE5mcYVYjIRr2rXuJh0tsSt3J34LDCnbvL5IC8tcos_rzC8T6So1Z3D7L11-1DETK7Y3wtjfJVYb0-SNjU2OrPebDC8DgC6gBuAS1NMesRF4w8blyQiChUIYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYCyZcZcsdMcityZ2B-dgN5j_XyFP92TmZamaiZjQguI8GoSSOR719sm5ProMglWVBLwYuDq4NK3QjwpdchEy0uzMyKSOV7Ht1AEZ_-gjLlt4DelbmXy4IzMU_cqNjtuS1jwx8H2M1obImRIKYn1VYzelPfZfMUyDfDtWaPdg1xuWLl-iw2Z3CTp3gyoLXWoERHKw3xCWB6VNWi1SUW_BvWcfkGb9ZMeokYuQf6fVjvCHvTrdAXfTa0UVuM-e4beut7MsyCkwZ-ENPxKPosZoUwtEwo_L2kaVDwbg6L0gZUMbrvju4htL0LbHiKRJh7_F8LTHd_B-07CVnC-i_tAWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قیام خون‌خواهی مردم یزد در اربعین
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/454504" target="_blank">📅 21:18 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
