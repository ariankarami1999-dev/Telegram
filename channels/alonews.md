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
<img src="https://cdn4.telesco.pe/file/PoTRiaYtNAYva8iG6vrNBT9ZG6y0o533YDXQ6LZXV6Dg3V2B64eOFqL5IoiyDGKh6MwKJItW_23UIP0txMRuLntZaZfhp2SO-pZmdPlXwpMM4MpfwHUOf-1b9rEA7BYMdUaXES7efRcbH5VbZECi4jj8FNi_5jewXeZmFIP0VP7m_4du4K_kiyT7F1d5O-hSDuGikcvRJA1Tiqpf3u4J7gh9dOEawZQ-6wGp66x19ztHqjIJuocLEWqUpLS_D_DuKobMCb6iaBFjiRa3XmUdo-j-aotVoS0IEIql-XtRXgTsJIa4H77b5etyZByd8bvWF582g3HQPb85Q1LGpV-VHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 913K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-147416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da4fb06f0a.mp4?token=af_nEjvcIS4jPXO2VDr13SEYOpWKBnACidF5rIB8pDNrvAt1i56y6l4A8Z5bvzf6Mn-Bcgf_aB2adm67tuMsNIUJOS5_YUQMcQtB6Ck8fYdXqCFVi4yk_p3hzaelG3ZxwbcJxNGCmBgBfVLMNYnNB1tomWkf6LO50raN-npG6DWgQREJjoTj3yR8P4nbNouJT38yDPXLVUOs4-3JMPpGU07ukDesJjZYpHH1RgKR-Heme-46nmQimWeDqzfRe9vwRwKjhOCQFSRHyBSuyiDRdAWnTtilE2kTMUru7ESArDrXGKnfFskJEGo0C7_42Rz1439AExMjURY1pAdCl3ubaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da4fb06f0a.mp4?token=af_nEjvcIS4jPXO2VDr13SEYOpWKBnACidF5rIB8pDNrvAt1i56y6l4A8Z5bvzf6Mn-Bcgf_aB2adm67tuMsNIUJOS5_YUQMcQtB6Ck8fYdXqCFVi4yk_p3hzaelG3ZxwbcJxNGCmBgBfVLMNYnNB1tomWkf6LO50raN-npG6DWgQREJjoTj3yR8P4nbNouJT38yDPXLVUOs4-3JMPpGU07ukDesJjZYpHH1RgKR-Heme-46nmQimWeDqzfRe9vwRwKjhOCQFSRHyBSuyiDRdAWnTtilE2kTMUru7ESArDrXGKnfFskJEGo0C7_42Rz1439AExMjURY1pAdCl3ubaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو خیابون شریعتی تهران، یه خانوم با یه پیرمرد سر رانندگی بحثشون میشه و زنگ میزنه به شوهرش که بیاد.
🔴
شوهره هم به این صورت میاد و با زانو حمله می‌کنه به پیرمرده و درجا میکشتش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/alonews/147416" target="_blank">📅 18:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">تلخ
‼️
تله‌کابین نمک‌آبرود نفری یک میلیون و صد
خانواده‌های ایرانی اغلب با دیدن قیمت
منصرف میشدن و میرفتن
تا چشم کار می‌کرد توریست عراقی بود
توی صف
ایرانی‌ها توی پارکینگ با کاردیاک
عراقی‌ها سلفی می‌گرفتن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/147415" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b48e7d1d.mp4?token=lEv54ewNxwF3DwF3aSNt2FaHphLxypDCTHh__mouPQTp5o2S46ZiJxlEKJOuTSlCA6Uj68BZCOXGngC9NuYa4zJj00E5EomA9yIdy6X-k9T7_uhTlh7YlpI54ZJTApjEyxfJoI5-BQjZ2USxf72Q2eQhSX6nTFywkYWpw80GH-JCcSVkT9jMqwAxrPfdmIiuYqMsEZm4S4pDDIeC54IXhZf-WWVC5EhZts-cTwLp4jOE7-5jxPPpYhBRgJp2GY-lz46aXmhlSTXrpnCkzsoejqf6ZunYEOsMILYRMMBsvntvGbXnoh5PJa_KSd6rmuec93rAQggx7ZT1mHwTyYxroA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b48e7d1d.mp4?token=lEv54ewNxwF3DwF3aSNt2FaHphLxypDCTHh__mouPQTp5o2S46ZiJxlEKJOuTSlCA6Uj68BZCOXGngC9NuYa4zJj00E5EomA9yIdy6X-k9T7_uhTlh7YlpI54ZJTApjEyxfJoI5-BQjZ2USxf72Q2eQhSX6nTFywkYWpw80GH-JCcSVkT9jMqwAxrPfdmIiuYqMsEZm4S4pDDIeC54IXhZf-WWVC5EhZts-cTwLp4jOE7-5jxPPpYhBRgJp2GY-lz46aXmhlSTXrpnCkzsoejqf6ZunYEOsMILYRMMBsvntvGbXnoh5PJa_KSd6rmuec93rAQggx7ZT1mHwTyYxroA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرید، برادر زن سابق مجتبی خامنه‌ای : یه روز با مجتبی تو یه جمع فامیلی نشسته بودیم، یدفعه موبایل یکی زنگ خورد ، بهش گفتم این چه موسیقی هس گذاشتی ، بعدش دیدیم آقا مجتبی وارد بحث شد و گفت این موسیقی رو نمیشناسی؟ این موسیقی فیلمه کریستوفر نولان هس ، اونجا بود که همه پشماشون ریخت از حجم اطلاعات و سواد آقا مجتبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/147414" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e22382ecd.mp4?token=CGmiaY71rqMdD2ci3_NK_29nDwb92R1R8GyR8AjWssHB9J--Cc0ThI_IaYDIQYuVY_vQUe9SIcwYbGs0thMvaK8cDTsHfyhgqesmxQoFaQYEtTvsz4S7S3vps76GHuJdiReQTB4Aiu7GAYFILWQkVI3sXFc_yYA9NJqczzcpnMzGbrRZd-ilU0CYNkOXDYYnheeyFo2mx9vXosDpNv-CQp4u14EXETN2TwGs_YMvsQURj3dVoDO3rwdOBBYj0Ql2Q-IE0RsdqdGOQQNRCZ1m2bG_wVGA9cLlY4TMQ0JVc2ktb66OwyOlmJjn3cOdfuO4bVKxdvZ4xFqv9aLIxUnhYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e22382ecd.mp4?token=CGmiaY71rqMdD2ci3_NK_29nDwb92R1R8GyR8AjWssHB9J--Cc0ThI_IaYDIQYuVY_vQUe9SIcwYbGs0thMvaK8cDTsHfyhgqesmxQoFaQYEtTvsz4S7S3vps76GHuJdiReQTB4Aiu7GAYFILWQkVI3sXFc_yYA9NJqczzcpnMzGbrRZd-ilU0CYNkOXDYYnheeyFo2mx9vXosDpNv-CQp4u14EXETN2TwGs_YMvsQURj3dVoDO3rwdOBBYj0Ql2Q-IE0RsdqdGOQQNRCZ1m2bG_wVGA9cLlY4TMQ0JVc2ktb66OwyOlmJjn3cOdfuO4bVKxdvZ4xFqv9aLIxUnhYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک بیمار سرطانی: شب‌ها که پرچم تکون میدید اصلا حواستون هست که ما دارو نداریم و داریم میمیریم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/147413" target="_blank">📅 18:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7f9d91bae.mp4?token=QfECycaKqdmzddHm7TxutJmIOpPsiwSLBKAh1BM3xuFzTfC7ZPXU79oZw6LtNpWO4dAyWMFVI_M7jMVWmEduUq-vvQqgSs08cAfdTI_4t5WrcAYS_7TwVACqgdce8z4cIEvuJCoZ-XVfjtLWDFWpkU-hkjao8Slp0bqqAPVD2HJT7rx4ghK_CM37K08OvnSsGRCNUwv-g4xyEyvF5gQGDuGI8oPWNn4cJCy2Gzz5vMdD65ZP07TvEW-nLhMz_5oBUk3DQzCxARO9wgDZlpGTpJEFDSWb6ACJO7BSHA7mOEoMKLA1k2Scwny3zax8t-Lm37u-ZJ-Tw_yEBqblbe_lbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7f9d91bae.mp4?token=QfECycaKqdmzddHm7TxutJmIOpPsiwSLBKAh1BM3xuFzTfC7ZPXU79oZw6LtNpWO4dAyWMFVI_M7jMVWmEduUq-vvQqgSs08cAfdTI_4t5WrcAYS_7TwVACqgdce8z4cIEvuJCoZ-XVfjtLWDFWpkU-hkjao8Slp0bqqAPVD2HJT7rx4ghK_CM37K08OvnSsGRCNUwv-g4xyEyvF5gQGDuGI8oPWNn4cJCy2Gzz5vMdD65ZP07TvEW-nLhMz_5oBUk3DQzCxARO9wgDZlpGTpJEFDSWb6ACJO7BSHA7mOEoMKLA1k2Scwny3zax8t-Lm37u-ZJ-Tw_yEBqblbe_lbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
باجناق برای سرقت طلاهای خواهرزنش، دو سارق اجیر کرد!
🔴
در تهران، مردی که از وجود طلاهای خواهرزنش خبر داشت، برای سرقت از خانه او دو سارق اجیر کرد.
🔴
سارقان پس از ورود به خانه، دست‌وپای فرزندان خواهرزن را بستند و طلاها را برداشتند؛ اما در همان لحظه، صاحبخانه به خانه رسید و سارقان گرفتار شدند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/147412" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
زکریایی، کارشناس حکومتی: حکومت امیرالمومنین هم فاسد بود پس انقدر به ما گیر ندید
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/147411" target="_blank">📅 17:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
انفجار در تنگه هرمز بر اثر شلیک موشک
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/147410" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147409">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b278137e.mp4?token=rM5-2ECpuXyskuZ4inFg3FvKanzkBxuKK0YeRQ5LdFxEeeG67pLvrzXMcxbFkxDEddd615IxXVGaquZT1W3zKawi70magdBaPhds9pmpexyu01uzepgb9HO7SxlZJW02FyUgTLrdiL8HHQiRsifB5cvy0ZfIPdOgrQNUYsDMy16PjVvWQCKdXrwpV0Z6R52U8rR7luAIGu5smfETnlnDm_tFhLDAMjQNji8wW7cIUoaMRxnjOaosCrknDGFIWvkOM-C5vv7nEW-__qnwFsi44gPW_0gIkWAmnEP9bIHMpaZuP7m9R52L8k4EBejsCs4RQ8CDa03anoAauoLqssmHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b278137e.mp4?token=rM5-2ECpuXyskuZ4inFg3FvKanzkBxuKK0YeRQ5LdFxEeeG67pLvrzXMcxbFkxDEddd615IxXVGaquZT1W3zKawi70magdBaPhds9pmpexyu01uzepgb9HO7SxlZJW02FyUgTLrdiL8HHQiRsifB5cvy0ZfIPdOgrQNUYsDMy16PjVvWQCKdXrwpV0Z6R52U8rR7luAIGu5smfETnlnDm_tFhLDAMjQNji8wW7cIUoaMRxnjOaosCrknDGFIWvkOM-C5vv7nEW-__qnwFsi44gPW_0gIkWAmnEP9bIHMpaZuP7m9R52L8k4EBejsCs4RQ8CDa03anoAauoLqssmHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار کرمی:
نیروهای دلتا فورس پس از هلی‌برن در اصفهان از ما ترسیدن و فرار کردن
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/147409" target="_blank">📅 17:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147408">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9132eb650.mp4?token=njaxi3r5SDn0v_R-acwZsSTI4EJPq1yKIhWTWBFxPps3i_cq9RTHrL6MFiS8nNDUHuXpnWbb7rXE9CH7BPGFLhqWTvVG3KWPos0OxemPM1f2VMf1zkF1eaIDpKtRfyZTsm-dKA8kpq2dW1XlkzjfcGuLATovaW4uYbdJvJRwmNyoZ6cwxE3Kr3yFcLofwSLvhc-jlFyvDlKHHgMq6jhsNyP3VtoW-zeFiCIxRtsj3PrOsIvwjlxdb1rZeKTE48FQ6jaAGIO-3QzHs7ZXb_CdL7Qhnwt853pMf47QFcMNfgRLRpzr5cAMJrp1TaRxDK0tNi01e0mkG8VllSRFHw_seg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9132eb650.mp4?token=njaxi3r5SDn0v_R-acwZsSTI4EJPq1yKIhWTWBFxPps3i_cq9RTHrL6MFiS8nNDUHuXpnWbb7rXE9CH7BPGFLhqWTvVG3KWPos0OxemPM1f2VMf1zkF1eaIDpKtRfyZTsm-dKA8kpq2dW1XlkzjfcGuLATovaW4uYbdJvJRwmNyoZ6cwxE3Kr3yFcLofwSLvhc-jlFyvDlKHHgMq6jhsNyP3VtoW-zeFiCIxRtsj3PrOsIvwjlxdb1rZeKTE48FQ6jaAGIO-3QzHs7ZXb_CdL7Qhnwt853pMf47QFcMNfgRLRpzr5cAMJrp1TaRxDK0tNi01e0mkG8VllSRFHw_seg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پروازهای مکرر و گسترده هواپیماهای جنگی سعودی بر فراز شهر طائف.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/147408" target="_blank">📅 17:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147407">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/147407" target="_blank">📅 17:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس: لاریجانی زندس
😂
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/147406" target="_blank">📅 17:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147405">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckWfRYSLHmPmDtLa4JYI-Su06MU5HoHTMJoQIEHHcHLpmWJ_lLnVdjCogP4dps1gD4_leSyh9Ufb1PD8iQc5-CcKmnLyFYhM7SRDTwJQjgQitizAL0nP8eHbz0oH-HVgEzip9bkk9kdpCzYWVeyFupkm6EYOrhwzyMQOjsKgXQAOBG2Cyf8UZYkTUcrtXHeaDN_wmyXeGewZKmsSJCv5Y3Mx7Vr-N3cBI-r_bV0W2P6yyxo2fGphi0431ldY9tkCCMaTse0xgMIVM881FB-xg6BHwSr8wtf6HE-MKesGSsQgW_8QDvGUde85Cz7zHj7-VmoYQbunwHVdi-YGcKgZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری معتبر فارس:
روایت آمریکا جعلی است و هیچ خلبانی نجات پیدا نکرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/147405" target="_blank">📅 17:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147404">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55f910667.mp4?token=QcxqvzlospsY6Wvvi_chHUOPv6SV5MQ3nGTcViuD4SK23gQxUJq6doETLRNk1KUBN2bD01YALvhGzIN2U5HsxSMuNtT_x34oCIb4rWCMkc-h52rUaePdko9iQJlCqWyK-uoj2kupzp3_GFbN5vieWlQwp8z2qD1DTlVSGu2SKhqRqQR55lBIhTVDJPERI_GBglTUGSIl9wEhYmW1Psx7nRDjXs5NVdG1lVVLuFxK0HJ2lYfCEvl6es6yFuk4iYcaL_aovW6w8bxI81_eSso-iHtXLI1DKdmZ9KofbaT4o5rE4RQBAIQjdgTkasYBNpUETUsIFylN_K09P-kt7GHyQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55f910667.mp4?token=QcxqvzlospsY6Wvvi_chHUOPv6SV5MQ3nGTcViuD4SK23gQxUJq6doETLRNk1KUBN2bD01YALvhGzIN2U5HsxSMuNtT_x34oCIb4rWCMkc-h52rUaePdko9iQJlCqWyK-uoj2kupzp3_GFbN5vieWlQwp8z2qD1DTlVSGu2SKhqRqQR55lBIhTVDJPERI_GBglTUGSIl9wEhYmW1Psx7nRDjXs5NVdG1lVVLuFxK0HJ2lYfCEvl6es6yFuk4iYcaL_aovW6w8bxI81_eSso-iHtXLI1DKdmZ9KofbaT4o5rE4RQBAIQjdgTkasYBNpUETUsIFylN_K09P-kt7GHyQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسئولین طبق معمول دروغ گفتند
‼️
🔴
نیکزاد، معاون مجلس،مدتی قبل: آمریکایی‌ها برای خلبان نیومده بودن،اومده بودن اورانیوم ببرن که بازم شکستشون دادیم
🔴
اما دیشب ایالات متحده فیلم نجات خلبان رو منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/147404" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147403">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / لحظاتی پیش دفتر نتانیاهو اعلام کرد:
نتانیاهو هفته آینده به آمریکا سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147403" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147402">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2436eef8.mp4?token=omY-BYuiNv0-vWGLKiqe-TFba6wlSA0cKjbU4WXUktWfmw6Pl7Qhh3RB_HZqCxCkwj3Qfi7_X70o01uBGeHTbqxwkeaqYKV1ugk8dppZ4aR70aziq2n9yQHPHogM1iqWtXhRx09k9nJgWosQ05nwj8fuQuBwc6ew3_bmpwFp1zqAljYfKTRQWIfitJ9EYwhzjIyPZqEMssgPyEGbw24TqHDnfb1UtCrPpTXQ8S3-NLG8Ln3LfMWVsn0AUuOiqSH2OFmiwOR5mSzXOgz1GBhoDbrzS6pP6gliNmwbvgHj-KUqocBXzg07YN7qJYcUhCuVtNDf3iscK3BIzeN7qcz-7X44NdW4tSMDWmr60Q6dWutJcBCXM7BrzxmNQ0vY-iaoH6Y41QIACvbpz8-v9aNjOWcY2v9h2-HLZVxDjtUW2zHmH7PQYZt64Bu4nhX4FrGd5P3mkXjkmGZpg58ZlG93SMLt6lcndLJk1DnY98ZY4YcvKIgWqIdPJ0HE56BQC0yR2y8DI2Oxd0FIJz9HyH-wBTgnFfDhyCdd_vfmPiHUhIZakkym-TmUL9ps4ZG8GsizmFJTLK1HNvhmY14KM_Bp7DRAVVjmBNIPD3mA70GRMyq_cbU24W0aCBgZYWXNIgeEeaXMaSqcDUU2pQclQGdSx5qk97sQXXuESs4kM3I0wTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2436eef8.mp4?token=omY-BYuiNv0-vWGLKiqe-TFba6wlSA0cKjbU4WXUktWfmw6Pl7Qhh3RB_HZqCxCkwj3Qfi7_X70o01uBGeHTbqxwkeaqYKV1ugk8dppZ4aR70aziq2n9yQHPHogM1iqWtXhRx09k9nJgWosQ05nwj8fuQuBwc6ew3_bmpwFp1zqAljYfKTRQWIfitJ9EYwhzjIyPZqEMssgPyEGbw24TqHDnfb1UtCrPpTXQ8S3-NLG8Ln3LfMWVsn0AUuOiqSH2OFmiwOR5mSzXOgz1GBhoDbrzS6pP6gliNmwbvgHj-KUqocBXzg07YN7qJYcUhCuVtNDf3iscK3BIzeN7qcz-7X44NdW4tSMDWmr60Q6dWutJcBCXM7BrzxmNQ0vY-iaoH6Y41QIACvbpz8-v9aNjOWcY2v9h2-HLZVxDjtUW2zHmH7PQYZt64Bu4nhX4FrGd5P3mkXjkmGZpg58ZlG93SMLt6lcndLJk1DnY98ZY4YcvKIgWqIdPJ0HE56BQC0yR2y8DI2Oxd0FIJz9HyH-wBTgnFfDhyCdd_vfmPiHUhIZakkym-TmUL9ps4ZG8GsizmFJTLK1HNvhmY14KM_Bp7DRAVVjmBNIPD3mA70GRMyq_cbU24W0aCBgZYWXNIgeEeaXMaSqcDUU2pQclQGdSx5qk97sQXXuESs4kM3I0wTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا: هیچ برنامه‌ای برای غنی‌سازی اورانیوم در عربستان سعودی وجود ندارد.
🔴
او گفت توافق همکاری میان آمریکا و عربستان بر ایجاد صنعت تجاری انرژی هسته‌ای در عربستان متمرکز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/147402" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147401">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=Nu-65V2Re7Z2RLUfFp1lb9FETUMqp6xmsc4tH4_DiI_SKoyynrbQvQzdxyfaeEPm-ItwBk1tqGJzh5mOWPszQhe3buibef19RzZNexG6gY6XcQcxpjfdlnHBW9RSQ3WaUeDh1PtnmfORuyD7GxIyIbLMutWzv4wr5LbgyIEdoknwLkCWBg_PYUwmI9soL6KOwYySpe_n0r9L2UQxylN-yjIkkk4ExwZVaapKhBxdAqUcs12e5orRDytVj7QsMKp9LBNngtlffhHxORIecth85cBS1IrWCGxoGltFqs3jfPi1d1JRxSt6S8Y-D5WGehgk7X5m8nb09ewWTHKfyRk7piSezQEg1PRQtETigvY2e0lhw8ouTgYzfYsjUgG5x5QVPvVBkXJWcZ9orCORQHRKL97dO1nPbIaVClt2iKo0wbC3uCJQTpoAv0YT9LVU1NjDm7uPWK6BUXwMHvfncyLuAgsfKR0AhzyTXUrKV7hQb4AQj4PZXT6d3eLXk8fn32nqCUZuOYIzrwIxno86RD19c1zI4T82yWZe9DJaN2f6nXenAXLVRgEgh4Q5drBfEPjuYlTnO0ZkDXFFp1TQ1Q4pUXDif-ovyOTe8YhXSn5RL6cZSRPcaMEKUHFrtTUezt7lkvdytGrmNVsIQwhiIw2boJlJfebohGhHHRjUat1x554" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=Nu-65V2Re7Z2RLUfFp1lb9FETUMqp6xmsc4tH4_DiI_SKoyynrbQvQzdxyfaeEPm-ItwBk1tqGJzh5mOWPszQhe3buibef19RzZNexG6gY6XcQcxpjfdlnHBW9RSQ3WaUeDh1PtnmfORuyD7GxIyIbLMutWzv4wr5LbgyIEdoknwLkCWBg_PYUwmI9soL6KOwYySpe_n0r9L2UQxylN-yjIkkk4ExwZVaapKhBxdAqUcs12e5orRDytVj7QsMKp9LBNngtlffhHxORIecth85cBS1IrWCGxoGltFqs3jfPi1d1JRxSt6S8Y-D5WGehgk7X5m8nb09ewWTHKfyRk7piSezQEg1PRQtETigvY2e0lhw8ouTgYzfYsjUgG5x5QVPvVBkXJWcZ9orCORQHRKL97dO1nPbIaVClt2iKo0wbC3uCJQTpoAv0YT9LVU1NjDm7uPWK6BUXwMHvfncyLuAgsfKR0AhzyTXUrKV7hQb4AQj4PZXT6d3eLXk8fn32nqCUZuOYIzrwIxno86RD19c1zI4T82yWZe9DJaN2f6nXenAXLVRgEgh4Q5drBfEPjuYlTnO0ZkDXFFp1TQ1Q4pUXDif-ovyOTe8YhXSn5RL6cZSRPcaMEKUHFrtTUezt7lkvdytGrmNVsIQwhiIw2boJlJfebohGhHHRjUat1x554" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: ایران می‌گوید آمریکا در جلوگیری از حضور محمد اسلامی، رئیس سازمان انرژی اتمی ایران، در کنفرانس عمومی نقش داشته است.
🔴
کریس رایت، وزیر انرژی آمریکا: او یک فرد تحت تحریم است و ما نمی‌خواهیم افراد تحریم‌شده از تحریم‌ها فرار کنند. او درخواست معافیت از تحریم‌ها را مطرح کرد، اما این درخواست رد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/147401" target="_blank">📅 16:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147400">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38918bdab.mp4?token=LcXhtDAnbUrgYvJYkkJ37vGjx9_30wywbbrkg2XzUvtqEc9ME4yk1pI4pvbpINntRnSy0QRx0ghaceN7xiXDYHZrkWAEVX37VwC-DJCc8N6QMlT16zZCr96S-CN3iVSvDTrubUn-PEsJMIpZRsfG7O_aBH-0jhid5WD9mEFQsHiaz3-w2b2sQBjN6R7U0QC-NxDtFOeRXPtxPFsTSzx08jEVcOMzcNq0pC0l9ETjcDee6VH_pc60FWEntPNLpJL37ATIzihq_e7SnfKVhbedqp96qy5qbqMnUX4dSvlHDjz6Rizvn-7u6z19oktPAzscs-H2qbg9UlJdZU2jPYDl_pKsze1PmK_XZ74WjQ7yIrS3JOeFiKQsae54BcEuX7Br0aaUwIKpV9h6G2o6hSwzysZD6mUXTW3UC89UcuPXTqtojwOeVUu3u_aFmsHn_oqT-DJJUSLxaJcl1KHZubiN4ZRH989B6j5mWxijymq7jvicUJNGruL7JBr1mpDJrHrGECjAjU9NjsNVbCJCKRek54XRQCYdJCSwbHQiqPfmdCIRv10byeDQihVSMjQg6IuFw_SLV8yK4VNCRZHByM6Lh0kvOilomIpD546Er4g6-4VHFng35A5cQCya5sNkC6jHnmitPHnpAd3bEeClBUGkQ1vKhcy9K3NFrWe91LVWK7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38918bdab.mp4?token=LcXhtDAnbUrgYvJYkkJ37vGjx9_30wywbbrkg2XzUvtqEc9ME4yk1pI4pvbpINntRnSy0QRx0ghaceN7xiXDYHZrkWAEVX37VwC-DJCc8N6QMlT16zZCr96S-CN3iVSvDTrubUn-PEsJMIpZRsfG7O_aBH-0jhid5WD9mEFQsHiaz3-w2b2sQBjN6R7U0QC-NxDtFOeRXPtxPFsTSzx08jEVcOMzcNq0pC0l9ETjcDee6VH_pc60FWEntPNLpJL37ATIzihq_e7SnfKVhbedqp96qy5qbqMnUX4dSvlHDjz6Rizvn-7u6z19oktPAzscs-H2qbg9UlJdZU2jPYDl_pKsze1PmK_XZ74WjQ7yIrS3JOeFiKQsae54BcEuX7Br0aaUwIKpV9h6G2o6hSwzysZD6mUXTW3UC89UcuPXTqtojwOeVUu3u_aFmsHn_oqT-DJJUSLxaJcl1KHZubiN4ZRH989B6j5mWxijymq7jvicUJNGruL7JBr1mpDJrHrGECjAjU9NjsNVbCJCKRek54XRQCYdJCSwbHQiqPfmdCIRv10byeDQihVSMjQg6IuFw_SLV8yK4VNCRZHByM6Lh0kvOilomIpD546Er4g6-4VHFng35A5cQCya5sNkC6jHnmitPHnpAd3bEeClBUGkQ1vKhcy9K3NFrWe91LVWK7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوالات عجیب خوش چشم در آنتن زنده بعد از ممنوع التصویری: بلبل دارین اینجا؟ مگه باغه؟ صدای بلبل میاد!
🔴
چرا روکش صندلی نو رو نکندین؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/147400" target="_blank">📅 16:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147399">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGcQdmrufNNMXnJ7QmYNm6j2OfEmPe84XmThTKyQJj7-LMCmBlKrydDV7UZJZb2lImW0gbIo8WrOzsHlCr1aqS9EMGhqpaJyu7JKp2MNDBdbfRddFCAREKFcRKMUDJHylyU6qYGJmNNb4dDYOM39NFLT4Pe7ulBp3fuzqTkEoPyrpIWSbq2GRMPpbNq7slew3Pad7_MRz5nzEjEfnfZXwxChhnWngnDxpN6tWlSSKeKZCiT2O81obDROjFsKDLTuImvJaRKj63sAIPWqbRi3ai_SazoCxMWzplcr4Y872O3Y1c5GSKdUkLBRqt044l9YFthAQ7kP3M3IwWYUx3NZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو تهران (ونک) یه غذاخوری افتتاح شده به اسم کتلت بی بی که فقط تخصصش  کتلت درست کردنه
🔴
حالا قراره به دلایل نامعلوم پلمپ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147399" target="_blank">📅 16:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147398">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22435ecca9.mp4?token=p8xNSGcoT9mqRbUxIygK3NUfQ1kGxQoVnbqxiwfVxVhvDt97DwhOHVoLE_Cfv4bT7482TNq666ho7Zwmx6j7vj6wuVjcCcuR0cwaMBDY_Rz-ngNNBeKIbKw6CLJa4rTUcbr6G2befG63QfHKj7cumBIyrBmzv28FSTLZB5Q1I4Dqs0ydiQ2vwyU8g_gaVTb4n8Ygr71wdShiNOTU_eFhrj8XIgiTfvu-9xGkz6eGhUtHzav1rG8hoQ58-MPL6Ab6pVMwtt9_lyBGvyc3osVF-_WWY3STZfe84T8y0OBbJpecil_W3UDy5jcUAyynYK8nGufn4BDfy59kP4fPPNsU8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22435ecca9.mp4?token=p8xNSGcoT9mqRbUxIygK3NUfQ1kGxQoVnbqxiwfVxVhvDt97DwhOHVoLE_Cfv4bT7482TNq666ho7Zwmx6j7vj6wuVjcCcuR0cwaMBDY_Rz-ngNNBeKIbKw6CLJa4rTUcbr6G2befG63QfHKj7cumBIyrBmzv28FSTLZB5Q1I4Dqs0ydiQ2vwyU8g_gaVTb4n8Ygr71wdShiNOTU_eFhrj8XIgiTfvu-9xGkz6eGhUtHzav1rG8hoQ58-MPL6Ab6pVMwtt9_lyBGvyc3osVF-_WWY3STZfe84T8y0OBbJpecil_W3UDy5jcUAyynYK8nGufn4BDfy59kP4fPPNsU8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بالگردهای آپاچی عربستان سعودی مواضع و تجمع نیروهای حوثی‌ها را در نزدیکی باب‌المندب هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147398" target="_blank">📅 16:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147397">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ماهواره چینی که در فضا به ایران داده ارسال میکرد، به دلایل نامعلوم(آمریکا) منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/147397" target="_blank">📅 16:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147396">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=f1ZuVA4H-KHrN_LHL20eLxCJrFgIa-p65VYXN4j30e3ebhIocwWpUkb_io0MBXBSihGicNNZ2xKkVbzzO4uNYTE_m4DjqlbjQHWZh8uCck0w7XRpEYykgI7W3ej_xiPzrmSWvDOOcp-UZV0mtF1NSnIpHqGbUAFk9o-cnRxkgGe0uTNjOW5Gfxt0b7yDzUsr1zyjB7YrVbjN1TWW6J7oiOEVMbf4hgTWSo0btKlhfC6MC3nwXCGjT4-bkVF9Ynw1itCjsNI_I3OMJNztyXN-xSNWvLkHpD_HYYlo81hcorIiZMqrrjfxPqz0icIjQKLrYx2saZGgWkR2s5ySewG6Eg4xIK6cWZjJxsAClA1KGmoSeP1x-b2reWadXasNQtXrwDHddear7IIFhLS1Wu31gq0VweXjF6RPStLM7XkUJk-amcNm49Mh3IpIw6uNBxfGm3_DFEaM6s3PP9D3anaPxwcr1HQk16myPp9zXXqp2mbg3EDAUpKZaSqBa17xOMA3P9mjJz8FcstwY1K8RuOIfHQPqnZK_c37ogaZy0ZPIcpD0UkDJTMIv0TfB6UAOCMbSdb541a9ZsCNcZx0_07-BEGFujVSOdmRF3UkoF6eJUd5CtUpw02RqgVbJPjqx8AIr9wrG6Wyy5yKqTIJbV5-8QwJ_tp-OXxbo6s1bYlF_AU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=f1ZuVA4H-KHrN_LHL20eLxCJrFgIa-p65VYXN4j30e3ebhIocwWpUkb_io0MBXBSihGicNNZ2xKkVbzzO4uNYTE_m4DjqlbjQHWZh8uCck0w7XRpEYykgI7W3ej_xiPzrmSWvDOOcp-UZV0mtF1NSnIpHqGbUAFk9o-cnRxkgGe0uTNjOW5Gfxt0b7yDzUsr1zyjB7YrVbjN1TWW6J7oiOEVMbf4hgTWSo0btKlhfC6MC3nwXCGjT4-bkVF9Ynw1itCjsNI_I3OMJNztyXN-xSNWvLkHpD_HYYlo81hcorIiZMqrrjfxPqz0icIjQKLrYx2saZGgWkR2s5ySewG6Eg4xIK6cWZjJxsAClA1KGmoSeP1x-b2reWadXasNQtXrwDHddear7IIFhLS1Wu31gq0VweXjF6RPStLM7XkUJk-amcNm49Mh3IpIw6uNBxfGm3_DFEaM6s3PP9D3anaPxwcr1HQk16myPp9zXXqp2mbg3EDAUpKZaSqBa17xOMA3P9mjJz8FcstwY1K8RuOIfHQPqnZK_c37ogaZy0ZPIcpD0UkDJTMIv0TfB6UAOCMbSdb541a9ZsCNcZx0_07-BEGFujVSOdmRF3UkoF6eJUd5CtUpw02RqgVbJPjqx8AIr9wrG6Wyy5yKqTIJbV5-8QwJ_tp-OXxbo6s1bYlF_AU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ایران اعلام کرده که ایالات متحده در جلوگیری از حضور آقای اسلامی، رئیس سازمان انرژی اتمی، در کنفرانس عمومی دخالت داشته است.
🔴
دبیر ویراایت: ایشان فردی هستند که تحت تحریم قرار دارند، و ما نمی‌خواهیم افرادی که تحت تحریم هستند، از این تحریم‌ها فرار کنند. ایشان درخواست معافیت از تحریم‌ها را ارائه دادند، اما این درخواست رد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147396" target="_blank">📅 16:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147395">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce9a0183a.mp4?token=u7LGT1m6tqHbJEffyhs_o3yd4xz9I0SbejxQ_rQ0yrg8tlUFAPc7EeV4lnOUtTuAm-uoaoBb5GCdxZiDA-Vims1asUULX5rjC6svU0QckXDFYV2Hb_1ydvQvnzqU2Kf33-LfaJX3VV7xcQCD1_4JwyH6CrQtZsM6aQjRdNM37IkumTN1ddknj-mEkE5fjYDCt2c-mqcMnll6BFLBJdctmZj1VzsaqUs5hMv-KqMtGYIax7Pare17_C1fmuuNpJz6NmJkDHZmh8m5Fvd2aUzQUFZcftzmUcmAEXd70oPYIF9aQVDGSY_z21Jj5G-p9mmYwIs6c6LhX-10YR5bNhfvlDdXW32b9E0Q-AFhnrshtkZ2M5CfKFJm79L15tnAHUBoUGG7y_oI89jxWXn1NRZex9_hk2m-qeY82Wn1EwZo7mwNXAHbYvYQYt-KKlQgm0WZ7oNe8C8th6OARqCriVmcPI2S37rrLBsqKN3TBTGMg513BnUSEjAkvSrV30NeE2CMslXltdNNdV_tKSxp6BaekHNa3Ui_hLtEd0P3XPVTpVq-xWs_3uIHFTNwwl2xh0wLvTK0nfVYTuN50HkcQ835IOa_Xl4Myoh0Z--XH46XYgzsBcRT0wbTGITTkeq38giUJ7l1XwPVYcF5vPKbgJytJ8jew2V3Xml9dHFfm8UB3CU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce9a0183a.mp4?token=u7LGT1m6tqHbJEffyhs_o3yd4xz9I0SbejxQ_rQ0yrg8tlUFAPc7EeV4lnOUtTuAm-uoaoBb5GCdxZiDA-Vims1asUULX5rjC6svU0QckXDFYV2Hb_1ydvQvnzqU2Kf33-LfaJX3VV7xcQCD1_4JwyH6CrQtZsM6aQjRdNM37IkumTN1ddknj-mEkE5fjYDCt2c-mqcMnll6BFLBJdctmZj1VzsaqUs5hMv-KqMtGYIax7Pare17_C1fmuuNpJz6NmJkDHZmh8m5Fvd2aUzQUFZcftzmUcmAEXd70oPYIF9aQVDGSY_z21Jj5G-p9mmYwIs6c6LhX-10YR5bNhfvlDdXW32b9E0Q-AFhnrshtkZ2M5CfKFJm79L15tnAHUBoUGG7y_oI89jxWXn1NRZex9_hk2m-qeY82Wn1EwZo7mwNXAHbYvYQYt-KKlQgm0WZ7oNe8C8th6OARqCriVmcPI2S37rrLBsqKN3TBTGMg513BnUSEjAkvSrV30NeE2CMslXltdNNdV_tKSxp6BaekHNa3Ui_hLtEd0P3XPVTpVq-xWs_3uIHFTNwwl2xh0wLvTK0nfVYTuN50HkcQ835IOa_Xl4Myoh0Z--XH46XYgzsBcRT0wbTGITTkeq38giUJ7l1XwPVYcF5vPKbgJytJ8jew2V3Xml9dHFfm8UB3CU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی ایالات متحده، درباره ایران:
امروز، میزان متوسط نفت و فرآورده‌های نفتی که از طریق تنگه هرمز به دریا منتقل می‌شوند، تا 10 میلیون بشکه در روز است.
🔴
شما خواهید دید که این رقم در هفته‌های آینده افزایش خواهد یافت. و اگر جریان نفت از خطوط لوله فرعی را هم به آن اضافه کنیم، میزان انتقال انرژی از این منطقه به 13، 14 یا 15 میلیون بشکه در روز می‌رسد.
🔴
بنابراین، بخش قابل توجهی از میزان انتقال نفت قبل از درگیری، که هنوز به طور کامل به حالت قبل بازنگشته است، همچنان با پیشرفت بسیار خوبی ادامه دارد و ما به این روند ادامه خواهیم داد.
🔴
حالا نوبت ایران است که صلح را به این منطقه بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147395" target="_blank">📅 16:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147394">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dfbb346a9.mp4?token=hAkCCsJsexVUd01wqtsY9_0WNM0ZG-KVBUfPQ7QGtzciJxOLt486gQow4-UPawO1MYJUX4bNfipSKVOszclYuG5BIBFTWk_0BXkHIzkWmgDpQDrzYsFz0allc-EKOP_11iqph32j7-uMpLsUDFWN7JE5NSOIT_ZjfqeCF4qtl_Aj0bWjiTwhYZJgDM203BGwfpZ1SqnLPSGJaacp_hvb2nzHK2qc7CzmE2gggJ9frEB-2uZh5fZhpqJqkXXinPdXwoFh2ttvhVdPEh_o9nsxWlHJgC8K4g56mDvTqVvfHghySleNXYHBj2O-URPsV34wpyFi454razcmGwtPYAZppp02qKtslfXcjvzc5IzBzztE73BrNthvr6NNGM4CIFmCtf7hhJ-cTSq07-GfVbPQ8WMgYOm-o68jqR9Qph8nm1kLXkcPROvjfVTUnl57aStp9rayMIG6n1QKCQ9VK4457rbyqrNudCexwf1Zo_4DQ-HlSbJiF5yc6lgVmI9rDyoSZ-UAVXoo19k6MTIL_HrxhmI0oVNPH2DhlgNyCvj_lWdDc6TEnwu8xQ-WdCpw-_hmjgZ81UWObHfdwnC7dm58A7M_JqbpskaCk-l3Sd-9XDj9SCShaHTYXR0AInA2exO7xYLj5KLi1jhxlEwrHRjozrvZ4K05JzXcLyXDGuSeVGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dfbb346a9.mp4?token=hAkCCsJsexVUd01wqtsY9_0WNM0ZG-KVBUfPQ7QGtzciJxOLt486gQow4-UPawO1MYJUX4bNfipSKVOszclYuG5BIBFTWk_0BXkHIzkWmgDpQDrzYsFz0allc-EKOP_11iqph32j7-uMpLsUDFWN7JE5NSOIT_ZjfqeCF4qtl_Aj0bWjiTwhYZJgDM203BGwfpZ1SqnLPSGJaacp_hvb2nzHK2qc7CzmE2gggJ9frEB-2uZh5fZhpqJqkXXinPdXwoFh2ttvhVdPEh_o9nsxWlHJgC8K4g56mDvTqVvfHghySleNXYHBj2O-URPsV34wpyFi454razcmGwtPYAZppp02qKtslfXcjvzc5IzBzztE73BrNthvr6NNGM4CIFmCtf7hhJ-cTSq07-GfVbPQ8WMgYOm-o68jqR9Qph8nm1kLXkcPROvjfVTUnl57aStp9rayMIG6n1QKCQ9VK4457rbyqrNudCexwf1Zo_4DQ-HlSbJiF5yc6lgVmI9rDyoSZ-UAVXoo19k6MTIL_HrxhmI0oVNPH2DhlgNyCvj_lWdDc6TEnwu8xQ-WdCpw-_hmjgZ81UWObHfdwnC7dm58A7M_JqbpskaCk-l3Sd-9XDj9SCShaHTYXR0AInA2exO7xYLj5KLi1jhxlEwrHRjozrvZ4K05JzXcLyXDGuSeVGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریستوفر رایت، وزیر انرژی ایالات متحده، درباره ایران: ایران یک انتخاب دارد. آن‌ها یک انتخاب دارند.
🔴
آن‌ها می‌توانند به جامعه بین‌المللی بازگردند و صلح، فرصت و شانس رونق را برای ۹۰ میلیون شهروند خود به ارمغان آورند، رشد اقتصادی و رونق را به منطقه بیاورند.
🔴
یا اینکه می‌توانند به تلاش‌های فریبکارانه، پنهان و شوم خود برای توسعه سلاح‌های هسته‌ای ادامه دهند، که در نهایت موفق نخواهند بود
🔴
آن‌ها در طول دهه‌ها، با این اقدامات، آشوب اقتصادی، مرگ و ویرانی بزرگی را به منطقه وارد کرده‌اند
🔴
اکنون زمان آن است که ایران انتخابی داشته باشد. آن‌ها کارت‌های زیادی در دست ندارند، و ایالات متحده پیشرفت‌های چشمگیری داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147394" target="_blank">📅 16:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147393">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: با تصمیم دولت، وزارت آموزش و پرورش مرجع تصمیم گیری درباره تعطیلی مدارس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147393" target="_blank">📅 16:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147392">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) چندین خانه را در منطقه طیری در مسیر حداثا در جنوب لبنان به آتش کشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147392" target="_blank">📅 16:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147391">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیر انرژی عمان : احتمالا بزودی تنگه هرمز باز خواهد شد و وضعیت فعلی کوتاه‌مدت خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147391" target="_blank">📅 15:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147390">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a18fd106d.mp4?token=YuWiBromjCkkN2I-eY3G64SiW0AHDgzlgKBelMz8ysLOn6QkpWDw4isgHvh7YYp2xGCSkNdb1z3-1oVi6jg3FxAbQ09itt60AtjqDrdxa95YnSgcbpO5uVaeFQ7BAYXn0gdBonoePgPOK-AvypyQU0rgP1wCEgT_m5H017tbrnmpWogkK92jkZoRDYfRuA-2_1q0TgaQpQDC0doWFRv29xZqzn-geB5KCYz9jxwY8yQO3EcqRSmRveYMtNsoqsUxUgyquGZn0xpatMDcyGg3HCtZJTK9PI6j85BrJTasKvZ4oaH1CwpVQcaveKcrEcLsCv-sXCUgzyWInJV_XRFwippc9w4D9kRlHX02R_KHvlmat_hdYVCZI3X7E1sVwM1EmQfjwDEpreXzmtkobjc9wjArAxE-rLdbhKKrUEyC7KW41xZXi5QfITQEePk_Wbg6AKO_ILLp9aRDdYHZRUeLcue6qPlkqeZ7OGH3GFSPrlRPA_IdgXVz099exnAWJlQ4CgkOuy23L8jWwXawSIUQlrJXRFEIUpK9Y_8OcZZvDLDuXErCdbnJ6cpsIVfq9vciG3bAzVUtyszOT6YNGo_SVzIVgwiV0IBXS1PtH66E1HLIoizeaX3HqDVAE0NG6-2-L-x68AvL69YK6BnjTZ-HvdR762MyR88sKAnpnYm-ex4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a18fd106d.mp4?token=YuWiBromjCkkN2I-eY3G64SiW0AHDgzlgKBelMz8ysLOn6QkpWDw4isgHvh7YYp2xGCSkNdb1z3-1oVi6jg3FxAbQ09itt60AtjqDrdxa95YnSgcbpO5uVaeFQ7BAYXn0gdBonoePgPOK-AvypyQU0rgP1wCEgT_m5H017tbrnmpWogkK92jkZoRDYfRuA-2_1q0TgaQpQDC0doWFRv29xZqzn-geB5KCYz9jxwY8yQO3EcqRSmRveYMtNsoqsUxUgyquGZn0xpatMDcyGg3HCtZJTK9PI6j85BrJTasKvZ4oaH1CwpVQcaveKcrEcLsCv-sXCUgzyWInJV_XRFwippc9w4D9kRlHX02R_KHvlmat_hdYVCZI3X7E1sVwM1EmQfjwDEpreXzmtkobjc9wjArAxE-rLdbhKKrUEyC7KW41xZXi5QfITQEePk_Wbg6AKO_ILLp9aRDdYHZRUeLcue6qPlkqeZ7OGH3GFSPrlRPA_IdgXVz099exnAWJlQ4CgkOuy23L8jWwXawSIUQlrJXRFEIUpK9Y_8OcZZvDLDuXErCdbnJ6cpsIVfq9vciG3bAzVUtyszOT6YNGo_SVzIVgwiV0IBXS1PtH66E1HLIoizeaX3HqDVAE0NG6-2-L-x68AvL69YK6BnjTZ-HvdR762MyR88sKAnpnYm-ex4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک کارنی، نخست‌وزیر کانادا: ما قصد نداریم که عضو اتحادیه اروپا شویم.
🔴
آنچه ما به دنبال آن هستیم—و بحث‌هایی را در این زمینه آغاز خواهیم کرد—یک ائتلاف منحصربه‌فرد با اتحادیه اروپا است، ائتلافی بین کانادا و اتحادیه اروپا
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147390" target="_blank">📅 15:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147389">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZEQsfCqzs9uB46S3B-OJ26fPcI67KsYEPRiy-H97G9ijHDNBEnOQ9iexW_7fRMBQma6o7KDCYQgg0GIlmozDtcPIEnQUc3__hXXzI2zE3ihW9z229rxInCyUQxy4W3-sLwoK2fFAH0KegZDO3lhpprdkyZQFF8AGLh5NvXfIIJyxYfFRDMJnXc8nUT0FqDMnlqypxfvepHBjSRVgov4pdNgy_W1rZqkGf9J1ehZQdOIs1IGztq6-oYV_p4oPPWKGMMLnjRiioWIa27DESVLLB0IR4vYgKj68YWlojniaVxpB9gxcyCKEx8bfB-SbDWAQsN6Dl7YcJfc2_VrPMcAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو انفجار در منطقه مجدل زون در جنوب لبنان، متعلق به اسرائیل، مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147389" target="_blank">📅 15:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyCgdqQz2ewulQmOhqJ1W7V5d5OOIICOx0wotfd6CIlqqZJQs_HgLOLKIUne0wTurF2Y5oWmHRI66QhRTth7BkqPysEvJ5omVUtVUe4-5YvJJA7EnVDXne_-3HtvoUvZRU_rnw9nUT2t-LEvZ4CWGPzO0DxAmAPhhwDf-GehWUR5tuCG-Z1LCpgsLl7hx5UmSSuGlilTy49D-qpy5krpiKVceirhAb55iK_QDA9Dym_-SX765trA1_0Eb2IADxVa6u07s9Mw6BJMjhv0zr1dQIHk--CBJhmqFEwfjz9UqEinv7SqLbQgSuPYYwz_JxurPz13Eg9zlP8FnkH2DupQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل، منطقه کفر تبنیت در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147388" target="_blank">📅 15:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147387">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
قیمت نفت برنت به ۱۰۸.۶۵ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/147387" target="_blank">📅 15:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147386">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دلار در تهران مجدداً از 235 هزار تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147386" target="_blank">📅 15:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147385">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: نفتکش‌ها شبانه از تنگه هرمز عبور می‌کنند و توسط نیروی دریایی آمریکا اسکورت می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147385" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147384">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4903cea3.mp4?token=Aw7QZC2jBv7f-yMxieRXU9VGT23d15rYDs5fuPxd2yBjgWJWpWOABzvVFYbzAsih_uAMU9ggYh7GY5Ps0Xfl7RubS0sixet57A6kUXVxTCqp9g7qM7V7p_RYRn5WDnvsdjKWzr74bkvmHoXeA8Y-vF0_per9z5ZfD0Jy3VMOMwY55ViB-MWg49Uy3zjMVC3amj2ukrbDa9emCK8g-7WsrfeeZvGLGYYHCD1bpEIbTkHq4qU8MBsHGpKZgk4p_c0iXeX0H3SgrPAH3zETP6I6UEi3KwvOGXiSfp_zl12r71pznr7DsNGECPBaZY134G0zaSf7s_zUbvozV0AcH8lrqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4903cea3.mp4?token=Aw7QZC2jBv7f-yMxieRXU9VGT23d15rYDs5fuPxd2yBjgWJWpWOABzvVFYbzAsih_uAMU9ggYh7GY5Ps0Xfl7RubS0sixet57A6kUXVxTCqp9g7qM7V7p_RYRn5WDnvsdjKWzr74bkvmHoXeA8Y-vF0_per9z5ZfD0Jy3VMOMwY55ViB-MWg49Uy3zjMVC3amj2ukrbDa9emCK8g-7WsrfeeZvGLGYYHCD1bpEIbTkHq4qU8MBsHGpKZgk4p_c0iXeX0H3SgrPAH3zETP6I6UEi3KwvOGXiSfp_zl12r71pznr7DsNGECPBaZY134G0zaSf7s_zUbvozV0AcH8lrqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: از پنجشنبه سامانهٔ بارشی جدید وارد کشور خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147384" target="_blank">📅 15:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147383">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3T2OEQrLgkSl8TZWWuPCmN8_H1cOMa7GWFqE4cxcr8qzqFZovPOqJIQQ0bQMRBMlOq6h1tIOjQu_PlWYFnq-Ak9GCE7C90GMs9tjQoazzyKFraGhYaRST6b_O802VaPYklScUIQMWKrEcLJJNjLKl8P-IcSK1K3IXnu_3QrE4PVElCkapNPPzk0hQChUb7Y8KRV8UbeE30azNdCi6d1MzKE2bfAoSJFH-ZIP1XR3mG9TW8952kPcZOtqesweiY-FDxR_oJw20s9IsJupc0BmJcVBdwF9SFL8hh1uK0sScQuJOXV5-rS5MKE1j6GVO-ZjZfcemUg5dqgVUC8vFwfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع دیپلماتیک غربی به شبکه خبری "ال-شرقیه" اعلام کردند که عراق هشدارهایی را دریافت کرده است مبنی بر اینکه ممکن است به عنوان یک کشور حامی تروریسم شناخته شود، به دلیل حملات و تهدیدهای مکرری که از خاک این کشور علیه کشورهای همسایه صورت می‌گیرد.
🔴
این هشدارها پس از حملات پهپادی به خط لوله نفت شرقی-غربی عربستان سعودی صورت گرفت که ردیابی آن‌ها به استان میسان عراق انجامید
🔴
به بغداد هشدار داده شد که باید افرادی را که مسئول حملاتی هستند که از خاک عراق انجام می‌شوند، شناسایی و محاکمه کند، در غیر این صورت ممکن است این کشور به عنوان حامی تروریسم شناخته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147383" target="_blank">📅 15:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147382">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e279215317.mp4?token=rxcxvpKBEhkEe-59kSXhfF-jgmwMlM96HcShMZZg4JnODQL5yAG5g4sxzG9forjHGb48di33ipCadEjGTz7dP0ZFrESALhUNHzZFY0Ia6Yi2215rloAZD8rFc8hFh55qDMfeSofyRMkNbUpL2MxBSPnR75DBW2fVwpeNLqOwjRq8GNmCytLFJMmNyS6dMSx37mlb3BKNCpgfg_JlGozr0ertkclE8C69Q207T8DsIp87OgZW0coge6O68X9g2BmN0HbMGbAyza9a90We435QbGxaOdaH8gMx90MaNrhsxTdMWf9UUsgvWov14Xm0mnWmpQ8ysGIxhHk1q8TNFMtwAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e279215317.mp4?token=rxcxvpKBEhkEe-59kSXhfF-jgmwMlM96HcShMZZg4JnODQL5yAG5g4sxzG9forjHGb48di33ipCadEjGTz7dP0ZFrESALhUNHzZFY0Ia6Yi2215rloAZD8rFc8hFh55qDMfeSofyRMkNbUpL2MxBSPnR75DBW2fVwpeNLqOwjRq8GNmCytLFJMmNyS6dMSx37mlb3BKNCpgfg_JlGozr0ertkclE8C69Q207T8DsIp87OgZW0coge6O68X9g2BmN0HbMGbAyza9a90We435QbGxaOdaH8gMx90MaNrhsxTdMWf9UUsgvWov14Xm0mnWmpQ8ysGIxhHk1q8TNFMtwAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا سیما : بازگشایی مرز تجاری شلمچه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147382" target="_blank">📅 15:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رسانه کوبیسی لتر: وضعیت وخیم انرژی در خاورمیانه؛ تولید نزدیک به ۳۰ میلیون بشکه نفت در روز یا متوقف شده یا در معرض خطر اختلال قرار دارد
🔴
این یکی از شدیدترین موقعیت‌های اختلال در عرضه انرژی در تاریخ معاصر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147381" target="_blank">📅 15:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147378">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEs2EbOlfYlozQOiMqbB7dgEmvLGzmY0U_J1QBVhVMCBML3yQAJHrDEGFhG5q3WTfPnhUKADlbrG3Ytf1mH-NZOl6Dpik59tiA694PS36rn0XTaWRh21NugrlIEiDy_5xWnLp1q6Z4-QWyDYa8w56K0wl_ucFOOaEWDeDhkqBbRw2DXvwvJ_XT3ig4vLiykxwHqgT2jGJijV5eRfyOsdzOlQD6NliNH6L5J9pVlwFu5cAeUrBz-VvHkHRJ9qDnLuPeqvWh1IxcyEkP1qTbPpyHRTdNIx6ovk8zWaKIgRr-xH21I-Tm0zezl_IX5wLQ6xgMTM2JmW-UHVncRMhxcPAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c1fe0954.mp4?token=b3YXPKM-H2Kwbp8D5f7DReOTYhGoH_xXx1UasYw3jpEXyhpv9wDI3YxWAwxDdbhFlp5DqFfE8bhUqXx6dsiJ52YoMsjE6MYe-zHr1Z5MDNvHwsHleA7d16fykBtwH5ilPmroJ1CHbdnjbHs8FXWNUf154HKkiUkli6ZviDDDdBuoBr8hYqQoz43Kv-NX2tiJHh0EcWj5QAI-2NOO-GIPugTzR7RUcxJC6ftx5OqYLctWDN4imi36GkyAmOtqXHrLguaSyPdmTo5ADKhHeh-IoZU2K22denN9K5xwZRA2BrDwB_O2_PNmstmqs88RowPjPXK0zMfy-zaaZixkTeupfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c1fe0954.mp4?token=b3YXPKM-H2Kwbp8D5f7DReOTYhGoH_xXx1UasYw3jpEXyhpv9wDI3YxWAwxDdbhFlp5DqFfE8bhUqXx6dsiJ52YoMsjE6MYe-zHr1Z5MDNvHwsHleA7d16fykBtwH5ilPmroJ1CHbdnjbHs8FXWNUf154HKkiUkli6ZviDDDdBuoBr8hYqQoz43Kv-NX2tiJHh0EcWj5QAI-2NOO-GIPugTzR7RUcxJC6ftx5OqYLctWDN4imi36GkyAmOtqXHrLguaSyPdmTo5ADKhHeh-IoZU2K22denN9K5xwZRA2BrDwB_O2_PNmstmqs88RowPjPXK0zMfy-zaaZixkTeupfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شب گذشته، در جریان درگیری بین حوثی‌ها (انصارالله) و شورای انتقالی جنوب یمن (PLC) که از سوی عربستان سعودی پشتیبانی می‌شود، یک موشک بالستیک DF-15 ساخت چین علیه استان مأرب در یمن مورد استفاده قرار گرفت
🔴
موشک DF-15 یک موشک کوتاه‌برد است که قادر به رسیدن به مسافتی معادل 800 کیلومتر است
🔴
حوثی‌ها نحوه کار با این موشک‌ها را نمی‌دانند؛ در حالی که عربستان سعودی از طیف گسترده‌ای از سلاح‌ها و تجهیزات ساخت چین استفاده می‌کند، بنابراین احتمال استفاده از این موشک توسط آن‌ها وجود دارد، اما این موضوع هنوز به طور قطعی تایید نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147378" target="_blank">📅 14:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147377">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87af46103b.mp4?token=W5PAJ-uAGsSPKP7jkWL9_qONNkXZ8BG9xJj7QuEpMIL0PHXOwUQBEOdgqoTKkOXmivT6-BPocoqk7dckgke6mZAX4dnHyY0PId52cK_r12In5znD90hFfHsD7JApBIMNsO_zPeyYJvORhMXW3Y4ivVUTtOhkCB4i_sq8WiIfO7sZmzQgrXAo0s5ipN-xliVK8yWpc7oc8IH5XIGBOJw9I0BFM24me_6NhMCeIM0Kp-QjfMAdZKUmqj6kt5AlVXS3EvtdzxwpoikP8cyDIcyR9XaWQH_SgjufaypvmPBmsOTvsEnRy0-8J3DpgJG1SIyOGDMI7WX9nQMCf1APb_pQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87af46103b.mp4?token=W5PAJ-uAGsSPKP7jkWL9_qONNkXZ8BG9xJj7QuEpMIL0PHXOwUQBEOdgqoTKkOXmivT6-BPocoqk7dckgke6mZAX4dnHyY0PId52cK_r12In5znD90hFfHsD7JApBIMNsO_zPeyYJvORhMXW3Y4ivVUTtOhkCB4i_sq8WiIfO7sZmzQgrXAo0s5ipN-xliVK8yWpc7oc8IH5XIGBOJw9I0BFM24me_6NhMCeIM0Kp-QjfMAdZKUmqj6kt5AlVXS3EvtdzxwpoikP8cyDIcyR9XaWQH_SgjufaypvmPBmsOTvsEnRy0-8J3DpgJG1SIyOGDMI7WX9nQMCf1APb_pQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه هند در جریان سخنرانی پزشکیان در اجلاس بریکس مشغول خوردن آجیل و لیسیدن انگشتانش بود و مدام از ظرف آجیل برمی‌داشت تا اینکه سرانجام کارکنان تشریفات، ظرف آجیل را از مقابل او برداشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147377" target="_blank">📅 14:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147376">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پزشکیان: رقم کالابرگ قطعاً افزایش خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147376" target="_blank">📅 14:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147375">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گزارش برخی رسانه‌ها حاکی از وقوع انفجار در العقبه اردن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147375" target="_blank">📅 14:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147374">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7003bc8130.mp4?token=I6vmT53AsRU1c5-qMzAhjkkjBvHA0CfbtJ1NaPz3Vp_y2kPXyDRDYR38b4jc24p1kwD3XDhe1ZbvuAG9MRpLn1-a3e5GaudNRKeIA0KWmldvhbvCpdQqxyAR4n2jSRpiGdrQIi1BSX4AacjtGWmRBtAgDUBDjMIM4ddnGJYohzfm-iJPw8OD_o680e5z57mNjGccqRR9ZS7crQNcU8512nnYBn73Ywj3pYcf7bBnGcJROfKl16yGFO2OMtOCbuEMkD22TrcYgpERFVuQRshZui4YgzPTeAL7PBBqvNazid_ncJRQskptPsvVxwg1-77wDntLclNaiJZPRVP6P0OAXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7003bc8130.mp4?token=I6vmT53AsRU1c5-qMzAhjkkjBvHA0CfbtJ1NaPz3Vp_y2kPXyDRDYR38b4jc24p1kwD3XDhe1ZbvuAG9MRpLn1-a3e5GaudNRKeIA0KWmldvhbvCpdQqxyAR4n2jSRpiGdrQIi1BSX4AacjtGWmRBtAgDUBDjMIM4ddnGJYohzfm-iJPw8OD_o680e5z57mNjGccqRR9ZS7crQNcU8512nnYBn73Ywj3pYcf7bBnGcJROfKl16yGFO2OMtOCbuEMkD22TrcYgpERFVuQRshZui4YgzPTeAL7PBBqvNazid_ncJRQskptPsvVxwg1-77wDntLclNaiJZPRVP6P0OAXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل (IDF) تعدادی از شهروندان سوری را در مناطق روستایی قونهیترا دستگیر کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147374" target="_blank">📅 14:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147373">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEZ70KulzN-b11WJ5rvtpHsWqJyGjGDKqOFMZTtDHXd3We8EgYkazKznJXsxLVDNuj20F9KEIQTUX9ZJbJRTYD95_G3X2yzsiSG908ziQZYwspioqqjoN9VX0Dp8BOFan1lDNWhBxxIY7p_ZQAR3QYD9eayWcaGDTLRZuv9CsNRk-PWJGDKUozl80ORWPzmXLUirUrKA1Ica8h84fe9Y6VjqTChxsqEkggr0auBcH5V0eCXFAWi2k9XKovpIjMJpcWsuGgl7gL_p4_iGtqCBMFNe9D2DujOiqvdBy2pHsQfWDUYmDXqxkf69cZYK1SBdhT_44oK-DJLMGhTdcGdtLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سدهای مشهد به گل نشست
🔴
دبیر و عضو اصلی شورای راهبردی روابط عمومی بخش آب کشور گفت: هم‌اکنون فقط ۲ درصد از حجم ذخیره سدهای مشهد آب دارد و در حقیقت چهار سد این کلانشهر به گل نشسته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147373" target="_blank">📅 14:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9dhoVkM16EWyQ9wwFShD1JmRtm6gEtbncwpqnYLPjSBvG7muOmPgsWGJWCph2YjhIdGoAczHGZ_0v-o0VPoT3MOVlfzOZB9LOkfVCIPXoWi7587M_F0QBwiJz17zcJsGM9Rzbf-x7GwvtprYVncl_HPBQOZXKlgbjz_gnneh6LQGyWJzZtTUDFcMCWA1flnQxIvWCdHImQIMYMPOAUUoKfrWB209rqs0UMAQcgj2uhxNAHe3tozNzi7OWu1P9Yqy0RvZr5xFuzz0udbtpJc2d-m1YnLFiIUqKPhEkmbpe-j8oopemkG6WC19ma5sA2eElGzGzZ1zuywSsZXkXdkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمودار نوسان قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147372" target="_blank">📅 14:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147371">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=uRpBpRiDwyZLcJx6pGTH3lGSjH_dxQwfaZlHFtwayHSAcmHok2ZIYd4bxW6JoXBu5Kdzf04RcmY1wwvqIJT6JQDob7XyNs35DwkA1z9sxxr5PGzQjisqc_Sm3FDQeLlNNJxNq3wKYIOMr6AyXswsOzYY10qMRPdN1A5eSr2oP3BaHmxlJp5QwMKTWr_fLskfyyDBwtXSUn7SBH-8zKmKJcsR_b_XqdgC5lCf9TKuJgEVboHbGgHoFiRe-1qUexnItfzHjZqHKkjLZ-aYHD6WE2GeqGMLNwJjxXpkKUrI3aZ5yda20_OxdmdGpi2TK31FwZkbNHELG2EckXImssUgRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=uRpBpRiDwyZLcJx6pGTH3lGSjH_dxQwfaZlHFtwayHSAcmHok2ZIYd4bxW6JoXBu5Kdzf04RcmY1wwvqIJT6JQDob7XyNs35DwkA1z9sxxr5PGzQjisqc_Sm3FDQeLlNNJxNq3wKYIOMr6AyXswsOzYY10qMRPdN1A5eSr2oP3BaHmxlJp5QwMKTWr_fLskfyyDBwtXSUn7SBH-8zKmKJcsR_b_XqdgC5lCf9TKuJgEVboHbGgHoFiRe-1qUexnItfzHjZqHKkjLZ-aYHD6WE2GeqGMLNwJjxXpkKUrI3aZ5yda20_OxdmdGpi2TK31FwZkbNHELG2EckXImssUgRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله افراد لباس شخصی و آتش به اختیار به یک رستوران در رشت به نام « سحرخیزان » و تخریب رستوران به بهانه حجاب⁩⁩
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/147371" target="_blank">📅 13:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147370">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
معاون هماهنگی توزیع شرکت توانیر: در صورت رفع ناترازی برق؛ از ابتدای هفته آینده قطعی برق نخواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147370" target="_blank">📅 13:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147369">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5255c77892.mp4?token=n2doI9D3rXghvACKhKVUyiJTCLyQqBq_KlsiXnolaW8qRPrfxmRgV94hS-ZO2cT2z1hnBTs7mvUkhXHqDL-2ZvEIudH7U7iDj7r-YxyA8PqrrVjwsq7Xyas4fBOvwEQb06zfmFAMOWFvY9dEY8Gp3pUX_wzgqRCS-CUHLCqGEawzWoijr8djssUPfXVRzHQGTIRYNKxCJwum3n0NwwEF16mcG6Q6RzHW0MraqU1LlXWoVux05XJOeH1T4N7BLT2QLVUC9aFd1CqxHdY33QkWWCR_Y9YNcY_ac3wd8LmGSk4ojsKO_9UzWGIt7GWcZ42oXGeyi-RSe17KMh3aT8NI9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5255c77892.mp4?token=n2doI9D3rXghvACKhKVUyiJTCLyQqBq_KlsiXnolaW8qRPrfxmRgV94hS-ZO2cT2z1hnBTs7mvUkhXHqDL-2ZvEIudH7U7iDj7r-YxyA8PqrrVjwsq7Xyas4fBOvwEQb06zfmFAMOWFvY9dEY8Gp3pUX_wzgqRCS-CUHLCqGEawzWoijr8djssUPfXVRzHQGTIRYNKxCJwum3n0NwwEF16mcG6Q6RzHW0MraqU1LlXWoVux05XJOeH1T4N7BLT2QLVUC9aFd1CqxHdY33QkWWCR_Y9YNcY_ac3wd8LmGSk4ojsKO_9UzWGIt7GWcZ42oXGeyi-RSe17KMh3aT8NI9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا ممانعت از حضور محمد اسلامی در وین را گردن گرفت
🔴
نماینده ایالات متحده: نمی‌توانستیم اجازه دهیم یک مقام تحت تحریم سازمان ملل در کنفرانس آژانس شرکت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147369" target="_blank">📅 13:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147368">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940396b8a1.mp4?token=aueg9OOiZh4I4uDDe0s-_0JA4IM5ewmFXEunn2fNhzh4y9BTL9GfwE3i5jUTcq_UDtUuuc1MYK_62_xwQNR9zGIkZAami4bShqXgrol3rmTyJKWac7zP0I-U6EItZPrqA57goWdmUe189oCHnsZW-Z_U7sNWKoBkPurrqGj1Qj_-gvI7_5fCsWpIt3OHCTcDlbW5KHFrZu7XiIEnNlaFu6MT_1Tfu3HMXGvJ33eYT_X2h0b-dI85JfC3ey1hYvMjfnBnOtjG4d3txDibMzA7IOgTanSoNNYDJUl5yikmEgPcolFzQcf821Q-ep_TZcZ6AOXpgYcnieT-7_0uguHBNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940396b8a1.mp4?token=aueg9OOiZh4I4uDDe0s-_0JA4IM5ewmFXEunn2fNhzh4y9BTL9GfwE3i5jUTcq_UDtUuuc1MYK_62_xwQNR9zGIkZAami4bShqXgrol3rmTyJKWac7zP0I-U6EItZPrqA57goWdmUe189oCHnsZW-Z_U7sNWKoBkPurrqGj1Qj_-gvI7_5fCsWpIt3OHCTcDlbW5KHFrZu7XiIEnNlaFu6MT_1Tfu3HMXGvJ33eYT_X2h0b-dI85JfC3ey1hYvMjfnBnOtjG4d3txDibMzA7IOgTanSoNNYDJUl5yikmEgPcolFzQcf821Q-ep_TZcZ6AOXpgYcnieT-7_0uguHBNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف‌های ناشی از کمبود بنزین در روسیه به شهر سنت پترزبورگ رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147368" target="_blank">📅 13:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
عضو کمیسیون اقتصادی مجلس: ممنوعیت واردات لوازم خانگی در آستانه لغو قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147367" target="_blank">📅 13:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
خبرگزاری عربستان سعودی: محمد بن سلمان ولیعهد عربستان سعودی با فرمانده ستاد فرماندهی مرکزی  آمریکا در مورد تحولات منطقه‌ای گفتگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147366" target="_blank">📅 13:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گروسی: ما بار دیگر دست خود را به سوی ایران دراز می‌کنیم تا با ما برای روشن شدن مسائل مربوط به برنامه هسته‌ای‌اش همکاری کند
🔴
به ایران می‌گویم که وقتی کارمان را در آنجا از سر می‌گیریم، نگرانی‌های امنیتی آن را در نظر خواهیم گرفت.
🔴
ما از وضعیت دشوار ناشی از درگیری‌های جاری در منطقه خاورمیانه آگاه هستیم.
🔴
تا زمانی که 30 کشور هسته‌ای وجود
داشته باشد، جهان امن‌تر نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147365" target="_blank">📅 13:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس‌ ادارهٔ آموزش‌وپرورش رباط‌کریم تهران به‌اتهام فساد مالی در آموزش‌وپرورش این شهرستان روانهٔ زندان شد.
‏
🔴
پیش‌از این ۸ نفر از متهمان مرتبط با پرونده‌های تخلفات مالی در آموزش‌وپرورش و برخی مدارس رباط‌کریم دستگیر شده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147364" target="_blank">📅 12:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147363">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت دفاع امارات: دو نیروی نظامی این کشور در جریان یک مأموریت آموزشی کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147363" target="_blank">📅 12:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147362">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
تسنیم: پدافند هوایی کشور آپدیت شد و آماده رهگیری هرگونه هواپیمای متجاوزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147362" target="_blank">📅 12:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147361">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgqwhzWzXOx1FtD00CZbfBWzdCA9usew5k2vCGq_gPCPYwJcrbETD82jaS6y92QkL1yyl_h-CAxFZ5dZDcmac7LgODz51DQvKbzsOsTmfWiYIrh6h3AWVzJzv9w6SupKi1qpoI0nyb7g53ptQ3HpZBHJoqFvcxppnKYzMAm4ivzNhRXVEjFmURhgx8jNabMKokVaDJtfe1Ywp4Q5nYEiLhyU0LY_hVXfAlWjf234HH0dWfLTKEhxrbrsYNe7qcdMviKXT89iMlvgYTqHEmh6MRgjHfK8DZ3GL_91qVAOPKOxY9Rn_i8BRw5kVpam58i95_0am5HaZqWgyd8H6VdBiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سامانه ثبت احوال باز هم قطع شد!
🔴
با وجود اعلام ثبت احوال مبنی بر امکان صدور شناسنامه المثنی به صورت اینترنتی، سامانه ثبت احوال همچنان با قطعی مواجه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147361" target="_blank">📅 12:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147360">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
چین: تصاویر ماهواره‌ای به ایران ندادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147360" target="_blank">📅 12:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147359">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7058bc1f.mp4?token=H0OWLS22VXxThlazr0893FgI-lmUuxUNjR58X6T39ksCWP--ihwd-aj_tM0CZ7d0MSGrI6_gs4qV4nkfGlms2a8Yo53HiCLVf2-fGUK2tqErlBID-jJieguR4e1jYW8s5iNK24Mx5d62MxAfsNnnBDK37MTa45VrcDQcAfcCAC-6Ew_njSaUpdZOonDkDK4_-8QksxkDoUN6ds06LtlzvPPP06-xT2tX8OADXFw_zNojxA1TbYQHxKH_-PEhPXIXcDxZHCGFAVQCFfxCj3slJDqf_LND2FizmjYIzid7kTve4AZRtAGoaZFUqohy9YemRQ29mzZ7_RCr6JR01h4lXRO-8Y0PGctVk4WcZBvpOm3ykZhwBEq9psXKusFxeX4ZerU08_qlZJtdopXiHuLIBPH1etFjqgA8lcGpjoQRCE2YwH0BsdxJ2PwvDTGvWkXrgAgoMdC4JD60Hv005d1iUB8r5XVDrISunoVSx0HDdFDwReEZmoFuA6m5s3quH8gkkCCbz7Oh3BDZy1LBauvYXKxGO2ezhVpVnPkn5O_lNDgvwNpG26xTkBZJXZJwUD51cNTgl4HGIHnwL7g3a_eqWZg7m8iqnw4v3Siq3SiBPosJev8I2t3Pjim0s6S7vFUzvwUoJ7dZbKO74tfCLztEiL8e998KWDT2-7v_AnbKagc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7058bc1f.mp4?token=H0OWLS22VXxThlazr0893FgI-lmUuxUNjR58X6T39ksCWP--ihwd-aj_tM0CZ7d0MSGrI6_gs4qV4nkfGlms2a8Yo53HiCLVf2-fGUK2tqErlBID-jJieguR4e1jYW8s5iNK24Mx5d62MxAfsNnnBDK37MTa45VrcDQcAfcCAC-6Ew_njSaUpdZOonDkDK4_-8QksxkDoUN6ds06LtlzvPPP06-xT2tX8OADXFw_zNojxA1TbYQHxKH_-PEhPXIXcDxZHCGFAVQCFfxCj3slJDqf_LND2FizmjYIzid7kTve4AZRtAGoaZFUqohy9YemRQ29mzZ7_RCr6JR01h4lXRO-8Y0PGctVk4WcZBvpOm3ykZhwBEq9psXKusFxeX4ZerU08_qlZJtdopXiHuLIBPH1etFjqgA8lcGpjoQRCE2YwH0BsdxJ2PwvDTGvWkXrgAgoMdC4JD60Hv005d1iUB8r5XVDrISunoVSx0HDdFDwReEZmoFuA6m5s3quH8gkkCCbz7Oh3BDZy1LBauvYXKxGO2ezhVpVnPkn5O_lNDgvwNpG26xTkBZJXZJwUD51cNTgl4HGIHnwL7g3a_eqWZg7m8iqnw4v3Siq3SiBPosJev8I2t3Pjim0s6S7vFUzvwUoJ7dZbKO74tfCLztEiL8e998KWDT2-7v_AnbKagc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی‌ها: یک عملیات نظامی علیه پایگاه هوایی ملک خالد در خمیس مشیط عربستان سعودی انجام داده‌اند.
🔴
حوثی‌ها مدعی شدند در این حمله آشیانه‌های جنگنده‌ها، تأسیسات راداری، باندهای پروازی، انبارهای مهمات و دیگر زیرساخت‌های نظامی این پایگاه را هدف قرار داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147359" target="_blank">📅 12:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147358">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dj5CamrHbIHBP1W9PwLwzlYmJc5_h7rN1zGShroMavlWT3smKXWoisAR9W3Z6fdFP3LDYaUpq_36ul66mLX8I0xi28jM6z489KpjABxfgQGQBuxn5r3gCmqFRYmuU-_lGn28EOKqo5nqfx3yz4G95INmOSnhujxwPyUm3LUu2M3huob1kfxksrYBiKbhHxhkRYI3C5Dn32J48duv2L47EzI9nBFUHblY73aD_iH1y55iN-oNp_lH_CXFjoVVCMCZSb71aNFENa7pvlGc53-Z4KfVCJCXKxXYvVToE3M9jKPY1N9sLSl0rItt1M7hX16yznQlE-JNC8B5xqt2HB2XFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی از فروشگاه های داخلی «آیفون ۱۸ پرومکس» رو موجود کردن
🔴
قیمت: ۸۵۰ میلیون تومن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147358" target="_blank">📅 12:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147357">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: دیدار پزشکیان و ولیعهد ابوظبی به درخواست طرف اماراتی انجام شد
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/147357" target="_blank">📅 12:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147356">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
آژیرهای هشدار در عربستان سعودی به صدا درآمدند.
🔴
ابها
🔴
خمیس مشیط
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/147356" target="_blank">📅 12:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147355">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e8b10a9c24.mp4?token=aG-UuW05F0BcYtUuLX-3NvVPySiYG8WylPbsVrwzh5qKROrkzx6h-cK5UxtSLKbobNzAwLQ1-1XC80guQbVuOs3bQxhEiBNMR8qy7AOnM-HGeMZLB3EaA02zBklaRyZ8xv0SlLiYoTOGikLOpbSfr_orm8SZfKq_lTd3ElwnS314_tehuDUSPSyac095WeuuoJKOyYmZSh9s0h7gR-Z4029o_OSynnj5Ask2IFY7jYmkGgynVvG6H3v7DpeEK8sMISQPtaDaLJ8UC9RX1GzoKVFV73YT7m57xYh0Tn24EZSQpN9RyKgdaQkWOO-S9a5ZJIZyclq1VccflXJXLi1Dig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e8b10a9c24.mp4?token=aG-UuW05F0BcYtUuLX-3NvVPySiYG8WylPbsVrwzh5qKROrkzx6h-cK5UxtSLKbobNzAwLQ1-1XC80guQbVuOs3bQxhEiBNMR8qy7AOnM-HGeMZLB3EaA02zBklaRyZ8xv0SlLiYoTOGikLOpbSfr_orm8SZfKq_lTd3ElwnS314_tehuDUSPSyac095WeuuoJKOyYmZSh9s0h7gR-Z4029o_OSynnj5Ask2IFY7jYmkGgynVvG6H3v7DpeEK8sMISQPtaDaLJ8UC9RX1GzoKVFV73YT7m57xYh0Tn24EZSQpN9RyKgdaQkWOO-S9a5ZJIZyclq1VccflXJXLi1Dig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «شما مدام می‌گویید کانادا از روسیه و چین برای آمریکا خطرناک‌تر است.»
🔴
ترامپ: «من گفتم برخورد و مذاکره با آنها دشوارتر است. به نظر من کانادا سخت‌ترین کشوری است که می‌توان با آن مذاکره کرد؛ دشوارترین کشور. با این حال، آنها شدیداً خواهان توافق هستند.
🔴
من کانادا را بسیار، بسیار دشوار می‌دانم؛ منظورم رهبران کانادا هستند، نه مردم این کشور. مردم فوق‌العاده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147355" target="_blank">📅 12:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147354">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز: قیمت نفت روز دوشنبه بیش از ۲٪ افزایش یافت و قیمت برنت به ۱۰۶.۷۲ دلار و نفت WTI به ۱۰۲.۱۵ دلار در هر بشکه رسید؛ هم‌زمان تشدید حملات در خاورمیانه نگرانی‌ها درباره اختلال در عرضه را افزایش داده است.
🔴
خط لوله شرق به غرب عربستان پس از حمله پهپادی همچنان بسته است؛ موضوعی که می‌تواند تا ۴٪ از عرضه جهانی نفت را در معرض خطر قرار دهد.
🔴
همچنین یک شناور در تنگه هرمز هدف حمله قرار گرفت و دچار آتش‌سوزی شد.
🔴
افزایش قیمت نفت پس از ازسرگیری حملات حوثی‌ها به عربستان سعودی رخ داده است. نشست برنامه‌ریزی‌شده میان ایران و کشورهای خلیج فارس درباره وضعیت تنگه هرمز نیز به تعویق افتاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147354" target="_blank">📅 11:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147353">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1d39d99a.mp4?token=Okxo-9yxae8xOBkmLpysvoH8huKVCSj9aB9NyL0YqA_7oR5enb9bN-POHpFKl1WGX3ukvz-RJGOGiqAIUiR4wC1p_cvdmbQoC-V-X3DN1fW8FEotCIDqdXGL0eTOXMKGuIroIu99QuQIt43_vyXTyg1sooQ3hx9mMr6_jx-iViKpyJo9EuwkPj3HoLH8gNmIUNyu-kOVcDRO49Gg2vIgdCpLoAquizFQyqhvQXJ4L8Yvx_XDlN32-IXpbPMaMbvdGgDHMkUdrckR7V95SpQ_wj6dkDAs_jJeGjVkwxsO27_Iu1pPlfESU-_jWcrr-qUfu3Vpiz0d78KjEGY51pK_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1d39d99a.mp4?token=Okxo-9yxae8xOBkmLpysvoH8huKVCSj9aB9NyL0YqA_7oR5enb9bN-POHpFKl1WGX3ukvz-RJGOGiqAIUiR4wC1p_cvdmbQoC-V-X3DN1fW8FEotCIDqdXGL0eTOXMKGuIroIu99QuQIt43_vyXTyg1sooQ3hx9mMr6_jx-iViKpyJo9EuwkPj3HoLH8gNmIUNyu-kOVcDRO49Gg2vIgdCpLoAquizFQyqhvQXJ4L8Yvx_XDlN32-IXpbPMaMbvdGgDHMkUdrckR7V95SpQ_wj6dkDAs_jJeGjVkwxsO27_Iu1pPlfESU-_jWcrr-qUfu3Vpiz0d78KjEGY51pK_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: زیردریایی آمریکایی توقیف نشده غنیمت گرفته شده و غنیمت، حلال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147353" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147352">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9e4ab0539.mp4?token=dLHWrifoenQdwjsZnTm9RK05qePbZ11dPscFZv32QaMyyp3RO9lJxUkrbvsgFp9AZJjJBsDRO1Xp6_pP5WKGZwIggctUnczafi2TtPd6b3o5h075bs6WKFdg5g5zx2wvCZYPAzlQNscDU51eyFeOqkVNr8MBqZ7YqXjmTocOQHWDi4Z5e9Y0TgEAZVnzIiyQm2AgyhOuBhHhtwjK7DBurdvejTKvZs829nm_b2rBMjquhBUk0DyHtbKr2SMQLf-NYCwcvJwK9KoCaR6HwYgRizof0RJrIPMpllW5yxGDqFIZy93PT6Szw2cec4YCHNC8-P3NEVep_QjKYSKGfE0QsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9e4ab0539.mp4?token=dLHWrifoenQdwjsZnTm9RK05qePbZ11dPscFZv32QaMyyp3RO9lJxUkrbvsgFp9AZJjJBsDRO1Xp6_pP5WKGZwIggctUnczafi2TtPd6b3o5h075bs6WKFdg5g5zx2wvCZYPAzlQNscDU51eyFeOqkVNr8MBqZ7YqXjmTocOQHWDi4Z5e9Y0TgEAZVnzIiyQm2AgyhOuBhHhtwjK7DBurdvejTKvZs829nm_b2rBMjquhBUk0DyHtbKr2SMQLf-NYCwcvJwK9KoCaR6HwYgRizof0RJrIPMpllW5yxGDqFIZy93PT6Szw2cec4YCHNC8-P3NEVep_QjKYSKGfE0QsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا ممکن است جنگ اوکراین پایان پیدا کند؟»
🔴
ترامپ: «این موضوع مطرح است. قیمت گازوئیل به دلیل دشواری خروج آن از روسیه در حال افزایش است. اگر این وضعیت ادامه پیدا کند، به جهان آسیب می‌زند. باید جلوی آن را بگیریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147352" target="_blank">📅 11:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147351">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8Emiyp0ECggmUdRWzLRwpxB9aSeyPPeRPLBUsoYpagonN_vgM2K_L-QGx5QZ83pKJ09YVlH7gzf99Y6TBaEtog3T2u1y-w6pbxhNKv3rnGCDAAl4LmDL8ZBXgCavGf6j61S5TfC7UVfuJEQXSy-do3IYgNSsQrQ4yGTefjq4kSq0R7YVzVih6hwMS_Xda-rccFeB0cI1-b6BSNWlW7HMZqC8Ri0_wfwYhpD0AuccuqVR2sOtaEm2HU_xKQ8BGCe1geaj-gi1RtmN-Z4JiL_f-RZPOye-1u0b6D4XFXa9XT1v3RVNw1TAKLZglJedhm42FeCAel4sNARUzJXJNRNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: حسین طائب بدون اطلاع دولت و فرماندهی سپاه، دستور حمله به سه نفتکش را داد تا توافق نابود شود
#یلخی
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147351" target="_blank">📅 11:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147349">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b3c56a710.mp4?token=kdzj2EkWkSoJqqvzC5uOvT1tdgHlordii7yoLTOn92WGZhsWdgIsrt835ZjcqcfhQaL5ZYC9tlHkoR1Ecv7-0lvJuY0VraYC3qhClxgSEPdB9MbUaOHG8fHwJhcfqT4X9eOx6XWO9vph8LRv7QFDrCrER-VcuSP95F6Ai6d3GySqN4JDrD9Dt82jw3DTLWcflr2RblNkgbtrywjElYYzG9tZhxmAM-J5SBHnnvRtnFv3TMnOIUTwcj0gjxo1qTdk_7dSL93g_nrzQLtZDEu3lptCzTf0grtujbZ9pf6ih1CChPEvjETsDld2B1flGlQVVvWlM1qVE0ZoeSeCoBtFig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b3c56a710.mp4?token=kdzj2EkWkSoJqqvzC5uOvT1tdgHlordii7yoLTOn92WGZhsWdgIsrt835ZjcqcfhQaL5ZYC9tlHkoR1Ecv7-0lvJuY0VraYC3qhClxgSEPdB9MbUaOHG8fHwJhcfqT4X9eOx6XWO9vph8LRv7QFDrCrER-VcuSP95F6Ai6d3GySqN4JDrD9Dt82jw3DTLWcflr2RblNkgbtrywjElYYzG9tZhxmAM-J5SBHnnvRtnFv3TMnOIUTwcj0gjxo1qTdk_7dSL93g_nrzQLtZDEu3lptCzTf0grtujbZ9pf6ih1CChPEvjETsDld2B1flGlQVVvWlM1qVE0ZoeSeCoBtFig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه بمباران نیروهای ویژه واکنش سریع سپاه پاسداران که به دنبال خلبان F-15 آمریکایی رفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147349" target="_blank">📅 11:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147348">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b168f1f6a.mp4?token=KIfF1hV-si2f-HqUJj3L_j0zbwYPSg-P_4fKR5jhwZ-to76_qaatbr1xpM92S708zUPVvYu56CoVbMWgMjhS-gU_a4i_aAWLP9VvHYrZTDaagyVXNAZXZ45HF-QygYR3NCLmt20AQzgT655X-nRmMXHfOxRlim1KbMUGAbF1vRmaVAXQuAlOOiv1qMmlGyQmchzKniyF0fyLpIc-mggFCkDar_lf0MuaC3bjmdip3HLz13ao9s3VB2I032LPucP6BKVR95h337c8jjiQXrYIE7iXDf0dsfEZyH0UTwCDYzLJ_fbxWrLtRJIZ7by3DIZ8HG_lT-RpTGenC-5rPu5jwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b168f1f6a.mp4?token=KIfF1hV-si2f-HqUJj3L_j0zbwYPSg-P_4fKR5jhwZ-to76_qaatbr1xpM92S708zUPVvYu56CoVbMWgMjhS-gU_a4i_aAWLP9VvHYrZTDaagyVXNAZXZ45HF-QygYR3NCLmt20AQzgT655X-nRmMXHfOxRlim1KbMUGAbF1vRmaVAXQuAlOOiv1qMmlGyQmchzKniyF0fyLpIc-mggFCkDar_lf0MuaC3bjmdip3HLz13ao9s3VB2I032LPucP6BKVR95h337c8jjiQXrYIE7iXDf0dsfEZyH0UTwCDYzLJ_fbxWrLtRJIZ7by3DIZ8HG_lT-RpTGenC-5rPu5jwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: چین میانجی جدید نیست؛ پاکستان نقش خود را خوب انجام می‌دهد/ هیچ وقت مشکل ایران و آمریکا مساله میانجی نبوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147348" target="_blank">📅 11:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147347">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA_SgKVnBjuKCq2G0t2Gq9slnmr4xhdcwrNoia-CpQTneWQVAb3ICWaVGFb7yFoGSAlg3gbPGUoYlBUTzM1-m2EBxwDExBVKFhhvU8iUrz4v6KIbkgY7m9RXAdTV2_Hr4GGWnJiIRgWU3SS7lV7hSOeYmrTkJTVNVHQOiKqPwTVpBw_UOWAtdnsn7lPwp4s4FTWcdRDR3lp4Dysat-EPLFK70FX9G45wzs0WDQRhmiUXrERLcgGL44x69uzhh5RKVE7RsBpobSI22sL5yheAwaUpy-3650C2o_YnIVwos18UTHk8aB2Bj_3QxRUhEDERbABHBlKLDgPWQKOYCjNUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لاله مرزبان که برنده بهترین بازیگر زن جشنواره ونیز شده بود مورد حمله حامیان حکومت قرار گرفته! چرا؟ چون از حکومت دفاع نکرده
🔴
در تفکر جمهوری اسلامی دو حالت بیشتر وجود ندارد! یا سمت مایی که وطن پرست و باشرفی یا سمت ما نیستی که بی وطن و بی شرفی!
🔴
شماها رو چه به سینما! همون برید تو شب نشینی‌ها پرچم تکون بدید به صرف چای و شیرینی مفتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147347" target="_blank">📅 11:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147346">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تهران در تصمیمات یمنی‌ها مداخله‌ای ندارد
🔴
انصارالله طرفی مستقل در یمن است و بر اساس مصالح خود تصمیم می‌گیرد
🔴
تصمیم‌گیری در مورد مباحث سیاست خارجی و امنیت ملی، تک‌مولفه‌ای نیست.
🔴
ما صرفاً بر اساس یک مؤلفه، در مورد موضوعات بسیار حساس و پیچیده مرتبط با امنیت تصمیم نمی‌گیریم. (قیمت نفت امروز افزایش یافت).
🔴
بنابراین شما نمی‌توانید صرفاً بگویید به دلیل بالا و پایین رفتن یک موضوع، یک تصمیم را بگیرید یا نگیرید.
🔴
تفاهم بین ایران و عمان، به عنوان دو دولت ساحلی، نهایی شده.
🔴
ما با مشورت عمان در مورد گام بعدی، اینکه به چه شکل این تفاهم را اعلام بکنیم یا ثبت بکنیم، تصمیم‌گیری خواهیم کرد و اطلاع‌رسانی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147346" target="_blank">📅 11:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147345">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/63f407f3a5.mp4?token=G0nAjXUdhuSzhBZ_F_BLhLD9IUMKgcIDg9Yw_ieTyyjXJYZ3XPAqdqOYknk3T8VEzHAMyuEebB3MS9cvZRpCUs_9Xlp3-jZFWAGVM-lBB5sBD2SWbTN92EzNtm1ZR5Qiv2G2Tw3Ymo6mzPeKqYXUx_3W7PqHg5sAMc21Js107wwePhYmVPVooeJN2ks68swEN9-b113dkAzng2JyoLl6zvjyhSHbbRK6p1PWzhE4jHfBESRdxHHmA-CRCsWJQh4iOFYtAqorF5GTwgdbb-ukfikTM_vMDf356WDvk5ptwCzjJdKzMNDhBqsxo8RABaot8_nX9akv7tbLKBST2GvibYyONZ5j7dG35cDNRCXVWUrx0iDAJ8Z9X5AHDEYADrHlBwDBqrA8nw1Sr87cVXiSlJhJ8XDlvNCIBmDEsn2GZU_6CXlyiVeWSn1Ox95Thn4ZwZLby__89TdDf15sL6tpg1H2WXVQlJJ2dQSEw7yAp0bNwfuP1pi68Pxw97KMMt4UWKWHHw_TED5GP6IqKS9IntacSBX-9wO3YzocJYlR3hvch3Xj5QMt3nRjiEEp0MDs174_9emLEcXrbWRUqCnvVEa7UzoP3le8_Dc4F2ipKpoEah5qpVSpyMhBF-llJUCr65Vr86OVWeXTaZaj4y5udEj3pPNeVP8orhmYcUN5A14" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/63f407f3a5.mp4?token=G0nAjXUdhuSzhBZ_F_BLhLD9IUMKgcIDg9Yw_ieTyyjXJYZ3XPAqdqOYknk3T8VEzHAMyuEebB3MS9cvZRpCUs_9Xlp3-jZFWAGVM-lBB5sBD2SWbTN92EzNtm1ZR5Qiv2G2Tw3Ymo6mzPeKqYXUx_3W7PqHg5sAMc21Js107wwePhYmVPVooeJN2ks68swEN9-b113dkAzng2JyoLl6zvjyhSHbbRK6p1PWzhE4jHfBESRdxHHmA-CRCsWJQh4iOFYtAqorF5GTwgdbb-ukfikTM_vMDf356WDvk5ptwCzjJdKzMNDhBqsxo8RABaot8_nX9akv7tbLKBST2GvibYyONZ5j7dG35cDNRCXVWUrx0iDAJ8Z9X5AHDEYADrHlBwDBqrA8nw1Sr87cVXiSlJhJ8XDlvNCIBmDEsn2GZU_6CXlyiVeWSn1Ox95Thn4ZwZLby__89TdDf15sL6tpg1H2WXVQlJJ2dQSEw7yAp0bNwfuP1pi68Pxw97KMMt4UWKWHHw_TED5GP6IqKS9IntacSBX-9wO3YzocJYlR3hvch3Xj5QMt3nRjiEEp0MDs174_9emLEcXrbWRUqCnvVEa7UzoP3le8_Dc4F2ipKpoEah5qpVSpyMhBF-llJUCr65Vr86OVWeXTaZaj4y5udEj3pPNeVP8orhmYcUN5A14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره گزارش‌ها مبنی بر ارائه تصاویر ماهواره‌ای از پایگاه‌های آمریکا در اردن به ایران توسط شرکت‌های چینی:
🔴
خبرنگار
:
«ما اخیراً گزارش دادیم که ممکن است برخی نهادهای چینی، تصاویر ماهواره‌ای از پایگاه‌های هوایی آمریکا در اردن را در اختیار ایران قرار داده باشند. آنها همان کاری را می‌کنند که ما انجام می‌دهیم؛ تقریباً همان کار را انجام می‌دهند. آیا هنگام سفر شی جین‌پینگ، این موضوع را با او مطرح خواهید کرد؟»
🔴
ترامپ
:
«فکر می‌کنم او رفتاری منطقی داشته و ما هم رفتار منطقی داریم.
🔴
می‌دانید، وقتی می‌گویند چین از ما جاسوسی می‌کند، می‌گویم درست می‌گویید؛ ما هم از آنها جاسوسی می‌کنیم. ما هم از آنها جاسوسی می‌کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147345" target="_blank">📅 11:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147344">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2c6047d82.mp4?token=JJJdl0NotY24-641DMvwqCUkI7d-jic9qwR0QGC-BPkE0lVhVat80YRIED82-bZy3vn5cWMKbH_vjz5rFj56UrTDG9uprhBTtDSr0RQHpSBVDctVfT5RpN1a6KOwc3sdzVJ-XjNyIFDvkQ36aBl9Vkuo54CGfyNSDmUdY_rND5c5RPBLuJdfDCEDn5ooP4ZAxeO2e1EdOZNkTYa7vEAksq8nqqoNRG3pukUgHDxRT258blP3SDYd8amch8ctuF2R7_w1bfcKythqGuYIN5t63Q2olZ7AE34u9Yt82gFYQ0i5NoGQDxCldC0T8XGQSDDuhmbQwhTolYQDD5rvmnD8SB7uo5lvJEcTpxnPyub7-Epzw2fCNNyakBCiXfnhMOwGE3Di42BB_aDCiWL1HcaxfNOjqDfL533s7RA-ytMlJSnfXl2pwdo9VuerVO5M2AiuKUQQQBDdf6ASGM8IDhy8l9a00p806NXRYEDvwY96orxiJ_Gl5khxn-2XW1_cUuYqe_oS7Zsw-IqmOgcWOjcich57MLYbwlv-Iqm-T2QoTgmA0Ehnc__RwoTKomJGM3kYjyelQII2o7KO7f0w5R1EEznBaxb2wlHaMi7dz1va-gk8st-95STbGnBVdjO4Z6W4Z75dyaharxg_Bl-7ld9vAnKWJiDNIT6BR6Dq8Q8aVA0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2c6047d82.mp4?token=JJJdl0NotY24-641DMvwqCUkI7d-jic9qwR0QGC-BPkE0lVhVat80YRIED82-bZy3vn5cWMKbH_vjz5rFj56UrTDG9uprhBTtDSr0RQHpSBVDctVfT5RpN1a6KOwc3sdzVJ-XjNyIFDvkQ36aBl9Vkuo54CGfyNSDmUdY_rND5c5RPBLuJdfDCEDn5ooP4ZAxeO2e1EdOZNkTYa7vEAksq8nqqoNRG3pukUgHDxRT258blP3SDYd8amch8ctuF2R7_w1bfcKythqGuYIN5t63Q2olZ7AE34u9Yt82gFYQ0i5NoGQDxCldC0T8XGQSDDuhmbQwhTolYQDD5rvmnD8SB7uo5lvJEcTpxnPyub7-Epzw2fCNNyakBCiXfnhMOwGE3Di42BB_aDCiWL1HcaxfNOjqDfL533s7RA-ytMlJSnfXl2pwdo9VuerVO5M2AiuKUQQQBDdf6ASGM8IDhy8l9a00p806NXRYEDvwY96orxiJ_Gl5khxn-2XW1_cUuYqe_oS7Zsw-IqmOgcWOjcich57MLYbwlv-Iqm-T2QoTgmA0Ehnc__RwoTKomJGM3kYjyelQII2o7KO7f0w5R1EEznBaxb2wlHaMi7dz1va-gk8st-95STbGnBVdjO4Z6W4Z75dyaharxg_Bl-7ld9vAnKWJiDNIT6BR6Dq8Q8aVA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره ورود خودروهای چینی به بازار آمریکا: خبرنگار: «آیا در دیدار پیش‌رو با رئیس‌جمهور شی، درباره خودروها صحبت خواهید کرد؟ و آیا اجازه ورود خودروهای چینی به آمریکا را خواهید داد؟»
🔴
ترامپ
:
«من این کار را نکرده‌ام؛ این من بودم که آنها را بیرون نگه داشتم. تعرفه‌ها آنها را بیرون نگه داشتند. من تعرفه ۱۰۰ درصدی دارم؛ از ۱۰۰ تا ۱۵۰ درصد.
🔴
برخلاف اروپا که خودروها در آنجا در حال نابود کردن بازار هستند. صفر. بنابراین، تا اینجا پاسخ
بله
است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147344" target="_blank">📅 11:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147343">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8edb1aff.mp4?token=muidXlM-CF_vtdblnZxQbg-rFG6SWN8ZD4-M10vfKCSqhXeDscM78Ucef-Ax-j3BPTskhczLuGBEiVGPJASWjb9wuKf8GkDqEtkF7BrGXQZHvbfO3Wl7Ul_ZMB6twEezSife2tcKR_05FgzPEZcRNW02oyNYismJGi6e5gbd0vsdsO6D_-aqAkeGd1wc96RN3d_kgeUsTtYadQhWcRWCTJ95smo_eJldAOVBTkxrP7b879YUFvwafGVqwNiUKXuuulcLIAlqD4xylHwsCz0YPTV4RbeIuMtUxQyrAP17oZZkNVJrS5lgGDxhGoZ_dYWWVt6W7uQT6KyU1eWQSCXO9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8edb1aff.mp4?token=muidXlM-CF_vtdblnZxQbg-rFG6SWN8ZD4-M10vfKCSqhXeDscM78Ucef-Ax-j3BPTskhczLuGBEiVGPJASWjb9wuKf8GkDqEtkF7BrGXQZHvbfO3Wl7Ul_ZMB6twEezSife2tcKR_05FgzPEZcRNW02oyNYismJGi6e5gbd0vsdsO6D_-aqAkeGd1wc96RN3d_kgeUsTtYadQhWcRWCTJ95smo_eJldAOVBTkxrP7b879YUFvwafGVqwNiUKXuuulcLIAlqD4xylHwsCz0YPTV4RbeIuMtUxQyrAP17oZZkNVJrS5lgGDxhGoZ_dYWWVt6W7uQT6KyU1eWQSCXO9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: عربستان درخواست کرد نشست عمان برگزار نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147343" target="_blank">📅 11:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147342">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650fa3987b.mp4?token=Bj-lWOYaIHThf1CZBpwH0Q7UGMmOxDn5nwzby2ysxwUJiXGYICVJKj2VbvQuQS-t2IAnoe9zRUyi-SzceXXI20_YPjAOyP-5PIqpd8WkuWmu1c0TY6DDn8HYcuZl8GkcSOqfqPz3WHqOaLLDxp4_30PVhSo-NxjZBeXPQuTzo-qXUOxGOWXHK34slZZ3rdW9jZFvfuFxT1wQlyVxB2WIWEixVFUR3asw5ETg1jsOB5lqgdjCoO8-uxfDW5e261p8VL6OhqYhI4FncCD4DDp5GSYDN7CnccmC7g0tjL32jMSNYd9mBzxB_9CfZuCK4KoUXsH1P7PSz2H-J6PyoVKS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650fa3987b.mp4?token=Bj-lWOYaIHThf1CZBpwH0Q7UGMmOxDn5nwzby2ysxwUJiXGYICVJKj2VbvQuQS-t2IAnoe9zRUyi-SzceXXI20_YPjAOyP-5PIqpd8WkuWmu1c0TY6DDn8HYcuZl8GkcSOqfqPz3WHqOaLLDxp4_30PVhSo-NxjZBeXPQuTzo-qXUOxGOWXHK34slZZ3rdW9jZFvfuFxT1wQlyVxB2WIWEixVFUR3asw5ETg1jsOB5lqgdjCoO8-uxfDW5e261p8VL6OhqYhI4FncCD4DDp5GSYDN7CnccmC7g0tjL32jMSNYd9mBzxB_9CfZuCK4KoUXsH1P7PSz2H-J6PyoVKS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کنایه خبرنگار به ترامپ در استفاده زیاد از هوش مصنوعی برای تولید کارتون
🔴
سوال خبرنگار: آیا خودتان تا به حال از هوش مصنوعی استفاده کرده‌اید؟
🔴
ترامپ: بله، من از هوش مصنوعی استفاده می‌کنم.
🔴
خبرنگار: چگونه از هوش مصنوعی استفاده می‌کنید؟
🔴
ترامپ: می‌شود از هوش مصنوعی برای خیلی از کارها استفاده کرد.
🔴
خبرنگار: شما از هوش مصنوعی برای چه کاری استفاده می‌کنید؟
🔴
ترامپ: نمی‌خواهم این را به شما بگویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147342" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147341">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
خبرگزاری فرانسه: بازرگانان ایرانی که حضور مستحکمی در بازارهای قدیم دبی دارند، باور ندارند پیوندهایی که طی دهه‌ها میان قطب مالی امارات و جنوب ایران شکل گرفته، به‌ راحتی گسسته شود
🔴
افراد فعال در دبی توانستند شرکای خود در ابوظبی را متقاعد کنند که تجارت، فارغ از تحریم‌ها، باید ادامه پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147341" target="_blank">📅 11:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147340">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رویترز: دونالد ترامپ، رئیس‌جمهور آمریکا، احتمال ماندن ایالات متحده در ایران و «برداشت نفت» را مطرح کرد و آن را با توافق واشنگتن که کنترل یک‌پنجم ذخایر نفت ونزوئلا را در اختیار آمریکا قرار می‌دهد، مقایسه کرد
🔴
ترامپ گفت آمریکا در نهایت ایران را ترک خواهد کرد، مگر اینکه تصمیم بگیرد برای نفت در این کشور بماند. او همچنین مدعی شد درآمدهای حاصل از نفت ونزوئلا تاکنون «چندین بار هزینه جنگ را پرداخت کرده‌اند.»
🔴
ترامپ بار دیگر گفت انتظار دارد جنگ با ایران تا پایان سال جاری پایان یابد؛ احتمالاً پس از انتخابات میان‌دوره‌ای آمریکا در نوامبر.
🔴
او افزود پس از پایان جنگ، قیمت بنزین «مثل سنگ سقوط خواهد کرد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147340" target="_blank">📅 10:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147339">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArAOhg7He-IuAS3G3fezhvIdUBtSlV7iljOWet54OlY-isiOfEgjxV-_mT89oYIBHx-T6PVHnygS8TGI6jyNd5QPrpsH7EUQUw-ZcQSvSdssvB47sWPNFYDtw7KUxjLBOEoj3Z8GWAP39TJ1yeKx3JOKHtehh53B6XblV50juxWyo2lBh-nYquz7kRldpBiXYYN8wjFbBIEsIYw0VVx4p40gC722VDSAp2py3LKSEsK2o1_4pR-o1u6UZK6Aybmtg3fZz1ldsC5TXzexTP_UQF0JtSxLAAntQ8RGlSxvBJNBN_LrpXCmGyNbnarlWpW9rzpxMN6nbEVWUy9-MZCpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش‌چشم: یه موشک جدید ساختیم که مخصوص ناو هواپیمابره و تست هم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147339" target="_blank">📅 10:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147338">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نیویورک‌تایمز: دولت ترامپ قصد دارد محدودیت‌های فدرال بر انتشار گازهای گلخانه‌ای نیروگاه‌های زغال‌سنگ و گاز آمریکا را لغو کند و بدین ترتیب بخش عمده‌ای از مقررات اقلیمی دوران بایدن و اوباما را کنار بگذارد
🔴
انتظار می‌رود لی زلدین، رئیس آژانس حفاظت از محیط زیست آمریکا (EPA)، روز دوشنبه این تصمیم را اعلام کند.
🔴
در صورت عبور این طرح از چالش‌های حقوقی، اجرای آن می‌تواند تنظیم انتشار کربن نیروگاه‌ها را برای دولت‌های آینده آمریکا نیز دشوارتر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147338" target="_blank">📅 10:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147337">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca3abb489.mp4?token=VBuMrlY2Gush-1014ZiByIPKI7z-8RPVeC8KEWgUATXB7Hel41LeaTtvtJ6FukzVKXpopqYSNJq9uONvClzS0KJiK2jAWb2ORqG7-YEXJGQSYMF42cf9haeRE1bRJCz0mYtJv2BIAxJFVfXJt9rt6O_T8SCMeyhOlWCHPEuHbKd-YDPkWB9QmgukujGDSvL0QbiNUiT1NDpCFh6MiS2jh-d4FeWf3hnU9RkA9oAi3bpZiLud5fXZUidYS6drfGtYqgYZpcY_-Et8mU_eOkE1yWah36rURMY8r4wyG63iqJNDZCv9nE44PhgvGST02YolYlEc3fCmVX7K_11_ZwOXig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca3abb489.mp4?token=VBuMrlY2Gush-1014ZiByIPKI7z-8RPVeC8KEWgUATXB7Hel41LeaTtvtJ6FukzVKXpopqYSNJq9uONvClzS0KJiK2jAWb2ORqG7-YEXJGQSYMF42cf9haeRE1bRJCz0mYtJv2BIAxJFVfXJt9rt6O_T8SCMeyhOlWCHPEuHbKd-YDPkWB9QmgukujGDSvL0QbiNUiT1NDpCFh6MiS2jh-d4FeWf3hnU9RkA9oAi3bpZiLud5fXZUidYS6drfGtYqgYZpcY_-Et8mU_eOkE1yWah36rURMY8r4wyG63iqJNDZCv9nE44PhgvGST02YolYlEc3fCmVX7K_11_ZwOXig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: نهادهای چینی ممکن است تصاویر ماهواره‌ای در اختیار ایرانی‌ها قرار داده باشند
🔴
ترامپ: آنها اساساً همان کاری را می‌کنند که ما می‌کنیم
🔴
خبرنگار: آیا وقتی شی جین‌پینگ برای دیدار شما به آمریکا می‌آید، این موضوع را با او مطرح خواهید کرد؟
🔴
ترامپ: فکر می‌کنم او رفتار نسبتاً معقولی داشته و ما هم رفتار نسبتاً معقولی داشته‌ایم «جواب دقیقی نداد»
🔴
ترامپ از انتقاد مستقیم از چین خودداری می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147337" target="_blank">📅 10:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147336">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-lZOfakq-5_k-bVpmLYzCVWkm9TbGa8pr7cWeW98pgpOdIlUa1dmCeEn_Nil_VxoJzse1LoR9gVmmRaqwSwQJSwasIt6WQqfG7MkDZGlxysJiL0xea20fkrB9iD4AtxHBXOZEUN07vbaupUyglgqakTsEhPP6LlDBmuSwQnTAihXNNDd0NCKwvTHoy2IfpW2WMszuLytJfKNpGHShcQXhtmcSRitHYQOVLAN78_CebZIgnlOcjYiU99wB6XyvNf8yUdZKH-AFEKwKtzzqAu0sL4SlqJkMxyNYULcQoxhcZ367dZHuqzWl0q6yYJe_5B-A4woA0SsbzZASP6YrVVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای سنتکام از چند قایق تندرو مخفی شده در زیر درخت‌های جزیره خارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147336" target="_blank">📅 10:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147335">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
در مقاله‌ای تحلیلی در نیویورک تایمز آمده است که ایران تشدید تنش را مسیری کارآمد برای تقویت نفوذ خود در مناقشه با ایالات متحده می‌داند. در حال حاضر، ایران و متحدانش بر دو مورد از مهم‌ترین مسیرهای حمل‌ونقل نفت اعمال نفوذ می‌کنند و تهران در تدارک دستیابی به دستاوردی است که می‌تواند جایگاه و نفوذ این کشور را تقویت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147335" target="_blank">📅 10:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147334">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: هرکس به علی الطاهر نزدیک شود کشته خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147334" target="_blank">📅 10:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147333">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سی‌ان‌ان: واشنگتن پرونده هسته‌ای را جلو انداخت؛ هرمز فعلاً اولویت مذاکرات نیست
🔴
سی‌ان‌ان مدعی شد برگزاری نشست به‌تعویق‌ افتاده عمان می‌توانست نشان دهد کشورهای منطقه حاضر نیستند وضعیت فعلی را به‌عنوان شرایطی عادی و دائمی بپذیرند.
🔴
به گفته این شبکه، مقام‌های دولت ترامپ به‌طور خصوصی به کشورهای منطقه گفته‌اند ترجیح می‌دهند، مذاکرات آینده ایران و آمریکا بر پرونده هسته‌ای متمرکز باشد، نه بازگشایی تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147333" target="_blank">📅 09:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147332">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر انرژی عمان : تنگه هرمز باز خواهد شد. احتمالاً این وضعیت کوتاه‌مدت خواهد بود و افزایش قیمت نفت و گاز طبیعی مایع‌شده (LNG) پایدار نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147332" target="_blank">📅 09:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147331">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سپاه: لحظاتی قبل یک فروند پهپاد پیشرفته MQ1 بر فراز تنگه هرمز منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147331" target="_blank">📅 09:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147330">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df64bda39.mp4?token=i3g3n578DyRmUQow8PADzvWO63_zbskL6CbkmFlWrrnTjODnM1NZO2OtjxEBl8vsm6p5EaCxTM8RM8ORI8FIw22XlyQHRrPJZDZiDZYL32TzKVPNlTAX2oKvfKvlmLXePN4IbCaG82FqNoW5V-dPxa-LoO0BA88RocPmWL_aQIthp4wXZjE982oE7j_DMJzJqidZZtcVKTvAbpb0fN9OA1bTgaIfeMUtYkoyhS1AecOkBsBsUpM8JBcCuANlxN8FWxouVpHVwxWAs4aaHaggyI0KwPUYHh1805-SJLt_6GreUyyG43SRZTDbFepEEWLMhCNB_QCX4ZFu8-yN5M84GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df64bda39.mp4?token=i3g3n578DyRmUQow8PADzvWO63_zbskL6CbkmFlWrrnTjODnM1NZO2OtjxEBl8vsm6p5EaCxTM8RM8ORI8FIw22XlyQHRrPJZDZiDZYL32TzKVPNlTAX2oKvfKvlmLXePN4IbCaG82FqNoW5V-dPxa-LoO0BA88RocPmWL_aQIthp4wXZjE982oE7j_DMJzJqidZZtcVKTvAbpb0fN9OA1bTgaIfeMUtYkoyhS1AecOkBsBsUpM8JBcCuANlxN8FWxouVpHVwxWAs4aaHaggyI0KwPUYHh1805-SJLt_6GreUyyG43SRZTDbFepEEWLMhCNB_QCX4ZFu8-yN5M84GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای خسارات گسترده به یک ایستگاه پمپاژ در نزدیکی
الذِکره
، در مسیر خط لوله نفت شرق-غرب عربستان سعودی، پس از حملات پهپادی اخیر که
از
خاک عراق انجام شده‌اند را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147330" target="_blank">📅 09:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147329">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مصاحبه کامل و ترجمه شده افسر تسلیحات نجات یافته ملقب به "براوو Bravo" با برنامه Minutes 60 پیرامون عملیات CSAR که در ماه آوریل در عمق خاک ایران انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/147329" target="_blank">📅 09:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
استاندار خوزستان: در شلمچه و چذابه از جهت تردد مسافر مشکل خاصی نداریم
🔴
تردد کامیونی از امروز صبح در بخش شلمچه آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147328" target="_blank">📅 09:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1-swAf08RDSZC4oBTRSm5N6X-4yN_OFP5d5RiA8x02yE_sgGKTLaDNGTCi5C1YGpC8W5Qhx3qDXP02cHMvtUZfa7l-gYfWGbtRfGxeKMGk1AOcUPB9qaHsblad_f0rvR_eyoEhvj1BGyVtQT0kkladgn-rIJUOMIpnFOIB91puYEXTJkM1jSLNOmfXAE5QmgMRIkBJMyGQGPkVAqFmV0GajTl9FSKBBSLRbLWJHj8g8rkWKi-zsBZN-jDu9SIeCT49nNGMJukeiqgAo3T0JIdEmo47gWm-pQ1lPpuEo3wwyCgP_3gZHD1lmj06dRPyQk_xyw4H2KqJD3gJSH6jsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی منطقه‌ای در اطراف شهرک المنصوری در جنوب لبنان را هدف حمله هوایی قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/147327" target="_blank">📅 09:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxTgbkJTp9ofM9rhBk5y45LdxiPQeJVVIAtVPQ8fnGHkIaruwe8BzCvUhG2YLU9DATjE78pkDkBE1eI6sX48OCAJCZoLQWaCSiYeW1cCIZuiF6ykPH7xrWaPOBO67964WXS7IFAbcZ2d--4s7mFJ0bkNngyKhQkNjh5qSBkJd8PIDel4tqpu_0XuYDcPSfV9lbyYIbJq36zYGstuPFSk7q-T8CJijqd6Qhfg4Hsf40x5y1gtST9eD6_U_q6LQ9iKBaApr5XRpjLJzwU8J29bbPM30Sr0oJX5uh5edBfO7V6C_1a8N59EURhVaf-V1xMT8P7MB4AXjGcDVTlTp2u0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: محمد اسلامی، رئیس سازمان انرژی اتمی ایران، از حضور در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین منع شد، زیرا اتریش پس از فشارهای دولت های ترامپ، از صدور ویزا برای او خودداری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147326" target="_blank">📅 08:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147325">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9nxM-bTId8YBXFci8_RgkR4nctNskX5Ui1SnPWY4m9YPqtrKUlKT9AweT0YkXtakVkiOC1Zfm4-rBBBP3RU6bW8Bb6G44b0MnbhbXpwRkZK-SCMzDRNDbxd5pkGr_SzFuBTssjWQgfFwqsIHcdn2xa8N7uP7lJNASsnhRt1Xyo61e8kn_t-q4GmUAaJcylg2-Y47nPK4C4ktWAy6FW4Z9lYjvqoGbcSA20Dlh-_vQechlLOGMsIJGJlDKySw0raAJsJxlkCtntBRfsLo38U-W6SpNLKy_mT6cmVJ7FCFOme2cYyCzWnnQ_A5J6QMrq7PnWfTnKa5wFc9rcDLlSYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جهش ۳ درصدی نفت؛ برنت به ۱۰۸ دلار رسید
🔴
قیمت نفت در آغاز معاملات هفته حدود ۳ درصد افزایش یافت و بهای نفت برنت با عبور از ۱۰۷ دلار، به ۱۰۸ دلار در هر بشکه رسید.
🔴
نفت آمریکا نیز از ۱۰۲ دلار در هر بشکه فراتر رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147325" target="_blank">📅 08:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147324">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
خبرنگار اکسیوس به نقل از یک مقام خلیج فارس: عربستان اصلاحاتی را در پیشنهاد عمان و ایران درباره تنگه هرمز ارائه کرده، زیرا از ایجاد وضعیتی جدید در این آبراه که قابل قبول نباشد، نگران است
🔴
باراک راوید، خبرنگار اکسیوس : یک مقام خلیج فارس به من گفت که عربستان سعودی اصلاحاتی را در پیشنهاد عمان و ایران درباره تنگه هرمز ارائه کرده است؛ زیرا ریاض نگرانی‌هایی داشت مبنی بر اینکه متن پیشنهادی می‌تواند عملاً به ایجاد یک وضعیت موجود جدید در تنگه هرمز منجر شود که برای عربستان یا دیگر کشورهای شورای همکاری خلیج فارس قابل قبول نباشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147324" target="_blank">📅 08:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147322">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHSzQZsreUfY3OLp3-h2Zy7LfP9NsQALg-6w55HFW58UoZh12m7EVA0X-1YJHWtYxiDbt_hTzo6CSHJHqZXPXh_JPxrq7ndWh0qoQbgryE8h1q07F6duaicnuQfR_T0ggCFbUV3IqZgpWS-1ozL7uN8FE4xkGsHeh8VMu77FAZ7m-eHjFB4_peZXhhaodaBdnaNNXuG8O6L5m6icWt8S6_io7oXEIH57QijWcp3F5770-EH5rcKoVzNoyGbCjkVNFceH86JcrphiXwvPZdJvJBnY0sf5XWaHwGo-gsAajjnxoz-X0Pemrcn8AkPIqs_VYxEqHMYNz3Qy1NZzonhRuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QU_fqgpsH1MFXnpVRYMsGUUbGZ-tJoBiyB34mOuS1Iu59-3evfJ90Me6IbNhBchjr64ptcbpQ_MpIYDwjxtK1VYqlYDV4utQaXtUdyPee19UqQFIgl9klhpvRZjHZqk01fkh4NdAzJd-PzpeYuKpJthBljdZXZmS5E6Dwc7pgaJqgp-jelruWSCSPXhGicvcCkVKBUoypVY_O9dGtK-8FvKCgq5WRNoSDFe0fD98C0Gm1z2cz1SenojflZaLZBIRt3XX8Ga1_U1tg66XpcCGR5mSX2RUcl009d1tQDzdSJsAVIzDrvtFTO6JXCtxfxrhKDfQHJ-v_UBg-yeuA8DHMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
به نظر می‌رسد که عملیات محاصره شهر تعز در حال نزدیک شدن به پایان است، به طوری که نیروها در جبهه حیفان در شرق و منطقه جبل حبشی در غرب پیشروی می‌کنند.
🔴
این در حالی است که نیروهای یمنی کنترل زنجیره کوه‌های کهبوب، که از اهمیت استراتژیک برخوردار است و مشرف به تنگه باب‌المندب و رأس العاره است، را نیز به دست گرفته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147322" target="_blank">📅 08:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147319">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbdd3f977d.mp4?token=cXRW971AZ_sm124Jc0PC76plv3t2rwNz-NIVBTwOlduXvcj7GFhTkjLwavCSJGW15DSiU7nStqmhva2apbhwgcdY7SijTU2jJvkYFSetYjkPA5uX9cuIqdVflXUyc6HHM5Q4ifJey_iuA16i1l56OTiKbdCk6jk7s7qeJBgpufikAZNU-1O7yqO343BUhhmgi5Lw2xPFEAd7SIb4c8c1CX3l5Gft1H5qofdZo2GKfgjx0n3ms_DnNq2rtjlVB9pztAlWEn1jVNxjlhSE6sKY_C4CrjPSSqu6tW7ls0Ie8gEqmUwJ0-dFA6asyN49pl-Sut6HdToUoQl4VvL2RafnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbdd3f977d.mp4?token=cXRW971AZ_sm124Jc0PC76plv3t2rwNz-NIVBTwOlduXvcj7GFhTkjLwavCSJGW15DSiU7nStqmhva2apbhwgcdY7SijTU2jJvkYFSetYjkPA5uX9cuIqdVflXUyc6HHM5Q4ifJey_iuA16i1l56OTiKbdCk6jk7s7qeJBgpufikAZNU-1O7yqO343BUhhmgi5Lw2xPFEAd7SIb4c8c1CX3l5Gft1H5qofdZo2GKfgjx0n3ms_DnNq2rtjlVB9pztAlWEn1jVNxjlhSE6sKY_C4CrjPSSqu6tW7ls0Ie8gEqmUwJ0-dFA6asyN49pl-Sut6HdToUoQl4VvL2RafnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس آمریکایی تصاویری از لحظه نجات خلبان آمریکایی که پس از سرنگون شدن یک هواپیمای جنگنده F-15 آمریکایی در ایران، سقوط کرده بود، منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/147319" target="_blank">📅 08:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147318">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzlU8SwDGCir8HBVGxpGLKX3hLSMd4iEOwOXd_lH0LLQyhasxlrTBE8jEiwwSeDZXnvuQpBRq7bM00tMdu1SbHnbPKInSHu-lofP2jZCqOOwnjxBqcJLMDMvDgfzpyMTE6dZXBmbzVSmKnaGnDxaKBjBcyIsf1xL3x-tyFR_HraHfk9FJJzmtiBPJzpDZN_94wuwFNdLqG22NGW6SP5BciqSI5wzN5SsEB27y2TCEheHZTM12RmzMSWP6ubuSdTSdnX4P0n7R2_KwcvQzg9_JMPBs_86E5NeOuYVsQ4Cve7PBhr0jVF8oSGX1GqVXB2vuGGPRMtl91fIiTcLJo6DTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشتی نفت‌کش «ال گايا» متعلق به امارات متحده عربی، در تنگه هرمز مورد اصابت موشک قرار گرفت و در حال حاضر در آنجا متوقف شده است. از این کشتی مقادیری از نفت نشت می‌کند و متاسفانه تعدادی از ملوانان هندی و پاکستانی آن نیز جان خود را از دست داده‌اند.
🔴
ایران، این نفت‌کش را در تاریخ ۴ سپتامبر در فهرست تحریم‌ها قرار داده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/147318" target="_blank">📅 08:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147317">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7bOtAcN4yyn1z6Vs5PicBXKoYDvB1XJQ5deSem7MNf1PxCmmcMkAzgMTjNPwovgCmxjgVwMNsq4yv_fl7B1reBZZVds9PIWaLVEpuV6YBtASbrKhf9mPw-RdqITXYVirV_-gMTqUkvgw_XMaa_agXyKH9soW1wIdvzpUbqrSsy38RlhEPVpnbc0fTEtq_0ll2uQzJFA8QLAxPKDAaa3zUyqkDtz36ZtggZqOYbdGZr3702Nx4yxByMog7kGG4NtqjPV1voKPbmpgW0WT8DBbe9ga7yVda7_yZpkiMAuv8TCNf2qCVIj7FC8pcCtE-UwTHA4D3C21zazYLhvsmLs3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
ایرانی‌ها با کمبود سوخت مواجه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/147317" target="_blank">📅 02:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147316">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
خبرنگار: ممکن است نهادهای چینی تصاویر ماهواره‌ای در اختیار ایرانی‌ها گذاشته باشند.
🔴
ترامپ: آن‌ها در واقع همان کاری را می‌کنند که ما انجام می‌دهیم. به نظرم او معقول عمل کرد و ما هم معقول رفتار کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/147316" target="_blank">📅 02:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147315">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap07BY61XRdwsjOcUTiPbzNrkIPFKkymLWedo12UkuUQ7beDzM0hXg-UKPiE5lN9u7EYVC1_3IhTn2W24WJkPxD2-bIkroZIhw-g1k-Rj8IgDHN01-5OfnkLMtU5_WCFK5JFKFnSkBIOTWdwrsEnNNwBIFiEB8saIH3WkvgZ4XmZC7coPhR8pDxGVr6xf8YF1SVxt9Gd6Es4Ln98AKtihFNp8HcVz34QRQXxAU7CsvmdejV1l0lVJM_rNbDBUxRYrp4nE9tewCcq_kr6ATBc3pbWS4qaCduvNbQ1UKBngaVW1k6FdrpE4tA9Pbf7vtoSD-W7s4k53h6G1pUzKw8nrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏
جنگ نزدیکه
‼️
🔴
قیمت هر بشکه نفت به ۱۰۸ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/147315" target="_blank">📅 01:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147311">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj5EgW8ZwSX9T8iZAG4kKoNwhJW6Ss2Y9y7pEgpT9tiHR5dWozBMi4j1Oz_jCyOv1HTBYjtp95z1lY9bC55v_HGpxb2qySuu5EkM1HRaxOLjSQbzdqq3aIl0h2ZNSW-s-nHK22R_WeXPwYgUjkdVSoO23UgsrWT_bQV_sBCJTuFmjzVS0IZ_r1wjNlEaeOKWqqIKXMw4TFQSHgzWFGX1m8wRR-8PYG_-fyGOayUril5bg4AN7G22nyb8rIQkJV0xQrpsBjzRaBKUXG6C5LcN9IQ3hbub5H5aUI5dk8wtFe7FMsBUiR6z7ameSxdTCImgH0NEhlStOn5MP9-IWuK7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b21bcfe4.mp4?token=ARTqF6jpzFy4uLALs3wxqypFqWpRdTtHJYaG75790ub1nUJsD-yKhvrJgIM5vwr5YxtXRrfCTSXENwvoSAR0-8HOcYKMbZpbC-od1kzV-IMrNczYKbnDjgmqHvAprPpXlk-ecz3YbCLVixtXfC45KMqThRXinwEyOEmsa4EQPjkHhb2NO1CFwgg2HX3ZWUWCGaLWOn1sz-Hhj-zRnFu3rEq0_weVqmY3YbDxE6jPeQCAkwy9zr9kG8fHqvRzZLgMP5GPOeXmxaMsXJZGZIhzgiA7B_Pz-nY2flU4CTSEHSpz2YEQf4LhKQQxwzzUBkNQGTC8dVF2WiOJgx9kb8n50w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b21bcfe4.mp4?token=ARTqF6jpzFy4uLALs3wxqypFqWpRdTtHJYaG75790ub1nUJsD-yKhvrJgIM5vwr5YxtXRrfCTSXENwvoSAR0-8HOcYKMbZpbC-od1kzV-IMrNczYKbnDjgmqHvAprPpXlk-ecz3YbCLVixtXfC45KMqThRXinwEyOEmsa4EQPjkHhb2NO1CFwgg2HX3ZWUWCGaLWOn1sz-Hhj-zRnFu3rEq0_weVqmY3YbDxE6jPeQCAkwy9zr9kG8fHqvRzZLgMP5GPOeXmxaMsXJZGZIhzgiA7B_Pz-nY2flU4CTSEHSpz2YEQf4LhKQQxwzzUBkNQGTC8dVF2WiOJgx9kb8n50w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات موشکی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/147311" target="_blank">📅 01:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147309">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6317df925.mp4?token=Dvvm1AM5nJoiwgJphOZ0HsDJ2E2znmZqV22RTGwF1NJI7Uo2TrJhoNQTWjaShJi8e-Aeuwdycj0Sz2yiwseoEfPjfx6gEmv6oajtS_CceD8P9MnUWUzlFSVAn6CUdK0yYu2r-tbEEieejXepsTzgX88fYJJcRnkwk85U04XMqJNh_EFYh3Blz5pWBgszKHz2Yu5ygrSYLgcWuZPkVAWW6c84CvEAOE-RB0wHFBdPE4iYqd5wEJOHsZ3H2vGhrG_V9_xcI5Tf6NJiPhvN68wWSUHXBs8fSgcPIsrFicjOCMYCkVVJqUaOQgwXW-iTj4BK2Bua3tOt9o5vgEpRYuGIgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6317df925.mp4?token=Dvvm1AM5nJoiwgJphOZ0HsDJ2E2znmZqV22RTGwF1NJI7Uo2TrJhoNQTWjaShJi8e-Aeuwdycj0Sz2yiwseoEfPjfx6gEmv6oajtS_CceD8P9MnUWUzlFSVAn6CUdK0yYu2r-tbEEieejXepsTzgX88fYJJcRnkwk85U04XMqJNh_EFYh3Blz5pWBgszKHz2Yu5ygrSYLgcWuZPkVAWW6c84CvEAOE-RB0wHFBdPE4iYqd5wEJOHsZ3H2vGhrG_V9_xcI5Tf6NJiPhvN68wWSUHXBs8fSgcPIsrFicjOCMYCkVVJqUaOQgwXW-iTj4BK2Bua3tOt9o5vgEpRYuGIgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از موشک شلیک شده به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/147309" target="_blank">📅 01:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147308">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری/شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/147308" target="_blank">📅 01:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147307">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1k5DWpcJsm8GyztlsH9cPZEZ5pZIyK4r44Hr4h2p0lIBv_iofAb12FMjCK-Z_pUkXo5ve9U_PeOW4MU1Z4EUj8CwQTFQWBc9ZxUqPFm-7127Zm8k25RwURxCKPVuvYjEeXzNcHuUp8RB21tINz79UGG5yf_IXVb5J2vIWA0AIGgMlWMUCg654mXbjcfCe6jS0H2PhipYVsjrXAA5UgiHDvFdLQi9Orc8qOizsvVh6JlR7JvT_xN4UbOcpQ-qpoeZPSrPOuCJYZ2a383v9nK8DxXgl2p3tGck1-BXpVqV-mUZ1KA2jP4BbCKByU9qBxjbQ-Y-0VqA2-WU-C1N3j_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقتی یه ایتایی تریاکی رو میبری توییتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/147307" target="_blank">📅 01:34 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
