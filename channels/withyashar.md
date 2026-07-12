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
<img src="https://cdn4.telesco.pe/file/KvRRoHMgctw-ifpnNZYr_KLKb5rpm2pTmX66vDC0J0qK6iRlWdtDeLzwgBjF7fiNfyheALMoGH4YtyQXF0INRppfl3cAeXBiPIXTy-FeZuT4Akf4XCwi2YUJQF-pQtCzVxZNGVR9T_dWhwSSvP8CB786wbwM7mBBucSE5XA6MFBke3Ekr66wq03nsshsVhLnipybK9hnp8hncrGUxx7734BkrK2rUS8O9206PDLlkPdVmSiO6YkdPfgJAB556-yHtqmrDGbPJJ6tZMUPAH47ExE8hTTxCEYjqd9PllPaJibXTf4L_AoxyTBhuMgo0d52vZCspEL0wxbEeGucv1_0cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 374K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 23:32:14</div>
<hr>

<div class="tg-post" id="msg-17666">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الکساندر دوگین تئوریسن مخوف پوتین:
مرگ ناگهانی لیندسی گراهام می‌تواند ترامپ را به تجدید جنگ تمام‌عیار با ایران سوق دهد. این به وضوح به این معنی است که "شما نفر بعدی هستید". لیندسی گراهام سایه ترامپ بود.
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/17666" target="_blank">📅 22:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17665">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیروی قدس سپاه پاسداران انقلاب اسلامی در یک اطلاعیه رسمی:
به ساکنان کشورهای عربی: از حضور در نزدیکی پایگاه‌های آمریکایی و مناطقی که سامانه‌های موشکی در آنجا مستقر هستند، خودداری کنید، زیرا این مناطق ممکن است هدف حملات قرار گیرند.
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/17665" target="_blank">📅 22:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17664">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فارس: قطر و عربستان بازوهای حملات هوایی آمریکا به ایران هستند
@withyashar</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/17664" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17663">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اطلاعیه ناگهانی منابع خبری عربی: به شهروندان و ساکنان کشورهای خاورمیانه و شورای همکاری خلیج فارس، به زودی یک هشدار فوری منتشر خواهد شد، لطفاً کاملا هوشیار باشید. @withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/17663" target="_blank">📅 22:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17662">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اطلاعیه ناگهانی منابع خبری عربی:
به شهروندان و ساکنان کشورهای خاورمیانه و شورای همکاری خلیج فارس،
به زودی یک هشدار فوری منتشر خواهد شد،
لطفاً کاملا هوشیار باشید.
@withyashar</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/17662" target="_blank">📅 22:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17661">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال ۱۲ اسرائیل : بنیامین نتانیاهو با اشاره به مرگ سناتور لیندسی گراهام که امروز درگذشت، گفت: اون به من گفته بود: باید به تأسیسات هسته‌ای ایران حمله کنید.
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/17661" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17660">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آنتونیو گوترش، دبیرکل سازمان ملل متحد، صبح امروز از آمریکا و ایران خواست تا به دور جدید درگیری‌ها پایان دهند و مذاکرات برای خاتمه دادن به آن را از سر گیرند.
این درخواست در حالی مطرح شده که درگیری‌ها عصر امروز از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17660" target="_blank">📅 22:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17659">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snligxLRTMnsdy9hwWT10OAnUhRiDpGhjE7whD0B8yVIgWeCnXZzPidPThehp6-BunAPx2sgqxy8hbKsT7A89NiENT2kebcma33FnL6Fz47uLicE_bccH0sjf-XRaFkWAKNSen2Ngol5_EZPUd-zWUqkDL7mzUMBCULncioE2TwiQ2maX18cwgckedSD6E_LkBSCTrien8LZA2t9gIMQiR8g7BfMiCrI7MwiTxVZOfjq8suTcC9-QMtsWn6QhMY5z4TYw4YdUyjgROazSd6xNItlBA0wqt162FZJsjzTRsebzVnGu3AXGvOGwt3WJOuXFQDU0Qh19AcW2-y3a077_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تریپولی‌رفته و باکسر الان جاش در خاورمیانه است که خیلی امکانات بیشتری داره
تریپولی:
بیشتر یک «مینی ناو هواپیمابر» است و قدرت هوایی بیشتری دارد.
باکسر:
برای تهاجم آبی‌خاکی کلاسیک مناسب‌تر است، چون می‌تواند نیرو، خودرو و تجهیزات را با شناورهای فرود مستقیماً به ساحل برساند.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17659" target="_blank">📅 21:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17658">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیوزمکس گزارش می‌دهد که ناو یو‌اس‌اس باکسر و یازدهمین واحد اعزامی تفنگداران دریایی (MEU) که ​​در حال حرکت بودند، در طول هفته‌های آغازین درگیری با ایران، پس از آنکه نقص سیستم خنک‌کننده موتور، این کشتی تهاجمی آبی-خاکی را مجبور به تغییر مسیر به دیگو گارسیا برای تعمیرات کرد، موقتاً از خدمت خارج شدند.
طبق گزارش‌ها، این مشکل غیرمنتظره تعمیر و نگهداری، قابلیت کلیدی واکنش سریع ایالات متحده را در زمانی که پنتاگون در حال اعمال محاصره دریایی ایران و بررسی گزینه‌های نظامی اضافی بود، از بین برد. پس از اتمام تعمیرات، گروه آماده آبی-خاکی باکسر عملیات خود را از سر گرفت و اکنون از عملیات جدید ایالات متحده در خاورمیانه پشتیبانی می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17658" target="_blank">📅 21:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17657">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اکسیوس: لیندسی گراهام ساعاتی قبل از مرگ گفت «الان نمی‌توانم بمیرم، هنوز باید ماجرای ایران را حل کنم و تحریم‌های روسیه را پیش ببرم»
او چند ساعت قبل از مرگ، احساس ناخوشی کرده بود
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17657" target="_blank">📅 21:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17656">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتاق جنگ با یاشار : این جریان خیلی مشکوکه صدا و سیما داره اینو یهو بولد میکنه مخصوصا این چند روز!  سید علی مصطفوی ، زادهٔ ۲۱ فروردین ۱۳۶۵ (هم سنه منم هست) مشهور به حجت الاسلام والمسلمین سید علی خمینی. وی فرزند سید احمد خمینی و نوه سید روح‌الله خمینی است  از…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17656" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17655">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ : کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است. من فکر می‌کنم خمینی [خامنه‌ای‌] و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند. چون آنها هم از او می‌ترسیدند.  او یک ژنرال درخشان بود. او مردی بسیار بیمار…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17655" target="_blank">📅 21:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17654">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حالا یه چیز بگم مغزت اتاق جنگی رگ به رگ بشه بری تعویض اتاق کنی؟!</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17654" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17653">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد! @withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17653" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17652">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بر اساس گزارش‌ها، چندین پهپاد ایرانی به تعدادی از اهداف متعلق به کردها در سلیمانیه، شمال عراق حمله کردند.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17652" target="_blank">📅 21:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17651">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">متیو ویتاکر، سفیر آمریکا در ناتو: معتقدم در صورت برآورده شدن شرایط قانونی، توافق جنگنده‌های اف-۳۵ با ترکیه نهایی خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17651" target="_blank">📅 21:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17650">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد!
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17650" target="_blank">📅 21:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17649">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اگه بیرون میرین پاور بانک امشب فول شارژ همراهتون باشه
😁
کلا کاراتونو انجام بدید</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17649" target="_blank">📅 20:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17648">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رسانه های داخلی : گزارشات از اصابت دو پرتابه به جزیره بوموسی
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17648" target="_blank">📅 20:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17647">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتانیاهو همکنون در حال حاضر در یک جلسه امنیتی با مقامات ارشد دستگاه‌های امنیتی است.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17647" target="_blank">📅 20:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17646">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2uwo_K8Q2_GpmEeE-CDRymeYpRJxasZg6iKP1OxjWyqY49qSY2ljWrfQBmy3eSWwJnGO_BksqAA_2k-I4M3KctHu5usgB-EJbCgxwAmu2tzORJ7xWSVOJwiegE5cpE4YryTXrIcEWEgXN7IY_EKrgWSOdBGzTGheHtexXKAnktZK44KvqHMUEgEgoGlfthL_Db2E9HEVVV1jhi7ZQsO3vgzy3mPe-BH0M1ZE1O3PK_k6HZcL6HLG5qNrj0XAttfXwWmZqIa1tpzYDthsIXNk6QVBu2wO2XJIG7fUbscmq-pvHCUPh2uWlprsDHKXtAWmKChZ_u_Ow6K-znqixGAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ دستور داد تمام پرچم‌های ایالات متحده در ایالات متحده به مدت شش روز آینده به نشانه احترام به لیندزی گراهام به صورت نیمه برافراشته اهتزاز کنند:
به افتخار زندگی و دستاوردهای قابل توجه سناتور لیندزی گراهام، دوست عزیز من، و مردی واقعاً بزرگ که برای کشورمان و ایالت محبوبش کارولینای جنوبی دستاوردهای زیادی کسب کرد، دستور می‌دهم تمام پرچم‌های آمریکایی در سراسر ایالات متحده تا عصر جمعه ساعت ۶ بعد از ظهر پایین آورده شوند. خدای متعال تو را برکت دهد لیندزی.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17646" target="_blank">📅 20:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17645">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مسئول آمریکایی : حملات آمریکایی که حدود یک ساعت پیش علیه ایران انجام شد، با هدف تضعیف توانایی تهران در حمله به کشتی‌های تجاری صورت گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17645" target="_blank">📅 20:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17644">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17644" target="_blank">📅 20:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17643">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وال استریت ژورنال یک ماه پیش در خبری مدعی شد: در صورت کشته شدن سربازان آمریکایی ترامپ پایان کامل مزاکره با ایران را بررسی خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17643" target="_blank">📅 20:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17642">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ولی خوب مشخصه دیگه امشب میترکونن
🫱🏼‍🫲🏽
😂</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17642" target="_blank">📅 20:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17641">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وقتی چیزی ننوشتم یعنی ترامپ چیزی‌ نگفته فیکه ! برو همونا رو دنبال کن  دایرکت منو سوراخ نکن  اه</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17641" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17640">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اف بی آی به کمک پلیس محلی در پرونده مرگ لینزی گراهام ملحق شد.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17640" target="_blank">📅 20:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17639">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اعزام سه اسکادران جنگنده از انگلستان به منطقه خاورمیانه
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17639" target="_blank">📅 20:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17638">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی: ارتش آمریکا یک ساعت پیش به سامانه‌ های موشکی، پدافند هوایی و قایق‌های کوچک سپاه پاسداران در دو موقعیت در حوالی تنگه هرمز حمله کرد.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17638" target="_blank">📅 20:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17637">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">منبع آمریکایی: حادثه امنیتی بسیار جدی در پایگاه آمریکایی در کویت پس از حمله ایران
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17637" target="_blank">📅 20:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17636">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjJCW1-jI2iUafHqCe0IGZHFmOmgzPqNfmMwykASasDGoszwKq8gDnFjluQAhzrgv7gkEH0Nfg14L5-A6k4ZDHvaIvq8DKp58HzGyO2DGNmTE14aA1p-W6AtAyn3VVbpqbfvhWxh4EWfSFNYnSvvAegDvYjexvojVkh2EwmCVud4FDI9KJ-01Qem2c49lJ9Wj1mYQQL1JDEzgRmbIdKmuyd0WHhCxA_tZqLRbsQoP0EqQ78ErUdUbb_1KiYly_wL1YuRwQXylJof6I0TCTeVBZwhpbmhbOmlPqaAQNDM2LX1S-crXKNGV6kMimqt87ij2Cne7wA3b-dM4qiAM78fkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس‌ها نشان می‌دهند که سناتور لیندزی گراهام در حالی که از محل سکونت خود بیرون برده می‌شد، که پرسنل اورژانس به او کمک‌های اولیه می رساندند.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17636" target="_blank">📅 20:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17635">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17635" target="_blank">📅 20:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17633">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGIe1W2rruVr4HTPb8odgEsDg6f9Vumo3jPVZyo7tFmHMmAzET92Nt1LUEno7rEWTz7jVu4snTLpM93X1YQ-KB3cNaipwqRA0kB8EO3F3J55KqanSzqVjRzwcgDZBrTqF4FSj4Pl9EgdW5xBqXQnw90kFSmKgxaLBG8xLeshDPRmmeNFAS6ExyWTA4XvyhCt1UBWXizQPD0wiauJ__--xAQwPIEoWRvfRg3yzBZcIzjyXEKLkg8r-fKnvYk-e4HFhyavq93mXkZ1LfuQVOmpo43Xe07Iouc2aqvp1tlrvKSi0JqvhlSMHxnDlL5lpAY_Z-n69kN5fa4lCQnWRbipUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون قشم
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17633" target="_blank">📅 19:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17632">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmczWbiiFOTj2uqfclHWXaJr7gzNREGn-cwkeRX8N2YSqrwDSkaBCGzuaXa5wiWG_YKGt9IPXMgzp5zh64IfKh2G2dLtyMuvENQt0AW_yCfV6JdHalwnB5LtLZ8aLtvszxe0wM4uwOig9wMBb2574-zAt0yYfG_8cEjYM9na92cAldNdT0yIhq5924HmHexYEfC57NyGm9Y97TCtD9NbWrckTLc6Fv1QHevEBsF-HUrg5BMrSMsB0mcifnpqLZdb-B4hP3cSjUxGoPY8jT-tTtLaEC4xlPkbcemAWVA-cKHqDffbTkK16yZCSJYiYIE7NaapZCfgrprjE2RD49PoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون چند انفجار جدید مِسِن در قشم ( مناره مسجدش تابلوعه تو ویدو هم دیده میشد )
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17632" target="_blank">📅 19:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17631">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز:
12 مجروح آمریکایی که حال 2 تن از آنها بسیار وخیم است به پایگاه رامشتاین در آلمان منتقل شدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17631" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17630">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش چند انفجار قشمممم
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17630" target="_blank">📅 19:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17629">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هم اکنون شهر مِسِن هرمزگان @withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17629" target="_blank">📅 19:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17628">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a1593a64.mp4?token=e1tWsr3gXkHNuj4kCs73sv2bnIU8Allp16CsUrc6t53s1B8wkKGbfH7OpssbNPLkXQqVQoumsDbbDyZVWdvaf3LPXcus2kE073zeRC7lcferEz7v2NuJ-8q9R27AotoRtag8v9JUWG6SEkyXAm-7eiBE-lDRL-gYFKbdC6q9jI8r-rWjAxx1hM5M6vk0HXKYPV3JRAi3SNQgEMvKtvehxGqUoOP72wNk-a8gXda3F5IBz0PYe1yNSvEfT5ysZm4QLmHP3jI7HMA4QY_4wBd1fnmd4KPFkYOkycMV3D9uy2NCeIsiOHM3QzXXQuNqEmZYa9xqvezUa4Z9ZLJkOJBbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a1593a64.mp4?token=e1tWsr3gXkHNuj4kCs73sv2bnIU8Allp16CsUrc6t53s1B8wkKGbfH7OpssbNPLkXQqVQoumsDbbDyZVWdvaf3LPXcus2kE073zeRC7lcferEz7v2NuJ-8q9R27AotoRtag8v9JUWG6SEkyXAm-7eiBE-lDRL-gYFKbdC6q9jI8r-rWjAxx1hM5M6vk0HXKYPV3JRAi3SNQgEMvKtvehxGqUoOP72wNk-a8gXda3F5IBz0PYe1yNSvEfT5ysZm4QLmHP3jI7HMA4QY_4wBd1fnmd4KPFkYOkycMV3D9uy2NCeIsiOHM3QzXXQuNqEmZYa9xqvezUa4Z9ZLJkOJBbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون شهر مِسِن هرمزگان
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17628" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17627">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تنگه بد دعوا شده…
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17627" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17626">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دیده شدن دود در آسمان قشم و بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17626" target="_blank">📅 19:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17625">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزیر دفاع اسرائیل: به ارتش دستور آماده‌سازی برای عملیات مستقل علیه رژیم ایران داده شد.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17625" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17623">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رسانه های
عربی از کشته شدن سه سرباز آمریکایی و جراحت شدید تعدادی دیگر از سربازان خبر می دهند
.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17623" target="_blank">📅 19:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17622">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عراقچی در دیدار با نماینده ویژه سازمان ملل در امور لبنان، بر ادامه حمایت از لبنان و تمامیت ارضی آن تاکید کرد.
@withyashar
🤡</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17622" target="_blank">📅 19:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17621">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">امشب
🫱🏼‍🫲🏽
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17621" target="_blank">📅 19:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17620">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری کویت :
رژیم ایران در یک حمله غافلگیرانه پایگاه آمریکایی رو مورد هدف قرار داد
بدلیل غافلگیری ۳ موشک پرتاب شده اصابت کردن
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17620" target="_blank">📅 19:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17619">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش شلیک موشک از یزد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17619" target="_blank">📅 19:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17618">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش شلیک جدید از قشمممم
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17618" target="_blank">📅 19:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17617">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رسانه های رژیم : ۵ لانچر از نوع هیمارس که درحال آماده سازی جهت حمله به خاک مقدس جمهوری اسلامی ایران بودند طی یک حمله پیش دستانه و غافلگیرانه توسط یگان موشکی هوافضای سپاه مورد اصابت ۴ فروند موشک فاتح ۱۱۰ قرار گرفتند.
همچنین در این حملات یگان پهپادی ارتش جمهوری اسلامی ایران با استفاده از پهپاد های آرش ۲ مسیر امداد رسانی و دستگاه های ارتباطی این پایگاه تازه تاسیس را مورد اصابت قرار داد.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17617" target="_blank">📅 19:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17616">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هم اکنون انفجار و ستون دود قشم ! @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17616" target="_blank">📅 19:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17615">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۶ موشک یا پهپاد شلیک از قشم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17615" target="_blank">📅 18:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17614">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مهر : شنیده‌ها از حمله موشکی جمهوری اسلامی به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17614" target="_blank">📅 18:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17613">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU2jZl-MCUHtfaAEz_25pAEXpuMxzrZFsP0D7EsPbn6x_o5cFbVTg-bN0DcBXKVjPArVkqcjHx01o4kalmOJNTZ2GQA1Klt4WMZ8E7ZUih0bdB0qYYk5rLtpEgAKmQrSIPhqn5X60DVdrn5MdCjSDbLckMRwT7XKRwlzY8Tblga4TGyJAvYy_rtmZ_QJUY3vfj9utcCRC8X05Ado6t6TBKFWuAaW-xkyxpCRmmIZfPw_AnbRFuteSzeLtjo0Y8lHu6GBuN50sGhfDtxShtQ6DGNv2shrcWaUR2fkVstiYOk0A56jkYJw8Sk3OItYQ4nXTn5ZI4BryZkAWHpclnCHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون انفجار و ستون دود قشم !
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17613" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17612">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">۶ موشک یا پهپاد شلیک از قشم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17612" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17611">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سه انفجار یا شلیک پایگاه امام حسین بندرلنگه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17611" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17610">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
تنگه دعوا شد
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17610" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17609">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ارسالی : قشم درگهان یه دود غلیظ از وسط دریا مشخصه اطراف تنگه
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17609" target="_blank">📅 18:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17608">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ5ushjrdrC37vCkKWjvKMHxOgkjpmLuOprGCMeYOOp2T69qGwHeEsFcR700AdlPn0Pxxuuw3Kp5hcMHnFEu-9mIqWED5hl10GRNWFJH5sxlX_kH5NKpusd420BWA2M-D6doW3CEZQWE_G8MMVzuzvyorPw1TG4lI7ER2IPzKoQ6S3LDA4OMGD3CJMgecr46Ip1PJL_XJJ9Ic0dQdftoKn65HuW_MT-Jd9oiztgbvLlCJDYNRC3S8XSseJwYtCyBbRVxQoG7tP2uekRutWXqrE1czubBt4U5eXiDTrlxLSwSNMZ_vNydkGGZh3ISyBrUkHQFKI1tGoWfkGYrtkPC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه راکت بالستیک در حال حاضر برخورد کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17608" target="_blank">📅 18:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17607">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هدف قرار گرفتن محل‌های پرتاب موشک‌های ATCAMآمریکا
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17607" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17606">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارهایی در کویت رخ داد.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17606" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17605">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d44ac8d93.mp4?token=Id3sgJZaeTTv-ZWMIqoQjTjqFIurQvTRUCp3wcW1x20ZRG3PpCFR9b8-Q0aNmKNIUzofngPZtzapI4iMYXbWV8iXOg_Lbj58gtGkourJXMg4twWg_PCUH4rVer7kwNVNJRgYs4i5BgoKrn0tj9QCdQdYKylRFlm2Wxde7lshpX-YPvkY1jaKHnfR44sKIVo1U56V8O6qaPsXKBpRd9vCByxkiwxPWYtpOgd_s_hwOg6aX7pKOmbI9DyOE8642t9zTe660c4-ZXki4_UchAiqCt8rdZrVIWaynjoqaquYj8TqqErITTw9B9PMyiuDaAqgcxaXsNoUdk24fT5SAHT3GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d44ac8d93.mp4?token=Id3sgJZaeTTv-ZWMIqoQjTjqFIurQvTRUCp3wcW1x20ZRG3PpCFR9b8-Q0aNmKNIUzofngPZtzapI4iMYXbWV8iXOg_Lbj58gtGkourJXMg4twWg_PCUH4rVer7kwNVNJRgYs4i5BgoKrn0tj9QCdQdYKylRFlm2Wxde7lshpX-YPvkY1jaKHnfR44sKIVo1U56V8O6qaPsXKBpRd9vCByxkiwxPWYtpOgd_s_hwOg6aX7pKOmbI9DyOE8642t9zTe660c4-ZXki4_UchAiqCt8rdZrVIWaynjoqaquYj8TqqErITTw9B9PMyiuDaAqgcxaXsNoUdk24fT5SAHT3GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های مانوک خدابخشیان درباره‌ی سناتور لیندزی گراهام.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17605" target="_blank">📅 18:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17604">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/facaf1d397.mp4?token=bE_axnCezWoyFulKdntgV8GhS3s_wNKybRknxj9i23mJ3Zk79pEIEA9k7Va0C5Zg0tkpaDiXMob6lLvg_cam_9gHUMqWcw516s8ceRwKWWbSQLZwSVAK6SJk335w_yRS7gzhl25UzbKeYU9UaNjLhIQAPzWBT-Iz3TigAfEg8ndj01Yy3cz57udyQ61LlJsUnXHKrhi9YYnIO-mg9-LYzUiURgOCV48acXcJJ01W3wn3MYZ-C7Tynyokk-1QD0sWXoz3fmQg-6-rGFbLgCS-l4Q1xjWt7r2vHlxSuMvgwJimbPx0vxyBeeVGg_Di4hKCcgMDaA6OlmzNByZOtRUoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/facaf1d397.mp4?token=bE_axnCezWoyFulKdntgV8GhS3s_wNKybRknxj9i23mJ3Zk79pEIEA9k7Va0C5Zg0tkpaDiXMob6lLvg_cam_9gHUMqWcw516s8ceRwKWWbSQLZwSVAK6SJk335w_yRS7gzhl25UzbKeYU9UaNjLhIQAPzWBT-Iz3TigAfEg8ndj01Yy3cz57udyQ61LlJsUnXHKrhi9YYnIO-mg9-LYzUiURgOCV48acXcJJ01W3wn3MYZ-C7Tynyokk-1QD0sWXoz3fmQg-6-rGFbLgCS-l4Q1xjWt7r2vHlxSuMvgwJimbPx0vxyBeeVGg_Di4hKCcgMDaA6OlmzNByZOtRUoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره لیندسی گراهام:
شما کمیک‌های سوپرمن را به خاطر دارید: «حقیقت، عدالت و روش آمریکایی».
این لیندسی گراهام بود.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17604" target="_blank">📅 18:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17603">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0736854521.mp4?token=Ag6Cx1xx8ZMD8P2AK1tylphMks7wkqGkw38LSHBxeVOZKlbsZotNZMSutZrM-0bwf7B7hW3vVyPkjEgMEhmCZsU0lZy5gEr8s_4iJlG7kx4f6NWyclY6aF6_YdNp_WaomS790Teb7qqP6PGIW94aVqH00LEnj3d-D1nvPxJDz6gUeDdWyh7kXj4eWWW0tsgXcjpGV547ptZeOorF4BweDK_CvmRckAc7PBw9Jvz_jJB5ba3eSmX5mjrab8hL8vo8bMkeQrU6iomM4_Z4rqwHBtzyLNci2Q3KrUPi69QnVe5_Umnr0MI1avoCVOJBrHykXqxJM_wn9p5hwB1eNNRrGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0736854521.mp4?token=Ag6Cx1xx8ZMD8P2AK1tylphMks7wkqGkw38LSHBxeVOZKlbsZotNZMSutZrM-0bwf7B7hW3vVyPkjEgMEhmCZsU0lZy5gEr8s_4iJlG7kx4f6NWyclY6aF6_YdNp_WaomS790Teb7qqP6PGIW94aVqH00LEnj3d-D1nvPxJDz6gUeDdWyh7kXj4eWWW0tsgXcjpGV547ptZeOorF4BweDK_CvmRckAc7PBw9Jvz_jJB5ba3eSmX5mjrab8hL8vo8bMkeQrU6iomM4_Z4rqwHBtzyLNci2Q3KrUPi69QnVe5_Umnr0MI1avoCVOJBrHykXqxJM_wn9p5hwB1eNNRrGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره سناتور لیندسی گراهام:
«او سیاستمدار بزرگی بود. مردم نمی‌دانند که او چه سیاستمدار خوبی بود... احتمالاً هرگز نشنیده‌اید که من این را درباره کسی بگویم. تعدادشان خیلی زیاد نیست... این مرد سیاستمدار بزرگی بود. واقعاً حرفش را می‌فهمید.»
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17603" target="_blank">📅 18:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17602">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ به NBC : گردانندگان ایران مردمی مریض و شیطانی هستند. ما دیشب ترکوندیمشون. امروز نمیخوام در مورد مسئله دیگه به جز لندزی گراهام صحبت کنم.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17602" target="_blank">📅 17:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17601">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ درباره جانشینش به NBC: یه نفر رو تو ذهنم دارم که فکر می‌کنم گزینه خیلی خوبی باشه @withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17601" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17600">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ درباره جانشینش به NBC:
یه نفر رو تو ذهنم دارم که فکر می‌کنم گزینه خیلی خوبی باشه
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17600" target="_blank">📅 17:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17599">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ به سی‌ان‌ان گفت: "دیروز ما با ایرانی‌ها به توافقی رسیدیم و آن‌ها از همه خواسته‌هایشان دست کشیدند. اما ناگهان، بعد از دو ساعت، یک پهپاد به یک کشتی حمله کرد."
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17599" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17598">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دونالد ترامپ به اتاق جنگ با یاشار:
بنده این توفیق را داشتم که پیکر شهید گراهام را بعد از شهادت زیارت کنم. آنچه دیدم کوهی از صلابت بود؛ و انگشت دست ایشان به حالت فاک درآمده بود.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17598" target="_blank">📅 17:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17597">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f6b3525c.mp4?token=ObGlEiWeeY-aUM9LBhB0OjGnkRY1NUf9NUBhiPP3a4B0nFYXczyLwJCyMDGj3UOBoEgaYftpOWZUkuhl9H-rW-8SH3ogL5RGKDmGhPKMq76ZuBXTuNbccMJnrm5NQifKdppQyEpZ7UQGgzBIPcVT77iIbopoBezofjfBomh5h6PzuG4zw5arFu5MW_EWv9Z4J62yPvdYXYHhGxZXzVfXOvYriG4keSKNu6o3O5SkLB4LZOWnY7lTakMW83Q3uhtNhqDOjwzX_EpDF9RJtuV7SO4DONuM8wNhkzVKqEeL_1WlgHDOOdSiLqgq3irrK98vQYUCVvxSpFgBJ67pL4CBcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f6b3525c.mp4?token=ObGlEiWeeY-aUM9LBhB0OjGnkRY1NUf9NUBhiPP3a4B0nFYXczyLwJCyMDGj3UOBoEgaYftpOWZUkuhl9H-rW-8SH3ogL5RGKDmGhPKMq76ZuBXTuNbccMJnrm5NQifKdppQyEpZ7UQGgzBIPcVT77iIbopoBezofjfBomh5h6PzuG4zw5arFu5MW_EWv9Z4J62yPvdYXYHhGxZXzVfXOvYriG4keSKNu6o3O5SkLB4LZOWnY7lTakMW83Q3uhtNhqDOjwzX_EpDF9RJtuV7SO4DONuM8wNhkzVKqEeL_1WlgHDOOdSiLqgq3irrK98vQYUCVvxSpFgBJ67pL4CBcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید ، به دستور ترامپ پس از اعلام خبر درگذشت سناتور لیندسی گراهام، پرچم خود را به حالت نیمه‌افراشته درآورد.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17597" target="_blank">📅 16:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17596">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ: تنگه هرمز باز است.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17596" target="_blank">📅 16:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17595">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنتکام : ایران کنترل این تنگه را در اختیار ندارد.  تنگه هرمز برای تمام کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای ایالات متحده در موقعیت‌هایی مستقر هستند و آماده‌اند تا اطمینان حاصل کنند که آزادی تردد دریایی همچنان حفظ…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17595" target="_blank">📅 16:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17594">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">😞</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17594" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17593">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سنتکام : ایران کنترل این تنگه را در اختیار ندارد.
تنگه هرمز برای تمام کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است.
نیروهای ایالات متحده در موقعیت‌هایی مستقر هستند و آماده‌اند تا اطمینان حاصل کنند که آزادی تردد دریایی همچنان حفظ می‌شود، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران.
ایران کنترل این تنگه را در اختیار ندارد.
ترددها به روال خود ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17593" target="_blank">📅 15:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17592">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">@withyashar
⚔️
شمشیر زن</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17592" target="_blank">📅 15:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17591">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سر صف
😁</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17591" target="_blank">📅 15:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17590">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTheFarhām</strong></div>
<div class="tg-text">اقا توکلی یه انرژی بده تروقران</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17590" target="_blank">📅 15:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17589">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSepehr</strong></div>
<div class="tg-text">هییییچیییی داداش
😂
😂</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17589" target="_blank">📅 15:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17588">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">طبق گزارشات بسیار زیاد شما تو دایرکت، به تعدادی از مراکز نظامی شهر های بزرگ حکم تخلیه داده شده.
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17588" target="_blank">📅 15:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17587">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">چراغ سبز آمریکا</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17587" target="_blank">📅 15:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17586">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">لارا لومر،خبرنگار آمریکایی نزدیک به ترامپ :سناتور گراهام یا توسط روسیه یا توسط سپاه حذف شده و مسمومش کردن
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17586" target="_blank">📅 15:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17585">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سیاست</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17585" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17584">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">من اگر تو (تیم خیلی نایس) شاهزاده بودم الان یه نطق مینوشتم با توجه به تهدیدات اخیر جمهوری اسلامی و انتشار لیستهای ترور و مدارکی که موساد به دست آورده و مرگ ناگهنی لینزی گراهام آتیش به پا میکردم. افسوس…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17584" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17583">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17583" target="_blank">📅 15:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17582">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17582" target="_blank">📅 15:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17581">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">باید تا میتونیم مرگ لیندسی گراهام رو در رسانه ها به جمهوری اسلامی مربوط کنیم منظورم جهانیه نه تو ایران(توییتر به انگلیسی) ! همین کار رو تندرو ها با تختی کردن که خودکشی‌ کرده بود و سینما رکس که خودشون آتیش زدن و گفتن ساواک کرده و از دلایل های بزرگ انقلاب ۵۷ بودن ! چرا ما نکنیم !؟ این فرست ها کم پیش میاد.. بزن بریم ! تازه این بار بعید نیست که واقعا روسیه و جمهوری اسلامی باهم کرده باشن !</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17581" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17580">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18fcd6ecd.mp4?token=G3hwoKfs1FeEPcAVJj3OWVJpXWgdRVf-3WUf4AC61KN16xq0_WHhvahLY9sdWJT7oBpO-DegYkS6IfCBWUSpBJUx8Bpo-i6bdv7JlON9BJjFeVWafN0WKqSV7dJsIXO2-Tf-Uqrw1U-J1b86Z-zmpiGH4uBObXtkdO7hdyLt2j9trjsqMO1yBfN9HSR8C7mk_P3k4NFaw6tfhgAJTQfiDKK2snHRx4VRswvxNM9zGNJB8jFXGs04LRQF0aN75LooVg62CoWuRSSf-BLokr7mpKoymjWUjw5_mnDPtMTZqOULHdV9taCQ1wYBFL48BYDHf4jBP9EQAToWbq5lvEIGwmOqLeketG7vyLxKV3SlqJCy3x6e0zA_tebh-GHAnmuqVf_-NzVCDCn7R4ksge3GaC65px8QqjKQGVWjvpDvl6WXiRluP2kRcs5jxo8GCmDJj01T_9p1ph6RI8n2_86G4C4FgM_SyA9hYO_j5onX8UgV6KeEfOi2CtTZhZNQRySMo0358_hgfWXwkYS8YsT8qJFtZb9S4fgmZnc_Zu2pNn62OmJuCi9Ha-_vwFy0eXrr-YkzVz-boNsUB4f-XifcEROP7B7PlCTsKUdbWeETG_W972h346mfhRrqWj6h3nSFoT_feGsH_w3isPoUWI6i0zLvKkzH-0R-FnJ3cd1pUDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18fcd6ecd.mp4?token=G3hwoKfs1FeEPcAVJj3OWVJpXWgdRVf-3WUf4AC61KN16xq0_WHhvahLY9sdWJT7oBpO-DegYkS6IfCBWUSpBJUx8Bpo-i6bdv7JlON9BJjFeVWafN0WKqSV7dJsIXO2-Tf-Uqrw1U-J1b86Z-zmpiGH4uBObXtkdO7hdyLt2j9trjsqMO1yBfN9HSR8C7mk_P3k4NFaw6tfhgAJTQfiDKK2snHRx4VRswvxNM9zGNJB8jFXGs04LRQF0aN75LooVg62CoWuRSSf-BLokr7mpKoymjWUjw5_mnDPtMTZqOULHdV9taCQ1wYBFL48BYDHf4jBP9EQAToWbq5lvEIGwmOqLeketG7vyLxKV3SlqJCy3x6e0zA_tebh-GHAnmuqVf_-NzVCDCn7R4ksge3GaC65px8QqjKQGVWjvpDvl6WXiRluP2kRcs5jxo8GCmDJj01T_9p1ph6RI8n2_86G4C4FgM_SyA9hYO_j5onX8UgV6KeEfOi2CtTZhZNQRySMo0358_hgfWXwkYS8YsT8qJFtZb9S4fgmZnc_Zu2pNn62OmJuCi9Ha-_vwFy0eXrr-YkzVz-boNsUB4f-XifcEROP7B7PlCTsKUdbWeETG_W972h346mfhRrqWj6h3nSFoT_feGsH_w3isPoUWI6i0zLvKkzH-0R-FnJ3cd1pUDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر مارک سیگل: پدر او هم وقتی خیلی‌جوان بود بر اثر حمله قلب فوت کرد احتمالا پرواز های زیاد و پرواز
اخیر
‌به اکراین باعث مرگ ناگهانی است
از سوی دیگر، همیشه این احتمال هم وجود دارد که یک عفونت ناگهانی رخ داده و به‌سرعت شدت گرفته باشد.
همچنین، همان‌طور که اشاره کردم، پرواز طولانی از اوکراین می‌تواند خطر تشکیل لخته خون را افزایش دهد؛ لخته‌ای که ممکن است در پا ایجاد شود و سپس به ریه منتقل شود و باعث آمبولی ریه گردد؛ عارضه‌ای که می‌تواند به مرگ ناگهانی منجر شود."
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17580" target="_blank">📅 14:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17579">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">علت مرگ لیندسی گراهام ایست قلبی اعلام شده
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17579" target="_blank">📅 14:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17578">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
اتاق جنگ با یاشار : شکی‌ نیست مردم واقعی ایران و انقلاب شیر و خورشید یکی از بزرگترین حامی های خودشو از دست داد ، عمو لیندسی عزیز …، خوشحالم که به واسطه این انقلاب با این شخصیت بیشتر آشنا شدیم و همه با هم کامنت های زیبایی‌ رو براش‌گزاشتیم
💔
😞
او واقعا مردم ایران…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17578" target="_blank">📅 14:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17577">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تسنیم: جمهوری اسلامی پایگاه‌های آمریکا در ۵ کشور رو هدف قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17577" target="_blank">📅 14:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17576">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تسنیم: سامانه‌های دفاعی سپاه پاسداران انقلاب اسلامی، یک موشک کروز متعلق به دشمن را در نزدیکی شهر خرم‌آباد در استان لرستان، غرب ایران، منهدم کردند.
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17576" target="_blank">📅 14:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17575">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرنگار هرمزگان :
از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات آمریکا در استان هرمزگان شنیده شده است
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17575" target="_blank">📅 14:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17574">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مرکز امنیت دریایی عمان اعلام کرد که
به درخواست کمک یک کشتی تجاری با پرچم قبرس که در پی وقوع حادثه‌ای در نزدیکی سواحل مسندم قرار داشت، پاسخ داده است
.
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17574" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17573">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : سناتور میچ مک‌کانل (۸۴ ساله) هفته‌هاست از ۱۴ ژوئن به دنبال یک فوریت پزشکی نامشخص در منطقه واشنگتن بستری شده است. دفتر او تشخیص یا دلیل خاص بستری شدن در بیمارستان را فاش نکرده است، اگرچه گزارش‌ها حاکی از آن است که اولین امدادگران برای نجات یک فرد بیهوش به خانه او اعزام شده و احیای قلبی ریوی (CPR) را انجام داده‌اند خبر مبنی بر چند ساعت پیش فیک نیوز است
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17573" target="_blank">📅 14:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17572">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرضا میرعلمی</strong></div>
<div class="tg-text">عمو یاشار
انتقاد دارم
شما هنر ظریفِ به تخم گرفتن رو نادیده میگیری.
بیشتر روش کار کن لطفا.
این عرزشیا میان دایرکت ی چیزی میگن پای ما ننویس. فقط دایورتشون کن.
عشقی
❤️</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17572" target="_blank">📅 13:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17571">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شبکه 14 اسرائیل : ایران با کارتل مکزیک رفیق شده و بزودی خیلیا قراره ترور بشن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17571" target="_blank">📅 13:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17567">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXuHz_wWzyPc4UrAMzabMG_wUOIjtdm9PTI0gb_MPNcxyMSTp2KGVnRGQf1UJLI8FtLebpz-avU0JkGz5b6rn-560JchBQmMIiw5FtVB1gsEPP8MqpCIZB_P8iiJCcD_UPB5rGwvJ8mgPTggqU8zoooIwl60E8CGXDNBLdwaruU1VpF6Dk1PrOA8Od1kYVg_EdbIGoJvaMU9ZM3X3Bra_YlpevsIbzU4LFkxuvvKxN-t7aNStqV6mT8naZruI74zNDtffAI80f5asKcjRVWk7EsOQiVhMJAn19Us9q8eTIOvr_bboPGLlTw8Xu59lJfyR8n-XxppPJmFwK-Hpchp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plhYgOqIE9sye8_OgLz5iVa8FdxpEunhbFyQBDXqjtXK_EyIwRV2q5GUgHq38fk-ImszBFq4L8Hwes_dD5VXi3SO0xBG5Hfo4N_6Ch8izB2TZvNcP9HbBIfFWv4fTd6_2mccagkHkMKB5lqXlawqTme-QLxJ_gKpi7o1dY-TVBPovKpeuuAIXgas71VUmU_rFax94o74UiRUESy8VzOLtWRGODglTjwmy7Ch7dh9gcSJBNAwifXaDrqS2GSigV04lwNv_g2zhCAp3NsnZvFbrpGWyVVABrR7l75qjbPPYLgfheyRWBMin1DW-tVljoQcLKyf0IKs7qMxwdoaJUdFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3H8CNbkN16amCGePe46OnbiLtCeBm-oXrbXkx4811Q93HRcSIi4pQmyCo7Pi2r4ZU6Ny8ip5Ph5SMeVErXnpMDoikkl0TLaU-sWOydh6FTVH24Pk51iuR2XGWiuCa357cSPYkqzUwq6qdjNFCVo6xfEgVj89rbivLuZbiLQGJgoSotcrQqlBwXV6NqFTir_1qFXSPLh3QR8Z6bQHJd3jVJ0-mTdqPofvb--ETBUEwPVa8W_fYB1qdhLUO9YQovTM6hsK5eFmjwMyiZzXkG-xZHKYWMJaojYW0QZ-FeLbvMw9mtOpoJ0Y4x1VOegv276R30R_KEK-NKsIgWgx8T1og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fc3wN3olFSnp423LVpfbiCEUHc4CgnmN0N7jKYh4zRpUlUrqhfVYid3Fr-Q5YwR6qprM9bxYLsVrFIe5wJZ-fmDZmCIjgvny7-Ws0kEViJnm4EMUh7P7V2DdkJ3ub-y3GKfLv09Yo7nwy5jSd2xVPiaxFWnVOxHBiCntNqFH7olSpgBCL7dknzjkdGSOAF87rNHNBAesHUNjJUtfTZAB99iatkGBgjnd_qDXN82Abx4tfeiTVxfTlOIrwj_HDO_13EgmhKoc3o9GlBwreAr3K16aR0HepkzUJZe3CJjGqqhe06Eu-URGSqN7ncoFw77qNGUvN8ifI4A2ckveA1IzQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب یه موشک بالستیک سپاه در لرستان سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17567" target="_blank">📅 13:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17566">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عمو یاشار گل ما اصالتا ترک هستیم و اسم شما عمو «یاشار» اصالتا ترکی هستش
😂
❤️
و برازندته خیلی زیباس و اسم یاشا هم هست و جمله هست که میگه: یاشیاسان یعنی زنده باشی یا زنده باد سربلند و پیروز همیشه موفق هستش</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17566" target="_blank">📅 13:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17565">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA®∆§|•^H</strong></div>
<div class="tg-text">عمو یاشار گل ما اصالتا ترک هستیم و اسم شما عمو «یاشار» اصالتا ترکی هستش
😂
❤️
و برازندته خیلی زیباس و اسم یاشا هم هست و جمله هست که میگه: یاشیاسان یعنی زنده باشی یا زنده باد سربلند و پیروز همیشه موفق هستش</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17565" target="_blank">📅 13:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17564">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">همین الان پارچین پاکدشت ۴ بار صدا انفجار اومد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17564" target="_blank">📅 13:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17563">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4352950692.mp4?token=gLQ8alUz6HemicBSvXQR6-LUryQzRhSzP3hOUMUMnIamekA8fwWJcqc0-U1y92jk4stgyYehrMQLlXjBlvPXxjdCCme5c6j3NtusN5EV9CEJF4aA-AY2nIuLZ8I6DUkCK612-_Yks8Bh255pnC6wAcEuimAa58uFJyd94CMWeXieFXokIikaVpyGX2OTyZDgX_l2ZDNsLG3f9SRJTMVLlUo_YJHQwo_FFQJVtoM76JxHXSKDlB1rI8BgSwSPMJ0WFq2pj_3brTLFer-MGWzHKvK-k3E9TY4EZ5fBAX6MHseCX_P21Zr-M9QX0I9s7151DNW2qOS_0X_V0YELwaSrwaqc_96MgtX95U7H0U6GeRvSYFAUmyFXHcf8MMT0aOpLTMICeRQpyxMQxFqnUcq6LI3uCAyieZTGm09aCZiU3vOgEnqWHYuvBITbCU_I71nS2uX-budMqupOv7-Ryt7MaWJmxfCYsAiYpCtdRN4CP47B2Xl_OOgywDReRA1uOQmKrLDGEmC-Y0Uc1FRxloi5KFf5wvK3MRS0oAiVZZfGnI16vgncvPAEEMvetolTcRC5xYvwBEmzzwqPqSA_AGcNtx6vdjEp9dqdQNcgvx6peSf_dMSxhf0zzij8EguvSgiOQTfzTT2UzIGJX3nfBLebxU7MVSOvg1TMP01LxKshet0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4352950692.mp4?token=gLQ8alUz6HemicBSvXQR6-LUryQzRhSzP3hOUMUMnIamekA8fwWJcqc0-U1y92jk4stgyYehrMQLlXjBlvPXxjdCCme5c6j3NtusN5EV9CEJF4aA-AY2nIuLZ8I6DUkCK612-_Yks8Bh255pnC6wAcEuimAa58uFJyd94CMWeXieFXokIikaVpyGX2OTyZDgX_l2ZDNsLG3f9SRJTMVLlUo_YJHQwo_FFQJVtoM76JxHXSKDlB1rI8BgSwSPMJ0WFq2pj_3brTLFer-MGWzHKvK-k3E9TY4EZ5fBAX6MHseCX_P21Zr-M9QX0I9s7151DNW2qOS_0X_V0YELwaSrwaqc_96MgtX95U7H0U6GeRvSYFAUmyFXHcf8MMT0aOpLTMICeRQpyxMQxFqnUcq6LI3uCAyieZTGm09aCZiU3vOgEnqWHYuvBITbCU_I71nS2uX-budMqupOv7-Ryt7MaWJmxfCYsAiYpCtdRN4CP47B2Xl_OOgywDReRA1uOQmKrLDGEmC-Y0Uc1FRxloi5KFf5wvK3MRS0oAiVZZfGnI16vgncvPAEEMvetolTcRC5xYvwBEmzzwqPqSA_AGcNtx6vdjEp9dqdQNcgvx6peSf_dMSxhf0zzij8EguvSgiOQTfzTT2UzIGJX3nfBLebxU7MVSOvg1TMP01LxKshet0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/17563" target="_blank">📅 13:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17562">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حمیدرضا دهقان، افسر پدافند دریایی ارتش ایران، در حملات آمریکا در منطقه جاسک در جنوب شرقی ایران کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17562" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
