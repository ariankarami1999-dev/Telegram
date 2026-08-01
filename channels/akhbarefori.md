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
<img src="https://cdn4.telesco.pe/file/iBBnj6TmPR_opyBQUkrk1K27OUvrgYHEsBE8EcfElK7up-zrRZrGEORGCE8oT0_UQI_VVqVv4CkOHE7ixwpsxDkOOV7YAcOaumtR4tz2aMLuR486YVaS1uUKidGNZNfPgtvxlhZhYRT779hIMhEeag55ztyoMBN1xmexdjO26p2SfddNYJtTnYC5aMXMrU09AZynoiVbEG-WYGm3tkJnFp7-3qt1iw8J1Hm8rFKsxbFo5jOCTHpI4ZK0DlFtYXVx-wFAFde5Yfc20yrzpRyWgYCHtjZwvc2_hzjZ_NpmH4ljWOzm0SAN3xwv-SAxCxB9OIKsgGY6_owvYgAGjqe02Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 19:05:43</div>
<hr>

<div class="tg-post" id="msg-677389">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ3XoVOSRXsVCYg1g2tA0PJvKlJa665YdXXQroK6I5flj6YA6S_9gICU479M_PXM7e2zaBoWrlxgPfRSWnhxvhi4J42rBE4UK0DgUwJ8CD8L_D_YtuJ5ao1sJJkKdM0IN79k2oj3D3Xd16RWWFsr-xQSTd4d74yepPHoq_pfEmbmB5geAmkE3ZvoaJngNFw5BUhIOILmFWgstHdK55c_imi31KirsLa9ljFmribd_GzUD9ToFDpsLhLAym7umf64aDhTa7Z03hQQk8vm8HGLNRQGjYFFU7IQSCO2C2f1MUS4RCg-EN7GCrmDiwCgUmvl8JopSENGCldWCr_psbojow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام عراقی‌ها برای زائران ایرانی
🔹
آسمانمان برای موشکهایتان و زمین‌مان برای زائرانتان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/677389" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677388">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mw6-37rX4Vu3Pafm0OTE4TqqZd1zsKPfiU4E083URydeWfFePQJDW7nZXvLmv-nFf-oubPi0UmgNSwnfFz6nVq8rP_QN5fNzFnlqZ-NDNfw124bHIHlDy-pOBEoyiivQzgToBS2WdA0HzrMvhozlHMxK0xXX5dxK3zO5yZqcIT-uzoWae3p9DN2mM5kBmfr-x8RTQpRCU6O2MppILfkUzZQw-lthJRlSPdx6GYndhA1sMDLCt9UXaONvkP1W4a9i8gMTaan57MN4DmfIQPRgDDDpsIEfmHeWjUC2BRSqZcXQYBTJWMzJAt7HWh_kySWL5JeBfbnNH0atF5sS11wqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦷
لبخند سفیدتر، اعتمادبه‌نفس بیشتر!
🔥
سرم سفیدکننده دندان LANBENA
✔️
کمک به کاهش لکه‌های ناشی از چای، قهوه و سیگار
✔️
استفاده آسان در منزل
✔️
کمک به تمیزتر و درخشان‌تر دیده شدن دندان‌ها
✅
روش استفاده:
بعد از مسواک، دندان‌ها رو خشک کن؛ ۱–۲ قطره روی گوش‌پاک‌کن/برس بزن و فقط روی سطح دندان بمال (با لثه تماس نداشته باشه).
⏱️
۱۰–۱۵ دقیقه بمونه، بعد با آب ولرم آبکشی کن.
🗓
روزی ۱ بار (ترجیحاً شب‌ها) | دوره ۷ تا ۱۴ روز
برای دندان حساس: یک روز در میان
⚠️
روی دندان آسیب‌دیده یا لثه ملتهب استفاده نشه.
🍵
تا ۱ ساعت بعد، مواد رنگی نخورید.
📦
حجم: ۱۰ میل
💰
فقط ۸۹۸,۰۰۰ تومان
۱,۲۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
📦
پرداخت در محل (در اکثر شهرها)
👇
برای سفارش همین حالا اقدام کنید.
https://memarket24.ir/product/brief/56228/180124/</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/677388" target="_blank">📅 19:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677387">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
فرمانده نیروهای آمریکا در اروپا: ناوشکن‌های ما برای پوشش هم‌زمان اسرائیل و نیازهای دفاعی خودمان کافی نیست
🔹
به گزارش واشنگتن پست، فرمانده نیروهای آمریکا در اروپا، به پنتاگون هشدار داده که دیگر ناوشکن‌های کافی برای محافظت از اسرائیل در برابر حملات موشکی بالستیک ایران، در کنار پاسخ به نیازهای دفاعی خود ایالات متحده، در اختیار ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/677387" target="_blank">📅 19:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677385">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCRsGAcejaUf02BP0RmeMvzfqkPyxqDI3LZ62AEa4jOMiKMvrUsJEtvOTwgvD2v2XyEU-wAHKAK1G9vNCFC7Nce1WGHB8R5t9eCURr-iAsWLznRlvvi3n3FLVvMYrEYmf8jPk35CCA0uF8TvhDX5BlSm6OeGa1a-nwxZQWdHGu7zN5l-iEEQkkvVTxSvHhaACUN1ZplS0PWnCilCvF4dbCjbpLAWsdugiAJ5IXclPzMgqY_Yqd5bil5gfz_HhRELcQ0aKfR25noy_LK9HxXD-KYZcyoPV3hG1Gg245xV9XVR7N-tQYGxyLmheGW0Jfkt9UAEoDVPKSHrl-XJ846_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای سریع مسکن‌های پرمصرف و موارد استفاده آن‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/677385" target="_blank">📅 18:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677384">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7EEhy31dDz2IVtSPrsFmDr1K6sJIFDQ2TzWkBntPikw1Jyv1VRqbD-LhVvmAM6L_QNcKYvoSyMAwePtcK2uW02-1pa6xN0Zjhsu9J54iwFTGbWiE1QodIyls9SU5T0bO46jmYXAAmNQpUXp9hNQBibZGfXxiJFbrgzzlmax2h1w2QTqM_p-PPpO6bravLH5DSgKMHGQ12EZRCzA4DppAB6P5lDIAWL-EQu97HqWVNsR938D-nmxY02KXaTTtN6J44nZ7kKhXkgZ3Z_4flSMElWo2-ZZ1SHM5xwFuFvYIyHq2q0cAkz5tL8xH83IIv8fYqIYqu5kTPVQKYemI8MTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
اینجا مهمان و میزبان معنا ندارد؛ هرکس می‌تواند خادم باشد.
▫️
اگر راهی اربعینی، سهمت را از خدمت بردار؛ حتی اگر فقط جمع‌کردن یک سینی باشد.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/677384" target="_blank">📅 18:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677383">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8ihLOEaWIBsEH4b1RDfXUJ0vVgN29SfTES-oKy2VVfRH8CEJwykhdxpaoc27CZo_CTrDAMrLZN6nVoqKSpQXWoHGio1ehzy1zPLYlqoBZPIxybJYpV4H0wadcEn1c1Chat3cDrfRzKdqXNI7t0Av3Gzj6pJFUzPt-FRdLzmZ0YPBdyCSYkeRsEW_6Op9iORtWMfE80iSWoCIc8coSvMxngvBVkHsvraRx2_-BnVK70l2f68UjRZ6KhfLi-mhx7JNxd_3LtbsTOdp1-066FErbXOC2atYipSoXCsLrr7nu_83JM4CYy3wtt4QY6NjTGwfGwjMfGMCBOwPfrgeU5Kow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: زیرساخت‌های ایران خط قرمز است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/677383" target="_blank">📅 18:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677382">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzUmnOGyoVKtxOqJ-Hy5oZzU6iHy3YeouYSx46wavrPMa_QXf4VSc7zakcB-a8YOJ1AleNhA1tH5WCtNzbMpZISL_jvZBj60L5S5mL8a40BNHfTm4cQ8uhudn1BkNp0LHFreBHRsXN085EnhST9F0dMyz2IRM3HxaYfPnHEGBjR_C6dYJGUEMKhIIshcx28IgYH3XGSdsHjcImVHMk4OaPXBX9JLBF9myvK7N2Vn334rnM-SJmyhXiV_H2aoABk3snRFdozzDnEn1sgNKdULHTohsVs0UqNIh8h2ycCi5HVVKvgVaPhhhNkWK_-UhKPlSj7yJV3R-agax961BYP7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر ماهواره‌ای جدید از خسارات وارده به پالایشگاه جازان عربستان
🔹
تخریب کامل ۳ مخزن نفت و آسیب جدی ۲ مخزن دیگر در اثر حملۀ یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/677382" target="_blank">📅 18:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677381">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای آماده‌باش دیتاسنترها برای قطع اینترنت صحت ندارد
مدیرعامل شرکت آسیاتک:
🔹
اخبار منتشرشده درباره صدور آماده‌باش به دیتاسنترها برای قطع اینترنت صحت ندارد. اگر مشکلی وجود داشته باشد، بهترین راه، استعلام و پیگیری از درگاه‌های رسمی شرکت ارائه‌دهنده سرویس است، نه دامن زدن به شایعات./ سیتنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677381" target="_blank">📅 18:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWo3Gv1X3kicy_tRcgnu0qyzqIfwuTmyrxvrub_kpKQdCNFXmzulYVSisaDssFxdCRxfXwYMiJ4LUWHLQm4RRTpZNJ5b65_182x1MAdw7CXS6n8J2PXZsZoBvuPhGOB2X3PTK5dxGk4E9VVnYoy_4M10FxzNxxxuwM9XzGDBjZ6Emc43vd1jLv2VhoXve_UaHoTrR1OPgXsJvOvA9tyPTX_XOVlsYrvpA1KWolsy3LzfjWULqG7uu5jqAmWLc3nm-5U0qBCOkVX3Z5HHcVzwxSxm_Y2nmGK5nTSZXqhO5grn2n0_bzZhGxU8DTHhtefl39NN33OXrpUzU2RDVHxO6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fehj6OR-5e_MFazo0iwpS4C2CXeR69V4CsWrlkM1SaWh4ZXMawdJqVBFt3nAEH1xU1FCjZkuBKrs4_bucZoNbeiXx3M_A3k_PtiN-1_2QrHcOF7TglKCWr3HdolnN-jS6ohf0-m3qieC50-IKA2GtkP5SmqnIHvMKNBvRTmFJzv0tXEt-Impd0gOElefeF36pt10xEKUEGnuHsURi3GayATSuZPP7I-X0G7xCr_TdP-gzF9pBMEjHHHjyUj3RB1L_abSf20PWNul-nR_oS5rJln-dsHx1ZEA3_vObLivjAiAlZb56pu9Izr5oy7mLiG9ZXQCZ32j9cSUCj9fgXL1wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNyhqr6PvBdQCf1RG87GlJQf13gUUpZ79rr7gBIWC6dr2-ol6Xi7RK7cQhulB8vLYh6JaRzUnzyziRHfB1atEEZ2B6WN5jARlSXb11ZvIqjzD8RN049vSJvElEWIIEdUsBRMZg65V5PaQ4PjzodT12_QItmmSIylzO1_58czhi1k8K0w5VAl3J65QBmecrRtmUP7NwCnnv115XgbgjZTDYbeFUj_P-RAUKRHQdpNTO8mH_ze0Kxr7W7vUNwsKakNoar-2Uen-PlMAVs58rCLE6vwMnKHt-IEF-nblCyXm3wIAx6YcxrA7OglJqzyEQZqq-J6VHnUeBZA1PQRcQ2jxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZShaqfxXKvOisxROipetoZC1wmZQZTx6_5nVbbd_bg23qKUdHfk4hFfPvcaa41wT9W8jpz-wsJ_8uEsyboYAA6fVM_-p8tQ5qEZXQvh-VoMYib9ec4m_19nMYZcmVexZFl31EFq0FEFguEARw_e3UYhBb6GPFMuL48GOAmABunUO5pZ3biHuLdfTIjEKzSIWBxgOJJ90lYmGuhdpw6ki483O8ul40IAUZcULYSMZI-xGCgiCLKJ1GI0lJTyOr9HuIeMM1slkIQfZ0kBF0qtl7EQyjEkALWFbSrDePpMeRAaS0zI4o1Zy3U72txRRzzchi0xizwakUzvpANyp12SYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vM1qHKocrhIUOgiURIqZ6VJmKMy4n3skUmDICJM6Ww4vtAg5kFteOSAK1HArsV-LZElfPz1Oq2gjNeTG28OE5XZxvquYxQXvbef-BwyBt2SlyGh24iANnWctJ9bhI-9AmQP-nlYqb4JORBgspXO5GmN0KZ4hHAcS30pnHBl0E27wBt0MufVmj8prYQa40snM2bT2bI1dU1L9j-_xt33Y2CSebfrlxm4Q16cFfjI0kg3mt1O0min_MY83POXyWH7EfAwkkgvFOj5lh1OvIsQpBG2nYol_Q_f5EoWtxrqjmneG1BKtmBkVFnE2R16TAFOWgaGAQeqDBpzohLWhTAib7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_s2lK7mBHr87iEPIYcksC3CIAN3JQcQOySw9c8pSnMMQrMKxEPXTAz_IwPux_-zeIqaogBx4R0vevShET4OK-aOFUyOK2I4ZKsdlm28n5UQveu_ViKwRs3_By2pdiQ4bQVrL4etnVdvG3np-Ni-5ZrszTXojR3q7Fmnd0PUvw3V4PU4SVmMKXz8n--2GwOzHhWzqjpT584QtY1V9Z1NSpCvq8-DfkQ4Dx06dHcW8AwvdIlwvSYqVoTBOBp0WRcVa5caZrPZ7V7W8qIaVcP-6uC5tNP7rEeDgcHZxSvfLlm8tP5PY1yH-61bZoDW3_GzYIe7zCJN7G64ix5TIKV6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PxLgi0u3eBBy-bT_ENj7MLwP7AeUKNozADgz7Nr-OcMe4gh2uSekYg0r8cxu6OVdSV1_216M3x5oqOujAKvpV27ee1Wn3pBFPd7fTnBg2qn3sC01JoD_vr9s3B3nE3GIaBGmpIi52gRBoHj17JwqOrfHhDfJa6bZRNntRmpcgS5gNtkY--Muv1uUdYwq9u90EQJ0TSqMQHXqofrSj8-NPCqcr9RzFWvTxw37dZhzKXnGX7m43GmABWQPDD6xJsoEIXxiUSl3CdgXRm3Wbr1hnSWBcGgbKZJHQn6cdMLsnh4_pPQqFFFDCt7Q43-QcDF4hC8aho7W1SgrIaE3kYPa1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدافع سابق پرسپولیس راهی کربلا شد/ محمد انصاری و جمعی از چهره‌های ورزشی کشور در قالب کاروانی راهی زیارت کربلا شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677374" target="_blank">📅 18:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677373">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
مقام اسرائیلی: از هیچ تصمیمی برای از سرگیری عملیات علیه ایران اطلاع نداریم
🔹
شبکه CBS News به نقل از یک مقام اسرائیلی گزارش داد که تل‌آویو از هیچ تصمیمی برای ازسرگیری عملیات نظامی علیه ایران اطلاعی ندارد و همچنین از اسرائیل خواسته نشده است که به هیچ اقدام نظامی علیه ایران بپیوندد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677373" target="_blank">📅 18:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677372">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: گسترش حملات سایبری به سامانه‌های آب آمریکا
نیویورک‌تایمز به نقل از مقام‌های آمریکایی:
🔹
دامنه حملات سایبری که سامانه‌های آب در ایالات متحده را هدف قرار داده، دست‌کم به هفت ایالت گسترش یافته و احتمال دارد شمار بیشتری از ایالت‌ها را نیز دربر گرفته باشد.
🔹
هنوز مسئولیت ایران در این حمله به‌طور قطعی تأیید نشده و تحقیقات همچنان در مراحل اولیه قرار دارد. ایران از زمان آغاز جنگ آمریکا و اسرائیل علیه خود، حملات سایبری‌اش را تشدید کرده است./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/677372" target="_blank">📅 18:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677371">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
گوشت بوفالو وارد سفره مردم ایران شد
منصور پوریان، رئیس شورای تامین دام کشور در
#گفتگو
با خبرفوری:
🔹
در بعضی فروشگاه‌ها گوشت بوفالو به‌ صورت علنی به‌فروش می‌رسد. واردات و مصرف گوشت بوفالو از نظر شرعی هیچگونه مشکلی ندارد ولی آنچه در جامعه مشاهده می‌شود مخالفت مردم است.
🔹
در ایام جنگ با وجود شرایط سختی که وجود داشت ۱۲ هزار تن گوشت از مبدأ‌های مختلف وارد کشور شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/677371" target="_blank">📅 18:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677369">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f170b4a0d.mp4?token=vWw4y_-TWGgWjVjKQd6jp1QpAg7c61IyXg8ZYSs9YDnSIpOb8zC933o-xdGAIR5Cbn5ff6QXAfM9rzPX9rLd6JE3mO6HiBCIuiR-EHoHZdG2J717eLvWbGZzFt1XN2GQhLdGdNfr8r0C2MSruCbj3ItZ_RdEO6pBWbRa23-G7uSPTQy1X841X456PjcL4hmjdfLSgJ288_rc2stwBP-Y8BZxIr_rUY4ODKNbXkDR_4Z0eJeYH67UR6JUJjn_pBgZOK7d214Twcwp2Cigd_RToaDyzwoMzrYqrP8Ff3xH-mVXDCGCuSfXX0xqBwR_z8i0uRrHbkuPvyxp3OyXDK-UGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f170b4a0d.mp4?token=vWw4y_-TWGgWjVjKQd6jp1QpAg7c61IyXg8ZYSs9YDnSIpOb8zC933o-xdGAIR5Cbn5ff6QXAfM9rzPX9rLd6JE3mO6HiBCIuiR-EHoHZdG2J717eLvWbGZzFt1XN2GQhLdGdNfr8r0C2MSruCbj3ItZ_RdEO6pBWbRa23-G7uSPTQy1X841X456PjcL4hmjdfLSgJ288_rc2stwBP-Y8BZxIr_rUY4ODKNbXkDR_4Z0eJeYH67UR6JUJjn_pBgZOK7d214Twcwp2Cigd_RToaDyzwoMzrYqrP8Ff3xH-mVXDCGCuSfXX0xqBwR_z8i0uRrHbkuPvyxp3OyXDK-UGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات پهپادی به مواضع تروریست‌های ضد ایرانی در عراق
🔹
منابع خبری گزارش دادند در این حملات، مواضع تروریست‌ها در سلیمانیه عراق، در هم کوبیده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/677369" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677368">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVn8TkkgK-btpvjt5AV_MwPJ4rf8UmN2OSWR26yrivkFWR62GpZvX_N-u3o7SUQbpantK0AP9hS15XJ20EDNKIV0nWXasNa7pY2nVkcgVDvA4wWnlzJt6prqnXVUALUsgwfOi6MnT03a6BFeawqtXPow4SNIHzK56s25z6iA1SyyZ5TKqa1F4VDVGzbGUfcvprgcMtGq4yRZeHbrRPxFVDaIOKUiWANbNRP3uclqq5-zWKE7hAdnAbXDf17EyVGv2_Wqukfm9q4HDPMaAoZdEM5wnKcEDI5zPJTY__TYMIyVy-CC93sX-tPXOOduZ4s89xNgZNYpddgRSsjWMTTpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
یک خرید حضوری، با یک امتیاز ویژه
با عضویت در رسانه‌های فروشگاه قرار و خرید حضوری، از
۱۰٪ تخفیف ویژه
بهره‌مند شوید.
کافی‌ست رسانه‌های ما را دنبال کنید و هنگام خرید، عضویت خود را به همکاران فروشگاه نشان دهید.
📍
مشهد مقدس، بلوار شاهد، چهارراه ورزش، برج ایلما، طبقه همکف، واحد G26
منتظرتان هستیم در فروشگاه حضوری قرار
📞
ارتباط با مجموعه :
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/677368" target="_blank">📅 18:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677367">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
کشورهایی که سفارت آمریکا به شهروندان آمریکایی برای خروج از آن‌ها هشدار داده
🇧🇭
بحرین
🇪🇬
مصر
🇮🇶
عراق
🇮🇱
اسرائیل
🇯🇴
اردن
🇰🇼
کویت
🇱🇧
لبنان
🇴🇲
عمان
🇶🇦
قطر
🇸🇦
عربستان سعودی
🇦🇪
امارات متحده عربی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/677367" target="_blank">📅 18:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677366">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
گاردین: جنگ آمریکا علیه ایران از کنترل خارج شد
ادعای گاردین:
🔹
طی هفته گذشته، این درگیری در سراسر خاورمیانه گسترش یافته و حملات و ضدحملات در حداقل پنج کشور دیگر رخ داده است.
🔹
ترامپ به جای یک جنگ سریع که به دنبال سرنگونی حکومت ایران بود، یک درگیری منطقه‌ای را آغاز کرده است که خطر اختلال شدید در تأمین انرژی و قیمت‌ها و ایجاد رکود جهانی را به همراه دارد.
🔹
این درگیری همچنین به حملاتی در عربستان، عراق، یمن، اردن و مصر گسترش یافت. نشانه کمی وجود دارد که مذاکرات صلح بین آمریکا و ایران پیشرفت زیادی داشته باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/677366" target="_blank">📅 18:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677365">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfb62ea7a.mp4?token=hzSOkUKnKhkrm2hNcWSr52IqoM2avxd3WuROzMIhRiVQnB2vGEv8-kWQ83nzKPsUm4sJZK2hTTVtT_Fr3ltySJI49qITn7SOthzraR6dbAbxhF_N5q0cLBQMEXcdWBTGpHanINLqfbukg-t0q5S9CE5Ztw7wKOkrSd6tMt1fe0BMEqIw9BEv-_zC-SNuNv8w4qmFF6goJf9FrDwdXczo_LbELjwp8x5oW_F6x4eO4dmIaWOT89BEO3laS4gsaDP_x_VZviPaW17eVWR2aW30evpvZhrVdOUs_EI4DZuPWaqxacrkom1TMNkXEj-mYENJW0K6gKG04d6tYsQrFl13yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfb62ea7a.mp4?token=hzSOkUKnKhkrm2hNcWSr52IqoM2avxd3WuROzMIhRiVQnB2vGEv8-kWQ83nzKPsUm4sJZK2hTTVtT_Fr3ltySJI49qITn7SOthzraR6dbAbxhF_N5q0cLBQMEXcdWBTGpHanINLqfbukg-t0q5S9CE5Ztw7wKOkrSd6tMt1fe0BMEqIw9BEv-_zC-SNuNv8w4qmFF6goJf9FrDwdXczo_LbELjwp8x5oW_F6x4eO4dmIaWOT89BEO3laS4gsaDP_x_VZviPaW17eVWR2aW30evpvZhrVdOUs_EI4DZuPWaqxacrkom1TMNkXEj-mYENJW0K6gKG04d6tYsQrFl13yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکسی‌های خودران زوکس آمازون وارد مرحله جدید شدند
🔹
این خودروها بدون فرمان، پدال و راننده طراحی شده‌اند و کابینی با چیدمانی متفاوت و روبه‌روی هم دارند. انتشار ویدئوی این تاکسی‌ها، واکنش‌ها و شوخی‌های کاربران در شبکه‌های اجتماعی را نیز به همراه داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/677365" target="_blank">📅 18:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677364">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0-b4-j_4sU6sRo2HKoDdfl2FUCxzwNGb3PTSWvIllKgqv3HlJLInCnXA2hg0Xo6JOo_Wvt-H1pUdICyoOFRYgtkZc7oR9RIGhviBdHH2DjMAvhC3uIo6OyNvcOpQRV4OzxuL6ZRfXBGbJQTsmajny5Nieapzrvu5W6suYXOFGChpM_PpoVoEEh5qdGR1wF3NBT8M5w4WZuFuaVTC5hK14hR37y0NPgqvEl57SlPYsELgP2YIlpRDs3FsabUxxzcz8wWbscDQkguhzu2e-KIcfsH51hLxh8dVJTFQfuTA0TWjDFfKWmnCYQCpSNrao3M8GgKM_tZh4Sq53DKESzqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشترین سد را دارند؟
🔹
چین با بیش از ۲۴ هزار سد در رتبه نخست جهان قرار دارد و پس از آن آمریکا، هند، ژاپن و ترکیه بیشترین تعداد سد را در اختیار دارند.
🔹
ایران با ۶۰۴ سد در رتبه ۱۴ جهان ایستاده و بالاتر از کشورهایی مانند بریتانیا، آلمان، روسیه و عربستان قرار دارد.
🔹
این شاخص تنها تعداد سدهای بزرگ ثبت‌شده را نشان می‌دهد و شامل سدهای کوچک و سازه‌های محلی ذخیره آب نمی‌شود.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/677364" target="_blank">📅 18:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677363">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سایپا قیمت پراید وانت را بالا برد
🔹
سایپا قیمت کارخانه‌ای وانت ۱۵۱ ارتقایافته را افزایش داد. قیمت پایۀ این خودرو بسته به تیپ، به حدود ۷۶۳ تا ۷۷۵ میلیون تومان رسیده است. این قیمت‌ها نهایی نیست و هزینه‌هایی مانند مالیات و بیمه به آن اضافه می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/677363" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677362">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef2693901.mp4?token=m-VhHZLmtL7kh3kvS6CCJswPciTL9WymUeTTvh9P_cTYxTmYTuphUHijdzhyvkRO-5_PQdZKdYLrk6K-KqfsrZCJFyisk1R5PARSL41Go5D59YrHfyi04vwzRXwGYvXnFca59lp6S8F--HxhQIO2Q74KwsN05eu9JFZQ6fRL4NBqVW6kBKECXg-MQTUcyXawfwF9nK4niXU8vnt40rf6V496xTwpUZFAqL2z-K-di43axcfaId03WwXm_By8qOutXSrEDc88l1nkid-EuqIe2QFKWH6ZvYRS2_qt8PPCPQYAJzXhON_50FewFxJUTMqgjSMadP3EkUiLJuX-My1OBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef2693901.mp4?token=m-VhHZLmtL7kh3kvS6CCJswPciTL9WymUeTTvh9P_cTYxTmYTuphUHijdzhyvkRO-5_PQdZKdYLrk6K-KqfsrZCJFyisk1R5PARSL41Go5D59YrHfyi04vwzRXwGYvXnFca59lp6S8F--HxhQIO2Q74KwsN05eu9JFZQ6fRL4NBqVW6kBKECXg-MQTUcyXawfwF9nK4niXU8vnt40rf6V496xTwpUZFAqL2z-K-di43axcfaId03WwXm_By8qOutXSrEDc88l1nkid-EuqIe2QFKWH6ZvYRS2_qt8PPCPQYAJzXhON_50FewFxJUTMqgjSMadP3EkUiLJuX-My1OBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
اذعان رئیس کمیسیون امنیت و سیاست خارجی کِنست رژیم صهیونیستی به نفوذ ایران در قلب سرزمین‌های اشغالی؛ «واقعا نگران‌کننده است»
🔹
ایران هم‌اکنون در حال اداره کردن جبهه کرانه باختری است؛ ایران در کرانه‌ باختری به طور آشکارا فعالیت می‌کند و این کار را به شکلی دوگانه انجام می‌دهد؛ هم از طریق سازمان‌دهی و هدایت عملیات‌ها و هم از طریق جنگ روانی و تبلیغاتی خود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/677362" target="_blank">📅 18:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677361">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKXmX7eG4e-r68IQqssh4B_Z2AisCyGBIQgV5noWqLkSnQW18kWuBxMCSdZutHFmRy6TxK5Io8LCGrMIzMnxIkyLsTzqzykEoGvCx4RhmHgfyk5x9EbRqMQUn-DJwevdo2L-31b6h5AKy34411WKiiOo-f9vjZigGnOanlMR5uYZZRYpxZqYA7fzxW50KaULKI_7piHcoqqrVtxGjB4ChCT1Ue49893lBGUjKMJvBOSF6jBYFv-rw8_uSNH_S4AAqoAWaFIRSe808Y5CMyrfMuQdqqarkS15upDL-RckYbbAjbwXwpsRDh-u-ybWTRuwLHCxzjXtItPDfXySHEjosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه نمایندگی کشورمان در آلماتی قزاقستان به نیروهای تروریستی آمریکا در پی به شهادت رساندن کودک ۲ ساله در قشم:
وزن بمب: ۲۰۰۰ پوند؛ وزن هدف: ۱۲ کیلوگرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/677361" target="_blank">📅 18:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677360">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان: امروز هماهنگی میان سران قوا در سطحی بی‌سابقه قرار دارد
🔹
ژنرال آمریکایی: نیروی کافی برای محافظت از اسرائیل در برابر موشک‌های ایران نداریم
🔹
انفجار معدن در دلیجان، ۲ کارگر را به کام مرگ کشاند
🔹
سفیر ایران در عراق: توصیه رهبر شهید به مسئولین عراق این بود که استقلال کشور را حفظ کنند
🔹
غرق شدن کشتی غیرنظامی روس‌اتم در دریای سیاه؛ مسکو اوکراین را به دزدی دریایی متهم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/677360" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677359">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d96dcf8b7.mp4?token=lSKKXjkEb0_IU7UZsph9TaVv1zyfDrPaJHFeGNP3gjnGO0gPctgDNRJVjNn_9ZOdBhPG4oW77XIVNW4P370R_DcvrBOOxr2y8uteQzwI6aEO7EsSiSZCdIleDrkkPHB-xYoRDPVTOiZcsSYqXaSFQKQViWQBNo1DPIorsiqnhXudDASr_LCy-raCvO0i575bhqYaWQZ3QEXkUvYoj-hoQAhUFz6jX27xGcxTCxt5ihEoQYUodq1-B2273T4yJYrm_80uDhTGNnJjAOs5iHkx2Wlgg5LCA68y69PEAeJwgYPdv1OBDKGGtEEy-azggHQ38dDcmmFiKWC0M0fhnQh4Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d96dcf8b7.mp4?token=lSKKXjkEb0_IU7UZsph9TaVv1zyfDrPaJHFeGNP3gjnGO0gPctgDNRJVjNn_9ZOdBhPG4oW77XIVNW4P370R_DcvrBOOxr2y8uteQzwI6aEO7EsSiSZCdIleDrkkPHB-xYoRDPVTOiZcsSYqXaSFQKQViWQBNo1DPIorsiqnhXudDASr_LCy-raCvO0i575bhqYaWQZ3QEXkUvYoj-hoQAhUFz6jX27xGcxTCxt5ihEoQYUodq1-B2273T4yJYrm_80uDhTGNnJjAOs5iHkx2Wlgg5LCA68y69PEAeJwgYPdv1OBDKGGtEEy-azggHQ38dDcmmFiKWC0M0fhnQh4Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
🔰
خاطره شنیدنی از سخاوت شهید ۲۲ ساله
🔸
پدر شهید «علیرضا الوندی» از شهدای جنگ رمضان، درباره منش شهید و اهتمام او به سنت قرض‌الحسنه اظهار داشت: پس از شهادت، بارها به من مراجعه کردند و گفتند ایشان [علیرضا] به ما پولی را به‌صورت قرض‌الحسنه داده و مشکل ما حل شده است و این حکمتی است بین بانک قرض‌الحسنه و شهیدی که با وجود سن کم کارش قرض‌الحسنه بود.
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/677359" target="_blank">📅 18:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677358">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4Ur7ZPvcXKl84Uk4H95JLg3SCsscrUMEMHneUf10Pwb-6gbRB5EgVXdt-ZR136Az2-XNRmVp50Izni8tB0SzYcmdk5qqayZcK4tzR4uUBcPBUA9bqTi6uBGK1GS4t7m5GYf2NhIGjd9YPZl1vck7kqrgKW6fe-w_ajdD9WXruZjN2_si8bOAheXkx6tT-hOrPRRwfldLpj9U67W7aQwEFRe9F3rSqggcg6114ZfpWj2ftVZOcjeF0QrKEbvKoXtE7awuzF1XSMiI9LyQBtjQeEGtMipa33u60my2S-xO4QMM-uyWuoQ-9702bG9neO-DJgiylzc842-dEUku4TIdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب تصویر پرچم فلسطین بر روی پیکر شهید هنیه در عینک رهبر شهید انقلاب، هنگام اقامه نماز بر پیکر این مجاهد فلسطینی
؛ ۱۴۰۳/۵/۱۱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/677358" target="_blank">📅 18:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677357">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/677357" target="_blank">📅 18:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677356">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/677356" target="_blank">📅 18:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677355">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1rkly8MMxJB1ujKqu3NyDwXfpYFyHH326sTddWPl-zG0OkB5Nbcz0gSdYjlFgi61T1pV-vK__TzUL99iFFF_RMw5El9o4gbYsss0Q7Uc3MhEshPIEb1Ugbuej2GQ3Xc8aR7MMPGsrvWB-WGIDmQXuBSuvLY9vpyE5KYw3bE1--RxiEhpBJGO68ig0cgnvzXV0sQGuiKYFwAGbbAaxo8dxo1d9HgCwQcKs2325yTFqIKKpJwHmt3hKeVOm7QCQk5SvbzM7KexoNhBcA_czBRAS2eKR6Qsb2w-vZibXce97a9jRWGVjt9CWL6PoGpWbJAHZoknzmkEepEj41i65hWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای هیل: جنگ ایران، دزدان دریایی را فعال کرد
هیل:
🔹
جنگ ایران، خطرناک‌ترین خط کشتیرانی جهان را دوباره باز کرده است. این جنگ نه تنها تنگه هرمز را به لرزه درآورده، بلکه به دریای سرخ رسیده و دری را که واشنگتن فکر می‌کرد به روی دزدان دریایی سومالی بسته را باز کرده است.
🔹
در آوریل و مه امسال، دزدان دریایی در کمتر از دو هفته چهار کشتی را در سواحل سومالی ربودند. جنگ ایران، ظهور مجدد دزدی دریایی را اختراع نکرد، اما به آن سخت‌افزار، آموزش و پوشش استراتژیک داد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/677355" target="_blank">📅 18:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677354">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxXWfkJlxO-N_3CdfGaERyo_9lpXfCpVVAVxo-Qb1iMAoKrb6MFSNqWk6BhOxSLdmTmvtY9j4X__oaCwVkhjv03dTRujkZpW-6SyflmJdObiCjlKIKPan63IgpZw-b7AegcaXHNQWeLXByeB3M0JAGDnTjY1v0EEShw22BBFk1i3WDj2d4_k_eoozEFvG9YB_miWGOd_pUKaq1orFhtIu8FYG3C5UT19IFwFej1lNeUE1U9iW5KnlTtGUIRvsX2TvM4QvO8Rnye5NaNqz-YbWxykXhQSM34w_XGm-lovRJiEfrHP4YAHcjRfLUfSApyY-SHFS6GLIFgCwLeFuKiNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میر داماد؛ فیلسوفی که اصفهان را به پایتخت اندیشه تبدیل کرد
🔹
میر داماد یکی از ستون‌های مکتب فلسفی اصفهان بود؛ استادی که شاگردانی مثل ملاصدرا رو تربیت کرد و نقش مهمی در شکل گرفتن اندیشه فلسفی ایران داشت.
🔹
نام میر داماد در شمار ماندگارترین اندیشمندان تاریخ…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/677354" target="_blank">📅 18:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677353">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
وزارت امور خارجه آمریکا: آمریکایی‌ها در خاورمیانه باید محتاط باشند و برای بسته شدن احتمالی حریم هوایی و اختلالات سفر آماده باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/677353" target="_blank">📅 18:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677352">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKMC</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbJonq867LGgq4ZRFr_DpcLivOJbP78l0LhfAmhoysfgDVNP0gHBZYz0DMI3qIosfmeYHkf1S0Wnfy55fYKimoD4oCVdqucHKGZn6ev3wAsfrpsC4OB57n_VREJPl3Xg1AGuZbbTuJfYp0QYTmOKt6eE4XgZYApNwEQsO_yDqFmfIru5vIGIHC7_Ajd1HWv_HHw5e69S84seAkDM-C2qt5ke2HW08YCwWV-PdfUo0dBNe47LAcf2uLOwpgoYBEa2PhJO4VyyOlKW2YC4WHeA9w8ngrk2vhzqrf6GvcTfPKs9cj3FpggT8YBnHL_o9-J9r5MfhwtcTWawuIipQB8KMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از تهران تا مهران، در مسیر ایران
کرمان‌موتور با استقرار پایگاه‌های امدادی در مسیرهای منتهی به مرزهای غربی کشور، در طول مسیر اربعین همراه مسافرین خواهد بود.
پشتیبانی فنی شبانه روزی از ۶ الی ۱۴ مرداد
▫️
02142724
▫️
KMC App
#امداد_کرمان_موتور</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/677352" target="_blank">📅 18:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677351">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYgkC4fJLUpIu94FLoiPpOjyk7feyZsH4jMcRo-d5ErrT9nyvqsIGAWODKowC1IzFS5yjm4O-g23ktSg7BsagBsjSjaO7DTbznRHeLQvPyPcJdvvNmNeId76eNTCRgu5mn8RQ_tHo65C1xx60gKmWRKrOuT_c5pKRJ1V2cscbwf1k4Md3-xUw1gmqYblW2Aw2QWCiGl5Z9w6RyAD-h1-hVYy-4Es-1BGZ6AnYwoMUw_NyUmn-bOcrm9lySuhu3Pj8LRA8mYCkClOQWLq_jaMzXRC-R-bYHH7-6KvfMCqFMrSEZS4N0QPD0Ok6_G9c5PulEuGTNOm4y9j83wfAaxHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادمان شهدای مدرسۀ میناب در شارع‌الرسول نجف اشرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/677351" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677350">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mw671sfdRXruWsbupx2sqLlj-bYqsSNXXVuSAx6Kb9pUM4SvpGaGLgfZi4k3criYccfsMHXNRqBbqBbkMl1rJ4Kvm0CGcgqqMDJyObTGs5T9SwZShEHxAlOkP_7BLuIkEiarNNczHdip4uJEwQCL-7t3JxsLeOC9QbYkdbNvcBZ_t6ulKvvlC6nmXzchusN1a459Hdo82CKqSRuSDfcRMvNZD-UArw_RIsGqF8blA21LDz9CwNkGAn1z5G_-dq0AFBVVNcF4KESyX7OfrzgpdnVxNg9_IivwUNnGq5reb9AshEmVeGWJVtKdDEGnGZinoldtN6QlrwmITsSSYs-PXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادداشت جنجالی وزیر آمریکایی در خلال برگزاری جلسه امنیتی با ترامپ
🔹
یادداشتی معنادار از وزیر خزانه‌داری آمریکا اسکات بسنت برای خرید چندین میلیارد دلار ین ژاپن، آن هم درست در خلال جلسه با رئیس‌جمهور آمریکا در کمپ دیوید، توجه رسانه‌ها را به خود جلب کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/677350" target="_blank">📅 17:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677349">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvQPnPqQGbSvBNzWYEH07lqYnM15WIWcBit1R4HL3-d-KP8ulwFoOQXkVGMor7ELgeAdeeSTau4XbviiNoYQDL9rbc7ia2B0NXFEDAoDsjo8-Jajo-4huHPYFWWBxBMgjnPeIk3ElPXuj3tSL3lsKzHt8GX3nGJdQFMkMdYuMBVll51xdeMps7d-JEQX3G3Ne0BptjcQvAHAcQSUTu0iULOT5IE8Sk4tYFEXJjlqWVc4RDJKTuVXdGuWAonnj3R5Orpitprj-EM6GYmy2TVoOIjTaj4c1yFOweeUFbcx073Bs0036mAre46QErXvlPdJTdlQj4gE6jSxmNSICnFR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از مظفرالدین شاه و کمان نادرشاه
🔹
ماسیکو معتکف‌الملک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/677349" target="_blank">📅 17:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677348">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFVMlQaArNngJNvqqH5UkTywBBTU5Kt_858ed9WSu4rBEfq46qbqkZO83p18gLayi3oVlXPN69HL4gVTC4FjPU4AdKnHX64a8dSkw5A55epfRHMtyLvQyO2uZCmP8_4DJ1fobXzkhE-MVQI05eGRwKzFZ2rlU8VpvFb5tZt3lNvsy-Rq_p5b3SuXBjKz6q8k51PDvdX2fWaOT_1pF5egiiIfEPfq9_W-c6w0w7iB1B7fU50dcfdymdEN46fYj64I4L_poX7VK3uAk23d-6SK0uYFgoCBMN-e927G-gkdWOQQdzWyAj9egQiR2aHZUxC1c4TtSMAqErs1EIXOSJfybA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ شغلی که هوش مصنوعی نمی‌تواند آن‌ها را از بین ببرد
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/677348" target="_blank">📅 17:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677347">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUmSNvyWYVStRNRTnLlx1GwJPdlGScOFWnN-M3SvS1wlEOkl4BCrdTK23a6rVxJjTsX-z4PHWRFYGsoOxjiFcYTextJR9zdrtPPV3lriUjfni71Txv4KT92XzmfBgGDmEcK7nbc453-y6OXM3Uh5pYmnEk3_eBF9ncFPtNnWS4qxQJOF-3AdsWAwW_ZxeXMuFFnYZ5BjtW1zWm4XeFHxPB2oAFv8nNH07sLf7nTFiSVI_8Ubn8wqeVPEYHU_GKMvlzy6GDtFJ-SB_H-TcR14XkEtD-XKammkMYhCusJ9gGR65YpBQDeDUFOVUs4-BdJD83jR2Fzaj9NyEEGDPU1dyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تداوم اقدامات حمایتی بانک صادرات ایران همزمان با پایداری سامانه‌ها/ جریمه اقساط تسهیلات در دوره اختلال حذف شد
🔹
بانک صادرات ایران با هدف جلب رضایت مشتریان تسهیلاتی و دارندگان کارت‌های اعتباری، جریمه تاخیر در پرداخت اقساط مربوط به دوره ناپایداری سامانه‌ها را حذف کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/677347" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677346">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo3AN_LHZrAFb_peuMn1MuZrQqSuQwZSQ9w23iyVjFOprawK5ZkDahNDtHsYxP6v0RHJZ8y41dQIFmRhdCnCd-AocAdNwRihvHPRBs9L4aXkabaup4pR8O6wTB5zSFK-ZaC5PlBNEqmkwp4dyKvhZx37FKtEP9AqojJyLjbw0lB-grqm33uUle63FVtCcuS6lHquzpu3VcNEP967v_G9-O6Qw53f0rff1jbFEH7ukBt1ConNxguoBeQL_x7IogB0dAROe0oTTy7GbTIhrdyLhaRRqMt72HRLY5l4LAHXZjr4WTxnOPBr5K5yIgLQzQydFLcsYm2jJ7DHarYO01_9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
خادمی فقط در موکب نیست…
▫️
گاهی جمع کردن یک لیوان، مرتب کردن یک جای استراحت یا حفظ پاکیزگی مسیر، خودش یک قدم در راه خدمت به زائران است.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677346" target="_blank">📅 17:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677345">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت دفاع: صنعت دفاعی باید سریع‌تر از میدان نبرد پیش برود، با کمترین هزینه بیشترین قدرت رزمی بسازد.
🔹
ترکیه و عراق برای ترانزیت ۷۵۰ هزار بشکه نفت روزانه توافق کردند.
🔹
نخست‌وزیر انگلیس: فاجعه انسانی در فلسطین توجیه‌ناپذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/677345" target="_blank">📅 17:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677344">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnWYGr_c0fcDf1W6hsNYf8DtBPYRe9tZuZyjbQj5WW9MKoEUatlNMNQQYQKGTXBohhmwWX1gts74wrlEWVj9LvUpwB3b3zph_1LOmKom6Mxre4GyPskFJq--P3jscOEJpdKczyz76X9iGDKSyAaV-PdUSF4i6Oqq_l1AqjSURHQiNeqeevlX0rT-_cARtZ8S_mzEntlHlEYL2tMvFHIWfxYRhERwFX07rVDep-KnLxOipy1c9ngSKO5jB9zfd3GTlHQMCRYQnHH4AaSed1e-osDmlt7hNCsVSdgtPeSZAKol_fRxhAZo_yMIF12nN2sdqrYyuPZQd5GDXaooTKDC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل گاردین، رویترز و الجزیره از برگ برنده یمن در جنگ با آمریکا و رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/677344" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677342">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
بلومبرگ: کشتی حامل گاز قطر هنگام عبور از تنگه هرمز مورد اصابت قرار گرفت
🔹
بلومبرگ با استناد به گزارش شرکت‌های اطلاعات ردیابی کشتی‌ها گزارش داد که یک کشتی حامل گاز طبیعی مایع قطر هنگام عبور از تنگه هرمز مورد اصابت یک «پرتابه» قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/677342" target="_blank">📅 17:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677341">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fckrNOJEbi3xveX058ILG-AQhYvOLfJYWD-Y765mPXVTgIZ8-MtwZ50MYAPTgx3Um3KWqvGzAR1ozAzcuKM6ZsqlO9AxE82bPDssyemYWptL2IAkOclcLKG6FpgTngF3HjxhqfqJwv-izKCTLrWFhtO8-qKGB1ciVbi5o6VJSvVhcg0Eo2S13ysGSmTcAO5e0EmekZpsJmOlqqFGuR7N6xWGcqTIeW5oubeKvr6hhX7uMss_j5eG_I8icLckCgjcO2QlDIHEISvbz9VfqSjdeKUiqHIYHgJ7KvviNduTIMlSp4JOEPbM4GqKBpYUYugjj36FVBbmQi9MzbCOWaeZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت‌های آمریکا در مصر، کویت و امارت درباره «وضعیت پیچیده خاورمیانه» هشدار دادند
🔹
در ادامه هشدارهای واشنگتن به اتباع آمریکایی، سفارتخانه‌های این کشور در مصر، کویت و امارات نسبت به تشدید احتمالی تنش‌ها در منطقه غرب آسیا هشدار دادند و از اتباع آمریکایی خواست…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/677341" target="_blank">📅 17:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
توصیه عضو کمیسیون امنیت ملی به عمان
بهنام سعیدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
مذاکرات ایران با عمان صرفاً درباره تنگه هرمز است و هیچ مذاکره‌ای با آمریکا انجام نمی‌شود. تنها ایران درباره مسیر عبور شناورها در تنگه هرمز تصمیم‌گیری می‌کند و هرگونه مسیر موردنظر آمریکا برای حضور در این آبراه از نظر ایران مردود است.
🔹
اگر عمان بخواهد بر مسیری غیر از مسیر مورد تأیید جمهوری اسلامی ایران اصرار کند، قطعاً متضرر خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/677340" target="_blank">📅 16:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
کانال ۱۲ عبری به نقل از یک مسئول ارشد آمریکایی: ایران در حملات اخیر به پایگاه آمریکا در اردن و کشتی‌ها در تنگه هرمز، علیرغم تهدید ترامپ، بسیار تهاجمی عمل کرد و آمریکا را شگفت‌زده نمود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/677339" target="_blank">📅 16:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNNLEjMh3XT5BeulrobbCU5AcWMH9THUN5U5-TDUtgZtryBXxvEa1hSX80P0BhFaMYVNiGokpmHg2UdcjxsfwWeXYzMWhpQ1CU7Ki1n6wfavA1-tjQLbag7g-p71IGZepN_WvcghrlpWdU4lah0P9fItl-QcKlqcnW84gSacrbuCBV1guGViI9gABjyNBuwubZZdROm4LXWYSgX9NJEzDN9DI7AtXJtUvSVinn1T5diTn3HBcEXJ_GnlhoIHVETq6wW0bWyFyHT9qCZntbbd_rldgOz4AqIHyy71m_A0ZOylEuRzbV5ccvo8WXKVCvuCsd_5COqewD4CezQQja90nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: آینده ایران را مردم ایران رقم خواهند زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/677338" target="_blank">📅 16:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwJuixGkBaAVzZ-oie3jc5ZHeQaKLlEze2JPPZrS6aBTm5NL8pYsHPw1ZKg_IKWiw7umGy5kPlAw-PjvaxRBaR6UTN2JF5ktFMTwHtttxfqGaS5hGSWRDPbvZD8XK_y1V2uIhmkdu3cVxZN7paREOBsPLhn4tGNwsl77WfoczXj6riBYRKTYAB2DqSWGviYc6zc56SaFLK_Vc39-T7n8VIxX__CAR0RjA9w4o6-HgyNuR7RPiYGUdILDsmUqNO8eqTSgfDUsnrlhHTfCEMX2EQ-8PvLnRvagM_E6jahuACSJXIcuf6PTWZGEiO5QGs-vtikXDHkjzHxH-HY-T1lpdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/677337" target="_blank">📅 16:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
بلومبرگ: کشتی حامل گاز قطر هنگام عبور از تنگه هرمز مورد اصابت قرار گرفت
🔹
بلومبرگ با استناد به گزارش شرکت‌های اطلاعات ردیابی کشتی‌ها گزارش داد که یک کشتی حامل گاز طبیعی مایع قطر هنگام عبور از تنگه هرمز مورد اصابت یک «پرتابه» قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/677336" target="_blank">📅 16:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b197534600.mp4?token=oynykU9-PgAcbcOH6yftciNir9sAeVd7fZ0BsENJmp709o9M0UBq3yx6_B1rA8xci-l8Qej5n1UmhpgFfoZmG5ZNDTl0Etxm44ubW2Z7-3AXICv9xYSyhr8hN19T4GGgQeeDTvj0iVwsgPOmOvuITtP3EzgI5k_nIuUDxrkbcgV8a6Q6lQ7oTWG6yIiJhWwlLEzH2aJ4R2mhGg77aoZ3pdPocPoJ_nl4Q7YK3bLfhlQIbm5Gvo1yPlIRwhf-drqsFz6dcBegHpFwtpwJ4RFiqBHB4mIbFUZeI1NxbuuckdiXoGrDkiNfJf7RtyG3SplQnvweCsnz_Gm0HdbE19BEIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b197534600.mp4?token=oynykU9-PgAcbcOH6yftciNir9sAeVd7fZ0BsENJmp709o9M0UBq3yx6_B1rA8xci-l8Qej5n1UmhpgFfoZmG5ZNDTl0Etxm44ubW2Z7-3AXICv9xYSyhr8hN19T4GGgQeeDTvj0iVwsgPOmOvuITtP3EzgI5k_nIuUDxrkbcgV8a6Q6lQ7oTWG6yIiJhWwlLEzH2aJ4R2mhGg77aoZ3pdPocPoJ_nl4Q7YK3bLfhlQIbm5Gvo1yPlIRwhf-drqsFz6dcBegHpFwtpwJ4RFiqBHB4mIbFUZeI1NxbuuckdiXoGrDkiNfJf7RtyG3SplQnvweCsnz_Gm0HdbE19BEIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا با افزایش درآمد بازهم پول کم‌ میاریم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/677335" target="_blank">📅 16:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMvGgzaW_ms02pytdWtuQriV1rnaiFnpUTDM-R7yKPHe5Y2uoIUtTp_zzXEswCocbB0Si76H_2_2C7gdpSsTuawvmCBy28KRUUK0F1haGFjQHv4XSULOpFYgeaIWRppI9ONyCklhXnROamg5ny11EGoDWHLJGcp9Kq3-aOMbvNsM9i0L_MhDq7fjoFIg01xHOomLInFZFGHb-Fy733jwPy3iotMGH65k_X_5WD_2pY-06v9mztBubnd7UhEPLDioD5B5gQJc7Srq33tck6n_1wuRlXbHtiC0zrGq0mA4qcChzfcCeqmBOL64y9iOAgB5zsNsLh3vE38ck4jV0XawWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
حرمت نان را نگه داریم؛ اسراف زیبنده سفره امام حسین (ع) نیست.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/677334" target="_blank">📅 16:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
اسپانیا خواستار نشست فوری اتحادیه اروپا شد
🔹
پدرو سانچز پس از ورود ده‌ها هزار مهاجر از مراکش به منطقه خودمختار سئوتا، از برخی کشورهای عضو اتحادیه اروپا به دلیل درخواست برای تعلیق اسپانیا از حوزه شنگن به‌شدت انتقاد کرد و خواستار برگزاری فوری نشست وزیران کشور اتحادیه اروپا شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/677333" target="_blank">📅 16:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سه گزینه نتانیاهو برای حمله نظامی به ایران
🔹
سی‌بی‌اس نیوز، به نقل از یک مقام اسرائیلی مدعی شد، بنیامین نتانیاهو در دیدار اخیر خود با رئیس جمهور فاسد آمریکا، او را در جریان سه گزینه برای جنگ با ایران قرار داد.
🔹
از جمله این گزینه‌ها حملات نظامی متمرکز بر مسیرهای زمینی تأمین تدارکات خواهد بود.
🔹
همچنین احتمالاً زیرساخت‌های انرژی از جمله نیروگاه‌ها و پالایشگاه‌ها نیز هدف قرار خواهند گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/677332" target="_blank">📅 16:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
مسدودی ۳ سایت و حساب آژانس‌های متخلف فروش بلیت اربعین
🔹
دادستان تهران از مسدود شدن سه سایت و حساب آژانس‌های متخلف به دلیل عرضه بلیت پروازهای اربعین با نرخ بالاتر از قیمت مصوب خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/677331" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb82625a1.mp4?token=If1TkU4xMxT8EY5Tar8M7bMkBebeu6kOTrTmc_DXudr457DuEERtGUuDYVsHBWonM4uHH8Ak7-zdi2LRIt__fm0j4bRfec0Q-k94lCpWHhVFNmEdmLYeOOeJT5TlLS-Dw0M4bS3BTl4GRskvUgRcc2SQRpENZhasv5-G2ysul-w20qCDBTa39jvbZkCw1SUkfS6381jJWj1ncXC7Vpoz_Ox940eIv3z8RVuZmEp2czJCCN9rUcrCHqprqUrydZMF8jSi1yXaYRZsS6w5Um1-gzfKgzpLGBpmPoJg9XdE1qdEjsc7c4AzF5gFCnL3UBPTtT4wECeh0I1vdF4n-2GJpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb82625a1.mp4?token=If1TkU4xMxT8EY5Tar8M7bMkBebeu6kOTrTmc_DXudr457DuEERtGUuDYVsHBWonM4uHH8Ak7-zdi2LRIt__fm0j4bRfec0Q-k94lCpWHhVFNmEdmLYeOOeJT5TlLS-Dw0M4bS3BTl4GRskvUgRcc2SQRpENZhasv5-G2ysul-w20qCDBTa39jvbZkCw1SUkfS6381jJWj1ncXC7Vpoz_Ox940eIv3z8RVuZmEp2czJCCN9rUcrCHqprqUrydZMF8jSi1yXaYRZsS6w5Um1-gzfKgzpLGBpmPoJg9XdE1qdEjsc7c4AzF5gFCnL3UBPTtT4wECeh0I1vdF4n-2GJpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب یک کامیون سنگین در روسیه
🔹
یک کامیون باربری بزرگ در بزرگراهی نزدیکی روستای «مارچوگی» در منطقه پرم روسیه منفجر شد و شعله‌های عظیم آتش تا دقایقی به هوا برخاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/677330" target="_blank">📅 16:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c5ec6cefca.mp4?token=g8CqCfrrP1EDCyo8caKdZCbvGZyepa_fc1dZdWLrobgeV4n5UDz0uDk-rVsgGajywW1QcdU64lKxKhMC_FzVOdmPwFw_cNyD97AhtAz6h49H3pNCS-dppKw8U2rDOg0JI65v0Ah72kXcn25z9tz_zYn2U_OG5XzXSVdBRJeF2pezQFHr1QIF7rrNkBnboantYdmAgaitdjLEvim9AKbddiAdI9qbz6_htR0_vS63_8TEFZpTgpeB3RkBvtPs4BH2fFtHUjs0KaUgBs136wq_9g396Ol8Ebq0T47Xk9xp_p82LU3XGAoxMZMGufVzM4OCp97siU214ESjJQ78yqL8xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c5ec6cefca.mp4?token=g8CqCfrrP1EDCyo8caKdZCbvGZyepa_fc1dZdWLrobgeV4n5UDz0uDk-rVsgGajywW1QcdU64lKxKhMC_FzVOdmPwFw_cNyD97AhtAz6h49H3pNCS-dppKw8U2rDOg0JI65v0Ah72kXcn25z9tz_zYn2U_OG5XzXSVdBRJeF2pezQFHr1QIF7rrNkBnboantYdmAgaitdjLEvim9AKbddiAdI9qbz6_htR0_vS63_8TEFZpTgpeB3RkBvtPs4BH2fFtHUjs0KaUgBs136wq_9g396Ol8Ebq0T47Xk9xp_p82LU3XGAoxMZMGufVzM4OCp97siU214ESjJQ78yqL8xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام سید عباس موسوی‌مطلق: تشییع رهبر شهید در عراق، بی‌نظیرترین بدرقه تاریخ عراق و بلکه تاریخ اسلام بود/ از مردم شریف عراق که این حماسه را آفریدند، قدردانی می‌کنیم
#
یالثارات_الحسین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/677329" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سفارت‌های آمریکا در مصر، کویت و امارت درباره «وضعیت پیچیده خاورمیانه» هشدار دادند
🔹
در ادامه هشدارهای واشنگتن به اتباع آمریکایی، سفارتخانه‌های این کشور در مصر، کویت و امارات نسبت به تشدید احتمالی تنش‌ها در منطقه غرب آسیا هشدار دادند و از اتباع آمریکایی خواست آمادگی لازم برای ترک منطقه در صورت وخامت اوضاع را داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/677328" target="_blank">📅 16:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677327">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
کشف پیکر ۱۱۲ شهید از زیر آوار خانه‌های غزه
🔹
نهاد دفاع مدنی نوار غزه اعلام کرد پیکرهای ۱۱۲ شهید را پس از حدود دو هفته عملیات جست‌وجو و آواربرداری، از زیر ویرانه‌های منازل خانواده «الحساینه» در محله الصبره شهر غزه خارج کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/677327" target="_blank">📅 16:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677324">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1bCNmn7nppVTPOAAsoNQP_lk5vs7FCuw-3bp74MWVv9Ch2nX1ynaxO65ebtMyfv4n-aPs4x4AY2nGNHPBWcsqYq9g4mgzRgB2aoo7w-ACzMxe4tTWRp3o2IHhlih-nCgEietWdHYiTWUkYgvkoGho63lW4r_T3rGdpOCSlpqwS4AdeDamoon0srDF_dPuejHFzUd2zfBmjBv0OSGhn6dXnoRAbNc-MUdFybB0V27nJqUJ0GKKqGaIHFYZSiPuOMvpTB2YptizYOJ5C5Yn8XC8DYERAxV68B3KsySkoPZSZjTSyexriTITXtzboku80nUN_MuDz6m4WCq-6VKy_q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APGehJbu-YB4H5s5AJhBwlnThrrpSi_q5RINRL1WzJ1NnU8yuTFDIpWcPq-aNtkaVGWVw3iqeLPzQBq77dveXGukzDXbGkXPhhBJ4algFuGhQRwqW3ZsheqUxhjcIPmCWJlKeQR0s5p60eFFuSx4SpsKtt2RWghWS43H5m85H3wB1nVp7C_AaVFOdDWQTpJ0ndJK5WbWTMPzKNTtP_sXZoYcIxb-C0oy1-GlJfPghj9DtRtLbDoji1LD51kaCotbpjjLhWgkR-9iob4Yte4ON-zhKcjqTbogwHEQQpha6XMbwrwm1g6s4bp5w9CYYDjnVxIcUUDZXF-0rs5H0UH5VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وقتی انباری جای خانه را می‌گیرد؛ «مناسب مجرد آقا» یا نادیده گرفتن کرامت انسان؟
🔹
انتشار آگهی اجاره فضایی شبیه انباری با عنوان «مناسب مجرد آقا» با انتقاد کاربران همراه شده است.
🔹
بسیاری معتقدند مجرد بودن، توجیهی برای اجاره واحدهای فاقد حداقل استانداردهای سکونت نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/677324" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677319">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آب دوباره گران می‌شود؟
آب و فاضلاب:
🔹
تصمیم‌گیری درباره افزایش تعرفه‌ها برعهده بدنه اقتصادی دولت و وزارت نیرو است که با هماهنگی وزیر نیرو و بر اساس الزامات موجود انجام می‌شود.
🔹
در حال حاضر هیچ پیش‌بینی و تصمیمی درباره افزایش تعرفه آب وجود ندارد و امیدواریم این اتفاق رخ ندهد و بتوانیم با همان افزایش تعرفه‌ای که در ابتدای سال ۱۴۰۵ اعمال شد، موضوع را مدیریت کنیم./باشگاه خبرنگاران جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/677319" target="_blank">📅 15:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677318">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31eafcc50.mp4?token=PdaB_yUAdnAHSmui5AXjL6Gih_5IBt_Vlio5Zfy2bQDJyMaP3BqT2pYy5TP6FSyiGepZAB5td-IBmm3-0u4xniJjoWX4gsv_w3OEvXwafCtBRRt5GxKjm8MoN8CuBKabo7dLTEb38H-OZZs10gVyy7AB1M95-HVfrFYSDfWBXLyKRrgUI9u_-WBsBHBpnmuuTC6Q7zTdf-LpbYkNcLUvlcZ34nN6LwFkZoW9f8UVFpvvu9IDmzmJdCvK5npsLXO4OOn_uAfLMZbhWHLbVwDatpuahMFaW97l61QYj6De6m6v-ohd3LeRYKLvreon1dtGJd6Al5G2iRQNrvPYoQRxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31eafcc50.mp4?token=PdaB_yUAdnAHSmui5AXjL6Gih_5IBt_Vlio5Zfy2bQDJyMaP3BqT2pYy5TP6FSyiGepZAB5td-IBmm3-0u4xniJjoWX4gsv_w3OEvXwafCtBRRt5GxKjm8MoN8CuBKabo7dLTEb38H-OZZs10gVyy7AB1M95-HVfrFYSDfWBXLyKRrgUI9u_-WBsBHBpnmuuTC6Q7zTdf-LpbYkNcLUvlcZ34nN6LwFkZoW9f8UVFpvvu9IDmzmJdCvK5npsLXO4OOn_uAfLMZbhWHLbVwDatpuahMFaW97l61QYj6De6m6v-ohd3LeRYKLvreon1dtGJd6Al5G2iRQNrvPYoQRxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه انحراف از باند هواپیما امبرائر ۱۴۵ از باند فرودگاه شیراز
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/677318" target="_blank">📅 15:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677317">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e5419cb9b.mp4?token=eARVfrKF0kk9d5pQtKCvnHsA5zTWG0WxDu9rLJMhX3SxJJgHCqO33sgzsWctN_DnGd4xkS1Pc88XaOp4v9TYoiNjo295iv61gCyjJEMHkiRuEwW6tQkuD8mz0vHAzlA4YrmqXpUdpUQIaWPa79joe75cxTO-ChOBuyKFWQkYDcI8nQKHuOHKhbZUSWN5OuaJUmIYXYrFzsau9bgkD36ltGkq4TfYnfZRqRh9cO1pREX6thpq7RSc5srtumTZN4IQVz1nh5gArzsopPJkaOvOjiNTkzpJYvf-lHL_oOFko6ehYquQy6jAxKRORFXh30mbhBoGj6nl6_DmnvNaDdSa0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e5419cb9b.mp4?token=eARVfrKF0kk9d5pQtKCvnHsA5zTWG0WxDu9rLJMhX3SxJJgHCqO33sgzsWctN_DnGd4xkS1Pc88XaOp4v9TYoiNjo295iv61gCyjJEMHkiRuEwW6tQkuD8mz0vHAzlA4YrmqXpUdpUQIaWPa79joe75cxTO-ChOBuyKFWQkYDcI8nQKHuOHKhbZUSWN5OuaJUmIYXYrFzsau9bgkD36ltGkq4TfYnfZRqRh9cO1pREX6thpq7RSc5srtumTZN4IQVz1nh5gArzsopPJkaOvOjiNTkzpJYvf-lHL_oOFko6ehYquQy6jAxKRORFXh30mbhBoGj6nl6_DmnvNaDdSa0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه بزرگ به کویت؛ حمله‌ای که برای همیشه خاورمیانه را تغییر می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/677317" target="_blank">📅 15:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677315">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9aeec8228.mp4?token=iGJe914PJmZltq_EErOdkL-xGpEjzrsVxpyhZSccErDb3uRPDbBIfzUqN2iIrw_a-WfXwj6Lx3UXyZRgjLgAafVuKkqyx9_7xRov7Q16d_2c3iAFq4pMpIJK-NeLsgIckwqQE8khDoRUbXTQiHWsLSwBg5sUNh6_sp7RZS4uczC1w-L6SSXVzl0O05Lkk9K7vuT87VWZJeg00JO5Vw092U-XpfvjXQq_Bmsu9cUKOOvsTRpUAdREQCpRkPg5VCOF_BjnPZ0wODH5vaCytrzq2XDyfYmMgD4I0XhxUYwGXzcb_3qv6JPxwN1S0qXKDWpuqLSHcrqpzKMoemSzYoIbrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9aeec8228.mp4?token=iGJe914PJmZltq_EErOdkL-xGpEjzrsVxpyhZSccErDb3uRPDbBIfzUqN2iIrw_a-WfXwj6Lx3UXyZRgjLgAafVuKkqyx9_7xRov7Q16d_2c3iAFq4pMpIJK-NeLsgIckwqQE8khDoRUbXTQiHWsLSwBg5sUNh6_sp7RZS4uczC1w-L6SSXVzl0O05Lkk9K7vuT87VWZJeg00JO5Vw092U-XpfvjXQq_Bmsu9cUKOOvsTRpUAdREQCpRkPg5VCOF_BjnPZ0wODH5vaCytrzq2XDyfYmMgD4I0XhxUYwGXzcb_3qv6JPxwN1S0qXKDWpuqLSHcrqpzKMoemSzYoIbrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
سعادتِ خدمت در این مسیر، توفیقی است که به هر کسی داده نمی‌شود
▫️
کسانی که با ایثار و سخاوت، تعریف جدیدی از انسانیت را به جهان نشان می‌دهند. خادمان اربعین، سربازانی هستند که در جبهه مهر و محبت، برای تکریم زائران امام حسین (ع) شبانه‌روز تلاش می‌کنند.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/677315" target="_blank">📅 15:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677308">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n67-Zope01EUJ8Eu5iuPsWRF0-mttzQZukT5X1CiZcPWgQhKoVV2rY8zzStFFg-x65tcezRh1ZKysN6FhtogPpIQ0hSSEV7Jj2e2qT_BeOTL4L3U53JPOXuDupYvrGeU6htI2XFou7bSwxTmCpQKJiQTrjhs9RRGZoWYMPbY9nprR1QrNJW8_jZkPdfiw5Vm7_WD4oGVozR1gNmYKPEJPC0NNhZmOUNwWFdDefR4skha86YmH2m-h1Criunep6poNpm_aNPpvXKmqVqk65vyfcfOUa5MO6ztA2Z38RZ32emUW0wmgq0lvHz-DiVsogeelS4Y-SKEpwj1OVWtaCKvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Td2FaeLEQN7RACJws0ovBw8VodzCLRL0IWi9_qRB32XGdPCSP6O1sEM1NRRoZ7lbIcm1MYwr-yvww8ZrVPKu9onbiVWT4fOww872V-hZnsKg8BQl8cEbFUsoi7Q4_dnX76OzvE2dn0WGNzTLZA73fgUadjh-h4L9tDlRq4jOAr9RGIfmP5E4PWCYnGpyjIZGR6IkSxLpOf5B0j-73N3erf3AIqk28XwaDU2KdzwQcmZeg9rLj6xMTTixtqBf3oIjprdhvLMaIA4shaJcljj14KPYmYNU4uKPOWiGhbb-RzzUHjrBU19gEFotk3cg48WhAZduD7QegFxQ949I8uKuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqZep3k2hG-IytLUPpUckKEzW-5l_d7gaYvIfIgitEahPDTUeu4ZtaTfAUnJ9DdrojWLzewqK2O7cU0ODzVYnZ8MbiNv9DtzT-Ip4nUN3y0okz32p-B9H33BN-IoTiUfO4b9cZpJxl7UIuTJjkAGG2uDdeK5Ts8fnvaeEttGQwKGIYAGMvUyFCoCLbkqP4kvU9FLlFe7jkq8b7MML_GX3H1soIP1uWzAjY6HHzDAL0NsOA0Ud3XyzsQwMc9WLqpo0s1xQsiRfI0RLE2nj8DJyNEJRVJCDiD76R4ItylnyRWM-MaOR1PT5hkBQ0oengyOCjlTS_TiXEq7G4VMR3AzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGFMy94t5qhm49dj8JVVCM32wBc28qD43LS1QxtnYdDrsC457AYIaCO7qddBY-XhetW0goQBAUr_N3oQYgo51GO_dcaxpWnG1CFAf-Jcnkmc6A8A7xc_fHFB5FDN8m9t4CfcYo790pJsxVLWu_P8LgpfLsgph9Y2Olt45hU9M0o3SHce7HgUqz4Ov9LAWHe1m61ezHdJNmZdsD7WeIh8-eHZWw8tpUFrQUPnfKDe51wIMLDSVnG2VTInotGxTMP_J2sUCqOqRhdEmAlAjAXKhE08S6GdOaBGVbMwL1cq_efi5tv6BK8aH1xAUXD4yR4cqnqN2vXEAmx-jZYq7ZVm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aH6Nvq0vGCedJ0IM0jU8jvathrI0IPfpn0x1s-9ulhnmtJTKkvzo63AWDi7Lblk65yW0qEpk7ENuZUT9Dw8V3oCZAuaK0LhxLcfhjp3WwrI5CM3aNSe-dcUJNnu3Kh12GyHOrDqWIrLUbBDeI3J_lzLZJHBu40KnMGPyL_n8YF6Dmnc9hqrIexfR4uhAUeOig6uW12CqAyhJwO4Wym3HeRgi3tJjLjHmHki_DAPxXGXHdTb5X50_u6p7omsXF1u6A6yLm7LaAagK-3x__MxLG6w2ydgk4Ov8cbfkhtHtmESn_E0I6JjccoIUM9rP0L-F1gIbjv_9tobpw_LeUTJKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1NbuXnTy9fuzj93iHMi8iB-QvBuc0IDbLYnWHawi_7bNLYq1MlmKgNMgwCe8RjejAzofNbWK6tcMJwo_axvTm80uAAlskojkZpBee8vlbP5Cp4uyORzvzJslmQwYF1ypqbvLVXvqKukEGBBsF0iSpMBhvXH0jclqw_9B_xEjHb8HQqfjcmNU7Vbd4rkypqHI72wtGXddK2J07ttNzqcqrnJUQncWAQxUtx5Vqo_hm9ixGOGJcA9aiBkLhD8FrryKCeDXy_Pb-Pzgs56Iln3W_4ilHzy4WrH9mqV93k25emG60hv-n8T227kKNR915s8fefzwS_chP3t98eEGnlZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2wkzjH-_hllLpssA8meJ96PjpcblhXIoR2kOURep7V2KXd5LbSrnqGO54apYeRsenA3rvoIbQak6M00q7CbbJUOfhA-O4wkwoEBckAtQRCbicW5ntnXISeeSn9GeO_S_eQB2FD8WFyuaSPFNzQ8yzaoK3eetow1RA2Gc6qLnTg14TvQdyG7HjCFF4-be47DvZ45GwN8pwyct47G4-uH43QormE2JyIuPtgEK_4-zErmckgDv0AUA1I3I5ftJgm6w6TGaw4VgoZMIU8u2t6GqDngjL614HySEegLJBSdBcM8ozTndjXACJItLigQ7YquzX4fRufq-KV0fypzLaLQhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمایش عشق و دلدادگی خانواده بزرگ فولاد خوزستان به مکتب عاشورا در چهارمین آیین «نذر حسینی»
🔹
در آستانه فرارسیدن اربعین حسینی، بار دیگر فضای معنوی و شورانگیز یاد و نام حضرت اباعبدالله الحسین(ع) در میان خانواده بزرگ شرکت فولاد خوزستان طنین‌انداز شد.
🔹
آیین «نذر حسینی» که طی سال‌های اخیر به یکی از برنامه‌های شاخص فرهنگی این مجموعه صنعتی تبدیل شده، امسال نیز با حضور گسترده خانواده کارکنان برگزار شد؛ رویدادی که چهارمین سال برگزاری خود را پشت سر گذاشت و توانست جلوه‌ای از همدلی، ایمان و مشارکت خانوادگی را به نمایش بگذارد.
👇
👇
akharinkhabar.ir/local/10964167/
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/677308" target="_blank">📅 15:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677307">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
پنجره متفاوتی به آخرین دیدار شهید هنیه با رهبر شهید انقلاب، در روز قبل از شهادت در مردادماه ۱۴۰۳
🔹
بازنشر به مناسبت سالگرد شهادت مجاهد بزرگ شهید اسماعیل هنیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/677307" target="_blank">📅 15:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677304">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7898f9c624.mp4?token=SYgyVGz05NFsUW5ZwBXcBwdJM1eG0Vx9grIQ1KGep1Y2AoDlDdj-daSRWe689fcijrpmVazTq1DrRxC-HbLje1O9-GlXZqg61-GX85RwRJeniK_eWgcZ46kjwCEYGslRPCBZxJDjMLBdGYqHprlfl09VVBt21n-MaT38IOQLFLMjnbtY5eUd5CdhrKEuSVJPgMqxMnnlUpAYMk3qNNV_tGFudTsXtEn-Hen3YaAXitA8kJZ2Yw5bECS7xJ-RbMdQsc7h1Qy2R231L_Tvq-G10y-A6qOV8ig-IbG4c57v2Ncc_F-Xs3vNHpaNjJt9dvvjP6bEM5sfUmdcRcM6GZbAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7898f9c624.mp4?token=SYgyVGz05NFsUW5ZwBXcBwdJM1eG0Vx9grIQ1KGep1Y2AoDlDdj-daSRWe689fcijrpmVazTq1DrRxC-HbLje1O9-GlXZqg61-GX85RwRJeniK_eWgcZ46kjwCEYGslRPCBZxJDjMLBdGYqHprlfl09VVBt21n-MaT38IOQLFLMjnbtY5eUd5CdhrKEuSVJPgMqxMnnlUpAYMk3qNNV_tGFudTsXtEn-Hen3YaAXitA8kJZ2Yw5bECS7xJ-RbMdQsc7h1Qy2R231L_Tvq-G10y-A6qOV8ig-IbG4c57v2Ncc_F-Xs3vNHpaNjJt9dvvjP6bEM5sfUmdcRcM6GZbAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت دانش آموزان در امتحانات نهایی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/677304" target="_blank">📅 15:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677303">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037bfd86f9.mp4?token=r2uda8on3KbCi886Wfd6GFyYC39BGxdyZE5hJV3lT2xJUql9l-xaYEoyX2Ch9km5cnIPxM9CgaekC2tnocoUeUOcRCYqxprjEBxsHf5iIgMdAiXGeiPEKa4RQaStZBouU4FCmdAAmtIkbrTZ9uSbeD0MzO2DKgq_qO4QR5qz0Ijv-SBZ3O4Bmc38Zd8bvFVEV4hacUCbietSbjAq-RxwULajAB7Dpyza0_RE7AWwvEEPYT4aG63BZRkmamYQ9pb80YgEfbk3mNJf6X1j7I-p3miCV1--ujSJym20DFTD0AOaucYMr7IJCcjtHSXn56sgc56maMrQPkfaNw48IXVJAQ62U0NTIQ_BwW7aIfSg1tZUtvwAUSMenxsfPCjR0SSCaswyHHGaFWtKEl2UCAXtwdHtZjgkcVJ3YJ5cSG7KhBzojGHy-ICMK6RyGgs0LpZEQgd3HjqAoqgdw6IZSjQlbWxxaUxvT-1DDE8IF0SjYeqqB5WXI5yTlanmfqLAxib45bqUyC2fHu-EsaGAyhb8Ia4T9xG7Ljo07_SIBLKqSjTv5FByCVF4vnBaNI6mthlzhAImKb4HiglbfEKoZrj_zbpa_20xOs1uJSf4ayXfxudnvrzx23L9B9TbStFyHXBert7aADAs--ccfSF6WIEop4AJd25g0SNLjw_NQcVW1bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037bfd86f9.mp4?token=r2uda8on3KbCi886Wfd6GFyYC39BGxdyZE5hJV3lT2xJUql9l-xaYEoyX2Ch9km5cnIPxM9CgaekC2tnocoUeUOcRCYqxprjEBxsHf5iIgMdAiXGeiPEKa4RQaStZBouU4FCmdAAmtIkbrTZ9uSbeD0MzO2DKgq_qO4QR5qz0Ijv-SBZ3O4Bmc38Zd8bvFVEV4hacUCbietSbjAq-RxwULajAB7Dpyza0_RE7AWwvEEPYT4aG63BZRkmamYQ9pb80YgEfbk3mNJf6X1j7I-p3miCV1--ujSJym20DFTD0AOaucYMr7IJCcjtHSXn56sgc56maMrQPkfaNw48IXVJAQ62U0NTIQ_BwW7aIfSg1tZUtvwAUSMenxsfPCjR0SSCaswyHHGaFWtKEl2UCAXtwdHtZjgkcVJ3YJ5cSG7KhBzojGHy-ICMK6RyGgs0LpZEQgd3HjqAoqgdw6IZSjQlbWxxaUxvT-1DDE8IF0SjYeqqB5WXI5yTlanmfqLAxib45bqUyC2fHu-EsaGAyhb8Ia4T9xG7Ljo07_SIBLKqSjTv5FByCVF4vnBaNI6mthlzhAImKb4HiglbfEKoZrj_zbpa_20xOs1uJSf4ayXfxudnvrzx23L9B9TbStFyHXBert7aADAs--ccfSF6WIEop4AJd25g0SNLjw_NQcVW1bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب زائران ایرانی به بمباران برخی مناطق عراق و شایعه وقوع جنگ
/ تلویزیون اینترنتی مدار
برنامه‌های تلویزیون اینترنتی مدار رو در یوتیوب ببینید
👇
https://youtube.com/@madaar_tv?si=ICb2BPIkhXtjbTUS
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/677303" target="_blank">📅 15:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677302">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_XVoClew39N6GLVClTqMzo3Va45KdFgmgSeAVPy8Kd6xL7XeyAUZ9v4leAU9jfIdnQrGQ6fj5--E8GZYAJfFyfxY0vBamKnBvgO4Nivz0u7LR9J7ixXRm0Wai6M_AMkRcrVYfVpOeqs55KcAvxR-lXYJGpwG7hmqlxONsklaPGCwBUGUMW2LS9yuvjexX2GrrzKLgwfvVfZaoCSN470WbceX4LEcI42L6cXnqTk6bI2lFrygN3pASOW8FS4rcsB8Xv28wk5guiz2IjtCjJY7IvUAXlQggNLRdizMGJjW3HamTsZw-2Z2dfG7PZzx-8LboM-4J4_1n_N-nm2wMhIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیبات موجود در توت‌ها، چای و کاکائو؛ دشمن پیری مغز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/677302" target="_blank">📅 15:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677301">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b36c837c.mp4?token=khR-7X8_uleoocYw1S3_YzfYIL-M4vUmVQp3AUhMa7v8pN_HeX4U0qQptIkMXdE1ik6kGJ3sioQoNob3CKDhwDtJeqjJfAEn2MlZsaPo-F0nZwFifqI5URhZe_uz-tjvqBfE4CM4qNYBBU1XbRSXfTKptdt5eiStIXQMyHImrgF7O7bC_UwcC0vvsuh0Pt2zp4yD8pTWSI6djv-vGTX9bN3LhN-xbPFGTXIg5y14hYO3AmGhqSymSBlIa7vq0Sh7QhZmopKX88IfbIclZwH3bHhlGldph-AKDryrUm-3fuSF5RomCNFChuoEcuamV5taUlRLD95nuB7LyoPDp40PIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b36c837c.mp4?token=khR-7X8_uleoocYw1S3_YzfYIL-M4vUmVQp3AUhMa7v8pN_HeX4U0qQptIkMXdE1ik6kGJ3sioQoNob3CKDhwDtJeqjJfAEn2MlZsaPo-F0nZwFifqI5URhZe_uz-tjvqBfE4CM4qNYBBU1XbRSXfTKptdt5eiStIXQMyHImrgF7O7bC_UwcC0vvsuh0Pt2zp4yD8pTWSI6djv-vGTX9bN3LhN-xbPFGTXIg5y14hYO3AmGhqSymSBlIa7vq0Sh7QhZmopKX88IfbIclZwH3bHhlGldph-AKDryrUm-3fuSF5RomCNFChuoEcuamV5taUlRLD95nuB7LyoPDp40PIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر اقتصاد: انتقال سهمیه سوخت از کارت سوخت به کارت بانکی آغاز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/677301" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677299">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2gEo-Fz2wcsncJEEI5_ChhkEv_5guuWGw2d00gClSgRmexfa556yZgJ9216nk-fA-X6bV0TP6o61iKVHvBYW26_-dlD1D0EUeycC6FVQ-_V1BMv7T0Dotin0u30Hw5WoYOxMHnd6bAS5x4RsyDI0ZIElnTbT2-Xjcxy9-s1dyUFL9dA98hdRSZW0ghK3hZpBN50shBygSu6eX1rZckJxMlBeBDSnbzAyWgwQJRIkq3ZalbJLsop7Z1eEKnCDEe-iLQU8OBZ4ReOa50fZ7yNbvzKV-iSv2VR4af323aQIkpMHEKsdjLX8lcsdXMM5gFTue1SZPhIJ6SXTFf5piKGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیر سایت انگلیسی امواج: گزارش شبکه CBS مصداق جنایت جنگی خواهد بود از جمله قطع برق یک کلان‌شهر ۱۰ میلیونی بدون اینکه حتی یک کلمه درباره مشروعیت و قانونی بودن آن گفته شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/677299" target="_blank">📅 14:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677298">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg81fqSDqoYXQhCoZKT47lxw2sjfaa_nFkX8O0-9ROykIdHIn8ltfYxZHM_eVQpx5YcUKDjuUn3znARxUI9mzcc2VYNZVo06hOo9kqO7rasOQJ-ES2OgjtnT1Bvh2LTGywY7c_4Qukq_HZUM9b7jl9e6NEPnpyXutGVfZqdaRrZr9B9UD_iR1v1lz-VHmRNYkr2mPe0YSmYbL0v2C7q7t79v2Hbng_57BzgpkKyZFB7B1mK4e0MEd9Ux5lxesc6JyY8dFeQWy2pnLtzrc6iGjfbtqEP0oaTLbwgNsmW6odV8zw-adP8fKfxnDpYCYNfmB5ePwYt8VPENbfSL6DKjtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۰ مرداد ۱۴۰۵؛ ساعت ۱۴:۲۵
🔹
قیمت دلار در معاملات امروز با رشد قیمت، به ۱۹۴ هزار و ۳۰۰ تومان رسید.
🔹
تداوم تنش‌های سیاسی و نظامی در منطقه، مهم‌ترین عامل حفظ روند صعودی دلار و افزایش ریسک در بازار ارز عنوان می‌شود./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/677298" target="_blank">📅 14:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677296">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmjShedhMHu9RYENWoRGHwhaE14pSiCGxPIni0IDRedh6kuyO3OlrTG8xrLmKbWqhwSQzZahQ7KU3kNTA9xIpl-7l0w1b2JwvkN-6XDxYJxppu0wjjVXnWfX10gvjWvlXvaiQ8PpwvAT1gsVEVTiSRbVHzv07NuTZJAF_gcQvU8lzTxHOCIORl-raSO-nzgrHKSs67tEDDEqcLPwtn73-7rk-InILGdccEolrtz6wgpvz583GKZ8ZEGMMb9Okmko4w_hjLVdOKs3QY9FCLp5HyhOeBB4pQJLpU_89NefQGlVD2xweLc4o8lQANcNNnOQGEusvj5AotBrdJnDVzlWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمیسیون سلامت دیجیتال نصر تهران: پلتفرم‌های سلامت دیجیتال غیرقانونی نیستند
🔹
رئیس کمیسیون سلامت دیجیتال سازمان نظام صنفی رایانه‌ای استان تهران در واکنش به نامه مشاور اجرایی معاونت درمان وزارت بهداشت درباره فعالیت برخی پلتفرم‌های دوراپزشکی تأکید کرد:
🔹
فعالیت پلتفرم‌های سلامت دیجیتال طی بیش از ۱۰ سال گذشته در چارچوب قوانین کشور انجام شده و تلقی غیرقانونی بودن آن‌ها بدون پشتوانه حقوقی، فاقد وجاهت قانونی است.
🔹
اگر دریافت مجوز برای یک کسب‌وکار الزامی باشد، باید این مجوز بر اساس قوانین موجود تعریف و فرآیند دریافت آن به‌صورت شفاف در درگاه ملی مجوزها اعلام شده باشد. نمی‌توان فعالیت کسب‌وکارها را صرفاً به دلیل نداشتن مجوزی که مسیر قانونی تعریف آن طی نشده، غیرقانونی تلقی کرد.
🔹
پلتفرم‌های دوراپزشکی به‌ویژه در دوران کرونا و بحران‌های اخیر، نقش مهمی در حفظ دسترسی مردم به پزشکان و تداوم خدمات سلامت داشته‌اند.
🔹
سیاست‌گذاری در این حوزه باید بر پایه تنظیم‌گری هوشمند و استفاده از ظرفیت بخش خصوصی باشد، نه ایجاد محدودیت‌هایی که می‌تواند نوآوری و دسترسی مردم به خدمات سلامت را کاهش دهد.
متن کامل خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/677296" target="_blank">📅 14:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677295">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czgppm7kOcSUUN-WmdPYlVaJnEF5oScfJA88O7IvEXKtOEk_P4vqvk5QPSeDEKEJoV7sQg_Tun52bEA4AijMhidnf2_qmG6pTqDFL3JX6YcZll9DUeuhvAhGgBKDQ0xz0NCczSEnSzrBKAu0JyR-wghLadrIsz3CYrs46wh91LkvrcZFZGab-F-T_lXxgsQtJN9DyvSzmbqAwSsbuf0IfmsGJZciddotkN7wxjYHt61E-uXWLOPyp3J7Wb_E08mo-VAC7LuqY_3hcFTwQrtDwtkEOABtbGTOEGu4Zpppsy-8aN3jjS7JPXGxZmc36ZBwJL1Ee8o-78J9tir01wEdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولویت مهارتی آینده از نگاه افکار عمومی چیست؟
🔸
در این نظرسنجی بیش از ۲۷ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۴ درصد، بله ۲۸ درصد و تلگرام ۱۸ درصد بوده است.
🔸
بیش از ۴۴ درصد شرکت‌کنندگان، هوش مصنوعی و کار با ابزارهای AI را مهم‌ترین مهارت برای آینده دانسته‌اند.
🔸
کارآفرینی و راه‌اندازی کسب‌وکار و مدیریت مالی و کسب‌وکار در رتبه‌های بعدی قرار دارند.
🔸
با گسترش هوش مصنوعی، اولویت‌های مهارتی از زبان انگلیسی و برنامه‌نویسی تغییر کرده و AI به یکی از اولویت‌های اصلی بازار کار تبدیل شده است.
@amarfact</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/677295" target="_blank">📅 14:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677294">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9316cef4f.mp4?token=VlxEli54Tqm-B9-s58T9YE9ZwPUCAFKcMawtajllDvSTmoTeiWLA6yFQ2pt1pYC4gznZB1JLq75yO5hgG_CaeITe1J4fNetG1Sn8xhDvisbEPsIu3Oi9ADT0SqREOSBNNZYiyw2DCH4iGAKtK22FBMiOKpfbk9-uJNDF4O6hDLrI2S3sHQggx3zV-2ywIUuHGL6IsyezwsvtL3CVry-fXvvvOiGV-73XQ4oOORn1fh0JuX07W8Z5QvuenC-aIyeupFeDfOLDRXQuu3LkI0yK4WTxQqC2usbcEr5BtCtlJxof0KoEFigPtPW07j4EJMbMH9K2a0Bg-vexX062k8PfyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9316cef4f.mp4?token=VlxEli54Tqm-B9-s58T9YE9ZwPUCAFKcMawtajllDvSTmoTeiWLA6yFQ2pt1pYC4gznZB1JLq75yO5hgG_CaeITe1J4fNetG1Sn8xhDvisbEPsIu3Oi9ADT0SqREOSBNNZYiyw2DCH4iGAKtK22FBMiOKpfbk9-uJNDF4O6hDLrI2S3sHQggx3zV-2ywIUuHGL6IsyezwsvtL3CVry-fXvvvOiGV-73XQ4oOORn1fh0JuX07W8Z5QvuenC-aIyeupFeDfOLDRXQuu3LkI0yK4WTxQqC2usbcEr5BtCtlJxof0KoEFigPtPW07j4EJMbMH9K2a0Bg-vexX062k8PfyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده ۲ قلاده خرس‌ قهوه‌ای در شمیرانات
🔹
مدیرکل حفاظت محیط زیست استان تهران از ثبت تصویر دو قلاده خرس قهوه ‌ای در مناطق حفاظت ‌شده شهرستان شمیرانات توسط دوستداران طبیعت خبر داد و این رخداد را نشانه ‌ای از پویایی زیستگاه‌ ها و اثربخشی اقدامات حفاظتی در این مناطق دانست.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/677294" target="_blank">📅 14:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677293">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
کلاهبرداری با عکس یادگاری
🔹
یکی از جدیدترین شگردها، ارسال پیام‌هایی با عنوان «عکس یادگاری» یا «تو هم داخل این عکس هستی، دانلودش کن» است که کاربران را به نصب فایل‌های آلوده ترغیب می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/677293" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677290">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
قتل در نازی‌آباد بر سر زنگ مکرر ساختمان!
🔹
مشاجره میان یکی از ساکنان ساختمانی در نازی‌آباد و مردی از اتباع افغانستان بر سر به صدا درآوردن مکرر زنگ ورودی، به قتل ختم شد.
🔹
متهم پس از اعتراض ساکن ساختمان، درجریان درگیری با ضربه چاقو او را به قتل رساند و از محل گریخت. پلیس آگاهی تهران تحقیقات برای شناسایی و دستگیری وی را آغاز کرده است./هفت صبح
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/677290" target="_blank">📅 14:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677288">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac437de3c.mp4?token=RH20cKLTbElyQWrnwuBjvp-4mrgXsto_WoT2pKJLIC-l1PWsOkaN0LvvDHFAvEw_25OWQLc7fEQhGmeGZsq4uQOMxPxU_1-F47WNpquWxJnBokLj5gKLoGjYLOAtsr16aMPaGUQbJ4zNiVbdd0A03-TFD4bqBB4pmPwPQgTC3fYsUKHy39f90xdfCmaGx4peUtFfGPdAa3W1EHIaLpYqK0lOfjdsDVZaNbpRYxWEnjvY_N-qwgCt_yRNq8O3O9bQTipUJO23jZ0N5ko2Wvi-VWMs3TakX2IN-9bWCSEYaRsgsLDH_MLkUcVM46zbVjaoaERqg8BbB72IoQ5jmyw-Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac437de3c.mp4?token=RH20cKLTbElyQWrnwuBjvp-4mrgXsto_WoT2pKJLIC-l1PWsOkaN0LvvDHFAvEw_25OWQLc7fEQhGmeGZsq4uQOMxPxU_1-F47WNpquWxJnBokLj5gKLoGjYLOAtsr16aMPaGUQbJ4zNiVbdd0A03-TFD4bqBB4pmPwPQgTC3fYsUKHy39f90xdfCmaGx4peUtFfGPdAa3W1EHIaLpYqK0lOfjdsDVZaNbpRYxWEnjvY_N-qwgCt_yRNq8O3O9bQTipUJO23jZ0N5ko2Wvi-VWMs3TakX2IN-9bWCSEYaRsgsLDH_MLkUcVM46zbVjaoaERqg8BbB72IoQ5jmyw-Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفع زگیل جوش و دست سوخته از دید هوش مصنوعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/677288" target="_blank">📅 14:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677286">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
مالکان مکلف به اجرای مصوبه سقف اجاره بها هستند
وزیر راه و شهرسازی:
🔹
موجران باید قراردادهای سال گذشته خود برای اجاره دادن خانه شان را به مشاوران املاک تحویل دهند.
🔹
سقف افزایش اجاره بها مسکن نسبت به سال گذشته ۲۵ درصد است و همه باید آن را رعایت کنند‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/677286" target="_blank">📅 14:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677284">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a7c160b8.mp4?token=tyTNSNerCmL7_KaxOpl4rQ40e7GYbBmtnBXwkm6flsJB3i4RCW7PzhTXLjqeXra7LCweKQorP4WkzT9wbQ7d_U_Oblxm5iVxbQoZoEMX4YBgaHTO8XEVvTcGsbUqswy2fNrniJ0O40f0TxluPxcXUhwu3cR8VBsfmhFqqNKZR4OuGKmRsAHbZPZfoweCoJDLIvsPM9_8Ql2SxycykAqeDXBGr1jW7ouIQ5QvRbTjNLPxN1UIdlO3lagF7lO016-awGWvLhQV7uLaJGQ8oqWdWsiJDFiwdiBArSz--wl39K2UJBHb-J9HXUsVPO2LEoMwOrSzcF8vEhl96VWLa5SelA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a7c160b8.mp4?token=tyTNSNerCmL7_KaxOpl4rQ40e7GYbBmtnBXwkm6flsJB3i4RCW7PzhTXLjqeXra7LCweKQorP4WkzT9wbQ7d_U_Oblxm5iVxbQoZoEMX4YBgaHTO8XEVvTcGsbUqswy2fNrniJ0O40f0TxluPxcXUhwu3cR8VBsfmhFqqNKZR4OuGKmRsAHbZPZfoweCoJDLIvsPM9_8Ql2SxycykAqeDXBGr1jW7ouIQ5QvRbTjNLPxN1UIdlO3lagF7lO016-awGWvLhQV7uLaJGQ8oqWdWsiJDFiwdiBArSz--wl39K2UJBHb-J9HXUsVPO2LEoMwOrSzcF8vEhl96VWLa5SelA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از  شناور متخلفی که در آتش اعتماد به آمریکایی‌ها، در تنگه هرمز در حال سوختن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/677284" target="_blank">📅 14:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677283">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm-Nrwbt5X_YHoJdrhgTinzK6AZdSEHDzcbC2ycFbJ5qfpnoEs54xE3BNbS5VGEPKb0VnQzbekQ_QhcGMqvahMZ0A8Bprene0CvHcaro2FWWEvnBfzGSCX6dtGlBWeO9cq18jctUwILFP41YXJa8r74jYDHtGE6SkMNt8Tky7tOgRzpDvVJHZclw0ppfFvu6AzARWo_NXfe25zsQ_lomVKUdb-pPpoNmSHEi0iCnE5rRQTls6JYUScYQ3L3VSkvVQap2eUObqWoaDHpmwfQvSprNo_uegD23fzkG19IVsITsBbz7x6fOIYPFVwr9RQBdek0biKpo0zUQkI9HeW6ctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
هزار سفر کربلا
✨️
▫️
فقط کافیه عدد «۲» رو به ۳۰۰۰۱۱۵۲ ارسال کنی و در پویش زیارت به نیابت از رهبرشهیدمان شرکتی کنی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/677283" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677282">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔹
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست./ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/677282" target="_blank">📅 14:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677281">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf15376740.mp4?token=QEgWrQ4V9IgCodGQuG-nRhoJMq6fpQsd88MdyfIlP-o_E2o9oiygfNnu98PIVoaZs8TJpLFG18hJJysQ3kcrRgUxZzStGJoaTQU561NFLEpZII-0Gv_xQQ1kVVogEh7tB9I3opDCmdnSTe1Oamq8jzNCYP91Y3vFyAQU1IrVO-sYVtHhlQWqERmetKBK0N3ObVxORZDmxn0JwRnsh64-4z68zEUJW9S7xZDltXTwA-Hr8WyM30-sbFV1UORtvnhamHpNrvqt2G6_8V8tcZJwUhF7Wvy-AZECMjyQZHu3dvultn4CsNgYmV-VbVZ-JuymDHzb0UE3V0Ech4lIEB-PpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf15376740.mp4?token=QEgWrQ4V9IgCodGQuG-nRhoJMq6fpQsd88MdyfIlP-o_E2o9oiygfNnu98PIVoaZs8TJpLFG18hJJysQ3kcrRgUxZzStGJoaTQU561NFLEpZII-0Gv_xQQ1kVVogEh7tB9I3opDCmdnSTe1Oamq8jzNCYP91Y3vFyAQU1IrVO-sYVtHhlQWqERmetKBK0N3ObVxORZDmxn0JwRnsh64-4z68zEUJW9S7xZDltXTwA-Hr8WyM30-sbFV1UORtvnhamHpNrvqt2G6_8V8tcZJwUhF7Wvy-AZECMjyQZHu3dvultn4CsNgYmV-VbVZ-JuymDHzb0UE3V0Ech4lIEB-PpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تست قدرت گردن یک راننده فرمول یک در مقایسه با یک فرد عادی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/677281" target="_blank">📅 14:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677279">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee349df35d.mp4?token=d5SsuCuCTLHoSx254cooVOxU_AMv9qVbDHWMeeFwucBe6iZC9CTOOLwAmPyfhnuspOm2SRGs_D_n1c364xAEhOizPC-eNYCCM6qeEtVnWM_mVKBW-2DSnHnQYycsdQrrkjeTFyPQF9sQyf7I5xQl39PBNfpf7LhfKVWvsqV7KMIWaafxDCKiOTcmP7ls0DggCGp7Fptvz0KbNSDusPk_8J4-3PIHseqIClNh86AAUEIM3o85Qxv9c_W9_nDonXtHpx3Tf5Sb5PdZSld9JyEf3SyFIC8R7FzCnxt7j0cRd9z9hhZFZc7oAEJGlhScS1d-yVD3Y6J8domXEcvQ0m6r0YSu9F8hcNIghwidcICeFTAtd7IQPKW_NC9Mt7sQGaLcBZjZd6VHRwLk_azAyWHcPb4IafnrpcaDIyv7u7g2iCBqUPoeYAf5a2SzA3CWHakJW-qPnZBM8eUavd8b95K88y4lXAvr-5FptDh-Uu5H1OoS8U9zIYaVAjl-S_Q6FFYYsruS3KxXoPNX_Skljc_nRHcV2GAWWJaSfn26CxnLnkVH4LwDx-XjeI5zzWYNk41LMZUL8J6kyUjJs2He3XO9v0bMRp7kGndDcmWaZZQ21HM6529I493TtZ45rRcxRdRpso3df9XP9BQIBmJSOl1Z9z9HQZxtAW0r0o7A2UUGuUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee349df35d.mp4?token=d5SsuCuCTLHoSx254cooVOxU_AMv9qVbDHWMeeFwucBe6iZC9CTOOLwAmPyfhnuspOm2SRGs_D_n1c364xAEhOizPC-eNYCCM6qeEtVnWM_mVKBW-2DSnHnQYycsdQrrkjeTFyPQF9sQyf7I5xQl39PBNfpf7LhfKVWvsqV7KMIWaafxDCKiOTcmP7ls0DggCGp7Fptvz0KbNSDusPk_8J4-3PIHseqIClNh86AAUEIM3o85Qxv9c_W9_nDonXtHpx3Tf5Sb5PdZSld9JyEf3SyFIC8R7FzCnxt7j0cRd9z9hhZFZc7oAEJGlhScS1d-yVD3Y6J8domXEcvQ0m6r0YSu9F8hcNIghwidcICeFTAtd7IQPKW_NC9Mt7sQGaLcBZjZd6VHRwLk_azAyWHcPb4IafnrpcaDIyv7u7g2iCBqUPoeYAf5a2SzA3CWHakJW-qPnZBM8eUavd8b95K88y4lXAvr-5FptDh-Uu5H1OoS8U9zIYaVAjl-S_Q6FFYYsruS3KxXoPNX_Skljc_nRHcV2GAWWJaSfn26CxnLnkVH4LwDx-XjeI5zzWYNk41LMZUL8J6kyUjJs2He3XO9v0bMRp7kGndDcmWaZZQ21HM6529I493TtZ45rRcxRdRpso3df9XP9BQIBmJSOl1Z9z9HQZxtAW0r0o7A2UUGuUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت عشق ملائک به غیرمسلمان‌ها/ چگونه می‌توان فرشتگان را جذب کرد؟
/ تلویزیون اینترنتی مدار
گفتگوی کامل در یوتیوب
👇
https://youtu.be/ckhhIgbCtaE?si=oXx9NgHAEAIdXDJ7
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/677279" target="_blank">📅 14:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677277">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159c0b99ec.mp4?token=QB4bpZmbOdu6fNqFWBpvKdeosjwEGNzaqcISXrHmgJE6FbwceUN4ZrGLIx_T-7CyqFOhd1Xlwri7soJLnm34hKlsNnU7F6vYykjDgUCeZLvelu_izXnf5imFnv86MBwituE5VOFh16rlMVWYWVPz9nOp9Jx4vg2_J0n5XTZjLsxNVgpCIBJfnEP5rxjwa7mFfSEQxqhK5YPWi8lIEWRWBP0J7R2SpC78BFOq6CGOz4YU7cDsow7tyfIKwe8ShxWha6-xjp2m-9Fi4_55Zgr7Mvzu4ElWJjO1tFcfEEN47mBEm9gv4g_a2UcYs8pH14salwobQqHC4SzEzIufBy1nDa0n60w_FNyEvpEoWKPYfZQi9v_AiqknUe77Vb-_sy9teADS0XgPXgjssj1bhTjh2Zcy1tPtMmmynKUUC4lPPSLWnIoaRoaj7rVGvyAyMaEd7cVTThaDUvQK8SX5IjaCnllpVKwin1vJAa11PVxtKyw0Y-LeuPzNFBcSgmHykg4rrjABpF8FuELxEh1hhopWyUrSR5nPD9uVN-C-RFiapB1Sv39y7GtW2FDeNYOIL3vF_1sW4kt6v-nUB9PO7tIX84xdl237eJCgk7C2sX5UenTtuoIZ1hQSN90pgR7Az-1XgsL3hHuH13JJF2xomSmIy4lLmM1YzFxLOPjpb5oFGvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159c0b99ec.mp4?token=QB4bpZmbOdu6fNqFWBpvKdeosjwEGNzaqcISXrHmgJE6FbwceUN4ZrGLIx_T-7CyqFOhd1Xlwri7soJLnm34hKlsNnU7F6vYykjDgUCeZLvelu_izXnf5imFnv86MBwituE5VOFh16rlMVWYWVPz9nOp9Jx4vg2_J0n5XTZjLsxNVgpCIBJfnEP5rxjwa7mFfSEQxqhK5YPWi8lIEWRWBP0J7R2SpC78BFOq6CGOz4YU7cDsow7tyfIKwe8ShxWha6-xjp2m-9Fi4_55Zgr7Mvzu4ElWJjO1tFcfEEN47mBEm9gv4g_a2UcYs8pH14salwobQqHC4SzEzIufBy1nDa0n60w_FNyEvpEoWKPYfZQi9v_AiqknUe77Vb-_sy9teADS0XgPXgjssj1bhTjh2Zcy1tPtMmmynKUUC4lPPSLWnIoaRoaj7rVGvyAyMaEd7cVTThaDUvQK8SX5IjaCnllpVKwin1vJAa11PVxtKyw0Y-LeuPzNFBcSgmHykg4rrjABpF8FuELxEh1hhopWyUrSR5nPD9uVN-C-RFiapB1Sv39y7GtW2FDeNYOIL3vF_1sW4kt6v-nUB9PO7tIX84xdl237eJCgk7C2sX5UenTtuoIZ1hQSN90pgR7Az-1XgsL3hHuH13JJF2xomSmIy4lLmM1YzFxLOPjpb5oFGvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت هجدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای حامد البرزیان که با وجود داشتن یک زندگی نسبتاً عالی، بخاطر یک تهمت که به ایشان زده می شود، ناشکری کردن را در زندگی شروع می‌کند و در شبی بر اثر سانحه تصادف به کما رفته و در برزخ روی تخت سنگی مورد عذاب قرار می‌گیرد اما با گله و شکایت از خداوند به خاطر دوره آفرینشش به دوره حضرت بنیامین برده می.شود و زندگی در آن زمان را تجربه و از کردار خویش نادم شده و توبه می کند را نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حامد البرزیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/677277" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677275">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران، حلقه اتصال دولت و بازار برای تاب‌آوری لجستیک
🔺
اتاق بازرگانی تهران به‌عنوان پل ارتباطی دولت و بخش خصوصی، با هماهنگی شبکه‌های لجستیکی، تاب‌آوری این بخش را تقویت کرده و با استفاده از داده و همکاری مشترک، به افزایش تاب‌آوری و مدیریت بهتر بحران‌ها کمک می‌کند.
⬅️
منبع: گزارش معاونت مطالعات اقتصادی و آینده‌پژوهی اتاق تهران
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
www.tccim.ir</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677275" target="_blank">📅 14:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677274">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxfTnJbCd1T0zfQf-nfgV4YyE0L7OASrlmE-mjHfhxHMPQ4RDDphcm3oPPWv0XLuwyQZRjQ3iTArdtdME91BoFkm1vWJL5Gh88lZa3ZN6KHYu1bXCC35kDGC9eMKrVfZF8DdQrkBjBLf5c8kMz4Fzk5mAz0i4ARUgyGVbmRORq2jJhNXq-O6md7Zkc_vGMFtgKLA5vN2rN5mWqejKkj-0t0SgZQooxt01I8w34peFZ_HzqmcOckFrGwicY_BzZ6MEMGdOcow6V4i2bNkPLm-Kbg7ngA2MzVnXoj44_dsJLjaaKkYVrMAL4IwwP_9SY9oz81CKqUiH5IXLzTjFgYceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربرد و تفاوت انواع کت رو می‌دونید؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/677274" target="_blank">📅 14:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677270">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e836379e.mp4?token=LEQ4R8uVdtUTn5sGmMXEFjas4E8vAIDRp1Sh-_fcopXsEuBjRDqkZwGCHvB4OZ1co9Bch8f3XNZqVOSk5GImFP6W2PjDhYoIcd-hapjend6bCHIdbpVtLxfikq27YpFACYIl7798EiiFRtLeqoCWug2tAOm8Ruq3_S5h_eAKrjPCIp1876DTEqyi2OdP0rnpQWt1kIt6HX1N9t_WogYUC3UvsY9P9zhsmDVhZAf2P9R0jpiTMA0mT92YKvLaQ5kdHymoirOegAAEVBy9a2tQza2dULHVte0Ub4t-_aCqXF8A9DJu6yVrONogq1haX5sBU3ICOxO3lfMGdVo20hOJxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e836379e.mp4?token=LEQ4R8uVdtUTn5sGmMXEFjas4E8vAIDRp1Sh-_fcopXsEuBjRDqkZwGCHvB4OZ1co9Bch8f3XNZqVOSk5GImFP6W2PjDhYoIcd-hapjend6bCHIdbpVtLxfikq27YpFACYIl7798EiiFRtLeqoCWug2tAOm8Ruq3_S5h_eAKrjPCIp1876DTEqyi2OdP0rnpQWt1kIt6HX1N9t_WogYUC3UvsY9P9zhsmDVhZAf2P9R0jpiTMA0mT92YKvLaQ5kdHymoirOegAAEVBy9a2tQza2dULHVte0Ub4t-_aCqXF8A9DJu6yVrONogq1haX5sBU3ICOxO3lfMGdVo20hOJxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان شدید آلمان را درنوردید؛ یک کشته و چند مجروح
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان آلمانی دنبال کنید
👇
@AkhbareFori_DE</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/677270" target="_blank">📅 13:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آبفای تهران: برای تابستان آب داریم
بهنام بخشی، سخنگوی سازمان آب و فاضلاب استان تهران در
#گفتگو
با خبرفوری:
🔹
با وجود شش سال خشکسالی و کاهش ۳۰ درصدی بارندگی نسبت به میانگین بلندمدت، در حال حاضر منابع آب سطحی پاسخگوی نیاز تابستان است.
🔹
در صورت تداوم مدیریت مصرف، در پاییز و زمستان نیز با تنش آبی مواجه نخواهیم شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/677269" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔹
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/677268" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677265">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH6hKrjQmBlgVO-iWLxZFKfXQDIolO_144c18__dYgrGykHFZs6YeuYj6-H-p4ryAHai3PUC_cjRdmGjBTSzdOzOJtX-wtZTfa_RWA6c-rGi0wLQrk822HI17vLnTAi4V1vmeIwypMOVe5P3PDuVBmwcbL2ugfpGiRq5tOuRf_c1rvxyhzVGJ7CrUbmt3zivmw3UauuxgQhby84oV2QrVayCLqDf_0pFvCHGtVSHSY1fk0TKF74GU0l_Tjr6eVoS7nbjlBDFiTsQ_23-Ae-kcfiEsNZ80twOzOOXHZiEXxFGX-u77rjaX8ZdFUfESDgOlqcq9h7WrmjWfujTb28VWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
یکی از زیبایی‌های اربعین، همین عشق و پذیرایی بی‌منت مردم عراق است
▫️
با رعایت چند نکته ساده، میتوانیم قدردان محبتشان باشیم
▫️
به اندازه غذا برداریم، غذا را هدر ندهیم و قدر محبت کسانی که برای پذیرایی از ما زحمت می‌کشند را بدانیم.
🤍
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/677265" target="_blank">📅 13:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677264">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20563fa6a9.mp4?token=R3BVetR3F0L3TZi19t1hzuMWcEWdz4rnLJChuHxH4fpJESy3e_3iwI9w7falrQvR61FuKuszSsc6XgVvgOlgLwCQBu1FDwYYIe8RSCni1mo1u-AuRLOW7yHIryDVz1LfdGm35ohV9qCtdL8OwlZiMdfQnSfsl45CmZB3vIM9sT4rBQYfqS9XCTZh1wG6x0H988g3Eh5H37sZu7S7p02Sgb9bDkia3Wj23kvAJvYsPZR4XsshcLR4et2fJFmI800lcdbfjZZLNzKR_LLlS8n1rHejLpCjHFMx3TXdKprRgVaEnhdc7L_A91ck8RBGGSlzFsoYDcSYfCFKFlngyxDRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20563fa6a9.mp4?token=R3BVetR3F0L3TZi19t1hzuMWcEWdz4rnLJChuHxH4fpJESy3e_3iwI9w7falrQvR61FuKuszSsc6XgVvgOlgLwCQBu1FDwYYIe8RSCni1mo1u-AuRLOW7yHIryDVz1LfdGm35ohV9qCtdL8OwlZiMdfQnSfsl45CmZB3vIM9sT4rBQYfqS9XCTZh1wG6x0H988g3Eh5H37sZu7S7p02Sgb9bDkia3Wj23kvAJvYsPZR4XsshcLR4et2fJFmI800lcdbfjZZLNzKR_LLlS8n1rHejLpCjHFMx3TXdKprRgVaEnhdc7L_A91ck8RBGGSlzFsoYDcSYfCFKFlngyxDRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج پر دردسر علی دایی در بزرگداشت اکبر عبدی با هجوم مردم/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/677264" target="_blank">📅 13:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677261">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
خودربایی دختر جوان برای فرار از ازدواج اجباری
🔹
دختر ۳۲ ساله‌ای که خانواده‌اش مفقودی او را گزارش کرده بودند، سناریوی آدم‌ربایی را خودش طراحی کرده بود تا با دریافت ۵ میلیارد تومان و مقداری دلار از خانواده، به پسر مورد علاقه‌اش برسد.
🔹
تحقیقات پلیس تهران نشان داد ماجرا ساختگی بوده و انگیزه او، نارضایتی از رفتار خانواده و مخالفت با ازدواج تحمیلی بوده است. پرونده پس از روشن شدن حقیقت مختومه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/677261" target="_blank">📅 13:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677260">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b270a75bf.mp4?token=gCCV5t3j_S5qSbaEAFNcU1phnMwrUQepXYGpp2pr6pBqMgREJV8Y5vrPnOlKa3BIXh_rzNM73Obx0TKYJP0qNrCHgtNfPgks0W-3CdTqzKr0MBBmJsPriL5eM1w56OEagNUtcRdW3NDvVqufTqkqJ-MmRZv82xCxJPQ-KB3NZUlDz1o2_zmbCgUtFQpgeXWKDxX4SkqQnQLo8KT5W4JDrqUqP6ZeTdvr2ZHsofr671PBBqxL4eSlbh9AEVjcpIa5TIJ7VYL4qBzi3q-aj23qts-WsfIc9_WsiBxhnKVctOJFZC2tlRa1FG7eROMjLVlon7lFDExbMJx45maQYrs-IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b270a75bf.mp4?token=gCCV5t3j_S5qSbaEAFNcU1phnMwrUQepXYGpp2pr6pBqMgREJV8Y5vrPnOlKa3BIXh_rzNM73Obx0TKYJP0qNrCHgtNfPgks0W-3CdTqzKr0MBBmJsPriL5eM1w56OEagNUtcRdW3NDvVqufTqkqJ-MmRZv82xCxJPQ-KB3NZUlDz1o2_zmbCgUtFQpgeXWKDxX4SkqQnQLo8KT5W4JDrqUqP6ZeTdvr2ZHsofr671PBBqxL4eSlbh9AEVjcpIa5TIJ7VYL4qBzi3q-aj23qts-WsfIc9_WsiBxhnKVctOJFZC2tlRa1FG7eROMjLVlon7lFDExbMJx45maQYrs-IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظامیان اسپانیا مانع ورود مهاجران مراکشی به سئوتا می‌شوند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/677260" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677256">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGfcWRYmEChx9FOiMyzlEiVsPzKSG6PBstppquJA_W25x3_xVQa0sIkg3xTF7CXAbYA1KPEJmbxQJxaEVIWu1pfEd1vt_FELflCoxOGGWkCepEom68-zjiBPKWRu8RfX8OKataQBl9I0EqijhPX4naMqxLKrUGLjOcVtUBvmjVVj5sqpZt3wZjQ5V-z3wpB6JwBJmxIOUhT1YU1cw76XJUvYULkYgBfL2Rnpx-07ESqeDvG7sasxzB69mY7kpCic44PYGHsHPckqcVi8eH_B2xtppk9BS-KyWeRj-qFauKQ0jVm8xw3xQourNUpYejgbI87zMtMMvFPP0bAKHT7OFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIbXFQ1QnyN-WS8qCdNSYWG2Hap2fvnkDOAD-0bK0gEDDGePbpRoH35FBJq485oApX5MR1-ZmjBxMv0WMLOwdt1Z2pnVRr7-i6H0SdNLYQNNu6zN_66lp2u6gHOlzPKRvTkeqjM_ZxAAUgYUJ4LNKXUAJYwJ7rfRs_5JXIDGxvgUaxAvOB0YigGeWcnkIEjBKrQph0DbtuVXTS6y_0BuYLUX4IzHC27psHqFPhgH0TXvq20TfWeKz2UQxf3j_Tx7KLW4PP6FYeXDvu2Jh18akK7INElNw8GK1pSXB1RtdG0qOD6H69qhp3TSoAaHLwriTTNq6kia99Bep_IhK4hZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9WU4woSD30R13p5xl268nFJQwP1EGyEsybfzFJYEC2Kve9WImx7sJ4qOdHmzLlmCgjOpXeWiIOBF7BP6nhw5D9KUFwQGtW0pqoAUPQa54CKbtxDRHKhX6IBMmn_Dti1sz1YSJ3CbNw7TyF-4KYCH-tK-S7twSFHf2YLRr9Y5KtUm_bNJTbj_ybD_bqghUZGK0GTjqXUQBz6gAr6MyNeRaTgDvvx9cb4HBQKekF8VNmajzfobYJNAgZjNjcwerIbcVkf3kzc3brw_bHQHkFPpZCy8uSE9HLs1PzHtpK1bDf1WMtAhcX9-P2fj2nAton93TWRWZXOikjhzsQ1MDnhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuZMFkp6S0RxBT7506AW3dzgpLd6D-5nagr7FXGBMpL50YlZ2Clnr06-USI0aWCNRqgsuM-hFIDmCI_ABwxGjAuDuy3g9W0EsEobjsYD-5xEVJUHNut2xdqkGQq5EK3iP0zG1MTVsrnV5LkIRmgHuTpWReOh50xJzwpcag_qJRhLLwI1HXpREIAWmfXwWPI0UVcsRb_iINmXfT-Z9HWQGMce2eHdI2qIoiwd92BSpG8rEA7JAcxco5grtmBQQEmO0l18-nkm8m8o93rJFbZb_SHHDpClSP9nzSPHIyIC7GhUrMKDL79e2pqkRC5UJLQaQI2KX1XSco46Y-bC08uSSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اکثر افراد نوع اضطرابی که دارن رو نمی‌شناسن‌، با این پست نوع اضطرابی که دارین رو تشخیص بدین #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/677256" target="_blank">📅 13:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677255">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پلیس فتا: انتشار محتوای خشونت‌آمیز و تحریک‌کننده جرم است
رئیس پلیس فتا:
🔹
تولید، انتشار یا اشتراک محتوای تحریک‌کننده خشونت، تهدید، آموزش اعمال مجرمانه یا تشویش اذهان عمومی در فضای مجازی جرم بوده و با متخلفان طبق قانون برخورد خواهد شد.
🔹
شهروندان می‌توانند موارد مجرمانه را از طریق شماره
۰۹۶۳۸۰
به پلیس فتا گزارش کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/677255" target="_blank">📅 13:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677254">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdtTq3IQpVLfzRDODN6aAU8nDo2PirQw_m9eN6OCGd-eZTIwRlNRYQUgBy25PDoikjRdM7MQnpalvQLnt0TDPtpvsQkZPFxy_Rb7q_o1Q41Wq-VLZ5NYPRr92qOu7BK1dElmTqFhe71FqQ_i_91WuaYjzVTv8FR8PfFWRPlAxSLyXySe9lyb1ShVzzmLcFEn0z4GUf8tKq0cKbA-FJNo0aTlYs2SXqe-rGGVOG9fizMirkJU1haeu5sBPnkat4L5OLY0_J1qtalUD0eWdQlhPWmm3BPRaQ76y0mj0JF1aFuvoRbiFvjGu5cnSprbUhA6UdMuvGenf9XyxsDoqAhDrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه فاکس نیوز با انتشار نموداری جدید اعلام کرد که از موجودی ۲۳۳۰ موشک پاتریوت ایالات متحده پیش از جنگ با ایران، حدود دو سوم آن مصرف شده و ذخایر این سامانه پدافندی ارتش آمریکا به حدود ۸۰۰ موشک رسیده است
🔹
همچنین مطابق اطلاعات منتشر شده توسط فاکس نیوز، نیمی از ذخایر سامانه پدافندی تاد آمریکا نیز مصرف شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/677254" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677251">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-text">🌟
وزیر نیرو از اعجاز همدلی  می‌گوید...
🌟
روایتی از اعتماد و ایثار مردم است که در سکوت خانه‌ها شکل گرفت و روشنایی‌اش در سراسر ایران ماندگار شد....
#قرار_همدلی
|
#مدیریت_مصرف
|
#پویش_۲۵درجه_قرار_همدلی
#صنعت_برق_عرصه_تلاش_خدمت
@tavanironline
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/677251" target="_blank">📅 13:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677250">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/It97SkczRQ0xmpCgGFt61TZIcuWIkcJQYnvBlvZU57aF3PKqxRglC7rNTQwtOKcE1E0OX-srmHeBZWYV_pdvA_YvBk1pcOgGM60GUMX7sNdvWIebg701F1cnqM6jp9eSeK6i4pXTElMCbujIScqwhsikhbrf8FwPhjmendTOwfSqykWIsDWydBNdg9EbsZg9-Ji5Vsa45NmYPHFP73rK3ext8MCi66O77C5hlmYAhj2PXR6e5T3uGQCAZQyZjKlO4KAJ04IfPcHarAWzBs0mmci-4TB_2waJkSjM7Jvg4vG7tENJNrrYCDPijRNFUkDBnw3DSI3xQxCj6mlqg5nlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۱۰ مرداد ماه
🔹
در بازار طلای امروز با حرکت در محدوده‌ حساس قیمتی، شاهد افزایش قیمت طلای ۱۸ عیار و سکه امامی و بهار آزادی بودیم.
🔹
قیمت‌های اعلام‌شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/677250" target="_blank">📅 12:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677248">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8JFbkNmlQxc-FZwUwOU3k7Duno7bBdvtmeNtWOl4Pg_OOb6WqXr51t2wprf9X7qm25Qm_9JIviH_mQHDeojjpTMApwsMdR5cfY2weGMnqASNgD4g--tnAoKkoybmsfqKQI9inT1708FAJDjGAKr-PYvWrrnS7QahdnyyoNJYzVQUQAtJ1bUQqo4IU2Tm18ApFIV-Bb-qkdNBuAaMCzixRo2mUXhkeXeOU5QrkYFNFMrKaUfFI7TCXBBeYip96QPJPseFR_jIXPtJV-3Ns1x-xn0EzMFgr5o19yzgnQrp31Ubu1UaQx4xmv9f0lKzL2nQHXA4V9-yLROg0Mw2PFXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس: اگر به ایران ضربه‌ای زده بشه، کل منطقه و تاسیسات آن را به عصر حجر برمی‌گردانیم. به نفعتان هست که حماقت نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/677248" target="_blank">📅 12:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677247">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8jyEmA1BMFgskLB-xzZJOXp2u_RaOL2So7J7ZI0lNRZq_Qx3t0EtO0tCxRm4PqOaXzqENYc3Wr0YwY79BOP2FcYB2qTzoTIywKL9xfunFiRcRDezpkb9bAX1DiZIr1Jw2yYbuNcZbzAsCCud223ItjdpGSg8QzaJ4JovhfRwgXBUXV6QUQBMC-huzAwhJgxHhnQaOGwsJCXJR90FWAO-q4EdKAtgLYmItUeVRGyHzj7H3a3xr65g4JgHZ_V90nSqW83fRahcj6Id3cn4hgF3Tk3VQ92HP4JbMfLnR7u00T3tPYOAegXk2hgg-stZ8bBsmgAdbWg_Ez5PJkn5jK24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین پادشاه ایران در اروپا؛ سفر پرهزینه ناصرالدین‌شاه به فرنگ
عکسى تاریخی از اولین سفر ناصرالدین شاه قاجار به اروپا سال ۱۲۵۲
🔹
ناصرالدین‌شاه آن زمان ۴۳ سال داشت و بعدها دو بار دیگر نیز راهی فرنگ شد. علاقه او به سفرهای اروپایی آن‌قدر زیاد بود که تأمین هزینه سفرهای بعدی، با مخارج سنگین و دریافت وام‌های خارجی همراه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/677247" target="_blank">📅 12:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677246">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
پاکستان به ائتلاف دریایی عربستان پیوست
🔹
پاکستان به همراه ۱۳ کشور دیگر به ائتلاف دفاع دریایی به رهبری عربستان پیوست؛ ائتلافی با هدف تأمین امنیت دریای سرخ، باب‌المندب، خلیج عدن و حفاظت از کشتیرانی و زنجیره انرژی جهانی.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/677246" target="_blank">📅 12:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677245">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b23215cb0.mp4?token=f_CohG_vYiWJQ-f8hU5zVsoEVzRmqRFzmxGrx1HkW1WaliADZ3IRt1KU25UZOH3RLNFPAa2tFMhPjtTjnYdioW5w3lahsep0kChHNXRFKxXQfb1XTtHzlV_lu0UDn-ZzJxtUkhntB1HSNSGYL3GWQ2ZBfS2-0gZBdZClg0klPF8IQkhaDIDm2iHs8IW-QgEBJ_LIukQmZ6TrwszG3FhTQ_zVjh-ZCezeBtgHD00qLXKAZXm95xWJ69_Id1nNh_k9I8AsC8mrjfdBc1peypELjB0ispQM-MnW_mKWYnErDdjpNjWHFNIKOaG0BwrWE1ueU3nVA_0pGEkg6SQ0eGfxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b23215cb0.mp4?token=f_CohG_vYiWJQ-f8hU5zVsoEVzRmqRFzmxGrx1HkW1WaliADZ3IRt1KU25UZOH3RLNFPAa2tFMhPjtTjnYdioW5w3lahsep0kChHNXRFKxXQfb1XTtHzlV_lu0UDn-ZzJxtUkhntB1HSNSGYL3GWQ2ZBfS2-0gZBdZClg0klPF8IQkhaDIDm2iHs8IW-QgEBJ_LIukQmZ6TrwszG3FhTQ_zVjh-ZCezeBtgHD00qLXKAZXm95xWJ69_Id1nNh_k9I8AsC8mrjfdBc1peypELjB0ispQM-MnW_mKWYnErDdjpNjWHFNIKOaG0BwrWE1ueU3nVA_0pGEkg6SQ0eGfxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
اینجا همه یک عنوان دارند؛ «خادم حسین»
❤️
▫️
روایتی از مردمی که با عشق، خستگی راه را تحمل می‌کنند تا در بزرگ‌ترین اجتماع عاشقان حسینی، خادم باشند.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/677245" target="_blank">📅 12:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677244">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpmtmSAuMYubfzyi1oSIZjfG0OKSE5BzcBze6HpbB9E0OfWSvADfKXIlAO9gZww-BypEboNifW37UDYfPtcvtLfDkS4W5ZZq4n-wxs-L8Xlg6dX3EgjNx2j9UsJDZNnY86BUoO7lvb-AvYe6UzTEe3nz-zElb03twc7cfSIjvPXLTruL5xy350pZxeexuPzvTZWWF3zd3kEy3hBhsyW3avPeuP51cpUx-sLz8ydHG-zgWshTFcH0E7x8ocZbkDwA28sa7mhrOsNTUEsUVJF1xLNjmK-YrNq9yNXII-UYTP2dfgO9DszViZ1798l34gCoombn1vjAd58DJmsoFRjZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانشمندان راز کوررنگی را کشف کردند
🔹
دانشمندان ژاپنی کشف کرده‌اند که فقط چند تفاوت بسیار کوچک در چشم، می‌تواند باعث شود بعضی افراد رنگ‌های قرمز و سبز را متفاوت ببینند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/677244" target="_blank">📅 12:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677242">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huDka3T_rAoA_idcdyR1j4TEevgbkl10Vj08YFSgzINyk8z5bojW1YWZM05kGIjT-MtN6Bgm40X3E4sYEbqvLapin2Wiqt0WKzL9B5KlFITI3O9DNmtK0blk-jbzSqzn85XdPNQqCgms9fJhcGbDLlJ3PbRgUD6TAMD-ODyHqrf1I3RD2mAcqJhqXq06xUDWw3J-3BT_LRx4pwJqtgeeMgniZGMqJ6TuCLHKaiVszjvAaQq6Mzhea7UY2qjp9tRs5bgf9QX8n6uVJRLDOqjrJeZU4MDHHJ49AuvfEs6U4mQwab8TXIRoE_RPJHpZOUHxkPeMF5wTYNuRNhEsYH41Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید مدیرعامل هلدینگ خلیج‌فارس بر تسریع در اجرای پروژه‌های تأمین برق شرکت‌های آسیب‌دیده با مشارکت مپنا
محمد شریعتمداری، در نشست مشترک مدیران گروه صنایع پتروشیمی خلیج‌فارس با مدیران گروه صنعتی مپنا:
🔹
از نخستین روز پس از حمله به شرکت‌های زیرمجموعه هلدینگ، مسیرهای مختلف برای تأمین برق از منابع گوناگون با جدیت دنبال شده است تا روند تولید در کوتاه‌ترین زمان ممکن به شرایط پایدار بازگردد.
🔹
حفظ پایداری انرژی مجتمع‌های پتروشیمی در صدر برنامه‌های هلدینگ قرار دارد. تدوین جدول زمان‌بندی دقیق برای طراحی، اجرا، ساخت و بهره‌برداری از پروژه‌های نیروگاهی شرکت‌های آسیب‌دیده ضرورتی راهبردی است.
خلیل بهبهانی، مدیرعامل گروه صنعتی مپنا:
🔹
این مجموعه آماده برای ارائه برنامه عملیاتی و اجرای به‌موقع پروژه‌های نیروگاهی شرکت‌های آسیب‌دیده را دارد. با توجه‌ به جایگاه راهبردی گروه صنایع پتروشیمی خلیج‌فارس در اقتصاد کشور و نقش تعیین‌کننده آن در استمرار تولید و تأمین نیازهای کشور، مپنا مشارکت در اجرای پروژه‌های این هلدینگ را رسالتی ملی می‌داند و همه ظرفیت‌های فنی و اجرایی خود را برای تحقق این هدف به کار خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/677242" target="_blank">📅 12:14 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
