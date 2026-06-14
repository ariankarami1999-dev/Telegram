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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 18:06:42</div>
<hr>

<div class="tg-post" id="msg-17522">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">طبق گزارش خبرگزاری فارس، منبعی نزدیک به
تیم مذاکره‌کننده ایرانی، تنها چند ساعت پیش از حمله اسرائیل به ضاحیه، فاش کرد که تیم میانجی‌گری قطر در حال حاضر در تهران حضور دارد و بندهای مورد نظر ایران و جزئیات مشخص را به طرف مقابل منتقل می‌کند.
این منبع تأکید کرد که هیچ چیز نهایی نشده است و فرآیند مذاکره را دارای فراز و نشیب‌های قابل توجه توصیف کرد و بر این نکته تأکید ورزید که شرط بنیادین ایران این است که تمام ملاحظات آن در هر توافق نهایی به طور کامل منعکس شود.
این منبع افزود که حتی اگر تمام دیدگاه‌های ایران گنجانده شود، در زمانی که دونالد ترامپ اعلام کرده است، هیچ توافقی امضا نخواهد شد. این اظهارات پیش از حملات اسرائیل به ضاحیه بیان شد.</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SBoxxx/17522" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17521">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ارتش اسرائیل برای احتمال آتش‌باری به سمت اسرائیل در ساعات آینده آماده می‌شود</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SBoxxx/17521" target="_blank">📅 17:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17520">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مرندی :
فعلاً مذاکره دیگری در کار نخواهد بود.</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SBoxxx/17520" target="_blank">📅 17:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17519">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">معاون قرارگاه خاتم الانبیاء گفته ایران به حمله اسراییل به ضاحیه پاسخ خواهدداد</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/17519" target="_blank">📅 17:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17518">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">برخی منابع نظامی نویس ایرانی:
به نظر می رسد فرماندهی موشکی هوافضا در حال آماده سازی یک حمله گسترده تر از عملیات "اخطار" و "نصر" می باشد.
- اگر در سایر موارد مسئله ای دخیل لغو عملیات نشود، شاهد شلیک از مرکز و غرب کشور خواهیم بود.</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/17518" target="_blank">📅 16:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17517">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/17517" target="_blank">📅 16:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17516">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/17516" target="_blank">📅 16:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17515">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">قالیباف :
تجاوز صهیونیستها به ضاحیه بار دیگر نشان داد که آمریکا یا اراده عمل به تعهدات خود را یا توانایی آن را ندارد
با چراغ سبز نشان دادن به رژیم، نمیتوانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب، دیگر کهنه شده است.
اگر اراده و توانایی عمل به تعهدات خود را ندارید، صحبت از ادامه این مسیر به سادگی ممکن نیست.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/17515" target="_blank">📅 16:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17514">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تلویزیون ایران به نقل از مسئول سازمان مدیریت تنگه هرمز در خلیج فارس: تنگه هرمز تا اطلاع ثانوی بسته است و اجازه ورود یا خروج به هیچ کشتی خارجی داده نمی‌شود</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/17514" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17513">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیم ساعت پس از حمله در بیروت، گزارش شده که یک عملیات هدفمند دیگر انجام شده و این بار در شهر صور</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/17513" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17512">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/17512" target="_blank">📅 14:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17511">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/17511" target="_blank">📅 14:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17510">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=hfExn4gxD3LFqBJdslPLlq6hB0Fqv4e6s50bTjv__AyIb2ryYy97GTCJ5LGU2warwV11BSF-TlyAhCFbNPH-VlnPMuhgEO3IPpMrYvNGxHgWeXAVaKkMzMivqLbJEp3HBRyfXvspKdyo4tPMYlIbtEk5dSxx95Mi9-U2K6DcRYRSlECW4FbjsFmaGVqk6KhryBAsq6a_WluhhUqVn0ScVoptupCfiOg4PpFOjsJppZ_MDQRSi4vQbjKWO-ScNnCWv9wbVEklQ3FZT00_G1bm8wfr2upg-r-JCkGl0INGgqn2GQyOdFXPI4Lh1pIGHsXbiyAoV_Xfw9TjG-_bCGJ5SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=hfExn4gxD3LFqBJdslPLlq6hB0Fqv4e6s50bTjv__AyIb2ryYy97GTCJ5LGU2warwV11BSF-TlyAhCFbNPH-VlnPMuhgEO3IPpMrYvNGxHgWeXAVaKkMzMivqLbJEp3HBRyfXvspKdyo4tPMYlIbtEk5dSxx95Mi9-U2K6DcRYRSlECW4FbjsFmaGVqk6KhryBAsq6a_WluhhUqVn0ScVoptupCfiOg4PpFOjsJppZ_MDQRSi4vQbjKWO-ScNnCWv9wbVEklQ3FZT00_G1bm8wfr2upg-r-JCkGl0INGgqn2GQyOdFXPI4Lh1pIGHsXbiyAoV_Xfw9TjG-_bCGJ5SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/17510" target="_blank">📅 14:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17509">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/864badacb8.mp4?token=sWWOal4LRhlZU7edbR9E0VmLAGwWer3V6wwr0AG_acNCQyB49wimz2jVimHiEmbFMX--V9dbW2UlT342rcs_5GzRMQLHCwWNnWIBoB9Oz5e00C_4fIr_4nh-f_G1TuYZa4u7592sOUKDUr9WWB6WQX3rDbB8dqjLJfUy0udRNKpLNbs9hABI3Fju95JJL27S8HqQlqfg8QwUopP0g22VBf5PvCyNy3KZRIr_xgKn6B3Nm2T2Yyz4CJDhNo3LnH7AJVtk-CWBMTTcbsv-C3PEB2bSq676CjF4QYOwd6MmeArC9wJbTwUxWheYNvDs4Zt9gdMekDbLtjZStD__EKWtbFNWJZBGjHFFjJYPnji9niT8EZ-gFnGA9KiPhDWXnOEdqaBo98fDpIeiS2DvFVPyTgdZK-2IEKWq5BM2Rm0f4j2yx3tBAuR-kXSyKQxL3uDuep2_dBvOJ4iMuOGHU-18Mf8nlw-MPSoSZcEOnYYm5VXET_dYh6FSk27A2Q28o1Faru8mxcS2FjwonL5uA3cV5TsHfq28ezbVoON0OxTtggXDdmck9JPISi78Xpgfsv4yC5EDhZzn8Y8RVq_5DUtWkc56l3PJ8aVx8m7-fLO-i4Ju0JPD-PfF0VTBZ6DiLYFg5OcT4049tl6EU0CxWAa0DHY_gGCZbFkyWeJnxLSSqaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/864badacb8.mp4?token=sWWOal4LRhlZU7edbR9E0VmLAGwWer3V6wwr0AG_acNCQyB49wimz2jVimHiEmbFMX--V9dbW2UlT342rcs_5GzRMQLHCwWNnWIBoB9Oz5e00C_4fIr_4nh-f_G1TuYZa4u7592sOUKDUr9WWB6WQX3rDbB8dqjLJfUy0udRNKpLNbs9hABI3Fju95JJL27S8HqQlqfg8QwUopP0g22VBf5PvCyNy3KZRIr_xgKn6B3Nm2T2Yyz4CJDhNo3LnH7AJVtk-CWBMTTcbsv-C3PEB2bSq676CjF4QYOwd6MmeArC9wJbTwUxWheYNvDs4Zt9gdMekDbLtjZStD__EKWtbFNWJZBGjHFFjJYPnji9niT8EZ-gFnGA9KiPhDWXnOEdqaBo98fDpIeiS2DvFVPyTgdZK-2IEKWq5BM2Rm0f4j2yx3tBAuR-kXSyKQxL3uDuep2_dBvOJ4iMuOGHU-18Mf8nlw-MPSoSZcEOnYYm5VXET_dYh6FSk27A2Q28o1Faru8mxcS2FjwonL5uA3cV5TsHfq28ezbVoON0OxTtggXDdmck9JPISi78Xpgfsv4yC5EDhZzn8Y8RVq_5DUtWkc56l3PJ8aVx8m7-fLO-i4Ju0JPD-PfF0VTBZ6DiLYFg5OcT4049tl6EU0CxWAa0DHY_gGCZbFkyWeJnxLSSqaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی اسرائیلی ها از لحظه حمله به ساختمانی که ادعا می کنند ستاد برنامه ریزی عملیاتی حزب الله بوده است</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/17509" target="_blank">📅 14:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17508">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/17508" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17507">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :
ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/17507" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17506">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/17506" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17505">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">العربی الجدید: تهران توافق را تأیید نکرده!
در پی سفر امروز هیئتی قطری به تهران برای گفت‌وگو در مورد یادداشت تفاهم، رسانه قطری العربی الجدید ادعا کرده که
ایران همچنان ملاحظاتی در مورد این متن یادداشت تفاهم دارد و هنوز تأیید نهایی خود را برای این توافق اعلام نکرده است.
العربی الجدید به نقل از یک منبع آگاه ایرانی نوشت که این منبع ا
حتمال امضای توافق در روز یکشنبه را منتفی دانسته
و تصریح کرده که همچنان گفت‌وگوها در مورد توافق در داخل ایران ادامه دارد و
موضوع به صورت کامل حل و فصل نشده است.
این منبع در عین حال تأکید کرده که ممکن است امروز توافق نهایی شود و تهران امروز تأیید نهایی خود را اعلام کند.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/17505" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17504">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اگر نتانیاهو بخواهد تسلیم این توافق بشود (با این فرض که اساساً چنین توافقی وجود داشته باشد و امضا بشود یکشنبه)، عملاً سند مرگ سیاسی خود را امضاء کرد و سپس باید ریسک دادگاهی شدن و زندان را هم بپذیرد.  اما میدانید که نتانیاهو سرسخت و سمج است و بعید است به چنین…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/17504" target="_blank">📅 14:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17503">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsAlyuvBXj2JhtxMe_ghMwlGgPnsVlbX2xD1M6C0QeeBe4lIViE026lVgs_tDtv3CNE-lwAt1defUDpu1FWlf1FJPa5KhFusFc6Xo1xKATG9PBaVUicilgkZ4301ck4wsxUzW3SHS8uDS1l9Y9o1IWdSWIx4LJv5WH6sAVUIl-2e54TXioRHa5tM2vSs5NSF_rFpUooFR8yD--wSkUVhXpYEwsLlLZft6C8oP6LGItd2Werpp74VOud3SNM2T8bNfS_UVLZf83XEzAguaBHhCtFetU2bWyzr6LWx4vrSop92zZCZud1IaF57KmbjDr1pyCN35nTCbbBqkn939Q_JvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/17503" target="_blank">📅 14:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17502">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/17502" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17501">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1668556cde.mp4?token=G8v_vjHYCWBcOWEmihkYzonraM8ot9eOtGL4lqaJ_5-Uzb2yiZUlqYgQffpQ7oPOh8vN5Zq-mfC1-tyEkTUGaY7MZEh-2Jppk7Ct2di6Ec_TishblXXk5XwLBBcjUsiUU1of0PWeOX1f3M_RJqYaOhj24zPA58kvo9L0IryE6DovDTTkEpoZG2S9gwMf34BeTKyAKHKMCBfvfjadyoY3s8GDLHj7h_g-vio_MLuIRi9cH5pPhHxRlPNY4srOVh-eADbsrV9fCwaxTIT0M6FM3iSWzxnce3AhaYE1_9F7ZzO3j2B0naHjT-4v9mMaUF207FAm3Z_XGivpMCmr3y_NUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1668556cde.mp4?token=G8v_vjHYCWBcOWEmihkYzonraM8ot9eOtGL4lqaJ_5-Uzb2yiZUlqYgQffpQ7oPOh8vN5Zq-mfC1-tyEkTUGaY7MZEh-2Jppk7Ct2di6Ec_TishblXXk5XwLBBcjUsiUU1of0PWeOX1f3M_RJqYaOhj24zPA58kvo9L0IryE6DovDTTkEpoZG2S9gwMf34BeTKyAKHKMCBfvfjadyoY3s8GDLHj7h_g-vio_MLuIRi9cH5pPhHxRlPNY4srOVh-eADbsrV9fCwaxTIT0M6FM3iSWzxnce3AhaYE1_9F7ZzO3j2B0naHjT-4v9mMaUF207FAm3Z_XGivpMCmr3y_NUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوبی است.  باید تدریجاً هرات از هر جهت در بوم ایران ادغام بشود.  چرا وقتی نظم مسلط فروپاشیده و همه دنبال گسترش مرزهای خود هستند ما بنشینیم و به مرزهای جعلی استعمارساخته احترام بگذاریم؟!  هرات؛ نگینی بود که توسط ناصرالدین شاه حمال از دست رفت و هیچ قرابتی…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/17501" target="_blank">📅 13:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17500">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV5jAQsJMAzK7FKWlUHhvFkDskl5iMrvfUePvgb8tzZGvIkXG0CxhAijMldRwvVxHt6maWHSqDK3eEewzv1Jd2nEeRrr-0RqXec9ILbHy_rSQS_BXRGWLM-5OJf5BrAxGLEJbRPJdljLQkHEC4ncdtOcPjukxlKHbHc-eRbs_ebdfmIBri6BIEge3omYh0bLjLGfqJEJeM15jKkJoJWRJu6-5hvG3fKbUdSpXDMuW8-yMmeeByjTrzaKcwe7l84K2lxty5mA7KvQ3FsPBByJILD9kgfaIYDWr_RSCQWBuImu3HJj9yMsUvh2oPBSwClm1RJFgC81vFNDSWpglWZv7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز هشتادمین زادروز این نکبت است.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17500" target="_blank">📅 11:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17499">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5xolQFDvTwvdiU6YkqsIJASrs4ON94gXmzydlwr43mX5IZy6gynCZpwHDJPpYW434I72yRlTA0zgk1_mAryZn1VzMJdSE5TCmNB5DfAABtfcZV-lGiTwTvsM3FeYTuTYccjCGd2wOUo6lXusYPC20YjZQrj9dGFzjorNxPwvqU_eVn_Hzy2P2Zb8DMdkFD4en_HRKck9zXEgUZxzwIjYdkeMMaVGrAqqOWnUCiT9Yu5AlS4nsH0O5crFsSleKF_-CIJLYKmkuZ73pF-dc4BkBHAhcG9S4XkqJ8GsMdLHKdhlAaAwPxEpsPGCFOVSN6ga4soXKyJGzVunYdNwqzb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنا به گفته دو منبع آگاه که با شبکه CNN گفت‌وگو کرده‌اند، عالی‌ترین فرمانده نظامی ایالات متحده اواخر ماه گذشته سفری محرمانه و فوری به مقر فرماندهی مرکزی آمریکا (سنتکام) در فلوریدا انجام داد تا به‌صورت حضوری در جریان طرح‌های ارتش آمریکا برای اعزام نیروهای زمینی به ایران و تصرف اورانیوم با غنای بالای این کشور قرار گیرد؛ ماده‌ای که مؤلفه اصلی و ضروری برای تولید یک سلاح هسته‌ای محسوب می‌شود.
این منابع گفتند جلسات توجیهی آن‌قدر فوری و حساس بودند که ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، ناچار شد در ۱۹ مه نشست مقام‌های ارشد ناتو در بروکسل را ترک کرده و به سرعت از آن سوی اقیانوس اطلس به تامپا در ایالت فلوریدا بازگردد. به گفته منابع، سطح بالای این جلسات و فوریت آن‌ها نشان می‌دهد که دولت آمریکا تا چه اندازه به صدور مجوز برای این عملیات زمینی پرخطر نزدیک شده بود.
سخنگوی ستاد مشترک ارتش از اظهار نظر درباره تدارکات مربوط به یک عملیات احتمالی خودداری کرد.
یکی از منابع نیز گفت که ژنرال کین پس از آن، رئیس‌جمهور دونالد ترامپ را در جریان گزینه‌های موجود برای انجام چنین عملیاتی قرار داد.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17499" target="_blank">📅 10:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17498">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تحلیل من همین است که ۳ هفته پیش ارائه شد و امشب یا فردا یک صوتی هم در این کانال قرار داده می شود.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17498" target="_blank">📅 09:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17497">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrVzNsGF9DYPeAuTCD8V0LAXO-Nf24jPpEfQqI5VB3q7x-R4gyrdMFaE-z8YZ17VbXcuH9kuU0FVXS6E_7auLFYc1buSh1p81ftQGGMLfjULJHRjcRPY643GRBMWA-bTGEoRgGDg7N85kWLCh_sIHtRTlm0tjGivJJlwxOXuCIsvLXWxg_gVrHLwvpX8otXkvo5teY7tp7enmBd1HoXIay1fOrOJxWSa-Bx4o7KQ3tTGqpfT9kaNBFrTKLoENiLbJ9epP6hfge9gJAx9t0mLaIhABiZCM5AEV1KT-OaGEJsoul-g0VVMpqN3b9bddt69N3vKdgzsb7KYi-98BSkJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک رادار آمریکایی در بحرین بعد از حمله موشکی-پهپادی سپاه چند روز پیش</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17497" target="_blank">📅 01:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17496">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خدایا درگیری جانفدایان کف خیابان با جان برکفان ناجا را هم دیدیدم اما قهرمانی .... را نه!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17496" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17495">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایران تمام دارایی‌های اقتصادی مدیریت شده توسط ایلان ماسک را به لیست هدف خود اضافه کرده است و شرکت‌های ماسک را متهم می‌کند که در حملات دیروز ایالات متحده علیه ایران کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/17495" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17494">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwIGjLTefaBj-KDLC7SBtIyTo3jIxMkYHTJoJyyFRFYEQzMLZ5uv6HkG9g6ZherRi4XuUR5VMTcJHMmLBtN48yYVJZcWHgboxMxR7pmRC-n2HTH07MNXakUz4dZqft0yETzToN5Ik4wCcs8tq0DC54W-ShoEnuxRdSrg1Ym8jNZkhrHdpVqRuJAwrsYseykbyF-SznhHRqrOHingM0LmrSQWN8SVL_SiOhrnELNynZ5Oea71mhOaGiTyYH5MnR8cW1Y3z192Cc9JXdrEAClN82M1dfGKj-mIVcmQ0Qc56iJxJl8PSwJPwNfGznmBMEdsnRhbyD8ScSn1vEfvTA4bOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا همه دارند به تنظیمات کارخانه برمیگردند!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17494" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17493">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpejYECtNqex1n10fJs9ienHB2e6Dtt69fU8H2Kfct1DJ_hIxRlA39xZT75mHM5GnbFPRNbam96kVud_kNd4_Njo1XZq194vvm7jPpmcrTx4faHd0qyhXNIEkcK0I9EjVLzCx02q-XLZ-Jd639_BQxOcbI5eawJpILTC6wZT_r_9ufez-lhpnHTNLrfgTSzMImd7X0sf9luj6_EwAoONMDMD1DhWFcxlSlITl4_L1G6_3Y-sC1lFYlGosvBY20dGVm71L2sbg6a4O6VzzeQvY5mMT20a2NFTw5o9qVlamKgLt_Fy-6nbRv-y2JDs0nix1g0NZwR7CDozwJONofle7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!  فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/17493" target="_blank">📅 23:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17491">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/17491" target="_blank">📅 23:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17490">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!
فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17490" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17489">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/17489" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17488">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/17488" target="_blank">📅 22:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17487">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:  "هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17487" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17486">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:
"هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/17486" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17485">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شرایط جدیدتر اینطوری است که ما کشتی های هندی را که از ابتدای تنگه هرمز  می خواهند عبور می کنند میزنیم. در پاسخ، آمریکایی ها هم کشتی های هندی را می زنند که از انتهای تنگه هرمز به سمت دریای عمان می خواهند عبور کنند. ِ  این وسط، گاهی کشتی های غیرهندی هم هدف قرار…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17485" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17484">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خیلی جالب است؛
ترامپ می‌گوید نه پولی می‌دهند نه عوارضی از تنگه هرمز اجازه می‌دهند و بعدا اورانیوم غنی شده را هم خواهندبرد یا نابود خواهندکرد
مقامات  ما میگویند هم پول میگیریم هم مدیریت تنگه هرمز با ماست و هم بحث هسته ای الان مطرح نیست!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/17484" target="_blank">📅 21:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17483">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17483" target="_blank">📅 21:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17482">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">منطقی هم هست؛ امضای الکترونیکی که دیگر حضور فیزیکی لازم ندارد.   بوگندوهای فاکستانی فقط دارند می روند شام مجانی بخورند لابد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17482" target="_blank">📅 21:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17481">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فوری | ترامپ:
ما امیدواریم که عملیات به راحتی و به سرعت پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مجبور به استفاده از آن نشویم.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17481" target="_blank">📅 21:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17480">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حالا که همه چیز را دادید رفت، دستکم به رستم تهمتن بگویید دیگر نزند!
کور شد بدبخت!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17480" target="_blank">📅 20:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17479" target="_blank">📅 20:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ:
«توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.
امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد شد».</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17478" target="_blank">📅 20:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17477" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17476" target="_blank">📅 19:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سخنگوی وزارت خارجه: باید هزینۀ خدماتی که در تنگۀ هرمز ارائه می‌شود را دریافت کنیم!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17475" target="_blank">📅 19:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17474">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این طرح واقعاً بامزه است.  کشتی ها باید هزینه «امنیتی» برای دریانوردی در تنگه هرمز پرداخت کنند تا نیروی دریایی سپاه پاسداران از آنها در برابر حملات نیروی دریایی سپاه پاسداران مراقبت کند.  سبحان الله!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17474" target="_blank">📅 18:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17473">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزارت امور خارجه ایران:  «تیم مذاکره‌کننده ما برنامه‌ای برای سفر به ژنو یا هر مکان دیگری در دو روز آینده ندارد».</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17473" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17472">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17472" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17471">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17471" target="_blank">📅 18:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17470">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/17470" target="_blank">📅 18:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17469">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2c7dzHEJc6f4i9Pt8fbQBYaq8yZcGV6wLnI2_bnzS0NDg6D1AcAUDIMjYhToOxOCYhEfdjVyR4mXriycL2PTGXvaAsBxC__TCBSQpdrEFFQWMyT6j1ZSSu3LLycBrvapuhF-hl9a7iRZtDZVEdT3U7tC_8TJI6zTvGSRkFdUKfAKY7wBgSmElDR0wcBqwXhB45UeumVR_vpRmpsRbS1WjVrynNlFJTSvz1HoiIXD2rdjg3wAzixCLMj3aNxqAB4k9qZkgruM-dn4twqRlalxrwaTXLQgNufSioamgvEL5rYMvGWztGRqm7CNj7RN3VOB1ufSS_CsefMMuuQdIy9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله! جانفدایان یک پویش توییتری راه انداخته اند با هشتگ نمیپذیرم!
که اشاره دارد به برائت از ائتلاف قالیباف-ویتکاف!</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17469" target="_blank">📅 18:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17468">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گویا یک ستون از ارتش اسراییل نیز به سمت صور در حرکت است.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/17468" target="_blank">📅 18:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17467">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17467" target="_blank">📅 18:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17466">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlSsFTBw_9sVRaIxqTRIPzyWKU26X-oedvbayNJ-kE0MTRnLXa9VHWKp4a7nOSC9E1m7PyFdyHe4GgYelWSld9PrZrazZKgQ1Mq7OhcRuRzUscPsGsD8qGMNK1-vCL79n7I54I_PrD3zg71H2ZoCbPOZCb6c5pfcRqMEMP0y_b-oitP8gmcEHSD5AC3sDQEmpDZWfcSLPesgkMbMRljQ1KlS1bKGljhB_wi2d3YpkkdxPJ-CJk2gf6LvIwc4M_HBXI79IspOyzwK7Q5yDNRQ6liq6vwe8xCu2re1K6XIMRxVD94NO-ZcaXFEEeZLyMbgqLHeKJ1fzfn7loheA4Q_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت را دوباره بخوانید:  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  پس در واقع تنگه هرمز برای همه باز است جز خودمان؟!  سبحان الله این که عکس چیزی بود که میخواستیم!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17466" target="_blank">📅 18:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17465">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17465" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17464">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgbgRNhnwAsj8ahInkzqjV7jDEj-OtmMIOPTmAd9InMcFN7KbuNZIFAru7Gzbyjl8aDdRFh4QX7dWlGMCm7vderZg2Osl9YAEyycE4hA0n9nKcjFZjqj91nGevK43FCqMZ-aGs858cmuRvlhe_scG5YyhvqvhfOqDHXQMxpihoAfTmOySLa7MOTJxp-z5eb70tlKk8df-ziJ8dUSVKjpMwpwlZWreyI9dBUyMUcVEGfw6iPx77koQQLC9uE6UHOn8ElYuTgslaDDPPrqeSeZ7f4OzTvjsxcSnvLhG0ykhAslWF2a9TEAQ9ir_VpZMES8RIGEYnOv1c-HrDvId8l-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه جنگنده اروپایی (FCAS) در آستانه فروپاشی!  پروژه سیستم جنگ هوایی آینده (FCAS)، که با هدف ساخت جنگنده نسل ششم اروپا و با همکاری فرانسه، آلمان و اسپانیا راه‌اندازی شد، اکنون در آستانه فروپاشی قرار دارد. این پروژه، که در سال ۲۰۱۷ توسط امانوئل مکرون و آنگلا…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17464" target="_blank">📅 15:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17463">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">13 و 14 تیر: وداع در مصلای امام خمینی.
15 تیر: مراسم تشییع در تهران.
16 تیر: مراسم تشییع در قم.
18 تیر: تشییع در مشهد و تدفین در حرم امام رضا.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17463" target="_blank">📅 15:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17462">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpLCdZ6W6lS5M4qkpb27HwXXbzd0jF_jyeXCN3G5tBgZ8bvJ2q6Hl3uaLMdf1vdmcSvSVAWhfhgfx1XZmLUYrz-i_N6-D8FHx9mnLQnU0n47Kkks2IpfC4rUCh6y5vF63hzTvvTdw15gGT045Ad6jQS_QGK_yigChjqhdTNytUo0NprD1-3EF3ImaRovltfjYTnOmwr9MyQSs6z384Qn7WRAVUE8z62wCLKpuStc1emrUUgtbKvkKVXHCZ0Z0c6J6IgVaqMpq-AfOzhLFAkuVqsFHVDLMagDeirz-TyuHyWypkBFeE_s-AEqb3cap74Msn4bER2N_eByt5xYW_-_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در جنوب تنگه هرمز هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17462" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17461">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">صحبت های جاناتان پولارد — جاسوس معروف اسرائیلی که در آمریکا دستگیر و 30 سال زندانی شد — درباره جنگ بعدی اسرائیل با ترکیه و مصر و لزوم استفاده از سلاح های نامتعارف کشتار جمعی.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17461" target="_blank">📅 14:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17460">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=ZLDgSMEZ1U_gN2JKkHV9F7zSgL7jjpUVWmF3JCy6mp9_vLEeuER-yByuOWxdGVhfSlWpk2WmUaPfjuvnztsTDXKoUq6ZyeZR3psk7bll4hMBecf-Bknk2tivOgpmhc68_zQmlmIoARYQhyU2Mil8UX8kXWa1W_Ed9JiLOFKCCOnRaKIQrdpO0o3imwB6o3EEtN-Ljp-wkYNhQp_13v61xL6co3YIFHdRx5h_oDyj8OVvEo6alQ6wzU-d35mc_Neg0lg1t6HKykOan36sVIDcyDWCMK-DWJ7AAeCV4W3wnzRfQB0jKqLVlN1p0LDi_zX8imF_ldyEvTWJCfokK9a9dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=ZLDgSMEZ1U_gN2JKkHV9F7zSgL7jjpUVWmF3JCy6mp9_vLEeuER-yByuOWxdGVhfSlWpk2WmUaPfjuvnztsTDXKoUq6ZyeZR3psk7bll4hMBecf-Bknk2tivOgpmhc68_zQmlmIoARYQhyU2Mil8UX8kXWa1W_Ed9JiLOFKCCOnRaKIQrdpO0o3imwB6o3EEtN-Ljp-wkYNhQp_13v61xL6co3YIFHdRx5h_oDyj8OVvEo6alQ6wzU-d35mc_Neg0lg1t6HKykOan36sVIDcyDWCMK-DWJ7AAeCV4W3wnzRfQB0jKqLVlN1p0LDi_zX8imF_ldyEvTWJCfokK9a9dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17460" target="_blank">📅 14:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17459">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17459" target="_blank">📅 13:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صلح دوست ترین ارتش دنیا را لبنان دارد.  به محض نزدیک شدن جنگ، مرزها را ترک می‌کند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17458" target="_blank">📅 13:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MITQlAqNmJLxDGzYpiK-RUl8Pb0wPB6eswhH1d7taQYSgILdSkyO17ykFn4w1U_Zt25azVnNsTSuOFJhYM9L5PZMdMNgXnsOW7BpZiyc7TlUHpNVlSKwAC2EM1NteeQ7h3gl52jvlfCodUUcTHwbKk3l-pYSCbyX8rFWKM85yN3kfl-1DMhMz0LWeTAkKs2wlVjhDpbnjsBqhTkIm67ATwR6bz5iMRoSJ7et0bsKC9yc4SKbwz-aYtiRkAKQKSBD11TMjXNchpMa-fsyA1owLKOjZA1u_5KG0hbd_I4WEuCmvAX0LfV_qRv6Lx-EsAm0oColFnrAZax6lbajuAY0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17457" target="_blank">📅 13:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خدمات الکترونیکی در چهار بانک بزرگ ایران — بانک ملی ایران، بانک تجارت، بانک صادرات ایران و بانک توسعه صادرات ایران — از صبح امروز مختل شده است و این اختلال بر بانکداری موبایلی، بانکداری آنلاین، خودپردازها، پرداخت‌های کارت و سایر خدمات بانکی تأثیر گذاشته است.
گزارش‌ها حاکی از آن است که این اختلال ممکن است نتیجه یک حمله سایبری باشد، اگرچه مقامات ایرانی هنوز علت را تأیید نکرده‌اند.
— خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17456" target="_blank">📅 13:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17455">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">در هر مقاله اش ۸ سوال از خودش میپرسد آخرش هم نتیجه ای می‌گیرد که معلوم نیست اساسا چه ربطی به سوال های بی پاسخ ش دارد</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17455" target="_blank">📅 12:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17454">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17454" target="_blank">📅 09:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17453">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">CNN
:
گزارش‌ها حاکی از آن است که ایران ممکن است زیرساخت‌های تونلی مرتبط با اورانیوم را تخریب کرده و به تله‌های انفجاری مجهز کرده باشد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17453" target="_blank">📅 09:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17452">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">— مقامات اسرائیلی به یدیوت آهرونوت گفتند:
«اگر حزب‌الله شهرهای شمالی را هدف قرار دهد، ما به ضاحیه بیرون ‌حمله خواهیم کرد و در آن نقطه، واکنش ایران را خواهیم دید.
اگر ایران در حالی که ضاحیه‌ را هدف قرار می‌دهیم به ما حمله کند، ما پاسخ خواهیم داد و اصل آتش بس در همه جبهه‌ها را نخواهیم پذیرفت».</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17452" target="_blank">📅 09:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17451">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اینفوگرافیک سنتکام از وضعیت تنگه هرمز:  تنگه هرمز برای عبور و مرور باز است  • مسیرهای امنی برای عبور کشتی‌های تجاری از تنگه هرمز ایجاد شده است.  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  • صدها کشتی در دو ماه گذشته…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17451" target="_blank">📅 09:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17450">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRS7e6K7o0D6E_-8cPB5WiVDaal67eFcZuaWcnJ86oklVWExjFS2RmUVYEyNtV3qKfPP2Ri160SJiwe5k55rvuSWAEFlVI4uDET_6801_mFvMt90AGIuMPI9L5a0YlG-NZLK32YZep90sZfHuGCD0IebO5BJnWXofKuVxOQsflNj5Z57OD9iIodr9BJFuK1OxqDCp2v1wE0QRGJHh5HhziGs6stzHkifGAKmk3L-6u8vwCISz5gWcX5yXi97D2s_jKhIAJxdYNopQvSCQAAXDRFORtZlSahtdw9NIEwnZ39wDVfJ1YEMZNODvYHvbAeozHruW-5TQnMnFAz0b2d53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی از دیشب تا کنون ۳ کشتی دیگر را منحرف کرده و از ورود به بنادر ایران منع کرده اند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17450" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17449">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKTbj-22zwMOl32UqeNfrfT85owubDnpqN0jYbeouLqhoFwrXGH3dEltrZhz2umh__Hjos7G0evkLU2IjlDYeIKdx0dEVApdKiSknFkO6-lsh-bwCKSJgmnayIja80IWOfWYmCRRBMMUF7rjbvXfIct6e1GCPgFwh429vQNzNBuRPk5M8V3OzRRZrTsg9B1AbQANIup_cFptureSs_SVP-njhgNX0UjUJlaMAir_a8iv-4QaN5dOTM-B9PfmBlLUU-Npsgd_-Ixs8GpxLr7rKH-5L1N2J1swNLnzIIDu39qEN3F-7ce3z1GSBUF9wQx_choZKoOSdvjHrcJHF1pJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای انفجار در تهران شنیده می شود</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17449" target="_blank">📅 03:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17448">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پس چه کسی پول ما را می دهد؟!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17448" target="_blank">📅 01:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17447">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امارات متحده عربی اعلام کرد هیچ دارایی مسدود شده ایران آزاد، منتقل یا از طریق این کشور جابه‌جا نشده است</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/17447" target="_blank">📅 01:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17446">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/17446" target="_blank">📅 00:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17445">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/17445" target="_blank">📅 00:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17444">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-BIBmFys8tgUlZ71Mck27AO-u4qZB1yWwQiBpXChyZc8JiL3wnupZhLdm1ck1_XX82VPyWo8Mf_FuoH3s52cAGiiZMqUowdtZ9MQ1e6_ux1vz8EY3KllNS8AxsR86hNmUj8qNCkusYzmYihBLmDMofIOqEJ0n_qwokImdHUTkd778R63En3rueZimOGDhhD5z4SHEbSEqHHF3-GUdpW7dnbbYjGoRW0IRySc8mGMR0oEiMw0Q3rKs8XzRI9SizEFsEPHPFE-Y3VbvvtRS-cfiy6u8w7P0lpRO45KngaD7XjGufRks7lHYQHxLneD52xtEJ8u-HjiNExcOEi17YMRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با Secret باش خدایی کن!  با Secret نباش فقط برگرد!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/17444" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17443">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVZmw5fwKt78B_ehuhJMT2jfDS_q5IsbVHbP7wSXmSrAhT_znODobzNRXazsoRiO30mI6X-ruxkYPztu6U0FX0XgAmk-8L1kIcoGtLJXtEg_vTAfkOE0uCNCaL3DMyuCZOBCa-1e3IxBfQBHbMpP5WJ45VbT7lj8sDN5qBXGjoUFlxxVvUUJ91TtHochuGWOBzR3JRoJeciBjpkcdGpAGK3_FrBryBTwFHwiTcoA1Rls5tOKTxM193bVSGAL_Il3_suGKl7a_8ZVfphPplXDkapzse2qE5DxkGG_fSVy_GJIsLrN4BbPv_2ih4EDefY78cNRJI5qNY2UTJgZu2dmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/17443" target="_blank">📅 23:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17442">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حسین الحاج حسن، نماینده پارلمان لبنان و عضو بلوک وفاداری به مقاومت وابسته به حزب‌الله:  «ما به وضوح از سوی ایران مطلع شدیم که لبنان در آتش‌بس گنجانده شده است. مقامات ایرانی به ما اطلاع داده‌اند که اسرائیل طبق توافق از خاک لبنان خارج خواهد شد.  ما هرگز بازگشت…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17442" target="_blank">📅 22:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17441">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17441" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17440">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سنتکام:  کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند.   تا امروز، نیروهای آمریکایی ۱۳۶ کشتی را تغییر مسیر داده و ۹ کشتی را غیرفعال کرده‌اند تا از رعایت این ممنوعیت…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17440" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17439">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slm2bQJ2Su2z7HF4sKvAD3-ld9OPmX6zyLFt1VwuY9DIqOXcfxFJGlDSbHOCzhMmoNLvIgCZFLlqynfKPD5idD41ufviEI4yzUta_ku8QByF4_LSCGWnHqQva6sDIDYnOHoA3JZsCMqRBTCc8oKAGvnH1ABtwKiug25-WhpzTw7Y7xg4aG6o9jSOrFAbJ3lzKAiOtkdQS5-y-ZR8RNek3SYnqD1Ar-1bsjuLNQcjfMx4be8MFKcGtrmhGrex6ayuylJPu0Co6y5qNDKbQpidszq5xXoVH87IlQmdFZZwi32m_Zk3NxEqUXPQuG1NPyI_CWi13DjzQeeM4PGIomu15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
نیروهای آمریکایی همچنان به اجرای دقیق محاصره علیه ایران ادامه می‌دهند. سنتکام از ۱۳ آوریل تاکنون ۱۳۹ کشتی تجاری مطابق با این قانون را تغییر مسیر داده و ۹ کشتی متخلف را از کار انداخته است.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17439" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17438">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">— وزیر امور خارجه پاکستان، امشب برای ادامه تلاش‌ها برای میانجی‌گری بین ایالات متحده و ایران به ژنو، سوئیس سفر می‌کند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17438" target="_blank">📅 21:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17437">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مثل این است که بگوییم شما نزنید ولی اگر لازم شد ما خواهیم زد!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17437" target="_blank">📅 21:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17436">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yei9CfLYNHNl1hvW81unocL3gM5N_WKZHg72Hr4gEGdy8_adyYAAU5uDiRiZVloh3dJzM4wTu5NL-RldwtAgdvGNIYLzZDuBFWTrgMKk1juyw86sg3r6VX_4ORTK6sXf7RKX3HrLxrKcV0GYE95XGGdZdZvMdgu4YBaCBNqvYokJROqBYBgLLJulKD3q-VkPaZ6A59fNpwV1xArKUIt0uAjbqhDfSk4oA-gxrFQ_vcNW69ZsLmJ5GMSdXJhLCrjuAzYvKPP0A_ydSMRoOnOsRtV0i3qpwPkFYyegNkksJmB6DR7BIHfHann10wDkrBKPivRFy9F8s-7GsjIkaIVKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17436" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17435">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:  ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17435" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17434">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:
ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17434" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17433">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مقام ارشد آمریکایی :   احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17433" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17432">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مقام ارشد آمریکایی :
احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17432" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17431">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17431" target="_blank">📅 20:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17430">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17430" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17429">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نیروهای  اسرائیل تا چند کیلومتری شهر نبطیه در جنوب لبنان پیشروی کرده‌اند و در انتظار تصمیم رهبری سیاسی هستند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17429" target="_blank">📅 20:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17428">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خداوکیلی راست میگوید!  الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!  پینوکیو با گربه نره و روباه مکار بهتر…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17428" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17427">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeGE6258tZc2Ym8UmavrRS7T2xunJdrZq5d66WvBHiHLZbq2KDBesiFWbAcQ13kTttVODi1mrmQecvuV7hWl-Ex35U0CQSY7rwJMCqGB07l2zHzjgHjSR4SAB5A536GHwEssvy_jG35SGaP2eKpIVDnfg4Xv47CxQrP0TIxCOvrczYiONlrljuNiiGYCs6FUT1JLu7UrykHTbCQIPJGUCcz1ySPz7fiki0u-qo4az9JYtciI5Iw_neUomnPTAxHjU4Lt8HX3-pr0fTrDj5fMd748bY9SfV_4bvrw8qLTX-lisHXW5p5QNNcjC4HeKUbbAl7X_NKvMzOBAVJQviAyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوکیلی راست میگوید!
الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!
پینوکیو با گربه نره و روباه مکار بهتر deal می کرد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17427" target="_blank">📅 19:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17426">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه  اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.  این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17426" target="_blank">📅 18:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17425">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه
اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.
این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به آن‌ها و کل منطقه خواهد رسید. این توافق پتانسیل بازسازی منطقه و ایجاد صلح پایدار را دارد.
در گزارش‌های چند ساعت گذشته چند نکته عجیب دیده‌ام. اول، افرادی که (به درستی) یک ماه پیش گفته بودند دونالد ترامپ رئیس‌جمهور تاریخی بود، اکنون بر اساس گزارش‌های رسانه‌ای تأییدنشده از توافق انتقاد می‌کنند. دوم، افرادی که می‌گویند نمی‌توان به هیچ کلمه‌ای از سپاه پاسداران اعتماد کرد، ظاهراً به پست‌های ناشناس در شبکه‌های اجتماعی باور دارند.
رئیس‌جمهور به هر حال نتیجه خوبی برای ما به دست خواهد آورد.
t</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17425" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17424">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbUf2FZi9MlR24VQvLeor_zroPMkNvOaq6wfNPNRWML0gwNxO8-pxGYQTSMP0qRaKarVePuG4YT-BXaifmT2G7Lq4ijBIcM-nzk5rUMlreBnRn329gx6stY0y6Kvv7PS14P60IZGWv7JfRALdVT-iAxKQX0962dfhFfMf7aGsMQujeOd1ildO5Z6p3rqHS3AeQnjr1SFg-eBAqtiynuFdkFjcDwlN5XHNR6d9WUCYNbywm78A7nuB13fvjyQ80ky4QCgDXMbnYWOKVrGMbQDYrySQ63-yKEAthgs0aNKhCa8DOmPZHMq8UOhk5uWdpTAgTqARafkt197qaGcPRW60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه دیدید یا نه؟!</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17424" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17423">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cttz_aNBfQqQy67kIVImt8fX9BTuV8GZNs8etDUvba7MZiW-NbHLctqCSqPgMQ2UefoZfaN115f27FbgcT-TlyA3w1iddlmp_NfYRJIifB_2EKNG_9WGmEnwc8t3aZdYf0XfuWTtgWLIr1AtUXXXZaxBH8w-VQn_tznGA_AVoYy_Fa3lrJLrrtckPyYGRt0NhA_NPCkqohMRLfLCPaa0uMv4bFiQj46GDKNRe3UJx7ZHl7Gl7UchnE_RVbh9BM13xeFF8rh8Dc3LpBBgwc9_fNj51PLfy9_IoxE6cg5CJRX1Uni6TVmP7eVkV9YdiNyadBxT6E8vatp7SmzWRRpV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17423" target="_blank">📅 18:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17422">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزیر خارجه ایران عراقچی:
تفاهم‌نامه اسلام‌آباد هرگز به این نزدیکی امضا شدن نرسیده بود</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17422" target="_blank">📅 18:26 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
