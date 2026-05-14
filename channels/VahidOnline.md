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
<img src="https://cdn1.telesco.pe/file/HMT-U8covYXy3tpq-y0ZG0a4MB3FCs62JSJJ_V1bC06Ii8XpqMtBTW7ECc2fahsncCcSTkgK9bTb9DmrEtOt4uWfdnUTcNw6pE_Pw1BUgbPO-9Yqyx02VlSZPCph6vibGB3j2rpR0-LWK6fF2dhIaaIn1PFPkfHlFsVakzpyzk_ll1cbWpqStZD00zckmMd4erphxOwkHDV-2RDu7B7_YvSn7Cn7qL2p-_TUSARns-9lc1KC7Zpu-U_pvlUngi3ifoP_xzVb8q5v5jvgVGufPdAopAgj7fynslCf_KrCez8wNfS0twIzmi5zdG9NkFTb14Q6-07pBDOaMHgdPpXy2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 07:08:59</div>
<hr>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BWFpApOxzn-PKPY99L6x5R0nGFc8oF-yC2RQ0fz4zs0bsmF45CCGAxkgxYBc_yBZR2ELt6YPWsTlRNZUhTHSi-DPSmea-420GMwMlrwAsGkhVKKA0F6XWKw9912NaeqKyO52yTjNTPaOMTBj2lxbXwvDHGDBKB4CwWbbiy9zXiGF4BpIA8eF_Rc880BgMlw2HiAceoOSoQTo_esPruKb9RdlCwfWq9pzjqdT79yr6JUdTUlc9gjQGABxzYS8GVphWupZzU74XxN7da9OKHPquJlFt0e1a90BLDZ58uLAWyN0x9Q2qED_2szsLbPNQPsg3Bx_XV93petpXbsct-Xz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی اعلام کرد گزارش‌های منتشرشده درباره سفر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به این کشور صحت ندارد.
پیش‌تر دفتر نخست‌وزیری اسرائیل اعلام کرد بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی، به‌طور مخفیانه به امارات متحده عربی سفر کرده و در این سفر با محمد بن زاید آل نهیان، رییس امارات متحده عربی، دیدار کرد.
وزارت خارجه امارات متحده عربی اعلام کرد روابط این کشور با اسرائیل علنی است و در چارچوب توافق‌نامه‌های ابراهیم که به‌طور عمومی اعلام شده‌اند، برقرار شده است.
وزارت خارجه امارات متحده عربی افزود این روابط مبتنی بر محرمانگی نیست و هرگونه ادعا درباره سفرها یا ترتیبات اعلام‌نشده «بی‌اساس» است، مگر آن‌که به‌صورت رسمی از سوی امارات متحده عربی اعلام شود.
عباس عراقچی در واکنش به سفر نتانیاهو به امارات متحده عربی در زمان جنگ، نوشت: همکاری با اسرائیل در این مسیر غیرقابل بخشش است. افرادی که برای ایجاد اختلاف با اسرائیل همکاری می‌کنند، پاسخگو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/VahidOnline/75454" target="_blank">📅 00:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOGY9A28aAMN5wcl6JONtrcpq5Bll4BKMy_5n1211-N6CTxCdK8K7AO8QbavZGVes_QwYm1rTAEdLfGe9GfiCocXxXoKK3JfB7Db1-Q89tnuv_QgwLrJwvBAhXhvNk9T74iIHjlN3DegX3xMowEwj7PtiuGG1O5umFhJCLkJjeDRjh0-HEJCyN1wg3EF41Up2cZ8i3Z0cKO0zE_CPcYYhME9ZDy75zrScIpGITOhbRwZxcByhBk9z-XgXjpm8xux1N6oyZU4CjZcRggbfukXsZ9ZPK3rNCfn3zJ4pSOxywzehOsNT-EJqK_s1OMOqntGsEn0ss_FpjvMkH_87yoCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد که واشینگتن معتقد است در مذاکرات با ایران «پیشرفت» حاصل شده، اما هنوز مشخص نیست این پیشرفت برای عبور از خط قرمز دونالد ترامپ کافی باشد یا نه.
آقای ونس روز چهارشنبه در کاخ سفید به خبرنگاران گفت صبح همان روز با جرد کوشنر و استیو ویتکاف درباره ایران گفت‌وگو کرده و همچنین با مقام‌های عرب در تماس بوده است. او افزود: «سوال اصلی این است که آیا این پیشرفت به اندازه‌ای هست که خط قرمز رئیس‌جمهور را تأمین کند یا نه.»
به گفته معاون رئیس‌جمهور آمریکا، خط قرمز ترامپ این است که ایالات متحده مطمئن شود «سازوکارهای کافی» ایجاد شده تا ایران هرگز به سلاح هسته‌ای دست پیدا نکند.
اظهارات ونس در حالی مطرح می‌شود که ترامپ پیش‌تر پیشنهاد تازه ایران در مذاکرات را «غیرقابل قبول» توصیف کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/75453" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sQ1WyOwT63GWDznGTxj55_GXDRk61OvTsoOtFtmrx0pi4NhHKRasD6Ahc_ioWul_hvkUGjaHjxHFxAIP9jHE3Ad94OB307AyvnvQtXLyKhnTH8mJEjdZVVZdQOnUPJ626mao8dzlMcxA8kdtAEc5QcQBKXm72QcBGmd1tzEmDDfy9hCWAXPvVQr87R2saQlypxw-FeG8u6TiFeQyJpQxMOzdIzkRo3L0A1EfMiCdN3qeWvke0r_OslqDId8pK1a8_El-1B3kRtshwM81iGAY2kEFYfRPW4AYfsdEWOi_2RSuUyGNuv50NNcj4uBEyeEUrfzadWLSYjnoafUCDMNC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی شامگاه چهارشنبه ۲۳ اردیبهشت اعلام کرد که محمد عباسی، یکی از بازداشت‌شدگان اعتراضات دی‌ماه سال گذشته به اتهام قتل یک مأمور امنیتی اعدام شده است.
خبرگزاری میزان، وابسته به این قوه، گفته است که او بعد از تأیید حکم توسط دیوان‌عالی کشور و با توجه به «تقاضای اولیا‌ء دم»، «قصاص» شد.
ساعتی پیش‌تر، پایگاه خبری هرانا به نقل از یک منبع نزدیک به خانواده این زندانی نوشت که مسئولان زندان قزلحصار از خانواده محمد عباسی خواستند که برای ملاقات با او به زندان مراجعه کنند، «اما پس از حضور خانواده در زندان، این امکان از نزدیکان او سلب شد. پس از خروج خانواده عباسی از زندان، آنها در تماسی تلفنی از اجرای حکم اعدام محمد عباسی مطلع شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/75452" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYXGcnpMNP4rUdDGfNHNfj-RC5UdBvGVOaeQZHEv_yvyXqLPh0YkleH3ib9Gao0FTd-2ZcxG9TygoWHWQ_KFzr1jjUonaSZG2yP_UKXApZV7ya7-rDGiNWSOQtDeM7NjSkaQiM8tvlM7q2Nm9pQ7vFzVEv9kGc6dLTcb_mtoTUcE6yoYw1xGwrajOuGGNLUekHhKLM6t9G4Bfhkj4ow64bw5tYUjyLnXB3BkEDWqP_MRtIZHGCNKk6nR1c2DTlD_98cnSwAeoqN4VIvehlIFSiBrbQC7L0PKz3TyYZUljynqj2cL0Sa_v8FB8fBLHBETLOwrB2xst_aiyABXxKnRUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل روز چهارشنبه اعلام کرد که بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با ایران، به‌طور «محرمانه» به امارات متحده عربی سفر کرده بود.
در این بیانیه آمده که نتانیاهو با شیخ محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
دفتر نخست‌وزیر اسرائیل گفت: «این سفر به یک پیشرفت تاریخی در روابط میان اسرائیل و امارات متحده عربی منجر شد.»
پیش‌تر مقام‌های ارشد آمریکایی تأیید کردند که اسرائیل در جریان جنگ با ایران، یک سامانه پدافندی «گنبد آهنین» به همراه نیروهایی برای بهره‌برداری از آن به امارات اعزام کرده است.
همچنین به گفته مقام‌های عرب و یک منبع آگاه که با روزنامه وال‌استریت جورنال گفت‌وگو کردند، دیوید بارنئا، رئیس موساد، دست‌کم دو بار در طول جنگ با ایران به امارات سفر کرد تا دربارهٔ هماهنگی‌های مربوط به این درگیری رایزنی کند.
@
VahidHeadline
آپدیت:
امارات تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/75451" target="_blank">📅 21:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O14IFO4Leg8r14i-eJQcq6nBidwI05y_mv0HYxPhz1Hob3svJpkwytROq9IRVuo2h1LLuSiM-fSnBnulBU-6A2En5gYgg85rYR2oQtcsGtdThWUrISzoggOQW7wrFWWDbfRu5Uo_QUVXUYNEHCyKN_OjMRCJAXXKCfjN9TbzIXbZFC2d-GVB--L9G805okiFEA8OwOGidijWnRwdKKrXHBVJEa1rSa5wkqsrsDCVOJKLsk35G6xZ5lvG3XB-IIzXdv5vEeqQ1TA4Dqgwyvd5el0pJotGPU6ns4W-2O1mCJD42p-ALEw4muh00AFqWOLmuTHvmUanTjlmWgn-bLeATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده روز چهارشنبه ۲۳ اردیبهشت با تاکید بر ادامه محاصره دریایی بنادر ایران اعلام کرد که از زمان آغاز این عملیات، به ۱۵ کشتی حامل کمک‌های بشردوستانه اجازه عبور داده شده است.
سنتکام در پیامی در شبکه ایکس نوشت که نیروهای آمریکایی طی چهار هفته گذشته ۶۷ کشتی تجاری را وادار به تغییر مسیر کرده و چهار شناور را نیز برای اجرای محاصره «از کار انداخته‌اند».
این فرماندهی همچنین اعلام کرد اوایل هفته جاری، دو کشتی تجاری دیگر پس از تماس رادیویی و شلیک تیر هشدار از سوی نیروهای آمریکایی مسیر خود را تغییر داده و از ادامه حرکت به سمت بنادر ایران منصرف شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75449" target="_blank">📅 19:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=UYn6kupIf4VDPIzqRMYteucjuKYetzCpABBuOkua5kOUrT7mv4fD_kzvRLM_msKyolMVPIoQVMo-MofJJVwZxt0nqvM9XresAa0e3J5T_WyxLSUHLjlWCA2V0P7CjyhYi9LGdg-suHAJsLqw6bhhMz5gUffNiG1a7XM7FO1Rx-s85XiQDoxV3amAut10tyKDKG7kNa5DXavWaA0qL80w3DWr4zBrgcENn2nwvIKZuALvNHhIcFi6OmxPKIm5Gw1ACl53jhNXa2E0O3mEFyhw0NLUH1CEBLneJW76AAXYo1fhWdasfF719sYvsosZCQQllbdScZsUKrrsW-rLNfGLIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=UYn6kupIf4VDPIzqRMYteucjuKYetzCpABBuOkua5kOUrT7mv4fD_kzvRLM_msKyolMVPIoQVMo-MofJJVwZxt0nqvM9XresAa0e3J5T_WyxLSUHLjlWCA2V0P7CjyhYi9LGdg-suHAJsLqw6bhhMz5gUffNiG1a7XM7FO1Rx-s85XiQDoxV3amAut10tyKDKG7kNa5DXavWaA0qL80w3DWr4zBrgcENn2nwvIKZuALvNHhIcFi6OmxPKIm5Gw1ACl53jhNXa2E0O3mEFyhw0NLUH1CEBLneJW76AAXYo1fhWdasfF719sYvsosZCQQllbdScZsUKrrsW-rLNfGLIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ‌های ملی‌پوشان فوتبال در صداوسیما درباره میزان تحصیلات دانشگاهی‌شان جنجالی شد.
در این گفتگو، یکی از ملی‌پوشان در پاسخ به سوال مجری که پرسیده بود «در کدام دانشگاه درس می‌خوانی؟» گفت: «نمی‌دانم، الان حضور ذهن ندارم».
در دوره قبلی جام جهانی نیز انتشار ویدیویی از دروازه‌بان تیم ملی فوتبال ایران که گفته بود «من دکترا دارم»، بحث‌برانگیز شده بود؛ دکترایی که بعدها مشخص شد به‌صورت غیرحضوری در رشته تربیت بدنی دانشگاه پیام نور اخذ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/75448" target="_blank">📅 18:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA5t2YJ66l6D4r6kWOB6gtUby7uZddouscSQ9RBZIlxhqkpx9Us0kKl4aPcSEef648Kw60y3zC-z_1t8tUWTBXhyJLqyace-5I4w7w09dfkrXtWgJ8xy1bLAowxIgJFWyvhqDXfS8VQOlSz71mDt5CwFhZ7q9xkUFr8OEKOXvvSsfjcz2vq_MZXglTrdSQy_q-IMHaV_qrQrPH6lcRnCeXjGCmdBpAaGcWQYfaZNMFcWvB0cNY5PplUqQLDZaOwHLy-Je44fli7CImAkJMmJy6zxPlcRFC2YV0YOX65xFsILdzdHYBcwfOrfQcz7qVKiFDKlxX-lq74Fzx84xHAtBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از دو مقام غربی و دو مقام ایرانی گزارش داد عربستان سعودی در جریان جنگ خاورمیانه، در پاسخ به حملاتی که در خاک این کشور انجام شده بود، چندین حمله اعلام‌نشده در ایران انجام داده است.
به گفته دو مقام غربی، این حملات توسط نیروی هوایی عربستان سعودی و در اواخر ماه مارس انجام شده‌اند. یکی از این مقامات گفت این حملات «اقداماتی تلافی‌جویانه در پاسخ به حملاتی بود که عربستان سعودی هدف آن قرار گرفته بود»
رویترز با اشاره به گزارش‌های پیشین درباره حملات امارات متحده عربی به ایران نوشت اقدامات عربستان سعودی و امارات متحده نشان می‌دهد کشورهای عربی خلیج فارس که هدف حملات جمهوری اسلامی قرار گرفته‌اند، به‌تدریج وارد فاز پاسخ‌گویی مستقیم شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/75447" target="_blank">📅 18:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIT32DOKjVCT_sbkUhWvz45WxT5dQEsmLT-Brt7ipyBs5j4oh1JECRx_JhvEP5C7Bpd4b7yI8hPcR1FL-jHqhYwGIip30W79881UuQD8XPTsTUo7RjgvU57USxoQ2-FrgXZyHWgfOirFeoDflvBghPAF8ikRkM84oBVXG3tdhTkqsOjiJxBpPCQdGgUBPJda3Zi7T29jWCeBKN_z-c0c8muyUShZaJdJlJl2MjiydlI8JRhULOdi1g8G-jd8LxITNoHdL748pPyia6B00yiCUCfxOftzig3FzfEjgtq_Yj_tEj6mBAhaiV9Uuawa28tDX9aEzUs9XLu8KMwxDsKXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کمیسیون مستقل اسرائیلی جزئیات تکان‌دهنده‌ای از خشونت جنسی «سیستماتیک و گسترده» توسط حماس و سایر گروه‌های مسلح فلسطینی در جریان حملات ۷ اکتبر ۲۰۲۳ و علیه گروگان‌ها منتشر کرده است.
گزارش ۳۰۰ صفحه‌ای این کمیسیون نتیجه‌گیری می‌کند که تجاوز و شکنجه جنسی «با هدف به حداکثر رساندن درد و رنج» انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/75446" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PIZxgnGUQ27EKKKnPLzG9dPIAo4zWkZMYVTg26JFWqmd106wlx7vmnNnJviEE_S-EZC9xYuUdhxSDVk0yFgP73e7JXel7pc0g3gcZgi14mCU723FmYWqxhDGqLSFgyf1-ECnDRF6XbKblHePBNa85EmeyBk2toGUFSgEKUoAVccfjO7bgyjGFuNNuXTMvP1PmJ2-oyHp2G_6WsMk-24tYIuA4keIcgHxjr1UzTr_Cjg59Lq47vedyZ8h-fGjcWP17wZTVUvxIYeYlENXFGVovGHxfzGjkfXlFlbhzh71TGWtaP3Qpgh_c0-DG_U5mPnDNbLvplgWZkcmSvoUGqEhow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، محمدرضا عارف، معاون اول خود، را به ریاست «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» منصوب کرد.
در حکم آقای پزشکیان بر «حکمرانی یکپارچه» در فضای مجازی، پایان دادن به «چندصدایی» و جلوگیری از «موازی‌کاری» میان نهادهای مسئول تأکید شده است.
این انتصاب در حالی انجام می‌شود که امروز هفتاد و پنجمین روز اختلال و محدودیت گسترده اینترنت در ایران است.
حکومت ایران از ۹ اسفند (۲۸ فوریه) و همزمان با حملات اسرائیل و آمریکا، دسترسی به اینترنت بین‌الملل را قطع کرد و تماس‌ تلفنی با خارج از ایران هم با اختلال جدی رو‌به‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/75445" target="_blank">📅 17:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jei5nMTri7ibMtCTTk3oJN1HkZc7OVjd7EotNnrTX7ZIhEqFHd7siMC5xHkdOc60uyi60KoaHwPjEfkhQ0OOQPoAZKxoyMv9ILPN_FY7yN506v6z0S1EeFj0NzBPb4FqMK7eI0kJ_N2GyJSh9rkZkQ4v0zGagwc4fnMjE0t_My00iYi77P20WrNXH89R8cvFTXKyu6LS0TQ1_p-HXCZ7fQClQvZVlrx_eWM1AMqTYEXaH3bEqiIhWKJzi0dslEOCmTjnE72IUpMf_BnTOsDsndKIPhDsAdyRj91XZP63tj7PETvX7iccPOjCUFMwceguz2hg77kWshg9QjRN98DSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، مهدی زارع، زلزله‌شناس و استاد پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله با اشاره به زمین‌لرزه به بزرگی ۷.۱ در قرن نوزدهم در گسل شرق تهران گفت: «وقوع زلزله‌های ۴ ریشتری اخیر در ۲۸ فروردین و ۲۲ اردیبهشت در پردیس نشان از تخلیه انرژی دارد. وقوع زمین‌لرزه‌های کوچک به صورت مستمر، بخشی از انرژی گسل را تخلیه می‌کند، ولی این لرزه‌ها می‌توانند نشانه‌ای از ناپایداری در پهنه‌ای وسیع‌تر باشند که مقدمه رویداد بزرگتری است.
به عبارت دیگر، لرزه‌های خرد و متوسط، هرچند تا حدی تنش را کاهش می‌دهند، اما نمی‌توانند به طور قطع احتمال وقوع یک زلزله بزرگ را منتفی کنند. در برخی موارد، چنین توالی‌هایی می‌توانند پیش‌لرزه (foreshock) باشند.»
@
VahidOOnLine
امروز پیام‌هایی از پس‌لرزه یا پیش‌لرزه ساعت ۱۲:۳۳ دریافت کرده بودم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75444" target="_blank">📅 17:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCc7lDOSE8QLQz827-lAlxQqXnHQQx_nE22HDCoVPt8ELhJ7s-Psgao0rj34e-DSgade3RNQBQOZQ-kegNc0Dv50UUUmHumkYztlI5na9aZ_1-lLcxI-myMnSiRx3_auTv69A2aWrRwQJQxSGiGQMNkA-gq9PHhmCFhaZQkJ2gK1RHzA45zqw5_774hc7YEZ5KXDEXOvXxs-olDLDiyIN4MophTgYOH0xhXIeiZkLzj-CSEpzyX9rEKE_2mFVXSuHPaVHOJcez8o6DcrmlLtoRIPWvCYghqR5XoCtV6mG0fb9HW4ArV3h0v8xn0zpOt1gghfsKCs7hEvjGWp7CE_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احسان شیرخانی، شهروند ۳۵ ساله اهل شهرستان ملکان در استان آذربایجان شرقی، بامداد روز سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، با شلیک مستقیم نیروهای بسیج در ایست بازرسی شهرستان بناب جان خود را از دست داد.
بر اساس گزارش رسیده به ایران‌وایر، نیروهای مستقر در ایست بازرسی بسیج شهرستان بناب، خودروی این شهروند را به بهانه «عدم توجه به دستور ایست» هدف تیراندازی مستقیم قرار داده‌اند.
یک منبع مطلع در این‌باره به ایران‌وایر گفت که نیروهای بسیج بدون رعایت قانون به‌کارگیری سلاح و بدون شلیک تیر هوایی، مستقیما به سمت اتاق خودرو تیراندازی کرده‌اند. به گفته این منبع، چهار گلوله به احسان شیرخانی اصابت کرده و او در دم جان باخته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/75443" target="_blank">📅 17:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V-P_gDvnq04fdrhMCvSt-KOV3kFu3aO_50Me4UhzwjDGIwZylc6v6aaSOOvV6cmIw6PnqFYGJxSiNPIj2EREnZbfHelm89ILnosMBMXfC4RrYlzJbxlDsX4PPc967fQ3R24WS5L3wrFob6DlATu8iuNJy_qxRlr-YKKF12W_KNoBwFah2V47j6Dj1t_ZHengYG0i7he4FRlYMecL04C4fQCZfcj-TteJVqJ4PNZ4rj0dKEIeOUL1Mzeo_78i6W1o_prA68sx2kcTak3ckCq-4a1qM6VgUKmq2Y6MY3BQAJmP_9yYHJc6FtF13qCHhD_QRIJ4cLJz6G4jAi1JJYyPEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vu5CnyLcuLL-CzUGNORBrhMr9aLPz3WHleKOljVeXuUMaaGgs8AmXMwtUy-HbhqElSFFyFVc-edOLMCJ3JgrwtLyfpuEz8A1lQd0jrhmQUnPqY7ZqSv6bo95wfRkleMiecu_VpQd7lKxU_OMG9apqPVmi0s3XWrj_CUXB9b1E2i2hrd7QsF41dsyDBK-rWR0C4hj9dWZCa1U_hfQcVoXczpwlt8diJXIJa1UlFFtg_cCO4a_dckiO_O_VCL6q5DAp8hFv2aN6CBHU3N4ZppPWyTWJYeRs7YLTslapGi8Xktg1CgoWDpz7Qv8fLJy7A2TfkWcegsJnS7bRUxiCkgPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GLCbzzhAQrWO_qBrJK6nGyHuY9f_UE3hQDX3Hz7r4ikd7J7T2oARGOTw1Cj1q3U7Bbg-aqxDmH5YCQ9uGkLRPzobmqayrXRIu7eHzd0XnuL6DoDDkHcWe0ddE8ZFclazelbO95IE2U8kG0Vz08XqcUzNVE74vqPrfEY9lPxdZPh-bwpa32Rpj-ctT2-zqzALk3bSvvaWFyLFC74VSmbyQTz-gTNceYUZxFSlcBkJXK_JwAqlh0wm6qtb0t0kORFpFtJ4XyvoTjJPCajbr1ZMRWfOKb3XlEKcMhFM2qn3Z102cHt-5umCWR-LrR4QYCc_AuVQDvGsUMWS6DUSm9jFsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UlB4-9vf2e-2TfGmBmwe4z1gVQZcrZIzGjlyJybenvxiAmzTMJN-f1pwgcC0PQqwGZ6barOJy93knVfAI4cGANMEY1Ly99zAUxb1ErNyAFcD37FRKZbTNFjGOUIhv74bCKlJYgQUjE8lX4amSQZ0B-tPx7jBM2ESP5bnekkGGdrsFMGba9Sh2eWgrRArbxd8cvAdgQb_-DnFbaWJZUz2VDw1o5QnRKYPmwLAOwON6XKOEogxTuRTU2oHCDZ5Db4f05oQSi5ACHYSR3HMYy-OlE5MvXiXyG6wyY9jqkHiqx5EAwNCSJpx7X3N2qw_aZTUzovBAV_ZL4oRliwEJFoBBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قوه قضائیه ایران یک زندانی دیگر به نام احسان افرشته را به اتهام «جاسوسی» برای اسرائیل اعدام کرد.
میزان‌نیوز نوشته که افراشته که «در نپال توسط موساد آموزش دیده بود و اطلاعات حساس کشور را به اسرائیل می‌فروخت»، بامداد چهارشنبه ۲۳ اردیبهشت اعدام شد.
در بخشی از گزارش بدون اشاره به جزئیات آمده که او «به عنوان کارشناس سایبری در یک شرکت وابسته نهاد نظامی مشغول به فعالیت» بود.
با این حال در گزارش مفصلی که ارگان رسمی دستگاه قضایی ایران درباره این زندانی منتشر کرده، مشخص نیست که او چه زمانی بازداشت و دادگاهی شده و از جزئیات روند محاکمهٔ او نیز اطلاعاتی منتشر نکرده است.
شماری از وب‌سایت‌ها و نهادهای حقوق بشری نوشته‌اند که احسان افرشته، متولد سال ۱۳۷۲ و فارغ‌التحصیل کارشناسی ارشد مهندسی عمران و متخصص شبکه، اوایل سال ۱۴۰۳ پس از بازگشت از ترکیه بازداشت شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75439" target="_blank">📅 08:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ilajmroBqEC5AemlWBqFZFzRiGgJ6MzK4rRazh9snqogUK6EHpQ7hyLG6wIg0099JRYSVdgMiaZBsAMdSVUc_gnHj4KLpdlwE_NMl2FRwVkhXsx5Cg6PL0GyQLLIgMNSm1gy68Bmb9JJuH-gIFevTS2-ZE1Sj8-BD5hHaR7Q612Ax5ziB5SlIwHPzWf1Mhq8-i6UNX8orcQC8z5HaGc-qqViFUtNopTMCrMfRW96mohQ7nZK2qb456hTmp1dNzWMjfXBQrGhdMpVykiaddCtlqhrOn4mzxt-SpfZoClj_xQzuuQjKudR4hJHc-rQaAULg69CkKpfwyQNTbZWKTt1Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه چهارم۰۰:۳۳
پیام‌های دریافتی:
دوباره لرزید  شرق همین الان 12:33
بازم اومد ولی ریزتر از قبلی
همین الان دوباره لرزید (نارمک ) ۰۰:۳۳
من الان دوباره لرزیدم
وحیددد نزدیک چهاربار تو پردیس
#زلزله
اومد نمیدونی تختم چجوری میلرزید
آپدیت: تصویر دریافتی بالا و متن رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
بزرگی: ۳.۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان وقوع: ۳۲ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۱۰ کیلومتر
🔹
نزدیک‌ترین شهرها:
۱۰ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۱ کیلومتری تهران
۷۶ کیلومتری كرج
🔄
آپدیت ۳:۳۰
پیام‌های دریافتی درباره لرزش پنجم
زلزله دوباره
ساعت ۳:۳۳ شرق تهران باز زلزله اومد
پردیس،۵ دقیقه پیش برای پنجمین بار زلزله اومد وحید جان سابقه نداشته تا حالا خیلی مشکوکه
ساعت ۳:۳۵
پردیس دوباره لرزید سه و نیم
سلام وحید جان
ساعت ۳.۵ باز زمین لرزه اومد پردیس، با صدایی شبیه به ترکیدن
🔄
آپدیت: لرزش ششم ساعت ۵:۵۷
یه کوچولو دیگه زلزله سمت پردیس حس شد الان
و الان هم دوباره لرزید
٥:٥٧ دوباره پس لرزه اما خفيف تر
آقا وحید ساعت ۵:۵۵ دقیقه صبح، پردیس برای ششمین بار لرزش احساس شد
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/75438" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">زمین‌لرزه دیگری به بزرگی ۴
این میشه سومین بار ظرف چند ساعت گذشته! اولین باردر شرق استان احساس شد و پیام‌ها از پردیس و بومهن و دماوند بود و یکی هم از لواسان]
پیام‌های دریافتی لرزش سوم:
تهران مجددا لرزید
دوباره لرزید کمی خفیف‌تر
وحید جان دوباره لرزیدیم  شرق تهران .. ۲۷
دوباره! پس لرزه بود.
دوباره هم اومد ولی ضعیف بود خوشبختانه
وحید جان شاید باورت نشه اما سومیش هم همین الان اومد، منتها خیلی کوتاه و کم بود...
ان، زلزله، ۰۰:۲۷
باز اومد، کوتاه، شاید پس لرزه باشه
دوباره اومد
یعنی اون رفت این برگشت
دوباره زلزله اومد
باز هم لرزش ۱۲:۲۷
سلام بازم لرزید حدود دو سه دقیقه پیش طوفانم هست خدا رحم کنه تو این شرایط فقط بلایای طبیعی کم داریم
اینجا ازگل، ۱۲:۲۷دقیقه، دوباره لرزید
🔄
رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
🔹
بزرگی: ۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان: ۲۶ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۸ کیلومتر
🔹
نزدیک‌ترین شهرها:
۹ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۰ کیلومتری تهران
۷۶ کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75437" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IhV0UDCpsAGLvgK7Cx4ZLnTKTvd-W0l-sn1pYYY5cIR0v_OxqBFuY4VAC1yjl8HIGcdmRGgY1cGOMjEwvTtcUp2sSKbNRPCv9volyaZTPh88XXzWdGy7jWWJ0pwkr5yPL55FYjNiz42Bo2PlTuMhNPihmzZsKRNmYTUArhRp4tA4hqMFxW9ee2-JnJUc36W4q9L4ZmpNrbe2OXFbdI_bP_HtZD4P95Za0SHOaQWGm6gMdfRy6Qv0zrYwa6Q7Y6eJ8bWXV7ONYqRl_XoajUOKoIqwr0F2zmHphaiQyMBjk9Rzj9tFBaigcbythl2-RA6numso4T-yb0Bg-4U63qyscg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی «رسانه‌های جعلی» می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آن‌ها به دشمن کمک و از او حمایت می‌کنند! تنها نتیجه‌اش این است که به ایران امیدی واهی می‌دهد؛ در حالی که اصلاً نباید چنین امیدی وجود داشته باشد. این‌ها بزدل‌های آمریکایی هستند که علیه کشور خودمان طرف می‌گیرند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت؛ تک‌تک آن کشتی‌ها اکنون در کف دریا آرمیده‌اند. آن‌ها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان از بین رفته، تمام فناوری‌شان نابود شده، «رهبران»شان دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلالی مطرح کنند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/75436" target="_blank">📅 23:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">"وحید تهران لرزید"
+ ده‌ها پیام دریافتی مشابه درباره احساس لرزش زمین در مناطق مختلف تهران
به نظر می‌رسه بیشتر پیام‌ها از سمت شرق و شمال شرق تهران هستند گرچه در غرب شهر هم کاملا حس شده.
حدود سه ساعت پیش هم در شرق استان تهران حوالی پردیس و بومهن و دماوند زمین‌‌لرزه خفیف‌تری حس شده بود و غیر از اون مناطق فقط یک پیام از لواسان داشتم و پیامی از خود تهران نداشتم.
🔄
رسانه‌های داخلی:
زمین‌لرزه‌ای به بزرگی ۴.۶  ساعت ۲۳:۴۶ امشب مرز استان‌های تهران و مازندران را لرزاند.
این زلزله در حوالی شهر پردیس و در عمق ۱۰ کیلومتری زمین به وقوع پیوسته و در بخش‌هایی از پایتخت نیز احساس شده است.
بزرگی: 4.6
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
طول جغرافیایی: 51.83
عرض جغرافیایی: 35.82
عمق زمین‌لرزه: 10 کیلومتر
نزدیک‌ترین شهرها:
8 کیلومتری پرديس (تهران)
10 کیلومتری بومهن (تهران)
11 کیلومتری رودهن (تهران)
نزدیکترین مراکز استان:
41 کیلومتری تهران
77 کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/75435" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZLYDJYnUbDMRKMQ8X18poEgak23idrmp6Usu88RFJqfAvFoUzYv-LnW9tapo43LHMoBggSMw0sdyXsAtaJriq6hzGp2l1NLQ3WmIInKZXKN7-WSGS_aksGoxxzCW3UMflk7NrNY91UoHLWHhCFF553JTicADWT5bwSSsd5n2mRiRy_b41MSj0EW8g8uNAQHbG92gWypyLqX9ZOQeIO1AWTMtYsEpeCTCSyvSjbx7uuVNycHX24NrdbqWJjTG7tn3etWuMIo3eRB-ycW816yC-unfOaL40_urLzTnK8eN8Rvrl2nx5Ch_c7kVAbD7KKSFETnV5CbybxsFjp1ntGFESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=mPgvtGwmcivGeZiQxDkyh6QCzya0_s1GuaMS_UKldHcD0PFlZFpptbCNjqCQzFQevZM25LMhx6znRf97YIn6bxzjRBck15pUORGZL1Ziy0hZEfFW2fbN60EcGxAZtyNVxgYnMeKSjF7L71MydPxu5oqG3q-vPlA4AHLEKGDV7360-RQmxWD4lwZNpZ5xciE72ddqWiwv3TaOLPBGRMNU8Pcs1vb4vffMqCKMfvsdNwOkjmdfqi6LbBXqC6rLUMkweDPNyO8rX2s1z6UKyzmdlV421gOpBxXqA5JEckiJPEjp0ANRdX_pRWEEaEa6ckWVA-POMD_xpf0Fo54bCCE6OA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=mPgvtGwmcivGeZiQxDkyh6QCzya0_s1GuaMS_UKldHcD0PFlZFpptbCNjqCQzFQevZM25LMhx6znRf97YIn6bxzjRBck15pUORGZL1Ziy0hZEfFW2fbN60EcGxAZtyNVxgYnMeKSjF7L71MydPxu5oqG3q-vPlA4AHLEKGDV7360-RQmxWD4lwZNpZ5xciE72ddqWiwv3TaOLPBGRMNU8Pcs1vb4vffMqCKMfvsdNwOkjmdfqi6LbBXqC6rLUMkweDPNyO8rX2s1z6UKyzmdlV421gOpBxXqA5JEckiJPEjp0ANRdX_pRWEEaEa6ckWVA-POMD_xpf0Fo54bCCE6OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: خواهیم دید چه خواهد شد
دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از سفر به پکن گفت که رئیس‌جمهور چین درباره جنگ ایران «نسبتاً خوب» عمل کرده است، اما واشینگتن به کمک او نیازی ندارد.
او روز سه شنبه در جمع خبرنگاران افزود که قرار است با شی جین‌پینگ «گفت‌وگویی طولانی» درباره ایران داشته باشد.
ترامپ تصریح کرد: «فکر نمی‌کنم ما به هیچ کمکی درباره ایران نیاز داشته باشیم. ما به هر شکلی که باشد پیروز خواهیم شد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری.»
رئیس‌جمهور آمریکا با اشاره به این که توان نظامی ایران در جنگ اخیر از بین رفته است، هشدار داد: ««ایران یا کار درست را انجام خواهد داد یا ما کار را تمام خواهیم کرد.»
او به جزئیات بیشتری درباره این هشدار اشاره نکرد، اما این اظهارات در حالی است که ترامپ پیشنهاد آخر ایران برای توافق پایان جنگ را در روزهای اخیر رد کرده و آن را «کاملا غیر قابل قبول» و «فوق‌العاده ضعیف» خوانده است.
رئیس‌جمهور آمریکا قرار است چهارشنبه برای دیداری رسمی وارد پایتخت چین شود. این سفر که قرار بود در ماه مارس انجام شود، به دلیل درگیری نظامی آمریکا و اسرائیل با ایران چند هفته به تأخیر افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75433" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZSdYI19yH98-TNBLYS5nyTeFyjXCV3_Y3fUr2LQGvvKm7juliOSeEGn8N_Dg5OhFWpD5gBIJqQlb_TCT_QvrsbK2C3ffzEmBycEp2O_8RvWfSAk-3TeJriw_JHPQLb2PQQnNSAtViXPYolkrXJiuZ3Vm75haLnRAgF3WoUUsgjw5AA9yiR_H-TYOz526r6-LROT_-KkRPvO3vGGx-bj-G0x-gPGD-7PSQ3neEWgcvUH14I31U6dK6nouVW7gmenQFUQRmXWeICpK_lS2xR8LlsjU8tN40XUd6sVvslNCU500JgmbQOHHB7y3V4jV1ObHG0_PjPxIZreNeuWvhVR6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با برنامه رادیویی «سید رازبرگ» گفت: انتظار داریم اقتصاد ایران زیر فشارهای ناشی از محاصره بنادرش فرو بپاشد.
او افزود این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.
ترامپ گفت ایالات متحده در حال انجام ارتباطات مستقیم با مقام‌های تهران است و برای رسیدن به توافق عجله‌ای ندارد و او اطمینان دارد که تهران غنی‌سازی اورانیوم را به‌طور کامل متوقف خواهد کرد.
@
VahidOOnLine
دونالد ترامپ گفت حکومت ایران با انزاویی روبه‌روست که آن را از منابع درآمدش محروم می‌کند و انتظار می‌رود اقتصاد ایران زیر فشارهای ناشی از محاصره بندرها دچار فروپاشی شود.
او افزود: «این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.»
دونالد ترامپ درباره اورانیوم غنی‌شده در ایران گفت مقام‌های جمهوری اسلامی به او گفته‌اند قرار است آنچه او «گردوغبار هسته‌ای» می‌نامد در اختیار آمریکا قرار گیرد، اما بعدا نظرشان را تغییر داده‌اند. او تاکید کرد در نهایت این مواد را به دست خواهند آورد و موضوع را جمع‌وجور می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75432" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmhNoHaEik-Ll5juwD9o9NUVUp4WpfijvOhKH4aJbjs8-tGSlkv4TYLgndufHaqDia9OnJqpI5XGd3B6amU9KkdsMfyBWGhGgR5oWGvvDbKQo0LDqOkGkihVtDfe0zxOkCT-W-KduDV9Qsm0ysxev7zE56wvbfOsPKpdV3DoqZ7zDHAFqp5hMfHw0c7PsVG0H1xYwyqAGUn4HXVZPPiM7CjfiOkRcglZMV8C7lVThNVNTVeFeb9xMYddWjHQR2yEgtkchMMae5ZuXfd_SToG4eA2FzApWqtZDi9lipwMtU5t-m8W3Jy-zF0si0JKA9noUzw5yXklbNVNK7tt_Wmzvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد پنتاگون روز سه‌شنبه ۲۲ اردیبهشت اعلام کرد که جنگ ایالات متحده با ایران تاکنون ۲۹ میلیارد دلار هزینه داشته است، رقمی که نسبت به برآورد ارائه‌شده در اواخر ماه گذشته، چهار میلیارد دلار افزایش نشان می‌دهد.
به گزارش خبرگزاری رویترز، در حالی که تنها شش ماه تا انتخابات میان‌دوره‌ای کنگره آمریکا باقی مانده است، دموکرات‌ها در نظرسنجی‌های عمومی موقعیت بهتری پیدا کرده‌اند و تلاش می‌کنند این جنگ را به مسائل مربوط به هزینه‌های زندگی پیوند بزنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75431" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jyFL5x3nEMqh6laN9MhPbqP9ZnkCIkX-DdCfzUuwyfnUDf3iEWb58TRuF-oWNGHWEFX4rHJ6rXq9bGEZur7jYMnAFn_lRDynfOaiy2pEMUitcsfwXbA4IHPA64Onxy88eYfRp0wjx4w7KQwzmvSfivhNP8nlvDkoPgw-DR08btNsD_4iZ088QSP27zoiUcdd7JvS74pfQdrwTVkX-TK3BbbZ2F6MxprmKIYJ6Ta-5NSM8rqvCkC_E6dG9WpbogJfsSAM-W7K26DNsYyPc2xS_x89o2jcqs_7Vt6IXGzVjUvAkcj5pJA3Z0GEy3wJn_5G9jg19cqYx0GY7xmf1vc47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه در تروث سوشال دو تصویر گرافیکی منتشر کرد که صحنه‌هایی از حمله به پهپادها و قایق‌های جمهوری اسلامی را نشان می‌دهد.
در یکی از این تصاویر، یک ناو آمریکایی با استفاده از سلاح لیزری یک پهپاد جمهوری اسلامی را هدف قرار داده و نابود می‌کند. در تصویر دیگر، یک پهپاد آمریکایی دو قایق جمهوری اسلامی را هدف قرار داده و منهدم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75430" target="_blank">📅 16:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=bETg-71rr9YsJVwujxHqd2UlBmGf_Ujo9HyLIy7UvLgJd2C4anoI1Rx_jtJ4sxsow6rG1vjs-q3TVVt1B3MdxvArrzGLdul8DVbkGNtCY9guqSYjHL-CCEu2GC96yX-nTY-JkTtdIfUbjisw4yNpmoFlZllO6lbyMB_2flc8DhM4WZgXr-Dy4IW33QoVMmt3FUI4N3TZ5hsYivPXW6fmgoYhPM24Pw6FNuoolPGKV9fF0HnaNIj-R1Jf4rdfZhApB_OE3zdATFxABhZAR0ATBMAZtftsGBlIPEg80jgjHrKh7Cpqo_80NwNlKfEATo12NezstCQosHYZeIdM0UCuhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=bETg-71rr9YsJVwujxHqd2UlBmGf_Ujo9HyLIy7UvLgJd2C4anoI1Rx_jtJ4sxsow6rG1vjs-q3TVVt1B3MdxvArrzGLdul8DVbkGNtCY9guqSYjHL-CCEu2GC96yX-nTY-JkTtdIfUbjisw4yNpmoFlZllO6lbyMB_2flc8DhM4WZgXr-Dy4IW33QoVMmt3FUI4N3TZ5hsYivPXW6fmgoYhPM24Pw6FNuoolPGKV9fF0HnaNIj-R1Jf4rdfZhApB_OE3zdATFxABhZAR0ATBMAZtftsGBlIPEg80jgjHrKh7Cpqo_80NwNlKfEATo12NezstCQosHYZeIdM0UCuhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری سخنگوی دولت مسعود پزشکیان روز سه‌شنبه ۲۲ اردیبهشت به دلیل وضعیت اینترنت به بگومگوی خبرنگاران با فاطمه مهاجرانی منجر شد.
سخنگوی دولت تاکید کرد که «اینترنت پرو» با مصوبه شورای عالی امنیت ملی که ریاست آن را مسعود پزشکیان بر عهده دارد،‌ مورد استفاده قرار می‌گیرد.
او در عین حال تاکید کرد که این اینترنت ویژه کسب و کارها است. [در حالیکه خیلی از مردم بدون کسب و کار هم پیامک گرفتند بیاید پرو بخرید]
@
VahidHeadline
فاطمه مهاجرانی گفت با توجه به وضعیت جنگی، فعلا اینترنت عمومی وصل نخواهد شد.
مهاجرانی در پاسخ به پرسش‌های متعدد خبرنگاران درباره وضعیت اینترنت و به‌ویژه «اینترنت پرو» گفت ما در وضعیت جنگی هستیم. رئیس جمهوری به‌عنوان رئیس شورای عالی امنیت ملی پیگیر حقوق مردم است اما وضعیت جنگی است و بعد از پایان شرایط ویژه، اینترنت به‌حالت قبل بازخواهد گشت.»
پس از این سخنان، چند خبرنگار تلاش کردند تا با یادآوری تعهدات دولت پیگیر وضعیت وصل اینترنت شوند. مهاجرانی خطاب به آن‌ها گفت: «وقتی رئیس جمهوری آمریکا می‌گوید آتش‌بس به تنفس مصنوعی وصل است، انتظار شما چیست؟»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت جمهوری اسلامی، با اشاره به قطعی طولانی‌مدت اینترنت در ایران گفت اینترنت حق مردم است و عصبانیت مردم کاملا درست است. اما در ادامه تاکید کرد: «عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود.»
او افزود: «رسانه‌ها کمک کنند که این ادبیات را جا بیندازند. دولت طرفدار دسترسی آزاد است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/75429" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SpvzjGlgh6a3D27-04Gs-BxDFL4hsiOg93_Cek46h8GsC_W6rvqE8isT8RB5OADdND7XXh_bVaEVMbJaCyfmcO7OBvWa971wtofpUyPqHkwi-ekJnalkpyIk352MlZkE9XZRKXk4mOZJV-LhpI1Tnrg1iHspBB2mP2JCrCbzwc9zblKCxpl5WPwkA0_D8UUZorMGa7S2sN7Y-m_-R_zdezqdM2a6_MfQRyOZh2dfQkep-GDdSe21cRVByhrSChppdLsfr-sKdWt5VGzJWgrYcQ_CkJw5FGDRrkOGUACc23J9kXKWRANGIwgqzcpCFKwvN07k_LlH8bRaijgL9dn9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه از اجرای حکم اعدام یک زندانی دیگر به نام عبدالجلیل شه‌بخش در بامداد سه‌شنبه ۲۲ اردیبهشت خبر داد.
ارگان رسمی نهاد قضایی ایران، شه‌بخش را «تروریست آموزش‌دیده» گروه «انصارالفرقان» معرفی کرده است.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75428" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTVCWNkstmTxJxwom5QFVahNP5pJjMDiSxT2Se3au0SbpuOKr8Hi7DsZV-6R2PJiBGBNL_nohZ2_M_AJW4Iu5gMtF_aOIC8j0RJWvy-KD-il3kCkn8bn9kiKx5ZpYZUafJnD-cGtMf5kTXluxuAsdsdnS0JCeRn7SmL4FIk68B-oCyExJVwkuF8G_ZlBmCH5tdAkjyk2-4kVdUMPsRTojFjk0f4rowNDHehz5WkFqFw10q17kKxpZC3uKK44TehFUHZuhRuRaJ4YrVkOu-337rWfuDp8nj1OCOcGGfnebfaaeLPCbQIUPes_jVJYA07HU2phItPKJac-fzfVQN0A1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نشریه آمریکایی وال استریت ژورنال، امارات متحده عربی به‌طور مخفیانه حملات نظامی علیه ایران انجام داده است؛ موضوعی که به گفته منابع آگاه به این نشریه، می تواند امارات را به یکی از طرف‌های فعال مخاصمه با ایران مطرح کند.
منابع آگاه به وال استریت ژورنال گفته‌اند حملاتی که امارات تاکنون به‌صورت علنی تایید نکرده، شامل حمله به یک پالایشگاه در جزیره لاوان در خلیج فارس بوده است.
در اوایل آوریل گذشته و هم‌زمان با اعلام آتش‌بس از سوی دونالد ترامپ چند حمله هوایی به تاسیسات نفتی ایران در جزایر این کشور و اصطلاحا مناطق فلات قاره شرکت ملی نفت ایران صورت گرفت که باعث آتش‌سوزی گسترده و خروج بخش بزرگی از ظرفیت پالایشگاه لاوان از مدار برای چندین ماه شد.
ایران در آن زمان اعلام کرده بود این پالایشگاه در یک «حمله دشمن» هدف قرار گرفته و در پاسخ، موجی از حملات موشکی و پهپادی علیه امارات و کویت انجام داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75427" target="_blank">📅 03:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1KSzHjpltXaWIyryeO16WkgC7gffcD1ChGE0sZNRCnG0Lx1gzHKQzhVb0d-CkeTv_XkCXBu4o465_KUf1o4bocsKmPctcLpoJ3EpyPW6ZsATlinmU6hamE5lBtK4t9hHS71BRfMQK75ZbrSqTMAlcARkHRAb_EKXSvbykDOwvp16XlEZFkntQ0GWcn25SCj3zmRBZxYpHvSWSlXkhBwYa--RVIsdtfZMUFXBg_Cma-4Q_jb6YnQoXO_PsVEXpZNcSYrLFAPbGUXrAiDBb_WIBeYPz1bzU7uXTL-uB3Q3eFi0edOI5Fj7FeOHxV7wtFOn-k3xL_S4YxbjCX0hB3sqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده، روز دوشنبه، ۲۱ اردیبهشت‌ماه، در بیانیه‌ای رسمی اعلام کرد که پاسخ اخیر تهران به پیشنهاد دیپلماتیک واشنگتن، نه‌تنها از نظر سیاسی غیرقابل‌قبول است، بلکه با استانداردهای لازم برای لغو تحریم‌های مالی و اقتصادی نیز همخوانی ندارد.
این وزارتخانه تاکید کرد که رویکرد فعلی ایران مانع از هرگونه گشایش در مسیر مبادلات بین‌المللی و آزادسازی دارایی‌های بلوکه شده می‌شود و تا زمانی که تعهدات شفافی در حوزه برنامه هسته‌ای ارائه نشود، فشارها بر شبکه مالی این کشور ادامه خواهد یافت.
در همین راستا، اسکات بسنت، وزیر خزانه‌داری دولت دونالد ترامپ، در اکس با بازنشر این بیانیه، موضعی قاطعانه اتخاذ کرد.
او با اشاره به اینکه پاسخ تهران نشان‌دهنده عدم تمایل این کشور به همکاری واقعی است، نوشت: «در حالی که دولت ترامپ با حسن نیت مسیری برای دیپلماسی باز کرد، تهران با پاسخی کاملا غیرقابل‌قبول به میز مذاکره بازگشته است.» بسنت تاکید کرد که وزارت خزانه‌داری، سیاست‌های مالی را به گونه‌ای تنظیم خواهد کرد که جمهوری اسلامی متوجه شود عدم پذیرش توافق، هزینه‌های اقتصادی سنگین و غیرقابل‌جبرانی برای نظام پولی و بانکی این کشور به همراه خواهد داشت. او نوشت: «زمان آن رسیده که تهران متوجه شود هزینه لجاجت، فروپاشی کامل اقتصادی است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75426" target="_blank">📅 23:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A6Im-C_wWvYCgU9GVFsTbs9jlSvK40jruuRbO1U7-BrmUEh2I3_qhnGpZ9J3ompLFWV9Jc4FY_9XTxjxw3RM8l4q7FjPBDUfNTn3ceRh8JGVsRaHRk_neWQqrqIbdY1H4gkzfK-WGazQaRemq3PQ_VLQt3vCBMAUwm6eu3ctnY92P7lKCSEEhP58lmBbwo9tjSh12lAQSXuMkSeB0gIjjQNiJL2KOIl43gMhzSaChc1DwKB2X6yiNPjbdNhkEmIQNft6qFkV-2fE9fuZMADoC4MkpFfZ5t1NO7IDgOkBnJSTvWLZ7DXdyQ7yMdgdyI96n0IIX7z_T3KOOybDySU0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیات جمهوری اسلامی در مذاکرات با آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در شبکه اجتماعی اکس نوشت نیروهای مسلح جمهوری اسلامی آماده «پاسخگویی درس‌آموز» به هر تجاوزی هستند.
قالیباف نوشت: «استراتژی اشتباه و تصمیم‌های اشتباه همیشه نتیجه اشتباه خواهد داشت. همه دنیا قبلا این را فهمیده‌اند.»
او افزود: «ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/75425" target="_blank">📅 22:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQHfp5tgFR3DGLJiIXMgDkN2bAI5FAmo4lpzcazdcIddWYU94l1wn51bHyG4eRABLxdVQmIjxWD4JprgHsgfFvSC6PaHKNiljJhf0S5kKNQjEo91ABYzVk9sX0M93sKbPwKwt7sPdufFi9mqgCwRgoOK1OD1C8a8DBNnVzINWBdoxa6On8hWNTDvMXy-uflJA9d2yJYWnBbbhTmD9aRu2oGuzh1bZTt8TEbwPTd1CtX9yAU6fAYwy-3Qoe93MTfSvH2NhMAexXiYwE4TlOrXybbc15RicmzqDCqDBRSeV2GIhSAcmlPRGqeRwxdXexroPvP1bymc5FsdV3v77whaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد دونالد ترامپ روز دوشنبه روز دوشنبه ۲۱ اردیبهشت ۱۴۰۵ با اعضای تیم امنیت ملی خود درباره ادامه جنگ با ایران و احتمال ازسرگیری اقدام نظامی علیه جمهوری اسلامی جلسه برگزار می‌کند.
بر اساس این گزارش، سه مقام آمریکایی گفته‌اند مذاکرات میان تهران و واشنگتن روز یکشنبه به بن‌بست رسیده و همین موضوع گزینه نظامی را دوباره روی میز قرار داده است.
اکسیوس به نقل از مقام‌های آمریکایی نوشت ترامپ همچنان خواهان توافق برای پایان جنگ است، اما رد بسیاری از خواسته‌های آمریکا از سوی ایران و خودداری تهران از دادن امتیاز جدی درباره برنامه هسته‌ای، احتمال اقدام نظامی را افزایش داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75424" target="_blank">📅 22:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ab-ARDwBwJfBlQDyzGSGlAIqDUMHfsWALdFTZJt1ZiwZwzoB0wJ9RRRBTLRIx2MA5oHNEczCHkGRmxegCC_QaEN0OVFu2FWt9Kk2WGgD6PCXIMTgI4rUOUIJCyKkwrgzqgcZs-HXHk1id9dFsvHeLlvVxv9OkEUPnk-b4s9w29mP5EEytdF2xoQndq1CKc19-0ph5ZYI17FTgNBZkOBpJd_8BkTeKklWdo6z3x72K0EhxFK6dET0HAxnFwfzVEobCb-d1ERvKxskSfKroOBc1A-DtSv9Zw_0WddtAZVRafujeM3idJnYW9tNTFxiSyr-Hca2g1RB2_PqC6mm5iyEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Clmhu35gLiL7Jmt37mHWGTk4GgxZQWf8amzD0lvgu6ZElWfIINkOpVjfAy48WWn97fFKsebpHxc-uM3nqRYqq4hTJ-kHsKMJu0wMG7YiQr05Swun7PdZHCUDitIs9eIORzJlIKn-X2fKKlkR1wWL0J2KDtwVF8LFwYVCyJtEVUzBytaDdGWOK8t5sLx5AK51Tf1FzT_6cVkBLhpI2Ko1cA4FajuaUsN-_n8hbUmN94jDyXCTee6I3cajz0A9quagkqdT6EkosRVW7E13NUl4PEBQTu4FXPyhe3rROBehyEa68EyWLm6cXfDrk6pqT0eIMupj9AtgqtDcnVHMqkMuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RK0okAjjMUqIO0zXiqRag4UuopaOaNtUZu0O2ddKV5I8Utr_IyAVyHaTXE3whZAo-6XoST43QqHtMboGvtXlLxIfbLbrzCN2iG3lqDvPNQXVazi5lqs2U752fi8Rzdo8dXIkc-OAWZqg0hVCqt6IAxJY7iDx7hb64ypY18ldV_UKLy3F3HHX6v5tVmIyVSYWxCPqsCCAvQBMH4WoNzo5EAna1btp2Vd-nm0qGIkC8kCup8V-nAi4GRs5_YpP5_YllkaAeESFZex4FkDzodDPCZNwAc2L0324srdKYU8YEI9Zy3o3w6tzDTw9an_Q84-0zCzMOsI3nFdC9N4ygHxXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oKsfIYL9R7y_mtGpIGZl9fCpHuzPH-L4Z7guD2n4ipn-SM7A4AUeGayG6hrJDRqdBotSNVoBKKo2uVrv-MmlCVP3JHN-RHbp2r2p2RZInAIxYRdO0mNNr7sH4SqRJBEZbAJNBy70G7kLE7bs8YORv6YrJva9WBOlDEPydENgr5-7umXdFg1OnnMD5T7uWvFb6wS4DI6GQQ1Way9W4bTP81kfEPU3jT_L9ObR2_GUpXJXcyWeioxneFjGhizxg8pOqCQPY_epbZJrcewcOkedyi5kc_hI8D-b51EnB1aRGt2Y8iafePb3QAgvwRirKGZuCc8t6EY4d9TJ5vl9Fb-8DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی حدود ساعت ۱۹:۳۰ به همراه تصاویر بالا:
▪️
وحید الان برام پیغام اومده که من جان فدا هستم و ثبت نام کردم ولی خودم در جریان نیستم
😂
▪️
آقا یه اتفاق جالب افتاده. ظاهرا بعد از هک شدن دیتابیس جانفدا دوستان یه فکر بکر به سرشون زده.
من هیچ وقت در این کمپین ثبت نام نکردم ولی پیام زیر رو برام فرستادن. فکر کنم خودشون به صورت پیش فرض همه رو تو این کمپین عضو کردند، حالا هرکی جرات داره انصراف بده… البته نمیدونم انصراف داره یا نه.
▪️
امروز این پیام برای من اومده در شرایطی که من اصلا ثبت‌نام نکردم.
حتی برای پدر خانمم که فوت شده هم اومده.
▪️
امروز عصر واسه من این پیام اومده
در صورتی که من حتی تا حالا سایتشو هم باز نکردم
حالا یا خودشون دارن روی شماره هایی که از یک سایتی یا صنفی داشتن ثبت نام میکنن، یا اینکه یک ادم [...] واسه من فرم پر کرده یا اینکه مسیج الکی فرستادن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75420" target="_blank">📅 20:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XC1scM2TcXPNCUujiWO_05T_p0qI5zxUusTshpQGhYhIK92H4e3q8iD-EAUIBEete1RZKj6_4nb0rtK_c4yYCVPwhXGNUS51GF11Qo3eZg9Teyldt5l30UeUZWVZLd5RartCA_HJYTVcgqVuLZV-I0e0GkBiIh8nG4kFY_fg3fiA1KsGUfRoPkbtU7Kwdm6-wNhmy21pHAh5r8_F9gbWXFcd3c-0iGWR58Np06P1M__A_2Z_UK6QmiQ_UvfbeSPw2PkCYZRF4tVJXgvaO8mBAywGnKwrDmFpaLPK-eetlCiXCS12fotdEveJzL0cIIjlvcyZT8aM4lS6NklE-HhYfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JuOiVH4ZrmRd57ZxHYEp-avGq853BhNRHo2Q1Uudnko_rYGyz5YUP9ShuBJ9UmlbBtEv91Ad26t9CUxk3yIp94uLruzVfE_CP5BtH12KfGyBxZiBbya-C-gHPZ0Kg6K8uOM-MIPlS0hlCRMo5m_9rk3Z_z-duddBufCRpyhUs3iWcsG-C5z37iHiWF7KzLwtiWZqdquy1n6tqZYq0w6XYNRIvZFnqDvitm77b7UKOg7jZ8OPzFdwJIck7KvoYBQkO8ulkPnkyikR6PnQhMa09T_N0lOQPkCFM59IdQqUS_BjpysmZ7v7-ydOlE9HnmbzDqU0UDT63VzWH-oPCfOZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pOMIkbbPoPjxxckdYHcXi8SpTy9mtuyhMyScEu8ovxXWrXdjAe1cM3MFDpCXGzk3XfRmwtvs3UTGxEZzoRw8S8D_jw7buTBKde1osdM963KHaxdyL1s62X9UMOnXunoc2aOBdsmJntRsejTgoJF3DgL97qg8XvdLpMI2Q9AyReup3lSD3ddin8iJWgXT9xpWETvv39l-09G8WdFRn9Le6DjrhPSLX3Jn2L9riHwoWF1zwQ9FJg2JEB1kefRcCdLjglWagLZVbYeLcTOrae0ciiJrCJljgVrszmxjZWjbtFLUl77FkJEyHoioWaHR757_V1kQoyqkksczawHkVLrtIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/okXd4F0cdqA5FLep3XBMRrFgACsBcj6Hqw4vOPFWP-QPV8cfs7fUMbnFVRoFxSrSssT0TiPLKGPPfqlmVOZs0_A5SIdEq_linmRjNHkuGXZj6ip-utmBTyDzsrp8ih9v20zFSYhLiq1F-DyufngpwDmkqKdoW6QVNnCIs1Q8swx6p6VQ2em9ga_JBQ3-7BWE73ne7dMsyk_BDfF0k4jTyxETWR6LbZGX1AFYpsmD8ZHWdLbx79xaRz093hwPivYcURqwPZdf3RI0hmYp_ZbzaAhdtvKpHcpE7oDKlGgbEQB6yuzxNJdBF-bSQDcMquftBsRg8l0oCloR9GxAyH6AZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=XuXBtl_7E9swH1kko9IMNu6w9ATIDCuU5xCl4tg-mQzeMgq_VWZHJIyefx0aE8BkPdXZnJdym1TyoRVKwNLmqRAwMJM2dKNrkrKfF4RvS-3G1ga0wfjjqPWE6uuFCUIch21HyI7_d31_EAahgsIYHqY-BkkwTIt0smZ7GMAGnPy-wYHZl5N8yTJmyWfu7r6mFDbLtf8al40hh7HmLW8pyLe5V_Yiey50fcziaX33VR7Vh44yAFV-Lt17lMYM-2mmSkSuEauQu-rh8uhfpNpxz01fvMs37VsrzQ35bOV6ZddTTfIeG8peDtRlTu8J0SShX6bZDJDA4KlJWo-QuCtFZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=XuXBtl_7E9swH1kko9IMNu6w9ATIDCuU5xCl4tg-mQzeMgq_VWZHJIyefx0aE8BkPdXZnJdym1TyoRVKwNLmqRAwMJM2dKNrkrKfF4RvS-3G1ga0wfjjqPWE6uuFCUIch21HyI7_d31_EAahgsIYHqY-BkkwTIt0smZ7GMAGnPy-wYHZl5N8yTJmyWfu7r6mFDbLtf8al40hh7HmLW8pyLe5V_Yiey50fcziaX33VR7Vh44yAFV-Lt17lMYM-2mmSkSuEauQu-rh8uhfpNpxz01fvMs37VsrzQ35bOV6ZddTTfIeG8peDtRlTu8J0SShX6bZDJDA4KlJWo-QuCtFZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت گفت پاسخ تهران به طرح پیشنهادی صلح آمریکا احمقانه بوده است و او از ادامه جنگ و فشار بر ایران خسته نمی‌شود.
ترامپ در یک برنامه عمومی در کاخ سفید و در پاسخ به پرسش‌های خبرنگاران درباره طولانی شدن مسدودیت تنگه هرمز گفت: «احمق‌ها نمی‌خواستند قبول کنند. فکر می‌کردند من خسته می‌شوم یا حوصله‌ام سر می‌رود یا تحت فشار قرار می‌گیرم اما هیچ فشاری وجود ندارد.  ما به یک پیروزی کامل خواهیم رسید.»
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت، در پاسخ به پرسش خبرنگاران درباره آنچه او تغییر رژیم در ایران خوانده بود گفت: «در ایران میانه‌رو و دیوانه‌ها را دارید. دیوانه‌ها می‌خواهند تا آخر بجنگند.»
رئیس جمهوری آمریکا گفت جنگ خیلی کوتاهی در پیش خواهد بود. ترامپ تاکید کرد که میانه‌روها در جمهوری اسلامی از دیوانه‌ها می‌ترسند.
دونالد ترامپ از پایان هفته سوم جنگ می‌گوید با توجه به کشته شدن دو صف اول رهبران جمهوری اسلامی، تغییر رژیم در ایران پیشاپیش روی داده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد که در حال بررسی دوباره «پروژه آزادی» در تنگه هرمز است، اما هنوز تصمیم نهایی درباره اجرای آن نگرفته است. او گفت هدایت کشتی‌ها توسط آمریکا در تنگه هرمز تنها بخش کوچکی از یک عملیات نظامی بزرگ‌تر خواهد بود.
ترامپ همچنین درباره مذاکرات با جمهوری اسلامی گفت: «حکومت تسلیم خواهد شد.»
او روز یکشنبه نیز اعلام کرده بود از پاسخ تهران به پیشنهاد آمریکا رضایت ندارد و آن را «کاملا غیرقابل قبول» توصیف کرده بود. همزمان صداوسیمای جمهوری اسلامی اعلام کرد پیشنهاد آمریکا رد شده، زیرا به گفته این رسانه، به معنی «تسلیم کامل رژیم ایران» بوده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، به فاکس‌نیوز گفت واشینگتن در حال بررسی ازسرگیری عملیاتی برای بازگشایی تنگه هرمز است.
او افزود واشینگتن فشار بر جمهوری اسلامی را تا زمان دستیابی به توافق ادامه خواهد داد.
ترامپ همچنین گفت هنوز تصمیم نهایی درباره ازسرگیری «پروژه آزادی» را نگرفته است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در گفتگو با سی‌بی‌اس نیوز درباره پاسخ اخیر تهران به پیشنهاد صلح آمریکا گفت جمهوری اسلامی در برنامه هسته‌ای خود امتیازاتی داده، اما این امتیازها «کافی نبوده» و پیشنهاد تهران همچنان «بسیار ضعیف و غیرقابل قبول» است.
@
VahidOOnLine
دونالد ترامپ در واکنش به اظهارات بنیامین نتانیاهو که گفته بود «هیچ‌کس پیش‌بینی کامل و دقیقی» درباره تنگه هرمز نداشت، گفت: «من داشتم. من می‌دانستم آن‌ها تنگه هرمز را بسته‌اند. این تنها سلاحی است که دارند.»
ترامپ افزود آمریکا می‌توانست در چارچوب «پروژه آزادی» این گذرگاه را باز کند و گفت این عملیات می‌تواند از سر گرفته شود و در آن صورت «بسیار شدیدتر» خواهد بود.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده یک روز پس از مخالفت با پاسخ پیشنهادی جمهوری اسلامی به طرح آمریکا برای پایان جنگ، به فاکس نیوز گفت که ایران فنآوری لازم برای بیرون کشیدن ذخایر اورانیوم غنی‌شده مدفون زیر خاک را ندارد.
ترامپ در این گفتگو تاکید کرد که اورانیوم غنی شده ایران آنچنان در اعماق خاک تاسیسات هسته‌ای دفن شده که آمریکا باید آن را خارج کند.
براساس آخرین گزارش‌های آژانس بین‌المللی انرژی اتمی، ایران دست‌کم ۴۶۰ کیلوگرم اورانیوم با غنای ۶۰ درصد دارد که گمان می‌رود در تاسیسات هسته‌ای اصفهان مدفون شده‌اند. این تاسیسات در جنگ ۱۲ روزه و جنگ اخیر اسرائیل و آمریکا بارها بمباران شدند.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده در اظهاراتی گفت: «مردم در [ایران] می‌خواهند به خیابان‌ها بروند. آن‌ها هیچ سلاحی ندارند، هیچ تفنگی ندارند.»
او ادامه داد: «فکر می‌کردیم کردها قرار است سلاح بدهند، اما آن‌ها ما را ناامید کردند. کردها فقط می‌گیرند، می‌گیرند، می‌گیرند. در کنگره هم درباره آن‌ها شهرت خوبی دارند و می‌گویند خیلی سخت می‌جنگند، اما نه، وقتی می‌جنگند که پول بگیرند.»
ترامپ گفت: «من از کردها خیلی ناامید شدم، اما ما برخی سلاح‌ها را با مهمات فرستادیم که قرار بود تحویل داده شود، اما آن‌ها آن را نگه داشتند. من گفتم آن‌ها آن را نگه می‌دارند، اما چه می‌دانم؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75408" target="_blank">📅 20:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ncp6ogYWNun2Fpt3DhpU4QipNT9U2gIxsENy-PkQQbJT-MuVkvOi9cFPObixT2mbklQ5lu9Gz4CtXDkgO69XXUQhQdoBDQenfY20btT4i8NLOLWTE5omLSpuirAlsk4DzQIPu4PWhP-84QpA8RbSgWR2iSlmD6f1YNxuRksDMbBdgAg_kaQ4PCrzUmpV3FNmm44ITuRCRx6tVtc8Rzww9UjVDlWuKz_hnf4rkF_HhBC_B7mHMq7wZCZMynGpS8jBrB4j69kAifRCtfX_FCa1awms5Sh3psYlATAqfZ5mP1dlLt784cMQoVqNxZiuR-5C9i2Op6M00P4PVxfGHW08Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WmkMaAaUR8RNyWMXa8V9WFEYeAr7KGEajCek5TrtBj2f9_GQRQz_ox-VtU6myvISQUiyJwzQpEVF1hII7EU7TK3ilUToBkOHyKIE4KdEtH6VS6lg4f6nWjCqVJam6nH_6lOgY2SgMO4au0yVZSOSSccspauQOKv7a35j04EAZjTrx4esTS7SxhyGNacUYUArX9gOzxGw8iWYVcTcS3JeXSy4Bina28NUd2GqJYPcKsYfMi1wIuRswFfRfkDOuNtqldOQi7hzs6kkkXg8Zb7qNBZvQFbr5AWPhpZUiJ31BqcKDfoLeUFBwlWHx2pczH8zoLBkRomHtC0nql_rxMCqVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">AmirKh1982
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/75406" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قطع اینترنت نه تنها ربطی به تأمین امنیت زیرساخت‌ها ندارد، که «اقدام علیه امنیت ملی» است.
در ۷۲ روز گذشته میلیون‌ها گوشی، کامپیوتر و سرور ایرانی از صدها پچ امنیتی حیاتی محروم ماندند و در معرض انواع نفوذ و هک قرار گرفته‌اند.
در این
#رشتو
بخشی از این آپدیتها را مرور می‌کنم: @
hamedbd_channel
hamedbd
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/75405" target="_blank">📅 18:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI2fT250iZiOAiX-MDRcoRJW4TXMktehfjV6lW4sZW99SKsrQ_cfa28vsfEWg69EyAdkRCww-tnYDnJLekTyQJE6f3otLYTM2vs5V72Tam2ao46M1WSFbDXxuhZjPuyyEBCZ9OYvnJ8r1StQfkS9inbyV57mHWLpzrO1rZm6UtDhKG2XJRDDgIZi2imRCSAT0X-ct_qtRn5_6sQFjXL2JWmaG36xvq-RZ2m5IsS6eZuBEBbvS8fYSI_EXN8BJh_mVIZrXD6gMZNQuWrxiCV4o0P7XpOjA90bWQD12us-mw1C4SnDhyoD-Eh-eVrGTu0S37-36dyVuDDN1l9c3VzzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار روز دوشنبه ۲۱ اردیبهشت‌ماه در بازار آزاد تهران به ۱۸۲ هزار تومان افزایش یافت.
این جهش قیمت کم‌تر از یک روز پس از مخالفت شدید دونالد ترامپ، رئیس جمهوری آمریکا با پاسخ جمهوری اسلامی به طرح پیشنهادی آمریکا برای پایان جنگ روی می‌دهد.
علاوه بر پاسخ منفی ترامپ، بنیامین نتانیاهو هم اعلام کرد که کار اسرائیل با ایران هنوز تمام نشده و ذخایر اورانیوم باید از خاک ایران خارج شود. این اظهار نظرها احتمال برخورد نظامی دوباره را تشدید کرده است.
قیمت هر سکه طلا هم روز دوشنبه در بازار آزاد تهران به ۲۰۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/75404" target="_blank">📅 18:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HaCNIdSwnEAAAbovL6PKyKxP4Mma4sTIGb-_F3yry7SbUFFQqRD_pRg1HSB7EkU6kPwzOD0aQvq6z2guR4yvj0m8rJAUDDhopYTpTyW0YnvMF9LUDGzjcXD2L51n2OwoxFAdpisuZwZjU67BVRdbscQpOXtXcPNRPDThR1-sVkVqts2eHu8KPm2m_a8Rz6M0xebosJwqayAaRtYE5YbikmLlNGoHSYl4Q_lAnoJbSK3MVRwFwcTM4vTDNwG20YfsltopggtdFcqTSfItViRXKHYgifaUO2koFYa9cEe0HrtprLSqXiSfk26XqtcAGCpdVi9AmTuKFfjh1pwJkL786w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fBUIDEnfQVsyhG9XEMtF5rGW1cIKvWKwW5do4YsS_aCifa2ORkJPqaBoYXpYFaKSARvMW2zI9cZtOWTn_0ktSE5uxA6ghWOkFtrXB68nnyQXT24OvqwqKogY5AznpPXycOGKBRwx5DswN1P_tsJwXFMsBn-T8hPpaj-C309qzQQbjPWAi0wC5Vah-JB3mU6QbQySfxNKtzFW6ESLg5NbzYp__d12rpRJEVp9xIl6ujWxgBmBC6beyj_yqb0GX7l7VKsWrij2mZ8M5-9oN1F9EYe311Wx8d6z-ruvryELqbSYgl6GVsolPHXpso_l-4t74P49013teGR9oYYdDSjLqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😋
💩
«محسن محمدی عراقی» معروف به «محسن اراکی»، عضو مجلس خبرگان رهبری، انتخاب «سید مجتبی خامنه‌ای» به عنوان رهبر سوم جمهوری اسلامی را «کاری الهی» توصیف کرد و مدعی شد در روند این انتخاب «دست هدایت امام زمان» را دیده است.
@
VahidHeadline
«ابوالفضل ظهره‌وند»، عضو کمیسیون امنیت ملی مجلس جمهوری اسلامی، مدعی شد حکومت ایران به ظرفیت‌ها و سلاح‌هایی دست پیدا کرده که «بمب اتم» در مقایسه با آن‌ها «ترقه» محسوب می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/75402" target="_blank">📅 18:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dsax45d2YzJwIyoJufc2GEgmd8B7aF7CeyE9Ll_f90vJoXqeAZLzxJKzXtEzzdEqpyx438lZwz5jzmrgIuwJBiN0A8HcpZsE4dZqxnq-QNcXEyW0gMDjrAKeI79JZCp20AOy_lsUR7qL47q40AVYk3Cwv-6zbc13EWahJdmg5m_OTO_l-iJt4wexMfm_TK-h_UqobVRO4p9N_MGVbmMx8khmHUkykkFP4enAxM14sRUyPykh-51_SaEAvCVG3NYon9f-mbulS-X7Epi7i4d_7hpRBu0sMzbWnbfurtSlk1mrHI51ExY2RC3uEipgHtMjcqFA4uTNTNTJPviOY0-2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UYy2QlZlqLZ00T-vttndZpZeHfxwUQhQHKLM-vSlK7AsTrR7F7E7vqTq5qWkYBxr5JgxptkRWWvsS4K-X3kSusvy9LoTiFaJPlr-EvGjuabX3h8Q62fRU5lNJ447SmK1yrhMqAoDlj6GzR68ppnvcPMb73fFVf4-HvWzgXj68KRVX1j-sjF3Ovn_qpbdS30er12iHJTB7rQBnBHhOdweIOKKjLD9P4nMQ4elaGQhjzZ8XdMXXsjHS_iLpb-rehzi566SAWQxBwvyY923tOPKrMUELnCISeggNMoFlBqxy_vdScQCxBdRIuygKtKbILc_2EtZbJsy7kDlVXK56aQD_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نخست‌وزیر بریتانیا تاکید کرد که از جنگ ایران حمایت نمی‌کند و افزود که شهروندان این کشور نگران افزایش قیمت بنزین و تاثیرات اقتصادی آن هستند.
کی‌یر استارمر تاکید کرد کشورهای دیگر می خواستند بریتانیا را جنگ ایران بکشانند اما او هرگز این کار را نخواهد کرد.
@
VahidOOnLine
دولت بریتانیا روز دوشنبه، ۲۱ اردیبهشت، ۱۲ فرد حقیقی و حقوقی مرتبط با حکومت ایران را تحریم کرد.
به گزارش خبرگزاری رویترز، این افراد به «مشارکت در اعمال خصمانه» علیه بریتانیا و چند کشور دیگر متهم شده‌اند.
در بیانیه رسمی دولت بریتانیا، از جمله این اعمال خصمانه به «طراحی حمله و ارائه خدمات مالی به گروه‌هایی که در پی بی‌ثبات کردن بریتانیا و دیگر کشورها هستند» اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/75400" target="_blank">📅 18:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7U_qxR8-Ly8FTliSq2ycB-CRabS3tCh1BEiktyZLlKl6vcIh0mCobw7WsCPO0n-gfWTsPpK1qK3CWw5DwDP7cled0cmoa2ZDaY4WQ8CrK75L6pCum3bnmkJXtYLfDpIWRR9O0UzpH_jDJAkeIuRltWyXnycArfZwphrbM9BWKGe6lXVT4PX2mQvHvCYonpVJw9DbQEt_4WxOxH-sQ1DeGszgRzsGMfXjDnzjPFa4M_L883lStdk5wVQhczSHZnEAUVPtO3ZY3VSjxGehgOkqPvwoFj_Qx-6574OH6vdPggv5jouvuSGF4kyhoMSsE8sGVrTKh8dacQVBy4btPW96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی جعفری، فرمانده قرارگاه «بقیه‌الله» سپاه پاسداران، گفت: «تا زمانی که جنگ در همه جبهه‌ها پایان نیابد، تحریم‌ها برداشته نشود، پول‌های بلوکه‌شده آزاد نشود، خسارت‌های ناشی از جنگ جبران نشود و حق حاکمیت جمهوری اسلامی بر تنگه هرمز به رسمیت شناخته نشود، هیچ مذاکره دیگری در کار نیست.»
او افزود که با این سطح از بی‌اعتمادی به آمریکا، طبیعی است تیم مذاکره‌کننده با هدایت کلیت نظام، شروطی را مشخص کند که همه حقوق مسلم جمهوری اسلامی را تامین کند و این شروط «حداقل انتظارات» ما است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/75399" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a1CV6QrBH12Wpg-pow3QQcpAm-znOfLeQ6B3KxJL5hjofIXj2y9oBmn9k8aOydlkqTuTPnWdnfsTFC3e60xyzZzbaPqk2GhPOKoVnhEOAkzs3wcjDn5WZT3fznxM_Ddr3dvhvwZ2Bw18ZWCAjwJyq_x13wuH5aAlthHlmO3d37W7GTYht4Q3Xi8Ky6Q6LG11LdCw05CyzZXpb1xj3Dc3R7_DoAJo2l41G0o36n5kkcfG8wvzJfWyfP5HJMd2gbnc8IBbv_ee1KmulEmtc-g7pGH-Rz6DxOIJn78ULxg0fF6VCnkWFDlg6yUmc_J-LZ9RBp-P22hr9iWQ3YrXGybHcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RxHS9BR0fobo7PiOsPcLBGWklfiLNXo4I-GgC4ns46_8bovgKOhPBk4sDPhdhuXAT14QKNPnwzFdeX5Voo-F8UT7yiwMTS3BynRc1v2Jt1HluQhALbM0Lb_qyYVFyq91s3rlKM38Bx_6MYikOieo3kLvaPvfPE8hcDwbrH53-32cP8TIucBKiAsKXRaB_goyh5GYeEfwNhJMYeQLjByg6OI26XbrXKIMm34qNH5aoF0kWxCF6u08lT6l7Ar30I6dLQjm1pXhDHnKT2-6Z8xqi2Rf9hJkdS1n9DY9tPCJBBqASgjx_RgpIPEqD2RUnn5qyvjjE2eQc8bJRYtlYIrIpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=kXmsMCQwmMtx5V1sFJObDW4ssEVDyX7RrkdBnGJny1lmUf06VeySpugTnL-PJwkOL1FTNwOa9bUh1IwNaVwAuu-SPT9LWSuMYemgxnzENZwnU3q_0NtlooVRV57_2-hMXwCC7xJX4iP_JB23dwx-K60rG6Ln5yi2nLld4DhknFkXh3ZEW_B-6tWu_MWHK-t6iTnOsxLqj3lFHoBPn7dX3sF8T5THA_4mzXwDrQIt7n9C9sGLFLvvdI1p01bw1OvVxkmHDhhkzazMSj7UuN3Cnu-F3KNXamiO5to7cRyk_gyKhDPGpBgsUP8F0TElI3PeIAtjEbPZd8iwUK3aQHqc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=kXmsMCQwmMtx5V1sFJObDW4ssEVDyX7RrkdBnGJny1lmUf06VeySpugTnL-PJwkOL1FTNwOa9bUh1IwNaVwAuu-SPT9LWSuMYemgxnzENZwnU3q_0NtlooVRV57_2-hMXwCC7xJX4iP_JB23dwx-K60rG6Ln5yi2nLld4DhknFkXh3ZEW_B-6tWu_MWHK-t6iTnOsxLqj3lFHoBPn7dX3sF8T5THA_4mzXwDrQIt7n9C9sGLFLvvdI1p01bw1OvVxkmHDhhkzazMSj7UuN3Cnu-F3KNXamiO5to7cRyk_gyKhDPGpBgsUP8F0TElI3PeIAtjEbPZd8iwUK3aQHqc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نشست خبری روز دوشنبه ۲۱اردیبهشت۱۴۰۵ گفت در شرایط کنونی اولویت تهران «پایان جنگ» است و نه تصمیم‌گیری درباره آینده برنامه هسته‌ای یا ذخایر اورانیوم ایران.
او در بخشی از صحبت‌هایش بدون نام بردن از دولت یا فرد خاصی نیز گفت: «هنوز با کسانی که علیه ما تجاوز مرتکب شدند تسویه حساب نکرده‌ایم.»
بقایی در واکنش به اظهارات «ولادیمیر پوتین» درباره آمادگی روسیه برای انتقال ذخایر اورانیوم ایران گفت: «در مرحله کنونی تمرکز ما بر پایان جنگ است. این که بعدا در مورد موضوع هسته‌ای، مواد غنی شده ایران و مباحث مرتبط با غنی‌سازی چه تصمیمی گرفته شود و چه گزینه‌هایی را مد نظر قرار دهیم، موضوعاتی هستند که وقتی زمانش برسد حتما در موردش صحبت خواهیم کرد.»
او همچنین درباره روابط تهران و پکن گفت جمهوری اسلامی با چین «ارتباط مستمر» دارد و گفت: «چینی‌ها به خوبی از مواضع ما آگاه هستند.» بقایی مدعی شد چین نیز مانند جمهوری اسلامی، اقدامات آمریکا را بخشی از روند «تشدید یک‌جانبه‌گرایی» می‌داند.
سخنگوی وزارت خارجه جمهوری اسلامی در بخش دیگری از سخنانش، آمریکا را «بزرگترین تهدید کننده صلح و امنیت بین‌المللی» توصیف کرد و گفت: «جمهوری اسلامی ایران ثابت کرده قدرت مسوولیت‌پذیری در منطقه است. ما قلدر نیستیم، بلکه قلدر ستیز هستیم.»
اسماعیل بقایی با اشاره به حملات آمریکا و اسراییل علیه جمهوری اسلامی گفت: «حمله به یک کشور، از بین بردن زیرساخت‌های آن، ترور رهبر و شهروندان یک کشور، مصداق عمل مسئولانه نیست؟»
او همچنین در واکنش به انتقادهای «دونالد ترامپ» از طرح پیشنهادی جمهوری اسلامی، از مواضع تهران دفاع کرد و گفت: «ما امتیازی نخواستیم. تنها چیزی که مطالبه کردیم حقوق مشروع ایران است.»
بقایی در واکنش به صحبت‌های رییس جمهوری آمریکا گفت: «قضاوت را به مردم واگذار می‌کنم که آیا مطالبه ایران برای خاتمه جنگ در منطقه، توقف راهزنی دریایی علیه کشتی‌های ایران، آزاد شدن دارایی‌های متعلق به مردم ایران که سال‌هاست به ناحق محبوس شده، زیاده‌خواهانه است؟»
او همچنین گفت: «هر آنچه که ما در طرح پیشنهاد کردیم معقول و سخاوتمندانه بود و برای خیر منطقه و جهان است.»
سخنگوی وزارت خارجه همچنین مدعی شد که این وزارتخانه، از هر تصمیمی که از سوی نهادهای نظامی مانند سپاه پاسداران برای «تنگه هرمز» گرفته شود اطاعت می‌کند.
@
VahidHeadline
گزارش ایسنا:
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/VahidOnline/75396" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLhladzXUQmXELZrQJp_tVQ0uR0YrfPz2foZUUHWH13OdOCsO_FjjF62wkJQhzAM63n2NM6n9HQubmT3-vS0heurnLTa4KLJ3mNFIeWmLQH91JEZTQpWP8VUMfPvWCuCWWN9bmn7iyafo29uENnHxRmOfaA5mTZq770S5Iz1aQn72AjWJZQ2DWell44yoNnKhvNvmHoIt3c16yfAWUngQkpckdC_s_mgmCSL9i7tRZv5hqu7ytoaAgXZsGviCpBhCbXPDmvWRtfeVPGdhjLqf99rH2cDJtX_3y5wnA3dDl0N4glAVB_aadygGMgFwS6-3VaHrByrIpneB_CyORv65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار تصاویر ماهواره‌ای که نشان‌دهنده نشت احتمالی نفت در محدوده‌ای در نزدیکی جزیره خارگ است، سازمان حفاظت محیط زیست ایران می‌گوید: «منشا آلودگی مشاهده‌ شده در اطراف جزیره خارگ ناشی از تخلیه آب توازن آلوده یک نفتکش آسیب‌دیده بوده است.»
این نهاد گفت: «هیچ‌گونه نشت نفت از خطوط لوله، تاسیسات پایانه‌های نفتی و یا سکوهای متعلق به شرکت نفت فلات قاره ایران در جزیره خارگ مشاهده یا گزارش نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/75395" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6eaJtwhMwQQ8w7wJ4iCgORHUaGi-s2Ll1krSdNhFt04U5TWk6mi4yxryS1t7BuofGuFVK8sIEYvMhqvCNrJxSZ4ytYNGZko78AL65hZk0afBDXhis-VzfVV0DISnbeRxBcrdjHsGvjDlnGn5oPcyGfuF9r9xGrGuhOATwRLZxU-zLDVq3AkqAeckFdpeBI9U_TUmb15IKA7LObcTgF9Gal3NYBNiU4uFZnHmqOS9ncu-7bvFcVgg91DRoobue4ErK4dFt0_a337S5CLvAp46NLkJK7WVthqn9w7oMyzYatgVpLMFCwoao8O6r9yJGYsPbA6j5absbL6fR7qMR8Fww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گزارش سی‌ان‌ان از اینترنت طبقاتی؛ «فکر کن با بدبختی وارد اینترنت می‌شوی و می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است»
♦️
سی‌ان‌ان در گزارشی میدانی با اشاره قطع اینترنت و رواج اینترنت طبقاتی در ایران می‌نویسد، قطع اینترنت در ایران اکنون بیش از دو ماه ادامه داشته و طولانی‌ترین اختلال ثبت‌شده تاکنون به‌شمار می‌رود.
برای میلیون‌ها نفری که زندگی و درآمدشان به اینترنت وابسته است، این وضعیت ویرانگر بوده است. فراز، ساکن ۳۸ ساله تهران، به سی‌ان‌ان گفت: «تصور کنید با بیکاری و تورم دیوانه‌کننده دست‌وپنجه نرم می‌کنید و به ترتیبی موفق می‌شوید ۵۰۰ هزار تا یک میلیون تومان جور کنید، فقط برای خرید چند گیگابایت وی‌پی‌ان تا بتوانید وارد اکس یا پلتفرم‌های دیگر شوید، خبرها را ببینید و صدایی داشته باشید.»
او افزود: «بعد وسط همه این استرس و خشم، وقتی بالاخره موفق می‌شوی اکس یا تلگرام را باز کنی، می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است؛ واقعا مثل مشت به سینه آدم می‌ماند.»
متوسط حقوق ماهانه در ایران بین ۲۰ تا ۳۵ میلیون تومان برآورد می‌شود. سی‌ان‌ان می‌نویسد، اینترنت پرو، شکاف عظیم میان فقیر و غنی را عمیق‌تر کرده است.
وب‌سایت «خبرآنلاین» نوشت این طرح «جامعه ایران را به دو طبقه متمایز تقسیم کرده است: نخبگان دیجیتال که از اینترنت سریع و بدون فیلتر برای تجارت، آموزش و ارتباطات بهره‌مندند، و رعایای دیجیتال که در محدودیت شدید، سرعت پایین و هزینه‌های سنگین بازار سیاه وی‌پی‌ان گرفتار شده‌اند.»
قیمت وی‌پی‌ان‌های بازار سیاه به‌شدت افزایش یافته و بر اساس اعلام سازمان «فعالان حقوق بشر در ایران» مستقر در خارج از کشور، قطع اینترنت طی دو ماه گذشته حدود ۱.۸ میلیارد دلار به ایرانیان خسارت زده است؛ رقمی که با برآورد اتاق بازرگانی ایران نیز همخوانی دارد.
روزنامه اطلاعات نوشت: «قطع اینترنت ــ که خود منبع درآمد شمار بسیار زیادی از کسب‌وکارهای مجازی بود ــ وضعیت بحرانی و پیچیده‌ای ایجاد کرده است.»گزارش‌های داخل ایران نشان می‌دهد «اینترنت پرو» از طریق «فهرست سفید» در سطح اپراتورهای مخابراتی و بر پایه «سیم‌کارت‌های سفید» عمل می‌کند؛ یعنی برخی سیم‌کارت‌ها، حساب‌های موبایل یا نهادها از سیستم فیلترینگ کشور مستثنا می‌شوند.
برخلاف وی‌پی‌ان که با رمزگذاری ترافیک اینترنت سانسور را دور می‌زند، «اینترنت پرو» ظاهرا کاربران تاییدشده را از مسیرهایی با محدودیت کمتر عبور می‌دهد. گفته می‌شود دارندگان سیم‌کارت سفید همچنان به اینترنت جهانی کامل دسترسی دارند.
بر اساس گزارش‌ها، هزینه اینترنت پرو برای بسته سالانه ۵۰ گیگابایتی حدود دو میلیون تومان است، علاوه بر هزینه فعال‌سازی ۲.۸ میلیون تومانی و حدود ۴۰ هزار تومان برای هر گیگابایت اضافی. در مقابل، اینترنت عادی ــ که اکنون به‌شدت محدود شده ــ هر گیگابایت حدود ۸ هزار تومان هزینه دارد و همین باعث شده بسیاری ناچار به استفاده از وی‌پی‌ان شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75394" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q0Y5zm7o5ZvTsiPGrk8s57fkwRX-GcDCZwxakBOrmaeCjMZR88MN8rUs_WKMiGZfV2lVjBF3kv-0BrKVm1AJKVQEL0OTvGgoNKgUgVXCeCauQfgL6HFa2UNi75vQx1iIu5oi4oXxc0KUfvyetaWgktQEeh_gTiFOftjbW6_ZrPJ1lcMZvKehFhZDs7_sJMUjldmm2X1MD4OORm8fzIOn5XaUTBmJMarogXflIs2Oc_ORbrkkf8COsmx_BH5tLUUhKXrkXXmqwsSUng9sIFZXFSfonTTYdjOtnzqsx4-guGPh66fIyULIsBmaYUeUxToJta3HqW8pNWB3InoQEnPnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، صبح دوشنبه، ۲۱ اردیبهشت از اجرای حکم اعدام عرفان شکورزاده، زندانی سیاسی، با اتهام «همکاری با سرویس‌های اطلاعاتی آمریکا و اسرائیل» خبر داد.
شکورزاده بهمن‌ماه ۱۴۰۳ از سوی اطلاعات سپاه با اتهام «جاسوسی و همکاری با کشورهای متخاصم» بازداشت و به اعدام محکوم شد و حکم صادر شده علیه او به‌تازگی در دیوان عالی کشور تایید شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75393" target="_blank">📅 09:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kj5v_66fQ-RmQ6sz3za_F1ZCMlTKGJc-AsoEm_PVvQrTBOTuEQ7NlF-zfS7CCs-BmiDTNJqjPqvey5rmZYz2nI_w5EMHRootFaQA2NkGht27nYqxjNvBkahH40TVliopaUcElNwHbQstS3TlYNI3V7wWghQWIabMgtBfy10IaI7mnZwo1LtFUbOuv54-_y9nl_Rr4uhndScCxZjBedOi2sBUXGCWnBmdQiGN044lBuHOpaZV8gJaUXBc4dic3bRXQYSVdeL74MNEPSspQVvE6NEVIXT8gp62O5tCKsMNnzfmuSkfHU2vKRery-3kT1xiwirQrX_BwS1JrhUdgp2E2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dHEGbGv2xzSwOBuMyoBHlA4hNOknQIUQ9tGQ0Ud_t-aNPq-mgNPX9_heHLWhLO8nhFF6LZcQ68AG3Pc_KRW31DixEuRCjg_7uJs_07F0d2ZpMqOiaL3nzFqIu_uhhjYiIMhf1IwEDKbc8-VK1L4ao2O4COuq4aRoorG6TiZCYEoYQGpB12nVw7yHqTI8yH-HXhOLx-gzuQbcFJhGAAREMBR7nRnMRNWQMko6_f3N8K_hoqqJiw84HX3ziRuq2dzn5mqK0DAcKfvuIJq65ry-0LlXggsRlWaXnWb_wK8Qjp0-ba4Gd-W8l60e71cGJIlsiFfM_05mW4onNmwpY9BCWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس
: پرزیدنت ترامپ روز یکشنبه در یک تماس تلفنی کوتاه به آکسیوس گفت که پاسخ ایران به تازه‌ترین پیش‌نویس توافق برای پایان دادن به جنگ را رد خواهد کرد.
ترامپ اندکی پس از این تماس، در پستی در تروث سوشال، پاسخ ایران را «کاملاً غیرقابل قبول!» خواند.
ترامپ به آکسیوس گفت روز یکشنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده و در میان مسائل دیگر، درباره پاسخ ایران نیز گفت‌وگو داشته است.
او درباره نتانیاهو گفت: «تماس بسیار خوبی بود. رابطه خوبی داریم.» اما افزود که مذاکرات ایران «مسئله من است، نه مسئله دیگران.»
ترامپ در این مصاحبه کوتاه روشن نکرد که آیا قصد دارد مذاکرات را ادامه دهد یا احتمالاً گزینه اقدام نظامی را در پیش بگیرد.
سناتور لیندسی گراهام، جمهوری‌خواه از کارولینای جنوبی، در ایکس نوشت که ترامپ اکنون باید اقدام نظامی را در نظر بگیرد؛ موضعی که گراهام در سراسر آتش‌بس یک‌ماهه بارها تکرار کرده است.
او نوشت: «با توجه به حملات مداوم آن‌ها به کشتیرانی بین‌المللی، حملات پیوسته به متحدان ما در خاورمیانه، و اکنون پاسخ کاملاً غیرقابل قبول به پیشنهاد دیپلماتیک آمریکا، به نظر من زمان آن رسیده که تغییر مسیر را در نظر بگیریم.»
گراهام نوشت: «پروژه آزادی پلاس همین حالا خیلی خوب به نظر می‌رسد»؛ اشاره‌ای به عملیات دریایی برای هدایت کشتی‌ها از تنگه هرمز که ترامپ پس از کمتر از ۴۸ ساعت به‌طور ناگهانی آن را متوقف کرد.
@VahidOOnLine
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، روز یکشنبه، ۲۰ اردیبهشت‌ماه، به نقل از «یک منبع مطلع» در واکنش به پیام ترامپ مبنی بر «کاملا غیرقابل قبول» بودن پاسخ تهران به پیشنهاد واشنگتن، نوشت: «همین الان واکنش به اصطلاح رئیس‌جمهور آمریکا را به پاسخ ایران دیدیم. هیچ اهمیتی ندارد؛ کسی در ایران برای خوشایند ترامپ طرح نمی‌نویسد. تیم مذاکره‌کننده فقط برای حق ملت ایران باید طرح بنویسد و وقتی ترامپ از آن راضی نباشد، قاعدتا بهتر است». تسنیم نوشت: «ترامپ کلا واقعیت را دوست ندارد؛ به همین دلیل مدام از ایران شکست می‌خورد».
@VahidOOnLine
خبرگزاری صداوسیما گزارش داد طرح تهران که ترامپ آن را «غیرقابل قبول» خواند، بر ضرورت پرداخت خسارت‌های جنگ توسط آمریکا و حاکمیت جمهوری اسلامی بر تنگه هرمز تاکید دارد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75391" target="_blank">📅 00:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DB93xjXgnQ5VIhugiMTThAfUEvIB9QfiCOWNEE2sVs88loNZxzHSfBM7xJG5ID3PaqvXDlONcciMNgJKnIyM6GWLGLwOYD4P7eVZTDs0p0kUxTjDlDIuuMMNltek9CWA9U1Y-ZqhRxpOl-BTwZAwwX5olKUu861YtSG5krql6bDnGQd8_yp_4w00chbd476vUIaDqmtHhRIIdNit8T9O9FGoxW_hHW98ssXm1vlcIpIYjQMD73bsXgkyX_-AE6C4jcfMMfRujQFepVlIP1TlkfWaNiEPejLtiuC3rBJIiT_g-9PSORqzimCRPrlIDI0q5aFQruQeasm4woidivZ_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ پاسخ جمهوری اسلامی را رد کرد
پست ترامپ، ترجمه ماشین:
همین حالا پاسخ به‌اصطلاح «نمایندگان» ایران را خواندم. از آن خوشم نیامد — کاملاً غیرقابل‌قبول است! از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75390" target="_blank">📅 23:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GG2FIWjLyNAEgU-YbF3PxlgzkXsyCnWNgwujnWvA02PZhooNtmMdsXbA_NVqHhcdGn6xfgqi0iJ_4iqr-EcIaTcjwvfY6eEHtnC3sxjv3drt_H9lh71LaQeuN5xXFl4yUxkmce3-pLd8oj-7qDzEctHG1wySOBkLrLIeQZGdiKWvPQhk6gXWMT0RzvwraoCO_ALTpdBP7BHyzukBqni-t6bBKfLp1Ik5h3N5s2gqh-3_OH_aCYBXMtIMkNMVdsuAx8jdbL_fVIZ8b1AZmqP3qn5hH2w5eorZkNzS_HZVo7ptnc-5pOXLa40PL7Ex5XDnYyaUF7vFTWKL3toNeqEC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال، شامگاه یکشنبه ۲۰ اردیبهشت ماه، به نقل از منابعی آگاه، جزئیاتی از پاسخ ایران به پیشنهاد صلح آمریکا را منتشر کرد.
به گزارش این روزنامه، پاسخ ایران که از طریق پاکستان به‌عنوان میانجی به واشنگتن منتقل شده، همچنان اختلاف‌های مهمی میان دو طرف باقی گذاشته است.
به گفته منابع وال‌استریت ژورنال، تهران حاضر نشده از پیش درباره سرنوشت برنامه هسته‌ای خود و ذخایر اورانیوم با غنای بالا تعهد بدهد.
ایران پیشنهاد کرده مسائل هسته‌ای طی ۳۰ روز آینده مورد مذاکره قرار گیرد.
مقامام‌های ایران همچنین برای رقیق‌سازی بخشی از اورانیوم غنی‌شده و انتقال بخش دیگری از آن به یک کشور ثالث اعلام آمادگی کرده‌اند.
وال‌استریت ژورنال گزارش داد تهران با برچیدن تاسیسات هسته‌ای خود مخالفت کرده، اما در عین حال آمادگی‌اش را برای تعلیق غنی‌سازی اورانیوم اعلام کرده است؛ تعلیقی که به گفته این روزنامه، مدت آن کوتاه‌تر از توقف ۲۰ ساله پیشنهادی آمریکا خواهد بود.
بر اساس این گزارش، ایران در پاسخی چندصفحه‌ای به تازه‌ترین پیشنهاد آمریکا برای پایان دادن به جنگ، خواستار پایان درگیری‌ها و لغو محاصره کشتی‌ها و بنادر ایرانی شده و پیشنهاد داده است تنگه هرمز به‌تدریج به روی رفت‌وآمد تجاری باز شود.
وال‌استریت ژورنال نوشت ایران در مقابل، خواستار تضمین‌هایی شده است که اگر مذاکرات شکست بخورد یا آمریکا در آینده از توافق خارج شود، اورانیوم منتقل‌شده دوباره به ایران بازگردانده شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75389" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ftb0OBvKEo4Y1Ruw2UroXo5__I0pw4RuXReVo9dt11djRQiiBHgKNbiMslA10DpPm2q4K3Q9mzxGxzanozuuGdba-yOhiokfACGocaXCcSEodFJZIaHiTFEVj6TiSJDfnl7ZxVNG6PtmaZAFs2CvC8T6T25HgcnAhp3j1cybIN1p-IMSzGWVVug8F40cHPUorClZWJN7oJMB1FvJg8uxQkRWvpS-C4o_9fx3zBRSRIz7hjnWmfk38AqV4dHdlvsIz5gdHt5jBT2jRRwsks-OZBxEhifmZHOUQKJ0KiztTsAtNGuftRZXftwDPaniJb-wEJxLgxtLSuUMPURPJ-KJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران شامگاه یک‌شنبه با اشاره به شنیده شدن فعالیت پدافند هوایی در اندیمشک و شمال دزفول از سرنگونی «پرنده متخاصم دشمن» در اندیمشک خبر دادند.
شهروندان نیز یک‌شنبه ساعت حدود ۱۰ شب از شنیده‌شدن صدای پدافند در این شهر خبر دادند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75388" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">#دزفول
#اندیمشک
پیام‌های دریافتی از شنیده شدن صدای پدافند:
پیام ساعت ۲۲: دزفول حدود 20 دقیقه صدای پدافند میومد
دزفول وحشتناک صدای پدافند اومد.جدود ساعت نه ونیم
سلام پایگاه چهارم شکاری دزفول از ساعت ۲۱:۳۰ تقریبا یه ریز پدافند فعاله
پدافند پایگاه وحدتی دزفول فعال شده از ساعت ۲۱.۵۰ تا الان ۲۲.۱۷
فعالیت  شدید پدافند در اندیمشک ساعت 22.15
اندیمشک
ساعت 22:19 امشب پدافند فعال شد در حد 30 ثانیه.
یه صدایی میاد انگار پهپاده
سلام، اندیمشک ۲۲:۲۲ دقیقه چند دقیقه ست پدافند ها فعال شدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75387" target="_blank">📅 22:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75386">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNeMcvInIIDJX4N0t4AIqk5tE9guoMgK7Y3jkBzO3H56FCly2Qz7tG7Cl_4KoO_V6Vm9oadod0YoSwsdl3y-yhdeC2-UYlhdvyRZAxbC6loPHyUdBHCNzTHpNHh1SgTl0nPVkYjaGiaJhZ1P0ilS-UJ7X5MLqicAkDwLbdCPXrzaCxarIvYT26DE-YytneIlqSJREHosfyAJOKRdCGyfPsJGUf6pKLSP4VpsVEVi8GFLeQvwA_nvRnSR1jUzojTX3SDiY6seClZf2TfP10WzlGtRxGrBDSRXkzFqzCIJsRCpTpnNgFSOYRZYEal-aVKwRxP9jhPiv5e6LofF-4Rw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: آن‌ها دیگر نخواهند خندید
پست تازه ترامپ پس از آن که جمهوری اسلامی گفت پاسخش را از طریق پاکستان ارسال کرده. ترجمه ماشین:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است؛ «تعویق، تعویق، تعویق!» و سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به گنج رسید. او نه‌تنها با آن‌ها خوب بود، بلکه عالی بود؛ عملاً به طرف آن‌ها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه، بزرگ و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار، و ۱.۷ میلیارد دلار پول نقد سبز، که با هواپیما به تهران منتقل شد، مثل هدیه‌ای روی سینی نقره به آن‌ها داده شد. همه بانک‌ها در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند. آن‌قدر پول بود که وقتی رسید، اراذل ایرانی نمی‌دانستند با آن چه کار کنند. آن‌ها هرگز چنین پولی ندیده بودند و دیگر هم هرگز نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما پایین آورده شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آن‌ها بالاخره بزرگ‌ترین ساده‌لوحِ همه تاریخ را در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی پیدا کردند. او به‌عنوان «رهبر» ما یک فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
ایرانی‌ها ۴۷ سال ما را سر دوانده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای خود کشته‌اند، اعتراضات را نابود کرده‌اند، و اخیراً ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند و به کشور ما که اکنون دوباره بزرگ شده است، خندیده‌اند. دیگر نخواهند خندید!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75386" target="_blank">📅 21:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laORilQGGQHHvN9AVeSoNnnMrrzboCisetMYJGpfBOwgfOwgZBC0wEAc4-urtLARIUlrjSBV3vG9qhZGZReW94ShvL1wn05ridUHYXiZJrsUZtouWlT1hg9d7QyLxl6wuIYrM8WxTmuzl6h9oo3j8ijQTqMUiwF2tqhR_p5rxv4pj1MVyx4DNgsG-m5P5OxUZzBPIJg1AH4rinTnMA6fWvAlGHnBm5QIGU0KhQ3PeMYMfvjfRGfYSnj62LoNf5Ij1cX4BnpSgm0nRilfBZzFz9aH6CAt69Sp4sOG9qfJgHkNxSM9KcXiW3_5s2OW3pFD19-Vxk6VOrMy5suPyWI2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در بخشی از یک مصاحبه که قرار است ساعاتی دیگر مشروح آن پخش شود، گفت که ذخایر اورانیوم غنی‌شده ایران باید از بین برود تا بتوان گفت جنگ آمریکا و اسرائیل با ایران به پایان رسیده است.
او در بخشی از گفت‌وگو با برنامه «۶۰ دقیقه» شبکه سی‌بی‌اس گفت: «این [جنگ] هنوز تمام نشده است، چون مواد هسته‌ای، اورانیوم غنی‌شده، باید از ایران خارج شود. تاسیسات غنی‌سازی هم که وجود دارد باید برچیده شوند.»
او همچنین گفت: «ایران هنوز از نیروهای نیابتی حمایت و موشک‌ بالستیک تولید می‌کند. بخش عمده‌ای از اینها نابود شده‌اند اما کارهایی باقی است.»
آقای نتانیاهو در پاسخ به این پرسش که این اورانیوم چگونه باید خارج شود، گفت: «وارد می‌شوید و آن را خارج می‌کنید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/75385" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75384">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YiZNqB0GJS8BZymMb7zZC19hsq7MqOLp204tpD7m0IwgDt6mWxdpRuwL5SpyBdITI7GZp1mYIaItKyxALVvE9eZ4q2SYWoiRG1SrmPNm8phD8tro4WEMFm-Pb2x7OHZgK-Dvp_uWMSfyRav8R6pcBhCRlnViMPn-Huzq_jeTKXF09Yp0seuCSS5-WmuQon4VpPkkZ1R1FJo76BSbqeIDGb4urQo1TknfIGJ-kYBQ7t24rfrcm9Rb-PVWEupeoaiJc6dSKaWv2CITfsBOuWkfN-_CYzoCtyAnlMfBgfyN3K-yj4-UIctwDKF8XPQWxlZ4Fk0P1qLqOjmopQ9lmTqz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Afkham_minus
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75384" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75383">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8hVYhi6m7dlfXM0TzStxZdFsooIaydelcVTRXYulo770bhm37YgOj-VzfLd9sZpAYKAMzHJKDsW1EJvm15Ajw2s7nBY9A00vlxhROHSb366V0QAJBdsCYYXkRwPUpVn5AGsCjtDFwnqLSvJWF_BLcoXzIQ6-aAsRlrd5oe-gdj7PB85Ar77oRQt59TgdoCtzneLl5lTvtOYuK_8_YgeURTvzB5I1Rxh-OgbBfDpKxRlujyVDhgPbBcWlkV0NDtF6mn23ZhKkFNFPSHdua3Km3mnEDWm6dlIsuTHUyASBD6wVjq6286Q4RzmWqZOR6HxFHz6CX7E_xmohIQige2ryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحیم نادعلی، معاون فرهنگی سپاه «محمد رسول‌الله» تهران گفت: «در جشن بزرگ پیوند آسمانی زوج‌های جان‌فدا، خودروهای جیپ جنگی برای جابه‌جایی عروس و دامادها در نظر گرفته شده که با گل‌آرایی، پرچم جمهوری اسلامی و تصاویر رهبری تزئین شده و زوج‌ها در این خودروها در مراسم حضور خواهند یافت.»
او افزود زوج‌های شرکت‌کننده قرار است با «ماشین‌های عروسی به شکل جیپ نظامی» و «خودروهای نظامی گل‌کاری‌شده» در سطح شهر حضور پیدا کنند تا «فضای شهر را به یک شکل هنری و نظامی» درآورند.
به گفته او، هدف این است که نشان داده شود این «زوج‌های جانفدا» جان خود را «زیر پرچم جمهوری اسلامی تقدیم این نظام خواهند کرد» و «از هیچ چیز نمی‌ترسند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75383" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75378">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IKucoO5tZRxKCdXpA9EZOG7HQivUjGVaHf2IURjbm5gB4qCLKVihUWBL6cBezp99M0F20P6mC19huVtdyA3FivV4_zef-QfBhT9UImNxcu07v02Ho6btUzbIz2FbLH7uPshEdoQCACqcLbq-tmmUo2XR2WG6fPe0H1A07jgbEhbSjGHRYCk7Ub9mlbDQ5yxGj3YLX1iFYyp2K0WGYNM_vSychr9n1qY4fRlbynPtsV_4sVVoZGiPc6I3mvopczatp9LR_OtOGLN04EjD9NtTi85MmcL2wW0DOGNMj63ox3vR61pG_qxRPCoOpKbktQNVPFSzbJAheKXsPIOCXNPmNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wxz0RAurb4LTNkfe6h_BMMMhETFvUQvF5O9N3rN9JIO-3qpL7lJFGcUFtlmUXLlzHhgIe39mVjlQ34KaAieemHZFBOxaPZ0dUu4qBKbhQLGe9qElxk79MDdyfI7YIpmx80ABhjneNW4pUR8WXXy0YANhObZZQCl1hEzh3TvLUHeX6E_bibGsngeJtUCAwxvKluu_bVjpgyvt_W3bySCuFSXlG8RxvXird3meBUDFvA5vznDaRIl6Yl9WiXrIHA0Wyz9suU01MMdt8rClIfLgxqZ9GcUWuR4Pg82DJUi8DePvDOdSesbsBVKFxG_3ex30yHXvtG3R2fQqPYUeZRbWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eHn3B8QAPSiYK4Yjj-yZPNH4YextUs_9QpITdfj3IPEmecLd-HysopvFBboDGDeNcxpLpwNe1mUo9k36Os-FQ6Ck3NLtF_AlqXe91C29-v4_XZlIVUurpAgs-sbkJQKl4OGD2o7uRdj5OhgPwK8i9zpqtR-aKDMu7UHDLsy1y09xzGETn3F5gJGsx_Ol5obi_aTwlvp1HcdsN-CHroOkxOMv2tL0rgWME6QpOra0R1wR-TatDjcxdNH6klw9KSsuGO6xTJccQx_zHTjN9l2YYYR8RYSGBLz9wORcL241oUSDXrG_Zi69jAfoPDLh62i0RcAmBVHVv8fINapBRLE00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VvIINSg63A-2FpGIP_eMqqllhsPT-YGYr0sCP2TQBANGmJ8bjSgWaX-T5AICjqQ3wWQ8zLu8mOLZu4oUZIcKS1bPeQMsi4q75NTk9hLK_fFTx3es3KnrLW87dxHJuF8GBdedFsAPfCKsHUM6J2IGx26Mz-sSPvWtx2dg8kHsmkoo6E9dIjHJ2gkRlbnLxhpungWnaStt2QgLboeZyXD1D6yf4KaEj64F42X7MTjng-qjANERcyTPwV_nSNTSvj9oJWy0f7ZBnQsiLpCIOo8GvZXYG28nlAqwfCWJfr5quEMVW1zYKqq_mFlQw1yBYrcxN8iBe57-Ro1NFZL8CTe1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LfN37Rk5M-taI8LJ98Ne8zzqfc4R-x25NARc2ypzYkVggbt74vCSUH2ucDQiT76ZgqSVSxkHnLRe0Y7sTodHLPaizkXfSjrWRNdnjFUG9A47GTMae3CflRhccVggHb64QyN6XlUksATgWzjY0Z1xt46l-Wlr2JGlsrpUYwDWRw5AKh97S5VDNqptfVIlZkHKD4pvpqBSfe1g1TAHefVvldi8xRPdfOwn-hWK_J8uCApNMn7_PPTmlJVG1zRk_KT0VLBkSFa5oXoN70Ug2Gvwlz0GbJeqYwQHWEyY3-Rg7yVSt3Ec8E-n1QncOWQtcCOM-BR-0WLzPqysHOQeZNFMTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید عملیات نظامی در ایران تمام نشده و ارتش ایالات متحده می‌تواند اهداف دیگری را نیز هدف قرار دهد.
دونالد ترامپ در گفت‌وگویی با شریل اتکیسون، مجری آمریکایی، که هفته گذشته ضبط و روز یکشنبه ۲۰ اردیبهشت پخش شده است، در پاسخ به این سوال که آیا عملیات رزمی در ایران تمام شده است، گفت: «نه، من چنین چیزی نگفتم. من گفتم آن‌ها شکست خورده‌اند، اما این به آن معنا نیست که کارشان تمام شده است. ما می‌توانیم به مدت دو هفته بیشتر هم وارد عمل شویم و تک‌تک اهداف را هدف قرار دهیم.»
او با اشاره به این که در حملات آمریکا و اسرائیل طی جنگ اخیر «احتمالا ۷۰ درصد» اهداف مورد اصابت قرار گرفتند، افزود: «ما اهداف دیگری هم داریم که احتمالاً می‌توانیم به آن‌ها حمله کنیم. اما حتی اگر این کار را نکنیم، سال‌ها طول می‌کشد تا آن‌ها دوباره بازسازی شوند.»
به نظر می‌رسد اظهارات آقای ترامپ پیش از ارسال پاسخ ایران به آخرین پیشنهاد آمریکا برای این توافق انجام شده است. هرچند که او پیشنهادات قبلی ایران را رد کرده بود.
رئیس‌جمهور آمریکا در مصاحبه با شریل اتکیسون همچنین دربارهٔ اورانیوم غنی‌شده ایران که در عمق زمین و در تأسیسات هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون شده‌اند، گفت: «ما در مقطعی آن را به دست خواهیم آورد… ما آنجا را تحت نظارت داریم.»
ترامپ اضافه کرد: «من چیزی به نام نیروی فضایی ایجاد کردم و آن‌ها آنجا را زیر نظر دارند… اگر کسی به آن محل نزدیک شود، ما مطلع خواهیم شد و آن‌ها را نابود خواهیم کرد.»
او بارها اشاره کرده است که توافق با ایران باید شامل تحویل ذخایر اورانیوم غنی‌شده ایران به آمریکا باشد. تهران چنین درخواستی را رد کرده است.
@
VahidHeadline
رئیس‌جمهور آمریکا گفت: «ما نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد، چون آنها دیوانه‌اند. نمی‌توانیم اجازه دسترسی هسته‌ای به آنها بدهیم. اوباما این کار را کرد. اگر من توافق هسته‌ای ایران را لغو نکرده بودم، الان سلاح هسته‌ای را داشتند و الان علیه اسرائیل و خاورمیانه و شاید حتی فراتر از آن استفاده می‌کردند. می‌دانید، آنها در واقع موشک‌هایی دارند که دیدید می‌توانند به اروپا برسند.»
از آقای ترامپ سوال شد آیا این درست که عملیات رزمی علیه ایران تمام شده است.
رئیس‌جمهور آمریکا پاسخ داد:«من این را نگفتم. من گفتم آنها شکست خورده‌اند اما این به این معنا نیست که کارشان تمام شده است. ما می‌توانیم دو هفته دیگر هم وارد عمل شویم و هر هدفی را بزنیم. ما اهداف مشخصی داریم که احتمالاً ۷۰ درصد آن‌ها را زده‌ایم اما اهداف دیگری هم هستند که می‌توانیم بزنیم.»
آقای ترامپ گفت حتی اگر هم این کار را نکنیم، بازسازی سال‌های زیادی برای ایران طول می‌کشد.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با سی‌بی‌اس نیوز درباره اورانیوم غنی‌شده در ایران و جنگ علیه جمهوری اسلامی گفت دونالد ترامپ به او گفته می‌خواهد وارد آنجا شود و به نظر او این اقدام از نظر عملی امکان‌پذیر است. او افزود اگر توافقی حاصل شود و بتوان وارد شد و این برنامه را برچید، این بهترین راه خواهد بود.
نتانیاهو از پاسخ به این پرسش که در صورت عدم توافق چه رخ خواهد داد خودداری کرد و گفت برای این موضوع جدول زمانی تعیین نمی‌کند، اما این ماموریت را بسیار مهم دانست.
IranIntl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75378" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TStqWj1bXTa-3u7_g0nB3k1d7QkW1A-1-6X3j1hXsPF8v_Tw9rkBdRFtcwERV0Xw1GMavzovxPTKv-ny2o_i8T2BNCbS9Z_UaOrPNJ8DlTvPFB-ztgO2I0SL7E2JbXR1EoiQSGclVCB6d31l3RJa40G1fueQnzVF_1mAEjffIDIrIxHGaJiVhg966uttznLv6k7NTkcjyBSDhhnDrBV6gtGlxZcpe6FFcg7tZTuEcE78vqCSJwObI0t6ulMYNoisabQYEd_yLZZpVIARVKuzXCZuL33Qykd2fZYt1wq5vXYPEBnbJbDirRMioGH_g1ak34pmoSTcmy18s_b-M9D0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایرنا، روز یکشنبه ۲۰ اردیبهشت ۱۴۰۵گزارش داد پاسخ تهران به آخرین طرح پیشنهادی ایالات متحده برای رسیدن به توافق بر سر پایان جنگ، برای پاکستان به عنوان میانجی مذاکرات ارسال شده است.
ایرنا بدون اشاره به جزئیات بیشتر نوشت: «بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.»
وب‌سایت اکسیوس و خبرگزاری رویترز، چهارشنبه هفته گذشته گزارش دادند که واشنگتن و تهران به یک «یادداشت تفاهم یک‌صفحه‌ای» برای پایان دادن به جنگ نزدیک شده‌اند.
رویترز نوشته بود در این تفاهم‌نامه حتی به تعلیق فعالیت هسته‌ای ایران یا بازگشایی تنگه هرمز که از سوی سپاه پاسداران بسته شده، اشاره‌ای نشده است.
در مقابل، روزنامه وال‌استریت ژورنال گزارش داده بود که در طرح پیشنهادی آمریکا، تهران باید ثابت کند که به‌دنبال سلاح اتمی نیست، تاسیسات فردو، نطنز و اصفهان را برچیند، فعالیت زیرزمینی هسته‌ای را متوقف کند و همچنین بپذیرد غنی‌سازی را تا ۲۰ سال متوقف کند.
رییس‌جمهور و وزیر خارجه آمریکا روز جمعه گفته بودند جمهوری اسلامی تا پایان همان روز قرار است به پیشنهاد ایالات متحده پاسخ دهد.
@
VahidHeadline
ولی جمهوری اسلامی به جای جمعه، روز بسته شدن بازارها، صبر کرد یکشنبه پاسخ داد که ساعت ۸ شبش به وقت شرق آمریکا بازارهای مالی هفته کاری رو آغاز می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75377" target="_blank">📅 17:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhUSnqLnCUMKqaIDQurMIAmwtt6_g8eL52KzkQoREHY2O-0QT23GArsRFGCpnQ-ZQCHdKHJpGTHUbKij4ssVANg_u8q4WIRI8z0UAGoOGsdtHDvcjAItt0-qKSLiKw7tl-bu72Qv2rnlRC6oiEf20gAicLkJ-B4bYUF0N-5QzMfBufovzRfvy9ijNrL8UR80Iw62FN9KkyHn_SycjxYTxW3MjnVvvanB-U3dMPaGlR_GaaWGHbLRQ_d4lArqIM2srGpB5HEfzJUpwpw8OMZ_4HcNkBXFhQmrp5ZpDH0DMuWpVAkzYV02pVTfsjGY3lIBmahz2mEvjrAjhFa1Ui8PAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع امارات متحده عربی روز یکشنبه ۲۰ اردیبهشت اعلام کرد که سامانه‌های پدافند هوایی این کشور با موفقیت دو پهپاد پرتاب شده از «ایران» را منهدم کردند.
این وزارتخانه تاکید کرده است که از زمان ««شروع حملات آشکار ایران، پدافند هوایی امارات متحده عربی در مجموع ۵۵۱ موشک بالستیک، ۲۹ موشک کروز و ۲۲۶۵ پهپاد را منهدم کرده است.»
وزارت دفاع امارات همچنین گزارش داده است که از زمان شروع حملات آشکار ایران، تعداد کل جانباختگان نظامی به ۳ نفر رسیده و تلفات غیرنظامی هم ۱۰ نفر از ملیت‌های پاکستانی، نپالی، بنگلادشی، فلسطینی، هندی و مصری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75376" target="_blank">📅 17:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0bO3xY3SUL7YDk67Ia1GEv4VibMjwVOMnEx6o5B1yzkoxtUZvn8IwPtepifj4FSL5l7GL-Vs7XESOkFJnHROa_5K9h6JE_Y64iFGccQQQcsWTtTe3NnFGYpUVlPGJGqas9AXI2ZKZJpAk9IBgiJXBTJfZi8h8zOZTLDYsB0_2u2FumQwL6UAY6-030iCwJtO__VvzkBUNcyDrbOEiNQ2dNSJcTKto5ySVrAW9ODjY0D5Yau8q4A7k7e_pz5PPCO7WK7f9R25Z_gxpCeoxHjSbrYL8s8J7FC5GnVROIC0kks9ncU0ETDJ_fpNZMcF0WUJYU8mL10YclRJnpknewxPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی گفته‌اند علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، با مجتبی خامنه‌ای دیدار کرده و گزارشی از آمادگی نیروهای مسلح، از جمله ارتش، سپاه، نیروی انتظامی، نهادهای امنیتی، مرزبانی، وزارت دفاع و بسیج ارائه داده است.
بر اساس این گزارش‌ها، عبداللهی گفته نیروهای مسلح از نظر روحیه رزمی، آمادگی دفاعی و هجومی، طرح‌های راهبردی و تجهیزات لازم برای مقابله با «دشمنان» در سطح بالایی از آمادگی قرار دارند.
این رسانه‌ها همچنین نوشتند مجتبی خامنه‌ای در این دیدار تدابیر تازه‌ای برای ادامه اقدامات و مقابله با دشمنان ابلاغ کرده است. با وجود انتشار متن این خبر، رسانه‌های جمهوری اسلامی تصویری از این دیدار منتشر نکردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/75375" target="_blank">📅 17:46 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2cbPdXrmZlje_-Mf2Hu2IefSadDoXqBul1LO53Hp88I5x7oVJ5npCAK1c0MpqCz12Ca0zsBO2XvaNsbk3PT53Pc6qJvp5LEsFyBIgtoa-INib-PnWcOb5zE5D4HFdUyDFFQKg-K15RAh4vgp9cvm-aOuyQcLsliNn5vYhKsogBi-chAZ2Gw_o9f2ClcxFEGUpyP91e_iOM1FXs7oPJi4Ml6JdvedsWZR47NorVad2oeIR06687Bo9UImgFwMEmKC6ER33pi_82oBAxRtAJlC_6JefvSkHSCQS3Zy_vUr_c6Cwty_XvNh94LLyuQ1cNfL7hjmCKxxHD6jY-wIu7O8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران درباره کشتی باری هدف ‌قرارگرفته شده در نزدیکی سواحل قطر، به نقل از منبعی که نامش را فاش نکرد، گزارش داد این کشتی با پرچم آمریکا تردد می‌کرده و متعلق به ایالات متحده بوده است.
سازمان «عملیات تجارت دریایی بریتانیا» (UKMTO) صبح یکشنبه گزارش داد که یک پرتابه به سمت یک کشتی باری  در ۲۳ مایل دریایی (۳۷ کیلومتری) شمال شرقی دوحه شلیک شده است.
بنا بر این گزارش یک آتش‌سوزی کوچک در این کشتی رخ داده که خاموش شده است و تلفات جانی نیز نداشته است.
این خبر در حالی اعلام شده است که مارکو روبیو، وزیر امور خارجه آمریکا روز شنبه با محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر امور خارجه قطر، در میامی دیدار و گفتگو کرد و شراکت دو کشور را برای بازدارندگی در برابر تهدیدات و تقویت ثبات در خاورمیانه حائز اهمیت خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75374" target="_blank">📅 17:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mghj0WOiT2-2S8AOOLGqSBI433F5TFgImaBmvb_RQtE0Rp7PY00cltQNbza8i6kaMPO_zKWY_5hlOI0Npy8GB708RBRQLnaEuiXfqfEBdRJzsSxRmzXLHikEYu-8bfasMpH8pY6RabRakZQpDza70LZBvyXM-Q_shTIy5IYAa2FwxY4RKkRS3dB4Jr-hMIx1kbdrBFLrXJVR1b3xNXVASNQ4GGIlVIwmI_Q2aN6zNoBy9F_c4WXxQfxM-CFtzBzoHAAPH23F5QNle9TOSmBMptYUDugCklvFRT-q6e5zLN-SUHrSw0QgN2SI2vBJqU1LRZvGt1FRnk6rX_7M2E7bsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
خبرگزاری فارس می‌گوید «یک نفتکش حمل‌کننده گاز طبیعی مایع متعلق به قطر به نام الخریطیات» با «اجازه ایران» از تنگه هرمز عبور کرده است.
بنابر این گزارش، این نفتکش «روز گذشته در دهانهٔ تنگهٔ هرمز دیده شده بود و پس از آن سامانه موقعیت‌یاب خودکار خود را خاموش کرد.»
به گفته فارس، «این نفتکش که مقصدش پاکستان است، نخستین نفتکش غیرمرتبط با ایران است که از نیروی دریایی سپاه اجازه عبور از تنگه هرمز دریافت کرده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/75373" target="_blank">📅 17:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75372">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnYd5kqkfJ4ktt6O9A6QjcAeyUgqwLii5vkMNDbSOxMFuaCVKqttAvUnApXPZi-97mhAFi9WCf3IuatWNQE6uXrPywNhYYx2fgUdFNL6ZKxERGiXGEZ65GXN1l4OC_745oTbvbo_-4lLHBWgrh6UswKOXJwZRmYGFGJnozelUlAykhHCrrMqruDTXFe8H6sgmOQhAd9nw-aXy8TfHqRi3a2g3NBtczIaErqIfKtuqV3iomagdwFTAny-GXunKbV1HEUi-dhiELjf-xd4BJqi7YmbMS61kVa6z-R4Fip_srXtFVrV_g6Jxlkck8g3MN4sPFftH6bRuT3f-JubmWJ1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های داخل ایران روز یک‌شنبه به نقل از مدیرعامل شرکت پایانه‌های نفتی ایران هر گونه آلودگی نفتی ناشی از تأسیسات جزیره خارک را تکذیب کردند.
او گفت: «به محض انتشار این اخبار، گروه‌های متخصص اچ‌اس‌ئی و اداره شیمیایی و آزمایشگاه، همه منطقه را پایش کردند اما حتی کوچک‌ترین موردی یافت نشد.»
خبرگزاری رویترز گزارش داده بود که تصاویر ماهواره‌ای ثبت‌شده در روزهای ۱۶ تا ۱۸ اردیبهشت، لکه‌ای بزرگ را در آب‌های اطراف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، نشان می‌دهد که به گفته کارشناسان با «نشت نفت» سازگار است.
بر اساس این گزارش، لکه‌ای خاکستری و سفیدرنگ در غرب جزیره خارک دیده شده که به گفته یک پژوهشگر «رصدخانه منازعه و محیط زیست»، مساحتی حدود ۴۵ کیلومتر مربع را پوشش می‌دهد.
به گفته عباس اسدروز، «طبق اعلام مرکز بین‌المللی «میمک» به نمایندگی از سازمان بین‌المللی دریانوردی هیچ‌گونه نشتی در زیرساخت‌ها، مخازن ذخیره‌سازی، سیستم‌های اندازه‌گیری، اسکله‌ها، خطوط لوله این منطقه و کشتی‌های در حال بارگیری وجود ندارد.»
اسدروز توضیح نداده است که لکه موجود در تصاویر نشان‌دهنده چه چیزی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75372" target="_blank">📅 17:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSZa9W7rnGmZcx8mhdxVYUemKcAtSi24j6DH5hYDwTHVgjMUc5vARNmaIfCXDFyWwq7tJ9A9Y3VFutkzzqSIbdQw-iBNwUSEMOG1qyRx-VvxhIu8jQaINW6ftqxZifchlSDJgMOcx3Ae8S8DIAK9wwwmBG962MRhakQTajOzjjtD8unLOlnls6mIvSBMbVj8Z__zGT7VlQ62GteWh666qRSJczH6d_0x6ElSczigxjaVmMVAsmq79FcBpgVEa4RQAdJWuta0VfMBx0yQyVr10nHaSu9xAF2xAW3AgpUfXArozX9LhJpHLZ5qaTPfFPIikEd79WMhlQMJHU74s5D80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «وال‌استریت ژورنال»، اسرائیل در اقدامی بی‌سابقه یک پایگاه نظامی مخفی در بیابان‌های عراق ایجاد کرده است تا از این طریق عملیات هوایی گسترده خود علیه ایران را پشتیبانی کند.
این پایگاه که پیش از آغاز درگیری‌ها و با آگاهی ایالات متحده احداث شده، میزبان نیروهای ویژه اسرائیل و یگان‌های امداد و نجات برای خلبانانی بود که ممکن بود در جریان حملات سرنگون شوند.
طبق گفته مقام‌های آگاه، استقرار این مرکز لجستیک در فاصله ۱۶۰۰ کیلومتری از اسرائیل، نقش کلیدی در مدیریت هزاران حمله هوایی تل‌آویو علیه اهداف نظامی رژیم جمهوری اسلامی در خاک ایران طی هفته‌های اخیر ایفا کرده است.
این گزارش فاش می‌کند که مخفیگاه مذکور در اوایل ماه مارس و پس از گزارش یک چوپان محلی درباره تحرکات مشکوک هلیکوپترها، تا آستانه لو رفتن پیش رفت. در پی این گزارش، ارتش عراق نیروهایی را برای بازرسی به منطقه اعزام کرد، اما نیروهای اسرائیلی با اجرای حملات هوایی سنگین علیه سربازان عراقی، مانع از دسترسی آن‌ها به این سایت سری شدند که در نتیجه آن یک سرباز عراقی کشته و دو نفر مجروح شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/75371" target="_blank">📅 01:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m329B-oj6VX-SkwkjuysSS_7HD2HIpfuyr5mgTcvzqNWR_D9Cb8_IgIRrf-J4mkXbS2q4iFNvLpZNVFxjAOMsesuod3K-sZtJhehUjsJ1tVeXvd0og02L4Sg2tchsh9eVYIeLxbBOkiqF21q6ViU7FZmuW263eeQk81p8pMxgidiquPq7O58X8c1_TnZDPL53zHpc3hTdssNuCkt_beKEcd-7Dac5NkzaJbJYstiWK8K_r9sfUbWt4qFxZdwLETnngR8IVDPs4YamKl4AZ2f2zoNKuFBx60DTN2qf1mUgDo7cMc0NONxUBMBZKiCB6fIZvnXZByJarwHCWqSPdAPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SbpjmdFHxzfDBqxhH5y4DrfK-81M1y2-Sut7WM9kYH11BqblZUVtIkRFP2S41Csk0rp_0dPQvodH8HRZhitOVeeZHv0x9d7n2bcrtKog7nniz1e-_pltQSpapP2OqRNjpr6a8-jjLELev70WXeSVONJ55jsJq1k3JguQb0v8X-GJIEyRe8NwoExFFNKMf3znQrm6rSxsgAMKHNGF-AtOIplhNWQd1YPlGl1F0JPtghPm7ky_oWOiBILqTy7OdrEsawVC0tUIGY3QbP83xZbiUGrOGJbKkeQG1todCxqqUW6utXlikMDOXDnjalYm3d9ERZ3HZPhVVqRABWa7HXsLMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر ساختگی دیگری که ترامپ در صفحه‌اش منتشر کرده
:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75369" target="_blank">📅 01:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E94XeEV6swMMXoTT5MgvfcNvNhGgsqXt9la9OK-WTrqi4rTGYtXQ-kPCxPDz97hIfVQTfYSmB1YAqt39Ldbcfd-1MVEaaMShsJGBYOIEKLaAqd0spst0610-lf5tet-4Hf25eyaIx_6gM6Fh48TSTqmwB_y20UXHe06pgaftB8SJZ9F-XWnu1ujPmxOAEi7076LJcvSoEp3R7EhmWjeyn0RkJGlM1Q24ytOLMjmZj6gz_T2NS5mjhfrR9iRBwZMIFpOX5eqojwAwUy2RaMmBWcamnaV0Bpirj62HwYlDKNNWPVIPEh9z5F2cWTb-w6SP-8pLFGMKl5GtQbQ2kcHAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75368" target="_blank">📅 23:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKjaSyoVezWSteCQutCBOs-uxKDlbvOZ7wgY2eKVUACOHEKBdYohco4hzvI3JRsHLonQIi63WKnFqRRz8xiQooZmrQDE9e3LpwfBcOrvYv6-9T9G4z0unZpbmezfYzX2PJPnK2UUoaNCfs-jquLYFDumYOiP16t8gsZkohK1Rt9hKZdQwQyCpHFN3QGyshrhSxgkjvNC0LtnYeOR7FFGefLddQ7F4QVIDlcKexy0ITRC513TALQvR_JTnzvQUPtZDYz0FZreeICEwy6r_Ov1lv636ptjxSKPDYUtATgmqBhmGOmeO49xBcYMooHbPxYl5U7uq5mQeyNgECOTB9Pqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، با اشاره به کابل‌های فیبر نوری عبوری از تنگه هرمز و تهدید به اختلال در اقتصاد دیجیتال جهان در صورت آسیب به این کابل‌ها، خواهان اخذ هزینه از شرکت‌های خارجی و الزام غول‌های فناوری نظیر متا، آمازون و مایکروسافت به فعالیت تحت قوانین جمهوری اسلامی شد.
تسنیم نوشت: «کابل‌های تار نوری زیردریایی عبوری از تنگه هرمز روزانه حامل بیش از ۱۰ تریلیون دلار آمریکا تراکنش مالی (شامل پیام‌های سوئیفت، معاملات بورس و تبادلات ارزی) هستند.»
رسانه وابسته به سپاه در ادامه خواستار «اخذ هزینه مجوز اولیه و تمدید سالانه از شرکت‌های خارجی، الزام غول‌های فناوری (متا، آمازون، مایکروسافت) به فعالیت تحت قوانین جمهوری اسلامی و انحصار تعمیر و نگهداری کابل‌ها از سوی شرکت‌های ایرانی شد.»
فارس، دیگر وابسته به سپاه، نیز در گزارشی نوشت که ده‌ها کابل فیبر نوری زیردریایی که آسیا، اروپا و خاورمیانه را به هم متصل می‌کنند، از گذرگاه تنگه هرمز عبور می‌کنند و تهدید کرد که «هرگونه آسیب به این کابل‌ها می‌تواند اختلالات گسترده‌ای در اینترنت و اقتصاد دیجیتال کشورهای مختلف ایجاد کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75367" target="_blank">📅 23:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZko7cSU1TFQ2QICWCdpVZaQHrJ8eUJh5m83VmzjNtclNsDfTxAS0e_LbGYxZ8sqgL6o5h6f0YVY6ux57UMWi6lnv0aUqf38vrgN9Gb97Mxhpiq5T0NY_K5OWKfSVLWxfpet5wcnRzMlVIbiYUwPQh3HDIM0eaCQzeGM1foglV8LjkZg3G057rpeRPnSzhEPKWXE0g-O1f1benqLBUYhefgFMPCfLR6o2YKAJjxnJ-2Ig7JjATctPmzDe5tAPD9hBQercz7fnXiVtpo_F6Q0I42SkhAM_Ll2l3jeu0oTk9f9FMaqE2OJbBjCCIN0D9qcbPitquyjORdvy_zJD_1CQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، روز شنبه ۱۹ اردیبهشت، ساعتی بعد از برپایی رژهٔ «روز پیروزی» در مسکو، گفت که معتقد است جنگ اوکراین در حال اتمام است.
او بدون اشاره به جزئیات بیشتر دربارهٔ این جنگ به خبرنگاران گفت: «فکر می‌کنم این موضوع در حال پایان یافتن است.»
روزنامه فایننشال تایمز روز پنجشنبه گزارش داده بود که رهبران اتحادیه اروپا در حال آماده‌سازی برای مذاکرات احتمالی هستند. وقتی از پوتین پرسیده شد آیا حاضر است با اروپایی‌ها وارد گفت‌وگو شود، او گفت که گزینه ترجیحی‌اش گرهارد شرودر، صدراعظم پیشین آلمان، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/75366" target="_blank">📅 23:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6d6c074f6.mp4?token=XaRqnfnMsPe5RV2mAzM4GI4AJHLHKdF11IYsIz1ydp3kyo1prTXFYfK-Cf8QYeKAQLpeyqO6qTmhBx-6gmcUF_zOQBSqHHC4krCCqSsP7G2ETuCisBskFKsYsJz9XgX30kQxnxGpaJzv1mPgL1S4XklXFwZWqQBiHqqbmJNOJ99fQaEfOfydm18zMu7xfcJSfVqeesI04bUvzRKA5yvDaAkI8GduWjpbdzoWjsrS6HhcUnE_z0PToexORAnRhdrlhtMfmFpRnqjFd8gKs5EVKfIJLIfKClLIZBL9kcheErRSLOCW3J0c_jtWCHfCK6UESwLRIaNfm9O9uxtnRLgk9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6d6c074f6.mp4?token=XaRqnfnMsPe5RV2mAzM4GI4AJHLHKdF11IYsIz1ydp3kyo1prTXFYfK-Cf8QYeKAQLpeyqO6qTmhBx-6gmcUF_zOQBSqHHC4krCCqSsP7G2ETuCisBskFKsYsJz9XgX30kQxnxGpaJzv1mPgL1S4XklXFwZWqQBiHqqbmJNOJ99fQaEfOfydm18zMu7xfcJSfVqeesI04bUvzRKA5yvDaAkI8GduWjpbdzoWjsrS6HhcUnE_z0PToexORAnRhdrlhtMfmFpRnqjFd8gKs5EVKfIJLIfKClLIZBL9kcheErRSLOCW3J0c_jtWCHfCK6UESwLRIaNfm9O9uxtnRLgk9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از تجمعات شبانه طرفداران جمهوری اسلامی منتشر شده که در آن فرد خواننده می‌گوید زنان «کم حجابی» که در تجمع طرفداری از حکومت شرکت می‌کنند «نور چشم» آن‌ها هستند و ظاهر افراد ملاک نیست.
نظام جمهوری اسلامی پیش از این زنان بدون حجاب اجباری را بازداشت کرده و طی لایحه‌ای به نام «حجاب و عفاف» قصد ابلاغ جریمه‌های و محرومیت‌های سنگین علیه آنان را داشت.
با این حال، در هفته‌های گذشته حکومت سعی کرده با انتشار ویدیوها و مصاحبه‌هایی از تعدادی زن بی‌حجاب در تجمعات حکومتی، پایگاه اجتماعی خود را گسترده نشان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75365" target="_blank">📅 21:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWuoPoGcRa5EDrMnALSqP-iccNryAfgE5rVyc-YVBCU2NtsNSU4X5B60h95qF9lZ87acQpGtZ-HJqm3eeCH_j37kbmPPSHL0uSOAlIfGVPSYSj96FraJnsSBngAgLXesIhTtiQOl9RUzmaAXNyYMEbOthSNqRI-dfIakD9L6FXnPyQXc2e0fn9gxcqqv-2LvJM7U5aO1P5xU3d77ChCwJP2mdgCOZygmIiH2Z4eN-hOYyU6rPsdSCpPoDDTfB_oSnUzc4NwCL3XLGizuhx5q2LvtA5vcHE7ZvpS5cIwsCI8GlhWqGH2RZTHf8T_THS4XPGwaJ5FYK-kyTomW4oNREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های لبنانی روز شنبه اعلام کردند که در حملات هوایی اسرائیل به جنوب لبنان، هشت نفر کشته شده‌اند. همچنین بزرگراهی در جنوب بیروت هدف حمله هوایی قرار گرفت.
این حملات تازه با وجود آتش‌بس سه‌هفته‌ای میان اسرائیل و حزب‌الله، گروه مورد حمایت [جمهوری اسلامی در] ایران، انجام شد؛ آتش‌بسی که تأثیر چندانی در توقف تبادل روزانه آتش، عمدتاً در جنوب لبنان، نداشته است.
حزب‌الله روز شنبه اعلام کرد که در واکنش به ادامه حملات، نیروهای اسرائیلی در شمال این کشور را با پهپاد هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75364" target="_blank">📅 20:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN7zeMB0-2ED7htlaMOsvOQzmj9uUAvmuo7xtDBbluCFWODO3-iiwlF1o-tgHL9CU8dW5p4lHWaED0dpn0tk5V_R5qH3zZWliI-tFioOsmmUShIWZfRb6iRu6b0p7b2Ew4hl9H0iyrKtEShfGOSPhY23MVw6UeUUNHKHS8fiJTQPzcL3KppnE4PQ2d3p542_jhNOOb60tDjneC6Q_cc0Nj-SEkbvsi28azmxNfTmaPcRUp2mpdG9Yqit-_BujAVpGrNwioybHh9ida8NyPwOdD_uE2A9A5eX-VhPQjdBjtrurQ9sVgmYlvB8Fh1gxvaXAsxyTcN2GgmdC-2Q90rojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی آمریکا، سنتکام، روز ۱۹ اردیبهشت ۱۴۰۵ اعلام کرد محاصره دریایی آمریکا علیه جمهوری اسلامی همچنان به‌طور کامل اجرا می‌شود و نیروهای این فرماندهی تاکنون ۵۸ کشتی تجاری را تغییر مسیر داده و چهار شناور را از کار انداخته‌اند تا از ورود یا خروج آن‌ها به بنادر ایران جلوگیری شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75363" target="_blank">📅 19:40 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75358">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CLVoI7KSt4_AiVOu7RksakEwtAnAbB2qjbz4qeUa6_KsUdMi-JN8YFurOCG6RxSxdxg1whFY6zQSTDI__u2SEUlnpy9KNZ0ELex5uEIrodCC10EcC19lFAmr7Obcs_d3OfIOxopNqZP_X4oQk3D356JJKyDcCQszXMiaisIwbI-Zo-DAutc0HGCOACkpng9ZscDeW2VKEki5P2WVr3jnBMeDCteM1pGB3wL1SsD9Ry8icgphRzj-vUJX4AaKkU3XZk93PMd8n0Bfvdjn6UJttTkOM9F-9dTjnSPO4ifvaw79LzXvjElg5nXCdZRo6jHFjv030tdPKb-efpaw7qSdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BMxfy5vn_wFbwjbHWHjnVKwa8V61ehsI5GrKZJ8haGK1H1to3V7TuDjNA3IIHdyFaob6f06-BLv6QRSUEsqN6MKuKSQccSt1akpD6vrtD1UXMnIuAsbItd0aFeDLro-KoCmIiO9CkKs5jlub_sv2f6_JeTrqXp_qI2BOae3SxjpgCi-TkUpAtBzu_v7EFqxzZIImgIscb3p583vxtKOpExgwWIQBIgBgHRnlsjPChNDS6WShAoTIwHsfB4CDaZCRbiffWEumcGnT-smkw1UmgDMTm7xdcMQ-yh6Jw-kL5zlf9kYh9RNe_Uysh1eBnNsb-b-pIet9pC9nRYRNGtgmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FKmZ9uwuOu0HDtKy9G7r8YGwm-7paAwC6SKuowVVvQkPqfNZybWa_rWTGaG10c0OaquONQSB3bbGmbeEEyxOa8obYEq6wEAZ7zVtEsZI28Ds-gVzI-_mcfnTrjnwO2p6TVW1gqCubiyjD3gEEmqSH0PSmYkQ9e5GZvn_sRBMcq0-qsHCOqAMxtKMQZG324q44dUYoIZoiSNT2yw4iDIj52kV6H7wj9FwDncG9qwszZnc6zt9YieIIC-sWQ1sma7oK58jujdRYk0k3o6VNqPE5_RcQy4eUFmUpB230W4tbBQRQGWvVFNbTnzf2tGrVd8e-kNLFFYl9Ja9oyoxzFKPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mk4-x6MPsgwQgjjO0fws0XqC7QHgmZhYIb9pFbTgrxldSQE-fv57-NKLNiOmINf_89qNqmSFdYlGBE19UdN-jziSC23xEydsnmk0a8Nn6I_8JdUXIFBU-LpO-f16A7sauQ73vFTub910OFsSat7Q5MxgnRKpHdHNR5QHpCsrAFoNJnoQiwr6yIU_64RI8ZfOc0IKQcHnEVe1GJslPC-GxJYLD0Tgt3VS6ZKiXHonnWjosZ71yGRNyhnEDFidW-8EJ9kr_ZxpE1orH4HJVAzZdAgwp72TDpg_3P56s8fSWi3mAlz6td7XJczB3Kk8_5jKcf3nibaCjZhcE_z-Qfzh1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tPM7J7YNoqreY80TYGXk3zDQO7FLkxMRZ2_4-wc8QQ9klcf6O8eUOgS5UZDKxZG3m4Edz7kHGNgrxF3SNflvMHHQ85JkWREX0ZfgKgpHKSXIh0Mn2IEEx8q13lCzIqxbQhyOwX1_e_A_XbTSQpthEOTT3mGy3XNrRiQTFq20jps_-XCExXFDC7ZCtDvICNioODIA9zyxbAXbx7lxx-D51jhmi7U4YBSisQeIiD_D7zSxPBZpvP6NUkexBPhK1561xgazEcVDpm63QkamErzf5PehzakdrRYMF9Cu4b0tU6rMhKw2VFrNgFx_IoBUuaD6nE3fAypWtz1gNwiwP8RDag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذشت
‌ عبدالله امیدوار، یکی از دو برادر امیدوار که اولین نزدیک به ۷۰ سال پیش با موتورسیکلت دور جهان را گشتند، در سانتياگو، پايتخت شيلی درگذشت.
عبدالله،  برادر کوچکتر پس از پایان سفرشان به شيلی رفت و در آنجا ازدواج کرد و شرکت فیلم‌سازی در شيلی تاسيس کرد.
عبدالله۲۱ ساله و عیسی ۲۳ ساله،  در سال ۱۹۵۴</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75358" target="_blank">📅 18:51 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7t4NPY0L43fZ52Kaf2k7ApW8jTCtxzbd3oIj7UU2xLj7ub3d5FO4_kFiT7Z3SiC6jMLHZQU9r3I2OddD95QyHLAj0OPxv00KnRtE2Tl9c4sqg1fGrdEEBZ9cxSm2A6ES6J9Aj3EFtS_aRl8a2oIxNCOx2Acya1SfDm_kP3yx6ibeXkwhV_iWNsn_Ebig6Q2ziFct_qf19_FbgcHuAnr9tCAvHnNw5hvCACYVttH9MpilNHnibX-Toq-ZrroZ6uon6WqkX6buLiEHc_y9YaGXad2SihsP6hgm7bm0Fm-bTJRHzBzrCDEN1mCgYYwu5v3-78rMlBWIUln5GPe29wijA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع بریتانیا روز شنبه اعلام کرد که پیش از هرگونه مأموریت بین‌المللی برای کمک به حفاظت از کشتیرانی در تنگه هرمز، یک ناوشکن به خاورمیانه اعزام خواهد کرد.
سخنگوی این وزارتخانه به خبرگزاری فرانسه گفت: «استقرار پیشاپیش ناوشکن «اچ‌ام‌اس دراگون» بخشی از برنامه‌ریزی محتاطانه‌ای است که تضمین می‌کند بریتانیا به‌عنوان بخشی از یک ائتلاف چندملیتی به رهبری مشترک بریتانیا و فرانسه، در زمان مناسب آماده تأمین امنیت تنگه باشد.»
لندن و پاریس چند هفته پیش اعلام کردند که طرح‌های نظامی برای تأمین امنیت تنگه هرمز در حال شکل‌گیری است و در بازگرداندن جریان تجارت از طریق این گذرگاه حیاتی موفق خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75357" target="_blank">📅 18:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75354">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VVgg5cDzK9Yts09InAUGItb0TK0LM2m4ZvWmOPrV496zE7lzqXmxoBdOgeUHprhma1WzRLn145KTycs8HfAoKPyTVeDNNFKL0nS8gSQ9XSLgVXAOPuBUNgR3KxHOZCsAaMmMkfGqUBm315GzcFZH2C98bgiWatOmrzVH1-b0xqVyK3CtqvZOqeb5dguaDIvAS6D3oYoNofGIDhJh7sKeoIPYdSWNHNP3ya-MFoGaIOTsOxBrQwbE9zyvQ0oJmUTNht8AjJZNJSJNhYP7-hjw9tuPBYjkkDGEPBnSjgqGh5BA220SjVxEoOvFbFylPzzmfaciPW1HHKlXQXCw6KO14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sTIDNdN5HwBTVFULvvhhr0IfB8tZpTu4tmGAc5vIlLqYWOCEA71Gz8jKYEnUD7jSFNbL02XjKKRVwiY1uhpq6P6tQxbjkiAefs9EU-D_DjZDfY6EtaJQH21u0ZjvZweZ8Q2Dch4UPw_ns5mKoosoXQQoCG2ieFZDpuSxbooIL1nTtoKBUME5Jik1JtBrtthrcV83rY3Jx291ZIQNk0QWcYPUMZlR9FASzhMx-ExWsNMWioB_sLHuP4qR8rZohm1_gxEYO5Fz8IkhULQ1p44ZdLYgsixg5_R-Lnrm1VgEkAW19akpXL0snXUsuUIJWABJOLxkmLpzS_uaErZ9cuLd0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LBPG3dVvNlzvNe9e4ZiF_CcVu0Gu8mN3sPG5OdCE7ieQ7urfb7XzFzdmBtnqT5YAo3jME8QizWIxTaqroG6HLOfreskqH6IFnrtHkppdqPLMQl338d2tnKI5KV1qN7-j9sNZRiRLlrVrSjw72O3a6aHyrauJhQ3zLxQ0Qk8qAVa4sauh87llOC1YHPPi2bqZcCcC5_o-l56Ai39EJMepeF8Wq9DhbvbifqQamsvRRfbMOLr_Y3PdwcWmboz-jfVumsrRGS5GB6-tmZGSypiVa0P4ncl_a71l3EauhYRbhlN-v-60eeliFrtXvs4LkRN6vlgUEmXkItrMG8w7h-ue4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت کشور بحرین روز شنبه ۱۹ اردیبهشت اعلام کرد که ۴۱ نفر را که به گفته این وزارتخانه با سپاه پاسداران ایران مرتبط بوده‌اند، دستگیر کرده است.
خبرگزاری دولتی بحرین به نقل از این وزارتخانه گزارش داد که مقامات امنیتی گروهی مرتبط با سپاه پاسداران ایران را شناسایی کرده است و افزود که تحقیقات برای شناسایی و برخورد با هر فردی که در این تشکیلات فعالیت داشته ادامه دارد.
@
VahidHeadline
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی، روز شنبه ۱۹ اردیبهشت، با انتشار پیامی در شبکه اجتماعی ایکس کشورهای منطقه از جمله بحرین را تهدید کرد که در صورت همراهی با قطعنامه پیشنهادی آمریکا در شورای امنیت سازمان ملل، با «پیامدهای جدی» مواجه خواهد شد.
عزیزی بحرین را «کشور ذره‌بینی» خواند و نوشت: «به دولت‌هایی همچون کشور ذره‌بینی بحرین که در حال همراهی با قطعنامه آمریکایی هستند، درباره پیامدهای جدی این اقدام هشدار می‌دهیم. درهای تنگه هرمز را برای همیشه به روی خود نبندید!»
قطعنامه مذکور که با حمایت آمریکا و کشورهای حوزه خلیج فارس به شورای امنیت سازمان ملل ارائه شده، از ایران می‌خواهد که ضمن توقف حملات علیه شناورهایی که قصد عبور از تنگه هرمز را دارند، محل دقیق مین‌های کارگذاری شده را اعلام کند و از دریافت هرگونه عوارض عبور از شناورهای عبوری خودداری کند.
@
VahidOOnLine
وزارت خارجه عربستان سعودی در بیانیه‌ای حمایت کامل ریاض را از اقداماتی اعلام کرد که پادشاهی بحرین برای مقابله با آنچه «اقدام‌های صادرشده از سوی ایران» خوانده، اتخاذ کرده است.
در این بیانیه آمده است این اقدام‌ها به گفته مقام‌های سعودی، امنیت ملی بحرین را تحت تاثیر قرار می‌دهد و با هدف بی‌ثبات کردن امنیت و ثبات این کشور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/75354" target="_blank">📅 18:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75353">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddEJboOy1JrtwlSanG-ZkbMDZJSExJ4YJsiMAxXsPdRk27mEe_CvOWgMBuuKEk1ueQJ7K8_TkYvDpGc-j-eZbtOkZ8IN7b0VhwPghyvdM3C5G2FMWdF0Go02NaJZKR_eQ6LpKzo91TN3ozQaOTWevwDaPxiFyyLldv7KNNUhaVtkD_eB6xuzYDblEKIe9FwAWjHRV8bBVF_7DwavyiYFjNGnAjS0sctOSag8xVEXO9xFGtYK2pQsvQkR823DvOcAZgqTLELr9RcvijMu8TiQPwbOp2VwofsOkV5SoS91gEVQ2D6876d0Hwpf_83n-EvixmRZ-TslbitpgzuFqTsHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75353" target="_blank">📅 18:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75348">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sTGrvUvtrUHXW1DT_EsEyBTloj7zNnTCbMskn5kZplZV6IntIHv9QrHYd3tbWcao6REE6byQTCyxA3tMLpWrFWoXOjYA4A5Gncko27rm1jh-DlqnQ9-SI59n4mMIyM566AyV59fBuOsBzgBTcjYhnFRHY5xi7jp-u_3V4-8XYm3-ZIfNyYBkqIus5AlNmaz84o35cLWUj7h-0WkOM9hdLbm8uHBxGvwAuCA_UZ0iK8Dj6dpWtLEVrnsUUcb10b7Y2qvSQWkxESagw1JeGjoV3yzHGFxGvyWl-CC9BhNMteZdJf70igoodgWUw0t-9PH_8ihuEcU8GrjJI9dSrSo4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iJWVRMORRu_1-gPGb94D22GVKXrLN0OECKc8l5VsgNmZ8ih7V0amY25gX9Dnw5CKMwsfWQC_JDYWW_xo4JFbmP2DKXI-CEicTjvmcgA2Umoinn9C6HqgvNItZFKpbJmtUbQKD4Bs_at4xALHp6atkPljEgOO1OdmpwAw5RQ1pfnoJ-ouIEuCnw-De0ews3ru6CmqoaAAeEjDfDdnR9vD5INL5dnwOcSpRvK895lj9_EItgA8M1nQ6E0wtYjPKAR7SVZb-VNQRhy0vzvQLbF52wMIoYRkTWYdrsbZX78Gn8ji99J67zMGFnv3H2Iyz_bO2axLiuXDDEoe8R6tn5P7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J1JaKxUi0PazIo9kkgSM3JnxaQO6JdkDzbJ7gA-dBwlCTBwd0OtUQgwP25QWW8_iegUh1Z51b9cUfPPV32-tuIBkpHFwSfuB5EYmMWuXXxMem6QSUdj5bubDBzKu_TskQruOEZyGb1A7yzl9P6Jg4bZTTDCnJHhYUDtkO1zlZmSI4eYJMO60fvv6Py98o7Zp-iNjMgljTUgtpXr5GHgneNUlwsuwFVmtuHW4Kx0HaeYhztrNkdw5abTtbw3Cp7GAfc1MnWp5_8eQvH_YSCXCLmWVA2H35VZfPrpS5WFPkisvOv0m11KpHee8dYnRDXjcdjMhW_azOwnL7ah8bWBD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ucbDcxf8c9K0bKfbS-WPkt7q0xU6tfLeIx9MOEQjdbACIG8xnz3Srx0S2excRixVyzT6duzsVIbWSuGYftXg5XhyTdCru0-hnGbMwJG2mFs-9EyaT1baZpMWfNSxyt_U_jVODOjSdBBl-Hoz_g1VtplPd6FsbowQX5lP7xX4NdoF-GmuH9dWF7DaLZc4YDA_gGXaipcjsWQc2RChSgI3DksbXMzZGaqUgNHiQHzdQKhuhPeylGJNdAka4RZtpfB8ekqNnATrvXe_vq2BwtUUJ5HDB4WgHRFM0pQyU_hbuKaWram-kL5qp9xApqmzz48P4bAQ2TtklgxZe52RgpopQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZIxlfVVnLPmsLDOPBsnIElAh8gGZTs6zY1niA6Yi1xUKza2eOIMFHduMtV4K8sjtNQlXAxL08Oe4rcwIfCtZA6eO0D1FvCw8tMAsdNmNT-_1ra1g4qgdr8D8CGU4JCaGRt1iRvrIEV7vsGLq7fm7byvr0S6YyPkqmV8B5rXzTFdCqfgDCkmXS7m_IAfg68unbEvgPzjOX0rI4vxByABcUSDRqJaVA0Zg6W532H7mCoA1oOBEx-yb7A69O0yIECYcnEssXT734LeqE-MeXAFI56APzKtSppatNRZ5Hx1rnwEle1FuJGYYrCFFYhlQlIDbcpa6SPZ_UhQDjfJvIm_36w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در آغاز یازدهمین هفته از قطعی سراسری اینترنت بین‌المللی در ایران، یک مقام دولتی هشدار داد که این اقدام حکومت در درازمدت خود به «تهدید امنیتی» برای جمهوری اسلامی بدل خواهد شد.
احسان چیت‌ساز، معاون وزیر ارتباطات در دولت مسعود پزشکیان، گفت: «قطع اینترنت فقط در بازه‌های زمانی کوتاه می‌تواند کمک کند و در بلندمدت تهدید امنیتی است.»
قطعی اینترنت در ایران روز شنبه، ۱۹ اردیبهشت، یازدهمین هفته خود را آغاز کرد، در حالی که مردم عادی در کشور تنها با صرف هزینه‌های گزاف می‌توانند به اینترنت بین‌المللی دسترسی داشته باشند و مقام‌های حکومتی و عده‌ای از حامیان جمهوری اسلامی با مانعی در دسترسی مواجه نیستند.
@
VahidHeadline
معاون وزیر ارتباطات ایران خسارت‌های ناشی از قطع اینترنت برای اقتصاد دیجیتال ایران، در پلتفرم‌های بزرگ را ۵۵ هزار میلیارد تومان اعلام کرد.
او گفته است: «مجموع عدم‌النفع (کاهش درآمد) این حوزه نزدیک به ۱۶/۳۲ هزار میلیارد تومان برآورد می‌شود.»
معاون وزیر ارتباطات ایران همچنین گفته است قطعی اینترنت در حوزه مخابرات و ارتباطات حدود ۶/۴ هزار میلیارد تومان کاهش درآمد مستقیم کسب‌وکارها را در بر داشته است.
آقای چیت‌ساز گفته است: «قطع اینترنت برای کسب‌وکار اقتصاد دیجیتال ممکن است برای چند ساعت قابل تحمل باشد، اما قطع گسترده و سراسری آن عملا یک شوک اقتصادی ایجاد می‌کند.»
یازده هفته از قطع سراسری اینترنت در ایران می‌گذرد.
افشین کلاهی، ازاعضای اتاق بازرگانی ایران، پیش از این گفته بود که خسارت مستقیم قطع اینترنت در ایران ۳۰ تا ۴۰ میلیون دلار در روز است و خسارت مستقیم و غیرمستقیم این محدودیت تا۸۰ میلیون دلار در روز می‌رسد.
@
VahidHeadline
خبرگزاری دولتی ایرنا در گزارشی میدانی از تهران، عملاً تأیید کرده است که قطع اینترنت بخشی از فروشگاه‌های مجازی را از فضای آنلاین بیرون رانده و به خیابان و پیاده‌رو کشانده است.
ایرنا نوشته پررنگ شدن دستفروشی فقط محدود به نقاط مرکزی تهران نیست و از بازار امامزاده حسن در جنوب غرب تهران تا شهرک اندیشه شهریار نیز دیده می‌شود.
به گزارش این خبرگزاری، مدارای شهرداری و «دستور آگاهانه» برای برخورد نکردن با دستفروشان، این روند را آشکارتر کرده و بخش‌هایی از شهر را به ویترین بساط‌گرانی تبدیل کرده است که به‌اجبار از اینستاگرام به خیابان کوچ کرده‌اند.
ایرنا نوشته فروشندگانی که تا چند ماه پیش با صفحه اینستاگرامی، پرداخت آنلاین و ارسال سفارش فعالیت می‌کردند، حالا در نبود اینترنت آزاد و پایدار، ناچار شده‌اند در خیابان بساط کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/75348" target="_blank">📅 18:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75346">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pvMmrYOwcredFoQahZCQ23VU6AZ2a23AJVggJuKVmpCwNrZEVf6drzCE6uZrfo8z347cMM5xJRuqYhSmxr383AWIHuEFuIayrIKxaKGsDAH_fyw9zhtL9UcGbrPT0BUZau0wYLSOLvrBRQ-MXlsrYbic2DIpSIr0mOo67Ct_I_UIJhQNiXAmWmewpm5DMf5RZ8w9fQno75rQuSu5BErzlR3cbergQIywQfMp0J1d0BQnLqPDkkkQjyOAM-X1MLIxjf0PJmYYmY3C4lmm67zvFruvabL3C1WJeaz3DN_7OvAhSf-XWbGqpPPq0B0vrx90TW-KheyolqaPoSm27eB4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AuZUaJkqrL8mI8zaqLY5vli4CZgZKpzypc-lFE6_obfmqrUZU6kKTKdEE1IBHni0w9Zpuy8NNM7-heUGyRrwrJScAKIG4bRDXYJoa0mKgLr7A8y9iWwBjwmewkc7RT_pXKdV8EXJl7wDebtgA30YHeFhPihz134ksMKKUaigce_K9tTQO66zNcI_Z6fICmtQomlcEyZC6P0j6wfB1U-vqCf-X1oK_7_8DaaqwFPsiFleusXVCTzaoQCZShUezi2iscFxj6xHACFvBljnEzs_Ou0B9hlZ54_MbNxymNANmm_mJq5WkipuIlh9SdXqNn1XPhC_u_oCtKyyeVV7oDS0Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه‌ترین داده‌های مرکز آمار ایران نشان می‌دهد قیمت برخی کالاهای اساسی خوراکی در فروردین ۱۴۰۵ نسبت به مدت مشابه سال قبل جهش کم‌سابقه‌ای داشته است.
بنابر این گزارش، روغن جامد با تورم نقطه‌ای ۳۷۵ درصدی، بیشترین افزایش قیمت را در میان اقلام خوراکی ثبت کرده و قیمت آن از حدود ۸۱ هزار تومان در فروردین ۱۴۰۴ به بیش از ۳۸۵ هزار تومان رسیده است. روغن مایع نیز با افزایش ۳۰۸ درصدی، از حدود ۷۴ هزار تومان به بیش از ۳۰۰ هزار تومان رسیده است.
برنج خارجی درجه یک با رشد ۲۰۹ درصدی، مرغ ماشینی با ۱۹۱ درصد، سس مایونز با ۱۹۰ درصد و تخم‌مرغ با ۱۷۰ درصد افزایش قیمت، از دیگر اقلام پرتورم بوده‌اند.
این جهش قیمت‌ها در حالی رخ داده که فعالان کارگری سبد معیشت خانوار کارگری را بیش از ۷۱ میلیون تومان برآورد کرده‌اند، اما حداقل مزد پایه ماهانه کارگران در سال ۱۴۰۵ حدود ۱۶ میلیون و ۶۰۰ هزار تومان است؛ شکافی که نشان می‌دهد حتی درآمد رسمی کارگران فاصله‌ای چندبرابری با هزینه حداقلی زندگی دارد.
@
VahidHeadline
خبرآنلاین در گزارشی نوشته اثر افزایش ۶۰ درصدی حداقل مزد سال ۱۴۰۵ تنها در ۴۵ روز از بین رفته و قدرت خرید کارگران دوباره به سطح پیش از افزایش مزد بازگشته است.
بر اساس این گزارش، حداقل مزد پایه ماهانه امسال ۱۶ میلیون و ۶۲۵ هزار تومان تعیین شد؛ رقمی که در روز تصویب، با دلار ۱۴۳ هزار و ۷۰۰ تومانی حدود ۱۱۶ دلار ارزش داشت. اما با رسیدن دلار به حدود ۱۹۰ هزار تومان در نیمه اردیبهشت، ارزش دلاری مزد به حدود ۸۷.۵ دلار سقوط کرده است.
خبرآنلاین نوشته قدرت خرید مزد بر اساس طلا هم افت کرده؛ حداقل حقوق که در اسفند معادل حدود یک گرم طلای ۱۸ عیار بود، حالا به ۰.۸۱ گرم رسیده است.
این یعنی افزایش اسمی دستمزد، زیر فشار سقوط ریال، تورم و سیاست‌های اقتصادی جمهوری اسلامی عملاً خنثی شده و کارگران دوباره با شکافی عمیق میان درآمد و هزینه زندگی روبه‌رو شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/75346" target="_blank">📅 18:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75345">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS3EE8FBO6I9idYd8RSF89XkChp68tBL-n05LlEwZMOCTD6K8dHOHL7R12aWdYd3ZMOHeaBwDkNKEbuuS6OvoiFXXWw-UbCfHRZFlIn6I7r51lTNcRMsuMYqvpYJtSddVxuNfzvbFS_ytA-wheRvqMMAOQFUH1dkrcmBvVEEsykgI9RFkuaDAqj3QihyuXkxXG32hC_qV5k_MAma125-jbukP4fhEGw55YkhE7QVgbDqM6Br2TmQoXKv0GktWMZC8ZIZKfgTN-2EoO86EwZh--0gGOsWPH8k4NjKDpa00WIO4LudpSED7io-9UgG9lNiC5I4tgE8O0GxFr8b0fQU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جمعه،‌ ۱۸ اردیبهشت، یک خبرنگار در کاخ سفید از دونالد ترامپ درباره نتیجه تحقیقات دولت آمریکا درباره حمله به مدرسه میناب پرسید.
او در پاسخ گفت که این مسئله هم‌چنان در حال بررسی است و نتیجه تحقیقات «به محض آماده شدن» در اختیار خبرنگاران و رسانه‌ها قرار خواهد گرفت.
در جریان حمله به مدرسه‌ای دخترانه و پسرانه در شهر میناب در جنوب کشور که در روز آغازین جنگ مشترک آمریکا و اسرائیل با ایران رخ داد دست‌کم ۱۲۰ دانش‌آموز و ۲۶ معلم کشته شدند.
چند روز پس از حمله، تحقیقات رسانه‌ها نشان داد که این مدرسه که در نزدیکی یک پایگاه دریایی سپاه قرار داشت با موشک‌های آمریکایی هدف قرار گرفته است.
از آن زمان تاکنون هفته‌هاست که پنتاگون اعلام کرده است در حال تحقیق درباره چگونگی رخ دادن این حمله است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75345" target="_blank">📅 18:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQPn-CqwIIqNvCmAPr9M2K2EYgh8GVB-AjAL3S8379Tn2JN22l4jd3_IWNsXf8mHzmfWD3i1diUG9Vb6zFbMegtoFH6LidDdPb_WaBqI3cD4CjrS1JB_BhYCZ5ILEui0VAVCuaa6Rh2x65UDChj0dLKkAFbmVND7WYou_XwrApVmX50fQeaTsqmV5l6dZgPcJx0ubA0FSHYVZUgaaR6QHiJPf3_kh3VIPiiQkTk2kpHPvuEYPQolmAxJQtdIITlRF_jKFpQvjhsLIEKK9_bap62ldnTyg9v8uCvLDRfapMAhL14wtWXhxELOG2zwcoe-YVYCccgdcH6bgikpXDsIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به خبرنگاران درباره چشم‌انداز توافق با جمهوری اسلامی گفت: «اگر همه‌چیز امضا و نهایی نشود، مسیر متفاوتی را در پیش خواهیم گرفت. اگر اتفاقی نیافتد، ممکن است به پروژه آزادی تنگه هرمز بازگردیم، اما آن پروژه آزادی پلاس خواهد بود؛ یعنی پروژه آزادی به‌اضافه موارد دیگر.»
او در پاسخ به پرسش یک خبرنگار مبنی بر اینکه آیا جمهوری اسلامی عمدا روند مذاکرات را به کندی پیش می‌برد، گفت: «به‌زودی خواهیم فهمید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/75344" target="_blank">📅 03:02 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j1X_oh5QIPSc6-FDk8_iRlB03w2utQ-fEj4YSxWd1IBV5Sxi5GxaFhp4yKyrxiFnR3AA3aDLPtLOUrqve8101pdNmroWSSP2Pa1RU6W9Wp8jM2Yu5UCAclcjTxgxSxBfhzMhwnwRcmRBAMT4ZM12dLUvmH2g8yNGDuedBeSV-85NxXLx2nqHQc6TzmIBdoYFgzdXCcyfrxAN1ekidhXoXpciHmvvM0YjmziWaDJtrNZrGJhlEIOKmBrRo2Z3VDCP4kFltgMLaR_bOFRqO-cMXk7C1aHNaMWfvhRhDnaxuci-rXwvxIJ3ESlmBTed3BEjGdOzLQ8aoAfxMQHWgdiXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس گزارش داده که لکه‌ای نفتی ظاهرا از بخش غربی جزیره خارک، پایانه اصلی صادرات نفت خام ایران در خلیج فارس، در حال نشت است.
آمی دنیل، مدیرعامل شرکت اطلاعات دریایی «ویندوارد ای‌آی»، به ای‌پی گفت که از روز سه‌شنبه، معادل حدود ۸۰ هزار بشکه نفت از جزیره خارک نشت کرده است.
@
VahidOOnLine
شبکه خبری فاکس‌نیوز به نقل از کارشناسان می‌گوید این موضوع ممکن است نشانه‌ای از فروپاشی زیرساخت‌های نفتی جمهوری اسلامی باشد که زیر فشار فزاینده ایالات متحده قرار دارد.
به گفته تحلیلگرانی که خبرگزاری رویترز از آن‌ها نقل قول کرده است، این لکه که در تصاویر ماهواره‌ای کوپرنیکوس سنتینل بین چهارشنبه و جمعه دیده می‌شود، منطقه‌ای به وسعت تقریباً ۴۵ کیلومتر مربع از غرب جزیره خارک را پوشانده است.
مقامات آمریکایی بارها گفته‌اند که با محاصره دریایی جمهوری اسلامی، ذخایر نفت در ایران به زودی پر خواهد شد و رژیم ناچار می‌شود که تولید خود را کاهش دهد، امری که می‌تواند آسیب دائمی به میزان برداشت از چاه‌های نفت وارد کند.
حالا، نشت مشکوک نفت در دریا این نظریه را به وجود آورده است که جمهوری اسلامی نفت خود را به دریا می‌ریزد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75342" target="_blank">📅 01:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIsJ8Lo_la6Qs1amD-IVxAvQ2SpIcNxIEry-VK3Cc3TIcvnu8rheydJnzC-tUIxsjXFSfQpyYnEDeBM6PbEp6sZxQRgcQMilpv3mzOT2lUACI0QDiCmf-RyOj4LUwu9sYalNeRE2S33-cIdEv66pryjQ6G4Nx7_M0rpbl92b4Kp-JGRepnm9J43WaZ_7FnzClK1aX2Uo4qNeOhYWJrXK06lA0cJoAnFIsdyj8lQas9nZwc3SM9rAjGZQXgJC0mEjECyrI5H8Ft1kQrn7rXEoXUlV92Mh4CQBLAGNma2uG-z0wWci-BiYVSXhtAvBwHmpNCD1kEVHFVHPeflIMkUM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «واشنگتن‌پست»، معدن‌کاران در میانمار موفق به کشف یک یاقوت سرخ بسیار کمیاب و غول‌پیکر شده‌اند که از نظر وزن، دومین یاقوت بزرگی است که تاکنون در این کشور کشف شده است. این سنگ قیمتی ۱۱ هزار قیراطی (معادل ۲.۲ کیلوگرم) در نزدیکی شهر «موگوک» پیدا شده؛ منطقه‌ای که به دلیل استخراج یاقوت‌های سرخ تیره و باکیفیت که در جهان به «خون کفتری» (Pigeon Blood) شهرت دارند، شناخته می‌شود. اگرچه وزن این سنگ حدود نیمی از رکورد کشف‌شده در سال ۱۹۹۶ است، اما کارشناسان معتقدند به دلیل رنگ سرخ ارغوانی منحصربه‌فرد، شفافیت بالا و کیفیت بازتاب نور، ارزش مادی بسیار بیشتری نسبت به نمونه‌های قبلی دارد.
میانمار تامین‌کننده حدود ۹۰ درصد یاقوت‌های جهان است، اما تجارت این سنگ‌ها همواره با مناقشات سیاسی و حقوق بشری گره خورده است. سنگ‌های قیمتی یکی از منابع اصلی درآمد برای دولت نظامی میانمار و همچنین گروه‌های مسلح قومی به شمار می‌روند که برای خودمختاری می‌جنگند. در همین راستا، سازمان‌های حقوق بشری مانند «گلوبال ویتنس» از جواهرسازان بین‌المللی خواسته‌اند تا خرید سنگ از میانمار را متوقف کنند، چرا که سود حاصل از این صنعت سوخت لازم برای ادامه جنگ‌های داخلی و تقویت قدرت نظامیان را تأمین می‌کند. با وجود تغییرات سیاسی ظاهری در میانمار، ارتش همچنان کنترل بخش‌های کلیدی این معادن را در دست دارد و کشف این یاقوت عظیم در میانه بحران‌های امنیتی، بار دیگر توجه جهانی را به ثروت‌های پنهان در مناطق درگیر جنگ جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75341" target="_blank">📅 01:18 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b37b7b7858.mp4?token=a9B4wj_1JnXpQI1GRthfRLjyhEBvFn6A0TciyOsBRC_kPdUWQD6Dlj4r7nBEznHv91wGz-7fz81OHgwtqoFdqZNerPEeEz9oFC5rgJLa5MfQ4xssJGAh89rAjuN95fVU76R4mWrwlbkGuvWec0ylCImUmHqcyB20bB-xXMJq_ORYaCvygM7yuxLgFvZYngi5g8aKki-pULT92Kge83OcRL2eyFkW2WsXdhdLCkTyA5qrFOIxaWE1_V_k3yVfSYDx_wdOPGM-uKITMNczhj-WvA3DaS7niwEuUmX1wXPAge6HP-iMzzNYrt6-BTq7mf48lDvApP9qqeJbhgjc0nRt5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b37b7b7858.mp4?token=a9B4wj_1JnXpQI1GRthfRLjyhEBvFn6A0TciyOsBRC_kPdUWQD6Dlj4r7nBEznHv91wGz-7fz81OHgwtqoFdqZNerPEeEz9oFC5rgJLa5MfQ4xssJGAh89rAjuN95fVU76R4mWrwlbkGuvWec0ylCImUmHqcyB20bB-xXMJq_ORYaCvygM7yuxLgFvZYngi5g8aKki-pULT92Kge83OcRL2eyFkW2WsXdhdLCkTyA5qrFOIxaWE1_V_k3yVfSYDx_wdOPGM-uKITMNczhj-WvA3DaS7niwEuUmX1wXPAge6HP-iMzzNYrt6-BTq7mf48lDvApP9qqeJbhgjc0nRt5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظاهر حسینی، مسئول دیدارهای دفتر علی خامنه‌ای، در تجمع شبانه حکومتی، گفت که مجتبی خامنه‌ای در جریان بمباران بیت علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، از ناحیه زانو، کمر و پشت گوش آسیب دیده است.
حسینی گفت: «زمانی که در دفتر بودم، در ۳۰ متری ما بمب خورد که شیرازی [رییس دفتر نظامی علی خامنه‌ای] و دوستانشان پرپر شدند. ۷۰، ۸۰ متری ما جایگاه کار علی خامنه‌ای را زدند که آن اتفاق افتاد.»
او افزود: «منزل مجتبی خامنه‌ای را زدند که همسرش کشته شد. مجتبی خامنه‌ای در بین راه که آمد در پله‌ها که برود بالا، موشک آنجا خورد و خانم حداد [همسر مجتبی خامنه‌ای] کشته شد. مجتبی خامنه‌ای در بین راه ضربه موج [انفجار] خورده و روی زمین افتاده است.»
مسئول دیدارهای دفتر رهبر پیشین جمهوری اسلامی، درباره آسیب‌های وارد شده به مجتبی خامنه‌ای گفت: «یک خرده کشکک پایش صدمه دیده و یک خرده کمرش. کمرش در این ایام درست شد و کشکک پایش به زودی خوب می‌شود و در سلامتی کامل است.»
حسینی گفت: «یکی از عزیزان در هفته پیش با او دیدار داشت، آن بحث پیشانی که گفته‌اند بی‌خود است. یک ترک کوچک پشت گوشش خورده که آن هم پشت عمامه است و اصلا مشخص نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75340" target="_blank">📅 01:17 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Asjel_hJguSQ20oPhD1Zmltp4WiQP5uVkSrtxDRQlNctgon4qltr3GbOt7CEUB4wzx5UCAHEPYJ2AA_WLI6JAq65spUe8X31QDsiKcaQGnZXXlI8QcxEEFpAyq3-8kPw8gMkdVr0o0u4gh6HiWP0-BQUb3f5u2UA4rqLOJ51wIajwCmmWm75OFNsBKVgZgdV6CX5DO5-EWs3ZcekSd1wG5FW5s8KB8V6xg-cBXtnk28UMtTR6nSf0nI37djGGYSXseRt9bMHPYVd8zDMY_LKAQqgkpOPhiO0Lu2bkMROSBb-Ou6JiWWKD8UJlP7YwAyGI3SwQ2gZxSc-gPRWNVQRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۱۸ اردیبهشت، اعلام کرد که روسیه و اوکراین بر سر یک آتش‌بس سه روزه که از شنبه آغاز می‌شود و همچنین تبادل متقابل ۲۰۰۰ اسیر (۱۰۰۰ نفر از هر طرف) به توافق رسیده‌اند.
ترامپ در پیامی ابراز امیدواری کرد که این آتش‌بس در روزهای شنبه، یکشنبه و دوشنبه، «آغازی بر پایان این جنگ طولانی، مرگبار و سخت» باشد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75339" target="_blank">📅 22:20 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-7McSySqv0gft7MNjL5ggLl8p-8ILZJBXdv0o3xaI6DEfyNFvV-fQOzOKs2oOPARU94LzH3-xtIgZE8iyXxzlmEBE4qYqcSceiHkvYouwXS1X0zoHvhOo_ycrRh7RkMovl3Bkclz-DFLg1iVPSgL8ijBzOTVNvs_P9B_1Nlv-LTSUAax_5U-7jiEZeBDV83iZ2y4YOm9HNxzGwRNUo0fykktev5iIeFpFLNmUozwDa7829QqKbxLtyf9abDxMd6q_B43eZ1z9nsG8HMEXLLoJ7f0GMeKGyuuA20qCcuSdO-yquV0z-bQBAXdn3KXb_iUxiwDAS14HrnwnZ7Yf2IlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»،رسانه نزدیک به سپاه پاسداران به نقل از یک منبع نظامی نوشته است که  «پس از مدتی تبادل آتش، هم اینک درگیری‌ها متوقف شده و فضا آرام است». او اما در عین حال ادامه داده که «اگر مجددا آمریکایی‌ها قصد ورود به خلیج فارس را داشته باشند و یا برای شناورهای ایرانی مزاحمتی ایجاد کنند، مجدداً پاسخ قاطع دریافت خواهند کرد. بنابراین احتمال ورود مجدد به درگیری‌هایی از این قبیل در این منطقه همچنان وجود دارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75338" target="_blank">📅 21:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NExRFxmiX_aFIHX01VGoUUT37XMux3uoqvnF30FR3JaVJ0m32P8CS90nNaq4TQz2jdcAC-1sJOa4FaudmIEuE2Z2ObJKHX8aaRmL5h4S3JVOn4s2-1Uix6txSc_IVDBOXqp79LvUXy49AU__VdrB31znFTqmNQ9c8b7EuRgMwqEfsXUFh19XPFJMHs2EgDh5MS4e-g1sH4M_mwIMSkbIRyesoUrzm4TPPt2X-1X0gHRpj_1hnTUjzB71WVoYB90GMt59YXliUqubTwmfBYIfroDPfDhrXcbrVEwVqaGxGrV3O8DdOr3VuvGqZBljn5nVkAaF5Vnm7iUuQ11Wy9HQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LjN8qp22X-y2M9wS7JcVcjPpCsU8bIwhwzc9RYsEPrTkS8UOgxOfWSqlVt7oUvDbc_Pp6mnRRPpFd2xnd_syf04co7ifVX4JnNTAS9Aig8__b6lG-rR3Kbms0uhKbZXIQQ7o7QctE3kD3513RRFKXyOiXuWD-YLoRuCkd21jcmPg5o2HBeFZxe80mpDF7hM-2TJteyiEbQNKRgdgXWfxDUhzAUJVjGfl9yQgY0KHXI4Hb-FMDDBzCw0xAM4VPi6k0I0OszZrikX3d3t4Uj1smSz8S2TKGSmDHfO0GfPTh2MjDxFdi7gGHZeCZuUfbpJrRZLg3YBeM0mRnX67ALjhwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که در راستای اجرای محاصره دریایی ایران، نیروهای آمریکایی طی دو عملیات جداگانه، سه نفتکش با پرچم ایران را که قصد ورود به بنادر این کشور در دریای عمان را داشتند، از کار انداخته‌اند.
در آخرین اقدام در تاریخ ۱۸ اردیبهشت، یک جنگنده F/A-18 سوپر هورنت برخاسته از ناو هواپیمابر «جورج اچ.دبلیو. بوش»، با شلیک مهمات دقیق به دودکش نفتکش‌های «سی استار ۳» (Sea Star III) و «سودا» (Sevda)، آن‌ها را از کار انداخت و مانع ورود این کشتی‌های خالی از بار به بنادر ایران شد. همچنین در ۱۶ اردیبهشت، جنگنده‌ای از ناو «آبراهام لینکلن» با شلیک توپ ۲۰ میلی‌متری، سکان نفتکش «حسنا» (Hasna) را هدف قرار داد و آن را متوقف کرد.
دریادار برد کوپر، فرمانده سنتکام، با تاکید بر پایبندی نیروهای آمریکایی به اجرای کامل محاصره، اعلام کرد که این سه شناور دیگر به سمت ایران در حرکت نیستند. طبق بیانیه سنتکام، تاکنون چندین کشتی تجاری توسط نیروهای آمریکایی از کار افتاده و بیش از ۵۰ فروند دیگر نیز تغییر مسیر داده شده‌اند.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران، روز جمعه ۱۸ اردیبهشت از وقوع «درگیری‌های پراکنده» میان نیروهای مسلح جمهوری اسلامی و آمریکا در محدوده تنگه هرمز خبر داد.
فاکس‌نیوز به نقل از یک مقام آمریکایی، اعلام کرد که این درگیری‌ها ناشی از اقدام آمریکا برای مقابله با حرکت یک نفتکش متعلق به ایران بوده است. بر اساس این گزارش، نفتکش مذکور قصد شکستن محاصره را داشته که با مقابله شناورهای آمریکایی مواجه شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75336" target="_blank">📅 19:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FapVXyl2Brf-OdHh3ELZtSjn9elLj43kyhhlW30VTx9nXSdtaBgSJkSgo2fJwTYm3Qbc-rGZnqLy3fDGW75jnkeY95vpff47fNDNTP7yvBZbSrwO8Kr4VBk2q5U0l4da4SU2YUUK7tJLtRiJvTMhMht6WJrm86wtEx7cvsIGHf0ofAWlVw_c-pvVKnoyCIZO86revtWKyTVkd16caqqdZIYTpaujCf_6RahsW5WJ8MCeEaIM-3aCCIpRWOUk5FxqfzEODXfvb7Hmt-g6sxi-P0SZOYWjurXChioDK7lbiBy1lg9H70d-zU-YNIPvWTDIXpmc-vl3N3M9nfKTeyHqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روح‌الله مومن‌نسب، دبیر ستاد امر به معروف تهران نوشت نمی‌شود نیروهای مسلح، مرزهای ما و تنگه هرمز را به روی دشمنان ببندند اما دولت فضای مجازی را در اختیار آنان قرار دهد.
او افزود که «فضای مجازی به هیچ وجه نباید به حالت قبل برگردد؛ همان‌طور که امام شهید ما به حالت قبل برنمی‌گردد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75335" target="_blank">📅 19:23 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eVt0cOqVjbvVnax-9Z9aqea-xy6-IeY_jtv6xFnPpNUASKww54OQZFoZcuqEJdXRnmQz8RVy35LSkaiMbUMS6aoJlSoII0yf7zkS1-BtZQsYpV1zTsdTRkXP4o4e5JeU4dbaRGtDuYrWdHR3fa58E5z21k8sW0vl7Jfxk2H6l1cjjRbKf1rsOykP5Nxo_p-bzwrlLvZHQ6lbJz-01WjPGeXnbleHrhOfxDIwKfG1O7yASSZ9GHPc1pdvbKOBmgiW86IzfLzKySy7eFO4uTrqUMbl8y5GuAYpFpbNDVPMY9FuIPVC00nb8sDw31pH_eYCHxSgN8pkjt6UOrPG8vaTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در حساب تروث سوشال خود با انتشار تصویری شبیه‌سازی‌شده از انهدام یک پهپاد ایرانی توسط سلاح لیزری نیروی دریایی آمریکا، سرنگونی پهپادهای جمهوری اسلامی را به «پروانه‌ای که به سمت قبرش سقوط می‌کند»، تشبیه کرد.
او در واکنش به درگیری‌های شبانه ناوشکن‌ها در تنگه هرمز، این تبادل آتش را تنها یک «سیلی از روی محبت» (Love tap) خواند و تاکید کرد که آتش‌بس شکننده منطقه همچنان برقرار است.
سلاحی که ترامپ به آن اشاره می‌کند،سامانه لیزری ضد پهپاد «لوکاست» (LOCUST) است که پیش‌تر اعلام شد بر روی ناو هواپیمابر «یواس‌اس جورج اچ.دبلیو. بوش» نصب و آزمایش شده است.
به گزارش وب‌سایت «وار زون»، این نخستین بار است که یک سلاح انرژی هدایت‌شده روی یک ناو هواپیمابر کلاس نیمیتز نصب می‌شود.
مقامات عالی‌رتبه نیروی دریایی اعلام کرده‌اند که هدف نهایی آن‌ها، تبدیل این سلاح‌های پیشرفته به گزینه اصلی مقابله با تهدیدات نزدیک در آب‌های بین‌المللی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75334" target="_blank">📅 19:22 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_JV7633DIubZIzoJQfXKUU1rqAZ0zl3aqJyWrro-4_1PPGO9WOZ75HVwrFXTuYiiI2hLLYTq0JDGhRS9rAPaNEnZQe2PSQONAOVKXMAUgN5LlFs73HqDDC3lo_v9WzX9Nxf0uRXvTErMG7LmLyjRHMSIUZIfqLyN64Q1yekNTHpfBZGdWK_CrOPlKCMffjsWDJNjO520UfZs4OMO220LvwOVKcz7FgLamqdZvIRYO8NjprUYIjPV4LiN9ns8OS7Su1ORJvpWO1hFvTdUnf7SEMuHWkLkhsP__pupcVYpk8AuvUtBb8Hb08LKpSQ828RSbRczdhkeXMQNkDhhds84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار میناب: حمله آمریکا به یک لنج باری یک کشته و چهار مفقود بر جا گذاشته است
فرماندار میناب می‌گوید که در حملات دیشب آمریکا یک لنج باری هدف قرار گرفته است که منجر به کشته شدن یک ملوان و مفقود شدن چهار نفر دیگر شده است. [گویا قبلا گفته بودند پنج مفقود داشته بعدا جسد یکیشون پیدا شد]
به گفته محمد رادمهر، ۱۰ ملوان دیگر این لنج هم مجروح و به بیمارستان منتقل شدند.
به گفته آقای رادمهر این حمله در نزدیکی آب‌های شهرستان میناب رخ داده است.
عملیات جستجو برای یافتن سایر مفقود‌شدگان ادامه دارد.
دیشب نیروهای ایرانی و آمریکایی در آب‌های جنوبی ایران تبادل آتش کردند، هرچند دونالد ترامپ می‌گوید که آتش‌بس همچنان برقرار است.
آمریکا می‌گوید که نیروهایش «بی‌مقدمه» هدف حمله موشک‌ها، پهپادها و قایق‌های تندرو ایران قرار گرفتند و ایران می‌گوید که حملاتش تلافی‌جویانه و در پاسخ به حمله آمریکا به یک نفتکش ایرانی و یک کشتی دیگر در منطقه تنگه هرمز بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75333" target="_blank">📅 19:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75328">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S0NKiLyY20kdBSZluQwG0ewAeqRClOz84AyoXoiekpWcfxoUIsOjDMc8_crm3qD7QVrTq46vaqf5fUWzOJP8VehYJICiP8Khb-B_yIHcfv5KgnnODUSXvv_otbKnAQ-BBh5ZdaNRLDFdcVDdC83IJAkuJ7sqxmWXvZCuVPBT5IsVArl2WuLnsEC5rorycS6LXGlo7jOHqMP0lTts72l-q7Qfbw1kr5EF5H_TWk65rgZUp5oNxZzhCYXjAYevSGBe9L9Qt02VTXfH4Xt-3VTX_0uePDJujOkzbP4S4hS-lBkeOgF9g6KldUnRPsbI4UdEon-ONDwwoIsZ8vQ3kKd5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N_BU6fQ5Qn8V337gNbip75xiys7BgE83kIku9CDCC1_24-ca-EJzaUkKOdZYLujSaTiAoxSHY2HIS-ubvvAHN3VZZGAj2hDQoyMlbbSGxWsa8kMf37wzuR1AlOvMlokxT2pNVcJPFrd5BYtR0PHhPOgnC7mSTgnItl1ma-Mb-fFPeG_YnfRmO-2h6xHyz3Dl3GzI44YP7xVEO6ZDsLNbIklLfbQ52oDs-3e9AGJbYE45qrqg12FhiGqTeXQeoxZWliBF1wQB-_8N3_zMC_JPpzZhUgeVmOqkByXSYWDnjp2V_vLwVDvQizpb2prY5Vrv5cbZzN7o1FQt7aAZ0LwDtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OzCyTs3Wy_9yegLIYVPiFbIEBn5N8qmTke6gvCPLO2igsjpEr2LCY43t9WiIC1CIYFxvlTbQvOV9rSP0pLCwMLsJ70gPYAYZrVOmqjvqPnpANJxoJXlNdOGpVpzb939h_JpkhXlu10o74aaAof5O_S1nJddNuC2f5PVwQKRhbIZSDiliIBEMuU54_PG7FbvqeSY-2Xx1JT9mUL5Y4LmYMsLvZCSMd1dW0jocVLWRz85MLhS6kNuoNG06L4Z69-Kd7-UmrklGYiEw6EARA2LnzqVsxblWx48eoWedpUGMtatY5cKxNFF5sszfBzfiW68k1088TjHTLzjzayIS2yd2iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/858d7055f6.mp4?token=sp5bZ0YG9m2bNliLc5CGW8ZF4HYHE208DkchpDm2vWiEbYAVa5UXMa5EdYmXw2llnPbAXBh8smGqzJZfl48NPPH01GvhDittAYIV4qUSBQqnSFVU9V7yX9SutyCXQ6LsyoCDdkQztuSOoO4ptoHbeQP7ikQlvEnv-TROXIDcwNBNDj3kuvmD8jgAys8R0-v_sYEc9_uWbBQqEUUSbbTTxZzciCi2dgb-RSqDjQuUTW6FkEvbDLQJW2vBuq3NRJ02syn0NzvvWn9Jv6XJfoSaGOgT--8Q-6aRKG-KE6YyPG4KCCEhpeC8PHR4Ur4mhGi1bnRYUEX34iagY1KjbYtIcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/858d7055f6.mp4?token=sp5bZ0YG9m2bNliLc5CGW8ZF4HYHE208DkchpDm2vWiEbYAVa5UXMa5EdYmXw2llnPbAXBh8smGqzJZfl48NPPH01GvhDittAYIV4qUSBQqnSFVU9V7yX9SutyCXQ6LsyoCDdkQztuSOoO4ptoHbeQP7ikQlvEnv-TROXIDcwNBNDj3kuvmD8jgAys8R0-v_sYEc9_uWbBQqEUUSbbTTxZzciCi2dgb-RSqDjQuUTW6FkEvbDLQJW2vBuq3NRJ02syn0NzvvWn9Jv6XJfoSaGOgT--8Q-6aRKG-KE6YyPG4KCCEhpeC8PHR4Ur4mhGi1bnRYUEX34iagY1KjbYtIcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، گفت اقدام نظامی آمریکا علیه ایران در بامداد جمعه «جدا و متمایز» از عملیات «خشم حماسی» بوده و ایالات متحده همچنان به‌صورت «دفاعی» واکنش نشان خواهد داد.
روبیو روز جمعه در شهر رم، پایتخت ایتالیا، در جمع خبرنگاران اعلام کرد «خشم حماسی» که او اوایل این هفته گفته بود به پایان رسیده است، «یک عملیات تهاجمی بود که برای نابودی سکوهای پرتاب موشک، نیروی دریایی و نیروی هوایی آن‌ها طراحی شده بود.»
او افزود آنچه ساعاتی پیش رخ داد «ناوشکن‌های آمریکایی بودند که در آب‌های بین‌المللی در حال حرکت بودند و از سوی ایرانی‌ها به آن‌ها شلیک شد، و آمریکا برای حفاظت از خود به‌صورت دفاعی پاسخ داد.»
دیپلمات ارشد آمریکا گفت: «فقط کشورهای احمق وقتی به آن‌ها شلیک می‌شود، پاسخ نمی‌دهند. و ما کشور احمقی نیستیم.»
وقتی از روبیو پرسیده شد که آیا آمریکا خطوط قرمزی را به ایران منتقل کرده است یا نه، پاسخ داد: «خط قرمز روشن است: اگر آمریکایی‌ها را تهدید کنند، نابود خواهند شد.»
وزیر خارجه آمریکا همچنین خبر داد که واشینگتن انتظار دارد روز جمعه پاسخ ایران به پیشنهاد واشینگتن برای پایان دادن به جنگ را دریافت کند.
روبیو در این زمینه توضیح داد: «خواهیم دید که این پاسخ شامل چه چیزهایی است. امید ما این است که چیزی باشد که بتواند ما را وارد یک روند جدی مذاکره کند.»
او همچنین تلاش‌های ایران برای کنترل تنگه هرمز را محکوم کرد و گفت: «ایران اکنون ادعا می‌کند که مالک این آبراه بین‌المللی است و حق کنترل آن را دارد... این اقدامی غیرقابل قبول است که آن‌ها تلاش دارند آن را عادی جلوه دهند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/75328" target="_blank">📅 19:18 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75327">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMAYOCmb3KBH2qPG-r6WqR0l9RiMOWjsLI1l-qTvak10uMjXAuTu5Dy3oj29EIz4LxUMv1fdB9TsTaswYsf0jZhsGP_nmyAMkl8K32mZZz4W3wn9oileGny7hWZ0b4wUUbrBmL60tf64r8RQEebyX-U6hrfkt2i8_SgL_4wmzNAukMTjzla6Fumw7mrAu3MynxuzSYu9IPNPbnUlhaEJwiwwUQ-9K6LpcjB4HZQTHLWQxkGugcuPUnHyK_UjqPtkOoDFd2T6FatUHRMXNPxvXiFxwCVttRgQBg-PXTHA38UKF0RWQTsF209vJtumSyOvA0ccvLa4cz5C3Rp1tjB59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی، آمریکا را متهم کرد که با «ماجراجویی نظامی بی‌خردانه» دیپلماسی «قربانی» می‌کند.
عباس عراقچی در پستی در شبکه اجتماعی ایکس نوشت: «هر زمان که یک راه‌ حل دیپلماتیک روی میز قرار می گیرد، ایالات متحده به‌ یک ماجراجویی نظامی بی‌خردانه رو می‌آورد.»
آقای عراقچی در ادامه می‌نویسد که دلیل این اقدام چه «صرفاً یک تاکتیک کور برای اعمال فشار» باشد و چه «فریبکاری یک خرابکار» که می‌خواهد «رئیس‌جمهور آمریکا را به باتلاقی تازه بکشاند» و یا هر دلیل دیگری «نتیجه همیشه یکی است: ایرانیان هرگز در برابر فشار سر خم نمی‌کنند، ولی این دیپلماسی است که همواره قربانی می‌شود.»
او همچنین ارزیابی سازمان اطلاعات مرکزی آمریکا از ذخایر موشکی ایران را اشتباه توصیف کرد و نوشت: «ذخایر موشکی و ظرفیت پرتابگرهای ما نسبت به ۹ اسفند در سطح ۷۵ درصد نیست؛ رقم صحیح ۱۲۰ درصد است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/75327" target="_blank">📅 19:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75326">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_fryoiW0e0IQ8EcGnyJmg5zbB5-fCoBFauFeHpY33xz6XqqhvIwt14qf8fhHU74epBTGkhmkFntdFOM2XgIjW8kCchXWKGecd8WbiisYQW6fRl1d5-YMFQrTSxJIIF4StobsW4po-S2suKXN9LW08Et1-7TKEzVpCC1Q28vburYqgHhlXr5OzL_8DO6EBk5l4zeI-7AQ3x9-oXeNFyeYTesCEnMJHDghSahEDI_h7vXePdnslF2yObuLXw56Lxd8RwvnwLABOBGc6_RDGGqlr9KsqFcDyxoZucv1yiHO-QjlQFjbBQan0CFiPNsh7ybcUGMSFWIv67LpYT5pFEs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام، فرماندهی مرکزی ایالات متحده، اعلام کرد از زمان آغاز محاصره دریایی تا روز جمعه، ۱۸ اردیبهشت مانع از ورود یا خروج بیش از ۷۰ نفتکش از بنادر ایران شده است.
سنتکام در پیام تازه‌اش در شبکه اجتماعی ایکس نوشته که این کشتی‌های تجاری ظرفیت حمل بیش از ۱۶۶ میلیون بشکه نفت ایران به ارزش تخمینی بیش از ۱۳ میلیارد دلار را دارند.
این موضوع ساعاتی پس از آن اعلام شد که ارتش آمریکا گفت نیروهایش در نخستین ساعات بامداد جمعه حملات «تحریک‌نشدهٔ» ایران علیه ناوشکن‌های آمریکایی در تنگه هرمز را رهگیری کرده و در پاسخ، «تأسیسات نظامی ایران» را هدف قرار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75326" target="_blank">📅 19:10 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75325">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU2ILDHINMjupvqaT-BV6_15nMrZPb2CFu55EmZo4hHiiCkDeV8CGtCoEBs8TDBoPfTEWkntWfBBQmsU78q8tQNMc9RNA_bXRSpntHqUPif1n2VwZ3EHuMQUYEowJ2wSAVeHQN002UR9w00xEZ9bHbUZacB1vvKEt4qmhXqKg20qEkQgEfOocpso88uS-7-rMz018wc36HuUqTPoTVsRNZQRccocZqRFIjll4CzhI2FrurXaI48nuoi_t1n4V1Bmq-uamHZF-zi9iQFRLcw1wGnBWlGxRvzWEYQ0Qh3HLWVbT5fIZ889Q9VXgeq8zn94vfoU_B992VMnq3SWdMh9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز هفتادمین روز قطع اینترنت در ایران است و به‌گزارش نت‌بلاکس این اختلال صبح جمعه ۱۸ اردیبهشت از یک هزار ۶۵۶ ساعت فراتر رفت.
این در حالی است که مقامات و افراد نزدیک به حکومت یا کسانی که حکومت خود با واگذاری «سیم‌کارت سفید» انتخاب می‌کند، هم‌چنان به اینترنت دسترسی دارند.
علاوه بر آن، اخیراً برخی اپارتورهای نیز اینترنت موسوم به طبقاتی را باقیمت‌های گزاف در اختیار برخی مشاغل و طبقات قرار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75325" target="_blank">📅 19:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75324">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scgLsjI6STNaDO80SOlzZ5QGQ4Wp-7yMI6ism1BQUIJAdNDzWglBlSBkRW3iy9GgcwXlFCtUmaZ7vUj5uw7HrBlqgqZSbhCQ_moM6G-RffGnusX6ORKZZM_ePfX_01z_djKSTXjO-4zJuZTpMdfBiFHE-OpLRe-YkJfYdJo3mYnDBW7u1g6WB2mjCtaKr7917awj2jH7ceg2hvm7wx1AW-z92Q8J7LGwt6mTiqGRwzantmSnhmERRi7-gYzuvEJKnJrELnlprTN45z6GKJzoPOV06ytPj6B_Q5f5usIbx4fea6nipsjtQeqfNsTk3GDc3Y_jMdvZZQkENTZf9pCaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز جمعه ۱۸ اردیبهشت و پس از حملات متقابل در خلیج فارس، تنگه هرمز و انتشار گزارش‌ها از مقابله پدافند امارات متحده با موشک‌ها و پهپادها، پیامی «تهدیدآمیز» به زبان عربی منتشر کرد.
بقایی در این پیام نوشت: «اگر دندان‌های شیر را دیدی که بیرون زده‌اند، تصور نکن که شیر لبخند می‌زند.»
به نظر می‌رسد با توجه به حملات روزهای گذشته به بندر فجیره و دیگر نقاط امارات و اتهام‌های قرارگاه خاتم‌الانبیا پس از درگیری در تنگه هرمز، بقایی با این پیام امارات متحده عربی را تهدید کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75324" target="_blank">📅 09:38 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75323">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/linafWgT8PgTpwB9XXLREuAXRYUjsHZEcBhNHBHbyxduaH4J449zceibKEtYK19AU-ViywcWLuFoBMBpSzO9uw6G8LbmXL6PHx-Xu1cqvyNa9_wKhlTHURmHIg0jLjBLZsc-b8smTaUKBnsHN73fYUKdJoG0m8sKXmsSVZxH531AlKy0Oyb6p4koaEy_7Xu7bRKFjN-9PQuI7IlPFVdiBGaAniW6lea0a9nkXFI6bT_nu371LWgOYc-B5H9l7Nq8QwzLL3j4_cb5r3dInx8G06CKJ-yMi-C68eSizJBeOfUM5g6q8659d5YMTgDJbdRZxEdKJpmbnSRcXGKl9gHYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اوایل روز جمعه اعلام کرد که سامانه‌های پدافند هوایی آن در حال مقابله با حملات پهپادی و موشکی از ایران هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/75323" target="_blank">📅 06:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75315">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T1_HplbjvIn8K5BoQoPayDV-CuDbffvAhts59ymYREXPGeQuxrmMFxw3Sm2AnVHOmdXoOHW-5lT1oGCrY7UK9ubJcAYO6zia2-LmygtgjYb1sHmmcfv86necRzIolQhZJQk4Zm7J4n8txnW9cQ_UvYuuFwBwq1IsakwJ2Mh81_9-HGLAg0ssRYdlXGxWG4pH6HUO6TzJFo9vfrvlPAwFFAAKZk9AqPKEnVY7dHagdMl-YNalYELnCynjJoUOKeldEDpAT026YHquFe6TuYSIU9QCA9O7cB-aqfsRRZ0xeRXu1zS1LhTRVMEykowd-5l59cvh7rv6e7KDKC5UrSGQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ELZdddsSR-v5W6l2Mysm8p3hx4PRfHLq3hSAiH8zLYa36Hz3Surim0cCTnaK0EZMP0XjQhuGBEqsOP0vMeTyeYcPIdsxgpkfixMV-7C-jqbs4s6mT9EK0A-vYsF2CrCken6xsERZgGLMhhUuH6qNq9RN9_ZpYFEtQqp7eK_Ej_bnk-GFUPfQiY8KmuyJCPhjBFxJoRroEqqWneePiKaaUDMMqJWxHEL1diCmqIy-Y2WvdRAb_G9w3C2rZHOOnB9y7f3H7ntsFIe1gc7bYhVbAqd-OhHWXwLPFMggcS-fkorphws3LXoy1k45X6yjIRMkDTF4wU-EVg34uulAiYzymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MNft6_mb-5O3O7KPTzuIOR4nZnpbXICkRh7j1orkntc0D-g8ieK8t0wi8BMK42IgTRSnX5s7wa8_n_QE5-0wfuKrRJL6muzaMdikNvxE_Sse1Ht-DvW__QWNjJL88bCTfhs_Z-qHhTWc5Vlw-fLoT2AMiUlhjFrM-Kqa7NHYihg2C-YnrdKORMKlOzMMyJIVRv_J6CZJBpC2zBpa0fH5-CVKYlQJG1xxSgWnADcAoeL2s3CTFI4p-BcHxr_rGh2ExxTLXg8um4ykrHlps0CnPSZAh6tuE3gXBHIuJhcUhcZRNsX9xdurCDY6l3m9BaTJakcQ5VcF6I-R_B0jogaZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i9S2BideRkCKc1WiX77ihKvMMdpGFHSHD7RUM6y7JyubPNeSUQGawkf-1Wg4v8dzTBUSGjdzCEls8gul5ucZvkzhahW2zf2UOkvP0P9eknRgSatwmVbreho2UGaywbnoELkbSHgyNa7Jac5fPF3tFaNVN28aoettXANev3PDNGyXcqCOXXDr2xBXWdSsFspLYoTJo5XQTLB05NWByzJ5rEBMdCVmmJtWqjeFVE7Es166IrrYRJQ8fbSbM2Bl63-9r4asA1rfs0QPLA8LI4D8rRBbJqdDToSm5Nj1hQYm45qO8q9z8tzNOibKcWBrkZrmR4uPUuu327cqqT11ZLCAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I5c71Y3HTUoc4UfmLBYOiaYb5TtVVTZRQhzpKvV3K7YkNFB8zck26ljQlCHXkIOptLX3NECXnQbBEcuUe7Noel1OfIeCJWUYDYx6rsh8O_BVOlq6K2yPP_qkeh2t7ElivhW8WPzuPcUl_6vYKzHIT-0ubgU0lDgBH9dgVdIsV5yIldMrUWtnOsgLyAAUtKNbT1B2n6huiptKBUggnYX5ucD-nk3T9zN6Mv-UbczmFeIZMvT0Ry0dRTiy1oQT8Hg8y-jHZ4jAuswSWqqFQzkxFuRUrvcVzoWMX5eaIwm_6ChO5eBvBajg4FLSFgkmy3lqOFKHl9XmlpmHKjxxKD9TOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g57CNIJ0zxtFMFpyhWoSPz0SHsuPyZRZAthghPTDVw7P-2Jit30mPfZW4LwN3j0jusNpyKyFqgap5IAO4F26-cMoZPd8zIzFjfOOhhkpvW89uwkscp6GaUB64OWa87MzEGEOFzEEYErAwtZ91J92BlJycVkSonl1x2wV75fT9-Ox7cRDT4Y7NpbND4KGAlxdmy9u6MxrrBu3tfSdMNaXSZuo9jne0urvPVg5oUy2yeb0Mow2PicFsJH_VKrw7WiW_YeUeeD_nyF5Cu-7temQ_9fhKXp9kkuOhAbtD_iBv9po6YT37zfRR3NX4Q_fpRsfBzvy0f07PTrwbRt2hsGlKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e24b568a6c.mp4?token=qRx_xnow6Jjc0_LtsorvQkhKeqb3BtJ8ixyrbR0UR3VAf0SchYuSeAdxqzhkHreulTkwI_HbiotvWrLzCNn5EY83GWJAkjs8nL3tyLr5m9qZ8Uh4LYVcC01zLNQHzD-xotKjCuD9rw0vpejlRgwJCaKBm5fNGt3yTfPDAjNmKDTv09bzS4WN7qK3slp2GOFTZxTovCpxktvHCxN83njK3BmdsZYxmbtBvecb8-sa_ip53cleM5wUUlPfMQKpT_nX30XlN7MREC2YFKVIOSDDoEISpKp6nr8Agy6xpdG5HnZDEJiSSMMU2G4tv3EpZUvrnLsz46y3UYmLKTGJNUXsEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e24b568a6c.mp4?token=qRx_xnow6Jjc0_LtsorvQkhKeqb3BtJ8ixyrbR0UR3VAf0SchYuSeAdxqzhkHreulTkwI_HbiotvWrLzCNn5EY83GWJAkjs8nL3tyLr5m9qZ8Uh4LYVcC01zLNQHzD-xotKjCuD9rw0vpejlRgwJCaKBm5fNGt3yTfPDAjNmKDTv09bzS4WN7qK3slp2GOFTZxTovCpxktvHCxN83njK3BmdsZYxmbtBvecb8-sa_ip53cleM5wUUlPfMQKpT_nX30XlN7MREC2YFKVIOSDDoEISpKp6nr8Agy6xpdG5HnZDEJiSSMMU2G4tv3EpZUvrnLsz46y3UYmLKTGJNUXsEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در گفت‌وگو با خبرنگاران در واشینگتن، با اشاره به درگیری جدید آمریکا و جمهوری اسلامی در تنگه هرمز گفت نیروهای جمهوری اسلامی با آمریکا «شوخی» کردند، اما آن‌ها ظرف حدود دو دقیقه نابود شدند.
او گفت: «امروز سه ناوشکن درجه‌یک آمریکا از تنگه عبور کردند. هر کشور دیگری در چنین شرایطی چنین کاری نمی‌کرد. به آن‌ ناوشکن‌ها موشک و پهپاد شلیک کردند و این قایق‌های احمقانه را به سویشان فرستادند. آن‌ها ظرف حدود دو دقیقه نابود شدند. نفتکششان هدف قرار گرفت. می‌دانید با نفتکش چه کردیم؟ نمی‌خواستیم شرایط حادی ایجاد شود، بنابراین سکان آن را زدیم و نفتکش شروع کرد به چرخیدن دور خودش. نباید امروز این کار را می‌کردند.»
ترامپ افزود: «همه موشک‌هایشان سرنگون شد. همه پهپادهایشان سرنگون شد و کسانی که آن‌ها را شلیک کردند نیز دیگر در میان ما نیستند.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه گفت پیشنهاد واشنگتن برای پایان دادن به درگیری با ایران، بسیار فراتر از یک «پیشنهاد یک‌صفحه‌ای» بوده است. سی‌ان‌ان نوشت، تهران همچنان در حال بررسی پیام‌های ارسال‌شده از سوی آمریکا از طریق میانجی‌های پاکستان است.
ترامپ در پاسخ به پرسشی درباره اینکه آیا ایران به آنچه «پیشنهاد یک‌صفحه‌ای» توصیف شده پاسخ داده است یا نه، این توصیف را رد کرد.
او به خبرنگاران گفت: «خب، این بیشتر از یک پیشنهاد یک‌صفحه‌ای است. این پیشنهادی بود که اساسا می‌گفت آنها سلاح هسته‌ای نخواهند داشت، گردوغبار هسته‌ای را به ما تحویل خواهند داد و بسیاری چیزهای دیگری را که ما می‌خواهیم.»
وقتی از او پرسیده شد آیا ایران با این شروط موافقت کرده است، ترامپ گفت: «آنها موافقت کرده‌اند. اما وقتی موافقت می‌کنند، خیلی معنا ندارد، چون روز بعد فراموش می‌کنند که موافقت کرده بودند.»
او افزود: «و می‌دانید، ما با مجموعه‌های متفاوتی از رهبران طرف هستیم.»
@
VahidOOnLine
ترامپ در واشینگتن به خبرنگاران گفت: «مقام‌های ایران بهتر است خیلی سریع توافقشان را امضا کنند. مذاکرات بسیار خوب پیش می‌رود، اما باید بفهمند اگر امضا نشود، درد زیادی خواهند داشت. آن‌ها خیلی بیشتر از من می‌خواهند امضا کنند.»
ترامپ گفت: «ما اکنون در ایران با مجموعه‌های متفاوتی از رهبران سروکار داریم. وقتی درباره تغییر حکومت صحبت می‌کنید، آن‌ها مدام از تغییر حکومت حرف می‌زنند. ما حکومت اول را کنار زدیم. حکومت دوم را کنار زدیم. بیشتر حکومت سوم را کنار زدیم. بعد می‌گویند آیا این تغییر حکومت است؟ من فکر می‌کنم این نهایت تغییر حکومت است.»
@
VahidOOnLine
دونالد ترامپ عصر پنج‌شنبه گفت: «ما هرگز اجازه نخواهیم داد» جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند. آقای ترامپ گفت: «احتمال آن صفر است. خودشان هم این را می‌دانند و با آن موافقت کرده‌اند. حالا باید ببینیم آیا حاضرند توافق را امضا کنند یا نه.»
@
VahidHeadline
ترامپ پنج‌شنبه به خبرنگاران گفت آمریکا با وجود تازه‌ترین تبادل آتش با جمهوری‌اسلامی در نزدیکی تنگه هرمز، در حال مذاکره با حکومت ایران است و افزود پاکستان از واشینگتن خواسته است در طول این گفت‌وگوها، طرح او برای اسکورت کشتی‌ها به خارج از این آبراه را دنبال نکند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75315" target="_blank">📅 06:17 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75314">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W8km5k_SKDRS5E-eVTWiyI2TTR5PfBy8yGb3XsdrD4r1iWDEPNIoW-S_LzvCE7v2t3Ozrj8-eOku6fcofCCGWPj45g0PYMye3jGoRhNol3gLb0F0vkWPqiv67Es3pwJLkri96cyPn0h_JsCsvFrVUS9GJjEkTy-6jhLH2maPvfd-akvoxsjEqt3AmIrHnMxhQWvCY8JPBwX5GtXT5d1gZznsvgkxHfCtyNL08nQzMHktS9Wf5NcRk_WAYcUXKGRbe5IjfksmDE2JvYQQMTXViS0rL1kuKAnmZhBfb-1uMVMdfAWruMNNfQ_jLVwIe3KocoTJFMvd4aiumghjh2EznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران را دیوانگان هدایت می‌کنند
پست ترامپ، ترجمه ماشین:
سه ناوشکن درجه‌یک آمریکایی به‌تازگی، با موفقیت کامل و در حالی که زیر آتش بودند، از تنگه هرمز خارج شدند. هیچ آسیبی به این سه ناوشکن وارد نشد، اما به مهاجمان ایرانی آسیب سنگینی وارد شد. آن‌ها به‌طور کامل نابود شدند، همراه با شمار زیادی قایق کوچک که اکنون برای جایگزینی نیروی دریایی کاملاً از سر بریده‌شده‌شان استفاده می‌شوند. این قایق‌ها به‌سرعت و با کارایی کامل به قعر دریا رفتند.
به‌سوی ناوشکن‌های ما موشک شلیک شد و به‌راحتی سرنگون شدند. پهپادها نیز آمدند و در هوا سوزانده شدند. آن‌ها به‌شکلی بسیار زیبا به سوی اقیانوس سقوط کردند؛ درست مانند پروانه‌ای که به سوی گور خود فرو می‌افتد!
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند، اما ایران یک کشور عادی نیست. آن‌ها را دیوانگانی هدایت می‌کنند و اگر فرصت استفاده از سلاح هسته‌ای را داشتند، بی‌تردید این کار را می‌کردند — اما هرگز چنین فرصتی نخواهند داشت و همان‌طور که امروز دوباره آن‌ها را از پا درآوردیم، اگر توافق خود را سریع امضا نکنند، در آینده بسیار سخت‌تر و بسیار خشن‌تر آن‌ها را از پا درخواهیم آورد!
سه ناوشکن ما، همراه با خدمه فوق‌العاده‌شان، اکنون دوباره به محاصره دریایی ما خواهند پیوست؛ محاصره‌ای که واقعاً یک «دیوار فولادین» است.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75314" target="_blank">📅 02:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75313">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kw7bqK0EteeZblV5XWtTNEaWM7iSjsbeW_IDolvoCaiaplDMUyen9i3HCVRV7lOthNQR6984EUs5pXX0fLDV8aRyOVbS4eVWkxQlE9Cl51CPQMBu6KDk3Wz_akjR-z-whD0xykCdwSHGawNDp0jak2LM-kav-Uw1LZ5q_6OMVD7h5x-i_6bxS1s6Rk7E4jQI71fejmgUCBSGHAm7z7cNIPNBMXtJLQojA13YtlQkcv2oyYGm1sZWiVD-1Slzua33iN6eZFPM-2W6odGOkC6V802pg3Zap77Xech0i64SpILTdofhRYUOPW3KGJTtjzevA3x0n5Uy9MAXSb4OFpamnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا در پی حمله‌ها به بنادر جنوبی ایران و شنیده شدن صدای انفجار در غرب تهران به ای‌بی‌سی گفت که ارتش آمریکا در اقدامی دفاعی به رژیم ایران یک «نوازش دوستانه» داده است و آتش‌بس همچنان در حال اجراست. او گفت حمله‌های متقابل به ایران فقط یک نوازش دوستانه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/75313" target="_blank">📅 02:14 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75312">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mue0UQaFQHkFf1JGKH1lveq5LQRZXCUweQ1XoXD3srHxVNtZeFQyx0gY6vj2RT9ARBWo0ZJGLEjKHgYptVsKABdk3nysAa91DkZmPuPsold0FuLadzaPbYu5o6gR16PzpCfpU-mNI-nJmhj55nDmfXMCSTbge44ZuCL1Pgzyfy7SqB9J7Kmbn9G4Dplw3bJC0SFPfSsCxmgHRK5dm8hKI4tuO45UfEG7Tk9PeyfgV6zPQS0QtdkCrqtGb-hszElt_Yxlo_9FuyQOpi_U_vzxJJ086uUQ2jif6nvCoIO-Rk06bPNhVB5iLAooefCzZEZuWENoUZv6VTvxk9gtpM_Myw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنیفر گریفین، خبرنگار فاکس‌نیوز، در شبکه اجتماعی اکس به نقل از یک مقام ارشد ایالات متحده از حملات نظامی این کشور به بندر قشم و بندرعباس خبر داد. این مقام آمریکایی تاکید کرد که این اقدام به معنای شروع دوباره جنگ یا پایان آتش‌بس نیست. این حملات دو روز پس از شلیک موشک‌های بالستیک ایران به بندر فجیره امارات صورت می‌گیرد. گزارش‌ها همچنین از حمله به ایستگاه بازرسی دریایی بندر کرگان در میناب حکایت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75312" target="_blank">📅 01:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75311">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjOJeKP_jk8xhbO5O9wm9pZyb59YrBraL04brMqA6OMWDzFUgCZDCCeh7uaoI0NpH8vHKMSF9KDBJqow6Zbp4zYmxMw92l_yxfJZlYmIfbSKNicHsE7z9CMCwRC6khLJJScxHRVXZQdl_dyix6-dlsKvgRmTDHG0Slppyc7NQbctd3_7XNMPu5XWC7J2ZoNzkGsavF-uHNCsEPs3mTLMQLYKKdJ-V4ucS8N-B5wbgQ4LSxUySoXtMuePZu0hVpsI1lRjatxgka7nXNWU3mCQHdkVi8P0C6HTDBfrX1syHijWoHhUuy17XaFbojo6vVHa0m-vwV0pcvb0r5kJyA30Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، اعلام کرد نیروهای آمریکایی ۱۷ اردیبهشت همزمان با عبور ناوشکن‌های مجهز به موشک هدایت‌شونده آمریکا از تنگه هرمز به سوی دریای عمان، حملات موشکی، پهپادی و قایق‌های کوچک جمهوری اسلامی را رهگیری و به منابع این حمله‌ها در ایران حمله کردند.
طبق اعلام سنتکام، نیروهای جمهوری اسلامی در حالی این حمله‌ها را با چندین موشک، پهپاد و قایق‌های کوچک انجام دادند که ناوهای یواس‌اس تراکستون، یواس‌اس رافائل پرالتا و یواس‌اس میسون از این گذرگاه بین‌المللی دریایی عبور می‌کردند و هیچ‌یک از تجهیزات یا دارایی‌های آمریکا هدف قرار نگرفت.
سنتکام گفت نیروهای آمریکا ضمن دفع این تهدیدها، تاسیسات نظامی ایران را که مسئول حمله به نیروهای آمریکایی بودند، از جمله محل‌های پرتاب موشک و پهپاد، مراکز فرماندهی و کنترل و گره‌های اطلاعاتی، نظارتی و شناسایی، هدف قرار دادند.
سنتکام تاکید کرد که به دنبال تشدید تنش نیست، اما همچنان در موقعیت مناسب قرار دارد و آماده حفاظت از نیروهای آمریکایی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75311" target="_blank">📅 01:25 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75310">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b377a19a19.mp4?token=Ue1sJlDFXBflg6ib8JzQP3KZbxkipkz5b76N_AqoIIMTJO7hekbdi3eZzY7yToKAZPy75cTewjS8pGLOHe5MQ8sH4ZFABf3yWSiYaAcYE3-erwXBIE2Wz5HRKuewxAhlo6sEt4KwJgHuJD0h-Ic2wGP38_hsJuJbWBrQpfYpHbrV-kFXpeiSUwbUbI_rVhu9yBIcAUWIzkVYua281GchzmafvsrEAvp_7Jtjbpc1YyXGrsmPUsgYMYpiE2-nRbzPpwYp62J1c2U5PTr6q1g-IivIAzrY8WX2hkGKTpQLRou2uE_oarscGy3DriS8o8Wo2RLmn0w_xafia8EWoAQJxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b377a19a19.mp4?token=Ue1sJlDFXBflg6ib8JzQP3KZbxkipkz5b76N_AqoIIMTJO7hekbdi3eZzY7yToKAZPy75cTewjS8pGLOHe5MQ8sH4ZFABf3yWSiYaAcYE3-erwXBIE2Wz5HRKuewxAhlo6sEt4KwJgHuJD0h-Ic2wGP38_hsJuJbWBrQpfYpHbrV-kFXpeiSUwbUbI_rVhu9yBIcAUWIzkVYua281GchzmafvsrEAvp_7Jtjbpc1YyXGrsmPUsgYMYpiE2-nRbzPpwYp62J1c2U5PTr6q1g-IivIAzrY8WX2hkGKTpQLRou2uE_oarscGy3DriS8o8Wo2RLmn0w_xafia8EWoAQJxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرارگاه خاتم النبیاء که مدیریت جنگ در ایران را بر عهده دارد، ساعتی بعد از گزارش‌ها از حملات و رد و بدل شدن آتش در حوالی تنگه هرمز، با انتشار بیانیه‌ای این حملات را «نقض اتش‌بس» و در پی «همکاری چند کشور منطقه با آمریکا» ارزیابی کرده و گفته است: «ارتش متجاوز، تروریست و راهزن آمریکا با نقض آتش‌بس یک کشتی نفتکش ایرانی و در حال حرکت از آبهای ساحلی ایران در منطقه جاسک به سمت تنگه هرمز و همچنین یک کشتی دیگر در حال ورود به تنگه هرمز را روبروی بندر فجیره امارات مورد هدف قرار دادند و همزمان مناطق غیرنظامی را با همکاری برخی از کشورهای منطقه در سواحل بندر خمیر، سیریک و جزیره قشم مورد تعرض هوایی خود قرار دادند.»
این قرارگاه در ادامه مدعی شده که نیروهای نظامی ایران به این حملات واکنش نشان داده‌اند: «نیروهای مسلح جمهوری اسلامی ایران نیز بلافاصله و در اقدامی متقابل شناورهای نظامی آمریکا در شرق تنگه هرمز و جنوب بندر چابهار را مورد هجوم قرار داده و خسارات قابل توجهی به‌ آنها وارد نمودند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75310" target="_blank">📅 01:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75309">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt80_MKuWcCR3Kdoo_5V9VMHI5OMzMRlxOTYdvr_ldsAOh59_BlIWKGqrhRCzBsSwtyMuSOKvoMEfld7TF7fQY0dPDPfjDlSvhakYY9g1KuD3AlqUr4qUrx7Mp9Lwuijo3sbYAFeXRQXTRHQQX4uueRH1M5mb3kDZN6wF-UcwdK87Y9l8EBPt-MWsazgg0Raeq8n4CgY3_VLgW0FBQZQvK3egUmAc3MQtWW6Z9qfBdbdyFfw4obh9ODsYWC5MczpFRki-H3CpwV6fpkHXfVw7XN3OCXYaRdA27QgxfaZtmRF_rKhy10fIB-jp67ljSz4sBrbuokAcpfVntMN--6MrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا پیام دریافتی پست قبل درست بود:
خبرگزاری مهر بامداد جمعه ۱۸ اردیبهشت‌ماه به نقل از محمد رادمهر، معاون استاندار و فرماندار ویژه میناب، گزارش داد یک پایگاه دریابانی در این شهرستان هدف حمله قرار گرفته است.
به گفته رادمهر، این حمله ساعت ۰۰:۱۰ توسط اسرائیل و آمریکا انجام شده است.
همزمان فاکس‌نیوز گزارش داد آمریکا حملاتی را به جزیره قشم و بندرعباس در جنوب ایران انجام داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75309" target="_blank">📅 01:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75308">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هرمزگان
پیام‌های دریافتی:
وحید بندر صدای انفجار اومد الان
الان ساعت دوازده شب صدای دو انفجار دیگه در بندرعباس شنیده شد
همین الان بندرعباس صدای انفجار اومد
سلام بندرعباس ۰۰:۰۰ یک صدا اومد
۰۰:۰۲ بامداد جمعه ۱۸ اردیبهشت صدای تک انفجار این دفعه از فاصله بسیار دورتر ظاهرا از مناطقی در نزدیکی جزیره لارک یا هرمز بود.
خودم همچنان در همین محدوده نزدیک اسکله بهمن، محله دوحه و چابهار هستم
👈
پاسگاه بندرکرگان در میناب استان هرمزگان مورد اصابت موشک آمریکایی قرار گرفت.
پاسگاه دریایی است. می‌گفتند پهپاد از همین نقطه بلند شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/75308" target="_blank">📅 00:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75307">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/95a8a7b0ee.mp4?token=UvflyJIlXK9Tzyq9eFzBhcQXVBuziWmmqdeIqOlsHruH-rEsk5jNw5GQCFhkLnUWJ3vptzvBc8WEY-i-F_iqmBPzMIcxvflJzK9PX4eb2b5yOeULK6PaaD5ZVhi5Ay11itokexoGwqSwdYByLSkYU_RBU8QfYXSUXLWLPlSCG4j1wzun5lTuI5G1GXxTbABY41K0IaFwPgZhAx7fbXuWX6afb2-vzfHNTb5KMUZc11LG9ksaIKh40iFuueTIumfmk8Uz7aKMk_GRdW_CO1vXkgc_PVvdS__6snjR5uL8EKiS4q8zX0ckg9VnJCeSpb0UHyZATL19a73KNPBg51Pp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/95a8a7b0ee.mp4?token=UvflyJIlXK9Tzyq9eFzBhcQXVBuziWmmqdeIqOlsHruH-rEsk5jNw5GQCFhkLnUWJ3vptzvBc8WEY-i-F_iqmBPzMIcxvflJzK9PX4eb2b5yOeULK6PaaD5ZVhi5Ay11itokexoGwqSwdYByLSkYU_RBU8QfYXSUXLWLPlSCG4j1wzun5lTuI5G1GXxTbABY41K0IaFwPgZhAx7fbXuWX6afb2-vzfHNTb5KMUZc11LG9ksaIKh40iFuueTIumfmk8Uz7aKMk_GRdW_CO1vXkgc_PVvdS__6snjR5uL8EKiS4q8zX0ckg9VnJCeSpb0UHyZATL19a73KNPBg51Pp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو و پیام‌های دریافتی:
وحید جان سلام ۲۳:۵۳ غرب تهران فعالیت پدافند
غرب تهران نمی‌فهمم صدای پدافنده یا انفجار ۱۱:۵۳
سلام غرب تهران چنتا صدای انفجار و پدافند ۲۳:۵۲
صدا ها مرتب و پشت سر هم نیست
وحید من غرب تهرانم، ازادی. ساعت ۱۱:۵۳ صدای انفجار دور میاد
چندتا پشت هم
ساعت ۲۳:۵۰ امشب ۱۷ اردیبهشت صدای انفجار یا پدافند محدوده غرب تهران.
۱۱:۵۳ تهران شهرک اکباتان ۴ افنجار دور شنیده شد
مطمعنم صدا پدافند نبود انفجار دور بود
۱۱:۵۴ صدای پدافند به صدای انفجار ها اضافه شد شهرک اکباتان
ساعت 23:53، ممتد صدهای پدافند و مشابه انفجار باغ فیض غرب تهران
صدای چندین انفجار الان سمت شهران ۲۳:۵۴
سلام ساعت ۲۳:۵۲ دقیقه صدای چندین وحشتناک انفجار  سمت غرب تهران شهران
پدافند غرب تهران داره میزنه
از غرب، جنت اباد نمی دونم پدافندها فعال شده یا داره می زنه
غرب تهران بلوار فردوس ساعت ۱۱:۵۴
صداهای متعدد میاد
شبیه پدافند
صدای انفجار و پدافند
جنت آباد ساعت 1154 شب
امشب
سلام وحید همین الان دوتا صدای انفجار اومد سمت بلوار  فردوس غرب صدای پندافند هم میاد به شدت
چند تا صدای انفجار و پدافند میاد سمت غرب
منطقه ۵ ساعت ۱۱:۵۲ دقیقه
بلوار فردوس شرق، غرب تهران از ساعت ۲۳:۵۰ دقیقه صداهای ممتد شبیه فعالیت پدافند میاد، و یا حتی شلیک یه چیزی فراتر از پدافند
سلام محدوده چیتگر فعالیت شدید پدافند ساعت ۲۳:۵۴
وحید ۱۱:۴۵ شب، جنت‌اباد مرکزی تهران، یه عالمه صدا که فک میکنم پدافند بودن
وحید جان همین الان غرب تهران (سمت میدون آزادی) صدای پدافند شدید میاد
سمت شهرک نفت هم همینطور...
صدای پدافند از دور در مرکز تهران ساعت ۲۳:۵۵ شنیده میشه
صدای ضد هوایی بوضوح در جنت‌آباد شنیده میشه
سلام وحید همین الان کلی صدای پدافند تو تهرانسر اومد ساعت ۲۳:۵۰
وحید سلام شهرک غرب ۲۳ و ۵۳ پدافند فعال شد.
سلام وحید جان ۲۳:۵۵ منطقه ۱۰ صدای بم عجیبی اومد چند بار پشت سر هم. شک دارم چی بود.
وحید جان ساعت ۱۱:۵۴ جنت آباد مرکزی بنظر صدای پدافند میاد چندتا پشت سر هم
سلام وحید جان ما تهران، جنت آبادیم، پدافند فعال شده، انفجار نیست
۱۱:۵۷ دو مرتبه صدای انفجار و پدافند شدید غرب تهران شهرک اکباتان
ساعت ۱۱:۵۷ باز صدای پدافند شدید و صدای انفجار. جنگ اینجوری صدای پدافند نبود.
غرب تهران، ساعت 23:57 تشخیص نمی‌دم صدای انفجاره یا پدافند، اما صدا مهیبه
وحید جان ساعت ۱۱:۵۷ جنت آباد مرکزی بنظر صدای پدافند میاد چندتا پشت سر هم
صدای ممتد پدافند غرب تهران ۲۳:۵۷ همچنان ادامه داره
۲۳:۵۷ سمت مرزداران غرب تهران صدای پیدافند میاد همینجوری
ساعت ۱۱:۵۷ باز صدای پدافند شدید و صدای انفجار.
غرب تهران، ساعت 23:57 تشخیص نمی‌دم صدای انفجاره یا پدافند، اما صدا مهیبه
11:57 صدای انفجار میاد بعید میدونم پدافند باشه جنت آباد مرکزی
صداها وحشتناکه ۱۱:۵۷غرب تهران جنت اباد مثل زمان جنگ
الان صدای خیلی شدید تر میاد ۲۳:۵۷
جردن ۲۳:۵۵ صدای پدافند میاد
سلام وحید همین الان دوتا صدای انفجار اومد سمت بلوار  فردوس غرب صدای پندافند هم میاد به شدت
ساعت ۱۱:۵۷ بازم صدای انفجار و پدافند، انفجار هم هست  ولی انفجارهای بزرگی نیستن
باز هم به صدا انفجار میاد، به نظر پدافند باشه
ساعت ۲۳:۵۸، شهران
ساعت ۱۱:۵۷، همچنان جنت‌اباد مرکزی تهران، همچنان صدای پشت سر هم به احتمال زیاد پدافند
سلام ۸ انفجار مجدد ساعت ۲۳:۵۷ غرب تهران شهران
غرب تهران سیمون بولیوار دوباره صدای احتمالا پدافند ۲۳:۵۷
سلام وحید جان ۱۱:۵۶ صدای پدافند شدید محدوده دریاچه و میدان المپیک میاد
همین لحظه ۱۱:۵۸ همچنان ضد هوایی شدید
سلام سمت شهرآرا صدای پدافند میاد پشت هم
ما مرزداران هستیم
از دوردست خیلی صدای انفجار میاد
ساعت ۲۳:۵۶
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/75307" target="_blank">📅 23:54 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75306">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/872058ebf9.mp4?token=KvCZ13np-yRJmWVZf0oK9jcfWOh-HPq-SOHaYTHFzF5htlMgFjwgpTjL_pPF7hshfY08957mGZIenVCQpHmkspNsUZMeq_dA_XAUYuUcds8h4cULPdedVETCsCSk2A_YMN6t2dQ01-eg7E_0dJKaEc0tYfS9RTAVBXSa8ZQfshnpy4Xjre7vWzJoRuo-M-KpuJ34WKWtYZU7BlcKLpCj-c_h3EWK6sXVVibi3nr6JYLh9RtUwZ7b6GZ3ZuAKHHwxKlLHwrt4ve1QUrxnuWrYq6ktyWYzet0eyoUmKgpUm-lcM-vxkh5VYlWRKa7b2GJ0mUdMSfEEJOg_452QzcL-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/872058ebf9.mp4?token=KvCZ13np-yRJmWVZf0oK9jcfWOh-HPq-SOHaYTHFzF5htlMgFjwgpTjL_pPF7hshfY08957mGZIenVCQpHmkspNsUZMeq_dA_XAUYuUcds8h4cULPdedVETCsCSk2A_YMN6t2dQ01-eg7E_0dJKaEc0tYfS9RTAVBXSa8ZQfshnpy4Xjre7vWzJoRuo-M-KpuJ34WKWtYZU7BlcKLpCj-c_h3EWK6sXVVibi3nr6JYLh9RtUwZ7b6GZ3ZuAKHHwxKlLHwrt4ve1QUrxnuWrYq6ktyWYzet0eyoUmKgpUm-lcM-vxkh5VYlWRKa7b2GJ0mUdMSfEEJOg_452QzcL-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما به نقل از یک مقام آگاه نظامی گزارش داد «به دنبال تعرض ارتش آمریکا به یک نفت‌کش ایرانی، یگان‌های متعرض دشمن در محدوده تنگه هرمز زیر آتش موشکی جمهوری اسلامی قرار گرفتند که پس از تحمل خسارت مجبور به فرار شدند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75306" target="_blank">📅 23:38 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75305">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnucGN5SFddE867hI0Cb-G88Sn8rmkEFpUO15t1CDik8AoFE38BzGF7FcBhW_ezUl3o1aAnLl-i6eOXBKRtvQaK5BrAYbbIapjPYG3WyBz1eyz1VmeMoarEelyDAYGm0WJgOCP7bHb_qDWfbQzgF8IM3oqAnFbmr6Va-ker9bp-LHFgiQZSA7peOnh-xD0dPC3_yi3UnSQrgfHYnhEqojeEuI0aPaInULiZxU6OhPDkpn-o9Q7U4lPFmh96mDExt-f_uigdYxYfQyScuQ9Cr7vSOVrqVC0PsbmrdcFSv4KPCcEK5Sfc5hUTEQzCcG8DJMj2r6qEONMlE6AKQ466y-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، در خبری اختصاصی اعلام کرد که صداهای انفجار که پنجشنبه‌شب، ۱۷ اردیبهشت در حوالی بندرعباس شنیده شد، مربوط به «تبادل آتش» میان نیروهای مسلح جمهوری اسلامی و ایالات متحده بوده است.
به گفته فارس، در جریان این تبادل آتش، بخش‌هایی از اسکله بهمن در جزیره قشم هدف قرار گرفته است.
@
VahidOOnLine
آپدیت: منابع غیررسمی حکومتی و سپاهی میگن امارات اسکله بهمن رو هدف گرفته.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75305" target="_blank">📅 22:53 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75304">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bQX-BoXhKND2PX44cTYNMawNTpZM9Hc4buC0NR2_6tp0Qsha6b4ZX0xKBW0tk9w47tgkd9llvu-gsuK3i8l5YuKvTVbmcj566sGHjw_iXyjX6wcZ7fHf0jIuZA_1q6RVLhN504kyLgK186-9oOIiZpEo5cGFm5a9-JBVJC85zYuAPIbUt7pDpQvF9cN_M8YGNreZr0wmOl5YFDUV0bpT4dacZjuycWcQ3UwCiX5OZiQ4WyIhNE9gmOsp4HGXQAzAkfq-mxOAZXfy9f01D6k6tJ82FQ1KPDh4oeljYEnqt5yUssIV9C4PhmxI0yEwCN6WOw6d6w2gwxGlX9cLeJ8lEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
تماس بسیار خوبی با رئیس کمیسیون اروپا، اورزولا فون در لاین، داشتم. درباره موضوعات زیادی گفت‌وگو کردیم؛ از جمله اینکه
کاملاً در این موضوع متحد هستیم که ایران هرگز نباید سلاح هسته‌ای داشته باشد.
توافق داشتیم که رژیمی که مردم خودش را می‌کشد، نمی‌تواند کنترل بمبی را در دست داشته باشد که قادر است میلیون‌ها نفر را بکشد.
من با صبر و حوصله منتظر بوده‌ام که اتحادیه اروپا به سهم خود از توافق تاریخی تجاری‌ای که در ترنبریِ اسکاتلند بر سر آن توافق کردیم، عمل کند؛ بزرگ‌ترین توافق تجاری تاریخ! وعده داده شد که اتحادیه اروپا سهم خود از این توافق را اجرا کند و طبق توافق، تعرفه‌های خود را به صفر برساند!
من موافقت کردم که تا دویست‌وپنجاهمین سالروز تولد کشورمان به او فرصت بدهم؛ وگرنه، متأسفانه، تعرفه‌های آن‌ها فوراً به سطوح بسیار بالاتری افزایش خواهد یافت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75304" target="_blank">📅 22:46 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75303">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEiYLw-uhfyh8IihS2eRJzHwL4GwyMea_pQIK4jk_bJG766gKLTDyDLlcgwV2baezOZBArpjtSPAD25yNFsqnVXF1n-reOfro5qmUFLc0lQxnw9QGtW0Sl6vZdXi_kiFAb7vvtHQikmAbCzvMqLXdW9ZtpklKyZpwMGtsqAwjoOopwdprjB6vaafLmEgqP23eooT1qIlCdVj2R4Kk4_tMYBZJYjiS53kWWGDQm8fgomznVbPAnqfIVDgF8_R26KRn7eDtnTlWvSkDjXkh4n7GyNXUZ5tMd8D6eB84HbT2NpG1zTwVVwnEv6KDpJ_E1IWqqrIl5XDdgmWfs8JWcCOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با تلاش‌های ایالات متحده و بحرین برای پیشبرد قطعنامه‌ای در شورای امنیت درباره بازگشایی تنگه هرمز و آزادی کشتیرانی، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، این قطعنامه را «یک‌سویه و تحریک‌آمیز» و روایت‌های مندرج در آن را «گزینشی و جانبدارانه» خواند.
عراقچی در نامه‌ای به دبیرکل سازمان ملل و رهبران کشورهای عضو، محدودیت‌های کنونی در تنگه هرمز را ناشی از «جنگ تجاوزکارانه، غیرموجه و غیرقانونی» آمریکا و اسرائیل علیه جمهوری اسلامی خواند و به جامعه جهانی هشدار داد که نباید اجازه دهند شورای امنیت به گفته او مورد «سوءاستفاده متجاوزان» قرار گیرد.
او در این نامه تاکید می‌کند که تردد در تنگه هرمز تنها در صورت «توقف دائمی جنگ و رفع محاصره و تحریم‌های غیرقانونی» علیه جمهوری اسلامی به حالت «عادی» بازخواهد گشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75303" target="_blank">📅 22:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75302">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هرمزگان
پیام‌های دریافتی با جزئیات تایید نشده از ساعت ۹:۲۵:
درود
ما غرب جزیره قشمیم. از ساعت ۹:۲۵ به فاصله چند دقیقه ۴ بار صدای انفجار اومد و موجش شیشه ها رو لرزوند.
ساعت ۹:۴۸ یه صدای انفجار و ۱۰:۰۲ صدای دو انفجار دیگه. صدای جنگنده نیومده ولی
صدای چندین انفجار پیاپی قشم همین الان
بندرعباس همین الان صدای انفجار اومد مثل صدای برخورد بمب بود
بندرعباس صدای انفجار اومد حدود ساعت ۹ و نیم شب
سلام، ساعت 21:30  بندر خمیر استان هرمزگان انفجارهای پیاپی و شدید
سلام وحید جان قشم صدای پنج انفجار
سلام وحید جان بندر کنگ ساعت 21:50 صدای چندین لانچ موشک شنیده شد
ساعت 22:01 شهر قشم در محدوده [محله‌های] دوحه و چابهار صدای دو انفجار پشت هم شنیده شد
ظاهرا انفجار ها از سمت اسکله بهمن شهر قشم بوده
خودم حاضر بودم و شنیدم
صدا بسیار بلند بود و موج انفجار هم حس شد
امروز ۱۷ اردیبهشت ۱۴۰۵
سلام داداش
قشم دقیقا الان ساعت ۱۰
دوتا موشک زدن اسکله دوحه
خیلی وحشتناک بود کل آسمون قرمز شد
همین الان بندرعباس صدای دوتا انفجار پشت سر هم از سمت دریا اومد  نمیدونم لانچ بود یا برخورد ولی هم صدا داشت هم پنجره ها لرزید
درود بر آقا وحید گل
بندرعباس ، الان ساعت ده و دو دقیقه شب صدای دو انفجار پشت سر هم آمد
ساعات پایانی روز پنجشنبه
سلام آقا وحید. قشم  همین چند دقیقه پیش  ساعت ۱۰ شب دوتا صدای انفجار اومد همراه یا نور روی دریا. چیزی رو توی دریا زدن
همین الان ۲۲:۰۴ دقیقه
صدای سه تا انفجار سمت دریا میاد
سمت سیریک استان هزمزگان
یه موشک هم بلند  شد
با فاصله نورش دیده میشد
به سمت دریا رفت
الان سمت میناب دوبار صدای انفجار اومد
با شهر فاصله داره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75302" target="_blank">📅 22:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75301">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bD0lksq5sIULxxWsJTn4wxn7dZwC1_MqgxVQYUVJxf8MkSxmKnJ3jR7D87v9g79Tj2wGnp4UpJbZVxD670y1E0Cdac_2NzLIdjcpeuTfs4UtadRDu0sR2v0CXWWnTfIKBCITF3AmmryUcBP9zBJo0Cw81KouLKZ_CjMSFV1grZwxmteCXaTyC_rnrbCqk2las7QHnvJLRBlPTUT6c7cLcjY1I380htX58fzncdNB7aN9UFPPrSk0PAphdjR-hO7-E1rx4slcihZ6HfsJh9vJRHVtcwPuN_-rrhln8Zu9p7XV2xbeP7LIWMfFPtfRrv5M35GodHSnG1UVW8a6wtZhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">mahshids979
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75301" target="_blank">📅 18:34 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
