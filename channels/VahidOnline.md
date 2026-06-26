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
<img src="https://cdn1.telesco.pe/file/kiJZpLApdaHsvydG61pV_hYeFislCrBgh3Psc5QXYsiL8fzB0RxR6XrdtfI1xI4S1WUMsVvchVcpsO4JPuPWR-VHxyDF5v4cm9mYP1Xn8QMiAgXIoJX67hl9Jzje1RfqDZKhyjjO9ZBbpA729pEazuilb_J03JYf24vEl8xxTKdr0hX7UQkpfwKO_kYpvQ4_cjm5TPXjnVDg-2Q5NtgFcZON54Ic0HJfRTaVsr9O-0kfsShEnoT4CdT8L9O36wSPBxd7nqyUofqHo9bz7mc3ytLFTWPvj60kep436_DbCCYXexsnaBDIEQwn5A_LYXnGzgXB9xo8AJ_7u_qTyV10LA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 20:43:45</div>
<hr>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=FBsEE9s7-8tpDSNwWkKRpJ54O7ukFBCVKUDGIzznh9fkqfUj6PATa8OW-x4tLHwkbRlQ5Sn4q7xGJUOm526YEW8Ymcwu4ynbWhmFr_waavJhjUaO7EFRpSQ3gNzBrwYs2VbSXIatsbjn6VAMy2V9j0XGTPIok20Eyx2MMgbmujbUlhiwK_6pmOdKlazGZ-aXXvx2o4hteCtEz3MoZqcEx_ZLa3JaXxZop7FT07WOf-2TnRHah92tAK8qYClb1qQcM-XYaPLFfb_4RehFkQmxDLL1qZX916Tq4JoxgeI9I0kxD8TpemrXIJQ19__U8SyWrztzlzEsw9Gdjc80PkPcvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=FBsEE9s7-8tpDSNwWkKRpJ54O7ukFBCVKUDGIzznh9fkqfUj6PATa8OW-x4tLHwkbRlQ5Sn4q7xGJUOm526YEW8Ymcwu4ynbWhmFr_waavJhjUaO7EFRpSQ3gNzBrwYs2VbSXIatsbjn6VAMy2V9j0XGTPIok20Eyx2MMgbmujbUlhiwK_6pmOdKlazGZ-aXXvx2o4hteCtEz3MoZqcEx_ZLa3JaXxZop7FT07WOf-2TnRHah92tAK8qYClb1qQcM-XYaPLFfb_4RehFkQmxDLL1qZX916Tq4JoxgeI9I0kxD8TpemrXIJQ19__U8SyWrztzlzEsw9Gdjc80PkPcvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8qihro49aoK1z5CB0KzsFUDsexOqAbgeHDuG57g0l8Gep9Vw2TDW91vaEaugSPYi2iUCeV6pW2SL9ixMpXU7omTEb4Om6UD4fBKQ__fVROcQ_u2O5eyEczbYuPtd1zvcfHIf-NMNp36zM3IGoKzTvc_WOQS8S-L_qSf8M2EMIwGhAV46Z5BGQm3cAd6jSbMTpXLXJ--yZuIWsyM87Y5HzuU0otkR8HKjrM5eWqhpohOUV1pgmzLoCL8tsfBo26RWJnjNrryyaIZAQm-dDsIyNuUwWbx3kZX2kCdi-vB8-CmsrK3yJeS5m9nPQgI2Ylm5iXvWKqWQaX9FNpAx6G2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QhIB_yHg41cYSQ9Xfa9XCFJFq5iPPkqJ5jy43Ax95FIiJ5iEPdT4KaoiiKi4sCumkHMfPzfU3ddxkuPYvKkZWzKzYHc_M0-uuex7aKcLOcrVwoBSLNfd_JCKUPlt_wjSkuF0d-u1OGVetGJtD4-VKNOg1PuAmru637t9Xu_u0ob3E0gTElo0RqJUGoh_eZql1Rp8yRzmEJLZodubDojHyadvKsFFPxVNmuJSpmcRVr3ra97rmU7ndsDJvSHpZPw0Oj0OZUmFgnzuaAsemhmdriT59SJ_cPoc07k0cc5lBD2PUnCeOYww3pnEz881pNAugiwX7p-FlJNtAElUWSHrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKsQ9KD0rZMlk9JVfVQPqbkxCdgJCalkMA1_bPrCz1uSrW96LZmsoHk8mEiUP493EV6j8b5NteFN79AseyOzp75l00vLDfDsyJom7heGyTPwmxiRLwJpFDn1nLrJ_I5rWl8vTuRLmXS4WDdiqz44R_tcerSfioWqgPsdv0fhKMatB8xZqHmBMF8Rs0ubpL4UkogD_z4T-aMuHv7WPZJxBMLCsmSfocJsQCG7hEPkE6Oq5Lm-7bECTnnWfzzJSD1kDqRGL1li_MBHGGIbzKPPiOQ9njI6jDEQ_K0zRWZxHZTYh0HZxr6GK_iesJidlTlSBZX3YG_w9_Xb3Eklh8e0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iwkZj25bdwDmGy9ifDAAbnOIQMlltiyxmCwtOjvkUNlCpPVdZ9o_A09UUmQVFybE9yl9m2jI5Bt7A8dfdIMtcF7iQ_g9ghE3NBTZK71YQrGIwnUciluk5IOHATzpCjSH6QBPkDhQgfKZCE9m8JyAqtan8XQEqse2e4qi6if2kLf4Hw0674qUFy9r_Dt8j69pfjTtqaxq_CeNA-ckjeA90FDZVe47Gthsvpr5eSn6dZvRV2QIU9Yz0fBcEvELp9thngJlpdRwNniRhp_192iPpu0s61Ia5_eiK_3B3KAjUz--fu-kL9i1gPHNwIY1YIqe_j-PJg_ZDEYr9rrrLENgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uYvoAVnQnfGt6cbiyZ9FLBlNGlfoGZIro2_xYFGGwSg1j383wmoSa3-c_konr7jk0gfL_IMYHj82_kpjbOCrr27YLGeh2WdA_d5BT1l7MWOGQDipmRJhdWIBB2dNVtYhl3MeWxZCjUmvPwOdtYMQXB9QIugK9WcDv1Howw26wfb_D-eeWMJEVymeEZ_QzFhz91PU0Ow8oWwV6BhfyuujTGsaobbOH6j44VUmqUQ7KhkqQlfFvI1oGgiBYYFb0eA-SKaiawOzM7aKOzZnkx5oWDbFYw6uFFaVJ_P0BguT0goWYSum4zb75RAeJwfGPDIuME3QwlSX18ETmCeXQUl2GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tbgx3OKqAHi5mLDnCb53LeuNYfHxVoGFe7WkN_aIwUSGA2E4wwoyYZREWJ1-WxpvC-4LvjmS0ZXlLXcLNpN0NQSDJ1kqdI5KjJSedUP8Vx7NQFCr35WwiiVSU_8Zdr52AA8prvX9TW6Dc9B9Q27_JcMfNtiHkSmtNaq-v0gH7eub9doWBawtjeMB7t6M3cVOzd6Wtk-d1IkLoD81RFOPyy66irSBv43sQuE36IlAbwSEn8LVANa4GhYY0HEjwbZjxjd-cd7E5mf8gr_ZLMAGdyi-Tbn6REYNOd43gYxQBU-orHB3ecPeQ67PT0LRCUAbs8seRyL7O38ZvaWKEz7uiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bpFsZo594K-ah_H7VCG0Kc7bSkCZt6aKjcHFMEAs-Bz3fsBMUOXA5gcjbNFiGjPCnRRfmQtkhavqu0qmqO4FDslOXJHlSWDbZi-vZSkC8mXCmPe3Ht6oS129mAiDUynslvoFJ0bLS33hTTIjAg36jr3zkEUMTQ2E25PCtvG8hzE8tJm6BUKAaSbARrY2YhhNDTHDnOK7grIkaKm2QBKQ_dgvplbKnPUezNcHcmLZ8hZCLpVwGASDMYx5bL17gZfR2SMmDFYzxrPN5D5zsadt8X0WuVLQROgQW80W4F2OeQFlr5ISXQW9Of2-3BUbT0YC8tRsL05m79Fpdv6FJ581KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uQ5P2_k6imbIUrXs-eyZtEiPqDDcOERR4UfMhX4pIBZGnF3bYYijFAQi3x5-ex4C6kaE1KemIK1jGmFZHlrDxBIGlIWMlw2wGgoY5TFtFwGYOyIgLauIqQfPM2-UA2lx-BEZy4AwfTxelmf_-QAucKK5ZOgMGhDuv2istCSGRoF_mUwx5ZkIhqSpbUPx-h7_iyBK5zvs6X4ri5tzO7SPjiBuYnRsHilChzhPi1z6W6uBnwtUzTQZ14euZ9ICfpQETusij8PAv8t4n7TyveoBQ2YTFaSQGVKuKHhz6gCLEPStJWX3S-CXVu6nYOaEryOFfPPTCCCjDzPWMRkb0BUD2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rCDgKHh4j6a_SZ0xLIkqu640xpPWR3c1lTMKGLwjBjRrG_6CgzoV24Q-ukpx65GnLy5niN19LO3HROWfkWp5Wj9wg05q2QudTHwQc1Nj2lV4UC3SfcsLYJOy-5rHltrEmKDlKxwdL-jIeT3avhBENqELWRSopGX6912RKTyfAIJfFYKi8d-Pxtiwge2Q9mMPm0RdVPf-4ABrvVDvG4Epy2K301Tfd8OXiFu9TlIbyTseBlzRt-oGFucg3cS46fiidfB1JBmu_fEmB-8hvHbiW3a8iggeS9C_GLTZmJLgX_RVbyTtto8YjDN_At9VYQCVqwDVd_ypWsALnbYXmZ4NCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QiqsHrcdae14HmViGGk4oNsNYMMRH8AVFY8sE55_bHJvcQCbFsc1RaHatbnOWLPeHrQW6uERgH-LqW9FfAB-0pL_486deGg0MbT8A9YGkzbkI4ij8brauiZZfn_yr8LGm0G2MgEUpUvyypRuLtb8e5_rdYyHDNq8N7a8BVkMoaPb_EkSbQR4VWR-9k1Xa4LwF6z6xD3TSHt-aM15uELFUSDdK0nMgBc5ip8Nw9KqkWcjRB_KSI_Vit4mfrepAxVvuPv25Ggls4idTyKo6o1JxT02wMQJZpTenxwo5Cr1Hts3rXEeFhXNaBCYwQPjfhwARBbVPiV5X171suQ4Nx0GbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dri4-dFt9TiBab3k2DLPPPBlRoMT6HhTJPtLERi4ToUS5gsOVxysno8PwbTVgmt8KxptJL21xBsnukVxVyXJzjUka1PoLDDJh2S_DO-xjp--u-Vb3SJ6iqHnh2qKgVWaf-cBiufajAoLrX_ccLuzG8_jDqSQCeWiAytlCsVFMABDLEqbw9n9c60JrqvsS2tM47rltWtPMZiJJaCX8mSiiDOEEZzIOw1x3EF3rBogOvvFSoaytHMCOpmy-9Ke2KOeOUoCnW4OI4PVFoMFAkOg9HjWzgfYplrhfKOSpKyXmWs7VhsPUooHfqgyi6IajKQziNoxJMrLjsJXtxVsQ88IHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hJ6AwYeMdh2-ZcG29ioUckNuaEIKenLArb-jIko7_XP2XikCTxZy8KhN-WFacAPlNrYVWalsKeymSpFcL8-H0T_yXUWeAZPcEYNt6E99afbuSIW3PgAyxH3kpwG1WULCTE4QCAjfVDUm-4Fkp4Wdw2WOJgMSqtpYkF50mkcY7qx0Ee3LeccLqFlkdesF3yMhrBjVcZrep-CnArwGQ6Kee3g1RRd2ltD2DvcZD7JA7OznkBRMI-MK7EyQA3V6yk5ATGUE9-yI60PXe_CCwI3GfzrjHegFbsAzxhDvXK-uN2m0yLGl2GhtzvyKsqS9t-toSP3-ImcawkB39Dr8k2Fk3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aapOBHnNC8ilb2F59TYAtxvCiHto4kLxg-T5XwfGYMQjIlj-oC9mS7Ace_vreJRvRGB5tB7RcEnF_Fa30DVj_WyHR3nPF1qfwP89WTdMjzgZlRqFJ8xsNxXT6HdKn-m2ygr2y-FfhAnFep-YskDl4BqSe-7pekH6k5gt4Sy17pTq7wl2TASOoySGKMITjE3vplhdaIcdtyh1zaUbo0J_N8cz8tcKZJ_O-cg-KM5L1HqpfO3V3H41h7TlLD9Wa693GurLzDIMiJ_bPxmGCbTc9lj8Ckw1bcsMNaAlntUZ_Ghh0gLTH6cnFM9frf9SKJvfhIsg3O-Fqns1uQ0E0vZ_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpPGOFYT3Fu23WnBXZT3DdmO3FSF1OS4FF2kGD3X70TbORTBceHScXntc9gs90FOJcBj1ayKFHEpObHUiq2Lyl2rqaFittLI1sOrXau-42eHBWJioWljoiV7GvhSxkxeF-j0uFwwICd5W9zK0HJAXpkTm4txfugdfEBYOcV0g1TDYXhEtT_SOAPFdetq49JNq5viBlQuuIL47chVoL3BNKyJ67KTDMQWKrNShdLPIzIVUKYEX52exuCXc3eX4BLANf1neVpThZtFos1j8whIL3KsoM7fGeBJrxssFnNdLV_RjZTyB6etIDhX0Ah1sS13MM6zgCTuGOokd5hg5_Botw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=Eb27NRgqnlHIB3druv-GRDBIFejGYeLcL3G3j4HMRS_Vn6h8ffA9FDUM80WavcM238L6VKeXXdZqljVTA74CCm7GjNRuk3TQRlJg8phjRvxCHx_bHD3Q_TV0muNggnOeuavrb2GYV9QN8FeNm_Z2pq3y2YnMggaLzi0Oi7DriNXffamTHNNyRhBrfQU23JYL4MBz9eJhQnHtaujuSAwhwH5HnJ4GNhFN8PBDdTAa2br_5gi_ws_5yWugNr6jcPFzoE0IW8oLU9L14SnJPMP0ecJXu-GUNAXboW_bW29ZnECop2iBEZHc-sucsXyuiCP_XyCRTe1F021yezuPfPO-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=Eb27NRgqnlHIB3druv-GRDBIFejGYeLcL3G3j4HMRS_Vn6h8ffA9FDUM80WavcM238L6VKeXXdZqljVTA74CCm7GjNRuk3TQRlJg8phjRvxCHx_bHD3Q_TV0muNggnOeuavrb2GYV9QN8FeNm_Z2pq3y2YnMggaLzi0Oi7DriNXffamTHNNyRhBrfQU23JYL4MBz9eJhQnHtaujuSAwhwH5HnJ4GNhFN8PBDdTAa2br_5gi_ws_5yWugNr6jcPFzoE0IW8oLU9L14SnJPMP0ecJXu-GUNAXboW_bW29ZnECop2iBEZHc-sucsXyuiCP_XyCRTe1F021yezuPfPO-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cDDct-XtLP3GTXUYFXOnt8yj3N4Uc7KLFkzxh4tWnHSzT-RqicfUjkLRnwKVeP88lMD_tLAAPaq79i44KrkQ3Lq54WoHt5B7SD1MmZj0aNW6161DKWRXAb55GKULoOdGpYpCS7DEEAdwd3j_SCJOZ8gEpL3cXcu8fltMsvnCgCDHqpQx3wNbDNMWVHnCXjlF9hFe4rdX0m7WkcHKTKTWRXGj7BerkFWQnEvMnlwiWE0gSpE-u9z7h-w4gcxx9WyTvl9r3ngao-ey0cE0Y-od55041ocT8UFjnF2hZswDZ_3SniBmnPN76ukexJBwfewbelDMVjXHyV0mNEp2bbL9Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lNs0XdumXPaiqKLFwNu5gouIH7dHScIk6pRCAVdklQzB9RMP2LyHB4sxtu2bdvwIzDHMMTqMK-oFCqnS71k1fuF8kDq95nSGLfDX7rpjV8hUKCZaVhMi3JayNhk7Tlv1osoyUcw5uUrMkGmvC8LLmOBm0sem_r8lgjlspyo77OJh4_a1RLivJRqyZDPuJZMFQL6eo2i__jGmNUz2_7QvYcVAdfMcGjumAc1ru29RlLqOmIp0KwcJPKdope3bT7x2nq4kck9Or9Zr6NQciCDrybqjFIIGUTJvtFGFxu-EBWbDql9M8kfVqPznpERDPWEhz053ZJrTIh0JZ3ZMTDoXoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TvGyhs3V2t7pTqYNlmELmnSKHFUbH9rPlpEdFWFULcPpxCvdGATaviQeCC5SO05oLyQnKh2bF3G7ZmXu7jWvbgol_zeBpParQHk2d5oxfnDG_VNQxUrdukfyLrE5ewuprZC1yifxOuzk6fcNAuOZl-rYn0zxCNwONj6jXVAV-V2e4nUUg7KiY6VI15CJasA1BWfaiQsZaJ6x1Hi6YEWCTmUtkVxMXV9e6rwOzhlDgdt6q6U_3q-EVor3ijXc2qTlu6kI_3I3r5IVgyIYL6NC8J2rC5-g390ZyK1jrSxOdt5gdpAXr860ZzxWR0N6mg4XD26KDlFGbuRZmpdYE1anxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AL-AhYPV_pr0jUvD-O3xRrZlVc6T1XQgzJtTRr4Adpkkj4RJrJvJaUO9nZkA-7sKNgl1ualYEpwoGjMtZzvi0uFWtXF94as1x6CKqiO2kmRWLnkm4Lz650L7k1EBNWTLpnnULyoGYtg4Yx16DSqm-W5wHplQXj2V-7jjWbtNQZVD_O8GvuWZ8aMT0zOpTtFbm9yDCaCCuWjhZmZ7j50Cz_vlqJv4wFDBXSEp5DS0mNO1D3-s6s8SGwTSwl5Whp0E6WrFMibPMqY0IOuyRBCWyfvmjDz7xTxqHKoUririscRpirxq9djlnjAo0L1eXz72A7L_OTK7OwUkIC72e3lq1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a0mesFfMsbj_MFvRtSlOw0s-5g-TmYvG9oaVYQfqYaXDI8S0BZkCe9eEjokIvk4-sxyHn7iBTezGO0jO9lEyF5B9H0HLkvpqBoLXaURQNt0wWOS4ziX_6q6LcwFe4CocSI_wQLwqEp40FX7VRUqK536_P3pFhjBKCtm71OfV9Q4pBAylZ7-vWyPwjAZijTaRRdsqbC4o3JYvdG14_MDXzjVG_eyPcb_Hmihqgl7sJDFClwCLc0mtdgZhhWYWxfcc3bZiXikAsIOAK78yOPtOYNCShioTb0MDtzoLfS2qaG4m1iy76zssvvoZRnnbnv_BwcubTENi02sFo9aRbi1BMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hg_fDeEM114J_8v6dADCavIsHu1gO0RksMjnammnWpN4-4hDHvSaeabty9XoDFf3cnwo5qUojGwsc45gPTai_U5_bIyR4JWbFmdEptsv7DqYijWxSTLsBe4awFojCybwsVdqfVlf2rrtlQfENTf9MJhRC59vmVB79C77kI3hOIL-2D0VdxlxkFmPS5RfnEYDjaph3GaAAwbAol9k1od0brG7Pg3hkhjgMd19hE7XrsLQOLMDaway1aP_YxKCFoMTyQ7412FeCsFaJO7B3QZLi6vp-DQPnNEG5CVBN6FPMqaVGr6HDF2ganZr9SIfZ0zfMWlT-WxakrfcDJ02iwR8wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=kl-ov8H_1TMhdPKU1x4i3uURRujrSJ2vbMqM2AgCj-2_ovEkOPeXpanowXmiHfK9Tx4xKbjnzmWcN3yYdj9wIp8X5b1u8FCpkPf9DcEFNIC88aPBazIxDqR7-Zjh4uBKyWOM0FKLrAIv7MMFlyzpKLOlzpGpdh4ymYRtKPJZH4K_BF-q4dPxEIuOtGbldAex4Mh9nn_UgKvG5dEvNsGSGBgPHfaHUIHNwW3vxjhw3nU3UkPe98HjVY1TStdmJBIglogmFMv_bg9rRYCw9V6k0v0t-ktA90TV6g92wzZtknSz4EpS9zgQ5hDV15TqKCN_ihZAKetbBLHIFe-8mrrvng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=kl-ov8H_1TMhdPKU1x4i3uURRujrSJ2vbMqM2AgCj-2_ovEkOPeXpanowXmiHfK9Tx4xKbjnzmWcN3yYdj9wIp8X5b1u8FCpkPf9DcEFNIC88aPBazIxDqR7-Zjh4uBKyWOM0FKLrAIv7MMFlyzpKLOlzpGpdh4ymYRtKPJZH4K_BF-q4dPxEIuOtGbldAex4Mh9nn_UgKvG5dEvNsGSGBgPHfaHUIHNwW3vxjhw3nU3UkPe98HjVY1TStdmJBIglogmFMv_bg9rRYCw9V6k0v0t-ktA90TV6g92wzZtknSz4EpS9zgQ5hDV15TqKCN_ihZAKetbBLHIFe-8mrrvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sGUQIMxXTUMqnmt2EpcahKQGAFdE_Jbd3Ne-l7ojiq7C8Lv8SCjThH3NICZhEYCCSKrSqHJ6uKW6wwtf7_mAq_GbwdYrW_O7aqF7K1aspJn4xK3xy3WfZXOg8ThZB_E-JXUgL4VP4EK7JGY6dsafCPuZ8VGN5Y18xzxWmDIuG_fd07LjnyjBCkfqTq6y-3l3b1usbW8dCZVN_45zjSq61W4Q0sDcoxl9aNECJ_kf5T0K3Zz-zmdK-DJh5kgJwhXtGLGBJemaEY1L-hbgA-ucVRh1l9lsc2PW4UZffNlVMi3-xhSZ0dv0jIDZbzugldrCXFSZDCIIyUx0gsJx9d55AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=H8b2MVd0zJ8qrtB34Qg8YKC9jDSIb5sKASqXwuPkJX_oUe2S_TnF3YA0s9zS-tV8uABXrDgWFSaXB511K1yX8-g44wk5rDE5VJ2F2TNenRigpRPxHj4PRg-NLfiFbuWAV7eYYXpzBj8GU-u8WXMyRQl_H6O8ei08OZz0ZNpubZ1ME3a0ZqrR4M16XXeiKdsL4QOlsYkCsqRw12Yj2znHWMnwfNtZVCjburE47I_Oas3eOa-O5PSq9gsp_P0-QC-V6KHtHt29FkarocXdIUFOYN-fUa0yaJGFKZZlcQfOkbt9pzCgDltFqt4z52b_h5F6L-RWjYy-OTAplnsAUZEOBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=H8b2MVd0zJ8qrtB34Qg8YKC9jDSIb5sKASqXwuPkJX_oUe2S_TnF3YA0s9zS-tV8uABXrDgWFSaXB511K1yX8-g44wk5rDE5VJ2F2TNenRigpRPxHj4PRg-NLfiFbuWAV7eYYXpzBj8GU-u8WXMyRQl_H6O8ei08OZz0ZNpubZ1ME3a0ZqrR4M16XXeiKdsL4QOlsYkCsqRw12Yj2znHWMnwfNtZVCjburE47I_Oas3eOa-O5PSq9gsp_P0-QC-V6KHtHt29FkarocXdIUFOYN-fUa0yaJGFKZZlcQfOkbt9pzCgDltFqt4z52b_h5F6L-RWjYy-OTAplnsAUZEOBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGu6OmLGnOlodg8xcOph4wYApyvrXsJINsKSXap6K3DXShne201hawuhXNFD_HOvwwEkB1V8IKuswdKWkN2uDgBOzU8KQpsbc8ExMi85G0xj00wxqKJ5vaycski-156k8rtCFPz1604HBim2lv6IecEXKZDGRV8OBJDpmf2e3u_kOX4h43qcrqzk7MXmijL7rUwAlFBHYCdrwVG8WwMd_4awP7t-wFQy_3mvV1ujknwKcWy8rcJ3aNR_Z_3zLCuWhCKwMhCLunRo6df4vBUmVNLKDOFVGCU9AI6FHdDCzBPsGDR99Q8JbtLYsBIWhNKs6oaRILXUU7B5bSTfYRUsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_xaZ2KP9JcP1IdrpZUnhaSv8SovrWryCQdZEb_7G7UKdfMgNeHX5XX3SvF02-nnknx3TbZ335urauE5c-wkpIfzaEbbT1pFG35J-12352psTa3I6cqZ5AgAvC7nCLn3J9KR96O6rQXJnoESxsHfX9UbZU05Bb0Z2uYTSBdr2-uIELEzXdIP9F3HAcDFSLJgQHizr62xmkOXAyTEZfww4C__5mw-SKwGtjuiOuHzPKwbvbvBSkg2odYzuG2fSKBjJ5UCVnznttp0gLd03iE5cGUHK8fwo_XpaXJWAPhiufXfxi0vxYjFkHPT1KGQIKnjOj8Y58qDnZgXBSN5UF1btg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijljZyRt-Gea_L16poI3PpRAlqgkTgcJkXBf3dT1E6oNBqzRZcpQ4YzvqceAVMKauihwx-ejK9xLnLVqbg9yuaMJkgtcDznaYI2QOvnVAyX5e6It11dI-bchK2BDFUwwIF3rj_fPuPwM9Y0eiSfc-Yoa7dYbhhDdHZyhuayysMK6Osl0m7qEejV8rNJO4g2Jvft7zOPJyu8mkUaJpyEqSZrn61teS8ANxmJcZtMLmTWfS3G5a7VKL1uPXndE8gwKEsFOZPLdjMD-zkfjeRFzGjRk8_i5vbzjkTEKBFtPtZj5geDuNki7oPzHosnZW6g6ZePwL_Ji3FcfGRYdNZ0uuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRurstPjYimkoWfFpT3gzAwe2RcRF4oLH1TcMRNLEsGvcAU9ZJ_TUJZzI4RBGiLJxp91pQx0UdggARNE2ZRfpf8UgUs3_qfgE94ktBpIgeGhcP964W2MCkvxJXbhESTzkwq2A9gZtBdoI93ihLWtFZIKsZszvw_oKneK4PbFsaK5EYIPARrbDmDxL0F4SD0sJuqoV5ApTtdEKbaQOy2wZSbB6_MPWpDlp-yy_NxUjbHbcty0IZZvqTkQEi4oMf4_4pH1gCWyy7fMTAMogsJz-7b37ZKsO00HCbnw7pYCYe5pHS6AKZuAtPhXk5GB8GTXkZHlgz6iLhrazXk5hZBldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kXg61VZ74acftTDlpcm9QFElmk8lQAgm4Dbcg7n4-DYuJ2P0Y3beiJLtE544vJoUggOJ8MFZQmSaz111XEVVPStg7pRoe-L0a_kL0Q2jkkvA5znCCFevANrDuG28mJLpdU4eqUx3jBUOODkvVa4MdGwE3Q-WWtFmVW4wykHAnU1-OVFRahhna0pq0mJULp6fBrIj9By6LlfiujBH4u3uo6xtOXfkcB6XpDDhufB9UwirvmL1O_O9CneiCnc-r7Rb9MdyytIu6lTrMStyKoVM1w2_PwjeyneViZtmTECPfFsIjV9ghFPZkUz0ojYF8m43PJoG6hq81Hlh694W6T-s_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=qRK-CbwzXTbz4gr92uc8Uez582Q825mCnnXJgVgTCogVoay-koRkKdC5ZHcPYJjcm2IiXs8nSQGsXBsN3SOeWdjf2vSQPSNbR56f0KkgqcaifEFPJfb6kuo6clyV2OZjS42Wn_ucbD07Wc2MVvRfFWW37JZui7b8shh7QC1ubWsJvCidwqBscNja8xu9tD6VCofdmaBsTH5N-lwp-jVYpElpwgd9_Ah3tOoCCDe8XWzT9S4uOYuSpoz15gUsB_I5rwi0ghNtcFflblKhnYqC6pHUz_JBM4OnYs9U5MkW4B-SvS7W5hxLcDf9ETiqfIy5DBncki_VYn3r5t5fdJvZqhrSO6HJCXsHEYQqCQ01_Qr1-oDvpa04Zf87gxsFGw7wdj2PTburI7JI7-NiU08wLe4TY2871bTnwY182quhD7UGDl-CpgPHZ6LAEZlR1T1hH5kEIKVfq4dmthXPlRCcvTN4t3k6sYdP8io-NCrtHBixp34puWKslJjxtFzRanZwD2hF767k_Ie8bzc1s8iz8u9EpHcmUYjngM1h5hvxvMWoa3JMiieSec4A2hgCyCDAlh21BYGh98sOrAEVuaLtqPDxypqq5pql5EsoVc8Y7lwKaLdiwlW14hX61sxe9A-u6HzegWeuNwNsOSVSKgNQ0hmkpeI0ajbmP7lCRsKQVYs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=qRK-CbwzXTbz4gr92uc8Uez582Q825mCnnXJgVgTCogVoay-koRkKdC5ZHcPYJjcm2IiXs8nSQGsXBsN3SOeWdjf2vSQPSNbR56f0KkgqcaifEFPJfb6kuo6clyV2OZjS42Wn_ucbD07Wc2MVvRfFWW37JZui7b8shh7QC1ubWsJvCidwqBscNja8xu9tD6VCofdmaBsTH5N-lwp-jVYpElpwgd9_Ah3tOoCCDe8XWzT9S4uOYuSpoz15gUsB_I5rwi0ghNtcFflblKhnYqC6pHUz_JBM4OnYs9U5MkW4B-SvS7W5hxLcDf9ETiqfIy5DBncki_VYn3r5t5fdJvZqhrSO6HJCXsHEYQqCQ01_Qr1-oDvpa04Zf87gxsFGw7wdj2PTburI7JI7-NiU08wLe4TY2871bTnwY182quhD7UGDl-CpgPHZ6LAEZlR1T1hH5kEIKVfq4dmthXPlRCcvTN4t3k6sYdP8io-NCrtHBixp34puWKslJjxtFzRanZwD2hF767k_Ie8bzc1s8iz8u9EpHcmUYjngM1h5hvxvMWoa3JMiieSec4A2hgCyCDAlh21BYGh98sOrAEVuaLtqPDxypqq5pql5EsoVc8Y7lwKaLdiwlW14hX61sxe9A-u6HzegWeuNwNsOSVSKgNQ0hmkpeI0ajbmP7lCRsKQVYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3okoglNWK6mwTcNxx4WLTumrIFDHxaQnPqDsKF0lblWHlQZ5U-W32GRL7HwtNvXCgu_Qq-UW-g-6YS81fgHYHEk9xDmYIK5jisSjHPyQAY6jPEOqAONL3cOqFh1NXQ9F4O0PWx2Q2jhtRIwfpPpL71S9XrL1GWoY8Crulu4zutA93DOY7J7viob4pCMF2ZlS7n7gLD9zS8e-lTovoVxZ_bkPjOOsaTxPgkDw8snbeR5A6_SkGaX_Ov9yYVIcBxnUWKXO4Baryuy2otmEE1-BD4c_uSSygUL8BbHUkoL_gAgNXnL_Tu1ML-cRtDH1SlSGtgckSbkEt6qkBTUVerTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=Hsuth6daWQUJJCOOVrp7cPbvTkMC055F1oFVeVCaUZOySn0Dj279POZkUWViOZlHAJUBy0t4S_fxHX0oP2rURR2ZBu1Bo9b974nCnYUDC__lPN-jqkHHxmvRqrFu4WuU67oLQb-lqiwPscInIGAzZAIVUCvAzvOq7_BxXLV_eY9Ksax2x_jMI3WRfnhfB6JKBAD6rf6KkxWpbvtpNDFTwxDTfPV03s0bqFpQGY8hOlB5qKem7fHkkZ6G2xzHmbrNZeSBGm0YOKXtq3Puw2StJjv4HGJlsZT9B5m-AsBiikpJne_oApCMSDVFmREucspWHZwqx9kSpCxFxjHEZV02-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=Hsuth6daWQUJJCOOVrp7cPbvTkMC055F1oFVeVCaUZOySn0Dj279POZkUWViOZlHAJUBy0t4S_fxHX0oP2rURR2ZBu1Bo9b974nCnYUDC__lPN-jqkHHxmvRqrFu4WuU67oLQb-lqiwPscInIGAzZAIVUCvAzvOq7_BxXLV_eY9Ksax2x_jMI3WRfnhfB6JKBAD6rf6KkxWpbvtpNDFTwxDTfPV03s0bqFpQGY8hOlB5qKem7fHkkZ6G2xzHmbrNZeSBGm0YOKXtq3Puw2StJjv4HGJlsZT9B5m-AsBiikpJne_oApCMSDVFmREucspWHZwqx9kSpCxFxjHEZV02-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=XaBwH6yrdxcxH5ZNVdTpB6S23R8cTOWlhvtHkrm8cmc4gSPXn-Lp1MWzoQPZwhFnipGru0VCRyFxuVMjk9JUsVGA30J-b4S65cg3qBuykIq6bJt2iHKhwk8hLYM7OI9dwb4lfRhMy5rsdA8GIz3ZCdsWc7edjUAYwMSDeRJ_Mao9FD9kPtuOMhxyDO_YqYZeLpYk5T1SVVAHlAsGnHE8ZyjWZO9s4blMI5jWqD2AgHx0hnLEYA6AqBLxn4A27pNtHuhyyEtlB03oigr01r4iZUHNuwq5GM_DVnJk6k-qjF1qmWxb_XEskAxp3YPTNWvsW6GOWFObI8KCKxUcbue6Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=XaBwH6yrdxcxH5ZNVdTpB6S23R8cTOWlhvtHkrm8cmc4gSPXn-Lp1MWzoQPZwhFnipGru0VCRyFxuVMjk9JUsVGA30J-b4S65cg3qBuykIq6bJt2iHKhwk8hLYM7OI9dwb4lfRhMy5rsdA8GIz3ZCdsWc7edjUAYwMSDeRJ_Mao9FD9kPtuOMhxyDO_YqYZeLpYk5T1SVVAHlAsGnHE8ZyjWZO9s4blMI5jWqD2AgHx0hnLEYA6AqBLxn4A27pNtHuhyyEtlB03oigr01r4iZUHNuwq5GM_DVnJk6k-qjF1qmWxb_XEskAxp3YPTNWvsW6GOWFObI8KCKxUcbue6Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=Rk93BOnROMUZXLUkGecpmD-wvtXSIWJSHEpEjm2C5O9z1WYKL1krij-c--gxLZEmLja6vdQir4QvND74GSWJ5YrE9GuRBRRsh97Qhr2fZATYs2vfLVgl3FTBW0gAar_KE13XVDXe5rKIX26_0Fa4iPtTZ_83JtvsP54_2r5T5tk_MNCZM6jVTiNuD_JwiLLNaqJPDx_7PAIAsZhn903KhiBB5HSqR9R9iPBbYbLK5tE0EGBURP1fmE2FzVMH6LARlSOKy6AeRuZorSo6Z2toMnZFosPziR4y8nqEA59Oyq23mfGZAYcJaV7FlGZ4pPeXg_j1sz4oM368zMKLha5QoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=Rk93BOnROMUZXLUkGecpmD-wvtXSIWJSHEpEjm2C5O9z1WYKL1krij-c--gxLZEmLja6vdQir4QvND74GSWJ5YrE9GuRBRRsh97Qhr2fZATYs2vfLVgl3FTBW0gAar_KE13XVDXe5rKIX26_0Fa4iPtTZ_83JtvsP54_2r5T5tk_MNCZM6jVTiNuD_JwiLLNaqJPDx_7PAIAsZhn903KhiBB5HSqR9R9iPBbYbLK5tE0EGBURP1fmE2FzVMH6LARlSOKy6AeRuZorSo6Z2toMnZFosPziR4y8nqEA59Oyq23mfGZAYcJaV7FlGZ4pPeXg_j1sz4oM368zMKLha5QoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=UpKrdUETbAs7mJH1NwflfCHFuSbRWT-j5raSmR89CIgaSYKVEzq00edgjUW2kFrc4vRWxt541UPwYcmcbvYRlWCI05HyoMNq2VVACtw5CpAIxdKdvvPlRrp4iE8JW27nTvYdTm885YIrHuyu2ettvIGkOibD9YZUyJ-ASNr-bpVY5RtYmXVnNRJALfLsikQYbV4tPD4Fgo4kgN5iqayR0QGu6IsgnxJDMX78Ruq8ITlmiLuAtxZ212Hw3ngPIaKYTqmK8Ds9zL_xpr4aZq9uqdT75t0vZVg6Mno-Ncc4Ax_NQxvl2DJUayW4avccx8S-eW2e8VTNe2B_ovNApF8_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=UpKrdUETbAs7mJH1NwflfCHFuSbRWT-j5raSmR89CIgaSYKVEzq00edgjUW2kFrc4vRWxt541UPwYcmcbvYRlWCI05HyoMNq2VVACtw5CpAIxdKdvvPlRrp4iE8JW27nTvYdTm885YIrHuyu2ettvIGkOibD9YZUyJ-ASNr-bpVY5RtYmXVnNRJALfLsikQYbV4tPD4Fgo4kgN5iqayR0QGu6IsgnxJDMX78Ruq8ITlmiLuAtxZ212Hw3ngPIaKYTqmK8Ds9zL_xpr4aZq9uqdT75t0vZVg6Mno-Ncc4Ax_NQxvl2DJUayW4avccx8S-eW2e8VTNe2B_ovNApF8_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC5Ajhp-uzn24lxpJ6k5b0MZJL1m2KSP4wPi5bGGySrpWLnZWNBhr6r_xXIYK1uhFrFZWk_1zK0PCEYs3EfvSy_sc91JZhr5II2odemjcdcNMuf0qgWtBmV17T-TpjsH_0PAGqPOlf5g6nqbv3PMbkoOWRQ0vvDA2nIyx7lg7i3_CG9YlFBSNR8Hc3mjA7iM3TKXTmctX76QTGw-ASvjs-EDN5pFPyC6N38RhwILZFNuh3xSmjbivwMt82pg-WuGkIVHlYx9I3EdUkQCsXumvHFS2eJhAneTep7WiAT7f652sg-riRbiTXHvdzUEoe6Da1Lise9VecxjtodtE3k2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS8pZwOowWBXZqY9joCRprnmucPWzui_qFwG8qkn0T4QK3mh09e4DrZjlhQDBatbiw7JQpehYhpM-YDUa1o22dc_t7bJbu3-SHY26cHpn73dXInANFS6diKsoqKvSZZzZFDWArVSjBYIPh6R3ZeoHxz9TCZpRyybEqRTsemMRntBR3DwgH2HWYOgZuXeYt4Y5z2-SpN-jDoj_7lqq4TQQmeTec7c9j3Xi8gsxRFF7oeGo2_ft8hW9XCI3wIkNHC6FxDM_qrMLvrTurjRV5zZ0KzrJ3jO75EGC53PmiFU7Vc2th5AQ5OkNwAsrLpB4-7XlOde8zwOcyF3Ysb3gf15cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPkMHw73PxW1NSUazrESjhWyvX3FUjhxcuUnOaPOMxILmNTc_tHeER3DRZR0N3IDEa1t_FAAsVOKM0hVqoO8aoSFx4IMj0bHRZElcU7BkcI4QU6wHB_viDEuIsZSAag5MOVmHcF1K0I6mIDDylCjjEInsTGNUHbgIlfKVHCYrSs0i7SxJIzExC-WETSbf98nWJpIRl8ln4_Ub6923plYLnqYI4WKui8AUNwjzxc2rCd7Ag7Yr3eUxgdxpjVLH8f4Sgib7nT7-VLBjiEsbQqiqHKI9DeqOS5ElpoQ7Un9NkAY2yFnECth6ln8AVAgejOk_I1K463Wgf3AEtvGWOW6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1ZkdZ6bHDfoeuDtvfJVyesNDL2O3eKfRFr1N3HJvZL-m00BXz2JWx6xeJuCp9pGRlU7xKSItpI01Uv0aLDVTaf-Vps0fB5v6UNGOmYIy2qd_0cPtfyiYe-GMfuvEJu2eLEDlpkTcmJAopMuVf0FrrzVMS-E6YGaM5S2eAcOShnxcHSVz1_t1nZy_KX0bOHudf_p7ev4KIkR_AE85dJhMvvgtnp99pruY96-rcWDGgL5WQyDA2Pn07aXdS2akyzSjGgCjEhzJkwrGbbV2Lwe8kTWQ0JlVdRA_xQCHDEsu1xl6UUbqfNEMvKEBGcour3084HljOKF2IkgTYB6BF5mtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zcds6EyBPsoYsEP_mpQXq31G7lEe4PMQSdr-uUK8KltyDQN2EfSKtH-JR2AUqfqwtUxRKYcwFeC7tcYBEGR_KbavocObwm_ehn4b_gF-58W8WFQhXVO0ZukFGCV0EKt9ebO3gwk_g_KhQ2xdHmgOR0_vBFBBqtQFERrHMatTLY7cAIdaKa9btMYLdWb5LHQacycTCTLn8bTIAjZNLPElRLKAFfI4lica0_KAlaD07AHbooj0Dzs1T50sgHpQppkSjoIEmqXBK7iwGCQwIrUHKwu2P78NeIImtln-hqR0xx9osBmaLB2zsByBacVfDXxtfvdcE2GGrydO13D8yyocKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiMxsDjZZ1Kw7Kzwj67jOFzOnlgkmusjk8cUYgY0m5yRqhAefp2L3zOtQZ2E4yFPI1t2sjR9YjoPuzhx-alhzaNO5aX0rxmqdhSMP2BBSEK_UIZRz18bZuGo4QzkZw4x6yWwLMydUTDdIMf0gNcqOsOXer6D-UrKSxD1lVKWt-OrLPLmLWc-fUuWLHpSYMVz2QVLggNLhKCGgkub62OCONRpW8cQvmt4IBm9QIgpxLpa1MkawM_PIp5sJMGM8u6ovC95BQrIBQqUEQ4VdkjK4n6diKvnhisy-J_Ih1aotWyPPwALI6JM0Nwghq_p8CWmQJaJ7_Eb4iO-R0AQv-sAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BR1AySHS6laixGdks-XJJ_7buhtXC9yd58BXWXMTrmfacM9uGFbQzZwy82QsGP72ENJAMrDMozEvSRokJHgZ_n60XdPugZPQiG_1zvDuS84aV-A24OIOTGlueHlG5kko1BQXJQWxCJJTX3B_zZXItXE_CArj9bFS2y0KqcyX9L76bGyEUGhJvFeqkSDNGxmGd8B9NSIpOc50sAoXgI5vqGFCcARXMqrfISB0D2_tMOLcGfql3GBOq__akS4-w-2ySJGzjJcC78Mpn-dI3VkPgooFmYrowd8XtfqJuTzFDRmmuOFrupA9gFIw5r87xRYUkL8KjZIEqEFrGMBT3GICRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNqEvqGwublKKaEmvAnEmhHZCARxpXUYzu4E18ydDcnjrNrykKl4EE-Dl01YjYG6HIzN0JozZh90-8u8HX4SwRiPQrEoeHPFSOwLVUPiMrXPz-wkJ_JJu-iwd5_y9RhuqKJUibeO3a6HR9mr8v5JqFVfiksiFjrlpySJx2IidL1h_0q4TeZioP1THvRqoziZRRRfcL70Zj5gJ7N5wXteBQdVPfqIW0YKMAUFBSnK9kLoj3Ir4uwwV6O-vr6ES5LWNE279OSKYz45fqdB08UINahyM68z9AjcsKURcZibmLYXJdL6vDANwXqrKiRB1oebqZvcKTYHt579dU9Z6KiM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLf-xdGESCjbbbMjMROADkspIi2xUWxqbFUM4wL-RfNBq5T2xWTU7IJLOpzkeZK0gMevYJ40mV42vo1XsKgo4-RtzcU1J1O5qyTmJQO91yIQDB9_nPGjHxu-4b8hhEmwmrq6CLHQ0-DTgAyCzQLTvUKpKlqapszlQDkqYL3cvo9wMpjv5jADDASX0umFFlLckKFnW0iSv1zlGgqNL2XQeaExQB_ENLKDoTIPwAB6gOzzp4r5_bI1BtePcia2i2Hwvs8XQnExBt_em1d2mscNjA7vDowF7VdXrLlVt4QFrmBiztV3FXK1GWNXHIKjg7f0K3CCYEL87FJXlTZxr0CycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjEZ3Nrt-oeIO-A7uCJpY2Q0zU1cTK56M9QmV9cIYyuf4pUdlVImF7AW5RNTzIXgn51BrcTdi9tzDzPkltNu-fnxf46dAV-emz_QvC7uhDvdeiP2Qkc15U4hAkB-KLPTQaE1UCfcKRq6-J9LXzBzGqeq-QoOJFWXwKYY0X6l6IKjDw-R1noHlH8nbWL3_dTlLOjooeiWfz5lDIzi0DGHE-nZF6P-Trw1QRajseC-_qcH_-04dQZfnexkZ22kHaaWCDXfrqK-46Y6R61yCC6TXvea0Wemapfos7jbObJZgS4S9D5Y_EPVbhERgNsf3xBCqjEnnRyTkN-e-RMEIHFIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ob3RCddogKivZ01Iw6QaGPZEbdRU8hHDhUjbpT9MiclSHB7Qhw_o8ipsGxc7QlCt5YEFQYFSbyw-h17dXiYW_bGMoHTL_BJJOj6r7ZTfEKcm3OuyuGBlu9tpd0Z5y9LF2hGFPBal0-dNuc-A7yeE2l67pQqNIwiT9WPAnM4NyVHJer7PIDN_bTk7O_zA8_C4leR8PTAA4-_48LfzC1Ur0T8fuiTz-hRF5BE5bGJfhZtlmms3OR0L4s4-Gokj6H-WkaLrufdXB98VNovn-uQk4hL_B0LspN58yCf6L8Vw7cMMNBSQr_2ieO-DQW9kdQJxbPHJ2Iav1do6-7cxV7F9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErNnvfcbecZFgSUg15MFShsrg9VLcJBF1-TTzQphqC61nFm1FYcjw8eFmFMHnDdLzbBqYeLQ3th7LFxD1x0mToTj-JWiddEUTiWVTmhbNA7eU8IFPEq44xlhiPu8L04NTg3ZpUZkgu1AhY9HjVBounYnmSjKTtBswT2Pjqm1k5CFumWcFiZdEtiaLoHEXJdRWECcshhVze_z7NFSHTcufBs32KyxMY-YW224934vkCaeDhkY68uUWOEKu8sUaQiusS0s2B4E2_3NIDfU6_eEpfCv0VzK6RqysBL86bPz3hvyn7-QenHsw7AZj3sJxBEt8Ma-ZZaCp0L7ZTDtfH27rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/beSpP_bdGPZ2ssfAIX5yk6Vbx3ePLA-VfaUMZwFN1Jfu0oTG0E8ZPwK_BuO0C-YB4Tsia-y0zvhLG3JmNr4V5DWiMDRPD92bxP3wAXXfajCC_knaw_mbIwEQQH536TtGP2Qi1Hl18D8-314t12I6SBqRmWcy1Qx0v4ejK2VWYMCYYrlALuBfhHljQPM_1rWN2U9M-6mz7n4UcokiMpguEJoQjkh0OY80Yc02E9uY9yC6k_eH_q3aIc3IUHBKCHD_lelxcJW6xbrXb8eteiPbCUY5-1KYpY9c7CCTkHIgNijKEVNpfwmuilH7b2F9TABkoKlUHnyIGI1XHrdvNj36yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1HPGJCKc3yvRwrHTzYZLsi6IMtiUDLXfgFasa2j4DLoZzH03Qjv3rKjDT8wRPKbUdgXsIbZd8dCUyuay1Q3rp9smiFv5fWNje0UDFnpbCacWLbAJkATChOrTBA4KlnwaKFJzNHScMTTY3naIKZmuxsUiAI67apcr1hPtLRTIh3H5kI9C0HnPgU7NyLeKQlc2RR3t11lctBaDl4fBvIrB0ELiFhernln0Kv2-L05yZn8gh96SHw5OvksEiTJOVTKvt5sH3l3jmdwDwdX6BPNofKrcg_uuE3TVeq7Xq0ucgdZ3XPEil6U31S6e8MCnKZY2qYya6KKW2LVbWgztVnPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K7XKH-S8Hcy1cYFuBeK7-VGbd8Ao7BKKgEyDodWKTYsA4APZ-V3og3dSueDi1s17nKaLBF82J1W2qWxkPQY-AcRBC1RXdodN2ZZaazuX_KG0bzRa_Nzoq8K-l5Sd1F-3bSAzR61fDSC5mCu3Zfw3YlThcq4zQV35eh_rpUWPpXclZeVrljibNfiGvR2reqz8Z0pSXsQrSUnIiErAeDA863_9J5Snmz6vUsVYaA_oXSCzaxg0G3n4DEZ3iDc9_aKBNhXaoUvbybaS5RjsJ-iljqY4jy-uvoRBwyZtk-8WisTLKkdcCQVjMz0RYm3eVfIQSBe2vZ6RplSYGCEc3XhYuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=CPiXGKsGorJyM17rA1FM_ScBbG2DAa0bMrUOdrAkB9gywwfe2xpdU8Yss9Z_KeesKNRu_KOO1IGCVENUb_MCAPLQFzgjz5gJsMTF3JsKMp7eef6bg7uRculzNan9EMH7HLIbtsDH1wNBEPC3plgZyJja6wRTlv5YaiRJEEouISh4Qz1MAnwl9UZ8Oka9AHxXiX8zX0V_vmJLOaTHGUD-pTlKDel8XW2NW9w7Cn4XjT0a47U_LQ2c4BhUMAp9Wunp8I9kGzIJY0Sq7DXyS_CgbtbBiI-jupAUtl1vFdfBuicqLinBlcWFny3x8UmYidNa8P_CernBmiACRVHVECOnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=CPiXGKsGorJyM17rA1FM_ScBbG2DAa0bMrUOdrAkB9gywwfe2xpdU8Yss9Z_KeesKNRu_KOO1IGCVENUb_MCAPLQFzgjz5gJsMTF3JsKMp7eef6bg7uRculzNan9EMH7HLIbtsDH1wNBEPC3plgZyJja6wRTlv5YaiRJEEouISh4Qz1MAnwl9UZ8Oka9AHxXiX8zX0V_vmJLOaTHGUD-pTlKDel8XW2NW9w7Cn4XjT0a47U_LQ2c4BhUMAp9Wunp8I9kGzIJY0Sq7DXyS_CgbtbBiI-jupAUtl1vFdfBuicqLinBlcWFny3x8UmYidNa8P_CernBmiACRVHVECOnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ua8od5V9ld0ZOO0OXZxgtBkWcMSGJ0ZEBfWB5Irb-6XtTrfIwMr18vJ3KZX43q24lUv_Oz_IIXN9lXYSPy3ljL1JWnOdg4tZbjHeeycai0uZvJTc9Z369rTw4nkIcl4FkDbZWsY0eeCWXoFbfRCKaxMV_T89X57Ris5Mx7VFJww3SXPQlWcle2YKaUgGYkxsEZbQZm6otuk2WBoLrpDAyRQL83C_bX8TAvtLzRzs5OepK8IgUNxOFDCb26nGfaFZfPeslkbM08IHG3bVOZeCRP3_jgotnQb1hEcHygagtCFa3acW9nCYOojb38wDui1yi0wGjOLLmN65TF14tYEkUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SX1YAFbpkOJAwZVgvJH2Hg1yy08d2kV0zA6ym_FaYbic12zO68eEuvmqci9QXAcD5eUfhSnLzmMI1oIeudbKUr6VX_OmnCOng8MvwJoBUI6OkRzpxEWKiy6tlEycVQyIhKcO17BlIddkpwlTk6DoSTNBgRTGpHS0jezBMmSGgmxJeNeSn6QiUmY6DWKZMNrGJ0V4pDFJJxUXVPwcnywHONNd0kSf_L_XilVVCgKDJnwqNo9AvnYpqFaye9sTn9TLPuu-5iLDDmHeUy_f0jDrOAwFUzfcQTlqqzwFAjm9EqSieEEAPgexP75KOG2j80YbpowwLhz7YhqT1-U6qyUWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=EwXWLjBIBPLxDGcij4mOSEZbSr3LF2zLo2HVmkC0FiVRWqbULsPZojZ3vOx4keOOD0I3CkJ_69p1RVUIC_sl0Cl8DxE9r7ftpbUecSmkVOjG-TtcQakZmfBNqfUUJmQUCceIRuOPIpvny__q4OrblrtNzk4SZsKBWRSuYFxgrgqrtzWtMmm3vHNH6X3k5hLd2X0yJ1GM0KOf4QsGJx0YBa1-qhO53va5LHltpHliFMiS0dF2an2Z6S0CEOiu7i3AqviaMgAUE40Ew3q58bAQGNrNJuiVdCDjdn7-mDgaflTR5Kn3Jzfj3550FqROeYAuY0s4BpnZTOQQjq-MScEcTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=EwXWLjBIBPLxDGcij4mOSEZbSr3LF2zLo2HVmkC0FiVRWqbULsPZojZ3vOx4keOOD0I3CkJ_69p1RVUIC_sl0Cl8DxE9r7ftpbUecSmkVOjG-TtcQakZmfBNqfUUJmQUCceIRuOPIpvny__q4OrblrtNzk4SZsKBWRSuYFxgrgqrtzWtMmm3vHNH6X3k5hLd2X0yJ1GM0KOf4QsGJx0YBa1-qhO53va5LHltpHliFMiS0dF2an2Z6S0CEOiu7i3AqviaMgAUE40Ew3q58bAQGNrNJuiVdCDjdn7-mDgaflTR5Kn3Jzfj3550FqROeYAuY0s4BpnZTOQQjq-MScEcTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=TedjtPkPcAsW6wpF_hQkdSFl2do_l3AO-XyMYSZLyvQFe5CzBKIKoYweS3EJsk4fOTc-PrbhblXTm1qE8pP0TbCcf9kFq2pagndHvjEGX0sj6Wxx2oidr06Gv5VPIlWJQtNH-h-gDOoWm5fupQIT5Almc3Tl9ka7GGnLhmW75KYsGXPX-TUhk1Gz4wpnBm88vLTuubJkWLqLV3p41pR8FUdsKihdb5Exs5hCVNUlss6ix7nF8Z8dqXxgu8VBC9U693huJ_HOudQI0ZuGTRi5_cJYMZqstMaR4hEbpifGuC2KYzxAqTawejo1XILizzlsMwmZBSTagRXXMKSk5dvEMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=TedjtPkPcAsW6wpF_hQkdSFl2do_l3AO-XyMYSZLyvQFe5CzBKIKoYweS3EJsk4fOTc-PrbhblXTm1qE8pP0TbCcf9kFq2pagndHvjEGX0sj6Wxx2oidr06Gv5VPIlWJQtNH-h-gDOoWm5fupQIT5Almc3Tl9ka7GGnLhmW75KYsGXPX-TUhk1Gz4wpnBm88vLTuubJkWLqLV3p41pR8FUdsKihdb5Exs5hCVNUlss6ix7nF8Z8dqXxgu8VBC9U693huJ_HOudQI0ZuGTRi5_cJYMZqstMaR4hEbpifGuC2KYzxAqTawejo1XILizzlsMwmZBSTagRXXMKSk5dvEMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMgms13NlkUu9SO3aBpsY-TNxTfZ3LooXB1owm-IF5UX9xlmKwCDZL6LGSup1b6jo2vWjn84IFdpGlovcsT0by0VqHuETcAEEYMcK4VmvYjTQ-Ccv0-mQqjnnE4RZKfAXm0E3_wATO_2brOx4PRydEaSCClSEEJem0jSDA9YU-IzhFmh42nU_OHmKeFW3rn9TsbDv46NfqB81OlfFdjUzMFPdfiE37Pn9SxZdJ_Z8T5DMzCssh06upXckdLkG8XunL7iz43uJ_-2q2fCJjHD76AZ5i4_5aXcC5iAdFVGwpaPcWqlklHyDOjMFk_D7CFIIiBb4ZZ0_xzpi66w86HgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=RG1shbVHe6JIdk9GR6jfRHzDVP_ekIJLG32cusN7VyO0BG87jKzHJ1JH_L6EFheUp1a6mFczn-h9ibrZAkgVwPWU2kW7fabjoLc5HYLCaHj4LUhJRkLvDy6gi46oTddTTkIx5Pg-g22PtE91b5ALaG0uTeN0m-sI_ZTySSlYdNHuglcda2epohKL6FIP-mVyWHUy5jRimJ148G2Bo0cIwGosi_d79rSlDX9RlPq32Zek8f0klywGrJ3t1vqCjWQ2-Hmkv4Pz6M9aKACdHAN9gpi-asDWGhQmi60w6PyZ6JyFR2qzUUUkroBNY6T8zuEAAbtlahb1TOxxmVCSlvRPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=RG1shbVHe6JIdk9GR6jfRHzDVP_ekIJLG32cusN7VyO0BG87jKzHJ1JH_L6EFheUp1a6mFczn-h9ibrZAkgVwPWU2kW7fabjoLc5HYLCaHj4LUhJRkLvDy6gi46oTddTTkIx5Pg-g22PtE91b5ALaG0uTeN0m-sI_ZTySSlYdNHuglcda2epohKL6FIP-mVyWHUy5jRimJ148G2Bo0cIwGosi_d79rSlDX9RlPq32Zek8f0klywGrJ3t1vqCjWQ2-Hmkv4Pz6M9aKACdHAN9gpi-asDWGhQmi60w6PyZ6JyFR2qzUUUkroBNY6T8zuEAAbtlahb1TOxxmVCSlvRPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc96kz27xeZRsMzHWCiJPXXDAaUu6-TaGmZf-NvjtWkwPUBBq-ojX7MM-g1lvCw6EPO-v2kelbWMX6J9gAEJb2JxN7s7uayCrrFQitxvoJBtkC2owFAlDxFwLuB06ICTyRGcLGzwUDSMn458c91gWUmFTeWuJ38zEVlwqahpo1gOkKuOEnBcJyKRr4hSPj3eqgVnSE87R-zEvOi14kmnta9rXOhLa-MOpPuUI2DpW_eNwDFC8fHLCBsUzjkiN2j3dVwXZ6VCYjxBCh3lafu5rZCzHRdhx3sB91II2ndrEYEI48dTV1sGrEplEU_J1s1x_LSZtKSZUPlfMLUrALc3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، سه‌شنبه به شبکه ان‌اچ‌کی ژاپن گفت بازرسی از تاسیسات هسته‌ای ایران انجام خواهد شد و هرچه زودتر آغاز شود بهتر است.
او افزود اولویت اصلی آژانس، شناسایی و تایید محل نگهداری اورانیوم با غنای بالا است.
گروسی گفت آژانس بین‌المللی انرژی اتمی به‌زودی با مقام‌های جمهوری اسلامی درباره زمان‌بندی و جزییات بازرسی‌ها گفت‌وگو خواهد کرد.
او تاکید کرد آژانس این بازرسی‌ها را به‌طور مستقل انجام می‌دهد و نیازی به نظارت یا کمک دیگران ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/76630" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PvIyaUOFoauzZhJs2DZ-W1HgocOa98NpqdbReojvDQ34566T3gmC10prbOvmXMJ49DD-RI1tHY7vBpgN2LtckYjh1QTqwj5JK5b0N3BprsK58RPVAWMBI1N1chkdXbdaDOvEttzK_N3yM92A0Hg8KLxEECYpn79zTImMGEUNZyWIaNQG98YVNdwpYLiMu_w5e-W5lF2kBr_gjAdXjnFQbxlT_e4tkk5k8fpQ-59W4C0Fyygx-OaRY75R2DnA4EmayftiJdY7fr1bCd09uDUgs0wGV1TEK98DOrRCp9lMhzqQbMK1BjxU4_wBa2eEJOOWsBFrX8HNVR4MsAEa6pyrTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا می‌گوید تا زمانی که گروه‌های نیابتی مورد حمایت ایران به حملات موشکی ادامه دهند، دستیابی به صلح پایدار در منطقه غیرممکن است.
مارکو روبیو که به امارات متحده عربی سفر کرده است، روز سه‌شنبه دوم تیرماه افزود این موضوع «در زمان مناسب» مورد رسیدگی قرار خواهد گرفت.
او همچنین تأکید کرد هیچ کشوری حق ندارد بر تنگه هرمز عوارض یا هزینه‌ای تحمیل کند، چرا که این آبراه یک مسیر بین‌المللی است و بر اساس قوانین موجود بین‌المللی حفاظت می‌شود.
تنگهٔ هرمز از زمان آغاز حملات آمریکا و اسرائیل به ایران در ۹ اسفند پارسال، از سوی سپاه پاسداران مسدود شده بود و تنها هفته گذشته پس از توافق اولیه بین تهران و واشینگتن برای پایان دادن به جنگ تا حدودی بازگشایی شد.
وزیر خارجه آمریکا در مورد لبنان که برقراری آتش‌بس در این کشور بخشی از توافق بین تهران و واشینگتن است، گفت که ما قرار است مستقیماً با دولت لبنان به توافق برسیم.
روبیو تصریح کرد که «آینده لبنان را مردم لبنان تعیین می‌کنند و پرونده لبنان از هرگونه توافق با ایران جداست».
@
VahidHeadline
فرماندهی مرکزی ایالات متحده،
سنتکام
، با انتشار تصویری از ناو هواپیمابر «یواس‌اس جورج اچ. دبلیو. بوش»، در شبکه ایکس نوشت که این ناو در
دریای عرب
در حال فعالیت است.
سنتکام افزود دو ناو هواپیمابر آمریکا همچنان در خاورمیانه مستقر هستند و نیروهای آمریکایی حضور خود را حفظ کرده و در حالت آماده‌باش و مراقبت کامل قرار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986282857.mp4?token=Ye3QWYF_tPpyi-eaTK9YIAS66GmdyAS2ntNirsLnRMfVei8rtkTjkXOcXvdB9xOsVLEPrA0fVfI3smdV3yASReDnnw0K4-cAhJsF8CSOZ3MZu6ju2wiSgXWzAviEqE0eF6B1DWP9_ybumA9rgsl05NMRj_gYnUTv_v4vYm6ha4AOQxvuOOqwWDvuN6ofq6ictMjdxqiuneLVrQFxQFOT2Yc14x0s7tebBsvA-6hIsYL2M_RlMXvVLXwA1w5A0_jrnCiRA5ah5lBi_OUztdLBJfShF6x-Llh3srFHIhiCizWo3l2DyU4vBc7WN60CeTfB4UNwbqnk5t9kbGAdsWQStw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986282857.mp4?token=Ye3QWYF_tPpyi-eaTK9YIAS66GmdyAS2ntNirsLnRMfVei8rtkTjkXOcXvdB9xOsVLEPrA0fVfI3smdV3yASReDnnw0K4-cAhJsF8CSOZ3MZu6ju2wiSgXWzAviEqE0eF6B1DWP9_ybumA9rgsl05NMRj_gYnUTv_v4vYm6ha4AOQxvuOOqwWDvuN6ofq6ictMjdxqiuneLVrQFxQFOT2Yc14x0s7tebBsvA-6hIsYL2M_RlMXvVLXwA1w5A0_jrnCiRA5ah5lBi_OUztdLBJfShF6x-Llh3srFHIhiCizWo3l2DyU4vBc7WN60CeTfB4UNwbqnk5t9kbGAdsWQStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdO7K5Df-BfTdMkQbPtO-dzNgyRi9tpkhu2BSQ6UPWN1S-TT_AZnZeZG83aB9CLe_LRu3yovgjz8XoZpLd6X9z7XkaNiJvieH-efyqad13URf1Ohr3EjjLqube0BREiplbvfwRWjmlCj93tgBJXEPpmzo1KuD47jrnn2C6mW_DL64fcVRlb44qdTORQEKdBbvsDyxh_3WIUT1d-JXyHspP4BU0H-8fo780fD1RN3JoBhKWW0ceUWaJ3Agk_19nqDhxWP61hCl5RxpNKLrkX8rtbrFoidfmm5vyEcbr3iGKvlofKoQey7xvYZK_FOpBPbSPkv1wLyey697YMXT6DjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثریا طالبی، مادر امیرحسین موسوی، فعال فضای مجازی مشهور به «جیمز بی‌دین» که از آذرماه ۱۴۰۳ در بازداشت به‌سر می‌برد، می‌گوید پس از پخش گزارش تلویزیونی از فرزندش در جریان جنگ ۱۲ روزه، اتهام «همکاری با دول متخاصم» به پرونده او افزوده شده است. مهر ۱۴۰۴ صداوسیما با پخش ویدئویی از اعترافات اجباری امیرحسین موسوی، او را به «جاسوسی و همکاری اطلاعاتی و امنیتی با اسرائیل» متهم کرد.
پس از آن امیرحسین موسوی که با نام کاربری «جیمز بی‌دین» در شبکه‌های اجتماعی فعالیت می‌کرد، با انتشار نامه‌ای سرگشاده از زندان اوین اعلام کرده که تمام اتهامات مطرح‌شده علیه او «نادرست و تحریف‌شده» است. آقای موسوی نوشته که پس از ۱۴۸ روز انفرادی، بازداشت همسرش و تهدید به تکرار شکنجه‌ها، وادار به انجام مصاحبه‌ای اجباری شده است.
ثریا طالبی، مادر امیرحسین موسوی، در گفت‌وگو با «امتداد» با اشاره به وضعیت پرونده فرزندش گفت که امیرحسین موسوی از ۲۸ آذر ۱۴۰۳ در بازداشت است و خانواده او همچنان در «بلاتکلیفی کامل» به سر می‌برند.
به گفته او، فرزندش هنگام سفر به کیش در فرودگاه مهرآباد بازداشت شد و خانواده تا مدت‌ها از محل نگهداری و نهاد بازداشت‌کننده او اطلاعی نداشتند.
مادر این فعال توییتری همچنین گفت امیرحسین موسوی حدود شش ماه در سلول انفرادی نگهداری شده و پس از انتقال به بند عمومی، از او مصاحبه تصویری گرفته شده است. او مدعی شد به فرزندش گفته بودند این ویدئو صرفاً برای آرشیو ضبط می‌شود و در صورت همکاری، طی چند روز با وثیقه آزاد خواهد شد.
به گفته طالبی، در زمان تشکیل پرونده، اتهام‌های «اجتماع و تبانی علیه امنیت کشور»، «فعالیت تبلیغی علیه نظام» و «توهین به مقدسات» علیه فرزندش مطرح شده بود.
او افزود پس از جنگ ۱۲ روزه و پخش بخشی از این مصاحبه در بخش خبری ۲۰:۳۰ صداوسیما، اتهام «همکاری با دولت متخاصم» نیز به پرونده اضافه شده است.
طالبی با انتقاد از نحوه انتشار این ویدئو گفت: «فیلم به‌صورت تقطیع‌شده پخش شد؛ به شکلی که این تصور ایجاد می‌شد که امیرحسین در زمان جنگ اطلاعاتی را در اختیار دشمن قرار داده است، در حالی که او در همان زمان در زندان بود.»
او همچنین از شکایت خانواده علیه برنامه ۲۰:۳۰ و رسانه‌هایی که این ویدئو را بازنشر کرده‌اند خبر داد و گفت این شکایت در حال رسیدگی است.
مادر امیرحسین موسوی با رد اتهام‌های مطرح‌شده علیه فرزندش تاکید کرد: «انگ وطن‌فروشی به امیرحسین نمی‌چسبد. او یک فعال توییتری بوده و اگر کسی با ادعای ارتباط با اسرائیل برایش پیام فرستاده، بلافاصله آن حساب را مسدود کرده است.»
بر اساس اعلام وکیل پرونده، جلسه رسیدگی به اتهامات امیرحسین موسوی روز ۱۳ تیرماه در شعبه ۱۵ دادگاه انقلاب به ریاست قاضی ابوالقاسم صلواتی برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IrHYEeFR9VRgPsPF_UxTECWhgM6XDG9ly9illxE689djY9ZNjUuzWpvDjjyOh3DnzXprpP1wLP8QmpeLBXSHpDyhkieX_s8JMWxtlfSee8Max01LlMoZPzMGlvZ94HFpfr1UqG36LdgvfJy21eIR1RMRiju5aEt6u6BhPefcbUTMhnMDhj8rCimR9WtyFCLab1yLjm4VRGstgJozt0RvEI_TdQ-W539b7HlHXHyiVulqJh0ksw-7xd7OIZUi59uauLQ0IIIl2lXZ_FG3ceZNilOhM9owkWbahJvTp6aU_J5UwkcbDjaQxmUPr_mcjXmy_DlEtigLu523oXoyJsa8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DK3YqP8ROlFkrWct5Exx9NMVuAY4Q27-2WdoTcr_ue34uBodVIbWCA9vCT7E1G82lu1zQrMcxDVVeCiqCpiiMkfWeKF2Eb5eFKFQeo57hZoUf3HhIMAyrIMz8e9w3vAFhgxrj8Kp_xPFFj1EB9mDwgSySdw7tTNB4-bYrWPnG5A3Iw8Dl9CMpyWR1vdzSpi64-TTOnR7TBcsSpQANGvCFXmDdnXI3dfL52EpKTWWDnPBFz2kfhGzrd1QzftlLFLr9TKiL3NbFvAmFWsCNoqjgu2bc3QnDW__bFfaIT-iQRJ29BhIVkF_tgUStKwdyqzj2r0zA3PSb7xw4lsl62d3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YZB-e5itdl-B2e6F4qM8ZGUgB2xJ3CZNJGmTP2AevWTQyHlGOzccO-VwAfz9CZ6XMO_4imteGBjHldvMn_NWkrEmFvY_mCYc1oL0vjO4hoWdIEUEhgJIF4SHWoMgqaRmqtLVpSed276Dw-7HRdxWaG2cZbe73CEBllkP0YEmQrUSW9AlGkKmu-YqRzh2sZMFQYecJcYd_iZjUH7ebdoz-4R0Z5wYqfoze2xLbA3Pq-OAEE_tUAbW7wOAEv6j3JPCLsusXPoDZismDtftn_ZaJURKGmMEAG2xsyDjnrL4AIlcNVP_P5svZ6FW3ecAM1KPVrdsmPIlCKucD06KUeBP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP7rLoH3M_LiGeiPkFlwB7ClGATREW5r1nQbYYpS6O-yi0JQqlUMqDdTrfpc0rPzcgHjCZ8m-1soEzrkWSl86kjNG9qNxXQDyjFCLiZv7K6At_IAy1QOHTuql5aHgoI4SfVRBe-fJhCIxuZ1d27clehfJcgTA3dU1avWIuxDVNhv6Np2AKtf5VNoOqGccm5v2BcdaAEtIzl3xPrMa6vvXaKB6YZsaobLRJs2-2zmTLznVleKk6Ii11gcsF57Gwl9IvQy9_Jzsd5iwyWAI9ti2Uc70S4MwUREo9ZyvqQNR4vm-31Hj05c7PaGiupZNrbLVQT8HMx53pahUWGL40on0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CHzY1VeuxntTkut7y6wsw6xCfEtU-wZlWbv2dnaTsJWBvL98MiTuS50_dEQIgyFzIkWukrxAWGzQem8ngZXxfZa9CpsROvE2F3QJ1AqIVktYaeTDesD2osjhWPrP7j5QGVXjereYqwmctf8tKaD5yxlLl-gNERIYKBRLiRWewRx_Ytv4CNiK3ICZkifrAfVLK4sjceY9hnUrDQVtooGB-M3kXCa7B7yfFbef0nb1HERTIQ0S7ItuSr349J0clETooyNjDGSLZQp9lIA2zLsXXoi66F2a-skGdW5T9uFqaifXpn3TRLLGWhBWubmtQ8Jh4hMik_XUpgLJ0AzLC-nPNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌های کاربران از بروز اختلال شدید و قطعی در سامانه‌های آنلاین و پایانه‌های فروشگاهی (POS) برخی بانک‌های کشور از جمله بلوبانک، بانک کشاورزی، بانک ملت و بانک رفاه حکایت دارد. این اختلال‌ها موجب شده مشتریان در انجام تراکنش‌های مالی، خریدهای روزمره و استفاده از خدمات غیرحضوری با مشکل جدی مواجه شوند.
@
VahidHeadline
گزارش‌های مختلف کاربران در شبکه‌های اجتماعی حاکی از اختلال گسترده در خدمات بانکی چند بانک بزرگ ایران در روز سه‌شنبه، دوم تیر است.
بر اساس این گزارش‌ها، پرداخت الکترونیک و انتقال وجوه در چند بانک بزرگ مانند ملی، تجارت، صادرات و ملت با اختلال همراه است.
خبرگزاری‌های فارس و تسنیم، نزدیک به سپاه پاسداران با تأیید این اختلال‌ها از احتمال حمله سایبری به مرکز خدمات پشتیبان خبر داده‌اند.
در همین رابطه شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، با تأیید انجام حملات سایبری، گفته است که «شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است.»
این برای دومین بار طی دو هفته گذشته است که خدمات بانکی در ایران دچار احتلال می‌شود.
چندین بانک ایران اواسط خردادماه هم با قطع ارتباط و خدمات روبرو شدند که به گفته مسئولان دولتی به دلیل حملات سایبری به زیر ساخت‌های خدماتی بانک‌ها بود.
تاکنون گزارشی از عامل این حملات سایبری منتشر نشده است.
@
VahidHeadline
آپدیت:
پیام‌های مختلفی دریافت می‌کنم با نظریه‌های توطئه که فکر می‌کنند بازار ارز و طلا و...  قراره نوسان داشته باشند و نمی‌خوان کسی بتونه خرید و فروش کنه و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecK5rl3SNDrR2wDtZdyEVwyukVI6bIP42tI57uSzIGjJIF3mOjkAmbgOl_P46DaC1I2WUcC2a9UwCVv9VfiZ2RBaIG4o8WcP7T-2KYkv-XPLersJi4D-844JRMPy1QQpLiHPVPytYY7l-DNuPnn0FpTfgVIP2CKS8KQXt0qCpAwUG6t9juANziudiWV2HlQ_NFe4aIOR-1X-oyGzA-iv5DFd6-o-15UIuomX_x-0wPLaAEawOLuKcmsDqk6xTzKzYU19d398RuuHe-wHXcJS3VwB3zB0m-Gdl5O16uGTtBcs3T0KF8vq8RhWxDR-I8BmHx-JGkRh2FTpBjzJ9ubUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان و ایران روز سه‌شنبه دوم تیرماه توافق کردند گفت‌وگوها درباره نحوه اداره آینده کشتیرانی در تنگهٔ هرمز، از جمله خدمات دریایی در این آبراه راهبردی و هزینه‌های مرتبط با آن، را ادامه دهند.
به گزارش خبرگزاری رویترز، در بیانیه‌ مشترکی که پس از مذاکرات مسقط منتشر شد، دو کشور اعلام کردند یک کارگروه مشترک با مشارکت وزارتخانه‌های خارجه تشکیل خواهد شد تا این گفت‌وگوها را پیگیری کند و همچنین با دیگر کشورهای ساحلی و طرف‌های مرتبط رایزنی خواهند کرد.
این اقدام به نظر می‌رسد اجرای بندی از تفاهم‌نامه‌ای باشد که هفته گذشته بین ایران و آمریکا امضا شد و بر اساس آن، ایران موظف است با عمان و دیگر کشورهای ساحلی خلیج فارس درباره مدیریت آینده کشتیرانی و خدمات دریایی در این تنگه، که مسیر حیاتی برای انتقال نفت جهان است، گفت‌وگو کند.
این توافق پس از سفر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، و عباس عراقچی، وزیر خارجه ایران، به عمان اعلام شد. این دو مقام ایرانی با سلطان هیثم بن طارق، پادشاه عمان، دیدار کردند و با وزیر خارجه این کشور، سید بدر البوسعیدی، نیز گفت‌وگو داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76621" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nI3kdJsPux6Xrulf2FwI8y1j7MyTgSQUIxu2as0BRZkBrhp9NSEGus6_jMwDp_Rem5tJjpxJmOKN30g2DRT-wo6S4ZFxhR_sUVjR1HaIkp3HzrWqqpO_fajgg5cspvuZDFkE_EECH0Rr_bibiRO0qKxzwHZjBj6nt6bJOmij1E1U_9U9fK5zVTQrjBg_9ix9vSmrXOcVQ3WZcIHFX_E_XNajx5Z5YMk9SMd7w6onDs4ha-sXVNjwX_aJwzEHUkRMwqsJ1vm2dOLdBSg_RLpTnhOzeuSqxUI1_Ycq-4GIsjRFqbpAiMJ2FnORmGrNbqT9HoZa8u1_aQ3vZZJXMzFCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=TIMhfL_uBGMLZOmSY91w_Lv_Vkj0eFLXN-DkOkAT0BdEiw3L-vPGjNq5yfhFV27KZKXWgax0EDqVPRTweIWdysv2Gkaq9WO7fA1Im9MroYMFi_E3ON5u8epoDAmuPEnMbLjc6q6KQkAXfRIKj5HujssTLUbW3pbs8T9m39XTL1U-EYGoheDToLhvFj_oldTGnLXECv0-RUV58VvcyaXWh_RU1V1J_yfCdBJizPRbJXlqfexiJcz1G1cc1f1kOrW_Q5hVOQ3L1S67wrV7o1PZRwberUhMemwCkuP6XOtg6YZBGdFt6Ec8b5fMi6iz-LXejfo1UN20qSei3qeVpVzY7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=TIMhfL_uBGMLZOmSY91w_Lv_Vkj0eFLXN-DkOkAT0BdEiw3L-vPGjNq5yfhFV27KZKXWgax0EDqVPRTweIWdysv2Gkaq9WO7fA1Im9MroYMFi_E3ON5u8epoDAmuPEnMbLjc6q6KQkAXfRIKj5HujssTLUbW3pbs8T9m39XTL1U-EYGoheDToLhvFj_oldTGnLXECv0-RUV58VvcyaXWh_RU1V1J_yfCdBJizPRbJXlqfexiJcz1G1cc1f1kOrW_Q5hVOQ3L1S67wrV7o1PZRwberUhMemwCkuP6XOtg6YZBGdFt6Ec8b5fMi6iz-LXejfo1UN20qSei3qeVpVzY7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامران غضنفری، نماینده مجلس شورای اسلامی، در شبکه اجتماعی ایکس از برنامه شماری از نمایندگان برای «تحصن» مقابل ساختمان این نهاد در اعتراض به ادامه تعطیلی آن خبر داد.
او نوشت که «چنان‌چه مجلس بسته باشد، تا باز شدن مجلس، در همان‌جا تحصن خواهیم کرد.»
شماری از نمایندگان مجلس به تعطیلی این نهاد طی ماه‌های بعد از حملات اسرائیل و آمریکا به ایران در نهم اسفند ۱۴۰۴، اعتراض دارند.
حمید رسایی، یکی دیگر از نمایندگان مجلس شورای اسلامی، یکشنبه ۳۱ خرداد با انتقاد از ادامه تعطیلی مجلس گفته بود در صورت ادامه تعطیلی، همراه برخی نمایندگان مقابل ساختمان مجلس جلسه برگزار خواهد کرد.
حسین صمصامی، دیگر نماینده مجلس شورای اسلامی، نیز در پیامی جداگانه در شبکه ایکس، نسبت به ادامه تعطیلی صحن علنی اعتراض کرده و نوشته است: «بیش از ۱۰۰ روز از تعطیلی صحن مجلس می‌گذرد و نکتۀ تاسف‌بار آن است که در سامانه قانونگذاری، امکان ثبت استیضاح وزیر و صدور بیانیه مسدود شده است.»
انتقادها در این زمینه به خصوص از سوی نمایندگان نزدیک به جبهه پایداری با پررنگ‌شدن نقش محمدباقر قالیباف در مذاکرات با آمریکا، افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/76619" target="_blank">📅 17:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXsEC9rQUwbEMV3CWoFvDoIJ3eARKVVVvW7ZFecLYB6yxUGc8PiINolT4nCZ4qV2hOuOt8NqOxfEHc02W6z-X6bLTF7pvig0cTBYUSeBPdIweCR3-L7VdtMRq4vEyXext3yA2k-2k3ecaq_dkkfTzGanLzGDAPw1M3uY_ogA5rnFQSbum7DS5wk0hRC7vWAtyAaXmdVhH5tShMggZ_z1P43DJ1JZPZDwERVO0-p7DGNvsuER8sA765r7U800kdhqhRdwYXifiriiLcQOmTmAYlHww4VJ7hhZWudnSWyaCsNvs7F_f6R05oCU_g-tWpG__Pv6CFlqT4oDOM2hXZjjCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون فیلمسازان مستقل ایران، ایفما، در بیانیه‌ای نسبت به احتمال اعدام علی صفری، بازیگر تئاتر و دانشجوی دانشگاه فرهنگ و هنر هشدار داد.
این کانون با ابراز نگرانی از طرح اتهام «محاربه» علیه او، از مراکز سینمایی و نهادهای بین‌المللی خواست تا برای نجات این هنرمند و سایر هنرمندان در بند، «فشارها بر رژیم ایران و قوه قضائیه آن را بیشتر کنند».
به نوشته این نهاد، علی صفری، بازیگر جوان و ۲۳ ساله تئاتر و دانشجوی دانشگاه فرهنگ و هنر در جریان اعتراضات سراسری ایران در تاریخ ۱۸ دی ماه ۱۴۰۴در شهر کرج بازداشت شد و «تاکنون اطلاعات روشنی درباره‌ی روند پرونده‌ و وضعیت این بازیگر منتشر نشده است، اما اتهام «محاربه» در تاریخ ۹ بهمن ۱۴۰۴ به طور رسمی به او تفهیم شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76618" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUAJC745a21fEbW9oaRECVPMT89-H2wg5xdilFaSx7qBxQx4Um5kM4PkryMyG0awVY5MoU4q6sSbLGd6kj4lW2b-z31Mpc7RHhb8gJopOZRmSyKD9hX0E_1fMRN6-hf7Yd1VCV8iPHt_tBmwG64bQFqh1zLV8d1BoNs-HyluiCcgGt1Eve06IFfNGSwpjOwEdmvbkUgkHYxdR1b6ezSk5_LYuC3ApBktMjk6glBtrrCFccG-gTLWKtTNi_4llLsaRhquyPpMoDjgWvnia9OAgKLqglveXDo6979qgzDYGotGK-D9HHIbtu33nde_geMBQCiw-FrlCvh_gtVs_CRm5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11113460cd.mp4?token=Vli4wiyaWweXZhCDLnB8035wVg-xYc5eu-xbHTFAviwqfN-AZLiW7jcPyMuk9QTXMcaiGqzFhMB5hwaV4y_o5ufj9N3S4c2oi_U4jZ5oAhDlhNmag29P7cuC4Iu8XXdg0rjDc8R0aJjcqk_ju4jeNVmiG-TU_IyDgFIA5G6v6o8wghj6fbxDTGrLipbdkz0tMQ2N8emSG7AUT0LG05_HaYnh5pIGCgDdtNjTj8ZJuiRQ5zq_1f5xzplN2_AhATmdoGqQaq40gf54ijTds84xNKW8G-6JEqb--oveSWCtgEUUwcJiWyY1iMgAm0AJW-dgBaVHwXsMckkPLA_FKXgc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11113460cd.mp4?token=Vli4wiyaWweXZhCDLnB8035wVg-xYc5eu-xbHTFAviwqfN-AZLiW7jcPyMuk9QTXMcaiGqzFhMB5hwaV4y_o5ufj9N3S4c2oi_U4jZ5oAhDlhNmag29P7cuC4Iu8XXdg0rjDc8R0aJjcqk_ju4jeNVmiG-TU_IyDgFIA5G6v6o8wghj6fbxDTGrLipbdkz0tMQ2N8emSG7AUT0LG05_HaYnh5pIGCgDdtNjTj8ZJuiRQ5zq_1f5xzplN2_AhATmdoGqQaq40gf54ijTds84xNKW8G-6JEqb--oveSWCtgEUUwcJiWyY1iMgAm0AJW-dgBaVHwXsMckkPLA_FKXgc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه دوم تیرماه بار دیگر تکرار کرد که ایران با بالاترین سطح بازرسی‌های هسته‌ای از تأسیسات خود موافقت کرده و این بازرسی‌ها «تا ابد» است.
دونالد ترامپ در پستی در شبکهٔ اجتماعی خود، تروث سوشال، نوشت که با وجود اعتراض‌ها و «ادعاهای نادرست» ایران، و «هم‌زمان با جار و جنجال رسانه‌های جعلی که هر کاری می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند»، ایران «به‌طور کامل و تمام‌عیار با بالاترین سطح بازرسی‌های هسته‌ای برای مدت طولانی در آینده (تا ابد!!!) موافقت کرده است».
به گفتهٔ او، این امر «صداقت هسته‌ای» را تضمین خواهد کرد. «اگر با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد!»
نخستین بار، جی‌دی ونس معاون رئیس‌جمهور آمریکا بود که روز اول تیرماه خبر داد ایران با بازرسی از تأسیسات هسته‌ایش موافقت کرده و این امر ممکن است در هفته جاری رخ دهد.
با این حال، مقام‌های جمهوری اسلامی بویژه سخنگوی وزارت خارجه ایران هرگونه بازرسی آژانس از تأسیسات هسته‌ای را رد کرده‌اند.
@
VahidHeadline
پست‌های ترامپ، ترجمه ماشین:
با وجود اعتراض‌ها و اظهارات دروغین آن‌ها در خلاف این موضوع، همراه با هیاهوی مداوم اخبار جعلی، که هر کاری می‌کند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهد، ایران به‌طور کامل و تمام‌وکمال با بالاترین سطح بازرسی‌های هسته‌ای برای مدت بسیار طولانی در آینده، یعنی تا ابد، موافقت کرده است!!!
این کار «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این موضوع موافقت نکرده بودند، هیچ مذاکره بیشتری در کار نبود!
بر اساس این موضوع و سایر امتیازهای بزرگی که ایران در حال دادن آن‌هاست، من موافقت کرده‌ام اجازه بدهم تنگه هرمز باز بماند، بدون هیچ محاصره دریاییِ دیگری. با این حال، همه کشتی‌ها در جای خود باقی می‌مانند تا اگر لازم شد، محاصره دوباره برقرار شود؛ چیزی که در حال حاضر بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که وزارت خزانه‌داری آمریکا آزاد می‌کند، به حساب امانی منتقل می‌شود که تحت کنترل ایالات متحده آمریکاست و صرفاً برای خرید غذا و تجهیزات پزشکی از ایالات متحده استفاده خواهد شد، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما.
این‌ها چیزهایی هستند که ایران به‌شدت به آن‌ها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است همین حالا، پیش از آنکه خیلی دیر شود، کمک کنیم.
گفت‌وگوها به‌خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد؛ رکوردی بی‌سابقه در تمام دوران. قیمت نفت به‌شدت در حال سقوط است و جهان جای بسیار امن‌تری شده است!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/76616" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T116A0-XmyGCu-1N5p1y8G-fMJwc_4cjS5G0CJGwn3Qd4Gs70-6ubzQCzjfAlV6JMxYw8PHvKWk4kRZxQSryfBKB2mreuAE7TE32desjBrevBsUB41TjWZE0OsLVZJ0rfhXbLesc5nbQNuXjv5LLYbwGcBGfzw2nIKE9JSO6E53TuiGD01tONPF2QrCl0_boujJKM39i_RZpeH5qXQwcKY8dUFAYXICBjcIDYnxN1ipg4227E3r5ah46vL-0q9hCEWyfZwo-7Vkn0QKLrMgfc6qfOgOaq-5a1TsiGmyZSb_tcRAkNsXh_-4ERrS6PJySPnP9Qmt-_GStPMSgDn6nzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر سه‌شنبه دوم تیرماه گزارش داد قیمت  [نان یارانه‌ای، نان یارانه‌دار] در تهران و ورامین افزایش یافته و در برخی موارد به حدود دو برابر نرخ‌های پیشین رسیده است.
بر اساس این گزارش، قیمت‌های جدید از سوی استانداری ابلاغ شده و از امروز روی دستگاه‌های نانینو در نانوایی‌ها اعمال شده است.
بر اساس نرخ‌های تازه، قیمت نان لواش به دو هزار و ۷۰۰ تومان، بربری به ۱۰ هزار تومان و سنگک به ۱۵ هزار و ۵۰۰ تومان رسیده است.
محمدجواد کرمی، رئیس کارگروه آرد و نان اتاق اصناف ایران، نیز افزایش قیمت نان را تایید کرده است.
در ورامین نیز رئیس اتحادیه نانوایان از افزایش ۹۰ تا ۱۰۰ درصدی قیمت نان خبر داد.
بر این اساس، قیمت نان لواش از هزار و ۴۰۰ تومان به دو هزار و ۷۰۰ تومان، تافتون از دو هزار و ۳۰۰ تومان به چهار هزار و ۵۰۰ تومان، بربری از پنج هزار و ۳۰۰ تومان به ۱۰ هزار تومان و سنگک از هفت هزار و ۴۰۰ تومان به ۱۵ هزار و ۵۰۰ تومان افزایش یافته است.
مسئولان صنفی افزایش هزینه‌های تولید، از جمله دستمزد کارگران، خمیرمایه، حمل‌ونقل و اجاره‌بها را دلیل این افزایش قیمت عنوان کرده‌اند.
رئیس اتحادیه نانوایان ورامین نیز گفته است اصلاح قیمت‌ها با هدف ادامه فعالیت نانوایی‌ها و حفظ روند تولید و عرضه نان انجام شده است.
این افزایش قیمت در حالی اعمال شده است که نان از مهم‌ترین کالاهای مصرفی خانوارهای ایرانی محسوب می‌شود و در برخی اقلام، نرخ‌های جدید نسبت به قیمت‌های قبلی نزدیک به دو برابر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/76615" target="_blank">📅 17:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zyl15JHh60MEY9RqJLz1d8dQzq-RyRhnqnJ5lr5ftI5G97wbEofsbrEKNfFmyDkI59OhT_Pn0YjO5fAk-wIQq2BqBuX49Ya9AlId83COvPHBefc897qHmRTzoNDNDyf7b8FEd5pS1bGxh3YD713nIogHlKXvB5NIEL-c6RFj8kl3asjoOOfuziaSn8QNCqmZ0KFG6HNe4e1ugCRkCzCLg_3puKXAH-6_kv-ORcuc5Km32TyuX8gK_A3ZR2phLkxNPYp4gSK62otL-EeQdtZPVsZVWAZ66CCsTBQXPmE-LpJns3h7AivBNEnXn6Mr32nCWkQ1y9H4BxoL9XDQ5K1jZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Eozu4pqBrb0q12NHE6HhM2NqcnGM0205TrAYCqE1AzUt15cf0yHsllk7ATh6YChy58zeR79VyCSfJinxA8C59ZfN5Mhw4dneo_VwhjPReO_jXtDaNtbnrcdTsfb2LhWjQgDPG5taU7pQquR3t6YpBoCZlNPsCSfLBWW1u40xcPp6sNDhFxPuIixMEuFFIwPnen0CqeXrJaPPJc84ZExBNh_vkeT5vcHXYsHSf0sz1eY5_O87Hr25sLMk82qt9q9k72uYPxijbBI92bZZ-Sl24tGpy4Qjena3lwvXz8NQTdGcWxN85L6Ry8kFFzgKaTDRVT9SI3Xs_VOlEgTiacbjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W8HQV1T4DBJW4KYMFQN5ZhqAdTR_HZIbFKJ5l4O_C03xe5IKF8X2AE4kskCh7fpDFVV1HIStUR28vhAij5A6ztExNfJKbNNlmOBFcq8Ljgu3EHRAo48PKz8xpriUK9yoC9trwS3ms8yhUkvsvxCRrfkDSH3q_3ufK0tTbtrKLX0XDv8v42RT8dej7Ldk9Ipt-zaedBMJx9NIj0BGLWroPWdJWtH_gTZd1lRvJoUKRytzL6NhNAF5r0yGRjhf4JsVuPxL4mHZXNYzNhdxvHY1sduvOtOpNLViCXm3Gp-M87JYRlD9yMFD-zt0GA_QCaRogsfojDewH3qSjBTDFXIdrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=vvfp8TViqw4KZx_X5C9Ji5rT15qT1NGKS3PSgb6KWQKeXMVuJP4DmbRaNkk-dBKkprYqOvMDQ1z5W3SkX2kN7_o87TnE9sCdkcs9bLR1ndlp4GSAqDVgk1MvXaZKX-Fjas_RtQTE2ls2PeSw_wgikbLexpuYr7lVXMZDfMB_NxAhZoYQL3ScYjxXKYC4GT0Ikq377-V-O0zUH0K06Vh4nO3056h_2_RUwd6yeUcleF1JaY3srJd0mBjesH7L-tracnf-dOF_D_TdNabhxxApuLgz7uxnC5zzuCdX4HaLGnpqLq8yrtTGriBZ4IZwaLFMfPBZNTPH3Jw1AK1GZ3ys9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=vvfp8TViqw4KZx_X5C9Ji5rT15qT1NGKS3PSgb6KWQKeXMVuJP4DmbRaNkk-dBKkprYqOvMDQ1z5W3SkX2kN7_o87TnE9sCdkcs9bLR1ndlp4GSAqDVgk1MvXaZKX-Fjas_RtQTE2ls2PeSw_wgikbLexpuYr7lVXMZDfMB_NxAhZoYQL3ScYjxXKYC4GT0Ikq377-V-O0zUH0K06Vh4nO3056h_2_RUwd6yeUcleF1JaY3srJd0mBjesH7L-tracnf-dOF_D_TdNabhxxApuLgz7uxnC5zzuCdX4HaLGnpqLq8yrtTGriBZ4IZwaLFMfPBZNTPH3Jw1AK1GZ3ys9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«امیرمحمد هموله» ۲۴ ساله، ساکن شهرک صدف شهریار، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ بر اثر اصابت گلوله به ناحیه سر به شدت مجروح شد.
او پس از تیراندازی به بیمارستان نور شهریار منتقل شد و حدود ۵۰ روز در کما تحت درمان بود، اما سرانجام در روز هشتم اسفندماه ۱۴۰۴ بر اثر شدت جراحات جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76611" target="_blank">📅 17:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/orGLO8b60KV6AtgqYqtS4OCMYeGKjCRm9wnnO-MCoYMNbvuviErXDD3CN1wizQ9-6SZpuVtesd_tROAB-twKSullr1fKG5_Emj1fBpC_tODC5GBVKQ8t-B-5fGwfBw9nhXkYf1f8EAhJr8rHmHGeAVNEPZj8SW7xT-c2ij6nxZ7a9YF_MUYLHJw7BYOjwTtdtIx2i_IiBQrAhXQX3lyEdlBjxHqvig2ZbAf3ftWwqapr_XFYEQDGJBLXvCoEY0hSzSmeyf-jwbTtOEPmThIuU7av2i8cucgovr6BnJ_Zp9eS1zFtPe9-BYAirE39bK6Yjx4t4qsHXTniqXzKTAQ1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sZM6_NIgEmOrSyDBwblfbHDgLY0Bozt3I7zidHDiJ4lXeHPWpwX-Nph0hRb2Jxv06BbrD7cLCQ5f-5tOaXjSR1G2ZNMn_R4strHDMUoh2OSzEdP-yDl2R3C7YRQPmqhoWtNP69ZVK0alaEL0VsDNoLiS5CV8f0s6dOEesJK2QGxzZvu3GSgC63z56aPf5fsjEJFL2kE3CKQmZzuTGNfmVsZW8GxyeLPQrtKi9h_1Xq3RtKDzfytQSyZ_R1IXGgZlvIo6pPS2Fl8d55qtBEoEqjfB_avsKAUjMgfjR0nf5mBQqOfnXZqwd_F_4Srpiu1NPn4lnZDaSKCT7t8H6FpniQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E49fcnCzwn4Nh5FYxG9x8aazTUWiZVgaw4xolIR0IE_INgf5q4A_avyDexI58QQxybk_6VtBIL8_216XxQGW9_GqqGTlbNxv9J0D4EK2gkJYLaHIktmjZXNdsQfYc-xgpWnJHNMS7vr6iJKqTIsXFAMu0NBW1wddBy6Vk3B3v7Wca2HF3l7v02fioXNUqXet0IXpNyXnzXUq6rG11pC7kRGeCbpc2zInrOuUXrVJ4QRItERIJLNgUQvDQK8xFXbVWZsIZVNQ-_1Z7F73poqlwVknHvLT1t07dwNSQ-hby6SvmGfik31_9onrJQsCGYJrKemeYb4LxzYpWIP1w0l_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pQEK8S6vr38ThA4L8ktrNvADQdIsIyq8n_8Ox2q2ezG660JhG6F64ju3nYSnBfR1lTEylPXKtUFmogZBkh-qiQGRQOVRR8Xa6U7faBYJ4Fd92VnT78h3odZDY7Wbw_-ITgQEz_SRKZxyJzTXZfLIHV1bLQtooO1ybAu9g5oR5biHEa5ERMEQsiPIwvo_WvuVC26uuid6i51zGmuwRBMu8XCG0uHwLFp9C7aP-rE36vHYwXYxruPh5xRFdMmmtoBqJ7XR_gdDfwm2US-f1vgDaepsZ43q_vW7wOVo9zDxevSOE_GSpZ3HWS8JuzvlBJ6C3IpengrHanzExmaJYYRq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UA4g-KZnW0Qs6_NGpDZ70ynBIof_dXs_bgrdnnnd6N8OOVvbEd4s0OR36aI3F80gfffCLM07sOWD-ZsMALDad2SlF1nHs8Bws1RX0x1q9VLCGDhmO-gq1e0jW0ZuL6cOW-lZjAEtUqZLqOgZOdkyXfc77otEcFL5uVU9ewynlLX6NFS1QzLP6MfR4-TywRvSsH2nTuKABV7D3obNeL4cl3JJaamKVeNU8lZAd56dD5tVifbj0Kx5o8wySoXni3weLcKSLbN2ae7ctf3I2pVo8qaJ9bfKS0aUZYRTwhoe2wQYaowFKG6rUOgV4b_mlMOcUi1eZPbkBuJN24lQVVHb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PlVYj5iTcjimwh79aqiagw3HiamDrv_qvlpXQJvZ5lXmC3QlPqtB02cBt-qTP_Jy83CBWBpzLe7g3pcFv9BYieCT5ymj3uepKxgDM5bSxkIlIIZP34CP7YGhnBg5YbwxJv8kw1LLCnLPaJXma2WJKHV6DC27FjDni7Kg9wURY-A0F0YpLUnhFrAMm8IoJP5XOb5hbsaDH1u8tb-7UEKltWI-o09IdCuZeHC7sa3TAkBSP9xY8gf87LzRjFKe42jzWn3YnNyoicnbCoR6iJDM15mAy-tJoMHfzQr5l0Wf1634b3GO7eGrSJOBBgWMvslxgxMREcg7FMv_feSUpaQYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BL9SJsw0a-vZ4y-BkcFImQ5WdNLQyjeovQRE6Kk3SDWgKb21EGJzKBzwxLJGmUqnTEFyLAs1mPQt_cvS29RatCHr-xbVphcoa_RpZGcZTvRx9wfu8pHMpR5xXDXka04XVsBD0oYDrO2DVjPk4g8TqPIuG9T0oDlI0NEErxh3NyTOa1AYzEe2nUcPKC2ageb1zJGFukSwWCtKDIccaqkpP-etu-fHcQqOtPq1our7yDZVs6jkpWQS6W_TBVOkIrZuRwNOWxJZ933bTn1E0FZ_azWYbfXfNgHwi4rvnTKBKxWJNxqPzwhndd1Zi3XzISjts4HPVH6IW_etmMVwCDtgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZHmLCj_KdoEAAcXXtB-vOA2_IqyWOqOoDjJvoEG3ihpu_SaKHQejG0z8FhRow6fAG7PlcRJA7yhIE_Bu6xQC0pBvapq0iJnibL2jjZbgYtxcU4_LOYNL4XppJCAqYxJYfLceMp9K7grK324vq6Dt766RO2xE0dS744lq4IHrWlPGAlFS05p81YBmo6oEwSl0viK6ynyRyGtszJMcMlia_qDzpma9CvBKbLsL1NNRUDflJAHarz5_UbG71ahQtNCtAHqdPqlG8ojLbs40dfEXT7pq3t4aqurDeq7qFZp7ErYrdiwWPxMoIckb_v_qaOlzN6vt6r4dg04sOMk3YX5fwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ پشت سر هم پست کرد + ترجمه ماشینی
دونالد ترامپ، رئیس جمهوری آمریکا، دوشنبه عصر نتایج چندین نظرسنجی مختلف درباره توافق با جمهوری اسلامی را منتشر کرد.
از جمله یک نظرسنجی مشترک «سی‌بی‌اس نیوز» و «شرکت یوگاو» می‌گوید که به عقیده ۸۰درصد جمهوری‌خواهان، این تفاهم‌نامه «بهتر» برای آمریکا، و یا «خوب» برای هر دو کشور، است.
در یک نظرسنجی دیگر، ۶۷ درصد می‌گویند از تفاهم‌نامه اخیر صلح میان دو دولت حمایت می‌کنند.
در نظرسنجی دیگری نیز ۴۷درصد گفته‌اند که این تفاهم‌نامه اثر مثبتی روی نرخ تورم و توانایی مالی خرید مردم آمریکا خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szTV7bRQpjTO7gg2XgCVps-9Cl2U6T8XnO6Jd_pcLAdxP0DXLIi_1ORpPs4fOw_GAwYaakPsdyPOl5zS0MPc7nJoRjZLOnLQyfuZHzvqV_t3UvqNTCG2AZU_S9TCBLFfxXRWIBoOlr1JYezTCWpN47XwBdPgFWw9Qwgnsu798w8t-o41ILsQl3RhAqQwl0AD2MKB2rnPoacRI9CKuVfpAiHi3uT2V_GL-L9qFCfVfbi_KzdciwBPOgQyQFyBthOshOIJXvtNDFZ3IohLXEWa9jJ9BtOddhY3IER1vm26BsGIKQplXV0nZrl-QcHbzv-aF1SE4-EwyFlDRWkBGNmDrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: اوضاع ما  ‏در مورد تنگه هرمز خیلی خوب است.
‏دیروز نفت بیشتری از هر زمان دیگری از تنگه عبور کرد؛ بیش از   ‏هر مقداری که تاکنون از تنگه عبور کرده است.
‏احتمالاً این را می‌بینید.  ‏ما با یک فوران نفت روبه‌رو هستیم.
‏تنگه کاملاً باز است.   ‏این را می‌دانید.
‏خواهیم دید همه این‌ها چطور پیش می‌رود.
‏اما ما دو چیز داریم.
‏ما یک تنگه باز داریم و کشوری داریم که   ‏هرگز سلاح هسته‌ای نخواهد داشت.
‏هیچ‌وقت، هرگز، سلاح هسته‌ای نخواهد داشت.
ویدیوی بالا:
به تشخیص ماشین، حدود ۱۱ دقیقه از نشست خبری ارتباط مستقیم با ایران داشت.
متن فارسی اون دقایق
ترامپ در پاسخ به سوالی در مورد تنش‌های احتمالی در تنگه هرمز گفت
تا زمانی که ایران به ما احترام بگذارد، نمی‌خواهم بگویم از ما بترسند، تا زمانی که احترام بگذارند اوضاع خوب خواهد بود. 8:15
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه عصر گفت اگر جمهوری اسلامی «به توافق خود عمل نکند یا اگر رفتار مناسبی نداشته باشد، من کاری را که باید انجام دهم انجام خواهم داد.»
5:00
ترامپ: نیویورک تایمز جعلی گفت، اوه، وضعیت تقریباً همان چیزی است که چهار ماه پیش بود. نه، چهار ماه پیش، آنها یک نیروی دریایی داشتند، دقیقاً ۱۵۹ کشتی. آن از بین رفته است. کل نیروی دریایی از بین رفته است. آنها ۲۵۰ هواپیما داشتند، همه از بین رفته‌اند. ضدهوایی آن‌ها از بین رفته است. رادار آنها از بین رفته است... همه چیز از بین رفته است. رهبران آنها از بین رفته‌اند. کل کشورشان از بین رفته است...»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=Vnjl0PGW6rFTNpaAC7cHv24amrR5gf38JrxpF1a096UDUDhpiu-O-EI5A6zxVFsfscu85HXK8e45Se9l_1fcO4yTp0FcgeT_-VtQQpJkssn7aGgO6d36yTshkLZRzPNWiFtvfjd_YyBn2R_KptjHMfJORVcY0wDvdfjl6s4gEx2ReGRNXKk2f3xsgik-6HkpZjo6GCFmk5zJvR0lCbYmS5H7_sVtX5kO525w_h7h-Ndvgbclvmi-i8LZ31wm_iGqU5tfQDzCwV5y9DVD8qrDnnkN6Wlsj0vETsbp44HRJXHsBKp_CNT-Z666UHdDbMxe7tpim6_PWqjWnhkTb0JqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=Vnjl0PGW6rFTNpaAC7cHv24amrR5gf38JrxpF1a096UDUDhpiu-O-EI5A6zxVFsfscu85HXK8e45Se9l_1fcO4yTp0FcgeT_-VtQQpJkssn7aGgO6d36yTshkLZRzPNWiFtvfjd_YyBn2R_KptjHMfJORVcY0wDvdfjl6s4gEx2ReGRNXKk2f3xsgik-6HkpZjo6GCFmk5zJvR0lCbYmS5H7_sVtX5kO525w_h7h-Ndvgbclvmi-i8LZ31wm_iGqU5tfQDzCwV5y9DVD8qrDnnkN6Wlsj0vETsbp44HRJXHsBKp_CNT-Z666UHdDbMxe7tpim6_PWqjWnhkTb0JqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس، ونس هنگام ترک سوئیس، ترجمه ماشین:
🔸
سازوکاری ایجاد کردیم تا مطمئن شویم نه‌تنها تنگه هرمز باز است، بلکه باز خواهد ماند.
🔸
قیمت بنزین همچنان کاهش خواهد یافت.
🔸
سازوکار درستی ایجاد کردیم تا آتش‌بس منطقه‌ای تضمین شود و درگیری‌های اجتناب‌ناپذیری که پیش می‌آید مدیریت شود.
🔸
ایرانی‌ها اجازه داده‌اند بازرسان تسلیحاتی، بازرسان هسته‌ای، پس از مدت‌ها وارد کشورشان شوند.روشن است که ما این رژیم بازرسی را تقویت خواهیم کرد تا مطمئن شویم آنها هرگز به سلاح هسته‌ای دست پیدا نمی‌کنند.
🔸
بخش زیادی از تیممان را آنجا گذاشتیم. ایرانی‌ها هم بخش زیادی از تیمشان را در آن اقامتگاه گذاشتند تا کار را ادامه دهند.
🔸
این دارد بنیانی می‌گذارد برای چیزی که می‌تواند خاورمیانه‌ای واقعاً دگرگون‌شده باشد.
...
خبرنگار: آقا، خیلی سریع؛ دیروز لحظه‌ای بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما دست ندادید و بعد او از اتاق خارج شد. آیا احساس کردید به شما بی‌اعتنایی شده؟ آیا فکر کردید این کار از طرف آنها عمدی بود؟ شما آن اتفاق را چطور تفسیر کردید؟
باور کنید، در چند ماه گذشته زمان زیادی را با ایرانی‌ها سروکار داشته‌ام. گاهی آنها را به‌عنوان مذاکره‌کننده‌هایی بسیار گیج‌کننده می‌بینم.
اما ببینید، ما یک نشست خبری کوچک داشتیم.
آنها آشکارا در ایران از همان حمایت‌های
متمم اول قانون اساسی
که ما در ایالات متحده آمریکا داریم برخوردار نیستند.
ما با شما صحبت کردیم و بعد چند جلسه واقعاً خوب داشتیم. چیزی که برایم کمی خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی توفان در شبکه‌های اجتماعی شکل گرفت که همه می‌گفتند ایرانی‌ها می‌خواهند بروند. و بعد ما حدود ۹ ساعت دیگر با آنها صحبت کردیم.
بنابراین فقط به رسانه‌ها توصیه می‌کنم کمی به آنچه از شبکه‌های اجتماعی ایرانی می‌بینید بی‌اعتماد باشند.
آنها می‌توانند مذاکره‌کننده‌های گیج‌کننده‌ای باشند، اما احساس می‌کنیم در حال پیشرفت هستیم. ممنون از شما.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z-VdM9iNr1UAfkliWVw2zYBiC3iL13wh2gPrNmW3uGJWrqkPfcNLASDRDvYUEI_tDZpLNx3rad_KI2aumXuaFB3UH8UCF0i0TXt5Dmsm7erIPBuSpEBvqwyOTyH0M7BDxIKd_EXX85qkkrJTOsyqfWhqlk_NzzNj1LZENVzFbvbgxox99nGEFvTXIAuQdh8a1OCD7YxkIFW4Uu1u3i3cB2NL6QBT91qNzDgrl17CahS51V-DcykLeYRs7-dh9Nf7Ymq9UozJhzypgh6srQJWrnULFyu-xpcxyr9fX3BoEdRBS9zl1BFIyFvg8qK7TQ2JcwQYGeSoPQzKdPnQuYoxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chsdh69bCGSWamysQV-nkPeu88H0eE63HYwMEHuHGhCGotmmqab818jJqqVGHN16MqA1h86LeoROyYOrvBKsAw6mBJ-s0W0TBaRD4sdqtbj1bGU_yKKteYjxj0-bYIf5A4wdXw4ApJZI2heMTIZ2Xe9P-VDkQ3HRh5ZdeF8ByMaPGPZrXedAmNgIxlHGifNsuk9G2e3uHNlNcdrFycJT8VtYhB3ADv5eEZ5Mu2oKmgX8pYZZYOqRA7OSZnXyzjH2ojGMCeZcmjbWYpELjYVpjCM3jfCIxLA96chwg_e51F4bPeoaarTPUc_bAqIQFFlsRg37RsS8H2vSLicNRspKvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، رسانه‌ها خبر دادند که محمدباقر قالیباف، رئیس مجلس و رئیس هیئت مذاکره ایران، که تازه از سوئیس به تهران بازگشته بود بلافاصله برای دیداری دیگر به مسقط، پایتخت عمان، رفته است.
به نوشته روزنامه هم‌میهن، قالیباف در سفر به عمان به همراه عباس عراقچی،‌ وزیر خارجه، قرار است با هیثم بن طارق، سلطان عمان دیدار کرده و در زمینه ارتقای همکاری‌های دوجانبه و تشریک مساعی «برای تثبیت ترتیبات ایرانی»‌ برای اداره تنگه هرمز گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76598" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cRB6F_x6kMdYLq5umgglzQa4aB0h_aIBvH81pQpW8bKnYvaIpxst6jKCmTZzfWkw4GYxU_vDLt5HFeZCalFRW5FVjHxz6AaG1qqOT36g4y7EFPy4Ih8iaO-fgWsELG28Q7Gq2NACCzZx2vc4NlRdjI3N_hT8PdMyKLn8zkF1w0oPF_R_z2rILz80x_xzYEyWgVXr3fhJjVHySQWlufJuMI2gPwyG1j_F9F7NN42lRKj1HghE_RPytIYMOnWmZ1pkkrvpnKZisaFYhczandPulHBN8cwGZ_uArCnmA9UNz-iTETSnXa58eNiPXBVOBBmaOHo5vOWnxXSHm4pc5kErAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نوشت اظهارات جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره بازگشت بازرسان آژانس به ایران کذب است و در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76597" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=lrOE1MVS53Jsw1lzgUSzRA-MHyruoKraoWU5wrzo0MOb_mk4pPionZHH7cXKOLXzFQrNL-V7zvl5L-YT-FY2Xrh2OVwWNqzUVhLjDqoKj1yUXMe0ZYEJnAPyz1faeS4Gu7NkpQE98-brDDGGLVFRmR9T9vlMZJo3NIWtHOlHA62zLvll-2R6v3DflCW9AHbK5qDyYzJ9z35_ndfUaAVQVZK3cnn-_-_fw7_GjqUmbgpgfDNPjSVsDOWRC22UiOwOTLOdyQ0QonJlU_MfaBqAhnuIY1NCaEtyo8q5RXp1zq5mR6UZCqBPoQADxXCsbaPVYiFf8Pi4nqCpBOd5QBuPVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=lrOE1MVS53Jsw1lzgUSzRA-MHyruoKraoWU5wrzo0MOb_mk4pPionZHH7cXKOLXzFQrNL-V7zvl5L-YT-FY2Xrh2OVwWNqzUVhLjDqoKj1yUXMe0ZYEJnAPyz1faeS4Gu7NkpQE98-brDDGGLVFRmR9T9vlMZJo3NIWtHOlHA62zLvll-2R6v3DflCW9AHbK5qDyYzJ9z35_ndfUaAVQVZK3cnn-_-_fw7_GjqUmbgpgfDNPjSVsDOWRC22UiOwOTLOdyQ0QonJlU_MfaBqAhnuIY1NCaEtyo8q5RXp1zq5mR6UZCqBPoQADxXCsbaPVYiFf8Pi4nqCpBOd5QBuPVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تا وقتی که لازم باشد در جنوب لبنان خواهیم ماند
بنیامین نتانیاهو اعلام کرد که موضع و دستورش به وزیر دفاع اسرائیل تغییر نکرده است.
نخست‌وزیر اسرائیل نوشت: «نیروهای ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم علیه خود یا ساکنان شمال را دارند.»
او تاکید کرد که ارتش اسرائیل «هیچ محدودیتی در این زمینه ندارد.»
نتانیاهو بار دیگر تکرار کرد که ارتش اسرائیل «تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهد ماند.»
در مذاکرات ایران و آمریکا در سوئیس، هر دو کشور تاکید کردند که حفظ آتش‌بس در لبنان از موضوعات محوری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76596" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NRaQjGTkRgD0acScnrz-_ScJTSSfcFwVWP2iFA9GWF76XVxpja4TAeyZrSTg7Uy6Y9D8kTfpPAp-H3J5NeqVf2Nj0WotYfGEKh1VAdLOi74Nl2SWACCTszZP8en8oNvdV0GkmMezUd9kCtPic0Zu1t1zKmV5MCHxFi7Nm0ReQcJLBASgr151xQ6jc1wLbq27xoeAdz_PmuZnhnVic29nyaaXrfdQoD1EGNfYpMgcprOqqKE7QAF44VERcBBZaBd1MUtQ97OOB953c-LqtQKaBeWwV1h_RCjNv2MjGeo-5xy9kLa7FiBrk_KjCP9xxhwGdJ8YU8MsClcDHsJsz3_H2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا با صدور مجوز عمومی، تولید، فروش، حمل و تخلیه نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران را تا ۳۰ مرداد مجاز اعلام کرد.
بر اساس این مجوز، تمامی معاملات و خدماتی که برای تولید، فروش و انتقال این محصولات ضروری هستند، از جمله بیمه، مدیریت کشتی، تامین خدمه، سوخت‌رسانی، ثبت و پرچم‌گذاری کشتی‌ها و عملیات نجات دریایی، مجاز خواهند بود. این مجوز همچنین شامل کشتی‌هایی می‌شود که پیشتر تحت تحریم‌های مرتبط با جمهوری اسلامی قرار گرفته بودند.
در متن مجوز آمده است که واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران به آمریکا نیز، در صورتی که بخشی از فرایند فروش، تحویل یا تخلیه مجاز باشد، امکان‌پذیر خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76595" target="_blank">📅 16:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vR_bZaRuDkE8CQBOwKjfqqHfA1hI6HFgbMH0XP0t6ph5fWxVnV86OqZa_2KS32pYKagovpdNCdmHqLkIxMBpf9i6WDYV1GfN109bVR9nIBw0BynuDfKH03xfd_itTFJXa5VMtIuYOkCHYNt6KSsPS2YEcjyL8jVJpQiYAqCDvlRpRG7wxeDl_ZHNGfLDGch5E39pBYWbAfd11iwzAXz6sTlIKNzeDNAqR4_0qBEAFkzxs9PaArtERm5g9UHNkiapFdgBtyfZ5mBMI4bVLqQZ9vsVRt9i0mtsWD-Tk_t1mU5xQZQrwliCVHBwKG71E9BP0NKxGmdLgx4bjrKEyTMCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش هرانا  در خردادماه ۱۲۷ حکم اعدام اجرا شده، ۱۹ نفر به اعدام محکوم شده‌اند و حکم اعدام ۱۲ نفر نیز تایید شده است.
هرانا همچنین از ثبت ۸۰۹ مورد بازداشت در حوزه آزادی بیان و صدور مجموعا ۴۹۳۳ ماه حبس، ۷۶۶ ضربه شلاق و ۵۱ میلیون تومان جزای نقدی برای ۸۰ شهروند خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76594" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eeyQcpSbLqskNmcGZFUy4VeQ-O5YBjS8_fgq_KTI1Rl4RCP7VKo307etZdlL20vNjZdGtBEaKkaVBQEjMPbeSi7GT3li0N6wLW8p6Bx29jNXKehllgqeA1chYxd_pCKSRqV7bTv-S6LBW_lLGVWyGt6Q-c3cEgHoVvFR8nKzhqFTEaA0fCC2YUjoHyAoH1cgxDy6fkaTHf_NeKhCVlqj8kqbUlJClP3fehklLHAYEfyzzdn_IZVjsUNthorPEeewxHUPBw8eZffUGEtElzCEEIGE8Hv6RKccBBeyxQNX1dlW3UwRghY6lZ-9ithmHuNiJN2lgW6CW1o9Su7-JO_sqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tGX6iXa9tq-bYQaNivYfRfoXeheS6bBFhtx2ucT9AbriJ4RMCL1-EoYZh1UMtUNoG_cwv9OVUAR1DJqc0wRB3U5UC-nRDEUxR03OBvZ5vc0UxbMQ-_1mnoLC6VR-0tjICnwUhc8LOcdru6BrQPH4hQ3mcfSQ29ysqqT9ms2QK66T6Wz4w2EePKwajYkV3c1KldNUuptgSKHA3gBXqW2IxTIiikUr-ntXH_W7tfeOgrX9bNmAZDEpWWOQIAj_esYEHYBX8eyET9U0-RJMft9wz8wdPf9JK6a8-jg-pYXlOFq2Et_x132ObmQk-H_-BWn2cqAM1Vv2wxrZLNDBzCiLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KaFY1pLibhigggjin-YtgR0Q14KSMkD7ZePe8K-G8Wg3NjKsKMSYb_T62MIuHJIlb9wtcwlSqLpfO28LbWbzrG5Fvpvpgdjr9fHO0J6Nk90z4bDzwGNa6dspXZ_wrjBZuFtdna06MPtB3Irt1MFWzpHBnJ63kv0p9MolD0ZCWrzrn1WkVeJhcdElfOOrAcEc0Jaudsw74H-m4rx6U4GlCdNLJEWSpQlyGA5n6KFwuxInCRuzcmOhy9TpJRlg0lKTMUhIAACP9oGR1x0Twp9MuLiHxHm3A9NiVlQ9vJy9JqWu3JJt9YzyXoQLaRBm97VYdpJn6EAPrpZ-mzh-20w-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IGXMSP3qfBjHiOesoUHIbvvwsrJHIy9DmcSmJq1B858cIoD4QT3WI-jOq3BOUMw_xRz9PVLTpybu60U4V1oCCMiowfqM6bb6iVOlnwdFNAIC03j5EpEUO4FdEqYx_7dfXpmJDj34M6fwSuwtHLVVSFCh9GgDsVORwp3nhyna4dB2I9Zp1A4V3sWhaji3S-Sph_EQRtOqnKJfrgfZqhWlIX4vrz3Y-1BVr7I4b99a-HRW_3pE59xKzCw3lCl1f9FfvJ3BYSwiMe4Y_vj3fuKXcTweSpaNChbqRP5RGVO9Sf4RROj-wGG06XvU7GENXHJwm65bC0Bs6go9bKLsAJPfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gBDRW4TPMJWFtaXv0ZLhTsjcR13tNDvqD91DoEHyqCWWxQPX_wiQYbDa8cNGsAZKMVt0HhoC7X9IplKq40Nc9ehff0T1CDJ31p0aDxpm-KHpDYMdGrTtOxKNGSFD9XZ6ug7rpTYhKx--ZQRw36N6d9_MXh45CJ7icD18h-baNZ0o58sKQ-w0rUXc9tNr49dh3uPN3Lzx1jhuwYiTedmEYVAiLwKJT09ku5wvfXUFuTWkP_mZAgVkll7t3wlT8E9JA0NgjNoSk7YZdwj5FYGyuz-E8o40WM8aWRHRP2qhIQi1lMwW5tJylVhfAQfRPLiKpJCgcyH1-PJjEf8Vy1GNtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=WCy06e2v0GJ_RsjP8DWqcMEh7-Kr52na_xHglnsVYCw-pJaveGekzzktH-Z0vKxSWLxqg5r2VfJ-jlbt1-MUugQVHGhj2s2vJ5EIHB56B_KZpngO_sDX89TQand8PJ3HoUloBxCgOZ42aIthN3zVCmF52_an2d0dNxQx-nQgM4zLpHLNjhk2rYSijW5ypqiV-YLdj4_qVuMQrDFXJkIaKSL_mC5d4erSwyW5GrP3tvZ6Ieeg2p-LkA304Oni-GbdMqOW0wwZFJ7z_xKfBSD-F5wuSv3siGtKJKlIy9_ROCImlWtDSgjM_cSCSo2OPBYXe8r9W52uFi_ykyoIw-psUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=WCy06e2v0GJ_RsjP8DWqcMEh7-Kr52na_xHglnsVYCw-pJaveGekzzktH-Z0vKxSWLxqg5r2VfJ-jlbt1-MUugQVHGhj2s2vJ5EIHB56B_KZpngO_sDX89TQand8PJ3HoUloBxCgOZ42aIthN3zVCmF52_an2d0dNxQx-nQgM4zLpHLNjhk2rYSijW5ypqiV-YLdj4_qVuMQrDFXJkIaKSL_mC5d4erSwyW5GrP3tvZ6Ieeg2p-LkA304Oni-GbdMqOW0wwZFJ7z_xKfBSD-F5wuSv3siGtKJKlIy9_ROCImlWtDSgjM_cSCSo2OPBYXe8r9W52uFi_ykyoIw-psUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی گزارش داد «تحریم صادرات نفت و پتروشیمی تعلیق و محاصره دریایی برداشته شد.»
علاوه بر این، عباس عراقچی اعلام کرد برخی از دارایی‌های مسدود شده آزاد و طرح بزرگ بازسازی و پیشرفت اقتصادی ایران اجرایی شد.»
آقای عراقچی این موارد را در پستی در حساب کاربری خود در شبکه اجتماعی ایکس اعلام کرده است.
@
VahidHeadline
معاون رئیس‌جمهوری آمریکا اعلام کرد که در گفت‌وگوها با حکومت ایران پیشرفت حاصل شده و جمهوری اسلامی با ورود بازرسان هسته‌ای به این کشور موافقت کرده است.
جِی‌دی ونس، روز دوشنبه در سوئیس گفت که گفت‌وگوها درباره بازرسی‌ها ممکن است از همین هفته آغاز شود. ونس درباره زمان آغاز کار بازرسان هسته‌ای در ایران تأکید کرد: «احتمالاً همین هفته، شاید از امروز.»
معاون رئیس‌جمهوری آمریکا افزود: «ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم. گفت‌وگوهای فنی در هفته‌ها و روزهای آینده ادامه خواهد یافت».
@
VahidHeadline
معاون رییس‌جمهوری آمریکا، گفت یکی از اهداف واشینگتن در مذاکرات، ایجاد سازوکاری برای نحوه استفاده از دارایی‌های مسدودشده ایران در صورت آزادسازی آنها بوده است.
او گفت هدف این سازوکار آن است که اطمینان حاصل شود منابع مالی آزادشده به مردم ایران کمک می‌کند و صرف حمایت از فعالیت‌های «تروریستی» نمی‌شود.
ونس افزود جرد کوشنر با همکاری مقام‌های قطری طرحی را ارائه کرده است که بر اساس آن، در صورت آزادسازی دارایی‌های مسدودشده ایران، ایالات متحده و قطر بر نحوه مصرف این منابع نظارت خواهند داشت و باید آن را تایید کنند.
به گفته معاون رییس‌جمهوری آمریکا، این منابع مالی برای خرید محصولات کشاورزی آمریکایی از جمله سویا، ذرت و گندم اختصاص خواهد یافت تا در اختیار مردم ایران قرار گیرد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در پاسخ به سوالی درباره تهدید تیم مذاکره‌کننده جمهوری اسلامی به ترک میز مذاکره، گفت: «آن‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم در شبکه‌های اجتماعی چنین تهدیدهایی مطرح شد. اما ما دیروز تا مدت‌ها بعد از ساعت یک بامداد در حال مذاکره بودیم، بنابراین آن‌ها جلسه را ترک نکردند.»
@
VahidOOnLine
گزارش‌ها از سوئیس حاکی از ادامۀ مذاکرات فنی ایران و ایالات متحده، به ریاست کاظم غریب آبادی، معاون وزیر خارجه ایران، است.
رسانه‌های جمهوری اسلامی نوشته‌اند که قرار است دوطرف روز دوشنبه اول تیرماه در مورد سازوکارهای اجرای یادداشت تفاهم اسلام‌آباد و تشکیل گروه‌های فنی مربوطه با یکدیگر گفت‌و‌گو کنند.
با این حال تیم اصلی مذاکره‌کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سوئیس را به مقصد تهران ترک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76588" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qNMbv1rhkBwYMM5DjVleju4QhXVi_iV_PHaTEiWgjwrChd0uxdXze4hEhoQ2oAsCNSBdvgkCNOLNsSOMEAwPNdpF325Ax-fY_W9Zibt998AnhLrvAiNtmn2i8cVppoz8lB_pkGxUbgoXcF_urqx0qTGM11rlThJDbl8NS8B6DrSvueI2VnL8Ku8x5qbYOq5GVvMgp6vKeGxd1U9RZQvtN0mBn-1YHhYk1_MWFmuLe-Gm00ISUIxFCM_ZBk17fM0tGi6VP-cn7OiiskCM_mZx3lMTCtRrFxEw-FU6x-DIrSXf46NMcc09HThDFfFl3jhkKjRs5dYSoYAnmPzkVVCp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانجی‌ها اعلام کردند ایران و ایالات متحده روز دوشنبه اول تیرماه توافق کردند خطوط ارتباطی مستقیمی برای باز نگه داشتن تنگه راهبردی هرمز و پایان دادن به درگیری‌ها در لبنان ایجاد کنند.
بنا بر گزارش‌ها دو طرف از طریق تشکیل یک کمیته عالی مذاکرات، بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیدند  همچنین قرار شد گفت‌وگوهای فنی از همین هفته در بورگن‌اشتوک درباره همه موضوعات ادامه یابد.
در بیانیه مشترک دو کشور میانجی یعنی پاکستان و قطر آمده است که: «طرف‌ها با تشکیل یک کمیته عالی موافقت کردند که مسئول نظارت سیاسی بر روند میانجی‌گری خواهد بود. مذاکره‌کنندگان ارشد به‌طور منظم به این کمیته گزارش خواهند داد و گروه‌های کاری مسئول موضوعات هسته‌ای، تحریم‌ها و نیز گروه نظارت و حل‌وفصل اختلافات را هدایت خواهند کرد تا اجرای مؤثر تفاهم‌نامه و دیگر مسائل تضمین شود. کمیته عالی بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیده است؛ نقشه‌ای که زمینه را برای آغاز فوری گفت‌وگوهای فنی بیشتر فراهم می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76587" target="_blank">📅 05:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jfXHbgwU1clhF8fZkerz2hLYDgEa3u2m4OqNs_bW9t-eZyZ5lpw0jg35LFfD4Ku1HMnXk6jq7_lVsanxY2t5P3AB6onlgQ3h0HI4IBTOhMCeW63U7CrIQU39s4UB3D57CxJ79LTwPaaUiGES99IZEOUCsTRWWZslAi666OaeQ4XuP-p2UPxuWojr8fEYtBFkygNJW6vQbvKk2h5qOm4c2oJTOMJEgHpDVEOLEpPoWvMH4opf-g__WG9QUAROzGIasOAjOescOK5UowQcjhDzF-0T_tgQO_gyNiBSAtY0c7nuZFF7ETrXdCAmQA17frIAMQPqhgKyDRPUA9CEcd_uww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین: ما این‌طور از سرزمین‌مان محافظت می‌کنیم. mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76586" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SIzGvCzKE7txj2visiECaJTE-mq1q-O-qyLyjNegRc6JhQO8HtTWGJmEoa7xAWreXdx8U7P8naWi7kkFRWztJT9oOnNMqjx3natbtFOfpP1mSbNwFz087oKEAOBH-kO2d3nAcYA9EOXE-p-HL0BDEfSUUMwjHpCGxKu1NU2GmKeAPILqorDJbUgdvFCXpov2mFAmxeyLwhLjGMqQcVtpJK2uA6io76jbXTJJlty0ToCqLQCdZrwNcLrr0U5SQ2kOI_o3IW_ZBEYsGO7OPEvdU7M2QpXOvX_xt3SCWi51pVwuIkJkh8qC5UYZ6XC80oRAlzMQc_ZmC_DUJgU7tpWDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e6eePyOFIon1kTMB1x6C852okQizojby2387tMKnsua6gFSXR-i1VdVhpy1jhN9pdr4cOPKbkFFXkQX6OPeSvDpXjL3m083-cJqBB1bKdT44BmQtVz981cPEzGM7EtWZvB6AZ6etA-u1oaoDwWiWg40BPBC6Lus51MWtSiv6bkWzQpSvk2C8u0CYrHMGnaTuAaHaBHZfwKDByYvz1ky6ECFMJehw2edL0j4wdXqznLOm3IYRQ-hPeEOcfkzkweqNiy2YKrj413VCLqcIDs3pi1rh6QQ5Nc5mSKObx-NpBtDBdpqMy0HNdTyJDFd4aBwpt_TPqhKFGdzU1wo3R2gfrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، اعلام کرد مذاکرات سوئیس با «پیشرفت‌های خوبی» همراه بوده و گفت‌وگوهایی درباره پایان جنگ در همه جبهه‌ها از جمله لبنان، فروش نفت ایران، آزادسازی دارایی‌های مسدودشده و سازوکار عبور کشتی‌ها از تنگه هرمز انجام شده است.
او گفت درباره صدور مجوزهای لازم برای فروش نفت و آزادسازی دارایی‌ها پیشرفت حاصل شده و قرار است سازوکاری برای موضوع تنگه هرمز نیز تدوین شود.
بقایی همچنین تایید کرد هیات جمهوری اسلامی پس از انتشار آنچه «اظهارنظر تهدیدآمیز آمریکا» خواند، از ادامه نشست چهارجانبه خودداری کرد و مذاکرات از طریق میانجی‌های قطری و پاکستانی ادامه یافت.
به گفته او، تهران بر اجرای تعهدات طرف مقابل، به‌ویژه در زمینه آتش‌بس و تعهدات اقتصادی، تاکید کرده است.
بقایی افزود گروه‌های فنی دوشنبه مذاکرات خود را برای بررسی جزییات اجرای تفاهم‌نامه ادامه می‌دهند و قطر و پاکستان نیز متنی را به‌عنوان جمع‌بندی توافقات حاصل‌شده در جریان ۱۸ ساعت مذاکره منتشر خواهند کرد.
@
VahidOOnLine
تسنیم به نقل از بیانیه مشترک قطر و پاکستان گزارش داد که نخستین جلسه مذاکرات نمایندگان جمهوری اسلامی و آمریکا در بورگن اشتوک سوئیس و با میانجی‌گری پاکستان و قطر به پایان رسیده است.
در این بیانیه فضای مذاکرات «سازنده» و روند پیشرفت «دلگرم‌کننده» عنوان شده است.
به گزارش تسنیم، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
براساس این گزارش، «مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.»
تسنیم می‌افزاید: علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.
@
VahidOOnLine
عباس عراقچی بامداد دوشنبه، با انتشار پیامی در اکس از پیشرفت‌های حاصل‌شده برای پایان دادن به جنگ لبنان در پی میانجی‌گری خستگی‌ناپذیر پاکستان و قطر خبر داد. وزیر خارجه جمهوری اسلامی نوشت: «صادرات نفت و پتروشیمی معاف شده، محاصره برداشته شده، برخی از دارایی‌های مسدود شده آزاد شده و طرح بزرگ بازسازی و توسعه برای ایران آغاز شده است». عراقچی با این حال تاکید کرد که اولین آزمون واقعی و جدی این دستاوردها، عملکرد «سلول مدیریت منازعه لبنان» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76584" target="_blank">📅 05:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTJ1kkJQXZYgg8FmZyEr_UZdefOKzQsott0ZneJRTS0VbX31dCs07Tm7v0vDjV72M2VOvP5WAGRE0oH8ph7bIGqiF9c0kyXsR8bY68G7pV5Q70lCGp8f763EMXBRs4ll77mD58ptct0-UfS0yhBBdDKsMN8ada8mCgb44H-JIkUP2JeaHKC8uREdxkJvHwsq269ALRFdFPXF6axnMBf10t4bnNEBQ_dwSm96Y3Jw5ohhJCJ2w4sPm3q96Pec6cnu4qdm56vYSPC8gwq8u_v7uQmDEKy7xth66jB9TzeO12-yTqe47Mi87-uyqDktNrIwqSveYXh1v4VAkJodS5Ru6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، از دو روز دیگر، یعنی ۲۳ ژوئن (دوم تیر) در سفری دو روزه به خاورمیانه به امارات متحده عربی، کویت و بحرین سفر خواهد کرد.
در این سفر، آقای روبیو درباره مجموعه‌ای از اولویت‌های منطقه‌ای گفت‌وگو خواهد کرد؛ از جمله:
تفاهم‌نامه میان آمریکا و ایران
تلاش‌ها برای تضمین عبور کامل، آزاد و ایمن کشتی‌ها از تنگه هرمز
اهمیت حفظ صلح و ثبات در منطقه
وزیر خارجه آمریکا همچنین در بحرین با اعضای شورای همکاری خلیج فارس دیدار خواهد کرد تا درباره اولویت‌های مشترک کشورهای منطقه گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76583" target="_blank">📅 01:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TvME5E5wKCJeW8pqWKfVPSNth0JnSBicuNPXNTYzP4gZrQRofDOs-6UsbnPB78ikNyxdiI-h_nkOxDovVdsnOe0cBirflh_9ZZQ_ESObxureY6tIQm7NNe3_Lw8UadGCLS1zLVlGIFqXkysf9Y9Kh_k1GaBSgVhd238oG1E9T6-Uthft9AcS7wYD4pbRgG0bi11zBcU1EvlPf4zcLVf4WTpwtUHFb_Y8z1QAx0LHyU9PZ68y7vc62sbODnhOqnH37RlGeCuoVogGf86-Q3CT4s_KLS3bmE3M7C_5Oe3MjuOaYEd5tPgu3oS8u4vPpNIKSEtw7KBLB6nSMYnCt2obNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین:
ما این‌طور از سرزمین‌مان محافظت می‌کنیم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76582" target="_blank">📅 01:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nEgAQ_MI4xZF_PpC-cPpW9P_zGwSNHHINTcx4TLAGNrg2CXPdXJxKgdHLi9vx1fFIPuWODudGgEQjgHeFuzAhdowbfEjuL1n-TjHJVnIF6aUVlvyd_nDHR9d1fsewy2RissZR_q7OV-eRgUlN71pM9FTcQQncG7SEbavafxP_f5mmYU4PSlwu3LbtLrhm9CMBYjgXAcvT9faAk4HxHKacNrzjlyqWjjgmgCxAjaqtv54mg1ycal43e1KIRssFsH6uj8b9dfvZqJio59BS8ZF5_KZLKteAoQIHfw8Rf9DsKUklDzPzc4kRWfU-CgZF7VGmk6CzvbUXlwKlpUae_6eOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست ترامپ علیه نیویورک‌تایمز درباره اخبار جنگ:
تیتر نیویورک‌تایمزِ فاسد و رو به سقوط این است: «بعد از تقریباً چهار ماه جنگ چه چیزی تغییر کرده؟ تحلیلگران می‌گویند نه چندان زیاد.»
واقعاً؟ ارتش آن‌ها از کار افتاده، نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آن‌ها تقریباً نابود شده، دو رده بالای رهبرانشان از میان رفته‌اند، تورمشان به ۲۵۰ درصد رسیده، اقتصادشان درهم شکسته، به سربازانشان حقوق پرداخت نمی‌شود، تنگه هرمز باز است، نفت با شدت در جریان است، و بازار سهام و اشتغال در آمریکا به بالاترین رکوردهای خود رسیده‌اند. این‌هاست آنچه تغییر کرده، ای ترسوهای فاسد و بی‌اخلاق، و حتی بیشتر از این‌ها!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
نحوه پوشش خبرها درباره ایرانِ بسیار ضربه‌خورده و آسیب‌دیده از سوی نیویورک‌تایمزِ فاسد و رو به افول، از طریق «واقعیت‌های» جعلی و ساختگی، به نظر من «خیانت‌آمیز» است. من همه گزارش‌های دروغین و مضحک آن‌ها را به شکایت چندمیلیارددلاری‌ام علیهشان اضافه خواهم کرد. آن‌ها مجرم‌اند!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76581" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/plnTLNa7Xehn0oJw_BiR0nGE-Wg3gsxbssAzSM_9460bOGv5vPBoWMpJURLddNG4b4gpGA5BWqgOofzwcaso03-1CTgUx6sG2onzD-XLglteyIGlQOiSZXL_MtHBhL-ZWw5LQBIM5EtfipSQ6iYElQPd8TY_VNHdaUXwuMHM1ACsLIL4OixgX4WKrHz67I1RFL2d-TrR0CdGn0YiNcPRQnkepySnFsAcTPe-oT0K3LnnUvv5DJ4mfzY_mibOhJoW7mX-cH3I033y_U2Sx1qYXwZ0nNwU7EXHB4R2QKdmzUuEaEcHz1-d5kFJ0rleL3m5F1cIzkazbjv8Gk_YB5AQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LxKG9G_uHni_2dPwUSs3ptMU2cZQbT6ZFrr5UQTsem9eelMLrHfXpFzcD1FKJ7ehc4LpvRWCRZVVD4O1oLT7MZHNWSo7YlCauKaWQebGVIG8zywqE8Ne1pmjYTzCqbC_mfRfjvWLwOKRjS3OaRK0JFZMgTuJ7I6yrgqZR7t2yi-xXa3mWSD-La_AvC1ApQcVU2FbeHjJRYxI635eitoKz4atJ6qwwSXAz1WRib3n-967rfk0-EsxofqCxrDC4pYG6i71Fje2BJpCTH2CkVh7GJD7f3M4ZYZVFgsq1qu1pB63cMKjlCSTOSo81nf5AlGxEUjUIQuV0_0O_Ees-GWM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JCufkJliSfGjFgCA2AFS0CCYGDIdEJv0J8cNCCU1dzCQCcR2ub5uRj_QbegX8Qh2c2PonvdztmQkUzppjWIfnoZJqwBDmOBKMpEVQOu8tIHs7zgWjflRODkss9A541u37yQ2WxSliqv8AHnyRkeunNKjRND_XtsByWnn8jYE56RlNad_J2CB4azaJdw0Tw91k3x_Wk3eYrUaxIFsH1L3hvF5D-W4DaTeCJ-c-Co_zCXv5-nWqunAbcGCx_DQDHmUXYrXCde9No5UlQrK8L4X8md_6JVPW4n3WA6trOyQAqC2MtSg7SF0qqvf213V2AQjjJ2I4N3yQ_eHaCVi3Vn9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mlAHJpkT8A7qPO3BL-C_0FnGMRZ9cb3oEIiV0szMDlNbqZrmV36CrHwN_Dhh42AAfny33qVQ5EbK8kMnAMMjt4ixc9T9Kcw0_rX3veLsx-ZhQeZA2sZLsFi-dOT2gkbGIx10FlKPrCFXviqxU82D1GpKyIiHscjpc2S0yvjm1PI5kRLnltFudnWlK9FD2BM-x-M1fDKoeceZrPK4GyhcrDXa7Ey_6m047A_yKPiw_LbnsGNzBNwEBpuP7aWR2aX2uIkL3Tz_MIRT07C3WjTyftS7RmXhwcGV6L89uWBa5Rab8SLGzxApsjydWOXyIbU1WUMOv00r8rO2Qylkag7WGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qIAUtelXCMcMLr0bA2HywODsasuv-JRBHbUHt_-0OYlRoGFR7akU80QWHsXzNaFoVNuwttXziDZRaz-X47pohua-2FGBgGlJ2L5dqIi3yyAXtM5wUlSAB3ISrkzCBatICDHM6g_YSQPJoPOCvbw1T86QTqcTS1bGfWXFqYqGOTYhfz6y64ZpXKVka1q_oVRbbi0Y8nxhjDXMhdwmfnUuwxGQk0jptVdMFZJGLy-aaQchUEaT4Mj96xe5aDuEAv9UkCzY0cuyuTrvzKuunu8kyiRdQ67oUhoWg9iGEX_fpEYTahQKiyFucuhF6D8zVphVd4XB-5HA_XBRe7KJRxz_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lw3caWH9t8COH8iKi5Xa_c9lSfiwQ8r28rGibx4ThwRMPcvc2hTnrSEvcSTQpiEt8CHcK9zHWnnxnmb_qe9AibzFddNDqntYU14RjDr_y-0jShv45INwsLfWBQhMHLIzuBgOwDoTUtWth1GytlgteS0ni5N4lBDe8Bjoa3yGtb1N8CY9Xmh4NOgGUUVnztiluWSF2vuAShMSbvRU_24293ulxnTPq6UJ005cyvb6MGGKvFdDrGahvwUWTagJK6GdHP-ZprXOsnJ-Zd5nOPf4_yOGBI9cM1rGUhZ29g5EX9O_gOdi6909HsrggmC_JDYa5oCAarQSVoQ-CDkbtsuzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q6omDHWxjj2PZggfaWDQ0bT5AdbnVZRj9LwMcSgzMjNntWwWreeLGwiUXeUwcDJMSdy9rK5__MQqr3RWdGfrWutKnA_53de4JrhukC19ZRoWjkZMFmiG-b-LgJclPCciJuFQd3CHKnL9ATnWPq1lzWnICk6aX2j1WJ93Hm0g8bT8dQm5E0ry1nVGcy6WXQApopKeFuWRr6vtU7VDGphHo6ac7Bx2HbDz3lCvKufShSXtEHSwG9o8o1fjJXrvtxRHTX-byb2XIMoeeVNhmJNkHxasmLpg4UWIbl64AI_IJbkSpGAR_ojHf_MGs5M111tL6tgitIzvkeHzqhuihjuuqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=a2q2lVxtyYC-WsKSE5SgTGsXKfvjQ7V7eo46lKXod2ylrZV0hY8OcYlaUj6DOBbXd7unszNp3FBFJUpQQ3xOuApidSDDTKbHUXE9a8P4wsSiUx6FH8mlaXsKckrTa7KcfLRC712htJ0kaAhtqW6ewJfPLx3Rjy0V3b6Wb8NmLgSGwwB3b1TwK9WqitLQBnX4bf0sOqRu6wxnZAEmy_LqhJo1IfaacGZkxSMVnowj1OSMRd-LxZUmMfEWksvS5RAvexm55L4GQBGXe3REInxdxOHaSesQF14QqE6TasfdxY5lvzOY8A6vIASQHL3QFGmoCrXbw2GwhjZG1ULIC016PA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=a2q2lVxtyYC-WsKSE5SgTGsXKfvjQ7V7eo46lKXod2ylrZV0hY8OcYlaUj6DOBbXd7unszNp3FBFJUpQQ3xOuApidSDDTKbHUXE9a8P4wsSiUx6FH8mlaXsKckrTa7KcfLRC712htJ0kaAhtqW6ewJfPLx3Rjy0V3b6Wb8NmLgSGwwB3b1TwK9WqitLQBnX4bf0sOqRu6wxnZAEmy_LqhJo1IfaacGZkxSMVnowj1OSMRd-LxZUmMfEWksvS5RAvexm55L4GQBGXe3REInxdxOHaSesQF14QqE6TasfdxY5lvzOY8A6vIASQHL3QFGmoCrXbw2GwhjZG1ULIC016PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال ایران در دومین دیدار خود در مرحله گروهی جام جهانی ۲۰۲۶، با ارائه یک نمایش دفاعی، در ورزشگاه سوفای لس‌آنجلس مقابل بلژیک به تساوی بدون گل دست یافت.
مدافع بلژیک در دقیقه ۶۶ از زمین اخراج شد و این تیم ۱۰ نفره به بازی ادامه داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76571" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GFvFbHNt9nfJD4DiRDFzU24632bvuIQfrFsq5McPbCYlxliv9Oem2XK5MaJqTmS3mjnIsDeYFUjHZKLcHITIOu1udO84VDxHZ9-bGdten1yCLeu5Rgv9_EoywrzbKZ1RkniV6zIGNLDzNPRMDgXtpAlEM9-O18WJRun2bOwIQmDBnF3tix5OAaDKmicozCufe5AZsMbnUunFXI0-e6L3uG8VqQvEwdYPdkBIZLvf_iAQJ-BFC_s-N-NZ_ujaHWfSzsTs1gc1rW5E33ud-o7dy3IJEq1pT8JyW7V7E7m7CZgIdWqEa4ZMtFQwlIe5jx_z31tupPIO_5uWOjlb1Dp7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
بعد از آن‌که تریلیون‌ها دلار خرج ناتو کردیم، ایتالیا و نخست‌وزیرش حتی فکرِ درگیر شدن با جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آن را هم نمی‌کنند. دهه‌هاست که ما از آن‌ها دفاع می‌کنیم، اما وقتی پای آزمون به میان می‌آید، آن‌ها برای دفاع از ما و بقیه جهان حاضر نیستند. خوب نیست!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76570" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sPUxsWsMjbpLR8jgG-2pJULMh-I1gjoXatq-2k36Bg4dyXpz0r4pj4nSxzv4py_GOq1DNNrnSbg0NimWYXSZCOQW_W9Y_8DynRUKTa_TheMDgjIkDrGOVNXMVJinqEAsWypW9CVzMnbXoBdY-agWQmFxgp8vVkRXXYwEJtgk41pFeNAn2c9Y1IwEqXRtpoD0KDheWGmc3Ctcaf6rxL2osLDhz4k6rtJBVG7RPntyMqKGRjWyCXy27Eq8ufSzheE2-MChW4fnC7BNnsPcVgI4J2eajZ7DJky5TKG-kakpha_PTXBUSs8J_66-3BWx4IkODR9bXIqhefMBEDjBqEJrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ک مقام ایرانی یکشنبه شب ۳۱ خردادماه به خبرگزاری رویترز گفت مذاکرات میان ایران و آمریکا در بورگن‌اشتوک سوئیس متوقف شده، اما پایان نیافته است. این مقام جزئیات بیشتری درباره علت توقف گفت‌وگوها یا زمان از سرگیری آن ارائه نکرد.
این اظهارات در حالی مطرح می‌شود که گزارش‌های متناقضی درباره وضعیت مذاکرات منتشر شده است. پیش‌تر باراک داوید، خبرنگار آکسیوس و کانال ۱۲ اسرائیل، در شبکه اجتماعی اکس به نقل از یک دیپلمات حاضر در مذاکرات نوشت که هیئت ایرانی محل مذاکرات را ترک نکرده و گفت‌وگوها همچنان ادامه دارد. با این حال، خبرگزاری ایرنا دقایقی بعد به نقل از یک مقام هیئت مذاکره‌کننده جمهوری اسلامی گزارش داد که مقام‌های ایرانی پس از دومین دیدار با هیئت قطری، محل مذاکرات را ترک کرده‌اند.
@
VahidOOnLine
خبرگزاری ایرنا، رسانه دولت جمهوری اسلامی، گزارش داد هیات جمهوری اسلامی پس از دیدار با هیات قطری، ساختمان محل مذاکرات در سوئیس را ترک کرده است.
هم‌زمان، یک منبع نزدیک به هیات مذاکره‌کننده جمهوری اسلامی به شبکه سی‌ان‌ان گفت گفت‌وگوهای میان جمهوری اسلامی و آمریکا در سوئیس متوقف شده است، اما پایان نیافته است.
به گفته این منبع، گفت‌وگوهای غیرعلنی همچنان ادامه دارد تا طرف‌ها به میز گفت‌وگو بازگردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76569" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KgF-7iO7ZuMw3ENEpIEeAIHR-JddH9GqjCL3ebToxBoVEM9MNgQTzbvodmG26esnxUAhzfyQpCplbnYhlQq6tPqoAQ4bNDPCJzk6JRzb2kV_-sZtaP90ZTxOk93NY2kFBGJHOWnjO0Ih6Fsch0P_QMY3VZAs30b3y4owFDfEW0ZmuLYcECFa4d1fIJisG44ZK46qhHJ9Wphn1_OT3dvkld3-ZgszNqSvFyNPrH2-aMulPuXrq_PDA6Q1z39bDriYhqCEnKSOj5qJ8r1f9SzpahZ6FE2E-ziUSiKo9p0eXAliLtoHw6wkPdfiYEZXKwohZJAb-hkH4_dRmfGQ3xKatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
"
ادعای فارس و تسنیم به نقل از "یک منبع نزدیک به تیم مذاکره‌کننده"
پیش‌تر در
اکانت قالیباف
همچین توییتی منتشر شده بود:
با خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76568" target="_blank">📅 20:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eyZ1IsMGKa_HGbASxcACsxKSx01n9o7ILn9jmyCIhDfDTPvNO4HRZSRMUraybW8DdsR-1arVKchQRczFuvRvXYxQhZPYn4EoJ2kZ-rWVJltS4upkw5GKxDDKHWLnr7kAfdx5jHNCcLuFtRmsnPDeQ68ikQO8xHWv9EJ_rxoOCzcvTS-QnJnD7TUR0P2tJ5ZXAJ1szmtsL-7yRyVrw9NK96L9ooiZ3qus-d29nrO-IX54Y-1t5Q9k-l5YFPDc19awF9KaPS9OxhxYnwkR7bSRbkBJEp4EooM7DfYndD8AptfnWVW_ZuBNGX1EgDCVzJApEK8xBs7kVXhpBPBZFHoSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در واکنش به اظهارات مسعود پزشکیان، رییس دولت جمهوری اسلامی، درباره ناچار شدن آمریکا به پذیرش تفاهم‌نامه میان دو کشور، هشدار داد که تهران باید در مواضع و رفتار خود تجدیدنظر کند.
ترامپ در گفت‌وگو با فاکس‌نیوز گفت: بهتر است مراقب حرف زدنش باشد. بهتر است رفتارش را اصلاح کند، وگرنه ما کنترل بقیه کشور را هم به دست خواهیم گرفت.
این اظهارات پس از آن مطرح شد که مسعود پزشکیان روز یکشنبه ۳۱ خرداد گفت: آنچه مسلم است از حق غنی‌سازی اورانیوم هرگز کوتاه نخواهیم آمد و طرف مقابل نیز ناچار است آن را بپذیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76567" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JzIixKutuhrYqx6U6YnZ9uI37TMspEM-g0wTzCCMLx90ZZHy8-j2US_h5osPZZTwR-Qwtnl1wWGoMOxMf9rh5TWKS-y5K1hqkjGTWVTe7NxKiqlsWTW4gUlvpMt4JHppLa1K_RAiVFzRrROyLyShW44lmziuBL1LCG-_xaFKV0s4X67QQ--Aa94EZjwImiv-eVNkDt7lZXpJtrcv1jPlMSZ8KxZZsKx5s-g_uCm3N3neMtJhssdGkViTmOK_RK-gERO77IbsrB9l7mfsLgTXUJOvNXKkN4G8rJbUI3osdWVV8N9zT6dtmj7-B-itpcr_uvUYWKxQeocjpt1P54gBoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد همزمان با برگزاری مذاکرات در سوئیس، به مقام‌های جمهوری اسلامی درباره هرگونه اقدام برای بستن تنگه هرمز هشدار داده است.
او در گفتگو با شبکه فاکس‌نیوز گفت این هشدار شنبه شب به تهران منتقل شده و تاکید کرد در صورت چنین اقدامی، ایران با پیامدهای سنگینی مواجه خواهد شد.
ترامپ همچنین گفت به مقام‌های ایرانی گفته‌ام که اگر تنگه هرمز بسته شود، «دیگر کشوری نخواهند داشت و حتی امکان بازگشت به کشور خود را هم از دست خواهند داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76566" target="_blank">📅 17:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/POi2_wKjc-kiTtgeL0UCmISCoCcDEyIMhQvqzrKmF_DrXCkGnSPS9iyt65zCGdBUSeIkfjDf-FcBZ1AJ5Fu91ns5vC8RFasyF6vOUcN9HC3G8RzKKljwP8Z4kVg1XDaHhqFAuNtAB6vlvX-IwZPGWrN-B_MpVZ-0jdE0XHpHIzDUTkpmqdoZEMeOPy5IJC7gVYHjC-MKtJhzjIS8uaWwna59ZHs9GmAFS-MuiN9GvjXeUfN1lQlx55a6w2S5x0Wqf1XQVhK9dCqSA6fO4QLVguzudB6cNjbNJ7A8dNuv_izX_Khw5Cf8uvQxtgQTFvO4_CtWdfBPtu7kj43e73M5-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران باید فوراً جلوی نیروهای نیابتیِ بسیار پرهزینه‌اش در لبنان را بگیرد تا دیگر دردسر درست نکنند.
اگر این کار را نکنند، دوباره به ایران ضربه‌ای بسیار سنگین خواهیم زد؛ درست مثل هفته گذشته، اما این بار شدیدتر!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76565" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=qB3fuy89SRWJ5Z7RSJ_wugVGCBw0877HVG_UQnnOVXEWCY5iCjzUiA-xQMiDKH5sgOfYL94JfHLaqXsOqeuxdgRwRpad6XoaittFzkay38VWvfxa4_wJ2SOuvMbUpvZYLayhbg1r6Q_8cwlYNT9DdgSh4F8MGLpj8RPeSaaKn9mli9g7FAZHa1Eknp7wcEMynVwTjVrAUeHR1VbYy08ejna8Vp8vQZEJMewAKslglHx0oBr4Tma1AEN0b9gzs3PvcSzOkq1HzI--F8AsPo8T4J1tYt9SHNNvDg6A53MQ-MdqgvPQMErSIdAdfRGRh6FoBOzLb4HDtDLNGa_tspcbnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=qB3fuy89SRWJ5Z7RSJ_wugVGCBw0877HVG_UQnnOVXEWCY5iCjzUiA-xQMiDKH5sgOfYL94JfHLaqXsOqeuxdgRwRpad6XoaittFzkay38VWvfxa4_wJ2SOuvMbUpvZYLayhbg1r6Q_8cwlYNT9DdgSh4F8MGLpj8RPeSaaKn9mli9g7FAZHa1Eknp7wcEMynVwTjVrAUeHR1VbYy08ejna8Vp8vQZEJMewAKslglHx0oBr4Tma1AEN0b9gzs3PvcSzOkq1HzI--F8AsPo8T4J1tYt9SHNNvDg6A53MQ-MdqgvPQMErSIdAdfRGRh6FoBOzLb4HDtDLNGa_tspcbnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس و عراقچی در یک قاب
خبرگزاری تسنیم به نقل از یک منبع نزدیک به تیم مذاکره‌کننده جمهوری اسلامی گزارش داد که هیات آمریکایی و برگزارکنندگان نشست ژنو قصد داشتند پیش از آغاز مذاکرات چندجانبه، مراسم عکس مشترک و صحنه دست دادن میان هیات‌های جمهوری اسلامی و آمریکا برگزار شود اما محمدباقر قالیباف مخالف کرده است.
به گفته این منبع، محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، با این تشریفات مخالفت کرد و اعلام کرد اعضای هیات جمهوری اسلامی در مراسم عکس مشترک با هیات آمریکایی حضور نخواهند داشت.
این منبع افزود در پی مخالفت هیات جمهوری اسلامی و خودداری آن از حضور در این مراسم، پخش مستقیم و برنامه عکس مشترک لغو شد و پس از آن هیات جمهوری اسلامی وارد محل برگزاری مذاکرات شد.
به گفته این منبع، هیات آمریکایی از هیات جمهوری اسلامی پنج دقیقه فرصت خواست تا خبرنگاران محل مذاکرات را ترک کنند. او افزود مراسم پیش از آغاز مذاکرات، بدون حضور هیات جمهوری اسلامی برگزار شد.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز یکشنبه در آغاز مذاکرات ایالات متحده و ایران در سوئیس، این گفت‌وگوها را «تاریخی» خواند و تأکید کرد ایالات متحده آماده است روابط خود با ایران را به شکل بنیادین متحول کند.
ونس در حالی که در کنار نخست‌وزیران پاکستان و قطر ایستاده بود، در اقامتگاه بورگن‌اشتوک در کنار دریاچه لوتسرن گفت: «این یک دیدار تاریخی است. پیش از این هیچوقت رهبران ایران و آمریکا در چنین سطح بالایی با یکدیگر دیدار نکرده‌اند.»
تصاویر و ویدئوهای منتشر شده از محل نشست نشان می‌دهد هنگام حضور معاون رئیس‌جمهور آمریکا در اتاق محل مذاکرات، عباس عراقچی، وزیر خارجه ایران، نیز حضور دارد.
معاون رئیس‌جمهور آمریکا درباره اهداف مذاکره با ایران گفت: «آنچه رئیس‌جمهور از ما خواسته این است که فصل تازه‌ای را آغاز کنیم تا روابط خود با مردم ایران را متحول کنیم و دست دوستی را به سوی آن‌ها دراز کنیم. پیامی که به مردم ایران می‌گوید اگر رهبران شما حاضر باشند از نقش‌آفرینی به عنوان عامل بی‌ثباتی منطقه دست بردارند، و اگر حاضر باشند در بلندمدت از جاه‌طلبی‌های هسته‌ای خود صرف‌نظر کنند، آنگاه ایالات متحده آماده است روابط خود با آن کشور را به شکل بنیادین دگرگون کند.»
او ادامه داد: «این بدون تردید هدف ماست.»
ونس همچنین گفت: «ما تنها در چند ساعت گذشته پیشرفت‌های بزرگی داشته‌ایم و انتظار دارم در ساعت‌های پیش رو نیز پیشرفت‌های بیشتری حاصل شود.»
او با اشاره به اراده ایالات متحده برای «متحول کردن» خاورمیانه، افزود: «ایران در گذشته یکی از عوامل بی‌ثباتی منطقه بوده است. اکنون آینده‌ای را می‌بینیم که در آن همه بتوانند برای پیشبرد صلح و رفاه برای همگان با یکدیگر همکاری کنند.»
@
VahidHeadline
جی‌دی ونس پیش از آغاز مذاکرات اعلام کرد واشینگتن طی ماه‌های اخیر بیش از هر کشور دیگری برای توقف درگیری‌ها در لبنان تلاش کرده و این روند را ادامه خواهد داد.
او با تأکید بر اینکه «صلح آسان نیست» گفت رسیدن به توافق نیازمند تلاش و «بده‌بستان» میان طرف‌هاست و افزود هدف آمریکا تنها صلح با ایران نیست، بلکه دستیابی به ثبات در کل منطقه دنبال می‌شود.
ونس همچنین مذاکرات جاری را «آغاز یک گفتگوی فنی» توصیف کرد که قرار نیست همه اختلافات را یک‌باره حل کند، اما فرصتی فراهم می‌کند تا طرف‌ها برای نخستین‌بار درباره مسائل اصلی به‌صورت مستقیم گفتگو کنند.
به گفته او، حضور رهبران سیاسی برای تعیین چارچوب مذاکرات و حمایت از تیم‌های فنی است و با وجود چالش‌های پیش‌رو، طرف‌ها با انگیزه برای ادامه مسیر آماده هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76564" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=O1OshgoajHpFx-hg_UtSIc2SjBVxlA7zDFKhwgO7UCFwMFTRBjmXdVL1tZZiVfiabMu__xEHAPbnamFrhmJQmUJ6eevjJv0bsrHYvEYOaDbo75lTnfInkKWK-tbL2xqb7G1BZqMeeqlDZhTYRjxuEzty3fPgd-h5agmouj54z19y_GiT-iW_pzdZOqitMrdTKcP6vLod4yGeR2joJ77Jh0M7cOpbK8VTRamUDKaWl9o__paooFSrgXaPVwt2eZb98QuCZXfH1sR2lVt2-7sKXVC0W0JYIfEI84ZLKA-s5k8ZhVmsw_VldVb0JTGW6MdsQxGmxg_Emk--YcVvvfRGOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=O1OshgoajHpFx-hg_UtSIc2SjBVxlA7zDFKhwgO7UCFwMFTRBjmXdVL1tZZiVfiabMu__xEHAPbnamFrhmJQmUJ6eevjJv0bsrHYvEYOaDbo75lTnfInkKWK-tbL2xqb7G1BZqMeeqlDZhTYRjxuEzty3fPgd-h5agmouj54z19y_GiT-iW_pzdZOqitMrdTKcP6vLod4yGeR2joJ77Jh0M7cOpbK8VTRamUDKaWl9o__paooFSrgXaPVwt2eZb98QuCZXfH1sR2lVt2-7sKXVC0W0JYIfEI84ZLKA-s5k8ZhVmsw_VldVb0JTGW6MdsQxGmxg_Emk--YcVvvfRGOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، همزمان با برگزاری مذاکرات مستقیم میان ایران و آمریکا در سوئیس، گفت همه نظامیان در شورای امنیت ملی موافق مذاکره بوده‌اند.
او در جلسه‌ای به مناسبت تشکیل بسیج اساتید در دانشگاه تهران، در میان صدای اعتراض عده‌ای از حاضران گفت: «همه امضا کرده‌اند که این راه را باید برویم. حالا هر کسی می‌خواهد تفرقه ایجاد کند، این گوی و این میدان.»
او با اشاره به نظر فرماندهان نظامی در شورای امنیت ملی گفت: «فرمانده قرارگاه [خاتم الانبیاء]، فرمانده ارتش و سپاه، و نهادهای امنیتی همه بودند و همه یک حرف زدند و همه متحد بودند و همه آن چیزی را که می‌خواستیم عمل کنیم را امضا کردند.»
این سخنان پزشکیان در پی افزایش انتقاد اصولگرایان تندرو از دولت در پی انتشار نامه منسوب به مجتبی خامنه‌ای صورت می‌گیرد.
آقای پزشکیان همچنین با تاکید بر نقش دولت در حمایت از نظامیان در دوران جنگ گفت: «۲۰ میلیون بشکه نفت که مال دولت بود را به هوافضای سپاه دادیم. ارزهایی که داشتیم را به این عزیزان دادیم.»
@
VahidHeadline
مسعود پزشکیان، رییس‌ دولت جمهوری اسلامی، گفت نگرانی اصلی او این است که دولت نتواند رضایت مردم را جلب کند و نارضایتی‌ها به اعتراض‌های خیابانی منجر شود.
پزشکیان گفت: «از آنچه می‌ترسم این است که نتوانیم به مردم به درستی خدمت بدهیم، ناراضی شوند و به خیابان بیایند و اعتراض کنند. آن وقت ابهت ما فرو می‌ریزد.»
او افزود مهم‌ترین قدرت جمهوری اسلامی، وحدت مردم است و مسئولان نباید اجازه دهند کمبودها، کسری‌ها و نواقص باعث نارضایتی مردم شود. به گفته پزشکیان، بروز چنین وضعیتی موجب «خوشحالی دشمنان» خواهد شد.
@
VahidOOnLine
بعضی از جملات پزشکیان به انتخاب خبرگزاری دانشجو، وابسته بسیج:
🔸
اظهارات عجیب پزشکیان: من از این میترسم که نتوانیم مردم راضی کنیم و به خیابان بیایند اعتراض کنند
🔸
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد بود.
🔸
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔸
۶ میلیارد دلار پول ما در قطر برخواهد گشت.نتانیاهو اولین ناراضی از مذاکرات است.
🔸
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم، این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
🔸
شورای عالی امنیت ملی در وحدت و انسجام تصمیم گرفت؛ همه یک حرف زدند و متحد بودند
🔸
مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده/ آنها پذیرفتند که حق ملت ایران را نمی‌توانند نادیده بگیرند/ قاعده عوض شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76562" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdq0j-ApxS59kjBVr4ZeN0GS98TE8esYHAmVnlDUl6VHpQgpYwMeWRtAj0DsbjWeawPIUHytKq2qgiJZt3dKbeSOiKpMx_E_HblCTrs2O-B_ZvDgfnrYuUwKvxHQriDsCnXkvPLOwt6rNl5_PmVMcoql0ou_YT76TxYMTxOt-iRSaverkg1SGAzsv3oVrNdY7SZqkegS4_vP5h_K5JkDYgnQqA1pO5FyJnH_BTryFd4LVVUWdKv8_x538y9cy3hMqImygFTNcUxl1L99-jGmN2eE3Ls0yAYeMbBNtMxRW56Nmf8EmqhTls5PJwQeim3rpF7iNqjTURNkreM2gCVDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو منبع منطقه‌ای آگاه گزارش داده است که آمریکا می‌خواهد نخستین دور گفت‌وگوها با ایران با دعوت تهران از بازرسان سازمان ملل برای بازدید از تاسیسات هسته‌ای ایران پایان یابد.
به گفته این منابع، این تاسیسات پیش‌تر هدف حملات آمریکا و اسرائیل قرار گرفته‌اند و آخرین بازدید بازرسان از آنها پیش از جنگ قبلی، در ژوئن ۲۰۲۵، انجام شده بود.
اکسیوس می‌گوید: «آمریکا در مقابل آماده است به ایران اجازه دهد به بخشی از دارایی‌های مسدودشده خود دسترسی پیدا کند؛ از جمله حسابی به ارزش شش میلیارد دلار در قطر.»
بر اساس این گزارش، ایران می‌تواند از این پول برای خرید کالاهای بشردوستانه استفاده کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/76561" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIJbhN8DdfA3YbIeW9fcMWqMAFUIpcAslDWcqPuHIEzmCGP-FyyjBgq4MbASGErvm9JTa5LyQ5cPrYrdzM9xIdSvNktxUUypMOnZWL5FOzf10FXM1GUKnxm5D9wF5X81Dio_zTc1fVWq56hnC9ANpHfswPcVoZnMJkn8wuPqRO11GmsAMWfBY1ska1AxgS60zuH50HJJ9TE9IietDgXUSRQCFayGT1TUzGVUAR7FgrOjmH11JCReKbqsdaOudf1_DupkCEgJ-zzUuvJBU7qVnfkdec7uJPn2mKF-ZILo7rwuwRDo0NLIdBVQ3p6HmEsgH8o0pluG1_yEvicbKozwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های بهداشتی در غزه می‌گویند که دست‌کم ۱۰ فلسطینی در حملات هوایی و تیراندازی نیروهای اسرائیلی در چند حمله جداگانه کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76560" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4Uv24ps8bQJte_pWylLjpzSa_UPKgT9luK9mObnRgecN7OF6tbDqR-7iw3UPnWojjMwsxqvB9xYinvFO18WzHmCEppf5305TqZNnTFjzt8xvcXD1_Mzqc7mTZgH2YG7w1dc6-7iz_vpyrJa6brSRFREpE-sbJsCdbfGQCjhQ3KUIFEr8yno0t6Ke6WMrA40PU5KUxdEJNXmh85aTVlLGaIZYveQB3z88nN8hvErdb2U6RJqJJxzqfIQAVrMr9rkrjEhvhBmlkw8Vc-klfOkgA-WkBkBp19q-Kmqbvi-Dpcv4gu3CiaMv-aPvbUGeB02meeTqqEfUdNDThPMdNRcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از هزار دانشجو و فارغ‌التحصیل دانشگاه صنعتی شریف با امضای نامه‌ای سرگشاده خطاب به محمدرضا تجریشی، رییس این دانشگاه، نسبت به آنچه «تشدید فضای امنیتی» و گسترش برخوردهای انضباطی با دانشجویان خوانده‌اند اعتراض کردند و خواستار پاسخگویی مدیریت دانشگاه شدند.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف تاکید کرد که بیش از هزار نفر این نامه را امضا کرده‌اند. انتشار این نامه یک روز پس از رسانه‌ای شدن صدور احکام اخراج برای شماری از دانشجویان شریف صورت گرفت.
امضاکنندگان در این نامه نوشته‌اند که در ماه‌های اخیر دست‌کم ۳۰ پرونده در کمیته انضباطی دانشگاه تشکیل شده و ۱۳ دانشجو با احکام بدوی تعلیق یا اخراج مواجه شده‌اند. به گفته آنان، احکام سه دانشجو نیز در مرحله تجدیدنظر تایید شده است.
نویسندگان نامه تأکید کرده‌اند که آنچه در دانشگاه می‌گذرد، ادامه «روندی نگران‌کننده» است که به دلیل نبود واکنش مؤثر از سوی مدیریت دانشگاه، هر روز ابعاد گسترده‌تری پیدا می‌کند. آنها همچنین نسبت به افزایش سرخوردگی دانشجویان، گسترش بی‌اعتمادی در فضای دانشگاه و آسیب دیدن اعتبار علمی دانشگاه صنعتی شریف هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/76559" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxKI3_M5rtgnVHKB_y_Dd-a2CxRvcYHr9d_KyrJxeG8jkGoKVEw6wbkcdc_J2ESaaEoko2ONyfhQDH1zHmEMy43H3Nx-3HZsZanF1SlrhH_8QkJltqutY8U5cQcN1R813WuxWPYVskH9QkZJAiK_FOoSq2aPMMIobJ7OxFzk2kAjviB5Nww44YkrEpHk9tA6Bn2n0cYtNiUamSwPtF3hE0gkR03gATvb8JHQDQjB258hbes0iqsGQR7dB61kFypAaNNPTKhUJpU2fWYy-wKhOojAhBaO1PEWQgqvTvL8nvolWch2pDutjJVm6TyPTZFE_0dCDR-f-gc1fnethQz2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Okm4luYaosntYAYzzWFRY5SIwQ5YzdZYAsOQwuHK6bIRqbQYTo_8vp2jeJ0IM8BD5iy6qWE8mAsorVyfxNI3G7eJT2_MGhAxQLm6R3f2tcydNpvUPFDUpqYuT4vt3PXNQJW_k3E3WFpKhwoe3JNQ5ao74mhR4lw-Rp8WyZ0EHqwBjP6TrkQICJDAYHs4ItyljKRbblgqp-UGNV98Rp_wHAoDlkyYFxYjLdO283cNKRv1kFCIH13st8zA2UJBTGXm9pQn7pLtPVZ2kSDuiVtvbAIDB3SoYY1BXCTC0ArN5t8OhmmyARdlIfUQmyWxcfK2gotkxhedzDu3AqBBGbX8Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
جواد علیکردی، وکیل دادگستری زندانی، توسط شعبه اول دادگاه انقلاب مشهد به ۱۸ سال حبس، انفصال دائم از حرفه وکالت، دو سال تبعید به سراوان و دو سال منع خروج از کشور محکوم شد. جلسه رسیدگی به اتهامات او در ۲۰ خرداد ۱۴۰۵ برگزار شده بود.
🔸
به گزارش خبرگزاری هرانا، آقای علیکردی از بابت اتهام «اجتماع و تبانی برای اقدام علیه امنیت ملی» به پنج سال حبس و از بابت اتهام «فعالیت تبلیغی برخلاف امنیت ملی» به ۱۳ سال حبس محکوم شده است. پرونده او پیش‌تر در شعبه ۹۰۲ دادسرای مشهد مورد رسیدگی قرار گرفته و پس از صدور کیفرخواست به دادگاه انقلاب ارجاع شده بود.
🔸
جواد علیکردی در ۲۱ آذر ۱۴۰۴ توسط نیروهای امنیتی در مشهد بازداشت شد. او ابتدا به یکی از بازداشتگاه‌های امنیتی منتقل و سپس به زندان وکیل‌آباد مشهد انتقال یافت.
🔸
آقای علیکردی برادر خسرو علیکردی، وکیل دادگستری و مدافع حقوق بشر است که در آذر ۱۴۰۴ به شکل مشکوکی درگذشت. وی پیش‌تر نیز در پرونده‌ای جداگانه با اتهامات سیاسی و امنیتی محکوم شده بود که اجرای بخشی از احکام صادره
علیه او به حالت تعلیق درآمده بود.
@IranRights</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76556" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZevyUW5BlGWeR0a_qscTqFpcVNOxqlyWlusQnhFoE19ir3N2wWbJrOAzA7_bHpwYGTm5yYoFofOOggg-EAVU8hXhLlZ8503gR2QjO6q1j2KyiECq9sNb4mvzaBkoG35cyn6Fb49br6OgIS-cgnbs7yHiy4DAPWZF8W_iMbuj71KuegER-QevHt0naMYry7Td12WrYAm6oCURr0S0U-Des276dpms-AyUjcHLILmmo_OLhgobzp5kibOD3F9ONK6zW7K64RqtkcuzDHpmsRC5fqzE2zYq6PkLAbJ6yMnXLGBMM7qwDfdt9t_RuT00jXAdzw6sXVnHQFSsKVQj3J_p9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هیچ‌گونه عوارضی در تنگه هرمز وجود نخواهد داشت مگر به نفع آمریکا
ترجمه ماشین:
در دوره ۶۰ روزه آتش‌بس، در تنگه هرمز
هیچ عوارضی در کار نخواهد بود
،
و پس از پایان دوره ۶۰ روزه نیز
هیچ عوارضی پرداخت نخواهد شد
؛
مگر آن‌که، در صورت تکمیل نشدن توافق، این عوارض
از سوی ایالات متحده و به نفع آمریکا
وضع شود؛
آن هم بابت خدماتی که این کشور به عنوان «فرشته نگهبان» کشورهای خاورمیانه ارائه داده، برای جبران هزینه‌های گذشته، حال و آینده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76555" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=vCJj6rmSZyJv7Q-398vhW34J06dZVhcbWrEmU-T3M66Anl1V6KdowcmHE45em34X1vKrSIgR6SGv488TDfrVvIXn7rq_4EfDeOFoGMttnDIlFc18yE778CKXWBmbGClFc-U5_6We-tF3MkT1aHJWCP5yJuX1UTLewLmq_eYprbgvvr8YPLVudoU-jD-pzKTN-cajS57ovWzjiw84_K10T1zMeXl2lR5c4uSw-Xk1iWbABPFtJudSCLA6PhjXcmsOF_04_5a0ueeYQLzTrfMfe_f1FreAgjeqA_e2iFO7293-bJtwWZQqaJUYeJ1W6wPDAyoDuyGHiWiChs0SNAchFSNVjQBFbxgSE-WmH_ultLMUpLGTCbJyHFxzdQQqeH9G9IJQrU56vur1Q3t2IUB17fU1ddcyhNUMZl5D6VViJd1PgoVCUeUg2GvKs8kUPtFYeXPqkOxWKTlN6ifQyUy4pTQH34OuvrrSwWTu1yvLrK1fIKQ-q3yapBA21kWPCmjx4upuAvyjy59evOAcF0rO7DF6dvsmh1JkJAzbrtLbSihnASuLouDhmezMt9hkXBaZRj7x84NIY1Hac7gmRh9YW1ttJdgLuKYqU66m3RsXxPvSNkHdtxmk0DRA7Xe6rUleidMJR788Y-AbULcD7fX5v7nm9XoA8MOPJhO7I9UjniE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=vCJj6rmSZyJv7Q-398vhW34J06dZVhcbWrEmU-T3M66Anl1V6KdowcmHE45em34X1vKrSIgR6SGv488TDfrVvIXn7rq_4EfDeOFoGMttnDIlFc18yE778CKXWBmbGClFc-U5_6We-tF3MkT1aHJWCP5yJuX1UTLewLmq_eYprbgvvr8YPLVudoU-jD-pzKTN-cajS57ovWzjiw84_K10T1zMeXl2lR5c4uSw-Xk1iWbABPFtJudSCLA6PhjXcmsOF_04_5a0ueeYQLzTrfMfe_f1FreAgjeqA_e2iFO7293-bJtwWZQqaJUYeJ1W6wPDAyoDuyGHiWiChs0SNAchFSNVjQBFbxgSE-WmH_ultLMUpLGTCbJyHFxzdQQqeH9G9IJQrU56vur1Q3t2IUB17fU1ddcyhNUMZl5D6VViJd1PgoVCUeUg2GvKs8kUPtFYeXPqkOxWKTlN6ifQyUy4pTQH34OuvrrSwWTu1yvLrK1fIKQ-q3yapBA21kWPCmjx4upuAvyjy59evOAcF0rO7DF6dvsmh1JkJAzbrtLbSihnASuLouDhmezMt9hkXBaZRj7x84NIY1Hac7gmRh9YW1ttJdgLuKYqU66m3RsXxPvSNkHdtxmk0DRA7Xe6rUleidMJR788Y-AbULcD7fX5v7nm9XoA8MOPJhO7I9UjniE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبویان: مجتبی خامنه‌ای نامه داده بود که چرا شروط من رو در مذاکره رعایت نکردید؟
07:20
صدا و سیما: افشای مکاتبات مجتبی خامنه‌ای از سوی نبویان در شبکه خبر پیگرد قضایی دارد
صداوسیمای جمهوری اسلامی ایران اظهارات محمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس، در شبکه خبر پیرامون مذاکرات پیش رو بین ایران و آمریکا را «مصداق تخلف قانونی و مستوجب پیگرد قضایی» عنوان و اعلام کرد «مدیرکل مربوطهٔ این شبکه استعفا کرده است».
محمود نبویان، که به جناح تندرو موسوم به «پایداری» تعلق دارد، روز شنبه ۳۰ خرداد با خواندن بخش‌هایی از متن‌هایی که گفت مکاتبات مجتبی خامنه‌ای با هیئت مذاکره‌کننده است، مدعی شد رهبر جمهوری اسلامی در مراحل مختلف با روند مذاکرات و بندهای متن‌های گوناگون مرتبط با مذاکرات مخالف بوده است.
این گفت‌وگو پیش از آن‌که نبویان به متن نهایی تفاهم‌نامه برسد، قطع شد و موجی از واکنش‌ها را در میان دیگر چهره‌ها و فعالان رسانه‌ای جمهوری اسلامی در پی داشت.
صداوسیما در بیانیهٔ خود اعلام کرد نبویان در اظهاراتش «اشارهٔ ناقص و مخدوش به برخی اسناد دارای طبقه‌بندی» داشته و سعید آجورلو، عضو تیم رسانه‌ای هیئت مذاکره‌کننده و از چهره‌های نزدیک محمدباقر قالیباف، نیز او را به «تحریف عمدی متون» با هدف «فرار از پاسخگویی درباره ادعاهای نادرست قبلی» متهم کرد.
محمود نبویان، ۲۳ خرداد ماه، در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا، در یک برنامهٔ زنده در یک خبرگزاری نزدیک به سپاه، متنی را که مدعی بود تفاهم‌نامهٔ ایران و آمریکا است، روخوانی و از برخی بندهای آن به‌شدت انتقاد کرده بود.
نبویان یکی از اعضای گروهی بود که پس از اعلام آتش‌بس جنگ ۴۰ روزه، همراه هیئت مذاکره‌کنندهٔ با آمریکا به اسلام‌آباد رفته بود.
مجتبی خامنه‌ای، که پس از اعلام رهبری هنوز هیچ صدا و تصویری از او منتشر نشده، پس از امضای تفاهم‌نامه توسط رؤسای جمهور ایران و آمریکا در پیامی مکتوب اعلام کرد «نظر دیگری» داشته اما «با تعهدی» که پزشکیان به او داده، مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا گذاشته است.
@
VahidHeadline
حمید رسایی با انتشار ویدیوی بالا نوشت:
نبویان در آنتن زنده شبکه خبر، در حال تشریح جزئیات نامه‌های رد و بدل‌شده میان رهبر معظم انقلاب و شورای عالی امنیت ملی بود که پخش برنامه به بهانه میان‌برنامه به صورت کامل متوقف شد!
ما که از یادداشت‌های آن امام شهید در این باره اطلاع پیدا نکردیم ولی گوشه‌ای از یادداشت‌های امام حاضر توسط آقای نبویان در حال پخش از سیما بود مانع آن شدند!
صدا و سیما:
🔹
روابط عمومی معاونت سیاسی صداوسیما: به استحضار مخاطبان محترم شبکه خبر می‌رساند اظهارات یک نماینده مجلس دعوت‌شده به برنامه امروز زنده این شبکه و اشاره ناقص و مخدوش وی به برخی اسناد دارای طبقه‌بندی و مکاتبات مسئولان عالی کشور، مصداق تخلف قانونی و مستوجب پیگرد قضایی است و سازمان صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار می‌دهد.
🔹
شبکه خبر ضمن ابراز تاسف بابت بی‌توجهی مهمان مذکور به قواعد اخلاقی و الزامات آنتن زنده، به اطلاع می‌رساند مدیریت این شبکه ضمن پذیرش استعفای مدیرکل مربوطه، برخوردهای انضباطی لازم را به دلیل بی‌توجهی به الزامات برنامه‌های زنده و سهل‌انگاری در مدیریت حرفه‌ای به عمل خواهد آورد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76554" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kuezcdeMMRCS_uQPUxKyWAfGP5dCR00pXx8ENiHtbCGnHuqiE783KeyGtPtGtuwVJPC6HNND_m7CHQFr5D0GXsFCG6RjgMddmIPBc3vGbGe_CqXml764vITUshnU3gr7wRN2WBz0RGiyQ2e0U40bc5OnzMl_vN6_Cqwuao75s2bviJ2qioOe-KBTSdCfh3Qlay2_negTBSYMlk0YJxsrJL51C-gQHc1ZyLHOWC6vspyIrZKGqn24M9Zh38G6uYGmwt2OQDLjDrDZLfEVkbSL6SfhF0uCdcV1xv1IzFb2YSgChmgFnc5aW7r0DtUzKGBprSIC-XL9_f16o6dY0f1nYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sXu3ddm0WwbChS4bWuPbEzlC89euOQwAN2uaihkqbXsqKNgpsIpTRapsiFqfJN4D4Up1mXIJfWh4UGqwv27iFCGMmtyIzE-pjqqN-Z-Ow6TiUkuqdFvqiV-_JUgbZfIZ7ph4BRhTISU2Kn4hM3hk1cHj6LCkiUJsBbqrnl7I7jC7tc5vmnG2E6IPHL7apZQHH2ubX9ya3nGVAtd3wvsLuatFwW3FzNSW1C08lzs_U6Pl1tce451-cNIlu2_6FrDn5npU2mnV_3gwXfR_NbUjAwu8fL7bGU--WATdqJ1CMFRHi_14ANMQQBhaDvVC2Od8mrTUj_NZuQBPNIqNFzWwpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ در تروث سوشال نوشت: محبوبیت ملونی در ایتالیا به شدت کاهش یافته، شاید به این دلیل که او و ناتو در جریان ماموریت جلوگیری از دستیابی ایران به سلاح هسته‌ای، به ایالات متحده پشت کردند.
ایتالیا حتی اجازه استفاده از باندهای پروازی خود را به ما نداد که یک مانع لوجستیکی بزرگ بود؛ آن هم در حالی که آمریکا سالانه صدها میلیارد دلار برای محافظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند.
رئیس‌جمهوری آمریکا در پایان با لحنی تحقیرآمیز تاکید کرد: اکنون که ایالات متحده ایران را از نظر نظامی شکست داده، او می‌خواهد برای بالا بردن آمار محبوبیتش دوباره با ما رفیق شود؛ اما نه، ممنون!
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، با انتشار بیانیه‌ای تند در صفحه اینستاگرام خود، به هجمه‌های اخیر دونالد ترامپ پاسخ داد و حملات کلامی رئیس‌جمهوری آمریکا را «بی‌دلیل و بی‌معنی» خواند.
ملونی در این پیام خطاب به ترامپ نوشت: «محبوبیت من به هیچ‌وجه به رابطه با شما بستگی ندارد و دوستی با شما نیز کمکی به آن نکرده است. محبوبیت من حاصل توانایی‌ام در دفاع از منافع ملی ایتالیاست؛ یعنی همان کاری که همواره انجام داده‌ام.»
نخست‌وزیر ایتالیا همچنین با دفاع از تصمیم خود در جریان جنگ اخیر و عدم اجازه به آمریکا برای استفاده از پایگاه‌های نظامی این کشور، افزود: «نحوه استفاده از پایگاه‌های نظامی آمریکا در خاک ما، تابع توافق‌نامه‌های متقابلی است که ما همیشه به آن‌ها احترام گذاشته‌ایم. تا زمانی که من نخست‌وزیر هستم، این توافقات نباید نقض شوند؛ چرا که ایتالیا یک کشور مستقل و دارای حق حاکمیت باقی می‌ماند.»
ملونی در پایان نوشت: «در هر صورت، میزان محبوبیت من اصلا به شما مربوط نیست. پیشنهاد می‌کنم شما روی محبوبیت خودتان تمرکز کنید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76552" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gv8lUHkrA8sCsCqxbE80yCaT1V5HjS2E24-YZb_bDyUwJ-2VKvoieCg024-c1qAyITYtgfgfCR8c691ZOAgE5jP5OgnwvpMWMW2Ct_Ycxg7rQtrzaVoZy4g3oBPsTBKA_kvndCp5R4OE7ef3vn50aNXSrYA2TBPY8QLkgWDwGYw2UcFlSEaDl1ZwYzDEzIVA7EJ1VSpcB07pNZ-QV5E9x_2u9mt-MkEvBy-DREGcQim1pBrgi3EMBgx6zEaNcdB3ZOGzwcd2eL9mpcveq8VRBb_o9cYKXHTAXA_DSnnRGTgoUMgWHWBUSpTyjFrkaqSPf4MddHSzRJvZreHaz4wHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که هیات مذاکره‌کننده جمهوری اسلامی به ریاست محمدباقر قالیباف و با حضور عباس عراقچی، عازم سوئیس شده است.
بر اساس این گزارش، عبدالناصر همتی، رییس کل بانک مرکزی و علی باقری کنی، معاون بین‌الملل دبیرخانه شورای عالی امنیت ملی نیز در این سفر حضور خواهند داشت.
همچنین کاظم غریب‌آبادی، معاون و اسماعیل بقائی، سخنگوری وزارت خارجه و حمید بورد، معاون وزیر نفت نیز این افراد را همراهی می‌کنند.
پیش‌تر وزارت خارجه پاستان اعلام کرد که مذاکرات فنی میان جمهوری اسلامی و آمریکا، یکشنبه در سوئیس آغاز خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76551" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/leqt0CC-PApwQBtOBi4GhyvZV2Y7WMKB2iSZ0RO-3-h5M47CJjnhcNSy5BmXTtb5PgWym6Aq2ZZpO8RVWQpAPm2gzLBmv_iwbQTMTJ9A9H2A14DG5Bjx2uiUmfcB0NJHOLgECgFvw59fg1lffwxcqrT5m0BazkYwReZl2jFhsHwHK0-bFEILV39_tYiVC1gQAVLbiZBiIoaBkFQ1dP_IfbkxZw1zQd9mYh9f7KzQRHyEFUrMv_8U6hxONAkDqfc4p7c6zsfRmWArUBpVv75WNk5wXf2YqVpN2fNCfkwEcuiZHDT0NyT_JzYif5s1z1KrrcQ5C-_RiMac_2-GYhqo6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی مرکزی ایالات متحده،
ترجمه ماشین:
عبور کشتی‌های تجاری از تنگه باز هرمز
تامپا، فلوریدا — تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت؛ همزمان نیروهای آمریکایی به عملیات خود در منطقه کلی ادامه دادند تا از آزادی کشتیرانی حمایت کنند.
امروز عبور امن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری از آن عبور کردند؛ کشتی‌هایی که حجم زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل کردند.
مرکز مشترک اطلاعات دریایی این هفته اطلاعیه‌ای صادر کرد و در آن عبور امن همه کشتی‌ها را در یک مسیر تعیین‌شده تأیید کرد؛ مسیری که از ادعاهای خودسرانه درباره الزامات یا هرگونه مانع، آزاد است. جزئیات مربوط به عبور امن را می‌توان در اینجا دید:
ukmto.org
نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اجرا و به‌طور کامل برقرار و لازم‌الاجرا باقی می‌ماند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76550" target="_blank">📅 18:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=c03zZieQ6bzu__864nzgfB22yKlwyQN7OZhFTJNhkjlWEMfWa2_S8kWAhaECFKVFeD501jpCVmK-P8O6BYooh59fj8lrWbCHtj-DWALzTkTUUgFcivajRZQcECB69rR1xkY-vheK3k8am9C6PfAL9laY_Fts9p5STuSxmBwcDQMNc0rkxm2J3pPZ2NrDnLj8rzJCgw25q5bgcrtu2rF3FINDo11zIApXM_6iXEy7MbU-AtKXU4mDOriZKM5X5DoO0DJKtUf3-c0bvoUxpe3D-b8ef5v_17HPjkEJcAsqof0qJZlgcA8GyeSM_s0Nj0FUpz7QDEV1gSeX7CjyJuDWUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=c03zZieQ6bzu__864nzgfB22yKlwyQN7OZhFTJNhkjlWEMfWa2_S8kWAhaECFKVFeD501jpCVmK-P8O6BYooh59fj8lrWbCHtj-DWALzTkTUUgFcivajRZQcECB69rR1xkY-vheK3k8am9C6PfAL9laY_Fts9p5STuSxmBwcDQMNc0rkxm2J3pPZ2NrDnLj8rzJCgw25q5bgcrtu2rF3FINDo11zIApXM_6iXEy7MbU-AtKXU4mDOriZKM5X5DoO0DJKtUf3-c0bvoUxpe3D-b8ef5v_17HPjkEJcAsqof0qJZlgcA8GyeSM_s0Nj0FUpz7QDEV1gSeX7CjyJuDWUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی پربازدید شده که مادر مانی صفرپور، جوان کشته‌شده در اعتراضات دی‌ماه، را در حال سوگواری برای فرزندش در کنار یک دستۀ عزاداری نشان می‌دهد.
عکس پسرش را بالای دست گرفته و می‌گوید «پسرم، پسرم».
مانی صفر‌پور، جوان ۱۸ سالۀ لاهیجانی، ۱۸ دی‌ماه ۱۴۰۴ با شلیک نیروهای حکومتی در محلۀ سلسبیل تهران کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76548" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76547">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAlyN0u_LaqT0srPodMKeUNbTChslBfgOHQWPQjd-lHuQHz8eFOufBcoGnB3a-gNX3WjMbLTbX0rGw7kNbfyf5LprMkqLy3f54SGnxfb1gwtgPA1D_JIvgAPKJVGwbPNi5V0cRFbI_1IhjkdvAN8zhexp84TvJjhvmjCDsjyz3IL9r1lGsH1NgMaQQZjqT6Xxc5EK2cNAHJRQuivRiNqrWhheDYvO5jUKcKWttVd0nRZxw70D3l2d3P7SOpI-hd7JWg_IBHzcTItOvNBNQJbyzZSOYWYfPrEeh8awvmDa6ivfiNKTHx8TamZDuQw3mFUblYOXfZad6JqQuvCb9nUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد تنگه هرمز در واکنش به «نقض تعهدات امریکا در اجرای آتش‌بس» و «حملات اسرائیل در لبنان»، به روی همه شناورها بسته شد.
نیروی دریایی سپاه همچنین از شناورها خواست به تنگه هرمز نزدیک نشوند و هشدار داد در غیر این صورت، امنیت آن‌ها به خطر خواهد افتاد.
قرارگاه مرکزی خاتم‌الانبیا، واحدی از سپاه پاسداران هم اعلام کرد تنگه هرمز به‌دلیل «بدعهدی و پیمان‌شکنی» امریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه، به روی تردد کشتی‌ها بسته شده است.
قرارگاه مرکزی خاتم‌الانبیا روز شنبه اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.
خبرگزاری فارس، وابسته به سپاه پاسداران به نقل از یک منبع نظامی در نیروی دریایی سپاه، عصر شنبه اعلام کرد که تنگه هرمز از دقایقی پیش به‌طور کامل بسته شده است.
حملات اسرائیل به جنوب لبنان در روز شنبه دست‌کم ۱۰ کشته بر جا گذاشته است. اسرائیل اعلام کرد این حملات در واکنش به پرتاب گلوله‌هایی از سوی حزب‌الله، گروه مورد حمایت جمهوری اسلامی، انجام شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76547" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IWLyIHckIHNl67Ny0MmZAke3mxpmKuma0kmc89_x4SElWjp6DQZrZkQyUrbckxx0jI4EFGNhesCZJotHBAWR8iYS5iXO67ZKjzVsf8kcIrxM6-00t_ZuGP3mVrvVZCMCPJkbKauJVdZ5OXvP_0NnK5cGiugom2w7yMq6fZpVEf7Eo3IpK5a4ga6q4FIm1HBybEsx_jxhafM8-NsXJ6kiWvLTyHrN7t7jCDEzzQ3_7jaZsbB85taPaxUUYR5098N8xu56doHv7nJzsQBTi_pQRfN1xhjL3XpMed60H_YTZwCxXoWOq1t-z6msO6e1dXRmyDcCSvgnCc4OIDKvXQGnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، روز شنبه ۳۰ خرداد در گفتگو با فاکس‌نیوز اعلام کرد که استیو ویتکاف، فرستاده ویژه ترامپ و جرد کوشنر، داماد او، «چند ساعتی است» که در سوئیس حضور دارند و مشغول بررسی «برخی از ابعاد فنی این مذاکرات» با ایران هستند. به گفته ونس، کوشنر و ویتکاف در گزارش‌های خود تاکید کرده‌اند که «امور به خوبی پیش می‌رود.»
ونس همچنین از احتمال ورود میانجی‌های قطری و پاکستانی به سوئیس برای پیوستن به این گفتگوها خبر داد و افزود: «قطری‌ها و پاکستانی‌ها می‌خواهند مطمئن شوند که ما این کار را به شیوه درست انجام می‌دهیم، بنابراین من تلاش می‌کنم به این روند احترام بگذارم.»
معاون ترامپ که سفر خود به سوئیس را در اواخر پنج‌شنبه شب به تعویق انداخته بود، بار دیگر تاکید کرد که انتظار دارد طی دو روز آینده عازم این کشور شود. او با این حال خاطرنشان کرد که هماهنگی‌های این سفر «همواره یک رقص هماهنگی ظریف دیپلماتیک است.» این مذاکرات که پیش‌تر قرار بود روز جمعه برگزار شود، پس از وقفه‌ای کوتاه دوباره در آستانه ازسرگیری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76546" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/samAV6o5kX-l1cCq8ldZNxwQwfjVtPpG9U7ZUXcLL7VjTHnK1SHjvWGGuVjRj7tiR0UGQjTSAgyjHsoecbmEHUHu4MpGHKBtUrZZyS3IreTwpH4AgQG2rUCnfZyrg1ix30Dx_Avw4xTE9X6TWi55MoCn-Izad-6gcG-SYsGzXClps9Wx-kxJ7VGljx2-jkhdb5dc_pGOuLBFSd6_RmlAU0nhAxYSwHJcwiNur4o7_rt923p4uR0maUppd6DY_cVMt8UIDc3gyH8BQ9vnH6vF7l8YZ0lmSeJKoHd6q_aoj1DGrb7OSmN-RsWA9rKquxqh2Hj5P3Bhqkuoo1iBtmfWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«طاها نظری» معترض ۱۸ساله که پیشتر به‌دلیل حضور در اعتراضات ۱۸ و ۱۹دی۱۴۰۴ بازداشت شده بود، پس از  تشکیل جلسه رسیدگی به پرونده، به ۵سال حبس تعزیری محکوم شده است.
ماموران اطلاعات شاهرود، در فروردین ۱۴۰۵، طاها نظری را شناسایی و به صورت تلفنی احضار کردند. بعد از مراجعه به محل، این جوان ۱۸ساله به‌صورت موقت بازداشت و تحت فشار برای پذیرش اتهاماتی نظیر «ارتباط با تلویزیون‌های فارسی‌زبان و فیلم‌برداری از اعتراضات» به او نسبت داده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76545" target="_blank">📅 17:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v12BqPu6Clu6htTqUvXkCwz4IRspz4LPaulrf1bvnQZ0IJ8FvzkpFQd24NCOUjGvx_VBcl9iQ8tNPJzQvpF_x3wug-an5y_EmeTgxO5a4klmOT4TfC7DfhjAzvMmvFvBweyLmKI7u5vOjFp-rMyc3qmClqmRwui8kRKi_WX4tNFf9ptJl82FhBnUSW3mz864OiMCtYu8PUsQa05yxtb8H1GW_UJqt3r-oHikxtakqSORo0l7Q2Got_Ioon7Y_B7O04X6b4gfFKP9xYXoSSrM1y4gEmE5PT18fKtivbExCAwCDi9d4H5-dCJshNA3rVxUm9HQJvOw_PCKvDsfdFADLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KZgGI7982CznLnlt2YXOQ8nrvro_ZsXfPPRW2pHNgx79tVRZz706MJu3Vb2tPh0jqFuKjhhg-haiSTXDhHtUdg1vSj_OuGSvls95mILjQI36nU_cWZFYfMroPer0VOgGGRvERajDaifEZDWPAJBq7w3KzpQr4DQGkNRYNQjKu-7tJnJBxFhdgX25MwUlH3TwBJljOkdaQkOibGbk5tofwYg2xv8-qrUm0RW3zg9Eb4qHc8OD3GfC4ZIgmM_GQx0JfPMjF6oi4tEq-thnqqPmXUBNz0uNOxcw1MCIhqfkLXkyZJp0YenBxqdMbb8fPCs468V-lBZ0iWNSFrgo18Ywaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت دلار و دیگر ارزهای خارجی که در پی نتیجه موقت مذاکرات ایران و آمریکا کاهش یافته بود بار دیگر افزایشی شد.
روز شنبه، ۳۰ خردادماه، قیمت دلار آمریکا در بازار به ۱۶۲ هزار و ۵۰۰ تومان رسید. قیمت یک یوروی اروپا نیز در این روز به ۱۸۶ هزار و ۴۰۰ تومان رسید.
این در حالی است که در طی روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسیده و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شده بود.
روزنامه هم‌میهن روز شنبه قیمت سکه امامی را در بازار طلای ایران ۱۶۹ میلیون تومان گزارش کرد.
از زمان اعلام تفاهم‌نامه ایران و آمریکا در تلاش برای پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران شاهد کاهش قابل توجهی بود.
@
VahidHeadline
حسین صمصامی، عضو کمیسیون اقتصادی مجلس شورای اسلامی، در گفت‌وگو با سایت خبری تابناک افشا کرد که در هفت سال گذشته بیش از ۱۳۰ میلیارد دلار ارز حاصل از صادرات به کشور بازنگشته است.
این در حالی است که حکومت برای بازگرداندن ۲۴ میلیارد دلار دارایی مسدودشده کشور وارد چانه‌زنی فراوان با دولت ایالات متحده شده است، امری که نشان می‌دهد تا چه حد به این پول نیاز دارد.
در این میان بیشترین میزان عدم بازگشت ارز صادرات مربوط به سال ۱۴۰۴ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76543" target="_blank">📅 17:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76541">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QK6sF_goGb-fzDhQc9vVHiXiC3il966Av_iR6xT63sPAiSJo7FHE10Kz_iMiNdUg2F8LAhist448tZzbu6urEL-HDRFlkRmb0qqR8BCIT3e8mUTq86H0IvI-h8vomCpl4ffU-R4lE4ab5rlGw11PBvqYE3jqCTAYqkKHfkb8oTXVl4RSs4r76wDlVslF1nMz1ijdc-kk4JIoP3Xb2XZnNrK2LV79_KfYBnotCYD2iKgkGToAJ9XuZ_-MhisjHO1XFXFJFgoFe3ckWUgT2usPjq41FkdlFTCLAFAOCtD5RCBgx2LkddBVYW5_v4w_NFg6vE4aJTWBnNQkECAw_HSRCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=Wp2mVZYM-W5otJJ6-E9Jw_-LTyHAiWTqlAMgf1NV1Nti8qVbJ9fOrzdQ472AnhLBIAqZm0HJ0sIWJo98PkG96ot3bebB9NqOKsNvHJWKqt5r20cCHj8JzHUy8NNEyOBQkxzcEPerf9AHN7U0Z0Tfigeyr241Xfk3E2-uNv8diyDyuwbelYvud3b9tFxxdIffJ6yQUMtPVvxN4zY0fQMq5H1GFoHBH7YBInN3RTJ8sp6O7y4o1Rq8OM6XnrP6qj42hxd0yggIeXVx866AF-gdfPK_OVuz4DIuwX0bOFgFXFUtELhfBEAIfb36s7w8jmihc9whnh25fD8P1dGiJlIdmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=Wp2mVZYM-W5otJJ6-E9Jw_-LTyHAiWTqlAMgf1NV1Nti8qVbJ9fOrzdQ472AnhLBIAqZm0HJ0sIWJo98PkG96ot3bebB9NqOKsNvHJWKqt5r20cCHj8JzHUy8NNEyOBQkxzcEPerf9AHN7U0Z0Tfigeyr241Xfk3E2-uNv8diyDyuwbelYvud3b9tFxxdIffJ6yQUMtPVvxN4zY0fQMq5H1GFoHBH7YBInN3RTJ8sp6O7y4o1Rq8OM6XnrP6qj42hxd0yggIeXVx866AF-gdfPK_OVuz4DIuwX0bOFgFXFUtELhfBEAIfb36s7w8jmihc9whnh25fD8P1dGiJlIdmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که هاجر نادری، مادر متین پرویزی، در صفحۀ شخصی خود منتشر کرده است او را در کنار آرامگاه پسرش نشان می‌دهد که می‌گوید «من به پسرم فقط یاحسین و تشنگی را یاد ندادم، به او یاد دادم که جلوی حرف زور بایستد»
خانم نادری در ادامه با شرح کشته شدن فرزندش در اعتراضات ۱۸ دی‌ماه می‌گوید امسال محرم برای فرزندان میهن که «ناجوانمردانه کشته شدند» عزاداری خواهد کرد و ادامه می‌دهد که «می‌دانم امام حسین هم برای این جوانان عزاداری خواهد کرد»
متین پرویزی ۱۸ دی‌ماه سال گذشته در سبزه‌میدان زنجان با شلیک گلوله جنگی نیروهای حکومتی به سرش کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/76541" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqbtTnt7F2peC2T1cFDQyMBtD3b4pmA1MaxILnbKvoB5EsS1p9nc_il6u0_hIXnOSS6FAzSTeETIgpvpJS-wU0JCTHv3pD6-3ZrCmVXo76jWd5kQxnBIhwO0WW4aO6xB5vDZfPSvTEKQHTpqRFuDWF4yx4I4nnY3qcNthL1_Ud1iRAUCTEbsYbLZAWeF96Xc_iqjvaFca2Hrzxoy2pkzwxOv6c1nzD9Sdtvu6r7LSZ_lFakuvAG8dv7co5Aym_TTUup3bbhv1kctmA6SvMf8yqDRq_LGctOTybgxRKSDe9g5u4cKpFM4PbTOODv2R9hV42HamXJx5fyWGUcHhF5HRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، صبح امروز وارد مشهد شد.
ایرنا به نقل از منابع خبری در استانداری خراسان رضوی گفته است که او سپس برای گفتگو با مقامات عازم تهران خواهد شد.
بر اساس گزارش‌ها وزیر کشور پاکستان قرار است در این سفر در مورد از سرگیری مذاکرات مستقیم بین آمریکا و ایران در سوئیس، با مقامات ایران گفتگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76540" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76539">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhR6aggYHMjMbFNYvJD1fnpOzDojZd-oAHtbmBL8evQ5jVh31iTBWzz3iBk5GnTNaRtgZtJtn3xmgvTLejhsfWtGi3YBh2U-UPKu6Gfn_C96XeVShT78Zvt80mh4BJKM3JxJ--dtE9Wj1sswYVv52yLxUcJHT8ObkQJlFASu1xeqHRsZwxa5Sbei5rzIE-iKfsxQMWH4qskwZPZnfgjB1OYqAt1AhPXrwolWWkHfsKJqkWLtWOHbIYeB9LEf6aRfShV3aEXha4y_0XQHSU2VmUrhjySWIQDCpuTPjKRK9BSnlMKpZi5ndyOWSPnJlQDg7xPhzyFTLuJGVzXFEN4C3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز اطلاع‌رسانی پلیس استان لرستان از پلمب یک واحد صنفی و معرفی فرد متخلف به مرجع قضایی خبر داده و اعلام کرده است این اقدام پس از آن صورت گرفته که به گفته این نهاد، واحد مذکور «ضمن عدم رعایت قوانین و مقررات، اقدام به هنجارشکنی» کرده بود.
این در حالی است که تنها سه روز پیش نیز مرکز اطلاع‌رسانی پلیس لرستان از پلمپ پنج کافه‌رستوران و سفره‌خانه سنتی در سطح استان خبر داده بود. در آن گزارش، دلیل برخورد با این اماکن، اجرای طرح موسوم به «ارتقای امنیت اخلاقی و اجتماعی» و آنچه «هنجارشکنی» عنوان شده، اعلام شده بود.
در هفته‌های اخیر و هم‌زمان با فروکش کردن فضای امنیتی ناشی از تنش‌های بیرونی، گزارش‌هایی از افزایش تمرکز نهادهای انتظامی و قضایی بر حوزه‌های مرتبط با سبک زندگی شهروندان منتشر شده است؛ روندی که به نظر می‌رسد بار دیگر کسب‌وکارهایی مانند کافه‌ها، رستوران‌ها، فضاهای موسیقی، پوشش و نوع تعاملات اجتماعی را هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76539" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=D5wC-kY7PdVZa43rhKmWjoEEla7kx9SQUrWBxJk_EDD0V3lyFd6W3lkr5fFs5mOS95C5b8FqraREUW5J0EVPh3tU-9BdaAVc4fyRFKq1m9ycyP3EpxGhKdZ0FKa3eLDiaHP9YcZzOINaAN9T4IoJELhFOynLf7rnCdyuuCClK55ZHhb2P-ke4ngGpJA8XMW1utgl7sCUvwpM3KS2XhIosHveehJ8yMNGsjACTCFHVvtTfGikHi6BKtvo0ZhGavkrHOH0MfZofHp5npMiozdeXx8UC3_aLS798viVDGslJgAPCkWqnyMmBwAzuC2Bj8EqIELzYQFY9GYYYfaJQTnn7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=D5wC-kY7PdVZa43rhKmWjoEEla7kx9SQUrWBxJk_EDD0V3lyFd6W3lkr5fFs5mOS95C5b8FqraREUW5J0EVPh3tU-9BdaAVc4fyRFKq1m9ycyP3EpxGhKdZ0FKa3eLDiaHP9YcZzOINaAN9T4IoJELhFOynLf7rnCdyuuCClK55ZHhb2P-ke4ngGpJA8XMW1utgl7sCUvwpM3KS2XhIosHveehJ8yMNGsjACTCFHVvtTfGikHi6BKtvo0ZhGavkrHOH0MfZofHp5npMiozdeXx8UC3_aLS798viVDGslJgAPCkWqnyMmBwAzuC2Bj8EqIELzYQFY9GYYYfaJQTnn7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع‌های اعتراضی زنان به فعالیت‌های معدنی حوالی دو روستا در استان‌های کرمان و سیستان‌وبلوچستان با حضور نیروی انتظامی به خشونت کشیده شد.
بر اساس گزارش‌ها زنان روستای پشموکی از توابع فاریاب استان کرمان روز ۲۷ خرداد در ادامه اعتراضات مردمی نسبت به نحوه واگذاری و بهره‌برداری از معدن کرومیت پشموکی تجمع کرده بودند.
گفته شده که نیروی انتظامی علاوه بر ضرب‌وشتم معترضان، شماری از آن‌ها را بازداشت کرد.
هم‌چنین منابع بلوچ گزارش داده‌اند که زنان روستای سرسیاه از توابع تفتان استان سیستان‌وبلوچستان هم روز ۲۶ خرداد در اعتراض به گسترش فعالیت‌های معدن طلای تفتان و پیامدهای آن بر زندگی مردم منطقه تجمع کرده بودند.
در ویدئویی که منتشر شده شنیده می‌شود که مأموران نیروی انتظامی با خشونت، تهدید، توهین و واژه‌های تحقیرآمیز با این زنان برخورد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76537" target="_blank">📅 17:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b5NlVm6Z0X9MmwMGZmtgrILC_yXBh_4Th2JHv1rVQNnzlYvNQyzlqQIeeZWctRc36Y9thvqYYHPHMLThcdnM471MqpiHzkodQQZsLrqg2JjaB7JqbeA-8OU3XFzWfg-lAHkzsLcNHz9_PFep4Wdfaw3ycNlB4AHoAX9vFeIAksiTRdyAKD_WS84KyHlYEq7NSxDDYSbOb-OzBf5FVDxdnbC0tiBe0PssA6gt0DwefVlMJ7Z8hGPFiEknfzSzmCHFkRnN8MwJWxsjLX-N9tS33i1nnnY8d92WB29MoEvuQJDfeXt2szWFvmEvTKTRX0i3KmNUsn9dGkMTIUxvO-VCAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LtYRyjPqs3e7BhxadqQ7y-O7EEuJj4k-LaxQEyGeQfw3FhhsmJZfUF7MTcHl_GQn1aWMlsqRT3_PpeIKd5hYwBFI_TLqFMcsf3w66Ny_qnBuKkuXdAODxIGZISumwqFgmo-LSgPOZfFdSjao6VgGKhjULsLZEq3AL4KVTz7tZ8-cHE-Ikh4Lp8KK6Y2HRnGFiWDhJBzXAHG46tH36c0elpt62ODMzdgigAlYuweye6mjr8y5WFucnCwP1pajnJXGhuu-6XFlffUShuihPIxT1X8ks6ki10GK_wvR8s-XynD9u5GTfipPop7EweLxgN67EmN4lWkWGFkz0hBV8GASlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: استیو ویتکاف، فرستاده کاخ سفید، در حال سفر به سوئیس است، جایی که انتظار می‌رود دور اول مذاکرات با ایران در مورد توافق هسته‌ای احتمالی برگزار شود.
به نوشته اکسیوس، قرار بود مذاکرات جمعه ۲۹ خرداد آغاز شود، اما به دلیل درگیری بین اسرائیل و حزب‌الله در لبنان به تعویق افتاد.
@
VahidOOnLine
خبرنگار اکسیوس به نقل از یک منبع آگاه، روز شنبه اعلام کرد: «عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، در حال برنامه‌ریزی برای سفر به سوئیس در روز شنبه است.هرچند این برنامه همچون گذشته ممکن است تغییر کند.»
این خبرنگار به نقل از منبعی در یکی از کشورهای میانجی فاش کرد که عراقچی روز جمعه به چند تن از همتایان خود گفته است: «موضوع آتش‌بس در لبنان برای ایران یک مسئله حیاتی است و حکم برد یا باخت (تعیین‌کننده سرنوشت) را برای مذاکرات ایران و آمریکا دارد.»
خبرنگار اکسیوس همچنین به نقل از یک منبع دوم از میان کشورهای واسط افزود: «ایرانی‌ها صراحتا تأکید کرده‌اند که می‌خواهند پیش از سفر به سوئیس، شاهد برقراری و تثبیت کامل آتش‌بس باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76535" target="_blank">📅 04:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=EKMuvTbitclgYGMzOxZEG1YzX5NLp5qCM6E65zFJkqh2BQJahln3X3EjcQJJYBTxSKg4gm8oQJG4yrX7jGK-ecNvdan2cY8e-hVKuX7BxT56G9KSn_7KRdV0cmHx4UqzXi6MO43zjqUFyiYSJ45yV26Iv5QkCXHem96a3MS6w4jM4l8PjIEoLryyiBdUTab5K9wb48qtDjtBHlG4rQUK6JkUogfROeKpW9ODp0wLsl4d7z73Re1gxlOnqgia5wHkcFpa8CvjUAXmR7KZpoiAn0tcNl_ra5HbfNRRBnDPHuw-IXIGCbI_sPz17Rv1NmZD8_B4eZAisHz13_3M171DYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=EKMuvTbitclgYGMzOxZEG1YzX5NLp5qCM6E65zFJkqh2BQJahln3X3EjcQJJYBTxSKg4gm8oQJG4yrX7jGK-ecNvdan2cY8e-hVKuX7BxT56G9KSn_7KRdV0cmHx4UqzXi6MO43zjqUFyiYSJ45yV26Iv5QkCXHem96a3MS6w4jM4l8PjIEoLryyiBdUTab5K9wb48qtDjtBHlG4rQUK6JkUogfROeKpW9ODp0wLsl4d7z73Re1gxlOnqgia5wHkcFpa8CvjUAXmR7KZpoiAn0tcNl_ra5HbfNRRBnDPHuw-IXIGCbI_sPz17Rv1NmZD8_B4eZAisHz13_3M171DYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بخش مربوط به ایران از مصاحبه امروز ترامپ
متن کامل این بخش‌ها:
https://telegra.ph/trump-06-19
بعضی از جملات همان متن:
ترامپ: و من آیت‌الله را کشتم. یک مقام سپاه هم بود. و متأسفانه به آیت‌الله دیگر هم آسیب جدی زدم. به شما بگویم، من او را ملاقات نکردم، با او صحبت نکردم، اما دیگران درباره‌اش حرف می‌زدند. او شجاعت خاصی دارد، چون به‌شدت آسیب دیده است.
با وجود همه این‌ها، نمی‌توانید بگویید بی‌خیال. من ارتششان را نابود کردم. نمی‌خواهم این را نادیده بگیرند.
برای کسانی که می‌گویند شاید من به‌اندازه کافی سخت نگرفتم، باید بگویم من ارتششان را نابود کردم. بزرگ‌ترین پلشان را زدم، چون دیر در جلسه حاضر شدند. گفتند این کار خیلی قشنگی نبود. من گفتم پل جورج واشنگتن؟ سه دقیقه‌ای نابودش کردم. خارک را زدم، همه چیز را، جز یک چیز. گفتم به لوله‌ها دست نزنید، چون نمی‌خواهم به اقتصاد جهان آسیب بزنم.
بنابراین فکر می‌کنم خیلی سخت گرفتیم. به کسانی گوش ندهید که می‌گویند می‌توانست سخت‌تر باشد. کل ارتششان از بین رفته است.
پرسشگر: چطور تغییر رژیم است وقتی هنوز خامنه‌ای جوان‌تر و خیلی از مقام‌های سپاه آنجا هستند؟
چون افراد متفاوتی هستند. خامنه‌ای جوان‌تر با پدرش فرق دارد. افرادی هستند که بسیار کمتر از دو گروه قبلی رادیکال‌اند؛ و من هر دو گروه قبلی را می‌شناختم.
اما به این فکر کنید: همه آن‌ها رفته‌اند. بعد می‌گویند چرا سخت‌تر نگرفتی؟ تنها راهی که می‌توانم سخت‌تر بگیرم این است که دو یا سه هفته دیگر وارد شوم و آن‌ها را شدیداً بمباران کنم. اما این چه چیزی برای ما به دست می‌آورد؟ تنگه هرمز باز نخواهد ماند. فرض کنید این کار را می‌کردم. فرض کنید تصمیم می‌گرفتم این کار را بکنم. الآن بازار سهام ما فوق‌العاده بالاست. قیمت نفت در حال سقوط است. قیمت نفت تقریباً همان جایی است که قبل از شروع کار من بود. تفاوت بزرگ این است که ایران هرگز سلاح هسته‌ای نخواهد داشت. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت، روشن است؟ خیلی واضح و ساده است.
آیا می‌دانید در دو ماه گذشته، من کشتی‌های زیادی را از آنجا خارج می‌کردم و کسی خبر نداشت؟ می‌دانید چرا خبر نداشتند؟ چون ما رادارشان را از کار انداختیم. همه تجهیزات دفاعی‌شان را زدیم. آن‌ها قادر به دیدن نبودند. هفته گذشته، یک شب ۲۵ کشتی داشتیم، یک شب ۲۲ کشتی، یک شب ۱۹ کشتی، یک شب ۲۱ کشتی. هر شب، همه این کشتی‌ها بیرون می‌رفتند.
ایرانی‌ها مردم بسیار باهوشی‌اند. نوعی نبوغ ابتدایی دارند، اما باهوش‌اند. منظورم این است که باید جلوی آن‌ها را می‌گرفتم، چون اگر سلاح هسته‌ای داشتند، از آن استفاده می‌کردند. می‌خواستید ببینید؟ بگذارید چند شهر را در جایی منفجر کنند؟ مثلاً اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت. چون من توافق باراک حسین اوباما، یعنی برجام را لغو کردم؛ توافقی که مسیری به سوی سلاح هسته‌ای بود. آن‌ها پنج سال پیش به آن رسیده بودند. به نظر من، در همان هفته اول از آن استفاده می‌کردند. اسرائیل دیگر با ما نبود. اگر من آن کار را نکرده بودم، اسرائیل سال‌ها پیش از بین رفته بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76534" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2VPRlaM8iIQ6_LrQtUodZlbSUH4GI4imGTV_6iX0juzHtAqVoE1xC7fnj1IGyHrsBJV5j9rJi1i3Yu5flRm1dvYJyPG0_2HbeH9LKa8dz5ripTxqmNx0ZEDM5AdOn-5naISdF_sAEosvV3jfJTV-QbZKdFaIIfUsk5lWwoq9N_MrzkJ_IDbFYY63GhrVLgl6L236nMra1hY26UWMzUex3Tju8yjzzIA-oMD_hALgrAL5Mwj97cT3Kwk4-tqHBpi9joA8_Sl5u-DmeVU5r8Xzsh2mfRmdxIWhgP-fDtK3EncT_BQLMkG7ryIC9Ja_JeMjL4Ld9E5axJTgiGFtQX8bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا، در مصاحبه‌ای با برنامه «آکسیوس شو» با دفاع از تصمیم خود برای شروع عملیات نظامی در ایران، مقام‌های جمهوری اسلامی را «بسیار باهوش» و «نابغه‌های بدوی» توصیف کرد و هشدار داد که آن‌ها در عین حال بسیار غیرقابل‌پیش‌بینی هستند.
ترامپ با اشاره به مداخله نظامی اخیر ایالات متحده گفت: «من مجبور به اقدام شدم تا جلوی آن‌ها را بگیرم؛ چون اگر سلاح هسته‌ای داشتند، حتما از آن استفاده می‌کردند و با منفجر کردن چند شهر، از جمله در اسرائیل، هرج‌ومرجی واقعی به راه می‌انداختند.»
او با تاکید بر اینکه اگر اقدام او در لغو برجام نبود، اسرائیل سال‌ها پیش نابود شده بود، توافق دوران اوباما را مسیری هموار برای دستیابی جمهوری اسلامی ایران به بمب اتم دانست. ترامپ همچنین با ابراز شگفتی از زمان‌بندی تقابل با ایران افزود: «چیزی که مرا غافلگیر کرد این بود که آن‌ها این‌قدر منتظر ماندند. آن‌ها صبر کردند تا من به قدرت بازگردم؛ البته این کارشان عمدی نبود. هیچ‌کس، حتی با وجود سلاح‌سازی ساختار حکومتی علیه من، فکر نمی‌کرد بازگردم، اما من با خروشی بزرگ‌تر از قبل بازگشتم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76533" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
