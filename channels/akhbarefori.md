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
<img src="https://cdn4.telesco.pe/file/m7bCQLEfXHB3TCwQgHen6R8sfZ8XWSGlfBfgWbKqP7KQ7drigxpzcb86KKN5P1iOzueWl_7twW9QnzLsmMXa_JfvJTC0Q_tKFZVnc4TWOP4snIDY02DWBPgzoGmE3ks5WuPcdcqcq1wr5-b951ELjR57nL3iMdnKiTsmswV9CMCc7d4v2U1LEWBrLfMAqYiuNeCDF-qhkfhPlXMxs8TNtEjNg5CvxPfM1I0tH3XZA5ngtVS9aJz4bIyU1Ni_FDLWyfx3foVrfVOyuB1YcG9XCxbOv3sJApkHu1ZfNVO_su1CkxxZG1q2Z2REaQqE0-PX_IkC1hlHsSUIiEyLrsuEfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 11:41:22</div>
<hr>

<div class="tg-post" id="msg-667373">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9555d366.mp4?token=YHAlWI4TwrluUVRoOY1erf3q-YHnpmpKkdJ_PUk3of_RhLWY20ZNQsdbNI5XzqD_0dgNIj1nVDA_iqCxI7AXTaPmDGKdjiDO2p6AlUuUB32dmxD3RCu3xfUHP0x4IsKPn95IIOrjMSj0Cwi0q0H4-9-hEblCaWochvtcTd_jJEuckk_jgaQAk6OrFPhWZ0OzuuT8sreFfH9Dh5Hk-lHAPKNQVJ7RVtqVBcEl6GBoxIMiZqQKx9NJulozITLM6E_kQLRcH40QI3zul8tLVgxQsAC8bEnalgHKk92ryZED3E5KT3WJCxjBfBVL07dsRYZBvVPaenQkTenRC-rzdQa_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9555d366.mp4?token=YHAlWI4TwrluUVRoOY1erf3q-YHnpmpKkdJ_PUk3of_RhLWY20ZNQsdbNI5XzqD_0dgNIj1nVDA_iqCxI7AXTaPmDGKdjiDO2p6AlUuUB32dmxD3RCu3xfUHP0x4IsKPn95IIOrjMSj0Cwi0q0H4-9-hEblCaWochvtcTd_jJEuckk_jgaQAk6OrFPhWZ0OzuuT8sreFfH9Dh5Hk-lHAPKNQVJ7RVtqVBcEl6GBoxIMiZqQKx9NJulozITLM6E_kQLRcH40QI3zul8tLVgxQsAC8bEnalgHKk92ryZED3E5KT3WJCxjBfBVL07dsRYZBvVPaenQkTenRC-rzdQa_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدر زهرای ۱۴ ماهه در مراسم تشییع همسر و فرزندش به‌همراه شهید انقلاب
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/667373" target="_blank">📅 11:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667372">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYaIvqz-auKl5VR5ZEYk-ahOAArBuwNJgq6BXxHkFicGEQgtNSnyF--2gZ8C_rFWluZkWI1BrCRVpXxNh2_jKF2vVnp6DzhYLq8nMnth5F4upzqRlenWpXh5pJeslRE1KyJae-7uYPk1tlzeYrnn-WqKU4rt2a8dIPcHea4MMaC0dYOQ6yYG1r4xen0vM4sOpOgZM-ihCAHkJV9znnfVrWCgoFPaVaORRPhV9LYMDUfXxbkQfKLSZ77ARt5ZCfnyuo9yBHva1qLrjgqDtk8Lw8urvSudYCYZbKWY7bMitqEF8OyKgMVrLUzaOZvucxL25aIpxsXtb5yg3W6HTwfwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شکوه حضور مردم از نگاه دوربین/اینجا خیابان آزادی تهران است
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/667372" target="_blank">📅 11:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBhpi5QPYqrBaBnyWfTzDKYqhUujLYdVJajTrMIW8QUQAwNPIYwQTxVKzOhcLJyNY7COVimLfdJW8fIeflvONcrvSww2wPEFIh1zFeDzKg6Y_UYxbz4hSD9-5e7x8_4JZG4J_RVI3fm4xQm2bvyERwMcBfDmvp7vvtZ4Lmfq5kzJOcBsln5eAXDV2pvaRbhHs9LmLXHTatY_lXGfnvx-nunk92gaTeIFrIN5t5H8TQCquSUtQ617odDQPRwyUwJm8DOX2R0e6RHNoFNeM1tzUDn5egLzA292k5RGJAT4npUd23CxXTseA4uawHRV6Ic4IESPKaWZWax7XmVMfevUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دعوت مقتدی صدر از زائران اربعین برای تشییع امام شهید
🔹
سید مقتدی صدر، رهبر جریان صدر عراق، امروز با انتشار بیانیه‌ای خطاب به امت اسلامی، ضمن گرامیداشت مقام شامخ شهید ولایت، جهاد و ایستادگی از عموم مؤمنان و زائران اربعین حسینی دعوت کرد در مراسم تشییع و وداع این شهید بزرگوار شرکت کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/667371" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qllD8rAYNjjHzkLOFa2MrmC18ZaQ2abpSROE350gYeqTWHb-GuMYqygTVmNRdgmayLTJjH1_viZXgbfXpcotDAirvyeSyTF2LAPoupWP-ZbQ1wxyoZ2HtxXhi3dxvfa_aEaKfJ3v3ug0TfYxiXd5TVwQpuDReFFS8UZwznAnFJTGGn9dF0kPAAyh8CHPTVqJJgfNstFGyAvnX6VKUZ3oHvHrdw28cEn8mPov90RdhZ_f49K4Dc4fgikcYuDAtaopDZ-eCgIo69KzUyrUfDpjfUN9eltvKvrFfqjw1HxDs1ZVFpMOOMQlzOwCJ2hRnaRlERdvkAdTFZ7dvAP3bzPz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲٠ میلیون دلار پاداش برای قصاص ترامپ/مرده و زنده‌اش هم فرق نداره
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/667370" target="_blank">📅 11:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
صنایع سوده و زیان‌ده بازار بورس؛ دارو به صدر رفت
🔹
شاخص کل بازار سهام پس از بازگشایی بورس حدود ۴۰ درصد رشد داشت.
🔹
صنایع دارویی، زراعت، فرآورده‌های نفتی و محصولات غذایی با بازدهی چشمگیر ۷۸ تا ۹۴ درصدی به صدر جدول بازدهی صعود کردند.
🔹
در سوی دیگر، گروه‌های بزرگی مانند فلزات اساسی، محصولات شیمیایی، خودرو، لاستیک و پلاستیک و یوتیلیتی نتوانستند حتی به عملکرد شاخص کل برسند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/667369" target="_blank">📅 11:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daDQlvoJWZsX7Tu53NdPSyONv7cfuysl8NXjaTg0Q5W_Hx0dOIvxK8dSWXeQmkmBAb6SNdW_4TxyaKF3wlRtgwGhh4129gEMmTR3WvOZoHjT-oVDtq5a-SyaBA9l7fTeA6O32KduRcEyzsA1BJLapnBRewwQ5iALzjIit72x4DhcdBQ6n5pl9VGlcAYBFMcij2y0bmKDLcCLGx6CQxx5VPOFz4WyYkgslJBKNvQ6VNR9g-q2Z117hbhTtt2EaETlc7kRys-z9QlHtYtPN089wb1FyZxd4ASizIy_9lNz-qHpDdFYMAJnwK-L_xTUDGdgOD3hVNBRJXSF7CYZXzs1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حسام‌الدین آشنا: حضور در مراسم برای کسانی که رده حفاظتی بالایی دارند، فقط در اختیار خودشان نیست
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/akhbarefori/667368" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667367">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8044130594.mp4?token=C-BknVv0XeZr-X6EVHTLB9rw1xM3_pH6coDchHHs4tMFs_dZoDzaNA2drvop61eys8-F4TbfesNDmeOUvG1L7ILLiSjAKQO35g1afE0p-8FBPGv6-CIj5-CPgmZyy-BhC-zXDIHMt-913alEWqs-YOdb4ILpfHZqP_LWC61l-Bi154KaukC0C59rOvqNTA6P6Tmx9YI88tYZXwtuX8bx_jGjQzin7wdL25ANYp64Fi4Juan3yaUP6pNrmqbnnMFLWno2ALS35BKkSekQn7_-PWWEhEsmuL5i8NORBR20X-GmuLjP5bRxymkIaAfK9qfSV5zyEzgdNc985IlrQJv0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8044130594.mp4?token=C-BknVv0XeZr-X6EVHTLB9rw1xM3_pH6coDchHHs4tMFs_dZoDzaNA2drvop61eys8-F4TbfesNDmeOUvG1L7ILLiSjAKQO35g1afE0p-8FBPGv6-CIj5-CPgmZyy-BhC-zXDIHMt-913alEWqs-YOdb4ILpfHZqP_LWC61l-Bi154KaukC0C59rOvqNTA6P6Tmx9YI88tYZXwtuX8bx_jGjQzin7wdL25ANYp64Fi4Juan3yaUP6pNrmqbnnMFLWno2ALS35BKkSekQn7_-PWWEhEsmuL5i8NORBR20X-GmuLjP5bRxymkIaAfK9qfSV5zyEzgdNc985IlrQJv0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد لبیک و انتقام‌جویی مردم در وداع تاریخی با رهبر شهید انقلاب
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/akhbarefori/667367" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667366">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سازمان هواپیمایی کشوری از تعطیلی چهار روزه فرودگاه بین‌المللی نجف به احترام یک وداع میلیونی خبر داد
رئیس سازمان هواپیمایی کشور:
🔹
این اقدام رویدادی کم‌سابقه در صنعت هوانوردی منطقه است و برای نخستین بار در تاریخ، یک فرودگاه بین‌المللی به دلیل برگزاری مراسمی با حضور میلیونی مردم، برای چهار روز متوالی از پذیرش پروازهای تجاری و بازرگانی خودداری می‌کند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/667366" target="_blank">📅 11:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667365">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5925dd4ad1.mp4?token=EhJ2XHJBZXYRX5TjYwRFUrYeK7OX-NX5jsEtWG-aTTiJqxRHXirSTLOl1SkdWzxoeMYSbRbZQ51_L92bU4IsKywl80VbCN6HRFFCONriLYo0izEZ_alKBc6NwjK8aNCBDjHLUlWb8UgLz0AEbAnM78yyxPFjv0FbdkAEP4ruCTZ2QdPTg1TCtzYx9VrUDtGWsbCYLfOy4B6PioFKeMFvTbzxmlgMgM7iQ8XhNCZlyt9_2BQ-GrNYp-sI1VXa_pPqcLGxbU5gjO7ig93jNrIlZ-5CX_wx3JrwXAWn7ERcBRrQOfAWFimeXuDBmYA3gMO1MXZ5B9TItQlxougq4gkq_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5925dd4ad1.mp4?token=EhJ2XHJBZXYRX5TjYwRFUrYeK7OX-NX5jsEtWG-aTTiJqxRHXirSTLOl1SkdWzxoeMYSbRbZQ51_L92bU4IsKywl80VbCN6HRFFCONriLYo0izEZ_alKBc6NwjK8aNCBDjHLUlWb8UgLz0AEbAnM78yyxPFjv0FbdkAEP4ruCTZ2QdPTg1TCtzYx9VrUDtGWsbCYLfOy4B6PioFKeMFvTbzxmlgMgM7iQ8XhNCZlyt9_2BQ-GrNYp-sI1VXa_pPqcLGxbU5gjO7ig93jNrIlZ-5CX_wx3JrwXAWn7ERcBRrQOfAWFimeXuDBmYA3gMO1MXZ5B9TItQlxougq4gkq_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم بلند خونخواهی امام شهید در دستان مردم در ورودی میدان آزادی
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667365" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667362">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHaKBy_iBQajr9vgVSkvMsFHJ4sP1xOasAw1b-QzVVraKK_O5fS4QTkroyss8zVTPhXCDOSIjvIAUCBfAemtik6XRklUXoRvhITSmoPPtiUgVe0GNo7HM7MACbwk_k9nvxubp_mRd8fWnMCqz24FlquHbVPG74D-dHHpsfIIiREuCCAZsQy5JGbxTXo7cDr4Y2NUCq7wkc1MPytAYzMDPs0BHS3rkcCGOC7UHSPmOphfgklrYBMnv8TxkBAslK0jWLxlpVrNM6EBirk24czSBT1gDDZB8-usRkof_5WehbHBm6JRctxE77FDNt2WP86nICtv7ODj3uiCC1kt7rMT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
به زودی...
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667362" target="_blank">📅 11:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667361">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3920eff16a.mp4?token=qbJLlyfwVOAATh0rwhQN0cS_oW1N72WClw6hQp23oeh-Flm2FJx8v4Jn8dy1-cVMJcquZsXdYrPbmoyqp_WVf6Dcnf2CKbjfWOewcRIuTN9F9qJrCG1hHnGw9bdbX9JhA1kXC2TzQqXbqLrf7FqTxJlCnPpW7S9Jo9j10RZsRH16w5LqrIBQBuNgvw4TOC-Io3hVPh4ykfGkO6ft0-1vtmYUME-HL15UbE-o_mqS-hAMW_hsPVwVj86pqQwK5L0eo7V2i9pVpLxNLNWVX8ptGu_Y0MaECo3SQby4ROynfhpzCxNDWYJeAYwJ0OE6HSpjGVU9DR64m1QH0hi_BkiLTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3920eff16a.mp4?token=qbJLlyfwVOAATh0rwhQN0cS_oW1N72WClw6hQp23oeh-Flm2FJx8v4Jn8dy1-cVMJcquZsXdYrPbmoyqp_WVf6Dcnf2CKbjfWOewcRIuTN9F9qJrCG1hHnGw9bdbX9JhA1kXC2TzQqXbqLrf7FqTxJlCnPpW7S9Jo9j10RZsRH16w5LqrIBQBuNgvw4TOC-Io3hVPh4ykfGkO6ft0-1vtmYUME-HL15UbE-o_mqS-hAMW_hsPVwVj86pqQwK5L0eo7V2i9pVpLxNLNWVX8ptGu_Y0MaECo3SQby4ROynfhpzCxNDWYJeAYwJ0OE6HSpjGVU9DR64m1QH0hi_BkiLTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدس الاخباریه: ترامپ در مراسم تشییع امام خامنه‌ای سنگباران شد
قدس الاخباریه:
🔹
در مراسم تشییع پیکر امام خامنه‌ای در تهران، عزاداران با پرتاب سنگ به سمت پلاکاردی حاوی تصویر دونالد ترامپ و سر دادن شعارهای ضدآمریکایی، خشم خود را نسبت به سیاست‌های آمریکا ابراز کردند.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667361" target="_blank">📅 11:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667360">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
راز آیاتی که برای هر هیئت خارجی در مراسم رهبر شهید انقلاب تلاوت شد
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667360" target="_blank">📅 11:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667354">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoXV7sMavkKQACFYVDWMNHMhuvzaQ9ZSw7z-VRpZWxXKp-d7QFWDFHyr2Jy9PMGmPhMsS1KTITzrW9JtDTTOOPSDS4WtQg4xWG3t5W-g3KgJgkFHyAA7GtXntQ-RioTY96-3H4o1FdvKJ_SlGuSILDPQb9NpwGL_VInbue2V5uxCi1CJdwGz76rD2DBBIf0jO0GU1C53DpaMLc8QSVkH3YZEqF2v0DfXD_E2Pm6WxBfMMg6mR61nOqqgLrcj486bI9o7JKmoAt61I7iuUxKT6LJvgGAPqBqIA74QpD0iaWMb3EmNyUTV-OxN2_vaIPcrstf8IiG1gGSaIAKKSbXX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2tDsrQ4lp3SP-gMq4azT7XQXM7RMmYmvD8eUD3_eIFGWN12Ez7aEIIV7Fjg8c4KP8ngdgN9ld6UAjBd4j3x1PZiQ331198HwzTvZJJACakTzz-unvyF8YA6pnc6x40zuCrQaGgNfkFKBL6PDddCfwME4svPr4QQwZnweHB2xWf04WlyGyQkMTRO0xomUu_VKzACS7-vR9K5Vd5HmFbrFWqRO0c5uouML1zNwwovvBxkuQc4B82LrGxvk7C2iAr2QbI_wmC47V0zZuKDa2GtCPtGgNL6WfHT0hBi76gJZfrgiJAM8BBsMm6aQckPxARo8nayB2mxyhMu1bcDPeQL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMBx_W0iFeNH2qAlgQ7MwmtJCLDHuSGEsGK-8nP3CZu0Dv4TjyXg4aGDB_bKKBVwsQbOc1vMvJUd61o6yw6iTV3BPAEJU4VN8Iexuoch3loDvmlcb_bnOH88HV-54BwhUKpJg_4j4FWgcWsQikf6GToDqFIftn3c3gpHLKf8kaT6sWq4uLEsZQSQI7osF5Meba8QVB4vveBWE4VRXtg9OIlTa988GnMkiH6pBXMIw7JKmi8NdECbrilY0Afb__e-vj5HAeqjyH3iFN6R1eZ1QAw4HhWdmjyVBjf4_rs5H8gMHpw2s3JKevrE4NDvRJHWSCj0K_Ff7OcSRufeJLpSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icOH8ygo1HNs68R1YeffoaFU5YMu5LeHAbebYPDMLe3cZ1rl7Dy6E4EroDhNffcq-t_NavzI0n0auJuTfwy4K_4WZbj0BCAzcd4HP458kYbsS9Y01-TlXVmsdaqCETf8kUvJPggp2cABSaanxZkgkYB5_YbDiV18q0qV52oOYVlFJB6Ggo-bijpx8AaPFrYuTZ0vH4jQgE6RlHxhKWmNkgQYhlAMmYoiUs8Ut8jXiq168Bv5gqdm9hdygs7pM1UeNAJdNc5nQ-tYnEeW7lVI_KV_YmbEgLTy-ilxy0zAxncyFM5i3FaCFbN6wVgwgcxD1LI5wUxEWdY1n_rSBnDrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJmKbLfXtfdbkgc5cYF8dXad_rEXZtlVySrMoltx7jnC-rX6nz8xnto8RCWa1AEOoiTzzHX7WHgZ4m39xjQwWxWvmtBvgFBWCCgcBYPsLuzGuS_5dIKrneAftRgcPAc_Uj6OSWfMJWguyEndeNU5wzmvszRjfbS63pu0bzsZTJUSpYQwcVsJBwOqPZ_-y-_qYJhxQnKyTndh6eWXX9XUdtnhiwmTSQT0A_YUqlyg6TJRqraoaGqPCzbxke4Ztc8JY6Obcqqx_QIeye97lxNGbDuN7DIaCZa8Wl9GyrrSDuO8JUSA83ffruPFY8ScrtbI1B7wABT3qiXjOZdrd0HtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rp24h7yi5wtl_ZPMtMeloyp1Usyqi67fXNgsmMD_P5HQzdJ5dmAR2IZSQuHGSxQHdyo3GnmK6o4oVK1KiqEzHBWtgCcw-THlXWLi6jzNTlbvHV5DC21fknjJk_6SCRK0QlSGHi3Dd3VDDOgqj-cIXTZC_QIihx3B2XnaRTeAe5fBjJNJe3WZQr4cKPOZ0pzXXj2qBBRqW3CHL0laIGBW5_-Cpjov1-h-yGRk-lU9RPR-T0Kj-kh89czAR8lOz8q49j99ftO9o3vfAuiF-sP1dqlJxyn23IvP5weiRMUiPdGFPWKa8cKek2kjrFDearizuJb5VGw5wIkCnFcw2J2Znw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش مچ‌بند سرخ
🔹
تصاویر مردمی از همراهی با پویش مچ‌بند سرخ؛ نشانی از وفاداری، ایستادگی و تجدید عهد با امام شهید و نایب برحق حضرت صاحب‌الزمان(عج).
🔹
این حرکت مردمی همچنان ادامه دارد...
🔸
شما هم تصاویر خود با مچ‌بند سرخ را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667354" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667353">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a8e16d83.mp4?token=dBl9pophggVFeGPCLbBKg3dIGuwIJ6pvUfIq2FixK46M-BXl_tlbDH5ujmYn97HRTufLTyQv0eH7nLDCfY4C-UaJUMyVgK7_jbBGYBnDwTWWrscKBKUJVa5cqQJYYZcZaVd17ezwlCCC5Qah9Rg8qnDfIAaC57sJA7wbOIhGdP2y2FRKn9WOB3UBVLQH9FYPRFnliGJ-H2Ccte_UphagoM4Kll9W2cDoKZyDmCQWLqELfMgWEe8TK0FK9U4VbPE1N2g8MkahNEyds9Y_zplNdOttkd00YoWdYylkATwUv_iyliK5BSmIkv-WmK8XCNrQ3M2DR7pnhKL6ym66m40siJnyeKkWHiOzR_w68y8M4YTs5c8sJEf41X-Ip9mOUC0RgQ9kbq5V5wyxdIGFJpOMGPAVEQvjWv5kM4jMTU1svqt6LqENyEeM6C8KYRRhs-wsOtIQ9IBwHAHdSRsBG9t84osIkRHbBYWHAc6UPcViSovBqkqx6seH72gCTbQQzVWQqO-Nohea3ggjVcigs5V1eyg-O2mTufdkwg3mdsj6horiDgwNXRILeZaGxj2Vgm6gSVG9_7vx7TKZtVpvhMsFo5mycaoJn4Hn2-dZk0FMSg9M7MX5wmbnaLs5s4YW2v2RHLEilUhtSdBpRr3684op1mimkOpXmKAf7PW7inw-BUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a8e16d83.mp4?token=dBl9pophggVFeGPCLbBKg3dIGuwIJ6pvUfIq2FixK46M-BXl_tlbDH5ujmYn97HRTufLTyQv0eH7nLDCfY4C-UaJUMyVgK7_jbBGYBnDwTWWrscKBKUJVa5cqQJYYZcZaVd17ezwlCCC5Qah9Rg8qnDfIAaC57sJA7wbOIhGdP2y2FRKn9WOB3UBVLQH9FYPRFnliGJ-H2Ccte_UphagoM4Kll9W2cDoKZyDmCQWLqELfMgWEe8TK0FK9U4VbPE1N2g8MkahNEyds9Y_zplNdOttkd00YoWdYylkATwUv_iyliK5BSmIkv-WmK8XCNrQ3M2DR7pnhKL6ym66m40siJnyeKkWHiOzR_w68y8M4YTs5c8sJEf41X-Ip9mOUC0RgQ9kbq5V5wyxdIGFJpOMGPAVEQvjWv5kM4jMTU1svqt6LqENyEeM6C8KYRRhs-wsOtIQ9IBwHAHdSRsBG9t84osIkRHbBYWHAc6UPcViSovBqkqx6seH72gCTbQQzVWQqO-Nohea3ggjVcigs5V1eyg-O2mTufdkwg3mdsj6horiDgwNXRILeZaGxj2Vgm6gSVG9_7vx7TKZtVpvhMsFo5mycaoJn4Hn2-dZk0FMSg9M7MX5wmbnaLs5s4YW2v2RHLEilUhtSdBpRr3684op1mimkOpXmKAf7PW7inw-BUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نزدیک‌ترین تصویر از پیکر مطهر رهبر شهید انقلاب در مراسم تشییع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667353" target="_blank">📅 11:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667352">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHOtt3ij2AN43G9Et1XKsk8bu6xR7P3_Pt6-MVPQiP2p0IfzhZwqU08QeNzn7wzGCGK8-zuggWQP4aUQzwE1ZjKryKTiuV6mDBIENKDyZ-Nik__VsTcSr7sYIHNajrI7Nl0XvjaO0la42J-skhKzmjvfF9bQDKil6sZ9FSrVyqGRthNZ7N1tGEJxMfpXGKxT7SddD1E7yWYtnwkwnIQMrXOPUWxIqdAFRUQPnK7T14Y9nA_Q998YwQumRucWOfE3faB2mTaMIVazKaZ7vHXrbjKz2DMGmCCIntXdb4Yn0gmO5O7lME9rnNssuaJOt2Qt8GQgJLRrQvVIk5K6_wU9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت‌الله نوری همدانی: همه دنیا از عظمت حضور مردم در مراسم وداع رهبر شهید متحیر شد
آیت‌الله نوری همدانی:
🔹
در این چند روز، همه دنیا از عظمت حضور مردم متحیر شد. دشمنان بدانند که این حضور حماسی، تنها بخشی از ارادتمندان ایشان را نشان می‌دهد.
🔹
این ملت هیچ وقت ظلم پذیر نخواهد شد و عاملان این جنایت بدانند که قصاص آنان قطعی است.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667352" target="_blank">📅 11:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667351">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a0deb299.mp4?token=UzQU-CoriXsuqBuLZr9fGyZUV4dE9ZIEp6L6AUDdz32tg0J8LCUkNmhhf_5SisYeNQyue311XVMLA1y2Krc6wH6-kVHCGVoi3zrEW_-Ukyod4JSsLthPfj2o1Gb38OQF1ws5bdEZobzERzl1jx7rCJAh61emKWMqIjWpuFJYb5uT6EuMvkvVONy8NGTOfqeyTyoIWlt798AQmWSJlgrvsmVzJ91F7fxn-dZfwBrGx0GYch-TPmbcrFkk_OThQlhqtCUWQ3P9m-K6BVWBnomWh273VoO3Pt9MwsCrT3a1cl7BQ36Uy4wPwqpPKBrZLF5tVJI2fdCPJ4eUNTrM8XGMzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a0deb299.mp4?token=UzQU-CoriXsuqBuLZr9fGyZUV4dE9ZIEp6L6AUDdz32tg0J8LCUkNmhhf_5SisYeNQyue311XVMLA1y2Krc6wH6-kVHCGVoi3zrEW_-Ukyod4JSsLthPfj2o1Gb38OQF1ws5bdEZobzERzl1jx7rCJAh61emKWMqIjWpuFJYb5uT6EuMvkvVONy8NGTOfqeyTyoIWlt798AQmWSJlgrvsmVzJ91F7fxn-dZfwBrGx0GYch-TPmbcrFkk_OThQlhqtCUWQ3P9m-K6BVWBnomWh273VoO3Pt9MwsCrT3a1cl7BQ36Uy4wPwqpPKBrZLF5tVJI2fdCPJ4eUNTrM8XGMzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲ میلیون سفر با مترو در کمتر از ۲ ساعت
🔹
همزمان با آغاز مراسم تشییع رهبر شهید انقلاب، در کمتر از ۲ ساعت، یک میلیون و ۹۷۲ هزار و ۳۲۸ سفر با متروی تهران انجام شد.
🔹
به‌دلیل ازدحام جمعیت، ایستگاه‌های میدان انقلاب اسلامی، تئاتر شهر، دروازه دولت، فردوسی، امام حسین(ع)، توحید و شادمان موقتاً تعطیل شده‌اند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667351" target="_blank">📅 10:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667350">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8f1356ff.mp4?token=ajKAejthcxqOWS9MbSG2hjGZixEeWOz62BALBqdfK6GRKzsF8SZlRoo_ymYkPc1CkyFz9s9d8TuHHdLkEZ_-xqa41sN0DZkzVC6TxfCCOvhOVwaaiPauBV6vW2Acb8OvZQvil63nu_PXAVGUTrcdK9_KEput3UcJrTtL7dl-gP8t9HfmKfc9VccDRxs5DlOvA2pV0hHp2EiQ6VuiB9w80F-AIQRiMkRLBD9V4IZt86WOWRJ3pZFjBEbIj2CaUdioN_GKG8rxuHAcecRiQUt0EAtG5v-0N9A91WAdRcKzaDh3C3OywBCfuvoU9eBsbac49betRJKveX0PH9K19BmurA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8f1356ff.mp4?token=ajKAejthcxqOWS9MbSG2hjGZixEeWOz62BALBqdfK6GRKzsF8SZlRoo_ymYkPc1CkyFz9s9d8TuHHdLkEZ_-xqa41sN0DZkzVC6TxfCCOvhOVwaaiPauBV6vW2Acb8OvZQvil63nu_PXAVGUTrcdK9_KEput3UcJrTtL7dl-gP8t9HfmKfc9VccDRxs5DlOvA2pV0hHp2EiQ6VuiB9w80F-AIQRiMkRLBD9V4IZt86WOWRJ3pZFjBEbIj2CaUdioN_GKG8rxuHAcecRiQUt0EAtG5v-0N9A91WAdRcKzaDh3C3OywBCfuvoU9eBsbac49betRJKveX0PH9K19BmurA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگفتی بلاگر ایتالیایی از جمعیت حاضر در مراسم تشییع رهبر شهید انقلاب
🔹
بلاگر ایتالیایی با انتشار این فیلم می‌گوید حضور مردم تهران در تشییع پیکر مطهر رهبر شهید انقلاب باور نکردنی است و از این روز جهان تغییر خواهد کرد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667350" target="_blank">📅 10:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667349">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
کالابرگ دهک‌های مشمول از فردا شارژ می‌شود
🔹
از فردا اعتبار کالابرگ خانوارهای تحت پوشش نهادهای حمایتی، نیروهای مسلح و سرپرستان خانواری که رقم انتهای کدملی آنها ۰، ۱ و ۲ است شارژ می‌شود.
🔹
مهلت استفاده از اعتبار کالابرگ خرداد نیز تا پایان تیرماه است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667349" target="_blank">📅 10:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667348">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3669ba8d.mp4?token=ZlMmHp2SlfsMYmwuDe4SaJegpmqtp72_il-XFgK2kjQVWCBz6jdpmr_HftqyGAd9I-Jg-VlxfoGgwS4IXvrh2pEYCQUjYDgqJCqOKZNEkqLH4t5tESU-YHCeQ2oK0oGmN8IUl3f4_KKw8osq7sV-LAWhIez1U4RleN216gh99yDLtkzUmi-dbWhXmhzVHz7MlSS8ZURzVAQ-zj-2ajxCqLzh3bFdI50jC56v4y_6z62pKhOtjs0ZmrCcTj20bC6pOUpFrjaqWnE8zxEkPcOUVwL-Sa4T7BbbcN-jV2TpBWNJaEm2F5Tljn9vArjUREgTmCHiSu907dKq2paew5GHhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3669ba8d.mp4?token=ZlMmHp2SlfsMYmwuDe4SaJegpmqtp72_il-XFgK2kjQVWCBz6jdpmr_HftqyGAd9I-Jg-VlxfoGgwS4IXvrh2pEYCQUjYDgqJCqOKZNEkqLH4t5tESU-YHCeQ2oK0oGmN8IUl3f4_KKw8osq7sV-LAWhIez1U4RleN216gh99yDLtkzUmi-dbWhXmhzVHz7MlSS8ZURzVAQ-zj-2ajxCqLzh3bFdI50jC56v4y_6z62pKhOtjs0ZmrCcTj20bC6pOUpFrjaqWnE8zxEkPcOUVwL-Sa4T7BbbcN-jV2TpBWNJaEm2F5Tljn9vArjUREgTmCHiSu907dKq2paew5GHhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایمان عطارزاده، سخنگوی ستاد تشییع رهبر شهید انقلاب: ‏خودروی حامل پیکر مطهر رهبر شهید انقلاب در میدان آزادی متوقف شده است #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667348" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667347">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYhGxxu-n4F0UcT-Ebx9hF_T43IU3x79_cQrr5HndD1OGJMx_J9RT4nc_EQOBuPzaDjW_cTz5FSYd41Y47_FaJury_Onoql6RvleYEEqRz0CItXk3-ZWkysL7h2-yKXe6oXZ7s0h5-abobNjtT7MPVaiCLFjwbuHz6WSMSV6YgncLIeRaoBC1pBXreVg4I54Sc3BM3lt3HuYa070zzMvOXkb2K_d1VGqk1eTLR_JF-SDYtb2SII0KBSmnWEMJ4BVcGx3hwtHZxXZ0dewnVkALktHsYGLgZY37iYyeyu6pxYGmgnMJQChn4Cq7augT-i2Cxrlh6NdG0A15Ci5-UhdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور اسحاق جهانگیری در مراسم تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667347" target="_blank">📅 10:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667346">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/952e0ba2bc.mp4?token=krVSKiwjK4GUR08lt0zwmHp4oqRy_Aq9FYuDsATNNCb2fR2rBNxUyLUsZkqm6vcFTU9fNlyvdtxkywM7KisSRgkoTje55zQ3Ay_-AGhZrZZ6_PKcqWK3Ef0elDU9vcTogCipV34gS0rga9Fe6XmDu13_cZ4PMbPbcKaHEH9wOCdWw_Gx-HYUK83kv0tQ_KyojFjvao2MaF8JOtTG1bidHN7o3BluC66LT0mNQ8GRXGw9W7n7g7Sm1toQoS0HmXBNoDHp7MGbxlA7eA-SEwLsAgNhP6k6wChdF5sAONcp4CauicuOxHYqkPF6HKXtApMy7r7HcspDGlJsrPmIQl936g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/952e0ba2bc.mp4?token=krVSKiwjK4GUR08lt0zwmHp4oqRy_Aq9FYuDsATNNCb2fR2rBNxUyLUsZkqm6vcFTU9fNlyvdtxkywM7KisSRgkoTje55zQ3Ay_-AGhZrZZ6_PKcqWK3Ef0elDU9vcTogCipV34gS0rga9Fe6XmDu13_cZ4PMbPbcKaHEH9wOCdWw_Gx-HYUK83kv0tQ_KyojFjvao2MaF8JOtTG1bidHN7o3BluC66LT0mNQ8GRXGw9W7n7g7Sm1toQoS0HmXBNoDHp7MGbxlA7eA-SEwLsAgNhP6k6wChdF5sAONcp4CauicuOxHYqkPF6HKXtApMy7r7HcspDGlJsrPmIQl936g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاب خبرنگار رسانه النور لبنان از حضور کم نظیر مردم در تشییع امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667346" target="_blank">📅 10:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667345">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4nXhUaO__b-p-chqC868qtwZSSmM562tITbyv9gw-2q7qSWFxgtLGYDqhh-3IOQheNsazLPP-LfesLRKu-HNegGPZtRRGb-AwGcwz_huhPP400yTd5G0wQcb6-JPQK7NyEbhXNzyiyr5KMH-OduTpa23ZFdNjFRIWZy6KgabjW32PEMbqe1QkSdF1cydGuSQ7xoDGH6BiPwUVmvldbRoz-uACn6tXsLMANvBEjMCMyfctajVp6CLaNrkUBgHHba54EG9mpBCQpWg_XEh4RBhRtVYkP0d-V-BuuDX-XbZEY6Pk5LNNyGXbHfoHbFonpl6zpdJU3aCPwuNfTYc8gnhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خودروی حامل پیکر مطهر امام شهید به علت ازدحام جمعیت در خیابان آزادی متوقف شده است
🔹
تشییع کنندگان می‌توانند از مسیرهای اعلام شده خود را به کاروان شهدا برسانند.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667345" target="_blank">📅 10:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667344">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f51e24ed2.mp4?token=WbPvZljHeZq_jZHug0ZdGFcjCgrVaCNuuC7zlV8KLHoL2swOdsUf_esBFbxgfQWd7Rjt4bhaiDS9DT-GD4GvjoNpiHi7pWkyRI9v8TrbmKkDtzzti97FlEybxmCtX5lPDDGKUELx7hgQatajD2PixLoNdSqV_aW4C7r7fXuz5piqGUyBOqZAS1cyStKByF-3wp03Bv1PbUE67a1cMn-AsHbuVNU2jU1ktQG5NBBjoccwM3JpRG80zHl6_zj99iv4fM9fp7QsTgzYTGwPiSAcxe0FASWr1mDNNg0SR8RDMeNPDH2UdN7MYR5dOW5uZT8-2CUo7nk3V2BEKPRRaRvBcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f51e24ed2.mp4?token=WbPvZljHeZq_jZHug0ZdGFcjCgrVaCNuuC7zlV8KLHoL2swOdsUf_esBFbxgfQWd7Rjt4bhaiDS9DT-GD4GvjoNpiHi7pWkyRI9v8TrbmKkDtzzti97FlEybxmCtX5lPDDGKUELx7hgQatajD2PixLoNdSqV_aW4C7r7fXuz5piqGUyBOqZAS1cyStKByF-3wp03Bv1PbUE67a1cMn-AsHbuVNU2jU1ktQG5NBBjoccwM3JpRG80zHl6_zj99iv4fM9fp7QsTgzYTGwPiSAcxe0FASWr1mDNNg0SR8RDMeNPDH2UdN7MYR5dOW5uZT8-2CUo7nk3V2BEKPRRaRvBcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت الله جنتی در مراسم تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667344" target="_blank">📅 10:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667343">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed1NbkmABWtF9SuSxbnIcjSVEI_v94TaseTszmn3x6n2KIz-n9RYW0Miq2Gk3tqM6oZYNJBNy1vRQ4qJC6JuwPSjjEM6KVdm8i2tD6IHBQetixGcn1J8y8z_Zc5s9GMF7Mng2EgWjfGZL0vmq1UfARJBzRkWcNSsCcfbUA_nkkdQOa5RAB7DyfP149SuR90oLAA9k01oCbvE7RYGaUQGFVNekVE-9_SHWyR2-ypiLnHJvfsYrKISO2F14b7f2Aem-zw5wAGT8-WcYVPMQmuGfojLmXedKwr36R-8WxYGN2OdgeFNJa7h5SOd6bi3GUahRk7m4c5ChqQ04CYaL4QN7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌های مرکزی سالانه ۱۰۰۰ تن طلا خریداری کرده‌اند!
🔹
بانک‌های مرکزی در ۴ سال گذشته، سالانه ۱۰۰۰ تن طلا خریداری کرده‌اند که ۲ برابر میانگین دهه قبل است. بر اساس داده‌های بنزینگا، پیش‌بینی می‌شود ذخایر جهانی طلا در ۱۲ ماه آینده افزایش یابد.
🔹
تحلیلگران معتقدند ادامه این روند، می‌تواند محرک بزرگ بعدی قیمت طلا باشد. ۹۲ درصد بانک‌های کشورهای در حال توسعه، طلا را سپر دفاعی در برابر ریسک‌های ژئوپلیتیک می‌دانند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667343" target="_blank">📅 10:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667342">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5hVrtZGi-5_sM0awT6yTvVYXuKAwsXrHLT6v1rKmmXs5Dqb4_C3BLc8dJ7JNQ-ldzaajedg4H5H3OR_lSLfbLYEmTC7m0d_HTTYWGbLpZSA1h5TGZOESkYl4RPzR_pDxu0OG9A2azeQDtSpUoPYxmsS6ehzrMkfNliv0TbJkdqMuvRhBCWA5yB_FPDPaoxsdtytKhPIEuXPt2yNZ24h2TAhr7eeWEeUhvYgQrDWKasIbxaJheLtaDwGI9c58cC03MqvP37Zf3R8Qq5z8u8Lsg5MHZMXAjZbTp-BAhiaRov_NoPGWX_oGz3iTUvtiQU5Vu9ZNu6gLHgoOy4y8ZvRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور محمود احمدی نژاد در مراسم تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667342" target="_blank">📅 10:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667341">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8204e18a9d.mp4?token=PG2iLHaYUiBjkn4FoE8gGRfMpbQmCrGYuSgPUi1PCK89TsMKVDPPjD770l8XxwHtaicJPdjLdS6Ka7n62vZeEz-1l0i98CnCzRWW5Iq9hoJpWuC5cjFu0CDVxajxm7nuzbN8plZYYK7kskmySBSlbmOJ0sdze_4f-CGF5qe8r6zc3-WMSnN6TqURia3S-YXTcVoOvgb0Ue2TQzb0q_B4TAKtk60h2pK_x_lWdK09StLQK4LtKYn8tBNPR0cUSIhkjQhiY_m4DPZm2r4_lKcCblzt-NLBzFzDOE1XnrhpOnZTGgnQn7p_uoa4LQZ5w0Hx7Yxwt57fKxf1SoQBLnQYjpfmVhAUKTNbyVTLIL_WjhAHme6Kp0sFq1yudV4pJKZB-Ei5ZyY3fPuHDbW17Qvt8G3pzeaHIkmOHqBWRaiEOzsTz1KvEEYuLSmlJPpuX4QwbG9pYTcP53f2Gz-yxXtDLRe3tpZvM7JoA9ET7nFhdE_IbefpamicaKQ8HQVu9XJGA3SOYn4lbN6v2UU6KcRAEMmL3sOCSGf-p67yTbRNPfNBCtluT2TagsqRcUiy1PffSISwmju4F2bsul7F8sIM41_AjeBzTZUXU5MNbEI_sy3jcMbXO8zBgE4e3EI0V3nZVf4MgK4bNg2ZKiq4XV07NwtmgDUQzCJwic4p7sbSzME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8204e18a9d.mp4?token=PG2iLHaYUiBjkn4FoE8gGRfMpbQmCrGYuSgPUi1PCK89TsMKVDPPjD770l8XxwHtaicJPdjLdS6Ka7n62vZeEz-1l0i98CnCzRWW5Iq9hoJpWuC5cjFu0CDVxajxm7nuzbN8plZYYK7kskmySBSlbmOJ0sdze_4f-CGF5qe8r6zc3-WMSnN6TqURia3S-YXTcVoOvgb0Ue2TQzb0q_B4TAKtk60h2pK_x_lWdK09StLQK4LtKYn8tBNPR0cUSIhkjQhiY_m4DPZm2r4_lKcCblzt-NLBzFzDOE1XnrhpOnZTGgnQn7p_uoa4LQZ5w0Hx7Yxwt57fKxf1SoQBLnQYjpfmVhAUKTNbyVTLIL_WjhAHme6Kp0sFq1yudV4pJKZB-Ei5ZyY3fPuHDbW17Qvt8G3pzeaHIkmOHqBWRaiEOzsTz1KvEEYuLSmlJPpuX4QwbG9pYTcP53f2Gz-yxXtDLRe3tpZvM7JoA9ET7nFhdE_IbefpamicaKQ8HQVu9XJGA3SOYn4lbN6v2UU6KcRAEMmL3sOCSGf-p67yTbRNPfNBCtluT2TagsqRcUiy1PffSISwmju4F2bsul7F8sIM41_AjeBzTZUXU5MNbEI_sy3jcMbXO8zBgE4e3EI0V3nZVf4MgK4bNg2ZKiq4XV07NwtmgDUQzCJwic4p7sbSzME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزله خرمشهری‌ها در مراسم تشییع رهبر شهید
؛
تنها چیزی که می‌خواهیم انتقام و خونخواهی رهبر شهیدمان است
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667341" target="_blank">📅 10:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667340">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGDgfVXzHjc4CPutjsJOGPaAqvhJrLS39pOcKYHzAfRhOmXxgOx5cAHv58hNAOSSuUqYVmduhJDTpoYGoGAcwat-E-IezSZeNpgW0KbhydtRjCpvSdKeEbFAs3G8yWyH4p_cT8NRyjU9SnMaNNXvX8WBN7uBrb0dmDp8Uz35PeLBhlnupy09r5b4_A1TO9d-BlHNzusDSlA_rrxgSm7heScg8FXNYZUmKUyxwosKuwdkUhDVB8h1EV3VJSddUVodbPUGOo_QWQM39ziNWLi9bDkG0-MdIKXmVLXnjjkpaDXHOizjhIkE-7NeSLU8siEaJ1DMD5nea2ig73N6d9PTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اطلاع‌نگاشت‌/ مدیریت لحظه‌ای و هوشمند سفرهای جاده‌ای در مراسم بدرقه باشکوه قائد شهید امت
‌
‌
#چشم_به_راهیم
#باید_برخاست
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
‌
🌐
@cheshm_be_rahim
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667340" target="_blank">📅 10:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667339">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d1b7fb3b.mp4?token=P2ETJL-_sGvkoI9sF0uSIVwhxOvNnvN09WKxbuWugA2dhCnZoVYVHy0t0BQf7vNIHccneTZwQlMgwNDo2oSDV9bpXFVXXXtjGm8c3Q-V6DbiO70GcD3lcY5dOOlH3L7B8g77XHXs89LcotvU-D-bmFIzY665EtKmjZkvmYnMYIoSJ1BVVh9KAoO-3H5x-DrspS7JTWlhifwJgAnTxX07m-g4d26AKyZy9OO3H3IxaEtuJ3B0Q3tucpxj596mzZ9D_-opQvYOw1OnfVs2tyFxdi_vmdI1EyVlhr_jUuTHXnHEgRVUtRm7JKmj90dOSFc1LVel2orwpfMSdU2gLStIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d1b7fb3b.mp4?token=P2ETJL-_sGvkoI9sF0uSIVwhxOvNnvN09WKxbuWugA2dhCnZoVYVHy0t0BQf7vNIHccneTZwQlMgwNDo2oSDV9bpXFVXXXtjGm8c3Q-V6DbiO70GcD3lcY5dOOlH3L7B8g77XHXs89LcotvU-D-bmFIzY665EtKmjZkvmYnMYIoSJ1BVVh9KAoO-3H5x-DrspS7JTWlhifwJgAnTxX07m-g4d26AKyZy9OO3H3IxaEtuJ3B0Q3tucpxj596mzZ9D_-opQvYOw1OnfVs2tyFxdi_vmdI1EyVlhr_jUuTHXnHEgRVUtRm7JKmj90dOSFc1LVel2orwpfMSdU2gLStIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ قاب هوایی از بدرقه پیکر مطهر امام مجاهد شهید توسط مردم عزادار سراسر کشور در خیابان آزادی تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667339" target="_blank">📅 10:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667338">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
خبرگزاری هندی: آمریکا ۱۵ کشور را از حضور در مراسم رهبر شهید ایران منصرف کرد
خبرگزاری هندی (ANI):
🔹
حداقل ۱۵ کشور در اروپای شرقی، آفریقا، خلیج‌فارس و آسیای شرقی تحت فشار آمریکا، یا به طور کامل از شرکت در مراسم انصراف دادند یا سطح نمایندگی خود را برای حضور در مراسم رهبر شهید ایران کاهش دادند.
🔹
گفته شده دستورالعمل‌های محرمانه‌ای در این زمینه برای سفارت‌ها و مأموریت‌های دیپلماتیک آمریکا صادر شده بود./ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667338" target="_blank">📅 10:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3106edd7.mp4?token=KCI6lvqg3BOjeAhee-tHyTg6qsjjRxGzA7fK6TwfOuQSDMLHuKKy68UNpGsKvRgKihMFtXJSvJaxKTv4bvIDTAvO8GjNj1pPIteoqw6shYtsFLoZkdLNf7GqTyg_yXDe7LQRoY_aMhN7ZiKkwZYAtd0tyZsqs1LpRyC_HPrqhG5L1ecGoPjAsY9TGVxfbH2U05Eo8GrTz8iPY-K3jWEbhafaDwLoz4EBsy9wE-zt3aQoitkGKt3dYjT133D-aUqpesOE2Qr5u-JyWbClygfWQ8qTbj6_x9VKMc9t9r6aP20NfaJtdwxGH6OD41MpBtQuQ0zwpS5xFlzKoZMsw7y34g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3106edd7.mp4?token=KCI6lvqg3BOjeAhee-tHyTg6qsjjRxGzA7fK6TwfOuQSDMLHuKKy68UNpGsKvRgKihMFtXJSvJaxKTv4bvIDTAvO8GjNj1pPIteoqw6shYtsFLoZkdLNf7GqTyg_yXDe7LQRoY_aMhN7ZiKkwZYAtd0tyZsqs1LpRyC_HPrqhG5L1ecGoPjAsY9TGVxfbH2U05Eo8GrTz8iPY-K3jWEbhafaDwLoz4EBsy9wE-zt3aQoitkGKt3dYjT133D-aUqpesOE2Qr5u-JyWbClygfWQ8qTbj6_x9VKMc9t9r6aP20NfaJtdwxGH6OD41MpBtQuQ0zwpS5xFlzKoZMsw7y34g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پل کالج تا به ‌حال چنین جمعیتی ندیده بود
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667331" target="_blank">📅 10:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667326">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P20FxI_uusMmlhllkkOhXry7YfGKsOprN5myEd5bScedpwwcvROUIglCkdDIS8jIBE4UPiXC5JRKAiNmWXdo0hlm6020vjTM43fCyAh6oRHg5kTEaQr0u7qStg2rgOgxli0I2iO88aXhAqAyDyPQpszVs3dV4yJZ2g6Q6ULLMrpc-pRMc0GRySoSDzhQp4KrzJj2Em0nQmYoXAMh81i6i0rS8yGFtMaDUQKC81hcqfSiq8m5N7MOQnsCgEuzMO5VUZ7d0Y3buqZ95APpF3GeR95T5EZT95jaWfPq4pXraQIYDchyvfRO5FQBS1A-hx732GOqIzkT0ponsJBPZu7dUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGDyCM2Jd08-IZY8vQOyJKa-IId10KcOOyajHPk1Lt8JSxei4YExMJA7DvOQYEK05ZWMfdkcUbZMGyrXjUYOHsj7dpJQnroJOEr0ZQkg0G1OefMwKqSS_0UVgfdk6wZ1I7gMyCQ3vhFSs-0Gzi-ZCSrFoB9Vbi_lOVyQGewD4t6wx8RNkmuK7r1lc-u_D5XhcG9Y464UqnpUTLT8cApX_mPUfZjHYjHdr6uyttVMNTH6IwD4CJo3486FmADpLWpkRvKZZAhNu0dUh-8kZhkbijuiOitp-yAaTG2yfpwhNdaULWckWiZk52Q28q8GgUZJpt7x36bX2wPRA6SnuY8TFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWKPU0Id7Pp4nZ6TorCTv6XAZipIv0zx1GRZ--Jq4c2qrxJhvIzaXIrI7u1Jxtw8uVO0LD54vZqh4U9qb3JyeMx-bNQOlaUDHa-lGm-jvfj7BIIcMAmNfwblxf-n9BanTGmqTkndUUzQ0Dl-zQjeUHN0ZpUJ4gsdNMFG7zdKhzd5olpaOsaEDx9ioeLc_-Tr6vGWQJAG9ZopUqj-M1E0TjncgV8Ud78IqFfjCw4V6JXKBIWiZP_iGCB7AiUdvwQI6XTgzpxXSCh435SRQJacjm3kObsEURinmmeeN3m5Uh8qIL1N0EVsvrKJPUQ49Ximw86e7uBMVEjM_52TNoxl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRhMB8S0Zp_61aNU1IZlCj6wUXrxFCaO4sIuenBAlXiCUWmipWZX79ww7m6112N1UK8yqClcre5wcBlRQxkwIf-92_XAsR1cFR1IXfFOoS5SlhfJUlZt-zZdbkFwhidpfGDREteMwvs_3Pyi6_36uAa27v1_UoaAKigE67mvKNZiFU2IHqwptb4gs7CxYgtToekMMxaedFchszG6LmVQmp8ZNEtvMhnXLqgj6Tkd5rxArHF-rSxw2blPkadIIsOokhCZDcG8V5Drk0wS0Ci8ubRy39g9HMEFdI_ZbPZ8PprXRhFJZFL-1CwMcVli1mkJdKAr3Tk5-zOjiZf1GRc8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtABg0QKh1gyuLUHwZ4h97UsFThOnt552kCEXen-8swY4a3YDFTVef8DzDZHhLEj9mrgLsrze0uQ0lPbmhqXezf2xa0TtbcmLM3vanWJt31UfZ4xjxHgil9eR4uc3vBgcJcsYEUTH6vbmkWTHUKcgeKw_PxXXP45faLCLJtmtrB_n_8iNaiebFeV2Q5gwgJODT2it6NN_bclAIh8IRfBeYd2BF7O9ginmHMAZ0i_j0JW7Vk_a2EoZ0HTO-pBen8gSOFg_hXKg8cnmySdgCDQPrSogGIFslOHJCfMlVIJIBx0MXberrcUf8HbZwFORv-r233IdXMi0hwpd6dmRLkedg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ تصاویر هوایی  از حضور جمعیت عظیم مردم تهران در تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667326" target="_blank">📅 10:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667325">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
شما شنونده ۱ دقیقه روضه دلتنگی فراق هستید...
🥀
🔹
روایت کوتاهی از دل‌هایی که در فراق رهبر امت، پر از بغض و دلتنگی است...
💔
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667325" target="_blank">📅 10:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667324">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
المسيره تصاویر فرود هواپیمای ایرانی در فرودگاه صنعا را منتشر کرد  شبکه المسیره یمن:
🔹
با فرود هواپیمای غیرنظامی ایرانی و اعلام نیروهای مسلح یمن مبنی بر ادامه دائمی پروازها و مقابله نظامی با دشمن سعودی در صورت تلاش برای مانع‌تراشی، رسماً نبرد برای شکستن محاصره…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667324" target="_blank">📅 10:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa4bd5f908.mp4?token=TiCtcpdoKSP9-fIJTZqzRhr6hv631mypeCM-If4wSUUP3N5RUSJXr7g8TuKxHadsajhBOU8twKYO6jyNvT_54n9tow670Rdo8auh5flvTmgPO_g7Xwph3edLsQNeFbVC96dnbBoub3kd_3HSv9XIm1qpBt9WNH8_SW-KWJlVLgBi-Vn3lqKimW1jt3NWLHOgh4URiCrpBOVW5D6SxrZXVC6MEddY1vrKNymLNU3x297XqBQGYJKvAcC1lfUZVyFqV5xla-PI5Pr9dhMp3XQbsllDFsyW-KCTkprSZIkuvxTS5PYUXdeABkXbt0i2HI_d8LCaxD9i2kkZiyWTf44pGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa4bd5f908.mp4?token=TiCtcpdoKSP9-fIJTZqzRhr6hv631mypeCM-If4wSUUP3N5RUSJXr7g8TuKxHadsajhBOU8twKYO6jyNvT_54n9tow670Rdo8auh5flvTmgPO_g7Xwph3edLsQNeFbVC96dnbBoub3kd_3HSv9XIm1qpBt9WNH8_SW-KWJlVLgBi-Vn3lqKimW1jt3NWLHOgh4URiCrpBOVW5D6SxrZXVC6MEddY1vrKNymLNU3x297XqBQGYJKvAcC1lfUZVyFqV5xla-PI5Pr9dhMp3XQbsllDFsyW-KCTkprSZIkuvxTS5PYUXdeABkXbt0i2HI_d8LCaxD9i2kkZiyWTf44pGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم در تشییع آقای شهید ایران به شیطان بزرگ سنگ زدند و عکسش را پاره کردند
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667322" target="_blank">📅 10:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
حضور رییس قوه قضائیه در مراسم تشییع رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667321" target="_blank">📅 10:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667315">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwveaxKNFJFws3FwqZiNqNV150Q3nBO_5AVnhsTMnPw3q6xTaMptd2rFo_YGNcFEDkjh3U8xRcc3gHcLd9ZxQB60GV4hydYRRFawxw4h8MEPU7a8HOOqHuuIHqEi8AQwt8vLYpmI_N8TBTjI0jBwXFeQerRsOlCCjexmgtaHj4LqSZVN4an4clD-X_7oiZGLrv_C9OdflFflXOTtjSeVIt6TmDBDoMIyFKtLMhhrHoUMmOca40RV66QQ_aMmL0JQ013hgwN-9q3XJ2zQ6yrLHzxurTNol32tKW-OC2sUxM_iQ9LKnNxYQc7YkxzwQKFHlc2_92VHCUGl2m5V0oVWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZOx4kvwLvi7tgZa1vSkYMALK12ogvHLVDDRPUyvaB2dbXYg2sXqC2_KzEHbABDvIY-r7RT8Qu0Ap3PIA1rX-BP4TWQNeavp2FKi_3GQzYd15mkN85TZCkTLS5Hwba-9kXe61cy1GO1KSOch-GMeO6wqlXH97KywO0zO2-jWVO4B0whNN-Ib1u0i13ZPGmZSlPGOqbynNtzVv7hv_CKTPokHVqw-vKyOCeeSh7Dlsiuim-ksqtPcaeQETCoJoETBWHwDIDKLYAYSea3JbO2SaLfk1KLkSvdtTAURrD9MON9Z13IlJrGGYvmbscVx5QncFh92rLlUAKruDLyexIgbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVjfmT8JJyci1h6qnZf89pYBbel6I73W5RF6hPgGxRgtkCJWXrov_Dv40V01xOvDM49fyzkqn7pZs_Hsha2iXADojIB5LRxbwJwJw-uDqTTyLhiNctJ1RDKPcQt_gyDqDm4aFRWuHw211zUfs8xE7_1f0lHRnLF2FAPA8qObpGxY1qu10kkD7OcFGoq9SE1WEDJEC8YbNXUpkY5la3rHy--pqL3ZWrJdkA8Ogjurz5fQu-fAoWkS_Gb8mvz7BZ9NskU84SSROpFm4bagQ54n-on1x1wAOa9VWk9VKJKZPZLf4wscmnBcbHJJM6sMXO8zHHDEYnjI5MotOlol3r9D5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXMv_uig4nUmSlF7dCw9JgQGULBnREqkvPg84QNyPyDirvucFNG5A6yssgwbaOKavGYizpFgwjIZgxsODDxshHAPYpPrl1w7yTj037o6ICg3MA9mxuWR1Ro7O0v_iuoZVqiTcpj7ZzgNsIn2YHEq5caCz1-fMKUiOBIwzlHQNmuYrNr3W6NPr6kIyJYvoKW6YxG5Eu3fT85FTRIEauhM8K4qDENMbfoTMgv8O8a17PZcd7weGLVzT4O22AHEXSpwd7Zz0asNWJWGz90CJ9J_BUfYx_82Fr3t3mAPhAL2VMsLb1kxiSrf9uunphP2ZDe4GbhPN4e4rHfILXN3O38iNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbTZhlXyZbegHva2k-Bw2H0IcqLmemdMfMS5lWZYYEasfnUr5I4sE_njUzKb72hwpB2-eq1-mU7TeY9odIxB7jy2-qOPUaBEWNsYMTLqujBA3iXSw4wzu2dt3aInsQVd3gfY243qBaHx7bLL46kmGiSv4UwyHR6cJ1rkBrUMAAEeYdpMZLYKF8crvqEn814ngd9pBG8uiZeroXE61ddMxefILVaE1FmVnpBgxMvW8fZuqGNgS-U_Ehe46FfR0KHwqxuq_iDhn4Qol1YIVYdaPrprnfwSyuWTcUvT1i5HuxB9wwpOljBmtbrP96z5f-uGOXTtaBEVSun6_6zqeXKFYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab365b2d7.mp4?token=H6w675Jti-ZXIAvLAZzZPW09ZW-XNQ5EPsCtSPrsX1xSxxVshjVm9VIRbTFr4SJxQRUade7ylMsRQsOlq2wQRRlFAJK69U-hZbEcZAM3VMpsmV3SMfe5DkoYRMtsWTHqV4ae_QMiVX3GzCqGbymzv4gREOhn90LqWfhYWt_ra75POBj0SR1nqqm111rQzue5vSn7HcLjw8snKRSwgvPFY07qQva8hBUnmT3XrRI3cspWnruIA47BMfI4nZrTDsL2Q_Zjgo-pWmnFL9SQEP27jTzez7im2bcOajvho2jcuoVHhfKEz8OY661rYQV-_FlbzRMC_8IcXRNVi1JlwNyJbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab365b2d7.mp4?token=H6w675Jti-ZXIAvLAZzZPW09ZW-XNQ5EPsCtSPrsX1xSxxVshjVm9VIRbTFr4SJxQRUade7ylMsRQsOlq2wQRRlFAJK69U-hZbEcZAM3VMpsmV3SMfe5DkoYRMtsWTHqV4ae_QMiVX3GzCqGbymzv4gREOhn90LqWfhYWt_ra75POBj0SR1nqqm111rQzue5vSn7HcLjw8snKRSwgvPFY07qQva8hBUnmT3XrRI3cspWnruIA47BMfI4nZrTDsL2Q_Zjgo-pWmnFL9SQEP27jTzez7im2bcOajvho2jcuoVHhfKEz8OY661rYQV-_FlbzRMC_8IcXRNVi1JlwNyJbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیل عظیم عاشقان رهبر شهید در میدان انقلاب
🔹
تصاویر خبرفوری از ازدحام جمعیت عزاداران میدان انقلاب در مراسم تشییع پیکر رهبر شهید
🔹
عکاس: فهیمه فرخی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667315" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667314">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8bb0513b.mp4?token=LMt2nBQXmqV7CT0Zmn_-8Z9lNVajQL0O-2Rx8_X6QU3as5YQII76wHXXHyjxgLHc3roKCnlBSoljhYvDWxbhFLI0_E2UjPZVmZ6ecUoDRpJkg17hs3GnGKFRVrvktXgxIxGEhRBbmCrDZ2ArvsICIEcSWl4bmFb9fcx_5cmJORi7kyTxeHiEjHE4IEZ0SHlu50FV6NsFLyckLoDSJODBw95RM1-D59le6RKkl8mAJn8e8wlnJHu419072edB4UZK38F9GDkMJVajbRkFR9e_GijZklM6plrDspssMZdWb9f-XUiEABW8NLQrUZcDEMZ80PXokJweUNYvOUhidik--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8bb0513b.mp4?token=LMt2nBQXmqV7CT0Zmn_-8Z9lNVajQL0O-2Rx8_X6QU3as5YQII76wHXXHyjxgLHc3roKCnlBSoljhYvDWxbhFLI0_E2UjPZVmZ6ecUoDRpJkg17hs3GnGKFRVrvktXgxIxGEhRBbmCrDZ2ArvsICIEcSWl4bmFb9fcx_5cmJORi7kyTxeHiEjHE4IEZ0SHlu50FV6NsFLyckLoDSJODBw95RM1-D59le6RKkl8mAJn8e8wlnJHu419072edB4UZK38F9GDkMJVajbRkFR9e_GijZklM6plrDspssMZdWb9f-XUiEABW8NLQrUZcDEMZ80PXokJweUNYvOUhidik--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی دیگر از  تصاویر هوایی حضور بی‌نظیر مردم باوفای ایران در تشییع پیکر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667314" target="_blank">📅 09:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667313">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc389bb94.mp4?token=u2PY8ujamV9grVGZA49WDzP-wnuMMCFbeA1h1mdWot3thVeQmWb1j4VL2_X8P_imc7OdZswXUC4dQWL-3ev47MBaFhpTptskuNd-eh-fis9TsYSEEV98LqRhVyivfIR0tJ9p0U7XtcCuKF2qysOHrwXz3no8z6sWHCXsAkWEckMRrlQBNbNLjkiLTi1GQ6YPvGwof_KpZExmmbRppWKDtTQ074ZIILw2tk-V3_8ijFTSlhkwEEwjZq5yKtskOW66iEhbB4SL6X-bbiNX-dJSs9gQSYMi3AUJj8LjhHzCLYitfL1v3auVVunR1e6dpJSTCFJ70x17Q9RIkf6xCKIuyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc389bb94.mp4?token=u2PY8ujamV9grVGZA49WDzP-wnuMMCFbeA1h1mdWot3thVeQmWb1j4VL2_X8P_imc7OdZswXUC4dQWL-3ev47MBaFhpTptskuNd-eh-fis9TsYSEEV98LqRhVyivfIR0tJ9p0U7XtcCuKF2qysOHrwXz3no8z6sWHCXsAkWEckMRrlQBNbNLjkiLTi1GQ6YPvGwof_KpZExmmbRppWKDtTQ074ZIILw2tk-V3_8ijFTSlhkwEEwjZq5yKtskOW66iEhbB4SL6X-bbiNX-dJSs9gQSYMi3AUJj8LjhHzCLYitfL1v3auVVunR1e6dpJSTCFJ70x17Q9RIkf6xCKIuyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر اکرمی نیا سخنگوی ارتش: مردم ایران امروز حماسه بزرگی آفریدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667313" target="_blank">📅 09:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667312">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b5806c9c88.mp4?token=YgnL9CiVuJoSvGCtDNg7aLRLY7TQtPz8X33ZgliByN1GVKTEGQ3Ejf7LZafNg4H3TkIymcqwkYZxC7QOL7jHgz2f2WWd3McPDE0EIIzMRf4BXmBn5zd8Wp4cQF4MEmXho0NG86o0BhstgjvL9VutmoviWvVu9tum0PqBCUVEwcWAZUIKwEj_23yn1-5xKC5jN4ddTMSBG8HP0KfS6G5a1EIpdnfs1f_41siDM_-HPNVyS3dUP_xZK0BAxK1yGd-HM4YK2shrXsFdGG2LtN9pG4lSHo-jwzQHmqcn9EmB34tZjStz9AxrD6aFEral-5PgprKyAhreU6DKy-pDwGA5FDcA_Nf1j3TyM_agfsvcntR7xewHINvy8O6S9ow6LCNJApB9SrAlqueNIY-FHosWOcjsGK4cf04ywgw9aoSofXz7nO-1NZOfiuEEU3HRpSG9SQzUpqV2faMg3ZODINNyY6bliNZKlve2uiyFQzVz1wDZcbMShhhSyAH9azyCd3BiaEFGwKYLZkpwO78ErmG6HZBqbUaz_kS3eZ20e5ZEUY6Qp2-PF50sL7pHJ6iZZOUd2z7a2uGRo54B_9BMXLVFVlj9yFfRPpESh_qah8ybnzbYkVIwMfzYQZyyxpxMNsOlrzUW6MslKSXZn83sBsluev75SPXmy4Egmr-jxTmEvc4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b5806c9c88.mp4?token=YgnL9CiVuJoSvGCtDNg7aLRLY7TQtPz8X33ZgliByN1GVKTEGQ3Ejf7LZafNg4H3TkIymcqwkYZxC7QOL7jHgz2f2WWd3McPDE0EIIzMRf4BXmBn5zd8Wp4cQF4MEmXho0NG86o0BhstgjvL9VutmoviWvVu9tum0PqBCUVEwcWAZUIKwEj_23yn1-5xKC5jN4ddTMSBG8HP0KfS6G5a1EIpdnfs1f_41siDM_-HPNVyS3dUP_xZK0BAxK1yGd-HM4YK2shrXsFdGG2LtN9pG4lSHo-jwzQHmqcn9EmB34tZjStz9AxrD6aFEral-5PgprKyAhreU6DKy-pDwGA5FDcA_Nf1j3TyM_agfsvcntR7xewHINvy8O6S9ow6LCNJApB9SrAlqueNIY-FHosWOcjsGK4cf04ywgw9aoSofXz7nO-1NZOfiuEEU3HRpSG9SQzUpqV2faMg3ZODINNyY6bliNZKlve2uiyFQzVz1wDZcbMShhhSyAH9azyCd3BiaEFGwKYLZkpwO78ErmG6HZBqbUaz_kS3eZ20e5ZEUY6Qp2-PF50sL7pHJ6iZZOUd2z7a2uGRo54B_9BMXLVFVlj9yFfRPpESh_qah8ybnzbYkVIwMfzYQZyyxpxMNsOlrzUW6MslKSXZn83sBsluev75SPXmy4Egmr-jxTmEvc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار العهد در تهران: ایرانیان خواستار انتقام خون رهبر شهید هستند
خبرنگار شبکه العهد در تهران:
🔹
ایرانیان با در دست داشتن پرچم‌های خون‌خواهی، خواستار انتقام خون آیت الله العظمی سید علی خامنه‌ای رهبر شهید انقلاب اسلامی، هستند.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667312" target="_blank">📅 09:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667311">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
نمای نزدیک از پیکر پاک رهبر شهید انقلاب در مراسم تشییع در نزدیکی میدان آزادی تهران/ خبرفوری #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667311" target="_blank">📅 09:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667310">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e090af8ab.mp4?token=D03qNstf9PRZb_B1b4XQ98y-rtTrO3AmG0QwXtBypEXJTH7-v-TQlRzoglPWZcQOLarr2wRQblQa3EkG_lS5hZZgDpntFNfQYJIPuoCJ2t3jm3Mb4kWLGDT7Utu2XfytGmkrTjhKe6bdEf5Xqmde0kOMfq82Ml5uxgAItN73VZK5M-Z76c06BJP5EVMXyfHQD4LxmYLbVS657PRvI-8Mv9HZrq1Fj5dMlBfvSZvszk9aJROAxyh3PNdhDyxun5zH9MlNirgafVBnuvHTRWeQ5jQ0QUyQZLcVan9XF0V0NWRb3-geOzaVc0oX48JmO0YzjdkbEjbOCWYE1R9ElDrO0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e090af8ab.mp4?token=D03qNstf9PRZb_B1b4XQ98y-rtTrO3AmG0QwXtBypEXJTH7-v-TQlRzoglPWZcQOLarr2wRQblQa3EkG_lS5hZZgDpntFNfQYJIPuoCJ2t3jm3Mb4kWLGDT7Utu2XfytGmkrTjhKe6bdEf5Xqmde0kOMfq82Ml5uxgAItN73VZK5M-Z76c06BJP5EVMXyfHQD4LxmYLbVS657PRvI-8Mv9HZrq1Fj5dMlBfvSZvszk9aJROAxyh3PNdhDyxun5zH9MlNirgafVBnuvHTRWeQ5jQ0QUyQZLcVan9XF0V0NWRb3-geOzaVc0oX48JmO0YzjdkbEjbOCWYE1R9ElDrO0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از تشییع پیکر آقای شهید انقلاب در میان سیل عظیم جمعیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667310" target="_blank">📅 09:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667308">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73797f7d52.mp4?token=bJoVQKV7W_urdvvxqtkWo9REhXUYxSMbVfKxAiP8tJHwzzWetG2GiSNlNg11lyhp795dkDi2c0_lq0RoKyE5exEZ6aZnYOyWrAU4ltVw5et0ZHrvPlN0uzv2piMs6HfBPjo3RR_UgjdpI9AiW5hRIj_KUtQ1_ZbwX6z69VQ1wsoCAVK_bz_BHkLS0DId3BeTMFYmipD47UkCNaMGNu8rnMoJmck4ybLy307V8Fn3eMNYtmhjPtwLuuBCrIrmP4Hat9ztExAb4fqA2KOy01bYT2V9EXyUBhuScsiV3gnMoJ60rJj-44IXZQgcc_60lvkmcYZp8rf36kXkyvH4uFZmDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73797f7d52.mp4?token=bJoVQKV7W_urdvvxqtkWo9REhXUYxSMbVfKxAiP8tJHwzzWetG2GiSNlNg11lyhp795dkDi2c0_lq0RoKyE5exEZ6aZnYOyWrAU4ltVw5et0ZHrvPlN0uzv2piMs6HfBPjo3RR_UgjdpI9AiW5hRIj_KUtQ1_ZbwX6z69VQ1wsoCAVK_bz_BHkLS0DId3BeTMFYmipD47UkCNaMGNu8rnMoJmck4ybLy307V8Fn3eMNYtmhjPtwLuuBCrIrmP4Hat9ztExAb4fqA2KOy01bYT2V9EXyUBhuScsiV3gnMoJ60rJj-44IXZQgcc_60lvkmcYZp8rf36kXkyvH4uFZmDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای نزدیک از پیکر پاک رهبر شهید انقلاب در مراسم تشییع در نزدیکی میدان آزادی تهران/ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667308" target="_blank">📅 09:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667306">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d5593cf4.mp4?token=pw3M_jPX5iKvCA7VmOHJvXkxqlmqoVLLpn5pS3xuoXmM4pefwkda-2zzCDwp9PXVMFVvS64KjZN3y8dDYmohge9y182JflR6dUH8G9fVDJMHCQSYqZP6BgSC5XMWgWSZe33TT2MAoma-0C4TLPzihHeDeKkLZChucuIYuMqXljk2vh8CQMr7gA4i9mKg-JyRMIC5d7mNnrG0StsibSiLOA49HvszdyQDVdv_1cwyfAGDpi5kZbxHIlOunIq4WSqcumoKnpu6WQ_uQpUFVrSU5NGM82-IhzRCFF9aQMqH0txNSn6QAWtE13bC2kcrOcJia0d_bxTm0uW1fyPMtrEEUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d5593cf4.mp4?token=pw3M_jPX5iKvCA7VmOHJvXkxqlmqoVLLpn5pS3xuoXmM4pefwkda-2zzCDwp9PXVMFVvS64KjZN3y8dDYmohge9y182JflR6dUH8G9fVDJMHCQSYqZP6BgSC5XMWgWSZe33TT2MAoma-0C4TLPzihHeDeKkLZChucuIYuMqXljk2vh8CQMr7gA4i9mKg-JyRMIC5d7mNnrG0StsibSiLOA49HvszdyQDVdv_1cwyfAGDpi5kZbxHIlOunIq4WSqcumoKnpu6WQ_uQpUFVrSU5NGM82-IhzRCFF9aQMqH0txNSn6QAWtE13bC2kcrOcJia0d_bxTm0uW1fyPMtrEEUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد الله اکبر میلیون‌ها عزادار در خیابان آزادی تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667306" target="_blank">📅 09:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667305">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سیل عاشقان برای بدرقه رهبرشان آمده اند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667305" target="_blank">📅 09:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667304">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx8c3buLJ08sL8v00gOYDo1WoTfH3X4T8_508Y_A-1SFdF8gBpEcRXcg--9UE1J9GYcRRm4wUJ5jdiyidnFyKXNtjoE_v1jU6o6ulEjOsVz6hhRWmieRAu7cjGb3cjikRCpuT4KThqkVrTPfKcdIDvYSmkk58NGizZ6xdcYbbnKcWzIG-LXirfK4PsCF__lEkc-Y82BQiGSa8X99LcAhASwE669bb7xnpRNg5D2W6vox8OOFixVOXap-Iov75tIqQmvT6yVL7GUjnLchp2t6C-k7VUl99HQyGF0kOJgEvzzGCJTFAwGAnGdLc-fiVdXmXXiZjxbEeIZMuE2EOAixLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قائم مقام جریان حکمت ملی عراق در تشییع رهبر شهید در تهران شرکت کرد
🔹
سیدمحسن حکیم قائم مقام جریان حکمت ملی عراق لحظاتی قبل در مراسم تشییع شهید امام خامنه‌ای و خانواده شهید ایشان در تهران حضور یافت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667304" target="_blank">📅 09:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667303">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5fbb61c8.mov?token=KLom69jqMSDUvvBkxJS0RG3hIxOwHpRFnh2JhdO5oROETpi5kfsOcgHpXsWKcKHm6i_IwWeyugWZnJHEhgf0otaKF8ozMeRDWnYivzh0vFLHe7_5BJjz6wEwgn-UbwDCAm70s2tY8B4SZ1KDzWsfrHVay2GABaKL1X4JcKkfHGuvIeIgNN0Y6BLW-G1PI_G0jLROsQpoHwzALe9txIlzATHrUdqA6tFoBZt2h0zuezALjFu9Zfi0ibBRAifh7xy5i5qZZKXZzFc7zBNOwkmyHEXbAXdP5u3qNz2b9JA8j-a7sdtZwVHa8wkWgzGG905ToZaT2KvQ1SB2dxdOlh0xAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5fbb61c8.mov?token=KLom69jqMSDUvvBkxJS0RG3hIxOwHpRFnh2JhdO5oROETpi5kfsOcgHpXsWKcKHm6i_IwWeyugWZnJHEhgf0otaKF8ozMeRDWnYivzh0vFLHe7_5BJjz6wEwgn-UbwDCAm70s2tY8B4SZ1KDzWsfrHVay2GABaKL1X4JcKkfHGuvIeIgNN0Y6BLW-G1PI_G0jLROsQpoHwzALe9txIlzATHrUdqA6tFoBZt2h0zuezALjFu9Zfi0ibBRAifh7xy5i5qZZKXZzFc7zBNOwkmyHEXbAXdP5u3qNz2b9JA8j-a7sdtZwVHa8wkWgzGG905ToZaT2KvQ1SB2dxdOlh0xAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جای سوزن انداختن نیست
انبوه جمعیت اطراف خودروی پیکر رهبر شهید انقلاب را فرا گرفته
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667303" target="_blank">📅 09:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667302">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d1f796a0.mp4?token=XIQrRhKcWHqndRwEzMhYjZrUgoYw82LhFRpy7arzZ6-sFe6pWDZ8OUaXucNGNeHKJwcTRmi2CwwP4jBNPzUDtEhezWyECrwXK_m92ZLdDa5jjJbzncg4-v15SsJbtSZMbwdbaogJszQCKLV8wYd57_I-P_T6NZ1VVJaM7D0oxT1V5GrG71DzywOhHSulDGfgTll8WcsYI4_Tsyaz1vEwvoH4pdR-PrnO7OkgSAqARZO9t7lydLeg7Al6QdUDwrVogDNh42H0o6mh2uTH4-4fEapQfmbMzty03e2A5eRnRpIU3GVlPJ1NgqYzRfeoUGFjUtTuMOMDotM1jaXjOyx86IOm_96sCF7Tg1pRcFU5QlkutU9mPDa6bBnmwOxOQf6WuBUlFzloZsw_07-gSQ7FI82HiETHE0pVh1oWB-d3iffLmImgYTx0g32HK2oqtzYKhonywaQhAb122BU7gyv4W3ns5my2Vdw-d6Q_LMlurbUuk1xowfmwTKXB5q21todgTgxVhkfY7Bumdd-jSdzYSZEJRg1goPzGUx0mEkLGnq3YIb3YDse-9BjQUnkWhj7-pMmlebE_yL7HuOxUFl0FCQWln3Jl6fzsxayyrglDRIgrFGzcH3M5ey163hFj6IaloLl0ARV-vCHCryH79k-6255itCcFw9FLnXilSIrqlwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d1f796a0.mp4?token=XIQrRhKcWHqndRwEzMhYjZrUgoYw82LhFRpy7arzZ6-sFe6pWDZ8OUaXucNGNeHKJwcTRmi2CwwP4jBNPzUDtEhezWyECrwXK_m92ZLdDa5jjJbzncg4-v15SsJbtSZMbwdbaogJszQCKLV8wYd57_I-P_T6NZ1VVJaM7D0oxT1V5GrG71DzywOhHSulDGfgTll8WcsYI4_Tsyaz1vEwvoH4pdR-PrnO7OkgSAqARZO9t7lydLeg7Al6QdUDwrVogDNh42H0o6mh2uTH4-4fEapQfmbMzty03e2A5eRnRpIU3GVlPJ1NgqYzRfeoUGFjUtTuMOMDotM1jaXjOyx86IOm_96sCF7Tg1pRcFU5QlkutU9mPDa6bBnmwOxOQf6WuBUlFzloZsw_07-gSQ7FI82HiETHE0pVh1oWB-d3iffLmImgYTx0g32HK2oqtzYKhonywaQhAb122BU7gyv4W3ns5my2Vdw-d6Q_LMlurbUuk1xowfmwTKXB5q21todgTgxVhkfY7Bumdd-jSdzYSZEJRg1goPzGUx0mEkLGnq3YIb3YDse-9BjQUnkWhj7-pMmlebE_yL7HuOxUFl0FCQWln3Jl6fzsxayyrglDRIgrFGzcH3M5ey163hFj6IaloLl0ARV-vCHCryH79k-6255itCcFw9FLnXilSIrqlwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ را می‌کشیم
بنر چند متری در دستان مردم حاضر در تشییع امام شهید:
🔹
ترامپ را می‌کشیم.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667302" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667298">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtQIHIQqubm533_pTQkk752ikHnu9iGgGQS-N1gruhKKehZkQ7TEKubKbYtPZd1j0tUms9p__d0fHa7x9aG75KNoBOyP1UiOSSwa0BYc9wr4H-sNHfK3GklHw0HY62FKrKEHfWa45i_szMqPsMf50XVMGvn-vRVU-5lXH2HKDZvRCAdzXwQasiVDnPxglSU6tqsP-KkMmZD_nTlr363_8EK9oZsZabFLnGy6DL1S9bieOL1IzoR-5LY8HdVNtEDqDg3Eiun8kWQU-RE4d_r_8nRYZSo0JHv5aw40T_xum3VgFJwQpsxiQussLil65atinGc3EkCcrvUsovRKDq5s-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzoZ9LlgyNp4WfFyaGXONo4jJM1SuQOX5GnVsaH-sGYLZSSRCi3VVujSMobMtUM858yUDw8zyBChJm8OAzk4PnMPqNJMCEN3dDEkq63vgAPfMW-X-8sQjmLEWsy48HZoosGO1zN68hE1aBDd5fXGHwif4amp6O6GxQys4upGtLoXtT6I8lbLbYnYOg41-kRCAfuknsE7jpPGFdZlmRtRcNsRcfmmrv2ZYMTPDaspZUur2KmdBe-N_FvmqWg02kpezpt5RVvB8kBfO8UWp3uS_u0ftfrTENCMzHAffPn-9ysr5Q1P1TG__dDc-YqKTCODKhywlHZjB-mgKHDHi7eBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXyB2BsHZpw5k_mAGRM3T-mJ-SGbw_nlF4omAUQG2OknbbQEVAQHcBjETyRK8-fXJhqNPV_DLAjmVlr7pk6CI8esDGhJsEDDBkLRidtaZ7MHEwFMXVFWRS82Q0p9lyIFzV6zpqRz0-XIR61L6zetVSZ2wqKVfEf2UgJnfZuehsUMVsGUbyJx_0gfUIt9gVSO0gECEHDyJG28dTNbq1VmZi4wEX7V4OPZng02YeAGYvNZeWB0Z901wzApsbm7AYCVbOhrBnqFeumZFeY0G-qsAhinEZZnI-h77pvl9HuIaTykCT1kSzq8uX0_9lCoSYl7wptFhbcg9YyN8gp_9oB-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GahSwBeY46rq9fGvHZ8AEMyBj4gcD_OkLxMbexoJnOBZP3QFIrzK9uYIMslfQRwWdeDM3mftxFy2gSzh7NJ_WoA42EUOQDx_Dtd83R9DbPqVduIPpzb7Z6aTWk7P4C21fqrZCRzctHa9XgwWTUpo6DHpdXluLVC_OierRzzxhpcsG3tsV3UVGCP0uK5vuMWMsydCyPUmlhU-hmSvBWLH1Bi_Nb350_-agkdiKVNGKIkhm0oE6S_6EvJwOaF454uwfSRxBH6pZMJ5WfNtVbumKyauHvzBW5VnWNzlrH5g0LSLzj5-Pw5Ol6QHh0vs-c5vbLNj_F4GTtT1HpJZNmnUgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خودروی حامل پیکر آقای شهید‌ ایران و شهدای خانواده ایشان در میان خیل عظیم جمعیت؛ تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/667298" target="_blank">📅 09:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667288">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uftA2Bxd_bCyZ0L63v16f0Q4OtnRVqzdxUXxW4DD0kSel6n6SmbKJnYvlZ2TT-uEyo4Yocg3274mm2P9EL-p097MqpX6qZ3zUpa6OZGZQFmjYWdBcWGDhxu4wNhkpy5N2O-cJTn3rq2OI550iwkkb-nrpVzDWoxsNNAhITWbtB7lrsC0btjkRcvoV8lyx8pzPV7AGDMB5O5Wkof0gOYbAy86p48mj07qolM-q5hi-dCfWcXq6RCvRWbtYajmbxu1JWX1nVTxImwP2s4GPuPME2meSKuNQUhhCkURFiZsprmoutOaG7BxBM4YxyQXRzq-D6_i4Tp0FfI4Kwy-LS3AkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CMESpaoXjTj4Nhx6r_t2RXAcoXHfq4T4riY7AwEnks46-kObnxvkNZDgTF6c9_NAexjFTU2wWnDYXQRYVJWkm2ZaB6qBzUpRq8F3pOLC00WvFvilzWijxtcTN4K6GXh-YtZUUDsbnCtzZPv32LpVrbyjeH8yLqFRYrPU5o2nMSyCec4ZwiPVq_yn6ZrpDjqrd2sk3AGKkNF7JTV6iwohqaPG8nx-NvPfSvPuRCliigjJr0FLCHeSIgH_vSHjjyOt9eWPXXIDfTy9lQKx-XKzN1UlhOGkrOPB4uzLP_-jQXDGUB9qTrjNcLMUuUQCn1VV3-aE1UJ5VO_g7_3Ucxvm5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PQnGwAXLUGpqUdC1QkUFXWxRKEp4jb41Vn3rUl93vnnfcrpyeSMgQG0zrFKn2IRAZN-cGEoeAnXCq79FVAR07oRZPr8XpXmZ3hYIiNPCPuRivJia4qTRyeEjgfaaJRFjywkgkpmmaNgK_XfbBVdC4mRgE5xdl62jXr9RPdoMLES2akPcblxE2XBcHFW5CKTOqTMkTfqPjRWp86_89o068MeQI8Qlq9kpdD6U3yg8MM1q5U1wkMwRIljmjd5DRJVR_LXpNiuR9EzfwyTRGwQaBwrHWO5yHjzE0NoIeZrFYtxv0zoQar_ivq_GCnrrOWR26APjxARVgroHaymvAxdSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NlyXEbUpi7YAu6iBo4LlVcXPUY6EcTFlJN6D03qE1D2jIuUl2EU4fRaYXpyA-h_IXKc8MOMLmTw6ElTNyL77tnP7G67mFjWyfMxAG5jf6Wwo9cfsNOoDo7HFTIUFHBVMAGLrO4NPLIAKl1DNFkrIcrWm0SKyCfXMje1ELQj8uNSsrRxinFUico4Lp_qPzZ049UpAZvhkWU5KmlKXY8ngtgjrdOX9I4DUyQSCJWzUhK_dO_AKTDdOg1WnnOlP8-vvVEfIsFirIQrgupDRc78x93vRkfn95KMpDLmYOQcj7FMBu40WtBW3eYN-O0Zd68WEX05NvrE6zaPD8ttjPycvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iIxucdciCo_Aeu9QnOZGXw-Ultb-_gosuEjEPJjOw8tbrxv6Jw1rBM6snyx0_FHkQkgEbMqWGMqPn-FyjX6TitfZ4eVipZdw_j6dUZN9kriEo8zDqJBcscGq7Z7h-_rLcknY5CLNRoC8Kz-Sa6V6voJgbeArYBhUMrrJNPYnJRa-TmfTvmo1uBMxs24Jea_vEzXJrdVvHUTPMbeDt4njXq4ndX3aIxpxM7i2PidTBl6IOEcGbjffC3Bcrh-2Lfz6Lljx6GUEHMERjiw6j247LE2I0HJ8JNtkNbAdLrILm2d1nGUvUDGoKkp9j3XWuEFrTXWm1OSkuYYkTT3helwiUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k9FLekvGpjZuP5FhJjKPBlHh7pL0dB5S2HAin2K3kIgJ625EFNMWanBtSejqygd25hHlxdlAZ4t1Z_rQAiwMS6ZaH3zdhHkdoGlBa44YhCBkVMyLuxvo3UvnCYeZd-maZKn8WVXJmioZ_mIfWxHraFBZ1kjd1MHC0m2RcYRZy8ak7OKA-r2e3aEoWBtM8qzbmsL2-pUsNURHWAgTc4Np_Ew3qUMBW_6CBtyhThxBpL1UMFUProPba29MZ2XWf6U2ivbIYe6C6LLmturXVHcNENTOGzlaqz79YeY9qf2Ag-I0xJiXv85VoFX9VUR9Ye_eA5mksJTtItiEkXUGGm-BGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qYQRGwlJMA9ssuy2X6U61G3VvQ5HL3_mlz30xI7ID4GT1Un2jehfRWrESn01rtdx92udQaANBvrsejyTRtF1us40JqfUpeb3QXD7ZIgkPwjxrNbmc1alpsFIvoAlfyQ2XAnQEivrdGN27iCsZ1OFT2JqjKECMrEnmwPgMgKmq31yaoyliGn92aJfj8iradUN5mLW-7mJbTS0GTYSbewmFh5tORYuzI8KicdiLgBMiJj8KIXFBUuCL2r_RNVASlmwlZvLQW5UFe6Cj8HsactGwr00UD6MVwqnSCy5g1HG8nIWNuuH5Um3GzFzuiJNREI0vSc5iXdhbVVL5yRSLTVS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aeJ1p843mZ76gigjCA9-7DZWrmaVB4-4CdY3m7rwZwiy2f9pSwoVKgXOmKZ4STYMdWrKs9UuF_L2hrf7UjAbyDqnKy7bw8o4ykpJjotsEt9DaMYTTuxZWYqdbyj5hU_EORjPW_u-5jLhpAvooZEJN2fm0J9bgZhm8Xhh46E2B5iVLFxcZo4JKXNhGE5imebzRbyL1eo_dZo3th6HlP2A5hDx1ffoOJ13dg4LlC9l1M8DIlXvvGTjlo6DRlBs4j3gMT5G9SsIaRfBSok6aBfq6pa5T8xIl8Qm6pGj15A8Gq7L_j7z3zMHVj3N-I9ubP9El_DWaAv1g_8VyQdKIk1v9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tmVXGKydV5khbq_k7yYmrz2NerzfID0qLqhrDoP8pAxiaJDHVtTE999K_uVGtHsKtMGaQTTHR-jEpV8rlMIcxUquIWZyyOcj0qO37s2f09rvdmmLrKHgUvbBhzmlkGwDo4AW25OLOTyrAqu2czPj3m6gatGalsYQG-ty7T_PUBYKIkL7pQxgx-GTjH0MjHB-hk6T-pBKRGVbxBOW5-iFoWAA9z4HhDKKH2KK8f4r3BgboQs-pW93qxSVMWmScdy168eL6BGWKduIVUQZ9nzCpbeQAAkXgByRvfVGInaXdzIzoZqTjqPTNRxjHfdUzpjy62BGj6l2b7r3eHZxt9ni5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I_R6ymXsEsFyx82XS12Su6WHcVkM_Kj4FGZOLot0U9TcsG2tbCCdBJR_3-HCgyQlrPtXHrkzCvbxEkJbdLXM94cG-Nm_Rspw8nfGYRs12VlnewVb9qX5yvrrVEDEr0_uqzwXrigX_so0WLrdsIedDaof5m4PgFubOU4LhHmnf-ixHp5O7dg7i7IBnfqPReHjOWf_hjJ0meMIPwCAqTGkWVkzrHFNoPyjkcjlJVCfpy4DNq8vk-A4GB_alFMqn8512eo9FGk-Jzx97HAtVi4BvMnUm9pgzBTH-gwcvb_2VjHdqOBZ3rw6SbGVCYDcZ1EyhNmF2VXmfH7SxuvbesmTgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انتقام، حرف قطعی ملت ایران است
🔹
مردم در مراسم تشییع، با پلاکاردهای مختلف اما با صدای واحد فریاد زدند؛ «انتقام، حرف قطعی ملت ایران است». هر پلاکارد روایت یک دل است، و همه دل‌ها یکدل.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667288" target="_blank">📅 09:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667286">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3zXmg8rQSamvWEwU6eqpt90Bg6qYZwlvuJBC8FH1Girhyd4iXO6T161zKkWTHVv6BMdFsARtyd457D-2V6RKYFES14CLlTevBSqfYfbcD-qzMgj6f17vWKpF-7U5L6XQEaJRY2nz1uP4uLkrpqwCVSt_sJTcZP0HTLWtjwXrgZulsZW8qRZTv5Cd_17OsbHjVP8nFtPbEM1SnPGY_o6J6OeElkclxdbmH5LKJZpcEIfEz0sYqgGvmrERlTsN3ykx8gmQBrPTPRYTFuvWkMUY6g__YVYkuHoIF8HVz_WNjTRQiCEMp4PFh7ftBktFS3cpYFfNCRDOmTl-3-7lEMZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خون به‌پا میشه
بنر خون‌خواهی مردم در مسیر تشییع رهبر انقلاب
🔹
عکاس: سمانه صالحی
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667286" target="_blank">📅 09:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPvQ3VxErc60d28MH-YSmNwMpWhqvqmGoqxiEXu9mtTf3Gj8rLC5xVbLN6wwSUn4LFXkNbJexK_PBTxeYFZBd4HzwhMT3mSzCLvPs1xZbVpi5RAdo3DEN_YEg1GSTvwql26c4GLBmehe491TrOttOpzK8QgczR7S8uQvba6SmiSuaV27btungTdBA6ygjMI5CrJOjcqPKO0uRu2_A6aCRmlffp8tRRmHhSYlFdddzDhi-N5YlG8FPovGpKZN8plOhx9dv7g4CotJWrId3pdujfoKmQMBvWyLmtsJ-g1OrkVjjKYS8hvd1PEg2cAQzT6_5j3FntRPKrBfDNO4GHTOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور رییس قوه قضائیه در مراسم تشییع رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667285" target="_blank">📅 09:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5771ea7f1d.mp4?token=d0uQ0crFduPW16I-hKucD-a0hkapGFAQ0ODktqH-tSYBE3M7cM8he5tH1UUOhkrlYFYmphmZ1_r52IcK59B-NP9pk00VEfr4FS4awdYUsAT9ODJbCr2q65N72d_LhixNbOhnrmvtUWVMBjulJi3pDgURr8-RQ2w8wMYRFSoLLjOyvqmQ7U652NDZ2uOwlXwven6MYQ7Og-ZDLB2V9g7UCLP-Sc52Zzdf0YOl9LDVFR35ERjyc_Fug6V1JqyJ6As48RwPHVXyTOFwG3F5s_zao74lOX70qq8Dyp2w7Gm2ebOOFIAWkXeZaqfEBlk6v6OsF8cbTdQ76c-bLJJJppHmuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5771ea7f1d.mp4?token=d0uQ0crFduPW16I-hKucD-a0hkapGFAQ0ODktqH-tSYBE3M7cM8he5tH1UUOhkrlYFYmphmZ1_r52IcK59B-NP9pk00VEfr4FS4awdYUsAT9ODJbCr2q65N72d_LhixNbOhnrmvtUWVMBjulJi3pDgURr8-RQ2w8wMYRFSoLLjOyvqmQ7U652NDZ2uOwlXwven6MYQ7Og-ZDLB2V9g7UCLP-Sc52Zzdf0YOl9LDVFR35ERjyc_Fug6V1JqyJ6As48RwPHVXyTOFwG3F5s_zao74lOX70qq8Dyp2w7Gm2ebOOFIAWkXeZaqfEBlk6v6OsF8cbTdQ76c-bLJJJppHmuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماشین حمل پیکر قائد شهید امت در انبوه جمعیت زائران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667284" target="_blank">📅 09:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b38aa4113.mp4?token=LL6WcheN_s2v-Dkr4bHHJ1GMFBkGMlnbTsa3f0RMcglJCjPPCW9nLpm7y0YR51DC48p7Ogclsv1pc9ZmWNOgxlXNCahjYImf44303t9KJI0Ow3ZK8vg76AaX_Yr9ChDt_Z99LLGfk6lpdkv5KKKTRgigV8ZQfAZXdDL5WU6XIa0jJwDcx8iuBkl4Jog3o3DugFosaSO64l2QBgMnv1JO_ugutYAa-CCY0oDwqMhM17x7fM58UKjqm15v0sBcEu1NnVtUhoPjZNsyWvO2-vfhH1i3LQ2yecyr5RJkwQ-yKs1QAXjPr4_qWUnkZF3GsRQCloe1RaUT5qQ8XSuMOpTeQGUV5TOuGp_2diLA8AbjGKeRX6KsGrpK0bz_Rr2LQP_-sG1z40aiBqAR8yPxEgaI2wopA7wns7GmbHRSM03WOD6CiXbWsZOmQ6N3uU3GVTuA_p_mIX2awM-ekczqFSMmHfLqoGv5F98Su5GxilE-kmW7IGqSi40TKXrrBoSxj0nWJ152nlSl3jk9tFov2fUcx1JHfnmzN1-mc5tSfj8LafVLTrYDAasDaomw6jjk4pnKiOjg20K7BS1mBFfqeUSCiP63vV-hs9jcEBD8gRQ7fEjYMwQoO1ojUzyuexc8bn_KWzoPbjlQ90DxkR-rJnr2kK2iAjP8o5PtDP4J0tiGSrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b38aa4113.mp4?token=LL6WcheN_s2v-Dkr4bHHJ1GMFBkGMlnbTsa3f0RMcglJCjPPCW9nLpm7y0YR51DC48p7Ogclsv1pc9ZmWNOgxlXNCahjYImf44303t9KJI0Ow3ZK8vg76AaX_Yr9ChDt_Z99LLGfk6lpdkv5KKKTRgigV8ZQfAZXdDL5WU6XIa0jJwDcx8iuBkl4Jog3o3DugFosaSO64l2QBgMnv1JO_ugutYAa-CCY0oDwqMhM17x7fM58UKjqm15v0sBcEu1NnVtUhoPjZNsyWvO2-vfhH1i3LQ2yecyr5RJkwQ-yKs1QAXjPr4_qWUnkZF3GsRQCloe1RaUT5qQ8XSuMOpTeQGUV5TOuGp_2diLA8AbjGKeRX6KsGrpK0bz_Rr2LQP_-sG1z40aiBqAR8yPxEgaI2wopA7wns7GmbHRSM03WOD6CiXbWsZOmQ6N3uU3GVTuA_p_mIX2awM-ekczqFSMmHfLqoGv5F98Su5GxilE-kmW7IGqSi40TKXrrBoSxj0nWJ152nlSl3jk9tFov2fUcx1JHfnmzN1-mc5tSfj8LafVLTrYDAasDaomw6jjk4pnKiOjg20K7BS1mBFfqeUSCiP63vV-hs9jcEBD8gRQ7fEjYMwQoO1ojUzyuexc8bn_KWzoPbjlQ90DxkR-rJnr2kK2iAjP8o5PtDP4J0tiGSrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از خیابان انقلاب و چهارراه ولیعصر
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667283" target="_blank">📅 09:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c3ad72e4.mp4?token=sMiL438olhmMNuMHlbu5bekWVUhUd7HDkEjM5xNEIWxtfh_Qkb29Y_wqDl_QH9B-ikoS6gR-73O1kRtZv4-Fd6I0CExc2Nxeiiz7BEsQEXRRm293Vs4_57YuONFBfJLKmwFuVLDbE4N6mdHhElI0JwdOSPD-jfVaYxTk47HNV59VAdzyCUq2yPrUW3A5Ri9Dw0dfXV91vPsJNWvkQSZhfTBU5e-U2SRT9MHL553mYdAJzWMeuJqhQU54XwNb9Jh8WdII8eePT9AoqKtbq0SnJylJ0957Cn2NCA7sVxBKjeP1hg62ykBRn8H16G_VodWxExytuEWhZL3ve8csiunAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c3ad72e4.mp4?token=sMiL438olhmMNuMHlbu5bekWVUhUd7HDkEjM5xNEIWxtfh_Qkb29Y_wqDl_QH9B-ikoS6gR-73O1kRtZv4-Fd6I0CExc2Nxeiiz7BEsQEXRRm293Vs4_57YuONFBfJLKmwFuVLDbE4N6mdHhElI0JwdOSPD-jfVaYxTk47HNV59VAdzyCUq2yPrUW3A5Ri9Dw0dfXV91vPsJNWvkQSZhfTBU5e-U2SRT9MHL553mYdAJzWMeuJqhQU54XwNb9Jh8WdII8eePT9AoqKtbq0SnJylJ0957Cn2NCA7sVxBKjeP1hg62ykBRn8H16G_VodWxExytuEWhZL3ve8csiunAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون مراسم تشییع رهبر شهید انقلاب در تهران
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667282" target="_blank">📅 09:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba60ac675.mp4?token=rLc0dirike64MlBntG8hDMJ6R3-40zKsGwjVljHcBVfJcC4eAfoe1TpPn7rxZf6XFQdMBLJyMAyK0b-Edr5PwnZstlz8VmXoVz9eCqHw9gLXCVdc1D0XREHpppgCwiuNYuqejPISTqgZyTdhpMe92bBOgEKszCC0EUIcZ0v3dxBWLgairEZqAJdCI1A3oE2se2fL12ucClpVm9cDm3Lk6FhkqxOmiCfHe6nULpM9s4W-odcVZMxaR5WOkj8r4KEkKJ7BTDCvtYcKCuB1cXN8KoZStMYeOMzG-F4bYNbTigtm-AJTu4qaO9RzNMVSIwexsNTvul_N7K0jjr5SEl6VjqseUxySVa45mW5nqcg2wcsELYsJjhIuyPxw2ZwMzhIYhMtVtc4TO2i8fQJGsVhrV0BDrmK2x3ZJ4kH9hWy2Kq-pQLCa6ZQVl5Nuka4BtgveQoy5-Zlhc4Etu6qKSOImSi2duQ0UjAtkw0ClRcdWhq3t_6BWU2iI3kgKmL81aG3cA6hmRbJdkJ0a4sLGjDKgYe3u_HqIxeNHH9j9rNqxFvVIqvCrdqBS0dBDAUyncyBGT59X8k_B1hFXcWdfWxjWE0Mkct4xfWD7R7xWGjsdtVZDMp22HOPRT-DFfUoPN6MjqNRbXOxrl12mqXSR0cmbniWwHRsRmzUCb_eOM2Bl_Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba60ac675.mp4?token=rLc0dirike64MlBntG8hDMJ6R3-40zKsGwjVljHcBVfJcC4eAfoe1TpPn7rxZf6XFQdMBLJyMAyK0b-Edr5PwnZstlz8VmXoVz9eCqHw9gLXCVdc1D0XREHpppgCwiuNYuqejPISTqgZyTdhpMe92bBOgEKszCC0EUIcZ0v3dxBWLgairEZqAJdCI1A3oE2se2fL12ucClpVm9cDm3Lk6FhkqxOmiCfHe6nULpM9s4W-odcVZMxaR5WOkj8r4KEkKJ7BTDCvtYcKCuB1cXN8KoZStMYeOMzG-F4bYNbTigtm-AJTu4qaO9RzNMVSIwexsNTvul_N7K0jjr5SEl6VjqseUxySVa45mW5nqcg2wcsELYsJjhIuyPxw2ZwMzhIYhMtVtc4TO2i8fQJGsVhrV0BDrmK2x3ZJ4kH9hWy2Kq-pQLCa6ZQVl5Nuka4BtgveQoy5-Zlhc4Etu6qKSOImSi2duQ0UjAtkw0ClRcdWhq3t_6BWU2iI3kgKmL81aG3cA6hmRbJdkJ0a4sLGjDKgYe3u_HqIxeNHH9j9rNqxFvVIqvCrdqBS0dBDAUyncyBGT59X8k_B1hFXcWdfWxjWE0Mkct4xfWD7R7xWGjsdtVZDMp22HOPRT-DFfUoPN6MjqNRbXOxrl12mqXSR0cmbniWwHRsRmzUCb_eOM2Bl_Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یادبود شهدای مدرسه شجره طیبه میناب
در میدان انقلاب
🔹
این کودکان معصوم با  موشک‌های آمریکای جنایتکار در روز نهم اسفند ۱۴۰۴ به فیض شهادت نائل آمدند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667281" target="_blank">📅 09:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSVnUTxWvjDMw_Hgf0om3O6Y6Xqv5-FbAmUdeIYgZ3TnY1lhFCdhoC_IaUmdXoPe2Ca-PvSZdYXoDVd9eLzmNghWIwoFcN5wRdB2Q_eZ2KQCsCVYDAQVXnum2GQlKyVcLpmFIHl1l3gEPuvC-saqJGp_LpPPWSJs-J3eWKF2xfkNRpfNQ5BI448I8L4ywJWSpPsW_lrmz47KEreAnoYhxjI9cNfCGfvXidn214bjUc0Q06RVflzFJh34r6eyp8K_ayaJG7Iktq0UtDrwLrTB07qnb_zcDV3ouOz9BcpKb0OafcEQu-KKvIjrZRPShi9oFw8c0uMpN6jQkHWXZUT8xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tb4XbXk6s2DW3vzhGQO5xzMjj1BHbAGCunT83ah8Gch4DrrwH732mn4ew9p6Bb_KFf8FIyKUyKxuehcuwe66_zqkRoMWpc8sgudZ6xlFfv4Smkq2dvEwAJcS0rAVirDid5X94_HFIYzpwQXwgr6uGAgfBIO1J6eISVAe14MWhIp6qS6bG8j9L8EuPd8YEKVybIQ22v86aSStiMGxtay9NS6mzB_vgH3XPyu-0HA9WfbEwbwJfvnWllGZ00B5IxQTlq2BLkO_GxHNVhFJvX2FuohjKwb2FIzqx3M964wGFKdIkXZJNNTtWAmmgArku8asNsqbfpPbp0yWwBA7uAhuYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSCGCYPxrpr3J8thEJzYKRSLpUDm32y71YUZsCo1SHPGVPGpVFWWUipkCUB9fptvfsN_dd5rPD6NwRyN_rbnvh2W4JqwpiqjX1CjMtBLS5eQ2PGLar1RFndu6UIzJtzlvEwpfSvgTjzJmW9kSownzR3mEHhAwLkAX1Tdtzhd0QlvcqMOqI3hqQbWOlhkk-tav81xhkDn8HNJPIoM5Tbvut5XHwfkqiatRBI5ddjYq5KAgiS_rJu83FisPn6D67mi4fdtTLm83fUS0lgQT8_io7r4TGhsjfzHNg87sfdKs0DmZDMZ5s-Y7-WtsVkaea3d912Q35avEHzYqvjmiSMWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLqj3msu-MpEifyeiA_PSjirVzjNVzV0y46Pci0q5IGk_O2pobBhPUN8kSIOjQ0EO7kbAEjfw9Dfq7fV9661pWJ28BW7glBeR7CyQctB4BD-RqFJ_7JPwnApwRJbHDnS6_EENKHvIuFDiLZSRwEs5-uxgUnAZHKav-9PYECjFU8l0nCzNujyTFLnHb9_ED-yehwGk6xm9z3H6UERR9FMkgh1ek6jlqY08iM_coGYPEGQK4FCyPRXWoWOUxbTlYi7HmHUT9nOqyLySMjhLw6xTmO46cXI1nBugUyAVs3vZMoTdEk-nzL4Sp5AZ6czZ_5q-hlubflCcK2w3vk3t7hv-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HKH0sf_KPiGxKeD26NK-xG5Dy3iP0_WbRz0m3MGyEdoIkfb-1mrTrQoRwMUHVZhi8WzzO5VS32W5P8QgKpBkKRCiCehVpmHNWHq_jZ4EPUwpA0edGXyQZZ37DhYMcqleKMqU6MBUYTC6e-X7tkjm0Np86a8p3P1F8xgsxhP--a_dOcELIfEaq-8wlfW_SVBVLFPUtYBPg9LkOKoXajJ5wjQA2CjKsCP0u6rYWpEb2QiEViMA0a4TpziK_Cnvr4TBJF7D6ZIF00yN937ZDusuGh0N7epiF7t8bcawGX4x0-Y-rFCI-tmAB_3k7IfBHc3tNb1L-appRRzbP-OP5d2W7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9NnhjUPeD4YXLfP6F9IbyvXWxiclcPMWmFEjEVAi-0HF-wnhCL1mOam94OM-zoWXzXXq3kz0UNL7hco9hRwmRBUgsHg_my1GQUIRiHXpmSo7-zno5hkXpBjB2zKi5erENJM_oojSpdz2uPHpk_kGuHaty3QjL9Jj2Q31QeS3F-vSY68vAWCpwuufSOR51SsG5Ed9A9ZqUqGOPvN0VaWlt1v0ZoDqlnm1MZFrInOduslRldruKwPLcb1AboU7OlkL7Q4WOQAjqF5nylmxh5QSh9a67S3g66Xq39-Xb5Sgso1rV5OmLbxkxtRjRAWIWCiE79G9SttOyJCgaYFuZJkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3i2VRgLCHE72aKW7PqoQqIxI86goUzRmhiWEfi_juDXagEatOfg92jdfQkpgYPb7WXe4lbe7TAEC5F-C4N30Pkd-ck5dS0a9-8sXnMVpJBndBVOjfyBXdQNl9kquuhNU5cPWGz8CWWcfX8ym-EUzqQ9IESUuIjQJcstm1N_vuJ3Zbub1bNOsF1Gax9ijeCoSP_nfg4Fbeig1Yo6YCuJWKOv1izsL5VhzrEjISvnxWElSdWxJI2oIDgQTnhexgoJE4o_9WeDHBsPZR1LIGeKhXdqVIkwuQ7rz5sptE0-Mo3ObMzi9bJMISgHhg6A9si2zsWk5hyStI7VQPIZHFewIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqESiPVTTtFeb8ZxYsL1_1zWFtP2GF5J7BiNVgxVk2jAhZh-IUOFfi9OJHipljA1jDahunEt23-L5mCYd6TZnUuBaGlbxlHRkoZ9rWaDrcmplsFSMlSpHS9sFhAVERlS4KWq7xIB71qMdO4IoT2eDIz9NWO6lEzD48g6XBuief8ufPoBTRKZbr5AyICQcjblw-aV-1wyWo7b5D5DIKTKHQ__dtcBcdFEIfH4xUL95BYSCVyGxF_qSF84oozYnfq7TiAqYsvr6h9mexv4QFOzInhgxZlBUCveo9e0v4rNQ5cKvoY4HJNRMx8BKT3T8LWmTkwmIdoNTIjKex7bMXEjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-lojSd-ZfUPapIEbdXJJhykyQ6iBicXfyQcPocPSMb_z5BHrmEbtA6oOXOJGXnRN42h67v67zx4js0HzxiaKyLog29TPEd0jq7HZQk5TsdkLYRA1p3gT_l3-Ve7bdQG2aONroeOgFaaeNbnRjZ4Jxlt_RhIMKF1kwCrCYjaGZgKtINJTW7odWoN_Ccxi2pE8iOdfqC8VInKw0E-7r8U6cggVqN3i5E674Im6eBltUTHV5I60PB_qLFizF0vOsf2ZagLHq-SCuXMPKmyEI40OeREMDheHoRZFnD_F0mmk9dNbcl9u8ap44tjjvzGj5F07rRKHs3-RNM3j2mUX5ZuqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از مراسم تشییع پیکر رهبر شهید
🔹
عکاس: سمانه صالحی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667272" target="_blank">📅 09:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667271">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBjtgEq8oFOeFIBskrP8I_uK2UbLyPAhwtbLI6BS7naphq1JADyN5il4nsWnHSR2Le1SdyMh2OpY322-fmTLRAPGjZ-JnB80wV6l_Hi7pEx5lFd5c6ChWwgDLgMXS7VEcetJJxLAKFWZ6JE2ky-yKp6jjEmxf_sstbV2CEZ-4n6OQD2kWx6ZPqQmfOsAKr3OGpGM3F1-spiZH3Vvh0YJbsUu-oKVwuEsR_ncHUNJQQwCDsIoai5_73XJtBW73YbMICbOi84cQ2Dz5c1XLWeDkmJyIpK1xXumqI00gHq8wL8Pn0fzp23rM7kcnZzyNNWStJN6HyrG7tugJr6ppqohjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور آیت الله آملی لاریجانی در تشییع رهبر شهید انقلاب و خانواده ایشان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667271" target="_blank">📅 09:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667270">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM5krwJ6OAX2hkcANr7UmY5_XBoXzGKHjKYqE8nY82WDs_VJIum0oFV7KmdDETI789gRftzpndHAaUJhE-pxoVGyOzB_YA7kR_OlDKZvrjalBvXw_Mw6H5RtQoOSfWofppFx5GAUdIpoUxk4HkmBogIpimCHVjjVBP9STXaHEGTRZsuUP8eWLdpUclpfI4QCkUj5Dagrm7UyCm55uGtr-QkgNrHhZZdJfRkI5AGCRep3MRcqK3whYRSjmT-OttOuNyQaIh0ozJ28QLFRI1PzH8SXl2-4Z-h_84ctJ-O7GDPI-4iYBW2IBwXQjiaTzemY91nNE1I3JoD82xedMyqqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور محمدرضا عارف در مراسم تشییع رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667270" target="_blank">📅 09:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667269">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c88bf2348.mp4?token=O9AzvF_piDy0A_7AnyRCP4eqyInBHfwvy3bZwkjWgzAxRF7zgfy8_c2Znu16Og7723vX-FDmICxUl56HIHYBDh9QohsKUYwFs_45KMgOglao0mA_YwclldtDi0yAPjplIcq5myXGllQ5OWzUrWDnU9_DlwYYlIzwDRid2iUs8L8Oj_w5kWIcBbs__Oeo4f7E9ewNTsAeIyfNY0HtgHc0PQMr1_DmyVzqrBUZ2Rw21VEJdibhovrt1z3gLj7vw0_5WJk1OT7QFmG78eJjPx_DrOq3Zae7CD4AzybN8MBtJxrwjdd4GQgeo1V6gnzydrLFzol9Y0UhE8CkXi0TRHk_wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c88bf2348.mp4?token=O9AzvF_piDy0A_7AnyRCP4eqyInBHfwvy3bZwkjWgzAxRF7zgfy8_c2Znu16Og7723vX-FDmICxUl56HIHYBDh9QohsKUYwFs_45KMgOglao0mA_YwclldtDi0yAPjplIcq5myXGllQ5OWzUrWDnU9_DlwYYlIzwDRid2iUs8L8Oj_w5kWIcBbs__Oeo4f7E9ewNTsAeIyfNY0HtgHc0PQMr1_DmyVzqrBUZ2Rw21VEJdibhovrt1z3gLj7vw0_5WJk1OT7QFmG78eJjPx_DrOq3Zae7CD4AzybN8MBtJxrwjdd4GQgeo1V6gnzydrLFzol9Y0UhE8CkXi0TRHk_wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاب‌های ماندگار و بی‌نظیر از تشییع امام شهید
🔹
عزاداران با لباس‌های خاکی در مقابل خودرو حامل پیکر امام شهید سینه‌زنی می‌کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667269" target="_blank">📅 09:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667268">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سردار حسن‌زاده: مسیر تشییع تغییر نکرده؛ مسیر همچنان از شرق به غرب است/ ما پیش‌بینی تشییع ۱۰ تا ۱۲ ساعته را داریم
🔹
ما تلاش می‌کنیم از نزدیک‌ترین نقطه مثلا در میدان انقلاب پیکرهای شهدا را در مسیر مردم قرار دهیم. #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667268" target="_blank">📅 09:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667267">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5fxB96_PP26VuOt5zcPQjMoZ8O0B4AEgiAQfaisltDj3OLzMK9t7EIw-RI8HmSsxHJeiq1O2x_TZSNeONJW7EaN4Qbmtp7vCuCedOjpVUlJWuPlVBjyTtY07e0I7cqo7h9zF9JPPLeRPnA0ANyxdaWW6LoAe16KmRz6MQGxvg7jWp1ctDDgbjuJfvvarm2h7PgmRBmFxVhB5RqFMusijrlxTTs5fxEv1ru2i1UxwcnMBuV7lJsSqqVwwLGMJgyVhLoKvfcK8GqVSzBbCzrxjSiF0EYfNj0AM2z5EhzTAhFVGSTIl_69MzPV88yE68VBU1Pn5WJ7MnpjGCdmP6BkYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
المیادین: پیام تشییع قائد شهید این است که خون شهید قابل معامله نیست
🔹
حضور گسترده مردم نشان‌دهنده انسجام داخلی ایران و شکل‌گیری آگاهی جمعی در سطوح سیاسی و مذاکراتی است. همچنین ارزیابی‌های آمریکا و جنگ رسانه‌ای واشنگتن علیه تهران در عمل نادرست بوده است.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667267" target="_blank">📅 09:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667261">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LyBEbmqdcjJkEvLi5wSoCONHLwvwVVyVWwn8vUOzHhBoK4_-YqRyKiFgA46Xj4P7LMZCNgaJ6yseoEccliGOhQGcIiJE2icbMWZNkR5FE0f5krjmEbxKV3ZMAjuYn685bv2y9E0lE-tizDRZIgqEKqOCK22ybsqE15-IqNcAC4dDjqwL-1lpkJ-NHOoQqlWSa_wHkraPc_MRnLAAaiG99uyo1UqtY8p2pgLWAUb6P5duxGaKzYSn-Pc9d0pw_c18LAogEJKu4Qme9MT_l01sC9PTGT4hdyDbeEQesd-_sOZz6kr_pa5NLKl1oKG3PHm2ejGPbd36UmZmCn7EA0NQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MO9gp5n7PbWezbzbl8lrZ7sinJK2vdxyf-_IxDpnl6DlEdU797pqP8GYmzxTTFzlOokHpaK61uLORKz35zwGxqkShp8-ck7P-HaxpyBnS2GzY8aRmcxFatbycfyFcR8kQCvEluPtxN_S4oZzLD14OEKLguuiJT4p97Lw8HRxgF_b141fSEXy6ETtlym0S5h5WRzG_uRUeEesKyHxMIJv46_zHWibhUQWqv8r-6Yv_owhqYFRhVOFgZCTPbXl3B6p7jxxXk975KexjIZGH7wFotrX_nrGW4ojyZ-q2NT092pUXJ9b8jySWDZAXETBMx8s_D8VyiNfy4cTX3ck0DOxOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVaEVppNTTR1fhhD9OqV-LANc2jrJ6gZ5IgLuveUJ6cJBUbKzzuTy48UywztKfm3D3dRoYH6iXgCDRB093xmKOVzM2SmKH5oAdf9EpqI3UMWTB5eyfKZT7T8H2ooq3-HqLKVhgnUsu2aEioudC2IrdnD0-e50XRbrxCQXQtPMX-JkAQbXRoJny1kk6WUwTjJasNq4I-JHbxS8w3sf8NjPyGQOvjgAR9kjljyyeZbtgOzT5egTQDFhCaLFx72wmzakVhrzpWkTOnyEaiv2oAWW_M-M-IQkStOPVNmJ3U3uzp-DzMIs2tymy6_UGmN9ODvtzswYi-PLLqJAP_zzZzC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhLdOQuMRgmWk3LY6SDwyUH9RkWacXEB-zswydj8DmA4uzpJd75qI8uyac62Wo7N7V1QfgN8fhHwfQ-aNKFq8wwNklecRhudzFWrpBOYqS0OZB_QIHroNS2VTNTMBlC-46CCSJyJa_9uluXMtdonco0vw911reDsf20721a03sj-psT5z7ZzGHdOvTpw3fNEQN6U2nCo9jIcm8-jFVQEbslCCharzOF9Pa9WSbNOQLx4kY_bv1-iGTRKQ96ZIuUppjZHNJLZPpjRZ3vFuHj6_8NUCJpC1L0m34kJJwSp6mAFfGLJcp6wjpfne_fKxogoB4UTwf6JAL2Jyg_JD0H33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXM-HsEyQ6_af4DjRjNIQGVoG0Lezno8eWb7JE4kClXDQvDf-3qcdbLfLG4ndT8lbQZSwzLZtmv_w70gsj4O6o1rGXxDhEVcEzC5neYXqm8DkAjb2m4vk0QV-b1N-1Jh2nOsZvXQrSGdDJO2fJg-Jir3MTMpnG0-t1fAryV0IErZq5XNpzULj0JrtBjiNNiGS1Bh3REfZTM2kdkoWoajA9VDDw5rbiButk_4ad_zW5R0GvuEbyWu1YP5W-5kXxaZSomNpCshMZuY6RGpPeiy7cScbQ-enY0kAxwTYd5C2MCicMX5UvwkcjXHDys0PWxx06tJALqS2d_aQMaEHVPY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFRUpKDMDr9iWt8-iISf6FSo_Ug_6gRJFTG6O90xI07y0CJeL_l6Yw-KuKKtKFEO5vi9lnKo1jjBFbG8tHn-Wyw7pM3PxU2bQaCvMYsDDVyw-azUpug0qc-mJ1hxPDrJinkt-AeO-BtE1BwtsZLoS66l5kYuJsfn4Zf3hpBoAdAEjptzMF0aga8Y8lfL7A1204F2toQp8Or6kZwd3-91Hg-4IbR4H6bR97V0iBIzy4XZ2eKHUn1YU5DtSMUrcMZUC9TgJd4Rcjb6GjhF3Woh_wPdw2prF8ZLznuhflnWkl3aP4yGkgPNWMKRLBlg0ctt_ckD0pqSaISwY7ioud5PTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از حضور مردم در مراسم تشییع پیکر مطهر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667261" target="_blank">📅 08:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667260">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4eadffc.mp4?token=t1TX-aopI5dMmDdmEk1lam-2c6TQxeG6wH5om0bt0yhdgtfo3fhOZR26gf5QEO8HgcwtxEqooS7y2ySixujmnh2Ia3kjc9JRQeqjH3pIY5T2cKPjE1pxOs-ltr13AbZnhwkiOBtqsedKmuE4nRS4vwp18snHRTiL-95cbmB0Z0HZaoIqQfN_BJBVpWVfAtAi7eFeCFU80N-dCj3WwuJb1TzVCVAKRKmY72KWAsEZ8fyGqdvLqWDvS-Q8yK9ZEY2QXwyK5YDmcOFfoRqrNtl9f6S-tiJE-0fxaOI-Z_MeL9L5nArT1FmvDXjtM26-ns-Y3j5S32wKhx0hKE2TieOMn20EuHlqV0FcTxDSzJ0i0f8ZWjkaqK3bgOlH_5WIMQc6nNX27js0iYggaYpyT9ShA6t0RCO3tRO7B-Fg5vc33lUbLW-aNF_InBA3_n8mcKOmLUbWmRVIcbVm1Oy0YaZmwOOhr3Z4krfY2RxOt-WK3YFWxxMFTdgJFzab0zD2XOX6Poizw0t3T3565QNdHmWA08QQ0PwvWgq2xAgsQTF9ZL8zY4L_h1PiVI8aa5pJhKXPTtRoKfe8l_sq8VgpVmZOBP3azal6oft_8mR2rqhCVl1b8YWjf7tIx8yc6wUqx_b7F12gM0-VeQQ7YcBf1pAK4q19zUn2y3mbcNj1vhX_4ro" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4eadffc.mp4?token=t1TX-aopI5dMmDdmEk1lam-2c6TQxeG6wH5om0bt0yhdgtfo3fhOZR26gf5QEO8HgcwtxEqooS7y2ySixujmnh2Ia3kjc9JRQeqjH3pIY5T2cKPjE1pxOs-ltr13AbZnhwkiOBtqsedKmuE4nRS4vwp18snHRTiL-95cbmB0Z0HZaoIqQfN_BJBVpWVfAtAi7eFeCFU80N-dCj3WwuJb1TzVCVAKRKmY72KWAsEZ8fyGqdvLqWDvS-Q8yK9ZEY2QXwyK5YDmcOFfoRqrNtl9f6S-tiJE-0fxaOI-Z_MeL9L5nArT1FmvDXjtM26-ns-Y3j5S32wKhx0hKE2TieOMn20EuHlqV0FcTxDSzJ0i0f8ZWjkaqK3bgOlH_5WIMQc6nNX27js0iYggaYpyT9ShA6t0RCO3tRO7B-Fg5vc33lUbLW-aNF_InBA3_n8mcKOmLUbWmRVIcbVm1Oy0YaZmwOOhr3Z4krfY2RxOt-WK3YFWxxMFTdgJFzab0zD2XOX6Poizw0t3T3565QNdHmWA08QQ0PwvWgq2xAgsQTF9ZL8zY4L_h1PiVI8aa5pJhKXPTtRoKfe8l_sq8VgpVmZOBP3azal6oft_8mR2rqhCVl1b8YWjf7tIx8yc6wUqx_b7F12gM0-VeQQ7YcBf1pAK4q19zUn2y3mbcNj1vhX_4ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعرخوانی طایفه لرهای بختیاری در مراسم تشییع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667260" target="_blank">📅 08:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667259">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
بازار سرمایه فردا فعال است
سازمان بورس:
🔹
با توجه به پایان پذیرفتن آیین وداع باشکوه مردم ولایتمدار ایران با رهبر شهید انقلاب در شهر تهران و بر اساس اعلام بانک‌ها مبنی بر دایر بودن شعب کشیک و امکان نقل و انتقال و تسویه وجوه در روز ۱۶ تیرماه ۱۴۰۵، بازار سرمایه در روز سه‌شنبه هفته جاری فعال خواهد بود/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667259" target="_blank">📅 08:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667258">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dae2156d0.mp4?token=NizW8zaCEdkTpHnOIdPSE7I7Rpg94LNasNHxpNgQ33ObgT-SVpmtFTkbo1D_NyLKRlyJNvzbtyz9RJdbbf_WuIblmySt-UkCZgLuGmTnv0Am8nRtoSZzCCAfC4yNk1wtWvm_OZy2hh8uT-4OpNgg0J9Z7A1NdkxW6vtz7ImXwE46T0sz50UTLlFDQ0eMa5fAAoPZp1Milo7VfUtdC0ITtvkjiE4DWRXK0Vpm3vKjt5tCHWHbT6Yg0p4XhgZFhOv7rObm1WGGcdyNvKjsvs3vwJveFkKHaudO2RTV6u7r-WL2Rk3As6TH_wqgC_zHo1fEyamkHi788xfWcU6TZHCXVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dae2156d0.mp4?token=NizW8zaCEdkTpHnOIdPSE7I7Rpg94LNasNHxpNgQ33ObgT-SVpmtFTkbo1D_NyLKRlyJNvzbtyz9RJdbbf_WuIblmySt-UkCZgLuGmTnv0Am8nRtoSZzCCAfC4yNk1wtWvm_OZy2hh8uT-4OpNgg0J9Z7A1NdkxW6vtz7ImXwE46T0sz50UTLlFDQ0eMa5fAAoPZp1Milo7VfUtdC0ITtvkjiE4DWRXK0Vpm3vKjt5tCHWHbT6Yg0p4XhgZFhOv7rObm1WGGcdyNvKjsvs3vwJveFkKHaudO2RTV6u7r-WL2Rk3As6TH_wqgC_zHo1fEyamkHi788xfWcU6TZHCXVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور نمایندگانی از کشورهای آفریقایی برای بدرقه رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667258" target="_blank">📅 08:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667257">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9a627324.mp4?token=HjoDxehVgBSS44wlmmVqsoI7E5s9pstW_JGyf__PnW2ehcnGlnrccVRwmWXAygLmtZzQr5rY_OSLUrDUkC3JJBWCMwTej1YbatkvhyZ4USRgycfzXfW3XKyhPXZSI8FxoSL8Aa3voDsxXQKKr_P1Om5DtVn3QtB06SQgeZU8ZpBlnMHSBLRybWHS-eIhfctaIEn0kmifYs8zPTY8fZIqyKT-3zK-FhVZNDb0KGljmYn0a8AoAv47IePPmQXdAq_6sZqP_edKt7cR5jDl4ejlXXuUNTOKMwHu8kQp8-N-BgY76FinUuJsevqC_BTzhQuFO4tqQ-EIAhNv8cHG2YO4sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9a627324.mp4?token=HjoDxehVgBSS44wlmmVqsoI7E5s9pstW_JGyf__PnW2ehcnGlnrccVRwmWXAygLmtZzQr5rY_OSLUrDUkC3JJBWCMwTej1YbatkvhyZ4USRgycfzXfW3XKyhPXZSI8FxoSL8Aa3voDsxXQKKr_P1Om5DtVn3QtB06SQgeZU8ZpBlnMHSBLRybWHS-eIhfctaIEn0kmifYs8zPTY8fZIqyKT-3zK-FhVZNDb0KGljmYn0a8AoAv47IePPmQXdAq_6sZqP_edKt7cR5jDl4ejlXXuUNTOKMwHu8kQp8-N-BgY76FinUuJsevqC_BTzhQuFO4tqQ-EIAhNv8cHG2YO4sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیل عظیم عاشقان در محدودهٔ پل روشندلان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667257" target="_blank">📅 08:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667256">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5cc2c1d09.mp4?token=jAsXP4hNqYe9k5APljAmnsJcu0IdGd8W14Kp_qXYFJzOp2Dggt0BTlRH84f-7dHzloWMKoSUA4C6PWKH7J_OW2zwkqYgaNLeGpT9awuBHg_JDhzzGZ14M2lXy7pbHrntaivsFhlvWK90_DTiCojMIMeOi3W6iwPgAsnhMIvrp1kKOlqvQCd0u0z7j0n2rUQJ1RgOw0yzuO6dMZP1nQuarVewGLRxTlFLWq05FRnvCN43PKwapJEbBG8ry3TLX3PCOZ7f4NTwI4qCsKdjIk_cGbeaOIICqxenplh-UbR09U5w4oHseBOomhvN0R48--FHoRnQwMPtttuJ_3vy6xcQ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5cc2c1d09.mp4?token=jAsXP4hNqYe9k5APljAmnsJcu0IdGd8W14Kp_qXYFJzOp2Dggt0BTlRH84f-7dHzloWMKoSUA4C6PWKH7J_OW2zwkqYgaNLeGpT9awuBHg_JDhzzGZ14M2lXy7pbHrntaivsFhlvWK90_DTiCojMIMeOi3W6iwPgAsnhMIvrp1kKOlqvQCd0u0z7j0n2rUQJ1RgOw0yzuO6dMZP1nQuarVewGLRxTlFLWq05FRnvCN43PKwapJEbBG8ry3TLX3PCOZ7f4NTwI4qCsKdjIk_cGbeaOIICqxenplh-UbR09U5w4oHseBOomhvN0R48--FHoRnQwMPtttuJ_3vy6xcQ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید: حضرت آقا حلالمون کن؛ امیدوارم امت خوبی برات بوده باشیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667256" target="_blank">📅 08:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667255">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74012bfe1.mp4?token=Pizqk6gQ5trVfe-DgqfIwy_qrci_beV8f4HiOLjke2IW5jkjZRLeJHlclVxTObvWhA8f9CJPxFsBrme4aXFx_tnK6Wvv-LZdXjlme13U08IbXOEEfd6QWrgyX9oPfaBe1yLABaCB5xtbR2DHXC76EuyGBMtooLCSK4r2RRgfZKJxb62RD5kk1d4wWfaKPrwpkGmomDDlYt9xeG4nV4DnCucMUIGLTho5SbtRS8i5-Ruhw4JSmW_agD2JxmzGxiyF_RMB-iY5oO2q-mMcKpZaiS-n3sPPqDjWcbiGcKWlsYkq0o1GkUw0TJbEmEj46OXwbzwEZrH_9-tp4lXumrlP-p5mbJMAMtcGEC2oYh_9T15gSzzycJ8dlD7_r-2BAlm9V7NMsKpKd6g9-ELhYV9WHag9jv96Fn5GjQfTLG566ylDfSx2nkK5521NozQkPmC_VFvEVr-J8Q8RlbldIuiUtkj3u_sa-oJGbCfZArfmfXsPs3bH96wI773FmSWTGtBj8_60Xfv7f8USwowxkRSq3UBLzkWvPQM5cDwNpi747uzpds5WtXlV6kDnP0Dxj-XSYV3xs_5PS5Po7X2FntSGDLjiLtxhtSBam93_PoTtmsn5qd9mq71o-oDB0A4SB9fH6QnC70VCy7r7WC_NlT5cnW8qaZDg_uLpCj0KIEJx9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74012bfe1.mp4?token=Pizqk6gQ5trVfe-DgqfIwy_qrci_beV8f4HiOLjke2IW5jkjZRLeJHlclVxTObvWhA8f9CJPxFsBrme4aXFx_tnK6Wvv-LZdXjlme13U08IbXOEEfd6QWrgyX9oPfaBe1yLABaCB5xtbR2DHXC76EuyGBMtooLCSK4r2RRgfZKJxb62RD5kk1d4wWfaKPrwpkGmomDDlYt9xeG4nV4DnCucMUIGLTho5SbtRS8i5-Ruhw4JSmW_agD2JxmzGxiyF_RMB-iY5oO2q-mMcKpZaiS-n3sPPqDjWcbiGcKWlsYkq0o1GkUw0TJbEmEj46OXwbzwEZrH_9-tp4lXumrlP-p5mbJMAMtcGEC2oYh_9T15gSzzycJ8dlD7_r-2BAlm9V7NMsKpKd6g9-ELhYV9WHag9jv96Fn5GjQfTLG566ylDfSx2nkK5521NozQkPmC_VFvEVr-J8Q8RlbldIuiUtkj3u_sa-oJGbCfZArfmfXsPs3bH96wI773FmSWTGtBj8_60Xfv7f8USwowxkRSq3UBLzkWvPQM5cDwNpi747uzpds5WtXlV6kDnP0Dxj-XSYV3xs_5PS5Po7X2FntSGDLjiLtxhtSBam93_PoTtmsn5qd9mq71o-oDB0A4SB9fH6QnC70VCy7r7WC_NlT5cnW8qaZDg_uLpCj0KIEJx9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار لبیک یا حسین مردم عزادار در کنار خودروی حامل پیکر مطهر آقای شهید ایران در مسیر تشییع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667255" target="_blank">📅 08:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667253">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b05339ecb.mp4?token=PdWSXYfHezBq4zevCcti6NN6B0KWq3uab-AARaQyTCZooa7Bnwveq2W0W68H5kKUBSxmDd5fNGgK1zd_jkAzLNtMeSl1bo-NPMoBdZlBoxVrW5UyLItEJ4SHbr_1Vv9zCTmwik70clQG47qJrUTvH9c3ZERBY3S_SG6b9q8bXp_fseUT4Xt_9bLdDbjEEk6sCIVdfBgcotfz2whqIHxk_v1FWQu52iQNb91CXfRX_sJLsWnxyUktlIfgO_CIA9jYrxS2XXKclNFl0tcNCvlZ97QpvPfPSc9GzuWVLorzxTlBhCiHQXf_IUB6aESZb_u-R83joRfBhid05AsVrQ8zST4hYVLUxEZ4gBeR_z4AVdGrAxZXq7Da3ILLezFW3wpqSJyTq8IV0fTixJ0sJWMF49Rybssq88S5F8bx2nUwLFRYtfOZHF3XjojOMhnUMB6nrNl0UqsKHYjiGxW_5OVch469R21_oacTbDzlQab3U8xldsJLYboQ5UCQ140aMewe72lfN5COJbM8g_cRHQv13BSCjI3azmlYMnaWozHiN99neg_n55y_k2MMOFx4Q0YHBz-v-q2l0LHfi9q5dBRgng5NnUC0CyBgeFS5Du7AQPXQlU_f2sfPH2JdfWm6Z01O7hXvZfvpgVFd9es_4gt0BVPkNUCmJKIM8OwWxjtLNl4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b05339ecb.mp4?token=PdWSXYfHezBq4zevCcti6NN6B0KWq3uab-AARaQyTCZooa7Bnwveq2W0W68H5kKUBSxmDd5fNGgK1zd_jkAzLNtMeSl1bo-NPMoBdZlBoxVrW5UyLItEJ4SHbr_1Vv9zCTmwik70clQG47qJrUTvH9c3ZERBY3S_SG6b9q8bXp_fseUT4Xt_9bLdDbjEEk6sCIVdfBgcotfz2whqIHxk_v1FWQu52iQNb91CXfRX_sJLsWnxyUktlIfgO_CIA9jYrxS2XXKclNFl0tcNCvlZ97QpvPfPSc9GzuWVLorzxTlBhCiHQXf_IUB6aESZb_u-R83joRfBhid05AsVrQ8zST4hYVLUxEZ4gBeR_z4AVdGrAxZXq7Da3ILLezFW3wpqSJyTq8IV0fTixJ0sJWMF49Rybssq88S5F8bx2nUwLFRYtfOZHF3XjojOMhnUMB6nrNl0UqsKHYjiGxW_5OVch469R21_oacTbDzlQab3U8xldsJLYboQ5UCQ140aMewe72lfN5COJbM8g_cRHQv13BSCjI3azmlYMnaWozHiN99neg_n55y_k2MMOFx4Q0YHBz-v-q2l0LHfi9q5dBRgng5NnUC0CyBgeFS5Du7AQPXQlU_f2sfPH2JdfWm6Z01O7hXvZfvpgVFd9es_4gt0BVPkNUCmJKIM8OwWxjtLNl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون تجمع گسترده مردم در میدان انقلاب؛ فریاد یک صدا خطاب به یزیدیان زمان: هیات من‌الذله
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667253" target="_blank">📅 08:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667252">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6199eaa2.mp4?token=CzJSiG5ZIMNt3JOFNG6GQZB3zRGaTmW_6enhAK_8A3ZKuAEGQYxKn00oYildyOgsLpTWXlQmULpnNfBkSziiaMxtn6RVN0YLN1rLvw3s7EYCcIbb0pLBzqLy0JPg1WjAib0ROCyixE5jNB_U_q6cPNBVz2nI1h97OfEX_W6Af0Dj88SarqpMax0C6iVFtF7PjpjZ9gPLLr1-KFZfql96CIvSN973prDPP5NyQffJ75tb4sOB6FUekzW3iXj0WPHJP4HN_uXbfBuzCncfO52ZHNsc2FSgeVJql4fZg-fLXZed6s6VDY6ZuiPPqvViWT9Axh_OIyRX3hJ9SWHDjvguZxYP-z2HEmQvY79rmzomMPzlOLAk6ASYkJiksOGbYsHmEiUL08LDexvSbllblRdGyO7bDU5_A-tF3BxaUDgVwChF5EdvtClvYTRxlOr84jdgU9o0vyYASCYKrHPnk7Kv8s3YGTb1SfLSY-2jMuHnKQhVZD3iWFewCY9mLXwwJ05laLqR6tdKMs7AlDmYmNBt8vTqA5Pmc9lvryYgLk7sEMyqswF6cCyvYeMnVXZTjmyhI4zc-GK8oQubCq1IpcCVIumKK9c2ihCDH_knOQILsv76mT1FsG4C25UfDfJ9PmpVFF3IOSsM3eWvZWbgo8hHBMtsu5Gu-YrvJOWMCMdlMY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6199eaa2.mp4?token=CzJSiG5ZIMNt3JOFNG6GQZB3zRGaTmW_6enhAK_8A3ZKuAEGQYxKn00oYildyOgsLpTWXlQmULpnNfBkSziiaMxtn6RVN0YLN1rLvw3s7EYCcIbb0pLBzqLy0JPg1WjAib0ROCyixE5jNB_U_q6cPNBVz2nI1h97OfEX_W6Af0Dj88SarqpMax0C6iVFtF7PjpjZ9gPLLr1-KFZfql96CIvSN973prDPP5NyQffJ75tb4sOB6FUekzW3iXj0WPHJP4HN_uXbfBuzCncfO52ZHNsc2FSgeVJql4fZg-fLXZed6s6VDY6ZuiPPqvViWT9Axh_OIyRX3hJ9SWHDjvguZxYP-z2HEmQvY79rmzomMPzlOLAk6ASYkJiksOGbYsHmEiUL08LDexvSbllblRdGyO7bDU5_A-tF3BxaUDgVwChF5EdvtClvYTRxlOr84jdgU9o0vyYASCYKrHPnk7Kv8s3YGTb1SfLSY-2jMuHnKQhVZD3iWFewCY9mLXwwJ05laLqR6tdKMs7AlDmYmNBt8vTqA5Pmc9lvryYgLk7sEMyqswF6cCyvYeMnVXZTjmyhI4zc-GK8oQubCq1IpcCVIumKK9c2ihCDH_knOQILsv76mT1FsG4C25UfDfJ9PmpVFF3IOSsM3eWvZWbgo8hHBMtsu5Gu-YrvJOWMCMdlMY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید: همه ناراحتیم، اما پشتیبان رهبر جدید خواهیم بود؛ تا پای جان از رهبر جدیدمان حمایت خواهیم کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667252" target="_blank">📅 08:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667251">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7mOP7ZdQ_T696D3g62U1TRpsuBzKMj2NBXHC93FI6EOfb4nLncuHCUPJ7O1rCfLeuB9MT6JvwXe5JweZVAOkGBgOhvcFSCXLFEG3_rOGN3FSUo02NfXJAyL4PMUKMaL9j0xzpIuXVUA7EgwIYrzUCP1F8pZqeDLw_GZ08cVX751oCkqPcOnJReg2d_nou9gFxlEjdTK5KEd9PNf4QGdaXA6_giilRAVLKQ_LIHIkBgHlb7wUg6q4FDgxdDuLH4KA2mS8d2ZWgRPiKHEmzIuRm-xlgziUVhmHW2nwI757Kez8xxA3mi6pwzX0hmWmzp_eQQtYXphs9UeH9O5GAiAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دریای خروشان عشق و وفاداری در وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667251" target="_blank">📅 08:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667250">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d26ff3524.mp4?token=eRgH-iyO8dBSutQFl6O3HgzM6b9buNjxxNxMO3Tk_Ju9uYBr0aKEUWUD5yanLw1PDK5DD4cEV5Yvh2XXSADsgoWZ0PuV4cslILXqvHbbqltxKjn5eHLSbWzhLkgattlngwFCGopl6UB40-etE_WKwV-NDQxdw1EPLOHHMfRwTOfXZJq0PqVTP85y55xX5FJgzNrTqVv6TSbaByMRXqplhxntyyDsW6VR9K7h7hkJkzmfmDtKPCBnIA9_dhv6P00g7nJNoBiIgQIyUuYYrKTY-0IRO8TGprLXulI191p9fFTJoYK2Pgfn0Gj8_CUtOlH3q8ifdfv0k3pa8upKzOPBzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d26ff3524.mp4?token=eRgH-iyO8dBSutQFl6O3HgzM6b9buNjxxNxMO3Tk_Ju9uYBr0aKEUWUD5yanLw1PDK5DD4cEV5Yvh2XXSADsgoWZ0PuV4cslILXqvHbbqltxKjn5eHLSbWzhLkgattlngwFCGopl6UB40-etE_WKwV-NDQxdw1EPLOHHMfRwTOfXZJq0PqVTP85y55xX5FJgzNrTqVv6TSbaByMRXqplhxntyyDsW6VR9K7h7hkJkzmfmDtKPCBnIA9_dhv6P00g7nJNoBiIgQIyUuYYrKTY-0IRO8TGprLXulI191p9fFTJoYK2Pgfn0Gj8_CUtOlH3q8ifdfv0k3pa8upKzOPBzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار فدوی در مراسم تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667250" target="_blank">📅 08:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667249">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23131f49a0.mp4?token=n8yTEOmrVZl7IVlREvgfVyXoGl9DexrKH-q5TWfNWj0kzYG1NZ_kl7XaWPDogSFUqP9YUVMpGB_xyfqqYLn7OfDgR9IhwY2Px7sce6AM69GUIET7hPSo9Hxq-WIZqGliIdQpq00UZRj1BRYjjfSJwG0oFNMyfngfGzrK3yUbHly5zTkbTEnv6HygRZjPLuI1uozNZkjVBzk4fzqpRf4Nm0KH825QJyhYGG4LVHOo9wjgz1zX1vwaSXkrSjzgCIYa9OjAYBHz1EQKBSuPjUNhuDQ7o3H27axgD4wbHHsvo6WTyNBEwB0oDe_sxuLuoUViryZ6XPer_BD84eWo-Fanzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23131f49a0.mp4?token=n8yTEOmrVZl7IVlREvgfVyXoGl9DexrKH-q5TWfNWj0kzYG1NZ_kl7XaWPDogSFUqP9YUVMpGB_xyfqqYLn7OfDgR9IhwY2Px7sce6AM69GUIET7hPSo9Hxq-WIZqGliIdQpq00UZRj1BRYjjfSJwG0oFNMyfngfGzrK3yUbHly5zTkbTEnv6HygRZjPLuI1uozNZkjVBzk4fzqpRf4Nm0KH825QJyhYGG4LVHOo9wjgz1zX1vwaSXkrSjzgCIYa9OjAYBHz1EQKBSuPjUNhuDQ7o3H27axgD4wbHHsvo6WTyNBEwB0oDe_sxuLuoUViryZ6XPer_BD84eWo-Fanzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت عظیم مردم در مسیر حرکت خودروی حامل پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667249" target="_blank">📅 08:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667248">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d37ce8846.mp4?token=dBIPN7sarkr_PC3Uss8DXi9WzysgjKvCx_5FKSBHkSkg7UC8wOWlSTDL1_IMArI_WdGYuI73vCtdZs4xTVzchjyWe0pLWPHgdumTCEPdCjMPa-qTItNfpRMkwC_j5r86mUuVEeLvKbz8oke50h2UXRrjlw_jDfXzkGJrcYJlpElVlFrmEvzwIlwRlcjHGMuVJnSZ2k7Mu5dUVAdWwgG2RE72ryQ2Y_YPnViAhrKxmfWoRDal1wMamxZZCygkEZDjgU7jZQQ7XGJb017t2Ojs53xK_jjtMkrazu1myL0hKOSwPP4XwHNv9pPO10gcE6ZIgPfDObs3KhKSCWrizrajmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d37ce8846.mp4?token=dBIPN7sarkr_PC3Uss8DXi9WzysgjKvCx_5FKSBHkSkg7UC8wOWlSTDL1_IMArI_WdGYuI73vCtdZs4xTVzchjyWe0pLWPHgdumTCEPdCjMPa-qTItNfpRMkwC_j5r86mUuVEeLvKbz8oke50h2UXRrjlw_jDfXzkGJrcYJlpElVlFrmEvzwIlwRlcjHGMuVJnSZ2k7Mu5dUVAdWwgG2RE72ryQ2Y_YPnViAhrKxmfWoRDal1wMamxZZCygkEZDjgU7jZQQ7XGJb017t2Ojs53xK_jjtMkrazu1myL0hKOSwPP4XwHNv9pPO10gcE6ZIgPfDObs3KhKSCWrizrajmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور نیروهای حزب‌الله عراق در مراسم تشییع قائد شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667248" target="_blank">📅 08:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667247">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a28d733f57.mp4?token=lg200W_SRg8rQPKBLRWEpHJVNX_xS0debrEOnLrWipluBo_6FFyTY56HNs5bSPu3_oPHqtcP9T5Tm-1dKhQ8kF61VbRYhJYx_fwuBjXxHg-DY3k4gvWjfknNPdA0h1YCKe76DA94HNmGsZncAlWEwa_thlc29dgNARRjkuy3z6W63wbn3DeIPhbED242eFXl0h5kC60maas1AgTE_tqmc_POBZZbsqTl4BK0d9IHuPsXXoFMd7V2ayEZ7cXXTkMyWxK-IAyO9WsfirpmogrF5sRHEZgIqCc4sArChHLihujOM6vEYEqTcr_KuhaqRY1jSAQM2_7JrVrtkXL8Xiwt1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a28d733f57.mp4?token=lg200W_SRg8rQPKBLRWEpHJVNX_xS0debrEOnLrWipluBo_6FFyTY56HNs5bSPu3_oPHqtcP9T5Tm-1dKhQ8kF61VbRYhJYx_fwuBjXxHg-DY3k4gvWjfknNPdA0h1YCKe76DA94HNmGsZncAlWEwa_thlc29dgNARRjkuy3z6W63wbn3DeIPhbED242eFXl0h5kC60maas1AgTE_tqmc_POBZZbsqTl4BK0d9IHuPsXXoFMd7V2ayEZ7cXXTkMyWxK-IAyO9WsfirpmogrF5sRHEZgIqCc4sArChHLihujOM6vEYEqTcr_KuhaqRY1jSAQM2_7JrVrtkXL8Xiwt1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین تصاویر از داخل خودروی  حامل پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان  در میان خیل جمعیت مردم عزادار
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667247" target="_blank">📅 08:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667243">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_R7GoOkulaHRIWfCAS-nTDIdoFj4osxQOdlqGDCAcxuISGUkZAMp4YNs9Ms78k0jJ56yxR2mFIj9sCknYfQjQTY6gFqjjTjO5JviY_FIMdCmevVIAICo-hvRsIzD4NHFwyRuQn4hVr8rbiaPfnx99HFpIO2ffigd9JzXqGWK6VTVgkQ5kT0H-TEF406EcKSEkg_O2-XwQfbpn5dwSrF3R-2xHtf1k2eUaYMFrtpXhMt09FH_3ZHDttCt94379wA0qXkleXsZDZ6chkY4X99-Qvt4VNqbExB3D_69OeBwrfC4pRrA4-OINoos7e_gOM6Qt2ZE28fY_m7v_CISnJ09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQ76gAj6Nk9bSekFdDk9ENcxaHLQZ-M_1YSsDLzBe5wBgD8FRCHKZaFyGgegymnY4iolGFHju4y-HTRpbApUDQjXHR2U_ElT0lw8jfcchrjM_nuePEnZp6-oFMABvz5fqKxkFcqziutX3yGXUIwsApFGlGEXFroYg8OV8on8b-uckNPyM_N3jv8N5lQcGEheK0Jmf-ebbs703PqYZxM57qyZXHfhf1SQz-8fuLg6Jv8cfjR6mSzu7qvyNZlzyNbeJ9uZ1BXXftomR_3CncCG6YAbttrAmmzYLnMzse3RBEcgQ2s4Sl-yY1FFWpkJ59EDAwWY9PjCS9UpVWkYcxQdZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KK0usomBvy7wDqhCb0cbfr7ynixq56Qaqo9bAexZxgkrG92qBN4S7sqTloIZvgBNKRdkL3K0pzRuP2_QMMa1CKte28fHC8wZDjmUPJUndUdyADT_4CTwMMQaE1CO_Zn5h3ysNw47n441nDMOjNreTS6rnGz0xQZGVcCFI1E46DTLJuhAyhbhzjHXZGEdUfMP-rUO1RgWia6bgQESW8Kz-odw5bYjTOXWan52sw3TwlgZVPpHOeqn2FfKL-e2vynZld5yV0ws8UkfCAIwwgQWTxoVg-IgYgeFv5DOo7YKfuhy7_BD8kTOrkordEeIU1TEgT5QGlvpnxgjZ7xb_8jI6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a1497c08.mp4?token=l7FCioMilHE_7Ucsovn06MLWpsea6LQpMSUDSmHphJ_SXCufwsmdhDT9uANWPa8QH3JG4xib1CAO_UChiuBvAXEKJis1KJYfeyVlcMiG6AacdACLCvyr4ceUAjoUTY5g68blUlI3weJFVd21eG4Fsqrvdm1S_pA3UGmPo5jdCvbv0CLDZ7YJmh1KZwNLGyPfR7xqE_O_-ZrhSpiP_sekVHtdYG4aJ77yStgcCD_WQ1uE76zsb2delQbisOKnm4gypPZiNJgZYNotjXhhPrUkoktFcGMK62YWdJF7lJB4iJegJNuBtvjuacvCd3nGwPAD7Xl97h9MMkAuWJOrn9CHbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a1497c08.mp4?token=l7FCioMilHE_7Ucsovn06MLWpsea6LQpMSUDSmHphJ_SXCufwsmdhDT9uANWPa8QH3JG4xib1CAO_UChiuBvAXEKJis1KJYfeyVlcMiG6AacdACLCvyr4ceUAjoUTY5g68blUlI3weJFVd21eG4Fsqrvdm1S_pA3UGmPo5jdCvbv0CLDZ7YJmh1KZwNLGyPfR7xqE_O_-ZrhSpiP_sekVHtdYG4aJ77yStgcCD_WQ1uE76zsb2delQbisOKnm4gypPZiNJgZYNotjXhhPrUkoktFcGMK62YWdJF7lJB4iJegJNuBtvjuacvCd3nGwPAD7Xl97h9MMkAuWJOrn9CHbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای دیگر از خودروی حامل پیکر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667243" target="_blank">📅 08:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667242">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d72V1GZ-nxCEnqwi8yWZ6DUIKPlN3fDt5VJ5p_wzOOgxeybQf926w1CaBE-PrXNlGmaWXeusspHSri4QFUe47KCIogzMRJGLdONKDB-GRuXJeiUeSGNRSQO1E-EczbI9Xn9ScDwFj8P0_2Zm1gDD3w03RTS2ZkOdLvDn09np1rqVWkNrl_iqReFJRtungrtXBxn6odYC5GQEjndGKGK7vcmdxmleJA69oY0S5wn0jHUHaMDF_XYJUectMBhZ5Cx-nau6LU1POUtxWgQoCmLiKPf7cerm6imKQKpjgaP0ZAWn4Pbng5ubxyxaMZQDVo5Mh1YlR4echr5P9COgIeliNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: خیابان‌های تهران برای سوگواری رهبر شهید ایران با جمعیت انبوه پُر شد
🔹
خبرگزاری انگلیسی رویترز با انتشار تصاویری از جمعیت انبوه عزاداران و سوگواران رهبر شهید انقلاب اعلام کرد که خیابان‌های تهران برای برگزاری مراسم تشییع رهبر شهید انقلاب با جمعیت انبوه پُر شدند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667242" target="_blank">📅 08:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667241">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYRT-b4FltREqkaBZ2PsGoK1n3AnJzRM7h6NtzuKnmlhETIieW-amM9n-ydosJU3xBdKNJUGwZRBji7I7lGFs955YEZsFoPvbCQojF1Py1kdoSisltw43dI6sVLOp2EGcUZb7WZuWAt7YlV50VggKLReVr5O_qYtkU7x41dB9xVgtjwVHsNDN7Jg588tML77vA6TbNOC9opCIPr51YSlAd1uRzOIceqD4dykY7i3oGok2_Vpj0mLodpdV_zUCtU-q_Bh1RmKCD5pWg5nHWbmC5LmnXpRlu6mKau4sUPP2R4nZQyhpSCXFKwS8fZJHTt0A52T7wvqwZfX3dUqkVpEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز حرکت خودرو حامل پیکر مطهر شهدا در میان سیل انبوه جمعیت #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667241" target="_blank">📅 08:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667240">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e3e83030.mp4?token=GEM6lkfXZ_wkvwz7ODa-ManheEnAMfinDM2vfzAkZAlqwqLaA-cpyca8fYCVezGSVccH4lbwim8YqwboFAEFknBG7GT1d7I3PTbf7OIOqVAv_5etlbxuxOaVnrTdclRIFHli3CCNldoMtHPrhBcFqtskpknAcdcgCyqFZuo5JwBYZsEOcCgeS9kOcat1zrnzBcLZbIFQDMvGutYysAAwG5bpqEjZn3DU9pWYxKQUGtM2JIi8o3U5bTZlehN6WY7FWxB91-XJ8-cIJJbv8i9meq6C8wbIq0uw1dcs1hWXpDUiR9zWTSOowAY3ZBLVyAa_LI8Em_BbGezKMEJGjGirqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e3e83030.mp4?token=GEM6lkfXZ_wkvwz7ODa-ManheEnAMfinDM2vfzAkZAlqwqLaA-cpyca8fYCVezGSVccH4lbwim8YqwboFAEFknBG7GT1d7I3PTbf7OIOqVAv_5etlbxuxOaVnrTdclRIFHli3CCNldoMtHPrhBcFqtskpknAcdcgCyqFZuo5JwBYZsEOcCgeS9kOcat1zrnzBcLZbIFQDMvGutYysAAwG5bpqEjZn3DU9pWYxKQUGtM2JIi8o3U5bTZlehN6WY7FWxB91-XJ8-cIJJbv8i9meq6C8wbIq0uw1dcs1hWXpDUiR9zWTSOowAY3ZBLVyAa_LI8Em_BbGezKMEJGjGirqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج حضور مردم پایان ندارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667240" target="_blank">📅 08:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667239">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d00af951.mp4?token=SpAtFsOkHiQlyOCaKDRm750A0w27v5FMtizGSCGlYzVsUVmWBA5qBPhyPoMfcnbxmTQLWUqx2kD7MSUTWNqPmz5SeAauspeJqheQZzzGs-HM1Tke0JG6i6yQj-4Oz-5pBIpsHkxUvRmoVwalEpl_LcKYHIdnW6L3_uzcq0C9x566F77wJJnsukUQQ7vPDVi59gexhjpIXz0XeTxeimtMOH3gJbNx3v4xu1RpqroHJx0Q0QaIb06eoNUT0wwqwfhpPmug55ZB0rNRbpL8qSumX4N7lm7iRvM9SryvoDQKYHdlEmVyCBatDnjTZFwjGLQFcvFfF3Kbq2lPTuAi6YZBkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d00af951.mp4?token=SpAtFsOkHiQlyOCaKDRm750A0w27v5FMtizGSCGlYzVsUVmWBA5qBPhyPoMfcnbxmTQLWUqx2kD7MSUTWNqPmz5SeAauspeJqheQZzzGs-HM1Tke0JG6i6yQj-4Oz-5pBIpsHkxUvRmoVwalEpl_LcKYHIdnW6L3_uzcq0C9x566F77wJJnsukUQQ7vPDVi59gexhjpIXz0XeTxeimtMOH3gJbNx3v4xu1RpqroHJx0Q0QaIb06eoNUT0wwqwfhpPmug55ZB0rNRbpL8qSumX4N7lm7iRvM9SryvoDQKYHdlEmVyCBatDnjTZFwjGLQFcvFfF3Kbq2lPTuAi6YZBkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌های مسیر تشییع پیکرهای شهدا مملو از عاشقان رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667239" target="_blank">📅 08:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667238">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257bff6b38.mp4?token=CQZ6uwXqZiXHLSUuBysWm2mhKAaT02Al0NJw9T91USK5fjIHjF7U0L-cB-5RtETCqnMwzk2AH9-0_6oWSnbnEbeBPWsa5aohmJIJxGDH5GIuHJiO8WTJQwzpaQBxbjnYm5GtrFulIG3WNYM71jPeDmhthVIV6ufGFNPMCvffAv6dG1Cy_8CRSGbwL1Eo8FI7YutMc4goeoZMRu7S55onWTYCgh0hBn53zpXKf3-ziIZ8_7fI9C73PeJ424xxgT7MyIpkVIC6l7k43G5XgglBCioHmdGZiDw3dxKMs9_JBXCNHVX4LJ6mpKxsUOwbOEuaxH0D0XSn7V_zwm44jHdu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257bff6b38.mp4?token=CQZ6uwXqZiXHLSUuBysWm2mhKAaT02Al0NJw9T91USK5fjIHjF7U0L-cB-5RtETCqnMwzk2AH9-0_6oWSnbnEbeBPWsa5aohmJIJxGDH5GIuHJiO8WTJQwzpaQBxbjnYm5GtrFulIG3WNYM71jPeDmhthVIV6ufGFNPMCvffAv6dG1Cy_8CRSGbwL1Eo8FI7YutMc4goeoZMRu7S55onWTYCgh0hBn53zpXKf3-ziIZ8_7fI9C73PeJ424xxgT7MyIpkVIC6l7k43G5XgglBCioHmdGZiDw3dxKMs9_JBXCNHVX4LJ6mpKxsUOwbOEuaxH0D0XSn7V_zwm44jHdu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز حرکت خودرو حامل پیکر مطهر شهدا در میان سیل انبوه جمعیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667238" target="_blank">📅 08:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667237">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4271d31f.mp4?token=JY6DtUz5ivlFi46P8q3F-gkNdOIFbme70r012wRYCB_198n03o-Ki7cwTh7nm7VcQMx4s-rkus7sID7enOn8oqh-d_QdZ2Wq6X7f4VcmoImlW94CwyS12q0cgn9g80ZKdqOJ5PT9IxH1bFlVckziFRtkAd2YDvnLQ9MQNiBGD7KCr9pZAitJ8mm9UIUhRUMnzBAcbx5ciM8LW0UpIEuCdfGrmJScYJ-HugS-zTkGWK8OacndHsojMD8qXSmQCK4sgCA_e769tXi77JHkIG5Jvb7ek0pA2hzy2N5-WEwJrdNNM3EFbcLmEKXl64uT9RYrbMATJfqEp74_FX5Dj_8jyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4271d31f.mp4?token=JY6DtUz5ivlFi46P8q3F-gkNdOIFbme70r012wRYCB_198n03o-Ki7cwTh7nm7VcQMx4s-rkus7sID7enOn8oqh-d_QdZ2Wq6X7f4VcmoImlW94CwyS12q0cgn9g80ZKdqOJ5PT9IxH1bFlVckziFRtkAd2YDvnLQ9MQNiBGD7KCr9pZAitJ8mm9UIUhRUMnzBAcbx5ciM8LW0UpIEuCdfGrmJScYJ-HugS-zTkGWK8OacndHsojMD8qXSmQCK4sgCA_e769tXi77JHkIG5Jvb7ek0pA2hzy2N5-WEwJrdNNM3EFbcLmEKXl64uT9RYrbMATJfqEp74_FX5Dj_8jyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری سنتی و «گِل مالی» لرهای غیور در مراسم تشییع پیکر آقای شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667237" target="_blank">📅 08:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667236">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3daf03cc.mp4?token=TyY_OLOwNGCND6hASz4Ew0oL4ZFKjromoBWG21AhouSN73SLcioMcsXSEOxQ8iuwqJxbux69zPjib4KDTQpYSDok0BX7HV5lkTIbNcMkVox_3QysC_FtdfhaRN0EtF5qLUt2Ugy1Xu4rzBmldogNrR6qTV4nvU7_mCfV9OVFjDoNc7RDLotWJ6nd5WQsX8qYV7OtiPI8x8xvXLebv1SuZ4VdzyaWhGx8aFriWOZxELBkLBnzlQ44CuK3N8eihn21a4JaC5sOYgAruszSiCZWjX-adVn654I66RfvbGGwcNdHZhU8N2NYmaai5T014vm6R-dHONzCsC7JKCsa_WmMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3daf03cc.mp4?token=TyY_OLOwNGCND6hASz4Ew0oL4ZFKjromoBWG21AhouSN73SLcioMcsXSEOxQ8iuwqJxbux69zPjib4KDTQpYSDok0BX7HV5lkTIbNcMkVox_3QysC_FtdfhaRN0EtF5qLUt2Ugy1Xu4rzBmldogNrR6qTV4nvU7_mCfV9OVFjDoNc7RDLotWJ6nd5WQsX8qYV7OtiPI8x8xvXLebv1SuZ4VdzyaWhGx8aFriWOZxELBkLBnzlQ44CuK3N8eihn21a4JaC5sOYgAruszSiCZWjX-adVn654I66RfvbGGwcNdHZhU8N2NYmaai5T014vm6R-dHONzCsC7JKCsa_WmMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم مکزیک به انگلیس توسط خیمنس / برد انگلیس ۱۰ نفره مقابل مکزیک در جنگ فراموش‌نشدنی آزتکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
3️⃣
🏆
2️⃣
🇲🇽
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667236" target="_blank">📅 08:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667235">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54092b1eb.mp4?token=H9k7WmMrsK1OGIqT4fChJa7ECgD-eOpGbC8_kx4vXViqXnE_W1yRFoIhoEQKE1UMlV110aAWmuphYza9QNr7TzdvLH4emk0SpH-VGhY4-NNjq0XGR5NOwUCstiLD5dUo8nWt5Kx-MFIRJy7vMfc-lEEaywfNs14EnrlhJRn3RLSrEcpayglYSvlIa0BwuTy3azLbPydIvZAL5q3uEXQa2OWc34ZkWc-CAfF4ayXKYK91DZAUIxHwUTzN0v4XnuTZMswdNgbWSuyY8IqJoOpkDe-5LSEdHnW_cGO3TUddrJyWf8SWj9YxW62SBbSchQ6q1-WQMhvHv93vlVwo44km5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54092b1eb.mp4?token=H9k7WmMrsK1OGIqT4fChJa7ECgD-eOpGbC8_kx4vXViqXnE_W1yRFoIhoEQKE1UMlV110aAWmuphYza9QNr7TzdvLH4emk0SpH-VGhY4-NNjq0XGR5NOwUCstiLD5dUo8nWt5Kx-MFIRJy7vMfc-lEEaywfNs14EnrlhJRn3RLSrEcpayglYSvlIa0BwuTy3azLbPydIvZAL5q3uEXQa2OWc34ZkWc-CAfF4ayXKYK91DZAUIxHwUTzN0v4XnuTZMswdNgbWSuyY8IqJoOpkDe-5LSEdHnW_cGO3TUddrJyWf8SWj9YxW62SBbSchQ6q1-WQMhvHv93vlVwo44km5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار زائران بندرلنگه در چهارراه ولیعصر: انتقام انتقام
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667235" target="_blank">📅 08:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667234">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e26d1aa65.mp4?token=elIf3jKpDyKBsToQdUK3jj5lB5KqY6YFVnoHHlHwgJyqVSUVk6MyL21XIfTI-jEeq8ROTkQQanWnOBjTaMsY_v5C_RgFRYtcrnP2dSLp8Jm0bG5mk2qKBro1Ln4jR0Mi2WunX5rg8YqFH1kI4-linMRoXisuQg44tTyC029XS3AHZcKQU2h6JXDfR8dkAtmn2o6Q2n64xZ42ar2MNUKhkffqc-Rmo92fn2mk-hZI6lUGxleWYkWEv3e9LOxz527S8SEhs3WVFLLsd9S7Y7WwO0XI1gfzoQhduVzNk0Yd14zL5mY0w7qXiUe_AiiVR25XSKwb3g6FLcEF3ebEfQ4CtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e26d1aa65.mp4?token=elIf3jKpDyKBsToQdUK3jj5lB5KqY6YFVnoHHlHwgJyqVSUVk6MyL21XIfTI-jEeq8ROTkQQanWnOBjTaMsY_v5C_RgFRYtcrnP2dSLp8Jm0bG5mk2qKBro1Ln4jR0Mi2WunX5rg8YqFH1kI4-linMRoXisuQg44tTyC029XS3AHZcKQU2h6JXDfR8dkAtmn2o6Q2n64xZ42ar2MNUKhkffqc-Rmo92fn2mk-hZI6lUGxleWYkWEv3e9LOxz527S8SEhs3WVFLLsd9S7Y7WwO0XI1gfzoQhduVzNk0Yd14zL5mY0w7qXiUe_AiiVR25XSKwb3g6FLcEF3ebEfQ4CtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تایم‌لپس عزاداران رهبر شهید در میدان فردوسی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667234" target="_blank">📅 08:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667233">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc32cf0c8.mp4?token=e4Ffwy-JU62H1a6RcXbPuNnRyMODq2F69jDX0xlGYim3p6ZfMWH2xBcd1pz4EwYYYykFgr8-_vtuWEYdAWItxoJZFiRRAhQqoMq2F7l87NX6IdwYRChTVWvkmC6TwMx1WGytlfLmTMhAteXfcaliSiVArCuQt3odHwb_bpiE2s1AWi6MHXanteGgL9PLpRrIEmdxlEAOKFQRGBFjv6LIlo2e1HkDO-9l04CB_hJ-5vHf7lY1Pf8190WlOFuZSzW6gdzGDPF_-umCUp3CF0bteDQ1pstVsvW4byf-PX9ZK-PoIlL0Jp9GMv-ZPxao_hUU3ue26qMV2cdH15MeGy6DJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc32cf0c8.mp4?token=e4Ffwy-JU62H1a6RcXbPuNnRyMODq2F69jDX0xlGYim3p6ZfMWH2xBcd1pz4EwYYYykFgr8-_vtuWEYdAWItxoJZFiRRAhQqoMq2F7l87NX6IdwYRChTVWvkmC6TwMx1WGytlfLmTMhAteXfcaliSiVArCuQt3odHwb_bpiE2s1AWi6MHXanteGgL9PLpRrIEmdxlEAOKFQRGBFjv6LIlo2e1HkDO-9l04CB_hJ-5vHf7lY1Pf8190WlOFuZSzW6gdzGDPF_-umCUp3CF0bteDQ1pstVsvW4byf-PX9ZK-PoIlL0Jp9GMv-ZPxao_hUU3ue26qMV2cdH15MeGy6DJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم انگلیس به مکزیک توسط کین
🏴󠁧󠁢󠁥󠁮󠁧󠁿
3️⃣
🏆
1️⃣
🇲🇽
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667233" target="_blank">📅 08:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667232">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dc76de03.mp4?token=R554RKvgEMoZYaJb8MH4fIiA1r3NNpRcqhMFh29NfQwPakQB57QDC1l0VJQqPO_Lq8MAkb3TSd9D-5uwLda51oZr2B0LRmpOlMj-RxLuOWW78qfD5oMKekCePolHGF5rSneUWN8oNYBpG5GKYVnQg_HWyEC_kAoQ3mRlgDWO0BbFO-ee5JEJAdzCdAmYyk60r1kkmRUkGmAK7VA3RjkPBItLL6YXv9_PqhWKkX4NR8mfFXM36He5q_lQXzbO5HWbFIbuMn8XGBE2gZiK9KhJcHOu_p9Iq4q7bm9jJVYveup9CIQ5qPQe_ZZPbukWrGMoqpzNW2v-MQ3eKLOwDoTuP68iEDIdGkLa5YoxuGlvb6HLc0neNjPJacyCxtavD9UoNKMcc1UtmMTeKcncqJQ6EiJ1Xt0t6VotPdoWd01Yd1fkpDguTvp9hN5F7aycNDH9I3AHF4kk8Aj27OZNk_XpgkkO68rgfavWwss1KBCQKIy_l6I6tuvHIqZ3OWkJNrAFXwjwYI_aVKbClTzUNObGtz-1y1hvbPk-C3k7tJ9dT93U8_uEZ5Qdq5YPQg3xc4uWzHtYQVVscoYBq2Ov12VotQSZ7pXH37CqZu4IyETm2FRwbBIIKYfUn2qiI7JxzFuscFrwheNQz-0VrM5bx8qSQgbCAyCyyZVYkrqVCzZ7WDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dc76de03.mp4?token=R554RKvgEMoZYaJb8MH4fIiA1r3NNpRcqhMFh29NfQwPakQB57QDC1l0VJQqPO_Lq8MAkb3TSd9D-5uwLda51oZr2B0LRmpOlMj-RxLuOWW78qfD5oMKekCePolHGF5rSneUWN8oNYBpG5GKYVnQg_HWyEC_kAoQ3mRlgDWO0BbFO-ee5JEJAdzCdAmYyk60r1kkmRUkGmAK7VA3RjkPBItLL6YXv9_PqhWKkX4NR8mfFXM36He5q_lQXzbO5HWbFIbuMn8XGBE2gZiK9KhJcHOu_p9Iq4q7bm9jJVYveup9CIQ5qPQe_ZZPbukWrGMoqpzNW2v-MQ3eKLOwDoTuP68iEDIdGkLa5YoxuGlvb6HLc0neNjPJacyCxtavD9UoNKMcc1UtmMTeKcncqJQ6EiJ1Xt0t6VotPdoWd01Yd1fkpDguTvp9hN5F7aycNDH9I3AHF4kk8Aj27OZNk_XpgkkO68rgfavWwss1KBCQKIy_l6I6tuvHIqZ3OWkJNrAFXwjwYI_aVKbClTzUNObGtz-1y1hvbPk-C3k7tJ9dT93U8_uEZ5Qdq5YPQg3xc4uWzHtYQVVscoYBq2Ov12VotQSZ7pXH37CqZu4IyETm2FRwbBIIKYfUn2qiI7JxzFuscFrwheNQz-0VrM5bx8qSQgbCAyCyyZVYkrqVCzZ7WDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برگزاری مراسم تشییع نمادین برای رهبر شهید توسط
شیعیان بحرین
🔹
در سایه خفقان و سرکوب شدید، شیعیان بحرین شب‌هنگام برای رهبر شهید امت دست به عزاداری زده و تشییع نمادین برگزار کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667232" target="_blank">📅 08:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667231">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5864b45f28.mp4?token=sc-N4qVGtAl6jA3gneA0I5O5MFZYhuHC8nwr6sx6OXlhSSfq2V42f2BtVQmlKN2aCtBlcBoSInOoj0bms7qC01XUTig4EccCXrViMPqV75GfCdr5J0ldL0533bLLPT-ZMmt93mmQBxLtgt0DJVKhOO-6pQwZOjmzgMow6BPTRTuQKZL6-VcfQGNLTHXZav9naxWrS0DCoweIYfqn_jQlUrAE4EGZmJcbRpWaEHg13oKEeIVbokj-T9MPccQGMURJq34rv4zzg6LBKcLSw44NrH4e_0VMM-Qgp7bgGW-IcFMlJt-HULJUdpYUTntnpfaBDJahPnmbuPZUgvGubqMqz1mfPqVKM4ERZm4aSqoPdiCsD4RZf1nP0Lg7azywZxlQmyBz1snRDaF4SSgFDrSkksQ0bilMqtQMmQKZ1ZZbxT3j1wQgvvB7ArGbZmA0Dd7_xcs7A6mY0CGtBSs3f_FbYg0QGNvv72wceMCZiR2lMhLpfG15xhmXslb_dBPJZwtoBHH0enhpQcnTgI-bVb7V-9Y4m07b02pBIWCr8W_JqQ6yuT5btbO3csoPb-HghGs89CdlQzdvhoMkwMwchEVuKQGMb6RHkrzowTcM38oD9iIpK68GvAXbu4fBQyNRH8cEb6GjuephvQTGwZEFPMBE2USpCbVWQupo_HpmpPHNYDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5864b45f28.mp4?token=sc-N4qVGtAl6jA3gneA0I5O5MFZYhuHC8nwr6sx6OXlhSSfq2V42f2BtVQmlKN2aCtBlcBoSInOoj0bms7qC01XUTig4EccCXrViMPqV75GfCdr5J0ldL0533bLLPT-ZMmt93mmQBxLtgt0DJVKhOO-6pQwZOjmzgMow6BPTRTuQKZL6-VcfQGNLTHXZav9naxWrS0DCoweIYfqn_jQlUrAE4EGZmJcbRpWaEHg13oKEeIVbokj-T9MPccQGMURJq34rv4zzg6LBKcLSw44NrH4e_0VMM-Qgp7bgGW-IcFMlJt-HULJUdpYUTntnpfaBDJahPnmbuPZUgvGubqMqz1mfPqVKM4ERZm4aSqoPdiCsD4RZf1nP0Lg7azywZxlQmyBz1snRDaF4SSgFDrSkksQ0bilMqtQMmQKZ1ZZbxT3j1wQgvvB7ArGbZmA0Dd7_xcs7A6mY0CGtBSs3f_FbYg0QGNvv72wceMCZiR2lMhLpfG15xhmXslb_dBPJZwtoBHH0enhpQcnTgI-bVb7V-9Y4m07b02pBIWCr8W_JqQ6yuT5btbO3csoPb-HghGs89CdlQzdvhoMkwMwchEVuKQGMb6RHkrzowTcM38oD9iIpK68GvAXbu4fBQyNRH8cEb6GjuephvQTGwZEFPMBE2USpCbVWQupo_HpmpPHNYDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‌
مردم عزادار در میدان امام حسین علیه‌السلام بصورت نمادین ترامپ را به دار آویختند
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667231" target="_blank">📅 08:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667230">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114b582aa1.mp4?token=Rr7YZFIKESgRWc5rLmyl48JKiUeA8N1WmsOTYvf8bQ6WXBYF1mGPPSig9YAn8wEYMtvJF7CPyEl-z3KVjtQbVY9xokVWUQguC_JjGWgdH-vCmmii0SFZUOlfoB6o4Qn8DPn2almme9Ce8R4Knnbk_wSAt_50_7tqSKTKkvODyPg5Vft1kiHbjbUFkrRNZw6XmLDk69HMC0MIKz-YXabhIieDxtaPTI51QGAJYOxYZJ_uxQnHNnlMhUQCGJQGrTfMlamaRb7PUeJqM8HkDZEX2zQ2RTOKs0KTnQFHZuxpSdBYYsH9hHfHTUqVVPQnlX7Xbq7PRskGwHbl0bYgNQCi6Ay1LCCo1nqQSkeiShHglitTmEkDMBzrhsTpTJm-ELKdwKAbfG1BoZKzW6EcLq_5u8uixvVwO2K7tmt9UIgjSW1f7-60d6Um_CnmBOVx8ZEehcxkQ5ewzIaIzADfk9huzRuQxZi90NY7Xh-Mn1k8Kcf9D7WL9-cgDH4Ls5Byz-krJC8-fkvXTDLrqD5L2Gd8bVWYt4kMzN7vVyiVRi-HTmvHTJfeuYW3aoF0olYSrnJgvBi_684p5JbCmcVw1JI8gup13OlPIeyxGAwkn6MjK3jlH0-tgNgZVHK_fJEm6PLWON2ZEzWyRuyEijJeH6sNvuaxeSGY9yObgHys8KxNHmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114b582aa1.mp4?token=Rr7YZFIKESgRWc5rLmyl48JKiUeA8N1WmsOTYvf8bQ6WXBYF1mGPPSig9YAn8wEYMtvJF7CPyEl-z3KVjtQbVY9xokVWUQguC_JjGWgdH-vCmmii0SFZUOlfoB6o4Qn8DPn2almme9Ce8R4Knnbk_wSAt_50_7tqSKTKkvODyPg5Vft1kiHbjbUFkrRNZw6XmLDk69HMC0MIKz-YXabhIieDxtaPTI51QGAJYOxYZJ_uxQnHNnlMhUQCGJQGrTfMlamaRb7PUeJqM8HkDZEX2zQ2RTOKs0KTnQFHZuxpSdBYYsH9hHfHTUqVVPQnlX7Xbq7PRskGwHbl0bYgNQCi6Ay1LCCo1nqQSkeiShHglitTmEkDMBzrhsTpTJm-ELKdwKAbfG1BoZKzW6EcLq_5u8uixvVwO2K7tmt9UIgjSW1f7-60d6Um_CnmBOVx8ZEehcxkQ5ewzIaIzADfk9huzRuQxZi90NY7Xh-Mn1k8Kcf9D7WL9-cgDH4Ls5Byz-krJC8-fkvXTDLrqD5L2Gd8bVWYt4kMzN7vVyiVRi-HTmvHTJfeuYW3aoF0olYSrnJgvBi_684p5JbCmcVw1JI8gup13OlPIeyxGAwkn6MjK3jlH0-tgNgZVHK_fJEm6PLWON2ZEzWyRuyEijJeH6sNvuaxeSGY9yObgHys8KxNHmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید: حس میکنم تکه‌ای از وجودم جدا شده/ حسرت دیدار رهبری تا آخر عمر با من خواهد بود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667230" target="_blank">📅 08:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667229">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f2afc386.mp4?token=i7KBJGomWG506NdmJgiNS90HcTn3KAhUzQEqQ5imrRvJFA7hVhNGnXsMnLcm8aKBCh3NNVN64WXFkxUBgZonwgk6BD6117xL_tJPIL789PXsnL2-Lh8mzeD2HouQMF6COVaeP1wIMHLPMymSOeGZ9QanqKHeerTDNclyMEwLbQ6wSKUFiA5LxLzWQMyD_hckqai8i9o6fWb8d4vKq24b9WNksJ-Y8LfxDS3ZneaFWDJPSeS5dvpanvAuObVqNmIZGWkeYY15ylSw_liD9HOMg49bC_rKJZtmJ5gppj-VDUqhXApFFCtX0BIfdwn6q3bi7Z4IQdpIdhROt1IoyCqZUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f2afc386.mp4?token=i7KBJGomWG506NdmJgiNS90HcTn3KAhUzQEqQ5imrRvJFA7hVhNGnXsMnLcm8aKBCh3NNVN64WXFkxUBgZonwgk6BD6117xL_tJPIL789PXsnL2-Lh8mzeD2HouQMF6COVaeP1wIMHLPMymSOeGZ9QanqKHeerTDNclyMEwLbQ6wSKUFiA5LxLzWQMyD_hckqai8i9o6fWb8d4vKq24b9WNksJ-Y8LfxDS3ZneaFWDJPSeS5dvpanvAuObVqNmIZGWkeYY15ylSw_liD9HOMg49bC_rKJZtmJ5gppj-VDUqhXApFFCtX0BIfdwn6q3bi7Z4IQdpIdhROt1IoyCqZUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول مکزیک
به انگلیس توسط کینیونس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
2️⃣
🏆
1️⃣
🇲🇽
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667229" target="_blank">📅 08:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667228">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1971ffc51e.mp4?token=Z1_pNvohKO-25flLFG7CCuAAT02XJZ25oz49r21VtepFtkvWCTuwDE-VE7kdOghENFmmuQrrRirk1Ya2jS38UrjhZsoKi_rRfNGcU5K6lt-W5iKbJSo06SiKmw2hH1lYbKwHHHM80CTJEGqGbc_-e4gQDV7KcufyCkSUNX43TwCuiDZXWZciFK-5RI4VvZJ849YJKwST8TLADA188P4ik9GpEjclGj1vXODsVdB05ydSdUAvBB_I95QRmZP-c59wyjxEIVdF5MeVCq7PCBRAvH98qj6SxOHB0W70IppQr54HC7B6uMamETgN2YgS3C2Ph_3uvxlEWBbepb24kfTDXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1971ffc51e.mp4?token=Z1_pNvohKO-25flLFG7CCuAAT02XJZ25oz49r21VtepFtkvWCTuwDE-VE7kdOghENFmmuQrrRirk1Ya2jS38UrjhZsoKi_rRfNGcU5K6lt-W5iKbJSo06SiKmw2hH1lYbKwHHHM80CTJEGqGbc_-e4gQDV7KcufyCkSUNX43TwCuiDZXWZciFK-5RI4VvZJ849YJKwST8TLADA188P4ik9GpEjclGj1vXODsVdB05ydSdUAvBB_I95QRmZP-c59wyjxEIVdF5MeVCq7PCBRAvH98qj6SxOHB0W70IppQr54HC7B6uMamETgN2YgS3C2Ph_3uvxlEWBbepb24kfTDXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی پیکرهای مطهر شهدا برای تشییع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667228" target="_blank">📅 08:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667227">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e3a52336.mp4?token=O65Dqgvi8wh6TQtimZoO5w-6eV95wlAf_2Hx7Xyb5eXpHP0IDvAEeVC9MnlwdDAnxIQIIR57g7j4_3oNgSAoxAz25eTSnnXNvg24AtiHhcU0VOpZZ1QjxrgnDjZ2ZiiTz4X9qIeaZ1ARVj9SM2PS8rzWbTYQfaW2WNfhTImrqIhLkwUk_Tn39eOF44uz8GyMiG_8Vj0cWlRa8hIP1BTaWse7xghiVkjsnmhAMSUlnaKC4bnz-4ppa3OjRTgrHw-nF9ZzHj0XSXBW2I2cbQeebQ8tGM5USBTGbUUuewTOPAhrZOebE-ImsVKGshTZhgk3mNletqPEEkifTVbOJ5Vp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e3a52336.mp4?token=O65Dqgvi8wh6TQtimZoO5w-6eV95wlAf_2Hx7Xyb5eXpHP0IDvAEeVC9MnlwdDAnxIQIIR57g7j4_3oNgSAoxAz25eTSnnXNvg24AtiHhcU0VOpZZ1QjxrgnDjZ2ZiiTz4X9qIeaZ1ARVj9SM2PS8rzWbTYQfaW2WNfhTImrqIhLkwUk_Tn39eOF44uz8GyMiG_8Vj0cWlRa8hIP1BTaWse7xghiVkjsnmhAMSUlnaKC4bnz-4ppa3OjRTgrHw-nF9ZzHj0XSXBW2I2cbQeebQ8tGM5USBTGbUUuewTOPAhrZOebE-ImsVKGshTZhgk3mNletqPEEkifTVbOJ5Vp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور بی‌نظیر مردم در میادین مختلف تهران برای تشییع قائد شهید امت
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/667227" target="_blank">📅 08:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667226">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f466eed7a1.mp4?token=DfDzT61vIHyBlJ_DW1nGOSIdWUWYzuaVUcwtcCSut6z_77XmweciFRjgscy9ezcVsEbuykSshHJiZDc2WXZr-Gz2UqJL-mIHeFDX8IYcvsanRlBH_-FbwMuoS7fQHzftl_yP08yTmPat6ZhRlWaMtSSfGXZAXYzffbg3moM2n_aEqr9BUMOl2fQmvvmdTY5eCcuXAX23LD-M06isAtEh_hsINHcv_rBZ3knOT01WC6B_RFgAsOjucSJ2nqbG_Ejm5rssMCktZ5gX8vKQgy9PpYVx1rmxCyD5DZ7rwjhqp4kRcChGe0aU2fMHHidh--sTEbKNEisHhKZ1xO0turqFvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f466eed7a1.mp4?token=DfDzT61vIHyBlJ_DW1nGOSIdWUWYzuaVUcwtcCSut6z_77XmweciFRjgscy9ezcVsEbuykSshHJiZDc2WXZr-Gz2UqJL-mIHeFDX8IYcvsanRlBH_-FbwMuoS7fQHzftl_yP08yTmPat6ZhRlWaMtSSfGXZAXYzffbg3moM2n_aEqr9BUMOl2fQmvvmdTY5eCcuXAX23LD-M06isAtEh_hsINHcv_rBZ3knOT01WC6B_RFgAsOjucSJ2nqbG_Ejm5rssMCktZ5gX8vKQgy9PpYVx1rmxCyD5DZ7rwjhqp4kRcChGe0aU2fMHHidh--sTEbKNEisHhKZ1xO0turqFvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید: افتخار می‌کنم ایرانی هستم؛ تا آخرین قطره خونم فدای وطنم است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/667226" target="_blank">📅 08:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667225">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe88dcdc5.mp4?token=F4rz2fRwD_R_9Hv31bLnniOpIi2KJ7if3yAvfZiLrLH5abJJs_b9ZIFcT0J1PUbQ9tXdwIK9ryQqi2GL_1r4pPb2S-Fz_v9Ec1e5dDJaprr3GA5OkOfeba-mfP2F1sPxxrwiVjp59Y0xgl10zbh6MryqilMAPKwXgK-RxxvwXbL0Zi5apJQwRM7YcB47B1W6oh9StinOOXGz1w2RKp_hRL8395yfdWKboQetBWNoOuvZYJO1-T89rlGT1SfFp9lBxjYe3Xm7DPQLCnVJDlFLFvefYLSsqyV6xZKOQjPA0JfLEE6Ki-hnwvlkaoGVKaeKWUiZ8QfBJF-GBPej-S_vZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe88dcdc5.mp4?token=F4rz2fRwD_R_9Hv31bLnniOpIi2KJ7if3yAvfZiLrLH5abJJs_b9ZIFcT0J1PUbQ9tXdwIK9ryQqi2GL_1r4pPb2S-Fz_v9Ec1e5dDJaprr3GA5OkOfeba-mfP2F1sPxxrwiVjp59Y0xgl10zbh6MryqilMAPKwXgK-RxxvwXbL0Zi5apJQwRM7YcB47B1W6oh9StinOOXGz1w2RKp_hRL8395yfdWKboQetBWNoOuvZYJO1-T89rlGT1SfFp9lBxjYe3Xm7DPQLCnVJDlFLFvefYLSsqyV6xZKOQjPA0JfLEE6Ki-hnwvlkaoGVKaeKWUiZ8QfBJF-GBPej-S_vZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم انگلیس به مکزیک توسط بلینگام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
2️⃣
🏆
0️⃣
🇲🇽
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667225" target="_blank">📅 07:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667224">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e04aa02d93.mp4?token=glublL1-nFmgPmFau8j44qKbfeKhywknV3UlN3cKmRl-7vyJ2NMwCaatgO_YQ9ujodiUP_ofTUBssgLFmjwod0il9uczlu43u54UTY7hGFxz81QrguBNsDkmrUhaLw1WZJSKdF9hZQ5Dgg38ZXzNcQGigNmEIhkha0Cfe_ZRhim9DekFlpY9IuoT9PualyiKxbLp-ua7iyFGOmW0J-rHC-vtdC3s28-Ru7J1tMTHlZdhIReVUp6G2xE8jdtpBJQn9sI9ZlVkzk4QTlFg-ZFcHwmcFuh8hLVNg_zFeoRzJO9Fhx61mWC5dA5cvVkoVug6KGOkAxn9qOsyYGvcszvp4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e04aa02d93.mp4?token=glublL1-nFmgPmFau8j44qKbfeKhywknV3UlN3cKmRl-7vyJ2NMwCaatgO_YQ9ujodiUP_ofTUBssgLFmjwod0il9uczlu43u54UTY7hGFxz81QrguBNsDkmrUhaLw1WZJSKdF9hZQ5Dgg38ZXzNcQGigNmEIhkha0Cfe_ZRhim9DekFlpY9IuoT9PualyiKxbLp-ua7iyFGOmW0J-rHC-vtdC3s28-Ru7J1tMTHlZdhIReVUp6G2xE8jdtpBJQn9sI9ZlVkzk4QTlFg-ZFcHwmcFuh8hLVNg_zFeoRzJO9Fhx61mWC5dA5cvVkoVug6KGOkAxn9qOsyYGvcszvp4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید: متاسفانه در بسیاری از موارد، علیرغم اینکه باید از رهبری دفاع میکردیم، سکوت کردیم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667224" target="_blank">📅 07:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667223">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رصد لحظه‌به‌لحظه مراسم تشییع پیکر رهبر شهید ایران از سوی رسانه‌های جهان
🔹
رسانه های خبری جهان برای چندمین روز پیاپی در حال پوشش لحظه به لحظه و رصد زنده مراسمات مربوط به وداع با پیکر مطهر رهبر شهید ایران و تشییع پیکر ایشان در تهران هستند. امروز نیز حضور میلیونی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667223" target="_blank">📅 07:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667222">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4928a1c970.mp4?token=fZtRtoi_C-leopBzUumTnucvUqqp69cbjqKcyK0av6YKGK5YeAYcGrFH-H9isQNRG3WYY3gjx3vmi2UCqG3YavrTx4X0YTbea37npyefj_-rFuS3C3OVTVeaMgSamR3b-I7laOaopaz5dwVvy2Oq2cyxMbos7xyeNsHXmzqIrUqcDvVRL-dMRB0vLl5gkbpOleANOxgBhCe1TpK_aKRVvGflvL4F0MjuDgALXK0wclzR-J8Voch2dhZHAAYyCgpOh-D50zmcz58yrbO2pkHXecXuZTwpOP9v6v42sP1odHBjlOfw1AmEvaancpDeUXoMlzw0qLVn5UmJIMM8PWK7fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4928a1c970.mp4?token=fZtRtoi_C-leopBzUumTnucvUqqp69cbjqKcyK0av6YKGK5YeAYcGrFH-H9isQNRG3WYY3gjx3vmi2UCqG3YavrTx4X0YTbea37npyefj_-rFuS3C3OVTVeaMgSamR3b-I7laOaopaz5dwVvy2Oq2cyxMbos7xyeNsHXmzqIrUqcDvVRL-dMRB0vLl5gkbpOleANOxgBhCe1TpK_aKRVvGflvL4F0MjuDgALXK0wclzR-J8Voch2dhZHAAYyCgpOh-D50zmcz58yrbO2pkHXecXuZTwpOP9v6v42sP1odHBjlOfw1AmEvaancpDeUXoMlzw0qLVn5UmJIMM8PWK7fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول انگلیس به مکزیک توسط بلینگام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
1️⃣
🏆
0️⃣
🇲🇽
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667222" target="_blank">📅 07:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667221">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e11f66b5f.mp4?token=rRH14CWVgRBmZ3hgGpTsLAJbc9rq0mbpBA_ScT4jp2FZHcBnJH2CfyLQGeAyrOimnuYd9O5tk31f57T5-d-liBK8B1fNybvimS3IY88iUNj6buXvcLyqd0LzzwQwv1c2ymPu-fpLYtAtAjqLitYDs8tD7r6dZqlSW7Ypacm7V2a4a-hS3iq8oPUTMtJt0Jm5BDs2urCX3QBcWh-ZWSHC5_TdNdiw33Nd8cLMzuf7_arMOQhXVVR3W9SSvf47FC4QFS3mttLEp8BiGKzmJeqsL7KP9HeiJgEfegAvJz_FpWwKf7WUqB3CmdmDk1GoTPXrdt8G9BeGPyYVZCzYBaLRRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e11f66b5f.mp4?token=rRH14CWVgRBmZ3hgGpTsLAJbc9rq0mbpBA_ScT4jp2FZHcBnJH2CfyLQGeAyrOimnuYd9O5tk31f57T5-d-liBK8B1fNybvimS3IY88iUNj6buXvcLyqd0LzzwQwv1c2ymPu-fpLYtAtAjqLitYDs8tD7r6dZqlSW7Ypacm7V2a4a-hS3iq8oPUTMtJt0Jm5BDs2urCX3QBcWh-ZWSHC5_TdNdiw33Nd8cLMzuf7_arMOQhXVVR3W9SSvf47FC4QFS3mttLEp8BiGKzmJeqsL7KP9HeiJgEfegAvJz_FpWwKf7WUqB3CmdmDk1GoTPXrdt8G9BeGPyYVZCzYBaLRRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: مسیر تشییع تغییر نکرده؛ مسیر همچنان از شرق به غرب است
/
ما پیش‌بینی تشییع ۱۰ تا ۱۲ ساعته را داریم
🔹
ما تلاش می‌کنیم از نزدیک‌ترین نقطه مثلا در میدان انقلاب پیکرهای شهدا را در مسیر مردم قرار دهیم.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/667221" target="_blank">📅 07:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667220">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3bfb4c4d.mp4?token=Nwzyt0C-WvVRu8td4XSO1pHXdXNCmVQO3MEXn11kwVKF-fc6WuReIxyIOXnD2G638SD388tlSbcbPXAV_GDYdo3SVy3I2I-fdCadl-7pj32mDEOJVvllR-DnP-a669Ld-AXn_J4r_OU-dzpn1a4BWwUbYCoR2azxtZ8SnzAcGnkQWhlglZWqVtDOob7QHSC6bfA4CoQQcP2Euh3WFdd9xNoFVemETy4AvVxDeJ4dVGTSh6E5cYHXk_7EEwVknLsXB3KzKfpBoWuSSf4IelUO9GZau-XAjz1U3a93B1IVQAAZdX-ykh_S3c2yYlRKZQ0nxbJtfuYISZ6ugFRcx2yc6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3bfb4c4d.mp4?token=Nwzyt0C-WvVRu8td4XSO1pHXdXNCmVQO3MEXn11kwVKF-fc6WuReIxyIOXnD2G638SD388tlSbcbPXAV_GDYdo3SVy3I2I-fdCadl-7pj32mDEOJVvllR-DnP-a669Ld-AXn_J4r_OU-dzpn1a4BWwUbYCoR2azxtZ8SnzAcGnkQWhlglZWqVtDOob7QHSC6bfA4CoQQcP2Euh3WFdd9xNoFVemETy4AvVxDeJ4dVGTSh6E5cYHXk_7EEwVknLsXB3KzKfpBoWuSSf4IelUO9GZau-XAjz1U3a93B1IVQAAZdX-ykh_S3c2yYlRKZQ0nxbJtfuYISZ6ugFRcx2yc6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین تصویر از آماده‌سازی خودروی حامل پیکر مطهر رهبر شهید انقلاب اسلامی و شهدای خانواده ایشان در مراسم تشییع تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/667220" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667219">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24554971f4.mp4?token=IwLqDdegi_bAQ0YRFwfmjIt4ZEV1hBxnwYL02ClXk_17JYEhNCJqsnZwj4gD9FUqu3g4YyG3ImmcrZSKwKqZ8Ki4f8xgGDC6o9cjpScrImBy8BsX2aNDPrKlsiU_VLsa8d1KpnKqGjeP22ZGY0dZjv-PyUGeO234JsI5QEH07pjF7e2nz_TMvTk42abkg8Y-HKKONU9Pf971e3E7s107Pa0S4uAX4v0Wk5dvsFQbPtGAZ9HKkfSSPbr1M2WzmLWnoYeXpDkDKl5pHmgu9vjvAO8cntqZi_yRNN0BbC8BrwQPVgdd3u80laYd9CbzScgDcMqMwz_bC54ot47svgyJtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24554971f4.mp4?token=IwLqDdegi_bAQ0YRFwfmjIt4ZEV1hBxnwYL02ClXk_17JYEhNCJqsnZwj4gD9FUqu3g4YyG3ImmcrZSKwKqZ8Ki4f8xgGDC6o9cjpScrImBy8BsX2aNDPrKlsiU_VLsa8d1KpnKqGjeP22ZGY0dZjv-PyUGeO234JsI5QEH07pjF7e2nz_TMvTk42abkg8Y-HKKONU9Pf971e3E7s107Pa0S4uAX4v0Wk5dvsFQbPtGAZ9HKkfSSPbr1M2WzmLWnoYeXpDkDKl5pHmgu9vjvAO8cntqZi_yRNN0BbC8BrwQPVgdd3u80laYd9CbzScgDcMqMwz_bC54ot47svgyJtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول برزیل به نروژ توسط نیمار دقیقه ۱۰+۹۰
/
بچه‌غول حکم به حذف برزیل داد و نروژ را به یک‌چهارم فرستاد
🇧🇷
1️⃣
🏆
2️⃣
🇳🇴
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667219" target="_blank">📅 07:40 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
