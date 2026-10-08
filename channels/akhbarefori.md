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
<img src="https://cdn4.telesco.pe/file/YUoH69Vdj4udi-rPH0tDbJPYDXXM1ahcTRg09dYIwqgYE6tlC8hn1NgyoVjLB4ge8R928UTdVlBiaUNbpgXfdLPg5ThxgTPGXjFMpXamt3AfRdU5VGlVt9gV3qpA5tkKtOHErmVbbOIubJqZq0s5KU9xYRIF0sB7uNJif6q5J-RDJL4SAANK-V7y_gy94Uqi_n2JyeyHnsQrtDpFIdaOUY9x5HeSMHBd_iUt82yOYfVHNnrQnYVDvbYHh3tvOqUG6h_FWBXEfxaOE-iGQ_l3hQv2YzZnjdF6dP5mwse5a3tz-0LNJD7QPdyiupz9UxDBPqPSCvrSce7TPVgr-uSIig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-696669">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">23-2 Ane Manaee (1404-02-10)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/696669" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وسوم؛ بخش دوم
🔹
تفاوت میان علم حقیقی متصل به ولایت الهی و علم مادیِ متکی بر ابزارهای فناپذیر [00:00]
🔹
تجربه‌های نزدیک به مرگ، انعکاسی از علم حضوری و شهودی اهل‌بیت در زمان ظهور [03:14]
🔹
فهم ملکوتی لایه‌های آفرینش و نقش ملائکه در تصویرگری نطفه و باز کردن قفل‌های دلها و رحم ها! [08:16]
🔹
سرّ "لا فرق بینک و بینها الّا أنهم عبادک"، نقطه تلاقی اراده انسان کامل با اراده خداوند و بازچینی هستی به دست ولیّ خدا. [12:33]
🔹
جایگاه حقیقی انسان، نقطه نزول قرآن و جایی فراتر از توهمها و سایه‌هاست. [19:30]
🔹
حقیقت در تبعیت از قرآن و اتصال به حبل‌الله است، نه در اوهام و محاسبات غلط شیطانی.  [22:38]
🔹
لایه لایه قفل‌های خلقت در رحم، نشانه‌هایی از تدبیر دقیق، لطف پنهان و حکمت جاری خداست. [30:20]
🔹
کلید نهایی درهای همه عوالم، انس واقعی با قرآن است، نه صرف قرائت، بلکه عرضه، استنطاق و دریافت اشارات الهی [35:52]
🔹
حضور قلب در نماز یعنی بریدن از حدیث نفس و دل‌سپردن به نجوای حقیقی با خدا.   [43:40]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/696669" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696668">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8651a8c2e8.mp4?token=Ac69Q1OH-nBqWCB-s73p_zD2u_JE_uoFY1AjrYn4npV9xWFBWF7kKvv0RTLXEN2FrIDWLXQEPWurtlkz_YiOynFB24afWgEJTCf4oOmKLDu0wp5ts2y44tOGm1p5O8uiphtIwrj_2zvB7URtjlU85-dTRWqV1YmreGAq-KypuYrAwf68UthOQ7X6o5tx_xx79ozd-SWHmnsUqR9FQXexv5H7nM55_WSorm9Kuzhbao76S9x2OYEjOWthfg1CDQqoF-Sy7DtOc4fuYY6AoTf3HH7Mq5eMtbP0cQsPra08a9LxGLpgBVLpLWOM9lQOrm96U74Zt1V0WfH7nnC25KdHBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8651a8c2e8.mp4?token=Ac69Q1OH-nBqWCB-s73p_zD2u_JE_uoFY1AjrYn4npV9xWFBWF7kKvv0RTLXEN2FrIDWLXQEPWurtlkz_YiOynFB24afWgEJTCf4oOmKLDu0wp5ts2y44tOGm1p5O8uiphtIwrj_2zvB7URtjlU85-dTRWqV1YmreGAq-KypuYrAwf68UthOQ7X6o5tx_xx79ozd-SWHmnsUqR9FQXexv5H7nM55_WSorm9Kuzhbao76S9x2OYEjOWthfg1CDQqoF-Sy7DtOc4fuYY6AoTf3HH7Mq5eMtbP0cQsPra08a9LxGLpgBVLpLWOM9lQOrm96U74Zt1V0WfH7nnC25KdHBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رپ پرطرفدار فارسی در تجمعات شبانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/696668" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696667">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای ترامپ جانی: تا پیش از انتخابات میان‌دوره‌ای ( ۳نوامبر ) به ایران حمله نمی‌کنیم/ ما در حال انجام مذاکرات سازنده‌ای با ایران هستیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/696667" target="_blank">📅 20:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696666">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فروش ویژه «چرم مَنطِـ»
به مناسبت روز جهانی دختر
تا %𝟳𝟬 تخفیف تمامی کالاها
➕
𝟮𝟬% تخفیف بیشتر
و
تا 𝟮,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان هدیه اولین خرید
⏳
به مدت محدود
دریافت هدیه
👇
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/696666" target="_blank">📅 20:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696665">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAdad │ آداد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D01KFn3a1U6GZ22G5GgxiOX6zE5fzkyBDBxWnwRp4zzHWuDzX9GtGRAIhhsv30eUDq_bjT56eEPNPNuL3oecNXYL0No3A7XT46R9qlGpu4S3ohewfctUx_neJIlUE5AzUOoX6y0gi4tVFVrxPrWSMgEx8B9-47CSgZgwQucTOc9Nddu52olK6FxrtWxPF7GvuFVCwN1Xk785lGMuOigFVE0ceSrschsyHBfIE3ZZ1ZNcmgydYQbxoEzzFegoxItu0j2VIRk6ddnzopq4FErhYY77wjfpBu37glP_RnrpNOIMGXW8-HA0hFigGy74ano1A09Q5g-VqpEXo6Otg1yjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پیش از امضای قرارداد، بدانید دقیقاً چه تعهدی می‌دهید.
یک بند مبهم یا یک‌طرفه ممکن است بعداً هزینه‌ساز شود. با «آداد؛ دستیار حقوقی هوشمند» قرارداد خود را بررسی کنید تا بندهای پرریسک، تعهدات و ابهام‌های آن را بهتر بشناسید و برای اصلاحشان پیشنهاد بگیرید.
👇
بررسی قرارداد با آداد:
https://go.adadai.ir/wkHN1Rb</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/696665" target="_blank">📅 20:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696664">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
انفجار و آتش‌سوزی در دومین پالایشگاه بزرگ ونزوئلا/ آتش‌سوزی این تأسیسات را به تعطیلی کشاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/696664" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696663">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcGskWM7ly7Id8KcakywxR01yxeDjrIYfelANEv0MDQBApAoAf5U1VQeJ_tqXRKMuHSTvNoHvw_MxVLM9Wt8mKx8bkxlerafOrMh71WmjyClfIZrUusyXLzKiei62cSTMsf4LCauVYD3KhNm1k_cWeDRQnCEWBRVtmeLqD-_bi1rUN2lDvpTQjzUKVYVCgYoUERzeBe0k3adcIoUZuhf_YVs18ctV6A3LEVFkgl1lT-tDDbHK1hCNBoFeuJ7WUEbN6p9laiA2lH_-LN5zfmCL4_QkSTj_Mx7bTUvsYfS1tu1j-PX9qS5x9DwVfnfr2QakqQvAYC4Pk21CEjrE_vitw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات ترامپ دیوانه: اگر می‌خواهید مشکلات را ببینید، اجازه دهید آن‌ها به لس‌آنجلس حمله کنند یا به مکانی مانند سن دیگو. اجازه دهید به یکی از شهرهای بزرگ ما حمله کنند/ این همان چیزی است که به آن "مشکل" می‌گویند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/akhbarefori/696663" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696662">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9964c26be.mp4?token=Mc6YbFkUbe8Oq_psoy7ft4jwm13oPghbsY0_cPw9gHCDp5sJxYHHiAtTdD2exCAqSLM6pS2hOv066MbWIBo7XyIWO7HBNo0K3_5-rgHyuin7xc51oJ9Bc9s8QitIu4dv7dgJPdjPpXnEXc0aw0H_nL_qRQIgj_bMuTSsg9gHlc4ej520mh_Nj6frHIxNHLerun8hVOe_DUjvzTUhR1zGaZSOQHChL4GRreEmIOEk3SRuUML2hmbhPzR_J6WWGxu5ds8I6__h1vxLngdbGTMTu-LziUmDJkNWe9CDFe1fu-VVIRmUv2edRDP8PS8lIJzCjLs3MQcIH-CEQoLlxw8iOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9964c26be.mp4?token=Mc6YbFkUbe8Oq_psoy7ft4jwm13oPghbsY0_cPw9gHCDp5sJxYHHiAtTdD2exCAqSLM6pS2hOv066MbWIBo7XyIWO7HBNo0K3_5-rgHyuin7xc51oJ9Bc9s8QitIu4dv7dgJPdjPpXnEXc0aw0H_nL_qRQIgj_bMuTSsg9gHlc4ej520mh_Nj6frHIxNHLerun8hVOe_DUjvzTUhR1zGaZSOQHChL4GRreEmIOEk3SRuUML2hmbhPzR_J6WWGxu5ds8I6__h1vxLngdbGTMTu-LziUmDJkNWe9CDFe1fu-VVIRmUv2edRDP8PS8lIJzCjLs3MQcIH-CEQoLlxw8iOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی درگیری لفظی میان راننده یک نیسان و یک موتورسوار، موتورسیکلت واژگون شد و نیسان نیز در آستانه واژگونی قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/akhbarefori/696662" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696661">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزیر آموزش و پرورش قول افزایش حقوق معلمان را داد
ولی‌الله بیاتی، سخنگوی کمیسیون امور داخلی مجلس در
#گفتگو
با خبرفوری:
🔹
در جلسه کمیسیون با وزیر آموزش و پرورش، مباحثی مانند سرانه‌های آموزشی، حقوق معلمان، ارتقای کیفیت تحصیلی و کمبود معلم مطرح شد، بخشی از گزارش وزیر قانع‌کننده بود و بحثی نبود اما وزیر در این جلسه قول افزایش حقوق معلمان را داد.
🔹
دولت در حال حاضر به دلیل شرایط جنگی، توان تأمین منابع برای افزایش حقوق را ندارد، هرچند تورم و گرانی فشار شدیدی بر مردم وارد کرده‌است، اگر منابع درآمدی تأمین شود امکان افزایش حقوق وجود دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/696661" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696659">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aega7VnfJ2f2eWCIm1asT_A7DHYgv1d8bGSpJj-ghU1Oze8S3tGNWAsthqgEyuulHnjP5Z0pZTTExNkYdzLuTB5-ucqmcApGdwj0kSjjILTI7jS5ZqAakipX6QY54WxwVEJSPAwvc0K5NP4iOV2l0h5Oki9hUXdfw4NoFzWoMBU9L0ltkCcueuj1OzjlQFOf90qF2kwIXkufJ_pHkNNaBMB74gmLYjAzn7Wq0Oy0Mh12RTy8Iasv1NTT6ugrSdIwbemaUvhjjWeM1VySLD6jmdsqEDD6ylO-wQwt7VhDMRxaiDFE6FiuxP40psy3A3wjqqwExlAnyZW_bqPL7v_rAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1182817ce.mp4?token=DCAlnWDf6PQq6zwdjUdmzFOejEMkkgUlf-Gw1YTKxfcnwa-ay8DEr-BxpXhuVuXlkSMlrdMuNGfsyyTMZ9mxjcyWw1LSJFda4pLRY-i1Ycgcs2sLmvwngXUcez75KxjvZzHwJapNxvf7-3u3CYDz1174bZtWp7PdBORSvOA75HbmL1pfGQIveKOd3oWjernKfv5V4Vhlqgd424IBTLOOiIbx-yM9thhyDjs7X1JoWp9vWhFWFqQCmVNMtEnPxueeZniojqc2yvHucaXklw5Jmr1pU2_MrIu7LPDz9L6DULNxdjdBQaHxtjrid1SFkAUo3gv7M0jwZuk_ubjWLDwcWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1182817ce.mp4?token=DCAlnWDf6PQq6zwdjUdmzFOejEMkkgUlf-Gw1YTKxfcnwa-ay8DEr-BxpXhuVuXlkSMlrdMuNGfsyyTMZ9mxjcyWw1LSJFda4pLRY-i1Ycgcs2sLmvwngXUcez75KxjvZzHwJapNxvf7-3u3CYDz1174bZtWp7PdBORSvOA75HbmL1pfGQIveKOd3oWjernKfv5V4Vhlqgd424IBTLOOiIbx-yM9thhyDjs7X1JoWp9vWhFWFqQCmVNMtEnPxueeZniojqc2yvHucaXklw5Jmr1pU2_MrIu7LPDz9L6DULNxdjdBQaHxtjrid1SFkAUo3gv7M0jwZuk_ubjWLDwcWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به بزرگترین پالایشگاه نفت روسیه
برت اریکسون، استاد دانشگاه:
🔹
ویدئوهای اولیه ظاهراً نشان می‌دهند که پالایشگاه نفت اومسک روسیه پس از حملات اوکراین در آتش می‌سوزد.
🔹
این بزرگ‌ترین پالایشگاه روسیه در سراسر این کشور است. همه‌چیز برای بازارهای انرژی دارد به سمت بدتر شدن پیش می‌رود.
🔹
یک مفسر آمریکایی جنگ روسیه و اوکراین: این پالایشگاه، یکی از جواهرات ارزشمند  است؛ این تأسیسات روزانه ۴۴۰ هزار بشکه نفت را فرآوری می‌کند و...
🔹
۱۱٫۵٪ از بنزین روسیه
🔹
۹٫۲٪ از سوخت دیزل روسیه
🔹
۱۵٪ از سوخت هوانوردی روسیه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/696659" target="_blank">📅 19:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696658">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOVss--1gXjjVDmchoQmVRiBGmJC1WSaDx7PUwVlBkttpanVmPiyt_xWZt9LqUFOHpsGhV8flfwxHrc9L602AwwEMonA1Jr83385b1FSaw5BBl_8wX4wLsXh6FC7mvV_coKlkiRxr5iZsMXveacvBYsSSnGQG5Zn3qjwxwlyNq0NoxDjBTKl_b1HDTcCrjP8aKKAtiSmzdsaGMUoEi3Y8iiL0wZovuFQbCqIBOnsvGDrqcJ9FTQaBQ_FQgatOQqcY9EyhaFNN0AtAGQD9N36DN4xTYg3iODBdvfKVQpH41aw764wfSQ8C1X-rWNRflWWRm00ak-ZbGg-pK0J408iYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ستون‌های دود در پالایشگاه ابقیق در شرق عربستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/696658" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696657">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVuWS1_fBuS636E0ch_9II7petqLNpLJnVbUyUlx6MnT7pnykD8IzoRpwvya5ntAYg7srtLRmFMpkRg1eSC-hAbSqbpt6CIePHmkp7QWGq-fTicZnUN_JsJPLfzAsLALxEMMjClE8z44mqn1qlQ3XP_nymgzCSkkEScon7AhP0NPM030CK4c0SBfY73VlKiXuiPnT1GNPmdSoQI1fHYbSspn9oruGBj514eUAYRkzKgLehBRbktCra8k0FPCdNOQy8O5XMD9vTA45_o5MJYcjEF360vHHt7jkHaa4RPi-h416Vx58AOSPkYPEGsa9Ykp9j2Kf0iiL7p46DMspahWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌بی‌سی: یک ابرنفتکش برای حمل محموله از سواحل خلیج مکزیک به چین با کرایه ۷۶ میلیون دلار اجاره شده است؛ رقمی که ۱۰ برابر سطح پیش از جنگ است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/696657" target="_blank">📅 19:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696656">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba5db5421.mp4?token=OhHrpJiShMjTycuRmKK_rz8MPpQEYOgvvB21abOWN2rNjOilfKRqkyGxvbjzsz4WwijMR7kxXOxo1hv5gvHIY3XQyXQfxqrwzC5rpHrLfOEYKELdaE92Dp0WvO-K10xn4mo5HmN2bJRRx-PXFtfWN0SH3H_YG2mxoCpX86B2P74W5DzbAhlvVm3uJ2UPi6hOcnXM9vSmtmBq085l1JRkJ0Wf3nl11BcWW0AHvrzWuq-aH36g5vEGiBtVYv0zja0RpiuZAmQ01ZZhS0O1bYCWI4KX7M-5gCi2Sbx9Vl3UvATrEgVZc_dR091vWTOaKiD25UOMOPI_CsU9l8oSyVk3b0nui0iO-vKb35z1QmL3i8kAPxgDQvxx0PaNKLOyVBA3J0GgVvqEeopc5_5xA1-sH1ptyLDrnZp3GWspZHFZ_RDNeIihJFK9RJOT1KTqDlI8FMHZaVmqaCC3aA_SU3y6enIritD6HzanvGav8OOLFp_VSiJ7brtc-wR4qQhe4-xcELsBvDhanr2ejDhf7FwjAy826gAc62ergBj_GBVp-AwHGz5cdaUjCQqAUfOM5QOfuVej_HEQbUBL-kDFs8NGnOo6TeeLytUj5jB9-9cysDFF9W9InnWLnNz30z7Z8w4vNS_Ox_ec0_8SWyQxDfdkkbU8E1Phgp6DagDkB1kGK5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba5db5421.mp4?token=OhHrpJiShMjTycuRmKK_rz8MPpQEYOgvvB21abOWN2rNjOilfKRqkyGxvbjzsz4WwijMR7kxXOxo1hv5gvHIY3XQyXQfxqrwzC5rpHrLfOEYKELdaE92Dp0WvO-K10xn4mo5HmN2bJRRx-PXFtfWN0SH3H_YG2mxoCpX86B2P74W5DzbAhlvVm3uJ2UPi6hOcnXM9vSmtmBq085l1JRkJ0Wf3nl11BcWW0AHvrzWuq-aH36g5vEGiBtVYv0zja0RpiuZAmQ01ZZhS0O1bYCWI4KX7M-5gCi2Sbx9Vl3UvATrEgVZc_dR091vWTOaKiD25UOMOPI_CsU9l8oSyVk3b0nui0iO-vKb35z1QmL3i8kAPxgDQvxx0PaNKLOyVBA3J0GgVvqEeopc5_5xA1-sH1ptyLDrnZp3GWspZHFZ_RDNeIihJFK9RJOT1KTqDlI8FMHZaVmqaCC3aA_SU3y6enIritD6HzanvGav8OOLFp_VSiJ7brtc-wR4qQhe4-xcELsBvDhanr2ejDhf7FwjAy826gAc62ergBj_GBVp-AwHGz5cdaUjCQqAUfOM5QOfuVej_HEQbUBL-kDFs8NGnOo6TeeLytUj5jB9-9cysDFF9W9InnWLnNz30z7Z8w4vNS_Ox_ec0_8SWyQxDfdkkbU8E1Phgp6DagDkB1kGK5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
واکنش وزیر آموزش‌وپرورش به مشکلات معیشتی معلمان
علیرضا کاظمی در گفت‌وگوی اختصاصی با تلویزیون اینترنتی «مدار»:
🔹
شکاف حقوق معلمان همچنان وجود دارد و اقدامات صورت‌گرفته کافی نیست؛ با پیگیری ویژه رئیس‌جمهور و برنامه‌ریزی‌های انجام‌شده، به‌دنبال ترمیم اساسی این شکاف‌ها در بودجه سال آینده هستیم.
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/m5c6CNUMRxY</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/696656" target="_blank">📅 19:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696654">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vl8iWURtsbpBBOEyQ27qNCXauaDK4k4ALQdEt2H3UiDNVHGnUe2qfvYuXZth-aIYS8-8f9jXpFr4amjvobBRNUyvsGSXCrV4AUqr7id35AVfmcVo2Tn8gUd6DGtXdZV2cMcWCT1_qUD_0nUkKaUpy0YL6IBtMPfPGLBBY7JjfLXTIfXdRaNtvsgV4OHA0TTZ-K8GaVwSMjmWtq-4Fr--jnDD7zjO9TTr1a5OruQEnBoY6HcWEm1g0KbNBzCO_nwvjj8sJZhjl4pdJ6idAABN8yJG3kiRpH5a3I0RXHjfzrogAY6MLM6GAwsclkLpaq5sEygzHg-oxmF3bDF2SPaMAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6172a23e39.mp4?token=n6PrwzuaLSAbqKyF6uuxYAmICr5zhoHJB2e_xnenRhya4EgOh9uWK23JDF0ejEUyVNShwZPaW2WapcxcHXdbKT0GdN6sxZXX8rrE0MsPIWubwPEIXHmqRVT_4gdl8YM6AJCC87fz6l98G1dId3o8DEJhKE0JmmdNGAuuN2znuyLNbvLvnxlrQC5IngHjfb-tNnnsntRH6pXXRg6-dT3mhC6T7cQDxENCfwjAG7dNHEsfZ4Si358SZzdBsmkoVjJ2MJZajxVyToDof3H_Uri7UfXVJdFeohaJWY1oTv3EHJf6JwFbpCRSMf9hI6Y-apDo2htrRI6i1o9PhOI-glsuug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6172a23e39.mp4?token=n6PrwzuaLSAbqKyF6uuxYAmICr5zhoHJB2e_xnenRhya4EgOh9uWK23JDF0ejEUyVNShwZPaW2WapcxcHXdbKT0GdN6sxZXX8rrE0MsPIWubwPEIXHmqRVT_4gdl8YM6AJCC87fz6l98G1dId3o8DEJhKE0JmmdNGAuuN2znuyLNbvLvnxlrQC5IngHjfb-tNnnsntRH6pXXRg6-dT3mhC6T7cQDxENCfwjAG7dNHEsfZ4Si358SZzdBsmkoVjJ2MJZajxVyToDof3H_Uri7UfXVJdFeohaJWY1oTv3EHJf6JwFbpCRSMf9hI6Y-apDo2htrRI6i1o9PhOI-glsuug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از فرودگاه بین‌المللی ریاض پس‌از مورد هدف قرار گرفتن توسط یمن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/696654" target="_blank">📅 19:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696653">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qshm2EyBW_fVDXSKcSw320iujku2XVD5CEUdoYMcrDyJWYc2WENC5CsvXJFAwSA-yUw8Qyc_n0SaZhTFayP8BuRvn_6akR-gTcLtR7eoYyqmNzo6V5AWPlX0pXFAl2hc1LU2ecLNQBBEmocSNwndssPLRnjAqZ9jWASu_1uPhkWYAZXjLxlFq6oWNdzI_2DDwxLJfm5u7wxlc2YtsQjybbO5SIPw8aocIvkvEwnSynBzaT4AX6UiY8CpGyo_DD1WvAw0S0yXSGBCVkbSqmoHlKbCv9j9JF_m_MuJGrEYyHGg8Cu23BrMuMoKKsunAGlbUdKTMg1lhmVsNfcBVRBffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک هواپیما از نیرو هوایی پاکستان وارد تهران شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/696653" target="_blank">📅 19:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696652">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
واشنگتن‌پست: خروج مخفیانه بمب‌افکن‌های B-۱ آمریکا از پایگاه فرفورد بریتانیا، نشان‌دهنده توان ایران در استفاده از جنگ نامتقارن برای تحت فشار قرار دادن آمریکاست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/696652" target="_blank">📅 19:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696650">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c3730114.mp4?token=FalOBowk2zhXuDTSbUgww-FFJuiFJczJsuxiyV17_Vfq91poTeWbIEg5uew-NPhjmHPHzNqy0dJ1jTrBo8ZpWlNg-Y0sRb9yVQ8oZVGYjbSrgaCFUOah64eyeg9_YNnuZ-kzG0IRQb35qsw2o93mU7Osmjh5qJXVwTu4KVpMHkdRTRcSTEtLAnbPG-SJa1zOatZ7riKMhY7E-Aw5spzhcvArOI6o-jXEG7vrrpVr94HW2TMOtHvhZVj2qyuqR_p_kaiW7EQIpRl4mHAuLj6KyV0zyPe4-lTw-TtlaI_AD7UqZ2q5gCdCakUifJ-_6J_D6HC8jpZKWtwSfeuLE6KFDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c3730114.mp4?token=FalOBowk2zhXuDTSbUgww-FFJuiFJczJsuxiyV17_Vfq91poTeWbIEg5uew-NPhjmHPHzNqy0dJ1jTrBo8ZpWlNg-Y0sRb9yVQ8oZVGYjbSrgaCFUOah64eyeg9_YNnuZ-kzG0IRQb35qsw2o93mU7Osmjh5qJXVwTu4KVpMHkdRTRcSTEtLAnbPG-SJa1zOatZ7riKMhY7E-Aw5spzhcvArOI6o-jXEG7vrrpVr94HW2TMOtHvhZVj2qyuqR_p_kaiW7EQIpRl4mHAuLj6KyV0zyPe4-lTw-TtlaI_AD7UqZ2q5gCdCakUifJ-_6J_D6HC8jpZKWtwSfeuLE6KFDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنگام توقف پشت تریلی یا خودروهای سنگین، فرمان را کاملاً صاف نگه ندارید و کمی بچرخانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/696650" target="_blank">📅 19:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696649">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do9GpIl1_kJklwWW2yEG5BS7ee-KGBR9A8SagtywH738RGCWUCVGf_vSeFkkYusKIf3oEwmqDi3DuhphGgTto1Yd9lH9ztdO1gigf7TdOuWe8O6i8jQ6pWkXCQew3fi4fH37wkhAYOuJhSQx40kk__oDoakyb4ms_wc7DHQn5He-VcqNj-INQQ0amjvv93ib8ijg8JCEkABAEjAn1cKexrzpVUCQkXJeVNza4E76IUCMf_W2U5CEbwBLIhHQXH4efx7bM7TXxElzQtHpGbHzBhm9sGDEF2gVOzN6Auq9lxVNmiFIDv0dO8gsEaPbgc4Skk1d_rv3E0ULrLzDAtyh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل اول تراکتور به استقلال توسط سید مهدی حسینی
❤️
تراکتور ۱ - ۱ استقلال
💙
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/696649" target="_blank">📅 18:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696648">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار گیلان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d8fa34d3.mp4?token=b4hNYqINvv3xuAkxg9wpBXfigaExKhiRTAZn4cdoOwZTm_WyY5enBPKfDpJ2OOHN6s6ke7CT5SrjpXwAvw8sShQ9jchrUVrGrTiyILKZCriL2w47EJoXCQt999hHJqg8nbMAcF9A-NmImU87bgVXPl1cWUSfLIxhgEafz-rh8oQL9aYcVOiVqU1edD5Sbhdc3IAxkpYW0-aPL5JAvNe9jzR_fprvpjLesfxZ4gHMNg4gQC0onJzGtqTak4Ppa4pUG6Qw67fA77yU_Di6bewhwDwbTdcPvRnMYNlgYfOB-R_H3MlqNV-vvJHY4YTPMVhpXwkRgiWMz4Iikz367AAOYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d8fa34d3.mp4?token=b4hNYqINvv3xuAkxg9wpBXfigaExKhiRTAZn4cdoOwZTm_WyY5enBPKfDpJ2OOHN6s6ke7CT5SrjpXwAvw8sShQ9jchrUVrGrTiyILKZCriL2w47EJoXCQt999hHJqg8nbMAcF9A-NmImU87bgVXPl1cWUSfLIxhgEafz-rh8oQL9aYcVOiVqU1edD5Sbhdc3IAxkpYW0-aPL5JAvNe9jzR_fprvpjLesfxZ4gHMNg4gQC0onJzGtqTak4Ppa4pUG6Qw67fA77yU_Di6bewhwDwbTdcPvRnMYNlgYfOB-R_H3MlqNV-vvJHY4YTPMVhpXwkRgiWMz4Iikz367AAOYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه هولناک برخورد صاعقه با دکل برق فشار قوی!
🤯
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/696648" target="_blank">📅 18:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696647">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
اظهارات ترامپ دیوانه: اگر می‌خواهید مشکلات را ببینید، اجازه دهید آن‌ها به لس‌آنجلس حمله کنند یا به مکانی مانند سن دیگو. اجازه دهید به یکی از شهرهای بزرگ ما حمله کنند/ این همان چیزی است که به آن "مشکل" می‌گویند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/696647" target="_blank">📅 18:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696646">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
رئیس سازمان انرژی‌اتمی: آمریکا و رژیم‌صهیونیستی آژانس را تحت‌فشار قرار داده‌اند تا از مکان‌هایی که هدف قرار گرفته بازدید کند و مشاهدات‌شان را در اختیارشان قرار دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/696646" target="_blank">📅 18:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696645">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3a80b6a6c.mp4?token=if0DSGtKNvFISe1EAa95jtudNEvvRbTcglR-YItmQqP_VQgBSiblwrEhy684N03uB_ZJU76MgGkEDdXZqM9nTWUT0ckO1YyL-mLrrxq3g0O_gLm1PhhKd6Kyc2FQqPO-QJ7AV7g1kKBH1BVn2G6V5DzUNHRp_970je73jrrARcwJaJ6dLqm7gjKFOk4EktIqQtKr8CEdoBvq02lBus0SCfSwMEhv2urNgf3olyPrJgPfeC-TWD3pUyS1sGhMcgud8BwXje-CZKlFGW3RjEXExBanKGZji2Wp99uOuffor5DjIOd7R6R2POyV2tVWY3TSUSb1-KBzdcGevfP5wl4cug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3a80b6a6c.mp4?token=if0DSGtKNvFISe1EAa95jtudNEvvRbTcglR-YItmQqP_VQgBSiblwrEhy684N03uB_ZJU76MgGkEDdXZqM9nTWUT0ckO1YyL-mLrrxq3g0O_gLm1PhhKd6Kyc2FQqPO-QJ7AV7g1kKBH1BVn2G6V5DzUNHRp_970je73jrrARcwJaJ6dLqm7gjKFOk4EktIqQtKr8CEdoBvq02lBus0SCfSwMEhv2urNgf3olyPrJgPfeC-TWD3pUyS1sGhMcgud8BwXje-CZKlFGW3RjEXExBanKGZji2Wp99uOuffor5DjIOd7R6R2POyV2tVWY3TSUSb1-KBzdcGevfP5wl4cug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به‌دلیل وقوع طوفان در برخی نقاط تهران برق قطع شد  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/696645" target="_blank">📅 18:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696644">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799c92e63b.mp4?token=uBanRXCf08j4lIiU_wpn0mdE1aC3z0ub1LJRmQlnEFiwR_Eiw6dTPHOfk68knm2Tg9D86a0Csx82XHvj0LSkQG8AcTL0RV8XQlOZQCZ6HYQtrfSTJly9ZcXvxt0hPx64VVrfo6I3MFaH89l79AzqlB35LDqr3yJTtDREfa08khmgjLcJm0q3K74D5ktzjJmw1gJdgiDJCo3NuH0hYIMjjzXR3W9Mncxg77jZMcQlEvUqmOoWPJJ0x_drXxuzr2xEwmgoCHSOWAX6Au0P4qnpOccFckPhqey1UcDu74AUNe_nTF2QHb4W1KzRivWHrxIPcHt6kzEgZZnNCTNYfNxDhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799c92e63b.mp4?token=uBanRXCf08j4lIiU_wpn0mdE1aC3z0ub1LJRmQlnEFiwR_Eiw6dTPHOfk68knm2Tg9D86a0Csx82XHvj0LSkQG8AcTL0RV8XQlOZQCZ6HYQtrfSTJly9ZcXvxt0hPx64VVrfo6I3MFaH89l79AzqlB35LDqr3yJTtDREfa08khmgjLcJm0q3K74D5ktzjJmw1gJdgiDJCo3NuH0hYIMjjzXR3W9Mncxg77jZMcQlEvUqmOoWPJJ0x_drXxuzr2xEwmgoCHSOWAX6Au0P4qnpOccFckPhqey1UcDu74AUNe_nTF2QHb4W1KzRivWHrxIPcHt6kzEgZZnNCTNYfNxDhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل تساوی تراکتور به استقلال که توسط VAR رد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/696644" target="_blank">📅 18:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696641">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b343876a5.mp4?token=vklo9CW3hvug8zApY335CGaSKUSGwC2vSWvh4eZ7DJZFdo5n1lbE5BWwLBVKD2fC-N6cX-DBgo478XtE7tnLpyjV6B3VIOoDZyxhYkDtorXfSDcgHeF6Y80m0PIZuMunESRDh95JQDkoM2JC8MjjoPJBL0h4tMEGP3G_UxomwzyDFy4CdyyWRKKMQcSzVx2BtjTLDbmAhZjPQsO1L4ovntAqrLSnPko3UxYfu2qjQx7VkOlPtAPoZcjmL8Z7e7GyQEHyCvz7YS_nc1uVhM1Ac3KcOwRmOlVfjkQvq7syS--bnx50oY-T6Q-AxlfKsssk8vIcjpTiG8XM4QJD3t1pWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b343876a5.mp4?token=vklo9CW3hvug8zApY335CGaSKUSGwC2vSWvh4eZ7DJZFdo5n1lbE5BWwLBVKD2fC-N6cX-DBgo478XtE7tnLpyjV6B3VIOoDZyxhYkDtorXfSDcgHeF6Y80m0PIZuMunESRDh95JQDkoM2JC8MjjoPJBL0h4tMEGP3G_UxomwzyDFy4CdyyWRKKMQcSzVx2BtjTLDbmAhZjPQsO1L4ovntAqrLSnPko3UxYfu2qjQx7VkOlPtAPoZcjmL8Z7e7GyQEHyCvz7YS_nc1uVhM1Ac3KcOwRmOlVfjkQvq7syS--bnx50oY-T6Q-AxlfKsssk8vIcjpTiG8XM4QJD3t1pWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گل اول استقلال به تراکتور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/696641" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696640">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f597d294b8.mp4?token=uoXVgcwVR4855ZWuTgFlzfd0RbmhTEjErj99yNFmnlQkxhIVJh3jL4f949UqL2OakCK5xOMX6xQ4LhthkXeKoAsq0izAbSsqbd5NIl8Me2xLHHhJ7-QXXPVRfouA3RMjc1SlMtj5NUGy3BQcqyykGZbDlg8CppEN6BShyY0ZhR21NowWIxzAwr1305QRXXgphHo-6SlpsqrFuTXpyy1ztvu1IqgsEtJA7UdUIACNYqyHTWWyA34gIXsnQgnPQx26dOSDbW_TpGsKZpot-jwVevT6Xg-n_H4E62e2BX3GZDPnkQAZWfOtk4_6Tq4ymZJMFYlZM3BE0gj90FuAixrtCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f597d294b8.mp4?token=uoXVgcwVR4855ZWuTgFlzfd0RbmhTEjErj99yNFmnlQkxhIVJh3jL4f949UqL2OakCK5xOMX6xQ4LhthkXeKoAsq0izAbSsqbd5NIl8Me2xLHHhJ7-QXXPVRfouA3RMjc1SlMtj5NUGy3BQcqyykGZbDlg8CppEN6BShyY0ZhR21NowWIxzAwr1305QRXXgphHo-6SlpsqrFuTXpyy1ztvu1IqgsEtJA7UdUIACNYqyHTWWyA34gIXsnQgnPQx26dOSDbW_TpGsKZpot-jwVevT6Xg-n_H4E62e2BX3GZDPnkQAZWfOtk4_6Tq4ymZJMFYlZM3BE0gj90FuAixrtCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی خیره‌کننده از سایه قله دماوند بر کوه‌های البرز
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/696640" target="_blank">📅 18:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696639">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رمز گشایی از اظهارات رئیس بانک مرکزی؛ وضع ارز بهتر از سال ۱۳۹۹
مهدی عبداللهی، دبیر سرویس اقتصاد روزنامه «فرهیختگان» نوشت:
🔹
تقریباً ۸ روز پیش آقا یا خانم اسکات بسنت، وزیر خزانه‌داری آمریکا گفت «اقتصاد ایران تا دو هفته دیگر از بین می‌رود». حالا ۴ روز از اعلام این ضرب‌الاجل مانده، اما حالا اقتصاد ایران گرچه از ناحیه التهابات ارزی زخمی شده، با این حال ضربه‌گیر‌هایی برای مقابله با این جنگ اقتصادی ظالمانه تأمین کرده و نفس می‌کشد.
🔻
در روز‌های گذشته مسئولان بانک مرکزی ایران با حضور در رسانه ملی برنامه‌ها و تدابیر خود برای مقابله با جنگ اقتصادی آمریکا علیه کشورمان را اعلام کردند. عبدالناصر همتی، رئیس‌کل بانک مرکزی می‌گوید با وجود فشار‌های ناشی از جنگ، تورم نقطه‌به‌نقطه متوقف شده و روند آن به سمت کاهش حرکت کرده است. به گفته وی، رشد نقدینگی در شهریورماه به 1.3درصد رسید که کمترین رقم در چند ماه اخیر است و روند رشد نقدینگی نقطه‌به‌نقطه نیز از اوج خود فاصله گرفته و اکنون به ۵۱ درصد رسیده است.
🔻
به گفته همتی، از ابتدای سال تا نیمه مهرماه با وجود تشدید جنگ اقتصادی، این نهاد حدود ۲۵ میلیارد دلار ارز برای واردات تأمین کرده، رقمی که در مدت مشابه سال گذشته ۲۸ میلیارد دلار بوده است. همچنین در این مدت، تأمین ارز کالا‌های اساسی کاهش نیافته و ارز دارو نیز ۳۰ درصد افزایش یافته است. همتی همچنین بر نقش جنگ روانی و رسانه‌ای تأکید کرده و می‌گوید القای نااطمینانی از سوی دشمن بر افزایش تقاضای ارز اثر داشته و به بازار ارز فشار وارد کرده است.
🔻
به گفته وی، بانک مرکزی برای سناریو‌های مختلف واکنش‌پذیری مشخص دارد و با عرضه ارز و مداخله هدفمند، به دنبال مدیریت نوسانات است.
🔻
تأمین ۲۵ میلیارد دلار ارز واردات
🔻
همتی با اشاره به روند تأمین ارز کشور، می‌گوید: «با وجود فشارهای اقتصادی، روند تأمین ارز امسال مناسب بوده و از ابتدای سال تا نیمه مهرماه ۲۴.۹ میلیارد دلار ارز برای واردات کالا تأمین شده است.» وی افزود: «در مدت مشابه سال گذشته مجموع تأمین ارز حدود ۲۸ میلیارد دلار بود و امسال با وجود کاهش ۱۲ درصدی تأمین ارز در بخش کالاهای اساسی کاهش نداشتیم و تأمین ارز دارو نیز ۳۰ درصد افزایش یافته است.»
🔻
رئیس‌کل بانک مرکزی، بیان می‌دارد از ابتدای سال برای تأمین کالاهای اساسی، دارو و مواد اولیه کارخانجات برنامه‌ریزی شده بود و بانک مرکزی برای تداوم این روند در شرایط مختلف آمادگی دارد. همتی با اطمینان‌دادن به مردم درباره تأمین ارز، می‌گوید بانک مرکزی برای فروش ارز و تأمین ارز تجاری به اندازه کافی منابع دارد و سیاست مدیریت بازار و عرضه ارز را تا زمانی که لازم باشد ادامه خواهد داد.
🔻
نقش سلبریتی‌های اقتصادی در بحران ارزی
🔻
در روزهای گذشته عبدالناصر همتی در تشریح عوامل مؤثر بر افزایش نرخ ارز، علاوه بر متغیرهای اقتصادی، بر نقش القای روانی، افزایش انتظارات تورمی و انتظارات منفی تأکید کرده است. به گفته او، بخشی از افزایش قیمت ارز با وجود تأمین منابع ارزی، ناشی از افزایش انتظارات تورمی بوده است. اظهارات همتی مصادیق عجیبی در فضای مجازی کشور دارد. بررسی‌ها نشان می‌دهد بخشی از این تشدید انتظارات گاه از سوی اینفلوئنسرها و سلبریتی‌های اقتصادی، برخی نمایندگان مجلس و حتی برخی افراد با رویکردهای سیاسی و جناحی صورت می‌گیرد؛ افرادی که با برجسته‌سازی اخبار و روایت‌های منفی، خواسته یا ناخواسته منجر به تشدید نااطمینانی و افزایش انتظارات تورمی در جامعه می‌شوند.
🔻
شرایط فعلی بهتر از سال ۱۳۹۹ است
🔻
براساس اظهارات مسئولان بانک مرکزی، درحال حاضر روزانه بیش از ۲۰۰ میلیون دلار تأمین ارز تجاری انجام می‌شود. این عدد از این منظر قابل‌تأمل است که طبق داده‌های مرکز مبادله ایران، حجم عرضه ارز در بازار ارز تجاری مرکز مبادله ارز و طلای ایران از ۱۵ شهریور ۱۴۰۴ تا ۱۵ دی‌ماه ۱۴۰۴ به طور میانگین ۱۰۰ تا ۱۲۰ میلیون دلار و در برخی روز‌ها حتی ۶۰ تا ۷۰ میلیون دلار بوده است.
🔻
این عدد ۷۰ میلیون دلار از دو جهت قابل‌توجه است، اول اینکه معادل کل عرضه ارز در بازار ارز تجاری در دوره شهریور تا اوایل دی‌ماه ۱۴۰۴ بوده و مورد دوم اینکه معادل ۳۵ درصد از کل تأمین روزانه ارز در مرکز مبادله (روزانه ۲۰۰ میلیون دلار) در شرایط فعلی است. آن‌طور که مسئولان بانک مرکزی می‌گویند، با توجه به اینکه از زمان فروش نفت تا بازگشت ارز به کشور چندین ماه زمان لازم بوده، ادعای اینکه فروش نفت ایران در شرایط فعلی کاهش یافته، نمی‌تواند مبنای توان ارزی کشور باشد، چراکه منابع ارزی که فرضاً در مهرماه وارد کشور می‌شود، نفت آن ماه‌ها قبل به فروش رسیده است.
🔻
موضوع حائز اهمیتی که در اظهارات رئیس کل بانک مرکزی و دستیار وی مشاهده می‌شود، اینکه وضعیت منابع ارزی فعلی بسیار بهتر از سال ۱۳۹۹ است. به گفته رئیس کل بانک مرکزی، درآمد ارزی بانک مرکزی در سال ۱۳۹۹ به یک‌نهم میانگین سال‌های گذشته، یعنی کمتر از ۶ میلیارد دلار رسیده بود. در همین خصوص، بررسی داده‌های نماگر‌های اقتصادی بانک مرکزی نیز نشان می‌دهد درحالی در ۴ماهه نخست سال ۱۳۹۹ کل فروش نفت و گاز ایران حدود ۵.۷ میلیارد دلار بوده، اما براساس اعلام وزارت نفت، در چهار ماه نخست سال ۱۴۰۵، میزان فروش نفت ۱۱ میلیارد دلار بوده است.
🔻
تجربه مداخله ارزی سال ۱۳۹۷
🔻
مرور داده‌ها نشان می‌دهد در ماه‌های ابتدایی سال ۱۳۹۷، گرچه بخشی از افزایش نرخ ارز را باید در متغیر‌های بنیادین اقتصاد، جست‌وجو کرد، اما با گذشت چند ماه، رشد نرخ ارز با همان شدت دیگر صرفاً با این عوامل قابل‌توضیح نبود. نرخ دلار از حدود ۵ هزار تومان در ابتدای سال به بیش از ۹ هزار تومان در ابتدای مرداد و در نهایت به بیش از ۱۸ هزار تومان در مهرماه رسید. در این مرحله، تقاضای احتیاطی، سفته‌بازی، خروج سرمایه و تشدید انتظارات تورمی، نقش پررنگ‌تری پیدا کردند.
🔻
بنابراین، اگرچه شوک اولیه ارزی ریشه در تغییرات بنیادین داشت، اما تداوم و تشدید آن تا مهرماه، بیش‌ازپیش تحت‌تأثیر عوامل غیربنیادین و انتظارات بازار قرار گرفت و اینجا بود که مداخله ارزی مؤثر بانک مرکزی توانست اضافه‌پرش نرخ ارز را مهار کند. این موضوع در شرایط فعلی کشور نیز مصداق دارد. به گفته اقتصاددانان، بخش قابل‌توجهی از جهش اخیر نرخ ارز را نمی‌توان صرفاً با عوامل بنیادین اقتصادی و ارزش واقعی نرخ ارز توضیح داد و عوامل انتظاری و غیر‌بنیادین در این افزایش نقش مؤثری دارند.
🔻
تجربه مداخله ارزی سال ۱۳۹۹
🔻
به گواهی داده‌ها و اظهارنظر مسئولان بانک مرکزی ایران در سال‌های اخیر، طی دوره‌های تحریمی پس از سال ۱۳۹۷، سال ۱۳۹۹ یکی از دشوارترین مقاطع ارزی اقتصاد ایران بود؛ چراکه برخلاف دوره‌هایی که صرفاً با افزایش تقاضای سفته‌بازانه مواجه هستیم، در این دوره منابع ارزی کشور نیز به شدت محدود شده بود. بااین‌حال، مداخله سیاست‌گذار توانست موج انتظارات را مهار و نرخ ارز را از قله هیجانی خود پایین بیاورد.
🔻
درس سال ۱۳۹۹ روشن است. گرچه تثبیت پایدار بازار ارز در نهایت به پشتوانه عرضه ارز و بهبود متغیر‌های بنیادین اقتصاد نیاز دارد، اما مداخله ارزی مؤثر و اعتماد به بانک مرکزی می‌تواند حتی در شرایط کمبود شدید منابع، یک شوک قیمتی وارد و انتظارات را مهار کند.
🔻
سهم وزارتخانه‌ها در مدیریت بازار ارز
🔻
درحالی که در تحلیل بازار ارز ایران، معمولاً نگاه‌ها به بانک مرکزی و سیاست‌های این نهاد معطوف می‌شود، بااین‌حال، بخش مهمی از معادله ارز، خارج از ساختمان بانک مرکزی شکل می‌گیرد. موضوع این است که سه وزارتخانه جهاد کشاورزی، صمت و بهداشت، به دلیل سهم بالای مصارف ارزی از مهم‌ترین بازیگران این بازار هستند. بر اساس آمار‌های ارائه شده از سوی بانک مرکزی ایران، طی سال‌های ۱۴۰۲ و ۱۴۰۳ سهم وزارت صمت از کل مصارف ارزی کشور (واردات) حدود ۷۷ درصد، وزارت جهاد کشاورزی ۱۷ درصد و وزارت بهداشت ۵ درصد و سایر مصارف ۲ درصد بوده است.
🔻
تجربه سال‌های اخیر نشان می‌دهد این نقش گاهی نادیده گرفته شده است. برای نمونه، صدور گسترده کارت‌های بازرگانی و ضعف در اهلیت‌سنجی، یکی از حلقه‌های مسئله بازگشت ارز صادراتی بوده است. طبق آمار ارائه شده، در سال‌های ۱۴۰۳ و ۱۴۰۴ مجموعاً ۶۷ هزار و ۳۹۸ کارت بازرگانی صادر شده، رقمی که تقریباً با کل صدور کارت بازرگانی در فاصله ۱۳۹۱ تا ۱۴۰۰ برابری می‌کند. در ظاهر افزایش تعداد کارت‌های بازرگانی باید اتفاق مثبتی در زمینه تسهیل کسب‌وکار و تجارت خارجی باشد، اما اتفاق بدتری که رخ داده این است که طبق گزارش‌های بانک مرکزی ایران و سازمان بازرسی، طی سال‌های ۱۳۹۷ تا بهار ۱۴۰۵ حدود ۳۵ درصد از تعهدات ارزی ایفانشده منقضی شده کشور مربوط به کارت‌های یک‌بارمصرف یا اجاره‌ای است.
چنین ضعف‌هایی در سیاست تجاری، در نهایت تبعات خود را به بازار ارز منتقل می‌کند. نمونه دیگر، پرونده فساد چای دبش است که به دلیل ضعف در مدیریت تخصیص و نظارت بر منابع ارزی در وزارتخانه‌های جهادکشاورزی و صمت پرونده فساد بزرگ واردات چای و ماشین‌آلات شکل گرفت. موضوع بعدی که اخیراً رخ داده، واردات خودرو‌های لوکس توسط ایرانیان خارج از کشور یا همان واردات خودرو با ارز اشخاص است.
🔹
این موارد نشان می‌دهد اگر سیاست ارزی با سیاست تجاری و صنعتی هماهنگ نباشد، بانک مرکزی ناچار خواهد بود هزینه تصمیم‌های سایر دستگاه‌ها در بازار ارز را نیز جبران کند.
﻿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/696639" target="_blank">📅 18:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696638">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
شرکت Kpler: برخی تولیدکنندگان نفت در منطقه خلیج فارس ممکن است به‌طور مخفیانه به ایران عوارضی معادل ۱۰ تا ۲۰ درصد از محموله‌های نفتی خود پرداخت کنند تا در ازای آن، عبور امن محموله‌هایشان از تنگه هرمز تضمین شود
🔹
این ادعاها هنوز تأیید نشده‌اند، اما Kpler می‌گوید چنین توافق‌هایی می‌تواند به توضیح این موضوع کمک کند که چرا قیمت نفت خام برنت همچنان در نزدیکی ۱۰۰ دلار در هر بشکه باقی مانده است./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/696638" target="_blank">📅 18:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696637">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ترامپ تروریست: ما به شدت به ایران ضربه می‌زنیم. دیگر هیچ تهدیدی از سوی سلاح‌های هسته‌ای وجود ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/696637" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696636">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c6857d6c.mp4?token=OvseWwZoxUIvK-fwUYyvEcfd-L9bt04MeIW6h4TARQ-hV1_EvsA7n5NFIywvweAem9Ncs7_FTPo3r3dAtDvwgip1_2CqkJSuuYAhNY4N33vn_9WJ7lZ766sjsu9uSsVdbNaowF_KG0jO2SnIM4rjuefNtynuC9kRhBIvlUD7GZu2l4adnlGXyO6n7aRLDrDpBiCf2sd7uFkiFgV4tURsxMjfaDsiCYyIds9rWBa7bMRPdwzlFYsyriR8vO2vjrmhUieU1NR3w02XzU3z5YG617wSHnqn0cW6Gu6dtm4Q45U5JUlfjQSC1tT7UQ8nnGG5TtM7m_bqrnfYFDWKZ08R3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c6857d6c.mp4?token=OvseWwZoxUIvK-fwUYyvEcfd-L9bt04MeIW6h4TARQ-hV1_EvsA7n5NFIywvweAem9Ncs7_FTPo3r3dAtDvwgip1_2CqkJSuuYAhNY4N33vn_9WJ7lZ766sjsu9uSsVdbNaowF_KG0jO2SnIM4rjuefNtynuC9kRhBIvlUD7GZu2l4adnlGXyO6n7aRLDrDpBiCf2sd7uFkiFgV4tURsxMjfaDsiCYyIds9rWBa7bMRPdwzlFYsyriR8vO2vjrmhUieU1NR3w02XzU3z5YG617wSHnqn0cW6Gu6dtm4Q45U5JUlfjQSC1tT7UQ8nnGG5TtM7m_bqrnfYFDWKZ08R3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ تروریست: ما به شدت به ایران ضربه می‌زنیم. دیگر هیچ تهدیدی از سوی سلاح‌های هسته‌ای وجود ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/696636" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696635">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سی‌ان‌ان: ارتش ایالات متحده در جریان جنگ با ایران، ۸۱ فروند هواپیما را از دست داده؛ این موضوع در گزارشی از کنگره آمریکا که این هفته منتشر شده، آمده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/696635" target="_blank">📅 18:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696633">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15be8aa467.mp4?token=IPi5PxOja-jrlllMo5Qk13f56cPMo66cnKIgzzOi2MucAkZjv1SVo4-MGhEEwC2DuYAGE52sNpyR4Ad4UYrYZWALt9-zjkWLvKmoyNoo6Z4lHHE7xxUZV9IPhAxXDddS_WLdeX4LnyWvFpiZb_0EdM_1jFlGytibZa9gTYUF6c_EjmcKgQ9A8xEseKWEzlpRZfGAQiz-6Q8yj2JIORRxvaU2_ICBbZ1Syl2ZoUzNtJsGeNBMejKP-IabyepbV9t6NvcN5zNXqfGGGD9YdizWg0GH0RqfSwmXtioD5jjW5Q-WOUoB_MEUz1yqt5Jj_ewPXWsYwWiET36LQ_S0LNy78Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15be8aa467.mp4?token=IPi5PxOja-jrlllMo5Qk13f56cPMo66cnKIgzzOi2MucAkZjv1SVo4-MGhEEwC2DuYAGE52sNpyR4Ad4UYrYZWALt9-zjkWLvKmoyNoo6Z4lHHE7xxUZV9IPhAxXDddS_WLdeX4LnyWvFpiZb_0EdM_1jFlGytibZa9gTYUF6c_EjmcKgQ9A8xEseKWEzlpRZfGAQiz-6Q8yj2JIORRxvaU2_ICBbZ1Syl2ZoUzNtJsGeNBMejKP-IabyepbV9t6NvcN5zNXqfGGGD9YdizWg0GH0RqfSwmXtioD5jjW5Q-WOUoB_MEUz1yqt5Jj_ewPXWsYwWiET36LQ_S0LNy78Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرتمیا؛ مهمان کوچک ارومیه با توانایی شگفت‌انگیز
!
🔹
آرتمیا یا «میگوی آب‌شور» سخت‌پوستی کوچک است که در آب‌های شور زندگی می‌کند و تخم‌های مقاومش می‌توانند مدت‌ها در شرایط نامساعد زنده بمانند.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/696633" target="_blank">📅 18:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696632">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
به‌دلیل وقوع طوفان در برخی نقاط تهران برق قطع شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/696632" target="_blank">📅 17:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696631">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
رئیس سازمان انرژی‌اتمی: آمریکا و رژیم‌صهیونیستی آژانس را تحت‌فشار قرار داده‌اند تا از مکان‌هایی که هدف قرار گرفته بازدید کند و مشاهدات‌شان را در اختیارشان قرار دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/696631" target="_blank">📅 17:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696630">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdQ_psaIxF2mwfS23vDTfnrvh2Jea4ppX3m-vpsM4iDsg8_Rri4K_basEM0-4n-XCgbZflWz2o92M5MH4APIZKxnNAtwHmksly5tz2BL3d1qbeuHTyj3Lq_A5SbzClnVpn9qamFcMgZQujrK_zVjABwIAkHW4NGds4Z487CcGTPqpyL_KtMISwwUM1Nrf8Akc-Zjt9EIihs8_IjYoNerajQayX9Q7Of2dQ4t74dx9xprmgU4iPY0mgmuNMv5e026jtzej6bb2ilEdbx7kvPegSZbAcNN81ATGCm6Oy9HMbjLdKUS81__sbBBXuMLJClyszukcKQnnf8_81bC5NDqwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: ارتش ایالات متحده در جریان جنگ با ایران، ۸۱ فروند هواپیما را از دست داده؛ این موضوع در گزارشی از کنگره آمریکا که این هفته منتشر شده، آمده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/696630" target="_blank">📅 17:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696629">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/716d610e31.mp4?token=VhwiZxS4eEfAXgk8jAc8xLCHv8EikvOAczWAeVRU9pADiTQK6qJgEAfEPVLA1R65KJznu4lm_wIIBIIvmqzD681QkUE9pPpHcO2eX0N0P2BYeGXEmPhGmyjVUypbn4XGekJOiiatUdZkXxzFzE_B6XW9eIaNNbK7wIhl-z-xureRj3ycFkbvygEAxViK30qOGBFLC7VHGyQEOztsfGzNzhmh_VOl1g0oXLPjLsbOeTlALGoM9Ntp191JKe5xmPDDQTzvC9XiOsakV36avpE1xcepvsiXUI2VF10h0-GENpYXyGlsNQHoS9vx0eYRaR89YR48zAVWudjEgEl376jExA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/716d610e31.mp4?token=VhwiZxS4eEfAXgk8jAc8xLCHv8EikvOAczWAeVRU9pADiTQK6qJgEAfEPVLA1R65KJznu4lm_wIIBIIvmqzD681QkUE9pPpHcO2eX0N0P2BYeGXEmPhGmyjVUypbn4XGekJOiiatUdZkXxzFzE_B6XW9eIaNNbK7wIhl-z-xureRj3ycFkbvygEAxViK30qOGBFLC7VHGyQEOztsfGzNzhmh_VOl1g0oXLPjLsbOeTlALGoM9Ntp191JKe5xmPDDQTzvC9XiOsakV36avpE1xcepvsiXUI2VF10h0-GENpYXyGlsNQHoS9vx0eYRaR89YR48zAVWudjEgEl376jExA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گل اول استقلال به تراکتور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/696629" target="_blank">📅 17:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696627">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TJtv8oLphXhdTRFTB_Tm0JrNkDtxQN8ZpuMFLkTOZr7zGfTH_1NnWmh2Tq8FJ3fFGdpz3l0gc69C1K0PynkITqV9IDUmWGYEHRkfTCzcUB3rurz2zEMscEwkBULcYykgThGOtyk4fELkFMEEZOUBur2pQqQz2l9cFrKo-Zeu4VeE3gTYPgLmABzAPjicN2wgQq5dkaXJox0agFnwANLSH97LYq86BfY6UVl1eKS1X3K7RNb1ccoHYC5rK82bDdI8bakzaVOIh8SQtUt-d1vACx_PkCzbnQaMOMUdf0ZfD-n4AMq3I4fRfJo-yCpLus0QpuQRyLd7gZszWfIgtkQtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08203f0128.mp4?token=jAozGGCBgJul8yiPYT0jn3qH0P_EXis3jH7klFTMxkPF-8IO_94eGoFD8zdunzzsifjLiNA3u3g2vtZe-WspDfkssQB_Gk04mXzFQckKi7pqIRS68OVBssR2seWlBjSzFGLNeFPjYo_EDAPIINoJZ0DulZEhs4kn5vkCWU-WRQyYcweGpf5XSr8wKnCZPe9KME315Th-81vXNosn7slRXrudYXvS9Z36856-6XtGPxlop7XjVxPpAIsnQOZGO6ALXmu7JK2hkJgd7eNqwSE8WFSxYT8soFlzTc_pr0UqkSouO-1zIY7rsyAuNfLkIeIfuKiWBqy7ppla5Cso2-ssiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08203f0128.mp4?token=jAozGGCBgJul8yiPYT0jn3qH0P_EXis3jH7klFTMxkPF-8IO_94eGoFD8zdunzzsifjLiNA3u3g2vtZe-WspDfkssQB_Gk04mXzFQckKi7pqIRS68OVBssR2seWlBjSzFGLNeFPjYo_EDAPIINoJZ0DulZEhs4kn5vkCWU-WRQyYcweGpf5XSr8wKnCZPe9KME315Th-81vXNosn7slRXrudYXvS9Z36856-6XtGPxlop7XjVxPpAIsnQOZGO6ALXmu7JK2hkJgd7eNqwSE8WFSxYT8soFlzTc_pr0UqkSouO-1zIY7rsyAuNfLkIeIfuKiWBqy7ppla5Cso2-ssiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چهره‌ی دستیار ترامپ در کاخ‌سفید که حسابی وایرال شده‌است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/696627" target="_blank">📅 17:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696626">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6de472e16.mp4?token=UMDzhvmq960ErdLisBRRe98x-urylJqbC7VGKnmrbbK_Syne_dz3mUkHDVDyU8jTOnBrEE5Kgq0E7m4q6CUOuLR9Fg8kIkydgenOxW5Rxef4jY5wTyb38p9r90sw7GlOgV_e7-f2NNxIic2t0YwG_Ymg1knj0RtpEP_7PjiCw9E5dkKazzlV_0hYie1i2HcU0J0HcIti6RZMqcAHyfs3fKUKJSoqnLKKsvHYcElqyR20W3Pg_xJdoeLh7TjggsRCv-X3ghX6tUhlf0rYoa7mywLK_DJrKJ-RXEebOSAL_Ji_1_SY1AjDwAwGfxykrXA-m46WNmH9lLjvGprKnuDQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6de472e16.mp4?token=UMDzhvmq960ErdLisBRRe98x-urylJqbC7VGKnmrbbK_Syne_dz3mUkHDVDyU8jTOnBrEE5Kgq0E7m4q6CUOuLR9Fg8kIkydgenOxW5Rxef4jY5wTyb38p9r90sw7GlOgV_e7-f2NNxIic2t0YwG_Ymg1knj0RtpEP_7PjiCw9E5dkKazzlV_0hYie1i2HcU0J0HcIti6RZMqcAHyfs3fKUKJSoqnLKKsvHYcElqyR20W3Pg_xJdoeLh7TjggsRCv-X3ghX6tUhlf0rYoa7mywLK_DJrKJ-RXEebOSAL_Ji_1_SY1AjDwAwGfxykrXA-m46WNmH9lLjvGprKnuDQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای روبیو: هیچ کاری علیه ایران وجود ندارد که بخواهیم یا لازم باشد انجام دهیم و هنوز نتوانیم آن را انجام دهیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/696626" target="_blank">📅 17:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696625">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFEWHxaKMGAER4ewUF_3HBIvIIKnJyWWAcKNJlepdW5ltV8zeWo3wQ1bsH8aMYSsSySwyGSXXpY2nZqwXJ1Ay6GbOehat5K5WGNBsdBgTLsZhsX7MQSZASTaCyhvlavNvAO5GrED7Lxnzvrg31pC3djRRxnhG_xVi7Y7CYuQlSbwOATkiUqll9WlWvL6wU1BOiCm3Rj7I5HA5PRvoJRKBpbZ5p8hM4uDdFA9gyVUk6LmirgoFLQDB6Z4vQmRkmWDOrHQALGlFthOlsS_-7FjnjvOG58O3F2SP0IplFLHV6Bn8be9zXyhdmTNwv3jRn0wyQvvhxTfwg3UxMYrCBZ3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسجد Dimaukom در فیلیپین که به مسجد صورتی معروف است؛ رنگ صورتی اين مسجد که توسط مردم محلی ساخته شده نمادی از صلح در نظر گرفته شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/696625" target="_blank">📅 17:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696624">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
یک مقام ارشد نظامی پاکستان که نخواست نامش فاش شود، به نیویورک‌تایمز: از جنگنده‌های نیروی هوایی پاکستان در حملات علیه حوثی‌ها استفاده شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/696624" target="_blank">📅 16:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696623">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
مهلت انتخاب رشته آزمون‌های سراسری و دانشجو معلم تا یکشنبه ۱۹ مهر تمدید شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696623" target="_blank">📅 16:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696620">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی: در حال تشدید محاصره ایران هستیم  یک مقام آمریکایی در گفتگو با الجزیره:
🔹
نیروهای ما از اواسط ماه ژوئیه، در چارچوب محاصره بنادر ایران، مسیر ۱۳۰ کشتی را تغییر داده‌اند.
🔹
ما در حال تشدید محاصره ایران هستیم که از نظر اقتصادی دچار مشکل شده…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/696620" target="_blank">📅 16:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696619">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
معاون‌اول رئیس‌جمهور: در مرحلهٔ نهایی‌کردن تامین منابع برای افزایش رقم کالابرگ قرار داریم؛ همین روزها کالابرگ افزایش پیدا می‌کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696619" target="_blank">📅 16:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696618">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
یمن خطاب به کارکنان تأسیسات نفتی عربستان: از تأسیسات نفتی دور بمانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/696618" target="_blank">📅 16:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696617">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
رئیس سازمان انرژی اتمی: از حق غنی‌سازی کوتاه نمی‌آییم و اورانیوم را هم به کسی تحویل نمی‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/696617" target="_blank">📅 16:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdedba5cc6.mp4?token=TZInyn8Ox6jb0LGWjU8a6zS8jkdtDnLoR_ABlh7pkUjrHbhUAcT7wakHmdCbbUuiz0eusMx--zpMkSckymPIqvvMeZC2i4OeuhMEyZkWmw_CxxqLSGwOOJf7s11paRZtU2ofiZoSt4gb7JEB01iOK0BuGWYX_bLq2nTrJf8_BabZ0YPtdWrGGQDdRxdQI6cB8m4F60--0d3jlPkRADhU5JwywJu2bVFVVCSh81PMTjbNfW-82cPk6OzMvos1gcmMzbLN9FkmDNO3-Kga9Bzj4s2s9y_ByQCWrYp-HNyNOCUX5RHlUc-fjWbnMt4qu4AF_WjBksh9l0yI2UFlznDUtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdedba5cc6.mp4?token=TZInyn8Ox6jb0LGWjU8a6zS8jkdtDnLoR_ABlh7pkUjrHbhUAcT7wakHmdCbbUuiz0eusMx--zpMkSckymPIqvvMeZC2i4OeuhMEyZkWmw_CxxqLSGwOOJf7s11paRZtU2ofiZoSt4gb7JEB01iOK0BuGWYX_bLq2nTrJf8_BabZ0YPtdWrGGQDdRxdQI6cB8m4F60--0d3jlPkRADhU5JwywJu2bVFVVCSh81PMTjbNfW-82cPk6OzMvos1gcmMzbLN9FkmDNO3-Kga9Bzj4s2s9y_ByQCWrYp-HNyNOCUX5RHlUc-fjWbnMt4qu4AF_WjBksh9l0yI2UFlznDUtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیژن زنگنه باز هم صحبت نکرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/696616" target="_blank">📅 15:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae83d6942e.mp4?token=Uy0P4ImgNz8njxnz4YzetOxf2lanSkRuqYtMCEVmWmgdiW4hZfqCkoJQ1cGKYrDPlDM7MF-dki5wvhobrpo4RokE0XF5zJ8cxht59yZLR9D6k263ltV1wt0jW8YFae4NvIdR5V0x4cHuv7MYWveColHPq3jxeDXeVCtEMYZ4PQuadJvoICsnZ0uVDV0aGOFMUk4UEPEcLlHaypBymhm98wlhBI2worWgp_KPWDnOrTmvqshqmpGEhxCSveF3XQ996w3J6WaCJxZjjG7o3PEsjZynT2z5TV_JZoCi4NNYuHpHxhHxxF-X6XcHgaiRDAVGIyb11vKhusdXEQiglab5KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae83d6942e.mp4?token=Uy0P4ImgNz8njxnz4YzetOxf2lanSkRuqYtMCEVmWmgdiW4hZfqCkoJQ1cGKYrDPlDM7MF-dki5wvhobrpo4RokE0XF5zJ8cxht59yZLR9D6k263ltV1wt0jW8YFae4NvIdR5V0x4cHuv7MYWveColHPq3jxeDXeVCtEMYZ4PQuadJvoICsnZ0uVDV0aGOFMUk4UEPEcLlHaypBymhm98wlhBI2worWgp_KPWDnOrTmvqshqmpGEhxCSveF3XQ996w3J6WaCJxZjjG7o3PEsjZynT2z5TV_JZoCi4NNYuHpHxhHxxF-X6XcHgaiRDAVGIyb11vKhusdXEQiglab5KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افزایش کالابرگ از تورم عقب ماند
🔹
۹ ماه از اجرای طرح کالابرگ گذشته و حالا صحبت از افزایش ۳۰ تا ۵۰ درصدی اعتبار اون مطرح شده، اما قیمت کالاهای اساسی در این مدت چقدر بالا رفته؟
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696615" target="_blank">📅 15:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cac921445.mp4?token=ZFDvBaonLBIQYT_VbjnW9MttRA6ENRe8pdYsPkA6Oquvi3IuLT6yhZUE2-jfZDsDd0fmR3B7GqPRgpGP6Q3_NphcxAGxSw4Ji1vB98gYI57mLW21bNYoUafEknSB65UhEtwNYS_D0d3WK3ISeBBtwmVSwebd3AtDxMxSoUjJJVvx9LAVzt0dUxRR3vTNL1Ch4u9NTRUAuQC7s9xBO9aihtrSZv88NdF-Yn5aLQMixOOLvKIOs2UwD53HVfhd47eq5Wo7LTv475t6gYT2Dje3k3T4hiB07Ugb3TSxIgwCea5Q3KRX0nLj2zbuwDXak5ThPYKL9hcseEx8qYDPH6iinyMpvKbuzn3LYKdPgDsNs1jNnIqURslYyrsQCqPWiHZO1HUNA42uUGMtxthmj_0Z7poGj6SARCrZUDDh-d7tHjmWO3UchfvwqrEGZIccY_dvikji39_1tRTjiFrrPkfiXbxk2OyAiEMhlFBHL9yNKFG3pmtngeG6l-8JyfWJnaClX5v7WNIUmWEOk0INzWgYOsXQFAoMBGnFxNqw__YK2Qg-q9qlkgbtsYVcx95Radem_m2i5wa7AWw3HWMYh27UmpWqfZNYc5Eh5GMNIe1o2lv1xSI2LAGwx2Uu-WNS24Fxxaath3xYNk6F-qfiy2bQgj4kGIw91DjIaRCg2KG53fM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cac921445.mp4?token=ZFDvBaonLBIQYT_VbjnW9MttRA6ENRe8pdYsPkA6Oquvi3IuLT6yhZUE2-jfZDsDd0fmR3B7GqPRgpGP6Q3_NphcxAGxSw4Ji1vB98gYI57mLW21bNYoUafEknSB65UhEtwNYS_D0d3WK3ISeBBtwmVSwebd3AtDxMxSoUjJJVvx9LAVzt0dUxRR3vTNL1Ch4u9NTRUAuQC7s9xBO9aihtrSZv88NdF-Yn5aLQMixOOLvKIOs2UwD53HVfhd47eq5Wo7LTv475t6gYT2Dje3k3T4hiB07Ugb3TSxIgwCea5Q3KRX0nLj2zbuwDXak5ThPYKL9hcseEx8qYDPH6iinyMpvKbuzn3LYKdPgDsNs1jNnIqURslYyrsQCqPWiHZO1HUNA42uUGMtxthmj_0Z7poGj6SARCrZUDDh-d7tHjmWO3UchfvwqrEGZIccY_dvikji39_1tRTjiFrrPkfiXbxk2OyAiEMhlFBHL9yNKFG3pmtngeG6l-8JyfWJnaClX5v7WNIUmWEOk0INzWgYOsXQFAoMBGnFxNqw__YK2Qg-q9qlkgbtsYVcx95Radem_m2i5wa7AWw3HWMYh27UmpWqfZNYc5Eh5GMNIe1o2lv1xSI2LAGwx2Uu-WNS24Fxxaath3xYNk6F-qfiy2bQgj4kGIw91DjIaRCg2KG53fM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر ارتباطات: هنر، برگشتن و خدمت به ایران است
🔹
در دیدار با جمعی از افتخارآفرینان المپیاد نجوم و اخترفیزیک، از تلاش و موفقیت این جوانان نخبه تقدیر و درباره دغدغه‌ها و مسیر پیش روی آنان در حوزه علم و فناوری گفت‌وگو شد.
🔹
وزیر ارتباطات در این دیدار با تأکید بر اهمیت نقش نخبگان در آینده کشور گفت: رفتن نخبه‌ها ایرادی ندارد، اما هنر این است که بازگردند و دانش و توان خود را در مسیر پیشرفت و خدمت به ایران به کار بگیرند.
🔹
در این دیدار همچنین بر ضرورت تقویت ارتباط میان دانشگاه، دولت و استعدادهای برتر و استفاده از ظرفیت‌های وزارت ارتباطات و مجموعه‌های تابعه برای حمایت از مسیر رشد و شکوفایی این استعدادها تأکید شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/696614" target="_blank">📅 15:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff5c17f96.mp4?token=Hj1_6uVFdp-EHlbZ0DJ8uh17RYCN-5RcFkVLp9GIsfamEHKd1dhbnzN_tpLDNH4ccjBNm44XEGYaEktif2r5JnPRs7Dg_AigT11xkPEZEdXM3kUsu_PmYrvBpAUn4MdwXSKggWcWFuZkhA2BVTAzDfLBqyC4v31X2VTzX_uFUopxjdXTEW_bT5Q7wobA_ATUcuyR-LaXJAlE6hZKFOdCNWLX_GaFSjYW1RwT98N4QwPuz0kGw1Q3v-4yJ5MZcTSQj3v_DzfTy_k1j5MAItRJAcOEb9o4B4Ec1Zy3oLXCtYdQXg8-tnVc5lK20RUkSnNGl_p736DPeK0CJpWsNKLETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff5c17f96.mp4?token=Hj1_6uVFdp-EHlbZ0DJ8uh17RYCN-5RcFkVLp9GIsfamEHKd1dhbnzN_tpLDNH4ccjBNm44XEGYaEktif2r5JnPRs7Dg_AigT11xkPEZEdXM3kUsu_PmYrvBpAUn4MdwXSKggWcWFuZkhA2BVTAzDfLBqyC4v31X2VTzX_uFUopxjdXTEW_bT5Q7wobA_ATUcuyR-LaXJAlE6hZKFOdCNWLX_GaFSjYW1RwT98N4QwPuz0kGw1Q3v-4yJ5MZcTSQj3v_DzfTy_k1j5MAItRJAcOEb9o4B4Ec1Zy3oLXCtYdQXg8-tnVc5lK20RUkSnNGl_p736DPeK0CJpWsNKLETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمد مخبر، مشاور و دستیار رهبر معظم انقلاب: تنگه هرمز تحت هیچ شرایطی بازگشایی نخواهد شد مگر اینکه مشکلات کشور حل شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/696613" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
مدنی زاده، وزیر اقتصاد: می‌دانیم تورم و گرانی مردم را اذیت می‌کند ولی بسته حمایتی دولت مصوب شود خبرهای خوبی برای مردم خواهیم داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/696612" target="_blank">📅 15:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
وزارت بهداشت: تاکنون هیچ مورد مثبت یا حتی مشکوکی درمورد بیماری طاعون، گزارش نشده است
🔹
طاعون یک بیماری باکتریایی است و بیماری باکتریایی، برخلاف بیماری ویروسی، اگر زود تشخیص داده شود قابل درمان است؛ یعنی با آنتی‌بیوتیک قابل درمان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/696611" target="_blank">📅 15:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/027db46971.mp4?token=GW9bg67P7XV_BI6976sh5RzKV03AHCah5aPKqIPNJDmD1ELZPhPTUfdMF4GQ55YBye5FSIIpKJ-o2jDRB5OzK3z4q7C4J2fE1Oqag_ODPOjYFx2o9w3MNyEr4OGJF_6D1-_fRn8Vk9zFWfRpMTEEMAk1BUh_vRWysEy036_9JFxxg2Vt2oUkFijZHhx2vbWet_EadMz3elcrGQKPdb9_7Sq484-IeCR9SvWXDkAA0saAmNhwiprU4ey-6UfQzMu5Lyiqob5nC0ugDCr4m-OfWmh8mgJKZPppWHUN_8ptOiorACL3m1NdvhATJWiI5QAHTT3O1WCqkIL_ms7sCGHSPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/027db46971.mp4?token=GW9bg67P7XV_BI6976sh5RzKV03AHCah5aPKqIPNJDmD1ELZPhPTUfdMF4GQ55YBye5FSIIpKJ-o2jDRB5OzK3z4q7C4J2fE1Oqag_ODPOjYFx2o9w3MNyEr4OGJF_6D1-_fRn8Vk9zFWfRpMTEEMAk1BUh_vRWysEy036_9JFxxg2Vt2oUkFijZHhx2vbWet_EadMz3elcrGQKPdb9_7Sq484-IeCR9SvWXDkAA0saAmNhwiprU4ey-6UfQzMu5Lyiqob5nC0ugDCr4m-OfWmh8mgJKZPppWHUN_8ptOiorACL3m1NdvhATJWiI5QAHTT3O1WCqkIL_ms7sCGHSPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از فرودگاه بین‌المللی ریاض پس‌از مورد هدف قرار گرفتن توسط یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/696610" target="_blank">📅 15:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3da572ff8.mp4?token=b3BXcH0nw_-N2qg5Sey15Ktmbmqbd-ExGt5LqQWa0ZcDHNQHtL0rTyG4YOaYX_XZLv8UFfEDpv19xaDgfnkjiXEwmx80wzHr7rzqjBsq518DpQog6vGtzJfUaFRi3CU0lRtUMvifGTqQaduuzairNKpaldbi3Mnm8lLsPu7vHcru6SOIumCw0N2ISMGRq7bb92GQ2WekcrOrjKSNXwI95WsynqRpB9mcD94tmVHU37VOC2Lcal5kapPbe1-sDOFf7jFmLsdM-WonsMQMgZ77fpQbZaLxOPIqcOH5Cn4JlFDUDLRKl7a22dsVmOXrMABlooP0P1_Fp4t5O77wn0TiRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3da572ff8.mp4?token=b3BXcH0nw_-N2qg5Sey15Ktmbmqbd-ExGt5LqQWa0ZcDHNQHtL0rTyG4YOaYX_XZLv8UFfEDpv19xaDgfnkjiXEwmx80wzHr7rzqjBsq518DpQog6vGtzJfUaFRi3CU0lRtUMvifGTqQaduuzairNKpaldbi3Mnm8lLsPu7vHcru6SOIumCw0N2ISMGRq7bb92GQ2WekcrOrjKSNXwI95WsynqRpB9mcD94tmVHU37VOC2Lcal5kapPbe1-sDOFf7jFmLsdM-WonsMQMgZ77fpQbZaLxOPIqcOH5Cn4JlFDUDLRKl7a22dsVmOXrMABlooP0P1_Fp4t5O77wn0TiRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به راحتی از صدا و دود موتور متوجه مشکل ماشینت بشو!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/696609" target="_blank">📅 15:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696607">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سخنگوی کرملین: اگر ایران خروج از NPT را در دستور کار قرار دهد و واقعاً برنامه‌ای برای خروج از پیمان منع گسترش سلاح‌های هسته‌ای داشته باشد، این مسئله در دیدار رؤسای جمهور ایران و روسیه مطرح خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/696607" target="_blank">📅 15:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696606">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27086a1605.mp4?token=EOZVR4JybzJ3RCefKjwnbKziRigHmXQpGjOZgMPsJDH_TebhrvgDTEqnmxN7ijroyeTgGnVYmM-lYHBSN1oG4Z3NNHW0i0BMaVHxBy69e5PA1o6J2qWVGd6QRsIeALYuIZXTWhS-KDnyyg8EJFFDDltbr0Ekxm_2JiSnVIxQQy047TsvktRPN3_QDl-oIwRNkL2iZvgbt5YAR0CzICyrKbvt3Tujj1u7fb3DcPRIcecQBbAJzhrEzY7J0N3PHIy_u7d_LaCvvAHt3rHOhhGv5gfkpYg0IFevYy7YUE7RWTfeB3Li0hWegNinyIDPwxOCcd2Hv9ho8E8kq70RLqJ05g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27086a1605.mp4?token=EOZVR4JybzJ3RCefKjwnbKziRigHmXQpGjOZgMPsJDH_TebhrvgDTEqnmxN7ijroyeTgGnVYmM-lYHBSN1oG4Z3NNHW0i0BMaVHxBy69e5PA1o6J2qWVGd6QRsIeALYuIZXTWhS-KDnyyg8EJFFDDltbr0Ekxm_2JiSnVIxQQy047TsvktRPN3_QDl-oIwRNkL2iZvgbt5YAR0CzICyrKbvt3Tujj1u7fb3DcPRIcecQBbAJzhrEzY7J0N3PHIy_u7d_LaCvvAHt3rHOhhGv5gfkpYg0IFevYy7YUE7RWTfeB3Li0hWegNinyIDPwxOCcd2Hv9ho8E8kq70RLqJ05g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: روند مذاکرات ادامه دارد؛ ظرف چند روز به پیشنهاد آمریکا پاسخ می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/696606" target="_blank">📅 15:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696605">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82810059df.mp4?token=oxoNZ0Ly89YI63MDvvUOU6JgCjafImf0ZK4m0q_5XLwXpMphAglSLHcwLkz0Xn_OLNObW7vXdo9mG7pDRwjYVuW-E5aMSk9e2sVZiGFmRK405ZIWQoPMoq_aDJStu0IZE03weB-KrhKqMkdTWugrCouHMdNHoqlVX25oaJZ2il7dzv09HfFc3Bl3AydGQpajuK6TLAMhwMIh5YvjETyr6XH65T6icxZy6j-aPAANq9WOQ7iIOdyTxULd_rRHhxSOivabFCduTBxQcDAJ3xM_J7pGk7-XkkwyImmKfXK8eLaBbmdj3VIoXT6Fg4NBvMv_MqnEcoIzeNvrxWet5lOwAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82810059df.mp4?token=oxoNZ0Ly89YI63MDvvUOU6JgCjafImf0ZK4m0q_5XLwXpMphAglSLHcwLkz0Xn_OLNObW7vXdo9mG7pDRwjYVuW-E5aMSk9e2sVZiGFmRK405ZIWQoPMoq_aDJStu0IZE03weB-KrhKqMkdTWugrCouHMdNHoqlVX25oaJZ2il7dzv09HfFc3Bl3AydGQpajuK6TLAMhwMIh5YvjETyr6XH65T6icxZy6j-aPAANq9WOQ7iIOdyTxULd_rRHhxSOivabFCduTBxQcDAJ3xM_J7pGk7-XkkwyImmKfXK8eLaBbmdj3VIoXT6Fg4NBvMv_MqnEcoIzeNvrxWet5lOwAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا فکر کردی چرا آسمون آبیه؟ #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/696605" target="_blank">📅 15:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696604">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ترامپ: اعزام نیروهای ترکیه و پاکستان به عربستان عالی است #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/696604" target="_blank">📅 15:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696603">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFpK5BHxXLtK2QENjzBpKa1g6qir-pnTHUoM9jVN-Zngs6sXp9tbUbfniloWZYUzD6IKZbMjHN8wdTgDIIZ1HiNaihlTKw44yiC3gLQJmc_xeAZhphU3Pdk469PVsraIqOSGmURHLl3qGL5U6LAczNnB7Sbjw5B5eWASV5mc85eYUFUrDxLaV8syYMvJKIfFULMRM59nqcO8_DAH_uxvrN5l4C1MnEOnQtlo_IW2DHPY2EnJ2F2OqAmnPlT-gpuZNrh3TpxldpEyHp1XmMhs_zBh_EbFjDsC-c6emBdg-RhcXfeqc7Wk6Jp0rixFZldeRIRCqrO7rbGOrY9EFIBxoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایتخت زرشک ایران، افینِ خراسان جنوبی
🇮🇷
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/696603" target="_blank">📅 14:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696602">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
افزایش اعتبار کالابرگ منتفی نشد
🔹
پیگیری خبرنگار خبرفوری از وزارت تعاون، کار و رفاه اجتماعی نشان می‌دهد اجرای طرح افزایش اعتبار کالابرگ به دلیل نهایی نشدن میزان منابع و تعداد دقیق مشمولان، به روزهای آینده موکول شده است.
🔹
این وزارتخانه اعلام کرده که تیم اقتصادی…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/696602" target="_blank">📅 14:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTIymsCVr9b5sv8-doFGeAfs4twZxeTNnlmdd3delrsLfWhmm3voiQ31wPenXIByDKZxNiZKX9o89ATgHEyO7ap5QlfUUdQG-m3bjjzXQ5B-LdTl38C48YMuuVvbl_FZJkIYM_uk_cFzOg_8Z84IzIW-GehZbdEr-aAVZA_Neg9UZzD6BlV1rcD9yMHeQ_YPjnCmVfLm3pKrU0uLKRMDigS9a-4-YAumIIbQvOLXTjnDPpBurgdD8IcKps-AqS6PJcFReGojqo2LmcSaTTdvDJith2E7RMeIdZlVbpms77N67RoQ-OS82PmCGovf1vAVOQXmpWLlnbQD33E_qys9YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: فاصله شما با ما را موشک‌های ما تعیین می کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/696599" target="_blank">📅 14:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696598">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای وزیر خارجه آمریکا: ایران با فشار اقتصادی عظیمی روبرو است که در چند هفته آینده به طور قابل توجهی بدتر خواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/696598" target="_blank">📅 14:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696597">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6f3d30.mp4?token=aketzeUqbayKFaK79ZUcirYo9DOQDFZtVnXLwpJMwbEHE32XQyHUtMAxZpeoXn8LS78bzn0aA-eovsZ6EmbAywSlO3e8kdRuphV1AdFdDsH-Qtp1MSqotS--c6RCXMKmE8cr1pGkE6559w08hJWKqSkwJvYaWkZrXqKwG-dJqr54exwQ1TgB4uFeG2y2UV1r60Xud7ekaoGFgjkLhmxorPVDSorRH7eyYph7Z6GEb412LehwFOI7g27OmfFycJcb9IDFzDtk1v2bcSoqz-U49GR7YSDQatXBllpBHqfNUnEYguk7F0W8SBA-wVUQvH1wBY7c58PSqRlDyn-LcwvZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6f3d30.mp4?token=aketzeUqbayKFaK79ZUcirYo9DOQDFZtVnXLwpJMwbEHE32XQyHUtMAxZpeoXn8LS78bzn0aA-eovsZ6EmbAywSlO3e8kdRuphV1AdFdDsH-Qtp1MSqotS--c6RCXMKmE8cr1pGkE6559w08hJWKqSkwJvYaWkZrXqKwG-dJqr54exwQ1TgB4uFeG2y2UV1r60Xud7ekaoGFgjkLhmxorPVDSorRH7eyYph7Z6GEb412LehwFOI7g27OmfFycJcb9IDFzDtk1v2bcSoqz-U49GR7YSDQatXBllpBHqfNUnEYguk7F0W8SBA-wVUQvH1wBY7c58PSqRlDyn-LcwvZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با هر مدل شلوار چه کفشی رو نباید بپوشیم؟
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/696597" target="_blank">📅 14:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696596">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای وزیر خارجه آمریکا: ایران با فشار اقتصادی عظیمی روبرو است که در چند هفته آینده به طور قابل توجهی بدتر خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/696596" target="_blank">📅 14:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696593">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFaoN9u5Cb_DGynyQsurxL76gxT00Mh8fwOQJBZn1GPoZwrlBlF26QKRuwT0osRTygyMuOlCuCRGRQzS-nXmcgZokLRtQZApXkkIGq9Chi1blGa84NvkHt-rVpYHv15Qyh9aQ8W6Jtwdp2lexEHJNBNhzHqPMeMX7kMXyd4gQYV0x8BvB5tIZy7bM3Uf7khtFULR9e8D4JnYxEZxQfMrBoGo-vQs9SFR-J_0XAa5uXBpJZYQE62sgMv_rzzhkjaiHi6kClNwqhlIwo_t1Wv1crGVwcTokPitmkt7XUEnWBC-_SPzTkIDnewhaUe_JlfmfiXGB2OWGaSVu01y5gwqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKDHmBUDEPDngzK-d1t2KaBUWctoQQRMnwhuiAOFMcIU-qP0nCbuBAhkEethldPkwJXfIy-AC4YUxL68Gk70tj17QCxjFjCvy3T3vRxl2K2Rzm_ZxPAEJBdbB46Zf3mmCTpnBRA7jlKHuyIbxEFoo4g9Ox9YQZBlKP5xjfjykwlXYiyaYI7qkCbsIRBo8DKuEp0jHYNeKZb8Tqhy-gUwnlorco14iWke2MjIeDMMjoFG-y13KRh0IW9fd1GZLwCFFwE4qGPTqttGDbUvYkiEZxdbYOeAbfkMqyYha4ZGDtH75Zd1bVs5dzrVzcHZ5wNleGOHQ9KNr1VUsxxhx3KR9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fca78e9d.mp4?token=qG7wZfaEkpfGKrazOEu5DdglN6wmvvhXnz65u20ure4oE5hHbdpxH0ZHVJpCM-GTVp8jkr65igVQ4Stgksam7Z-zKF8G0KbhFzxP2snGmbMO4qJIREknALySuH3fAz7VpytJT3a33GwIyQzSFfFV2byvLLUklJsCbLuG2hPmhSuUOsOyjpe-c1wQkDj-VhyBoKzvulyXA3iuVw9d9Leidl84WJuYCC3a2bH4errZGz0o2dRrKtH-60WGvza1v917luRcQQPPelPjt44bEzUKnfYjUmkUJsF0kPqd6ufxrf1CMNDy2c4G36rNZQ-eH2HBr-9Vs3Y9c6hkeVo5nVP7Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fca78e9d.mp4?token=qG7wZfaEkpfGKrazOEu5DdglN6wmvvhXnz65u20ure4oE5hHbdpxH0ZHVJpCM-GTVp8jkr65igVQ4Stgksam7Z-zKF8G0KbhFzxP2snGmbMO4qJIREknALySuH3fAz7VpytJT3a33GwIyQzSFfFV2byvLLUklJsCbLuG2hPmhSuUOsOyjpe-c1wQkDj-VhyBoKzvulyXA3iuVw9d9Leidl84WJuYCC3a2bH4errZGz0o2dRrKtH-60WGvza1v917luRcQQPPelPjt44bEzUKnfYjUmkUJsF0kPqd6ufxrf1CMNDy2c4G36rNZQ-eH2HBr-9Vs3Y9c6hkeVo5nVP7Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در نزدیکی سواحل امارات رصد شد؛ به نظر می‌رسد یک کشتی هدف قرار گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/696593" target="_blank">📅 13:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696592">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3008a4a83.mp4?token=V_HhfNAkubNkE2A4lbZY_VYBT5Fa0ku9O04v0vuPwBP0HIiygSfVvwPlkBPo1O7oWw3gtW_iu-FBjjL8Zde1-h0Yt9GUMctHTKQ2zfuTBZrU_n0sN1_UkZgvGkltZ07MFai4dL4zkojy7yX-0qYOqLoiI6MwYcvxA7kAZaikZ2-CE8S5WNOBkd-JlTZ1f6K_55aYZ0vBb231ZldEJEoAhFOmK1PFuyDEcoTaV9wCULQMZXTWM0U8rJwWnl6q6QOY3u7_HqTjSx2dG5aVIvgTSM_AlM4SFItG3OTYSZTHhszSzohXmYZBamEgKI_0OBsU8cHP2MYYDZsSsm0Kr267uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3008a4a83.mp4?token=V_HhfNAkubNkE2A4lbZY_VYBT5Fa0ku9O04v0vuPwBP0HIiygSfVvwPlkBPo1O7oWw3gtW_iu-FBjjL8Zde1-h0Yt9GUMctHTKQ2zfuTBZrU_n0sN1_UkZgvGkltZ07MFai4dL4zkojy7yX-0qYOqLoiI6MwYcvxA7kAZaikZ2-CE8S5WNOBkd-JlTZ1f6K_55aYZ0vBb231ZldEJEoAhFOmK1PFuyDEcoTaV9wCULQMZXTWM0U8rJwWnl6q6QOY3u7_HqTjSx2dG5aVIvgTSM_AlM4SFItG3OTYSZTHhszSzohXmYZBamEgKI_0OBsU8cHP2MYYDZsSsm0Kr267uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/696592" target="_blank">📅 13:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSe0vd4zNNcqqVd91_b5YkEw6gEyh9qNWGvz15lzehhOX9J7egHP0BUn1DMDF8FXZFUe_2l_n7qofvEkdbn9m2VgrPrufVJsCONjErlliTisEuWENCleo4621YmKnE-nQF3dYz64Od81h9yxIDcaRRiBStQHUO3JQZ3vFiZO9XgAOCEP_VALdAaKvRTDQDHWMzBWIv5g3N6CE5O7eG7pl5AIJyggw4PWJSvl7B49qot7LcIdOOl3ITPl0376gKiRzyKFCevHmOxCknr0OVkl_q80kVeXtZypNHFsX5TlYT3m808u0a3t2r0AlcAOQaMjj4g2lqFZ_T8Z-j_OoznTbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دوران آتش‌بس، غزه فقط ۳۶ روز آرام بود
🔸
اسرائیل در ۳۲۵ روز از ۳۶۱ روز آتش‌بس به غزه حمله کرده و تنها ۳۶ روز بدون گزارش حمله، مرگ یا مجروحیت سپری شده است.
🔸
با وجود تداوم این حملات، ایالات متحده همچنان معتقد است که آتش‌بس در غزه برقرار است.
@amarfact</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/696590" target="_blank">📅 13:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f438b7327f.mp4?token=a5smVndnLTl0JlFzIG_nQoVQ0g5wpCn4iMffWLW9ta9PEDVwYtvaYSmABQKcxWBqBB-GY427P5rWAINSSSWNBFByw0p8oFHL-H-yiNkkes_Z685SE59lPkvElyln1EZ9IjwNuWzUz7Z079qgVGRQsKJarO9c4ajCwD_l0gTAOFX1p279QA-dpzO2LnOseMGRQqLN24qhpb1M4zrai4l-Y8NB7sMIy1hrte4j5Hyml8yDamJMgPFkFU-cDQLTgRUjiany1Qf21SzNKdovFjh3g3AABk7s-aXIQiz2uqs-crGY1y-kzNlQKYSFsaOTuDlJLJ8tQuBm-rcJdn2RfYwHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f438b7327f.mp4?token=a5smVndnLTl0JlFzIG_nQoVQ0g5wpCn4iMffWLW9ta9PEDVwYtvaYSmABQKcxWBqBB-GY427P5rWAINSSSWNBFByw0p8oFHL-H-yiNkkes_Z685SE59lPkvElyln1EZ9IjwNuWzUz7Z079qgVGRQsKJarO9c4ajCwD_l0gTAOFX1p279QA-dpzO2LnOseMGRQqLN24qhpb1M4zrai4l-Y8NB7sMIy1hrte4j5Hyml8yDamJMgPFkFU-cDQLTgRUjiany1Qf21SzNKdovFjh3g3AABk7s-aXIQiz2uqs-crGY1y-kzNlQKYSFsaOTuDlJLJ8tQuBm-rcJdn2RfYwHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جوگیری به سبک مکزیکی
🇲🇽
🔹
یک کشتی‌گیر در مکزیک با کوبیدن داور ۷۵ ساله به تشک باعث مرگ او شد. این ورزشکار بازداشت و پرونده‌ای با عنوان مرگ ناشی از بی‌احتیاطی برای او تشکیل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/696589" target="_blank">📅 13:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF8q3FnVzABcj8Khvo4uxl0u2ZreAYRz8lbOhCxG3sdReLdqiuMZQMUHBceaSTSl_RYbkVmfVGpV8em7Jy7IaoHsg99_SZ_M8gKQGzYqx13Os7oY31qqLU2UEjwDYJHCM3eZy1dUU01BuS78D63FBy5kIhrHTIS7snJ1XoJt5qcxcqSpGAaJbOEn8cjAvuhpfKMYICBMwllcA8Y_UCj4PkFIeARSIxDOsv-rJiWSKdUFuuIEExLKTSBmA2L_jePzGC3aGJ2V-7zoz7kfUjwvAJoYWPvrCitTybsBaF2BI2pGxLy0wWLBMt5V2ZNvb9ZNdtTnwvUCQBdDPN8hHncqnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلیس سیستان‌وبلوچستان: درپی حملهٔ تروریستی به گشت یگان تکاوری نصرت‌آباد، ستوان‌سوم‌ وحید عنایت به‌شهادت رسید
🔹
چند تن از مهاجمان مجروح و از صحنه متواری شدند.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/696588" target="_blank">📅 13:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ترامپ: اعزام نیروهای ترکیه و پاکستان به عربستان عالی است #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/696587" target="_blank">📅 13:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696586">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d9f202eaa.mp4?token=KTCOt2z4MXsADcKv2GEIl4Hn8ly0UGQT1IuofyJU2iJ_jsd4Ub5-cBGIbOqsw3hxjPzA6Y8Tz2i6dI-Vq_BCm8dOBNKVhNa8JPIoS5M0z8mS5qU_W7sFM796ZMhu_YpGPqTWwMKIWABPV-g_nXhai3-AuyIPOh2uc7RVsnXdEGen0GiZZezl_S2jW3VGdDN0D_T0EmkW8hYagYQNcPKwPEpjfO3TwMMChww-NGRKZX2YGW5yMR0QgtyR139ZgCL4XF4a6gA_niHjgAEoxVaKd2mC2VWMyFpJmulfvAGh6wfL-2cxfAePi-tNU__dOMLGDRugXyK-rsqsFHSLA-4mFJBhULgsUPmEu5sv2Uzvn69BI7Kq4sZuiCPZz2R-Yu_6Cth0Z5qDdbv8MLy0lU4FdqX5qZsUb-kH4927HO3gKV0iCRYkW5w5AhRHaolCgsSm_7b7Z-IRW4whk09fjomlzLSzMn6ib0txMvAUyFpZXbaujiBD3xpQVv1_dVgANJL-iAYgj9EHrL9XbgQarQiWxzx4lJ1Fbyy9MYbfXpYr_EMGw19viYcxgoIr_uywnIs8I2ZtPtY9yRcJ_mh9ikJiFG5GcqB__FSvKhYhT0k18YLb0G5g-VMfZryC_qznApSyOWmB5bowMT7wd5CyNwahWuk3SjJzHQfiMGQcxxCv0D0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d9f202eaa.mp4?token=KTCOt2z4MXsADcKv2GEIl4Hn8ly0UGQT1IuofyJU2iJ_jsd4Ub5-cBGIbOqsw3hxjPzA6Y8Tz2i6dI-Vq_BCm8dOBNKVhNa8JPIoS5M0z8mS5qU_W7sFM796ZMhu_YpGPqTWwMKIWABPV-g_nXhai3-AuyIPOh2uc7RVsnXdEGen0GiZZezl_S2jW3VGdDN0D_T0EmkW8hYagYQNcPKwPEpjfO3TwMMChww-NGRKZX2YGW5yMR0QgtyR139ZgCL4XF4a6gA_niHjgAEoxVaKd2mC2VWMyFpJmulfvAGh6wfL-2cxfAePi-tNU__dOMLGDRugXyK-rsqsFHSLA-4mFJBhULgsUPmEu5sv2Uzvn69BI7Kq4sZuiCPZz2R-Yu_6Cth0Z5qDdbv8MLy0lU4FdqX5qZsUb-kH4927HO3gKV0iCRYkW5w5AhRHaolCgsSm_7b7Z-IRW4whk09fjomlzLSzMn6ib0txMvAUyFpZXbaujiBD3xpQVv1_dVgANJL-iAYgj9EHrL9XbgQarQiWxzx4lJ1Fbyy9MYbfXpYr_EMGw19viYcxgoIr_uywnIs8I2ZtPtY9yRcJ_mh9ikJiFG5GcqB__FSvKhYhT0k18YLb0G5g-VMfZryC_qznApSyOWmB5bowMT7wd5CyNwahWuk3SjJzHQfiMGQcxxCv0D0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ تولید داخل به یک نیاز عملیاتی؛ تجهیزات جدید آتش‌نشانی رونمایی شد
🔹
در افتتاحیه نمایشگاه ایمنی و آتش‌نشانی و با حضور دکتر محمدی، مدیرعامل سازمان آتش‌نشانی تهران و دکتر نصرتی، رئیس سازمان شهرداری‌ها و دهیاری‌های کشور، اعلام شد ۶ گروه محصول تخصصی و عملیاتی آتش‌نشانی برای نخستین‌بار در کشور و با کیفیت قابل رقابت با نمونه‌های وارداتی، توسط تولیدکننده باسابقه ایرانی به تولید انبوه رسیده است.
🔹
در این مراسم از نازل‌های تخصصی توربو، تجهیزات خط فوم و سه‌راهی‌های آتش‌نشانی تولید شرکت آریاکوپلینگ رونمایی شد؛ تجهیزاتی که تولید داخلی آنها، ضمن پاسخ به نیاز عملیاتی آتش‌نشانی‌ها، وابستگی به واردات را در صنعت حساس آتش‌نشانی کاهش می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/696586" target="_blank">📅 13:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
هدیه ویژه به نوزادان تهرانی
«چشم‌روشنی» شهرداری تهران برای مادران تهرانی فعال شد
🔹
شهرداری تهران در اقدامی هدفمند، طرح «چشم‌روشنی» را در اپلیکیشن شهرزاد کلید زده است تا گامی مؤثر در جهت حمایت از خانواده‌های پایتخت بردارد.
🔹
این بسته اعتباری که ماهانه بین ۳.۵ تا ۴ میلیون تومان شارژ می‌شود، مستقیماً به حساب شهرزاد مادران تعلق می‌گیرد.
🔹
به گفته مریم اردبیلی، رئیس مرکز زنان شهرداری، این تصمیم با هدف تقویت نقش کلیدی مادر در مدیریت تربیتی و فرهنگی خانواده اتخاذ شده است.
🔹
این تصمیم حمایتی شهرداری همزمان با روز ملی تهران اتخاذ شد و این ویدئو روایتی است از اهدای چشم روشنی به مادران تهرانی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/696585" target="_blank">📅 13:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696584">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383a37abc0.mp4?token=vwThD0nESYClNTYRs2tf5iQrq0MOJA3unRWQkFUTv8kc9k4cueTGCtiYiY6nFNEpnoP-G1Sw7jZFJFgkoAFOVrUNaVLZr0hwDGW0HZyaREyaaqDREZY4R0SHRP9H6tja5KNE_gaMVyp7VcA0ieq6PqzFhKORTGnk6CRCjfyQLmhD43MGxjLBOKfqngegZQSty1t0HuRMR4VMuUDHO94JppTc2HVQSL0ANlWt53rG6A---WTKn8b9zdFd2A4CcBMOWJMuU5RdwIlZkNxVaxvnQHCaHobEZKyVvg8f-Ii1mpqt57X7fX3kj9pRthwj56RlSuvxhF6xQ_g-k-GG-uZrdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383a37abc0.mp4?token=vwThD0nESYClNTYRs2tf5iQrq0MOJA3unRWQkFUTv8kc9k4cueTGCtiYiY6nFNEpnoP-G1Sw7jZFJFgkoAFOVrUNaVLZr0hwDGW0HZyaREyaaqDREZY4R0SHRP9H6tja5KNE_gaMVyp7VcA0ieq6PqzFhKORTGnk6CRCjfyQLmhD43MGxjLBOKfqngegZQSty1t0HuRMR4VMuUDHO94JppTc2HVQSL0ANlWt53rG6A---WTKn8b9zdFd2A4CcBMOWJMuU5RdwIlZkNxVaxvnQHCaHobEZKyVvg8f-Ii1mpqt57X7fX3kj9pRthwj56RlSuvxhF6xQ_g-k-GG-uZrdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزیره قشم، ایران
🇮🇷
#ایران_زیبا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/696584" target="_blank">📅 13:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696583">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f411d34ec.mp4?token=JoFSjXZzZHJi7-R1cRtYzGP-Dc8JjE9nHdsd9pHc9jtvD7lSuxRHAyWuzxDP2fTgCARzoJf5FBMx9BqcgGMtU0e82qhXedUdOsU9IiNGwmp__AJWUJAh8ryRSSPc-1Kmb0nT0DfGTWN6cD-Vl95QBwgDtOYPlHyqXDVG4Kd97B2vRhgWUerzIsi0mUv5Nk756i1Np_Nn7wed6IidVHuzOAzX1AOfts9o2AQuVUcnhX4Zoos7Hzio_hHx4B4OZht8i-vWzZBXf3TB4g5HveuZTsKNXTBU8xMlmadWVYH3ULAwe9v_iH95tjC-wuME4CIxVXUSDSc9-yHSEtmS3dqZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f411d34ec.mp4?token=JoFSjXZzZHJi7-R1cRtYzGP-Dc8JjE9nHdsd9pHc9jtvD7lSuxRHAyWuzxDP2fTgCARzoJf5FBMx9BqcgGMtU0e82qhXedUdOsU9IiNGwmp__AJWUJAh8ryRSSPc-1Kmb0nT0DfGTWN6cD-Vl95QBwgDtOYPlHyqXDVG4Kd97B2vRhgWUerzIsi0mUv5Nk756i1Np_Nn7wed6IidVHuzOAzX1AOfts9o2AQuVUcnhX4Zoos7Hzio_hHx4B4OZht8i-vWzZBXf3TB4g5HveuZTsKNXTBU8xMlmadWVYH3ULAwe9v_iH95tjC-wuME4CIxVXUSDSc9-yHSEtmS3dqZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانم ۶۷ ساله مست پشت فرمان جنون به پا کرد؛ چرخش‌های عجیب مقابل دادگاه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/696583" target="_blank">📅 12:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سی‌ان‌ان: نامه ای از سرپرست اداره نیروی دریایی آمریکا منتشر شده که مطابق با آن، هشت نظامی حاضر در ناو ابراهام لینکلن، از ابتدای جنگ با ایران، اقدام به خودکشی کرده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/696582" target="_blank">📅 12:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06a2cbb3f8.mp4?token=Crk9KG1f57goOtCVUu5FU3e-NnCkYbP_dc6Io3zcyhBrjqL25NqN7iT2lnCRn_OVV1c3e_5qckkDtP06a6zG1NEfVvF3lZIwJuQMsLc5tDcRdwbfnEDqMC5K1qdEP9gZvnErHxzD05lq9z2RDyZdcSxV1qjbQGr2Dk0-2u8P-0HFoXyDgM98nXHw1ZuKfKRBllnpHHwwrDRbfZYpZo6P0y_f8fmhqCWT_pSKW61TU8gU9g87of-F-zTRzIqJ6Qs5gY3d3tyh18_nQl1xVfnfW9_-SENXHRu65M4jfblkMMsySzfRqXF-Q9jlfwNq4Ykv_8sSSXIAtgqNmWG_hBmCZ3GqJlnre0UvwVc_3wyzN9cESYtq-P_J4wDcpEsBkbLO7mKo3wFMc7btKk5n2_IcE0XiG7bhiXkqjh8dHYrtjE86St9gKKSb_wPoKTLZUIX-J6tCUL7vuMKEPC1X3pkQX7x_xyLKhEUJAlnl5Ye7Uhr4y0WUEaGcRn_udgrLix-mLhdArrI09X8afUfX9MYCbsNoEZMe8slrY17N_ILmfzS8F-fAiDm08PhKKMwCnWjaAUBN9_xo6_-z65oZObJqfv-UWShCTUlQsEzTXIW0AnY-WY7y9LYXP9K3bGEgPvlUqmky3Ib0OwHvxycySLyxKt9u40UuXYveL6YOisu1AJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06a2cbb3f8.mp4?token=Crk9KG1f57goOtCVUu5FU3e-NnCkYbP_dc6Io3zcyhBrjqL25NqN7iT2lnCRn_OVV1c3e_5qckkDtP06a6zG1NEfVvF3lZIwJuQMsLc5tDcRdwbfnEDqMC5K1qdEP9gZvnErHxzD05lq9z2RDyZdcSxV1qjbQGr2Dk0-2u8P-0HFoXyDgM98nXHw1ZuKfKRBllnpHHwwrDRbfZYpZo6P0y_f8fmhqCWT_pSKW61TU8gU9g87of-F-zTRzIqJ6Qs5gY3d3tyh18_nQl1xVfnfW9_-SENXHRu65M4jfblkMMsySzfRqXF-Q9jlfwNq4Ykv_8sSSXIAtgqNmWG_hBmCZ3GqJlnre0UvwVc_3wyzN9cESYtq-P_J4wDcpEsBkbLO7mKo3wFMc7btKk5n2_IcE0XiG7bhiXkqjh8dHYrtjE86St9gKKSb_wPoKTLZUIX-J6tCUL7vuMKEPC1X3pkQX7x_xyLKhEUJAlnl5Ye7Uhr4y0WUEaGcRn_udgrLix-mLhdArrI09X8afUfX9MYCbsNoEZMe8slrY17N_ILmfzS8F-fAiDm08PhKKMwCnWjaAUBN9_xo6_-z65oZObJqfv-UWShCTUlQsEzTXIW0AnY-WY7y9LYXP9K3bGEgPvlUqmky3Ib0OwHvxycySLyxKt9u40UuXYveL6YOisu1AJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهزاده ایرانی که بودیسم را به چین برد
!
🔹
«آن شی‌گائو»، شاهزاده اشکانی، در قرن دوم میلادی به چین رفت و با ترجمه و آموزش متون بودایی، نقش مهمی در گسترش این آیین در چین ایفا کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/696581" target="_blank">📅 12:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-z9dmYLkmVvEXpPjaaZCjnuZQsaXKnG7leOAEvxaJzTVlnhRhisOgE7KQx_aeq_ME0cPL20AXBCHHrD58veg5d7Bqo7r6CuE-kTqgqy_Hi7u60Ad1Y3Lkum5nMw2XHHDyeRTEg9kbTMp6Q_n-Fi0CLd78d0s_uha9tGG1F-0ZUXvQgPpaQXDs30OXXoy-VNRkW7FgSJIck3cMKG0XF3ABHRw5eHTcPZOHTbGtJL4uO-re_0gc0xAv65Mtjb5t487IgcTlDGApEXTTS-SHTCKrQDMJNcv_ucdgBSHG2Pv9OC4L2HQ1cXhGJOIQZZz3Vqx_Am7iWkHGxvFFrwjmKTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgpyoFKILlR-37wGQxdMv3NiZZjvCbSf5IPUv0pf5sJH8zBfNDudl7yJKmCUsz_OM9XszJ2J9ievadbHeKXqgrZs8EEpXLnONP7PVeLfdjXQJtFBCi65681wqEfH-GUhii6UrD-eWqyZ_9yyhKKAb5zNrjT0UDwjm5r79ph8Gy2enl0XWNB9Qrw-udtmn_XoHJ5bRG-R2DAEg00YfIfQwDXfxxenmWulMJ4JJYT3_LCpM87s1eVO0ADE0RebLFROgIiZvXljmKIKONiE-kqGPWJRrxPCfjCSfatPRPEdZhlnvr1KxaT1vw42yCP2ZADZvXKEONqAXVdxCEyvfVqRWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwjjbpzTkUHCOiJVtvXmLGlgoMB_Xr883qxXXHmyFCA_DRJXVzLnbACOsBskMJGAUO3Yxgts2HQU8D-g8u8BuHfK6iX_tufUmdMZ1y1gIVX9NIfHc6ThfBKYO_YkK-jHI0-rHLixtOSK8Br2ttJ1NKFPvxJPBlQthj6GxSUH-LeV-a4k6e-snW3lnOFfaMiJ9vvdyh88YG-gtszaXeJVBoU4BsZCjhhnAnUPLgs6qqooWXV2GbZNYvO7T1dP5b_4DAffZ6xZlYOJTbLqgVorTavMB7DRdWNuC3-OMxL89a7rPpt5HbhHbRg82TLuUWrFHEjCokSY-NNfB9Brdm3EVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBWuc8bv1Ggurva2n9zV-7BABZ7z1aHIaaMxoc2Jb-5GF_D3t_8tqUdP7RdxNwmYgnCH_3Cg34Q3PDyt52cG7ZrUko1AEl7v--V8Sh51azHARGlN_iqJ9iWbzMuleM3-yWJMKHl-_PrLlJ5fUFUL27x_KNraFsImGsChr_4saZBTjnietI_HdpR2PKjnvSz1JDWxLf9gTnv3h0l8bq3JGhIgWjQDzUJN-lS4loJr1-aISmE9SFmTECjbyC55JUxoJaQ1LnR874TzY_O0Wb5vdPjXVNEB1B-2DgpwYqcbKVex_99kbAZJCrOySPR6SkMQi6XL5DxBYxFiFhDpkZ3V6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-vJjdpLLLpCQp5nmuMLBLGRK0q9JeUcHhSluM1ShgpbzRcWAYbpbxs6QpQ_c64IcbM7tzXcImRFjLIIQ1rTf8mdL1jBmE8vEqVUScMy5XpNcuFxlvY8Sl5vPSDvju01nMz8-ScWoCAb1VjeAdwlmT-vdqxYU59FRR25R4NbvC_ihRvK4ybF12f_8wtM3aBsFiWNfHzBW7R9WOIDm9sfv7MNEDQmjudI24cEp14rFLcLdVyLShiobzGRW-_M-jWutunajEDu5g7v5DRQzPWKyBeoc6uXIR7cKfxuFfu04CztBL_aBjYCmVm51bSqs5W5sTs4DsFKCU4ulDE57-fOTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵۰ پرامپت وایرال برای ساخت تصویر با Chat GPT
#هوش_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/696575" target="_blank">📅 12:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696573">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
حملهٔ مسلحانه به مینی‌بوس حامل کارکنان نزاجا در زاهدان
روابط‌عمومی لشکر ۸۸ نزاجا:
🔹
ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، مورد حملهٔ مسلحانه قرار گرفت.
🔹
در این درگیری یک نفر به‌نام محمدرضا اوکاتی به‌شهادت رسید و ۳ نفر مجروح شدند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/696573" target="_blank">📅 12:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696572">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amvMZgVkCuk19y_s8my6LhB2OjKZOLlcZJSF3m72gqnIXptE9BmX0jluVdYnede21gzb4IBlrcH1nkKelD0XsPk6l7FWc2eLEry9x2NbCtw-GvJILEVmWAcuBxE8f195efj3s96YUzoh-kWESadOZD9sVbMllnOlDf1m2DFyjxNYF_TwKm3ha4mh74QWUraEWI9V7Zpx1Vf9ErcZTBkxmOUipGAo2T1WXXqpoI62DMGYywdl75uOeGz1cqYXpIlR-feE8lZzRi7oYjlQFAtrUrj-Xom22cPVVRhfspaLqATWRn9D6w7JjUoMoIinpLc_AUIhX_Q-WbQ4ejSlKWadXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا شب‌ها انگیزه برای تغییر زندگی داریم اما صبح، پشیمون می‌شیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/696572" target="_blank">📅 12:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696571">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه : افزایش مجدد حقوق‌ کارمندان و بازنشستگان فعلاً در دستورکار دولت نیست./ مهر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/696571" target="_blank">📅 12:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696570">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-B1wMTCYlqAO4Cc2YjYsgfCP7vZiVNaMUhDMlK4GysOlQL_IXde7AIXO1Vz89M-JJfK75N7MJ47zq8DS_3HaWuVq685MYw8Zdcz3B8dU9wNt0aY25ZnxS4PwGlHT_ZUieJ4c_hK5f-c9_-c_MVI6Kvk87JrmK_FULTfWMrF3pkgx8MTYN5G3URF0_iyfW29LutYw9D-o6MMJJiwt_3YAxx4zMfPHMoDwHg6Y96dpzi8aQgvaPYUxz5CkYCEcUDCS26rF5H28-Qg8wpwDHDF808OC3GNO3N5bKvBJFxwi8R8lEGow2exGZ_-VhavRnskiykN2oKKMnCsxONNc5D1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرانی نجومی خودرو در ۴۰۰ روز؛ در یک سال گذشته خودرو چند درصد گران شده است؟
/ باشگاه‌خبرنگاران‌جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/696570" target="_blank">📅 12:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696569">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ساعتی پیش یک خودروی پلیس در منطقهٔ نصرت‌آباد زاهدان هدف حملهٔ تروریستی قرار گرفت
🔹
در جریان این حمله چند فرد مسلح به‌سمت خودروی پلیس تیراندازی کردند./ فارس  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/696569" target="_blank">📅 11:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696568">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1340b42a.mp4?token=Kd-9g44ggnjzxDHdzDDDMTr6E5jYUaPyIbcGk1XsJNlMLg7ifbIHFBnmuFw7nS2U-jH3pRDXmbnJlYS0xOFtkYDlnwv_1A35o2EiecTlpYOI-s1BZp-tpomHWooOqvI07B_-_PP4F4OrPzabKDXcSwlgU-TH3nne3OtG54Q4Nv8IWv8XwN4sKBbB12x4GjYwnsqILZAHZiLhKAG6yf78T_QYKBr0ZpAEb0TuPAW0MRcWvNTD4y9tix89rdch8SdBoK4bQU4Wo6XVYymJZKZ77ITKgc-uJmvf0_E8CJTfrZ3G3eGZTanC0iAhpMJtRVhm_d6AYur5kzC6JnxqGFtaDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1340b42a.mp4?token=Kd-9g44ggnjzxDHdzDDDMTr6E5jYUaPyIbcGk1XsJNlMLg7ifbIHFBnmuFw7nS2U-jH3pRDXmbnJlYS0xOFtkYDlnwv_1A35o2EiecTlpYOI-s1BZp-tpomHWooOqvI07B_-_PP4F4OrPzabKDXcSwlgU-TH3nne3OtG54Q4Nv8IWv8XwN4sKBbB12x4GjYwnsqILZAHZiLhKAG6yf78T_QYKBr0ZpAEb0TuPAW0MRcWvNTD4y9tix89rdch8SdBoK4bQU4Wo6XVYymJZKZ77ITKgc-uJmvf0_E8CJTfrZ3G3eGZTanC0iAhpMJtRVhm_d6AYur5kzC6JnxqGFtaDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهنمای‌کامل‌برنامه‌های ماشین‌لباسشویی
که هر خانه‌داری باید بلد باشه
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/696568" target="_blank">📅 11:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696567">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سخنگوی قوه قضائیه با اشاره به رأی پرونده‌ کلثوم اکبری: ۱۰ خانواده‌ درخواست‌ قصاص کردند؛ به ۱۰ بار قصاص محکوم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/696567" target="_blank">📅 11:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696565">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
بازگشت افسانه آمریکایی؛ دوج چارجر کلاسیک پس از سال‌ها خاک‌خوردن دوباره غرش کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/696565" target="_blank">📅 11:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696564">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df45dd269.mp4?token=uN0qmL7-_uiYVvKsypoMcuH-oJNkuNeehkEuGRkF4quVTQPB-sOD2-0Z_i96kjM9K14NjIfIuah81Qyp3A0KPlQiJ8IOxPnNPcZAZaPfYDwUfZTsEs4Btvd11nWNrdGsWF67ga_T-Uzgx7dyAoZOcP5wGiTvs1jKY5iqH3VNNw4-PgC_50-lvfvkwUOCr-6mZNyYBKkvCfVeBBLfxappV77tW4ShDsrmwmVJcZ8f-x7t_WBiw9pUrZuF1DrsSEAORYpb85McYbklYe6gG1IRp87KxTLYSCgh_J9C9wih-sPKSEHQPdFu7Q9Enw8H8UI3CllpXCd0IKkrUBSADvbKig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df45dd269.mp4?token=uN0qmL7-_uiYVvKsypoMcuH-oJNkuNeehkEuGRkF4quVTQPB-sOD2-0Z_i96kjM9K14NjIfIuah81Qyp3A0KPlQiJ8IOxPnNPcZAZaPfYDwUfZTsEs4Btvd11nWNrdGsWF67ga_T-Uzgx7dyAoZOcP5wGiTvs1jKY5iqH3VNNw4-PgC_50-lvfvkwUOCr-6mZNyYBKkvCfVeBBLfxappV77tW4ShDsrmwmVJcZ8f-x7t_WBiw9pUrZuF1DrsSEAORYpb85McYbklYe6gG1IRp87KxTLYSCgh_J9C9wih-sPKSEHQPdFu7Q9Enw8H8UI3CllpXCd0IKkrUBSADvbKig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت: امام جمعه کرمان چه چیزی از مذاکره می‌فهمد که در این خصوص اظهار نظر می‌کند؟
🔹
کسانی‌که در میادین می‌گویند مذاکره نداریم بیخود می‌کنند چنین حرفی می‌زنند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/696564" target="_blank">📅 11:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696563">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNFGPLU6cOPO_3ku2rJCCGLfYAkjXtelHNgNw9OmBD1CT_CTmPu2rYWSWZElV199SI2OdW3cnX5IIhyT-LBtNjbG2Q12CjIV6sGCv_m4cpjzThBI698n1ohiv6F2hZYVmK0duwt6D9qQ_f7WlXrNUopZyL6n7SO5HshdxBheas3MD4aAIU-8iUtvg8xIWXvZgpylq8e05E2I5gVz7G1oKyYt16HZVgRwUHgr1P44fUEW55UnZ1DesBHTGMu9nuLTC3ZMGMupifbHzPYyCX4xnMnJBU6L9WN-BjBnDJGbkP0l7x-Q0kbhuR6rDierGSHAzNc-F5qPiH2Ux0FvPS7OWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کرگدن ۲۰ هزار ساله در سیبری؛ کشف باورنکردنی از عصر یخبندان!
🦏
🔹
در یاکوتیای سیبری لاشهٔ کرگدن عصر یخبندان پیدا شد که شگفت‌انگیز سالم مانده، این کرگدن جوان فقط ۳ تا ۴ سال داشت و ۲۰ تا ۵۰ هزار سال پیش مرد. نکتهٔ عجیب، سالم‌ماندن بدنش است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/696563" target="_blank">📅 11:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CpQSDRyy0TzfTi3ey0GSUbEmyp4zYFZwnXTKMO0vhprgocVljqLoaCuvD0OnV3i5IdWo8KEFJq5Hsrz_iPzV18vwPBHkT4al0BG6i9Hlll0H9Ts9M4HXv3e7sfk1nsGqVm2ka8XrsKMK7JNQNt__xEpZg8WqRME7N8UO15hbGNFWa-4J82lslMAvZMTpBfH9ramn34GpTI1QWqc1aepKUhSd7CpEQF6ueDlYwGSgshStd0-pUGlYUPfwwaEcaR-fD-5OqSDWppd3oSoVEu0p01ewIf6wiEHUeGIMZDpCcz3YK18jA2vJy8KY5XkCGiktv20KXVeQmFG5986KFycefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای کامل کدهای تلفن همراه
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/696561" target="_blank">📅 11:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ساعتی پیش یک خودروی پلیس در منطقهٔ نصرت‌آباد زاهدان هدف حملهٔ تروریستی قرار گرفت
🔹
در جریان این حمله چند فرد مسلح به‌سمت خودروی پلیس تیراندازی کردند./ فارس
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/696560" target="_blank">📅 11:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAmyLbsWRI3DnI33GeSPBzxWM__f9E-9TYqnoC5CJ_GLycRbjjUMz0Hbjqik62PuEJh57OUdVyx2_f5dHPt094OrrpS_cJI_SJIZ44wnbx9-29QeoNjUgxKCr5C3G75s_0cY3lvcQV_qvCk38xiRMICiAxooIWFIAXEF4483nWM1Vbh2va6QnTFYal9bIDHpT-rqOcCtsTYRxQy_ZgdDsxwWUbZX6Sp4YMxJtcJLObz_mu7ZDxzkKE_5LcxFbYOWb_zVr-27uYZEOZCJ1jsmJ5iTWAAWP24sqL5MRshPNhv1uVKAFcudcYK1__AGxqMERtE554Bj21DY1GudCKxdsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل شاتل موبایل: ۹ سال عقب‌ماندگی تعرفه‌ای در صنعت ارتباطات داریم/ طولانی شدن سرکوب تعرفه‌ها، صنعت تلکام را به یک وضعیت قفل‌شده رسانده
🔹
آرش کریم‌بیگی، مدیرعامل شاتل موبایل می‌گوید تعرفه دیتای موبایل در ۹ سال گذشته تنها سه بار تغییر کرده؛ یک بار ۳۴ درصد و در سال گذشته نیز ۲۰ درصد در آذرماه و ۱۸ درصد در اسفندماه.
🔹
این میزان افزایش با رشد تورم، هزینه تجهیزات و نوسانات ارزی و همچنین هزینه تمام‌شده ارائه خدمات همخوانی ندارد و تشدید تحریم‌ها نیز فشار بیشتری به هزینه‌های اپراتورها وارد کرده است.
🔹
کریم‌بیگی با تشبیه وضعیت تعرفه‌های ارتباطی به «ماجرای بنزین» معتقد است طولانی شدن سرکوب تعرفه‌ها، صنعت تلکام را به یک وضعیت قفل‌شده رسانده و اصلاح تعرفه‌ها باید با در نظر گرفتن شرایط اقتصادی و به‌صورت تدریجی انجام شود./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/696559" target="_blank">📅 11:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696557">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
یکی از عجیب‌ترین اتوبان‌های دنیا؛ تقاطعی ۵ طبقه در چین!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/696557" target="_blank">📅 10:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696554">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e09d3f41e.mp4?token=izmUU3q-NpH_FTFFFrhMnOaOt8ob976GgsbrmOVXIyBEkDK9GPh_AG7FwIQIHqqz1JTgh3oPCo41l-9n9dbc1ofTNoI8z6zE8VmpJDj0uITPju-ucuUZeX5XLyUOKsLXDtSpfl_4zDV4KYSskJB6hyCKdhEQmfM1lSCKMz510SgkCwGdYAQYeHxdMTzcctJ8yOOVVa5Z48OJ7v7XNUIv1N4WJoxlvyvD0PfXIXXJmabd6rN1vnL45ahOeK090VlIuyx59zStPrG7gyyVddE1j-ABA2N_cEgtXt5gyiQ_Urd4yUPurrN6xSH2YamvS6wUoMgV_7sG7FhbQKpyiGdiOHKURIIlBt_2bQsP8bGQeBTd48Q2i6lfMTkOLnC2jRZWPBqI_f2RZxsUJen8DrBplLoafuq0SYf4DlGbW38Qpgb-ZjRPoiAbgAnKnlUaqMjXAKGfzgv7-VDRBpVWYH7oZfGI_vRrlKPNnEJQfNuHPgGdgwM26mTCTOCgKEb6f7UR_ZsZny5hzrLQtwpTkdJMgr-50Cfh7Zy703wpKwPf6N1_9Zn5uT-rmRceE40kZdUNjpj0KBVT_QRWCBxRtHCCSifkMI6c89iik7SIxlNRAbFtFq4_RJJRE5R0iunF-C5g2_NOnGL2cW5mxn03YqT-yiRpMYCxIt_ojsiBfAzfTgU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e09d3f41e.mp4?token=izmUU3q-NpH_FTFFFrhMnOaOt8ob976GgsbrmOVXIyBEkDK9GPh_AG7FwIQIHqqz1JTgh3oPCo41l-9n9dbc1ofTNoI8z6zE8VmpJDj0uITPju-ucuUZeX5XLyUOKsLXDtSpfl_4zDV4KYSskJB6hyCKdhEQmfM1lSCKMz510SgkCwGdYAQYeHxdMTzcctJ8yOOVVa5Z48OJ7v7XNUIv1N4WJoxlvyvD0PfXIXXJmabd6rN1vnL45ahOeK090VlIuyx59zStPrG7gyyVddE1j-ABA2N_cEgtXt5gyiQ_Urd4yUPurrN6xSH2YamvS6wUoMgV_7sG7FhbQKpyiGdiOHKURIIlBt_2bQsP8bGQeBTd48Q2i6lfMTkOLnC2jRZWPBqI_f2RZxsUJen8DrBplLoafuq0SYf4DlGbW38Qpgb-ZjRPoiAbgAnKnlUaqMjXAKGfzgv7-VDRBpVWYH7oZfGI_vRrlKPNnEJQfNuHPgGdgwM26mTCTOCgKEb6f7UR_ZsZny5hzrLQtwpTkdJMgr-50Cfh7Zy703wpKwPf6N1_9Zn5uT-rmRceE40kZdUNjpj0KBVT_QRWCBxRtHCCSifkMI6c89iik7SIxlNRAbFtFq4_RJJRE5R0iunF-C5g2_NOnGL2cW5mxn03YqT-yiRpMYCxIt_ojsiBfAzfTgU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با بچه‌ها درباره شوخی‌های خطرناک در مدرسه صحبت کنید/ ممکن است جان بچه‌ها را بگیرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/696554" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696552">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAvCiD6AL8LrGhaKZqCnaucdgqiVI_kjiLrKV8KSnaHl8e_dE4tLIwHEVxbzLDGaM8FAReYg6a_UNUFW5QgNqXMZtxFYQ7o9MGsfuZbQ7Avsu9GKYi1sx8sBZvYoZwDUvJTFATQ_hrHDaaeDUVy_QXm0SYi_si354F0aAhqWQoUq1sewZ3F2gTRy3NMVGltJpwz9hFVI4CP-wUKBPO-wQeNbqKHB28hbWhClPAX3Q6-zk_IK3Uo0MSmTK6fzK8bOnZFfFfABdj1sld1ePmScshxbcWI2ypTOhZ6elYAkKR0WIQMDKLoYaqI4wSpuIdWIqIMz8Y2BtgNgIIvasMQ6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محل تجمع نفتکش‌ها در نزدیکی امارات منفجر شد
🔹
آتش‌سوزی در خلیج عمان، ۳۰ مایل شرق فجیره، ۱۴ کشتی در ۷ روز در تنگه هرمز هدف حمله قرار گرفتند.
🔹
قیمت نفت هم‌اکنون در مرز ۱۰۲ دلار است و تحلیل‌گران می‌گویند با تداوم این شرایط، نرخ نفت به‌زودی از ۱۱۰ دلار عبور خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/696552" target="_blank">📅 10:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696551">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سه قلوهایی که رتبه برتر کنکور شدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/696551" target="_blank">📅 10:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696550">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nttMkZ2cCbfqD5Y67OL4m598WnY-gaWGO00HXH-DoeziIOkJE47EQ5SpOhXvEjLqbsSHy6W-4VljXXYw1Ivl3cZfYZH48gDFmBxtbOFE1P3GWlFvJMVtmNTstMCx1ivY4kxpgX4NUYf_4GQ2L8qTvEyYZIMmYfoRFekpKxQU3loNDo4H5n17Wyi5Xs1i8ld1mW6gvUY_x_qigSa-_7Stm7v2DoyUd14Gllmd1ZJAG4-kQZoj-dknUBpr4Z1KChjvdX84kAvzQnRSFMVdYMQx26n052A7JtvIrdxNuPD6tojxdp0OSnS754H1zDEjcCjnUFQ8o3IIzkb5I4pqzy5Lzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: قیمت نفت به سطوح پیش از جنگ بازگشته است!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/696550" target="_blank">📅 10:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696549">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93242736a.mp4?token=JW2w-G7lSOPf6IyVDgCwODk_q1--JCvVz3HiUj_Rbd1RcQvfxYpMYYH25UOkHEmy94lNEbtw6iVhfJYxojGTw5qauX99CpGtbVQqwIJS1m59zeYaMlje6OhQwI00rAyLUhUp4mRgxebQ7vgH6ADnit0xEnXlT6fziA7sgK4tlzDyvQIJM1Yfn_rSUhE52RhJKoA91eO5-AijYPj9RQeSogaROE7oVvl2BgVnoQKhy-GP8B0A5Ktk65SwiVpeM-nrtxazbZ48S2rTEPGse13S1EnXwgw1XjVyKv-09Wsq1_23fHTIHEd7IdqoUgD6Dtkuz89bEKJmnJhB6FIEfJ10LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93242736a.mp4?token=JW2w-G7lSOPf6IyVDgCwODk_q1--JCvVz3HiUj_Rbd1RcQvfxYpMYYH25UOkHEmy94lNEbtw6iVhfJYxojGTw5qauX99CpGtbVQqwIJS1m59zeYaMlje6OhQwI00rAyLUhUp4mRgxebQ7vgH6ADnit0xEnXlT6fziA7sgK4tlzDyvQIJM1Yfn_rSUhE52RhJKoA91eO5-AijYPj9RQeSogaROE7oVvl2BgVnoQKhy-GP8B0A5Ktk65SwiVpeM-nrtxazbZ48S2rTEPGse13S1EnXwgw1XjVyKv-09Wsq1_23fHTIHEd7IdqoUgD6Dtkuz89bEKJmnJhB6FIEfJ10LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش هیجان انگیز و تماشایی آتش‌بازی سرد در کوه مینگشان در چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/696549" target="_blank">📅 10:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696546">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGoldiran | گلدیران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358f4d9375.mp4?token=MQ-12B1OhHOBxZrN4zSW5Vu6qvpdq98oZyUWjJZDfYuD1DBegQz9xOVXhn-x53nzrBoLkJ6coINQ7KEtBYNmYGzu8U2E950sW7Vj2rLTacn7OjuMl2R-ujFyQnvh2Yi_I0pSUWiTI62bVlg8pmoDI4DdOeOKBFftxuY3dskhBCJZ1Qz4jASxVVuiZYZjmb2Zk2i3USrAyI8OxLDyitwKO5Pc9lmWXdZTLwmaFEP2aIzFV5-ODbXW_kUV-xpgKwDnazjP4BP6O7lsGm69PbqaA9O6quVyJqT29WCssTyYAh-GtTuqJuiy2R-cGfmPoytArbGo9LUOGg-y_KVl7Ej_wX3mgr_zX1xHN2xHwnrRoxSvh83cC7T_HztCIcZ9dzK_SqnTr-yCngPcp7hMOXeS3bwQllS4qxmxlQJRR3efSssoKv2MRf08lzjNCo3jmad0Gbt7XV5eM2BL_JGXucXyPA74Ycip1ioZeWy_sRuJTrUfhRm6CbK_hvY6-nITqulC7ZeQFcX4TmOWwiCAF4V-oyrWcpaV77THxSBhscP8ZMwzzcqK6WG9Kprkm1rzHZHwr3YtPnmc2wDa8t2bOCx9-VBKuyLj_uVJnDONLNzAT94ULoqiEND9vHdj9On9RLsyJRgy4hcfUZKBkLFQWyxDpAEwsqQwDZEEiPECMDKJsaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358f4d9375.mp4?token=MQ-12B1OhHOBxZrN4zSW5Vu6qvpdq98oZyUWjJZDfYuD1DBegQz9xOVXhn-x53nzrBoLkJ6coINQ7KEtBYNmYGzu8U2E950sW7Vj2rLTacn7OjuMl2R-ujFyQnvh2Yi_I0pSUWiTI62bVlg8pmoDI4DdOeOKBFftxuY3dskhBCJZ1Qz4jASxVVuiZYZjmb2Zk2i3USrAyI8OxLDyitwKO5Pc9lmWXdZTLwmaFEP2aIzFV5-ODbXW_kUV-xpgKwDnazjP4BP6O7lsGm69PbqaA9O6quVyJqT29WCssTyYAh-GtTuqJuiy2R-cGfmPoytArbGo9LUOGg-y_KVl7Ej_wX3mgr_zX1xHN2xHwnrRoxSvh83cC7T_HztCIcZ9dzK_SqnTr-yCngPcp7hMOXeS3bwQllS4qxmxlQJRR3efSssoKv2MRf08lzjNCo3jmad0Gbt7XV5eM2BL_JGXucXyPA74Ycip1ioZeWy_sRuJTrUfhRm6CbK_hvY6-nITqulC7ZeQFcX4TmOWwiCAF4V-oyrWcpaV77THxSBhscP8ZMwzzcqK6WG9Kprkm1rzHZHwr3YtPnmc2wDa8t2bOCx9-VBKuyLj_uVJnDONLNzAT94ULoqiEND9vHdj9On9RLsyJRgy4hcfUZKBkLFQWyxDpAEwsqQwDZEEiPECMDKJsaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
این جارو جمعش می‌کند!
💥
جاروبرقی جدید جی‌پلاس مدل Hunter با موتور 2400 وات به بازار عرضه شد.
جاروبرقی هانتر با تمرکز بر قدرت مکش، عملکرد دقیق و استفاده آسان طراحی شده تا گردوغبار و آلودگی‌های روزمره را حتی از نقاطی که کمتر دیده می شوند جمع آوری کند.
🔥
برخی از ویژگی‌های هانتر:
⚡️
موتور قدرتمند با توان حداکثر 2400 وات
⚡️
مصرف انرژی A
⚡️
فیلتر تصفیه هوای 5 لایه هپا ( Hepa Filter )
⚡️
گنجایش مخزن 6 لیتر
⚡️
شعاع عملکرد 9 متری برای پوشش ‌‌‌‌‌دهی گسترده
⚡️
لوله خرطومی کنفی مقاوم و منعطف
⚡️
لوله تلسکوپی با طراحی ارگونومیک
⚡️
نشانگر هوشمند وضعیت کیسه
⚡️
سیستم محافظ حرارتی ایمن
⚡️
24 ماه گارانتی گلدیران
🔗
برای مشاهده جزئیات و خرید محصول، به فروشگاه‌های گلدیران پلاس در سراسر کشور یا سایت فروش اینترنتی مراجعه فرمایید:
🌐
Goldiranplus.ir
گلدیران؛ روی خوش زندگی</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/696546" target="_blank">📅 10:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696545">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
اسکات ریتر، افسر سابق آمریکا: ایرانی‌ها و انصارالله با تسلیحات کمتر و ساده‌تر می‌توانند آمریکا را شکست دهند، اما آمریکا تصور می‌کند هرچه بیشتر هزینه کند، بهتر است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/696545" target="_blank">📅 09:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696543">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d9bf4e68.mp4?token=EwYFuYWAtvF42JSrmDhv4kxNWliidQFgwcWBcaGBwuizTJU_8spgGdfbyfhYVGahlyvzfKq47Cu5zNTR95Sc9HgDWdilQ4rMksj_T1Rsv0YIcNCiQL1bn6hAkENJklMMEnANdTkpqHtnme6L2_rApj-kM4rK7axrIv91bTuX03zs6AgT9KJBebEhs2kzCcx_AAOTkbjeopzvSmoZkzm3GKz6Kh2qTs1BYCWm5C5oc4vGHrgYFLamwdwXFBosVQD9hsfR_31c3ae1l4G667m5nYxvkcELnP5JqhE1iF7FotZAod5mM_DcVXra8JxB8lvB7aQbQewe4IhChWBBwtYqfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d9bf4e68.mp4?token=EwYFuYWAtvF42JSrmDhv4kxNWliidQFgwcWBcaGBwuizTJU_8spgGdfbyfhYVGahlyvzfKq47Cu5zNTR95Sc9HgDWdilQ4rMksj_T1Rsv0YIcNCiQL1bn6hAkENJklMMEnANdTkpqHtnme6L2_rApj-kM4rK7axrIv91bTuX03zs6AgT9KJBebEhs2kzCcx_AAOTkbjeopzvSmoZkzm3GKz6Kh2qTs1BYCWm5C5oc4vGHrgYFLamwdwXFBosVQD9hsfR_31c3ae1l4G667m5nYxvkcELnP5JqhE1iF7FotZAod5mM_DcVXra8JxB8lvB7aQbQewe4IhChWBBwtYqfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوش مصنوعی با ضریب هوشی ۱۵۵؛ فقط چند قدم تا سطح اینشتین؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/696543" target="_blank">📅 09:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696542">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqJ49cra4xXenz-ECrEzBDIIbg4EQObl-_t91Cgrt1stO57TEHhyA9IKUN3np7mYsBdsKDPKsZ4ZGwRWYuEn-w05FrU-wLSETc2nAI6-vMCK7amYigzsTMsfCAO28zhKBFvf_5A2ivHxQO-QyW1SWgwoVRzVAjw-Cw6Qj4S7DvX-66jKRehISytS6t2c8bHMMGtsasmpo_sr_pXpFnlWYi7VGYnLXupzQwWo0JgB1gDjLHr10PUtqaJqqSkCEZOZiUZlTSXbi6WxfzFdytzIhIvLwx_4AXKcPbmdSTe5m5N-Gsiw3_kuBVT-oDoBPtfscKf83a1YtlQ6Z3PzkZfr7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صاعقه‌ای ک به دماغه هواپیمای هندی برخورد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/696542" target="_blank">📅 09:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696541">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/696541" target="_blank">📅 09:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696540">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcTJ6Z07-qA9FrSZbg8XjEiwuGcmKGJQzeS9-cveVuv0gPKgVJI7jY7g0sbXQ6_E5QaJ7jSETo4kaeWlahhgogIGsspxk3gvuSwvR9nLiSpt3w56T9hLo2E0rNkq8mmMBYeb1JTiDpTfi2zsZYfz5IPoRG3z3n4P6VoPXc5c1GieUL10glTBnaIdwxmS7bxU8tSCwQiu_oc4jQ9OnE_m7GPHzqzgMw2trGP-oF0NCIbiLkNqvFGMIyrL5UF0UahByGS_R_iKeYQ99xbjd2MegBr2Tk04oDHkDGJ8Khk5LyWu_35CVJneqguOb_yYwg9b7iHJBXBbtWK0tptcSoEJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر خارجه کشورمان به پنهان کاری سنتکام از خسارات وارد آمده به ارتش امریکا؛ نمی‌توانید مردم را برای همیشه فریب دهید
🔹
در ماه می، سرویس پژوهشی کنگره آمریکا اذعان کرد که نیروهای مسلح ایران ۴۲ فروند از هواپیماهای نظامی آمریکا را از چرخه خارج کرده‌اند. اکنون این رقم به ۸۱ فروند رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/696540" target="_blank">📅 09:33 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
