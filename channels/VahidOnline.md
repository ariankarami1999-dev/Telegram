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
<img src="https://cdn1.telesco.pe/file/Lf2vvtv8vP1LFESNACHgktcIsvq_CkYCaKtuLCzKtXfbY2xwIgAtqvV1tzdQHkmRYvwpVqijUv8N8thzSWVjmhyIzvA6Pv2lb6uDoSIoBdScuj2y2-IRcwsedGygiTjthZ_GxEYxL_QpZsgQLHmwJaGLdYpIieKfEFjksvcG14p6bp35Klg9dvR5WbNVsaQV9-LkzCnSUOdf1gIh-sqKgIU_auhtyKvoQS1gQh-wMvFj9ybYvJWUEDjWfiZeBfIh5DKq4LG9rMo4YLk7z212K4FS-m91pAsjO_0nVCYFrA6A9_q82D3ibpdvhit1qbdXqlCkoTsgapgXSwm433cfyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.43M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 03:00:38</div>
<hr>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=nkOMUjRb4yBNNlskWPNYc5Y88w6Zis_gnqcElsfTCw5UgTlvYS_9GZkcGaVqHlvsNQOJt4hx6cVQUFb2h22B7GPf8h5tjVfOhxRULx5T_PB0PXfSZD347RaulYuHTd6fYI4KrbVe68TjwRTIFjqRGJsouV19VeAnujY67A64IZc0vI81m6mqLphBbbqFiZjhBnwZpYoAoAZKyXhIUX-1PU-PI89v4MEI84Zv5lIg3PqGq9iPVMSvxsPuKefBhq_Pmpf73-bfr_sPlouK3MpKPYYTjdSj-QwQ2ogbnelXp9Z-vFQlgCBPTOhtBoT6UsAeIF_8ODaS5wrfUqrtd4GsDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=nkOMUjRb4yBNNlskWPNYc5Y88w6Zis_gnqcElsfTCw5UgTlvYS_9GZkcGaVqHlvsNQOJt4hx6cVQUFb2h22B7GPf8h5tjVfOhxRULx5T_PB0PXfSZD347RaulYuHTd6fYI4KrbVe68TjwRTIFjqRGJsouV19VeAnujY67A64IZc0vI81m6mqLphBbbqFiZjhBnwZpYoAoAZKyXhIUX-1PU-PI89v4MEI84Zv5lIg3PqGq9iPVMSvxsPuKefBhq_Pmpf73-bfr_sPlouK3MpKPYYTjdSj-QwQ2ogbnelXp9Z-vFQlgCBPTOhtBoT6UsAeIF_8ODaS5wrfUqrtd4GsDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری‌های ایران تصاویری از «آلودگی نفتی» در بخش‌هایی از سواحل قشم منتشر کرده‌اند.
به گزارش این منابع دادستان قشم دستور شناسایی منشا آلودگی، مهار، جمع‌آوری و پاکسازی نوار ساحلی را صادر کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/VahidOnline/77823" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO_iCj2w_Bl2K-WWaPVqbwZVK31M7uuadVMiRDWEzDA3nGTJziCsYSEKkVcLE6EXOfecryvtHPViUObYDzfhRjETuzMIIPDGqNkfn4Go3Gs0jQSKRYDr94sXwQ8zp-rd50mcyMWTuznmwnDe0N6SF_rI25SWiYFe12zTwF_361RSvXL3am-G07Nly11ENqvvHv-u91JPsNVOVLpPJ8wU5sLVqycNjeCWmGMhlnASxA9FCBRzB0IJ3GlqzOURIHQLKkClCvj_mVGtY4-SqTH7OvBFJcoOwdkNGz529TP2_P1CIW3aVfoVKqJsrGnlzu4XJE-r0ErUwPvc7zYMiDeGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر جدید شورای عالی امنیت ملی جمهوری اسلامی، در نخستین موضع‌گیری پس از انتصاب به این سمت اعلام کرد برای باز شدن تنگه هرمز، آمریکا باید جنگ را پایان دهد و پول‌های مسدود شده ایران را بپردازد.
به گزارش رسانه‌های ایران، او در دیدار با سفیر چین در تهران گفت تا زمانی که آمریکا «رفتار خود را تغییر ندهد و شروط ایران را نپذیرد» ایران اقدام به باز کردن تنگه هرمز نخواهد کرد. او پایان جنگ و آزاد کردن پول‌های مسدود شده ایران را دو عنوان از شرط‌های ایران برشمرد.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در کاخ سفید به خبرنگاران گفت ایالات متحده کل تنگه هرمز را «مین‌روبی» کرده و کنترل کامل آن را در دست دارد.
محمدباقر ذوالقدر، دبیر سابق شورای عالی امنیت ملی، که رضایی جایگزین او شده است، هفته گذشته شروط مشابهی مطرح کرده بود.
محسن رضایی درباره مذاکرات جمهوری اسلامی با سلطنت عمان درباره عبور و مرور در تنگه هرمز که طی هفته‌های اخیر در جریان است، نیز گفت اگر بین دو کشور توافقی در این زمینه حاصل شود، «این توافق موضوعی جدا از انسداد تنگه هرمز خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/77822" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n1HHIuzugroPcFVzSz0ptnLb2b_Ty5rCTDQKugivfgqnT_RKqpXrjW0AELE-FQSDEnq1F6S9b48VyE0jJwJP93INZygXAAE1Uhs7OigLW5kCUIHibZomZLG86_5gkTpa1yoBrEMkhjgWfHI1jo-6KEGYIH4K9Lnynh-QTupXcHIge6-NYX7-7jDF0kaNrytek1BsyiNA1bWRIIQN8ejp1ay3-HeqAPF1jiazpzhPQqBPaorAl8PUx1LbwyoCrInXeqF4R2kZdenLbV-21tDOUaNCkj-hVScJNJPWq42nkuF4VAVw_nKwN1NMw5x5WT-DXjQ91AR_cJAABc8xAJUIew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر مانع دستیابی آن‌ها به سلاح هسته‌ای نشده بودم دیگران ناچار بودند رهبران جمهوری اسلامی را «آقا» خطاب کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/77821" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77820">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hdAIJB02PTd8XIROaZ86umddPvueOl0yP6ZpK9HjpJBsmHre2m9b7wV8CDT_fgIor4avG48mTuokWjuKLBFLb6TOog7ciBYj5SjrtZdmhSNQRiS3vvzcMJfyINgAHdZgzHChqXdiTMaglKqetkPqdPpBYulwqiLWdzxNmzoMZQXJimu_lsJ-N5THoSqSfHgL8bIGLO7GGw1-Bi43j814KnN50bMd_PTF44IeC9rVyu3oa5HMs5L41tkBadE4Aq4dQ6JrUBmdvwlekZUmDOnDAY-mpDIe4HCtbiZW-_hnKIo5SFsg5km5v56l9X8o5w_lr2ogWHBPDna21KWCOLI88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسی کوهن، مدیر پیشین موساد، گفت ماموران این سازمان در گذشته چندین بار از تاسیسات غنی‌سازی اورانیوم فردو بازدید کرده بودند تا اطلاعات بیشتری درباره این مرکز هسته‌ای به‌دست آورند.
به گزارش تایمز اسراییل، کوهن، روز سه‌شنبه ۲۰مرداد ۱۴۰۵، در نشست «مجمع جلیل» در شهر صفد، گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک کنیم.» او درباره زمان این بازدیدها و این‌که چه افرادی از سوی موساد در این بازدیدها حضور داشتند، توضیح بیشتری نداد.
او همچنین درباره حمله آمریکا به فردو گفت: «بمباران آن توسط آمریکایی‌ها تحقق همه رویاهای من بود.»
تاسیسات فردو، همراه با مراکز هسته‌ای اصفهان و نطنز، در جریان جنگ ۱۲روزه اسراییل و ایران در ژوئن ۲۰۲۵ به‌شدت آسیب دید.
گزارش‌های پیشین حاکی از آن بود که حدود ۴۴۰ کیلوگرم اورانیوم با غنای بالا که در این تاسیسات نگهداری می‌شد، زیر آوار مدفون شده است. با این حال، اسراییل بر این باور است که ایران پس از جنگ بخشی از این ذخیره اورانیوم را به سایت «کوه پیک‌اکس» منتقل کرده است.
کوهن همچنین گفت اورانیوم غنی‌شده تا سطح ۶۰ درصد همچنان فاصله زیادی با ساخت بمب دارد. این سخنان با ارزیابی برخی کارشناسان هسته‌ای تفاوت دارد. دیوید آلبرایت، کارشناس حوزه هسته‌ای، پیش‌تر گفته است اورانیوم ۶۰درصدی ایران می‌تواند در صورت تصمیم تهران برای ساخت سلاح، ظرف چند هفته یا حتی چند روز تا سطح مورد نیاز برای تولید جنگ‌افزار هسته‌ای غنی شود.
کوهن پیش از این نیز به‌طور علنی درباره فعالیت‌های موساد علیه برنامه هسته‌ای ایران صحبت کرده بود. او چند روز پس از پایان دوره ریاستش بر موساد در سال ۲۰۲۱، در مصاحبه‌ای کم‌سابقه با تلویزیون اسراییل، جزئیاتی از عملیات این سازمان علیه ایران را بیان کرد.
او در آن مصاحبه از انفجار در تاسیسات زیرزمینی سانتریفیوژهای نطنز سخن گفت و توضیحاتی درباره عملیات سال ۲۰۱۸ موساد برای سرقت آرشیو هسته‌ای ایران از یک انبار در تهران ارایه کرد. کوهن همچنین گفت محسن فخری‌زاده، دانشمند ارشد هسته‌ای ایران که بعدتر ترور شد، سال‌ها در فهرست اهداف موساد قرار داشته است.
کوهن در برنامه مستند «اوودا» با اجرای ایلانا دایان در شبکه ۱۲ اسراییل نیز گفت که با تاسیسات مختلف هسته‌ای ایران آشنایی نزدیکی دارد. او در این برنامه گفت اگر فرصت پیدا کند، دایان را به بخش زیرزمینی نطنز خواهد برد؛ جایی که به گفته او سانتریفیوژهای ایران در آن فعالیت می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/77820" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oiii3bCreJSf_SOaGho4VFzfpfSbiZGhEvt0Jg6pQlamebKkMRTyhfLMNz2He1nEs0852sdY70VZkU9pEkZwLgV2dOoDrG25Tr1_LP3Gm4pfis7iNdzTgsnM55TSCWwUswBx8D72ucAvVAxhUJtIDQ8n5K_F24ZxBWTj8aadyOjrGWJGTcqxcC9DqHBwlmZijTZwuGDGklzcTtL4l9CYoch5CBmZrdbbBSEWQZwTIFlhCxMLoy7-eZbIuWNi1JP3PdIrBjnU24L0Jh_H5xVFbxtXc79Ymny2R02EmOYgsbbcTnnCu_rW4pY6Fc3ltUZ7_ZeXfb1Sk10RAd6Kj8eP0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار شبکه‌های تلویزیونی العربیه و الحدث عربستان سعودی روز سه‌شنبه، ۲۰ مردادماه، گزارش داد که در پی اصابت یک موشک بالستیک  حوثی‌ها به یک کشتی تجاری در تنگه باب‌المندب، سه نفر از اعضای خدمه این کشتی کشته شدند.
بر اساس این گزارش، قربانیان دو پاکستانی و یک تبعه اندونزی بودند. الحدث گزارش کرد این موشک از شرق استان تعز شلیک شده و کشتی تجاری را هنگام عبور از باب‌المندب هدف قرار داده است.
این حمله در شرایطی رخ داده که تهدید علیه کشتی‌های تجاری و مسیرهای کشتیرانی در دریای سرخ و تنگه باب‌المندب همچنان ادامه دارد. باب‌المندب یکی از مهم‌ترین گذرگاه‌های دریایی جهان برای تجارت و انتقال انرژی میان دریای سرخ و اقیانوس هند است.
همزمان، درگیری‌ها در چند جبهه یمن نیز ادامه داشته است. بر اساس گزارش «العربیه» و «الحدث»، نیروهای دولتی یمن مواضع و تجهیزات حوثی‌ها را در چندین جبهه هدف قرار داده‌اند.
@
VahidOOnLine
شمار کشته‌شدگان حمله حوثی‌ها به کشتی تجاری در باب‌المندب به ۴ نفر افزایش یافت
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/77819" target="_blank">📅 18:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vho3c-ekD-3vUoii3wo3YMGjxxbR9kgjRuclQJ3SoB06_1Ui0IDNvy7q3GZNOvrka8-myqyZyFqhuS_cR_PpeOd2y7tmLLBnFUdJ3CD4xl1Npq955ZV0g7ddhL2u-jANqnuT6wlwYsqN-jmVnb-3q_ownfx7NN_zNbmLQkaJmG861d4JaM92ZFZ8Fd_sOCA6j9iC6my4pdeRbATtfqxNVDrVyvE_KqEjDF7eCB3TA-S1unGuztMvJ-CsMzEb7CiV64cT3FEl1smBEE2hBwWEF4ZKp715XeyAWhOmi-JNckOHSgU8-fqTr4lXWm0S5n_iVmRjQHDmf1hUmCdZAh5Icg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی و منابع امنیت دریایی از هدف قرار گرفتن یک کشتی کانتینربر با پرچم پاناما در دریای عمان خبر داده‌اند؛ یک مقام آمریکایی می‌گوید این کشتی به هشدارها برای توقف توجه نکرده و در تلاش برای شکستن محاصره دریایی بنادر ایران بوده است.
همزمان، روزنامه وال‌استریت جورنال به نقل از یک مقام آمریکایی گزارش داد که یک بالگرد نظامی ایالات متحده پس از آن‌که خدمه کشتی هشدار نیروهای مأمور اجرای محاصره بنادر ایران را نادیده گرفتند، به سکان این کشتی شلیک کرد.
@
VahidHeadline
آپدیت:
پست سنتکام ترجمه ماشین:
اوایل امروز، نیروهای سنتکام تجهیزات هدایت کشتی
M/V Vela Nova
با پرچم پاناما را از کار انداختند؛ این کشتی باری در حالی که می‌کوشید از خلیج عمان عبور کند و با حرکت به‌سوی یکی از بنادر ایران، محاصره آمریکا علیه ایران را نقض کند.
پس از آنکه خدمه غیرنظامی کشتی هشدارهای مکرر نیروهای آمریکایی را نادیده گرفتند، یک بالگرد
MH-60
نیروی دریایی آمریکا دو موشک هلفایر به موتورخانه
Vela Nova
شلیک کرد. این کشتی دیگر برخلاف محاصره آمریکا در حال حرکت به‌سوی ایران نیست؛ محاصره‌ای که همچنان به‌طور کامل برقرار است.
تا ۱۱ اوت، سنتکام مسیر
۵۵ کشتی تجاری
را که می‌کوشیدند محاصره را بشکنند تغییر داده،
۳ کشتی
را که از دستورات تبعیت نکرده بودند از کار انداخته و وارد
۲ کشتی
شده است.
نیروهای آمریکا که در خاورمیانه فعالیت می‌کنند، به‌شدت هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/77818" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77816">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fY24RNnv5j7H-r1Rj39XIy6VkFRLFPU97ji-d4NAwcx9HfFBgVmhmCFkdtdklDtoDSCyfo-I8OMB0rObqMcuPrQ8qTTiAjR9O_vXTxfJwcAtT16r_ahJNxiVC8trwRrRuZNHAl6tB7D3yAIq9-GKKheNZhv1Js_Q7RU7eX1SBRNIlHYeasWs8zlLYgtzklB8PVOGhy83sgll6bl5ELx6R58su-byh-kLnsFiDUS96FY_gdGtKu1ktyEo0F5K8pxkxCfQS8WwzC_gqBqdtML4WFC-8lPxMaFCXYSe4UiGCsEOkyeRqicy83KRxuzfteUok6v5Vztk4El5Q53ndAaGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kVvkvGVQmowEDbdrjc-lobP8IkIhRaVLNCke_RMI4BLnYzbuykhHbNERYAcE7zQd8hRyqJtGN2cPn3hiS4AeOjc8OTpOIA_cwBnsfbMn4K2bF8CM36ZWbt0qGE7csmFg816HlsHLCBzspIomY0kmcFfHLjqbqMucVwZGlD9zUA1DqWfm9fG3WLA0T006_QtU8NFieB9HvHd9-Vipd0JF4Kd3ugd5kalu55bMm-N5TSL2RsS8DEL9COcxynSVsX-OxHccT5NleV1ngcJNhI9_VpHicDOEsGE1JHnYBR4veVX2ZQeOgKeIctg2BMSL_07zbIID2t8hROHmNBqHprVsjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی وزیر کشور پاکستان، پس از ورود به تهران در عصر سه‌شنبه ۲۰ مرداد ماه با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران دیدار کرد. محسن نقوی پیش از دیدار با عراقچی، در تهران مورد استقبال اسکندر مومنی، وزیر کشور قرار گرفته بود.
@
VahidOOnLine
وزیر دفاع پاکستان می‌گوید ایران و ایالات متحده به «شکلی از توافق» نزدیک شده‌‌اند.
خواجه محمد آصف این موضوع را در قالب گفت‌وگویی با بلومبرگ، که روز سه‌شنبه ۲۰ مردادماه منتشر شد، عنوان کرد.
این مقام بلندپایۀ پاکستانی گفت: «روند تحولات جاری، بار دیگر به سمت‌وسوی یک توافق یا تفاهم صلح شکل گرفته است».
وزیر دفاع پاکستان تأکید کرد که «نشانه‌های مشاهده‌شده طی دو، سه روز اخیر حاکی از نزدیک‌شدن به نوعی توافق هستند».
هم‌زمان خبرگزاری ایسنا می‌نویسد که محسن نقوی، وزیر کشور پاکستان، «در چارچوب تعاملات دو جانبه و میزبانی اسکندر مومنی وزیر کشور» عصر سه‌شنبه وارد تهران شده است.
@
VahidHeadline
همزمان با ادامه تنش‌ها در تنگه هرمز، سخنگوی وزارت امور خارجه قطر روز سه‌شنبه ۲۰ مردادماه اعلام کرد که مذاکرات میان تهران و مسقط برای آینده کشتیرانی در این آبراه راهبردی بین‌المللی، به مرحله «پیشرفته» رسیده است.
به گزارش العربیه، سخنگوی وزارت خارجه قطر با اعلام این خبر گفت پاسخ‌های مثبتی از تهران دریافت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/77816" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77814">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pByEDLTrRFfLJPsaW2v49jI1vn3zhm2UUcpV61h7d0t3vbos8IJenwbeiQt56DYZuEiSwXpyNEAPE8Ng3gRtHtbXkx2yiJItseymHXUpeSR30N2HXIOanrA92aTEOIXI67NmyTS32CF_NE7QEwQWGb6WvWrETBcnMARCCZBOPPNWAyUdBtUnG50938yrG3K3mAqM_sM4sv79V9iUlLL3DUx_fC6uEw04RrDUtku1rzCYlq13Wl81aN2z6Hv3QrstgKgO91Zd5SU3kSash9XGFduPtXI84WaU8MfL0qgS-PdF8AMC0FSc3GL8MIwQtQEza0xC2g9Q0urDs7zXeB-wPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=OmtNI-uUsBlcWJkmiYxAYHtQsn0UNm_hMYOh0HYm3HoDhragSjN7AwUcO-6BiTx-Gf3FQ1g0bg1I9LURX9b58kuAgKWIEncn0iAjar-kVXjoqHoo49XlzNUXkDMVHFErfcOLcHUJHFr1xFGe5BjB6NSoNG8Br_kMeywE4Fo0F97MBMUQppHtdEFDNseeMPJ4hncf7PQs5j5j96qfu1mDaqnToitVD4LhW3oWRdLA1nsZDyO4PuHSA1Ji1O-Zo3HcwpggVLRGLXGeQhy-40iGnnkxi8wN5BWTtn2KDvSFp7ULdGZg9pPAJI-_el5Ff4X3cl8dbvzog3-KCBaydHOEnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=OmtNI-uUsBlcWJkmiYxAYHtQsn0UNm_hMYOh0HYm3HoDhragSjN7AwUcO-6BiTx-Gf3FQ1g0bg1I9LURX9b58kuAgKWIEncn0iAjar-kVXjoqHoo49XlzNUXkDMVHFErfcOLcHUJHFr1xFGe5BjB6NSoNG8Br_kMeywE4Fo0F97MBMUQppHtdEFDNseeMPJ4hncf7PQs5j5j96qfu1mDaqnToitVD4LhW3oWRdLA1nsZDyO4PuHSA1Ji1O-Zo3HcwpggVLRGLXGeQhy-40iGnnkxi8wN5BWTtn2KDvSFp7ULdGZg9pPAJI-_el5Ff4X3cl8dbvzog3-KCBaydHOEnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاهی در دمشق، پایتخت سوریه، روز سه‌شنبه ۲۰ مرداد ماه، بشار اسد رئیس‌جمهوری پیشین این کشور را در یک محاکمه غیابی به اعدام محکوم کرد.
فخرالدین العریان، قاضی دادگاه دمشق، روز سه‌شنبه اعلام کرد اسد به اتهام‌هایی از جمله «قتل عمد، کشتار عمدی بیش از یک نفر، قتل عمد کودکان زیر ۱۵ سال، شکنجه، شکنجه منجر به مرگ و سلب آزادی به دفعات» مجرم شناخته شده است؛ اتهام‌هایی که دادگاه آنها را «جنایت علیه بشریت و جنایت جنگی» طبقه‌بندی کرد.
دادگاه همچنین شش مقام نظامی و امنیتی سابق را به صورت غیابی به اعدام محکوم کرد که در میان آنها ماهر اسد، برادر بشار اسد و فرمانده لشکر چهارم ارتش سوریه، نیز قرار دارد. ماهر اسد نیز پس از سقوط حکومت برادرش از سوریه گریخت.
دادگاه کیفری دمشق از فروردین گذشته روند رسیدگی قضایی به پرونده اسد و شماری دیگر از مقام‌های سابق این کشور را که برخی از آنها در دادگاه حاضر بودند و برخی غیابی محاکمه شدند، آغاز کرد. این افراد به ارتکاب جنایت‌های گسترده در جریان جنگ داخلی متهم شده‌اند؛ جنگی که در سال ۲۰۱۱ با سرکوب شدید اعتراض‌های مسالمت‌آمیز علیه حکومت اسد آغاز شد.
در جریان این جنگ بیش از ۵۰۰ هزار نفر کشته و میلیون‌ها نفر آواره شدند و ده‌ها هزار نفر نیز ناپدید شدند؛ بسیاری از آنها به زندان‌های حکومت سابق منتقل شده بودند.
اعتراض‌های سوریه در مارس ۲۰۱۱ از درعا و پس از آنکه ۱۵ دانش‌آموز به اتهام نوشتن شعارهای ضدحکومتی روی دیوارهای شهر بازداشت شدند، آغاز شد. ساکنان درعا اعلام کردند این دانش‌آموزان شکنجه شدند و در پی آن، اعتراض‌هایی برای آزادی آنها شکل گرفت که با خشونت سرکوب شد.
نیروهای امنیتی برای متفرق کردن معترضان از گلوله جنگی استفاده کردند و اعتراض‌ها به دیگر استان‌های سوریه گسترش یافت.
خانواده اسد بیش از پنج دهه بر سوریه حکومت کردند. بشار اسد در سال ۲۰۰۰، پس از مرگ پدرش حافظ اسد، به ریاست‌جمهوری رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/77814" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77813">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vKjN3t1lA1IwgXAHSk-Om6aDvLbG0i7HP5BuVWaK3PjuwZ7kxJscD3oSldEaVEaWbjaBcBCJufXt-wBWJe1wKgCH2qqzwYs6YciAcjWGzllV5EBZM-p58Rln0uw8bjMzkubZs1u8kI6Prg4xF2zc2nitH4r4NOgRgJKQI0542VLb_NeThhwhpk8T7hfH9o-nt0f-IJbWR7i8svjMRFVGiZxtqh8H34FXq7NhmxQVcCD0HmiA3gQV4s--Wx4Xpomx_YgynJBfvKzOfkxTkm6Q98kwsma864TpXoEd7uGxP7fcixs9tyEZ83Jhn-nPruma3Gwb4vaPn4pgXnZDO3AMPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارلمان لبنان روز سه‌شنبه مجازات اعدام را لغو کرد و این کشور نخستین کشور جهان عرب شد که این مجازات را با حبس ابد همراه با اعمال شاقه جایگزین می‌کند.
اکثریت نمایندگان پارلمان ۱۲۸ نفره لبنان به لغو اعدام رأی دادند.
فراکسیون حزب‌الله تنها گروهی بود که با آن همراهی نکرد.
عادل نصار، وزیر دادگستری لبنان که در جلسه حضور داشت، آن را «گامی تاریخی» برای کشورش خواند.
سازمان‌های حقوق بشری که خواستار رسمی‌کردن توقف اجرا یا لغو کامل اعدام بودند نیز از این رأی استقبال کردند.
@
VahidHeadline
بر اساس این مصوبه، مجازات اعدام با حبس ابد جایگزین می‌شود. با تصویب این قانون، لبنان از کشوری که سال‌ها اجرای اعدام را عملا متوقف کرده بود، به کشوری تبدیل می‌شود که این مجازات را به‌صورت قانونی نیز از نظام کیفری خود حذف کرده است.
عادل نصار، وزیر دادگستری لبنان، تصویب این قانون را گامی تاریخی توصیف از لغو مجازات اعدام حمایت کرد.
لبنان آخرین بار در سال ۲۰۰۴ حکم اعدام را اجرا کرد و از آن زمان، اگرچه مجازات اعدام همچنان در قوانین این کشور وجود داشت، اجرای آن عملا متوقف بود.
حامیان لغو اعدام می‌گویند این تصمیم علاوه بر جنبه حقوق بشری، می‌تواند در روابط قضایی لبنان با کشورهایی که اجرای مجازات اعدام را ممنوع کرده‌اند نیز تاثیرگذار باشد؛ از جمله در روند استرداد متهمان و مجرمان، زیرا برخی کشورها مجرمان را به کشوری که احتمال اجرای حکم اعدام در آن وجود دارد، مسترد نمی‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/77813" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77812">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VPaoZ6iOFvq5IB1gO2XtuLpURk9rbg7NqmD0GkXqb4wnfmlY21jwULR3Xg18wAEi1Cl7akz_7l2B0KFw8hgDHcOzF_nT3ld0jVuPrC0BNOyuuLReNSFHXR5ULRcBUztAMlPIKH80EwopVTx3Q41MgVx121IIX8zQb3rxLVIM94QeQEAsS7kEHlSOFNvL0pOWp2d9UVegHNsSjd7a0kdjjPz07KAZJ32f7DXIN3STpNbjGXYbz2VW8txcViP_iLYA7gxKZBc-EX2paqe8yr9T6vsUrac2v1-xLw_-6COa4DKn48WvNrIkHd1s76cDMz5beV88J0UL2e3fFLCmPLZCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا می‌گوید واشنگتن سه راهبرد برای جمهوری اسلامی در اختیار دارد و در این مرحله بر محاصره دریایی و فشار اقتصادی تکیه می‌کند.
دونالد ترامپ در گفت‌وگو با برنامه «آمریکا سخن می‌گوید» در شبکه «صدای واقعی آمریکا» گفت: «می‌توانیم همین‌طور رهایشان کنیم و آنها شکست خواهند خورد. می‌توانیم همین کاری را که الان می‌کنیم ادامه بدهیم؛ به‌نوعی آرام و راحت جلو برویم.» او گزینه دوم را «واقعاً سخت ضربه زدن» و گزینه سوم را «شکست‌دادن آنها از نظر اقتصادی» خواند و افزود گزینه سوم هم‌اکنون در حال اجراست.
ترامپ گفت: «از نظر اقتصادی، آنها به‌هم‌ریخته‌اند. نمی‌توانند پول قرض کنند. ما پولشان را کنترل می‌کنیم؛ پولی که داشتند و مقدارش هم زیاد بود. من بانکدار آنها هستم.»
او افزود: «آنها ۳۰۰ درصد تورم دارند. پولشان هیچ ارزشی ندارد. به سربازانشان حقوق نمی‌دهند. سربازانشان دارند ترکشان می‌کنند. فقط همین وضعیت را ادامه بدهید، چون قابل دوام نیست.»
ترامپ مذاکره‌کنندگان جمهوری اسلامی را «بسیار فریبکار» خواند و گفت: «با چیزی موافقت می‌کنند و بعد می‌روند به رسانه‌ها می‌گویند که چنین کاری نکرده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/77812" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77811">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ru2NPnO-bxEOy8vQw6Xq55_FYoFy6aPnvDx6VVNVbtSyhWsJPqfNItWTxxs4PNT3xUvjljzhvWHhSwsbAbdd6uxmNpn9NosQ1eNbQuvGyiGWKkqJhjigqnaj4SVcpdv5Vb1BoNjcXo2BNotc8wjqYye6nxkvjNo9c1uRfWXCLkYbgVc3hEiprlJIZnTCze8zWnntJh5zCGG5VdJyqPlFMNUy_Az_NDKV85ejVk8KZdKYJSLPqp7D87AnyOzjhlDfQl6ojZN9eGZvxwg3KT73O6TJArumVBSr8f6MyEqF6drk6otyWRylp6is5OqHisg1B5_RTJ9MXLL-nFUa9p-PYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی احمدی، معلم بازنشسته ۷۱ ساله، پس از بازداشت در ۱۵ اسفندماه در ممسنی، همچنان در زندان عادل‌آباد شیراز نگهداری می‌شود و نگرانی‌ها درباره سلامت او ادامه دارد.
احمدی هنگام بازداشت در دوره نقاهت پس از دو عمل جراحی چشم و پروستات بود و بنا بر این اطلاعات، اکنون با مشکلات قلبی نیز مواجه است.
او با اتهام‌هایی از جمله «افساد فی‌الارض»، «همکاری با موساد» و «تخریب اموال عمومی» روبه‌رو است.
با وجود داشتن وکیل، پرونده او از زمان بازداشت پیشرفت محسوسی نداشته و دسترسی وکیل به پرونده محدود بوده است. وکیل او نیز پیشتر یک بار بازداشت شده است.
بر اساس این اطلاعات، از زمان بازداشت احمدی هیچ ملاقات حضوری با او انجام نشده و تنها یک تماس تلفنی چندثانیه‌ای در روز عید برقرار شده است.
همچنین درباره وضعیت جسمی و روند پرونده او اطلاعات دقیقی در دست نیست.
احمدی پیش از این نیز چند بار به دلیل پیگیری مطالبات صنفی فرهنگیان بازداشت شده بود. ادامه بازداشت او همچنین خانواده‌اش را با مشکلات مالی مواجه کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/77811" target="_blank">📅 18:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77810">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=dlszHn_sB7VJN64l7xDgURl05l9MZQgi9wbtJXjxV1c1K0poSpaEMO7U9lD6DLnhXAAbAY2OuSNUNngbpK7FUV7cx1XE-ivaGVl0610T2KDq6zQgtiMHOj9oc7wVdJ8DgtuEYSqc5-JxfJ5We4EgWUpUgh5QiSOi9IudxopOd7EhhIVtxC4hKsoPN1AIko-qkMHmHog6H_DS_L2mztmtf0uUBr25_kG2zT8iPMhh7mo72vp_9fX4jDH77aQP5TlIeaamyyB2N7bX1DC7TorJftwHvg7GqjfVGOQA6I6T6j9r3m0Zr9hzjGMY_9JtQ3917cAh5DVslFN098mOYFvn5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=dlszHn_sB7VJN64l7xDgURl05l9MZQgi9wbtJXjxV1c1K0poSpaEMO7U9lD6DLnhXAAbAY2OuSNUNngbpK7FUV7cx1XE-ivaGVl0610T2KDq6zQgtiMHOj9oc7wVdJ8DgtuEYSqc5-JxfJ5We4EgWUpUgh5QiSOi9IudxopOd7EhhIVtxC4hKsoPN1AIko-qkMHmHog6H_DS_L2mztmtf0uUBr25_kG2zT8iPMhh7mo72vp_9fX4jDH77aQP5TlIeaamyyB2N7bX1DC7TorJftwHvg7GqjfVGOQA6I6T6j9r3m0Zr9hzjGMY_9JtQ3917cAh5DVslFN098mOYFvn5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد
ترجمه ماشین:
واشنگتن‌پست
دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه پرواز کرد، در حالی که کاخ سفید اعلام کرده بود او سوار ایرفورس وان است.
این مأموریت محرمانه که پیش از این گزارش نشده بود، بدون اطلاع خبرنگاران و حتی برخی کارکنان کاخ سفید انجام شد؛ افرادی که تصور می‌کردند در همان هواپیمایی هستند که رئیس‌جمهور در آن حضور دارد.
دولت مدعی شده است که ترامپ روز ۸ ژوئیه با «ایرفورس وان سابق» ترکیه را ترک کرده است.
در آنکارا، ترامپ در برابر دوربین‌های تلویزیونی سوار ایرفورس وان قدیمی، هواپیمای غول‌پیکر جت، شد. اما به گفته مقام آمریکایی و بر اساس مطالب تأییدکننده‌ای که واشنگتن‌پست بررسی کرده، دقایقی بعد به‌طور مخفیانه با یک کامیون پذیرایی فرودگاه ــ از همان نوعی که معمولاً برای بارگیری غذا و دیگر ملزومات پیش از پرواز استفاده می‌شود ــ به هواپیمایی کوچک‌تر، یک C-32A نیروی هوایی، منتقل شد.
به گفته این مقام، در نتیجه ایرفورس وان، با حضور خبرنگاران و برخی کارکنان کاخ سفید در داخل آن، نقش یک «طعمه» را ایفا کرد.
متن کامل ترجمه فارسی گزارش
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77810" target="_blank">📅 04:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/scmVS5lo5NbOjWO6f_dCHchtWKXRLe3R1l1u9ZuZk4OlXW8_ADxD7uRwSySeAw3KRm8Li-I2apvadq_JGrpmxqQEmXj7kI-WXBsHRGT5FReKS82pDHSa5wlkfmsiKR797JnKUtCAl49h8M9NnbCDlpl-nuXLvM8F7qdW1DfBVXwBLD4yh7NJ7cEjbY53TGDX7cyMpvjkIlYiLoN7pDDDmvKdxcos-1Hftxh0ZjOBTpg4b4SztJmjrgN0wbO-DPkTaHtnnaejdzyHX9Jjfq1oBcasodFcEy0mIyEleoRrkIG75v6Lcdzt9f01OUbdAGvK6e_F0ewywX5KDPlkqSCKuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا بار دیگر نموداری را که نشان می‌دهد ارزش ریال در ایران در دوره دوم ریاست جمهوری او سقوط کرده ‌است، منتشر کرد. این نمودار نشان می‌دهد که ارزش یک میلیون ریال از یک دلار و یازده سنت آمریکا به ۵۳ سنت کاهش یافته و به «داخل زباله» رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77809" target="_blank">📅 04:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni-1vhKS_cOohztN_DdOShHQen3l5So7d3PHpwYuoaiDyuAhNN6oZYofRisbWICV9mqGUwTWzW1F-stbfte6psgBp_x-X4mIqEvRt7af9dkkjyvkhm2N3HDCvtNsRfn4aK5oHOWIjUkgNujiiJCwZuZlBc53jwxkIU7b9mWRtFL3HQPh713UTUwwpBRqNMx62lOacWvxA93kbML4fZ4TxXqmYu4rqbWeBC5DM8-6ODy9GcnUxPEv47WQs1cGBKRWo5EH7EjjAmQ_ip6jcuIoDYfQhmgvNawYAEc2NvGK3SKUKwe2bYOjEWfzLwpGj1Z5Ws3gJwgrUJozWs7Vbz-slQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «آکسیوس»، آژانس بین‌المللی انرژی اتمی به‌زودی مواد هسته‌ای باقی‌مانده در یک سایت مخفی در سوریه موسوم به «سایت ۹۹» را پس از توافق‌های محرمانه دولت ترامپ با اسرائیل و سوریه، از این کشور خارج خواهد کرد. این مرکز که در زمان رژیم بشار اسد برای نگهداری کیک زرد و بقایای رآکتور هسته‌ای «الکبر» استفاده می‌شد، پس از سقوط اسد به شدت تحت نظر اسرائیل قرار داشت و حتی ارتش اسرائیل برای جلوگیری از دسترسی به آن، ورودی‌های سایت را بمباران کرده بود. اگرچه این مواد برای ساخت سلاح هسته‌ای کافی نیستند، اما مقامات آمریکایی و اسرائیلی بیم آن را داشتند که در ساخت «بمب کثیف» و آلوده‌سازی منطقه‌ای مورد استفاده قرار گیرند.
براساس این گزارش، در ماه‌های اخیر و پس از مشکوک شدن اسرائیل به تحرکات حکومت جدید سوریه و احتمال مداخله ترکیه، تل‌آویو تهدید به حمله مجدد کرد، اما دولت ترامپ با مداخله به موقع و وارد کردن آژانس بین‌المللی انرژی اتمی به ماجرا، مانع از تشدید تنش و بروز بحران نظامی جدید شد. در نهایت، سه هفته پیش توافقی میان دمشق و آژانس به امضا رسید تا این مواد خطرناک به صورت ایمن بارگیری و منتقل شوند. مقامات واشنگتن این موفقیت دیپلماتیک را نشان‌دهنده رویکرد موثر دولت ترامپ در تعامل با حکومت جدید سوریه و حل‌وفصل بحران‌های پیچیده مانده از دوران اسد می‌دانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77808" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=sSJQFOuq6reWA5MNTW0MYiUSQrf9s-mQJG0FLwdx_PIp-uvzUfEDRHyIHBNimCeqhtRoiDF_zzGwfyOv5NHseSulQ7DGEytFjO_d18pt8u6Ybaril44BGOFAJf0kue34NhnGUcKdvT6D5IgSx5fnomYqfCOqx3jUcncaMKiRxY7hFcmoqQdfdTPqGvIQwGD31ueYYUitqP8ZB4aCsWJkRBqKE5IdZR6gGq8ICQ5Cbus4q4fGc409iJKWHBZFJy_EHCp1EI10wlP7mPj4gAq9kDycOu7DPuk1RBLcQKwy-EtRGGtQfiRm3plOBbBwnYeTytrzGKVMVhPXclSej4-GHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=sSJQFOuq6reWA5MNTW0MYiUSQrf9s-mQJG0FLwdx_PIp-uvzUfEDRHyIHBNimCeqhtRoiDF_zzGwfyOv5NHseSulQ7DGEytFjO_d18pt8u6Ybaril44BGOFAJf0kue34NhnGUcKdvT6D5IgSx5fnomYqfCOqx3jUcncaMKiRxY7hFcmoqQdfdTPqGvIQwGD31ueYYUitqP8ZB4aCsWJkRBqKE5IdZR6gGq8ICQ5Cbus4q4fGc409iJKWHBZFJy_EHCp1EI10wlP7mPj4gAq9kDycOu7DPuk1RBLcQKwy-EtRGGtQfiRm3plOBbBwnYeTytrzGKVMVhPXclSej4-GHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز دوشنبه در گفتگو با خبرنگاران در کاخ سفید با تاکید بر تسلط نیروی دریایی ایالات متحده بر تنگه هرمز گفت: «تنها نیرویی که در حال حاضر بر تنگه هرمز تسلط دارد، نیروی دریایی ایالات متحده است. ما محاصره‌ای برقرار کرده‌ایم که خطاناپذیر و مانند یک دیوار فولادی است.»
رئیس‌جمهوری آمریکا با بیان اینکه اجازه رفت‌وآمد کشتی‌ها بر اساس تصمیم واشنگتن انجام می‌شود، افزود: «ما اجازه ورود کشتی‌ها به ایران را نمی‌دهیم و آن‌ها اجازه ورود به تنگه برای رفتن به سمت ایران را ندارند، اما مسیر برای دیگران باز است.»
او همچنین با اشاره به پاک‌سازی مین در این آبراه راهبردی تصریح کرد: «ما تنگه را مین‌روبی کرده‌ایم و ۱۰۰ درصد بر آن تسلط داریم. آن‌ها ممکن است مشکلاتی ایجاد کنند، اما ورشکسته هستند و هیچ پولی ندارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77807" target="_blank">📅 00:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X97SfD64y51ghkDewL3HwVLo1v6pC77S_6BawShIPz25DFKMztUm-8fVnPygL9uB-r4W5O78uFsvz9QUg0Jd9tXx3gA2sTPVP_K9fg2j6yQjuEKjWH40rFay8xhnXi0SkvhNm1OE02mmuZ_PyBiy-S-acWqm-tN7y5Q52Y8BWbOynwv-VKHvOHFWLt2JiTOp_xJy0igl6FVxbqu8zNisb_MyQInug0F2pobEGZ2OHmOsLCrOlhN425I9iL7_4jZ6uW0Luu6UXXFklMwylotTq8uW_7utdwSDUqJyFDUn4eaE2NJIzjAAWBu6Jj4x7sPskrPl8VnaKIqHLid3ApN3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه ۱۹ مرداد و پس از مطرح شدن موضوع پرداخت غرامت بین ایران و آمریکا و کمرنگ شدن امیدها برای بازگشایی تنگه هرمز حدود ۵ درصد افزایش یافت.
ایران اعلام کرده که آمریکا باید تحریم‌های اعمال‌شده علیه تهران را لغو کند و برای بازگشایی این آبراه حیاتی، چند شرط دیگر را نیز بپذیرد. در مقابل، دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت ایران باید بابت «تمام افرادی که کشته یا به‌شدت مجروح کرده است» غرامت بپردازد.
قیمت هر بشکه نفت خام برنت در پایان معاملات با ۴ دلار و ۱۷ سنت، معادل ۴.۹۹ درصد افزایش به ۸۷ دلار و ۷۲ سنت رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز با ۳ دلار و ۹۵ سنت، معادل ۵.۰۵ درصد افزایش، در قیمت ۸۲ دلار و ۱۳ سنت در هر بشکه بسته شد.
درصد افزایش قیمت هر دو شاخص نفتی، بالاترین میزان از هفتم مرداد بود.
هر دو شاخص نفتی هفته گذشته بیش از ۷ درصد کاهش یافته بودند؛ زیرا امیدها به نزدیک بودن ایران و عمان به توافقی که می‌توانست به بازگشایی تنگه هرمز منجر شود، افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77806" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FcMao1FWd-hmGLywgeWTcpEoHa-n2AdEJudyQfAwtr8cBSbYKn4jVAL2Ic8y_X1JivT69zAmwcvhAuaxjvDfdYTTCzVCB6edrpOmND01uznXf1a_cRc_iQ7jahksIPqReRGFhHCtJ7K0dMyaTp5jqQLTDLBjEIG7jlTEcZ6KM2Gqgx5Wuw5mOkkDNQ1ySq4HByyPpp1azWfH5B1mbuCBzMb2kLq_vnOkstuvgzkj_IimHqQn7gyLanrgevxzcBy9GCiHym86Dzma5nZ2Yptox76Nu9RM0A9SHA9Vf67tcTlUaAMxZSAHm10lnqZTw8J1n1EwBn5G_xvZVRRTmN9U0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست تازه ترامپ در ادامه متن یک ساعت پیش:
همچنین، در ارتباط با مذاکرات با ایران، ایران باید مسئول خسارت‌ها و مرگ‌ومیرهایی باشد که برای مردم لبنان، سوریه، یمن و غزه به بار آورده است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77805" target="_blank">📅 21:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77804">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUanenaJocriIisy0E7NOAGcccMZt6jqc5i4ahPtaZwV_XI73hhdPj_5-1MoAUmRYGEzo2fzHOnd1bA_fKzcumubhJFefwDDnuA5U7gSJZJyzrK-dnRdJU-9gsurQwJGx1cI4sFz_YhLmBd8T2rirzzZkMoIrfafuyNVZmukcxh0PunUaZAkrm6NStc6Nppt7RHjPOOXviDJc8yNV42H8dinSRrn66YdzCN6uF8popc9no332ZfNIL0uUNiuNsBheW9ht3qehSYa8beuoY80A4qyZEVHWCh5RWS-PkIMiV1Ztx0Tk-Mp_iUPbeM4dXdoISVCu4HGzt-5v5xgVg9vHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در مذاکرات موضوع پرداخت غرامت به ایران مطرح نشده، جمهوری اسلامی به خانوده‌های کشته‌شدگان غرامت بدهد
ترجمه ماشین:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج‌ماهه اخیر به آن‌ها وارد شده است (درگیری‌ای که به این دلیل آغاز شد که، آن‌ها
سلاح هسته‌ای نخواهند داشت
)؛ با اینکه این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما ایده جالبی است، چون حالا من نیز به همین ترتیب از ایران غرامت مطالبه می‌کنم؛ بابت همه افرادی که با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد ــ که به آن‌ها شهرت دارند ــ کشته یا به‌شدت زخمی کرده‌اند؛ اقداماتی که در ابتدا تحت رهبری ژنرال سلیمانی انجام می‌شد، از جمله بابت خانواده‌های کسانی که در ناو «یواس‌اس کول» کشته شدند، و هزاران نفر دیگری که در نبرد جان باختند.
علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه رسد به ۵۲ هزار نفری که در پنج ماه گذشته کشته شده‌اند.
به نمایندگانم دستور داده‌ام که این موضوع را قاطعانه در تک‌تک مذاکرات آینده مطرح کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77804" target="_blank">📅 20:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iw26J-CFVoNLDwS7lEifEMCgNc9khuEpPz7r2drQrNq-WDdoJPmjzrMyU3fny_kGEgKC0NNc6HuX_335wzNBCZPWicTAMruYUl1_4x2IL5qRo7YobglldtNr4komIQEiRvmxj4ErBhM-SlAnoRa-CyxNWF2JUuIo8NiMAyna4Mxdq2Ewr0_0efA2tz8HNVqAIXkvpmrDwkpi3SkJUtlAqxvhD48qXIPbU67DDsSDkht0o0myyuGi6y4pQKnSDddJKDc2oahTdMltd-yrMz_oHJATHf1bX9eI_FxUvY4ix1dhWftJif36nbvYmiY2HK8f00ti3TxUSAiatDwB5SpK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احکام منسوب به مجتبی خامنه‌ای برای انتصاب شش فرمانده ارشد نظامی؛
بازگشت رسمی حسین طائب به قدرت
دفتر رهبر جمهوری اسلامی روز دوشنبه ۱۹ مرداد خبر داد که مجتبی خامنه‌ای احکام انتصاب شش فرمانده ارشد نیروهای مسلح را صادر کرده و خواستار آمادگی برای «عملیات تهاجمی پرقدرت» علیه آمریکا و اسرائیل شده است.
بر اساس احکام‌ منسوب به مجتبی خامنه‌ای، علی عبداللهی که فرمانده قرارگاه مرکزی خاتم‌الانبیا بود، به عنوان رئیس ستاد کل نیروهای مسلح و کیومرث حیدری به عنوان جانشین رئیس این ستاد معرفی شده است.
رئیس قبلی این ستاد عبدالرحیم موسوی بود که ۹ اسفند سال گذشته در نخستین دقایق حملات آمریکا و اسرائیل کشته شد و ستاد کل نیروهای مسلح ایران در حدود پنج ماه گذشته بدون رئیس به کار خود ادامه می‌داد.
موسوی تابستان سال گذشته جایگزین محمد باقری، رئیس پیشین این ستاد، شده بود؛ باقری خرداد سال گذشته در حملات اسرائیل در ابتدای جنگ ۱۲ روزه همراه با شمار دیگری از فرماندهان ارشد نظامی جمهوری اسلامی کشته شد.
مجتبی خامنه‌ای در حکم صادر شده برای عبداللهی خواستار «تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیا» شده که به گفته او «تدبیر» آن در زمان رهبری پدرش آغاز شده بود.
او همزمان با انتصاب عبداللهی در سمت ستادکل نیروهای مسلح برای فرمانده جدید قرارگاه خاتم‌الانبیا حکمی صادر نکرده است.
احمد وحیدی که از آغاز جنگ و در پی کشته شدن محمد پاکپور، فرمانده‌ کل سپاه پاسداران شده بود، روز دوشنبه بر اساس حکم رهبر جمهوری اسلامی درجهٔ سرلشکری و حکم فرماندهی این نهاد قدرتمند نظامی، امنیتی و اقتصادی را دریافت کرد. او پیش از آغاز جنگ ۴۰ روزه، جانشین فرمانده‌کل سپاه بود.
احمد وحیدی از اعضای ارشد و تندرو سپاه پاسداران سابقه فرماندهی نیروی قدس سپاه پاسداران را دارد و به اتهام دست داشتن در انفجار مرکز یهودیان، آمیا، در آرژانتین از سوی اینترپل تحت تعقیب است.
او به جز مناصب نظامی، در دولت ابراهیم رئیسی، رئیس‌جمهور سابق ایران، به مدت سه سال وزیر کشور بود.
در حکمی که به نام مجتبی خامنه‌ای برای احمد وحیدی صادر شده است، رهبر جمهوری اسلامی خواستار «ارتقاء مستمر و همه‌جانبه‌ توانمندی‌ها به منظور بازدارنگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن» شده است.
بر اساس حکمی جداگانه، مصطفی ایزدی نیز مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفته است.
مجتبی خامنه‌ای در حکم دیگری علی عظمایی را به عنوان فرمانده نیروی دریایی سپاه منصوب کرده و او جانشین علیرضا تنگسیری شده که فروردین ماه در جریان جنگ ۴۰ روزه کشته شد.
مجتبی خامنه‌ای حسین طائب، رئیس پیشین سازمان اطلاعات سپاه، را نیز به عنوان فرمانده سازمان بسیج معرفی کرده است.
از طائب که کار امنیتی را از وزارت اطلاعات آغاز کرد و سپس کنار گذاشته شد و سپس در سپاه پاسداران نهاد اطلاعاتی موازی ایجاد کرد، به عنوان یکی از اعضای حلقهٔ امنیتی و سیاسی قدیمی اطراف مجتبی خامنه‌ای یاد می‌شود؛ حلقه‌ای که سابقهٔ آن به بیش از دو دهه پیش باز می‌گردد.
محمد سرافراز، رئیس اسبق صداوسیما، دربارهٔ نقش پشت‌پردهٔ مجتبی خامنه‌ای در تصمیم‌سازی‌های سیاسیِ مقام‌ها، سخن گفته است. او که خود در مقطعی عضو این حلقه بوده، از ارتباط مستقیم مجتبی خامنه‌ای با حسین طائب یاد کرده و گفته او به گزارش‌های امنیتی طائب علاقه‌مند بود.
او در تیرماه ۱۴۰۱ از سازمان اطلاعات سپاه کنار گذاشته شد، اما بر اساس گزارش‌ها یکی از چهره‌های مهم و نزدیک به مجتبی خامنه‌ای به‌شمار می‌رود.
مجتبی خامنه‌ای در حکم خود برای حسین طائب گفته چند مورد را «مورد انتظار» خود خوانده که یکی از آنها «تقویت شبکه‌ی اطلاعات مردمی، افزایش مهارت‌ها و آموزش‌های لازم توأم با بصیرت‌افزایی و بهره‌گیری از فناوری‌های نوین برای مقابله‌ی مردم‌پایه با تهدیدات دشمن» شده است.
او همچنین خواستار تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت حامیان جمهوری اسلامی که از ابتدای جنگ ۴۰ روزه در تجمع‌های خیابانی حکومتی شرکت می‌کردند برای «حفاظت از انقلاب اسلامی» شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77803" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77802" target="_blank">📅 18:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77800">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0943082a05.mp4?token=PlH1vnuGOsgRqJDVX-MVQGSkTlh1K3wzQjAr1XR5J3ms4XOIB8X-mTtvAM2Q0xrXXUc5KB-rwftGmqolwBTC-7JwouE22UgAdeez8Eojy0CxIup0oxIWTGoGpfyrz4QMPk8KX4kMVRfo1vbMNSm7e327CEzX95DNvBMFjxXQPjKm1lsJJXeoxRLGDKa8asqwPOQ8kfR1kFqMAJqTYZj98xL7GBuwYBboBHesLArlv6xnl2xgPO1YFifn2HbNWERmZDeN_HjjPXxNXBlc6vm4WHZxsH-RpGgVv--kBSsbFjSGDI5_0tCGGe7aQphSPbuDw6MwgYrV0tUgkZruhaefDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0943082a05.mp4?token=PlH1vnuGOsgRqJDVX-MVQGSkTlh1K3wzQjAr1XR5J3ms4XOIB8X-mTtvAM2Q0xrXXUc5KB-rwftGmqolwBTC-7JwouE22UgAdeez8Eojy0CxIup0oxIWTGoGpfyrz4QMPk8KX4kMVRfo1vbMNSm7e327CEzX95DNvBMFjxXQPjKm1lsJJXeoxRLGDKa8asqwPOQ8kfR1kFqMAJqTYZj98xL7GBuwYBboBHesLArlv6xnl2xgPO1YFifn2HbNWERmZDeN_HjjPXxNXBlc6vm4WHZxsH-RpGgVv--kBSsbFjSGDI5_0tCGGe7aQphSPbuDw6MwgYrV0tUgkZruhaefDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز دوشنبه ۱۹ مرداد اعلام کرد دیدار اخیرش با مجتبی خامنه‌ای، رهبر جمهوری اسلامی، «حدود هفت ساعت» طول کشیده و به گفته او «از هر دری گفتیم».
مسعود پزشکیان در گفت‌وگو با تلویزیون حکومتی ایران گفت: «تقریباً حدود هفت ساعت خدمت ایشان بودیم و دربارهٔ تمام مسائل کشور توانستیم گفت‌وگو کنیم».
از این دیدار عکس یا صوتی منتشر نشده است.
پزشکیان در ادامه درباره وضعیت جسمانی مجتبی خامنه‌ای اعلام کرد: «از نظر وضعیت سلامت کاملاً سالم بودند. کسی که می‌تواند هفت تا هشت ساعت بنشیند و بحث کند، نمی‌تواند از نظر سلامت مشکلی داشته باشد. بسیار راحت حرف‌های ما را گوش می‌دادند و بحث می‌کردند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77800" target="_blank">📅 17:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAwHxINNstIUp-F2W4aJdAqFxTj57hWbcap8jjzk0uAbCTtzemKJs7g6MqF_8yZzHYjBygGxU0noJS2r_FfQK-olTwtbvau_YBADY_vF3U3HkNATKbXCi48crh2N6MZhqjnEFafZ0UyzVjdbpJhZvYhSUra_5M9GZY-MDzHnJPJ1giObmlBQDEC9Uua3uVRqOJIJuExRXZ8Wi1iBhw7ptPk4Zi2F6VfEsWTYGndmf8JKNKcyACbXL5a-qzHTqzX9wa8DD_Yu47I59vN4deYwGAwcJibax158wulDSY6Mrz6aYTpNxgpc9T5GXvuZChEstU16G8nolazcZVlJCo_m4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، یک کولبر ۲۵ ساله بامداد دوشنبه۱۹مرداد۱۴۰۵، در پی تیراندازی نیروهای نظامی جمهوری اسلامی در منطقه مرزی «هنگه‌ژال» شهرستان بانه جان خود را از دست داد.
خبرگزاری هرانا به نقل از کردپا، هویت این کولبر را «محمد توحیدپنا»، ۲۵ ساله، فرزند عثمان و اهل روستای «وزمله» از توابع بخش سرشیو شهرستان سقز اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77799" target="_blank">📅 17:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CxQdEOjB0ZiyKLqgYKXKow6dQ5TUFhmAuPnxlARPUmIwkCTAR2dA2IuZllHB36YDY3ahQUdlX6zMgo3Op-VIQxk8-VMqFnAs-vtAEcWl79IRN6GoGPwlDxC97kft2I_QD7kl7cT-5_zPuWcwEqFPWQNgeRKVOlU_eJtEZXNVzWhxVT1RkXBsTEaSxGTSLetcJLmRxRvoZk-1EDivoA9GxcJInuwMNVCietR48rmWdOipE8jQ15N1hvcsu_LaYlyUw66M4GgtOT6lqHR6o9LNEUEDV6XKsO7egVAZ3jMhTAP58Shb2v6obtQGz9kuGpqe2ZCIBT6mHCwNHVDFQp-77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، یکشنبه بعد از ظهر به وقت شرق آمریکا با انتشار نموداری در شبکه اجتماعی تروث سوشال، به کاهش ارزش پول ایران واکنش نشان داد و نوشت: «۵۱ سال رفتار بد!»
realDonaldTrump
در تصویر منتشر‌شده، با عبارت «ایران هیچ پولی ندارد» تاکید شده است ارزش یک میلیون ریال از حدود یک دلار و ۱۱ سنت در سال ۲۰۲۵ به نزدیک ۵۳ سنت در سال ۲۰۲۶ کاهش یافته است. ترامپ توضیح دیگری درباره منبع آمار این نمودار ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/77798" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KlXujDgt8e_DEJePCcXTI2Qr_XswVDiPT72p6RL8829hfz0158HYeIadmIV74jJJmsfJcNsbsUCQVLGS3TAy7mfIt0hiBEvoqarROdm5DFfUhGyKaYqHlx8dNmd3BV5JuafSEE-wypIjygZKQXgKrAOtaeo458W2T_WUaaIpfu2C_HKQ7C76a8K5QfuqFYZDP78SXe5J_P52q8oXvmoOT2NBRDKrmvnFzkfh0lbek-hgIlg8Qu2T6QPl1_0X8mlqtNj04VX8MifBgXKh_qyCBFLx3iA1mkWMd1Bo0KEFD7riHGKRK2h9UYhsRZ2MOVZMeW_6cba7-37XI6lNQq4OFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a0SHgfNBa5ZdTWbf6R4mSdGd-WrzOJYSn5hiTgqM-tUJY9sGJmXEkUkJ8XMtjI2ea7STfZD732q2T7_kEfYvJJ5W3T5K61TGJllQUS84q1bjxD7ZCRB-zZ-r98P5re90wr4GPPqDXKcDdaqEL_vgFDB_HygCxYnRxnMKWFsVU8YtTBcWpVCxz64TH97HPZJLFRaJaoyRXEngGooCrbWKVgFA4QoqzvoJ7jIQseYFcDmcouOK5YIeVcUtlZpvIPf5lFpPMtLzYnSjzKiGTQ8BHaIDbISzIpLZoSQlfPKahLKsl6ZZWnOon-PAZNxxOQZB1Om4FmjVegSVLh7PrXwCxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در بحبوحه گمانه‌زنی‌ها درباره استعفای محمدباقر ذوالقدر از دبیری شورای عالی امنیت ملی، روز یکشنبه ۱۸ مرداد ماه، پیامی منتسب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در خبرگزاری حکومتی تسنیم منتشر شد که در آن محسن رضایی به عنوان «نماینده رهبر» در «شعام» (شورای عالی امنیت ملی) معرفی شده است.
در ادامه این پیام مکتوب، بدون اشاره به استعفا، از محمدباقر ذوالقدر «تشکر» شد.
این خبر در حالی منتشر می‌شود که از دو روز پیش اخبار غیررسمی درباره استعفای محمدباقر ذوالقدر از مقام دبیری «شعام» و جانشینی محسن رضایی،‌ منتشر شده بود.
خبر انتصاب رضایی در شعام، صبح یکشنبه در خبرگزاری‌های رسمی ایران منتشر و کمی بعد در بسیاری از آنها
حذف شد
.
آخرین گزارش‌ها از فعالیت ذوالقدر به عنوان دبیر شعام، مربوط به پیامی منتشر شده در روز شنبه است که بازگشایی تنگه هرمز را به پذیرش ۶ شرط جمهوری اسلامی از سوی آمریکا منوط کرده بود. پیامی که بازتاب گسترده‌ای در رسانه‌های بین‌المللی داشت و تلاش‌ها برای بازگشایی تنگه هرمز را با ابهام‌هایی مواجه کرده بود.
@
VahidOOnLine
🔥
رجا نیوز نوشته:
در اعلام بدون تاریخ این حکم نشانه‌هایی است برای اهل اندیشه...
🔄
آپدیت:
کانال خامنه‌ای نوشته به ذوالقدر پست مشاور سیاسی  رهبر جمهوری اسلامی داده شده:
📝
انتصاب دکتر ذوالقدر به عنوان مشاور سیاسی رهبر معظم انقلاب
💬
رهبر انقلاب اسلامی در حکمی آقای دکتر ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔻
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
✏️
بسم الله الرحمن الرحیم
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر
باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید.
✍️
سیّدمجتبی خامنه‌ای
🔄
و در نهایت حکم دبیری رضایی صادر شد:
معاون ارتباطات ریاست جمهوری:
محسن رضایی دبیر شورای عالی امنیت ملی شد
🔥
اما بخش جذاب ماجرا
محمدباقر خرازی
است.
او پیشاپیش گفته بود ذوالقدر می‌رود و محسن رضایی جایش را می‌گیرد.
درست درآمدن خبری چنین مشخص، همه ادعاهای خرازی را ثابت نمی‌کند؛ اما حالا دیگر دشوارتر می‌توان گفت او از پشت پرده قدرت هیچ خبری ندارد،حتی اگر خودش مدعی باشد کلیپ‌های جنجالی‌اش را هوش مصنوعی ساخته است.
@
pourostadv
🔥
امیرحسین ثابتی (نماینده انتخاب شده برای مردم تهران در مجلس شورای اسلامی) علیه پزشکیان با عنوان «علی الاصول ۲»:
پزشکیان مقابل خواسته مجتبی (رفتن ذوالقدر و آمدن رضایی) ایستاده بود.
علی الاصول ۲؛ انتشار حکم محسن رضایی توسط رهبرانقلاب
با آشکار شدن حکم نمایندگی رهبرانقلاب برای محسن رضایی در شورای عالی امنیت ملی، یک مساله دیگر آشکار شد و آن اینکه مدتها پزشکیان به عنوان رئیس این شورا در مقابل این خواسته رهبر انقلاب (رفتن ذوالقدر و آمدن رضایی) ایستادگی می‌کرده است.
به لطف خدا، تقریبا همه چیز برای مردم آشکار شده و دیگر کسی فریب "همه امور با رهبری هماهنگ است" را نمی‌خورد و اتفاقا مردم فهمیده‌اند کسانی که تحت پروژه وفاق و با چوب وحدت، میخواهند مردم مطالبه‌گر را سرکوب کنند و مقابل دوربین همه چیز را گردن رهبری بیندازند، در عمل خلاف نظر ایشان را عمل می‌کنند.
آقای پزشکیان! حرکت در مسیر رهبری با حرف زدن نیست، دست فرمان‌تان را تغییر دهید تا مردم تغییرتان نداده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77795" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dBLRLPueF61TCce1Quz2qB9QxuJLjxCk_W_P31Wzc1bxj2G-GPmiH0vefP-mSOIOhBL4TBv-kCpttd9A6z2PVvtQeDv1atdrGB6KDjaOYYT-m1naii2Alk33Agc1jZ5EJ17TolvNwZrg77Qn7Db1E3Jes5tOwaWflHa2uBLoatErh4oIFtpQwLWJvJhqvhrUEC62ZT2O95Wv36k8PRfjx4xFCmSKYlbSDy2Sn6PCApq14PQGJemfuL6ECFRo4Ztc6b35giW4uh7Abl2DTnjjxKyKJW9X4kH6J2P4YJHJS1Cz06O1A92m09cwP8Y5X2pxY-XJCTtsOzdThKNtSVzphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس: درباره ایران «داریم قضیه را کم‌سروصدا پیش می‌بریم»
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، روز یکشنبه نشان داد که آماده است اجازه دهد فشار اقتصادی بر ایران افزایش یابد — به‌جای آنکه دستور یک حمله نظامی تازه را صادر کند — حتی در حالی که این کشور همچنان در برابر آمریکا سرپیچی می‌کند.
چرا مهم است:
تنها یک هفته پیش، ترامپ در آستانه صدور دستور بازگشت به عملیات رزمی گسترده بود. اما او در گفت‌وگو با اکسیوس هیچ تهدید نظامی تازه‌ای مطرح نکرد.
▪️
ترامپ همچنین از اینکه ایران اعلام توافق با عمان برای بازگشایی تنگه هرمز را به تأخیر انداخته است، هیچ خشم یا نارضایتی‌ای ابراز نکرد. ایران روز شنبه فهرست تازه‌ای از خواسته‌ها را برای اجازه عبور کشتی‌ها از تنگه مطرح کرد.
ترامپ چه می‌گوید:
ترامپ در یک تماس تلفنی کوتاه گفت: «داریم قضیه را کم‌سروصدا پیش می‌بریم.»
▪️
«ما فقط یک‌جورهایی، نیم‌بند با آنها مذاکره می‌کنیم. فقط داریم ایران را تماشا می‌کنیم، با آن تورم عظیمش و این واقعیت که هیچ پولی ندارد.»
▪️
او تأکید کرد که ایران از نظر اقتصادی «در وضعیت بسیار بدی» قرار دارد و پولی برای پرداخت به نیروهایش ندارد. ترامپ گفت محاصره دریایی آمریکا بحران اقتصادی حکومت ایران را تشدید کرده است.
▪️
در عین حال، ترامپ گفت با کاهش قیمت نفت به اندکی بیش از ۷۵ دلار در هر بشکه، مصرف‌کنندگان آمریکایی فشار کمتری از جنگ احساس می‌کنند.
▪️
ترامپ درباره کش‌وقوس با ایران گفت: «درست می‌شود. همیشه درست می‌شود. مثل یک بازی شطرنج است.»
اصل خبر:
توافقی برای تنظیم تردد در تنگه هرمز میان ایران، عمان و آمریکا مذاکره شده و چند روز است که در انتظار نهایی‌شدن قرار دارد.
▪️
بر اساس توافق جدید، ایران کنترل بخشی از تردد در تنگه را به دست می‌آورد — چیزی که پیش از جنگ در اختیار نداشت.
▪️
میانجی‌های قطری و پاکستانی مطمئن بودند که توافق روز چهارشنبه اعلام خواهد شد، اما از آن زمان چشم‌انداز آن رو به افول گذاشته است.
▪️
مقام‌های آمریکایی همچنین می‌گویند اختلافات درون حکومت ایران رو به افزایش است. یک جناح به رهبری مسعود پزشکیان، رئیس‌جمهور، به‌شدت نگران فروپاشی اقتصادی است و معتقد است ایران باید با آمریکا به توافق برسد. جناح دیگری به رهبری احمد وحیدی، فرمانده سپاه پاسداران انقلاب اسلامی، هرگونه امتیازدهی را رد می‌کند.
وضعیت فعلی:
محمدباقر ذوالقدر، رئیس شورای عالی امنیت ملی ایران، روز شنبه شروط تازه‌ای را برای بازگشایی تنگه مطرح کرد — افزون بر شروطی که در توافق عمان درباره آنها مذاکره شده بود.
ذوالقدر در بیانیه‌ای گفت
برای بازگشایی تنگه، آمریکا باید:
▪️
«هرگز با هیچ زبانی ایران را تهدید یا به آن توهین نکند.»
▪️
«جنگ علیه ایران و متحدان ایران در لبنان، غزه، یمن و عراق را برای همیشه پایان دهد.»
▪️
محاصره دریایی را لغو کند و نیروهای نظامی را از اطراف ایران خارج کند.
▪️
او همچنین خواستار پرداخت کامل غرامت خسارات جنگ، لغو همه تحریم‌ها و آزادسازی تمام دارایی‌های مسدودشده ایران شد.
▪️
تا چند هفته پیش، این خواسته‌ها پیش‌شرط دستیابی به یک توافق هسته‌ای بودند. اکنون ایران آنها را صرفاً به‌عنوان شروط بازگشایی تنگه مطرح می‌کند.
▪️
یک دیپلمات از یکی از کشورهای میانجی گفت بیانیه ذوالقدر بازتاب‌دهنده کشمکش سیاسی درون حکومت است.
پشت پرده:
مقام‌های آمریکایی گفتند ترامپ یک هفته پیش متمایل به ازسرگیری عملیات رزمی گسترده علیه ایران بود، اما متقاعد شد که فعلاً تنش را کاهش دهد.
▪️
یکی از این مقام‌ها گفت ادامه درگیری به حکومت ایران اجازه می‌داد از مواجهه با پیامدهای جنگ، خسارت‌های واردشده به زیرساخت‌ها و بحران عمیق اقتصادی ایجادشده اجتناب کند.
▪️
این مقام آمریکایی گفت وقتی ایران درگیر جنگ نیست، ناچار می‌شود با واقعیتی تلخ روبه‌رو شود که هیچ راه‌حل واقعی برای آن در دسترس ندارد.
▪️
در عین حال، این مقام آمریکایی گفت هر شب حدود ۸ میلیون بشکه نفت با هماهنگی ارتش آمریکا از مسیر جنوبی تنگه هرمز از خلیج فارس خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
موضوعی که باید زیر نظر داشت:
جی‌دی ونس، معاون رئیس‌جمهور، روز شنبه به فاکس‌نیوز گفت: «این ماجرا تمام نشده است. واضح است که دیگر در ابتدای آن هم نیستیم. ما وسط بازی هستیم و مجموعه کاملی از ابزارها — ابزارهای دیپلماتیک، اقتصادی و نظامی — را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77794" target="_blank">📅 20:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77793">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77793" target="_blank">📅 19:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTEZqC9Rxy0Zr2LFZYEIc2JBFyqeSme6Qowh6KWrnQXrbseQ7-XBlt12sM_4vWxcyorxfu9v2pA3Wx-q_A4W9aSkkHS-vv6BnD1S8eT97tcncmE36w7PAW3qaCQr7MmTE9pxRvNhUVzQTy5RQv0m7Am_Y-C2htwNvB-vlFLZASC5Y4XcOXN3Yd14V0lCfTWMm1A79agp0BJaCbpHYvQrAjym2SkE1rENEGAGR20bhjvra-igv1hlrAEbP2ZyX3EwTvDPsYmMb4U4sNz51d9x74kitpf1ppsWYM6DfyppzYEF1rm3xiUl2f5XyqP1BToWkRl4Z8Ie9kOIE_wBLczaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه اطلاع‌رسانی دفتر رهبر جمهوری اسلامی روز یک‌شنبه ۱۸ مرداد ۱۴۰۵ اعلام کرد پزشکیان هم‌زمان با آغاز سومین سال ریاست‌جمهوری خود با مجتبی خامنه‌ای «دیدار و گفت‌وگو» کرده است. خبرگزاری مهر و ایرنا و دیگر رسانه‌های حکومتی نیز این خبر را بازنشر کردند.
بااین‌حال، از این دیدار نیز هیچ عکس، فایل صوتی یا ویدیویی منتشر نشده است.
پزشکیان پیش‌تر نیز گفته بود پس از انتخاب خامنه‌ای به رهبری، با او دیدار کرده است؛ اما از آن ملاقات نیز سند صوتی یا تصویری منتشر نشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77792" target="_blank">📅 18:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77791">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lg8AqO3DclDDcMYrAX7pSwAdRFHr4LsMM7mE9vRGTYO_Wn79LP_TF1olpO3vnAeFUg4klRzgUktpRzbdWz8p5Q_RNwraaKUffw1U7qJ0FtFmHdhhWmwgYkyqspA4ftHVuURUZLAqYPXAjrh6jcRdTFVAiHuV9YFW02606WYReZZ5psckXwNw7MDD5sLYcdPi3c16gDiaM8-bEWy0XLTUCWI-acNNsENV-ROzClHGgdM_WvexaUhRicZgH227VZgg_szwJWvx72HvM06dA8GYib41LfUrshlsucQMVCXRUQ7HTDmE6i2gzagPDnqWM9rgElJU8DEgUBZ95-Gc9ddCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماری از رسانه‌های حکومتی یکشنبه ۱۸ مرداد از انتصاب محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، رهبر جمهوری اسلامی، به‌عنوان نماینده او در شورای عالی امنیت ملی خبر دادند، اما دقایقی بعد این خبر را حذف کردند.
خبرگزاری تسنیم، وابسته به سپاه پاسداران، به نقل از «شنیده‌ها» نوشت که با این انتصاب، محسن رضایی و سعید جلیلی دو نماینده مجتبی خامنه‌ای در شورای عالی امنیت ملی خواهند بود. تسنیم پس از چند دقیقه این مطلب را از کانال تلگرامی خود حذف کرد.
رسانه‌های مهر، ایسنا و جماران نیز خبر انتصاب رضایی را منتشر کردند و اندکی بعد مطالب خود را برداشتند.
انتشار و حذف این خبر در شرایطی صورت گرفت که در روزهای اخیر اختلاف‌ها در ساختار جمهوری اسلامی بر سر روند گفت‌وگوها با آمریکا، از جمله پرونده هسته‌ای و چشم‌انداز تنگه هرمز، افزایش یافته است.
@
VahidOOnLine
🔄
آپدیت: خبر شش ساعت بعد از حذف دوباره
منتشر شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77791" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=d8kxHU7MWI7H5wjdvavEDQ3x5CVS6fV-xIPzwAWx5zcWuUcVpn9imvOrdvoL-7dwNSRuVlidtld9mo1Ce_T3uuffUklJYhTC9WuzhuE2aT6fCxQXE-V5-puVI7ZgGGkddApR7KUfCzC6D5H6KaoYMZSO50I4lLtRkWncmaevUD13SMpxkgaBUP-RDrc3Cv-8UBQI5GTbcvZ2Y4RQtGqpbdB0eRyG-MCjNEt8H0aksDA-RPJjrD4RmhQKZ6Xu_C3LRpxOTtoFhhTqFWBT_K2edsAEXoZMrToCXdODUdgmknjBRvpdDJwUe_HgGJdHQge0MVLBatJ-N3eZ1-bHLsnUrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=d8kxHU7MWI7H5wjdvavEDQ3x5CVS6fV-xIPzwAWx5zcWuUcVpn9imvOrdvoL-7dwNSRuVlidtld9mo1Ce_T3uuffUklJYhTC9WuzhuE2aT6fCxQXE-V5-puVI7ZgGGkddApR7KUfCzC6D5H6KaoYMZSO50I4lLtRkWncmaevUD13SMpxkgaBUP-RDrc3Cv-8UBQI5GTbcvZ2Y4RQtGqpbdB0eRyG-MCjNEt8H0aksDA-RPJjrD4RmhQKZ6Xu_C3LRpxOTtoFhhTqFWBT_K2edsAEXoZMrToCXdODUdgmknjBRvpdDJwUe_HgGJdHQge0MVLBatJ-N3eZ1-bHLsnUrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در نشست روز یکشنبه کابینه، با رد صریح طرح ۱۵ ماده‌ای «شورای صلح» دونالد ترامپ برای غزه گفت: «اسرائیل طرح ۱۵ ماده‌ای را رد می‌کند. ارتش اسرائیل تا زمانی که حماس به‌طور کامل خلع سلاح نشود، هیچ‌گونه عقب‌نشینی انجام نخواهد داد.»
او با تاکید بر لزوم خلع سلاح واقعی حماس افزود: «منظور از خلع سلاح، شامل تمام تسلیحات سنگین، نیمه‌سنگین و سبک است؛ ما از یک خلع سلاح واقعی و نه فرضی صحبت می‌کنیم.»
نتانیاهو همچنین با اشاره به رایزنی‌ها با طرف آمریکایی خاطرنشان کرد: «ما در حال گفتگو با آمریکایی‌ها هستیم. آن‌ها ایده‌هایی دارند که برخی از آن‌ها برای ما قابل قبول و برخی غیرقابل قبول است. امنیت اسرائیل قابل مذاکره نیست و ما قاطعانه بر سر منافع خود ایستاده‌ایم.»
نخست‌وزیر اسرائیل در پایان تاکید کرد: «تا زمانی که من نخست‌وزیر هستم، هیچ کشور فلسطینی تشکیل نخواهد شد؛ نه در غزه و نه در کرانه باختری.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77790" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJmdVpHyREqUPo25HjNrKWeZbvVQqoH6qjClWYawH6xysxiOqiITIXsayqFbQF8DQb0aV2Nybk2zIQKSfQbyiAvPRyEj5VujH3aYq4TBpfoHWpiJfo_bMZeoCE1oOonFT6Dq7um0f5B-5pJltlFJ2t3RqR4EDkvz2CoQB9YTLRKCmbtbnUfikT-3Vbtt5t4EUp3gIF9wTxzo3ShpiwbPZZFsGvXV7JJXV54PtMcZteHLLsvghAy6CZiuIOnm4BqftzOdjBh3y-ptCYAg4P9nXCHhz0v2T6cfJaIBKCtvThHLWjGGFHFnuB44h6cZ1eIRtDglvKjrOHNMdeqRKBj-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان امروز منابع حکومتی درباره قتل مداحی که ۶ ماه به بهانه "دعوت به حجاب" مزاحم یک "دختر بلاگر" شده بود تا رفت سر قرار باهاش:
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شده بود اما ۴ روز پیش ویدیویی از پیکر آسیب دیدهٔ این فرد در یک کانال ضدانقلاب منتشر و در فضای مجازی دست به دست شد.
مرد گمشده مدتی قبل در فضای مجازی با خانم بلاگر جوانی آشنا شده و به او امر به معروف و نهی از منکر می‌کرده و می خواست حجابش را در پیج اینستاگرامی حفظ کند و به مسائل سیاسی نپردازد که در روز ناپدید شدن نیز این خانم بلاگر از او درخواست ملاقات حضوری داشته است.
تحقیقات کارآگاهان نشان می‌دهد زن جوان با طراحی قبلی و با دعوت از مرد سرشناس به محله خلوتی زمینه حضور وی را فراهم کرده و پس از رسیدن مداح جوان به محل قرار با تعارف خوردنی مسموم ابتدا مقتول را بی هوش کرده سپس با همدستی 5 مرد او را به قتل رسانده اند.
خانم بلاگر در بازجویی ها گفت : من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و... من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند.
...
تحقیقات همچنین نشان داد این افراد پس از قتل، اقدام به فیلمبرداری از صحنه جنایت و جنایت بر میت کرده و فیلم تهیه‌شده را در ازای دریافت پول برای  شبکه‌ معاند منافقین ارسال کرده‌اند چون تصور می کردند برای این فیلم ها که در آن بسیجی ای کشته می شد پول خوبی می توانند دریافت کنند.
بررسی‌های کارآگاهان در این مرحله نشان داد مقتول با ضربات متعدد چاقو به قتل رسیده و پس از مرگ، با آتش زدن جسد جنایت بر میت رخ داده است. متهمان همچنین درباره نحوه انتقال و سوزاندن جسد در بیابان‌های اطراف پرند توضیحاتی را در اختیار تیم تحقیق قرار داده‌اند.
براساس ادعای افراد بازداشتی، یکی از متهمان که به عنوان عامل اصلی جنایت معرفی شده، ضربات اصلی را به مقتول وارد کرده و پس از آن سایر افراد نیز در این جنایت مشارکت داشته‌اند؛ با این حال، متهم اصلی پرونده پس از ارتکاب قتل متواری شده و تلاش‌های پلیس برای دستگیری او ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77789" target="_blank">📅 18:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PgEc3dSy_b3QBbhvFbZpisoOoaGG_OtcCV7In_cetOs_NgiJd5IzzsXEPn_eRUZL35jkNSLdse9aCvDw7x54NQtCkr4LOkpurNO2PRCTQ50DixvR_OdqTtRRAJF6esYWjkGleM1PoeOOyu9abEc4fekXwBhzPoMb34_GX4nTZYblwbpIw3rADM0MC-pGOPb7hxyTeq0o0V6ZECPuA80q2qEvyjcudhydIPt7YnkIamnXlHN8C-0vS9odfdKnlLa1UPyzDyN7eDguGzgeqrDS7vEQLPPPpcBtV4iumhe5QVIh322UHc1OabbmwYv3j9G1C4DEJAD1S3e_baPlYYmr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات حکومت ایران در عین اعلام پیشرفت در مذاکرات ایران و عمان درباره تعیین مسیر کشتی‌ها در تنگه هرمز روز شنبه، ۱۷ مردادماه، شرط‌های تازه و گسترده‌ای را برای باز شدن این آبراه مطرح کردند.
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه گفت تا زمانی که آمریکا به گفتۀ او «رفتارش را تصحیح نکند، تنگه هرمز باز نخواهد شد» و تأکید کرد این شورا «چه در جنگ و چه در مذاکره» از این موضع کوتاه نخواهد آمد.
او شش شرط را برای بازگشایی تنگه مطرح کرد که از جمله شامل پایان جنگ و حملات آمریکا به ایران و متحدان جمهوری اسلامی در لبنان، فلسطین، یمن و عراق، رفع محاصره دریایی، خروج نیروهای نظامی آمریکا از پیرامون ایران، پرداخت کامل خسارت‌های جنگ، لغو تحریم‌ها و آزادسازی دارایی‌های مسدودشده ایران است. ذوالقدر همچنین خواستار پایان تهدیدهای آمریکا علیه ایران شد.
ساعاتی پیش از آن نیز سخنگوی سپاه پاسداران اعلام کرده بود که بازگشایی تنگه هرمز اساساً «ارتباطی به مذاکرات ایران و عمان ندارد» و تنها در صورتی انجام خواهد شد که آمریکا «شرایط ایران» را به‌طور کامل بپذیرد.
@
VahidHeadline
شرایط شورای امنیت ملی ایران با یادداشت تفاهم با آمریکا چه تفاوتی دارد؟
انتشار شش شرط ایران برای بازگشایی تنگه هرمز، چشم‌انداز بازگشایی این تنگه در کوتاه‌مدت را در ابهام بیشتری فرو برد.
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، گفت که این شورا چه در جنگ و چه در مذاکره «هرگز کوتاه نخواهد آمد.»
شورای عالی امنیت ملی ایران زبان صریح‌تری در مقایسه با تفاهمنامه با آمریکا به کار بسته است.
در یک مقایسه سریع با یادداشت تفاهم، ایران این بار به شکلی صریح خواستار پرداخت «بی‌کم و کاست خسارت‌های دو جنگ» شده است، موضوعی که در نص یادداشت تفاهم‌ دیده نمی‌شد.
پذیرش آمریکا تقریبا ناممکن است چرا که آن کشور را در موضع «متجاوز» قرار می‌دهد و به زبان سیاسی هم به «شکست» تعبیر می‌شود. در عین حال، پرداخت غرامت، تبعات حقوقی دیگری هم به‌عنوان آغازگر جنگ و همچنین اقدامات غیرقانونی بین‌المللی دارد.
این در حالی است که دونالد ترامپ گفته بود که خسارات حملات ایران را از پول‌های بلوکه شده ایران می‌گیرد. این موضع آمریکا عملا نفی ششمین شرط ایران برای آزادسازی تمامی‌ دارایی‌هایی‌هایش است.
شرط دوم ایران هم اگرچه به بند نخست یادداشت تفاهم می‌ماند، با یک تفاوت بنیادین. در تفاهمنامه دو کشور تنها از پایان دائمی تخاصم در ایران و لبنان نام برده شده بود. این بار اما جمهوری اسلامی خواستار پایان دائمی جنگ در «فلسطین، یمن و عراق» هم شده است.
به نظر می‌رسد شش شرط ایران نه موضوع مذاکره که موضع این کشور است.
پیش از این، اگرچه مقام‌های ایران اعلام کرده بودند که توافق با عمان به معنای بازگشایی تنگه هرمز نیست اما رئیس‌جمهور و مقام‌های وزارت خارجه تا حدی این موضوع را به بازگشت آمریکا به تفاهمنامه و تعهد عدم نقض آن مشروط کرده بودند.
حالا به نظر می‌رسد شورای عالی امنیت ملی مطالبات را افزایش داده است، اقدامی که حتی اگر با هدف فشار بر آمریکا و امتیازگیری در مذاکرات باشد، مخاطرات خود را دارد و مشخص نیست که واکنش آمریکا چه خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77788" target="_blank">📅 18:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_7HvPzgRBQISyugbAHXPguhk48rwX6v1hXJhp3239fROA3kqRe27ODE3uGUKRqANX2Uayc4T2j9k5pm48-4PgzKHQbtuJyk7iSd_KwJbR2nC_R9YbaMjQm68b4aoyHq_vopY-fjGpXex6r3g0EdGpPBcLkKmoAv3AjsbMAFIMctirHMLGE6j0HlcJHTIAnWF3njk6WlsPVoCgPlX1lCPWn_zpQDAwJdde_cOW85JbG6cM2E__dFw_EUpmeTgWpdxIj4wimEp2vtLU91ixs4XJKoonpWmuDNQBY0h5mglDbEsryOHjIpQA8uMcg4y_zWZDh1MYl0FlU4aewwg6EaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام رسول رضایی، شهروند ۲۸ ساله اهل فریمان و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در دیوان عالی کشور تایید شده است. او پیش‌تر از سوی دادگاه انقلاب مشهد به اتهام «محاربه» به اعدام محکوم شده بود.
خبرگزاری هرانا، روز یکشنبه ۱۸مرداد ۱۴۰۵، گزارش داد، رسول رضایی که در حال حاضر در زندان وکیل‌آباد مشهد محبوس است، پس از تایید حکم اعدام در دیوان عالی کشور در معرض اجرای این حکم قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77787" target="_blank">📅 17:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=rwqf73CmYsMKfEK8WhngiDmx1RkHWHnMlYcdw2YHRMMp9PYt4JdNW4JrrvRuNu-B4cbS1VgpZh_BOmnPpXJmpfhd4kAr3LD1D4dnscqVrPeyZmiaHd2hOGP2Dg_9tVW5k3dJkkmD8kFq1iuLwDaHM6iruu8HENHQZy_CKndRQlZZrYwUg33Ilfef6xgbyY230PXAOPgWAHdZz-NMdwH9ohTT8_Wovmvv-bxtGPZQR40ZsilanGY8ZSixHpdbBE9WrNTBOx1aYBlGR9gkNwdzhpwNUonMuaC6q9APmIXsM4WS1a8AO5Gx6RUGesXo2eNrNkwcWr9Pew2ivFkMEIrE_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=rwqf73CmYsMKfEK8WhngiDmx1RkHWHnMlYcdw2YHRMMp9PYt4JdNW4JrrvRuNu-B4cbS1VgpZh_BOmnPpXJmpfhd4kAr3LD1D4dnscqVrPeyZmiaHd2hOGP2Dg_9tVW5k3dJkkmD8kFq1iuLwDaHM6iruu8HENHQZy_CKndRQlZZrYwUg33Ilfef6xgbyY230PXAOPgWAHdZz-NMdwH9ohTT8_Wovmvv-bxtGPZQR40ZsilanGY8ZSixHpdbBE9WrNTBOx1aYBlGR9gkNwdzhpwNUonMuaC6q9APmIXsM4WS1a8AO5Gx6RUGesXo2eNrNkwcWr9Pew2ivFkMEIrE_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی جی‌دی ونس، معاون رییس‌جمهوری آمریکا با فاکس‌نیوز، بخش مربوط به ایران با تشخیص و ترجمه ماشین:
🔻
ونس: ... ما با ایرانی‌ها در حال گفت‌وگو هستیم.
تلاش می‌کنیم میزان نفت و گازی را که از تنگه هرمز عبور می‌کند به حداکثر برسانیم. در حال حاضر بیش از هر چیز روی همین متمرکز هستیم. فکر می‌کنم می‌بینید که قیمت نفت امروز به حدود ۸۰ دلار در هر بشکه کاهش یافته و گاهی کمی پایین‌تر هم می‌رود.
بنابراین فقط تلاش می‌کنیم مطمئن شویم آنچه را که از این درگیری نیاز داریم به دست می‌آوریم.
اگر به عقب برگردید و به یاد بیاورید که اینجا چه کرده‌ایم، برنامه هسته‌ای آن‌ها را نابود کرده‌ایم، نیروی نظامی متعارفشان را نابود کرده‌ایم و آنچه را می‌توان توانمندی‌های نظامی نامتقارنشان نامید، به‌شدت کاهش داده‌ایم.
و اکنون می‌خواهیم ببینیم آیا حاضرند آن نوع تغییرات بلندمدتی را انجام دهند که برای داشتن رابطه‌ای بهتر با ایالات متحده ضروری است یا نه. اگر هم حاضر نباشند، اشکالی ندارد.
ما همچنان هر فشاری را که بتوانیم وارد می‌کنیم و تلاش می‌کنیم تا جای ممکن نفت و گاز بیشتری از خاورمیانه به جریان بیندازیم تا آمریکایی‌ها بتوانند از قیمت پایین‌تر بنزین و انرژی بهره‌مند شوند.
این همان موازنه ظریفی است که باید برقرار کنیم.
آخرین چیزی که در این باره می‌گویم، کیلی، این است که همیشه سعی می‌کنم به مردم یادآوری کنم که واقعاً هنوز وسط بازی هستیم. این ماجرا تمام نشده است. دیگر در ابتدای کار هم نیستیم؛ وسط بازی هستیم و مجموعه‌ای کامل از ابزارها—دیپلماتیک، اقتصادی و نظامی—را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.
کاملاً مطمئنم که به آن نقطه خواهیم رسید، اما هنوز تا حدی وسط بازی هستیم.
🔺
کیلی مک‌اننی:
ایرانی‌ها هم از راه‌های مختلف این پیام را داده‌اند که می‌خواهند کنترل خود را بر تنگه هرمز محکم‌تر کنند. بنابراین در یک توافق فرضی، وضعیت قابل قبول در تنگه هرمز چه خواهد بود؟
🔻
جی‌دی ونس:
انتظار ما این است که همان میزان نفت و گازی که پیش از آغاز این درگیری از خلیج [فارس] خارج می‌شد، دوباره از آن خارج شود.
ایرانی‌ها به ما گفته‌اند که قرار است همین کار را انجام دهند. کل ائتلاف کشورهای خلیج [فارس] نیز همین را می‌خواهد.
اما می‌دانید، ما اعتماد نمی‌کنیم؛ راستی‌آزمایی می‌کنیم. به حرف مردم نگاه نمی‌کنیم، به عملشان نگاه می‌کنیم.
می‌بینید که برخی افراد در داخل ساختار ایران درباره گرفتن عوارض صحبت می‌کنند. ایرانی‌ها به ما گفته‌اند هیچ برنامه‌ای برای گرفتن عوارض از عبور و مرور در تنگه هرمز ندارند. اما باز هم خواهیم دید در عمل چه اتفاقی می‌افتد.
آنچه طی حدود یک هفته گذشته در جریان بوده این است که ایرانی‌ها و کشورهای خلیج [فارس]، به‌ویژه عمان، درباره چگونگی تضمین عبور و مرور امن گفت‌وگو کرده‌اند.
البته یک مشکل این است که ایرانی‌ها در آغاز جنگ تعداد زیادی مین کار گذاشتند. بنابراین آنچه اکنون واقعاً داریم روی آن کار می‌کنیم این است که چگونه می‌توان سازوکاری برای تردد ایجاد کرد تا کشتی‌هایی که عبور می‌کنند بتوانند با ایمنی عبور کنند.
این طبعاً شامل مین‌روبی هم می‌شود. همچنین شامل تعهد ایران می‌شود که به کشتی‌های تجاری شلیک نکند.
آن‌ها به‌شدت آسیب دیده‌اند. می‌خواهند این ماجرا تمام شود.
سؤال این است که آیا قادرند—آیا نظامشان قادر است—چیزهایی را که لازم است ارائه کند تا ما راضی باشیم و احساس کنیم آنچه را از این رویارویی نیاز داشتیم به دست آورده‌ایم.
این هنوز مشخص نشده است، اما فکر می‌کنم طی چند روز گذشته مقداری پیشرفت کرده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77786" target="_blank">📅 18:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkNjnGvwlSJXsUxbdQhnS1aAQuv7LkzZAq4XmB5vKGknQBbWuIFn4Apskk2Te-yg6op5Ox2SJnCAGHVim8EfMVwTRrPm7xK1pehkC1ECF8JYdVnRVXloCGMM6bE4wDc4fhdhDe55tMFPTadwdP5X1rNKap2phg_1603bSvAIpkSABWtAkwupM5kMP844gGel8szQJYDofM0wj8j9Cuk2OcycHLl2F1T1LxE59hpL7eFg3pgEZCKY5nQL5zSvfcrjwBFi0u1T7AlqxE89GwK54AZ6GpG5sqOGL-q8x3NMM3S8so-gxStMnhtzagmxN2ewlNUrt3QFr5cUGH78JsIw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از هدف قرار گرفتن یک شناور در تنگه هرمز، در فاصله حدود ۱۸ مایل دریایی شرق خصب در عمان، خبر داد. هم‌زمان، امارات متحده عربی اعلام کرد یک نفتکش متعلق به شرکت ملی نفت ابوظبی، ادنوک، هنگام عبور از تنگه هرمز هدف حمله موشکی قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77785" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naDLP3njjP6NjEdOPnSFBKV7jvezDanpvz9FgLiBELAJGwdsOr9WnME5ezGTg8p1vHqHzg6-QdPFTVq1HDRpSMsMupIWg4HpCJYla86EvEeX-BrRqI3LMbftSmBh5DurkJydmX8fGI52ME8gz4Snr95dQ85gz60zA5fkvrhUwthUKLFKzhbkuv8aaAdcPmNHGWAqlkjnPJ-CcAJAP2Y9peVQydPDFjr095__DmDgygfsRJw6B6tvmjwcHFIkI0OkRZ0qefC-_86c9RvFlJyOFCMW3EHqj_bNCG_KFgeCk-ihPcsQhgZOrTN-9fdWM2mpLC1U59f5JGQTPIAbZvzRMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه ۱۷ مردا ماه، با انتشار پیامی با تشریح شروط جمهوری اسلامی برای بازگشایی تنگه هرمز، تاکید کرد تا زمانی که ایالات متحده آمریکا رفتار خود را تصحیح نکند، این آبراه راهبردی مسدود خواهد ماند.
دبیر شورای عالی امنیت ملی تصحیح رفتار آمریکا را مشروط به تحقق ۶ بند اصلی دانست و اعلام کرد آمریکا باید تهاجم و جنگ علیه ایران و متحدانش در منطقه از جمله لبنان، فلسطین، یمن و عراق را متوقف کند، محاصره دریایی را برچیده و نیروهای نظامی خود را از اطراف ایران خارج کند.
او همچنین پرداخت کامل خسارات جنگ‌های تجاوزکارانه، لغو تمامی تحریم‌های غیرقانونی، آزادسازی بی‌قید و شرط دارایی‌های مسدودشده و پایان دادن به تهدیدها و توهین‌ها علیه ملت ایران را از دیگر شروط اساسی ایران برشمرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77784" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj6UTnPGp7dmrvUUpgWZankSEr2YBiwoy96-Y5blUFXVNI8FeO0MTD_iKq-JdCS-yGHO16fNM9FsaZ_Imbmz5jpP2Y1NHhJDb2iudYg6NBTP0X72FZbsa6IYgviCXAuDYXMB2-zZjAWjbLYHKvsNwwTCrUkgBXR0C0n8tts1heaiLd6hMsQgFgMB1Bsk6Q497kvSFWB8u-3IuTGKWKiYIXaNyhou2VN140FURt4VKBpfwACKbdQsUHYLXG-RFCeJwtN-Fd7R5yyxCbThmZ_47K5rqiP0KBLG3Oevd5im1lbzZHV4VhUe_Le4oFblIIjF6QshIrxutrxluQuWfuK5kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه سازندگی روز شنبه به نقل از یک منبع آگاه اعلام کرد که مسعود پزشکیان، رئیس‌جمهور ایران، با استعفای محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، مخالفت کرده است.
در روزهای اخیر برخی رسانه‌ها از کناره‌گیری ذوالقدر و انتصاب محسن رضایی به عنوان دبیر جدید شورای عالی امنیت ملی خبر داده بودند.
این روزنامه که ارگان رسانه‌ای حزب کارگزارن سازندگی است، در گزارش خود به نقل از منبع آگاه نوشته خبر استعفای دبیر این شورا «صحت ندارد» و پزشکیان به او گفته است که با «قوت و قدرت» به کارش ادامه دهد.
با این حال سازندگی تأیید کرده که ذوالقدر پیش‌تر استعفای خود را ارائه کرده بود «اما این استعفا با مخالفت مسعود پزشکیان روبه‌رو شد و در نتیجه او همچنان در سمت خود باقی ماند».
محمدباقر ذوالقدر در پی کشته شدن علی لاریجانی در اسفند ماه گذشته در جریان حملات آمریکا و اسرائیل، به عنوان دبیر شورای عالی امنیت ملی منصوب شده بود.
علاوه بر برخی رسانه‌ها، محمدباقر خرازی، روحانی تندرو نزدیک به بیت علی خامنه‌ای، نیز هفته گذشته در یک سخنرانی خبر استعفای ذوالقدر و جایگزین شدن محسن رضایی را اعلام کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77783" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-LNieFZxDnY7ZVD7SzIA9eVfarJVg1wuY55htO5VxqFzq1P72O0rH-Dm4RsYs3mQCL84Hnyw4ELWyBUBPaX3n054Ywn9B5FpxHWqUlAPsQoozLEEjt0ccJNqVCziRfFWubFT3HHokpkpKJyfc5RameevQedVgZ0FQNsmif_yb89ikxEvWLz_CNrtEEisO71F9CHib1uMyXBLf4G9wxWj2LIGsU33wbAfJ96zoLdE4ffdJVzq3pIArPLZZ3B-tgocxQaMxC4iuiifIWI4W53cgOkDJajW0JYNQDHkiwe95rdTetgWuLjgKL_YigefPFRiydCSrDkFLkzWPTbVNDLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌ها در مورد حمله موشکی روز شنبه نیروهای مسلح جمهوری اسلامی به نفتکش اماراتی در خلیج فارس، وزارت خارجه امارات متحده عربی با انتشار بیانیه‌ای ضمن محکوم کردن شدید این حمله اعلام کرد، این حمله تلفات جانی نداشته است.
وزارت خارجه امارات، روز شنبه ۱۷ مرداد ماه، در بیانیه‌ای این حمله را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل متحد دانست؛ قطعنامه‌ای که بر آزادی کشتیرانی و مخالفت با هدف قرار دادن کشتی‌های تجاری یا ایجاد اختلال در مسیرهای دریایی بین‌المللی تاکید دارد.
وزارت خارجه امارات همچنین اعلام کرد هدف قرار دادن کشتیرانی تجاری و استفاده از تنگه هرمز به‌عنوان ابزاری برای فشار یا باج‌گیری اقتصادی، «اقدامات دزدی دریایی» از سوی سپاه پاسداران محسوب می‌شود و تهدیدی مستقیم برای ثبات منطقه، مردم آن و امنیت انرژی جهان است.
امارات از مقامات تهران خواست این حملات را متوقف کند و به‌طور کامل به توقف تمامی اقدامات خصمانه پایبند باشد. ابوظبی همچنین خواستار بازگشایی کامل و بدون قید و شرط تنگه هرمز برای تضمین امنیت منطقه و ثبات اقتصاد و تجارت جهانی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77782" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vp4HZ6GoOFBpGUD1Nnw-GJxu03ajoMyZVPmNSJxm0G8XSaVr9agtpYKgmEwyzg-C7NS9U87cvJ1psQHcX3KCkXWSz5_Wzlj2gIFFJVBnwnUoRjdrl_an_ogwGqPS4KhU2gJfqVn7Eiy1nSQejfIckDkLaXBxIOTrViwGKB2PA-XcbLRmAFNUM_q-XLxZ_8vEPzdRShVqCdbwRbAe4POmdeBlS6hmZSVuiP7GXYGySHLtOiEKuR1bAVeNM1iij6KaL88ndmDkAVPl3r9MJkWe4FLFTL49Ru_kfD3wcvpT46mu7jzUBP45-bUgljBVfk9J9tO4jayndIpvs3e3QY1pQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/se7K1bcnCcSQhUilroIs5nE3x2rPi9adENoi6lbL4Yuap4gd_8hbgGsLXcFMY8lfZ1qtfUP9vmMaDk5IdPyyrRAZ7QIK1-8OBX4_RVREnwRaarqFtJTf4shNnciOazdH6pbR4aJ3VZ7JI6ByjaNhS54Aeryyf5rWqjTXxKz45JcfRE5D5pVjA0E3TDN6e2cLqkeawAy68IwlKqpLpOG8enrbYmjz_hIjJR5uu3ZZLVQLsz976liewWDp0-cOBnHLOrC5FAA1k6bANb9bnewlx6x_nTlskDdxo4xgQs06JxwA9SlMruTrrw1bs88mouhN0TDHxpdwFUufth_Y4_6FuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dq2q5p4WWjaF_CNbekEPZRUzDPjhwQqJgRSbEmoGgBVu4jJ-Ry3Wj1suVA37YuVLrCjB7zLaZq066QqJCZc8yBEUEcubiEqz8s9rt1T6tSmBG2f71yNnakXN_1S3d8LMKJoUgBcQsdibuIl9RlVQ52OaJRc-fwbt0F0Qczb7aMMyPmx4g1xFNPXd5C1KlB9n2llBrxRvcONd1XQc_UJhTv8atSxUCXua6LNs1tz9D4zMjGuWkF7sYOrWpn9UEbF9PG1X3cuF4NOSxorArvHzOVEd6fPFJhDEG2faYvXg8a3qcEkWyd4OvzfWTVWY36tAWf-3Nhg3-6aydBLnei3_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICITx89OL--2yljdIqeq3iuZ0sCbMEj-KQWgizP1nQF6mkoqRfN1ArfnWhAYqE9YSDQ9DiGBDWgs5GhY19H3MMSfaS2Py-1TiyapFmFDqpVtkV_dFxtdy-klxjoRpmCU_o0ScDbyFwtIfomJxqSG5yN_IoLvNZLn8pJ4BktAqlKNYZF6ZschsaPaQc36kxEytHwGtcpFc8s8PnkDwlMvRKsVtTkiPVLR1DpDn0TfG5-1VhkeN75hOzqIVGvDdI2Rd60Sz6Bfb_op0wPK_ewjAA9bPwFSwgR1Iz3AJVzIHy6haH3W95Zv2Dp-kqifZ86Q2OM3cvwTqKB0f37F4wWc8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9LLF9BHLUzOMpts3aiyFnvMw340fESTqJxT_8DQJu8rwsTprf1gBjW_T5HCOvC568O0qdfhL38oego3w-xOIflzianVW_1JPVOPxOuNiEWapVEdSqeDo6w8xPWV0ZemO9Z0Nep4H1o1AMFx7sZ91OpFIbkKDTcHI0kh4oyFzSOf5ufW7ZbU9Tx7-yv7C0CsZ5udwJfHpHnJXsJPfCaMtIACspotPJHBp4za2_UrQkqXOXqVBzieOoaqDedE-o5-b6vmHTxXNYSWfJQnyRVMJVB9OmxtnzuHqTdGN3XHzmIerDsvE_kM9gdA9Xv4QwSDvSYtSc8u9mnZmgiHgCCDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxnUTYU9BOWEoTchNceYBWP8NVq2ApL5czetghE-ZEnV9TdBhUsGGPUWFbpeR2loG776BUz2EvtQqvE_EDaYguagq0GHI0CP9EZtAKSiyZdwe6yxNeakUgA2ZjCSk3TN_28yxhvRVfiWN1LMI_cVMDW9J6B9X0fF2Vd_t3lSn9PTPWy4YvB3BmAmK1duZct5T7QU48PEkmE7tOVrrt6D0ffamJ-VaPjp0mXfqKgQkG8t-RNLbFUotOclQcQsxsNTBWZ1riGhB9CUetqDxkgqTAPLM5x9YMTV5q006MZj3lzTygu7Blk9pqk-GacAz2mMiRuCYHx3jVJ6rYvJoZvNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyk9CQaa9CYJDnrq1Fw80kQgry2olQo4htWlY9RSGYpntcPa37hFNcoMXjhI_sQXhVYT_HZW-ygT5tfz_CpMPzUGuR16RM4N3TV1t69PmblEYkIT5geeZOQ9NSnPLO5PICs4yG5Jx7Abfat1Cp04To7QkrS9FQ_OWAlzfOb7tAlI5AEMQ1nGJyXC52aVvNLi0lFy9PG-8tEbHFSOHVCcRMvCW4yyVMKSxSIU9zMPYKzlIguUHb3leVr8tcqFCWhSEBUf624icrmpkMyF6EGm4OAdy_Le2OiS35hoLnhANoHHGe6F6KjPGG0pao-YqLTGcYh-pEGen_TMUzHsQx4xgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی
قوه قضاییه روز شنبه اعلام کرد محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در پی اظهارات اخیرش به دادگاه ویژه روحانیت احضار شده و تحت تعقیب کیفری قرار گرفته است.
به گفته سخنگوی قوه قضاییه، با توجه به روحانی‌بودن محمدباقر خرازی، رسیدگی به اتهامات احتمالی او در صلاحیت دادگاه ویژه روحانیت است. او همچنین گفت خرازی «می‌تواند اتهامات متعدد امنیتی» داشته باشد و در صورت حاضر نشدن در دادگاه، برای او حکم جلب صادر خواهد شد.
@
VahidHeadline
در حاشیه ساختار قدرت در جمهوری اسلامی، همواره ردی از «خودی‌های دردسرسازی» پیدا می‌شود که مقام و جایگاه رسمی ندارند، اما آن‌قدر به حلقه‌های قدرت نزدیک‌اند که نمی‌توان حرف‌هایشان را نادیده گرفت.
نسبت خانوادگی، لباس روحانیت یا وابستگی به یک تشکل حتی کم‌نام‌ونشان، به آن‌ها امکان می‌دهد از تصمیم‌های پشت پرده خبر بدهند، مقام‌های حکومتی را متهم یا تهدید کنند و سخنانی بگویند که واکنش و تکذیب بالاترین سطوح قدرت را برانگیزد، اما خود در حاشیه امن قدرت باقی بمانند و پس از مدتی با ادعایی تازه برگردند.
محمدباقر خرازی بسیاری از این ویژگی‌ها را دارد.
روحانی بدون منصب حکومتی، دبیرکل تشکلی به نام «حزب‌الله ایران» که وزن و جایگاه واقعی آن در فضای سیاست ایران چندان روشن نیست، و عضوی از خانواده‌ای که با حوزه علمیه، دستگاه دیپلماسی و خاندان خامنه‌ای پیوند دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77775" target="_blank">📅 18:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-RbpDbLR5e2M1r_fOg6-lJDmbYbYuLafNRmja9gtbpysCO3wR6CXdexweUAhYhyXIlLqA5ivOKqNs54eNEPFQBYkSstWBvGgyHtdahFuzGtrn_1zFQiSkOjvUeieGI2mziuDHEfcCSx32DPKbu6BcGZdrIsyaByH8j2HC5Rd2isGMADgQLhFFRatw3BxC4ZFf_ktNZGBtadJCRHw42QdDX6lkpUnPmd-ySU6hifoZBD9MzufjM7hP6TXdhtW7DS0YYNPxPyPF_mDkn2H8XMYzSN9ZmIvhXAap8EIMkTMXLSrnQI3f_aXRq7FvwYjsSlFEDMoXQ5VHC5BkZ1oeE7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم روز شنبه ۱۷ مرداد از ربایش و قتل حمیدرضا رجب‌زاده، از مداحان حکومتی، خبر داد.
تسنیم به نقل از یک «منبع آگاه» گزارش داده است که رجب‌زاده چند روز پیش ناپدید شده بود و پس از آن، ویدیویی از لحظه قتل او برای خانواده‌اش ارسال شده است.
بر اساس این گزارش، پس از اطلاع از این حادثه، تحقیقات پلیسی و قضایی برای شناسایی و بازداشت عامل یا عاملان قتل آغاز شده است.
با این حال، تاکنون اطلاعات رسمی و دقیقی درباره نحوه ربایش رجب‌زاده، محل وقوع قتل، انگیزه عاملان، هویت افراد دخیل در این حادثه و جزئیات ویدیویی که برای خانواده او ارسال شده، منتشر نشده است.
@
VahidOOnLine
🔄
ادعای دقایق پیش تسنیم:
🔹
پس از ارائه اطلاعات جزئی از سوی خانواده وی درباره آخرین برنامه رجب‌زاده و مسیری که قرار بود طی کند، پیگیری‌های تجسسی صورت گرفت و نهایتا، خودرویی که رجب‌زاده برای آخرین بار سوار شده بود، شناسایی و مالک آن دستگیر شد.
🔹
این فرد که در ابتدا منکر هرگونه ارتباط با این ماجرا بود، نهایتا اعتراف کرد که با تحریک شبکه‌ای تروریستی در خارج از کشور، به همراه 4نفر دیگر اقدام به ربودن حمیدرضا رجب‌زاده کرده است. آنها در ادامه اقدام به شکنجه و قتل او کرده و تصاویری را هم برای خانواده او ارسال کرده‌اند.
🔹
به گفته این متهم، آن‌ها با وعده دریافت چند هزار دلار، اقدام به ربودن و قتل رجب‌زاده کرده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77774" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پست زلنسکی، ترجمه ماشین:
ما از سنای ایالات متحده و از همه کسانی که از اوکراین حمایت می‌کنند بسیار سپاسگزاریم. تصویب قانون تحریم روسیه و ایران، طرح لیندسی گراهام، قطعاً به افزایش فشار بر متجاوز کمک می‌کند تا این جنگ جنون‌آمیز روسیه علیه استقلال ما و مردم ما پایان یابد.
اوکراین قدردان
تمام
حمایتی است که ایالات متحده از اوکراین به عمل می‌آورد — از سوی هر دو حزب و تمامی مردم آمریکا. و اکنون، زمانی که پوتین آخرین امید خود را به موشک‌های بالستیک بسته تا جنگ را طولانی‌تر کند، و زمانی که ما برای یافتن موشک‌های پاتریوت به‌منظور دفاع از خود، با تمام توان وجب‌به‌وجب همه‌جا را می‌گردیم، هر نشانه‌ای در حمایت از حفاظت از جان انسان‌ها و پایان دادن هرچه سریع‌تر به جنگ، اهمیتی فوق‌العاده دارد.
فشار واقعی و قدرتمند آمریکا و تحریم‌ها علیه روسیه بیش از هر چیز دیگری کمک خواهد کرد. با هر گامی که برای افزایش فشار بر متجاوز برداشته می‌شود، دیپلماسی نزدیک‌تر می‌شود.
از همه کسانی که این را درک می‌کنند و از طریق
قدرت، صلح
را پیش می‌برند، سپاسگزارم.
ZelenskyyUa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/77773" target="_blank">📅 23:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
نیروهای مسلح قدرتمند ایران آمادگی، توانایی و اقتدار خود را در برابر گران‌قیمت‌ترین ارتش جهان به نمایش گذاشته‌اند.
وقتی مسلمانان در کنار یکدیگر بایستند، می‌توانیم با هر چالشی که از سوی بیگانگان بدخواه ایجاد می‌شود، رودررو مقابله کنیم.
وقت آن است که فقط به خودمان تکیه کنیم و برادری واقعی را در آغوش بگیریم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/77772" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرنگار اکسیوس:
یک دیپلمات از یکی از کشورهای میانجی به من گفت که تیم مذاکره‌کننده ایرانی در انتظار تأییدهای نهایی شورای عالی امنیت ملی ایران درباره توافق با عمان و ایالات متحده است. این دیپلمات گفت: «انتظار داریم این تأیید به‌زودی صادر شود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/77771" target="_blank">📅 21:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rAoO_FRwd8iEy9X4cbdnxicCnTRuBZyIJngtJaolpwIHCEIqy21E1VgGMLVDwkSXjv09RVIkC2SlEEOoLjw3d_puHQCYr_Wts3_RIpZdEwHYVXdp583CMThVXBowHfcWLz9MJ-Llzi-iS8b3kvt5rZ2fLJ9So6h0yxJgX3ynqFPtHt9uYWTk86QPhqI5tWoAur1y2BnOiN5_u1pVlEbutAt7XdCAgtyJ2PGxyKWhRnnBQF55PqsbOA4Lbp_Q6_jPbfrDLP_l8YiZW4PuUA6YPcRNdO_lKPO1rkCiYQ0UJIercC_tdhojBsmeAu0YXez5yg8Je0Mzi9NG0y2nEamcMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده آمریکا در گزارشی که روز جمعه ۱۶مرداد۱۴۰۵ منتشر شد اعلام کرد که «شبکه‌ای از صرافی‌ها و شرکت‌های پوششی مرتبط با جمهوری اسلامی» را هدف قرار داده است.
در بیانیه منتشر شده از سوی این وزارتخانه تاکید شده است که ایالات متحده در حال اخذ تصمیمات قاطع با هدف «قطع شریان‌های مالی» است که حاکمیت جمهوری اسلامی ایران را سر پا نگه می‌دارند.
این وزارتخانه در بیانیه خود نوشته است که این اقدامات با هدف برچیدن شبکه‌ای از صرافی‌ها و شرکت‌های صوری انجام خواهد شد که به ایران کمک می‌کردند صدها میلیون دلار را به‌طور مخفیانه از طریق نظام مالی بین‌المللی جابه‌جا کند.
در بخشی از بیانیه وزارت خارجه ایالات متحده آمده است که «تهران از طریق این شبکه‌ها به درآمدهای نفتی دسترسی پیدا می‌کرد، تحریم‌هایی را که با هدف مهار فعالیت‌های بی‌ثبات‌کننده‌اش وضع شده‌اند دور می‌زد و با استفاده از شرکت‌های پوششی، منابع مالی خود را پول‌شویی می‌کرد.»
هدف قرار دادن بانک‌ها، صرافی‌ها و افرادی که این شبکه غیرقانونی را اداره و تسهیل می‌کنند از سوی آمریکا چنانچه در بیانیه منتشر شده آمده راهی روشن برای اعلام آن است که «هر کس به ایران برای دور زدن تحریم‌ها کمک کند، با پیامدهای جدی روبه‌رو خواهد شد.»
وزارت خارجه آمریکا اقدامات انجام شده از سوی وزارت خزانه‌داری این کشور را نشانی بر تداوم سیاست «فشار حداکثری» دولت «دونالد ترامپ» علیه ایران دانست. سیاستی که بر «قطع منابع مالی مورد استفاده حکومت برای تهدید ثبات منطقه، حمایت از تروریسم و تقویت توانمندی‌های نظامی‌اش» تاکید می‌کند.
@
VahidHeadline
پیش‌تر:
وزیر خرانه‌داری آمریکا روز جمعه گفت که ممکن است «امروز یا فردا» توافقی با ایران برای آتش‌بس و باز شدن تنگه هرمز منعقد شود.
اسکات بسنت در گفت‌وگو با شبکه «۱۲ نیوز» با اشاره به وضعیت وخیم اقتصادی در ایران گفت: «فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد توافقی برای برقراری یک آتش‌بس ۳۰ تا ۶۰ روزه خواهیم بود و تنگه [هرمز] باز خواهد شد. قیمت انرژی هم باید کاهش پیدا کند.»
او با تأکید بر این که ایالات متحده هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست یابد، گفت تحت تاثیر عملیات نظامی آمریکا و اعمال تحریم‌های شدید علیه تهران، «آنها با تورم ۱۵۰ تا ۱۸۰ درصدی مواد غذایی مواجه‌اند و دیگر توان پرداخت حقوق نیروهای نظامی‌شان را ندارند».
بسنت همچنین درباره وضعیت زیرساخت‌های نظامی ایران گفت: «نیروی هوایی نابود شد، نیروی دریایی نابود شد و بخش بزرگی از موشک‌ها و مهم‌تر از آن، توان تولید موشک آنها از بین رفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/77770" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">#توافق_مکه
:
وزارت خارجه پاکستان در بیانیه‌ای اعلام کرد جمعه ۱۶ مرداد، پاکستان، ترکیه و عربستان سعودی، توافقنامه مشترک دفاعی امضا کردند.
توافق امضا شده تصریح می‌کند هرگونه حمله مسلحانه علیه هر یک از سه کشور، حمله علیه همه آنها تلقی خواهد شد.
در این بیانیه آمده است این امضای این توافق‌نامه «نشان‌دهنده تعهد سه کشور برای تقویت بیشتر امنیت جمعی آنها است.»
وزارت خارجه پاکستان همچنین در این بیانیه نوشت این توافق با هدف تقویت صلح، امنیت و ثبات در منطقه و فراتر از آن و برای دستیابی به آینده‌ای امن و با رفاه بیشتر تنظیم شده است.
همچنین رویترز به نقل از یک مقام ترکیه اعلام کرد «توافق دفاعی میان پاکستان، ترکیه و عربستان سعودی ماهیتی کاملا دفاعی دارد و هدف آن، ایجاد تعهد برای حمایت متقابل در زمینه دفاعی است.
این مقام به رویترز گفت: «این توافق علیه هیچ کشور یا طرف مشخصی تنظیم نشده و کشورهای دیگر منطقه نیز امکان پیوستن به آن را دارند.»
به گفته این مقام، این پیمان جایگزین یا لغوکننده هیچ‌یک از توافق‌های دوجانبه یا چندجانبه موجود میان کشورها نیست.
@
VahidOOnLine
ابراهیم رضایی، عضو كميسيون امنيت ملی و سياست خارجی مجلس شورای اسلامی، عربستان سعودی را به طور غیرمستقیم تهدید کرد که پیمان دفاعی مکه برای آنها امنیت به همراه نخواهد آورد.
رضایی در شبکه ایکس نوشت: «سعودی‌ها باید بدانند که توافق کاغذی با ترکیه و پاکستان برای آنها امنیت‌آور نیست، همان‌طور که سال‌ها شیردهی یکطرفه به آمریکایی‌ها برایشان امنیت نیاورد.»
او عربستان سعودی را به «گدایی امنیت» متهم کرده و به مقامات این کشور توصیه کرده به جای آن، سیاست‌هایشان را «اصلاح» کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/77768" target="_blank">📅 18:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=IXRWurbBXl6igMr_d-XaUfUaWxOTHDK9vJCrtwiJ8JU3dA7RzBtDifQe0HfeF2LmIFRlRGEB8Q6QTVi8Hl7NnRoJ834UxXrxRZQ-XHe9OVBKB1HTm8nn64o6xjC1TTmlqa3FNcSj-EwAfN7tut7J22BDFMA2BgQWvMIP_vvC00-9hWEH98EC7hgVjAmG26FbREv9ekD9qYH0a9bChULE5XKFS2qbo478GCuXmbl7QuV-irwz4U7s8_be2s3yvwxClpe56WL2mfnmoDPEnzR0dzsEDNUjaz7r-Xm1p0Su3oA-inXzPDkwD4AU4Ejinxu1hKZKvlTR1eaeq6qoqzwncw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=IXRWurbBXl6igMr_d-XaUfUaWxOTHDK9vJCrtwiJ8JU3dA7RzBtDifQe0HfeF2LmIFRlRGEB8Q6QTVi8Hl7NnRoJ834UxXrxRZQ-XHe9OVBKB1HTm8nn64o6xjC1TTmlqa3FNcSj-EwAfN7tut7J22BDFMA2BgQWvMIP_vvC00-9hWEH98EC7hgVjAmG26FbREv9ekD9qYH0a9bChULE5XKFS2qbo478GCuXmbl7QuV-irwz4U7s8_be2s3yvwxClpe56WL2mfnmoDPEnzR0dzsEDNUjaz7r-Xm1p0Su3oA-inXzPDkwD4AU4Ejinxu1hKZKvlTR1eaeq6qoqzwncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین:
🔺
خبرنگار:
و آقای رئیس‌جمهور، جمهوری‌خواهان اکنون بحث زیادی درباره قدرت خرید و هزینه‌های زندگی دارند. پیام شما درباره این موضوع در آستانه انتخابات میان‌دوره‌ای چیست؟
🔻
ترامپ:
سؤال خوبی است، اما پاسخ آن تا حدی ساده است. من بالاترین قیمت‌های تاریخ را به ارث بردم. بدترین تورم تاریخ کشورمان را به ارث بردم و ما کار فوق‌العاده‌ای انجام داده‌ایم.
قیمت نفت اکنون به‌سرعت در حال کاهش است. اگر به اوضاع نگاه کنید، تا ۷۵ پایین آمده است.
وقتی آن اقدام بسیار مهم را در جمهوری اسلامی ایران آغاز کردم، اقدام بسیار مهمی بود؛ چون آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. در غیر این صورت، تمام جهان منفجر می‌شد. ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. مسئله فقط ما یا خاورمیانه نبود؛ برای تمام جهان فاجعه‌بار می‌شد. چاره دیگری نداشتیم.
قیمت بنزین در بسیاری از نقاط، مانند آیووا، به کمتر از دو دلار رسیده بود؛ قیمت‌هایی که مردم سال‌ها ندیده بودند: یک دلار و ۸۵ سنت، یک دلار و ۹۵ سنت. سه‌شنبه در یکی از توقف‌هایم در آیووا، در یک محل قیمت ۱٫۹۵ دلار و در محل دیگری ۱٫۸۵ دلار برای هر گالن بود.
بر اساس هرچه می‌بینم، به‌محض پایان جنگ، خیلی زود دوباره آن روزها را خواهیم دید. فکر می‌کنم جنگ به‌زودی پایان پیدا کند. تصور نمی‌کنم آن‌ها بتوانند مدت خیلی بیشتری ادامه بدهند. بله، بفرمایید.
🔺
خبرنگار:
آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
🔻
ترامپ:
نمی‌خواهم بگویم که توافق حاصل شده است. تنگه در حال حاضر تا حدودی باز است. می‌دانید، چیزی داریم که «محاصره» نامیده می‌شود و نیروی دریایی آمریکا آن را هدایت می‌کند؛ ما آن را کنترل می‌کنیم.
اکنون کنترل آن با ماست، اما آن‌ها همیشه می‌توانند به چیزی شلیک کنند یا مینی در آب بیندازند. حتی اگر فقط یک مین آن بیرون باشد، اوضاع را به هم می‌ریزد؛ چون مردم نمی‌خواهند کشتی‌های میلیارددلاری خود را وارد منطقه کنند و تصادفاً با مین برخورد کنند.
اما فکر می‌کنم عملکردمان بسیار خوب است. خودم در مذاکرات دخیل هستم و فکر می‌کنم اوضاع خوب پیش می‌رود. ممکن است توافق حاصل شود؛ ممکن است به‌زودی باشد. بله.
🔺
خبرنگار:
آقای رئیس‌جمهور، درباره مهمات؛ شما شب گذشته نوشتید که آمریکا مقدار عظیمی مهمات دارد و وجود هرگونه کمبود را رد کردید. در عین حال، یک درخواست بودجه تکمیلی ۲۱ میلیارد دلاری برای پرکردن مجدد ذخایر وجود دارد. اگر کمبودی نیست، چرا این درخواست همچنان مطرح است؟
🔻
ترامپ:
چون همیشه به مقدار بیشتری نیاز داریم. منظورم این است که مهمات بیشتری لازم داریم.
ببینید، دولت بایدن مقدار بسیار زیادی به اوکراین داد؛ رایگان، بدون دریافت هیچ پولی. میلیاردها و صدها میلیارد دلار.
خوشبختانه من در دوره خودم ذخایر بسیار زیادی ایجاد کرده بودم. نیروهای نظامی را بازسازی کردم و مقدار زیادی تجهیزات و مهمات نیز در اختیارشان گذاشتم.
از بعضی انواع مهمات بسیار قدرتمند، ذخیره‌ای نامحدود یا تقریباً نامحدود داریم. در مورد بعضی انواع دیگر، وضعیت کمی محدودتر است و هر روز محموله‌های تازه دریافت می‌کنیم.
همان‌طور که می‌دانید، شرکت‌های دفاعی ما اکنون بیش از هر زمان دیگری در تاریخ کارخانه می‌سازند. برای موشک‌های پاتریوت، تاماهاوک و همه‌چیز کارخانه می‌سازند.
در عین حال، انواعی از مهمات داریم که ممکن است به آن اندازه دقیق نباشند یا در آن سطح ممتاز قرار نگیرند. نمونه‌های ممتاز را هم داریم و این موضوع را بسیار دقیق زیر نظر گرفته‌ایم. اما بعضی از انواع مهمات ما بسیار قدرتمند و بسیار خوب‌اند و ذخیره‌ای نامحدود از آن‌ها داریم.
بنابراین در وضعیت بسیار خوبی هستیم. بااین‌حال، همیشه مهمات بیشتری می‌خواهیم و باید مقدار بیشتری داشته باشیم. ممکن است مسائل دیگری پیش بیاید و ممکن است هم پیش نیاید. امیدوارم هیچ مسئله دیگری پیش نیاید، اما ما در وضعیت بسیار خوبی قرار داریم. واقعاً مقادیر عظیمی مهمات داریم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/77767" target="_blank">📅 01:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MdS5sIosibk805nJ9btIQUBxMdqeT2roPNidwDamUPUyBrF4_JsBUvxEXxQmjETtjCIuHQzjE5-WY6Gy77TjDQSnHF0x1QH5hVasq47JxapGzmfApvdr9aKsvGSDaQjLhHC10neWYzATDofxDoJWnXymCLyL_q0MXmiVd3CfrIggs6S5IJHIaCgGHB09rO8i4TQycEGK9sXKeuFmNePBPpfPKSQCy8rPPV52UItZ3E0TmHR8Sp3mbNyaqKWDiem-bnXNKKxQigjmt7B2yV29kjqlsABZ8zFztxJxuNoAtB1v96BiEmpRedE20FplNPG4_k1r6XXbSDySGG4G_RsRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی: سلام وحید جان  همین الان دو صدای بد انفجار شنیده شد قشم  سلام ساعت ۲۱ و ۴۳ قشم دو انفجار نزدیک شهر   سلام وحید جان الان قشم صدای دو انفجار بد اومد صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن  وحید قشم رو زدنننننننن [لطفا صداها…</div>
<div class="tg-footer">👁️ 488K · <a href="https://t.me/VahidOnline/77766" target="_blank">📅 23:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hh-XUC1FTsVDlsUs_1rSfn697x7sjdr4818GcZYsBS0OZ5USmWtHVFrL5mYlgmFkpkckXAaH3Jz_zfXNH1Sy9DKmqj3VPH4AjxyfKSVEyl5MuivjkgUjnPclJW3idGmshLSyYfdE9lo83bS-QIB-woaXLTHwww4w_Q1qs9IwJdV9KWc96b13Nnt6ZR3c7tDrRHjxd9rg4hrN07V4IpYkT4MFDPK_87xWSW_OBNqXkCiFFBrzJWxIAbH_2gpURwqt8ZUcGODlGk5RnvlXm6Kc0mHFKzxpNINXo1wRxPfjI5pEHxfcLZT54RhOKeiyFUij2-vGQchVt5O-cf2Hh7tXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
«حمله‌ای عظیم در راه است... صبر کنید، بی‌خیال؛ آنها می‌خواهند مذاکره کنند.»
این همان نمایش دیپلماسی است که مدام تکرار می‌شود.
استفاده از زورگویی، وعده‌های نقض‌شده و اخبار جعلی به‌عنوان اهرم فشار، راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتری نیاز نداریم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 473K · <a href="https://t.me/VahidOnline/77765" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
همین الان دو صدای بد انفجار شنیده شد قشم
سلام ساعت ۲۱ و ۴۳
قشم دو انفجار نزدیک شهر
سلام وحید جان الان قشم صدای دو انفجار بد اومد
صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن
وحید قشم رو زدنننننننن [لطفا صداها رو تفسیر نکنید]
۴ تا انفجاررررر
قشم هم اکننون سه انفجار
ساعت ۲۱:۴۱ قشم
دوتا انفجار یکیش خیلی قوی تر بود، اسکله بهمن بود یا کشتی‌های نزدیک اسکله
بندرعباس ۲۱:۴۳ دو سه تا صدای انفجار [که لابد همون قشم بوده.]
همین الان صدای ۴ تا انفجار اومد قشم
دوتاش خیلی شدیدو نزدیک بود
دوتاش خیلی دور بود
سلام وحید جان ساعت ۹ و ۴۲ دقیقه قشم دوبار صدای انفجار اومد ،نمی‌دونم چی بود ،خونه لرزید
ساعت ۲۱:۴۰ صدای ۲ انفجار شدید شهر قشم درب و پنجره ها لرزید
سلام وحید جان صدا سه تا انفجار تو قشم اومد دوتا شدید بود یکی انگاری دور بود
🔄
منابع حکومتی:
🔹
معاون امنیتی استانداری هرمزگان،: تاکنون هیچ‌گونه اصابت یا حادثه‌ای در جزیرۀ قشم و شهر بندرعباس گزارش نشده است.
🔹
بررسی‌های لازم توسط دستگاه‌های مسئول برای شناسایی منشأ صدای شنیده‌شده درحال انجام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/77764" target="_blank">📅 21:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U6pNlLOp7eIqBtNIQczn4NZvzheaiRymKF1Mv1CwbvZ0L6kFFl5MU_2oZzDzcz97ogzHpDUQOerLT88IEAuI7b8g3IP4FVHD8OzieQhqpkdLM_iL7fSlMFXSu7wQJ9PPJtE_0avfHk8GKkJsroR44M97Ku6vdghEq2Q3BjedsINwCOFU1Heb-7R7lu5Uzcmfm938mID0RUtTmirl5vjYz_YGF5tmm8YDfWuWNzjEmlaJZIpVWaEmXvr5rQh_aHC1AdZxQqRCTSs0hew2dCMCLvPulHt1cLVLgVfsGaKdUOXfYgPgOJrwbjCTgb0vDV7f26pzYL5ytczVbnY1mbaGIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اخبار جعلی، طبق معمول، در حال انتشار شایعاتی دروغین و کاملاً بی‌اساس است. من از عملکرد پیت هگست به‌شدت راضی هستم. همه‌چیز فوق‌العاده بوده است؛ از جمله حمله ما به ونزوئلا که نتیجه آن در کمتر از یک روز حاصل شد و به ما امکان داد نیکلاس مادورو، یکی از بدترین جنایتکاران در سراسر جهان، را به دست عدالت بسپاریم!
همین‌طور اوضاع ایران، که برای هرگز اجازه ندادن به آن برای دستیابی به سلاح هسته‌ای به‌شدت درهم کوبیده شده، بسیار خوب پیش می‌رود! پیت در میان نیروهای نظامی از احترام بسیار بالایی برخوردار است و اصلاحات عظیمی انجام داده؛ از جمله برچیدن سیاست‌های تنوع، برابری و شمول (DEI) و افزایش جذب نیرو به سطوحی تاریخی.
این شایعه را «واشنگتن کام‌پوست» ــ یکی از بدترین رسانه‌های این حرفه ــ به راه انداخت، آن هم با وجود اینکه به آن‌ها گفته بودیم گزارششان کاملاً دروغ است. در واقع، من واقعاً معتقدم این «گزارش‌گری» جعلی آن‌ها خیانت‌آمیز است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/77763" target="_blank">📅 20:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eODyYxffUxuEj9mGWP6nQEUI3sZk4vleXSSafBTmXM-rchFhZVsMO-Dc206Irc3wP0dsYfX8J4snZCqTdvVde02-uqJ_0Hs5tg6K6Y5utcWkZnqVue0-Em4WLZMqB9VNi82TB7-Hg0qhq5Xk4rguSKVPzGC4DKl4a7Max9hL7c5-470DEEtQ-j65gFLFKkJtFbGB7owqh32TQTsq33ziQ7khXoG2B3ck5xy-2HwsbXeebQgQ3LTrdg8RDOnauCqrLoejTXY0hr3ufjcrXPqDbyd-C9HonnZ07G5wWKXrFOVCU-jjggjIBk2AraXTNMynkYE6G2x9UUJuBinOX23_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
ایالات متحده مقادیر عظیمی «مهمات»، به‌ویژه از برخی انواع خاص، در اختیار دارد.
افزون بر این، هر مقدار که نیاز باشد، حجم زیادی مهمات تولید و به ایالات متحده ارسال می‌شود.
شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات تولیدی در تاریخ کشور ما هستند.
کسانی که این اظهارات خیانت‌بار را درز داده‌اند، تحت تعقیب قرار دارند.
برای آن‌ها درخواست محکومیت‌های طولانی‌مدت زندان خواهد شد!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 471K · <a href="https://t.me/VahidOnline/77762" target="_blank">📅 09:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYvvqjF8TKqtjMRI1cngMNOi7hIBUeLLsx6tTBpc187c1o__eEbczusHwaXUTMRt2MlPUlqYrYH-W_KwG5QBaxxAHe7YjYoaSksw_8HAOcbbBgxcBe1zqSrxcTAsntAIbz7R5UMOv-wxVPwX3OsAI-fM5CrhNQTM8c5Oe25WNbyKvrzcElAaEwRUwzg15Jr5JexAr6KypDnBqt943MaDPnvfFXg_4Rg72Ai3GW84QwDCyL_0pKhnwtqbsTmotkl6tX2mXFLR-WXTAPWG_EilWTcnec33CFHYHHZxxmHqIwYPYznFRzDvZv9EspLaS3xBCqdC-jac1bsCsNXYlQOwZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشینگتن پست
:
درگیری ترامپ و هگست در کمپ دیوید بر سر نگرانی‌ها از کاهش ذخایر موشکی در جنگ ایران
ترجمه ماشین:
در نشست این آخر هفته در کمپ دیوید، رئیس‌جمهور ترامپ از پیت هگست، وزیر دفاع، درباره کمبود شدید مهمات توضیح خواست.
به گفته دو فرد آگاه از این گفت‌وگو به روزنامه واشنگتن‌پست، سرخوردگی دونالد ترامپ، رئیس‌جمهور آمریکا، از جنگ ایران هفته گذشته در کمپ دیوید فوران کرد؛ جایی که او از پیت هگست، وزیر دفاع، خواست توضیح دهد چرا ظاهراً درباره کمبود شدید مهمات ــ که اکنون گزینه‌های نظامی در برابر ایران را محدود می‌کند ــ گمراه شده است.
این رویارویی روز جمعه و در حاشیه نشست کابینه ترامپ در کمپ دیوید رخ داد. به گفته هر دو فرد آگاه از گفت‌وگو، ترامپ با عصبانیت به هگست گفت تصور می‌کرده مشکل مهمات «حل شده است». این افراد نیز مانند دیگران، به‌دلیل ترس از تلافی‌جویی، به شرط ناشناس‌ماندن صحبت کردند.
به گفته یکی از منابع، کمبودها، به‌ویژه در زمینه موشک‌های هدایت‌شونده دوربرد و موشک‌های رهگیر پدافند هوایی، از دلایلی بوده است که ترامپ در روزهای اخیر از اجرای حملات گسترده‌تر علیه ایران عقب‌نشینی کرده است.
کارولین لیویت، سخنگوی کاخ سفید، در پاسخ به پرسش‌های واشنگتن‌پست گفت: «این خبر صددرصد جعلی است. واقعاً هرگز چنین اتفاقی نیفتاده است. رئیس‌جمهور ترامپ نیز نهایت اعتماد را به وزیر هگست دارد.»
متن کامل فارسی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 483K · <a href="https://t.me/VahidOnline/77761" target="_blank">📅 08:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=ukq__N6dd0MF_5rs2OjRezchwtCYBNSMFT7hW_vcS3j7kQLl6bs_N8jqrKdCsKght1uN4Otd4orApy0C1YQPG4LuTVGAIJevt4ZvY0efnXp4eh8mQL8HcvY50g0vyd0xiUIXcLC2T8hUJyV3tlOsKcQsXj7-vG2iz1vW6ZKhwA2B7IqXlkKTkXp2cIgXpJ--8mJYs6Q0PKuJ0SXDzcgqtI_U-bunJ8GiTFZcV6ngM2lIW6r-WzgW_k_C7Wpqi3X3mYsQ_N1LshqWq5z575jb3P9zysLpQeib4E_VN6TSPe4g-iBGf6lAXYNfnXU6vcfjiNoxgjr7LOeNx5ioLlhjVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=ukq__N6dd0MF_5rs2OjRezchwtCYBNSMFT7hW_vcS3j7kQLl6bs_N8jqrKdCsKght1uN4Otd4orApy0C1YQPG4LuTVGAIJevt4ZvY0efnXp4eh8mQL8HcvY50g0vyd0xiUIXcLC2T8hUJyV3tlOsKcQsXj7-vG2iz1vW6ZKhwA2B7IqXlkKTkXp2cIgXpJ--8mJYs6Q0PKuJ0SXDzcgqtI_U-bunJ8GiTFZcV6ngM2lIW6r-WzgW_k_C7Wpqi3X3mYsQ_N1LshqWq5z575jb3P9zysLpQeib4E_VN6TSPe4g-iBGf6lAXYNfnXU6vcfjiNoxgjr7LOeNx5ioLlhjVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش مربوط به ایران،
تشخیص و ترجمه ماشین:
در ونزوئلا خیلی خوب پیش می‌رویم.
نفت زیادی از ونزوئلا می‌گیریم و رابطه‌مان با آن‌ها هم بسیار خوب است.
میلیاردها و میلیاردها بشکه نفت از ونزوئلا خارج می‌شود. ونزوئلا یکی از غنی‌ترین نقاط جهان از نظر نفت است.
و همان‌طور که می‌دانید، آن یک جنگ ۴۸ دقیقه‌ای بود؛ ۴۸ دقیقه طول کشید.
و هزینه جنگ را با آنچه از آنجا بیرون آورده‌ایم، چندین و چند و چند برابر جبران کرده‌ایم.
قبلاً کجا چنین چیزی شنیده‌اید؟ هیچ‌جا نشنیده‌اید.
همان روش قدیمی است، درست است؟ همان روش قدیمی.
غنائم از آنِ فاتح است، درست است؟
و ضمناً همین کار را در جمهوری اسلامی «دوست‌داشتنی» ایران هم انجام می‌دهیم.
داریم حسابی می‌کوبیم‌شان.
ترجیح می‌دهم توافقی انجام شود، چون نمی‌خواهم مردم را بکشم. نمی‌خواهم مردم را بکشم.
اما بالاخره در مقطعی قرار است... ما... ما برای بزرگ‌ترین حمله در میان همه حملات آماده شده بودیم و طی چند ماه گذشته ضربات بسیار سختی به آن‌ها زده‌ایم.
اما کاملاً آماده بزرگ‌ترین حمله از زمان جنگ جهانی دوم بودیم.
آن‌ها با من تماس گرفتند و گفتند: «لطفاً این کار را نکنید. بیایید گفت‌وگو کنیم.»
بعد می‌گویند: «ما هرگز چنین چیزی نگفتیم.»
می‌دانید چیست؟ رسانه‌های جعلی می‌دانند که آن‌ها چنین چیزی گفتند.
اما در حال گفت‌وگو هستیم. ببینیم چه اتفاقی می‌افتد.
ولی آن‌ها برای ما احترام قائل‌اند. به ما احترام می‌گذارند.
۴۷ سال گذشته است؛ ولی در واقع ۵۰ سال شده، چون سه سال است که می‌گویند ۴۷ سال. ۵۰ سال شده است.
هیچ رئیس‌جمهور دیگری کاری را که باید مدت‌ها پیش انجام می‌شد، انجام نداده است؛ زیرا ایران نمی‌تواند سلاح هسته‌ای داشته باشد. نمی‌تواند داشته باشد.
---
و به‌محض اینکه این وضعیت با ایران پایان یابد، قیمت نفت به‌شدت سقوط خواهد کرد. قیمت بنزین هم پایین خواهد آمد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 469K · <a href="https://t.me/VahidOnline/77760" target="_blank">📅 01:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVo18KOz6zu-3kR8hfJKJU-mYH1OQ-vwgDvQP0-YRk32ase63BA6RxM5TwX-dy5NaRbgTZY0ZbpfdWSV-20BoUMTNmOUshheY7H91qX3fpRmmBlELOpvxAT3chHS0_r64-EVFemIComiNgvQOlgX9NqzrMqieWsH8MI7XLhnLPDhlowDZEs_woZLlTvofkkIMDGtJ-jcm_hwRnMbgDyc0IVSsxww0FoWlYgjvpbpco8wdAeHi_yQBIg-hRs8PCHvrfLzaiZPO6lWGFQieko5cxWsZ_DGkhLpAjTlyDhFt3WqRzU6BzoALhJ5k_cYPNk9cDj0ksQGVCtS3gW2ssFivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز چهارشنبه ۱۴ مرداد، حملات جدیدی را به جنوب لبنان آغاز کرد و دلیل آن را «نقض آشکار آتش‌بس» از سوی گروه حزب‌الله دانست. این حملات که با صدور نخستین هشدار تخلیه پس از هفته‌ها برای ساکنان شهرک «منصوری» همراه بود، دست‌کم یک کشته و ۱۱ زخمی بر جا گذاشت.
این رویارویی‌های جدید در حالی رخ داد که نمایندگان لبنان و اسرائیل با میانجی‌گری آمریکا در رم مشغول گفتگو برای پایان دادن به درگیری‌ها و عقب‌نشینی مرحله‌ای اسرائیل از جنوب لبنان بودند.
یک منبع آگاه از روند مذاکرات به خبرگزاری فرانسه گفت هیات اسرائیلی، سه ساعت زودتر از موعد مقرر خواستار پایان جلسه شد. به گفته این منبع، یحیئل لایتر، سفیر اسرائیل در آمریکا و رئیس هیات مذاکره این کشور، درز «اطلاعات گمراه‌کننده» از سوی طرف لبنانی را علت این تصمیم عنوان کرده است.
با این حال، انتظار می‌رود این مذاکرات روز پنجشنبه در سومین و آخرین روز خود استمرار یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/77759" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX9cw9-URXzxj-p-HtjBwHwlpKoUKivT_ouXQ5_v0YiieaP3c9peyx3k-nCjW0OIPznoQMcBL6ch23OsudOPorFNUq23CTHSqWwN7ot5JHIWXZkb9jyEoKBsfhzacx6CoLc1_1ti4FUteI1J-s3Pj0QlxOc9xKB1IiffAX5rx6iK70qt1U_FWHxFEvMG6cB-im2rLZI5CW2lMQjikAiEzc1JCw0X3GwyO7Kmjjj1fl8o6UXJ-p2VkvNV8YDynMtOXGsTiwnTug36UZ4dL92Y9TIXVcPAjrUGMGKcEUGfZEW3zA56xNJPacfhe64-ZZ2KvU64chlRX2MWnUxW3DyJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده روز چهارشنبه ۱۴ مرداد تحریم‌های اعمال‌شده علیه شرکت هواپیمایی عراقی «فلای بغداد» را که پیش‌تر به اتهام همکاری با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بود، لغو کرد.
ا این حال، تحریم‌های بشیر عبدالقاظم علوان الشبانی، مالک معرفی‌شده این شرکت، همچنان به قوت خود باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77758" target="_blank">📅 19:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=plt3QFvqNOjcwJj9XyMOZyp_EehauKK_i3Hk2yXSAgzzhHxJbzhmgkta4lUIAXVVL32szzFunF5LxW2IoTVxOBhzDQdDjoy3hpxlbHndOAMTcXODwD4poBX9YDP57CqgXmuFOp8BqjS4FvkywDit9tgI50ch-kHbiwo9cj9B9kuHnDMtoQuDEN2YiYjVnUNEAv7nUh10xsx_m8QbSL07dS-2_46CfORqrR1rcq4aTc8AUxBFtTF9OACgrWEWJ1iAeL15nbiL7pPgSOwaQ-J8dp_-lO44hcGsXfUIO-4CYnQJdQ7EESXWQ0oyvcGhVvG2N57t-0jsyXDE6_8u6X5k4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=plt3QFvqNOjcwJj9XyMOZyp_EehauKK_i3Hk2yXSAgzzhHxJbzhmgkta4lUIAXVVL32szzFunF5LxW2IoTVxOBhzDQdDjoy3hpxlbHndOAMTcXODwD4poBX9YDP57CqgXmuFOp8BqjS4FvkywDit9tgI50ch-kHbiwo9cj9B9kuHnDMtoQuDEN2YiYjVnUNEAv7nUh10xsx_m8QbSL07dS-2_46CfORqrR1rcq4aTc8AUxBFtTF9OACgrWEWJ1iAeL15nbiL7pPgSOwaQ-J8dp_-lO44hcGsXfUIO-4CYnQJdQ7EESXWQ0oyvcGhVvG2N57t-0jsyXDE6_8u6X5k4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل روز چهارشنبه ۱۴ مردادماه با انتشار پیامی ویدیویی اعلام کرد این کشور با طرح پیشنهادی آمریکا برای خلع سلاح حماس و مدیریت غزه موافق نیست.
نتانیاهو در این پیام گفت: ««رئیس جمهوری ترامپ و تیمش فکر می‌کنند می‌توانند حماس را به خلع سلاح و غیرنظامی کردن غزه وادار کنند. ما در حال بررسی این موضوع هستیم. آنها پیش‌نویسی برای ما فرستادند، ما موافق نبودیم، این پیش‌نویس ما نیست؛ ما نظرات خود را ارسال کردیم.»
حماس هفته گذشته اعلام کرد به شرط خروج اسرائیل از نوار غزه، خود را خلع سلاح می‌کند. با وجود واکنش مثبت ترامپ، اسرائیل همچنان با این پیشنهاد حماس مخالف است و چند وزیر کابینه ائتلافی، پیشاپیش تاکید کرده‌اند که ارتش این کشور از غزه خارج نخواهد شد.
@
VahidOOnLine
نخست‌وزیر اسرائیل در سخنرانی خود در خاکسپاری رسمی پدربزرگ و مادربزرگ تئودور هرتسل، با اشاره به تحولات جاری تاکید کرد که این کشور در میان رویدادهای حساس نظامی و سیاسی قرار دارد.
بنیامین نتانیاهو با تمجید از رئیس‌جمهوری آمریکا گفت: «می‌خواهم این موضوع را روشن کنم؛ رئیس‌جمهوری ترامپ بزرگ‌ترین دوست ما و بزرگ‌ترین دوستی است که تا کنون در کاخ سفید داشته‌ایم و ایالات متحده نیز بزرگ‌ترین متحد ماست.»
با این حال، نخست‌وزیر اسرائیل با تاکید بر حفظ منافع بنیادین تل‌آویو افزود: «اما موجودیت اسرائیل — چه با توافق و چه بدون توافق — قابل مذاکره نیست. من مصمم هستم که هر آنچه برای تضمین امنیت و آینده‌مان لازم است را انجام دهیم.»
اسرائیل در حال حاضر در میانه گفتگوها برای دو توافق قرار دارد: توافق با لبنان برای خروج تدریجی نیروهایش از جنوب این کشور و توافق صلح غزه برای واگذاری مدیریت این مناطق به هیات صلح مطابق طرح ترامپ.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز چهارشنبه ۱۴ مرداد، در جریان بازدید از مرکز جذب سربازان جدید با تاکید بر اتحاد داخلی این کشور پس از حوادث هفتم اکتبر، تصریح کرد که تل‌آویو اجازه تشکیل کشور مستقل فلسطینی را نخواهد داد.
نتانیاهو با اشاره به این موضوع گفت: «ما در اینجا یک دولت تروریستی فلسطینی تاسیس نخواهیم کرد؛ دولتی که می‌دانیم قصد نابودی کشور-ملت یهود را دارد.»
نخست‌وزیر اسرائیل در ادامه افزود طرف مقابل در پی نابودی اسرائیل است، چرا که این کشور ترویج‌کننده ارزش‌های پیشرفت، دموکراسی و آزادی است؛ ارزش‌هایی که به گفته او، مورد نفرت «دشمنان بربر» قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77757" target="_blank">📅 17:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K09I6NFN-3WU2jN4GNlSY9xdwnENB-FA9jO3RfCvmIHXkMax_8qbdzYK4xqjslF2u6SYlKpv3z1mGYDXgXo7qIFmJlKUwcJOoHOYaGdb3uCuEe--JSU_72DCMxtvXXyyUGGixmWyPCfba34FEbj--aa9ZF4UMVfNfLu81fr8ekfMHhTweZ_CFHoI60G8wWZKPhZT-m2VHXAOYQ5OrJhLgIzslSahP_-uqm4Z9uOo9OuAEDmWpyvC-Am7pmSd-4K4Zb50fEadfthGun9htY1HPgVZ3SyylvnaD35AuS2HMLRzHegq_bQa2X8SZTjRD8wE10nhx3GaNa38lIic2y5PfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77756" target="_blank">📅 17:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWZ4rj7KZnpdrOPjLXTK5bKGZAlgraS9v-IfELbSVa0ulnPHPshUUXZ5kmo8qC7KsIX1zrcKIIVjJJ-s6Fc_W_wCLYreWfaOuUEFYpKVwhZ6YmVkUbPNsfnfqU5lfVTKqoV2G-aGokwePKZmhITv-ldHAzgaFSjB4p1Ry65jiuU0PiBNhFZfMcZr-fzbndegdj0rLsiBzSGkI4uUhlV_gggFR5SOiL-sSZkINJ1r9bMq8lk5H3fg9WiIWaj5SWK_oP3FzJCHx5eMvUueaCrcZqHLn3ZQixJ21eRfYVnDHzBmBESXFVeIS6iVFwkfil9ANuVlXaBfvR7VDaGAeYnR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در واکنشی دوپهلو به تکذیب دفتر مجتبی خامنه‌ای، اعلام کرد این تکذیبیه را می‌پذیرد، اما ابراز امیدواری کرد پس از «تغییرات مهم آینده» این دفتر نیز همچنان پابرجا بماند.
این واکنش شامگاه سه‌شنبه ۱۳مرداد۱۴۰۵، در صفحه اینستاگرام دفتر خرازی منتشر شد.
در بیانیه دفتر او آمده است: «گرچه به احترام قائد شهید و نیز رهبر معظم حاضر، تکذیبیه روابط عمومی و دفتر نشر آثار را حدوثاً می‌پذیریم، ولی امیدواریم پس از تغییرات مهم آینده در حوزه دفاتر فوق، این تکذیبیه همچنان باقی بماند.»
در ادامه بیانیه آمده است: «خداوند ما را در صورت استقامت و صبر در راه اهل‌بیت و ولایت معظم فقیه یاری خواهد فرمود.»
فرستاده است.
دفتر مجتبی خامنه‌ای ساعاتی پیش از انتشار پاسخ خرازی، ادعای او درباره هشدار رهبر جمهوری اسلامی به مسعود پزشکیان بر سر استعفا را تکذیب کرده بود.
در بیانیه این دفتر، بدون نام‌بردن از خرازی، آمده بود: «مطلب منتشرشده در فضای مجازی که در آن فردی، ادعایی را درباره واکنش رهبر انقلاب اسلامی به نامه رییس‌جمهوری محترم مطرح کرده، از اساس کذب و خلاف واقع است.»
دفتر مجتبی خامنه‌ای انتشار این ادعا را «زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه» توصیف کرده بود.
یک روز پیش از انتشار این تکذیبیه، ویدیویی از سخنان خرازی در شبکه‌های اجتماعی منتشر شده بود. او در این ویدیو مدعی شده بود مسعود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده است.
خرازی همچنین گفته بود مجتبی خامنه‌ای در واکنش به این موضوع نوشته است: «یک بار دیگر پزشکیان استعفا کند، استعفایش را می‌پذیریم.»
او مدعی شده بود پس از این هشدار، پزشکیان و دیگر مقام‌های دولت از مطرح‌کردن دوباره استعفا عقب‌نشینی کرده‌اند.
@
VahidHeadline
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77755" target="_blank">📅 17:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFl6vToPoEx6pYN9kWvcOtgI-5HJFHZO7m8htIVk8NhVH4UHHhsYi1EuQOV8Zu78F43WnB8jgeYFoahrvlSkWeUsXQJ_c5U_zak6Kew6mfad0N1vujdUqUH6xwFBuoFgQ1Gcl_uquDUibXsw0VA4WM_--eCwZ4h5c719D4TU5TZQATzHz1FmkwVtOBLcNYdvUStXL-CcvLSOLQC2HmmVS-bPsTdPtvZGxk4-Gco-y5Hg9gGmNjBROlPsz6jdn3567qe1nuIiDxroLImZqSa-m22RwmItRjmIrM6A20rZtrt6XtZr5IM39RFW811SqFzXtOmuSl1FrD9Mgk34KnChVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل متحد، اعلام کرد که از ۲۹ اسفند ۱۴۰۴ تاکنون، دست‌کم ۵۶ نفر در ایران با اتهام‌های امنیتی اعدام شده‌اند.
ولکر تورک با صدور بیانیه‌ای یادآور شد که از این تعداد ۲۷ نفر از معترضانی هستند که در تجمعات اعتراضی دستگیر شده‌اند.
او اعلام کرد که در این مدت روند صدور و اجرای احکام اعدام در ایران افزایش یافته است.
کمیسر عالی حقوق بشر سازمان ملل متحد از مقام‌های جمهوری اسلامی خواست تا همه اعدام‌ها را متوقف کنند و در مسیر لغو مجازات اعدام گام بردارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77754" target="_blank">📅 17:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/upwBaOLJ7AWBiws4Wx1j99Na3o1tMXIk5ku_v6AN975kwb7qwBW0F0Zu5q3xaA9EOEE8xNglrwlSKucaHH_5YWze2SgZzdDbHQav6CrWrI0lq6G0FST8Dr0j-iHHXxzOCFQICVCb3kjboDQZ9dptVGyPqBub1UNEL1xmuiZaviGi40mGG-0BZylI2-6TnoV0ETd2I3CqoXQqO0SpnRHCUxlnuvGkkwTOpWvhkuKY1mNxyOyvqSuwaXHlj6OoeOdlDrDxrp1jqJAbNeEbDQfIYp7gt1P51FqIlopu0AO2u-Zhe1VaGuWLQKBJoUJpVoVQbD_z0wQPwJpl_9BXdrfO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی قاسمی حسنوند، شاعر، زندانی سیاسی سابق و شهروند اهل شهرستان الشتر، روز یکشنبه ۱۱ مرداد ۱۴۰۵ پس از اقدام به پایان دادن به زندگی خود مقابل دفتر سازمان ملل در اربیل جان باخت.
منابع آگاه به ایران‌وایر می‌گویند او پس از آزادی از زندان با مشکلات روحی و فشارهای ناشی از پرونده قضایی خود روبه‌رو بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77753" target="_blank">📅 17:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04787365a6.mp4?token=PmYVv-lljZesgsmVLp0MhKL75VkIZV3_jFWQxVDSeNV3T2OVm8I3euSdNdWgY9NI_4ZxmISaU-HvFowcPP7-_5JQj7Z0CF1vZeFNU7DxeUcrZTiYpkEnS3eRldehoCV-ZUizJpBRnpRE4mZbL0ACkFw71ukBNIWmQ6ygxghwy4LxZtTyqtV44gbLBZyP45HsF9yM7uV7OUgFiPAQmGyP4_GhbFbPBNT81gIfwLJP4LV_bMJ007WEjhXoeocFQLxDDmNWl5ov9q__Y_zc0gupxWBV1S0UaSsQCEUywZTBCUJKOgT281hhYtJmqYQHDohvzM-n8dSAQhVe5qN-oVkV-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04787365a6.mp4?token=PmYVv-lljZesgsmVLp0MhKL75VkIZV3_jFWQxVDSeNV3T2OVm8I3euSdNdWgY9NI_4ZxmISaU-HvFowcPP7-_5JQj7Z0CF1vZeFNU7DxeUcrZTiYpkEnS3eRldehoCV-ZUizJpBRnpRE4mZbL0ACkFw71ukBNIWmQ6ygxghwy4LxZtTyqtV44gbLBZyP45HsF9yM7uV7OUgFiPAQmGyP4_GhbFbPBNT81gIfwLJP4LV_bMJ007WEjhXoeocFQLxDDmNWl5ov9q__Y_zc0gupxWBV1S0UaSsQCEUywZTBCUJKOgT281hhYtJmqYQHDohvzM-n8dSAQhVe5qN-oVkV-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
▪️
تنگه هرمز به‌زودی باز خواهد شد
▪️
مذاکرات با ایران به‌خوبی پیش می‌رود، اما تهران تمایلی به تایید آن ندارد
▪️
اگر بار دیگر عقب بکشند، ضربه سختی خواهند خورد
ترامپ:
اگر به اقتصاد نگاه کنید، اگر به اتفاقاتی که در حال رخ‌دادن است نگاه کنید... برای نمونه، ایران هرگز سلاح هسته‌ای نخواهد داشت. همین حالا هم دیگر نمی‌تواند داشته باشد، اما قرار است این موضوع رسمی شود.
تنگه [هرمز] خیلی زود باز خواهد شد؛ وگرنه ضربه بسیار سختی خواهند خورد و پس از آن، تنگه باز خواهد شد.
ما آماده انجام حمله‌ای عظیم بودیم؛ بزرگ‌ترین حمله از زمان جنگ جهانی دوم. بعد آنها با من تماس گرفتند و بسیار مؤدبانه گفتند: «لطفاً، می‌توانیم صحبت کنیم؟ می‌توانیم گفت‌وگو کنیم؟» آنها نمی‌خواستند... [جمله ناتمام است].
من هم گفتم: «بله، می‌توانیم صحبت کنیم. بیایید بالاخره این کار را تمام کنیم. بیایید انجامش دهیم.»
این کاری است که رؤسای‌جمهور دیگر باید طی ۵۰ سال گذشته انجام می‌دادند. می‌دانید، مدام عدد ۴۷ سال را می‌شنوید، اما سه سال است که همین عدد گفته می‌شود؛ حالا دیگر بیش از ۵۰ سال شده است.
رؤسای‌جمهور دیگر یا کشورهای دیگر باید می‌توانستند این کار را انجام دهند.
من کاری را انجام دادم که مجبور بودم انجام دهم؛ چون اگر آنها سلاح هسته‌ای داشتند، تمام این جهان جای متفاوتی می‌شد.
خبرنگار فاکس‌نیوز:
اگر دوباره عقب‌نشینی کنند و زیر توافق بزنند، کارشان تمام است؟
ترامپ:
اگر دوباره زیر توافق بزنند، ضربه واقعاً سختی خواهند خورد. خودشان این را می‌دانند و درک می‌کنند. من انتخاب دیگری ندارم. آنها نمی‌توانند سلاح هسته‌ای داشته باشند. موضوع بسیار ساده است.
این‌طور نیست که بگوییم: «خب، بیایید درباره چیز دیگری فکر کنیم.» نه؛ رؤسای‌جمهور بسیاری باید طی سال‌های طولانی این کار را انجام می‌دادند، اما انجام ندادند. حالا من دارم انجامش می‌دهم.
اوباما را کاملاً سرکیسه کردند. او فکر می‌کرد می‌تواند با پرداخت پول خودش را از این وضعیت خلاص کند. میلیاردها، ده‌ها میلیارد دلار به آنها داد؛ آن‌هم به‌شکلی بسیار احمقانه.
۱٫۷ میلیارد دلار پول نقد، اسکناس‌های سبز، در یک هواپیمای بوئینگ ۷۵۷؛ هواپیمایی پر از پول نقد. احتمالاً وقتی آن را دیدند، گفتند: «حتماً شوخی می‌کنید!»
نه، نمی‌توانید با پول‌دادن خودتان را از چنین وضعیتی خلاص کنید؛ تنها راه این است که با جنگیدن راه خروجتان را باز کنید.
اگر ما این کارها را انجام نداده بودیم، آنها مذاکره نمی‌کردند. ما ضربه بسیار بسیار سختی به آنها زدیم. اما ضربه سخت‌تر هنوز در راه است و امیدوارم مجبور نشویم از آن استفاده کنیم. امیدوارم مجبور نشویم.
گفت‌وگوهای بسیار خوبی داریم. آنها دوست ندارند به این موضوع اعتراف کنند، اما این کمی آزاردهنده است. به افرادی مثل شما می‌گوییم که گفت‌وگوهای فوق‌العاده‌ای داریم، بعد یک نفر از ایران می‌آید و می‌گوید: «ما دیدار نکرده‌ایم، ما...» [جمله در زیرنویس ناتمام است].
تمام روز چنین دروغ‌هایی می‌گویند. متوجه هستید؟ باورنکردنی است. می‌گویند: «ما این کار را نکردیم.» می‌گویند درباره موضوع هسته‌ای صحبت نکرده‌ایم.
خب، پس درباره چه چیزی صحبت می‌کنیم؟ آنجا نشسته‌ایم و بی‌کار انگشت‌هایمان را به هم می‌زنیم؟
اما اهمیتی ندارد. اینها فقط حرف است. تنها چیزی که اهمیت دارد، عمل است. آنها می‌خواهند توافق کنند. خواهیم دید چه اتفاقی می‌افتد. اگر توافق نکنند، برایشان خیلی بد خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77752" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hlj-h956ZlCRxvoMo74p2IhNpz-tZ9_ivG-FD3tm_D21cEoBOYMivlIGdbBaTi-HP-7KEpWobp_oBvK7gNC1JKxsgHEvfg-JF0ufqBzgUSJTW_-635C6589RdeqNd6ojSeTfIEYqQVwMJa5rsfYtP0vz7QCaRaFByUys-2U7VqCFUiq1ZSmPL3vuNO_C7XHCdB_WPWe-a8Q_gr5Y_0NLKquBmiHKSeXnxsSDLeuuinMebMav3M-W1s6hDQmjPgiGgUdSL0aSUUTFUWy70kP6kEzDWWIctKkLRTAXhsggsuUv1_OCoix6H0q4eb8gVQ6wV5gXC2YycvAgKqs8cHurug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"آمریکا به توافق درباره هرمز نزدیک شده و به‌دنبال اعلام آن در روز چهارشنبه است"
اکسیوس، ترجمه ماشین:
به گفته دو منبع منطقه‌ای و یک مقام آمریکایی، آمریکا، ایران و عمان به دستیابی به یک توافق موقت برای بازگشایی تنگه هرمز نزدیک شده‌اند و آمریکا قصد دارد این توافق روز چهارشنبه اعلام شود.
🔻
چرا اهمیت دارد:
هدف از این توافق که چند هفته است درباره آن مذاکره می‌شود، ازسرگیری آتش‌بس میان آمریکا و ایران و آغاز دوباره مذاکرات بر سر یک توافق هسته‌ای است.
▪️
رئیس‌جمهوری ترامپ روز شنبه تصمیم گرفت تهدیدهای خود برای آغاز یک کارزار بمباران گسترده را عملی نکند تا فرصت بیشتری برای دیپلماسی فراهم شود. با این حال، اگر به‌زودی توافقی حاصل نشود، ترامپ ممکن است با حملات بزرگ موافقت کند.
▪️
توافق در حال شکل‌گیری برخی از خواسته‌های ایران برای کنترل بیشتر بر رفت‌وآمد در تنگه هرمز را تأمین خواهد کرد؛ کنترلی که ایران پیش از جنگ در اختیار نداشت.
🔻
اصل خبر:
به گفته دو منبع منطقه‌ای، توافق مورد بحث یک سازوکار موقت ۶۰روزه میان عمان و ایران در تنگه هرمز ایجاد می‌کند که امکان تمدید آن نیز وجود دارد.
▪️
همه کشتی‌هایی که از طریق تنگه وارد خلیج فارس می‌شوند، از یک مسیر شمالی در آب‌های ایران عبور خواهند کرد.
▪️
همه کشتی‌هایی که از تنگه خارج می‌شوند و به دریای عرب می‌روند، با هماهنگی ایران از یک مسیر جنوبی در آب‌های عمان عبور خواهند کرد.
▪️
در دوره ۶۰روزه هیچ‌گونه عوارض یا هزینه‌ای دریافت نخواهد شد.
▪️
طرف‌ها تلاش خواهند کرد ظرف ۳۰ روز مین‌های دریایی را از مسیر میانی تنگه پاک‌سازی کنند.
▪️
پس از پاک‌سازی مسیر میانی، این مسیر بر اساس مفاد یک سازوکار دائمی که قرار است میان عمان و ایران درباره آن مذاکره شود، برای رفت‌وآمد کشتی‌ها در هر دو جهت مورد استفاده قرار خواهد گرفت.
🔻
بله، اما:
کاخ سفید، عمان و میانجی‌های منطقه‌ای سه هفته پیش تصور می‌کردند با ایران به توافق رسیده‌اند، اما ایران حملات به کشتی‌ها را از سر گرفت. این موضوع به دو هفته درگیری و وضعیتی نزدیک به جنگی تمام‌عیار منجر شد.
🔻
پشت‌پرده:
به گفته منابع منطقه‌ای، علاوه بر مذاکرات میان عمان و ایران، مقام‌هایی از قطر، پاکستان و عربستان سعودی نیز در تلاش‌های میانجی‌گرانه مشارکت داشتند.
▪️
منابع منطقه‌ای گفتند کاخ سفید به‌طور فعال در مذاکرات حضور داشت. در روزهای اخیر چندین تماس میان استیو ویتکاف، فرستاده ترامپ، عباس عراقچی، وزیر امور خارجه ایران، و بدر البوسعیدی، وزیر امور خارجه عمان، انجام شد.
▪️
دو منبع منطقه‌ای گفتند عراقچی در پایان هفته گذشته در اصل با توافق موافقت کرد، اما همچنان به تأیید مجتبی خامنه‌ای، رهبر جمهوری اسلامی ایران، و شورای عالی امنیت ملی نیاز داشت.
▪️
یک مقام آمریکایی و یک منبع منطقه‌ای گفتند رهبری ایران روز سه‌شنبه روند تأیید توافق را تکمیل کرد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/77751" target="_blank">📅 06:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW1-vc-MvWKyTRcEHWxMJth2mz_COZPYAMm3hngWBUhXaBCuh5EFGwPNNHiypR_tr1XLHXKfSSOmyW0UwT0nOAlEppB7tECJ22u1pKur8_w7f6vttpNrVAeCjRZQWRVvPWco1KMSTA_g97kihoE1oFfxX8V65vKwsuYe1y3eN9NFgAhSySIaDtCp3xnwbd1Q1Hltsh4AFeK2POIBg6tDSvXTB5AWin5X2FdwCagItGyBZm1ZWTl4czLMki-QGHT0xb87mVnDve5VCIoyLpcqvYbt0C1ZWWzeoD-XTEOZKZ_M2ZICwUtZjKbp-D6_heUK8pSVo8g5GR1EFcFzpwSRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
مسیر جنوبی عبور از تنگه هرمز همچنان برای همه کشتی‌های تجاری که قصد گذر از این آبراه بین‌المللی را دارند، آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی با وجود تجاوز بی‌دلیل ایران، به بیش از ۱۰۰۰ کشتی کمک کرده‌اند تا با موفقیت از این تنگه عبور کنند و این ترددها امروز نیز ادامه دارد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77750" target="_blank">📅 01:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77749">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=v2Onb-rbelqGxKFoT9DzZdTL-CU732cGk5oOg-eFlO492Is_4JcjNqQl_RrhPJLXbSmyxvhAD8_T-07aEuK8ZaBvv0nDOjUBx3pX26tA3LnEMScg3DrkA6foww7CFJ4AoPy2QQWA4qJYJlHYIUZ7o_ClYaP_2jrJYx_t8vCnw_NhT7vNBHMDYVc8tbsrzsKhh6CKCIWSxEIQeNAN1OVR0CK57ZY0A59EO24BQPvoIiEJQ4a-gYpbIzBztC2ZT98FVdd6x0W3KuUQCuqhI1woxAHfqTGMRI5tePaE9n52LalHKt_NDYpiU_SxPbb9GuiUuFYSiJey6zaeVQeBFzLgZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=v2Onb-rbelqGxKFoT9DzZdTL-CU732cGk5oOg-eFlO492Is_4JcjNqQl_RrhPJLXbSmyxvhAD8_T-07aEuK8ZaBvv0nDOjUBx3pX26tA3LnEMScg3DrkA6foww7CFJ4AoPy2QQWA4qJYJlHYIUZ7o_ClYaP_2jrJYx_t8vCnw_NhT7vNBHMDYVc8tbsrzsKhh6CKCIWSxEIQeNAN1OVR0CK57ZY0A59EO24BQPvoIiEJQ4a-gYpbIzBztC2ZT98FVdd6x0W3KuUQCuqhI1woxAHfqTGMRI5tePaE9n52LalHKt_NDYpiU_SxPbb9GuiUuFYSiJey6zaeVQeBFzLgZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت امیرعلی حیدری و سروش کرمی، دو نوجوان کشته در اعتراضات دی ۱۴۰۴ که هفته گذشته برای دومین بار به خاک سپرده شدند.
یکی از خانواده‌ها بعد از هفت ماه متوجه شد جسد اشتباهی به آنها تحویل دادند و خانواده دیگر دریافتند فرزندشان در بازداشت نیست و کشته شده.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77749" target="_blank">📅 01:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=gCi9noIfmbHz9iTgmv527ILXHdqUsi2qvWVGqvR7VUcmhu4Fy99QVafhgok_o18P9rZJPs57J_n22jM7nMLRFLWYA0svBYAFvRvy-AD33Hy45llu961LQUy8gm6UhQ3LDuQo4EhMpEcx_UAZSqZ9ioZ8gbeOqMptfPKWjamtbYxp-X7zh5AYIPaaiQZeLd4qwGzbrVX1USCDJtICaOrHqPvxe1LSC-LUmh-BWqMS_oslm3BW3b-PnvCzM0OFEABkgxS-iigHhLAoS2CPZvo0ucN3lJcnLcscDpqT7KqWIbBAjKbPTH3gRoty-ZrrDvtzMdjbg_Yr8yJKFBVGU3DF_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=gCi9noIfmbHz9iTgmv527ILXHdqUsi2qvWVGqvR7VUcmhu4Fy99QVafhgok_o18P9rZJPs57J_n22jM7nMLRFLWYA0svBYAFvRvy-AD33Hy45llu961LQUy8gm6UhQ3LDuQo4EhMpEcx_UAZSqZ9ioZ8gbeOqMptfPKWjamtbYxp-X7zh5AYIPaaiQZeLd4qwGzbrVX1USCDJtICaOrHqPvxe1LSC-LUmh-BWqMS_oslm3BW3b-PnvCzM0OFEABkgxS-iigHhLAoS2CPZvo0ucN3lJcnLcscDpqT7KqWIbBAjKbPTH3gRoty-ZrrDvtzMdjbg_Yr8yJKFBVGU3DF_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه ۱۳ مرداد اعلام کرد نیروهای این کشور تا خلع سلاح کامل حماس، از خطوط فعلی در نوار غزه عقب‌نشینی نخواهند کرد.
نتانیاهو در ویدیویی که در شبکه‌های اجتماعی منتشر شد، گفت: «ترامپ و تیم او بر این باورند که حماس می‌تواند کاملا خلع سلاح و غزه غیرنظامی شود؛ ما در حال بررسی این موضوع هستیم.»
نخست‌وزیر اسرائیل همچنین با اشاره به طرح پیشنهادی آمریکا افزود: «آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم، چرا که پیش‌نویس ما نبود. ما پاسخ‌های خود را ارسال کرده‌ایم.»
او تاکید کرد که نظرات و پاسخ‌های تل‌آویو پیش از رسانه‌ای شدن این موضوع به طرف آمریکایی تحویل داده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77748" target="_blank">📅 23:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwbPbsvNpnMX1mwMVxPPj37zvELgiViir-I8j1SJIalRePl8LIROjauMybsY6b6fUEEkulTQiK6Ms-DTctR0MXbOEdsyu63fGTPnTBVhw6V7tvltaZNpTeaA48Fk4PVX_-37RLDk6zZFFyHkkXHHpHKOxvQ3JEFu8Qz6iHtFbh22LC9uctZGZyyTqRDHIqhNfmKt2yfB5zcW5eaIxFM02cTI8luBWD-1hVzVi0Ff99lFz2F3Q5X7cAooC8sa_aIubvRSRaqFLi5bK6GWkGFmYEAT0VhKaFMpsAUrQziFLXBI8yEliQ6b3zMztcYRcMQcWbw8kwYAi9770FVf-WI-MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی قطر گزارش داد تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه در تماس تلفنی با دونالد ترامپ، رییس‌جمهوری آمریکا، آخرین تحولات منطقه، به‌ویژه تلاش‌ها برای کاهش تنش میان آمریکا و جمهوری اسلامی و نزدیک کردن دیدگاه‌های دو طرف را بررسی کرد.
بر اساس این گزارش، ترامپ از نقش قطر در حمایت از تلاش‌های دیپلماتیک و تسهیل گفت‌وگو میان طرف‌ها برای تقویت امنیت و ثبات منطقه قدردانی کرد.
امیر قطر نیز بر اهمیت ادامه گفت‌وگو، استفاده از راه‌حل‌های دیپلماتیک و پایبندی همه طرف‌ها به مفاد یادداشت تفاهم میان تهران و واشینگتن تاکید کرد. او همچنین خواستار حمایت از ابتکارهای بین‌المللی برای مهار تنش‌ها شد.
دو طرف همچنین درباره شماری از موضوعات مورد علاقه مشترک گفت‌وگو و بر ادامه هماهنگی و رایزنی درباره تحولات منطقه‌ای و بین‌المللی تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77747" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLgxqPPCRPdLFjPMf9V_cDLRqU-PYYoPdes5lizd87QP96Bu2RAAJnMJ7QaAQUWe1z2VMzU1xsEi8-5cuG30FyLi3L6pFLheRZWD45VmojQ79snCr5lKRyyTdMllNYMdmTRpHwdq7ZQwlvGoejF3QdIqdPhxiOoQXlZEaOTTPQ85fR7RuEbVnX88fYPH7EX3BbYSnqwp_0jM0K2Uz2opo04N6eUL9s3eogyImB6Bl9RDoLuLdctd6YGK1EXd0ABEQcGW1iE20rzSlX23aMcQ5KOgJbUaOXWxfDZgJlBEY-xGzQ36x2Ftx6HTlMRcK_Qrh-j9s00EBAuKcfaIjRCWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشتیرانی هند روز سه‌شنبه ۱۳ مرداد اعلام کرد که یک پرتابه به یک کشتی با پرچم هند در نزدیکی یمن اصابت کرد که باعث واژگونی و غرق شدن آن شد.
ساربانا‌ندا سونووال در پیامی در شبکهٔ ایکس نوشت که اما هر ۱۴ ملوان حاضر در کشتی، از جمله ۱۳ تبعهٔ هند، توسط گارد ساحلی یمن نجات یافته و به بندر مخا منتقل شدند.
وزارت خارجه هند نیز اعلام کرد که این کشتی تجاری به نام «ام‌اس‌وی فیض نور علیا» روز ۱۳ مرداد در دریای سرخ و در سواحل یمن غرق شده و این وزارتخانه در حال هماهنگی با مقام‌های یمنی دربارهٔ این حادثه است.
پالایشگاه‌های هند از زمان حملات حوثی‌ها به چند نفتکش سعودی، به دریافت محموله‌های نفتی خاورمیانه به‌صورت تحویلی روی آورده‌اند.
تردد در دریای سرخ در نزدیکی سواحل یمن به‌دلیل اقدامات حوثی‌های همسو با تهران مختل شده است. حوثی‌ها با ایجاد اختلال در صادرات نفت عربستان، دامنه درگیری میان آمریکا و ایران را گسترش داده‌اند. پیش‌تر نیز عرضه نفت از طریق تنگه هرمز مختل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77746" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vm-IvAHtJitJ6R9FUfeIZDcZmn0FdRslkzPLDj6xjPmkTOB9AdCgy-j__aD8MJHqMO8m81Kj0CBEmHxT4pGDYfaqsof0aval6ojtYd6ojMyPW7nlQA8S-fVRQo9p3FxT6je2GdDmzfTGgxueQGLEzQjwy4kKmMhdpF09YR4ryk_tbnR4pGN1Lt6AJMq2gtSw1_gPzxEg20TwyfulXP_pn8ua1bcSk24hNoJMnSftB4BbcaXYLP6fcYwkpmAU9qf_zCZTG8xtoIiKg-4yICexA5m_GKfRl91tt4aYqfB8rPnCf4jNDLLBkLDjScOMV-fGwyHojtJgcN5O8DUsULavZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LRfCgVkBJgq1mbLfM2C7fESAeHiXIqtDdTapfO0WX8M0XezTW42MScsfIK4ULSHtvZItMPNE29vQrC2p7V_IG5b2ZA9P8c4y6k64pbsYL43mVvqnWm1h-MrYpTeWwrLs4-XPO_Gl48hY7-fETfEYfwxeabDTWJl3i7FlWhDsamqcuS2LnrfkT5eXa63mmnafXO-CxcadhoCbsxLZGBcNFxVWl2S_CE2MfHNB-nu2A2Y5Hmng6Luk8GVXuO-fT-sOlzqnLAiloI2ujl4oClBwdRjoDvMjHNZegWJS2ByRjg0hveMuezcM9KvdknFjIf_l-vk-pslo7CWp4Wew3fQoMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nt8GM-4shLcubB91vhUJoMd0WYxGNe6fw0Y-km1LUfsnlBYz88wulZ5Gx0IuGoBO106RhZA1oJM-PzWKXRThRfjxCySslLohXCS349afBT9SkhzILBDDcne5ZT-LVV_y4I4tm81rEwYufGCz9Aj8ZLjRw3wuj8itFdMK9WBk3KFwAn5HG5Or9dZ6jYA6KwzqUXJ0032htFlNWbP3-mEUt7Pc8ktWBrQ95RJW93cNyWUoAd9upWkR96f9kTZG_VFOk-4Hfz1kF-OpNw5EXbnePUx5dQ_-jAuk6UNz-b6bmzSvkcMox_yWkK5VDSqN2ix3xgdz79HG8LxMqZRyLpRRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JXqhiqSmCwuqFKFwAghVAcddwtHSV5cCNlcFc8BaU_46N3ghaZu_l6Idk-lVHkBoqDYA9ORUQp6NO0MdsWDUrAMU9QCBRMB0y9hKcI_cR2ME1FZnaKEEQpZs9FkXz5sAr7yKTG9xbXDeUhj98xVKOGagn6RXriebngErnWJBp1EHBRVj6QaeNGxq1kQNPLUgrMcmPZDVeiTOLmxr4AgAb_rAlNlSyokzQ_QqztUc_92Xfbi4gQLLbyTA8seVoY7WjoKZ-CrFfM-3gQ7cL9Rayc13YDgsCOqDrZtLYk4-XHD0KZt6SNXiybeGdjyFMpQTV3ZYyxt4IEufRuXr0lk2SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=Q1SNoQVj_glw3grP7uBmWvb4Vcu_VSbYR9sdnya_S-9GhlcHT4buqJvvCrl5jvWZIaYGwMKX-krcIffp2wzdUKw0R2yPu_UNPeZPNttALPplwPN8f9OZfmwbl8CGpRjY4vRMSzuHzQZh-mkqbHf4gLv71j9shHvtUnqLe7x60NIeafmoxxi46eZDDmfidKMUii4RMb0DqEDt8RzIydqbsqZR0G6f69ETn5P-uJiH7VjChfj3-rN_m68ttx0nukJ9ghdFR1E1EWumvzjxSlQJ2H3EZtWp-0WUPUwU_NP1S1AP9rWOtuQZN56YPC9n_QYUEy5UrrYgU4Cxhs9tl-uBMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=Q1SNoQVj_glw3grP7uBmWvb4Vcu_VSbYR9sdnya_S-9GhlcHT4buqJvvCrl5jvWZIaYGwMKX-krcIffp2wzdUKw0R2yPu_UNPeZPNttALPplwPN8f9OZfmwbl8CGpRjY4vRMSzuHzQZh-mkqbHf4gLv71j9shHvtUnqLe7x60NIeafmoxxi46eZDDmfidKMUii4RMb0DqEDt8RzIydqbsqZR0G6f69ETn5P-uJiH7VjChfj3-rN_m68ttx0nukJ9ghdFR1E1EWumvzjxSlQJ2H3EZtWp-0WUPUwU_NP1S1AP9rWOtuQZN56YPC9n_QYUEy5UrrYgU4Cxhs9tl-uBMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت ایالات متحده ممکن است تا روز چهارشنبه برای بازگشایی تنگه هرمز با ایران به توافق برسد؛ توافقی که به گفته او می‌تواند قیمت انرژی را تثبیت کند.
او روز سه‌شنبه در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «ما با ایرانی‌ها در حال مذاکره هستیم و فکر می‌کنم این احتمال وجود دارد که امروز یا فردا برای بازگشایی تنگه و حرکت به سوی وضعیتی عادی‌تر در این درگیری به توافق برسیم.»
بسنت در پاسخ به این پرسش که آیا چنین توافقی به ایران اجازه خواهد داد از کشتی‌های عبوری عوارض دریافت کند، گفت: «فکر می‌کنم منظور، آزادی رفت‌وآمد خواهد بود.»
@
VahidHeadline
مارکو روبیو، وزیر امور خارجه آمریکا، روز سه‌شنبه ۱۳ مردادماه اعلام کرد هدف نهایی مذاکرات با ایران، دستیابی به توافقی برای خلع سلاح هسته‌ای این کشور است و گفت توافق کنونی که تمرکز اصلی بر آن قرار دارد، به تضمین عبور امن کشتی‌ها از تنگه مربوط می‌شود.
روبیو با اشاره به ادامه تردد کشتی‌ها و انتقال نفت از تنگه گفت: «همین حالا کشتی‌ها از تنگه عبور می‌کنند و صادرات نفت ادامه دارد. تنگه باز است.»
او افزود: «خلع سلاح هسته‌ای ایران توافق نهایی است. توافق فوری، که اکنون بیشترین تمرکز بر آن قرار دارد، مربوط به تنگه است.»
روبیو همچنین گفت مذاکراتی میان عمان و ایران درباره فراهم کردن امکان عبور امن کشتی‌های بیشتر از تنگه در کوتاه‌مدت در جریان است که آمریکا نیز در آن دخیل است. به گفته او، این مذاکرات پیشرفت کرده، اما هنوز به نتیجه نهایی نرسیده و واشنگتن امیدوار است به‌زودی به جمع‌بندی برسد.
@
VahidOOnLine
قطر اعلام کرد تلاش‌ها برای دستیابی به راه‌حلی دیپلماتیک میان ایران و ایالات متحده ادامه دارد، اما هنوز توافقی حاصل نشده و هیچ مذاکره مستقیمی میان دو طرف برنامه‌ریزی نشده است.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، روز سه‌شنبه ۱۳ مرداد ۱۴۰۵ به خبرنگاران گفت رایزنی‌های دوحه با ایران و آمریکا همچنان ادامه دارد. به گفته او، این رایزنی‌ها بر دستیابی به «راه‌حلی کوتاه‌مدت» متمرکز است تا زمینه ازسرگیری گفت‌وگوها و احیای کامل روند میانجی‌گری فراهم شود.
اظهارات سخنگوی وزارت خارجه قطر یک روز پس از آن مطرح شد که دونالد ترامپ، رییس‌جمهوری آمریکا، گفته بود مذاکرات با تهران در جریان است و ایران با «آخرین فرصت» برای دستیابی به توافق روبه‌روست.
ترامپ گفته بود این مذاکرات به درخواست ایران، عربستان سعودی، امارات متحده عربی و قطر انجام می‌شود و افزوده بود: «این آخرین فرصت آن‌ها برای امضای یک توافق خوب است.»
در مقابل، مقام‌های جمهوری اسلامی تأکید کرده‌اند که هیچ مذاکره‌ای با آمریکا در جریان نیست و گفت‌وگوهای کنونی ایران تنها با عمان و درباره تنگه هرمز انجام می‌شود. تهران همچنین اعلام کرده است که این هفته هیچ نشست مهمی برنامه‌ریزی نشده است.
@
VahidHeadline
قیمت نفت روز سه‌شنبه ۱۳ مرداد پس از اظهارات مقامات قطر و وزیر خزانه‌داری آمریکا که امیدها را برای حل دیپلماتیک مناقشه خاورمیانه و بهبود عبور نفتکش‌ها از تنگه هرمز افزایش داد، حدود ۴ درصد کاهش یافت و به پایین‌ترین سطح خود در سه هفته اخیر رسید.
@
VahidOOnLine
—-
ترامپ هم دوباره چندین پست پشت هم منتشر کرد که یکیش لینکی است مربوط به مطلب ۲ روز پیش
breitbart
با تیتر:
ترامپ: «توافق قریب‌الوقوع است»؛ مذاکرات با ایران درباره خلع سلاح هسته‌ای و هرمز دوشنبه از سر گرفته می‌شود
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77740" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gxUwJ8G1haqHe1WtOVK3rz9goAXfY78Xynkgkm79H7yUGW4qsUWHXc2-1KkymPuZy3AQfIJtsmDOJbEJZftjwFpPiVQ-_HV94zsk00djCFauYFLp8PCQM6DCeQHbjvhIELqOzTLuaqaSZtbrC0KOo9T_H-NlxiqrespnZNzY7sq4Or6w29AHqBf2JaXsR7RxmYdkjZFOeUYQ4hDT1Pm0hfvboetQVJWugrMYlOPTehZ4T7__9IcY7FFOHNSzS-t8rRZ-UKNpqdplguFAvbKVYqviW0SxoM8daFh5m7ibnB7mg_IrRt7DlKq7y9NZXFxm5WZLooZbyH6n3bcXo2FORQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=iVdgIb2hxqlTfRRh7wUfoAc2LKbHgvYUUrZMwLD4yzBKvqrk0YO0sooyTyiGZ22ceoi0qsFYJ0_lS_d5QmhYW-PUcpDS9rwQboqWZpcMjua-maJ55I9UKKVFh__JDuVOMS5mKiNpGUZhXQ2rvjRwDRM6fDmjlcVD99Am3J4j-3lHBu_AeEUwKK2NfOWstSdjAlSKNo-E3XNlLpdhSbikOn55gWhkZqfb1iuQBrsdS1aut8v38lhMxgHD9NdSb_zH1BZgNnNzKxNWXSgh_pE8mffjahavC4QAZWXlVILJfm0Z_Cjuw6XU8BtPnNEfHBL9Du9RyipUhphexkbkqS09nA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=iVdgIb2hxqlTfRRh7wUfoAc2LKbHgvYUUrZMwLD4yzBKvqrk0YO0sooyTyiGZ22ceoi0qsFYJ0_lS_d5QmhYW-PUcpDS9rwQboqWZpcMjua-maJ55I9UKKVFh__JDuVOMS5mKiNpGUZhXQ2rvjRwDRM6fDmjlcVD99Am3J4j-3lHBu_AeEUwKK2NfOWstSdjAlSKNo-E3XNlLpdhSbikOn55gWhkZqfb1iuQBrsdS1aut8v38lhMxgHD9NdSb_zH1BZgNnNzKxNWXSgh_pE8mffjahavC4QAZWXlVILJfm0Z_Cjuw6XU8BtPnNEfHBL9Du9RyipUhphexkbkqS09nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوها از کانال‌های غیررسمی حکومتی
درگیری میان حامیان جمهوری اسلامی و مقلدان صادق شیرازی، از مراجع تقلید منتقد جمهوری اسلامی، در جریان مراسم اربعین در کربلا به بازداشت ۱۴۰ نفر و مجروح شدن ۵۴ نفر انجامید.
شبکه تلویزیونی «اشعائر» عراق، رسانه نزدیک به "آیت‌الله صادق شیرازی"، صبح دوشنبه ۱۲ مرداد ویدیویی از این درگیری منتشر کرد.
بر اساس گزارش این رسانه، گروهی با در دست داشتن تصاویر علی و مجتبی خامنه‌ای و پرچم‌های «یا لثارات الحسین» و «یا لثارات الخامنه‌ای» مقابل دفتر آیت‌الله صادق شیرازی در کربلا تجمع کردند و علیه او شعار سر دادند.
این رسانه می‌گوید حامیان علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، و فرزندش مجتبی خامنه‌ای هنگام عبور از مقابل دفتر صادق شیرازی این شعارها را سر دادند که با واکنش هواداران و مقلدان این مرجع تقلید روبه‌رو شد.
به گفته کاربران شبکه‌های اجتماعی، این درگیری ابتدا با مداخله پلیس عراق متوقف شد، اما در ادامه میان حامیان جمهوری اسلامی و نیروهای امنیتی عراق نیز تنش و درگیری رخ داد و پلیس عراق در نهایت با استفاده از قوه قهریه به آن پایان داد.
بر اساس گزارش‌های منتشر شده، در جریان درگیری مقابل موکب منتسب به آیت‌الله صادق شیرازی، ۱۴۰ نفر بازداشت و ۵۴ نفر مجروح شدند. این آمار تاکنون به‌طور مستقل تأیید نشده است.
همچنین در برخی گزارش‌ها ادعا شده است که حسین ستوده، مداح حکومتی، از چهره‌های حاضر در این تجمع بوده و تلاش داشته این مراسم را به موضوعات سیاسی پیوند بزند.
"آیت‌الله صادق شیرازی" از منتقدان نظریه ولایت فقیه است و رسانه‌های جمهوری اسلامی او و جریان منتسب به وی را با عنوان «شیعه انگلیسی» معرفی می‌کنند. او ولایت فقیه را محدود به امر قضاوت می‌داند و با تفسیرهای جدید از اسلام و مذهب تشیع مخالفت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77735" target="_blank">📅 18:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rvtrReLKIGT_nh3-e_stPT3vsQGKFETZigiyucPqGj4nd_5KtHy_k7vnitxmFhoesBycMAcz1CtCE23EAoCu517F0riPoL2GZZABvi7ak3mbDuNDrEQPzP48I6VhMoLdCshKINZnri-i4JGW7sJr9_qr89LpVD5TPpkAX0sR0Gvt-J_5oIUCiQvSwEiI6MNc_JNtY2hJsvCixDjBfIQJdre3d6EEFKiHbck5mcNMydVYGaPJ8Z0sVSrdgyqBwaWPZma7euTmP3gZqyh19uzRPbM7M6NSqGDhFB-u5gzlPgc1QwGuQi1ePRX3PqARcgKJUzYms9cCJ6gGAJvxm0yADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/veLh1RsBkCLS7mprDGTGiB_bLHU7ggs1tqiHosmofaZTd2Rxki4mNCqtH7nUSTTXfMN9IsD8lOmAobVI9shsdmuT8wnrYPk9A9gLIc8c5k63EnjV7rCIqvpBsT8a_tG9RcPet5znoJSwda_y79MMCTH6NHafhTcZMsGtZx5JD4F8v2rr9YYNdTSjV7eFym0sn4Z20EmFEVdu4l8u4fmypozoksa2jtpKRoPCIdO7FOpUi1EjRA5UdGMCfbwp01g3myKuKWKEb5CNiaU_7nkQ85eiSprzRAURbzvoPXn2E10EyP_eO7OyKDCZj-U4IqMFjUV2zaP7YhYCQAcGT1JoEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شرکت نفتی آرامکوی عربستان سعودی روز سه‌شنبه اعلام کرد سود خالص این شرکت در سه‌ماهه دوم سال جاری، هم‌زمان با افزایش قیمت انرژی بر اثر جنگ خاورمیانه، ۴۴ درصد رشد کرده است.
بر اساس گزارش مالی آرامکو، سود خالص این شرکت از آوریل تا ژوئن به ۱۲۲ میلیارد و ۶۰۰ میلیون ریال سعودی، معادل ۳۲ میلیارد و ۷۰۰ میلیون دلار، رسید؛ در حالی که این رقم در دوره مشابه سال گذشته ۸۵ میلیارد ریال بود.
امین ناصر، مدیرعامل آرامکو، گفت این شرکت با وجود اختلال بی‌سابقه در عرضه نفت از مسیر تنگه هرمز، توانسته است با استفاده از خط لوله شرق به غرب، ظرفیت‌های ذخیره‌سازی و پایانه‌های صادراتی، فعالیت خود را ادامه دهد.
اعلام افزایش سود آرامکو هم‌زمان با انتقاد دونالد ترامپ، رئیس‌جمهور آمریکا، از سود بالای شرکت‌های نفتی صورت گرفت. او گفت این شرکت‌ها به‌دلیل کمبود نفت ناشی از جنگ «بیش از حد پول درمی‌آورند».
@
VahidHeadline
شرکت بزرگ انرژی بریتانیا، بی‌پی (از بزرگ‌ترین شرکت‌های نفت و گاز جهان)، اعلام کرد سود خالص این شرکت در سه‌ماهه دوم سال ۲۰۲۶، هم‌زمان با افزایش قیمت انرژی در پی جنگ آمریکا و جمهوری اسلامی، بیش از دو برابر شده و به سه میلیارد و ۹۱۰ میلیون دلار رسیده است.
سی‌بی‌اس به نقل از خبرگزاری فرانسه نوشت پنج شرکت بزرگ انرژی غربی، شامل بی‌پی، شورون، اکسون‌موبیل، شل و توتال‌انرژیز، در مجموع نزدیک به ۴۷ میلیارد دلار سود خالص در سه‌ماهه دوم سال ثبت کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77733" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JC_J5GwLC-dGSZqssUgjWcgIPBRgCF5-mobz17VE0_Lw2-Dv9hJxhHnbqmld0ZyB4AHQiHLk6rlt44gaMgvktHp6xes3Xo_NCvy-7wragGpXk4ozLvjKubuLAdm8Wemln2zWxbSleragIoZS2w18S1ir5KbmXBvIfDxjk4_deDWgUhMpz-1JihxYzN5-p4BvWmUX6QJ-RuBZI727Z5kgYN47kqSVIbfhlvt0CaHzvwFi4xthkxRlOK34zOeNmzg9Q4DNbVWx1Zv_xpD89TmZDmXxU7fyz4YQkX576sc1WaR7vq0tgFnlcicB2M9bSzwdbAywP3UfEkunEYBO5VKAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LrTDQnR5M1X6lHys8KjC2nHhA5G7cYqQ3r4TVzOBmyfAerIKQUNlqsCeFXcdsGD3TJVyvfvU32nmtKy41hvmJS2XgwLA4pSqT9TcAzbv-Jnam5sOfNCwLrIyUnlCJjhzif9kz6dibgPhif-3UhJkgMnO01wbWYI3jeDwryrVIiMvLzMCHC2kVuqk0i4V4xPbNg29Sj1qYV8TytHe5Np85HCQ-veAreCyyNhTdbiyuFanPNtzb8fOKjhEemDkKk-k3Da4QEAUW63GksKqHBdPQdd2PG6SLe6GHK_3gxSwm5NopQKF_v4XsBu0gVlhPqvvADZeoRFksi4jorLCCwWQHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/616a7ca97f.mp4?token=Yeu8j_ytE8n97TWGnvbu57cArVWuwVdJWWrIPZBOSu1svuekZwGabraqg5e7n-aLAnDbZy68lKGlv9yN_M0S3khivKZ3GJSVNzEi0wcpUOpf9FvofG18k8-jh6PJlNtUn4dERppskVG7CpQ03BK3vxJs1SSpPlXb4r1TyDtVv-_0yAYoz28qyNsGpUqrrH8FueYHBd8lb01cjB063IysQ3AG7nMRVVVy1lv9D1C_fLAtPu0DfUG_p7EC0mQnRDgy9JefRVYgI-684CbXNOXCQxtbu7albJ4arxdN9dFV4TtcgwzTH1d-4irEPwkICCLCI8JYcHOUfRTScbQVZY9_kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/616a7ca97f.mp4?token=Yeu8j_ytE8n97TWGnvbu57cArVWuwVdJWWrIPZBOSu1svuekZwGabraqg5e7n-aLAnDbZy68lKGlv9yN_M0S3khivKZ3GJSVNzEi0wcpUOpf9FvofG18k8-jh6PJlNtUn4dERppskVG7CpQ03BK3vxJs1SSpPlXb4r1TyDtVv-_0yAYoz28qyNsGpUqrrH8FueYHBd8lb01cjB063IysQ3AG7nMRVVVy1lv9D1C_fLAtPu0DfUG_p7EC0mQnRDgy9JefRVYgI-684CbXNOXCQxtbu7albJ4arxdN9dFV4TtcgwzTH1d-4irEPwkICCLCI8JYcHOUfRTScbQVZY9_kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در تیزر تبلیغاتی حاوی بخشی از سخنانش که قرار است در چند قسمت و از امشب به وقت محلی از تلویزیون ایران پخش شود، ضمن رد گزارش‌ها درباره استعفایش گفت: «استعفا نخواهم داد و خواهم ایستاد. اینها می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و اینها یک چیزی می‌گویند.»
این سخنان یک روز پس از انتشار کلیپی پربازدید از سخنان محمدباقر خرازی، دبیرکل تشکلی موسوم به «حزب‌الله ایران» که برادر همسر مسعود، برادر مجتبی خامنه‌ای، رهبر سوم جمهوری اسلامی ایران منتشر می‌شود که او درباره «۲۸ بار استعفای پزشکیان» و «تهدید مجتبی خامنه‌ای به پذیرش استعفای بعدی» سخن گفته بود.
این سخنان واکنش‌های چهره‌ها، جریان‌ها و رسانه‌های حامی و منتقد دولت را برانگیخته است؛ از جمله حمید رسایی که از آقای پزشکیان خواسته بود برای راستی‌ازمایی سخنان محمدباقر خرازی استعفا کند.
مجتبی زارعی، نماینده عضو کمیسیون امنیت ملی مجلس ایران در واکنش به طعنه آقای رسایی نوشت: «از ۹۰ میلیون ایرانی فقط یک شاهد برای تهمت خرازی به امام سید مجتبی شهادت داد ؛ سرکرده شریان!»
@
VahidHeadline
حمید رسایی نیم‌ساعت پیش، یعنی پس از انتشار ویدیوی پزشکیان هم تاکید کرد که هنوز تکذیب نشده:
بعد از اینکه سیدمحمدباقر خرازی درباره نحوه برخورد رهبری با استعفای پزشکیان - که تاکنون تکذیب نشده - ادعایی کرد، اطرافیان رئیس جمهور برخوردهای متفاوتی و گاه توهین آمیزی داشتند.
تصور کنید اگر وی ادعایی برخلاف آنچه نقل کرده به زبان آورده بود (مثلا رهبری به پزشکیان گفته شما باید محکم ادامه بدی) چه اتفاقی می افتاد:
rasaee
👈
بعدش، یعنی دقایقی پیش، این خبر منتشر شد:
دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، با انتشار بیانیه‌ای، گزارش‌ها درباره هشدار به مسعود پزشکیان در خصوص استعفا را تکذیب کرد. این بیانیه یک روز پس از انتشار ویدیویی از سخنان خرازی منتشر شد که در آن مدعی شده بود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده و مجتبی خامنه‌ای اعلام کرده در صورت تکرار این اقدام، استعفای او پذیرفته خواهد شد.
@
VahidHeadline
نسخه منابع حکومتی:
دفتر رهبر انقلاب: مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور مطرح کرده از اساس کذب و خلاف واقع است
🔹
متن اطلاعیهٔ روابط‌عمومی دفتر رهبر انقلاب:
بسم‌الله الرحمن الرحیم
🔹
با گرامی‌داشت اربعین حسینی و ادای احترام به روح بلند رهبر شهید انقلاب به‌اطلاع مردم شریف و مبعوث‌شدهٔ ایران می رساند در روزهای گذشته برخی نقل‌قول‌ها از رهبری معظم انقلاب اسلامی در فضای مجازی منتشر شده که متاسفانه زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه است.
بر همین اساس برخی نکات را درباره اخبار و مطالب مربوط به مقام معظم رهبری بیان می‌داریم.
🔹
مرجع رسمی انتشار پیام ها، اخبار و مطالب مرتبط با آیت‌الله سیدمجتبی حسینی خامنه‌ای، پایگاه اطلاع‌رسانی دفتر رهبر انقلاب و یا پایگاه حفظ و نشر آثار رهبر انقلاب است و هرگونه مطالبی که خارج از این چهارچوب منتشر شود، فاقد سندیت و صحت است.
🔹
رهبر معظم انقلاب اسلامی در پیام‌های خود از جمله در پیام اخیر بر حفظ اتحاد مقدس و حفظ حرمت مسئولان دلسوز و خدمتگزاران نظام اسلامی به‌ویژه دولت محترم تأکید داشته‌اند. مطالبی که برخلاف توصیه‌های مؤکد رهبری، موجب انشقاق و دودستگی در جامعه و زمینه‌ساز نسبت‌های نادرست به مسئولان محترم می‌شود، در جهت اهداف بدخواهان و دشمنان قسم‌خوردهٔ ملت ایران است.
🔹
بر همین اساس مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور محترم مطرح کرده از اساس کذب و خلاف واقع است.
روابط عمومی دفتر رهبر انقلاب اسلامی
۱۳ مرداد ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77730" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fWWScX669Yh-Qa5V8v8OzhMBjt7wUpbvCS_hpLe5RY-5MRMbUpfB8VUibiNTqnSngn8SZTdz-qIKcU_ZU4mqI9HEdhWGn-G_--tPmPLHzJb9JoDLo8SSWR9Vr0gzvQzcpkvcQMGq0uTiCLXlt-k60UFSYj4BysgkMd4v2JHjs7_XiTUQqDz7sLo6Eds8rYtkKQOhOZGesT6LaDb46XTR1cJ7gHYzo9rTmTHBSdCR0Wb_luT5iNnhisnrVLYoDftC5DEuQgDrlw5JZG96Yxrv0IVnVbGKvVX6_1Qik7Cv2B9gAntUiY_FmR6RHK8b5hGb6aJDTTBHiXqMhVhbPQFEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساکنان شماری از روستاهای جزیره قشم حدود چهار ماه است به آب لوله‌کشی دسترسی ندارند و برای تامین آب مورد نیاز خود ناچار به خرید تانکرهای چندمیلیون‌تومانی یا استفاده از منابع نامطمئن شده‌اند.
براساس گزارش میدانی آوش، یکی از ساکنان روستای طبل گفته است: «چهار ماه است شیر آب خانه‌مان باز نشده. حالا فقط با تانکر زندگی می‌کنیم. من توانستم سه میلیون تومان بدهم و آب بخرم، اما خیلی از روستایی‌ها حتی همین پول را هم ندارند.»
پس از آسیب‌دیدن یکی از تاسیسات آب‌شیرین‌کن در جریان حملات ماه‌های گذشته آمریکا به نوار جنوبی ایران، وضعیت تامین آب در بخش‌هایی از جزیره به‌شدت بحرانی شده است. او گفته آب لوله‌کشی تقریبا قطع شده و مقدار آبی که با تانکر توزیع می‌شود نیز پاسخ‌گوی نیاز ساکنان نیست.
این اظهارات در حالی مطرح شده‌اند که عباس علی‌آبادی، وزیر نیرو، ۲۹تیر۱۴۰۵ و در جریان سفر به هرمزگان گفته بود همه آب‌شیرین‌کن‌های منطقه در مدار بهره‌برداری قرار دارند وهیچ‌یک از جزایر کشور با کمبود آب مواجه نیست.
او همچنین گفته بود با وجود آسیب‌دیدن زیرساخت‌ها در حملات اخیر، خدمات آب و برق پایدار مانده و شرایط مدیریت شده است.
عبدالرحیم رضوانی، نایب‌رییس شورای اسلامی بخش مرکزی قشم  گفته است ساکنان برخی روستاها بیش از سه ماه برای وصل‌شدن آب انتظار می‌کشند و پس از آن نیز تنها چند روز به آب شبکه دسترسی دارند. به گفته رضوانی، قیمت یک تانکر چهار هزار لیتری آب به حدود یک میلیون و ۴۰۰ هزار تومان رسیده است.
در همین حال، یکی از ساکنان قشم گفته است برخی خانواده‌ها که توانایی خرید آب ندارند، برای مصارف روزمره از چاه‌هایی استفاده می‌کنند که از سالم‌بودن آب آن‌ها اطمینان ندارند. او به نقل از یکی از اهالی گفته است: «آب تمیزی نیست؛ حتی حیوان داخل آن می‌میرد، اما به‌هرحال آب شیرین است. برای خوردن استفاده نمی‌کنیم، اما برای کارهای روزمره مجبوریم همین آب را به خانه ببریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77729" target="_blank">📅 18:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDfBEvfGGOBYM9yWJBZrPd6v7S2izVtZkIJLALgW7idWbJOvcGvySK3-8aGWbiHvTei4f0x-9MD6F6m0DmRw-XrYfSOZdG9Xc-YSEJZ1FxfUJhuk67UpgNXPANk8eOs8HB7r959d6dCEvZgjI3pihj426nc-3J5SgTyGOU5MH-cFrIZRsHKj1ev2yBycUVE-VsDNqwb8Wrwx0Ow6T82CsbLREBfJR7S8I69BjANie2N7yptYaeoktfWuQ4IVNnRp58Pb3gXbxBaBzyyhqoUqMS4rWf3Dx0qFFhqBQ6_JXvjMYWShZYGBy--GIprl7HCSfohIZEvhRlQhjFGruzUIBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه موج پلمپ واحدهای صنفی و مراکز فرهنگی در ایران، در روزهای اخیر، دست‌کم سه مجموعه فرهنگی و صنفی در بابل، مشهد و تهران با دستور مقام‌های قضایی یا نهادهای ناظر پلمب شده‌اند.
هرانا خبر داد مجموعه «شهر کتاب» در شهرستان بابل، با دستور قضایی و به‌دست اداره نظارت بر اماکن عمومی پلمب شده است.
هم‌زمان، گزارش‌ها از پلمپ «کافه معماری سکنج» در مشهد حکایت دارند؛ فضایی تخصصی و فرهنگی که محل فعالیت معماران، هنرمندان و دانشجویان بود. تاکنون درباره علت پلمپ این کافه اطلاعاتی منتشر نشده است.
مجموعه «خانه ارغوان» نیز اعلام کرده است که به‌دلیل «پلمب موقت از سوی مراجع ذی‌ربط»، فعالیت خود را تا رفع محدودیت‌ها متوقف می‌کند. این مجموعه در خیابان فرشته تهران فعالیت داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77728" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KqUwt9N9urSCVqZP1_UvUQUrfLwPhEWlXjnIIKk5qsgxT8tojUQdkZNHhO9_zhgOCROp_YvXTKhEtBPlP5taDHPGlFWUneqGkrmeQHgJaKcdh0meIT_QVaQCMBIgq-Ffr9OEJSiTs18osB-QLGqUJKICnVa6427aGktqohUBtzBHMOcdF3fk6bkKYCj4m6anY9EEJC73rEnYgeVNLkr7Y5t8kUvz8OX8-FUd5cJvL5pDj8-gwIb9705rBGWdsvi5BbHoVMBTpjZ_8WtbOXquJj4giuwT3lQx9jRJvrTt2Aq7hLGzSkhWhRVO2GLA7nh0eCB7YkIu2euk6t7lEWqWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سازمان حقوق بشر ایران» اعلام کرد «مهدی روشنی»، معترض بازداشت‌شده در ارتباط با اعتراضات ۱۶دی‌۱۴۰۴ در شهرستان ملکشاهی، با اتهام‌های امنیتی به اعدام محکوم شده است.
این سازمان روز دوشنبه ۱۲مرداد۱۴۰۵ گزارش داد مهدی روشنی روز یکم بهمن‌ماه در منزل خود بازداشت و به تهران منتقل شد. به نوشته سازمان حقوق بشر ایران، او پس از بازداشت، دو ماه در بی‌خبری مطلق نگهداری شد و برای گرفتن اعترافات اجباری تحت شکنجه‌های شدید قرار گرفت؛ اعترافاتی که به گفته این سازمان، مبنای صدور حکم اعدام قرار گرفته است.
سازمان حقوق بشر ایران به نقل از یک منبع مطلع مدعی شده که یکی از افرادی که مهدی روشنی را پس از بازگشت از تهران دیده، آثار گسترده شکنجه را بر بدن او مشاهده کرده بود.
این فرد گفته است: «اگر بدنش را می‌دیدید وحشت می‌کردید. جای سالمی روی آن نبود. پر بود از آثار شوک الکتریکی و شلاق، اما حاضر نشده بود اعتراف کند.»
بر اساس این گزارش، مهدی روشنی اواخر اردیبهشت‌ماه ۱۴۰۵ با تودیع وثیقه آزاد شده بود، اما حدود دو هفته بعد بار دیگر نیروهای امنیتی او را بازداشت کردند و از آن زمان تاکنون در بی‌خبری مطلق به سر می‌برد.
این منبع همچنین گفته است خانواده مهدی روشنی تحت فشار قرار گرفته‌اند و به آنها هشدار داده شده درباره پرونده او سکوت کنند. به گفته این منبع، حدود یک ماه پیش به خانواده او اطلاع داده شده که وی با اتهام‌هایی از جمله قتل «احسان آقاجانی»، مامور پلیس، به اعدام محکوم شده است.
بر اساس گزارش‌های منتشر شده، احسان آقاجانی در جریان اعتراضات ۱۶دی‌ماه در شهرستان ملکشاهی کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77727" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Aufvwt1xeeO4B5NLBw9v4O73l7F1Lc97I8KOf0p68n4IUHJM6virmqJcs-XN7TvjJk1NWfg2IvPd4La43L3NwK4432hv3qeuyzh5NKXz8_qgGnGn3ThzPEEVkLQx_nD5eWh00xjhvKdK1jgeGpfVZ3AxgmalihUCYrwLGlT60GhM8omV-PB7v9pNC4fs-u6EtPpDz_wyp79Msl1UAjO0OoMrq60Mu4U2o7z8WKNAjTVOxANZvmxS-9Y5LzIcHeBUcAJVqgnd21vgg3Eye-6T3_JpeMTjlpr-8OwwgZI-Fwn6o-quA9XbfKi-pbuarhuWGdZOs8Nd1mEGr4qhB2wCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
آپدیت: برگشت
پیش از آپدیت:
نرم‌افزار پیام‌رسان «تلگرام»، روز دوشنبه، به‌طور ناگهانی از فروشگاه «اپ‌استور» شرکت اپل در سراسر جهان حذف شد.
بر اساس اعلام کاربران شبکه‌های اجتماعی، جست‌وجوی نام تلگرام در اپ‌استور با هیچ نتیجه‌ای همراه نیست و
صفحات رسمی دانلود
این برنامه با «خطای ۴۰۴» مواجه می‌شوند.
اگرچه این پیام‌رسان روی دستگاه‌هایی که از قبل آن را نصب داشته‌اند کماکان بدون مشکل کار می‌کند، اما امکان
دانلود تازه
یا نصب مجدد آن روی آیفون و آیپد فعلا وجود ندارد.
تاکنون هیچ‌یک از شرکت‌های اپل یا تلگرام بیانیه رسمی درباره دلایل این تصمیم صادر نکرده‌اند و مشخص نیست که این اقدام دائم است یا موقت و آیا ناشی از بررسی‌های قانونی و محتوایی است یا یک نقص فنی.
پیش از این نیز در سال ۲۰۱۸ اپل برای مدتی کوتاه تلگرام را به دلیل «نگرانی از انتشار برخی محتواهای خلاف قوانین» از اپ‌استور خارج کرده بود که پس از اعمال اصلاحات لازم، این برنامه مجددا بازگشت.
@
VahidOOnLine
🔄
و آپدیت چند ساعت بعد:
شرکت اپل اعلام کرد پس از آنکه در یک بررسی مشخص شد محتوایی مغایر با قوانین این شرکت در رابطه با «ممنوعیت سوءاستفاده جنسی از کودکان» در تلگرام قرار گرفته، این پیام‌رسان را به‌طور موقت از «اپ‌استور»، فروشگاه نرم‌افزاری اپل حذف کرده است.
به گفته اپل، پس از آنکه تلگرام «محتوای متخلف را به‌سرعت حذف و حساب کاربری منتشرکننده را مسدود کرد»،  دوباره به اپ‌استور بازگردانده شد.
تلگرام نیز در واکنش به گزارش‌ها درباره حذف این پیام‌رسان، در شبکه‌ اجتماعی ایکس نوشت: «گزارش‌های مرگ من بسیار اغراق‌آمیز است.»
@
VahidOOnLine
🔄
پست پاول دورف، مدیرعامل تلگرام درباره این موضوع، ترجمه ماشین:
🍎
دیشب، اپل برای مدت کوتاهی تلگرام را از اپ استور حذف کرد، زیرا یک کاربر به‌تنهایی محتوای پورنوگرافیک غیرقانونی را در یک گفت‌وگوی گروهی عمومی جاسازی کرده بود.
⬅️
تلگرام ظرف چند ساعت دوباره در دسترس قرار گرفت. اما می‌خواهم توضیح بدهم چه اتفاقی افتاد؛ هم برای هشدار دادن به دیگر توسعه‌دهندگان اپلیکیشن‌ها و هم برای کمک به محافظت از جوامع آنلاین در برابر حملات مشابه.
🧹
از آنجا که تلگرام با استفاده از گزارش‌های کاربران، فیلترهای هوش مصنوعی، هش‌های محتوا و دیگر ابزارهای نظارتی، محتوای غیرقانونی را به‌سرعت از گروه‌های عمومی حذف می‌کند، مهاجم ناچار شد به یک ترفند فنی متوسل شود. او با ویرایش یک پیام قدیمی در یک گروه فعال، محتوای غیرقانونیِ تغییریافته با هوش مصنوعی را در آن قرار داد. در نتیجه، این محتوا عملاً از دید اعضای گروه پنهان ماند و آن‌ها نتوانستند آن را ببینند و فوراً گزارش کنند.
💰
مهاجم یک «باج‌گیرِ حذف محتوا» بود؛ کسی که از صاحبان گروه‌ها باج می‌خواهد و در ازای آن، جوامعشان را هدف قرار نمی‌دهد. این باج‌گیران با استفاده از حساب‌های خودکار، محتوای غیرقانونی را در گروه‌های عمومی قرار می‌دهند و سپس مستقیماً آن را به اپل گزارش می‌کنند تا باعث حذف جوامع مشروعی شوند که صاحبانشان از پرداخت باج خودداری کرده‌اند.
🤝
از نظر عملی، محتوای پورنوگرافیک غیرقانونی در گروه‌های عمومی تلگرام یک مشکل نظام‌مند نیست. نظارت ما مؤثر است (
https://telegram.org/safety
). همین که مهاجمان ناچارند به محتوای دارای تاریخ گذشته و عملاً نامرئی و دیگر ترفندهای فنی متوسل شوند، این موضوع را ثابت می‌کند.
⚠️
با این حال، دو درس مهم برای توسعه‌دهندگان اپلیکیشن‌ها و جوامع آنلاین وجود دارد:
— باج‌گیران راهی پیدا کرده‌اند تا اپل را وادار به واکنش افراطی کنند. اپل پیش از تماس با ما، تلگرام را از اپ استور حذف کرد. این موضوع برای هر اپلیکیشن موبایلی که میزبان محتوای تولیدشده توسط کاربران است، یک خطر بالقوه و نظام‌مند ایجاد می‌کند. اگر اپلیکیشنی که بیش از یک میلیارد نفر از آن استفاده می‌کنند بتواند بدون هشدار قبلی از اپ استور حذف شود، هر اپلیکیشنی ممکن است حذف شود.
— تاکتیک‌های مورد استفاده باج‌گیرانِ حذف محتوا در حال تکامل است و جوامع در سراسر پلتفرم‌های اجتماعی را در معرض خطر قرار می‌دهد. تلگرام تجربه گسترده‌ای در شناسایی ترفندهای باندهای هماهنگِ گزارش‌دهی و محافظت از جوامع مشروع دارد؛ حتی وقتی این کار خطر حذف موقت خود اپلیکیشن ما از اپ استور را به همراه داشته باشد. ممکن است دیگر پلتفرم‌ها به همین اندازه آماده نباشند.
هوشیار بمانید!
☝️
durov
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/77726" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KWKcQrK6_6EK7HCp-0eOS_sfYYA6EGtCFawNqkWMuu8d78zz4CC9UzPAqnEA72A4-AhSzb10Ta3GLL2SbHMNv8poAOGHsHQaWXsdVmeD32VqIznJJmmI2_TK3vjWbxn2OK6I1EpTQAFIV_isH2uuyvAVmEyzPLuJGPup3nWrU5CXAQ4kajdGQNj-zMGm2lwwHrKxh_wfTyZVrtWjenG3lDGj26DGOIEmv4naxX7yxs2wXg5lKNXae2YIbcN5py2bhaC8ppr8QaGcRcELJST0IQ17kipgxUhry_jw4y4jiaEAsQs7R8uMANX5nBV8Lsd9vgxs2k5DUJ7MCp3N_NyVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)  گزارشی درباره وقوع یک حادثه در ۲۰ مایل دریایی شمال‌شرق الخصب در عمان دریافت کرده است.
یک کشتی باری از طریق کانال ۱۶ بی‌سیم VHF اعلام کرده است که با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
مقامات در حال بررسی هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77725" target="_blank">📅 03:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu13yVu02aG9YeKBATEl9G53kRZXYIfib-GQyUN4NLTeqgrP17cabSyd-HBONBbzClMIGMF7Zf0Ucb27GjB-xJ_YxP15__JeBNjTHQ0Tu31z5B4LNJxNTBFuq23CBY0Wul79JSeYKEci0cX-eB5IA15zmkhD9RiiIijFy56bYe_li6bHVVk8nFeswnVUkq-j6icsYBLs4SMVGUqwLgJ7JBtwj_cs_7xFb3w0u9OWFozXOML3dii0XjYypRP1yt5gm49ZiMCDzoOAiMtKrOBE-ZP3HigJxOe1XEJDBPzWO9sx5nggDsUgVNix_8vr8qEPuKirCGjw7tO8_CMQxYvFlgUs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu13yVu02aG9YeKBATEl9G53kRZXYIfib-GQyUN4NLTeqgrP17cabSyd-HBONBbzClMIGMF7Zf0Ucb27GjB-xJ_YxP15__JeBNjTHQ0Tu31z5B4LNJxNTBFuq23CBY0Wul79JSeYKEci0cX-eB5IA15zmkhD9RiiIijFy56bYe_li6bHVVk8nFeswnVUkq-j6icsYBLs4SMVGUqwLgJ7JBtwj_cs_7xFb3w0u9OWFozXOML3dii0XjYypRP1yt5gm49ZiMCDzoOAiMtKrOBE-ZP3HigJxOe1XEJDBPzWO9sx5nggDsUgVNix_8vr8qEPuKirCGjw7tO8_CMQxYvFlgUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مربوط به ایران
متن مکالمه با تشخیص و ترجمه ماشین
:
به دلایلی، وقتی در حال مذاکره‌اند، دوست ندارند بگویند که دارند مذاکره می‌کنند. من می‌گویم: «صبر کنید، ما در حال مذاکره‌ایم. چه اهمیتی دارد؟ داریم مذاکره می‌کنیم.» و آن‌ها گاهی آن را انکار می‌کنند، با اینکه ساعت‌ها و ساعت‌ها کنار یکدیگر می‌نشینند و مذاکره می‌کنند.
مذاکرات در حال پیشرفت است.
قرار بود دیروز آن‌ها را به‌شدت هدف قرار دهیم؛ بسیار بسیار شدید. حمله‌ای شدیدتر از هر حمله دیگری.
فکر می‌کنم می‌توانم بگویم—و ژنرال‌ها از روی آگاهی می‌گویند—شدیدتر از هر حمله‌ای از زمان جنگ جهانی دوم تاکنون. این خیلی بزرگ است.
ما آماده اجرای حمله بودیم که آن‌ها تماس گرفتند. علاوه بر آن، عربستان سعودی تماس گرفت، امارات تماس گرفت، قطر تماس گرفت و افراد بسیاری با من تماس گرفتند. نمی‌خواهم از کلمه «التماس» استفاده کنم، اما به‌ویژه ایران نمی‌خواست هدف حمله قرار بگیرد.
آن‌ها گفتند: «می‌خواهیم مذاکره کنیم. می‌خواهیم درباره تنگه مذاکره کنیم.» اما از دیدگاه من مهم‌تر از آن، می‌خواهیم درباره هسته‌ای‌زدایی ایران مذاکره کنیم، زیرا اصل ماجرا همین است. دلیل اینکه این کار را انجام می‌دهم همین است.
این کار باید مدت‌ها پیش انجام می‌شد. اکنون ۵۰ سال شده است. همیشه می‌گفتیم ۴۷ سال، اما سه سال دیگر نیز گذشته است. ۵۰ سال است که رؤسای‌جمهور دیگر باید کاری را که من انجام می‌دهم، انجام می‌دادند. یا کشورهای دیگر؛ لازم نبود حتماً ما باشیم، اما کشورهای دیگر باید این کار را می‌کردند. هیچ‌کس انجامش نداد و زمان آن فرا رسیده بود.
ما درباره تنگه صحبت می‌کنیم؛ بازشدن تنگه و اینکه به معنای واقعی کلمه تا فردا کاملاً باز باشد. این مرحله اول است.
مرحله دوم این است که پس از آن درباره موضوع هسته‌ای  صحبت کنیم. اساساً هسته‌ای‌زدایی ایران باید انجام شود. باید انجام شود. این مرحله دوم خواهد بود.
اما
مرحله نخست، بازشدن تنگه است. مرحله دوم هسته‌ای‌زدایی خواهد بود. آن مرحله کمی زمان می‌برد، اما ما در این زمینه بسیار قاطع هستیم.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من هرگز موضعم را در این‌باره تغییر نداده‌ام.
درباره کشتیرانی در تنگه هرمز: من اجازه نمی‌دهم از کسی پول بگیرند. ما طرفی هستیم که کنترل کامل را در اختیار دارد. ما کنترل کامل داریم.
می‌دانید، چیزی به نام محاصره داریم که با این نیروی دریایی اجرا می‌شود و به آن «دیوار فولادین» می‌گویند؛ «دیوار فولادین ایالات متحده».
نه، نه، هیچ پولی گرفته نخواهد شد. اصلاً درباره گرفتن پول صحبت نمی‌کنیم. پولی گرفته نخواهد شد.
فکر می‌کنم به این واقعیت بسیار افتخار می‌کنم که به مردم فرصت می‌دهم. به مردم فرصت خواهم داد. انجام حمله‌ای به آن بزرگی علیه یک کشور، تصمیم بسیار بزرگی است. ترجیح می‌دهم اکنون آن را انجام ندهم.
امیدوارم سر عقل بیایند
قرار بود حمله دیشب آغاز شود و مدت زیادی ادامه پیدا کند و در نهایت عملاً چیز بسیار کمی باقی بماند؛ هیچ‌چیز باقی نمی‌ماند.
اگر این فرصت به من داده شود که اجازه دهم افراد زیادی زنده بمانند، می‌خواهم آن فرصت را به آن‌ها بدهم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77724" target="_blank">📅 23:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9_PbHIUpceT9wSBryd7rwVnzFKuyq1NdJVuxWO9oYz1Tt-XjOWwmKecIW4vRSoOaEkMhuzOFeN16m-dcnnCX7nWeF7hCM7Gn7-wBxXmCFKsjdGpk5K-8BuDGK_DZVzxIFqRhQFpAIx4XvhK-ulxCawEHKNr-9GiZ3wMYCTkqGvygxaH2y5e2jQ08LAvf8V2Ke0fyFbveX-40XF7cICUrSuee_nspK_LmJBumGctOhVMKQwXzFrS5m8Hftq7j3gj9CP2JpNAqA0xW8ppMjBoxwIim446jdnGmDmdV3hrkov0A8uJISCUJz5vKnnR8ceFW9iLViBckwGkBHliF3wjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه ۱۲ مرداد در حاشیه نشستی در کاخ سفید، به خبرنگاران گفت مذاکراتی که در حال حاضر با جمهوری اسلامی ایران جریان دارد، «آخرین فرصت» تهران برای امضای یک «توافق خوب» است.
ترامپ که پیش‌تر حمله‌ای که به گفته او «بزرگ‌ترین حمله نظامی از زمان جنگ جهانی دوم تا کنون» بود علیه ایران را لغو کرده بود، با انتقاد دوباره از مقام‌های جمهوری اسلامی که انجام مذاکره با ایالات متحده را تکذیب کرده بودند، گفت: «ایرانی‌ها تماس گرفتند، بعد از آن از عربستان سعودی، قطر، امارات و بسیاری کشورهای دیگر با من تماس گرفتند که یک فرصت دیگر بدهم. نمی‌خواهم بگویم «التماس» کردند ولی ایران واقعا نمی‌خواست مورد حمله قرار بگیرد.»
ترامپ تاکید کرد که این مذاکرات «با درخواست ایران» و حمایت کشورهای منطقه و جهان انجام می‌شود و «آخرین فرصت» برای جمهوری اسلامی است که انتظارات او درباره برنامه هسته‌ای را برآورده کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77723" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SrnKqjGScFvzqqOxRqLWOW7txWlIzrbw27Dzt7vgGl61mHUsxh-01ImCpeu7YC7zqa0VEoHWXrebDFN2TdGxiX-cc3svgQ_xlUAhOlt-08UKg8DM0jHAFTh5PpMOlc51tu0S1Gp7_D3uzpavR6LK6y6NxnlHdY0a8b06dQg9ZF430CmSj_463_UBN7_Kx2rcdmJ41aN39z7A2AubpYMzSpWbJhhdG1tlGKrlrzT6iWWQ7_9VwwVw393AHBih2XYdrKnLhoZtiRIwTAk656s0_YmvIvq7kcvqDmSO3WWkNczYHrBe2toB8CQS4HutXYUp3MmV7CJwA0ddynd9c2sivA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رهبری ایران به‌طرز باورنکردنی دورو است!
آن‌ها درخواست جلسه می‌کنند ــ بعضی‌ها می‌گویند «التماس می‌کنند» ــ مذاکرات آغاز می‌شود و جلسات بیشتری نیز برای آینده بسیار نزدیک برنامه‌ریزی می‌شود، اما بعد آشکارا و با افتخار می‌گویند که هیچ گفت‌وگویی ندارند، درباره هیچ‌چیز صحبت نمی‌شود و فقط با «عمان» سروکار دارند.
سپس همان یاوه‌گویی‌های همیشگی‌شان را ادامه می‌دهند و می‌گویند تنگه هرمز با قدرت توسط آن‌ها اداره خواهد شد، در حالی که این تنگه همین حالا نیز کاملاً تحت کنترل نیروی دریایی ایالات متحده و «محاصره» ما قرار دارد؛ یا همان‌طور که بعضی‌ها می‌گویند، «دیوار فولادین ایالات متحده»!
هیچ‌چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ‌چیز نیز نخواهد رسید، مگر آنکه توافقی حاصل شود یا تسلیم کامل صورت بگیرد. چه ایران بخواهد این را بپذیرد و چه نخواهد، ما در واقع در حال گفت‌وگو درباره راه‌حلی برای مشکلی هستیم که آن‌ها طی چندین دهه ایجاد کرده‌اند.
موضوع بسیار ساده است: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77722" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edfchGAuJR2OHg1HcoQZ0WN0wUI3DRdsH6Tz_D5oFpLm-cikL1Mf5n8ySoIhGbK5_BOJC5jMf16dJ_qj2TzhWd-8A_xDTqtodPJNjiugCen2xyb51tvtiGumqduiQeE4YUow_yQGU0RJYR_rHg-whtWLgWOlYsZkriTHq8kMUAtwUNHSCENL7M2A7J1_zaZiEY1Had5BWJEtbEpFh26X2PgV9DZhHg4ed-ezmCccCG9zRSsIZzsQk0Lx5OPNodfxjS79zJHQJcuMgwxjZGF3qqOPaHfseFtPbe34BHVXo1zayrnTflMvyDiSb9v3IyhqqeyN--cRr6n6bEVR3Fk8nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیران امور خارجه جمهوری اسلامی ایران و پاکستان در گفت‌وگویی تلفنی درباره تحولات منطقه‌ای و روند تحرکات دیپلماتیک رایزنی کردند. در این تماس، محمد اسحاق دار، وزیر امور خارجه پاکستان، از عباس عراقچی برای سفر به اسلام‌آباد در نخستین فرصت دعوت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77721" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqsp1SJ_Q3XHKViNEHhBnFC58rSgL8dfBg3QmyCXDNFLaPHMtPHi1xchLk07QB7KXYTB9SUViqWBmX3O8BPiBICY1wv4TKazvCGfnNFHBEa1Uu4lgBCiufc66F4a9mHhudZ7ukUfkeuTd5YR8GCff73kmSAlOesSzFa2KvMb8Kb10XbGXkiMmey1q9b1ZVOcrZm-XUrc1MqW4fYBI_DDj6Gysu32PVwq-PuXBi1XnAfq_bTmMVJST8kSoPrLLzE9jtwS6Xp_o1eA7lvn9jFqd2FsReok0vW-k5j3ORbYhO5vUjSx6j8f06hfirzXI0t5J4rsAOcBer9e5McpAREiqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا روز دوشنبه ۱۲ مرداد بار دیگر از شرکت‌های نفتی خواست قیمت بنزین را برای مصرف‌کنندگان آمریکایی کاهش دهند و مایک ویرث، مدیرعامل شورون، را به‌دلیل قدردانی نکردن از تلاش‌های دولتش در حمایت از صنعت نفت مورد انتقاد قرار داد.
دونالد ترامپ در یک مصاحبه تلویزیونی، ویرث را سرزنش کرد که به نقش دولت او در کمک به شرکت‌های نفتی اشاره نکرده است.
او در پیامی در شبکه اجتماعی خود، تروث سوشال، نوشت: «تنها چیزی که او به‌راحتی از گفتنش صرف‌نظر کرد این است که بدون نبوغ، دوراندیشی، قدرت و ثبات دولت ترامپ، صنعت نفت و حتی خود کشور ما نابود می‌شد!»
ترامپ افزود: «برای مثال، آن‌ها مایک و شورون را از ونزوئلا بیرون کردند، اما حالا بازگشته‌اند، بزرگ‌تر و قدرتمندتر از همیشه، و انتظار دارند ثروت هنگفتی به دست آورند!»
به گفته ترامپ، «این موضوع شامل سایر شرکت‌های نفتی هم می‌شود... و همین حالا قیمت نفت برای مصرف‌کننده را پایین بیاورید!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77720" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRHVliAUw6dGzFUbbpZ_Hxwn6q9QdrK6YNCx0tXeInG0KEmYi4b21CQx2YaLNjV7pmouSieCX_PZ70DsQo0obEG2h-pI09gNvNTWDqnHUfNsI6WSWJiIMq6MKk4OBPPxAo1XjDMkedoyj4yLh5iGETdeXMHPHNtuB0p-VtaVKnPczwK1jbbQuymDleUIZuUMFVnm4zNvu9G6Oa7DwHMiQDTetvrk_bsLi-YEkf24K4_Nwuiw6qOdxWRnftL66RvbamskQiSigkH12qCFRUfNRzyujjVf_a76OpgJk3UY1lmdxV-ZmLe-731mOzltIaYJeO66s78IOOIwLdccX6pR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی‌رغم افزایش امیدها برای دستیابی به پایان درگیری‌ها میان اسرائیل و گروه‌های فلسطینی، مقامات امدادی غزه اعلام کردند حملات هوایی اسرائیل برای دومین روز پیاپی به مناطق مختلف این منطقه در روز یکشنبه یازدهم مرداد، جان دست‌کم ۱۸ فلسطینی را گرفت.
به گفته مقام‌های بهداشتی فلسطینی، از بامداد یکشنبه، جنگنده‌های اسرائیلی شهر غزه در شمال، شهر دیرالبلح در مرکز و منطقه خان‌یونس در جنوب نوار غزه را هدف قرار دادند که بیشترین شمار تلفات روزانه در چند هفته اخیر را بر جا گذاشت.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از دستیابی به یک پیشرفت در تلاش‌ها برای اجرای توافق آتش‌بس سال گذشته خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77719" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTaACJ3jcL3N_942G-kr6jFzBbRSSd0_I7O7r2ojv5q__5vDqCO1OXZWTlYAoyr6l5PBh02rolY4hBSEtb96Wfn6_wu2EA8ksXadVs3E-h03iuyzkhELzNOP0LJYj-XpW0x6nrqYvTM6OYs1-fSiJvUW83P0vMJHxpz6Cug5vI0MsuauowaN6zp4RGu5KLmcpsuvIuFqYM5ATXJ0TTOKbRswRGZeIRSkQZrj5kl2z8m7qx87ThYbJ5CGgF5yWZ4G30m83ybH2dTIP2ZwltfbKoy4_qCbpXEA1G1Ixz_fhtzdje6JESAjMxbfmqd9xlHbj-Q8yGQr_FUCNukwoBY9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز دوشنبه ۱۲ مردادماه گزارش کرد که «سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه» یک پهپاد ام‌کیو۹ را در آسمان تنگه هرمز رهگیری کرده و «مورد اصابت» قرار داده است.
این خبر در حالی اعلام می‌شود که دونالد ترامپ، رئیس جمهوری آمریکا از توقف طرح یک حمله بزرگ به ایران به شرط توافق برای بازگشایی تنگه هرمز و اطمینان از دست نیافتن ایران به سلاح هسته‌ای خبر داده بود.
مرکز فرماندهی ایالات متحده (سنتکام) هنوز واکنشی به این خبر نشان نداده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77718" target="_blank">📅 17:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OjLNNoR9I6NGF7Qxphkz9tHKNtIBe-icpkwXTIb2kQOEkO8xKoXgWZFys0XgblydaGyekxcRSKSYoGy9Ujq2uem5YFgQDirx7tVKUgJ4reav19dFE5Et9tyurb4RwSEZLBSNhPkU77yMDhwLJzyO8RZzwG8bq0rbfQaZhpLpe1H4mn7X1ZN4arYQo4BXWVoZWHjOFVCsClxyxfwvh00VckqAqAX6ywS3PJCsvUpoC8jdSrwOGKzEDet5UpeNM18cxGh0v85TgdEEK1g0nJMZW4AL36mCPtVqz_Q7Gq7TzqYDsu3rzPuVU58S6XouH8D91kwaxFWYtC_TvUjvpYQ8fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30d5424a40.mp4?token=OxPhEOSahFWNaIVfnOgiMfG3ZjwojZyM4_zSkTmxrzYVeyEZFkL3xXxwDX6RlrDufTeqCuwhB0NgT0EUO3dYkaaXxiQMRx17dj84dYYNy2DMdmCOil-2VyGK62XRgs5MhDNiIoH2Hbe8qeQMNo1Dw3j90Ij4cJ8B5KE21YqT8BemEtqJb2LZle0f7KD-aQtpYT-CVTf4TvGTGCaD5N5CGA586HZGXm2I0vVDrolHwhv0tK9jKuvsyYvIfsbUkGBxTbSDjySXbVO83ifHZkssWRfPdBjSg9gdawsgyjl9jqDkjr2daWFzXkxE2KlOLoX0O9q-7XH2-CVsVcas6_vVzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30d5424a40.mp4?token=OxPhEOSahFWNaIVfnOgiMfG3ZjwojZyM4_zSkTmxrzYVeyEZFkL3xXxwDX6RlrDufTeqCuwhB0NgT0EUO3dYkaaXxiQMRx17dj84dYYNy2DMdmCOil-2VyGK62XRgs5MhDNiIoH2Hbe8qeQMNo1Dw3j90Ij4cJ8B5KE21YqT8BemEtqJb2LZle0f7KD-aQtpYT-CVTf4TvGTGCaD5N5CGA586HZGXm2I0vVDrolHwhv0tK9jKuvsyYvIfsbUkGBxTbSDjySXbVO83ifHZkssWRfPdBjSg9gdawsgyjl9jqDkjr2daWFzXkxE2KlOLoX0O9q-7XH2-CVsVcas6_vVzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی، می‌گوید در حال حاضر مذاکره‌ای بین ایران و آمریکا در جریان نیست.
اسماعیل بقائی در نشست هفتگی خود با خبرنگاران در روز دوشنبه ۱۲ مرداد، افزود آنچه در حال حاضر در جریان است، مذاکرات دو جانبه و بین دو دولت ساحلی ایران و عمان است.
او  می‌گوید که «حضور دیگران در این مذاکرات می‌تواند سازنده یا مخرب باشد اما موضوع بین ایران و عمان است.»
اظهارات او در شرایطی بیان می‌شود که دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرده که مذاکرات با ایران بعدازظهر دوشنبه ۱۲ مرداد آغاز خواهد شد.
با این حال او روز یکشنبه، هنگام بازگشت از تعطیلات آخر هفته در نیوجرسی به واشینگتن، به خبرنگاران توضیح نداد این مذاکرات در کجا برگزار می‌شود یا چه کسانی در آن شرکت خواهند کرد.
@
VahidHeadline
سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس می‌گوید در حال حاضر «هیچ بحثی» برای مذاکره با آمریکا در دستور کار قرار ندارد.
حسن قشقاوی در گفت‌و‌گویی که خبرگزاری دانشجو منتشر کرده، افزوده که حکومت ایران به‌ویژه در پرونده هسته‌ای، با واشینگتن مذاکره نمی‌کند.
او بدون اشاره به جزئیات افزود: «حتی در مسیر‌های احتمالی دیگر نیز بحث هسته‌ای مطرح نبوده و آینده این پرونده در متون مربوطه کاملاً روشن است».
این نماینده مجلس، اولویت فعلی جمهوری اسلامی را «لغو تحریم‌های اولیه و ثانویه در کنگره و بازگرداندن اموال بلوکه‌شده ایران» عنوان کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77716" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77715">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4T_wqd86UBgTNbZ2wvbiHPt45OfJmaj0g2tRz5Jqfls8aW57PGh957_94FkR0bTspJw9lhumz_f02fI9WOKfkOfcs-42hspeonKDLxmirAiWL8jI1LulRcLxCSP4EU-HK1uO1DHFN9Vx7trQg0gfjryIs9x8QdqfpvtHc8tjUKAl2qQ-E8_GmcDa_qc-U7-aA7Dr6caUiPudxK9lFot8k83mHmFnHbipnReC3YiIr9IsGX_TDyGcHamx7zcaNsm9D3NxQIli0vK53mTiSreWchJlxrDQAUAYPVf0L9-vXI2tKNMRA1YJMqlbm9uwlOk9JgHEqctBBOl6EqDR1NO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ آمریکا، روز یکشنبه ۱۲ مردا گفت نیروهای این کشور همچنان در آماده‌باش هستند و آمادگی اقدام دارند؛ اظهاراتی که نشان می‌دهد تصمیم دونالد ترامپ، رئیس‌جمهوری آمریکا، برای به‌تعویق انداختن حمله به ایران، تأثیری بر آمادگی نظامی نگذاشته است.
پیت هگست در شبکه اجتماعی ایکس و در کنار انتشار ویدئویی از رئیس‌جمهوری آمریکا نوشت: «وزارت جنگ آماده اقدام بود و همچنان در سطحی که از زمان جنگ جهانی دوم دیده نشده، آماده است.» هگست سپس گفت ارتش «کاملاً مسلح و آماده شلیک» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77715" target="_blank">📅 17:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPg6Xlc5soaNwezGMpSHTAFxGl5rnZnK6HZ8-wOLhe8uDkZo0Fw6-QlDzzGdQnhI8tpf-DxnYfTL0B9g2djid4wSqtwMpUhH-ZkNFIMezhu_WCGUbgWxLZzyQSwaEt6sCABt98s8eiTpYH8v95GdN_EjJj1vLw5wg6BUP_OKUaoJniNW-jzGdWiZEBYTZvR9Ocr9_BbEvDq-58hiT2E63HNxc78BAXEW2x6jXcCFBCpsHSv9WLic4UsBwjJykFWAi17O6It7EN349IJQwGc1TB3C83hbXwSMzIif4nTVmdbhj6KDV3T1BDkg84FVMoZRJeBJZoFS4xBXI03lI87oYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
خبرگزاری فارس از کشف یک خط لوله ۹۰۰ متری غیرمجاز انتقال نفت در استان بوشهر خبر داده و نوشته این لوله نفت سرقت شده را به مخزنی زیرزمینی منتقل می‌کرده است.
به گزارش فارس، فرماندۀ انتظامی استان بوشهر گفته است: «انشعابی با لولۀ ۴۲ اینچی به طول ۹۰۰ متر، و مخزن زیرزمینی ذخیرۀ نفت در شهرستان دشتی استان بوشهر شناسایی» شده است.
این مقام محلی به فارس گفت که «تاکنون بیش از ۵۰ هزار لیتر نفت خام به ارزش ۵۰ میلیارد ریال کشف و تجهیزات» مرتبط با این خط لوله غیرمجاز توقیف شده است.
در این گزارش به مشخصات فرد یا گروهی که در احداث و بهره‌برداری از این خط لوله غیرمجاز نقش داشته‌اند اشاره‌ای نشده است و معلوم نیست آیا آنها شناسایی و تحت تعقیب قرار گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/77714" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-VOFkitWOG3uh3AbqEmO30AS8znzbKfKrbHymFIe-SuWpQQxTaO66UhqMk7e7zHdTksPIxXXZMahHsC_pxhqQImlleI7oLxmK9a3MYYh49uHhR1Lvu2HY7DXZ9uAXbCZWVdkUBT59TXC3OR3cAwrBQmmvBxj-9_nKr9TPoNWHTLAbCLJ87HNAGXoiOCyWain_U1JL85BwaGDDKna2b__CoCPiBghkhJ5RbchFendkP_E6WjX-wvCCDl_ZM78iqCHTjegwItiKE9cNEhJoBgw0EwwuBUcK2EK6qnrAVLd--hSRVEaEhWuimTMouXO3-77OvAAdbmqCCYCD_9yD07jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت جهانی نفت دوشنبه ۱۲مرداد۱۴۰۵ پس از اعلام «دونالد ترامپ» مبنی بر توقف حمله نظامی آمریکا به ایران و آغاز دور تازه مذاکرات میان دو کشور، بیش از پنج درصد کاهش یافت.
خبرگزاری «رویترز» گزارش داده که بازارهای جهانی، کاهش احتمال درگیری نظامی در خاورمیانه و افزایش امید به دستیابی به توافق میان تهران و واشنگتن را مهم‌ترین عامل افت قیمت نفت می‌دانند. به نوشته این خبرگزاری، نگرانی معامله گران از اختلال در عرضه نفت و بسته شدن احتمالی تنگه هرمز، پس از اظهارات ترامپ کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77713" target="_blank">📅 17:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f4-nTVwBv69YVTTTV1YctqOrHw3-PVl52FN10POaSoUiiSI3NYWA_MNo9czIw1S4milxxXErERTcfT_WMeYpAhjmyFe2RB8d5fccqPAnp1bFj7nCoAUiSvyoCQ1G_xcItUEwxaHZb_Kfa55Omwk0n7uKBeUFvi61D8TEI894G4zJYmI-Y63Syh2LErRY2AHxszEGd2VsFBf2g-03wqYipRTjC6-iJGIjSz-fU0VvylZYlJeb2gJPpjB46h3YilQdd3-2eTu-59U-QYy796DJsWAN0iJpYFWJtemriDhADWA59r_2qmyRhmsLDdQ78lf-0BdwH4YIgGt7lkpwdjZD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» رسانه وابسته به قوه قضاییه جمهوری اسلامی از اعدام دو زندانی به نام‌های «امید بهزاد» و «پوریا صفوت» به اتهام «جاسوسی» و «همکاری اطلاعاتی» با اسراییل از طریق «ارسال تصاویر مراکز امنیتی و نظامی» جمهوری اسلامی خبر داد.
خبرگزاری میزان، ارگان رسمی قوه قضاییه، اعلام کرد این دو زندانی بامداد دوشنبه ۱۲مرداد اعدام شدند.
به ادعای این نهاد، «بررسی‌های فنی» انجام‌شده روی تلفن همراه امید بهزاد این موارد را تایید کرده و او نیز «در جریان تحقیقات» به آنها اعتراف کرده بود. با این حال، مشخص نیست این اعترافات در چه شرایطی از او گرفته شده است. جمهوری اسلامی طی بیش از ۴ دهه حکومت خود، بارها اقدام به اخذ اعترافات اجباری کرده است.
در گزارش میزان، پوریا صفوت نیز بدون ارائه هیچ‌گونه سند یا جزییاتی، به همکاری «مستقیم با موساد» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77712" target="_blank">📅 17:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e5fb7b499d.mp4?token=sHdPcbiw_QJ0H8kAuWrkHug-e_nnMwyiq9myMSQH0XjsrAJ931DdfJlUmwd7YhG17nH6pFHb6vWwpvTpKRjFeCFMGOSfifSISNPhDSfHBcsbBKvQ08K5pryoeOXkjOuCf-uTXnPOokbVsiMNXX2z9lti-gJHUthTDC_Pq1_awWHWUomvXGoy0DSESdPmT3p5Ktvv_ep3Isb4XDnIJ_TcL6DpZ1yrA9mZ6JunAsiD5adYv_rDdEKEoKRWz5LToKKl6uan5OL1o_8iE3Ed1FNNPMHu-EHvMLaSBpVxWtkRiawagHyIv-i0io49KOULkNEIWFbXAmckSge81erTScL3ZCy4RrZFvLeBi4hi0dJVZzmpWv0hOJf1tgvr8w6x4mTErEM823DpdpfJZl1puVHWLvNJR9duZ_E11rbC_BxadtkKTGOSNYn9t4I0dojSVNr3TgFfRzsMEs61RgUO-lt8Pl1NPcVl2JC1SUbJDvoU_zKDKQOx2a6Hftnm0LSX5oZFe29NDlwrhfax8yZqi0sGbqGkRJhZeGKjshIQw07K6fd4aJl8aYPXYPpc1cmTKHB5syRyrt29XKVpRHbl3x9iT-mO1R7HXNhbz4HyevRvg2dG-ysrj2LV7i1f1nqZnY3iRIRHVvO_mqrUGchrgQ2VUyOvZNkY32HCqAeKPTPn4j8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e5fb7b499d.mp4?token=sHdPcbiw_QJ0H8kAuWrkHug-e_nnMwyiq9myMSQH0XjsrAJ931DdfJlUmwd7YhG17nH6pFHb6vWwpvTpKRjFeCFMGOSfifSISNPhDSfHBcsbBKvQ08K5pryoeOXkjOuCf-uTXnPOokbVsiMNXX2z9lti-gJHUthTDC_Pq1_awWHWUomvXGoy0DSESdPmT3p5Ktvv_ep3Isb4XDnIJ_TcL6DpZ1yrA9mZ6JunAsiD5adYv_rDdEKEoKRWz5LToKKl6uan5OL1o_8iE3Ed1FNNPMHu-EHvMLaSBpVxWtkRiawagHyIv-i0io49KOULkNEIWFbXAmckSge81erTScL3ZCy4RrZFvLeBi4hi0dJVZzmpWv0hOJf1tgvr8w6x4mTErEM823DpdpfJZl1puVHWLvNJR9duZ_E11rbC_BxadtkKTGOSNYn9t4I0dojSVNr3TgFfRzsMEs61RgUO-lt8Pl1NPcVl2JC1SUbJDvoU_zKDKQOx2a6Hftnm0LSX5oZFe29NDlwrhfax8yZqi0sGbqGkRJhZeGKjshIQw07K6fd4aJl8aYPXYPpc1cmTKHB5syRyrt29XKVpRHbl3x9iT-mO1R7HXNhbz4HyevRvg2dG-ysrj2LV7i1f1nqZnY3iRIRHVvO_mqrUGchrgQ2VUyOvZNkY32HCqAeKPTPn4j8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، می‌گوید که «مذاکرات جدید» با ایران روز دوشنبه آغاز می‌شود.
آقای ترامپ گفت که در حال حاضر توافقی درباره تنگه هرمز وجود دارد و توافقی هم درباره هسته‌ای زدایی ایران حاصل خواهد شد.
@
VahidHeadline
گفت‌وگوی ترامپ با خبرنگاران در هواپیما
تشخیص و ترجمه ماشین:
🔺
خبرنگار:
چه چیزی باعث شد حملات دیشب را لغو کنید؟
🔻
ترامپ:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند این کار را انجام دهم.
ما تقریباً همین موقع کاملاً آماده اجرای عملیات بودیم و قرار بود حمله‌ای عظیم باشد. همه‌چیز برای اجرا آماده بود. اما وقتی متحدان می‌خواهند حمله را لغو کنید، ناچارید بگویید: «خب، ببینیم چه می‌شود.»
دلیل درخواستشان این است که فکر می‌کنند توافقی وجود دارد. توافقی دربارهٔ [واژه نامفهوم] وجود دارد و بعد هم توافقی درباره موضوع هسته‌ای حاصل خواهد شد؛ یا می‌توانید آن را «هسته‌ای‌زدایی از ایران» بنامید. من آن را هسته‌ای‌زدایی از ایران می‌نامم.
فعلاً آن را متوقف نگه داشته‌ایم. فقط باید ببینیم چه می‌شود. هر زمان بخواهیم می‌توانیم آن را انجام دهیم.
اما سه طرف اصلی از ما درخواست کردند. ایران هم با تأکید زیادی از ما درخواست کرد. گفتند: «مایلیم توافق کنیم.»
حالا نمی‌دانم بیرون چه می‌گویند، چون خیلی وقت‌ها این را به من می‌گویند و بعد بیرون می‌روند و می‌گویند: «نمی‌دانیم او درباره چه حرف می‌زند.»
بدیهی است که نمی‌خواهند مورد حمله قرار بگیرند. آن‌ها از وسعت حمله خبر داشتند، چون [عبارت پایانی نامفهوم است].
🔺
خبرنگار:
حالا چه اتفاقی می‌افتد؟
🔻
ترامپ:
کاری که اکنون انجام می‌دهیم این است که در قالب مذاکره با آن‌ها گفت‌وگو می‌کنیم. مذاکرات فردا بعدازظهر آغاز می‌شود و خواهیم دید آیا واقعیت دارد یا نه.
خیلی دوست دارم این اتفاق بیفتد. جان‌های زیادی نجات پیدا می‌کند و [ادامه جمله نامفهوم است].
سال‌های بسیار زیادی طول می‌کشید تا بتوانند آن را دوباره بسازند؛ البته اگر اصلاً امکان بازسازی‌اش وجود داشت. فکر نمی‌کنم حتی قابل بازسازی می‌بود.
حمله‌ای آماده کرده بودیم که اگر انجام می‌شد، بزرگ‌ترین حمله از زمان جنگ جهانی دوم می‌بود.
برای آن‌ها فاجعه‌بار می‌شد و نمی‌خواستند ما آن را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم آن را نمی‌خواست. آن‌ها فکر می‌کردند توافقی قریب‌الوقوع است.
🔺
خبرنگار:
آیا ضرب‌الاجلی وجود دارد، قربان؟
🔻
ترامپ:
توافقی قریب‌الوقوع است که به [واژه نامفهوم] و در نهایت به هسته‌ای‌زدایی از ایران مربوط می‌شود.
وقتی این را می‌شنوم، می‌گویم: «آیا می‌خواهیم تا این اندازه شدید عمل کنیم؟»
گروهی از مردم هستند که می‌خواهند من فوراً این کار را انجام دهم و گروه دیگری از مردم هم هستند که نمی‌خواهند من این کار را انجام دهم.
🔺
خبرنگار:
آقای رئیس‌جمهور، آیا ایران برای رسیدن به توافق ضرب‌الاجلی دارد؟
🔻
ترامپ:
باید ببینیم. ببینیم اوضاع چگونه پیش می‌رود. هر زمان بخواهیم آماده‌ایم وارد عمل شویم.
آیا ترجیح می‌دهم توافق کنم؟ من در پی کشتن مردم نیستم، چون مردم کشته می‌شوند؛ تعداد زیادی از مردم کشته می‌شوند و ما این را نمی‌خواهیم.
بنابراین آن‌ها از ما درخواست کردند؛ مشخصاً ایران. اما آن سه طرف دیگر هم گفتند که واقعاً...
از آن‌ها پرسیدم. [اشاره نامشخصی به پادشاه و سپس ولیعهد.] گفتم: «ترجیح می‌دهید چه کار کنیم؟ ترجیح می‌دهید ما این کار را انجام دهیم یا نه؟»
گفتند: «ما توافق را بسیار بیشتر از حمله ترجیح می‌دهیم، چون نمی‌دانید این [واژه نامفهوم؛ احتمالاً اشاره به حملات یا اقدامات] به کجا منتهی می‌شود.»
آیا کشورشان با ورود سیل‌آسای مردم و فاجعه روبه‌رو خواهد شد؟ اتفاق‌های بد زیادی ممکن است رخ دهد.
🔺
خبرنگار:
قربان، گزارشی منتشر شده است که می‌گوید نیروهای آمریکایی را از بحرین و کویت خارج می‌کنید. آیا نیروها از خاورمیانه خارج می‌شوند؟
[در ترنسکریپت هیچ پاسخی از ترامپ به این پرسش ثبت نشده است.]
....
🔺
خبرنگار:
بازگردیم به ایران؛ آیا آماده بودید اهداف انرژی را هدف حمله قرار دهید؟
🔻
ترامپ:
نمی‌خواهم این را بگویم. نمی‌توانم این را بگویم.
قرار بود حمله‌ای عظیم باشد. قرار بود حمله‌ای باشد که با فاصله بسیار زیاد، بزرگ‌ترین حمله از زمان جنگ جهانی دوم می‌بود.
اما از ما خواستند آن را انجام ندهیم. گفتند: «لطفاً این کار را نکنید.»
همسایگانشان هم همین را گفتند.
بنابراین فقط می‌خواهیم ببینیم آیا می‌توانیم درباره هسته‌ای‌زدایی به توافق برسیم یا نه.
🔺
خبرنگار:
[پرسش ناقص درباره اینکه مذاکرات فردا انجام می‌شود.]
🔻
ترامپ:
بله.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/77711" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77710">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tU1XU7255a5TBehtNyzvHO1Gy1LiwgFpHlzyAezOnxFrbqnWGpW59TI9L0yS_Gls6-DT_K6HW9ow8hhQJcWQqTkTi_hOmEcglH1MHmtkqbxTWDIfKMCxLzJlB5MIkiKeYY4uCkX7vIT2q5c_2GSKgld9vTJplDu38sviNFOqnxbzALM59hICZgNC3Dssx6Sv-y3rcGWlPPFKXE2b2m3B06VmxD7vNLXiZSIfscjB--rwoNMcrEEd7hLQaUZ0Wf7EfM5D3a3mnoY2qDsMYd2HdjzvTnDlX3fSx4ecxQltwYtRrbSDYsU-W2xumcu8RxYOeb6-Kb9ciwt3jMfxH_O78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رییس‌جمهوری ایران، در پیامی یادداشت تفاهم امضا شده میان تهران و واشنگتن را «حاصل خرد جمعی اعضای شعام» توصیف کرد و نوشت: «باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند.»
پزشکیان روز یکشنبه ۱۱ مرداد در شبکه اجتماعی ایکس نوشت: «تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند. باور دارم این تفاهم‌نامه مرکز ثقل روابط خارجی ما در آینده خواهد بود. باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند. امنیت کشور، منطقه و هم‌پیمانان ما با این تفاهم‌نامه ارتقا می‌یابد.»
همزمان، کانال ۱۲ اسراییل به نقل از منابع آگاه گزارش داد کشورهای منطقه در حال میانجیگری برای بازگرداندن آمریکا و ایران به یادداشت تفاهمی هستند که ماه گذشته میان دو طرف امضا شد.
بر اساس این گزارش، توافق پیشنهادی شامل باز ماندن تنگه هرمز به مدت ۶۰ روز بدون دریافت عوارض و تمدید آتش‌بس میان تهران و واشینگتن است. کانال ۱۲ گزارش داد یادداشت تفاهم پیشین به دلیل اختلاف بر سر نحوه مدیریت تنگه هرمز از هم پاشید؛ به گونه‌ای که دونالد ترامپ بر باز بودن کامل این آبراه تاکید داشت، در حالی که تهران معتقد بود این توافق به جمهوری اسلامی اجازه می‌دهد مسیر عبور کشتی‌ها را تعیین کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/77710" target="_blank">📅 23:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عراقچی: مذاکرات ایران و عمان درباره تنگه هرمز به مراحل پایانی رسیده است
🔸
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه خبر داد که مذاکرات با عمان درباره تنگه هرمز به «مراحل پایانی» رسیده است.
🔸
به گزارش خبرگزاری رسمی دولت ایران، ایرنا، عراقچی در جلسه هیئت دولت از وضعیت این گفت‌وگوها گزارشی ارائه داد و اعلام کرد که «مذاکرات در مسیر نهایی شدن قرار دارد و مراحل پایانی خود را طی می‌کند».
🔸
هفته گذشته وزارت خارجه ایران گفته بود که مذاکره میان تهران و مسقط همچنان ادامه دارد. این در حالی است که کاظم‌غریب‌آبادی، معاون عباس عراقچی، سه‌شنبه همان هفته اعلام کرد که جمهوری اسلامی پیشنهاد عمان مبنی بر تقسیم برابر مسیرهای عبور و مرور میان دو کشور در تنگه هرمز را رد کرده است.
🔸
پیش از آن، خبرگزاری رویترز پیش‌تر به نقل از یک منبع آگاه گزارش داد که عمان پیشنهادی برای ایجاد یک سازوکار مشترک منطقه‌ای با پرداخت داوطلبانه عوارض یا هزینه‌ عبور و مرور برای مدیریت تنگه هرمز به ایران ارائه کرده است.
🔸
همزمان با انتشار اظهارات روز یکشنبه عراقچی، سخنگوی وزارت خارجه در گفت‌‌وگو با تلویزیونی حکومتی ایران مدعی شد که مذاکره بین ایران و عمان دربارۀ تنگه هرمز «ربطی به باز یا بسته‌شدن تنگه هرمز ندارد».
🔸
اسماعیل بقائی همچنین گفت که مدیریت آینده تنگه هرمز با ایران است و با مشورت عمان انجام می‌شود.
🔸
این مواضع در حالی مطرح شده که دونالد ترامپ، رئیس‌جمهور آمریکا، بامداد یکشنبه اعلام کرد طرح جدید برای حمله به ایران را با درخواست جمهوری اسلامی و کشورهای خاورمیانه و برای تکمیل توافقی که به بازگشایی «فوری، کامل و تمام‌عیار» تنگه هرمز و «پایان تهدید هسته‌ای ایران» منجر شود، متوقف کرده است.
🔸
رسانه‌های ایران به نقل از منابع آگاه حکومتی درخواست از آمریکا برای توقف طرح حمله را رد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/77709" target="_blank">📅 23:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WLHSgH2vnsahKxbxzOfsstUivh4NAvl_F4SeYyhvgoa_FK624eMDwv1FqCVT8cB1vpnZjnPCOm5elBQdhYqGZWhhHtH1ebEaqrA8PkhGX0qMy0JtzhAdWH8ifyQ3PKgZAEWOjpapgv8mNnoGpPo4kxx84QiTrHGhfI8vCZL5QHto7wpU7pCeLLZ8q2Y0i2tOGeO4TPXNHJhdRJZPA1WsHAa5jZTpUJr6IPb0R-GQKIfr3y2D3wEpTCOdXfQPH7sVv2vvB9IJZloCHv8ONCAAndhTiogfCjO9jLNUH5VHKldVWNzzW-M2Ro0Vwazjgoii2hSw22G38uWCcQvJwCk9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BhtA7g-XG6DllKfjuMQIUTDHm_WcgojMoVEXdvSqbSgHfKIcyiSDZHXRCyxhpI93mm7ZbNTbeXGtBEeRyg-S_NMwGCPpZ6BblBF3TFbJ2SWX6Vn7LWPQKGacR-c5ivLal4OKqyYnv9yuVzlwt4xgqF7i3ztjURr2rwMyiGaOfdST8lRohaTwTS37N38zXJK9aiNhB4tj8NPox95OwVbYJ673WBBO2l-wS-iw21EyiMYg_gV1yYeSs5C7cVqZ5jHxu9G0Ipp7TKKF39suzu-xKEpAoSDduK48t_O5QEVdvKwwHmUqDPpNuOybwqeRgTJ1hHQ5Lm6iIsxDIBv-v-5KaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کانال ۱۲ اسرائیل یک‌شنبه ۱۱ مرداد گزارش داد عباس عراقچی، وزیر خارجه جمهوری اسلامی، شب گذشته با پیشنهاد مصالحه‌ای که میانجی‌های قطری و آمریکا درباره سازوکار بازگشایی تنگه هرمز تدوین کرده بودند، موافقت کرده است.
این شبکه به نقل از دو دیپلمات آگاه از جزئیات مذاکرات گزارش داد پاسخ مثبت عراقچی یکی از دلایلی بود که دونالد ترامپ، رییس‌جمهوری آمریکا، با لغو حمله به ایران موافقت کرد.
@
VahidOOnLine
خبرگزاری فارس به نقل از دو «منبع آگاه» گزارش کانال ۱۲ اسرائیل درباره موافقت عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، با طرح بازگشایی تنگۀ هرمز را تکذیب کرد.
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای ایران به این خبرگزاری گفت هیچ توافقی درباره بازگشایی تنگۀ هرمز حاصل نشده و اخبار منتشرشده در این زمینه «کذب» است.
فارس همچنین به نقل از یک منبع نظامی نوشت تا زمانی که «اقدامات خصمانه آمریکا» ادامه داشته باشد، تنگۀ هرمز مسدود خواهد ماند و عبور شناورها تنها از مسیر اعلام‌شده و با مجوز نیروی دریایی سپاه پاسداران امکان‌پذیر است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/77707" target="_blank">📅 17:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77706">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twzPvx0pkRU701sdJK3jVUDtR71i91TzURBMR6D2VthFfjmnKsRFxhHy6zv4w6DHSgu9N9kx2ENB8rbnnHGii6oJcF_e5L_cLM6fMoWnr3dQFRqFqNA1Uo9DBPpJ3eAxv3tVAlcv678ocPcTXDW1BNGwh4lX97HkToFUhpwhN393OtKs7mutaaGkTowoq3pxZ7HfM5YlJkdYZAQAdKS4lIjJ3x8IKQPwfbgdYMbKCxyP9L0lNrVK5dh21eFtnV2u3ifcY7rVbItQuWanjoPg8g6bOp0vyUr6mHkgegIs0FochqcnxfE-dgy12lGeuw41cq37hdsc4PuFBUq11c04RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در مصاحبه‌ای با فاکس نیوز که لارا ترامپ، عروس رئیس‌جمهور آمریکا، انجام داد، گفت حتی اگر در تهران به‌طور رسمی «تغییر رژیم» رخ ندهد، حکومت ایران «باید» روش خود را تغییر دهد.
وقتی از روبیو پرسیده شد آیا واشینگتن می‌تواند بدون تغییر رژیم در تهران، ایران را «هسته‌ای‌زدایی» کند، او گفت:
«فکر می‌کنم آنچه باید رخ دهد این است که حکومت باید تغییر کند. ممکن است تغییر رژیم نداشته باشید، اما حکومت باید تغییر کند.»
او افزود: «حکومت ایران به‌طور سنتی رویکردی توسعه‌طلبانه در خارج از مرزهایش داشته است. در اصل، دیدگاه آنها این است که نمی‌خواهند فقط بر ایران حکومت کنند؛ می‌خواهند بر منطقه حکومت کنند. آنها می‌خواهند انقلاب را صادر کنند.»
روبیو ادامه داد: «این رویکرد باید تغییر کند و تنها راه تغییر دادن آن این است که هزینه‌اش را آن‌قدر برایشان بالا ببرید که دیگر قادر به پرداخت آن نباشند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 475K · <a href="https://t.me/VahidOnline/77706" target="_blank">📅 17:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3938f205b4.mp4?token=A27kNUEcu02kau8OCLRyhztu1p9jsHBxzeAN-5iA9PWY2uuMsFbSA6igvG6QlooEZKjk4IE53XISPYYp9vB9Yqd57TEiebYxenKlxTZp-ciKMP_4x5aJIWtXFALPOWv3wcubObUqYNmp4jJu8VHy3IUHLPPXWLMabt6DdkaPDgyskMD1OQzK4vBgURiKehDGc63X08i2Si1deymuylYUIgj82g5G_mf2lymcq-HKxRlZI9RtbV_RyFdlfkd-KDAv0SYGR9HvnncMsc8Gt8uNlvKIvVSLL7SgVlNn9bwWT2iAE5B6SxppX6SqmKUDF_pAKL-HLSHtwxzYzLVmrBAv3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3938f205b4.mp4?token=A27kNUEcu02kau8OCLRyhztu1p9jsHBxzeAN-5iA9PWY2uuMsFbSA6igvG6QlooEZKjk4IE53XISPYYp9vB9Yqd57TEiebYxenKlxTZp-ciKMP_4x5aJIWtXFALPOWv3wcubObUqYNmp4jJu8VHy3IUHLPPXWLMabt6DdkaPDgyskMD1OQzK4vBgURiKehDGc63X08i2Si1deymuylYUIgj82g5G_mf2lymcq-HKxRlZI9RtbV_RyFdlfkd-KDAv0SYGR9HvnncMsc8Gt8uNlvKIvVSLL7SgVlNn9bwWT2iAE5B6SxppX6SqmKUDF_pAKL-HLSHtwxzYzLVmrBAv3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشر شده در رسانه‌های اجتماعی نشان می‌دهد بامداد روز یک‌شنبه ۱۱مرداد۱۴۰۵ پیکر آروین خیرخواهان معترضی که در جریان اعتراضات دی‌ماه۱۴۰۴ بازداشت و ۱۰مرداد در شاهرود اعدام شد به خاک سپرده شده است.
خاکسپاری در سکوت و تنها با حضور اعضای نزدیک خانواده او انجام شده است.
بازداشت، محاکمه، صدور حکم و اجرای آن برای این شهروند معترض ۲۰ساله در سکوت خبری رخ داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/77704" target="_blank">📅 17:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77702">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JTm7IvHJkyzVq_hO4bQs2NtFUljAI2hEcgNbtxqLLMQ0zR9R85lUFQHFVxMDhW4WYY_APF4MJwH_mf8kb050ydQ_tiO-jSso5gjnmSKjYPpwEK849HHjV0vtIIz6AQL1ueBAyAIbaZy7R9y15NUJ-pfeL9mLtJh90JYtshkYA6iSMytdyhPb3VHXYgLNavPEqt5G3ZKsMfc9-YxBCNT2CwVYELXkrCr10gIeqpy8SxeDv6gd5ID00D4IPcAUQwkoJxQPOt6dV7KwPxvYyPPeR36UmNRLwK0SspQ4qSHxA5WY_JzbKZQXRJxaSBEZv8iA1AEnQPPV5UA1uRn3uGP1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به درخواست ایران و کشورهای منطقه، حمله را برای فراهم شدن زمینه توافق، متوقف کردم
ترجمه ماشین:
ایالات متحده کاملاً مسلح و آماده است تا با جمهوری اسلامی ایران مقابله کند؛ با سطحی از رعب نظامی، توان و قدرت که از زمان جنگ جهانی دوم تاکنون دیده نشده است.
با وجود این، ایران و دیگر کشورهای خاورمیانه همین حالا از ما خواسته‌اند که از هرگونه حمله دست نگه داریم، زیرا بر سر چارچوب‌های یک توافق تفاهم حاصل شده است.
این توافق شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران خواهد بود.
بر اساس این درخواست، برای منافع آینده جهان و همچنین بقای ایرانی موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانیم به‌سرعت به یک توافق دست پیدا کنیم.
کشور اسرائیل نیز در این تعهد با من همراه است.
همه دست‌به‌کار شوید و کار را تمام کنید. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. is locked and loaded and ready to go against the Islamic Republic of Iran, at levels of Military Terror, Strength, and Power not seen since World War II. Despite this, we have just been asked by Iran, and other Middle Eastern Countries, to hold off any attack in that the perimeters of a deal has been agreed to. This would include the Immediate, Complete, and Total OPENING OF THE HORMUZ STRAIT, and an end to Iran’s  nuclear threat. Based on this request, I have agreed, for the future benefit of the WORLD and, likewise, the survival of a successful and prosperous Iran, to cancel the attack, subject to being able to rapidly make a DEAL. The Country of Israel joins me in this commitment. Get to work, everybody, and get it DONE. Thank you for your attention to this matter! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 570K · <a href="https://t.me/VahidOnline/77702" target="_blank">📅 05:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DNZ-SBMmmL6Y4OLcvYNDFjoKBf2Q6OEvFKl-YDYCvTxzbq6U0bl9LWti9ipezeJC1hdQBbrkGO8dqhB765O3kzQhCeFm8K5n0pFphTGpDRD-dkCXvDfSIMjHAOj44XIyBVvhPNGUXifCjJMDayeY8xkGH3b9zuwB3k6tGMINtWB8dJMt_Kfy9VOkJJL4pTrKZIucErzm1pGxQ-7t1bgIAaIMdKlawaJpuAarWm14EP4rlR7xS1I3-qtsyxgTw8Tm3rXeTpanOxvw0rBgvY1WsPQfVtKkIkYapcEMXhcxENg3aKJApDIk2xT4yfS2T9t5c9CGXCkjgW3lejEDwH38Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد بن سلمان درباره برنامه‌های ترامپ برای حملات گسترده به ایران ابراز نگرانی کرد
اختصاصی
اکسیوس، ترجمه ماشین:
محمد بن سلمان، ولیعهد عربستان سعودی، روز شنبه با دونالد ترامپ، رئیس‌جمهور آمریکا، گفت‌وگو کرد و درباره برنامه‌های او برای حملات گسترده جدید علیه ایران ابراز نگرانی کرد.
این خبر را دو مقام آمریکایی و یک منبع دیگر مطلع از این تماس اعلام کردند.
چرا اهمیت دارد:
ترامپ در واکنش به حمله موشکی ایران به یک پایگاه آمریکا در اردن و ادامه اختلال ایران در کشتیرانی از طریق تنگه هرمز، به‌طور جدی حمله به اهداف انرژی ایران در روزهای آینده را بررسی می‌کند. او هنوز دستور نهایی را صادر نکرده است.
تصویر کلی:
چنین حمله‌ای ممکن است به تشدید بی‌سابقه جنگ پنج‌ماهه منجر شود؛ جنگی که با باز کردن راه مذاکرات از سوی ترامپ بارها متوقف شده، اما پس از شکست این تلاش‌های دیپلماتیک دوباره از سر گرفته شده است.
جزئیات:
ایران تهدید کرده است که با انجام حملاتی علیه تأسیسات انرژی و زیرساختی در اسرائیل و کشورهای خلیج فارس تلافی خواهد کرد.
▪️
یک مقام آمریکایی به آکسیوس گفت: «سعودی‌ها ابراز نگرانی کردند و خواستار شفاف‌سازی درباره برنامه عملیاتی شدند.»
▪️
یک منبع دیگر مطلع از این تماس گفت محمد بن سلمان از ترامپ خواست تنش‌ها را کاهش دهد و از انجام این حملات خودداری کند.
▪️
کاخ سفید و سفارت عربستان سعودی در واشنگتن از اظهارنظر خودداری کردند.
مرور سریع:
ترامپ روز چهارشنبه با شاهزاده خالد بن سلمان، وزیر دفاع عربستان سعودی که با نام اختصاری «کی‌بی‌اس» شناخته می‌شود، دیدار کرد.
▪️
یک منبع مطلع گفت این دیدار پس از آن به برنامه سفر وزیر سعودی افزوده شد که او با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، دیدار کرد و به او گفت عربستان سعودی خواهان کاهش تنش با ایران است.
▪️
این پیام با وجود حمله مشترک این هفته آمریکا و عربستان سعودی به شبه‌نظامیان طرفدار ایران در عراق منتقل شد.
▪️
این منبع گفت هدف از این دیدارها انتقال دیدگاه‌های محمد بن سلمان درباره جنگ ایران و اوضاع گسترده‌تر منطقه بود.
در پس ماجرا:
عربستان سعودی یکی از مهم‌ترین متحدان واشنگتن در منطقه است. ریاض، با وجود دوره‌هایی از تنش طی پنج ماه گذشته، از زمان آغاز جنگ در چند مقطع حساس بر سیاست ترامپ در قبال ایران تأثیر گذاشته است.
عامل خبرساز:
دیگر قدرت‌های منطقه‌ای، از جمله قطر، امارات متحده عربی، ترکیه و پاکستان نیز آمریکا و ایران را برای کاهش تنش تحت فشار قرار داده‌اند.
▪️
عباس عراقچی، وزیر امور خارجه ایران، روز شنبه با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، که نقش میانجی مهمی میان واشنگتن و تهران داشته است، گفت‌وگو کرد.
▪️
عراقچی همچنین درباره احتمال حملات آمریکا با وزیران امور خارجه ترکیه و عربستان سعودی گفت‌وگو کرد.
▪️
عراقچی، بنا بر بیانیه‌ای در کانال تلگرامی خود، به همتای سعودی‌اش گفت: «هرگونه اقدام خصمانه از سوی آمریکا یا اسرائیل — یا مشارکت یا همکاری کشورهای منطقه در چنین اقداماتی — با پاسخ قاطع و متناسب نیروهای مسلح قدرتمند ایران روبه‌رو خواهد شد.»
آنچه باید زیر نظر داشت:
میانجی‌های قطری روز شنبه در تلاش برای دستیابی به توافقی برای بازگشایی تنگه هرمز، جداگانه با عراقچی، استیو ویتکاف فرستاده کاخ سفید و مقام‌های عمانی گفت‌وگو کردند.
▪️
یک منبع مطلع از مذاکرات گفت این گفت‌وگوها پیشرفت داشته است، اما هنوز مشخص نیست که آیا این پیشرفت برای فروکش کردن بحران کافی خواهد بود یا نه.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 506K · <a href="https://t.me/VahidOnline/77701" target="_blank">📅 03:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77700">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gGczJ1Aq0pqXazN1K1FoAv_ggPRiRniigdv1AiTnmOC7SNvy3YxWOIRju9HzxQ44V63qDUZc0Si3sn6XO0Y56vmhqgljWx_ZYRFBW7lTokROEUG9USYE5pMkfsqQphhdQmnkr2XIJCwf0nxCIdaRmJAPxU8VusJP6z_qpx25t47mSXgkQ_wamkB-BRNHB4-CELhdBK5qr_UK-ueXIHI82w6my_vvqYQnYhDtOX48icTXJVKFv2sFau3bCPyIidviORbGe-DLjMgHPC5krth5vOGWkNL2JNK8psU1kS9XaZMoUMApdl-_NkZr3vwGx7KmNGD17QtbsFhg1k-ApFmlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با افزایش تنش‌ها میان واشنگتن و تهران، «وای‌نت» روز شنبه گزارش داد، ورود و استقرار بیش از ۳۰ هواپیمای سوخت‌رسان نظامی آمریکا در فرودگاه بن‌گوریون تل‌آویو و افزوده شدن ۱۰ هواپیمای دیگر در روزهای آینده، موجب بروز اختلالات شدید، ترافیک سنگین هوایی و تاخیرهای روزافزون در پروازهای این فرودگاه شده است.
بر اساس گزارش سازمان فرودگاه‌های اسرائیل، میانگین تاخیر پروازها در ترمینال‌های مختلف به بیش از یک ساعت رسیده و دریافت بار مسافران نیز تا دو ساعت معطل شده است. وضعیتی که هم‌زمان با اوج سفرهای تابستانی و نقایص فنی اخیر در سیستم‌های کنترل ترافیک هوایی اروپا، مسئولان را نسبت به تشدید بحران و جدی‌تر شدن اختلالات در پروازهای بین‌المللی نگران کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 507K · <a href="https://t.me/VahidOnline/77700" target="_blank">📅 03:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BChRrGxDF7MNaxfaWaGlxss1_bMezMPMoXHTb50g-PJcAZeQnO3JTfD-h57LJ_9N9-CYJwjcHNbfheIutWiZMNAfTB7kzr3s4cErnsMdFJBGK3UQTLkvYgRxCxmmOAwqXAnWE1dpjBdD10NYPpI-G6DEvjBqUwfbCydVcM7Y2Q5o7_3VPlzvhqUCjwd--aI3pFEqgGC7hENWrwMJN6i0aaKhUqqMGuVYGRMqrOM1weySg_iWbabuysHqPyjXQAseVyYB3kl8W4BhtBGMbxAOk5S3zcM16kUOYj69Zwp4zgkx2gD7ZJJBojaggRedrW8viNa0ZP3mPo-ZMCrnfSUuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر پست ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است
هم‌زمان با افزایش تنش‌ها در منطقه و انتشار گزارش‌هایی درباره احتمال از سرگیری حملات آمریکا علیه جمهوری اسلامی، دونالد ترامپ، رییس‌جمهوری آمریکا، تصویری را در تروث سوشال
منتشر کرد
که به کاهش ارزش ریال و افزایش تورم در ایران اشاره دارد.
در این تصویر با عنوان «ترامپ در حال نابود کردن ارزش پول ایران است» نوشته است که ایران با تورم شدید روبه‌رو است و ارزش هر دلار از حدود ۹۰ هزار تومان به ۱۹۰ هزار تومان افزایش یافته است.
ترامپ توضیح یا اظهارنظر دیگری درباره این تصویر منتشر نکرد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه شنبه دهم مرداد ماه، تصاویر ساخته با هوش مصنوعی را در شبکه تروث سوشال منتشر کرد که او را در لباس رزم جنگ استقلال آمریکا نشان می‌دهد. در مطلب دیگری، تصویری از ناوگان دریایی غرق شده جمهوری اسلامی در زمان ریاست جمهوری او دیده می‌شود.
در یکی از این تصاویر ساختگی، ترامپ با پوشیدن لباس فرماندهان جنگ استقلال آمریکا و در میان دود و آتش نبرد به تصویر کشیده شده است. در تصویری دیگر تحت عنوان «۱۵۹ کشتی ایرانی»، شناورهای نظامی ایران در دوره رییسان جمهوری سابق آمریکا روی آب نشان داده شده‌اند، در حالی که در به دوره ترامپ، تمامی این شناورها در قعر دریا غرق  شده‌اند.
این تصاویر در حالی منتشر می‌شوند که رسانه‌های مختلف از جمله
شبکه ۱۲ تلویزیون اسرائیل
از احتمال حمله گسترده ارتش آمریکا به ایران خبر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 579K · <a href="https://t.me/VahidOnline/77699" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8n1o9HKB2C-OuapQtAKn6nKaZJlF_6f4-Z6xSa0mNUJf8WWBKWD6shrh6VUv1NJVlrduIzuB8YXmaw7QNNdlpd5GI-y9F5PRcDsy_tBo8jxBvhmBUYwyvGg978ARNyB-UigE1YtBco_4oINfVxmr24KQFy4VCPZ4fluaWU6CR6ZokNcpdn8TDeBKZo0DFFfM9UD_GiwsMNJWP2NrGegoEikH6wvopqrz17djPyLvOPMYh1N-EHKm4VWmhPJzbQyBfp6E7bQ-Vr6bkYg7DgY-N2hRmsGeJqmdfnmwGPYfac5bmxDn9IFtDgnjT4ksChYNn5-5Aqi2xj08guzUFwBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سحرگاه روز شنبه ۱۰ مرداد ۱۴۰۵، حکم اعدام آروین خیرخواهان، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان شاهرود به اجرا درآمد. این جوان معترض، پیش‌تر از سوی شعبه یک دادگاه انقلاب شاهرود با اتهام «محاربه» به اعدام محکوم شده بود.
به گزارش خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، حکم اعدام آروین خیرخواهان حوالی ساعت چهار بامداد امروز اجرا شد.
یک منبع نزدیک به خانواده این زندانی با تایید این خبر به هرانا گفت که مسوولان زندان تاکنون پیکر او را به بستگانش تحویل نداده‌اند. به گفته این منبع، به خانواده اعلام شده است که ساعت سه بامداد فردا برای تحویل پیکر مراجعه کنند و مراسم خاکسپاری نیز باید ساعت پنج بامداد برگزار شود.
آروین خیرخواهان در جریان اعتراضات دی‌ماه ۱۴۰۴ بازداشت و سپس از سوی شعبه یک دادگاه انقلاب شاهرود با اتهام «محاربه» به اعدام محکوم شد. این حکم پس از اعتراض، در دادگاه تجدیدنظر و دیوان عالی کشور نیز بدون تغییر تایید شد.
تاکنون جزییات دقیقی درباره زمان و نحوه بازداشت، مصادیق اتهامی، روند بازجویی، دسترسی این زندانی به وکیل انتخابی و مستندات مورد استناد دادگاه برای صدور حکم اعدام منتشر نشده است.
هرانا نوشته است، آروین خیرخواهان هنگام اجرای حکم اعدام ۱۹ سال و شش ماه سن داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 591K · <a href="https://t.me/VahidOnline/77698" target="_blank">📅 18:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f9d9bdf8e8.mp4?token=RIIa1F4vE4jx3fGXyuGbV1_uZ_a8ygNE9d-W5xWUl-u8fxgVvQp-R-KPJ8zp6VNLfJa_4o5VaYLhydSoF_vTDf_UAWCXX53R8MuMB3bYMFs3kSjTvd9SPO9mc_CN4I7gaZg1jfDTx3-ZuEOfdADlUik4x8gkNY4S7ARsIiT6VUV4GZUfTnz0gTYYxpeLSHh_4k2uuF1c3Ql7frCxHokhNIrBbBgfP-I59eFavNGDgS41CIDrNmIsjAbvTPstvSSt4NjWtPSDKFI08Fq3f0zVEtpkTKzFsK3dYuVvuRIj_BXapZ4CIHdqzJYiD26PsRTYmKAHbPCc1LvnB3TVVJjibA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f9d9bdf8e8.mp4?token=RIIa1F4vE4jx3fGXyuGbV1_uZ_a8ygNE9d-W5xWUl-u8fxgVvQp-R-KPJ8zp6VNLfJa_4o5VaYLhydSoF_vTDf_UAWCXX53R8MuMB3bYMFs3kSjTvd9SPO9mc_CN4I7gaZg1jfDTx3-ZuEOfdADlUik4x8gkNY4S7ARsIiT6VUV4GZUfTnz0gTYYxpeLSHh_4k2uuF1c3Ql7frCxHokhNIrBbBgfP-I59eFavNGDgS41CIDrNmIsjAbvTPstvSSt4NjWtPSDKFI08Fq3f0zVEtpkTKzFsK3dYuVvuRIj_BXapZ4CIHdqzJYiD26PsRTYmKAHbPCc1LvnB3TVVJjibA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر علی منوچهرآبادی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، با انتشار ویدئویی در اینستاگرام، تولد خود را کنار مزار فرزندش جشن گرفت و یاد او را گرامی داشت.
علی منوچهرآبادی، شهروند ۲۵ ساله کُرد اهل کرمانشاه، در جریان اعتراضات دی‌ماه ۱۴۰۴ در محدوده فلکه سوم تهرانپارس با شلیک گلوله جان باخت.
او پسرخاله میثم کُرانیان، از دیگر جان‌باختگان اعتراضات مردمی در کرمانشاه، بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 531K · <a href="https://t.me/VahidOnline/77696" target="_blank">📅 17:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W1CIavJsp79x3eL8VOKPof6SS4nVJP1-9-7NIwOwDZMY8TFs6ofDxANgN0sAO93I91mSYLeMMjcrYUMAM6KwaSqCEWDaiaZ9v3QeDMZaLLGPQEmFFfTTGSlUGpQ8nxG53vpaHRhzh69mcQkwFtaYP-LPy4dQedi40oOiYaq-H3J62KwBgJoIKW4w2I43l4aU_PMND_JKYXM4WFLveO7_ZLXZjCm83TzSY10tUXBTE3uTh1eSiXLk2b2EGAH4VagYTycG5rqgsyHEyH7eHtPCwzD_beHDjHQqcOtyL7uDkI14UlDM_0uLLlQ9gSusKd-I8eA9YB6wtR1YSgxvRKCVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت ارتش کویت، ترجمه ماشین:
سامانه‌های پدافند هوایی کویت در حال مقابله با حملات پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران، هستند.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان درخواست می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 583K · <a href="https://t.me/VahidOnline/77695" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
