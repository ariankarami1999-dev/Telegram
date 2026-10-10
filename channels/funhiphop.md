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
<img src="https://cdn4.telesco.pe/file/ImXOoy79bOdOpAhF1nTXZMOTZXc_aitYHg8fqFdznL61eilCyYsGEESDXRpbook16VDm5dI_OPKCik5olOWkFTSiUtF0yzxDi4T84WHMWo4qRn65h0lhnuguR3i2seyBcE2UJYNSHZYRRtJ2dAFsGlSx07JK5Wd4fzoi_IovvRBRzf8OpysV36MsEadMUzpglZde3TDlkLnF3aizPEGAedb31320BmzpIuU35Dl0jE2yQDeUX5K_nPjZNI9dbPS3x_85ftF5ynwBP8L1Ht-DFVuwtKbm_M5vq6_n2oFSpwRGKzco3b5o_mdHF1Wz5EZyy2eD5XIYIhBhuQ0eg5bcVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 266K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-84660">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاش آرتا و هیچکس یه فیت بدن، هم فنای آرتا کف و خون قاطی میکنن صدای اگزوز خاوری هیچکسو بشنون هم فنای هیچکس کصخلشون در میره صدای اوب دار آرتا رو گوش بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/funhiphop/84660" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7MMwzQz9udyJNao2ZKFoPKd8UhBpEmlRHSxRvSRMU5zAVquc79OPE3iGoNYBPJAdsP-fgZpxEglvw_8GwMyPOA9fEnfyJYuarU8p4N8IjvDzbvvcDe5cugD3yNaGe-bpLOy5s6HdgXbIgDd6H9OOK0r88IyZIHDrMXM67XS2GszcDJ2A_0a_38STYfw45_0wMuSHsmOrr30pkuMto0gfmGM4YVvxPV8gSGxAkiK-WOco5ANg3e6xvw7oJ2S2ndV_nO1pLpo7ZpQsVmZFKvxKrRsVmAvuXo2yamvYqqY_5AN182WhEO2e9mqYiGF-ZZpe3i33eA0J9cmCRyZi3zhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-6voDmu0wQ3OTFTCE-GuWa14_9VLkRAIvMZk0LwXYfLx20SuUoM2BX0OQ3bF4j623tftSphVITssQXI86YQNnsvf-EIn-NglSiSNUpEHhoiDmBDWJP4bpr2DgJmEwEwD0lCF5fcH8q4Z8hgVOWvnQUoq0BWHUeGh8tg7nhAyIjMl9KNAkqumFx5ugWnh-7BwiUg38mVogf1wEKJ9efnT6UHZv_xOSlLimDMeKgwNBXrXUjw2x4jf4Bf299aD3T9BiuBN9rGwY43aBDS9uAGoGMpznQWz5_YS1TVkP3fjDfJV371Q_6_Mav0sZsdij89DSzBpjxKtndeJqq4W8UxWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوتیدا، ملکه تایلند برای نخستین بار پرواز انفرادی خود را با هدایت یک جنگنده گریپن در استان سورات تانی در جنوب این کشور با موفقیت انجام داد.
وی همچنین خلبان بوئینگ 737  هم می باشد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/funhiphop/84658" target="_blank">📅 13:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حصین جان جوس ورد از اون دنیا هنوز داره آلبوم میده، این یاد کیریو بده کونکش پیر شدیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/84657" target="_blank">📅 12:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در این دوره از تاریخ که ما شاهد امپراتوری آمریکا در دنیا هستیم و دیگه بریتانیای کبیر و شوروی سابقی وجود نداره، هنوز عده ای وجود دارن که کلش آف کلنز بازی میکنن، منم جزو اون عده ام، کسی کلن فعال داره؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/84656" target="_blank">📅 11:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ:
ما گرینلند رو با قیمت مناسب به دست آوردیم: صفر دلار!
کصکش املاکی
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/84655" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFx19AZBOlm_WdDjZ-dG1tga-F2gdCEc0yQQGJf_8gEhe2bPplxZ6RmPFJ__tkpNd_8BqgLCHFKXnvw1xDlFv999nE5oDN1-cTLm8Xe6OOGUlBLkQebGqSblT1rTo0up1y9JcOpM9sv7l-D6yeyLimMGxcE5f4GZG76mE-HOMtZoPql-3Fd4BiZ4Wtkda3wZLN6zJD9TrZ49GP7Fu1xh6BoRYExKsgrlRTZY_0jE_PtLhh98w-qucQRQlt4n0fv3VKPALmaGFy6C4I4FlS_cykcsOzYIrMOIgFXiex0dzAQ-2OFwoT-CdnNpCTQU4XQIqBE0so8rW8N0jLhzfu73_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میدونم تا مدت ها قراره اکسپلورم با این تصاویر گاییده شه، فقط بگید چقدر طول میکشه، میخوام بدونم تا کی اینستارو باز نکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/84654" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/84653" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4xHSNqQ1N5kHmEESexJLSaN7nXq7ok4888l9CWzXic1V_9G1vT4DZiDaV9NIrFjh5K3L1nJxoXM1YVOcfhqfUA5He144cbD4g6h6SNYr1iU6IHu93t94l9Lkj6513IuBPnQOI9vqAfJAglRpCP9-RavvdNKtejG-UfJilZow9q6RO0YoaoKQYe_Qmv4o_osW_xxk5yf43lNBIVSFZPxg1gfL6qfnbl_SMv8qrscqw20N7xW7gXs8QOJAf94khdCAGatF6sVsNfNRoIy82mTDcmqgeErnLYNpLNoOede3llnkas9ZdvENDU64CLuGxCosyhDUUh7ITedydYrjTjWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
چلسی  - بورنموث
🌎
ساعت ۱۷:۳۰
⚽️
منچستر یونایتد  - تاتنهام
🌎
ساعت ۲۰:۰۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r18
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/84652" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=EOVWF3xXB5PCQeODaxXpfSPtogcu4FmhzNwR8IBGWmhi43qUzOoVtoz2YmoiACbW57rMONxlswEPhwiGklh45Mj26pZGQ85NQMdAOUsH3AsrWg-8DhpcrSMCDL-6aL0WMiLGVBa5JCXKwBQn8n_T70zZoiNATT0LaXR9lG3YppqEMbYziOP4f6MRl3d01YLG_hVVWWN4CEfXMm6aDdvAMLrTUnMB63Q096ZtwtfHqqqNabRIs3DG6Rf2iGZ_tgF9Nt0jGhExNXwLDujBLoCKnwPxgbv44GtGsa6zi5JZNL2RBWRwaC-7kOH0mggAPGglF2jEy6p8fOhn7kTQMS5fSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=EOVWF3xXB5PCQeODaxXpfSPtogcu4FmhzNwR8IBGWmhi43qUzOoVtoz2YmoiACbW57rMONxlswEPhwiGklh45Mj26pZGQ85NQMdAOUsH3AsrWg-8DhpcrSMCDL-6aL0WMiLGVBa5JCXKwBQn8n_T70zZoiNATT0LaXR9lG3YppqEMbYziOP4f6MRl3d01YLG_hVVWWN4CEfXMm6aDdvAMLrTUnMB63Q096ZtwtfHqqqNabRIs3DG6Rf2iGZ_tgF9Nt0jGhExNXwLDujBLoCKnwPxgbv44GtGsa6zi5JZNL2RBWRwaC-7kOH0mggAPGglF2jEy6p8fOhn7kTQMS5fSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوکیلی ۵ سال پیش به یکی میگفتی پیشرو و هیچکس رو قراره یه روز کنار تهی و ۰۲۱کید و آرتا تو یه کنسرت ببینی فکر میکرد مواد زدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84651" target="_blank">📅 09:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258be0442c.mp4?token=a64pIb-17nEt954KNNdzgt9din8p6DBcXmTY8tNwodIFAOR1OcQ1JbM3II-XZdkidjFXZkTfW7JjZNWrqUYWDE8vRSt3wptL-usQuqKl64KV8-3AoXkyDv1a_QirNx3y1RUXPFQ_QLiN0n5v9tzvmBHtzRpPrwMaH7rgBZS6mYtgYHkDndiAFbWmMU1epA8KH0nKi8yahhYzaxuT4uD1PGcehGuPreUbTscDijax9IQMh8C8nGFnC4T8qu_OvlhjOtR4DRG-5rUgxJYXhRUv5xUHDLA78BXuXXa1NMpJsv758z8Yb8jKCxUg8RDgYyJSmbkTJFOXIhsmBjdjO7wlEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258be0442c.mp4?token=a64pIb-17nEt954KNNdzgt9din8p6DBcXmTY8tNwodIFAOR1OcQ1JbM3II-XZdkidjFXZkTfW7JjZNWrqUYWDE8vRSt3wptL-usQuqKl64KV8-3AoXkyDv1a_QirNx3y1RUXPFQ_QLiN0n5v9tzvmBHtzRpPrwMaH7rgBZS6mYtgYHkDndiAFbWmMU1epA8KH0nKi8yahhYzaxuT4uD1PGcehGuPreUbTscDijax9IQMh8C8nGFnC4T8qu_OvlhjOtR4DRG-5rUgxJYXhRUv5xUHDLA78BXuXXa1NMpJsv758z8Yb8jKCxUg8RDgYyJSmbkTJFOXIhsmBjdjO7wlEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد جنگ ایران:
آنها یا همه چیز را به ما خواهند داد، یا دیگر وجود نخواهند داشت، آنها این را می‌دانند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84650" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تو تنگه بزن بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84649" target="_blank">📅 01:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84648">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اوه اوه
روسیه تا ۷ اوریل سال ۲۰۲۷ توسط امریکا معافیت تحریمی گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84648" target="_blank">📅 00:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7Z35vIP7RrZQXdtDNELk5LYO7kxqZl4S-o75h-UEl9_2czt3_gC4n5ANNLjXDj0550ONFvSpQz54tgqZG3id0-ePque1GtBPmyrDt251T2LisPhmRX0W9crmnAXaT31LpC1zEJivKJ3eQCOnhHJGt574iTtc6amNGF3b7nsMa4el-qZCZ7Jwi2gcNdeMZSVvk-vf5vka7h0cwbciUWlMo_MJ3b7RRlZJ3c5AgVZ0U2ASm60I2HTuWxERNt1zPwAbZb2D96ck-uydXjCbI_zjcaLJLelrDYC1ocJeuaMkZz9UG5zY7CFTmRGNLY8iz29jXUAKSVb2si28AUjuzC_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی داره یکی بهشون اضافه میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84647" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5dODRyPhcBUkUVffPG_n_hArCHDNJQ10QlKd4p-AbFU0m0e5fYuk18rTtbdhwtNp0A-KL3vtIdmF_N3A4IVC5imn8yunLQF6czKPRpgU_4jh8L_Huj5fWo_scmCGyOm2XMxB5fQ8GGyxsrVOiUwATZqCkevNX_uamJ6yoa78JoiOcLvC87_Ay3hgf5PJYFvCK0jIEEKZ-dp4daTYMc0LV3rMbT3FsgLDvzAPYfthurtgwH6xvMPoq_NYH4J9b6QfevJTMhKEZRPCjWJW_aMgBbgD5CzPtuqBjNCiEkF4yDuEMmt6AGPYxtV3shiK47jlWYwB2AaSvZ4sMhdvalbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان فعلا پست ندارم اینو داشته باشید تا بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84646" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JVrlyuvhbiQccnH0ae1oew3pPBNR9nBYMTAhTyncAeUAjJ50CZmmw3nfL7TpFs8a2amaNo3oqX3Q8unNwo0RSuLjADmWvhIjmN4JYeT44V2exouCvqpfQdPsmgPDRU7FJiGVIficdAiKwhD1t9jjeDPewGA1KjinzZL1IM9CumobPQQbmQrCEZRwkWo7yk80MJQqxCQmrURcS4PXu8zEGXbdGofN722QVgWnCrVPa1BcgSu44ritxIcUg-1qjVt2bp-8If9V3Gxlc2Me83i8qEkKY1hnRbQFLGxa2xTUL9Z4N4vOKX-vb_BN4HW1iKSEQw6a2-k9LXQYgLdU-hxiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FE5V5DkGjB-HIh-kipLYEbvHPnfq-bYsTg84IGj7NdpgoawR0ZlJUnMIEqPpaOkUPPs94DYt46WPlto-YwHa_Ne1fBNIerfV9kj-xL_1zZAUCQuDRPXcuq9iFYu5hgZ55YrQ6dfaPrFCHWNbDFaMw-Euy4H8tqrOPzlyqxJeY_cO8YKZ8VicU6HPgsgVdhmgdMbmxmFSKDjqJbBNWZL8DViAMc5ZmjgJb2atrWA5WbGarc8VbTwMOPSCYg-Ai-h5QwN5zv-F-4myHN9N74Zh3oj_3vSH7tv4KDbHMT7X-OYSU6D-RvPVaPIKGEbK6rUEZKas1Dq4ZYsuGSizvVIKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NF3AUX6UBT9wDzDReIS525A6bULNS2h3qXT4C_WDBEye1AprfGux1oASwwU8fD78xNb12LPkXrGvSqZlchX0AXtG6VOBo0skfLQQKPyW30dEvbQ_zhbjfKGH-H246lvNqXWDymCofVOUruEhnMIrSWBiM6bxURINS7a28htRHdGRXFjYsKpNRwsotb9iK9CRSxZC7CblrR7sS2hiszdzZmn1SSss5p_iGLELr_UALMsllPT6VI6IHQCImOgbfGFLRraJpnbpm3cOmXtflm8y3d1R0hrJ0iwgMjYpahJFQS57TeKHFQRS5pwfpYKCq3fIpQwW9aP_VjMnENTDKe3Iew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t6fulLaETbDhpeK81yNdI-Fa39ZC8MJ8A7pHcI__hcMGAxuuy5PFZiC7IWHV6YjsPrjbhp3KI94APmECK1SjQAkPGyab-eb0QW9ZM1Q_yAzA0hsUuAiXs1Ur2y7VeIprNx8Cnl8diDKZENoRha4y1vbeWsYA4NF-Atk4R5Jm-S38fl-ZUiSDn5X5Zc9Vwy43Bvo11zccTx0u_c3JbkWAXuhT_qBc-dIs02I2MSHgfIl6HAYuPSkaUcdtmCCHX1TnRrqA-FDY6lIUYqN36UkQXceeu2rhl-URLFKDC7eNRoldYE2XlZ_KWSuEGJPxuT-6lCVKx2ZgnhcU6Gx_mCK5hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با ماه کامل بر فراز آرامگاه کوروش بزرگ، این اثر هنری زیبا خلق شد:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84642" target="_blank">📅 20:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnvvXvniejU55dJr0hOhUqoIM5dXGaMsJQ1GUOYe1MZOt8SFWusYYCozw4o9Q_aFOB7o-5eB2wAB85BT6cMwMyQ04GUHv5bIC9Htlbdo5SfcdyDRdIl7Gen3xGgsSzQWcxDuWY5V8h87AHxQtDLUVPxHfkGEiF8Slbn6SeI5crCqv8R5NQfyIeFGhkuVnMUSMYHC5DrxgxXyfDrM2nIUjHCgsoRKLnfaj2vH7zhIEYZZQi35QI9ZGiDzQ2WbSBD64_fH11D6WIZdEKZIFOGzZf9D9CbCSmwSh8XG7Ooi09f2RDiIGrWdT4sCOc11DAN0iGdjtSccAXYUIISdo1r6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چجوری مصرفمون از خود افغانستان بالا تره؟
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84641" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6QNah4nqy5So1zuwx0EgSTixFrB3sGlfL630ZN1I__bh91xApSg_XOGEr_Van2710YQuZ20B7QmWtLjZjXmrjF1EwubrOLwhyzUhTH4AjSSwXEAbVXIi0_CTwNRvKfaASSyn45pIlkMXfEL8HRLIPfUYXflgMy12dQsKjehk0a8tJWy7Sl86NXS79_VCCanapnTzCwymnld2iuH6fxpSXfd5pPpTCvCX-D_moe7_sN0L-UNVmK13COOBRIPIvjfWxIinfgAeYXOQ4nwKBaQTWrL594Lu0hkfHgkwYdyjs3NBxdvpky6R95tiU8HAomfP0pxEoKwzD7VqXOoNhQE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G17
🅰
🛒
ورود به سایت
👇
✅
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84640" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84639">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX9l-lJTjfsi1khJgNTl1Nvku8jyux5mSiHYPphYmnC-7raIB3YA_xpFElFkft_lc8Ld3wPqA4LEn85jbG_9USV2XGkZ7ugZESrwiVe1lXVDww8--w2g0PYQc6wpP9PUz9iVtZWNL5-s1cPD0vKL_9sbp5XJTNzzftJgg4iIehXBc-wgCyHFIwVqNg93Z2L9pt59wFElLZ66URnHK1anfR70sOMKHZXsrpA-zASyCAkeSMI0fA9hdopFYHeJ9M0h20NEjQpqkTrT_TnmlHr2kfBC8S_bDmm8BHC_n-Ly__Q-3EvRgzbAt5-ktIFpQe45HRba6fBGEZGzpC4XGXJfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا خودت رحم کن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84639" target="_blank">📅 19:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84638">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uShaL4IYApvlk0cafGUKA-F01svTLMla2WAs8-Ym7IqvFk8DJG2yzpRxLvL6BOG-JXoKER3GoO4BYWjs45KN8Nb4AAEmpkvixZTNWH8PdtdsfhyOLKvUczPY7Kx2cijvJzZIDy9QG5beenju82I_CKDl3iNAhYfIPle7e2AV5f8Sy7XK9J7fDbZ5_FsdttUo8cGCINsUF0pWMH7Rd61dAfiNXWKLFl3560BfRZg3bn6y-al-lBYXMVC8fjOzwbbfy8Wws9BlYtd52-fmkB24lSPCdIlrpC41VE7wxWisDe98GNjqMf_yE46CMu9rbNHl5u2ReR3_22CFl6PevkOl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین چیزی که امروز دیدم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84638" target="_blank">📅 19:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84637" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خدابنده‌لو چقد شبیه رودری بازی میکنه</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84636" target="_blank">📅 17:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش‌های اولیه از کشته‌شدن معاون اجتماعی انتظامی استان در پی انفجار مین کنار جاده‌ای علیه خودروی نیروهای انتظامی در منطقه چشمه‌زیارت زاهدان حکایت دارد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84635" target="_blank">📅 16:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">میرسلیم، عضو مجمع تشخیص مصلحت نظام : تیبا در سطح ماشینای معروف خارجیه و به راحتی می‌تونه باهاشون رقابت کنه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84634" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84633" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84632" target="_blank">📅 14:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqZArGC5OdIB72zaFI1W8TNPYUngy-b_amVm2qD6Ild4s63K_zs-i0GuTexccyw--PO7IMNMDO-GttVPtI1VydMcnx3xZtH0Ne2JwK1PIdRNec8fShESQTV0miLUGcXEpbp1pJd_DjzoxL1uZLOtQkF6D1DydH_GDaVltafb0Ho9I3_pZ229TRLRviFWMvUzL47yMvR2M5Ci8Bu0vZPlHMwQDOYiu-hghKm2JnimszzL1Q6FXQ84Fkh0lvGmsXBo4o6tY2x8xAHILjWGku0xBc4-zmZ_eVaoeyiSoBWtc09qpyDpiIz2t2bZnS-nnB_7gwSYNF-ea8ChGVqiyyJPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا حاج اقا
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84631" target="_blank">📅 13:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84630" target="_blank">📅 12:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84629" target="_blank">📅 12:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84628" target="_blank">📅 12:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴀᴍɪɴ.</strong></div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84627" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZB5rm630WFQ2nxuPnyU7K7Y89Ptrq7ABLojpY63x_oBZm1p1nINYuF0A9Y7c0u9_AofRJDOA-VWgfF38sIhBc31QeALqVUNFKwizyVFiaaLLxtD_fTR8xI8-M3CFprZZEHEWq0AX8mn9Qbs8X3WzjQ8NlhCufdYCdFk-igTSPwTW_otIlboPsRKYpmTESW8Leoxu7V01wC4aMzL5DajtEuBGGBey_mNQiLyPMvdfSGmvPG4QTLE3KNDqBD5OHq4aICaxBkeBW1uEmEmID9NJ1-oTuAxMiIheKw55jIGrlCXYVlBzVLpqI1ueU7wLYB5w4AXmpb8Xx01jWDp4eCQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا فک کن فیت بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84626" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هالند و امباپه تعویض بشن بین سیتی و رئال جفتشون بهترین تیمای جهان میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84625" target="_blank">📅 11:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlTAwicdLVmEANjQe4I5oBc0fGoz13NNs1ES2UElIlH3cXjuzBEjT5ePGjOeRKyocf8_zIDR2W_VVkkVGJuCuZjcQ_kpDyVvGuOSvlVECQBy4uaKssweaHBZisSv86Iyb6LbTKCFTWoVwDeW33WunSokSYdF2x4ECEiAojdt3f2BltxIykpoVA-KiKb0kHoVhKWrZhb40e4lU0nVlOOSbTo3xfMJgqtkNeaeX41T0hYjD-9PW-5VsJlKvxQD0X2txB6PCDXxZgwYF0dQKKmz8VNDLuBUBDJ6yBpU3lxRH9nRWQ0Hjt2yev_xTjYsDYssHOXT3kYSHh-n3sOuu6HBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV52Yts5KOg705MB6r6lbIrQuWkO1r-BmXx2Z9wiCiJPahITEtltHVnLxLFxmtwPUyivsEhnEyB4dTzqNf4Ra_LRRQaR4bACxb2uzviFiq_EgBlTzTKl6Q-6AHWS_OboVTca4HOb9y-nTPKrQkSbzgnJvsSphuI8gQqCX3E8OKSLIbojgdiTMsCmDTXFRzTkbB3udfzi85TuVcd6Xi-DLQNrwuE5Z7VrAxU86T-5ZVjlyT7_WXj_v_njZU59qsf7Z5HdzJ528iBDmuDQAedODVzV9O56U0vUozPUNe3NPt3eh0i9lmxeNEWHKyKEEOKaQXnfOfVtX0WCEL3zjRV6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boqwOFzm1aDuveBVsZgZmE0oIYSoRhV7x0NAJbF6-yg97SZNmBfRNUcmNGENl_8KASpCJY58-FbNmPKKAcCgaj0q-oBJRRsWo9CJ1BcVn1wcAwTPOqaexd03MmHWV8e4BuvTpOgJJC2evAlcVifBC7PO-YFXhCxtoKqr_VsmVwINXyyAL2-VIZuKw9EX6ZdreIsrqG0TDEzOjlKa5PsPvkQ8qFhGZMTMj4nmGsoPOUy86mtRvwhv5BekMwf5KXS8WK9QGCEuNfayIHOTeV21_vWonqK5NAyu6ZCMTzhUY42ykzNf1AOQ6AH1B3queMAXEWy0FzyyhJcyTOLyjgdxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی کیر تو روزی که با این تصویر شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84619" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84618" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5GbIrwM2hQFingIK9YFabpww3kEFthYfsc1rdEu_Yf1kKsKkIgTsnQoPWJcBPq9dI8_YvuMGg_nZi7vmEvjyu9LuqGJE5nQas74T3X6OQmsxN_tiYUA1mvEklGE2WW_cSasNYeUvrydM6-hjgqzoLfyhgR4cGvNxWXn3ojoLl0RkX9UEUH2lnQWrKWhfC5p1N9Ke49QPX8LnvbQ8pU9ZB_tNM2kYogLjHfKYFKBgmpfknue-0I23S8ufYC1cDn29T6S2ZX59qbmMCLkIu-VRXsz3sagMJduQ4xteEQz97MR6aLrXnYdZAOyEH_tnV4CIn9jZM1kLNknX-8lpKhnFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
پرسپولیس - صنعت نفت ابادان
🌎
ساعت 17:00
⚽️
چادرملو اردکان  - خیبر خرم‌آباد
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r17
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84617" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=FdYz7t15yic_APbLHHe5JVifAhz0mad1ud9oL0AYToXK0SyGtWfRrIfWKEXu6rj0XW1nhyhSmjcK0Pv5zoYMtqLxqdEZbARC1QJT78sLFjIUQSmvW2gWh3pwRv7TgFv29qHIMF2rg34ryEKZuX5TuR6DZf3DPZg_5XREqmAcemv1_oAvLYDP4Fpt_8FWX1RuX4dOtCMGSqeKGm2KjC_KrVWeO-ma3MVP34rIY-tyoLVUPNU16EjylE-lE1pAzlgkqtJKSiJp-NcyVMyjJAWHAFzLHksfnbAoSHMt9-H9bImnXuWUwQ4f1ImFCunnYEwi7TUF-yb7Hz0cSgFaVq-16g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=FdYz7t15yic_APbLHHe5JVifAhz0mad1ud9oL0AYToXK0SyGtWfRrIfWKEXu6rj0XW1nhyhSmjcK0Pv5zoYMtqLxqdEZbARC1QJT78sLFjIUQSmvW2gWh3pwRv7TgFv29qHIMF2rg34ryEKZuX5TuR6DZf3DPZg_5XREqmAcemv1_oAvLYDP4Fpt_8FWX1RuX4dOtCMGSqeKGm2KjC_KrVWeO-ma3MVP34rIY-tyoLVUPNU16EjylE-lE1pAzlgkqtJKSiJp-NcyVMyjJAWHAFzLHksfnbAoSHMt9-H9bImnXuWUwQ4f1ImFCunnYEwi7TUF-yb7Hz0cSgFaVq-16g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و تهی رفتن لندن که سروش هیچکس رو از نزدیک زیارت کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84616" target="_blank">📅 02:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84615">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZFsORSX1czS3DcwW5hZRseo_1mNuzjvplkaEfj-vFAFlPgKJv4Cbt6BUI_tdOCueLOMLbguoQK51kdsA9m0qrwXBxdcBdHMOK5O9IuAJoWtmUgazCm01z5GyUxp9Pi85z7Dx8QIKO-voyp24nFJsYum6cgbCyaV6pT01_x39men5P1l7TdtzeKHIDf2ChoPSEIj5-o4kvbIq1PLgY6CHcItYBjlkkD54bkw5yL7Ecc7qfFzci3VjRimFk70dbY6WU886AjQ8b4OPQuvgTDNmixnqkiYSQEsu8GsypX6aKY113gNI8jV4BNFJMbf1U-lZcROiryojQLghpfahFV8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز شیوع طاعون تایید نشده؛ تو ایران شروع کردن ماسکش رو میفروشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84615" target="_blank">📅 00:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84614">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سپاه به اربیل عراق حمله کرد، احتمالا هدف مقر کرد ها بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84614" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/84613" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=UOCwvvGnVqpvDHJuymYs8A2aaWLTzwo-zWl2bPWbrJ-KO6zIsff9CKcmblXUy7ruaj3q52DUybUp-ChuNmK4tqPfZFRDRBKX6Y4BLq3nbSLhJGS8vKPoVfAhumXT-waQ8SHKw4LZHGND94YoFz8uQmxrIjmYq0HI-CvouXMZGArQLG5sdv7LXrEECOXAvMqrb3Pe_4Yu_Dbmw82h6tfI6wdZKKj8smGLVpYLzdp81aV31ax4uGlKCJELrK_udAGGuHLEhjkFBltTEGB_7qPjBkzsaRZBJTg8M9OxPs2MYZJzDPBS0QinGWlFfPwP_848_8sys2CKsFlvdN35rt9P2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=UOCwvvGnVqpvDHJuymYs8A2aaWLTzwo-zWl2bPWbrJ-KO6zIsff9CKcmblXUy7ruaj3q52DUybUp-ChuNmK4tqPfZFRDRBKX6Y4BLq3nbSLhJGS8vKPoVfAhumXT-waQ8SHKw4LZHGND94YoFz8uQmxrIjmYq0HI-CvouXMZGArQLG5sdv7LXrEECOXAvMqrb3Pe_4Yu_Dbmw82h6tfI6wdZKKj8smGLVpYLzdp81aV31ax4uGlKCJELrK_udAGGuHLEhjkFBltTEGB_7qPjBkzsaRZBJTg8M9OxPs2MYZJzDPBS0QinGWlFfPwP_848_8sys2CKsFlvdN35rt9P2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوجی انانوبی بازیکن بسکتبال+۲۱۰ سانتی نیویورک نیکس رفته دایرکت یه دختر ۱۲۰ سانتی و میگه بیا ببرمت نیویورک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84612" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=uKVmqLGMMw1EibTTgvfDuPEJMb8Oh7TI17V05zIClVzukVCBgetXCLgdR0HjZ978KdhFUSXlvaFD5VVHK9ZGh4Fu4fQUTUYEUaSExgR_pyZlss2tdk9NvSEzvX6eP4bsjlJXT5GTtOvHFG7qhOqr_SW_Ys-yMr9oGJVqG-8GTCmEdQtsL7SRZfrNToy7mFvvvINEEnzhxRycL8yUjaX8l6UB3_KitJmSqf1B72osarBifBemBVeRqw7kQ7PQWM7Y1zf3ydXy5KfUm6KUVgexHLRI5qVyzVb64_YoRnWr_4yCr5UvSZ9UzqRZaVh5ddamf5C5HARJ5ilVD3Ye4BOhgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=uKVmqLGMMw1EibTTgvfDuPEJMb8Oh7TI17V05zIClVzukVCBgetXCLgdR0HjZ978KdhFUSXlvaFD5VVHK9ZGh4Fu4fQUTUYEUaSExgR_pyZlss2tdk9NvSEzvX6eP4bsjlJXT5GTtOvHFG7qhOqr_SW_Ys-yMr9oGJVqG-8GTCmEdQtsL7SRZfrNToy7mFvvvINEEnzhxRycL8yUjaX8l6UB3_KitJmSqf1B72osarBifBemBVeRqw7kQ7PQWM7Y1zf3ydXy5KfUm6KUVgexHLRI5qVyzVb64_YoRnWr_4yCr5UvSZ9UzqRZaVh5ddamf5C5HARJ5ilVD3Ye4BOhgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت غذا تو یکی از فست فودی های کشور:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84611" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=M_bxcnXb1jEqrG3U9VEvrdubGLeyIDZqK-cuE8unvSzxvbb3f-Nhfndx52rRC_uaQtUQKQBGF6LKqHE4xCKo8sAf0rncV6iHbpnKZkVfK7OB1tHGmpF_VV9VCo7GYuIlfarj6ZtqiAXo01mQ9WII8IU1iGIh6KncOOF23Ca0cp3jGXRj3Adw7V5DZ1X9lChP2PoJzlFPuxyplkZGjoo3-J7h9PzQcoLcHRZwlP298FFUXECP6jmzezzMg4t-QOO290yON00F0ruG87JtKZ8ZrjsOILSULwWDE53XtcmBtOE7m5yCokizGhD5gP0-EZhLwyDZb2FxcxxpZDEtMq6ekA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=M_bxcnXb1jEqrG3U9VEvrdubGLeyIDZqK-cuE8unvSzxvbb3f-Nhfndx52rRC_uaQtUQKQBGF6LKqHE4xCKo8sAf0rncV6iHbpnKZkVfK7OB1tHGmpF_VV9VCo7GYuIlfarj6ZtqiAXo01mQ9WII8IU1iGIh6KncOOF23Ca0cp3jGXRj3Adw7V5DZ1X9lChP2PoJzlFPuxyplkZGjoo3-J7h9PzQcoLcHRZwlP298FFUXECP6jmzezzMg4t-QOO290yON00F0ruG87JtKZ8ZrjsOILSULwWDE53XtcmBtOE7m5yCokizGhD5gP0-EZhLwyDZb2FxcxxpZDEtMq6ekA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچ کاری به این که رئیس بانک مرکزی ایران به وزیر خزانه داری آمریکا سه روز وقت میده و این که دقیقا برای چی وقت میده ندارم.
ولی چرا میگه ۳ روز بعد با دست ۴ نشون میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84610" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=MZrLwGA54aowFmIZ18EqKNSFPpAfcV1QId7XAixhoT52jbmMH_UIhs8yElSzCNsamndHSAZ0d-XojzmTaLA3hU3jd01NJudqTaikFPqXZ4qXguEAWD77sd3i1idDTL9Cj5MLFD2kNrd7au5DzzJssjyTbJ1Iq7CfQfIm2ABl5iNwvdycVnWw_dMz6d5x-hm7pnezGI2oRBbyvbo-P-A2rAAJZDjS_TTLCcPjzK4jQTK6zhqSvy-HmCHfiupkpFyqsWgVjXt_-6XC9jlO9XpiHTo00nG0xqVvqSrFq4mUyZbQpkHBa3cA5TIndN1Zwcx9mwgh7y4j3F-G5ft9dOI_tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=MZrLwGA54aowFmIZ18EqKNSFPpAfcV1QId7XAixhoT52jbmMH_UIhs8yElSzCNsamndHSAZ0d-XojzmTaLA3hU3jd01NJudqTaikFPqXZ4qXguEAWD77sd3i1idDTL9Cj5MLFD2kNrd7au5DzzJssjyTbJ1Iq7CfQfIm2ABl5iNwvdycVnWw_dMz6d5x-hm7pnezGI2oRBbyvbo-P-A2rAAJZDjS_TTLCcPjzK4jQTK6zhqSvy-HmCHfiupkpFyqsWgVjXt_-6XC9jlO9XpiHTo00nG0xqVvqSrFq4mUyZbQpkHBa3cA5TIndN1Zwcx9mwgh7y4j3F-G5ft9dOI_tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد.
از این به بعد در سراسر کشور، با خانم‌های بی‌حجاب برخورد و براشون جرم ثبت میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84609" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMf_GAGOjmTbKIU3BMdyOQez3ywBRr_B5s6YnWDCT3_UcQeVynyuuI9uTp-UaS0atcSnQpZZATbhV-mDSjYu8NTLC5UbIlVJseZK7QNSz3kFJmHXulJyiSWixXP2riTTmWrigtQPjYLpY3pDZdIjrRZ0rhA47ckxsoLFKJyhZ_5GviociQ90Efqkv210koIC3-OSwBO2NHaeQSVzqr3fs-O1q64AYmq0Ow6uukouPZrz56v3r-w6DWsiju2AtLi3R3f4FiWfmnfW_zLjLWwjAGJtUTHuHMlq_MmVu3uqppIpSJWkhk0S6Ee-8ASalFl8hqUggq9aFgqAD7c6JHqllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پاشید یه جوری شیشه‌هاتون رو چسب بزنید که ذخایر چسب کشور تموم شه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84607" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJrGkHxt1Sf-zV2IdgOdDhZzsJxpsYktLhYXSEBqMGmK5boRWtFfQEkIDCuMiVEIR9UirIM23VV1dRr28l2ZhTfUKqot-DQzmdmPhyjH--qEok6qDT3FmjLLhieK6y5jl33A2MBClRZcPmMf_P5Vh70SzbPqeaYY3OquKh2RY2GoURXokjffzYirpxNRoMOtiOpWKJUksX9HssgTSmiGP4COupRccUufAzMiJ31PyoFkiirCP360I7fXffnZzFkKePgRk0xxyL595ev8eVOmV863ZK1LMTrBe4-fde1-slivLzIG24mOKMaOuI9T06A3bl-RGjrk5N3lKwEKIV4YIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlyiNdfja17lQy4AKGLXcKTHNTRZvMZFbRudLjA8XD-gadlpF8k3JmaJPpAJm2ze07bvj5rUQRaJIcYdIpEaOWt1AtONg8_6rAeqtBzBMv1OfcUO2zqCJPu_4cs3uGA1Rbio6F8rQ5TKyHyqDNuLa1Uf8nJl6JXqCPNPj9XVzJGdU27JEg8fwPmn-jEz4YQZPd5l4pICjWArNI_2uz-VYeE0UAnMWDbxH7sFa_IH-OUn-4Jfpbv4DT4oqmtGIrRRvb_5wSwBMlzkZhF9ucRxepRC9tOGQv2DbADrkmg2y31b71TreZqPPI54dwWMTe1HGKirDk99beVxUHH_kDGmwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توماج صالحی با رپر بسیجی‌ای که شبا تو تجمعات اجرا می‌کنه درگیر شده.
(به نظرم رپره داره حق پسر ایرانمون رو می‌خوره
💔
)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84604" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=ejA02eX-aFMeysYzIxCzM-CvRLMo9kRm2jM5d2MLyai6a3J2laCrR_cL2l5oSxg9NBD6CtsaMYiBYKBAJOb-6kO19BKkYpgfUdsDb3HrFnqZD7w_pqVmgH4oPBM0QB--IPbJTHX-OGhHttDBGjPRhwt0YP5D6drsqVGtYHPbjLfnr4IVyTWZjom-EwuImxo09dC5k8zihMvFBSGoPNwqrsJIFN2bRK-3EJ4WxkwFwfJRNZoAM6TUGVxoMzhWrNEvOgOqC9oX0kuvvFU7e10r-RVaPCAtB5KSF4bR67YRsCLb3uD_nQK299lY_1oQk8NAIQ7dSyWhFyo5R2n-dp5AzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=ejA02eX-aFMeysYzIxCzM-CvRLMo9kRm2jM5d2MLyai6a3J2laCrR_cL2l5oSxg9NBD6CtsaMYiBYKBAJOb-6kO19BKkYpgfUdsDb3HrFnqZD7w_pqVmgH4oPBM0QB--IPbJTHX-OGhHttDBGjPRhwt0YP5D6drsqVGtYHPbjLfnr4IVyTWZjom-EwuImxo09dC5k8zihMvFBSGoPNwqrsJIFN2bRK-3EJ4WxkwFwfJRNZoAM6TUGVxoMzhWrNEvOgOqC9oX0kuvvFU7e10r-RVaPCAtB5KSF4bR67YRsCLb3uD_nQK299lY_1oQk8NAIQ7dSyWhFyo5R2n-dp5AzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روزهای
بلک جک فارسی
در  Berrybet
💸
بازگشت نقدی:
معادل
0️⃣
1️⃣
🔣
از خالص باخت
💎
حداکثر بازگشت نقدی:
۱۰,۰۰۰,۰۰۰ تومان
❤️
🤌
حداقل شرط واجد شرایط:
۷۵۰,۰۰۰ تومان
🩷
بازی‌های واجد شرایط:
فقط میزهای
بلک جک فارسی
از ارائه‌دهنده
Creedroomz
⏰
روزهای واجد شرایط:
دوشنبه، پنج‌شنبه و جمعه
🌐
ورود به سایت:
➡️
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
🌐
تلگرام ما:g16
🅰
➡️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84603" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=ACZ9dnKrts7DJLQ2WfzyyY1gEdxSIZfHoZKWcCa3PxWKI9E5TgWog_iI81AetrxiS3bUsO7GIGNd84RnNb301DBYe9Tugf0R0uqosNOzF4grsWRDSC0V3R05f7NMnD0XN2A-5HqsFZStAyr3SxvnBghMeREmDO6DKse-KwsFUPfdV_Zpr7vsCs2t_qEKjGMruHvfPjfZjRSdCHlsf4s9L9LXyUpljLGbictfnVPm5a4LeWlsELj-Fx7yYBI6alQ5PtvpMD8V9aiE4bB6nEo6RcZOarUEDzqbR13MkzOANxqS7_N2n2QzNJAiEFwJBvi688L7mWJZR-tR2CgKxT3PHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=ACZ9dnKrts7DJLQ2WfzyyY1gEdxSIZfHoZKWcCa3PxWKI9E5TgWog_iI81AetrxiS3bUsO7GIGNd84RnNb301DBYe9Tugf0R0uqosNOzF4grsWRDSC0V3R05f7NMnD0XN2A-5HqsFZStAyr3SxvnBghMeREmDO6DKse-KwsFUPfdV_Zpr7vsCs2t_qEKjGMruHvfPjfZjRSdCHlsf4s9L9LXyUpljLGbictfnVPm5a4LeWlsELj-Fx7yYBI6alQ5PtvpMD8V9aiE4bB6nEo6RcZOarUEDzqbR13MkzOANxqS7_N2n2QzNJAiEFwJBvi688L7mWJZR-tR2CgKxT3PHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی رشت رعد و برق جوری میخوره به دکل برق فشار قوی انگار که زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84602" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84601" target="_blank">📅 18:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هوا الان یجوریه که همه تو خیابون فکر میکنن شخصیت اصلی داستانن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84600" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حالا من که میگم استقلال یکی زده به تراکتور، ولی ناموسا فوتبال ایران دیدن نداره</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84599" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84597">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84597" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84596">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84596" target="_blank">📅 16:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0uYgp_BtkrWWjqsF9HMB_TijTAtbEpUd3qZW3Sl2Z-i1i-xHxZjCIspH2jYs8KK7f9OO7qePV_7a62N4FJPR7NtCqGVXRA8Dhw95Slced980cUN_h33vJ2aee32k2xLVsXfgjeq6wqp0AEg7m4MsRiBV86hegxScyZJ4WgCgOAayvLFHtKmVLyteX7Y3wxHkJadxOftscB21kBNQHdq1msgousnmrkth7Fixag1HJ4QgfQUeBJPxWijbZO9Qe3drB4wtJSmaOOIiHPelxKI0MKzUVQLqP0OPcdJ-ViXJ75CYgYbAxfEJH7ovDYFXHqH1atLTrCdAig3qPJflZxsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر دلو فوت کرده
خدابیامرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84595" target="_blank">📅 15:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84593">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gww4xJwoYlvlOuF8kpLfXccUIk-xMVF3FF5f765EutS3k-Ui15pFVL2YZtvKUT8G0XCuFsU2tIKGFkdiOxtm9f9kYVv_GuAbDYsKalxhiF1iS4H-P7Xz6wGRXCPUk0Clu-CcXku7kTjPKIGa20ytpp7XI16C7Hyu-wOxVUAJWrF_Q0-lANMIKZvAhIF8SmxqZmRRZu9TkAvzptLvQd-z_G34ek5ARPhE-jylK1OaHR07K9pM_lyzRb5EmLtlmUpsSuaeoSU14NVZ2J-wJfQvVqHZiW_KmZl3FLrb35WYPGMjSd9_SlTjI6TyTXdb52v8-UW6PSiJ_xmDYR50ikMNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5hM3qzcOfMt7Ny8ReAmXVAPW1UbJGvT8geWfJ4IcchlHH-NWbB-MwHt6sivSJvICGwV3kDuVnq49myXwayRN58hR5plU1ReyfObeHEzGgIac7zS97q7tXlVdHalsSsqqyvwyXcxquj9XOnYTV9H530fVUGTnkY_moeo7Y2A8fXRHcuZhEsYDs51hMcaWsAzVPSE0MPyifWkRLlTRrSU-Ok7blxxFQpdglCrG2_u5xC6PYiOf6SBrDdRDdYPWTyODY6J4-D05QXuaeQHKqOjEFe4nUu_xanSyYqhSOoDy40_2RpJjXNYFXAeHAY8zyoUG_Wdsn2n7oidKppnwZ9jcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشتی ریدی که
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84593" target="_blank">📅 15:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84592">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مجری صداوسیما:
گاو که دلار نمی‌خورد، پس چرا شیر گران می‌شود؟
کارشناس:
اتفاقاً گاوها هم دلار می‌خورند
عالیه پسر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84592" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84591">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=PhU9vM998Qj5sxD-Qwa9--6B1HvbLJrMOi6Y8iieRZjsrJOnO0T3fwOkM419p_9PYHB9HJQK1UYqeE260gxY9tL1NRzjpE3p6xVVe4E3JHw0IdKeHOf59eGUxFF5wNGVDaP4bezpDvvVjcse_8ozue-plZX12TlhSZUifXJD80nm5YZhTezPpWMqDUizP8GxfhUU6yABLIoumoqm5UTrNan-0--uIhxIyR0KoXlO_zPc6MnuG_Qq3KcMuwRQ9zZvXcIYlzgNVbm650RcA9uZCYB04LA0qi3-J9iaEbVXYNibz6alefyiDBqOHeD46MhT_k3beRhHiRMCjDLGIA_9pA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=PhU9vM998Qj5sxD-Qwa9--6B1HvbLJrMOi6Y8iieRZjsrJOnO0T3fwOkM419p_9PYHB9HJQK1UYqeE260gxY9tL1NRzjpE3p6xVVe4E3JHw0IdKeHOf59eGUxFF5wNGVDaP4bezpDvvVjcse_8ozue-plZX12TlhSZUifXJD80nm5YZhTezPpWMqDUizP8GxfhUU6yABLIoumoqm5UTrNan-0--uIhxIyR0KoXlO_zPc6MnuG_Qq3KcMuwRQ9zZvXcIYlzgNVbm650RcA9uZCYB04LA0qi3-J9iaEbVXYNibz6alefyiDBqOHeD46MhT_k3beRhHiRMCjDLGIA_9pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۱۶ مهر؛ روز بزرگداشت داریوش بزرگ، شاهنشاهی که نامش با شکوه و اقتدار ایران هخامنشی گره خورده
👑
داریوش بزرگ در سال ۵۲۲ پیش از میلاد به تخت نشست؛ در حالی که شاهنشاهی هخامنشی درگیر شورش‌های گسترده‌ای از ماد و بابل تا پارس، ایلام و ارمنستان بود. او طبق کتیبه بیستون، طی ۱۹ نبرد مدعیان سلطنت و شورشیان رو شکست داد و دوباره یکپارچگی شاهنشاهی رو برقرار کرد.
در دوران داریوش بزرگ، قلمرو هخامنشی از شرق تا حوالی دره سند و از غرب تا تراکیه و بخش‌هایی از بالکان گسترش پیدا کرد. او همچنین فرمان ساخت تخت‌جمشید رو صادر کرد؛ یکی از ماندگارترین نمادهای تمدن ایران باستان.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84591" target="_blank">📅 14:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84590">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نیویورک تایمز:
پاکستان به کمپین نظامی عربستان سعودی علیه حوثی‌ها در یمن پیوسته است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84590" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84589">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خیلی دوس دارم صبحتونو با درو دافایی که تو اینستا دابسمش میگیرن شروع کنم ولی اکسپلورم کلا شده کچالویی که باباش داره مسافرت و بهش پول داده تا ۲ سال دیگه برگرده ببینه با پول چیکار کرده</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84589" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84588">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4X4iLJXzLQvMjvQNp5LApSoeKofpHzrukVlMJcPhIjj920UbwL0AOi5dj-M4-OzByldw83knVeVjbmz4WwLgyq9Thab7L4fi2LVEQFx7Tyc7f5Uj-PASDpk8vqPmkKYxrQPXzxqmLD17s2F4Bfr4gTnlull136XjKdT8b812sptGDIu9BoPQI2sHGjXOz59KCw4MSoaMda2AtE56RTsUkjakUeGu740e7TpcdLmziCg-UmjVaPS14CvZteSGVSARowF9knPX3hx50EB-KA935ywpkeh-D5jzMMHwfMVcswykwnfiYv5iWT1VKb0QrabqAAWLeQKHMAbzfRjjRzHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84588" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84587">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84587" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMe_23cStrlIEXsx7BjtNGx-cas0YYcuHJUkQK4I3DRL2wN7SQWsosy43y51Rb1aB6jqhYMln-3RM2zNVx9Y0qJAANbMMX7SDR01l2L2Eht_C_YyazlKhBRqJ_cqMqjg3K-I0eU94FXM4RWw607SILKxSOyz0pk851GL_gd46pp9jhURz1ukVVZcrQBDSIZxHyFuhkQPFhuUPxVJZ9-OTQFN_jd8rQTlEatNoN6RUpZKic9JQ6_EjYvpGNonJkCRAIzJa7rebdNTr8akcwEsuEyWusKW3jUW0ytcBoh3xVSqkXqIFWO6BQGVQg_YQ4reBe7EqYkd53cwCoubAGoA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آلومینیوم اراک  - ملوان
🌎
ساعت 16:00
⚽️
گل گهر سیرجان  - استقلال خوزستان
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:r16
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84586" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خیلیا تو بندر صدای انفجار شنیدن حالا معلوم نیست چی ترکیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84585" target="_blank">📅 09:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وحید جان بیدار شو، زدن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84584" target="_blank">📅 09:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894c49154.mp4?token=CPMhkVEphzpgWWTprIryCN2EpXCDf5mOCSLflKZ42wty0rOyE88e7yiUnmOvAh3gH9jZT09nxSAdtqegDAlw-a-nreWVHWoaRLNdmLwdIofS5TS3leNbAbHHsLHt7ezl5xf_D7Wlp0qpG2q0tkSovflrpp9D7g64A69TEUuu0WQXEiYQSsZsO0X400MVDk2LohomoUcczU1gn-cGS17oQz6wzM4AD-w6nOebO7RdtTHVwqVZLEtOtZyynKfOefeJ1UW3nDkxYHZ-jKDylbrF5ZPoMOx6Qjq1Uhuo2Lzb6EjUHU9GkWnQvrVnrqa55EDW4mZ177B0Zz1TdfWCw-Okzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894c49154.mp4?token=CPMhkVEphzpgWWTprIryCN2EpXCDf5mOCSLflKZ42wty0rOyE88e7yiUnmOvAh3gH9jZT09nxSAdtqegDAlw-a-nreWVHWoaRLNdmLwdIofS5TS3leNbAbHHsLHt7ezl5xf_D7Wlp0qpG2q0tkSovflrpp9D7g64A69TEUuu0WQXEiYQSsZsO0X400MVDk2LohomoUcczU1gn-cGS17oQz6wzM4AD-w6nOebO7RdtTHVwqVZLEtOtZyynKfOefeJ1UW3nDkxYHZ-jKDylbrF5ZPoMOx6Qjq1Uhuo2Lzb6EjUHU9GkWnQvrVnrqa55EDW4mZ177B0Zz1TdfWCw-Okzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ آقای زنوزی پولاشو از کجا اورده؟
- آذربایجان ستار خان و باقرخان داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84583" target="_blank">📅 09:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA3JdszyQMVQ_bnNG_OZizpl0m2T6LbA0F0yIxdAwgpQUFgSde6ZnZb_8rX911DIsumC2V-XtIvX6mCVCDsRsU_gvIOTkjkdT6QohpSCDtIXLCNyM-BASRjiDU5GASJ4T0V7R-ivA16V9oAn9qTyXp64Ufj9K8_8039IYT8uAHYGNUn7jz-wUmHcOhAuPYd9rSG2_4XY4sQL8ULj00AwOLmqitM65ybRPwLHFcb0lQsAu-xy2rDpPUE890Qx9C7WPKP1ywmuQMTuZxY3YN01gzxTye0IJ6U0t8EUKsYTzhVYo5w3s4yaal3Cz9PO17rQ2XpMvVrdBttNVzp6xb9Mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه گویی رسانه‌ی جعلی آکسیوس:
مقامات جنایتکار پنتاگون به سنت‌کام دستور دادن تا آماده بشن برای حمله‌ی مجدد به خاک مقدس جمهوری اسلامی ایران قبل از انتخابات میان‌دوره‌ای آمریکا.
همچنین دو مقام اسرائیلی گفتند که احتمال حمله‌ی پیش‌دستانه‌ی سپاه بسیار بالاست، زیرا آنها دوبار دچار غافلگیری شده‌اند و دوست ندارند این غافلگیر شدن برای بار سوم هم اتفاق بیافتد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84582" target="_blank">📅 03:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84581" target="_blank">📅 01:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84580" target="_blank">📅 00:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستان زیاد دنبال موضوع فعالیت این چنل نباشید، هرچیزی جالب باشه یا حتی جالب نباشه رو میزاریم ما
هدف ما راحتی شماست که مجبور نباشید چندتا چنل جوین باشید</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84579" target="_blank">📅 00:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رسما جنگ زمینیه
افراد مسلح ناشناس با شلیک راکت آرپی‌جی و تیراندازی با سلاح‌های سبک و نیمه‌سنگین، مقر فرماندهی انتظامی جالق در شهرستان گلشن را هدف قرار دادند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/84578" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84576">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=noCJEV7xvGC0syUwCoBFRcmJK6i81drwo7RSJViumy57ITNSIN8iqnEyZtlaKEfbypdN618sv87OzLO2FUu07E8pd1oBRW9lJQqBXVKIYwE98Q2ozPMc2wCHwZWYGOHEKp9ixyXxYUHrroMi0jiK-chQSs7wjb5nUpF-A7ehm_Guz9l05IPnwH0xz-Pj6gWuu4Pz6ndsqeSrjnOjiN6oe-Is5zempK_b1PWWc-1hR1rJqWiT4ZRdk72Ylm2tCTDv3uvw3ES5Th2USzyfRP3zWRGcoOEypZYZYyc_tHBMSPdD_2_XFeS1X9p3W8-XLyVljpvKv0Oap1jTMYUGh9M0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=noCJEV7xvGC0syUwCoBFRcmJK6i81drwo7RSJViumy57ITNSIN8iqnEyZtlaKEfbypdN618sv87OzLO2FUu07E8pd1oBRW9lJQqBXVKIYwE98Q2ozPMc2wCHwZWYGOHEKp9ixyXxYUHrroMi0jiK-chQSs7wjb5nUpF-A7ehm_Guz9l05IPnwH0xz-Pj6gWuu4Pz6ndsqeSrjnOjiN6oe-Is5zempK_b1PWWc-1hR1rJqWiT4ZRdk72Ylm2tCTDv3uvw3ES5Th2USzyfRP3zWRGcoOEypZYZYyc_tHBMSPdD_2_XFeS1X9p3W8-XLyVljpvKv0Oap1jTMYUGh9M0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی قیاسی رو با تیر متوقف کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84576" target="_blank">📅 23:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84574">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HflKXXRSDK6uzAhwXYcTFyAN6NrqSAK9PJ23eMxXYUyWEMTH_wmKjf_KWj2iX6HU84zenRdqEDd3LUEy-b1cjIBSBHgzvhSUDKyiiZLUNy5rEkvnee_tuonTgfBKP8_YdiIBUY3supC3DhMlfMweJ5lVY5XfpEbw9y7S9l8TAgLaCUWNMSrqy7bchhzpZlG_HXFOU6SN3mWQqWlI0_SImu627_1KgbKz5JWCPa-VUXxzOS7kpHmmRMztIYpa4RyC3ZVxfgy76nJlzN44LTYnzJsJaVAfOCsGvWOBTbGTMaRSoDw87VStAd--VsqXkGu4Y1DHcC-3hPzFtl6VYeZV-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-7IAkzuajGYQbf95r4glbK2JReVC-HdQfadDImi1JUwlMo30dzqIrJnR5IGu1ny7-49BS-fYPp0lV3HUjUFUO4osL5Z74rFPDtpDE7hRjaAbG8elJo2-fN3xbRb5ExoaWkitVq2DMT080FG4RAofsjZHBrxOLIa6nLeiUlajJ2Sz1CxklXdSR2Eyos7Nsxi1zqQdaxW1bz8LtQg77SlB-HhAzQVXbXEd39gxYMUwN5JOutk9jm022-MRzO33aRn2Lz2hBU0cU1B9Sv7-XU2BCIzPyA0XKwUZ-UEsbnbG2hFzfs4u5kZJxTLjYoy9_0sHARL0tPVhez2ha15q02khw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان و ادرویت دوباره افتادن به جون هم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84574" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84573">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐒𝐡𝐚𝐲𝐚𝐧</strong></div>
<div class="tg-text">بلندگو هاشون خوب نبوده</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84573" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84572">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=GyUACpW2mjwA2LKvLoTihH-o3FoKYiN0OcagQAATbbCvx9dMT8EF7i82v6qwpo4zRRhPZraDQ4NW3vbgXxcZ8RS15UmtvOvmWJt3f8T4TTrBU03VP3vIVgiR2g7FA8elA3ExprEL80yFcs2qwR-JxO7T7azrrGIEJZkuHApL6OK6PQOcx2JPrd1FGq2ZKO4A04ZYl4c1qWkiOQeK2R43iyKpHD2NKVynquNn6Rb2asCNgigp2cdGeI6kpEzHRsXF_gYiZbrx4ZytEdbVq5rwz8R4kaDEVYGyRbfz2A7LPcoxPEgHlzqO-ZBtYtW5f7kP4uBVSFGr657VqmwZ7VPePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=GyUACpW2mjwA2LKvLoTihH-o3FoKYiN0OcagQAATbbCvx9dMT8EF7i82v6qwpo4zRRhPZraDQ4NW3vbgXxcZ8RS15UmtvOvmWJt3f8T4TTrBU03VP3vIVgiR2g7FA8elA3ExprEL80yFcs2qwR-JxO7T7azrrGIEJZkuHApL6OK6PQOcx2JPrd1FGq2ZKO4A04ZYl4c1qWkiOQeK2R43iyKpHD2NKVynquNn6Rb2asCNgigp2cdGeI6kpEzHRsXF_gYiZbrx4ZytEdbVq5rwz8R4kaDEVYGyRbfz2A7LPcoxPEgHlzqO-ZBtYtW5f7kP4uBVSFGr657VqmwZ7VPePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84572" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84571">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a289765.mp4?token=eYToV95gjFoq5q1dmrx_6cKg6KzVn6vkIsrMd_rkGOWzB3v3XGYuG6tdPo3DgJU5oCcTF-YL3Xg4ic_DpZD6DqV22xX0ItkH8FtnrJKffWBPautHMAVqmhJI1HCzebis35Gd_nd-i2JUQgkrFYjEdKvwd5PHStb0h1hbsa4jTDJQetfHMyTIqIljxMfflUUkIktLC1QsqFv6smheWnfIefUvDnF_kkZOeRn0vR6NfMZZVkofcATz2ZGhtxsUo8--G7t8PFGTUmewf-hfbJW1JzDzTZ_W6PCc2beExPjllYeSHR-bTJoWUm5sPhlQ3y4GbkjJ5Z4auUUeDiJlMnJbyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a289765.mp4?token=eYToV95gjFoq5q1dmrx_6cKg6KzVn6vkIsrMd_rkGOWzB3v3XGYuG6tdPo3DgJU5oCcTF-YL3Xg4ic_DpZD6DqV22xX0ItkH8FtnrJKffWBPautHMAVqmhJI1HCzebis35Gd_nd-i2JUQgkrFYjEdKvwd5PHStb0h1hbsa4jTDJQetfHMyTIqIljxMfflUUkIktLC1QsqFv6smheWnfIefUvDnF_kkZOeRn0vR6NfMZZVkofcATz2ZGhtxsUo8--G7t8PFGTUmewf-hfbJW1JzDzTZ_W6PCc2beExPjllYeSHR-bTJoWUm5sPhlQ3y4GbkjJ5Z4auUUeDiJlMnJbyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای سامان ویلسونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84571" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84568">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6nVYSae9k0DRjn3C1MT1Nu1YiAn7c1oxnkFjWMEjZ6Fu8SszsL7eQQ4fBYlwQr-T1a8ftnim4A-1W2JH2f4Al5p2tVTisJx0iUqLbx2F7yRuYSr7ZKpiNuxAC2GA4flTZ76UN46ba8ZkbLJd6DNHcDpMPoHTMirpLFIiEx5jipNeUc0LZ34gJriN7n8M4g7qIibSlunzxIXv3iprxrbMLJ6BdfNVw6EqybvAGstMPqmpfSYhPks_vqLHukxz3W4N9K2u-L3pEuTZfPhnUS8fPdIW-VoXu0Y70ZRXhIJZ0I2VxLgZd6fgi38jB7x9aUYQUEQibgO1lKwJJfqNK_CEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی: لئو، سال‌های زیادی از کشورت دفاع کردی و تاریخی ساختی که برای همیشه ماندگار خواهد بود. بابت تمام چیزهایی که با آرژانتین به دست آوردی، نهایت احترام رو برات قائلم. یه بغل گرم...
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84568" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84567">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کیانا عظیمیان خودش یکی حرومزاده تر از مهدیاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84567" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84566">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghnn4c1_eQy7DakhHAISOxXPxiq5DyR0jp1jFohWz_MYXrcW8wdYZ7gQYY-l9KScq-2qGQNtbDlGVJfDReNn5GJpwwMYczQvAkFVyew4H0lPg5VctgBbDQ0IBKIdFtR_hM_CvoRSklmzULrvs5vEBPIl3qbI9Wr_weHIcYupW_cgPL44fm-NbUNCH4YsqwEzlB3CDnH7KoduG8Tzcwe8Kbw12GEsOD32c-itclPR7rLq4Lhr8Mn0XKNCwtpl5jPHJ2Lh6lL_bL4V0KA0EC3pqDklj9tcANyWgmPXKW-pWpnb3KhVuYMPRhbDO7E5ITtAc_TbMLs-cRh2RX78YFiSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری های صاحب صفحه‌ی ۱۵۰۰ تصویر خطاب به مهدیار و ملتفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84566" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84565">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مسی کصکش جام جهانی خداحافظی کرده بودی دیگه بازی خداحافظی چی بود پولامونو بگا دادی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84565" target="_blank">📅 20:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84564">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پاییز نیومده ثابت کرد بهترین فصل ساله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84564" target="_blank">📅 20:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">HEJAB</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84561" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84561" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K08cT0QeLas1d4oj9scMsQN7q2Y8hWmpLQ4kEznzyYjcxnPXYo1f3z7eO3WTIllI4TrfrNdhaK4YhHG8uGu63bEjvtvZPw9MBRokS51i30WvBSaIAHwBcPYdk_rui5XfDGMceSA_GMfMqVvnEdPXRBA9jUA4qsu4EKVAsbpnvYFuQkbnR3aakfL-8QvdqG62VNX8M98TOIcCCbWq9EzqwCETbks27ZK190EHIRj-l3nO222Nv4vFC04PYFhPvFZIj1VjiMDyPu13AWWg5dQDJmDp-RLSlCCuMNDiDDfPQDz5OAsmn-72SV6-r9NRLv7enEqhYHMMXN3iSesw8FdLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84560" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=pxwYbIwu2J9SF18sEJxQQFSn1WhOXTi3anrgTdbljgE6nx6_A4o-N5tWyS_a34nWryjWCOVuaoB-2EE6i6bUi0sbs-Wb8iIeLQjwJ2-E1EvpwBX6aoOpAh9N7J-F9SrFoAYfZgcKAn-CaspiHDZ-fBAc2bKPT2Z40xI8ZvyFkfj5Lx2JvK9jq-7mimribMiEOSqiig9Rix0fnHhjYvAf0Flvjj4nw0F-85Oe4NQi7YWzZFMO59iVuHGp5g-7g_iY4mY7Bz8m_xp1N6iQ5wl291PbTCc7jJwmJgsGv3F4TYNht6WKiMOQe8661eHkclu5OVk4G89juftGYMy3OjrtOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=pxwYbIwu2J9SF18sEJxQQFSn1WhOXTi3anrgTdbljgE6nx6_A4o-N5tWyS_a34nWryjWCOVuaoB-2EE6i6bUi0sbs-Wb8iIeLQjwJ2-E1EvpwBX6aoOpAh9N7J-F9SrFoAYfZgcKAn-CaspiHDZ-fBAc2bKPT2Z40xI8ZvyFkfj5Lx2JvK9jq-7mimribMiEOSqiig9Rix0fnHhjYvAf0Flvjj4nw0F-85Oe4NQi7YWzZFMO59iVuHGp5g-7g_iY4mY7Bz8m_xp1N6iQ5wl291PbTCc7jJwmJgsGv3F4TYNht6WKiMOQe8661eHkclu5OVk4G89juftGYMy3OjrtOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسسخوش با ۵ تا سرعت پراید چپ شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84559" target="_blank">📅 19:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84558">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r92ErKZj5zGCn9-n05a7c9zVspLbVnS4Od_PAj-x4XWliajh4vMJrzoVJ7zGxDp8yM2tnqvBfZjAI6_ZXdC_MblxA2HV3-QpV6Hr99QGx7MTv-zTxAC3Czr5WK9bUTUcz_i4v64sQwQgrqflC64Ksl_rYw0jUpswMs4lfSrXICtlaViCcPHja6OuZ3x6TdAj4GDB-y25iDxszExvJy3Px0QQu81Crxcl1O05Z3MUZ1eyRM3xk_2kcq29P3P8eA6WQK6MIsixGdh2sIrBAN_Vzw70EvRKufHgAgOM6F1RxJDJ4UCIdSP5nh_t44gAUYTTHIwnhpPTKMRK0vxxZ0VEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این کامنت ادمین دومینو بسیجیا دارن دهن شرکت دومینو رو‌ میگان و هر روز جلوش تجمع میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84558" target="_blank">📅 19:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84557">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0UMFz1dPggIMT5ALELWxOlPfKeVPd8PpnaM61y6fB7p224CtULtOiBzoGFW2EfPtiEzwx07OLtY5lFWy272JiI9X8Vs8boeT6Xr-80J1PAy2-sjjDOz5oHoaK7XqZzRr9VhEM_RggEZLkOPjIZBHDJyoFDAulTfavlXTTbX-EKrm8Xw-edLSXt4JUVS208A-8_6cZ_zCk5LbpmnYdPhdNlS0zi7fmhcySVQ--TTkOY-PY0jAeore2_RiTcEcN_8m0dLn81l0heIFSdkjHu8HFdcr_JGnM0gc0qxEbS_03p6sBLaseR1-tT2gtVB2YkhRxFYLwJlzXXlG1aNxKPQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیم‌کارت با قابلیت درآمد زایی؟ اونم تو؟ بیا برو مادرج
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84557" target="_blank">📅 18:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84556">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=iSMp2HJKXtBDdc9hV2q7kf6VZnZRig7MUsCU_JJgQIneDTPqtlFEwMjW3OZV0alW9OQWvYhFDZePXpSHzAjmESWWtwqBxZPiN-Erx4yemCtWZVoJuJGBMf2h6ZuT9RKTgVRftDf0Y-ONLQM3QmCntKwpf6VNkcgrHWWq_fEGYqJfA-6kC668j84Z1KoK8ezgwpwzaABWPDk_b8PWTjfhG7DdToXlN7ZjxQHwt6FQB0E4sByzgtw5Pm7gZuzQrSLNLIjOKrIj28q9ObPlyU_y_CgiJso2RvtMwt9XLFP7rYE3MOBA5-FoCSrdjPGEXcgXL6b0HSFcygiJufMnu2PdGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=iSMp2HJKXtBDdc9hV2q7kf6VZnZRig7MUsCU_JJgQIneDTPqtlFEwMjW3OZV0alW9OQWvYhFDZePXpSHzAjmESWWtwqBxZPiN-Erx4yemCtWZVoJuJGBMf2h6ZuT9RKTgVRftDf0Y-ONLQM3QmCntKwpf6VNkcgrHWWq_fEGYqJfA-6kC668j84Z1KoK8ezgwpwzaABWPDk_b8PWTjfhG7DdToXlN7ZjxQHwt6FQB0E4sByzgtw5Pm7gZuzQrSLNLIjOKrIj28q9ObPlyU_y_CgiJso2RvtMwt9XLFP7rYE3MOBA5-FoCSrdjPGEXcgXL6b0HSFcygiJufMnu2PdGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمااااام تتلو همه تتو هاشو لیزر کرده و از زندان آزاد شده
😐
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84556" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84553">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojYhMn6l32Kg4OVz9wSaNKco1ywcAOin3XYpSuBjjnvaX-0v88Ogf0VEZZ9KIbzOAMIJ_avU9dPw9pM7V9xs5JzWtYyaKUEeS5jTHLiIytffvdmpBx58RsgmUzzrKDrimTJ2y45g87aUjFXfwPt_Zgpm6CZr3U_32NUjoV4ilGBvcYoujbcdGQH5C46HqVllBLxggPxmXCwtbb-X7zRlMnDQrWI01locdP6K3Qz8cbFZXwO0DuDv_1bHW7-fMBIfPDR27GAURApvAuJflU7UjFmZ7fP0mRQpkLfn1D8RnH3pRFkEGUioQyw4EuQ_5_XPs9OowFtB5gXz9OAvgEl6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نارین خانم دختر ۱۵ ساله سنندجی که تا سر حد مرگ توسط پدر و نامادریش شکنجه میشد زیر نظر پزشک تحت درمان قرار گرفت و بالاخره حال روحی و جسمیش بهبود یافته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84553" target="_blank">📅 17:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84552">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvC1CgWbGHmabVD3ZsCtBaWx89JWZCaf2fGoiEC7VGvc87Z0NKmV2sfcDBRn9sRSk4ER0Qyg7smJuiPMg3JyBjOG0JpaxpghT_293GyiaHLfa6WhLxU0re65nieQ-pbm6HPwOwGj1IaGLoFwi4Id4z6qhf6U3285LW0BcP11aCt0KWAsK5ieb7JManFotX3xXJAaBSamwwFJVkk9lMUAU21P9o4Ackws1izHVBN6qqO5RAGllf8l0YFKL-iaCggqBT6ogaiPtrebRmuXHECInxamdozIn2wL1c0Mxi0-sJXGuWRW5VdNQd79_2y3wvqCotgmSnF5bwipxizx-a3-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اینجا واس دوستام تعریف میکردم تو مدارس ایران همو انگشت میکنن خایه کرده بودن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84552" target="_blank">📅 16:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84551">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">من اکسپلورمو به کچالو و مردی که عدد روی پیشونیش رو قایم میکنه سوخت دادم، هر کاری میکنم هم درست نمیشه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84551" target="_blank">📅 16:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84550">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlVOOJsbO8hZTnS5mLTHSGRzxWnQfQeSPMFy6TiKzUrIWEjExDgUvCQHr5iNzZE7HqwfyM4RMx5WNv8V_GEHlxtB6yI-LhPpxGH7EZc63WnyylHZ3MnacWIPMIAg-7x1BZ0oDszCReourXMX4qnx8uW3sCDMtOtQif0_DOLwAkkH-0dbNAum_irL18Wuk8JCDcLiVl_dG_g3-mXSI6x2kityus2JCdpOCM5I-lyMdtjjP6gki2tsUI1HDPAN9YbfzyCxhH0ddPuLbivnpw0x-X8Ggq0r6aQNhcW8KMRGgF3vPeEVHacEnbTMSoEioDPum-y9BOJcV18S1JradeSvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نالوتی یه ویدیو با هوش مصنوعی ساخته سلطان ازاد شده کل کسایی که تو توییتر هستن باور کردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84550" target="_blank">📅 15:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84549">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=vuw1WmisVVlC09NvgJFlZtAAkMLxZMU3q6PDqKaTTTbMO4AZA1VJ30nVZCZ6bbOFcS2vAUzoRFfFDdq84yOLFvyun9CIl9Gx8pO77bUwV4xtLowcjyJQEHLIFo5VO1fpMlsHIonO8Uh0ke0cJmE4jxWEbCpl64xuJ7-X7HStg6upR2NLYD_VauF8g8mU1drjRomZPZgOCmj6ZBdbfTUAEVu72jXbgkkILSdqY_D85m9MLRyBom75k519bqEHmqpdFAKMaBlHyhCKYsBGnEBfqWCo5Oz6IczU32sOZxXHF_5SE1iK872vV-LCwUbRlFkoyDDD7jmO9Aw80GOnrIvJOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=vuw1WmisVVlC09NvgJFlZtAAkMLxZMU3q6PDqKaTTTbMO4AZA1VJ30nVZCZ6bbOFcS2vAUzoRFfFDdq84yOLFvyun9CIl9Gx8pO77bUwV4xtLowcjyJQEHLIFo5VO1fpMlsHIonO8Uh0ke0cJmE4jxWEbCpl64xuJ7-X7HStg6upR2NLYD_VauF8g8mU1drjRomZPZgOCmj6ZBdbfTUAEVu72jXbgkkILSdqY_D85m9MLRyBom75k519bqEHmqpdFAKMaBlHyhCKYsBGnEBfqWCo5Oz6IczU32sOZxXHF_5SE1iK872vV-LCwUbRlFkoyDDD7jmO9Aw80GOnrIvJOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک مرکزی افغانستان در گزارشی خبر از شکست دلار توسط پول ملی این کشور را داد
در این گزارش آمده است که:
سال ۲۰۲۲ 1 دلار = 90 افغانی
سال ۲۰۲۶ 1 دلار = 65 افغانی</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84549" target="_blank">📅 13:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84548">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرنگار حوادث: تو کارخانه شیرخشک سازی،کارگر با کارفرما دعواش میشه،برای انتقام مخفیانه ۲۰ لیتر اسید توی مخزن شیر میریزه و لحظه‌ی آخری آزمایشگاه کارخانه متوجه این قضیه میشه و از یک بگایی بزرگ جلوگیری میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84548" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84547">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رایتل یه خبرایی از واگذاریش بخاطر ورشکستگی پخش شد، ولی به دلایل کاملا نامعلوم مدیر عاملش اومد گفت کیری سودیم واگذاری در کار نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84547" target="_blank">📅 13:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84546">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=Bg6SrQyNAZbg4FCTPajHLxpfGH8WeYDgwj0ofehgPP4OCDFGo-q98oRyQfyPLAySgLRnhigN_pFU06VPoNBqE3FmIGF-coLBAetl3oMgb2S1kBamGFuBo-ePQRGTI10ajVIG_D4ZuGWHJY67ms0XCVAls6aGOYoq98bsroZTcoU2VdYCe-CbPJJHD8DPBRCc0pJOj6keEs-AlE-Dy1YgHNPmYw5S7iYN6-8pA7soIPBu2b9fNAk0YYzXeg_5NZw_A2lmjDCEln2RzyogZrpPNhu7SpgL73ZSyWaDnNKVjlEk91fV7u-AUCeZyI7BnkFKqgWZsGu76LGkkR5TaixF7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=Bg6SrQyNAZbg4FCTPajHLxpfGH8WeYDgwj0ofehgPP4OCDFGo-q98oRyQfyPLAySgLRnhigN_pFU06VPoNBqE3FmIGF-coLBAetl3oMgb2S1kBamGFuBo-ePQRGTI10ajVIG_D4ZuGWHJY67ms0XCVAls6aGOYoq98bsroZTcoU2VdYCe-CbPJJHD8DPBRCc0pJOj6keEs-AlE-Dy1YgHNPmYw5S7iYN6-8pA7soIPBu2b9fNAk0YYzXeg_5NZw_A2lmjDCEln2RzyogZrpPNhu7SpgL73ZSyWaDnNKVjlEk91fV7u-AUCeZyI7BnkFKqgWZsGu76LGkkR5TaixF7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خلاصه دستاوردهای همتی در بانک مرکزی.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84546" target="_blank">📅 12:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84544">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDKncRT_CAGQ3VhDr_1m-6QXurHH9Qv8NsD6qkhYmNXs9II8jLILZ-JBcOeW8Zr9iPCqiDlNyK4hFV0VuGZWbL11Z99GdaWrxONRq7iSpZYTlGkLt7y0WiUHfmDHMMPHoxBDsjMbne-MT3xI7-UuvvvxGubk7TIJX-21HXPI6e5zh7K1j_EHcUcbe6m9lai4St0_mGz0iVFV08tJKuZFe7QvmrR3FeIomASfJ_dCnNmvxRehL0BK7EO4b86ggYG4vOCrbaoLYa3oKgS6OhuFyPsKlVTMRHlCRl0hcZt58bqcK38ImiU8_wI_bVEGmHJP1fI6IudWDUY1Mo4iI7gx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ab280716.mp4?token=EA4wM5kLKMFgPwH124x9kzAzXJLQFN4YbNCBtpjVJ4HwXRgGJ8j35BVM54o9x_z6kkpWDaE3T8YNDF_G-4135-i_DlBQ3dtmym9bBIJ2QOegiHAmqU4IhWedlIonH-CwAYSX5TdEdXEQ_kEyDmHHRRGEyDqzqw8Vocy7jLbThZyP5E8ep4ub4uMnn79MwHvmZzw0OmAD4RXjG-Bjs4BYPCgGVllm2CMx9bK2hYGzxcdNwAIxcDYbwWfYZ3Tau5iOZyf0I98kgAgwQeyLrd3AAjoEtBI_pbiTW13RsNDQTs4AqCzRyUq7CJFq5zOi-VRKPfPnS5BbFuDRO4BVyd9ZXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ab280716.mp4?token=EA4wM5kLKMFgPwH124x9kzAzXJLQFN4YbNCBtpjVJ4HwXRgGJ8j35BVM54o9x_z6kkpWDaE3T8YNDF_G-4135-i_DlBQ3dtmym9bBIJ2QOegiHAmqU4IhWedlIonH-CwAYSX5TdEdXEQ_kEyDmHHRRGEyDqzqw8Vocy7jLbThZyP5E8ep4ub4uMnn79MwHvmZzw0OmAD4RXjG-Bjs4BYPCgGVllm2CMx9bK2hYGzxcdNwAIxcDYbwWfYZ3Tau5iOZyf0I98kgAgwQeyLrd3AAjoEtBI_pbiTW13RsNDQTs4AqCzRyUq7CJFq5zOi-VRKPfPnS5BbFuDRO4BVyd9ZXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسیم مقصودلو؛ خواهر امیرتتلو :
خبرهایی که در مورد آزادی امیر پخش شده فیکه و هیچ تغییر در پروندش ایجاد نشده. اون فیلم هم که گفتم شرط عفو شدنش پاک کردن تتوهاشه مال پارساله که اونم دروغ بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84544" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
