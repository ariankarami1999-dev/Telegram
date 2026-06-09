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
<img src="https://cdn4.telesco.pe/file/XGPjN6iDDvlF36BxpIbKJCAM1I_B4lkDcU8sD0Rxpo6ta4_3BU8iZQegmZvgsTK0EVBP2Gt6dgD4ouxlRPrZugqZNsluAVjbaPorTawDZpPGT43efdiQLXGnrCTMm9V9hoXkruQY0_3UUWXjgz3cmm67fGIKyjKnHreVVx3XfPnc4-hQGYS_IttutZ2A3Q6w6kx-LxV05vg42CaHhdsdpVL1Ok2MluVEFwDCa-wMJufGXSBWi4qTPWy4e5rFYRh6HkUlyFXBKeBb92c9TQbSTUcxnqbzdHi6QczU21GZ2CwSqYjhfyW1SJP3yPje1FhBmyDOUqd7dSwBHCV58jV7FQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 16:54:32</div>
<hr>

<div class="tg-post" id="msg-657668">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRU6Q0XMErDS2VhAlmOL67Qwh4CzKnsnsFjpZzhiTNmuzg20k929arrtMbMmcmN9rdXcEymyADKTyAt4x58KFzhcdI5IqVI8B1plRwP36fibP7F9ccPx-e5Aa0oT_ZHrqiukXSSUK8ElPkaOZoRVJ-BxGtHhaDdCUucQdmUnJp_WadEtpd1OWAAYDC4jSwL7exavhQHEdPTvWWl6q5F5eLbT6z5OeEWnc-mEt0wBUbKZ-R9Ave4DgEFp7HQ2JRMdpsz0dJUYb4Etc2ToKlyhL7IG6Z7t54qFsvLDURYJDNOGr05IFpGmT_nQonj_v2_adhLla9My10LztptvT1nuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رِد بانک؛ با ارائه مجموعه‌ای جامع از سرویس‌های بانکی، سرمایه‌گذاری و هواداری فوتبال، تجربه‌ای متفاوت و یکپارچه را برای کاربران سراسر کشور فراهم آورده است.
🟢
در قالب طرح «رِدبانکی شو»، کاربران جدید پس از دانلود اپلیکیشن(دریافت از آدرس:
https://red-bank.ir/download
) انجام احراز هویت و افتتاح حساب، مبلغ ۱۰۰ هزار تومان هدیه افتتاح حساب دریافت می‌کنند.
🟡
همچنین هر کاربر می‌تواند با دعوت از دوستان خود از طریق لینک اختصاصی، به ازای هر افتتاح حساب موفق، ۱۰۰ هزار تومان پاداش دریافت کند.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/657668" target="_blank">📅 16:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657667">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سامانه کنترل قیمت مسکن به تصویب هیئت وزیران رسید
علیرضا نثاری، رییس کمیته مسکن کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
وزیر راه و شهرسازی در جلسه‌ای اعلام کردند این سامانه در هیئت وزیران تصویب شده و کارهای پایانی آن انجام شده است و به زودی آغز به کار سامانه شروع خواهد شد.
🔹
در این سامانه قرار است سقف افزایش قیمت‌ها مشخص و قیمت‌ها کنترل شود. اگر کسی از این قیمت‌ها عدول کند نیز از مراجع قضایی و حقوقی قابلیت پیگیری داشته باشد. سامانه به این شکل است که هرگونه قرارداد رهن، اجاره، خرید و فروش در آن ثبت می‌شود و قیمت‌گذاری در آن فرایند تعریف شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/657667" target="_blank">📅 16:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657665">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
با تصمیم شورای معین شورای‌عالی انقلاب فرهنگی، تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/akhbarefori/657665" target="_blank">📅 16:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657664">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای اسکای نیوز: پیشنهاد جدید ایران برای آمریکا ارسال شده است
اسکای نیوز:
🔹
ایران پیش‌نویس پیشنهاد جدیدی را به ایالات متحده ارسال کرده است. این رسانه همچنین ادعا کرده که طرف آمریکایی این پیشنهاد را «قابل قبول» می‌داند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/akhbarefori/657664" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657661">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWVmsqV9JBH_HHrD7OQCeE5Ll7zfHfdrLnPBEdSYxukliKWWwsgkKCLFS1xXK3Mmnxvlf_oaCNVaRJjUxktUWYh4DjIZkuIcub_nuisCNVPNpcplavdUeNG49ofvz-WNsiDMZUjYR7nfKT4DiEMidPImA91k7qBszsxuDMb_VABmz0x336ZFOOln4L_sAhASjwFtxG_c_HTcqQlVQWX67Ks--_CRjs1sqEP9vScI45z9qKMeqaGYG9VKLrud96Dod6ZrOgQl8uRa6N3j06pa5kqyWWfSUe7-yMQpuitNO3G-rkt_hPBOmjosi05gDTT9HyWAHuoH-gTZBnrvMiX4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6aad3ad89.mp4?token=TNxmCJh__i2dg5zTvDIDjfdCBg94opKlRdtlp-puVtVB-2oiu0K4EGYcWH_1dmos2GGl4K9R72LvC5od3-RfDN0jZDFhlkDQG3mQVmYxREMa3TvtEXSzaGiv85_ZZsCBjubklHrDzp5ydN-3yfh8mSggHVL2LSwxrKlOxqHAAns-pF0jg0M47F2oaHW_C8mAYNvJz51SKiNisPcTO2u6_nMqziJLQRmfWyc3siEkp4vCtgDhPcPar8dc3gwKdl8eN44URofn4E4lk7kn2uEqIbdYBFiP-tm6DVVJ9WboLuge28dXsxYjqoiIa7FM3Lcq5zR2hH6_UiZ99RC50vFL9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6aad3ad89.mp4?token=TNxmCJh__i2dg5zTvDIDjfdCBg94opKlRdtlp-puVtVB-2oiu0K4EGYcWH_1dmos2GGl4K9R72LvC5od3-RfDN0jZDFhlkDQG3mQVmYxREMa3TvtEXSzaGiv85_ZZsCBjubklHrDzp5ydN-3yfh8mSggHVL2LSwxrKlOxqHAAns-pF0jg0M47F2oaHW_C8mAYNvJz51SKiNisPcTO2u6_nMqziJLQRmfWyc3siEkp4vCtgDhPcPar8dc3gwKdl8eN44URofn4E4lk7kn2uEqIbdYBFiP-tm6DVVJ9WboLuge28dXsxYjqoiIa7FM3Lcq5zR2hH6_UiZ99RC50vFL9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش احساسی پاندا «فو بائو» به صدای مراقبش منتشر شد
🔹
این پاندا پس از حدود سه ماه دوری از مراقبی که از بدو تولد کنار او بوده، با شنیدن صدای او واکنشی قابل‌توجه نشان می‌دهد؛ لحظه‌ای که توجه کاربران فضای مجازی را به خود جلب کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/akhbarefori/657661" target="_blank">📅 16:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657660">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ستاد ویژه ساماندهی و راهبری فضای مجازی فقط جنبه مشورتی خواهد داشت
🔹
با موافقت رئیس‌جمهور «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» اصلاح شد و این ستاد فقط جنبه مشورتی خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/akhbarefori/657660" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657659">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سه نجات یافته از حوادثی که هیچ کس فکرش را نمی‌کرد
​​
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/657659" target="_blank">📅 16:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657658">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
قیمت‌ مصوب ۴ قلم محصول لبنی اعلام شد
🔹
شیر نایلونی کم چرب ۹۰۰ گرمی ۸۴ هزار تومان
🔹
شیر بطری کم چرب یک لیتری ۹۸ هزار تومان
🔹
پنیر یواف ۴۰۰ گرمی نسبتا چرب ۲۰۳ هزار تومان
🔹
ماست دبه‌ای کم چرب ۲ کیلوگرمی ۲۲۸ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/657658" target="_blank">📅 16:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657657">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
قیر ۴ برابر طلا سود داد!
🔹
از ابتدای مهر سال گذشته، برخی دارایی‌های قابل معامله در بورس کالا بازدهی چشمگیری فراتر از طلا و سکه ثبت کرده‌اند.
🔹
قیر با ۲۵۱ درصد سود در صدر بازدهی‌ها قرار گرفته که ۳.۷ برابر بیشتر از طلا سود داشته است. پس از آن، شمش نقره با ۱۵۰ درصد و مس کاتد با ۱۱۴ درصد رشد، عملکردی بسیار قوی داشته‌اند. در ادامه، شمش طلا با ۶۸ و شمش روی با ۶۴ درصد سود در رتبه‌های بعدی قرار گرفته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/657657" target="_blank">📅 16:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657656">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای ارتش صهیونیستی: یک نیروی حزب‌الله از مرز عبور و به‌سمت نیروهای ما شلیک کرد  رسانه‌های صهیونیستی:
🔹
به‌دلیل حادثه امنیتی مشکوک به نفوذ رزمنده‌های حزب‌الله، از شهرک‌نشینان مسکاف عام، مرگلیوت و مناره خواسته شده در خانه بمانند و جاده‌های این منطقه مسدود…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/657656" target="_blank">📅 16:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657655">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llnabQUP5UAmOg9mCR5aSztGUgA4lQbxabRsS3ItgZkdQ6jCvcwj4EFIUTdc6ylmlVfr7CfKhYu4RyBkn-YsHAbYbhy4PRAaBVNL3YzK7DdMWs5ZZKudToquK9ISklL3KZ5_ckODZI5yK_3Q8bPjuO2RlH7KcbUF54z1hHg6X7YUlAmnOyBEtmCwiybOhesfChVRN1tgUkQu6gU7xyOnFSVOdOf2WthOiu5GOe-6QsNNwdfCgtQRUkBIPGD-mm6xtOLMkKq85pzsKpH4RdpIZYIU2Y5JxX7ixSkpRROxLvur-yIUtyjr6lxLMOEIH8z4GCSV8V1qQHigKrFXvuvyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قانون عجیب جام جهانی ۲۰۲۶؛ نیمکت‌نشین‌ها در رختکن آماده می‌شوند!
🔹
به‌ دلیل گرمای شدید در برخی میزبان‌ها، احتمال دارد بازیکنان ذخیره تا لحظه نیاز در رختکن بمانند و فقط هنگام تعویض برای گرم‌کردن فراخوانده شوند.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/657655" target="_blank">📅 16:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657653">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJtlxpwMOixTOAQtSZdSvbP09vh4cFoDdYrd1PzODZUsclpQ6rchCvgxxSrCmxrxc2fCGflDtdAmXvb5lijgULwauZjRb-XSvMk3VQjJrN0m2Lk9ku_r1IlLq2biLNkLylSXS0kcEObFXfhsqAEAebHGTmh_VtaC5KarRKus2NfN28JQ_2a2DSt3jUmQNxFpOkwNIT86RUV_n3FT7_fPYjj3TNVqJBH4WPbWiP4EnjnN_2kxzzGTDsfXLZTUo_4UQUpHhjOf6T9ivwtkx27YhllGYeBbdWlK1IKG978jEL8UpEhomAeJsJwS3tQlU-YXIhyBGdk29AORdnGo5eRkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا سقوط هلیکوپتر خود‌را در تنگه هرمز تایید کرد  سنتکام:
🔹
ما دو خدمه یک بالگرد آپاچی را پس از سقوط آن در نزدیکی سواحل عمان در حین گشت‌زنی نجات دادیم./ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/657653" target="_blank">📅 16:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657652">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای ارتش صهیونیستی: یک نیروی حزب‌الله از مرز عبور و به‌سمت نیروهای ما شلیک کرد
رسانه‌های صهیونیستی:
🔹
به‌دلیل حادثه امنیتی مشکوک به نفوذ رزمنده‌های حزب‌الله، از شهرک‌نشینان مسکاف عام، مرگلیوت و مناره خواسته شده در خانه بمانند و جاده‌های این منطقه مسدود شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/657652" target="_blank">📅 15:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657651">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c267b4079.mp4?token=rGz8iGvqBujxcHd1keNFBSx26AxLjIS_8wkzSkRSE1gvWIxnMVtTCz37pmpiUvxS3mJ3_KOJ__ctEFn3V5pJZ1cOfxGT9i4vjGJv2OeEcKPkmXLaqEqUdJ6TfzL5cAJtnV7BUsy0XrzqID7lcZbKfQFIpQmQxO8mxaaHx3EjjXsEA3POSiHp8dINJ5GQC_U8XZZAm3zdnR3e_myZuR80nTANM42-h9iRrZsM1J7Pi0DCx4hVsOTD9SF2NLCsJyKRreFy9YsKNTTq5ZK49FPrQJjrXskE8Yn7rlmdE9eowLFfJ_Y5wR1YBcmrdvnSljshpaxOJ_Yw5eyqTe8i50WaFxCN0jwDduEbyJmy12vE3PuFubOc6S9HJm3x7VmRvYyZmmnQNaBaTROOa051M7l_5pUPBx_hOmVirKbtLSOOk67DBhj1yUhecRR_LGUXc2BpQeL_UA18KX97Xferx0OkEVvk-iI7QceY4o4RZziRkcWr8aQ-7J1dHl9AOxP6jQonubsGs1d58iJ0rutBcz0g5efkS9Lx5kqPcDt8zSFNO5N3GE2v87cGeuhFxynDGszFGvshB8nnFo_xvwRmlccssd4ecnJIJxlh6oua2m0ST6E0lCM9Jpxpk5wVworXm2pa4394XrRElPrL2qddGE0a9iYTI7Ww9XtHVnjXIDhV_kI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c267b4079.mp4?token=rGz8iGvqBujxcHd1keNFBSx26AxLjIS_8wkzSkRSE1gvWIxnMVtTCz37pmpiUvxS3mJ3_KOJ__ctEFn3V5pJZ1cOfxGT9i4vjGJv2OeEcKPkmXLaqEqUdJ6TfzL5cAJtnV7BUsy0XrzqID7lcZbKfQFIpQmQxO8mxaaHx3EjjXsEA3POSiHp8dINJ5GQC_U8XZZAm3zdnR3e_myZuR80nTANM42-h9iRrZsM1J7Pi0DCx4hVsOTD9SF2NLCsJyKRreFy9YsKNTTq5ZK49FPrQJjrXskE8Yn7rlmdE9eowLFfJ_Y5wR1YBcmrdvnSljshpaxOJ_Yw5eyqTe8i50WaFxCN0jwDduEbyJmy12vE3PuFubOc6S9HJm3x7VmRvYyZmmnQNaBaTROOa051M7l_5pUPBx_hOmVirKbtLSOOk67DBhj1yUhecRR_LGUXc2BpQeL_UA18KX97Xferx0OkEVvk-iI7QceY4o4RZziRkcWr8aQ-7J1dHl9AOxP6jQonubsGs1d58iJ0rutBcz0g5efkS9Lx5kqPcDt8zSFNO5N3GE2v87cGeuhFxynDGszFGvshB8nnFo_xvwRmlccssd4ecnJIJxlh6oua2m0ST6E0lCM9Jpxpk5wVworXm2pa4394XrRElPrL2qddGE0a9iYTI7Ww9XtHVnjXIDhV_kI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در فینال بسکتبال آمریکا چرت هم می‌زد
🔹
رئیس‌جهور آمریکا علاوه بر هو شدن توسط مردم، در میانه‌ی بازی فیتال لیگ بسکتبال حرفه‌ای کشورش، با چرت زدن خود توانست برای بار دوم به فاصله چند دقیقه، تبدیل به سوژه‌ی داغ رسانه‌ها شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/657651" target="_blank">📅 15:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657650">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXtf18BHDBaIBXIuUQnWA9ftfUEs8MEtX1IAOeNqE2isHSAyj1_5b8YX6OiKZ8cKmiTPejzC265kleKaOamHbt_2YAZJLzOEAQkHHcCXvCYSqjikCaZNkgaurz5TkHbJc2IjA4KSJGKncO1nqRYeaZg9kcyyMkcBFHNdBdp0fZdTdiHY7h3thRUKMRgMmyg1HxHj2EVAsmZpqum1LECeTuhpKIC4XWBeIL_wcYfs8pNi9g2Y6rboKqrLKjAY7PHnQjsADxX9C_ZoSs5E9IfHYs2gvHgnwpo1dJEB5G0ZXK8XWXgN2d8KmMPIYp0yEY4pkbRVcopsl3tf1bV7z3inWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات معیشتی در صدر خواسته‌های بازنشستگان
🔸
در این نظرسنجی حدود ۳۰ هزار نفر شرکت کردند که سهم روبیکا ۵۸ درصد، بله ۳۰ درصد و تلگرام ۱۲ درصد بوده است.
🔸
بیش از سه‌چهارم شرکت‌کنندگان، افزایش و همسان‌سازی حقوق متناسب با تورم را مهم‌ترین مطالبه بازنشستگان کشور دانسته‌اند و حدود ۱۰ درصد نیز پوشش کامل هزینه‌های درمان را در اولویت قرار داده‌اند.
🔸
مطالبات بازنشستگان بیش از هر چیز بر حفظ کیفیت زندگی و تأمین امنیت اقتصادی و رفاهی در دوران سالمندی متمرکز است.
@amarfact</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/657650" target="_blank">📅 15:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657649">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkHv6FNhREOtORemuMG2LwNTBP_Ty5GvqR25V6uel2NBc_ccQ_uNg82BKPWRfMeGrFj-2OGbHkNNhw1yu0FVJzLIcbTjEV6veH-kSRYXtqHCzrlc3OiYueb8EcH2lhpjni7Uf_BTBXYW_04mjuWpq_yqO65XhxL5OMS0VM5mjiBxeFPMk1NTr1CurFW04r-iazeRGLFToiK3bphuifjgi3fuFAAIBWAxI2AAh1NmYl4gM7GXaydKanSWYHlcSeugaj6pMAU8tKVzjHShzrevZeOHkb3bRmgnS7uKqUTQIR5BU_JTPymrjGrmR-WA2EWqRVIdVEKFtinA6tXlJxD8Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونس: ایران برای ما یک باتلاق طولانی نخواهد بود
جی‌دی‌ونس، معاون ترامپ در گفتگو با یو‌اس‌ای تودی:
🔹
مطمئنم که دخالت آمریکا در جنگ ایران ظرف یک سال پایان خواهد یافت و به یک باتلاق طولانی تبدیل نخواهد شد. آمریکا یک سال دیگر درباره جنگ ایران صحبت نخواهد کرد.
🔹
کمپین آمریکا در ایران مانند جنگ‌های طولانی مدت در عراق و افغانستان نخواهد بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/657649" target="_blank">📅 15:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657648">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر نفت: منابع حاصل از کاهش واردات بنزین صرف بهبود معیشت مردم می‌شود
🔹
انصارالله یمن: ممنوعیت کشتیرانی اسرائیل تصمیم راهبردی صنعاء است
🔹
ورود سران صهیونیست به برخی‌ کشورهای اروپایی ممنوع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/657648" target="_blank">📅 15:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657647">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
پیش‌بینی مقام اسرائیلی از درگیری دوباره با ایران در روزهای آینده
🔹
یک مقام ارشد امنیتی اسرائیل در گفت‌وگو با شبکه کانال ۱۴ اعلام کرده است که بازگشت به درگیری‌های گسترده با ایران تنها مسئله زمان است و احتمال وقوع آن در روزهای آینده نیز وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/657647" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657645">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594890a614.mp4?token=Nim0Zq6xofudHIAnciNn2wpJmbLgakgbPHTwbBn3X5bn8HpDfouPrFYuMfYiJeGKm-3lRp2Msp_IYoxCF94rKY-PUrz6wdO3Lkuw8CFY_x7T0w-u4lEYf8JH3QvvG3RtU5fSuMN5uqBO9NciT8tvvi6S3nJoWOXKLUuz0kBPP4w5yy2wM6QSrtVGXfAJmvjcpQzAblZYG_PriWpPbOKxgd7zZw0Hu-H06GJwPicbZaV8FUcfn6Ik9-SXpRVVZBoshVJ2SdlA6B9tgVTutsm7SMpSpArylmsC41Tuyg23XCJMxvYngqJoEye_c1aIylqjZuL6TnxcSNtquQ_aK7tGBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594890a614.mp4?token=Nim0Zq6xofudHIAnciNn2wpJmbLgakgbPHTwbBn3X5bn8HpDfouPrFYuMfYiJeGKm-3lRp2Msp_IYoxCF94rKY-PUrz6wdO3Lkuw8CFY_x7T0w-u4lEYf8JH3QvvG3RtU5fSuMN5uqBO9NciT8tvvi6S3nJoWOXKLUuz0kBPP4w5yy2wM6QSrtVGXfAJmvjcpQzAblZYG_PriWpPbOKxgd7zZw0Hu-H06GJwPicbZaV8FUcfn6Ik9-SXpRVVZBoshVJ2SdlA6B9tgVTutsm7SMpSpArylmsC41Tuyg23XCJMxvYngqJoEye_c1aIylqjZuL6TnxcSNtquQ_aK7tGBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت ۳۷ وعده ترامپ درباره توافق با ایران
🔹
ترامپ بار دیگر گفت توافق با ایران «ظرف دو هفته» انجام می‌شود
🔹
ادعایی که در ادامه ۳۷ نوبت اظهارنظر مشابه او در سه ماه گذشته است. در این ویدئو خواهید دید
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/657645" target="_blank">📅 15:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657644">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
قیمت نفت سبک و سنگین ایران در بازار جهانی افزایش یافت
🔹
بر اساس داده‌های سایت اویل پرایس، قیمت محموله‌های نفت ایران با تأخیر یک روزه منتشر شده و نسبت به روز قبل رشد حدود ۲ درصدی داشته است. همه گریدهای ایرانی نسبت به روز قبل ۱.۸۱ دلار افزایش قیمت داشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/657644" target="_blank">📅 15:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657643">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
مهاجرانی: بودجه بر اساس دخل و خرج کشور بسته‌ می‌شود نه جنگ/ اگر نیاز باشد اصلاحاتی در بودجه انجام خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/657643" target="_blank">📅 15:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657642">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
مهاجرانی: دستور اجرای افزایش حقوق کارگران ابلاغ شده است
سخنگوی دولت:
🔹
وزیر تعاون، کار و رفاه اجتماعی، دستور اجرای افزایش حقوق کارگران را ابلاغ کرده و همچنین، حکم‌های مربوط به حقوق بازنشستگان و مستمری‌بگیران نیز صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/657642" target="_blank">📅 15:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657641">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0439452658.mp4?token=EJa4Pc1Fj5bgVMbxKUEdK1_GvXsiT10QtfK48J1QbRYlFApcXgKQmWx9j_qxeylDggbZ9uxGTJNJ3h0GFLUS4SMsbxZzn-JKHD-VrmSGbZwKZrNmbXP_0ZZ50GwUO2DA8aTDK0zBDjjW4Par6KsMe7KMJOm4jbJ3Coy9A-REN-syCCRl2u-EYeesGkvFHlKgzs9pUnFe8t46iLCmuzqIUZQfSJgNDeUx-Mo2bYi401d1_hBMHJuDI5a-_Rp8F3EfKYqMZmay2WAFpxtpoBrXwqDpd5JCm6AHZBUz3gncKhmgp2sZ8OffXFCWs2abLboVnx_mwxcKRPw5vnz_-sOr-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0439452658.mp4?token=EJa4Pc1Fj5bgVMbxKUEdK1_GvXsiT10QtfK48J1QbRYlFApcXgKQmWx9j_qxeylDggbZ9uxGTJNJ3h0GFLUS4SMsbxZzn-JKHD-VrmSGbZwKZrNmbXP_0ZZ50GwUO2DA8aTDK0zBDjjW4Par6KsMe7KMJOm4jbJ3Coy9A-REN-syCCRl2u-EYeesGkvFHlKgzs9pUnFe8t46iLCmuzqIUZQfSJgNDeUx-Mo2bYi401d1_hBMHJuDI5a-_Rp8F3EfKYqMZmay2WAFpxtpoBrXwqDpd5JCm6AHZBUz3gncKhmgp2sZ8OffXFCWs2abLboVnx_mwxcKRPw5vnz_-sOr-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مناظره داغ و جنجالی رسانه آمریکایی سی‌ان‌ان درباره ایران
🔹
ایران چند آمریکایی را در خاک آمریکا کشته است؟ جواب صفر؛ چرا سربازان ما در خاورمیانه بودند؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/657641" target="_blank">📅 15:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657640">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: جنایت آمریکایی‌ها در لامرد کمتر از میناب نیست
🔹
موضوع حمله آمریکا و صهیونیست‌ها به مدرسه لامرد باید به پرونده‌ای برای رسوایی آمریکایی‌ها و حامیان و پشتیبانان آن‌ها تبدیل شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/657640" target="_blank">📅 15:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657638">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWw_LornMC8qrLAxmPmAZWNhsE9oNk7fsVu1Jb875AAqfdtXDDCBuot-sMPlLZ2NKuPxtqiq1Mb3j7dBA7No_e3xhaCQKtIDxH3AVQjQNFhhT3MuKmLXD0OpubKn-5RjAsEGUaj5bafbKqHnlzdskSnZWOSvK1u6q6OCyGESWvzYYCZf6Z7ROX4mxnh-J1VXf-Us6cpt3y9L2ubagAH-a4RE_losZJHOXml6dPJTxpa4Ecgi9dlbktYxV1jDkB05mJwnKzRvxHbpot8QUSCX8kcJ33sg6Bq-Rm7UxgkLH-1Ho29d-5Lk2HKZZW7GtVVKr8JInppVGyFtz2SQoRkDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یدیعوت آحرونوت: تصاویر ماهواره‌ای نشان می‌دهد که دو روز پیش یک موشک ایرانی با دقت به یک آشیانه در داخل پایگاه هوایی رامات دیوید اسرائیل اصابت کرده است
/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/657638" target="_blank">📅 15:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657637">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
کانال ۱۴ اسرائیل: کابینه امنیتی تصمیم گرفت که هر موشکی که از لبنان به سمت اسرائیل شلیک شود، بدون تأیید سیاسی با حمله به بیروت پاسخ داده خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/657637" target="_blank">📅 15:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657636">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اسرائیل مدعی ترور ۲ فرمانده جهاد اسلامی شد
🔹
ارتش اسرائیل مدعی شد دو فرمانده ارشد وابسته به جنبش جهاد اسلامی فلسطین را در حمله‌ای هوایی در جنوب غزه هدف قرار داده و عملیات موفقیت آمیز بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657636" target="_blank">📅 14:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657635">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای اسرائیل هیوم: مارکو روبیو نقش کلیدی در متقاعد کردن ترامپ برای حمایت از حمله اسرائیل به ایران پس از حمله موشکی تهران ایفا کرد
🔹
بر اساس منابع اسرائیلی و آمریکایی، روبیو از استدلال اسرائیل حمایت کرد که عدم پاسخ دادن به ایران برتری می‌دهد و تشویق به حملات بیشتر می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/657635" target="_blank">📅 14:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657634">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای سفیر اسرائیل در واشنگتن: امیدواریم جنگ با ایران ظرف دو هفته پایان یابد/ می‌خواهیم جنگ را به گونه‌ای پایان دهیم که تضمین شود ایران برنامه تسلیحات هسته‌ای یا موشکی ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/657634" target="_blank">📅 14:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657633">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bbab9bb2.mp4?token=PlavUTIVmCv3uMdjv7eb6vz9vnAndvxBG1TRwxHiJ-bxjqgFALRd88sdw3z39zfgdMeqpHPQUO7xje6PPx_5V31z-y6GKjQl4WyPuHUuUC7VGX0vncCE15bS5I67ORtCALsUy9fcCAFlarYtMYFunnx9cIlerGa1olKZNSoCJXx1yORDnoPSiH7GPyWOnSy6CamhQRDKbcVueIKrVE6mOp8hBP34nbZUgRxDv0IxEYovxRw7xBKw5oDJglrJEm_v4KQRX-7ZU1cMVEIi_j5M4qBmyD9wuDKMa3qYtrn_9Cp5jM8ccu0daxEge8295GtlWYryAGZJ897q6aqRjTvZDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bbab9bb2.mp4?token=PlavUTIVmCv3uMdjv7eb6vz9vnAndvxBG1TRwxHiJ-bxjqgFALRd88sdw3z39zfgdMeqpHPQUO7xje6PPx_5V31z-y6GKjQl4WyPuHUuUC7VGX0vncCE15bS5I67ORtCALsUy9fcCAFlarYtMYFunnx9cIlerGa1olKZNSoCJXx1yORDnoPSiH7GPyWOnSy6CamhQRDKbcVueIKrVE6mOp8hBP34nbZUgRxDv0IxEYovxRw7xBKw5oDJglrJEm_v4KQRX-7ZU1cMVEIi_j5M4qBmyD9wuDKMa3qYtrn_9Cp5jM8ccu0daxEge8295GtlWYryAGZJ897q6aqRjTvZDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات سخنگوی دولت درباره حذف یارانه برخی دهک‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/657633" target="_blank">📅 14:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657632">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde5aa2c4e.mp4?token=oTMZh2HXMJ6TFhBSNOG_IMp0WogmBHFgu3k0BUEugHQG5DropsuZ4D619N-tzRM5dOJ84C8V2coCza0tI9m_mT9KS1JDmFdTNrl40ICw-hPj6WXWe9BZW2IrJDxdG-dFeuWnHyehqolQU9Me_086tBegfoeVvaxzQshSRaYTOcbahzcQJYvW1uDxsNPtHfx6vX8eDrGs5EPCJo0d5ZT2M9c4bwMiT-ZRH1KiL0q8oRFMkwssbaZS1eLmJL-G_x7qUsOAnt6wOYANmoPRLc77qWaB6QengVrdsZx-WfPmdck3eC0ryi2L9Qf1Cu-8mPRio0_s9KW5SNc2t84GSOb31w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde5aa2c4e.mp4?token=oTMZh2HXMJ6TFhBSNOG_IMp0WogmBHFgu3k0BUEugHQG5DropsuZ4D619N-tzRM5dOJ84C8V2coCza0tI9m_mT9KS1JDmFdTNrl40ICw-hPj6WXWe9BZW2IrJDxdG-dFeuWnHyehqolQU9Me_086tBegfoeVvaxzQshSRaYTOcbahzcQJYvW1uDxsNPtHfx6vX8eDrGs5EPCJo0d5ZT2M9c4bwMiT-ZRH1KiL0q8oRFMkwssbaZS1eLmJL-G_x7qUsOAnt6wOYANmoPRLc77qWaB6QengVrdsZx-WfPmdck3eC0ryi2L9Qf1Cu-8mPRio0_s9KW5SNc2t84GSOb31w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کپلر: تردد در تنگۀ هرمز به‌شدت کاهش یافته است
مؤسسۀ رهیابی دریایی کپلر:
🔹
داده‌های ماهواره‌ای از محدود شدن قابل‌ توجه تردد کشتی‌ها در تنگۀ هرمز حکایت دارد. در ۳ روز جمعه، شنبه و یکشنبه تنها ۸ شناور تجاری و غیرتجاری از تنگۀ هرمز عبور کرده‌اند؛ رقمی که تقریباً نصف میزان تردد در آخرهفتۀ قبل است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/657632" target="_blank">📅 14:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657631">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
بورس در چند قدمی قله؛ حقیقی‌ها خریدند، حقوقی‌ها فروختند!
🔹
امروز در بازار بورس، حقیقی‌ها ۷.۹ همت پول وارد بازار کردند و ارزش معاملات خرد حدود ۱۶ همت ثبت شد. در سمت فروش، ۶۷ درصد توسط حقوقی‌ها انجام شده، در حالی که حقیقی‌ها فقط ۳۳ درصد فروشنده بودند.
🔹
شاخص کل با جهشی خیره‌کننده‌ ۱۱۴ هزار واحدی به ارتفاع ۴,۵۴۰,۸۷۴ صعود کرد. یعنی چند قدمی قله تاریخ! مهم‌تر از همه، ۹۵ درصد نمادها مثبت بسته شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/657631" target="_blank">📅 14:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657630">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd4f1e481.mp4?token=bL6ebIrcv8FvHNw6GlBe1F0TSZAT0UFt0eeD4zJnrGCnAm6xBEKWnnvnHAKbsv1nj0j7LZeZrieDyu1Aik-hyAWpCkBBDDMXpkR1C55VwGwE0ddO2XlnJQRQol6_6M-NBsiBJ77Za9sz2HUPSoYvo5Jcmh0B3nNgUmkl5AUiB6832Fpo_vDokCa52l9UVE98Q3btJ4KEg7YWlRDYrvaGvlvbaBFtm_ZflCDe3MxovfMoXKKS1mkmU3NeDEflE3ZxFAsLxXo9dulYAvsEGnKbqOWt6kn7zwK7sbTKnZFB8iyNSP6uRYJJf3vrt5ZrMyLKFnSJgT6gm1JqiOMV_nTFgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd4f1e481.mp4?token=bL6ebIrcv8FvHNw6GlBe1F0TSZAT0UFt0eeD4zJnrGCnAm6xBEKWnnvnHAKbsv1nj0j7LZeZrieDyu1Aik-hyAWpCkBBDDMXpkR1C55VwGwE0ddO2XlnJQRQol6_6M-NBsiBJ77Za9sz2HUPSoYvo5Jcmh0B3nNgUmkl5AUiB6832Fpo_vDokCa52l9UVE98Q3btJ4KEg7YWlRDYrvaGvlvbaBFtm_ZflCDe3MxovfMoXKKS1mkmU3NeDEflE3ZxFAsLxXo9dulYAvsEGnKbqOWt6kn7zwK7sbTKnZFB8iyNSP6uRYJJf3vrt5ZrMyLKFnSJgT6gm1JqiOMV_nTFgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک نظامی عالی‌رتبه ارتش روسیه در مسکو ترور شد
🔹
کمیته ارشد تحقیقاتی روسیه اعلام کرد که در نتیجه انفجار امروز راننده یک خودرو جراحات متعددی برداشته و در محل انفجار که حدود ساعت ۵:۳۰ صبح به وقت محلی رخ داد، جان خود را از دست داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/657630" target="_blank">📅 14:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657629">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
نماینده ایران در آژانس بین‌المللی انرژی اتمی: تجاوزات و تهدیدهای مداوم که شرایط استثنایی فعلی را ایجاد کرده‌اند، متوقف نشده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/657629" target="_blank">📅 14:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657628">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTfvoSqiIzK_l6PbO3DOtTR4kuxG1CyEYHFbDFGZ-3sAH9dxNwAKxgZdHjobkVj6XjTzvvqezN8-utjbz2VBQHmnRqmhO68-1VWb3WTb7oX-QegR7trqFtTGJxRWtWwlxK0w-cNty64ivIzsVwYXntManegpa-u6HNOEclFew8yb0z8lxhhvDdJeBlHL-bQVRHgnaC2QUxjfuWwTBY2ecWv1nFJ4-SVoCkPjSBf8ZBi1vYF8i_myhwMq6a_Bh8AxtECrd2G27yL-BeQ3xxPBiKcWxRR32_TXABnzethgdB-3xjm0fj_3sZJfAJ1oqdlxXYvJuQn7uXP8blSoyjADVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از پوستر تیم ملی والیبال ایران در لیگ ملت‌های ۲۰۲۶
🔹
استادیوم ۱۲ هزار نفری آزادی در جریان جنگ رمضان مورد هدف موشک‌های رژیم صهیونسیتی و آمریکا قرار گرفت.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/657628" target="_blank">📅 14:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657627">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای یک منبع پاکستانی در گفت‌وگو با العربیه: اسلام‌آباد در حال انجام تماس‌ها و رایزنی‌هایی با همه طرف‌هاست تا در همین هفته به یک تفاهم دست یابد/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/657627" target="_blank">📅 14:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657626">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtQFXAObQ9lgbPMmP2EV2q8p9r5lsgIhGYStIothqouse_mp5XT3nPplSzYxQpY3Lb9mi2PMVSMLE7N2fU3wo8-H5O2X6bGsXaXgS8B0q6BWjwnouyc4DlYtO2z0sgOEj4z-mOL8Ck_KZsi_amzazdNgBO6WagMs1ivRetSgrfm-8YjHRcoJeNmB4rsAcjud3o_TDNXXPR9ZXUkJOUbdjdwvZFNQByJDRI6qJXLEf7zR-9udmjsT3DyXo4AYibEqK_4lremE2iG0_Y5zq7Hn9PFGUWhXmUKzh_0IyCWTM1-6m4NdghGGVyoq9jXuFU4EwHKdTZ7JWzWVhuPyuhmAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران برای تحقیر ترامپ، بازی ۱۹۷۹ را آغاز کرد!
سایت تحلیلی Conversation:
🔹
ایران بحران گروگانگیری ۱۹۷۹ را کش داد تا آمریکا را تحقیر کند. ایران نقش کلیدی در شکست جیمی کارتر، از رونالد ریگان در انتخابات ریاست جمهوری ۱۹۸۰ ایالات متحده داشت. آنها ۵۲ گروگان باقی مانده را تنها چند دقیقه پس از مراسم تحلیف ریگان در ژانویه ۱۹۸۱ آزاد کرد.
🔹
بن‌بست فعلی با ایران تنها ۱۰۰ روز قدمت دارد و به نظر می‌رسد ایران اکنون آماده است تا از استراتژی مشابهی برای تنبیه ترامپ و نتانیاهو به خاطر حمله به ایران استفاده کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/657626" target="_blank">📅 14:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657625">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
وزارت دفاع: دست رزمندگان اسلام را پرتوان‌تر خواهیم کرد
وزارت دفاع و پشتیبانی نیروهای مسلح در بیانیه‌ای ضمن قدردانی از حماسه ۱۰۰ روزه ملت ایران:
🔹
وزارت دفاع و پشتیبانی نیروهای مسلح این حضور کم‌نظیر را پشتوانه‌ای ارزشمند برای مجاهدت‌های فرزندان ملت در نیروهای مسلح می‌داند وبا همه ظرفیت‌های علمی، صنعتی و دفاعی کشور، روند تولید و توسعه تجهیزات، تسلیحات و سامانه‌های مورد نیاز نیروهای مسلح را با قدرت و شتاب بیشتری دنبال میکند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/657625" target="_blank">📅 14:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657624">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5fb5c1a7.mp4?token=O9Ir__wIKmPs4eAfhtRQ5zgfdJFWNjQ1zyQSeLBEQiORYRDG6KPpp0ejAv_AcpnKeZppiBs5E7ivyRuWt97a81ZCbKowHj6fNU_aN08xj94hXaCA9g2w8DdEQRE3SmEL7x2ziiorjFK_J7YMv6l1XyvBjLUk1K6k1IiZjQqPCgWvg7XDcjcRZ_M-rWZvBR5BwEMJMcZH_fpVhMn5-slbEcqsdiJa317yXPePwfrjReX_TyhimjTr9t-9uWfXj0tDF3DTGBO2izUKN6igcQoznPr49SasqHwZhGJrUnRILGLBdUgt5ryURO1DxTHYUIOjJd9SOXhgypZm3vod5A9AvasuJHBamvv65rJ51sDjqwK5V9gMI_U97iQkiaEdYSRdBI92__o8NQlNHvi6TXecOy1Hu1y4dq5TXMs2CyR6JFw75bB9Z0SoXy4ccwkK6hrC09lKEbc-6FSBdjeIYjnIC10ffuG7GKt29p7J3mUeaztk7YYt8P0u1rYFvPXTmO2xqg9jvLDc61L6khdnb-5OS6VUJ1iUw68Q4L62qzOlMzsm3Ss9JRoTYkBWnnPqiEE82tDa512o9BvlkJ41PWKz-NDDab5PY7WoPx2rYM1HF0KlShT4WPBsVqBuLFDs0eXbLRjY3T6jkKRfuZGnio8z7M8JmQB5AnjJIx4uJiPRp9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5fb5c1a7.mp4?token=O9Ir__wIKmPs4eAfhtRQ5zgfdJFWNjQ1zyQSeLBEQiORYRDG6KPpp0ejAv_AcpnKeZppiBs5E7ivyRuWt97a81ZCbKowHj6fNU_aN08xj94hXaCA9g2w8DdEQRE3SmEL7x2ziiorjFK_J7YMv6l1XyvBjLUk1K6k1IiZjQqPCgWvg7XDcjcRZ_M-rWZvBR5BwEMJMcZH_fpVhMn5-slbEcqsdiJa317yXPePwfrjReX_TyhimjTr9t-9uWfXj0tDF3DTGBO2izUKN6igcQoznPr49SasqHwZhGJrUnRILGLBdUgt5ryURO1DxTHYUIOjJd9SOXhgypZm3vod5A9AvasuJHBamvv65rJ51sDjqwK5V9gMI_U97iQkiaEdYSRdBI92__o8NQlNHvi6TXecOy1Hu1y4dq5TXMs2CyR6JFw75bB9Z0SoXy4ccwkK6hrC09lKEbc-6FSBdjeIYjnIC10ffuG7GKt29p7J3mUeaztk7YYt8P0u1rYFvPXTmO2xqg9jvLDc61L6khdnb-5OS6VUJ1iUw68Q4L62qzOlMzsm3Ss9JRoTYkBWnnPqiEE82tDa512o9BvlkJ41PWKz-NDDab5PY7WoPx2rYM1HF0KlShT4WPBsVqBuLFDs0eXbLRjY3T6jkKRfuZGnio8z7M8JmQB5AnjJIx4uJiPRp9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احیا و حقیقت | قسمت سوم: سرمایه مردم
🔹
روایت محمد جامعی از حمله ناجوانمردانه دشمنان آمریکایی‌صهیونیستی به زیرساخت‌های غیرنظامی ایران اسلامی در شرکت فولاد خوزستان
🔹
در آن یک دقیقه، فقط آهن و فولاد نسوخت. رؤیاهای هزاران نفر زیر آوار دود و آتش ماند. پشت هر سهم، یک زندگی بود؛ پس‌اندازی که قطره‌قطره جمع شده بود، امیدی که سال‌ها برایش صبر کرده بودند، آینده‌ای که قرار بود امن‌تر باشد.
🔹
فولاد خوزستان تنها یک مجتمع صنعتی نبود؛ بخشی از سرمایه مردم بود. سرمایه کسانی که به ساختن ایمان داشتند و سهمی از آینده این سرزمین خریده بودند.
و آن سوی ماجرا، هزاران کارگر ایستاده بودند؛ مردان و زنانی که چرخ زندگی‌شان با چرخ تولید می‌چرخید. با هر شعله‌ای که زبانه می‌کشید، نگرانی برای نان، آینده و امنیت خانواده‌ها نیز بزرگ‌تر می‌شد.
🔹
«احیا و حقیقت» روایت خسارت یک کارخانه نیست؛ روایت مردمی است که دارایی، امید و معیشتشان در دل این مجموعه جریان داشت.
روایت این حقیقت که وقتی یک صنعت هدف قرار می‌گیرد، آسیب تنها به سازه‌ها و تجهیزات نمی‌رسد؛ بلکه به زندگی انسان‌ها گره می‌خورد.
#از_نو_تو_را_آباد_خواهم_کرد
!
📱
@khouzestan_steel_co</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/657624" target="_blank">📅 14:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657623">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
اقدام خصمانه آمریکا و اروپا علیه ایران در نشست شورای حکام آژانس
رویترز:
🔹
آمریکا و سه کشور اروپایی پیش‌نویس قطعنامه‌ای علیه ایران را به شورای حکام آژانس بین‌المللی انرژی اتمی ارائه کرده‌اند. در این پیش‌نویس از تهران خواسته شده اطلاعات دقیق‌تری درباره ذخایر اورانیوم و تأسیسات هسته‌ای خود به آژانس ارائه دهد.
🔹
به گفته رویترز، در نسخه فعلی اشاره‌ای به ارجاع پرونده به شورای امنیت سازمان ملل نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/657623" target="_blank">📅 14:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657622">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6tXIBmZMVuMH5pOKULIscW78mgAUcQi1vzQ9o4gr2mzCJArfCrMm0Zq4DDk7A_DHORU7jC-TQo5oklW6J8XWGW8wQVDatj5r2D3t2YjlF5V9A_sp1gUk9V4Igq1nuRQ7XLEDdFOkC30fHAn8np0p2puLTCiphO6Lfe_GW3MA42u3hhjJQnPgA6IkfD8ihpEiVGIWIUoHYB5m1uc_FDM3djED9LVdgmSkCzHHnsNmNrZs0Or5AozvMiBcpKwwR0TRzBeKUu4AZcykmKtyXXKvIelaYDLUOhy0EHmZQOtf52jbH-OU8lleuoSYGForU-FTBupIXzU956qmI3qOxCMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران‌چک جدید ۱۰۰ هزار تومانی با تصویر مدرسه میناب
🔹
بعد از جنایات امریکا در مدرسه میناب و شهادت ۱۶۸ کودک دختر و پسر دانش‌آموز به همراه جمعی از معلمان، کارکنان مدرسه و والدین حاضر در محل، بانک مرکزی سری جدید ایران چک های ۱۰۰ هزار تومانی را با تصویر مدرسه میناب چاپ کرد.
🔹
این ایران‌چک‌ها به‌تدریج وارد شبکه بانکی و چرخه مبادلات پولی کشور می‌شود و از نظر ویژگی‌های امنیتی نیز مشابه نمونه های قبلی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/657622" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657621">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تیزر قسمت دهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم زینب حیدریان که ماجرای زمان کودکی و زیر آب رفتن در زاینده‌رود و رفتن در مسیری با نور سبز و ورود به جنگلی با درختان پر از میوه که اجازه خوردن از آن میوه‌ها را نداشت را نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: زینب حیدریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/657621" target="_blank">📅 14:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657619">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2YH2aQErSo-6ya5aWgvE3L4NHAn6MIPSjI1BO10vX0uEvbXYVp7KW5RueTyizZcBIW0zvz8GKH5CIO9r1rLuoeRY0IsKXqKonDIWMvR8sxC95jpk3I0-ft4E1A6BcKTOxfUAAileP7wXFT-qM1LGaDhh13eZbRTnQYTKwcNYkKGsAMMYEfbjCndthdq5sNJ08iJUYwNKqivYCALcI09-gOAJ3s5Yi2ZLGZzGJXb_D06LDV-XIrIwejN7khpWmXG-BUWQ3R-Dc9lle7nvVRlcxkCOGaRPuSfdZVXbAYXz72ZDpeYsKalwufmhSBc7SC3cTE5ZEcCp_ydH3QXRqb3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بالگرد نظامی آمریکا در نزدیکی تنگۀ هرمز
🔹
طبق گزارش نیویورک تایمز، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند./ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/657619" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657617">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIqpqE4fsWCdjypQHWWCfcRG9X-1WiQI3RGNNbdBOvbvfmGfozDAGOWgAiwKqlyzKVNyUfAhWWdEWPM_lDl39iiLWjHV6nxozQolnQk4wfrCkOn7paQocBTukmZvWzyl5omdm86W4HgsiPC65GCujuN96je3Ri8v0AWiRJ6Wn2RWYAHHvVw2jOCG3JFJtMUi0c_car1kPsAqzuV2njFVCBSfkPnNehZoOSygDtNYggno7ghp5gJXXRvJZHTOxpGfuu54XSOhlZj5Qbaj52AyymRTjmgouuAxDugIBdGK8iqCY3Tf1IY5xsBgTmFVo5aTPeoiH1h1fZg-8GK_D6TwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول مسابقات هفته اول مرحله گروهی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/657617" target="_blank">📅 13:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
زیاده‌گویی ترامپ درباره ایران: اگر برویم و بمباران کنیم، اگر بخواهیم خیلی آسان می‌توانیم این کار را انجام دهیم
🔹
اما تنگه برای ماه‌ها باز نخواهد بود. اگر بمباران کنیم، می‌دانید، افراد زیادی کشته خواهند شد. چه کسی می‌خواهد این کار را بکند؟ من نمی‌خواهم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/657616" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy6-ThwUF6iI1PUEQvgPx1GIZk1UAk2Zn6YLs55H7_ueo5E8_MemODN3TG_P_6gHmDUQcZI5QrhrfypkG4qbkrwBaQ6TGRIBrGY0O-HRezkbmMYLsMEHYoYykaT9sgx-QEYQpoyZEXfmGztbpqsCXpxVFkYo1UgZf5CYLBI3vwV9Ej43HW85LUy8NcDSr94326wOgVYcrUeF2CyghlqmrJIH0r2TimcFB-16nfJ2VmWYf9MD42Gdv9RmruVFAJZIxcGoNBvGH-2uquk1-oSBVan7Y1CuSM_gJl8rKlc8gzdT5mVuUGAx-FPrK2_lFzJGKYlGChAYv35hyhLf1aFdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ بقائی به نخست‌وزیر آلبانی: برای شعور مردم خودتان احترام قائل باشید!
‌
🔹
آرام باشید آقای نخست‌وزیر! شما آغازگر این ماجرا بودید و باید پیامدهای آن را بپذیرید.
🔹
به شعور و درک مردم خود احترام بگذارید؛ آنها حقیقت را از دروغ تشخیص می‌دهند. اگر با اعتراض افکار عمومی مواجه هستید، برای فرار از پاسخگویی ایران را مقصر جلوه ندهید.
🔹
نخست وزیر آلبانی در پاسخ به واکنش بقایی به تظاهرات مردم آلبانی علیه داماد ترامپ گفته بود ایران حق ندارد از مردم آلبانی سخن بگوید و به ناحق تهران را پشت حملات سایبری علیه زیرساخت‌های آلبانی دانسته بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/657615" target="_blank">📅 13:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
پروازهای فرودگاه امام(ره) طبق برنامه انجام می‌شود
مدیر روابط عمومی فرودگاه امام خمینی(ره):
🔹
با صدور اطلاعیه هوانوردی توسط سازمان هواپیمایی کشور در شب گذشته پروازها در فرودگاه امام(ره) به حالت عادی بازگشت و طبق برنامه انجام می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/657614" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIMunG7UH--pLa51_AKBF99YfAL-AsxpMAFVCrkpvINsTxU2asC9E6y6gpH4QxmDme-zoS8YQRtP_V2VjLxnlVZVOzGM-l17WfxuueRss76860cOSxHk2Dd-Gq_HA_GNhNjQKMbTlGmXTAFTNlvlguL76XMhhn7VZQK4wnBoY0BX-7YnnDTr3yqaCghXZaoHy4DHxGOPjrhxMOFSxzp6v4GbEhgy4_HI1Qc49IEDjLE337RzHr0VKc7NQrGgz_vGe8FJT98XqNmYSDRnBJimyiun64zsimXrnE5oEfFiyCXv3RCQ5hc8EV4V4CMk309I-eIM_k7BITqJvS9-K-cdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبدالله گنجی: روایت منتشرشده دربارهٔ جراحت پای رهبر انقلاب غیر واقعی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/657613" target="_blank">📅 13:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLf9FzWqqqTw-HWEJ02qDl_xfCMQ2naJof59m3cOzZs5xupNBh7mgBV5zbEA4oexQ26PjVazP5eVZkO3kdH78euu55LsKCvo90YWEyhnlwFH6mq-ANOX3bwdghGRC5nw8tDLq6vLXl62VLxixVYvtlCjZO92RIUcMMwSTUF3Ov-wp8s4rz0yHVXusNII1VsomN-AShKJjqHY7xSnlB6RFsSISH7FPcv_USgf3-F4oCBks-HfsB1-D67jVZqMiqUKtFeOQ0YgPOHD6EbP70eBUyRYqKkrHZWfXslA01Oqd0IAiCeSnbARmEqkKyaO62UmZryuSy_MLkYUhZF9SXQ36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۲.۱۹ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/657611" target="_blank">📅 13:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657609">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پروازهای فرودگاه شهید هاشمی‌نژاد مشهد به روال عادی بازگشت
مدیر روابط عمومی فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد:
🔹
با فراهم شدن شرایط ایمن و انجام هماهنگی‌های لازم با نهادهای ذی‌ربط، محدودیت‌های پروازی رفع شده و فعالیت‌های هوانوردی در فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد طبق برنامه به روال عادی بازگشته است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/657609" target="_blank">📅 13:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657608">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تصاویر اولیه از کشتی مورد هدف قرار گرفته
🔹
بر اساس اعلام اتحادیه ملوانان فوروارد هند، تعدادی از خدمه این کشتی را شهروندان هندی تشکیل می‌دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/657608" target="_blank">📅 12:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657607">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmOjuzZ1uMgtbBnuanDeZ1ljHZN3ApPbV16z1Ib1rMey4lXrRyzPUZOw4e0A6grvZ_cD5SIMiKs2HuJlT0N58mlbMHQC6_oQCkXy5mv8k6gIBaChFBrC7iEyDFr7WMOOuwC8Ub56lKMZdGfa9BHasxaYEG_3_hoAn59E_dq5tRE822afG0-SrRUAH2Mn6q7eRGzXhQlkhL22aQl-0LzRNnQc6FUsUFm7VZWPDOeSeI5FJw7axoG76ENJq8-0qw7qbGL1l6RTkLnIKHPVfkC4G3ukubR1xg4LFlNdfSdtX7_atU_I6MTZqOQuv8SbyNBt-tOsefLNCmiamRHHxV6MQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقیقت پشت اعداد؛ چگونه آمار و نقل‌قول‌های جعلی را شناسایی کنیم؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/657607" target="_blank">📅 12:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یوتیوب رفع فیلتر می‌شود
مصطفی پوردهقان، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود. منتظر هستیم گزارش وزیر را در یکشنبه آینده داشته باشیم که به چه نحوی پیش می‌رود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/657606" target="_blank">📅 12:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm2noI5aoECLi4K8wv-EdiK2EmHtE4o6Ku_eH2h__5uUp5e5bEPyGd1VM7mEqAtuH7oc6eWST45EretFv_g_wOsu9A8xj-WDXshlTSdxL7tB1NPf6RejaIOdjADPWOKjWGO98f3DuViNx3lkP6QZeYqsZvLbU0ikc6CLUhu2tda92rugKBfCypThl9lX2B58xw1F5gmGjUp0jyLhrMbgIQsrpcgseV-fdy3sNysvFcqE1Cmiwgn3Tr--A7Q7PvxsivGiNKd50DeoKZqNK4tkBTBtbzmVVN3Ke4mwbRRgxYtBn4U37AJaYn42gvGJSG29sm_UWNncpD1eBKIUFJFwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت دو تن از رزمندگان پدافند هوایی ارتش در دفاع از آسمان کشور
🔹
شهیدان والامقام «سید بهمن حسینی» و «علیرضا عبیری» از کارکنان نیروی پدافند هوایی ارتش، در جریان مأموریت دفاع از مرزهای هوایی ایران و مقابله با تجاوز رژیم صهیونیستی دیروز به فیض شهادت رسیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657605" target="_blank">📅 12:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657604">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsdGNJ58JzRT7NLeTSVzJJo3tq61Rx1C-VGJEmJG4W7pqNZLP9jQb5z4Q7mj4elap0r4L--eW9GzmU4UG6U4lHyGYz1Kq4FwYGnVoYZ4Gf6GSbq4P74r5XtouSaH8dRe7TqwudxaJaEum_VHSlekP90mG9z0BrmAYOhIpj596WMx5pCy-lfkSntndxNa8vH4Wtbq_9dQOrO_mLkLh2QaOJyPiStfQzUxo06rMjKGOI3bOOfOY0rLMLzGrmOI5HGojnarypgtS1J3b5mJ-GUzlIISrzXiSM7CUYY-inQHHlyh4HFESDtxMI3gH-0rPOA47vEugCzBavRry1vV9A-d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با جهش سه‌رقمی ۴.۵ میلیونی شد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۱۵ هزار واحدی به ۴ میلیون و ۵۴۱ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/657604" target="_blank">📅 12:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657603">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a9998b2c.mp4?token=CJA85mnm3X4-UPEz2M7tVvx-WjGwPt2xVASCHjSGbyfxQP3tnI3SJbCchcMSRunIBaIr33ck2yxW1un1EHS3-rVWZrzGA_6VTbPLJc2lCCLoz8dH8AqeeWJdeMDtF47ghEYr_L7Nio8bbaIa_wI1zA7QoknRSL95j7crFVU47q5O-bVUyF-OYK3uqCDlfmxuPj2BsnK2Cwvg19MMIW4DD59BOr1QCiric4x5MscBJv2m6tUG1hYTUxUtdHLgIRuwOwH9SvPyHmr0V27uUaKSMaksfJy3Kh7hCqsvxbY5AOMJ_Rga-iTkIr6kRL_fTUNgbH_Of1ZlxLsdh3C0wefHxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a9998b2c.mp4?token=CJA85mnm3X4-UPEz2M7tVvx-WjGwPt2xVASCHjSGbyfxQP3tnI3SJbCchcMSRunIBaIr33ck2yxW1un1EHS3-rVWZrzGA_6VTbPLJc2lCCLoz8dH8AqeeWJdeMDtF47ghEYr_L7Nio8bbaIa_wI1zA7QoknRSL95j7crFVU47q5O-bVUyF-OYK3uqCDlfmxuPj2BsnK2Cwvg19MMIW4DD59BOr1QCiric4x5MscBJv2m6tUG1hYTUxUtdHLgIRuwOwH9SvPyHmr0V27uUaKSMaksfJy3Kh7hCqsvxbY5AOMJ_Rga-iTkIr6kRL_fTUNgbH_Of1ZlxLsdh3C0wefHxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی دیدنی تیم ملی نروژ برای جام‌جهانی به تقلید از وایکینگ‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/657603" target="_blank">📅 12:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657602">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
کاهش زمان جلسه محاکمه نتانیاهو
کانال ۱۲ تلویزیون رژیم صهیونیستی:
🔹
دادگاه مرکزی قدس تصمیم گرفته است جلسه محاکمه «بنیامین نتانیاهو»، نخست ‌وزیر این رژیم در پرونده‌های فساد، به جای ساعت ۱۶:۰۰، ساعت ۱۴:۰۰ پایان یابد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/657602" target="_blank">📅 12:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اعزام محرمانه چتربازان آمریکا به اسرائیل در اوج جنگ با ایران
ادعای کنت کلیپنستاین، خبرنگار آمریکایی:
🔹
آمریکا در اوج جنگ با ایران بخشی از نیروهای لشکر ۸۲ هوابرد را به‌طور محرمانه به اسرائیل فرستاده است؛ این اقدام با طرح احتمالی تصرف جزیره خارگ و ایجاد منطقه ساحلی در داخل ایران مرتبط بوده است./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657601" target="_blank">📅 12:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657600">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsUMn0OYlrSUdVTUx1wFxO3gRcGO0onF6drcD4R7AysriQN_3Gtdor8trLEQ201Xiu9iAA6kQcyFTeNOCcNwXqZuHrAi1B9gnNRwYa4C4G4TytTnoElJ_ppC16Pcpu7Hphdn05G7d_iBRvGTPScc7JhzwDAtzAG3G7JcvkRe39pd5uJaI-rEoOpM4-gIASiE_WUWY_broLr1taaVTx3HRogA5F05oTRYwrogqD75t3gcOwpLXkGlp5VVEZn2BT8GKntE-cUuZoyhi7_bU4H4YQG_cKGlKwJRV-Lw-8pxykg857Zs79L3TVfrJR4GP7aUNzDQyb_J42jy_csPvBHUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازیکنان حاضر در جام جهانی ۲۰۲۶ با سابقه قهرمانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/657600" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657599">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
تغییر مهم در ثبت‌نام حج ۱۴۰۶؛ تأیید استطاعت جسمی زائران پیش از واریز وجه و ثبت‌نام نهایی
رئیس سازمان حج و زیارت:
🔹
تأیید استطاعت جسمی زائران پیش از واریز وجه، شرط ثبت‌نام نهایی حج ۱۴۰۶ خواهد بود.
🔹
برنامه‌ریزی حج ۱۴۰۶ مطابق زمان‌بندی و دستورالعمل‌های وزارت حج و عمره عربستان انجام خواهد شد .
🔹
فراخوان متقاضیان و اقدامات مقدماتی پیش‌ثبت‌نام حج ۱۴۰۶ از تیرماه آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/657599" target="_blank">📅 12:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657598">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt6Eit1Nc4QwaACtSsEAR5vGF814x24z-PMvz3xEf5v8018AUOanVlOcMcThl4azwxiIVIfDeyQ_TNuWa8z9nYtLZvaoyIv5YXRu8xBIV0ws8A4Tc20rsLQvc6Jq5vQgz1zUpynyoDmNCw5r5rXf4_BjzXoxwLqVpEwAM_vob9Lsaw3mPZIPhnH-LMWFOp0TTn4kZlV6C2-XGpzrD5ozw-DN32e-byDG0loSgNFk37bmPu_vkAVRzCS6MwL-nFqMtAMD5qNeRyzyu5YBkxybLJB1CNqtoWRHpLbpwXjG7fXNTHTfZSbYsSa09DLDhBwlr7Mu3v2RP8CAarwGIzdZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ گیگ اینترنت هدیه بدون قرعه‌کشی منتظرته!
🎁
با پیش‌بینی بازی‌های جام جهانی در اپلیکیشن «همراه من»، ۵ گیگ اینترنت رایگان هدیه بگیر؛ به همین راحتی.
اما این فقط شروع بازیه…
با ادامه پیش‌بینی مسابقه‌ها می‌تونی شانس بردن میلیاردها جایزه هیجان‌انگیز دیگه رو هم داشته باشی.
🏆
زمین بازی در «همراه من» منتظر توئه!
⚽️
👇
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/657598" target="_blank">📅 12:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657596">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S02-06ulBGUSYAowcf9Q7xo4I2fiJGS8L02F0Rpj0j0DEkSdsHY1Ni4A1RuQca1rFJEw92QFg6xdZBXwDuVtZIA9ypfzwQ3bbml-4pydMvWJi1IcjQy-NI3HrFiDfGvVbCjgdPhFsVTEPGxgGEQvjE32y8Z131WJS9RrF1kpy44C0t3IPNUft0tum7YlNIfMhfIJDENm6FGSkkuCik0Jj1lhMJvLejxmzMr97mmun5KtuJd6Kq0ZH3Z4ZyMCkhcqgXyzn0r6ZB7NaIRLVYNwhZ3wA_FilUZmOZEeBQe4wlCW58GYSVEpTbrLpnqW7bfHtdwZIDFtfJHcM1kedLezGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلعه میران، گلستان
🇮🇷
#ایران_زیبا
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/657596" target="_blank">📅 11:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657594">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/757ddf32fc.mp4?token=ABiMFp6i5wgaNq7u0LvoKp5NnSAMkbdSZoq6RPtjotutqcLT3Rpjj-G5jAE8Kvw9nl4IuDzWNZmRGfaDmtHcrRtO4RiwupLZ5OlPs4CCmEx6bNPZgRFTUwejGvHcdzf9QjucCqUQIq1FAaup_Oqk9wWd2d_5bUta1rco-wgvQSZDmLneWS6Ivw8XnQY5fhdgYpnV_U_F0dHT4h9GYI20XdRIVs-_IndCZow59xEyKjZUQDVp5J3z5G8DEaDAeMJWjlgAMPuNNfezxPQuNg3AqmfHCgyqHd76WqzvzndXlHL5G9G7d0VYgdvBM4uBBmwh9OtPVJKJfQrK7A8-8x4AEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/757ddf32fc.mp4?token=ABiMFp6i5wgaNq7u0LvoKp5NnSAMkbdSZoq6RPtjotutqcLT3Rpjj-G5jAE8Kvw9nl4IuDzWNZmRGfaDmtHcrRtO4RiwupLZ5OlPs4CCmEx6bNPZgRFTUwejGvHcdzf9QjucCqUQIq1FAaup_Oqk9wWd2d_5bUta1rco-wgvQSZDmLneWS6Ivw8XnQY5fhdgYpnV_U_F0dHT4h9GYI20XdRIVs-_IndCZow59xEyKjZUQDVp5J3z5G8DEaDAeMJWjlgAMPuNNfezxPQuNg3AqmfHCgyqHd76WqzvzndXlHL5G9G7d0VYgdvBM4uBBmwh9OtPVJKJfQrK7A8-8x4AEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر ارتباطات: ترافیک استارلینک با اینترنت بین‌الملل در مرزها برابری می‌کرد
هاشمی:
🔹
ترافیک اینترنت بین‌الملل قبل از ۴ خرداد با ترافیکی که از مسیر استارلینک از شبکه‌های مرزی خارج می‌شد، برابری می‌کرد؛ این تهدید جدی برای امنیت نظام حکمرانی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/657594" target="_blank">📅 11:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657593">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG3_NsJCyyyOLCo3MuItN3jXbxqVvPyxKxY-RJLSEU2U2Zz8vWo6IZn1fdnuID7P3SI-_QA_u8dk1W2_cOmeE6tjkdUUohVY0KuM5tPOp_9XrLZFoq5N7WVvpL88-wt6SGrHmqJgC-4QKgy552INFLVFKR2qet28pOQIJXhLysk5_F-4-cvELBEudw8YnP4Q0rypaa7C4ZMm0Vdozfso34JjvzcXBh5Nbq3DDxzTaG7YQdD9sbYgkeOCyyKIBKYOJKblAZ-Uzw_x5PkPsXEPaxFG9ao5kufLHjw3VhLerDGsDDwU2sHkj5caemceNL69tWrmJeHZflOwWyYW8znCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: ترامپ ۳۷ بار از «نزدیکی توافق با ایران» سخن گفته است
سی‌ان‌ان:
🔹
دونالد ترامپ از آغاز تنش‌ها با ایران دست‌کم ۳۷ بار مدعی نزدیک بودن توافق شده، اما این اظهارات تاکنون به نتیجه ملموسی نرسیده است.
🔹
تحلیلگران می‌گویند تکرار این وعده‌ها به اعتبار دیپلماتیک او آسیب زده و موجب افزایش تردید ناظران شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/657593" target="_blank">📅 11:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657592">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
مراسم وداع و تشییع رهبر شهید انقلاب پس از دهه اول محرم برگزار می‌شود
ستاد بزرگداشت عروج رهبر شهید انقلاب:
🔹
زمان و جزئیات منتشرشده درباره مراسم وداع، تشییع و تدفین رهبر شهید انقلاب و شهدای خانواده ایشان در فضای رسانه‌ای معتبر نیست.
🔹
با توجه به ایام عزاداری محرم، این مراسم پس از دهه اول محرم و پس از هماهنگی نهایی دستگاه‌های مسئول برگزار خواهد شد و جزئیات آن متعاقباً اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/657592" target="_blank">📅 11:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657591">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyzhUi6maudcW6Kgj2axgA6DE87sH8w7aMCB_VrOCw6Jpaew4Bwz_cRFQGc0cAX6qCaMwLKE0HKir-bt3xNwPfeEx87veU1r74tlXJrcK6DRIval7HJs_pv4Zet5FR94EIE0Pcc6bCJZThFSI1QC1Vv2rk-YA-88rcypUimwf-oDE5wNw168apyd25ZlYoQEQwJNU_4HlVmlsahIFiFg3Mrv4A2cpzdJA8lhjPAMP06ZKMErL_NZp4W6VLYNrMWcDMFtkcvtVgtdfPRTsZenp9S-V07nH9CthItGSKolUxnsgMXjkHH5bSnecnnL3CbXX9IQLvJrAwrWlxehdnse8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ خطای وحشتناک در جام جهانی که فوتبال را فراتر از یک بازی کردند | از تکل‌های مرگبار تا جنجال‌های فراموش‌نشدنی
🔹
جام جهانی فوتبال فقط میدان نمایش مهارت نیست؛ بلکه صحنه‌ای است که در آن فشار روانی، غرور ملی و رقابت شدید می‌تواند منجر به برخوردهایی شود که گاهی از مرز ورزش فراتر می‌روند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3221244</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/657591" target="_blank">📅 11:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657590">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBqSzl3WqvaPZNAiuzNepX418yqbWIp6pYgrZU_3Z5XDm3KnrlLlI-qt1GBM_OjnxtjFLOSSqW1O5Jwd-Qz-cPfu78ad4ql2rROx8quVedKe2Qklxf9-UYAjoWEi1dDdxRUeH0Szi0GL0cBs0bE3fujPUYViZzLa3uRLKWZ7i7T-gpHRTLwoXSCvi8Z15zi4ZlBUxEcqprkgLmwdsIb4TzhOHk7uNtCoUaWLhk3kQoyguAuLJPDTpb9FdiUpq8sXMCz9j1zVk2tmy94DBwYuR9et7TkCBHjprQM5rV_bSa3idQrvaD9Pk-QB2g5F3JzwVneQaMQNk0kTj_tvBXae2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر استراتژیک نفت آمریکا در آستانه کف ۴۰ ساله
🔹
ذخایر استراتژیک نفت آمریکا در هفته گذشته با کاهش ۷.۹ میلیون بشکه‌ای به ۳۴۹ میلیون بشکه تا ۵ ژوئن رسید. با ادامه این روند، سطح ذخایر طی روزهای آینده به پایین‌ترین میزان خود از سال ۱۹۸۳، زمان آغاز پر شدن این مخازن، خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657590" target="_blank">📅 11:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657589">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
چین: مذاکرات ایران و آمریکا در مرحله‌ای حساس است
سخنگوی وزارت امور خارجه چین:
🔹
مذاکرات میان ایران و آمریکا در مرحله‌ای مهم قرار دارد و هیچ طرفی نباید زمینه‌ساز ازسرگیری تنش‌ها شود.
🔹
استفاده بی‌رویه از زور، مناقشه میان آمریکا، اسرائیل و ایران را پیچیده‌تر می‌کند و از همه طرف‌ها خواست با حفظ خویشتنداری، از هر اقدامی که به تشدید تنش در خاورمیانه منجر می‌شود، پرهیز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/657589" target="_blank">📅 11:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9ItIpGLM9g11RF1zd2wtCEL5GUzIQHZNArIDw0li-8HYZsAtVTzbKPZHtmnPAclwLs7t67tWLNsVWaDGGGe-OFvDguRzRl0JYnNh8KbbxI6ML8WvliOJDXCZNUUx7QFVCc4LkFw4UGuSsVFTv-5kgFVWaI9YEpLSn-rz0Ol_VvxaZGCtnRwbFBMhL5BG7FWOV3KPJqYA4EOQqeMYyxmZJnqFKiX1vZasn212iydtd11lpLO2jSAtpmQXw5gNjjdqwkrVrpDum1Uzr8nRIGsXtt0xJQV62pZK90jigXQjh-3TwJD9SuOMY2ioIRgitXG8C8itMgZF3xambolU3hKUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4VzG121G9nMW0r4bR_Ncqded6eSOwDynJUcaJUNNERQMyvCBbves4gikpNV3LWpmhgh9UxHdCjYpcNvOIf3Nhqmh3mGBZQrjtCcgEn-zsOfoY5U187nM5eTpgypdUd8Q_6APqthvCDOf85uba-sU0UVX33KqAOeoyo7JvEe_Rc3y7vN3JF9b9uokTzIE6JriR4P2vpX0ArwwXKGVY5CLbYPOm8eo-okgRezZRi2Un9z0D1S0oL55zxX_8jHhmJJljzmmQ9pvaQlfCEBmY4mVAu9zhSP8Z9f6ZT3aPhTy40rMOK2uh4ykAHCf6G0aFd4KFcGXA1e6KyT_oYkMI5N0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUamUxSyAfxL3Wb0IwpycB0gEY3bJEiXu9zp9h037CWUgVmgriK536DDCw5MutNkm2cwzRAMsaRdzvQbsO5wql8hiBn2itGOYnUwCDig6DxKSei7OBGmhpiP-7uoEGbnhNrDFVpsphNGFs_TsJSMmygbftiAS1yJS-VS9MWl0LDvinMYd6FCN2BdSGklUyItWO0ih91Xj9kStI8l-_V6YKGat19i2udE6uW1kGK7XSvnwPKR8mNwapnO43QldIlz16OENWb3G3BhiGqsEf-d4lXHme7hUZoKirnBWXGE9XrfG64P2xLQvnZ_NGWJSeV7jmt1LI3g1CELvssfErLO1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ih32R6xb47fZCv2VT74o7u64s7r6bhukcWj1D_NZlJX5xTsEmc1Xb2_5axE-lpuEfFpUP_EPhEtkI0puBDqFixBejBjjM91t0v7KYNAwtc_vb9aERh14N1Z-rbmNiNM8Oj-XgN93I0tBRCEEHEvep2ykrObx50AYAoQZ5GVDUaenZMNEcHAHESBXfSdYbJhldM9-hGCVlqF690YZk7oM6H-i9HViISi9TGeSVWtZTxWd0T0zdr8WpP1JW_Jmru84AHMaRy8MiR9J-_Uxu_h3P6O7jX0KQe603Yvu0kNLMD5DhkWBEZ3TRVUWqIIUmjAHCb1MPdblegCKRxrMNXxtlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6a4abb628.mp4?token=bwhVQ1lhtItSZ92HL7D6n4DGN-Tk2R2DfR8YUgNa5hmdtmCDnN0ZkbY0G8Li5TzIquQmZYEoOctjh7PImZXew3xfqbk-KdstFN-yzieJMl4UHcjdczEoADZFuHi1sDWBzsImELGi9NorErCd0b7PNppW5oF-MTSFOaN_6G2TGGb-TTH0rxywaukmAjRoEuZ9b3BepCxlQP1y8bp3yMr_Dy-eBsP_pk9DIhjgM91vtoZTANDK6soJCGwM1Ey_PS4bY5zDbjpktfB_9LH7nbYjnx6TYV5clPdC3OQiMnPikCYkDeeJIJzn_48dftk0vmo0wJGpklVueaJfPh5fLdtn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6a4abb628.mp4?token=bwhVQ1lhtItSZ92HL7D6n4DGN-Tk2R2DfR8YUgNa5hmdtmCDnN0ZkbY0G8Li5TzIquQmZYEoOctjh7PImZXew3xfqbk-KdstFN-yzieJMl4UHcjdczEoADZFuHi1sDWBzsImELGi9NorErCd0b7PNppW5oF-MTSFOaN_6G2TGGb-TTH0rxywaukmAjRoEuZ9b3BepCxlQP1y8bp3yMr_Dy-eBsP_pk9DIhjgM91vtoZTANDK6soJCGwM1Ey_PS4bY5zDbjpktfB_9LH7nbYjnx6TYV5clPdC3OQiMnPikCYkDeeJIJzn_48dftk0vmo0wJGpklVueaJfPh5fLdtn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شست‌وشوی گنبد حرم حضرت اباالفضل العباس (علیه‌السلام) در آستانه ماه محرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657584" target="_blank">📅 11:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c7cabe88.mp4?token=YxORp_1JalS0aWxgc4rmMwLHiT1fzjDPsZnUakZmZAxQYEywWqM33yGcpEHDeOXRXliHcQfzzJGq5nWsqO4JoGnGqa9rF4leTLtSBJJk8mSVVhCe6eVQmZXKujBgwPmNjGWDzSZkg3BZ9f8V1mSMLMNSmi2S-SDU32prO_EBvdkFyCwBiGBAnzyf9wCRp6epSIvG2XH0x5xbn6lVZFnjibi2J4eSHzVQFHmRy6zEAKCdMROHCuhjEvqQfWPo5excLy5Tk4qDlv_zAsth6d-PqkVTYs-pVrsU_DX-pmsc9-9FcN8_vw7Ouq2DwFRhByE9kUnbGRGqmDix7IucjOJ69g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c7cabe88.mp4?token=YxORp_1JalS0aWxgc4rmMwLHiT1fzjDPsZnUakZmZAxQYEywWqM33yGcpEHDeOXRXliHcQfzzJGq5nWsqO4JoGnGqa9rF4leTLtSBJJk8mSVVhCe6eVQmZXKujBgwPmNjGWDzSZkg3BZ9f8V1mSMLMNSmi2S-SDU32prO_EBvdkFyCwBiGBAnzyf9wCRp6epSIvG2XH0x5xbn6lVZFnjibi2J4eSHzVQFHmRy6zEAKCdMROHCuhjEvqQfWPo5excLy5Tk4qDlv_zAsth6d-PqkVTYs-pVrsU_DX-pmsc9-9FcN8_vw7Ouq2DwFRhByE9kUnbGRGqmDix7IucjOJ69g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آتشفشان لووتوبا در اندونزی
🔹
آتشفشان لووتوبا در اندونزی با ۹ بار فوران، خاکستر را تا ارتفاع ۳.۸ کیلومتر پرتاب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/657583" target="_blank">📅 10:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
درخواست ایران از فیفا برای بستن بازوبند مشکی مقابل مصر
🔹
فدراسیون فوتبال ایران به‌طور رسمی از فیفا خواست مجوز بستن بازوبند مشکی توسط بازیکنان تیم ملی در دیدار برابر مصر را صادر کند.
🔹
این مسابقه پنجم تیر و همزمان با عاشورا در سیاتل برگزار می‌شود و ایران اعلام کرده بازیکنان به احترام این روز با بازوبند مشکی وارد زمین خواهند شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657582" target="_blank">📅 10:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e36a1fb33.mp4?token=F5vLAs2FddjDWOXp5LqfxezdAWH1RgQVaHDSp-Gj6HemhUUtpCIe9407NyKQbYnbO_MJpF_C5DpPb4LUTWCvf8c3GDDsHxJNrdPu6NQ02qRkLnDsAi9r2DbGu1-0ud0HqiFk1vfLiyphSYUEPmm7IYGBmWlDsvWBk6YIEHaQ-LzPYmeFD0_jLcGXFkj_kf_9jAnUE_6EQM4PU5LFQF22b_CuY48y6Ulnhmy_w_YEm1a6Tdh0T8ROVSgg8FuCpy81CE3Kok-qptgJ2GFVby1eBAoDc2EFgX2WVguLwtoJvIXxiSBPFyIJ3XZT6u-JqHd4QYwqvFM9fixbKaBSePgUmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e36a1fb33.mp4?token=F5vLAs2FddjDWOXp5LqfxezdAWH1RgQVaHDSp-Gj6HemhUUtpCIe9407NyKQbYnbO_MJpF_C5DpPb4LUTWCvf8c3GDDsHxJNrdPu6NQ02qRkLnDsAi9r2DbGu1-0ud0HqiFk1vfLiyphSYUEPmm7IYGBmWlDsvWBk6YIEHaQ-LzPYmeFD0_jLcGXFkj_kf_9jAnUE_6EQM4PU5LFQF22b_CuY48y6Ulnhmy_w_YEm1a6Tdh0T8ROVSgg8FuCpy81CE3Kok-qptgJ2GFVby1eBAoDc2EFgX2WVguLwtoJvIXxiSBPFyIJ3XZT6u-JqHd4QYwqvFM9fixbKaBSePgUmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی صحن‌های حرم مطهر و منور رضوی با نزدیک شده به ماه محرم
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/657581" target="_blank">📅 10:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657579">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85cba66719.mp4?token=MIceP1lSdJTXFpmbF7MKrRlCUQMCQSL9pkOkTHUJCgX_qQHFFqz0BLn3Yopz-ssnW8-YNvxjIskU4BgUaiflJ0ofs7wWs9zO7YxoT2z1eiKsfs_virvZPEebzPTPIvnlMX_48UF1q9dEm9xbLkG9kWPAkENs1nUF93wlOB-wEDxOj0T0VSzBEHROvqs1ImyDSOPAoH0iOva4YtuBsXK7lMmsH7YoNMzsQKWTqKCx2hytNM9mH7FAP9GMkmMxP_xo1BMOvSPjwuW6W9Ti85lco7NlxTHzluIoccDo5byXkb28KBPXzd73rkx1k5vFKlOHDbswpUAthb6IcdbEEU-NIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85cba66719.mp4?token=MIceP1lSdJTXFpmbF7MKrRlCUQMCQSL9pkOkTHUJCgX_qQHFFqz0BLn3Yopz-ssnW8-YNvxjIskU4BgUaiflJ0ofs7wWs9zO7YxoT2z1eiKsfs_virvZPEebzPTPIvnlMX_48UF1q9dEm9xbLkG9kWPAkENs1nUF93wlOB-wEDxOj0T0VSzBEHROvqs1ImyDSOPAoH0iOva4YtuBsXK7lMmsH7YoNMzsQKWTqKCx2hytNM9mH7FAP9GMkmMxP_xo1BMOvSPjwuW6W9Ti85lco7NlxTHzluIoccDo5byXkb28KBPXzd73rkx1k5vFKlOHDbswpUAthb6IcdbEEU-NIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژیم صهیونیستی خواستار تخلیه دوباره شهر صور شد
🔹
شهر و بندر صور چهارمین شهر بزرگ لبنان محسوب می‌شود که پیش از این نیز دهها هزار نفر از ساکنانش مجبور به تخلیه و حرکت به سمت مناطق شمالی شده بودند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/657579" target="_blank">📅 10:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657576">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1HdFFsnUrwu9Kmsb4QcGutH_AvAEd89eRxsO7fKK29qpZzrHZKuBE6FpnrIq_as1ru9zcWZHimNY4t5Hqt_gyM-6N0_0kEDCjwv6UuySJ2Ay006B7YCr9x6kPfuAr2OIArQZItSmU8Rm_Oz1PcLjcEhpcG_Uj98WuolKe6KaJ83_vW70iXY6Ucq5Zali2Zts8vpGHLZDlSCVtm-IW4cKxYwqBCYVeiI_84ExEL4pJ2FE4W07doqu6GW8ifh2dXJCzQNSVakzelpH5OGCizl3r4r5Om9V7_KSKxbt8f9SeH9ax-_w58QVaPiYmJ9A_NVTJDKeP3NxLmMrAxcT2s3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b41b0975.mp4?token=glciAscnLaC20B8B_HzneiML5KnPb2fUJgGZey0WsJt8ZA1wOz3dN2ZPYDIUm74Mearoae6H2VB2Tcss13wBsMDHinoo0voN3NK1zray6UMuFnf_wu896wM5uidXl8ThfvP1vUQrZArElLGIVJO6xQzllAD3IAXkLjXdAvT9rRWktjNryp1WFGZMTmwSIBV_n8wZhN0iJPd9BCdyxXnc7HQvTRdVJSa0PdFbvN6SOBagZFBB_Z4BvHYOgxlEFvIAnhqyX6WhbL1syqDm09beTub6ff2-DI53glztif-Ux0qnUIpUEKaE3slHER6kKTKq26E_8ZvaYluQwOp79k2bug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b41b0975.mp4?token=glciAscnLaC20B8B_HzneiML5KnPb2fUJgGZey0WsJt8ZA1wOz3dN2ZPYDIUm74Mearoae6H2VB2Tcss13wBsMDHinoo0voN3NK1zray6UMuFnf_wu896wM5uidXl8ThfvP1vUQrZArElLGIVJO6xQzllAD3IAXkLjXdAvT9rRWktjNryp1WFGZMTmwSIBV_n8wZhN0iJPd9BCdyxXnc7HQvTRdVJSa0PdFbvN6SOBagZFBB_Z4BvHYOgxlEFvIAnhqyX6WhbL1syqDm09beTub6ff2-DI53glztif-Ux0qnUIpUEKaE3slHER6kKTKq26E_8ZvaYluQwOp79k2bug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بخش دیگری از اموال علی کریمی به نفع مردم توقیف شد
🔹
پیش از این نیز ۲ واحد تجاری و ۴ واحد مسکونی از علی کریمی شناسایی و به دستور قضایی به نفع مردم توقیف شده بود که یکی از املاک شناسایی شده یک پلاک ثبتی  شامل دو واحد تجاری و ۴ واحد مسکونی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/657576" target="_blank">📅 10:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFOmoem8QGMUR7zS96i68O2eVSzYZd3O5jf8Epurt0hrBdlbT9Gp1oZKkINEhPRvuAwUiWHbpT_1P60aq9v3Uyj__cjBxMSwf5qMekOVirZOdqn5pwe1xGyT5hNmlKk0ToOhnJGc0YJctesaer08EUpIvtODqA_Trcmg28gRrUgDrlwlQs_rjiT9CT6DUi1XvnvAVHz0AIkP57D2YPKStm0EERrchuIpRcHFbUx6QlN8yuU3jxTuCVgoKy_6DN5uWHv0MWO0sMt7ffhyalHeZGf8Py5CIaOAOgzh6rWDFbtJ9g930mBw7wO9JMM2kkTEwQt7R6N578Sfeenze05H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رژیم صهیونیستی خواستار تخلیه دوباره شهر صور شد
🔹
شهر و بندر صور چهارمین شهر بزرگ لبنان محسوب می‌شود که پیش از این نیز دهها هزار نفر از ساکنانش مجبور به تخلیه و حرکت به سمت مناطق شمالی شده بودند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/657575" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
دیدار تدارکاتی ایران - گرنادا لغو شد/ گرنادا به دلیل آماده نبودن نفراتش نتوانست راهی مکزیک شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/657574" target="_blank">📅 10:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d289f2dfff.mp4?token=W7hyvx5s8-nBPqKuLcCsnLx8T2eR7pg5FAhpboAfRXEXO6ii3uHEDqOSs8DhKE8SQmxTBxeZqYGsdBKUFNPz_AMV4rL9qpNXNnNQGfZLXI5AwCbq9XKZmzDu5RJBKXOMEAi-mR8B8EanBZB7hd3MTYyjCm9u1lppa8yXNKPbei6PlGl-kLZMfU2EUlGPQZY1B-eMF2KBTCosoTpylM0_uyNym-pj6O_fuBnIgVN3D2_N5P_5Z-4P0tBQbBNAQiF7gV58rictScwfHdICFX-yojLrK1NF_Qf0OrJ5cEuCnYN4LYnjzgQroj8IYTm_aU6P5RPcxIacuxsQGVbyDSsvgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d289f2dfff.mp4?token=W7hyvx5s8-nBPqKuLcCsnLx8T2eR7pg5FAhpboAfRXEXO6ii3uHEDqOSs8DhKE8SQmxTBxeZqYGsdBKUFNPz_AMV4rL9qpNXNnNQGfZLXI5AwCbq9XKZmzDu5RJBKXOMEAi-mR8B8EanBZB7hd3MTYyjCm9u1lppa8yXNKPbei6PlGl-kLZMfU2EUlGPQZY1B-eMF2KBTCosoTpylM0_uyNym-pj6O_fuBnIgVN3D2_N5P_5Z-4P0tBQbBNAQiF7gV58rictScwfHdICFX-yojLrK1NF_Qf0OrJ5cEuCnYN4LYnjzgQroj8IYTm_aU6P5RPcxIacuxsQGVbyDSsvgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از شوخی رامین رضاییان با قایدی تا فارسی صحبت کردن دنیس درگاهی
🔹
تصاویری از بازیکنان تیم ملی پیش از ترک اردوی خود آنتالیا ترکیه و سفر به تیخوانا مکزیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/657573" target="_blank">📅 10:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f212e28708.mp4?token=nqna1BJsl6pSBN69CHrFmVVqLSnVCZaYD55xAXRrfYsvzkfn4JDt4a7F_T7QNNaDc52d8FAIJ51KkUgHbtL_1MddQOsn-96WZ7Kmzvivo0nq_AnjoTyu3Mq79M2PufgCIBf0djQZyD9UoCC_VP3B3fSZO_2Oc87N_1jcT5MiszD3aCEJrY6a5boO4rPCvLy8Lh2Oq0t7GRont8-Nv_jEchKOVqKB74aTTFL53Lk9atm_VaNBS5m1XhvoyHACxTZMS-7El_5jCMOreIwpYH2oMpVIIQz9YxhrLzESkmiU-FI3JN03At1ct7acqapGa_y8m8G4TqOrkop6U0KQboNakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f212e28708.mp4?token=nqna1BJsl6pSBN69CHrFmVVqLSnVCZaYD55xAXRrfYsvzkfn4JDt4a7F_T7QNNaDc52d8FAIJ51KkUgHbtL_1MddQOsn-96WZ7Kmzvivo0nq_AnjoTyu3Mq79M2PufgCIBf0djQZyD9UoCC_VP3B3fSZO_2Oc87N_1jcT5MiszD3aCEJrY6a5boO4rPCvLy8Lh2Oq0t7GRont8-Nv_jEchKOVqKB74aTTFL53Lk9atm_VaNBS5m1XhvoyHACxTZMS-7El_5jCMOreIwpYH2oMpVIIQz9YxhrLzESkmiU-FI3JN03At1ct7acqapGa_y8m8G4TqOrkop6U0KQboNakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
كمال‌گرایی همیشه نشونه‌ تلاش برای بهتر بودن نیست، گاهی ترس پنهانیه از اشتباه کردن، قضاوت شدن و کافی نبودن #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/657572" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
فدراسیون فوتبال ایران: سهمیه بلیت هواداران ایران برای مسابقات تیم ملی در جام جهانی ۲۰۲۶ لغو شده است
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657571" target="_blank">📅 10:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-F4iGcDRfPc7mq03aP7IUlopYw7BhwoNrUsPdR6DJ8_5E6lgyQdBfqxRHLe40Jrzh3oSFa_XcNR8lZ2M_fcSBQ0NQpBmvGoRmqTnv1tUJ5i1vID1eYatGef36vKFmvbmkcLJfi4matpPhRSe75IF1mnNNcbPgjzhwQaTt4pxZp6Jh_tfjTllAzgSyaufq79Fe7_-3cn-On1r7NxkZCvoOUxf-hv98Hr-WgbSTq6Y_RMmyMD0CdDbs0BH-F3f7pMOAuXdcVq-VzFm1Sw6i74ltNeqv2sl4-fXOKswpYc5OYogRZ14LY1bBQrRWRkhjxnexXFhArt1Vo5FztM3rxKKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/657570" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
واکنش دبیر شورای عالی انقلاب فرهنگی به بازگشت برخی هنرمندان به کشور: ایران، کشورِ امن تمام ایرانیان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/657569" target="_blank">📅 09:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
فردا چهارشنبه، کالابرگ کد ملی‌های ۳، ۴، ۵ و ۶ شارژ می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/657568" target="_blank">📅 09:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657567">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: هیچ تصمیمی برای اصلاح قیمت انرژی گرفته نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/657567" target="_blank">📅 09:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657561">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Of4RCdL2vMCvGhC_cQUUC5hBVa5L39UivN8h_oIdyAGnx6ESMhPrhwq4atICfbyaI82899NXjBgKff5PpELJ9ZCjLBsWPMu7FMlwbz8v46Zupdkr4p3wg-nc2U3HEkOuRfVq0pW5v8XLK-OuxziygrZZrKk-MgeBR98UzJqG3ZGlAfP6Eu3l0x9HM8HLDlnBJnpXDX6r8QsnC_6wLkxR5cxMIMmYGELtnbMzTxRj_hlkfIBFdeqj_wQjwo_foH52U3FKNt31WJL0FLbYqv6hznC7wmfS1JNE3Ko9hmMUTsiJrhJzuFhXGHW1PwbtkbvD8RqPDeuyRT_UTxriM-ct7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DapmaDnYgcDEF5pl3Zcnjg5ZDY7lfq6L-lJCI84gyJnZpZNfDifJXUj8P6VsEXJMaZNvYyuU_JlA3deBSef85S-e0lKJLSx3Zd0CahIwGzuk_no23Uo3X87FJBlguKiABDThzy6igJZV7TBeQ1-2uiew0Oaob7O2sp_jOJQEKKcJGfCu24-NWijntH1r1ao89RQUeuSJTZRNWlz9Oh-OHIzUKdvbV9D29_oVihG6m6erOxnyhvzEzuoM5f853DmbEjuTSxMnzT2we4y7pSL6AwnOhbczU7J76ixlKzFDFia78vQEJfv7Du5nZGubkZtP52aQQXF5gP_IiFUDPwQQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhsE90a4zpGHvUInIMcP-U8NRnBtTyiEcECfFT6A2jkHTxrF22N4Lbik04aZyb0YH-MwZkKYWsXQEkWtHXeH98TJ8f2Zn-0_G2e15mXGkJPnMIFLw1K1zZNGhIE-8AlIhXNYj-xVRLJefdmy7DNGSuBOAyesH4FAttMvrmv3bFPcRVGWnZpzlcdzcv2Wbjho-2arHvCN8rsxaXU8kO-rrvLxN4FQz7LsC4LiiCK0HLFTVMTRoiXX0n7yuJMpJ-PPM-vVyb2qSaeFa8fN2fIGi7trSH-EDDBaTJ1PxtEAm1n5_tCl3wT2aWVEXkGjtjL1eO_x3LlhYpOcgOrbmghmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WoCe8PqZxgMpcw1_f3ZtuQMkxx2GFtITLxsN8PJG3nQgpFnUqg9BrIdukNUNzCihKQzOOllGxz97ZnJdtj8jmcjosjKwd-oTlZ0Sr0BYFkIbIqVLYIss5Ds4Ycyvd3Vq1YXRecICMtC1--dqHZane-oNR2xuc1IErFzGk7WM-N-mjorpKjWA3rjUEIHbksEWbEqiEeSQvwSWBGYUptYz0DSlcHwpiafzgNYhq8m4UR5dUQDcsTx_jnK7zI1IMZxCYJALRd3PA9nCbSwrJrGe7v-t3ksdApW85b2sEGvsXVjTPIyVXRwkHw_kb5KAPGRvqwi5rKO0Eg197pDV0SuQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hheUf4b0xiPKs0MkHD2b1AKzHgpBlxdq44qEi4pnNN4rUMNgDziuxFSQ3qCMcLC1R_VfTAHzmgG7JFxxFs9oI9gCF5TWYCRm88CARXuEa_eMZ8zRDXyEfD1h7LKpt69KPJuQ3Xz7phwlra2rtJDTlAvQpxodHu30Emc6kaTMMkIiB-_jDLzggP4cn65dBAPQmAb1j9OlhpkrFWb5u5hGlF8qT0Wi5SrRO_pooWkUA7He_IAwY_QnA7JZqe8sCsfR3AeQPNEKJ58sPTOqosDiUjiowpXxoBq3A9Ro2oz1NES2_ocKQ9K4z2IQhbpZ3oJtYN-lKOeXAJ7OjncZVXL1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooWsGhlygta8MZH70OpT_BOp5FzT1SULmmUeuaPmZUeOvjK-f7ZAKzKbFXAyhbgNuzlyzuEmElwtcjckODiP3H1dYPLNLsbT0Q5nugw6GOej4Qqq0tFeuGnYvZuw4_vdmbwj-oqouPQ7LJeiKhbPvt0K9hOLrQw0icDcN70moxn10BCj60XcMVrzaSBnd9G4dQzr9RuFwkj5XFcUd5OD2szNvJEcjULWL-UbXN99RwDPkzDUqiIQkHvBr9pru4RAB_E9lPMuPX8ZnIxl6dYHqTJCt3U9XV1gMMdR-gTj1Nje4rD45ZlkUVCdtX9g9Ka7mYquh-Lf9FPOdxOuH4nSeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خوراکی‌های کلیدی برای سلامت اندام‌های حیاتی بدن را بشناسیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657561" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657560">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3RPuPeBuO3NuaqNwZXEmw1eTwECaFLdsyJAAgYdQW_E7Th3jaKhhEZkHPpBRi-4EuN5fJ-6uSXIHhVolusjtZAUCWBrgjSjVLVRTn5t-bi7MkcHVwY6nHJ1dU3mlKoMfZlesYwfzPXKr5PNM4ERHY7Ckf3ECjLAu-gvmWgbhZDAHP__64pHSzAmP7Q8wz4mTXVWnQaYVDZAq8ELvOqpKjpWMTEh7S6FesrfJUoeRt62RdGBfp-zc_ND3Y8EfojlVut_Qlkgr0oyYOlDv9_WGuNs2MicdIfsPx9Jb9RCG8K5biMMSM99jzl1JV5KFt2EEOZKlfUlzm5LCQ_tLxckQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر سیاسی آمریکایی در واکنش به ادعای یک سناتور که گفته بود ایران ضعیف شده
‌
🔹
می‌توانی تمام روز به خودت دروغ بگویی، اما واقعیت این است که ایران امروز از قبلِ این جنگ قوی‌تر شده و آمریکا هزینه سنگینی پرداخته است.
🔹
به جای پذیرش شکست، آن را موفقیت جلوه می‌دهی؛ اما این روایت ساختگی دوام زیادی نخواهد داشت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/657560" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657558">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c62decf3.mp4?token=diQ698F-sADxZXHfDCgvD8Pnk3k94QGLZ94ZAbYCftH6gc0VMU3SV0Gc61dMuQjSlRChQvCPO2iUmsrsBGN78pPpH7PP7nPIAPeBivhDM_YtvVt22Vvgt3piJwmr6HfGpvUx05i1ImxUWsjikBkijoe4esBUlNRY_A4FkaqSGtXWi47NCQsDLct-rkW2G_gfgytx2ar73Sd3_o7EXqj1ZCSTnlgCEMYkMzJVXvNh-Y6WpK5Pc8m5bOZzF4-XSMmeqmKH_X71ikQvXU6PRs8ZNTfzHnOMO2J2S2Ci3a9I3SQEaT9moHw74cxDnTny7YEg-_aHs5Vgj-P0kfo9eBOu7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c62decf3.mp4?token=diQ698F-sADxZXHfDCgvD8Pnk3k94QGLZ94ZAbYCftH6gc0VMU3SV0Gc61dMuQjSlRChQvCPO2iUmsrsBGN78pPpH7PP7nPIAPeBivhDM_YtvVt22Vvgt3piJwmr6HfGpvUx05i1ImxUWsjikBkijoe4esBUlNRY_A4FkaqSGtXWi47NCQsDLct-rkW2G_gfgytx2ar73Sd3_o7EXqj1ZCSTnlgCEMYkMzJVXvNh-Y6WpK5Pc8m5bOZzF4-XSMmeqmKH_X71ikQvXU6PRs8ZNTfzHnOMO2J2S2Ci3a9I3SQEaT9moHw74cxDnTny7YEg-_aHs5Vgj-P0kfo9eBOu7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات ضددولتی هزاران نفری در برلین
🔹
خواسته‌های آنها شامل معرفی دموکراسی مستقیم، پایان دادن به پذیرش مهاجران و «پاسخگویی دقیق سیاسی» بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/657558" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657557">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec543b729.mp4?token=sseMS3C8tSEqPY-E5J1uHjrsm1PSUV0clVq8NVdk4raoHe7lhZOXSLi_UvePvEiFTz8QtG6tzcoA5ZtUeBmQu-jmq7JpaFGOZdIsEij8mPyJN_gUqr6wK5MbhLo-1l2YtB2dG-icZMs5ekjsR1tIGGfoUUgDq9JZiAoKuRabtM1GAMz-TRc_MhLCbgYdHGopHSafGYwbqsZb8Y7KZ5fg01FFqG8jyHM0vvTIMar_frT1eAxPragOFSm7IXvJR6QUgLTUSZTvDezoabSedBrTxQg1UeCOluu1J7MCw3NacTUcJW_JCO2yW4DeZUrG4eHoZM3818yguC7ewLem4EHIDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec543b729.mp4?token=sseMS3C8tSEqPY-E5J1uHjrsm1PSUV0clVq8NVdk4raoHe7lhZOXSLi_UvePvEiFTz8QtG6tzcoA5ZtUeBmQu-jmq7JpaFGOZdIsEij8mPyJN_gUqr6wK5MbhLo-1l2YtB2dG-icZMs5ekjsR1tIGGfoUUgDq9JZiAoKuRabtM1GAMz-TRc_MhLCbgYdHGopHSafGYwbqsZb8Y7KZ5fg01FFqG8jyHM0vvTIMar_frT1eAxPragOFSm7IXvJR6QUgLTUSZTvDezoabSedBrTxQg1UeCOluu1J7MCw3NacTUcJW_JCO2yW4DeZUrG4eHoZM3818yguC7ewLem4EHIDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
اتفاق عجیب روی آنتن زنده
🚫
😮
توی شبکه سلامت مجری از یک کرم استفاده میکنه که مهمون برنامه گفته چین و چروک رو توی 2 دقیقه از بین میبره. منم تا نتیجه اش رو ندیدم باورم نشد ولی واقعا توی 2 دقیقه 10 سال جوون‌ترش کرد.
😳
☘
این محصول گیاهی توی ایران خودمون تولید میشه
🇮🇷
و متخصصاش دارن به مردم مشاوره 100 درصد رایگان میدن.این فرصت محدود رو از دست نده.
👇
👇
bam30.net/ads/landings/22565-2e958
bam30.net/ads/landings/22565-2e958
bam30.net/ads/landings/22565-2e958</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/657557" target="_blank">📅 09:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657556">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
منابع لبنانی از دو حمله جنگنده‌های رژیم صهیونیستی به شهر النبطیه در جنوب لبنان خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/657556" target="_blank">📅 09:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657555">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozWdhUSq8_NriRREoPVkZ_IGelPE9q_ppolAjMOc1EOFKOBNYTWE1spuIx9XZU6M0NZLjSbPMerNuYc4z-kTQvjK37a06Tm2JYn-fJ8CFTNanTRzP9wwykJQq5nepSTnrrAOHnhvN95F5Zd4Z-yBAnm9J11fHU2yKSuVi0sLcu1blz7zsMAclUa6OZ5hY-503wDvSLzuJDNebTTfUKlQDB15eLwzPRtSBWnDJhS2tzZ8t3r9ZTRrQwFMreH46Nr34dmcnlNG9GngrhfVUBx4Vnq03LKUJoflINTkq0_pZqnTpDpezYnvsorwHez3UsJqzKqC_gDn1ZKC-Uv-vL1Jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس وارد کانال ۴.۵ میلیون واحد شد
🔹
شاخص کل بورس تهران با رشد ۹۰ هزار واحدی روز متفاوتی را رقم زد و ۹۶ درصد بازار سبز پوش شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/657555" target="_blank">📅 09:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657554">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794b8b8bec.mp4?token=Ei_b3nLIIELrFOeYTnBU_Vg7IZDpzj4zsZUzWKY17CunX9UqdWIQ0tPdhfMPCHXXlFl0hVshKmZYTF0oRf75O-Htu-3QEa8NGB8GZR85M7-BTLrbWF31ShDIOrQa5kggeuqv-UwiSj__B3BYbykqYMCrrvEE3qGPGyoWvlBhKxLXaiCv7QCnDe_EUh9OwAk40jN7u4bSSTB4ql1-HXg8SSMhktnZFPVzqIbuE0fK-r0QJP-QSNc6L940XlHDXYKBfLxednIFNiciNv3roU5EGE8xmuotNM1F3dxEyPGTtmIVwaKiNGyJOUtCHUB7PIHIu33cYrBDBDko7M9yOI2Izw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794b8b8bec.mp4?token=Ei_b3nLIIELrFOeYTnBU_Vg7IZDpzj4zsZUzWKY17CunX9UqdWIQ0tPdhfMPCHXXlFl0hVshKmZYTF0oRf75O-Htu-3QEa8NGB8GZR85M7-BTLrbWF31ShDIOrQa5kggeuqv-UwiSj__B3BYbykqYMCrrvEE3qGPGyoWvlBhKxLXaiCv7QCnDe_EUh9OwAk40jN7u4bSSTB4ql1-HXg8SSMhktnZFPVzqIbuE0fK-r0QJP-QSNc6L940XlHDXYKBfLxednIFNiciNv3roU5EGE8xmuotNM1F3dxEyPGTtmIVwaKiNGyJOUtCHUB7PIHIu33cYrBDBDko7M9yOI2Izw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در فینال NBA هو شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/657554" target="_blank">📅 09:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657553">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
دبیرکل فیفا: جلسه مثبتی با تاج داشتیم
‌
🔹
فیفا همچنان به گفت‌وگو و همکاری با فدراسیون فوتبال ایران ادامه می‌دهد تا اطمینان حاصل کند که تیم و کاروان ایران، از تجربه‌ای مثبت بهره می‌برند و همه شرایط لازم برای رقابت در زمین را دارند. ما مشتاقانه منتظر هفته‌های آینده هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/657553" target="_blank">📅 09:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657552">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0e58cb23.mp4?token=PDVVfCukyxLWcQGN3dvON_f73yiXkaM4Vd9DwJUBy2F9XjA8EV9yAUxFf8hgoUTWI1LZn-SHCAPDa0e28aLo-Nn3GsOV2Ta7eSuBShPjE0vpTeLy2ca8ZSOqlMOvyMQl3Bnlrr5cDgJiDAfQiQvQdl1xhdp41uBu_WgjMdCcA-hhhHuoBrpdVf8OAhX_FN3IdKGpD2V5TKllhz0A5j7d8KKcrEKyS4v6RWt0urzzrmiGbEpmaUb1pGkYOWhf90VICn61yHj_QcWPVZRi3By3oNi8iiJJBXwpgq98U-rwSiEDhuKw4OBdvX-3MjJZx_1mQ5mBz7mI0WU_O6E3Yw9xKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0e58cb23.mp4?token=PDVVfCukyxLWcQGN3dvON_f73yiXkaM4Vd9DwJUBy2F9XjA8EV9yAUxFf8hgoUTWI1LZn-SHCAPDa0e28aLo-Nn3GsOV2Ta7eSuBShPjE0vpTeLy2ca8ZSOqlMOvyMQl3Bnlrr5cDgJiDAfQiQvQdl1xhdp41uBu_WgjMdCcA-hhhHuoBrpdVf8OAhX_FN3IdKGpD2V5TKllhz0A5j7d8KKcrEKyS4v6RWt0urzzrmiGbEpmaUb1pGkYOWhf90VICn61yHj_QcWPVZRi3By3oNi8iiJJBXwpgq98U-rwSiEDhuKw4OBdvX-3MjJZx_1mQ5mBz7mI0WU_O6E3Yw9xKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از چاقو خوردن الهه منصوریان در فدراسیون ووشو!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/657552" target="_blank">📅 08:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657551">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3750d770.mp4?token=eRZHWL7QmMyFOmEUrVwQb8zpV6yfkbk_RIJ3Nu-FFIETyyQfGSUBUrh9-ckhRIRgQ6vYwUB9syXGrlr4sOSyS3nhsk3YlAIpBac3aWyicE1VQP9DUZbAoKg5VWReg6G7XuaAt_k1nReOmOH8vmhUHKsWB68OEZdhdE8ZLw-dGuxceEuWYRmX8F1vBzVnMrQRyg7EFxQvYMVPMkveyN-v3gHmmwM09EknHmGxCJkAt76x91pcQBfy0Fcudu9C9RubJe0PS4zQX2-7tZ4VGZTGTcV7dokoqIDlycSIE0meC7kHxrktdx6stUQdKaU9KLuQiLJ6B_S32_23GrZZ7YSpLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3750d770.mp4?token=eRZHWL7QmMyFOmEUrVwQb8zpV6yfkbk_RIJ3Nu-FFIETyyQfGSUBUrh9-ckhRIRgQ6vYwUB9syXGrlr4sOSyS3nhsk3YlAIpBac3aWyicE1VQP9DUZbAoKg5VWReg6G7XuaAt_k1nReOmOH8vmhUHKsWB68OEZdhdE8ZLw-dGuxceEuWYRmX8F1vBzVnMrQRyg7EFxQvYMVPMkveyN-v3gHmmwM09EknHmGxCJkAt76x91pcQBfy0Fcudu9C9RubJe0PS4zQX2-7tZ4VGZTGTcV7dokoqIDlycSIE0meC7kHxrktdx6stUQdKaU9KLuQiLJ6B_S32_23GrZZ7YSpLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیپلمات ارشد سابق آمریکا در گفتگو با بی‌بی‌سی: ایران با این حملات، قواعد جنگ را بازنویسی کرد و این پیام را رساند که هروقت صلاح بداند می‌تواند به اسرائیل حمله بکند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/657551" target="_blank">📅 08:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657550">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299e25219a.mp4?token=bOgzRj-JuOvvo7_iJsLylKdAGCnCFInkjYV90KsXOEDwDaBCIeZ3RYGW08z4bxrGyLdxAhZKJUtsO-MCsa-BCw1tcpYzivVGK3U7kI-VZThkQ_pEutUVL4bVNhaQwdjNaiwChhO5Y_a53uG4ROrLrxRTcYJpH6yRX2_pv9VyOmGQTuTaUrDu-B6rZ68J-2TJRY6oV3r7y6yIbXf3KQdyXaEgAEwkXuLgRKObFdInSxyRuuMUCVhqE-PO1bC8We5cXB-QiQFIVLe3XpTIiPPpkXMyw-QFfVeOtC2FaoRYYkNiZELdhTzZkSck3CwL9igekaXWZpOx0BR8z8zSZGw1Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299e25219a.mp4?token=bOgzRj-JuOvvo7_iJsLylKdAGCnCFInkjYV90KsXOEDwDaBCIeZ3RYGW08z4bxrGyLdxAhZKJUtsO-MCsa-BCw1tcpYzivVGK3U7kI-VZThkQ_pEutUVL4bVNhaQwdjNaiwChhO5Y_a53uG4ROrLrxRTcYJpH6yRX2_pv9VyOmGQTuTaUrDu-B6rZ68J-2TJRY6oV3r7y6yIbXf3KQdyXaEgAEwkXuLgRKObFdInSxyRuuMUCVhqE-PO1bC8We5cXB-QiQFIVLe3XpTIiPPpkXMyw-QFfVeOtC2FaoRYYkNiZELdhTzZkSck3CwL9igekaXWZpOx0BR8z8zSZGw1Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: هرگونه خطای محاسباتی علیه امنیت ملی ایران، با پاسخی به‌مراتب سخت‌تر و پشیمان‌کننده‌تر از عملیات‌های پیشین مواجه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/657550" target="_blank">📅 08:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657549">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
اسرائیل هیوم: حمله به حومه جنوبی بیروت با واشنگتن هماهنگ شده بود و روبیو ترامپ را متقاعد کرد که در پاسخ به ایران از اسرائیل حمایت کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/657549" target="_blank">📅 08:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657548">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4a89c288.mp4?token=sN7b3kH4RZ_oRYDUFjbjIzwRlXdYmYOk9Zw9jCa8yaHbUmrlFiMqf1aTUi7h_xjhInFpYX_wl8Si0dNx0_ypgpEIIJiXr28vcZvRwh48kIme_exGN_o9IXfUhauxU9ch0D-1CjIpkhQzWtcQZ2a9n-Cv1rt0iFDETrq8bz5GzCpp0y8PpJXmpITRram_1-a2obOAK3QVWCfLeKM7uUEbVII0sU2EeaS4tJJo_m8Z68zEGYxgxOpWrNaQ5Fq0lUUc4UMgLLH2Z-5lq_VPP2UgKemDapYP-4RFxayszNkO_LxoXSKdlFibR4-hDZwozZXcFnkEfejiAp3CJWGEH86iqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4a89c288.mp4?token=sN7b3kH4RZ_oRYDUFjbjIzwRlXdYmYOk9Zw9jCa8yaHbUmrlFiMqf1aTUi7h_xjhInFpYX_wl8Si0dNx0_ypgpEIIJiXr28vcZvRwh48kIme_exGN_o9IXfUhauxU9ch0D-1CjIpkhQzWtcQZ2a9n-Cv1rt0iFDETrq8bz5GzCpp0y8PpJXmpITRram_1-a2obOAK3QVWCfLeKM7uUEbVII0sU2EeaS4tJJo_m8Z68zEGYxgxOpWrNaQ5Fq0lUUc4UMgLLH2Z-5lq_VPP2UgKemDapYP-4RFxayszNkO_LxoXSKdlFibR4-hDZwozZXcFnkEfejiAp3CJWGEH86iqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر هر روز یک دقیقه این حرکات رو بزنی پاسچرت(حالت قرار گرفتن بدنت) اصلاح میشه #ورزش_صبحگاهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/657548" target="_blank">📅 08:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657546">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2mvbwYr30zL1SYm0cIBn7TfTVqA6DZ07vWUYs0RvxUUYRdyLlIU8JxKFfNJZpg98Q_SLPyBu4xq9v-2-zGU-dDvm-x4rwNAjU2F2BU2L-xqdrjU9kBsIMKX8eynIhkqDG6T-nZc-oBqmbronNoBnY4wEGnX2-aM8LCfqZTMOSv1lXkOs1FrprZoetZ-4vC23hN3nyk_geqcv4n2shbt8f-1Ttfax8zNEoEtkU5lN_4pbKcMHyhM6kBoWlJtKntHxJ8HrsWYXnyGg49JBSAslkU3nXOB14iqfeQ5cO2a7I5lxZf5mupGVXh75_kSu12YGPM-iFi_XiCZ-PTYwOzV5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جوسازی لس‌آنجلس‌تایمز برای تیم ملی ایران
لس‌آنجلس‌تایمز:
🔹
تیم ایران با سنجاق سینه‌های طلایی شماره ۱۶۸ به یاد کودکان جان‌باخته در حمله موشکی به یک مدرسه ابتدایی در میناب، همزمان با آغاز آماده‌سازی برای جام جهانی، وارد تیخوانا شد.
🔹
حرکت یادبود بازیکنان، ممنوعیت فیفا در مورد پیام‌های سیاسی را آزمایش می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/657546" target="_blank">📅 08:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657545">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
سقوط بالگرد نظامی آمریکا در نزدیکی تنگۀ هرمز
🔹
طبق گزارش نیویورک تایمز، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند./ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657545" target="_blank">📅 08:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS1j_77YWqbxlvXRd0QpE5yzzy93nunBcagEmVtdXjemJGUUtMVhu4YnamcYHVDFthdOqeE3yehS-pYoav1h31AWEWnTrJz-VWZDiekzx4Pk4nmo991JDSRHjcw8Qr5A8UpMKW3FaexGw56oA-cSSYBVyGP1Ench7aHXYngWTwD-JxTibt0NqccRrjnWq7A3Ls8YQr0AX_sTYo759_Mf8SFqKKyMC98s-9Hl0Nbns-5QdKUyZzC0Dsil__c7vzyT49niJ7yOfmdWvV-tGYiHiN0qNK4XEdnoBPSyam-hVZ9ZPrmmFbWuPz_9r0PAfeY3SaYyiqfF7peglJ9D32g9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: همه ما در قبال حفاظت از محیط زیست مسئولیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/657544" target="_blank">📅 08:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پرواز‌های شهر فرودگاهی امام خمینی (ره) برقرار شد
🔹
هزینه صد روز نخست جنگ آمریکا علیه ایران از ۱۰۵ میلیارد دلار عبور کرد
🔹
تیم ملی امید از بازی دوستانه با بحرین انصراف داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/657543" target="_blank">📅 08:08 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
