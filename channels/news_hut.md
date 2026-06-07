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
<img src="https://cdn4.telesco.pe/file/jwa-aGPNbzZ3bHB-Hhx__1Av4pwuR4mBTOGMKUVXnD3aZd0dNnj4uY4FQDnzBeYn7aplP0jhUpfHIrWY85IuIl0ph8s7h9Ka9KrOulKjt_qgl4nGo9rzNwmCUOQmRMxTFdCrFMbX8tvI0kv2--qiMuKeriVBoHynElbGYS1KOsZbXOuvny7cWIHeeqLNRDoFboiuy5JjKVmcDE1RqOuuN2dp3Fz9VA8di6p3xAGBBJEPvLnzY1ZVlYrJjAIPUyIW8Q_4Mo8jiOUgI93DyfL9TmXxepE6i-HjhxWhy6l1JBoYVT4X-Adifqa5nLHPtfMk09u3oJYSs-TlqcFdopoVPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 227K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 19:37:35</div>
<hr>

<div class="tg-post" id="msg-65373">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQKn-GtgpxrpooK3bz7_xDEL6emhBwaDP2_5aO_2LoK1m0dhR9mvPQQUSCcS-xk4oXCQZqT48P4sjLmd43cIgVbJkPGNkX2Y_ipSIl_a7N_E5_kJbXgQUELVfCkmQ1jFlqrKZjPntsFe6sycPAWPTi7qMbR-IhI3AAcqjFa34reXsdowJ8jQDwtL-Zc4fubwlMVsabwh1VKpnSr_W9e5ik429JcC_b9JMDjy8n7Pp7jNaZuP_9KuR5q0GOmx6ViROLAUCGpKX13sJUTk568Ub1uNsapWZxhT6dM7Q34Oy5HhlpY6ifdHWiMXrwk8siS3OyaEwzZ7en_vDMttmAWN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۱۰۰ روز از آغاز جنگ توسط واشنگتن و اسرائیل گذشته و به نظر می‌رسه تلاش‌های ایران و آمریکا برای دستیابی به یک توافق موقت جهت پایان دادن به درگیری‌ها با پیشرفت ناچیزی همراه بوده است.
همزمان، وقوع حملات جدید، فشار مضاعفی را بر آتش‌بس شکننده فعلی وارد کرده و دستیابی به صلح را دور از دسترس نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/news_hut/65373" target="_blank">📅 18:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65372">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با شبکه ان‌بی‌سی نیوز گفت که اصراری ندارد لبنان در توافق کوتاه‌مدت میان واشینگتن و تهران گنجانده شود.
‏ترامپ گفت که به‌عنوان بخشی از هرگونه توافق، دارایی‌های مسدودشده ایران را از ابتدا آزاد نخواهد کرد و هیچ تحریمی را نیز پیشاپیش لغو نخواهد کرد.
‏ترامپ در پاسخ به این پرسش که آیا این اقدامات پس از توافق انجام خواهد شد، گفت: بله، بعد از آن. اگر رفتار مناسبی داشته باشند و به تعهدات خود عمل کنند، آن وقت گفت‌وگو را آغاز می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/65372" target="_blank">📅 17:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65371" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/65371" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qabe7FDBti2E5ig5tLeUb4N7t9uwa-iCrIjYF5VrkpjsNjDKpDg5PUnAAF3qkFWf7FQ8_9Rk0cDikujZRqMCWWETfkZ5AH9pe2doEA3eB7y04-ypH--D4udA8MsanosqzzTChup2pjv5nfD5oPiOU8v1BB3gEnRv2ULS7jfr9TxFgF_YCddmGuwcBOHYmM9FYYeZ_Yg8fSyHI8L0PH4xvxMqdkV7Xlo7awZDn97r5ulDd3OA0h3MJ3esh_5u5UnCWaXkzEvkoJnSv5Y7lmxs56bzNf3QfwufCKwaEp32_EEZL_BVdTyRAkdxe90kjwJk4yUHb1hAXtt2Hu9t4JCH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤼
روی مبارزات با 1xBet شرط ببندید و شرط بندی رایگان تا سقف 100USD دریافت کنید!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/65370" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: احتمالا بدونیم مجتبی خامنه‌ای کجاست؛ اون از پدرش عاقل تره!
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/65369" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیما: منتظر واکنش قرارگاه خاتم باشید  @News_hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/65368" target="_blank">📅 16:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65367">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم   @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/65367" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65366">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65366" target="_blank">📅 16:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65365">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65365" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65364">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Shl81rMs3B0EitHN69bXH48alS9gStDt8t0SwZkyu14yiKOXFX-XI85aeyPUfGwmUzX9O_dn5P8QcyTzzD3fc7IyQa3ELX0rWkxawHe6SoYHwQiTTjAglOPKY3g0vUwmWCHsKUpGDqejan3QE5K1D6YmnKe0o84kqL2_YWfcCeNv2WLIs0kUS_GpdTr0-NyjIXnEh67FewZHVoEMZD5mBbPLvTrMDvLWWroITQI4BvNpzdBmk54LwIW2X7aGkO83KdPdRL0ayJKotMlHYLKEwFuBhwJ-TQUsNt6RAS6MAc-i_GPX6CQETeHFgUpmOKyRnkjhI_4PrW70VKBnNZq2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65364" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65363">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ اسرائیل رسماً به ضاحیه بیروت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/65363" target="_blank">📅 16:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65362">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGL_RAkMaJtjoxyZmNig6Ye5rFK70-BEFwc7P0BTfWOskwaSrsuNfMyg_3GMXb1ZH4aOyGN9PRF61EhVYXklbrPzaD23J0lpTOmoQPDEZIks_d156KO-eMGtwPCoW12nCx8QbG0VS_DgXgeQkDt37otinKYOF30TlIBeGMQra9OMnXm1zrzqZsnv_iwkjaIypOSWrNaWwYYoGM5kdNoAfLzlFu0E6sF2gPVqJoK1PYjDmZJSyqi0JfZutng4pxmAjsXXrcANbyvaderA_QqnDkUrlbAzfHkc3bnjkD_nSpKpD6uhifwMQmkDlPFap1YYQ3815Z3GqOmr8VUAwMo1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل امیر تتلو:
توبه «تتلو» از سوی دادگاه پذیرفته و برای طی مراحل نهایی پرونده به رییس قوه‌ قضائیه ارسال شد، ولی هنوز تصمیم نهایی اتخاذ نشده
اینکه موکلم برای ماه محرم درخواست مرخصی کرده تا بیرون از زندان مداحی کند، حقیقت ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65362" target="_blank">📅 13:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65361">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=bMlkyRnoIi7-41K95GCjFhYyNYgFKnuqtUkn1Ionse66VTW2MEAccDqvakRiapZiNMQFgUxiv1ROQ3yEp2NaF27ucAMwE4a_M2I7naAGxVLpOKfu5Iye6bbO3UI7E6y5ik57S-9MmJW8e-YSAaTk54k1EWyj6DXtBX6twW1gXU_gKqjlIC3vrpkj3eJOIcexrspVlOjM3ImMpdZHv3NEY6dZogGdNM6iR46Xbx49rG5IsqqQnYelIJH15EAvVgyFpuv2u3pIWqC7ZxuFdbJYflmo-zQWHv_yIOCVW4VfP16yst1XYhVkPEQQTJ2rrORio05ru9nH-083A306rKUMhHgeMQ7xJ_W3fvG46JWE5GD6eprZXMBc9IUoUtbCMfLw5yZsllI8dF8y8tUgHLGLa7-5nBwvidTVvscA7I6kYUKAFvqEvn9v93ShJVr37E8e5ynrcJtW875RLIUfNB4NhyZyZlZq-6nBilkd5Gb13crqhMNWl19_nz8nKQpGgm6DcBBs1LaLY6fWLipPIBHC8aTQDJqQOINzBkhGctyBKN5HFSdNCA0EVXPzUm5biu69z5T1-HZEkVprIcJvExt3KCt5DPxHzAFwrrTx5_NOvx_2QbLbS81r-ZwaJXmL0lENAYA0HDoSUY4TAx-pOUscEkW_kLJvRJT3nh_4zS7fxe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=bMlkyRnoIi7-41K95GCjFhYyNYgFKnuqtUkn1Ionse66VTW2MEAccDqvakRiapZiNMQFgUxiv1ROQ3yEp2NaF27ucAMwE4a_M2I7naAGxVLpOKfu5Iye6bbO3UI7E6y5ik57S-9MmJW8e-YSAaTk54k1EWyj6DXtBX6twW1gXU_gKqjlIC3vrpkj3eJOIcexrspVlOjM3ImMpdZHv3NEY6dZogGdNM6iR46Xbx49rG5IsqqQnYelIJH15EAvVgyFpuv2u3pIWqC7ZxuFdbJYflmo-zQWHv_yIOCVW4VfP16yst1XYhVkPEQQTJ2rrORio05ru9nH-083A306rKUMhHgeMQ7xJ_W3fvG46JWE5GD6eprZXMBc9IUoUtbCMfLw5yZsllI8dF8y8tUgHLGLa7-5nBwvidTVvscA7I6kYUKAFvqEvn9v93ShJVr37E8e5ynrcJtW875RLIUfNB4NhyZyZlZq-6nBilkd5Gb13crqhMNWl19_nz8nKQpGgm6DcBBs1LaLY6fWLipPIBHC8aTQDJqQOINzBkhGctyBKN5HFSdNCA0EVXPzUm5biu69z5T1-HZEkVprIcJvExt3KCt5DPxHzAFwrrTx5_NOvx_2QbLbS81r-ZwaJXmL0lENAYA0HDoSUY4TAx-pOUscEkW_kLJvRJT3nh_4zS7fxe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با زنده شدن دوباره دریاچه ارومیه هزاران فلامینگو مهاجر بعد از سال‌ها دوباره به دریاچه برگشتن
😍
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65361" target="_blank">📅 11:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65360">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZcZVouJ1EXlnQooayhyo-dh32Hga9Xef7_WZip0rghbA1FAiIG_UwqBWdsdA9B9j53OImfpgpIYIyTtFTJdG_IORHuOOYrmQRAvu2k8r4p_Od4DQGu1Lg2nPQLhc4dWhVyS39727HP4h7QSzGiPQDG_GDPBPX9B4pCRvlDbao_k0_a7DWvbJZF38O33HYTokYHNaFfh90UekH4bbr4k0y1OnL7jtYkH9nGicrCcmvg2fOxLxDGpPFAN4hp7Bzzi-0t4qRQim2GrpQWrgRiaDNXvjKNB9FZCOLGxv-TrXV0zuEjeguGPbEvl0bIBJvrBWjbFqP3whZ_Q8bULmt9p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خوبه خدارشکر بعد از این دوتا پویان مختاری هم برگرده جمع نخبگان جمع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65360" target="_blank">📅 10:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65359">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SprInxUKQUyd3NZk_O1Iv228Ri8gdy8SOB5_cVqHWxpc2oZLgxs8Wbqai-TJ82fkp3ZWJxHbTm18FFCn_jmxpChZ4GuCZ1Hh59o2NGhJn-4b5F4fzfL4-vk1p0QQ6-vyqA7-ZNaC2ieJ_T6K4Fqv2Vyp7BifN_0dFnhzjfVs3LbC_MClo1KO7MzKDI_j30J8VetRQ4NHpyuG_V13wZqerW9J7fhhpdzQzxmO3z766UBuB-0_thtI_tn7P6UovRnGn7RiAu-hjFAgoSL4HJorto-EIygWOFwSHUq8a_A7243w8z_XXaezqBcmfx46kZog1nqyOnnN4WkdwRfG4rerMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش یک میلیون تومن وجه رایج مملکت از سال 97 تا کنون
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65359" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65358">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884f21c214.mp4?token=pupjp8FpClfWWvoI1wSKqwaI6sdT2l1MEQOfkYne2UOT4wIFyXVXsHagcsOAkwyYdjr6d32ffA4ObOGWD2br0G_hMsLn81LT6ntrGmOD3bTNN6GVOS6XaJGEyN_3OrTOdMLQSoqa014qFYpqFBm5XJ0fJew9iQehGtqD7z28IMiZBkTRMcpCAnEeMnNueSzo851e_b3CLZfy_bc9izncFnTkgQk8lOLs7YC6Lu-4F-Q2wkYlz9mYSrBiR6zJb_OZNmfW0lfQ3GrW-wDuthghxwoa4kduDGs6mdUUfT0rYTzfHFNTGhXRiDXudxKKOJJQlCq-Yfm9m9NO-ZZal9nvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884f21c214.mp4?token=pupjp8FpClfWWvoI1wSKqwaI6sdT2l1MEQOfkYne2UOT4wIFyXVXsHagcsOAkwyYdjr6d32ffA4ObOGWD2br0G_hMsLn81LT6ntrGmOD3bTNN6GVOS6XaJGEyN_3OrTOdMLQSoqa014qFYpqFBm5XJ0fJew9iQehGtqD7z28IMiZBkTRMcpCAnEeMnNueSzo851e_b3CLZfy_bc9izncFnTkgQk8lOLs7YC6Lu-4F-Q2wkYlz9mYSrBiR6zJb_OZNmfW0lfQ3GrW-wDuthghxwoa4kduDGs6mdUUfT0rYTzfHFNTGhXRiDXudxKKOJJQlCq-Yfm9m9NO-ZZal9nvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از طرفدارای حکومت تو تجمعات: ما تقریبا یک ماهه تو خونه دیگه غذا درست نمیکنیم و طوری شده فقط میایم اینجا میخوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65358" target="_blank">📅 10:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65357">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌐
آفر ویژه سرویس های VIP
✔️
🙂
Standard PLAN :
🔸
10 GB
➡️
90 T$
🔸
20 GB
➡️
160 T$
🔸
30 GB
➡️
240 T$
🔸
40 GB
➡️
310 T$
🔸
50 GB
➡️
390 T$
حجم های بالاتر از 70GB  گیگی 6,500 هزار تومن
💵
نامحدود PLAN :
🔸
ایرانسل و رایتل
➡️
450 T
🔸
همه اوپراتورها
➡️
730 T
⭐️
تضمین کیفیت تا آخرین روز
🖥
⭐️
تضمین اتصال پایدار
💯
⭐️
تضمین قیمت منصفانه
💵
⭐️
پشتیبانی سریع و واقعی ۲۴ ساعته
🔜
⭐️
مخصوص نت بین المللی
🔒
🔖
قیمت همکاری همین آفره
💎
🔴
@MAMADXVM
CH :
@proo_V2rayng
CH اعتماد :
@prooo_V2rayng</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65357" target="_blank">📅 00:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65356">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65356" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65355">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXp9G0EKJC-BLnbTuy8vJzRKToFs4Ls_FtYkvQfk9gA32tdNxCRpkEjNfvNL7b1lt7kK8Ndl_L27u_MUGvJMMOMP2kIk7zvmCovc7A5OWx_L5Jb89C-8fkTeKwyi8YzLqI0tswZijLt5BDWbFzytBxj06pUd9FENYcTImM92b7mHlmbhuCJAWDKV3UZrOHYny9BdqO5Xw0YYGgUwCb3OxELnNehQSZbB5JV6WQOYEik9LmrC56cJkYOLH1WflSJywRuf_YC3YUkyjRCKIMHUXlcs2lod8B2WSBG85m8KYttI9RRwWvBSVMkxrZe2JqX1b76XLsPggfgH5TgSdkFfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65355" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65353">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=dTGOGaMhQtFlsKJYwh0nTTkSwosGsFYNhOQqPZMGqPdjyQ1NYdPgSnTKXtdBpPWpjBW9A8Al2bQPo9JBqRRIjJgfkUe8wEiGk9fanla4lSeM0sa2Gpl-VPlf4fX0_Cwg_7GSOr4HfFY7zTJe09Ts_ewKcJTFXM5C5R4UQir5Es_Ld5ONWF7vVelC49HC_K0MgdSRt0fhxMpg_82rdv5Ajp-iL1yoB1151ptCVpbTbmesIe6RG-uahbaxdwgOCOg8Fd9Vd8JzSD2mJEFwHcvmDskl8x8mkRArM1s4BwOQ8blWqSvJ3qzKIiDJuLNE2Cq-Bq8TLPANROJtNpTmjF7ZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=dTGOGaMhQtFlsKJYwh0nTTkSwosGsFYNhOQqPZMGqPdjyQ1NYdPgSnTKXtdBpPWpjBW9A8Al2bQPo9JBqRRIjJgfkUe8wEiGk9fanla4lSeM0sa2Gpl-VPlf4fX0_Cwg_7GSOr4HfFY7zTJe09Ts_ewKcJTFXM5C5R4UQir5Es_Ld5ONWF7vVelC49HC_K0MgdSRt0fhxMpg_82rdv5Ajp-iL1yoB1151ptCVpbTbmesIe6RG-uahbaxdwgOCOg8Fd9Vd8JzSD2mJEFwHcvmDskl8x8mkRArM1s4BwOQ8blWqSvJ3qzKIiDJuLNE2Cq-Bq8TLPANROJtNpTmjF7ZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیکزاد، نایب رییس مجلس: تنگه هرمز طبق قانون مجلس به حالت قبل برنخواهد گشت، تنگه هرمز برای ما از بمب اتم مهم‌تر است
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65353" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65352">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
صدای انفجار در جزیره خارگ
تسنیم: خنثی سازی مهمات عمل نکرده دوران جنگه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65352" target="_blank">📅 21:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65351">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ1UMfH36ralkUN9ZvfXhQn1zvY0fCl_xpgPJS6O9m2aVpL8JTyTtDzFHVtgsZX61D4KIzAP4k-u2wmMsT4w3Lh7zGzDQQHp8tQAemgU5ylpaMavYT8pzlhNhUzDI_iS3Z1-pPfamHYrdrpLB5zt8ynJW6SVBzXEnoQJ17fCFKSmTUiplupj602fgYQTMuM4gs_PrFP8BumLsDBG36sl8bDNiZiB7rzYBsxEyatWPDJ2mlwgeSeo2L5bVLnzn8mLKouB465y4cIR6CRMQNUuet20Wv3ZTiFD1GkiyDHx7QpR1np5PeuJM0qMW21LX68_1mRYN9_Rr9pc8HpejNC7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تو تروث‌سوشال: کتابخانه باراک حسین اوباما، در ۱۰ سال، وقتی کاملا به بلوغ رسید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65351" target="_blank">📅 21:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65350">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457010896e.mp4?token=dkQxWNBkiRuI3z5YQFA72TJwvK3xMc3FURpoNrsME7zs5AvzX3nFipwcE3IjvFQkyuH-23OcfNV4uq_UJwtt6hacEln1enI9EXRctXlJzFJRz2UGgbZKnRAbCAGSy9eRBQJJNH-6IvJrE2cRGT4Euc-XcMyXWdZmUR3Lt5n6vj2q3W9H6c60KdjqzanBiXT8ItayO81aAd8GiIALe5SGoGn6YnU0Fe7iUfzKryslMWqDWU9SHL_mhL3MMzm-LxgbXm_0TzykGjBAbu4FqDEnTFo-Qy4V5j19rHgIW7dRbV2lPUYKy4k3TUqmGMAIMQ9lu6mH6M5nwhIthpIHRwA8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457010896e.mp4?token=dkQxWNBkiRuI3z5YQFA72TJwvK3xMc3FURpoNrsME7zs5AvzX3nFipwcE3IjvFQkyuH-23OcfNV4uq_UJwtt6hacEln1enI9EXRctXlJzFJRz2UGgbZKnRAbCAGSy9eRBQJJNH-6IvJrE2cRGT4Euc-XcMyXWdZmUR3Lt5n6vj2q3W9H6c60KdjqzanBiXT8ItayO81aAd8GiIALe5SGoGn6YnU0Fe7iUfzKryslMWqDWU9SHL_mhL3MMzm-LxgbXm_0TzykGjBAbu4FqDEnTFo-Qy4V5j19rHgIW7dRbV2lPUYKy4k3TUqmGMAIMQ9lu6mH6M5nwhIthpIHRwA8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با وجود مثلا وجود اتش‌بس ارتش اسرائیل اعلام کرد که در طول آخر هفته به حدود ۱۵۰ موقعیت زیرساختی حزب‌الله تو جنوب لبنان حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65350" target="_blank">📅 21:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65349">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65349" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65348">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fq74Skiwj8lpulBHL_xdJUvNO7jVCh0PPwjxZWjRsfk9wFE4d5Gl05qPZWGW1yK7JikQ3mm3xTX7QYmGV0wowfZOP42Ebu_FNFvlFo3nrlU5AqLrTukacEPAeNiUXhMO_vEFRmI4l2ux3VzP67Kku4Qr_FtjClOKKPVd4GVnB_xByiFfy0TPdPp6X8bYDt8mxRQCOatnQkBJDPN2G35sG4EwD1v5APXk21zrMlJBv9W7hurVkk7bFpFckRIc_ZquTXizewEYvJSD3jG6Vnf4aUBLUyGDj2omnaeikY_LagiCzykWWhC2ON0RppzgM9dZAGCuEiv2zYKExVgGPCj-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65348" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65347">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=LAH8c5X5bONtHda_MnZbU4dFfNVkjHCCXtIh5Tvk97kD2rNX1U73vpfTOi8XKncodSmCh9oJeGaSIYxppbylgiGWkP8S3eGQiOnk5emqQYM_RawHQ1EUIy5HDN3AycKy2VHPChvQCwYjO88cJp_BLScleud0TtT7v1tCGn0-mwZs4HvJWt5H9ZQcpRwXXkFw5sWehWiWV8752q7gZntplPhMjbjsbrxs4caRvEf69EVdjLfy2G_DOWyqCRdb-EFQOPVtXyqtlWkEnvZqtiPktWUDf5BbEfzHdDtah8XezOVT9vZqs7f8O-S1RdD-IdABtslwn8X0bzKUTvnk3RcAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=LAH8c5X5bONtHda_MnZbU4dFfNVkjHCCXtIh5Tvk97kD2rNX1U73vpfTOi8XKncodSmCh9oJeGaSIYxppbylgiGWkP8S3eGQiOnk5emqQYM_RawHQ1EUIy5HDN3AycKy2VHPChvQCwYjO88cJp_BLScleud0TtT7v1tCGn0-mwZs4HvJWt5H9ZQcpRwXXkFw5sWehWiWV8752q7gZntplPhMjbjsbrxs4caRvEf69EVdjLfy2G_DOWyqCRdb-EFQOPVtXyqtlWkEnvZqtiPktWUDf5BbEfzHdDtah8XezOVT9vZqs7f8O-S1RdD-IdABtslwn8X0bzKUTvnk3RcAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پخش دیشب برنامه «خیابون انقلاب» بخاطر این حرفا لغو شد.
ما اسرائیل رو تهدید کردیم اگه کوچیک ترین خطایی کنه میزنیمش، الان لبنان رو با خاک یکسان کرده و ما هیچ کاری نمی کنیم.
ما همش الکی تهدید میکنیم اگه فلان کارو کنن مام فلان کارو میکنیم، خب چیشد پس؟ یه بار به دشمن نشون بدین که ترسو نیستین.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65347" target="_blank">📅 19:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65346">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajeqP4vCw0aNHWvZ6DhpXoVBbIo2c3XmsbA_WTmjU3-UFppNbuoC4miLYEe53GiB91r9OewSX0rSYJD2wY6h8pDV_ZRnCkcJYjtojCVSy8bDjjtvfJEVcrTQHhevb77v5NBSPDaRMjczIw5lVJwW2x6eu_f_zXBswbxF_kunDyqDqOrHDW0cpXpuqSBHB3Z9gzW9niu_zfF6UsOqUDnjpLd_CRZZCaA2DcXDyf-Qzb3IB-TvAPwoBA_bc29FP2F9DkWYJuEHrMkIWCsnp5UAfRdeBFLmxir3QpiZFJBKYMF122nIpXiYUo8V80H6l1jzOqeJ-dzsY3Nv2yYqkO6UuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام وزارت آموزش و پرورش رسما امتحانات نهایی پایه‌های یازدهم و دوازدهم، به صورت نهایی و حضوری از تاریخ ۱۳ تیر برگزار خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65346" target="_blank">📅 17:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65345">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=niS-Dg2gLhk6pbg1J6adWkg4U936N57oSsUKTo_TZtrkWA3Uts0qOo59H85W3yhqkVzL-SSMVWJsUZal2CKeaHfgAG59mH_rVWK-90Up_tXadPfSY3SrWiZwVCXLqNS9hK-wm5-nNw-8MSGRB2cx3tU8HtDQBAmOb3FyujexUoX4IVXpZ4YLEiB9mpH7Or6MQoEbbbkFPEzZZNqysdmqjlEPrQKNPjPq6Ag8UTEv3M4TnV7kmPVWDgG91Z4idMrCr2qyyB7DCea5tZeTz8KQLfw_jH0n5AOdZzprMFmmBARNCrIwhv4xyL7O3AyKfN_SQOZ06ko6wAu1crXHPCOtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=niS-Dg2gLhk6pbg1J6adWkg4U936N57oSsUKTo_TZtrkWA3Uts0qOo59H85W3yhqkVzL-SSMVWJsUZal2CKeaHfgAG59mH_rVWK-90Up_tXadPfSY3SrWiZwVCXLqNS9hK-wm5-nNw-8MSGRB2cx3tU8HtDQBAmOb3FyujexUoX4IVXpZ4YLEiB9mpH7Or6MQoEbbbkFPEzZZNqysdmqjlEPrQKNPjPq6Ag8UTEv3M4TnV7kmPVWDgG91Z4idMrCr2qyyB7DCea5tZeTz8KQLfw_jH0n5AOdZzprMFmmBARNCrIwhv4xyL7O3AyKfN_SQOZ06ko6wAu1crXHPCOtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط یه آتش‌فشان تو هاوایی امریکا به شکلی آخرالزمانی فوران کرد
الانه که تسلیم تیتر بزنه کائنات انتقام مارو از امریکا گرفت
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65345" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65344">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxT-8KtoXiBrrAS0xxSS5-SJILyYGItI4TKYmxVfSfYfm-HdDXSItxylTp32oIUtvHu53We9rp-2kyvR15glss0H2QEhpQ5lCCX7LSUEMu2AsEmUWQK6Va-8_8IYCvmxFwQhFJRK1a4mcuTSo_1kr0vDJNGigzEA-QssVcgXxHdVetGRztns-N6-q0qX2H7-MLyU1cPbytmJLYwPwYgoDOXcPeJaanFG7ShasvytnIdClr72Fne9DgYuU7BYZ9BcP07G_ICxEar-VkWEyxd0yYPxMCwv0KibsKKK6ySwFlX_xRGBuCENyhS2kiy_Dt4TFD2kjs9VAejkCwf2G2NIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمهوری اسلامی پاکستان به دلیل فراخوان اعتراضات مردمی اینترنت منطقه کشمیر رو قطع کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65344" target="_blank">📅 15:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65343">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=Ns8juhD5eO3NWFQRo89lJ_zL1twKlS1Q6XbMuP3d-F3Bv8nmk--8VbyQlwPmgFpEs-27mK1HQAJW3gSsRQRfldZ0zr5wXfxXzY9swIWZr95-N9-NECjEJlV5rAR7fADsB-CcjM52SLVEviMEJGe8i7815Fls3lnRItqgRo2daHuGAXWdcqe5QH6IIJ4Ktp1thr6FIRxrUcyeRN8W41f6a7IUEclsQ0aIIA_ycS1wbAyMtQa2PfobI1zrFxiMbXoLKB-ljzVRBQayzUnjTB6m2E-eDmiYo-CwOP976uhFJxlxqN2xNCm8XMy9TyJ0vxOuUbUbgt9CcnYgsk6Qk9CogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=Ns8juhD5eO3NWFQRo89lJ_zL1twKlS1Q6XbMuP3d-F3Bv8nmk--8VbyQlwPmgFpEs-27mK1HQAJW3gSsRQRfldZ0zr5wXfxXzY9swIWZr95-N9-NECjEJlV5rAR7fADsB-CcjM52SLVEviMEJGe8i7815Fls3lnRItqgRo2daHuGAXWdcqe5QH6IIJ4Ktp1thr6FIRxrUcyeRN8W41f6a7IUEclsQ0aIIA_ycS1wbAyMtQa2PfobI1zrFxiMbXoLKB-ljzVRBQayzUnjTB6m2E-eDmiYo-CwOP976uhFJxlxqN2xNCm8XMy9TyJ0vxOuUbUbgt9CcnYgsk6Qk9CogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65343" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65339">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nswO1eX9wDHrzVyLmD-9FfOFZ4Idj8w6Pbw4X28EK7vccTxSAteqXlvb0i_7XAAQfEIPkblYO8Y6jM8RrRSMkNgH1qsS4fADZlRfrcnw8sG0RFbbDSfAK68xU3VSADwK3-YSX7giXcTLu5rygha4xessEZrLdO6HTjA2eSMcJQ-lq4h9QpAmbBZvH-CNOlKTDlbm8YYR-L7_xd7laKSxIk-HLisQFTSNVQORKUVgMlZ5oMhu7ki7leIOPJLuAz9pAY20frsyyq7c9JpNT1uK_EWJcFR0eSE5ikNHXJYxAfYIjDFGMI7b6E36XTuxkhV83T007sljuUTgfhNyULp7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YooIbm3BYdtSEfZ83smw3zm-BOZ9QFYx4Amracq0sM8j33LaXM4uSF2FJVUISUrUeW3thJdCufkneQid3i2JVDuFnsutSY5P71uIk0VraEx0d2PYZrI_C7ePSgpmbJEqwmTDmAUbl7gfGWDa9gUoO_mPU0orXvLxBdY2cIvGHl1tj6HSlgm2pxG5Kes33iWXa9xFhfT5ZpijyM3qCkEEGF8z8RtyeCpUQy9Wa13OYzJccT8z_5uwArN8_Eb7FxABA4qmlmOan0Ci1df78YCgDOyG9wVGLqvrPpOAPD6W6AXeZjMMUGwzWxNipchjOuLTPFl7hXm-GsPa5h-rvaR5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqtqjNFYHdCsKy8tGuU5rHXe_SOjHT3WXOqSGMLlkZktDRwPW-LDu3TQ3HbDz0LUmr7opTFFtbXGasMK4jxt3nDpKIFcwvLGcGhuDmq-CbCQrOuIctXmNG_8LzG9A8FtiedQ9blV_QOdLAZPHbYU47zB-c8FcgE7fpcCPyEi45FCzMWMFMMlapzr9Me-UIZhv1PpmDOtBMZ1EJLoO4LPe6SJXX4-SfuEA6WXuGI61cTsSZRHx8WXZ-f46rJZ3J4Aw7H2Enf_VZrYc_ia1zFsyxvYYjXIoxJPS6T7XQnWdMKcgNVU4mFHtqGoScxu34I5bopjXdTuwvu6MGLm7R2Chg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aa546373.mp4?token=v-GQiFnUQcfE14iuHMgKK_wpmkdqEC-GPFGiO3IUYKM1tDG4_k4C7UMpF8QsFOA_vYEyERYt-pQHa8kRGSD_DSLqsoJsg-O94r6CY11UUfEOBCx5TUJ4w6lW7QcwPf-2ZoDFBwpjhWvVvtg7rJFzIpPhOljbUkOQG3yfPf2yLDv9mq-C_8WKjrVdrDTCSA3xtyBBx-6_btOQqMfjARUIbwuvhLv0yQ3OSIZyWW1OPMIACj3SewmFOiTAdAtarDoPaAP1cSGh8g_tdbfjPykqEUi3rdkJceQ_sCu0W-_Nq3ba4hU3Quk9t-jBkrpG8eBXpEK-u4kiP0JSeYFQoY6iLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aa546373.mp4?token=v-GQiFnUQcfE14iuHMgKK_wpmkdqEC-GPFGiO3IUYKM1tDG4_k4C7UMpF8QsFOA_vYEyERYt-pQHa8kRGSD_DSLqsoJsg-O94r6CY11UUfEOBCx5TUJ4w6lW7QcwPf-2ZoDFBwpjhWvVvtg7rJFzIpPhOljbUkOQG3yfPf2yLDv9mq-C_8WKjrVdrDTCSA3xtyBBx-6_btOQqMfjARUIbwuvhLv0yQ3OSIZyWW1OPMIACj3SewmFOiTAdAtarDoPaAP1cSGh8g_tdbfjPykqEUi3rdkJceQ_sCu0W-_Nq3ba4hU3Quk9t-jBkrpG8eBXpEK-u4kiP0JSeYFQoY6iLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بعد از درگیری های دیشب سپاه با چندین پهپاد و موشک به بحرین و کویت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65339" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65338">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65338" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65338" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65337">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpLF-BCPTsZ6Hv031v98edu4eCFAUq5qNHAO2nU4bERy2kyp9WZTnO4uiaRaVkZIrx7TZKGxBSiwhRWWXnF64WqGC8x3t4DpW1rC3f04o4h5E6V98Fcx9IxYwPb_BR2cpr1R00ln7SaIj-Du_IzPiyg2XYnUcRYsrGJ0llTFO-us0a3tnfNHgyVCZKs9HYWt8pUtb1uHHuYeKAzNB4R4qHEOR1tcxXEaf4p_LCNr6G9BiZnb9cFnzpyYOcZrgf6QItTm-MNxdlk6rOZxZMQ6YpU4drEYYpWLvKZgPzje7-QgVn-TeWVmVa72Kv8m1JIJU-tTUgnpAC7DhN0WGoL2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥊
پیش بینی بدون ریسک بر مبارزه
Muhammad
🥊
Bonfim
🥊
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65337" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65336">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L4Yi8CJqad9BIa7r3bmt2kGSp8IB-Ll_no2Ex-IKIlF8hL082n2KbiGI0T5jfiNjv3wJuPU5W6LHunTCYTJdCHJ_IjMTdkn03_StIP-IeQA3zS_DBhX34AI-VHitHst1EO8-uhj3BMXbLT6VTKYhOoVmnz-N6rIidQ_JGvwDJZrwxpopj8Oc5HyiMHWsYSQy5ocp2OKp0BB2qPhjxfvouU0iRIEP5T4jyaJvuNrR3CiGzTALdjYnMaDpaH4M1BAqtdGVi50drPkU3PwxjIchWYVLUCqh76fd1CLmMMS8nVcfJkkSACklwT1W5caxbQYzSQrsIrf3tVS10shFhzO-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
بیانیه فرماندهی مرکزی ایالات متحده(سنتکام) درباره اتفاقات و درگیری‌های دیشب:
چند لحظه پیش، نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند. پهپادهای حمله‌ای تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای ایالات متحده پس از آن برای دفاع در برابر حملات بیشتر، سایت‌های راداری نظارتی ساحلی ایران در خارک و در جزیره قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در دفاع از خود آماده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65336" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65335">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLCEleOToGKV_BDQHbfwa22pudP1LxBRstlZtUwIVmUvXpd1Tu9lwDC9RS19kTSKqk0NrZK09DP4i9QiIMd_8m1tXGZ2C9FwOF8eizX9Wn2BBaBjL-jfEVohhnijAMpF7zb8V46bGWxGuGMsQc3SSu-wtaevIn5He9T80VlMO-gUL8crqEgnpWAI5xHBazlArdypfCet9sDBe9Cj_wfZ8OVkS-TqPbhhj6lbENvqEpgzd87w2gAxuvs2614b5hvfuYHmTk8arlyIa3-RBKzhfUnb3pq0WeqNCDTq2645MO_8pYsCoq_2KiU9wm9iUk6LSChz5zYat47EFVcFWkRM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم خمینی در سال ۱۴۰۴ Vs مراسم خمینی در سال ۱۴۰۵
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65335" target="_blank">📅 10:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65334">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=mq_9pwGwbO92I2DotbxBrnBj8ItjeEjgvx72MvlEfIQVr8GpckWGg692kO04oVucb9GaG0Bi7JQBpP_ZwJgndGzgQiWCbC5OwZhzE88TTd-HDrHEglUr25QSvNcZcJF-AUjwWyousUPdN40YA95KmgWBkwsc5ZA6SXq4FgFKT0IKoLfv4y_moRigKd1Pd4V7LwZHb0FuLgngGzX1eCmKoTmAegNhIFyRQKeObGCB1tA595evb33BUrE2-EHuTDmUiglyxverv_G5o3LxcaPj8m1vbF7epHP-FdOgwv5134g0V8KhiyI3I39ACFF0hAhucOOR39aHazLeRCT-Kzh_VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=mq_9pwGwbO92I2DotbxBrnBj8ItjeEjgvx72MvlEfIQVr8GpckWGg692kO04oVucb9GaG0Bi7JQBpP_ZwJgndGzgQiWCbC5OwZhzE88TTd-HDrHEglUr25QSvNcZcJF-AUjwWyousUPdN40YA95KmgWBkwsc5ZA6SXq4FgFKT0IKoLfv4y_moRigKd1Pd4V7LwZHb0FuLgngGzX1eCmKoTmAegNhIFyRQKeObGCB1tA595evb33BUrE2-EHuTDmUiglyxverv_G5o3LxcaPj8m1vbF7epHP-FdOgwv5134g0V8KhiyI3I39ACFF0hAhucOOR39aHazLeRCT-Kzh_VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: ایران با آمریکا به توافق نرسیده است چون رهبرانش «قوی» و «مغرور» هستند اما «آنها چاره‌ای ندارند.»
کمی زمان می‌برد. شما درباره ۴۷ سال فرار از هر کاری که می‌خواستند صحبت می‌کنید.
یعنی، این باید مدت‌ها پیش انجام می‌شد. این باید توسط رؤسای جمهور دیگر یا کشورهای دیگر انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65334" target="_blank">📅 09:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=Dbw7iHrqsd8RBJpET48xfIyfaZl8Y9b1jW8oKeyFTbgdohltmFKeIgW7JPmLp5FQaJyt7gFqw5FABk3WgEM_zODTtjC_dX6Zeatogt9FGcWSw3rD9SzpLSF6u2v-xYSSQa8TJq6qcOWXWQEjOYyWbSLrfFLsz3N2TJ49vJg3nbAtSokKS-YaYjxuWnCysp13LVq2et0a0pQ0Nn0WKe-SLSVBUhHixJo9iNBTQuwnLVyzN6avseppuBQXQ83EwzHmqvOtCzg6EoJOD24ncoq9L_NoIFQs5kdquRfUqo9mdBbtxL5XMiKrI4odN273l-7-qmNr0pMspC6YN16_74AEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=Dbw7iHrqsd8RBJpET48xfIyfaZl8Y9b1jW8oKeyFTbgdohltmFKeIgW7JPmLp5FQaJyt7gFqw5FABk3WgEM_zODTtjC_dX6Zeatogt9FGcWSw3rD9SzpLSF6u2v-xYSSQa8TJq6qcOWXWQEjOYyWbSLrfFLsz3N2TJ49vJg3nbAtSokKS-YaYjxuWnCysp13LVq2et0a0pQ0Nn0WKe-SLSVBUhHixJo9iNBTQuwnLVyzN6avseppuBQXQ83EwzHmqvOtCzg6EoJOD24ncoq9L_NoIFQs5kdquRfUqo9mdBbtxL5XMiKrI4odN273l-7-qmNr0pMspC6YN16_74AEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e15
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgiPGw21D98Lzu5hco4JT5iX6nv4e4HRcGAT4Xc8zTLYBFsH1sVeH0vGZLE3AHnYuNsiPz0r4lBwPJJAgiTksdYSAmBIz5R4HwLeSu7dqegY4hb5jgizLxSjS6i0XEKHHW8UzMz0cHkGBsMEmGCRAwFrGky7qJZGs61KeLeAzggo6HsgPwxva-KIf5OdEZgv1x5Vjhnymtu0RN8y9k-dZ3zi-Q3exXKzfvXor59vnakPHyhlssy1Tt2E2Fi8yDoKmHDsYjIjyiPXP36Obe7cMSV-06qskSCq9xI_eILesX-Rref_ftEbUGgcx0voP-2_hUGLkQ0-jhwrs2d-funtAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65331" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65330">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=Zb7PZx03Wll7BqbZTqDs2Jn3sS4JdqKqoXwqV-pjw58qzs6lUB4RS3LGmdUPsNEosiAaQ41sCfTBiYoR3gxfXbAX9qL-eh8TobgiG2oO2Mps6G1X1jb-MxpeoO28AvVsWWjoPVV0m-3LNoha42e7EVcFgEXonh0cyqpyd3cmUH2mqEffESDkpswBXUd7xKSw1ZF8I4oMFZD0abMq6nUEbjQSXji9LmXHHL7-tI4yklcwcZSMqffz-hFT2RpA93ZZ7pnhLaah1C4ZVSk2Z7bbCfZ_zPsTMCuOauyzlVmFv_oIYlw8OqWTJFlKKKaOlaOuwr3e4VgU3gj8nKqAxAQ4Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=Zb7PZx03Wll7BqbZTqDs2Jn3sS4JdqKqoXwqV-pjw58qzs6lUB4RS3LGmdUPsNEosiAaQ41sCfTBiYoR3gxfXbAX9qL-eh8TobgiG2oO2Mps6G1X1jb-MxpeoO28AvVsWWjoPVV0m-3LNoha42e7EVcFgEXonh0cyqpyd3cmUH2mqEffESDkpswBXUd7xKSw1ZF8I4oMFZD0abMq6nUEbjQSXji9LmXHHL7-tI4yklcwcZSMqffz-hFT2RpA93ZZ7pnhLaah1C4ZVSk2Z7bbCfZ_zPsTMCuOauyzlVmFv_oIYlw8OqWTJFlKKKaOlaOuwr3e4VgU3gj8nKqAxAQ4Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:
ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد.
ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=GoKK5zir4f8_h3jJxax6gHALFaQSUmcnJcgGyRFn7AEgeEzJ3sT3UINdsfSBhkmLFp7R8jKl3Dm_lG_dv_UMecEcQBVa6K9RC-_pPXgNAi-0_9JgSr6YLQIInVcBZo65TLkMxpqxHbsjEUFwjy7IlpRigrDmasDN6aSLC2H6eJIT_-IyiyrX2UmUG0jmdkOEPKFtj26G_OaEwTEoXAmB03MoFYDSGZ9m5OBe7A7uCeiuC9wM3XghcEY7aUjdgaMXwp_dsby5iC3hetAHKiZPViUHFblq_z-VGHdBOreAbx9MizEPjNTcea3LATvtpZSr-Lhdh6fU8m5r91W6rGcE6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=GoKK5zir4f8_h3jJxax6gHALFaQSUmcnJcgGyRFn7AEgeEzJ3sT3UINdsfSBhkmLFp7R8jKl3Dm_lG_dv_UMecEcQBVa6K9RC-_pPXgNAi-0_9JgSr6YLQIInVcBZo65TLkMxpqxHbsjEUFwjy7IlpRigrDmasDN6aSLC2H6eJIT_-IyiyrX2UmUG0jmdkOEPKFtj26G_OaEwTEoXAmB03MoFYDSGZ9m5OBe7A7uCeiuC9wM3XghcEY7aUjdgaMXwp_dsby5iC3hetAHKiZPViUHFblq_z-VGHdBOreAbx9MizEPjNTcea3LATvtpZSr-Lhdh6fU8m5r91W6rGcE6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
مقدار زیادی نفت وارد کشور ما می‌شود و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند. و به همین دلیل است که قیمت هر بشکه نفت ۹۷ دلار است نه ۳۰۰ دلار.
وقتی کل این موضوع (ایران) حل شود، نباید زمان زیادی ببرد — به هر حال، این کار انجام خواهد شد.
وقتی همه چیز حل شود، قیمت نفت ممکن است حتی از قبل هم پایین‌تر بیاید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v61d4WX91HsA8qanu2vvBbDpY-cmM-6-mPSLA1jkoYgkBzDN6ETt-Le8eobyXkQSY6Q52BwYRvIT0PEtT_u98kAynDEqO0wujg8nklDKNCYkwTZC5Dtfga1G30jqvfVVS9oTj7XXS6ThcAan4fLXgS6Ytlw_jT4YLjbAAalPaN-K1Q_aMC3BtKFpio7yMlXZUqQVqnIU5bmjIeIJyJ-YtOCGftLvvu8zO1zz5UfDfHLX9aqkTBdMV1dGLquJWDcHOkoZBiEpMBEHlmattmrkoQ8GercR5fTVXUWEGUROtahujuFhUb81TkZ4WGJbwJmOTAI5ziH13CVE6G6HM5aUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
صحبت‌های جوزف عون، رئیس جمهور لبنان بر علیه نعیم قاسم، حزب‌الله، ایران، اسرائیل و امریکا:
به نعیم قاسم(دبیرکل حزب‌الله) می‌گویم مردم لبنان، مردم شما نیستند. شما نماینده مردم لبنان نیستید. مردم لبنان از جنگ بین اسرائیل و حزب الله به ستوه آمده‌اند. دشمنی بین اسرائیل و لبنان باید یک بار برای همیشه پایان یابد!
ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
حزب‌ الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
خطاب به اسرائیل، از جنگ از سال ۱۹۴۸ خسته نشده‌اید؟ واقعاً می‌ خواهید در صلح زندگی کنید؟ بیایید بنشینیم و صحبت کنیم
ما آماده‌ایم. ما مایل هستیم. ما متعهدیم. آیا شما هستید؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvuTHHLsro0U8qZ0CD62NNnxE3JqgTNvx87D6pmuBPKXj4lLZBxj9xitKFtDQHgeAGJ2FxU4n41Jt9J77pUY9Gb8hA7CsKKyS7QYKx0k6mho5bgKhY9u-QaZONwUIEibJhcAEcyZS9Ij2bProcTP_szcpX8fIluztTwXMxcSkUvgCbZwU9mQNiE5Q33R7v29X6QPmAzLY7Slu5vi-L8eMb_Zci5llmpNhGmuUfNNOoojjY1TlIUZxgBl5zyN1I2Kd-vllyWq9Z-x-2XnwFw7up7T6YUgo9vUbYIo_-T3IX4RVVHJpXhI73HRQgzBgVfje5Ndsb_17-hKZo2L8QOt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=TyMeINhcXqUmBX17O-DIquSr7IDuBdPLlFfRYggp-h8kzbNHrR7whUS09FLh1Y-GPQcxk4BgmutouyHA9JaF-kXj5HeirnIIgTAAu2fHAR4pzh-A7Md8a7JrAW28FuQi_BIDUPuso0Gv3pc9182rpbYrffSpngqfWxLfk8zWwwv3A5qFgU6PXk9QpgFtK4CAS1RbJhMwIzzTbNlMWlg5StgOHVEf8PtDYZXWz2goNYdFlQbOvPvoDPv03a9AP4ZGxkXyVBzI_RTh7GF7tqCMkSB8i8MgFB78xILdKjzTTDXgBNHh2YNMXiqSMu5PmZ1g0_JSZWeclo8OzdhfFDFsuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=TyMeINhcXqUmBX17O-DIquSr7IDuBdPLlFfRYggp-h8kzbNHrR7whUS09FLh1Y-GPQcxk4BgmutouyHA9JaF-kXj5HeirnIIgTAAu2fHAR4pzh-A7Md8a7JrAW28FuQi_BIDUPuso0Gv3pc9182rpbYrffSpngqfWxLfk8zWwwv3A5qFgU6PXk9QpgFtK4CAS1RbJhMwIzzTbNlMWlg5StgOHVEf8PtDYZXWz2goNYdFlQbOvPvoDPv03a9AP4ZGxkXyVBzI_RTh7GF7tqCMkSB8i8MgFB78xILdKjzTTDXgBNHh2YNMXiqSMu5PmZ1g0_JSZWeclo8OzdhfFDFsuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=NnEb_RZe5obYoEbCtcabVqzDCSGR3PUwCWUJO-P9WWXZpT43teR8IEINR_6B0I0p86Sbpkq8hZKtD3aB5G477rK6F2ayiLix-9cbKrCWks1d-bbC1j_cqi-quFz_Fxcmq8IJ4qWEHmqZxSh2WOLqaFav7uAtAWWOUErjs60xxZ20PlX5Yp-qInZ70ci4yfmOIX3ndJtCPgjUo1JZbnDRieZt-8NDf0KqWpLRhJrSPtIjWwlQibn_GDvGqhg5W2BMpHyXfD47XV88DyrEqwVDQPpUFLM1SMhCovsaNY0xBjnNw5gxwALDo9Hnm0pezXl6B0DsKftGmBDJjTjyRqBecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=NnEb_RZe5obYoEbCtcabVqzDCSGR3PUwCWUJO-P9WWXZpT43teR8IEINR_6B0I0p86Sbpkq8hZKtD3aB5G477rK6F2ayiLix-9cbKrCWks1d-bbC1j_cqi-quFz_Fxcmq8IJ4qWEHmqZxSh2WOLqaFav7uAtAWWOUErjs60xxZ20PlX5Yp-qInZ70ci4yfmOIX3ndJtCPgjUo1JZbnDRieZt-8NDf0KqWpLRhJrSPtIjWwlQibn_GDvGqhg5W2BMpHyXfD47XV88DyrEqwVDQPpUFLM1SMhCovsaNY0xBjnNw5gxwALDo9Hnm0pezXl6B0DsKftGmBDJjTjyRqBecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/msd3NXBf2dST-XaWbxWvWic_6bUHeaOL5xvM5I4dSWBfNIxOuXnDuK3zvrBs5TZwC-0auma4H9XAiziJaq9Vjkq4YmZZ-9Qy3mvSuemPbSaQZLgMK6V44mY5XlGy01alBgRAbkw5zZ2hlo2EBhHPM4WeJTgveVfuMFRbHSY2NBr0dgEtNZd-UeNDPI2C7HdZpcm-oPnm2bZjxM0ECk20TYaAlrw3Ld08JWKMj5gP0SgolJkXNO5ft4U_UbXVIRMpV1P47ROqsGksMNQV6lkvXc3KTldjppHAGCTmG9WkSGslAcrEkZfRGxiSZf__6Fa7N04cTPQrGh3nUTjIuVGamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/leJlcr8J2Wbp_2A3b0Dv6rv8FKe4w0HKj3X4VcFtJaOi0IPGWnFAQjFxmCDyDvsAcYj4T3APZ9jkHplTE8PL1i5Fo_NubdNxh2bjT2CZlBEUwhqcxyDyoz9JTDZUh3mqPhF9dyuqFMb5fciJwuke2YVsLiZ2u6JbnoHS1g8yvHXdKLaGWIc5DlTLH1LXC3GMB61udD18cMM2kL8LJLeckG_jaCGSasGAR2APqZ0af6qBs0xaH3Abwd8DinVjBOCLCm6j8_ap7JGabqKDxG453zeZC97sI3tDN5Ivaz_TlK6qkwYl8IdR8A4ubllTLkYfFB-PdqIFx5ByxY12_hDiUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eG_yVcOf6YLEl-BXRzUhpzixVKALZDELTmkYSGvjAARoFBt_93-ngKZmLDms6MYPtCec2J5LizBD0oWgtT9fP41XLfMLyrviw1DNIpA3QqLXhF7nrjxmuKn07gDK1QT15tW6KEFDoQLor8C5j6Q3k9PlhDinc9N4tEk8y54nA_IEK7DcoGAiOzIHfWWbnE5zmdB8px-N_Kc2_MabhfZJ2szabTSeRp7KAbkxWLt-dw1tqIUu2UDtdB6nze2OgfCgQzjKUAqhPeciVRs2KwzECOE9m5voKcppa5_tls7bE1Xlp9zIsSPJUi7jAKj_Yw1xXT5A5pdTXCwAHIdt8A3VAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds3eADNvduyQZpsWII_srcbGppsnETX4tsIlKpTjrl_oLeHqSMRWGWU0L9hWHhLuFh89sHQM5oSPcAOOcXi1KM-f-LTzsZZj2xDYiKk1QWKyZIbjYYWhXcHNY5HArfh8GW-HL0HHzo2pULW7fT4ucgeKb0DHMMOJodK-L8nb3UNSexiZiKysRTcG0LR4OtqgwXWzba3h7Ph8l9Bb2J9K2dfQHxQv9Re00REhRLIj6dOPHHicVsKtZ67sR6mV_lsu-mwtJLg1HAbomQOeIZN0ut8wq_VA4vg5WoHUPUcLo4Ii7ej3GPm99BelAB_zhKx7MP2j4Y3AbPDU9y98ZAfnuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=n9aPBXgP5lozu5-iSyFPJLRk3P3kB8Ie_1N4Eqkw614MGq41KUm3tmMFP7g7V3AA1ZwwuXW2Ge22G6SjpE-z07wORhzDTsTow4-wHd-03TIdTTmAyd4Eo2uexk8YMMtkZixwL7CGf9X4fk804EjPM3KVAc5JqZmIJ_0QyQqvzMgAiCIq2YXfTq__t0nGmqbNtIEYPo605OpYJCpVK_TlXDp_0OHWh_i0q1frEh_fgo8OMX8gfigc28QKPN1koKYvSISQ6piDVIDqKkVkSql0K5kgytR7FfL1E3x37joKKuRYfEhhUsiUTOU3hO7xpuHJo9lqQlcSSb8TdVD7xIhySQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=n9aPBXgP5lozu5-iSyFPJLRk3P3kB8Ie_1N4Eqkw614MGq41KUm3tmMFP7g7V3AA1ZwwuXW2Ge22G6SjpE-z07wORhzDTsTow4-wHd-03TIdTTmAyd4Eo2uexk8YMMtkZixwL7CGf9X4fk804EjPM3KVAc5JqZmIJ_0QyQqvzMgAiCIq2YXfTq__t0nGmqbNtIEYPo605OpYJCpVK_TlXDp_0OHWh_i0q1frEh_fgo8OMX8gfigc28QKPN1koKYvSISQ6piDVIDqKkVkSql0K5kgytR7FfL1E3x37joKKuRYfEhhUsiUTOU3hO7xpuHJo9lqQlcSSb8TdVD7xIhySQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtOH5Jo8igGOdSz_TRO-Afj2Tn6ta3pKEco4bgSaXISDd1LESu33cdKWMK_d3trRqvPZWYNtHk1S3XeHclszWUhLcrvgbI8mjRINQJ_Padl7PNtU7NAyx81XE8K4PEYgp3YHKoHipbHp0FtyH34nHPuGXmkt2J6bX8eFEvpbdp0jAXciZA_8NMc12DKcT4wG4dJXwrJ82LStH6Ppl3Z-hKhwugYQI5Emjg64t7KzkLMHFRdePHNQKmnKqw8VtRpZPHF55A8O1MVPG0ttgd61zlVDj7Fs-dOYzrGqUnJSPcEny0AeMtCkFcZ43bW3WkmYojKxC0EeefcAWukaW69BzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=b6ULf5Tt3ttAv9fx4db23BOJ9MSPXSe6Zia6YN8ermv8gUEAU4Ilm2kr3PeMA-dMqtEuX0wzm5PsfcipNI7ir6UHnzwwvFQX143QuhWGPvhw3wfcIH0awXIzTsjxzRReGlN4GwbgluOov2ZmDXDopVoSUKCurgKz2BywMyqKkrpPRzJfXEEkR9dgbfmt-_P_SPLz7On5zmB3xDNZi-bBykLBg5MYBSI0xJ4fwCI-YDDCppZa0LP90s2GJ6bYsEaxXP5Wj55noLN1yur6o713dlzFFtY7-FOYSPV7SuyTnVsqVNaIhOM18lVMRG14OK_jPnLzQRgwbZ5-bcQos2OsWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=b6ULf5Tt3ttAv9fx4db23BOJ9MSPXSe6Zia6YN8ermv8gUEAU4Ilm2kr3PeMA-dMqtEuX0wzm5PsfcipNI7ir6UHnzwwvFQX143QuhWGPvhw3wfcIH0awXIzTsjxzRReGlN4GwbgluOov2ZmDXDopVoSUKCurgKz2BywMyqKkrpPRzJfXEEkR9dgbfmt-_P_SPLz7On5zmB3xDNZi-bBykLBg5MYBSI0xJ4fwCI-YDDCppZa0LP90s2GJ6bYsEaxXP5Wj55noLN1yur6o713dlzFFtY7-FOYSPV7SuyTnVsqVNaIhOM18lVMRG14OK_jPnLzQRgwbZ5-bcQos2OsWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=vbQICtprvS0eluZZ9aMFlfdMwU285MXmKT0l5iS762-U_qW0_gqeT-YypGc4LOQGE2N0tJAVzMPve2f-Tv1-UCkkjonTzv34r5F3Jkwtjxz88HpHfMrQjWa5DWdrfMKKaxRHvc7AKAIo36CgscFslKRDrEczRbyNvxip1q57RIVxqhevirvTFkJQ_2Qmva-oNx52WWsSweJkWe6Q5mlRhr671Poxg9XF0NO2ZTS-dIoBbza1GE_aVF1BVIB0LHl-wDZQEa8MDfVtDYeUeHQfJFJpwjanC73q6FIa9MeDjnqJohMQ9tE2AIqq14QMecARksc8bzbmnvWKMLCUVSECBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=vbQICtprvS0eluZZ9aMFlfdMwU285MXmKT0l5iS762-U_qW0_gqeT-YypGc4LOQGE2N0tJAVzMPve2f-Tv1-UCkkjonTzv34r5F3Jkwtjxz88HpHfMrQjWa5DWdrfMKKaxRHvc7AKAIo36CgscFslKRDrEczRbyNvxip1q57RIVxqhevirvTFkJQ_2Qmva-oNx52WWsSweJkWe6Q5mlRhr671Poxg9XF0NO2ZTS-dIoBbza1GE_aVF1BVIB0LHl-wDZQEa8MDfVtDYeUeHQfJFJpwjanC73q6FIa9MeDjnqJohMQ9tE2AIqq14QMecARksc8bzbmnvWKMLCUVSECBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=LtEV5JV6sYrgISH0sWAuDEVyC03xt3n2qa2_ZdHkMl2cyaLJlRWdqs_z0hNM9Ka5n0EnBEeyosxhVkaaRoEDaZYR2gqLanT0g3T8vUS_hM_AIaosN93ClGa9sLS1A3BzWq43lDWmGGzGuwxoAFoCtThm1P4vo_U8yT4fK18Xqy3TBNFEIZ8G64F_hYYhf97pIsf9eqra2mJYf-qBezgo3eCuJ5HkbiMJC_5otbug3Qz4acVTFHbagUJjhSGfwUxi2rxOvaoaXYYk7PgCxy8l3feLlJhWsjRGWLGyxQCDgRzqjkQAa702HbkWv6WVLe0XLyx7bfYErQ4LWyB5ULpgtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=LtEV5JV6sYrgISH0sWAuDEVyC03xt3n2qa2_ZdHkMl2cyaLJlRWdqs_z0hNM9Ka5n0EnBEeyosxhVkaaRoEDaZYR2gqLanT0g3T8vUS_hM_AIaosN93ClGa9sLS1A3BzWq43lDWmGGzGuwxoAFoCtThm1P4vo_U8yT4fK18Xqy3TBNFEIZ8G64F_hYYhf97pIsf9eqra2mJYf-qBezgo3eCuJ5HkbiMJC_5otbug3Qz4acVTFHbagUJjhSGfwUxi2rxOvaoaXYYk7PgCxy8l3feLlJhWsjRGWLGyxQCDgRzqjkQAa702HbkWv6WVLe0XLyx7bfYErQ4LWyB5ULpgtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=JmXd1hSQBSGNEDBaecssAAdQehUzpr6zIyIWU6EkdCCeodJ7g_jKHW4PmXF0-inqvviC6xXW4qwZxnzCf-YuMmrcsw9aDsaj9qKyyS_XVH4XOgc6oZFxzad7RXVjh8nUTcZskFlFApFiOs2GqIApmtwg7LD-I8IDJ346Z6jyus3seCtx_eqL2VJJaqnkQxZbIo_E_Pvjf-pV2GOsNVE9I5ThnrTav1Bm_wxym7tfcXNUbM67za-Yjy0I08efFGmUFTvaNUbmnNH0VBbkyu7mshrN4zWsouR45cPQ-rA9kySf1mj01BpEEvt5UwtEajH8I8J9m9m8YEl5Bg1u_NrIAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=JmXd1hSQBSGNEDBaecssAAdQehUzpr6zIyIWU6EkdCCeodJ7g_jKHW4PmXF0-inqvviC6xXW4qwZxnzCf-YuMmrcsw9aDsaj9qKyyS_XVH4XOgc6oZFxzad7RXVjh8nUTcZskFlFApFiOs2GqIApmtwg7LD-I8IDJ346Z6jyus3seCtx_eqL2VJJaqnkQxZbIo_E_Pvjf-pV2GOsNVE9I5ThnrTav1Bm_wxym7tfcXNUbM67za-Yjy0I08efFGmUFTvaNUbmnNH0VBbkyu7mshrN4zWsouR45cPQ-rA9kySf1mj01BpEEvt5UwtEajH8I8J9m9m8YEl5Bg1u_NrIAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=kqa4UXdDgMJQx0LD6tnu7_KjzevGWdbrr8IzHC-jwCgkjeggwIMdo1fYsHcoa92wxtyyxutCbFZtqS10UWwTIIvB5hoZNaMZUaPJf3SErCwVlNTUOtgUDvg0CSDOZHVhsi9G2O33PxtYvq58i1fH5I8eNJdxgC5GkhCtBg4yXpseHlW9ghifn5CF8CZQql-avmR2xFjOU4ASw0D0B4ThSphwwIOhUfe4hDxhDRBr43XVZpsFc7qLSCfszvvQJJfSoCdVKd5Zg7OWeReEkomuMunhhlzsUcxKWy-ogYH-EwPbKOKHMksz3FNO3aFDXP4smgnlXVeN0yyPDSGXvv59VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=kqa4UXdDgMJQx0LD6tnu7_KjzevGWdbrr8IzHC-jwCgkjeggwIMdo1fYsHcoa92wxtyyxutCbFZtqS10UWwTIIvB5hoZNaMZUaPJf3SErCwVlNTUOtgUDvg0CSDOZHVhsi9G2O33PxtYvq58i1fH5I8eNJdxgC5GkhCtBg4yXpseHlW9ghifn5CF8CZQql-avmR2xFjOU4ASw0D0B4ThSphwwIOhUfe4hDxhDRBr43XVZpsFc7qLSCfszvvQJJfSoCdVKd5Zg7OWeReEkomuMunhhlzsUcxKWy-ogYH-EwPbKOKHMksz3FNO3aFDXP4smgnlXVeN0yyPDSGXvv59VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=Pxki4aAFNQa5Lq98mYeba9A3dgQR2Pi-WIWF6M_Qz8KWVzld5V9nfc0Ie8LK6V6IqF8w-aqLE-9VXh6oBhFi37WWsptKRqu_OG2N4pbtx2xHA_YsqUmSjA1e9KcYDwJMhLLDW6VOOZjA9HJZNiFxeewTBvlm8gb5Qb0hgp_v34wjdPL6mzl27qrVKTqeSndoxjKreeJ3PAOg3q4H821GMxo0CcKNGMoWJW28kX9p-e0oGxZu8S_Iox1-H1G5Y-hpLK3-gcAdefrs2OZ-a-Xr8pi4aETFFDQbaLZ9N5kwxp4HrUMcUyfjPCTjAIHPaROec8yU0JExffvABsjzi37wmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=Pxki4aAFNQa5Lq98mYeba9A3dgQR2Pi-WIWF6M_Qz8KWVzld5V9nfc0Ie8LK6V6IqF8w-aqLE-9VXh6oBhFi37WWsptKRqu_OG2N4pbtx2xHA_YsqUmSjA1e9KcYDwJMhLLDW6VOOZjA9HJZNiFxeewTBvlm8gb5Qb0hgp_v34wjdPL6mzl27qrVKTqeSndoxjKreeJ3PAOg3q4H821GMxo0CcKNGMoWJW28kX9p-e0oGxZu8S_Iox1-H1G5Y-hpLK3-gcAdefrs2OZ-a-Xr8pi4aETFFDQbaLZ9N5kwxp4HrUMcUyfjPCTjAIHPaROec8yU0JExffvABsjzi37wmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXjU7GWguRRqav6PPjxwOhEVY2lfmbU1htntQWSNCw2kkRVZUpn2DQuNFd3lFsui3W4KFhvKmPFemKL1ivBX_ZHiQxxonHRpEOmLyhM_3Vn9iAPP69gkm7zBLIMvXNj6K48Y4F4-NKMYFPx8WWMX52so33CqCgRXtLtrS9RqzryE-qDAdYM-RavcY2Lqqe2yQVnq9ljFPxoQU_6rXQnwhN76BS-_Ky8QhiwGX4ZTBsZP-KlmtRcBhYNh_cQFGQ-vunydnDT_sFcp_Akwtt2WuEDpiAn_-pnXD_bdzZjRmUa9prUPFxMSqrpAkeCckDeyanDTSlRSQjo3V3GYpgNU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFwsHrdlsHUux38qmREKExXC4D59Q46Thh3gWu14ug3e2T3gWtThUDMG4s8_XksDndOo4eoRyiwy2q-_WjPnWdKAn9HQSetUDhHgt0UfQCO1p5oGu4LBK0eSEdQoQAwmbmwAjKTX4kQ4QT42PqGy_eySYNajNqVTVaxShASW7smOEfksH_wKgXiXrx1mWAoJOy6tfzj_tBoIj5Sg6daxNMsv5CT8bfI0Z7iv7cHT-w7HYcgQx8jXKlxPXnp_irE3KTqTyxl4E67wVcHbVAgej8B0kkH6CsAkfGnH15Y19mRzOP-nPxVhyHzEpSTgnZmnf1x-ER5MyeK8h1UIIRrrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdfYI0gqdHTVuApoc7xDCO_81aTTbFxBg29aaDOF9jlBbYk6Ccrgjz6qfwo2xEmYFfnOBaq1-bvAGSM4tOjgA1zj6jLkJgckn9VT8bdXCF6sw3y-K52Z8gUO2N0WYZDWYJv6xBJL_Mv7lXaQmcyPZ7drOtL_w2UlW3Cgk5_gQx4-_NG2eR9ftYEDUCzRCRrchv69HZ5Q0InJIY8xTWTBjzh3MgR5MWIpSK5b9N5D63v97OGWXXGYDywmG0OdPE6Yr7_hxJkbXVYJwZ08UbD9xIQ4pKqbrkZG5BogksSNmsH2uRFmzmp75VzanQBcrSvIyhXjetdlmk-mY3GkE9H1MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=QTQpreYAOzJ3tSFEIl-BJ-s0EWeKBNKx7OxfKymgH_iOfD5IZ7VbG_G2Ej7BP2sSw7_HXCnn_5taDNM1ghdsbPaelQzTfwYucIOiGEJHRWxV3YjffZctAQ0tEe6kgVMOy3NOl3_2J13sIrqgbFY4YoyB-Mrp-Az2BLEk488MT9hc8ZQgy7bmr_e_jkDBOiwad4QXQ81knt0Af77bVY_zaNep-1JbPYP1S287OoZHRao-XvIou1I0N23DvhbIBn03H4wADLRzzuoZLjnHBcPe1RezsfldqVWcvXkB5WWai0G4eA3_mV8Ozv7il_ilSRVDF2bG_B445jfKQ6hP22qXOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=QTQpreYAOzJ3tSFEIl-BJ-s0EWeKBNKx7OxfKymgH_iOfD5IZ7VbG_G2Ej7BP2sSw7_HXCnn_5taDNM1ghdsbPaelQzTfwYucIOiGEJHRWxV3YjffZctAQ0tEe6kgVMOy3NOl3_2J13sIrqgbFY4YoyB-Mrp-Az2BLEk488MT9hc8ZQgy7bmr_e_jkDBOiwad4QXQ81knt0Af77bVY_zaNep-1JbPYP1S287OoZHRao-XvIou1I0N23DvhbIBn03H4wADLRzzuoZLjnHBcPe1RezsfldqVWcvXkB5WWai0G4eA3_mV8Ozv7il_ilSRVDF2bG_B445jfKQ6hP22qXOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXvx6eWW7ODuII9IRgQ-LvjGFvwk2Al4GMVAiDk4yj1OMNzBSg-dg0MTN7pNmj5SMWjNzpIjbwmjdy9rAiWgFeahm0_3paI_ub2rITBfPjBzmc0fgJ47bg2MuVljEfL9LpiryKd2ciSQxk-WY9YTqW_LUbl3us-n5qbh4UNSLWZfDQt8lv_cbMxPc6KK9FjCgDOL70Vs8PdYLq8HnDXHGnJRiZlsKmMkonJQsT99EcAP0OiTO8qPS82FJsHKJVBojeGD46AiLol3H_ZtOqvfto1E_1uotqJQ5f8nRMr0VifE4OWHHbTzEPWeUGLqj8uslmhb-1piz1FKVn8G4M6hig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxZy3OHFmpLTMxEE2fbNih6gEHRZLMViQ8ILxVWZh2EYsmgBkl8xp-08TBcsFiQ0PbTMP9zg3JsC5PTP3EqEySbuXzy9DrCKRxTrr7OL9pvXWpL9yLPHYhAnuV75tDTFlxB5JWygP-8a9fJ7PCxwYwzbOcqwDEVa78-FjHSMdNbN8kiHBTGYi6q8oyxPBzS9lsITKIoogJpDEfLnJdWOrXAoxZ3jegm4uTgeglrkyBCsNhi_PaZnJL68l_VUP3bcsMawUfJonVP5hnJom1w4KxvMNbKl2NEVgqCyIXkCNrSaS-N30Pqw-c7rAQLagqNkTlsLmGtyMOHhBH0Ar5ltTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozDgcPGanFKJpGGxPQrzAD59EzXj87ECjdzUito19_PVm6M1s3Y0aI2P3VhrlpJ0s-yxtmp7-Te-fLiFJln3PaoGsqQ6CW9qwdaNBJzOaWZL6OjH2NI_dHkcO2nmsl71poOfZxlcfIVHK4Is6iyfnMC6oeiIpzTDhPmZI0EN38bkl6ZjL3KRG2nPBARJCFg7HyI4-Q81XpdbyTGIg41k1yaSFxbJ2X-bPrvDWSH0_dqG-TgO0wUJ1-u6QCVHgHzuTIifFsGSZe_txbQk3mYhKXsRPRzLT9GB3JdkE9gh8TneUNXB8noSOxbPRYvybU9nl9EYzoN4dcPBvEazJsvsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=ZQaNEeTPr7x2-PUB8iswHmba_Dch89bCCAkoi0gSfK3D8H_vPMRYKlxH3hyRBxKajp-ZB-U0u4yFKysyVzJ5JvZaY_NoylITWWcrMO-AbdxhaZFluqH2_4ymz7I9ifMf0E7XsRv6Z-bOn8J8iES12ih-z3oxnPB1RvLWtLTgNd1nxzgzNyL3Q3rLyoe5LkTM-moFgxANNw9Shtvid8VB3V3t4ypI2faIeli7DIJ83hXWaGB4mHDu5ho6_UtGKIOnnMbUifFllNhVoX_-ZTq2pSzNp_uhqAnX96KbnjZ0XAJi9iW-VYctFJgMopDY2ffPsuaPqRSfUEqpp2oPiujaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=ZQaNEeTPr7x2-PUB8iswHmba_Dch89bCCAkoi0gSfK3D8H_vPMRYKlxH3hyRBxKajp-ZB-U0u4yFKysyVzJ5JvZaY_NoylITWWcrMO-AbdxhaZFluqH2_4ymz7I9ifMf0E7XsRv6Z-bOn8J8iES12ih-z3oxnPB1RvLWtLTgNd1nxzgzNyL3Q3rLyoe5LkTM-moFgxANNw9Shtvid8VB3V3t4ypI2faIeli7DIJ83hXWaGB4mHDu5ho6_UtGKIOnnMbUifFllNhVoX_-ZTq2pSzNp_uhqAnX96KbnjZ0XAJi9iW-VYctFJgMopDY2ffPsuaPqRSfUEqpp2oPiujaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=BlGm-8IUmIcvy8WNByeS9uvrGSH2FQ3tKA6k2aaqrTAncpSW_cQSW2Tdx8jH7xsYGKJCv-AbaCcEyG6aBi38cpVCVolBfpYOv13npAX6ktcVfQVU3r1lcgRps_MQnYiJWf8xPWQuaqdWRs3Q18AepV5tIXfoQLYrqmPsLkjEHMIHAIFEiXjBs4szZny_V9Zw0HgdxjpB8p5bhQsgKc2tUUtZ12uguxZ_CXkqLv7HfHmsHqxiTCvRawOwG7l9kmEs7sKFclwt9u_11vDbbwOSwcf41DW0E8Q6BhEK7PMv3aAL5GamlufSjImaAHasJIhfCFGmfEp6_bYzW0RSOZH-THbR3fCX4Un4SxhK0_iIm7NYARLDCx1NQX2MTRh7zG9Om3QWhM4fh7hhMKHKRhzaGy4ZbdM6HAnJkkIN2gZGcSPM6weVHxvwkrYvEc9SLhs7bNu8MmghmXAJerBptLvS1Rjud-94MO1CZNddtXOdBwiEmkaLOhpApMzbL29e4jO38RWsy0vOXfI4usIYWdO7hyIufBbyvbedtIYqHqWpHfaQFKkFvZPqwroc_jO-u4b2qSKqaGiB0W3JYfbLnMs4VJX1gT5rAZvFkTQ2zChfGvkaHm43PdHn_aVt8Py05HGPMR089SvNoQdN4a7FbQBUrsrZDdu4XSP2yZCUr8tn5WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=BlGm-8IUmIcvy8WNByeS9uvrGSH2FQ3tKA6k2aaqrTAncpSW_cQSW2Tdx8jH7xsYGKJCv-AbaCcEyG6aBi38cpVCVolBfpYOv13npAX6ktcVfQVU3r1lcgRps_MQnYiJWf8xPWQuaqdWRs3Q18AepV5tIXfoQLYrqmPsLkjEHMIHAIFEiXjBs4szZny_V9Zw0HgdxjpB8p5bhQsgKc2tUUtZ12uguxZ_CXkqLv7HfHmsHqxiTCvRawOwG7l9kmEs7sKFclwt9u_11vDbbwOSwcf41DW0E8Q6BhEK7PMv3aAL5GamlufSjImaAHasJIhfCFGmfEp6_bYzW0RSOZH-THbR3fCX4Un4SxhK0_iIm7NYARLDCx1NQX2MTRh7zG9Om3QWhM4fh7hhMKHKRhzaGy4ZbdM6HAnJkkIN2gZGcSPM6weVHxvwkrYvEc9SLhs7bNu8MmghmXAJerBptLvS1Rjud-94MO1CZNddtXOdBwiEmkaLOhpApMzbL29e4jO38RWsy0vOXfI4usIYWdO7hyIufBbyvbedtIYqHqWpHfaQFKkFvZPqwroc_jO-u4b2qSKqaGiB0W3JYfbLnMs4VJX1gT5rAZvFkTQ2zChfGvkaHm43PdHn_aVt8Py05HGPMR089SvNoQdN4a7FbQBUrsrZDdu4XSP2yZCUr8tn5WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGl70rg46DEXHRLi9ZjP4f6_UYHyIPA2k81T3iqxfPcFLyMzILhrfiHcY-Wx4ZxKA41PNmzixdR3FwO9kThfF1xhq8KZKMZVMlAg9iQxT8o9AM5Cr77ZRAB5mfbZ7E-UMgZO1fCezkBaQwICNSQC4rt57JOIjKnYs0jE9GH2pDEs43jd0-AWgEJZz-0ZlMCZqv_W9TxfjvPvTOunxFqczhjWOu1yGASUHmHoKxUT2YVcftYuvLO3IwNw74-9Z2J9YmT0Og3KUpSPRIlczllaiT7_UNip8eLmS4D7HxsuEYkLG_ls9HYqcreOIq1MBd7MPHeKa8QcawVMemrOuP9Pxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=oI8oMY2seNQNfYCwkB9KrT5OuSgrtyOMCOKHQb-M8Ya2MBXsS3_wnpM3RJD_ng6pngKZM36VvcwEoS1M3PNvLb1QrWRuL3PaLaehINCkZzJUAGx7grWKAdYkKfGt8w9ccfMNRgkGb6dl1Xt2uDAwQXfZt-b-Iy9VjcsJx18U4TU6-xHk3D2uVQcpF78eLWIQiU8P_3Z5arKuZo_pVU2PZGYESAap3shnbrB_mgS3wlmYZfSRgC1ktWB6E-ihqj3ti-cbOE03efCmwVeD8q2DHLR0nsjdrLSqWsnPV3_3yvDydbzqGCZ-ISYP93LP6BELuu58AmEI7PUy24Q4Qk-GSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=oI8oMY2seNQNfYCwkB9KrT5OuSgrtyOMCOKHQb-M8Ya2MBXsS3_wnpM3RJD_ng6pngKZM36VvcwEoS1M3PNvLb1QrWRuL3PaLaehINCkZzJUAGx7grWKAdYkKfGt8w9ccfMNRgkGb6dl1Xt2uDAwQXfZt-b-Iy9VjcsJx18U4TU6-xHk3D2uVQcpF78eLWIQiU8P_3Z5arKuZo_pVU2PZGYESAap3shnbrB_mgS3wlmYZfSRgC1ktWB6E-ihqj3ti-cbOE03efCmwVeD8q2DHLR0nsjdrLSqWsnPV3_3yvDydbzqGCZ-ISYP93LP6BELuu58AmEI7PUy24Q4Qk-GSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4-Qj4nRiEiLr9-Muu_wlaBfRoyYjuEM9hFGnh1KmDkYIgvVuzjs6sDOn2DDldWWkKFLXaQsCOr1WRxEdIaSXnXsg3CWdZAdgiwKUYd22xsD5LH9nWhHdzzqkllHYGmghxI-bwMTS-lh4zIn5Ut-HHl57XPYG_o_2Jp97_xli85vIWn_-2wMNGySQ74Gf_w3xPTMj65huMoz9W1-3Elj3oArY-8S7CS-xwGSwzGSnuWjJ7q-AwF00zMHArSFFI3a5iEJiWupBHapyXW_G9yW93sfDEY0WFkWWm4CASe0tg_Do8IXGnso30QGrmJQxJTfqtDXFkDKry2LUCN8qsvazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=XTky15s0w8xe4NEnRLUMhgUDVf4z66bcnWITD1oX9_NEj_HODXQ8Vaa2kMS7Pdu7kBIzPJZ5z5WlwgUnHGhSUb9MdirJabi7hKu0H20cmtnmLL48Y5JyWgVdVtlGDmMDvkBNecv7VlYeI5L6-ujwlyqLAJ-hFVOQb1INMQUznJMYSP56dcX8xLnFfBRp__PVkSUMrJmRX_109tYv5e6aE2VB14tJ3rY5HaLJFBBbN7IS4_vjhXkKWz8Wob80tyDfXqLCy-c4IAuTWrkv50lqDolU3L4-Ebw40mZJaQ5ymH5uIuOsaytuVkjd1b9psfwllEcWL-Nc6D0yCyFXz226Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=XTky15s0w8xe4NEnRLUMhgUDVf4z66bcnWITD1oX9_NEj_HODXQ8Vaa2kMS7Pdu7kBIzPJZ5z5WlwgUnHGhSUb9MdirJabi7hKu0H20cmtnmLL48Y5JyWgVdVtlGDmMDvkBNecv7VlYeI5L6-ujwlyqLAJ-hFVOQb1INMQUznJMYSP56dcX8xLnFfBRp__PVkSUMrJmRX_109tYv5e6aE2VB14tJ3rY5HaLJFBBbN7IS4_vjhXkKWz8Wob80tyDfXqLCy-c4IAuTWrkv50lqDolU3L4-Ebw40mZJaQ5ymH5uIuOsaytuVkjd1b9psfwllEcWL-Nc6D0yCyFXz226Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyFfVzu05Z2lKBEYRKoHTpNVdqwUwt-jo1fl1DsHMWccgldbJOAgx1UOeU46-iKIvQDtnsuDYUpp3UH7dwI3koY7IcndBv8DxROswlFpcVqzoHUMzyIEkXcXqR33DmG2JpCD3x763-hWknUhdTPfRjKszZXAxIbVvzr2HmGx9OJVnW_KQ0VKdTeSdDCQf9nKCIQYa1IV1WiJPNV6NSk9HzSpcPIHq-qANb-_BlA15RDZ8sNvxjvQmep-qt6wJ77csZziuWr8GRsIFQRzcp6ahj0NOm1Rs2iw7t-Zo3tatf6mt39gi_FLMQDXJ455vBy6whDZC-q5dIt7MG8a01lq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=kDzl0KCuDvH1qrwWcxMcdnIxu4gKrGVj1HJFaStqoCPNhenbK4GbVNyFK8py_cIPADsSf8sxpVoCFtKbzWMA7ejnkd1GKTciYbcQbpIDe3PKXPG8dgkSRGRWia4dZNrhyaMcPttrobIpB5ZQinjbN293dRPY9l5QesVnEaYLZeXzkBRH1DVs-VWYf8_0mwUpyed64pNWNRIZsCcmi_Guh_5Bkaf8PJVvIldz97zj_HmIrm4--H-Pibj4-WMveUGte4aLkN4GYSU0EXAVqmdkNhxpFchNVLp4EAf3amXJK4SiKwGptc52TJaJxQhGXm2GhoLELGVncyyxuD9k3BCTdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=kDzl0KCuDvH1qrwWcxMcdnIxu4gKrGVj1HJFaStqoCPNhenbK4GbVNyFK8py_cIPADsSf8sxpVoCFtKbzWMA7ejnkd1GKTciYbcQbpIDe3PKXPG8dgkSRGRWia4dZNrhyaMcPttrobIpB5ZQinjbN293dRPY9l5QesVnEaYLZeXzkBRH1DVs-VWYf8_0mwUpyed64pNWNRIZsCcmi_Guh_5Bkaf8PJVvIldz97zj_HmIrm4--H-Pibj4-WMveUGte4aLkN4GYSU0EXAVqmdkNhxpFchNVLp4EAf3amXJK4SiKwGptc52TJaJxQhGXm2GhoLELGVncyyxuD9k3BCTdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=ZDaLC77VBhqDbqcXPHnFwtrPAWqdD8Rto1VXhMFDbagIhha5N8y26_mZabuYwPkE2Mehuf3ZBRVCYXwdqT5-lkg5gRR045N1d5Dg2JUwY38kY6IIMywRPpzt5h9RndHCa-nz2OTtMonPhlZ5zR3GLcsPsCcVpyld1Iu-ZgqsgvBN2SAPudmz_FbgKYxF58sE0FXfn_FWG3HsaO3-19DbKGbjgS7M2V8Goa1hl1JSlQcr2NZ40pkfurQG7X8Gj97FolhfRxxhqwe0C5Dlw4FA8OSmp113IXm1Stf_n-vvRXEpctcSHyE6YzxWg2uZPkTQyfJgzf_eh0Bf8ePvs5zCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=ZDaLC77VBhqDbqcXPHnFwtrPAWqdD8Rto1VXhMFDbagIhha5N8y26_mZabuYwPkE2Mehuf3ZBRVCYXwdqT5-lkg5gRR045N1d5Dg2JUwY38kY6IIMywRPpzt5h9RndHCa-nz2OTtMonPhlZ5zR3GLcsPsCcVpyld1Iu-ZgqsgvBN2SAPudmz_FbgKYxF58sE0FXfn_FWG3HsaO3-19DbKGbjgS7M2V8Goa1hl1JSlQcr2NZ40pkfurQG7X8Gj97FolhfRxxhqwe0C5Dlw4FA8OSmp113IXm1Stf_n-vvRXEpctcSHyE6YzxWg2uZPkTQyfJgzf_eh0Bf8ePvs5zCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuPCmZaG9JkiiLM86ut4De__sN7B5xmrFRhAzVHoatuM2mpryKbs8YrE2mhuQ_5jKl5QUXk51eduIry0BNyWuaYR-_ghI_5sx32o6q02EhCQNFkta6KZSTkVbltriPf3vftLdtuKMcGixW-NmXC-IUQLSoU3lQ_aWBFovAthwHocgnahb-NEgO9BqJguQCJB5pE0v_Yp0idfOi9uwmge84cnxt8d3iBscjot8RO3Hv4RySWiMVJ8MxR--rm5e16151Q7DYETD7meIQz1-_1fx3wNoRLmAMq-55jwVNWKEQSx1iSxfgs9n5SBlXl2p5EOLPexcHYSTZshU6n7xc-XDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=Q75qFDPzTPKcJpTUg0PyrUtphEuW69kBRTM6ggrnszZFl_8paXn4nnKZA63GdfaP5NxQTaVwAjNjUYEpzVy40nO52aEs_A9fgoTCmrMLJq4fvr1CGoI4ySRwlRkhDvHV4IAkcTAf1mVYUoFasyZK0gNgfwTPRPkCltr0GCCPS-pecJoVgp45a-Mhu1j6oKAUEyWSM11jdvhTGP_jti3ZPbL8VgCmcYjdz5Aa9zpWedTuiuSjQRyn8LGRzL_pJpKZfYavt1Fonw5hh9DReCj0oFsggFNcD8mQs4rzM1mj7abQ4y2aNtXg1FLItOOAgFxdgiyLba6Om4g_2v2MgDMofA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=Q75qFDPzTPKcJpTUg0PyrUtphEuW69kBRTM6ggrnszZFl_8paXn4nnKZA63GdfaP5NxQTaVwAjNjUYEpzVy40nO52aEs_A9fgoTCmrMLJq4fvr1CGoI4ySRwlRkhDvHV4IAkcTAf1mVYUoFasyZK0gNgfwTPRPkCltr0GCCPS-pecJoVgp45a-Mhu1j6oKAUEyWSM11jdvhTGP_jti3ZPbL8VgCmcYjdz5Aa9zpWedTuiuSjQRyn8LGRzL_pJpKZfYavt1Fonw5hh9DReCj0oFsggFNcD8mQs4rzM1mj7abQ4y2aNtXg1FLItOOAgFxdgiyLba6Om4g_2v2MgDMofA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfxHIqm_s1zSC1nMH76cUBby3SLxrTn0eA_70cc0l-6VvZfqVPZGOuJ-curjLysKtB_SYEANSMvr02YPimy5four0oTTwiG1loS8xLnn-g9BeRuEnwkxdM0FgySZ0nl9PtDcCYns54AlxRml-2wEs_IbrajK_w1K5K4gBu-t9hyb7tcMPihhK1GurzrPMOkYf8LmYFphH1hqBX35WFSl5Yp4sXMRYZTNesTkk6qRPHxY2DOoDpa-P3BXkAzYPfvssPYzAjSbZcwnS8e3nLMm8o_gmD3TNIO_NE79rS3mfHrWvB-inatB2KF4tj1g51RczpWHdewTW-bhOME5o2D0TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=dXhx7-9_YSX9F0vWnG-EZkVTWsZkcOfY-hprVb1QrQqx7SvPNTpT-K4MLuudUkm7yPWmeOLDYTUAs2w2dTGpuEg6BUT-K2UUYnPMR_F0S5LDl-5D428lepCT99exXXaBdWiJH8Gx4224-2fCmZetRK0f-0iBjonNlRn74bNWpEDqY5b6OuRNWR_hiGU8Go_jWp79BoOhYglK-r-yi1UNLZlZmyPv0HPoPSYxrJFbTqoo33RIjXnXRzr5u2M_8iTMhwWgQp3KOh-84bw4PwM9Egf8ddVHB3x94TXLL8G5J2g8eu5ua9va9tUn2MNywA51TmE_T2lhRSjL1APUWlrXvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=dXhx7-9_YSX9F0vWnG-EZkVTWsZkcOfY-hprVb1QrQqx7SvPNTpT-K4MLuudUkm7yPWmeOLDYTUAs2w2dTGpuEg6BUT-K2UUYnPMR_F0S5LDl-5D428lepCT99exXXaBdWiJH8Gx4224-2fCmZetRK0f-0iBjonNlRn74bNWpEDqY5b6OuRNWR_hiGU8Go_jWp79BoOhYglK-r-yi1UNLZlZmyPv0HPoPSYxrJFbTqoo33RIjXnXRzr5u2M_8iTMhwWgQp3KOh-84bw4PwM9Egf8ddVHB3x94TXLL8G5J2g8eu5ua9va9tUn2MNywA51TmE_T2lhRSjL1APUWlrXvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=cxMXW-rIN6IptIqX2l-ronUcrKl6TQSpQpWgFkQAhcAF8NJBAOWLroUBvOptyZNZkKta_fq46WZKMdkpt5Njl3OVvaM1tw9NT-LYbjWw7Tp3zYinH5i9p1Q38DatyUaB7ZX4F-FAQsVfP3rbGqYGYRxOVw-yWENxbQctJhWUBMn0cTC8jpppMX-Six9qIds_KyKDkZ8tTSO_aPlNNSaMVFEJ-bk5BmjY-VrnsCtUP9GXEh5vWlFcuxmmou9pJ6quI-HPKiMUDTrhLR7wPP1A8xnP5Q0b23b2J_tSnMpL2wdclV90irUGG2XTbuTsD8lI8LrfvEr2OhrcF6NFMlGz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=cxMXW-rIN6IptIqX2l-ronUcrKl6TQSpQpWgFkQAhcAF8NJBAOWLroUBvOptyZNZkKta_fq46WZKMdkpt5Njl3OVvaM1tw9NT-LYbjWw7Tp3zYinH5i9p1Q38DatyUaB7ZX4F-FAQsVfP3rbGqYGYRxOVw-yWENxbQctJhWUBMn0cTC8jpppMX-Six9qIds_KyKDkZ8tTSO_aPlNNSaMVFEJ-bk5BmjY-VrnsCtUP9GXEh5vWlFcuxmmou9pJ6quI-HPKiMUDTrhLR7wPP1A8xnP5Q0b23b2J_tSnMpL2wdclV90irUGG2XTbuTsD8lI8LrfvEr2OhrcF6NFMlGz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=T6D5VxlwuzPMS_735b8-CobO0OFTkdfGkHB7KWlpfj41SL-UQpbh9FOsLtgXUi33WD1gw4PH6Q0yo7EVliqHYR6AhoMJBBRxp5C8FXdwRUFd9gKqxf1XZfqY2wqXiFAdxKZnsXOOumevXpkPmGH96u84icLoCHbBnr_nskNKeHiX-C-tVqwpoxfHnkn2KbOIz3uDb5m3cvON8zPlfPT4VXOHCf6aGqjK9HoRwXl8Qj-9D8blKc0Tp7NpmlOO9DrbJ_xJcWDT6FnPYeNlYstKhkF_mVdiuF-6Yvs6jL-qFzasGo-SiKcPOZjI8KMyFfuDvPj4et9nT53Fvwk-3eMPQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=T6D5VxlwuzPMS_735b8-CobO0OFTkdfGkHB7KWlpfj41SL-UQpbh9FOsLtgXUi33WD1gw4PH6Q0yo7EVliqHYR6AhoMJBBRxp5C8FXdwRUFd9gKqxf1XZfqY2wqXiFAdxKZnsXOOumevXpkPmGH96u84icLoCHbBnr_nskNKeHiX-C-tVqwpoxfHnkn2KbOIz3uDb5m3cvON8zPlfPT4VXOHCf6aGqjK9HoRwXl8Qj-9D8blKc0Tp7NpmlOO9DrbJ_xJcWDT6FnPYeNlYstKhkF_mVdiuF-6Yvs6jL-qFzasGo-SiKcPOZjI8KMyFfuDvPj4et9nT53Fvwk-3eMPQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=IqU0wImFRKkIEAcKq9z1RYFLhU0zDxEcXHIASCTb5iqzLwSTSh518eEBQbO005yzV7IytwcnkclXQcstF804fCzRe4XGkHGmo1LpydYsdLNWV94-z6LkyzETJtjMcxMHGnBniUl6stjrIHemDx3jSW-_Yro8Yxy23BO4gzyZFobn02DLDNVRkzgbGRrLoGSGri6PqpG3QIDFhdPmv1omLhYWtjS5dhgJ40Xw1zZtpKoG59dFU3LlXKibosPwAa0OVB1XNP4ajQObCjyTEzPeyj7ze7u3W8m-KBhO2gILQ4O19o_MiWnzj0zvuT8fsPWAdV0GiHxCcJcDmpZLiDaJPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=IqU0wImFRKkIEAcKq9z1RYFLhU0zDxEcXHIASCTb5iqzLwSTSh518eEBQbO005yzV7IytwcnkclXQcstF804fCzRe4XGkHGmo1LpydYsdLNWV94-z6LkyzETJtjMcxMHGnBniUl6stjrIHemDx3jSW-_Yro8Yxy23BO4gzyZFobn02DLDNVRkzgbGRrLoGSGri6PqpG3QIDFhdPmv1omLhYWtjS5dhgJ40Xw1zZtpKoG59dFU3LlXKibosPwAa0OVB1XNP4ajQObCjyTEzPeyj7ze7u3W8m-KBhO2gILQ4O19o_MiWnzj0zvuT8fsPWAdV0GiHxCcJcDmpZLiDaJPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwVDI27ybkRshOexmMyHrrM-lmX60nC8A2iRfP_KI1AD4AuAE1uczlYgiYXMIHSV4NCHl2mugDDGpVfk_S-ZkXdeM71UVO3Dm3pkTlf7yy129zGtPpX5phbQhDYI-m-yPsdOKq4lmY2FS_gntsWaQO5x1mrEboMcdIEmeDMC_8Sfm1EcYyTFzblvzf_A34qGqjZeT514282wXC02jRh_LnpmoSmQ9IYbbGlj3tJhnSCz83FqADPhTEOxGSzHJHnj8n-NdlfjzO0WixUYOUn-AYqP5NhqXoln57wEfSrbmKDX86NibKiLbh0Pr2Ig7kxf8R-fv0DUs6BAdb0eYj9sTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MZB8fpDMB-_xqDx1wOMGBPjfq4S8UQslXEmjgskBVB4dsskx425bj0aP2mfJ3HnqrSgW_UKKpP7WHI7dczttvT5ogcOuzej1GoWZeQdV7L4f6ZeiJNHJlvcXPB08dD55MctSr8EbmSiGgDa_9YsUwTBsfwRUH-9Mmf3QPsMOp-rVQ77S3-6c7D0a-VioUbOj4ujJNDRuxDL1tPGoJorXvJpU_5PKWj0ycJctyr_Y849OVDkD5h364IYBfWo_zagYqOlf5j2bNPnD03JjHrFN3XrmpMx5L7uchRRDrFYKi8qJ7Yk48TAnvNp_SdQ5oVApZ4WE0J8Zt0NCu2xSCOoo7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKvyGCdGYaXhMWiHhWJPnQFtA-x8CMc0B6p2HZQPilfciCP0dQBmqRWx17C9mguwlSZbF4FcTiDxFHRJpWjeFHiay00LUQm9oIeXgWNAcyoJQ6RlDx6VOLDboSZKMtCJrDe2rkEf1J416ez0aot6euAp0eDNe6CbrYsPAktqZj9FbpNwM5m3yGNNFJazk6QHyenpKzB1SVujlGiYDAcD8HIpHBYs5I9nwiMH9MlwQI6l_O1qcVYIeU79xjDKU53LZFs_gQSoQiBvJZc-WgT97LS-nqbSo03sPkDKabKmkkwKLKwIWq0Qw9hYIli2pi_u4JYV_Kk44s2RHI0m-ugFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKxkIrgUxzpXJzlGDRyYwgngO1hYSVVv0wcc2P1sVHb_wJJzQk_kTt20AIhsTZ8VG6dJCmGFJss9UtLjOg8PtcdLzhClI_A72AAZETzFc68xpZGvpglj7RIfwIq2uNblLNtv4vZ2NLu-FYgSa4u44mstcJKy6KxcrmqkS0yM06CQ6gLp5rrJmpUGqijtw3Zf6bObKvXtG7jytrDK8a_S_OFf-10FRbAY4Hq1L0n4TmhNP-CJnNTnDfVRfaRI_KAKyxoKof5C6BE9t5vRMiNCPAzcwBIHSCWR0pYHzYc7Vd-1MaFys4LwYGieyNFWNSp_195bDm6aJORqE8bW47aPwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxcIZ9sFIP8trHwfizzTDki8ANOJ_B0VQohVbuHo14vzcpZj_xPXVqTac6-Z5j3CVnRHI7-m8AyFV9f-Ee7bv3lS010XwuV8FScLabEjd_OSxozwwwyrv2f6GsyZd29710Hq_yNIDQh_oGeFUIVLmNFvENevy9EubCW3NKmWUSZ88l9eF2LUP3kNZswihUzB-4qxgLjCPMrzPTZstB9f7enC578gFFvDrsut3zKauDKjvs52Z0XMKBeCnt0h7ZmK_N5VVEJjaVO43zeWXIuUGUmsNhUjqAeG9MCST5bqf83cCng7IoZmnbr0H6tuAopLyUjzppxdbEeYePoJ95yLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
