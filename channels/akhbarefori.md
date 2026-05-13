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
<img src="https://cdn4.telesco.pe/file/Fv4DFSyCIVvujP-oiP82KWpiD-TnvMTQg_sCXaK1hwbRgoLS0l-xgyvBCJtUP1g7Ur5yq_k6KnXdkrjLgAsPMSJWevtP_69m1mb58_zMCRwpx-_-iL5ERwyQf_x2XnYofltQHTcHkimHDgmG9kFGpi2d7o29cBr7ODKYw9qmW6Zdbx3YTDubo6OriJW6tA6-QzUat4URLlEtcWtVLl3lKAV_AcIzpj6J3n2PoNP1MieArFJS5gVVRjCpiAv2Swg1P3ZmYknPj5xbesmzpSWI8sLy_a8yqRYnQvfa1B-OAwlt293mTDeiVJcc74nMRHaPKKm9CYw1JpYbLQgRUXrN_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.93M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 20:07:55</div>
<hr>

<div class="tg-post" id="msg-652154">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT7Pct0IbQFvWsKlgD5Ie-6JnXC4aYvUigcvnAbQvdvKRr8sBs27vVZH2Ur6i3igDhjGFe6Em8nbNiFqrPs3rXSZV2S6OrKahZ2NqGb5xro1X4uB1Lm70Nc4zteQWaVbBq3zJ0giCfNgrvH1iuq_2ZlO8HoMkQjyIt0zw17tcjqU7shjRiU7Ampl-B_3p4dLEzhoVQRafyIf8EaCbEPnNkTOdLxsBXuhPa30zfIMv_uFEYeBMzdrg-qV8mCVXNwrECuH9pgIAZWtM9J1NaCr_-5yFsbZUGdUCBw2GlJqpafvX-t1OcSyiZen3A-poXsNxjFwo7dTZYsb1ZXXOZBJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: خواستار آزادی فوری اتباع دستگیرشده در کویت هستیم
🔹
وزیر امورخارجه: کویت در تلاشی آشکار برای ایجاد اختلاف، به طور غیرقانونی به یک قایق ایرانی حمله کرده و ۴ نفر از شهروندان ما را در خلیج فارس بازداشت کرده است.
🔹
این اقدام غیرقانونی در نزدیکی جزیره‌ای که ایالات متحده از آن برای حمله به ایران استفاده کرده است، رخ داده است.
🔹
ما خواستار آزادی فوری اتباع خود هستیم و حق پاسخگویی را برای خود محفوظ می‌داریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43 · <a href="https://t.me/akhbarefori/652154" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652153">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2eQNHBJBaPUbw5vYO8x4b-j32QG0_u0RxxVpOlODo9e7Kk6jlHg4V67BjWjaIALsyG3M08H7V90bpv-Yx0YCFNCXRpZPPGrl5uAS65C7suHnbGbWtx0B3XX0VGuMa0-C90bK7PWu93fpJd8yZatIDERZJqubmV7NXi_p-LQnJVAVirJP3syrOvUWCwgUKVQgnEnSlk0Ytr3Pw5K3Aantm2jbhC9JM09LTbLzTg1UInW0vJTMw-lx-ZbB02HaCqv26sleQlLxwt5pHfGmfJdTUiqHAB1McogDl70zj5bk8VT3oTTPLOOnn3-n-M2-rxZQh_4S2qYFJk9vQXrbifW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراض وزیر خارجه ایران به دستگیری غیرقانونی اتباع ایران در کویت؛ حق پاسخ‌گویی را برای خود محفوظ می‌دانیم
🔹
در تلاشی آشکار برای ایجاد تفرقه و تنش، کویت به‌صورت غیرقانونی به یک شناور ایرانی در خلیج فارس حمله کرده و ۴ تن از اتباع ما را بازداشت کرده است. این اقدام غیرقانونی در نزدیکی جزیره‌ای رخ داده که ایالات متحده از آن برای حمله به ایران استفاده می‌کرد.
🔹
ما خواستار آزادی فوری اتباع خود هستیم و حق پاسخ‌گویی را برای خود محفوظ می‌دانیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 575 · <a href="https://t.me/akhbarefori/652153" target="_blank">📅 20:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652152">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggMObWheAnKJdYquAv8K_8oBixmBmgZlfMdBpUvgsDlW7OyhqbcYZGKcDxRUtYOcPnrjqKKnNnOIGbDD1SDbH3O1FxIWqlHWY4dESdwTABFzEscXbtnGTtG2s6gcLeuaA6uCkGG3HWvvwJi5RofRDYF7mU8GmtMQygkVjPwHvqmehQm47-BGkOS0chcp4ZT0qkYOuWIVPWD4INP3xzlVeFNFA6Vjj-0TkM3Rdh2N3S4sutTfDoBHsKqcomQpCVY53q3yPGnN7mUEauLu_NPaauVN_HFOYZ-ZXC0_t9utURJdSrQC8Iyd9gHjD0Q-jN-7MRNnpLP3Wne_WLrXiABEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان استخدام فعالین رسانه‌ای، اقتصادی، سیاسی و فعالین صنفی دانشجویی در ۴ استان
مجموعه خبرفوری بدینوسیله از تمامی فعالین رسانه‌ای استان‌های گلستان، گیلان، خوزستان و اصفهان جهت همکاری دعوت به عمل می‌آورد.
اطلاعات علاقه‌مندانی که سابقه فعالیت رسانه‌ای، سیاسی، اقتصادی یا فعالیت صنفی دانشجویی داشته باشند و در فرم ذیل اطلاعات خود را بارگذاری کنند، توسط واحد نیروی انسانی خبرفوری بررسی می‌شود و برگزیدگان به مصاحبه دعوت خواهند شد.
برای پر کردن فرم کلیک کنید</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/akhbarefori/652152" target="_blank">📅 20:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652151">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ed274467.mp4?token=M7JWCswnfi6n0NMTVgl0gMUGIx7_JFIcZ7T_z2Ryehk8Hbf69oNHVFFOMqWNKTCSud_STs0n1voBW5SEfwIrboQyf5scpsTr955PzAbTtlyI1EIza5UWM_pSxpQnsNDUzmQyc7sEUDZ483Aa0Wnt0sZLoQu9SA9hR1GB96vYgJvl5wysYYGe8WSRGxOBhjInDUuN225ZWYA7YWxvBuk3vTk72aYqVgvbdj4eKCj0S-tG14UWxiJli7mn81hfKc9xE01tb_JwkonYGNR-WAlNXpVA9CAEABZT3huYgn8EQBdUm6Niq2UDdWWyGEEc71JVW-9h_2TPz2r5GU1gWjZDyklw_Q77mcGkIsxINRVbo7TV3Hlnj1yl7WDR1EjO12kSDaifJe5UfkJVVsAd5Hzpsn6d7ZRUY7swVayjXeaPEJkhVyEdwVCocL-_Zjf4Ha8Kag8nrjWP2-L_DCLVmghGaXlwB8kGEs0KoYCI7FNNo-r1yAvGbWgZduRdMOjpiYJMk5XUG1AmLsc2gsBXGEiMHhr2Orp9kVSGvxgO0VDYE9mFMHS2LwPqkol1f8Kw49mURvUo3X4y1fQNgyE0Ff-HHU-f6sRSLFx3PfSdMxjRdzutW49Ls76j9XZNwzSRuAk1d7VDvtdHtLHHyOj53CrXAlrniPwEtUN0CrtvCzLY8zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ed274467.mp4?token=M7JWCswnfi6n0NMTVgl0gMUGIx7_JFIcZ7T_z2Ryehk8Hbf69oNHVFFOMqWNKTCSud_STs0n1voBW5SEfwIrboQyf5scpsTr955PzAbTtlyI1EIza5UWM_pSxpQnsNDUzmQyc7sEUDZ483Aa0Wnt0sZLoQu9SA9hR1GB96vYgJvl5wysYYGe8WSRGxOBhjInDUuN225ZWYA7YWxvBuk3vTk72aYqVgvbdj4eKCj0S-tG14UWxiJli7mn81hfKc9xE01tb_JwkonYGNR-WAlNXpVA9CAEABZT3huYgn8EQBdUm6Niq2UDdWWyGEEc71JVW-9h_2TPz2r5GU1gWjZDyklw_Q77mcGkIsxINRVbo7TV3Hlnj1yl7WDR1EjO12kSDaifJe5UfkJVVsAd5Hzpsn6d7ZRUY7swVayjXeaPEJkhVyEdwVCocL-_Zjf4Ha8Kag8nrjWP2-L_DCLVmghGaXlwB8kGEs0KoYCI7FNNo-r1yAvGbWgZduRdMOjpiYJMk5XUG1AmLsc2gsBXGEiMHhr2Orp9kVSGvxgO0VDYE9mFMHS2LwPqkol1f8Kw49mURvUo3X4y1fQNgyE0Ff-HHU-f6sRSLFx3PfSdMxjRdzutW49Ls76j9XZNwzSRuAk1d7VDvtdHtLHHyOj53CrXAlrniPwEtUN0CrtvCzLY8zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استفاده آمریکا و اسرائیل از یک موشک جدید با ۱۸۰ هزار ترکش برای حمله به یک سالن ورزشی دخترانه در لامرد فارس در ۹ اسفند ماه ۱۴۰۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/akhbarefori/652151" target="_blank">📅 19:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652150">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
آشنا: تنگۀ هرمز دیگر رهاشدنی نیست و یک وضع واقع پیداکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/akhbarefori/652150" target="_blank">📅 19:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652149">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فروش فوری ویلا ساحلی در شمال ( مازندران )
💰
قیمت ۲۰میلیارد اقساطی
🏕️
ویلا مدرن لاکچری
🔥
فول هوشمند ، داخل شهرک
🔥
✅
متراژ زمین ۵۵۰متر
✅
متراژ بنا ۴۰۰ متر تریبلکس
✅
۵ خوابه (مستر)
✅
شهرک با گیت نگهبانی
✅
معاوضه با خودرو ،طلا،دلار و...
✅️
دارای سند تکبرگ
✅️
💰
قیمت ۲۰ ميليارد اقساطی
⭐
اقساط بدون بهره
⭐
- تماس جهت بازدید :
برای قیمت و اطلاعات بیشتر و ارتباط با ما
وارد لینک زیر شوید
👇
👇
🆔
شناسه:
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/akhbarefori/652149" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652148">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSrEDOAjIMI8pb0LAxJdmF1vhOrwcF96YOSCmfx-No14c4KKZ_hh0FDUSNIBa158nRW_nGTd_hgcLcQfHc2MBwcC1IziX0kYoQWBSl5HzE-2H3RxQyB6fmksWKgP-BRqFhqTahCETfDB9k2bR8jwI9e_yakK-Ezhim7lcpOVooSNz_guXvtpaKnKe7YnKbZebvP-AkkjTJuFfRpwGso_UJtiGlrBIy5UtZayv2fdrmjk_Bn32b4e2ADv_Ez8-PG8OUgwD0o91dZu17z9ZARBEh1uDSxJQBAy1hjnvi9H4AYnQdPVi7ZTOgUwU7H9QYUcyzXYLTtweJ_Qo5nR17dWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایتن لوینز، تحلیلگر و روزنامه‌نگار آمریکایی: امارات متحده عربی شروع به نصب تورهای فلزی مخصوص پهپاد در اطراف انبارهای نفت کرده است تا از حملات ایران محافظت کند
🔹
من نمی‌دانستم که پدافند هوایی آمریکا چقدر ضعیف (رقت انگیز) است...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/akhbarefori/652148" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652147">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBu4nc-fovNhUd11FlRo444mxRyxR5saAwcOsjB9tauUpTKmHsQWMCSY6Kqe38bB-7kyptwxqMiMEtELQBGsgOpWuqRxTEUFpeB-V_ONejwLEPKMyjzAkakWw9YqA57SXCn9EbGz3973W0HAWTNHusZFWMNAPJLZp44S-vAwbNnuzImlF4pSD8wmmMxRwstldGiMnNd-ZodNnxrBHgsLZVu714WVk88D7XopZUiVCSSD-kxJzA9tZPv_zCF49LMiw5hso9VczmXn2vlDwFzl7OQ72oMkZ06iNa8b-p7aqPvCBifSox19LsRdHJ6gxPq1G6ewBEPYWtkjzvZJE23VCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نیرو: تابستان خاموشی نخواهیم داشت
🔹
عباس علی‌آبادی وزیر نیرو: با همکاری مردم و افزایش ظرفیت تولید، وضعیت امسال از سال گذشته به مراتب بهتر خواهد بود و امید است تابستان بدون خاموشی سپری شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/akhbarefori/652147" target="_blank">📅 19:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652146">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-kzTU_WIVwlDeKbqAAFuNSe5K8SRceGp8AXhLWLUkAAhNcXXfS6-pCMCNcL187iF7_v6ZCtkHXqpE5xlB6bRe2tiHu7dIIU_xB3DpR1tL9dkR2TPsknDz2vlX8McKkOrOADQYMjhthNxdhIUAV6ICxNUAQB_7R1jc3TFxRrfwxMckqdDjRfwNuhe1qpk57hFkOTHDnH-ZzxDqUVYUmfWF_T0NSLjnuaK7Oe61BUSvJaHj3fxn5uMaIuEequhZlZOeU3QVAbaZDl6Cb59KoaGqN_7sFeltYDax36X77g5NE-yCBcXH4trSWmSIdN895z1sv4ipO1sMxSCWUnlcDldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احسان تقدسی، روزنامه نگار: ایران همیشه بهشت صورت مسئله پاک کن ها بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/652146" target="_blank">📅 18:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652145">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 در زمان انتشار اخبار مهم نظامی و درگیری‌ها، کدام شیوه اطلاع‌رسانی برای شما جذاب‌تر و قابل‌اعتمادتر است؟</h4>
<ul>
<li>✓ ترجیح می‌دهم اخبار را به صورت فوری و کوتاه (بدون تایید نهایی) دریافت کنم</li>
<li>✓ ترجیح می‌دهم کمی صبر کنم اما گزارش‌های جامع و تاییدشده را بخوانم</li>
<li>✓ بیشتر به دنبال تحلیل‌ها و چرایی اتفاقات هستم تا خود خبر خام</li>
<li>✓ فقط تیترهای اصلی را می‌خوانم و وارد جزئیات نمی‌شوم</li>
</ul>
</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/akhbarefori/652145" target="_blank">📅 18:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652144">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نزدیک ۴ هزار نفر به خاطر مهریه در زندان هستند
سید اسدالله جولایی، رییس هیئت امنای ستاد دیه کشور در
#گفتگو
با خبرفوری:
🔹
سال گذشته ۱۲ هزار و ۶۹۷ نفر زندانی را که رقم کل بدهی آنها ۴۷ همت بوده است از زندان آزاد کردیم که ۱۲ هزار و ۴۸ نفر از آنها آقا بودند.
🔹
هم اکنون در کل کشور ۲۰ هزار و ۳۶۵ زندانی غیرعمد داریم که از این زندانیان ۱۵۶ نفر بدهکار دیه، ۱۷ هزار و ۳۵۸ نفر محکومان مالی و ۳ هزار و ۸۵۱ نفر زندانیان ناشی از تعهدات مهریه و نفقه هستند.
🔹
مجموعه بدهی همه زندانیان غیرعمد موجود در کل کشور ۲۰۰ همت است.
@TV_Fori</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/akhbarefori/652144" target="_blank">📅 18:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652143">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuQ35caBqywSC2K-mO-hWPJ4wK-gkZqAerqgYbP6y8hiLhBVK-UomxmaalvhE6AB6v1H0sx-z-bwK6O29MAr-nCjaxJxJwS_aBPDmFnJ4U-RgOAy2a0tW6Px-xZdFfP5TDPPKnihzS8DFRb6sbcOh6t6Dfaq_TzWDmPEk8vXMFqbSGMEDHbRcEZLDylqarQDuwX3zNgBjNcdWr_EGvOVIV2kvcqnYKZ4ZCsavxP-1RQMIxjWtE6lurBJ6pr6977KTf3mWPDvx2omMmvBjXz55CFcGreeheFNGwJsCs6Yr1BJFMsWg2lNr8E3MXm6_xHeJpLBr9XmN7BpTZTPsmOVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موجی از زباله، دریایی از درد
🔹
پلاستیک‌ها تجزیه نمی‌شوند، فقط خرد می‌شوند و وارد زنجیره غذایی ما می‌شوند. برای حفظ سلامت دریاها و خودمان، وقت آن است که جدی‌تر با پلاستیک خداحافظی کنیم.
شما هم به کمپین
#نه_به_پلاستیک
بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic
#نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/652143" target="_blank">📅 18:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652141">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
معاون ارتباطات دفتر رئیس‌جمهور: اینترنت بین‌الملل حتما وصل می‌شود
🔹
محدودیت‌ها ناشی از ملاحظات امنیتی دوران جنگ است.
🔹
دولت قصدی برای دائمی شدن محدودیت‌های اینترنت بین‌الملل ندارد.
🔹
محدودیت‌های ایجادشده ناشی از ملاحظات فنی، امنیتی و نظامی بوده است.
🔹
دسترسی به اینترنت همانند بسیاری از خدمات عمومی، حق طبیعی شهروندان است و دولت نیز قصد سلب این حق را ندارد، اما در شرایط خاص و اضطراری، مسئله امنیت کشور بر بسیاری از حوزه‌های دیگر تقدم پیدا می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/652141" target="_blank">📅 18:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652140">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZf-Y0Dbl5L-vPwhyrKuqlmenZjoOphdJ8fEl6uW8E0BoOOjLWFiBEQbCsRBHw5DvtOxLQfsDx1BbhZdRBVxJFSXPwJja5GBvet_BZ6UDxqV1FavDlzKXhJhT1YkcyrZOU9JlhhWInLB8HGK3l8RIK1DpPD4xU_c3bpjQhglvRqp2QvaD5FqIKe3oeHPmGUyKyxTb0UKpzdZLBKpAcvkiGmG5OWsHlZFSfAUHaSBLFAqpNwflZBiAxPklFNDziSzg92ravgvxGqUWfIPLc21580xP7vdYR85p68lixiFA3ukuWJ0fiC8lHKzGS8DMzsk5KSeb5LdyO7kFrrYCbE3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهم خودروسازان از ارزش ریالی بازار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/akhbarefori/652140" target="_blank">📅 18:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652139">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2a897a4f.mp4?token=VKLSJmqidGqfxdGYBWQV6Shz8zm-iFwbZGqRoSzYvrtr06jnjNQ8LcKqc8C-5R08XbehTByKZuUoqXK56Yvo3vIj-b2y0NOL3kX3EHg240kb4axn-RpqW4QZlu0788y74jmjRp1ZhiON6SsSB7R5YX15Kk-nDnngmCS6a-DfArBvHkkEzYcNNmZjqiHv2ek0HR5DS29wLLlwcgHzJwtqzB6s2LXO0MNwDVAzSauLl5QBBhLBmSfrmHLwMRzvQTIPCLI4T4UzpXBQn_P2WnELb7NEfkAlB3YEXi06kqkaZGxCQqszldma6tpGsnyCC77NMNWPLAeJPAkEzXhqWjEufLp9eJqUL-o_dPNuLiBoNulyDXjz3aS6pfTRCmQHd3JTLlQSzI9WP7_1Ilj1xO95bgshaFStwogphm89zxz8MBNaw8WwH7lSmCSwhiqGoI9ENbaUkrLlAlD5x1QJ4I4_s-b6sSR0uYJxLAoYL0mgp90WsVKlzSV6c2b_9imyO8zMwZcPxP7eQI2fjOqMxqrUB73eLVC9C2FYQqcyd9EOkBNHxiugXaZFFzjRPnC4bp8BBOQeFbpxV4N39Zizrd-8_auJtIAkg6oUtQFIFK4Dwiq6dp3DjCzpDdnRMXe8zRn0y0cHUo_F93cX89P3GKVOaVBzq3DkZ5V7E90lI71i5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2a897a4f.mp4?token=VKLSJmqidGqfxdGYBWQV6Shz8zm-iFwbZGqRoSzYvrtr06jnjNQ8LcKqc8C-5R08XbehTByKZuUoqXK56Yvo3vIj-b2y0NOL3kX3EHg240kb4axn-RpqW4QZlu0788y74jmjRp1ZhiON6SsSB7R5YX15Kk-nDnngmCS6a-DfArBvHkkEzYcNNmZjqiHv2ek0HR5DS29wLLlwcgHzJwtqzB6s2LXO0MNwDVAzSauLl5QBBhLBmSfrmHLwMRzvQTIPCLI4T4UzpXBQn_P2WnELb7NEfkAlB3YEXi06kqkaZGxCQqszldma6tpGsnyCC77NMNWPLAeJPAkEzXhqWjEufLp9eJqUL-o_dPNuLiBoNulyDXjz3aS6pfTRCmQHd3JTLlQSzI9WP7_1Ilj1xO95bgshaFStwogphm89zxz8MBNaw8WwH7lSmCSwhiqGoI9ENbaUkrLlAlD5x1QJ4I4_s-b6sSR0uYJxLAoYL0mgp90WsVKlzSV6c2b_9imyO8zMwZcPxP7eQI2fjOqMxqrUB73eLVC9C2FYQqcyd9EOkBNHxiugXaZFFzjRPnC4bp8BBOQeFbpxV4N39Zizrd-8_auJtIAkg6oUtQFIFK4Dwiq6dp3DjCzpDdnRMXe8zRn0y0cHUo_F93cX89P3GKVOaVBzq3DkZ5V7E90lI71i5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: بانک مرکزی منابع مالی بازسازی واحدهای آسیب دیده در جنگ تحمیلی سوم را تامین می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/akhbarefori/652139" target="_blank">📅 17:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652138">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ec3b0e04.mp4?token=EwPWvuh_eJNkQ8fgOBh3Gdr_zXV2pZcpAkPuAQEPbdE5HDAAqK0iRM_P6w8sy5oeXmohIp0MRhUvLnvDhR-5kmYYDwUxkZsq89F-hlVHzOANq_igM28KdIcWF4PxFwbwM3a21uf4FAyN7ibpGxkRzyOj-qA8O6GPoEKhocG-d2jczw51gbJYRcrdN6emgIW2sZNFR0ejy257hw_zEmIiy5D9_fa80hNW6Jopc2FdMHW5TWPo7u1NDEWmGg3itD9GS_wsoFR8pQA857sT1nvwNwPe_Jt_6kdsZL0sLaeXiP_tjBmjPspbsanrmmVGIJ3h-U4qhtwVQq0hWVY1tey3iDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ec3b0e04.mp4?token=EwPWvuh_eJNkQ8fgOBh3Gdr_zXV2pZcpAkPuAQEPbdE5HDAAqK0iRM_P6w8sy5oeXmohIp0MRhUvLnvDhR-5kmYYDwUxkZsq89F-hlVHzOANq_igM28KdIcWF4PxFwbwM3a21uf4FAyN7ibpGxkRzyOj-qA8O6GPoEKhocG-d2jczw51gbJYRcrdN6emgIW2sZNFR0ejy257hw_zEmIiy5D9_fa80hNW6Jopc2FdMHW5TWPo7u1NDEWmGg3itD9GS_wsoFR8pQA857sT1nvwNwPe_Jt_6kdsZL0sLaeXiP_tjBmjPspbsanrmmVGIJ3h-U4qhtwVQq0hWVY1tey3iDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین  انهدام بالگردهای دشمن توسط رزمندگان سپاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/652138" target="_blank">📅 17:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652134">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o76XmQOPALwX11_fOooySlG0sT15jSfmm7J7hrukZtPo0QyYVJelFrn4Rvvmh62ez-QH5HFjNrcnY4LZV_Trxr6Y4M5oXbSCHndMDRtSSmt399Echg86vSJprU0Go7chHdkfEBQQu8kmzRcNubbU9qPW-cQpFYuEkzBhxDVjnuK0YcW02yI3tEhJYWk_YyEDSFGsMK0NuOlH1wP3BmQylZ6a2KBO-lac2t6enlzLa6bOtYRo2RnZ614m_Ez9pvvAbK8RCqUkAj1Cqxo2JpwQrz3WE2a5U8CmsRwvlNhlxISzm5d4j0r7JJAC3KvDzK0wpXGYs3C1722fj-be5N-jVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دعوت از اعراب برای حضور در نشست ناتو با محوریت جنگ ایران
🔹
به گفته منابع آگاه، سازمان پیمان آتلانتیک شمالی (ناتو) قصد دارد از نمایندگان چهار کشور حوزه خلیج فارس برای حضور در نشست آنکارا دعوت کند، نشستی که احتمالاً جنگ ایران و شکاف فراآتلانتیک بر گفتگوهای آن سایه خواهد انداخت.
🔹
بر این اساس،‌ انتظار می‌رود وزرای خارجه کشورهای بحرین، کویت، قطر و امارات متحده عربی به نشست ۷ تا ۸ جولای (دو ماه دیگر) در پایتخت ترکیه دعوت شوند، اگرچه دفتر مطبوعاتی ناتو از اظهارنظر در این باره خودداری کرد.
🔹
این نشست در پی افزایش تنش‌های فراآتلانتیک بر سر جنگ ایران برگزار می‌شود. دونالد ترامپ، رئیس‌جمهور آمریکا، متحدان ناتو را به دلیل عدم کمک برای بازگشایی تنگه هرمز مورد انتقاد قرار داده و متعاقباً از خروج حدود ۵۰۰۰ سرباز از آلمان خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/akhbarefori/652134" target="_blank">📅 17:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652132">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e1a3ee0e.mp4?token=mzuUcFhplo7kRaodv_MmsY_OAQnJXKXGwDfF-GiUZ0R5hrTGyF6SZ380kDzVS6AOwy59FVITJurvWVp9LmVL8cOm670w7_VxOb8qaJ8yvt51SzuR3OWtc6nrOoeQ8zWHBL9ZXb9r5xJIcrp-n4MGQwrNJrjHRNSN_nyE1RWjqNvrvqM-2GwzGdkzi0JF7lZ-79Ai0wa-itSbrMxhc-0vNRhArX0qBmEP3Qr6FE2SsTIWffILl5RhasAUyjeqA1u4rwimucjyf23FQt5OGJlxfWK96jqDlt4Gd6yWBvocqEjosVbCQljb0vivjw-hO0pIoPLRpBJYCMi3EGlhL8nX0Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e1a3ee0e.mp4?token=mzuUcFhplo7kRaodv_MmsY_OAQnJXKXGwDfF-GiUZ0R5hrTGyF6SZ380kDzVS6AOwy59FVITJurvWVp9LmVL8cOm670w7_VxOb8qaJ8yvt51SzuR3OWtc6nrOoeQ8zWHBL9ZXb9r5xJIcrp-n4MGQwrNJrjHRNSN_nyE1RWjqNvrvqM-2GwzGdkzi0JF7lZ-79Ai0wa-itSbrMxhc-0vNRhArX0qBmEP3Qr6FE2SsTIWffILl5RhasAUyjeqA1u4rwimucjyf23FQt5OGJlxfWK96jqDlt4Gd6yWBvocqEjosVbCQljb0vivjw-hO0pIoPLRpBJYCMi3EGlhL8nX0Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کولر پوشیدنی رونمایی شد!
🔹
جذاب‌ترین خبرهای حوزه فناوری و تکنولوژی را که با هوش مصنوعی تولید شده را ببینید و بشنوید.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/652132" target="_blank">📅 17:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652131">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
۷۷ واحد صنعتی اصفهان در جنگ رمضان به صورت کامل تخریب شد
🔹
مدیرکل امور اقتصادی استانداری اصفهان: بر اساس آمارهای دقیق، یک‌هزار و ۴۴۸ واحد صنعتی، صنفی، تولیدی و توزیعی در سطح استان دچار خسارت شده‌اند که از این تعداد، ۷۷ واحد به‌صورت صددرصدی تخریب شده‌اند.
🔹
تاکنون چهار هزار و ۲۷۵ نفر شغل خود را از دست داده‌اند.
🔹
میزان خسارت خوداظهاری‌شده این واحدها نیز بالغ بر ۳۷ همت، معادل ۳۷۰ هزار میلیارد ریال برآورد شده که این رقم، ضرورت مداخله فوری شبکه بانکی را بیش از پیش آشکار می‌کند.
🔹
از این تعداد، ۱۰۶ واحد نیازمند تسهیلات خرد زیر ۱۰۰ میلیارد ریال هستند که با تأمین آن، ۹۲۹ فرصت شغلی احیا خواهد شد.
🔹
همچنین ۲۸ واحد دیگر به نقدینگی بین ۱۰۰ تا ۵۰۰ میلیارد ریال نیاز دارند که بازگشت ۵۰۶ نفر به بازار کار را تضمین می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/akhbarefori/652131" target="_blank">📅 16:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652130">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سخنگوی ارتش: تنگه هرمز تحت کنترل راهبردی نیروهای مسلح ایران است
🔹
دیگر اجازه نخواهیم داد تسلیحات آمریکایی از تنگه هرمز عبور کرده و وارد پایگاه‌های منطقه شود، هر کشوری بخواهد از این آبراه عبور کند، باید تحت نظارت نیروهای مسلح ایران باشد و عبوری بدون ضرر انجام گیرد.
🔹
غرب تنگه در اختیار نیروی دریایی سپاه و شرق آن در کنترل نیروی دریایی ارتش قرار دارد.
🔹
دشمن با وجود برنامه‌ریزی ۲۰ ساله برای حمله به ایران، هرگز پیش‌بینی نمی‌کرد نیروهای مسلح نه تنها توان رزم خود را حفظ کنند، بلکه با شلیک موشک و عملیات زمینی، مانع تحقق اهداف دشمن شوند و این مقاومت، عامل بزرگ پیروزی امروز ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/akhbarefori/652130" target="_blank">📅 16:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652129">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL5hpXIjBxGcOjVpHi-iOWwzL9dacDsnIfSb8McsXD7HARKjuEXclhgN7-Jou6Or7jtDq370c5Z91iwWqbJul1dvcbbBLGRgylyJP-_Hl9zjESyaNPJja_8xn3qwKcdIsflTVpN5D-anwget0lwWxe-5G1bhKqNY71jAViqthK-PeWzLxxo3iws0OONMReRHqGl5K5eKRgNWK5qbZyMuBbBowtB_W5SndCg4mw0iI0-7r0dhITcnlGXFbzjFagHY-hYjtHaURxdW9HtiaswtyMBfulnIuiYNAWwiG56J5QiVutWCX2X7cdA_OferLQ_e5HRbGs4BMfa0BWEIq5GxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حذف ارز ترجیحی بیشتر از جنگ قیمت‌ها را بالا برد
🔹
درحالی‌که بعضاً ادعا می‌شود قیمت مواد خوراکی و اقلام سفره خانوار عمدتاً از زمان شروع جنگ تحمیلی وارد شوک افزایشی شده، اما بررسی آمارها نشان می‌دهد درصد قابل‌توجهی از این افزایش قیمت مربوط به بازه زمانی آذر تا بهمن‌ماه ۱۴۰۴ یعنی دوماهه اول سیاست یکسان‌سازی نرخ ارز و حذف ارز ترجیحی ۲۸۵۰۰ تومان می‌شود.
🔹
بنابراین مرتبط دانستن کل افزایش قیمت‌ها با تغییر سیاست ارزی یعنی یکسان‌سازی نرخ ارز و حذف ارز ترجیحی، نمی‌تواند گویای تمام واقعیت‌ها باشد، همچنین ادعای اینکه کل افزایش قیمت‌ها در این مدت به دلیل شوک ناشی از جنگ بوده نادرست است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/akhbarefori/652129" target="_blank">📅 16:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652128">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وال استریت ژورنال: حمله به پالایشگاه ایران در جزیره لاوان، کار امارات بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/akhbarefori/652128" target="_blank">📅 16:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652127">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ایران یک آژانس جدید به نام اداره تنگه خلیج‌فارس تأسیس کرد
نیویورک تایمز:
🔹
طبق گزارش لویدز لیست اینتلیجنس، که کشتیرانی جهانی را رصد می‌کند، تهران در حال حاضر یک آژانس جدید به نام اداره تنگه خلیج فارس تأسیس کرده است.
🔹
لویدز اعلام کرده، با این کار، ایران «خود را به عنوان تنها مرجع معتبر برای اعطای مجوز به کشتی‌هایی که از تنگه عبور می‌کنند، تثبیت می‌کند».
🔹
این مرجع جدید ایرانی فرم درخواست کشتی‌هایی که به دنبال عبور هستند را برای آن ایمیل کرده است تا ترانزیت را تأیید کرده و از هر کشتی که از تنگه عبور می‌کند، عوارض دریافت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/652127" target="_blank">📅 16:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652126">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تب گرانی بی ‌حد و حصر خودرو خوابید؛ افت ۷ درصدی خودروهای داخلی
کرمی، رئیس اتحادیه خودرو در
#گفتگو
با خبرفوری:
🔹
وضعیت بازار خودرو حباب داشت که مجدد مقداری از آن برگشت. فعلا بازار خودرو رکود است و خرید‌وفروش نمی‌شود. اگر همین روال باشد، شاید تا چند روز دیگر قیمت‌‌ها ریزش بیشتری داشته باشد.
🔹
حدودا قیمت خودروهای داخلی ۷ الی ۸ درصد و خودروهای خارجی ۱۰ الی ۱۵ درصد افت‌ قیمت داشته است. درحال حاضر نه خودروهای خارجی و نه داخلی خرید و فروش نمی‌شود.
🔹
ثبت‌نام ماشین از طریق سایت معمولا الکی و بیخودی است و حتی یک ثبت‌نام هم نشده، سایت را الکی باز می‌کنند و می‌گویند ثبت‌نام کنید و مردم را سرکار می‌گذارند.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/652126" target="_blank">📅 16:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652125">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: طرح مدیریت هوشمند تنگه هرمز در کمیسیون به جمع بندی نهایی رسیده و برای بررسی و تصویب  در سامانه مجلس بارگذاری شده است
🔹
عزیزی:
🔹
سه گانه موشکی، مردم و تنگه هرمز محصول پنجاه سال تلاش آمریکا را بر باد داد.
🔹
پیام حضور و ایستادگی مردم در خیابان ها و میادین ، بخشی از رسالت مبعوث شدن است.
🔹
جمهوری اسلامی ایران با مدیریت هوشمند تنگه هرمز می خواهد از این ظرفیت جغرافیایی به عنوان اهرم قدرت‌ساز استفاده کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/akhbarefori/652125" target="_blank">📅 15:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652124">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVKh-Pq3aLMX0FBEhRkYQyKuIiIiFgDXpSDqEb4Vmr2rwdzTXkZdo_7n0rTq5WcSWNFo6jRgo7yxzyWvFlwq8uwloN3zl1ZjDjb4R46gMLyjm8uSMS4LYTbOJNApUz6aDP3AlLKOF_Wsy6LMimgDDtk8MCvKi14XVbFZPh8qujneUe7gFmWXk71UXOIMf0RW-ToFU0tVYSpMs1PYTx7DgME-7JNr9V4D6XTySHoTPzEeSkt5rFW3V1QQJwtailfHl-yfY21GyHsK1_AlVinQoB5_uDtJ6pr8iJ5uoPE0ScYJuwpq_0yF98OGNsqqm0kczfUUGP78U1utBgencImK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: پاکستان و عراق از ایران مجوز ویژه دریافت کردند!
رویترز:
🔹
به گفته پنج منبع آگاه، عراق و پاکستان هر دو با ایران برای حمل نفت و گاز طبیعی مایع از خلیج‌فارس قرارداد بسته‌اند که نشان‌دهنده توانایی تهران در کنترل جریان انرژی از طریق تنگه هرمز است.
🔹
دو منبع آگاه صنعتی که نخواستند نامشان فاش شود، به رویترز گفتند که به طور مشابه، دو تانکر حامل LNG قطر، پس از توافق دو جانبه جداگانه‌ای بین اسلام‌آباد و تهران، به سمت پاکستان در حرکت هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/652124" target="_blank">📅 15:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652123">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
جدال داغ در الجزیره؛کارشناس ایرانی با سندی از جنایت میناب، کارشناس آمریکایی را به سکوت کشاند
🔹
مختار حداد کارشناس ایرانی و سردبیر روزنامه الوفاق در پاسخ به ادعاهای واهی کارشناس آمریکایی در شبکه الجزیره درباره جنگ تحمیلی آمریکایی-صهیونیستی علیه کشورمان،با نشان دادن بخش هایی به جامانده از مدرسه شجره طیبه میناب گفت: این‌ها بخش‌هایی از مدرسه میناب است.
🔹
این مربوط به اولین ساعات جنگ است، زمانی که آمریکا با چهار موشک به آن مدرسه حمله کرد و کلاس‌های درس به این شکل و به این قطعات تبدیل شدند،و۱۶۸ کودک به دست این دولت آمریکا شهید شدند.
🔹
حداد افزود: کسی که غیرنظامیان را هدف قرار می‌دهد و آن‌ها را به شهادت می‌رساند، آمریکا و رژیم صهیونیستی هستند،وکسی که از قاتلِ غیرنظامیان حمایت می‌کند همین دولت آمریکاست؛ همانی که از این رژیم صهیونیستی حمایت کرد، رژیمی که ۷۰ هزار فلسطینی را در نوار غزه به قتل رسانده و همچنان به این عملیات‌ها ادامه می‌دهد و هر روز فرزندان ملت فلسطین، لبنان و ایران را به شهادت می رساند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/akhbarefori/652123" target="_blank">📅 15:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652121">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-OYKHr9lM1sCR1AIZkfvnsSYbqNMZkaoDbT1v0JOID1nc41kPuouX37V2jbsso54DfeQBqYfreifLBMzbhgVfS8YeOwCZ7TKWvUZ26ABMzzqJ4qQ5Rl6D6jV9dfjasKCYQxhgu94O1BgMWJ_9wLvuZ5UQ7-ZPXvYBslQ_eDMG7yuUOUxT02QKQmAHMfs-A28Er_6VRZYivJZ2oV2f1rurrK4Jbc2gNxDR6asTUbDB_UM6FNZT2ULF0ug2maqN53-yvYVPZfSYNGHmQQp2z4mrysN9ZKumEz6qFjllreZBKq_0VyJq_QtDGEirPvsnMkP48avNRHolXU6TA_R_43Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4MUJE1bsSbpbOepy0cpRxutPZ7snbo-tgvGya99k1wd5dk1s9pdmbxM3fWkYg1F4LUd6vYFndNUYMrbeFXh4B3ra5H72tbK73YuK8czsRsiBZPY6IcJPi_NrCjnXxBVKa6ZQ8HmWmMlJg5lJYVCCGjmg_bo6mJP9ikS6hSX3kh_vXAFZpMPTpsZU8BHC8nAvnqCRR29gL_BL6Ng9NCbROW0fGSyYAOl28OIxBk-y_I-OqyQOgvcOVQcuN3SniJzwj0d8o7MFttnqM6mv9qv3xT-xyhMt0vQERhKtW2YFWQ-dpx6LNM59xUK2_ZsBP08YvI80d6HycuT2H8zCc6_xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زمین را خفه نکنیم
🔹
هر بطری پلاستیکی که استفاده می‌کنیم، سال‌ها بعد از ما باقی می‌ماند. پلاستیک‌ها مهمانان ناخوانده‌ای هستند که هرگز نمی‌روند...
🔹
امروز نه بگوییم، تا فردا دیر نشده.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/akhbarefori/652121" target="_blank">📅 15:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652120">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ba53bbb1.mp4?token=UNs74Rndbpz6JAMT0Qr6z0QpIWnBh_yh1TelCnhnfDT38yXNBBr8RZ7zaavIX7n8IGiSUoop6jIojjd-RUVh5WlLIchJ25_t8TNqyUFVywap572iUl4EvEM3a5xSZ5MEqM-taMpww9gvY-az5huEXyVRnAe6J1fwri0_-2lpqwwy1wGhrAiUqd6sXee7OwY-g84PW-UWQlwL4T9jR_lt9DtVTUJG95sc7s0FyiuKHaoRKTXXz_O4M97n5uzow62RM_vVbT5pBHnfXZ5CfdKjRRgaS0383_JGeE_Y6BkyuWQybGvOjrzRINY59ogy266pjpbjc3Nhk48xwyr7ppEPSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ba53bbb1.mp4?token=UNs74Rndbpz6JAMT0Qr6z0QpIWnBh_yh1TelCnhnfDT38yXNBBr8RZ7zaavIX7n8IGiSUoop6jIojjd-RUVh5WlLIchJ25_t8TNqyUFVywap572iUl4EvEM3a5xSZ5MEqM-taMpww9gvY-az5huEXyVRnAe6J1fwri0_-2lpqwwy1wGhrAiUqd6sXee7OwY-g84PW-UWQlwL4T9jR_lt9DtVTUJG95sc7s0FyiuKHaoRKTXXz_O4M97n5uzow62RM_vVbT5pBHnfXZ5CfdKjRRgaS0383_JGeE_Y6BkyuWQybGvOjrzRINY59ogy266pjpbjc3Nhk48xwyr7ppEPSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما هنوز برای هم هستیم ...
🔹
توی روزایی که همه خسته‌اند، هنوز آدم‌هایی هستن که حاضرند بی چشم‌داشت کنار بقیه بایستن…
🔹
یکی زخم می‌بنده، یکی سقف می‌سازه، یکی جون دوباره به زندگی میده.
🔹
این ویدئو رو ببین؛ شاید دوباره به آدم‌های اطرافت امیدوار شدی.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/652120" target="_blank">📅 15:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652119">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbxuRO7F5i7SzintC2f_NYC-vK7-HTtdcCNYiCHxsZawwX4-XDH8VrpzKHskDtHv6sqkMPw2zi7FWkquq2OZT2_vbvrzWir5MkCtG2u95_kgWTX6BK2_wwxxevLTK7r3-9Kjz6WmEO0fUYLynabmXNpAYqpWXc2cfmARvJoHuPEBEPMJASM-4_CqcqsVG0AQZjPKTKwzKMwaRTbf7PkJj1JhV5jUEeI6F5dAn-tQorOVbW6e68GNtr84lx_pwHUgKpeDoBNdDWOo5UMk7vcGIYSkKsS1FyoPwLPlyhOaoMtquYf2BWcMqiELvGWRgmqz7FAyidYZXqY1H_BGdFy2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود نظامیان اسرائیلی به منازل سوری‌ها در القنیطره
🔹
منابع سوری از تداوم تحرکات نظامیان رژیم صهیونیستی در مناطق جنوبی سوریه در سایه انفعال دمشق و ورود آنها به منازل سوری ها خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/akhbarefori/652119" target="_blank">📅 14:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652118">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تداوم نقض آتش بس؛ سومین حمله امروز اسرائیل به جاده بیروت-صیدون؛ افزایش کشته‌ها به ۸ نفر از جمله یک مادر و دو کودک
🔹
یک فروند پهپاد اسرائیلی خودرویی را در شهر سعدیات، در نزدیکی مسجد جامع این شهر، هدف قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/652118" target="_blank">📅 14:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652117">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
آتش نشانی تبریز: در پی ریزش ساختمان نیمه کاره در تبریز  ۲ نفر جانباخته و ۶ نفر مصدوم شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/652117" target="_blank">📅 14:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652116">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giIlsT3Zs21TupR7sRckA6T9Y-7Anv8UfZT3c-2TQVTZI1YvHSTRT4NAiB0rICIO_vf4x624pPGSA3f3R-8y7N4y6smR2pK49eRS5EttyjTnctSrjPeDnkM4FZkZtNpa7m7lpW_DPcPVd1FXCwSW7wjYf18Uq-a3qqkuVqaVT91jCtYx1djBIMoPtqn4htLJrhnsA45jpXRR1dzrPSIefJYECthSvLmEYCfIILItReaM4vRMws7VEKiFOI9BDbUQ1c8vo4vXCWIPJ1qB9QKDSF0NtEEeFCi8DV5wyjR8Hzx1nzPBDmjFsuczOKY6J-6mrZDB5LBCYX3RTFxFhlNN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کانون وکلای قوه قضاییه: حمله به فرودگاه بدون کاربری نظامی جنایت جنگی است
🔹
حسن عبدلیان‌پور رئیس مرکزوکلا، کارشناسان رسمی و مشاوران خانواده قوه قضاییه در فرودگاه شهید دستغیب شیراز: فرودگاه شیراز به لحاظ موقعیت جغرافیایی به هیچ وجه گزینه و هدف نظامی تلقی نمی‌شود و دشمن بدون رعایت تمامی موازین و قوانین بین‌المللی در جنگ، این منطقه را هدف قرار داده و منافع ملی و سلامت جان شهروندان را به خطر انداخته است.
🔹
هدف قرار دادن مستقیم هواپیما‌های مسافری و رادار فرودگاهی مصداق جنایت جنگی علیه امنیت شهروندان تلقی می‌شود و به همین منظور وکلای ما در کنار کارشناسان رسمی حضور پیدا کرده‌اند تا در مورد پیگیری حقوقی این جنایات اقدامات لازم را در خود میدان انجام دهند.
🔹
براساس نظر کارشناسان ما دشمن در حملات خود با استفاده از سلاح و مهمات نامتعارف و غیرمجاز درحالی که فرودگاه در ساعت خدمت رسانی بوده امنیت و سلامت جانی مردم را به خطر انداخته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/akhbarefori/652116" target="_blank">📅 14:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652115">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSr9tLtTU0usJAtr_sgjYLJeFMoEJHhWOCMxYWbwzFhCJq3XlI88F5PwyvOMvj9yElsgPgW17SYqm1nvyrvP6IrcCG6Z4FO8BCavHpaoYGu2Mra8K7WiqdLQq032yc96RJt2gY8zlFrDn3tDbA3nSSyQkAFgyPy34MLoiZNwvIIszXJHo0OSELN54KSr4kjbqvroCUJoxSAVzNUubQu-1G4DgVQZpW7rflVGJRk1Logk1mAgRCGh7vQK7Y5c2ahMWoBxwxuL027ZYcnfci7ikV809jRqTJ0A0GvFelePEnCZMCsJKK922JNq7JHcuJZAKcKl4O7d9Nl2Tlje5j5aug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف ۷۰۰ تُن روغن احتکاری در بروجن
🔹
فرمانده انتظامی چهارمحال‌وبختیاری: درپی بازرسی از یک انبار، ۷۰۰ تُن روغن خوراکی احتکاری به ارزش تقریبی ۹۹۳ میلیارد تومان کشف و یک متهم دستگیر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/akhbarefori/652115" target="_blank">📅 14:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652114">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زلزله شب گذشته را ۷ میلیون نفر حس کردند؛ احتمالا وقوع دوباره زلزله
مهدی زارع، زلزله‌شناس و استاد پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله در
#گفتگو
با خبرفوری:
🔹
اینکه در زمان کوتاه زلزله‌ای به عنوان زلزله بزرگتر اتفاق بیفتد، با اطلاعات موجود چنین پیش‌بینی‌ای نداریم، اما با توجه به اینکه منطقه مستعد رخداد زلزله‌های بزرگتر است، زلزله‌های کوچک را همیشه به صورت نشانه‌های احتمال رخداد شدید تلقی می‌کنیم.
🔹
منطقه تهران در این ماه‌های اخیر لرزه‌خیزی قابل توجهی را در بخش شرقی خود نشان داده است. منطقه فیروزکوه تا پردیس اتفاقات لرزه‌ای را در ماه‌های بعد حداقل در حد همین زلزله ۲۲ اردیبهشت ماه نیز تجربه خواهد کرد.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/akhbarefori/652114" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652113">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O36dDzH0LqP3rHRizNNvpIBIapGp587ztVKiJmUAWR6x7n5OqqNLYHCAd5MxJS4ZeXwn2F4Wz72hmFbnJdtucodac5FrADw4ML892L3dXA-wDHF8W6ZJausfcLkDUKSX77EtiY_KmbbEOiNT7nWB7x5RdgSP_2EzDs1-J_oEWBDhjV07DcI9f9bq3V_9oaqnekuWhgBWVGkBwLFaAIJ-8OSvpKGBY8NwjVKzoyXL13jGkcw7pK0tFPgNw52DZY-Twc_otyxCjIaiXVQzA-IelhxQV5p4zK_20QRrm47qVOO08TmV70hC1akqD3SD6SslogeOB4vCm1hXy0zplfPAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست رئیس‌جمهور از کارکنان وزارت جهاد کشاورزی: می‌خواهم تمام توان‌تان را برای کنترل قیمت‌ها به‌کار ببندید
🔹
مسعود پزشکیان: با قدردانی از نیروهای جان‌فدای وزارت جهادکشاورزی از دورترین روستاهای مرزی تا پایتخت و وزیر محترم که از ابتدای جنگ رمضان پای کار معیشت مردم عزیز ایران بوده‌اند، می‌خواهم تمام توانشان را برای کنترل قیمت‌ها به‌کار ببندند.
🔹
وظیفه ما این است که با همه وجود در کنار مردم باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/akhbarefori/652113" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652112">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
قیمت آب در ایران واقعی نیست
🔹
سخنگوی صنعت آب با انتقاد از پایین بودن تعرفه‌های آب در ایران: وزارت نیرو خواهان اصلاح قیمت آب، به‌ویژه در بخش کشاورزی بوده اما قوانین و تصمیم‌های بودجه‌ای مانع اجرای این سیاست شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/akhbarefori/652112" target="_blank">📅 14:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652110">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3_6MAbW6oRNGuKshqMDyUKbwP2rHAwdwlU29U94VwlWk6vVJjTFSQ3LOgLP_oB56bOGQrM67z-eqa0OkZpSUibOXSlHxKCc9du93o4yK7v0fMdYEkOy0Fi_n6r-vy7vq2Y_cWg2Sxohv1WTOlb5nCr1guffXNYk3D2Oi3N9dG5APiAdhXMf23bhztYiMB4GIh27u3uMQ0eJUq6vsQy1eSGc4lw49i9GLcDEIEl_J8CtWLqyDTh85m8iTyNDmw0CXq_BZ9LRiyjCKFxjX-zoXMGvcU_L1_0n7BwDVk_rFpzmYvv3InWmvstC-caZtD2NTHZQyaVGprG1KvjX5Mn5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفر مخفیانه رئیس موساد به امارات در طول جنگ علیه ایران
🔹
روزنامه وال استریت ژورنال گزارش داد که دیوید بارنیا رئیس سازمان جاسوسی موساد در خلال جنگ آمریکا و اسرائیل علیه ایران دست کم دوبار به امارات متحده عربی سفر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/akhbarefori/652110" target="_blank">📅 13:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652101">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cei6DvVJy09YwS8sfVImgD_0iZMShBOHlWYJ3-OfpfheQlsKoRztlcA2veGTzQfJtjaCTU3z0dCvaOyoSP3OdVwaM5Af7fnv0wOWK3xHS9wIxibS-BwArUAElJ0glbBniMy2DyFF_PRcnd1HBiy_3L6tv7bfbZYWI1hh8sYhbnzUYJ9QsjrLFFdf15142fIAW0-tOzD81DiL6QzRwFsuZ_3pdKXWLOsn_-ifcFYuYlxIqMKp8bO4OMeFFZIMAYYY2MiEsHucBbsUpEiJ4yCxFOd4ER4eWJVFVhZGALMueryG-qAyxrKZBNbhBizOwdVX_TthhlWAeyvoN-U3rb7-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8VFkVu4mdiQpcEQoj0Os4N5Z51pZJvRyZYlHPNHBmK5SGhwkQUzh4CGqIAWdydGuUztT0nqqMA80LcwI9gz8Y5zZecAH8vzXXbeo_bxWEkhYyStM2Sg-ggVOL7yOfHhysTKqR18QXlWav7SDiu00kMW6zotgMQVAp18vLNp2vo15t44irR5ofwNYuZOde4Nyl685LIRugnRtIxLznMFWrcmjyEoFV6-uRVenSnb7czW7iiKDglz-w2vi1RNMNBL8wgJWyntZpVIcjMOXJn5Cs4Yi8l0R2B0fBPp8EhQy7-nIsb0PWL9TR18dO0Y-BerSy-jDBCUukGG3lvN5Vi71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAJnQSq1eqevu_SayewdE7QZBvNChVccFh-Q8lFOtOCvXoyRe8A_b6HA1xbIxXO5DYG1l2E8KpTH8SO6SqCtUfRPbxUuMPXduKWqvc9YZKoT1OMA5Rf2HXdCWK1lxlr1hvqRpL5pxKk9Guxly9aT6Cig4ryWY28BkYYBriZiUC8k2kItYVZ8o_1pqN2U2kg7v8oiLeDtEFZgN_WwFYjdbmBqoIm7yANKexqsJl0NPRg6WmCuvULbl88o7ScxVzKs5aAz8FkV-blg9Bzz4GVX8V_Te04AzC1T6fHY3ZnFsKLhProREP2SHO1lxdlLRmmgX6s7XyL53lvEXoYp7-h3lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2OvBIXmBpZHUZwcrNOh-5WLk4U9ckBsK0JdIwZAwIxpNib0i5S3XwZUbx7c5pay6FHCQ1VwqmVGCeKZEVhPk_M5kB0na7vil7TV91AmOre8WlmEfVE6Q29AGr6pQFfhowVfcKekE3YXBktGIC-gm0_Yqkyt-mbfwDAhEGZPbpAIQiPAosPDRbPlEWKDIHKOL5Nyas2EI3FjNtXtTbNlSRBVLUOXoNqC8AO1uHpO_I10fJuLxI9ie6ia4WdaeavDu1y5bnCzxvJPzAwdI3xWFm0QY9Gk78FwrSVY0pQ7C9fW47vdoX75D2S8sJAeQ0PZ7r57he3kCHl5aU3XzoTtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uoXk8Kcu9cABWUoPC0fDBSzsazXlx_Gs_35rUwTmb3Yq3zr4-hAFkP8Si1bbx89XYL2MDZXzoTRPKLSBwIjzzjDGzSuLnHZgSqZZyKiK_HGa1iiZaAMHGATDGPCgMDRg3JQzhA5DFoHkekMbwg-sVfAdscETHGZ3jGUDMmnwY3WQEwrr6NNk52NnqpPx5xR9d-foQicNBwdK0YarXAFq9EmxVU39dtSmc77Np5vMjsp4kBjPrAuPDbVdENz_-ER_kPbeYgrQlCsUky3gribIRU6PmEmEdScNrYm1H64zNL87g065G436B_T8JRGFoMdjOtD2YUZj1YI7VglC-SAh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBIyzMIn0z-SBSiGtALK0p3qRLszJLuaDLIIJJhvx4j8w6gCwnM1OpCORyDeHlxfwsJihNqRj6WnamoA67FM09WDQN-4TqIbuUubzjtiHcy1RdUcei4b1_8FQHuHXFWUqKBOlNtBQeAecmiTyv8249nbgGhPIYlpF4ZB5Aai_zma3xi1Uds9D-opzb7Ove43XvYTqAJm0jhF0fndD9gBZFL1dN2qRVTjd76fUz1FV_3AgwGZZpE6KtMqTuOxe8AqDDKhnnRjofpqkFdnzM8hqSkmPPEAkISEb4RG_itITD0b_aKF-vc4lcRyQVGMTkDel8El5cX_wi5QZ0VU0oQ2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KePhJ5vh4Zz_4ysKGvBI6QFnKBO7Mr1UJJqRrdVigsajUxsIGqoVIcbugFGiDc5mL1aBaVIG094tfxMg1tx5I3zjUW3ozUZCXq-I7NHm-6Vuf9NWPstGC3Jcg4cxGCpPFHv-8kDFKHmvAToGXKTP1Ug2ncRcjdOAHbqJi_R9GKT1gdYFRLF8fIEOSUe8IzzVk4qywR27wJCHzDvULfJWNEMxJ0VOldEMZmLUsjXTOIYcACkVE8ytzVANPJt_FJ9XQP1LKwqny6PH5kJqEnhSD_3IZxheGSVhBuL9nPWnUNsZFRHHf8zuG2cFR7mKc8p0fmje0h5NKLlv8Zi2vK3KVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8C4gL0HVZfmLJRBsAwDkNedbvZ5QImeHOpCeRS-nK7DOH9hEKkHXb-tPpUh1-UFoHyPfgB15n0f7MCQzoQmN5920melu73ue3OFfR4ENia-gFhUWSDMbiYA1t2f8tz0KSeXl139ZO1A6P9wE9g_4CUEjUHm9w2H-Xp9ZOexOKBPRlC4gysWhEyx29sJPPSFMLtDe10XtAmbs_SL5KwTKVy5f91fhi-Xrc-GfsXPDv2A72Bt1oKTvjiT5BaLyw_jjbMDGU97W2CyFBbWXMTKBPPxP0Qb-9T3-AxlE82iyrgIegcgCTd0D0bacb67xYq4cnbYJfRclUZ4bS3yYEv2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAhoW_LwGO-yu4e4LuPS-dI889Z0rNO7z5O85z8oQpMS5yhLfjn3GPGtH_pNGdULOZF0rJIfgspYuL-0evLxOHzeVfIV9-Ot4l8oDeuP4ZJtjF_KgIiZrvCXwadu8hVYX0K_krxYz8pWvRiOK-XkQ2iS36qJMh1f4TZnZAAODddal6XjfrN27-XMwa4Hz5lB6bNNWtIHYAqglFYxCq-mUaAtzXc5WmrQTCAgyrr56D-zRPzqv8SnYqzdSJZjSNtw7wnsPh3qiw5YiO2LuKunboB2pHBEPJOmUaIYjbm2KNXsc9wKmsviFLuj28Hg3R7GBnCqIPdYLVI6kY_6hrUBig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قاب‌هایی از تنگهٔ همیشه هرمز
🔹
بیش از ۱۵۰۰ کشتی خارجی در دو سوی تنگهٔ هرمز منتظر دریافت مجوز از سوی جمهوری اسلامی ایران برای عبور هستند.
🔹
عکس: معصومه کمالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/akhbarefori/652101" target="_blank">📅 13:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652100">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9d2fea12.mp4?token=dGed6nhiL0t6x88kLvMnyuegT06kG3f2zA0bSLmSJt4otxH-CwxOOFFYDz-xoobSqIQx9EI3pr5At3ZkyEL3M8mGcV7OfGAfPVcWOTdbNUuZZKTmimJkiTsIxopLDNeUvASwyoc1IP1HHUV5JO1QqMDDc5au-pu0CvAtFlhuOASovcGMa2niQacL4nBmMFvBJy2G6Xl1P1QWP4R9t0OX7CHv3HH1hekFHFFF86Rbj24uOtSQsJGt3TYSR9akiSqf397konYPC9Vok29btjJtQ8r8TH3IMV4EFw9k5p32i9yluQ2SOVeG5yP2g-P0kFztXRMoquSrtETZjQr_QLxtg2fDiKPmpVNnpFHojq7a4O0soI7dIoKawmY1WYLw-4aP6blUgUa1RDlRC1D7d1PJN1V9d_3-tMpJBrEpiAccP66xG8wO-3JNtdFYAnMhwiD2cJFmu1B9csmEINpbfIJ6nZuvPGGti0GtkbVFKVxAhHyX9QyjNfeWHc9zR42qtxvxnLP8d-OqfYgwwBqPY11_tTo0gA1Hl33Nwp5-Y9w3TZftue6eOZCOpLhjDG4FzGHCUGNIsXxmN95UCoT2Phjn0qqswUU-QSidLtSsoX6-v0METE8G96bgFx5D07FMic0bhVIbfb5ue6b6EfLmUVmqyQ-C3kPhDNdKN4o4hlLdKMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9d2fea12.mp4?token=dGed6nhiL0t6x88kLvMnyuegT06kG3f2zA0bSLmSJt4otxH-CwxOOFFYDz-xoobSqIQx9EI3pr5At3ZkyEL3M8mGcV7OfGAfPVcWOTdbNUuZZKTmimJkiTsIxopLDNeUvASwyoc1IP1HHUV5JO1QqMDDc5au-pu0CvAtFlhuOASovcGMa2niQacL4nBmMFvBJy2G6Xl1P1QWP4R9t0OX7CHv3HH1hekFHFFF86Rbj24uOtSQsJGt3TYSR9akiSqf397konYPC9Vok29btjJtQ8r8TH3IMV4EFw9k5p32i9yluQ2SOVeG5yP2g-P0kFztXRMoquSrtETZjQr_QLxtg2fDiKPmpVNnpFHojq7a4O0soI7dIoKawmY1WYLw-4aP6blUgUa1RDlRC1D7d1PJN1V9d_3-tMpJBrEpiAccP66xG8wO-3JNtdFYAnMhwiD2cJFmu1B9csmEINpbfIJ6nZuvPGGti0GtkbVFKVxAhHyX9QyjNfeWHc9zR42qtxvxnLP8d-OqfYgwwBqPY11_tTo0gA1Hl33Nwp5-Y9w3TZftue6eOZCOpLhjDG4FzGHCUGNIsXxmN95UCoT2Phjn0qqswUU-QSidLtSsoX6-v0METE8G96bgFx5D07FMic0bhVIbfb5ue6b6EfLmUVmqyQ-C3kPhDNdKN4o4hlLdKMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشته شدن پرچم ایران بر روی کشتی‌های متخلف آمریکایی-صهیونیستی
🔹
ماجرای توقفی کشتی‌های غول پیکر با ارتفاع ۶۰ متر توسط نیروی دریایی سپاه پاسداران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/akhbarefori/652100" target="_blank">📅 13:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652099">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ3I9z93ClK_bHlXpdOKT_icDrYGNSxcEyhiT5XrrmNm88qfYqL7mIVLHWUd-NqwZQuR9ecbhJl2cHOLhUvINp5a-mFd-vfSQKufFRLIMJKlINpWWrlyBCrFHcgYdI6qg4n7sBWPla8YaxaMrQF9EfUGbOlJpkWHGrOgurk7hVuf-Zlsa5H3s8MV16c4CYHhsEbebwS5oprZtGKh50KJz6lKwes0jNOYa0lMqyNCQAJFgpYi3uoK7d7HKV9TQHF9vwJNN4NIM39e-E1icD8cbpzCbxjBUBFVYJEr63QxXzLUkE-kuVuX9g2FOSkaTXiRWmtd2jx3TEr4VbLaonMQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: هرکس جرأت کند پا به خاک ایران بگذارد، به‌شدت پشیمان خواهد شد
🔹
سخنگوی وزارت خارجه به شبکه هندی ایندیا تودی گفت که متجاوزان به دلیل اشتباهات محاسباتی‌شان درباره ایران، این باتلاق و وضعیت فاجعه‌بار را ایجاد کردند و درباره تکرار چنین اشتباهاتی در آینده هشدار داد و گفت ایران، غافلگیری‌ها و ظرفیت‌های زیادی دارد که هر زمان لازم باشد از آن‌ها استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/akhbarefori/652099" target="_blank">📅 13:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652098">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yj9EdDoeTBWRMvi2JWPzwtXmdAYx4HmfvT_3vv39H4RmlDS253Q3LIrbaM5QJWwfpSNauNS6U9BDxWY73__pRBG-XcvcX6dXTX8XwHy3sUOA4wM07e7mx9ZD1yytdxZxFrcInC9SwqasAELL3RMXyON8vNcPZVwLDBvfMuPYqr5sgKxOlZ6dKIBdfv7Be6TVyMZ5Y5bQI6Wh35tZyWX_lry5YfX0bP-Bw0Kl7ZJe4dM2iOGPd43XNVdRKv47N80xTssE0SGmr75Cp7doMLAk27OAH3z2lgtu5RGAVbYodduuNP1vq9D-3dh9N2XtXcgPnnUf_X_Yq9ximVQ2pWwuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرزبانان در ۴۸ ساعت گذشته  توانستند ۶۶۷ کیلوگرم مواد مخدر و۴ قبضه سلاح را در برخی از مرز های کشور کشف و ضبط کردند
🔹
فرمانده مرزبانی فراجا: مرزبانان هنگ مرزی میرجاوه توانستند یک تیم تروریستی را متلاشی و تعداد ۳ بمب انفجاری را قبل از ورود به کشور کشف و ضبط کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/akhbarefori/652098" target="_blank">📅 13:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652097">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
انجام آزمون، مصاحبه و دریافت شهریه در مدارس هیئت امنایی ممنوع شد
🔹
محمودزاده رئیس سازمان مدارس و مراکز غیردولتی: تا زمان تصویب نهایی، مدارس هیئت امنایی موجود موظف به ثبت‌نام دانش‌آموزان صرفاً بر اساس محدوده جغرافیایی هستند و دریافت شهریه برگزاری آزمون و مصاحبه در زمان ثبت نام ممنوع خواهد بود.
🔹
فعالیت این مدارس بر اساس آیین‌نامه مصوب سال‌های گذشته شورای عالی آموزش‌وپرورش انجام می‌شود، اما مقرر شده است فعلاً این مدارس موظف باشند تمامی دانش‌آموزان محدوده جغرافیایی خود را ثبت‌نام کنند.
🔹
ثبت‌نام در این مدارس باید صرفاً بر اساس محدوده و جغرافیایی تعیین‌شده از سوی منطقه و استان انجام شود و هیچ آزمون یا مصاحبه‌ای برای پذیرش دانش‌آموزان برگزار نشود.
🔹
اکنون حدود ۳۵۰۰ مدرسه هیئت امنایی در کشور فعال هستند و نزدیک به یک میلیون و ۲۰۰ هزار دانش‌آموز در این مدارس تحصیل می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/akhbarefori/652097" target="_blank">📅 13:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652096">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgpvEgBUWPnSjm1PlxWQnBRfnx05Hg45w4RohaXKx0uqgFdq8fOomXxiOOeWTZo9v4Z6YiVxBz6FICHBnjqYkxTV_zjEfR3gPnSTcOScGNzFw3k2o8S5142cMktZncryF8rUOWCmPJkar4whF9XPsiu1WLLOiDGTRrMyV9CDkVQBVpIN9uoitOkjVZKVvnw3pe0dxHyq7wQhN4Oy1LVYWSPodadNb1kSeqprB3umr_jYWcTRSI9Um-6scWtN3c7d-F0m5CuO93LQpYWZwIFVAPORGberZTiHVvy-4TrBypQmQo35GKNGwP-2aaWZOa4QbNBAISIvoPFGmVtpwd6Bqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تبعات اختلال در هرمز؛ ذخایر نفتی جهان به سرعت در حال مصرف است
🔹
آژانس بین‌المللی انرژی اعلام کرد: از ماه فوریه تاکنون، به دلیل بسته شدن تنگه هرمز کاهش عرضه نفت به ۱۲ میلیون و ۸۰۰ هزار بشکه در روز رسیده است.
🔹
به دلیل جنگ علیه ایران عرضه نفت در سال ۲۰۲۶ کمتر از تقاضا خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/652096" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652095">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: ایران با وجود ۱۵ همسایه عملاً محاصره ناپذیر است
🔹
تنها ابزار آفندی آمریکا در جنگ اقتصادی با ایران محاصره دریایی است.
🔹
خلیج فارس با حدود ۶۰ درصد از ذخائر نفت دنیا و بیش از ۴۰ درصد ذخائر گاز دنیا مهم‌ترین منبع انرژی جهان است.
🔹
در جنگ اقتصادی بایستی دستگاه‌های متولی اقتصاد آرایش جنگی بگیرند.
🔹
ایران با وجود ۱۵ همسایه عملاً محاصره ناپذیر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/akhbarefori/652095" target="_blank">📅 13:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652094">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8E0XguDzTHq8-5lQSpiIJ_dcLu0BgkkgHebWlF2I9CHJk0CegD5Q98X28w1Cz2cUJySk_XbmuN4-xdr2b5WsekP6fAFnoBcfUxa91b_309gRsNKPEEgEAcAppl6IuLTDEfDy0E6q8pY9c7hNfLHKo704aV9MVEsY1mgi7GbsEErtHN-PjuL8DWT4TUtkyJkaWEDYTf0YhxfImVtoKFCr1wgYgp0GnR-cyp80Je_GQTV7p9ax3y_MoLWXfv_Bd3fsKPwpBgVjf6DdGS_n_NppaY5ldOxlSZ0UpFH0WLnxZhWATs83JzQvNtLlhcpb13996Otm5Y4HmerIjs82BczqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کاربر فضای مجازی: بعد از اینمه فشارها آیا برای بعد از قطعی اینترنت پرو، راهکاری هم برای کسب و کارها دارید؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/akhbarefori/652094" target="_blank">📅 12:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652093">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
۲۸ نقطه شمال تهران مورد اصابت موشکی قرار گرفت/ ۴۵۷واحد مسکونی آسیب دید
🔹
شهردار منطقه یک تهران: در این منطقه ۲۸ نقطه اصابت موشک ثبت شده که در نتیجه آن، ۴۵۷ واحد مسکونی با آسیب‌های جزئی تا تخریب کامل مواجه شده‌اند.
🔹
۱۱۵۳ دستگاه خودرو و ۸۷ دستگاه موتورسیکلت مردم عادی آسیب دیده‌اند.
🔹
در یکی از نقاط اصابت هشت بار انفجار رخ داده و همچنین انبار نفت نیز هدف قرار گرفته است.
🔹
در اصابت محله زعفرانیه ۲۸۳ واحد مسکونی پیرامونی نیز آسیب دیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/akhbarefori/652093" target="_blank">📅 12:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652092">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
همه بانک‌ها مجاز به خرید و فروش ارز تا سقف ۱۰۰۰ یورو شدند
🔹
براساس دستورالعمل بانک مرکزی، هر فردی می‌تواند تا سقف ۱۰۰۰ یورو (یا معادل آن به دلار) در سال، ارز اسکناس برای نیازهای ضروری خرد از شعب بانکی خریداری کند.
🔹
منبع این اسکناس‌ها، خرید از صادرکنندگان است و کاملاً از منابع ارزی حواله‌ای که برای واردات کالاهای اساسی و مواد اولیه استفاده می‌شود؛ جداست.
🔹
بانکها موظفند ضمن الزام به رعایت سایر ضوابط و مقررات ارزی در اجرای این بخشنامه، مراتب را به تمامی شعب و واحدهاي ارزي ذي‌ربط ابلاغ و بر حسن اجراي آن نيز نظارت کنند.‌‌‌‌‌‌‌‌‌‏
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/akhbarefori/652092" target="_blank">📅 12:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652091">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
۴ شهید در حمله هوایی رژیم صهیونیستی به لبنان
🔹
منابع محلی خبر دادند که در پی حمله هوایی رژیم صهیونیستی به دو خودرو در جاده منطقه «الجیه» در شهر الشوف واقع در جنوب لبنان، ۴ نفر به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/akhbarefori/652091" target="_blank">📅 12:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652090">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8176e013.mp4?token=Jg09XGaIg8IotFvjftMi7mWwML_XeGjzaRwf83fkJT8jhWrKRVdgyKfmEYrQdwK1MSTY8bb7qa6mYHSI95uvdbkTiBADVo8sTN1s9LCF9ofuwoO6JZdmESHfxJ__oWnE8zpYO_MOnfCwJcO_8yPXDURC8GepXiROMUUicfQNQGLsVFQCiuuQEAvad9Iiu9CAsTXjzQhzuU3AL9vJGcPueXGG3EjuxCw7wYv2avUZ2Q8ly3hZkakhBqV2_8cIkWAshjVDMRB9cZimcMz7zfcEn4pJmkBejMn4S5Vp0cT4EnLza_eaODPcwfssYYneEZheOmjwhJOpwItQuH8HDf17iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8176e013.mp4?token=Jg09XGaIg8IotFvjftMi7mWwML_XeGjzaRwf83fkJT8jhWrKRVdgyKfmEYrQdwK1MSTY8bb7qa6mYHSI95uvdbkTiBADVo8sTN1s9LCF9ofuwoO6JZdmESHfxJ__oWnE8zpYO_MOnfCwJcO_8yPXDURC8GepXiROMUUicfQNQGLsVFQCiuuQEAvad9Iiu9CAsTXjzQhzuU3AL9vJGcPueXGG3EjuxCw7wYv2avUZ2Q8ly3hZkakhBqV2_8cIkWAshjVDMRB9cZimcMz7zfcEn4pJmkBejMn4S5Vp0cT4EnLza_eaODPcwfssYYneEZheOmjwhJOpwItQuH8HDf17iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابعاد گسترده ویرانی‌ها در پی حملات سنگین اسرائیل به «برج شمالی» لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/akhbarefori/652090" target="_blank">📅 12:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652089">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxSGvZX8EX3CMLLY99EhkbAVRrtlaSuoTzRGmp2fiK54zQCKQqZuvIFmX3rgxWsQeyRDmDHDSQQn6joOu7fLjNPf9-r6l1Qckc1_KXj1VHDg3m99y5CpzdGX1xPqVZanomqtUkkLa8f83dwo7FR87Ko0z2FWe-rx3BTNzobJUF5YEKluUb92CTTXcwQp7PZqEV5sxXokrC_abZcCI_eZ9PZRlaqas6ww1bwoFrqhMvYOUgocRXykA2NURM1LjkLgoh0qzJrTWIuZFKCjFAuUYZ8XG59TV-PC2Lux7WvKgqePnA4XBFOINMrMP0TnbTyV3u2vlV60XPEAo9hpisSy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاستیک کمتر، خرید بهتر
🔹
با انتخاب‌های ساده مثل کیسه‌ پارچه‌ای، ظرف چندبارمصرف و بطری شیشه‌ای می‌تونیم مصرف پلاستیک رو کم کنیم و به یک زمین پاک‌تر نزدیک‌تر بشیم.
🌱
شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
…</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/akhbarefori/652089" target="_blank">📅 12:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652088">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIcRJLZyeBmHm5DLY4HCeCxPo5pP-ANBxqSbTh-GUu9ygzYgQ68XIYCxK_0ZDbNBrW4DvThtaZ4smcMAFOZdERuwz2kLtsEkQ7BaHmoZEFltbOtir-c9bQhXniSvl5dcngJykC2V0-e3FLgftVszmLulQZVVeiONaZcD2Td-cWNgPJ4awsg201ZUx1mfs_EqizrGy1lTL-we9kTHKU6euCCNsVJpN20ziyLVQYX2ZArf27wxm1GhB7pbcQuzmM12pQLX_5BYiD6Wwlq7Z43EhAGA3RJCM1ImiV8L87wxJLrZmSGC7YceHug9KZkPjm-hgPUE29dyZlTnN7ORomjF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دعوای مجلس و مرغداران بر سر مقصر گرانی
🔹
نایب رئیس کمیسیون اصل ۹۰ مجلس، وزارت جهاد کشاورزی را دربارهٔ گرانی مرغ مقصر دانست که با وجود نهادهٔ کافی، جوجه‌ریزی کمتری در فروردین انجام شد و تولید را کم کرد و قیمت‌ها تا ۳۹۰ هزار تومان در هر کیلو بالا رفت.
🔹
این درحالی‌ست که اتحادیهٔ مرغداران، کمبود و گرانی ۵ برابری نهاده‌ها، خوراک،‌ واکسن و دارو را مانع جوجه‌ریزی اعلام کرده که تولید با هزینهٔ گران برای آنها صرفی نداشت.
🔹
بر اساس آمار اتحادیهٔ مرغداران، جوجه‌ریزی مرغداری‌های کشور در فروردین ۱۰۶ و در اردیبهشت ۱۲۶ میلیون قطعه است که این میزان افزایش جوجه‌ریزی ۴۲ هزار تن تولید مرغ را بیشتر می‌کند و نیاز ۱۷ میلیون نفر را در ماه بیشتر از ماه قبل تامین خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/akhbarefori/652088" target="_blank">📅 12:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652087">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
هشدار چین به آمریکا در مورد فروش تسلیحات به تایوان
🔹
چین امروز و پیش از دیدار ترامپ و «شی جین پینگ»، بار دیگر مخالفت شدید خود را با فروش تسلیحات آمریکا به تایوان اعلام کرد و از واشنگتن خواست به تعهدات خود در این زمینه عمل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/akhbarefori/652087" target="_blank">📅 12:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652085">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBfOCtZDrtZfWZ0TYmgR4vzenQc4DtV2gVpJ4kEchdxRZ1-3Z-pRd--m_MmQgf5PKSPx9tEIP2Qro_WJW5J9RCpm0ee6gBqoETZIS8RAIDgxtXdYVTA6-0kyllJjxl0Jkudu6upU09_uXDi6QOl99KOMtC2zbBesyWXrpWHciUNIDafG08pZ-a2yoe5oE1ykRHrMAVvAyTASKi9HsnAw978f5lUG3W1sYUsbuQ81KrtZMrk8Q4vBhQIbz_dDUBEodde7vfmClTirIIRO8_QcTpBxb0DGr-B49anmjeUnCKv8FkfSrGNNCIiA9yqszPq-tFaa3kgy7VUwO3x2bdlkRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uya0lzq4lzvgXyEERnK7EPfbCoOUFB3Kg5QSCLViNu7k0tfnVOAFPHAppGnSZ_fkUsYaj44sGPsG4ETKq15UR0dJxWlNvn5fDMmVRK3euHVNeyeq1cpq3PKg1F4bH_QqhY1aH_tYQKUFAaAjQ1alChWSbtd6Hvvulep2cpbVKcW0ALMW4mbENrBTRNWgF4BoGiXXWLPPz3fhxzh82Rpy0EAm5Vfsf3kTH6zRI0j8Tfr9-hFpRt4Hk0-Ojzr6Hijazsl8m7ma2KPgwfakj882kQz3APaswYZlCD7HODpcG843BfKoRqYj9wlPrZu94oev7T8i29WIhoOW578M1Fuosg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تداوم نقض آتش بس؛ حمله جنگنده‌های صهیونیستی به دو منطقه در جنوب لبنان
🔹
جنگنده‌های صهیونیستی لحظاتی پیش دو شهرک یاحون و برج الشمالی را در جنوب لبنان بمباران کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/akhbarefori/652085" target="_blank">📅 12:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652084">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36bd0aa3fe.mp4?token=NyZ1Sqyb9qp6v8j9B0tuB-d7l2m6CMGIUqhyl6pCRFoAMgfg3qJ5dBQt9ndu-pXvJ0xY_8rM4dY61UVCQwGSyD17UfJVh-MI3tY_QgI_fT_edJKRommDZEIYzQ_KnhYsR5DU8OLfTUPA2G4qDW4qlf9FrWdi3cjRJDSKBrb0ISiAuto5H0Isj0u2GatoJjJqJ_7DmfPxdlaaaaYXGkzNiMVlmw6npIF3OdZassf_0knL133jch6PWyCaHXZuJt1a1lSqAyf3B7eEzr2BgHEPHfV0tC48z85UcW-TBaoNNUZPxx5nyPdOHFF2Bx4yQmc8E3Af7yo8zFmrijoEsrYXQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36bd0aa3fe.mp4?token=NyZ1Sqyb9qp6v8j9B0tuB-d7l2m6CMGIUqhyl6pCRFoAMgfg3qJ5dBQt9ndu-pXvJ0xY_8rM4dY61UVCQwGSyD17UfJVh-MI3tY_QgI_fT_edJKRommDZEIYzQ_KnhYsR5DU8OLfTUPA2G4qDW4qlf9FrWdi3cjRJDSKBrb0ISiAuto5H0Isj0u2GatoJjJqJ_7DmfPxdlaaaaYXGkzNiMVlmw6npIF3OdZassf_0knL133jch6PWyCaHXZuJt1a1lSqAyf3B7eEzr2BgHEPHfV0tC48z85UcW-TBaoNNUZPxx5nyPdOHFF2Bx4yQmc8E3Af7yo8zFmrijoEsrYXQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی معاون وزیر بهداشت با هانتاویروس و تنگه هرمز
🔹
رئیسی: کشتی کروز که هیچی یک کشتی بادی هم نمی‌تواند از تنگه هرمز رد بشه نیروهای ما سریع می‌زننش و هانتاویروس هوا میشه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/652084" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652083">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
رئیس روابط عمومی وزارت بهداشت: ۴۰ هزار نفر در جنگ رمضان مجروح شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/akhbarefori/652083" target="_blank">📅 11:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652082">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
مدیرعامل یک مؤسسهٔ‌ مالی با ۱۳ هزار شاکی دستگیر شد
🔹
دادستان مرکز استان کهگیلویه‌وبویراحمد از بازداشت مدیرعامل یک مؤسسهٔ مالی به‌اتهام کلاهبرداری و فعالیت غیرمجاز خبر داد و گفت: در این پرونده بیش از ۱۳ هزار نفر مال‌باخته شناسایی شده است.
🔹
این مؤسسه در ابتدا مجوز بانک مرکزی را داشته اما از سال ۱۴۰۲ بدون تمدید یا دریافت مجوز به فعالیت خود ادامه داده و این تخلف با گزارش پرداخت‌های گزینشی احراز شده است.
🔹
براساس نظریهٔ اولیهٔ کارشناس رسمی، ماندهٔ اصل سپرده‌ها حدود ۱۶۵ میلیارد تومان و مانده تسهیلات پرداختی در اختیار اشخاص حدود ۸۵ میلیارد تومان براورد شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/652082" target="_blank">📅 11:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652081">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDqd-vl4mIr-oIhgWNhRfdAFRY2Gsdzj8lsxma_WkScknrJ02FwXqkGk1SjEw6X6an7747ZNo19zLODWKpXD3qH7UzWPdBtRCoqgyqcD86FH6xLd4CsqvNGoM-SwwFoyMshBNJO-uebTk9rGmsAJecF2-dHtldqxAWUZl-Q1MPch4hd0lPpxq0hbcQW6mAEp1t--ssMgbJbx95PX8E0_2lGGRLb1Ldi_OISA_Gdb2t6BJnoq-k1J2IL7XM4RFo7cVCwvCv6iB6sg-12sY0_Lqrkr3Z0x5WwmIy7YVsLHmR6ViSxcTB827ynIAtwknC5lwL9k49V9J0r5C6cgDA7ClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: ایران به ۳۰ سایت از ۳۳ سایت موشکی خود در تنگه هرمز دسترسی دارد
نیویورک‌تایمز نوشت:
🔹
اطلاعات آمریکا نشان می‌دهد که ایران قابلیت‌های موشکی قابل توجهی را حفظ کرده است.
🔹
ارزیابی‌های جدید و محرمانه می‌گویند که ایران به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز دسترسی عملیاتی دارد.
🔹
طبق ارزیابی‌ها، ایران هنوز حدود ۷۰ درصد از پرتابگرهای متحرک خود را در سراسر کشور مستقر کرده و تقریباً ۷۰ درصد از ذخایر موشکی پیش از جنگ خود را حفظ کرده است.
🔹
گزارش داده‌اند که ایران تقریباً به ۹۰ درصد از تأسیسات ذخیره‌سازی و پرتاب موشک زیرزمینی خود در سراسر کشور دسترسی پیدا کرده است. /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/akhbarefori/652081" target="_blank">📅 11:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652076">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flroLY5Lf0HxGsQj9R1zAFL6bv3chLgD9fk-HHw2rETXHqT4s_7IBfdsXSsAPQ2b8Ab9ppgHo8VveNfun6ttjcSjFBHV_CNgwpfIKwdU0mPXkIRTZhCWZv1nbAKMTBKaQ9rIXwe4jLVfFeEYU9ct-9066ZapXwRq2NXB3JEEwPQ68Ijp0_f1e8hzWC1fyCsVLRTGCtWMQ-3Zz-vl6D4Pbcd1AD-lMIc-GUIRg1dmwicWa7MB7mK1UN_ecdqNGzgbIkpVUSKozUCebyfbx_ekgp6H8PYPlCkVZ5oI_FKB7N4VcMzfzvfJBcrgoZvu7KhKnV1U77nSc2aXLZLYop73gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_fl7CnVC8rfLyOZLhOyeAlFmMKnxzYzYQmUX10kIaZ78gMMALvpIkjuyKIWuaZsZIutIHf47eKYzISMUSjbAcV-c1NGxhoC9IXF66QYrCu6bn4QHObIf78YMSn4XX0fact4Tu7tUJ7zdl0CKorLEenEXV8QKF2pDG0PXJbH8SzPd6HSzebgoiOrDWNgf-liv7tsDyOuN34iS8QuNENSKt5uZsvoVSBU-ltkfRdnIPcC54ftDVBTuIJiOD82XGbXImMaMaKWBFjO0H6JSmliA8yF2R93YrYrkSqbmCbRR4rofR6YLLKj6zsB-IjJ54wUG2C5kyXKnihNEsuewKGJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIRThvVD-Piy6pU0COZhqGYhrXoeKdU4VGKOheGDECGxe3-VX7RUWyU2XHzAB84BodYQOb4kSG8VUHwFa4TBwIpUCiU8_VPEw7YSSg1wxXtzoU0dHL64_aPuDwWK1Ze7CGRNyA-9i3p_YWSh67XhG-QOdldc8KJaBKAs2Popaxr_V7c8adAXOTAkaHz_Qhn6Ow5JscLJyFYiYo3rjLe6YRUk4ZSvtNb6YgyNRM9229limRt7J8DNf4JIXZ-o6B3ih8YM9a4OHqZuvjZc_qPSuUqzka-H35N7ZCQwimkzRCKhRNMha0kR7kK8aC50DUiqTKDgfg05GhHehMQsauII-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3q-VwZq6m760TCVtv9Ixk6QjFhXywkTy3QLNdyuBuU6gFvbeDVuaeD_4FneIV_2X8AvyZA20hrpPODVWDENLmliYDDViojC4BUGwBIxg9gxpwuxsHr6nFqcBy69EigYHN6DxqG03uygBOdGJ_xh53wgPVrTt_cXFoxa7Ukjp1qTAbrL-y1SzI8Gm_CBWCyY6anPKM1s3oNlney3P-YcbBgGmkWripM3UYGSIJVpV9z6OUett1jPoszusValc6mib9bRhvQJC7aaXtl1tU2hRVpQWUNN373rnU7KMaPm3XRwa7VGKU-6y_Lybcb5678iJBGDAiQzFVlqj_zFx_jjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dd26kMrG_JeCmuMuZZuiz1w7U8oirKf_1X1QpTP_AKbVNBU5o6SW96s9hbbiS3fOHpQUJcixukP3gwEm7NQ6rlby3fIESCQWM0Se9jJnYvevo9CAWBAtH8W34ZsxGwRtmoFlWH3y01nxHHNLJDuniFuoQyWfCC-aBMinbI7BZ9fmeG6R11ln_5utVcAnjtqLGSmmwH4BpdWATCT-oD8HqtJP_N8VwXiqSp5uKMDM-CgtArppTTs_gwMZF1EiSvlTdku0iMs_5UzUs4g27HnR7-GUoK47j4c2rH-auW83_YbINWXKaC30T_Vor95cT_sGNHc-F5f1HVm6fzIAjiomvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انتشار فهرستی از وطن‌فروشان خارج‌نشین توسط گروه علاج
🔹
براساس اعلام گروه علاج این افراد از حملات رئیس‌جمهور آمریکا به ایران تشکر کرده و نسبت به جان باختن برخی هموطنان ابراز شادمانی کرده‌اند.
🔹
علاج خواستار اقداماتی از جمله توقیف اموال، تعلیق خدمات کنسولی و سلب تابعیت این افراد شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/652076" target="_blank">📅 11:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652075">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv6H4DyadBBBSWIKxV-sf8nbndsB56hwIdjzpydf-6V3Bh6_jKnldUbUMlyZ5-qd9ZKfr9QrmdSd_mku-D1_MziwsflMI8k9FD4aAPNu-tDTOidmaqtfSV3obrVX6__toL9VGjMrJyAnWe60f-ZbAP23LeUcsSwELTSgICAKlg3YS2Bav0ApIRZ7sOSJLezRE1kkDdM6oy1s-ODEeJz27S604InyJO4G5ugbF5P83JNIcv9hyHJxGXVqhGF0MpKCLYZyyYh0eXiooQ0VkokyjlhC_j8Xzp6uBrjqUJ-mE2K2Z2RSevPsQSztg4pFn8MyPWvTccU_jZxYEHENNUaEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار ۴۰ روز جنایات آمریکا و اسرائیل در ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/akhbarefori/652075" target="_blank">📅 11:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652074">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207f1553c1.mp4?token=ajeQ4bvgBx1LtSy2bSAxmy4aBjIStloGoBUTdQcOg4ebnmW_HGPXz-UFqXwAmRGtbEwyDgh_mut58mWPmQhdZkGZ8prCuDtyr3WIaB-0z093XBkPDXZoEocifQhokGgyKMRqjlXKad3Dp9ZU7lBQNJKJD55kZ6Pb8B5iAQm778YcUCtZOpYOJ3JsZIfaoVsFumJjsa4TXS3CTU7f6sIAv2ffENrsQXXWHMmCtuRtuhZd-iRwyN4WbgoLOVbqthJ_V96ReUU5LTuKCRdDuWCRfzAHPsfXBbwCxP8li4pahInpBXlOxC33S8pOR5omp1BpUCQZjew9bAExIDWNglt6UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207f1553c1.mp4?token=ajeQ4bvgBx1LtSy2bSAxmy4aBjIStloGoBUTdQcOg4ebnmW_HGPXz-UFqXwAmRGtbEwyDgh_mut58mWPmQhdZkGZ8prCuDtyr3WIaB-0z093XBkPDXZoEocifQhokGgyKMRqjlXKad3Dp9ZU7lBQNJKJD55kZ6Pb8B5iAQm778YcUCtZOpYOJ3JsZIfaoVsFumJjsa4TXS3CTU7f6sIAv2ffENrsQXXWHMmCtuRtuhZd-iRwyN4WbgoLOVbqthJ_V96ReUU5LTuKCRdDuWCRfzAHPsfXBbwCxP8li4pahInpBXlOxC33S8pOR5omp1BpUCQZjew9bAExIDWNglt6UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر بهداشت: سیر نزولی جمعیت‌ها ادامه دارد /  ۸۹۲ هزار در سال ۱۴۰۴ تعداد متولدین ما بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/akhbarefori/652074" target="_blank">📅 11:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652073">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OarH9fEf2KT9c3AEB6jqmcegpHhcW4LZD5kCR85rs7LcmLyQIl88-PL5FUzg_VS0477AHgXNyIr95fsUairOqJYu4PWGuqNE0babToIYL9QKnBYwe1CB7H-NsUgzIOKPQco5nKVTvlCCb-edmw-ARwxoFcmNTzwseXGoIBFz7QU8mmdmBZgY_ItstMZwVo67FzAgkWj9WPfgnK-cbaA3co4k38xr_1xiiYDh2QTyKGFboMFZUFmbGZY5LtNBn4fwauAvt3bYsn6NuqiXgYb5Kooa5LuDwpjtqYLJy8zSXUrjoFyeos5KrnOy9oh5njodyJNkheYLTZw_PHHxHIF_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاوروف: تهاجم علیه ایران با هدف جلوگیری از عادی‌سازی روابط با منطقه بود
🔹
وزیر خارجه روسیه: شکی ندارم وقتی این برنامه‌ها برای حمله به ایران از سوی اسرائیل و آمریکا انجام شد، یکی از اهدافش جلوگیری از عادی‌سازی روابط بین ایران و کشورهای عربی بود.
🔹
در دوران دونالد ترامپ، مقامات آمریکایی حرف‌های درستی در مورد همکاری با روسیه می‌زنند، اما در واقع، واشنگتن همچنان سیاست جو بایدن را دنبال می‌کند.
🔹
ایالات متحده خواستار باز شدن تنگه هرمز است، تنگه‌ای که قبل از دخالت واشنگتن، در واقع به روی کشتی‌ها باز بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/akhbarefori/652073" target="_blank">📅 11:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652072">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5575ee58cf.mp4?token=RdkB6xBlwA2aX24c6r6iIMHshhmyw-Ln11l2TfKFGwSZkjVpH8ziLTc99_jVlBRbl25QN2jHd-VyOz3X9bE2d83AT-kr7fP56xHpL_Szjy1NAf0QUq8PRQtlWFHqNNYY73eBpUXLbH7dC7qRZ03KCA33elG441L5HifQbe9GizyjBawZbpjzxPOAl1C6cMSY9Esw_s5fPKazhE341L1WiFQ0CZiaGKnAsln2LvzIaHqfjsUtHTWzuCPvuqKrOqLl9m9r_DYV-Uax8XKp46stNr3jedShYW2NzCHFksxGaPjj3d5e5JFdpWedxpMMqgjmQfzlieEXRy2xYcQbyhcsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5575ee58cf.mp4?token=RdkB6xBlwA2aX24c6r6iIMHshhmyw-Ln11l2TfKFGwSZkjVpH8ziLTc99_jVlBRbl25QN2jHd-VyOz3X9bE2d83AT-kr7fP56xHpL_Szjy1NAf0QUq8PRQtlWFHqNNYY73eBpUXLbH7dC7qRZ03KCA33elG441L5HifQbe9GizyjBawZbpjzxPOAl1C6cMSY9Esw_s5fPKazhE341L1WiFQ0CZiaGKnAsln2LvzIaHqfjsUtHTWzuCPvuqKrOqLl9m9r_DYV-Uax8XKp46stNr3jedShYW2NzCHFksxGaPjj3d5e5JFdpWedxpMMqgjmQfzlieEXRy2xYcQbyhcsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر بهداشت: مسئله جمعیت از جنگ مهم‌تر است
🔹
رئیسی: اقتدار ملت است که روی آن تکیه می‌کنیم؛ شهدای جوانی که پشت پدافند می‌نشینند با اینکه می‌دانند شهید می‌شوند باز حضور دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/akhbarefori/652072" target="_blank">📅 11:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652071">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0797785fb.mp4?token=WGwKCaq9EWkMTsHrkXXf6bnW1O8M4qhXn-gCsqkKXj70hATxT_kxUeewgQHglp5ynuqEjH3EbumbDNl257GtMwLNIspigf-d8ldWWjyhMq-CdyQ9IaxqBVljrJ0JIWblCHA4qtpRRQczA_kc9lo8lEqfEzN32KKizFhHIaTiQ2vu84RB2RiTw8rApCT8-VKxZKQES2Nzo4CDFQm81StYYjFyhJFE-G-qNC6DzL2YAKKqspz0vLHylQbkjbe_xxjOJ9tzDXercBNNSZiI1GGHyfz8vcRaHVqJsjqX5Zwl-Zj6eGwnZ5UOw6MKsoWKopQ2sPxEUuFiyDXzGS72Zpoz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0797785fb.mp4?token=WGwKCaq9EWkMTsHrkXXf6bnW1O8M4qhXn-gCsqkKXj70hATxT_kxUeewgQHglp5ynuqEjH3EbumbDNl257GtMwLNIspigf-d8ldWWjyhMq-CdyQ9IaxqBVljrJ0JIWblCHA4qtpRRQczA_kc9lo8lEqfEzN32KKizFhHIaTiQ2vu84RB2RiTw8rApCT8-VKxZKQES2Nzo4CDFQm81StYYjFyhJFE-G-qNC6DzL2YAKKqspz0vLHylQbkjbe_xxjOJ9tzDXercBNNSZiI1GGHyfz8vcRaHVqJsjqX5Zwl-Zj6eGwnZ5UOw6MKsoWKopQ2sPxEUuFiyDXzGS72Zpoz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم نقض آتش بس/ دومین حمله پهپادی اسرائیل به جنوب بیروت در کمتر از یک ساعت
🔹
منابع خبری از وقوع دومین حمله پهپادی رژیم اسرائیل به یک خودرو در بزرگراه ساحلی «الجیه» خبر دادند.
🔹
این دومین بار طی ساعات اخیر است که پهپادهای اسرائیلی خودروهای عبوری در این محور مواصلاتی استراتژیک در جنوب پایتخت را هدف قرار می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/akhbarefori/652071" target="_blank">📅 11:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652070">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0412efd61.mp4?token=qMq5JxwYF9B3Md-XGM42KjiyCSE_HR1nxOAh2EXv45yqG9yJNu5jbgp0IE9oVGv5zw9JPPyUeR7njSYOHiue-GPIsClGyvf3SqLmelAGJ0u57CNhlRbNGJnjsxgMdiO8rbwNTqTONv6mokRAFsLfsLLRCkvV8pjaOuiW9Ngphg4NIquTr9ViwxjHSKkQPFIZ1zNRSq0H2KdIFbwJU7Px6-F4jnMaGP0qF_hbr-WXEOnye9XODRHdOv6fRpjU2uLWeI1pDFyfc1hyBJAzB0UAZ2yyyfn5vBtUeSbr9PWtQspjTNC0Ffdbe-kCiB1xj1znC5XTKATj8qb6PU7fl2t1cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0412efd61.mp4?token=qMq5JxwYF9B3Md-XGM42KjiyCSE_HR1nxOAh2EXv45yqG9yJNu5jbgp0IE9oVGv5zw9JPPyUeR7njSYOHiue-GPIsClGyvf3SqLmelAGJ0u57CNhlRbNGJnjsxgMdiO8rbwNTqTONv6mokRAFsLfsLLRCkvV8pjaOuiW9Ngphg4NIquTr9ViwxjHSKkQPFIZ1zNRSq0H2KdIFbwJU7Px6-F4jnMaGP0qF_hbr-WXEOnye9XODRHdOv6fRpjU2uLWeI1pDFyfc1hyBJAzB0UAZ2yyyfn5vBtUeSbr9PWtQspjTNC0Ffdbe-kCiB1xj1znC5XTKATj8qb6PU7fl2t1cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر بهداشت: ۲۴۵ مرکز ما در جنگ آسیب دیده است
🔹
رئیسی: بیشترین سهم مراکز آسیب دیده وزارت بهداشت را کرمانشاه با ۴۸ مرکز داشت.
🔹
۵ نفر از همکاران ما در جنگ شهید شدند که یکی از آنها مادر باردار بود.
🔹
کمتر از ۴۸ ساعت در تمامی استانها همه مراکز آسیب دیده جایگزین شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/akhbarefori/652070" target="_blank">📅 10:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652069">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
اژه‌ای: هدف اصلی دشمن؛ ایجاد تفرقه و ناامیدی است
🔹
رئیس قوه قضاییه: انسجام ملی؛ اصلی‌ترین سرمایه در جنگ ترکیبی است؛ هدف اصلی دشمن؛ ایجاد تفرقه، ناامیدی و فرسایش سرمایه اجتماعی ملت ایران است.
🔹
امروز بیش از پیش ضرورت عبور از رقابت‌های سیاسی و اولویت بخشی به همکاری و مسئولیت‌پذیری ملی اهمیت دارد.
🔹
امروز؛ نقش مردم در تبدیل تهدیدها به فرصت‌های پیشرفت و اقتدار ملی بی‌بدیل است، ظرفیت‌های گسترده دینی، انسانی، طبیعی و اقتصادی ایران برای عبور از شرایط ایجاد شده از سوی دشمن کم نظیر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/akhbarefori/652069" target="_blank">📅 10:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMpBQVAoLJgLXsZJyCzPsMaCbp5xZtdTN5pYKEBhlew9XWay6YRaRuCVvE8JAjo-c8Z3Cq7_7079gOU1lTSKN1TWJWMZgnpdZtBNR5Y_ngddsYrg3lDcuSTKnnp_U4Hyh5hWdy1ovQhH0frOWJRkf4xtDm88EGK-_OszpuArhGKBX6xGWKS7yLLJdO0VRdNvKPoplQz-IiiHTUdFHVSA_7LqVyc-6FO_N5zFG9WkLlXu4cosFsiT6hiYkGbPJd3mHCdpl2aGfnxpd3ZVUFjnCoJNG8nGX1n2IJ0tMNDLV3LYvHaaJpaZOWS4wKt6s8UMtPd_1Uv_nRXHVgoiBJmzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تدارک صهیونیست‌ها برای برگزاری راهپیمایی تحریک‌آمیز پرچم
🔹
رژیم اشغالگر صهیونیستی در تدارک برگزاری اقدام تحریک‌آمیز «راهپیمایی پرچم» با حضور حدود ۵۰ هزار شهرک‌نشین در قدس اشغالی است.
🔹
این راهپیمایی از بخش غربی قدس اشغالی آغاز می‌شود و با عبور از باب‌العامود ادامه خواهد یافت و این راهپیمایی معمولاً با سر دادن شعارهای نژادپرستانه همراه است.
🔹
اشغالگران همچنین خود را برای یورش‌های گسترده به مسجدالاقصی آماده می‌کنند. پیش‌بینی می‌شود تعداد یورش‌گران از رقم سال گذشته که ۲۱۰۰ شهرک‌نشین بود فراتر برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/akhbarefori/652068" target="_blank">📅 10:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652067">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf1f551d1.mp4?token=cfKiAgOl1-H5Sduf2_LCuzrjKNZciOEzHwH4SHw8VHKWgTXV2JafZpILj8slZJz0gP81PHzUK6gRqL7HxaSJgINk9XbjdW7C-e09LZh4nQ1WHjqrzfGfedsAzt99BQeSVBL8vz1s4MZ5hLt1yZo7IJHsv9vYNTPECUgyhYGrsj_aUywvMhYjSL99W8nR9dwDsS_058nZH31Oyh8d6Dd6GhZELQWJgApX26CUYITedKgkJqS3Q3DMcWCvxVJXPnTXxV0mTMC8OWd5iwmn1t70O_SGQ9b2ATJaNiFthKQGfxfSq8_MT6UuDqJFZQSeUWhyMTVtlI6fUYT1lLeFCNk7mKk0LQpMgeASIg1_k7Mav3e6Wyz2sidWa2mARy_qQNRTMtz-3UP-CjvNMCgJlI-ktidZZLjymiCaVkdF6dzUzInUNmzHPTVfYPI14Jzpkn7ZRXkZGpFgNiL8soHMaN7BS2mbcMEnHg4jgWuOByQATWfInXlAztYNbqUnvOSEkdEQEhpenFwt5hw2q61WZfGQJA9mmAQgvhrH5AH_ACZBv08uOaxSmd7uCCkpGaVyq_bZbJ4FAbIKca6ILPlAapdKYEHhGhxmO6ouh8nvM6QdevcZc_iWip-v4Dknr5xUTTlJB2auIIOFMuGGW7qsnmwqMJl3QkYERhTZjy_rXb2EY2s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf1f551d1.mp4?token=cfKiAgOl1-H5Sduf2_LCuzrjKNZciOEzHwH4SHw8VHKWgTXV2JafZpILj8slZJz0gP81PHzUK6gRqL7HxaSJgINk9XbjdW7C-e09LZh4nQ1WHjqrzfGfedsAzt99BQeSVBL8vz1s4MZ5hLt1yZo7IJHsv9vYNTPECUgyhYGrsj_aUywvMhYjSL99W8nR9dwDsS_058nZH31Oyh8d6Dd6GhZELQWJgApX26CUYITedKgkJqS3Q3DMcWCvxVJXPnTXxV0mTMC8OWd5iwmn1t70O_SGQ9b2ATJaNiFthKQGfxfSq8_MT6UuDqJFZQSeUWhyMTVtlI6fUYT1lLeFCNk7mKk0LQpMgeASIg1_k7Mav3e6Wyz2sidWa2mARy_qQNRTMtz-3UP-CjvNMCgJlI-ktidZZLjymiCaVkdF6dzUzInUNmzHPTVfYPI14Jzpkn7ZRXkZGpFgNiL8soHMaN7BS2mbcMEnHg4jgWuOByQATWfInXlAztYNbqUnvOSEkdEQEhpenFwt5hw2q61WZfGQJA9mmAQgvhrH5AH_ACZBv08uOaxSmd7uCCkpGaVyq_bZbJ4FAbIKca6ILPlAapdKYEHhGhxmO6ouh8nvM6QdevcZc_iWip-v4Dknr5xUTTlJB2auIIOFMuGGW7qsnmwqMJl3QkYERhTZjy_rXb2EY2s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به سالن خاطره‌انگیر ۱۲ هزار نفری آزادی؛ مصداق جنایت جنگی/ میزان برآورد خسارت بر اساس قیمت دلار و طلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/652067" target="_blank">📅 10:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b3806e94.mp4?token=EpxGHF7w4hbnMht8MfT2wqKaP0I4RJv4ev_JUQvYSjqqfFT_z2Rbd0WllNIOSLVHcQzV5K3gllZrdQjec--Kymct17n9Gzg8UsEDNwD6JRfhMRq8L2wMhtUQqbJn3HWP9Euuqp9Sl0lbhNekfKrF3vorv4V9HOZ_Iqp-sb8FEwiLchnSxcT5n-AUJXhChCYziyK7gfLvwBrvc9S0YDjf-PDRsDusuF8-anySFO-3_DEPhpHUAJZXxY4v83Z4EZ-6PnckUflLTCqc7ZJ2AbCevotOWN7G4qVGl5BdAoYeNaar3fgpaXAm-GioUnX67ZYPhuRzvH-lWuBxWfE6v3YxRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b3806e94.mp4?token=EpxGHF7w4hbnMht8MfT2wqKaP0I4RJv4ev_JUQvYSjqqfFT_z2Rbd0WllNIOSLVHcQzV5K3gllZrdQjec--Kymct17n9Gzg8UsEDNwD6JRfhMRq8L2wMhtUQqbJn3HWP9Euuqp9Sl0lbhNekfKrF3vorv4V9HOZ_Iqp-sb8FEwiLchnSxcT5n-AUJXhChCYziyK7gfLvwBrvc9S0YDjf-PDRsDusuF8-anySFO-3_DEPhpHUAJZXxY4v83Z4EZ-6PnckUflLTCqc7ZJ2AbCevotOWN7G4qVGl5BdAoYeNaar3fgpaXAm-GioUnX67ZYPhuRzvH-lWuBxWfE6v3YxRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یکی از پرستارهای بیمارستان میناب که دو فرزندش دانش‌آموز مدرسه شجره طیبه بودند
🔹
کرمانپور، رئیس روابط عمومی وزارت بهداشت: هشت نفر از کادر بهداشت و درمان در حادثه میناب فرزندانشان را دست دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/652066" target="_blank">📅 10:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652065">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رهایی ۳ گروگان و دستگیری گروگانگیران در خاش
🔹
فرمانده انتظامی خاش: در پی گروگانگیری به قصد اخاذی، پیگیری موضوع به صورت ویژه در دستور کار پلیس قرار گرفت.
🔹
کارآگاهان پلیس شهرستان خاش موفق شدند با انجام اقدامات تخصصی و شگردهای پلیسی محل نگهداری گروگان ها را شناسایی و در عملیاتی منسجم و غافلگیرانه ۱نفر از گروگانگیران را دستگیر، ۳نفر از افراد گرو رفته را آزاد نمایند.
🔹
افراد گروگان گرفته شده از شهرستان های مشهد، ایرانشهر و خاش بودند.
🔹
یک قبضه اسلحه کلاشینکف به همراه ۳ تیغه خشاب حاوی مهمات مربوطه، یک جفت پلاک خودروی سرقتی از متهمان کشف و دستگیری سایر گروگانگیران نیز در دستور کار می باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/652065" target="_blank">📅 10:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64f1c12a4.mp4?token=EKJGiP4BDwM93XbzBGsfL-CtYvIQTUz7YCxdotIiP-21rcpkTPyDsujC0YoknknmZQF22ioHhElVDn8FvYWVuHZ452jcAFolqZu0P7sP7qoRvgGvhyTxgpCZri01loAt0kPHLpbC5gT8yOflpaGLj7G8oBdggikk9JU8LURSb-lDjncVkJwyJ8j0tzCtH_V0nG9YwsG7PMhdFxjtMQwS669W44TZTchKjI8J6U5NMEoXcIpm-pXV9Eo5mtgD5FmQUTuNYgRyHSbseJMGER70RykrYTfznRvo_WzeM4ZxSDIfzIbRweRXGkELcL3l1im5N5_ZiyXKbvhIcvXdxip84g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64f1c12a4.mp4?token=EKJGiP4BDwM93XbzBGsfL-CtYvIQTUz7YCxdotIiP-21rcpkTPyDsujC0YoknknmZQF22ioHhElVDn8FvYWVuHZ452jcAFolqZu0P7sP7qoRvgGvhyTxgpCZri01loAt0kPHLpbC5gT8yOflpaGLj7G8oBdggikk9JU8LURSb-lDjncVkJwyJ8j0tzCtH_V0nG9YwsG7PMhdFxjtMQwS669W44TZTchKjI8J6U5NMEoXcIpm-pXV9Eo5mtgD5FmQUTuNYgRyHSbseJMGER70RykrYTfznRvo_WzeM4ZxSDIfzIbRweRXGkELcL3l1im5N5_ZiyXKbvhIcvXdxip84g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا کالاهای اساسی گران می‌شوند؟/ تشکیل کارگروه ویژه برای بررسی قیمت‌های کالاهای اساسی
🔹
نادری عضو هیئت‌رئیسه مجلس: ما به طور مداوم پیگیر افزایش قیمت‌های کالاهای اساسی هستیم و قرار است یک کارگروه مشترک برای بررسی افزایش قیمت‌ها تشکیل شود.
🔹
در جلسه با وزیر جهاد کشاورزی این موضوع بحث شد که چرا بعضی از اقلامی که با معیشت و سفره مردم سروکار دارند، باید گران شوند؟ در حالی که بیشتر مواد اولیه کالای مایحتاج مردم در داخل کشور موجود است. هرچند ادعای وزیر جهاد کشاورزی وقوع جنگ بود، اما برای ما قابل قبول نیست. بنابراین، ما به طور مداوم پیگیر افزایش قیمت‌های کالاهای اساسی مردم هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/652064" target="_blank">📅 10:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652063">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3580e63b79.mp4?token=jqnfd7kIy3mYwzTaA3508ONStlpD7OMnz3hHAuHxx4huLmA3r9IZrsS4Icocr3wEGE88Z1zuN9ZduE8JxMRD8AjHfINm-iTNePPp5v4YFrkhaEZENYBTxtlDbl6CHvvIxmp5xRLNgsdIWDUq6Uedqb0sYiP1rS-9S8JIOXjwME08FLSvZllHLL3FU3B1bIoLo588nlCUfWT1JjsuiOhc17wUsEE6CaQyg9f9d4vq_qKsRdy84CMbP6wGx4mrv5SzGzJ5IfSyZ-LO5-fMR8D69dm-FaXbz_SxKFJ7z8sWAEiN8q-MtEohLh8tQhX3cpAuMnKkmm2c7kpm_Wxdfc3v-qxrDvxlUtfbJrYxHofE_16t6MUXmADw5fShj9MFTyIXtq6ew4wiJJNdA-1zc5QPBc7nFmDs0eOyHQi_oahXEaVDrRX0N940afVXD5ekNCqrLtw4OT96zc9XeLDD4VI1u4Rzuy9-a9jfzqq9AZCvUdEWq12hBalU3XAJzGEoPm6iLfSwNWp5SC3fXTnjIsS8CFLwFB542MoHlGrvcOfFLh3b4v8kJ6XWQOCijDdNNrOP_A2mmOUa6nfJH4vUGdDRXJKR1Qz9Y4PWH1v0udaU_At1gYC2MpZ0AkcoufqjsmHoLDg6cSilGJ5puHnYNJBWPx7xJEcgESaqFl4oHoOatJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3580e63b79.mp4?token=jqnfd7kIy3mYwzTaA3508ONStlpD7OMnz3hHAuHxx4huLmA3r9IZrsS4Icocr3wEGE88Z1zuN9ZduE8JxMRD8AjHfINm-iTNePPp5v4YFrkhaEZENYBTxtlDbl6CHvvIxmp5xRLNgsdIWDUq6Uedqb0sYiP1rS-9S8JIOXjwME08FLSvZllHLL3FU3B1bIoLo588nlCUfWT1JjsuiOhc17wUsEE6CaQyg9f9d4vq_qKsRdy84CMbP6wGx4mrv5SzGzJ5IfSyZ-LO5-fMR8D69dm-FaXbz_SxKFJ7z8sWAEiN8q-MtEohLh8tQhX3cpAuMnKkmm2c7kpm_Wxdfc3v-qxrDvxlUtfbJrYxHofE_16t6MUXmADw5fShj9MFTyIXtq6ew4wiJJNdA-1zc5QPBc7nFmDs0eOyHQi_oahXEaVDrRX0N940afVXD5ekNCqrLtw4OT96zc9XeLDD4VI1u4Rzuy9-a9jfzqq9AZCvUdEWq12hBalU3XAJzGEoPm6iLfSwNWp5SC3fXTnjIsS8CFLwFB542MoHlGrvcOfFLh3b4v8kJ6XWQOCijDdNNrOP_A2mmOUa6nfJH4vUGdDRXJKR1Qz9Y4PWH1v0udaU_At1gYC2MpZ0AkcoufqjsmHoLDg6cSilGJ5puHnYNJBWPx7xJEcgESaqFl4oHoOatJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خشم سناتور آمریکایی از میانجیگری پاکستان در مذاکرات ایران
🔹
سناتور لیندسی گراهام در جلسه استماع کنگره آمریکا با لحنی تند و بی‌سابقه، پاکستان را به نقض بی‌طرفی در مذاکرات صلح متهم کرد و ادعاها درباره هواپیماهای ایرانی در پاکستان را تکرار کرد و گفت اگر گزارش‌ها درباره پارک هواپیماهای ایرانی در پایگاه‌های پاکستانی درست باشد، واشنگتن باید دنبال میانجی دیگری بگردد.
🔹
وی در جلسه استماع کمیته نیروهای مسلح سنا با حضور دن کین فرمانده ارشد نظامی و کاتلین هیکس معاون سابق وزارت دفاع برگزار شد، از کاتلین هیکس پرسید: «اگر میانجی اجازه بدهد هواپیماهای شناسایی ایران در پایگاه‌هایش پارک شود، این با منصف بودن یک میانجی همخوانی دارد؟»
🔹
هیکس گفت نمی‌خواهد خود را «وسط این مذاکرات بیندازد»، اما گراهام با صراحتی کم‌نظیر پاسخ داد: «خب، من می‌خواهم خودم را وسط این مذاکرات بیندازم. من به پاکستان اصلاً ذره‌ای اعتماد ندارم.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/akhbarefori/652063" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652062">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0mTT_5oYzkMNaRLgzflhwQtyEOQtJT03ZUHZXFD_R14Q0dFkQibqUxoSB7F0HIx-OErOj2qkwNmv5sPXCXf2mV4PTCuAe3TSSdRE3wuA_U8Db_B4-En10PTUbgybHsYriQc-ATBCC-hVW7tWBJ3EvIQN0tldj4JIPsrb-IvOa-KiZIWoJ8BWQ0FkmiowRnLIB8m5fdTGk4XAPBb2NMU4h2fXSJ75A-FmRFROP2Uxwg5OWQAUtu-x_wrJnFYJNsknzJZOuY_nqBR6A1cn7hE-aI_z2T21bweZP1VEXTuX9yYh-XxGApcM8gETVzbha6_GIqFYYQjOHTSYeTqhoxeGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلزله‌های بزرگ استان تهران
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/akhbarefori/652062" target="_blank">📅 10:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652061">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
متهم در یکی از واحدهای مسکونی محدوده چیتگر تهران مستقر بود و اطلاعات مربوط به محل‌های اصابت در جنگ رمضان را به شبکه‌های ضدانقلاب منتقل می‌کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/akhbarefori/652061" target="_blank">📅 10:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652059">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1pvFnpr9PkGm0_MWdI0fbO2ThX8SykJEexQeFTgJK3dsG1oN34-Mj8TobUVK2WvItJ4ZMI8_eldFtaoByLF-kAmY0L6_TFV-Ky0dJQfb3QdMChmy1WWYgC99-P6xnUT3n6Wyuo6-H63KInDztdxU1bx-ec57Kacuh_Lb_1tWX_7vlp9XfMMaQGmVlN8fMW5s-_aw0Byl7Hp9OTJi_WPXJDG8a3sFRS2DYEMtlgC8xRmMvbuzHEt6PpjWIaROdhrXCmqlafoBskhpauEcgBcIuXKddTZPCxDS2L5Xkbd4IT8pG26uP4B-7SD1_TZXTlJeN1897mPl3YYhwV7Nc3pUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفتالی بنت: کابینه نتانیاهو ارتش اسرائیل را تضعیف کرد
🔹
نخست‌وزیر پیشین رژیم اسرائیل، گفت کابینه فعلی، ارتش اسرائیل را تضعیف کرده است و ادامه جنگ، کمبود در شمار نیروها و فرسایش میدانی فزاینده را آشکار کرده است.
🔹
نفتالی بنت که «شکست ۲۰۲۳» در عملیات «طوفان الأقصى»، به تغییری سیاسی بزرگ منجر خواهد شد؛ تغییری مشابه تحولی که اسرائیل پس از جنگ اکتبر ۱۹۷۳ شاهد آن بود.
🔹
نفتالی بنت، کابینه بنیامین نتانیاهو را مسئول شکست امنیتی آن روز دانست و گفت کابینه کنونی از این حمله درس نگرفته و همچنان اسرائیل را بر اساس «همان رویکرد» اداره می‌کند؛ رویکردی که به فروپاشی نظامی انجامید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/652059" target="_blank">📅 09:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652058">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr-V6yU3RYE2JK_psLpriDvISxLYQShPLmxuUZ0n7c-9r5R36ms5WvtOb4SVy1LUewS4ijHSFrT9toz2IjJh4nJ6KlGIIlZwVu7ksRo93tKCxdPupJxA5-YTG3KG5zM0n4PPIf4ZK7HP6H67g0mBhYEZr7Y6oOIMUjMtkMKcVrCP9vfB1QsIIY_eLITq54oGCMA-b-dJIpJonMEAtg0hmY_8oL0EcRvIdx28J_c7FZeBJXlUL2EWa924Xtj5vUmfkr-FmFk1-rEsvND60mfmeEaYDfr9MeFYuNSbm4LfkUBgTYb57DWM31Wu74W6jARZBL3kl64fA7msUTPgQY6ALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر پلاستیک در کیف‌ مدرسه‌ دانش‌آموزان
🔹
پلاستیک‌های کوچکِ مدرسه، زباله‌های ماندگارِ طبیعت؛ تغییر از کیف دانش‌آموزان شروع می‌شود  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/akhbarefori/652058" target="_blank">📅 09:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652057">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnU_BZmtyVi4_bNfTPmp51JL0Z4nv4cAFAjEauA-a2FLwAW5BRJfMIIbfrw1f-QzbWDryZeTGzLH3Wurny-3rR_9PUGS2IlTeXaLB3ZYjU4cHY-alX4CXMD-ciFdfES8iTon_KnxZJ0mAEoTpSoiMLGKDgaio29PjkACvs2KH_pWRj2dSQ5rkvLjyWsTwzbRThbXBC3HdUEgDSqyUJzhqq8htKsObE1bDFOm3Tw2ej6b3oBwN9DB5pHzTq_3qrsAKy8Loadoo8SOY-vJpw0G_PfEN5sRKaD4ch-dUBHshCfu4gOsFHr0ozEDS0yPRZwFwyVuA9MtBtMZDef2iZHDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلیه خریداران ورق گرم فولادی مکلف به عرضه محصولات خود در بورس کالا خواهند شد
🔹
بنا بر شنیده ها از ماه آینده کلیه واحدهای خریدار ورق گرم فولادی، مکلف خواهند بود محصولات خود را در بورس کالا عرضه نمایند. این تصمیم مراحل پایانی مصوبات قانونی خود را میگذراند و در روزهای آینده ابلاغ خواهند شد.
🔹
به نظر می‌رسد پس از بالا گرفتن قیمت ورق و کشفیات جدید ورق‌ها به صورت انبوه در انبارهای غیررسمی توسط نهادهای نظارتی، این تصمیم با فوریت ویژه اتخاذ شده و اجرایی می‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/652057" target="_blank">📅 08:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652056">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
احسان افرشته، جاسوسی که در نپال توسط موساد آموزش دیده بود و اطلاعات حساس کشور را به اسرائیل می‌فروخت اعدام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/652056" target="_blank">📅 08:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652055">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
آیت الله عاملی، عضو مجلس خبرگان رهبری: اغتشاشات و کودتای دی‌ماه، آغازگر جنگ رمضان توسط دشمن آمریکایی- صهیونیستی بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/652055" target="_blank">📅 08:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652054">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTAXRtRo3AFPkGHdP6X5ZjpmnsCQcdtdnXkIBinPE6QzmQorAKj_5n65_xu9pAzDTQObW4yU017CmtNLYndXMTb13nw2kHElphLESDI5Q01VENGxICdoWk3PD55FqZTUr1KD4Bwx-FnNKEQaObx6Z-4JOFOzPTRYnsreI6v3ngECjqjGrArOU83IZeqLO1Zlytfi8TDRsps6HErgjysH5_j0dBsyZLAJVON4QIQvOyhd-NcNNpHlx3e4GYs_Ml8WxlH4xR7bwYhG5Kcr2a69O-zz6HTtN7DF0Me53OWMAhMbiDfwBsWfBfBfHo-vVDqteCFxnGLnlncV08vaMVouuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازداشت معاون دبیرکل سازمان ملل در فرودگاه اسرائیل جنجال دیپلماتیک به ‌پا کرد
🔹
روزنامه صهیونیستی یدیعوت آحارانوت گزارش داد که سازمان امنیت داخلی رژیم صهیونیستی (شاباک) صبح امروز (چهارشنبه) ژیل میشو معاون دبیرکل سازمان ملل متحد در امور ایمنی و امنیت را هنگام ورود به سرزمین‌های اشغالی بازداشت کرده است؛ اقدامی که به گفته این رسانه صهیونیستی موجب ایجاد بحران دیپلماتیک برای رژیم اسرائیل شده و این رژیم را در وضعیتی دشوار قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/652054" target="_blank">📅 08:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652053">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
سی‌ان‌ان: اسرائیل نگران توافق آمریکا با ایران است
🔹
شبکه خبری سی‌ان‌ان در گزارشی نوشت که تل‌آویو نگران است آمریکا بدون رسیدگی به مسائل مد نظر این رژیم، به توافقی با ایران تن دهد.
🔹
یکی از این مقام‌های رژیم صهیونیستی گفت: یک هراس واقعی وجود دارد که ترامپ به یک توافق بد با ایران دست یابد. (رژیم) اسرائیل با تمام توان خود سعی دارد بر این امر تأثیر بگذارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/652053" target="_blank">📅 07:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652052">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcRIgcTIFhsT-iYbsTRqH3KvZgLLCOJvnUVBd0G_cXKMa7mMx46LIKcj0UdaSDYZKW2gxuqQ_dHsBgqu5pzPgSLilYBIR02ZRs6ISU11mOrVa5jek76653l0wsmjyiqc9QAiMshdBKYQGHk29kbWhAh8roaToQWvVnREpg3kEVYOyqoJ4a0AEvte6LAq_ToFS5iKirR3jvUAYdbtaGp2WShd2ZhSQIGo2xAmAmMs4C1QUSudtli6L8CU0-iwCHWkL0ccul7yXXdHHSZ4jK1LSaw5tiTJGBnicc1ocCrYYhAvTJl3LVH55EQuJE2YBH5nXZBnpf_-YyLMnpR0py6fFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ظرفیت ۳۰ میلیون تنی که محاصره را دور می‌زند
🔹
در حالی که تنگۀ هرمز به گلوگاه تحریم‌های آمریکایی تبدیل شده، دریای خزر به خط مقدم تاب‌آوری اقتصادی ایران بدل شده است.
🔹
استاندار گیلان می‌گوید که بنادر شمالی ظرفیت واردات ۳۰ میلیون تن کالای اساسی را دارند؛ رقمی که معادل کل نیاز وارداتی کشور در سال گذشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/652052" target="_blank">📅 07:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین- داریوش بزرگ -قسمت هجدهم</div>
  <div class="tg-doc-extra">داریوش بزرگ</div>
</div>
<a href="https://t.me/akhbarefori/652051" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
▶️
«داریوش بزرگ؛ معمار امپراتوری ایران»
🗓
این قسمت روایتی‌ست از پادشاهی که پس از طوفان شورش‌ها، ایران را یکپارچه کرد؛ از مردی که با نظم اداری، قانون‌گذاری و ساخت پارسه (تخت جمشید)، پایه‌های یکی از بزرگ‌ترین امپراتوری‌های جهان را استوار ساخت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/652051" target="_blank">📅 07:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652050">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac1de98ac.mp4?token=VQUPOphMkckf8pI_5PRoGgaKJl64yjOa-V9wEihbwDRTrnqtr0VYvv2UzhG0Tgjk5dOe8-yKDRLepqwfd88jX6Tr6w2t68i6A3n70iZaiCKueEByRIt4baLV6emj9hfyOIgbg9wkXRPw0BplaHWRPc00CAeZYiPCnAiottv4YmGtoTng7PEjXZD7r8oYoNe3bC089wdJED0TwN4EtXh_3s8vUQXZF8swlAIdpvM_EO421_Q_4kW4d95omXX61_pypMzgpCRWcQM49g-OeL8dDHCq6iRS6tZH9db-Os9sAAQ0h12RzpH4JSjRpWuIqg2QNxHrBa5c2t-lEHjg4tyjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac1de98ac.mp4?token=VQUPOphMkckf8pI_5PRoGgaKJl64yjOa-V9wEihbwDRTrnqtr0VYvv2UzhG0Tgjk5dOe8-yKDRLepqwfd88jX6Tr6w2t68i6A3n70iZaiCKueEByRIt4baLV6emj9hfyOIgbg9wkXRPw0BplaHWRPc00CAeZYiPCnAiottv4YmGtoTng7PEjXZD7r8oYoNe3bC089wdJED0TwN4EtXh_3s8vUQXZF8swlAIdpvM_EO421_Q_4kW4d95omXX61_pypMzgpCRWcQM49g-OeL8dDHCq6iRS6tZH9db-Os9sAAQ0h12RzpH4JSjRpWuIqg2QNxHrBa5c2t-lEHjg4tyjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ، پادشاهی که امپراتوری را از نو ساخت…
​قسمت هجدهم پادکست کافئین منتشر شد
☕️
⚪️
با قانون، جاده شاهی و نظمی کم‌سابقه، ایران به قدرت اول جهان باستان بدل شد…
​
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتون باشید!
​از اینجا ببینید و بشنوید
👇
https://youtu.be/Qfgg8RqcuBg?si=5uXMp7EKJBtDtAjp
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/652050" target="_blank">📅 07:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652048">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJSSj3TvpP5XH3olRBd1NPaZbiPo33Ph-W1u8vZFKRBsHM55VMHfunfeLptevrhMEqyUqOF7uL0qMqq6OLj4Gx7STkeAg2kHLQ5g4GPbONQOhJv1oChxApzBf-Vn-2XG2uol2o7wwuf6eo_GxwwCZWThgFWOgB-vNvvT4r10EBDzW9NgeKJiMluGq9LvbTDY-ptIxBSi5ja5a6iCTpOyrO_UnPpm7Mm0mMO2bHHMVayJHzMLbSacwgD-JTWYTWYOS7YzxC_0bBbXyqSH9cekVpg69J1WomOl3aMIiHUhDaLNka1q_uXffPddYiwuzN2PXgmgEHBlpHjIVXo5Rh3i2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۳ اردیبهشت ماه
۲۵ ذی‌القعدة ۱۴۴۷
۱۳ می ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/akhbarefori/652048" target="_blank">📅 07:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652047">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfVpml5PzLXNQnFF18dvpodzcF1Vdi9Wh7ZzJyuKty80ju1agf56BAuh--q2KDarcANzqheSN-XIiDVEc3gIs8yrumTqqW0BWS8whhaSOfbKoGeEcVEql09yPQq0cfh7PCIBm3oofQ0MglBZRYCur_-Sl4GxpXcuuNlOS6LyUTgl3LufM46tPePe3v-bSj1PSlku04d4afsaouU-JQ1NJg8gxXL1T97oc7qEqNKYRfyzYVMQqyul3CrDE6Ja0il0ISJ_eOWVQ5_6FEMPD91mexTwB4UNLSkfVYSFOX13VNe7xe3QV6r8JL65jEHiULt8t61FTgixozNQ4uLlu6KSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسوشیتدپرس: پرسش های سخت کنگره به ویژه واکنش های منفی جمهوری خواهان به وزیر جنگ آمریکا
🔹
هگزت، وزیر جنگ روز سه‌شنبه با پرسش‌های سخت قانون‌گذاران جمهوری‌خواه و دموکرات در مورد پایان بازی دولت ترامپ برای جنگ ایران، از جمله افزایش هزینه ۲۹ میلیارد دلاری این درگیری و تأثیر آن بر کاهش ذخایر تسلیحاتی ایالات متحده روبرو شد.
🔹
اگرچه رئیس پنتاگون لحن خود را در جلسات استماع کنگره تقریباً نسبت به دو هفته پیش ملایم‌تر کرد و به ویژه از همان انتقادهای تند قانونگذاران اجتناب کرد، اما از سوی اعضای حزب جمهوری‌خواه خود در مورد میزان مهمات مورد استفاده آمریکا در جنگ ایران و انتقاد شدید دونالد ترامپ، رئیس‌جمهور آمریکا از متحدان سنتی به دلیل عدم شرکت در این درگیری، با واکنش بسیار منفی‌تری روبرو شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/652047" target="_blank">📅 06:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652046">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7R5ur12qQmSDSjfSb26obkOMJ9AmL6Z3aTsjQfM0aZ-k5Y5VRP8_-bu5flVpNewCR4SONMCIzCJqpVMth2vOgpws5XHqvCw13k0Rn30BIRJdZxQld3IEWnRnDUd3kFdQ1iZWoZ4P6BQmL_UDTa5f9kS253jenDfRQ2_yDdOhysGr7gPNLJn24WhSkLJZqrrLVH55TIjQPl4xiF_mB7VM9FmX63J3XhcBqyyJvVtjhE8KT2zK_KAwfcZx4jhFzeF1ZMaewTPSVnoUgLM5kO2WlUHew5lFniK5VI_wxkN94Epw5vlcdVIfmKdZiNTeHi2NyhQNIgrL83H7lzY8aUWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دموکرات‌های آمریکا: جنگ ترامپ با ایران غیرقانونی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/652046" target="_blank">📅 05:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652045">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
چین از پاکستان خواست تلاش‌های خود برای توفق ایران و آمریکا را تشدید کند
🔹
وانگ یی، وزیر امور خارجه چین، در تماس تلفنی با محمد اسحاق دار، معاون نخست‌وزیر و وزیر خارجه پاکستان، از اسلام‌آباد خواست تلاش‌های میانجی‌گری خود بین ایران و ایالات متحده را تشدید کند و برای حل مسائل مربوط به بازگشایی تنگه هرمز نیز نقش فعال‌تری ایفا نماید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/652045" target="_blank">📅 04:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652044">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
انگلیس نیروی نظامی به تنگه هرمز اعزام می‌کند
🔹
وزارت دفاع انگلیس شامگاه سه‌شنبه از آمادگی ارتش این کشور برای اعزام یک فروند کشتی جنگی، چندین جنگنده و مین‌روب‌های بدون سرنشین به تنگه هرمز خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/652044" target="_blank">📅 04:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652043">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmPkZOVYXtsRyROM66OJiWeyvgbfD8UsCkpRDBYrB1KC6Rwl5USKbyGi15LzZK2GZgerZCM6JIFjL3shXalNNO9tgLYRHtm5UhjH0WZ4yUXuCNZaxE7ObxlBqV69rHhztqddrUKCDllPzWpctWcikYgkF4ARZnmVQ2gb7njlh207AtIRrJw12SEzyGTIUOfQmsr-vVQePj2ICyNOf-1bK-auGefUJIO0uqYRYtft2p6QcRqlbXGSR-Cu5lhG_Wobvq6J8b3Q4hjnvUx9HyhkjxU0KQM586wXQnC1G8tWwg6Zx30hX4NYI5asuANmF06FTSzIK9MbfYuP-Bmcke61wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: اسرائیل نگران توافق بد آمریکا با ایران است
🔹
مقام‌های صهیونیست به شبکه «سی‌ان‌ان» گفتند که تل‌آویو نگران است آمریکا بدون رسیدگی به مسائل مد نظر این رژیم، به توافقی با ایران تن دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/652043" target="_blank">📅 03:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652042">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تصویب قانون اعدام اسرای فلسطینی در سایه سکوت جهانی
🔹
«ریاض الاشقر»، مدیر مرکز مطالعات اسرای فلسطینی: سکوت جامعه جهانی در قبال قانون اعدام اسرای فلسطینی، رژیم صهیونیستی را به تصویب قوانین جدید برای اعدام صدها اسیر اهل غزه و جلوگیری از آزادی آنان در هرگونه توافق تبادل اسرا تشویق کرده است.
🔹
این قانون، یک جنایت جنگی و نوعی مشروعیت‌بخشی رسمی به قتل اسرا از سوی کابینه افراطی رژیم صهیونیستی به شمار می‌رود و هدف آن، انتقام‌گیری و بستن راه هرگونه توافق تبادل اسرا در آینده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/akhbarefori/652042" target="_blank">📅 03:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652041">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnzY6y3B_FwNJxAO7RnQ3R9PebRXZ4p17yJWFoOwGrMqTDuZe_A-d5OEIMRIyuGGl4MLomEssT-14fTe7kHC0fcQ7rBwMKy_2H0Y_O-UcRoQ3ksLi8W9KqJnU7Xy5geQCCdPifdes1wxWm1x_3iEsE-NNcZ2KvFRnwS09oUi1LqhSbga7oGDlFSp2HpzPl5g5zs7nfJoI1vPV-2L1IHrT9I5A2zBf3fvXvWjERFNcXux0U-txj69eBgs225XQZ7r4p7FfGuvMrUzIHl6EqP_LA8L-kiWajPrHdT1TdxrQQdfTsb2h8x7esBG_NftMioWNCnvisalp0dwpgvP5vyfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ۱۱۲ کشور به قطعنامه آمریکا درباره تنگه هرمز پیوستند
🔹
منابع دیپلماتیک می‌گویند که ۱۱۲ کشور هم‌اکنون از پیش‌نویس قطعنامه پیشنهادی آمریکا به شورای امنیت سازمان ملل درباره تنگه هرمز حمایت می‌کنند.
تحلیلی دراین‌باره را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214584</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/652041" target="_blank">📅 02:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652040">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
اقامۀ نماز آیات برای تهرانی‌ها درپی وقوع زلزله واجب است
🔹
به دنبال وقوع زمین‌لرزه در مرز استان‌های تهران و مازندران بر اساس موازین فقهی، با وقوع زلزله، اقامۀ نماز آیات بر افرادی که در محدودۀ لرزش حضور داشته‌اند، واجب فوری است.
🔹
طبق رسالۀ عملیه و فتوای مراجع عظام تقلید، رعایت نکات زیر حائز اهمیت است:
🔹
محدودۀ جغرافیایی وجوب: اقامۀ این نماز تنها بر کسانی واجب است که در شهر یا منطقه‌ای حضور دارند که زلزله در آن رخ داده و یا لرزش آن را احساس کرده‌اند.
🔹
زمان اقامه: نماز آیاتِ زلزله باید در اولین فرصت ممکن و بدون تاخیر (پس از رفع دلهرۀ اولیه و پیدا کردن شرایط ایمن) خوانده شود.
🔹
اطلاع دیرهنگام: اگر فردی در زمان وقوع زلزله خواب باشد یا به هر دلیلی متوجه آن نشود و بعداً از طریق اخبار یا اطرافیان مطلع شود، همچنان خواندن نماز آیات بر او واجب است.
🔹
تعدد زلزله‌ها (پس‌لرزه‌ها): با توجه به وقوع پس‌لرزه در ساعات گذشته، اگر فردی هر زمین‌لرزه را به صورت مجزا احساس کرده باشد، برای هر کدام یک نماز آیات جداگانه بر او واجب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/652040" target="_blank">📅 01:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652039">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ایران به اکثر تأسیسات موشکی‌اش دسترسی دارد
🔹
روزنامه «نیویورک تایمز» بامداد چهارشنبه نوشت که بر خلاف ادعاهای ترامپ، ایران به اکثر سایت‌های موشکی خود دسترسی دارد و ۹۰ درصد آنها عملیاتی هستند.
🔹
در این گزارش آمده است: «ایران دسترسی عملیاتی به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده است، که می‌تواند کشتی‌های جنگی و نفتکش‌های آمریکایی را که از این آبراه باریک عبور می‌کنند، تهدید کند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/652039" target="_blank">📅 01:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652038">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSS7el8gs70WFvERz1o0U1s5YKl2Cys3PPA9XrjvpTMDaICYS-kiCYzCWoj6B05VWoiHrUfpi6BlrKvUKj4BB03-jppLTJveLl5zD_QrgIk8DF6Q4gOr2gUWKRwZBNjOBbjqB60hVon2Y9Q2l1vynxuEq0O2w6orQDQcDfiMJHYZWC_-zDG0916KrWNswS_rPNVH_Pg1xhbEFIO2Bw-LQO_Td89l7g-ZUL0efiBWyYrLPuUBNeST0xkUFerKD5rasij63dGRBnUEAPoa9DDrck4q0oMBA-diIfn8LomPrVOkQ3UTOwYipsCj2xkWyqhs4Tkq_PtZ3Ge2yte8FXa4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف صریح مقام صهیونیستی: خوشحال می‌شویم اگر توافقی میان ایران و آمریکا در کار نباشد!
🔹
منابع اسرائیلی گفتند توافقی که برنامه هسته‌ای ایران را تا حدی دست‌نخورده باقی بگذارد و همزمان از موضوعاتی مانند موشک‌های بالستیک و حمایت از گروه‌های نیابتی منطقه عبور کند، باعث می‌شود اسرائیل جنگ را ناتمام تلقی کند.
🔹
یک مقام ارشد نظامی اسرائیل نیز ماه گذشته به خبرنگاران گفت که اگر جنگ بدون خارج شدن اورانیوم غنی‌شده ایران از این کشور پایان یابد، آن را یک شکست تلقی خواهد کرد.
🔹
این منبع ادامه داد ما خوشحال می‌شویم اگر توافقی در کار نباشد، خوشحال می‌شویم اگر محاصره هرمز ادامه یابد، و خوشحال می‌شویم اگر ایران چند حمله دیگر نیز دریافت کند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/652038" target="_blank">📅 01:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652037">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
مصرف ۱۳۰۰ فروند موشک پاتریوت از سوی آمریکا در جنگ ۴۰ روزه با ایران
🔹
رسانه‌های عبری اعلام کردند که آمریکا در جریان جنگ ۴۰ روزه با ایران، ۱۳۰۰ فروند موشک پاتریوت مصرف کرده است. هر موشک پاتریوت بین ۴ تا ۴.۵ میلیون دلار هزینه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/akhbarefori/652037" target="_blank">📅 01:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652036">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
فعالیت‌های ماگمایی قله دماوند با ایجاد تغییر در فشارهای منفذی، باعث تحریک گسل‌های اطراف می شود
🔹
اینکه باید منتظر زلزله بزرگی در شرق تهران باشیم از منظر علم میان‌مدت و بلندمدت زمین‌شناسی دارای دو جنبه است، از نظر پتانسیل لرزه‌زایی که از نظر علمی، گسل مشا توانایی تولید زلزله‌ای با بزرگای بیش از ۷ را دارد.
🔹
با توجه به اینکه از آخرین زلزله بزرگ این گسل (۱۸۳۰ میلادی) حدود ۱۹۶ سال می‌گذرد، این گسل در مرحله تنش بحرانی قرار دارد ولی هنوز در حال حاضر هیچ ابزاری برای تعیین زمان دقیق وقوع زلزله (ساعت، روز یا ماه) وجود ندارد.
🔹
وقوع زلزله‌های ۴ ریشتری اخیر در ۲۸ فروردین و ۲۲ اردیبهشت در پردیس نشان از تخلیه انرژی: وقوع زمین‌لرزه‌های کوچک به صورت مستمر، بخشی از انرژی گسل دارد، ولی این لرزه‌ها نشانه‌ای از ناپایداری در پهنه‌ای وسیع‌تر نیز می تواند، باشد که مقدمه رویداد بزرگتری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/652036" target="_blank">📅 01:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652035">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5b045bd6.mp4?token=s9FgAojaJCBaqE2sKvWgNhRBuR5nuR9wAnp4jQt9eUbeFmArF0637GI6wiysi0-jP1Im5xGADa6TlJ8PJSwhKETFofXJeojgMzrUM_j5mjRYHDw6zXm5gxh_u4pVFfYwRuRWIXLuI8UeGd4Gi5GfhhgNAfaoD8Rzbxr4JOgEyUZGDinhPg6XKrKbu0ZEaPSNLP-doqrOc-s3DsepF9WbxgIMGDZjpJ7jJCZPXXH-Cq2kZXjJBaF3LvoKun7ZQsAkehI2URieb_Rn68d5io8EmjFSGi4qrbBLe_IhygHq7Pd07yix_OvKSWFA7N02gY1QpkpWMuXEkYI9ByC8ljAbZYOoynerdLJb07uZJC6YR1STcIeHXN4xCnC1enYIaRbeIUu7eDJ7ZojCMpu5HhCg4g616SkMih35dx8pgPwZyvCMDtb0Avao0NS0q_7CbMrsIdSZO9YRFSluymVeC3yiaD1HbYJlTf26YGgTtXlZMY4Rq_7HtI2sC53_awC6-_R7t80UhW6S8RYoCVfb1YxICvOvR2VwWjstRmFwdcswm6UB8OUhfWL_xW_vvZLfEL4eumG2y_ObCsc_UQWVN4z_zdQ_zGz4uLxG0tl45y9ZJ4h7Z4bxjlaDmcovWuxSbT837Vpey5tDh3BAM-VVfn1uvWQXoJIOS7waPFOofa95_iM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5b045bd6.mp4?token=s9FgAojaJCBaqE2sKvWgNhRBuR5nuR9wAnp4jQt9eUbeFmArF0637GI6wiysi0-jP1Im5xGADa6TlJ8PJSwhKETFofXJeojgMzrUM_j5mjRYHDw6zXm5gxh_u4pVFfYwRuRWIXLuI8UeGd4Gi5GfhhgNAfaoD8Rzbxr4JOgEyUZGDinhPg6XKrKbu0ZEaPSNLP-doqrOc-s3DsepF9WbxgIMGDZjpJ7jJCZPXXH-Cq2kZXjJBaF3LvoKun7ZQsAkehI2URieb_Rn68d5io8EmjFSGi4qrbBLe_IhygHq7Pd07yix_OvKSWFA7N02gY1QpkpWMuXEkYI9ByC8ljAbZYOoynerdLJb07uZJC6YR1STcIeHXN4xCnC1enYIaRbeIUu7eDJ7ZojCMpu5HhCg4g616SkMih35dx8pgPwZyvCMDtb0Avao0NS0q_7CbMrsIdSZO9YRFSluymVeC3yiaD1HbYJlTf26YGgTtXlZMY4Rq_7HtI2sC53_awC6-_R7t80UhW6S8RYoCVfb1YxICvOvR2VwWjstRmFwdcswm6UB8OUhfWL_xW_vvZLfEL4eumG2y_ObCsc_UQWVN4z_zdQ_zGz4uLxG0tl45y9ZJ4h7Z4bxjlaDmcovWuxSbT837Vpey5tDh3BAM-VVfn1uvWQXoJIOS7waPFOofa95_iM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: مبادی سفارش‌ها تغییر کرده تا بتوانیم کالاها را از مرزهای زمینی و بنادر شمالی وارد کنیم
🔹
گفت‌وگوهای جدی نیز با کشورهای همسایه و کشورهایی که با آن‌ها در تعامل هستیم، اتفاق افتاده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/652035" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652034">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApqBSqaXtxuyp7H_Q1BwVsTFanlSQ7N9P3kdEU3bQ8i0lG8R_e6WOXntoIqJzcDpK-Ub1Blsh0_RUy2QMKnMvrtax9AOl8SaMrTkmuqUWi9PvADrWiAHbr6z_JoxY_7AI84Ncqbvw1hbf9srNpfulovACZ4P_S7TzuBKpl-FrMoF4MiVCWmxRakuHE8kYbIktukFUxcOQ1zqfm_cqD85WfMB1udEj0ojiLOH8c2g_p2n03XOkHR4LDfWivVeVb5Ya1GhY-qxSacYdRIm9rLmLhyOeCedad_PwMNrZd8uZUHFXkiKw_r8PzpgLrIVGIAjUPtnftdT7lajWaeX-NRgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: آنچه بر ملت صلح‌دوست ایران تحمیل شده جنگ متعارف نیست
🔹
سخنگوی وزارت امور خارجه در پیامی با بیان اینکه آنچه بر ملت صلح‌دوست ایران تحمیل شده، یک جنگ متعارف نیست، نوشت: این جنگ میان دروغگویان حرفه‌ای است که برای خشونت‌شان توجیه جعل می‌کنند، و مردمی شریف که فقط با تکیه بر توان و اراده خود، از وطن و کرامت انسانی‌شان دفاع می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652034" target="_blank">📅 01:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652033">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔹
از داغ‌ترین خبرهای امروز و امشب، جانمانید
🔹
🔹
زلزله‌های پی‌درپی در تهران
👇
khabarfoori.com/fa/tiny/news-3214578
🔹
دیدار مهمی که سرنوشت جنگ به آن وابسته است
👇
khabarfoori.com/fa/tiny/news-3214551
🔹
ترامپ به جنگ ایران بازمی‌گردد؟
👇
khabarfoori.com/fa/tiny/news-3214321
🔹
چین بین تهران و واشنگتن میانجی‌گری می‌کند؟
👇
khabarfoori.com/fa/tiny/news-3214364
🔹
سیدنی سوئینی به سوی آثار مستهجن می‌رود | ماگا علیه عزیزِ ترامپ!
👇
khabarfoori.com/fa/tiny/news-3214209
🔹
تصاویر و ویدئوی املاک توقیف‌شده خبرنگار ایران اینترنشنال
👇
khabarfoori.com/fa/tiny/news-3214399
🔹
ویدئوهای جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/652033" target="_blank">📅 00:50 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
