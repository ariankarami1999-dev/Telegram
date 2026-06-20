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
<img src="https://cdn1.telesco.pe/file/G6Ut2AovigygSrRHrPaz6_XuHVy4O_4F277K1qa0hIt0uiB6QlmJPeD7InefE78kFm6emlv2_GLhYYnR5ugUgbGPmJrkTIbEA_gWzrY2cT2c8L_h7CLHuYCXCZxxKfbmoW7haEfhLQ2KKhl2bkpoQSIWdD74aYls3AAj9A2yVFRCNkEd0Loyrj299iUMdiUNudj5xht_Aao94QvbfJzNjovZC1RThEbecjQI5yhYL3SKgzFo3TJJuK-dUiJZAQqwltjLaxoxWitauiOuCrOmbYhcY0lwn-B2eswAOdjQUxSfZMIDSLNzRsNMUuIoRbFOLNwP2BSvlWxhD2gHRJdguw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 01:30:28</div>
<hr>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kvEKEJBfkiUpOrGCm8dsC6NBFkhtj9caNem1RbZQ-ZL4jm82rRAduPIKziYccuimwUq0vPMPC1dmXx1GqT44PWqKoJvHx_DG8nN42i7ZjiZ0Qjzao4kwGUL_zs5fTW7zDLlV-5e5vmYIIPRHrc6Aho-or8wy2GlX63e2iwBF-wTE94cFo-NrOkkADLs2Htj3Z03v1eJ6LVMRY76VWUeFRSpxG0hPBCRxvQdHFPWVFxASnx6uENHTl6siBca-DQXE9ukFDQVD206U-aZ4aTrkONtu7xIKX-fPk82D8YVQK6QN7og3T4EBru_4v-bdWPdv5fjEQNs_hCabKWO6XtZn2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 155K · <a href="https://t.me/VahidOnline/76555" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=vCJj6rmSZyJv7Q-398vhW34J06dZVhcbWrEmU-T3M66Anl1V6KdowcmHE45em34X1vKrSIgR6SGv488TDfrVvIXn7rq_4EfDeOFoGMttnDIlFc18yE778CKXWBmbGClFc-U5_6We-tF3MkT1aHJWCP5yJuX1UTLewLmq_eYprbgvvr8YPLVudoU-jD-pzKTN-cajS57ovWzjiw84_K10T1zMeXl2lR5c4uSw-Xk1iWbABPFtJudSCLA6PhjXcmsOF_04_5a0ueeYQLzTrfMfe_f1FreAgjeqA_e2iFO7293-bJtwWZQqaJUYeJ1W6wPDAyoDuyGHiWiChs0SNAchFYAILzG6zAdHLk-vdv2RP0PRl5YhrnkrGS6LypkhKt4jfbj7dfJLLG2SONQzL31p8W47DHS3eqvZ0_yGRSuD5lRZaqrJMwNvQ_hvn4jZkR--sOqi-df1EQSOOwcUHdLqMoReqo96fXFQOs4AGckV6uw5FMk9HNZefhpDCzLl4zz3FlHxSvHgEWRRn13qo5MXAHUtv7KSh7BJR0zc0aSV0nUmZm4gb2--PUFYxD6P2DxdLcP8rougrit5PIOuPoE6qyE6aX73EJU2ENTukCbEigb_fYdjHb9jlQFrsx-sWD7FITp-pwZuLdfOtLHZ9Hs-ZUGbFzeYVbr5fsAP97kM15s" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=vCJj6rmSZyJv7Q-398vhW34J06dZVhcbWrEmU-T3M66Anl1V6KdowcmHE45em34X1vKrSIgR6SGv488TDfrVvIXn7rq_4EfDeOFoGMttnDIlFc18yE778CKXWBmbGClFc-U5_6We-tF3MkT1aHJWCP5yJuX1UTLewLmq_eYprbgvvr8YPLVudoU-jD-pzKTN-cajS57ovWzjiw84_K10T1zMeXl2lR5c4uSw-Xk1iWbABPFtJudSCLA6PhjXcmsOF_04_5a0ueeYQLzTrfMfe_f1FreAgjeqA_e2iFO7293-bJtwWZQqaJUYeJ1W6wPDAyoDuyGHiWiChs0SNAchFYAILzG6zAdHLk-vdv2RP0PRl5YhrnkrGS6LypkhKt4jfbj7dfJLLG2SONQzL31p8W47DHS3eqvZ0_yGRSuD5lRZaqrJMwNvQ_hvn4jZkR--sOqi-df1EQSOOwcUHdLqMoReqo96fXFQOs4AGckV6uw5FMk9HNZefhpDCzLl4zz3FlHxSvHgEWRRn13qo5MXAHUtv7KSh7BJR0zc0aSV0nUmZm4gb2--PUFYxD6P2DxdLcP8rougrit5PIOuPoE6qyE6aX73EJU2ENTukCbEigb_fYdjHb9jlQFrsx-sWD7FITp-pwZuLdfOtLHZ9Hs-ZUGbFzeYVbr5fsAP97kM15s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبویان: مجتبی خامنه‌ای نامه داده بود که چرا شروط من رو در مذاکره رعایت نکردید؟
07:20
صدا و سیما: افشای مکاتبات مجتبی خامنه‌ای از سوی نبویان در شبکه خبر پیگیرد قضایی دارد
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
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76554" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iEJoiJGPoUka9ggEfdGMg1T4DmMpgyHip6INYsWX0nrmtdu4BRXzftMaojSrsSBrcs18nf-LWgzWWgG_4e17CKv5OmYVGy4MqjgN-a6OxKD8T1Pmymsh4nHvNRywPAgYTMJKWswIVwltUsrrKJJUApMqVP3tMNAXGi3ye-COqFnc2rR-ZzYfoGqVFzXZ7ehWqY4NNSKULmBqy0LdbZ6xbOnaCqZrExKOeohoeyoQzYZLZQaSMK-KAEPvTxVBSDMVMyXLi9vAU921n4ivHppzN_xWr06kx-IYF3fX4uCQhpBbp0gf1rOBpNhh7qdE0hIbj-tJEqfNYp4KLOiiChciAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mmCOwyPq6MI9jRhXIumUrGQD2Oy89m4PnYp0hTkdFWQpuJodPpmLxtKIK5JB20UIMvnUGJNuHKym2B9x6vr3ORe_1SqlIsmaxQEq0EXfpUMM8M6zRGX_gpiT9vNnSzUXtoqk-vBLRjMkZrDssJCLYhVi3eJH2KeJz_3iLG1cAjeaCu_e7XiW7YyLsCWJY0ZpC5zMWWBNGzzAMVlOGrA1i1c0J3-F4qnxiNPlc85bg8kTZC0ytOjadsz3NYz6rJEeUy0lXiUo7TT7iIyXrYFizPuMag8C79SpscPHCcGj0gc_u_WjxRTNsIT7GnITAkJXCY_X1Bm47y6iYoy1HkzMaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76552" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jSXfcR4THfHqT49DM-yuVtyjHfiK45zlWFLGdRVM6pD9UKQBTsoo70Un74kPYD6w2LLGzffyIz5NzeRl6fobIArId1Gzti-e_dih0xu3If84CoDKESh1ijmEfv328bHcMQRINvl3aYx-t3cMSH1P4VSafdpsAWdU52JrXMTliYGE4wvQJTxRznbHzpfkxAmrtp1PPO2Mii-1V__o60fxwPtfYlLQ1Kg6sKD560KStUANvnqBNlnQSXrnzZF2deq1nhi1szaIxiofGgnzijVn7JVCzz3R-uxSfWNRCvlJhtiHigS5tV2f4n_QkUfhEejjPygbIth__SezBeWlczDQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که هیات مذاکره‌کننده جمهوری اسلامی به ریاست محمدباقر قالیباف و با حضور عباس عراقچی، عازم سوئیس شده است.
بر اساس این گزارش، عبدالناصر همتی، رییس کل بانک مرکزی و علی باقری کنی، معاون بین‌الملل دبیرخانه شورای عالی امنیت ملی نیز در این سفر حضور خواهند داشت.
همچنین کاظم غریب‌آبادی، معاون و اسماعیل بقائی، سخنگوری وزارت خارجه و حمید بورد، معاون وزیر نفت نیز این افراد را همراهی می‌کنند.
پیش‌تر وزارت خارجه پاستان اعلام کرد که مذاکرات فنی میان جمهوری اسلامی و آمریکا، یکشنبه در سوئیس آغاز خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76551" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lWd6aur0Wgjj03Y1LetsFXwrs1UtrZADLihqiyAObYjtBm3j1pCwmy-aCYD2l1kxH734BANjhmXDjvqOXkdLab4NZ78UXHOreOMSLIS3Oz2-RwzvzwfhYaJGP4zdttB8A3x1CuT7Hd4U5XUA5iALSL4Ew965uhIyAq9wt94UBglxDSlpjbQkI09s9MRM6IgUZHVz48VPbfwROkDQpGADBe4KWY_OBq-MAM6KpHH1OadoK_z6r6flMgfbNeiX2cYT4dxe_KUNfuTWQ7OSb1HBcGngRXnnm5qgqJqAuE9TnfsQaIw8mpAI45_-SceDd0b6g1qWcuDyVzSwt-tIx9KSfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/76550" target="_blank">📅 18:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=q33KDesTYEoIvOQ5HVisAipQxQ1oJSPlaRk7oWi7RjBNlPo3eIeI6TXfkARc0ochCZaX7YnBBFynIbpCicBuove0cnd8-BUEi4tKlqP1QbWO5BpmKFDYmwgOH9L6f_QzMMoyb22Ltg54_QcpZ0Mj-DsnFvufd8LJCVMNZfv3Wme2cTy1bbzL1thDTRT8DmyFzGbQxnerTsBFQB5NWhLSiLtFYAPjlaPXYuSbpRzedmpJ4nc_0W38CK8qPThLU4V5CMXhX_2gdA72Y8j05WOY7AGkJe7H21kmDCfMjr5tj4Jrb2U8qjnJ888cCLy4VFtuzGR1kGWo0ZeSjEu6tOHGQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=q33KDesTYEoIvOQ5HVisAipQxQ1oJSPlaRk7oWi7RjBNlPo3eIeI6TXfkARc0ochCZaX7YnBBFynIbpCicBuove0cnd8-BUEi4tKlqP1QbWO5BpmKFDYmwgOH9L6f_QzMMoyb22Ltg54_QcpZ0Mj-DsnFvufd8LJCVMNZfv3Wme2cTy1bbzL1thDTRT8DmyFzGbQxnerTsBFQB5NWhLSiLtFYAPjlaPXYuSbpRzedmpJ4nc_0W38CK8qPThLU4V5CMXhX_2gdA72Y8j05WOY7AGkJe7H21kmDCfMjr5tj4Jrb2U8qjnJ888cCLy4VFtuzGR1kGWo0ZeSjEu6tOHGQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی پربازدید شده که مادر مانی صفرپور، جوان کشته‌شده در اعتراضات دی‌ماه، را در حال سوگواری برای فرزندش در کنار یک دستۀ عزاداری نشان می‌دهد.
عکس پسرش را بالای دست گرفته و می‌گوید «پسرم، پسرم».
مانی صفر‌پور، جوان ۱۸ سالۀ لاهیجانی، ۱۸ دی‌ماه ۱۴۰۴ با شلیک نیروهای حکومتی در محلۀ سلسبیل تهران کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/76548" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76547">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ew294wI_hUoj2etym1kyJ7BqNp6Lfsi_HMR_IMlXTr01EJv9Oi90g2aqWjUoVaMTxM39VcAE4DHtcW_6oSFKsZX0EFhw7djjVvpKsBFJD6Pqwh0RKL9DU8hXpwp8WjAsCzjEnt7z6zU_WuZ8eYjFa7wEtiQm5_R3biiVCMlG3GB1kJ6NIFrBTgogkqMjMGM-Q8vdhUC6lg1IqQBM0nt2E7XfjyO8SA0IsnkphEHcmjPaMIpGyqtCTPQKj1ulMtNqPpsbIX94tX1yUjYy-8NWR0PXff5APQGODKDkkEs2QbYTVh256lnGNJCUgtEK7z4UKNAPtS0ZACPXRgHIJ0jUhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/76547" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r_B4qF1gqxWjB6lY4RPLmll8aWmkP7JEVRMDiuhi_kyhVg_U_PpN5eGf0qdqUsPwALZO4_fCaa3TY1jtAS_M6uNcz6o09un42IiNcG20W0lw3mvGU726oP7j7D9yAblofxs4PZCbej7GjMunZ9CJCb0fUCIvJkuTdIiXTNwYE8lhwyzYQT9uOVJLX12umyk309zb6YKdTEcLI9vXacRM5fdDNpPrKSBxIxf7lEKiIigTsnSd9G5AqG-CzgJ9cMEXVzwBAMRguqE1B2mLwPWmeJYnESil9fFIAE5J1UPSFjSnYHWQtOqz-jgAa6GOSG_JIGpOhqys1e9Px6kRFXGaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، روز شنبه ۳۰ خرداد در گفتگو با فاکس‌نیوز اعلام کرد که استیو ویتکاف، فرستاده ویژه ترامپ و جرد کوشنر، داماد او، «چند ساعتی است» که در سوئیس حضور دارند و مشغول بررسی «برخی از ابعاد فنی این مذاکرات» با ایران هستند. به گفته ونس، کوشنر و ویتکاف در گزارش‌های خود تاکید کرده‌اند که «امور به خوبی پیش می‌رود.»
ونس همچنین از احتمال ورود میانجی‌های قطری و پاکستانی به سوئیس برای پیوستن به این گفتگوها خبر داد و افزود: «قطری‌ها و پاکستانی‌ها می‌خواهند مطمئن شوند که ما این کار را به شیوه درست انجام می‌دهیم، بنابراین من تلاش می‌کنم به این روند احترام بگذارم.»
معاون ترامپ که سفر خود به سوئیس را در اواخر پنج‌شنبه شب به تعویق انداخته بود، بار دیگر تاکید کرد که انتظار دارد طی دو روز آینده عازم این کشور شود. او با این حال خاطرنشان کرد که هماهنگی‌های این سفر «همواره یک رقص هماهنگی ظریف دیپلماتیک است.» این مذاکرات که پیش‌تر قرار بود روز جمعه برگزار شود، پس از وقفه‌ای کوتاه دوباره در آستانه ازسرگیری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/76546" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwOUAjxnianhFwvPI7FGyWDBjDTDJEOzujvPPuNTIaIusMZ8fWKeDjT10Xb6wvlLt-GJzsKGnagCZ3pDU4198DQYWb_eG5QbJ4CW6vFrZgc9x8k4ViRYhpkk15xJkwnuquTDm1EikLbDKEzFWQGc0ujPl-V2buXJbIbfFJEvmekNDwMuxPqeYdcZ6wRzMiSMwqBN3GGCSYnA0DWEn3ERHzibCJcnRO44Rmk4L3FKBiegdzcBZ-BE-lqIcllQakSjtJ46YFTU2-8bizyu-1JMBQxXWRPxiiJ-xJGQ2MUnilNbuoKjliRrsTyNy59U7Q5rd11dRVFOF_6qMPuIt0MmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«طاها نظری» معترض ۱۸ساله که پیشتر به‌دلیل حضور در اعتراضات ۱۸ و ۱۹دی۱۴۰۴ بازداشت شده بود، پس از  تشکیل جلسه رسیدگی به پرونده، به ۵سال حبس تعزیری محکوم شده است.
ماموران اطلاعات شاهرود، در فروردین ۱۴۰۵، طاها نظری را شناسایی و به صورت تلفنی احضار کردند. بعد از مراجعه به محل، این جوان ۱۸ساله به‌صورت موقت بازداشت و تحت فشار برای پذیرش اتهاماتی نظیر «ارتباط با تلویزیون‌های فارسی‌زبان و فیلم‌برداری از اعتراضات» به او نسبت داده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/VahidOnline/76545" target="_blank">📅 17:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mo01mssCP_oOk5BQ3jKu5Sf875FCvF60BO7gepuEZVYt6tm5YPZutlftu-PFNGBwglb3Ju2GIhO7ATTzpbGpcnDnaGUAK0P18y2iAxeOAEzkYYWdHIqGOmzBBHNj_yfL8VVd0c9baAJVzRp1yY-5RGc5NBNzz--kicJUPvvHea1sPQrxYSiEWag2H6elTf6_GDjpOmtaLIOKDt9QkwS83BHpAJwrkJtLCvB9G2VIZqD_ECDq80qXJ6Xt_1K9ooYNq-NAcdK-lArkgvpqQUbTBYygCB-q9Hi2_ZTk3Xqt-fQ5QN8rfLci6coKUTQePpLzMVCCBgX958bw1ahCDzyvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OFxNdjA0pr19Kk5WWLjBRBWkGRUg8UjCZOg4Zue-NAeeQZj7F82fJyW52DVI_irs_7F4BoVdnjCDVlHqxIeWfPcxDm3Xd2DB-iGPlr1vAiXUD7SraiXzpkF8g1sLkVE95VCtOcScwoH0zzxvMw8GqC8xaZm-rcwbs1ZVh7P0oju8D4dKFHMaEmtkZEzOaG7P9XiPDFAeKzRoPvQ7zHJIEZxgCQk36RzVITUhKv4AhdO8zKO8shR10zDHHt_4fHXHOGObAhGld2u5HqVkHHx3L6H6oCNKyTxiZZgYUcI6EnN7CP3nm9CACER4tDLRTmC44ueVGiCXfBjfqqg5k5xJqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 164K · <a href="https://t.me/VahidOnline/76543" target="_blank">📅 17:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76541">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pk2R3nFOu5_041Q2zUrhbs5jE4cxUceFEiznAnm3J8pRYiEFn1uS1LpsvgC2AsidcXb9QypKKerLYRxyaSDMHFXasXXh7nUmiNDzUUI7j1qLoq8yBIzldcB8--_NP8CbgwbxVAReIuHG61EavIuYIXfe8rUE9js0slGo1sI9TY8eCABJVS1mL6dzs8BP0VY29O3YsY2ZWn9tya9GlSIPlkifeiVGaxEBFKw1dP5BRa105Ko4rVyhqdf82bGvdpat669i2vfSPPxkTft3-aEKP77VXY3su3F1zp1YyDJVt5f-LVgnvz5Vmmq54mY9nIGcLrhutkMLsVBl6pq5jnxdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=mJxyShikqEbfTNys2wI4faSvB5k9RLPBuLTHwcUZCIpqLeQ3LzVeJMfYAU0KNE5wHTcJs4_RFD1_wFrt7RGY22aguinHH_injvISTXZvmoDoQqguJWIhjXgLTQlGz0qiyLsCiw9klyCIBNX4lGLHQQ0ztV6Mupy5D2V7KjcYFon_I02ryGnx_EtadA6SUTNwIwKqk3QjUW9RYGgRQpUOUw_6B3HKiM491ZwDgEixSJ4RM6ZJfcVEC-WeZ_qp_8uedc5T14mu59IWeZkXd0OSuHDFW5cX0kGwRRlAgj6jEsKwhwyNoxeZk1Rq5zY1g941F9UKD9cMNF2AMY1OIR1f_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=mJxyShikqEbfTNys2wI4faSvB5k9RLPBuLTHwcUZCIpqLeQ3LzVeJMfYAU0KNE5wHTcJs4_RFD1_wFrt7RGY22aguinHH_injvISTXZvmoDoQqguJWIhjXgLTQlGz0qiyLsCiw9klyCIBNX4lGLHQQ0ztV6Mupy5D2V7KjcYFon_I02ryGnx_EtadA6SUTNwIwKqk3QjUW9RYGgRQpUOUw_6B3HKiM491ZwDgEixSJ4RM6ZJfcVEC-WeZ_qp_8uedc5T14mu59IWeZkXd0OSuHDFW5cX0kGwRRlAgj6jEsKwhwyNoxeZk1Rq5zY1g941F9UKD9cMNF2AMY1OIR1f_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که هاجر نادری، مادر متین پرویزی، در صفحۀ شخصی خود منتشر کرده است او را در کنار آرامگاه پسرش نشان می‌دهد که می‌گوید «من به پسرم فقط یاحسین و تشنگی را یاد ندادم، به او یاد دادم که جلوی حرف زور بایستد»
خانم نادری در ادامه با شرح کشته شدن فرزندش در اعتراضات ۱۸ دی‌ماه می‌گوید امسال محرم برای فرزندان میهن که «ناجوانمردانه کشته شدند» عزاداری خواهد کرد و ادامه می‌دهد که «می‌دانم امام حسین هم برای این جوانان عزاداری خواهد کرد»
متین پرویزی ۱۸ دی‌ماه سال گذشته در سبزه‌میدان زنجان با شلیک گلوله جنگی نیروهای حکومتی به سرش کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/76541" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS2tOkVYFbLEZuEZoImAkqaTYMVdHDMzaF1XtTWgyQTE4n4oPFqRzW2w-drcnR2kceDoAVxfK7zkkLd7vvGKa52sqlQBQAR4tBfaDzlg2H7RhiW3HZjXZHQmthxvkFmA3LNwd_cAQKT9mokfyE9imknkKe7AYJgT0SGqnLKjtkJSGxgtFP4TUimcV603J6KLsqsvNWDgAdbeuPrvYKIhQUaTmQ2SvWwpK-Iz2T7iJQKUcXQmJdD_dlRPUGx-4Q0AJ_jG1EjaLBUDCBRd1rNdIHL-bP6gz9JpopGQ-cVvEcuRtMV1KNg9JWw3_1VOx9SRuGAnHdbY8kN4HMEMlmTwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، صبح امروز وارد مشهد شد.
ایرنا به نقل از منابع خبری در استانداری خراسان رضوی گفته است که او سپس برای گفتگو با مقامات عازم تهران خواهد شد.
بر اساس گزارش‌ها وزیر کشور پاکستان قرار است در این سفر در مورد از سرگیری مذاکرات مستقیم بین آمریکا و ایران در سوئیس، با مقامات ایران گفتگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/VahidOnline/76540" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76539">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBINmQe3JqdTmTmK78YpR0P7vaNgl3MX4FmzKOh6Y23TBSYeDeXQQEQ27piCG4vhrN3C0U3bxrvKI5OZIv1ptJKZC_hgUrFdABad_UONNRN3fzT85uec7X0UBbsEQyOz15jaqKFJRb8C6poKjYYZgJvq0_TIJ4q_FEs8QL-ofEUNftkpNGzks4juAdJmy5D_kvmwHSaBGnheB40NKO6o-zOHfYszrvESgZOBQIUq4j1715ek_2pV8GuddD8P3Ot-e6TGwZpg11LN4PKnYGHwPUeibS-NR7XCnI-UBIxcga_mRB9qBxhEmD6FbsZSyeEEg2y56lmNDvCOeehT4QCozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز اطلاع‌رسانی پلیس استان لرستان از پلمب یک واحد صنفی و معرفی فرد متخلف به مرجع قضایی خبر داده و اعلام کرده است این اقدام پس از آن صورت گرفته که به گفته این نهاد، واحد مذکور «ضمن عدم رعایت قوانین و مقررات، اقدام به هنجارشکنی» کرده بود.
این در حالی است که تنها سه روز پیش نیز مرکز اطلاع‌رسانی پلیس لرستان از پلمپ پنج کافه‌رستوران و سفره‌خانه سنتی در سطح استان خبر داده بود. در آن گزارش، دلیل برخورد با این اماکن، اجرای طرح موسوم به «ارتقای امنیت اخلاقی و اجتماعی» و آنچه «هنجارشکنی» عنوان شده، اعلام شده بود.
در هفته‌های اخیر و هم‌زمان با فروکش کردن فضای امنیتی ناشی از تنش‌های بیرونی، گزارش‌هایی از افزایش تمرکز نهادهای انتظامی و قضایی بر حوزه‌های مرتبط با سبک زندگی شهروندان منتشر شده است؛ روندی که به نظر می‌رسد بار دیگر کسب‌وکارهایی مانند کافه‌ها، رستوران‌ها، فضاهای موسیقی، پوشش و نوع تعاملات اجتماعی را هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/VahidOnline/76539" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=HKE2yK-DxCYH1UF7PyFZrn-u-HV2uB2cb75EweZfekbkkyKGkkYs3WWWQU5mn7GLQ6Co-h9z9rmflwyDmnv37JhmtBHlwBXvkq2YySTKGjurCjj9qw4UjOnSWqdCmt004RfMZdx_-RrTg7QD3y_dkw6WjVmas3hwZBK44J9YqxPXn-Yuss5YhH605YAU25G6oicyHS2nmL6GvBmiz8GcGycl_HPdkTghwOxGZQrZBODRSCwV6tZaqxNqxFVB_l2Cv_UsQRK7toQSLNrqJ1uLMRLBgkhIqYmPn2dKMorb5zsNsgL30gLDcWYT51a2YqGnaRck2KDyZJjnOxc2jPQrkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=HKE2yK-DxCYH1UF7PyFZrn-u-HV2uB2cb75EweZfekbkkyKGkkYs3WWWQU5mn7GLQ6Co-h9z9rmflwyDmnv37JhmtBHlwBXvkq2YySTKGjurCjj9qw4UjOnSWqdCmt004RfMZdx_-RrTg7QD3y_dkw6WjVmas3hwZBK44J9YqxPXn-Yuss5YhH605YAU25G6oicyHS2nmL6GvBmiz8GcGycl_HPdkTghwOxGZQrZBODRSCwV6tZaqxNqxFVB_l2Cv_UsQRK7toQSLNrqJ1uLMRLBgkhIqYmPn2dKMorb5zsNsgL30gLDcWYT51a2YqGnaRck2KDyZJjnOxc2jPQrkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/76537" target="_blank">📅 17:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LUBWtA855mRywBUhHk2WLOJJs9FsX5CnH4OLIdbhDkPRROu2StogQ1DPwTlzxv76ZBd7ymfLmCtvw0GURBPvGfzWqAGOJsNUA2MoG5HtPVH9-H_BYCsNj0Yr0OZHqH-RuI9re-8317C64_M58EDXOqhx7mcOAFX7z2cJFZHsjeJ-o4cJIYBi4qt_vMipwSwXBVQcGMXN7Npw6d2zA19hdfhu4UIrdZo39dPGeDF0VJFOWjs0bfNVza9hjSEybxvZZp7E72KqkNqFwgehLQUVYsIEAxZU8txPfodkNoNMC0-WJMoVtXwrqg3Qk4WFQ4dlxE9HRx8whRNMz2xTFrD-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FqLvkq4H8JMME6dHa9wIOBiB01wwSTZ0abG921s1urdAKAk1XfOwk9uFgqAKCFFRvCcjJ0bS1vKV3z1U48dcYqCBviuslnQ8Y3Nyc5_U8_fbKmzI9JKy8rbNYNeyWUaS4LCrNLlP5wscCXo8mWbgOWtivUXm5Lu42v8gphnUJzcNS_GanQizPjsAqcmZxCUvk8NSfnsKSefkA6Y7vzNfJHq_bg_myHzVgjHt2lqDJf4AeO9LWKAYn-Ik_iaPCoCdDKHKg4mLWXmV8AZiSJQLwfJoBasD5NUKcTsL1FGFvPuD73ziX3YQvPKm8Qg6ocMvxWjoyoNEnvhOY_iL-HZRrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76535" target="_blank">📅 04:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=P3HJ481iz_NXbk7VY1M3vza75psNLnaQfbCajbmPTA0xs-ttUU52gAfEs_mvWjj3BaFY58KA7q6_VJj5pu3cjQTNJShqFmLiaK8riLVyLbBMuDQToAs6IolDn9tQN1N9ItrPhjlglYkyAFm8KJWmFJkltu7RbTuNW2ra2JVC4YHlWH9uUfKOkw4OMmLQCOfaojbpTZ8E8UEwHlOEANFvqqqnDYRHyWmfoGnM9rpR-lzgYvBTVNkGQZYbXF6ce9gKoN1Xlzg07_A1OnukjSIZRtzNMn_1xF7RIi_TXachgDH-aX33clPI0fXyu0_4ZCBDsn-eFuqH7nhbyfjO3gUtAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=P3HJ481iz_NXbk7VY1M3vza75psNLnaQfbCajbmPTA0xs-ttUU52gAfEs_mvWjj3BaFY58KA7q6_VJj5pu3cjQTNJShqFmLiaK8riLVyLbBMuDQToAs6IolDn9tQN1N9ItrPhjlglYkyAFm8KJWmFJkltu7RbTuNW2ra2JVC4YHlWH9uUfKOkw4OMmLQCOfaojbpTZ8E8UEwHlOEANFvqqqnDYRHyWmfoGnM9rpR-lzgYvBTVNkGQZYbXF6ce9gKoN1Xlzg07_A1OnukjSIZRtzNMn_1xF7RIi_TXachgDH-aX33clPI0fXyu0_4ZCBDsn-eFuqH7nhbyfjO3gUtAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76534" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOYbH7m71Gw0xnP3moa5kABoLBufoOQoOuvKGai2hLA_wMHaCut6vtwy299DT88b83otsomaojQxC3bVJX4WUTgfDPis2vHeEqbbKqtX-APOf9MP_hOzNtmUZ1AHxRuVPk0MqK4Fv2f7xHGoXTrMf4d6D2TC1XyLLuC8z2Y8jHwfd_EJHd8O6Dq9np83dTOaneASzgN6tcz_uOKR5aVJf5T5ZiMrgQ7SINN1GvvEDJ-iFSpvclXAzWDBKIdPx8NmRSUYeHH5i_ZLWlOwklANuTMIJy88Jz4Mvv7kU9CrIGsjacKj8DnF3l0SnJRSkZBEcKaEUvz-2Dnk5ks63bF-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا، در مصاحبه‌ای با برنامه «آکسیوس شو» با دفاع از تصمیم خود برای شروع عملیات نظامی در ایران، مقام‌های جمهوری اسلامی را «بسیار باهوش» و «نابغه‌های بدوی» توصیف کرد و هشدار داد که آن‌ها در عین حال بسیار غیرقابل‌پیش‌بینی هستند.
ترامپ با اشاره به مداخله نظامی اخیر ایالات متحده گفت: «من مجبور به اقدام شدم تا جلوی آن‌ها را بگیرم؛ چون اگر سلاح هسته‌ای داشتند، حتما از آن استفاده می‌کردند و با منفجر کردن چند شهر، از جمله در اسرائیل، هرج‌ومرجی واقعی به راه می‌انداختند.»
او با تاکید بر اینکه اگر اقدام او در لغو برجام نبود، اسرائیل سال‌ها پیش نابود شده بود، توافق دوران اوباما را مسیری هموار برای دستیابی جمهوری اسلامی ایران به بمب اتم دانست. ترامپ همچنین با ابراز شگفتی از زمان‌بندی تقابل با ایران افزود: «چیزی که مرا غافلگیر کرد این بود که آن‌ها این‌قدر منتظر ماندند. آن‌ها صبر کردند تا من به قدرت بازگردم؛ البته این کارشان عمدی نبود. هیچ‌کس، حتی با وجود سلاح‌سازی ساختار حکومتی علیه من، فکر نمی‌کرد بازگردم، اما من با خروشی بزرگ‌تر از قبل بازگشتم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76533" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76525">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشجویان متحد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leupyKuypiL9X3JS4SUSEaKPvH8u93b6OCoIw1waWwcY4dkbjv2OOogNOqlNgojKL4mJcCDthPYaOvcYcBy9M9tirtJqshc9EdqQf-fY_J7J2g4quCds4TEsDukyy3A4DRZvxiJLRg42OgaqAn9d1OpgYkAItH2XCpkAr5N3wHjIdr6xcnp7JLwwk5CarkgZAN36iJU7qsi1PMGC0NXMGQs8nAKBfUvv3dzRetXcUxq2Vhg7TdzQz3fUT8x9Xp6CtsGovN2ayzzE_1CaVFWBKZasvZqkkEuiaPWdGYsOekTxr0ScK0UGNCNkXFMhOoIidcONBGbShZNNkuxKQL_VAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiMKOXCcd-cLwem31pxHZ0dDSarPHBS7UfTGH5cn6gH6kgDm2uC1zAAiZ6r2SYup5hQLSZLIO1UCs7_1aIiz99HHkCuSZiX1yf660L9OFOTKmbMMvtYqBCMdKmOzmOg0_ThTVjfkCNkQJTTAKe0_NBArdfztZdi6dLXaUZ-ugpCe3-QsOry2ygMskvIFL584MRuKwwmfLGjPZOQ5NWI4o-ZM5lhm1yNmH4OvRVFn0-qTOHL19Yf7ob9yEYLCtIo1KH2shn_lLp6bnDP6FH7uJ8Ow__scL0bPlW1ZCr0Hu-ZdTI30PTXWnMXtm-mjc4E1_X10wZJ2WWjJDDvo09H_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqAPrIttDUtizLwX8Lf5SAwyU7ENHepE2Ey2oISrGWT9y8Z885SbRxlOQmQ4HjvDTVojgDlpGBgdDdczb9YiKtx4Tr5DfrXJXn9njsnfs3ZcIV2qZoh-0iVSz3hTYhUoHZwtX9UeMONjBpCt7RHUJ1EtDY33SRTHb_FKmBAQAlfJMF5XbjgpHY7GNM4SSesGUSf8EU-UQB994IGr5Ciyd-yk-ODH2bWMGu0aoOLCl6xP4X-f6WZrfaslw6Ygo9-GOby33GZoqsGUaf3GWWlm0_ULg_vzJr73YauIf0YBLYkXYaP7AKsRp0zRQiS9wmEVce4lTuhr2hhraOsChJ2uvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qeQQDlNKPiXPOPvGSzGp00HIQ__nyVNBNzEaQ33xSShkhqpUPmxQaH3l0W8LUSUDMGBU_B3wBx6xaqYpsaug5n95pZrnhm0CjDuBdsWWjOGwm5iwD56jHXZ-DUFpLK0GVCZ3gO1eRkUyhULymVBSdhzUGNJNBD3tUA8CufREn-WzBQiZBFyzPgs9dy2wSzmUlv3QqAU9cY8c-1pKEOpoKd52UCqhBfFe3-M-z6aje5NmqGPuvbjWbSnO8gvkVGbxgX9wALzjwCyIH0k9R409wNB1nSKj0sufLzt6W9LJn7TOXDWBYVQWz_u3A9es8w_Tp7-88GZUb--Ua_yovWIgxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrsFGGgGpYIC5nD-VJ3_dMboZfFc6_fDpmgtqpCEH_PwaFa2-4fAIOHJKHM5RRHKN5mFG_yBVE9xih90rhmzS0bCXvRhAj43ffWjyotBJk2leU81YKFXreiSH00GPS8OWHCaFJVe8l3hoqz4Awzx7sBFKjL44JNAOIW9iInRvKNKblG5MbwvhgHyHOmr3KPNu7S_EQRS7tP_3CQPqa2WFfCn0iBW-hpAv6qQU0c7lsMLZ56A6bwUqOdqpvs2INGtLgE3-2Gc7ESGcqFeoqVf4MI2oJXn8QpRkutxyYVRuKmO-LZXytU1rL3ij20ZCixGTSDaQbzGCbAedU5VSy9RSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oaoQ0G1RK94JjPj7eQrs7UNDTLlSfcWr1YwbrFK1MbbDCrkTbRn6mWMhPap0LMYTW0d-m-wk4aqZm0lYuhHqPQpi3u9Iqu2entTL3luI-zQwmAAtAdDpXzm6Bz5Q8erOlllyeu4oQxsaZaxKomxn8hIkWHmJ9OqHqjFOF7QiXxxGUi22OeZcuBuKlr4hFSAUVou4PHBSVlPQhiqfuV41IEmMGh2uLqa4tM8eu4eWDfh8rK4AdB4VCkRdwLw2RwUiaR5jQlpvusZi1zLE4WwCYkop8lJjpfnUfyTUfoY85uO5S3MAbe8nXX8pJ24TrOMGw_kE-TSWOIiw6bQ3qluyAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JXggxvSfpaYbN1IZldqZAta4H0rgkN5GwiR_ivgWCeRMpc7AabbGXgTfvlLBjuDAT2lhQFmIvaBEwIlA7KwidqI4gvwsQnSgtcmR9C5bzo3SmsZq9yIMxzk7YhvqtLBdEuHIzYhXGACYVomlDlKzfG4NeyicZCecR24KtzEyp6RWn1cg8WVGC-VrDGk9LmXmtwuc7G9CtJDmKjFsoQI-T6890qpdpji0JbiV_wSl2idm6dwFA22emK-4byUqZbcO0Bh7nivxO1kldd-J_aW9SzozbxgMxQER8V6-s19TU8rU5OboGsdeVNlz9_nxnsgyt7QzZZIsVorVsu29OaGWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOiB7xbWfeVvg3IG2vQNkC_SL-CFke6ccc-GoxChwmgzFIJGT6qAFQm3jcmHdXHT-mrJ0Bx0bpFFN29TbKw37rJW2mTi7pC4ZxzhTt7lu61XvtMaJNEYZukzGY_VOysrZ_p0bMVVD2ggbW0tI6osEjoSqNqpDfmQ0zN1hZhQrL3aA4tV5VMs7JpbSr88RamWyOJkD5RFCFmjw7XEUqESFHHh13Xg0vwpnIpzm2NXA1bMdT1OghPX-ui9msrpZ-cAMUwrDXVUfxrbr-PzAuHZT-iq_Tdnh0NFgZcwk98fY3-MyqRrcU5bqVcLaqhZhOHNL1iP0Wa4ziSxplexLMX8zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
صدور حکم اخراج برای هفت دانشجوی دانشگاه شریف؛ صدور حکم غیابی برای یکی از دانشجویان بازداشتی؟
🔻
بر اساس گزارش‌های رسیده به دانشجویان متحد، کمیته انضباطی دانشگاه شریف، برای هفت دانشجوی این دانشگاه حکم بدوی اخراج صادر شده است. اسامی دانشجویان به شرح زیر است:
🔻
رضا دالمن، ورودی کارشناسی ارشد ۱۴۰۳ مهندسی کامپیوتر: اخراج و چهار سال محرومیت از تحصیل
🔻
فاطمه خاکپور، ورودی کارشناسی ۱۴۰۳ شیمی: اخراج
🔻
حسین شادمان، ورودی کارشناسی ارشد ۱۴۰۴ مهندسی صنایع: اخراج
🔻
سپنتا سعیدی، ورودی کارشناسی ۱۴۰۴ مهندسی کامپیوتر: اخراج و پنج سال محرومیت از تحصیل
🔻
مسیحا باقری، ورودی کارشناسی ۱۴۰۲ مهندسی کامپیوتر: اخراج
🔻
فریبرز کهن‌زاد، ورودی کارشناسی ۱۴۰۰ مهندسی برق(تغییر رشته به مهندسی صنایع): اخراج و پنج سال محرومیت از تحصیل
🔻
پرنیان خدابخشی، ورودی کارشناسی ۱۴۰۲ مهندسی و علم مواد: اخراج و پنج سال محرومیت از تحصیل
🔻
همچنین در برخی رسانه‌ها خبر صدور حکم اخراج برای «آریانا کوچکی»، ورودی کارشناسی ۱۴۰۰ مهندسی صنایع، نیز منتشر شده است. هر چند بر اساس گزارش‌هایی که به دست ما رسیده، ایشان در حال حاضر بازداشت هستند و خبری در مورد برگزاری کمیته بدوی ایشان نداریم. هر چند صدور حکم غیابی برای دانشجویان بازداشتی در جمهوری اسلامی، پدیده تازه‌ای نیست.
🔻
لازم به ذکر است از میان هفت نفر یاد شده، کمیته سه تن(سپنتا سعیدی، حسین شادمان، مسیحا باقری) با محوریت فعالیت در شبکه‌های اجتماعی و کمیته چهار تن دیگر با محوریت اعتراضات اسفندماه برگزار شده است.
ارتباط با ما:
@Public_anjmotahed
🆔
@anjmotahed</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76525" target="_blank">📅 22:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=lccinhGmFQI1e26DHn0KdK5miNqqHwBeZZVhIB_VdCtR_kFyHaU8_sUrgOg2ku-digB28a9TeQTF-csRipmaWOzNP8dswsO2GtORlP2RCLV-LkMtYs5I_OrQcq1kJ-05vkCWcEFXI1-3v8EQ9zdVXIWQw464Xeolx4TQrotBX1Zq1-tXkUWJVQdZ6TMwDgMfFoFtDMIBXjv8rHctZzSKLNrUl2CO0zr1DEAImKxc3p2ht9TTXheXb0vOhmTPXvokmw8pTuLs-9HtrAnMgu0NoBenkiqNpWQgB0FY_gR2CtVstwrHUTpqgQrJTZ4KhEvVwbwJilesBE_6bYosycT3uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=lccinhGmFQI1e26DHn0KdK5miNqqHwBeZZVhIB_VdCtR_kFyHaU8_sUrgOg2ku-digB28a9TeQTF-csRipmaWOzNP8dswsO2GtORlP2RCLV-LkMtYs5I_OrQcq1kJ-05vkCWcEFXI1-3v8EQ9zdVXIWQw464Xeolx4TQrotBX1Zq1-tXkUWJVQdZ6TMwDgMfFoFtDMIBXjv8rHctZzSKLNrUl2CO0zr1DEAImKxc3p2ht9TTXheXb0vOhmTPXvokmw8pTuLs-9HtrAnMgu0NoBenkiqNpWQgB0FY_gR2CtVstwrHUTpqgQrJTZ4KhEvVwbwJilesBE_6bYosycT3uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه جی‌دی ونس با زیرنویس فارسی
گفت‌وگو با:
الی بث استاکی، مجری و مفسر محافظه‌کار مسیحی آمریکایی، میزبان پادکست Relatable در شبکه BlazeTV
برنامه‌ای که در آن از زاویه‌ای مذهبی و راست‌گرایانه به سیاست، فرهنگ، خانواده و مسائل اجتماعی آمریکا می‌پردازد.
او در میان مخاطبان اوانجلیکال و محافظه‌کار آمریکا چهره‌ای شناخته‌شده است و در این گفت‌وگو با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره ایمان، خانواده، سیاست داخلی، اسرائیل و توافق با ایران صحبت می‌کند.
یک ساعت درباره مسیحی زندگی کردن
حرف زدند
و ده دقیقه درباره نقش و نفوذ اسرائیل در سیاست آمریکا و توافق با ایران برای مخاطبی از اون نوع
اینجوری می‌پرسه: می‌خواهید یک مادر معمولی چه بداند؟
متن این دقایق:
https://telegra.ph/JDVance-06-19
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76524" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76523">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL9QJXprLXdLlK4YpQCQikn4AqlMhgx1bVKHFbo3R0Kaf-Pt_Xe0SAahxNLxOsAO1gu1ik_8mWsSqP6rdKAS7ZIpxV0hmj_x8andzBRbxCPg3FnehOK-gDzUpt5S24YI1_SATzMKqCQdMv5P1OaDvZDAo7M_4N6lZCeYrglOLVmyXzUqWH0XHvWtQDoGEeveQ5MBz0K3OLYVy_2kShWNnF9d3e5bc7QpgYStMJempfoKqCiifvOtgaxFyoP4Ru_8sCJDSLUdfkyVly1Ffg02ybQiXq8HyoHvioZwmf3RD_Phy6B21kSYcUoZARDBDQCUoGcfoFSqBUaYGSqDVmn0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در یک گفت‌وگوی تلفنی با شبکه ان‌بی‌سی نیوز گفت که روز جمعه با مقام‌های اسرائیلی صحبت کرده و از آن‌ها خواسته است با گروه حزب‌الله بر سر آتش‌بس توافق کنند.
بر اساس مطلبی که خبرنگار این شبکه در شبکه ایکس منتشر کرد، ترامپ به این مقام‌ها گفته است: «بعضی وقت‌ها فقط باید آرام بگیرید و از عقلتان استفاده کنید.»
این خبرنگار همچنین افزود که ترامپ مشخص نکرد آیا مستقیماً با ‌بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفت‌وگو کرده است یا خیر.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76523" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VsYSdJ-sbliRY82F5tPZX1bp4U-Rzuy7s5AnG8qL_oz3VV021e882dYDE2F-TW8Yn9-HqDEngXydYLHzMkmVUcDb16H9X6aYDr_xyiMCOuXJ9ZN8t8liRhxnl4dGau3Yw4-VUFMGKGklFHlTyV5qw48pY7a5pFhVGTbZcWQhnkC6eoXYye10wi6xVx5NfCKWaQ-xkCBbUX-d8nlgnZKjiPUdLGHP4J66snXWdUX7mVldwAFTh4Hc3nMzatX9tgVBPL52NcfDF8gT2fRPsXulVhDPMnGS9PiDCzim8S3RIjg609QnAljJzUlupfR3WLy08I6P-Cs7G3tk23cK9LLlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
او تحویل سلاح‌های حزب‌الله را رد کرد و افزود این سلاح‌ها برای مقابله با اسرائیل هستند.
نعیم قاسم همچنین گفت که ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
دبیرکل حزب‌الله لبنان ادامه داد: «ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76522" target="_blank">📅 20:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76521">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1yYW8T4BS9ddyg2v7HXBnS6VXSIDqu-QIu6OJMaJx-yrD6jYItWfliY8pUNGQ15Pk0Jt5k-yJ_jeNPrXGtIeHxi5nYk6gSBErZ0BsUCBlBQfVglWyppDSaI4XhFfPoezl6NG3fpHCMKu-KzwZXZd-yRQ6HcEpZtUjAuj_H8X2ScSQWAWl-GDbtAklNERS5Y_xD8NzhUP2ks3oheQQOklRjYMxiFyoLS38_fEziawpZrL0xH7svg3heE89xNM2azjyXVKbdnwlX0wYxX142UkVal5Ucvai7mu_-GfS0Q_mRHejh7ttANpEmzBnO8H6yaJVi3RTbaTUgWtLWX1IcXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه ایران، روز جمعه دعوت جمهوری اسلامی از بازرسان آژانس بین‌المللی انرژی اتمی برای حضور در ایران و انجام بازرسی از تاسیسات هسته‌ای را رد کرد.
او گفت: «بازرسی از تاسیساتی که دسترسی آژانس به آنها به‌دلیل حملات نظامی متوقف گردید، منوط به روند مذاکرات و نتیجه آن خواهد بود.»
پیشتر جی‌دی ونس، معاون رئیس جمهور آمریکا پس از اعلام توافق اخیر در گفت‌وگو با شبکه ان‌بی‌سی گفته بود که بر اساس تفاهم‌نامه میان واشینگتن و تهران، بازرسان آژانس بین‌المللی انرژی اتمی «قطعاً» به ایران بازخواهند گشت.
اسماعیل بقائی همچنین گفت در حال برنامه‌ریزی برای برگزاری یک نشست طی روزهای آینده هستیم.
نشست بین نمایندگان ایران و ایالات متحده که قرار بود جمعه در سوئیس برگزار شود، لغو شد.
سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد: «با توجه به اینکه امضای متن یادداشت تفاهم در بامداد ۲۸ خرداد به صورت دیجیتالی انجام شد، برگزاری نشست مزبور در سوئیس فوریت ندارد.»
او همچنین گزارش‌ها درباره بسته شدن تنگه هرمز را «بی‌اساس» دانست و گفت کشتیرانی در این مسیر در حال انجام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76521" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76520">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw2Uv7F5qZDRkV00A50M_Fy2CCCHjq2YOCyVPyht4wy8E1b-ilVGDGwLshyhEbPrKKZ3ZLStLYfEDxaIvf86CB0KNKI6-ydAyslf_gm3VM_hxoAWfN1TPSLEh4DCkrGrkLcJf2WQkYgca6DcXn9R1gHPwUuItoc9dl_1tmkjuY0rkqNy6H-GR2GAwdw0vpEVfJyvUrIF9YlxlSPSLYfajLWUAaqo39ZBaXkrb9LAmju7xwBgSEDlDAosDaCdpVeRzXkDffUPHr9uNTxfH4HimRk_w9Qd1zXIjHsFvJlbs435buUTbGH7sqiamelUP43jbxWgKGex_-erTtHfTbtBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز گفت که اسرائیل و حزب‌الله بر سر یک آتش‌بس توافق کرده‌اند که قرار است از ساعت چهار بعدازظهر روز جمعه به وقت محلی آغاز شود.
این مقام که نخواست نامش فاش شود، افزود که مذاکره‌کنندگان آمریکایی و قطری با کمک ایران این توافق را نهایی کرده‌اند.
این مقام همچنین گفت: «درک ما این است که پس از تبادل آتش امروز، اسرائیل و حزب‌الله اکنون در وضعیت آتش‌بس قرار دارند.»
شبکه العربیه نیز به نقل از یک مقام آمریکایی از توافق برای برقراری آتش‌بس بین اسرائیل و حزب‌الله از جمعه خبر داد.
این در حالی است که نخست‌وزیر اسرائیل ساعتی پیش اعلام کرد نیروهای نظامی این کشور تا هر زمان که لازم باشد، در خاک لبنان باقی می‌مانند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76520" target="_blank">📅 17:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQt893MeVDgLUOH7Zi3uv4bUN0dqhmb-ubf4dq2FgxsDLVH2S0fKHza59QrbG3c0AEy4V8gw8CUgfmMHwUKLZ9Dtj9GO20I-BKajMrcEDd7LFAe3pjgg3s0jpRgjE0oN0Wh2LCvrvfR3j8jQmcSQBD9YPYoB4LyjVGk-QmwUq7hBufS8IzJMbXPnlTrRRecR2iR7yROysxkU5R14mSx_Etr0C3a_Nr18JU06nZQRDPf7QFVQr_PzZkEq3IAzSGHzyytMmZ7XZ5_eLeqcCcyr93sO_rdf-hNq2M5JgVZBJ_W0vxDpQdF7oUvkqjt1lEm6Y-WpTEOhA-LAZOeh0JBlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957528437f.mp4?token=D_uzNwjXSEDjIquetnV_Uyk8jG-dM19HfVkRlKy1qAuvMeLgHHBooZD2eZAAbNlRxw_6URU45oFIvsVE5tT8tE70yH9b2oG_W541iENjMBqVXi1bJDeKqQAlQEJf1maPJAp5IYOv7Uq09S_c89Lo3jR3Pug4V1tnbFQG2unnV1ZY515awOtaY-FZbFpmMuXf3OFvFRX2RtTRcBG0C72Qcsk5U3hirSnE80RMZ8nJbdBExldzzkvSUiuUpNN4YAfIdUEsOGkZ3YpAPr4-TZV5EzbACXKAT5hGxcnK_xIC7q5IQZCFWCC2lYkpnI5KwuKBURNEHCxkZ5uqDp8Qgyx2yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957528437f.mp4?token=D_uzNwjXSEDjIquetnV_Uyk8jG-dM19HfVkRlKy1qAuvMeLgHHBooZD2eZAAbNlRxw_6URU45oFIvsVE5tT8tE70yH9b2oG_W541iENjMBqVXi1bJDeKqQAlQEJf1maPJAp5IYOv7Uq09S_c89Lo3jR3Pug4V1tnbFQG2unnV1ZY515awOtaY-FZbFpmMuXf3OFvFRX2RtTRcBG0C72Qcsk5U3hirSnE80RMZ8nJbdBExldzzkvSUiuUpNN4YAfIdUEsOGkZ3YpAPr4-TZV5EzbACXKAT5hGxcnK_xIC7q5IQZCFWCC2lYkpnI5KwuKBURNEHCxkZ5uqDp8Qgyx2yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه ایتالیا روز جمعه اعلام کرد در واکنش به گزارش‌ها درباره اظهارات دونالد ترامپ سفر برنامه‌ریزی‌شده خود به ایالات متحده را لغو می‌کند.
آنتونیو تایانی در شبکه اکس نوشت: «سخنان شدیدا توهین‌آمیز رئیس‌جمهوری ترامپ… به همه مردم ایتالیا اهانت می‌کند.»
به گزارش شبکه ایتالیایی «لا۷» ترامپ درباره دیدار خود با ملونی در نشست گروه هفت گفته بود: «ملونی آن‌قدر می‌خواست با من عکس بگیرد که فقط از روی دلسوزی با او موافقت کردم.»
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، در واکنش به اظهارات اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا، این سخنان را «کاملاً ساختگی» خواند و گفت از نحوه رفتار او با متحدان «مبهوت و شگفت‌زده» شده است.
او تاکید کرد: «نمی‌دانم چرا رئیس‌جمهور ایالات متحده این‌گونه با متحدان خود رفتار می‌کند» و افزود این نخستین‌بار نیست که چنین مواضعی از سوی ترامپ مطرح می‌شود.
ملونی همچنین این رویکرد را «مایه تاسف» دانست و گفت او قاطعیتی را که در برابر دشمنان غرب نشان نمی‌دهد، در قبال برخی رهبران متحد خود به کار می‌گیرد.
نخست‌وزیر ایتالیا در پایان تأکید کرد: «یک چیز را باید به خاطر بسپارد؛ من و ایتالیا هرگز التماس نمی‌کنیم.»
در ادامه این تنش‌ها، آنتونیو تایانی، وزیر امور خارجه ایتالیا، نیز اعلام کرد سفر برنامه‌ریزی‌شده خود به آمریکا را لغو کرده و این اظهارات را «توهین به مردم ایتالیا» خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/76518" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ1Wglo54potyppZpKDLclbLgxznmErF4zOy8jbRbKHESR8ijJGADGAOB6IC6GlNkizfgBrwmVx7RKHTuPPyuJzpF4pIhLzomtLOYFxxnLz7oofdSwyhQYWeWj8MqlkGoCmlg7SWJR_reWUbyghlpS7bVOIpdjIIFiGrdPqjA2ZXsfW-6XcpoVjbBVi8i10yndXUor5D7-hbsO2ir3A-zLvRajNmqDLctP-Jnx_WIettXfh3oB5knz9s7IPObveWb0UGtAB-x_2Zgu_d-no9YsaMeCuMX7OxIn8pFI5jn18o6qRydEyce4Sr2JohYjeq-2Azm_CA99OV7TQcKXS0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅️
#محمد_نوروزی
، شهروند افغانستانی ساکن ایران، که در روز ۲۵ دی‌ماه ۱۴۰۴، در منزل مسکونی‌اش دستگیر شده بود، توسط دادگاه به شش‌سال زندان محکوم شد.
🔹️
طبق گزارش رسیده به کمیته پیگیری، محمد نوروزی پس از بازداشت به آگاهی ملارد منتقل شده و پس از ۴ روز همراه با ضرب‌وشتم فیزیکی به زندان قزلحصار منتقل شد. او طی این مدت مدام تهدید می‌شد که رد مرز شده و از ایران اخراج خواهد شد.
🔹️
او در نهایت با قرار وثیقه یک میلیارد تومانی از زندان آزاد شد و سپس توسط دادگاه به اتهام "اجتماع و تبانی و تبلیغ علیه نظام" به شش سال زندان محکوم شد.
این حکم هم‌اکنون در مرحله تجدیدنظر قرار دارد.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76517" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76516">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuvYVw5gk58UXhgF-EsqNuKVdFm10RmB-50BpEU2BEOvRSAwwxIqo0Y-qev8EdzzSydl35vEM_WCEcqJ0OCWjgzufG0qGBtfqwRgownBQoqSB6VWGGu6Dso5m6Q5Px0WmvCXnLKrLe9q6J60NLUg5MqB0owrx9E3sbgQ2wOHKDu2hvxdEM7kvBvZNfJA01bNdgckDAvfHmMu_f8nOd49CJtt9qNjQFRXVULIy725uo17z6Hmc6iwy1o5NFyhHAIj-Vpx_W5DQknhYt98_cNwlMjqwi04w1vXN7UNbKFcONqCujZp5NmsZSNoI09L1P344D_ft0sPLfNh47yIpCf0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز جمعه بار دیگر گفت که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در لبنان باقی خواهند ماند و وعده داد که حزب‌اللهِ مورد حمایت ایران برای حملاتش «بهای بسیار سنگینی» خواهد پرداخت.
او روز پنجشنبه، ساعاتی بعد از امضای تفاهم‌نامه پایان دادن به جنگ توسط ایران و آمریکا، نیز بر ادامه حضور ارتش اسرائیل در مناطقی از جنوب لبنان تأکید کرده بود.
نتانیاهو در بیانیه روز جمعه که پس از اعلام کشته شدن چهار سرباز اسرائیلی در لبنان از سوی ارتش منتشر شد، گفت: «اسرائیل حمله به سربازان یا قلمرو خود را تحمل نخواهد کرد و بابت این حملات بهای بسیار سنگینی از حزب‌الله خواهد گرفت.»
او افزود: «اسرائیل تا هر زمان که برای حفاظت از جوامع شمالی لازم باشد، در منطقه امنیتی جنوب لبنان باقی خواهد ماند.»
یسرائیل کاتز، وزیر دفاع، نیز گفته بود که ارتش در لبنان خواهد ماند و افزود که به هر حمله‌ای «با نیروی قابل توجه» پاسخ خواهد داد.
لبنان اعلام کرده بر اثر حملات اسرائیل در سراسر این کشور ۱۸ نفر کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/76516" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76515">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mJ1xnFthtTvsVtNk8pKlMEGHnVr9DoQofFTU1Qk_3pcNXass2sdebTUDYpe3v-gH9sfJx-t7B-fgY9-EFjBe60EJXR39uGOQ96KvKeiug8YsdHQ1VFZ3acqwbP8Q9YKOVHwPpcpJ4K0Mjv_IuMQXbYXQsmgsTETj-fpOYr0XJKeerxpFZdLQOIe2NqH8GHQ40HvA4sazfplS9Gq11ZtI9NoOnJf9Ep-vIcLTtL5k32sbwlMjMLBcxdLoFtiJdok3eaWS1Wz14F7DJRrT6_TCmMOSkUf1F20hlHEroYM2SASElWo52VsZS_sLcMZCYjuWK6XBFrhLuSl4KnE5GAoiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینعلی شهریاری، رییس کمیسیون بهداشت و درمان مجلس جمهوری اسلامی، در گفت‌وگو با دیده‌بان ایران، با اشاره به ادامه «تعطیلی مجلس» گفت: «مجلس را بستند تا هر آنچه خواستند امضا کنند.»
او با تاکید بر اینکه تفاهم‌نامه با آمریکا در نهایت باید به تصویب مجلس برسد، افزود: گذشت آن زمان که برجام را در ۲۰ دقیقه در مجلس تصویب کردند. ما یک بار از این موضوع آسیب دیده‌ایم و نباید دوباره همان اتفاق تکرار شود.
شهریاری همچنین از اظهارات عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره احتمال رقیق‌سازی اورانیوم غنی‌شده انتقاد کرد و گفت موضوع هسته‌ای نباید در مذاکرات مطرح شود، زیرا به گفته او «جزو خطوط قرمز» جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/76515" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/msRQVbJZtgabg08UffQKN-k2PRjwRbnT2HfS0v7F-oo3lNdjjd43yMN9PQkdCKwJu5aiNE1C-rURN3Cv9RTe6TiU1osc3DwuDpr9pb-3D0f0T-TjpMEz1iuvj4Ae_docV2lit7vF-C5sfdT1AS6GpRx44Re-1AwxwXpAqJVOrSS-MGTQkzK76g7tOvmo8R3EEOwIOqMs1urb-zY_2h6EIZSmtGNSDyv6lF61enYi_KERhtO70JRuymUtiFoHwPPFu_hEqJ9c1OjZ4f9nzGBmyqsnqAQnUQKQrOCDIntSeuWEMJZ6c-_GHQ2dI_0GUSRhtSDy6hn1kxedpi8FuA3Ccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام پیشین مرتبط با تحریم های ایران درباره «صندوق ۳۰۰ میلیارد دلاری»: پیش نیازش لغو همه تحریم هاست که دکمه روشن و خاموش ندارد
میعاد ملکی، مدیر پیشین «دفتر هدف‌گذاری تحریم‌های خزانه‌داری آمریکا» در یادداشتی درباره موضوع «صندوق ۳۰۰ میلیارد دلاری» برای ایران که بسیاری از کارشناسان درباره آن ابراز تردید کرده‌اند، می‌نویسد: با کنار گذاشتن موضوع معافیت/مجوز نفتی و نگرانی‌های مربوط به عدم اعمال تحریم‌های جدید، باتوجه به الزامات برای اجرای واقعی بند ۶ (صندوق بازسازی ۳۰۰ میلیارد دلاری) و بند ۷ (لغو همه تحریم‌ها) به این نتیجه می‌رسیم که مذاکره‌کنندگان آمریکایی یا می‌دانستند که توافق نهایی ناممکن است، یا این یادداشت تفاهم فقط تصمیم‌گیری را به آینده موکول می‌کند.
ملکی که خود در طراحی تحریم‌ها علیه حکومت ایران نقش داشته در این یادداشت می‌نویسد: این چیزی است که «اجرای کامل» در عمل، فراتر از امتیازهای هسته‌ای، به آن نیاز دارد:
بند ۶ — صندوق ۳۰۰ میلیارد دلاری:
صدور معافیت ریاست‌جمهوری از تحریم‌های الزامی بخش ساخت‌وساز ایران طبق ماده ۱۲۴۵ قانون IFCA (معافیت‌های ۱۸۰ روزه قابل تمدید که در هر دوره نیازمند اطلاع‌رسانی به کنگره هستند).
خارج کردن سپاه از فهرست سازمان‌های تروریستی خارجی (FTO)، زیرا در غیر این صورت سرمایه‌گذاران با خطر مسئولیت کیفری به دلیل «حمایت مادی» مواجه خواهند بود و هیچ مجوزی این مشکل را برطرف نمی‌کند.
استفاده از معافیت مبتنی بر منافع ملی در قانون ISA (قانون تحریم های ایران) برای سرمایه‌گذاری در بخش انرژی و نفت.
در نتیجه، هیچ نهاد سرمایه‌گذاری حاضر نیست میلیاردها دلار سرمایه را بر پایه معافیت‌های شش‌ماهه قابل تمدید متعهد کند.
بند ۷ — لغو همه تحریم‌ها:
ماده ۱۰۴ قانون CISADA (قانون جامع تحریم‌ها، پاسخگویی و واگذاری سرمایه‌گذاری‌های مرتبط با ایران) رئیس‌جمهور اختیار معافیت ندارد؛ تحریم‌ها الزامی هستند و لغو آن‌ها مستلزم تصویب قانون جدید در کنگره است.
ماده ۱۲۴۵ قانون NDAA (قانون مجوز دفاع ملی آمریکا) معافیت‌های ۱۲۰ روزه قابل تمدید که در هر دوره نیازمند ارائه گزارش اجباری به کنگره هستند.
تعیین بخش مالی ایران به عنوان «نگرانی پول‌شویی» تحت ماده ۳۱۱ قانون پاتریوت: این موضوع نیازمند مقررات‌گذاری جداگانه از سوی شبکه مقابله با جرائم مالی وزارت خزانه‌داری آمریکا (FinCEN) است و صرفا از طریق دفتر کنترل دارایی‌های خارجی (OFAC) حل نمی‌شود.
تحریم‌های مرتبط با تروریسم، حقوق بشر و موارد همپوشان با پرونده روسیه: هر کدام مستلزم اقدامات حقوقی مستقل و جداگانه هستند.
ملکی در ادامه می‌نویسد: «لغو همه تحریم‌ها» یک دکمه روشن و خاموش نیست، بلکه پروژه‌ای چندساله در حوزه قانون‌گذاری و مقررات‌گذاری است و کنگره نیز در آن حق رای دارد. و این پرسش مطرح است که چگونه می‌توان اتحادیه اروپا را وادار کرد محدودیت‌های مرتبط با ایران را که در چارچوب پرونده‌های مربوط به روسیه وضع شده‌اند، لغو کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/76514" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76513">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfPXY4LKXYkr_Zb58-uD1HF8SzbksUeqP_xnzIBBCM3Sb65atDX-r-oQfotQ6eE3Qod80ck5XSJG4lPWbAcw1DHrAUFveFNVnfeKSZ03b2KjGwbojpO9wQv88Xc2U-Ty9gGEMKiDr31qH12WPIwe6WskR_-xlF48Q5RfjvXn5hj_umHdEl-RDspk2n2_0z1K9lI-HXqyITN8rqGwEmZ_6_9zcno5YmGuqtC-zsgpHE0bJe9BeP6EuTv2eGRkCG_lSVxPLyhbltCTQOlEq6UFgQaIR49mZMSy0CpvX60_fELoEevEx701_SXTG5NeUr0qnqkF4Zmr9ddvCGQer9-x2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه هاآرتص در تحلیلی نوشت توافق دونالد ترامپ با جمهوری اسلامی، برخلاف انتظار بنیامین نتانیاهو، نه‌تنها به تقویت موقعیت سیاسی او منجر نشد، بلکه شکاف بی‌سابقه‌ای میان واشینگتن و تل‌آویو ایجاد کرده و نخست‌وزیر اسرائیل را در آستانه انتخابات با بحرانی تازه روبه‌رو کرده است.
روزنامه هاآرتص در تحلیلی نوشت نتانیاهو امیدوار بود سفر ترامپ به اسرائیل و حمایت علنی رییس‌جمهوری آمریکا، مهم‌ترین برگ برنده او در انتخابات پیش‌رو باشد.
به نوشته این روزنامه، نتانیاهو انتظار داشت این سفر پس از «پیروزی کامل» بر جمهوری اسلامی، سقوط حکومت ایران و انتقال ذخایر اورانیوم غنی‌شده برگزار شود، اما اکنون نه‌تنها هیچ‌یک از این اهداف محقق نشده، بلکه ترامپ تقریباً هر روز با اظهاراتی تحقیرآمیز از نخست‌وزیر اسرائیل انتقاد می‌کند.
هاآرتص افزود توافق آمریکا و جمهوری اسلامی در اسرائیل به‌طور گسترده «فاجعه‌بار» تلقی می‌شود، زیرا ترامپ برخلاف وعده‌های اولیه خود، جنگ را بدون تحقق اهداف اعلام‌شده پایان داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/76513" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76512">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxfqJGif1QkblcLVUy8xIj9YCFJbF9N1UtgEJM1j0Jjcwv82oEJs_uBZQ_zpmENZuGfpUrapawpLLs99BlHOQ01HPIlcXnX66aQrLKxjLfrFKVDHM-2IBgp4_nNCNZYm0nzhGaSir-3GH_Jq1EQief3NfMJg1Q6xHa1jOyk08VShllOyulI764NUTlYlLx39_y07NCWYayEr-bwdI9rTYD7aMAVAxOR8CQe31Z5uwFdQhPbb0WZhbci7hAen0VmUeZxCQddXDMLINngHfh272oXZhhnIqp3pJVg6xfaXF1N1LQiV8Iq0gz_-9UhCXo_9bTGMmhXB2a9scTgV8pflXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«معین بصیری» ۲۱ ساله، ساکن شهرک اندیشه تهران، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله از نقطه‌ای مرتفع و از روی پشت‌بام شلیک شده و به قلب معین اصابت کرده است.
او در پی این جراحت جان باخت و پیکرش پس از انتقال به کهریزک، به بهشت زهرا منتقل شد.
نزدیکانش می‌گویند پیکر معین بصیری را از بهشت زهرا تحویل گرفتند و مراسم خاکسپاری او روز ۲۱ دی‌ماه برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/76512" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76511">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RzlVOwYubVkMdLM7ECzZ1sWmkCdmgZOZRq2Sm-E4L-rtxDflVir7_bENSBv7EIQvI87EIjD6GkPrnzPeo_TVV4fDVMq_1uTSi5QHSb_WZS01fgQvgk4tNIGPZBt6DGYmv9tgnAOgcyimU4IfmSQG3ATYs8HLJsOQ6jED5u1T8A0E3BG30ZFIYI-5SxuKCxpZ5CHjiuxun-lRg9KZRrUSyan_BRfbYqBiIqrOUsYcgAXeEk6YeO_LLodKunP36IKWqW6fEAXFyU_k9A4ey5SvBMJXI_lMze8hQdLkvJ8NMb1SxZOWvYcQh9hQnLgoO5E7X7rRbb_zN7BOdSOp87I1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
«جنگ، ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات ضدهوایی، نه رادار، و عملاً هیچ چیز دیگری هم ندارد؛ با این حال دموکرات‌های احمق می‌گویند ایران الان از چهار ماه پیش وضع بهتری دارد. اصلاً می‌توانید تصور کنید کسی با چنین حرفی قسر در برود؟ بعضی‌ها چقدر می‌توانند احمق باشند؟؟؟
رئیس‌جمهور، دی‌جی‌تی»
realDonaldTrump
«ما از سرِ درماندگی دیدار نکردیم؛ ایران بود که از سرِ درماندگی آمد. کارشان تمام است! این ۶۰ روز را هم طی می‌کنیم. هیچ پولی گیرشان نمی‌آید، حتی ده سنت!»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76511" target="_blank">📅 17:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IQgisxs6DYKaFlBiVbcJbRBty_JBm681hrI-UOvOuYMM1zsOh2XQCBkULdeo5IdlGnUSgvQP3IMqfEcjsdskDGo7-djjMPxokMZvGty4YIYnYIdemJbFZhzHuSPOJep7S_bJGgefRk2sfO9VX-jpA_au0lsOG_3W2KD0AJVPA5sq9XvJxtKbaDNyNTge_Vj2pe2f-a6IuEKtaE_Gs2eJYJ2JelnbyYY-0alA_Omi9mwNIVuX3FV5sgvMuq_Yv7eMzpnOVDuNxDmSiMC443b0-qhG2_ox3HCgl4xW98vLe8WKMC1awjwkd4rDngDvUIeajnDtjlERzZj_Ke-V-0fINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MF418VbvNhEv-hbGjz_SaQY4YFCx8lHr6jIXPTMsobfJ35EfmTghhtUXzwsHma-ypRXE-Ra4mF9S7fTrMad_vC6OYv67Aj3GLk4Hd2_um-ZtlAoWZjksdMkodi-xkchO0EJoAPCEVYqB2kcLCkIYBVUbJMG8L0P5GmrB-xgJUVMUHknrRlE_DZEsuZ_I4Srdj2UBVk8Xp8l7PiGA22kVo8y2POUSbRluiMrnyfnkogGhl8Nq0PhMbia-c6kyooyJGtGnXQDASpRljJIQ0CHyBVEYlYqlAmBb1AOAYqPG_5QCxpqiNrbBTNZlDlEzREBwmUsE9RdM3rk3pcPkCU-1sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر خارجه فرانسه می‌گوید پاریس تا زمانی که اطمینان حاصل نکند مذاکرات درباره برنامه هسته‌ای تهران انتظاراتش را برآورده می‌کند، با لغو تحریم‌های شورای امنیت سازمان ملل متحد علیه ایران موافقت نخواهد کرد.
ژان نوئل بارو روز جمعه ۲۹ خرداد این موضوع را اعلام کرد. فرانسه یکی از اعضای دارای حق وتوی شورای امنیت سازمان ملل است.
بارو گفت تا زمانی که مذاکرات آمریکا با ایران به ابهامات مربوط به برنامه موشک‌های بالستیک جمهوری اسلامی و حمایت تهران از نیروهای نیابتی پاسخ ندهد، ثباتی در منطقه برقرار نخواهد شد.
او افزود: «ما به یک تغییر اساسی در رویکرد ایران نیاز داریم.»
@
VahidHeadline
وزیر خارجه فرانسه: کشتار معترضان دی‌ماه را فراموش نکنیم، مردم ایران بزرگ‌ترین قربانیان جنگ بودند
بارو که با تلویزیون «فرانس انفو» مصاحبه می‌کرد در پاسخ به پرسشی درباره سیاست فرانسه پس از «امضای تفاهم‌نامه پایان جنگ» ایران و آمریکا در قبال تهران گفت: «مردم ایران، بزرگ‌ترین قربانیان این جنگ بودند. آن‌ها از یک سو گرفتار سرکوبند و از سوی دیگر به رویشان بمب ریخته می‌شود. ما کشتار ژانویه (دی‌ماه) را که در آن خشونت دولتی بدون تمایز، معترضان مسالمت‌آمیز را هدف قرار داد، فراموش نمی‌کنیم.»
فرانسه حملات نظامی آمریکا و اسرائیل به جمهوری اسلامی را «غیرقانونی» توصیف و بارها اعلام کرد که در این جنگ شرکت نمی‌کند.
دونالد ترامپ تفاهم‌نامه پایان جنگ با ایران را در کاخ ورسای و در حضور امانوئل مکرون امضا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/76509" target="_blank">📅 17:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX3eBEhOIvX4XSRa0duaFllL779Tf94TmD7SdAxvxCN1CmbdD1MNCRkvZgCQXcTuHfNbIF1KwECttjmpHfeHkik5_BsvVuTHH2CXz6A_r3a5pogA5bmtr06c5kixbqLTV_2Rnzf3AT6kPIlRTM3eNBlpksxRwJs_SedpgTzniTLpSuZscmMDwwMY_FKqU7NyuvDQY1_4dWd32OR3AU7zEOLXHwSJ5HD87j1eDfKCu2x788qLwEtTyYRRl0_ZI7bkhNWkQARNsegwINneyPYyKj6GPrPhO-gzjFyT8PiywvHZpi4GJ-kUW4GPlM3By73_Fa1PjkiVNxq2GvxfCq7R4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال از قول منابع آگاه گزارش داده که طبق توافق پایان جنگ، ایران حق دسترسی به شش میلیارد دلار منابع مسدود شده در قطر برای واردات اقلام انسان‌دوستانه و غیرتحریمی از خود آمریکا خواهد داشت.
به گفته یک دیپلمات آگاه از جزئیات توافق، این منابع مالی به‌صورت مرحله‌ای و در بازه زمانی آتش‌بس تمدیدشده ۶۰ روزه آزاد خواهد شد و تنها برای خرید کالاهای آمریکایی قابل استفاده خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/76508" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twgTKmg2xLWF5T6A3tQvga_hjQuNiYvC3i7yYfjX_i1uopsidsqxF-lv2-p20iU-9LCKMoob0-E1EuaRDAR1V8lLgxiIU9zIAWg390c9QW-HO8N2TP0XB_SVLY702Tni3lPgyF9s3nekAVanXfjlSwb5cKWGkTbz64-XEAeNssD-k8iqK1PlSo7G-F0HG6PtMEIucTa6Eh8yk5uFTgbt2oK9-ws-DccaPIZpu_IXkdFmA-WF6zn-vFoF4vldFnglgNvzbB7NZ1545PYC2k8AL_GBold8BDdJznFIfbdYOl7gbiREwhjeM9nQ2KTXD7e-XFzJH0ipdgjQ4vxrNUH3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ob1Lg9z1gOZMZuSLvnYH9xlPN6HJj2h_q56S4_mqrv11FVSMVnlEKOzIETQuQlDdnwcFJ2Md_AaZum3ootLXzH9eePcRNk5h7lG3H8zGbug9grDgwtvNQ65Nlx6PwWTmfPLL7sKJI1NJ44_RF4c6I0V4Zyxb1oj-ZdU1QlksO7Df51KGVTbmMl48F0p993iI9ss8IvoHl1MCUE3nGg2ZQmNLiK1Ml1KTOCwt0jw9fzcmxUlTWRbEgwak5hd-LLI3bYk_Qexvbjbx0xX-EZrwcItMeZAKNCzfNHd8ceLKjqTAFUSTdMBRHjN9vdCX4nhnXtQDdcWZa_oQ3qRMG6WFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oIwB1e-w9lPiseEVLA_QpboZpoEVVNMNWSimUn5JEyQHgww_XDQHHsNvXV_kgj6A3fScMGL9EW4T_Jtw6ISsusN0khqOXcdpRMvN1NWVlZfeFWh5t-QEf8--Gcxu5E40RsHJtLCOq0KDaLhzP97ZLfvVNrE_MM-6UZuP6slm92PI9lgEs9PIuRVQVxdzamWHOKoCCg5laPRr3qGSeJKp9SLKqfkNnCHpMqqQvrwm_9xvO_txNXWjKKQAwQTMUeq1KlYMmIGJxpQFRvth9wLXzm1Ek3K2L2W0CAkmIovKABb4ShUe2bO48pOamqs7_rEy5pgsJB86n1FpjFbSHL_gYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بيكر علی حسن‌پور را بعد از ۱۰۴ روز به خانواده
‏تحويل دادند
‏
🔸
⁧
#علی_حسن‌پور
⁩ در ۲۵ خرداد ۱۳۸۸ در خیابان آزادی تهران بر اثر اصابت گلوله به سر کشته شد. خانواده او پس از ۱۰۴ روز سرگردانی، سرانجام پیکر وی را میان اجساد مجهول‌الهویه پزشکی قانونی کهریزک شناسایی کردند.
🔸
اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است.
🔸
علی حسن پور یکی از این افراد است. سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/61687/ali-hassanpur
@IranRights</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/76505" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veuGmxdAYOIMl9YUT9rNqRX9rVMsv0YdthXTghQUl7Vl4o0ggvONXm12hUy-pG98YSjJ7Ab-h5gvaB4j-AeWvg-_7aBIpPuodbiRXF8QmKQtTXXX_WEgD9IqQvQpEO5q-AOztTZGicXudJdA80It3lR63x_GxdKe3-26Vtx7jccfPZLNxk1gW-9ITLi6WGmH5oKci8B0ksvsIpLp8DbesJWP8hUdnyNherSYg70fG1Sdd3lAOc8xKPGNpDAra6Hj-r-8Y3F276XYnsYaIO9f3QsmHvlfZimYmiTlWRM_ElrbyG7-9ycYLPJLa0fbfkJDEnQhB3UNJdCg86je11_62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ملی لبنان می‌گوید در حملات اسرائیل به شهرک‌های شرقیه، حاروف، کفررمان، کفرجوزو کفرصیر در جنوب این کشور دست‌کم ۱۶ نفر کشته شده‌اند.
به گزارش رسانه‌های محلی لبنان، از ساعات اولیه بامداد امروز، حملات توپخانه‌ای ارتش اسرائیل به شهر نبطیه و مناطق اطراف آن ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/VahidOnline/76504" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZr4RH0dmVbMssI0UcZO2EG35bQgmc5l6M8R7M9Pon3mlx-JzW1AuEpoQZmpmEMkKlGPrkFBwK3QNz6uffPEY9Z1bnznQlf_DSdwCGdAF99pzxYbmZ5ZJJn6SM2F2Cjm5cpS46E2-NXm4SAc9QGjPeK921eXSftdGEp_AcQiHwpv8W0zjJzCPGzQX9i2IdeSyXwOJbM4TTYWO5hR21qASm4r-HglaVDhhFn8NKE00mmiOBFp3xrnsT_Lb8PoaUEk9iivexF6IGMCL0tl0L5BeNGCqdGSeMTJ5kgRdWAUMTzCRibLu4Zgyfy8IoaXRYBdb3EqN7AJSGW9iu-pTmK5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی اعلام کاخ سفید مبنی بر لغو سفر معاون دونالد ترامپ به سوئیس، وزارت خارجه این کشور اروپایی رسما خبر لغو سفر هیئت آمریکایی و لغو مذاکرات تهران و واشینگتن در روز جمعه را تأیید کرد.
لغو آغاز فوری مذاکرات بین دو کشور متخاصم تنها یک روز پس از امضا و رسمی شدن تفاهم‌نامه‌ای رخ می‌دهد که یکی از مهم‌ترین بندهای آن ۶۰ روز فرصت برای مذاکره درباره فعالیت هسته‌ای ایران است. قرار بود این ۶۰ روز بلافاصله در روز جمعه آغاز شود.
اما خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز پنج‌شنبه خبر داد که مذاکره‌کنندگان ایرانی پیش از آغاز دور بعدی گفت‌وگوهای صلح نیاز دارند نشانه‌هایی از اجرای توافق موقت از سوی آمریکا مشاهده کنند و هنوز تأییدی درباره سفر هیئت ایرانی به ژنو وجود ندارد.
در پی این انتشار این خبر بود که سخنگوی کاخ سفید هم در بیانیه‌ای که پنج‌شنبه شب منتشر شد، اعلام کرد ونس و هیئت آمریکایی آماده بودند به محض نهایی شدن برنامه مذاکرات، عازم شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/76503" target="_blank">📅 17:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vfGvwjgpwY7e28t7PTjqxbNrxtkASpVTSj-J9SGOnPhjgxrn4UQBsMbWk0lxws9W00B2LObkKIqvit6xIgCuTfa_ahTE9L2SOP3z2exPqDlBKs2IIgBUncWzNblMWmxjV2lLlAxiVpKGKihDWDeeHTVeYLPZDPSKicQZU-9Pf26ujxZ0V_g9XEDj4LZ4Of6qy-4NaPLG5mZyLtkxUt-C9-F0qDEslaMdDiEQaE9csMSnotxNgDiuT7DAGYTNf-LBfXqI0RqTpfkVwAZisefz_2jCaj-NNBy-91RbSNpRv6cHUOxteFE2ZsxL7AFW-C08TdxJvzK9rnDQlQNfs5rhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود قنبری‌راد، متخصص امنیت شبکه و از کارکنان یکی از شرکت‌های تهران، با اتهاماتی از جمله «اجتماع و تبانی علیه امنیت ملی»، «جمع‌آوری اطلاعات طبقه‌بندی‌شده» و «ارائه اطلاعات به اسرائیل» روبه‌رو شده است.
بر اساس گزارش‌ها، محمود قنبری‌راد، شهروندی ۴۰ ساله و متأهل، اردیبهشت‌ماه سال جاری در منزل شخصی خود بازداشت شده است.
یک منبع مطلع به دویچه‌وله گفته بود که او هیچ سابقه فعالیت سیاسی یا مدنی نداشته و به‌عنوان متخصص امنیت شبکه مشغول به کار بوده است.
گزارش‌ها حاکی است که او در تماس تلفنی از زندان، پرونده خود را «ساختگی» توصیف کرده و گفته است که برای پذیرش اتهامات تحت فشار قرار دارد. همچنین اعلام شده که وی از زمان بازداشت تاکنون از دسترسی به وکیل محروم بوده است.
بر اساس اطلاعات منتشرشده، محمود قنبری‌راد ابتدا حدود یک ماه در زندان اوین نگهداری شده و سپس به زندان فشافویه منتقل شده است.
همچنین گفته شده که او از نوعی اختلال عصبی رنج می‌برد و خانواده‌اش نسبت به وضعیت جسمی و حقوقی او ابراز نگرانی کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLL0H0yODfg2yZOUMSVy-ueWVm_MpujlMh2gWJ5rGpVrX5ro7Y7rcy1xKmyiNE54Fhbc6SOV0mZabI8Q7HFrZb6OioLY-2aEBKQiFFFD7sAYNTbmw195T-Hk_kVhvkXHE6s9rbt5o6rQMg_qTRllCnGbgG96qtHIFNu_Ccj8yGHNmGCYr6RxWGp-U-XPEWMBWtOtLs4PJO1e4muhf15Yc5Zm5wq1tL3ND3kFwz1zTS9U4HSRVVf8MCwPjQ3BjMayymwsQmAyq9ffpODikGyfiOrshrPjHuh7ah9um-1c066ZQOaH3u2kx6Vfo69JSsN2a6rHd5iFAehiPJ4Ld0k_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از امضای تفاهم‌نامه میان واشنگتن و تهران  را
منتشر
کرد.
این تصویر مربوط به مراسم امضای تفاهم‌نامه در کاخ ورسای فرانسه است؛ جایی که ترامپ در حاشیه سفر خود به فرانسه و پس از پایان نشست سران گروه ۷ (G7) حضور داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76501" target="_blank">📅 05:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWA1taaq5NMrKY-E0d3_R6StzhXFw2dY9sLWiY-llKEaNIfVIynehkUtd83EgItxXEsg2HaTGY-jGRvVC6sdLmwyXLuk5a9Kp5gkrQbiWr2A4BXosuk-4klJrb71L_RO5autwBRbwEhM5s2BNQyQgDcsNE29qqQBpqC9U30MvSF9QPL45qvLHKsMGuLM7L1hsiZsVdTcxuSSUrMYCdhQ0bMIzz_wZSN7g7uGEn777Y_1xmFUzVMFtDVm9dJesEbS9t8omZAHAvJvRpO5AYQ2dBTAeBaYabKQAl1vhcVW2SxGJydLXZVUdnomJoYXXcR7Iyi8fa3VRANITLMh47Bbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در«گفتگو ی تصویری با اکسیوس» گفت یادداشت تفاهم امضاشده با حکومت ایران را می‌توان «نوعی تسلیم کامل» از سوی تهران دانست.
او این اظهارات را در پاسخ به پرسشی درباره تفاوت میان خواسته پیشین خود برای «تسلیم بی‌قیدوشرط» و مفاد تفاهم‌نامه مطرح کرد.
مجری آکسیوس در این مصاحبه به ترامپ یادآوری کرد که در آغاز درگیری‌ها گفته بود تنها «تسلیم بی‌قیدوشرط» را از ایران خواهد پذیرفت، اما یادداشت تفاهم امضاشده چنین تصویری را نشان نمی‌دهد. ترامپ در پاسخ گفت: «خب، احتمالا در واقع تسلیم بی‌قیدوشرط است. فکر می‌کنم همین‌طور باشد.»
رئیس‌جمهوری آمریکا همچنین با اشاره به جنگ اخیر گفت ایالات متحده ایران را «کاملا از نظر نظامی شکست داده است». او با تمجید از توان نظامی آمریکا افزود واشینگتن توانست محاصره دریایی موثری علیه ایران اعمال کند و هیچ کشتی‌ای نتوانست از آن عبور کند.
ترامپ همچنین گفت پس از جنگ با ایران، محدودیتی برای قدرت خود نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76500" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sDndConh-JmtY2JkgtUoeLccivbv32QlBv5_4K9ghz5M23PUDZowv2czsDovOwS5yq-fowMohpCfeGcAKjEmJ0voZzSfYowSorkc839fDBaM_5Wc7CzyajM5e6XaFGPS0MByGa0xPl4GJjG_L5-bti19wOzIS4aldMC5ZLc8jKdXSdpjIc5UO6cuu2MEZ9KEckPZnW6kyxVowcdezakO0B9VhyZdyw9KbRf09i6lhjNVowL4OcDuUAT8zr2FD-bblEDnLEvo-RZFy0p6HXR1Bny1Vm4Fm50iHjXzFktg96-oeZGnoXriTsEI_p7R47cbmAAt0JXRtrW7R24R8KcJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر جی‌دی ونس، معاون ترامپ، در اطلاعیه‌ای اعلام کرد که او سفر خود به سوئیس برای شرکت در مذاکرات با جمهوری اسلامی را لغو کرد، زیرا برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و تدارکات و هماهنگی‌های این مذاکرات ساده یا قابل پیش‌بینی نیست.
در این اطلاعیه آمده است: «برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و هیات آمریکایی آماده بود در نخستین فرصت ممکن عازم شود، اما تدارکات و هماهنگی‌های این مذاکرات هرگز ساده یا قابل پیش‌بینی نبوده است. در حال حاضر، معاون رییس‌جمهوری امشب عازم سفر نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76499" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZHgfnwvKD4NvwtHchN37NqbNK1HRe6mTCTKYueMLH7IR_7AMl3LQDmrx3X8IhUUvF-G5q9UUSYjlpGd1GlnjxnCvIPvPNhR7NqK1a8bD5dimxsYM4cfmeUw53jfxHVmNk7waKDovAPS7iEHYgFepv0VZWpeFyoiJEq7zZBi7V0d16QGigUXuDZ_ehNRQLzM-e379SS_DG4OLBukzTOIdzcYEeJgTxEliIUd6RzTq94_gFrzrrqkcsJ3_2WL7jict1O5mDQpHhhko_AijaaWNR0LlI2c1I-k0yrNbybu-z-2wf5j3DfIs2bH_gftm15WsvkZgueQjGfxIPL7JZTs2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آسوشیتدپرس گزارش داد استیو ویتکاف، فرستاده دونالد ترامپ، پنجشنبه‌شب در نشستی غیرعلنی با قانون‌گذاران آمریکایی اعلام کرده است تهران از آژانس بین‌المللی انرژی اتمی برای بازرسی از تاسیسات هسته‌ای خود دعوت خواهد کرد و روند شناسایی محل نگهداری مواد غنی‌شده را آغاز می‌کند.
بر اساس این گزارش، ویتکاف به رهبران کنگره و اعضای کمیته‌های امنیت ملی گفته است تفاهم‌نامه میان آمریکا و ایران هیچ توافق جانبی نداشته است. با این حال، تهران و آژانس بین‌المللی انرژی اتمی نامه‌ای جداگانه تنظیم کرده‌اند که در آن دعوت از بازرسان آژانس و ادامه همکاری‌های نظارتی مطرح شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76498" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCAxfilYc5BEW0GHB4y8AcBk_C2skodwhFCzk6cre-5xrBWSdA_-Z3RvoaGWiwN0dpdNf191V08PzGVsQkBW-UC4ndJyqZfDKA53-VL8OT-W7thXI4GpK20J02BkvqQiVZyhYwmOTB86jsX28D2DpnJmNqjC6gDLH-1iTf_TVxmTiTjeBqYTCa2WkfhlxPssRfRcV_zp1JLDL3v7WrKjZoeJC7VpqKUytv9mEbC76CRnpIhvfD0OTo9fNP3JjcoOAPs9Vq2QObolg8fsH_gPHTJb6GJopRUnHWEx7yMQvF7iODGk57QgYxksq1VkUUQgakRg8kZ6gotldiaI-ESb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجه اتحادیه اروپا، گفت هنوز برای بحث درباره لغو تحریم‌های اتحادیه اروپا علیه ایران زود است و این موضوع پس از دستیابی به یک توافق هسته‌ای با ایران بررسی خواهد شد.
او پیش از نشست رهبران کشورهای عضو اتحادیه اروپا به خبرنگاران گفت: «زمانی که شرایط فراهم شود، کشورهای عضو درباره مناسب بودن لغو تحریم‌ها گفت‌وگو خواهند کرد، اما هنوز به آن مرحله نرسیده‌ایم.»
اتحادیه اروپا در حال حاضر مجموعه‌ای از تحریم‌های چندجانبه علیه بیش از ۷۰۰ فرد و نهاد در ایران اعمال کرده است که شامل ممنوعیت سفر و مسدود شدن دارایی‌ها می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76497" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76496">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWeWLW_A_vQpoFYTbaQPQyzhmDcmWMA9_l070LkqbrbLmnRWBfJmFuqYxopOV5_5V3X13zRuneszuLnjbpE0b0bhOQ4gueaIkDH1fwuYIaCcafTVN8gKKq6mf4lLbK3Dt8qKEWcJ98Qzx2tQWSWO3pw6-CnuGNPlLxnE8F4mkABq_dbvVjPH_jUDMofYjCF0hgtUQVt8Oqt26bg5O2ES1syLmLQOwPKxI5JNukM444n4FnwD91H9COXnBtiXCcaSpAyxG7v8ps36xWwxcjWpY-Rg6Ps6AZnzxs6jZ6l_XwQ6-tWuNaht2fWvhB9XbzTcfO5rP5vvRYukqk0EykzZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین به نقل از یک منبع آگاه گزارش داد هیات مذاکره‌کننده جمهوری اسلامی به دلیل ادامه حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس برای آغاز نخستین دور مذاکرات ۶۰ روزه را به حالت تعلیق درآورده است.
المیادین افزود: تهران پیش‌تر به آمریکا و میانجی‌ها اطلاع داده بود که پرونده لبنان در ادامه یا توقف مذاکرات نقشی محوری دارد و هشدار داده است حملات اسرائیل تا عمق ۱۰ کیلومتری خاک لبنان نقض یادداشت تفاهم و توافق چارچوب است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76496" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CZcgqmrik1X28VZa0bvZSEjCv5Ck4frCoJKfOcnTSHBOSRpTVDXL2tLYEaxYsPqE3fIL_lckbzc9HicNrl4jVNj56AONxFGHdgb2XIApfIi9rHDldAc4iRlUed2Sh-6amFrgdDq05CnqeiwN3uQTW6eZUeWXekVU9NiqLbjglDiAtNP4ms0XdZRkKyCB_Y_dSCNg-itHGMR-bxWi5Z6tzYZfKkAuYTzm_xiScRihkydG0CdgJrSN18SoWE05Cm0USQOPvR_v3MNjRclgWGOvH2cjuNr3Inl91kUgvfW4QRu9iuGoUAnXj_0Xr5KlSBz436G_8ii9yEZLYO_w9YYBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت کاخ سفید:
رئیس‌جمهور دونالد ج. ترامپ تهدیدی را حل کرد که واشنگتن چهل سال صرف مدیریت آن کرده بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
یک پیروزی برای آمریکا.
🇺🇸
WhiteHouse
ترجمه با هوش مصنوعی به تصویر اضافه شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76495" target="_blank">📅 22:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZKaVwe1PpCsR39UbdQTmveVYBC2Ir-_BiDHWCOc6SwrIrj-UrR_Alpp6Rr1fdYdMlINosYkxjm028kg5_DLEyVWlDxmB2ypAAuIcQhU8EIIR_BQV0obZ_Qt1U8ZQ7Z8shrJQ-2FzMtipMNXp3A9p-XYijyHpeqSyZz8IUMtxbu-EDTuPq0KjRNNyeRh7g3kFBkVC4eu4RYQtrOdA-PdlSz_phkQc2PX5sbU4YpPNHtfp9jso6u3C1xyGGj8OhiEuiVKVcOj0VTXeHl6x8hyisK_C1MGIkiK2XiSJ7Fn8O0F75oYUmnxVqxJs4lYMGSLaII-ZGpe_Zlwed-N04Yx73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'
بیانیه شورای عالی امنیت ملی
'
منابع حکومتی:
🔹
در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (PGSA .ir) ارسال نمایند.
🔹
به موجب یادداشت تفاهم اسلام‌آباد، به مدت شصت روز، هیچ‌گونه هزینه‌ای از متقاضیان اخذ نخواهد شد و این هزینه‌ها توسط دولت جمهوری اسلامی ایران تأمین می‌گردد.
🔹
بر این اساس به مدیریت آبراه خلیج فارس دستور داده شده است، در جهت تحقق اهداف تفاهم‌نامه درخواست‌ها را با سرعت و اولویت رسیدگی و پاسخ دهد.
🔹
با توجه به شرایط خاص و وجود برخی مخاطرات ایمنی در مسیر عبور و به دلیل لزوم حصول اطمینان از تردد ایمن و جلوگیری از حوادث دریایی، لازم است کشتی‌ها در مسیر و زمان اعلامی به آنها عبور نمایند تا به تدریج، امکان تردد افزایش یابد.
🔹
ترتیبات اجرایی و جزییات فنی عبور از تنگه هرمز از طریق مدیریت آبراه خلیج فارس اعلام می‌گردد.
🔹
در خصوص سایر موضوعات، از جمله مین‌زدایی، اقدامات لازم مطابق بند ۵ یادداشت تفاهم اسلام‌آباد انجام خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76494" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76493">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUDQ38abYii-ckK5zrXf5nePPfuAJClhDFMM1inPIXlKqV9NmcdrA7DrusH_Wh9zQArPPpvPHrpANelqVUf35DGPHypCvKABoHQjlJlBWacwnbMPDrc211WmWNKeKWt-9gw13FfYzLzd4hiyjTcskmlXtFARAqyColuAwLpcody-uF2EcLeJBo0yYZkVpjKUap4vJznwnz7_CRaLG-I7chAScKYU3aP55ihJQRdaGol5fPwqwGmY1UryJWzKamlPf9_E_Pv4zdcQk0z4bBF3b1oU7KC0VlcMcmPJ6ubLuzOZuI63fFlJIJjQzszLd42-Twkd7sGmUu3q2AOuBI7Qqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: انتظار آتش‌بس کامل در همه جبهه‌ها از جمله لبنان را دارم
ترجمه ماشین:
ایالات متحده به صلح متعهد است و ما همه در منطقه خاورمیانه را تشویق می‌کنیم که به تعهد خود برای فراهم کردن امکان پیشرفت زیبای مذاکرات ما پایبند بمانند.
بازارها از آنچه در حال رخ دادن است استقبال می‌کنند: قیمت نفت به‌شدت پایین آمده و سهام به‌شدت بالا رفته است.
ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76493" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76492">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPourostad وحید پوراستاد🔷(Vahid Pourostad)</strong></div>
<div class="tg-text">« پیام منتسب به مجتبی خامنه‌ای در واقع نوعی فاصله‌گذاری حساب‌شده با تفاهم ایران و آمریکا است. مجتبی خامنه‌ای رهبر جمهوری اسلامی اجازه امضا را داده، اما مسئولیت سیاسی و اجرایی آن را بر دوش پزشکیان و شورای عالی امنیت ملی گذاشته است.
پیام همزمان رو به داخل و بیرون نوشته شده است. در داخل می‌گوید رهبر با رضایت کامل وارد این مسیر نشده و دولت باید پاسخگوی نتیجه باشد. در برابر آمریکا هم این سیگنال را می‌فرستد که تفاهم، زیر فشار ترامپ و دولت او به‌معنای عقب‌نشینی قطعی نیست؛ بلکه مشروط است و اگر شروط ایران محقق نشود، موافقت نهایی رهبر با توافق نهایی هم تضمین‌شده نخواهد بود.
در واقع متن، بیش از آن‌که اعلام رضایت از توافق باشد، تلاشی برای حفظ دست بالا در مرحله بعدی است: هم مسیر مذاکره باز می‌گذارد، هم امکان عقب‌نشینی تبلیغاتی حفظ می‌شود, هم به واشینگتن گفته می‌شود که فشار بیشتر ضرورتا به انعطاف بیشتر ایران منجر نخواهد شد»
@pourostadv</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76492" target="_blank">📅 22:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4x4SMB24PA7onldP8ppkfzJ6MS64bpioWaA3PhcyARqL1oe2pJWxJyEqYBuY14I9K6a77kFHbbjBLFhpis1plcbRBVIEcTHGJ23SSAlme4B9UB543sMh1zC62Q95YlfGGY5nEqoNe4ulk140q93u2Wg9z-hEaLfAz30JRTimcwwP_Pe6yfMPFX8Lk5IWc1pzJcpzHoQwfJY4w0v6QgMFf5UiHRyBZcW3d3sGEYPQU-IQOPdEObuVVQoWMzpJj449satXkCFQs7biKYK7zT4C5XV_dPMhBHIXFI3Dp8tfcHDrGHD8p94uqeuBGnWPvaOxuTwQMiTvWXk1U7w_9n2zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول
گردن‌نگیر
جوان شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76491" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ULyPUO-LH8rLeGRD7e-LdJ_AHgDy3Z4uemZ5oBNMinhKn3XKRZIuxiE2KvbC_snZF5wTko94srY-wUMxZm93uCJzoyKLNsFYXCxbn4tZZTKtkTyvv7VQHDKpIFRL5vP2UXjY_Hc0DH8Dd2yAxetsmWuAclzxPqOOQexwQ_-hFjfmLg0tO4WW5llmmbD6rO1Ifr5atmBZ5Nr7oZwQdsuUNMAW0ih369q20sdxvxyF-ja2IIhu_MUVa3Re5OuDwjY6lNop11KWq7oWXn5UQZkxm2UFZqx8RsW3zUL_1CWxohrrKsD7W61-l9WAxlf2amKaRe7Cuwe_TG_Kt7E9JGv22Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پنج‌شنبه شب متن پیام مکتوبی منسوب به مجتبی خامنه‌ای را منتشر کردند که در آن رهبر جمهوری اسلامی درباره امضای تفاهم‌نامه میان ایران و آمریکا گفته است که «نظر دیگری» داشته و مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا دانسته است.
در این پیام درباره توافق با ایالات متحده آمده است:
«بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیت ملی از طرف خود و سایر اعضا در پاسداشت حقوق ملت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه آن را صادر نمودم‌.»
در این پیام به تفاهمنامه اخیر به عنوان «تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و آمریکا» اشاره و گفته شده است که رهبر جمهوری اسلامی و مردم از این لحظه «منتظر تحقق شروط گفته ‌شده» خواهند بود.
در این پیام آمده که مذاکرات حضوری آینده «به معنی پذیرش نظر دشمن نخواهد بود.»
VahidOOnLine
در تیتر و متن نامه و خبرهایی که درباره‌اش تولید میشه بسیار تاکید دارند که این تفاهم‌نامه‌ای بین پزشکیان و ترامپه و نمی‌گن بین ایران و آمریکا
در واکنش‌ها از کوچک‌نمایی نقش
قالیباف
یا محافظت ازش با سپر کردن پزشکیان هم میگن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76490" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VTRdUEekxsQcg8o2Dx78RcteJdLoJmx-7w2fJktk8uoFXKrSNsnUYBMUgnRi4bgHNBXHkYejwJdaxHc2DBO9RPe7dget6zCF8_VcPUEIKQN7jC9u6z4t3MPTjeEbnhz57dpO1Z4Cvokmhd0P4WmtTjrfkCUEQZyQ0IsHu1fMlbMnOYPNAZjr8ymemQtZiChAkNYEYLVgtlAlYxmXtaqozrJz0XMp55pyVpEOKcCHNJ_NbwoKX6JXhbobjHmH370sehnGd6E50Fb4WtncU8lTMDzVP1xo6OGtIcuyWdI3LmzjBtpGMccYvTVDTU0-jqzDG9YA8z9akeb5smSlIc44tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!!
رئیس‌جمهور دی‌جی‌تی
(توضیح: Dumocrat بازی زبانی تحقیرآمیز با Democrat است؛ از ترکیب ضمنیِ dumb به معنی «احمق» و Democrat. در ترجمه می‌شود چیزی مثل «دُمکرات‌ها» یا «دموکرات‌های احمق» آورد، بسته به لحن مورد نظر.)
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76489" target="_blank">📅 20:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EynsGaVUdVXPxtsLWj0fw-YCSMUTzUmo_OaFlXjkAdhoEsUeCfv9e5XFRedwK-bg2LtRwH5p8LWJBfAxLIt_u8K1d7wIUY-N20P8m1nrvNwhPDxATrBORAFfrxx9PcTnyT9jHPBVMsIuUJfdQjY_kJHUlZm_d91urEOPHVz4PFuqTwCKVIQjHq-M9MIpQ35bcK-NCgkdqS3_9ajmgmQiJuG9E06cN56I5B5EFTM_CRnAiVOKH0-Olek4pLG69hOvMHtu0KO26GWtGNuwTwHYo1guFW_dOkLU9e8Mbnh8z3qpt41GpuLBxWN7gENRMqxuqG_YIGFUCnC2UWoPGOqDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام پایان محاصره دریایی
پست سنتکام، فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
امروز، نیروهای آمریکا مطابق دستور رئیس‌جمهور، محاصره‌ی همه‌ی رفت‌وآمدهای دریایی به مقصد بنادر و مناطق ساحلی ایران و از مبدأ آن‌ها را رفع کردند.
نیروهای آمریکایی مانع عبور کشتی‌ها به سوی بنادر ایران در خلیج فارس و خلیج عمان، یا خروج از آن‌ها، نمی‌شوند.
همه‌ی تلاش‌های نظامی آمریکا برای اجرای محاصره متوقف شده است.
کشتی‌های بزرگ نیروی دریایی ما در منطقه‌ی کلی باقی خواهند ماند تا اطمینان حاصل شود که همه‌ی جنبه‌های توافق رعایت، اجرا و به‌طور کامل لازم‌الاجرا و مؤثر باقی می‌ماند.
CENTCOM
البته سنتکام ننوشته خلیج «فارس»
🔄
آپدیت:
توییت رو ویرایش کردند و در نسخه جدید اون جمله مربوط به خلیج فارس رو کلا حذف کردند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76488" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76487">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DOU7VYQRGT9N1kDa1Tq4q2emnBNH89JKNAyJJ-3J8OT2WQ5aa8EvgFoZf_Fz3lY_Z8Oa7drM11F1lN_t5NibHYT_0mXAV2qsgsjdKiiBY7ilyKuAtyCutN76-GiS-w34MjeFurfXTGrUgEYph_1HcYaSbBujNuZJOcsWe8YApny9ymkE12I6va_PoFhYYfG8RJVkotZAbvypAY017E1sNuEtg4js7i_HWIVkKLELT0EwjlIPKEtP43r5UrU2MQAYL_qBEuQamLRJqbvCjBPv3duCWr8lPGTO543OSa6j6Up2YzHw_zaapEWgz9LN3e_iPSmpPcpHum6ASyI6UDe5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره: ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار. realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76487" target="_blank">📅 20:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=GX5zdIuOKd-U9Btt6x-x2nkI8J1w8sCAX5QZKmbNhkQGzL7j3h43mXRID2t0ICG3XA524FXkKFpAMcc035mXICFjgkwgyur4yV_WxV_I08ttK2WPaKadqyPTODg_OuIdhYwt8On7omjZ0YGOqYifXPUxkPmcS1JxrdgVYO54KKVx2_NxQGgan6dYe6mywFr_9krpVYi_7qq4f3lvYdkXq9eQDwGBN9kQ9ddncEoSBy6Aiphqs5BeekV9k1S6OwcSI84vo4dJmpeN_CkOMghMJnSpU1Sk8A68upydPtchg5Pn5h72f-voSQ8gbK72kfW1vYZE_aUwBdKIFDyKLhiZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=GX5zdIuOKd-U9Btt6x-x2nkI8J1w8sCAX5QZKmbNhkQGzL7j3h43mXRID2t0ICG3XA524FXkKFpAMcc035mXICFjgkwgyur4yV_WxV_I08ttK2WPaKadqyPTODg_OuIdhYwt8On7omjZ0YGOqYifXPUxkPmcS1JxrdgVYO54KKVx2_NxQGgan6dYe6mywFr_9krpVYi_7qq4f3lvYdkXq9eQDwGBN9kQ9ddncEoSBy6Aiphqs5BeekV9k1S6OwcSI84vo4dJmpeN_CkOMghMJnSpU1Sk8A68upydPtchg5Pn5h72f-voSQ8gbK72kfW1vYZE_aUwBdKIFDyKLhiZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی در ایران که ریاست هیئت مذاکره‌کننده ایرانی با نمایندگان آمریکا را برعهده داشت، عصر چهارشنبه در مصاحبه‌ای مفصل با تلویزیون حکومتی در ایران به نهایی شدن تفاهمنامه میان تهران و واشنگتن واکنش نشان داد و آن را موفقیتی بسیار بزرگتر از مقابله نظامی با ایالات متحده دانست.
او در مورد دستاوردهای ایران گفت: «هر آنچه را که با اقدام نظامی می‌خواستیم به دست بیاوریم، چندین برابر آن را از طریق مذاکره گرفتیم؛ اصلا قابل قیاس نبود. هر جنگی ممکن است پیروزی‌هایی داشته باشد، اما اگر این پیروزی‌ها در نهایت به یک سند حقوقی و سیاسی منجر و ثبت نشود، هیچ منفعتی نخواهد داشت.»
او در بخشی از صحبت‌های خود درباره انتقام کشته شدن علی خامنه‌ای گفت: «همان‌طور که خونخواهی امام حسین، ظهور امام زمان است، خونخواهی رهبر شهید هم آزادی قدس است... صد نتانیاهو بند کفش امام شهید ما هم نمی‌شود.»
قالیباف در مورد وضعیت تنگه هرمز هم گفت: «تنگه هرمز هرگز به شرایط قبل بازنخواهد گشت. البته این به آن معنا نیست که ما در تنگه هرمز بخواهیم برخلاف قوانین بین‌المللی و مقررات دریانوردی عمل کنیم.»
@
VahidHeadline
قالیباف در مصاحبه‌ای که همزمان با انتشار مفاد تفاهم‌نامه تهران و واشنگتن از صداوسیما پخش شد، گفت برای حضور در مذاکرات با دولت دونالد ترامپ تمایلی نداشت و به دلیل نقش ترامپ در کشتن قاسم سلیمانی، «کراهت شدید» برای ورود به این روند احساس می‌کرد. او افزود که با وجود این مخالفت شخصی، به درخواست مقام‌های جمهوری اسلامی مسئولیت مذاکرات را پذیرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76485" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76484">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U51k1gM_8k77u1YdORrbm6eXSINXozlRy4hNRXI0oaFkTx-MwVMF-sSwppaaS37B-DXC-gy0zRQ2Nzin0fwFjrgz_vIzVTp3z0Adle3KiCF3r6cWZcBBjsJAmhL4AzHKz5oA-4aE6JomPnm5eYpzPOtparNGIyPo5O_cs-Cl38MzmBz8dQsKsPmcoB1zocPDjDQZ6Fr-7ajN9juWR3IDtzLk4CJ_IkUowON1g-Wlinau95PztRH76yxBHLdJajYpisj7FIi4TXz-HTgt4c_35RMCsodGmPyvIiLQSPpvnhyXhjFqVgbzqIh7dp915_jZNAXyFFHQ22lDSBbahRI19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، یک روز بعد از امضای تفاهم‌نامه ایران و آمریکا در نخستین موضع‌گیری خود اعلام کرد که نیروهای اسرائیلی از جنوب لبنان عقب‌نشینی نخواهند کرد و تا هر زمان که لازم باشد منطقه حائل امنیتی خود را در آنجا حفظ خواهند کرد.
این اظهارات پس از آن مطرح شد که دونالد ترامپ، رئیس‌جمهور آمریکا، طی روزهای اخیر از عملیات اسرائیل علیه حزب‌الله لبنان انتقاد کرد و آن را بیش از حد «تهاجمی» دانست.
نتانیاهو در یک مراسم رسمی گفت: «ما امنیت و رونق را به شهرهای شمالی بازخواهیم گرداند.»
او افزود: «این امر مستلزم حفظ منطقه امنیتی در جنوب لبنان است؛ مستلزم آن است که آنجا را ترک نکنیم، تا زمانی که نیازهای امنیتی اسرائیل چنین ایجاب کند.»
رسانه‌های رسمی لبنان پیش‌تر گفتند که در حملات صبح پنجشنبه ارتش اسرائیل به جنوب لبنان، ساعاتی بعد از امضای تفاهم ایران و آمریکا، سه نفر کشته شدند.
از سوی دیگر، یک مقام ارشد اسرائیلی پنجشنبه به خبرگزاری رویترز گفت که اسرائیل «در حال انجام مذاکراتی سرسختانه» با ایالات متحده دربارهٔ موضوع ادامه استقرار نیروهای اسرائیلی در جنوب لبنان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76484" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شروع سخنرانی جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔸
دیشب، ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرد.
این بالاترین میزان از آغاز درگیری است.
🔸
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آنها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است که دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به تعهد خود عمل می‌کنیم.
🔸
شما چیزهایی درباره ۳۰۰ میلیارد دلار یا ۲۴ میلیارد دلار، یا این یا آن عدد یا مقدار پول خواهید شنید، و واقعیت ساده این است که تنها راهی که ایرانی‌ها به هیچ یک از این منابع دست پیدا کنند — حتی یک سنت، به هر حال، از ایالات متحده آمریکا تحت هیچ شرایطی — اما
تنها راهی که آن‌ها می‌توانند از این معامله بهره‌مند شوند این است که کاملاً مطیع باشند و رفتار خود را تغییر دهند.
اگر ایرانی‌ها رفتار خود را تغییر ندهند، برنامه نظامی و هسته‌ای آن‌ها همچنان نابود خواهد شد؛ اگر رفتار خود را تغییر دهند، آنگاه رابطه‌ای تحول‌آفرین با خاورمیانه خواهند داشت.
این یک برد-برد برای ماست.
🔸
در ایران تقسیمات واقعی وجود دارد.
آنچه دیده‌ایم این است که عمل‌گرایان در حال پیروزی در بحث هستند.
🔸
من کسانی را دیده‌ام که به این توافق شک دارند — افرادی می‌گویند ایرانی‌ها هرگز رفتار خود را تغییر نخواهند داد.
خب، شاید این درست باشد، و اگر چنین باشد، آن‌ها هیچ‌کدام از مزایای این معامله را به دست نمی‌آورند. اما آیا ارزش امتحان کردن ندارد؟
🔸
می‌گویم دوره ۶۰ روزه رسماً امروز شروع شده است.
پس بله، توافق دیروز شروع شد — ما امروز ساعت ۶۰ روزه را شروع خواهیم کرد.
🔸
تمام چیزی که رئیس‌جمهور دیروز گفت این است که، البته، کشورها حق دفاع از خود را کنار نمی‌گذارند.
اسرائیل حق دفاع از خود را کنار نمی‌گذارد اگر حزب‌الله به اسرائیل راکت یا پهپاد شلیک کند.
ایرانی‌ها حق دفاع از خود در کشورشان را کنار نمی‌گذارند، اما
ما انتظار داریم که به عنوان بخشی از توافق نهایی، آن‌ها نتوانند موشک‌هایی بسازند که بتواند به طور گسترده کل جهان را تهدید کند،
و این همان چیزی است که رئیس‌جمهور ایالات متحده دیروز گفت. و ببینید، خیلی ساده است: نمی‌توانید به کشوری — چه اسرائیل، چه ایران — بگویید که حق دفاع از خود را نداشته باشد.
🔸
خبرنگار: رئیس‌جمهور ترامپ دیروز گفت که اگر مذاکرات این دور به مشکل بخورد، شما را مقصر خواهد دانست. آیا نگرانید که او شما را به عنوان مقصر معرفی کند؟
جی‌دی ونس: نه، اصلاً. فکر می‌کنم رئیس‌جمهور شوخی می‌کرد، همان‌طور که اغلب این کار را می‌کند.
🔸
جی‌دی ونس درباره تنگه هرمز:
ما هرگز نمی‌خواهیم این اتفاق دوباره بیفتد، درست است؟ این موضوع مربوط به عوارض نیست.
این درباره اطمینان از این است که تنگه‌ها هرگز به عنوان نقطه گلوگاهی برای اقتصاد جهانی استفاده نشوند.
صادقانه بگویم، این چیزی نیست که ایرانی‌ها بخواهند.
🔸
جی‌دی ونس درباره برداشتن تحریم‌ها:
صادقانه بگویم، ما این را به عنوان امتیاز بزرگی به ایرانی‌ها نمی‌دیدیم — ایران... این را به عنوان امتیاز به آن‌ها نمی‌دید، چون چیزی که مانع فروش نفت آن‌ها می‌شد تحریم‌ها نبود.
آن‌ها بدون هیچ تخفیفی مقدار زیادی نفت می‌فروختند، چون تحریم‌ها اساساً بی‌اثر بودند.
در آن زمان، کاری که تحریم‌ها انجام دادند این بود که سیستم مالی ایران را به نوعی به سیستم بانکداری سایه‌ای منتقل کردند.
با برداشتن تحریم‌ها، ما در واقع قادر خواهیم بود کمی ببینیم که سیستم مالی آن‌ها پول را کجا می‌فرستد و از کجا دریافت می‌کند. این یک مزیت واقعی است.
🔸
آنچه به برخی از منتقدان توافق که شنیده‌ام می‌گویم، کسانی که می‌گویند «خب، ایران تمام این مزایا را به دست خواهد آورد».
تکرار می‌کنم آنچه را که گفته‌ام و احتمالاً باید چندین بار تکرار کنم: مزیتی که ایرانی‌ها به دست می‌آورند و قبلاً نداشتند چیست؟ و پاسخ هیچ است.
آنها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتار خود را تغییر دهند. اگر رفتارشان را تغییر دهند، این چیزی است که باید جشن گرفت.
🔸
هیچ‌کس نمی‌تواند حق دفاع از خود یک کشور دیگر را نادیده بگیرد — اسرائیل حق دارد از خود دفاع کند.
اما اساساً، اسرائیلی‌ها، درست مانند همه‌ی مردم دیگر، باید به این روند صلح که اساساً برای آن‌ها و کل منطقه مفید است، احترام بگذارند.
🔸
در انتقاد از اسرائیل: به نظر می‌رسد که ما درست در آستانه یک پیشرفت بزرگ در توافق هستیم، و ناگهان یک انفجار بزرگ در یک مرکز جمعیتی غیرنظامی در بیروت رخ می‌دهد و بسیاری از افرادی که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل قبول نیست.
🔸
توافق هسته‌ای اوباما اجازه غنی‌سازی داد — توافق ما این اجازه را نمی‌دهد.
توافق اوباما اجازه انباشت مواد با درجه تسلیحاتی را داد؛ توافق ما در واقع به نابودی آن انبار مواد غنی‌شده منجر می‌شود.
توافق اوباما بیش از یک میلیارد دلار پول آمریکایی به آنها داد؛ این توافق هیچ دلار پول آمریکایی به آنها نمی‌دهد.
🔸
آنها تعهدات هسته‌ای بسیار مشخصی داده‌اند.
آنها متعهد به نابودی ذخیره بسیار غنی‌شده‌ای شده‌اند که در اختیار دارند.
اما نکته دوم، تنها کاری که ما انجام داده‌ایم برداشتن محاصره در تنگه است — که اساساً آن را به وضعیتی که قبل از درگیری بود بازمی‌گرداند.
🔸
خانم‌ها و آقایان، کلمات مهم نیستند، ما درباره تأیید صحت صحبت می‌کنیم.
🔸
فرض کنیم — دو سال بعد، آن‌ها آنچه را که ما باید در برنامه هسته‌ای ببینیم انجام داده‌اند و تحریم‌ها را طبق توافق آزاد می‌کنیم.
سپس تصمیم می‌گیرند که برنامه هسته‌ای را دوباره بسازند.
البته در این صورت، آن تحریم‌ها دوباره باز خواهند گشت.
و به همین دلیل است که این موضوع واقعاً شبیه یک دکمه تنظیم است: هرچه رفتار خوبشان را افزایش دهند، ما می‌توانیم تسهیلات اقتصادی را افزایش دهیم؛ اگر رفتار خوبشان را کاهش دهند، می‌توانیم آن را قطع کنیم.
🔸
آنچه واقعاً اتفاق افتاد این است که ما یکشنبه یادداشت تفاهم را امضا کردیم. این موضوع شرایط توافق را تثبیت کرد.
ایرانی‌ها به ما آمدند و گفتند: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً این را درک نمی‌کردم—می‌خواستم متن را فوراً منتشر کنم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «باشه، ما تا جمعه صبر می‌کنیم.»
و سپس در طول دوشنبه و سه‌شنبه، در حالی که رئیس‌جمهور در نشست جی۷ بود، شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را تشویق می‌کردند که این کار را انجام دهند.
ما قطعاً به آنها می‌گفتیم:
«ما تمایل شما برای عدم انتشار متن تا جمعه را درک می‌کنیم، اما می‌دانید که ما در یک نظام دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق را ببینند. ما قطعاً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها تصمیم گرفتند که رئیس‌جمهورشان آن را امضا کند، رئیس‌جمهور ما آن را امضا کند، و سپس متن را به عنوان یک سند امضا شده فوراً منتشر کنند.
🔸
اینکه فکر کنیم فروش چند میلیون دلار نفت قرار است اقتصاد ایران را به طور بنیادین تغییر دهد، درست نیست.
🔸
در مورد وجوه مسدود شده، مقدار پول — صادقانه بگویم نمی‌دانم.
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. در واقع اعدادی بیش از ۲۰۰ میلیارد دلار هم شنیده‌ام.
بیشتر آن در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در خلیج فارس است، یا در اروپا، یا جای دیگری.
اما مقدار دقیق پول را نمی‌دانم — مقدار زیادی است.
🔸
من گزارش‌هایی دیده‌ام — نمی‌دانم این از کجا آمده — که قطری‌ها میلیاردها دلار و دارایی‌های ایرانی را آزاد کرده‌اند.
این اصلاً درست نیست. برای قطری‌ها غیرممکن است که بدون موافقت ما این کار را انجام دهند، و قطعاً بدون اینکه ما ببینیم.
🔸
درباره موشک‌های ایرانی:
توانایی آن‌ها در پرتاب موشک به طور قابل توجهی کاهش یافته است.
آیا این توانایی صفر شده؟ خیر. اما به طور قابل توجهی کاهش یافته است.
ما آن مأموریت را رها نکرده‌ایم. ما آن را به انجام رسانده‌ایم.
🔸
خدا را شکر. خوشحالم که پاپ چیزهای مثبتی درباره تفاهم‌نامه ما گفته است.
🔸
آنچه ما می‌گوییم این است که
نیروها را به سطح قبل از درگیری بازمی‌گردانیم،
قصد نداریم چند گروه ناو هواپیمابر اضافی را آنجا نگه داریم.
ایرانی‌ها این را نمی‌خواهند؛ صادقانه بگویم، ما هم این را نمی‌خواهیم.
🔸
خبرنگار: چه کسی آن صندوق ۳۰۰ میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
جی‌دی ونس: تمایل زیادی از سوی دنیای عرب و حتی خارج از دنیای عرب وجود دارد که اگر ایران رفتار مناسبی داشته باشد، واقعاً در آن دخالت کنند.
🔸
کمی به توانایی رئیس‌جمهور ایمان داشته باشید، با توجه به اینکه او ما را تا اینجا رسانده است، می‌تواند ما را به گام نهایی برساند.
🔸
دونالد جی. ترامپ تنها رئیس دولتی در سراسر جهان است که در این لحظه نسبت به ملت اسرائیل همدردی دارد.
اگر من در کابینه دولت اسرائیل بودم، شاید به تنها متحد قدرتمندی که در سراسر جهان دارم حمله نمی‌کردم.
🔸
در سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط دست‌های آمریکایی ساخته شده و با مالیات‌های آمریکایی پرداخت شده‌اند.
مشکل اسرائیل دونالد جی. ترامپ نیست، و هر کسی در اسرائیل که فکر می‌کند بزرگ‌ترین مشکلشان رئیس‌جمهور ایالات متحده است، باید بیدار شود و واقعیت وضعیت کشورشان را درک کند.
🔸
خبرنگار: چه چیزی مانع ایران می‌شود که در آینده برنامه هسته‌ای خود را بازسازی و از سر بگیرد؟
جی‌دی ونس: اول از همه، آنها باید پول زیادی به دست آورند تا بتوانند برنامه هسته‌ای خود را بازسازی کنند
.
c-span
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76483" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXOxo0tdC1ia8SOxutF8BUuKJScSlTDOxIf81UnN716nCBRHJpFwib6cSCh-NyrAvatr9e0lIyMjwl4PAWx841QSB7fzYodivelkKtMFOZL8bFskubdKHxc28pMTEVCBTPO6meyLcKvGnp9c3beKiT8VQQmYypV0oTo-pxlUquoVWh3xgGqsr7eVvuQ7aUUo9WLHiOYBE-RfcfVs598HWgb2ohVMMfG0kvS91eeTnDUn6AS9B670QHPkNDIjr4zJrYdvwVhsc6yl4e7NEDO5-O9P5fXurNLr-XuqNEmJb9yNTqpmbQVR2cU-r8mehLV_Qq0x4RjGgqxlGxVuXljz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر کشور و رییس سازمان امور اجتماعی ایران می‌گوید به افرادی که در تجمعات شبانه «دوقطبی‌سازی» می‌کردند، در یک نامه به طور «محرمانه» تذکر داده است.
«محمد بطحایی»، بدون اشاره به نام این افراد گفته است که «مورد اول مربوط به یک سازمان و تشکل سازمانی بود و در دو مورد دیگر به‌صورت فردی، نامه‌ محرمانه و البته همراه با احترام و تکریم برای افراد مورد نظر ارسال شده است.»
پس از اینکه گفته شد ایران و آمریکا به امضای تفاهم‌نامه‌ای برای رسیدن به یک توافق پایدار نزدیک هستند، برخی مخالفان این توافق که از چهره‌های نزدیک به جبهه پایداری، تشکل سیاسی اصولگرا و تندرو در ایران هستند، علیه «عباس عراقچی» و «محمدباقر قالیباف» شعار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/76482" target="_blank">📅 18:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76481">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_sBPAHh0nJBA1GzQ1n8WXdsTTDxTbuDHv0Tmj1flT6GPWXp-HmBuXI4QmkHcapM3pGuMncn6qjBtPt31mhNPJtmNHoo1nwO93OuvAUExsA-4HweIP-bak8dVXclhMVVNHhsy74wzUAMuf4t6SWXvjRZSiHGtbZHnnuTybktBIxuYJ1woiYukoLivH8y9_nAnVxMeIOXwhqmevB0-hnnZl_AGw_LuyLRuW8aVvkWn5D_e0QJJAuOuTSp5TsVrWHZjhZWC8sxW84mLxNurcB9FKv2wZ4_o8a7QjgGx_pnQdg36_57pjscIxzd8ZcD35D-aV8BKjEtE5HdFLI2kPQn4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرنا: به پاکستان گفته شده "نیازی به برگزاری نشست حضوری در سوئیس نیست"
ننوشتند کی گفته:
منابع دیپلماتیک پاکستان گفتند که سفر برنامه ریزی شده شهباز شریف نخست وزیر این کشور به سوئیس لغو شده است.
این منابع مدعی شدند که از آنجایی که یادداشت تفاهم اسلام‌آباد از سوی رئیس جمهوری اسلامی ایران و رئیس دولت ایالات متحده به امضا رسیده است، به طرف پاکستانی اعلام شد ‌که اکنون نیازی به برگزاری نشست حضوری در سوئیس نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76481" target="_blank">📅 17:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uO3boyQMi51WmWRZWefJUXXSVOpsxYmJ13CPnpMOcX-ghg43Gw0LNu0k6ixoxuCGkH38wX7DI83_sqZj2lnSEwAhhzud-HIurisrCw2sJBTwpkZM4sJOMiQOHsMD3wdunYcgxhgOmcmoXQOHQcBbnDcYolRykWi1Z8MKHCagkHig5-mPjaZOaCWi96rllUGMgfu3e0rB4B1h1l7fERJnnBjZn9vTiFlEwuQ6-1ptr_6LKv5s24fUnpKG6uTZ8mmuXO-k14EdNrf20UH2A1CoVzguQ65jIQBe2r9rbBQblgHWBCADIwd3gJ3-l8VZaz_M82qf88oY2ybAc1rcwq5dIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
«نفت در جریان است، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد، جهان امن خواهد بود! بازارهای سهام غرش‌کنان پیش می‌روند، مشاغل در سطح رکورد هستند، و قیمت‌ها در حال کاهش‌اند؛ مقرون‌به‌صرفه شدن! کشور ما مثل هیچ‌وقتِ دیگر قدرتمند، امن و محترم است. «خواهش می‌کنم!» رئیس‌جمهور دی‌جی‌تی»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76480" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jCN-zxopRhczRV5nZ9DOue1-FHGhPsDeoVj13ivhDHNofMZNWsLIx0iVVtOJlaE47Q5g708U-8P3PA0KG0maE4UcRm9Do2wMWyaAtK9DfR4uJGLigRn7Hc5z_cz4BW-yL0cFMzM_h7gJRolsgjUCwHzO00CJpe7M2ftE-h09QTDQIyRD2B-QuKJmjx6yMxGWFZGuIOHZ5B4iF800jqG_r14DcRtGItp4eNGPol8jVF-b-mLwuABFBS_UwhOByOjTL3q17mjYdeVRe1AXcEMvMau4mIMBQvBgtt2TkqQ5p1KWOfnhRQOHoMq9oyxrpCzqZbI6bppv7huCO6nzxEs93w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند دقیقه پیش ترامپ: "پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد."
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76479" target="_blank">📅 16:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X8z2c8qtX75RGqe-N7mYARbeyqNY9c4nvVwKT2MefocAjBHNeuDc3hO-qjqPrYRCteK1j3O9CyE9qpk57TQR_bZYSj_EeyZISOHCuRjwg5H3uAmoyw2dBRXsIFQ8ggauNdH8Jez3EW9MkNN0G06ZtTrN4u5da-31D6NUFPtYvunqQBPl5glyN0P2-VUqX_6hLUlY9UDFwTCo5rnRWrsqNRr3SVyDOAejLJknkjhlpZXrZPGlL2S6MT0l-Yt_ERGZ_izDj4x3KdsXoLZokMuEwsIur9EwK8D3KA7AGZTgbQKoqBKK6MlN1sbds0tzP3LmKmw23OXxYK9Q76oY9CiiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند ساعت پیش ترامپ:
این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سخت‌گیر نبوده‌ام، در حالی که بازار سهام همین الان به رکوردی تاریخی رسیده و قیمت نفت هم دارد «سقوط» می‌کند، یا حسودند، یا آدم‌های بدی هستند، یا احمق‌اند.
آمریکا را دوباره عظیم کنیم!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76478" target="_blank">📅 16:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fj7vFkM7HYkU14zzeUgEtacCevcV7P7WD-1AVnEmhnPqcYROvP-wmU6wHZZBrSMtdiLaEBa-IW8WYSf1imgUQKyYFEFgrQ3XImF-JFyjISiKruRXeU_kgOeg9iB38pvFrrn1yGMkQL6mNAbEfu1ZV8YdgymEku9zMCk0R1l4Hhje-u-toRxBc1Pcs3O_G2vu-rtq9KJwRFcL-TQd_FXmu0jmXR9HR2NvihpVm88frDE0Fx7R3-tCIKUSrxQXef0qcyY2wlJJQsmZs3wsIyXIZhtlNITw3G-KIPwS8HbmqXhcqtqqSIxRaoZgVdCbSqEwCXPFmfxVOO_bAIMq4_5rZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز پنج‌شنبه ۲۸ خرداد در یک موضع‌گیری درباره تفاهم‌نامه اسلام‌آباد تأکید کرد که ارتش آمریکا قرار است «چماق بزرگ پشت مذاکرات» باشد.
او همچنین تأکید کرد که هر گونه تغییر در اندازه حضور نظامی آمریکا در خاورمیانه «بسته به شرایط» خواهد بود.
این نخستین اظهار نظر هگست در پی امضای تفاهم‌نامه اسلام‌آباد میان تهران و واشینگتن است که بامداد پنج‌شنبه توسط رئیس جمهور ایران هم امضا شد و رسمیت یافت. دونالد ترامپ ساعتی پیش از مسعود پزشکیان سند را امضا کرده بود.
متن تفاهم‌نامه‌ای که دولت آمریکا به امضایش رضایت داد حتی از چند روز پیش از امضا شدن هم انتقادهایی در پی داشت، انتقادهایی که با انتشار متن کامل آن افزایش یافت.
به نظر می‌رسد که سخنان وزیر دفاع آمریکا هم تا اندازه‌ای پاسخ به همین انتقادها باشد.
به گفته پیت هگست،‌ آمریکا «از موضع قدرت به توافق با ایران رسید».
@
VahidHeadline
وزیر دفاع آمریکا همچنین گفت که برخی کشورهای اروپایی آماده‌اند در عملیات پاکسازی مین‌ها در تنگه هرمز مشارکت کنند.
هگست در عین حال از بریتانیا خواست نقش گسترده‌تری ایفا کند و گفت که این کشور باید «گام بیشتری بردارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76477" target="_blank">📅 16:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqmWTojHYp9IAC6R-qQvxk0MGd3kN-B1Tq5NhDNF3uFxqzetPml4oqtsYB-ubNS8WGAlIBBhipYtk4lA06bq5JxDXUsBWcVWYJkZY9r8neVi-eOmZul_Mpp1oQqjdY2TUzklQmAB3xL_2kW8eHBloi_15HK-7oYBnHrNEzuyZdKE5EePtPvX57nVlAKsOihZrjedW15O2X1YMPZAk5I0_PWmKLYmNL8aEMEwq9VIOl7S6vTDIN3dpCA6nglXxBD24LL-DLcESEocNIzr2gqroWnGodkBjtSb7iGcaaqa2jMAlQY6OKgiX6Tj5QDE51QbbdeRJOx7CORNYOOWYH658g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه کیفری استان قم، پرستو احمدی، خواننده، و هشت نفر دیگر از دست‌اندرکاران و نوازندگان «کنسرت کاروانسرا» را به‌طور جداگانه به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال ممنوعیت از فعالیت هنری محکوم کرد.
اتهام این هنرمندان در این حکم قضایی جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» عنوان شده است.
پرستو احمدی ۲۱ آذر سال ۱۴۰۳، به همراه گروهی از نوازندگان مَرد شامل احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا، در کانال یوتیوب خود ویدئویی بدون حجاب اجباری، از «کنسرت کاروانسرا» یا «کنسرت فرضی» را منتشر کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76476" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IUs9RI0I-uD_Zxfmc09StTr-yXqe9I3nYPNafe316PxYmr-6qs6HEj9uGCNlPFrfsmuNCK-IKGzaoOC0vRDk-clB_Smfy9IeBKC8gdM1oCHNeDklrpRdt2unVGhhVSJfUefKQ1_FA07VjzUsAOB9zG6LSixqQmvdLwStNNd5WShx4T62RYN9ssBzp2APVj20C3xJi0SIo04oXYiuUsIX6XytHJJVOp6EYYH2S-_MiiT1S5luYuppEjiswXzkHtxAs8Fp4xYB1o9vheb65YApSOdvBNJZd_YusvvVz1RgGIKoH-hLpAQCst-z-qM7U8fkQDS2nyRkD_1VnS1X9d6g9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره:
ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76475" target="_blank">📅 05:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nFc_iWxvcAj4X8JbMcG2SQ2C7-o7daZt-W8fviOpbDxR8xuBoiW5AiLm1IVhMrqq6-svIuAiZPi-cFLT9U9oeHnpl0qHJ_VJvqTy_bt6Cf7Ap1xpdB-iOIGgTkjwYbhGGQ4ghZbDqlKjK-ko32f1_pDfadmAAUw6U9_7iny1pQYywhukqMF5e5qkKMFK2L1FaK1BVn8xuQ_v3eMOodJh-b83pd1L--9DOliZKGRh5d4vMPPWqw2N9yypiqSk4I0c5D7Qu6ESoDMdFtHN6BDWVVNTGpfMdy1uk3y5U054CO6PwdHZVN2c9Lkf4fWw69Mai9gXSSe4Y6AqzWV62QZYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درستش کردم
MahvashJebeli
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76474" target="_blank">📅 04:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IiPYaOYz2dzeUSF-rgBVkeJJxtzcuODqQBn5pw853jq7KY367rLn2tjhh-HQgZem-aO3bSwQuL2fcQXki1RmvrzFJ0kiMDB3XWu3tp9QH7ag75d7ERncN_YNQYFGyH_JpwGkBboie7ezEf7qONp-mRLHERnKDouz3Ll6kW5eec-pijYK_QjBltEu8cWSChNzryRaMxib58QUoZLc1Eyr7FRbpqq2g4lawlpghsF3NkH2jSNKYoG5JfuUjKf9k3iL938KvmMoC3gmWPECXovzjnqxGUT1bEfZS0cuLsTFy7AfW9xZdHpYCUwOhS0NUQXFYFvsaWjZHYj2UElk25AleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L5l-xAiDrkkjkqd6g3YE-51YhELEtmgZAEHNJ0eKVRh6O2WlMGRoXWnbKZpqXK0XGZ15UntxRL1tINMT7GCMMvN5zORObjH43lGcwICiXgz9i_HI6_suiySj2rK7BEBThq980AuBGkUA-qrGMo0YlR6P72-Ow_6tDAEb0ZYEPMO1so67IA8IDNepy15k_sl5MQAErs9cnmKiNW4DURTIdQJUSQeDvpQVhs8DyFuSzMa7nCK0RsXx-sZuewFnptPkme_lmJ2JonRlN8IXlLqySeRUoccE6f9ZFqRG5RvmOQCI0mHm6BmfuP-uu4RfrehJ3gMoL3NT7X9ey5XPzLnFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sy6hRa4WrvBmNf4zFwV0xqwD9bt54a0zoEz3kqRY0IUfZDGWBByOaVooJGC4kyDxyQFzfLm-OC_Vg4GaRtopG-txMkZ0_MlpkpGGGFfNZtVlQJg2fUmF6EWzJfclRtUlp6GorT04LUjPF1Q7DzmpPTvrKGfpKJpojp1c2a5oXcd1CmdzhRpllIi2A1OZHZto18hhiSat1CF57ogaMZxxxpAJnpOc-3H8PDrmd_dw3Hv-RcqmnEzxaUmomsucFvUn0RK_bRBTur4JH9AoyulrUklohr1wCiODNJRgn2fwajx60iXJ6caWgASvwWm84woQtAZf60jKi1ph43zeWKfYvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امضای پزشکیان پس از
امضای ترامپ
تصاویر منتشر شده از سوی ایرنا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/76471" target="_blank">📅 03:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6a09c6ccc.mp4?token=HBhKccgBR-Mb-gp_V5r5wN8x8OaeZXAhAnEyrtKOfCrw9AmymNz8B5tZBfSjlHsHEl8priF9Kx-Vg7SVCL6RIAWCVef4wQOlTEsZ7Y8sUysFvAipV-0OVWTOqsS4eDoQ2a4ZiDnPv0ADDeSuvSqK0MkdSMPq7ZIkxxwpimi7RUSE6e2qxNTKRFp_iyOSbJZGh4CdosQOMUZaF1AXlhPt3yhulq_-PmUdR9rBkvA6zbTbp4UrH60FUpLjWXOxaVdJ4RMDtJwHsxYzFt58HYyiVTf6DK-UQxj5H8WBY8khLFxUZQ4g6TgH6C51XA8ERNu6D0SSRLUekkmHeuIwoy8-Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6a09c6ccc.mp4?token=HBhKccgBR-Mb-gp_V5r5wN8x8OaeZXAhAnEyrtKOfCrw9AmymNz8B5tZBfSjlHsHEl8priF9Kx-Vg7SVCL6RIAWCVef4wQOlTEsZ7Y8sUysFvAipV-0OVWTOqsS4eDoQ2a4ZiDnPv0ADDeSuvSqK0MkdSMPq7ZIkxxwpimi7RUSE6e2qxNTKRFp_iyOSbJZGh4CdosQOMUZaF1AXlhPt3yhulq_-PmUdR9rBkvA6zbTbp4UrH60FUpLjWXOxaVdJ4RMDtJwHsxYzFt58HYyiVTf6DK-UQxj5H8WBY8khLFxUZQ4g6TgH6C51XA8ERNu6D0SSRLUekkmHeuIwoy8-Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه امضای یادداشت تفاهم از سوی ترامپ
دونالد ترامپ، رئیس جمهور آمریکا که چهارشنبه شب در کاخ الیزه میهمان ضیافت شام با امانوئل مکرون بود نسخه نهایی و منتشر شده تفاهم‌نامه با جمهوری اسلامی ایران را امضاء کرده است. مسعود پزشکیان نیز این سند را امضاء کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76470" target="_blank">📅 03:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10e61c88b0.mp4?token=ZKwA6bPVPR6EBD0BsnVnKE3Ymk_FBXwh57chH6c0RcS1IXgatNT2r--PZ_dlmQSyi1dWF7FlJydTjSSxFo2kXpzbOApylp8D66CO_gr2_mTfi0dWGSZ38FI1Wpel2aGBVq4w0QTaGEXJomB0043UPuA8WFNQAbZVDi_CHRUjFzf-kGPG9rwPBoq7safSuVu97Q4-VUXNWI0FFeG1XKpsXZ-WaxpxKA44TqNArn3G541ljkztjh8cDwklAkchJhqjaJNJeUegJL6uJdeF_Wal1sv0WI9vHUnJQgmaQ5g2wzNxtICqke1Rc6f_pRtwmKb5oaEUvEJbj5YGiyMtjAS0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10e61c88b0.mp4?token=ZKwA6bPVPR6EBD0BsnVnKE3Ymk_FBXwh57chH6c0RcS1IXgatNT2r--PZ_dlmQSyi1dWF7FlJydTjSSxFo2kXpzbOApylp8D66CO_gr2_mTfi0dWGSZ38FI1Wpel2aGBVq4w0QTaGEXJomB0043UPuA8WFNQAbZVDi_CHRUjFzf-kGPG9rwPBoq7safSuVu97Q4-VUXNWI0FFeG1XKpsXZ-WaxpxKA44TqNArn3G541ljkztjh8cDwklAkchJhqjaJNJeUegJL6uJdeF_Wal1sv0WI9vHUnJQgmaQ5g2wzNxtICqke1Rc6f_pRtwmKb5oaEUvEJbj5YGiyMtjAS0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☄️
ترامپ و پزشکیان امضا کردند
دونالد ترامپ، در پاسخ به سوال خبرنگاران که آیا تفاهم‌نامه با جمهوری اسلامی را امضا کرده است پاسخ داد: «بله امضا کردم...در ورسای امضا کردم.»
@
VahidHeadline
پیش‌تر
:
بقایی: همین الان که با شما صحبت می‌کنم یعنی بامداد ۲۸ خرداد احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
آپدیت:
توییت شهباز شریف نخست‌وزیر پاکستان
ترجمه ماشین:
باعث افتخار من است که اعلام کنم «یادداشت تفاهم تاریخی اسلام‌آباد» امروز به‌صورت الکترونیکی میان ایالات متحده آمریکا و جمهوری اسلامی ایران امضا شد. این یادداشت تفاهم به امضای رؤسای محترم هر دو کشور رسیده و من نیز به‌عنوان میانجی آن را تأیید کرده‌ام. امضای این توافق در بالاترین سطح دولت‌های مربوطه، نشان‌دهنده تعهد دو طرف به حل‌وفصل دیپلماتیک این مناقشه است. یادداشت تفاهم اسلام‌آباد با اثر فوری لازم‌الاجرا خواهد شد و در نخستین گام، جمهوری اسلامی ایران فوراً تنگه هرمز را بازگشایی خواهد کرد و ایالات متحده آمریکا نیز بلافاصله محاصره دریایی را لغو خواهد کرد.
پاکستان، با حمایت دولت قطر به‌عنوان میانجی مشترک، مراسم رسمی را طبق برنامه در تاریخ ۱۹ ژوئن ۲۰۲۶ در سوئیس میزبانی خواهد کرد تا این رویداد تاریخی گرامی داشته شود و گفت‌وگوهای فنی آغاز گردد.
صمیمانه‌ترین تبریکات و قدردانی خالصانه خود را به رئیس‌جمهور ایالات متحده، دونالد جی. ترامپ، تقدیم می‌کنم؛ کسی که تعهد استوارش به دیپلماسی و ترجیحش برای حل‌وفصل مسالمت‌آمیز، بار دیگر به پایان دادن به مناقشه‌ای کمک کرد که می‌توانست پیامدهای ویرانگری برای منطقه و فراتر از آن داشته باشد. همچنین از تلاش‌ها و کوشش‌های خستگی‌ناپذیر تیم مذاکره‌کننده ایالات متحده، از جمله جی.دی. ونس، استیو ویتکاف و جرد کوشنر، به‌خاطر نقش ارزشمندشان در این دستاورد تقدیر می‌کنم.
احترام و قدردانی عمیق خود را نسبت به حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر عالی جمهوری اسلامی ایران، و رئیس‌جمهور مسعود پزشکیان ابراز می‌کنم؛ به‌خاطر خرد، دوراندیشی و دولتمردی آنان در پذیرش آرمان صلح. همچنین مایلم تلاش‌های تیم مذاکره‌کننده ایران، از جمله محمدباقر قالیباف، عباس عراقچی و اسکندر مؤمنی را به رسمیت بشناسم؛ کسانی که صبر، پایداری و تعهدشان به تعامل سازنده، در به ثمر رسیدن این توافق نقشی اساسی داشت.
مایلم به‌طور ویژه از تلاش‌های صادقانه و تعامل سازنده رهبری دولت قطر در کمک به رسیدن به این نقطه قدردانی کنم. همچنین از رهبری پادشاهی عربستان سعودی، جمهوری ترکیه و جمهوری عربی مصر به‌خاطر نقش ضروری و مشارکت‌های ارزشمندشان در این زمینه، بسیار تقدیر می‌کنم.
همچنین مایلم به‌طور ویژه از فیلد مارشال سید عاصم منیر یاد کنم؛ کسی که تلاش‌های خستگی‌ناپذیر، فداکاری بی‌چشمداشت و نقش کلیدی‌اش در تسهیل این پیشرفت و پیشبرد آرمان صلح و ثبات منطقه‌ای حیاتی بود.
باشد که این یادداشت تفاهم، بنیانی پایدار برای تفاهم بیشتر، احترام متقابل و رفاه مشترک در سراسر منطقه باشد.
CMShehbaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/76459" target="_blank">📅 00:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">"متن کامل یادداشت تفاهم اسلام‌آباد بین جمهوری اسلامی ایران و ایالات متحده آمریکا"
به نقل از ایرنا:
https://telegra.ph/mou-06-17-2
ترجمه متن منتشر شده از سوی آمریکا
@
VahidHeadline
مقایسه نسخه منتشر شده از سوی ایرنا با نسخه  نسخه آمریکایی که بی‌بی‌سی به آن دست یافته است، نشان می‌دهد دو نسخه از این توافق ۱۴ بندی تقریبا به طور کامل یکسانند.
تنها تفاوت جزئی در بند ششم دیده می‌شود؛ بندی که با این عبارت آغاز می‌شود:
«ایالات متحده آمریکا متعهد می‌شود با همکاری شرکای منطقه‌ای، یک برنامه نهایی مورد توافق طرفین با حداقل ۳۰۰ میلیارد دلار برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران تدوین کند. سازوکار اجرای این برنامه به عنوان بخشی از توافق نهایی، ظرف ۶۰ روز نهایی خواهد شد.»
آخرین جمله این بند در نسخه آمریکایی چنین است:
«تمام مجوزها، معافیت‌ها و اجازه‌های لازم برای انجام معاملات اولیه مرتبط، از سوی ایالات متحده آمریکا صادر خواهد شد.»
اما در نسخه منتشر شده توسط ایرنا، واژه «اولیه» از این جمله حذف شده است.
با این حال، به نظر نمی‌رسد این تفاوت جزئی تغییری اساسی در مفهوم یا محتوای توافق ایجاد کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/76458" target="_blank">📅 22:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrAMsWUdqKX7Uty1KLk0hJVWFgR4xHcaJTKuWcEL3zFR4zsOnvc111cFcMCZlNf_vh98xixyOIpkYuF_L8D5Jr6imVAev_puw7ZPpW9TAp8lSffGJw8puv2IUGeUx8Zpb5lasfLOoH66oCIzZscxDHT3gI6BknaVbmlYkAsHvZRB5K10y2UIwpeh13oBQ5d_pNOWB7ynUom9mQGKid_LLHvyAC_JsOb_L4c9ucgPniraOnXEqKaKJCiXXuDsBJNmGqhWR77Jry_07p3vOBulG6RByQ-oyjVHIcGrpzqWl4C5LVE840qKxgYBYMZEYNmdU8OJe1N08eYyIsmjz2uplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی روز چهارشنبه از احتمال امضای توافق پایان جنگ توسط روسای جمهوری ایران و آمریکا خبر داد و گفت این مسئله «در حالی بررسی است».
به گزارش رسانه‌های نزدیک به حکومت ایران، اسماعیل بقائی درباره احتمال امضای یادداشت تفاهم از سوی مسعود پزشکیان و دونالد ترامپ اعلام کرد: «این ایده مطرح است و همچنان در حال بررسی است.»
پیش از این طرف‌های ایرانی و آمریکایی خبر داده بودند جی‌دی ونس، معاون رئیس‌جمهور آمریکا، و محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در سوئیس این تفاهم‌نامه را امضا خواهند کرد.
دولت سوئیس تأیید کرد مراسم امضای این تفاهم در اقامتگاه کوهستانی بورگن‌اشتوک برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/76456" target="_blank">📅 21:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25681b6811.mp4?token=iDJZbCyDrPedHT9isDprtfT0VuF-pfaOwm8hQQr-r6nVrq7liJ2eo1jqPTndYfdOIwmxr2tAZTDdiTHkQo63RYFt6nKtTa2weCQbwbJKKqKKaOWisi43Bj1rZicNNYyAWGjAlpaZkmlxsIAd4NmN81zB6LAtFTHrYTjHlsH0aUnqYiYWOT5h0r-iYkxit5_YI2Wna3JNpSEVxeb_ithK9OqK76DP_gQHT3PXIIHR8wgi1z2PlDcdHksOOOcrvsniVfoa2fjy6x42AUmm1JWGfKyk1CVPqFmyryXmcXfH2l5Szraxl6SAcYwX0O-iwGdzFzBjo8fiH1-X8E9Lg-E83QBp9WPfT8fGjyeH0TuVbefRPIMHYBJIcoUEyUNfQkF2bKNhWdA-uXf7eSeca9eLXvy61hYPxq2g-uxi65IZhroGNNAZoXpArMunGZZ4_7rNkpDrieBhIM_nv362FMVhyuwipk48FbCbT5itIHI4GYTo0BL5aLXTt7HR_3VWOskl0Q3OHFBGfL24EGnOSO20GGSS7bbTrRl8GKcjf4nUrzQL6PNRCLsNoVt7ObdcsQOpeP9FungVIwrzpPdEOhTPy7fGNoGt4N3eeTVOAuNbHK8knK0zwCLCAugeLG60ymK5b-QCPGfNowQk9m2HPMSFF2WDgV8AZ1vY0LjYJ5xyAlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25681b6811.mp4?token=iDJZbCyDrPedHT9isDprtfT0VuF-pfaOwm8hQQr-r6nVrq7liJ2eo1jqPTndYfdOIwmxr2tAZTDdiTHkQo63RYFt6nKtTa2weCQbwbJKKqKKaOWisi43Bj1rZicNNYyAWGjAlpaZkmlxsIAd4NmN81zB6LAtFTHrYTjHlsH0aUnqYiYWOT5h0r-iYkxit5_YI2Wna3JNpSEVxeb_ithK9OqK76DP_gQHT3PXIIHR8wgi1z2PlDcdHksOOOcrvsniVfoa2fjy6x42AUmm1JWGfKyk1CVPqFmyryXmcXfH2l5Szraxl6SAcYwX0O-iwGdzFzBjo8fiH1-X8E9Lg-E83QBp9WPfT8fGjyeH0TuVbefRPIMHYBJIcoUEyUNfQkF2bKNhWdA-uXf7eSeca9eLXvy61hYPxq2g-uxi65IZhroGNNAZoXpArMunGZZ4_7rNkpDrieBhIM_nv362FMVhyuwipk48FbCbT5itIHI4GYTo0BL5aLXTt7HR_3VWOskl0Q3OHFBGfL24EGnOSO20GGSS7bbTrRl8GKcjf4nUrzQL6PNRCLsNoVt7ObdcsQOpeP9FungVIwrzpPdEOhTPy7fGNoGt4N3eeTVOAuNbHK8knK0zwCLCAugeLG60ymK5b-QCPGfNowQk9m2HPMSFF2WDgV8AZ1vY0LjYJ5xyAlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنفرانس خبری ترامپ
:‌
🔸
یکشنبه، ما به توافقی با ایران رسیدیم که همه چیزهایی را که قصد داشتیم به آن دست یابیم محقق می‌کند—همه چیز و حتی بیشتر.
🔸
اگر این توافق را انجام نمی‌دادیم، می‌توانستیم برای ۲ تا ۳-۴ هفته یا حتی ۲ سال بمب‌های بیشتری رها کنیم.
شما هرگز تنگه هرمز را باز نمی‌دیدید.
🔸
اگر من ژنرال سلیمانی را نکشته بودم، احتمالاً الان درباره این توافق صحبت نمی‌کردیم، چون او نابغه‌ای دیوانه بود.
آنها هرگز نتوانستند جایگزین او شوند.
🔸
رهبران جهان از اینکه ما به توافق رسیدیم بسیار خوشحالند، همه‌شان.
هیچ کشوری به ما نیامد و نگفت «لطفاً آقا، بمب‌ها را روی آن‌ها رها کن. لطفاً بمب‌ها را رها کن» — آدم‌های احمق این را می‌گویند.
🔸
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آنها بسیار کمتر رادیکال شده‌اند. فکر می‌کنم واقعاً کشورشان را دوست دارند. آنها خوب هستند.
🔸
نمی‌خواستم شاهد یک فاجعه اقتصادی باشم؛ اگر این روند ادامه پیدا می‌کرد، ممکن بود اتفاق بیفتد.
هر بار که درباره صلح صحبت می‌کردیم، بازار سهام بالا می‌رفت.
بازار سهام از هر کسی که آنجا هست، از جمله افرادی که روی این صحنه هستند—به جز من—باهوش‌تر است.
🔸
بازار سهام بسیار درخشان است. و هر بار که چیزی شگفت‌انگیز می‌گفتیم، مثل «ما قرار است توافق کنیم»، بازار بالا می‌رفت.
و هر بار، هر بار که چیزی منفی می‌گفتیم، مثل «ببین چی شده، ما نمی‌توانیم توافق کنیم»، بازار پایین می‌آمد — خیلی زیاد، خیلی، خیلی زیاد.
این به شما چیزی می‌گوید.
🔸
من نمی‌خواستم مثل هربرت هوور بزرگ دیر کنم. من آن را نمی‌خواستم.
[چت‌جی‌پی‌تی: هربرت هوور رئیس‌جمهور آمریکا در آغاز رکود بزرگ ۱۹۲۹ بود. در حافظه سیاسی آمریکا، هوور نماد رئیسی‌جمهوری است که بحران زیر دستش منفجر شد و بعد متهم شد که دیر، ناکافی و با احتیاط بیش از حد واکنش نشان داد. حتی محله‌های فقیرنشین دوران رکود را با تمسخر Hoovervilles می‌گفتند.
پس منظور ترامپ احتمالاً این است: نمی‌خواستم آن‌قدر صبر کنم تا بحران از کنترل خارج شود و بعد همه بگویند رئیس‌جمهور دیر جنبید.]
🔸
درباره کشتن قاسم سلیمانی:
این یک همکاری مشترک بود، همان‌طور که در کسب‌وکار املاک می‌گوییم. این یک همکاری مشترک بین اسرائیل و ما بود.
ما یک ماه آن را بررسی کردیم. تقریباً یک ماه قبل می‌دانستیم که او با کدام هواپیما سفر خواهد کرد.
او فقط با خطوط هوایی تجاری، آن‌های بزرگ و پرجمعیت سفر می‌کرد، چون می‌دانست ما او را سرنگون نمی‌کنیم. آن‌ها خیلی باهوش هستند.
اما ما می‌دانستیم که او در آن هواپیما خواهد بود، او را دنبال کردیم، و سپس اسرائیل به من اطلاع داد که آن‌ها این کار را انجام نخواهند داد. و من باید تصمیم می‌گرفتم.
و من به او گفتم، «خب، اگر اسرائیل این کار را نمی‌کند، ما همه آماده‌ایم. آیا انجامش می‌دهیم؟ دوست داری انجامش دهی یا نه؟» گفتم، «البته، اگر می‌خواهی انجامش دهی، ما می‌توانیم انجامش دهیم.»
🔸
درباره نتانیاهو: بیبی نتانیاهو مرد خوبی است. گاهی کمی هیجان‌زده می‌شود، اما اتفاقاً مرد بسیار خوبی است.
ما یک اختلاف کوچک درباره لبنان داشتیم — من گفتم، می‌توانی کمی ملایم‌تر باشی، بیبی، لازم نیست هر بار که کسی وارد می‌شود یک ساختمان را خراب کنی؛ این کار حزب‌الله است.
🔸
نتانیاهو به کشور آمد و از باراک حسین اوباما، رئیس‌جمهور، التماس کرد که برجام را انجام ندهد. او گفت این می‌تواند پایان اسرائیل باشد، و اگر من وارد ماجرا نمی‌شدم، همینطور می‌شد.
و اوباما به او گوش نداد.
بیبی واقعاً به کنگره رفت و از آنها التماس کرد، اما به جایی نرسید. و آنها این توافق وحشتناک را داشتند که برای اسرائیل فاجعه‌بار بود.
🔸
این یک یادداشت تفاهم است. اگر در ۶۰ روز انجام نشود، اشکالی ندارد، ما به بمباران بازمی‌گردیم.
می‌دانید، من نمی‌خواهم این کار را بکنم، چون خیلی خوب است، خیلی خوب.
اما، خب، ممکن است مجبور شویم، چون هرگز اجازه نمی‌دهیم آنها سلاح هسته‌ای داشته باشند.
🔸
توافقی که ما با ایران روز یکشنبه به آن رسیدیم، به زودی امضا خواهد شد، فردا، شاید روز بعد.
🔸
ترامپ درباره اسرائیل:
فکر می‌کنم آنها می‌توانند در مورد حزب‌الله بهتر عمل کنند. نمی‌گویم نباید از خودشان محافظت کنند، بلکه می‌گویم — وقتی دو پهپاد به بیابان شلیک می‌شوند و بی‌خطر سقوط می‌کنند، نیازی نیست ساختمان‌ها را در بیروت خراب کنند.
آنها می‌توانند بهتر رفتار کنند. و صادقانه بگویم، آنها می‌توانند کار بهتری انجام دهند — من آنها را دوست دارم، به عنوان یک شریک عالی بودند، اما می‌توانند در مورد حزب‌الله خیلی بهتر عمل کنند.
🔸
ترامپ درباره ایران:
خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
پس کسی باید به آنها کمک کند — خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
تقریباً هیچ‌کس چنین پولی ندارد — این همان نوع خسارتی است که وارد شده است.
🔸
آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند.
🔸
درباره موشک:
ما در حال کار روی یک تلاش موازی با کشورهای خلیج فارس برای رسیدگی به مسائل غیرهسته‌ای هستیم، مانند موشک‌های بالستیک متعارف، که درباره آن صحبت خواهیم کرد و حمایت خواهیم کرد.
منظورم این است که آنها باید مقداری داشته باشند، چون دیگران مقداری دارند، شما هم باید داشته باشید — کسی این را گفت، «نباید به آنها یکی بدهید»، و من آدم‌هایی دارم — بعضی از این آدم‌ها را دوست دارم، اما فکر نمی‌کنم این را، فکر نمی‌کنم آنها باهوش باشند.
«البته، نباید اجازه دهید هیچ موشکی داشته باشند» — من گفتم، خب، من چه کار کنم، آیا می‌خواهم به عربستان سعودی اجازه دهم موشک داشته باشد، اما آنها نداشته باشند؟ «بله، قربان.»
اینطور کار نمی‌کند، می‌دانید، اینطور کار نمی‌کند، و موشک‌ها مشکل نیستند — موشک‌ها به یک مکان کوچک برخورد می‌کنند، اما سیاره را منفجر نمی‌کنند.
🔸
اگر آنها به توافق احترام نگذارند، یا برخی موارد حتی در توافق ذکر نشده باشد — این یک یادداشت تفاهم است، اما ما درک مشترکی از برخی مسائل داریم بدون اینکه آن را مکتوب کنیم — و، اگر آنها به آن احترام نگذارند، احتمالاً دوباره به بمباران آنها باز خواهیم گشت تا زمانی که به آن احترام بگذارند.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کار می‌توانند بکنند.
🔸
مردم می‌خواهند من پل‌ها را بمباران کنم.
من قبلاً این کار را انجام دادم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگ‌ترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن در ایران.
اما ما آن پل را بمباران کردیم، شما دیدید.
🔸
می‌خواهم از چین، رئیس‌جمهور شی، تشکر کنم، من با او بودم و او کاملاً بی‌طرف ماند، کاملاً بی‌طرف، و من این را قدردانی می‌کنم.
و می‌خواهم از ولادیمیر پوتین تشکر کنم، او بسیار بی‌طرف بود.
🔸
خب، آزادسازی پول‌ها — پاسخ آسانی دارد.
ما مقدار زیادی از پول آن‌ها را گرفته‌ایم، و پول آن‌ها را از آن‌ها گرفته‌ایم.
وقتی پول ما نیست، پول آن‌هاست و ما در یک زمان مشخص آن را مسدود کردیم.
فکر می‌کنم باید آن را پس بدهیم، می‌دانید؟
اگر پس نمی‌دادیم، هیچ‌کس دیگر هرگز در دلار سرمایه‌گذاری نمی‌کرد.
🔸
گزارشگر: یک مرد دانا زمانی گفته بود، در ژانویه ۲۰۲۰، «ایران هرگز در جنگ پیروز نشده، اما هرگز در مذاکره شکست نخورده است.»
ترامپ: این را چه کسی گفته؟
گزارشگر: دونالد ترامپ.
ترامپ: اوه، فکر می‌کردم همین را می‌خواهی بگویی.
🔸
اگر آنها پرچم سفید تسلیم را بالا ببرند و بگویند «سپاس خداوند را که دونالد ترامپ بزرگ‌ترین رئیس‌جمهور تاریخ است»، نیویورک تایمز و سی‌ان‌ان خواهند گفت «ایران پیروزی بزرگی به دست آورد.»
🔸
راستی، محاصره تأثیرگذارتر از تمام حملات هوایی بود، جایی که ما بمب‌هایی به ارزش یک میلیارد دلار روی ایران ریختیم.
🔸
گزارشگر: چرا حالا برای شما قابل قبول است که آنها بخشی از توان موشکی خود را حفظ کنند؟
ترامپ: آنها چه چیزی را حفظ می‌کنند؟ آنها اکنون کمتر از دیگر کشورها دارند.
ما احتمالاً ۸۴، ۸۵ درصد از موشک‌هایشان را از کار انداختیم، بقیه زیر زمین هستند و حتی نمی‌توانند آنها را بیرون بیاورند.
🔸
ترامپ درباره ایران: آیا می‌خواهید اجازه دهید ۹۱ میلیون نفر از گرسنگی بمیرند؟
🔸
خبرنگار: آیا اکنون می‌توانید بگویید که آیا کسی در دولت شما بابت حمله به مدرسه‌ای که در اولین روز جنگ بیش از صد کودک را کشت، مسئول شناخته خواهد شد؟
ترامپ: اشتباهاتی رخ می‌دهد، جنگ چیز زشتی است، می‌دانم که در حال بررسی است.
من از پیت هگست سؤال می‌کنم چون آن‌ها در حال بررسی این موضوع هستند.
🔸
خبرنگار: چرا برای مراسم امضای توافق صلح ایران نمی‌مانید؟
ترامپ: ممکن است بمانم.
🔸
گزارشگر: آیا در این موضوع عنصری وجود دارد که شما معاون رئیس‌جمهور را بفرستید، اگر موفق شد که عالی است، شما به عنوان کسی که او را فرستاده نابغه به نظر می‌رسید. و اگر موفق نشد، تقصیر معاون رئیس‌جمهور است.
ترامپ: من این ایده را دوست دارم. خب، به این صورت، اگر موفق شد، من اعتبارش را می‌گیرم. اگر موفق نشد، تقصیر JD است.
بهتر است مراقب باشی، JD. او هواپیمایش را برمی‌گرداند و از اینجا فرار می‌کند.
بله، من این ایده را دوست دارم. فکر می‌کنم ایده خوبی است.
📡
@VahidOnline
بخش‌های بالا رو من انتخاب نکردم. هم‌زمان با حرف‌هاش از منابع خارجی با ترجمه ماشین گذاشتم.</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76455" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ux_nmoze9_q9nWsQyfTYTGmAgxI90YJxr6dhHZDpXSH_kx8mtmPgi7gzxU2cuZef8qs2fKxqX3mWPGDiQLRV6bfBkbYTQxSvpyba6Mu6n90etuvlkjQakB_-ekMzzp3P2oXWkIS-LoArUA2nAedQVYBUwGcvZRRW3_wWpR4mOlalMXtrmXcvot-hUaclnoW9pJf-JLroAWCIZxThjhwxFJwjfLOcEiGlrzClAeHV-MEz8SBnbvrSU7k2jdcFlrW4ta3GxJVNRHP0RVJf6acTduI1KGnGRbmu6ImCo1JsiXUHg9zlM_kmJ-Z07EbCkPUsAxk9ysyfWwU7uAYdswHEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای هماهنگی بانک‌ها، روز چهارشنبه ۲۷خرداد ۱۴۰۵، اذعان کرد بخشی از خدمات چهار بانک ملی، تجارت، صادرات و توسعه صادرات پس از گذشت چهار روز همچنان با محدودیت روبه‌رو است.
این شورا پیشتر در ۲۳ خرداد از وقوع یک «حمله سایبری محدود» به این چهار بانک خبر داده و اعلام کرده بود که این حمله موجب اختلال در ارائه برخی خدمات بانکی شده است.
رسانه ایران آی‌تی گزارش داده است که بر اثر این اختلال چند روزه، میلیون‌ها کاربر همچنان به حساب‌های خود دسترسی ندارند. این رسانه با انتقاد از وضعیت پیش آمده نوشت بسیاری از فعالان بازار از انجام معاملات مهم در بورس، طلا و سایر دارایی‌ها بازمانده‌اند.
شبکه بانکی ایران در سال‌های اخیر بارها هدف حملات سایبری قرار گرفته و در مواردی نیز اطلاعات مشتریان برخی بانک‌ها در فضای مجازی منتشر یا خرید و فروش شده است.
با وجود این، شورای هماهنگی بانک‌ها تاکید کرده است که سپرده‌ها، تراکنش‌ها و اطلاعات مالی مشتریان این چهار بانک در «امنیت کامل» قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76454" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tdfYOZv1_Rkyh6OFQfin7dlKWvadaQ3H4UtBLTduwEwl-ivH5Llhvt3FrWIhAnbLfWP9naN4B0yENDv1YU_sf3mRUZ4-vB5Nec620RmHVemn0Bio9qGufBcuQbPMK1qLonMo6WBrBz1i-7aipyVf9wIlr8SB-lP3PEV8WUbNERoE9GzxlK0S4w4yFaVpcTmlFa8fSuMNm0MvrINDViLNfWt76PoQFklsqpIN3lFCm1Fz3vZTCs2CmdMpPZ-8A09Wmo1WAE4bXlNuiXYrKTNoUh1JIFn-U2HzEL5eoOBgRScf05rp4bWE1aWXCJEIQ5QO6EeKAlVafBu4GHp8c3l2LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم‌نامه ممکن است زودتر از نشست سوئیس امضا شود
آکسیوس، ترجمه ماشین:
آمریکا، ایران و میانجی‌ها در حال گفت‌وگو درباره برگزاری مراسم امضای یادداشت تفاهم هستند؛ مراسمی که در حال حاضر برای جمعه برنامه‌ریزی شده، اما به گفته یک دیپلمات از یکی از کشورهای میانجی و یک منبع دوم آگاه از گفت‌وگوها، ممکن است زودتر و حتی روز چهارشنبه برگزار شود.
چرا مهم است: اگر چنین اتفاقی بیفتد، یادداشت تفاهم به‌صورت الکترونیکی امضا خواهد شد، بخش‌های مربوط به تنگه هرمز در توافق اجرایی می‌شود و آمریکا ممکن است سرانجام متن توافق را منتشر کند.
منبع دیپلماتیک گفت گفت‌وگوها درباره جلو انداختن جدول زمانی با هدف باز کردن تنگه هرمز زودتر از جمعه انجام شده، چون هر دو طرف درباره این موضوع توافق داشتند.
عامل دیگر می‌تواند فشار سیاسی بر کاخ سفید برای انتشار متن یادداشت تفاهم باشد.
منبع آگاه از گفت‌وگوها مدعی شد این ایران بوده که خواسته متن تا زمان امضای رسمی منتشر نشود و رد کرد که کاخ سفید در واکنش به فشار سیاسی چنین تصمیمی گرفته باشد.
وضعیت فعلی: تا صبح چهارشنبه، هیچ تصمیم نهایی درباره تغییر زمان امضا گرفته نشده بود.
کاخ سفید از اظهارنظر خودداری کرد.
خبر اصلی: حتی اگر زمان امضا تغییر کند، نشست هیئت‌های آمریکایی و ایرانی، به ریاست معاون رئیس‌جمهور ونس و محمدباقر قالیباف، رئیس مجلس ایران، طبق برنامه روز جمعه در سوئیس برگزار خواهد شد؛ این را منابع گفتند.
انتظار می‌رود آنها درباره آغاز مذاکرات بر سر برنامه هسته‌ای ایران گفت‌وگو کنند.
نکته مبهم: یک مقام ارشد دولت به خبرنگاران گفت این توافق روز یکشنبه به‌صورت الکترونیکی از سوی رئیس‌جمهور ترامپ، ونس و قالیباف امضا شده است.
منبع دیپلماتیک مدعی شد چنین امضایی انجام نشده است.
منبع آگاه مدعی شد که این امضا انجام شده و امضای جدید یک «امضای دوم» خواهد بود. روشن نیست چرا دو امضا لازم بوده است.
چه چیزی را باید زیر نظر داشت: کاخ سفید از روز یکشنبه گفته است که باز شدن تنگه از سوی ایران و لغو محاصره آمریکا فقط از روز جمعه، پس از مراسم رسمی امضا، آغاز خواهد شد.
به گفته منبع دیپلماتیک، اگر توافق زودتر امضا شود، این روند هم جلو خواهد افتاد.
axios.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76453" target="_blank">📅 19:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc6738c570.mp4?token=UY6kENIuBCcDu8hkhS8DlpsxMWx2aasfQmF06oXT8LbegML8Wq9sk7yAeeMMa1zWrp9FEn9Rf3Tdh7sU_sHDA7mYtbssMQR1v7fihCjCu1m-YOObMOKnzVzwOnb3V7qKUFG7I_rm4OGFP1vbjo7FfKm1iIDLP9YJU0NNnkZrWoc4PecgF2Z_NF7LRSQc1mFiy-_Q13K2sDu6iDxUA49Eq9WVsWijsf9SFnujf64yIgqGvPcy6kmCfIPufg5D2xAGlnSidQNG5wv3G7VFnx_rtEHjjKj9Ensnv_mpFh8QYehyJxvAJ39M7CxvEo6gEdHSI63ZsjcEQqW-VWW9jaF1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc6738c570.mp4?token=UY6kENIuBCcDu8hkhS8DlpsxMWx2aasfQmF06oXT8LbegML8Wq9sk7yAeeMMa1zWrp9FEn9Rf3Tdh7sU_sHDA7mYtbssMQR1v7fihCjCu1m-YOObMOKnzVzwOnb3V7qKUFG7I_rm4OGFP1vbjo7FfKm1iIDLP9YJU0NNnkZrWoc4PecgF2Z_NF7LRSQc1mFiy-_Q13K2sDu6iDxUA49Eq9WVsWijsf9SFnujf64yIgqGvPcy6kmCfIPufg5D2xAGlnSidQNG5wv3G7VFnx_rtEHjjKj9Ensnv_mpFh8QYehyJxvAJ39M7CxvEo6gEdHSI63ZsjcEQqW-VWW9jaF1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهوری آمریکا در دیدار با نخست وزیر هند در حاشیه نشست گروه هفت گفت: تغییرات جمهوری اسلامی با دستور من برای کشتن قاسم سلیمانی آغاز شد.
دونالد ترامپ افزود: جمهوری اسلامی رده اول و دوم رهبری خود را از دست داده و اکنون با توافق من هرگز به سلاح هسته‌ای دست پیدا نخواهند کرد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، گفت از حق اسرائیل برای دفاع از خود حمایت می‌کند، اما انتظار دارد این کشور در تصمیم‌گیری‌هایش «قضاوت درست» داشته باشد.
@
VahidOOnLine
ترامپ در پاسخ به پرسش خبرنگاری که از او پرسید «آیا برخورد گرم رهبران اروپایی نشان‌دهنده همسو شدن آن‌ها با جهان‌بینی شماست؟»، گفت: «فکر می‌کنم آن‌ها به این نتیجه رسیده‌اند که حق با من بود. یک‌جورهایی همیشه حق با من است و در نهایت، آن‌ها هم معتقدند که حق با من بود.»
رئیس‌جمهوری آمریکا که در کنار نارندرا مودی، نخست‌وزیر هند با خبرنگاران صحبت می‌کرد، با اشاره به تمایل ناگهانی دیگر کشورها برای ورود به فرآیند توافقات اخیر افزود: «حالا یک‌دفعه همه‌شان می‌خواهند وارد ماجرا شوند و مشارکت کنند؛ در حالی که کار دیگر تقریبا تمام شده است و اصلا دلیلی ندارد آن‌ها را مشارکت دهیم.»
@
VahidOOnLine
بقیه حرف‌هاش (بی‌ربط به ایران):
۲۰ دقیقه ۲۲۰ مگابایت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76452" target="_blank">📅 18:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LBi9s1rmjFcd_WC7xYGTo62Tw6k9kDocWZZZEXeIEZAFgDflrAp-FtQuY3pR_N-8m2c_5gjKOfVYjyUXvOoZPlYIPQgvhtJUK-YTNMehFK_mK-i2v-RrpuiolEXTddQOtvEda-hdwr7jKeYJsRzWshEeLJTZUmvr47ye2d7U-ngaV79XLBqmsQrfVBFfybmM8CC_i2PXccS1EpaH7mxGWkXkB-0t2kSTmhaKx8fhqiGazZwaXH6cUCKZDLnxiPA2bzWgqM3C8HkPb07TNnMRpfLWa_9NizelYGWycJN4Hv7Ybh0Irtc_CqzVnCeXtCWNGaQxy1tM7JPqo2zGqc1Hrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من ۴۵ دقیقه دیگر از فرانسه یک کنفرانس خبری برگزار خواهم کرد. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه بازمی‌گردم!
این سفر موفقیتی بزرگ بود، اما چیزی که بیشتر از همه می‌خواستند درباره‌اش حرف بزنند، این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد.
در همه شاخص‌ها، ارقام مربوط به اقتصاد ایالات متحده عالی است؛ امروز شمار افرادی که مشغول به کار هستند از هر زمان دیگری بیشتر است. بیش از ۱۹.۱ تریلیون دلار در آمریکا سرمایه‌گذاری می‌شود، کارخانه‌ها و همه چیزهای دیگر در حال شکل‌گیری است؛ اما نکته مهم این است که ارقام اخیر بازار سهام به خاطر این توافق سر به فلک کشیده و به همین ترتیب، قیمت نفت هم به‌شدت در حال سقوط است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76451" target="_blank">📅 17:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl5hFpOnGaHXUF0dku8TJQBcfDh1P2WAnhoBFHYZmRAZ44VdphqSL5VQboNmSPcnrpAEsnjWYHnP83E0VoslAMhvMLxBauMBO0YiO7RTPeTCuOxyCJuRW1zVK6rByM53X5RSC9nMBjYDkLdggTZOQqKQWr7vpcv_Njc88XUmqgWUDMII_59zFwT58p_20pckjMPQKXOhYQQ7-Ln4Birf1UZOvJJ4D6gNgNL4RT3n_ypGh1GhB0h2FQWwhaX0IS3-Yr4Bbvn0UNLQJoCOsYeptXuv4cLXZn57C0cb0_oFqn1RKusDBXE-QwSnKqeliCyA9XbTEA2PeSldKe1teIbHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، در گفتگو با برنامه صبحگاهی شبکه سی‌بی‌اس (CBS)، از سیاست‌های دولت دونالد ترامپ در قبال جمهوری اسلامی ایران دفاع کرد و به انتقاد از کسانی پرداخت که به گفته او، صرفا به دنبال تداوم درگیری نظامی هستند.
ونس با تفکیک میان «ابزار» و «هدف» در سیاست خارجی واشنگتن گفت: «رئیس‌جمهوری از دیپلماسی، اهرم‌های اقتصادی و فشار نظامی استفاده کرد تا مطمئن شود ایران به سلاح هسته‌ای دست پیدا نمی‌کند؛ هدف اصلی همواره همین بوده است». او با انتقاد از تندروها افزود: «بعضی‌ها فقط می‌خواهند بمباران‌ها ادامه داشته باشد، بدون اینکه توجه کنند آیا این کار اصلا دستاوردی برای مردم آمریکا دارد یا خیر».
معاون رئیس‌جمهوری آمریکا در پایان تاکید کرد که هدف ترامپ ایجاد بدبختی و رنج برای مردم ایران نیست، بلکه تمرکز اصلی دولت او، مهار برنامه‌های تسلیحاتی و جلوگیری از دستیابی تهران به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76450" target="_blank">📅 17:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76449">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UpeMrgfHZKnqbBF8EK6Hj7Y0pt9D11s_wyopn26vTBCVqurxA4541a9oUWYCz3iD8MJvDWWjrDEKXQIJ89yuDybVoO-Tvl_nhPiiSh7V1TAO0pBOQqVyh9hhvx0o63uZSDH79qOKpW6XHtACz2y0Uf0kbo-mvfU73Fz2t83jt-tqa8uQ4qFJzv5C6zPYR8bc3lHUldREpvWRS-_dUu-fcPUbMQbJKkdkAtRGNp5OxnicmKxxTBreFamKRQCr2gClUYSil7ZPYXuo-fPZBCLZhu8riFqZaAkvwo_DKWJYBBtukKWJPu9BY22JfOoeh_N6aZwL44_PM-Qn3Awm6BKqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76449" target="_blank">📅 17:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/790e3a4857.mp4?token=ts34lvAna50bqUoauvWLrl6Z8jDd5C18tELFbMfW3qwGwiLsRTL4yQiBXN25zRvNz80ZK87eQg_jOXxpm625wVizxXpmdOgjVfED_6ORFWqGennk6LlqU8ZHkzhMgeQcV4U03KaEQyEX5kfkTdKaqrlGr2Yr_YupS-x1BLEX2pX4fPKBrkM8Bm0Y0tQl3EVMZYJnPwo88-t0LnhGTKJAsnWXS-NiYGw-JBLiJWS6WyWBAVavWiA0-4meBMsEA-Ik4NgfT4b-AkLEbBQWXgBDhQKMrIt1ZNDMjFu7uWFkSRptJtQYkN91BWgD79g-k1aVgiUWgvjOBhQNPSM1Xet1ag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/790e3a4857.mp4?token=ts34lvAna50bqUoauvWLrl6Z8jDd5C18tELFbMfW3qwGwiLsRTL4yQiBXN25zRvNz80ZK87eQg_jOXxpm625wVizxXpmdOgjVfED_6ORFWqGennk6LlqU8ZHkzhMgeQcV4U03KaEQyEX5kfkTdKaqrlGr2Yr_YupS-x1BLEX2pX4fPKBrkM8Bm0Y0tQl3EVMZYJnPwo88-t0LnhGTKJAsnWXS-NiYGw-JBLiJWS6WyWBAVavWiA0-4meBMsEA-Ik4NgfT4b-AkLEbBQWXgBDhQKMrIt1ZNDMjFu7uWFkSRptJtQYkN91BWgD79g-k1aVgiUWgvjOBhQNPSM1Xet1ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: خامنه‌ای در «عراق» هم تشییع می‌شود
علیرضا زاکانی، شهردار تهران روز چهارشنبه ۲۷ خردادماه برای نخستین بار و برخلاف گفته‌های پیشین مقام‌های جمهوری اسلامی اعلام کرد که مراسم تشییع علی خامنه‌ای در عراق هم برگزار می‌شود.
زاکانی به خبرنگاران گفت پس از دو روز مراسم وداع، جسد علی خامنه‌ای در روز ۱۵ تیر در تهران، ۱۶ تیر در قم و ۱۷ تیر در عراق تشییع خواهد شد.
مقام‌های جمهوری اسلامی پیش از این اعلام کرده بودند که رهبر پیشین  در مشهد دفن خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76448" target="_blank">📅 16:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d8cc30b9b.mp4?token=BzVm7BlSfn_TSRAOS7q41-j8coD0tBjSp5HpLh_JFx9mYT0ylwZTpPq7DHgPel20i5IhrKks1UZGcxIEBk4f_lPR05_XyESa8VdV0HOgDmJw2tfB_PhfMB5FHUJAev_FVhT2SnqqF2Ey6LpZ8O-TZBPsy6-Wmet68OgK-CSQWc8bj_qjAtDVVR3qm8Y8rTYQDX9YLVWLTmxgrQiBxak60jl3Br_HY42Ype6bNXXRsdaDmUP-QJh7EnwDQCXwxW-Wsw2ndRbyIYVsLq7h8qmztQm673D0Gl82TkHGOTgZ3fRd_NfxRf8FvdFfBkWzspdS1x50tDiHe6xqt7xoBJ5VZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d8cc30b9b.mp4?token=BzVm7BlSfn_TSRAOS7q41-j8coD0tBjSp5HpLh_JFx9mYT0ylwZTpPq7DHgPel20i5IhrKks1UZGcxIEBk4f_lPR05_XyESa8VdV0HOgDmJw2tfB_PhfMB5FHUJAev_FVhT2SnqqF2Ey6LpZ8O-TZBPsy6-Wmet68OgK-CSQWc8bj_qjAtDVVR3qm8Y8rTYQDX9YLVWLTmxgrQiBxak60jl3Br_HY42Ype6bNXXRsdaDmUP-QJh7EnwDQCXwxW-Wsw2ndRbyIYVsLq7h8qmztQm673D0Gl82TkHGOTgZ3fRd_NfxRf8FvdFfBkWzspdS1x50tDiHe6xqt7xoBJ5VZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس جمهوری اسلامی و رییس هیات مذاکره‌کننده جمهوری اسلامی با آمریکا، درباره اهمیت روابط اقتصادی با چین گفت جمهوری اسلامی باید از مرحله تقابل عبور کند و بر توسعه اقتصادی متمرکز شود.
قالیباف در نشست همفکری نماینده ویژه در امور چین با اتاق بازرگانی ایران گفت: «باید سنگر را از بچه‌های لانچر تحویل بگیریم، مردم را از زیر فشار اقتصادی دربیاوریم و کشور را بسازیم.»
او با توصیف جایگاه چین به‌عنوان کشوری «منحصربه‌فرد» برای جمهوری اسلامی در حوزه تجارت، افزود پکن باید باور کند که تهران «شریکی به تمام معنا» برای چین است.
رییس مجلس جمهوری اسلامی گفت هر بلوکی که با حضور کشورهای ساحلی خلیج فارس شکل بگیرد، محوریت آن «حتما چین و جمهوری اسلامی» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76447" target="_blank">📅 16:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kJwl6ZS2DQyhPW28Xj0oKRdMknOs3Fy_H823VEriObIOrsOEZuEhmPod_yLWfEvzg8JvZ158hdcYLEVil2wtplPiP8ojd0ur_GXuLTj5ls8ySoLQXjsa-slKT6EIe_4X-McihG6Itzr_l3e6E8oBWwJbbuBF3MShN_gRCdE43g7HUIpZwp-uT5-TOj8kyIw_0oRUdGDnf_3ZZgQCYIJtklojetb8Oah17p9SWpgdoAEC8tHcme0R5y3a1ZoEdOv2NE2V9pOf4gagzK3Ha-pyUxpo1ZUUeV-EK1XBO8cp0NejahfGkqs5_wLyP0z5buXgjSrhzA61fCYBro2arQDUpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cda5339562.mp4?token=o3Ypc7-_wTycForqgZspLRqvcwEdy0dzPfV0Tpe22Bjnd_-J8wL_6DcsE2l4Udoij0x_gEqICakz3yERfZ9ZXhxFlZLS1NQiLe0e5C4r9F2k5DwjpJ13whvjhe0DMMTte5Fbl2btEmPkvKIIt4w_lxYIs6E_cT-k0hxeidEK0oFkbGOUarVfhAsGR0zmXSXg2y476qY7qGeIpWBJ3j0vuDg_bOiKt150vfgpQozJkHQa__Mz4IS3J3o7Or-R8gVsRN3iIN3Q4QgJD9cJmONIYpM2FlekDXnf3InuyFGc4dIDsFMiTCZmE-yDEnxDlqpp2CzE-7T2NRwSZF9fd3IVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cda5339562.mp4?token=o3Ypc7-_wTycForqgZspLRqvcwEdy0dzPfV0Tpe22Bjnd_-J8wL_6DcsE2l4Udoij0x_gEqICakz3yERfZ9ZXhxFlZLS1NQiLe0e5C4r9F2k5DwjpJ13whvjhe0DMMTte5Fbl2btEmPkvKIIt4w_lxYIs6E_cT-k0hxeidEK0oFkbGOUarVfhAsGR0zmXSXg2y476qY7qGeIpWBJ3j0vuDg_bOiKt150vfgpQozJkHQa__Mz4IS3J3o7Or-R8gVsRN3iIN3Q4QgJD9cJmONIYpM2FlekDXnf3InuyFGc4dIDsFMiTCZmE-yDEnxDlqpp2CzE-7T2NRwSZF9fd3IVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ می‌گوید اگر از توافق رضایت نداشته باشد و ایران رفتارش را اصلاح نکند، بار دیگر ایران را بمباران خواهد کرد.
رئیس‌جمهور آمریکا که روز چهارشنبه در نشستی خبری همراه با عبدالفتاح السیسی، رئیس‌جمهور مصر، در حاشیه نشست رهبران گروه ۷ در فرانسه صحبت می‌کرد، گفت: «این فقط یک یادداشت تفاهم است. اگر از آن راضی نباشم و رفتارشان را اصلاح نکنند، دوباره به سمت آن‌ها شلیک می‌کنیم و روی سرشان بمب می‌اندازیم.»
دونالد ترامپ همچنین گزارش‌ها دربارهٔ سرمایه‌گذاری ۳۰۰ میلیارد دلاری این کشور در ایران بر اساس تفاهم‌نامه را نادرست خواند، اما گفت که آمریکا مانع سرمایه‌گذاری دیگر کشورها در ایران نخواهد شد.
متن تفاهم‌نامه هنوز  منتشر نشده، اما بر اساس یکی از بندهای متنی که برخی رسانه‌های آمریکایی منتشر کرده‌اند، چنین ذکر شده که «ایالات متحده متعهد می‌شود همراه با شرکای منطقه‌ای خود، طرحی جامع و مورد توافق دو طرف برای بازسازی و توسعه اقتصادی جمهوری اسلامی تدوین کند و تأمین مالی دست‌کم ۳۰۰ میلیارد دلار را تضمین نماید. سازوکار اجرای این طرح، به عنوان بخشی از توافق نهایی، ظرف ۶۰ روز تدوین خواهد شد».
رئیس‌جمهور آمریکا همچنین گفت در متن تفاهم‌نامه گفته نشده است که آمریکا پولی به ایران پرداخت می‌کند و وجود بندی دربارهٔ رفع فوری تحریم‌های ایران در متن تفاهم‌نامه را نیز رد کرد.
در متن منتشرشده در رسانه‌های آمریکایی، که صحت آن هنوز مورد تأیید قرار نگرفته، آمده است که «ایالات متحده متعهد می‌شود بر اساس جدول زمانی مورد توافق در توافق نهایی، همهٔ انواع تحریم‌های اعمال‌شده علیه جمهوری اسلامی ایران را لغو کند؛ از جمله قطعنامه‌های شورای امنیت سازمان ملل و شورای حکام آژانس بین‌المللی انرژی اتمی و همچنین تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76445" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YuU8nkjjJO-btuwtn8o5YLaLRQkK8y6npXfYNKrFFumZ3sEufGY8T1P_j-lREXerBs8KTfpf7cb4nxzSiNHo4-f4N6lmzFvk7-qtYr1Wbin_VD0_Fraqc80Sf2Ahk_nnSKmmoSI87JSAvbDaEeb-PzEx9pn7WRKOxM57k24CvBT2051hJ7HjjMXLbplQIPpfHu_39zL8P9I_dpXpfu0mhok-ba92zQj0A0BlIEt6bMYhHF66n33LH_00wm_recQjYcEFw5_6utkWHhT7VURvUGfuhjy87PMn0tiQf9Q8dZsic5e7crxelRL-WKjhCdXlfnxqwDttb6EA9UeSVr6b4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس جمهوری اسلامی، با انتقاد از یادداشت تفاهم میان جمهوری اسلامی و آمریکا، این توافق را «نامتوازن» توصیف کرد و گفت همه خطوط قرمز جمهوری اسلامی در آن رعایت نشد.
رضایی در یک گفت‌وگوی تلویزیونی افزود جنگ پایان نیافته و نباید تصور کرد شرایط از وضعیت تقابل خارج شده است. او گفت: «ما در یک جنگ ترکیبی تمام‌عیار هستیم و باید از فرصت ایجادشده برای قوی‌تر شدن استفاده کنیم.»
سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی همچنین از منتقدان یادداشت تفاهم دفاع کرد و گفت نباید مخالفان تفاهم را «تندرو» خواند. او افزود: «اگر این افراد نبودند، الان سربازان آمریکایی بالای سر ما بودند.»
رضایی پیش‌تر نیز در شبکه اجتماعی ایکس نسبت به نحوه دفاع حامیان توافق از این تفاهم‌نامه انتقاد کرد. او از مقام‌های جمهوری اسلامی خواست از منابع عمومی برای تبلیغ «توافق» استفاده نکنند، منتقدان را تحمل کنند و برای توجیه تصمیم‌گیری‌ها از رهبر جمهوری اسلامی هزینه نکنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76444" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtO6o0VmmGsV_ZfzhDPQz3mF0M35uLeZcb3vB5Y1h5pCikw5-vNBhhiBF9cooZNxlgXmjTBTz-S-Yhc9533WyFgUMoAEF5-KViHH8dfOlWwWYpV6SLnAi_GCJOTfHw0g0Z1EOp6S4h70r8Hl6eg29RMoNhyt4FXEk8mevIhMhkq4WfLBLopFX0O4Z103gZbqHtLUrMKGGy8XLimJt5kRdzfQzxj9XcTbYSGAi3_rj0q8WWZ6zLHQtdxi2bGBsGNi9UcvYcTfVquyWL4GKnDc-kjJI5kYEvpo1oynJbYDAEjE9ViZJyHwWRFRgVF0ilYEs2OQka2NwjxoHo4oyS449g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامهٔ روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسید و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شد.
قیمت دلار آمریکا که در مقطعی تا ۱۹۰ هزار تومان بالا رفته بود، تا کنون حدود ۲۰ درصد کاهش پیدا کرده است.
قیمت هر گرم طلای ۱۸ عیار نیز روز چهارشنبه به ۱۵ میلیون و ۷۶۷ هزار تومان و «سکه امامی» نیز به ۱۵۹ میلیون و ۵۰۰ هزار تومان کاهش یافت.
در مقابل، شاخص بازار سهام بورس تهران از زمان اعلام توافق رشد چشمگیری داشته و روز چهارشنبه با ثبت رکوردی تازه به بیش از ۵ میلیون و ۱۰۰ هزار واحد رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/76443" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xph7dPXFhbOQpT4RoYcUpa5i3wFel-k0FAfckISCMjFW80Mz7yHVeI7-cBmSB_S3hQRx5Wj3zGMH6WMcZwmBe08rjxCXk1rCVP7GDAZlHnpV2Y2xCIjqHuDzaEJxgWfjxli31rq-R8E02Ho_8F1orG-onwfFcaN1YBhyGo6Qu-yCYtUoZNyLNq9Sbbbt_VhPf5sqHGyzK7rsWBnAsiYVflhtK68kMFDVv3LFMzCmr-8zdoouQAFVTs8qx_YXF45qAEClTuDey93-M4S4U7go7K1DKURzXoeEuqvkcxtKrPBb-KyFbMVGFRcsF52Yw4DesymROXUwU3GF21WiQQdaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سران هفت کشور صنعتی جهان (G7) در بیانیه پایانی نشست خود از توافق میان ایالات متحده و جمهوری اسلامی حمایت کردند و آن را فرصتی مهم برای جلوگیری از دستیابی حکومت ایران به سلاح هسته‌ای و محدود کردن فعالیت‌های موشکی و منطقه‌ای تهران دانستند.
رهبران آمریکا، کانادا، فرانسه، آلمان، ایتالیا، ژاپن و بریتانیا همچنین اعلام کردند آماده‌اند در روند اجرای این توافق مشارکت داشته باشند.
در بخش دیگری از این بیانیه، بر ضرورت حفظ آزادی کشتیرانی و عبور بدون مانع کشتی‌ها در آبراه‌های بین‌المللی تاکید شده و این موضوع یکی از ارکان اصلی تجارت جهانی توصیف شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76442" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hYi52d0Ea7LSSGrE5VbzRqngjFtZRDZXIA7dJMMI1Jj7f9C9mAkgqvGprNksHdSJyi6aMUxW3V1lLZLz0jWkAQ940KZm8YUafDT-T1Us5B9DtRWYtDCvMKn9ltD5xc0s-3UFpdqrAvVvsDgny_L2RT7MaugR36wlDHHPoPJJilU38eEhI0PnwEd8vlDzi_3cO0bVvA0cO2DsAaqh-9n4qtqi6wt4I_H5h9HHJnA-rxih0yUNlaU45c3jwdwlH1NLviAi23NgNRqXf5QmpknEiHU8Werq5fAwE43VzRMYoK-lH4zKDbtf2j_C-JUky5l-d6WKObLALlHR09YVTNqiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مهری فرج‌زاده» ۳۶ ساله، ساکن کرج و مادر دو فرزند، روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در فردیس کرج هدف شلیک گلوله قرار گرفته و جان خود را از دست داده است.
به گفته منابع مطلع، گلوله به ناحیه جمجمه او اصابت کرده بود و مهری فرج‌زاده پیش از رسیدن به بیمارستان «به‌آفرین» فردیس جان باخته بود.
نزدیکان او می‌گویند پس از دو روز پیگیری، پیکر مهری فرج‌زاده را روز ۲۱ دی‌ماه از بهشت سکینه کرج تحویل گرفتند.
مهری فرج‌زاده خانه‌دار بود و دو فرزند داشت. دختری ۱۵ ساله و پسری ۱۰ ساله که با کشته شدن مادرشان با فقدانی جبران‌ناپذیر روبه‌رو شدند.
@
VahidHeadline
آپدیت:
پیام دریافتی: پسرعمه‌ی مهری، اکبر حسن‌پور هم ۱۹ دی تو گوهردشت کرج با گلوله کشته شد. اکبر دو دختر ۱۶ و ۱۸ ساله داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76441" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaBoROL6S7rkiVXn11jcQspr8KH2O9Rfd_mmwtyIPs_a1O-7XbEpdQs5sw1eA2ZC3OWK0CjEnEMJdr_vYgx3LmAMLXiZLh8Sujb84cV3N3ie_ZJbEOM-RAoXe4GirawUGJTrkstYy1EjpNTVelV298i1u3rQXbf4IzextR02nHjTjkL6jqz1ZInGH8S_ZqiiNwQJZ8p2d-ov5anO1tnbWUbRHTaSNjIhqHuQnPhPYSycte528PyD8Zdb_sRLQKjSh3PIU8zEHkmdemuOI8JG_S51pNUsPzTbtr9sTGalCirbd5GVJ4vIErPtlPHo6ayY1cc8s_h8zq29VH08XTbPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند از اول ژانویه ۲۰۲۶ تاکنون، ۷۴۶ مورد اعدام را در ایران مستند کرده است که تنها ۵۲ مورد آن از آغاز ژوئن ۲۰۲۶ به اجرا درآمده است.
‏
🔸
جمهوری اسلامی در سایه جنگ و در واکنش به اعتراضات سراسری دی ماه ۱۴۰۴ به اجرای اعدام‌های سیاسی شتاب بخشیده است. از ابتدای سال جاری میلادی تاکنون، دست‌کم ۴۵ معترض و زندانی سیاسی متهم به جرایم علیه امنیت ملی، از جمله جاسوسی، اعدام شده‌اند.
‏
🔸
گزارش‌های رسیده به بنیاد عبدالرحمن برومند نشان می‌دهد که مبنای حقوقی اصلی بسیاری از این احکام اعدام، «اعترافات» اجباری اخذ شده از زندانیان تحت فشارهای جسمی و روحی بوده است؛ امری که نقض آشکار حقوق اولیه دادرسی عادلانه و مصونیت‌های بین‌المللی در برابر شکنجه به شمار می‌رود.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76440" target="_blank">📅 15:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76439">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/649b79d41e.mp4?token=oi69P_VNry1YlCDkPnFjZ9s3Wr8pbJ213XHhAaXDsjf5R7LeP6T1Ad5R_PBAE3PowGPvxcMa01eaUZSXCajEL5lmK--kWzrybzBN-FgBGkJ-WO7-k5gNU6HGQVXkRO_R2c2-1Dj9iwcw2RxZn0wFsMkscJWUVKrcAT0T4WsZeBAFoY9Xt13PWxdD7pF-dTfDvuOcTzHDf0IGJfwu1MX0_DC04gq0bkHzOe8lEI-g2MMj6jBr2icdmuqM2X44Cp5TIBlgpI-Lt1ieo6DY4O2rOpNqnWEu6BNZUSoPAUmBwez6Vgkf8ky69iCyLSyRY891CC0FlWwlFfRxV7-ggcb8wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/649b79d41e.mp4?token=oi69P_VNry1YlCDkPnFjZ9s3Wr8pbJ213XHhAaXDsjf5R7LeP6T1Ad5R_PBAE3PowGPvxcMa01eaUZSXCajEL5lmK--kWzrybzBN-FgBGkJ-WO7-k5gNU6HGQVXkRO_R2c2-1Dj9iwcw2RxZn0wFsMkscJWUVKrcAT0T4WsZeBAFoY9Xt13PWxdD7pF-dTfDvuOcTzHDf0IGJfwu1MX0_DC04gq0bkHzOe8lEI-g2MMj6jBr2icdmuqM2X44Cp5TIBlgpI-Lt1ieo6DY4O2rOpNqnWEu6BNZUSoPAUmBwez6Vgkf8ky69iCyLSyRY891CC0FlWwlFfRxV7-ggcb8wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک جت خصوصی تو یک اتوبان در تگزاس سقوط کرده، راننده‌ها رفتن کمک سرنشینها
J74wabx
یک نفر کشته شد؛ پنج نفر به دلیل استنشاق دود در بیمارستان بستری شدند.
AZ_Intel_
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76439" target="_blank">📅 09:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76438">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlEYfyAE-ulKWLvt1rA3Cn3FGvGKTxC867iiOqN2mHTVbl1tyHZT6CDWJlbXYQpx6uXoewxCEJgkzvdcoJsHUgbKLeOVm7YnKeNjL4X_KHv80XrqX4q0E81in6w4PnhBfwTAF3qs2rxMv7L4GGgWdDC2XloWt7LDCDwNPNMVQLXc9nGsy1t7sl4QunxD2GJvj271RJVsLAHdBA4PDoJi_zc8rCH13Lp_M3jKTzrQmc4JaiF1CQx-y3Yi5UDn4ExwMF7eeLB2XM9SYy044QOIoM8mYhXQyEgq2N2a91PLBSfJXNgcx3x_rQue5jknHbZvexUd7R1WFDwTbRY66Qq9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین نفتکش‌های حامل نفت خام ایران از زمان آغاز محاصرۀ دریایی آمریکا، از تنگۀ هرمز خارج شدند. این موضوع را صبح چهارشنبه یکی از وب‌سایت‌های ردیابی کشتی‌ها اعلام کرد.
وبسایت «تنکر ترکِرز» (Tanker Trackers) که ذخیره و حمل‌ونقل محموله‌های نفتی را دنبال می‌کند، بر اساس داده‌های دیجیتال منطبق با تصاویر ماهواره‌ای، «اولین صادرات نفت خام ایران در دو ماه اخیر» را تأیید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76438" target="_blank">📅 08:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76437">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyKCORytaSW90W6RmWSDDB1x6mzLqHTp5MiIKsg78hxwsF7UgmF8D_HI5qr7Z76vFwbEw-2e1omHOgRnxngbpnOXksduaQhp07DsKqfM-odw7Fck3HdKtGCQjq85R9RohKOFim-3VpuCMQEhfOzeYPkxCsIZ_VkOTGGrgo44RwMgAkcSswqdZeETIDPSNB8mM57tjBHzpaKS46SBNpXHMV44bXRKa9nlRPvvfj05UbsXbYjndoPKfQ9OxNFqWlHV_ABBodO3Cp3JxoGPTLgC7ZPX9VCVspORc4xhOKnMldhgPvdEtm2Kv4lf9Zw8ah5TrzdjgXhaB6jU9NdSOgft_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ان‌بی‌سی، حکومت ایران پس از اعلام یادداشت تفاهم با آمریکا، همچنان تعداد «زیادی» پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است.
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی گزارش داده که سپاه پاسداران پهپادهایی پرتاب کرده که آمریکا توانسته آنها را پیش از آنکه تهدیدی برای شناورهای تجاری، کشتی‌های نظامی و خدمه حاضر در منطقه ایجاد کنند، رهگیری کند.
بر اساس این گزارش، سپاه پاسداران از زمان امضای «الکترونیکی» یادداشت تفاهم در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76437" target="_blank">📅 05:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76436">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/75a49fba40.mp4?token=FKyi5orJDIBfd7TssvzAK4183MDPKlKmsF2JZTcuRZuZ3jLr6u01C9FqA35a6oWmhHzVODr34jdYHfH9MZJ52caXP9-nfNhWNDn9-bfm5adU_dchinumXxpovTGtrhYqibOyZh27bJpeuf-NHF4UfhQ143CQtt8TxOMhKrW0qMfCm4crWVN0Jz9dKGpH9e-ibcT8Vd9Fd2Dp-a7reC433uGjLX4NkrwsA375_QGlJyZGBWreDvanOWj--GOWDiIe6NfBlUqAOYBSuMtbOg-Gh9Q4xVRdSzUCoGm-OjuEv3hGY1vCpC34Kq8NNugt5CUYVQyjV_Ysl2NVuZm3yIsQxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/75a49fba40.mp4?token=FKyi5orJDIBfd7TssvzAK4183MDPKlKmsF2JZTcuRZuZ3jLr6u01C9FqA35a6oWmhHzVODr34jdYHfH9MZJ52caXP9-nfNhWNDn9-bfm5adU_dchinumXxpovTGtrhYqibOyZh27bJpeuf-NHF4UfhQ143CQtt8TxOMhKrW0qMfCm4crWVN0Jz9dKGpH9e-ibcT8Vd9Fd2Dp-a7reC433uGjLX4NkrwsA375_QGlJyZGBWreDvanOWj--GOWDiIe6NfBlUqAOYBSuMtbOg-Gh9Q4xVRdSzUCoGm-OjuEv3hGY1vCpC34Kq8NNugt5CUYVQyjV_Ysl2NVuZm3yIsQxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون دونالد ترامپ که روز جمعه در سوئیس تفاهم‌نامه پایان جنگ با ایران را امضاء خواهد کرد، گفته مفاد این توافق اولیه در یک جمله چنین خلاصه می‌شود که اگر ایران به تعهدات خود در چارچوب این توافق عمل کند ایالات متحده آماده فراهم کردن زمینه برای بازگشت این کشور به صحنه اقتصاد جهانی است.
آقای ونس روز سه‌شنبه در گفت‌و‌گو شبکه رادیویی سیروس ایکس‌ام گفت: «دونالد ترامپ هرگز نگفت که هدف اقدامات او به قدرت رساندن رضا پهلوی در ایران است. آنچه گفت این بود که اگر مردم ایران بپا خواسته‌اند و مقابل حکومت خود ایستاده‌اند، خیلی هم خوب است اما آنچه او می‌خواهد اطمینان یافتن از فعالیت‌های هسته‌ای ایران است چه از طریق دیپلماتیک و چه از طریق جنگ که خب در نهایت راه دوم روی داد». 06:21
معاون رئیس جمهور آمریکا همچنین تصریح کرد که خواسته منتقدان آقای ترامپ مبنی بر ادامه جنگ با ایران با آن چه دونالد ترامپ به مردم آمریکا همیشه وعده داده و قصد اجرای آن را دارد، «همسو نبوده و نیست.»
آقای ونس در این مصاحبه چند بار تاکید کرد که آنچه به لحاظ اقتصادی ایران از آن منتفع خواهد شد «به هیچ وجه» از منابع و دارایی‌های آمریکا پرداخت نخواهد شد بلکه در صورت همکاری ایران و اجرای همه مفاد توافق، آمریکا با رفع تحریم‌ها به سرمایه‌گذاری در ایران «فرصت» خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76436" target="_blank">📅 03:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76435">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H511PX_2XgymtWMd_3vrhc_RqKapBPt70PTXMHxaHiFWxKC37YYu0RaihNk-aWJq1EAIwDn9r0fRl-NU9TF7KMqCuc6peBlqXqxu7B74TVg04IxQJ1SOYUSUugUyoRONjZL_mtbTZdZCOc65KB_BJ3RxxVm-mM7ZLys7bEDw-ymuywWwsmEGfiDlTAeY4JRnYsb3R_KFDbPCrgv791D99qAMZ8tBEedDHyT6Z2BL8YeCi26Y4tyMnBYbS6tDjSJoaheUsRZT9c7hkTMBCyOxRNz7bVhBxEX6KMryoFJGFSTZ0FQMaGFD1tFF58k94An6eZR36mCnbeNAz5WgdmN4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری که در شبکه‌های اجتماعی
منتشر
شد، دارا خسروشاهی، مدیرعامل ایرانی‌-آمریکایی شرکت اوبر، را در استادیوم سوفای لس‌آنجلس و در جریان دیدار تیم‌های ایران و نیوزیلند در جام جهانی ۲۰۲۶ نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76435" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76431">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RMigyvEdE36DXVQ6JsdbzExOybd5KRwMBY87QDRbKVpO7HpmMAJZXpUZJXVbHVwB_4hK5gf432E_QGG1oJZ3tzeSLOMgCtsANxWX3iVgDVm_Kv3j_bMBMpUFU3Wg7-xIBuGVQGPgHrpvaL5nxlAIObcw_g19cRkFx-AVxDu1SYEss-kzPbrSyQCNW7iUT1dOyKmZwR1bqLGrFNFhsisyPkpV5FRtPMxB1giqoWEu6fIc5Og63UlRg6v8rNXvmSC-eMdqA9-KcPLcHLU-HTlSmh8e49K40ai8F2s_OzaSHOUiofcl8yG6H8B6Z3sx-4ZlvRKv89hb5EnVBPPYUOtEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aO-W0eJyicR68QONn1VvSyTmiNiWGiFSdnMtAwAOaVrlBlvlz-dX0JW0x2S_P-8A49cnFQkDH8Dtm1UqcG4_hDGVuwV_lCu2MXGvaxYcu2Yb2VMbxatnPtGfHIFpRgpSebuVMZnH4M3TANZW-3IRuqUoVfR_GFSBuSyjkiCiGD6PtluFxNB80qyQlpP-NSWQl5NwRXzjFz0_UeqjaCU4aX78mR5zqN3r6aKd8VXRhV7rlio1qVon1jTJql57IyefuExc9YOorB_Hf6OGE1h6B5S0GLIS1gRIwCDp6WYybNA7vzDu1eN22-nAsDDSCjaCJUTDZTcpPVvZn4nyamJheA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SvcNALgApNvmd2CR-d0iyt8oBcweTIDjp8MGY95rCysqmkhqZUa8S2AqC-7K1mSMTHtUx0IAq_06b1cbwStsD38D8DGH32OGqVQLy5RwWoYzjcUqBu9mcP80W1aYn_8CJvLd7TyoqvAfVYaoZef-jjJpsaS09wKrsM4ITO4ybybummztrZJFzD3V5_DCUR1n1pLKc_mkkyK89cGkpiGr4xBmiwuOt315JxqVDQ2X9rQuvUn8vpFL9nT0mV3KWeh-nkcYlKOIVKyc9KHowRUeXrugpPKZ-_BthX8_AeVaBSgLdtVFm4QoqBEzFF6bUwnOSxY0Nv4iDD3ysEey7_Upsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/57a8c06d44.mp4?token=h_LOeRCFDo7gDltysczjc8k-vfv8HU43zj1N0CI0n1R7YUU2lhz1gLNqqkTHusfOORwHfUSTvJOx0Z1ttKi9A9tjUjkHqMI5dwjgLHa8CqdsnId7o9ucOYY0WZCbz2rZ6kkMaUMxMgaJyKY4Nl6XFYKVASKBzPyX5FLpENalahNYk0r4V1i-7yLbyOjQ-w4LFuPYoERF80861FcZ4SzWySzPJO7hspBvTndMeQQYPilgjDc-wyTqGzjaTJamKJQkMFgjekAhYNrBHjPoq-80AE_UIwZ0N1-H2frRbKSi7i1bRMfF04EzS9yfcBhk7t6rD2IvZc2Jkzlyc9lkMx68vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/57a8c06d44.mp4?token=h_LOeRCFDo7gDltysczjc8k-vfv8HU43zj1N0CI0n1R7YUU2lhz1gLNqqkTHusfOORwHfUSTvJOx0Z1ttKi9A9tjUjkHqMI5dwjgLHa8CqdsnId7o9ucOYY0WZCbz2rZ6kkMaUMxMgaJyKY4Nl6XFYKVASKBzPyX5FLpENalahNYk0r4V1i-7yLbyOjQ-w4LFuPYoERF80861FcZ4SzWySzPJO7hspBvTndMeQQYPilgjDc-wyTqGzjaTJamKJQkMFgjekAhYNrBHjPoq-80AE_UIwZ0N1-H2frRbKSi7i1bRMfF04EzS9yfcBhk7t6rD2IvZc2Jkzlyc9lkMx68vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکان جلسه امضای تفاهم‌نامه
ترجمه ماشین:
توافق چارچوبی میان آمریکا و ایران قرار است روز جمعه، ۱۹ ژوئن، در بورگن‌اشتوک امضا شود؛ نه آن‌طور که ابتدا تصور می‌شد، در ژنو.
این موضوع را وزارت امور خارجه فدرال سوئیس، در پاسخ به شبکه SRF تأیید کرده است.
وزارت خارجه سوئیس توضیح داد: «این مکان، یعنی بورگن‌اشتوک، از سوی میانجی‌ها، پاکستان و قطر، و همچنین آمریکا و ایران پیشنهاد شده است.»
به گفته این وزارتخانه، سوئیس زمینه گفت‌وگوها را فراهم می‌کند و شرایط دیپلماتیک لازم را ایجاد می‌کند تا این دیدار بتواند در سوئیس برگزار شود.
وزارت خارجه سوئیس درباره روند برگزاری و جزئیات امضای برنامه‌ریزی‌شده، اطلاعاتی ارائه نکرد.
srfnews
چت‌جی‌پی‌‌تی:
«بورگن‌اشتوک» به‌عنوان منطقه/کوه در سوئیس است، ولی مجموعه هتل‌ها و ریزورت بورگن‌اشتوک با قطر پیوند مستقیم دارد. Bürgenstock Resort Lake Lucerne بخشی از مجموعه هتل‌های لوکس سوئیس است که مالک آن شرکت/گروه هتل‌داری  Katara Hospitality مستقر در قطر است.
رستوران «Parisa – Persian Cuisine» در بورگن‌اشتوک نیز نخستین‌بار در سال ۲۰۱۲ در دوحه افتتاح شد و بعداً شعبه‌هایی در سوئیس، مراکش و نقاط دیگر پیدا کرد.
در ژوئن ۲۰۲۴ نیز بورگن‌اشتوک میزبان نشست صلح اوکراین با حضور ۹۲ کشور و ۸ سازمان بین‌المللی بود. در آن نشست هیأت‌هایی از اوکراین، آمریکا، فرانسه، آلمان و کانادا شرکت کردند، اما روسیه حضور نداشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76431" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76430">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QfA3J8rdgFntZmzQcJVyVFw4-TRCnImn_Csj7uAwi7LR7x8auuRZvcNTc84PwHjeOFAfzi_0NtKixIrLjx00K1usAsznE9ezZvJ0Qj9cnJ5YJzwvFf59Q0U6jKBS3CHnWHGtXF7qiMOhhZ0bCF6qj0GpaH3dynu-NkaY9OQ1kdifwlwUy9cqc_VOGFPuwFbYEfQ_-oQvx88efuaiuyGQTFS_C5wMOzgiHhJx6RGbXQTKNKtXHLbnVShZ_lqHYpsZ9vKUEvfPvZ44YSVDw4LYfkXHoOEnL1Nq5X7s9RmOVs93b7Cbf9NMijDE89HB0dQ-3-IGBYOX21BDylmmZHRrqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختصاصی رویترز: منبع آگاه می‌گوید توافق ایران شامل یک صندوق ۳۰۰ میلیارد دلاری است که بیش از نیمی از آن تاکنون تعهد شده است.
ترجمه ماشین:
دبی، ۱۶ ژوئن، رویترز — یک منبع آگاه مستقیم از جزئیات توافق به رویترز گفت در توافق چارچوبی آمریکا و ایران، یک صندوق خصوصی ۳۰۰ میلیارد دلاری برای تحریک سرمایه‌گذاری در ایران پیش‌بینی شده و بیش از نیمی از این مبلغ نیز هم‌اکنون تعهد شده است.
این منبع که به دلیل اعلام‌نشدن رسمی این طرح، در حالی که واشنگتن و تهران آماده امضا در روز جمعه می‌شوند، به شرط ناشناس‌ماندن سخن می‌گفت، گفت هدف این صندوق آن است که برای هر دو طرف انگیزه اقتصادی ایجاد کند تا به یک توافق نهایی برسند.
مقام‌های آمریکایی و ایرانی روز یکشنبه گفتند که بر سر چارچوبی برای پایان‌دادن به جنگ خود به توافق رسیده‌اند؛ جنگی که از ۲۸ فوریه، زمانی که نیروهای آمریکا و اسرائیل به ایران حمله کردند، آغاز شد. این چارچوب همچنین شامل توقف محاصره ایران از سوی آمریکا و بازگشایی تنگه هرمز، مسیر کلیدی تأمین نفت و گاز جهان، است.
این منبع گفت صندوق جدید، یک ابزار سرمایه‌گذاری خصوصی است، نه برنامه‌ای برای بازسازی یا پرداخت غرامت، و هیچ پول یا کمک بلاعوض دولتی در آن وجود نخواهد داشت. او افزود شرکت‌هایی مستقر در آمریکا، کشورهای عربی خلیج فارس، آسیا، آمریکای جنوبی و آفریقا با تأمین مالی آن موافقت کرده‌اند.
به گفته این منبع، سرمایه‌گذاری‌های تعهدشده حوزه‌هایی از جمله انرژی، لجستیک، تولید صنعتی و حمل‌ونقل را در بر می‌گیرد.
یک منبع ارشد ایرانی به رویترز گفت تهران در ابتدا خواستار ۴۰۰ میلیارد دلار غرامت بابت خسارت‌های جنگی از آمریکا شده بود، اما واشنگتن گفته بود چنین مبلغی را پرداخت نخواهد کرد.
پس از آن، ایده این صندوق که قرار است «صندوق بازسازی و توسعه» نامیده شود، مطرح شد.
منبع ایرانی گفت سازوکار پیش‌بینی‌شده شامل مشارکت کشورهای منطقه به شیوه‌های مختلف است. این شیوه‌ها شامل تضمین وام‌ها، ایجاد خطوط اعتباری یا تأمین مالی مستقیم بازسازی مکان‌های آسیب‌دیده در جنگ، از جمله تأسیساتی مانند مجتمع فولاد مبارکه، پالایشگاه‌ها، فرودگاه‌ها و به‌طور گسترده‌تر زیرساخت‌های آسیب‌دیده از درگیری، می‌شود.
ایران، به‌عنوان یکی از بزرگ‌ترین اقتصادهای خاورمیانه، در چهار دهه گذشته تقریباً هیچ سرمایه‌گذاری مستقیم خارجی قابل توجهی جذب نکرده و به دلیل موج‌های پیاپی تحریم‌های آمریکا و تحریم‌های بین‌المللی، از بازارهای جهانی سرمایه کنار گذاشته شده است.
این کشور دومین ذخایر اثبات‌شده بزرگ گاز طبیعی جهان و چهارمین ذخایر اثبات‌شده بزرگ نفت جهان را در اختیار دارد.
ایران همچنین جمعیتی جوان و تحصیل‌کرده با بیش از ۹۲ میلیون نفر، پایه صنعتی متنوع و ظرفیت‌های بکر قابل توجهی در بخش‌هایی از پتروشیمی و معدن گرفته تا گردشگری و کشاورزی دارد.
این منبع گفت صندوق سرمایه‌گذاری کاملاً جدا از مسیر موازی مذاکرات درباره رفع تحریم‌های آمریکا و آزادسازی دارایی‌های حاکمیتی ایران است که در خارج از کشور مسدود شده‌اند. او این دو را سازوکارهای مالی متمایز با اهداف و جدول زمانی متفاوت توصیف کرد.
این صندوق تا زمانی که یک توافق نهایی و رضایت‌بخش حاصل نشود، ایجاد نخواهد شد و عملیاتی هم نخواهد شد. تفاهم‌نامه، پس از امضا، قرار است روند را طی ۶۰ روز آینده ساختاربندی کند.
این منبع گفت: «این صندوق فقط زمانی ایجاد می‌شود که توافق نهایی امضا شده باشد. در طول این ۶۰ روز، مدیران صندوق با ایرانی‌ها و سرمایه‌گذاران کار خواهند کرد تا پروژه‌ها را برنامه‌ریزی و محدوده آنها را مشخص کنند.»
وزارت خارجه ایران و وزارت خارجه پاکستان، که به میانجی‌گری در توافق مربوط به صندوق سرمایه‌گذاری کمک کرده بود، بلافاصله به درخواست‌ها برای اظهار نظر پاسخ ندادند.
یک سخنگوی کاخ سفید به مصاحبه روز دوشنبه جی‌دی ونس، معاون رئیس‌جمهور، با شبکه سی‌بی‌اس اشاره کرد که در آن گفته بود ایران در صورت پایبندی به توافق با واشنگتن، از جمله برچیدن برنامه هسته‌ای خود، حذف ذخایر مواد غنی‌شده و پذیرش یک رژیم سخت‌گیرانه بازرسی و اجرای تعهدات، می‌تواند به یک صندوق بازسازی ۳۰۰ میلیارد دلاری با حمایت کشورهای خلیج فارس دسترسی پیدا کند.
این منبع نگفت که صندوق چگونه یا توسط چه کسی اداره خواهد شد و یادآور شد که جزئیات کلیدی هنوز باید نهایی شود.
این منبع از شرکت‌هایی از کره جنوبی، ژاپن، سنگاپور، مالزی و آمریکا به‌عنوان شرکت‌هایی نام برد که تعهداتی داده‌اند، اما از ارائه فهرست کامل خودداری کرد.
تفاهم‌نامه ۶۰ روزه یک چارچوب است، نه توافق نهایی، و انتظار می‌رود مذاکره‌کنندگان آمریکایی و ایرانی در این دوره روی مسیرهای متعددی کار کنند که مسائل هسته‌ای، تحریم‌ها و امنیت منطقه‌ای را در بر می‌گیرد.
reuters
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76430" target="_blank">📅 22:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76429">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oZj-3GqL6tHaRV2QAYqTLbkPcmx2fwSxpElylbHGIIEFckJlbHSjfE5sXSpoAyMZZaZY4m1GRMEbtOUss8Fgv_xrbw6rEHvtu77-7MQZDuThGvBRNlxH4rjQAHfde5aZJtR7KSPmaENsuxG9QM_HGPMdnLoCihPxwXH59c77cVnTu7iwx4iKsbjyDdcmfxndq6LdfWHMz7HP-80-j5_mM8UirAS1RpGtEQaXZ5i9isASIzar7d9_m-wsFc8ZUg1io1BdSMpuDxYDmzw4ExF0iYMu8ZerUQ-843wL9OIRQVwZWBnw_UqHh9rUUjSDoDeh_J4J36IcQ-sYs1z4pH2eTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی حملات روز سه‌شنبه ارتش اسرائیل به جنوب لبنان که چهار کشته به جا گذاشت، قرارگاه مرکزی خاتم‌الانبیا تهدید به پاسخ کرد. این حملات بعد از اعلام توافق ایران و آمریکا انجام شد.
قرارگاه خاتم‌الانبیا که وظیفه هماهنگی میان نیروهای مسلح جمهوری اسلامی را برعهده دارد، در بیانیه‌ای اعلام کرد که اگر اسرائیل به حملات خود در جنوب لبنان پایان ندهد، باید منتظر «پاسخ سخت» نیروهای مسلح جمهوری اسلامی باشد.
در این بیانیه ادعا شده که در پی اعلام نهایی شدن تفاهم پایان جنگ توسط دونالد ترامپ، ارتش اسرائیل «۸۴ بار» آتش‌بس در جنوب لبنان را «نقض کرده است».
لبنان ساعتی پیش اعلام کرد که حملات اسرائیل در جنوب این کشور چهار کشته بر جای گذاشته است؛ این در حالی است که اسرائیل گفت چند راکت شلیک‌شده از سوی حزب‌الله را رهگیری کرده و حملاتی را نیز انجام داده است.
خبرگزاری رسمی لبنان گزارش داد که پهپادهای اسرائیلی دو خودرو را در شهر میفدون و یک خودروی دیگر را در شهرک نزدیک شقین، هر دو در منطقه نبطیه، هدف قرار دادند که «بر اساس آمار اولیه به کشته شدن چهار نفر» و زخمی شدن تعدادی دیگر منجر شد.
ارتش اسرائیل اعلام کرد که پس از آنکه «یک خودروی مشکوک» را در منطقه‌ای که نیروهایش در آن فعالیت می‌کردند شناسایی کرد، حمله‌ای را در جنوب لبنان انجام داد، اما محل دقیق این عملیات را مشخص نکرد.
ارتش همچنین گفت که نیروهایش چندین راکت شلیک‌شده به سمت نظامیان اسرائیلی در جنوب لبنان را رهگیری کرده‌اند و در پی آن، نیروی هوایی اسرائیل سکوی پرتاب این راکت‌ها را «هدف قرار داده و منهدم کرده است.»
@
VahidHeadline
📡
@VahidOnlinene</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76429" target="_blank">📅 22:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brnsGXHlxwllv8nsfdjszn7lk6Ju_pi2wYD9ZTaQmYJzrTfzAEa085CdpXS4sqi9zudEUALi0c3tPoj36BAkKZFnAaN5HVSk3uWixTg1jXz2-qC8epfRIkLSaThLvuMAAZeC2T8aFI4k78NysOKWtkx7iUUroYevIfYe_KQwJUcDt8SLNc361j-q6O7YYjrQG0vocOSw6RBG9oh9dwhIHn0PHZUPSk_JqOToVTgltelE2RATk2mkwjLM3tT6JQiT-iGS_uTPXqLOU13vSTdEz2QQqYol3yDMANZoIWnua4QU06oqqOJq-27tzteBNT2bw6cjVTsk5xVyuYPlcGCqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طیبه نظری مکی آبادی، مادر دادخواه مریم آروین و از بازداشت‌شدگان مراسم هفتم خسرو علیکردی در مشهد، از سوی دادگاه انقلاب این شهر به پنج سال زندان محکوم شد.
بر اساس حکمی که در تاریخ ۲۳ خرداد از سوی شعبه اول دادگاه انقلاب مشهد به ریاست قاضی غلامرضا اکبری مقدم صادر و به این شهروند ابلاغ شده، او بابت اتهام «اجتماع و تبانی علیه امنیت کشور» به چهار سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم شده است.
طیبه نظری، مادر وکیل جوان، مریم آروین است که در جریان اعتراضات «زن، زندگی، آزادی» در سال ۱۴۰۱ در سیرجان به دلیل دفاع حقوقی از بازداشت‌شدگان دستگیر و مدتی پس از آزادی موقت، به طرز مشکوکی جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76428" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76427">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpbQH_nooxf46Jh8idiUHK5wiauzsVMNRM7OKhYOKoTjnYrmRZ42S2kkrqCZGu4_JE3VSFuJumnc809yUhO5axGFGEcIR0uHDCNWH9NfBwvfXVX1Jq8eDPvvCHAS3_imBWLStpmSxpbaZp21AHcOW5QwsNeOrPN3rKKvxdrIRKV61eP1flrfrIVpcu1yxHogf5yrXkW2tE9tEo3lK4HSy33WyUzwcaFQVkQ3mT8BICElaTq4fmVAZyKEGHewwSUEyvXXPWBXJJm3m7nyxmcheQRyqwGHe89j2gaujOkpTSknk4Qt_kCE9Cggp_s_ZuWHS8V5jPAWFfBu5wekem38cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت جورنال و خبرگزاری رویترز روز سه‌شنبه به شکل جداگانه و به نقل از منابع آگاه گزارش دادند که یادداشت تفاهمی که ایران و آمریکا به آن دست یافته‌اند، به ایران اجازه خواهد داد «بلافاصله» فروش نفت و دیگر فرآورده‌های نفتی خود را آغاز کند.
منابع این دو رسانه گفته‌اند مفاد مربوط به لغو تحریم‌های فروش نفت ایران پس از امضای توافق در همین هفته اجرایی خواهد شد و خدماتی از جمله بانکداری، حمل‌ونقل و بیمه را که برای تسهیل این فروش‌ها لازم هستند، در بر می‌گیرد.
وال‌استریت جورنال به نقل از این افراد گزارش داد که با اجرایی شدن این یادداشت تفاهم، موانع ناشی از تحریم‌ها بر صادرات نفت ایران و خدمات پشتیبان مرتبط با آن برداشته خواهد شد تا امکان انجام این معاملات فراهم شود.
یک مقام آمریکایی نیز در گفت‌وگو با رویترز تأکید کرد که این توافق دارای شروطی مشخص است.
او که به شرط ناشناس ماندن صحبت می‌کرد، گفت: «این یک توافق مبتنی بر عملکرد است. ایران تنها در صورتی می‌تواند از مزایای این یادداشت تفاهم بهره‌مند شود که به تمامی بندهایی که با آن‌ها موافقت کرده پایبند بماند؛ از جمله نداشتن سلاح هسته‌ای، خنثی‌سازی مواد غنی‌شده خود و عدم مداخله در جریان آزاد کشتیرانی در تنگه هرمز.»
یادداشت تفاهم ایران و آمریکا که ۲۴ خرداد به صورت الکترونیکی امضا شد، قرار است روز ۲۹ خرداد در سوئیس با حضور مقام‌های ارشد دو کشور به شکل حضوری نیز امضا شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76427" target="_blank">📅 20:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/note4BQRn_kY5ZkLWaSLTkeVQFy-Qs7SaWy-btHd-Tt0-WkYrAqOVyozX9djUNFM09_iWlELsN3f39-NBXdpY8el6EkRNYsgGPjaAEa20DayzERydhC6ghBTAmekc3NFLjHiHyT8qGb9f6bWEaIcXmEhoEbz6W-OFN7moaCn5QXGEUdU4Uybc9Nmp20qjQtyvN-voBu5siWao2pVB7dmaHSs7k1rpayLIhc2XBMBUY4vp3qpT_42ZA5Zc44ZI7B-G_n1vwWlbjk0cUDlMOODQiC6QncEINSqZPfdMiuNe1hTJ90FBPIG8-YM1-IKFM0rViDZa2-7VBkwcW1qA_0G1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی
آن گفته ترامپ
:
لیندزی گراهام، سناتور جمهوری‌خواه آمریکا، در شبکه ایکس نوشت گسترش توافق‌های ابراهیم و ایجاد ثبات و رفاه در خاورمیانه یکی از مهم‌ترین اهداف دونالد ترامپ است و این هدف زمانی محقق می‌شود که جمهوری اسلامی تضعیف شود یا رفتار خود را تغییر دهد.
او افزود که امیدوار است مذاکرات پیش رو برای پایان دادن به برنامه هسته‌ای ایران موفق باشد.
لیندزی گراهام اضافه کرد: «جمهوری اسلامی و نیروهای نیابتی آن به‌شدت تضعیف شده‌اند و توانایی آن‌ها برای رقم زدن رخدادی مشابه هفتم اکتبر دیگر وجود ندارد.»
او ادامه داد: «اگر درگیری با جمهوری اسلامی به گسترش توافق‌های ابراهیم، همگرایی منطقه‌ای و صلح پایدار منجر شود، این نتیجه یکی از موفق‌ترین عملیات‌های نظامی در تاریخ آمریکا خواهد بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76426" target="_blank">📅 18:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromﻣﺎﻧﺎ ﻧﻴﺴﺘﺎﻧﻲ Mana Neyestani</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHz9z6wkzNxmk2PgtTgyAdgZQq4P7hskqNnOkh9DLqoNxvuQqb21Cok_WB075WsFMG2fWIjMI_cr-jLURWgYGhfTX11e4rYlUam7JuVUFvboB7imvULwrMkiOXW5bNcJEJPl9d4D2jf1K-ve5ScyJuyQsOWdP9S372ifeY-tvc3xkTLe_Im9QmvGEIMBswBbK5pT4UpLfMU6Q0VU-Ck21zqXgzpMkUjKKZqoOCM3JcK115G5sSikibNhhDQ_Bgt3NNm80yADFt-pzvWD2xA4CKuIGrIXN8ZmnmVwgNex8quN25W41dL4MfpjVjo99k16HZMNMDj4bALbLymJ8chIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObhHkjFckADePXIZGeD35jYzmZ8nlWcF7o_qaktaV1qWxWDvW3-Qrn5WvSyp4iGEQ42B1F2bYX_xz9ygcs8U8v1TgU8OHksL3bSZDL9W-c3SXmsv02tTUi3akQpR_1SuWyYY4_7lKc3LkDiuTuP8t0ZtSEf8eo4JahqPI9yLyBnURzamgjCaMHf_C8zrPNn4Gw3OTHcXvmU4yOzQCkHz2woGkozVkht0o4YxsAkc4ukfjpVEMpYuqRGie7tc1gXenZOB-tfHPZCHKTM-spIo7KDBa3_N1dQHSj-wkBjowxNpXr1isIVx_aWOCx_3D_lSNZVvZxxC8yFoW9Oxireocw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پهلوان سازش ناپذیر
@mananey
مانا نیستانی</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76424" target="_blank">📅 17:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKi4uh-Ecwg3FCcan5TWfKidRMhLOPoC5NPwJ5ZfJtcsp-JE3dMfpWpFK98t6uspnrufi82AV3xT1626ox2JTarIJGPp4R0DABEb_gZ04-sQmEsw0JCCOyV10_w7FPliZyEzGgUxY91KBNPRPca7dzd8WhdfMJsmIsJzqvEqGX9naJqVkImX1vszTxOYrHsGIwTEvc1536jfZJ0-snYWNwJnhvm3EaNZ7Wf7SRzCfNu38VuYL1IBOWycdGuPJ3MiY5LTASqpn0Lnh2_nVzLQlVCFobOWQD2khjBrdsmSjgkL6tjD_NlHtW2bjDE46ZDvSja-45f92FtIb0PC0DWiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnrMrC2EVhhycBenqdsF5D1vNV9VjWZca_pus0G8Hc4gEBtsfQqg1j77_S0F6S3pCvlqo-AA9N20yx0GCW-0gvINzFsaDU6tA_GH3poPqj4bkNGB5ZFTMZOeyzaqG_jPIZex0jhlKtgCEhztn-9_zaw-qpyZHV3HzuumC3mY6kbg9VKTdhmT748NnYUw2Tmk_M3nZ6JjEGcyIlnJbbh7X0hOW-5XEbKpjjYKUjeEXtEz2YlPwk1_E2s7KlF2eVvskO9fMlllQ-2CfsB6-RBlUYkNk-xYqldwSLo-92kZwJOfelvYc4sM2TEOjNvJbZbZ0cYnEnh-TrM7eG_Zuezu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPBq-fLNd5hA45BCQYFNLFP59iflqjyyLRarFNiXNGl3cOQf88uJtyNhUa1wBipO3E3h5PT65PFf7gujiSLQfx1YZx74Z5ebz6MntwDyVUCEmLMvcemsPYoF925VS1UdirD-h3n-0WePkfTC57lJqjrBSp_DShDZLMGvNsyIqW4J41J1_lIG8tbglh7szzh3dfE_y1S_tFNVEGmdiPG0hZT_83bIoNdGTQRrTdU1lA0uGU4YUea2jNdPWtwIEGninH8hLvCAT8ObXU0F1EMGGbTEibcbU9pt1DSV9VL3fl5cnF4IAc1n4KoMWuyqJaWRklzvyvrITe-_iVunpDNZ_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa23faa31.mp4?token=MIbj1FzCVi187XJZ3q0Qfar9cCI21C4ds1ELdVNkDORAN750sw20HGyO2FVR1U4dhlvI86Q3HpmK0l5mNCs7z232VtS6_Ut0XNI3zCbkUI60W1Ym97Drpm4dDPGzzn5OuBvZfd70rOYbSlkpmfdHkOejgQe23Ao2erIaij5YFR9eRzp7vbK2cGa_3JH9LNEtuWGnxGf3XUCrOILkrJ_dF4xxe-dt-1ERCzByCeMR7OJUFdcyk4dBT-pA2GZC7zFjXY0N7CXVvZA51TsuyPC3T054W0zB5STOpri6NkIFcXTkCBRP-NkRhsQaQ32sH72GUVtBZfPZJ_7CCHGPwlZpVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa23faa31.mp4?token=MIbj1FzCVi187XJZ3q0Qfar9cCI21C4ds1ELdVNkDORAN750sw20HGyO2FVR1U4dhlvI86Q3HpmK0l5mNCs7z232VtS6_Ut0XNI3zCbkUI60W1Ym97Drpm4dDPGzzn5OuBvZfd70rOYbSlkpmfdHkOejgQe23Ao2erIaij5YFR9eRzp7vbK2cGa_3JH9LNEtuWGnxGf3XUCrOILkrJ_dF4xxe-dt-1ERCzByCeMR7OJUFdcyk4dBT-pA2GZC7zFjXY0N7CXVvZA51TsuyPC3T054W0zB5STOpri6NkIFcXTkCBRP-NkRhsQaQ32sH72GUVtBZfPZJ_7CCHGPwlZpVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ که پیش‌تر در پیام‌هایی خطاب به ایرانیان از «کمک در راه است» سخن گفته بود، اکنون در گفت‌وگو با مقام‌های قطر، کشته‌شدن معترضان را عمدتا به «گروه‌های قبلی» در جمهوری اسلامی نسبت می‌دهد و میان بخش‌های مختلف رژیم مرزبندی تازه‌ای می‌سازد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76416" target="_blank">📅 17:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76415">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0db862b726.mp4?token=ifrDagW5CHQNn7bw6YYHNFWG30bs5wdxVyWU7qiHbyA8c5dzM1jtRo0-1xWm9A9yaRVnsMwcOPhvRJwukWdrc2vAvzakWOcKUema4qozOCdE6I06j0kXnN_aoypwPFEmHTWqRpJ5-wiMlxv5eTpaLasMwSvSS0iptVfz6jQ1u_9Rmf34ZkPGNDwWBmMZtUXCdHnb4rQ5EPolBbDOzLy9HEafJzpPaUFXs3Q0u2ze5s15m848anfUoMMFP16sCrOrAo5AVjv-RU026W9GPcXVz1sRW1vlVCNlUVg8HuTPBZKnu8JvWx8V7Vf-c34J9DKpnlld97-b6466K2XxQBdHkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0db862b726.mp4?token=ifrDagW5CHQNn7bw6YYHNFWG30bs5wdxVyWU7qiHbyA8c5dzM1jtRo0-1xWm9A9yaRVnsMwcOPhvRJwukWdrc2vAvzakWOcKUema4qozOCdE6I06j0kXnN_aoypwPFEmHTWqRpJ5-wiMlxv5eTpaLasMwSvSS0iptVfz6jQ1u_9Rmf34ZkPGNDwWBmMZtUXCdHnb4rQ5EPolBbDOzLy9HEafJzpPaUFXs3Q0u2ze5s15m848anfUoMMFP16sCrOrAo5AVjv-RU026W9GPcXVz1sRW1vlVCNlUVg8HuTPBZKnu8JvWx8V7Vf-c34J9DKpnlld97-b6466K2XxQBdHkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در حاشیه نشست سران گروه هفت (G7) در اویان فرانسه و در دیدار با امیر قطر، از رویکرد نظامی بنیامین نتانیاهو در قبال لبنان انتقاد کرد.
ترامپ با اشاره به حمله هوایی اسرائیل به بیروت، درست دو ساعت پیش از امضای توافق آتش‌بس با جمهوری اسلامی ایران، آن را «کور و بی‌هدف» خواند و گفت: «به آن‌ها فهماندم که اصلا از این کار راضی نیستم. برای کشتن یک نفر لازم نیست یک آپارتمان را با خاک یکسان کنید؛ آدم‌های زیادی آنجا هستند که همه‌شان حزب‌الله نیستند.»
رئیس‌جمهوری آمریکا با بیان اینکه اسرائیل زمان زیادی است که با حزب‌الله می‌جنگد و افراد زیادی کشته می‌شوند، پیشنهاد داد که کنترل این گروه به سوریه واگذار شود.
ترامپ با تمجید از عملکرد احمد الشرع، رئیس‌جمهوری سوریه در ساماندهی سریع این کشور گفت: «او با مشارکت من و اردوغان روی کار آمد. او از حزب‌الله خوشش نمی‌آید و این کار را بهتر انجام می‌دهد؛ اگر اسرائیل نمی‌تواند بدون کشتن دیگران کار را تمام کند، سوریه این کار را خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76415" target="_blank">📅 16:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C75IgGpDerBklZIRy8Oi5MDZ37bqsie4XqtINuGjYlVcuWkE-Oeq-vIBv_YWPLoVGzcSLdyJikVknPLNcjDKuzloPFt_nx24RMj5K8kNV206691ZyK66nmRELc_zLoOOPVaE3PHe9BLfzVdmxZndLuTJpBjdP0irhmBw5DmVDquG_NGtAgEvTQaICSDthbGE0Kge92IWp5LzF6nhKRszwIpVszQj8gR6IG9ek0FLR0nt8Ex_Nq3eLPeB7YmnXrMY3LERxIWZ-cL7M8BeUOewI-N-ZezQ9CiemZzrDVXhqnBYuH5d4rUJYUBaMyh85VrAZ3ZvYE-6wE1EMfn6SYN6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در پاسخ به پرسشی درباره متحدان او که نسبت به چارچوب تفاهم با جمهوری اسلامی تردید دارند، از جمله لیندزی گراهام، سناتور جمهوری‌خواه، با لحنی طنزآمیز گفت: «لیندزی تردید دارد؟ باید با او صحبت کنم؛ دچار دردسر بزرگی می‌شود.»
ترامپ سپس تلاش کرد نگرانی‌ها در میان هم‌حزبی‌های خود را کم‌اهمیت جلوه دهد و گفت گراهام «آدم خوبی» است و مشکلی با این توافق ندارد.
او افزود: «این توافق یک موضوع مهم را به‌خوبی پوشش می‌دهد. ما بابت آن هیچ پولی پرداخت نمی‌کنیم.»
رییس‌جمهوری آمریکا ادامه داد: «بازارها اکنون نسبت به زمانی که کار را آغاز کردیم در سطح بالاتری قرار دارند.»
ترامپ گفت: «اختلاف فقط بر سر یک موضوع است؛ این‌که ایران هرگز سلاح هسته‌ای نخواهد داشت؛ هرگز، هرگز و هرگز.» او افزود: «بقیه مسائل اهمیتی ندارند.»
@
VahidOOnLine
آپدیت:
توییت گراهام
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76414" target="_blank">📅 16:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pVekf_bY7XJqLuCbw6KjfvHv7yHqhOmL_Nf97rypb-XrsjgkCkelWAbDfiTjuR0OlmIaX45cULMW-7WEZ60p8nzSuIb6a7_LWmO6hGadhnYeSzH6xp4xnKZ4y8rMyK9qUzCGOCG1PTioUnIJUwbgDVuJzfKu6g228qhG33I-QWPjs_P-vtAASCbRvECNR7RD14PmG3tVpsvKl3tEVhkELAflceivQ6EMizG74CKZXOfqA5jYh_GH-aQxN47Q1HAP9jd79G8RXmX_EEFv0kn8TeJhu1SVBQa02jVdHPvsuO4IiJwWToQWcJCVv9MmGx3AcJIRxZkAWrhD2bOkrCZe2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JIQPJIhMA1v8-vLBgorPNypWIFxJ1K1DENC3QDtOegsfYjRVqfjoHnraX2_5HZR-4bYZh_wyiMZLo3cRwz91Ef8v5yr6iKoP9z094pbn_kj0UZS-StYqZBfca-NLhYrkg2zMXhLQ3XWWYwzGEroThFIO68ozhRN7GKehlXjmvDGWzqw8bFr_B9eO653HaZLbt3zWAQhpNj2DgIKgLPpO-1WWkwyGiySCuIcsJhxTA-hdEDu-2yzma4frkPQluhTXj6x3n-4XyEHKfhiPpEVHZbBv0siGom_948XAgLhrdUKZffMgJmhWs79jCW-L5ySHof7Oi25FS56rXrG7TdKx1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی درباره دو پست قبلی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76412" target="_blank">📅 16:44 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
