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
<img src="https://cdn4.telesco.pe/file/b0-U4v9vHM4d-LqL3F-o5sRPXb20BfPDCn0uMueNnyGvrByxwI1BQcJZgui74iJX_A-qcwPhOPHpSg9iNrbm_5B7ZdPwlnzh-FrCSvB4Ua24Xcf8kLjCOOsbFLaRoPEKvu6eqDpc1LvTJflgunhY1KWJslu32SpDUdCOeccjMHaMXRZVwmIbGW1h1OtYOpEo2BIKFNEkjbgb9JbRIQrdYUzu1gtKMylmBxcOZ_BEASrGV2qEfav2AmDRPFDG1u1HNgX69BQnrTCRVq2ldMwv8RkSr3uAOfteAEPPA2MRttBiwXXBzE8MPaw5EzjH7zvA8QKjnB4dA5o77r3syWr-CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 04:27:56</div>
<hr>

<div class="tg-post" id="msg-20384">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این چیزی که ما اکنون تجربه می کنیم عملاً نوعی «تجربه نزدیک به زندگی» است.</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SBoxxx/20384" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20383">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجار در سیریک</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SBoxxx/20383" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20382">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایران یک تانکر نفتی سعودی را در تنگه هرمز متوقف کرد.
بر اساس گزارش خبرگزاری فارس، یک تانکر نفتی بزرگ سعودی در حالی که از مسیر جنوبی تنگه هرمز عبور می‌کرد، متوقف شد.
ظرفیت این تانکر 2 میلیون بشکه نفت است.
طبق این گزارش، در حالی که این کشتی از تنگه عبور می‌کرد، ناگهان سیستم شناسایی خودکار آن فعال شد. فعال شدن ناگهانی سیستم AIS نشان می‌دهد که یا به این کشتی دستور داده شده بود تا موقعیت خود را اعلام کند، یا اینکه در شرایط اضطراری در تلاش برای اعلام حضور خود بوده است.
امروز، سازمان UKMTO گزارش داد که گزارش‌هایی مبنی بر وقوع یک حادثه امنیتی مربوط به یک تانکر نفتی دریافت کرده است.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/20382" target="_blank">📅 00:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20381">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">- یونان و اسرائیل در آستانه اجرای توافق‌نامه‌ای به ارزش ۳.۱ میلیارد یورو برای برنامه «سپر آخیل» قرار دارند که در آن سامانه‌های اسپایدر، باراک MX و اسلنگ داوید با زیرساخت‌های دفاعی موجود یونان یکپارچه خواهند شد.  این شبکه مبتنی بر هوش مصنوعی برای مقابله با…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SBoxxx/20381" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20380">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovrVLRQ9UGa0xGOLaN1BgQnEuxTT4DGm1zsiGTnWzkGEpa8Gk3xklqL8bRDOzjQXbR3-lEq5p1OvDlXXLimq8Ao_FzKBMpN2SxOkrKH7KyUX5il3ON1APH8xIEhpLRzaPJP5m0jQL5JWNshfzGfN_p91cOz9RPnEMGdM5JWDycW5uCtFtMIQXePZhLuWVFgPmSAmeEbg6YWrh8ckZegWQXBhMuAFplVBBV-NpLWibLbfmkmyGxv3b46QfYEMabuZnidfZLlmNXhPjqSC2rZgBxweMspkCVIiG2PnUmoh_tD_VMYTk_n3x4DGCzhE_ICX498d7FEJb_X7gU76Hes5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار رشدهای عالی را در طلا شاهد بودیم.</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/20380" target="_blank">📅 00:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20379">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش های اولیه از حمله موشکی آمریکا به یک نفتکش ایران در اقیانوس هند.</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/20379" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20378">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حملهٔ مسلحانهٔ عناصر پژاک به اهالی یک روستا در مریوان کردستان
در جریان این حمله، تعدادی از شهروندان محلی زخمی شدند.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/20378" target="_blank">📅 00:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20377">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/20377" target="_blank">📅 23:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20376">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKbPJbTQbqzL5cSstZkr56Px5qKX1JsfFSBl5skxwf2H7UkiwVbT7kf6vo9cxZmRJ3GGMY-46D4ffRneAI9JqY1Wx8f-C-U4L35foxvz_KhphH9Scfk0XBKJgaXDxJFUpFHuYpTcXAgcPvBa1TBX_xem7COfidFCOlYK15M3GwR6uee06x7JsWejtEYIIjxKQK-wm_yrthfcSZANZmZUurkXVCjCGBBvjm4cVtuiHipnrUuNQvFCgkgagQhxgSc5j8BBVVkfRbgAXLeaJ24a3_qRwPUnK6O7C8GWUNfIGpQ8FSNxA_vRbYVRRUZbuzbXQuNYvSmeC5kY0zWyYdkviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20376" target="_blank">📅 19:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20375">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دادگاه مرکزی کیفری عراق، امیر رحیم جبار لازم، عضو کتیبه‌های حزب‌الله وابسته به ایران، را به دلیل گروگان‌گیری روزنامه‌نگار آمریکایی شلی کیتلسون، بر اساس قانون ضدتروریسم به ۱۵ سال حبس محکوم کرد.
کیتلسون در ۳۱ مارس در بغداد ربوده شد و پس از حدود یک هفته، در ۷ آوریل آزاد شد.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20375" target="_blank">📅 19:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20374">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسکات بنت:
به دلیل محاصره، تنها 30 میلیون بشکه نفت ایران روی آب باقی مانده است - بنابراین حتی اگر آنها بتوانند از چین پول دریافت کنند، این مقدار تمام خواهد شد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20374" target="_blank">📅 19:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20373">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شمار کشته های حمله شب گذشته آمریکا در لارک به ۳ نفر رسید
خبرگزاری تسنیم:
در پی حمله شب گذشته آمریکا به نقطه‌ای در جزیره لارک، ۲ نفر به شهادت رسیدند و چند نفر نیز مجروح شدند. مجروحان این حمله برای مداوا به بیمارستان منتقل شدند که ساعاتی بعد، یکی از آنان نیز بر اثر شدت جراحات به شهادت رسید.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20373" target="_blank">📅 18:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20372">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«ایران تحریم‌ها را بسیار جدی گرفته است. رهبران ایران از وضعیت اقتصادی کشورشان شوک‌زده شده‌اند.
ما شاهد صف‌های ۳ تا ۴ ساعته در جایگاه‌های سوخت ایران هستیم.
ایران به دلیل از دست دادن توان اقتصادی خود، به اقدامات نظامی روی آورده است.
می‌خواهم از اتحادیه اروپا بابت حمایت آن از عملیات موسوم به «Economic Outcast» تشکر کنم.
خبرنگار: آیا بازه زمانی مشخصی برای فروپاشی اقتصاد ایران وجود دارد؟
بسنت: لازم نیست اقتصاد ایران فروبپاشد؛ فقط کافی است حکومت ایران به خود بیاید.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20372" target="_blank">📅 16:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20371">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سرتیپ ابوالفضل شکارچی، سخنگوی ارشد نیروهای مسلح ایران: صدها نیروی آمریکایی در طول جنگ کشته و هزاران نفر زخمی شدند
➡️
در این جنگ نابرابر، نیروهای مسلح ایران با استفاده از تاکتیک‌های جدید و نامتقارن در مقابل توانایی‌های فوق مدرن آمریکایی و صهیونیستی صف‌آرایی کردند و ضربات سنگینی به دشمن آمریکایی-صهیونیستی وارد کردند.
➡️
به عنوان مثال، هر زمان که یک پهپاد ۴۰ هزار دلاری ایرانی به سمت اهداف آمریکایی یا صهیونیستی پرتاب می‌شد، ارتش آمریکایی-صهیونیستی از چهار موشک به ارزش هر کدام ۴۰ میلیون دلار فقط برای رهگیری آن استفاده می‌کرد که نشان دهنده میزان خسارت مالی وارد شده به دشمنان آمریکایی-صهیونیستی توسط ایران است.
➡️
با وجود این هزینه‌ها برای آنها، پهپادها و موشک‌های بالستیک ایرانی همچنان از لایه‌های دفاعی آمریکایی و صهیونیستی عبور کرده و به اهداف مورد نظر خود در پایگاه‌های آمریکایی و سرزمین‌های اشغالی اصابت می‌کردند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20371" target="_blank">📅 16:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20370">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ به فاکس‌نیوز:
ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد!
ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20370" target="_blank">📅 16:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20369">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">میگویم اینکه خارج نرفتیم به این می ارزید که موقع برگشتن زیر تیغ «حافظه تاریخی» نرویم!
سبحان الله !</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20369" target="_blank">📅 11:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20368">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD7K9TuFqPPd63buoFVhGAZfXFQoVvVDGRvD5qzHe3wtJOsjp3n5fw8yWXGaZZeXczMfVOg4-IES-6jxr-hol_vl9HoCsbVN4_5q1zWmnvCWEE0xl0I6wITfdQVtY4CNMM0t6YsguiVQ4cQU3XivE8zemCFItpy30xu-7ZnFsIy7Nm2kJUYPV1bBPQ-NYg9POyM0PnPtkykmpJs3LuSQ3divnqx_0sBAaRC61TUdQR4n87eO9-lbK0Ql1fRcRQyfOXWdVwqX16MV_fDyITuO9XqRfLCVTZM7MFwp92J-FrV7VJIGIoesnbyLhjqIH07LMyQjSGc-upQAp5V1Zb6xJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20368" target="_blank">📅 10:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20367">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">امارات متحده عربی اعلام کرد که با یک پهپاد که از ایران به سمت آب‌های این کشور پرواز می‌کرد، مقابله کرده است.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20367" target="_blank">📅 10:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20366">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9mdvIx88l6v3fa7jQuDBP_Vaeq6Xqg0t6paYjYyu-QixPRJLBuPaMv_4dZXSlcAIGd9qYWfYSpUCpXn22EeZOB_UJ2thal9dznfKXypasg3IKwDGD_B5y_NRp91nfV31I7ygAPz1AXquypv5S9mx4x_AjAD2Y5bRmOoPLVcEsNCDzmq0g73iDCoRXbvF9ZITtU80NIgHwVciDSBJ5v-mC5v1n97q8FDUC3IdEj15WXRJpCJQgpfy9j2lJoGhtvohdNSqigJeAnQEyrVw4ymjlU-81vFS1Wd6GxS9CAilgJjcIXr0JdluOFZZl3yDxFHqopW75LPQ8XXrhPuK5yKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20366" target="_blank">📅 09:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20365">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔺
پایگاه آمریکایی «المنهاد» در امارات هدف پهپادهای ارتش
🔹
ارتش جمهوری اسلامی ایران، محل استقرار بالگردها و نیروهای آمریکایی در پایگاه «المنهاد» امارات را مورد هجوم پهپادهای انهدامی قرار داد.
👤
روابط عمومی ارتش:
🔸
از بامداد امروز در پاسخ به تجاوزات اخیر دشمن متجاوز و در انتقام شهدای دلیر سپاه پاسداران انقلاب اسلامی و مردم بی گناه ایران اسلامی در جزیره لارک، ارتش جمهوری اسلامی ایران، محل های استقرار بالگردها و نیروهای ارتش کودک کش آمریکا در پایگاه «المنهاد»  امارات را با شلیک دهها پهپاد انهدامی، هدف قرار دادند.
🔸
پایگاه المنهاد، یکی  از مراکز مهم پشتیبانی و جابه جایی هوایی نیروهای خارجی است.  روابط عمومی ارتش، با اشاره به تجاوز اخیر دشمن به جزیره لارک، اعلام کرد، رزمندگان ارتش جمهوری اسلامی برای تامین امنیت پایدار و حراست از سرزمین ایران اسلامی تا رفع تهدید دشمن از متطقه، ایستاده اند و انتقام خون همه شهدای جنگ تحمیلی را از نیروهای ترویست آمریکایی خواهند گرفت.
☑️</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20365" target="_blank">📅 08:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20364">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT01cubN4hDkulswatyBeoLNSWNJoRfslygyNZoP8ij4p3rJpVROjEOOapDWAm-ayUfdD4BXYADBotzh3OWpjZ9qrxqNgOqSDZQF63h89VPQhUMuBQs2Ef2-fzZGLPQvb7bg--Cx4AHvZtHuI0-hj58ZHbepqpaCeDOd3lU1YamdJv7ZM5vocs6IezR8UV6u-e61NBleT037QjEiAOrhS7V8Yquv5CZn67QW4bUnym1JKHH2FkwJvGvqZsZpIWRJAsrYlAujwfpKnZgNN4jCVQxhZ1bxzwKsfV2FI1Dzgx7WxwCcqKrnH_sROZ9DG5NPAhG3aEP10ZgVAOEnUG3dIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20364" target="_blank">📅 07:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20363">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ:
دور جدید عملیات نظامی ما در ایران تازه آغاز شده است</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20363" target="_blank">📅 02:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20362">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش هایی از حمله ایران به قطر</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20362" target="_blank">📅 01:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20361">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مدیر Secret Box بر این باور است که این تنش‌ها هنوز به جنگ نهایی موج ۵ ختم نمی‌شود و چند هفته ای دیگر زمان داریم.
لذا اگر تن ندارید لااقل آماده باشید.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20361" target="_blank">📅 01:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20360">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ادامه پرتاب موشک ها از ایران</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20360" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20359">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20359" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20358">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دلار ۲۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20358" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجار در جزیره ایرانی سیریک</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20357" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20356">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجارهای پی در پی در اردن</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20356" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20355">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20355" target="_blank">📅 01:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20354">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDHyzD_kH0yA-1uC_kKDacqUPFSmHzzH0vzHTjD1KTcs71nsTs6_9UyyI1TPQ0dFRk3wSCtctGacmgHZdihaxU9P_ifE18xKUKPQuf4v3W154QWZwTt-VM5YFZ68Neotps2FezdEfRK6__3v6h-OQVfgswvoQbzyejEt78CSa__QXKoXPoQXdUW132YTT-5ZaJcfcoe5aBPpbFvDGeLHnesuSRBd7zd71KW1s2C7gwBKgjnifrVEvBiODfYcCX6GwdfN2EbzGyVE3x3Qb3wU69sNp9BHlQMMzN5aTy5Im0a9PTP10zzW4dRSqsUUbotaD877zfRHpOZumbW_noh-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین کشورهای هر قاره جهان
بر حسب مایل مربع</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20354" target="_blank">📅 00:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20353">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U94g9zg9ajJd0W9_EXa05zZuFkNQhRUeXUws2Iw0leBHhQv7mrWAGhzpZ1u8UgsslR-YaNU3prwg6SZjWD7ORQTYfPjhsobZW9lVFlFSoFy94RJS0BVX9QBgTSDI11bFKPHoJpr_HPo-w5Qgo8joIW2BKseBckoJDtBVqyvRjbZGkVDncXUag7Da0hKwSRObqc7LkegGokmz1VHmusPxcTqPksG61pL18FSIWh2SYrftOlWJap3N77Eu_M5CTYJzsxFeUMesBCAg80PcXanXisSanKjcARZgMd0b7jzkgYry8VPowdg5hD9Jdkp_ZrvutiLSiPpZhIwLlW2w2bkEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20353" target="_blank">📅 00:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20352">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20352" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20351">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmrHLANX32XwBwjg4euDp6yk9htETleZAy-hd5JcjXApAKcKMJvWlx0R54fBDLIqwMsILlnzln5KrQWTjRAq5nOijWEjmLECPs8EsO_Kyczoz0HQU5Y_NnPe4KL66baMVOjB2_cgI18VvLFIFdV45V6voMNf0qnJkaQnObCrTvXtu7FHEdfd-8gJu-yuk3HvaSajnm4jzGKMd-c1w3_s9jTNroYos-Q8Sjt_9po5NHrvl1h1rb_basU2n9Rf14sm2yb_AX07CHu9kMHnritgDRIzwPkP96ECBXfEOwHLjAmmLaHD6OhJw6gzOlm3s59BvhWYx7D74XRHr5NufF0SRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20351" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20350">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20350" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20349">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اخباری دال بر شلیک موشک از مناطق مرکزی ایران!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20349" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20348">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اخباری دال بر شلیک موشک از مناطق مرکزی ایران!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20348" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20347">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">برخی منابع خبر از کشته شدن 70 نفر در حمله آمریکا می دهند که به نظرم اغراق آمیز است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20347" target="_blank">📅 23:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20346">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجار دوباره در جنوب کشور!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20346" target="_blank">📅 23:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20345">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20345" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وضعیت خریداران نفت در شرایط کنونی</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20344" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20343">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13228b50c6.mp4?token=XdbojnDRtTTySYXilozzgyiq1DSv7w5BQydf2unirJCTrr_IEd0zUf_64IkS9CdRDlJq7Z7D_0y-MaRW4PZUx8pMyb9EZikDLYVOU19JoaZcATZN4cX4_3WQIcAb73uYfkqEwJL0FurG4CMVcgAhhHhoCAeS4JJQ2bK2KIoo0LhigFXvyQcQReopE4aDq3pI02GYdWfTfCy9xmFSwwENrt30exESxoY5AUWLMCwfOER58RcPYw-BN30qPAa4Lz6qzfdlLDSDbdo1cbGLxc143QAwr6b_BnaAgFyBNZ2I6LaYCf8GGSSCr3o91tOKGQ8Mk-nNcarAV8wnfbIzPmAU0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13228b50c6.mp4?token=XdbojnDRtTTySYXilozzgyiq1DSv7w5BQydf2unirJCTrr_IEd0zUf_64IkS9CdRDlJq7Z7D_0y-MaRW4PZUx8pMyb9EZikDLYVOU19JoaZcATZN4cX4_3WQIcAb73uYfkqEwJL0FurG4CMVcgAhhHhoCAeS4JJQ2bK2KIoo0LhigFXvyQcQReopE4aDq3pI02GYdWfTfCy9xmFSwwENrt30exESxoY5AUWLMCwfOER58RcPYw-BN30qPAa4Lz6qzfdlLDSDbdo1cbGLxc143QAwr6b_BnaAgFyBNZ2I6LaYCf8GGSSCr3o91tOKGQ8Mk-nNcarAV8wnfbIzPmAU0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کانال نزدیک به جریان تندرو:  بر اساس آخرین اطلاعات دریافتی، نیروی دریایی سپاه و ارتش در کنار هوافضای سپاه پاسداران امریه‌ای بسیار مهم دریافت کرده‌اند.   این امریه که از دفتر فرماندهی معظم کل قوا صادر شده به یگان‌های رزمی در تنگه هرمز دستور داده است که حتی…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20343" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20342">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک کانال نزدیک به جریان تندرو:
بر اساس آخرین اطلاعات دریافتی، نیروی دریایی سپاه و ارتش در کنار هوافضای سپاه پاسداران امریه‌ای بسیار مهم دریافت کرده‌اند.
این امریه که از دفتر فرماندهی معظم کل قوا صادر شده به یگان‌های رزمی در تنگه هرمز دستور داده است که حتی اجازه عبور یک قایق ماهی‌گیری را هم از تنگه هرمز ندهند، هیچ مجوزی به هیچ طرفی داده نشود و هر طرفی که از دستورات صادره تخطی کرد، هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20342" target="_blank">📅 23:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20341">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چرا می خند؟!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20341" target="_blank">📅 23:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20340">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسمان ایران و منطقه  @Piknikanalyst</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20340" target="_blank">📅 23:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20339">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/csV-4FUvqdYwZUK8StRlm_UDEdNymbLozeCuvxjKBOwLW6CIpqnpokBXqSqjXhuLejgjUHo7yYOwUkGkwJXCrCz5-uIP49XpPdFqZfQmyvJvYCLcjDjDsTLLQtlWMGhJbP_lVwq_7XIPAW9zJpYIZiX36TCZ6G8n0sKJv6wUxNVhv5NXSUOqO73moQRGTWysF6cu5GcWE3_ADf1rhvRiDm-t8ln4DSGxtAimgWzGrN99BbwhwiEDtwznVAnu6BihrKDjJLgzMR2e9VahEn2jU5L0XbQurUEssFZlNkJn9-TVA2pSGkfr9JtgLoKPPmCj6VF0ujCigOeTTcKbrvXxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمان ایران و منطقه
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20339" target="_blank">📅 23:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20338">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سپاه: تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
روابط عمومی سپاه پاسداران انقلاب اسلامی:
دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی، در اقدامی تجاوزکارانه، با حمله به جزیره لارک منجر به شهادت و مجروحیت تنی چند از رزمندگان و هموطنانمان شد.
این اقدام توسط فرزندان ایران اسلامی پاسخ داده خواهد شد و تنبیه متجاوز را به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20338" target="_blank">📅 23:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20337">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuYOXGobF1xmE38RxYYfUb3f_FaUZNnGqfhV0Ak35d3Im_EAkz6W2nl1CyVd05Dg1PUbfk9NWGSnxVRo9SQQhizUMwGLxUt3AHJ_bkra8b_C1atTg-4O08xo7u3FFkPeQXDLqBanVZ7IRgFcoKwdXWwfv51liyuqEMG2pBdyLYeXPyfVAtCfYF0bcPjmUAoS0t6TKLcOsqC3mLPDPi2MHFOy9w56AZVaN7bdQxhOFAMqY9hRtGLFPlVl-sPzH1_HvZa7Ufz8bLqu52_hNrJImCkdTdGpJy5NrDRDtJ0mIgIfnD5UKYDL0hU99ACHlJmPA5rXhWw15R9FX_l37IUYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدافزارهای داخلی از آنچه می پندارید به شما نزدیک ترند....</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20337" target="_blank">📅 23:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20336">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مرندی :  رژیم ترامپ مرتکب اشتباه بزرگی شد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20336" target="_blank">📅 23:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20335">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این صوتی را عصر ضبط کرده بودم و اتفاقاً محور آن همین وضعیت سیال و پرنوسان خبری — خصوصاً برای یک ایرانی — است و جالب تر اینکه از مرندی (خریدار سنگین نفت و خالی کننده شبه جزیره عربستان) هم یاد کرده بودم...
برای هشتگ گذاشتن تاخیری حاصل شد و در همین فاصله دوباره جنگ شد و مرندی و ....
سبحان الله!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20335" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20334">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl7ZB0GOlPbaX7aZiUL8OKvTkZwam_ru8BnxXd-taQiK3ogNudEwn0M-_iDC-xpsj4viC9j0SAc3gAwdkrEF2vBhT6qDdb0sbxJcTmbzF0fMVg4N9MCbJqm6cvBJ3w4olt1DGlysG6KBN9kYsXLSznocn2oydIDxHj1E7PTCtSZ4s-9ETR2QnavqTcNjb5H7-GC1-EJ5oN9WUn5bVGdOC-uqQ8nnipnUo4VkjTRqswmDmnld4EIeOncOs5hffWGJHBBtodgQfEK0ngPCcheI577XBpoLTBVBjqsWn8fcFzAraIrh2g7NLsZ6zihRYxiGfQdhQhJsZQ836GhchSSE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرندی :
رژیم ترامپ مرتکب اشتباه بزرگی شد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20334" target="_blank">📅 23:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20333">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رسانه عراقی به نقل از یک منبع ایرانی:   شهادت شماری در پی حمله آمریکا به جزیره لارک در جنوب کشور</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20333" target="_blank">📅 23:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20332">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال Secret Box بی تردید ناهمگن ترین کانال سیاسی فضای فارسی زبان تلگرام است!
از بسیجی مبعوث شده کف میدان تا شاه اللهی مخلص اسرائیل اینجا هستند!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20332" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20331">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خب گویا لارک بوده نه خارک!  مقام آمریکایی به شبکه الجزیره اعلام کرد:    نیروهای این کشور امروز به یک پرتاب گر موشک در جزیره لارک حمله و آن را نابود کردند. مقامات آمریکایی اعلام کردند این سامانه آماده شلیک موشک به طرف تنگه هرمز بوده است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20331" target="_blank">📅 23:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20330">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2967016a4b.mp4?token=QuCkwueOqjaOyJivxkRkGrJ_VGUU2jl59y8O7h5RnJnf5HaHC8r2Jy5ZSldH4nMWhSczZdo_bOpmSH-P1-ULsREbjP8iPJ9afriJtzTAd9OKUhZko6IlrgrCkbTkA9EUOSfEo2qS6A_m1AZFIoK5KyeD4nSaCwaC1eQYdNRYHuOr7Tx0Wan7FwP6ePHD6HNsBmAGbylS_t8I9m3VpZjhnm2_vSP9LAaxtsP8DQVa8Nq67IIDgUiWkZMq9ewtL1Aqhiz0TCsY9jVC6tRwZLHT9I80oQcUGgg_vRd8luKzM_1AKmW-L-bB1eIUuHT8J5NsRcin7gJg_wcSFJyfwMNtAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2967016a4b.mp4?token=QuCkwueOqjaOyJivxkRkGrJ_VGUU2jl59y8O7h5RnJnf5HaHC8r2Jy5ZSldH4nMWhSczZdo_bOpmSH-P1-ULsREbjP8iPJ9afriJtzTAd9OKUhZko6IlrgrCkbTkA9EUOSfEo2qS6A_m1AZFIoK5KyeD4nSaCwaC1eQYdNRYHuOr7Tx0Wan7FwP6ePHD6HNsBmAGbylS_t8I9m3VpZjhnm2_vSP9LAaxtsP8DQVa8Nq67IIDgUiWkZMq9ewtL1Aqhiz0TCsY9jVC6tRwZLHT9I80oQcUGgg_vRd8luKzM_1AKmW-L-bB1eIUuHT8J5NsRcin7gJg_wcSFJyfwMNtAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20330" target="_blank">📅 22:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نتانیاهو :
طبق اسنادی که به دست آورده‌ایم ایران بار دیگر می‌خواهد برنامه هسته‌ای خود را از سر بگیرد و بمب اتم تولید کند و ما قبلا هشدار داده بودیم که اگر ایران برنامه هسته‌ای یا موشکی خود را دوباره شروع کند ما به آن حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20328" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20327">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اخبار تایید نشده از حمله هوایی آمریکا به جزیره خارک!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20327" target="_blank">📅 22:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حمله ایران به یک کشتی بحرینی در خلیح فارس</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20326" target="_blank">📅 22:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20325">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اخبار تایید نشده از حمله هوایی آمریکا به جزیره خارک!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20325" target="_blank">📅 22:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20324">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سناتور تد کروز:
چیزی که من خواستار آن هستم این است که رئیس جمهور ترامپ و دولت او معترضان را مسلح کنند تا مردم ایران بتوانند این کار را انجام دهند، کردها را مسلح کنند و به معترضان اجازه دهند این حکومت را از قدرت سرنگون کنند، نه با نیروهای آمریکایی در میدان، بلکه با مردم ایران.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20324" target="_blank">📅 21:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20323">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل طرحی را برای سرنگونی نظام ایران تدارک دیده است. در راستای این آمادگی‌ها، هزاران نیروی کرد به اسرائیل منتقل شده و سناریوهای عملیاتی مختلف را تمرین کرده‌اند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20323" target="_blank">📅 21:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20322">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سازمان رادیو و تلویزیون اسرائیل:
شناورهای جنگی ترکیه به کشتی‌های نیروی دریایی اسرائیل نزدیک شده و برای آن‌ها مسیرهای دریایی مشخص کردند.
نیروی دریایی اسرائیل سطح آمادگی خود را به منظور مقابله با هرگونه تحولی در دریای مدیترانه افزایش داده است.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20322" target="_blank">📅 21:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20321">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20321" target="_blank">📅 17:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20320">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20320" target="_blank">📅 15:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20319">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315342d71a.mp4?token=kdET3skpzqOseJIiacCeHNcl2c9K1qd5p9aPWuoaS4dP3G3GCMfWmGh2AD5lYGjaLaMLbTNltxebjtot6_hqaMxu9OhMWS5PoeqXKOqUiCPZ7J-X24MOaoAKBCazX3pq3Q_DDZSt9lqkNuAIHqjCdj4zY9ov662k_xCzDrJW-PrRh7IU1mhnGBt98yCSGezebijH2vzSb3K5U1fxsq_4w_hyVjyfdZwB4GaPf6uFUc1_0fmlJYGXVdp6Ujd6rcZpEt9jSre-Rmo8FALJi0hPTEGyQirsg3lDsPjsPYQT0Xr-RmVZuZvBOXhrwg_ZPKqKsSVUd18YuB5GHjLhVnFyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315342d71a.mp4?token=kdET3skpzqOseJIiacCeHNcl2c9K1qd5p9aPWuoaS4dP3G3GCMfWmGh2AD5lYGjaLaMLbTNltxebjtot6_hqaMxu9OhMWS5PoeqXKOqUiCPZ7J-X24MOaoAKBCazX3pq3Q_DDZSt9lqkNuAIHqjCdj4zY9ov662k_xCzDrJW-PrRh7IU1mhnGBt98yCSGezebijH2vzSb3K5U1fxsq_4w_hyVjyfdZwB4GaPf6uFUc1_0fmlJYGXVdp6Ujd6rcZpEt9jSre-Rmo8FALJi0hPTEGyQirsg3lDsPjsPYQT0Xr-RmVZuZvBOXhrwg_ZPKqKsSVUd18YuB5GHjLhVnFyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتتاح یه خط فاضلاب
به مناسبت هفته دولت
اوج خلاقیت
فقط اون روبان قرمز روی شیر تانکر
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20319" target="_blank">📅 15:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20318">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kizQdZxV87-oDedc2qx0McE5DPoMzHyFQTVxwEEpoCxvkgRpGkM9Ei7HipUUtVKoCysyIVu-FtiNolTCJFrVO5OZzKDtoYeo5C4jXctmCxEXxBWhjZPdn6I3NA8HJj5WQivkfh7RvV1jLw6-yjtzEFSy5LJPzWE0bA-S-QZDQSqgutiL5Wr-a9cFn4EzrQIm6A7hywFi9fx-693vhkXqGi65zCwD4CR-pMRo9mhMjxOcOM4zZVJvXPlzALW6hbpFHEj24kEbwoZjP80O4BFK77q8rnL_HJI0Qn5Agd0Cwo27jKFpiKgoKGyFaKkes2vpkkCW2WXY9h11d6m2-BYzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور سرباز وظیفه در درگیری مرزی در پاوه
مهرداد طاهری آرپناهی، سرباز وظیفه اهل شهرستان کوهرنگ چهارمحال‌وبختیاری، در جریان درگیری با اشرار در منطقه مرزی پاوه ترور شد.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20318" target="_blank">📅 15:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20317">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عراقچی:   ژاپنی‌ها آمریکا را بابت جنایاتش پاسخگو کنند</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20317" target="_blank">📅 12:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20316">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بیکاری هم بد دردی است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20316" target="_blank">📅 12:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20315">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فوت ناگهانی، هنگام سخنرانی شبانه!
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد حین سخنرانی شبانه فوت کرد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20315" target="_blank">📅 12:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20314">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20314" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20313" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=ABr0cRxXA0L031Rp_JsUU3PXlaYKnFy4lryZm7bM688lvFlWlwgwyTttgUPLcTW0ArEiq1k2H90qa9DbrHSbIDplEe3ZUjZBuguDxUlM0va779rFN9pLbhj_6sSqeFp0tt9Ikl0GyJAI7cAFVjXgYGUa1WQ9ANKc8dOIfndKggSwJZUCPow6jymGiIFIZ18hdOAEVhERtgLudvIHqc15bYr6_bNCGwz249dcGZDBmpmvYcxEFeB5LcZOFNq2sbybLoza_w-HPSVvsEskuCWoOnSqo_Xca2HXCayM8FWeflAUxoPSEu147wPZHqW87hC73fFtGrGn8XPmFywIVwLb5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=ABr0cRxXA0L031Rp_JsUU3PXlaYKnFy4lryZm7bM688lvFlWlwgwyTttgUPLcTW0ArEiq1k2H90qa9DbrHSbIDplEe3ZUjZBuguDxUlM0va779rFN9pLbhj_6sSqeFp0tt9Ikl0GyJAI7cAFVjXgYGUa1WQ9ANKc8dOIfndKggSwJZUCPow6jymGiIFIZ18hdOAEVhERtgLudvIHqc15bYr6_bNCGwz249dcGZDBmpmvYcxEFeB5LcZOFNq2sbybLoza_w-HPSVvsEskuCWoOnSqo_Xca2HXCayM8FWeflAUxoPSEu147wPZHqW87hC73fFtGrGn8XPmFywIVwLb5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20312" target="_blank">📅 01:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=DDYqMk7V5V2x2D3slxkCZPWgnt_ATm4ARHDFCPmWtuAl_4Im57eZIwYi8cOTYIF5FINQrx6dJHVAn5vdwhXzUrRy5P9Zcm1jRVLZsZvkw2OrSMDN69UJfsZjF2btTWJPPDLjhtbMxZBrE1WtfxMRVnZQpFN1Qn0uSaDBUptR0-vbTaoc6eDsNURYZZQ5HzIDd7lvRtMTQh21p7-gR3Ni1D1R94I6LT6vY0aIwHkVAAAx9YVGyNdUMDoPu-5ZM8zebtmZWgLL_Eui-ct63wXhAVzQ04pM_ESYLoho0DN7i6Bqffi3217gTDvS482JgMLR3ztt39t_ScU7ys0UvyW9nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=DDYqMk7V5V2x2D3slxkCZPWgnt_ATm4ARHDFCPmWtuAl_4Im57eZIwYi8cOTYIF5FINQrx6dJHVAn5vdwhXzUrRy5P9Zcm1jRVLZsZvkw2OrSMDN69UJfsZjF2btTWJPPDLjhtbMxZBrE1WtfxMRVnZQpFN1Qn0uSaDBUptR0-vbTaoc6eDsNURYZZQ5HzIDd7lvRtMTQh21p7-gR3Ni1D1R94I6LT6vY0aIwHkVAAAx9YVGyNdUMDoPu-5ZM8zebtmZWgLL_Eui-ct63wXhAVzQ04pM_ESYLoho0DN7i6Bqffi3217gTDvS482JgMLR3ztt39t_ScU7ys0UvyW9nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:
به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20311" target="_blank">📅 01:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAlzsF4bWwcZ0XJ5CAK8n_w0xiTiH1uvOMzK-mPYcwN0unkukaNf71csBBrwvaBUoHkYDYOfyzg8reV_HNeD8HgnMJ7Zw2AnXp17vDB9SgYxfC8xHPQjAcZ-CUeG7nCPzQKsrs_Hw149i5QvyrbB-G5uAlO0SzFEYDYa0hOJPGqvbJ80C-Bxb708DNqmUtfDcc5dpI0KB4H3_AJFc_Lg4HLlXBdhXFwO4YT56t5g1g0jq5VRHUxLE1orAmxGSCIHF_b4HTZJLDFr9pfnwx2Q1W5U1TnLvUYt91IPd2to2Z6iZWzaA9H5Q4LjOv2jeTTHwvHJpDh_AmwnMpwd9LLmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20310" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20309">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند  وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.  و آن درس چه بود ؟  ترس ها برای ایستادن در…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20309" target="_blank">📅 23:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند
وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.
و آن درس چه بود ؟
ترس ها برای ایستادن در برابر شیطان بزرگ ریخته شد .</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20308" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">غریب‌آبادی:   هیچ کشتی‌ای بدون هماهنگی با ایران نمی‌تواند از تنگهٔ هرمز عبور کند   تنگهٔ هرمز کاملا بسته است و اگر کشتی‌ای از تنگه عبور کند قطعا با هماهنگی و مجوز ایران است.  نیروهای مسلح ایران کاملا بر هرگونه تحرک در تنگهٔ هرمز اشراف دارند و به‌هیچ‌وجه ادعاهای…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20307" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20306" target="_blank">📅 22:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20305">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌سرلشکر رضایی:  ضاحیه و بیروت خط قرمز ماست و هیچ‌کس حق ندارد به‌سمت بیروت و ضاحیه حرکت کند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20305" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBgVZvL9TwJaORQA1YU00IcrTKS6E0CrUROOh8BFkJ2QUYiWziyjmTD8MK_mSzJnFvjZB5KLIQrOVwGEB7T1EGUmlk9j1Do4dTHkVkl4NMXHaxN2j438sCjpzZZZjTMaNlG1MOPJgGuxGYrTFzk8xgn0ygcL3VoGR9ep6IAxSvorLWNVTGD9nErCBiWzJdpBoU0Wc7wehHGxhYFQnAtRuflrc_Rr-GPfXSvkuLrAgulZg4kNPFUduQX5CJ7_-9upJvIfOPysqz4Fraq0alFVyfUaWtRflfYkmv18UeJ9TUZ4CREgZa3uSy_A_qxsb5R9fN9dWHbtJ6qTvdXunECU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه هشدار داده است که در پاسخ به حملات اوکراین به اهداف داخل روسیه با استفاده از موشک‌های کروز بریتانیایی، ممکن است به اهداف نظامی بریتانیا داخل و خارج از اوکراین حمله کند.  این هشدار، قوی‌ترین هشدار از این نوع تاکنون از سوی روسیه بود که توسط ماریا زاخاروا،…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20304" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20303" target="_blank">📅 18:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOlIkTp17zJHr5AgTlX_om68vYbdJljr_sHAKWCpq7WeMMbugHv1W2g7w8gXaVvvYli5bp5MMjEKYOK2mCFD9u8R3b_ublRKfagTCI7OmPSjn19nH2-G4ZUbO2LzNP7MHwirsLiEHhqoFTA0bfT5lCIBAuytRJHweFtY-s4uqFFUvlbb6seZyjm270G_xjAm83Fvvff_Qiy_z47gf6Uv1CpPqP4FKVCN4PRJx7ao6DgdTWr9IvbUSaHcJgQ98w2v9QVtxrWDBda9jADRIRJ7sZLh498Xn7d4o5wAYHdtqaYqLuTeBZzxfAJUpodoIgHOyFz1ASMP_FZPNkoVe1jb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!
علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20302" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20301">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تحلیل اسرائیلی: اتحاد اسرائیل و یونان  بازدید رئیس ستاد مشترک نیروهای مسلح یونان از اسرائیل، اهمیت راهبردی روابط نظامی بین این دو کشور را برجسته می‌کند. با توجه به افزایش تنش‌ها بین اسرائیل و ترکیه، این همکاری اهمیت بیشتری پیدا می‌کند.  احتمال صادرات تانک‌های…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20301" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏پزشکیان:   اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.  با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20300" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏پزشکیان:
اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.
با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20299" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20298">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20298" target="_blank">📅 15:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20297">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqhhAugHR-uYd8Ouj-eMYHf5taKZL8HOpJcCLivdSvLaL0TMZ6WJ0Rcov7nrvbCyvsO7puAp59u2rF-llVQGgQlkmpWAUbKHSjMV7kJtoLfhAG_VdODqRwzw8iHjXo4cmG0U2s5LA21bWm-2FCfwb4WKzHy6iW3_8ImVV7TxQsEcdRlvpRsZSWDNhmcghLWsxOzTOalXGX61O1XNjbysbM3_YQe99r7kYQXLC2Us96ENdqJ2W0uUk4IAHi9NbkU8yU7z8dh3uBFRYv-ZeGo3b1-Lb4O2u9z-Ml29nVChZNS5HT2ZhjQQpIC1wRIebI8FWAOWKd0eNBMPe30m-YGU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20297" target="_blank">📅 15:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20296">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20296" target="_blank">📅 14:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20295">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20295" target="_blank">📅 14:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAyR6ISZs_wPrpnxNR8q_oXXM8CKAQJ_UWGMpie4rJ6XraesEAqm_cyE0UPXpQuuu_HfBr38cJKDRfrmP1XTxdjUTYkyfSAbviVHOQG3sJgeyDSwgu4X7Uuvf3JEkrM81_7Y2jH7vwsT3nHselgCVYrmGNVdI5-20MZg-0D8nzyDQxeHtP8QOgGe3t2aSey_2bG6l6TbQUZGqYRxCd77gY9kbphdd0J1bBbeBg_mb8gYzVkf11YikFF7pl1AGu7L4HTfwZpdldzH_t799CpYSPOdftzL5s4-mX46dExPP_cE-OONKtEg__LpO6NRoj1ktt5D-dmW-Dqz5VRl1lAfFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20294" target="_blank">📅 13:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20293">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=muvvEHuUZ1S1Q8_9a2HxTvbYybboG7Alvu1Nlz7vTtu1GzOh3Pf6Fz2b3JKrUrSGZ_iuFHWakU3Vg_Wt6WfvyH0TKViF3dpijYpOT4buF7VEv09l9BvHYERIzPa7L2w2Z5MVL80wHxnNU1GpdeJ1_fDO3OP2YU4c8BM7yjpbgSJncAzDxX9dhAiuxoOTR_lkZ6WH2QfQyVkJKOaTBu1O2xrslyo7wnGQev4GyL4EYeS5YFgCzmkTtV7TeZGRv0TPAlnIG0SiaBljZcDTMRwUi7WmSrzRnxbgdTGVEhZtoRsM1L8ThgkHS6K9dM8Tv3rhCI_0j4sRGE7i_djIJoF0vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=muvvEHuUZ1S1Q8_9a2HxTvbYybboG7Alvu1Nlz7vTtu1GzOh3Pf6Fz2b3JKrUrSGZ_iuFHWakU3Vg_Wt6WfvyH0TKViF3dpijYpOT4buF7VEv09l9BvHYERIzPa7L2w2Z5MVL80wHxnNU1GpdeJ1_fDO3OP2YU4c8BM7yjpbgSJncAzDxX9dhAiuxoOTR_lkZ6WH2QfQyVkJKOaTBu1O2xrslyo7wnGQev4GyL4EYeS5YFgCzmkTtV7TeZGRv0TPAlnIG0SiaBljZcDTMRwUi7WmSrzRnxbgdTGVEhZtoRsM1L8ThgkHS6K9dM8Tv3rhCI_0j4sRGE7i_djIJoF0vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20293" target="_blank">📅 11:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20292">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd2g6UQ6X-opNHg1M953Dou1N9_rdtJsDTc3PuHcQXBYe-bT6F9P23Vl8riO9j_UXm3JSRkWHAZ-ASa4fod6-ecTI1E9FUMD-wmxn7sqV-ge136D-ATIOkK8slZS8elqyPpQF6Nc3v7IE8SgRTqJPJx-FCz-p5ILzuy4u0u5lwOpPwWSrcnhnQ9wARhuGfAg0E_7xe47-0JF5Exu9LoAiZqkqepFeKeAaggRdZz9FHX8uSenWfHLyyEEng52ZCObVFk0hYIt9uWZTBjmVz_bSEVKmd1jzDmjaGquriFGpDKJb16L4ecc3aQ3YBj8ln398NIx69BGK73ymDhE-bR8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
مواضع هاوکیش کوین وارش در نشست جکسون هول
مواضع هاوکیش کوین وارش در جکسون هول نشان داد اگر تورم با سرعت کافی به هدف ۲٪ نرسد، افزایش نرخ بهره همچنان روی میز است و فدرال رزرو لزوماً مسیر کاهش نرخ را ادامه نمی‌دهد.
بازار نیز این پیام را جدی گرفت؛ احتمال افزایش نرخ در سپتامبر از ۳۵٪ به ۵۶٪ رسید که می‌تواند به رشد بازده اوراق و دلار و افزایش فشار بر طلا و دارایی‌های پرریسک منجر شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20292" target="_blank">📅 10:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20291">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ:
ایالات متحده قراردادی با ونزوئلا امضا کرده است که به این کشور کنترل بخش عمده‌ای از ذخایر نفتی تایید شده، که بیش از 65 میلیارد بشکه است، را می‌دهد، و این کار بدون هیچ هزینه‌ای برای مالیات‌دهندگان آمریکایی انجام می‌شود.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20291" target="_blank">📅 10:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شلیک های متعدد در تنگه هرمز!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20290" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkdpJAqsSao_Li0Lavk3GVtrYSG3EnfoXUire8hEoPvGvngtEkznVHTHTvSWMhoruNw-DXj5xKo6Cbw7BGavYe2U5g4z9aKp4lyIReTAAt5Y-Qjf8eEDGjGBA9jpxLRTK-ds1y1yI8sgmgUi3dlNdZQgFolOG4_QEpVEOTQGzjM0aPmW_pynAFdduo-2V6JCn3xcLIJhdF9F-EbrD53EsNGFk5SQSxIU_whSzcuigHZXnQ9592lTKFle0eOsQJ6nEbuas54No3H_ApujRg-sB2Ol_rVNkciW7caN1w7GtlhKYcetJFntpkwOjSdVyVJM95urCqcKmRQ71otkv5IKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحول در پدافند لیزری اسرائیل  و تغییر احتمالی معادله بازدارندگی ایران
گزارش اخیر درباره پیشرفت‌های شرکت البیت اسرائیل در توسعه سامانه‌های لیزری، صرفاً یک خبر فناورانه نیست؛ بلکه می‌تواند نشانه‌ای از آغاز یک تحول راهبردی در موازنه نظامی خاورمیانه باشد. سامانه پدافندی پرتو آهنین  Iron Beam تاکنون توانایی خود را در مقابله با پهپادها و برخی تهدیدات هوایی به نمایش گذاشته و اکنون مهندسان اسرائیلی آشکارا از چشم‌انداز گسترش این فناوری به حوزه رهگیری موشک‌های بالستیک سخن می‌گویند. اگر این هدف محقق شود، ایران با یکی از جدی‌ترین چالش‌های راهبردی تاریخ معاصر خود روبه‌رو خواهد شد.
اساس قدرت بازدارندگی متعارف ایران در دهه‌های اخیر بر زرادخانه گسترده موشک‌های بالستیک و کروز بنا شده است. تهران به دلیل محدودیت‌های ناشی از تحریم‌ها و برتری هوایی رقبای منطقه‌ای، سرمایه‌گذاری عظیمی روی توسعه موشک‌های دوربرد انجام داده است. این موشک‌ها نه‌تنها ابزار حمله، بلکه ستون اصلی بازدارندگی ایران محسوب می‌شوند. در واقع بخش مهمی از محاسبات امنیتی ایران بر این فرض استوار است که در صورت وقوع جنگ، حجم بالای شلیک موشک‌ها می‌تواند سامانه‌های دفاعی دشمن را اشباع کند.
اما فناوری لیزری دقیقاً همین منطق را هدف قرار می‌دهد. تفاوت اساسی میان رهگیرهای موشکی متعارف و لیزر در هزینه و ظرفیت درگیری است. هر موشک رهگیر سامانه‌هایی مانند پیکان Arrow یا فلاخن داوود David's Sling ده‌ها هزار تا چند میلیون دلار هزینه دارد، در حالی که هزینه هر شلیک لیزری در مقایسه بسیار ناچیز است. به همین دلیل، اگر اسرائیل بتواند لیزرهای پرقدرت را برای مقابله با موشک‌های بالستیک عملیاتی کند، دیگر مجبور نخواهد بود برای هر تهدید از یک رهگیر گران‌قیمت استفاده کند.
اهمیت بیشتر این تحول در پروژه لیزرهای هوابرد نهفته است. برخلاف سامانه‌های زمینی که با محدودیت افق راداری و شرایط جوی مواجه‌اند، لیزرهای نصب‌شده روی جنگنده‌ها یا هواپیماهای ویژه می‌توانند در ارتفاع بالا به موشک‌های مهاجم نزدیک شوند و آنها را در مراحل اولیه پرواز هدف قرار دهند. چنین قابلیتی زمان واکنش را افزایش داده و احتمال موفقیت دفاع را بالا می‌برد.
البته هنوز موانع فنی مهمی وجود دارد و هیچ تضمینی نیست که رهگیری موشک‌های بالستیک با لیزر در آینده نزدیک به واقعیت تبدیل شود. اما اگر اسرائیل از مرحله مقابله با پهپادها و موشک‌های کروز عبور کرده و به رهگیری مؤثر موشک‌های بالستیک برسد، بخش بزرگی از مزیت راهبردی ایران زیر سؤال خواهد رفت. در آن سناریو، تهران ناچار خواهد شد برای حفظ بازدارندگی خود به دنبال راهکارهای جدیدی باشد، زیرا ستون اصلی قدرت متعارفش دیگر همان کارایی گذشته را نخواهد داشت. به همین دلیل، موفقیت احتمالی دفاع لیزری علیه موشک‌های بالستیک را می‌توان یکی از معدود تحولاتی دانست که قادر است معادله بازدارندگی میان ایران و اسرائیل را به‌طور بنیادین تغییر دهد.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20289" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">منابع اطلاعاتی سعودی اعلام کردند تا ساعات آینده، گروه های مقاومت عراقی به عربستان حمله می‌کنند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20288" target="_blank">📅 02:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خلاصه
یادداشت الجزیره | تحریم‌های جدید آمریکا؛ تلاش برای خفه‌کردن شبکه اقتصادی ایران، بدون ورود به جنگ مالی با چین
موج جدید تحریم‌های دولت ترامپ علیه ایران را باید فراتر از یک بسته تحریمی معمولی دید. وزارت خزانه‌داری آمریکا نزدیک به ۶۰ فرد و نهاد در ایران و چندین کشور دیگر را هدف قرار داده و تلاش کرده است شبکه‌ای را که به تهران امکان
فروش نفت، انتقال پول، خرید فناوری و تجهیزات، حمل‌ونقل و دور زدن تحریم‌ها
را می‌دهد، همزمان تحت فشار قرار دهد. اسکات بسنت، وزیر خزانه‌داری آمریکا، این عملیات را بخشی از راهبرد «خفه‌سازی اقتصادی» ایران توصیف کرده است.
نکته مهم این تحریم‌ها،
ماهیت شبکه‌ای آنها
است. آمریکا به جای تمرکز صرف بر شرکت‌های ایرانی، واسطه‌های خرید در چین و هنگ‌کنگ، شرکت‌های لجستیکی، کشتیرانی، شبکه‌های موسوم به «بانکداری سایه»، شرکت‌های مرتبط با تجارت نفت و حتی برخی فعالان ناوگان سایه ایران را هدف قرار داده است. این شبکه اکنون از ایران تا چین، هنگ‌کنگ، سنگاپور، امارات، سوئیس، مالزی، بریتانیا، فرانسه، یونان و چند کشور دیگر امتداد دارد.
هدف اصلی واشنگتن، افزایش هزینه هر مرحله از تجارت خارجی ایران است؛ به‌گونه‌ای که فروش نفت، انتقال درآمد، خرید تجهیزات و جابه‌جایی کالا برای تهران دشوارتر و پرهزینه‌تر شود. به‌خصوص شبکه‌های خرید فناوری دوکاربردی مورد توجه قرار گرفته‌اند؛ شبکه‌هایی که به ادعای آمریکا از شرکت‌های پوششی و واسطه‌های شرق آسیا برای پنهان کردن مصرف‌کننده نهایی تجهیزات استفاده می‌کنند.
اما
بزرگ‌ترین نقطه ضعف این استراتژی چین است.
آمریکا چند شرکت چینی و هنگ‌کنگی را تحریم کرده، اما از هدف قرار دادن بانک‌های بزرگ چینی که در تجارت نفت ایران نقش دارند، خودداری کرده است. این تصمیم اتفاقی نیست. چین بزرگ‌ترین خریدار نفت ایران است و اعمال تحریم‌های ثانویه علیه بانک‌های بزرگ این کشور می‌تواند پرونده ایران را به یک بحران مستقیم مالی میان واشنگتن و پکن تبدیل کند. بسنت نیز صراحتاً گفته است که نمی‌خواهد با این اقدامات «سیستم مالی جهانی را منفجر کند»
بنابراین،
مرحله بعدی تحریم‌ها تعیین‌کننده خواهد بود
: اگر آمریکا به سراغ بانک‌ها، پالایشگاه‌ها و خریداران بزرگ چینی برود، فشار بر ایران می‌تواند جهشی شود؛ اما همزمان خطر تقابل اقتصادی با چین نیز افزایش می‌یابد. اگر واشنگتن از این مرحله عقب‌نشینی کند، ایران همچنان می‌تواند بخش مهمی از نفت خود را از طریق شبکه‌های واسطه‌ای به چین بفروشد؛ البته با تخفیف بیشتر، هزینه انتقال بالاتر و درآمد ارزی کمتر.
در واقع، این بسته تحریمی نشان می‌دهد آمریکا تلاش دارد
تمام شریان‌های اقتصادی ایران را باریک کند، اما هنوز از قطع مهم‌ترین شریان ــ چین ــ پرهیز دارد.
همین مسئله احتمالاً سقف واقعی کارزار فشار اقتصادی جدید علیه تهران را تعیین خواهد کرد.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20287" target="_blank">📅 01:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">البزشکیان:
من میخواستم مردم بیان تو صحنه
و اصلا ریاست جمهوری تخمم نبود.
ولی حالا خودم اومدم تو صحنه
و مردم به تخمشون نیست.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20286" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پزشکیان:
اگر تحریم ادامه پیدا کند، گرانی افزایش می‌یابد</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20285" target="_blank">📅 23:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا دقایقی پیش از اعمال تحریم‌های جدید علیه ایران خبر داد.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20284" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
