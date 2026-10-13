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
<img src="https://cdn4.telesco.pe/file/OYaIccYs0HSHe5SSD53UpqP8HJRc9wkRTxmLFn31LydC5j1VwvIeP5G5DrhN50cI8hv2L6jHcTlA4DpS3uxodHj6Nx-m-7jMup7LxaIO470jiSnfdovbP5rfU5cYQ437IocM66Fk1_URFO_qsufMJ7mozGS5i429LWL8CfuTC91uSQuDlbPicOZd6uaRef5KDaJN-eP9U820uKsPXBcAu6WIq7sWlSBGPJQa2GGS3Kt0H-dOWhd7vgrJwlaBMQJDxJ5IRqlkKJHsnFzN75HgORBcmpNSJXsWnTezQKIoDNrXnIscWn4uHW-225dTeiY4zAM9gLdtKICGM-a4ZMHwvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-152476">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
اکونومیست: خطر وقوع یک «چرنوبیل هوش مصنوعی» در حال افزایش است
🔴
اکونومیست در تحلیلی نوشته است جهان تاکنون از وقوع یک فاجعه بزرگ ناشی از هوش مصنوعی، آنچه این نشریه از آن با تعبیر «چرنوبیل هوش مصنوعی» یاد کرده، در امان مانده است؛ اما به ارزیابی این رسانه، احتمال چنین فاجعه‌ای رو به افزایش است.
🔴
این نشریه رویکرد «رها کردن هوش مصنوعی بدون قواعد و محدودیت» را سیاستی نادرست و یک بن‌بست توصیف کرده و بر ضرورت تدوین چارچوب‌هایی برای کنترل خطرات این فناوری تأکید دارد
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 23 · <a href="https://t.me/alonews/152476" target="_blank">📅 15:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152475">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
۱۱۵ اورژانس قطع شد/ اعلام شماره‌های جایگزین
🔴
روابط عمومی سازمان اورژانس استان تهران:از دقایقی پیش شماره ۱۱۵ قطع شده و شهروندان برای دریافت خدمات اورژانس می‌توانند از شماره‌های جایگزین استفاده کنند.
🔴
لیست شماره‌های جایگزین
🔴
۴۶۰۱۵۹۸۱
🔴
۴۶۰۱۵۶۱۹
🔴
۴۶۰۱۵۹۴۸
🔴
۴۶۰۱۵۷۳۴
🔴
۴۶۰۱۵۷۳۲
🔴
۴۶۰۱۵۸۷۳
🔴
۴۶۰۱۵۶۱۳
🔴
‌۴۶۰۱۵۷۰۳
🔴
۴۶۰۱۵۶۴۸
🔴
۴۴۸۹۶۳۹۱
🔴
۴۴۸۹۱۳۹۹
🔴
۴۴۸۹۱۵۲۵
🔴
۴۴۸۹۶۳۴۵
🔴
۴۴۸۹۶۳۷۶
🔴
۴۴۸۹۶۳۸۹
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/152475" target="_blank">📅 15:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152474">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4501f8d0c.mp4?token=NetFdR9KRL9l2gbXVy8Pn-7CTjUQvmOSrndjDo4xL8Wf4NDwUtfJeQmYVoX8AJ-a-e3ZCE_PQ6CXVTty9hd-pWTmcBNvdCSEipFpCKZr5o_QuhBWwiXi8ufR8XZQGEPG2Smet-ON1vy2slHIp4NAayGFSw_BWG4JbCV-O1Ba_hnt6G68IXl_gMLsydzwNCJcrz-oGqrzeQ7c0rU0KIaRDVSAGjZMEK9L1SVR09s0DZ7WkegZUVpgHC-8eAr8VH1gkAotTSf0Q_Y8p9Pc8sSNy5MeXJCrQLqU0lubNnJpL5xgoDs957yZPFSgYTs2QiZW_u4ePdmUDLX9XBzjQjhuAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4501f8d0c.mp4?token=NetFdR9KRL9l2gbXVy8Pn-7CTjUQvmOSrndjDo4xL8Wf4NDwUtfJeQmYVoX8AJ-a-e3ZCE_PQ6CXVTty9hd-pWTmcBNvdCSEipFpCKZr5o_QuhBWwiXi8ufR8XZQGEPG2Smet-ON1vy2slHIp4NAayGFSw_BWG4JbCV-O1Ba_hnt6G68IXl_gMLsydzwNCJcrz-oGqrzeQ7c0rU0KIaRDVSAGjZMEK9L1SVR09s0DZ7WkegZUVpgHC-8eAr8VH1gkAotTSf0Q_Y8p9Pc8sSNy5MeXJCrQLqU0lubNnJpL5xgoDs957yZPFSgYTs2QiZW_u4ePdmUDLX9XBzjQjhuAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمعیت هلال احمر: برای هر سناریو از جمله حملات هسته‌ای و شیمیایی آماده‌ایم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/152474" target="_blank">📅 15:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152473">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شنیده‌شدن صدای ۳ انفجار در پی حمله پهپادی به پایتخت عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/152473" target="_blank">📅 15:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152472">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
بریتانیا قصد دارد نقش روسیه در کارزارهای «اطلاعات نادرست» را علنی‌تر کند
🔴
لوک پولارد، یکی از وزیران دفاع بریتانیا، گفته است دولت قصد دارد با شفافیت بیشتری درباره آنچه نقش روسیه در کارزارهای «اطلاعات نادرست و ایجاد تفرقه» در میان افکار عمومی می‌خواند، اطلاع‌رسانی کند.
🔴
به نوشته تلگراف، دولت کارگر بریتانیا این رویکرد را بخشی از برنامه خود برای مقابله با فعالیت‌های اطلاعاتی و تبلیغاتی منتسب به روسیه در این کشور می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/152472" target="_blank">📅 15:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152471">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab51fa2077.mp4?token=RyoL4HPL93-PzCqmxviiZAwMdSSrcvtZ8zb6xP-npFdjTchpPY7aAXa9yJy61yhptleWZNiedVcR9vwbRe3jyMpp1t6yxWxYphSsBA-UY5cPoLxV1baqYfxlv30Ce-9Fn2LuUrYpsleVh4Ki3T1sKLFYWhK1OtJ10KgU_4rvVqPruBPhzWGG3XXQcGiYee0y2ioMncK6lWyvN0gwL90ViTmygoD5pnmztEYS51r6FrsRNrZin-GydNty7XMOK0u5SjmHJ2kGdh-B7jBOAsn7QPxSNCia22TZJAjrDWw_SUHZ7qXG15Kq1C4NtbM3fDLX8nnMcx-5r95698E1uc9ppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab51fa2077.mp4?token=RyoL4HPL93-PzCqmxviiZAwMdSSrcvtZ8zb6xP-npFdjTchpPY7aAXa9yJy61yhptleWZNiedVcR9vwbRe3jyMpp1t6yxWxYphSsBA-UY5cPoLxV1baqYfxlv30Ce-9Fn2LuUrYpsleVh4Ki3T1sKLFYWhK1OtJ10KgU_4rvVqPruBPhzWGG3XXQcGiYee0y2ioMncK6lWyvN0gwL90ViTmygoD5pnmztEYS51r6FrsRNrZin-GydNty7XMOK0u5SjmHJ2kGdh-B7jBOAsn7QPxSNCia22TZJAjrDWw_SUHZ7qXG15Kq1C4NtbM3fDLX8nnMcx-5r95698E1uc9ppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجمع عمومی سازمان ملل متحد در ۱۲ اکتبر، اعلامیه‌ای غیر الزام‌آور برای آمادگی در برابر همه‌گیری را با ۱۵۳ رأی موافق، ۳ رأی مخالف (آمریکا، اسرائیل و آرژانتین) و ۲ رأی ممتنع تصویب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/152471" target="_blank">📅 15:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی مجلس:
آمریکا رمزارزهای دولت را در جاهای مختلف ورود کرده و مقادیری را برداشت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/152470" target="_blank">📅 15:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152469">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: دوست دارم برای سومین دوره رئیس‌جمهور آمریکا شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/152469" target="_blank">📅 15:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152467">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZaSGzaP3nYV4jMmZwyhas92WBu5DwizD6TpX2lJLL3mmtIvJDACClu117NfOwXnZT8WYzemibL1ZizVBkYnSGhkiAYmcDXOpJ2P5qOpT5XL7q75adK82hkdJuJ4svDKh_RMIEamRtS6aR1jeS_p64gwYISjxTh7_dOeiU3riB4XcrTuLQe4CIoNsH6lj9h9L-LydzrGqfNnZn0nMx-5XJ6PbnYz7Btm0jVmvd5rSkGdTHj4eVP_A1dTLOR8xsJfpg_-Yjktt7xqbvFe62vQxwlRoKuWyZene3fAyIdHDv6HWZPY3MOIy3RPxPnjTuYwpLim3tyFPKwxJ_cum-K8e3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WQnzynYjplxJQ9g9vsnY_-jWP5mu1Wx_CpUAUxeNdngfYSCvewQ6OkuEnjAANoNFbz1O9rMOG7y1jg1ugNzFz8kr3CiGexJRR1z1A4c9sMTTdSlsfawf8OII7o-03ETwQoUaHEQEFkUVV5vswh0npHWrZ9gp1-pKHLZWMn2GaQ3Nn07U5Pc-IXsGWiu4qIKUuK-JvZtlcghPc003WAI1Ew_3vfeOIR8wZ15-qKmCeTNb3hUpe28uJdszkB-WHJ2IXnCQOu6JvQtCAa212iqxsXlkjMB5Egg7mtlm2VwSnBKx5oVUI6B4h-I8VjfnrYiAZtJHwW3PMjt-dAEBSTsDhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بوسه کریستیانو رونالدو رو شمشیر و درخت نخل نماد عربستان سعودی در بحبوحه حمله حوثی های یمن به این کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/152467" target="_blank">📅 14:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152466">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=YzVqlMFunQQr6j3j-AzB9AnPX-1_p39OU_LvebNF2K2lZzGPmUnRCdaxyc6-lbOC_iiwU0uZAiPIo2bKh6RteeSVuhYVhNmHQKEmghKWRVi2b0LqmyPX-nbNbT4lyCtY8sVz4U83_ZHdakBdg_RxjgBnxcuvMa0S-9hxM6CoQj-Z5yxRDp6hSzCHFgzQPyIlYp-0PoJ3bqEIP9Kh3I9X35MSUUjMqCSgoKP8vDuYN2Uefgw7-RhD15yEXU-5WgN3ijwj09S9Js180nWCpBUjXrmig64k9Lm1xUI8oLMM4CvFF3tP-V5RGQLCS3p_g25UjIPYF4hqkV81SJdlCi-mHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=YzVqlMFunQQr6j3j-AzB9AnPX-1_p39OU_LvebNF2K2lZzGPmUnRCdaxyc6-lbOC_iiwU0uZAiPIo2bKh6RteeSVuhYVhNmHQKEmghKWRVi2b0LqmyPX-nbNbT4lyCtY8sVz4U83_ZHdakBdg_RxjgBnxcuvMa0S-9hxM6CoQj-Z5yxRDp6hSzCHFgzQPyIlYp-0PoJ3bqEIP9Kh3I9X35MSUUjMqCSgoKP8vDuYN2Uefgw7-RhD15yEXU-5WgN3ijwj09S9Js180nWCpBUjXrmig64k9Lm1xUI8oLMM4CvFF3tP-V5RGQLCS3p_g25UjIPYF4hqkV81SJdlCi-mHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهردار کرج: همه شهروندان ایران کرجی هستند اما خودشان نمی‌دانند!
🔴
آغوش کرج به روی همه باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/152466" target="_blank">📅 14:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152462">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyxqZSKpfNRf3n3ejJy9OEXXj_xGJjsNAV4Z4P8T1GOC06OFEtDeNYJ4DjDPusQbOrvgh61jHDxGVHXuzS1RQUh14OjfAVkL50JcbEsJRtQRCwc8Pu4IKNkJRxvQRdq7z_g62JUeGsPmsiMJnKcRBh7ylh-krgncu0jL-B2pb6IL7QZArrnMAo8KZOslAWAqXBbW1j2exm4kdEXUeCO3za9hvlzdi5GVTw5QXyiCpr5fs2CBm20W_azwN0-d0H0DVGZvzacO5RWctNjsvJejxXAEE38ZgrRW8iQKQWC3z5NiCcmiCDRe6ZgFAho17mNbFQvcKdKSQwwwMT7MG1xnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/huRMwoyTJ2Xe5RKXRzq3tsq0MZg5adxBi6GfeKwnwGHfKR8Nm6FbGcY23GMZpZ4CjH9Idr4FVUZS5kLoNm56OatMe4D3CH14j3U4W2kIRTUT7IfSYRfWP6hAO2tuBJS_DV86BcFdx0QxvGhEXTirnpT7EBts_pELX3SZR9-fMtskPcmyEa72ZbMcSu-mywHAOkKurWQAXliBFz4Q3I8Te4HCHulPG4g4tckEfH0z5nnLt1h6Z5lyPomS3b5CkJ7AbSdrohSkSbX8_u7opbIs6gMp_Rhn-5mpJihCyGPUxMp2OoMWKXz7gLI9OZeLo1MoXd1pCcmQ1KuextLyxTDU4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXU66E5RDRksyfspwii3axDFQ5f7lCeoe1PHIEwz1vWspPXqU5NQCJ-NzDZH4wkBfeFLNrwd4QGYASYuXyk9veG06niOEJykDaWnalZI1E3oHZkuj5zoSZLEQRTz9yv7I7viEDD2Rhzhd2f1i5ilepFL0PhgbiiAhOySlWdzbSrraKYv6qwUpmaKBTd66GlpkBNkjVf-AJkGzTkNBtBcbBgQ8f5BXS_KOKqeZi4uJAaO8L5V3M9hiJDvbnjcFltKjUas4IdoNyLaTmfWqjDMU_MpL5p0sSO4xUmp28P0SIQHcTC1C-9y9TUYOGimmrYBNl7sO_vGh24CTzqYLOzBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SL9gSQ_skYLj6G77k1kKSUArv0v1ExKRXJ4BPqItz-aHPRNeVrwTDen4HzMuhvCFlNjTBh5tBBjSaPbzPo0FNnoKHLJDUY0_lot99uKbu2ipwqkjpguvs5rFKPXPJ2bm1YHs2l45JmvJXYWAFzKc2W5emSnWxNhgczj-hPEXATQmz-UPOnDPooEq8WKdpgr5qFDIBP8wTtjbIXaWXsKPL7-hvyFCAHXzkKvMChqc2-RBDcXSSUh8OnCzdIQOrNuTobJ4ztUVwPWeomb4WSamUPxPw8LisuZNo7x8_nyOjNJbwAbc_bbvHovgkKWdviWelVJSROh-3wYwkYMyjl1ZvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیروز یه عکاس فرانسوی تونست از پدیده‌ی زیبای red sprite | رِد اسپرایت ، عکاسی کنه
🔴
رد اسپریت‌ها نورهای قرمز کوتاه‌مدتی هستن که گاهی بالای ابرهای تندری، تو آسمون دیده میشن.
🔴
اونا فقط چند لحظه (هزارم ثانیه) می‌درخشن و معمولاً بعد از رعدوبرق‌های خیلی قوی ظاهر میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/152462" target="_blank">📅 14:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152461">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر بهداشت: در ایران سالانه حدود ۲۰ هزار جوان در جاده‌ها بر اثر تصادفات جان خود را از دست می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/152461" target="_blank">📅 14:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
حسام الدین آشنا: برخی امور مستند‌تر از آن است که بتوان با جابه‌جایی نقش‌ها گاندومالش کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/152460" target="_blank">📅 14:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152459">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مفقودی ۱۱ ملوان در دریای سیاه
🔴
در پی غرق شدن یک کشتی بر اثر حمله پهپادی در نزدیکی سواحل بلغارستان در دریای سیاه، یازده ملوان مفقود شدند.
🔴
این حادثه که احتمالاً دومین مورد غرق شدن یک کشتی باری در این منطقه طی یک هفته اخیر است، منجر به احضار سفیر روسیه توسط بلغارستان شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/152459" target="_blank">📅 14:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152458">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zpwyo-d1JT1BfQMOUnfeEB3QD0k0MQOMxMBr5qLQueZBaVgUI4148k8A92DNEMT-9zD_D0oSrLQnUN0kwDzrfwMNO7P43fHq4t96oe_nzFLNJUkD-9ugYYQq_rsq3y70crf8FAQ-BXpc5r6ehTrjUmvc2iy-7meRBdXEBspCmXmN-pXYWwkfyHiwlJsIoph32hQSsQRqjT_vyfxww_o6oVv2YfK9Wp_p_e20qigu4DZP7iucaYUXcOgs0SI2WqqeqJRNJcvC81R0sh46d8TiEzc6aA7ga7ajuqePmnjo4WNg3Gk2eoV8Gl2RHyxTETDP3lWBdd2wEzBWJopAxcbv3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسما اعلام شد که ‏برداشت ریالی از ۵صرافی نوبیتکس، رمزینکس، بیت پین، تترلند، ارزینجا تا پنجشنبه ساعت ۱۶ متوقف شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/152458" target="_blank">📅 14:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152457">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رویترز: سامانه هشدار عربستان پیش از حملات به فرودگاه ریاض از کار افتاده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/152457" target="_blank">📅 13:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152456">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
استانداری اصفهان : صدای انفجار در اصفهان مربوط به امحای مهمات بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/152456" target="_blank">📅 13:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152455">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ایلان ماسک: شکنجه هوش مصنوعی شاید به انتقام‌جویی آن منجر شود!
🔴
ماسک با ممنوعیت آزار بی‌دلیل مدل‌های هوش مصنوعی موافقت کرده و هشدار داده است که فشار شدید در آموزش این مدل‌ها ممکن است پیامدهای پیش‌بینی‌نشده‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/152455" target="_blank">📅 13:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152454">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فوت کارگر ۲۲ ساله مشهدی در میکسر کارخانه سوسیس و کالباس
🔴
سخنگوی سازمان آتش‌نشانی مشهد:
یک کارگر جوان در مشهد در حال نظافت داخل دستگاه میکسر کارخانه سوسیس و کالباس بوده که دست وی در دستگاه گیر کرده و منجر به فوتش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/152454" target="_blank">📅 13:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152453">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
زلنسکی: ما در دو روز گذشته، پس از اعلام ترامپ مبنی بر آتش‌بس در حوزه انرژی، هیچ حمله‌ای به پالایشگاه‌های نفت روسیه انجام نداده‌ایم
🔴
اوکراین آماده است تا گام‌های متقابل برای کاهش تنش‌ها بردارد، اما تحقق این امر مستلزم اعمال فشار موثر بر روسیه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/152453" target="_blank">📅 13:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152452">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزارت امور خارجه : ایران و عمان به توافقی دست یافته‌اند مبنی بر تعیین یک مسیر موقت برای کشتیرانی، و جزئیات اجرایی آن در حال پیگیری است
🔴
توافق ایران و عمان درباره مسیر امن عبور کشتی‌ها، موضوعی متفاوت از بازگشایی تنگه هرمز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/152452" target="_blank">📅 13:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152451">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کرملین: تحریم‌های جدید اروپایی علیه منابع انرژی روسیه ممکن است مانع دستیابی به توافق بین مسکو و واشنگتن شود.
🔴
مذاکرات درباره آتش‌بس در حوزه انرژی در اوکراین ادامه دارد، اما تا کنون تغییری حاصل نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/152451" target="_blank">📅 13:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152450">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
قالیباف: باید مشخص کنیم که سناریوی پیش روی شش ماه آینده چیست و اگر در این خصوص اتفاق نظر داشته باشیم می‌توانیم طراحی بهتری برای آن داشته باشیم
🔴
در شرایط جنگی باید مسئولیت بپذیریم، تصمیم بگیریم و شجاعانه از کسی که کار می‌کند دفاع کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/152450" target="_blank">📅 13:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152449">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0Lrxn65f7lznqAom3awlxg_gPxUZH0UMZNGO7XKaMBChNivKSUqrXjkQ6X0kRb6F59zTmpXutB-9IdEgOctlkQ0jzSq15vvNjGrPo6uiAJCqoNgoqD7_9DGs-RsUaUzrKKQ9QU7Xg17nZPopqFf0P15Ryqu5czPVyKk0y77XCkh6yMsYAAwyiHnkm1zxnXgoMxPjEs_XyRnRh-74jRDoFZMYMNYouLjxOYwv8mbwZXuU43EOCyr3BILPhGiZ2PjMILGbsGS_nqYYMdw9TZPRPYQxdgj-0U7ot_MqaZ3EjcI8nchNyJeJUh_8WHEi2CvesWGP8UHKi0XwfFlBDi-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش مشاور قالیباف به اظهارات سعید جلیلی درباره دعوت به وحدت: تقویمِ وحدت از روز گرفتاریِ دوستان آغاز نمی‌شود و در همان روز هم پایان نمی‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/152449" target="_blank">📅 13:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152448">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5731b893b4.mp4?token=H7X15xJIOnhXaieC9eBPZaP7W5xZWOywDpJ9TMhggBjcgahXv9VxmF7yx82Jv8fmNW2skRLmnA-XCqUdLM3kxFRO1jk_AWgtY-_af3THJpZtLchOiBTnl1zzpGw5YUU5ans2voL5_iTRYwTnp3VAkzTI45ull_ahDZftJlk4wxA9mAG7PpOCbg3CbnSIonT34iLg2c-l_mIbofPydZqKLR3bM1ITnwFsVscQv6GkFUC5rJILs-jEprOCcLHmSHp0ICjrlZDJZhmFz7NUr-aHEcbGg3l_xFRq3US_hzaayi28uzMqhPqnuZUIsY4y-vO4wyHPrmHCuZlDB39hGpPX2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5731b893b4.mp4?token=H7X15xJIOnhXaieC9eBPZaP7W5xZWOywDpJ9TMhggBjcgahXv9VxmF7yx82Jv8fmNW2skRLmnA-XCqUdLM3kxFRO1jk_AWgtY-_af3THJpZtLchOiBTnl1zzpGw5YUU5ans2voL5_iTRYwTnp3VAkzTI45ull_ahDZftJlk4wxA9mAG7PpOCbg3CbnSIonT34iLg2c-l_mIbofPydZqKLR3bM1ITnwFsVscQv6GkFUC5rJILs-jEprOCcLHmSHp0ICjrlZDJZhmFz7NUr-aHEcbGg3l_xFRq3US_hzaayi28uzMqhPqnuZUIsY4y-vO4wyHPrmHCuZlDB39hGpPX2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قیمت عجیب هر دونه پسته در‌ مهر ۱۴۰۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/152448" target="_blank">📅 13:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152447">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
دبیر شورای عالی فضای مجازی: سند ۳۲ بندی فضای مجازی امروز منتشر می‌شود
🔴
این سند در زمان تصویب «به دلیل حساسیت برخی دستگاه‌ها، دارای طبقه بندی محرمانه بود»
🔴
سند مذکور برای ایجاد سازوکارهای جدید در حوزه ایجابی و دسترسی‌ها در چهار مرحله طراحی شده
🔴
مصوبه ۳۲ بندی یک دغدغه‌ای بود که در آن با توجه به شرایط کشور، در مورد میزان استفاده از سکوهای فیلتر شده بحث می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/152447" target="_blank">📅 12:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152446">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lz39PkN6jHjskq4HMO16yPp2yNfJi87xg-rL8J9r2pjLd1sOECVrFk6gFaT0DlBf74tjNbbpCpYHfzV0JGIsQNlt7meUv0-6xscESJS9ZW_6vtAgieW8jeuiSm1P1SKajDnsPYRF8E16lZX922BLLH_MyiqN3Yg8zDOuTtOmS_QYpw1-YmdGur0rabNWPBTNV2InHNhZ-oZyPfvJTFzuU3zrYYdXqZCCwkqWN3P4HeQCyEfFtJ8AftjfdN5x-ZuYP_73S4-WI5Qly0kuONl4ErdTm9UPKhfpv5IG95EUYbJ8T8R1-q9PbipvC2GnZciSaGzMTzE0pQBZJyOVbLrOLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر قطر: باید به مذاکره بازگشت/ راهبرد ما مبتنی بر خودداری از سوق یافتن به سمت جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/152446" target="_blank">📅 12:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152445">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
عوستاد رائفی‌پور: آمریکا داره اجماع جهانی جمع میکنه تا دوباره حمله کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/152445" target="_blank">📅 12:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
جوزف حبوش، خبرنگار العربیه: وقتی از دونالد ترامپ، پرسیده شد که آیا ایالات متحده به دفاع از عربستان سعودی کمک خواهد کرد، پاسخ داد: «به‌زودی خواهید فهمید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/152443" target="_blank">📅 12:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
دبیر شورای فضای مجازی: اینترنت در سال گذشته فقط یک بار قطع شد؛ بقیه موارد محدودسازی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/152442" target="_blank">📅 12:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152441">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
روزنامه وال‌استریت‌ژورنال به نقل از منابعی مطلع مدعی شد: مقام‌های حکومت ایران به برخی کشورهای منطقه هشدار داده‌اند که در صورت حملهٔ آمریکا، نیروهای نظامی ایران ممکن است دست به تهاجم زمینی به کشورهای همسایه بزنند.
🔴
تهران به‌طور جداگانه به مقامات عرب هشدار داده است که در صورت ازسرگیری درگیری‌ها، می‌تواند اهدافی در منطقه، از جمله تأسیسات نفتی عربستان سعودی را هدف قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/152441" target="_blank">📅 12:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152440">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW2MFFex45fFDRuRM1N-NSalpKNio8EWej5VY00FQboqxN_WPOgdPTFBzpMRRUL3BjH_FICKKbSf53SU-dviuO5-Tx7ebevtA6ZgC5bbHuKAzyZsf01AmHOCaJd5qCtSMYHsF7GLa0qSm-0MST2c-_6wqi984_sOArj2WhYmc2-Ryd1w1B13eK01zEmBKzr6_Zbw68nRa9OI6pU7LGEfsdLft1tdgjuayTTrDRvZNwJN4TkHK-Jq9TFFlH0L2snK6zHtM852wsNmMReX4DNvUlYxg7ph0f_Gz_cMknHlnQispLkxHrzk_016dbt-XK8ivXq4DJ9yZXDIaX3p8Fhz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌ها از وخامت حال رسایی در زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/152440" target="_blank">📅 12:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152439">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xupa3fb9VlcQCFjWGcqRpcaGVwnmAp4HlKOdJlXZBRXVPziDFFVtf4v0GJdnVCFY9qsgWJnEauhFz4Z2PhPpYNBeM91aOwE1-PHKAjP1LPJbp6ITG2dPz5VlGIzS3ZE_4duR2vWkZzGaF57Kjw6UkKIeoBEW95FT3-DbbgAMY-OA_gcBZ7f3mg_EdZAxQKkCO2qVcywj8ubJlsJuGXeEfx96hWp3n7VqGXXkHgdn6TF1a9LorPUlgvIDuPsg2Dg4g9aUQF7ScmjzzGm16Fa68B8Ml430maKREgIIyqSM1ThlwVi5zWotNNxF-a1dXr_rQonqrpj8WLoU-RnhlYsbJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧡
اتصال بدون دردسر
گیگی
4️⃣
تومان
⚡
سرعتی که حسش می‌کنی
📡
با دو روش مستقیم و تانل(پیشنهادی)
📡
مناسب همه اپراتورها
❗️
و مخصوص تمام مصارف
کانالو داشته باشید از تخفیف ها و جا نمونید
❤️
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@VOXNET_BOT
☑️
چنل کانالمون
👇
📣
➡️
@VOXVPN_NET
☑️</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/152439" target="_blank">📅 11:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152438">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
شایعه درگذشت میرحسین موسوی بار دیگر تکذیب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/152438" target="_blank">📅 11:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152437">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سخنگوی دولت: دولت قطر در مورد خلبانان ایرانی قول مساعد داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/152437" target="_blank">📅 11:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152436">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_7f583hhfQxcclfB6fCINqx2Wp0l0aVgkqz9ZvJjJ-HhGBp3DsSgV6T3x8kf0ymVhsvRtAt84pyE0Rsod2fglB_G13sSESSbtjRe85fA-NaOPVe1qTXWJbVFChJ2mNEBlaI-RTM8pBf7iroVXdxIUiNjKKwx1V1H8V2jErtXNdwCbpLXBCF5DmxwnkhK49qIbNCPE0g0CDh1PB6XJJTScsm3l0OSuOjrhAyiFJnSCaQkLeN_qPqgvcnU30Xg8KZ-y_m68Qy9qj5OxEUBRBt_fPghrL_lylHB0lBbTVzIs8R7sjH6-w4WHrdlMdbeFuUSbMUUvSzqSKB8wB5HTH0CZsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_7f583hhfQxcclfB6fCINqx2Wp0l0aVgkqz9ZvJjJ-HhGBp3DsSgV6T3x8kf0ymVhsvRtAt84pyE0Rsod2fglB_G13sSESSbtjRe85fA-NaOPVe1qTXWJbVFChJ2mNEBlaI-RTM8pBf7iroVXdxIUiNjKKwx1V1H8V2jErtXNdwCbpLXBCF5DmxwnkhK49qIbNCPE0g0CDh1PB6XJJTScsm3l0OSuOjrhAyiFJnSCaQkLeN_qPqgvcnU30Xg8KZ-y_m68Qy9qj5OxEUBRBt_fPghrL_lylHB0lBbTVzIs8R7sjH6-w4WHrdlMdbeFuUSbMUUvSzqSKB8wB5HTH0CZsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: شاید در برخورد با رهبران [ایران] زیاده‌روی کرده باشیم، چون دیگر نمی‌دانیم دقیقاً با چه کسانی طرف هستیم. راستش را بخواهید، برایمان دشوار است که بفهمیم اصلاً باید با چه کسی سروکار داشته باشیم. به نظرم زیاده‌روی کردیم.
🔴
می‌توانستیم در همان سطح اول متوقف شویم؛ رفتن به سراغ سطح دوم و سطح دو و نیم، احتمالاً زیاده‌روی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/152436" target="_blank">📅 11:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152435">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی دولت:  در شرایط جنگی، حفاظت از پایگاه‌های داده و خدمات اینترنتی اهمیت ویژه‌ای دارد و انکار نمی‌کنیم که گاهی دستگاه‌های متولی ناچار به کاهش سرعت اینترنت می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/152435" target="_blank">📅 11:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152434">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a28d4b0f.mp4?token=Y2bfyb3pheLrRwQ-ufhsaJE-j-_7e2L1Qx0YkW6Ozni7iY1Pcd0tzXlbSJbollT_BOq1yonPqbHPQb85VqTVL6Wd3OQXQcFddURJZCs4SwewVp79hDvgJCFTKo6cglr0hUIJGcnnnMEyKBeGZiiz78Ib_ZVZkZyxhUZg3gS7CMv8Sqr2a4X99iH9qG4JvkpK4-TrLvPvayDpqSx0eyl6R6Gp7GCuAxs-Iq8B_2iHah5txI6rQzecEGtoDnNZbjznrdIsxHqPHwEaqIl6W3Y_qw_K7IZFvnohmqSdxXX0OwBWt63xM7YwIb5xl95GWWNfpfwtATrGi9rqRk1jtC1yrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a28d4b0f.mp4?token=Y2bfyb3pheLrRwQ-ufhsaJE-j-_7e2L1Qx0YkW6Ozni7iY1Pcd0tzXlbSJbollT_BOq1yonPqbHPQb85VqTVL6Wd3OQXQcFddURJZCs4SwewVp79hDvgJCFTKo6cglr0hUIJGcnnnMEyKBeGZiiz78Ib_ZVZkZyxhUZg3gS7CMv8Sqr2a4X99iH9qG4JvkpK4-TrLvPvayDpqSx0eyl6R6Gp7GCuAxs-Iq8B_2iHah5txI6rQzecEGtoDnNZbjznrdIsxHqPHwEaqIl6W3Y_qw_K7IZFvnohmqSdxXX0OwBWt63xM7YwIb5xl95GWWNfpfwtATrGi9rqRk1jtC1yrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو ژاپن یه زن 29 ساله برای خودکشی از طبقه یازدهم میپره و روی یه دختری که داشته از خیابون رد میشده میوفته و دختری که از خیابون رد میشد جونشو از دست میده، در حالی که زنی که میخواست خودکشی‌کننده زنده میمونه!
🔴
حالا قراره این زن اعدام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152434" target="_blank">📅 11:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152433">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات الونیوز</strong></div>
<div class="tg-text">👈
پلن ویژه افزایش ممبر برای کانالهای تحلیلی و اقتصادی داریم جهت اطلاع از شرایط به دایرکت پیام دهید
دایرکت</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/152433" target="_blank">📅 11:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152432">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7088d734.mp4?token=vvUGVT-Hbgz9P3gDxYGCcaK_K5swkdmHuXjiRA1andyqq_sOWeL6___0GWG4E-L3pVL2hlQA8-0maYTmUEhbkxH13TW1hUuFCY1_eMUzMT_TqF7k4MGjRlXjBukNzTm799CIdAuT4uqYPsJD88vZG1xT8Zpz-3YXoH2pbg543stcybxtLzK7PPpYXCav5LtUVQaDXlmGJjPLi_x8xmYwqSpo-WcXYYIKQNedwoCbua0GdduMKkuG63dI-o9X26RmM8CaE7eO4xUWmRbKbHzFP28bOi61m3zvYAGqwGrjv46ihAmmPMfIkxs__HulNWAYS4RYpKl9rtNr3ldhclRT2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7088d734.mp4?token=vvUGVT-Hbgz9P3gDxYGCcaK_K5swkdmHuXjiRA1andyqq_sOWeL6___0GWG4E-L3pVL2hlQA8-0maYTmUEhbkxH13TW1hUuFCY1_eMUzMT_TqF7k4MGjRlXjBukNzTm799CIdAuT4uqYPsJD88vZG1xT8Zpz-3YXoH2pbg543stcybxtLzK7PPpYXCav5LtUVQaDXlmGJjPLi_x8xmYwqSpo-WcXYYIKQNedwoCbua0GdduMKkuG63dI-o9X26RmM8CaE7eO4xUWmRbKbHzFP28bOi61m3zvYAGqwGrjv46ihAmmPMfIkxs__HulNWAYS4RYpKl9rtNr3ldhclRT2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی نشتی گاز در ساختمان دانشکده علوم دانشگاه علوم و تحقیقات تهران، این ساختمان برای رعایت نکات ایمنی تخلیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/152432" target="_blank">📅 11:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152431">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifSdqTPZUwgGrCWOPfIOKCQGJNcyKV18Y3n9RB4pE8U2EUyfmucPT0bs-qVlrat9IAEYNLi5CwyfkQASwiDQDTEdcJaWII6ctmxbeFV29PNNSZL2gOzQb4OW0ho6al2ADSLeK_nR7gbhkRy1hW_iXEfRygEsv_Mcf0_184P4EeOPDeOlfRbfsBHP2R6qPxbw4JOeF5arBeZ2P5-1hZjiyT_KH5q4ZjdmFbt1JayR8-vj1Nd1i9E7cMcvnIUWBY3PTtXicnH9-WQAMBeZ_efCVYrtRQyrPp7tVeo3ALuW5C8FfHxpeJjYSnRV8TROYxEtWg-_GlJ-H6Td8lKrF8AiVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا حسین طاهری مداح بخاطر اختلاف بر سر مسائل مالی دیگه تو میدون انقلاب نمیخونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/152431" target="_blank">📅 11:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152430">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e36cd10d5.mp4?token=czc8HuxSzFElqQGQAPXPZbcpI1Dr58gHI3Iw-Vvxt8IuRskHX_o0O_10EuNdzmR9es_eorBRXwx97vODbRC8q4ZCOhIHXd6IE5UZu01Nduv9GHBF41zM1s4uT0pX8dki1Qx5_p-agsTciJJ7GO7oLKe5J5tXAdU68wqK_G4hrKVdbnrhRfFPbmJFLwrXKwNzluY-QqqW240NYG8RMywaVW70ROx-IUnnsjNUyWfa1lHJJqZ1OAaBBsa2eSn-g0mC3BVBvbh0Z1EXBiub6CPmCejJPYvHb8l91q5NmiqMeMGywbZri9xQn3Cx-SBgMPKObnk119eUKO5OK4LbnLhvpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e36cd10d5.mp4?token=czc8HuxSzFElqQGQAPXPZbcpI1Dr58gHI3Iw-Vvxt8IuRskHX_o0O_10EuNdzmR9es_eorBRXwx97vODbRC8q4ZCOhIHXd6IE5UZu01Nduv9GHBF41zM1s4uT0pX8dki1Qx5_p-agsTciJJ7GO7oLKe5J5tXAdU68wqK_G4hrKVdbnrhRfFPbmJFLwrXKwNzluY-QqqW240NYG8RMywaVW70ROx-IUnnsjNUyWfa1lHJJqZ1OAaBBsa2eSn-g0mC3BVBvbh0Z1EXBiub6CPmCejJPYvHb8l91q5NmiqMeMGywbZri9xQn3Cx-SBgMPKObnk119eUKO5OK4LbnLhvpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجرانی: واردات انواع خودرو توسط هتل‌داران و ایرانیان خارج از کشور متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/152430" target="_blank">📅 10:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152429">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8IEg5mwzUEcp9WSWMReVX1EffxCyl0upxKjE0doNklLSXuFQhCbll0L93xfg6wnvhgMmhRrQ3_OEblhQ-u-X4XJ35FrO305CinQAQhnNN33-d_S5OjLPhQQ_6a1ZKAAGV4oPI9YssYkNfnoRqn4YbRXVU_uBqptXIqQlFQK0JUZYiB9dlifET0tFTnDqxlX-A2E33z8eoIfyTgYHFZQCEt7pUbGVp3pRUThaPiI3Fnb3kmFcwsuoGt_3RzjFw2e9KwbDauKnv9MeLuscSuKa9EP_WmCtYA7lj0RFSSg2HJaj5Z2NDElXfO--D1KAYhW_yrChYbj5CnX3T-7CnsWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: آمریکا داره دست و پای آخرش رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/152429" target="_blank">📅 10:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152428">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه اینجا رو بخون تا از بازار جا نمونی
👇
👇
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/152428" target="_blank">📅 10:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152427">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf32100694.mp4?token=qABVahiYsmkV2z5-zQWT3lSGy7Y4phOmM1NhjNk31PLvTVhFOFzOYYwfFii8mq9oLy4RTd5M4jYqzd-Kr7p8cp4LnKhWGlBwAzQKNwmoj7WrrUfNW2fBmjd4h36zTLE49EXPSGJwFUrJZMkm9nSV4ZWQH8ctSp3GWy6pPpYUX76At51yQ2HWOL4v6NKjDJBqPOOOWWKOgC8uXBbue6g0KWfOQ6dhIQF17yFCZXUIoijlYsV3Nj37FfoBVpyuCXU4BCiGVYdzNQzM8b52HN2yVJPw8SgoaXyCjR75z8FJJUdQ2BxR6tYBl_KEPodxF_5nptNpomD6UHouwXfAlYpJxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf32100694.mp4?token=qABVahiYsmkV2z5-zQWT3lSGy7Y4phOmM1NhjNk31PLvTVhFOFzOYYwfFii8mq9oLy4RTd5M4jYqzd-Kr7p8cp4LnKhWGlBwAzQKNwmoj7WrrUfNW2fBmjd4h36zTLE49EXPSGJwFUrJZMkm9nSV4ZWQH8ctSp3GWy6pPpYUX76At51yQ2HWOL4v6NKjDJBqPOOOWWKOgC8uXBbue6g0KWfOQ6dhIQF17yFCZXUIoijlYsV3Nj37FfoBVpyuCXU4BCiGVYdzNQzM8b52HN2yVJPw8SgoaXyCjR75z8FJJUdQ2BxR6tYBl_KEPodxF_5nptNpomD6UHouwXfAlYpJxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش وجود بمب در هواپیمایی در تل‌آویو
🔴
کانال ۱۲ اسرائیل: گزارشی مبنی بر وجود بمب در یک هواپیمای شرکت دلتا که در فرودگاه بن‌گوریون فرود آمد، منجر به تخلیه سریع مسافران شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152427" target="_blank">📅 10:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152426">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
صحنه‌های ویدیویی ادای سوگند قانون اساسی بر نسخه‌ای از قرآن کریم در مجلس عوام بریتانیا، توسط «سغال عبد الولی» به عنوان اولین نماینده زن سومالیایی در پارلمان بریتانیا را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/152426" target="_blank">📅 10:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152425">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کارشناس صداوسیما: بعضی رضاخان های حزب الهی به دنبال این هستند که مجلس و آرا مردم را تعطیل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/152425" target="_blank">📅 10:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152424">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=L9H0h7uLxdfzZLgPR0_9MHGtlg9qw55NrTHHpkwbnvlMiYN7g4rEHtcY909DcOwGC_-a1ejVPRYchBnJXhzAmB3Ju858sLM1s10kWvN8F_orSPRXn53Br1UNS-g-jpbwEtwWpEGGDV1L6VbpzSz9ab6HNCstFQavux6Dp-UexaFgcBCDHfKbR-vne9FephD3hLXLbDWPomoK5URL7205LITnXACyu9_8BVrA_rTB6zbhwcADsQG_y0z9W0oZn9DLEHq4ayJaQkmk-tGcPE-_UouBPE4ZoUh6xLy3ypplRVdx-w7PlxhVvzMTdrVjqj7NbEuruVivyvqwZnO98yvuNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=L9H0h7uLxdfzZLgPR0_9MHGtlg9qw55NrTHHpkwbnvlMiYN7g4rEHtcY909DcOwGC_-a1ejVPRYchBnJXhzAmB3Ju858sLM1s10kWvN8F_orSPRXn53Br1UNS-g-jpbwEtwWpEGGDV1L6VbpzSz9ab6HNCstFQavux6Dp-UexaFgcBCDHfKbR-vne9FephD3hLXLbDWPomoK5URL7205LITnXACyu9_8BVrA_rTB6zbhwcADsQG_y0z9W0oZn9DLEHq4ayJaQkmk-tGcPE-_UouBPE4ZoUh6xLy3ypplRVdx-w7PlxhVvzMTdrVjqj7NbEuruVivyvqwZnO98yvuNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: ‏شما گفتید که روسیه و اوکراین به توافق آتش‌بس رسیده‌اند، اما هر دو طرف می‌گویند که به این توافق نرسیده‌اند
🔴
ترامپ : آن‌ها به توافق رسیدند. می‌دانید چرا؟ چون من گفتم: «شما باید به توافق برسید.» به همین دلیل...
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/152424" target="_blank">📅 10:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152423">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز: عربستان در پی حملات مداوم انصارالله، تعطیلی فرودگاه ریاض را تا روز شنبه تمدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/152423" target="_blank">📅 10:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152422">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آسوشیتدپرس به نقل از مقامات منطقه‌ای: ریاض تحقیقاتی را برای تشخیص علت ناکامی پدافند هوایی خود در رهگیری حملات حوثی ها آغاز کرده
🔴
هدف، فهمیدن این است که چرا سامانه‌های پدافند هوایی، پیش از حملات هشدار لازم را صادر نکردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/152422" target="_blank">📅 10:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152421">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
شرکت هواپیمایی اتحاد ایرویز پروازهای خود بین ابوظبی و شهرهای دمام، جده و ریاض عربستان سعودی را به دلیل «اختلالات منطقه‌ای» لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/152421" target="_blank">📅 10:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152420">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5nBdZ352nKatRVRTRJ80pF9jWw0E6_JTdnWCEKYriuDbvFawv84hoMTw7WNBX76h3vNc0s32s5caqJ7GN5JnrCAZhmOPC6PazQdolWgmKGwOEBoGReyqbLY7ZiTxVFKBVtdJngLXqvQ_3VG84TG5CEtnKDorC4ZFB4f8KZ_Of7NbXailLcF9puYyrfHl0fyYZTH-KBTSENYjR3jAyQmKJSMFxZRYXfb0sTcda6JKiiJ6iaSYqWXgvN3VvGvgWyVfTzCdxOnnMqPQeggqvBw95awm7LP7BhQYx8V35V2AQMgIXM-1UAkZT9bGs9psXlaVSKRFpxUFp1UZJvOtnnaSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایت دیوار پر شده از آگهی فروش سبدهای گل دخترهایی که به مناسبت روز دختر، جعبه گل هدیه گرفته‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152420" target="_blank">📅 10:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152419">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ : «ما در جنگ با فساد و تقلب پیروز خواهیم شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/152419" target="_blank">📅 10:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152418">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ : «گروهی که بیشتر از همه دوست دارم، «همجنس‌گرایان حامی فلسطین» است.
🔴
«همجنس‌گرایان حامی فلسطین»! می‌دانید اگر در آنجا همجنس‌گرا باشید، با شما چه می‌کنند؟ شما را از بالای یک ساختمان به پایین پرت می‌کنند.
🔴
شما را به بالای بلندترین ساختمانی که دارند می‌برند؛ البته آن‌قدرها هم بلند نیست، ولی نیازی هم نیست بلند باشد. شما را از بالای ساختمان به پایین هل می‌دهند. با این حال، من مدام شعار «همجنس‌گرایان حامی فلسطین» را می‌بینم.
🔴
نظرتان درباره «زنان حامی فلسطین» چیست؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152418" target="_blank">📅 09:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152417">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ : «اگر دموکرات‌ها در انتخابات میان‌دوره‌ای پیروز شوند، من آخرین رئیس‌جمهور جمهوری‌خواه خواهم بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/152417" target="_blank">📅 09:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152416">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
امیر قطر: مسدود شدن تنگه هرمز و خسارات وارد شده به راس لفان، منجر به توقف صادرات مهم این کشور شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/152416" target="_blank">📅 09:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152415">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
هشدار بمب‌گذاری در هواپیمای نیویورک به مقصد تل‌آویو
‏
🔴
در پی دریافت گزارش‌هایی مبنی بر احتمال وجود بمب، نیروهای امنیتی یک فروند هواپیمای مسافربری را که از نیویورک عازم فرودگاه بن‌گوریون بود بازرسی کردند. تمامی مسافران از این هواپیما تخلیه شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152415" target="_blank">📅 09:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152413">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QhRsSudSOsgc3uRqo3V7PwGcFUwkhOY2Fa2KjYvvuOt6PxEDY_mRCpwzc0Od-WwJhAyxP45GQMMl-MkItKXdkL2_1vgUKmqGW7jClefFXf6ZK-Q5LvSPlNjQRWlU8srY3dVqwndxl2lCvHvZASNNbf-TA9qt3pEWVpaSkrUgXYBNb-ZJnGgnGvJGqtgu55em_no5-7hRRyYzQM5pquKTj9tvcDWvWE3VhPOtlq8Ci1Dc2bes2558BZNk7E0lnpG4DKNqyGN39EkrpSVUCI_H-nY9ZMkyEaYhwO1ccY52d-kVoNCmppqEyuUWRbasrWfE0Ud1UmGEyzVqOdnBrO2_KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JlqJfZNnM0uUeGw3L3Zmhai68kyixEW4KgXMWQtRDr_C3yEd-Qgqj9kHPD-igaqGM78JuXdedg4eq_iyJ2gSYsd65EGw897mPlfIs0b2nX3vmoiM7hEmfST9SNKYzNBmScg-XwwzaHq2IOXiFJfCZswcROX5IL1VbdVEEMzl8XLRi36uOropQ3dqyHI-ASOip-XTJXp7qRONnRF-KGT0XBSJqf4T8NJum9HgEN5-xHre_HUPwz8_AOi9ojlAnsNVQKVDzNsQDMjN8GNHwb6zw_7wTlSRJzA6xBeJ86vgeI7kKzBkF0SZnYLtT2MdKu5pbnTVPQHU219FgFkVaTtfsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
محمدعلی ابطحی فعال سیاسی اصلاح طلب، تصاویری از سید محمد خاتمی منتشر کرده که مصدوم شده و با عصا راه می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/152413" target="_blank">📅 09:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
آغاز رزمایش اتمی ناتو در ایتالیا
🔴
رزمایش اتمی سالیانه ناتو که برای حفظ آمادگی نیروهای هسته‌ای این ائتلاف نظامی برگزار می‌شود، با مشارکت ۱۷ کشور در ایتالیا آغاز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152412" target="_blank">📅 09:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وحیدی، فرماندهٔ کل سپاه: هیچ قدرت فرامنطقه‌ای حق تهدید، حضور سلطه‌گرانه و دخالت در تنگهٔ هرمز و خلیج‌فارس رو نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152411" target="_blank">📅 09:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152410">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: با بن‌سلمان درمورد حملات به عربستان گفت‌و‌گو کردم
🔴
حوثی‌ها خیلی بد دارند رفتار می‌کنند؛ این اصلاً خوب نیست
🔴
ما عملکرد خوبی در مجلس نمایندگان خواهیم داشت
🔴
فکر می‌کنم پوتین بیش از زلنسکی خواهان توافق است
🔴
روسیه و اوکراین بر سر آتش‌بس توافق کردند، می‌دانید چرا؟ چون من گفتم «توافق می‌کنید»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/152410" target="_blank">📅 09:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152409">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5921718ede.mp4?token=QrQUiADOZHhFCoIqeQ3STF6EUY5diYYFjHaHhqatuqqJyPAgWAQ7PXWQ7LNzF52TrQStdB-fSb9H0p5KYuMEJ9NhTL_LHfqboXbIcLk50TN2bhK-opCUAS5o0JpLgXhDBKRoANqhIzYt6p4IKuYH410Hp24IvKU8kvlNv1yF1PwuXz2hvA5y6oBS4Mo8D7wm5vyfZqFDiX_gqAPuB0zQiASPfVclEsz19xLsvcPWcwHp-NGxKreHiNIumJu0jqg95rc33wItcwwM_ALRkUwKPEVI_VqPGAzYOVxdlXknuytMfcr_nOQqlPf1gQyt1rnoNo3UkNlS4sPDTI8hQIKEz3gcYBWE7wgYkgBUGWbEz608nRi015pAVus8KQkH-hmxRVyBDahUZRb0KdfkC9o41ALecmD-s_UnPYkO2kbvPH0cElxZLCUm3Kj-JNrVkGyy16yEArwZZSguYrfTPlzpkq9AFM4gaW_CS90PX1ggbao4LYndnJfJcyhvv9kSe4Ie8GOhrqYMIAPyCbR5FcjFCZNjC0NzAcIE3EuPNAe6TF6V6ga9r9Lgbk4Fy2BasZJ9rRe0385X_Q-6TxDwL76VIsCh4H8b7pbI3aVVE0f_Yfe2br8ozeQZ956RiWv6Vhtv668fXa75R0VJVP60SAIoNKnMC6Eg1sCYEirsCgvIcJI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5921718ede.mp4?token=QrQUiADOZHhFCoIqeQ3STF6EUY5diYYFjHaHhqatuqqJyPAgWAQ7PXWQ7LNzF52TrQStdB-fSb9H0p5KYuMEJ9NhTL_LHfqboXbIcLk50TN2bhK-opCUAS5o0JpLgXhDBKRoANqhIzYt6p4IKuYH410Hp24IvKU8kvlNv1yF1PwuXz2hvA5y6oBS4Mo8D7wm5vyfZqFDiX_gqAPuB0zQiASPfVclEsz19xLsvcPWcwHp-NGxKreHiNIumJu0jqg95rc33wItcwwM_ALRkUwKPEVI_VqPGAzYOVxdlXknuytMfcr_nOQqlPf1gQyt1rnoNo3UkNlS4sPDTI8hQIKEz3gcYBWE7wgYkgBUGWbEz608nRi015pAVus8KQkH-hmxRVyBDahUZRb0KdfkC9o41ALecmD-s_UnPYkO2kbvPH0cElxZLCUm3Kj-JNrVkGyy16yEArwZZSguYrfTPlzpkq9AFM4gaW_CS90PX1ggbao4LYndnJfJcyhvv9kSe4Ie8GOhrqYMIAPyCbR5FcjFCZNjC0NzAcIE3EuPNAe6TF6V6ga9r9Lgbk4Fy2BasZJ9rRe0385X_Q-6TxDwL76VIsCh4H8b7pbI3aVVE0f_Yfe2br8ozeQZ956RiWv6Vhtv668fXa75R0VJVP60SAIoNKnMC6Eg1sCYEirsCgvIcJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار علیه لیونل مسی در تجمعات شبانه!
🔴
خوبه که فرد ذلیلی نباشیم
🔴
مثل مسی اسرائیلی نباشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/152409" target="_blank">📅 08:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152408">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قطر و امارات پروازهای خود به عربستان را لغو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/152408" target="_blank">📅 08:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152407">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یونان در حال تدوین قانونی برای ممنوعیت استفاده کودکان زیر ۱۵ سال از شبکه‌های اجتماعی است؛ قانونی که انتظار می‌رود از اول ژانویه ۲۰۲۷ به اجرا درآید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152407" target="_blank">📅 08:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152406">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGMhlHeGCi-gShFxCtBBJqkKuSMFCRRz4F50eAr5MEEcue29xDBqx5OswnaOGatw_9R5e8TTcc_JURYTCAJMX-BMe6RZUOFn6ost6aP_rfm0Anwoudx3iOs6GMUKgMJsNJxVd0BCvy7djREM412es46OzvxslKoTebd3AXZRkjJIOgugx0U7qJPp2w2IkynvqoP2wsqCcJCh81oqQfp2ITgsDjdeLue66SVDoPDJ_DWeru1g5owASqIqy_xt3oXDXwfOcMIqC4P3ikK4w2NMtU3dxyvZQP92_dTBh9P8GeSD-N-31gVuxS0nOarAQNAu4HQm78x5NN7de5cSZSf0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من نظرات زیادی از چپ‌های رادیکال احمق و دیوانه می‌بینم که چین و روسیه به جمهوری اسلامی ایران کمک می‌کنند
🔴
اگر هم کمکی می‌کنند، در سطح بسیار پایینی است، اما من اصلاً باور ندارم که چنین باشد
🔴
آنها چیزهای زیادی برای از دست دادن دارند و ما خیلی سریع از آن مطلع می‌شویم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152406" target="_blank">📅 08:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا می‌گوید ۶ حادثه در تنگه هرمز و دریای عمان طی ۲۴ ساعت گذشته به وقوع پیوسته
🔴
این بالاترین تعداد حملات ثبت‌ شده در تاریخ این سازمان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152405" target="_blank">📅 08:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152404">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از منابع: فرستادگان ویتکوپف و کوشنر سفر خود به روسیه را تا زمانی که زلنسکی روابط خود را با ترامپ ترمیم نکند، به حالت تعلیق درآوردند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152404" target="_blank">📅 08:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152403">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqegBWLJ9wGOTENPYR2N3g4QYgv6Nx8KrkEA5aQMjEMJgW7Lhsen-6eYm4AtLJ9dYrvRT0VGUzlOLWq5WtDSCVSHCcXuusQ0HHVWuWll1y3G5yBq9PmFAYFXD1IoKaVEXzGaQxx2-mzJKhy-EB2buoQtvfkTkhwvbcQ52CfcIRknVWZtMlab0Vf97VrReE9RMoskfX0k3rcstIu9xC_4ECNKoXn3EqgzhLIGsNSdPu9H272RJ1xoIPXIUcW5r-i3QsoRd2SHRhYOj_l8H4Uqm3W7RTyt5kU6q1crri_B63jC3U50mWWjcIevuRXfcpr6dMtfkKqLJiolN_TfNAjJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامنت عجیب یک ایرانی حاضر در لایو زنده نتانیاهو.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152403" target="_blank">📅 08:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152402">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7JhuapcbVR1jZoLlCzd65VhxxAtUQOmmFZ1WTKe18-M9a8z-zuirh7lXNIlPdX9Qm2EiheFqbXANBU2-UzWIp2EXZSymOpgSf72DUWKUJACtGxxt-FOgI_nzHnuCtfMDX0nH33pWLUS39nhGOx_p9OYSG_PFKdGs7p7L0vmCpPWnOaJdLr0stkHJ5YqHuKiW6Xkpd_pMMbXLsgmHusMy1QNhVKfKFMDu10FhAdsACs7R7pMu0KElmYWw7FI269UNfTLQl2jllrenfgewKXZb6xWvb73LK6IbuRPPcfGZRVJI1ukdpQsEWZ2j3Zdo2s2YOQ5RRA85YLhoRWM4ofk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
آلن ایر، عضو سابق تیم مذاکره کننده آمریکا:
احتمال انجام دور دیگری از حملات آمریکا علیه ایران بسیار زیاد است‌
🔴
ممکن است آمریکا در تلاش باشد ایران را به حمله اول تحریک کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152402" target="_blank">📅 07:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152401">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: روسیه و اوکراین می‌خواهند به توافق برسند، اما نفرت شدید بین رهبران دو کشور مانع این امر می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/152401" target="_blank">📅 07:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152400">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2615637194.mp4?token=nnwfoC-2c9q6ZcLlNZytGSd45iPm287EVgJuLE_-Nl0pFu_ePXs2PrZ-uV3X2_NP4zQTVrqQtva_TK_cnVR8gMot0_KpJ3wJdgTz7J8lqGQl2XhAhQXYb7eHod1vseM9UQbuUWKg-tLaWL-mPYkQk2xN7ufMLzXHnb9gGqWxNpyaOrAnM8hQ5S7w6KpezbiGziTcIYz_b5hI9pbQfO-L5RNusiZB350dFBfz8L3zX6gJy7-Ng5Gwde4FHBWOotzyFvHqXNNoN-rRp6QW4q6lVlmz0wZnQ7VQaorwaUb6EwIM3FabCbSUJh6-MJzjcRG6Mqbd3jpXxUeIAUnd5sutcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2615637194.mp4?token=nnwfoC-2c9q6ZcLlNZytGSd45iPm287EVgJuLE_-Nl0pFu_ePXs2PrZ-uV3X2_NP4zQTVrqQtva_TK_cnVR8gMot0_KpJ3wJdgTz7J8lqGQl2XhAhQXYb7eHod1vseM9UQbuUWKg-tLaWL-mPYkQk2xN7ufMLzXHnb9gGqWxNpyaOrAnM8hQ5S7w6KpezbiGziTcIYz_b5hI9pbQfO-L5RNusiZB350dFBfz8L3zX6gJy7-Ng5Gwde4FHBWOotzyFvHqXNNoN-rRp6QW4q6lVlmz0wZnQ7VQaorwaUb6EwIM3FabCbSUJh6-MJzjcRG6Mqbd3jpXxUeIAUnd5sutcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران به دنبال توافق است، اما نمی‌داند چگونه!
ایرانی‌ها دیگر نه نیروی هوایی دارند و نه قدرت نظامی، آن‌ها می‌خواهند به توافق برسند، اما نمی‌دانند چگونه باید این کار را انجام دهند.
روسیه و اوکراین نیز همین وضعیت را دارند؛ آن‌ها هم به دنبال توافق هستند، اما نمی‌دانند چگونه به آن دست پیدا کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/152400" target="_blank">📅 07:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152399">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTURBO VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9oRsymSGQfdS8h2j92Csf43k4-zW37GvceuGTeqdhaRzDAYfnSbZCw0Xvk2poSPi5jMjWWtE-dDNnsrvoMZVkEcWgG0qDWdk5VSe8kecz6aXcGCvOpkaIo1EO3Ru9AeEXNC7Zc1JsrLgwo6Cm7Ygbh_sOpmn3SgSflHgrWA227Vtezi3PzFS-0TD-VL6lZXe3a-DM0BMFpA83WQu9sL-XFk_t6Y_wayaN7MSHHorbfGyrdAH2gu8H6WJyk4cbnCLAFzMAIbe5uzvQyydqoWVj69exQnznv2fllCFvTjE92ixrvC-MxRTX-4D3lBoe2fiHo27mgBM83fu2FsQP0cPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
🔥
قدرتمندترین سرور WireGuard ایران آماده شد!
🚀
در روزهای اختلال اینترنت، با تلاش
شبانه‌روزی
تیم فنی، سروری قدرتمند و پایدار براتون آماده کردیم!
🚀
🎮
مناسب گیم‌های آنلاین و شوتر مثل
Call of Duty و CS2
⚡
اتصال
سریع
،
پایدار
و
پینگ پایین
📈
مناسب
ترید
و بازارهای
مالی
❤️
ایده‌آل برای
اینستاگرام
و استفاده
روزمره
🌐
IP ثابت برای اتصال مطمئن‌تر
🛒
خرید از ربات:
@turbovpn_new_bot
👨🏻‍💻
پشتیبانی ۲۴ساعته:
@kasrazandi
.</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/152399" target="_blank">📅 01:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152398">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر دفاع سابق آمریکا : هیچ راه آسانی برای خروج از درگیری‌ها در خاورمیانه وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/152398" target="_blank">📅 01:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152397">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKjrK7lYknHRYwaJGYcud6JFV5zmHd_qnh1xfamLExloeMS-8LvRzxoZ0k6Uaje2ti1HIfLf9DuJ3Xl0SiWjsNDrUNe30gNBd_UMiKKSuG4bSYdGCKEY20qF_Nqagg89zpbq-C6iyGrpEHT9A92yF1t4874SF3tkJ4v7pAPqwitQEZIfQh57kiBhutFZHJaFGY4Xz-uTenwf9fOgKusSt49LIc23eFVnOkZV01nLa-eoCI8zMxhYQxdf8ijFAGDcsFp-UV8E5rTODRhc3Jm3JXY-kX-GL8us4KRmxF8_CXPyyjNEFaXxYJjBK4J92k22tn9r8rbRIDqJ4TUkYhxC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم: به من چه بچه‌ام جاسوس بوده؟ مهم اینه توبه کرد و آزاد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/152397" target="_blank">📅 01:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152396">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: ممکن است با کیم جونگ اون دیدار کنم. این اتفاق هیجان‌انگیزی خواهد بود. من با او رابطه خوبی دارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/152396" target="_blank">📅 01:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152395">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-poll">
<h4>📊 شما به عنوان یک ایرانی از صنعت نصفه و نیمه اتمی خیری دیدید؟</h4>
<ul>
<li>✓ نه جز بدبختی چیزی نداشته چون هدف ساخت بمبه</li>
<li>✓ اره کلی برق و دارو تولید کردیم</li>
</ul>
</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/152395" target="_blank">📅 01:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152394">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e3835b1dc.mp4?token=f8s3o3QjhQ9jcDNzA7YaxzvfgGTLusAPMK2zMvFXtFykjiFelRIkOGct5A5LXOwSTww1OpgO_KKBf4n0v-nxpv1lJBM200jF5XBDcJecqM_pHb1TOWr6YiZ7SpSe5JL_csw9kwQjcJ6h7yVocN9BmMdbcWuUtnswFH-JTCfI3LOTylcbcWlBeYe3wGL-w_UQQjc9cGdjRnVaAUjCb5-3kiBqq6BSCBqWFYBeAHUvhlGjEInJUrpLgmIq6ehYARXyzf6nrI35o4XCDWFaMEw1NPI5z9dleUutSi1MsHNgoooZTLIsirMb_czOJs9yqDZ35vkyfeQap6ySKdnKAEyLTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e3835b1dc.mp4?token=f8s3o3QjhQ9jcDNzA7YaxzvfgGTLusAPMK2zMvFXtFykjiFelRIkOGct5A5LXOwSTww1OpgO_KKBf4n0v-nxpv1lJBM200jF5XBDcJecqM_pHb1TOWr6YiZ7SpSe5JL_csw9kwQjcJ6h7yVocN9BmMdbcWuUtnswFH-JTCfI3LOTylcbcWlBeYe3wGL-w_UQQjc9cGdjRnVaAUjCb5-3kiBqq6BSCBqWFYBeAHUvhlGjEInJUrpLgmIq6ehYARXyzf6nrI35o4XCDWFaMEw1NPI5z9dleUutSi1MsHNgoooZTLIsirMb_czOJs9yqDZ35vkyfeQap6ySKdnKAEyLTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
رفتار حوثی ها اصلا خوب نیست، حواسم هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/152394" target="_blank">📅 00:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152392">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⚠️
دیدن این فیلم برای اشخاصی که توان غم زیاد رو ندارن توصیه نمیشه
🔴
اگه کمکی داشتید میتونید از طریق زیر انجام بدید
👇
Ir150130100000000405720701
5894638800062288
موسسه فرشتگان دانژه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/152392" target="_blank">📅 00:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152391">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: جنگ با ایران به زودی پایان می‌یابد و قیمت بنزین در آن زمان کاهش می‌یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/152391" target="_blank">📅 00:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152390">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/152390" target="_blank">📅 00:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152389">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اتاق جنگ اسرائیل: به مردم قول میدیم تا قبل 5 آبان حمله ای نمیکنیم ، مگه اینکه ایران حمله کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/152389" target="_blank">📅 00:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssnfY1jqXYaMgmf3qE-J0pIyCD-hU7lsZtvSIVMc5eONpqJuR6xcY8FEBpTr3vHz1-nzIW4TwlcxhiUuZ8Hd2ZSLRL5cB2QKo5nKQINMxoBunEA3e-KakB0c0yBis6qTk6hGX7Leekwflnx5B2ziQ7odOnlL5RYRHysTFp_BdkdyyvPnlBaS4hJOB-vmSTzLcWVZefzyp9dCi7Xu-Yv-IeoeaiP2DbIO0FZ2h_nFV91D2BhRTpGZ018VUjRSAZkSJHPTjsU4buSfAuOLgjbHzg9_usyS6UVfsvJPrAvCTooPPsXlWxrqs-t_usbJK-SYVsHhDdQLqiW7m8WXqDJ5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgPjintR1f2ccHaPeOQAdlMloDcZlf12mHnBxXH50b9wWY_1f3qv41yb0oJ-sacKxlfDBIgNd0J730OnIOAQ7s4KLQxEdsCcTUeEMNUiEjhFVqLKxZnV5dr9w_SG7MKzsxsytmSFsrhWha2Hunyf4sidHjbpUlo9868GDZYwkePaGSiH91-DCPAPnLPP5YzmqcEI2ecXQKc_m-RU61rsWtDKzUBQExFxCC4k8QJd-uXbrtVO7Ya4N22qF5xZAwgsqex6_YYBYXAXU5Yi3ZIIeSZIQF7Ke_lMUc_xJYL061dg4trqyTqWn321yR7ffmfvrUmrlGGQqsXbTBWRwVn0CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بازیگر سریال "بریکینگ بد"، آر.جی. میته، که بیشتر به خاطر نقش والتر وایت جونیور شناخته می‌شد، در تاریخ ۱۲ اکتبر در ایالت تگزاس در سن ۳۴ سالگی درگذشت
🔴
به گزارش‌ها، او به زندگی خود پایان داد و مقامات اعلام کردند که تحقیقات در مورد این حادثه همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/152387" target="_blank">📅 00:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCN5yJ-GJag8sl6-l16ZdKldlhOOjt4Y2Lfco8FG6jGrmV5mDAwUVZJuvKFh5igtEg9H0satmORw_-LSVC45EOFWQvXZJ_PxDAa49BtLuvb_6tiRjfCQpDoc3cbr6LdBbOObrMnwS4xH1eti7RQtq_uKI-wYs7jP9sQ4pYtq0X201CQq_E33ANNbPvRizwB2SBgR82o5vMap79tgD2I9irAzwxLw5-yjQ08hC9iFuUl1wKJ7gDEUpxk7UiuGpIBm1ktTEIFNFGEphszMGU8qc4P0QD4_Pl7O6fYnHoml96AQ97WfeayyEiZJX_Uao9HaxOkzZ-kEW2LdXJF7kbXZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مطهرنیا:
آمریکا در نهایت ایران رو درستش میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/152386" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152384">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfmN0CVpvzp_h65NCzlFOzcoUn-u5We4oBk7Q8VBR0YHrbKlRVT6VeOAUlA_qWmiV0ay6RVG2qdRh7GFynPeY97folDffX7sLJIeHjF0_-Bf37ISlFJW_uhO4rglovbmmBQpI_AVcTOHdyeQEUqVX6pDMnxiPhKp7fnAp8mfSJtzvchw_YYmsF0Zs07MMUFQ-2poJ6aZIDV6VBtBss0pGtdq3oE_rZd_Wj0r-en_veX2tLaN2PCxGoL-dFFDF1XJFtOzcafvoRx18gXTbr7irR7_66x-GFgNYWdkRH2FC1vO-EfsdoW3SWQs7oNf_mBksyZ5TF1S3YDyxy8hdgcOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2zwInt2RHheGNpEpSZkYBZ_nRypzYiafMH_ix04_9f5YiXWhoBSBiyMDb6vv1cQRVB1VbsAbtQMxMAJuglT6rW0dt9IbFmsg0QBYqmpZrWvfPQX4LC-SydQWjeajBxOxdeujjfjpQD16wBZ6sJz33lym3CvTTo5kIj3dCkD9R0lpLmezbjrb23ytZLsP5RA_FnqIxbcRk7pG8UYLjW6satIzpITNwOBwv7vriOTdgJNDbPLpbNf-Qo9o4MYoQc28RfGkALlNCw1IJ4YGWvc6jWUAFT0Myw27K1IzCZYOkSLzc6U8wiHK2gXeMG_2jEuUy-k22cMXlli7RAmqgqz9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ادامه تعليق پذیرش پروازها در تعدادی از فرودگاه‌های عربستان سعودی:
🔴
نجران و جازان: بیش از 155 ساعت
🔴
ریاض: حدود 57 ساعت
🔴
ینبع: بیش از 28 ساعت
🔴
عرعر: حدود 15 ساعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/152384" target="_blank">📅 00:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152383">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بارزانی، رئیس اقلیم کردستان: تو جنگ نزاشتیم از خاک ما ایرانو بزنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/152383" target="_blank">📅 00:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152382">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI3qdQaNb_A8MkeB_1V8SSdkqZv8RD0bfnJ5nb00P1UoxU8R-Ks8XfdPCddJRQV1Ti54murpFssWaiPiggZsUBgll6Nn1kmdlS21n62DV1oxFbiAkGTD5APQVhLUeJuamuJVMNRrIEuwLBB2yrDvhdxttT1x_QP8Cvsp0CYLEiW_qLcIhrrPemRd73GxHc2idp85aycg7VQvirzB3CAgy98OfcigraBHN4Wl1tHZ6lK-9k1YSQEvutVAggbio3n7mDdj4ixiC3lMViUm6KowSNvBpgDXhWyr3uFu8seby8uwWrGano-Ti8PskUvfihe3iAmMCAtfqIgdM52zTB0RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازار ارزهای دیجیتال خبر از جنگ میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/152382" target="_blank">📅 23:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152381">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
هاآرتص: نتانیاهو به عربستان گفته اگه باهامون داداشی میشی میام براتون حوثی‌ها رو کلا شخم میزنیم ولی بن‌سلمان فعلا مخالفت کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/152381" target="_blank">📅 23:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152380">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">جدال تیم‌های میان رده ایران و قطر با پیروزی ۲بر۱ تیم ایرانی تمام شد
@AloSport</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/152380" target="_blank">📅 23:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152379">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVHK9pH1SLK0EvznqERpL91dgicYlDgYRPDNPy8D0fqDXaxW9YzZOqZILUGjb45vrqCtfiEOV8xpwyjyhOTZGkQDi3g4NcmBNxzJMEe6SplDt_DzHZVuvryaDJVJ7fd3Q5RT6QJYqfreVdpzy89PQdW4cxrI9gcVs_rqvdTiuBjvL3tw514bIZNzO3D60tU0l7yfGx3QTcM6H5PGbgc9z2qUh60XxLr2StkzmiCEoRb_BAic1JyY52T0vr-ghW1qMEBic0nOVJDj7F-CElkLQouW8TIRe6TKvM5Bj96G-YzBSoZmopdM9ZnRbUJqxraxnPBiWvhO-cpHqciLK-FJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه جده دوباره متوقف شده است و حدود 5 هواپیما در حال حاضر در آسمان معلق هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/152379" target="_blank">📅 23:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152378">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
هم اکنون قدرتنمایی جنگنده‌های ایرانی در آسمان کرمانشاه، در غرب ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/152378" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152377">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وضعیت اینترنت کشور ۷۰درصد افت داشته چون احتمال شروع جنگ خیلیه
‼️
🔴
اگه سرویس متصل و پایدار حتی تو قطعی میخواهید سریع تهیه کنید
👇
https://t.me/voxnet_bot
https://t.me/voxnet_bot
با پول یه پفک اینترنتت رو بیمه کن
✔️</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/152377" target="_blank">📅 23:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152376">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
عحیب اما واقعی
‼️
🔴
ایران اعلام کرده آماده میانجی گری هست و عربستان قبول کرده اما یمن قبول نکرده
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/152376" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152375">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
منابع خبری از شنیده شدن صدای انفجار در شهر ریاض پایتخت عربستان خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/152375" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152374">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
عراقچی: وزارت خارجه استفاده از ظرفیت‌های دیپلماسی را برای تأمین منافع ملی با جدیت دنبال می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/152374" target="_blank">📅 23:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152371">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/McasVo8tSoW8jFFeSYWEFpTYdcBiQpy8BnHQ9095X5lRhxG1bmwms80ZI-EEJmykZM8jZWQ38l_9MI5TnBmg_PIXcePW9i5kJS0-x4kAwdCPwG5osYBj-SBrjDdP9PF0xpECcS2OeTgQkbrdFsrRyXQRmWcn_HTFQQ8PFdFvtym8tpyfGCI7OfLHxJTnuwRgGb1EI3jAgcdiVK6oqJVaiuj4apgBZ3UYspx0y8aaBrERCMcawCTDHXPR0Itf_-9Y5J-Mjqlc6ewTjw8vn0q-PHGdZwz3fXyWfTIfQoe7x0H3_ow3AzMHQrSJRGg5aTZKh-Yuz5bjx1jHKkkbHVKLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q33R9TSmsvKklE5FJ071blOpej87oYfHJn4FS8_Ah48jnziiDR6fP7wL9j7PEmMtYmtay4El4BIMsQAcGgbqDWeby-lDdlkp4bfE_dyr9iiYKD7GfcPIP-8TH6VVZpCkJU3mKozOFcGSc8vFP4rTvYThkjrrNE1IqD3WGfR5XH3spFJOQmXLg7fZB-yS-MYKkIPit7BvntylQu9ayTfljQ64OIeePbykvp94beruVXRYfCxDZEQpkoSFon966Khoci_Wz_4agHb7jYTgz3aybHMwRbHA1IgnBunk6wZnp_12rd9K75YwojBrQnt7rQmamywjf-aolE9vdEuiQS_G7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQFkXm01rS6JkyX0iyI8RlLvhB1qN4_fZ4mt5mYLGtI4YFRDdjILDzo4jZP8YaKKkPTNS0sB1-CA7BzQr6UVmG6jEThMOb62K0Y8fOx4geuuZPlqO7mBl5-VCcjNGbChlL5Ww6HxFpZTZI1SyWvHs_uhdwZRA9XZSuwpxhU6mYdn7UmYEfdNwl_swA9uKK9lpmeG00bNE0N1u75ABd7y3Y2y9v7ZoYp_uNnYVypScNkemQq1uaIQl8SItACB0CNh3b5xlMtFYUEoNPhKlcHSzf5Vu0rpCDPLsX93yvAq_2lvu2G_bKOdYqfjSYMixB3lDAwfJl0fQ7HPXs53sxsv8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حدیث ستاری، دختر ۲۵ ساله ایرانی، به عنوان زیباترین زن سال ۲۰۲۶ در خاورمیانه انتخاب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/152371" target="_blank">📅 23:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152370">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!  @AloSport</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/152370" target="_blank">📅 23:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152369">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔵
سوپر گل دوم تیم دوم تهران به غرافه   @AloSport</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/152369" target="_blank">📅 23:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152368">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKXY2nmMGtzog5e0F3PyuJ0RlJ-07ZA2VblGNdpnQi-dqF_OZ0I_zdzXHA7KAfwbkTJ0IrhwVCqZNp94AEdWZfaBt1EhF7YRkV2p0OxDh7_YXjdjh5C3CQ8WEGcEOk5LcTK7ZM1GoAhYA8jdQ3DEn3WF7le5rx5D1ALnlZJHYwm4fd2nasynkVkZjirpe4Hg6udLTFhZhR-z3--lL2pbCMaEwWjmN5yyIZGmAeGyPoy0Rnb1WYkHhZfVw8MKXnncPmGtgfdpNGnXnYEAv0rI_91jxl0PemakCkkw3vL2OdlQ8ES79fr5fg4BOvbLZJQcn4PhV4hz42vPsbCTXCzKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با اثر پرفشار جنب‌حاره‌ای روی ایران، روزهای پیش رو هوا گرم‌تر از معمول می‌شه. دمای تهران به ۳۰ درجه می‌رسه که حدوداً ۱۰ درجه بالاتر از میانگین این فصل میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/152368" target="_blank">📅 23:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152367">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: نفتالی بنت در رقابت با نتانیاهو برای نخست‌وزیری پیشتاز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/152367" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152366">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / ایران برای میانجی‌گری میان عربستان و حوثی‌ها اعلام آمادگی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/152366" target="_blank">📅 22:49 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
