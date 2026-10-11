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
<img src="https://cdn1.telesco.pe/file/LfYi-_W_64RayK-cSVATznE_3Jq-NhSbEfZslteSNB1j76NaI2g6b45niWy0PBxPs1r-L_1HpQLl-DmhwAQjCwL7DAwmEw_Y5OLahpJYBioGrjkk-ZvwQG5Gxxaap0700ydFb-ec15jTe3T6xMy8Djq8ja2aDLZqmKos2ycJ5HWvz4G7KbP7ki-lA6rFTXEZYIrkqgBDZYYn-nbpy22Dp0hnzF4cvHaFJ5jPh3DJZCY3_WBAAsjX9bs01vzLHX07v8FlQg2Q1Q0QsqeJE8UyY-tAnPHtCR0fY-p1k0m9WuArhDmXuCH1D4lu_YdzjfEq0N5WUhlJ3cVKS89e365g8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.39M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی می‌گن. اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جوری که می‌خواستم به خودم نشون داده بشن می‌گذارم.ممنون از حمایت‌های ماهانهvhdo.nl/patreonیا گاهانهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 01:40:53</div>
<hr>

<div class="tg-post" id="msg-78695">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hyoeRzw4kT78hg_txm6y1ys4P-ael4i-u7cSbmNLRZ0WkqgHWf39LLD-rNLUM783mToWeSDDH81exUmejkD8a7hPfYkksANUFlejf7reJrWwSHunrT62zM80M9sxEkySGQlDYhV4UNQjhNs25LKyi6KszeRec-tdHvtLVKRw9YPYh_OcHKYNmthHS_W5y5M2Daafn7SN_opMjCoablfjqLc5x6QESKSXnXxrhl1mLI8hG-JpcyyPbxo1JmF4atioMlyUEOgMKP2s6WmqTElxchg08r8JFxfUSGam2IOLOsYeJ-bCOEiyACr5ZCv8gBU9LYUrQgcea67yyutwbceQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1281277307.mp4?token=f9j3xfZbQntodULIeomPkLN7HhZzdJbPT8oVl2RqlddXQTYadsiOkDk-95f4JEUvvamyVsIaySHSuzOTZzqAMiWV4zNh5U96SDhxuYIYb773f19fbdxd6xGvgV6FDN-imzyIJz_QtJ52v0cZikAiyOfN4qW4tcTYnRBmmMaX0iSixUyvzJNb0PLqEEIX-umD_ZOHppBel0XbZPZ80qBts8q0YltnqxMYnfmUfUbkRg1IhfRMbR2fhH4Rcs5tRcIV2tGjXA2HuqFfsvXXnbDj9tIqR_p8BiQHIrJsUWxxNsh2vPMSOGU6IewNeckPlFi3cA4mLTRzHaoaUymUvXFqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1281277307.mp4?token=f9j3xfZbQntodULIeomPkLN7HhZzdJbPT8oVl2RqlddXQTYadsiOkDk-95f4JEUvvamyVsIaySHSuzOTZzqAMiWV4zNh5U96SDhxuYIYb773f19fbdxd6xGvgV6FDN-imzyIJz_QtJ52v0cZikAiyOfN4qW4tcTYnRBmmMaX0iSixUyvzJNb0PLqEEIX-umD_ZOHppBel0XbZPZ80qBts8q0YltnqxMYnfmUfUbkRg1IhfRMbR2fhH4Rcs5tRcIV2tGjXA2HuqFfsvXXnbDj9tIqR_p8BiQHIrJsUWxxNsh2vPMSOGU6IewNeckPlFi3cA4mLTRzHaoaUymUvXFqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO)  با صدور هشداری فوری از «حمله پهپادی» علیه یک نفتکش در نزدیکی لنگرگاه بندر صحار در عمان خبر داد.
بر اساس به‌روزرسانی این نهاد نظارتی، این رویداد پس از تایید اصابت مستقیم یک پهپاد به این نفتکش، رسما به‌عنوان «حمله» طبقه‌بندی شده است.
بنابر این گزارش، مقام‌های محلی عمان در حال کمک به تخلیه خدمه کشتی هستند، اما تا زمان انتشار این اطلاعیه، ارزیابی دقیقی از میزان خسارات وارده، تلفات احتمالی و اثرات زیست‌محیطی آن در دست نیست.
@
VahidOOnLine
روابط عمومی نیروی دریایی سپاه پاسداران با انتشار اطلاعیه‌ای از انفجار و آتش‌سوزی یک نفتکش خبر داد و اعلام کرد: «یک نفتکش از نوع شاتل با ۷۵۰ هزار بشکه نفت خام، بی‌توجه به هشدارها و اخطارهای نیروی دریایی سپاه تلاش نمود از مسیر غیرمجاز عبور کند که به مین دریایی برخورد و دچار انفجار و آتش‌سوزی شدید شد.»
بنابر گزارش خبرگزاری فارس، این سومین نفتکشی است که طی روزهای اخیر در اثر برخورد با مین‌های دریایی به دلیل «نقض هشدارها و تردد در مسیرهای تعیین‌نشده» دچار آتش‌سوزی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/VahidOnline/78695" target="_blank">📅 00:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqdQtWYSwILbbcUwTFrcbWyCG2JojpEp-GDXTuSXYhkpUb9E2qVfbcvh4d3RoM78ftLc0ADmGfwMyBkQa9kAuMEgMh9tG6uKeUjCjc3jkNQCpGl45sK7LGFFCmEMxqt82fVu_D5KGcQNep8Zz2juKHsWS2TZQHbf3jl432f8CFZZ1jyaIXyuMs_7PhHtLjSXOkTLwJSIEpmsHYmC4TyUvrjLNY4kJXv_VVTdO8l0jJ0deM1qLYCEBGdR_nw6DVTS4ncdtgT01snsA1mUxBa3yffUjy9vE--eaJ2WPnEQ5BqrkeO-2gwSVAK6NAEv9GeAKIZOSdvq6YYCcBgaLOVzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه ریاض روز یکشنبه ۱۹ مهر بار دیگر هدف قرار گرفت.
ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد که یک «پرتابه ناشناس» فرودگاه بین‌المللی ریاض را هدف قرار داده است.
ترکی المالکی، سخنگوی ائتلاف، گفت این پرتابه به پایانه ۴ فرودگاه بین‌المللی ملک خالد اصابت کرد و موجب آتش‌سوزی شد.
این در حالی است که حمله موشکی روز گذشته به فرودگاه بین‌المللی ریاض که حوثی‌های یمن پس از ساعت‌ها تنها به طور تلویحی مسئولیت آن را پذیرفتند دست‌کم ۱۲ کشته و بیش از ۳۰۰ مجروح برجا گذاشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/78694" target="_blank">📅 19:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qBt_kQBvAI_c4PqWnLbjgaE4cTmVsDl62qUXF81wWYckuDXprlnCBhPnNDtkP7xg0k_RVGOExpO6E6zcGLD0Fw3kykpwPCp9wsAeYAhdJcXAr_Tjqjc_amFtn3Io7m9mcyeKxPqKMCy8k-NlEOuL9ana3dMmGQ_fYfixL6ePJZ-YD2qiBUj6Nq3lXrstOsFuadOSPQjQpT8fpWyKVsiSpLgfe_uPrevbiW3jNBrBmlvtSOr1AinFWuKWh8e05P8B5jPp1xOi6GJu1SEOepZ3CCGlEb6hYWcuZkM1xMl3Mwb_pwiSVQFnmMIK_wSppXPcs-A4sb66Sykp19PxoJzEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3ec7037002.mp4?token=utFesqA1b0J8LuVkawTdqHMHbYy4YKF-aKP-uz4K0viFTTi2Lxppwi3U8MRcV9zGsgVh4QDoI3N4yhj7H8uX3Qk8rJioYMa-e2uOtF8Lvz7JO2VJ1vUKQZYuXV4quc4NvTaIdcnwhZftkyav7dxJghuao9-1N0svFGmC6in1N5aF4wnwyLu8oaZjpl-L17HoagcI_bQbIltuLgbbE6B3luaLtuEdba-B7RoIKEiBspg6yuqbh0I77xtR4YvC4x6-H3-QalvFeN8C0ffUxDf64ENETT-mr-SaWDe5UFxWhOTSs2RJ2HYec0TyN5EATd9poH7Xtq5NyH09IgT-oaOYTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3ec7037002.mp4?token=utFesqA1b0J8LuVkawTdqHMHbYy4YKF-aKP-uz4K0viFTTi2Lxppwi3U8MRcV9zGsgVh4QDoI3N4yhj7H8uX3Qk8rJioYMa-e2uOtF8Lvz7JO2VJ1vUKQZYuXV4quc4NvTaIdcnwhZftkyav7dxJghuao9-1N0svFGmC6in1N5aF4wnwyLu8oaZjpl-L17HoagcI_bQbIltuLgbbE6B3luaLtuEdba-B7RoIKEiBspg6yuqbh0I77xtR4YvC4x6-H3-QalvFeN8C0ffUxDf64ENETT-mr-SaWDe5UFxWhOTSs2RJ2HYec0TyN5EATd9poH7Xtq5NyH09IgT-oaOYTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا
گزارش
کرده است که یک نفتکش در حال عبور از تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفته است.
براساس این گزارش‌ها این نفتکش در حال خروج از تنگه هرمز بوده و «از ناحیه سمت چپ» مورد اصابت قرار گرفته است.
مرکز عملیات تجارت دریایی بریتانیا همچنین گفته این اصابت به کشتی آسیب رسانده، اما تمامی خدمه در سلامت کامل هستند و هیچ‌گونه پیامد زیست‌محیطی نیز گزارش نشده است.
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از منابع خبری گزارش داد که یک کشتی در مسیر جنوبی تنگه هرمز بر اثر اصابت یک پرتابه دچار آتش‌سوزی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/78692" target="_blank">📅 18:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78691">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNlHWk4Xtuz6113OVa469_A8E_pvfOKc1Y-isA8sOtF8ML-cEUtgbfPOATxNSCx4PLovH1uVoIbFBtIJh6_Gofy4fGojAVxKo20HLq551ssWmq1QHzsKgUk0b1zB3lGKxrF1wEfTwCGmYXYvODt4Law-BGCv7eleN3yY-Df8MAclKLJcZcJj1cWFz_HxVNM1kmfZ0H-gIZLl2SBUQWewBwFC9qKoLpge0wdezAUY_Oq4iD4IUUSD8p-QXQBqO6uf2o7i68W-Tlqif73-GiekVPKHmY5rj28adXAzP9L0oaz63PEoJtZ84dLBwHB6lDxgFVaSkV0aQ3E1TSdLrpRVLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرزاد شهبازی، از وکلای متهمان پرونده «میدان علیخانی اصفهان» و وکیل علیرضا سپاهی، با رد روایت رسانه‌های حکومتی اعلام کرده است اتهام قتل ماموران انتظامی به هیچ‌یک از متهمان این پرونده تفهیم نشده و دادگاه نیز به این اتهام رسیدگی نکرده است. تاکنون پنج نفر از متهمان این پرونده اعدام شده‌اند و هفت نفر دیگر در خطر اعدام قرار دارند.
اظهارات این وکیل در واکنش به انتشار مصاحبه‌ای در رسانه‌های حکومتی مطرح شده است که در آن زنی، معرفی‌شده به‌عنوان همسر یکی از مأموران کشته‌شده، متهمان را به قتل و سوزاندن ماموران متهم می‌کند. انتشار این مصاحبه پس از افزایش انتقادها از اجرای احکام اعدام، به‌ویژه اعدام علیرضا سپاهی، صورت گرفته است.
شهبازی همچنین حضور این زن در محل اجرای اعدام‌ها را زیر سوال برده و پرسیده است وقتی موضوع پرونده قصاص و حق شخصی نبوده، بر چه مبنایی به او اجازه حضور در محل اجرای حکم داده شده است.
شهبازی روز شنبه ۱۸ مهر ۱۴۰۵ در پیامی در اینستاگرام نوشت: «به هیچ عنوان اتهام قتل برای هیچ‌یک از متهمان پرونده میدان علیخانی و میدان شهدا تفهیم نشده است.»
او تأکید کرد موضوع «سوزاندن ماموران در راستای قتل عمد» نه در دادگاه رسیدگی شده و نه از اتهام‌های مطرح‌شده در رای بوده است.
شهبازی علت ورود نکردن دادگاه انقلاب به موضوع قتل را نداشتن صلاحیت رسیدگی به این اتهام عنوان کرده است.
پرونده میدان علیخانی پس از کشته‌شدن چهار مامور یگان ویژه در جریان اعتراضات ۱۸ دی ۱۴۰۴ در اصفهان تشکیل شد. رسانه‌های حکومتی پیش‌تر ویدیوهایی از اعترافات متهمان در بازجویی‌ها، بازسازی صحنه و جلسات محاکمه در شعبه اول دادگاه انقلاب اصفهان منتشر کرده‌اند؛ اعترافاتی که نهادهای حقوق‌بشری آن‌ها را اجباری و فاقد اعتبار می‌دانند.
علیرضا سپاهی بامداد دوشنبه ۱۳ مهر اعدام شد. مای ساتو، گزارشگر ویژه سازمان ملل در امور حقوق بشر ایران، در واکنش به اجرای حکم، از نگرانی‌های جدی درباره شکنجه متهمان و رعایت‌نشدن دادرسی عادلانه در این پرونده خبر داده بود. به گفته ساتو، حکم در حالی اجرا شد که وکیل سپاهی همچنان برای رسیدگی دوباره به پرونده تلاش می‌کرد.
سپاهی پیش‌تر نیز در آستانه اعدام در ملأعام قرار گرفته بود، اما پس از حمله قلبی به بیمارستان منتقل شد. در همان شب، شهروندان برای جلوگیری از اجرای احکام تا سپیده‌دم در میدان علیخانی ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/78691" target="_blank">📅 16:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TM16SOT5Gkd-3NLZcebd0d1DlfKNw8WzfldwSYMieaSpw8ZhWcxKkh7E8wEIdbSVS3bbDuWtqkusOJog_mAP98GOhrs4XO67MM2oLsSZ83Qx1dGcriz-jsHQ0bsF4yKrOU1rzcZwEw1hYibcVwIowKH2tVE1IMoKLNeOjQADL8XGs6iJmNY48y6SJNGy64DNw9nvJAJPM__4IXPbopPXwmx2bl6WGvmsIuOnR9U0-Uu8Ftzzc3V-BZ0bWuyAASlvtlPOA542rERXXkNneECMXMvxBusXGigxAvMAUiNg4CVvKQwqszRL_z7lMZyb-gk8MoYiy3LUFbGcIS97rqo3SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان مدیریت بحران ایران اعلام کرد در سیلاب و رعد و برق پنج استان کشور هفت نفر جان باختند و دو نفر مفقود شدند.
به اعلام این سازمان، دو مفقود در استان گلستان ناپدید شده‌اند.
در شهرستان سوادکوه شمالی استان مازندران دو پل کاملاً از بین رفت. آب‌گرفتگی در معابر و خانه‌های این شهرستان گزارش شد و شماری خودرو در آب ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78690" target="_blank">📅 16:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78689">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vpyLm_bbzUczDc6Lj0x-7OjiunH0HRei3F-6gMxdIkSZW6VYGveXFsP3Uw-rXmgiqZyIA2dAnG7ZICkzChOrwKxJ_uW64PriWUlXKFvexUVFcgcYFjy0nTAwTM-0UPPFTZp-s0bWsScRYHlnlrhM13eWOOEBnSSn-YYhDKKfWl0zRGlglD-1F9Ql44uw0noX2rRXQsJTWZkbsb429Y1oGcgCUm6dRL5eFakkb2TqZy5Y3iUnbPDHxaXyx9ZZQSk0vm0xNYzdyODAmvvX55uMkRPlZUNlDu1QqoMx2JQrKylf-_bNNmMhgySf5_P_fQccAyjwOPOI_vhrQ0Ob-Ttn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی از اعدام یک مرد به اتهام قتل یک مامور نیروی انتظامی در بندرعباس خبر داد.
این مامور نیروی انتظامی رضا احترامی و مأمور یگان امداد شهرستان بندرعباس معرفی شده است.
متهم نیز پیش‌تر با نام «دانیال» معرفی شده و ادعا شده بود که این قتل چهار سال پیش هنگام درگیری با قاچاقچیان سوخت، بر اثر زیر گرفته شدن با خودرویی که مرد اعدام‌شده رانندگی آن را بر عهده داشت، روی داد.
شنبه نیز دستگاه قضایی جمهوری اسلامی از اعدام جابر خسروی، زندانی محکوم به قصاص در پرونده قتل یک مأمور انتظامی خبر داد.
این پرونده به حادثه‌ای در بیمارستان ولایت دامغان در ۱۱ شهریور ۱۴۰۱ بازمی‌گردد؛ حادثه‌ای که بنا بر ادعای مقام‌های قضایی، در جریان آن سلاح مأمور انتظامی گرفته شد و او بر اثر اصابت دو گلوله جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/78689" target="_blank">📅 16:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OG5R0TZoSryAgnZc6Q6lz1RooGQrRXmmjHkcSJUHl7dipCN-w5KzTUKSrq92_a1Rl98iY45aztS4WdEwAymEJKDoWc8Lu5gNNgRTq2Fi6tyj_LXxn604vE9TbXAesDXoIa1FlLU8UpHiXP_aajnc3lOqD70gFxK_zORjwN4FDS0v_w5WPQ-U7q-kiX36X70CB-rBMYp8rCRcoN4mND7IJuYuonrenxz3nZCF3e4fuPIJCeokyvhw4QD_msLtvmquQe8DsAavgqxgs8-OEZDdNu1F0cCpI_Lf8beGaidog6AtERki49OwkKHvr-VqBP1CE76BEPmmYZURAoaN2zkDaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی در بیانیه‌ای گفت حمله روز شنبه ۱۸ مهر به فرودگاه بین‌المللی ملک خالد در ریاض، ۱۲ کشته و ۳۰۹ زخمی بر جای گذاشته است.
بر اساس این بیانیه که بامداد یکشنبه ۱۹ مهر صادر شد، چهار نفر از کشته‌شدگان شهروند عربستان سعودی و هشت نفر دیگر اتباع خارجی، شامل دو بنگلادشی، یک آمریکایی، یک مصری، یک اردنی، یک سوری، یک فلسطینی و یک سودانی هستند.
این سازمان همچنین اعلام کرد که شرایط سلامتی شماری از زخمی‌ها وخیم است.
به گفته سازمان هواپیمایی کشوری عربستان سعودی، تمامی مجروحان در چندین بیمارستان تحت مراقبت‌های پزشکی لازم قرار دارند.
در این بیانیه همچنین آمده است که حمله به فرودگاه بین‌المللی ملک خالد خسارات مالی و مادی نیز به همراه داشته و ارزیابی میزان این خسارات همچنان ادامه دارد.
حمله روز شنبه سومین حمله این هفته شورشیان حوثی مورد حمایت جمهوری اسلامی در یمن به فرودگاه بین‌المللی ریاض بود. شورشیان حوثی مسئولیت حمله را بر عهده گرفتند. حوثی‌ها همسو با تلاش‌های جمهوری اسلامی برای ناامن کردن تنگه هرمز، سعی کرده‌اند به کشتی‌ها در تنگه باب‌المندب که دریای سرخ را به خلیج عدن و اقیانوس هند متصل می‌کند و یک تنگه حیاتی به‌شمار می‌رود حمله کنند.
طبق گزارش‌ها روز شنبه، مسیر تمامی پروازها از ریاض تغییر داده شد و فعالیت‌های فرودگاه به‌طور موقت متوقف شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78688" target="_blank">📅 03:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78687">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dBneWBiF7_NEHQcAOyyeaSiTcvGqtD4N8TGPlkd6gIMOLA1p6voi_yr3mwHvfHAxg1EknkGZYrOkkA1YReCyL8KcxyZNXZfYc3Ry42ueWR90WTIgx4LnmFkMzLBE6I2u4SfsSHo5oCAx78spHrjG48voPCi9PHqBW725Ju90sxZyCKMiZKdPqrIpgRtkXit76GcK3SRaGr8_r5rGm99w-72dOv0tlMkSLedTGvGJYuW0guGeQSdZVpS9en6MniKJKmOi6m1K1k4uz45KpJIRUptVZsNEF1oUmdSElTLd9t2_zLCd6d_onyQISMjROEBIVh922lw2UJuvARvWCY_3ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
سازمان عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
ناخدای یک نفتکش که در حال خروج از تنگه هرمز بوده، گزارش داده است که یک پرتابه ناشناس به سمت چپ کشتی برخورد کرده و باعث آتش‌سوزی در آن شده است.
بر اساس گزارش‌ها، خدمه کشتی در سلامت هستند. در زمان انتشار این گزارش، میزان خسارات و پیامدهای زیست‌محیطی حادثه مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78687" target="_blank">📅 01:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78686">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGuphiWAtP1pYtn96hYaHUe2GpiBnjTAycpcday9sTuY6TLHeS4R4lmJTsHQmhMzZ2Zpn3YVd1apGSq-PuBKgUR-cMVSV2Lu8N56AMKgd0xSU_NnyP7kJg3CS1p0STjioiJEyLjtA420Ym4A_ppEmXyhG9r9S-H92VjEFUzcc3cJZLScdzZUCVkPgcLPN3lUC_O4Yu6g7Kk0hpoRYH6ZuRBwp0ddW8DLqF4mrI6nm-Cwv43GNQYfKSSHCNfkSpuTs1Bz9yglrL4z58uDVGmi69ivwPW5wq4jWZHm5uuaw8TBxxQ8GQbfjdL8CUQa5uWW7DM28OZGSc5GAfFBLKUhsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، روز شنبه، طی سخنرانی در ایالت تنسی درباره ایران گفت: «اوضاع تا حدی آرام شده است. آن‌ها احتمالا پیش از انتخابات دست به اقدامات اضافه‌ای می‌زنند و فکر می‌کنند این اقدامات به ما آسیب می‌زند، اما ما می‌توانیم این ماجرا را خیلی سریع تمام کنیم.» او در ادامه افزود: «آن‌ها اصلا نمی‌دانند من چقدر با آن‌ها خوب رفتار کرده‌ام. واقعا خبر ندارند که چقدر با آن‌ها مهربان و با مدارا بوده‌ام.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78686" target="_blank">📅 01:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78685">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcdec5c24b.mp4?token=SGT5-XyS1E_A84GBoKVrGIDYVdAZLZJWWoE7m_SFnl-vzZFCigSY1kjyAaR1WXhM5q2KyRqulea450CqUe1LWjbjXdWlbnp4K3Z4PkajI-adSc_SNTWKO5PmXZHjBBnJOit7QNTwlsrzoSvvRaymdDp2MoJGTa4vQlre3qN7fygCsS4urjscvmeENGlJu8bPoI2Yuyn1SophQUT9Cb4fJjp7806TDDAfxjnLLRBovcLOvHF37eQyq8qFZSMXeX9ILhZNZsj7Hnyumato-x9w9-HngruqEiIir5FSCL43YelHX8g6XtPHmkw6aHLfMIT-3mHOTx4zBv1XgX8PB6ef0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcdec5c24b.mp4?token=SGT5-XyS1E_A84GBoKVrGIDYVdAZLZJWWoE7m_SFnl-vzZFCigSY1kjyAaR1WXhM5q2KyRqulea450CqUe1LWjbjXdWlbnp4K3Z4PkajI-adSc_SNTWKO5PmXZHjBBnJOit7QNTwlsrzoSvvRaymdDp2MoJGTa4vQlre3qN7fygCsS4urjscvmeENGlJu8bPoI2Yuyn1SophQUT9Cb4fJjp7806TDDAfxjnLLRBovcLOvHF37eQyq8qFZSMXeX9ILhZNZsj7Hnyumato-x9w9-HngruqEiIir5FSCL43YelHX8g6XtPHmkw6aHLfMIT-3mHOTx4zBv1XgX8PB6ef0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز شنبه ۱۸ مهر تأیید کرد که در پی حمله به فرودگاه بین‌المللی ملک خالد در ریاض و زخمی شدن شماری از افراد، فعالیت این فرودگاه متوقف شده است.
دونالد ترامپ، رئیس‌جمهور آمریکا، در واکنش گفته است که از این حمله مطلع شده و درباره آن تصمیم خواهد گرفت.
دونالد ترامپ در جمع خبرنگاران و در پاسخ به این سؤال که آیا آمریکا به جنگ عربستان سعودی با حوثی‌ها خواهد پیوست، گفت: «ممکن است. این موضوع را بررسی خواهیم کرد. ما تازه از حمله اخیر مطلع شده‌ایم. تصمیم‌گیری خواهیم کرد. خیلی سریع اقدام می‌کنیم.»
پیش‌تر برخی رسانه‌ها خبر داده بودند که حکومت ریاض از آمریکا خواسته حوثی‌ها را هدف حملات نظامی قرار دهد.
پایگاه خبری اکسیوس یک هفته پیش گزارش داد که شماری از بلندپایه‌ترین مقام‌های امنیت ملی دولت دونالد ترامپ روز جمعه در نشستی چندساعته و اعلام‌نشده در کمپ دیوید، درباره گام‌های بعدی آمریکا در جنگ ایران و همچنین درگیری عربستان سعودی با حوثی‌های یمن گفت‌وگو کرده‌اند.
با وجود تأیید رسمی وقوع حمله و زخمی شدن افراد، مقام‌های عربستان هنوز شمار دقیق مجروحان و میزان خسارت واردشده به فرودگاه را اعلام نکرده‌اند.
حوثی‌های مورد حمایت جمهوری اسلامی نیز تا زمان انتشار این گزارش مسئولیت حملهٔ روز شنبه را بر عهده نگرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78685" target="_blank">📅 22:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9492aa3856.mp4?token=ktVYRKlAg9X6TJigs8UBNa_rlk_fXyDg4RLyq_TrHlyEBcexEzvJbJOtTu8cXfmn3N17IdQvzI4KJQlbIsHFnITiZMBDYoU62KpEZAO7HXsiXgMZHu3EZUqVOJiQjwssGWqtoiRL03YbAzCr5J1IfzE5q8nRTOxWkVTEKjsnU2OL0zhUUHpj5AOlXNsR3HcD5_JJhB_zXRRlohhLIfSB6O8GuNtgp-TdsOvsqs5RpHuUgN-Pv71zXELgs0bvF0daBYtCAU1DLO23LmJSAZu_eeoAQYsekcb2sRRWYCeFwbcgcbzo3i4vRh-t4W2BnUA_jMKh2yV47Kl0rSpOmz0cUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9492aa3856.mp4?token=ktVYRKlAg9X6TJigs8UBNa_rlk_fXyDg4RLyq_TrHlyEBcexEzvJbJOtTu8cXfmn3N17IdQvzI4KJQlbIsHFnITiZMBDYoU62KpEZAO7HXsiXgMZHu3EZUqVOJiQjwssGWqtoiRL03YbAzCr5J1IfzE5q8nRTOxWkVTEKjsnU2OL0zhUUHpj5AOlXNsR3HcD5_JJhB_zXRRlohhLIfSB6O8GuNtgp-TdsOvsqs5RpHuUgN-Pv71zXELgs0bvF0daBYtCAU1DLO23LmJSAZu_eeoAQYsekcb2sRRWYCeFwbcgcbzo3i4vRh-t4W2BnUA_jMKh2yV47Kl0rSpOmz0cUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از هو شدن اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران منتشر شده است.
این اتفاق شامگاه جمعه ۱۷ مهر، هنگامی رخ داد که بقائی برای سخنرانی پشت میکروفون قرار گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78684" target="_blank">📅 20:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78683">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54a079f69b.mp4?token=AcBSUZXLX4DWKvJGPyAZ7of7H2skRlLGHNuWr3vtl4iy3ofdROVJjWwH39lukW7rfd0RBlbG7-5JAUz-qFiE9CogXFZMplYfG-PJkxYZdo4fG3VREOGsYhs217nekzps0q6KqBK7LtgcvRi7CmavISn8w6wf8jTCuDpb2umvWNqOymS5JT6aOOcSIvK0TNvnkvM1GuHZo0cVqHMATxgykFfkpOf4kRBlsCkTPQ3SoLfvNCnde5FdnFFTeR5jlFAh_ktI8-iQF9VF4h7laPh8JpdDOzT2rdsQXMHg4-Lu4sa7Yn9KpC0KRxejQaCL5FiQ9W6pEQcZCpns4VzgtpxMqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54a079f69b.mp4?token=AcBSUZXLX4DWKvJGPyAZ7of7H2skRlLGHNuWr3vtl4iy3ofdROVJjWwH39lukW7rfd0RBlbG7-5JAUz-qFiE9CogXFZMplYfG-PJkxYZdo4fG3VREOGsYhs217nekzps0q6KqBK7LtgcvRi7CmavISn8w6wf8jTCuDpb2umvWNqOymS5JT6aOOcSIvK0TNvnkvM1GuHZo0cVqHMATxgykFfkpOf4kRBlsCkTPQ3SoLfvNCnde5FdnFFTeR5jlFAh_ktI8-iQF9VF4h7laPh8JpdDOzT2rdsQXMHg4-Lu4sa7Yn9KpC0KRxejQaCL5FiQ9W6pEQcZCpns4VzgtpxMqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز شنبه ۱۸ مهر تأیید کرد که در پی حمله به فرودگاه بین‌المللی ملک خالد در ریاض و زخمی شدن شماری از افراد، فعالیت این فرودگاه متوقف شده است.
یک منبع دیپلماتیک به خبرگزاری فرانسه گفته است که حوثی‌های یمن حدود ساعت سه بعدازظهر به وقت محلی با موشک به این فرودگاه حمله کرده‌اند. بر اساس گزارش‌های اولیه، ده‌ها نفر در این حمله زخمی شده‌اند.
روزنامهٔ وال‌استریت جورنال نیز به نقل از مقام‌های سعودی گزارش داد که موشک‌های شلیک‌شده از سوی حوثی‌ها مستقیماً به ترمینال شمارهٔ سه فرودگاه اصابت کرده‌اند.
یک منبع بیمارستانی به خبرگزاری فرانسه گفته است که پنج نفر از مجروحان در بخش مراقبت‌های ویژه بستری شده‌اند. یکی از شاهدان عینی نیز گفته است هنگام حضور در گیت ۴۰۳ ترمینال پروازهای داخلی، شاهد اصابت موشک به محدودهٔ گیت ۴۰۱ و زخمی شدن مسافران بوده است.
این شاهد به خبرگزاری فرانسه گفت: «دیدم که گیت ۴۰۱ هدف قرار گرفت و افرادی جلوی چشمانم زخمی شدند. همه فرار می‌کردند.»
حملهٔ روز شنبه در حالی رخ داد که فرودگاه ریاض پیش‌تر نیز در روزهای چهارشنبه و پنج‌شنبه هدف حملات حوثی‌ها قرار گرفته بود. این حملات در مجموع چهار کشته و چندین زخمی بر جای گذاشت و به یک فروند هواپیمای مسافربری شرکت سعودی آسیب جدی وارد کرد.
سه شهروند سعودی، از جمله یک خلبان، در حملات روز پنج‌شنبه و یک شهروند سودانی در حملهٔ چهارشنبه کشته شدند. حوثی‌ها مسئولیت این حملات را پذیرفته‌اند.
تشدید حملات موشکی به عربستان در پی ازسرگیری درگیری‌های گسترده میان حوثی‌ها و نیروهای دولت مورد حمایت ریاض در یمن صورت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78683" target="_blank">📅 20:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS6daEr-8rUaew1zT1h3fhZHhKcBxvF8OhAt-fmmIGmrWPvR80fv6URYMHKTNC0lRbx5qqrxFjyUgJjThu6Abrcv5danR0yNL4FxaDfVn2yeRtkQdahKVvYNo-FurwKR5zc3bPrPu63qOs4iZmzjey_LWfWRMmGq7YHQckpdSZ28ullTV1PLoVr3oN34If3yTvkiEm567YhmOYjFNSHXY-05B8t4l03tJKKyGxBRf13r4ddkaUPt3kNBp0cUaIomMuoVFwuzLDNnXqPVkHU_XwK5ZdX-SdYoJfIOZIoKBPPGzD18RthKrd8-KEuBIIGOTTj3cTo1nQqkw1yua1aGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ کرملین اعلام کرد ولادیمیر پوتین، رییس‌جمهور روسیه، با هماهنگی مسعود پزشکیان، دیدگاه تهران درباره راه‌حل احتمالی پایان جنگ با آمریکا را به دونالد ترامپ منتقل کرده است. هم‌زمان، مسکو از ادامه مذاکرات غیر مستقیم تهران و واشنگتن حمایت کرده و گفته پیشنهاد انتقال اورانیوم با غنای بالای ایران به روسیه همچنان روی میز است.
@
VahidHeadline
در همون انتقال به
توافق گازوئیل
رسیدند؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78682" target="_blank">📅 19:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LGocOXQNuH_ZxNEQ5FVEUr-5xuGMowAx2cSp_383-pEAeXR9OVCpqGUG4xHp5VMqVMH8-iV04I2himhcU46aHGCXcDbjAQxhI-wf9wbb5uWZuyCpPm1ShJIO0jzZ5SXnTtAJXEmTYhGHtYvvIdJ7EKGtvEm8n7mswkcHGfgb-rm2fHtPQZOgjU1IbeY7lL2oBy2QjuqRi096L14hOM9DFRJ2RCFgCD9oY9p8CsDWmuWze-ffJGAonbMiwX3Ib0fxVJEnzv2FcWFKFfWHSbYR6NcjwcJ5azEtU-pm_LOIoIXfSaLo-kBNIVqBHGACHazhxiF8-KRM_FcStETMsK9GVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه فعالان حقوق بشر در ایران در گزارشی به مناسبت روز جهانی مبارزه با مجازات اعدام اعلام کرد طی یک سال گذشته، دو هزار و سه نفر در ایران اعدام شدند که دست‌کم ۶۹ نفر از آنان با اتهام‌های سیاسی و امنیتی روبه‌رو بودند.
شمار اعدام‌ها در این دوره نسبت به دوره مشابه پیشین حدود ۲۹ درصد افزایش یافته و از هزار و ۵۵۳ نفر به دو هزار و سه نفر رسیده است؛ بالاترین رقم ثبت‌شده در ۱۰ دوره گزارش‌دهی.
بر اساس آمار این گزارش، شمار اعدام‌ها از ۵۰۵ نفر در دوره ۲۰۱۶–۲۰۱۷ به دو هزار و سه نفر در دوره ۲۰۲۵–۲۰۲۶ رسیده است.
در تفکیک اعدام‌ها بر اساس نوع اتهام، ۵۷٫۵۶ درصد مربوط به قتل و ۳۶٫۲۵ درصد مربوط به جرایم مواد مخدر بوده است. سایر اعدام‌ها با اتهام‌های سیاسی و امنیتی، تجاوز، محاربه غیرسیاسی، فساد فی‌الارض، جرایم اقتصادی یا اتهام‌های نامشخص ثبت شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78681" target="_blank">📅 19:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78680">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6008e28bbf.mp4?token=Ur87UVMfk-53gVuG6U-OLRy9gaXDWvvyVuBiPdNm9lNpLhIlF8_lcL-_O5UZsYm_o0WGsN1txFwq8kxPIUF6xOBBC6t275xuTNStSq2j-_C2MTxdIWKY14UZEOO9o_z0-uvfxCgSss5ytlNhUSUSjLR11S3kygBCHlrJOyh1_kuQa-4sUx-49bmJmj6zsiLxSENGvOwDDWMfPEqREKoYg-ASGm4rNT7tSD97nOo_ppbw5306d3km4FfQSlsWW3MG_JB8A5AzaO8WA1cfd6MPQ2FdP4IqEkw-dUuNwelH8o4ffHZldvVS0PiCwBywQgMf-X8VeFQTRfg2UKT82A-3Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6008e28bbf.mp4?token=Ur87UVMfk-53gVuG6U-OLRy9gaXDWvvyVuBiPdNm9lNpLhIlF8_lcL-_O5UZsYm_o0WGsN1txFwq8kxPIUF6xOBBC6t275xuTNStSq2j-_C2MTxdIWKY14UZEOO9o_z0-uvfxCgSss5ytlNhUSUSjLR11S3kygBCHlrJOyh1_kuQa-4sUx-49bmJmj6zsiLxSENGvOwDDWMfPEqREKoYg-ASGm4rNT7tSD97nOo_ppbw5306d3km4FfQSlsWW3MG_JB8A5AzaO8WA1cfd6MPQ2FdP4IqEkw-dUuNwelH8o4ffHZldvVS0PiCwBywQgMf-X8VeFQTRfg2UKT82A-3Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، طی سخنرانی در ایالت نیویورک اعلام کرد: «مسئله ایران به هر ترتیبی که شده، خیلی زود حل خواهد شد. یا آن‌ها همه‌چیز را به ما می‌دهند، یا دیگر اصلا وجود نخواهند داشت. خودشان هم این را به خوبی می‌دانند.»
او همچنین با اشاره به بحران اقتصادی عمیق در ایران و تسلط نظامی ایالات متحده بر منطقه تاکید کرد:
«ایران در ورطه بزرگی گرفتار شده، از تورم ۳۰۰ درصدی رنج می‌برد و هیچ پولی ندارد، تا جایی که ارتش و نیروهای پلیس آن حقوق دریافت نمی‌کنند. ایران هرگز به سلاح هسته‌ای دست نخواهد یافت و ممانعت از دستیابی آن‌ها به این سلاح دلیلی بود که ما را وادار به رفتن به آنجا کرد.»
ترامپ در ادامه افزود: «به لطف ارتش ایالات متحده اکنون کنترل کامل تنگه هرمز را در دست داریم و امروز حجم نفتی که از این تنگه عبور می‌کند حتی از دوران پیش از جنگ هم بیشتر است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78680" target="_blank">📅 07:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78679">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sk8Bk5CQtkYj1vIEfktcCPaPTekvnuC0-63P-e2f9W26Y_k84pOWYCQKfuvomjM8pOdbmYBhcVmkwQNRC_KO975bexcm8ptrEG9GJ0BsBqHPr4UccDa7ZDVCixfoqiX7tdRjhqhL8_n5OWahpbZxQUxEEyXhREtYxBjs2GafwAXSisHq5Df8lJraIuYmWEA9mLJGbJ-WakS9evvac3TVOBdl5SNuD9P3KHGYSFYjhxovsOcjj3T20fo9rbk_aMqMkrYpqTc2IsSutk1ldcqQdE7Sf3FZqYiU7l29mKVC5iAIAubYPk5dA5W0sakYHEuT9UxwcQMUL4HbAkjeVMHAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در شبکه اجتماعی تروث سوشال اعلام کرد کنترل کامل آمریکا بر تنگه هرمز، همراه با توافق تازه واشینگتن و مسکو برای عرضه میلیون‌ها تن گازوئیل روسیه به بازار جهانی، باعث کاهش سریع و چشمگیر قیمت این سوخت خواهد شد.
ترامپ گفت پس از گفت‌وگو با ولادیمیر پوتین، رییس‌جمهوری روسیه، توافق شده است که مسکو بلافاصله بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و جهان عرضه کند و ۵۰۰ هزار تن دیگر نیز در ماه نوامبر تحویل دهد.
به گفته او، روسیه پس از آن یک میلیون تن گازوئیل دیگر به بازار عرضه خواهد کرد و با توجه به وضعیت پالایشگاه‌های این کشور، سه میلیون تن دیگر نیز در مدت کوتاهی تحویل خواهد داد.
رییس‌جمهوری آمریکا گفت کنترل کامل تنگه هرمز از سوی واشینگتن و افزایش عرضه گازوئیل روسیه، قیمت این سوخت را برای مصرف‌کنندگان آمریکایی و دیگر کشورهای جهان به‌سرعت کاهش خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78679" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=vFD1cVrBsyO1RM3x-AdV72M_ppRTd_IPyEFGVsK-KgQMREDWGgeP8tnAuDJ6s-7Lf7dMOXKh-AHQ6NVcHz7zv_fv0mIdEAWhMgC7OZ2wLKjYeYXPXaemqJ_sfISWGXGUYFY9NpUz0ufwb7Te0GtZKZuw6TzWboCcPacPMiEZ3ABfCKJEKkocStXqd3zENibbSXqCNT7pbyRn4XGbCkFUh0wm1pftmHTn02CLY2dhwFpcn8EhdHigI6faSLLoUHw8dero1HWpwB9NM9dOu6EtUtlrq7NsVxqAr5h5aObpgbmyb_nTurkF0KiU8KFqdeB-HimmeiNv1D1VxjKYXXR2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=vFD1cVrBsyO1RM3x-AdV72M_ppRTd_IPyEFGVsK-KgQMREDWGgeP8tnAuDJ6s-7Lf7dMOXKh-AHQ6NVcHz7zv_fv0mIdEAWhMgC7OZ2wLKjYeYXPXaemqJ_sfISWGXGUYFY9NpUz0ufwb7Te0GtZKZuw6TzWboCcPacPMiEZ3ABfCKJEKkocStXqd3zENibbSXqCNT7pbyRn4XGbCkFUh0wm1pftmHTn02CLY2dhwFpcn8EhdHigI6faSLLoUHw8dero1HWpwB9NM9dOu6EtUtlrq7NsVxqAr5h5aObpgbmyb_nTurkF0KiU8KFqdeB-HimmeiNv1D1VxjKYXXR2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره صداهایی که نمی‌دونم این بار هم آتش‌بازی بوده یا چی:
سلام وحید جان شرق تهران صدای پدافند و انفجار ممتد
صدای یک انفجار و بعد چندتا پدافند شرق تهران
وحید تهرانپارس صدای انفجار شدید بعد ضد هوایی الان ساعت ۸/۳۰
صدای شبیه پدافند یا تیراندازی در تهرانپارس شرق تهران
سلام وحید جان خوبی
پدافند تهرانپارس 5 مین  کار کرد ساعت  ۸:۳۰ دقیقه شب
وحید جان شرق تهران صدای تیر اندازی اومد الان
دود هم دیده میشه تو اسمون.
آپدیت:
دو ساعت بعد دوباره شرق تهران:
صدایی شبیه به تیراندازی در محله مجیدیه
ساعت ۱۰:۴۰ دقیقه ۱۷ مهر
چند دقیقه بعد: دوباره اومد این سری انگار رگبار بود
سلام ساعت ۲۲:۴۷ صدای تیراندازی چندین بار. مجیدیه شمالی‌
چند دقیقه بعد: الان هم دوباره اومد
صدای پدافند شرق تهران
سلام وحید جان
صدای پدافند همچنان پست سر هم
مجیدیه
صدای پدافند
مجیدیه
سمت مجیدیه تهران صدای تیر اندازی و پدافند میاد
صدای پدافند میاد
دولت کلاهدوز
سلام وحيدجان سمت اختياريه صداي پدافند مياد ساعت٢٢:٥٧
صدا پدافند سمت پاسداران
چند بار شلیک ساعت ۲۲:۵۷
سلام صدای تیر اندازی شمال شرق تهران ۱ دقیقه ممتد اومد الان قطع شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/78677" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78675">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/guud3mzXhE_TAOFpvEs4AG5804iAV4UKHgUu-pVM2DOHXd2syOV51VOFZ1kPBYU_JrwboULBOu8s5mIILAyc8LHDBmEaNUFDnSebpn77GzWWim5n6PEpJhpNBzqz9Y9wUnWZkqYM83RAtSlSVDqvwuVtUIazUbUVRMH-XwYU994-quVsisRZtd3MT_zPGVSgqW3MJuzj66MNtIYogXePrH_ZRJs-V7VikHRSYziM54kYIz1BrmA3BK8rCqeMUWfQjQnLoT7xtaEPGN71bqC_n0xAUVGtDhvkuaKZu917NooaEaV8ljLakV4MuVrL4i3a-gw1tdAwOz5I7ZGE8yluCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f20c8d9bec.mp4?token=GDPPKq5IzIk0OOeBvCupaYd-fhlXma2N3SAKPZH-e6CaFH3ZVN0anCuB8lLGJZ67ieI97Zxj-F-y_SqQL0tzTQbkOxSPNWnfaDa3SNG8FIwAQI8chcd6kKrgV0091JwqLqFaQKoEqc0N6ROruMVSNynsW9VpXDC2PiaX6q5HXgPGtOmROBZeE4NHFVCZ_a2l6r5eeeoZefAwpSKzK0-cwAZ0BE2s7qV5Gw7HpzlPdti9B6uMwb4Q8-UCjTO9du3wm9vSV-R1WeZlzh7WIlRafCToQlzwGUC5K003w4zp8xHjIayaoUCLSZrHT2lDHQ80gwY_3dLUqR1rHjjBbrjy4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f20c8d9bec.mp4?token=GDPPKq5IzIk0OOeBvCupaYd-fhlXma2N3SAKPZH-e6CaFH3ZVN0anCuB8lLGJZ67ieI97Zxj-F-y_SqQL0tzTQbkOxSPNWnfaDa3SNG8FIwAQI8chcd6kKrgV0091JwqLqFaQKoEqc0N6ROruMVSNynsW9VpXDC2PiaX6q5HXgPGtOmROBZeE4NHFVCZ_a2l6r5eeeoZefAwpSKzK0-cwAZ0BE2s7qV5Gw7HpzlPdti9B6uMwb4Q8-UCjTO9du3wm9vSV-R1WeZlzh7WIlRafCToQlzwGUC5K003w4zp8xHjIayaoUCLSZrHT2lDHQ80gwY_3dLUqR1rHjjBbrjy4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت اگر حکومت ایران به سلاح هسته‌ای دست می‌یافت، ممکن بود پس از حمله به اسرائیل و دیگر نقاط خاورمیانه، کشورهای اروپایی و شهرهایی مانند لس‌آنجلس و سن‌دیگو در آمریکا را نیز هدف قرار دهد.
ترامپ جمعه ۱۷ مهر در مراسم روز کلمبوس در کاخ سفید گفت جمهوری اسلامی پیش از حمله بمب‌افکن‌های بی‌۲ آمریکا، تنها دو تا سه هفته تا دستیابی به سلاح هسته‌ای فاصله داشت.
او گفت در صورت دستیابی جمهوری اسلامی به این سلاح، حکومت ایران به‌سرعت از آن استفاده می‌کرد و ابتدا اسرائیل و سپس دیگر نقاط خاورمیانه را هدف قرار می‌داد.
رییس‌جمهوری آمریکا افزود کشورهای اروپایی احتمالا پیش از آمریکا در معرض چنین حمله‌ای قرار می‌گرفتند و شهرهای لس‌آنجلس و سن‌دیگو نیز می‌توانستند از اهداف احتمالی باشند.
ترامپ گفت: «دیگر لازم نیست نگران این موضوع باشیم. آن‌ها به سلاح هسته‌ای دست نخواهند یافت.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۱۷ مهرماه در مراسم روز کریستف کلمب در کاخ سفید، با اشاره به درگیری‌های نظامی با جمهوری اسلامی گفت که این وضعیت به‌زودی پایان می‌یابد و قیمت سوخت نیز به‌شدت کاهش خواهد یافت.
ترامپ در سخنانش با اشاره به عملیات نظامی آمریکا علیه ایران گفت: «ما مانع دستیابی ایران به سلاح هسته‌ای شدیم.» او افزود که پایان درگیری‌ها از راه‌های مختلف امکان‌پذیر است و تاکید کرد: «به هر شکلی، این وضعیت خیلی زود پایان خواهد یافت.»
رئیس‌جمهوری آمریکا همچنین درباره توان نظامی جمهوری اسلامی گفت: «آن‌ها نه نیروی نظامی دارند، نه نیروی دریایی، نه نیروی هوایی و نه تجهیزات پدافند هوایی.» او در ادامه با اشاره به محاصره دریایی اعلام کرد که آمریکا مسیر عبور کشتی‌ها را مسدود کرده است.
این اظهارات در شرایطی مطرح می‌شود که واشینگتن هم‌زمان با ادامه فشارهای اقتصادی علیه جمهوری اسلامی، محدودیت‌های دریایی و تحریم‌های مرتبط با صادرات نفت ایران را دنبال می‌کند. تنگه هرمز نیز به یکی از محورهای اصلی تنش‌های نظامی و اقتصادی میان دو کشور تبدیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78675" target="_blank">📅 20:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bB-g6o2UzxzIwdW4M216r2EoGUBvLEW_OEyv4gQidc2TNN_tybjZ5djlZeKJXzjxDPxEx_YGvgt8qBmEOeKsCJNV3sK0uq7ccSMTPXLVvUedX0B6_pisUZjCHkqgAWFLb1C4opm5XV8KjJhk7dIwFYQI9Q_zIPwc8XVVfa2HWNuxAMhDfEsLUgxraDwvtqjOauGabLzsJFUbRQwB3gZkaBl7bEpiEebKwc__B_ksmSSUo9nRum6A6nh0aXTB11aiyZqol_V5b-MAtT9SN2hBYaF85LjnE6MDz-Z7HD2hYTc7ekXbXwQRGzUE9DiJX8XRGz4PxNq_iZ52dS87n7DmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صداوسیما با انتشار گزارشی اولیه، از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان سیستان‌ و بلوچستان خبر داد و نوشت در این حادثه نصرت افتخاری، معاون اجتماعی انتظامی استان سیستان و بلوچستان، در منطقه چشمه زیارت زاهدان کشته شد.
این منبع نوشت عامل اصلی بمب‌گذاری هنگام فرار کشته شد.
خبرگزاری فارس، رسانه وابسته به سپاه پاسداران نیز گزارش داد این حادثه در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان رخ داده و چند نیروی پلیس در جریان آن دچار جراحت شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78674" target="_blank">📅 18:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FjxYdJKOAq78R5dsNt4MgKIrOA7VKww9WWoti_3gtfV6yNuuVhXlnbsOqZ4E-OXzJmADJSBohoe0Q04uEUl7JF69alIogcTFB868m83tiMROU1NUBWwj-N5po-qLmZ5YIk7Zl4S2cqcquwNgp9uM5rdTeg6_2N9hNWHKKvsCVovVsYW3Nc0vqybVy1sW22u-qFE4SeZ0tHxG7dMz7-KXuSinpGzBRaWiECBMaRRJvJz0syl9O3QxYoyukwbQbOOcQ1wADd0U6FPrX_fg3_xKsh0evdBSAuhgAYlW5CatM6cWHlqM1tzcweA-nIhM4wOoILGzDPNkJDlBkxAWfM9w9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران،  اعلام کرد یک کشتی حامل گاز مایع به‌نام «ان‌وی سان‌شاین»، متعلق به شرکت نات‌ویت را هنگام عبور از جنوب تنگه هرمز هدف قرار داده است.
سپاه پاسداران اعلام کرد این کشتی در حال عبور از مسیری «غیرقانونی» بود و پس از اصابت، موتورخانه و سامانه رانش آن دچار آتش‌سوزی گسترده شد.
نیروی دریایی سپاه همچنین اعلام کرد کنترل تنگه هرمز را در اختیار دارد و اجازه حضور نیروهای نظامی آمریکا در این منطقه را نخواهد داد.
سپاه پاسداران در این بیانیه اعلام کرد شرکت‌های کشتیرانی که با آمریکا همکاری کنند، با تحریم و اقدامات تنبیهی علیه شناورهای خود روبه‌رو خواهند شد.
بر اساس این بیانیه، سپاه از این پس برخورد با شناورهایی را که از مسیرهای غیرمجاز عبور کنند، به تنگه هرمز محدود نخواهد کرد و این کشتی‌ها را در سراسر منطقه هدف اقدامات تنبیهی قرار خواهد داد.
@
VahidOOnLine
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)، روز جمعه ۱۷ مهر، با انتشار هشدار جدیدی اعلام کرد که حادثه‌ای در ۱۳ مایل دریایی غرب راس‌الخیمه در امارات متحده عربی رخ داده است.
بر اساس گزارش‌های دریافتی از منابع مختلف، این شناور مورد اصابت یک پرتابه ناشناس قرار گرفته که منجر به بروز حریق شده است؛ آتش‌سوزی مذکور تاکنون مهار و خاموش شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78673" target="_blank">📅 16:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il1UXXVji95d1XhjK7ZzAZpXsxEE3Ixogo2lIyukKDGuElwYZfEQu5Ot9HDeZjxsoc02PSKBJ6JWdmGT-jJir_yebCCj1k3YJk0t1SHHFEu7U3PxrIM9jC5kEu75L34OktSoeVSj9idmXDIaV8-RYcOqio4xyoVSFPeILP1HDucq-rsjnwS_4lUxzLcIdIhwh9B46uCB2sWJtyAiMRRIAxj30K1o4PDdRmn4nULpkZNCfgRCejG_HNzHmxEESwCwaivRGXO138bmzzkaCpHbg5-x7IpEUC-dp065u9py1A0PBKKtrj6-uaMmVsGA_P7R0yYMYmQO4vST0KT-V-yZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه‌های نیویورک‌تایمز و وال‌استریت ژورنال در گزارش‌هایی از بررسی گزینه‌های تازهٔ حمله به ایران در دولت آمریکا و تقویت حضور نظامی این کشور در خاورمیانه خبر داده‌اند.
این گزارش‌ها در حالی منتشر شده‌اند که دونالد ترامپ، رئیس‌جمهور آمریکا، روز پنج‌شنبه ۱۶ مهر اعلام کرد ایالات متحده پیش از انتخابات میان‌دوره‌ای سوم نوامبر به ایران حمله نخواهد کرد.
نیویورک‌تایمز به نقل از مقام‌های آمریکایی گزارش داده است که ارتش ایالات متحده در حال تدارک گزینه‌هایی برای ازسرگیری عملیات رزمی گسترده علیه ایران است و پنتاگون به دستور آقای ترامپ طرح‌هایی را برای حمله به زرادخانه‌های پهپادی و موشکی، تأسیسات انرژی و دیگر مراکز نظامی ایران تدوین کرده است.
به گفتهٔ مقام‌هایی که با این روزنامه گفت‌وگو کرده‌اند، تیم امنیت ملی رئیس‌جمهور آمریکا و پنتاگون در ماه‌های اخیر پنج پیشنهاد برای انجام عملیات‌های بزرگ علیه ایران یا حوثی‌های یمن به او ارائه کرده‌اند، اما آقای ترامپ هر بار این طرح‌ها را رد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78672" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ragSSx-yozvCxy2k9AY-Tki_Cj-y5rKNbRNlpjCyeVuFx4DDqCeCs6aAARHugEkudzWbWUhsRitVvrSRZ_tD6iqmoyZV3LYdU5EABymrnInh-h6XwceUXSGXVmvfqmOQ0DfPz81oojz7m87BYw9lapts4MK1uPCF_28pzvysiZQPchP4c2JgnSpx0WiLO4gY2pQ_my9hLyO4JDe9eR4-9kmZk1QGj1OQXLeQXS_7HnaNS9usPuccDLXinT91g7uQFi4joksPO-7PtbrLruTjtnnGYw5hh1L0kBDFjXpHRS8NDQ3oJlfyDToS3_S697TJ-q0iAph-AcIBJpaL-WtkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت اوپن‌ای‌آی اعلام کرد حساب‌های کاربری مرتبط با یک عملیات نفوذ رسانه‌ای با منشأ ایران را مسدود کرده است؛ عملیاتی که در آن، گردانندگان با استفاده از چت‌جی‌پی‌تی و هویت‌های جعلی روزنامه‌نگاری، نزدیک به ۱۰۰ مقاله درباره جنگ ایران و آمریکا را در حدود ۱۲ رسانه اینترنتی در کشورهای مختلف منتشر یا بازنشر کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78671" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IyW4k1UoMM_Dz09eqAX4DP37FgFjgjf6xhj2ZROmHggKLUXu5aQGuH8nE47q4qdk-wpvlepqeIvvA_BXB35adWI9D23Qi6T-zhTZ4onslzp92JHE2ToMisrutJkJK5Qk4x06gjWB7afqzaz0Wd_aUr3igaKNtSP4hRCcG1qyNHN58wJ55WqNDJfDEzAQ5E5sbDPNMnEd7PjTCVxzSQpRanpqXtVGuNDpw5kUMhjY1rp6--yGx5iWG0nvsYWTUVLrxLiTOkxgYq9IxuWTySRN19cYFEBOCJazzrnYVv9orJOSuuiF93tl4-eyAK4Xx3Po1XtV6lHzpDQBZu3AAwKh8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد واشینگتن احتمالا تا پایان هفته حدود یک میلیارد دلار دارایی رمزارزی مرتبط با جمهوری اسلامی را مصادره خواهد کرد.
بسنت گفت دولت دونالد ترامپ کارزار «فشار حداکثری» علیه جمهوری اسلامی را به کارزار «انزوای کامل» تبدیل کرده است.
به گفته او، این سیاست علاوه بر محدودیت‌های مالی، مسیرهای دریایی، هوایی و زمینی ارتباط ایران با خارج از کشور را نیز در بر می‌گیرد.
وزیر خزانه‌داری آمریکا گفت امارات متحده عربی و عمان در اجرای این سیاست با واشینگتن همکاری می‌کنند و دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن مسیرهای زمینی ورود و خروج از ایران است.
@
VahidOOnLine
اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتقاد از سفرهای خارجی مقام‌های جمهوری اسلامی گفت اعضای سپاه پاسداران دیگر نمی‌توانند برای دیدن «جراح پلاستیک خود در لندن، معشوقه‌هایشان در پاریس و پول‌هایشان در ژنو» به خارج از ایران سفر کنند.
بسنت در ادامه گفت: «اگر جمهوری اسلامی را دوست دارند، حالا همان‌جا گیر افتاده‌اند و می‌توانند از آن لذت ببرند.»
وزیر خزانه‌داری آمریکا گفت سیاست دولت دونالد ترامپ برای منزوی کردن جمهوری اسلامی، فراتر از تحریم‌های مالی است و محدود کردن سفر مقام‌های حکومتی به خارج از کشور نیز بخشی از این برنامه به شمار می‌رود.
او همچنین با استناد به گزارش اخیر نیویورک‌تایمز گفت اقدامات دولت آمریکا باعث ایجاد نگرانی و آشفتگی در میان اعضای سپاه پاسداران شده است.
بسنت افزود اقداماتی که واشینگتن علیه جمهوری اسلامی انجام داده، پیش از این سابقه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78670" target="_blank">📅 16:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a954e7da9.mp4?token=k74O2vZ9iB0tocVVuqKx8NGxUwIlqu_pQvYxmbaA1tUct9j0JFkjdPdXN8uC33gctttxyjxrXGRImW1vLesuAPyFyo3PrGb2EvoxrO1QYWcKm8KocLPg6afa7f2qRDC0-EKyU07AdhtsWZiDsb9VEKf1UPSAbvgP16QcGm017j4iPnOPM0jojiCY1rq4NjQqD1mKb_cOe1ix87EFjf11CMAR1F5c9hxHa8iDCGFH6FxVvZhN14-711qnUyllt6E9Hnm6FFId_X1ilauogaegtJkpI0TpDcCXqdLgDiqgMHPfwxByWtajPR2t2pcoTnHBmFyb6FcuG7qyVx5n7et4LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a954e7da9.mp4?token=k74O2vZ9iB0tocVVuqKx8NGxUwIlqu_pQvYxmbaA1tUct9j0JFkjdPdXN8uC33gctttxyjxrXGRImW1vLesuAPyFyo3PrGb2EvoxrO1QYWcKm8KocLPg6afa7f2qRDC0-EKyU07AdhtsWZiDsb9VEKf1UPSAbvgP16QcGm017j4iPnOPM0jojiCY1rq4NjQqD1mKb_cOe1ix87EFjf11CMAR1F5c9hxHa8iDCGFH6FxVvZhN14-711qnUyllt6E9Hnm6FFId_X1ilauogaegtJkpI0TpDcCXqdLgDiqgMHPfwxByWtajPR2t2pcoTnHBmFyb6FcuG7qyVx5n7et4LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان روز پنج‌شنبه ۸ اکتبر (۱۶ مهر)، با ولادیمیر پوتین، رئیس‌جمهور روسیه، دیدار و گفت‌وگو کرد.
این دیدار در ترکمنستان و در حاشیه دو نشست «کشورهای ساحلی دریای خزر» و «سران کشورهای مستقل مشترک‌المنافع» صورت گرفت.
پوتین در این دیدار خطاب به پزشکیان گفت «ما می‌دانیم که ایران تلاش‌های واقعی برای پایان دادن به این درگیری انجام می‌دهد؛ درگیری‌ای که ایران در آغاز آن هیچ تقصیری ندارد.»
پزشکیان هم در این دیدار به پوتین گفت «هر بار که [با آمریکا] گفت‌وگو می‌کنیم، دوباره حمله می‌کنند، ولی ما از میز مذاکره و گفت‌وگو کنار نخواهیم کشید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78669" target="_blank">📅 16:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KdINlg4dQw9wYrc2nUQxELuGML6e01QDrvatOt3LqVM5Eo6BktDAo92eCR1NeofucnyozazVmVt0W8p57Cf5iDqkvgctMT9-asfltwPyCi2I7ZEfX3obu0j_MJkyyIdLFX0W61XPsNL9iESOzWo0AinS-qJuZ2pOoTDZk7mYA_HraEbHgMXRENLZSwbEgXyJrJp8t0l6zu7AjH4FutvXEl1eQI7eCO-v913rQTSTDHRndX1INqCpPF-QGf48uQ7BaNTU5TkFWwEksoWYre__rL27VgZqccNGYSpmMwE6r1RlC8HVpJ1XPeZqpwVYmD17Xq3-qy2cUfiY7W67_QGv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TNksIDjHEj8ycBL1dXUIgLsPryQUllG1xiVLli7Anq5hKbqdQKub2ZQH7AtIExpJIN0YPu_pLs_2cha9D6eRPtmffvoK8woYVs395-nt5RVlzS9ZLGW21QbLMYk_nk-UuFxzcyRmMDxoU7sZirvhPmPzfITq-xMJSwiUtWDjJ6yADkXoUqbzh0TSsYNxKjf6x766LRbhR2iKrC82H5taejHKkkImZBb-5lN8jYlaAkBqq_ih4BptZ2_ihpzIwnNl1zamf5OdYs_d1WBzZ7uU_UyWCHPuFDmmjg7Di1ZXDhjztsvY39Bv3SdW_wbaC1k0PehlLBV-9oy1L26IVjNsbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی در بیانیه‌ای جمعه ۱۷ مهر اعلام کرد که در پی دو حمله به فرودگاه بین‌المللی ملک خالد ریاض در روز پنجشنبه، سه شهروند این کشور کشته و شماری از شهروندان سعودی و اتباع خارجی زخمی شدند.
بر اساس این گزارش، در حمله نخست، تاسیسات فرودگاه و در حمله دوم، یکی از هواپیماهای شرکت هواپیمایی سعودی هدف قرار گرفت.
این سازمان اعلام کرد پس از این دو حمله، فعالیت فرودگاه از سر گرفته شد و تردد پروازها به حالت عادی بازگشت.
شرکت هواپیمایی سعودی نیز اعلام کرد که یکی از کارکنان این شرکت در میان کشته‌شدگان بوده و یکی از هواپیماهای آن هنگام توقف روی زمین در فرودگاه آسیب دیده است.
سازمان هواپیمایی کشوری عربستان سعودی همچنین اعلام کرد که فعالیت‌های عملیاتی فرودگاه بین‌المللی ملک خالد از سر گرفته شده و تردد هوایی در این فرودگاه به حالت عادی بازگشته است.
@
VahidOOnLine
شرکت هواپیمایی سعودی (السعودیه) اعلام کرد کاپیتان حمود علی الکثامی، خلبان این شرکت، روز پنجشنبه ۱۶ مهر ماه در حادثه فرودگاه بین‌المللی ملک خالد در ریاض جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78667" target="_blank">📅 16:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9A9nTRZMoEyN-kLHoFp-bGR6Y5lesb2VP1iiXX2tqLvTiJTGI3GxACUAIFQcXNjaBXSSiastFOrPGSuvFd2mZpjWqmW4z7sVAweHfmqtYtleslkaQefcS6mvpGSelAp57Zone_3BTyhzbzUJcwRP4czdxxygriIGPvdrSiQPYPfaemCrvvsb-ofJ5EgBCwugBWNCZIHWnufum7Lev1MjLH8-vWTYYBRAcCv6OPQqf4Cb9GRbGCFL_hXVFMBqTsTY0yvWseCAQLM4_scJ5tzI__FsZWTVLNotdTxvYldkCs4vvfUumBZSUgl6_2Th1wdYMZZVL9J6jW1QSGzyMn10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی از کشته شدن رئیس پلیس پیشگیری شهرستان فاریاب در استان کرمان بر اثر تیراندازی افراد مسلح خبر دادند. این حادثه در حالی رخ داده که طی دو روز گذشته چندین حمله مسلحانه دیگر علیه نیروهای نظامی و انتظامی جمهوری اسلامی در مناطق جنوب شرقی ایران گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78666" target="_blank">📅 16:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYOMxMij6VaNEftu2_k_3OpmfX9GsXMGZqetyzqjpWDSuXvfPnU00hso3sKF3hSJzBXIql8KOX_-AhW580Mp4otUPAmVter2w9YBL-v92PLFAzhsLd2mNIt09V1nQ5lp6B2tB5joiSaxnHPW8U_DT_9_GxdHyB4sBOKQsl6XEDe_HGjm2Uz8WqAsoMv1xBjA3-weFjTs1vHVJHEJ-Kg9qKjAzqwboQAem0BVK42BfmRP9NQGVOC0_LnhJ9kygwrJUz5kg9mNktj_9sL8NUvv9pAj4QXBWLPj8cwmw6rxhYw66jTRQhSPjo-CK9h8ZaVCgcyQqEPdJ4E5YE0BVLmdSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترانه و رومینا رحیمی، دو خواهر بازداشت‌شده در جریان اعتراضات دی‌ماه ۱۴۰۴ و از متهمان پرونده موسوم به «میدان شهدای اصفهان»، در زندان دولت‌آباد این شهر به سر می‌برند.
ترانه رحیمی در مرحله بدوی به اعدام و ۱۱ سال حبس و رومینا رحیمی به ۳۶ سال حبس محکوم شده‌اند. وکلای آنان به این احکام در دیوان عالی کشور اعتراض کرده‌اند.
#ترانه_رحیمی
#رومینا_رحیمی
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78665" target="_blank">📅 16:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78664">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h83Sv-0FCKZhT5XllueAVE9W6w2tWM99ad61-o4i-yZzWuteRHgUZcpdTLCA8kUKSjAR78nWKM765OGZA_gaLd_D6gdORcRuxk51SUFrLEULXdZdzgYg4f2F8aAK1dGd6wjjQoqtrkL43b3051ybBJbtgQpvK109rB0q-FRTRIvRjq1j18rfAfZq1hSFHn7bPq8qAMgwljObuc3q_b3j1Q3PX72wapxXlDxRpr-XHx1ir28CWQoL_e0T5v2u79YWQtWJzVFYOtDOMU7BGACgDtTifM4qr_bdf8BRHwmpK9-0xvAiNtG_bpjqN_FE6XYTfMxCphuhu2bWDTCN8idZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رسانه‌های جعلی و ساختگی دارند تلاش می‌کنند این‌طور وانمود کنند که من از دشمن دعوت می‌کنم سن‌دیگو و لس‌آنجلس را بمباران کند، در حالی که آنچه واقعاً درباره‌اش صحبت می‌کردم این بود که افزایش موقت قیمت بنزین، بهای ناچیزی است که باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای پرداخت کرد. و اگر می‌خواهید بدانید بهای سنگین واقعی چیست، می‌توانید تصور کنید اگر آن‌ها سن‌دیگو و/یا لس‌آنجلس را بمباران کنند، چه اتفاقی خواهد افتاد؟
تنها کاری که من کردم، مقایسه پرداخت مبلغی کمی بیشتر برای بنزین، آن هم برای مدتی کوتاه، با بمباران شهرهای بزرگ ما بود.
همه این را می‌دانستند، رسانه‌های جعلی هم می‌دانستند، اما همچنان بیرون می‌آیند و می‌گویند که من از دشمن می‌خواهم دو شهری را که عاشقشان هستم بمباران کند.
«حرف‌های من کاملاً روشن است، اما این‌ها آدم‌های پستی هستند و فکر می‌کنند می‌توانند مدام اخبار جعلی منتشر کنند و قسر در بروند!»
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78664" target="_blank">📅 23:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dfqSsfYtPS78XGIQxQqVBtzuigzYxv6JUdg_mEgzeTpaO7S-zqGMwQGf0ckYwMg4zxzMM44UTWTTxypAdMSCfHDvYu4d03ixvL2uaRa6_txWSlliQkoI2wmbQnpfCrGeHkSJJdaB7_EeWZVNStyopHt6xeFQHzui268osXovteMuu_KXfObWP5nGCjAqZ52gS3Aqabd85a0mREGMJM05nVoqMveGeQW5E2DfFX2BNxfZhk76LFVZDgZIZEuQR9IFQlRYZ-I1Fp2hWAilnEgVh_xcLk3YKPmEoMeiHvaOiEVGhxF6c_6lPdU3PM6RMmyvPdAPzKketZ0fES5UasbkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات در جریان است، پیش از انتخابات حمله نمی‌کنیم
ترجمه ماشین:
ما در حال انجام گفت‌وگوهای سازنده‌ای با جمهوری اسلامی ایران هستیم. می‌خواهم برای همه روشن کنم که اگرچه ایران هم از نظر اقتصادی و هم از نظر نظامی در وضعیت بسیار بدی قرار دارد و اگرچه محاصره همچنان با تمام قدرت برقرار خواهد ماند، در حالی که نفت با حجم بی‌سابقه‌ای از تنگه هرمز عبور می‌کند (تنها دیشب ۲۲ میلیون بشکه، بدون اینکه حتی یک بشکه از ایران آمده باشد یا به مقصد ایران برود!)، ما تا پیش از انتخابات میان‌دوره‌ای که قرار است روز ۳ نوامبر در ایالات متحده برگزار شود، در هیچ زمانی به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!
پرزیدنت دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78663" target="_blank">📅 20:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78662">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b534ce975d.mp4?token=oO0uPIdQXQy0-HEZ2JKK4Wo-uPdLhaM5ZsXhQoxOm2S0b52K1yu8Kzl4TYfXM1Np_aI2Uumova4Zkk03R4l-k2tABKIHsY1oKul_FVYrcEKbqtUWd3sPn-wmzf_Th4OxYd6FJnDiCZl2pW2JAacNSvHscvyGQ1OfsDSJEoL0dLhwKxBF81oZNo87AzsK5VS4vfk1TEQ0BEsFeVy7aLY4w7ijo9dbi9rI6PJrsTxwN4jw9ob_ZTTwDeoq_3Y0wrN8A56KpGL4iBz2cW6ngWXxd0ocOpEOejhNwh-JJdX1iEJ0jBbPam4IVnr3cqlaUeVEbESAMhlrN_FOtrcO9yZz4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b534ce975d.mp4?token=oO0uPIdQXQy0-HEZ2JKK4Wo-uPdLhaM5ZsXhQoxOm2S0b52K1yu8Kzl4TYfXM1Np_aI2Uumova4Zkk03R4l-k2tABKIHsY1oKul_FVYrcEKbqtUWd3sPn-wmzf_Th4OxYd6FJnDiCZl2pW2JAacNSvHscvyGQ1OfsDSJEoL0dLhwKxBF81oZNo87AzsK5VS4vfk1TEQ0BEsFeVy7aLY4w7ijo9dbi9rI6PJrsTxwN4jw9ob_ZTTwDeoq_3Y0wrN8A56KpGL4iBz2cW6ngWXxd0ocOpEOejhNwh-JJdX1iEJ0jBbPam4IVnr3cqlaUeVEbESAMhlrN_FOtrcO9yZz4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ گفت: «من باید در مورد ایران اقدام می‌کردم، چون آنها به سلاح هسته‌ای دست پیدا می‌کردند و آن وقت می‌فهمیدید مشکل یعنی چه.»
رئیس‌جمهوری آمریکا در ادامه با اشاره به احتمال حمله موشکی ایران به شهرهای آمریکا گفت: «ببینیم اگر آنها روزی به لس‌آنجلس یا سن‌دیگو حمله می‌کردند، چه اتفاقی می‌افتاد. این دو شهر به دلیل موقعیت جغرافیایی‌شان بیشتر مطرح هستند و منظور من حمله موشکی است.»
ترامپ افزود: «اگر چنین اتفاقی می‌افتاد، وحشتناک بود. بگذارید لس‌آنجلس یا شهری مانند سن‌دیگو را هدف قرار دهند. بگذارید یکی از شهرهای بزرگ ما را هدف حمله قرار دهند. آن وقت است که می‌فهمید مشکل واقعی چیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78662" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78661">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoVNWoG3MAuERn_y974WCr6YEx5XbvedUi5HEUvLRqchKhAZAdx4IIAiHN1TY21uW_qiPxwot8DyVX3fATIOcmNolJsNXIbzEbPrgwXFzCHJVQ4uFMgOKzsYBYV8ZGhALvmHDdMTbmOt4JFdu6j7rxTZ4PX579pW-rk0SLLDJNRM47j1Lj5lPPfP6Azr0UpkH8Tk9xzo59au12W_uKxfViWJwF_-fI4CM_fzwsQ3FP_I1TaVq6UQ5DljOW38GNsuRmKZ2PYORJyOVjlCFQ26EqktquO2HpztxIiywGPOC--WnH38IdRQ-TE5HWJGrvy6ah6lsT0FlKvKx2zWMJpSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز پنج‌شنبه ۱۶ مهر گزارش داد شرکت هواپیمایی لوفت‌هانزای آلمان پروازهای خود به ریاض را تا ۲۴ مهر و ایر ایندیا پروازهای خود به مقصد و از مبدا پایتخت عربستان سعودی را تا ۱۸ مهر لغو کرده‌اند.
این تصمیم همزمان با تشدید حملات حوثی‌های یمن مورد حمایت جمهوری اسلامی به فرودگاه‌ها و زیرساخت‌های عربستان سعودی اعلام شد.
حوثی‌ها اعلام کردند فرودگاه بین‌المللی ملک خالد در ریاض را با موشک بالستیک هدف قرار داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78661" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gs208x7_noVJt76zFkDu5Q9CCiZZFX7JfO6d6g3kEvZQq5IHqMpQ_CEUuVONmbPS68I5J8Yapnh2UTGPBiJZ2cX4V2Gtw1DJzssI62fUqS8ZjsZAeOc5TmdOofvTVxQcYyMleZUqD8WPpppyKyYG7OQ8h3oy_6uWj4yO41oPVCvCSlA0efyob3elnfCO67pVh1xHZtO5ezztNMQM9dbiGAHNLbdM_9ocsl_Xo0ApZ3XhFnUdEe3dkadut8yppiOcA5yq9QH0lH9Mpp2lGn9djFBgDhm1ZpGJbJQ4oq9d5nsYeoYNK0-A9mxtwxNLtVOZU_p-_FWRXmtYwkv0ERFk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارگارت همیلتون، دانشمند آمریکایی و از پیشگامان مهندسی نرم‌افزار که نقش مهمی در فرود نخستین فضانوردان آمریکایی بر سطح ماه داشت، در ۹۰ سالگی درگذشت. او رهبری گروهی از متخصصان را بر عهده داشت که نرم‌افزارهای مورد استفاده در ماموریت‌های فضایی آپولوی ناسا را طراحی و توسعه دادند.
موسسه فناوری ماساچوست (MIT) با تایید درگذشت همیلتون اعلام کرد که او روز چهارشنبه هشتم مهرماه ۱۴۰۵، برابر با ۳۰ سپتامبر ۲۰۲۶، از دنیا رفته است. این موسسه در بیانیه‌ای، همیلتون را از پیشگامان علوم کامپیوتر توصیف کرد که پیش از فراگیر شدن حرفه مهندسی نرم‌افزار، در توسعه این حوزه نقش مهمی داشت.
همیلتون از سال ۱۹۵۹ تا اواسط دهه ۱۹۷۰ در موسسه فناوری ماساچوست فعالیت می‌کرد و مدیریت بخش مهندسی نرم‌افزار را بر عهده داشت. گروه تحت مدیریت او نرم‌افزارهای هدایت و کنترل فضاپیمای آپولو ۱۱ را طراحی کرد که در فرود تاریخی نیل آرمسترانگ و باز آلدرین بر ماه در سال ۱۹۶۹ نقش تعیین‌کننده‌ای داشتند.
در جریان این ماموریت، رایانه فضاپیما لحظاتی پیش از فرود با مشکل پردازش بیش از ظرفیت روبه‌رو شد، اما نرم‌افزار طراحی‌شده توسط گروه همیلتون توانست با اولویت‌بندی وظایف، عملیات فرود را ادامه دهد.
باراک اوباما، رئیس‌جمهوری پیشین آمریکا، در سال ۲۰۱۶ به پاس دستاوردهای علمی همیلتون و نقش او در پیشرفت فناوری فضایی، نشان آزادی ریاست‌جمهوری را به او اهدا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78660" target="_blank">📅 19:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwVAJYjgzxXZ0ZD-jkaNVyeSqDwRITc8nUqlmr16oolC7_dZFb7-1zmdNz7i2FNYk1tajBJYYjPHNNaXy-84cS7mbwGDjcpP-vqPzVeCJ8zdGtEuI0GNGQHXq0Bn0SyW4NSvLsmb5jkhH-ZayRCojhyfv2TVrljUl1_19hsVxHcKKjtHwoFGtnltA7hcUeH4JPeZqhckdDnZNSsPUFRCSzUNAugO8x67vi347Z8UnZTJf89KwT8h3jVbir0RaXNHFU4j4fSUeyUs14SO4cKI8co9ivYjtayF6IGOlgIepBQJq9nqpeHJhF4GB0GLchMtAj-PNAaeGuXbIVOsEVTGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی در چارچوب طرحی به ارزش حدود ۲۱ میلیارد دلار، توسعه میدان نفتی مرجان را برای افزایش ظرفیت تولید نفت و فرآوری گاز دنبال می‌کند؛ میدانی مشترک با ایران که بخش ایرانی آن «فروزان» نام دارد. براساس گزارش مرکز داده‌های باز ایران، عربستان روزانه حدود ۷۳ میلیون مترمکعب گاز از این میدان برداشت می‌کند، در حالی که ایران از بخش خود گازی تولید نمی‌کند.
در تازه‌ترین مرحله توسعه مرجان، شرکت نفت عربستان، آرامکو، قراردادی با شرکت آمریکایی «کی‌بی‌آر» برای نوسازی تاسیسات این میدان امضا کرده است. کی‌بی‌آر روز سه‌شنبه ۱۴ مهر ۱۴۰۵ اعلام کرد خدمات مهندسی و اجرای پروژه را برای تاسیسات فرآوری، فشرده‌سازی گاز و زیرساخت‌های برق مرجان ارائه خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78659" target="_blank">📅 15:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78658">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut_PCXcjYoTI0YX2FJnREjRuZz09ufAteA95o7eJENLev6Jtuo8nw6tH0T-hsCqQOskvcU5DJe9hWm5agRBwcnK3I8lDhyIWKotMKQXumDmuMuaTYiX1FXBQyGaIOratxwA_cvtaJhg4nkgfgcknrPUBVMMje4VG674JVweGK0Cooz2keEmVRxyKL_9KXT_ZGBXKQj9QQETqQEhE0VSN5b-9PzC_EAY1LyE3G8-U_7XrjrvaS1ASNNVd7VinZOZwdWR6UUvFFMa8HZwNgmc9Zr9kjWbNBDr2-wfRPIV05e53NkckEmieQWcTws6L84yqD-aSI0-YgSB6Zw3sewfD6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز، روز پنجشنبه ۱۶ مهر ماه، گزارش داد شمار کشتی‌هایی که از تنگه هرمز عبور می‌کنند، پس از افزایش حملات به نفتکش‌ها در هفته گذشته، به پایین‌ترین سطح در بیش از دو ماه گذشته رسیده است.
رویترز بر اساس داده‌ها و تحلیل‌های شرکت تحلیل کپلر گزارش کرد، روز سه‌شنبه فقط ۷ کشتی تجاری از تنگه هرمز عبور کردند که پایین‌ترین رقم از اول مردادماه تاکنون محسوب می‌شود.
عبور نفت خام از این تنگه نیز با کاهش ۲۷ درصدی نسبت به بالاترین سطح زمان جنگ در هفته قبل، به دست‌کم ۱۰.۱ میلیون بشکه در روز رسید که معادل ۷۴ درصد سطح پیش از جنگ است.
به گفته تحلیلگران کپلر، بخش عمده این کاهش به انتقال محموله‌ها از کشتی به کشتی در دریای عمان مربوط می‌شود.
به گزارش رویترز، با این حال، صادرات از سواحل دریای عمان و دریای سرخ به ۶.۷ میلیون بشکه در روز افزایش یافت، رقمی بیش از دو برابر سطح پیش از جنگ که به جبران کاهش عرضه از طریق تنگه هرمز کمک کرد.
داده‌های کپلر نشان می‌دهد تعداد کشتی‌های عبوری روز چهارشنبه به ۱۰ عدد افزایش یافت، اما همچنان بسیار کمتر از بیش از ۲۰ کشتی در روزهای یکشنبه و دوشنبه بود.
این گزارش پس از آن منتشر می‌شود که حملات به نفتکش‌های عبوری از تنگه هرمز در هفته گذشته به بالاترین میزان هفتگی از زمان آغاز جنگ ایران رسید. پیش از آغاز جنگ در نهم اسفند سال گذشته، روزانه حدود ۱۲۵ کشتی تجاری بزرگ شامل نفتکش‌ها، کشتی‌های حامل گاز، کشتی‌های فله‌بر و کشتی‌های کانتینری از تنگه هرمز عبور می‌کردند.
همزمان، دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنحشنبه نموداری در شبکه اجتماعی تروث سوشال منتشر کرد که نشان می‌دهد سطح تردد نفت از تنگه هرمز به میزان پیش از جنگ آمریکا و اسرائیل علیه ایران بازگشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78658" target="_blank">📅 15:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78657">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSKO8SCe02LC9JAVCeOQVOMa9CqhSQSozYpT5aDxvz6DZuOdPjOoZhnsBgSk-IqHalUChRWdxRN3sQUJqenX2P0DqBUdhfuzOHfC5WlBCJMreZvKlAQn6K7SXK6YYmKC0vwSKB5kia1JNFpd21vw9PgKNrt825zVtu1skxKWfHkdtTk0jjRey9RtC5L5Dszfgr-rp5b1BFyT3xKQ-ErR1ly8PhFPJGtPD5dhlLnKog0Qlhs-y5dSQ1wvBEOd7cHaxvpOZgYD4bCSTrdqFXpSbVmKPVk9hU38Ckdeo2O4Ug9mRlSVxxS4EAqTXOYLMzTekYaQRugfjZBQPrS80UL5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی حمله افراد مسلح ناشناس به ستاد فرماندهی انتظامی شهرستان گلشن در سیستان‌وبلوچستان، نیروی انتظامی وقوع انفجار و تیراندازی در این منطقه را تایید کرد. هم‌زمان، ارتش جمهوری اسلامی از کشته‌شدن یک نفر و زخمی‌شدن سه نفر دیگر در حمله‌ای جداگانه به مینی‌بوس حامل کارکنان ارتش در زاهدان خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/78657" target="_blank">📅 15:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HBOfNQ3L2-q0ar2_IcOS5pjp26OdOhtZygmU4I6_uc309scof2_lftdQ_dAsSVHg8ryY_A3ltZyX8J6_0b0vOPoHaw05VgBw1_P_iwNw8e71pwiwaCNPRvw303-RYcbLlMIGTK0RCQI_aH8zii2w7Ac21unVL3-yDDM6wEu0GSULBRCJqE6PfuWVPiev_NbPkH7chfewe5Ku0T-4RKcnq1UM4VZkL-Fl1cZo8jxEMNsc9lZ2dZn6uxaTyVX40j_cjAN31XIyKx1ki7vmTT4SGfCBo2hrcps8lM-mporLbhnxmCND_Y0IQE7hgPQm5UGNbhaZH0zO__vrllUIMjO4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز
پنج‌شنبه ۱۶ مهر در گزارشی تحقیقی بر اساس گفت‌وگو با بیش از ۷۵ کارشناس حقوق بشر، وکیل و شهروند ایرانی نوشت ایران پس از اعتراضات دی‌ماه شاهد شدیدترین سرکوب چند دهه اخیر از سوی جمهوری اسلامی است.
به نوشته رویترز، دستگاه‌های امنیتی و قضایی جمهوری اسلامی با همکاری صداوسیمای حکومتی، از طریق اعدام‌های شتاب‌زده، محاکمه‌های غیرعلنی، پیگردهای قضایی گسترده و انتشار اعترافات اجباری، در پی ایجاد فضای ترس و خاموش کردن مخالفان هستند.
بر اساس این گزارش، از ۲۸ اسفند ۱۴۰۴ تاکنون دست‌کم ۳۴ نفر از افرادی که در ارتباط با اعتراضات دی‌ماه بازداشت شده بودند، اعدام شده‌اند. پنج نفر از آن‌ها تنها در ۱۰ روز گذشته اعدام شدند. در مقابل، طی چهار سال پس از اعتراضات ۱۴۰۱، در مجموع ۱۵ نفر در ارتباط با آن اعتراضات اعدام شدند.
رویترز همچنین گزارش داد مقام‌های امنیتی ارمنستان در ماه مه به گروهی از معترضان ایرانی درباره تهدیدهای جدی علیه جانشان هشدار دادند و از آن‌ها خواستند برای حفظ امنیت خود و خانواده‌هایشان این کشور را ترک کنند.
اشکان، معترض ایرانی ۳۰ ساله که در جلسه با مقام‌های امنیتی ارمنستان حضور داشت، گفت به آن‌ها هشدار داده شد افرادی احتمالا برای ربودن، ترور یا آسیب رساندن به آن‌ها اعزام شده‌اند. رویترز نوشت روایت او را با گفته‌های معترض دیگری که در همان جلسه حضور داشت و فایل صوتی آن جلسه تطبیق داده است.
رویترز همچنین نوشت نهادهای امنیتی جمهوری اسلامی با تهدید خانواده‌های مخالفان ساکن خارج از کشور در داخل ایران، لغو گذرنامه‌ها و خودداری از ارائه خدمات کنسولی، فشار بر منتقدان را به خارج از مرزهای ایران گسترش داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78656" target="_blank">📅 15:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qttAIm0wLDX-nIKL7BoTcODyOsx6MvsXJpvFpLNKAwVvBZMb7jScvrZxqCTSiZAR7bPROBY-ksbm6rz39XimxGCQgFLneW_yzy5WVKTxCNhK3CFOT_PFAFIIkeKcGfFh64ynRaGNpGNshXuWAEMxtRibFanqF_OZlY3loza1jz0dDHdOWBrT4CKtPnwwMCbXWp3tBh6Cd1jovAMYxToyZn709-RX5z9XZB5ONpwRUSefRL0DDWA0Wm0R_rwrsczVUI5_w_Bj9vnf0nl4feb--9iwhX7GnIjA72Tt_exj5fVZ_nBJuA_zpzf-ScizSRIcCZ_RnxaI6Mf1Hr7kn93NZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، بامداد پنجشنبه ۱۶ مهر در سخنرانی در ایالت تگزاس درباره جنگ با ایران گفت این جنگ «خیلی زود» پایان خواهد یافت و ایران را «کشوری شکست‌خورده» توصیف کرد.
ترامپ گفت: «وقتی این جنگ تمام شود که خیلی زود خواهد بود، آن‌ها یک کشور شکست‌خورده‌اند، کمی رمق برایشان مانده، اما نه زیاد.»
او همچنین با اشاره به نفت عبوری از تنگه هرمز گفت این نفت در سراسر جهان توزیع می‌شود و بار دیگر بر نقش آمریکا در انتقال نفت از این مسیر تاکید کرد.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا در جریان یک گردهمایی انتخاباتی در تگزاس گفت «ما به زودی از ایران خارج می‌شویم و قیمت نفت هم مثل سنگ پایین می‌آید.»
او گفت افزایش بهای نفت ارزش جلوگیری از دستیابی ایران به سلاح هسته‌ای را دارد.
رئیس‌جمهور آمریکا همچنین در مورد احتمال دستیابی به یک توافق با ایران گفت: فکر می‌کنم این توافق واقعاً چیزی است که می‌خواهم انجام دهم، اما آیا آن‌ها حاضرند برای متوقف کردن برنامه هسته‌ایشان چیزی به ما پیشنهاد دهند؟ و ما قطعاً هرگز اجازه نخواهیم داد ایران سلاح هسته‌ای داشته باشد.
آقای ترامپ همچنین با تکرار سخنان جنجالی چند روز گذشته‌اش در مورد حمله فرضی ایران به لس‌انجلس و سن‌دیگو گفت: «همین چند روز پیش گفتم: بگذارید موشکی به سن‌دیگو یا لس‌آنجلس اصابت کند... بگذارید به سن‌دیگو یا لس‌آنجلس حمله کنند تا شاهد اتفاقات ناگوار باشید... ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما از شهرهایمان محافظت می‌کنیم. ما از کشورمان محافظت می‌کنیم. ما اجازه نمی‌دهیم چنین چیزی رخ دهد.»
این سومین سفر دونالد ترامپ در طول یک ماه گذشته به تگزاس برای تبلیغ نامزدهای جمهوری‌خواه محسوب می‌شود؛ نامزدهایی که در تلاش برای حفظ کنترل کنگره، اکنون با رقابت‌های انتخاباتی میان‌دوره‌ایِ به‌طور غیرمنتظره‌ای فشرده روبرو هستند.
ترامپ در ورزشگاهی مملو از جمعیت در سن‌آنتونیو سخنرانی کرد تا از کن پکستون، نامزد جمهوری‌خواه سنا در این ایالت حمایت کند که در رقابتی تنگاتنگ با جیمز تالاریکو، رقیب دموکرات خود، قرار دارد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78655" target="_blank">📅 05:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pn6DcXpg8sRXfOdh2hPXozdOt95KKITdmUZk0EBVNsCjr_8TcxBS_ihFiUax3hQo8P0zurAdpbyE74h4P9j7cDB8XjBw6PAGMyadoO8jR1ce4zS5NDBUDjUgZvhO1awKNjESmKmI0zW-GVn9ZoSmUtOVsxgxZ727hXLi61XA3rLv_yBNsyYTEcEX9EVD_wT4ZEntNJhLlzbCQH4k71iY62xXneCaXvaSGmPP1PBs23WKZ_SjDII8I92oLOWbKG8stWKEhSeze29j229gaMXMU1lflUY2wlNa1N0N9KuZY1soTle8BxKmrAfQfTV6VEu0SYvEqt72E6AfpbA6wZjucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رسانه آمریکایی گزارش کرده‌اند که پنتاگون برای حمله احتمالی مجدد به ایران طی روزهای آتی آماده می‌شود.
سایت خبری اکسیوس به نقل از مقام‌های آمریکایی گزارش کرده طی روزهای اخیر پنتاگون با صدور دستورالعملی از سنتکام (فرماندهی مرکزی آمریکا در منطقه خاورمیانه) خواسته روند آمادگی خود را برای از سرگیری عملیات رزمی عمده علیه ایران تکمیل کند.
همچنین مجله آتلانتیک هم در گزارشی اختصاصی به نقل از دو مقام آمریکایی نوشته کاخ سفید از پنتاگون خواسته است تا گزینه‌هایی برای حمله به اهداف ایرانی تدوین کند که امکان اجرای آن‌ها پیش از انتخابات میان‌دوره‌ای وجود داشته باشد.
به گزارش آتلانتیک، دونالد ترامپ مشتاق است پیش از انتخابات، قیمت بنزین را کاهش دهد و به پیشرفتی عمده در مناقشه با ایران برسد.
به گزارش اکسیوس، دستورالعمل پنتاگون شامل تاریخ مشخصی برای آغاز حملات نبود و دونالد ترامپ هنوز تصمیم نهایی را اتخاذ نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78654" target="_blank">📅 05:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnkrVLmjtyZEt36OjQCsgmFLpQn7wnYD_ekF-VUKPJI1zQMgca-IrE-2IM4kNzSC6z74A5f53DGhXHxCgxkNvQnLqfZ2XYzaxGXaOEbpwK3U0EnzR7VGy4q2bj8hzddcS-xthlE2jf9IpCCb2pxFeHqmvE8NSNzKcwwLE4mWvE0TEDL0MiOWeNcE4QoqxpYzUGJ_Ejvk-eg_L8z1xCd1cnFHhQvfm6X_codbLzysLtNV7i7t9lXA3r844oyGpLfrmMLzo6Cn8bG2LH5zNhFPol-02Gz4LvmFzsdFK47OOWcWFgp532hI2741IRb-DORcbLtMcP2w9YFDEBzVtWQ3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ارتش آمریکا، سنتکام، بامداد پنجشنبه ۱۶ مهر با انتشار پیامی در اکس، اظهارات یکی از فرماندهان سپاه پاسداران درباره بسته بودن تنگه هرمز و کنترل کامل ایران بر آن را «نادرست» خواند.
سنتکام اعلام کرد تردد کشتی‌های حامل کالاهای تجاری و محموله‌های انرژی، از جمله ۲۰ میلیون بشکه نفت خام، در تنگه هرمز جریان دارد و افزود: «ایالات متحده و شرکای منطقه‌ای به‌وضوح کنترل تنگه را در اختیار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78653" target="_blank">📅 02:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OkQeA3hjMNqpJgy83WyO9a3cKD-yeqDWOmTzql31NfcemZlba47XP6DG9w2zc6K9bhdxRI9wo7Wk6MNo48Hmhorpt8vzfTisku9rg9ModVFBQ-aeMIKK9EQYxmZiK4Xicceatays4W7NifKUR2b16APJHU8pcZK1CV9_A6RcwBJohyVRu8RxsU7SQLBFYXmOp5VCHspXN7_mr1KrZet0pNeut3g4GtEiuXinlUu8VFnqEr7SyCN1YOqDiA0aR4qCVRVlzPfMUWh2zma_VVVnfIfEUugUmiRtYQEJTyW2Lcjyuz5Ppy9nM9U2y-jGSp3oWMCyA3UEd2snE0paNeu1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات تجارت دریایی بریتانیا: در حمله به یک نفتکش در شمال قطر خسارت جانی گزارش شده است
سازمان عملیات تجارت دریایی بریتانیا شامگاه چهارشنبه ۱۵ مهر اعلام کرد یک نفتکش در آب‌های شمال قطر، در ۵۱ مایلی مدینه‌الشمال، با چند پرتابه هدف قرار گرفت.
بر اساس اعلام این سازمان، در این حمله تلفات جانی گزارش شده، اما هنوز جزییاتی درباره شمار کشته‌ها یا مجروحان منتشر نشده است. مقام‌ها در حال بررسی حادثه‌اند و از کشتی‌های منطقه خواسته شده با احتیاط تردد کرده و هرگونه فعالیت مشکوک را گزارش کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78652" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCrOmhl3vjaYJk5lVhbRfR2PbOV6jWQMqf8RERVCWy1VTmVGxIxI2oDqVQz1LOaeQQkHKsFmgHRgU6zlN12OVBEK-4y3jlWkPSHwROky3YKr_qUVOKTUXcrqTQVHJZxpxXIvJ4l14datKpB_IxGp13mni_DoP2Bafv6npgWYG53DzyT0-qpKL-qGnXy0mOprW4Fyaa6ttDMHn-Eb-_8hT5u2PqQr24iZ4iuprT1VGkF1pWZyxmT0HkdrQZZbnp4bHjPXQ55kKXOhhEIkuLw4Z7C9ebG08KALmqBF0QasXqHMR6sM1rpdzUW6beKqO2AwKjCIXjlNoAAl8F8l_wXusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع مطلع به خبرگزاری رویترز گفته‌اند جمهوری اسلامی ماه گذشته ۲۰۰ میلیون دلار در اختیار حزب‌الله لبنان قرار داده است تا این گروه به خانواده‌های لبنانی آواره‌شده در جنگ امسال با اسراییل کمک مالی کند.
بر اساس اطلاعات منابع رویترز، حزب‌الله قصد دارد در مرحله نخست به هر خانواده حدود سه هزار دلار کمک کند. اولویت با خانواده‌هایی خواهد بود که روستاهایشان ویران شده یا به دلیل حضور نیروهای اسراییلی در مناطق جنوبی لبنان امکان بازگشت به محل زندگی خود را ندارند.
یکی از منابع شمار این خانواده‌ها را حدود ۵۰ هزار خانواده اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78651" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T04OFIb0yloE04augdZNzTOZZYMyxWFzn8d5juHZWgDCyc_uX8rwJ7KGrqnbCJfojav7e3d8F7dGxqfROsSrkC7o_AX0fY97L0aPEGDXKhYkqBnjnY5LeoKAklpastheKETCxrxVNkp4mvbXnwVGXAlofbbxC5HsA4DRh5p5iC7EYwq9jEZc4PTfN9IoRgL3UUG_zcoD0h-V1XKhmskC2t5vUJxgX_lGlI7iIOPzSJ6SdiUnx-KrtQokEmZPy0fVHnN49TC6EyC-LkKRPOmMkmDrRDuwSAkZ44DJMTXI6lG353uiJ9H4tewjuKwFUBWB7ZOtrUfCxPxdOec9DiXKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهاره آقایی، وکیل دادگستری محبوس در زندان قرچک ورامین، به ۲۰ سال حبس محکوم شده است.
کانال تلگرامی شیرین عبادی
با اعلام این خبر، حمایت از معترضان دی‌ماه، حضور در مراسم چهلم سپهر شکری و کمک حقوقی به خانواده‌های دادخواه را از موارد مطرح‌شده در پرونده او عنوان کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78650" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVsMkgLV6Yo__zNpJ3hhvaX2eoz3SETLZQh67YvCsBt0gqguRTIJF0io7ZtjDZwyaP1YwWAz5987g0B0aVn9lLqCgJjJZJJ5T3W77DAqXpYSwv3WSCnWet9OEh4wiUP94Gn_arBj0g_fus5ctaK3tnzJTUw0eIWqPA_g2wRu8g241Icxr7gQ4exz9VPy3hPy1looZ4UR-swTmPMAT7HpEdL3JN9H38tAXp_D2aKvjYlaLTHfNsHnGYMMDh3INhQ3EnXC28MilzKf5tJePOQR_JK_to7LO3p-iruFCEqrFdtnXhTbpYLPXUeY0JMRvp-x7-hboGEVREQ7Fj1wtxARoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده آمریکا، با انتشار پیامی در اکس و با لحنی کنایه‌آمیز نسبت به استعفای محسن پاک‌نژاد، وزیر نفت ایران نوشت: «ایران وزیر نفت جدیدی دارد. با توجه به اینکه از ۲۵ اوت تاکنون حتی یک بشکه نفت خام نیز توسط ایران بر روی هیچ شناوری بارگیری نشده است، این وزیر نفت دقیقا چه چیزی را مدیریت می‌کند؟» پیش از این، مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر ریاست جمهوری ایران اعلام کرد، پزشکیان پس از موافقیت با استعفای وزیر نفت، طی حکمی حمید بورد، مدیرعامل شرکت ملی نفت ایران را به عنوان سرپرست وزارت نفت منصوب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78649" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STmjYu_MIn85dlQ17f9J0fDmwjLmBrHRYzmV0QoEKXn5LtO3K7650DpZou-DDhN0ZaMvGZFIn_2VlK_E-x88jj2kolES9y9zbWHukgJVgqn9tl9__Qout9EsLu-xiIwCVvw8hvRSOw575T4ZFK9w0NtQSVhUX_qoicjnHY0T3y5mKto3w7RsKSQivc4zQ2_d7YcT9OKOs9GmStWeAc3jDbaVE7sLyGzbWtmXIU-q2puHZIQRU4hoI83aa6B3PsgZ30XU-GG4uJ1FrAhdphDyCDAB7AmsvheSCZUw-z8L-EGWrXQtWkTfi0aOcyhrOOwVRG__vKnINUb_OUItF4qymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام امید گودرزوند چگینی، معترض ۳۷ ساله، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ و محبوس در زندان چوبیندر قزوین، در مرحله تجدیدنظر تایید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78648" target="_blank">📅 17:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bJCQO8SKTJCxn-NPa3nkPcwYABfUJ5ax4cYaCytMlGpuUtQJWP6UI8L-HfDB9YSqaPO95wmljTyY26A9rKqZYXZWM4q6OaAJziPcZd4M9u2bJ7zgP-LKD7olnv_g7U2G0KWjRqOn7LiDAxrwgc5Q42KjUn6bYw4JbYLWnqGqzLtqf5Rsr-eNOqqxnMwL28jxgkiOnKaU9mlkyz27m3EZOAs9TTd8PkuNU9-kvj48r2ZyGA1cgKDmYkAarhJ20lU4UGezqOjJx2xi1J6uWWJNVHtWF4zCBEWJ2kIZAJ5LwcXC01t34TljRgkCcFTrX5Ygt6FQ7AH6A7PblCoCdLSRFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20e0cac582.mp4?token=f0j-HNvA55vNOGfUBg-6AOFbqHIeWogMc8Dof7cv0t15K1b6-6Vz-cvE09faj6NA8b9z1AlJ46L-VniJy97f39ul3wspv5dN5cnM9RCUqECBtt56xM-dj7G26HNiYhaOnESe9tevF4BB5gv2PypPXqmiPoznvZFNvchDC4UhOz93wcbihTfLJDyQbOysNkPRQawdKJA9jN13prGSSmc_qAq97XpOpMp-6vbHjw1TbEIIkU6L7lCVOi8-R_pv4J36cwS3VeBbjlYAz0Cn3rVbS26V6m5dSrqcLL6R7k_yURo0Nw8oO0ZYwTaKmTLnAghWhwhD5ZZWBlyTt_rHKzUjgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20e0cac582.mp4?token=f0j-HNvA55vNOGfUBg-6AOFbqHIeWogMc8Dof7cv0t15K1b6-6Vz-cvE09faj6NA8b9z1AlJ46L-VniJy97f39ul3wspv5dN5cnM9RCUqECBtt56xM-dj7G26HNiYhaOnESe9tevF4BB5gv2PypPXqmiPoznvZFNvchDC4UhOz93wcbihTfLJDyQbOysNkPRQawdKJA9jN13prGSSmc_qAq97XpOpMp-6vbHjw1TbEIIkU6L7lCVOi8-R_pv4J36cwS3VeBbjlYAz0Cn3rVbS26V6m5dSrqcLL6R7k_yURo0Nw8oO0ZYwTaKmTLnAghWhwhD5ZZWBlyTt_rHKzUjgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید ایران فرصت‌های متعددی را برای دستیابی به توافقی دربارهٔ برنامه هسته‌ای خود با ایالات متحده از دست داده است.
او روز چهارشنبه ۱۵ مهر در یک نشست خبری مشترک با همتای یونانی خود در آتن گفت: «ایران فرصت‌های متعددی را برای رسیدن به توافق هسته‌ای با آمریکا از دست داده و همچنان مبالغ هنگفتی را صرف تروریسم، تسلیحات و حزب‌الله می‌کند.»
روبیو همچنین گفت ایران اکنون با اقتصادی رو به فروپاشی و تحریم‌های تازه روبه‌رو است و مسئولیت این وضعیت را متوجه «روحانیون تندرو شیعه حاکم بر ایران» دانست.
او گفت: «اقتصاد ایران در آستانهٔ رسیدن به وضعیتی است که از نظر وخامت، کمتر کشوری در جهان آن را تجربه کرده است و همهٔ این‌ها نتیجهٔ عملکرد روحانیون تندروی شیعه‌ای است که در آن کشور تصمیم‌گیری می‌کنند. آن‌ها هستند که مردم محروم ایران را به چنین وضعیتی دچار کرده‌اند.»
وزیر خارجه آمریکا همچنین با تکرار موضع واشینگتن دربارهٔ جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت دونالد ترامپ توان نظامی و بخش بزرگی از ظرفیت صنایع نظامی ایران را از میان برده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78646" target="_blank">📅 16:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4XjbCwu9W364G3H11oRkm5jCBqKsIfNkgY6bV1C_9uj_fE1QwNpL5tNFhtURpn0yjmE-kyZbh4fNC15sg6Fhwvb11jcbYVXDClArchlxLMs3P0WNA601akfuacFetr5hLgi37I2xTR9kMhWS7cdOFUQK0MJIGu2wr8F1Awri9nzx_HE9tnV4hIHEx3dzefK-4ZmfnRwATJy6PjxiEFeZ8kgpEHeL98trBAeVuUzju7eAQ1v2aKxWUXNULhtbxqQ2WZl6ViWMnAR4a64gTSUjuv3DIvfCtLt_NkKWVdtGNI6g2L3L0cxERuSl92fO2DBxfQKdBl8Iuw2YiZQY3aSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه خراسان نوشت که نجمه امینی، دختر ۲۳ ساله، به اتهام «سب‌النبی و توهین به ائمه معصومین» در فضای مجازی، از سوی شعبه ششم دادگاه کیفری یک خراسان رضوی به اعدام محکوم شده است.
امینی پیش‌تر در یک فایل صوتی از زندان وکیل‌آباد مشهد از صدور حکم اعدام برای خود خبر داده بود.
پس از انتشار این فایل صوتی، خبرگزاری فارس، وابسته به سپاه پاسداران، اعلام کرد که هنوز هیچ حکم قطعی برای نجمه امینی صادر نشده و دیوان نیز درباره پرونده او اعلام نظر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78645" target="_blank">📅 16:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rYCKAZN0ACQScaptOQiWAPLcWvpxplioCiJfuvVVoAdMZBKYIfr6N9t9KHDkdWhEreXNvPqI2qrDLiwbGM00aalMW_MfE-W-jnDvCtI7ZtOK7EleJxb5aP7gO8nwhc4mMidmoL-RQY0wMiFVO08Vk4LswsO1RZFTjNC4UQBMn0TiC7xKb3R0BpRwSLNiiAHGLzR8YC_AIsu2praQniFTa69SO85-asY6PG_EctrKYpZmZ_tmc666k9wFsxcu57fT3xrwYwTBc4jUDWIClHSuccCLtP8dYXZOnKR8Tmm_nKwgbFanz-IDfjYHwWQlCQQNkvKDGdssYTkxykn5IOGhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران باید غنی‌سازی را عملاً کاهش دهد؛ میزان اختیارات پزشکیان و عراقچی روشن نیست
🔸
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، می‌گوید حکومت ایران برای پایان یافتن جنگ باید ظرفیت غنی‌سازی اورانیوم خود را به‌طور «معناداری» کاهش دهد و ایالات متحده در مذاکرات با جمهوری اسلامی، به وعده‌های لفظی بسنده نخواهد کرد و خواهان اقدام عملی تهران است.
🔸
آقای ونس در گفت‌وگو با خبرگزاری رویترز که بامداد چهارشنبه ۱۵ مهر منتشر شد، همچنین گفت ایالات متحده با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه، در تماس و مذاکره است، اما برای واشینگتن روشن نیست این دو مقام تا چه اندازه در ساختار فعلی قدرت ایران اختیار تصمیم‌گیری دارند.
🔸
اظهارات او در حالی مطرح می‌شود که تهران و واشینگتن طی هفته‌های اخیر پیشنهادهایی را برای پایان دادن به جنگ و بازگشایی کامل تنگه هرمز ردوبدل کرده‌اند، اما دو طرف همچنان بر سر دامنهٔ مذاکرات و مسئله هسته‌ای اختلاف اساسی دارند.
🔸
معاون رئیس‌جمهور آمریکا در پاسخ به پرسش رویترز دربارهٔ شرایط واشینگتن، خطاب به مقامات جمهوری اسلامی گفت: «اگر سلاح هسته‌ای نمی‌خواهید، پس چرا به سوخت غنی‌شدهٔ ۶۰ درصدی نیاز دارید؟ و اگر می‌خواهید تعهد خود را به نساختن سلاح هسته‌ای نشان دهید، سوخت با غنای بالا تولید نکنید. این یک مسئله بسیار پایه‌ای و تعیین‌کننده است.»
🔸
او افزود: «فکر می‌کنم اگر آن‌ها بخواهند تعهد خود را به نساختن سلاح هسته‌ای نشان دهند، باید در زمینهٔ ظرفیت غنی‌سازی خود اقدامی معنادار انجام دهند.»
🔸
آقای ونس در عین حال تأکید کرد که آمریکا همچنان برای رسیدن به توافق آمادگی دارد، اما چنین توافقی باید شامل امتیازهای مشخص و عملی از سوی ایران در زمینه برنامه هسته‌ای باشد.
🔸
او گفت: «ما قرار نیست حرف را با عمل معاوضه کنیم.»
🔸
این موضع با مواضعی که مقام‌های جمهوری اسلامی در روزهای اخیر اعلام کرده‌اند فاصلهٔ زیادی دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78644" target="_blank">📅 02:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=isNUhrwOznak5UBkh8efyrqRABNVGbUmfFa8tuyl90HZUX6RD8c99XCh8a4ESVl7AiH9n528-nrx-cr-1M0VYd1BFOBafU0Fmi1XSM19n90W4R6bZi2tf29kSSi5hKSmJg7aIYFMzBe0g_hzbTLVhkFwXnYWxN3ky8P_nt3juLXqXlgjWRWkYM87_X2TubQIdQp9CXys_XRTc5dkb4SVwqPbBKW49Aj64PuxhjnpS6hgqwE5VhO8AzpLfzEQxx5TY7iTE4Sl4OZ5zGF14zHVfa2kZrmQyIY7pSt11d2LJt4Dhb9YQTGJLXyJjPP-_rGUiuuFlYk34oOQd4y141GCSbASJ0P7iUWKm4XWs19konINQ7TEixkKAxhxQRgDFPEadLSM3YL38-1hu_jnCeSlesuXU_eFpWMYv7C6RwxlJFjomT_SohG-K5lYj9dgLiz_oN6gdFqoWIvzLb3W0cNiAT5dGEPfcpcb9B--aeK-NsESL92r3jZYM6-QgPZTWlY_tlhhGRUCbXGKUpendkVj8t20Wzf6DZcG5g-d0P76LuUuHOsI7QE7vDCNhOlR4zmBLR4vlIbqKEKaYf6iNcjszd1rHWqWgr30TwjhWhkzLGc8CTyJRsW0KjL2jUpeLP_0F4nnJYKdccdfpc-XbNq0VDXlCj4n73ZFS6CZOmEzZVU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=isNUhrwOznak5UBkh8efyrqRABNVGbUmfFa8tuyl90HZUX6RD8c99XCh8a4ESVl7AiH9n528-nrx-cr-1M0VYd1BFOBafU0Fmi1XSM19n90W4R6bZi2tf29kSSi5hKSmJg7aIYFMzBe0g_hzbTLVhkFwXnYWxN3ky8P_nt3juLXqXlgjWRWkYM87_X2TubQIdQp9CXys_XRTc5dkb4SVwqPbBKW49Aj64PuxhjnpS6hgqwE5VhO8AzpLfzEQxx5TY7iTE4Sl4OZ5zGF14zHVfa2kZrmQyIY7pSt11d2LJt4Dhb9YQTGJLXyJjPP-_rGUiuuFlYk34oOQd4y141GCSbASJ0P7iUWKm4XWs19konINQ7TEixkKAxhxQRgDFPEadLSM3YL38-1hu_jnCeSlesuXU_eFpWMYv7C6RwxlJFjomT_SohG-K5lYj9dgLiz_oN6gdFqoWIvzLb3W0cNiAT5dGEPfcpcb9B--aeK-NsESL92r3jZYM6-QgPZTWlY_tlhhGRUCbXGKUpendkVj8t20Wzf6DZcG5g-d0P76LuUuHOsI7QE7vDCNhOlR4zmBLR4vlIbqKEKaYf6iNcjszd1rHWqWgr30TwjhWhkzLGc8CTyJRsW0KjL2jUpeLP_0F4nnJYKdccdfpc-XbNq0VDXlCj4n73ZFS6CZOmEzZVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ، به تشخیص و ترجمه ماشین:
ما در جمهوری اسلامی ایران خیلی خوب پیش می‌رویم؛ خیلی خوب. آن‌ها دیگر نیروی نظامی ندارند؛ نابود شده. همه‌چیزشان نابود شده و آن‌ها همان طرف شرور بودند؛ قلدر خاورمیانه بودند و دیگر چندان قلدر نیستند. اما هنوز باید کار را تمام کنیم و فقط مسئله این است که به کدام روش. می‌خواهیم این کار را به روش خوب انجام بدهیم یا به روش نه‌چندان خوب؟ خیلی زود خواهید فهمید.
وقتی به «دیوار فولادی» نگاه می‌کنم، همان کاری که ما انجام داده‌ایم و آن‌ها اسمش را محاصره گذاشته‌اند؛ من اسمش را «دیوار فولادی» می‌گذارم. حتی یک کشتی هم نتوانسته به ایران برسد. تنها کشتی‌هایی که عبور می‌کنند همان‌هایی هستند که ما اجازه عبورشان را می‌دهیم و این تأثیر بسیار بزرگی داشته است.
برای همین کشورشان از نظر مالی شکست خورده است. یک کشور شکست‌خورده‌اند؛ همه دارند کنار می‌کشند، همه دارند می‌روند. به نیروهای نظامی‌شان حقوق نمی‌دهند، به پلیس‌شان حقوق نمی‌دهند، به هیچ‌کس پول نمی‌دهند؛ اوضاعشان به‌هم‌ریخته است. اما هنوز باید کار را تمام کنیم.
نیروی دریایی ما پیشتاز است تا تضمین کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. و این همان چیزی است که همیشه گفته‌ایم: هرگز اتفاق نخواهد افتاد. هرگز اتفاق نخواهد افتاد. این دیگر یک امر انجام‌شده است.
ملوانان و هوانوردان دریایی بزرگ ما قهرمانانه جنگیده‌اند تا ارتش آن‌ها را نابود کنند. آن‌ها دیگر نیروی هوایی ندارند. نیروی هوایی‌شان از بین رفته است. نیروی دریایی‌شان از بین رفته است. آن‌ها ۱۵۹ کشتی دارند؛ همه‌شان همین حالا در اعماق دریا هستند، کف دریا افتاده‌اند. رادارشان از بین رفته است. تمام تجهیزات ضدهوایی‌شان از بین رفته است. ظرفیت تولید موشک و پهپاد آن‌ها به‌شدت کاهش یافته است. به‌زودی آن هم از بین می‌رود. دقیقاً می‌دانیم بقیه‌اش کجاست.
اقتصادشان ویران شده است. تورمی دارند که هیچ کشور دیگری در جهان ندارد. و آن مردی که چند روز پیش رفت، گفت: «من می‌روم چون کشورمان تمام شده.» این را گفت. نمی‌دانم. من هیچ‌چیز را قطعی فرض نمی‌کنم، اما اوضاعشان خوب نیست.
و به لطف مردان و زنان نیروهای مسلح آمریکا، ده‌ها تن از رهبران تروریست ایران از صحنه روزگار محو شده‌اند و مستقیم به دروازه‌های جهنم فرستاده شده‌اند. همان‌طور که می‌دانید، رهبرانشان رفته‌اند. گروه دوم رهبرانشان هم رفته‌اند. و بزرگ‌ترین مشکل من این است که هیچ‌کس نمی‌داند واقعاً چه کسی کشور را اداره می‌کند. هیچ‌کس نمی‌داند؛ شاید هم این چیز خوبی باشد. اما خامنه‌ای را یادتان هست؛ همه‌شان رفته‌اند و حالا ما اینجاییم.
ما داریم کارهایی انجام می‌دهیم که هیچ‌کس قبلاً انجام نداده است. مثلاً تکلیف این کشور باید خیلی وقت پیش روشن می‌شد. حالا ۵۱ سال است. قلدر خاورمیانه. این کار باید خیلی پیش به دست رؤسای جمهور یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم. همیشه ما هستیم. کشورهای دیگر باید خیلی وقت پیش این کار را می‌کردند، چون با گذشت زمان فقط بدتر شد.
اما ما کار را انجام دادیم و راستش مدام از رهبران جهان تماس دارم که خیلی از من تشکر می‌کنند. می‌گویم: «خب، کی می‌خواهید هزینه‌اش را بدهید؟» می‌گویند: «آقا، بابت این کار خوبی که کردید ممنونیم.» و من به آن‌ها می‌گویم: «عالی است. می‌خواهید چند کشتی بفرستید؟» می‌گویند: «آقا، ترجیح می‌دهم درگیر نشوم.» آن‌ها هیچ کشتی‌ای ندارند.
واقعاً داریم بار تمام دنیا را به دوش می‌کشیم. روی دوش ماست. و به یک معنا دوست داریم این کار را انجام بدهیم، چون خودمان قوی‌تر شده‌ایم و دیگران ضعیف‌تر شده‌اند. آن‌ها فقط ضعیف و ناکارآمد شده‌اند و ما کارهایی انجام می‌دهیم که هیچ‌کس دیگر، هیچ کشوری، هرگز نمی‌توانست انجام دهد.
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78643" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/141ace0942.mp4?token=tno8U-lEY_SUMQyjZOJGY5s1MCoCDzPB8DRFjDAHJ5QDDfEXOfTsi3u8kZd2RmnaT2K-GMJ4UKQbQohh8EfQ4UYHMYEzluoKdVxiosOgt5KOLkYVIf2Zi_Kco9vDBzDTjh5l9uWj2aLWrDqygZUdXslLzaGAsQyM1sHRuJRlGM0s9MbABRi7qvRB7zOCUwbOcECTxMPYKDb3K1pcC2fnPgEwtYYIBcL4QpVXAfc-IPz8VHUJSIzW7X1BxeGP5epCjXbEAhWFeK4n6QxgXJ3zas3U6UdrJfDBx9stoldtKeWkUbqSURgxpGppo7pr4gxRTDBfrBa9ukGFGwrCvz5ibA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/141ace0942.mp4?token=tno8U-lEY_SUMQyjZOJGY5s1MCoCDzPB8DRFjDAHJ5QDDfEXOfTsi3u8kZd2RmnaT2K-GMJ4UKQbQohh8EfQ4UYHMYEzluoKdVxiosOgt5KOLkYVIf2Zi_Kco9vDBzDTjh5l9uWj2aLWrDqygZUdXslLzaGAsQyM1sHRuJRlGM0s9MbABRi7qvRB7zOCUwbOcECTxMPYKDb3K1pcC2fnPgEwtYYIBcL4QpVXAfc-IPz8VHUJSIzW7X1BxeGP5epCjXbEAhWFeK4n6QxgXJ3zas3U6UdrJfDBx9stoldtKeWkUbqSURgxpGppo7pr4gxRTDBfrBa9ukGFGwrCvz5ibA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ یک کارمند ۲۸ ساله موسسه تحقیقات ضدطاعون در سیبری پس از ابتلا به بیماری که گمان می‌رود طاعون ریوی بوده باشد، موجب نگرانی‌هایی شده است.
بر اساس این گزارش‌ها، داریا شیپیلووای ۲۸ ساله در ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) به بیمارستانی در شهر شلخوف در منطقه ایرکوتسک منتقل شد و دو روز بعد درگذشت.
ده‌ها نفر که با این زن در تماس بوده‌اند قرنطینه شده و تحت نظر پزشکان قرار گرفته‌اند، اما مقام‌های روسیه می‌گویند تاکنون هیچ مدرکی پیدا نشده که نشان دهد مرگ او با عوامل بیماری‌زایی که در محل کارش با آنها سروکار داشته، مرتبط بوده است.
مقام‌های روسیه می‌گویند وضعیت تحت کنترل است و تاکنون مورد جدیدی از بیماری‌های عفونی مرتبط با این حادثه گزارش نشده است. با این حال، گزارش‌های تاییدنشده درباره احتمال ابتلای این زن به طاعون ریوی در شبکه‌های اجتماعی منتشر شده است.
مارکو روبیو، وزیر خارجه آمریکا، گفته است واشنگتن این موضوع را از نزدیک زیر نظر دارد اما در حال حاضر دلیلی برای نگرانی نمی‌بیند. دونالد ترامپ، رئیس‌جمهور آمریکا هم اعلام کرده که آماده کمک به روسیه است.
@
VahidHeadline
, @
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78641" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/be4hCYNjG5JEBp2kQIW9dmOShdvGLd2yZn3o0YHSkXLEqnZeR5scrziEFa1egpnGwna1pxtHxysAv4n3YHzHJpJLx2doq-hsLp7ZmNU9O9dATIvGaHAF3qtgxFCo90TfgtsQY6kVWwXuQFRLNnNbR1ZwWFtc7ETguMLOy5lcZ2SWJqn42X1NYvDfBma4Vx-Be1AlV7Sv9o12X6iK-i4mPayxjYp4eDnCrIwVIO_29wwj1WAg7RNl7-d9z9NMWL7TkSiQ3woCvpYEu4oFf_LLp0bLOsdlOSYFUe6XeM50zBmY52GtgBjbypxrOJQ98EPjGCa5eAhuulA2yk9WhwntyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: رسانه‌های دولتی ایران گزارش‌های نادرستی را منتشر کرده‌اند مبنی بر اینکه یک بالگرد MH-60R نیروی دریایی آمریکا، پس از اعلام وضعیت اضطراری در شب گذشته، در دریای سرخ سقوط کرده است.
✅
واقعیت: گزارش‌ها درباره سقوط یک بالگرد نیروی دریایی آمریکا در دریای سرخ صحت ندارند. همه هواگردها و نیروهای نظامی آمریکا در سراسر خاورمیانه در امنیت هستند و وضعیت همه آن‌ها مشخص است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78640" target="_blank">📅 16:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oFvCCFw6StDymlv5qUw8SpkxBSqurUo253RUR4reP0InqRk4D5u8N8ERiH8CyHFwjOLOa0HLTB9Z497DUhb0uDnE4MWGatXvyBucq0rbASbrvV9NEtU3qS9xzXHIXYcavBzUdQVMde8a_RdlkaEfD9UBJGXJPS7idK97fonisx8bAN8tPyTgf2obSF4vMqRFgP2B6lgWrQZaGhAqHfUaWKPXRAcW59XZVkB-wUG4Nqvj77jLqsltkhJ5n_RU65e6DN1Z47cFb7TfgGW3QzOgQBzvV6RfIX9-X99aF7LceLgxYvQia431TU2wbg7v8GBnJdn5jp5CwT6UBL7xGDxJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا بعدازظهر سه‌شنبه ۱۴ مهر اعلام کرد گزارشی با تاخیر درباره حادثه‌ای در تنگه هرمز در ۱۳ مهر دریافت کرده است.
بر اساس گزارش یک «منبع تاییدشده»، یک نفتکش هنگام خروج از تنگه هرمز هدف حمله قرار گرفت.
در این اطلاعیه به هویت نفتکش، عامل حمله یا میزان خسارت احتمالی اشاره‌ای نشده و سازمان عملیات تجارت دریایی بریتانیا اعلام کرده است مقام‌ها در حال بررسی این حادثه‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78639" target="_blank">📅 16:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa2Oyscm2rmhpgpUHhwylSuybKwq6761ceANZNAdRCs1hf664YM-FGTPz2Mt4W5vriGJYFlCYZlvoHp65c7bmLvAHOmoTHePCJx_tPLrE91deIZAQWDIg7VJDSu8CkedC2n1YIk9oxPdtl0jceY3eD98_AqiOoQkk4N3W7EftC3vcyPVviutrBAUutnlNm6EJ8iwyJZrmXpSz7mPFHCVDqMPkCifhoQDrRTBokt3VwKTZpilviieKAl8F6iGE9u7ZMu3wgTDC2Wce0oOlwsibtSIOCcM04kQ_X9W6-4C-hYTk4tuI51UYmKkZhQeqb0ceEzxUw500dWrW-CMPetHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز سه‌شنبه ۱۴ مهرماه اعلام کرد شامگاه دوشنبه، فرودگاه بین‌المللی ملک عبدالله بن عبدالعزیز در جازان و فرودگاه بین‌المللی نجران هدف حمله قرار گرفتند.
براساس این بیانیه، این حملات منجر به جراحت جزئی سه نفر و بروز خسارات مادی به فرودگاه‌ها شد.
شورشیان حوثی مورد حمایت جمهوری اسلامی دوشنبه از حمله به فرودگاه‌های عربستان سعودی خبر داده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78638" target="_blank">📅 16:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78637">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dq70rDI3G-w1RfrUPnabJ98HKtPdKHGI0s6YaOJko4RfAXEcp1IucFylB68cPa6pSBspsSAKmxEoL9A05mbSGrz1wpK9sGt27ioXB9tMp0Zh-2WXoFlrD3iMRvMREfKIFkRDBpFPJwcpP3xAOo0OlefpvZ_qKDYPDv5-hOAz1YfKuEc7eXCUJcB8QUR7OqBRHN-ObKiC288q-8eHRnYHiXESXPGyB0OafSabjWr1IIxM7_dymxC4sMXq1SoP1nCjpIUc2DxMtdEMYypjEpye_XVB4PMnIswj2_88sZOYRyVNgT9_kdPk5T9AANovY-MlzBYLp1wfESULy3QtmhS5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ کشور قاره آمریکا در بیانیه‌ای که روز دوشنبه، ۱۳ مهرماه، منتشر شد «اقدامات تروریستی» جمهوری اسلامی و نیروهای نیابتی‌اش در نیمکره غربی را محکوم کردند.
در این بیانیه به «تلاش‌های خصمانه ایران و نیروهای نیابتی‌اش از جمله نقشه‌های مرگبار، تأمین غیرقانونی پول، مداخله سیاسی و فعالیت برای نفوذ خارجی» اشاره شده است.
این بیانیه اشاره می‌کند که هدف از این گونه اقدامات «تقویت شبکه‌های تروریستی، تضعیف فرایندهای قانونی یا دولتی و ضربه زدن به امنیت منطقه‌ای» است.
ایالات متحده، آرژانتین، کانادا، کلمبیا،‌ کستاریکا، جمهوری دومینیکن، گویان، پاراگوئه،‌ پرو، و ترینیداد و توباگو امضاکنندگان این بیانیه هستند.
این بیانیه پس از آن منتشر می‌شود که آمریکا و پاراگوئه در ماه سپتامبر گذشته به طور مشترک «نشست مقابله با تروریسم فراملی» را با هدف همکاری در نیمکره غربی علیه «فعالیت تروریستی» تهران برگزار کردند.
سال گذشته اکوادور که متحد آمریکا است سپاه پاسداران، حماس و حزب‌الله را سازمان‌های تروریستی اعلام کرد و آرژانتین نیز در بهمن‌ماه ۱۴۰۴ نیروی قدس سپاه پاسداران را در فهرست تروریستی قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78637" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M5XMP831lETXGIi679K3PITTqaqIcQWxxKPMHvG97EXn9NoRVDWtu1f45qMN01uvdJmwY6ba0oOCs4QaoUeFJXm_lqAHU3AEiu4tCQ2Op5cH3d0D-_NCpz5WYBjRRgLgPeSqSI99pormaREIulHzD3BvD1ZFI_kH212qnCKU1mHxxYuCLGsjCuOP0udiQcG2S3m_3MwtS_q3P5Lv9ntMwnh2onrlPppKNNPCVLmgt1RfF2UwqybH3547PGmMqjj3gPoRKaI0dIt9Ic_RIfghaYWbPtvU-o7nvcTYR1CKUOcCPElhFEFo8Iv3J7cF1w-nH6xqF8ojdfyN5-7iCrI6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی عباسیان، ۳۸ ساله و ساکن شیروان، از سوی دادگاه انقلاب بجنورد به اعدام محکوم شده است.
یک منبع مطلع به ایران‌اینترنشنال گفت حکم اعدام عباسیان یکشنبه ۱۳ مهر در زندان شیروان به او ابلاغ شد.
هادی عباسیان در جریان اعتراضات دی ماه با انتشار ویدیوهایی از مردم خواسته بود در اعتراضات شرکت کنند.
تاکنون اتهام دقیق منجر به صدور حکم اعدام و مستندات دادگاه علیه عباسیان مشخص نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78636" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78635">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKUNu_KPG8aBw9qNA-bdzXragz0cgh-C2mP5YNQnaIVMq0Ufjl7Cm45XG1YI9pntaBE4w9_Brj5u92wAXWVcjDalbgxvAMf0QofkFM5RPo050sFJI2MygGkbcpgzy-sP-s3aN8bhpTmQQpkzTytmW7t7Z295GttB4asBkXefXNQf8GkWM8gbA5Ek16vniLU_mfWm8K-hP0vUESYOKCp1XSbf5KeBsWk1MVbnirqBaKOeIZWG6S2FJHCYfs2Py9sQ9p0GXGKTR6k9P0JI6GIqQjhcJFvyxV1SMJsuqByIV_BrKuzNIeGMirQLl1ah8uCWqVqLKgDEC2Knxd9b-jBkeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر ایران از اجرای مخفیانه حکم اعدام «تورات محمدی»، شهروند ۴۲ ساله افغانستان، در زندان مرکزی کرج خبر داده است. او با اتهام «جاسوسی» به اعدام محکوم شده بود، اما مشخص نیست دستگاه قضایی جمهوری اسلامی او را به جاسوسی برای کدام کشور یا نهاد متهم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78635" target="_blank">📅 16:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LtHbwpmHB5cJRHJp7ciJm9l8K8ZGEaugKWAjIeLFIar2kya9fe89_ODl5u4ZaBsJYJiJz4xa_qbsGkqmvwZQ_AwwlSqgRRo5iX1ZxY8Ds6mrGbxcZwzU4RNsscmsV8HE9A86troS8fH-65k7EBoo0KewR87HjeptwiUMI_A4B4ZO13lhtp2oUmknOkIOyRCoRtt18k0sDT-RLrOT2VCD9Nptq38lpEEGnm9yYS75xPRUz2s2I1OGiYpmPTuqx9SpC7rfD6ZajCyCFeX8vj_9QEUdw56Z5ra9Dg46B3nPHBLIMl1WcKOVVwEnVkb6zMgkDXtd_K0vEtQIJy6kakaFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PcH0nUMHVFLSYDR9SMBlut_qff_PfPrL50fOT3ij8rRjyKd1iU3o7kSxGcQMtQ6Vzj0GDRbZJrFf-SpAqXscMZ_NeUpra7-WET0gtOcc1D14ZapXabvxJp9W-xaHAfQt43SqruXjqwAb6_c4_BzV3bqSewXTOFpYVIJ3LpWXrV_lCbVNuwkqAPbN12tuswLcD2_eT2RYmHPQo0jrKnxKRSyEt6jBau5OKA5n5J9EUNNOENiDNdTN2Uvg9zeyIe-23gagEJX_FGUB_orL0zRHzyFpjujfRMM8CGrOtIytBgYqEEmplq4Sw5dZ7RzSnVijRGXIvNh4teAeSBJAC085hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده در پی دریافت اطلاعاتی درباره احتمال حمله پهپادی جمهوری اسلامی، ۱۲ فروند بمب‌افکن بی‌۱ را از پایگاه هوایی فرفورد، متعلق به نیروی هوایی سلطنتی بریتانیا، خارج کرد.
وال‌استریت ژورنال علت خروج این بمب‌افکن‌ها را «نگرانی‌های امنیتی درباره طرح‌های احتمالی حمله به پایگاه» عنوان کرده بود.
دونالد ترامپ، رییس‌جمهوری آمریکا، دوشنبه تایید کرد بمب‌افکن‌ها به دلیل تهدید امنیتی جمهوری اسلامی از این پایگاه خارج شدند.
این در حالی است که مارکو روبیو، وزیر خارجه آمریکا، ساعاتی پیش‌تر این انتقال را بخشی از جابه‌جایی‌های معمول نیروی هوایی توصیف کرده و گفته بود ارتباط مستقیمی با تهدید ایران نداشته است.
@
VahidOOnLine
روزنامه نیویورک تایمز در گزارشی اختصاصی به نقل از مقام‌های آمریکایی و بریتانیایی نوشته است که آمریکا پس از دریافت اطلاعات جدید درباره احتمال حمله پهپادی که گفته می‌شود سپاه پاسداران آن را طراحی کرده بود، به‌طور ناگهانی هر ۱۲ فروند بمب‌افکن بی-۱ نیروی هوایی آمریکا را از پایگاه هوایی «آرای‌اف فیرفورد» در جنوب انگلیس خارج کرد.
نیویورک تایمز به نقل از این مقام ها که درخواست کرده اند ناشناس باقی بمانند نوشته:‌ «حمله احتمالی بخشی از یک طرح پیچیده و چندمرحله‌ای ایران برای هدف قرار دادن هواپیماهای آمریکایی و کشتن شماری از چندصد نیروی آمریکایی مستقر در این پایگاه بوده است. به گفته آنها، تمام بمب‌افکن‌های آمریکایی در آخر هفته از پایگاه خارج شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78633" target="_blank">📅 08:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KnKl8M-WSUGIe1FNin59JkP9W2QZxCE-_W0Rtq7cEoweFMQvRAMxdGM-fJEIOWMDDk61PGbIWlz9cY2BQ2Biu0Rf5uEiHeBmQdRUHIGmJNUoCaNvsS0wv2JrSf1qgZga_7-8ju5zmPkudQamq4lXBVDjBRZ75Fe9vkHRsg7dFyuZob5BaQQBWvn0J8XH0j16hcoTPYsLWcgeapJ2MgD6g_5NmryA3ybbwUGtZlmkfmIg0x13zoFEF-Qn-PSHdFIDxUeQ_Nvs4PTUUntPBfrb-IwRvaGxlPYpROG2JQmx4iVHx7_WAy78OmjO_hRnx2ecMdc1Q0MM0PuFVOZa0YMbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EQ8r25ZaxuKIS37e8cwtFyadlDpFop-s_fpwBpY_T6HmNuxcGPnZW5yTeaSg2uSUPRf8nfTife4bwgy6siZzAtFy9xIBgzfD7HNErPpRlLD3Gg3LBZIDh_uXPG5slGhZD24Olk37lxBcY6_7cUjzbaZsNEiDK4ep3eA0Cxh5bK-q-TxC6ZMXk3BcPGmkxfn8vo5-L4LsDrfIuU3tCk08X11b-7aIqIVl-DkBt7HeI_DKkNOJcbKKFz9Yhca7yB_5OiIMD8wU_xNVoAn7C5W3UJOdPdiXJ0qQW0Bpdepz7_srDDUvW-crh3nH-NC1hDYJiAk48DCMNZKGnNDdood3tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در پاسخ به سوال خبرنگاران درباره حادثه امنیتی در نزدیکی پایگاه هوایی فرفورد بریتانیا اعلام کرد که ایران با این پرونده مرتبط است.
ترامپ درباره دلیل خروج هواپیماهای این کشور از پایگاه فرفورد گفت: «ما با یک تهدید مواجه بودیم و اگر قرار باشد ما را تهدید کنند، هواپیماها را جابه‌جا می‌کنیم. این اقدام تا حدی مشکل را برطرف می‌کند.»
رییس‌جمهوری آمریکا تاکید کرد: «ما افرادی را که این تهدید را طراحی کرده‌اند می‌شناسیم و آنها خودشان را با دردسر بزرگی روبه‌رو کرده‌اند.»
@
VahidOOnLine
ترامپ روز دوشنبه ۱۳ مهر در کاخ سفید و در پاسخ به این پرسش که آیا احتمال می‌دهد ایران پهپادهای رزمی را به بریتانیا منتقل کرده باشد، گفت: «نمی‌توانم این را به شما بگویم، اما اگر چنین کرده باشند، بهای سنگینی خواهند پرداخت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78631" target="_blank">📅 00:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=qHWGF_VbQpLgez867vFy7bREWh-ZxMqoEgP-DmLjLXm15UhFu_SknzyElUve4XZQ0ggqkhqvWJ_iCTxTw2LHT-CA_GPqgK7Te2WVUe988zjAAj3dYdlUiB2kr5bW31JblZ3lLdKWV5L85ZrhE1BGUQ5f1f16iebS6wBINbQ-YEdfhd42kRhF-mGfiSuLDm4DY3CCMxOFuh4vH6gZ5mvqfQ0xCmYDmX92SEwa_I9taArAD_PuXsxjJgXDt4Kfnk6AVVbcxJiyOuD5YXYkfh_iqEL-LGfQdRjpYi4JN9uVH9zXaGCDpUeX9KOnXsXWMowbvSPJpNFAzIFEc0RwN3vyXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=qHWGF_VbQpLgez867vFy7bREWh-ZxMqoEgP-DmLjLXm15UhFu_SknzyElUve4XZQ0ggqkhqvWJ_iCTxTw2LHT-CA_GPqgK7Te2WVUe988zjAAj3dYdlUiB2kr5bW31JblZ3lLdKWV5L85ZrhE1BGUQ5f1f16iebS6wBINbQ-YEdfhd42kRhF-mGfiSuLDm4DY3CCMxOFuh4vH6gZ5mvqfQ0xCmYDmX92SEwa_I9taArAD_PuXsxjJgXDt4Kfnk6AVVbcxJiyOuD5YXYkfh_iqEL-LGfQdRjpYi4JN9uVH9zXaGCDpUeX9KOnXsXWMowbvSPJpNFAzIFEc0RwN3vyXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ترک کاخ سفید، در پاسخ به سوال خبرنگار فاکس‌نیوز گفت: «شخصا باور دارم که ایران مسئول حمله تروریستی فلای‌دبی بوده است».
این اظهارات در حالی مطرح شد که جی‌دی ونس، معاون رئیس‌جمهوری آمریکا در همین روز به خبرنگاران گفت که هنوز مدرک مستدلی بر دخالت جمهوری اسلامی ایران در این حمله دریافت نکرده است.
در پرواز دبی به تل‌آویو که روز چهارشنبه انجام شد، کمک‌خلبان با حمله به خلبان اصلی تلاش کرد که هواپیما را با تمام سرنشینان که اکثریت آن‌ها اسرائیلی بودند، ساقط کند. این اقدام با واکنش به‌موقع خلبان و مسافران، خنثی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78629" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJswcr7-ta08qZfE_cmFQSJ8qVpaObvBhcqfbaoN-SohO3paZGcxbFj88v8AR2YoyyuKIgQ_DAg-XDsqJF0FAo4tWkcuHCzwB71ECMhmDbjAaUcu4faZPAok5IDhjny_fkD24ClCnHRFjHENg67il-7qbbO0FgKleGRjg5Xp49aSFjElMkmx4EG6ni-luIzX4n3jRWqacBea5z5vjkcH7aNggxEWntRT-erlxxMtMngmuWqIeckNwB6R7sNF0SWDKIFwYOEoXBcg32Hv1dMSzV4ikAHvAhrZlphwrDrzZyGEqQWzQmBKRBHLQFlWXoP4AOAkshRpy5QaUJrxIL3JjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید آنچه باعث افزایش قیمت گازوئیل شده دیگر ربطی به تنگهٔ هرمز ندارد، چرا که به گفتهٔ او، اکنون مقادیر بی‌سابقه‌ای نفت تقریباً به‌صورت روزانه از این آبراه خارج می‌شود.
دونالد ترامپ روز دوشنبه ۱۳ مهر با انتشار پیامی در شبکه اجتماعی خود، تروث‌سوشال، افزایش قیمت گازوئیل را به «پالایشگاه‌ها» مرتبط دانست و نوشت: «پالایشگاه‌های روسیه توسط اوکراین هدف قرار می‌گیرند و پالایشگاه‌های ما که در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط "دمکرات‌های احمق" تعطیل می‌شوند».
اشاره رئیس‌جمهور آمریکا به گزارش‌هایی است که در روزهای اخیر از افزایش میزان خروج نفت از تنگهٔ هرمز منتشر شده است.
شرکت کپلر، ناظر بر کشتیرانی جهانی، روز ۱۳ مهر گفت که داده‌هایش نشان می‌دهد صادرات نفت خاورمیانه، بدون احتساب ایران، طی هفته گذشته، با وجود حملات به کشتی‌ها در تنگهٔ هرمز، از سطح پیش از جنگ فراتر رفته است.
با وجود افزایش میزان خروج نفت از تنگهٔ هرمز، قیمت جهانی نفت در محدوده ۱۰۰ دلار در هر بشکه باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78628" target="_blank">📅 21:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد روز دوشنبه ۱۳ مهر یک پ نفتکش در حال گذر از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.
بر اساس این گزارش، این حمله موجب بروز آتش‌سوزی در موتورخانه کشتی شده که خدمه در حال اطفای آن بوده‌اند. با این حال، سازمان تجارت دریایی بریتانیا تایید کرد که تا کنون هیچ‌گونه تلفات جانی یا خسارت زیست‌محیطی گزارش نشده است. تحقیقات در این زمینه ادامه دارد و به سایر شناورهای عبوری توصیه شده است با احتیاط کامل در منطقه تردد کنند.
@
VahidOOnLine
پیش‌تر:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز دوشنبه ۱۳ مهر، با انتشار اطلاعیه‌های رسمی، وقوع سه حادثه امنیتی جداگانه را در آب‌های تنگه هرمز و در تاریخ‌های ۱۱ و ۱۲ مهر تایید کرد. پیشتر خبرگزاریهای فارس از هدف قرار گرفتن یک نفتکش در روز شنبه خبر داده بود و روز یکشنبه نیز ایرنا از شنیده شدن صدای انفجار در حوالی جزیره قشم خبر داده و احتمال هدف قرار دادن «شناورهای متخلف» را مطرح کرده بود.
بر اساس هشدارهای رسمی UKMTO، روز شنبه یک نفتکش حامل نفت خام حین تردد در تنگه هرمز، هدف اصابت یک پرتابه ناشناس قرار گرفته است. روز یکشنبه نیز دو شناور شامل یک نفتکش حمل گاز مایع (LPG) و یک نفتکش دیگر حامل نفت خام که از سمت خلیج فارس وارد شده و در حال گذر از تنگه هرمز بودند، توسط پرتابه‌های ناشناس مورد اصابت قرار گرفتند.
سازمان UKMTO ضمن آغاز تحقیقات رسمی درباره این حملات، به تمامی شناورهای تجاری و نفتکش‌ها توصیه کرده است با احتیاط کامل از این منطقه راهبردی عبور کرده و هرگونه فعالیت مشکوک را فورا گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78626" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fei2RvvXH5H0QHxmpAVo5WvlkvTucYes4AgQ5jJDrnblIH7MjnBzdKLwDx5n1bARZH5apNmAsb3Z7FDdZgYEDNZzqeM5cBN2GNW_u6HsRdjEkr759ElQa0hwAjAlPhuXg4U2MrldEyxp2MKhT6XasfRuumxRbKpB5Do2l4LAB3LqE_Lp63hFtRpLSZ2IY98aP16SBGKeXdFkXvmzbAB4fqvkAPXXml8DTkHDgJStGjmdTWaniEqP7oFQLMiBMnQZgNi2hqPhDMWRPbs1n8Ij7rYGL0M0OERKyrAm4dtSZHx-i2_HwTh6BYh2qRjpPYAbKrx67v3Mg5C-lD0ne3Lf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا رئیسی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴ را اعدام کرد
- علیرضا رئیسی سحرگاه روز دوشنبه ۱۳ مهرماه همراه با علیرضا سپاهی، از دیگر بازداشت‌شدگان اعتراضاتدی ۱۴۰۴، در زندان دستگرد اصفهان اعدام شد.
- روز گذشته برخی منابع خبری از فراخوانده شدن خانواده علیرضا رئیسی به زندان دستگرد اصفهان خبر داده و گفته بودند این زندانی سیاسی برای اجرای حکم اعدام به سلول انفرادی منتقل شده است.
- علیرضا رئیسی فرزند دختر عموی جاویدنام رامین رئیسی از کشته‌شدگان اعتراضات دی۴۰۴ است. رامین رئیسی ۱۹ دی‌ماه با شلیک مأموران حکومتی در جریان سرکوب اعتراضات کشته شد. پیکر وی را ۲۸ دی‌ماه به خانواده تحویل دادند که در «باغ رضوان» اصفهان به خاک سپرده شد.
- علیرضا رئیسی روز پس از خاکسپاری رامین رئیسی بازداشت شد. خانواده علیرضا تا ۲۰ روز پس از بازداشت فرزندشان هیچ خبری از او نداشتند. او طی آن سه هفته زیر شدیدترین شکنجه‌ها و فشارها برای اعتراف اجباری علیه خود قرار داشته و حتی تهدید به تزریق آمپول هوا شده بود.
- علیرضا رئیسی و علیرضا سپاهی از متهمان پرونده «میدان علیخانی» اصفهان هستند که به اعتراضات شامگاه ۱۸ دی مرتبط است و نهادهای امنیتی مدعی کشته شدن چهار بسیجی و مأمور یگان ویژه در جریان این اعتراضات شدند.
- در پرونده «میدان علیخانی» ۱۲ شهروند به اعدام محکوم شدند. با اعدام علیرضا رئیسی و علیرضا سپاهی، شمار اعدام‌شدگان متهمان پرونده «میدان علیخانی» به هفت تن رسیده است.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78625" target="_blank">📅 16:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78624">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t8jMll5RYZn-LnHLM7CSKmysYPdtfKMk2xdOv5xKdDSvMAh_tLZHaWqbf-laFk5Xu6U8CY_zgDGr_eImTSfycuw0Og9I1zkf8mMZ0YLYz_mqOzKACjSqPWEQTqPycgfsfCU765H9xKXbpgkZC5rbPWL1QaYTevC8tJEBUw-puwztlT3m0k1P2uAiWm7mv-_ZvisocjV0Fv-Bx-5YJSa2VAmnw23ZkjruxmObh3L9d9EiVQxoSXRNvKQYggGX6ALaxGb7xM7uVECN2q7b4JF7FsRs62kYuVmFvIqhvIA9hQkuBUlWhxhlOoCXOGIkWOY4fBSa7BEHLrIFG3CiJZBdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا سپاهی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴  را اعدام کرد
- خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام علیرضا سپاهی بادجانی، معروف به علیرضا سپاهی، در سحرگاه روز دوشنبه ۱۳ مهرماه ۱۴۰۵ در زندان دستگرد اصفهان خبر داد.
- وکیل علیرضا سپاهی روز گذشته با اعلام خبر فراخوانده شدن خانواده علیرضا سپاهی برای ملاقات با او و انتقال این زندانی به سلول انفرادی، از خطر اجرای حکم اعدام وی خبر داده بود.
- علیرضا سپاهی پیش از اعدام و به صورت تلفنی با نامزدش عقد کرد. مهشاد کشانی، دانشجوی ۲۲ ساله ساکن اصفهان، نیز در اعتراضات دی۴۰۴ بازداشت و به پنج سال حبس تعزیری محکوم شده و در زندان زنان دولت آباد اصفهان محبوس است.
- علیرضا سپاهی قرار بود سحرگاه سه‌شنبه ششم امرداد ۱۴۰۵ به همراه ابوالفضل سپاهی بادجانی -پسرعمویش- و امیرحسین صفری حسین‌آبادی در ملک شهر اصفهان و در ملاء عام اعدام شود اما پیش از اجرای حکم به علت استرس دچار سکته قلبی شد و اجرای حکم اعدام او عقب افتاد.
+- علیرضا سپاهی چهارمین شهروند بازداشت‌شده در اعتراضات دی۴۰۴ است که طی هفته گذشته و پس از صدور بیانیه ۴۶ کشور در محکومیت اعدام‌ها در ایران، احکام اعدام آنها اجرا شده است. سیاوش جمشیدی خیرآبادی شنبه ۱۱ مهرماه در شهرکرد و علی همتی سیستانی و مجید نیک‌اندیش روز چهارشنبه هشتم مهرماه در مشهد اعدام شدند.
- پرونده معروف به پرونده «میدان علیخانی» به اعتراضات شامگاه ۱۸ دی ۱۴۰۴ مرتبط است که در محدوده میدان علیخانی، میان ملک‌شهر و کاوه اصفهان رخ داد. نهادهای امنیتی جمهوری اسلامی مدعی شدند در جریان این اعتراضات چهار نیروی بسیج و یگان ویژه کشته شدند.
- با اعدام علیرضا سپاهی، شش متهم پرونده «میدان علیخانی» اعدام شدند. عرفان اسفندیاری و گل‌محمد محمدی ۲۸ تیرماه در زندان اعدام شدند. ابوالفضل سپاهی و امیرحسین صفری در تاریخ ششم امرداد در «میدان علیخانی» در ملاء عام به دار آویخته شدند و قائم حسینی نیز ۲۹ امرداد در زندان مرکزی اصفهان (دستگرد) اعدام شد.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78624" target="_blank">📅 16:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pBIF3EWJlZQYWn_2GFGe4DjZgvarzr9bp7kuJnUqIxljp5arW3jcIAmg8XyQRhUA_tdvTuKOjgOX7ieCqT22lLsLkaXVDIxL_ZX1CZ5Tm6rA6rfs7BUIyfGlJJop31CWhdghDVeymaRuvVxQpVcUTWU4LcwNWBHJDBQQdwq-X9nJJ2lZIEorqz4BmF2SLlsPCR6avd0KuN_BFuUcj-8V48CWZKywmeuNAu_FSccR29esPaXs89OhT7caiRzPqfBgatpkALZz2a0Tkq-EE2sMHMuqt9sSslU9IEulgA6-LPPt291zqcN7EQC3mMf5neIdBo3p98sFjt6sK-n6w37W1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت ایران در پی افشا شدن توقف کامل بارگیری نفت خام کناره‌گیری کرد
معاون ارتباطات و اطلاع رسانی دفتر رئیس‌جمهور ایران روز یکشنبه ۱۲ مهر اعلام کرد که استعفای محسن پاک‌نژاد، وزیر نفت، مورد پذیرش مسعود پزشکیان قرار گرفت.
مهدی طباطبایی در شبکه ایکس نوشت که حمید بورد به به عنوان سرپرست وزارت نفت منصوب شده است. بورد به عنوان معاون وزیر و مدیرعامل شرکت ملی نفت ایران فعالیت می‌کرد.
کناره‌گیری پاک‌نژاد از وزارت نفت در حالی رخ داده که محاصره دریایی ایالات متحده علیه ایران که از ۲۳ تیر ماه دور دوم آن آغاز شده است، صادرات نفت ایران را به‌شدت کاهش داده است.
وزیر خزانه‌داری آمریکا روز نهم مهر اعلام کرد: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت هفته گذشته در گفت‌وگو با شبکه فاکس‌نیوز اعلام کرد برآورد دولت آمریکا این است که حدود ۱۵ میلیون بشکه نفت ایران همچنان در مسیر تحویل، عمدتاً به چین، قرار دارد و پس از تحویل این محموله‌ها تهران «چیزی برای تجارت در برابر هیچ چیز دیگری» نخواهد داشت.
محسن پاک‌نژاد ساعتی پیش از استعفا، بر اساس ویدئویی که رسانه‌های ایران منتشر کردند، گفت درآمد ناشی از نفت فروخته شده «وصول» می‌شود و این روند ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/78623" target="_blank">📅 21:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP8D2UoZx-wzgDiViJxBnSwSlsxqWX059QXlb-pifj618LJwVKD08cCCU67ZCsMx5NmOnsB8qqf5LIww-wxLRZE6IQfVq_xr2GSIuZpDSnP6lt3PsMPVLw3rWp_vmoAfE8CA_3A1fVOCUuKeNXJfr1cbnQUEuNBvs66aJAw1pJg-mJkc6_Ro6dp_Jz0BEGTwRcalxmWdm6AR31HHYOuhym3W4ISwGeJ8xupbiKxaTYrJ5QqZ0SKG2y1JWC_QfpHLS8OetcZf4A-GVZaeasChhQB4KbPB8p8rYu0tfo3CghX-TaLPa4Z8_kgKCRaKIiv1jDTIrB6ysjeeKQx2oV0Asw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز و طلا در یکشنبه ۱۲ مهر همچنان در مسیر صعودی قرار دارد. قیمت دلار آمریکا با افزایش نسبت به روز گذشته به ۲۷۳ هزار و ۱۰۰ تومان رسیده است.
دلار در ساعت ۱۵ روز گذشته ۲۶۸ هزار و ۵۰۰ تومان بود و به این ترتیب در کمتر از یک روز ۴ هزار و ۶۰۰ تومان، معادل حدود ۱.۷ درصد افزایش قیمت داشته است.
یورو نیز از ۳۰۲ هزار و ۲۰۰ تومان به ۳۰۷ هزار و ۴۰۰ تومان رسیده و پوند انگلیس با افزایش از ۳۵۲ هزار به ۳۵۸ هزار تومان معامله می‌شود. درهم امارات نیز به ۷۴ هزار و ۳۵۰ تومان، یوآن چین به ۴۰ هزار و ۸۴۰ تومان و لیر ترکیه به ۵ هزار و ۶۴۰ تومان رسیده‌اند. قیمت تتر نیز ۲۷۱ هزار و ۶۰۰ تومان اعلام شده است.
در بازار طلا و سکه نیز روند افزایش قیمت ادامه دارد. بر اساس نرخ‌های منتشرشده امروز، هر گرم طلای ۱۸ عیار حدود ۲۶ میلیون و ۳۸۵ هزار تومان و سکه امامی حدود ۲۷۳ میلیون و ۸۳۰ هزار تومان معامله می‌شود. سکه امامی نسبت به نرخ ۲۷۰ میلیون و ۹۰۰ هزار تومانی روز گذشته حدود ۲ میلیون و ۹۳۰ هزار تومان افزایش داشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/78622" target="_blank">📅 15:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLpfAuzCmL_xIyDnk1yTxEkC_4JB0mGXrZP8yNvKHBAYTKvc2ORR94V79j701KzdN5W5WVV-mxwiFtMUVT7V32dV78h8Zy2BAyQSec4ldB341SIsMpRDF9wkrYmNMpiTeU2xoURej314J6qfZtjSqly23dY7eYOe1Dc8N5RJY0-1PR10GzIBfv-Nn-PAQwWqrufs9MoYtvzqJYLHRNVch553SEt4bHPE947PJjvXGAjOI7MvK3nbxn03Ej5rYzoPt8y95fmiWZpwuwmVU8XKygSds_P9QURW1FRaVw42SZXqTtSKf77Ru4jiUUVbATr6TkyyN_MHjokKMLu8YPKe2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۱۲ مهر با اشاره به دیدارهایش با مقام‌های کشورهای منطقه گفت این رایزنی‌ها «بسیار موثر، محترمانه و دوستانه» بوده است.
او افزود: «ما مسیر جدیدی برای ایجاد اعتماد میان کشورهای همسایه و جمهوری اسلامی ایران آغاز کرده‌ایم و به‌خصوص در حوزه خلیج فارس، این مسیر را به خوبی طی می‌کنیم.»
وزیر امور خارجه جمهوری اسلامی همچنین گفت کشورهای حوزه خلیج فارس در این روند با ایران همراه هستند و به گفته او، «اراده مشترکی برای ایجاد صلح، ثبات و امنیت در منطقه خلیج فارس، با مشارکت خود کشورهای منطقه، شکل گرفته است که اکنون به‌طور جدی دنبال می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78621" target="_blank">📅 15:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ixy8PjMcbaiuCRN52bu6R_OOlhn18ew1hMyJ94ZYztto4RqV0b8BsjBSC2iOfNGCCUFA_4v4mTy02BFclNSjPU8i4t0wMp9tV6olWPYtA9XR7o0HtZK61LjEy9G5GlvA-zbfX_N5B2XrptJj8Hx1i35mCoUd7TctAzzSEa6uN_Kh5PfkeD7Obpp52QQdk1ti6sdrGYql4NfVdwtr6BibJfO5ba47o2k4AphBzdTWvnUT-0HArkeqNT4cPpldTe1bvFpXY2QrgkUeYY3rNHG04CzoF8b30NsR5jX4rpeCdd0lcKkoom_RG9v9bFs2Vx9KsaRNhqTup49qiMD-5eny_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=nuUEQH6Mv8LtP7quioK8gWkkZFmRHjDestizXXHhUF3rB2iwQz-cDqQHgvj-Cs943Y6hay1nGT8Mlq6PXagl5PBXD3wjphFykJN81bqOrt2NXrXrsSYwXz0K1Q7TkBvENMrSa8z0gCtPq8vQm1v98oeYxbsNxPXdHLTpmQuu1oKqo0o_LhYQ615Sa8UR1bxpGMPfWQlf6zzQ5s1mR3VupKRb6NK6YZ7FzhMbzyzqm-SLUlbDcX-2wO2ZROa99OynTbyXYD9ryOTIA_2exX_qs3gfZIkD_gKpeFeNAkrF3KLRW44vD0oSekaJT5zL_tvbk7J7m1YNaNXP4MV_ddKpNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=nuUEQH6Mv8LtP7quioK8gWkkZFmRHjDestizXXHhUF3rB2iwQz-cDqQHgvj-Cs943Y6hay1nGT8Mlq6PXagl5PBXD3wjphFykJN81bqOrt2NXrXrsSYwXz0K1Q7TkBvENMrSa8z0gCtPq8vQm1v98oeYxbsNxPXdHLTpmQuu1oKqo0o_LhYQ615Sa8UR1bxpGMPfWQlf6zzQ5s1mR3VupKRb6NK6YZ7FzhMbzyzqm-SLUlbDcX-2wO2ZROa99OynTbyXYD9ryOTIA_2exX_qs3gfZIkD_gKpeFeNAkrF3KLRW44vD0oSekaJT5zL_tvbk7J7m1YNaNXP4MV_ddKpNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز شنبه، با اشاره به تحولات جاری میان تهران و واشنگتن به خبرنگاران اعلام کرد که به‌زودی درباره ایران تصمیم‌گیری خواهد کرد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه «ایران درهم کوبیده شده است» گفت: «تصمیمی است که درباره ایران خواهم گرفت. تنها مسئله این است که یا از راه آسان خواهد بود یا از راه سخت. ما این موضوع را یا از راه آسان حل می‌کنیم یا از راه سخت.» او در ادامه افزود: «ضمنا همان‌طور که می‌دانید، ایران عملا از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.»
@
VahidOOnLine
پیت هگست، وزیر دفاع آمریکا، روز شنبه، ۱۱ مهرماه، از پاسخ به سوال‌ها درباره اعزام ناو جدید خودداری، اما تأکید کرد که رئیس جمهور آمریکا «مصمم است» از دستیابی حکومت ایران به سلاح هسته‌ای جلوگیری کند.
هگست که روز شنبه با خبرنگاران سخن می‌گفت از پاسخ صریح به این پرسش که آیا جنگ با ایران تا پایان سال جاری میلادی، سه ماه دیگر، به سرانجام خواهد رسید خودداری کرد و تصمیم در این باره را با دونالد ترامپ دانست.
روز شنبه، چند رسانهٔ خبری آمریکا گزارش دادند که پنتاگون در حال اعزام ناوگروه ناو هواپیمابر «تئودور روزولت» و یک گروه آبی‌ـ‌خاکی تفنگداران دریایی به خاورمیانه است؛ اقدامی که در صورت اجرا شمار ناوهای هواپیمابر آمریکا در منطقه را به سه فروند می‌رساند.
وال‌استریت جورنال به نقل از مقام‌های آمریکایی بدون ذکر نام آنها نوشت این اعزام، همراه با گروه آبی‌ـ‌خاکی «ماکین آیلند»، بین ۹ تا ۱۰ هزار نیروی نظامی دیگر به منطقه می‌افزاید. به نوشته این روزنامه، «تئودور روزولت» به ناوهای هواپیمابر «جرج اچ. دبلیو. بوش» و «جرج واشینگتن» خواهد پیوست که در منطقه حضور دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78619" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MK5srw8-7jXKFhYrZ_dil6f2mfh39qKgN15qWqkiqOhqoJZuktCTAroHeUT5lhXJOv8Dp7lhoPS34eR_aU93Qo8_2tvgZ8sBXaccaE_iozLm-IVLa_SqgM17LmR0VB8YDZHwNgZbsEJ-NkMMR8cuRrqmCPiiIhYnoKqYa30lW6YHr2_ky5reTbzfajOZE3gxUJY_3d-y48BMWdMMt4gsgye0DKPJlGhE5gEEA-PMCMmTvy2oJ2OyvlG_akHbCPIQwSkTGTDiSNXCH3xAWMeRl6ZKFAb6nV_2zgtQZfPFvguogWROxZenhNISecfxEAASMqOxpsSvZ0yYFiQO290T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3y4Lkfm76KdvdjIMGUMDLEOxAiAWs3hcztEEOB08wHC3U8UMnEqSyPUbTQV6YU_1wP1EWSzPit9QHSfhkN003CqZ9VRFRxyjnzFK7kXS45KmgqTQzs_kYfP_OFRdwvtWTEYykq982hul44dVlSt77TRtq4Hdo9UGpdjO_4_IytjTdAOHviXrmXkyZ1NXQCFiimGW1jLI3eOmJLdg7EzWslrlEiRTSBrYnURbI5KJRzATWQ-yQTFkAMhEB6k5fVBYkxirjKGtgz2PwxlO9fqMv70ERzerFbSTbi52rWpgceHHzlYwCjg499ooC9Hwqos_c2KSX4tpQgiKEl3Z9i5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GvTrz-Ll0L9uCvbHcNpjQQXRFDvrLbEjdc-XaGML8P6Qsmvc0V8dUXRLc5DnGe0l2Cq6SzWh56rP38NOTAtJOm9qR8PKPD_bEE39E8wa5LGhayCip94B7hMdVa7l7LpfEaMpKY_Dv7hh-1NG-nnIxIh5l0Xo6OaN-MwcoFm508b1pWepAQYvp71g_Rigxo0nElo_r80331r9-cSNE_F2htuxgovFseQb2WhA3P8oM1_Mg-p-GWZL52MMO3t5nqmUFO80_hmn1h0uW40PsGy1KsOYhvR9HIm9W1iSBXr7SFMLWqbrvctTm78rKkZtTWMdS0JfL4wBhod_sRg-Bw91yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lfkjHptuQXXgvtj40bUhjdTnEhViqwXKN7StY82nWRfEePb-lOVgXxVfyLwv6QG6Y2SQyrqg_12x4NDyCTYYreiwYxCRn0a8eeDth5-3jhvczguslNjRQPS318Xw8t89k4mQYNdcTvzlpAihamAlzHmhX7ljq_NQ_VLquUJgnIeMVqZ78g3_cTL8qRW08ZlFvsFiUgDTx6M04Syzucajiy7v3Wn_UgHGLkQhfN633DoJMkLDC9IdFJArAwDR6_WUDMIERu-NAmWEdKzUk_23zFFGfnJZBQzRJZ6Um2Ki8_Gz56TQoEvk42lHtUVIPdcY_idOYdmU-nwvFweoBRIEJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
صدور و تایید احکام اعدام برای سه زن در پرونده‌هایی با اتهامات امنیتی، نگرانی‌ها درباره استفاده گسترده‌تر از مجازات اعدام علیه بازداشت‌شدگان و متهمان پرونده‌های سیاسی و امنیتی را افزایش داده است.
🔸
محبوبه شعبانی در پرونده‌ای به اعدام محکوم شده که امدادرسانی و انتقال معترضان مجروح از جمله اقدامات منتسب به اوست. مژده هاشمی بازرگانی، که حکم اعدامش در دیوان عالی کشور تأیید شده، از شکنجه، اعتراف اجباری و محرومیت از وکیل انتخابی سخن گفته است. سودا ابراهیمی شمس‌آبادی نیز با اتهاماتی از جمله فعالیت رسانه‌ای و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور به اعدام محکوم شده است.
🔸
هر سه زن با خطر اجرای حکم اعدام روبه‌رو هستند.
@IranRights</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78615" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P-25DjUJJDNkx0U_Ckir5Z_oetKHszXT4zU824cX2ZcqV-IIACZryQ0GrIO8tZ3ngnNYpBkSTNgQaOYf1_qRlBZcruKwOdX4DV6kGrRWGVz8KdUWCPl72rEavVfyP6pdNo3tcTPWuKLfO3WY6KKI6PjeBBK7RvtI8SKyX2IPNM7GzSH3v_ZnnXhVccRHxM7gfZD1CIIDcTuAgpG2RX6Q94TDS2-2-WqNK623g07UcPdwsvxaVUqnz5ZqX7_8G3fky-5v5VihGTnYuSbYDiI6UL_R5ElTMpBUgIYvOdt-KHQCHbw5MFrm52Xd5Vq5P10sMK8lPwh9Ehn8c5F_hOBFXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس روز شنبه یازدهم مهر از شنیده شدن صدای انفجار در تنگه هرمز و هدف گرفته شدن یک کشتی تجاری در مسیر عمان خبر داد.
فارس مدعی شد، نفتکش «اور وینست» که تحت اسکورت آمریکا قرار دارد، هنگام ورود به تنگه هرمز سامانه رهگیری خود را خاموش کرده بود. این خبرگزاری دولتی نوشت، این دومین هدف‌گیری یک نفتکش در تنگه هرمز در روز شنبه است.
این خبر پس از آن منتشر شد که خبرگزاری مهر ساعتی پیش از شنیده شدن صدای انفجارهایی از سمت دریا در جزیره قشم خبر داده بود و احتمال ارتباط این صداها با شلیک به «کشتی‌های متخلف در تنگه هرمز» را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/78614" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P65t8JBlSARGoU4TekKNLKe2y4m7m_psG1udohkRrvqLdMxb3MLhzh31EE45EZIM9KZSp5oAuFzko-iS6WQnyZ1doHci-5gEtGoxDHTNniYP7raB_lFq8Wxlt0GuyLlhGNpXL_FlRo-EsEqEo7NhM-Xp__CreOe9rqIOn3Hubg5LNHSNK9She4EViNyEo2jPcvKDso-ZUgqFKSvDWt3BU1f99OqwpTpdbQTVkCBb_Stzoe4wd01lRFzBMg1SWnPtmQONQg2k1YY4Ah0xxrmkbl67nRLCfmFQVxl6rjK_2QtRy6w2JhynI-fPsIvC_TXFpDpEI0tBva28H9UzZmE-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌هایی از شنیده‌شدن صدای چند انفجار در جزیره قشم در عصر شنبه ۱۱ مهرماه، خبرگزاری مهر نوشت این صداها مرتبط با اقداماتی در خلیج فارس و تنگه هرمز است.
این خبرگزاری بدون استناد به منابع رسمی نوشت «هیچ اصابت یا حادثه امنیتی در پهنه سرزمینی جزیره» رخ نداده است.
خبرگزاری مهر در عین حال این «احتمال» را مطرح کرد که صداهای انفجار شاید به «شلیک به کشتی‌ها» در تنگه هرمز مرتبط باشد.
این در حالی است که همزمان، تصاویر متعدد و گزارش‌هایی در شبکه‌های اجتماعی منتشر شده که یک قطعه بزرگ و استوانه‌ای‌شکل را در محدوده‌ای شهری در قشم نشان می‌دهد که ظاهر آن به بخشی از یک پرتابه نظامی-دفاعی شبیه است.
گزارش‌های تأییدنشدهٔ دیگری در شبکه‌های اجتماعی نیز حاکی است که پیش از سقوط این قطعه، صدای عملیات پدافندی و چند انفجار در قشم به گوش رسیده است.
مقام‌های رسمی تاکنون توضیحی دربارهٔ تصاویر منتشرشده و این حادثه در قشم ارائه نکرده‌اند و رادیوفردا نمی‌تواند جزئیات گزارش‌های منتشرشده را به‌طور مستقل تأیید کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78613" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DsSXukNvPwxqf8iIv38k8wNhXv5DEJevXHAR6D5sWivI1sxihozWeBCT6ehmrTxz2Zd3_4ldaisBsbPVt39lRLUxM98DJicWbLWBN3CoStYnkwZHM5D0EFZjuAjpqmqZgPamy8XyeUy-AH3IMXWT3wQAy0XCtTMYhSi7nNGgi8AcidumrNFavT2CEGlhUsKzkiRhhDoSbaOejw1GevLqoRqKXLKTCNki9Ns8nV8jKx4QsnsLoDa1lOvYU95q3UwHDlmrNMa0zvbL9s9j4lUKl2uJQbcoYLaHPQ6HPYazt67tDEnYM2rHw4vBMKzUu6NAPf8kyd7OL44NbNegnP7ZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از قشم  حدود ساعت ۱۶:۳۰:  صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم  همین الان قشم موشک شلیک کردن  16:34 دقیقه   وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن صداش خیلی وحشتناک بود معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد…</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78612" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCakUhHNI09f86vqTG2TAWB_XPf7XKtuWbCoK5HCv9nqNEqZu5hNbzxEoHUPc5x8iN1hZty3KvqbgrOkd80RZUXr2A1Bzt8F8Fhmcl4hw5uQAeTf8N19eGBMvmoJopQJAKa0pdOSUn936HmNsN__WPYdzGR1FdwK4OEqFi0JYXv9TwmaRR1tSjALRFn64ABo4yv0xLhPsM9ln-hjVQGjriZeu2X7FDCyf2cotiwZB3jy6i7wmZrJSuYR3obU6G903_wcTZTycjucj-NFthFzI-tuR1BG-hNN_nPL4RJS3ZraWE0vzVJgdFtKWDcxPYhA_YyuVkzR67w57YZGerSGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند کاهش ارزش پول ملی ایران روز شنبه ۱۱ مهر ادامه یافت و بهای دلار آمریکا در بازار آزاد برای نخستین بار از مرز ۲۷۰ هزار تومان عبور کرد.
بر اساس نرخ‌های اعلام‌شده در ظهر شنبه، قیمت فروش دلار به حدود ۲۷۱ هزار تومان و یورو به بیش از ۳۰۵ هزار تومان رسید.
این در حالی است که روز پنج‌شنبه قیمت دلار در بازار آزاد حدود ۲۵۸ هزار تومان گزارش شده بود؛ به این ترتیب بهای دلار در فاصله دو روز بیش از ۱۳ هزار تومان، معادل حدود پنج درصد، افزایش یافته است.
افزایش قیمت ارزهای خارجی در حالی ادامه دارد که بانک مرکزی جمهوری اسلامی روز چهارشنبه از برنامه‌ریزی برای عرضهٔ دو میلیارد دلار اسکناس به بازار خبر داده بود.
قوه قضاییه نیز از برخورد با کانال‌ها و صفحاتی که آن‌ها را عامل «قیمت‌گذاری کاذب ارز» می‌خواند، خبر داده است.
اقتصاد ایران همزمان زیر فشار جنگ با آمریکا، تحریم‌ها و محدودیت‌های فزاینده بر تجارت خارجی ناشی از محاصره دریایی قرار دارد.
ارزش پول ملی ایران، از ۲۳ تیر، زمان آغاز محاصره دریایی آمریکا علیه ایران، تاکنون بیش از ۳۱ درصد کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78611" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3pIdgbslQRo4HpZlqpSZn6bVB4Et_JXNeC4kBinoXiSZcmU7yeMMygdTsvp_PLhC2jpQJE58JaiEfgh6PyZBTTex2eGcnjoIg5bWpICytTV5TPNq4fuFtrI6Z9EIn2DIcCusQMwrX4LyrfVgF-o6av8OQqx8QjpTDxx7QgWa9grJ4Fu7UeZYZkabUTQeWqSzHxaeJ2WZGYG8Mowp5j6-Vw0hdbN5xQIBqfBYz61DmA-XDAydAufLIIaWx6vFMkL7m0cMd_x1tSAACERTib2zxRrPMKS6i4Yq1vTUdnKuQmMrwh-bFnj4Y9dPaYGGFYeZiVf1b4Qbf8lGZy7xVdaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با رسانه آکسیوس،‌ با تاکید بر تاثیربخشی محاصره دریایی ایران اعلام کرد، ایران برای نخستین بار از زمان آغاز صادرات نفت، در هفته جاری هیچ نفتی برای بارگیری و انتقال از طریق دریا نخواهد داشت.
او همچنین با اشاره به کم اثر شدن نفود نیروهای مسلح جمهوری اسلامی در تنگه هرمز افزود، آمریکا عبور ۱.۱ میلیارد بشکه نفت از را از این آبراهه تسهیل کرده است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال منزوی کردن ایران «به شکلی بی‌سابقه» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78610" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q33chyVCGDlGY9Y6QhX6RSIj7XWoqTKp-e2hxJTfuqsdDjwSgsDHugzaOzHIFnzY2RHnBjrOBxR4TVmPYRl4pmXAvFuWsMDQCAgtTyfe9Q8zJcwBLPXhsSRdv_QTolcCqgB0ygtSqE3aN_s-ZLdba3vWkgLvjiGquBVc9rqP_ppDf8l8KE0FVsB64wcE4P4Cg39xMdrVNB_stym3zQkkrt6oEz6VUXc4M9fvWu3F6jh7tLZAnEvlwIMvL9YJCUE1Te2UM5b11tBl4lYGzU3UPa9jTvo8Mbtklr-FYkumNqff6QHiry6ktDiH7ZNm6HadHuhqLzi0NI60AHwBff0Ljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا دو تبعه ایران را به برنامه‌ریزی برای حمله‌ای تروریستی علیه جامعه یهودیان منچستر متهم کرده است.
پلیس بریتانیا روز جمعه ۱۰ مهر ۱۴۰۵ این دو نفر را «سلام احمدیان»، ۳۶ ساله و ساکن لیورپول، و «رحمان صالحی»، ۳۴ ساله و ساکن سالفورد، معرفی کرد.
این دو نفر روز یکشنبه ۲۹ شهریور در منچستر بازداشت شدند و روز جمعه به اتهام انجام اقداماتی در راستای تدارک عملیات تروریستی تفهیم اتهام شدند.
قرار است احمدیان و صالحی روز شنبه ۱۱ مهر ۱۴۰۵ در دادگاه حاضر شوند.
پلیس می‌گوید این دو نفر برای پیشبرد توطئه ادعایی خود با فرد سومی در خارج از بریتانیا، که احتمالا در ایران حضور دارد، در تماس بوده‌اند.
به گفته پلیس، احمدیان و صالحی از طریق پیام‌رسان‌های رمزگذاری‌شده با این فرد درباره تهیه قطعات لازم برای ساخت یک بمب دست‌ساز گفت‌وگو کرده‌اند.
این دو نفر همچنین متهم شده‌اند که فایل‌های ویدیویی آموزش ساخت و مونتاژ بمب دریافت کرده، مایعات و تجهیزات مورد نیاز را تهیه کرده و برای شناسایی و بررسی اهداف احتمالی حمله از اینترنت استفاده کرده‌اند.
«ویکی ایوانز»، معاون دستیار کمیسر و هماهنگ‌کننده ارشد پلیس مبارزه با تروریسم بریتانیا، گفت این بازداشت‌ها نتیجه تحقیقات مشترک پلیس مبارزه با تروریسم و نهادهای امنیتی بوده و به خنثی‌شدن توطئه‌ای علیه جامعه یهودیان منچستر منجر شده است.
او اتهام‌های مطرح‌شده در این پرونده را «بسیار جدی» توصیف کرد.
این توطئه ادعایی هم‌زمان با اعیاد مقدس یهودیان، سالگرد حمله تروریستی سال گذشته به کنیسه «هیتون‌ پارک» و افزایش گزارش‌ها درباره حوادث یهو‌دستیزانه در سراسر بریتانیا خنثی شده است.
دولت بریتانیا دو روز پیش از اعلام این اتهام‌ها، جمهوری اسلامی را به دست داشتن در تلاش برای خرابکاری در پایگاه نیروی هوایی سلطنتی «فیرفورد» متهم کرده بود.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، روز چهارشنبه ۸ مهر ۱۴۰۵ در پاسخ به پرسشی درباره نقش ادعایی جمهوری اسلامی در حادثه امنیتی اطراف این پایگاه گفت واشینگتن در حال بررسی موضوع است.
پایگاه فیرفورد پیشتر در اختیار نیروهای آمریکایی برای انجام حملات علیه مواضع جمهوری اسلامی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78609" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JRzsjaI5bSj_9BmXdf29xNjiJAWg2LedLNSXmypyhLXPjdWtcsZWVtdX0hkOx4HyE8h5ObuOGeOffBFwWcJQrqUsIfgEGsHSLoEiQIlN4R1CGBHj63hPLbls7nkByRlCStBWOqGfli_UaTCZi2dBfKCbaLJiXUI2er8mhCpgkC3WzGX9rMc5uM-y4NzwidDKQkQACZLT6DB7GG0p-BviCRED5yQDt9o5et6QQ0Mlsa1ReJ9PeEjTMcf9QdeESJwolkew7Yfi_QUv3YLn8z4LsjJAEE3gKIyiQeJl7_q0U1Py0ih9b0IzHfnkoJ7Ev5OJ4qZDMyrbbLFV-BjXfiI5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ucn4tKCuMR72We7txC0Ab-S32QwzHleS58T9fHcEscR78q148RK1KhyI_rQlbvrcT8_aDHYFjnZyHTDEPgkoIG87-ynbiL6NeyBsHHw9mzF0OxznEAV3oKttb6RKuQlJlykJlJ74gBLgyDH5BmT1LnHbjlO0EpohtYz_EdWRSbLYnJRnErcJ4x9AEqqDxBktMPXieDf42vJNSXJ35S9Zdhg46hcwEcpGPiMjtmMTo0vZHMAh8Skil7vfWePopi1YCMUcmbbDLULUHELnJFGUpQFw6kXmTIUtO-7vqQ5fm-D-rJ8u15QGXgf0C823rHiq-3NPdxnaTqWqk9PDgKp2rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: جمهوری اسلامی سقوط خواهد کرد و «روز آزادی» مردم ایران فرا خواهد رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مصاحبه‌ای اختصاصی با روزنامه دیلی‌میل که روز شنبه ۱۱ مهر منتشر شد، گفت که به اعتقاد او جمهوری اسلامی «سقوط خواهد کرد» و خطاب به مخالفان حکومت ایران گفت: «ایمان خود را از دست ندهید، روز آزادی شما فرا خواهد رسید.»
نتانیاهو در این گفتگو مدعی شد حکومت جمهوری اسلامی ایران در شرایط کنونی «بسیار ضعیف» شده و گفت محاصره آمریکا به رهبری دونالد ترامپ، سپاه پاسداران را به‌شدت تضعیف کرده است. او در عین حال تاکید کرد که سقوط حکومت ممکن است زمان ببرد.
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت اسرائیل با همکاری آمریکا، مانع دستیابی ایران به سلاح هسته‌ای شده است. نتانیاهو گفت: «اگر ایران اکنون سلاح هسته‌ای داشت، چه اتفاقی می‌افتاد؟» و افزود که جمهوری اسلامی همزمان در حال توسعه موشک‌های دوربرد است.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتقاد از سیاست دولت‌های غربی و به‌ویژه بریتانیا گفت آنها انتقادهای خود را بر اسرائیل متمرکز کرده‌اند، در حالی که به گفته او، تهدید جمهوری اسلامی و نیروهای نیابتی آن را نادیده می‌گیرند.
او خطاب به معترضان در بریتانیا پرسید چرا به جای اسرائیل، مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنند.
نتانیاهو گفت: «چیزی که به مردم بریتانیا می‌گویم این است: کجا هستید؟ کسانی که علیه ما اعتراض می‌کنند، چرا مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنید؟ چرا تمام زهر دولت بریتانیا متوجه آنها نمی‌شود؟»
او افزود: «چرا علیه جمهوری اسلامی جهت‌گیری نمی‌شود؟ چرا علیه نیروهای نیابتی آن نیست؟»
نخست‌وزیر اسرائیل همچنین دولت‌های غربی را متهم کرد که تهدید جمهوری اسلامی را به رسمیت نمی‌شناسند و گفت: «این حکومتی در ایران است که ده‌ها هزار نفر از شهروندان خود را کشته یا مجروح کرده است.»
او افزود جمهوری اسلامی اقتصاد غرب، منابع انرژی و آبراه‌های بین‌المللی را «خفه» می‌کند اما موج خشمی را که علیه اسرائیل وجود دارد، متوجه جمهوری اسلامی نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78607" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz0ghCjSJcWjVjbd5VlaEmh9E4nzpjYSifejGGdnF9ZFTxxuvXqnfOPlcggiskvysSGmupj2IkCP0sogB30B2_Tf7VPMhFaaR_yqcsHrXosP9prJHjh9CSYEllKNrJRa5BOCiQdITnNDcsa92X280L1uKC8tfg7yVGHtOvZaSzmp_HsRpbn2li3-Zj0JSGnPzEXru_8g9irn46tGLQC2s918DQsFu5ijO25EPl_qqq10A68Jrna1TMYj7_E-AsjISuswVliqcrD6V4eF5dECCE1S6okImupfxIN4aBkOgSyPKiZj0GUx-oXrFj-aJ8BzdPaAAZoNXqhdwogs7sjuQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تیراندازی مقابل ساختمان دادگستری مهاباد در روز شنبه ۱۱ مهر، یک نفر کشته و چهار نفر زخمی شدند.
امیررضا رسولیان، فرمانده انتظامی مهاباد، اعلام کردە  این تیراندازی مقابل در دادگستری این شهرستان رخ داده و در جریان آن یک نفر کشتە  و چهار نفر زخمی شده‌اند.
یک منبع مطلع به ایران‌وایر گفت فرد مهاجم که چند سال پیش فرزندش را از دست داده اعضای خانواده فردی را که او مسئول قتل فرزندش می‌دانسته و در حال حاضر به عنوان متهم در زندان تحمل حبس می‌کند هدف تیراندازی قرار داده است.
به گفته این منبع، مهاجم پس از تیراندازی توسط مأموران انتظامی در محل بازداشت شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78606" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQci3oSVyT7XmKFszbImvPbE9OTFe_obV6u6fNM-zacy8VudW-4Ni2DXEMavi7TQHvk1g5UoqA4eMGGla5EsVIFmNi2CXxy8y53bYDP7YiMymkX4LryBZ-LCLqFnNxCe_PZSFjY6ZsYE2oCl7hEvtgNnx6XzYo9kGuUilCI5dCqIRhOKaHpNr2EhZscftffk3U9kmrhRa0oxQl7_ObFqnN9YA7LXCtt-ZrESkOkYI8ZE8ytWioce1ShuhaneLnRfbBvHqHHV4kP8wx7UD1-FYlE2k-euiAZ4yhQjOcipMJaYANawn_aUnO-pUVOim9QuYj3M7LJGy9XCJnp0W1esuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز شنبه ۱۱ مهر از بازداشت ۳۱ نفر در شهرستان سیرجان در استان کرمان خبر داد و آنها را اعضای چهار «شبکه سازمان‌یافته خرابکاری خیابانی» معرفی کرد.
این وزارتخانه مدتی شد افراد بازداشت‌شده برای شرکت در «فراخوان‌های سراسری» سازماندهی شده و در حال تهیه کوکتل مولوتف و ابزار تخریب دوربین‌های شهری بوده‌اند.
وزارت اطلاعات همچنین این افراد را به دست داشتن در «آتش‌زدن فرمانداری، تخریب بانک‌ها و ساختمان‌های دولتی و حمله به مقر پلیس» در جریان رویدادهای دی‌ماه ۱۴۰۴ متهم کرد؛ رویدادهایی که در اطلاعیه این وزارتخانه از آنها با عنوان «کودتا» یاد شده است.
در این اطلاعیه جزئیاتی درباره هویت بازداشت‌شدگان یا مستندات مربوط به اتهام‌های مطرح‌شده ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78605" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NThauR_qy9BxkanCxFAYh8_hbd56CHILNDpmUCwJMuPYrTfW2Ljt_VAp5WstbRofaV_--w3Ud7YJeZdo5CSz1iRehqurSztPUjY56SJQbiOax3y3qWsaGwmKjcFUmFpurb-4JFEVCeHh1qIQcgorUGcfjuQDY1dY-MbwI31nG9nXhLxtdLH2aJk5828-2CLa9Ax7exx1qnY5n9kq6Zpgt8cvSXesNA2aKhcPCmpYhpThPWd_pTRCykZCPD26b3bvwwaaBp0eJ5mIFWGmW7cUhSnh5k3Lm7byjMAToUmnTQoV_4oBUXftmszk19B4izS3lzhnDQpAlbYDdfXpUnwbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام «سیاوش جمشیدی خیرآبادی»، از بازداشت‌شدگان اعتراضات سراسری دی۱۴۰۴، در بامداد شنبه ۱۱مهر۱۴۰۵ خبر داد.
قوه قضاییه همچنین ادعا کرده است که جمشیدی خیرآبادی شامگاه ۱۸ دی ۱۴۰۴ در خیابان ناصرخسرو شهرکرد به‌سوی ماموران تیراندازی کرده و سپس از محل گریخته است. براساس این روایت، او دو روز بعد، ۲۰ دی ۱۴۰۴، درحالی‌که یک قبضه سلاح کمری همراه داشت، بازداشت شد.
در اطلاعیه قوه قضاییه آمده است که حکم اعدام این معترض پس از تایید در دیوان عالی کشور اجرا شد. بااین‌حال، در این اطلاعیه توضیحی درباره زمان برگزاری دادگاه، روند دادرسی و دسترسی او به وکیل منتخب ارایه نشده است.
مقامات جمهوری اسلامی معترضان دی‌ماه ۱۴۰۴ را «کودتاگر» خوانده و آن‌ها را به ارتباط با آمریکا و اسراییل و تلاش برای ایجاد ناامنی متهم می‌کنند.
«مسعود پزشکیان»، رییس‌ دولت جمهوری اسلامی، نیز در سخنرانی اخیر خود در مجمع عمومی سازمان ملل مدعی شد که مردم ایران طی هفت ماه گذشته برای «دفاع از ایران» در خیابان‌ها حضور داشته‌اند.
او معترضان را افرادی توصیف کرد که به ادعای او، آمریکا و اسرائیل آن‌ها را «تهییج» و مسلح کرده بودند تا در داخل کشور ناامنی ایجاد کنند.
صدور و اجرای بسیاری از احکام سنگین علیه معترضان دی ماه از جمله احکام اعدام ذیل قوانین «تشدید مجازات جاسوسی» صورت می‌گیرد که از منظر حقوق‌دانان و فعالان حقوق بشر شامل موارد جدی‌ نقض حقوق متهم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78604" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیام‌های دریافتی از قشم
حدود ساعت ۱۶:۳۰:
صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم
همین الان قشم موشک شلیک کردن
16:34 دقیقه
وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن
صداش خیلی وحشتناک بود
معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد بوددددد
قشم همین الان یه صدایی شد
سلام وحید جان چند دقیقه پیش یک موشک به سمت تنگه شلیک شد.
سلام وحید
دور و ور ساعت ۴:۳۰ جنگنده رد شد
سلام ساعت چهارو نیم بعداز ظهر امروز قشم  صدای جنگنده امد خیلی وحشتناک بود
[این پیام متفاوت هم بود که نمی‌د.ونم چقدر درسته. بعد از یک ساعت معلوم نشد صدای چی بود.]
قشم پدافند بالا نریمان و زدن
وحید
خیلی شدید بود صدا ها
معلوم نبود چی بود
رادار تازه ۳ روز بود درست کرده بودن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78603" target="_blank">📅 17:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78602">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=J_p7dfbqhFtqxDyrIYNbEWyRHn6HI4NGZQzNebidcDCe6U9VyPyCJHQ9t1G-vjE-H014gJFznv3VyaCAa0oogYgmK9MKXRrxzDj7h4eulseRykALCFNUcLQ3KuMU2-Ge7LiAb9VNixChOd1dWvmKpEfhIthMkuyMXL87PPLyG_N9MgzUjLKZVlU1XdG_3rP3v0tlKgPL2vqWZ3-qQYQB7rpGkLgBRIlbedr2LPPo1bHvN17UB8O3cZkPoKqHB9YPtN8Mz7b87ZSAdNidM1BwtIZVfOzkKaBU7Qr2p22HqXEkTw_cBFNQ-zbK783iP3z7Muga4rrZ-WEkTCOLrBUK2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=J_p7dfbqhFtqxDyrIYNbEWyRHn6HI4NGZQzNebidcDCe6U9VyPyCJHQ9t1G-vjE-H014gJFznv3VyaCAa0oogYgmK9MKXRrxzDj7h4eulseRykALCFNUcLQ3KuMU2-Ge7LiAb9VNixChOd1dWvmKpEfhIthMkuyMXL87PPLyG_N9MgzUjLKZVlU1XdG_3rP3v0tlKgPL2vqWZ3-qQYQB7rpGkLgBRIlbedr2LPPo1bHvN17UB8O3cZkPoKqHB9YPtN8Mz7b87ZSAdNidM1BwtIZVfOzkKaBU7Qr2p22HqXEkTw_cBFNQ-zbK783iP3z7Muga4rrZ-WEkTCOLrBUK2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز جمعه، در سخنرانی خود در آلاباما با اشاره به ضربات نظامی به ایران و انتقاد از برخی رسانه‌ها گفت:  آنها نمی‌خواهند موفقیت ما را ببینند. وقتی نیروی دریایی‌شان را منهدم کردیم، نیروی هوایی‌شان را از بین بردیم و چند ماه پیش ضربه‌ای مهلک به ایران زدیم، نیویورک‌تایمز و رسانه‌های جعلی می‌‌گفتند اوضاع ایران فوق‌العاده است. آنها همه‌چیزشان را از دست داده‌اند، از جمله رهبرانشان را.
او با تاکید بر خلأ رهبری در جمهوری اسلامی افزود: آن‌ها یک دور از رهبرانشان را از دست دادند، بعد دور دیگری را، و سپس نیمی از دسته سوم را. حتی یک دور رقابت راه انداختند که ببینند چه کسی حاضر است رهبر شود، اما هیچ شرکت‌کننده‌ای نبود و همه می‌گفتند من نمی‌خواهم.
بخشی از مشکل ما اکنون این است که اصلا نمی‌دانم باید با چه کسی طرف شوم. هیچ‌کس حاضر نیست رهبر باشد.
می‌گویم در ایران با چه کسی باید حرف بزنم؟ اما هیچ‌کس آن اطراف نیست.
در می‌زنیم، تق‌تق، ولی کسی در خانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/78602" target="_blank">📅 05:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dfGMsj2v9KNTdDED_ZSl0Ap6rKKXWyRm5IZgU4yu65gv01jz49HyHW9bHUlihscaIw0tSsP8yBEyVEymVci1bYj2bb6np07ITKsNcFmULAX6LpStxx26f2eujd6mg7wxs3gb_QCQ55AtTQhsM-yX1w2lKKfAGIVfMGwlg_nJkHbZe7pG_69hOvwjCkV3T1t5xfiUwz3HxNHu7dznLz6DyPU0xAZ0baeKwYitzDmZtk3sqSd-h117BnanmRRqBJitMRs7pyxY7S4OzKGSWR7wkrIjLQbWGHv1w8gz7Ui97xnDdLedspfwvqTbDosSZUGPiPcrC5op3HWF57k71x2Jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YEjfbSxYmzqFoRUQXHZbiwBWr6PJXa5vIQiHpoyNMNdwi6FjxU1uM2isHwjkQYalx-Lz2m0QNHARBbv82CHEywK4rq8UzDZE6YNnGbhtzrwa3dhiB3Jvx3RIfkTnMs4gG2SgwMHvYjm88Y8RNy3H3wSFZiVdTjfgjiLcpEm_w49mmw-HzFrmTceGcLZRTvVkz3LS8HXwNGFx8L2yDogkI1hF7n2Xr5ahaga1QiCBBFHumaiO_Lgb1PW1KflzNVPJ6buwr2NjrTyQwq5S6wiZwNA31pSJDGrVvwn3DTGr4wBppnJyY1a1wB1lNN7kE1ammhp8cCGoZ037gmNmLFKBGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وکیل «الناز شاکردوست» اعلام کرد دادگاه تجدیدنظر استان تهران، حکم بدوی یک سال حبس تعزیری و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری علیه موکلش را تایید کرده است.
الناز شاکردوست، بازیگر سینما، به دلیل انتشار یک استوری مرتبط با اعتراضات دی ماه ۱۴۰۴ به دادگاه انقلاب احضار و به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیزی و دوسال محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/78600" target="_blank">📅 18:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=Vlx_O_1_Tz51KeIn7OBmLliTHl8umQAGbZlw0vih-jwGC2pCYEuhRR9bUeU0VXjbwC9cDkcVvJOn3_csKwCL4I0UK82cht6_UqCxeAQ5sdk2c-Hu0VFTAZc_lwST-JAue88E4TnGMC3aaJ0HUY9aQFngLxPWf55L5azJVolK-DJyC2ioBn_CCAPDbidiV48CTBXE5W6oRulbuxpyvi_AcoI9PivnUs5G_xPFmgV9siNw1CVXCQBDgRa7U-QbVq4-3MPWpqUpuwILvZXVP5ZNi-7YtDkSdvH8j5OKaO-Gmqxd_HcYT8zWtqeO7LUYVnpMpG4OP2MX-RN30XfxpJ43Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=Vlx_O_1_Tz51KeIn7OBmLliTHl8umQAGbZlw0vih-jwGC2pCYEuhRR9bUeU0VXjbwC9cDkcVvJOn3_csKwCL4I0UK82cht6_UqCxeAQ5sdk2c-Hu0VFTAZc_lwST-JAue88E4TnGMC3aaJ0HUY9aQFngLxPWf55L5azJVolK-DJyC2ioBn_CCAPDbidiV48CTBXE5W6oRulbuxpyvi_AcoI9PivnUs5G_xPFmgV9siNw1CVXCQBDgRa7U-QbVq4-3MPWpqUpuwILvZXVP5ZNi-7YtDkSdvH8j5OKaO-Gmqxd_HcYT8zWtqeO7LUYVnpMpG4OP2MX-RN30XfxpJ43Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه پنجشنبه نهم مهر ماه، ویدیویی در شبکه اجتماعی تروث سوشال منتشر کرد که حضور گسترده معترضان در جریان اعتراضات سراسری
دی ماه
در ایران را نشان می‌دهد.
در این ویدیو، معترضان شعار می‌دهند: «امسال سال خونه، سیدعلی سرنگونه»
realDonaldTrump
این ویدیو رو ۳۱ دسامبر ۲۰۲۵ ده‌ها اکانت عربی و اکانت‌های مرتبط به یک سازمان سیاسی خارج از کشور منتشر کرده بودند و گویا بیشترین توجه رو هم در اکانت این مسئول اسرائیلی گرفته بود که بارها ویدیوهایی با شرح اشتباه هم منتشر کرده:
GadbanWaleed
اون روزها خودم هم کلی ویدیوی مهم از شهرهای مختلف ایران منتشر کرده بودم ولی به درستی تاریخ این یکی شک داشتم که مربوط به اعتراض‌های ۱۴۰۱ باشه و نگذاشته بودمش. به ویژه اینکه منبع اولیه‌اش اکانت‌هایی بودند که همیشه کلی ویدیوی قدیمی رو هم با شرح نادرست بین ویدیوهای روز منتشر می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78599" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین باستانی Hossein Bastani</strong></div>
<div class="tg-text">🔻
معمای «تیم شش‌نفره» در حکومت ایران
مسعود پزشکیان اخیرا به «تیمی شش‌نفره» در حکومت ایران اشاره کرد که در مورد بحران جاری با آمریکا «اختیار دارند تصمیم بگیرند و تصمیمات با هماهنگی آنها اجرا می‌شود». به دنبال انتشار این اظهارات در مصاحبه با سی‌بی‌اس، رسانه‌های رسمی ایران روایت‌هایی را از ترکیب تیم شش‌نفره منتشر کرده‌اند که عمدتا در مورد پنج نفر مشابه و در مورد نفر ششم متفاوت بوده‌اند. بخش ثابت روایت‌ها اغلب بر رئیس‌جمهور، رئیس مجلس، دبیر شورای عالی امنیت ملی، رئیس ستاد کل نیروهای مسلح و فرمانده کل سپاه تمرکز داشته، هرچند نفر ششم را برخی رئیس قوه قضاییه و برخی وزیر خارجه دانسته‌اند.
اشاره مسعود پزشکیان به وجود این تیم، البته اهمیت داشت، ولی این اشاره نه اولین بار بود که صورت می‌گرفت و نه نشانه تحولی کلیدی در ساختار تصمیم‌گیری کلان، یا مثلا ایجاد نهادی با اهمیتی مشابه شورای عالی امنیت ملی بود.
در تیرماه گذشته، عباس عراقچی در مصاحبه‌ای با برنامه یوتیوبی «ماجرای جنگ» گفته بود چارچوب مذاکرات با آمریکا در شورایی تعیین می‌شود که به «کمیته شش‌نفره» معروف است. توضیحات او اما نشان می‌داد که جایگاه این کمیته پایین‌تر از شعام ـ شورای عالی امنیت ملی ـ و در حد یکی از کارگروه‌های داخلی آن است. عباس عراقچی در گفتگوی خود، مشخصا از کمیته‌ای «در داخل دبیرخانه» شعام سخن گفت که ابتدا «کمیته هسته‌ای» و سپس «کمیته مذاکره» نام گرفته و در نهایت به «کمیته شش‌نفره» معروف شده است. مطابق اظهارات او، این کمیته از مدت‌ها قبل از جنگ چهل‌روزه فعال بوده و در زمان‌های دبیری علی شمخانی و سپس علی لاریجانی در شعام، به‌ترتیب تحت مسئولیت این دو نفر فعالیت می‌کرده است.
البته روایت عباس عراقچی از قرار داشتن این کمیته زیر مسئولیت دبیر شورا، این ابهام را ایجاد می‌کرد که آیا ریاست آن، مانند شعام، با رئیس‌جمهور است یا اینکه سخن از جمعی شش‌نفره است که رئیس‌جمهور را شامل نمی‌شود، ولی جمع‌بندی‌های خود را به رئیس دولت ارائه می‌کند.
در هر صورت، عباس عراقچی تاکید داشت که تصمیم‌های کمیته باید «عینا مانند مصوبات شورای عالی می‌رفت، تایید می‌شد و بعد ابلاغ می‌شد»، که اشاره‌ای به لزوم تایید مصوبات از سوی رهبر جمهوری اسلامی به نظر می‌رسید. او همچنین، به این سوال که آیا تصویب آتش‌بس (موقت) در پایان جنگ چهل‌روزه «با نظر آقا مجتبی» بود یا نه، پاسخ مثبت داد، هرچند در مورد شیوه تصویب گفت: «ارتباط ما با کسانی بود که رابط بودند و مسائل از آن طریق منتقل شد.»
قابل تامل است که مسعود پزشکیان، که در مرداد ماه از دو نوبت دیدار با رهبر جدید جمهوری اسلامی خبر داده بود، در مصاحبه‌هایش در سفر آمریکا هم به همان دو مرتبه ملاقات خود با رهبر اشاره کرد، که نشان می‌داد دیدار جدیدی با مقام اول حکومت نداشته است.
به عبارت دیگر، با گذشت هفت ماه از رهبری مجتبی خامنه‌ای، ارتباط تیم‌های حکومتی با رهبر کماکان به حلقه «رابط» اتکا دارد که، در مورد آن حدس‌های متنوعی مطرح شده است. از جمله، گمانه‌زنی‌هایی که حسین طائب رئیس جدید سازمان بسیج را از افراد موثر این حلقه می‌دانند.
🔹
ادامه  مقاله در لینک زیر در دسترس است:
https://www.bbc.com/persian/articles/cr9dw7dvjxj1o
@HosseinBastaniChannel</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78598" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVtaKONsLHmUOCA3S-HYo5OG1wqrJX6b_zhFmDolaGtv0DE6b6p0hmTS2P30ZdrN6QzFtmlOhb2UO1afVyvrU3ytS3hxzS3WzbdT7CdOFuK5K-AdftlO5YC6zh7_rwWgChDBwZGQz0mFkeHjA84qT8AeHvxpDNf1AUZKWmy2x06ux1o3v1FTOwnEyOAFtfQxXyxSb6Q70Qub6l6jXlJltIRirUX91HDVtoHKwuvBvjvQx6hLWL-zh4cCWdR--AmsFTgKD5gGzVK9XfsFty8_ZAsG596IpVTlgDjWcRQGCQAHP5T0cgazJHptpsz7Oh0b8_6bpJR734PzGbf0lsr9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا می‌گوید ایران در ماه سپتامبر حتی یک محمولهٔ نفت خام هم بارگیری نکرده است. داده‌های شرکت‌های ردیابی نفتکش‌ها نیز نشان می‌دهد در این ماه هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت شامگاه پنج‌شنبه، نهم مهر، در شبکهٔ اجتماعی ایکس نوشت: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
این در حالی است که برآورد کپلر و ورتکسا از بارگیری نفت خام و میعانات ایران در ماه اوت حدود ۲۲۰ تا ۲۵۵ هزار بشکه در روز بود.
ایران همچنان مقداری نفت را که پیشتر بارگیری و در آب‌های آسیا ذخیره شده بود به خریداران چینی تحویل می‌دهد، اما این ذخایر بدون خروج محموله‌های تازه از ایران رو به کاهش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78597" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ps8EesJLKO0MCcsyc3CLz5NKoUHFsl7h0Wv5zTtzsC1xXr0II_ei4juJnaL4hgFpetsFpzHa1ybtxkpbj67ZEKzSr2MidL8O_ozVjTdhG_vJUGOlKUiHXYAhTBCXKFapvdp6cCVkM2FP4wueOOV6TWn4_kqXuQxZ0Uu3dkt552EvKcCFkEHE_oxpczlOXZBFp9GwwwD3z8J-XeQR5jjVAItRBfM58geJ8WzJE3edPPUdRbTuJjtwzZGQ_Yw55kpEGOUz8IUa68tgFo3Gc5ILdl9pWl2aUepcGzBro5wI5uaB5WGdqvrlSVnQAb0eExpwXWjkui8lMaYB388-8rUxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز جمعه دهم مهر ماه، از وقوع درگیری مسلحانه میان سپاه پاسداران و اعضای «یک گروه تروریستی» در یکی از روستاهای شهرستان راسک در جنوب سیستان و بلوچستان خبر داد.
تسنیم با اعلام این خبر افزود نیروهای سپاه «در حال پاکسازی منطقه و بررسی وضعیت» هستند.
همزمان خبرگزاری حکومتی فارس نیز از آغاز «اقدام عملیاتی» سپاه پاسداران از صبح جمعه در راسک خبر داده است.
این خبر در حالی منتشر می‌شود که روز پنجشنبه نیز قرارگاه قدس نیروی زمینی سپاه با انتشار ویدیویی از یک درگیری مسلحانه، از کشته شدن ۶ عضو یک «گروهک تروریستی تکفیری» در منطقه منزل‌آب زاهدان خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78596" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcBiXkoHjVlPmrKsJ1egksV5qZa-c0WoSaNIi2bwVA1WiCv8y-U7rDs_qePW2JZuLnDpeWrNE2HrOVmi8bhrfAFDo71HFoqrQls3YFORscANfs91rbWdnTlbtLCEUhslW8BkIVhkGizZbttpSVqHrXA884_ei6EWwQgwe3iahDy7Ne8rBDXwHXO4eP-sRyTDb103bG4PnFn3WL7Bf0xrfv3EF3h33LRxZX4Wml3jvj42rwprLKXDBAbb-6auM3DfTqxjmVk5Z92W44sOsytXTS6JxdEnusqMqxb9L23df5-KJl6mMuIWOOCHYN0e3qymmSF3of-2qBlNbA8P61wF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در دو اظهارنظر تازه دربارهٔ ایران هشدار داد اگر مشخص شود تهران در حادثهٔ پرواز فلای‌دبی به مقصد اسرائیل دست داشته، «به‌شدت هدف قرار خواهد گرفت» و ساعاتی بعد بار دیگر گفت به اعتقاد او ایران «در آستانهٔ تسلیم‌شدن» است.
این اظهارات همزمان با ادامهٔ تحقیقات امارات متحده عربی دربارهٔ احتمال تروریستی بودن حادثهٔ پرواز فلای‌دبی و گزارش‌ها دربارهٔ تقویت حضور نظامی آمریکا در منطقه مطرح شده است.
رئیس‌جمهور آمریکا شامگاه پنج‌شنبه، نهم مهر، به وقت ایران، در پاسخ به پرسش خبرنگاران در کاخ سفید دربارهٔ احتمال ارتباط ایران با کمک‌خلبانی که به خلبان پرواز دبی به تل‌آویو حمله کرد، گفت: «بر اساس آن‌چه می‌شنوم، می‌گویم پاسخ مثبت است، اما همین حالا در حال بررسی آن هستیم.»
تاکنون هیچ مدرک علنی دربارهٔ ارتباط ایران با این حادثه منتشر نشده و تحقیقات دربارهٔ انگیزهٔ کمک‌خلبان ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78595" target="_blank">📅 16:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esGCd7-4-iRrxKQmMUzaW1AUEWpshz-XFQ5_I4f0qztDsJQlxqwVsIvYR0BtkIcte_7XU-kBQGTZ5djrA2RUuYkj_evaGjaHpmeH4wOmOQsEPFKdJfKIXZwGgtpwXlzZmtkNb6fXBi-0B7HqskXWRNa9Ah_AtZNxABhG8qg08AMpYZbET5UebTWFnD7P1zYvhuTKmetOcDQdw0C4TIxKOaLEy7pkvcEuQpkIwNHEDD8M3a7DJPNC_8nn0UARkL63LisHH8gOUA7tCXVO0NTaqLVS8Gx-Xpea8PPtkW_cqFbnB6UNL_I-WKq4P1Su-0x4qFQkuvjaLZ6rBX_mD4Il5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه شهروند اهل کرمانشاه، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در شعبه ۲۳ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌اند.
بر اساس اطلاعاتی که به سازمان حقوق بشر هانا رسیده، سیروان شعبانی، ۲۵ ساله، هنرمند و نوازنده و سرپرست یک ارکستر پاپ و سنتی، خسرو محمدی‌نیا و مسعود توشمالانی هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شوند.
هانا گزارش داده است که این سه نفر روز ۱۹ دی ۱۴۰۴، هم‌زمان با اعتراضات در اسلامشهر، از سوی نیروهای امنیتی بازداشت شدند و پس از آن مدتی در سلول انفرادی نگهداری شدند. بر اساس این گزارش، آنها پس از ماه‌ها نگهداری در شرایط انفرادی و آنچه هانا «اخذ اعترافات اجباری» خوانده، به زندان قزلحصار منتقل شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78594" target="_blank">📅 16:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCbbDMwS_h9nYsCbTUwwPNEY0i1wceR9dkQBgs7ZAV75IE3F98EvaAthFpJSA7fmULlc4SpW_coDaLLZaAO4Mie_-96XlRhsEU_bAF1KpL3YcdKKd0V_XnO8pwWH8Xi6dzv2OGSJebXDXCJZHwaOTGsFno02z6RPC3o1IMkCLwbiOkFqDVh9qWSZQVFhqt9wY7Bw__5lR1dYFg0CkOTEevlHsCs2DdLux-dfmx2wvUNd7qLV0cEbpcBNWCaUlZw3c8DNjnrA0rUj2xbR_VkohrpjJJEw00W6PaDTTZyO94pugIyIu6091z_eeKKN7UW1tKipVwn3FYn104XvhASRqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
«عملیات تجارت دریایی بریتانیا» (UKMTO) گزارشی از یک منبع ثالث دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته و در پی آن آتش‌سوزی رخ داده است.
گزارش شده که خدمه در سلامت هستند. میزان خسارت و تأثیرات زیست‌محیطی در زمان انتشار این گزارش مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78593" target="_blank">📅 23:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IcgHVJ926GcbuZJPIvbdGVJBIY0-Eyz-pnHlqyJ9CcxBZSVGv50EbReyBsrnDK8XouB7pRa7PiL40jRJ1L7ZCj0oH5hSlJZBq_EKnFWxTWzGwNInM9iEV4ikjIPAq8fqG9XTSjQxSmyRY9ov2CpRRNQbOyu076dBG_uNIurJK6wkMdIDT8dmkO3HRCEyAPAnKDi9Hr1-HABJYoOr8KU3iUMA13Smbpm5AuYsvsz_Ltyyq1rMqvdnru7AcPun_SpP-Ossn4LQeZpqD5S4pPZotUgJAjpTPiJX9OH-rGYkCehMDQ21DKX0BjuiZe65R5kA_hI2MfDQDTt8fIuCxNDjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78592" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qnpzS7N4ANZhcrcV792BfZ33WtfBM8gJEa_PF2d122vZl9dKTGz3vwBJdp0s0QzWw5zFFzYzT5O08I5Fr5rIPOcYsXLkixQpCVo5eU8YhdICKR8dpuA7MN9KPTJBgzHPUhXsfo1wEPQScK_xmi_VHfYtYI5_dzIVGVf3LGFjZRlKxWpCbSfxA4-lFOk52nYyIliOffOWCnkFC45bBc8dzLC2nn0wR3Tif-g11eQToKd-wia_eJKQHbjoI61vr7aktVWfgMm_jjhLzDW_He7gKU_YPpUjc3hFP_faW8Vm1vb5kZXpzTkitB1qdkGblEh_Au_L5cd6zrK2I36b-sKzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهوری آمریکا، در مصاحبه‌ای مفصل با مجله تایم گفت پیشنهاد اخیر جمهوری اسلامی برای پایان دادن به درگیری‌ها و بازگشایی تنگه هرمز را به دلیل «ناکافی» بودن آن رد کرده است، و افزود احتمال تشدید حملات نظامی آمریکا علیه جمهوری اسلامی را منتفی نمی‌داند. این مصاحبه ۶ مهر در کاخ سفید انجام و روز پنجشنبه ۹ مهر منتشر شد.
دونالد ترامپ در پاسخ به این پرسش که چرا درگیری نظامی با جمهوری اسلامی بر خلاف برآورد اولیه او وارد هفتمین ماه شده است، گفت پس از حمله بمب‌افکن‌های بی-۲ به تاسیسات هسته‌ای می‌توانست عملیات را متوقف کند، اما تصمیم گرفت «فراتر» برود تا حکومت ایران نتواند توانایی‌های خود را «به شکلی متفاوت» بازسازی کند.
او گفت: «توانایی هسته‌ای آنها را نابود کرده‌ام. نیروی دریایی‌شان را نابود کرده‌ام؛ ۱۵۹ کشتی در کف دریا هستند. نیروی هوایی‌شان را نابود کرده‌ام. همه هواپیماهایشان از بین رفته‌اند. رادارشان را نابود کرده‌ام.» رئیس جمهوری آمریکا همچنین گفت اقتصاد جمهوری اسلامی از بین رفته و تورم آن حدود ۳۰۰ درصد است.
ترامپ گفت آمریکا عملا کنترل تنگه هرمز را از جمهوری اسلامی گرفته است، و تاکید کرد شب پیش از مصاحبه حجم عبور نفت از این آبراه به بالاترین میزان تاریخی رسیده بود. داده‌های جدید نشان می‌دهد صادرات نفت خلیج فارس در روزهای اخیر به‌ شدت بهبود یافته و به سطوح متوسط سال ۲۰۲۵ بازگشته است.
در بخش دیگری از مصاحبه، خبرنگار تایم به اظهارات اخیر ترامپ درباره احتمال «نابودی ایران» اشاره کرد و پرسید آیا چنین اقدامی واقعا ممکن است. او پاسخ داد: «بله، این کار را خواهم کرد. ممکن است.»
هنگامی که خبرنگار درباره مردم غیرنظامی ایران پرسید، رئیس جمهوری به سرکوب اعتراضات اشاره کرد و گفت حکومت ایران طی ماه‌های اخیر بین ۷۲ هزار تا ۷۵ هزار نفر را کشته است.
ترامپ همچنین گفت از تصمیم خود برای مداخله نکردن مستقیم در جریان اعتراضات دی‌ماه پشیمان نیست، و عملکرد دولتش در قبال جمهوری اسلامی را «باورنکردنی» توصیف کرد.
او گفت ایران کشوری بسیار بزرگ‌تر و دورتر از ونزوئلا است، اما «نتیجه همان خواهد بود» و افزود: «آنها می‌خواهند توافق کنند.»
در پاسخ به پرسشی درباره علت رد پیشنهاد اخیر جمهوری اسلامی برای آتش‌بس، ترامپ گفت رژیم ایران پیشنهاد بازگشایی تنگه هرمز را مطرح کرد، اما شرایط آن «حتی نزدیک به کافی هم نبود.»
رویترز گزارش داده است پیشنهاد ارائه‌شده از طریق میانجی‌های قطری شامل پایان درگیری‌ها و بازگشایی تنگه هرمز در برابر رفع برخی فشارهای اقتصادی آمریکا و دسترسی رژیم ایران به دارایی‌های مسدودشده بود. مذاکرات غیرمستقیم همچنان ادامه دارد.
خبرنگار تایم سپس پرسید آیا دولت آمریکا پس از انتخابات میان‌دوره‌ای حملات به جمهوری اسلامی را افزایش خواهد داد. ترامپ پاسخ داد: «ممکن است.»
او از ارائه جزئیات خودداری کرد، اما گفت آمریکا طی شش ماه گذشته ذخایر تسلیحاتی خود را افزایش داده و شرکت‌های دفاعی با فعالیت شبانه‌روزی در حال گسترش تولید هستند.
رئیس جمهوری آمریکا در پایان مصاحبه هدف اصلی سیاست خود در قبال جمهوری اسلامی را جلوگیری از دستیابی آن به سلاح هسته‌ای دانست و گفت: «موضوع اصلی که همیشه مطرح می‌کنم این است که ایران نمی‌تواند یک قدرت هسته‌ای باشد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78591" target="_blank">📅 17:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwseyFD0TctJVEsCYInyrnuOHnhAyHKhrLM43yKQvo9hV-vS8wa9ohnyP7IJq-NUcd0S7i_ULlg-gF_4hpaNSAYwdT8uU8RjFwBMxMrD3ileHDcQ75qFHFg6OkO2qIrBMxHNnUaJotr-JUaisJK07a2fX1CfTsJFgv-dHtTmz1YWYmhm_YquWbsGrEgjyqEVzKDLnJnmwJYFcNRnOpLSs1Nn2bX_pLFc0q-gKYB3uA42vajASN6TOC-hkaZ76ndMMgvvj9Thyss8yUNeB2hKzhqCcHnwq3GnWIWRgXtTI7a-LmMEIycFpma33ZSPHBOf3fNKH0ao_RRPSi-ixLm0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد ایران روز پنج‌شنبه با افزایشی حدود ۱.۵ درصدی نسبت به روز گذشته به ۲۵۸ هزار و ۹۰۰ تومان اوج گرفت.
دلار آمریکا در مقابل ریال ایران طی یک هفته گذشته بیش از ۱۰ درصد، طی یک ماه گذشته بیش از ۲۰ درصد و از زمان آغاز جنگ حدود ۶۴ درصد جهش داشته است.
در بازه یک‌ساله نیز نرخ برابری دلار در مقابل ریال ایران تقریبا ۱۲۵ درصد رشد داشته است.
قیمت سکه امامی نیز در لحظه تنظیم این گزارش در بعد از ظهر پنج‌شنبه از ۲۶۰ میلیون تومان فراتر رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78590" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R1vDhhRvos9gdOMSRxQym1MsKRwAD1yxzsy_RarKaKaoxvwJU74u7L9CYIgH5kAmYQ77Fgwst7KO-QHE7TBI6RauB6P6BsPj2Wwcl4thlJRW9LMZOWa4gUIl5dsxi_rcTsP0BREdikx4PRn9vo_dG8yESXs0rKvoFfodcIUrlpzjFQHbs3PfU5kwibzyuO00ZKQafDw69VaGj72OE-jnvVgp5lPEfSbHVGcsde-5AANm2ujgK4aQPGv9wvsPECkSrGekhVTxw0SQnj_fj3aQ15TzNaWS3taxPmsnM0KKI5UeMbe8QKx9yuyKmMEP2jyB4iXYu1IzDfzBt_8Ht8fI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، در واکنش به اظهارات تازه «احسان حدادی»، رییس فدراسیون دوومیدانی جمهوری اسلامی، او را «بدنام‌ترین ورزشکار تاریخ ایران» خواند و نوشت که ورزشکاران جوان باید او را «عبرت» قرار دهند، نه الگو.
فرزانه فصیحی در متنی که در صفحه اینستاگرام خود منتشر کرد، خطاب به احسان حدادی نوشت: «در جهان موازی تو باید پشت میله‌های زندان می‌بودی و از هیچ حق شهروندی برخوردار نمی‌شدی، ولی چه کنیم که اینجا سرنوشت صدها و هزاران جوان پاک و معصوم رو هم سپردن دستت و حالا فاز نصیحت برداشتی.»
این واکنش پس از آن منتشر شد که احسان حدادی، چهارشنبه ۸مهر۱۴۰۵، در گفت‌وگو با وب‌سایت حکومتی «ورزش سه»، درباره ورزشکاران زن گفته بود: «با زنان دونده جلسه می‌گذارم و به آن‌ها می‌گویم تو می‌توانی مثل خیلی از ورزشکاران زن، مجازی شوی با ۳۰ هزار، ۵۰ هزار، ۳۰۰ هزار فالوئر، یا می‌توانی قهرمان شوی.»
فرزانه فصیحی همچنین با اشاره به «ریحانه مبینی»، «زهرا زارعی» و «فاطمه محیطی‌زاده»، از ورزشکاران زن دوومیدانی ایران، نوشت تصور این‌که آنها بخواهند از آموزش‌های احسان حدادی پیروی کنند، برای او «مثل کابوس» است.
او در ادامه خطاب به رییس فدراسیون دوومیدانی نوشته است: «شریف بودن ربطی به مدال و قهرمانی نداره. تو ثابت کردی با خورجینی از مدال هم می‌شه به قهقرا رفت و منفور یک ملت شد.»
اشاره فرزانه فصیحی به «پشت میله‌های زندان»، به پرونده قضایی احسان حدادی در دهه ۱۳۹۰ بازمی‌گردد. در آن پرونده اتهام تعرض و تجاوز جنسی علیه احسان حدادی مطرح شده بود و دادگاه نیز رای به زندان، تحمل شلاق و جزای نقدی داد. با این حال پرونده با دخالت نهادهای امنیتی مختومه شد.
در سال‌های اخیر برخی از زنان شاخص دوومیدانی ایران نیز کشور را ترک کرده‌اند. «الناز کمپانی»، رکورددار دوی ۶۰ متر با مانع ایران، از مهاجرت خود به آمریکا خبر داد و پیش از او «مریم طوسی»، رکورددار دوی ۲۰۰ متر داخل سالن زنان ایران، به آمریکا مهاجرت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78589" target="_blank">📅 17:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DBMtwim45W0m-r3WguaTGP-RxRYFpTUQXdLQoTTLq6I5YmXVsAWLkEGxsdtHvcfg5dmIK04S0rqSQ9X27n8TZgQ6hVg4ChlLh71beTww8piMJghSPC7ix1ciZ-HpdVHsZPoRjcLAuO5rqlCTPBmr8vaQBkof67LbfDFFOW8tf0GD3s71Yc5i3f6Wth7CDxGVtJKcMdBw4C_eF3lZ-qgjOnvQCn4kesL5OJ6-Q5Oowa_hRopVIAUzs2b2IglYffhT2h-kAXyETSzFmWfrTOPx921kPWPeiVn1umfzfR5hFhhDhv4N_dXQebYN9932Zbai2RT5V1vcO9HZ1D_9n8_-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان صادقی، بلاگر ۲۰ ساله و از بازداشت‌شدگان [اعتراضات دی ماه] در کاشان، به بیش از ۱۳ سال حبس تعزیری محکوم شده است.
او بابت اتهام «تبلیغ علیه نظام» به هفت ماه و ۱۶ روز حبس و بابت اتهام «انتشار محتوای مجرمانه برخلاف امنیت کشور» به ۱۲ سال و شش ماه و یک روز حبس تعزیری محکوم شده است.
«انتشار محتوای مجرمانه در رسانه‌ها و مطبوعات منتهی به هتک حرمت اشخاص» نیز از دیگر اتهام‌های مطرح‌شده در پرونده اوست.
ایمان صادقی ۱۱ بهمن‌ماه ۱۴۰۴ بازداشت و پس از آن به زندان کاشان منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78588" target="_blank">📅 17:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d4H0lZeCkckv2Orq3EjyGJSElOLeFELkadoBAnLDToPGay2JSmIj3z8-MYulGFzshXwGNDL0MbiN_O39YWxvqexBpHe-VGNpNDVVqRrUYIYNVB4B-tTek4N6Oo7YyXBYhMURCJjX54LTylCanbBWtTkFohSL4gXj6K22v5Z8WdWr79btVvfLG4YYNGSAhNtLiUOq-A81wFAKbHWHO3XboOqOUSQ5VIOOzq-I-9DgzEgsP_eWtp9_s1WyDGQRWZUNSWKBewM1RlDKgL3cZ9EjmEEg0BCgJo7n9sARb8AkMgmKZJw7yxjPdPu-yC1_QhqAfL9mCI1ty9_GPm5A1wxM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه شب، گزارش نیویورک‌پست از اظهارات اسکات بسنت، وزیر خزانه‌داری آمریکا را منتشر کرد که گفته است اقتصاد جمهوری اسلامی ایران، «ظرف دو هفته» هیچ‌چیزی برای تجارت نخواهد داشت.
محاصره دریایی بنادر ایران مانع آن شده است که جمهوری اسلامی از طریق دریا بتواند نفتی صادر کند. دلار آمریکا نیز در روزهای اخیر با سقوط خیره کننده ریال جمهوری اسلامی، رکوردهای تازه‌ای زده است.
آقای بسنت به فاکس‌نیوز گفت اقتصاد تحت محاصره جمهوری اسلامی ایران به‌زودی و پس از تحویل آخرین محموله‌های نفتی خود، در حدود دو هفته دیگر «چیزی برای مبادله» نخواهد داشت.
به نوشته نیویورک پست، بسنت در مصاحبه با فاکس‌نیوز ارزیابی کرد که جمهوری اسلامی به دلیل فروپاشی اقتصاد خود که با اجرای «عملیات طرد اقتصادی» شتاب گرفته، از روی درماندگی به‌شدت مشتاق توافق است و هشدار داد که مشکلات آن طی دو هفته آینده به شکل چشمگیری وخیم‌تر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78587" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WptTN_cFFVTCsJriwsYH87GhFlVGpTsE3a1Rcg3jxNGM2clTAT2C214H6yv2qZpYQepwuZJAYob4gyZUTTAIeCOSh9-DUm-lRFh7ROXtp6MEJcz9DOLSIvD2wHXW5yza0Zy53UdzbLLhEKgrZtDUlmTWa68TK7U5HvifWyDX-Q-oFVNMZVvxlshBSAkNz0ZkTyRVHyuKs7Jzio6WXI63pX1IeREJDuYEEmJ6KXY_zUTqFEvtC3Y3s7dDIER1EMlK-T_uX-WbKh9rUQYJaQjeXNgNBKO4YeghlAmL_HID0kvBVXDvCd55O8ctKAnXSNBUU1mJ8CpWrpZsNojuoBb6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آکسیوس به نقل از یک مقام آگاه، مارکو روبیو، وزیر امور خارجه ایالات متحده، روز دوشنبه ششم مهر پس از به بن‌بست رسیدن مذاکرات با جمهوری اسلامی ایران، دستور داد هیات ایرانی حاضر در مجمع عمومی سازمان ملل، از جمله عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، فورا آمریکا را ترک کند.
یکی از مقام‌های آمریکایی به آکسیوس گفت: «روبیو هیات ایرانی را که بیش از حد مهمان مانده بود، بیرون کرد. مجمع عمومی سازمان ملل تمام شده بود و وقت آن بود که بروند.» بر اساس این گزارش، نمایندگی آمریکا در سازمان ملل دوشنبه شب به نمایندگی جمهوری اسلامی ایران اطلاع داد که هیات ایرانی باید فورا نیویورک را ترک کند.
آکسیوس نوشت عراقچی و اعضای هیات چند ساعت بعد راهی فرودگاه شدند و بامداد سه‌شنبه با پروازی از نیویورک به دوحه رفتند. منبع دوم نیز درخواست آمریکا برای خروج هیات را تایید کرد، اما گفت عراقچی از پیش قرار بود دوشنبه‌شب برای بازگشت به تهران حرکت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78586" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lno38KoqUK2FpYTH7NYKhYUwTb5c2j4Qne3zrOL2Jhhs_pK1rqufZ5rl0dwf4u2t73jX38xxieI6hZGQzi1tmLhzHzLEOpk6NBqpvHNDcpoQpffpzrXSc1SVIfUCra05yZ-WKbQIoTd7Sxt7JVoomD-YyyyfmLwt4fhtypojwTvTyMfrbfr1tTJVj1gsAoioSqs513nkXSkQIlCroflVTF6ZUUtcBJmq1cvB6CtGnD4n5aaEuO9ZiZVoHUD7hOWjCM_oXYl01GrX_tW6meIjLPk58KBL7Yua9Rl7-aZXFiTUaKL38EpG9UBnd-raoL_ZweJyj_8D5EHKQtvKJvQU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، در پاسخ به سوال خبرنگاری که از او پرسید اگر رهبران جمهوری اسلامی به گفته او «دیوانه» و «غیرمنطقی» هستند، چگونه می‌خواهید با این افراد توافق کنید؟ رئیس‌جمهوری آمریکا پاسخ داد: «شاید آن‌ها را منفجر کنیم. باید تصمیم بگیریم. منفجرشان کنیم، توافق کنیم، وقتش دارد می‌رسد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78585" target="_blank">📅 00:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=E5grb9niICyI4UxVND370_f55f6iFeC1cWIi6BPye2buIS8ytaKw1Xpb3fOEqrwRJN4VghO1GG-9h33P7wZrRFUYUTJKdkCo8kVbXIHXiEc54G2lRdIpn8ErluRqLkmBLipi9KjJpsCbz26chbMkD1b7YD2YXMI_bYJCj5HSH4lSiDPjAQWnxciDXjUyJF7ACBIHVQWzTJSfarP7iSVl9c1QTRlXC3oD93JcsiE9O2WBZyLlpFIt9NFcJdgJq50UY2ALB16CUFPhAf-7DwpV202yVZEeGl3VVcbf8CjT8QfxJRoeL3Qxlpv89fdMsVeyufCLWxP-OJx1NdGCM0Vdzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=E5grb9niICyI4UxVND370_f55f6iFeC1cWIi6BPye2buIS8ytaKw1Xpb3fOEqrwRJN4VghO1GG-9h33P7wZrRFUYUTJKdkCo8kVbXIHXiEc54G2lRdIpn8ErluRqLkmBLipi9KjJpsCbz26chbMkD1b7YD2YXMI_bYJCj5HSH4lSiDPjAQWnxciDXjUyJF7ACBIHVQWzTJSfarP7iSVl9c1QTRlXC3oD93JcsiE9O2WBZyLlpFIt9NFcJdgJq50UY2ALB16CUFPhAf-7DwpV202yVZEeGl3VVcbf8CjT8QfxJRoeL3Qxlpv89fdMsVeyufCLWxP-OJx1NdGCM0Vdzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در تازه‌ترین اظهارات خود درباره ایران گفت تحولات جدیدی «بسیار زود» رخ خواهد داد.
ترامپ گفت: «خیلی زود» خواهید دید که اتفاقاتی رخ خواهد داد. او در ادامه گفت ایران «عملا ویران شده» و با تورم بیش از ۳۰۰ درصدی و وضعیت نامناسب اقتصادی روبه‌رو است. رئیس‌جمهوری آمریکا همچنین بار دیگر گفت که در جریان جنگ، نیروی دریایی و نیروی هوایی ایران از بین رفته و تجهیزات پدافند هوایی این کشور نیز نابود شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78584" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-XNitxkOVgbSR43VEdEUse8w-O8fJxaSwFXB0SW-YYOoHofrMpflgPcD_LXiAZBWkwLCzSA3cLnMjHOwzTlzsjjav1NiPPoodjQnWTrR9m06u0GVaGZZgodjAU2751Hk99VNth6G0w9H5CpczMDh83bhuUknpCXQisnHycrY_e74QN8rYQA8bGS5IpP61_r0Dx9T0kU6PyjTeZSTsJaBp7kzNgBbChm2kyVaOttTu44wJLotd4QmM2ScTAU3m4O19sPofxMoMKIbvv-Jjeh0WcvgkQLMI44doNN_fx4qylLmydqiiwu9lABZkGs1YJ35id7GPfE_Qon0hMGrAi_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، روز چهارشنبه هشتم مهر، اعلام کرد که قرائن و شواهد قوی نشان می‌دهد جمهوری اسلامی ایران در حادثه امنیتی اخیر در نزدیکی پایگاه هوایی «فیرفورد» (RAF Fairford) تحت مدیریت آمریکا نقش داشته است.
پلیس ضدتروریسم بریتانیا روز یکشنبه پنج جوان ۲۳ تا ۲۵ ساله — که همگی اتباع بریتانیا و ساکن لندن هستند — را به اتهام آماده‌سازی برای اقدام تروریستی دستگیر کرد، اما آنان روز بعد با وثیقه آزاد شدند.
پایگاه هوایی فیرفورد در گلوستشر بریتانیا که پیشینه‌ای طولانی در استفاده توسط نیروهای آمریکایی و ناتو دارد، از ماه مارس به عنوان نقطه‌ای برای پشتیبانی لوجستیکی حملات ایالات متحده علیه ایران مورد استفاده قرار گرفته است. بریتانیا مجوز بهره‌برداری از بمب‌افکن‌های آمریکایی مستقر در این پایگاه را برای هدف قرار دادن سایت‌های موشکی ایران — که کشتی‌های عبوری در تنگه هرمز را تهدید می‌کنند — صادر کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78583" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c6ec3cef6.mp4?token=uFqM7cWZnj7LbjOHIva00sAXuUxjfAKdqQ5OL4tbZTVb7b73OfQCoZlre2hI19cbKZECQFkPmknI1fVIUNlaz7DyAKz3AU62beRkhshcdD7VqzpdXCBysKeqgg3jgSJT3QtrlHaxVe6CGqGBGwlN1gDT9PjkB1drrw265B0mVhnPG2P4yZAoqK5a0VIp3fJPFopfR3tgCcCqRKnSEeOY2kunAiBqNhEVcx4OCRNKFAMMjbxfNkgwi6vo4-SVS0IQMeKig_EN_xx0cbDRnBCe9EbNhay5vbfp7hSidobMqW793KA7x4AZc_CtHfXbRAWa9mzLcnynp4zS0W5PdWUX6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c6ec3cef6.mp4?token=uFqM7cWZnj7LbjOHIva00sAXuUxjfAKdqQ5OL4tbZTVb7b73OfQCoZlre2hI19cbKZECQFkPmknI1fVIUNlaz7DyAKz3AU62beRkhshcdD7VqzpdXCBysKeqgg3jgSJT3QtrlHaxVe6CGqGBGwlN1gDT9PjkB1drrw265B0mVhnPG2P4yZAoqK5a0VIp3fJPFopfR3tgCcCqRKnSEeOY2kunAiBqNhEVcx4OCRNKFAMMjbxfNkgwi6vo4-SVS0IQMeKig_EN_xx0cbDRnBCe9EbNhay5vbfp7hSidobMqW793KA7x4AZc_CtHfXbRAWa9mzLcnynp4zS0W5PdWUX6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روزسه‌شنبه هفتم مهر در جریان ضیافت نهاری با حضور چهره‌های برجسته فناوری و مقامات ارشد دولت در کاخ سفید، اعلام کرد که واشنگتن رسماً عبارت Artificial Intelligence (AI) را به Super Intelligence (SI) (فراهوش یا هوش برتر) تغییر خواهد داد.
ترامپ با اشاره به امضای سند رسمی این تغییر نام گفت: «ما همگی هم‌نظر هستیم که این فناوری مصنوعی نیست؛ به همین دلیل امروز سندی را برای تغییر نام رسمی آن به فراهوش امضا می‌کنیم.»
این نشست مهم با حضور رهبران ارشد دنیای فناوری و غول‌های سیلیکون‌ولی از جمله ایلان ماسک، جف بیزوس، ساتیا نادلا (مدیرعامل مایکروسافت)، لیسا سو (مدیرعامل AMD) و مدیران عامل شرکت‌های متا، انویدیا، گوگل، پالانتیر و آنتروپیک برگزار شد. همچنین گرگ براکمن، رئیس OpenAI، به نمایندگی از این شرکت در جلسه حضور داشت.
در سمت دولتی نیز چهره‌هایی چون جی‌دی ونس، معاون رئیس‌جمهور، سوزی وایلز، رئیس دفتر کاخ سفید، اسکات بسنت، وزیر خزانه‌داری و هاوارد لوتنیک، وزیر بازرگانی، ترامپ را همراهی می‌کردند. این تصمیم در ادامه سیاست‌های جدید واشنگتن برای جایگزینی عنوان «فراهوش» در تمامی اسناد و مکاتبات رسمی دولت آمریکا اتخاذ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78582" target="_blank">📅 20:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daDMlmPJJ8XItjel8jf_eP7m9BGK1SmHhz8-xB6HbBQ8Qq1qraNUDBL4-eUDfcwgAbZXDtjRTii266i5Lu20KvBavTDjKybUVE6UibTpHKgCWSIUPt00KI-y2uyeA1kSZ8hxLTygouvTd1xRq_5Hk1EDIEo2fMo3lvfyxDAG0_Rk98evXmOR1x-B7zBgYdquatwiLLm1F_NEmQw8aWOTl6ZzPbuxwLu765_EBof0k8eZ4_2-D0enuihviCkiICKRH-N4PjJB1IcOMg3Z4rNWWFcbfS96GxEaIs-4e7PHrdoEfvQuSjHCPjxg-ptga0dlW00QJZMelYN5x5JfqZSYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۶ هزار تومان گذشت و دادستان تهران به ضابطان قضایی دستور داد با «عوامل اخلال در بازار ارز» برخورد کنند.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار ۲۵۶ هزار و ۵۰۰ تومان، یورو ۲۹۰ هزار و ۵۰۰ تومان و پوند بریتانیا ۳۳۹ هزار تومان معامله شد.
دلار صبح امروز ۲۵۵ هزار تومان بود و دیروز ۲۵۳ هزار و ۱۰۰ تومان، یعنی در دو روز سه هزار و ۴۰۰ تومان بالا رفته است.
همزمان دادستان تهران از برخورد با فعالان بازار خبر داد و گفت ضابطان قضایی مأموریت یافته‌اند با بررسی میدانی و رصد فضای مجازی، عوامل اخلال را شناسایی و به دستگاه قضایی معرفی کنند و گزارش اقدام‌هایشان را روزانه بفرستند.
نیروی انتظامی جمهوری اسلامی دوشنبه ۱۱ نفر از فعالان بازار ارز را بازداشت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78581" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZGA8ahyXJWeVHh1QgUEJHLlfISaYGW47rbdH5czll6aEwR5IIJItptPKah35Y4_Af15vL_GjG1VFLTZY_DfqVzlB5i2wwE3f0CBzGedRKnUv6mVxxm9U44858_huTwE7rSGwFMgI8-iU--K5lhGlL29Ib_2L5X3yqgin8giM9MMKdTm0N0w3ustR-ibMsGQxfuV5TwO3OBimjw_03CVHqDWr3bPf5onCfSHDHdS_FPfyMT-NLVTMu8CLzFcbph0AFU_1s8mhX9ZBX7wit95WJfVbMO0e6GVr5IBngOoMNcDrOY4oFTPy7WtlDpNf695HNiBh3hACe2vvCyU4wixa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=iHSGDa31FqGowFfQicyxY2OjDcdU6NwjFiSa_9QyLrYKviJmm6CSQHVKJm4x4Re-Xwo6vRJCzCBk8f_YhfPZh8HW5ZV2W4dftN4yTfsn8KC6PzP3bMhWuqx4FS3Llw4A5oOvc7BrToKZLkhAp2rmEfDEx09LMmP40c5_Kp1yHtzZLSq4CEUj07Lnam7pLvn39zxY0LytT2nhbc46fUcWocZpvUcVFPm99VVrUqTiJZ3N4D8GrX23doOIl2POh1CQABOVA78l2sgaNHM3-0WJc8YASEABJOmjrXm6evjzs7phFpjbkl6MyfHUcynMqTBxr3h65ufvsX2w0Xd4nduiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=iHSGDa31FqGowFfQicyxY2OjDcdU6NwjFiSa_9QyLrYKviJmm6CSQHVKJm4x4Re-Xwo6vRJCzCBk8f_YhfPZh8HW5ZV2W4dftN4yTfsn8KC6PzP3bMhWuqx4FS3Llw4A5oOvc7BrToKZLkhAp2rmEfDEx09LMmP40c5_Kp1yHtzZLSq4CEUj07Lnam7pLvn39zxY0LytT2nhbc46fUcWocZpvUcVFPm99VVrUqTiJZ3N4D8GrX23doOIl2POh1CQABOVA78l2sgaNHM3-0WJc8YASEABJOmjrXm6evjzs7phFpjbkl6MyfHUcynMqTBxr3h65ufvsX2w0Xd4nduiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فرود اضطراری یک هواپیمای خطوط هوایی «فلای دوبی» از مبدأ دوبی به مقصد تل‌آویو در عربستان سعودی، نخست‌وزیر اسرائیل گفت کمک‌خلبان این هواپیما پس از حمله با چاقو به خلبان دیگر، ظاهراً تلاش کرده بود هواپیما را با سرنشینانش سرنگون کند.
بنیامین نتانیاهو، در پیامی ویدیویی که روز چهارشنبه هشتم مهر منتشر شد، گفت: «در جریان پرواز، هنگامی که هواپیما به کشور نزدیک می‌شد، یکی از خلبانان به خلبان دیگر حمله کرد و ظاهراً تلاش کرد هواپیما را با همه سرنشینانش سرنگون کند.»
او مسافران هواپیما را «قهرمان» خواند و گفت آنها با اقدامات خود «از وقوع یک فاجعه بزرگ جلوگیری کردند».
نتانیاهو همچنین گفت عربستان سعودی کمک‌خلبان این پرواز را که به ادعای او به خلبان دیگر حمله کرده و تلاش کرده بود هواپیما را سرنگون کند، بازداشت کرده است.
او افزود: «خلبانی که دست به حمله زده بود بازداشت شده و اکنون از سوی مقام‌های سعودی تحت بازجویی قرار دارد.»
نتانیاهو همچنین دستور آماده‌سازی برای مقابله با تهدیدهای احتمالی بیشتر را صادر کرد.
یسرائیل کاتز، وزیر دفاع اسرائیل، نیز روز چهارشنبه این حادثه را «تلاش برای یک حملۀ تروریستی» خواند.
او در بیانیه‌ای گفت: «حادثه جدی در پرواز فلای‌دبی یک تلاش برای حملۀ تروریستی جهادی بود که تنها به لطف شجاعت چند مسافر اسرائیلی خنثی شد؛ آنها وارد کابین خلبان شدند، تروریست را مهار کردند و با دستان خود کنترل هواپیما را به یک خدمه پروازی دیگر که در آنجا حضور داشت، بازگرداندند.»
رسانه‌های اسرائیلی روز چهارشنبه از احتمال ربوده شدن این هواپیما خبر دادند اما بعداً گزارش دادند که «بروز درگیری فیزیکی بین خلبانان» در هواپیما باعث تغییر مسیر و فرود اضطراری آن شد.
بر اساس این گزارش‌ها، این هواپیما از نوع بوئینگ ۷۳۷-مکس کد اضطراری مربوط به ربوده شدن را ارسال کرده و پس از آن ارتباطش با اسرائیل قطع شده بود.
به دنبال این اتفاق جنگنده‌های اسرائیلی به پرواز درآمدند و فعالیت فرودگاه بن‌گوریون نیز متوقف شد.
ویدیوهای منتشرشده در شبکه‌های اجتماعی که رویترز محل ضبط آنها را پرواز FZ1073 تأیید کرده، مسافران را در حال رسیدگی به دو مرد مجروح در کف هواپیما نشان می‌دهد که دست‌کم یکی از آنها لباس خلبانی بر تن دارد.
در یکی از ویدیوها، یک مسافر اسرائیلی درخواست کمک می‌کند و می‌گوید مسافران «تروریست‌ها را مهار کرده‌اند». با این حال، مقام‌های فرودگاه تبوک و این مسافر هویت فرد یا افراد مهاجم را مشخص نکرده‌اند و جزئیات دقیق چگونگی درگیری هنوز روشن نیست.
بر اساس اطلاعات وب‌سایت فلایت‌رادار۲۴، این پرواز ابتدا یک پیام اضطراری عمومی ارسال کرد و سپس پیام اضطراری دیگری فرستاد که احتمال «مداخله غیرقانونی» را نشان می‌داد. هواپیما پیش از نخستین هشدار اضطراری، در کمتر از ۳۰ ثانیه نزدیک به ۱۴ هزار پا کاهش ارتفاع داشته است.
به گزارش این وب‌سایت، هواپیمای بوئینگ ۷۳۷ که رسانه‌های اسرائیلی اعلام کردند حدود ۱۵۰ مسافر اسرائیلی را در خود جای داده بود، بار دیگر پیام اضطراری اولیه را مخابره کرد و سپس در فرودگاه تبوک در شمال‌غرب عربستان سعودی به زمین نشست.
از سوی دیگر، شرکت هواپیمایی فلای‌دبی، مستقر در امارات متحده عربی، اعلام کرد علت درگیری‌ای که «در کابین خلبان پرواز FZ1073» رخ داده، همچنان مشخص نیست و موضوع تحت بررسی رسمی قرار دارد.
سخنگوی فلای‌دبی در بیانیه‌ای گفت: «در این مرحله، دلایل و انگیزه‌های اصلی این رویداد مشخص نیست و همچنان در چارچوب یک تحقیقات رسمی در حال بررسی است. از همه طرف‌ها می‌خواهیم تا زمانی که مقام‌های مسئول در حال جمع‌آوری اطلاعات و روشن کردن ابعاد ماجرا هستند، از گمانه‌زنی زودهنگام خودداری کنند.»
خبرگزاری رویترز به نقل از مقام‌های اسرائیلی اعلام کرد کمک‌خلبانی که این حادثه را رقم زده است، شهروند عمانی است. دولت عمان هنوز درباره این موضوع اظهارنظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78575" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
