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
<img src="https://cdn4.telesco.pe/file/uPx7a63hGcV4DJRwzKBBZIN5UOgz8_uj3jW3mRsuv7xvLTaPN9YJvuosNCoHP8dD2Betgdv-yexJoolpU07eeNrecnhXpzyYot708JNFrq2GiKrhJZxJBDTsL87quwuA1t12dsX-s1LSAr4_tYQcBzJLISiEUHLZomwssJ9nocyKZZEkiNWawH81aeu3bSvZBKRTDGRGnHtxPV4EvluY8WSmUTLkFqntX1VFh3H02Jwrm_c8uRelXQXCsXvJVGa78v7GPNXcer2QluMIJHKbzwfufmy1sINYbEPswKFElsQxBgeKlzqMJW8m0vHEQpAqtaLeZThU1z834bKysHXupw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 12:02:23</div>
<hr>

<div class="tg-post" id="msg-458323">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7ZAcOEoWW56A-eJ03Vm2O8CFEHpfZM2h_SgMTCTLZW2jXSixQj2XdfW5q3HK0c22otisnKWSUk0rcryLulwmIESrfFlrW3FCfFGLsBlrTwyfaixy1nsAFabiJlglBOyZbG6YnFsqJbuOLJ_hwk41HKIz6Ny7xfwo0H7LwG47GsS2kVu3POVz5Bh_dy872zpd06CIZ4VLTh0Fert9MtKuipihYfQLMSFGlwET5YsGv9hTr2RJl_YRx5LqJ8s1uzAaSknyg72mcoC13w7P6T57-ciOTg48DhrfaFXFXglzoWtrQ_qJUklXZeQqjiDvYp-hibiwf3_xsTstZh37tInGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل شلوغی پمپ‌بنزین‌های تهران در روزهای اخیر چیست؟
🔹
صف‌های طولانی در برخی جایگاه‌های سوخت تهران در روزهای اخیر، همزمان با افزایش مصرف بنزین شکل گرفته است؛ به‌طوری‌که مصرف روز گذشته به رکورد ۲۶.۲ میلیون لیتر رسید.
🔹
افزایش سفرها، استفادهٔ بیشتر از کارت جایگاه‌ها، گرانی تاکسی‌های اینترنتی و برخی ابهامات در اطلاع‌رسانی دربارهٔ سوخت از عوامل افزایش مراجعه به جایگاه‌ها بوده است.
🔹
از سوی دیگر، محدودیت سوخت‌گیری با کارت جایگاه و اتمام سریع موجودی در برخی جایگاه‌های پرتردد نیز به طولانی‌شدن صف‌ها دامن زده است.
🔹
این شلوغی‌ها درحالی‌ست که شرکت ملی پالایش و پخش اعلام کرده تأمین سوخت کشور پایدار است و مشکلی در تأمین بنزین وجود ندارد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 584 · <a href="https://t.me/farsna/458323" target="_blank">📅 12:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458322">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekJb9xsFYB7TA8paWUj4ksMVq2xE2_qNhoEdGJrCVnoUWfelBr0iWW2tvx6akSDsV_Os8KxJZsPvoMGzfUK37CodzS0kyxwOoxRqbGtxOvdXHjUkDeWMSQ12oY5gzdgPLDDlfEwQg0DoCs3IanN2KBY8AdR9gHz2P_ncfEbXRoBB0FwuaqMq3FzWO5f7l9NYrLQV7zbsSqx12c9-MXST_mgqmP49Yu1esTygERAgobMmIpfodaFl0yhXJ6-L78aAKPql7hoDI_rdrKT9tkWLMapAZYTEvd8aXYUJMMzy01NsZkfrEb6PZGceRddXIK0pQS__JqluH0o1yp-FW4t3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۴ ریشتر در عمق ۷ کیلومتری زمین، نوار مرزی کردستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/farsna/458322" target="_blank">📅 11:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458321">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در پاکدشت
🔹
سپاه استان تهران: درپی انهدام مهمات عمل‌نکردهٔ دشمن در پاکدشت، احتمال شنیدن صدای انفجار ناشی‌از این عملیات تا ساعت ۱۶ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/458321" target="_blank">📅 11:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458320">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9lr2jihaCPZ_P-ZLg7qdiQPMYghyBHoV9WmTcoaqWgQ9WD7lcMN-QZmD6fyzEhUTR4fN4JXz-PnbDKN4tC97mMzJY8uUBKhBO26F0TI0Gw48Zv3XA35G8ST4C9qXRbJ5Ewiaxp11wEe5ZWQkpvs787yj5YGA79a6uAldeLZYwYDMR767fq_0mNhgG0GvFSRNiC7fjzEbIlyzeXrqRVIDasoL7icM34ojDQZzAN_0KLgyzwoKeq4qy5NhikzVUEhhVxiQ0q5_a45BCyA9T0ls1BbAoC3fKEgkx7bWOXfKj7SSXs2tFHhIHNd6aOheOzAvWQiAEFrmP_BpVuZcfIfBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج آزمون کارشناسی‌ارشد اعلام شد
🔹
سازمان سنجش: نتایج اولیهٔ آزمون کارشناسی‌ارشد ۱۴۰۵ اعلام شده و داوطلبان مجاز از ۵ تا ۱۰ شهریور برای انتخاب رشته فرصت دارند.
@Farsna</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/458320" target="_blank">📅 11:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458319">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAsWtUvNpkgR7jr17WBudeafFZ_IWDaq0GOTWh2d9os5ZVjWmonunhJYlLQVnvqxVy-YDK3eoi5wKBCRc6fJm_3av7XCFxNSFlzi7zmIlM0dZWGYDMGR7LRzOcTUdbpn4ZuoiQOkckcBso9gbSRIP2gdROKNPEQ1cJa54_vOiRcT2V8BHX2c1yGVCGRLzENCjq984acs4rhm7epKAtJeqTo4QlbKR4YGbeFhweYaSgMn7B_60LCsYWOmIDxE5NZn0JbczbxA6WwUaANWa_9kv97r7mj-rquCIxM9FWS-zaGnPTZEPHnXTRUcPbJ_LChanJhoCvGheNuvLLCNaBGnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم: آموزش دانشگاه‌ها در سال تحصیلی آینده حضوری است
🔹
نتایج آزمون سراسری در نیمهٔ دوم آبان‌ اعلام خواهد شد و به‌همین‌دلیل دانشجویان ورودی جدید با تأخیر وارد دانشگاه‌ها می‌شوند.
🔹
کلاس‌های دانشگاه‌ها در سال تحصیلی آینده حتماً به‌صورت حضوری برگزار خواهد…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/458319" target="_blank">📅 11:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458318">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoLI8IDkPxb-yns7D3EXkDxQsGxzMBOHiDNymbSui-3vsdVMLs1juj50tDcCCKOfrOMEf8J_BAemzfnITmEF0HSzdX_8x2oKPt1dJ9ngyiEQ0oiNjKF1_RAG3Z6c-MsliYoilep8-INjiFqxKvxklTVKTzgxez4YUs5LO03sJEfFcNYIM2-UFQ1NH4LJz3xXII_lLG7dN_byaxhRzfTTCuy-XZtRYqoBZyD_yak1QvnradLxaEkURB9twauK6iaPI7nKaatg5ZY4gAnpH9djgFbiY37hYGcb1h91DPP7mANDE_hC4xpbAcjPKtWAjgrVlCE7GJ8MGWqE60rP4VPo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واردات لندکروز و لکسوس برای ایرانیان مقیم خارج مجاز شد
🔹
طبق اعلام گمرک، واردات تویوتا لندکروز هیبرید و لکسوس LX600 و LX700 صرفاً از مسیر ایرانیان مقیم خارج از کشور امکان‌پذیر است.
🔹
براساس این بخشنامه، ایرانیان واجد شرایط خارج از کشور می‌توانند یک خودروی سواری شخصی وارد کنند و این خودروها باید از محل ارز در اختیار متقاضی و به‌صورت بدون انتقال ارز وارد شوند.
🔹
لندکروز هیبرید و لکسوس‌های LX600 و LX700 مشمول مقررات خاص هستند و از سایر رویه‌های واردات خودرو امکان ورود به کشور را ندارند.
🔹
خودروهای وارداتی همچنین باید استانداردهای بین‌المللی را داشته باشند و در گمرک مورد بازرسی قرار گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/458318" target="_blank">📅 11:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458316">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml5dfsJ5kU5BkiUOECI_jQPniagV5HOCljPq0Wgz5UHU-33D434_SeyJPfw05MwbT7dLOG2VS873KeYwwii3CVGLSfTnrpi29Ez-dOhQTosebelsTrf70fxyz9rQwamn5IIX8z41xnNRniO_pTuSn57xyNJ3-kJHEn5yTnOXtpDWv1f0IgwATIUcL8l-ZnPzQA23YwzC4eTP0QLg2RbavOqXyOFHKWzFkpp78TJTNRjbk8t5TK4JApixzDTMSPSHjr73pPokFMBTla23B2_SvyXB5rIIj7XiGTVhWDZfyIlH87HSbdYYglgWkmSxYPw16r9_HWGIDf7iNoweihl0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر الهامی: تولید و جایگزینی سامانه‌های پدافندی درحال انجام است
🔹
فرمانده نیروی پدافند هوایی ارتش: تجربیات ارزشمندی در جنگ تحمیلی سوم داریم که در تاکتیک، تولید سامانه‌ها، چیدمان و آمایش سامانه‌ها برای ما مفید بود و تغییراتی ایجاد کردیم.
🔹
هم‌اکنون در شرایطی هستیم که با تکیه بر ظرفیت‌های ۱۰۰ درصد ایرانی پیش می‌رویم و سامانه‌های خود را اضافه می‌کنیم و سامانه‌هایی که در جنگ تحمیلی سوم امتحان خوبی پس داد را تکثیر می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/458316" target="_blank">📅 10:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458315">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6botjMJzeT5gX83y3opkAahSEC9Ol9PlWa4V4TRcOo0FKSZwJCoY1njAbrOWLsq0TyYOOZmJbZPScKSsMbkBLl6sl3zyVUbEgVv1ghTmSj5pmRR1Y7-PShfdlORMIEg9kJjKkqd5YW3zjOi7PZhKTvqZHOWoCC14X3djKQW-5J5gx769S2VVJa1JAsQgH9CnTOXvtvvBHYT0ua4XlqPozykn_-S4Y9XmUYN0Sx6G6bv1j34m6AwGybeY3_jnAwAihfw9PMm3WfWW-qWSVwx3zkeo8pcQ82p4xkX5TUaWaMfCJ29OGt0MM4LUL6AqpAQ17__2mfFfhSgyFniP6fnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴۸۵ کیلوگرم مواد مخدر در کردستان
🔹
فرمانده انتظامی کردستان: در طرحی ۴ روزه ۴۸۵ کیلوگرم انواع مواد مخدر کشف، ۶۶ خرده‌فروش و توزیع‌کننده دستگیر و ۳۱ معتاد متجاهر نیز جمع‌آوری شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/458315" target="_blank">📅 10:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458314">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuDZsyjHsY5Qwha4VZo3oL7K0ZD-k9m7UFqKlkGy70Oafr7G3S4Ew3oAjg-DtA_MZxhedLA7iCAti9EJv5-FRSYOhuq1nSlc8O4L2mgYQDzQtCVOgnlzhQU4bzO7y2had8TW3ZDVq89WzshVt7xOYBqV5aL56jVEIi517GmGWu-ZHo4DL1UDDnSBHoFqxXxoHYz0xxcGejBHMOaXiDpvEHhJXRkYQhBUeFodjYBjecV0W2XHcM63cUDSyTIYwFLJFQfmVE5JOwbQH0GM2xaLCY04PKyBE5q5MFzhQQB5ZwLMmDPoEBh5AhIXobLmr_yrPDlo3vLyOd4EIoOPSBkdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌باختن ۱۳ کودک درپی آتش‌سوزی در یک بیمارستان پاکستان
🔹
درپی وقوع آتش‌سوزی در بخش زنان و زایمان بیمارستان مؤسسه علوم پزشکی پاکستان، دست‌کم ۱۳ کودک که بیشتر آنها نوزاد بودند، جان خود را از دست دادند.
🔹
مسئولان بیمارستان موفق شدند یک کودک را از محل حادثه نجات دهند، اما شماری دیگر از نوزادان در وضعیت وخیم قرار دارند و احتمال افزایش شمار قربانیان وجود دارد.
🔹
منابع امدادی اعلام کردند که آتش‌سوزی احتمالا پس از انفجار کمپرسور دستگاه تهویه در بخش نوزادان آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/458314" target="_blank">📅 10:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458313">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En8Gu8xGqwFWpkhrwnvRmPuJPP5GGB1puzo8GB8KsIi7PfyviloRTx9bKaRb4-HV0s41njVANa_9oBsrrORCj3ZQX2WYSLdgealVT_hw3NCGDecAJ5pFTYL93ipQHD3SMC7mmiW-_pCYOQRJpgtdu7B88EagSZW81P1e_lkDG5Kci-3GlOReF3CpaBFr6E2nOk-gghJDoepU0P-VFZg4eQx_bBLSpbe9mu-9q7jLJqGD0uomRgj9Gc0i82FcBEOZvszcYVHrlHMWh_O9sBg0PX6DbysADJ5GvCs5znuW9Y2fgC6zzWkk1-bmNiOkEOVUNm03v8Z5dM9op_XKUFofKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۷، ۸ و ۹ فردا شارژ می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/458313" target="_blank">📅 10:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3Kcthju7NSF0jCbCb-1w88jN_hKxk5wtWBls_t8n-63tx4e4-Y5qRwgRzOy7sYtTrHwcJk5FvpMmBwpk0UOBjLg-HDeheIvXOF0ZXrfk-3H5-YkEwfszvEGvg3NtEpYrP9oh5-V2bNKeLR-E8FW-knQryRCT7QopIILc_uz7otf5DFvCHYm4uGacqkBT5b-5UL6gin1bhM34uj5nv4eFMQU3QfV-Y5BmGdmZtnBqRH83h7vmZQXoiwgda8-2RGTDOkAOXa5xYoKPlF1ciJUZqUlAAResQ_9eoonkbina6-q70LOJeZWIgEk5WRSlegFxGwGSNfRiOLd6hJaJ_ra7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvPFCpNomAReAwk9YIcO22AX7SYsjWbQgfQiDRYHi76v3Dtp2wI-bXxvORWzq8qtYUqKANW1_RXZzboYwokKByYhtLs-FFfIlSSRasvVPgUjSZcz6ryBk65XX8slVV0snTrzI_ExLuSyfkSuUO36vX37G0f8IxXD5fQkIEGSNgzmkZSrOhfTWQwUwFgR-J11lrFapa5bF3CFR3LtwUqmDyugulLaPyW7Big9_VLdM20bgjHkna4VNOIDgwUYweCZjzg3u0Yd5z669WBdgRE_X3FRLFxupKrjimwjJ5GUshN6gTGA2E2PeDKEys5ml6x4e6fMhc6f3QMDiGSGmyMDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nihZsLkSb6vXQHdKAO3sNSBlLP5ehTPQew2Vf1aQ4bL430YF6lDh4ubY5qseKdxeoCWSIoYA6HkeIMIMvL-4bOg6-jPzsbJNK3cei7f2tY7w5cq_Tu7nHOHkgFzh-pD4xyoCycHFaSVPxPat-MR0fHuXvy2nDlatMetpT-Yp1VaV1RUEuBVGRcAlCVyLMgXkOL-uTRmRRFWoKdY4sQLP-OcEEl9lj8GQ17-XgN_ff2rEe6z6KDWJA8TKTCXCqHUfkopwvgiytUaMqCy4wSJTYsd6js21XRC-6LKR84-7kP9JJOzrxyoHzqnnLHuUN39Vk1bRak7ZpUhk21IHmIXhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/de1HkGUgGbPPaSfzIjJa4piou_rpd1tFLyGAZmbQrftVRfWwQ67gVDZ708SP-l46NFObAUxBd-O6NxXCRmKRwFhkHp7ljXqx77W0c6kxSb2nnbTgBrQ4bFwVC-rdDwsBzjLmGmMIxQzoIAnYqPVz1Q741wRZ6J4FLuYvuAJCA9jyzalKZl5ysd8Cktwka3B5tRwmugKFfPINKNAG04cC9mVB2PnHZg0qAk0UbP6bm3APmJl6fOK3_XKQidyilYJ4w3t_tGtiUX_-ijLz_Yp6aykdwuzjeqGbESOeCo8nXy4To1D3LhzEH6VKbsuHgTcej7a_AADW7SHPHjPGeb5uNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMz0oH0u42QiAemlwAR_gUc-gDPQKdBpAKU1Nbza55e8hXJ44WQ54NLmrX0B9bC6YuGmG_qlgRzGXcqIufm0aVW541kyJCACFqfcTD1qgDPA2hOnqPgCSPevfkFKincsxxmC_moYo4ZJxI4G7z1LkeSxm0Gbvvr4WABjsCGFajqRJE2J1c31TYlXTPetufzv8k6CBpaHdGONJmbU-rOou_Y8cem5Lo7ggVnViE91Esbki7TGF2NY6gRjVaOg_GZB4n33xsiSf75zsI82utibFGmAfR7puxpZJKazCxqa58aywV6TRRFUZjPz61IpJrZAFPTtagvrvIZuXVr4ake9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsJepwvYNu-HnRJanXCJ_-HkLG2A7t1Y6GW_nuaTATdAqZl2g3gzNbZ4jhssP6EKcfTpnloE7QNCvLE3ACBpHXhOTUbIlsCTq-k40noYBExPPkIm1Q3SZ8YWUkppotfq4T_deIqjr6XANVzW2pMSuZ350XThI1RgcpGnzjNT1cEkjtoWfJywpOeVYCDvIue3lW79yJp0t3trDACdZLUrU7IdFGWIiM3tGi3dTFgwivG4k4v_IRHiPEaADjrFWIp82z8eFfWQ7IY4m6d0CjpJIlCVnwoeCzBjGj5H4_R9e-8Gewg4_sT7eruC3gpeMjPmrHqhBMgSN-bKz6_vnCCvsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMig2nsaX9Sgxbn_jA0lHe1iYzsfM9Ol1ZLuhpz4btsBmpOp7Ti4kL-PlovyA95ZGDWD5uLr91V-CgZ-sqOn2pqRSPcf_-p3l3qDZnOJVcSjBj8dA6o8N3FOU44LhqmW7zsEfdztEnTaB9zlxpdFy2U6YBRfhWgg6-OjqfkWVxeYM-MF5-u8HMwQiCPKZkF_NStBe9UU0JLTj8pm30vfCLsbxfCxzNGJupjuUteGr0H42pibYqx8xVkWELsntGYmapgdRg-zIZjGlNgzxTNylan-W43MB4Vg3s8Nmajx55At-JN7AqQJuMS-d1zccvnQLk9yB6ew47IyjFng5hl8tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رقابت شطرنج‌بازان در مسابقات اوپن ابن‌سینای همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/458306" target="_blank">📅 09:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUNwCIYb_wcxKKZA2D4Pg1S3B_SiFYb5MAfPiV87yCmRggLDh55zOJM9C0E8NpOdBUtZ2vZ8ggYu3cVDwxegzOAZF6vkZqtER98mL6-yYUlKRVGA5ZLDNGeM6e9As5SW_sykmPSsqWF6xD5kQzX5_ZlfpXZVkttDM47P8EuLPVuFc9Wcl0q5RlA6TQ9-aRN-Hcu9YpwxeUV0NT9eNs95qjMXbMZE7SL2FhGnQF9B2mCGr5yPLyZ8DdUnBOZUML1oR4pr6wCcjYW0lzLfqwOQz_DWc7nA_m9YD4hXndImYClP0RWsIlq5iLl4iDzUKzZIfWxxhxoulmOEpdOpAAqlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سندی که برای جبران شکست‌های برجام امضا شد
🔹
پس‌از خروج آمریکا از برجام و بازگشت تحریم‌ها در سال ۱۳۹۷، بخش مهمی از وعده‌های اقتصادی این توافق عملی نشد و شرکت‌های بزرگی مانند توتال و رنو از همکاری با ایران کنار کشیدند.
🔹
در صنعت هوایی نیز قرار بود با اجرای برجام، قرارداد خرید حدود ۲۰۰ فروند هواپیما از شرکت‌هایی مانند ایرباس و بوئینگ اجرایی شود، اما در نهایت تنها ۱۶ فروند هواپیما وارد کشور شد و هیچ هواپیمای بوئینگ به ایران نرسید.
🔹
در چنین شرایطی، دولت دوازدهم به‌سمت امضای کنوانسیون رژیم حقوقی دریای خزر رفت؛ سندی که از همان ابتدا با انتقادها و اختلاف‌نظرهای گسترده‌ای همراه شد.
🔹
قرار بود پس‌از امضای این کنوانسیون در ۲۱ مرداد ۱۳۹۷، ۴ موافقت‌نامهٔ جداگانه دربارهٔ مسائل مورد اختلاف، از جمله موضوعات اقتصادی و زیست‌محیطی دریای خزر، ظرف ۶ ماه تدوین و برای تصویب به مجالس کشورهای ساحلی ارائه شود.
🔹
اما حالا با گذشت ۸ سال، این وعده‌ها همچنان محقق نشده و موافقت‌نامه‌های مورد انتظار به سرانجام نرسیده‌اند؛ مسئله‌ای که بار دیگر عملکرد دولت دوازدهم در دورهٔ پسابرجام و نحوهٔ پیگیری تعهدات مرتبط با کنوانسیون خزر را در کانون توجه قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/458305" target="_blank">📅 09:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458304">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3bdd39e3.mp4?token=c6OIb-7sZokfZhKe-rsGmZSJYyxDS-Qx5TH3evAACPVbGx4LUPJyAHFfwpUCCK-IsRCWxG4LD1lkBgXbByE35EPsWRjr8IxZuHzTROIbBJTIsPX-N5jBirlml3NxO1aHaKLZitrpZyIN3Pw4kNywR1SjVHs9uYOhhAI6LRZAXir_7zDH48f3XniWZb1rvB4zPFoxfMNpz7bfyYB1a-7FXUJCtu2Fm8MU2ljJQwETAAgIENFjdRsKUSEI_-llw9CcY9rpxaW94l3IUi_RaceBlqrfDh6EpbbW7II0QAhlB1VE6SW5XHmtahu56asxqRUjz_0oAiSS2XhHFYll1M8DOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3bdd39e3.mp4?token=c6OIb-7sZokfZhKe-rsGmZSJYyxDS-Qx5TH3evAACPVbGx4LUPJyAHFfwpUCCK-IsRCWxG4LD1lkBgXbByE35EPsWRjr8IxZuHzTROIbBJTIsPX-N5jBirlml3NxO1aHaKLZitrpZyIN3Pw4kNywR1SjVHs9uYOhhAI6LRZAXir_7zDH48f3XniWZb1rvB4zPFoxfMNpz7bfyYB1a-7FXUJCtu2Fm8MU2ljJQwETAAgIENFjdRsKUSEI_-llw9CcY9rpxaW94l3IUi_RaceBlqrfDh6EpbbW7II0QAhlB1VE6SW5XHmtahu56asxqRUjz_0oAiSS2XhHFYll1M8DOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ مرگبار آمریکا به یک قایق دیگر در شرق اقیانوس آرام
🔹
فرماندهی جنوبی ارتش آمریکا از حملۀ مرگبار به یک شناور در آب‌های شرق اقیانوس آرام خبر داد؛ اقدامی که در ادامۀ سیاست بهانه‌جویانۀ «جنگ با مواد مخدر»، جان یک سرنشین را گرفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/458304" target="_blank">📅 09:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458303">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d2a92f83.mp4?token=IZVdiOW2pSwaZd_5OD55s5Mdho1s_Xh8z1lKeqN9VTRZ5dKTemU60wxYYhdPRl3-ZK8U7Ref6NWF5Rh1VBorXyPW6CGUgfON-_ksH0LaNJphpsr-FP0a6Yk_zqzTu3UJ0H-AIXQKmWJxwzsgF60F-HyhFw0PGOBcSFJV7XFFBy3LVH2PtHrLSDowEyqnWV4rnPc_cy1B8XT6_giZOy2sXabQWsSPfGWDY-9pU2ZI0KXOogyGQaj3Bl2Yh2nF4i_wLsxZUK9H5E-zOsj30iXELvfCTduO3IcAo5nwUZLR7JDx8PXnyR2_Fh_BQa0uvROZbPIg_HIHzEO76S8zxnn2gULxEwdKlq8LxGkMNWcR3LS11jWrHKDh9bXv_bgt4KDtdhJ2VkpzhostdrOCraZ5L1U2g_H9RTdKoJkpsDofIHokWQ1WwppFv-fMAtTs4g_JyjxSpzmvh8lar2D1DImE3Mo0VFAzojgVTNYx7PTfxS_Y8ikgiQe_c8YS-COynJU6F5ZVD6PiBcJDtfi6c1IvXCZISDW0AUUb5YqGx2iH29QHcDoFC1_3RwPW1OR3z3izprQzqlQKNgI6ph7uaod5jKswXLZFYCAaqe1rQjFF_0FqJw4En6nC5U4em0-YBCNHKS5ThdnPyax7OVLCkW66TiW0id7PKjWr9WXD65V3F74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d2a92f83.mp4?token=IZVdiOW2pSwaZd_5OD55s5Mdho1s_Xh8z1lKeqN9VTRZ5dKTemU60wxYYhdPRl3-ZK8U7Ref6NWF5Rh1VBorXyPW6CGUgfON-_ksH0LaNJphpsr-FP0a6Yk_zqzTu3UJ0H-AIXQKmWJxwzsgF60F-HyhFw0PGOBcSFJV7XFFBy3LVH2PtHrLSDowEyqnWV4rnPc_cy1B8XT6_giZOy2sXabQWsSPfGWDY-9pU2ZI0KXOogyGQaj3Bl2Yh2nF4i_wLsxZUK9H5E-zOsj30iXELvfCTduO3IcAo5nwUZLR7JDx8PXnyR2_Fh_BQa0uvROZbPIg_HIHzEO76S8zxnn2gULxEwdKlq8LxGkMNWcR3LS11jWrHKDh9bXv_bgt4KDtdhJ2VkpzhostdrOCraZ5L1U2g_H9RTdKoJkpsDofIHokWQ1WwppFv-fMAtTs4g_JyjxSpzmvh8lar2D1DImE3Mo0VFAzojgVTNYx7PTfxS_Y8ikgiQe_c8YS-COynJU6F5ZVD6PiBcJDtfi6c1IvXCZISDW0AUUb5YqGx2iH29QHcDoFC1_3RwPW1OR3z3izprQzqlQKNgI6ph7uaod5jKswXLZFYCAaqe1rQjFF_0FqJw4En6nC5U4em0-YBCNHKS5ThdnPyax7OVLCkW66TiW0id7PKjWr9WXD65V3F74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری پزشک قلابی که با سرم بیهوشی وارد خانه‌ها می‌شد
🔹
پلیس پیشگیری تهران بزرگ: مردی که با معرفی خود به‌عنوان پزشک و با پوشش «ویتامین‌تراپی» وارد منازل شهروندان می‌شد و پس‌از بیهوش کردن قربانیان اموال باارزش آنان را به‌سرقت می‌برد، دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/458303" target="_blank">📅 09:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458302">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d45ba451.mp4?token=HP6XoKx8PptfJ4935MHl39lNSGK2C1HSr3KYqpuYq8xZdi9EWOLfbWt025uTkLZ36xJk_gJJocD95EYAx6b77BSoR6W_oqyJWg6O3UJooRD-hdi25wwLTqPcGBcIUFCdOqVNHqUO6Xyexe3ZAEBgPuKJoDeRtCAlMYBAvLhBmjW04VhzQrnO1lq0Yts_sxI30XcZjdNLKd_GKusGgJwlmEuEJwoCMISDf7IKMf68R86HvrZ4dE69saEVvsQDzRmYb9UUdQqrdFQFoi9enwG7Bt_eJ4CRpWF5yRstuxYXRELwRF9YZ-Ys-UA4QOk0GGl03Muw6QimnYzFAYyT4QHxzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d45ba451.mp4?token=HP6XoKx8PptfJ4935MHl39lNSGK2C1HSr3KYqpuYq8xZdi9EWOLfbWt025uTkLZ36xJk_gJJocD95EYAx6b77BSoR6W_oqyJWg6O3UJooRD-hdi25wwLTqPcGBcIUFCdOqVNHqUO6Xyexe3ZAEBgPuKJoDeRtCAlMYBAvLhBmjW04VhzQrnO1lq0Yts_sxI30XcZjdNLKd_GKusGgJwlmEuEJwoCMISDf7IKMf68R86HvrZ4dE69saEVvsQDzRmYb9UUdQqrdFQFoi9enwG7Bt_eJ4CRpWF5yRstuxYXRELwRF9YZ-Ys-UA4QOk0GGl03Muw6QimnYzFAYyT4QHxzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت نفت: توییت‌های نفتی ترامپ خنده‌دار است!
🔹
توییت ترامپ در مورد احتمال پر شدن مخازن و ترکیدن خطوط نفتی کشور از نظر فنی و تخصصی خنده‌دار و خام و نپخته است.
🔹
مدیریت تولید و شبکۀ نفت کشور به‌طور کامل در اختیار متخصصان داخلی قرار دارد.  @Farsna…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/458302" target="_blank">📅 09:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458301">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
امروز روز کارمند است؛ چه توصیه‌ای برای کارمندان دارید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/458301" target="_blank">📅 09:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458299">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📷
تصاویری‌از اعضای اصلی مافیای سرقت مسلحانهٔ کشور که امروز اعدام شدند  @Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/458299" target="_blank">📅 09:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458294">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_iROrkkEdrUh8zVL5HZuC0K7DgTiZnVo-7HJiHz5a8xjY0GJfgsJJH4U4cS2K4PGhwcEDeSWUKdmLxwgBzEK9XZJgkpwz7nxH22N0gfetyqoZQaVnYTM7tvsTjz8-QleHgPx7PyaOa97IedILpwp2rx9BpfWOjYF7qkL4QcVZ9XOmcx9PNNQebyckmXWe-sZ5tfFpjmtbgB1xW0AlGJ5zkZWle-xmbfLixF_vCZTemGXNYZrnjkvFGJzQWEo-E3LsCHl4i_kO50VjDjMe4hQggM0h4ixno2b25OBe0gcyWXdJcIJykkGVD_kcF2XQ7-ho-TNEe2ZxWTcwkf97wLHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FW6wJSaxbuV4Z4AW7NZHubUrxxVBx0WkGGXej02kQ--ZPhBm8WSBOPmVYOeHwVGMstPP_7v92OBGnIFGoe7xBJvZOmLBKYaGtSBc3Bf9ZkwDOgpGll9jBB3FIw6yE_aqLpMqPdTHMnUDzsgwOuVEmdwCWpI4tWA9m6nfWIFYWPJ1Y73iRaG-MmILso4WC2JI1pIrDGKytQ4DsdZ6BQlbGTCYLbs-PIhjxYygUOpQha9_ZGPtTo-GmxX4N3I8KdOeGTuNlyUTEvOlrcS9o0F3ugQpXD5zy1Q9v4YBMpZm5JwH07XVvpQU9g19kN7iOj1yjQgHhZv-RyQl-SxanqDMKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERTNddzCwZCtg0a1NV26h7jQVIA1wemeRpL79Sxz5PhupczfKhRF43FD99n9dnVxqmu-K1WgAG_MDnfv5ivyMoh2jzkKSIVJ7kAeH9jCImnfEXB6sHtW7hiIiOOrdiDVL3XCLD9PVd2-Bdp2nlEL3lijct_meMJ3J5eFz0A8Q_Q97140eUaWdFcNm-l-brjGYAfItwPjlIFlnIr0hP_i4lhnJeCS6w2aFurT-79Ujt4U2GYM8c54cRks0gtW-Pg3rI4ianBlP3tftD9Nd-vLmVBuDSKV9KWM0KUHuRpGVcZ8B9ngSENxe_p8MaFNajcpoBjPld64W46mI_p-OZ8AZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/up0wdT4MZUcRm-ufioeTHhhUONE5U9labz8ZBGDwsclW0sXY-TCFcKDx_pOwpR6NZ84o9l1ukYBtSNkkzrO65cZnyr-HfoVEFkEjfPWlgudzezGEDMxWEg4u-zf6j6sM_rvcE5dUop4pUJRxfUB6Vlpeq5JkgNrDNu-l36QHkV7bk-YuWpyTjYI-bBVtTP5dKezKQPogWuNhwn4UOseEpaWLZ8Vz_kUS_SftTAP9nl_UTyr8z98rZdRjd3bT6993uJXxMS9Gsi39MARHY0EKr58yiX6KO5S8qvZC0MXrq-HyLVtH1rOnLw1pQHEfL6LtQCyxu42YNoaoBn1AONiEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxVi6IG4G6EcFZqo9PVGQlXfjPs2SrNuueMxFwh0NYRRkdJ0l2Odlb_BKu9uMMOUVK9NiaBlgO4YREyluLzSY0dnN89-43ufoDMicoO8RXnDWh-aggwB0_03M9X3UOgy52INILaZTUJ1_qv2rrX8LGXu4SM2rH9-WCbWy_b-oZgEN1nl2rzZ8DsnxR4Cf8XGs1pPiwYRuULz39TCRlwxPEO0bwZ-Wr5IXl3Vd35C7U8YgLdLq9eH6-F0EIF5-f7CMnUoL6ZsOkHZV7F4zGq7eO4squKwBiUPg0O6ZPJzjUm9poFuPXGpDTFnE5sgpNHvtDLoPIdvU_RICV5jA1_BnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«مافیای سرقت مسلحانه کشور» پای چوبه دار؛ برادران نجفی اعدام شدند
🔹
حمید و سعید نجفی، از اعضای اصلی یک باند حرفه‌ای و خشن سرقت مسلحانه، پس از طی مراحل قانونی و تأیید حکم اعدام در دیوان‌عالی کشور، به دار مجازات آویخته شدند.
🔹
این باند طی سال‌ها در تهران و شهرهایی…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/458294" target="_blank">📅 09:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458293">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d702a3dbe.mp4?token=uUKHn39g9VJuu6eC37hahEVq4XBVTATrzUzLivwT04BfFuhpjxaI7gFqKdJzjRs6AyDrLbj3K1e23P2GKlWF_w20OzRz2aG8n5V1dRp4vtyondrWXWDV6fE2SFmw3BC9jVGHfzfspaeCeATNMNJBRhZopvywlrYG3ZoUfahy90zpknm7-iwmyrz_pBIp8iSNtKXe7oFserXyTPkgH71tg03EUzuD94S5oYYTRZLULDIgKa0wpBJ_PLK1ol-wQATNw7CEdynHLN7_m1FPGQFl-jwEUkCc7fE33Cdi-K5_KjL5NqkXeP9vethUjqzwtVex12dDVdyFpFnSngmxr0XB9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d702a3dbe.mp4?token=uUKHn39g9VJuu6eC37hahEVq4XBVTATrzUzLivwT04BfFuhpjxaI7gFqKdJzjRs6AyDrLbj3K1e23P2GKlWF_w20OzRz2aG8n5V1dRp4vtyondrWXWDV6fE2SFmw3BC9jVGHfzfspaeCeATNMNJBRhZopvywlrYG3ZoUfahy90zpknm7-iwmyrz_pBIp8iSNtKXe7oFserXyTPkgH71tg03EUzuD94S5oYYTRZLULDIgKa0wpBJ_PLK1ol-wQATNw7CEdynHLN7_m1FPGQFl-jwEUkCc7fE33Cdi-K5_KjL5NqkXeP9vethUjqzwtVex12dDVdyFpFnSngmxr0XB9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به یک پالایشگاه روسیه
🔹
پالایشگاه نفت کستوو در منطقهٔ نیژنی نووگورود روسیه بامداد امروز هدف حملهٔ پهپادی قرار گرفت. در این حادثه دست‌کم یک نفر کشته و ۴ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/458293" target="_blank">📅 08:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">«مافیای سرقت مسلحانه کشور» پای چوبه دار؛ برادران نجفی اعدام شدند
🔹
حمید و سعید نجفی، از اعضای اصلی یک باند حرفه‌ای و خشن سرقت مسلحانه، پس از طی مراحل قانونی و تأیید حکم اعدام در دیوان‌عالی کشور، به دار مجازات آویخته شدند.
🔹
این باند طی سال‌ها در تهران و شهرهایی از جمله کرج، قم، مشهد، کوهدشت و مناطقی از مازندران و اصفهان، مرتکب سرقت‌های مسلحانه و ایجاد رعب و وحشت شده بود.
🔹
تیراندازی به مأموران، فراری‌دادن همدستان، حملهٔ مسلحانه به بیمارستان و قدرت‌نمایی با سلاح در فضای مجازی از جمله مواردی است که در کارنامهٔ این باند ثبت شده است.
🔹
اعضای باند با شناسایی منازل، با تخریب در و ورود به ساختمان، طلا، جواهرات، وجه نقد و دیگر اموال باارزش شهروندان را سرقت می‌کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/458292" target="_blank">📅 08:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458291">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0KxOumNn7RuLcFToLc9T25uXrDtSKC1IdhRFj1QvaFjeweuvv3uqCUPQ6WJyNcT1cZ2c-WdYPIWXSUw5p8xNnqpE0JUN9NWyPxFpl-6EDOu4-OTwddEaFSNh4TbY4x8wdK2adHqEthcLqj0Q2ya-yvUM-XGlWHr8sD6q0yVF3gC__05zEwBmS4wT-DORM1vIVxevLFaO0I8wB5rgpcyyIxHIfNLU2Gks8t6R4tvIZ3W-oBPlgkp6ZaIFMdachuQnze8uzNPNHA2WxwOuOxRgl3U0ERkra7NnpjbeF5QgR14OdOEFvSBRuiQ6SG6PiPHmY2MdKoEJAr-t6srszYagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمون جامع فعلاً جایگزین کنکور نمی‌شود
🔹
دبیر ستاد علم‌وفناوری شورای عالی انقلاب فرهنگی: ایدۀ برگزاری آزمون جامع برای پذیرش دانشجویان کارشناسی هنوز به‌صورت رسمی به شورای عالی انقلاب فرهنگی پیشنهاد نشده است؛ بنابراین در کنکور ۱۴۰۶ اجرایی نخواهد شد.
🔸
به گفتۀ دبیر ستاد علم‌وفناوری شورای عالی انقلاب فرهنگی، براساس ایدۀ آزمون جامع، دانش‌آموزان پس از گذراندن دورۀ متوسطۀ دوم به جای سازوکار فعلی، در یک آزمون جامع شرکت می‌کنند و پذیرش دانشجویان کارشناسی می‌تواند بر مبنای نتایج این آزمون انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/458291" target="_blank">📅 08:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458290">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هوای «قابل‌قبول» در پایتخت
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۶۹، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/458290" target="_blank">📅 07:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458289">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzBYuG3DIonhfQjhHCAPTInYvtt8JmFfs6OcpXEU6f4h2hCcNuLEycwWqG-2JXx6d0Otso1_Mf3AR8jhRUTmXs8nLQ9Y4jz7ef86y1f4uba_ys3vMdYZX3B9NMQ1_4NCmZFo7LDpIiPO8JKJb2qawvhA5gcXEhQV5RrOSUwAc0VUJhB3_UKNvdNgTuZq6_hNOtMfYgtOK13WMmsB5Oz9PvuXzYQ0xwM5hUxBztI4NFi8kCMYp4zDK5155nRPcLcxIUoSFNeg_rFMcLv9J1UQu62VcZNLbjGyIoy_rsG0bmQJofc42yPYecvMlCxQDARyPLnO1hT4qruhd_ik6Z5PJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان رسانۀ آمریکایی به خسارت چند میلیارد دلاری ایران به آمریکا
🔹
شبکۀ ان‌بی‌سی گزارش داد که حملات موشکی و پهپادی ایران میلیاردها دلار خسارت به تجهیزات اطلاعاتی و نظارتی آمریکا در غرب آسیا وارد کرده است.
🔹
در این گزارش آمده است، این حملات بی‌سابقه، نقاط ضعف دفاع پایگاه‌های آمریکا را آشکار کرده و مقامات را مجبور به تجدیدنظر در مورد نحوۀ محافظت از تأسیسات حساس کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/458289" target="_blank">📅 06:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458288">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119a91b079.mp4?token=IgYvtHBEfKreTsQQUWCa6eBavhZD_LeX_0bjNREOQ6JVAgkcgui-JnbV5vuPEKTvW382iqglgqsAWT36zPeelxJfEAqLfFeDCscfrQ8x5Gp7ZWCJw4z43FMW3tvWJ7vhP5-Po65AA0J0Aa9YTvttCD4ibqPvNwvg28qN39bfGSaTUttPaoHqPeP2Gyww2ti2AHUkX_hmDQCe3Q-9R-gFA9VhrFvkdbxL_j4w8n2sh8-nWUEsL37Jk0v_KeVMJ7pZRPWHVi2E-WwlCEKNWpAYQm0WSwAYu-NGpsIpZMTEzcePXTHMuxmUNStvWuZBoVwFnpQebndyoIQ2pvW228JJfkx6Yb-5sjqumrzAkuSGUpwbatBmq09qzzB7z09fgpzqO871677CP11VQjOHeX0i3Vu6P0qlr1agFIrlfgmxNCjVBeTuOzKRkh5qcRNmy6ZrefMoY6xKoJ-bn3Mbll5_Nknr0MSF0FViFY36IHV0rTmop4C8PrXwu2VHizAb6JnMPSMO8N1zy2cVHTriNbLPOWHMU4Sm7gLGn9npzhxZvpsyMY_dEFCFgBMLasVig8012WJ5_uBB3BiGmK9g9GFHK-csro_pDwvQTSWH6cn184lLcMNL4S1lB6PzcNmTeS3u0R3aTZXiTRqFaIckO7OGsgj6QsGDU68L_PADbieRa9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119a91b079.mp4?token=IgYvtHBEfKreTsQQUWCa6eBavhZD_LeX_0bjNREOQ6JVAgkcgui-JnbV5vuPEKTvW382iqglgqsAWT36zPeelxJfEAqLfFeDCscfrQ8x5Gp7ZWCJw4z43FMW3tvWJ7vhP5-Po65AA0J0Aa9YTvttCD4ibqPvNwvg28qN39bfGSaTUttPaoHqPeP2Gyww2ti2AHUkX_hmDQCe3Q-9R-gFA9VhrFvkdbxL_j4w8n2sh8-nWUEsL37Jk0v_KeVMJ7pZRPWHVi2E-WwlCEKNWpAYQm0WSwAYu-NGpsIpZMTEzcePXTHMuxmUNStvWuZBoVwFnpQebndyoIQ2pvW228JJfkx6Yb-5sjqumrzAkuSGUpwbatBmq09qzzB7z09fgpzqO871677CP11VQjOHeX0i3Vu6P0qlr1agFIrlfgmxNCjVBeTuOzKRkh5qcRNmy6ZrefMoY6xKoJ-bn3Mbll5_Nknr0MSF0FViFY36IHV0rTmop4C8PrXwu2VHizAb6JnMPSMO8N1zy2cVHTriNbLPOWHMU4Sm7gLGn9npzhxZvpsyMY_dEFCFgBMLasVig8012WJ5_uBB3BiGmK9g9GFHK-csro_pDwvQTSWH6cn184lLcMNL4S1lB6PzcNmTeS3u0R3aTZXiTRqFaIckO7OGsgj6QsGDU68L_PADbieRa9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باید هر روز بت‌شکنی کنیم
🎙
آیت‌الله فروغی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458288" target="_blank">📅 04:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458286">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKT7r3EjDBw-L5O-Z8aV9hnHXl0dvvwHDSo-vjcVm6aCrh-42Kr6NDMZV7g2ZWnLSRL_Gz1BUOK8bfeyuNa1DXaLPZxi7sY9Df97AZOSrpKPuO8fHFW6HnK3l9raBH0y-OLtJJ7rxrdS6HYmJl3Ygdf_yollzoeIhiSmLizy3WS9_XAqoB34x8LDfRZvLMP9Rlas9-ttyM5OJSsTyG0sV0DZQFIUXNPyG28nBbhUKb2HK_pSfGxCa1ZezCMzZLrbX9JCu4dJWNTAQfivRgrdfczh9atvsgTFZOjVyuBKnUVNyp9yhWGNW7-5bZrWAK8s-o6Y1JcNWwZzdm159dCfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط بالگرد «بلک هاوک» ارتش آمریکا در کلرادو
🔹
رسانه‌های آمریکایی از سقوط یک فروند بالگرد «بلک هاوک» ارتش این کشور در جنگل‌های «کلرادو» خبر دادند.
🔹
بر اساس گزارش‌ها این بالگرد تهاجمی در جریان یک عملیات آموزشی معمول دچار سانحه شد.
🔹
این بالگرد هنگام سقوط در شمال پارک ایالتی «گلدن گِیت کانیون»، چهار سرنشین داشت که ارتش آمریکا از ارائه جزئیاتی درباره وضعیت آنها خودداری کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/458286" target="_blank">📅 03:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458285">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گواهینامه موتور بانوان؛ یک کارت و چند گرۀ جدی
🔹
ماه‌هاست صدور گواهینامۀ موتورسیکلت برای بانوان از تریبونی به تریبون دیگر خبرساز می‌شود؛ یک روز از «رفع موانع قانونی» گفته می‌شود، روز دیگر از «آمادگی برای صدور» و روزی دیگر از «به‌زودی».
🔹
درحالی‌که هنوز زمان دقیق آغاز فرایند مشخص نیست، سؤال مهم‌تری روی میز است: آیا قبل از افزایش تعداد موتورسواران، زیرساخت‌های ایمنی، آموزش و نظارت برای این توسعه آماده شده است؟
🔹
این پرسش زمانی جدی‌تر می‌شود که وضعیت موجود موتورسواری در کشور را ببینیم.
🔹
اما نکته مهم اینجاست که نباید مسئله را به زنان تقلیل داد. بخش قابل‌توجهی از مشکلات موجود موتورسیکلت، امروز در میان موتورسواران مرد نیز وجود دارد: تخلفات، بی‌توجهی به کلاه ایمنی، رفتارهای پرخطر، آموزش ناکافی و دشواری کنترل تخلفات.
🔹
پس اگر همین امروز دستگاه‌های مسئول برای کنترل این وضعیت با چالش مواجه‌اند، افزایش تعداد کاربران موتورسیکلت باید بادقت بیشتری بررسی شود. موضوع، زن یا مرد نیست؛ موضوع ظرفیت حکمرانی ترافیک است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/458285" target="_blank">📅 01:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458284">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2hFNe20FVV-cSd_GSSx6dCptSyH8EmkHlKECM5dUOrmEzZMx3Em06LJ9PP6jSEfAXC9Yi1GlBwcfTVnTxYe1yv4Wb2f0TC_UmezxRgV7jDFh_tEtBkqQpgO1YF2NgwZCmNOS9u6VPzy4ECVPcd5YJWGihOtB7ZI5Qr6gMO1XDGFKjJ0QeRRUfSigbOMo-BkaXvW3q9PWspUV--0NIBdkaiKyYm03XXYQOA05OBPbSABdkoLpzTDd8T1kbDVO8TRtnWpblLFvs4GoewFBgYvlZe5s6mZZuM_TLx9saHNg1PdiUsy3mFXvIJWKnOdDHeZx79OzpRG9jeuCF5-eWX2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه هم حمله به نفتکش‌ها را کلید زد
🔹
روسیه اعلام کرد که سه کشتی باری حامل تدارکات برای ارتش اوکراین و یک نفتکش را در بندر پیودنی در دریای سیاه هدف را قرار داده‌ است.
🔹
همچنین روسیه به یک کشتی باری دیگر در بندر مجاور اودسا، و همچنین زیرساخت‌های بندری در پیودنی و اودسا و تأسیسات ذخیره‌سازی سوخت در بندر چورنومورسک نیز حمله کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/458284" target="_blank">📅 01:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458282">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fbfd859d.mp4?token=eqaSifM4uDKugHQBmhrO2-nIxt6Zi9RFIYftNcbN1qqG6-2OEhIFYPDm1pgunGhgjJZvQMyyMP9vA9Cedc8JZ7A2VgvFwt1180JNs3Rvp8l-XfMxHjY3UQ-CvKcu6DCZEyhzKdHhVkEKzL4-tOC9I_xV_KMxJlrfWK4kB06HGb5vhv-F0abnaIqmj-98zTnPjsdSaKrbDuY77h_PptVYlLu_TDfMtbmF7QfM2ZM7LuoU69wgvYZcL0ylKe60fn9Vl2cT6r0NaBl4QwEdqxO01EhHheSeuQdtNNpIoLD3E5OvI1cp7VDiD7u2q9Smy1IB4MA-qnhJs2t4737_TCG02A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fbfd859d.mp4?token=eqaSifM4uDKugHQBmhrO2-nIxt6Zi9RFIYftNcbN1qqG6-2OEhIFYPDm1pgunGhgjJZvQMyyMP9vA9Cedc8JZ7A2VgvFwt1180JNs3Rvp8l-XfMxHjY3UQ-CvKcu6DCZEyhzKdHhVkEKzL4-tOC9I_xV_KMxJlrfWK4kB06HGb5vhv-F0abnaIqmj-98zTnPjsdSaKrbDuY77h_PptVYlLu_TDfMtbmF7QfM2ZM7LuoU69wgvYZcL0ylKe60fn9Vl2cT6r0NaBl4QwEdqxO01EhHheSeuQdtNNpIoLD3E5OvI1cp7VDiD7u2q9Smy1IB4MA-qnhJs2t4737_TCG02A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات شدید اشغالگران به جنوب لبنان
🔹
المیادین از حملات توپخانه‌ای و هوایی صهیونیست‌ها به مناطق مختلفی از جنوب لبنان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/458282" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458281">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb48ad707f.mp4?token=v1tkyNwTbmEBBn1DzchkTJJkcfpGjpx1D4Bx7CcxaG9hFmDLC_NBMJM_kZGmE_YkRbZZvGWRBwMn7T8kdu6UtHiuSh8IIhxWupci4Dt7lkntr2hFTnenTon8IfYhmXoS4Mu9m5YFv9wvF7EEucE16pim14-BCSPEFm2IytB6y9gyAqiuiP2JK7Jqw02QjAHGXC37laBOraf_27cu-toG5Df-9LMq2BHnHArG_6ukjDnIO2X8AN1hTKDykO9zuFqflC1P4tYI96giNicBQDDXFSXD5tHcNILEKdqRNkUGtue6QefkQNUH15HagihooxrYonhS38I8Ws9pzaIYUM9oTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb48ad707f.mp4?token=v1tkyNwTbmEBBn1DzchkTJJkcfpGjpx1D4Bx7CcxaG9hFmDLC_NBMJM_kZGmE_YkRbZZvGWRBwMn7T8kdu6UtHiuSh8IIhxWupci4Dt7lkntr2hFTnenTon8IfYhmXoS4Mu9m5YFv9wvF7EEucE16pim14-BCSPEFm2IytB6y9gyAqiuiP2JK7Jqw02QjAHGXC37laBOraf_27cu-toG5Df-9LMq2BHnHArG_6ukjDnIO2X8AN1hTKDykO9zuFqflC1P4tYI96giNicBQDDXFSXD5tHcNILEKdqRNkUGtue6QefkQNUH15HagihooxrYonhS38I8Ws9pzaIYUM9oTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارتباط پنهانی جاسوس MI6 با مقام ارشد اسرائیلی تحت اشراف کامل ایران!  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/458281" target="_blank">📅 00:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KiPx4OirfIqOx45jumhwBszcukss_HkKHnFfQqE6U4eJePKGBtdQHzkjYEZj07uL2R90tKlTCy686LYRoCsqQNgs-OT_6OCbKYVMzjhWMkcWMN1oCFriCT439K8qqY9NYfBwK9hE6tPeQglQuPURr_lirPolhzNSz72DWC33gJAE3Fz9MH8szcElIGimBxBGpYiUnvIct6pLsL9uCjmSnIgcbKCIQXMvG26IHtFe936x09rG6nFv4AkyNDxE5qyVgXp6kAztVoD4F1oU_g_UyyWN-8J7CElt_YoeHhK77mZL0lI9RwmtVNXuXZmzsJri5q5GtW9Xggj_ZrwaOyrnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nqqdpo4F4K3DdPsUS9z3ne30-MXEntY4Q7YyuXsDypFzxVvlu0FlRaj4VOLEUXFgVVW388OLimq_9Kvq3riAWTEM5JGc2ILBU5PpqlZMNaJ7FUhNwgbP1xF17OOUykzMw3KLNmC1kJpSpC4uf-gQ85sMg4q_uhKONyy6nXKmBqPzNFZNRvJhgNTRPPVd1e9EK4IDfCMp_4_XVRSZEwmpVt_cESoUvy6-js_cs5FLTTK03F3yGgMzzzHk_BZ_lcWzjvgAPHHL3FbmhBbtCdB0XIDT5jA9irb8lLW824NnwrPV1Mo-1zZTmf465898C28WHMrusshUNA4HNr_q64obmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5PHNUk2r9duw9pyqz9F4-nHt3QW0v20K0pEzB8IaDQf7r-jHLkT1xTmYBYh595s8UbebsKdB5xevGX7S1sUQa-VPE_QEAF_FFRzTrf9oIGNUthUGzA23bkzcscT8GKVQYOSKXAwtv_HHdCHGz9PtguLzLyV5zwtHvSFg1XxiLfDbZ_rihe-e--EAsJsnsSg0J456KJgKquwWp6o60hPldsZCBKWlaK-GOUaAg3OHfooP7vpUWRS44kKEZFwknh8UzT3Zo9ZZht-4en1XlSET39t50Tu6wxhRBjgZu6tAVgJDG481tl_EWpXWwQ4qhqbIkLhbzFkG9vSoEMhBikjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxvUpcp6coNcfs0P66_OkXyGtalW8piMOxGZVKzmV77dFOVlwXPc46DP0mQvuaSj467JHxbUbsJ4cCXVCyjjd2vvHXrZpsbUIkCpSBYDdMZpqcmTHmNExihjDIHmwsB1UCJoTZIVvyzrhSZGc8mBdEDd0PCzSWDEoH_kh5iEsqkawzdNxWt76mlsBI0Iit3c0CYjzACXhhoMvTfvpGQfFLzfm1aZX6QDnCM17XV_TcPEqd-4NrTgarrlMItbjj2dtNVdVr7ZTApNm8kcF-r60HhTSEc3LqcVsBMfetsLmlRnocT4L3prnJoKlAGcU1KYttAKEvSkgRK1A_4Jb4eU1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۴ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/458277" target="_blank">📅 00:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458267">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ae8bcVFxNJEgDK4KNv58AZbii0EJqKIwzZJPJHcEtUS3oZeVwJ9XczW6j4gXKD3auZCZqr91NvBwcBaFZ8HF9eUxwhi0dpTNnBz2QRFiPZ9q74QNFzyFdwTpPSSBiJ7K9LtGj5GDGZGfojmwCEwoxgPL-A_KklWSs_uA-QHVntjm0Lh6kZFqybKAO0B0Fc_Dydqom1dlyKC7Xy-37FNgNIEIzPmq2CarzijK0pnmvUpnnGF_fm5IPCwOcuhJAWnMNPQng3nWm0XYur3GAxL0w8rzgG95ONU1Ice0lXE8o_kM9rMsa2PgO4wJahHfvqcNFPlkGgIdCA6lBH_Sgt4j7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KP6H3-e_RYgIUrp1t_iqp-clU2qIvju4kB0S0GVwU3d9KqvFNOGjtdVZeE6IV5mcjDdMLGX5TgwxybOW6yF7EehARnul1ZiQJFmF8t8J2S_OMLFaBzlkB865cUTYC-kYEZF_EmEvHduK5An7f-oR9RUYblzem5mfie65__cEqZEHxiceyMlXRXqge5U3bWmj2bCR02VZzh77DsQFXGLsf8dRS6AtUXbAPYxYyBq0Sgw9PyqeHeLVXh5P-wrwaI-DLKtdWW8WKvXGh4M9hspwxV4YqjyessUKQ2nSLaDILyiljj7QWCNPSJRQ-wYY_-lmmBBCRvXvQGwOhvunu0bdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6Xp3i4n4o9smgyCZ6bonMq3Tyig4KiOITsTUJK1PPQ2wlnoqUz05pS2HxYyjEsjZiPt_XEZ42BhKjPlSp1KuQkUw_r4JUdyD1z6RmuIuKy8uW8JdiG56-SCZ9g13INzqyiQxnKJBkj7jdyJSPo8DcMgvDOj6KYH0jFY9nqjaFa8faQDm2x5UjpDKVPAuNcomvKTHUvpCqmLjPbTMU3rYLvL_nJqu8l1uLAcl3xLGr5y8fiFY3UFDR17BolYAptc3WKrSA3juRiUHQJif02HW9AyApKQYzHu42kRXvtCRm3jCzA59a-MDuwMagv9GXleUjZw2DVRaBUUnEbN5ph1pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iu2nheat1feZgUm5AFxIL0Am8e7H3wWYb2iWNThV4QLSKo_6zIwDpCeEJOtqXrTdIfxjB6bCWql_eha41LHDF-lLld6mT2qNJJrmcKHD7wR3n9dGvLG2QSvxbjZoxR1uD4Nk5-Gj9YKXEAB5aZZk8_oGI6yFpiik4rD3NH75gokFR2lSWnYLHPBNbzr-TE--hc5mfcPZPPMxEr8sUJY3eTBZeIwgQ9cMzXsKeUXXQZAK9ZqI3F4-GIDVKpGAqd2eZNhXPQcYhDcuHkeS7MX50FZjLZR5bZ9UTg_T4baAeOJacnjrcA1A4moZ9F521bXtIG9ol8H8RDd8lCcJfzaHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6ST_jrqvaEwEhl3ZMM8slYJlSDyc9i39FZLajjsSe5Y8bvzTwwMnxwRelyaHj4P71Tt3PSr3wk8e0y3CjhArSAaKAIJsWnS15NYHgHuB8gqyTHnlI-vgvORKGN6LUFO8bjv_Yh06ta_BHSzJAxc1mZp6L1yaKvstc9DYq8AKPNamjTbgYI3vCJf1fVW0IXs2uNcnmwEKYReIfGvT4uBsFi1FgwB-Ka71bttrcIR7iiJ4BLkE8pMXrG9e-texiWyxnYBeuMbe7Yj2u_aZA64tC_LMSnlQVY7b6kjIcr6gVVpg6zJpe3qT1Grgw8gz85tWCYIQ4ZyA0RKr1s6wtg2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TK_IljML8udMUf90RKxxkg_r8oRu21wRS7lnwtINzuQdbBDGcsEMNJUgrhkZpWd9ncbzpUSlIlI4CA0pkhtLhJ1CoJg8NHMg0m5-p7dffKLQtZzfVsnAW6B9X9U59d5DpSrZuGg7tdVk0GMpGrN0Qh96CgUfcjNXFGZgLclrd-LKMkvtjVGDZgiffququFaKl5ku3wB9OFhsj0OGvIp0IUxKC67_Lips7lOJCb4BnUq5a7eeaFb_xPwEAQ-S1eVmsirsxehY_rwFsmN-ueAfbSZiUPzm5fpoA_G16yXVDCxPNTnbRTPlNd8G-_N0LisnhUxQWu7n7nkFyecLM5xamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVk54KKhBbKM5DYaJfv-pX2D20Sf2OLyujJnSRr63bwCVDa69mJJWeSCvz6fZuwy5HzAi-qDLRWd9tubT78uKOcbO3f5OY2JZUt3R-iL621Ts2t5_iFqRhJNkXtN78nrc7nw__y2tfe_XfxyuLZwaWGKyif9jOpJlOJb9puuxDkAIlQK88IVf5hk-s3m0Bl0XfAHKYe-b_K9SXhvtRo_6qPeaXla361J0wi_LAX8XudesQJwLOchbA2HkXFqX75Y9Sx7dAgQA7aY5DRDvn1HQIk8rnqAi10c1xJ45bmeKLXaUxyB5Z1kgzATIInuVAbdxB1eUd8nIsoXNWITT6TjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XUW-yzV_9mrhZsXf9q9wGHcaowbAv8JJSwAf9MgcnJJclj-bb8AHd3tr5txezOcOtOSZJIn6r9f3853Yha1woJjpUUZ9NfW8bdOPyJC5x_iDCA9agrZSM3uSdeiUJgUf0sfIk6qdUcDYVfz_8HnKRLRPDAslwTbx4EOLTKkA1_WJ1NS0WB6d9VRY-pw0X1p01P-KPOHFtrWb-9QDQPm7r3yHBV6DYGk-JzTaIF8IUdf6shMDyhobI48W5lICNvNCXiHb5z59Ir18ELF4Yrm07usk2OMlCKnbwby-AhILsh_M6u4ECuhnkCj5UP9EZfH4Ml2aAJI8p799pwlBM1mGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSjged_hULGcpeHU7akgjvMxJ5KJKrDmYJ-6FCK0VRpFjRX7ajQMqueueO9-q-txYKlwaEiG-bfZimHw-9ZKXOkjXAaVaGOQptgHGHUDtGi-lNnUe0aL078_-_e81JF2a6tPTVg5DMBwCgA1Y4HX7qDn1L4JO86z-hZCdM3_DiV0nSgZFE5jtTXqbinv1EvFNWOtFV-atB93S7xobUy-oOiBJ506TZWskJ2XIGdvWtsONkPkOkRSDnkvXez7KXJ8lcHxpHdZubRt4j_MtqUEwJP5KOwoSf7zb3NOqfPziMGmqcrOEKxRf-RDFM7fIBlcNHMqpXpg3f0SMueSiLHhbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjQFi230UNwZlLbh3jS3EZzAdl8YfcATnjXX-NcOmmLkcizG1IOOpg1qrDvTYhjt5hfEhMY3EexylGu-POMvKhXgWJHNCqHtJkZNYSNQ8VSpa3hwCa4TkeeN-a5QF9DkRWb7syFOPrgs45R_Kr1GNZdETHS4Z-TuvIwbO0rLr7KMyU2MyIs-Npc0plSvv6RREuKMeXT4hsfN9GLqHU8KyflXpfInRJZaU72WTZa89jl4cZp2yIj1EtzU2LmYogI2X7tZLigR5uCzcQZYA1QcXxyziJGs-vpX9srxVvoB5WIbLvEq_3LteU-92DpwWywlqHChVq7lROTkymgyL8kITA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458267" target="_blank">📅 00:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT2QDiUYoIt5qC7csdA7eA9Llxee0bKSfLWc0AkNmrsTD6b6PB1bBt54t_LSWCWEQnhMBP_-_U23UZZY7HTwg-Iz4sMPMP7ShpkONvvOPHojHcMV8ZAKAhOes3Nm6RMn21_kzL6JN36bi5jEmU8i2Io0tPB-WkRBWjdZ6caNsCBL999GV6kRwdgwWDPbiPKy07GB3jcHYFZye5jrAO7OeFxLhyowJFb0ydjMlJPPzfvBRYIriQaDkh5AxAEwc2TpAaj5EQXleLiMosQJWGhSevSXILBLVHzhN-Z_U3hxhGth72HLkhE9rE5I71jUcoOeMcqTD58nNcMf0fOLZNTosw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک به پرسپولیس در آستانۀ دربی
⚽️
اورونوف در دیدار تدارکاتی امروز پرسپولیس مقابل امیدهای این باشگاه بار دیگر دچار مصدومیت شد.
⚽️
هنوز میزان مصدومیت و مدت زمان دوری این بازیکن از میادین مشخص نیست. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458266" target="_blank">📅 00:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
ارتباط پنهانی جاسوس MI6 با مقام ارشد اسرائیلی تحت اشراف کامل ایران!
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/458265" target="_blank">📅 00:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458264">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b05f709e7f.mp4?token=fx9rt54wXg_Gb5SymxwqIaFV9FLX2FRndiV8k9pInLKSQ3mGS6MXc8rYp3RPYy7hOBK40qcGtYz4ytz1vw5gc_OPruxShIeBjSSfseFcKi23E1X1OfmqTVFoOwfywyczX5MQXyeaAAJalEulJGp_aN3ewSbKT8wDrdkEwkG_v8mPsmR_l1SkWulVnzz-poROPO8r0jimukB0ZRjH9aW4E71QwhPsOj9lhXipjJzAdLJCQAE_GW98rwzbhCjlsS1O-IHem9GY3IUii8k0FawFykMdF5Q1yS2f_HkVVbyTbhdHqf8EhgoghLkFOu41OTrMMVXUzAHicLvO2DU8fFi_qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b05f709e7f.mp4?token=fx9rt54wXg_Gb5SymxwqIaFV9FLX2FRndiV8k9pInLKSQ3mGS6MXc8rYp3RPYy7hOBK40qcGtYz4ytz1vw5gc_OPruxShIeBjSSfseFcKi23E1X1OfmqTVFoOwfywyczX5MQXyeaAAJalEulJGp_aN3ewSbKT8wDrdkEwkG_v8mPsmR_l1SkWulVnzz-poROPO8r0jimukB0ZRjH9aW4E71QwhPsOj9lhXipjJzAdLJCQAE_GW98rwzbhCjlsS1O-IHem9GY3IUii8k0FawFykMdF5Q1yS2f_HkVVbyTbhdHqf8EhgoghLkFOu41OTrMMVXUzAHicLvO2DU8fFi_qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غریب‌آبادی: اگر اقدامات آمریکا ادامه پیدا کند ایران ظرفیت‌های جدیدی را رو خواهد کرد
🔹
تنگۀ هرمز تنها ابزار ما مقابل آمریکا نیست.
🔹
آمریکا نباید فکر کند که خودش تنها طرفی است که می‌تواند آسیب اقتصادی وارد کند. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/458264" target="_blank">📅 00:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-Z1YmGgnm_7tg-fdMJYKrWM98neBhDZDQSBsjUujCMNw7x3RtP9315KKMYBX2r3mOOJWsWtnlDTBZIBdznR8ZtoKz_NnCjYCl6QJ7jcdvpx5lFKpxuF-v75NbKGqvbhCPpyhptj9Tb0OPeMb0Xb43xUwz1Y8SjpG8yBYX2bdF1LHpUmTPyYBEtfGp1Yq_XYpQU3tyB2AFc9cMynx4NMp72uJC_ayDK4Wt8PDtyKzNJ-teNEASPsvIghw3szsYrXBtHuwlozCZCJR8IU6HEy2H7PCqS9bEafLCS3JnS0y6h2_kMZuxgAWDH-AecZF1r5cwiDOqvTM4gy1Klm3v98Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمان واقعی کیست؟
🔹
پیامبر اسلام(ص) از محلی عبور می‌کردند که گروهی از جوانان مشغول مسابقه و جابه‌جا کردن یک سنگ بزرگ به‌عنوان وزنه‌برداری بودند تا مشخص شود کدام‌یک قوی‌تر است.
🔹
پیامبر از آنان پرسیدند: «آیا می‌خواهید به شما بگویم قوی‌ترین فرد میان شما کیست؟» جوانان با اشتیاق پذیرفتند.
🔹
پیامبر فرمودند: «قوی‌ترین فرد کسی است که وقتی به گناه و خواسته‌ای نفسانی میل پیدا می‌کند، بر نفس خود مسلط شود و دست به گناه نزند، وقتی خشمگین می‌شود کلام ناشایست بر زبان نیاورد، و هنگام خشنودی و خشم، از مرز حق و عدل خارج نشود.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458263" target="_blank">📅 00:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5419315c23.mp4?token=m0Osy8ywRzn3C78FASeeZbMGNmJXPrGjTxvGJsCzFMEpXZbkDjEFDgqKL4tnKfSboLSYTCz_0frfIT376vTLMSehs_XtgQ4MSZ7w3OKLksMUg8O336pOl2qA358LluLk4rrkfzs55VILEi1lZ8BYroV3QA05OsKF4elqROxNYn-ITepE8_6cJkgDjHfX8GY0bcdghSBqiN7jcRARe1f9tQMZpSOCYnOO7b8gj-QVtDMgPI3jtkau1iDSK2uSw1R_yVm1jT7drP7d8nUgiHMXN168KB8TcBW9ermbs4YWMlMEKslmpfG2i5EIm8t0M3Fvt0704-1HPeqc-UqY-hyZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5419315c23.mp4?token=m0Osy8ywRzn3C78FASeeZbMGNmJXPrGjTxvGJsCzFMEpXZbkDjEFDgqKL4tnKfSboLSYTCz_0frfIT376vTLMSehs_XtgQ4MSZ7w3OKLksMUg8O336pOl2qA358LluLk4rrkfzs55VILEi1lZ8BYroV3QA05OsKF4elqROxNYn-ITepE8_6cJkgDjHfX8GY0bcdghSBqiN7jcRARe1f9tQMZpSOCYnOO7b8gj-QVtDMgPI3jtkau1iDSK2uSw1R_yVm1jT7drP7d8nUgiHMXN168KB8TcBW9ermbs4YWMlMEKslmpfG2i5EIm8t0M3Fvt0704-1HPeqc-UqY-hyZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: به عاصم منیر گفتیم به آمریکا بی‌اعتمادیم
🔹
به فرماندۀ ارتش پاکستان گفتیم این ما نبودیم که تفاهم را نقض کردیم و آمریکایی‌ها اگر علاقه‌مند به بازگشایی تنگه هستند باید شرایط ایران در تفاهم را اجرا کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/458262" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51420b8699.mp4?token=Jf9Krrp318_ORnjxsYGkXZ8AqzZsDLRflZU4ICudTw4paIoj6EM_etJd9f42hWqudseZmkIBVyZx3mgOHEWVXGJe4K5ql-rOUME2Alnoa2vYFzZAM62qbcGcNi41Mr05hua7j6n8hmcarPMuyUcZjgWMM4RA3ZLMYHkyGORI0cHlk1H7lR6JUmd1l5k5idCU4MZ-5_kuvk5EgCo22mXLZdou3p-lNOJ8Uw0mE1zuHhkJQQTJkeaVWUOFRMTCkGzSUIbw6PJxEsWHrRXnnNSDLzXQ9Yh_Xp6ahYM2mYfBFBBfQPplkEknz-EimKHaKL-ZlWlsICFPqp2P5jXX0Ea2Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51420b8699.mp4?token=Jf9Krrp318_ORnjxsYGkXZ8AqzZsDLRflZU4ICudTw4paIoj6EM_etJd9f42hWqudseZmkIBVyZx3mgOHEWVXGJe4K5ql-rOUME2Alnoa2vYFzZAM62qbcGcNi41Mr05hua7j6n8hmcarPMuyUcZjgWMM4RA3ZLMYHkyGORI0cHlk1H7lR6JUmd1l5k5idCU4MZ-5_kuvk5EgCo22mXLZdou3p-lNOJ8Uw0mE1zuHhkJQQTJkeaVWUOFRMTCkGzSUIbw6PJxEsWHrRXnnNSDLzXQ9Yh_Xp6ahYM2mYfBFBBfQPplkEknz-EimKHaKL-ZlWlsICFPqp2P5jXX0Ea2Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: شناورهای مین‌روب آمریکا اگر وارد منطقه شوند اهداف بسیار خوبی برای ما هستند
🔹
صحبت‌های ترامپ دربارۀ مین‌زدایی فقط برای آرام‌کردن بازارهاست. @Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/458261" target="_blank">📅 23:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">زاکانی: برخی در داخل با رفتارهای خود به دشمن کمک می‌کنند
🔹
علیرضا زاکانی، شهردار تهران، در جمع مسئولان بسیج دانشجویی: برخی افراد تلاش می‌کنند ایران را به‌عنوان عامل برهم‌زننده تفاهم‌نامه معرفی کنند، در حالی که آمریکا تفاهم‌نامه را نقض کرد و با اقدام خود در جنوب تنگه هرمز و ایجاد یک مسیر، عملاً مناسبات موجود را برهم زد.
🔹
امروز باید با مردم گفت‌وگو کنیم و موضوعات مختلف را برای آنها تبیین کنیم،  اما این گفت‌وگوها نباید صرفاً در حد حرف باقی بماند.
🔹
در شرایطی که آمریکا در معرکه نظامی شکست خورده، به‌شدت تلاش می‌کند از طریق فشار اقتصادی شرایطی ایجاد کند که کشور به سمت فرسودگی حرکت کند.
🔹
عده‌ای در داخل کشور با رفتار و بی‌تابی خود به دشمن کمک می‌کنند و این مسئله مسئولیت ما را سنگین‌تر می‌کند.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/458260" target="_blank">📅 23:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3883c96fc4.mp4?token=SDACjBBa7oDhLddoVbeVC2gKijcFF-tyRnN4j47qZJphR5s7fvclyOMsQCueCiGAz7MhY5s-wcuaWzBn2euh6OQtiNVag3TRc6USB1Vq4-_-kSlwBk_9pR8IPQbmFrbgcmC1kOBB0bPr-ArBzwo849pH4O11ixaTqWWZ0hnxwX3a0xFZQ3kgLvLAYW7FZceyhnzqz0ssC7fEtuaxetnPnH3MkfK2M_GLv1fuT43teWE39yC8vVFxVJEcR-QLY34ZGCHRkEAiN0rGVaJVLCBbCh8Pgar0X4wp3i1sAY6s3TNP1rCMtZj5_44183WESm0jv-FXQjNbT9drocmCM_SKgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3883c96fc4.mp4?token=SDACjBBa7oDhLddoVbeVC2gKijcFF-tyRnN4j47qZJphR5s7fvclyOMsQCueCiGAz7MhY5s-wcuaWzBn2euh6OQtiNVag3TRc6USB1Vq4-_-kSlwBk_9pR8IPQbmFrbgcmC1kOBB0bPr-ArBzwo849pH4O11ixaTqWWZ0hnxwX3a0xFZQ3kgLvLAYW7FZceyhnzqz0ssC7fEtuaxetnPnH3MkfK2M_GLv1fuT43teWE39yC8vVFxVJEcR-QLY34ZGCHRkEAiN0rGVaJVLCBbCh8Pgar0X4wp3i1sAY6s3TNP1rCMtZj5_44183WESm0jv-FXQjNbT9drocmCM_SKgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: اگر آمریکایی‌ها تنگۀ هرمز را مین‌زدایی کرده‌اند چرا از آن عبور نمی‌کنند؟
🔹
هیچ‌کسی به‌جز ایران از مکان دقیق مین‌های تنگۀ هرمز با خبر نیست. @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/458259" target="_blank">📅 23:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b3fb88dd.mp4?token=q9BmFJnK8QFRpt_mJBF426Jqw9K7l6BUo-JN2zsWorSTzYWx_rUsoJQnSeG2IaWaVNYVFYR-PjX0aeZynMpd4qeGNa4QvRjS4qtKbCK2QKx4TdRA4qbzfkAuasJqPC_fQtItvtl9WsL6CRRCRAjQo9aOrMKAVfNJUTT70KhrAFjcXt79O2erMflNe6-s85ywtacEcqQBd9qV-1vIXoi0QgMgiys-GqmmXg9z_dp7ynEDE83e8zhBWyVuJ6jFsaT5SgqkTnLzH0HsTxH_yEFpZ8zXaJEQvG1Szdr2NrpCt26OhCJBqfLL9YMi-oHR6kYgV4RAluBQjxF4tLXWHUo6lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b3fb88dd.mp4?token=q9BmFJnK8QFRpt_mJBF426Jqw9K7l6BUo-JN2zsWorSTzYWx_rUsoJQnSeG2IaWaVNYVFYR-PjX0aeZynMpd4qeGNa4QvRjS4qtKbCK2QKx4TdRA4qbzfkAuasJqPC_fQtItvtl9WsL6CRRCRAjQo9aOrMKAVfNJUTT70KhrAFjcXt79O2erMflNe6-s85ywtacEcqQBd9qV-1vIXoi0QgMgiys-GqmmXg9z_dp7ynEDE83e8zhBWyVuJ6jFsaT5SgqkTnLzH0HsTxH_yEFpZ8zXaJEQvG1Szdr2NrpCt26OhCJBqfLL9YMi-oHR6kYgV4RAluBQjxF4tLXWHUo6lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غریب‌آبادی: پاسخ جدید ما به تحریم‌های دشمن هدف‌ گرفتن منافع اقتصادی آن‌هاست
🔹
نباید مثل سابق با تحریم‌های دشمن برخورد کنیم. @Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/458258" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f652d6dd.mp4?token=Dfg5M9ft6CR-G-43kiyTg1Q43wLzqc7Fr-0vJOa8hq7wu_PQ0Ny-eOeHFcAEejjHNrQCix_H3k_SEi-D-D5TaQDz7cdiidbjMio2DEBFRcP1CxDxQNbjYJDkigqDeCqaYFvQXuit9oQcp0hswNv6jb4arSH06T7-FGFJBDWQx-gj1ysZkGRHidyYPpfB5Di0pzhdLb-0pnFTP3yeZee_W1f4Ndglg9Rme3Hdn8ex7kn3GEeCmSsogmpu6MeWq7NGT41J_rL9PnSV0c7GQdatON6BLqL-_6z-wvCqMNMQJnNtPfK4Iwoo8mNFmXuN3Q8fIL8f9YJb26T32UpV51YYBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f652d6dd.mp4?token=Dfg5M9ft6CR-G-43kiyTg1Q43wLzqc7Fr-0vJOa8hq7wu_PQ0Ny-eOeHFcAEejjHNrQCix_H3k_SEi-D-D5TaQDz7cdiidbjMio2DEBFRcP1CxDxQNbjYJDkigqDeCqaYFvQXuit9oQcp0hswNv6jb4arSH06T7-FGFJBDWQx-gj1ysZkGRHidyYPpfB5Di0pzhdLb-0pnFTP3yeZee_W1f4Ndglg9Rme3Hdn8ex7kn3GEeCmSsogmpu6MeWq7NGT41J_rL9PnSV0c7GQdatON6BLqL-_6z-wvCqMNMQJnNtPfK4Iwoo8mNFmXuN3Q8fIL8f9YJb26T32UpV51YYBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی : چرا باید همیشه ما منتظر بمانیم آمریکا حمله کند؟ ما می‌توانیم دست به اقدام پیش‌دستانه بزنیم @Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/458257" target="_blank">📅 23:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1171817f19.mp4?token=pxSR-k4BWRIu5BgDJx5y6eNC7lowPi96iog8JTmfnyPDd1DQ_A0l84hYTqwJHqkEYqBl0TeU6gPAIZmzI3e0QgP8ElLPXS-RMZkk7XiUnVeWm3CrQyE276GXPEj7uXyu7N7G1gmWsUhOtSlVu5xarpa7xgRBvGBfaHApDa2fw61o_Xhq8qlmYGjYY0_SSAk0zm3XA3O9wTfW2SiamDuMOU7Ef86mNrfnQcKiaOY11vmpBReOUioHYfVoHNeehiaMDugFOqKVn5e3ZSjaWriF3ewLKg0i05Eo45cpMIig-WucI1VAo0tINYt8BhEOnKlZAASKexkxehx57bb29Ifdcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1171817f19.mp4?token=pxSR-k4BWRIu5BgDJx5y6eNC7lowPi96iog8JTmfnyPDd1DQ_A0l84hYTqwJHqkEYqBl0TeU6gPAIZmzI3e0QgP8ElLPXS-RMZkk7XiUnVeWm3CrQyE276GXPEj7uXyu7N7G1gmWsUhOtSlVu5xarpa7xgRBvGBfaHApDa2fw61o_Xhq8qlmYGjYY0_SSAk0zm3XA3O9wTfW2SiamDuMOU7Ef86mNrfnQcKiaOY11vmpBReOUioHYfVoHNeehiaMDugFOqKVn5e3ZSjaWriF3ewLKg0i05Eo45cpMIig-WucI1VAo0tINYt8BhEOnKlZAASKexkxehx57bb29Ifdcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: پیش از هر اقدامی برای بازگشایی تنگهٔ هرمز، آمریکا باید تمامی تعهدات نقض‌شده خود را به‌طور کامل اجرا کند.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/458256" target="_blank">📅 23:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74edce467f.mp4?token=rRvTBYwXuaWrJ9_6nZpqYF9J1I-lt3EeO9dV6dl5ZIOf2sPYp__5i5Yrs-CmvzxdZWe_BSrcc_HFiT70QX1xVDfxMGEJZ6dVhMYqd8HGJvcOOSk92i619bl-EV6XLrAGT8cJ6uVkH2S8OLgFXAez1RIeiq50JdkZJjCn36zsxGUShQVYwfSmLyNZAG-iNWfQYZ_yfLV5r6sZTFKBEkc5yyzPefz-IynIEYw4rxfiA5TL80hrka7hxgw0lWlO8dCG9vFJsIUPe1TVFbM-VAnyDf-rHJjJGjSAFQl63-HhjeyUddZVe-ImFW_Lbi4RXokLBwWRZOKMPBKYXlueZDUHpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74edce467f.mp4?token=rRvTBYwXuaWrJ9_6nZpqYF9J1I-lt3EeO9dV6dl5ZIOf2sPYp__5i5Yrs-CmvzxdZWe_BSrcc_HFiT70QX1xVDfxMGEJZ6dVhMYqd8HGJvcOOSk92i619bl-EV6XLrAGT8cJ6uVkH2S8OLgFXAez1RIeiq50JdkZJjCn36zsxGUShQVYwfSmLyNZAG-iNWfQYZ_yfLV5r6sZTFKBEkc5yyzPefz-IynIEYw4rxfiA5TL80hrka7hxgw0lWlO8dCG9vFJsIUPe1TVFbM-VAnyDf-rHJjJGjSAFQl63-HhjeyUddZVe-ImFW_Lbi4RXokLBwWRZOKMPBKYXlueZDUHpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ‌غریب‌‌آبادی: بازگشایی تنگه هرمز تنها در ازای پایان جنگ در همۀ جبهه‌ها، رفع محاصره و تعیین‌تکلیف وضعیت یمن رخ می‌دهد. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/458255" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌‌ غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
🔹
البته درحال حاضر هم نیروهای مسلح ما اجازۀ عبور از مسیر جنوبی را نمی‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458254" target="_blank">📅 23:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
حضور مردم تربت حیدریه در میادین، همچنان پرشور ادامه دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/458253" target="_blank">📅 23:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌ غریب‌آبادی: تفاهم با عمان دربارۀ تنگه هرمز به معنای بازشدن تنگه هرمز نیست
🔹
در تفاهم با عمان مسیر ورود به تنگه کاملا در اختیار ماست و بخشی از مسیر خروج هم در آب‌های ایران قرار دارد؛ همچنین فاصلۀ ۲ مسیر زیاد نیست. @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/458252" target="_blank">📅 23:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌ غریب آبادی: انتظار داشتیم تا با کمک دوستان عمانی مسیر جنوب در تنگه هرمز را ببندیم اما فشارهای آمریکا مانع شد و ما مجبور به درگیری نظامی شدیم  @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/458251" target="_blank">📅 23:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458250">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">غریب‌آبادی: همچنان در وضعیت جنگی قرار داریم
🔹
معاون حقوقی وزارت خارجه: تا پیش از جنگ‌های اخیر هیچ مشکلی در تنگه هرمز وجود نداشت و ایران نیز تمرکز ویژه‌ای بر مباحث مربوط به این آبراه اعمال نمی‌کرد.
🔹
پس از جنگ ۴۰ روزه، توجه و تمرکز راهبردی ایران به این موضوع…</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/458250" target="_blank">📅 23:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">غریب‌آبادی: همچنان در وضعیت جنگی قرار داریم
🔹
معاون حقوقی وزارت خارجه: تا پیش از جنگ‌های اخیر هیچ مشکلی در تنگه هرمز وجود نداشت و ایران نیز تمرکز ویژه‌ای بر مباحث مربوط به این آبراه اعمال نمی‌کرد.
🔹
پس از جنگ ۴۰ روزه، توجه و تمرکز راهبردی ایران به این موضوع جلب شد و ما همچنان در وضعیت جنگی به سر می‌بریم.
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/458249" target="_blank">📅 23:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458248">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27ed05b57.mp4?token=qpccxg7VhP5AGH33f5BPl4JYzi-Whn2uzmwh4-zKS1rwwpiOIdRY7yul2AuaZc_qn-9LATV_0yfLr3tnxpleWoLbLwZbK3SZr3mWdJjF-2z6eewelk1xmWYwzdwv6RGYvzb1MWTad_3BAaLk0PvcMr6LFxFigKjLcht_mzGfGqc-a_cWeT8sY0uQC14AbLAEif1KwEjJyFhJUujK__3jyHknYZyg0MnG7w3XUpGfjNvhN5sDXlxvr4ugC3XSqHxJOfy6dRKd9NuI2R4KMznIkDJrKMh1Hby44S0pZpV0MoMZYTWR_akjxidKMFEmk-TcE45v82obEtlktvzligS5cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27ed05b57.mp4?token=qpccxg7VhP5AGH33f5BPl4JYzi-Whn2uzmwh4-zKS1rwwpiOIdRY7yul2AuaZc_qn-9LATV_0yfLr3tnxpleWoLbLwZbK3SZr3mWdJjF-2z6eewelk1xmWYwzdwv6RGYvzb1MWTad_3BAaLk0PvcMr6LFxFigKjLcht_mzGfGqc-a_cWeT8sY0uQC14AbLAEif1KwEjJyFhJUujK__3jyHknYZyg0MnG7w3XUpGfjNvhN5sDXlxvr4ugC3XSqHxJOfy6dRKd9NuI2R4KMznIkDJrKMh1Hby44S0pZpV0MoMZYTWR_akjxidKMFEmk-TcE45v82obEtlktvzligS5cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: قیمت برق فقط برای پرمصرف‌ها گران می‌شود
🔹
بدمصرف‌ها اگر این شرایط را ادامه دهند ممکن است در ماه‌های آینده قبض‌های سنگینی داشته باشند.
🔹
اگر کسی نیاز به مصرف بالا دارد باید به ما مراجعه کند تا از بورس انرژی برای او تامین کنیم. @Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/458248" target="_blank">📅 23:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458247">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdcc2e628e.mp4?token=RUDLZ4QHxu7ApRI4gSDu8Pi6XUR1uN_l5G5PSIp1o4IY0RjOtWVNWN3RA-OvAuR3hArUkPa18bbRdb7wnhswjaM3ltB7HtKPTaKZGURV3k_anZxbfRHog74v-Z7thpysa42Y9cmNIT40Q1CpCfUHmfAhbzoPuVJrrrHGKGg8CkuEgiAt68wqVZ-4Z-aTgEJgYH5AtlExn8LPYALaogJ2AlHcPWWMsm2S9Tc7vZmiGPAeUAlsdLeZaBbe_9iN8Z0ZP-Suqg8suDfq0JR3bYi5tsZD-3fk29uovh1CJ0mStk8RcDUtoKtsSjxH6WDoj1C3ZbgCz1kKuloRl1Nw-obMJIkWIP-aP80zi86xO7wfB6et5e4r274iExT6jGFJdDQpTwFzhWugZ_cJQgLFS2C7s49Pyw0_1OFSeupxlIz3QX_dJ9fjYrO0OULdTNXWx86x7V-220B4zj8jWbe0JJ12cZQ2MES3P39agf3cdyaCXtXHJ6pz4JUlIMCzP6_vD1EyBMAktR5z2D7US6M1D7i2TPuKjj9xnd2wpZ2rgyyXmZm4tFZdy9Tx8s7J29jWQ2DYHZO_nb7fdlGfK8UKgorR9RGWc9ShfI6G7jr2fgww5X_y7akJ4LSDCd4uEFZ4rCb2uqbXxSSVg0WHw3oWx-8Dk68Mm9baZo19crCLOvFx-s8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdcc2e628e.mp4?token=RUDLZ4QHxu7ApRI4gSDu8Pi6XUR1uN_l5G5PSIp1o4IY0RjOtWVNWN3RA-OvAuR3hArUkPa18bbRdb7wnhswjaM3ltB7HtKPTaKZGURV3k_anZxbfRHog74v-Z7thpysa42Y9cmNIT40Q1CpCfUHmfAhbzoPuVJrrrHGKGg8CkuEgiAt68wqVZ-4Z-aTgEJgYH5AtlExn8LPYALaogJ2AlHcPWWMsm2S9Tc7vZmiGPAeUAlsdLeZaBbe_9iN8Z0ZP-Suqg8suDfq0JR3bYi5tsZD-3fk29uovh1CJ0mStk8RcDUtoKtsSjxH6WDoj1C3ZbgCz1kKuloRl1Nw-obMJIkWIP-aP80zi86xO7wfB6et5e4r274iExT6jGFJdDQpTwFzhWugZ_cJQgLFS2C7s49Pyw0_1OFSeupxlIz3QX_dJ9fjYrO0OULdTNXWx86x7V-220B4zj8jWbe0JJ12cZQ2MES3P39agf3cdyaCXtXHJ6pz4JUlIMCzP6_vD1EyBMAktR5z2D7US6M1D7i2TPuKjj9xnd2wpZ2rgyyXmZm4tFZdy9Tx8s7J29jWQ2DYHZO_nb7fdlGfK8UKgorR9RGWc9ShfI6G7jr2fgww5X_y7akJ4LSDCd4uEFZ4rCb2uqbXxSSVg0WHw3oWx-8Dk68Mm9baZo19crCLOvFx-s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو:  اگر اتفاق غیرمنتظره‌ای رخ ندهد تا ۹ ماه آینده مشکل برق نخواهیم داشت
🔹
تابستان سال آینده هم شرایط بهتری از امسال خواهیم داشت. @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/458247" target="_blank">📅 23:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458246">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84b7cdbcf7.mp4?token=LVjQEf4z-5lmmXyJ_agt1VgoviOceOGko8D5xWj4wEb6JpJxIlEKaODxByKktYznmyn5BBJbD2Mq8Zl5h7dgSyOM8EWk93WzzEMqHNdNSgS6yLJa1Egrooc3bO1FUG84mP6mioQLy3mG7abpBQBCedRIw4NlOcTwBAGMRZ6oiEcsyvAe-v-WaRWHKuTKKDPZYtfLdEoZScj9jEwaFzbY1-A7YCuqgYLpo67CUhBBYbx34Nsr3alx9bg5R2gDxbdYNY5zC_NHjo8jAbSOFOLqRJokabLLbpBByIEJxnf70A9Omz2HwxrummnPjQ1kC27WjndPP5GXlnMoVdyo2tLr9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84b7cdbcf7.mp4?token=LVjQEf4z-5lmmXyJ_agt1VgoviOceOGko8D5xWj4wEb6JpJxIlEKaODxByKktYznmyn5BBJbD2Mq8Zl5h7dgSyOM8EWk93WzzEMqHNdNSgS6yLJa1Egrooc3bO1FUG84mP6mioQLy3mG7abpBQBCedRIw4NlOcTwBAGMRZ6oiEcsyvAe-v-WaRWHKuTKKDPZYtfLdEoZScj9jEwaFzbY1-A7YCuqgYLpo67CUhBBYbx34Nsr3alx9bg5R2gDxbdYNY5zC_NHjo8jAbSOFOLqRJokabLLbpBByIEJxnf70A9Omz2HwxrummnPjQ1kC27WjndPP5GXlnMoVdyo2tLr9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضدانقلاب این‌بار یک «پل چوبی» را دستاویز دروغ‌هایش کرد
🔹
برخی رسانه‌های ضدانقلاب با انتشار ویدیویی از وضعیت نامطلوب یک پل چوبی در روستای ساتره بخش مرزن‌آباد چالوس ادعا کردند که این پل تنها مسیر ارتباطی اهالی روستا با مناطق اطراف است و وضعیت نامناسب آن دسترسی ساکنان را مختل کرده است.
🔸
مسئولان محلی ادعاهای مطرح‌شده پس از انتشار ویدیویی از پل چوبی را رد کردند و تأکید کردند که این پل تنها مسیر ارتباطی ساکنان روستا نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/458246" target="_blank">📅 23:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458245">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049564136a.mp4?token=PqlR4w6ab-JujANuIk707sZB9WLXWtL8ba5hdt1jh5sE00JniTsvBnFMpcX_NHxfZzr5oi2mUgY5myRk9rRAc-3agrt5ZLmYq2TARopU7AHlERzR4NOzDwQYow4RcuHalvrob_jXwrxO8cvTqhctHpbwsqTyXVzMLuMZ2Bvr_g4b95q23roF83gWpSLTeajkYHDsdvQw7xFDC2YDptQsbjmyf0FvLbja9u-8-WFe4JrbNrhBYaEM0-dSdDFwjf_-Wip-9qtHLehz8Dohk8NZGWEYgP-N3cCuPtCtbeYICAZfjcZPbjBpSo609Bs3woPL8l7VzOA9qnjRrKLiUN1ebw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049564136a.mp4?token=PqlR4w6ab-JujANuIk707sZB9WLXWtL8ba5hdt1jh5sE00JniTsvBnFMpcX_NHxfZzr5oi2mUgY5myRk9rRAc-3agrt5ZLmYq2TARopU7AHlERzR4NOzDwQYow4RcuHalvrob_jXwrxO8cvTqhctHpbwsqTyXVzMLuMZ2Bvr_g4b95q23roF83gWpSLTeajkYHDsdvQw7xFDC2YDptQsbjmyf0FvLbja9u-8-WFe4JrbNrhBYaEM0-dSdDFwjf_-Wip-9qtHLehz8Dohk8NZGWEYgP-N3cCuPtCtbeYICAZfjcZPbjBpSo609Bs3woPL8l7VzOA9qnjRrKLiUN1ebw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌آبادی: مبلغ قبض برق ۷۵ درصد مردم اندازۀ قیمت یک پیتزا هم نیست
🔹
ما از ۸۷۶۰ ساعت سال فقط حدود ۱۰۰ ساعت کسری داریم.
🔹
هر کسی بخواهد برق او قطع نشود می‌تواند از بورس انرژی برق خریداری کند. @Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/458245" target="_blank">📅 23:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458244">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235d2387c4.mp4?token=SXUMON1RXG0cbDLeWL9ADBV1oiZajHg6digmiCcLmbjYMQevupJ2s1-N6ksNyVPQA_7zzAzMywTvqG373xxl1p7WmWn91l8e9pKno8Q4q440kZLjTHaxgxqq_qicqCksUuZv_TtbADUV9JXu6BspYBWDX08yteCY8YTznlU0-nY7y_6XOR6AkhR244S_gLYw5ApzADu_L9JjN0cD-a8wo0dm8xt9G2PV3IalWdqpoXcuapaeih4rzAlfI6e80G-viifFXoFDI9bkhZfEnorSqL-OWl1aIU8avqj9EpNyz5eppCu6mC4_R5BBpoHaZ0kxT5oejDEKbeQ_DKdUILcIdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235d2387c4.mp4?token=SXUMON1RXG0cbDLeWL9ADBV1oiZajHg6digmiCcLmbjYMQevupJ2s1-N6ksNyVPQA_7zzAzMywTvqG373xxl1p7WmWn91l8e9pKno8Q4q440kZLjTHaxgxqq_qicqCksUuZv_TtbADUV9JXu6BspYBWDX08yteCY8YTznlU0-nY7y_6XOR6AkhR244S_gLYw5ApzADu_L9JjN0cD-a8wo0dm8xt9G2PV3IalWdqpoXcuapaeih4rzAlfI6e80G-viifFXoFDI9bkhZfEnorSqL-OWl1aIU8avqj9EpNyz5eppCu6mC4_R5BBpoHaZ0kxT5oejDEKbeQ_DKdUILcIdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: روی آنتن زنده از مردم خواستم به‌خاطر استان‌های جنوبی صرفه‌جویی کنند؛ ناگهان ۲ هزار مگاوات از بار شبکه کم شد
🔹
من همان‌جا گفتم پای این مردم را باید بوسید؛البته از مردم ایران همین هم توقع می‌رود. @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/458244" target="_blank">📅 22:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458243">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E02-99X5_aYMCojqssAMYZpbF6ckkIJN9puMaWEUUe3Wx8fNr5PNLeujFG0UNV_9o9G-xare-PcCHgiIrEanSVV61k6xD_newpUgAZyctUGhbVLF27XiLGOMoL0HO-zs9A7tue9dck_7O9VP83Lh2twnqAWFLe3_f-DiXB51vWSW7wnNBfhj21DpD4i2KPXmH2r8chD8dLJ4aTom8afTUb0yv3DITqvUSp0TIM_nyRrhKr2BAOXY4YoFc8ExY-r1zNnmQsapbZaQPGryD0PzmWhjKIL_n9xX5uIXdK2bT1fpn8jnzW_ryIU3iqW0LHg1K4pYCH0CaJo5kNJiv7PVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: با دیپلماسی با همسایگانمان تعهد به صلح را دنبال می‌کنیم
🔹
وزیر خارجه پس‌از دیدار با مقامات پاکستان و عمان: تعهد ایران به صلح و ثبات، همراه با دیپلماسی استوار و مستمر با همسایگانمان دنبال می‌شود.
🔹
در گفت‌وگو‌ با میهمانان پاکستانی و عمانی، بر راه‌حل‌های منطقه‌ای تأکید شد.
🔹
چهارچوب پیشنهادی برای ایجاد یک کریدور جدید، مین‌روبی مشترک و مدیریت آتی تنگه هرمز، نمونه‌ای روشن از این رویکرد است.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/458243" target="_blank">📅 22:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458242">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkFq4FYcRU7GGda3mKhdlffL9xwEoDVu5ZX_u0wqBb0eOlAZcKU_Ug2F8gWsNxwduCWuC9xc0f1mSXzOs0Rzlu99Hf_2FlOuN4z83UlLPG8XLMu-Qs16nGpBdhlXbXgDxOGtVsidl9NAOZnqNM51xExuRv1OUA1LFuMYhBGlb2FqzCDuBDiyqj1bwv-Hafpd4e31_RotrnYyGLmVG-m280egzHRm--iLSMpASW_1RtUeCDJPvYKsgzWUNKnp-05fovj45IvKvEFZTrPRI0U4DjXl-AanwwkX5m_A4zjnFNwlvSY_oODzAKsxDN9gqEsCOhPIKKBRGFOO4D2kC6uAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف به بسنت: نمایش مضحکت «روز پیروزی» نبود، «روز دلقک» بود!
🔹
وزیر خزانه‌داری آمریکا که ادعا کرده بود تحریم‌های جدید علیه ایران مانند «عملیات نورماندی (D-Day)» کوبنده و سرنوشت‌ساز خواهد بود، در نشست خبری دیروز به سؤال خبرنگار درباره توخالی‌بودن این ادعا پاسخ داد: مگر من می‌خواهم اقتصاد جهان را منفجر کنم؟!
🔹
قالیباف در واکنش به این سخنان نوشت: این برنامه اصلاً شبیه عملیات نورماندی نبود؛ یک استندآپ مضحک در کلاب شبانه بود که در آن حتی دیالوگ‌های طنز خودت را هم فراموش کردی!
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/458242" target="_blank">📅 22:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458241">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ac54f50d.mp4?token=smBLnfiZAfxRtM9htzKV7G00WaiOGaS197upP-DIku2shi628BwIXw9zkmxEQOtH8nw8uyTlFSwkNdN5lfYVAT4X9FbSODLxYP8UOBZPG643SzhDmB2cD6tBM-BN5roC3SdMcn2NqD_165fHY3P11msbgJI9NR9cmMAksCuQw-bWvdNamQcEPI5UDCvpRoGMGowTaW-n0xWl8d8bqkkxtB_t0XHPCK-3aihirc7vo955K6tWJWZ6dfZkIx17hH7wwZjWo4ImNcGEPRBwR21-KwOP7DbMTq1klm2kfE9STfJAJndYi2i0hhbgu7Nmy7nO8NziU70FCIsYTjK67OOwtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ac54f50d.mp4?token=smBLnfiZAfxRtM9htzKV7G00WaiOGaS197upP-DIku2shi628BwIXw9zkmxEQOtH8nw8uyTlFSwkNdN5lfYVAT4X9FbSODLxYP8UOBZPG643SzhDmB2cD6tBM-BN5roC3SdMcn2NqD_165fHY3P11msbgJI9NR9cmMAksCuQw-bWvdNamQcEPI5UDCvpRoGMGowTaW-n0xWl8d8bqkkxtB_t0XHPCK-3aihirc7vo955K6tWJWZ6dfZkIx17hH7wwZjWo4ImNcGEPRBwR21-KwOP7DbMTq1klm2kfE9STfJAJndYi2i0hhbgu7Nmy7nO8NziU70FCIsYTjK67OOwtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: ما آن‌قدر نیروگاه داریم که حتی اگر دشمن تمام توان خود را به کار بگیرد، نمی‌تواند همهٔ نیروگاه‌های ما را هدف قرار دهد.  @Frasna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/458241" target="_blank">📅 22:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458240">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-KO7IVUYXeJik-nusu-TeUuf9z-EBwyAcYpLLwECUOqf2k7x9ByJZf5GGPuMiMM0Jzx8qEwvdOdHdbJgX1XVbw9ew5qG6pBzPpb-T1pNgK9tOYrHaVPWb7aXpMx-9-Wets4WcHnNpMf7Q-CgmPczfza0ALax4mSDVo4ssyhkxJFgleWEp0G3oiSBESntVaIXj0JzWiq5axGbWXu0kb4dxpJYRbXpv2mWbh5JYm65olqD7dTFZt_dhjam9akS7C0Irs5nSMkL8dkmW_xflrz1cCfTO0km8LuBQcvMXb7BznfIVGB4aD9OOW-CcLKwdsiEHMf9wm-bCWIstsh4-03vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که دابسمش‌های سمی سر کودکان می‌آورد
🔹
درحال گشت‌وگذار در شبکه‌های اجتماعی هستیم که ویدئوی پربازدیدی توجه ما را جلب می‌کند
🔹
دختربچه‌ای خردسال، با ژست‌هایی کاملاً زنانه درحال اجرای یک دابسمش با آهنگی است که محتوای آن سراسر خیانت، روابط پنهانی و مفاهیم سخیف جنسی است.
🔹
شاید در نگاه اول، این فقط یک بازی کودکانه برای جذب دنبال‌کننده به نظر برسد؛ اما واقعیت تلخ این است که تکرار این کلمات و حرکات، بذر بی‌حیایی و بی‌عفتی را در ناخودآگاه کودک می‌کارد.
🔹
وقتی یک مفهوم سخیف برای دختربچه ما عادی شد، او در دوران نوجوانی به‌راحتی طعمه آسیب‌های اجتماعی و سوءاستفاده‌های عاطفی می‌شود.
🔸
برای اینکه فرزندتان را از این باتلاق مجازی بیرون بکشید و اصالت و وقار را به او هدیه دهید، این تکنیک سه‌مرحله‌ای را با هوشمندی به کار ببندید:
🔹
هرگز گوشی موبایل و اینترنت آزاد را به‌عنوان پرستار کودک رها نکنید. شما باید خلبان اصلی پرواز فرزندتان در فضای مجازی باشید.
🔹
اگر روزی متوجه شدید فرزندتان در حال زمزمه‌کردن یک آهنگ سخیف یا اجرای یک رفتار ناهنجار است، هرگز فریاد نکشید و او را با کلماتی مثل «بی‌حیا» برچسب نزنید.
🔹
در این شرایط، یک انسان مقتدر غرور بی‌جا را کنار می‌گذارد و پیش از آنکه کودک به سن نوجوانی و بحران‌های حاد برسد، از یک روان‌شناس کودک و مشاور امین کمک می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/458240" target="_blank">📅 22:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458239">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3cc1597a2.mp4?token=M2YWoBny11MfBGPrUWmwTSUFXj0VBjlRdlcQzZGgaOi65MJfJ1VgshglNwFwAz-cDXPpMDSM99IdZypzMe4fOP1w99snIxgS2sKZjXJehWIe7EiCSW0rlHHDOEDF0YS1QCryFX2MLFIeHMU9s34Uz_-sTlNB9svaOUS5fcS9q6ZQYAMmbXh9zhorSJ04nXXg39KL9v7cRZjqKV7lAKrcPAlsLDqMDbCm3Kr1Rdh37kv7SSyOjDmH-GioBMbVXbmJio82AWUPeEQjPP7oVGNSv_Sw11om3Ey_QwjPZ_t6F7x_O4O-qeSSPExf1cDG-mELz5hvx4qhHRqNrLXKgVy3cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3cc1597a2.mp4?token=M2YWoBny11MfBGPrUWmwTSUFXj0VBjlRdlcQzZGgaOi65MJfJ1VgshglNwFwAz-cDXPpMDSM99IdZypzMe4fOP1w99snIxgS2sKZjXJehWIe7EiCSW0rlHHDOEDF0YS1QCryFX2MLFIeHMU9s34Uz_-sTlNB9svaOUS5fcS9q6ZQYAMmbXh9zhorSJ04nXXg39KL9v7cRZjqKV7lAKrcPAlsLDqMDbCm3Kr1Rdh37kv7SSyOjDmH-GioBMbVXbmJio82AWUPeEQjPP7oVGNSv_Sw11om3Ey_QwjPZ_t6F7x_O4O-qeSSPExf1cDG-mELz5hvx4qhHRqNrLXKgVy3cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: یکی از هنرمندان در زمان جنگ به ما گفت می‌خواهم به نیروگاه بروم و آنجا ساز بزنم
🔹
زمانی که جنگنده‌ها وارد آسمان کشور شدند، با زحمت توانستند او را از نیروگاه خارج کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/458239" target="_blank">📅 22:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458238">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d787a763.mp4?token=GTIK4nAhrsR2JnP-Rwwi5M9Q5VjPtBGwq3SnRsgkwpa4z2znceEq1YX9iwz00rutaUg9Hymqj2zdLy-3i5YYWZMdRkStVLMYk5xdjvkl6jEJgp3C1yZy07NsVO5Vb12q9wISjrfwXpYLvdinLEhWZZxGROx9VmufuPaw8j84gr9rrccTPGk3-DAK53tBMnww0IUl91uBPUpXDlkXTye3W7HvSD8VPMqHd5EslKvCXHwyzr24T_fZt1uQwExpgwjD6mwIRxkce--WCbaE-a2uR5aFLiluRFYVP38sq7zVXBJRZzQxt8dYRHTgvM8qo4Acw09ykMKCmPmxqBQIRacXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d787a763.mp4?token=GTIK4nAhrsR2JnP-Rwwi5M9Q5VjPtBGwq3SnRsgkwpa4z2znceEq1YX9iwz00rutaUg9Hymqj2zdLy-3i5YYWZMdRkStVLMYk5xdjvkl6jEJgp3C1yZy07NsVO5Vb12q9wISjrfwXpYLvdinLEhWZZxGROx9VmufuPaw8j84gr9rrccTPGk3-DAK53tBMnww0IUl91uBPUpXDlkXTye3W7HvSD8VPMqHd5EslKvCXHwyzr24T_fZt1uQwExpgwjD6mwIRxkce--WCbaE-a2uR5aFLiluRFYVP38sq7zVXBJRZzQxt8dYRHTgvM8qo4Acw09ykMKCmPmxqBQIRacXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: یکی از هنرمندان در زمان جنگ به ما گفت می‌خواهم به نیروگاه بروم و آنجا ساز بزنم
🔹
زمانی که جنگنده‌ها وارد آسمان کشور شدند، با زحمت توانستند او را از نیروگاه خارج کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/458238" target="_blank">📅 22:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458237">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febdb381d4.mp4?token=XfnZsXZapcAqYcWu7rVWQRbzDJwTHRo4RCY7TStp2mz-TLbgsm8ZkLJSYgbg0-uAFkhtoSAySJVl08ExHgxdLrXP56qf80sVqW9NVmoomCJIzYCpeKiZ5gof3lAgdyv5sWP8ryOZMV1LCqXhfidXZqW4nqVYhvZ6-AeizZVf9AIevOHteyq0pg2fIRqZGtOT1JhWmSCL6ZJ8JF-Lmdhq2l0Sbk5i9RpgqI4Tb5qAsDSC-om2pSEOrfVEzCXgXI7bNBQ75DQ5jG5ypX3YFxvYWDZUElgiMRAlyNe7OIGBIeFgjuabkF9sP6XO5wwjzK5NysE3g_qcQjmNsjoewxLjfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febdb381d4.mp4?token=XfnZsXZapcAqYcWu7rVWQRbzDJwTHRo4RCY7TStp2mz-TLbgsm8ZkLJSYgbg0-uAFkhtoSAySJVl08ExHgxdLrXP56qf80sVqW9NVmoomCJIzYCpeKiZ5gof3lAgdyv5sWP8ryOZMV1LCqXhfidXZqW4nqVYhvZ6-AeizZVf9AIevOHteyq0pg2fIRqZGtOT1JhWmSCL6ZJ8JF-Lmdhq2l0Sbk5i9RpgqI4Tb5qAsDSC-om2pSEOrfVEzCXgXI7bNBQ75DQ5jG5ypX3YFxvYWDZUElgiMRAlyNe7OIGBIeFgjuabkF9sP6XO5wwjzK5NysE3g_qcQjmNsjoewxLjfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۸ شب حضور؛ مردم همچنان پای عهد خود ایستاده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/458237" target="_blank">📅 22:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458236">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a53bd01c80.mp4?token=mIamlku-vSUo4T7EfFThPt3z9aFY6uwUWMuuLkx343e9yoPj_FkOcfhdmS1FYgaB-x6P36kfoMQMtRdMTfxevs0laVA8mqmsqqST0S8aMf2DaB-QWeQGS5pWz7_As46dFAxh23SuIKqbDsSg9SDhYSryKCs8iyJjipz3r-FSiHofOre3L0G2n2VnouGHecrOkaDwllnhd9ALhP_sHP_QoS_zgQk2Lldaz6kyE07U_anYtS90AobqTdQ8-t4WzId1igSxtONYV16csl1dL6-rK4-UQry6KNL1xbKdvP6rNUcmbtOm8u5gRRYRgdIYbk5-hZflfkV7lDCKiUyEzLCAdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a53bd01c80.mp4?token=mIamlku-vSUo4T7EfFThPt3z9aFY6uwUWMuuLkx343e9yoPj_FkOcfhdmS1FYgaB-x6P36kfoMQMtRdMTfxevs0laVA8mqmsqqST0S8aMf2DaB-QWeQGS5pWz7_As46dFAxh23SuIKqbDsSg9SDhYSryKCs8iyJjipz3r-FSiHofOre3L0G2n2VnouGHecrOkaDwllnhd9ALhP_sHP_QoS_zgQk2Lldaz6kyE07U_anYtS90AobqTdQ8-t4WzId1igSxtONYV16csl1dL6-rK4-UQry6KNL1xbKdvP6rNUcmbtOm8u5gRRYRgdIYbk5-hZflfkV7lDCKiUyEzLCAdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم مراغه ایستاده در سنگر خیابان در ۱۷۸ شب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/458236" target="_blank">📅 22:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458235">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5327c0708f.mp4?token=ewg_a1ST8zPPvUup6BZwy50P9WzdvFAqhnStjrdPUd56Zt_6GserARiwHAiPpriZG0b2hRmM8zukLQ9-2vvqcS6owqF5FvLBbKaoo80lexxNu08d7D7cXT7dxTuU4nghhae-RFq7Y1SBe-83B-BHBBAwqp3y7dsrFKQwVfSb6jFu1sz1Q0DOLPRULNbV3LWrj5p3RMt90st-a0d1cBaYDg3L6DwFK5STSFhg5qKUjeeYjX9UayKDjAmNmELczUEh_e7N1L-HWkKbLScsDiWxb4BB8v1x2_V-YBz3sjhNSzaOhTMSl77WMf-jrwEGXmLwsDzaf7_h5u38-9rd3BR28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5327c0708f.mp4?token=ewg_a1ST8zPPvUup6BZwy50P9WzdvFAqhnStjrdPUd56Zt_6GserARiwHAiPpriZG0b2hRmM8zukLQ9-2vvqcS6owqF5FvLBbKaoo80lexxNu08d7D7cXT7dxTuU4nghhae-RFq7Y1SBe-83B-BHBBAwqp3y7dsrFKQwVfSb6jFu1sz1Q0DOLPRULNbV3LWrj5p3RMt90st-a0d1cBaYDg3L6DwFK5STSFhg5qKUjeeYjX9UayKDjAmNmELczUEh_e7N1L-HWkKbLScsDiWxb4BB8v1x2_V-YBz3sjhNSzaOhTMSl77WMf-jrwEGXmLwsDzaf7_h5u38-9rd3BR28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی حرف خیابان‌ها در شب ۱۷۸، یک کلام شد؛ «انتقام»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/458235" target="_blank">📅 22:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458234">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
ما جمعی از متقاضیان پروژه ۲۵۶ واحدی نهضت ملی مسکن در صومعه‌سرا (گیلان) هستیم که از سال ۱۳۹۹ ثبت‌نام کرده و هر نفر ۳۶۰ میلیون تومان در بانک مسکن واریز کرده‌ایم. مسئول پروژه اداره کل راه و شهرسازی گیلان و پیمانکار شرکت پایاسازه پاسارگاد است. با وجود پیگیری‌های فراوان و گزارش به نهادهای نظارتی و شورای تأمین شهرستان، هیچ اقدام مؤثری انجام نشده و زمان تحویل همچنان نامشخص است. متقاضیان عمدتاً مستأجر و از قشر ضعیف هستند. تا چه زمانی باید منتظر بمانیم؟ از شما تقاضای ورود و پیگیری جهت احقاق حقوق عامه را داریم.
🔸
برای ثبت‌نام فرزندم در پایه هفتم به آموزش و پرورش منطقه ۴ مراجعه کردم، اما امکان ثبت‌نام فرزند من و بسیاری از والدین در این پایه میسر نبود. مسئول مربوطه اعلام کرد که این پایه بیش از ۱۰۰۰ نفر اضافه شده و به دلیل اینکه پیش‌بینی این تعداد دانش‌آموز را نداشته‌اند، به مشکل خورده‌اند و ثبت‌نام فرزند من بلاتکلیف مانده است. لطفاً به وزیر انتقال دهید. ما باید چه کنیم؟
🔹
از بندرعباس پیام می‌دهم. بنزین آزاد در جایگاه‌ها نمی‌دهند. این ۱۲۰ لیتری که گذاشته‌اند همان چند روز اول تمام شد. سرویس حمل‌ونقل عمومی هم به اندازه کافی در سطح شهر و همه خیابان‌ها وجود ندارد. خیلی از مسیرها تاکسی ندارد و مسیرهای طولانی را باید طی کنیم. مجبوریم از خودرو شخصی استفاده کنیم. لطفاً این پیام را هر طور می‌توانید پخش کنید.
🔸
ما کارگران مستأجر باید دردمان را به کی بگوییم؟ کی مسئول این اوضاع آشفته مسکن است؟ من با دو تا بچه چه کار  کنم؟ شما را به خدا اگر از دستتان برمی‌آید، صدای ما قشر مظلوم جامعه را به گوش بالادستی‌ها برسانید، شاید فکری به حال این وضعیت بکنند.
🔹
چرا وزارت صمت این شرکت‌های خودرویی را به حال خود رها کرده تا هر کلاهبرداری که دوست دارند انجام دهند؟ مهرماه ۱۴۰۳ از فردا موتور یک خودروی SX5 پیش‌خرید کردم و مبلغ ۵۰۰ میلیون تومان پرداخت کردم. طبق قرارداد می‌بایست سه‌ماهه خودرو را تحویل می‌دادند. الان دو سال از آن تاریخ گذشته و هر بار یک دروغ جدید می‌گویند. آخرین حرفشان این است که جنگ شده و اصلاً این خودرو را دیگر نداریم؛ بعداً جایگزین و شرایط خریدش را اعلام می‌کنیم.
🔸
در خصوص کسب‌وکار اتباع در کشور پیگیری شود. چرا آن‌ها بدون مدرک می‌توانند کسب‌وکار راه بیندازند اما یک ایرانی باید اسیر کلی قانون دست‌وپاگیر باشد؟
🔹
لطف می‌کنید از شرکت فردا موتورز که بالای ۱۰ هزار ثبت‌نامی خودرو و معوقات بالای دو سال دارد، خبر انتقادی بگذارید تا به گوش مسئولین کشوری برسد و به داد مشتریان بیچاره برسند.
🔸
از خواف مشهد پیام می‌دهیم. حدود ۵۰۰۰ نفر برای زمین‌های امتیازی و ساخت مسکن ثبت‌نام کرده‌اند، اما هنوز در بلاتکلیفی به سر می‌برند؛ الان سال چهارم بلاتکلیفی است.
🔹
من از فروشگاه زنجیره‌ای خرید کالابرگ انجام دادم. همان‌طور که می‌دانید باید ۵ هزار تومان (به‌صورت یکجا) کسر شود، اما یکی از شعبات یک‌بار ۲ هزار تومان و یک‌بار ۳ هزار تومان از من کسر کرد. این موضوع باعث کاهش شفافیت می‌شود و کار اشتباهی است.
🔸
بنده ۶ ماه است که برای نقل‌وانتقال مسکن مهر فاز ۸ اقدام کرده‌ام. همه مراحل از طریق عمران شهر پردیس انجام شده و به مرحله فرم ج رسیده‌ام. ۶ ماه است که در سامانه املاک و مستغلات قطعه می‌خوریم و نمی‌توانیم استعلام بگیریم. می‌گویند شما نباید مبلغی پرداخت کنید چون ملکی به نامتان نیست، اما بعد می‌گویند ۴۰ میلیون تومان پرداخت کنید تا کارتان انجام شود.
صدایمان باشید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/458234" target="_blank">📅 22:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458233">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d5b024e0.mp4?token=TNbOudXzp1v5VtBrQhTuKEhXcRuhKxt2vCXmxW11FV3-QZ-oBnuaVyoIvc43jCtSpOanexOecf4EdthuxWRLICO11A060NzoI0udAs8-fzdEeQH637RHVfSvluub-tslp8JoCbGaK93HJXyHt1d1TIECLwe_psBqpfUpR7ySuO9iqVqcoZUBcfG4ndThKyuZO-Oa-e7a-HtRsb5Km5I5Vo_wqBp7pE069hCHnlhkoREwc-qrKtZOgjVc7i5LanZd9_w-lum9MXl9-9d-CCF7jr6FTazTK-75ig2JSvc7Uud6FwPYwijBSIVSL7yKnvS5xtMBKttl8lUFQOaEr9AIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d5b024e0.mp4?token=TNbOudXzp1v5VtBrQhTuKEhXcRuhKxt2vCXmxW11FV3-QZ-oBnuaVyoIvc43jCtSpOanexOecf4EdthuxWRLICO11A060NzoI0udAs8-fzdEeQH637RHVfSvluub-tslp8JoCbGaK93HJXyHt1d1TIECLwe_psBqpfUpR7ySuO9iqVqcoZUBcfG4ndThKyuZO-Oa-e7a-HtRsb5Km5I5Vo_wqBp7pE069hCHnlhkoREwc-qrKtZOgjVc7i5LanZd9_w-lum9MXl9-9d-CCF7jr6FTazTK-75ig2JSvc7Uud6FwPYwijBSIVSL7yKnvS5xtMBKttl8lUFQOaEr9AIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزه مقاومت: حملات رژیم صهیونیستی به جنوب لبنان و منطقه علی‌الطاهر با شدت ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/458233" target="_blank">📅 22:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458232">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f2bf22e1b.mp4?token=uDnDTWITDsNMEhiB8TMZJZfqdJlPVgOs0ZdhBFLdtuUDnRLWsBeG_faW4aunCUoh_BWrsIhTLu6FPbGdWu_6p24sRLrjqCkyBT-7PILkXmnNQ4BOsyzydsDAe3xggC5E3TwZdqRAIpsT5TJmt9NKTy8kf72Dsd00w4I3_NKxf5R6q_BpJwxkgZcedupYUY0PMLbuBpDIoGeh2RbQHoJrpnolh-Nfo95LHvqD9oEM7HFdxdkA7lZKXifYv_n3qNik7I15xDA5uq5j2OkFnHPyMrHNABhR6Z2vIsnHc1-j6HebALxHYUIuYwPsY47xQPoczEn5QMlhlgtrUcKeq_IsDHqHBBHXxtAWtn7twSOWOyzq_UnrHy7XnP6jBli0bwv46VMTE9gT_eHqpYzQtMBzqz011QbnCGctbmYBpft6enkzxbI45P_kzMBHNEmd-r6rSiP8IDgj_CE7nJrTzRP05g-hj8uySI4WG94pITAl38cwCfhKFen1Dmp7oD-Z4A3azYPglrtr0OW8_OwzmnZ7xrILgRtYtZ9ORmeP0gIwNwKfVlU-gdoXP_6xXlNSQF4Q25adLsYDv-F300lii7Zi5q2Ul48ppM0CZnaUw2I7HgrOUSTDWPrXrhMXt1OECWhedmTEV74ddemrnaMK77uJiZhzuFs_OjyWE8cNPRaMn2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f2bf22e1b.mp4?token=uDnDTWITDsNMEhiB8TMZJZfqdJlPVgOs0ZdhBFLdtuUDnRLWsBeG_faW4aunCUoh_BWrsIhTLu6FPbGdWu_6p24sRLrjqCkyBT-7PILkXmnNQ4BOsyzydsDAe3xggC5E3TwZdqRAIpsT5TJmt9NKTy8kf72Dsd00w4I3_NKxf5R6q_BpJwxkgZcedupYUY0PMLbuBpDIoGeh2RbQHoJrpnolh-Nfo95LHvqD9oEM7HFdxdkA7lZKXifYv_n3qNik7I15xDA5uq5j2OkFnHPyMrHNABhR6Z2vIsnHc1-j6HebALxHYUIuYwPsY47xQPoczEn5QMlhlgtrUcKeq_IsDHqHBBHXxtAWtn7twSOWOyzq_UnrHy7XnP6jBli0bwv46VMTE9gT_eHqpYzQtMBzqz011QbnCGctbmYBpft6enkzxbI45P_kzMBHNEmd-r6rSiP8IDgj_CE7nJrTzRP05g-hj8uySI4WG94pITAl38cwCfhKFen1Dmp7oD-Z4A3azYPglrtr0OW8_OwzmnZ7xrILgRtYtZ9ORmeP0gIwNwKfVlU-gdoXP_6xXlNSQF4Q25adLsYDv-F300lii7Zi5q2Ul48ppM0CZnaUw2I7HgrOUSTDWPrXrhMXt1OECWhedmTEV74ddemrnaMK77uJiZhzuFs_OjyWE8cNPRaMn2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح‌هایی که در دومین روز هفتۀ دولت افتتاح شد
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/458232" target="_blank">📅 21:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458231">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIfTY8zEsC-g9xSPXRy78oH1ntZkzdOLDkUnhimnXc5pbldZhhifi2JxFa_yflb-4OopEzo7v3dvihUEgI7pRKXfSG2eWy3QVtzjgEdPfdxW9SCRUjfOsHU9DlxpFiQ7gjOtdcRpgU0oz0nWT5IxPeeaRUVgVdUtqerZ_d4KHXpPlcWJiUF8oGfncxH1AYP2DC4gQGj6PbPMwzkFZ5NwWIdJlOIK3w8Ce-oTeo_vIaB5jJ97onTYfdW-Eke_hd1wnAWDgENS2D2dpRpaFfupnt8UcNoy32Mg2pJCCl_nueZ8eEGAFNO7Ho8QCEA2mR6YHw9k8QkggZltc5RV5kYCqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف به جعل خبر ۱۶ ساله علیه ایران!
🔹
خبرنگار سابق گاردین در پیامی با افشاگری دربارهٔ انتشار اخبار جعلی در این روزنامه اعلام کرد مطلبی که ۱۶ سال پیش دربارهٔ حکم سنگسار یک زن ایرانی منتشر کرده بود کاملا جعلی و ساختگی بوده است.
🔹
روزنامهٔ گاردين در سال ۲۰۱۰ مدعی مصاحبهٔ اختصاصی با سکينه محمدی آشتیانی شد و اعلام کرد این زن به سنگسار محکوم شده است. مصاحبه ای بحث برانگیز که در رسانه‌های خارجی بازنشر شد.
🔹
حالا ۱۶ سال پس از انتشار، سعید کمالی دهقان نویسندهٔ این مقاله بابت انتشار مصاحبهٔ دروغین با یک زن ایرانی از مخاطبان عذرخواهی کرد و نوشت : آن مصاحبه هرگز انجام نشد؛ من تمام آن مطلب را از خودم درآوردم. داستانی ساختگی و کاملاً کذب بود و من مسئولیت آن را می‌پذیرم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/458231" target="_blank">📅 21:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458230">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1mSh5CCnFSIhYSpPTnvuIWixNf1FTOG5C2l0ve9vESUbmhJEv64ldWc7bi3W1GT8cNQ2gxY-V-IPNyyfAtcSjJWMQl3bzswyGT7IQ4mmwXjO-UF2UUaTPrFC5RwdYJR9T_UkVYVKvsLNoXaAVOEve9bR0R2w9tZXpQe7Pf8PY_dXIxwpw-XT_xlNDci41ihM15l3tfQLY7y67j65UZBr2jUdc3yOF5f08somFyCVKGuGCbESWl5c8cwuIIC_svDPk_tV9NZbPBqaUbq-Nc11t4HHj3vkuGc76cdqymu0YmpX1oFKuptPv3ehcVoupzRVsMbXPLePKdvM2iYpnttTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«قسد» رسماً منحل و فرمانده آن مشاور الجولانی می‌شود
🔹
روزنامه القدس العربی گزارش داد که طبق توافق انحلال شبه نظامیان کُرد سوریه(قسد) رسما اعلام و مظلوم عبدی فرمانده این گروه به عنوان مشاور الجولانی تعیین خواهد شد.
🔸
فرمانده قسد دو روز پیش
گفته بود که این گروه تاسیسات نفتی تحت کنترل خود از جمله رمیلان، السویدیه و سایر مناطق را رسماً به دولت شورشیان سوری تحویل داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/458230" target="_blank">📅 21:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458229">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9LFSKb04Tla1arvLCfyeodKQ6no9bbeFKbQ0oblLFL_ha5bNffXc6swq1MfQhwJVWodlnzjcuzZwUycp6hhQ9gS_y3NNkcQ_Fk-jSffJCy4DVAxEYecThRwbC-STwgWZ01LjuMencusW83qD4DXcIeUsUJQxI-1IleApakRN6fmbbpdm5me1WUp9gg02rYzWoBVgAp71N5clYtR4XYDSCtC7s9mLcgPIoCK_BVBEATb8irR8QpDLucq1zfzmOxSueQQPo-xhsNFRyvAWgRTicb8vfr7I_GHfUZNKYCAPNqtgjyqrlW3_oRpWJdouL0qPHgw0phPP_Hsm6HoDontMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک به پرسپولیس در آستانۀ دربی
⚽️
اورونوف در دیدار تدارکاتی امروز پرسپولیس مقابل امیدهای این باشگاه بار دیگر دچار مصدومیت شد.
⚽️
هنوز میزان مصدومیت و مدت زمان دوری این بازیکن از میادین مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/458229" target="_blank">📅 21:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458228">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae424a74.mp4?token=C-JWvLW2RiM5yiaRJm8adbfjQb-n9m8otAEw4McmFnWBcIYdULTtZxfpJyV_GGr_Z7LkOXdEnxacp3zW_jeWY5uc8WFQUjgYK23Epwyub934d4c6HmWd9uF2TBYHx2ymWEkdTktSylqdGKIK-dIvony2nBJOXaTDYp0UhNze491WuIyg9oUbYXVucCT2t1xuUfbiDvkDr82HqG8XEkaDqg8EHCiC8dqeXA1ZVpQoW8I9kgmcwaPtF33UaVDYswUE8w0YAfG1cH8niFBC1gd-SONfvUcGkU--vGEZWecVRYxha7SwBSXPGuY0Be2Yf6EXgS0NxQ3ecoN8lCOuzqjPZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae424a74.mp4?token=C-JWvLW2RiM5yiaRJm8adbfjQb-n9m8otAEw4McmFnWBcIYdULTtZxfpJyV_GGr_Z7LkOXdEnxacp3zW_jeWY5uc8WFQUjgYK23Epwyub934d4c6HmWd9uF2TBYHx2ymWEkdTktSylqdGKIK-dIvony2nBJOXaTDYp0UhNze491WuIyg9oUbYXVucCT2t1xuUfbiDvkDr82HqG8XEkaDqg8EHCiC8dqeXA1ZVpQoW8I9kgmcwaPtF33UaVDYswUE8w0YAfG1cH8niFBC1gd-SONfvUcGkU--vGEZWecVRYxha7SwBSXPGuY0Be2Yf6EXgS0NxQ3ecoN8lCOuzqjPZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت ملی گاز: افراد سودجو با استفاده از انشعابات غیرمجاز، گاز را سرقت و از مولدهای اضطراری گازسوز برای تأمین برق دستگاه‌های استخراج رمزارز استفاده می‌کنند.
🔸
مردم در صورت مشاهده این موارد با شمارهٔ ۱۹۴ تماس بگیرند.
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/458228" target="_blank">📅 21:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458227">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwVexBQshduaXa9ORuQgTl6C2XLCpplHstW9_YLMMXHUU3q2aJAH8TFAXczCjaWkx8_fQk9xgmcc1qEDoz6lh-HaR3iuXAMgqmGU11AnJZuFEKYAG_WB4MTAsj8uGB992631ZO4l1N0CfAlmOul1Nbip9qdPxHgSYzsubgQ5YW30sbCEyif8X3omL0-0Q0kEIOZZyHUWai_RKG8y9PvWAHXEgu2CVAxFDcVM8tdtMZBYV2b6-hgXMmmwHUWEwPNJX-7GAhDYf2viUlx5QXCUyXPBjg1uemye4EbL7fY4npUBFPnb7PtIbrrpTq1p__6lRZFLDvMOU3eZWeB4uLeKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان از آمریکا درخواست وام کرد
🔹
پاکستان رسماً از وزارت خزانه‌داری آمریکا درخواست تسهیلات تثبیت ارزی به ارزش ۱۰ میلیارد دلار کرده که بزرگترین درخواست در تاریخ این کشور به شمار می‌آید.
🔹
این درخواست پس از نقش پاکستان در میانجیگری در مناقشه آمریکا و ایران، که روابط با دولت ترامپ را تقویت کرده است، مطرح می‌شود.
🔹
پاکستان در حال حاضر تقریباً ۱۲.۳ میلیارد دلار بدهی دوجانبه کوتاه‌مدت دارد که نیاز به بازپرداخت مداوم به عربستان، چین و کویت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/458227" target="_blank">📅 21:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458226">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djT681t2rwc9P1__i3q-3wnck39nFivGTCUAU-ymphANSr4YBQP8rLt45xVVcZtHBAngbTejjkc7LQ-PTOqrQ_VP6obG-HM3Jk4BwdBZJcAhm5FPy67opqpmY2KtUzLB4JBncb43Ejv0VIAJSHfNl307eO4AdhDOPJtVrWldwTeQIPIKhohshShcBb8OqA5LM9wP4sF6BWnmwzANCGMAJNnKakC0z5UlD2nZVPWbPlMT_4SzG63PVIPIybopbBkQMtbTfO4_3P31lfdvfaxxiw4beqwuJCUlgEE3PDAxWJl4HXj-yNkZLKnL4PfVrBxqwqwXjkvB1YxPieIyz8RuIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی در تیم ملی ماندگار شد
⚽️
دبیرکل فدراسیون فوتبال: به جمع‌بندی رسیده‌ایم که آقای قلعه‌نویی تا پایان جام ملت‌ها سرمربی تیم ملی باشد.
⚽️
انتظار داریم او تیم ملی را در جام ملت‌ها قهرمان یا فینالیست کند.
@Faresna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/458226" target="_blank">📅 21:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458225">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqtCHBSef1lKB1rDbSfl7CldOHFBRJ8dvHs0MtOw7XDD8rDzbzCY4LBn4aGCpoS3lOn4i96UCTUV1cdNWU2rxdvXYWGrLjbgW4_i5Gpjs2eHxKc1HsycBG1ilDWwjQmEinM-TgJ41inHK7qiUQJj_SNon-vtcGXCAjnl4ivyUhxk5c1AEcT9m9jtgKjXZFYvwNt7ngK8GfI-ETl1Ttu8v4zjmpDTQoCOFwCD5ISv0MRqvkZzFSaJ2-64Y1FOJJfPYHwtz7ujK0TqisvMq6h0rK8-uxrxCiIatTtP1ViSujJ0vDDW7DicDVj17AzalSCIjc0_HcZa0sES759Y2rck_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ماجرای استفاده از «شومیز» در یکی از مدارس تهران چه بود؟
🔹
انتشار خبر استفاده از «شومیز» به‌عنوان لباس فرم دانش‌آموزان یک مدرسه دخترانه در سعادت‌آباد از صبح امروز واکنش‌های گسترده در فضای مجازی به همراه داشته است.
🔹
پیگیری‌های خبرنگار آموزش‌وپرورش فارس نشان می‌دهد این ماجرا مربوط به مدرسهٔ ابتدایی دخترانه دولتی در منطقهٔ ۲ تهران است.
🔹
پارسا، مدیرکل آموزش‌وپرورش شهر تهران، تصاویر منتشرشده در فضای مجازی را غیرواقعی دانست و گفت این تصاویر ارتباطی با لباس فرم طراحی‌شده برای مدرسه ندارد.
🔹
تصاویر دریافتی فارس از آموزش‌وپرورش تهران نیز نشان می‌دهد لباس فرم طراحی‌شده برای دانش‌آموزان ۶ ساله کلاس اول در سال تحصیلی جدید از نظر اندازه تفاوتی با لباس فرم سال گذشته نداشته است. آموزش‌وپرورش تاکید دارد اندازه‌های ابلاغی در این لباس‌ها رعایت شده است.
🔹
یکی از اولیای دانش‌آموزان معتقد است اشتباه مدیر مدرسه برای استفاده لفظ «شومیز» به‌جای مانتو یا لباس فرم باعث ایجاد این جنجال شده است.
🔹
آموزش‌وپرورش تاکید کرده اول مهرماه بر لباس فرم این مدرسه نظارت دقیق خواهد کرد و مدیر مدرسه هم به‌دلیل سهل‌انگاری به هیئت رسیدگی به تخلفات اداری آموزش‌وپرورش معرفی شده است.
🔹
مدبرنژاد، مدیرکل انجمن اولیا و مربیان، نیز گفت یکی از سیاست‌های اصلی وزارت آموزش‌وپرورش برای سال تحصیلی ۱۴۰۶-۱۴۰۵ این است که لباس فرم مدارس تا ۳ سال تغییر نکند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/458225" target="_blank">📅 21:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458224">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df681d69b0.mp4?token=gQLNeaiq9EILL-bIs2vhBgCG2VxsccyIylwUrjqqiaY1jdwkRTFyN49dQ1JPKbrHhdF0JG9Bt-J2wgqxhk1fxM16QegBfRZtE6LZkOteYLHTxuSW21TUtqHNXkl4dHAz46B9HxRHDZHpcZtsYE62WRnH_7DP5sr6nLy9vBPAEBy04gliokH89YrBg5LIpTHNduLrQTNq3DVOnq8unwnAn0RXlY_MiDrimElgveq1LPJ0KYWGgRpkwf-pA_tHDJN7K5Pvl6CNx-AEGldLApp485HglY8AGC7o3lIg3-Wi-GFamjwwFt-Zb3ySDWzkquvN5aLs24i9EF5j-yPLZvf-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df681d69b0.mp4?token=gQLNeaiq9EILL-bIs2vhBgCG2VxsccyIylwUrjqqiaY1jdwkRTFyN49dQ1JPKbrHhdF0JG9Bt-J2wgqxhk1fxM16QegBfRZtE6LZkOteYLHTxuSW21TUtqHNXkl4dHAz46B9HxRHDZHpcZtsYE62WRnH_7DP5sr6nLy9vBPAEBy04gliokH89YrBg5LIpTHNduLrQTNq3DVOnq8unwnAn0RXlY_MiDrimElgveq1LPJ0KYWGgRpkwf-pA_tHDJN7K5Pvl6CNx-AEGldLApp485HglY8AGC7o3lIg3-Wi-GFamjwwFt-Zb3ySDWzkquvN5aLs24i9EF5j-yPLZvf-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افزایش عرضهٔ بانک مرکزی، نرخ ارز را کاهشی کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/458224" target="_blank">📅 21:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458223">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f161b189f6.mp4?token=IMJSwujgAe3YvgpenBn_cBv-PiiGLhHHf9QQYiRzQM1UwLoVxfeuEHYm62_fq4ahMz-7JRAcQeK-YOrpJAI7-chi776UjCo--YyTBAg2buX4qbY9YLbopBoXMSTtzjk4EBTsgFBimv41o0e5OR5bG7NHSdNC8JjTC1Z10L1bxt4LDYK2hiMEkXd_MeiaItmgrQC8t1B9EmiH4YiPzgVeEQDQs-JsXWTqg71dYSm3TpMHy8EBRbspSDgT56K1Fd5EtM2r-C_B_TaRscm8kJzSAq11FQpqllaNRDjl8jNvwV8EisZR5Oc2Wzxzi-1SyN5S3HBMjpN_v6xbOcf6GuyCsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f161b189f6.mp4?token=IMJSwujgAe3YvgpenBn_cBv-PiiGLhHHf9QQYiRzQM1UwLoVxfeuEHYm62_fq4ahMz-7JRAcQeK-YOrpJAI7-chi776UjCo--YyTBAg2buX4qbY9YLbopBoXMSTtzjk4EBTsgFBimv41o0e5OR5bG7NHSdNC8JjTC1Z10L1bxt4LDYK2hiMEkXd_MeiaItmgrQC8t1B9EmiH4YiPzgVeEQDQs-JsXWTqg71dYSm3TpMHy8EBRbspSDgT56K1Fd5EtM2r-C_B_TaRscm8kJzSAq11FQpqllaNRDjl8jNvwV8EisZR5Oc2Wzxzi-1SyN5S3HBMjpN_v6xbOcf6GuyCsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: با راه‌اندازی ۲ پالایشگاه جدید تا پایان سال، تولید روزانه بنزین کشور ۱۲ میلیون لیتر افزایش می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/458223" target="_blank">📅 21:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458222">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59db84866e.mp4?token=SNBn2VTblHhI43TUiLX4Iyeumhr7WDbD_bbiJtsMMd2jqdJjd0OYe5e5Y_sczjCo3f1Wb_vJj_2xdQ2USo5zMR9XwFEcuvk2H1qNfzxKPSKVbcGNX09PAM3J4BMn4ZtM0cisFeJaAlEak5KKKkPqa_E9ciPb4pyfkPPb64qcJ1HfAaQjwa39Ddr9NVuRkcNlVmEQn5PSsVy8TDjDq8Eq0Eu5RXHR05iblZfkKGIgpgU94qyjvHe8wQmONQMjEIvp0s6pNMHNQSyiUwkCKqob4IwfcXw59kDBqVYDafWPAKxbsghB-9ce8a53ehMBEHgwZ5jpzEvUfZZPa8K2DhCwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59db84866e.mp4?token=SNBn2VTblHhI43TUiLX4Iyeumhr7WDbD_bbiJtsMMd2jqdJjd0OYe5e5Y_sczjCo3f1Wb_vJj_2xdQ2USo5zMR9XwFEcuvk2H1qNfzxKPSKVbcGNX09PAM3J4BMn4ZtM0cisFeJaAlEak5KKKkPqa_E9ciPb4pyfkPPb64qcJ1HfAaQjwa39Ddr9NVuRkcNlVmEQn5PSsVy8TDjDq8Eq0Eu5RXHR05iblZfkKGIgpgU94qyjvHe8wQmONQMjEIvp0s6pNMHNQSyiUwkCKqob4IwfcXw59kDBqVYDafWPAKxbsghB-9ce8a53ehMBEHgwZ5jpzEvUfZZPa8K2DhCwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوک برقی وزیر نیرو به صنعت فولاد
🔹
رئیس انجمن تولیدکنندگان فولاد: قرار بود سهمیهٔ برق کارخانه‌های فولاد در این ماه به ۴۰ درصد برسد، اما ناگهانی به ما گفتند که سهمیه مانند ۲ ماه قبل فقط به اندازهٔ ۱۵ درصد تامین می‌شود.
🔹
تولیدکنندگان فولاد با اتکا به برنامهٔ…</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/458222" target="_blank">📅 21:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458221">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78fe676b69.mp4?token=iuUT1nvnWsP2bz9fcYM2LZcy6WXJhinMkv5e5NjGHqNTqEOSNa66voZXWXZY5XuHsfRxe5vgTxTaOF4GFoV6HrVagnxX1AGXrJdBh0QLNG2QBk7iwFPjt_rCYG9CMe4BdmHk7uPVMP8oV0KcXK_gvyCoKyUHVXo4Oe1H73_wW3vIS6k4zWfxEoyjjT3_TG1_lJinQufNDco7CXBX9oIKG1NVjrV87ZXIY5jelg57g7Kwrmb0SySSAs0gZu2qvmqjncle_CZ4hVAutwI7qlehN-W8wAzccBZxwuse5ne7fmhiMqe9PwmnG_SecdV9GTgSBOpvjI4c7D_u5z1a7yRaNUMF6pbxwsiqnCfpWF3Numa_FOBJgUn68jx0GaufL1CoOcw58hzAR6hnLT47vYedDaU0NYiT_B2CpZPus2auzBBCSw5FX91xNGyZjguKBmmKWxOMsKIwPbHTNgsrexqvy2YF_2bIAKi0NoySLOo599MoCzmjfmMfI_-raARk3isupAaE9HpUzRZg-MhKQKlhfApWsyYSJ9CQAHIVfVNMUTrOx6ZKMPyFtm00gxuplpn5lyElvmRwU60dVTNPwR1WHT61_h_oisJoDezhnKjaTn1MvC2BdR14VHaM3NYZScQctElKInSOY-h6YRrn5wojSZTlOuLpHDeOipmiF46iFMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78fe676b69.mp4?token=iuUT1nvnWsP2bz9fcYM2LZcy6WXJhinMkv5e5NjGHqNTqEOSNa66voZXWXZY5XuHsfRxe5vgTxTaOF4GFoV6HrVagnxX1AGXrJdBh0QLNG2QBk7iwFPjt_rCYG9CMe4BdmHk7uPVMP8oV0KcXK_gvyCoKyUHVXo4Oe1H73_wW3vIS6k4zWfxEoyjjT3_TG1_lJinQufNDco7CXBX9oIKG1NVjrV87ZXIY5jelg57g7Kwrmb0SySSAs0gZu2qvmqjncle_CZ4hVAutwI7qlehN-W8wAzccBZxwuse5ne7fmhiMqe9PwmnG_SecdV9GTgSBOpvjI4c7D_u5z1a7yRaNUMF6pbxwsiqnCfpWF3Numa_FOBJgUn68jx0GaufL1CoOcw58hzAR6hnLT47vYedDaU0NYiT_B2CpZPus2auzBBCSw5FX91xNGyZjguKBmmKWxOMsKIwPbHTNgsrexqvy2YF_2bIAKi0NoySLOo599MoCzmjfmMfI_-raARk3isupAaE9HpUzRZg-MhKQKlhfApWsyYSJ9CQAHIVfVNMUTrOx6ZKMPyFtm00gxuplpn5lyElvmRwU60dVTNPwR1WHT61_h_oisJoDezhnKjaTn1MvC2BdR14VHaM3NYZScQctElKInSOY-h6YRrn5wojSZTlOuLpHDeOipmiF46iFMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتخار ایران، مهمان ویژهٔ تجمعات شبانهٔ مردم شد
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/458221" target="_blank">📅 21:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458220">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b746a75b.mp4?token=o_xTMtEZ4iuNiTp4FNc4l6HLj2cLkpROLrhRe5CAIBnmVAEFfOfvpTEGr3IDCdbPcTYe-SbXz3dbZ_SJXkD59WN0P3-hXCwTEVh9bMvrLxwDMdqJTy8XsT2sCCnPNKM8LQ0hqa-fbT-d_y2tnsLBpz6AtmTxQivWlIXqOeb5s_k7Vok5ZxXqzinU1rkupywI-mxrDGEi3nTKMg6WdeyRcjedIB9tbuZe2uwAt1NaEEZZK4iIz_5LS2Od35-Ab-JwyEmemrYU6VUJCgeGCNoXtKiNLzmBNYhqWxQgPciyCTUYPEvFmxRLrv8hqWDkGiK84ISY04UAfv9eyPOjczd_nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b746a75b.mp4?token=o_xTMtEZ4iuNiTp4FNc4l6HLj2cLkpROLrhRe5CAIBnmVAEFfOfvpTEGr3IDCdbPcTYe-SbXz3dbZ_SJXkD59WN0P3-hXCwTEVh9bMvrLxwDMdqJTy8XsT2sCCnPNKM8LQ0hqa-fbT-d_y2tnsLBpz6AtmTxQivWlIXqOeb5s_k7Vok5ZxXqzinU1rkupywI-mxrDGEi3nTKMg6WdeyRcjedIB9tbuZe2uwAt1NaEEZZK4iIz_5LS2Od35-Ab-JwyEmemrYU6VUJCgeGCNoXtKiNLzmBNYhqWxQgPciyCTUYPEvFmxRLrv8hqWDkGiK84ISY04UAfv9eyPOjczd_nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌چه در دیدار نخبگان جوان با پزشکیان گذشت
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/458220" target="_blank">📅 21:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458219">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6-on3ilY-fpFxdg8jBfUe_efbgJq-Q6jfMQghEhhtnUsNZL5kHED4JQM2EMowq-_xWeCo3Y2aVj3Iqh2NjOtCl7leKdWDB6sjHH7Sz-frMyy3vqjq0PLMUGk2GarZfpE6iOzeMFvzC2soFjZBoUqWTcmnR3w9EnvhbnbR85GQlKWEBaAD-JodTKZ41hIFBvL0_YaNkyPg_r3HUazBCASsw3AsQeFR93vN1umL-mIsGZEE278i2SREzkXyvqP3o3ezBYRF_K_ZQEwyc6OQi1YaXqksqlg1Nk4lIeu32-gi4SihQ6uM3TiNUqXlA7MSfYj9lBn48FCYSfZA_OUOHkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج یک هواپیما از باند فرودگاه مشهد
🔹
روابط عمومی فرودگاه مشهد: پرواز تهران به مشهد هواپیمایی سپهران هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/458219" target="_blank">📅 20:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458218">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c5de9c08.mp4?token=eS8oZAc_bGGxceyqDovdiv5EVQE8KFkFgf6sG6VDdF3_OndjnJ6dUcGB2gkHZmfLiCM4DkCME0RbEIQ7BzYqmQg9JLCPidywIH9wYOa6zxro7F7TZ3vGPICMQbsYtdSHL_3E7wqHT_bpkprnY7aIWWjyZ3UuQ1s0oBwctfVrqeIbOb9zX_y-ywxIs35C0-QmySv1rnCAM3TlLMFxgDqDsTp7zG3uIH-TUQpSMcX_r6RHfhDSFrL5ESLJ6Qmbh-QtaM3RI6ww-7bYfzhgFFH6fojgWQWk96qhQ033hnoDz6mpYgn1_92tBGOMrXcb8vLOWg1UMQsddLhiL7Tb319tFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c5de9c08.mp4?token=eS8oZAc_bGGxceyqDovdiv5EVQE8KFkFgf6sG6VDdF3_OndjnJ6dUcGB2gkHZmfLiCM4DkCME0RbEIQ7BzYqmQg9JLCPidywIH9wYOa6zxro7F7TZ3vGPICMQbsYtdSHL_3E7wqHT_bpkprnY7aIWWjyZ3UuQ1s0oBwctfVrqeIbOb9zX_y-ywxIs35C0-QmySv1rnCAM3TlLMFxgDqDsTp7zG3uIH-TUQpSMcX_r6RHfhDSFrL5ESLJ6Qmbh-QtaM3RI6ww-7bYfzhgFFH6fojgWQWk96qhQ033hnoDz6mpYgn1_92tBGOMrXcb8vLOWg1UMQsddLhiL7Tb319tFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جایگاه‌های سوخت درگیر موج شایعات
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/458218" target="_blank">📅 20:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458217">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71720c1c8.mp4?token=gNujAiOMGx44ocozRbBR4eccVOnkG8HFzW8XFas77xff04RwIejqjpHr9Iy0Ic_v9skXJ-ordajbmFlftM1f2jVPcPqlgM5NKZmubwCuoeA33y8LUldJoi6B7IJnsr_2JIcsVcD_eFtmV8QIAJhAwPR7jIVOaLQuserJxsNaaq_XLLnMiW5MNJAMUJBH5ccQ5hDR4zItY1kCT5ln7olEPqfJwVFf1OSCpRV2eSNEDrz0khQwaHZ90-q5CtmHpFdZuYhc-xtGMHjp9SW79XeHaW3h3sOVdxcck05-SVGs29EQGUOTFpPSHUDPSdMCKJPYg8No7_cniX31Nm6qYmk8Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71720c1c8.mp4?token=gNujAiOMGx44ocozRbBR4eccVOnkG8HFzW8XFas77xff04RwIejqjpHr9Iy0Ic_v9skXJ-ordajbmFlftM1f2jVPcPqlgM5NKZmubwCuoeA33y8LUldJoi6B7IJnsr_2JIcsVcD_eFtmV8QIAJhAwPR7jIVOaLQuserJxsNaaq_XLLnMiW5MNJAMUJBH5ccQ5hDR4zItY1kCT5ln7olEPqfJwVFf1OSCpRV2eSNEDrz0khQwaHZ90-q5CtmHpFdZuYhc-xtGMHjp9SW79XeHaW3h3sOVdxcck05-SVGs29EQGUOTFpPSHUDPSdMCKJPYg8No7_cniX31Nm6qYmk8Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد کشاورزی: صداقت پزشکیان و اعتماد مردم به او باعث شد این ۲ سال سخت را پشت سر بگذاریم  @Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/458217" target="_blank">📅 20:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458216">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl7c9r6qWHDqxhur3pcPxHUeR6l493qRCjZbKjyjoqtQkSV47st7L1kOyEDfuJrJiWGGHYbnJQ8nhAloYfwunM9ByNkk60tt1XEZ7dDt1GDBJgwj1Tu76eakxgL9SfFRLAVIp-QHgAoOyl3kMQdwm-afj1iSsnBukSmwTtVzlltoTA_GWaj7-Yyn-gWxoa7NDJobLkBoVrg-SEYGb8vCuBxd2Lnzrxc4eMLjeKP27GtQQ0MiH3hhw13Y9XZMpOjHZ4rDvoefPc84DzP3-TyTLd8nPqXvEas2OUke4ZFqehM6PVe-jfp5CxMU2N2IkBj2jzJEZPOFUeqHKddhOgDR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک برقی وزیر نیرو به صنعت فولاد
🔹
رئیس انجمن تولیدکنندگان فولاد: قرار بود سهمیهٔ برق کارخانه‌های فولاد در این ماه به ۴۰ درصد برسد، اما ناگهانی به ما گفتند که سهمیه مانند ۲ ماه قبل فقط به اندازهٔ ۱۵ درصد تامین می‌شود.
🔹
تولیدکنندگان فولاد با اتکا به برنامهٔ اعلامی وزارت نیرو، برنامه‌های تولید، فروش و صادرات خود را تنظیم کرده‌اند اما اعلام ناگهانی تداوم سهمیهٔ قبلی برنامه تولید را بهم می‌ریزد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/458216" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458215">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSaB1OajpYfgWuRE0qgv72ROlLZxF08HwqElYsYbzOg0kkaqILrgQLRNn3x6rVb0A0OIraRqoA7FZww8N44Ij9KBYDiN1cIJiCcpVmH9Y3zSt3Qj7w52rSZbPg0bRtfzFENZh0igf4ov07u1GDc8BARvEsESncwoA0K33yDsaYVMm9dI7mofWvi0fyOPS1bxXQX1VF57Y44fKhVZ1bknIEdJXCsniq7flFw0fkTNLWbvoOnelsW7xWAy5ghMB3aj1wYOQW2sJVEo3wojTKnnSVQ55Ou9tnDGAh03tmFpBZSGEvGTsiER-hnZlLvnQ_U5RxjKLll79ii5CXQnjyQjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی دولت: سهمیۀ بنزین با نرخ‌های ۱۵۰۰ و ۳۰۰۰ تومان بدون تغییر حفظ خواهد شد
🔹
تاکنون هیچ تصمیمی برای افزایش قیمت بنزین گرفته نشده است؛ هرگونه اصلاح ساختاری نیز با رویکردی تدریجی، شیب ملایم و بدون واردکردن تکانه به زندگی و معیشت مردم انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/458215" target="_blank">📅 20:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458214">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۶.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/458214" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۵.pdf</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/458214" target="_blank">📅 20:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458213">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6kN_FCJjfQu7dbGDCD6QNZ6YJ7kmgfLwdHikk11okNOzi9sL4zLcktZ6AaFi6g4EAisRAGhDL0v7ukl_6J17w9gZ6v69VcVh7x_5dK3Q-lkpKcYbzNiaE3TTVX3P8OBtS5cD--ZagtFESYt5x3WGCGGUXsbrcAUR8e5atKOXnv9Q7c_g31PWktN2DXvKlh9gY0-7I4mhcUgpNF3qZbRgq6l0JE0ZQNEIfwJ-UHMY4Y9KCGrKcDeODTAECpn5e4PJWTJ8rUf0rzjv5xZqGjnig29ixgJs8_7xxKdSDkmgY1U_wtgXmfsZ26FixVGmVXkekHFzPPMT73swHcYmHje5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: آمریکا در جنگ نظامی و سیاسی شکست خورد و در اقدامات اقتصادی نیز شکست خواهد خورد
🔹
نقش ایران و عراق در ایجاد نظم منطقه‌ای تعیین کننده و شرایط برای ایران و عراق حساس و تاریخی است.
🔹
این که قرار است نیروهای ائتلاف آمریکایی از عراق خارج شوند، یک افتخار تاریخی برای دولت و ملت عراق است، امیدواریم این خروج به طور کامل از زمین و هوای عراق محقق شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/458213" target="_blank">📅 20:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458212">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgXG0deZfcRFYd4wDK_0yevaNH31nIK8KlyAlBdp-VGpsp-lBCGwuInCoCDYD6IoQrjV96eBcCkQ21Q_jdnbYXx7q248enVhl9MuG-iU4nx8m4TPngevJk6z6TOCyOsBLm8Uf78X8CWh3cqfcOiSnIv1Dj_eitdsoJdbJ693aGZET9WNPiSiOrtKX4U6Gouvp-kIj3u4QDd2G80BisknWL0rM6vHRBio9pdLZzy2nhxreJVzjgtDFJaM_1dwLI-QpJ6ZFEITgkB4bCVgw-mCIceyUxxFbHIKbwV8uQ-I4J0fpWJ366TzGdmUZ5wBDstzexSsyFtknF1XIJdDBONuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت سرباز صهیونیست از قتل خبرنگاران در بیمارستان غزه
🔹
رژیم صهیونیستی سال ۲۰۲۵ در یک حملهٔ دو مرحله‌ای به بیمارستان ناصر در غزه ۵ روزنامه‌نگار از جمله حسام المصری، فیلمبردار رویترز را به قتل رساند.
🔹
مقام‌های اسرائیلی پس از حمله اعلام کردند هدف، یک دوربین متعلق به المصری در پشت‌بام بیمارستان بوده که حماس از آن برای زیر نظر گرفتن نیروهای اسرائیلی استفاده می‌کرد!
🔹
یک سرباز اسرائیلی که به دلیل ترس حاضر به افشای نامش نشده به آسوشیتدپرس گفته: ارتش اسرائیل هیچ مدرکی پیدا نکرده که نشان دهد دوربین المصری با حماس ارتباط داشته است.
🔗
ماجرای حمله اسرائیل به خبرنگاران حاضر در این بیمارستان را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/458212" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458211">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نتایج اولیه‌ آزمون كارشناسی‌ارشد منتشر شد
🔹
متقاضیان می‌توانند برای مشاهدۀ نتایج اولیۀ آزمون به سایت
سازمان سنجش
مراجعه کنند.
🔹
مهلت انتخاب رشته از ۵ تا ۱۰ شهریورماه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/458211" target="_blank">📅 19:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458210">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed5e4ed0de.mp4?token=lDoHc-AGIf_5FleVEt5b0hJJemNJ_IuqeAw-D0dZiu9lufTNDMn8etOEH70ZQN6ZDkSUJhUNdroIveJI_1RGzvEDdN6dQ263thNv8O--Duz9BqQe1EzwDEyMgwGD4fHQkMk3-TG1fIuzZ9C8rYuv-AvAcqey8RVT8pT0vEhi95BUnO-LGjFWAwNEjNWkFEZKpOTWZ0Bm6N__MaFSGrYwZseqHrU0BTt8a4tjgnqKtjsUCAt72wc-1hlQJhnacNAk7_OI_6sg-ei36OBLwmko0AfeZw_tPKhaVbDbpcmZ-g80rjfUrMGEuuOdE_vD3C10kzqfPgIjXajVugQQaYYP5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed5e4ed0de.mp4?token=lDoHc-AGIf_5FleVEt5b0hJJemNJ_IuqeAw-D0dZiu9lufTNDMn8etOEH70ZQN6ZDkSUJhUNdroIveJI_1RGzvEDdN6dQ263thNv8O--Duz9BqQe1EzwDEyMgwGD4fHQkMk3-TG1fIuzZ9C8rYuv-AvAcqey8RVT8pT0vEhi95BUnO-LGjFWAwNEjNWkFEZKpOTWZ0Bm6N__MaFSGrYwZseqHrU0BTt8a4tjgnqKtjsUCAt72wc-1hlQJhnacNAk7_OI_6sg-ei36OBLwmko0AfeZw_tPKhaVbDbpcmZ-g80rjfUrMGEuuOdE_vD3C10kzqfPgIjXajVugQQaYYP5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد کشاورزی: از ماه اول دولت، افزایش ذخایر کالاهای اساسی را دنبال کردیم که باعث تاب‌آوری در جنگ شد  @Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/458210" target="_blank">📅 19:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458209">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6edef8b8.mp4?token=rCKVB7Ko_INjmp75kxbsKeO4I6yaZNagySTSpHlz1ymwhhsj04Kv1lJlzGUM2KTnV1XQWwxE84f34JOpvkqW_NOGny1e5oQVjcoa90j0t8F4GF8u08DlWiw5XW7P6FSlhHy2qLEG3tvqR07UDUHBGQwZtVzsBKqYh8fJ8RI4ozAvX8x4_A3dKna1SY1LfHGasnBwpSevZNH4s7dRfP50OopH-HDwPp4QFLQ9E61c7JqlGL1XEKnppQlWtG44CtE6I30MTFzPfjOUsqeobHO9ouMHVV84FK5MpN1LxGahA8FnofBenX07Pg1KaINmEjOXgHA1QPDUwvNlbQOyl7J6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6edef8b8.mp4?token=rCKVB7Ko_INjmp75kxbsKeO4I6yaZNagySTSpHlz1ymwhhsj04Kv1lJlzGUM2KTnV1XQWwxE84f34JOpvkqW_NOGny1e5oQVjcoa90j0t8F4GF8u08DlWiw5XW7P6FSlhHy2qLEG3tvqR07UDUHBGQwZtVzsBKqYh8fJ8RI4ozAvX8x4_A3dKna1SY1LfHGasnBwpSevZNH4s7dRfP50OopH-HDwPp4QFLQ9E61c7JqlGL1XEKnppQlWtG44CtE6I30MTFzPfjOUsqeobHO9ouMHVV84FK5MpN1LxGahA8FnofBenX07Pg1KaINmEjOXgHA1QPDUwvNlbQOyl7J6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد کشاورزی: از ماه اول دولت، افزایش ذخایر کالاهای اساسی را دنبال کردیم که باعث تاب‌آوری در جنگ شد
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/458209" target="_blank">📅 19:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458208">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOkQfucgakv_tIAsMS_Qoel96wAPy5WDFox3CtEt9aCIdPQLu7tcFlyLRujOnZhIFSxPjbzBSBzexm8pERbZ2ygz_P3GmzQSM0eVtlY1EralIo6s3IdXKkgBk6y6BCnHCfMQl0ZKkpQnoWwiOMvmL6MZp0YlsVwqzTCZ4r32z0p_V6GHOLVXZYR4z8W0fpyqigqWhCk7tV4O9HZpP5voyZbp5kte1LKNF-UW2t2EXNIblKf8EO4CTMuuO8jxq2zTYKx5fTab1DRQD4cyMhbQTlbOSPBuO3AfJT4jQZ4Rns_HhbxbJzEZ9vYTc0VYfCXxqMP5rrBo5Y7xSVIUhnzKBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: جنگ اقتصادی آمریکا علیه ایران، حمله به حاکمیت ملی همۀ کشورهاست
🔹
وقتی قلدری اعلام می‌کند که همه بانک‌ها، بنگاه‌های اقتصادی، بندرها، فرودگاه‌ها و دولت‌ها باید بین اطاعت از هوس‌های واشنگتن یا مواجهه با انتقام آمریکا یکی را برگزینند، موضوع دیگر صرفا به ایران محدود نمی‌شود.
🔹
هیچ دولت شرافتمندی که برای حاکمیت و منافع ملی خود ارزش قائل باشد، عادی‌سازی چنین قانون‌شکنی کلان و قلدری نظام‌مندی را نخواهد پذیرفت.
🔹
البته کانادا از جمله کشورهایی است که کم‌کم دارد طعم واقعیت (قلدری آمریکا تحت لوای مذاکره) را می‌چشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/458208" target="_blank">📅 19:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458207">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8aveJ1Bx5_4HQNukmesQZh81NuEw7zBlo9-Y8Au2mImd8cwP63sbS1nW2KI-WpCPXKLev-vZb556Zm1ipvKHd9DfUi-O8mQq-6du7mLPczF3Q17hnANhZ-TyDH5qbHIwg4C-rejTNkqgs5Eru81447JvkIc2paHtIdIggUrrsKUFGShgjniQkcy7HQnM_GvrjD-6tGNwKkKCZlW3BecKLds6rkadGLehIvVNG3y8wyUr8buE3B4CwcFxCFd6ugvtP3pGy84eY3mv002I6bmf7kWcsyJ8bAVTYhIDTHRXiKeGNznk7laG0GqYTiMM8VxK1w5o7mNFW3lnUhhqsbwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکۀ آمریکایی: مجروحان ارتش آمریکا در جنگ با ایران به ۶۵۳ نفر رسید؛ ۱۷۰ نظامی هم ضربۀ مغزی شدند
🔹
ای‌بی‌سی نیوز دربارۀ تلفات نظامیان آمریکایی در جنگ ایران گزارش داد  شمار مجروحان ارتش آمریکا به ۶۵۳ نفر رسیده که از این میان، حداقل ۶۴ نفر از افسران ارشد بوده‌اند.…</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/458207" target="_blank">📅 19:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458204">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7KxwVO_AExUSXCMikcWCB4ziWZL7SRsuscMDfG6VvixgJn0DgELcOH5C5eE-4PwH2on552bd_Xvl9Q0ARm3Fjyy1ueowwifC-O_C_EuKsKx1AZm51rSCU3nmZjP71UKH1TKVvy2AREEJMpDJZU1VsovUcD7X-rT7QDT6Tcv8Pzi8mZsU4Zo8t2Lo0e7mb210Z_lwBqwrvcDvZ0hb1Cgw3FGVpGKLl4tca09gk_gm4ebDMNJglrrDrucvk4GEyN_jYwyC5yt0Kfqb7K_LpxV6m2PdYiKG8ZrB4duHqV6QwrK_q7wdy0LmfQgVveqmngFEvFZ3AdkJOtkLY2bSi3zfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyX1I_KoYD_5Vp9o1YgvCZfeRiF9nrQ5_nIM4PXeiewewuzFzlT15w-pKTgK39To8Tgakxw7prO0L3MlnYGMUkfwjRfL-Qny8H36_Ls3QwxdP3M4OribvZohxT_vV_dWwZ8SB4Y5HeAazMrmeDQfM4VJi_Lgu1rmE2wl2egZ_A5qHnluNqhv6mR0q-dC2UfsQV4iuxvb0tcIJR8n6e-sJcYRHJnyo3IGAvBUlpmIzoFRPgIEexjZxdvGJ1Ihwmk3OZglThaDiJg5R-dDd81QUbecEXJLs2tHegn-eL_mC8yqaIphwzxhAV-0_LqJmjBbmXIAeEkxYvGbMHKD78P-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S79IZ0C5lmvfGjNllEJF4CLtLLm_o4EiZ35XeO0MildcXy3mI85RjhZCjjOZzVF5YWRRcBARshSRT66-SsHqCBiqu6W2GVH-UTl_0UTgV6yR2S_od5NQfIKDnRjkZsb3u0rRmy0-tSeR2CykH8l9uIQnrRfJKvm2EWTDhf0fydvsBU0HDRCvhAiJKk4nrA40qSrqjFjpYK43RHXMsaqovqwjxZqHluZDTf0ori4lwsdx7CznYDrvI5V3tmFoOh1mUP35EDyMAo46zaLFgad9auwyujybKpjIPWw8TZTX0CB-se__lPcuILEDQqXlTxRNY-jmOUMaJv65zEGIv-zkDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: آمریکا در آیندۀ منطقه جایگاهی نخواهد داشت
🔹
دبیر شورای‌عالی امنیت ملی در دیدار رئیس شورای‌عالی قضایی عراق: ایران خواهان عراقی مستقل و قوی است.
🔹
کشورهای منطقه خود دربارۀ آیندۀ خودشان تصمیم‌گیری خواهند کرد و آمریکا در آینده منطقه جایگاهی نخواهد…</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/458204" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458203">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda1ad0212.mp4?token=PljW-WiQ8X9I2RkVL46FABkrllxo0YTztsYD1ygIYiU0aWfjMv7nZy6SbYr9eF46oxY9K3gqSrC3l-xMx3modHcLvZ2sh_sRdHXyOYJ33Jv9FvHNFxKTaDDsj8q2v5VIoJDbNhrQL_muHze41MOv6rN0W5ytOgA964xhs3nvAIJKSb3LKjnJcaM8R4KML1TOtd9HSjv1LP2iyYPa83e3jaJqL6FZlet8yE1id0jV6athu4INwn7eEB8aO1QaaDsii5eQk0EPtyz6XWuIK-zJ3jpWLqSwSxNBbIYrRsG8sDV_qhl1PwecvZTtZMeA30Wf8KGe71lZAuxxwvVYwalD6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda1ad0212.mp4?token=PljW-WiQ8X9I2RkVL46FABkrllxo0YTztsYD1ygIYiU0aWfjMv7nZy6SbYr9eF46oxY9K3gqSrC3l-xMx3modHcLvZ2sh_sRdHXyOYJ33Jv9FvHNFxKTaDDsj8q2v5VIoJDbNhrQL_muHze41MOv6rN0W5ytOgA964xhs3nvAIJKSb3LKjnJcaM8R4KML1TOtd9HSjv1LP2iyYPa83e3jaJqL6FZlet8yE1id0jV6athu4INwn7eEB8aO1QaaDsii5eQk0EPtyz6XWuIK-zJ3jpWLqSwSxNBbIYrRsG8sDV_qhl1PwecvZTtZMeA30Wf8KGe71lZAuxxwvVYwalD6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تولید ۱۰۰۰ سامانهٔ دفاعی ایرانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/458203" target="_blank">📅 19:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458202">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXprYoLOyKbIy6BExuy_z6MEl3U_ZAtlCOPCwy8w1VB__13UQdKCAA_zVebPXSs0MQ8dA-H3G-2tGQEATr-cJkbj08MWUN2vUA1cAgA0Aw4ngMgnLSI6_6qTcvt7IVpeupEBx7TfmuTSopC1hIgPXXFYKwTIRYNBBEtbXPC9U6Mo8P5-tY1n-39nI9rkGlCtiB8KdJk5HMznKdRbmN8T09h6aUuFsYJgAEG6mFFV4PMyJFOvnrrYmXaSe9pmaP36CIcurq3-5vBj8eyJJhInaet5BFdhHtoP605jZRCSplDxoR7G63kFuyXlRy6EnFvY8f7L6AgYYdHC5Y5mhsjrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهام پیمانکار پنتاگون در سبد ترامپ
🔹
ترامپ درست ۲ هفته پس از ورود تاریخی و جنجالی اسپیس‌ایکس به بازار بورس، بخشی از سهام این شرکت را خریده است.
🔹
در نگاه اول، این کار شبیه یک سرمایه‌گذاری معمولی در بازار سهام به نظر می‌رسد؛ اما حقیقت بسیار پیچیده‌تر است.
🔹
اسپیس‌ایکس یک فروشگاه اینترنتی یا شرکت تولید موبایل نیست که سودش فقط به رضایت مشتریان وابسته باشد.
🔹
این شرکت یکی از شریان‌های اصلی جنگی و بازویی کمکی برای کشتار توسط آمریکا در گوشه و کنار دنیا است.
🔹
از پرتاب ماهواره‌های جاسوسی برای پنتاگون گرفته تا ارائهٔ اینترنت ماهواره‌ای در مناطقی که وزارت جنگ می‌خواهد، همگی به اسپیس‌ایکس سپرده شده‌اند.
🔹
مسئله این است که رئیس‌جمهور آمریکا از یک سو در این شرکت منفعت مالی دارد و از سوی دیگر، دولت او درباره قراردادها، مجوزها و مقرراتی تصمیم می‌گیرد که می‌تواند بر آینده همان شرکت اثر بگذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/458202" target="_blank">📅 19:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458201">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLhcuPb2buaap7AwwnpOYDoFfFLZyKPW4f7SDzyc6xZ7VF8TB7PlzKxaUbLTX5VedkcyqrU93sAGAf0flllcg61Q_CZ6HUkUW9VwIcTTN5qi3EEkNszTQEIBLkAr3aIYB3JOUcINqFhdK5E74FqE67cVGzKsx51edLGtOqoVL3av83yakTnuAMRASbCCIS72pdABX1szZEn14W3cmHqXyNIMDHnvei8TdkIRMmneJNr2c3gswF7wKkcMBpG3piPXesxDywPNzXskXxR0wLzj7Shw1w2jKd8G_FyGGmH-v3TnVY6E9uLUta1edb90tLtIyvIUgXnwJ9wTBp-jUfhAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلارهای گردشگران سلامت ایران در جیب دلال‌ها
🔹
ایران سالانه حدود یک میلیون گردشگر درمانی جذب می‌کند؛ بازاری که با وجود پزشکان متخصص، مراکز درمانی مجهز و هزینه پایین‌تر خدمات، هنوز با ظرفیت واقعی خود فاصله دارد.
🔹
رئیس انجمن دفاتر خدمات مسافرت هوایی و جهانگردی ایران معتقد است دخالت برخی واسطه‌ها و شکل‌گیری بازار دلالی، یکی از مشکلات جدی گردشگری سلامت است؛ به‌طوری‌که بیماران خارجی به‌جای ورود از یک مسیر شفاف، گاهی با واسطه‌های متعدد مواجه می‌شوند.
🔹
کارشناسان معتقدند گردشگر باید بداند از لحظۀ ورود تا پایان فرآیند درمان با چه مجموعه‌ای طرف است. قیمت‌ها باید روشن باشد. نقش شرکت‌های تسهیل‌گر باید مشخص باشد و مسیر فعالیت آن‌ها نیز قابل نظارت باشد.
🔹
گردشگری سلامت می‌تواند برای ایران تنها به معنای ورود بیمار نباشد. هر گردشگر درمانی برای اقامت، حمل‌ونقل، غذا و گاهی سفر به شهرهای دیگر نیز هزینه می‌کند. به همین دلیل، رونق این بخش می‌تواند درآمدی فراتر از هزینه مستقیم درمان ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/458201" target="_blank">📅 19:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458200">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTSt0tH1HYzilQ_NJIN2jG4Kjl0bYuH5o6m1xYndc11N6eYOfjhIIiDqEvSdhkIQNw3_OLm_xEg4apDHVhYf4pOHE_-5j1q6qZlmctxtrAs37lMyzsC4q77VEZYKAz6cphaJduV1O6Jpjw2xTMkmycIS5i8kOp9xiaYhmYs_qeL9BK5g33rBDUFcMOlyQs2rZxo8Tu72xp-6_aaCjnNTSyzTjQFlGCa-2TW276oA70Qpi7DmQ3Mr4mDXzG2Gg8xbZNKHJyr8aNex_ANmf-JKK6TMtVeGGh1TbfNdzUf2YgWinXlDsyIcrX3EdC1fJuQt0FZIQjKuPO_pwiXbZUPlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ایران و عمان: دربارۀ چهارچوب ادارۀ تنگه هرمز گفت‌وگو کردیم
🔹
رایزنی وزرای امورخارجۀ ۲ کشور بر ازسرگیری دریانوردی ایمن در تنگۀ هرمز با حفظ حاکمیت خود متمرکز بود.
🔹
چهارچوب پیشنهادی شامل این موارد بود:
🔹
ایجاد یک کریدور مشترک از طریق تنگۀ هرمز
🔹
اجرای پروژۀ مشترک برای مین‌زدایی از تنگه
@Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/458200" target="_blank">📅 19:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458199">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLgAxD9sYeyjaLFuIEWLUL1M_dlq2EE_KM5bc5GxxSXUe0Ids-4rB1w2dYFwr_pMmA5mfV8h8F1hDsyMKdWi2I_TvYld-b38ZnHRayB8KO4SXS2PCgQXy6Tltl2TsNlXZahlZbWzeA1-gtihJ1RKwKUo2AQgRwilDka-jRBNodOspacWhXMTdg28qlabxMocEkjIkA0WgooRQhn_x75KbE5nLBQfGgQzhvuLi3iC-0_GBXqs8whNgQ5GE628tsJPugX-r7IdY79z4TueoQvfWkx99uivrwAV7z6Doj7GZU42xyoMWsBrnhEVlKbi-CtR1oPbyGmOqGTrYW2QdkRJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: ما از طریق نیروی فضایی، تنگهٔ هرمز، کوه‌کلنگ و ۳ سایت هسته‌ای ایران را زیر نظر داریم.
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/458199" target="_blank">📅 18:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458198">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🎥
مسئول مسابقات لیگ برتر ایران: ورزشگاه نقش جهان بعد از ورزشگاه آزادی بهترین گزینه برای میزبانی از دربی است
🔹
نامه باشگاه سپاهان برای مخالفت با برگزاری دربی در اصفهان؟ من هیچ نامه ای ندیده‌ام. مشکل حضور بازیکنان لیگ برتری در تیم امید با تعامل حل خواهد شد.
🔹
محرومیت هواداران تراکتور و پرسپولیس چون رای نهایی‌اش صادر شده بود باید اجرا می‌شد. امیدوارم دیگر شاهد این نباشیم که بازی در لیگ برتر بدون هوادار برگزار شود.
@Sportfars</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/458198" target="_blank">📅 18:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7uOixXY3hJs7M8lZ1MoJM6i2hLjE6KILRkdaVJJmbiufGfxBJl4vljP0xwBbu5It_c0YOXTx-rAuz_P4tLftkjveYun3FK03pPVDTuFuZ0nvPVqGkGXbYPUADfFZnKRBrNAXTfwl3jodm9C6JXWb1QAHMbzphln38eINFxOR5cu_NjhzVqKj6k-suMqCeJ2s860hM8qacrLa8hNL1DT2cxFp3rAgB6-J4b_egWKxzXWABeCNLypmZxpUC-Pf4UIjhzKaty60xhAOuocCXe_3kIhfyh84FYemr_oSG9Jmp6-FdQDqtJEwKfrj3q5ikm46WGssyYnKXKKy57UgrhjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم‌ترین موضوعات مطرح شده در جلسه  ۷ ساعته رئیس‌جمهور با رهبر معظم انقلاب
🔹
تأمین نیازهای معیشتی مردم
🔹
شرایط موجود جنگ تحمیلی سوم و آینده پیش‌رو
🔹
بررسی تحولات حوزه نظامی
🔹
تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی»
🔹
تعامل اقتصادی با طرف‌های خارجی
🔹
وضعیت مسکن و اشتغال
🔹
بررسی نحوه ایستادگی کشور در برابر دشمن
🔹
مهم‌ترین توصیه رهبر معظم انقلاب حضرت آیت‌الله سیدمجتبی خامنه‌ای به رئیس‌جمهور
«حفظ وحدت و انسجام داخلی و پرهیز از اختلاف‌افکنی»
بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/458197" target="_blank">📅 18:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458195">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXBqrdPEtgbEML7wHLDx5QAznpimO0jTdoYSc2NL3DRwfmpMlF085rMVy1jZD8ZQ9ZZv0pE-Mph1yAG09altSevsC8mHJlzNC9NJ3owNDYYxnfkDygWozJfThcnuhzH6Dj5oc32OqdATVwrpD-dQSrMy29zQjPujAaBW46uZF87JdBNpFMJEt0EJmrBTOm1Ml4Uy0KChlHuH8NnPeI5alwTG7Uq2YONvK9p8KzELRzzB04vlvm3bioaVTrngKGzdsEHKSzdFnBFheevZdqhMdT9KaKBp8Gjl0BeGh6JDRbmCDuMDMPuDr92KjE6IROOCQOabFS1wkBzbqNTPAoP92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsykC9lRVkeSamvbKer2vWmmZH9pZOgfJkm3WPTWaCt2Yy3BB1B2DPp1b7bfHGE0CzNmKQZiCUa_FdJYvZf7bDa9UVQVjRzfzGW4lFaGKUJzdbAEvJzZ2-c3Uny7tfYniPjv0vmu4SOYsjnjhkvhaCtwXw_FpW51IpejtY3EyvgCq1u6T2T5zkMYaSQBfSS3rKqTeF-6DNdqLSB2V81X4q7n4-p2DXAeVm1AtIoIH6a6yXm1uwnOzmOUdzuNnrzdf5m0h22U5zOupb15rsvoXmcXKQn_ceXwJ77lwNtsr1BsaPYUvAFzr4_ZtoWjuS0IGFZ8DHWQGkKLlndJuqAYhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ، حریف بازار ارز تجاری نشد
🔹
طبق گفتهٔ رئیس کل بانک مرکزی در حال حاضر روزانه ۱۰۰ تا ۱۵۰ میلیون دلار ارز در مرکز مبادله تامین می‌شود.
🔹
بررسی آمارهای مردادماه سال گذشته نشان می‌دهد که این اعداد نه تنها در رنج ارقام سال گذشته، حتی بیشتر از آن است.
🔹
این در حالی است که امسال کشور هم درگیر جنگ و هم محاصره و محدودیت در تجارت از طریق بنادر جنوبی کشور بود.
🔹
رئیس بانک مرکزی می‌گوید تاکنون ۱۶ میلیارد دلار ارز تامین کرده‌ایم که ۹ میلیارد دلار آن مربوط به صنعت بوده است. این رقم مشابه میزان سال گذشته است.
🔹
ارز تامین شده در بازار ارز تجاری صرف واردات مواد اولیه تولید می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/458195" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
