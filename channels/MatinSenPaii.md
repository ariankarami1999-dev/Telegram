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
<img src="https://cdn1.telesco.pe/file/Ltdyy2ZgusoLFGEZhRQ2z7CVfGPdYrasGDbyWXmLcDLQfLdX_upJaHVdYGAKDSUS3tkNm2Z3MuYbOcsKwp8z4hMsF5BYpWK3WjTkG6nHNPIk4Aph2KT-ClhlUh7n3aZdQnU42XUQP_xRr2HMvVkzIcylvd8scl3DBGgcAEEMChIcL_30RftDia17En48aCmLv0QSbEoVTf5Zs2sZRGauFENBd1F7cHrtzLJh0IkrjOgGEN3ZFZaa3FUCR5H15INZgBN0PhZs9g_HEfg7A--NidH1KUyy3ITHHHJd-ETXhz_0GaQQDHBdHrYn5nZiomU19ERTam6dQxvZD1RGB9pKSA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 159K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-3562">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خب انگار مشکل از BPB بودش. چون الان edge tunnel بالا آوردم کار کرد اما bpb دوتا بالا آوردم روش کار نکرد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/MatinSenPaii/3562" target="_blank">📅 16:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3561">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امروز به دوتا نتیجه‌ی مهم رسیدم:
1- روی یه سری از اپراتورها، اسکنر نتایج فیک میده
2- پنل BPB ممکنه از اول تا آخرش ستاپش درست باشه، اما در نهایت کانفیگا کار نکنن. که دارم سر در میارم علتش چیه. فرای از اپراتور این شکلیه. یعنی با یه vpn دیگه هم ازشون پینگ میگیرم پینگ ندارن با اینکه tcping میدن</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/3561" target="_blank">📅 16:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3560">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">همچنان از
@Whitedns_Installer_bot
می‌تونید کانفیگ رایگان دریافت کنید. تا الان 21 هزار نفر دریافت کردن دیروز و حدود 5000 نفر، حجمشون رو تموم کردن(که امروز دوباره شارژ میشه). به زودی مقدار حجم روزانه هم افزایش پیدا می‌کنه</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/3560" target="_blank">📅 13:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3559">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یه آموزش کوچولو داریم امروز</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3559" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3555">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ldNsEEq2QXAOO9lCUqqtzZNSb-1qw_LlqOfKrRxDHY6d1K-Gvjhfvu55K-0UcUs84FxPT0g0s2mQEhGGW-Ebg9e7wkxdqRZcugJg6sYUsdmderHyvLqFQtoXtQ_JYZ6DJOAozXRWPnNd1JirhxtVK_1lH4GZCZc1EcD1wbwMQve05j1HFyRmiaWazIZ2eFVwCxrYo3wL3D1324jLx8VYhV0Mrzzlnf97C7tROMT46rx6pIMX7KZCyBmX17w217kgVer4rlFuMK9zo3tQeMFdqaNQd105KJbRjLzA4pZk_Vg2sFsJ5SqviG4wdrqEpmxkR_ob4yyBC2XLH4jkyEMtEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X6mpvImBzMqCSFFO4YU6sRgJT4mQ7mPRWaq8cOMmI4cnjrOvkkDJlcL28F3skGOWYZ7age6ATFbDZAmaHpI_Mo6eJNxg79oY1GjtlMvG7NqMxPiCo56lYPggt7639meXDWRNPm7Zw8rVY_4D6BroEBIHbyiqTmZPOlUO104NTedwmJEj_Uo319XL4Zl9ZgZBKYyfMvU6mQAFtNeVPFWet_uLzulnI2N013gpVAfevKdsSRlUcl_APnGZwW3D2EPLZ0gwNnRICKOcUgtwzBeSIXvk70IM-u1-iqfwz4GgdGJ0e4RzENrPg7iT19Pl0VFPgmqZ0JY39th7pnZHDxCrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jAr6TyBFlZqwXKljl862hurCHTQXwY6fcCLE044UIQ2RxdTENoOAvd1cS13rPD-b02aMPJG0USHQQieLtGX2NAwi_sAcbRkqAG1X6jv_J4Zb6BbLE-8l-_QK3eMELhbYg4RvK00kOB0b-CkSDiMYv-jB3Tr-nWAePn0bvTPG70y-Qua837W9gSm-BItKbJcbwDQGBlbrbEaCORq1Dp8HLuqliTT9WWP_ciV2-nkQa9qQ96kq3L59NOnkNNm43c2_YkPlROBP2uHP24H0drTqafiXsads_3tjpKm4KF1FrVg2puQiB0ekJRs9jox915xjAko-FRSEU0quZrnkwxYViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZBh2PGIh63nHQIxFnreYHTtBlcyZDukzOI-LmAHlVed_ythbRIO-KqNjlLnF-R2GKTN8FFo94Y3N4slrdOtcYEIZy-4pWu8yfbbATisjccRoVoPvaoZr0gDAO0j0ZwGJ_hkBE6DEwbz6FqHOIlOvKM-JFiCyrx6gjVktCXvLCR9GNBgh8uv9U0Lwbdk4WofYlOlpE46BzHYsNIZd07ZR0XhqJ8xM4RNYOuuT4pBvF2UGej7IaeHs00icGuhj_FeyjwomiSibsPHHC2FQPLvxdbGxNDus-v1DbpVksIyArWJ2_iG3rerUv-R3I6pYtrGxf8n2nxYpSVsKeDDVYGfn-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاری که خودم کردم:
1- صد هزارتا زدم بره برای اسکن با ورژن جدید سنپای‌اسکنر. با 200 تا worker کلا 10 دقیقه طول کشید
2- برای من 4 تا آیپی پیدا کرد
3- آیپی‌ها رو با این پروژه‌:
https://t.me/MatinSenPaii/3554
بازنویسی کردم روی کانفیگ پنل BPB(هرچند خودش داره اما این شکلی راحتتره)
(صفر تا صد ساخت BPB رایگان)
4- کپی پیست به v2rayN و ادامه ماجرا
سرعت آپلودا هم اوکی شده الان راحت اندازه دانلودم میگیرم</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3555" target="_blank">📅 09:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3554">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اشکالاتی که فرموده بودید رفع شد. پروژه با هوش مصنوعی نوشته شده و تمرکز بر سادگی و استفاده‌ی راحت مردمه. اگر اشکالی دارید توی استفاده باهاش بفرمایید و issue ثبت کنید یا اگر خواستید، pr بزنید و مشارکت کنید.
باز هم عرض میکنم خدمتتون که این اولین تجربه‌ی من از اوپن سورس هست و اگر اشکالی به وجود اومد در آینده، پیشاپیش عذرخواهی می‌کنم. سعی می‌کنم که یاد بگیرم و نیاز فعلی رو خوب پوشش بدم و همینطور پروژه رو هم در بهترین حالت ممکن maintain کنم</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3554" target="_blank">📅 04:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3547">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3547" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/3547" target="_blank">📅 03:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pLNb6k48lowYV7UFSU34eQVmK6--UcbIrg1Ra0JS1zLtQoFJ9VoYv-Pbc5Gq5ISRh1PiTVZhlEk4N8ldAHX7P8jz0GikeJang3xAavBob1exo2nGjfamyCFSRab_ehpJdTssvOltUIaOcr4fZNvtifEXZ6VWCTWy_P5-qUbQ01dqhUPrb7eNM6vBmXF_WEWXVKNmlTXd_jLtjk2FH_m2Oo053MnqG6dOdPzrHap4HHEsOBgrqrOR7aErF7eR37PyQqp7rBD-rwr6AICGBxNOoi2NWgKgdcJfSiKnuHIARWq50TWO1UPT-mFvln8-2LJNjw1B6YHamwhtsowvjx9mBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AiW8dC63EJghEpRrUVTeOPxn7_u6igOGt2KfsyqSE-j1Zl7NoDFDkOAFacXOcM4m3pstqFvzluRZhacw0N5i3vhkFVJxnQhkbFxYGZWXk1jVBitFMvnGUxG2yRKgCbn4VpuXp_ZYyv42b5cTdLL-qPxDm4N0TyyW3K1_QwiT4ZN4XsQBes8EdjnXu-cZCdnf27xKpfrUWyoYD9zZEENkc9PMTdwgTgr2Jd_tu-bZYL81q0TbpC6w_jFDa7nYyEJ_yFLtc9KgQiMs2aI2GIHou3BhMVPAQU4V42MkogpGPTwuFgTm5p6lM6GFgcVg-9vquB6XY-eUP67xoX2p2YM2qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی آپدیت جدید اسکنر، آیپی‌ای که Healthy هست واقعا بهتون پینگ میده!
همینطور با زدن دکمه‌ی c روی کیبوردتون توی تست لایو، میتونید این آیپی‌ها رو کپی کنید.
یک سری دوستان عزیز متخصص هم برای تست بهتر، روی پروژه pr زدن که دستشون درد نکنه واقعا.
تا دقایقی دیگه منتشر می‌کنم
همینطور که توی تصویر می‌بینید، یک آیپی به من healthy داده شده و همون داره واسم کار می‌کنه با سرعت عالی</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3545" target="_blank">📅 03:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3543">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D7vq0Tan6BEEi37ydFSBIH0yLMxZ_fUUjqYGD7PIp_rFs43-PR4-_L6ElAqrmmEuLQWKy8NItBUcCGDvhCKihiL0vCE-PH-pZVQzBPU8Duu3M2Sj-TqADn3EPUSCGDa8ld0rv2kMPjrnVgGM64bEHmpHR1B-28u6ktaWfrjK8oApwTIdzILt6XbGBGrpbb5X_x3xo_mzfoYvdSfhMf3AMNtFDGrxP1ZvlDo0Nv20STBQAsWL21Oms2DhfTmhwMRnhDAli-aa49Tbebow30asi02GmkqDD8ug2y_Yb6X-EbaBNGp0aJhl4ktJ8CROojmNAPv5ruy_FAq63ibNat5ALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنویسی یک کانفیگ تکراری با آیپی تمیز‌های متفاوت!
با این پروژه‌ی رسول عزیز می‌تونید این کار رو به سادگی انجام بدید:
https://github.com/seramo/v2ray-config-modifier/
این هم نسخه تحت وب ساده‌اش بدون نیاز به نصب:
https://seramo.github.io/v2ray-config-modifier/
برای حمایت از سازنده، روی گیتهاب بهش استار بدید اگر دوست داشتید</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/3543" target="_blank">📅 03:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3542">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8NoSdf7pdyCImavKubMs8c4MGNIjEFN3-AJdzfvQkCWCUPTwg1mwf2pAXAO9VdhSo2kTY8Us3bLwPPpNlrbo8ZxOj9ApPUW3pMZpz_HlRoMnlF8vvwvE5S5BiZxrcRWcPAvLuSgFmMsoXaAavWZcy1B0FV-7beRLEjkO6TaRMUpIC2wj92_A0QPkCxFNsYNP6zl6ie9V_7gC6VGvkfFRsHMKOkU6IENXLho9MFIinYVVl8xpPxtrGipT-5MGKD21WvDRRv60WzwKrpho81fFu2ttqbUaCbPA00STdL8_g2yG-mJGp1MFnn2TdzpsIVfsbDyQZXAT6IfSByxVC8ouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3542" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3541">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3541" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3540">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3540" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3539">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خیلی باگ‌ها پروژه داره و تا الان نزدیک به ۱۰ تا issue ثبت شده و دوتا pull request
دمتون گرم. همه رو اوکیش می‌کنم تا صبح
❤️</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3539" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3538">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RyclPpPZXl22Uwqqrff3WGzUKTeJDFMTEztFosVnQ7SNTVwS5iiEn9XgE22kWmaSp11j-vWx68ByrRIf3Jfqom3FHOgUJC1dZ5oWtHiaMBI9c7DyGDmyxVs4DG1u8XTXYHaYsNJU3qHz6f9Y8J3Ab6H6OSyD1-0FnAQ106ydZpQmKJu1izjzVMfe16LohQd9FwKki1ZsMC5AXciTdtT_juLZtGtNTkWV2I9OdMlSCMepsE0TTQYRxhFqT8GDTpwycQj5jGPYtaglgfwsKBjiVCWwtzN9oyH9iDzrF3jihnnyS8c4Sl9U3-8vsrm61h4e_GlwlSzfKKSBRtSxxPJVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/3538" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3537">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/3537" target="_blank">📅 23:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3536">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vyI5ZWQWpFWpSyvAbPBGCtpY0xB8XQfLBkToGAK0HCc3TS4sOmpFTd5WdZBgSS8tuAxWXRIJUJzv7ZcSLlYaRNbH02OH7PP94xcyhxrpzpI2jJuU9zmCbBcMbu1BGN4yjSaEkanD020xHuJ7lhOyvRigaHjLIPi-0HYZQ5-WTjmTW8Oaj4CRMni06tHUe4JUltO7yLYYTjz0zVfgu3id__m7xAKUrNvhN2TIHrNEw3SO0yycYSjJFmK45Zo_ppHXoNQ4rrfEPNhpoc8LKs6E146QQFbWuTT9mpgoTW2aVj-F7fdi__Or1PYwH6Qskh4-iQUJ58oOVeF50Q3Mm1HAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه
و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3536" target="_blank">📅 22:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3535">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iaSGrtiG2VJB4oTAKxvNucLVA_KZE5obVP2DcO88Cfe690sQTM3d_ur-YklAMHOUbM5d9vJ2iOpvPA8-DYLijyb-HxEa_-aIiGDD2xMV5mNPt93WhkPKP5viPLRs5Y-nBOU2dpAOqAJ383rDiYjwFCdt_dgbV6M9P-t8j10HeVNuqE7UrJONf5b_6oL3TDEMa2HNEHGp3PNZl1WtxD3MSxCT5rsmQhy7gLCderVeTX6HKATimJlUIwhSlakOqsWdTA92x1AWRxRnR8GdX6iglpzhnmjVWVWdgLnkwPIrTyt8cPdQpK32EViEkGgpRGyKTXo6Xk7NuqHDeoeod_QJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌ها کاملا رندوم اسکن می‌شن. برای همین باید تعداد رو خیلی بالاتر در نظر بگیرید. حداقل ۱۰۰ هزار</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3535" target="_blank">📅 22:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3534">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این اولین تجربه‌ی واقعی من از اوپن سورسه پس اگر کم و کاستی داره، ببخشید. صرفا این پروژه رو زدم که نیاز خودم رو برطرف کنه اما دوست داشتم پابلیک باشه و یه پایه‌ای باشه که از ایراد‌هایی که روش گرفته میشه، دانش برنامه‌نویسی و شبکه‌ام رو هم ارتقا بدم
❤️
امیدوارم که این پروژه‌ی کوچولو به دردتون بخوره
به شخصه از اسکنرهای پیچیده‌ای که هزارتا مقدار داره داخلش و نه میشه به عموم توضیح داد نه میشه به راحتی ازشون استفاده کرد، خسته شدم. نیاز داشتم یه اسکنر داشته باشم که به صورت رندوم، به تعداد دلخواه آیپی اسکن کنه و تست کارکرد بگیره ازشون</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3534" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3527">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای نسخه‌ها:
🪟
ویندوز (Windows)
senpaiscanner-windows-amd64.exe
مناسب برای:
سیستم‌های ویندوزی ۶۴ بیتی (بیشتر لپ‌تاپ‌ها و کامپیوترهای امروزی با پردازنده‌های Intel یا AMD).
senpaiscanner-windows-336.exe
(یا همان
windows-386.exe
)
مناسب برای:
سیستم‌های ویندوزی قدیمی ۳۲ بیتی.
🍏
مک‌بوک / اپل (macOS / Darwin)
senpaiscanner-darwin-arm64
مناسب برای:
مک‌بوک‌ها و آی‌مک‌های جدید با تراشه‌های اختصاصی اپل (
M1, M2, M3
و جدیدتر).
senpaiscanner-darwin-amd64
مناسب برای:
مک‌بوک‌ها و کامپیوترهای قدیمی‌تر اپل که پردازنده
Intel
دارند.
🐧
لینوکس (Linux)
senpaiscanner-linux-amd64
مناسب برای:
توزیع‌های لینوکس ۶۴ بیتی روی کامپیوترها و سرورهای استاندارد (Intel/AMD).
senpaiscanner-linux-arm64
مناسب برای:
مینی‌کامپیوترها (مثل رزبری پای ۴ و ۵)، سرورهای ابری ARM، یا لینوکس‌های نصب‌شده روی مک‌های M1/M2.
senpaiscanner-linux-386
مناسب برای:
سیستم‌ها یا سرورهای بسیار قدیمی لینوکس با ساختار ۳۲ بیتی.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3527" target="_blank">📅 21:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3526">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/er0bpPhpvRvF8B_yfDDq-t_Ys3_kJRLueAZwfFXfEUSSMUJ2ACBWwOIb26WvdMlfIMzOS07oR9ie9wFMy4Qnx1yALjGO7wlDAVAAJJ4Zm1jrCY8TEXRJTv2aSsNOlc9i9z-SikGmUuKoOBqcaSN1vbrGZR2-n7lBj4pnJwNezBKQ4NHNIrpjCNahulsCPgTDdKScoVKElqxW4otv82SFfsINtsUhRKSh0BZoNgBP2lzGfbHxPBtEVHKYd7La_vekHzbrK5dXh0zq1yThLkYNicADsvzwTx4qvM4TU0j1HDP-M04E4R1BoScLfSQqOusJmpp0UJNJmkWVo-OG13XS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3526" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3524">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZSUKS77iRdsBZA5GE5WqCazvJKzFdk8wCyedC1y8h_ko2jpmDV-2whCTRaLiNfxWs8OJnX7ieOHpRa8w2tGwsBi0p1MGpP2IyBE3Mz4_Q-dctBTjxu0jcnk-9ej1FVrrZyZ-04ygaPL-lSJ6D_z1VL2qbHG-C_LwsP9LOYA-5Yr1Z3LxDRM_9vQp3w97-lwn5J8WAR1hRT0Z-xgNQdzFq-fxHKhJ-_7m0y1IBSr-aTOgxekCHFGMZy7YSC6n6_HpqgMKYupAK_x8YtCSLYSBee_0CSqukv28hBU_keRd3E9Ui9oBiKGupiQCA00gIzcbWJiQtTNxyxfx4J9vm2ptSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cdgcEKhfaxJAT29g5ADzrkTXwNPZxkawaMrWzYaEBE1wHF6mpSMli_BlghE8sVC3CHwqGKYE13lBrkNbOy1ZCwDtSFRxfpTkHKOLErpCAl4iT8RwWN5cCe0Vr7Q_Umxv9kBuZdtVpPYm3CDGWYsnOqnIysPC4J88-apaxew5l6IZRkd4_988zurokSoxWRbcyqEEFipu9elNeWT3XVRsv8cLe1kkF7HAHbxUmb34J6PAxmdbNggOL99ajJi9u8ppBJ5Uam2xMSSa7ImW3DBPycLNXsLzgXLoDkWpZUUFbVDNujy_gCPHO9ZZ9AHIdSgniEseT15CupK4sDmgHN6bJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین آیپی ای که اسکنر پیدا کرد و داره کار میکنه
مبارکه</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/3524" target="_blank">📅 20:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3523">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3523" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3522">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u1kKKQz4tB4ICp8uJzBJSDbQ-gEzSriQaEyINfApUdfWsmSQtwEPQfdTDL-1EOFHY-RMClFk2gu1z2mz5GVpfZug72UslzFdhsGAtbGOCuZrWBe1rUbZsKgYqNoPTQW7ZuXh3QDtbWllz6CJxYqQbDX6ASDZP-IJkGVdggaonGo4kYPol3Isu5ExT3WWaEtvG032mQqXr7Rhv1lgBQjFNJhYgPXqFS73_fL2_QHck5uD5X3MGiev72-14Ad8MLm5kGO2PSPu0N9iyTLsezdO7_1W2zJuA81mbCmU8NTxWpWNyCUZ87uf1GNVBeoksoG7MN8Bu_OGN84z98CF8ydEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3522" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3521">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t5DpA3id-6Fkad_NpN1YB_9ao0ImsO23PKCL87ZUsFontkHJy75IszPdaSXSiIHR-MklrtnSCb0y3Ebjb6Bw2_VIIYE0P65h9vzETKtB5SluTg_eRQZhEdJoRM7mT6KFGmlcPYKlOqM21Q-iZSf4Awxo6d4D_K6SeRrIwd9UPLBy5zneeLE-k0oHHNS7sphdclsKTUifylMxA4jPGGZocj4EUYK4YiKobMFuGzlLqNa801EgRJb9UU6Z7Q7gR2BrKH_ON3iIeAdRAX-Ulf2vcLAeiNAorxLws_LKfhzkx9042lFwclobbF2T4T2UnppcmDngL1qWIZmnJhyI39t-og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3521" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3520">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آیپی تمیز مخابرات
69.84.182.49</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3520" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3515" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/3515" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dGJ6kh_FdtwRPcCaVOr2y0lDDgtAh8rp4HoRqm1r5EaILV4DzgqtyBhcpdQRzRTNVmBXjp7ZGzsM7xRevDNnCyhhIbJvwZGt_mBNTP4zdOvTQxXHY2nM8l56EE4V7Pwh3659IGRcSvVqRPn5MQ_URre-Xs6JzmACqafk6bRDd9f9TRla6mFxJDmoizCBRZqASDAIgE677zhhPX939OXmNGm5bmLemo5GnzcrtE0kGRsN8YQRs4_COlVfP315bqw7eAyBtLztdoDVHQ__5ypxnewm9IY3gJH8tvZIXWZxmEXjvqoIsFUYYR5LF8OO52PrCfqURExWQ2fe302tf8CzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZsPgflbiFAQYknAsfYwjak3NfVoTvTkOqb1Av99uYrU_wuukxim9u7XyJQLhtBL3eU8LE1pCsezEU3xB5jgihJQdyQ_I8aRrsozsMapjCrKpg5YD77jkd0QRCbkkfAc0OzVsGyJ0ohYl4EqOCk5RHc1KVqn0lSotUzZOH-kZ54K6uOLz2eZLdZfLdi6znWBp748vjw8d7PQtMBElrpJpFBEANRJJKB-_n3fAF0RGX6GCLa5AlvRF5vr2eda-oy8Pwx60CoYpZWQ_-So5fiTO_8XBUOR16dLV_1_E1oJXGhFkJU30Dcl7Tci4R0kEUD97_-JkGV-jtDM8XxFdNoUUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AL8ciQE9dS3mk7FmsgQ-LoOKaWhwNz_5vog7stxUTDzJcJ2nDHtQbd9a8m5gZRwrU2kA9Hdvovq2iKIQO0oFKQr9RWw9BS0pR3afCq-qoHTtjU6G8lXeXgTrVkCiDLOxN88BjfdEa119hx1xzAr3WR0EMXvYsb7BMHaZEi01QwPm7IlOwgc2sg4DSAegWZ5CZQVExhKx6O0bTtkPrpc1y-vBZfgEaUTYoK211JBsMkmEJ3J1kP4pT7FDnjIFfaDD9_RlAvKtmje6ifOrTNsbPEJDAzoXrKF65savif8RJLNiEU_ogOXcsPns8xWnpvrM-s9-J3ha8OFZpodlxS1wqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aLM0ZvrfrzsfOP6l_ayOsoGLp5WXUICk6Hjxezv74GaecRk89SlaM3wMQ8OOq9B_I_z6MgJQuFT0cRqYGY-3sBJ2Es1ijDqxs-5U8YR8irOG_rOaUSdD3sbHk-ACSvajgOqvysRMfiZfSyUEV35vHqOtzRTlypedihXBGHyc0CYqxl_UR95DL_NDQOHFnX3lq3XAE9GeU7775Wj4H8fsamso_GZtjc5BHS6Ct_ATMSPN1Iy4MhMKxWyHBz-a_2y0HcEKVN56z9IVYeLh243G9e6h0g9bQGB353YElSQI0TzSojUbFsK6liHvh7kI5xlQHtIntgsp994p45gWlHI_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ALsTg3pw8RxcrkED88if6XceP3vX2fnvdHh2Wf38sRCjJrY3lzbEFGVFzAWqyEIxbXqXL4K9uNp5gREdzd6i5hiLlaQH0uC_lm6v4OhFJoAcBxkNwHt4Buw_aVK9DoUGSQZbD1GQKq047U15nWJRbOFi1Ml2Ek7aswSODApB4H24nxErTflA3BnbhrJgGyQa2XrT4vHRVXwBlsgVYWOtOZAVENUwXQ46nOBHwokO7GCOMIc8j6grhwMGIupa90C7MEpKLu5LUAyNba-v8wRnKNpL38UQlM_OGemVFgzo13jsUn6bTOR6QoEEm0JNr24f_IpqC7pG6J9FoKIWWwv9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OCNPGDqbnF_nC7kmAMb9saXn8jKxBZJP6IPIo1W7v1jVIpRb5f0K7OjT4vSqKqN6KHLnhWexYWqib8DhR8rPY6DG4aNajXsQx7dpfgZaWVb4WKWPSh1wRg-TeUzEDS7xTXLObhK5EkwfwRNmdQhkiZ4EhI3SVGjJ5MaKFZUfDEWrD6BhkRXgavAMiBmrDd3sdf_fhjQgTS3urXIW01gvYXphXGW0BYEnvYNzPbyG6oaOfaW_-IZ0eEVE_Y9s5mhNxb_TR5jfaG20p5SL-lWX5JBZ2kGIKNHai6nOJTCjv3lZc97OGUUfeIWkq10YGSPL81bJN7Ywn0B7nw3JGcao5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K0_74Uct_nF4Omq52UmHUPJXYvPwUTybb4bUNQO4NFCbnBArQcyIODVugjxCpPCYauu9u22CYgKzhaaaZQ8FwvJ8vR7m5iln0SbHAnQHLbyjBZp1eL50NnqDkvcMaP7gIsrGCRoh9FOTZwTsXortL-QxzTSMG8PpRryajSYTCcBqU30ycWUB5f1QhhT9bX1idQTNyxn14FKm4ks9KRe6fzv9i-LU6qzkwT6bMRqRtHfvrr7NOs1oBSh3FYQT18yvHioAbKTVz4Z03KvUgDataOPU_0eENvWJp7xSupTwtTPoqBOb5wHmZP2fnN6bTeWiX7xiIR1-TNnagz1-KVkzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fk51XqrfVVlxRlbJsr9_-9_p_qjKBdSgtU4DxcxRrLmEBDa5OER91XzrfOYMxMNcM5B-smLzGWdt7AOrpv7_oioHUlPsx-kM1G3LDR2eqnMNwrOrX6KlEQkSfnbs9mn7VtcSVgU1l5ybFIkQx6lt6beg5wQ1FECf95fj4AUYCE8ju68NNtZhE1ZtFYfpytyqI_URmdt8VQ8W0ISqJ9MOuBPi83EYaanNQWPK5qW2MK3Ugu4m_lSSzXNlIpppggC1rNqm_jLJxmzGMMGmG1vEFJZRLP_ygHFL8xLh9fpRxWA2MbNNHp2A-A4ye4AxWX5i9adxKz3kGhmMQt3ChxF6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jsyTHp8LHOvK_GhFbaK7zxjpWp7Tc5AavNOOEc0cB5oCb4VEhBDbA7HvFcvcNQEzkVpYHtPFUt3ZGxNkcJ7TEtqVa_8udD06tINxcaD9QAS2se0Ka9aTOlrmfqB_l9aRXJa-xreLKlUK3Yuzq-kwBeNvHyAXe6np_Az8bB2Ejl_l21aQc-hWMXuyAiKTnIu8m12MedWkNxrZRB42Lmwj7qdQRB5Q92cTDTFBy06ng3gpiwMi7DoEjq0cDE5QOPoYmw9guvN3SvWp1jesOgggLP4LJ9Ugq6_Wyjq-1HgSlpi1jcLhJm0AJewSjdXzoTfmIdtXXGF18rYF0vyRotlOxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش قدم به قدم اتصال به کانفیگ های بات
نکته
از آپدیت آخر  V2rayNG استفاده کنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3506" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3505">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVRi03r0xzrLCef5Cff4Zo2qPZBJk5-ASV8EekpDWUMAr3rjKcnMMdKJ9hyswppyBlzo8-r92yuO0dhML2Rp-qC4HXwTqVbnG4BioGDbbHVNYoEQmqDMpAHcKsGSiSFwnmvNRn1vfKoQLIHmcL6BrXJZ4aTPbYt7LmaS4N-48CxDoxa7phg_Fi5EF13hnwnmGaV-_Ag1z8UNQQQwqXgXZJryzxG0vYcNLHW731tU1_1mJHxAI_D6OMW23VzbiTZ0Lc3Z5WYKlpOjzgeyj6xlFc4FQuFGPdsiHfja5W3xgEekkrGZUIVQNlsf2meXT1kBUh7QKZrofd34hohNwEX7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/3505" target="_blank">📅 15:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان ربات تحت بار و فشار زیادیه. کمی صبر کنید پدرام داره روش کار می‌کنه یه کم دیگه مجدد واستون قرار میدم</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3504" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3502">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A5kA4K3q1J8mZEq_4KG8-DhD3CJDW2ATfyofT4lod16oBrFDxLxUVLBvdjDP5y__GirapJTqHBCKnqoUtE2H0KsuTaNj-_c5uuXdXyh38m0OYsw2-OKltaDaBYAYZhGIgFH_JHXnodLJ_AxuhvS-LCuhR4oHox4gMMRPSiJu7Lji3n88CYXIl-kY4GOTCRgmKYDGKjEGxD14i8dCaiiHF6cD7chjkYUJ08h96gxbxg1JlxchK1uGIWEA_2y52hMrh-dbfn0z9ZarkoorG1gprwQhrffvcGWs5RhMfy7JytD_VDpQz-mAruFMDEAE3UZiOTwu5UJwkCcBISEgqKZJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شما رو نمیدونم ولی این اینترنتی که الان دسترسی دارم بهش، هرچی هست بجز اینترنت.
در آستانه‌ی ۳ ماه قطعی، اختلال و نابودیِ کار و زندگی مردم، اینترنتی را «برگرداندند» که طبق مصوبه خودشان باید به وضعیت قبل از ۱۸ دی برمی‌گشت؛ یعنی دقیقاً همان دوره‌ای که فیلترینگِ گسترده، مسدودسازی IP و دامنه‌ها و قطع دسترسی به پروتکل‌هایی مثل IPv6 ،UDP و QUIC در شدیدترین حالت ممکن بود.
دنیا در این ۳ ماه جلو رفت، اما شما ما را ۶ ماه نسبت به جهان عقب‌تر بردید.
۳ ماه از عمر، جان، سرمایه، فرصت و اعتماد مردم گرفته شد؛ بدون حتی یک عذرخواهی. و حالا همان اینترنت ناقص، محدود و ازکارافتاده را دوباره تحویل داده‌اید و اسمش را «بازگشایی» گذاشته‌اید.
اینترنت واقعی یعنی دسترسی آزاد و پایدار به تمام پروتکل‌ها؛ نه نسخه‌ای دستکاری‌شده که فقط اسم اینترنت را یدک می‌کشد.
روی «طرح تبعیض آمیز اینترنت طبقاتی پرو» همه این پروتکل‌ها در دسترس بود؛ یعنی وقتی پول بیشتری می‌گرفتید، ناگهان همه‌چیز ممکن می‌شد. سؤال ساده است:
مگر امروز مردم پول اینترنت نمی‌دهند؟
دسترسی کامل به اینترنت، لطف و منت نیست؛ حداقلِ وظیفه‌ شماست.
هرکسی این توییت را می‌بیند اگر اینترنت واقعی می‌خواهد، باید فریاد کند که این وضعیت عادی‌سازی نشود. مسئول مستقیم این وضعیت، شخص مسعود پزشکیان و ستار هاشمی هستند و باید بابت این سطح از سرکوب دیجیتال و اینترنت ناقص مورد سؤال و بازخواست قرار بگیرند.
خبرنگارها، رسانه‌ها و فعالان حوزه فناوری هم باید بپرسند:
این چه اینترنتی است که به مردم تحویل داده‌اید؟
✍️
iSegar0 || سگارو</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/MatinSenPaii/3502" target="_blank">📅 12:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3501">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">همه میگن سایفون افسانه‌ست و مال پیرمرداست و هیچوقت کانکت نشده و...
برای من WindScribe این شکلیه. حتی قبل از دی ماه هم یه بار واسم کانکت نشد
😂</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3501" target="_blank">📅 12:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خنده دار ترین اتفاق امروز این بود که دیدم کلی کانال که تا سه روز پیش گیگی ۳۰۰-۴۰۰ میفروختن، شروع کردن کانفیگ رایگان بذارن
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/3500" target="_blank">📅 11:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
apple.com : 17.253.144.10</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/MatinSenPaii/3499" target="_blank">📅 10:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni: certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/MatinSenPaii/3498" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5qaZ-G3P-_wX2qEo27WWEvrulX9O7RpRk1eHqjQzSvGZ6AiDdgQrOPG0sZj_TSTAamEvZN1ostraqxACgGyBcUOp3E0fUb0XXzOAt_GlHVFAmeD_lmnTvsmUFjlbLzuzPlXUHEltVO4yoEgOkxF30VrnYw5yWdXdlvWMdT_DYrw4fr8U7SejWXESSEzqKu_EKbrkFWg1xLwmne_0PMS9fIjGLHgEJXZFj0hOQ_Ay8TEOMzqvvmmJwQcdkVbt7asfafPwoVhzpU31F50PLi2Imop8yIzZKL-PdP1pOAw4uT7UTEW_4BS8x_ZT4rQBn4zxYjQZIBdHUU-7o41i-_S3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni:
certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com, bazion.ir, 8.6.112.0.sslip.io, abadis.ir, ikac.ir, ebooksworld.ir, iranicard.ir, gameq.ir, melovaz.ir, sourceforge.net, google.com, scholar.google.com, libra-books.com, uploadboy.com, soft98.ir, daneshpaz.top, berlin.saymyname.website, epicgames.com, uploadina.com, sarzamindownload.com, asiatech.ir, shecan.ir, par30games.net, 3fa.ir, taaghche.com, downloadly.ir, oldtowns.top, cafebazaar.ir, Shaparak.ir, uploadkon.ir, news.google.com, varzesh3.com, hooshang.ai, downloadha.comfilimo.com, gitlab.com, search.bertina.ir, mail.google.com, chat.boofai.com, support.google.com, search.google.com, vercel.com, farsroid.com, bosgame.ir, 2.188.21.46.sslip.io, divar.ir, okta.com, snap.ir, nic.ir, flzios.ir, digikala.com, fastdic.com, cdnjs.com, 162.159.152.4.sslip.io, hooshyar.golrang.ai, openai.com, aparat.com, download.ir, yasdl.com, pastehub.ir, downloadha.com, iranmatlab.ir, bitpin.ir, Python.org, my.files.ir, post.ir, picofile.com, namnak.com, gov.ir, dl2.sermoviedown.pwmyf2mi.top, nixfile.com, pirategames.ir, balad.ir, supermario.corp.google.com, faraazin.ir, vgdl.ir, aharvesal.ir, chat.smartbytes.ir, cdn77.com, behmelody.in, cup.theazizi.ir, alibaba.ir, zarebin.ir, patoghu.com, subzone.ir, navaar.ir, zoomit.ir, rio.ggusers.com, linklick.ir, gold-team.org, dlfox.com, centos.org, fidibo.com, tamin.ir, guardnet.ir, atlassian.com, 2059.ir, site.google.com, sheets.google.com, react.dev, irimo.ir, m.ulni.ir, 2.188.21.130.sslip.io, f2me.top, myket.ir, dls2.iran-gamecenter-host.com, Telewebion.com, airport.ir, ubuntu.com, email.google.com, radio.9craft.ir, torob.com, vercel.app, rubika.ir, dic.b-amooz.com, mizanonline.ir, 87.107.110.155.sslip.io, chess.com, gapgpt.app, ninisite.com
لینک دانلود اپ
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3497" target="_blank">📅 10:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3496">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شاتل و همراه اول هم شروع کردن به رفع فیلترینگ بالاخره(لااقل منطقه‌ی ما)
الان با شاتل با کانفیگای رایگان هیدیفای پیام میدم</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3496" target="_blank">📅 10:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3495">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-text">این ساب تیم مهسا داخل هایدیفای هم رو بیشتر نتا اوکیه پینگ بگیرید یسری سرعت بهتریم دارن
https://raw.githubusercontent.com/hiddify/hiddify-app/refs/heads/main/test.configs/mahsa
داخل خود هایدیفای هم + بزنید داخل نسخه جدید گزینه free روشن کنید هستش</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/3495" target="_blank">📅 09:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3494">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اینها هنوز کار می‌کنن دوستان. برای من اوکین</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/MatinSenPaii/3494" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3493">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/MatinSenPaii/3493" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UHkvd2e7-d5FsCNCHn6tpc6X1CHNmd29qE3mahupA-FL_IhxdjvpBoVIOFuh0Ox55XRm_rAmQFQ-OyrgPkXRSCusK5ffQG_vcMWjyhDlFFO4eEo_3DNr5quqFK3GvHr0wWhD9tJLMmbSAH2BSp31maTF5yMQZB53sVuc89h2kSXsmIaJm_LOSDYhBUqzmH8abvyYAZQRn37_-n7bfc_sHLMu8laHVRJ5-zaTtV0naFkHdUvB05CkLz3-zqb6NP9D5XzsnYYvKIAYwzJPAeKPBoh2_YF_v5hhIRo50kkkBQgZSmyzaqxDZgAPnv48GtgQjK6mC-QFZwfo55l9do2EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت اینجا توضیح داده شده:
https://t.me/MatinSenPaii/3467
اگر یادتون باشه دی ماه هم همین بودش. یک هفته‌ای طول کشید تا همه چیز یه کم نرمال‌تر بشه(هیچوقت به قبل از دی بر نگشت) و الآن هم متاسفانه احتمالا همون روند هستش</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/MatinSenPaii/3492" target="_blank">📅 02:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3491">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مورد داشتیم از چنل WhiteDNS و بقیه‌ی کانال‌ها، سرور اسلیپ‌نت برمیداشت می‌دزدید می‌ذاشت کانالش از ملت پول دونیت هم میگرفت. یک شارلاتان‌هایی لو رفتن سر این ربات که فقط خدا می‌دونه
دوران عجیبی بود خلاصه</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/MatinSenPaii/3491" target="_blank">📅 01:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3490">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">1- هرکسی میتونه با دی‌کامپایل کردن کدهای اپ npv منطق هش پسوورد و... اش رو در بیاره و فیلترچی خیلی وقته که این ابزار رو در اختیار داره. 2- آیپی پشت کانفیگ‌ها رو به راحتی میشه با وایرشارک فهمید نیازی به این جنگولک بازیا هم نیست. 3- آیپی‌های کلودفلر ای که باز…</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/MatinSenPaii/3490" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3489">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">با این ربات می‌تونید قفل کانفیگای NPVT رو بشکونین و لینک Vless معمولی دریافت کنید. حتی اگر رمز داشته باشه:
@DickiriptorBot</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/MatinSenPaii/3489" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3488">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">طرف با کانال دو میلیونی برداشته کانفیگ worker گذاشته توی npv و اکسپورت گرفته گذاشته چنلش نوشته کانفیگ موشکی وصل:/</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/MatinSenPaii/3488" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3487">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فایل Json جدید برای Spoof: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "172.67.139.236",   "CONNECT_PORT": 443,   "FAKE_SNI": "security.vercel.com" } برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/MatinSenPaii/3487" target="_blank">📅 01:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hiddify-Android-arm64.apk</div>
  <div class="tg-doc-extra">113.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3483" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/MatinSenPaii/3483" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=dgQx0Ly3kbNTXm6KU8g2AhLqNOzkND2dTOChBkKi0jAkQshRzIy8AI4_qeBou_GrXa5nixPJ-9dPwOBsJaBiTajobYgMqVdIGkXQqwSwC7IzApcO5-KBSIU7zvPPoeXLt_TvigIDugZKi3VtNZuZTj6MdJS2Uv2kucZb4P69Fv8_HOwle26v4xjoSS6iQu-mDuY2PkaDSmjlInx_8V9Qhz-yD6asxHvOHoi88evmkKFCX-AMyaIKknF54PDM1MnSj4vJgHLFoBanI1zWNuKqGyrxq_o59MJWh6c0FBkcwL7OBSnISoCJUWS9ZWZR9ta-AThDp1vTgU3vheACveUO4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=dgQx0Ly3kbNTXm6KU8g2AhLqNOzkND2dTOChBkKi0jAkQshRzIy8AI4_qeBou_GrXa5nixPJ-9dPwOBsJaBiTajobYgMqVdIGkXQqwSwC7IzApcO5-KBSIU7zvPPoeXLt_TvigIDugZKi3VtNZuZTj6MdJS2Uv2kucZb4P69Fv8_HOwle26v4xjoSS6iQu-mDuY2PkaDSmjlInx_8V9Qhz-yD6asxHvOHoi88evmkKFCX-AMyaIKknF54PDM1MnSj4vJgHLFoBanI1zWNuKqGyrxq_o59MJWh6c0FBkcwL7OBSnISoCJUWS9ZWZR9ta-AThDp1vTgU3vheACveUO4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☠️
آموزش اتصال رایگان با اپلیکیشن Hiddify (اندروید، ios، ویندوز، مک و لینوکس)
در صورتی که کانفیگ‌های CDN روی اینترنتتون کمی نفس بکشه می‌تونید به رایگان با کانفیگ‌های مجانی هیدیفای وصل بشید. چون مدام عوض میکنه کانفیگ رو، به شخصه تجربه‌ی بهتری از خود MahsaNG تجربه میکنید
لینک ریپو برای دانلود:
https://github.com/hiddify/hiddify-app/releases
فایل‌های اندروید و ویندوز:
https://t.me/MatinSenPaii/3483
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/MatinSenPaii/3482" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رفقا، Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w?si=yd2q8LmmyvZ_VfsQ
و Paqet تانل:
https://youtu.be/nwpLOANv7VY?si=OMOXPs7XTV9uqk_M
رو چک کنید که آموزش داده بودم قبلا. رسپینا شنیدم تانل تونستن بزنن بچه‌ها، اما مستقیم هم شنیدم چندین اپراتور. به توضیحات ویدئو دقت کنید Paqet مستقیم با اینترنت سیمکارت(CGNAT) امکان‌پذیر نیست</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/MatinSenPaii/3481" target="_blank">📅 21:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">متد SNI همچنان فعاله دوستان. کانفیگ‌هایی هم که گذاشته بودم(
https://t.me/MatinSenPaii/3183
) همچنان کار میکنه ۱۵-۲۰ تاش</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/MatinSenPaii/3480" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:
1- آموزش پایه:
https://t.me/MatinSenPaii/2627
2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید:
https://t.me/MatinSenPaii/3168
3- و کانفیگ‌های این پست:
https://t.me/MatinSenPaii/3183
ترجیحا با ایرانسل یا سامانتل
4- سؤالات متداول راجب این متود:
https://t.me/MatinSenPaii/3189
و تبریک میگم! شما به اینترنت آزاد دسترسی دارید.</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3479" target="_blank">📅 19:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qA0xZx2UjA1oEufFvIslBkOY34NAbMubZtp7jyXlrjivuZuzEfVhVTXzWUQp4X2rgUFDP_kvoUjS7EQqev-bYHfKEgMeAr6jtJlFyG6uJqCjqQlC9sThWN8GujzDHRD9q5A2PqwbKyUZH9AkddRqoCxFQ7TOl49Ykom4zM2IsscPv5LQa6jM5n10KF0_i3KumUdL7MaB382wfW_j_RH4UVOoeXaX9FRxigsXorYXFI78Aybf_PlxN-7jElMOubbH18i7XOv7QkAXRZBhsTvQyLKfwwe53oPAA1U80gP0QxuTLWfI-9RKxbdBlpcoBjjmb207EYMEnwQh505YIXAZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت اینترنتی که واسه مردم وصل کردن
خط قرمزا اختلاله !!!!
✍️
SamAlpha_</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/MatinSenPaii/3478" target="_blank">📅 18:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3474">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gm4Hxx8xm9-tbcthuldiWQCHRRV8mMT5XwSR_3l1iAvKhvtbrksnfOVTSRNPKst351Wbd2f4H9BivELT6HA-50BSOwwOtieMldTwMncbVOYWHd03JDEkkkjzSXXfJxl5MMN0ygjP39siZ34NeuU3nI8engn2C1BYhCRJg-v4ZAANrsQN2MdKeol1QZB8G3nG_1NcUkrcXJ7Y0_BoYm5qEanRpPFp7IMwqAnr8pgSWbQ1IN4DMae_odzMwFWGgvNBrVvH-3k3iShkX5KvhROxHOwwRwv0P4XaT-LW1KEyiy6iylrZAtiveT85jmEN79HZNxNQEdnfCxX2Kx-Ysku27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aDqhhHTZQZu5f1FJV7tIE6PJoFA0CQmeP52Hb_BQNBhyK7edFWUZNAuAwVB4DwB0tplPqUKSiZ_H46xmFJpDopmFdkWJYrbA7PLWaho4SdACBpoHM0Xb5SiLpYAB0gV5_o2H6ddBFgP7BB1ijbjikH2Z4ffLs6i3BTe6qqk0vevhWjA8FE5vkWxjf62mmHvL380uTOuiXehfiWOSbEAaAt91zamslCnS4Pn-lADjhP3I4Sjmmwl3MSJEpr-WVrM4aZ0CDdGCYBLSUl3Q7hVqKpBHlbDJwNIlnQnmID9ahy6Vu12MB29ik4jH6Snwh2bHCxgcRttoENlThVOM4S9Eaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SfRdCWi1gxRHOZqbeY3NWXxcwax4XTQXAB-d-ESdCR0K9GV4liB_cgXePCX_iApNoqhoyKtv3rMIdaDYbYZwewvSqz8k6EFmga2ySRk2Ki5RzDeEtzjiGZcgDST7vraE5bXd2VCcSMVPTa2uDZVjattu3aerMUUY_ppIs-G14XXvKD6eoBjIqZ6fVd_gXvzKcsrxAK4xa7ufRidxDZu_s1kWfBV09OcsA_0ZXuNMjpTCBCEHta3EChGNLYGSpa5C1mkzubF7QD1xTqEUEIRx3B8f6eRABUPZS8tSRS-8g9KanxzPaQG0ZCjnxC9vql360Nw0AY0Uo8XGR4-JNKD5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/twzbTF7sZgnGMjLwrn4DvG--YSjYRY2iv-bZH8GPVyhxizBcduCZDMRSuT6pnAj4s5uI2-l886qwkfLIydHhgHiXx-JVeyCfU9GqpWOSDmKNV3up0AHlfIw2D5Ct5CSiAMTKETJBQqtQP-8VCjeUO0kgUxVzIiubU__ni4tUUBpYfC4iZHdyIvB4ElX8ca3czwMdmLYzQnKYzzvWWrv752TU7rJvZDONGlIax1zSFMUHAqijOBx3TWHhmKUYpq_SAVi0usZziA12YAuAx6lXVTIq7r4j3SWqk5uU_kIIp0IzasZgHH7AzBpaE0rDdC02KDYe-8dUdJcqkb4OOsFaIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیر و خورشید برای من این شکلی شده که وصل میشه اما هیچی کانکت نمیشه</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/MatinSenPaii/3474" target="_blank">📅 17:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3473">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فایل Json جدید برای Spoof:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "172.67.139.236",
"CONNECT_PORT": 443,
"FAKE_SNI": "security.vercel.com"
}
برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/MatinSenPaii/3473" target="_blank">📅 16:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3472">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آموزش ساخت کانفیگ BPB شخصی:
https://t.me/MatinSenPaii/3443
آموزش  Sni-Spoof هم این:
https://t.me/MatinSenPaii/3186</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/MatinSenPaii/3472" target="_blank">📅 16:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3471">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8VahNZFFo1Wq0t7FzeYSvT2Qiv4dzedPtkdV0djosMb4povJXcCOKws43GsbHoNKxsEzAOJVXZfJAbUFNrQpz1Xw18VLEOoZIpDdeaMf_NUWdfbdf0otn6twJRSUwG8T7uo5mI2B6QTcmWbyByqsMRNfjpHPQJh8sS3EtuZe2s9k789hSNQADWbR-8Xq5oBlw2_Ti96qRWK6W30aNmGK8DmNvMf7uKwp0AgH3Q6uPF22RAUnqF8qTXuYPm3OkOMsPi1BRBQ7_KVacVKVZfJbabtul6zLyZ504l7uUd4GbnqL791Zi7eU2hrpaY6bn4fTGnRt7iac6i30KgEIG-p8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سرعت آپلود روی CDN و Worker Cloudflare</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/MatinSenPaii/3471" target="_blank">📅 16:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3470">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bwJC6EhcNuBc7XUYhFSBLfukrx6WFJgk6V5U-En3gtWoM9tm6Quu1TOF3wvh9_YOVN9Etw-DgJgbAXzdgTDYr7b_akVwUcXx0JMMO7aDMJJsGPaA997LKD12SAasTKlrYlUbDwkhSucFNxtfNVsuu1xeJI1ENJxxGhJk1b2udsFR9t-Qe0a_QyimpG2KaYsqJoEOhGpMpvwwnkhHSn6OAgweIn7GA86fP4kFWC9v-dMoWLjLYsK-LqkhEBjVRzLrYzwAYtKbS1yOECzxIXv25_Rikj72F9mmj221qFe2Js-5R43nI0NpT2DKv7F5JKzwAEvb82voaw7i7_4eYRABhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سرعت آپلود روی CDN و Worker Cloudflare</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/MatinSenPaii/3470" target="_blank">📅 16:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3469">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wr8B7mQk-i4dfFVlBYGHk_5Z4HXwtVu0xRyKPMwMkTylatBjEjGS7qP-xlUowLDNVVyfDplaDJoSOmJOXMtT_U6nNNfYQi8MEiIWT3joSz5p_9FWOzcUm0Yf0M8s1NJDm5faEn6OfLYV26CCRKTvY593AnQ_4siqz6iyP22xuJLRof94s0JYhMKINZ7CFqXfHB23_sj3M9BmTqgUjRE66C2NQW5FC0ECJdDdtc5HbbCxKerE-Xp9K8QNQgX91ZNQxHIOeS3hF5N9Li-36U4N_UhwBmEnvTgD2WtpvobGWU6tnY5uXilIR0QJpwnxQ8ZnNcW7Pu4Hu-CiGWmNZVsWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از اهداف من اینه که آموزش‌هایی بذارم طی چندوقت آینده، (هرچند قبلا هم گذاشتم) که شما رو بی‌نیاز کنه از خرید هرگونه کانفیگ. و هرشخص بتونه برای خودش و خانواده‌اش به راحتی فیلترشکن شخصی راه بندازه. منتها اگر فعلا نیاز دارید به لوکیشن و یا سرعت و... ، می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/MatinSenPaii/3469" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3468">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بزرگترین نجات‌دهنده‌ی ما، WhiteDNS و MasterDNS هستش که از واجباته برای خودتون ستاپ کنید! توی کل این 80 روز می‌شد باهاش وصل شد. آموزشش رو هم ضبط کردم طولانیه اما حوصله کنید و ببینید:
youtu.be/6Pm7kNQb3mo
‎</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/MatinSenPaii/3468" target="_blank">📅 10:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3467">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💭
چرا زمانی که اینترنت را قطع می‌کنند، درجا این کار را انجام می‌دهند اما وقتی نوبت به باز کردن می‌رسند، انقدر قطره‌چکانی این کار انجام می‌شود؟
1-
جنبه فنی
(دلیل اصلی تفاوت سرعت قطع و وصل):
🌐
ایران اینترنت را از طریق چند gateway بین‌المللی محدود (عمدتاً تحت کنترل شرکت ارتباطات زیرساخت - TCI و ASهای اصلی مثل AS49666) به جهان متصل می‌کند. این ساختار متمرکز است:
"قطع کردن آسان است"!
کافی است BGP announcements (اعلام مسیرهای روتینگ) را withdraw کنند، یا ترافیک را در gatewayها بلاک کنند، یا IPv6/IPv4 را محدود کنند.
با دستور مرکزی، همه‌ی ISPها (مخابرات، ایرانسل و ...) در چند دقیقه یا چند ساعت، آفلاین می‌شوند. مثل کلید kill switch.
وصل کردن سخت و زمان‌بر است:
وقتی همه چیز را قطع می‌کنند، فیلترینگ، routing tables، DNSها، و سیستم‌های DPI (Deep Packet Inspection) و SNI filtering در لایه‌های مختلف (gateway، ISPها، IXP) به هم می‌ریزد.
برای برگرداندن، باید تدریجی تست کنند:
اول routing را باز کنند، سپس DNS resolution را درست کنند، بعد فیلترینگ را لایه به لایه اعمال کنند تا "نشتی" (leak) اینترنت آزاد رخ ندهد.
هر تغییری ممکن است باعث باز شدن ناخواسته سایت‌ها/اپ‌ها شود، پس مرحله به مرحله روی ISPهای مختلف و مناطق تست می‌کنند. این کار ساعت‌ها تا روزها طول می‌کشد.
در قطعی(و سپس وصلی)‌های اخیر (مثل جنگ دوازده روزه یا دی‌ماه) هم دقیقاً همین الگو دیده شده.
2-
جنبه سیاسی-امنیتی
:
💬
قطع: تصمیم سریع از شورای عالی امنیت ملی یا نهادهای امنیتی گرفته می‌شود (برای کنترل اعتراضات، جلوگیری از هماهنگی یا جاسوسی سایبری و هر مزخرف دیگه‌ای).
وصل: نیاز به هماهنگی بین نهادهای مختلف (وزارت ارتباطات، سپاه/اطلاعات، شورای فضای مجازی) دارد. گاهی اختلاف میان این نهادها در بازگشایی یا نوع آن، باعث تأخیر می‌شود. آن‌ها نمی‌خواهند ناگهان همه چیز باز شود چون کنترل را از دست می‌دهند. پس "تدریجی و با احتیاط" اینترنت را باز می‌کنند تا فیلترینگ جدید را تثبیت کنند.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/MatinSenPaii/3467" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3466">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">کانفیگای توی
لینک سابسکریپشن
رو چک کنین. کار میکنن براتون احتمالا.</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/MatinSenPaii/3466" target="_blank">📅 01:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3465">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اسکمرها و کانفیگ‌فروش‌های دزد و گرون‌فروش، هم‌اکنون:</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/MatinSenPaii/3465" target="_blank">📅 23:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3464">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">حقی که نصف و نیمه بهمون داده بودن و با فیلتر رو ازمون کامل گرفتن، بعد ۸۰ روز هم پسش دادن، به همون حالت نصف و نیمه.
شرمنده اگه یک درصد هم باعث خوشحالی من نشده این وصل شدنه. هیچی تغییر نکرده.</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/MatinSenPaii/3464" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3463">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سرعت آپلود شما هم پشت worker و کلا کلودفلر پایینه بچه‌ها؟</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/MatinSenPaii/3463" target="_blank">📅 21:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3462">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⚡
cfray v1.1
یه ابزار تک‌فایلی پایتونی که همه چیز رو برای مدیریت کانفیگ‌های VLESS و V2ray پشت Cloudflare یکجا جمع کرده.</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/MatinSenPaii/3462" target="_blank">📅 21:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3461">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اینترنت برگشت، و خوشحالم که توی این مدت تونستم کنارتون باشم و توی اتصالتون به اینترنت آزاد راهنماییتون کنم
❤️
همونطور که همیشه گفتم، زحمت اصلی رو برنامه‌نویس‌های عزیز کشیدن. افرادی از جمله پترنیها با sni spoof، امین محمودی با MHR و MasterDNS، aleskxyz با پروژه‌های خفنش، iampedi و تیم خوبمون با اپ WhiteDNS، سارتو با پروژه TheFeed، سم، مارک، Samim با پروژه شیر و خورشید، و همینطور بچه‌های کامیونیتی زیرزمینی Vasl، عزیزی، امیرپارسا، ریتالین، GuardNet و... که اسم‌هاشون بی‌شماره.
می‌خوام بدونید که خیلی از افراد پشت من بودن تا بتونم آموزش‌ها رو به دستتون برسونم. و اسم خیلی‌هاشون رو نمی‌تونم ببرم. از اون عزیزی که به من صد گیگ کانفیگ داد گرفته، تا بچه‌هایی که قبل از آموزش‌ها باهاشون مشورت می‌کردم تا اشتباهی نداشته باشم و همه‌چیز بی‌نقص باشه.
همینطور از افرادی که به من دونیت کردن و من تونستم کیبورد و موس بگیرم که وضعیت بدنیم بیشتر از این اذیتم نکنه، و راحتتر بتونم تایم بیشتری رو پشت سیستم باشم.
صمیمانه از همه‌تون ممنونم
❤️
ما همه بدون چشم‌داشت کار کردیم. و هیچ منتی سر شما نیست و شما هیچ چیزی به ما مدیون نیستید.
و ما کسایی هستیم که امثال سگارو، یوسف قبادی، IRCF، وحید فرید، یـ‌بـ‌خـ و... رو دیدیم و قدم برداشتیم توی این مسیر.
هفته‌هایی بود که چند روز پشت سر هم نمی‌خوابیدیم، با درد مچ دست و کمر و چشم و تونل کارپال و وضعیت جسمانی افتضاح خیلی‌هامون ادامه دادیم؛
فقط و فقط چون به آزادی باور داشتیم.
زنده باد ایران</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/MatinSenPaii/3461" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3460">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تا فردا-پس‌فردا به احتمال زیاد روی همه‌ی اپراتورها کلودفلر رو باز میکنن. و منطقه‌ایه مثلا اینجا حتی ایرانسل هم قطعه هنوز</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/MatinSenPaii/3460" target="_blank">📅 20:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3459">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تا فردا-پس‌فردا به احتمال زیاد روی همه‌ی اپراتورها کلودفلر رو باز میکنن. و منطقه‌ایه
مثلا اینجا حتی ایرانسل هم قطعه هنوز</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/MatinSenPaii/3459" target="_blank">📅 18:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3458">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستانی که همراه اول و شاتل و زیتل دارن، حالا حالاها باید بشینن تا وصل بشن</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/MatinSenPaii/3458" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3457">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin Mahmoudi</strong></div>
<div class="tg-text">نقطه قشنگ ماجرا خارج شدن این موضوعات حتی از ایران بود، این افتخارش رو هممون بدست آوردیم، هرکسی به نحوی کمک کرد.
یکی روی توسعه کمک کرد.
یکی با ساخت ویدیو کمک کرد.
یکی با توییت زدن و معرفی توی کانالش.
یکی با استار دادن.
دوستان برای پروژه ها نرم افزار اندروید ساختن و ....
همه باهم کنار هم باعث شدیم پروژه ها خفن بشن.
همه با هم کاری کردیم که پروژه مثلا MasterDnsVPN، چندین روز بهترین پروژه زبان GO توی گیت هاب باشه.
همه با هم کاری کردیم همین پروژه 2 روز توی ترند گیت هاب باشه و اینا همشون خیلی خفنه.
توی پروژه ی MasterHttpRelayVPN، هم همه باز همین کمک هارو کردن و موفقیت های خوبی بدست آوردن.
همه با هم این کار رو کردیم، کار یک نفر نیست.
این مدت جدا از بد بودن و سختی ها، همه با هم افتخاراتی رو بدست آوردیم ...
که همه با هم باید به هم خسته نباشید بگیم
❤️
درکل همگی خسته نباشید.
امیدوارم این روز ها دیگه تکرار نشه ....
همگی عشقید و خسته نباشید، دم همگی هم گرم
❤️</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/MatinSenPaii/3457" target="_blank">📅 17:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3456">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسکمرها و کانفیگ‌فروش‌های دزد و گرون‌فروش، هم‌اکنون:</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/MatinSenPaii/3456" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3455">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18fbc73a71.webm?token=Op0CTRWAQ89Q_CjsL51S6WculLpL9GEyet2Mvp_ZDTCe3KFuqMsfFI33gfOzOolS5unqgyoB3ICqqcVD5_96VvHaVziuTvWHCrIw2naBjWoFytRJ0YYNDFha1ZyvsEZaP63YVRjHREcrTlzB7KPQSgCNn8-ctAh2acTBkXA_Bks93XkngvtX8erfkrO48gT1pHdEc3ORdo_5JMz1loecG56JiBrsWmW9JyGp75_-NCofns0rBhQ7C9MhpJvK4NNFBI7-1ZPp2BFI5ISCEpy_GctvSU044QxV-FZkAZubQNhsJ4WPZNPPI5imeeqtxtR0C_yfhDpb06GoLtcIaf7ijA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18fbc73a71.webm?token=Op0CTRWAQ89Q_CjsL51S6WculLpL9GEyet2Mvp_ZDTCe3KFuqMsfFI33gfOzOolS5unqgyoB3ICqqcVD5_96VvHaVziuTvWHCrIw2naBjWoFytRJ0YYNDFha1ZyvsEZaP63YVRjHREcrTlzB7KPQSgCNn8-ctAh2acTBkXA_Bks93XkngvtX8erfkrO48gT1pHdEc3ORdo_5JMz1loecG56JiBrsWmW9JyGp75_-NCofns0rBhQ7C9MhpJvK4NNFBI7-1ZPp2BFI5ISCEpy_GctvSU044QxV-FZkAZubQNhsJ4WPZNPPI5imeeqtxtR0C_yfhDpb06GoLtcIaf7ijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/MatinSenPaii/3455" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3454">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نت خونگی اوکیه
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.21.7.21:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%202</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/MatinSenPaii/3454" target="_blank">📅 16:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قربون دستت حالا که دستور دادی اینترنت باز شه
یه دستور هم بده اونایی که کارشون رو از دست دادن برگردن سرکارشون
یه دستور بده اونایی که زندگیشون از هم پاشید برگردن سر خونه زندگیشون
یه دستور بده اونایی که سر اجاره خونه خونشون رو تخلیه کردن برگردن خونشون
اینترنت شاید برای شما یه دکمه روشن و خاموش باشه، ولی برای خیلیا نیست واینترنت زندگیشونه که با دکمه خاموش و روشن به حالت قبلی برنمی‌گرده.
✍️
Reza Jafari</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/MatinSenPaii/3453" target="_blank">📅 16:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🍷
بازگشت همه به سوی سایفون + v2ray هست چند تا جدید که گفته بودم میزارم استفاده کنید ip جدیدا رو
✅
141.193.213.11
104.18.38.202</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/MatinSenPaii/3452" target="_blank">📅 16:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مجدد کانکت شد</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/MatinSenPaii/3451" target="_blank">📅 16:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lfPtq-gtYy0u9TdG_SDc3IVSyWUIjI2hH5H1UQX0j8HZ9HK_-8t3bGIIHSK7i7uz5pbYBOkDW2Zju-EAysJckW19jj_apGrlf6LCpJipGIlbm7Lpj3Bm5xIVRINz78i4lQQQDbZEEbt6pot9jM1O2knx_TOASpzmi3pMr6QxmzdVGw8YCcugO-eholRgE3kFh4fE3F0vWsjgJ-C8I3jTn7VDZ_ucv-GGKefIjFiwOkn1ALVtRAT1oionq7S-toGvV4xYB1PPW8zPule7l1o8WLHKtu-PzvPeaIhDUF1aaFjMgHSIBM8qK_xuJ6fYIHmJrDWE80NO0kxPqSS1EVVmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجدد کانکت شد</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/MatinSenPaii/3450" target="_blank">📅 16:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3447">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قطع شد
😂
چیکار دارن میکنن</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/MatinSenPaii/3447" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3446">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%201</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/MatinSenPaii/3446" target="_blank">📅 15:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3445">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%201</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/MatinSenPaii/3445" target="_blank">📅 15:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3444">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Matin SenPai
pinned «
☠️
آموزش اتصال رایگان با آیپی تمیز کلودفلر و کانفیگ‌های BPB  1- ابتدا ویدئوی ساخت پنل رایگان BPB رو از اینجا تماشا کنید(هم با گوشی میشه هم با سیستم. از نصب دستی استفاده کنید): https://t.me/MatinSenPaii/1965  2- سپس آموزش قرار دادن آیپی تمیز و سایر تنظیمات BPB…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3444" target="_blank">📅 15:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3443">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">☠️
آموزش اتصال رایگان با آیپی تمیز کلودفلر و کانفیگ‌های BPB
1- ابتدا ویدئوی ساخت پنل رایگان BPB رو از اینجا تماشا کنید(هم با گوشی میشه هم با سیستم. از نصب دستی استفاده کنید):
https://t.me/MatinSenPaii/1965
2- سپس آموزش قرار دادن آیپی تمیز و سایر تنظیمات BPB رو از اینجا تماشا کنید:
https://t.me/MatinSenPaii/1980
3- این لیست IP رو طبق آموزش مرحله‌ی 2، توی قسمت Clean IP قرار بدید:
104.19.229.21
104.18.139.67
104.16.80.73
104.16.117.43
104.16.89.120
104.16.118.43
104.16.63.25
104.16.7.70
104.16.79.73
104.16.90.120
104.16.62.25
104.16.6.70
4- از قسمت Raw (without settings)، یا Normal، لینک ساب رو کپی و داخل کلاینت V2ray خودتون وارد و به راحتی استفاده کنید.
5- اگر دامنه
workers.dev
روی اینترنتتون فیلتر شده بود، از طریق این آموزش دامنه جدید ست کنید:
https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/MatinSenPaii/3443" target="_blank">📅 15:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3442">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه کم دیگه واستون مرتب و تر تمیز میکنم آموزش‌هایی که قبلا دادم رو دسته‌بندی میکنم و می‌ذارم خدمتتون</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3442" target="_blank">📅 15:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3441">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/krMT_CIZ_OoicPBD9CSJORXbh5VxM9wb3TyoGTnpVYYxSMdYG0B6Ix-o6jNWf2tvNZCZ9C_DPBFANqxzfsI500cFaOuhODGz8bV_wDLl6MquajAJ5WpUt_YCmIEQO5djdSPUMFxvE3vIh6UIEGm6dT586y9GXgZ9_BB3p8rEF1Y9II8mt-ggTzGMr1lDUyg1khPyKPvVLuuGAAwhvtiMC0hCf6cIC7Q3CL_hNwBqHjBNJV4gQkiccfxvBF-4HDT-yDtTO41FjZjwJpCTbXf3mL_Taij5esGMCRCgtgjU1OeLr5ix80lf2IimR237w98AN3ddvlWPX_4dGQgVlBlWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/MatinSenPaii/3441" target="_blank">📅 15:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3440">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">با این وضعیت، کم کم نت‌ها رو دارن آزاد می‌کنن
از اختلال و اینها گذشت دیگه</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/MatinSenPaii/3440" target="_blank">📅 15:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3439">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">همچنین 104.18.139.67</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/MatinSenPaii/3439" target="_blank">📅 15:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3438">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خود آیپی 104.19.229.21 رو توی کانفیگ‌های معمولی BPB و کلودفلرتون تست کنید. یکی سری از دوستان میگن آیپی سفید شده</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/MatinSenPaii/3438" target="_blank">📅 15:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3437">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خود آیپی
104.19.229.21
رو توی کانفیگ‌های معمولی BPB و کلودفلرتون تست کنید. یکی سری از دوستان میگن آیپی سفید شده</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/MatinSenPaii/3437" target="_blank">📅 14:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3436">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v00B_yPHVHKgrkxK6enqr8tLfE8-GHEAjI75oRAAT_E8Rr1l00Hov55bB_J9X7s_jIqmJfjPi822qBCYoBp97OEFV3IttWYozwXi3v3fROo7TvleGwfaxMYhx6di90JQH6MUWyTsQOaHYoZnCBL1bN6W9ArqL2Xsbnz7CXwH3ybC_i2U5sseSgoCEKswG9VzVINDfvwfeE-lgo5ae4tR80gxCplrhsg1ulADGID-n74vO28GXo82DJ-z1vGYkmOSFX2a04UlIAYqS8ikullxdIpgQPYP-F-XIUrpXfQS6Kafhm_HF1AYJZsy3AUsXkK6jONc21B2lL1xYyJtr-LNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کم کم داریم توی هرم مازلو اینترنت پیشرفت می‌کنیم:) از صبح دنبال اینم که بتونم یه راه ساده و رایگان برای گیم واستون پیدا کنم، اما متأسفانه فعلا فقط تونستم با پینگ ضعیف با ترکیب سایفون گوشی، گنشین ایمپکت رو بالا بیارم و بازی کنم</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/MatinSenPaii/3436" target="_blank">📅 13:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3435">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نمیدونم احساس منه یا واقعا این شکلیه اما انگار اختلالی که روی پهنای باند سرورهای ایران تأثیر می‌ذاشت خیلی کم‌رنگ شده از وقتی Spoof باز شده</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/MatinSenPaii/3435" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3434">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قول میدم اگر فردا و پس‌فردا اسپوف همچنان وصل بود، یه سری آموزش باحال داشته باشیم ازش. همینطور یه سری آموزش راجب چیز میزای برنامه‌نویسی و ستاپ کردن IDE ها و نصب کردن آفلاین اکستنشن‌های Ai و این قبیل موضوعات چون خیلی آسون با اسپوف میتونم واستون ویدئو ضبط و آپلود کنم و کارم هزار برابر راحتتره</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/MatinSenPaii/3434" target="_blank">📅 03:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3432">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ecssrPDLd3aVxAWrXC-bjPQgQCx0pxPbgmCJ6vZokw-UftHq5MlyHpApo01MzSpnHenJ3F01-Jim32ysWAosQ20m2MG5cugBaIIbbKRaIgVdNMcj11E1Pbsr-igxqB-lFzG1lK3OZrysn59Bo-b2bFrtJw635saqpIY_roWGkSjV_25DVSNaelfhUFogyoHV6pCzQKP1N0TvrLZj4R0GEdWm5WRHed7VlNNXgs8gUhb8qVnpcpOMCzqjQaFTlIrgw92RaT1lCgxJ54vkZX2fKCd7Z3_xMgCF9zKISgjRqnrDiANPYWYO27PGqdOHgsVNebcPiJWQo8g2aAAlGRVKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EbYltG1r_0KkjVBRZ-VI1TrhQk7V23JYNJh70oKIgiXIhMejQ3Zqxrh92y80EodYgFtyosv4CIaNm4G5ydmzNHQBfoY7O0q8VQ_anyvbumBvjbDmYvy9yrofMpLtEBDZm2QSfFY_hxEV02QMKMJWAH5vH0ctEx2HNRVtojpm_BAhAQlv6_9qMiQ3zmmJdsmNVsP20tY4u7kti8ZwYIz33yK75huLe5WXdWB6nwqLA1OuslMMJ9v9FnkZ_JwdGseSmS-g95oK-BawJ4Vg8jINgYNm15_Y4M_2AnMfUY7t5HJ7MdSSTXqLbfPHRehyd-8po2n9v57WXY6q_Rhka0-OIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پولی که قراره آمریکا آزاد کنه: 6 میلیارد دلار
ضرر قطع 80 روزه اینترنت طبق گفته خود دولت: 6.4 میلیارد دلار</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/MatinSenPaii/3432" target="_blank">📅 02:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3431">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صدای تیراندازی سنگینی که در نزدیکی بندرعباس شنیده شد، پس از آن آغاز شد که سپاه پاسداران یک شناور را در دریا هدف قرار داد و در پی آن، جنگنده‌های آمریکایی قایق‌های تندروی نیروی دریایی سپاه را در خلیج [فارس] بمباران کردند.</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/MatinSenPaii/3431" target="_blank">📅 02:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3430">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نمی‌خوام دلسردتون کنم اما باز شدن Spoof روی فقط و فقط یک دامنه، به معنی اقدام برای سخت‌گیری "کمتر" نیست لزوما. مسئله اینجاست که فقط و فقط
hcaptcha.com
روی sni باز شده. مابقی سایت‌هایی که وجود داشتن برای ابتدای متود، هیچکدوم باز نشدن و الان ده تاشون رو تست کردم با config.json های مختلفشون.
اگر واقعا شل‌تر شده بودش، روی اونها هم باز میشد. بیشتر اینطور به نظر میرسه که دولت الان بهش نیاز داشته که بازش کرده و هروقت هم بخواد می‌بنده.
هرچند همین متدها، هزینه‌های بسیار گزاف روی دست دولت می‌ذاره. هم برای مجددا فیلتر کردن، هم برای خود فیلتر بودن این سایت‌های ضروری.</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/MatinSenPaii/3430" target="_blank">📅 02:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3429">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/MatinSenPaii/3429" target="_blank">📅 02:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3428">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انقدر چیز میز می‌خواستیم دانلود کنیم زمان قطعی، حالا که Spoof وصل شده دیگه یادمون رفته چی می‌خواستیم بگیریم</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3428" target="_blank">📅 01:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3427">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fzaK_TS5f5YZZ2RslgWB-frvvYKVDXxNMC93K-a5CZ7fK9XaprSTXHweF6JeYqu31dASWOaHUv8hQD-8ZZuYHZymG9-n3TrssjjfMTl9VKVPgITDyI3NoVOIrUdgzpyHCYeEk06kl2Vyeu9UtJ4VPzTux-gve0j2oPrFzGsC2jyLTVj2ZR3x6i1fwpHA37-S2IJGd8jn55JV-JuSLNOFQEijlEIb5al2ONmK1rZ3Ks36LxAqCcXqF694oxZRVsjKnsmC3Cj3bOPju1oLdJuj8SwZIo2XczCtvOWgtu-wK5d4gV8Sj0JehgzWIYmePcyoPDVdpgSK_B9xrlUYQRvTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aleskxyz
:
واسه sni spoofing من یه اپ با go نوشتم که به جای اون template واسه client hello که توی کد اصلی هست، از utls استفاده میکنه که میتونه رفتار مرورگرهای مختلف رو تقلید کنه.
همچنین fragment و ارسال چندباره fake sni رو هم بهش اضافه کردم.
توی تست خودم واسه لینوکس و ویندوز کار میکنه ولی نمیدونم داخل ایران هم جواب میده یا نه.
اگه sni spoofing روی نت شما جواب میده، این رو هم تست کنید، هر دو نسخه‌اش رو. ببینید کار میکنه یا نه
از firefox واسه utls استفاده کنید. خیلیا مشکلشون حل شده:
-utls firefox
توی نسخه جدید (v0.3.0) میتونید کانفیگ رو داخل فایل config.ini بنویسید و بذارید کنار فایل exe رو فایل رو run a admin کنید. نمونه محتوای فایل:
listen =
127.0.0.1:40443
connect =
104.19.229.21:443
fake-sni = hcaptcha[.]com
utls = firefox
قبل از اینکه بخواید از این روش استفاده کنید، لازمه این دو تا شرط برقرار باشه.
اول اینکه لینک زیر برای شما بدون vpn باز بشه. اگر این لینک باز شد مقدار ip رو بخونید و یادداشت کنید:
hcaptcha.com/cdn-cgi/trace
‎
بعد این لینک رو باز کنید و ببینید ip داخل ایران شما چیه:
ipmyp.ir
‎
اگه هر دو این ip ها یکی بود، این روش احتمالا برای شما کار کنه وگرنه قطعا کار نمیکنه.
https://github.com/aleskxyz/SNI-Spoofing-Go</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/MatinSenPaii/3427" target="_blank">📅 22:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3426">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3426" target="_blank">📅 22:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3425">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaL08fyjtmXdRb6n4l-DLjB93S_Kl2V4Q7BYlAltiV42lQkhtSPtpkfr0ruF0y5SQvDtA9ydX6DDrOMoZHq8gpkR8wNZbiTwVwuc7CUBQX7pgM0lCR6LZpBJRP2sfOqVUKYxLp5cz4FjO1noVcez3ayLhbIIiu3sQsXpT6xY2AdvGriN8i1RVDMiGVzQU0m5YdjeRKvhcWB40if-KGABabjrAlCOTfvCBgM-T7tceDNBOX95k4Nn0UuoIVjyK3Vz6SUgi4yauOW3y6LV45qWsNKHZXJg1RuLAoBUtIKt7dOxyqTGA5uwSZUtLXhAZXjthYHWCAV881k8tfFLUzygc6jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaL08fyjtmXdRb6n4l-DLjB93S_Kl2V4Q7BYlAltiV42lQkhtSPtpkfr0ruF0y5SQvDtA9ydX6DDrOMoZHq8gpkR8wNZbiTwVwuc7CUBQX7pgM0lCR6LZpBJRP2sfOqVUKYxLp5cz4FjO1noVcez3ayLhbIIiu3sQsXpT6xY2AdvGriN8i1RVDMiGVzQU0m5YdjeRKvhcWB40if-KGABabjrAlCOTfvCBgM-T7tceDNBOX95k4Nn0UuoIVjyK3Vz6SUgi4yauOW3y6LV45qWsNKHZXJg1RuLAoBUtIKt7dOxyqTGA5uwSZUtLXhAZXjthYHWCAV881k8tfFLUzygc6jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3425" target="_blank">📅 20:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3424">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو: https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/3424" target="_blank">📅 16:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3423">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hVai59-ztwgBqljxahqeXQvMyihxQK4Nx2K3mS41EJcmB-NsZqqBqxzKUfTGW8MVJi8QrFA-1_jINrsECybMy9nYLx-zffauASYyFZh3lNgMSciMzebDIXJ8UH_HOV-vWpJGjMc82FUnBQO9isQUI7p35JUkBisqWoSCFDkZjcNA9_W6WlK7x1PY869F374Il3F_b78Idl0kt4T7A4Xe2CfPMqVrgMAimLBj18PLTn3gu8pHnlQim0a0jBwVmx5nLZeVh_Is-aUCnAvXAXQieEPd37ieac4RQ4hQ-lAu8kk2HSsKQK8Z9Y8ysQuGBojvtZfFTKsIEBvcirtJ6Q3eQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو میگیرید روی دسکتاپ،
۱- چند بار تست کنید و تلاش کنید برای اتصال
۲- گزینه Parallel test رو با تمامی گزینه‌ها بزنید تا شروع کنه به گشتن
۳- اگر باز هم نشد، یک بار MasterDns رو حذف و مجددا روی سرورتون نصب کنید و با تنظیمات اولیه‌ی خودش تلاش کنید برای اتصال. اینکریپشن و اینها رو تغییر ندید ترجیحا و دقت کنید که دامنه و اتصال و دستورات رو مو به مو مثل ویدئو انجام دادید</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/MatinSenPaii/3423" target="_blank">📅 15:54 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
