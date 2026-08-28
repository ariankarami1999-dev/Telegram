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
<img src="https://cdn4.telesco.pe/file/e19dkDtGMIMw7LG-ecBJi9Mb8KgmXUPVORAD5qLHQMF4YFbYjxDrC8RDTGxCyDuvfR05ja8K8GIZd7sReDvSLZH0EQCdgayvHUc8a0tmDxhpQpEOYmnrdaWGQehlxJ7eqEwdpwDpzilrlKl2bc2Iu-8xCWnUTyOSVr8YoXlcesB_oeeDOSmTl20l5SvIHZWpp_wSFFOFbS_PmRzAkv4iOTb-YRTCopBTSErPoWqKPN0W2lrHqW-9TrDIjYsdjOzN8EsVgJNkbzOsaLOQjXQCP2t4ozjHe7VzSOsf3_SRBpNjm4pBIasVk_tt0B8r1TbU3fbLsMcdiMLvH6G9dWm-Cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-20273">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به حومه دمشق</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/SBoxxx/20273" target="_blank">📅 00:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20272">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یورش پلیس آمریکا به خانه پسر ایلهان عمر  ️روزنامه دیلی میل که این خبر را پوشش داده، نوشت که پلیس شهر مینیاپولیس واقع در ایالت مینه‌سوتا به «آلفا نیوز» گفته که سه‌شنبه حکم تفتیش خانه عدنان، پسر ایلهان عمر، اجرا شده و در جریان این بازرسی، اسلحه و مهمات از خانه…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SBoxxx/20272" target="_blank">📅 00:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بد نیست بدانید ایلهان عمر یک نکبت اخوانی است که اساساً به صورت نیمه غیرقانونی در آمریکا شهروندی گرفته و اساساً زادگاهش سومالی است؛ یعنی کشوری که دقیق ترین تعریف «دولت فرومانده» Failed State را دارد.  عًمَر همچنین یکی از سگ های وفادار به اردوغان است.</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SBoxxx/20270" target="_blank">📅 00:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
اگر محاصره ادامه پیدا کند، صد درصد ما منافع اقتصادی آمریکا در منطقه را با موشک هدف قرار خواهیم داد.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/20269" target="_blank">📅 23:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/20268" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20267">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پزشکیان
:
اگر وحدت و انسجام در کشور نبود، قطعاً ما خیلی جلوتر از این از هم پاشیده بودیم</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/20267" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20266">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiP8iu1nqaoGgrYlB1Z40qeV2zbqTKSZgLIumPX_8R9Fy95l1e27FvkPAkEb7hgzW4m3y-J_dMjb3smKSjmJSmLFIi9setQLetTpDLXHOwrdhaOO-PUs3Fj0y5c5r-STuI7BHQh42ZsgLXl6tzEjNCgF-TgusYE8_9M04DSCea4tuLHdopBHH3apPjBhRxQYZpwXVuoOmBEPa--H26TEP4-8mfv2J2Ag6l5qywTI5ssk1viF8yW8OLXxO-WDYovDP0QvtzOacDjas3HUa3sHvk0c-DRFTyNhnX8zrtuL9W_LdIuuq1VS5sXSAYfc8RC4itLbiTd1TJ8kxGVc4bOw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازگشت به تفاهمنامه مخالفت کرد!  کاخ سفید، درخواست بازگشت به مفاد یادداشت تفاهم ژوئن با ایران را  با مخالفت ترامپ رد کرده است، که این امر تلاش‌های دیپلماتیک این هفته برای از سرگیری مذاکرات را پیچیده‌تر کرده است.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/20266" target="_blank">📅 22:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20265">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ:   کاری که ما در مورد ایران انجام می‌دهیم به این معنی نیست که جنبه نظامی را کنار گذاشته‌ایم   نمی‌خواهیم با ایران صحبت کنیم و به دنبال ملاقات با آنها نیستیم!</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/20265" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20264">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ:   احتمالاً بانک‌های چینی به فهرست تحریم‌هایی که علیه ایران اعمال شده، اضافه خواهند شد.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/20264" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20263">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/20263" target="_blank">📅 21:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20262">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/20262" target="_blank">📅 20:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/20261" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-bomYi-mNuENcMu030xr98mOCF2FbwnEJ6RNp4fLWnsq8oWDSqQtZtY61E3wR6bthPM-wDiUVY0bWSKVjK5o3c0rc8KrCRl08FqTKnW7clR94fDKxtJlWZjUZyGvUUn1xtd-VxO2tWhVEJaxqYwkKSp-qYDLN2ezyDTNvUANLy683Cb0vhFirNYMI4qiwsDSQU5IfYFZ8xEh1Rzieq6jjKl-NhKPJNm7Y044jR7z5rBCXImsJPJ4Ds_UgJyHUh7B8jVIgGFSUO2u22zkUjsVLceh0M65vkeVMc3TisKSmklil-6_crmgko7Qq6WXfQ-gVQ4nwyZi_Z5WQOb2_qQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/20260" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!  از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/20259" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/20258" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/20257" target="_blank">📅 19:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک دور از 4570 حدود ۳۰۰ پیپ داد  دور‌ بعدی احتمالا محدوده ها را ببیند</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/20256" target="_blank">📅 18:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">محدوده های خوب خرید طلا برای امروز  شاید به این محدوده ها نرسد لذا توصیه می شود به صورت پله ای زیر 4580 خرید بشود و در خود سطوح افزایش حجم داشته باشیم.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/20255" target="_blank">📅 17:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/20254" target="_blank">📅 16:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سخنگوی کاخ سفید:
در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/20253" target="_blank">📅 16:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دقیقاً 20 روز از این داستان نمی گذرد و بحث حمله نظامی روسیه به انگلیس دارد قوت می گیرد!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/20252" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انگار یک دستمال سفید را دور اسکاچ سیمی بپیچید!</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/20251" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.  این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20250" target="_blank">📅 13:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxmDSAXGB5KdVBuNIrkwDjO5lJJzMpE73lkp_xzBEwzpRr-71DCUYK5syLIw_sb8DGYYdnRD14NVQ8Sy-Tb9H2-xywM2waTSKxckPV5MWI3bfIEV5EYLYEZeouLAeeBmJZxWSGpreURt3wVKiyqp6RjuVPkN1JmD906MSKhFkKH3gPCRe7Jz2zExvqq44HR5BSDu4WkI8zopwvx3pPHjoss-PALMYFrCUVtPpK3Q1qSrm-tU1rL1ueQcSzpKQkyv5mpzmclor_11J7AuobqJnCGcbMnP9UkO5MQ1YzmwGixBpUGlra8xxIV12BsgwxpZaoj4tCECN-LUjGMLM_trJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.
این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری می‌شود.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/20249" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kcna2gyXYyYfZa62N1vbyGe4xOvT4tTuM9vqKG-PCh2FP3cBD1ee1gvDPUX-Ba9UDCA9r8kFgtS4lHnbUDHYb6f8BfNsgLIqr72uqjO5Sc5sXbbXFfxzpFhTGSRPe4B6Q-Svdy8P40yJ3BjXGSmJQm0MiDOWatn1ho0TAgn3LkWNkEtSy5WIqCUgrxVnM-wB2mgm5f2JJoQrA6OHR48KFZ5kpwDzvltzxKbDeVrzB_c8dWCw9l9RXuKcZUIq-ciZrqk--nPpH1VpDnylff4KaTpYP1Mwb4yQwpg7i0-5jHbOglGtGwrU_aIiDpEMd7l2nSf8cvbD37C4fw9f--HhIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.  خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/20248" target="_blank">📅 13:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpioVgFO5pXBan7T81VfUgSxkEeLPvtagR-S0rl2CmFH4F52Xgz137QrgWUveK-1YhBuqd3Poz7PoyThvSqjN4FmwPm_0X10JL94COfyLYDxvVhC6JVNSzGYIW7nBymj4zI5HwNTzVyGfiamPcQ24_U0RVBMRA7C-fb2IladVjRRjU2q_d4K0uB6jS2aA8BjYUhXnUJqonKA5-4AdBaC8CV0_MYlXQJuG00Kokg4RKterpn2DIqDiEmf3SEIRmSVg0rnQXtSPTrzv152UvsbikS4vhz-d5dlhb6vvwsqvj4UgedOwaxoSiJt2lVYx1ot-7sWPsEZ6p8h9k6EeMNOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.
خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20247" target="_blank">📅 11:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwxgUMN1s_dHm0L86mFqIE94G7VZnkCdIrIU0aJvI87_etXT9uRY6gfmr3f0gJBVPKbXarJ9OShGwzrddrgq97S-JfZNR9M36htmj71kEPWv23rZ4bvCTKOgBcxBgXthvMVrbHaZ3_kMJr4Vse6a74tFllc_8q0ULmyKq8N0dMTN2HTCzvBeeyiASf-GtefXa7O4Ues-N0wrGHiZ2DB-XP9bKmlUn-ucyOhO59lDT-M0YWdqAy7CsyT9fx0-0cKuZwepJK2lStBeIgV9rw5lx4EBkRLSbZduxWz8HS7NE9TLKoWMAub82jI2ne-xWxGFtrotKdXTm5kjpo2hj5YDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aVb60OZpx5SWMZZqSSYMIiDBUEVbkAFBahiTV0dDU8KcvwePCQftTLheLDB1IK9YiJgVouPVCcZOuOMG71z6Iag9PtCldxAF7F3wC9J-KeYHcHxsm_jCnhft-QqU-Sm6iRfcqTFMgmVJnKwEIfen4h0HqgIvZfkZSKiUx9TgCLqd87_A2NWpW8881gfrMN5ZUYByOcA5v-jjv0cKUqh4huBs3nDxP4YEygEC1us7mfESWGSSfvbhUKuU_KfLYw44G2tDIWkrgfGJ89_HuI3pXvjXmIcK7AID0W6NR520xRUACWz-2JZxjqlgOcfDJk4nwIxxuDCe399I8dlk2lgzBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/20245" target="_blank">📅 11:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=BU-4h7RukTcehEIF1lVZu1vnabjSrEYXqYYUyb-7Zp7scorZfWPCJCjFE2jvJfYwkgvY7-7ANxq-5hDvsIuWbaw_wlXWHLI8CQ9AJqgkUqnplF2F7Z9cgNosqhHwOA0ncKxZHM-yuDIFcMUGCHEGwswfu3I33NFvbP0p_scloudla-9yxNO4V_QCOsR3IQrDJNuJGQn1RIcVJH0sCsm7D7KjaabTuJlCUFK0NzpSyjxpNZ0GGk65AFrDiFr4pM9-o_J64ZiYaGvJoVq41pvUgqhfS-HKpKw6juhiPBn9arz8fjJR6eKS1nE-ngiXj6k7c2BX3RlvA1slip91Ux022Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=BU-4h7RukTcehEIF1lVZu1vnabjSrEYXqYYUyb-7Zp7scorZfWPCJCjFE2jvJfYwkgvY7-7ANxq-5hDvsIuWbaw_wlXWHLI8CQ9AJqgkUqnplF2F7Z9cgNosqhHwOA0ncKxZHM-yuDIFcMUGCHEGwswfu3I33NFvbP0p_scloudla-9yxNO4V_QCOsR3IQrDJNuJGQn1RIcVJH0sCsm7D7KjaabTuJlCUFK0NzpSyjxpNZ0GGk65AFrDiFr4pM9-o_J64ZiYaGvJoVq41pvUgqhfS-HKpKw6juhiPBn9arz8fjJR6eKS1nE-ngiXj6k7c2BX3RlvA1slip91Ux022Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیخود نیست صنعا را پاریس خواهرمیانه می نامند!
ناموسا این ویدیو را ببینید! پلیس های ریقوی یمنی دارند مردمی را که هر کدامشان یک کلاشنیکوف بر دوش دارند «بازرسی» می‌کنند!
به خود تفنگ شان هم‌ کاری ندارند و اصلا مشخص نیست هدف بازرسی چیست؟!
شاید فقط دنبال بمب می‌گردند چون میدانند اگر فرد مسلحی بخواهد با این جماعت درگیر بشود که ظرف ۱۰ ثانیه به گوشت چرخ کرده تبدیل خواهدشد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20244" target="_blank">📅 00:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFYMEtD9NYhurmmj8xgOEJPpU-a_LVzFJngnYIFa2yYKPYHXObS3NLpjs0Ejl3doewftvdmDWPoOhThNpXm6VGB_J2d-k0lGpWLpiF2cwUxqKgnIOrr8HEwdEEIj-F2D49VX_0Hqaa2rk8kpXUiYiyfa4bfQJMN3Mw1vSMmZdJ5K1XZUzyvLFl-XbqOVrE9H8HaUVzbMbpo6SkXJKujpJhq7V_2ttuHUt_wsvxuXsb_D6vDBhIu9M4IfylCR914CZmkpH-gTJSguIdCPomFCNHWCR5rwFxLYySUZiPoRGsXkvFWp9P6F1pf0HPl4k1alPDIU6PSBlthRuwfNX70vUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhpF0hM4474GeK4nhrV2v0c9n8joCOm682VsBQxetAWbAoetKxOUfJi_1TfJRttoM2OQjZgiR9_wY4XKGjDi-2QpJAphyoBfUXUlHBnnx6b5ZXn62S6SDY2Yedr1ooDXDy7hgETnGV6HeZHlqk_i1DUgCYCqHy1ovEi6TnnEPrMJXj-aZ6x5B4p7elkHsNelEhqP14qEPmr0Go_Zg09bb-rPa9hKtlC1JVjNKYj9Sa2OoqgcWx55hntkeKUZiR2gkiwd9o1Rvw_8EFHYElpPmVMtxuSmvixSKD9NJKDTAqVfAwCzHV2ftAQfbvvs96GK2131U1OdqE4LAExGop4bRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 18 ماه پیش می داند که چین
«تا جایی که می تواند از اقتصاد و حاکمیت ایران حمایت خواهدکرد»
و البته از
خطر و ریسک این All-in کردن به اتکای چینی ها
هم آگاه است و متوجه است که به محض اینکه آمریکا یک امتیاز اساسی به چین بدهد، ر
وسیه و ایران هر دو
در موقعیت بشدت ضعیفی قرار خواهندگرفت.
اقدامات احتمالی ایران و پیآمدهای آنها را هم دقیقاً
1 سال پیش در یک نشست لایو اینستاگرامی
مطرح کرده بودیم که اغلبشان تا کنون محقق شده اند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk76vDlAtwmDC7iJjWnMJdqf8xE-80FGTckOoKoEm5pjSBCfLlwhPf6QUTQXvI-f2cCqULXXZs_fcucK59M0Cyx5cEvYLsSncPAbC-vmgEeth4jT3F14w08ky7OBepMnRAUV_S2-ahPM368lIpSKG0HJvYbfWcssSBH5fY1ZiBF-_qVZNsqG8Dou93okF9pgaEM4HeAvjXxlrjdKiEq8AVckqsoIvQF3331BD2_CB-xRffjUVsoPAq0WNhw6kvZDmMiSCZFP_dbN0OTr5cQzQ-8CrMi90uvRAx--gO4TUdQ6dpUVqXNG8kSyzvCin8sXvmVjkNowh990Jc6rGbr7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=i04nQ068XKcuccj1slpwHj7ZP2oO5taCYQ9wTHTL5fu2Uuk6RezS57RFP0Hg8hbfg9oR_Vrt5eLUR4h94uJQnOdC_3Xv9JtTYznWU4PYT1fm0dIbyx8s_bvbJyqr2egBSYS0neAZerIPX8_WPjJkmg8E7YP5p2KCHI5pt9u_Wlxe1H3bsqu4aG37_cheW4l_-Ex9VfD6QlKJPsxz6YzlqMnhj9n9lbhPVe2L39rvyt8ZvOfVYsq1qF9s4jFA3edwDmLa2bL6Lmc_Kt9N6PzpJOP5fnvflxxnRvSIpb4cnEAWrUNwEBw07j7WmFTe5bQoA1SXsamTzQworhh_Rp_dzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=i04nQ068XKcuccj1slpwHj7ZP2oO5taCYQ9wTHTL5fu2Uuk6RezS57RFP0Hg8hbfg9oR_Vrt5eLUR4h94uJQnOdC_3Xv9JtTYznWU4PYT1fm0dIbyx8s_bvbJyqr2egBSYS0neAZerIPX8_WPjJkmg8E7YP5p2KCHI5pt9u_Wlxe1H3bsqu4aG37_cheW4l_-Ex9VfD6QlKJPsxz6YzlqMnhj9n9lbhPVe2L39rvyt8ZvOfVYsq1qF9s4jFA3edwDmLa2bL6Lmc_Kt9N6PzpJOP5fnvflxxnRvSIpb4cnEAWrUNwEBw07j7WmFTe5bQoA1SXsamTzQworhh_Rp_dzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkeuSP7JgS1rOoRVna4gPSQJz34Wr4OykCnzgIi1n8EG9yNL4fQkT8DZTdklxmn9JrFYDh08-Glhy-ROFJlLkrHNDGUaJJqoZYjMTspfjfwlwYAjdWA22URXrPHGxClFWXdXi8yHov2qbxFhU-NUnFpcVxN-_pm-eYtNZ9zXCLTwLcV-hKtxjWxfDhIFLEmXKB1xuIqmuaXcTlBNWSm2B3FEcd4r-YbbQTQz3-gg20erYpNwH7uZHN3AXsfpHSa80r2GW5Jd7wpDB7p2TcNbXnszpJ1nYrhIS0f_VPrIqVkDIG95wFS7T6ieSwtU81Ukm2czE8b35GTA39iK-v63Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVza-2QG8xohtHMbg0SYHZn-EpHJSZf2BevkxcYYkiT3CygCqeGicYDE0yMAN2VXDvvQCHtXwG-_YeG8nxI4EPsqxebQYsVRbmjihDLPbR_kNGmBRxdnIn7TGBXViT8ou3L0sAeaqBr9N6AOhgV1-8p9qT2zgJgYtuQhAXkKjsxNCAArqPxkGUWERbUIPv7c89Trc12pSVJMl1Cygiw6r-3hGe9d_2PuHnrcTD7y1n49Xgvum7mt5OfAb7cxcpi1-Q4W1igWJXHNYbznbbAvgJTcl5Yc-qH80Ow-Kb7lsDo4gFEnQeA0G6xG2HjMWV49SypJOEcM9CR3j2eisWRcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8DdS-jcb_TgfrNRNjjCcIsV2MswrNmcIlrv339uZWcOBNwJlVkrceu4gVIHkGynUC_1kLf6neFKDKCDFVNkbeci7roE_WpeB7W5Vjsy5yXzueBT_LHchXyDJIAPGEVgZA_uST6MhLVy1wt5UhwFxHZhkh420H4I4Nlo4S3id6Yl76aABv2DtaO73Dcu3i8FK4YlnjPRqTlmXf7zMZdoC610hptNuQ7_z9ns9WLlDfZG1UlBAAWkR8kCg-fC8L0rnyL1zjBMiIv38Al9i7Q73MTjhhTXziseBXlSnp0ZsmPFuaoOPJUEvRF9ItHUWo7uSpgdHRC2yoOos2FV2oY3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnYbPsOFj2_ADgnv8HFcWz5rtnUmrqDSresITub_gmUH01yTGjuRLm6H5jHlMv1fj7zaB7wHCbBUVYObIT5kvBCT_97HbM2Wokq54LNFxo9qQMt1GpMaZUaViXK7qb9ZLaSAyvET1OWxJsCYDaNrSS0m9_FSX5-O6PVmkqbU85JUKz8rUUc9F6FmmpS_BJcMfYogJPYSSif3jh4M3dhQyRxJ4lB2Q6RJDmt6wvNdj9xsOf3TpD_fOTJHQZEnmdmppRmvr3lRtdf9kRyujOXDGZVlu-A2VHKBOn0hGgYqTV-0uJzlDm28Uunv2mucye98IZzgEyfSx2tLe37gucZv1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0HfYPR9nyVlEE_JG9tkmXWHBo2XLloUYRVv6LYcAd03BpI8owTerolCYomH9qeAhbai4pdd2IFCRdgvbZm0Gp4mojtFjApRYJnLDU9q3tEIYdBUCpeWtUsJI4MPONVv3K8MmnZHfu0j9pSusIz0JPrdGxeThcwlqlW5ucrCJtz5tBUKX39h6fF3S_qaKvXn05LrVPrhOxKhXW6RdzLzJDSPlnZYtXoFZ8ovFDP1tlGFyHOHuKVcj2oYPFW8ATP3EQ2B7SCjrMJnrPesG_x8WBbY9H_6y7VM9VF2tgAzR3vppsZ-UpRY81HolQCx_jqxeuDNRKF07Ar3m6Ard76PGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ1iHxmmp8bNeHG2WKotgwo0qrHEV_IUdCg1BXBhM_cTFLJfud8mX1VTAYFPSZYrgD4xDIGPn7LrDV6zn8rtabLAgguFd0ts8MeR9eq-0NUpwxNsDESt7A_PdnAEop9Esvi50yqQFEdsYrTuIFeBc8mjQIgMfv9Y-3jTTU8_l3EgWql1oBXOhkh2g1AOQDOqEHFI6i4v6PefFeh1MtHumVczHPE44RH6EYxeAcqD8dIhgHMCK_lb06bc9J8tt5nNyZ3vCyx_KyqJY1mvQ8Hg2pjK_iU1eHr7nvu4StdoDi7dIDHlExTgIrfldUP7dKHnSpCtUU0MMm-8HoPBnQm99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3f69Nd8DHjAiZDMZGmPgoBmzVTNHdz0dAcvzFqda2nTU23Ij9r9cJ-9LPSiAzsh4GDphZFQEoq3EofgKGquT8DPGWF45V14YkiSzoe3spZSM5WiuUAiJYxDYbDiu0h70G1kzJ4pzDDCHTNfJ41elIkZPdH_tSu_nJkK2is8BQdqoJ1B1opRI5CDUqmlnjxrCm8iV1_Jpu_V1uMjKxxqBfbSoXbPti_Gf8jjOvSaLGSiYD3oZesWnKPMtc8PNXmheOvPNWWcdmI_EyM8Zupvoa_3wPzxPUo6pjUTngSSvSze-5ZVzP9P-AfPUWmaWtZbIE9ldiuUPTyUH7FIQAZprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=Y7rEoNiV-00d25Z840aHyaKkDPvSrj61Tw272eKledVLTwhhJmYKct0UVQ8er52YvdlZWGhDo7aLAXa4siYy1iebI9cWkiMODsyHSfotwelG0gv81SzfmLVcMzD6h5OzZa6lWcmSec2uQQ8V_orUngSd61ygxpk5DPxfmgZSUoDZz6e_sTOJ9_9LokcAmF0WwQe3n8SFiG-evF9vOtGyIGV2-_HoXswBRZaFhf_zUGRpvZGjwaH1LdLPcUd_ixCyMHu2n9-cwnylIFkSY_fAJuQGpZhKimeqtOnBkVCiDSi8_91w0LMbKjI4ElrGV5s8MCL4FWIvxZzprjIbI8LFSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=Y7rEoNiV-00d25Z840aHyaKkDPvSrj61Tw272eKledVLTwhhJmYKct0UVQ8er52YvdlZWGhDo7aLAXa4siYy1iebI9cWkiMODsyHSfotwelG0gv81SzfmLVcMzD6h5OzZa6lWcmSec2uQQ8V_orUngSd61ygxpk5DPxfmgZSUoDZz6e_sTOJ9_9LokcAmF0WwQe3n8SFiG-evF9vOtGyIGV2-_HoXswBRZaFhf_zUGRpvZGjwaH1LdLPcUd_ixCyMHu2n9-cwnylIFkSY_fAJuQGpZhKimeqtOnBkVCiDSi8_91w0LMbKjI4ElrGV5s8MCL4FWIvxZzprjIbI8LFSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=AITOyEy8yzD9f38ACRY-q4xlvtNIQ-8zfH2inqOiJZbLkV9tKpO9BTjhAdZ9EjL38-SsZEMOrHOq7LOWUytvFiWLoUg7FX0Blh7dI4S7hsvbrFkxuxHefWV-WRv4PyswRNidTEVl3nUUQKWnWPAEEw8iaM8F1NmvyRhSC3Sq2MqRsjTYOQ9vOPVbnT_iiR6e5c6nsx-SRdcWXj7VGg9jvSITgg3v1-kTi8Su72QW0wb--8BEXVPgZnIMy_HF71h7X53rm9yxuu2Nd_elaCN6okSwu5rplXmlUpATG7bWVbrnxSnyAu-sHS8zBMrKrRBF408m33-YFfEm9J5FA0aM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=AITOyEy8yzD9f38ACRY-q4xlvtNIQ-8zfH2inqOiJZbLkV9tKpO9BTjhAdZ9EjL38-SsZEMOrHOq7LOWUytvFiWLoUg7FX0Blh7dI4S7hsvbrFkxuxHefWV-WRv4PyswRNidTEVl3nUUQKWnWPAEEw8iaM8F1NmvyRhSC3Sq2MqRsjTYOQ9vOPVbnT_iiR6e5c6nsx-SRdcWXj7VGg9jvSITgg3v1-kTi8Su72QW0wb--8BEXVPgZnIMy_HF71h7X53rm9yxuu2Nd_elaCN6okSwu5rplXmlUpATG7bWVbrnxSnyAu-sHS8zBMrKrRBF408m33-YFfEm9J5FA0aM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLTg1XLufq-ohJTBi76lAewvAD_Tq6a_C32DwaubuqdPjal28IvU-C65oEmNyZllybtwX0MzyxxcqoOLzc5e9BXbxHIzHezbhXXQG8GT7w_VlK3Oq9cIkQPdxG3ntODsGLSNoqA6gdrQabuRFsYs05L-4kYzNbggNwdMu_1wTrPbA-_tUUKQx0Qaa9Z9ycgs_s4Ohfn017qlMPqdEELR16JUcDtEKfR-6ZAF4dR2ooeZptUnJT2vavs0GrOt04BJlzoFzK2bswrUYPr6XClJZGJc6z8pouTepn5dMGszp_qqGbXV3b3BzCUEvjeuBVd8V5qqE2KSfabQtNSrenjWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmo2HsHjvDrNbOR82yjN-UF3N7EvWAca6Ohu6jk1MoSjbnu8P2Csww-SkUGm5z8CH_JH9v0K1Xmup0ntOV6AWDnd17QJKyS8USPu0iKXCFN5lCywVxm-_5ntn3tHr16gnuClbCcKLYHUFvgouUloJsnNrMDEvbFBBAoR1Q2vr9b0TTx26fVibbyT6hT7wg2nFqPhAlBdq-t_euCi3GA8Mlf6EucMyoT7AKt1e3Xt3ucTSmPMu04GC_YXgTD8cRsgitNGciK6FXQJWW2nyyGBvcLLn4sA66dQmY-74OCG_t-AHBZCO8ewFZqtrFWdeLHOEpx5aOCHAzVebYV5OF9qIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqvwppVHtct41M0MIRWc7IcwzytwZxoXV1PNSDbdtZxQjH7tlNuDzhaNulFvbwwFOqhLjrsnWL6YhuzvJQrnslIjOygulrW7Wy4f_v2VM5IHVTaQPQx_5GkNGyYE6MpWWN2PqQb4nw7LSV8_b3jhHMOBPoLirvdCJsL7FdcHkIj_1i7FCCnSzy9oUbyRqLVPKomMR3b5mFqwnHMGuVR3f4HcmfKPgKtxOWqaTeoc5KMInu2-lpZth7fJ_EvHzVkJ9qqD8yEDLWsV0k3bQiZEynA_btRPbAVqQQ9XSIlxxzRFyh4vXx29351WZUOD_fKUxs4SG-sPcmvJaMr0dXOOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ایران و عمان گفتند که پروژه‌ی مین‌روبی در تنگه هرمز را بحث کرده‌اند</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20199" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxNlhedPZtviP0OknT8v9Ctpx5ac9JoRGSofWGSDAtV-PJ-sJFrfGIzVaZbeOXvzcWf4jIRtsRnuxeedFtjRf64oZej3GuaN_tFrlXaLfWA64OPxrMWH_yYl4wSlsDbZl1tZ9iedgnU0-zwITK_D6BJv3DW8hLyV5KUNGYcwzkyyg-cL9o3RuwIn5UdepRxb_g28UryWdvMGf6koK6YAZJMd5ur8e4LS3hlpbRvnuMRZI36B7sUPjU_AvHrggeXpcFc3Anq4ffI3KrIi4jklrn3BjK9BQbJWaxkG6CrfZkUEhHuF695OAxtrfV0i3cKNoRa8WPJJwiHE9hKdfYcyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تمام مین‌های دریایی که سپاه پیش‌تر در نقاط مختلف تنگه هرمز قرار داده بود منهدم و یا جمع‌آوری شدند.
همچنین وضعیت تنگه هرمز به صورت وجب به وجب تحت رصد ماهواره‌ای (نیروی فضایی ایالات متحده) قرار دارد و هر اقدامی در جهت مین‌گذاری مجدد با پاسخ ارتش این کشور مواجه خواهد شد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20198" target="_blank">📅 18:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlqJe3683aLMLclmqYBIDtYjIrSelj55bE8O73uy-VdKQ-KHDQEITGkPO3iAH1CHMCgct7bnptc7S4eJRcxA4v3HA0gbP1tyjd6fQ_E_hiwQn9_Yaw-1TcuXNM0Fd_3Ytg-GAc4otv8m_v6wRihBzwa_BVBPAYeBk15-IHtxGBaMHHcqqi41dq1o_d3c-a78A8bzLfm96N-sQbDX5s5fpVeYv0TxBA_MWwE4VWjTbiPnDoS1xxCdbL13c5djrtO20kZDYIwPOIhDtccXpgUCnuf_SheMmuhFKcUEcR7jm18mxNeS02orwsNtT74NixOOU_6BiBh57W57GEvcxxWEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!  ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20197" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Srlgpdqf3Cq8L9ZrQsJ686LteSmlEnKxOrx306KA3697MDR104M0x8es0hXhps9VgkbqBUr0k6wdE_HLIZFW-YYQmxhAEJwx8PHcf-qwNVJ3Yi6Ee8Sp6r-c0-n45EhDGpqYkSkRZ9wLJ5wrR_otNIvNVVztTW6kBA-xSR2x196Rfq3tXqlMRtazrxdiYdt0AENngAa6gMrSdnMAc2Fsg10PxRQgSSogfYB45rHlP5AgaBDyFxNiHG3VqFAtF0GgeDbKw6tUSKcLsUlkz4GH058qgEH6FxoKsSGGqna51XtZ18q3ilMlRHxFpqcnvXVaLOEXCmYpzuQcun7nkek5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtmyEBV5351cZKy_3-T3KtqiMHgO7sE_YYLLU0JqOK3RvenO3bREaKPrNbdNDTy06xbNxDWomyUUh-Yid9engGbkoPOCVxuHKW_c8l9INGzB0b47CA8KlcleP-3CFl62bJkMZpnBBsx3xr45QjfHgUJrvcCK-_db9VeL4_CMNOMXPmqOoQHGbt_BpZEdhqc5mF2-tvgxQt2esNrw31gE2tU4SZguSPDgg81RWUG8CumOb2ihtI214OkViT5fTheO31e1soiNQCIOlp3VBkhT05pzhxbcvnuqIxIbKOsFjUKY_6P9woCJTCaTVcgmlkCQWL8zDcdgGlcHgOuiHtTiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esi_nsvnQx_46nf-sb6jZAwSIIwPFFNqcehkhtSGE_uiChnHrwlQVscApxnQzPrb2Gy419vuW1tQFnkJiM6N6oxxAKkyMkm6A5r8lKe2l2guaHCuG4JxJcZPJDW6bpdccsyIB2fbEDTn4inKazPfYz72T-98Gvt4MxkOenwqd9N_rsMqkWUmPPvbOADwCu0jLnPpHmXQQv8cLblbzZPITyu_J55WiVXdTI81Y8kX_ab5etUyyaBrdcMHke18rTxTvMkH9uop-j1fTd8AtrBiXKxkNfALkn_uk5axQcAqasDOfhN5EVhT-keR4t-cTFQy7WsU0TfhehVzpMKnlmvmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:
آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20189" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD6tzU2X3lsoc_t1s4BZHunnSOkcJtLg6jW8Vnwfc4kzr_TNI4JrvBhzXrxwugRtLZyPB-7Rw2mi0M0LO-puuBxoH6LL9N20xjmdJUoOr0awHyzUgUIfEujIr4uTNxVXSdLaqDNX7tZDM9I26n2cjblnRQPUISlBC5zx9ZmbK5iB4zP_Dc4gPr13ggEV2ppA5ri8_0syAtGTt7L_QHrzRI17jKc2AbTn-R3NjpXgbZgBKQZEXVxnbQl9uzI-_hqhdsHx7AnkeEQEIeP33lmvcpC1UcW6l76WVFWf8bfBiQ_AKBqWayaVrnSTFiT45d8zVdB0aqvQ8OTFh9Ykar_mvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.
طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.
دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20188" target="_blank">📅 11:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFH2DHGvMcuUMYZBDoqzZKjHo5RMo73pYOJ5o_9BJq_fuIrTGe-LGeKUzG3IwDcrsIqcf0iwsoP09da64QinoY7nGcO3Rv7V25JpopuCRav7nnPlVd20rBVpyxgBcEw3SqdFVGn_QfG8HhJykv4jpTOWnBxamzeX_uCTE2SwvnSYRc9f3dJDRNWFhBX8EYtknD6sOyK6sOcpZ817yD3cnNx0QRrZDrxRU7cmhLdRrdP8sH3lZmDUZfL_D_hjSoef4nJmHhAzvCVpeGyjX33jT8eVtMqRCgXakQw9MMtZatx8lEQa2KNypsBV4kE6CE6JOZ_JyuxR96bqp9mqxeTCiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج 2 نفت دارد تمام می شود.  موج اصلاحی دلار به ریال هم قاعدتاً باید آغاز بشود با تارگت 240 به بالا.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20187" target="_blank">📅 10:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDyp_5NPPJkxn6BEjVQJtZtutqwRtGDhHrTy77_JDSJknuapB0jT2-m-0i9a0EfU5ShRk6YNhvy115RAUso4S4YJo5YIGA7PQ1tAG3qD0iQ4F5098VkrjfmUJUxdy388NQ5Q7WVppk_3FMA5mKSDrO7mc2CzJB5wTDZVXVDXb39zppwwx1_UlULGG9iVwUxV18eyG0QbN_8qQe32P8Thfoce--G8Ffl_Rd6h_vd9jjKi-my4E8R4N5cdBtjiAzl7LDTwm8n8FEIuDIPtgXAGjVb0NTqNgWvNbHkrFq1-B3ywbUfeK9oWhsCrheilMylelthmTT8eiMyaR8mjJlSzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20186" target="_blank">📅 03:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9wWLw1qGaZUvrp7tz1-lfOMHPIeNZw5qptS86SwixAOm8ZHw3LtEQT6CY7-Mp7kvb62NFX_xlUUAMqUQrPE4kyBsqzxwYlEF76WGOu5ZLxAO6fJxzhRmhcl4fi5YpM4m14W1rluSDdbwgpgEPy3deY_opOYAbHQKN1E_BIGMzSt87ePvxCwWdXgupUzyeopnupQXYLYeb93ZDAOvixPGTJXjgxUHf56Od7WF6hwk_nLw1qh8RgIq0634m3ekPcui3qUZRfZeCnG2Uh7owCg0IeIXAi9V8DzEYzQgxG433U9EIShMyJOks_JDsMjb6dZAZSz_pntE1fXbApx7T53yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.  دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.   ولی با این حال، پیش…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20185" target="_blank">📅 03:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فرمانده انتظامی کل کشور در ساری:  جنگ سوم هنوز تمام نشده لذا باید با آمادگی کامل در برابر دشمن، غافگیر نشویم، چرا که خیلی از غافلگیری‌ها نتیجه غفلت بوده و دشمن از ما دست برنداشته و جایی از ما دست بر می دارد که ما دست برتر داشته باشیم.   دشمن به‌دنبال ایجاد…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20184" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20183" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=WN7aUqLiG158qWsN5txDAiKhKB6BZD0hI_BdfRS2Bc_SHGbdKWiPNhwkSzUH_DM8u98V8bc3UDyUqSOuo7iaQ1hOBt22mFWCZPD3oDWNAeP-oc64Fzxgk3jzA5VJUCIN-ikvc3KNih-b0SACp4fPUdxgopIlZ7VAeQv_bJLq7IYuJYTwe0LFoSkAKtQ2jAvfV6DFxderS3-KGdKQC81B4JWDjUJeuna_iqzDjhiJVENhF9UkpxtdYWLN3gAgJrSrA2qCBb__iaoGg_4wSamfapsEVORYVREXF34qLfWZLSevAZb6jh_RvJQ7Hrzbgd9dvcIk39Fg8o_q7ttSaUEJrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=WN7aUqLiG158qWsN5txDAiKhKB6BZD0hI_BdfRS2Bc_SHGbdKWiPNhwkSzUH_DM8u98V8bc3UDyUqSOuo7iaQ1hOBt22mFWCZPD3oDWNAeP-oc64Fzxgk3jzA5VJUCIN-ikvc3KNih-b0SACp4fPUdxgopIlZ7VAeQv_bJLq7IYuJYTwe0LFoSkAKtQ2jAvfV6DFxderS3-KGdKQC81B4JWDjUJeuna_iqzDjhiJVENhF9UkpxtdYWLN3gAgJrSrA2qCBb__iaoGg_4wSamfapsEVORYVREXF34qLfWZLSevAZb6jh_RvJQ7Hrzbgd9dvcIk39Fg8o_q7ttSaUEJrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20182" target="_blank">📅 01:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کری خوانی وزیر خزانه داری آمریکا برای عبدالناصر همتی:   به زودی دلار 300 هزار تومانی تحویلت می دهم</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20181" target="_blank">📅 01:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T05eHvHEPFRIj9zYDZTWF2X6ctShZxc73LPJF8zSlA5auOI0J3tqu9U1YBrnkgKYSDD__GlWhMgGfXoHACfQohP7-_rrj9S9GcylOuZDHgZITw_c7FnON2tHpByAURJtbwIno42Fz9C3CQtlBpCDwuh7S4BwZoa5LMu7pmeOznxr8YNcBn_OIFRjK-erWXhpJKkbf6ZHh1HGXvcGjOEZuEAKETOUx2Afr033ntHGRe5v-E3-t0MMYcDmCNhT1bsX_zwPqd5NvxYwwfGEsmrV0wth91JeucaKI1QGWmTHxaNNP56knYMUJWIexHiDUD-NcsrB6sqr6VV4pknGdrU06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20180" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20179" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyS7FeR2ZcTkWVd1BFx9S83gtjNu2PBO5L-Emjvm-_3Pz5iX9QqZiiCKXKHzWjAKc6cRaee9RK6b41mjgaQIru4WHdScwj3mHTVlx4UxU_6uyeRs7V0L3_byk3bz6jNTccp0SvHc3AQ4jeVY1StUuySbxIL3ioFrKDpLAK8uvF6BPyPW85JXfnjxoesq_wXoYizujTJo3rOP7oLaRlttoaYSz3MuVGhs6cQqxf9J0-DAf04U7k0iQU3V7LpmMda26lGA5I50-CytR79SnVB03kOf5g2ahkziTLNOhZYqZamOgANQPrGVTvD8KNjuKgXAZCpVh7VIcHWYDIyBzX34Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SBoxxx/20178" target="_blank">📅 23:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده، درباره‌ی چین:  «ما می‌خواهیم امروز اینجا روشن کنیم که هیچ‌کس فراتر از دسترس تحریم‌های ایالات متحده نیست.  اگر آن‌ها تسهیل‌گر معاملات باشند و بخشی از اکوسیستمی باشند که نفت ایران را به پول و سرکوب تبدیل می‌کند، هدف…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20177" target="_blank">📅 21:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسرهایم را به قتل برساند
کانال ۱۲ اسرائیل: سانسور نظامی ماه‌ها انتشار جزئیات تلاش ایران برای ترور یکی از پسرهای نتانیاهو را ممنوع کرده بود.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20176" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «خطاب به سربازان عادی حامی این رژیم: همچنان که حقوق‌هایتان بیشتر و بیشتر قطع می‌شود یا ظاهراً فقط به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشورتان را برای پیروزی ترک می‌کنند یا برای ویرانی، و به یاد بیاورید…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20175" target="_blank">📅 21:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «ترامپ در حال برقراری تماس‌های تلفنی با رهبران جهان است و درخواست‌های مشخصی برای توقف تعاملات آنها با رژیم ایران دارد.  اکنون زمان آن رسیده است که رهبران جهان بین آمریکا و ایران تصمیم بگیرند.  هر نهادی که از طرف…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20174" target="_blank">📅 21:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20173" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
«امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.
ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه شریان اقتصادی است که این رژیم استبدادی را حفظ می‌کند تا زمانی که تهران به تنهایی بایستد.
از امروز، ما حلقه محاصره را تنگ‌تر کرده و هر منبع درآمد بالقوه‌ای را که سپاه پاسداران و رژیم ایران را تأمین مالی می‌کند، مسدود خواهیم کرد. ما در حال اجرای رویکرد «بدون نشت» هستیم.»</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20172" target="_blank">📅 21:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20171" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2_W-xN6OKgcr1lFHx1P07YdH5LmYDn02gXaksQli4Xz4SYh0UV6OTRBTEX_rPDmR0sIjLKzDQ6hvl5jOZIgvq9GRJfpnt2lvUeXWzSurvM6TxWfmvDzT0d2NMx9p5DheH1MYniPuRVUOmexTsRqN8HOO5-CdRoMOlv-e9xrpyNaFgu0HeTWFSWMHCWP3PoW9ZxaLfhw8vBal58KCV-eO79ryL6Wp2FbXlzk7nHGCgJG1_4ESfm1u1kbHhRzNHqR50FTobMFGNo00erDzbkCEfrGonyghm9LCQoBVoXprUx9Q9zH0CCPlSMhzP_QAUmD65HZfO-KyK5KZLpGf6uvew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2.5 ماه پیش میداند که هدف درگیر کردن ترکیه چیست. بزودی یونان هم به اسرائیل خواهدپیوست.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20170" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
