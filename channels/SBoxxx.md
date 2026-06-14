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
<img src="https://cdn4.telesco.pe/file/SPa-D5OLL57pYtgNAoE0dESiATPbMYya3OqxespyHE4XzJlUsEK-sH8czMmMw4W-GakefxqIK0almOXC_LXvDbFFDbyX7H3qoK1thKfnjyLGwvYs4HZqk641-L2xFn9zYaBleOp3vzNbtDnOD3kLBjxwNr3OIL6wy84xGAOc_bm1OjTshqMhRtxyQdvIY9IOhT18bg6g-RJhIteMDugP13EqFyhnFI-EbCWzSyeP7DpHxTrtNIAEC8aNj3d-yO7alMtdWjiS8jekBqs1kHSrlbmjQ-asDdyiN0a6dkPfUZUkPDbrLTCRN085xjHXsL_k9tAZKC5tSOck9SBptoVFlA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 15:50:01</div>
<hr>

<div class="tg-post" id="msg-17514">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تلویزیون ایران به نقل از مسئول سازمان مدیریت تنگه هرمز در خلیج فارس: تنگه هرمز تا اطلاع ثانوی بسته است و اجازه ورود یا خروج به هیچ کشتی خارجی داده نمی‌شود</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SBoxxx/17514" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17513">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیم ساعت پس از حمله در بیروت، گزارش شده که یک عملیات هدفمند دیگر انجام شده و این بار در شهر صور</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SBoxxx/17513" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17512">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/17512" target="_blank">📅 14:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17511">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/17511" target="_blank">📅 14:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17510">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=hfExn4gxD3LFqBJdslPLlq6hB0Fqv4e6s50bTjv__AyIb2ryYy97GTCJ5LGU2warwV11BSF-TlyAhCFbNPH-VlnPMuhgEO3IPpMrYvNGxHgWeXAVaKkMzMivqLbJEp3HBRyfXvspKdyo4tPMYlIbtEk5dSxx95Mi9-U2K6DcRYRSlECW4FbjsFmaGVqk6KhryBAsq6a_WluhhUqVn0ScVoptupCfiOg4PpFOjsJppZ_MDQRSi4vQbjKWO-ScNnCWv9wbVEklQ3FZT00_G1bm8wfr2upg-r-JCkGl0INGgqn2GQyOdFXPI4Lh1pIGHsXbiyAoV_Xfw9TjG-_bCGJ5SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=hfExn4gxD3LFqBJdslPLlq6hB0Fqv4e6s50bTjv__AyIb2ryYy97GTCJ5LGU2warwV11BSF-TlyAhCFbNPH-VlnPMuhgEO3IPpMrYvNGxHgWeXAVaKkMzMivqLbJEp3HBRyfXvspKdyo4tPMYlIbtEk5dSxx95Mi9-U2K6DcRYRSlECW4FbjsFmaGVqk6KhryBAsq6a_WluhhUqVn0ScVoptupCfiOg4PpFOjsJppZ_MDQRSi4vQbjKWO-ScNnCWv9wbVEklQ3FZT00_G1bm8wfr2upg-r-JCkGl0INGgqn2GQyOdFXPI4Lh1pIGHsXbiyAoV_Xfw9TjG-_bCGJ5SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/17510" target="_blank">📅 14:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17509">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/864badacb8.mp4?token=sWWOal4LRhlZU7edbR9E0VmLAGwWer3V6wwr0AG_acNCQyB49wimz2jVimHiEmbFMX--V9dbW2UlT342rcs_5GzRMQLHCwWNnWIBoB9Oz5e00C_4fIr_4nh-f_G1TuYZa4u7592sOUKDUr9WWB6WQX3rDbB8dqjLJfUy0udRNKpLNbs9hABI3Fju95JJL27S8HqQlqfg8QwUopP0g22VBf5PvCyNy3KZRIr_xgKn6B3Nm2T2Yyz4CJDhNo3LnH7AJVtk-CWBMTTcbsv-C3PEB2bSq676CjF4QYOwd6MmeArC9wJbTwUxWheYNvDs4Zt9gdMekDbLtjZStD__EKWtbFNWJZBGjHFFjJYPnji9niT8EZ-gFnGA9KiPhDWXnOEdqaBo98fDpIeiS2DvFVPyTgdZK-2IEKWq5BM2Rm0f4j2yx3tBAuR-kXSyKQxL3uDuep2_dBvOJ4iMuOGHU-18Mf8nlw-MPSoSZcEOnYYm5VXET_dYh6FSk27A2Q28o1Faru8mxcS2FjwonL5uA3cV5TsHfq28ezbVoON0OxTtggXDdmck9JPISi78Xpgfsv4yC5EDhZzn8Y8RVq_5DUtWkc56l3PJ8aVx8m7-fLO-i4Ju0JPD-PfF0VTBZ6DiLYFg5OcT4049tl6EU0CxWAa0DHY_gGCZbFkyWeJnxLSSqaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/864badacb8.mp4?token=sWWOal4LRhlZU7edbR9E0VmLAGwWer3V6wwr0AG_acNCQyB49wimz2jVimHiEmbFMX--V9dbW2UlT342rcs_5GzRMQLHCwWNnWIBoB9Oz5e00C_4fIr_4nh-f_G1TuYZa4u7592sOUKDUr9WWB6WQX3rDbB8dqjLJfUy0udRNKpLNbs9hABI3Fju95JJL27S8HqQlqfg8QwUopP0g22VBf5PvCyNy3KZRIr_xgKn6B3Nm2T2Yyz4CJDhNo3LnH7AJVtk-CWBMTTcbsv-C3PEB2bSq676CjF4QYOwd6MmeArC9wJbTwUxWheYNvDs4Zt9gdMekDbLtjZStD__EKWtbFNWJZBGjHFFjJYPnji9niT8EZ-gFnGA9KiPhDWXnOEdqaBo98fDpIeiS2DvFVPyTgdZK-2IEKWq5BM2Rm0f4j2yx3tBAuR-kXSyKQxL3uDuep2_dBvOJ4iMuOGHU-18Mf8nlw-MPSoSZcEOnYYm5VXET_dYh6FSk27A2Q28o1Faru8mxcS2FjwonL5uA3cV5TsHfq28ezbVoON0OxTtggXDdmck9JPISi78Xpgfsv4yC5EDhZzn8Y8RVq_5DUtWkc56l3PJ8aVx8m7-fLO-i4Ju0JPD-PfF0VTBZ6DiLYFg5OcT4049tl6EU0CxWAa0DHY_gGCZbFkyWeJnxLSSqaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی اسرائیلی ها از لحظه حمله به ساختمانی که ادعا می کنند ستاد برنامه ریزی عملیاتی حزب الله بوده است</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/17509" target="_blank">📅 14:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17508">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/17508" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17507">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :
ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/17507" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17506">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/17506" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17505">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">العربی الجدید: تهران توافق را تأیید نکرده!
در پی سفر امروز هیئتی قطری به تهران برای گفت‌وگو در مورد یادداشت تفاهم، رسانه قطری العربی الجدید ادعا کرده که
ایران همچنان ملاحظاتی در مورد این متن یادداشت تفاهم دارد و هنوز تأیید نهایی خود را برای این توافق اعلام نکرده است.
العربی الجدید به نقل از یک منبع آگاه ایرانی نوشت که این منبع ا
حتمال امضای توافق در روز یکشنبه را منتفی دانسته
و تصریح کرده که همچنان گفت‌وگوها در مورد توافق در داخل ایران ادامه دارد و
موضوع به صورت کامل حل و فصل نشده است.
این منبع در عین حال تأکید کرده که ممکن است امروز توافق نهایی شود و تهران امروز تأیید نهایی خود را اعلام کند.</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/17505" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17504">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اگر نتانیاهو بخواهد تسلیم این توافق بشود (با این فرض که اساساً چنین توافقی وجود داشته باشد و امضا بشود یکشنبه)، عملاً سند مرگ سیاسی خود را امضاء کرد و سپس باید ریسک دادگاهی شدن و زندان را هم بپذیرد.  اما میدانید که نتانیاهو سرسخت و سمج است و بعید است به چنین…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/17504" target="_blank">📅 14:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17503">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsAlyuvBXj2JhtxMe_ghMwlGgPnsVlbX2xD1M6C0QeeBe4lIViE026lVgs_tDtv3CNE-lwAt1defUDpu1FWlf1FJPa5KhFusFc6Xo1xKATG9PBaVUicilgkZ4301ck4wsxUzW3SHS8uDS1l9Y9o1IWdSWIx4LJv5WH6sAVUIl-2e54TXioRHa5tM2vSs5NSF_rFpUooFR8yD--wSkUVhXpYEwsLlLZft6C8oP6LGItd2Werpp74VOud3SNM2T8bNfS_UVLZf83XEzAguaBHhCtFetU2bWyzr6LWx4vrSop92zZCZud1IaF57KmbjDr1pyCN35nTCbbBqkn939Q_JvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/17503" target="_blank">📅 14:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17502">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/17502" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17501">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1668556cde.mp4?token=G8v_vjHYCWBcOWEmihkYzonraM8ot9eOtGL4lqaJ_5-Uzb2yiZUlqYgQffpQ7oPOh8vN5Zq-mfC1-tyEkTUGaY7MZEh-2Jppk7Ct2di6Ec_TishblXXk5XwLBBcjUsiUU1of0PWeOX1f3M_RJqYaOhj24zPA58kvo9L0IryE6DovDTTkEpoZG2S9gwMf34BeTKyAKHKMCBfvfjadyoY3s8GDLHj7h_g-vio_MLuIRi9cH5pPhHxRlPNY4srOVh-eADbsrV9fCwaxTIT0M6FM3iSWzxnce3AhaYE1_9F7ZzO3j2B0naHjT-4v9mMaUF207FAm3Z_XGivpMCmr3y_NUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1668556cde.mp4?token=G8v_vjHYCWBcOWEmihkYzonraM8ot9eOtGL4lqaJ_5-Uzb2yiZUlqYgQffpQ7oPOh8vN5Zq-mfC1-tyEkTUGaY7MZEh-2Jppk7Ct2di6Ec_TishblXXk5XwLBBcjUsiUU1of0PWeOX1f3M_RJqYaOhj24zPA58kvo9L0IryE6DovDTTkEpoZG2S9gwMf34BeTKyAKHKMCBfvfjadyoY3s8GDLHj7h_g-vio_MLuIRi9cH5pPhHxRlPNY4srOVh-eADbsrV9fCwaxTIT0M6FM3iSWzxnce3AhaYE1_9F7ZzO3j2B0naHjT-4v9mMaUF207FAm3Z_XGivpMCmr3y_NUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوبی است.  باید تدریجاً هرات از هر جهت در بوم ایران ادغام بشود.  چرا وقتی نظم مسلط فروپاشیده و همه دنبال گسترش مرزهای خود هستند ما بنشینیم و به مرزهای جعلی استعمارساخته احترام بگذاریم؟!  هرات؛ نگینی بود که توسط ناصرالدین شاه حمال از دست رفت و هیچ قرابتی…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/17501" target="_blank">📅 13:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17500">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV5jAQsJMAzK7FKWlUHhvFkDskl5iMrvfUePvgb8tzZGvIkXG0CxhAijMldRwvVxHt6maWHSqDK3eEewzv1Jd2nEeRrr-0RqXec9ILbHy_rSQS_BXRGWLM-5OJf5BrAxGLEJbRPJdljLQkHEC4ncdtOcPjukxlKHbHc-eRbs_ebdfmIBri6BIEge3omYh0bLjLGfqJEJeM15jKkJoJWRJu6-5hvG3fKbUdSpXDMuW8-yMmeeByjTrzaKcwe7l84K2lxty5mA7KvQ3FsPBByJILD9kgfaIYDWr_RSCQWBuImu3HJj9yMsUvh2oPBSwClm1RJFgC81vFNDSWpglWZv7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز هشتادمین زادروز این نکبت است.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/17500" target="_blank">📅 11:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17499">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5xolQFDvTwvdiU6YkqsIJASrs4ON94gXmzydlwr43mX5IZy6gynCZpwHDJPpYW434I72yRlTA0zgk1_mAryZn1VzMJdSE5TCmNB5DfAABtfcZV-lGiTwTvsM3FeYTuTYccjCGd2wOUo6lXusYPC20YjZQrj9dGFzjorNxPwvqU_eVn_Hzy2P2Zb8DMdkFD4en_HRKck9zXEgUZxzwIjYdkeMMaVGrAqqOWnUCiT9Yu5AlS4nsH0O5crFsSleKF_-CIJLYKmkuZ73pF-dc4BkBHAhcG9S4XkqJ8GsMdLHKdhlAaAwPxEpsPGCFOVSN6ga4soXKyJGzVunYdNwqzb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنا به گفته دو منبع آگاه که با شبکه CNN گفت‌وگو کرده‌اند، عالی‌ترین فرمانده نظامی ایالات متحده اواخر ماه گذشته سفری محرمانه و فوری به مقر فرماندهی مرکزی آمریکا (سنتکام) در فلوریدا انجام داد تا به‌صورت حضوری در جریان طرح‌های ارتش آمریکا برای اعزام نیروهای زمینی به ایران و تصرف اورانیوم با غنای بالای این کشور قرار گیرد؛ ماده‌ای که مؤلفه اصلی و ضروری برای تولید یک سلاح هسته‌ای محسوب می‌شود.
این منابع گفتند جلسات توجیهی آن‌قدر فوری و حساس بودند که ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، ناچار شد در ۱۹ مه نشست مقام‌های ارشد ناتو در بروکسل را ترک کرده و به سرعت از آن سوی اقیانوس اطلس به تامپا در ایالت فلوریدا بازگردد. به گفته منابع، سطح بالای این جلسات و فوریت آن‌ها نشان می‌دهد که دولت آمریکا تا چه اندازه به صدور مجوز برای این عملیات زمینی پرخطر نزدیک شده بود.
سخنگوی ستاد مشترک ارتش از اظهار نظر درباره تدارکات مربوط به یک عملیات احتمالی خودداری کرد.
یکی از منابع نیز گفت که ژنرال کین پس از آن، رئیس‌جمهور دونالد ترامپ را در جریان گزینه‌های موجود برای انجام چنین عملیاتی قرار داد.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/17499" target="_blank">📅 10:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17498">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تحلیل من همین است که ۳ هفته پیش ارائه شد و امشب یا فردا یک صوتی هم در این کانال قرار داده می شود.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17498" target="_blank">📅 09:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17497">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrVzNsGF9DYPeAuTCD8V0LAXO-Nf24jPpEfQqI5VB3q7x-R4gyrdMFaE-z8YZ17VbXcuH9kuU0FVXS6E_7auLFYc1buSh1p81ftQGGMLfjULJHRjcRPY643GRBMWA-bTGEoRgGDg7N85kWLCh_sIHtRTlm0tjGivJJlwxOXuCIsvLXWxg_gVrHLwvpX8otXkvo5teY7tp7enmBd1HoXIay1fOrOJxWSa-Bx4o7KQ3tTGqpfT9kaNBFrTKLoENiLbJ9epP6hfge9gJAx9t0mLaIhABiZCM5AEV1KT-OaGEJsoul-g0VVMpqN3b9bddt69N3vKdgzsb7KYi-98BSkJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک رادار آمریکایی در بحرین بعد از حمله موشکی-پهپادی سپاه چند روز پیش</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17497" target="_blank">📅 01:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17496">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خدایا درگیری جانفدایان کف خیابان با جان برکفان ناجا را هم دیدیدم اما قهرمانی .... را نه!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17496" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17495">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ایران تمام دارایی‌های اقتصادی مدیریت شده توسط ایلان ماسک را به لیست هدف خود اضافه کرده است و شرکت‌های ماسک را متهم می‌کند که در حملات دیروز ایالات متحده علیه ایران کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17495" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17494">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwIGjLTefaBj-KDLC7SBtIyTo3jIxMkYHTJoJyyFRFYEQzMLZ5uv6HkG9g6ZherRi4XuUR5VMTcJHMmLBtN48yYVJZcWHgboxMxR7pmRC-n2HTH07MNXakUz4dZqft0yETzToN5Ik4wCcs8tq0DC54W-ShoEnuxRdSrg1Ym8jNZkhrHdpVqRuJAwrsYseykbyF-SznhHRqrOHingM0LmrSQWN8SVL_SiOhrnELNynZ5Oea71mhOaGiTyYH5MnR8cW1Y3z192Cc9JXdrEAClN82M1dfGKj-mIVcmQ0Qc56iJxJl8PSwJPwNfGznmBMEdsnRhbyD8ScSn1vEfvTA4bOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا همه دارند به تنظیمات کارخانه برمیگردند!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17494" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17493">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugDXjEZHUWrUrwPD7QnijDh-mnINI-xy2Dnq5yq2msVoMfueZykgFkId4EnBcGb-LoghI4CRhsnVuMDnXu78nvJsrWaSvmuSaDwrLhFWC-4lJb-O2Vv98mbWgxYkIStlsGVPy6nt-UdiuMY4ceZLVIEYJwrZckh0oJerYj-dpYFE6VhdoMeb7iMT6up5JfaUtoG1W415u1zoZ7_gDXXF84D-oPt5OyQTpnDTgD3cZp7ef_1poR1EQmKQ-QgLTasC5lmZnF0bn8HrKYl3LVsmEekJGFbRkD0Z6UAPJaxsgYXqtGGr5HUcrtJ_87jlfWC5pEm7a0tvQULMQgay_U6v6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!  فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/17493" target="_blank">📅 23:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17491">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17491" target="_blank">📅 23:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17490">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!
فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17490" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17489">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/17489" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17488">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/17488" target="_blank">📅 22:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17487">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:  "هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/17487" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17486">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:
"هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/17486" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17485">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شرایط جدیدتر اینطوری است که ما کشتی های هندی را که از ابتدای تنگه هرمز  می خواهند عبور می کنند میزنیم. در پاسخ، آمریکایی ها هم کشتی های هندی را می زنند که از انتهای تنگه هرمز به سمت دریای عمان می خواهند عبور کنند. ِ  این وسط، گاهی کشتی های غیرهندی هم هدف قرار…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17485" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17484">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خیلی جالب است؛
ترامپ می‌گوید نه پولی می‌دهند نه عوارضی از تنگه هرمز اجازه می‌دهند و بعدا اورانیوم غنی شده را هم خواهندبرد یا نابود خواهندکرد
مقامات  ما میگویند هم پول میگیریم هم مدیریت تنگه هرمز با ماست و هم بحث هسته ای الان مطرح نیست!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/17484" target="_blank">📅 21:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17483">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17483" target="_blank">📅 21:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17482">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">منطقی هم هست؛ امضای الکترونیکی که دیگر حضور فیزیکی لازم ندارد.   بوگندوهای فاکستانی فقط دارند می روند شام مجانی بخورند لابد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17482" target="_blank">📅 21:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17481">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فوری | ترامپ:
ما امیدواریم که عملیات به راحتی و به سرعت پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مجبور به استفاده از آن نشویم.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17481" target="_blank">📅 21:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17480">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حالا که همه چیز را دادید رفت، دستکم به رستم تهمتن بگویید دیگر نزند!
کور شد بدبخت!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17480" target="_blank">📅 20:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17479">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17479" target="_blank">📅 20:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17478">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ:
«توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.
امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد شد».</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17478" target="_blank">📅 20:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17477">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17477" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17476">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17476" target="_blank">📅 19:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17475">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنگوی وزارت خارجه: باید هزینۀ خدماتی که در تنگۀ هرمز ارائه می‌شود را دریافت کنیم!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17475" target="_blank">📅 19:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17474">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">این طرح واقعاً بامزه است.  کشتی ها باید هزینه «امنیتی» برای دریانوردی در تنگه هرمز پرداخت کنند تا نیروی دریایی سپاه پاسداران از آنها در برابر حملات نیروی دریایی سپاه پاسداران مراقبت کند.  سبحان الله!</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17474" target="_blank">📅 18:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17473">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزارت امور خارجه ایران:  «تیم مذاکره‌کننده ما برنامه‌ای برای سفر به ژنو یا هر مکان دیگری در دو روز آینده ندارد».</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17473" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17472">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17472" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17471">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17471" target="_blank">📅 18:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17470">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17470" target="_blank">📅 18:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17469">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCtAjeTBTV6aUjXjtRHqsMcJcfCzObhRBDU-qDFqPIISlkDN9dpEc1rXMWFbVD5QiI7wZL6J4hKdTzLDk8GLXZm3sniHMssIolzTI7uXpE7RqytPIk6Bp-ERyDap3ebFQZNpxnnObMY6Dn1_AmBCQSNd-4o8lsANiRiaM5-YKgvxiNN822sys2EHd-VBZvVRTmQ-_jpH1Tk_YwhhCW1j6UHEAvNfaHZyepynAfbX0Kbgh-Fs9F1es0X5aCwQ72LvCtH1Cy88bgsiq3sY2-PGkYXpqcd9bE24CMZGGMomIev0fBMvLFGEHkSo776DNS_c_y1Q_gnn8FxZzLLe9xazrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله! جانفدایان یک پویش توییتری راه انداخته اند با هشتگ نمیپذیرم!
که اشاره دارد به برائت از ائتلاف قالیباف-ویتکاف!</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17469" target="_blank">📅 18:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17468">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گویا یک ستون از ارتش اسراییل نیز به سمت صور در حرکت است.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/17468" target="_blank">📅 18:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17467">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17467" target="_blank">📅 18:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17466">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xvhm9aFk9bBGngiICspbiemDR0E1NmuxPWP5Hl1G-gGuoSsCwDKgnnE_A0N7gTjHUU17i6mr7VfTOIukMwtmFM4XmLARkvkV3JpgYGzCPMncSjvGcsEYQC4-3vSa1156Tx-nen15ETkEkr-Po95dGwaIWS0UP1O6ORA-gxHFIyE0LDi05dEuO5CBCnwLe6bFeLv6Z0RbV4f4wc6BrT7cdLwvXhEULW5esO4Frz33nvDGdAWQDb2ai_Bc85jo7FG8cRFygAt3udYKIVy5v6THj18AlBBQ1FfDqh0Qbi7cwwTnh--W0cWzleQWZhyE6X6SAwsKoBF7H7AHSrsupw48cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت را دوباره بخوانید:  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  پس در واقع تنگه هرمز برای همه باز است جز خودمان؟!  سبحان الله این که عکس چیزی بود که میخواستیم!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17466" target="_blank">📅 18:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17465">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17465" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17464">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xssv1QytxU43gMIwMNQuxvbIN-Q-wcQ0AvFToS5vhTESrwSFeczbftBQGXKG6ss8cAAZILtVcpdsJs_UlqxOaEaxYS2k6I20Z-9eK-00Sj3n2SWH_pgUf5f1xA4y3wXa_EmQSX4pQXU5d-B-1SIkOZOLO37qJthUm-AHi5MiP1JeheTlW679AXLuqsO1O8Sk7nHDSoI6axpskEFmIdyjOyav_EZrSrxEbZZawWL3rLCzoXEta5VuTcMkzY4rCIKDzvE_FoJtO6DC_sSvKwVA1fezgRhZb8amo33z3qgxVxqFHos6eEbhXf3MCDWcKG3qgNpmnVrmq-QUturR9tnEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه جنگنده اروپایی (FCAS) در آستانه فروپاشی!  پروژه سیستم جنگ هوایی آینده (FCAS)، که با هدف ساخت جنگنده نسل ششم اروپا و با همکاری فرانسه، آلمان و اسپانیا راه‌اندازی شد، اکنون در آستانه فروپاشی قرار دارد. این پروژه، که در سال ۲۰۱۷ توسط امانوئل مکرون و آنگلا…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17464" target="_blank">📅 15:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17463">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">13 و 14 تیر: وداع در مصلای امام خمینی.
15 تیر: مراسم تشییع در تهران.
16 تیر: مراسم تشییع در قم.
18 تیر: تشییع در مشهد و تدفین در حرم امام رضا.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17463" target="_blank">📅 15:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17462">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SceWw8NqMLTz2J7aGECtxFy3PZcfeKiZgLdSnc-m2-vKFlIJAK6FAvzNrQVA2a6K7iffm3M8uLZwk-e_f-dTaxAPqaAsG3dZw2-M2c1soEBWXRqx-Di4b0LccSTg4E0YxM86uUlBhrGFBF-gplEnW_QV5rxsWc42G8SQql9gJBP9OL8t3bAfVBGzLLWn3RQc3A379-RgEYGuKKXIWIIJCXNqbd9lIL0hwbbkgzF5jE9jMYGPd2Q_X-bAWRk6RETLeXF--CHDMM7jmVqmdnV6_RzdSHTPaypSWNuo8XX3gHorUtZVFAORej2k27eyHzGxsCR-eUF7QKoVUOrcas81hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در جنوب تنگه هرمز هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17462" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17461">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صحبت های جاناتان پولارد — جاسوس معروف اسرائیلی که در آمریکا دستگیر و 30 سال زندانی شد — درباره جنگ بعدی اسرائیل با ترکیه و مصر و لزوم استفاده از سلاح های نامتعارف کشتار جمعی.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17461" target="_blank">📅 14:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17460">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=cdOwmN-iq4VwX025V-GKiKOALhqRCatE_O0KQRpONJ2YY8BRQkgf6bdlDhOP6YD_svkGjWfBtGIi9vC5loTU5KB6hKRu6TCk6q2jR1DhW1bj1faZ8mrZUqeIEeQ7IDBdstiC67YgxQNJb2ayJN6ARfB3VFgeb9HZ1s3m5Yhq_ZMHe7nB38npf9tFWA5g4dFm9PfsXPgPJrymgroKMO66xX08PKbuhK8qLNwjX0HLQuuIcCiDBLTsG3vRtt3nuKAsCrwqz74F4eNt7KCpFMQkNtOTeZHpIlOyXvjX05deg9BfXXr5xA7k48vLvYbqvgxtXducvyh0sj7ailqxFsijZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=cdOwmN-iq4VwX025V-GKiKOALhqRCatE_O0KQRpONJ2YY8BRQkgf6bdlDhOP6YD_svkGjWfBtGIi9vC5loTU5KB6hKRu6TCk6q2jR1DhW1bj1faZ8mrZUqeIEeQ7IDBdstiC67YgxQNJb2ayJN6ARfB3VFgeb9HZ1s3m5Yhq_ZMHe7nB38npf9tFWA5g4dFm9PfsXPgPJrymgroKMO66xX08PKbuhK8qLNwjX0HLQuuIcCiDBLTsG3vRtt3nuKAsCrwqz74F4eNt7KCpFMQkNtOTeZHpIlOyXvjX05deg9BfXXr5xA7k48vLvYbqvgxtXducvyh0sj7ailqxFsijZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17460" target="_blank">📅 14:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17459">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17459" target="_blank">📅 13:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17458">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صلح دوست ترین ارتش دنیا را لبنان دارد.  به محض نزدیک شدن جنگ، مرزها را ترک می‌کند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17458" target="_blank">📅 13:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17457">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfCoG_6Yk1ALdcM3TAGj5WYg1iUMvPECL7R-1EfF-h5rfwPYZELZaiX1tHZvOE6PClsRSK0cLXzbeas2j7rlBiXUrDFlZX_k4P3V00dxMMVfpDQAhA5oND71z_9C08gO29e3YhT6c3pvauGzTjsw1_qX5aP66y76T7viGglvybUX-bfcF7DyCeZP0RnW5VouXI7CTrxyHWLnkDaKN7hdMM6lqHMlt5ucnSu8O54f0FlZzX2lJsGMHXggiZAvfj6SjRS52OkffWhLE2qdywT1hrN-dJGPk5V38v-8uM276qO-LQkSygFTdEqEQGYCs46Glu69AK6rGK4mF0BXTeqNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17457" target="_blank">📅 13:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17456">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خدمات الکترونیکی در چهار بانک بزرگ ایران — بانک ملی ایران، بانک تجارت، بانک صادرات ایران و بانک توسعه صادرات ایران — از صبح امروز مختل شده است و این اختلال بر بانکداری موبایلی، بانکداری آنلاین، خودپردازها، پرداخت‌های کارت و سایر خدمات بانکی تأثیر گذاشته است.
گزارش‌ها حاکی از آن است که این اختلال ممکن است نتیجه یک حمله سایبری باشد، اگرچه مقامات ایرانی هنوز علت را تأیید نکرده‌اند.
— خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17456" target="_blank">📅 13:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17455">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">در هر مقاله اش ۸ سوال از خودش میپرسد آخرش هم نتیجه ای می‌گیرد که معلوم نیست اساسا چه ربطی به سوال های بی پاسخ ش دارد</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17455" target="_blank">📅 12:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17454">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17454" target="_blank">📅 09:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17453">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">CNN
:
گزارش‌ها حاکی از آن است که ایران ممکن است زیرساخت‌های تونلی مرتبط با اورانیوم را تخریب کرده و به تله‌های انفجاری مجهز کرده باشد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17453" target="_blank">📅 09:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17452">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">— مقامات اسرائیلی به یدیوت آهرونوت گفتند:
«اگر حزب‌الله شهرهای شمالی را هدف قرار دهد، ما به ضاحیه بیرون ‌حمله خواهیم کرد و در آن نقطه، واکنش ایران را خواهیم دید.
اگر ایران در حالی که ضاحیه‌ را هدف قرار می‌دهیم به ما حمله کند، ما پاسخ خواهیم داد و اصل آتش بس در همه جبهه‌ها را نخواهیم پذیرفت».</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17452" target="_blank">📅 09:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17451">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اینفوگرافیک سنتکام از وضعیت تنگه هرمز:  تنگه هرمز برای عبور و مرور باز است  • مسیرهای امنی برای عبور کشتی‌های تجاری از تنگه هرمز ایجاد شده است.  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  • صدها کشتی در دو ماه گذشته…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17451" target="_blank">📅 09:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17450">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asuseoybUToydPL6Rwi00GUQJSMGqOvJUevfY46adm9CEEgW2UbFFiSDsc9gUIHc-Fhq-Ikqp0HiT0sPlB8DuJoXGGyd1A1Hl2qiYwpVbLNLyCK3XxAqoHtOJiV9hmtncFfMTIEn1vdYgWGth0aEWoVv3WKUQjOmAh_18aJuGTZ14LuXo0hn49mllaXyDwyChRAnmMP2a2NakNEU7Og1EAB18AbP8sBxaIOx2OlaNXG_3ixsy3UXlem7J_jpihQgAe32WYPWQ8CXVQ0HzMK8AfWCKuCP6Ati93vwjO0EQBT0zKaF6NvuA4Z6dpGRBMhjreyzHFbZhw8IvWvgpDpUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی از دیشب تا کنون ۳ کشتی دیگر را منحرف کرده و از ورود به بنادر ایران منع کرده اند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17450" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17449">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF84vKlPvQrlG4vxzrwISM-HqoXfB1-1MeFHMY9K7dnKOxmJCXJ4hsimwhYzviwdvCGqmmGzNBHwDVcvmJTdrxtMtApbKB_Fwaxdjs5nhgl2WSoWFJvWImRQwHpDpm7ql5EFXY6kssNR4RZ4xHGJV5CbMgp4mIBrWzogI8kfAYiaVsflcyD7-mnSNeXmbwReXhPPa8hFLXN41V_qh_W2RbAp6vB9U7Nvlo6CU9mL9gvjt-dIv0d3LWLK3q_-7MHPyDBVWnepUTNuiLiXYFNDCjUSN615ci1deO20hKHR5I4AbK0VAS994NyNqAOxMW2X6bBbuOfl0O_T1bTtfl3pAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای انفجار در تهران شنیده می شود</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17449" target="_blank">📅 03:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17448">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پس چه کسی پول ما را می دهد؟!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17448" target="_blank">📅 01:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17447">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امارات متحده عربی اعلام کرد هیچ دارایی مسدود شده ایران آزاد، منتقل یا از طریق این کشور جابه‌جا نشده است</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/17447" target="_blank">📅 01:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17446">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/17446" target="_blank">📅 00:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17445">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/17445" target="_blank">📅 00:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17444">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0MlsxO7lOYlw1nmTMg9nVP3RCjFvRKgaajZ8w_TSZg4p6_xuH_6Ld7GE7LBHwNSGzU0HnWVnJDQ3rP4B8LRJpcmWkWz_po9KJ9RKETWt7nNlAKTMf7baorwMlgdkbtq9GcypVit_nR1ujW0kodNCOpnjV4xKgNGgJbl3PG2nmhn9hEY329WfA0nMX4hnO4XxBB_kqvaOs_XlqqTcPXij--8T4jl-54XHvzpfeYAZQeEoPBYiOiTaM9AHWnLkefeZstljTT_iKrXpH9scsnsCQODy3xi0xtguPj2Ob6Cgt92akgpSaVoNPO2mTtkzVsK959AfvBbIBWqcQJJbN-1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با Secret باش خدایی کن!  با Secret نباش فقط برگرد!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/17444" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17443">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFJCXXGVdqjpTB59yewjEemBoOhimaxQiRaeqweAGo7IUfsMOQowKbAbGRdThC78l0TG1MEVZ7cwzgS3YXA0oyVp_f7U8E9c-uitEcwbExDnvFgyj0q5sTlxH-xQ59EmvEJRn4UAcqvZm-DA413YWCQtaWUHwJV2F0lZ51Is1IQ5Ry4VhhH72Hg6vhI61zY4viT_7Q13mj3oigOJd7fLAw2DldRWjxe41fhXWYeC_OKKlK35a3LoAT44epeuz63NShS_0aA39Hh_Kaw6hLF0ZDCsM5YVrEapIFTm1WzON2eqAqUnFg98IyASgQjCB2l7rzev4O7jJThT7u_lTfGugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17443" target="_blank">📅 23:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17442">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حسین الحاج حسن، نماینده پارلمان لبنان و عضو بلوک وفاداری به مقاومت وابسته به حزب‌الله:  «ما به وضوح از سوی ایران مطلع شدیم که لبنان در آتش‌بس گنجانده شده است. مقامات ایرانی به ما اطلاع داده‌اند که اسرائیل طبق توافق از خاک لبنان خارج خواهد شد.  ما هرگز بازگشت…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17442" target="_blank">📅 22:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17441">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17441" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17440">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سنتکام:  کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند.   تا امروز، نیروهای آمریکایی ۱۳۶ کشتی را تغییر مسیر داده و ۹ کشتی را غیرفعال کرده‌اند تا از رعایت این ممنوعیت…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17440" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17439">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/troH2x2-5FxCZftHXdyEyiplkqbiS3DEeLHP1xz6EuDTm6jZpTYUlilRt1S99xe5dJoOb_YV40BryOe4ygsirddws6y38GuAkTLttHCYp9SYeWYCcWhBsp4NrWwIqO0fFRWSZ-4ugQQniQ46U9tNAGsDavFwJ3-ZlCPqJSecxdPXToJzmi0WTnY7qahLmi-_e9_J5CDL4jrUIfF27iqmHycZKDnQn8xeDqS1KYs6rM3Z7ZLeESQCD7VFZZwcav9YLot46LJx0fveQ-boCYOl6qTtpQX98Hzbig9TIrjFjQCts-9zz2DWtJO5C0AKFNDbMv7zO2aUvDngcoCNsY4uCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
نیروهای آمریکایی همچنان به اجرای دقیق محاصره علیه ایران ادامه می‌دهند. سنتکام از ۱۳ آوریل تاکنون ۱۳۹ کشتی تجاری مطابق با این قانون را تغییر مسیر داده و ۹ کشتی متخلف را از کار انداخته است.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17439" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17438">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">— وزیر امور خارجه پاکستان، امشب برای ادامه تلاش‌ها برای میانجی‌گری بین ایالات متحده و ایران به ژنو، سوئیس سفر می‌کند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17438" target="_blank">📅 21:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17437">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مثل این است که بگوییم شما نزنید ولی اگر لازم شد ما خواهیم زد!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17437" target="_blank">📅 21:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17436">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1a77UF5xjrzHM0Iif2ydx6jEJnoYSazflpb-hwldBqsPh8RcsQBknKy22YMHufNBtPN6x8K5o-51U8qbubt7XynbC3qgIAdmt4J826A49cxhujneDByU_nK_ENrPWc3JApMMEQDCNcr5urlCDPn1zh0nMjmclC6gGZL4yIJoZBH67MNXN0j7RA6SfmwFyi5TXlFnAqFfnKRzivqPzqJ5VR3ovYqW8j41g_x8WAtfxsFM0keMcinr2BYMIn3KenocpzWOyKYVzGmDNdIAa8OF4ZjXCjDqq1lm5Yf1y9vPr7Tkimnr6LmANMq-n6yjOrQnyTSFZHjtLMiuWcBimwzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17436" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17435">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:  ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17435" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17434">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:
ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17434" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17433">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مقام ارشد آمریکایی :   احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17433" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17432">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مقام ارشد آمریکایی :
احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17432" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17431">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17431" target="_blank">📅 20:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17430">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17430" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17429">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیروهای  اسرائیل تا چند کیلومتری شهر نبطیه در جنوب لبنان پیشروی کرده‌اند و در انتظار تصمیم رهبری سیاسی هستند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17429" target="_blank">📅 20:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17428">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خداوکیلی راست میگوید!  الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!  پینوکیو با گربه نره و روباه مکار بهتر…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17428" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17427">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvpWpM_wluiJC1qqzQYX-iNYjxie2VoRuDk_1fVa8gZkDncCF76lJVz6fHRBG6xKgFDOmMj1snV8b_JINmNvQuRUSVzpECfCVn5ttpNR-wKJVvRYmXW6e_Nl-PIfKNIT6riLjXVmQFa58GdXVaSCkqn7dazvG899o2iadbKm2F2DdS_dF5O2zKU3vChnub_w-4bQtHWGN_2P0rTZwjRbzgDNUZ7ipQzMMOVDixEIvCgfAsnkc6TdCcGSCqqnK-hcwCdR-kiPDMnK7Fxf_Tq9KTylddU4Dw8kOXyG35c169khyJLClwqSWrpdt6UxyAbRkG1O8FmqwfE9zJypxjt-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوکیلی راست میگوید!
الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!
پینوکیو با گربه نره و روباه مکار بهتر deal می کرد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17427" target="_blank">📅 19:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17426">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه  اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.  این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17426" target="_blank">📅 18:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17425">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه
اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.
این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به آن‌ها و کل منطقه خواهد رسید. این توافق پتانسیل بازسازی منطقه و ایجاد صلح پایدار را دارد.
در گزارش‌های چند ساعت گذشته چند نکته عجیب دیده‌ام. اول، افرادی که (به درستی) یک ماه پیش گفته بودند دونالد ترامپ رئیس‌جمهور تاریخی بود، اکنون بر اساس گزارش‌های رسانه‌ای تأییدنشده از توافق انتقاد می‌کنند. دوم، افرادی که می‌گویند نمی‌توان به هیچ کلمه‌ای از سپاه پاسداران اعتماد کرد، ظاهراً به پست‌های ناشناس در شبکه‌های اجتماعی باور دارند.
رئیس‌جمهور به هر حال نتیجه خوبی برای ما به دست خواهد آورد.
t</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17425" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17424">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukuXpbfqSgUSXN5FN7Y3R_exlMptFayOCPg27UiYcUoECwecFq8nT5lAlByIctpczBgUK8-ROUOFfYbv1eEKu0kvM6is1SYPjfNOqMyG0fBIhNqxV3mG23P6iCcH7NLOdRdBl0rS5Xj3ir4Qe3dWjrvximk3qriL77Aa5qU9WimIX8nlrp68mjQ1nhmwq0H6fy2AbRM_F1gy2q_ZUc_DbNaYwSTeo_9eR42eL1xQQDG0S-p5BJoabWB_w6aIFGQIAFJzaJf2HfzrtTTwwhOx5ADPMvoZ5vb6s0VhX15R6gSNEf485rvdhCpCMjFZBzMIxkDyGl73o7WsZEOfyg0V9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه دیدید یا نه؟!</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17424" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17423">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5RcJ7lbGc-Q5vGFu6I-FpKeAogA99-baLBo7aC0zzoW5KiJ6yFvEE-bC-mMG9_UthaKwm08O58X6o_yHvJ5rjyMSDirPluVPWyHONdjogK5YH1q0qzePEkGo1BVyTYAKLrfRqjE1N33iEiHLPYIkHhmpHKsZU5g3PGlQhca-WxOO_vJSjCh0j8KFCpcADhuiKt6LL2ME_2Iwb6LueY7474CXt0X1p5UV0fCm0ESHqOLaJ4O-TCpuwB2fonBynu3ED0h-NqoZ2u2SeIDxwOFclHOQd977aVfi5QeEA_GZbN7UcofG0eUF1j-d93z0ITyljJebFUTEwJ-67mOYaMblQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17423" target="_blank">📅 18:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17422">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزیر خارجه ایران عراقچی:
تفاهم‌نامه اسلام‌آباد هرگز به این نزدیکی امضا شدن نرسیده بود</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17422" target="_blank">📅 18:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17420">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فوری | یک مقام ارشد آمریکایی به الجزیره: تنگه هرمز باز خواهد بود و هیچ گونه حمایت مالی از گروه‌های تروریستی توسط ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17420" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17419">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فوری | یک مقام ارشد آمریکایی به الجزیره: تنگه هرمز باز خواهد بود و هیچ گونه حمایت مالی از گروه‌های تروریستی توسط ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17419" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17417">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVcMgh8KkzIuieWJ2yRYdzq395arFtLP9AAoCswvuBeBlJRn3SRuYnC4mCsyVtUCrsSoIZMBvtNSjFAgg4tA66Or5yj_0-K_YC32_DAtNl4kX-X9cg8JxboY5Ys_0i0wnnG0ka5tZFkTWNN7i_OJL272iOee5LJqUokXJw721siJIr_dClSFc1B_tu2CRZufbw1jkcHS8XSe3vn4Hd2ZqnVijmNgUKCWP96ErRFMmclqSOOafrMS3ffDvn6zyedAbpPatF0w8e2VCxvnp7q4vM_opqOHxfnrKC0nKnMHdW-FTdmnQcaaosiXvXp_nvQaQAKR-AU3uQgEbP7HEW0lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17417" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17412">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ev4G_gTcIbDl-2JDfCIbVyvDfjKaIy-HpmPqnDXIRVpwQUI_--ftOkELj-mLUSR0PMlp-79t7f7svUaSI9lVfq-ZGPRYdY8T4tRVumbjRdvE0ab82AEL4On_X0g9mxtCsRal6PrVFtiFsgAn8xTPpKX5wEgJ_Jfc1H3o-4vYUhBSJn_oWYGy84EOFtXrLHLHtED9CPg-4FdMWxq4NPhynX7s4bkpLecm3QViEgrIvhr19jA3LQqhEdDAlxO16vWW9sZDbaH7oqD510eF3HqB_b4FmCecvCcnAz1Iv_1V-_iE8rCqmGlhYMkZ5ePo0YwArGp7X6UBLay30dGepevxYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p6roZz_aqzQfZQnW4hj1yO-DyvsEgKMcqmKq0Y3qG3EenH73s25hP54UFQRPsewYE7Qwd_T31d4Kgrog9EpTl_wGKuRuJEPk6yWsGsc6X6x4z766-EGOpZGshnMzlYTjbiSDYQGEvbZlE0UVpVdguOcrT3JLbx0NXtVs_csc7qumQX3IcuERrgUvwbD3Z5g7sZBIuoJvhkjfK-dA-YofVkHa0cgWFmhd5d4RxqQoOeU28dCficCnQCFO8WO6usyfOnL_GtJ1aRW6pjzmb8VhQ10c0U0A49gAMSfMmU6kf50kYTY4nRxUeHn6NqszDD6eQmzcvn9YG_dq5P_uZAvqvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WK98CMIJzE81Mty3JNOX3q4M9rQA0Hp9vlHdjwbuve2nt1hdyYNP6wEs5DB3638N96os3tD35MjRojyg3w-5DR9la54MQuJp43ZMUJ5whp5AfRNrNh1-KJTmyT-zs4r9YcDjJwdCxKur7Zf2nAbqrnrchhtV0d7kk3LpWJvl9dvJlLFoCONha7zar2O6S7ZnduBinmJ-idd7Wnu3T1CXW3q9NJbYh4hBBs3y_8sLjN5r7tmzFXLuIlcJr9CM3xocc0Q43u4oDfDZjA3qQVd9kpccSyIYjlOMnqUbjkKUmFgY556N6Q8DKaz5xaa2cGtwR3l0vgpwATAt6zTbgHnDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmM2HxfVkHTbgLpyJhOzQw2VFdh3idm1qZr4smDRsyvWslQMFq7e-UG4fEsu5n5rNhkDYqy2OQW1HX0nKY0ARaNdSZ8uw6-zIUXmdtn2uEzMCWdqXDOuKlpDSlb6Y77Uhtz7m6eYJGfgl6vahPAXEhVDNqVi8YhP0m5rOgHLJuM6Mwx9VfOqZa8Myk2WeNIdodGgYd0XPlI449ahinUUvJxbaLCbn-3KwRObIUuf-1FnTz7KA0kA9EQ4rmrs3m0kOcRIZ2P0tgWU32gaa-pDRX1o-Be_TiVR8yVA51zhA7zc1u8ao77m8q4b0RSkdSLRJVsKMZv2kaj8ehEcLCcNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIA8A2JqpluncJwLWghQWQw0f8LzMw8Yaeng1FP6cm-xYoGMQvrKTe8Q1F5k8btqsy9yeIOSRMfS8bmjFf16yIHWVjMmsyvD57rZU9-WP64AUkdo_PcImjdzgq11hs0V7OF7N__1FUXpQ7OtUdBMci5iawibHfTCqXQH1tzcw8D3o2RjZKCyqcRnkstbA1aD0h1RuawR_VD-tTVr4GKaMzcSjsNL9o06dS0nYpBoOJG4cDCOqxHN0S95huuuQaHcZKzxvlipBZ5gI3pqNAwZCH3tnmczSdkgY7yH60fRWulNqn_H0RGFx013n2GfmDpfHCx_95-I0ynE08r6RJNSGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتفاق جالب در ژست‌های قلعه‌نویی؛
⌚️
ساعت "رولکس اسمورف
"
چشم‌ها را گرفت!
👀
ساعت 10 میلیاردی امیر قلعه‌نویی در فوتوشوت‌های رسمی
#جام_جهانی2026
سوژه فضای مجازی شد.
🆒
این ساعت از برند لوکس و مطرح رولکس معروف به مدل
“Smurf”
است. به دلیل ترکیب رنگ
آبی پودری (Vibrant Blue)
در صفحه و بزل که تداعی‌کننده شخصیت‌های کارتونی اسمورف است، این نام روی آن ماندگار شد. در حال حاضر قیمتی بین 40 تا 50 هزار دلار دارد.
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/17412" target="_blank">📅 18:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17411">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امیرحسین ثابتی:   کسی حق ندارد تنگه هرمز را به امید رفع تحریم یا محاصره باز کند</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/17411" target="_blank">📅 18:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17410">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این یعنی توافق بی معنی است:   اسرائیل باید اطمینان حاصل کند که در آینده نیز توانایی اقدام مستقل برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای را خواهیم داشت و من و بنیامین نتانیاهو، نخست وزیر، به ارتش اسرائیل دستور داده‌ایم که بر این اساس آماده شوند.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17410" target="_blank">📅 18:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17409">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17409" target="_blank">📅 18:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17408">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خب این نخستین آزمونی است که باید گذرانده بشود. ببینیم در لبنان آتش بس می شود یا خیر.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17408" target="_blank">📅 17:59 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
