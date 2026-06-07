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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 22:38:20</div>
<hr>

<div class="tg-post" id="msg-65381">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است  @News_Hut</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/news_hut/65381" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65380">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
گزارش غیررسمی پرتاب موشک از کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/news_hut/65380" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65379">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری
؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/65379" target="_blank">📅 22:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65378">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/asIWLaRYKIGB9o-HlE598HXYic5Kr-QCwYY-ma49XFGxXARMqinI5nw3oImDSPzk6ohprb7BqLOe3j3VW4N4LSzGMtJJA73Bw3Mg5vA2y51XcVE0Up3iQ3uDOyJaZk4eFoKNady72dvKuaE22bRTa_fZ1mfYhLP2OLZM5xersFMG3VjQkou-EwZvRYBDxIZ8xX5I-luHhxFgZ4hGPb_vov962dNYpBF807UWi4ZyVgcztKFGFHHIh0SR3f89ynf-fBysPnslp4UyuGokliuHz7bkiJ7Q4RvswXpMa9x-1JiBZhxNKabe4Qb_uT9kWDLkDk3h3zd01EEp-P5ibD3IkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرواز تهران به استانبول به دلیل حملات احتمالی ٫ مجبور به بازگشت اضطراری
به تهران شد
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/65378" target="_blank">📅 22:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65377" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/65377" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrcdozbgLgRVPwmrKw7yPJRryJYtCN4AG6hOjGo5TvF5Kk0zI523szeZphkEpuYDFmEwEYnhVxoGyMB5zmeXhCmXVZxdhAv5Hs9ZM7KqfaSSrYZrNDf2GDrhQS03VlhHvEmC7m_78lATaNev2tTmQshVmD9fQrMgZsOgQZfhKeq-efakOqrkRorUbVubuz3Eor4KfsL3ddamdUk4IDOc9KKPpi3XO3MGMRTNp8C08pZff1V6m_hgG3NL3vsGtQPKJzpBOpP3rWByhmE9eJRk-rPyD5vxABzk02SeNz0-U2ImEU3KOwN3tOOIaHdjthGie-sLiE6PnQIhI4g1vhWf3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/65376" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BeRbT08Jv8TY8FCnEasfbu_g3V1TJW83rt5vqVyXucTUolAYWzTH1FCzVpW77RZqdFZrl1PJppKzW5TBbwdxxn4Fjy_JvrF6YnnB1QIFLLeGOV7IM-Qu-tF7KZcedeEMSqPAzbfdo112BE94lfFPhnWRdClu9mFe8GxaCvusE4VKMwjpapjtgkFnNcJ-GXS_Bh_Et_wVgTOPSV5sqa8HQVvnZe3y3nFRoU7GiLAFzLtXMFrzYSuOdIA8HzTrLNBRgXH9Ua9SOIEpqDOhXlqltusa_R7CRdqED2gnaXEqyP0TrOvjCJcQ-H1wzCR3D0XJdTG_vhvXVh4iERR8Xv7GJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
د اتلتیک: نزدیک محل اقامت تیم انگلیس درگیری مسلحانه ای رخ داده و 9 نفر زخمی شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65375" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65374" target="_blank">📅 21:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQKn-GtgpxrpooK3bz7_xDEL6emhBwaDP2_5aO_2LoK1m0dhR9mvPQQUSCcS-xk4oXCQZqT48P4sjLmd43cIgVbJkPGNkX2Y_ipSIl_a7N_E5_kJbXgQUELVfCkmQ1jFlqrKZjPntsFe6sycPAWPTi7qMbR-IhI3AAcqjFa34reXsdowJ8jQDwtL-Zc4fubwlMVsabwh1VKpnSr_W9e5ik429JcC_b9JMDjy8n7Pp7jNaZuP_9KuR5q0GOmx6ViROLAUCGpKX13sJUTk568Ub1uNsapWZxhT6dM7Q34Oy5HhlpY6ifdHWiMXrwk8siS3OyaEwzZ7en_vDMttmAWN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۱۰۰ روز از آغاز جنگ توسط واشنگتن و اسرائیل گذشته و به نظر می‌رسه تلاش‌های ایران و آمریکا برای دستیابی به یک توافق موقت جهت پایان دادن به درگیری‌ها با پیشرفت ناچیزی همراه بوده است.
همزمان، وقوع حملات جدید، فشار مضاعفی را بر آتش‌بس شکننده فعلی وارد کرده و دستیابی به صلح را دور از دسترس نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65373" target="_blank">📅 18:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با شبکه ان‌بی‌سی نیوز گفت که اصراری ندارد لبنان در توافق کوتاه‌مدت میان واشینگتن و تهران گنجانده شود.
‏ترامپ گفت که به‌عنوان بخشی از هرگونه توافق، دارایی‌های مسدودشده ایران را از ابتدا آزاد نخواهد کرد و هیچ تحریمی را نیز پیشاپیش لغو نخواهد کرد.
‏ترامپ در پاسخ به این پرسش که آیا این اقدامات پس از توافق انجام خواهد شد، گفت: بله، بعد از آن. اگر رفتار مناسبی داشته باشند و به تعهدات خود عمل کنند، آن وقت گفت‌وگو را آغاز می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65372" target="_blank">📅 17:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65371">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65371" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65370">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65370" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65369">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: احتمالا بدونیم مجتبی خامنه‌ای کجاست؛ اون از پدرش عاقل تره!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65369" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65368">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیما: منتظر واکنش قرارگاه خاتم باشید  @News_hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65368" target="_blank">📅 16:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65367">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم   @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65367" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65366">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65366" target="_blank">📅 16:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65365">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65365" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65364">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Shl81rMs3B0EitHN69bXH48alS9gStDt8t0SwZkyu14yiKOXFX-XI85aeyPUfGwmUzX9O_dn5P8QcyTzzD3fc7IyQa3ELX0rWkxawHe6SoYHwQiTTjAglOPKY3g0vUwmWCHsKUpGDqejan3QE5K1D6YmnKe0o84kqL2_YWfcCeNv2WLIs0kUS_GpdTr0-NyjIXnEh67FewZHVoEMZD5mBbPLvTrMDvLWWroITQI4BvNpzdBmk54LwIW2X7aGkO83KdPdRL0ayJKotMlHYLKEwFuBhwJ-TQUsNt6RAS6MAc-i_GPX6CQETeHFgUpmOKyRnkjhI_4PrW70VKBnNZq2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65364" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65363">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ اسرائیل رسماً به ضاحیه بیروت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65363" target="_blank">📅 16:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65362">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGL_RAkMaJtjoxyZmNig6Ye5rFK70-BEFwc7P0BTfWOskwaSrsuNfMyg_3GMXb1ZH4aOyGN9PRF61EhVYXklbrPzaD23J0lpTOmoQPDEZIks_d156KO-eMGtwPCoW12nCx8QbG0VS_DgXgeQkDt37otinKYOF30TlIBeGMQra9OMnXm1zrzqZsnv_iwkjaIypOSWrNaWwYYoGM5kdNoAfLzlFu0E6sF2gPVqJoK1PYjDmZJSyqi0JfZutng4pxmAjsXXrcANbyvaderA_QqnDkUrlbAzfHkc3bnjkD_nSpKpD6uhifwMQmkDlPFap1YYQ3815Z3GqOmr8VUAwMo1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل امیر تتلو:
توبه «تتلو» از سوی دادگاه پذیرفته و برای طی مراحل نهایی پرونده به رییس قوه‌ قضائیه ارسال شد، ولی هنوز تصمیم نهایی اتخاذ نشده
اینکه موکلم برای ماه محرم درخواست مرخصی کرده تا بیرون از زندان مداحی کند، حقیقت ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65362" target="_blank">📅 13:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65361">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65361" target="_blank">📅 11:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65360">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZcZVouJ1EXlnQooayhyo-dh32Hga9Xef7_WZip0rghbA1FAiIG_UwqBWdsdA9B9j53OImfpgpIYIyTtFTJdG_IORHuOOYrmQRAvu2k8r4p_Od4DQGu1Lg2nPQLhc4dWhVyS39727HP4h7QSzGiPQDG_GDPBPX9B4pCRvlDbao_k0_a7DWvbJZF38O33HYTokYHNaFfh90UekH4bbr4k0y1OnL7jtYkH9nGicrCcmvg2fOxLxDGpPFAN4hp7Bzzi-0t4qRQim2GrpQWrgRiaDNXvjKNB9FZCOLGxv-TrXV0zuEjeguGPbEvl0bIBJvrBWjbFqP3whZ_Q8bULmt9p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خوبه خدارشکر بعد از این دوتا پویان مختاری هم برگرده جمع نخبگان جمع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65360" target="_blank">📅 10:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65359">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SprInxUKQUyd3NZk_O1Iv228Ri8gdy8SOB5_cVqHWxpc2oZLgxs8Wbqai-TJ82fkp3ZWJxHbTm18FFCn_jmxpChZ4GuCZ1Hh59o2NGhJn-4b5F4fzfL4-vk1p0QQ6-vyqA7-ZNaC2ieJ_T6K4Fqv2Vyp7BifN_0dFnhzjfVs3LbC_MClo1KO7MzKDI_j30J8VetRQ4NHpyuG_V13wZqerW9J7fhhpdzQzxmO3z766UBuB-0_thtI_tn7P6UovRnGn7RiAu-hjFAgoSL4HJorto-EIygWOFwSHUq8a_A7243w8z_XXaezqBcmfx46kZog1nqyOnnN4WkdwRfG4rerMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش یک میلیون تومن وجه رایج مملکت از سال 97 تا کنون
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65359" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65358">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884f21c214.mp4?token=pupjp8FpClfWWvoI1wSKqwaI6sdT2l1MEQOfkYne2UOT4wIFyXVXsHagcsOAkwyYdjr6d32ffA4ObOGWD2br0G_hMsLn81LT6ntrGmOD3bTNN6GVOS6XaJGEyN_3OrTOdMLQSoqa014qFYpqFBm5XJ0fJew9iQehGtqD7z28IMiZBkTRMcpCAnEeMnNueSzo851e_b3CLZfy_bc9izncFnTkgQk8lOLs7YC6Lu-4F-Q2wkYlz9mYSrBiR6zJb_OZNmfW0lfQ3GrW-wDuthghxwoa4kduDGs6mdUUfT0rYTzfHFNTGhXRiDXudxKKOJJQlCq-Yfm9m9NO-ZZal9nvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884f21c214.mp4?token=pupjp8FpClfWWvoI1wSKqwaI6sdT2l1MEQOfkYne2UOT4wIFyXVXsHagcsOAkwyYdjr6d32ffA4ObOGWD2br0G_hMsLn81LT6ntrGmOD3bTNN6GVOS6XaJGEyN_3OrTOdMLQSoqa014qFYpqFBm5XJ0fJew9iQehGtqD7z28IMiZBkTRMcpCAnEeMnNueSzo851e_b3CLZfy_bc9izncFnTkgQk8lOLs7YC6Lu-4F-Q2wkYlz9mYSrBiR6zJb_OZNmfW0lfQ3GrW-wDuthghxwoa4kduDGs6mdUUfT0rYTzfHFNTGhXRiDXudxKKOJJQlCq-Yfm9m9NO-ZZal9nvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از طرفدارای حکومت تو تجمعات: ما تقریبا یک ماهه تو خونه دیگه غذا درست نمیکنیم و طوری شده فقط میایم اینجا میخوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65358" target="_blank">📅 10:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65357">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65357" target="_blank">📅 00:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65356">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65356" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65355">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65355" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=n83qYz2vUNMqQ13IDZAbpZkg72xy3wOpNAjBwZ2oE80lDMbvUGthTOpfg6PLU72tt1pMLGFGbE2IYgVwOGTT1aNPMg8-dQSQSXgnlon1Bv2PzG3LS36whVhbRDVeSjEDfqfWT3riRJrOfpB9EkPEg0awDY8U8AvBDcuj-UUheQR7qexa7LgAsKpZLfZRF2HkfMaddDNmNCyWsHO0P1j_Pjnv4t38ZJx63X3dE09pbDEd7_d2Uv4NqThnUtX_dROlU3XoIy1VGQnoS2YSKe2vxGZ090pbCo-T2H7_Fsz0jptgoaDQtwhuXm9KYKAX3rs7hNYqMnEK6f6BN0qvrySM-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=n83qYz2vUNMqQ13IDZAbpZkg72xy3wOpNAjBwZ2oE80lDMbvUGthTOpfg6PLU72tt1pMLGFGbE2IYgVwOGTT1aNPMg8-dQSQSXgnlon1Bv2PzG3LS36whVhbRDVeSjEDfqfWT3riRJrOfpB9EkPEg0awDY8U8AvBDcuj-UUheQR7qexa7LgAsKpZLfZRF2HkfMaddDNmNCyWsHO0P1j_Pjnv4t38ZJx63X3dE09pbDEd7_d2Uv4NqThnUtX_dROlU3XoIy1VGQnoS2YSKe2vxGZ090pbCo-T2H7_Fsz0jptgoaDQtwhuXm9KYKAX3rs7hNYqMnEK6f6BN0qvrySM-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیکزاد، نایب رییس مجلس: تنگه هرمز طبق قانون مجلس به حالت قبل برنخواهد گشت، تنگه هرمز برای ما از بمب اتم مهم‌تر است
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65353" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65352">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
صدای انفجار در جزیره خارگ
تسنیم: خنثی سازی مهمات عمل نکرده دوران جنگه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65352" target="_blank">📅 21:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65351">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUMxhnTvDhtm0ivbcbf-N56WREyVG8ez-wHCqfTCsiJ6U3VFlUeMY2pI_a6-s5GwUJmobbA0aXUU-O_86J1sTcNRcVjGCkriJtnQ6Vdbm4fxKRbajj9aa1UQKrko5_GCdzUn7zQ_P12S8RwTotVS8aom6pCTrugLCmuUsU_EkdRK3uAng8QsV9coCy-Ze9EWkh72imPKAQ2TY48WICCUqz6Cw0DP8beXMZfxXsVH8mxYHI2CCb5B7NscmtrNPHCe4Y2fm3JCJRJqXClrorIsO1wUV2apKSUiK3T6QU5fJlxszuxL52SogEHQJaLKNYYus-Go3D-sCi5o2_FGEMSWfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تو تروث‌سوشال: کتابخانه باراک حسین اوباما، در ۱۰ سال، وقتی کاملا به بلوغ رسید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65351" target="_blank">📅 21:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65350">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457010896e.mp4?token=N_cPKS8hqnE_4VwXU70OQQtYc_cqzrC-GvDoRpVYh5O7_QvRSDa_o01YZYZDPCYU1S9DC5D5ccIqz6MUkC6PysKpPwgO8OJT3Smq_SOO0SVW4QfKTY8gtWP9wWNjXe9lhpflIbY1nzKRzOdaoJPmE7W5ONLfPQcx_fZJyICC1ixcgiVV3LPP28HNhFeeB5_vd1EvpSJZhY-4uTVDzIiKc7Rwkxv6dz8hVLPTBuSSDX1nQYe-vNFKHivLnZq16fcCz0Yz3Xc0-hBzWiPOxxbVPl4xHSyez-IzGltsKULFsnDxxphAvppixZqry_cvb2Id46YyKB9e9ootZmZJuPeUjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457010896e.mp4?token=N_cPKS8hqnE_4VwXU70OQQtYc_cqzrC-GvDoRpVYh5O7_QvRSDa_o01YZYZDPCYU1S9DC5D5ccIqz6MUkC6PysKpPwgO8OJT3Smq_SOO0SVW4QfKTY8gtWP9wWNjXe9lhpflIbY1nzKRzOdaoJPmE7W5ONLfPQcx_fZJyICC1ixcgiVV3LPP28HNhFeeB5_vd1EvpSJZhY-4uTVDzIiKc7Rwkxv6dz8hVLPTBuSSDX1nQYe-vNFKHivLnZq16fcCz0Yz3Xc0-hBzWiPOxxbVPl4xHSyez-IzGltsKULFsnDxxphAvppixZqry_cvb2Id46YyKB9e9ootZmZJuPeUjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با وجود مثلا وجود اتش‌بس ارتش اسرائیل اعلام کرد که در طول آخر هفته به حدود ۱۵۰ موقعیت زیرساختی حزب‌الله تو جنوب لبنان حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65350" target="_blank">📅 21:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65349">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65349" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65348">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9RgEsnc4CnN72HtgIeOwpr9kL2HPa8GxUMtz-BON0E49guIY5JYtxUsvxa3SxWgZvaMaK1z76NJ9HuCI0XJwCm735nG5S1rmoAMNwWdWpUoOq1Wq3B7Sj-qJVsi-UdvulYiuVfv314wy_jAx_PmqXIq3PJkE1tfoyXz0grPA1XhxqctiCiErX6UfzQC0h4YBNg6OyxTbL7YLodwXbvB0MSWRI1WvE8QSzOUTjwAU3L35dNW0KHVIxQXkaDjFLD2uDH49QSavye_h5sbMQo4NW8l2QW1Xbk_5Y4JCBy_BKShR8tmqypuiEHDV4VELMSKifqp8xdacy-p_I66P_vZGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65348" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65347">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65347" target="_blank">📅 19:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65346">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajeqP4vCw0aNHWvZ6DhpXoVBbIo2c3XmsbA_WTmjU3-UFppNbuoC4miLYEe53GiB91r9OewSX0rSYJD2wY6h8pDV_ZRnCkcJYjtojCVSy8bDjjtvfJEVcrTQHhevb77v5NBSPDaRMjczIw5lVJwW2x6eu_f_zXBswbxF_kunDyqDqOrHDW0cpXpuqSBHB3Z9gzW9niu_zfF6UsOqUDnjpLd_CRZZCaA2DcXDyf-Qzb3IB-TvAPwoBA_bc29FP2F9DkWYJuEHrMkIWCsnp5UAfRdeBFLmxir3QpiZFJBKYMF122nIpXiYUo8V80H6l1jzOqeJ-dzsY3Nv2yYqkO6UuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام وزارت آموزش و پرورش رسما امتحانات نهایی پایه‌های یازدهم و دوازدهم، به صورت نهایی و حضوری از تاریخ ۱۳ تیر برگزار خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65346" target="_blank">📅 17:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65345">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65345" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65344">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxT-8KtoXiBrrAS0xxSS5-SJILyYGItI4TKYmxVfSfYfm-HdDXSItxylTp32oIUtvHu53We9rp-2kyvR15glss0H2QEhpQ5lCCX7LSUEMu2AsEmUWQK6Va-8_8IYCvmxFwQhFJRK1a4mcuTSo_1kr0vDJNGigzEA-QssVcgXxHdVetGRztns-N6-q0qX2H7-MLyU1cPbytmJLYwPwYgoDOXcPeJaanFG7ShasvytnIdClr72Fne9DgYuU7BYZ9BcP07G_ICxEar-VkWEyxd0yYPxMCwv0KibsKKK6ySwFlX_xRGBuCENyhS2kiy_Dt4TFD2kjs9VAejkCwf2G2NIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمهوری اسلامی پاکستان به دلیل فراخوان اعتراضات مردمی اینترنت منطقه کشمیر رو قطع کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65344" target="_blank">📅 15:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=Ns8juhD5eO3NWFQRo89lJ_zL1twKlS1Q6XbMuP3d-F3Bv8nmk--8VbyQlwPmgFpEs-27mK1HQAJW3gSsRQRfldZ0zr5wXfxXzY9swIWZr95-N9-NECjEJlV5rAR7fADsB-CcjM52SLVEviMEJGe8i7815Fls3lnRItqgRo2daHuGAXWdcqe5QH6IIJ4Ktp1thr6FIRxrUcyeRN8W41f6a7IUEclsQ0aIIA_ycS1wbAyMtQa2PfobI1zrFxiMbXoLKB-ljzVRBQayzUnjTB6m2E-eDmiYo-CwOP976uhFJxlxqN2xNCm8XMy9TyJ0vxOuUbUbgt9CcnYgsk6Qk9CogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=Ns8juhD5eO3NWFQRo89lJ_zL1twKlS1Q6XbMuP3d-F3Bv8nmk--8VbyQlwPmgFpEs-27mK1HQAJW3gSsRQRfldZ0zr5wXfxXzY9swIWZr95-N9-NECjEJlV5rAR7fADsB-CcjM52SLVEviMEJGe8i7815Fls3lnRItqgRo2daHuGAXWdcqe5QH6IIJ4Ktp1thr6FIRxrUcyeRN8W41f6a7IUEclsQ0aIIA_ycS1wbAyMtQa2PfobI1zrFxiMbXoLKB-ljzVRBQayzUnjTB6m2E-eDmiYo-CwOP976uhFJxlxqN2xNCm8XMy9TyJ0vxOuUbUbgt9CcnYgsk6Qk9CogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65343" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65339">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65339" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65338">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65338" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65337">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65337" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65336">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L4Yi8CJqad9BIa7r3bmt2kGSp8IB-Ll_no2Ex-IKIlF8hL082n2KbiGI0T5jfiNjv3wJuPU5W6LHunTCYTJdCHJ_IjMTdkn03_StIP-IeQA3zS_DBhX34AI-VHitHst1EO8-uhj3BMXbLT6VTKYhOoVmnz-N6rIidQ_JGvwDJZrwxpopj8Oc5HyiMHWsYSQy5ocp2OKp0BB2qPhjxfvouU0iRIEP5T4jyaJvuNrR3CiGzTALdjYnMaDpaH4M1BAqtdGVi50drPkU3PwxjIchWYVLUCqh76fd1CLmMMS8nVcfJkkSACklwT1W5caxbQYzSQrsIrf3tVS10shFhzO-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
بیانیه فرماندهی مرکزی ایالات متحده(سنتکام) درباره اتفاقات و درگیری‌های دیشب:
چند لحظه پیش، نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند. پهپادهای حمله‌ای تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای ایالات متحده پس از آن برای دفاع در برابر حملات بیشتر، سایت‌های راداری نظارتی ساحلی ایران در خارک و در جزیره قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در دفاع از خود آماده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65336" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65335">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLCEleOToGKV_BDQHbfwa22pudP1LxBRstlZtUwIVmUvXpd1Tu9lwDC9RS19kTSKqk0NrZK09DP4i9QiIMd_8m1tXGZ2C9FwOF8eizX9Wn2BBaBjL-jfEVohhnijAMpF7zb8V46bGWxGuGMsQc3SSu-wtaevIn5He9T80VlMO-gUL8crqEgnpWAI5xHBazlArdypfCet9sDBe9Cj_wfZ8OVkS-TqPbhhj6lbENvqEpgzd87w2gAxuvs2614b5hvfuYHmTk8arlyIa3-RBKzhfUnb3pq0WeqNCDTq2645MO_8pYsCoq_2KiU9wm9iUk6LSChz5zYat47EFVcFWkRM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم خمینی در سال ۱۴۰۴ Vs مراسم خمینی در سال ۱۴۰۵
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65335" target="_blank">📅 10:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65334">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65334" target="_blank">📅 09:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=R6zTlBYJkCmcvRIcFwUHOhJl49hibTcb2uYqqTbWp2JpDgjVj6IyEqWz4oNWtjxFeLjdcUKyA1YiChdCkHOTqR6JA2TjCx5Ys5UFEEz6BAW1DXwApPwI4lU-7dn59ze3Jdv6fseyLU1olSf30DvcfY5XJcWpsfC3TDkTO23qdRbPI3No41_darT-MtvAHGLyJGP3uFnrqUAFAi0DeIH-ufGv8qDpIaT4O8I0ykj2VwY5V96zE03dIiJ-ViwXhnEoKZi4dj5N53b0qdA_Wgk9ZeyoVmcTQj3z37-P59IQzH0gwCg89QcaAE4vBxaw5iLU3CSBIoUiWLU8cCA6sGQCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=R6zTlBYJkCmcvRIcFwUHOhJl49hibTcb2uYqqTbWp2JpDgjVj6IyEqWz4oNWtjxFeLjdcUKyA1YiChdCkHOTqR6JA2TjCx5Ys5UFEEz6BAW1DXwApPwI4lU-7dn59ze3Jdv6fseyLU1olSf30DvcfY5XJcWpsfC3TDkTO23qdRbPI3No41_darT-MtvAHGLyJGP3uFnrqUAFAi0DeIH-ufGv8qDpIaT4O8I0ykj2VwY5V96zE03dIiJ-ViwXhnEoKZi4dj5N53b0qdA_Wgk9ZeyoVmcTQj3z37-P59IQzH0gwCg89QcaAE4vBxaw5iLU3CSBIoUiWLU8cCA6sGQCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
مقدار زیادی نفت وارد کشور ما می‌شود و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند. و به همین دلیل است که قیمت هر بشکه نفت ۹۷ دلار است نه ۳۰۰ دلار.
وقتی کل این موضوع (ایران) حل شود، نباید زمان زیادی ببرد — به هر حال، این کار انجام خواهد شد.
وقتی همه چیز حل شود، قیمت نفت ممکن است حتی از قبل هم پایین‌تر بیاید.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwpbcgoS21sGasqCFWEPAS1r_wwYz77t0pKJOM5FJDG7aT-3hMW3pNielLa35pyk2rQVgq7sWxYttpYOzLa9MXoUEy0i-mf-lj8ABXFC_qgQ0xcnDczng1DF6wuiqbysSIj1X574_atc1NnTXTZUmcicqDYTJF3t7ZSIUuAOXeF3KQnnD2gCCa_ZvByCsNEuTFUptVsGRMOX17qumNOgvyxbxnZ8Hf1mU177xNFkg5u0V4aOUYWrMP19_FbYKSI-iGsk278dtr5Vs67Evs-rwmT_GKgZD6iyMxu32jiXhEgrvbubqQ7DMIn9Tr4EREtStPbKGrbc3JT2z4qSDAY0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=aFT2VMvEcFJ1O5NHoFeZyFF7r09YDKg5yJinmBEhNaQU6osTdAq3wMsYLNQr-x1sqehVuZfB5t2Fx6rzZvLNDGVM7nI8GNACHbyzHdo5SSG9TnBVbUjMxzwAGPxjNbbM_gy_9wiM5hoH0kbsPoSFLnpbhjy-KwkbSYx9q1G0zVmqkCTQGfTc8YVw25R6Ua0Y0qDPI_nWj343TQZdZRzCxZFB1ydtsE7P25DVhw8fZ5BoQ4-L5v-PJkt-Oog13lp2-2jxsa29DPPfX2-msyBMjXMxqaIsxY3sw_Sya7TEc4N34potiAUTQlAZsDqUTSIX5S94z9LPY-unNwj3wk1P7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=aFT2VMvEcFJ1O5NHoFeZyFF7r09YDKg5yJinmBEhNaQU6osTdAq3wMsYLNQr-x1sqehVuZfB5t2Fx6rzZvLNDGVM7nI8GNACHbyzHdo5SSG9TnBVbUjMxzwAGPxjNbbM_gy_9wiM5hoH0kbsPoSFLnpbhjy-KwkbSYx9q1G0zVmqkCTQGfTc8YVw25R6Ua0Y0qDPI_nWj343TQZdZRzCxZFB1ydtsE7P25DVhw8fZ5BoQ4-L5v-PJkt-Oog13lp2-2jxsa29DPPfX2-msyBMjXMxqaIsxY3sw_Sya7TEc4N34potiAUTQlAZsDqUTSIX5S94z9LPY-unNwj3wk1P7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=XCMTWXEPEjXcTIVYZgEy9vW509E0HRmUWZKNso0h-Dbre_T0-zuIipP21mq9Z7_Fe5TQY1RfeeyI_41l5GsZI3Lv0v4lFJD3I15v77TZxy9xMTh2I6-SbYPnP5pdc_POLfpbf3d6QeMpaMNu1R_5BAJyKEcq5n7GUUW9p9yA-Q1Z_Y10_SpndVcjNHJbKoPOjhA0IsJDDoBCHAkBxJuSWFPfnp11DDWGG69BqW22sYjdH2vn_iHViXjm28UA1aVeJ9lnHuDVezDp_8F05peqsK7mO8vzzyhBoItQ5S98ns-_7HbaifXXUoA_XFMA5JuJM8kY_l1ncpwlkuow1QDiBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=XCMTWXEPEjXcTIVYZgEy9vW509E0HRmUWZKNso0h-Dbre_T0-zuIipP21mq9Z7_Fe5TQY1RfeeyI_41l5GsZI3Lv0v4lFJD3I15v77TZxy9xMTh2I6-SbYPnP5pdc_POLfpbf3d6QeMpaMNu1R_5BAJyKEcq5n7GUUW9p9yA-Q1Z_Y10_SpndVcjNHJbKoPOjhA0IsJDDoBCHAkBxJuSWFPfnp11DDWGG69BqW22sYjdH2vn_iHViXjm28UA1aVeJ9lnHuDVezDp_8F05peqsK7mO8vzzyhBoItQ5S98ns-_7HbaifXXUoA_XFMA5JuJM8kY_l1ncpwlkuow1QDiBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qYQ33CWEypQZ6WQXVOYS0V5KHAiOIMuQTFfC1sIxYzlnS8D11U5-6gCZ2dUSI3kVZBJlRUbDkesAsKCTYMlaqH51iqGge_2A8CgRsQeJKab4XwkzjQt_9qengzGs-Dcvm0L_YU3jDyZWgQu4VGTmMvk47yLEE6Yj_HUwFop3zP2Hft-mAbgABzUhEYCcWwS2v7x7WyPl0mguOvVhI0qG0RlMUJztgQy40qRBmjFd3T8v-M_rTMj6xUI4guSC0FsYP9iVXHTP873pvBUbr9SOmHmz9chXjjoAM-ZgHSasIAEqWbBEU4AIHlm1zVzTgF1dh_Ncc7cP7Op7JOWQDl6lig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SFbEpEgZp6gBF6D7T2hEE8VL8BCJGxksR30TRY30mvTYopZpqaqjy1p-8LGYFrBNbmnzuvU-ye5rgg8JgGx8lttJxlMeTLIlK_autlsBkcYF8Yongq6H_225wmcfgYj--kvbpSpI-G-JE1TeSoMi3ZbhBM7ubJIRvBXAX8XMKzBTLHsfAatYo3jmnilw8uk5CBYPh0JIp9q1jc_MeFbm0KPVSFKmByYfbBKoAeUM_v7E5KmfGvOFv3LttyrsOE8PPBpdJOXa04nBKXZIM7JzYX5ijz-59kJsB0NyHkLtpT9zfw2oqwg4F8IJDxxKBEdgF7ohslx6HxiWIvJJhTuzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UN5varxATB2Nu6QreyvS8c3BT0oAvsOqCaQU018O0cbsWjMxNuHuFu61NEC2vnsQhCj5UQRNl-iZxXhSSUN_CPZlHy1ofl8h-QXvMYaGJuG-lvkDhT4ezqzSai_yPp3Lz5bbtIRRi0rKEhKrR1Cfe5TWEqkzVdO2UkNo24uITimt1YvkGUk4mZwAhNJ_RSIvxPQNwZ9hSsbP6FdQHBYir_cXznKEdv0yFxU2IurMDmeIRIwau0jtOzKLUeqhsw60TAvmCcnwAU-Hf7imimjQrujbBK5NLwty7-1rMYXbcwpXvnYZeqFHovF6oku-rsr87qyoQ-37EvW3fTPgPfM9GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds3eADNvduyQZpsWII_srcbGppsnETX4tsIlKpTjrl_oLeHqSMRWGWU0L9hWHhLuFh89sHQM5oSPcAOOcXi1KM-f-LTzsZZj2xDYiKk1QWKyZIbjYYWhXcHNY5HArfh8GW-HL0HHzo2pULW7fT4ucgeKb0DHMMOJodK-L8nb3UNSexiZiKysRTcG0LR4OtqgwXWzba3h7Ph8l9Bb2J9K2dfQHxQv9Re00REhRLIj6dOPHHicVsKtZ67sR6mV_lsu-mwtJLg1HAbomQOeIZN0ut8wq_VA4vg5WoHUPUcLo4Ii7ej3GPm99BelAB_zhKx7MP2j4Y3AbPDU9y98ZAfnuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtOH5Jo8igGOdSz_TRO-Afj2Tn6ta3pKEco4bgSaXISDd1LESu33cdKWMK_d3trRqvPZWYNtHk1S3XeHclszWUhLcrvgbI8mjRINQJ_Padl7PNtU7NAyx81XE8K4PEYgp3YHKoHipbHp0FtyH34nHPuGXmkt2J6bX8eFEvpbdp0jAXciZA_8NMc12DKcT4wG4dJXwrJ82LStH6Ppl3Z-hKhwugYQI5Emjg64t7KzkLMHFRdePHNQKmnKqw8VtRpZPHF55A8O1MVPG0ttgd61zlVDj7Fs-dOYzrGqUnJSPcEny0AeMtCkFcZ43bW3WkmYojKxC0EeefcAWukaW69BzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=FJEwoaXp70WZBT2HiC0AWIQQ0DWGqbUcWWkYtNWAz8iuC_V4iHNyyRQh8IhX9vgu72d_jRPk1yncdHw1A2iYPReAyh43MIcQRoBiSeZSakItlnmHr4DSp2GwdMlxSqY0mkYEIMQxInvWyonbvLBFu4SdLcy_oyoQKDWgl8m-V4BS_vKMyleR6pyVx0xYGhsr7i_G9JyYpITSlHfpcXzHFmHA0lGR7j6z1DxSVIHx1ozgUDVBXHTb3ro78VB4LnpEQEZanhaZZzVU-Pc47Tl0Ec-oG_MVyr0WcPNouOXQ_kVO45LyLotFCuet4d7Qx-pb_IQJZXIGVhFEBH5wySrhgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=FJEwoaXp70WZBT2HiC0AWIQQ0DWGqbUcWWkYtNWAz8iuC_V4iHNyyRQh8IhX9vgu72d_jRPk1yncdHw1A2iYPReAyh43MIcQRoBiSeZSakItlnmHr4DSp2GwdMlxSqY0mkYEIMQxInvWyonbvLBFu4SdLcy_oyoQKDWgl8m-V4BS_vKMyleR6pyVx0xYGhsr7i_G9JyYpITSlHfpcXzHFmHA0lGR7j6z1DxSVIHx1ozgUDVBXHTb3ro78VB4LnpEQEZanhaZZzVU-Pc47Tl0Ec-oG_MVyr0WcPNouOXQ_kVO45LyLotFCuet4d7Qx-pb_IQJZXIGVhFEBH5wySrhgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=rhp39ArE23iWYejMYbFrCbqZbUU-oLuK991Pm6-GmWl41jPvmW7KOdmQNkIlT7juao49qFtyxcPfL13zJ0DzjBUpbq5bxxSZEwvVoBkRkkl7rSYUBNUbViqa75rRCQxENb5_Qtep4mFgsD6IZHpowQlJ-aWzr12-iadJ1iM0ZGESJPPeRxvwIgbCLPQ-WCqzTepG-FhnYCO4nV5AjQNxSwNh6Akovmpc-2ttRSgWS-e5iAh0eaHAbXN1_UmDuVIoHBEtpSOUm-gL3hFWJkZgm90SPa5qLGKXg0-xD7GSqssa_rJ6GL_rhUvpALze-i8zIomtxStfRGcGeYrvtCVEyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=rhp39ArE23iWYejMYbFrCbqZbUU-oLuK991Pm6-GmWl41jPvmW7KOdmQNkIlT7juao49qFtyxcPfL13zJ0DzjBUpbq5bxxSZEwvVoBkRkkl7rSYUBNUbViqa75rRCQxENb5_Qtep4mFgsD6IZHpowQlJ-aWzr12-iadJ1iM0ZGESJPPeRxvwIgbCLPQ-WCqzTepG-FhnYCO4nV5AjQNxSwNh6Akovmpc-2ttRSgWS-e5iAh0eaHAbXN1_UmDuVIoHBEtpSOUm-gL3hFWJkZgm90SPa5qLGKXg0-xD7GSqssa_rJ6GL_rhUvpALze-i8zIomtxStfRGcGeYrvtCVEyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=Upq9YxTicBv5Ob_eHV3P8DptvM2njco6DVkM17RFFgs7eVFsOYT-JtKDNTlKOioaIfC99wM7JY4AWMSvi7GlXSkcJHrXiefKtaXJu8BE7u0quefN1g2gMOh__g_roC9tMGuP-lVXWbdsQ6ykv2oBRI-FFR0D7hb4lmdefqAI7xtGPnOjLuSQ39tTldI0kr2JMZUbpSanEQuZS-CIJfixRxPY-COQeux5f4ESAJN0ObV87M2HWAEWb8bavIoTG_vWvt-2guOTH93p3EdHIV7_vlRYom_3JRL4HLpxH7TRIytUVJunoq2Q9AwCINypjiuj5qfwVsS15VLlu7-U3JKxbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=Upq9YxTicBv5Ob_eHV3P8DptvM2njco6DVkM17RFFgs7eVFsOYT-JtKDNTlKOioaIfC99wM7JY4AWMSvi7GlXSkcJHrXiefKtaXJu8BE7u0quefN1g2gMOh__g_roC9tMGuP-lVXWbdsQ6ykv2oBRI-FFR0D7hb4lmdefqAI7xtGPnOjLuSQ39tTldI0kr2JMZUbpSanEQuZS-CIJfixRxPY-COQeux5f4ESAJN0ObV87M2HWAEWb8bavIoTG_vWvt-2guOTH93p3EdHIV7_vlRYom_3JRL4HLpxH7TRIytUVJunoq2Q9AwCINypjiuj5qfwVsS15VLlu7-U3JKxbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=ENA19pR7n9vjyUDEsqd0EoXOAPax99MQ551qK5zu3HjagAsu1q0KXBKwIZDYHTPZHrWQib3dHeS99G1XyPAniZD_GBnfXXiHhANrn-H2RgpI81_U4uSztn-kD79drqw7ZFCYpEtTxpQLF-rItmFs_BBUCltDJsCQGBF00J3Sll_T8L8n5YyrG1WjR14ku7nr9DyMhU2vGi3mKYR6QQ5lDp_0IuEB9vdioyhNuw-Sejn_3_lg0k3oOCRp0sfhPy5ic1aasNVjhpzjnRdNDu0M591PveebLkKJdBl5vNgg9dtE38mxoZhQ0UTt5h1HEka9C3-IpQ9RMoR0s9CB5HMXuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=ENA19pR7n9vjyUDEsqd0EoXOAPax99MQ551qK5zu3HjagAsu1q0KXBKwIZDYHTPZHrWQib3dHeS99G1XyPAniZD_GBnfXXiHhANrn-H2RgpI81_U4uSztn-kD79drqw7ZFCYpEtTxpQLF-rItmFs_BBUCltDJsCQGBF00J3Sll_T8L8n5YyrG1WjR14ku7nr9DyMhU2vGi3mKYR6QQ5lDp_0IuEB9vdioyhNuw-Sejn_3_lg0k3oOCRp0sfhPy5ic1aasNVjhpzjnRdNDu0M591PveebLkKJdBl5vNgg9dtE38mxoZhQ0UTt5h1HEka9C3-IpQ9RMoR0s9CB5HMXuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=nq3IWVyMkDAEZhk1Doz29kds145LwDfA0b9Yletv94T19pCaWMv8QNhLgimpgJtnucqvt-4dlJQGFvUIVtPLAevr9iEikttJ7Fmxx1gdKGYQS4-MYTYODJY1AJoHqIp4-20EaAt5Ks5-_F2hdjXwdZxPJIYe4CZTg0oksu8L-h78to0nEy13aGI6bbgs_JA_xjkhq1JuCd-ucp6EdZKvWOnMnVUfAeGVjwaT2e2i6RtmJpSJMbOMSn4IJm9Un_qut3fBsGTQPdJay7Adrp8xthLynHrgvp6aQO2SsgLk59PLQPfxao78g60ilxrm1BOYeHXvlg4PusFZ5LPJWQRZaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=nq3IWVyMkDAEZhk1Doz29kds145LwDfA0b9Yletv94T19pCaWMv8QNhLgimpgJtnucqvt-4dlJQGFvUIVtPLAevr9iEikttJ7Fmxx1gdKGYQS4-MYTYODJY1AJoHqIp4-20EaAt5Ks5-_F2hdjXwdZxPJIYe4CZTg0oksu8L-h78to0nEy13aGI6bbgs_JA_xjkhq1JuCd-ucp6EdZKvWOnMnVUfAeGVjwaT2e2i6RtmJpSJMbOMSn4IJm9Un_qut3fBsGTQPdJay7Adrp8xthLynHrgvp6aQO2SsgLk59PLQPfxao78g60ilxrm1BOYeHXvlg4PusFZ5LPJWQRZaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=mb_jEiCnuVlWoayUe6-oIa6JtgEMrv9UuvBwtq58S8bGP-AUgb-cZhpbzMCR4R6fIlz_Kn8jWdWIz8PdqJlfmzcv5b1qWnvOwxYKLlTEpgYPBSFUG_Q1G0zfBl8OxWyzTgo0fnSNBIuv17KEXLUv5OLrSIyj3cuQ0kfgg3SM3Jp-BhQn7y-i9EIQybQGgm4LzFXYR1qmVYBk3nm7YOVVWnB97KJLpItfP38SQiG--1XES3W-r4CENYrHxHn5llWpVU9ksZmwuHf2lewYVGFuuNX-Fbp2902JtoKro3C5pRTZ7nvPD-KHhLmePyXu15p9b5l3QH3LQJ4rMtWwko-wtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=mb_jEiCnuVlWoayUe6-oIa6JtgEMrv9UuvBwtq58S8bGP-AUgb-cZhpbzMCR4R6fIlz_Kn8jWdWIz8PdqJlfmzcv5b1qWnvOwxYKLlTEpgYPBSFUG_Q1G0zfBl8OxWyzTgo0fnSNBIuv17KEXLUv5OLrSIyj3cuQ0kfgg3SM3Jp-BhQn7y-i9EIQybQGgm4LzFXYR1qmVYBk3nm7YOVVWnB97KJLpItfP38SQiG--1XES3W-r4CENYrHxHn5llWpVU9ksZmwuHf2lewYVGFuuNX-Fbp2902JtoKro3C5pRTZ7nvPD-KHhLmePyXu15p9b5l3QH3LQJ4rMtWwko-wtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSowSbonK1yf_t6o6IcLodjO7MPkrECM-aNilbP_8NHPa0B2YSkwFyvYHHAtUXK39tf1ICQ-FR8kgnsw_osnXTQxku9Az7ANxZ8ocfZBRE-Y45H3DcLk2cwYqYz7uSeDs3exrolO6nUwOg-nc__YjFsHlZQuA0UZ3jjPKc_o-BD4Hh8fe3f8Je4109QFqq2nt9Uh-WFXubzqDvdZqliE31fiZzLWrMbf6nWt3nilmGPSdjvRL8h_TYGkmAdC_f9wG4F7F4GpHZ-LOh1aghSHn7cm_ECZg_bsPVog7hcLQaW14mAtbtL-JGcXRmhLmd04F193F6sejJgr3Q9uODv5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksj_a6T0YhnOtnGreu5PmcGZemDF9TBPEPRd5Hb2Zk82DFfd_iRipMStkKmNI7ElrPLtshKPdToOR82oLET_JtHvOYiGoofAIMmBClUUD1pSWPw14g6LtVQAoJ19ZI-MD6wo-_FLBsECngZJrw2YfxHVK61DyjANIg4nVjp8GEDaMFpdnMVHfhb2T5jPMLsJ2HX2m2lwBo4vLuqMgJcbDs3JXGEiYX3YasWxLYgpc5zfFMGYBuFQEvk5670Z_pvx8FK1I8cXLTDNuWerYT3LGOgb23JbBUTMyORXJhWaDjCYrvMDeCGRLRqKjATc_rmfWkGpecG7sW69BUMj5Vmxeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6szEWZdT4mnHtLNh2nFv-JUq9dW4F9glqSXfE-iHyZoL5JuBE7C8PWJqrLxfT6sq6D6aXDcz4RRxIsYQp_g61pYg0Z8zVRMRflKjw9BrMJeNmE25GjulBO_4-3eLCT4NxJkn99XbDPTsTkXjkKmtnVakvL6os3GW1VGAiSY3lP24eOJ1uQdfGqE5NDmjz3oMjsqVcigdd7ayDqBAEf7jf8nvV8DppkwU5gkLeZKnyXxQ3mKXaGp2UatZ7E0awHpmn1c2lX1QniH4dg8fGk04Uefp0GrJdnr6puDA75rybq6zdsNAQv3j4YCJR_76x6xuPexxapDLgkhlrRMM6umNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8CQ2oSOIyxmd6oP_8wG0rL-6FqNe5IcUwOjVFprnxJRl3xmdaGd2nru30CQHw0ElWuImYJ6yRQ1f3zs0OygJtIO7OALj5k9jVdkjLoXVH0gIP0UCxWvrcMMPWtCjh9Tx8qnQsIHSWX3dC2gAhjNxwuTgFDG6kWGXRIDOuW2O75zkUL-wMq4YQbOXPVoo-3DKP5NlgdUIk-7dlDOQhKXTCVPddDcZUvM6W4fV3XmcPIRJ1ZDSWir66qG66sxFpkVwiCpG8AMVsK1ka6uAhe9I9UCiSFtcwqqaoqFCOVJkSJ2ynWc9flbXjUWkLMJ1gwVaivVjwN6u8JDWMRl0CFkFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgGpRXfXZdKAS6OyNrijmTmsAzkDM1gunnmkRYyyuTHnx6n_7tXZP5hPOp05fd6SpCc0TNhrrWBnAbWImKGPHwiYsZ4_GpM_kI3pIv6h-eJOPDfGkGAepp46ZRRUPwN1lEt26lxp3yrTclvZuja7orh7stRmpg_CKfatKFNs6B6FcH43pBQxUc1Cw37MJeuYOf4y0vrct3N608aeSTrZCoy55i9IBSciGJ05vJFTiRj4fhzElD7biSm1LKhv0uRAu5GflykkuNj0_ALCe_ZfNj91Gq1EB4PSpsfkzNU6SiEyVkBoeEw0q8YUAOueNHn0wETRqBx_GGsUcre7FabFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRege_Z550G-fiK2tqT4gPK3ThY_xr7OsUgmErQoPUpk-BDLCSvph2Tx9x9m4RqTUenPysP6X3GPLItF9-x8tmAlA82fhuZ1GP4_UX8yoQMaXBlQma-oasaNvw-RfrG1McJEFJ_zNXQUoEPjacIOpvHaR4vcssMFBqMS_tqme-4nTuNKnowolljgMSj3Pi_nHat8DeoIEzUem9vdGrDVFRDQbAbxLBUckq3FbTMqz3xRNk-a--DguArREtnnvxHarR9f6IvJ0h2s6Q3VEZRky_6Y-V7BF42qDHw9JvbgcbOTMzirr9Gq2IA7NjtpWDBhlUMRYclNzuDavRCc04Q8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=bFqy6ymBVY-zaBFOeqTXm3ttLmlKCwqmk_HlbWpD9rE-FeN01DECJlDNIrSFZduAhx_x9aSEpq5eU27054vfe343XVoq2HMtPo5QcgGlrhUM1oju0x_vgKXGmaE3NluMNq8Usp8OQ3l4SXZI8kQfQdfV5thsT9LRL7KFa6xSo5LC2Mm9dHDqwDMQQL8kXokCSdtEZAtM41QxSNu-KpBNzITO39LRI_N7KoEYy8kA40zon4bgkRT8MTLWdsYtgrDIRqyW8zuuTkowfBAPE7F64nc1VK5ng6-4KAI1qayUQxjjshZY7nCMYEyZ5VyjJkhfmo-xnzjajSzF1nPJcOVfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=bFqy6ymBVY-zaBFOeqTXm3ttLmlKCwqmk_HlbWpD9rE-FeN01DECJlDNIrSFZduAhx_x9aSEpq5eU27054vfe343XVoq2HMtPo5QcgGlrhUM1oju0x_vgKXGmaE3NluMNq8Usp8OQ3l4SXZI8kQfQdfV5thsT9LRL7KFa6xSo5LC2Mm9dHDqwDMQQL8kXokCSdtEZAtM41QxSNu-KpBNzITO39LRI_N7KoEYy8kA40zon4bgkRT8MTLWdsYtgrDIRqyW8zuuTkowfBAPE7F64nc1VK5ng6-4KAI1qayUQxjjshZY7nCMYEyZ5VyjJkhfmo-xnzjajSzF1nPJcOVfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr1hhwA8IKnAiO7cyF5Fz4SN-nj0qCCXM5-F-pzJQrH8hAnkMd0IuILd7vze5fF290TcPh94iGDCiW-41GIYYf_enssPa8uTiepzD0Kfj8tGt4tVP9aI_VNOb3glJLYW43CnlLcp1QrKls1z_X_Qfkd1eTpebQYbL-jKPBZvBtBfwHcXDiSNHl1V0tt7OQQyLEtHIiyUNmk0RL0zKtJERU9jQ5K2-BS6-A7gFVTbIzVKSiTTKlku27yBjavNBlUr_35NoBiOtiujnk2TQ79weaGLOr8zuHy-5FIpC7QFi1DWykJ_01ThCw8vJFDg_RrZW_kVbOicbbHUmoS9Vjui-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=bpRsvREgQ-Yn2faM51wrP9sYzYIGkVSllaWQA_ygWYgXnd063eLpZ9db9gCTWU6OaaIfFgGdHLdp84YDNgJVupEwhDyqNhdUJZT-kho6fWwX3tLzzvYyKcxUUSfEGVR5cvVqrOOxLEW2K5C8LWZOi0kyuzET90ukzYIVRlqYzJMpH8-W7YOSmSR68o7wERrvMnYW5fmWVjP5M3ZN1_FcCmvRAwWYsAKXED2BJ6Vbe0mDJyQYq00yY1pFwpU1BkQeEtQ7k9a7fHS62zbnsC3BSLDPfbLLNdzBefWE0y5edYG8NzltI8vTX2Q0E_a2txMbaQ6wqEz2TM22ln-tfOyXNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=bpRsvREgQ-Yn2faM51wrP9sYzYIGkVSllaWQA_ygWYgXnd063eLpZ9db9gCTWU6OaaIfFgGdHLdp84YDNgJVupEwhDyqNhdUJZT-kho6fWwX3tLzzvYyKcxUUSfEGVR5cvVqrOOxLEW2K5C8LWZOi0kyuzET90ukzYIVRlqYzJMpH8-W7YOSmSR68o7wERrvMnYW5fmWVjP5M3ZN1_FcCmvRAwWYsAKXED2BJ6Vbe0mDJyQYq00yY1pFwpU1BkQeEtQ7k9a7fHS62zbnsC3BSLDPfbLLNdzBefWE0y5edYG8NzltI8vTX2Q0E_a2txMbaQ6wqEz2TM22ln-tfOyXNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipN7NWQgOki-lqsFc1U0GbH_MfEtdfsfi3tYKdEqY-eB9eDndpszk6btVF4GPnaiDT3RVH_8GKyF5Y0rw5vWTXpATLAK0ZPzQFCqLElJzX42zZI97M5t1S3ZA1CwpnzBT_4BMxidD0J7Tjs5q3tdxU8eUCUMlKs_zGej6BB5GxRjP82G7x0BmW1AyftE1NJd44nUS8V52rs-U0D6Uiu8pdbSMpFGpS8jgPmN5X6_c9Jg4NqB7VQ0IxWNzJpXakZYfs1JJRWVrlb6V5odWs8FcWdJ7a88b9dCjZajN6hNZgRFIAeKqQ9nO4E0CMxHFqRJlvhuxCB_mPpBTCbtJCBInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=pgGZlrbO4AjirQK3rQWgYsU0a6-oRENzyPbKRbOWyMeRBu-1HuigAguYo4pFU1B2ZVlVDSW8U2af5Q8NBU-nvIN_rq8U1_pgZUR0_6NOqXuV4BY6wgE3Z5xxPZrXmAeBbbdIgXtukEtlzVJsaOeLEwQAsSlQC61SSJYK9kUIF6HpVWPg_k35uDWvyuZcIQ4DIOgbOyCW24CcL8huzRMYFmaR8QSRq5uryAUpAjvccvpuqgXqxnZubD3vGnNrSy1RbDJNWm7ZKYYgND1yWpx4pPpuBJlRlbqUVfmyu49GoxXqcYzo0PvSLFlu9Gm5bLy1_qwpSFe-enx1YfSPGnjJdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=pgGZlrbO4AjirQK3rQWgYsU0a6-oRENzyPbKRbOWyMeRBu-1HuigAguYo4pFU1B2ZVlVDSW8U2af5Q8NBU-nvIN_rq8U1_pgZUR0_6NOqXuV4BY6wgE3Z5xxPZrXmAeBbbdIgXtukEtlzVJsaOeLEwQAsSlQC61SSJYK9kUIF6HpVWPg_k35uDWvyuZcIQ4DIOgbOyCW24CcL8huzRMYFmaR8QSRq5uryAUpAjvccvpuqgXqxnZubD3vGnNrSy1RbDJNWm7ZKYYgND1yWpx4pPpuBJlRlbqUVfmyu49GoxXqcYzo0PvSLFlu9Gm5bLy1_qwpSFe-enx1YfSPGnjJdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkkdINv54bv_V1K6NXlJ5D4he7IjrOVlmnUCgAqLf3ngvTLUW8x07oL0SJu40iwnrdToSMnUxaPGI6XOGSc0QfrMq43185QpvnsRCRJ2yKjEDrXpN7beYGPidEUflFOJ0FJRu0kRfkaHRJJmnxIiDE_Ld3Pk_V49YKSNVWcXjCltra-TfYsjdR4cQK5GSb6peuDWCVQPH1u3P6GbL7gTaDnn3XJsy9ZE4HdRv7Yx7HcMkw_7OoRJ_FsYursQJG23Oi0JvFfjK9c2OR-UbYp8w-oX2qT7zJq3tsP_kOFIrgaOT321VFjpU-9O-nktHZ0RVSoAFOfdMluDBmnQLTUxQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=a8WnwTj7Jj-bTZz0u_QMM_6oWr6bqwtYikYziT1V87NAHp2PE02d5LBCzUh5nx_Van4h9klsHKIgaq3eWZVR-VGmmWYAQggvfdBXMIxfB2qCLWrm4aDgSBBDvhTIXqJnlrUymygc5YXdQ-UaYTlDIj5WBFwiicsvfYRjDzW5P--GlnUPownxy8ln_GeNM4WGnf9ZkqoyCrDezNKVjfz0G9u11uKzJqOyl9X639G4D8YjIf4STNEalGUWxJftWJeuqdywOQZNlxDcbBR2gih1DjqX_GIMTrIuL4F5jx-O3GsdEAnD9jljlQjNahs4mNaunTdk_CBuSYx57-g1ht8CCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=a8WnwTj7Jj-bTZz0u_QMM_6oWr6bqwtYikYziT1V87NAHp2PE02d5LBCzUh5nx_Van4h9klsHKIgaq3eWZVR-VGmmWYAQggvfdBXMIxfB2qCLWrm4aDgSBBDvhTIXqJnlrUymygc5YXdQ-UaYTlDIj5WBFwiicsvfYRjDzW5P--GlnUPownxy8ln_GeNM4WGnf9ZkqoyCrDezNKVjfz0G9u11uKzJqOyl9X639G4D8YjIf4STNEalGUWxJftWJeuqdywOQZNlxDcbBR2gih1DjqX_GIMTrIuL4F5jx-O3GsdEAnD9jljlQjNahs4mNaunTdk_CBuSYx57-g1ht8CCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=q3rlmatYZBU7U-bOovC2lUsGEFt8uELRKtZDOmEk_Z52016gHEtg9IWTRRj1mTA5Xzb3RTXtPSArfMJUqxImBouSBNKCXGynfQS-afK_-zZFfV4vEP-A18Q3KLaSk6EZ9QvIq2l8xRlpygwhphlUFNyyy1HybGPJBDNVXlxYE54yJYQ6wh3c6XG4UQfbfFYAer1nVIyo57ycbAQaLVEzEwn0hB_P5sFmNYSJb72keWq6NC4Ui1PJ_vA7akt3Lo3EsxyNfefdoKpqr48rReWLPwCDGlTIfZNSSsv1XjjOAN3ZHEpcBd7vxjWASez6PbE8polSmK4p-ZV9cGOOsRHfFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=q3rlmatYZBU7U-bOovC2lUsGEFt8uELRKtZDOmEk_Z52016gHEtg9IWTRRj1mTA5Xzb3RTXtPSArfMJUqxImBouSBNKCXGynfQS-afK_-zZFfV4vEP-A18Q3KLaSk6EZ9QvIq2l8xRlpygwhphlUFNyyy1HybGPJBDNVXlxYE54yJYQ6wh3c6XG4UQfbfFYAer1nVIyo57ycbAQaLVEzEwn0hB_P5sFmNYSJb72keWq6NC4Ui1PJ_vA7akt3Lo3EsxyNfefdoKpqr48rReWLPwCDGlTIfZNSSsv1XjjOAN3ZHEpcBd7vxjWASez6PbE8polSmK4p-ZV9cGOOsRHfFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGy1vnSBf53rNXzOd9NH-RAzmQtPqfd3YvXxNoqVVJlTR_Bwfkw5z_VAJD68BIfZeedWQlcglCRHViQGX5xszoj0WS5PnShDwHsVPqfSOaxbqqzUZIfMiy6UbJw17oVn7dt4d2qRFDrb1F-9l2FJH_MvqwdiuMkYsbZilBIWuDO9r2MiqSakS0eNvfsNOdisk-0k692f8XXcs3Na4zgbjyJgoeSR1c5qNjYXqPmmsw_qQB5M2uYk8LMpnwAt4soaSeRh2tgnk-WMJ1hoacH1UhoWF6J_gYiOhBJs-TuPdapfcfktXcGRkKTYA0govqULrUFX6r252srZBl6XxPw8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=Xe1uvQCrkPlHMXQHJDxlu41dCOKAV733GnmIikH1QX4Fc0J-ebP2fIur4yZkpoLrZH1yAzjYeu-4443KEaT3ZNrWnYmTU0dL7ORoe9A8poMdbL9H5FMF8zX45WMbMXj33PfcX8bqx0SNBc-Fg7ihlTezkb32mevpGa1U7tvg_BN9rS39bWsjCtLagoAuaZrDKMla3jrSStJyl8G2VH9HwTqFVWl0CaLXDQF8vk95pPjbC7tO4Fwsw62qqMRtDrrDWOA3PyyemuHVfXjgStXDQscBojn8cX3IXEX18tkN5De3Uw1vNI21f7AUDE-iJtgDQE0_0fXnvXRigdRY0LM5HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=Xe1uvQCrkPlHMXQHJDxlu41dCOKAV733GnmIikH1QX4Fc0J-ebP2fIur4yZkpoLrZH1yAzjYeu-4443KEaT3ZNrWnYmTU0dL7ORoe9A8poMdbL9H5FMF8zX45WMbMXj33PfcX8bqx0SNBc-Fg7ihlTezkb32mevpGa1U7tvg_BN9rS39bWsjCtLagoAuaZrDKMla3jrSStJyl8G2VH9HwTqFVWl0CaLXDQF8vk95pPjbC7tO4Fwsw62qqMRtDrrDWOA3PyyemuHVfXjgStXDQscBojn8cX3IXEX18tkN5De3Uw1vNI21f7AUDE-iJtgDQE0_0fXnvXRigdRY0LM5HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZQg5s33WKlrpJ6r8XbkFCAl_t-DPX4kucmSFUXx7p0hKMVHHZvquR78dHRM2YyHimGuuuCgJK7Xcf9fgNahvX3Z8buwqHiq9Hbrq4klB5DRJbh9NQgfVn6J_4IjfmAJYO2VC261FiUbt9HPhtx2BojCSu0IZ7rpojDTN4W_ajU82jj0dl_itbfhrf1cwxkKBMtRxCRPzNEteg2XzIdQH5yxq13HuHdeVZtL2leun2FfKUMKEoKJKBQcShU_7x6_1OeI7vbDSDz0zT-M1h8puTeXo88BG3uWbjOfVwx4LLrvjZ30nFVPNNxYWc_zmUiFHmSQUKNW-g3OZCxwibCCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=Es7hHm2sVElX2fdIxMghjybJ-sHCN2pYnSfKGGIrIAeMfc3a2EHym7esiVghHlu7min_IbHetw_2k0q6ZkI91ZJCHlM9yXTkv1qgSATW0NM-GUkVqbflONsZS6_DdOoC33ZEoBNPv7msz1VTczPNwZVVtRzj7OJQyEtlUw8kZfz4AbCMylHAVkG0cueoHrPqaOFjE9a82C5LUqG5L5YQcS70ZAhdXOw4wuTT3_Wt9PaCbjMxGk0VkGQfXGNOVZoSn0D2Fz7sr-GZ1RBZDspwMIlw5T9vA7_6d6PaqOqAvXBDD_S_PPH1YMDYH3e_OT7iaD1kIbvcZb8gfXN5Vw_rBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=Es7hHm2sVElX2fdIxMghjybJ-sHCN2pYnSfKGGIrIAeMfc3a2EHym7esiVghHlu7min_IbHetw_2k0q6ZkI91ZJCHlM9yXTkv1qgSATW0NM-GUkVqbflONsZS6_DdOoC33ZEoBNPv7msz1VTczPNwZVVtRzj7OJQyEtlUw8kZfz4AbCMylHAVkG0cueoHrPqaOFjE9a82C5LUqG5L5YQcS70ZAhdXOw4wuTT3_Wt9PaCbjMxGk0VkGQfXGNOVZoSn0D2Fz7sr-GZ1RBZDspwMIlw5T9vA7_6d6PaqOqAvXBDD_S_PPH1YMDYH3e_OT7iaD1kIbvcZb8gfXN5Vw_rBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=Lvhb09Rsf7bVgkIlGWFM0hg3vk3qlKvQ_YYuYovC6K6BbwRrRiV6xMaTT3JXQGCUNKWflWJi6GM7oGH75n75qxcAYXz52PSog0D7usVVq-BJpIHhOpaUtd4LkSZxG_6Y1drvCOIK7s8oyiGkrQ8x7MixwLGTPlyrES9wqehW_tm_ThyKt1IQ2cR9jpEnys4obVoYDeLiQrqUj2aP0oSZjuCHNeQqYY4xRq3wqA1LcQrDSvPXzrRCQSxIm1qtQzz7NL3I0mJrzoYAe8R0aykl9zlQAMIh_qsHklKVNDnB3Yz3DFAlDrUDt0-S0er3jpumccg0cG_-P8XEUFYyvKt7Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=Lvhb09Rsf7bVgkIlGWFM0hg3vk3qlKvQ_YYuYovC6K6BbwRrRiV6xMaTT3JXQGCUNKWflWJi6GM7oGH75n75qxcAYXz52PSog0D7usVVq-BJpIHhOpaUtd4LkSZxG_6Y1drvCOIK7s8oyiGkrQ8x7MixwLGTPlyrES9wqehW_tm_ThyKt1IQ2cR9jpEnys4obVoYDeLiQrqUj2aP0oSZjuCHNeQqYY4xRq3wqA1LcQrDSvPXzrRCQSxIm1qtQzz7NL3I0mJrzoYAe8R0aykl9zlQAMIh_qsHklKVNDnB3Yz3DFAlDrUDt0-S0er3jpumccg0cG_-P8XEUFYyvKt7Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=OnCzo298XiUIAO2B2fxNMqCByhkIooy-9_X1iF_ODocMop3OfA7qddTjxJtDxp7nTKOvML-rOOL3-OOAyhfj1FPqpHD2HQRvmbDerykhPoxEUI4RVSybd47AY_7aLNNGYw3gO98iorpUUnRouD8f0dt1aN3WAx8CfoH9vc_u8kxW3905ZQSt8GFcoVmnOSfbmwUs0fJae8UdoWZJk_Fmr6QjwX6yu4U3aY1aIZDcGed31y_Y6nLJUmA-eKXHBtVrBtiurHXBOlffeb3_0Yt2qk7RQCE0iXJmEWiu426UIU7NsL5qQ1VEunDJUVHJKSoqs5smPFxExFxX621sMDhzLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=OnCzo298XiUIAO2B2fxNMqCByhkIooy-9_X1iF_ODocMop3OfA7qddTjxJtDxp7nTKOvML-rOOL3-OOAyhfj1FPqpHD2HQRvmbDerykhPoxEUI4RVSybd47AY_7aLNNGYw3gO98iorpUUnRouD8f0dt1aN3WAx8CfoH9vc_u8kxW3905ZQSt8GFcoVmnOSfbmwUs0fJae8UdoWZJk_Fmr6QjwX6yu4U3aY1aIZDcGed31y_Y6nLJUmA-eKXHBtVrBtiurHXBOlffeb3_0Yt2qk7RQCE0iXJmEWiu426UIU7NsL5qQ1VEunDJUVHJKSoqs5smPFxExFxX621sMDhzLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=dyLCyxm9d90TrmB7LjrMKuSH05a8_xUhYh1eg8HAF1saDqT4XeQIQA7IPnAPacv-wHLLsm_dsByl6SO36WDNWM2r2NS9R5oG7uE7tFXhT6bfmZD6Noy-ELJRH9naNuPsFdXnfxb-uaQMopBxzwIRrxXfb4P6BR0GmLFfXpmIEQlWnksJdpnwI6ewnmYQmjcPkHYqIUO_FrOpKg4H_dIGcuJmrjzkQHqxq9kYNbnqhMph23lEdozCRUpYP31_lHPRDvqBKOJowlbPFgkClOPmr5v6sN5NAYwUKEZJ51JApREa3LQsQCF7v10ssrx7rUoCckJo_PEtZLThwl-ImJj5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=dyLCyxm9d90TrmB7LjrMKuSH05a8_xUhYh1eg8HAF1saDqT4XeQIQA7IPnAPacv-wHLLsm_dsByl6SO36WDNWM2r2NS9R5oG7uE7tFXhT6bfmZD6Noy-ELJRH9naNuPsFdXnfxb-uaQMopBxzwIRrxXfb4P6BR0GmLFfXpmIEQlWnksJdpnwI6ewnmYQmjcPkHYqIUO_FrOpKg4H_dIGcuJmrjzkQHqxq9kYNbnqhMph23lEdozCRUpYP31_lHPRDvqBKOJowlbPFgkClOPmr5v6sN5NAYwUKEZJ51JApREa3LQsQCF7v10ssrx7rUoCckJo_PEtZLThwl-ImJj5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
