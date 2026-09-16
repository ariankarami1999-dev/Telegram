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
<img src="https://cdn4.telesco.pe/file/hejHqzUpMzzX9DxeFZL0MfxDD0g86OSyNx5bvdbsZnjmU0RhnERMh9wkGfThcuplrm1pwJPscV-f4dZsc-qlsHLAH5WPw0R6v9dz4VIKYStW4aZKhb2gXPRB8CRSPQ_Y1Yim_ILwW-8nQzmeJQMR3_Y7zWyfqVumHNnva8RMgLzzJE3RsF2XNVbISMxSby9bvK_J9Ic-frPQp88XPOpvy3crmWJrzeGHSgo8BWLsGSREj9yP3xAAoVQ-x0DX67zBISIIMbJqUgv6s2XjMzEVPQfJr4qbINQHH0_jFlrdr7GBpRMA-EhRvo_XWxeK-pE9k3Pob-vk3utejqwmeSv7Lg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 22:28:37</div>
<hr>

<div class="tg-post" id="msg-147780">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAVGo2OStTDcUNg62lgJTHv50U9aHbSqX-Ij01cQgBk7b3wWiPe_Z8tlP-BEOFCSEkEokGxW00xy5l65E7feRPPYNu9FgxdCYqYFmsbfx2XGyh1DMd-T-UIA3pqxQd-KnRtrMxIKA0in7w8cojxOZRWR3STGJnUczjOpuZ_uvKtz-_a_4osgRKRlNFmLSYjZd6oX2kdQMyKU162dZzwZwbDOaMYWytSjgjfgKg7O4E-akYESddf6g2Hi59-mByxzgmyJjTd2ncnS1OiCKpxP4hPYvx_OVGUIZtcOR38mqaZWYaM4gwI0P6B4SxDEbGuS8EDUtdN5qZjdQQFoPIEdtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ریزش ۸۰ دلاری قیمت اونس طلا با سخنرانی رئیس فدرال رزور
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/147780" target="_blank">📅 22:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147779">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
یک انفجار بزرگ ناشی از عملیات انفجاری اسرائیل در قنطره مشاهده شد که صدای آن در سراسر منطقه نبطیه شنیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/alonews/147779" target="_blank">📅 22:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147778">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بانک‌های مرکزی عربستان، قطر، عمان، بحرین و امارات متحده عربی، نرخ بهره را به میزان ۲۵ واحد درصد افزایش دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/alonews/147778" target="_blank">📅 22:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147777">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر دارایی ترکیه: جنگ آمریکا علیه ایران، تورم سالانه ترکیه را دست‌کم ۵ تا ۷ درصد افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/147777" target="_blank">📅 22:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147776">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqSc4ejtDfUto3va3ZetJxJvrcp-vD1hBLLt-Yib9hewaO2nHnJLomH7eNJ-AxRPYb0QhotXvRXVng61OLUVlCdcBhgECazmHYR-c3UENfCmt_TqhCEiP1GBF-d4itwuy8TKlFP2nTli9VR3DvlfpmFKSdjLryG_XwOu3OwmDy8qdLNo8ofGMm6-qRizPBeiOWVmVnHGLdVndFPPxuUNwkMRt8IodsDc6zIf7LJT5TPYTJdDJdRMDRhDzBcrUZI33jfLd7KsUcksIjkMJmKDHv0GVH_UamztmHFx8-ffd0IaDXQVi1Tzy6RjxfpbcKRcC9e2H_mKsSoCJUrmnnUQqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جانفدایان امروز رزمایش نظامی داشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/147776" target="_blank">📅 22:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147775">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری/ اسرائیل حومه دمشق را بمباران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/147775" target="_blank">📅 21:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147774">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
بلومبرگ به نقل از یک فرد مطلع: عربستان در تلاش است تا ظرف چند روز آینده، حدود نیمی از ظرفیت خط لوله نفت سراسری خود را بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/147774" target="_blank">📅 21:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147773">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
طبق گزارش ها تفنگداران دریایی ارتش آمریکا مجهز به سامانه های پدافندی کوتاه برد با سوار بر نفتکش ها، آنها را از تنگه هرمز عبور می‌دهند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/147773" target="_blank">📅 21:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147772">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی فرماندهی مرکزی آمریکا به الجزیره: ما وضعیت باب‌المندب را به دقت زیر نظر داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/147772" target="_blank">📅 21:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147771">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزارت دفاع عراق با انتشار بیانیه‌ای، اخبار منتشر شده مبنی بر صدور گزارش‌های اطلاعاتی درباره برنامه‌ریزی عربستان برای هدف قرار دادن مقرهای نیروهای حشد شعبی را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147771" target="_blank">📅 21:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که جنگنده‌های سعودی در ۲۴ ساعت گذشته، ۴۰ حمله هوایی انجام داده‌اند و از پایگاه هوایی خمیس مشیت، از جنگنده‌های F-15 استفاده شده است.
🔴
آنها افزودند که این حملات مناطق طعز، مأرب و حجه را هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/147770" target="_blank">📅 21:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147769">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
اردوغان: با پادشاهی عربی سعودی اعلام همبستگی کرده و در کنار آن می‌ایستیم. تلاش حوثی‌ها برای حمله به مکه را به شدت محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/147769" target="_blank">📅 21:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147768">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/147768" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147767">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
رئیس کمیسیون اروپا: از زمان آغاز درگیری در تنگهٔ هرمز، اتحادیهٔ اروپا ۹۰ میلیارد یورو (حدود ۱۰۴ میلیارد دلار) هزینهٔ اضافی برای واردات سوخت‌های فسیلی متحمل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/147767" target="_blank">📅 21:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147766">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnGSIWa7qJQA-Lq0TCuWIA1jb7ZceNPCvvGEkqvSvlGK73fLOjqRzgJWTzAhpulKV2M4Wt2v83jKq2L-sG1vQuQU7LaYcBJhe_dp__NYuv2Uv3heQqha7WDYY8J9kSgQcrl2kUex5si1ZarjUHd-jW9fozlALut9WNL__ACZhbTM5DC8aEeXVEasfes03ONfuITozaFgmHjuqFfEVEKhahDw6Ef7gLTqfZE3pqR8v9kOZ_ffwCWK1Az88rYH7wpcWpBVrbsKJavcopwldNicHLN5H65WdjE7eCSVsqHRKgt5tF97n0ql6-e5i5KEXkw3IXg7jycxT0Y2lOVAZTLQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تخت جمشید معامله‌ شد!
🔴
الحاق حریم درجه دو تخت جمشید  به شهر مرودشت نهایی شده!
🔴
ماجرا از این قراره که می‌خوان حدود 160 هکتار از حریم درجه دو تخت‌ جمشید، حوالی شهرک و محور مهدیه رو به محدوده شهری مرودشت اضافه کنن.
🔴
نگرانی اصلی اینه که با این کار، مرودشت کم‌کم به محوطه تاریخی تخت‌جمشید نزدیک‌تر بشه و بعداً پای ساخت‌وساز، خیابون‌کشی، پارکینگ، ترافیک، پروژه‌های شهری و...هم به این منطقه باز بشه
🔴
جالب اینجاست که بعضی از زمین‌های همین محدوده، مثل تپه‌های فیروزی، هنوز کامل باستان‌شناسی و کاوش نشدن و معلوم نیست زیر این زمین‌ها چه آثار تاریخی‌ای وجود داشته باشه.
جامعه باستان‌شناسی ایران هم مستقیماً به مسعود پزشکیان نامه زدن که جلوی این
اتفاق رو بگیره.
داستان اون‌قدر جدی شده که "محمدجواد جعفری"، سرپرست پایگاه میراث جهانی تخت‌جمشید، در اعتراض به روند این پرونده استعفا داده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147766" target="_blank">📅 21:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147765">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی فرماندهی مرکزی ایالات متحده در گفت‌وگو با الجزیره: کشتیرانی همچنان از طریق تنگه هرمز جریان دارد و ایران آن را کنترل نمی‌کند.
🔴
ما به تسهیل عبور بیش از ۹۰۰ میلیون بشکه نفت خام از تنگه هرمز کمک کردیم.
🔴
ما مین‌زدایی از خطوط کشتیرانی بین‌المللی در هرمز را تکمیل کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147765" target="_blank">📅 21:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147764">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAg6qvVlh2L8cClggX5_mAbQvcLFOEfuD6lJaYEWGPZFl-J7uekZieL5igsHQKkFdchBiojtXHBj8sLTdWErSg-p4YV6MASM3EUr6uKyQOJJoweEYHMunCvrEn1MoT0rlw2VN9Zljqi9dWhGXd9EvqehyjdhRaJn1NRpWt1ebvAAYSKQaoZoNBE8E8zYPMLcURVhOfXP-c56MG_LYdAnEBN23NNi7TB8UqjAHr-lw0_aiTN_QGnIK8AzNsspLdkM3O7lA829Q7tl54tcwrNsJLPFmnPVUbfTZvDS0axCYeemVZP1QHJGNcvEcfGbvPb-LEIPI-5UKkQDQfgyNDLd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلمان چهار فروند جنگنده یوروفایتر را به لتونی اعزام خواهد کرد تا به حفاظت از حریم هوایی این کشور در طول انتخابات پارلمانی ماه آینده کمک کند. این اقدام در حالی صورت می‌گیرد که نفوذهای مکرر پهپادها در امتداد جناح شرقی ناتو گزارش شده است
🔴
وزارت دفاع آلمان اعلام کرد که این جنگنده‌ها به مدت حدود یک هفته، از اواخر سپتامبر تا اوایل اکتبر، در پایگاه هوایی لیلوارده مستقر خواهند بود. لتونی پیش از انتخابات سوم اکتبر، درخواست کمک‌های بیشتر از ناتو را ارائه کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147764" target="_blank">📅 20:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147763">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
اگه توام تو ارز دیجیتال سرمایه گذاری کردی و نمیدونی آینده‌اش چی میشه بیا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/147763" target="_blank">📅 20:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147762">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت امور خارجه ترکیه: ما حمله پهپادی حوثی‌ها به شهر مکه را به شدت محکوم می‌کنیم.
🔴
ما حمایت خود را از حاکمیت، یکپارچگی قلمرو و امنیت عربستان سعودی تأیید می‌کنیم و یک‌بار دیگر همبستگی خود را با عربستان سعودی تأکید می‌نماییم.
🔴
ما فراخوان خود را برای توقف فوری این حملات که همچنین ثبات و امنیت منطقه را تهدید می‌کنند، تکرار می‌کنیم و از همه طرف‌ها می‌خواهیم از هرگونه اقدامی که هدف آن تشدید بیشتر تنش‌هاست، خودداری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147762" target="_blank">📅 20:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147761">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
گروه حوثی (انصارالله) اعلام کرد که نیروهایشان دو گروه از جنگنده‌های سعودی مدل F-15 را امشب مورد هدف قرار دادند، زمانی که این هواپیماها در حال پرواز بر فراز منطقه "ال‌موخا" در استان "طایز" بودند و از پایگاه هوایی "خامیس مشیت" برخاسته‌ بودند.
🔴
آنها مدعی شدند که موشک‌های پدافند هوایی تولید داخل، این هواپیماها را مجبور به بازگشت کردند، قبل از اینکه بتوانند هرگونه عملیات تهاجمی انجام دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147761" target="_blank">📅 20:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147760">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ویدئوی جدید از عملیات نجات خلبانان جنگنده F-15E سرنگون شده در ایران منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/147760" target="_blank">📅 20:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147759">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان ایالات متحده، اعلام کرد که نمایندگان مجلس برای تعطیلات هفت‌هفته‌ای پیش از انتخابات میانه، زودتر از موعد از واشنگتن خارج خواهند شد و رأی‌گیری برنامه‌ریزی‌شده برای استیضاح پیته هگستث، وزیر جنگ، به تعویق می‌افتد.
🔴
نمایندگان جمهوری‌خواه مجلس نمایندگان امروز آخرین رأی‌گیری‌های خود را، از جمله در مورد لایحه تحریم‌های روسیه، برگزار می‌کنند و پس از انتخابات نوامبر به واشنگتن بازمی‌گردند
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147759" target="_blank">📅 20:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147758">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41485a95c5.mp4?token=Oyl5UQNVAJSKQTqkjJc6y9zDxbyfwFdJCocYgYUIVMI53oQdSWL_B-pZqwXEookDpIbg2akEUn8Zw3lu5If6HIifZkNpJNC6bgdwpFnbQsVk8Btt9Chf9guucayEa6ASEviyd7iZe_WpoREw0iRmsFpX2xw7C-4qmwk0w33uUSrzqdFfNUSfdlhxdftnT3fIXODQJT5lA2dxPpaNI3dhTBbmYAfJmjxTNZhq-9iCFdXRQuXwNDws8oYzQhacYhoQZ5_kh57DDp8W0hZVLpnqaAJvNNArlMIZjDC6-bCXIhJ3jzRKpDnbhvDLxq7Y7yN19N-vPUREiyEKGDtGpbq8IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41485a95c5.mp4?token=Oyl5UQNVAJSKQTqkjJc6y9zDxbyfwFdJCocYgYUIVMI53oQdSWL_B-pZqwXEookDpIbg2akEUn8Zw3lu5If6HIifZkNpJNC6bgdwpFnbQsVk8Btt9Chf9guucayEa6ASEviyd7iZe_WpoREw0iRmsFpX2xw7C-4qmwk0w33uUSrzqdFfNUSfdlhxdftnT3fIXODQJT5lA2dxPpaNI3dhTBbmYAfJmjxTNZhq-9iCFdXRQuXwNDws8oYzQhacYhoQZ5_kh57DDp8W0hZVLpnqaAJvNNArlMIZjDC6-bCXIhJ3jzRKpDnbhvDLxq7Y7yN19N-vPUREiyEKGDtGpbq8IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ما تابعیت کسانی را که به سربازان ارتش دفاعی اسرائیل توهین می‌کنند، سلب خواهیم کرد و آنها را از نظر مالی نیز مجازات خواهیم کرد.
🔴
زمان آن فرا رسیده است که با این موضوع برخورد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147758" target="_blank">📅 20:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147757">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل ، کاتز: ارتش اسرائیل در حال حاضر بر حدود ۷۰ درصد از مساحت نوار غزه کنترل دارد
‏
🔴
عملیات‌های هدفمندی را برای ترور مسئولان ارشد جنبش حماس در نوار غزه اجرا می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147757" target="_blank">📅 20:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147756">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
عوستاد رائفی‌پور: کاملا مطلع میگم که رهبر پای کاره، حتی شبکه های تلویزیونم چک میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/147756" target="_blank">📅 20:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147755">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
میدل ایست اسپکتور:
چیزی در حال وقوع است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147755" target="_blank">📅 20:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147754">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAZgXInA4Dt040qt7FNw5c7Oo4LqBGoCQ_871Lw28kItODf9K-t2dO3yQxHNDVYU2M1mRLF-BpohYrR8CC2ZYH8ubnxL3aPFa-Gniug5fO8OwS0DY44I5MCyLm0kfsInct-l_WwF41gGj3EP8_Of_irPqUesCZg29f-TO--UheDzB0MEaGjYFv-ucZwqar399Cet9a2frsxM3JT9krM_pLbYSATWibjiMjxEm49uuI-1CjgfYH_4rZCGpWZu_I1T2ibung8IYX3n_h74wBvI7oaZuYiBsDOuZsOOVq7ZUsPYXy0jxdyqzZVRbqbQZYEXc9pXKlENpgUFlWX28KsPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش بلومبرگ
، عربستان سعودی قصد دارد ظرف چند روز، حدود نیمی از ظرفیت خط لوله نفت شرقی-غربی خود را بازگرداند؛ پس از آنکه حملات پهپادی از عراق، عملیات آن را هفته گذشته متوقف کرد.
🔴
شرکت سعودی آرامکو در تلاش است تا با دور زدن بخش آسیب‌دیده از مسیر، امکان راه‌اندازی مجدد بخشی از ظرفیت این خط لوله را فراهم کند.
🔴
پیش‌بینی می‌شود که ظرفیت کامل این خط لوله طی حدود شش هفته بازگردانده شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147754" target="_blank">📅 20:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147752">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMQ9QfECc8noG99tIGW6Xnv1DDgk1oJPnB4PzrOCplxkQfe3J4jBlg9Xjxc5AMUfBprtnanID4uZlw4D8NbSotRmR5ku1U_IWYVK_md4IRRboKmhO_rZvVY7CKC0AhCByC655-JvY7XSKUo6lucrMrdgaJMb6vNCCByRgQuAVEdTZsH929SgZkCrb0QTDxuWUF3UE6k1x_arZBLU5duhnmSIBFwTVWCGX8w2E9raODtCKAMyWpMFakUnG37HmB8DKBtMEbFKth44VJPx3SHfAW2bSNuFUCx8v7JYYny-Ri2fgKLethqnPyyXUFy7UyX4-NT3FTS5OPvKgoDtjhxY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDpsDEK2RsqU7hGnRkO7nfbeT5u1688f1jfy7ra7wXH11-KQWyxaVFezeE85ejt44IDuFHqjjvZ60D_0Ncll1okuyTYGwXninHz6laJJ-tyXZWCnPxpRIMuucO0axI-fI7-Hy0kdKfaQhM3r4lNVu8z0h55_OMaDGBFkrANnZjENksBh6F9fdhb5lxK1lfZVImRkVvVxld73BGaqsB8V9yPYsJOsV91bekBaIkOHo9de63_gVUiW7MI8kqoE5I6tjNifP0MYZTEBX_XxIWVfbFUzmHwVjHvrxQaENkMxg2LtuYJLvjBH5GrGt9yM4-yA2-p354ziqNWLf5goGoe0KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
احسان موحدیان تحلیلگر سیاسی :
دیروز جنگنده های اسرائیلی تا آسمون عراق اومده بودن با سوخت رسان های آمریکایی
بخاطر مقابله پهپادی ایران و لو رفتن حمله عملیات لغو میشه باید بگم که صبح دیروز از شمالغرب کشور حتی وارد حریم هوایی شده بودن
آمریکا و اسرائیل داره تست پدافندی انجام میده تا برای حمله‌ اصلی آماده باشن
اگر لایه های پدافندی ایران ثابت باشه نهایت تا ۲ هفته دیگر حمله بزرگ انجام میشه ولی اگه متحرک باشه ممکنه ۲ ماه طول بکشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147752" target="_blank">📅 19:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147751">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDiw5QI9bTU6w2nu5JUNMaydNrxaCKMW0v13c-7OdKqZfgIV-5HmwzN06MeZZyArtXDAC481fZ09YOinnRxGynqqxZsqashSXuX_TiS1Z1sR1yM9qxzkEKexF4YsJZTCVHTG0rm95PK5VtAM_hvHEK0A4oy1fzCigZV-2amepLXFA7HXU187ayDbj_MiFtmW1QyJ7TFnvQIPeDKn5QV8A3u3pUOD_wCb_X1xn9JlMvYmpiu5eaRhoDbbPH3fht0kxFTQNZreML9qx0ACWjAWusHymfO59RIPuR5qT08RRR8erLch_3xeg2ja0geXGUOt-p9BaeCzx0PtDP5rxvr9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
۱ کیلو تخمه آفتابگردان شده ۱ میلیون و ۳۶۰ هزارتومن و به صورت قسطی هم میفروشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147751" target="_blank">📅 19:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147750">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
کریس رایت: خطوط لوله جدید جایگزین تنگه هرمز می‌شه
🔴
کریس رایت می‌گه خطوط لوله جدیدی دارن می‌سازن. این خطوط وابستگی انتقال نفت به تنگه هرمز رو کم می‌کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147750" target="_blank">📅 19:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147749">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIcGuuTrwxDyZ-gvsrMp42IOcEZ8sYVYkVJjx5L4-XQrz-_3cfOo43LCwHJJiSyO2E4le5gVE7ieksgFbOU98KEfr8CtfTz8qSQqOdq36PdrimQ4M0EL5-YOIiRBbFu2NbUnzlfcsmcR_wZc3XXe6CPVnQBo25X4T5twDxXRAccbdR2qChLqfzyOyG6tHGiHfSzNf9FZsOeWu7ybP2UkPKYqIdWakan8PmfTzCmpO3Vjmbn6H2CnH_tvFiwYlOWGoakrv3yhO-51VdaNCEu5VpV-C0qM1WO9HnUl4pu9vlZPBHs_hGK058OAjmoIn89KB_rIuwPlkbOWKkVNygkurw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل حملاتی هوایی را بر علیه منطقه المنصوری و همچنین منطقه‌ای بین شهر ارنون و روستای کفر تبنیت در جنوب لبنان انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/147749" target="_blank">📅 19:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147748">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNLa_VKsmAYTJvFOy2bWRtA45LA0jI691LTLMUUBdm27KC3ezqiyJAuOkYT0B6UZzzMaXGUWczGKnL6Mvg6EFRfJPfoAmJwjEZDFOSUkOOCOKIjo4rz5KuSXZ5UmpZcrj_zvA-JinZ4yqzOs5UmhTmY4OuSqBboe8zWFVCITKkPo1IqlnO9nJiY50oNxoODz96HZvWP4-x1aY-pBO3qHGRX1wSvtvFi2aQTf4TJqtJLTu0sZlr2eBeGKcw7ssoVFX95l4QQQqxSf9_pMD5eZOTn7GSBXB2TkYwwue6WfVmqpanftIavxK8WuEFWsO45u7Lk7KI28wF7jHivt0t2HZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد سامتینگ:
قانون استرایتس تیلور:
i = r* + π* + 1.5(π−π*) + 0.5(y−y*) + α(SOH−SOH*) + β(BEM−BEM*), α,β > 0
بیایید ببینیم آیا افزایش نرخ می‌تواند تنگه هرمز را باز کند یا حتی یک بشکه نفت تولید کند!
شما نمی‌توانید با افزایش 25 واحد پایه‌ای، یک گلوگاه را تحت تاثیر قرار دهید، و r* خنثی نیست. این، حق بیمه ریسک مربوط به تنگه هرمز است، و ما آن را تعیین می‌کنیم.
استوار بمانید! (به اصطلاح، سیاست پولی خود را ثابت نگه دارید!)
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147748" target="_blank">📅 19:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147747">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIZ4pv-m5oXu_8_vlzcrB73qTtbyd_MEzzigzChJdtExz6SAhJHP4gCdM0x9lsmdrev0O395t3sf_atUziqUlJun2rwNCJaBhwtdxi0ijDM1l9ZnpkwGtkT55jbdnZN_IUi0geY_EmhCiWIs-dygihVlXlSMYEVSfoCI6m68MTnuXo84McYgitZvdec9SxpFajohGJqSGdar9A3CA9YrhKZhY_CiehLCdP9-skaATeHYN6XiKX0WGR9amsgP3hE-rRtDDArf_QG4MH2C2SEfCrKKYajuqahdGQAyHi0wWpspOi-hPJ5cYafkfOly5oH06f_Fg-Zu6YSsw9XQ2gsrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر نیرو:
مردم عزیز مفتخرم اعلام کنم قطعی برق تمام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147747" target="_blank">📅 18:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147745">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3564566c9f.mp4?token=kOy-0Vq8zIpIWWXnjjl9cnO547lYKSHle4QruYlY8y2_vLqMqHxQ4yv-6CiuGC8QQFdPb5UVBrVbNrkRrIDLr_gcwPU1y8VFI48Q0VhbUYC4hsTK1xTRQ1AiuaQ-Gst402Ng3Zf9cFI9TAVqPFBcWrHeECk9d3ETVrqsbaN32DG71hIj8XOZpkB_qzJR0er8RK76mT7wlPPkrD-BoO_U4OUXbKAMLTfm6wfVUuDROEbVB1Ot3liaOnDctWX7jKCrGhz52cZhJEsFY9LdBqpHw6rlJ5H7MFP3OTtUMLTZ2ll31hrj1lxIapplA6TLLr-v0U0kq2_qrE-2XIKJm-auWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3564566c9f.mp4?token=kOy-0Vq8zIpIWWXnjjl9cnO547lYKSHle4QruYlY8y2_vLqMqHxQ4yv-6CiuGC8QQFdPb5UVBrVbNrkRrIDLr_gcwPU1y8VFI48Q0VhbUYC4hsTK1xTRQ1AiuaQ-Gst402Ng3Zf9cFI9TAVqPFBcWrHeECk9d3ETVrqsbaN32DG71hIj8XOZpkB_qzJR0er8RK76mT7wlPPkrD-BoO_U4OUXbKAMLTfm6wfVUuDROEbVB1Ot3liaOnDctWX7jKCrGhz52cZhJEsFY9LdBqpHw6rlJ5H7MFP3OTtUMLTZ2ll31hrj1lxIapplA6TLLr-v0U0kq2_qrE-2XIKJm-auWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی ایالات متحده:
دیروز حدود ۱۸ میلیون بشکه [از طریق تنگه هرمز] خارج شد، که عملاً به سطح پیش از درگیری بازگشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147745" target="_blank">📅 18:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147744">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27adce909.mp4?token=VESmLcAabX2l-6MVSWC5Uo5k7j8aQFPcc3bVjsCvBsvYsHDHX3WVEgg31lj12_JasCu67PZRh3p7cxKnyg6dV9GwpB3dhbzTfRCECuG8LeaG4sF5a70epXxwAwu2yvGZ4OGi6O3G0-RsZnQhHf6nngZm7thflaCyuF94BqlXaMprmObWio-odhpa2GwQgk_Kw4KxREHTJkQIIvZv1ErxldqQEJkc9XvQBNbNHgz3iShoI2-I3ck_PZT-G34ByprKi9-q_3UGTI-3G-ALpxz6mxRYknumx5mV5d62Stf7W5FfvM6BqL38hMGNZJmsK00gYiKQ274ZMQg2ukAKRC5CHYd6B11GY6r59XGGNiBtAtXLrpMhOEtoob81NM454N_X_jO7QDaZFI7ET9vnPVTNVtvCUgomn28f54nK6-1Hgby1_TCpR3tCI8_oEuFnDOnTxSj9MFKffcvOOhKM_mdUMPVri0N2Cd5NYBKin1cz5aUifazyj5w1nv5SKryo9r9TbeZFezO3V5VnoSrpWcEgZKC_yZSUcwgXM_JB5iiEQHJKP9XDt97MA8G2m4S6Im9IBkKWZUjjfl8fu_Q2De2Hpm_mIXNwaza6MQLegLALCDyVF1Mofo-cchhFkY29c5Ucc6mu9Y9hyD6Hx8Zpui9texQbwD3fnQy531AJswqFhmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27adce909.mp4?token=VESmLcAabX2l-6MVSWC5Uo5k7j8aQFPcc3bVjsCvBsvYsHDHX3WVEgg31lj12_JasCu67PZRh3p7cxKnyg6dV9GwpB3dhbzTfRCECuG8LeaG4sF5a70epXxwAwu2yvGZ4OGi6O3G0-RsZnQhHf6nngZm7thflaCyuF94BqlXaMprmObWio-odhpa2GwQgk_Kw4KxREHTJkQIIvZv1ErxldqQEJkc9XvQBNbNHgz3iShoI2-I3ck_PZT-G34ByprKi9-q_3UGTI-3G-ALpxz6mxRYknumx5mV5d62Stf7W5FfvM6BqL38hMGNZJmsK00gYiKQ274ZMQg2ukAKRC5CHYd6B11GY6r59XGGNiBtAtXLrpMhOEtoob81NM454N_X_jO7QDaZFI7ET9vnPVTNVtvCUgomn28f54nK6-1Hgby1_TCpR3tCI8_oEuFnDOnTxSj9MFKffcvOOhKM_mdUMPVri0N2Cd5NYBKin1cz5aUifazyj5w1nv5SKryo9r9TbeZFezO3V5VnoSrpWcEgZKC_yZSUcwgXM_JB5iiEQHJKP9XDt97MA8G2m4S6Im9IBkKWZUjjfl8fu_Q2De2Hpm_mIXNwaza6MQLegLALCDyVF1Mofo-cchhFkY29c5Ucc6mu9Y9hyD6Hx8Zpui9texQbwD3fnQy531AJswqFhmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی ایالات متحده، کریس رایت:
خدا را شکر که پرزیدنت ترامپ در مسائل مربوط به انرژی، دیدگاه‌های منطقی و معقولی دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147744" target="_blank">📅 18:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147743">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2394ff45bb.mp4?token=TsWcwR46Rn_xHnMhv9dvbL_GVmxiD7PSAa7y_e8SWeWIS8vVd_QLZKd3aMLRXkXJM6nSQAFoGzEV_zxB3Xss4oKp34EWNZOGCm6OmAFAwrZXtQRNwqmsF7uBDh5Q3z04iu1tr5h5iVOTVZY-_CEl3DTgVfXRH5vVjIJzj-Le0dHhn-n1oVHQq3wEv2_RpolHXaVhXd3kkZINDAQFMSNiZqmV92BZDk_JViN5wi-u63k7oUMUhLj_Kveajm-7OaqSEUr3sCKDNu4PFKTFJKJXeVgsebn-6hIC94CVGECzchQEXLJ1NBVtim5diGGqQVYZBvCMuL6hVAiw3yvLjpAzyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2394ff45bb.mp4?token=TsWcwR46Rn_xHnMhv9dvbL_GVmxiD7PSAa7y_e8SWeWIS8vVd_QLZKd3aMLRXkXJM6nSQAFoGzEV_zxB3Xss4oKp34EWNZOGCm6OmAFAwrZXtQRNwqmsF7uBDh5Q3z04iu1tr5h5iVOTVZY-_CEl3DTgVfXRH5vVjIJzj-Le0dHhn-n1oVHQq3wEv2_RpolHXaVhXd3kkZINDAQFMSNiZqmV92BZDk_JViN5wi-u63k7oUMUhLj_Kveajm-7OaqSEUr3sCKDNu4PFKTFJKJXeVgsebn-6hIC94CVGECzchQEXLJ1NBVtim5diGGqQVYZBvCMuL6hVAiw3yvLjpAzyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری
: آیا شجاعت کافی دارید تا زمانی را تعیین کنید که قیمت‌های انرژی کاهش می‌یابند؟
🔴
کریس رایت
،
وزیر انرژی
: من قطعاً نمی‌توانم رفتار و اخلاق مقامات ایرانی را پیش‌بینی کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147743" target="_blank">📅 18:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147742">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
همزمان با سالگرد زنده یاد مهسا امینی، فضای اکثر نقاط کشور امنیتی شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147742" target="_blank">📅 18:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147741">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NZ0IEMES2ksO0j-wp-FFQXSEhqwBHknTGyR3xU0g8HxZh3MJ4s_KI1uxilWGA3tTFYm3iijUggu9zZw3tjHhIpG5pH6yrZt1b07-fM70ULcsiCTWGIKTr9zcnwrhlrHMvC3LYDs4fT0bg3Gx907pyfihxveeqzAhNcUEG1w1P-_RJrbrTs9FZ8RF8y4GqSvZVcWfr7EKij0rM8mGK0i3-cw4N7GADPYU4VYBO05Qa0flNMrN6NkZ_pg224slXVQuArqujeVvIZFGDqM7diAnvtdm6GVVL-iZg9HIhlD3roX1QQ0cxNxZtMvsF3fOklBMQpbU22D87zjiuDZ4hPbbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حوثی‌ها قطعات جنگنده اف ۱۵ عربستانی رو تو فرغون ریختن و بردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147741" target="_blank">📅 18:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147740">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نتانیاهو: ما با یک حمله جهانی علیه دولت اسرائیل و نیروهای دفاعی اسرائیل مواجه هستیم.
🔴
در این حمله، دولت اسرائیل و سربازان اسرائیل نه‌تنها به‌عنوان مرتکبان جنایات جنگی — که بزرگ‌ترین حماقت قابل تصور درباره منصف‌ترین ارتش جهان است — بلکه به‌عنوان آزاردهندگان اقلیت‌ها نیز تصویر می‌شوند.
🔴
دولت اسرائیل مانند جزیره‌ای از پیشرفت، جزیره‌ای از تحمل و جزیره‌ای از امنیت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147740" target="_blank">📅 18:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147739">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070959ba10.mp4?token=OqFCD1KRQWfKZRJxP053mKSduR6Itx_1umtRo0coxCWMDN06q0z6-LF2D0rE85f35-JsKjTqDkjD68L5VbBx1nuBfCrqUx-DAFJtJnsRc82fKXPCZC96AU4hh-WP8j1oiwcxtk19CAOcCcNxqZBwhSPN47bmEtGX5gze8opTXLzJkRlsZu8d8m4wFxAVS9aXYTnigjaL-sP5Ad-akWfKtkDo4Avg6BTbraohDqh2OcUTZnEtPecsYDmv2yU-_Up63nCA4EAskLB2AdrqkldLSLHePwnz5IDmc5d8NBy_h-zjtOtfyATgC3_5KYRubMIn0qhKzHRjX7Ju0INA7cMMUZMs9tEDaOsruY08q-7qIKEO0wPVSfQsCPKLKm8OkFihHiVzsCrihJkxyNso3Ixu1zBUtSXwEelo40Ef8XbpJC1dZ9l0-Er6ukm9zjVicY56TU_yD5O6LMzxPVSyPEFMqiDuWU5fpLYtsN7timFFkbzguFEzqktaV7-nP0tG8zpb0nOxLaWixzNkDgshohLYJIekm9x7naMIo06JBJ_ZeLKZRnuEiOTDmFSGbznwySM4wNO-nEo8j01wqlVU0DWsO58batSDs8lpduoiLLHwhTgeSSc6QETiwPgKy1x2vdmeR4bLxlOtcvQbFTaKHj7XrWaIhwWxLT2gIyxLuRjRyA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070959ba10.mp4?token=OqFCD1KRQWfKZRJxP053mKSduR6Itx_1umtRo0coxCWMDN06q0z6-LF2D0rE85f35-JsKjTqDkjD68L5VbBx1nuBfCrqUx-DAFJtJnsRc82fKXPCZC96AU4hh-WP8j1oiwcxtk19CAOcCcNxqZBwhSPN47bmEtGX5gze8opTXLzJkRlsZu8d8m4wFxAVS9aXYTnigjaL-sP5Ad-akWfKtkDo4Avg6BTbraohDqh2OcUTZnEtPecsYDmv2yU-_Up63nCA4EAskLB2AdrqkldLSLHePwnz5IDmc5d8NBy_h-zjtOtfyATgC3_5KYRubMIn0qhKzHRjX7Ju0INA7cMMUZMs9tEDaOsruY08q-7qIKEO0wPVSfQsCPKLKm8OkFihHiVzsCrihJkxyNso3Ixu1zBUtSXwEelo40Ef8XbpJC1dZ9l0-Er6ukm9zjVicY56TU_yD5O6LMzxPVSyPEFMqiDuWU5fpLYtsN7timFFkbzguFEzqktaV7-nP0tG8zpb0nOxLaWixzNkDgshohLYJIekm9x7naMIo06JBJ_ZeLKZRnuEiOTDmFSGbznwySM4wNO-nEo8j01wqlVU0DWsO58batSDs8lpduoiLLHwhTgeSSc6QETiwPgKy1x2vdmeR4bLxlOtcvQbFTaKHj7XrWaIhwWxLT2gIyxLuRjRyA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشته‌شدنِ دو نفر به خاطر یه آینه بغل !
🔴
یه جوونی با ماشین داشته تو خیابون میرفته که با یه موتوری درگیر میشه و موتور سوار میزنه آینه بغل ماشین رو میشکونه؛
🔴
راننده ماشین هم میفته دانبال موتور سوار و میزنتش زمین که متاسفانه راننده موتور فوت میکنه و امروز هم حکم قصاص راننده ماشین اجرا و اعدام میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147739" target="_blank">📅 18:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147738">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
جروزالم پست اسرائیل: عبدالملک الحوثی، فرمانده حوثی‌ها، بزرگترین پیروزی نظامی خود را در سال‌های اخیر به دست آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147738" target="_blank">📅 18:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147737">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFQeiXZQP-G6ovxfD5vVmkH0ARAYSi7qse_2W624T-icpf19XvRzGVWKSwwpalWwSkLP4fv0wJ39fwvL6DcoaCDxNwYJuK1Po1udJ5VCKNwLO2KPrCSi5tMvmqRJrFcG5Q7fYyGBCe174efd02FQdbJyHCJz8l0JnUma0oE0Ws3AacVefc4dTkpCOGTBKnkQ7ZBbvylhSW4fSu-kJ7IkE3jg0Vh-DJg3FoeB6BuXARsYBO_ZvTX8_hc4ylpJIT9Cjx15I3tgeJd_xa9QRzLB2Js-nKWSp6ko2LPVviewOFg5_QcIcZY5KrmQsU0S63EEorGMyR_XMIsLoCJi7Y2sfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حوثی های یمن تصویر سرنگون شدن جنگنده F-15 عربستان سعودی را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147737" target="_blank">📅 17:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147736">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نیویورک‌تایمز: تصویب فروش ۲.۸ میلیارد دلاری بمب‌های سنگین، می‌تواند یکی از بزرگ‌ترین محموله‌های تسلیحاتی آمریکا برای اسرائیل باشد
🔴
این قرارداد پیشنهادی شامل ۴۰ هزار بمب یک‌تنی خواهد بود؛ تسلیحاتی که استفاده از آن‌ها در غزه و لبنان به دلیل آسیب‌هایی که به غیر نظامیان وارد می‌کند، با انتقاد بین‌المللی مواجه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147736" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147735">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147735" target="_blank">📅 17:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147734">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فاکس‌نیوز به نقل از وزیر انرژی آمریکا: روز گذشته (سه‌شنبه)، ۱۸ میلیون بشکه نفت از خلیج فارس جریان یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147734" target="_blank">📅 17:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147733">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
روسیه: هر آنچه از آمریکا شنیده می‌شود را با نهایت جدیت دنبال می‌کنیم
🔴
در حال حاضر هیچ گفت‌وگویی درباره «ثبات راهبردی» بین مسکو و واشنگتن وجود ندارد
🔴
هنوز فرصت برای جلوگیری از رقابت تسلیحاتی در فضا از دست نرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147733" target="_blank">📅 17:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147732">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXtdLovYrzFFRmmqqXr93k2dzQ0VzF5BGteWG_30ZSUCha_P2lHldTv2LHe2BYVJL4bRqK3LXZmqhfyv1-vdlsA54Jh86v0sHxpqdYXjySnPWAF6zPa8Y2i8ffLmBsaa5j0sJwUPOYwFveYcxmVnxjCuc2nzHu14rLeN7__x0--Tg1Ravkb-Hs0gBPh1ZZnsZbgRshxucpUk4k0tvX0DzF9fZdijGinZ8FFt2FJ1wIPLaDSPex8N_DkoMetb8V2YdW_6FI6oXnWXbcbGhPBT3rsEEwWLmss0d7lkKVNNtdQ6GDwaJfDCTOZZZWK5s0myCpge2yUECQe4hqXZmtps2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقامات سعودی به شبکه ۱۲ اسرائیل گفتند که ریاض به طور فزاینده‌ای از عملکرد دولت ترامپ به دلیل عدم اقدام قاطعانه آمریکا علیه حوثی‌ها (انصارالله) ناراضی است.
🔴
یک منبع سعودی نزدیک به خانواده سلطنتی گفت که حوثی‌ها از عدم اتخاذ "تصمیم عملی" توسط واشنگتن سوءاستفاده می‌کنند و این امر باعث می‌شود که عربستان سعودی "هزینه آن را در عمل بپردازد".
🔴
یک مقام سعودی دیگر نیز با ابراز خشم از عدم حمایت منطقه‌ای، گفت: "از پاکستان یا ترکیه چیزی جز بیانیه‌ها به دست نیامده است" و افزود که ریاض احساس می‌کند رها شده است، در حالی که در حال بررسی یک استراتژی جدید برای تأمین امنیت دریای سرخ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147732" target="_blank">📅 17:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147731">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
مجله تایم: جنگ ۵ هفته‌ای ترامپ، هفت‌ماهه شد؛ اهرم ایران از هرمز به باب‌المندب رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147731" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147730">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbca1430d1.mp4?token=ppG3gOrCD3XIfowrBeXhjdrmfLcDIipYK3H8VHKRd78g7s96lHYkhFswkJWMdDm8vHyO7hC_FtHL-M3OeZa7aOwtEhd9QkaJ4NHxGQQ5RJStN-CPM_DyAPvbW0XfcsucsMpzcSUf8YNjEPT7SWeoiuyGe_vjgFVtAJkhE2XR5Qmrm8Z0XjmsOb5_Id5dN4ZY7Jb8Qc4OPC16BAN9fO3lZSz_CVU4XAoVltKDFiQgCUgeQgT1q9eTdRWaBoMdHSBtsF51PqYH-INbYdkN1OhG587s3rCA4jrE0i1EqeB0NygkWZeU-XVLivWx_5srkl7VvOCw6uLckmcZWa5u8U4_Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbca1430d1.mp4?token=ppG3gOrCD3XIfowrBeXhjdrmfLcDIipYK3H8VHKRd78g7s96lHYkhFswkJWMdDm8vHyO7hC_FtHL-M3OeZa7aOwtEhd9QkaJ4NHxGQQ5RJStN-CPM_DyAPvbW0XfcsucsMpzcSUf8YNjEPT7SWeoiuyGe_vjgFVtAJkhE2XR5Qmrm8Z0XjmsOb5_Id5dN4ZY7Jb8Qc4OPC16BAN9fO3lZSz_CVU4XAoVltKDFiQgCUgeQgT1q9eTdRWaBoMdHSBtsF51PqYH-INbYdkN1OhG587s3rCA4jrE0i1EqeB0NygkWZeU-XVLivWx_5srkl7VvOCw6uLckmcZWa5u8U4_Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک توپخانه ارتش اسرائیل (IDF) به مناطق المنصوری و بیت یحون در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147730" target="_blank">📅 17:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147729">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سوئد کارمند سفارت ایران را اخراج و سفیر را احضار کرد
🔴
سوئد روز چهارشنبه در راستای اعلام حمایت خود از اسرائیل، یکی از کارمندان سفارت ایران در استکهلم را اخراج کرده و سفیر ایران را نیز به وزارت خارجه احضار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147729" target="_blank">📅 17:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147728">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رویترز به نقل از منابع آگاه: عربستان پس از آنکه حملات پهپادی به خط لوله نفتی مهم این کشور آسیب وارد کرد، عرضه محموله‌های نفت خام برای پالایشگاه‌های آسیایی را از طریق انتقال کشتی به کشتی در نزدیکی عمان افزایش داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147728" target="_blank">📅 17:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147727">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
حوثی های یمن: اخبار منتشر شده در خصوص حمله به جده و مکه را قویا تکذیب می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147727" target="_blank">📅 17:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147726">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فاکس نیوز: در اوایل این هفته، یک کشتی آمریکایی با حداقل چهار پهپاد و یک موشک از سوی ایران مورد حمله قرار گرفت. چندین پرسنل آمریکایی در این کشتی حضور داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147726" target="_blank">📅 16:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147725">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUBo-tVOkxro3NbrjhEWQhl8wD1LmqA-K8Y5RPgkrKBc9GeKrHY-bRU-ju3YjPEJS1-AZigtcWb3wvFq_U3wuPditMTwdNCUPvZJYR6ogk1IbUqEHO0vcsids-f9kPrj2lr3d_PWzBgH6COeE3rF2ul841FK9TzpFcDyz7Ep6BhkwWY-6iZObmjkCBM5INcI_53j2Scxwu8Nk3aE7nz82Rucj-gD9SHBr0o3KbKflcN5hlerk77o_VDCcDGDiK058ahADA4-3cdbiiXuEysGPJd4e5oBhrp_ornQsqWyp0Rv1VVkadtSqO72QY-_C2mWcxEYb9t2KCRpkdwbMBY4lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز: در اوایل این هفته، یک کشتی آمریکایی با حداقل چهار پهپاد و یک موشک از سوی ایران مورد حمله قرار گرفت. چندین پرسنل آمریکایی در این کشتی حضور داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147725" target="_blank">📅 16:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147724">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwRDgPacSMG-kh0F2jwcV6LjVmIuBG6Dbvx4DfSz-uRgbVSOgdL7zCAVi4vf9rqPPgJBsQjVD7kqBW8los9IR3Z9Z4vRJX5VLa32Daid7zn77PHdXMkaye0WSUzDbAxAmxKSPLgCdViZ6YMVwDcv5BBqBBj-pFTJLhwKbv6pViVfw3l-K70m7ReBkPW1V6j_cowMR3qIb79h32irxs5gjmWgc21aqhfjsMzOqV2yXZdH2Dred53daLyGSaFSY1X1UudoROsf1bGvOT-xJL5ton3yYiC_aj9958n-MGsbLFkXwQyG2LHvjVOgbC4GjCVt2lB57OPj19sFiqwiI4BcLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
فعالیت گسترده نیروی هوایی آمریکا بین پایگاه‌های این کشور در اروپا و خاورمیانه و ارسال و جابه‌جایی تجهیزات
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147724" target="_blank">📅 16:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147723">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به نظرتون کدوم بیشتر رشد میکنه؟</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/147723" target="_blank">📅 16:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147722">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bc6d9887.mp4?token=CJQMwGclHBiL__TyUz1lc7nzCW4RaUsyxf-gliPodcqImsYs7pS4yi1LJrGBUnr-QuRu60wF_HhawhruSPAq5zS2HQdgspyvoajAIbBI1NDiwp8QnbqAa0gbi7ajkT7muHgtIp7nxEK8ygPOVFC7MpGiTw7rrin8_npsHUHMOQTguZThI1hVrhhHLA_QwOjvIxWekMRKiwdU0KTiLj1FbQSGX3NRqohuwfL4z5d5-TLhWHv9gryg53OtSBbzkFR7F_K_Iy78vAQF5P3tyTXDhrLBkjxxTgGrZQZa3n0ngPQ2G7YjRm33Uv4TuAOqdEOflkzv7rR95osVVO1gLTXiWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bc6d9887.mp4?token=CJQMwGclHBiL__TyUz1lc7nzCW4RaUsyxf-gliPodcqImsYs7pS4yi1LJrGBUnr-QuRu60wF_HhawhruSPAq5zS2HQdgspyvoajAIbBI1NDiwp8QnbqAa0gbi7ajkT7muHgtIp7nxEK8ygPOVFC7MpGiTw7rrin8_npsHUHMOQTguZThI1hVrhhHLA_QwOjvIxWekMRKiwdU0KTiLj1FbQSGX3NRqohuwfL4z5d5-TLhWHv9gryg53OtSBbzkFR7F_K_Iy78vAQF5P3tyTXDhrLBkjxxTgGrZQZa3n0ngPQ2G7YjRm33Uv4TuAOqdEOflkzv7rR95osVVO1gLTXiWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو تهران دوتا دختر با موتورشون چند ساعت پشت یه ماشین تو ترافیک گیر کرده بودن؛
بعد دیگه خسته میشن، میان پایین و می‌بینن اصلا ماشینه راننده نداره و طرف پارک کرده رفته...
[
@AloTweet
]|</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147722" target="_blank">📅 16:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147721">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بازیگر ایرانی معروف هالیوود و برنده خرس نقره‌ای: ایرانی با پرچم اسرائیل بیناموسه!
🔴
گویا وی هم قراره به ایران بیاد و به صداسیما دعوت بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147721" target="_blank">📅 16:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147720">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b8ab3224c.mp4?token=QvwtmTXuTyg3AwbMw6Jyt42TJ06LBNO2Ke8bFANAkZh06VJJPKfSQ1UQa8UFm1d2m6eD9TAGzz9G5TibfUznis3Tor7KG1BlPmPSASf0sG5usOaf_zC8WGwnJU940vJ60WKNvMRwlR7mhJvlxZDMq_6JcuWotD5ZL-BxifWn4bCfjuqDHyJJThUWb7oZ5izDTrngeE1Nc0T0rd07746DW7IvO9r8ojXDZHFQDXmD5vW1yyW7W_tlB4gQVnKpmkX9KC4_FTA4ixkM01XJwAs53i9QmCnM4XvbrT-RJA26MI2w23ujjn_r05sXl91FpN6Tc6QrPy4vKEVZ8ygnFBHkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b8ab3224c.mp4?token=QvwtmTXuTyg3AwbMw6Jyt42TJ06LBNO2Ke8bFANAkZh06VJJPKfSQ1UQa8UFm1d2m6eD9TAGzz9G5TibfUznis3Tor7KG1BlPmPSASf0sG5usOaf_zC8WGwnJU940vJ60WKNvMRwlR7mhJvlxZDMq_6JcuWotD5ZL-BxifWn4bCfjuqDHyJJThUWb7oZ5izDTrngeE1Nc0T0rd07746DW7IvO9r8ojXDZHFQDXmD5vW1yyW7W_tlB4gQVnKpmkX9KC4_FTA4ixkM01XJwAs53i9QmCnM4XvbrT-RJA26MI2w23ujjn_r05sXl91FpN6Tc6QrPy4vKEVZ8ygnFBHkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بازیگر ایرانی معروف هالیوود و برنده خرس نقره‌ای: ایرانی با پرچم اسرائیل بیناموسه!
🔴
گویا وی هم قراره به ایران بیاد و به صداسیما دعوت بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147720" target="_blank">📅 16:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147719">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
بلومبرگ: پالایشگران ژاپنی پس از تعطیلی خط لوله نفت عربستان، خرید نفت از خاورمیانه را افزایش داده‌اند
🔴
آن‌ها اخیراً نفت خام عمان را خریداری کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147719" target="_blank">📅 16:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147718">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
تعلیق پروازهای ماهان به استانبول، آنکارا و مسقط
🔴
هواپیمایی ماهان پروازهای بین‌المللی خود در مسیرهای ترکیه و عمان را تا اطلاع ثانوی متوقف می‌کند
🔴
بر اساس بخشنامه‌های ابلاغ‌شده، پرواز تهران–مسقط از ۲۶ شهریور و پروازهای تهران–استانبول و تهران–آنکارا از ۳۰ شهریور لغو خواهند شد
🔴
اطلاعیه این تغییرات به دفاتر خدمات مسافرت هوایی ارسال شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147718" target="_blank">📅 16:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147717">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3ece0c92.mp4?token=rCl5sm9rN65f3huN_gw3z_MbwbJWNmk3HJ_pkrahikCM95mI8mZddbXFXKsIpfeA9RwaO3nsvSTO2z3hyc3w09jwcgLGB8jXdMrX_bXQ65L-6ld0VuuOaljZvX88xN8xEbmZnVlWu7tUBQfLpPKJH7DBIFBaX0Cp2yAmJZiMzzdeXWc-kBLNQA4EuQgiN_FzAwfTOU5dkbnCHF6Ks20hmze1s5XYZwPwCfCukUEv74IEAb7IKh6QriFpIKxcBems53hkXqCKNK8P54m00kgMAXBCYhwNtTXz58Un_X8CUinPn1Z9kmLEVJgepPwXfeECbvdRm1lIOqa9c08k9wG-_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3ece0c92.mp4?token=rCl5sm9rN65f3huN_gw3z_MbwbJWNmk3HJ_pkrahikCM95mI8mZddbXFXKsIpfeA9RwaO3nsvSTO2z3hyc3w09jwcgLGB8jXdMrX_bXQ65L-6ld0VuuOaljZvX88xN8xEbmZnVlWu7tUBQfLpPKJH7DBIFBaX0Cp2yAmJZiMzzdeXWc-kBLNQA4EuQgiN_FzAwfTOU5dkbnCHF6Ks20hmze1s5XYZwPwCfCukUEv74IEAb7IKh6QriFpIKxcBems53hkXqCKNK8P54m00kgMAXBCYhwNtTXz58Un_X8CUinPn1Z9kmLEVJgepPwXfeECbvdRm1lIOqa9c08k9wG-_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرقت گوشی دختر جوان در اسلامشهر در کسری از ثانیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147717" target="_blank">📅 16:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147716">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
اورزولا فن در لاین، رئیس کمیسیون اروپا روز چهارشنبه احتمال تبدیل شدن کانادا به نخستین «عضو وابسته» اتحادیه اروپا را مطرح کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147716" target="_blank">📅 16:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147715">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رسانه عبری: بن سلمان خود را در برابر حملات انصارالله تنها می‌بیند؛ در حالی که تأسیسات انرژی عربستان هر روز منفجر می‌شوند، آمریکا و اروپا هیچ کمکی نمی‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147715" target="_blank">📅 15:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147713">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFioCslQi50x6YdTf2ym8tt36zkh4h3nO0DUwH-4F9jOpG6DMUEOS7f_cUReOY0gHHsy_7YaaCObiniFJhqPv2jR2R2KaCipg-WNrmmrvSIblsh82EyyO-2ALIHc9N83WCAWI2kfxiTV2VMKufp1EqJsuPvcJE93UlCZ0WcF09uNET8Ib3hG2E_ghRHdDvMsKRfMXDVFdY7MRppC9S1ZGzJlA7HVt2sYEYaH9uKVSDNl3QERtoP1IDoIGC6afq5rmqvmiAU4UeP1BWdw6nX8pVGZfurV3clzn5mCc8jZRx0XF51Nl2FvRIvQYuZryRFE5zZk3clazNSfLhT03w_uTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f303351168.mp4?token=tcUCx4-duLTG9zzlM3sE_rCHHfXmnUp84lNytOzMvsZQ2l_-cHxYnF-tekOD7sgKv2JiHkQk4pmk2kwzvdGMlUUdqznbAEXCHkFR-xpBwnVpiRS3mOaJMRZdaSLL27Li1tCkqY2nBM0NmValjpRTTXe77G_t0YqoMJtQfdzMz3a81aV7KUUYP30knInjWKBe4nQxJKFz17EvdxwhSJ4OZl6LS4AZKDxzKRixO418Rvq8xVtdLuIGEAslBMZb8_IWz99WUv-dHEnAVxvcNnmgJ1qElTD-nfKALvdlNgOz8PqhLmwGCQX747RmX1q16k2C3kMZv6Z-MSgNzvdoARj7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f303351168.mp4?token=tcUCx4-duLTG9zzlM3sE_rCHHfXmnUp84lNytOzMvsZQ2l_-cHxYnF-tekOD7sgKv2JiHkQk4pmk2kwzvdGMlUUdqznbAEXCHkFR-xpBwnVpiRS3mOaJMRZdaSLL27Li1tCkqY2nBM0NmValjpRTTXe77G_t0YqoMJtQfdzMz3a81aV7KUUYP30knInjWKBe4nQxJKFz17EvdxwhSJ4OZl6LS4AZKDxzKRixO418Rvq8xVtdLuIGEAslBMZb8_IWz99WUv-dHEnAVxvcNnmgJ1qElTD-nfKALvdlNgOz8PqhLmwGCQX747RmX1q16k2C3kMZv6Z-MSgNzvdoARj7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آنتون گرویس، ژنرال ارشد روسی و فرمانده تیپ زرهی چهارم، در پی یک عملیات پهپادی که توسط نیروهای سامانه‌های بدون سرنشین اوکراینی (SBS) در منطقه دونتسک انجام شد، کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147713" target="_blank">📅 15:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147712">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
دولت گرجستان در پی اجرای تحریم‌های جدید آمریکا علیه شرکت‌های هواپیمایی ایرانی، ورود پروازهای تمامی شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه ۳۰ شهریور (۲۱ سپتامبر) متوقف خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147712" target="_blank">📅 15:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147711">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بابک زنجانی: به‌ مردم ماشین برقی رایگان بدید تا بنزین صرفه جویی شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147711" target="_blank">📅 15:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147710">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رئیس کمیسیون انرژی: در پاییز و زمستان امسال به دلیل کمبود شدید گاز احتمال قطع گاز خانگی در برخی استان ها وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147710" target="_blank">📅 15:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147709">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chlcHqCeVD-FwJtWkSsi-m2tn5pmGudG8d5-Zhg4BwfeZLpjQjK7CBLeaq-WafIXJjls5FVe249qLsn21_yTKgaMXjt7odt4f2hDjqDpO3RdHJ_DQEfh0BMcc4ItwASsrfur3wpi6uE7vy5Pia03MwWgGwZbIsmjM0WlejTlKsMdz_S4XgDYGiXi4-SAsbEoAbJ-3P5r1k1lRjdVQxz4Ki_wkAa92A7I1FM-Addnz0p2R0AsTdQkHkSD9tsm1KsXeSOIsl2wdYKL20aSzQqpzNUg9d-C46SLoGOwbIDbGTUZzVj2ANq8Q_Ms9CuGq08LnhY4AbAOLSR1DEAS6oFRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرگئی لاوروف، وزیر امور خارجه روسیه، گفته است که اگر ایالات متحده از توافق‌های «آنجاکج» عقب‌نشینی نمی‌کرد و اروپا نیز این کشور را از آن توافق‌ها «دور نمی‌کرد»، «ما اکنون یک سال است که بدون جنگ زندگی می‌کردیم»
🔴
او این موضوع را «یک واقعیت آشکار» خواند و گفت: «نتیجه‌گیری خود را بگیرید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147709" target="_blank">📅 15:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147708">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/862138e439.mp4?token=UhGYX3WLyG33MXwTia-6QOiwtRp7cf5kodS_RxqxEb0v3tLKmuhlz1JuvKJFtDZPOMtZjcr5V_x4Sy_VrRnZ9Za8dUK2uqcUqrUsJsT4D_0XdkUUkP0W9jkbC4EWsNF1hzzvam5cFbI5RqUPiC0LJkGZRo6jaNjaf8DcfU72hx3TWgmrpLe9OQFcUZ8fkHfihjohoKcRB9oJAxGq89UVGhfqGxIgdhjRfTa1kDb3ruH1mxY8eVa0SM4LYXBhbPiTsFAOLFrcGm3Rosbs3Bh6A7QQCMMK5BmO0oT6n0AmUOxn4uGzmz5OciPktHB79zC625YA6oC2Hl7DOEPLYemgBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/862138e439.mp4?token=UhGYX3WLyG33MXwTia-6QOiwtRp7cf5kodS_RxqxEb0v3tLKmuhlz1JuvKJFtDZPOMtZjcr5V_x4Sy_VrRnZ9Za8dUK2uqcUqrUsJsT4D_0XdkUUkP0W9jkbC4EWsNF1hzzvam5cFbI5RqUPiC0LJkGZRo6jaNjaf8DcfU72hx3TWgmrpLe9OQFcUZ8fkHfihjohoKcRB9oJAxGq89UVGhfqGxIgdhjRfTa1kDb3ruH1mxY8eVa0SM4LYXBhbPiTsFAOLFrcGm3Rosbs3Bh6A7QQCMMK5BmO0oT6n0AmUOxn4uGzmz5OciPktHB79zC625YA6oC2Hl7DOEPLYemgBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه آخوند: تجاوز رو آزاد کنین!
چرا دخترا با هر پوششی میتونن بیان بیرون؟ پس باید برای آقایون هم آزادی باشه و اگه دلشون خواست به دخترا تعرض کنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147708" target="_blank">📅 15:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147707">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
روسیه: امارات و ایران به لطف قدرت بریکس، موفق به غلبه بر اختلافات خود شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147707" target="_blank">📅 15:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147706">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حوثی‌های یمن: تاسیسات آرامکو در ینبع و یک پایگاه هوایی در خمیس مشیط عربستان سعودی رو هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147706" target="_blank">📅 15:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147705">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
اتفاق وحشتناک برای طلا
‼️
‼️
👇
👇
👇
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147705" target="_blank">📅 15:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147704">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75f7c18dc4.mp4?token=X6gPDh9imkGE83tNnqC2tz6qlmZ1f-NRKH-t2ovBVumuwIQkt41dlnsv7UkOJg53rr_OvkMLWLE0yRYmSG3OccBrcChgMF-Xb5q589Yy4uPzDzx71W9aHPydT3h_-JgaITdXihHCdtprXBeRibTJs6T5HSfSOWTTH7E4tv596GgbwTXceP1aaB5VYGhXeGHQZ9zvTdqmIpIBsGCDNqYfK9lH7VMgLwdDbAvpiMAhklKVTX0fY0R9XrptCBbAximK--H-KGbgQ7BTWG1yZIT5XDepxnuGMbsNuovtmYTJXZhlkKUo-Qje7KgXyqlsm-2yJhC3AlzDTZ3Yr_7G97kIGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75f7c18dc4.mp4?token=X6gPDh9imkGE83tNnqC2tz6qlmZ1f-NRKH-t2ovBVumuwIQkt41dlnsv7UkOJg53rr_OvkMLWLE0yRYmSG3OccBrcChgMF-Xb5q589Yy4uPzDzx71W9aHPydT3h_-JgaITdXihHCdtprXBeRibTJs6T5HSfSOWTTH7E4tv596GgbwTXceP1aaB5VYGhXeGHQZ9zvTdqmIpIBsGCDNqYfK9lH7VMgLwdDbAvpiMAhklKVTX0fY0R9XrptCBbAximK--H-KGbgQ7BTWG1yZIT5XDepxnuGMbsNuovtmYTJXZhlkKUo-Qje7KgXyqlsm-2yJhC3AlzDTZ3Yr_7G97kIGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جلسه  شورای امنیت درباره تنگه باب‌المندب
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147704" target="_blank">📅 15:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147703">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68da57faf0.mp4?token=KD3L_7A-z4xF2nJOMD03u97HRe5o6M8UNfP1y21KIFUe1BPXXp24DMsu9x6czrO3dfXrs5cI6RWGrK7nAnvdAmvElb1B75ru5_zBOZVxK2km9YUpE5MK86C_Ps8_TTgVAugYDdv7P7iTE0HI7Tn_Ne0tlmisNPXZTM32TiXVaNrGntbWe9K5xxf4uryqTASMmFIbFqi6puugc_MeHJ3D2m9vTJrLovgcagu5SodZ0cievg4GKkbJQyFld57oDBPLaB6ZwC56mgX6SyWqagxLEbLg3nA0ebjegIGA2lj-OP37TN9qnIrSqWjfstufbs0RJgH8jZVWsVM0eKFGJ8OE_JJxJXdqXl77Svu-45AEafhx5Cg-rc7XhMVAyRB74W77XH7cHTE_Of8H5zJ0tMBTFp2e5a30cPS4PgyWcDlWrCamYTWv0Si7b7oBhLjaX0UCYpk2YqucAvImmI787JVQGBUZ3vbbOqrP4FU7Gm8CjCq4XaNkTQ3_QbP8t3y7ZJ4sZThA0KTPylJ8liBEjlLQVfWYoR9F0j4KYpiOXCDAUeiYqExpphQ1flSDxRyI8H0ngC3hMJg6mkMnX_EYTKRGWGvbh-Kivqh7CGVYenPb_HwOdogWf5sKZPH_nVBNV_xIjmtWOwh-o2Wp0jzXRn85eErK4kClulL19e9blwASwGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68da57faf0.mp4?token=KD3L_7A-z4xF2nJOMD03u97HRe5o6M8UNfP1y21KIFUe1BPXXp24DMsu9x6czrO3dfXrs5cI6RWGrK7nAnvdAmvElb1B75ru5_zBOZVxK2km9YUpE5MK86C_Ps8_TTgVAugYDdv7P7iTE0HI7Tn_Ne0tlmisNPXZTM32TiXVaNrGntbWe9K5xxf4uryqTASMmFIbFqi6puugc_MeHJ3D2m9vTJrLovgcagu5SodZ0cievg4GKkbJQyFld57oDBPLaB6ZwC56mgX6SyWqagxLEbLg3nA0ebjegIGA2lj-OP37TN9qnIrSqWjfstufbs0RJgH8jZVWsVM0eKFGJ8OE_JJxJXdqXl77Svu-45AEafhx5Cg-rc7XhMVAyRB74W77XH7cHTE_Of8H5zJ0tMBTFp2e5a30cPS4PgyWcDlWrCamYTWv0Si7b7oBhLjaX0UCYpk2YqucAvImmI787JVQGBUZ3vbbOqrP4FU7Gm8CjCq4XaNkTQ3_QbP8t3y7ZJ4sZThA0KTPylJ8liBEjlLQVfWYoR9F0j4KYpiOXCDAUeiYqExpphQ1flSDxRyI8H0ngC3hMJg6mkMnX_EYTKRGWGvbh-Kivqh7CGVYenPb_HwOdogWf5sKZPH_nVBNV_xIjmtWOwh-o2Wp0jzXRn85eErK4kClulL19e9blwASwGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان چندسال قبل: مهسا امینی همینجوری نمرد بلکه زدن کشتنش
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147703" target="_blank">📅 15:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147702">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrA4QIQaDt5Njmqa9TPeCXdClv8wjZuG1tkbwN1JzRGDSN-kbljuCLhmnxjK2_J00rOouwUi7VjSGdUYp1fCzREQ6D3ls3FIcMRcjbssAmNqtX3EKnGf5SQ4DYMtVBKakB8RJjQucMoIq_BJ8wPBho0WbzC-LwGx0Q0UtdY23ETneNY5M-5sUspQftam7z-tHiIFyKm-Y9g_0fW5qBTq82eBYIrmCPi1f8oK2VlRetmmyQXQRVL5UdAXKQKam1Ech5Otihd0NxcHi2IEroZJ7Z1m4HTTM3nWWI26N6iHzGNpwcxNgF3Id2yQzOdJqScl0L6vMW1n54TIQj-z-cGhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز سالگرد جاویدنام مهسا امینی است دختری که فقط بخاطر چندتار مو توسط ظالمین کشته شد
🔴
یاد و نامش تا ابد جاویدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/147702" target="_blank">📅 15:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147701">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نتانیاهو: پیام ما روشن است. هیچ تروریستی مصونیت ندارد و حماس در غزه نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147701" target="_blank">📅 14:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147700">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رویترز: مقامات آمریکایی این هفته در عمان با نمایندگان گروه حوثی دیدار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147700" target="_blank">📅 14:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147699">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
برخورد ناوهای هند و پاکستان در آب‌های بین‌المللی
🔴
یک ناو نیروی دریایی پاکستان در شمال دریای عرب با یک ناو جنگی هند که در حال گشت‌زنی بود، برخورد کرد. هند در پی این حادثه، دیپلمات ارشد پاکستان را احضار و نسبت به رفتار «غیرقابل قبول و غیرحرفه‌ای» نیروهای دریایی این کشور اعتراض کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147699" target="_blank">📅 14:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147698">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رویترز: مقامات آمریکایی این هفته در عمان با نمایندگان گروه حوثی دیدار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147698" target="_blank">📅 14:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147697">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به نظرتون کدوم بیشتر رشد میکنه؟</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147697" target="_blank">📅 14:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147696">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: دو نفتکش با پرچم کشورهای خارجی که عازم آمریکا بودند، هنگام عبور از تنگه جبل‌الطارق هدف حملات سایبری قرار گرفتند. واشنگتن تاکنون عامل این حملات را شناسایی نکرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147696" target="_blank">📅 14:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147695">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
یک پهپاد اسرائیلی در ارتفاع پایین بر فراز شهر بعلبک و روستاهای اطراف در حال پرواز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147695" target="_blank">📅 14:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147694">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کاتز وزیر دفاع اسرائیل: ارتش دفاعی اسرائیل در صورت دریافت دستور آماده است تا حماس را نابود کند و ماموریت را به پایان برساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/147694" target="_blank">📅 14:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147693">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKQGaGPuxNY5FVsYGDsA0lJ0LmHxetSxrU-IfG6faqQhkwOtKsqADwV-HXXdnzenPdvgiGJ2xu7M-pn3fyhOcb8n0QetIUtYZc_3YAeOTBaSbDX7np5GOUWDZkamJh06tjFZYizCi3lkINcb3yGNBfFmYmYhd_xPLqt2gMJYz8q1Y5lv-DXFeVsD2xcne5tBieyrqwN7ikyB_EFCa3j9qQVBgw24gwYCX2WeKUD1gfjY2iEvIiIPnAy6viESa96GHiCLjuLpgZO-5zgu6XLV7rSKD3_iAF4MywaIq0iks94u7b5fuU5aC9AH5GZI0y-D-nBgdKTmUPKlEH7tb280lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوارنگاره جدید میدون ونک:
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/147693" target="_blank">📅 14:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147692">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان به خبرگزاری فرانسه: ما به دنبال توافق امنیتی با اسرائیل هستیم که می‌تواند مقدمه‌ای برای توافق صلح باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147692" target="_blank">📅 13:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147691">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:
به زودی اروپا باید منتظر پاسخ ما به ارسال پرونده هسته ای ایران به شواری امنیت باشد و عواقب آن را بپذیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147691" target="_blank">📅 13:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147690">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر رفاه: برای مردم عزیزمون کالابرگ رو حداقل ۳۰۰ هزارتومن زیاد میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/147690" target="_blank">📅 13:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147689">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/147689" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147688">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
دبیر کمیسیون فرهنگی: شادمهر عقیلی اگر برگردد و در چارچوب اخلاقی نباشد، با او برخورد می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/147688" target="_blank">📅 13:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147687">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پیش‌بینی بارش‌های پاییزی فراتر از نرمال در کشور
🔴
رئیس سازمان هواشناسی: نقشه‌های پیش‌بینی نشان می‌دهد بارش‌های کشور در پاییز فراتر از نرمال خواهد بود و این وضعیت تا حدودی در اوایل زمستان نیز ادامه دارد.
🔴
هرچه به فصل زمستان نزدیک‌تر شویم، سیگنال بارش‌های فراتر از نرمال در نقشه‌های پیش‌بینی کمرنگ‌تر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/147687" target="_blank">📅 13:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147686">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: بزرگ ترین حمله را نتانیاهو تدارک دیده است
🔴
۴۰ هزار بمب و ۲۰ هزار کلاهک جنگی: تسلیحاتی که دولت ترامپ در قالب یک قرارداد عظیم در اختیار اسرائیل قرار خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/147686" target="_blank">📅 13:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147685">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
زلنسکی: روسیه دو بار تلاش کرد هواپیمای من را هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/147685" target="_blank">📅 12:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147684">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsLIuv2nAD_XB8mEcLnWRMlviXQv3rkfS1fpfX53jDo6ZCT7h7wpACg7KrqZEZyDqeT7MpluTWi-bE0A2uSQJWRfC0CbGOHPQY7iqY4rK9vZ4OjIPzwwzS52kfFMWdLagcx_HrWQZWNpVjYW06YTqDovqLVBKqxBGpdnjRhH80FB7CBqTG1kuBD9J0KPblbIklfrCHJbnM9bS-bmbie_Sc8CDuINQ6IBoh0lxUKZrYzUIDUIpkEZab-yuVzSW8tS2YJtjjvdsmAoJZTw6OBVVWvCSAVAYuFnzuHuAXuoSBLqnFK1BrRyEZVG7nhEa0ecZX14QKYUEKZASSX-w5nnnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای سازمان ملل متحد قرار بود در فرودگاه صنعا فرود بیاید، اما قبل از فرود، مسیر خود را تغییر داد و به فرودگاه بازگشت. این اتفاق همزمان با حضور یک هواپیمای سوخت‌رسانی سعودی در نزدیکی یمن رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147684" target="_blank">📅 12:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147683">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c0324d63.mp4?token=K8CsTMRLGytqudgsv-FsFd_1gdE9GSNIP20OCQTojsQkRXu8ikxDCmrEhebEaa4IxBSapIaa_Tzo_5gwJU7PaQHR9gGi2lUemkAdxERY-Zj--tY8tZnH3cThzQ7_35MRFJS-Eqx5P3tGVOIVkfPLBjN0Zkb9DzxPGXLoLAr2yudNtD6Z1jNh0uqkFsdHmspvZlbTQqtiiHDIgXlE0WFeYJIyXZ5KlzuDVJm1wu1B96j0g8pOasrlPNBGNVX4hjzbOJM1hHA5a7ZYRBmN_frmIN-5Mv1u8qViHCOxQDsG43gISei2zlP_tVUdAIAcSSMCYXCkn_K3RAjYE0nFNuudyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c0324d63.mp4?token=K8CsTMRLGytqudgsv-FsFd_1gdE9GSNIP20OCQTojsQkRXu8ikxDCmrEhebEaa4IxBSapIaa_Tzo_5gwJU7PaQHR9gGi2lUemkAdxERY-Zj--tY8tZnH3cThzQ7_35MRFJS-Eqx5P3tGVOIVkfPLBjN0Zkb9DzxPGXLoLAr2yudNtD6Z1jNh0uqkFsdHmspvZlbTQqtiiHDIgXlE0WFeYJIyXZ5KlzuDVJm1wu1B96j0g8pOasrlPNBGNVX4hjzbOJM1hHA5a7ZYRBmN_frmIN-5Mv1u8qViHCOxQDsG43gISei2zlP_tVUdAIAcSSMCYXCkn_K3RAjYE0nFNuudyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موج تازه‌ی بازداشت بانوان توسط پایداریا در کابل
🔴
دست کم ۲۰ زن و دختر در کابل بازداشت شدند و  گروه خودخوانده طالبان از تشدید نظارت بر حجاب و موسیقی خبر می دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147683" target="_blank">📅 12:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147682">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlLtKYanuMDmdvfbK3ghpaprY1MHpHJfUkpJO6Fh67zlaRA7DYlEY2Vtsj87n3wyDO3d1bsOq8U_CUxhUJpf0gB-Osr6mIU3sjstJekp-nJxyUXyY-3-w5wZZNcWLugLT2sg5ytLk7TCfECvGDqOZCfmdn4k01o_SCaeWr4gajc-mFOaXhfCk-9f3wvYhiLsHShD9bLwfLiaeIko-Inm5gorDz90505SzUkBr8eIjyvnhBqk4ICcGA5Q5ZDdLn43ZjWKHqJ_Ggx33OPL0gSXrKbPHgzf6LVnAEeI8qmlLkMUA3O7l1DYEcsWAFGWVsvNuOTSyoSg4hmQsXUeeFOzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
تخفیف فضایی تپسی‌فود
🔥
تا 50⁒ تخفیف ویژه رستوران‌ها
همین حالا غذات رو از تپسی‌فود بگیر
🔥
از اینجا سفارش بده
👇
https://tapsi.food/?utm_source=telegram&utm_medium=social&utm_campaign=fz0625
⚠️
مخصوص تهران و مشهد، کلیک کن
☝️</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147682" target="_blank">📅 12:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147681">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a02cc6cfc9.mp4?token=qezZIHxY_Uwl6TrERqJex62rel-b-ysw3qqtcCtCHYF2C1HvfE1t2UTL3Ghz0cBK7GV_8ZXop3V0oBT3zcOE2kV_D2RUNFnin-oUjJkRi0EtnvnCwNkiM0ivzfefa8Wn-5ltLnSF9JRnKXZ4Ao_WUiOHXjmlp3M_gJHxGmlblgqkBzuon7GcPp9ivr_RvImvKaUeAGdbOaXBFBXKZIfGiRQTrBtE9A5bKQNa2K9anyEyNdw1xFSDNJXB6n47F_1OpZirlGDwzV11t9wVc2kgC-OyPgAnTCzxgY5dOTrdtiMyw6H5yXFPdUXqpcO0Zyd15myVbJeUJGGCGOdr2fayOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a02cc6cfc9.mp4?token=qezZIHxY_Uwl6TrERqJex62rel-b-ysw3qqtcCtCHYF2C1HvfE1t2UTL3Ghz0cBK7GV_8ZXop3V0oBT3zcOE2kV_D2RUNFnin-oUjJkRi0EtnvnCwNkiM0ivzfefa8Wn-5ltLnSF9JRnKXZ4Ao_WUiOHXjmlp3M_gJHxGmlblgqkBzuon7GcPp9ivr_RvImvKaUeAGdbOaXBFBXKZIfGiRQTrBtE9A5bKQNa2K9anyEyNdw1xFSDNJXB6n47F_1OpZirlGDwzV11t9wVc2kgC-OyPgAnTCzxgY5dOTrdtiMyw6H5yXFPdUXqpcO0Zyd15myVbJeUJGGCGOdr2fayOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هلی برن نیروهای ویژه اسرائیل روی سقف یک خانه در اطراف کرانه باختری
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/147681" target="_blank">📅 12:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147680">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
بلومبرگ: پاکستان در حال بررسی گزینه‌های خود در مورد یک نفتکش سرگردان در دریای سرخ در نزدیکی خط لوله شرق به غرب عربستان سعودی است و هشدار می‌دهد که هرگونه حمله به این کشتی به عنوان "عمل جنگی" تلقی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147680" target="_blank">📅 12:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147679">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سی‌ان‌ان : گزارش‌ها، چهارده ماهواره جاسوسی روسی چند روز قبل از حمله ایران، بر فراز یک پایگاه نظامی آمریکایی در عربستان سعودی پرواز کردند.
🔴
مقامات آمریکایی گفتند که اطلاعات جمع‌آوری‌شده ممکن است با ایران به اشتراک گذاشته شده باشد و این امر به انجام حمله دقیق، که شامل موشک‌ها و پهپادها بود و باعث زخمی شدن ۱۲ سرباز آمریکایی شد، کمک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/147679" target="_blank">📅 12:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147678">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
تو سایت های شرط بندی احتمال حمله نظامی یا اتمی ترامپ به ایران تا قبل مهر ماه به 84% رسیده!
🔴
بالاترین عدد تو دو ماه اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/147678" target="_blank">📅 11:55 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
