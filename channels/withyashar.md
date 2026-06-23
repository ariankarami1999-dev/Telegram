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
<img src="https://cdn4.telesco.pe/file/vTwKHL0SD_peP_Vtu02mtyH8TQVdJt4TY51i9LYQCvALDmFEe5N6iYyWVlUYK014mVuyrPbRQ5teV-6Sdt4_beW98dJhcioT8Bx_XsXMnriLiNq4_Nu3guGqldaHUHoOj5ergAH9GW5dntAqh5EVYDMxw_XcPRGfIeruc3-Hzp0LOxgLmAsKH7W93QQ1x7rNme36eVVU1-aPEPvnvbi-EKqVGwihkI4_N5ngvWvNNdM_CdXPpCHxm2XZYNBDdsPnQKcumHCS80Zr_T4lIZC9DPaVvSAK-RDNHKd39hf0aLjRrw0BHvza9VNA7KApzvfJSuIie5oLa50JSBGcOBcGdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 02:13:40</div>
<hr>

<div class="tg-post" id="msg-15695">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6xgU1Bii5a_0FYHJDtvXFAW2tSWutSen6Usjhh-_FXDkpuN3ADICEAx4GEbABsWCscZ96rx5albT_UOrF6VOTkBNSmatU0sW0JQ_AeXlmcDQtvDrMgTttcTkutIdAI46PwHSBnaJrDGMeZyhJz9I_0ff3EL5zYXEcXLQLwP5fB3Q4Hp6uu9uNhX-Ljg7E39FWT3gSYluTS7fNSdByXzP8iYJb-dFMUautSWmJgaMdCc7VxnyZkOettzB6fI5oAqq7KZJjgUUVujPh_ZXHOoOFgpR7HSoAOCrBGT7rQL-I_ZXY-Ugff1eseHUaST3AQEmPdzqLt4Itox01l5ubjS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۳۰ نفتکش حامل نفت خام ایران که دستگاه‌های فرستنده و گیرنده AIS آنها فعال است!
اکنون به سمت آسیا، چین، ژاپن و کره جنوبی در حرکت هستند و بیش از ۵۰ میلیون بشکه نفت حمل می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/withyashar/15695" target="_blank">📅 01:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15694">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ‌ در‌ پنسیلوانیا:  ایران قلدر خاورمیانه بود.
ما باید این مسیر را انجام می دادیم. باید به ایران می رفتیم.
شما نمی توانید اجازه دهید که خاورمیانه و سپس ما را منفجر کنند، اگر این امکان پذیر باشد. ما قبلاً آنها را می گرفتیم، اما آنها اسرائیل را منفجر می کردند. آنها می توانستند کل خاورمیانه را منفجر کنند.
به توافق صلح تاریخی با ایران دست یافتیم
ایران عالی بوده است. اگر ایرانیان هوشمند باشند، منطقی خواهند بود؛ در غیر این صورت، مجبور خواهیم شد کار را به پایان برسانیم که احتمالاً کمتر از یک هفته طول می‌کشد.
اما فکر می‌کنم همه چیز برای آن‌ها خوب خواهد شد. آن‌ها کاری که باید انجام دهند را انجام خواهند داد زیرا ما می‌خواهیم این کار انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/withyashar/15694" target="_blank">📅 23:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15693">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سنای آمریکا به پایان جنگ با ایران رأی داد  سنای آمریکا تصویب کرد که ادامه عملیات نظامی علیه ایران مستلزم کسب مجوز کنگره است. @withyashar</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/withyashar/15693" target="_blank">📅 23:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15692">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سنای آمریکا به پایان جنگ با ایران رأی داد
سنای آمریکا تصویب کرد که ادامه عملیات نظامی علیه ایران مستلزم کسب مجوز کنگره است.
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/15692" target="_blank">📅 23:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15691">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانال ۱۴ اسرائیل نقل قول‌های اختصاصی از احمد وحیدی، فرمانده سپاه پاسداران، خطاب به مقامات ارشد رژیم را منتشر کرد.
1 «ما رئیس جمهور ترامپ را به زانو درآوردیم. ما به آنچه می‌خواستیم رسیدیم. طبق معمول، غرب احمق فکر می‌کند که در عوض چیزی از ما دریافت می‌کند، که البته هرگز اتفاق نخواهد افتاد.»
2 «هدف ما در حال حاضر این است که آمریکایی‌ها را در تنگنا قرار دهیم. هرگونه تخلف، هر چقدر هم کوچک، به ما اجازه می‌دهد که تهدید به بستن تنگه هرمز کنیم و ترامپ و مردمش با هر چیزی موافقت خواهند کرد.»
3 «ترامپ فکر می‌کند پولی را که به ما می‌دهد صرف خرید کالاهای آمریکایی خواهیم کرد. این هرگز در طول عمر ما اتفاق نخواهد افتاد.»
4 «حالا باید به آمریکایی‌ها بفهمانیم که اسرائیل بازیگر بد خاورمیانه است. هدف این است.»
5 «از هیچ چیز دست نکشید. تهدید کنید. و در صورت لزوم، از مذاکرات کناره‌گیری کنید.»
@withyashar</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/15691" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15690">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نخست‌وزیر پاکستان: هفته آینده با مجتبی خامنه‌ای در ایران دیدار خواهم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/15690" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15689">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15689" target="_blank">📅 22:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15688">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام ندهید. در غیر این صورت مسئولیت با شماست و توسط حرص و طمع خود شما انجام گرفته. به این مسئله دقت کنید و
فقط از تحلیلها و مطالب آموزشی افراد استفاده کنید
. هیچ پکج یا هیچ پرداختی به هیچ بی ناموسی انجام ندهید.
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
از توجه شما به این مطلب سپاسگزارم، یاشار</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/15688" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15686">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSyXYdfCNHETiWCqdvzyBQzo0mB9nSzofoMey4a1FQ15rEeZuchGP7GNRLhSQsF7ds227ZguzrWPnCel66PAYU5_kQQFprBCb6f4gyurBUo1BqXeZTvN6LzMTyEc1_XGwO33xNFOD2bDNm6Ee2qd_FmcrupqO4c5KVMxPwayXkgMsv-gBqAE20Ua0e1kuRdG0lgx11PQ8FxL-jdkjDEHPYIPqNYws3vwes5vyZ_6NFMWYNiG22mTyTkxA-au79vu0yU-LyN026J4r9D10RTPykYn0BQI7L-J0TE9mTg6DLcWHMoIMSOGLjaOS3IKjrWXO10qSW2FCzeWMMCAD54hfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه اسرائیل با انتشار نقشه تونل کشف شده جدید حزب الله نوشت:
حزب‌الله با حمایت مالی جمهوری اسلامی طی سال‌ها(صدها میلیون دلار) شبکه گسترده‌ای از تونل‌ها، انبارهای تسلیحاتی، سایت‌های موشکی و مراکز فرماندهی در جنوب لبنان ایجاد کرده ، هدف این زیرساخت‌ها حمله به اسرائیل بوده
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/15686" target="_blank">📅 22:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15685">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7644ffed31.mp4?token=aS4BnQnEPgUYW8udy6MC2XZRoYhHJFFXxvFUrm8z3Ee_cYx_q5QEwptC9BYN6JuevruE8FCzKy5D_DPibf9gy6qtBOSzaZ34xVvtZkCv5nj7Nc79xkzvzEN1uZ-WV5k2hH3pinnkQ8xBG6Mo2SPl3_C6jBAdEUpzKH8qgH5v9gCfBEXmGoqxnOB1O83RbfIpdyoWlXwUW2E9eTufzXjRrN73vlwO3CCLUeHoq0j_iqv0MMIHM4XCtJXQU1QHsbr2tKkhMxZn1uer2JEMwi3HnM60rHyc-eJWfNgSpTfPWFdXi1xV1twPc-ObcrD23vGAb2gK84Oixqfmk7-VjfaUSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7644ffed31.mp4?token=aS4BnQnEPgUYW8udy6MC2XZRoYhHJFFXxvFUrm8z3Ee_cYx_q5QEwptC9BYN6JuevruE8FCzKy5D_DPibf9gy6qtBOSzaZ34xVvtZkCv5nj7Nc79xkzvzEN1uZ-WV5k2hH3pinnkQ8xBG6Mo2SPl3_C6jBAdEUpzKH8qgH5v9gCfBEXmGoqxnOB1O83RbfIpdyoWlXwUW2E9eTufzXjRrN73vlwO3CCLUeHoq0j_iqv0MMIHM4XCtJXQU1QHsbr2tKkhMxZn1uer2JEMwi3HnM60rHyc-eJWfNgSpTfPWFdXi1xV1twPc-ObcrD23vGAb2gK84Oixqfmk7-VjfaUSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک یه ویدیو از محرم پست کرده
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/15685" target="_blank">📅 22:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15684">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7cLNzmXhNDLDIDi57_gyEgV-wjgjzpn0Bq_QxwlQrRf2NO8f1Wyu4R5fJsec0K2nbar4QP5Gq2qAvEuRDKEBR7-47WO41Lllw0nZft2UH6Vj0GOJVluP5v4FmhLoK3-Xct-tMk-sJR3GNWwQuqdEJU1eL_CPhr4MZ-W4sxnBGae8HTIfvq6T7SymrVlWeoQk7ZPTt6fzTt3bkCcVQz4svhZOklNtMjycEaZ10EWtV6i3uHD6AdRttg-FkkFoQbEUS0Szd9K451150eVLbHtMfZtQ2NMoUXFIX2EQt9cKYbvprLyb_2DyBb_6LwBVQFYburs2fYdPb6SY6EKcRnFUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مبینا محمدعلی‌پورثانی پس از ۱۰ روز پیدا شد
سیدامیر احمدی، دادستان عمومی و انقلاب بهارستان:
مبینا محمدعلی‌پورثانی، دختر ۱۹ ساله ساکن نسیم‌شهر، پس از ۱۰ روز بی‌خبری پیدا شد.
این دختر پس از پیگیری‌های قضایی و اقدامات انجام‌شده، پیدا شده و در سلامت کامل به سر می‌برد.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/15684" target="_blank">📅 21:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15683">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، در مصاحبه ای با شبکه سیان بی سی به وضعیت شکننده حکومت جمهوری اسلامی اشاره کرد و فروپاشی آن را اجتناب ناپذیر اما از نظر زمانی غیر قابل پیش بینی دانست.
وی با مقایسه شرایط کنونی ایران با وقایع تاريخي غير منتظره ای نظیر سقوط دیوار برلین و تحولات رومانی، تأکید کرد که شکاف های عمیق و پنهانی در زیر لایه های این نظام در حال گسترش است. نتانیاهو با بیان اینکه حکومت ایران در حال حاضر به شدت ضعیف شده است، تصریح کرد که اسرائیل همچنان بر موضع خود مبنی بر کمک به مردم ایران برای سرنگونی این رژیم پافشاری می کند؛ هر چند زمان دقیق وقوع این اتفاق در کنترل یا انتخاب آنها نخواهد بود و به روند گسترش این شکافهای داخلی بستگی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/15683" target="_blank">📅 21:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15682">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: هیچ عجله‌ای برای ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/15682" target="_blank">📅 21:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15681">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رکورد تاریخی رونالدو در جام جهانی ۲۰۲۶ کریستیانو رونالدو با گلزنی مقابل ازبکستان در جام جهانی ۲۰۲۶، به نخستین بازیکن تاریخ فوتبال مردان تبدیل شد که در ۶ دوره متوالی این رقابت‌ها موفق به گلزنی شده است. این گل که در ابتدای بازی(دقیقه۷) به ثمر رسید، به انتقادها…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/15681" target="_blank">📅 21:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15680">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رکورد تاریخی رونالدو در جام جهانی ۲۰۲۶
کریستیانو رونالدو با گلزنی مقابل ازبکستان در جام جهانی ۲۰۲۶، به نخستین بازیکن تاریخ فوتبال مردان تبدیل شد که در ۶ دوره متوالی این رقابت‌ها موفق به گلزنی شده است. این گل که در ابتدای بازی(دقیقه۷) به ثمر رسید، به انتقادها علیه این ستاره ۴۱ ساله پایان داد.
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/15680" target="_blank">📅 21:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15679">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرنگار : ایرانی‌ها می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
ترامپ: بلوف میزنن ، اونا داخل به ما گفتن و ما ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.
@withyashar</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/15679" target="_blank">📅 21:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15678">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارسالی : یاشار جان بانک رفاه و سامان و بلو بانک هم از کار افتادند ، ساعت شش عصر
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/15678" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15677">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26cd4a0fb.mp4?token=DcW4iI8TP3FihLCOgsAtT_5xWaTrF-oC1govTT6kQQNjTWd6KNX2rL0KJnRy6clCzr22-94Q1u99O25ywF9hxQmreBd-6efQrOY4QQVpOH03XiiN0muQah0BHyYRAVCjRh2o19gaeAaMe_gueU4kDjvcy5oBYU2s1IWAgQxUigTC5h2i384jOimeJuHqfWpGx_mpsglw1QrCwtJMio8oMZgCrB7kBTA_rJkz6YvcZYc9kIPSfUu61YRb_iHO9EnW-aWRLQ4yu5-edqAVPJMP6g-vZ8OWnWGw29LKMkP7PPvVykeyzZ0gCsNGIms5aNfyPfnykBAny6Sq0m09c0HLhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26cd4a0fb.mp4?token=DcW4iI8TP3FihLCOgsAtT_5xWaTrF-oC1govTT6kQQNjTWd6KNX2rL0KJnRy6clCzr22-94Q1u99O25ywF9hxQmreBd-6efQrOY4QQVpOH03XiiN0muQah0BHyYRAVCjRh2o19gaeAaMe_gueU4kDjvcy5oBYU2s1IWAgQxUigTC5h2i384jOimeJuHqfWpGx_mpsglw1QrCwtJMio8oMZgCrB7kBTA_rJkz6YvcZYc9kIPSfUu61YRb_iHO9EnW-aWRLQ4yu5-edqAVPJMP6g-vZ8OWnWGw29LKMkP7PPvVykeyzZ0gCsNGIms5aNfyPfnykBAny6Sq0m09c0HLhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان دکترای افتخاری از پاکستان دریافت کرد
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/15677" target="_blank">📅 20:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15676">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تتر 163K
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/15676" target="_blank">📅 20:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15675">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/15675" target="_blank">📅 20:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15674">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vlt-Z5aqnE_4yBKJP6AjRWnTAYtIF5r73NXk7ZlgbzAVQtxlP4UTJDew8GeK4WMA4lS9oT7B-bNfPQkWWVSbZ741RHCTJ2KwsWuczBnD_BcJtRW_kB3_M4jq61SVuoTo7q_31iIPiE7Xecm7fGr9L0PiqMp7G07hblCHxBIg9pcLdBSg-4EgEHlR-twtz5-nsPqFw4y5vUt6NgpSPMCcBZE46aq-Hf__SaZBkhpjOnX7khfAG-r73z-sb9bwtTVp4TQIjO0Yla8WM7JWCdOxkkQ8Lo8QWCCZp8-412E6plTgZlqxnVuzfQ7uzBWVIcSsSU-UPJD2WktpSDyypCgGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شواهد نشان میدهد مدیران دفتر انتشارات مجتبی خامنه‌ای دقیقاً امضای ابزار یکسان ، نسخه یکسان و سیستم عامل یکسان دفتر انتشارات قالیباف استفاده کرده اند.
در‌نتیجه هر دو نامه قالیباف و مجتبی خامنه ای با یک کامپیوتر نوشته شده در ابتدا و بعد از اوایل ماه ۶ میلادی، اوایل خرداد ماه، رایانه را از مک به رایانه ویندوزی تغییر داده‌اند.
@withyashar
پیشتر در ویدیو اتاق جنگ گفتم که ای آی دست ممباقر هست!</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15674" target="_blank">📅 19:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15673">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ریاست جمهوری لبنان:
ونس و وزیر خارجه آمریکا خواستار تشکیل یک کار گروه آمریکایی، لبنانی و ایرانی برای تثبیت آتش‌بس شدند
آن‌ها گفته‌اند که ترتیبات مربوط به حوزه اختیارات این کمیته و نحوه تشکیل آن، در دست بررسی است
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/15673" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15672">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هاآرتص به نقل از منابع آگاه: تل‌آویو علاقه‌مند است در مذاکرات واشنگتن راه‌حل‌هایی پیدا کند که مداخلهٔ ایران را از تحولات لبنان دور نگه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/15672" target="_blank">📅 18:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15671">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4IbgHGZtAvuGFRMnUxmFMcWyyogHpUz0YcRmDo8H9QLZP9CAsXjsxkniWC6b8NRS9otMKXH4hqXncTf1NLZpkT-TUTiL4W-MzJXaK81jwJJAa1Bycc_Hj11NW62EJErCHHeGAQuBJD8_V_jH7f1CTvB5BVsHjRtqEf_zNwO3GVM2cQuVQdQLvkqXS8ewPx7p-KkXh1HqUwG2d7l4D4Hlznf-1-wOaj4zZb_POefkNdc9w0uBIST6UTYsnlXuA8YlgMR9sGMZ6jLCbeKtT3-aI0ENf9VCASyUj9SoEiY0ZXSbtqa8uzZQKmiQXoLGMivxuc_-gqnJuyEpuBWtH7T0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ما هستیم ناو ها هم هستند نگران نباشید
ناو هواپیمابر USS جورج اچ. دبلیو. بوش (CVN 77) در دریای عرب(شمال‌غرب اقیانوس هند ابتدای دریای عمان جنوب ایران ) در حال حرکت است.
دو ناو هواپیمابر به فعالیت خود در خاورمیانه ادامه می‌دهند در حالی که نیروهای آمریکایی همچنان حضور دارند و هوشیار هستند.
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/15671" target="_blank">📅 18:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15670">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عمان و ایران بیانیه مشترکی منتشر کرده‌اند که در آن قصد خود برای ایجاد یک مدیریت مشترک آینده برای تنگه هرمز را تأیید می‌کنند
این بیانیه همچنین به طور ضمنی تأیید کرد که مطابق با استانداردهای بین‌المللی
هزینه‌هایی برای خدمات دریایی اعمال خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/15670" target="_blank">📅 17:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15669">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فایننشال‌تایمز
:
با وجود افزایش سطح تردد کشتی‌ها در تنگه هرمز، مالکان همچنان سردرگم هستند؛ این وضعیت در حالی شکل گرفته که ایران کشتی‌ها را تهدید به عبور از مسیر نزدیک سواحل خود کرده و آمریکا مسیر عمان را پیشنهاد می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15669" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15668">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هم اکنون حمله پهپادی هدفمند به خودرویی در جنوب لبنان،گزارش ها از ترور چندین عضو حزب الله.
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15668" target="_blank">📅 17:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15667">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شهباز شریف نخست وزیر پاکستان: مذاکرات ایران و آمریکا شامل دارایی‌های هسته‌ای، موشک‌های بالستیک و دارایی‌های مسدود شده ایران خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/15667" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15666">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzn-TaOvCWUnOrNSy2KyFgj5q8TvYQeIOiYKJSPlZNLRs-P-J02AMaoAoDtZIuIgARSDTn8kV9SOUPRlwWGZqzvl3VhUVRxiWgoxIoZtKmS8VoO5OeEYod8xx4RSxxA5rsEhdvDXIvGH94d-Us-zMFixEWDVC1fkJymHCtfB4nYVhTa0NrzWExOC_AV0XuNJz6Jzxq9oM6mL0ULDQeejaKaedD78gqdbcgNYDF5YwwVIUjHbw0zUxHrzPLdIgDxqUkv8S-JKCYJ4nhJUGWnDdZ9GqQhZBDkxbi-DrL1V0OA5iLcQbGaByX7pon-4UHIkOx_WixMUPTVDMQGjVtbFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز دایرکتی از طرف یکی از شما دریافت کردم که گفت از‌ کارمندان رتبه دار بانک است و این قطعی نه هک است نه چیز دیگری و به طور عمد از طرف خود رژیم انجام شده وی افزورد تقریبا با یقین میگم پایین اوردن دستوری قیمت ارز و طلا،حاکمیت و دولت با سرکردگی همتی و سیف میخواهند در قیمت های پایین فقط خودشون خریدار مطلق باشن و یک نوسان جانانه از بازار بگیرن با اختلال عمدی در سیستم(چون میدونن سرمایه دارها میدونن قیمت برگشت میکنه به بالا و پولشون رو میکشن بیرون که طلا بخرن،اما با قطع عمدی و به گردن هک شدن)
در نتیجه از دوستان هکر قدیمی دوران جوانی جوییا شدم که در امنیت سایبری بانکها کار میکنند. آنها به من گفتند که بعد از عملیات اکونومیک فیوری که آمریکا انجام داد که شامل محاصره دریایی هم میشود و تمام زیرساختهای اقتصادی رژیم را هدف‌ گرفت رژیم ضربه های مهلکی در رابطه با ارز خورده و این ادعا درسته و میخوان پول رو از جیب مردم جبران کنند دوستم گفت شعبه ها هم دسترسی به هر انتقالی را دارند ولی دستور این است که بگویند قطع هست
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/15666" target="_blank">📅 15:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15664">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6rYuIlzLvr0srlB5ppQ2idlT2cQfmZkFZNOopLbQl17kY01uoty0NtoQuLqfVWwnl3GNKm-Xakrd5bPqKEQsq2kALlQl_D6DgrVXUH8ZvzBs5VaB6Ggzuf--qdICQFJCayKLkg9zhit9uQoFH-_X6L_ILbmUSSgZ5cVnuMQJRv7LOslEtRvMqj944OW3Q_LKJSvXAhcW1BCJ07U-xxU3TVjhvsyTYny29MjmH_Rr9rNZTKqdyx4WIUgxbRMJ5Z8QlQiH5p-z7NiV21mNYsTagk4aS3jJCfwrhVagTHJjpECpxPqKzaidyCgWzuZtv3iUX-UqdWEpuqsyHrNQKi5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلبان آمریکایی جنگنده F-15 که در ماه آوریل بر فراز ایران سرنگون شد، به مقام‌های اطلاعاتی گفته است که پیش از اجکت کردن، چندین پهپاد ایرانی را دیده که به‌صورت هم‌زمان و هماهنگ در آرایشی شبیه «عروس دریایی» در حال حرکت بوده‌اند؛ به گزارش سی‌ان‌ان و به نقل از چهار منبع.
این روایت باعث بحث در جامعه اطلاعاتی آمریکا شده درباره این‌که آیا ایران توانسته قابلیت پیشرفته‌ای در زمینه پهپادها یعنی «شبکه‌سازی مش‌مانند یک‌به‌چند» (one-to-many meshed networking) را به نمایش بگذارد یا نه.
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15664" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15663">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnO-srv2b03FarGEmlVVLPqDwjnmbUzbM079-ncFGKe48l5e_l127Q-2ewLq5toIuOvdyF3ZoAnqP5Evpinj9FlxmP2XWh0LUJqOomoXd3sb4xcTN5OuZiIPFvS_kz5y4_qJxRqT_pu8vu_Z2ZujdD5R2EgUIDpgy7XZzIM75Nua2qudj0OXa-_SKNl7an-lIgqikE0oyvxXgzX8VIVnWMbp73ybEbyft6JQb-bezLmyL1oBAuGahk0G8zr6Ss4yYFz3iO0kp6uDmzK-ac7Oj4uejKt0kPlV-W4FLJRUd_CsEg_Nd5RkYLrh-Lwqu7cA6wCNNSsGtvQHqoONTIZh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
اگر آنها با این موضوع موافقت نمی‌کردند، مذاکرات بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات عمده‌ای که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی بیشتری اعمال نشود. با این حال، همه کشتی‌ها در محل باقی می‌مانند تا در صورت لزوم محاصره دوباره برقرار شود، که در این مرحله بسیار بعید به نظر می‌رسد.
پول و یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، در حساب امانی تحت کنترل آمریکا قرار می‌گیرد و صرف خرید غذا و تجهیزات پزشکی، به طور انحصاری از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما خواهد شد.
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود!
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15663" target="_blank">📅 14:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15662">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGB134uS8aMy-0dg_a71duA8-fWM5Qh9fLHQKTGwFcy0uTPT-QfI_yF0zJ2TQLMYPw-FKD0EKfOGlIlIYrzwKoHFb1fmVeCmLkUdYpE6-wXQEGNHuSmCwaGFbFhV3RNP1QdjixPu9dxL_BIQBUuWisPXMP3HWqN6-UlafuydZr9093lbJY7TBariE_y1qvIFVmCcyG35ydBmXvqm_H6127O_shUA1fpegD-jiuXTzxKyVUDN7bp9FgdKZTatr1WDwvp8lhi8pIqXod7ntbyJjHUfF4m-JOxQeYlnbVZev9Q7g7WjUC3w7U6RNBXTWTEdVZRxmQSsA5yl95OuQ8HWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان وارد اسلام‌آباد شد
وی در بدو ورود با نخست‌وزیر پاکستان دیدار کرد.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/15662" target="_blank">📅 14:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15661">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=eNkxVMgGlKx9SCMpx2u7yr4mk5Tj1t6PbXEf7dAYH-xt8u9RZ7laFQerxnKu_fLunHsB4I77ByAszACCZNwJwoNnptsgGpit_GRgR2yxeXoWX7iK1jV2O5EF9u9JH8KzbQwONawgnxqXpN-mbXaA1hYymnqrqnojbAHmm8SRoHJFUKUGeJt4wWwO3hu7jvD0t6dT2mQxn_YmqIZjD36o7tKxdlq52Bd5nrGfqwbPMSFliADpGQ4B7NX_Xt6Qyo9t4OPDs7k9cAdyhv3otB9uFu7Ay-9L7glPM5CbnE5wcgvT0bmnCvFWZmqv3YsLG1e6y8Vn3GO-hdxvHCkT-eJgXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=eNkxVMgGlKx9SCMpx2u7yr4mk5Tj1t6PbXEf7dAYH-xt8u9RZ7laFQerxnKu_fLunHsB4I77ByAszACCZNwJwoNnptsgGpit_GRgR2yxeXoWX7iK1jV2O5EF9u9JH8KzbQwONawgnxqXpN-mbXaA1hYymnqrqnojbAHmm8SRoHJFUKUGeJt4wWwO3hu7jvD0t6dT2mQxn_YmqIZjD36o7tKxdlq52Bd5nrGfqwbPMSFliADpGQ4B7NX_Xt6Qyo9t4OPDs7k9cAdyhv3otB9uFu7Ay-9L7glPM5CbnE5wcgvT0bmnCvFWZmqv3YsLG1e6y8Vn3GO-hdxvHCkT-eJgXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژیم : هک شدیم ، داریم روش کار میکنیم و مشخص نیست کی‌ درست بشه ! شرکت خدمات انفورماتیک: تیم‌های فنی و متخصصان امنیت سایبری در حال رفع اختلالات ایجادشده هستند تا امکان بهره‌برداری دوباره از خدمات فراهم شود. ضمن عرض پوزش بابت وقفه پیش‌آمده در انجام امور بانکی،…</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15661" target="_blank">📅 14:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15660">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رژیم : هک شدیم ، داریم روش کار میکنیم و مشخص نیست کی‌ درست بشه !
شرکت خدمات انفورماتیک:
تیم‌های فنی و متخصصان امنیت سایبری در حال رفع اختلالات ایجادشده هستند تا امکان بهره‌برداری دوباره از خدمات فراهم شود.
ضمن عرض پوزش بابت وقفه پیش‌آمده در انجام امور بانکی، از تمام کاربران و مشتریان محترم تقاضا می‌شود ضمن حفظ صبوری و شکیبایی، اخبار و اطلاعات تکمیلی در خصوص زمان بازگشت به وضعیت عادی را صرفاً از طریق درگاه‌های اطلاع‌ رسانی رسمی و مراجع ذی‌صلاح پیگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15660" target="_blank">📅 14:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15659">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">روزهای شنبه و یکشنبه ۱۳ و ۱۴ تیر، تهران و دوشنبه ۱۵ تیر، کل کشور تعطیل است  معاون اول رئیس جمهور اعلام کرد در روز سه شنبه ۱۵ تیرماه استان قم و پنجشنبه ۱۸تیرماه استان خراسان رضوی تعطیل است. @withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/15659" target="_blank">📅 14:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15658">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">روزهای شنبه و یکشنبه ۱۳ و ۱۴ تیر، تهران و دوشنبه ۱۵ تیر، کل کشور تعطیل است
معاون اول رئیس جمهور اعلام کرد در روز سه شنبه ۱۵ تیرماه استان قم و پنجشنبه ۱۸تیرماه استان خراسان رضوی تعطیل است.
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/15658" target="_blank">📅 14:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15657">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سفیر ایران در لبنان در واکنش به حمله به جنوب لبنان: هرگونه نقض تفاهم‌نامه در لبنان، چالش‌هایی را برای روند مذاکرات صلح ایجاد خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/15657" target="_blank">📅 13:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15656">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اختلال دوباره در بانک‌ها
@withyashar
🚨</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/15656" target="_blank">📅 13:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15655">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1JmrMwm_D93Kme8jkqeAyNxPmPw2cGhv_jwfSArjFEEEkF3r_gA2JoRm3TvnxO-WbwH1goitgW-EfuvQ6lw9y3GW4IrmlwZuMjzNLned3dkMkPgprM6GAHc2ccmDY4JJXVQQEbdh5-JXDEpVnouAxqEj1mFjWCbqwbRZyzUJC64uC8xhXZvvHeVmJM4sEzg64hma4exbbLK8vm_wJaxvz9Qa3-7Wur1esZdM86IXDy_oLo5B-QB887EeXCRA1Sz29vlAjbCRtDp2uzJHCd5Si9SEGhYQb7pMfWcVUE5hEUfqc69C4s27I85zh2gbJWI1z4FEljPW4odVYYzluJIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقض دوباره آتش‌بس ،حمله اسرائیل به جنوب لبنان
@withyashar
🚨</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/15655" target="_blank">📅 13:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15654">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو: حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم @withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15654" target="_blank">📅 13:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15653">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رادیو ارتش اسرائیل: تا زمانی که حزب‌الله کاملاً منحل نشود، از منطقه الشقیف در لبنان عقب‌نشینی نمی‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15653" target="_blank">📅 12:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15652">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتانیاهو: حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/15652" target="_blank">📅 12:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15651">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4MwcoIRf6Iu60hJmANfL7-2b2dn3UBOc2l0hN2D1-VRfGYLX3O6pnTEwPnCkGX0c0MmoxqwpWaU1ch7dvgA2DS52PxEEoyXzcx8g0j513pc3cEV1KXrZJZImgCIhJcRwbKCq_OPtK8wvGnHTbh4zMDMe70vnovDKPk6oizoP8G9KH4nYFVeEDCCXUgsTjcE4AdIWyud-e1ooGBgG9GM9rs2eB09_0CaJ9KS5a5w03C0X9Mfo0wmOrE7CEfj5tX0-ba4Y03jx4020a6h8HvEum9JrAn0MbfAxO1rFsQ5rxsK7-TfKxOXT9-zEbq26ZKef-EQMtsfW0T5KB0wSdXjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون ۷ سوخت رسان شامل، ۵ فروند سوخت رسان KC-135R و ۲ فروند سوخت رسان KC-46A پگاسوس نیروی هوایی آمریکا در منطقه خلیج فارس فعال هستند.
همزمان، دو فروند KC-46A با نام عملیاتی BOBBY 81/82 از پایگاه RAF Mildenhall انگلستان به پرواز درآمده و برای الحاق به یک یگان جنگنده در حال عملیات‌اند.
همچنین بر‌اساس گزارشها پرواز CUBE 31 شامل چهار فروند جنگنده F-35 تفنگداران دریایی آمریکا در حال انجام مأموریت بوده و هماهنگی‌های عملیاتی و ارتباطی لازم را در جریان پرواز برقرار کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15651" target="_blank">📅 12:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15650">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پلتفرم دریانوردی کپلر:
۳۶ کشتی دیروز از تنگه هرمز عبور کردند که این بالاترین میزان تردد در این تنگه از نخست مارس تاکنون است.
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/15650" target="_blank">📅 12:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15649">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:
اگر آمریکایی‌ها فکر می‌کنند ایرانی‌ها برنامه هسته‌ای خود را رها خواهند کرد، آن را لغو می‌کنند و از تمام رویاهایشان برای نابودی دولت اسرائیل دست می‌کشند، بسیار ساده‌لوح هستند.
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/15649" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15648">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: خودروسازان آمریکایی تولید سلاح را آغاز خواهند کرد
رئیس جمهور آمریکا در کاخ سفید به خبرنگاران گفت: «آنها برنامه‌هایی برای تغییر کاربری کارخانه‌ها دارند. ما قصد داریم سلاح‌هایی از جمله موشک‌های پاتریوت، موشک‌های تاماهاک و موارد دیگر تولید کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/15648" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15647">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هواپیماهای سوخت‌رسان نیروی هوایی ایالات متحده پس از تخلیه از پایگاه هوایی العدید در قطر به دلیل جنگ ایران(یک روز قبل از جنگ)، به این پایگاه بازگشته‌اند. حداقل ۱۲ فروند در حال حاضر حضور دارند.
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/15647" target="_blank">📅 11:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15646">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بقایی: توانمندی دفاعی و موشکی ایران هیچگاه موضوع مذاکره با هیچ طرفی نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15646" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15645">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الجزیره: «تغییری بزرگ» در سیاست آمریکا؛ ایران اکنون می‌تواند نفت خود را با قیمت کامل بفروشد
این اقدام صد‌ها میلیون دلار درآمد اضافی برای اقتصاد ایران به همراه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/15645" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15644">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل:
جمهوری اسلامی ایران با بازگشت بازرسان هسته‌ای به ایران موافقت کرده و این اولین گام برای توافقی گسترده‌تره.
برخلاف برجام، این بار بازرسی‌ها باید در هر زمان و هر مکان ممکن باشه.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15644" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15643">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عماد الدین باقی: طبق بند 2 توافق ایران و آمریکا، از این به بعد شعار مرگ بر آمریکا یا سوزاندن پرچم این کشور و لگد کردنش تو مراسم‌ها و اجتماعات رسمی (مثل نماز جمعه) ممنوعه.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15643" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15642">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">https://t.me/boost/withyashar
یه لول اومدیم پایین ایموجی کم شد لطفا اگر کاربر پرمیوم هستید بوست کنید و اگه نیستید از دوستانتون که هستند درخواست کنید بوست کنند</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/15642" target="_blank">📅 02:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15641">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">@withyashar
FPV  آتش بس و</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/15641" target="_blank">📅 01:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15640">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">@withyashar
شصت روز سنگین</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/15640" target="_blank">📅 01:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15639">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8773aac7.mp4?token=UMP5S_VBZCtF_PA-GaAykUWjpt-xDoPkeDgJNiBpMuhJtu8e_iDAYM_Xfq1vjynUbTmfDbQPqZUn7eotG7S2hFgG5L7lojHiWjFXWrvjeFmCmlQTmORHaEBU5FJAO9ASX8iEU4YqaxlEeHggko7IcL0lGJb-Plryjz33UF--IGcF0ctCD_dlHpwCfD8f5zFb_B03oaawha51HAduUMLX-2xiD2cw61IPC3n4RHks3L1_iehbXmTgDkBHOE5fl9H9kd7ekSY_mIi4nX32dCFv4VMMuKTGJjQ6S14wbfpyb0uUDpMuAENHz7AYDK2ns4kwPpN-7u_AIfExu3TXjomSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8773aac7.mp4?token=UMP5S_VBZCtF_PA-GaAykUWjpt-xDoPkeDgJNiBpMuhJtu8e_iDAYM_Xfq1vjynUbTmfDbQPqZUn7eotG7S2hFgG5L7lojHiWjFXWrvjeFmCmlQTmORHaEBU5FJAO9ASX8iEU4YqaxlEeHggko7IcL0lGJb-Plryjz33UF--IGcF0ctCD_dlHpwCfD8f5zFb_B03oaawha51HAduUMLX-2xiD2cw61IPC3n4RHks3L1_iehbXmTgDkBHOE5fl9H9kd7ekSY_mIi4nX32dCFv4VMMuKTGJjQ6S14wbfpyb0uUDpMuAENHz7AYDK2ns4kwPpN-7u_AIfExu3TXjomSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا می‌توانید تضمین کنید که ایرانی‌ها از سود فروش نفت برای بازسازی ارتش خود استفاده نکنند و فقط برای دولت بعدی آماده شوند؟
ترامپ:
خب، آن‌ها قرار نیست این کار را بکنند، قربان. خواهیم دید، اما قرار است پول را برای خرید غذا برای مردمشان استفاده کنند، چون در حال حاضر مردمشان خیلی گرسنه هستند و آن را فقط از ما می‌خرند — ذرت، سویا.
تباید پول زیادی باشد. امیدوارم پول زیادی باشد.
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/15639" target="_blank">📅 00:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15638">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
با یک تماس تلفنی میتوانم محاصره را برگردانم
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/15638" target="_blank">📅 00:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15637">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران شود. @withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/15637" target="_blank">📅 23:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15636">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قالیباف: اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/15636" target="_blank">📅 23:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15635">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ: هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران شود.
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/15635" target="_blank">📅 23:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15634">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرنگار: نتانیاهو می‌گوید نیروهایش لبنان را ترک نمی‌کنند
ترامپ: ما قرار است به این موضوع نگاهی بیندازیم. من یک حل‌کننده مشکل هستم؛ می‌توانم مشکلات را سریع حل کنم، از جمله با بیبی.
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/15634" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15633">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ: «تا زمانی که ایران به ما احترام بگذارد نمی‌خواهم از واژه “ترس” استفاده کنم چون مناسب نیست تا وقتی به ما احترام بگذارد، ما هیچ مشکلی نخواهیم داشت.
ما کنترل کامل تنگه را در اختیار داریم.»
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/15633" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15632">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">قالیباف در سفر به مسقط: در سوئیس توافق کردیم تا 12 میلیارد دلار پول مسدود شده ایران آزاد شود.
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15632" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15631">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏زنده‌یاد⁧ مانوک خدابخشیان  ⁩: چه کسی می‌خوهد این رژیم را براندازی کند؟ چه کسی می‌خواهد پایه‌های این رژیم را اره کند؟
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/15631" target="_blank">📅 23:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15630">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15630" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15629">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شبکه 14 اسرائیل که به نتانیاهو نزدیکه، مدعی شده ایران از یک «سلاح الکترومغناطیسی با فرکانس پایین» برای تأثیر گذاشتن روی تصمیم‌های ترامپ استفاده می‌کنه!   می‌دانم این حرف طوری به نظر می‌رسد که انگار از یک فیلم علمی‌تخیلی آمده، اما واقعاً وجود دارد و همین حالا…</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15629" target="_blank">📅 22:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15628">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به کانال ۱۴ درباره لبنان:
امشب دوباره با ارتش اطمینان حاصل خواهیم کرد که دستورالعمل‌های کابینه برای هر مبارز روشن شده است
ارتش مجاز است هر تروریستی که در منطقه زرد شناسایی شده است و علیه هر تهدید واضح حتی فراتر از آن، ضربه بزند.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15628" target="_blank">📅 22:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15627">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وال‌استریت ژورنال:
ترامپ این هفته با رهبران پنتاگون و پیمانکاران بزرگ دفاعی دیدار خواهد کرد تا برای سرعت بیشتر تولید موشک و مهمات فشار آورد
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15627" target="_blank">📅 22:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15626">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIPpQayr59aJGFoy1hSYORqD_RojMEGW-n4dF-iQm5PNv3rKYVfimt70HL-8JfCO96MFLHH4H_a6ah4Q-rsxj34B3ictXjHk1rTfCiKpOGqHvie8QR0fekw9dH_A16fjg9KCNhFXG9h5R_beclGe3wyfGRxywf1Gk-QQd3oDBzpQAVVT1ebc1EaGHR8kRskiK-gr2cf-GTzetS4lzTDwJHQ3dOgqjxxebFOotyGysHWVWYD4VsuRHc_C6Df3EKzo98n3Fvvy8cfEgLZnAVtKB98ERTkrUFI602GsDyh4M5Mpk5dME8tdOLp-0BtFeB54_m_tz2Zjp5B2VPYwRxhaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای ممباقر (هیئت جمهوری اسلامی) همکنون در مسقط عمان به زمین نشست.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15626" target="_blank">📅 22:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15625">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ونس معاون ترامپ لحظاتی پیش سوئیس را به مقصد آمریکا ترک کرد
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/15625" target="_blank">📅 21:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15624">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fe556e38.mp4?token=UgdcZDSciz7tl2WilB7S3MKjLzPx9pyOJPtPB2Zwq84OmtkwWEyr23x5-RqSuyTRNeBtDwN9exc7wFdoY72iBUVf8xUtAtFhPuy2bdH9k9TpJepMQb7FunhUjWv6YFkVCBrrINBlX97vL-TrhsCzbOCbBCchsiw8lEoGHwWXGbFPJHYm_0x_vfg5gSIfLI4paSmbDO57m6P9nsG3Vzhk6-9CTTolEQDFklSf-a_AUxm1k4eb8PbqUfehp0Lo9UKbhbuu1OVM-cZXgyudDk-XJdKOLVjulz1-CNyMLyWCSa_xAmTmF_mI_BK9mdK6KhSCozJbUrhkXS80IDP0URld_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fe556e38.mp4?token=UgdcZDSciz7tl2WilB7S3MKjLzPx9pyOJPtPB2Zwq84OmtkwWEyr23x5-RqSuyTRNeBtDwN9exc7wFdoY72iBUVf8xUtAtFhPuy2bdH9k9TpJepMQb7FunhUjWv6YFkVCBrrINBlX97vL-TrhsCzbOCbBCchsiw8lEoGHwWXGbFPJHYm_0x_vfg5gSIfLI4paSmbDO57m6P9nsG3Vzhk6-9CTTolEQDFklSf-a_AUxm1k4eb8PbqUfehp0Lo9UKbhbuu1OVM-cZXgyudDk-XJdKOLVjulz1-CNyMLyWCSa_xAmTmF_mI_BK9mdK6KhSCozJbUrhkXS80IDP0URld_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با تقلید از ترامپ دم توالت هواپیما
: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشاله در این گفتگوها به نتیجه نهایی می‌رسد و تا به نتیجه نرسد، رهایشان نخواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/15624" target="_blank">📅 21:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15623">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsCg-aek2uW2TtjkghVfjjiJDgZjnlbXK3fzo48lOOA6JcdDDrtWQCWpztRuWxJrHzuEGOSiT29HBFzrewbGdrS3XTlx0awH17BAaYFgCn1sWXalKRvIXWaXsigu6JIOpjQfiIgbjzHuP6xF2RceaR7ydqc7gqdz2A93JzAN5-rEEx88fQt2B1LUXkcXUzabWo59ctH0OEwSYWnQuTS8wSZe0haeOOFjBy-XHi4mZM4nb8jYp93S7jQAAvb9iZV6FICemuMNAmy6SHe5JFOnDmcyyi7rJr9A40OJSnnHHxURNF-DoaGzD6PHdDzh3qUz4p7ghdG-Sm53s_2DrIHXug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : همه کاملاً آگاه هستند که ایران برای تضمین «صداقت هسته‌ای» در آینده، با بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد. رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15623" target="_blank">📅 20:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15622">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شبکه 14 اسرائیل که به نتانیاهو نزدیکه، مدعی شده ایران از یک «سلاح الکترومغناطیسی با فرکانس پایین» برای تأثیر گذاشتن روی تصمیم‌های ترامپ استفاده می‌کنه!
می‌دانم این حرف طوری به نظر می‌رسد که انگار از یک فیلم علمی‌تخیلی آمده، اما واقعاً وجود دارد و همین حالا هم در حال استفاده است , این امواج رو داخل مغز ترامپ فرستادن. رفتار رئیس‌جمهور به‌وضوح تغییر کرده. چیزی شبیه تله‌پاتیه، اما از نوع الکترومغناطیسی.
روسیه این فناوری رو داره، چین هم داره و ایران هم بهش دست پیدا کرده.
باور کنید یا نه، از من خواسته‌اند این کار را انجام دهم و من هم روی آن کار می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/15622" target="_blank">📅 20:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15621">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مرندی: ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15621" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15620">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شاهزاده رضا پهلوی در اکس : در حالی که فیفا تلاش می‌کند پرچم شیر و خورشید را از ورزشگاه‌ها دور نگه دارد، هزاران ایرانی در ورزشگاه سوفای ثابت کردند که نماد واقعی ایران را نمی‌توان ممنوع کرد.
دفتر شاهزاده پهلوی افزود صدای مخالفان جمهوری اسلامی در جام جهانی بیش از هر زمان دیگری شنیده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/15620" target="_blank">📅 18:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15619">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تکذیب تعهد جدید هسته‌ای از سوی بقائی
سخنگوی وزارت امور خارجه:
تعامل ایران با آژانس بین‌المللی انرژی اتمی طبق روال جاری و منطبق با مصوبات قانونی ادامه می‌یابد.
بنا بر اعلام منابع مطلع، در مذاکرات ۱۸ ساعته دیروز در سوئیس، هیچ مذاکره‌ای درباره پرونده هسته‌ای انجام نشده و تعهد جدیدی از سوی ایران پذیرفته نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/15619" target="_blank">📅 18:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15618">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">طبق اخبار درز کرده این معافیت تحریمی نفت ایران در ازای بازرسی آژانس از تأسیسات هسته‌ای ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15618" target="_blank">📅 18:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15617">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نتانیاهو: تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/15617" target="_blank">📅 17:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15616">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده رسماً معافیت تحریم ۶۰ روزه‌ای برای نفت، محصولات پتروشیمی و گاز ایران صادر کرده است
این معافیت اکنون تا ۲۱ اوت معتبر است و ممکن است تا زمانی که مذاکرات ادامه دارد و توافق نهایی حاصل شود، تمدید شود.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15616" target="_blank">📅 17:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15615">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7JLj749kTppUvllWoKZ7LgeIRwrvj1GW8uVQ_hYxR-aOL99ZwgdLfmAud6RqtMBkU9S7G4LTPseRs7704V89HMbX6g9EQkDRA_xrd5umL2GnTqo9PlLJT5yy8I2AoCztZWbeSsf5DQBZwnEqfy7YQNgfWxzwd4MiFnxNFldPENoFD4ravl6e90tc_DVeBVQXYMFitY9trEUv_8edXd05FI1PGVTmVwoOnoULdqIcvrNwM01yo25AJQVxlX2oSaeOpoL54Gtj2L0HjgPRgRlXc0RvZZZbHAD47lQNqv9WG5fGlVNLZasVt7LGi_5kZZO3H7mbt1uuTFJ3bta2bxYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بمباران توپخانه اسرائیل منطقه المشعع منصوری و منطقه بیوت السیاد در جنوب لبنان را هدف قرار داده است.‌‌
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/15615" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15614">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فاکس نیوز: ایران متعهد شده است که به آژانس بین المللی انرژی اتمی و بازرسانش اجازه دهد تا به ایران بازگردند تا بر روی مکان یابی و برچیدن تاسیسات هسته ای کلیدی کار کنند.
معاون رئیس جمهور ونس توانست به چارچوبی دست یابد که از بودجه مسدود شده ایران برای خرید محصولات کشاورزی آمریکا برای ایران استفاده کند و این محصولات شامل سویا، ذرت و گندم آمریکایی است.
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/15614" target="_blank">📅 17:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15613">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">العربیه:وزارت خزانه‌داری آمریکا مجوز عمومی‌ای صادر کرد که اجازه می‌دهد واردات نفت خام ایران به مدت دو ماه انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/15613" target="_blank">📅 16:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15612">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">طوفان در راه تهران
سازمان مدیریت بحران: مناطق نیمهٔ جنوبی، غربی، مرکزی و ارتفاعات تهران در معرض وزش بادهای شدید و گاهی بسیار شدید قرار دارند و احتمال وقوع طوفان در این مناطق از اواخر امروز تا روز پنجشنبه بسیار زیاد است.
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15612" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15611">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72fc6efcdb.mp4?token=jOJ1UcM_i6WEBjxZeLzVp8nQH7r-s4GW72_XB_YcIDmfKkaDuSZpflf1OnYJ1t0buBcLmhZbTZr_eO2_X_c1OFeeStqAFLmJ8pTvqrFQBv8lhrkrQv2h0HBHeI8QhF-g37AZ-BKr11DkUFvj9-4yx-NOXXpP52lT9_7FXBgf9YxegskhJpacXL4UgoscmGvcjntZr3p5zLhLOh3108vuIhkwYP1VKDsFOGvLrc1ImQtjebA4OsncqqwaSyAfuDdUGbjf5AfDG4YzN3mkQm1PXP4pyB7CR3674pGEwNALT1T2dhgZbpZ4IjdB8r31UPfHvLl9ZwlDw_Lw5tbP7MAIPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72fc6efcdb.mp4?token=jOJ1UcM_i6WEBjxZeLzVp8nQH7r-s4GW72_XB_YcIDmfKkaDuSZpflf1OnYJ1t0buBcLmhZbTZr_eO2_X_c1OFeeStqAFLmJ8pTvqrFQBv8lhrkrQv2h0HBHeI8QhF-g37AZ-BKr11DkUFvj9-4yx-NOXXpP52lT9_7FXBgf9YxegskhJpacXL4UgoscmGvcjntZr3p5zLhLOh3108vuIhkwYP1VKDsFOGvLrc1ImQtjebA4OsncqqwaSyAfuDdUGbjf5AfDG4YzN3mkQm1PXP4pyB7CR3674pGEwNALT1T2dhgZbpZ4IjdB8r31UPfHvLl9ZwlDw_Lw5tbP7MAIPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک قابل مشاهده در تنگه هرمز نشان می‌دهد که حداقل ۲۴ کشتی در ۲۴ ساعت گذشته عبور کرده‌اند که همه آنها به جز یک کشتی با استفاده از طرح تفکیک ترافیک ایران قابل مشاهده بودند. به احتمال زیاد تعداد عبور و مرورها بیشتر از آنچه نشان داده شده است ، زیرا بعضی کشتی‌ها سیستم شناسایی خودکار خود را برای عبور خاموش  می کنند
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/15611" target="_blank">📅 16:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15610">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">معاون رئیس جمهور آمریکا ونس: ایران با ورود بازرسان هسته‌ای در این هفته موافقت کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15610" target="_blank">📅 16:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15609">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd2-IoI0umxRxVWkHRCzzyNy84YbuQCQdQibcWkjzcCoP2ee7TQaaYicrobkAgA3JXPJhkwhSehe7UtNdqRdmPw595RdBjnEX-FuQDkbw7J0EsU1YjQyXx3QbO0TDhcgk5knlHqrsTDFITfmehTD7AxTzK7ysS7t14C8r8O6OBe7wpOb1xHOAlNQU0uJgOucM7Ov0RDfVzxt_uxW93U3ltxEob_48pdDVgoqJO1xKAiYNPpBVQRgHrbGgIdWsz8ZbDdhjLB20AJbR5M8N4rFrpoQPEG7_YYtc3xobyo8kyiGPKcT9GCYOUZ4Jgs_VEiQDqJqfsxITS7Sn1udpOV1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : یا هر روز به جون هم میفتیم و به هم فحش میدیم و جونیمون میره یا همه باهم متحد میشیم و این وضعیت رو تموم میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/15609" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15608">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d6b1d15d.mp4?token=ufVAuKFlSh-6qXlV-C7Wz7UnbhI1s07RPioct3XzhjOty7IBihJ_BIob65wUwai0BDJv2N4cp3_D6xePrnnRPfJg1rNbnaq9eb_UWMZWaMjY6Uuy8NGL02p9D03RUkwyY5OKqd_LPrer9oYekrfphAgi3bFIXu0UzvACDL9uP9bTbI_TsscU1XkzjES2W2KaRlgghp-Nkm_cT3g4-N2Db8nyHEYcQW_UjzZX4jFrG7ulhuzChGXMpBnnbN2P00SVFag_-AZoNdfwOfP8MIeZag0VGIEVLOI_Mv2pc-rFk8cIWtHHAJQKMJjt8KRAg7FHJHtaHpvKT969lPMZdQroEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d6b1d15d.mp4?token=ufVAuKFlSh-6qXlV-C7Wz7UnbhI1s07RPioct3XzhjOty7IBihJ_BIob65wUwai0BDJv2N4cp3_D6xePrnnRPfJg1rNbnaq9eb_UWMZWaMjY6Uuy8NGL02p9D03RUkwyY5OKqd_LPrer9oYekrfphAgi3bFIXu0UzvACDL9uP9bTbI_TsscU1XkzjES2W2KaRlgghp-Nkm_cT3g4-N2Db8nyHEYcQW_UjzZX4jFrG7ulhuzChGXMpBnnbN2P00SVFag_-AZoNdfwOfP8MIeZag0VGIEVLOI_Mv2pc-rFk8cIWtHHAJQKMJjt8KRAg7FHJHtaHpvKT969lPMZdQroEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی : یا در مجلس را باز می کنند یا جلوی مجلس جلسه برگزار می کنیم مردمم ببینند
@withyashar
🤣</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/15608" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15607">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوحه: دیدار وزرای خارجه قطر و فرانسه در سوئیس با محوریت مذاکرات ایران و آمریکا
هدف از این گفت‌وگوها دستیابی به راهکار‌هایی برای حل مسائل باقی مانده است
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/15607" target="_blank">📅 15:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15606">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جی دی ونس: معامله نهایی، خانه است. ما فونداسیون را بنا نهادیم. ما خانه را نساخته‌ایم، اما فونداسیون موفقی بنا نهادیم. @withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/15606" target="_blank">📅 15:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15605">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ:
اگر پول‌های بلوکه شده ایران رو هم بخوایم آزاد کنیم شرایط رو جوری فراهم میکنیم که کشاورزان و تولید کننده‌های داخلی آمریکا سود کنند و مواد خریداری شده به دست مردم ایران برسه نه تروریست‌ها!
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15605" target="_blank">📅 15:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15604">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/15604" target="_blank">📅 15:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15603">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جی دی ونس: معامله نهایی، خانه است. ما فونداسیون را بنا نهادیم. ما خانه را نساخته‌ایم، اما فونداسیون موفقی بنا نهادیم.
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/15603" target="_blank">📅 15:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15602">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس جمهوری ایالات متحده: به آمریکا بازمی‌گردم، اما تیم‌های فنی به کار خود در سوئیس ادامه خواهند داد. پایه‌های لازم برای دستیابی به یک توافق نهایی با ایران را بنا کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/15602" target="_blank">📅 15:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15601">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عضو کمیسیون اقتصادی مجلس :
ملی، صادرات، تجارت و توسعه صادرات که هک شده بودن تا دو هفته دیگه وصل میشن
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15601" target="_blank">📅 15:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15600">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ونس دوباره تهدید کرد: اگر صلح در منطقه اتفاق نیفتد رئیس جمهور ترامپ همچنان گزینه‌های زیادی در اختیار دارد
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/15600" target="_blank">📅 15:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15599">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ونس: به ایرانی‌ها گفتیم که وقتی شما حرف‌های بیخود می‌زنید نمی‌توانید انتظار داشته باشید که رئیس‌جمهور آمریکا پاسخی ندهد
👨‍💻
ایرانی‌ها تهدید کردند که مذاکره را ترک می‌کنند ولی نرفتند و تیم فنی آنها در حال حاضر در حال کار هستند
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/15599" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15598">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جولانی : در صورت دستور ترامپ، ده ها هزار نیرو رزمی متخصص جنگ شهری برای نابودی کامل حزب الله وارد لبنان خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/15598" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15597">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ونس: «باید سازوکاری وجود داشته باشد که اگر حزب‌الله شلیک کرد یا اسرائیل پاسخ داد، ما با هم صحبت کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/15597" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15596">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">معاون رئیس جمهور آمریکا ونس: ایران با ورود بازرسان هسته‌ای در این هفته موافقت کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/15596" target="_blank">📅 14:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15595">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر به الجزیره گفتند: این یادداشت تفاهم نیازمند تلاش‌های زیادی با شرکای ما در پاکستان، با حمایت منطقه‌ای، بود.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/15595" target="_blank">📅 14:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15594">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جی دی ونس همکنون در سوئیس :  دیروز روز خیلی خیلی خوبی بود.  ما پیشرفت خیلی خوبی داشتیم.  ما دقیقاً کاری را که می‌خواستیم انجام دهیم، انجام دادیم. @withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/15594" target="_blank">📅 14:44 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
