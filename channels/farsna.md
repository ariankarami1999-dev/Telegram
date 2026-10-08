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
<img src="https://cdn4.telesco.pe/file/rseRqp8ULYMRQ0XxW9xjCcamxCZz1gT9EF1dXN51FWiw3jZuBxSn3KGtcC9vRnOsLHfjVAl3i4PJD-vFzpbfEeKINU0B1ZnLlyMuaJWHxwKG_iIIs3yii6SBsqlRA1_iynGnEll5OUoQB5WypdUlATV0GEorTYNHcB1GGMnnGltmySGM857Zjsm009v2EfNIzNE4NDL3qHv0HZxe99AhUUfytI-Ssl9GcxqjeLU8xSI4lNVjx64g8pgzMiHB7wnIXy_MrsNxROjnCjsh38pb66wczkSUsCGH-wuDNEI7BcIcksvVQArHgAsq2f0O9UlrBiOa3yl1RTw6C6SbtqxGZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 01:09:45</div>
<hr>

<div class="tg-post" id="msg-467182">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEXIvPqik5biOtuVqNgL8QdCHwh-IEpPAkFZcoDvR2ruT-yYhe08RO2PKb7OZ42_z4HUYA-X3jUrdO83uK1FmUE8KqGfXKva8IuWDFtRe6yfxeRLtufv7NtXG2k09SE1SSTR4ESginnjRuBoqvSp7xxN4wYQ2E1By47_ReoNQ2D6x7LbCfm53Q1vg58d8pRNUeMuiXuw0HONx4NPIMNvtYNM6ruR2ffnj_bk5FDUf9k5u8-rTVmjWojcUkdWCCDEYwdRuKxQo7zl6rfkmh2P4rXV7OEyqy6UxwAdt0gskEnqWXeu8y5TfaSlzkfZ6zDBJJPl5txAwwp9WWoSNfjWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروغ ترامپ دربارهٔ «مذاکره با ایران» هم نتوانست بازار نفت را آرام کند
🔹
وعدهٔ دونالد ترامپ، رئیس‌جمهور تروریست آمریکا مبنی‌بر اینکه ایالات متحده پیش از انتخابات میان‌دوره‌ای حملات هوایی علیه ایران را از سر نخواهد گرفت، نتوانست از جهش شدید قیمت نفت جلوگیری کند.
🔹
همچنین ترامپ در شبکهٔ اجتماعی خود نوشته بود «گفت‌وگوهای سازنده با جمهوری اسلامی ایران» درحال است.
🔹
بااین‌حال، روز پنجشنبه بازار نفت پس از کاهش کوتاه‌مدت قیمت‌ها به سخنان ترامپ واکنش چندانی نشان نداد.
🔹
قیمت نفت خام برنت که در مقطعی به نزدیک ۱۰۶ دلار در هر بشکه رسیده بود، در پایان معاملات با ۴ درصد افزایش، روی ۱۰۴.۲۸ دلار بسته شد.
🔹
نفت خام آمریکا نیز معاملات روز را با ۳.۶ درصد افزایش و در قیمت ۹۱.۴۹ دلار به پایان رساند؛ این شاخص پیش‌تر تا نزدیکی ۹۳ دلار نیز افزایش یافته بود.
🔹
سایر قیمت‌های مهم انرژی نیز از پیام ترامپ تأثیر چندانی نگرفتند. معاملات آتی گازوئیل در بازار اروپا ۶ درصد جهش کرد و قیمت نفت گرمایشی که به‌عنوان شاخصی برای قیمت سوخت جت نیز مورد استفاده قرار می‌گیرد، بیش از ۵ درصد افزایش یافت.
@Farsna</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/farsna/467182" target="_blank">📅 01:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467179">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTEXKi-NKYfhYrxl0lL15HapCuH2jLLVPKbKRSo-quSvzB_nyfCzcumaiDTHmQuwHc7b9pW9aZdIyVDK6r-4ddjv93T4WnNgl_DlMmVkHDYxXvIhI9iXdiiauqcFXf-YgC_vqjP7SZmY87hL677K74UGoBXnptF7LYG2DWTyRG6H-j6ld7eBEi_OwZkCSLAHJ8JWPugAFokYvaPQuu9dqppYCX45VePawaDfIeqxwMlzoHXpG1rLajogRdY_X24e4GJmZJpDes2fwJz1erkf_Y2i-o4V6vfKASmZ7M4jEwkjY5StgTP5DHtmLEfIlS_yOG8ra3iRBjOhROeM8s1qdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NE8QzdAcav_WDJ4CBkCreMyNDWPDBoDdrJogDauhPzGDP24CesbXznH5mmQOQXqhle5WKDBhLmk2_TrdPAAreH1JVEi45PTEm4qOjcIk_fMoiAwJKcxMyi5xQvlxutw9D7FoXVViTlEr3jBsRfuPecs_DznwsNYgkjy6QbM1T7eiGmsyUS93C8t8u55y3KRgC4RwkFRWlFz1l7E64iUxeb2Gpxa_74y4-qvWRFFB6Ig5aYmp9_nvhxjltWWJFl0tAswTfpFiQO8000d8OQEv-sf9uasElVY_JMcGbY0YjfIjofvzeTnz96HenrGHW_JeC45NAWaxNO809U383fY_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frLoPoLamPrre75JWtKInY65LQMADv89ucUHgN5ZTmScMLOi396ok6tAkq9d39nxuZYfSkTU_CM4TYAIqyaYsXnrpxFWei0O2QVvjftx7TdwgL9GIAGq40wdw0yANFN8p5Bnt5i8u6Vdu_3BTncBt3vxbjE7v_jjTAdXyv1BKJVzqIUZu_BwrC1bbPaYvtS9qUZLl25ZKVb0R76PyQWCzosE0uXUK8w3UkpJDxF48Qw8juPmKGGsym3W5qcod4P6HW0blcL24KcLorCenMDLZ61rlXJb-yN95xJzcDvGwkhk-elEw9MBgA5aJ5eiGU-A7D5fgVPnyriz8y-cox1qTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
۱۰ خبر امیدآفرین در حوزه‌های اقتصادی، فرهنگی، علم و فناوری و زیرساخت‌های کشور
@Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/467179" target="_blank">📅 00:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467178">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک‌تایمز: شرکت‌های چینی برای عبور از تنگهٔ هرمز به ایران هزینه پرداخت کرده‌اند
🔹
ترامپ روز پنجشنبه نوشت که هیچ نفتی که از تنگهٔ هرمز عبور می‌کند، متعلق به ایران نیست.
🔹
با این حال نیویورک‌تایمز به نقل از افراد مطلع از گزارش‌های اطلاعاتی این ادعا را قابل بحث دانسته است.
🔹
این روزنامه نوشته ایران به برخی کشتی‌ها که هزینهٔ عبور پرداخت کرده‌اند یا احتمالاً حامل بخشی از نفت ایران هستند، اجازهٔ عبور می‌دهد.
🔹
مقام‌های فعلی و سابق آمریکایی همچنین می‌گویند ایران ناوگان نفتکش‌های موسوم به «ناوگان سایه» خود را در اختیار دارد.
🔹
طبق ادعای این روزنامهٔ آمریکایی، شرکت‌های چینی برای عبور از تنگهٔ هرمز به ایران هزینه پرداخت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/farsna/467178" target="_blank">📅 00:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467177">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bdb68dc1.mp4?token=PH6rJHiR7ce6PCYdIMTA3vVhTGVKsreLDDY9hwSNgSPBl3-3Zv6X0_zFxcU-5oIXfes9mxU_Fqb3MYKtOM-9Qk3_Zbo6hPJErSHcE1G78aPuJtlUb2GPcz1kwx3w9_TVSA6GzKHc7jYlozceYR-UB_EeS8JDjb2WKLEorvi5iOM1YT99fGfYEkXsj6SSm3Oxn_2iAuz-v5RdiS-U1bOHOQUbJq_b54FYHGrpJlVbYw8eXtpbdSaXg9qHltOUysP6re3_s07JlZOtV_uWwiM9kHPyRTWAIvR2LxmgO6H7OUqRF9V_9MbkkTS0S860zG4BCHImyoJUxDoqypyGQjkPSwp5HnFeEyBioNTMSitMHdjJ8kFQaSp28QS58Fhxq9rAAU1aOubhtpW7NR6c1K8uLW31R3p8MCUdEketXT7ZDgNyi_C28ldDnfhawfRx-wKw8qJfKRuzKn31zdYHkk8-xdDecOSOd6mazDd5mzHP_PMX_GC6qYb-aa3Juxz9dw9m-SJe7YtMvKu3QJ7gE97oAgUUoreGVGtJvJd3NRG_ZlxO_QWwAxhTvURCkmAAb6AlN7piMOikbIq16KGc2PGCGEMp4beXBkUOdeYleGYSDdFKVW5HKAG2tqsKSRY8CzSHom5RDO2cd1YhTEeTEsEmvbfLGSTe5dFq2IkIwHAteC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bdb68dc1.mp4?token=PH6rJHiR7ce6PCYdIMTA3vVhTGVKsreLDDY9hwSNgSPBl3-3Zv6X0_zFxcU-5oIXfes9mxU_Fqb3MYKtOM-9Qk3_Zbo6hPJErSHcE1G78aPuJtlUb2GPcz1kwx3w9_TVSA6GzKHc7jYlozceYR-UB_EeS8JDjb2WKLEorvi5iOM1YT99fGfYEkXsj6SSm3Oxn_2iAuz-v5RdiS-U1bOHOQUbJq_b54FYHGrpJlVbYw8eXtpbdSaXg9qHltOUysP6re3_s07JlZOtV_uWwiM9kHPyRTWAIvR2LxmgO6H7OUqRF9V_9MbkkTS0S860zG4BCHImyoJUxDoqypyGQjkPSwp5HnFeEyBioNTMSitMHdjJ8kFQaSp28QS58Fhxq9rAAU1aOubhtpW7NR6c1K8uLW31R3p8MCUdEketXT7ZDgNyi_C28ldDnfhawfRx-wKw8qJfKRuzKn31zdYHkk8-xdDecOSOd6mazDd5mzHP_PMX_GC6qYb-aa3Juxz9dw9m-SJe7YtMvKu3QJ7gE97oAgUUoreGVGtJvJd3NRG_ZlxO_QWwAxhTvURCkmAAb6AlN7piMOikbIq16KGc2PGCGEMp4beXBkUOdeYleGYSDdFKVW5HKAG2tqsKSRY8CzSHom5RDO2cd1YhTEeTEsEmvbfLGSTe5dFq2IkIwHAteC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عربستان برای جبران شکست‌های خود، به دروغ‌های رسانه‌ای رو آورد
🔹
سلطان سدح، خبرنگار جبههٔ مقاومت در یمن: عربستان برای جبران شکست‌های خود در برابر انصارالله، به‌دنبال رسیدن به پیروزی در رسانه‌هاست.
🔹
العربیه و الجزیره به‌طور گسترده دروغ‌های عربستان را پوشش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/467177" target="_blank">📅 00:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467176">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud94cgEwqHievbCOXutS-eCyhgL0DnRHs4wVHEM55pC8RKz4yRqXlGpH7JFkjJGW-uZih0Ye8Q1Ut7q_9b0tptithflpc1M15uVTMJmPsA5_av_ymdyKPh8AP1QWgBG3VgU6BB44QGUkkR39qArNNZ_PeMv5WtPThM3d8-qH_bpB5TBCmS4btDXq0noeDGAW2X1GvKvSDeZ7hi7ZGh6Y2OUXF6C1gfOvqZUO3yVWSlv1b62EqZYrZRPUil15cISXfLA1rrDgjTm9zAMIRkddZRe8-sQJUd9FZdn4n8bDZREnr00iOqFLtdN_q0wwkkMN4XVeuUCGR4bGrU7TcHJLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/467176" target="_blank">📅 00:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkFjOI_y1329ZFAAZWq9R59TkCNNJ_UMByDtGOfq2HLaiE5Nn4MggJoRmA0ggFcUpHELqMU-lfXv2qSV1DJs7XaGqPL2iX31vtdpNfa2jQX5g-MjtKtHqEwSdBBUNBO_pAOUD6UsTa3VFja5h1P4h_0sNp4r9d5lTvMi6ww7VTMC1BoRAaBWch9LSQYDkL2xeKaztjD9clK0Goyv0MM8S5Eu9tK1hgGyNBOXsjqae3bOHydU0q0gxveJJv9xW8piuZCkf_MhlOqDkWGkoPGkaNQWo558CoSwMhslT2Hsb-zftbhIu0TqOJrcLgJIPsD40fSfXFz2O1k50abWk71jbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyEKcLYDEE3aV-XGo8JosYcHJ6o_H08wvHMEAfA0EFPhEaCnX9oi5R4Wfr9wOutCEx6HW9vGRrT39rel81kXGBkgT3yllO2DIwCqG1Ys0nXdY9Ay-laLqQQf5BnXzU5UUJnd-TWyWN1KddU6p3ZpflLzu2j_FG0ghr5GfA8wI9eMkmC5qLhuCLctNv6AmiH-7o3K2iZccMJM8xLCr3aeNnNhv0myLazDiwoKrx04xq0i-8lsqqxPnvHQ6up03WUC_4vXs8Zrc6Gb69byBVpIeJRmv9RKdf_KVxgxoxMg4ZiUx0j2jdeeneJx5J83N7aUlunuPiKAo8wOg-yd3EiuXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lso_BI_f62ukq1m2LWP9pnGPwNqyOHkjDnHzb0iKhEWEkb7uOaRDRU-JsT3SyZPO4neT6uvtTO7PF-UI3Jq0JOx1d-ohNKSQEFxx-BMNpGA08KSrzg0P__O0ulrT4aF9M6gTt7N8ciktjJsBGg237zQ1Q47zcLG6_CZzbPOhG7rpA9qyNIhpZh0rQP28vt0JClOBalszEIBfawVrxC2C42wduV6c5I33aiCGcirSxo5j-4bZgYH8pJiIV5b-0kPiBdWf5qZwTtDRevBhppi5P2SH4KPsr_v2hexPDca1_dE1S5OVOILSjEgVJJz0tQN5MEsGy19XA-7r9qXTwCJNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/euebMo3VQVmOfsrI-xEt-y-TDxDlYZuNynlqdce_qRadtGEfrK-36SDYJizN9WJIswP15MO6LHJYjF8uPCge61FIwcTm3I14wTtTOzENtJ1l2nEnk1i2pMIrnHU9nKiUC4Pgvm783hh01eOTd1W8LErwDT1npuyLKdxVJiI-f-rhbDAv4ZKTjtO0PijQteFt28BtpuOoZtNJ1McfBldSaUOAoG8vvPFMD6MtTwwaXQ-uBDTy6_TSNCUynwB6gYvUtxpz6m09MyUeqDmVTw9dOer-VwIHatBsPyhsaRguT_GHst6_xGTJrKUOeFCj-C9SvvVo5l34FjlQbvFiEKaQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_G1o8DHh5xfB0Cd8xqEPeL2C-PIyRyZo21au1Bdjs2st9gjRoROLV9yx1jeRRX9Uz1S5dM-06Z1QVXAX_uRslxWrqbM5G-Kc91OSJOqvz-hojgzTCPGILLi1KILNFcScvYvq6mqMT8RlYNlX92OfEyTF0k__4BTcF65d0n4xQV4Hd67wr0sobPeIB5mlLzkOav11iFMvCIz_YnUBTtyAL6VxYpyR6LrXjA22UNFyV0kkGFidMAMNCzCLknmsd6MU87REbW6KBU0wTA_6WFiz71l16-yTIGT5ifhHHL7u78gcdDB1pKTyLQoQjZs8HHRlY3e2ZWqvgK6rLh-GAbSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLEUXUODzufpZxki6hQUauroEezVUcUpQkff2lcrX61fE_Sh07mHfSCuX3kxRb0Qu2mQDlxYgjmR41-oSMqt8xyuZ9OkyrX-1D3z3hMswBRXwL1NGVh592z9KAZi27vMSkGT8t8krOM00fjXPIVXAqCbSf2-ioIVzll4mm3X7rT0TXj50qHMZheRIcTwFkcKGlZ-cmULcwJlRkkVPcAE-2VfPKkShEWFwVEl70S-_Ll-lm3ZPGJ7tNXwzcxTdGA0A6RwSuKNfn8Hu3zeRNDw9D8R-iPCYh8gkYg4vs6Q5B1WyKIOi4y5wWrlSn7mY6jYQbekYR-_sIbJI4DrHVS7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMSp62xyAVHPTWCDoDMJjMCy_O7PP5c_t56AT1A7qBZZehAy0cnw-FPPsxo5xJs4vmivy0mui31WroC4PtimSik83C2dg90DvTF0t0FM1MpifHIZ70xBN7tofjVxiRFEjdu2fflRE_bPya-2tW7uasnFhxI40oZVplerMYETVkh6fOXI7b2g95xAzKCxUW_by2BgckNeVWUT0ybtEQ5ox8cvOL8PDaFN5DC2L63ePGYavIGPVaqfN299STBCOmW_nqVq6b0nLJDayJlD4ITurmc3LniTiMjid7-aDiB_5oVNsfOzf174Q8U7_legSiEmx0ImbqieHWXjMwvY1nmaPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GClfqqgXy4nlrszThD4FEQSjc45HPNMJPVv-Zu-LSxMx5TGwc9DMkvOOvGuwbS37kz-PnNxnNnwZHN5q4606IKVCxKurP3ei8ufLOA1HZjNdkuRw8ONTepAInClsBy7pAzIx7kxTVXnIvkUeHrUF_2qO2-Jse8XcJLEyEmAaLbNapv74iPXSslJsPHFOT5JIrqlRUN-8cIxCa_T--zPP0QQF-m7G0hSnCpqe4hgc_Y-E6PpwmK1jpHy3QRfGpmK7FR5fVKvAwRzNZztvXaaR8edXRxudu8JVd-5TdwjLtr2X1A3zA00vUNBmEdvt8Cckf54gh7kFk_7SEgzaLTMlkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جانفدایان میهن در همدان حضور خود را به رخ کشیدند
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/467168" target="_blank">📅 23:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de6b8ec4e.mp4?token=R_LO9MlyNyeFE5Oclmgw0b9U9Xs_fIuLRzLijKCFxgYq601XxxzLA4jN-WQgZMGjG2aDmLKnzYIFlziqtdBmUkC_XQ8Edq7x-uP7a4fs4aTdpnABYI0ogdLes8U03iWwDKa71pU82sV7UkLXu2F9rKvBJmIoWv0k7GoXMuqgr2_WUI1joojqlxDGyN-kthOomW3kMGnk0-9e35xIrZOk4CGpCqU3cgvJE6zPqWjWvw5t3QcdKqjEl0IL6Xj5FB1W09zR1qhbdYB1yuR9j3wrvxiY7xU9FFjb9SgX2iAeVdzBC2vfjGxySCauMb0YO3NpmMHVpRhnQ9E1n4N0PuLr20Ao0EXlTTxvfh_tIyx06i11XCK--9HFAonsJcjuzZzZFkymaWderKDuhjY2yoV369umeyaKympYIMB3VTKJI73wn9fOERNm6DuwGcpvVYy0cdIbT7CdmU17krP63Ors3hNboEslW3AfIYqjOMzT0RULeeqp0Hy713vbQuMjJxxzvM6ToZrlSKqCHD_oj9zq7alwRPC7NK71_ujwIM1WloJy61HvVFB6M8v8Y49qYk-3pCvyMi55FrLAyTwTY8k6TcJfPdk3yvRsDX7XtRcW--4LXU0q2vK8RnuSLTRRa-LLBVNPynaShHcGzQWiu0cnMmsT1I_f27al8jGrvsvE5sI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de6b8ec4e.mp4?token=R_LO9MlyNyeFE5Oclmgw0b9U9Xs_fIuLRzLijKCFxgYq601XxxzLA4jN-WQgZMGjG2aDmLKnzYIFlziqtdBmUkC_XQ8Edq7x-uP7a4fs4aTdpnABYI0ogdLes8U03iWwDKa71pU82sV7UkLXu2F9rKvBJmIoWv0k7GoXMuqgr2_WUI1joojqlxDGyN-kthOomW3kMGnk0-9e35xIrZOk4CGpCqU3cgvJE6zPqWjWvw5t3QcdKqjEl0IL6Xj5FB1W09zR1qhbdYB1yuR9j3wrvxiY7xU9FFjb9SgX2iAeVdzBC2vfjGxySCauMb0YO3NpmMHVpRhnQ9E1n4N0PuLr20Ao0EXlTTxvfh_tIyx06i11XCK--9HFAonsJcjuzZzZFkymaWderKDuhjY2yoV369umeyaKympYIMB3VTKJI73wn9fOERNm6DuwGcpvVYy0cdIbT7CdmU17krP63Ors3hNboEslW3AfIYqjOMzT0RULeeqp0Hy713vbQuMjJxxzvM6ToZrlSKqCHD_oj9zq7alwRPC7NK71_ujwIM1WloJy61HvVFB6M8v8Y49qYk-3pCvyMi55FrLAyTwTY8k6TcJfPdk3yvRsDX7XtRcW--4LXU0q2vK8RnuSLTRRa-LLBVNPynaShHcGzQWiu0cnMmsT1I_f27al8jGrvsvE5sI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«جانفدایان ترکمن» سوار بر اسب به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/467167" target="_blank">📅 23:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3acb54a5c3.mp4?token=e9ImvktiiWpqFa4tUoQAtm7OwAKpICMMuzskNJ8ZdLCPj25luuVPEwiVqZ1tBOE_69FcYJ31HZnSsrilscRwajtFT3Rvd1Gt4SsiDMND1z3FUUrL3hMAfevRH4usgS5ylHjA23TDj5XLqwx5D5wV8UOY7Ixg2tw9O2H9KTP09OqfODoHSe7uq0tFBrK8W6YoN5Lx6PqhzEEc5Qx5QVqhKCbOaOxGBhN07q9ocZM4I4gxV8IXvohWCqEjy80_580amfJcBcdzBsoKxUFo15qcuTe2lPzKw4xRKGwEyWqCWBUDh0Bm9_uFUvlJJ57O0th_dE-0Ei8uaMKC6ol3mrePYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3acb54a5c3.mp4?token=e9ImvktiiWpqFa4tUoQAtm7OwAKpICMMuzskNJ8ZdLCPj25luuVPEwiVqZ1tBOE_69FcYJ31HZnSsrilscRwajtFT3Rvd1Gt4SsiDMND1z3FUUrL3hMAfevRH4usgS5ylHjA23TDj5XLqwx5D5wV8UOY7Ixg2tw9O2H9KTP09OqfODoHSe7uq0tFBrK8W6YoN5Lx6PqhzEEc5Qx5QVqhKCbOaOxGBhN07q9ocZM4I4gxV8IXvohWCqEjy80_580amfJcBcdzBsoKxUFo15qcuTe2lPzKw4xRKGwEyWqCWBUDh0Bm9_uFUvlJJ57O0th_dE-0Ei8uaMKC6ol3mrePYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امشب موج ۲۲۲ میدان‌داری مردم باغیرت ایران بود
@Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/467166" target="_blank">📅 23:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807406b7e2.mp4?token=BUcHnB5HwEbNcHjP0bP8-ZmlAnjaK8L4Jd-latdSl_viIcQVtpk2b-577DmGdWyx88KcL4Rc3GlYIKBWo1wQNs_Y2epLoy90zUOMZPBaQui2k2XuhqzDkDfj9vTxFvqVS_6qUqU7rYuC2VQKiz9MuRlwmVGhko6BcbFPBvElvKHjzDNxFvJIV0iTDRB0u0AY3VQhs-uQN9iU2KCbP1Gj3PFgwGN1gyQXqbtfGSagRL2FjC_w1SDQ26BZWdJTqRq65YV42aBT1lAZSudDln_lMjZM8ivIyDv8MiLup8M5ZTXirjCaMP98Jn8QgX0ryS7fpHnDD4itHBChc6sNxHmj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807406b7e2.mp4?token=BUcHnB5HwEbNcHjP0bP8-ZmlAnjaK8L4Jd-latdSl_viIcQVtpk2b-577DmGdWyx88KcL4Rc3GlYIKBWo1wQNs_Y2epLoy90zUOMZPBaQui2k2XuhqzDkDfj9vTxFvqVS_6qUqU7rYuC2VQKiz9MuRlwmVGhko6BcbFPBvElvKHjzDNxFvJIV0iTDRB0u0AY3VQhs-uQN9iU2KCbP1Gj3PFgwGN1gyQXqbtfGSagRL2FjC_w1SDQ26BZWdJTqRq65YV42aBT1lAZSudDln_lMjZM8ivIyDv8MiLup8M5ZTXirjCaMP98Jn8QgX0ryS7fpHnDD4itHBChc6sNxHmj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان در دیدار با پوتین: با ادامۀ یک‌جانبه‌گرایی آمریکا دسترسی به صلح غیرممکن است
🔹
ما از شما به‌دلیل موضع‌تان در مورد وضعیت منطقه تشکر می‌کنیم.
🔹
روابط ایران و روسیه در تمام زمینه‌ها درحال گسترش است. @Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/467165" target="_blank">📅 23:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
نفتکش‌های متخلف روی مین‌های تنگۀ هرمز منفجر شدند
🔹
پیگیری خبرنگار امنیتی و دفاعی فارس از منابع موثق نظامی نشان می‌دهد دقایقی پیش چند انفجار سنگین در معبر جنوبی تنگه هرمز رخ داد که ناشی از اصابت نفتکش‌های متخلف با مین‌های منتشره در منطقه از دریا می‌باشد.
@Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/467164" target="_blank">📅 23:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467156">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSBHNhbdADV-TpiwE_qUBjh_yTX6onjQLHVTWKsrpHFK5cz0NsmbquUVEBzscyV9PnzbZzm0kKIta_77g5jd8CeAhQ_5yeruA8P7jKj0xz2aZ-w8hOE5CKYpFz_rW8gm5sdTaLBEYJJzsvARkJ7DK56stIS_h3OEgodd3Mkn0AvT9-Mo8wzBxztEj0nbDr1BsjdjQXrS2rhvJBQyVvQufk-Ik_859wareFV-W1fj7GznZis8B_BoUQmK5UpRoFiR6YLy6xBFJEzXnfs-FtjdSs0GppFvegndGSM5bFZrluSZvdpBU6_2qzDCuwq58T5udczh5dz4heFMLPsz8AQrPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3_otSk1GThD_X9j29IyyJlSYpMIP4X_Ci0-DaZKiHfz2u8H9zL5lkP3cVxQCkOv6vdgHSAhyFS8P8o1fsje57DUto2Ih5Ush0v_38y5rLml28kpvWFOQQbFPItL0jHeVN2YH1b-xeT9Pkn6rtAt1UNR7N8dU4srkIMivj6ma2MJPafCSY093YYArPpMCsWwxzu8aOFF4-KmiXmi_NbfnUVOMs98X0bRSNumaX3gFKSLj8sI4UBUq8DmBoR0gaTZjYozAlVqYVq_juLQDujQjtuTCVdw_faFl3DJ2rYy0b7cjiShkH_HtN_kuL5g0rou_3DBvYgQOIPew4gNRW9eCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8Jy74SPheB5ERqfVZWMw5jCLm9mgyvRNblT5aCUASXTlrDOv4fr4a_oj_C9FcVlSS2OdRt24DBmjsgUgAOeaHx_v8HuFo-T_HykRAsYk9IvffEF9E2EPVfhYKRJMoIdIHHxWUyb73f6ZpLEaQq6RpbOM7PmgVqIArJISsmx1y7yjvR-jfTt0QOuqCIUQR5vsANtxc6aJbbwEUa19FA_tKRvpD8gU_XTFeBTCXNAGU1MRcGnosp5-JKWOIwIMs5B4b5aVnVDN7uEv1g9NHl9rpb6v8CW7T3j26RQhsefo8_Gt7QwQtPaUIazvbRFuOgdK1NLeoAeag-fQ_aducpayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vqll832NV1WPylJVQEuCeRJr47eJHFufDKGEqd2t_cquyRXDUkL7qgA0TgvwgFCzYVFucMqWMA_gRj5fCOhT-OzaFhsP1oLx7dBaWY9ZJ_hBYHrjhHasQ3W39ILKt10WX6D4r06GbI2EPdAm01j1cxPxzzHfLHYzhjH46nHIVWGX00j4dAFTJPylnTXlOD-VTgZRqykqescp-NPDYFJAOd-G9KNgAkDzstv_JbFXJCKFBY_ljhiysSdtiFyuzuCvLyKEsh2-AzwKgoal2cNmzy-P7U5sM32cOH-bLFdlt9IHxVSPtFkZmKZgVbWEIGrRAmb4NbFgfO0VxRrqu5zGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gf26qXIaFC8SLLPpYdk3fdLmXzuQ-wcToJkas2kGLhUD76ZZbEmjen0koVefUZeOzaxX2WdDOUiq3ZtN1AA_A-Pv_wl168v_QnaD6pK3OZaXiwk4QjylN2T_L03oiY1xW9QETCU6h5d8OrqfQXhIL2cWJq34W8_G612nGsr0eJwM_OrFVkcKwdDBQQZHIFHyZkvRJG7zGHjZIKu8Sj0tx_YB0UYLZbXNG-VHkhYQKwunXLT-3p192mRWGqJDBZsduDI5mES4Jk7Kl7fWws1cFY0yzmbaJKxoW0g4iauCZzhH85RId3FfftU8TfhbIHrMEpSAZPYFrlBPdf1cmf710A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RULsaaB3M_FPaN5oQHmfT5e-V9CIAkralk6-zGy0rW29OvEwUJW3Q0QmEsQxAHs3K6QIAMAAxvYXODRjPhnMRkYFdClKoxFOUEFUtaPswL7jGhPUTIaBRmvjDCavkg3mhu3vKMzgTzexKlE8oDsdnei5zPRpHpt9DDA050YA-79ysLHh9A097_qtq8g2PqS2uBxz0REYx6fSruiJESVc1SNHfx1OGkdUnIDgxgcp95MHkMRW_-56dpKHZ5KJbaPEQde7Q9031u9_a2nriCy16PqSP3xosW9AnhOwCT4CJCnJ73pkB_ShMWdBBEsT9bFp_B9rvUrqjcZ7DS6Cjs_9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWDotosqG8RJeSTeJ0axdsci__4UFIPFsh7EXYfcqgacvL6aiVLhpGET1bnrT4yvLMVuRQGTKSnPfHxqq3xJhNxRqxwr4_A43po_LT56bLEy_aquAbbD6YD8b2oY4MRF3Husfs_WMcdV2xwakdjVphEShNUZGKeFKYq3YZxISNyxVGlpKWMDz2Ye88tPtblfblsU1hMIh1WdpLQhm_GGWaBApc9m4XuexfRaAvoTWBZaeWb7_8oYFwTfjmtH1AnxW9sKFLUl36N7hfNI-H52xgbbEYVW8lu5rL7r5nRBlL1y9dN7LIHhisqUGtrO_XVA1CjZ_BF8xzZABO47Q3yEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNwVtj6tWhuJwfckTI6dcklodhDWMgoDYhy2YVvfEyyXWhzdqrDYje3qFjnYV4HPxtB2GxkxTqQHqrhKjwtuED3YhYR3_x6tMK9orF7JgbuKHFER6tpZTA92S4aGAdV_ebymIh7vPVa0OIPO4oOCU4bpY8n-E6Hm3kI8SjgaeWcjIesP89paG5ETlpCUj1Z3iT0UgaOrTLlrLZ7JVsnLFq_LPw0KsQ22PMgNQtWNePBzX5hwlRXkjF5j9IWSmOJM7hfAkWu3bHIYMN7khjeVr-jWQy4LYBC5hnJR6idVyaiWQsOav4P2IcYdZkUSK6pl6nFMBis_KTNUnlGEoJH75g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نبرد استقلال و تراکتور به نفع پرسپولیس تمام شد!
⚽️
تراکتور ۱ - ۱ استقلال @Farsna</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/467156" target="_blank">📅 23:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467155">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f79235cc3.mp4?token=WuTgLo-PbsU-OsijxOOQJUSElAuLHW6e4m8C-qq5Vr8xdnDpF0Kcbg9oS7yy7-Dc_zZLb7v1DS4GhPeS9jw6gyWTEParVWGVPU6iO3AAZwegmJToUaM0bf0iW0-o4MtW2mYNAQLROgNRHjgflp8YxJyTS8IxFvAIM5iOmvg95vEbI3JsBzDiR-f3DZwwG9Q1gFGXJnQRAxDD9aERNsgQ1qrDcdGLWfbFBMISBel6fplwT5aDGqRo4LC8lx8iJU49iy8pVrpxcLaaA7s9YgCvIkA3srj8VdMMOj5nTEXOBZXL0B26XuZm0ffM0UMVkpWXXvaBCbJ1faynME6GWczovJAuN_bSeoPjKdNmgk-EJLPo6LVjA7cq9dcGsReiu_CfML2uCqVEAyF3Y0kfB6S2cltlZPNtunjtmERSAP8DQN4QTCLNreqlTZsaKy8qX4dc2eYX6EEoF_UXvJ-ku5gjRdAjLHrbLvWorXwPBCUmz0upHn9jl-aazpAadqsdEPlcaQkqnveCvRuWzBjcZySAcmt-7d351uFpB7GbwYpXHbWWiJ-QTK-zjpGQsbkOZJJrytyWHp_Yoi0N9q-0dhTG0AGgKiURVRuNwfl_bSgKCH_rINDUIIPYMr4ZLoILeVuBT4FRPBqF84I2ZDSwNE1HHEIBjQ13uaNz0BwGdtoTSf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f79235cc3.mp4?token=WuTgLo-PbsU-OsijxOOQJUSElAuLHW6e4m8C-qq5Vr8xdnDpF0Kcbg9oS7yy7-Dc_zZLb7v1DS4GhPeS9jw6gyWTEParVWGVPU6iO3AAZwegmJToUaM0bf0iW0-o4MtW2mYNAQLROgNRHjgflp8YxJyTS8IxFvAIM5iOmvg95vEbI3JsBzDiR-f3DZwwG9Q1gFGXJnQRAxDD9aERNsgQ1qrDcdGLWfbFBMISBel6fplwT5aDGqRo4LC8lx8iJU49iy8pVrpxcLaaA7s9YgCvIkA3srj8VdMMOj5nTEXOBZXL0B26XuZm0ffM0UMVkpWXXvaBCbJ1faynME6GWczovJAuN_bSeoPjKdNmgk-EJLPo6LVjA7cq9dcGsReiu_CfML2uCqVEAyF3Y0kfB6S2cltlZPNtunjtmERSAP8DQN4QTCLNreqlTZsaKy8qX4dc2eYX6EEoF_UXvJ-ku5gjRdAjLHrbLvWorXwPBCUmz0upHn9jl-aazpAadqsdEPlcaQkqnveCvRuWzBjcZySAcmt-7d351uFpB7GbwYpXHbWWiJ-QTK-zjpGQsbkOZJJrytyWHp_Yoi0N9q-0dhTG0AGgKiURVRuNwfl_bSgKCH_rINDUIIPYMr4ZLoILeVuBT4FRPBqF84I2ZDSwNE1HHEIBjQ13uaNz0BwGdtoTSf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکاوران نیروی زمینی سپاه در مرزهای غربی خطاب به دشمن: پا در این خاک بگذارید، خاکسترتان را به باد خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/467155" target="_blank">📅 23:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467154">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/684171b317.mp4?token=DS9Ol2ZjPRP-1BHKBWt251MdHF6urVKoptMHcxWBHfs1Rj5VxzsePwjnYM43vulmHDRtcfbBQWR16hqIRgFIjQxfaswd__ouiFXpOeweOYheL6uFt65vi2LIN6TdwiS2edluvE5pgG5Z_Tf7dB0sX5YsyEBjQ6A45-yAw-QWvAJ2pYS_TDQfg4o7M9dCtyV-IibUYuC4iBBmXwGcaL31U0tL3tFY6hbnEpVi4v6Gl0BDShA5MnbtLSWYqEHhLU-xYphNAi5hSdIto_BiORaWhv-6xLConQ0azklLDyQWXdNIJQt4GSgZJK5JqZ9HVweQ6VMw7AgF8Jlu4Q5MajO6mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/684171b317.mp4?token=DS9Ol2ZjPRP-1BHKBWt251MdHF6urVKoptMHcxWBHfs1Rj5VxzsePwjnYM43vulmHDRtcfbBQWR16hqIRgFIjQxfaswd__ouiFXpOeweOYheL6uFt65vi2LIN6TdwiS2edluvE5pgG5Z_Tf7dB0sX5YsyEBjQ6A45-yAw-QWvAJ2pYS_TDQfg4o7M9dCtyV-IibUYuC4iBBmXwGcaL31U0tL3tFY6hbnEpVi4v6Gl0BDShA5MnbtLSWYqEHhLU-xYphNAi5hSdIto_BiORaWhv-6xLConQ0azklLDyQWXdNIJQt4GSgZJK5JqZ9HVweQ6VMw7AgF8Jlu4Q5MajO6mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای انفجار در مقر گروهک‌های تروریستی در اربیل خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/467154" target="_blank">📅 23:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467153">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای انفجار در مقر گروهک‌های تروریستی در اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/467153" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467152">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6A1r5XtMZhD-JC6pBZSerGo_bxriC11pSIZCCUnXPG0TCKrLjty5_i5e5KK4GL8VyGRerzo2NfW12FGJqM4undeBTIsINvOUpkI17CM_H2kZSOKFOWLI2PCk0qo4MGWCJBH3Z_md48q8QQUGqpLNZ_q47M3d2_DktZ0dbQCM8fL5x_98fUKzKRd6uWNXpxx949H-oTVuIQ-pdB2SoM1PdVL7gTMml-b25Ym1-IzM4ofrR8hAP8tWk8LgOCr-EC3YTtF2vngJV1NHmAwWNBxYGQnJM2Q2F0VBYqjMH-u6aJjax96A37kGiTYEObZfgYbasUQolVDmmJFBBEC6UPvRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخالفت عراق با تحویل ۴ هزار داعشی سوری به الجولانی
🔹
مشاور امنیت ملی عراق: با درخواست دولت الجولانی برای تحویل حدود ۴ هزار زندانی داعشی که تابعیت سوری دارند، مخالفت کردیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467152" target="_blank">📅 22:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467151">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شهادت مامور فراجا در حملۀ تروریستی در فاریاب کرمان
🔹
سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش درپی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب، به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467151" target="_blank">📅 22:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467150">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9547fda8b2.mp4?token=DO_0myEsxpf7AIbzpf4h6b0RRTeoof7H6uMhL8ghEr64XwwDGDgapGIAALvuCuSGchWm_e-poBoCn36ybp8uwIds_bPxfam_ELOJ5b7VWxuBhTRWrN4ZdoRfUCEQz-nLEpHSoEGwKBOAwsYyWpOsZVA0cletH5f0HdXuuwYPW29BbGKhouJDSzFK4r6ysl3GvggcR32nmlabeIMgQR6m0KUvXXfXaY6QJu5j_MLNIboFAE5DoNrqUNVEIK9htwh5p0mNrhmiIOcVUr3jxfulY0TJb0iK3wDLDZ7OAHue_3pbcXaoX2hyn1YJ2byq2K4SeWofVPzv1WlIO_hije3Ukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9547fda8b2.mp4?token=DO_0myEsxpf7AIbzpf4h6b0RRTeoof7H6uMhL8ghEr64XwwDGDgapGIAALvuCuSGchWm_e-poBoCn36ybp8uwIds_bPxfam_ELOJ5b7VWxuBhTRWrN4ZdoRfUCEQz-nLEpHSoEGwKBOAwsYyWpOsZVA0cletH5f0HdXuuwYPW29BbGKhouJDSzFK4r6ysl3GvggcR32nmlabeIMgQR6m0KUvXXfXaY6QJu5j_MLNIboFAE5DoNrqUNVEIK9htwh5p0mNrhmiIOcVUr3jxfulY0TJb0iK3wDLDZ7OAHue_3pbcXaoX2hyn1YJ2byq2K4SeWofVPzv1WlIO_hije3Ukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین در دیدار با پزشکیان: بهترین آرزوها را ازطرف من به آیت‌الله مجتبی خامنه‌ای منتقل کنید
🔹
روابط مسکو و تهران در مسیری مثبت درحال توسعه است و روسیه آماده است هر کاری انجام دهد تا به ایران در بهبود وضعیت فعلی در خاورمیانه کمک کند. @Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/467150" target="_blank">📅 22:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467149">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333dc748c5.mp4?token=jEPDn8wZXUST1_TT05gF-Hbao_YtNFVqW7WMJ80VsX0-05fJgawsv8rcaY5Tm2g7dsos13nxIs6j5lOMpy_6EfI0TsRNNTPwg1hPR8sGo0FiEjzlpQeFPIqEBm9rDI_XXlqX5IT6dLPNwv2XbEjYPrlWTBqUNhBfQw76eezHAMXcceQpQX5vCmsXckZ5UBAKLKkwFyqpTFmO7gE9WawyV98KOLHPkg6LLKcO9aPlyJmoQ7X-ziulOz8m7okXNfdLJ6NH38hA61c2ox3GxgDRn5SNbwt6RAcSIui_0qK_5g8PWJBFHxlNdodlB1rYaRhceTNe4KXoKf0VPM8WwcL_Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333dc748c5.mp4?token=jEPDn8wZXUST1_TT05gF-Hbao_YtNFVqW7WMJ80VsX0-05fJgawsv8rcaY5Tm2g7dsos13nxIs6j5lOMpy_6EfI0TsRNNTPwg1hPR8sGo0FiEjzlpQeFPIqEBm9rDI_XXlqX5IT6dLPNwv2XbEjYPrlWTBqUNhBfQw76eezHAMXcceQpQX5vCmsXckZ5UBAKLKkwFyqpTFmO7gE9WawyV98KOLHPkg6LLKcO9aPlyJmoQ7X-ziulOz8m7okXNfdLJ6NH38hA61c2ox3GxgDRn5SNbwt6RAcSIui_0qK_5g8PWJBFHxlNdodlB1rYaRhceTNe4KXoKf0VPM8WwcL_Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: تولید تسلیحات ما در طول جنگ ۲.۵ برابر قبل جنگ شد
🔹
ما از قبل جایگزین‌های امن برای مکان‌های تولید را درنظر گرفته بودیم و حتی یک روز هم تجهیز و تولید برای نیروهای مسلح قطع نشد. @Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/467149" target="_blank">📅 22:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467148">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff8ba101e.mp4?token=A_tSSalKIusDoZYkA9GPHLvGUlmoYJtaIIHhl6YUCHnHUWYozdN7m-402f2M7_-2QRh1y9jKAwaAvp56YUnGiUlAxaolbPM1rs0oxkdansjmbv2QkB2cez6ESM_DQva0ThSnjzgqbZzSr0ztR9JTsRGuIgqlXXf1pU7HW37apFqcao3qV1Mw_6w5_JnM_VZckxnFymN9m96edTBqwCMnb8XTd2OWbPLasaHHE013m5yWJ8xqkIUxPc0YSP8RHFcEXRBSJ_3yTcvKh2p_E2x1HxVbXK1QkBLT9FXwDGdTMnzczLRlZua0HLIOcwxjhLwdyrzY1ALM8pnGlI0xVpOGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff8ba101e.mp4?token=A_tSSalKIusDoZYkA9GPHLvGUlmoYJtaIIHhl6YUCHnHUWYozdN7m-402f2M7_-2QRh1y9jKAwaAvp56YUnGiUlAxaolbPM1rs0oxkdansjmbv2QkB2cez6ESM_DQva0ThSnjzgqbZzSr0ztR9JTsRGuIgqlXXf1pU7HW37apFqcao3qV1Mw_6w5_JnM_VZckxnFymN9m96edTBqwCMnb8XTd2OWbPLasaHHE013m5yWJ8xqkIUxPc0YSP8RHFcEXRBSJ_3yTcvKh2p_E2x1HxVbXK1QkBLT9FXwDGdTMnzczLRlZua0HLIOcwxjhLwdyrzY1ALM8pnGlI0xVpOGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: تولید تسلیحات ما در طول جنگ ۲.۵ برابر قبل جنگ شد
🔹
ما از قبل جایگزین‌های امن برای مکان‌های تولید را درنظر گرفته بودیم و حتی یک روز هم تجهیز و تولید برای نیروهای مسلح قطع نشد.
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/467148" target="_blank">📅 22:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467147">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63730388b2.mp4?token=aFdMx4fAYyjY7baRfKFMcvm-nbCY_jH-j4wJ5ZW0oNyR1SEzKsl-hQfhqTJsBb_lMmLkzLW5ZoOVx0yRrBgS0qmXczzayzogNLPztlJJTir5-LuWuqvikIOOE0JCTYE3ehLbF8Iok06U7f1wWZZO4t9eBtxxkob2QcvWo7RO4bwoBqWNDUURR7J5wriC9Sz1sHTMsprz-0Rdmf5RUv3qZc1dBmdrDGHusjNJKunD2EI-GkuM0pk_A6q1kei3k68zKvRm2qEhuyThbV9wUY_L3BEOhMweyvIpxLrH9wrWt7hd-Q_-XwMr9rcWDTXFn57jXCBuDvOXSRSIVy4TFa2y2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63730388b2.mp4?token=aFdMx4fAYyjY7baRfKFMcvm-nbCY_jH-j4wJ5ZW0oNyR1SEzKsl-hQfhqTJsBb_lMmLkzLW5ZoOVx0yRrBgS0qmXczzayzogNLPztlJJTir5-LuWuqvikIOOE0JCTYE3ehLbF8Iok06U7f1wWZZO4t9eBtxxkob2QcvWo7RO4bwoBqWNDUURR7J5wriC9Sz1sHTMsprz-0Rdmf5RUv3qZc1dBmdrDGHusjNJKunD2EI-GkuM0pk_A6q1kei3k68zKvRm2qEhuyThbV9wUY_L3BEOhMweyvIpxLrH9wrWt7hd-Q_-XwMr9rcWDTXFn57jXCBuDvOXSRSIVy4TFa2y2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرۀ سعید جلیلی از جلسات با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/467147" target="_blank">📅 22:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467146">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa2e248cde.mp4?token=CN-v2euw4EYMxvC_eX8t93Yw-0etq6CdKHMEms9op1QzZbUX4abLsAc4CTm6UkS9ocqgLP4e2rW_j3EWFVWTXPoZWBtoMUa_DAjGNuLaC9aMHff_H8nxsUE586IC0gmOP86KhDFZdlQs1mLcHyeTULBJEZbw3JXYg66VRqg8n5wLd1mFelC3tkHXrKXQFBtCjc5QVmrJe3vAEw8dXzTJ5i3OTLtLAFo9fngTzaQEUnlQ8y-lCMsA06Ytl-VpgP3yXFv-_FSNh0vuIBdaTs0Mvz-L2sztb1-0MPpm9VJyWqC9y6r_ocV1Y_40UrqcDIKEVBlbBXmoUtKKfLY8gHrVWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa2e248cde.mp4?token=CN-v2euw4EYMxvC_eX8t93Yw-0etq6CdKHMEms9op1QzZbUX4abLsAc4CTm6UkS9ocqgLP4e2rW_j3EWFVWTXPoZWBtoMUa_DAjGNuLaC9aMHff_H8nxsUE586IC0gmOP86KhDFZdlQs1mLcHyeTULBJEZbw3JXYg66VRqg8n5wLd1mFelC3tkHXrKXQFBtCjc5QVmrJe3vAEw8dXzTJ5i3OTLtLAFo9fngTzaQEUnlQ8y-lCMsA06Ytl-VpgP3yXFv-_FSNh0vuIBdaTs0Mvz-L2sztb1-0MPpm9VJyWqC9y6r_ocV1Y_40UrqcDIKEVBlbBXmoUtKKfLY8gHrVWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن تصاویری از درگیری‌های زمینی با مزدوران سعودی منتشر کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/467146" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467145">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حملهٔ مسلحانه به مینی‌بوس حامل کارکنان نزاجا در نیکشهر
🔹
روابط‌عمومی لشکر ۸۸ زرهی نزاجا: ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، مورد حملهٔ مسلحانه قرار گرفت.
🔹
در این درگیری یک نفر به‌نام محمدرضا اوکاتی…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467145" target="_blank">📅 22:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467144">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNNOnWBfu1yWaAACI158Jr37Kvmq3iQyT3KdHIdXXW_tW_OayJEE3H_hDjUnoJA-sQr4WJSd_Eij_xztqTs6YmS2ew9gQq8gdgDB389Ulx0fg4XsaZEyZMluVGwDY7eh2BBHA8xRI3WcVUfObyHTGUtTFw2Gm-C1QZ5WGgnRYyDJDlT76ZzUO01HXSd-3f2wDxedBi-dokmfO33m3X5a-4PtFbO61pRbT3exiy4ikOW7jlGdHfJYBKWvyQVZBC7CWxYNHaPbJTjrEULprgYvbB9GuJCqZMyJC004iJ2UPT3Pn5gAvNwekIIX4ARM8dTSGSp628f2pV-Zpsuubaw7ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان و پوتین در ترکمنستان باهم دیدار کردند  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/467144" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqMP6K6UmaEseDohALcbHp3qN1nslnx6vSv_PSziSiQ87McxAfJAUVwmYuLdaP7YEk8R08UMU3OxPznbF5u04GFfDyHNLpQElDi81FtOkxZM8UGCrsuhU7aO2vm9LyzwgfZDVv26dE_XiloQD4ZxtjLxWYY69eKpwJyItQ61R7oJr3tW3InV5mwR2lLLzr5wE13evsxmhnU5dlYcL2sBjAvC3sawGQpiUoLW5tx4WubnoDvpwyEOoLTUAwAcizir147dq15RSIYW3-zIY-hTDVWsWf--3A-6JB-6MOrspYZCk-VD3wZCBH698CsC9ir_hlPIJIYrIn4iZO9IIIERsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند از تراکتور اخراج شد!
⚽️
با اعلام باشگاه تراکتور بیرانوند به دلیل مصاحبه علیه زنوزی، مدیرعامل این باشگاه بعد از بازی با استقلال از این تیم کنار گذاشته شد.
🔸
بیرانوند در مصاحبۀ خود پس‌از بازی با استقلال گفته بود: از مدیرعامل تراکتور می‌خواهم به‌جای حاشيه سازی برای دیگران، اول داخل تیم خودمان را درست کند و حقوق بازیکنان را پرداخت کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467143" target="_blank">📅 21:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXFGJ0BsPcoFaKdwPe0meUzm03oIOpV5-_S9738hey-BNLZzKWB6ABjDF8zUgb-9grxrnwyo9fQhoB8oZse3hERk7L7AnmM4SYtiW6RliYB4yEMN5UKOIc1dTrEfIlFiPowzq89GdY3_V4K2cpjnmaH22c3c9tfwJyZ2pCp5GenK13HpLRsf8nnpTmfxLxhYvJEdFAAAbyZDsYzRUdlkvhoyB_ZRX9lyWkHsig2ShPyLjQaSMZ4PL1iS8Ugoq3_vhC3RAquzW5TiDuDyClWnV7Yaa54054bPDh-0xyfs_MTSdmK-6ZlOWv2KYd3-clakegRNBaDaedMLK8wKG7irHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتین با پزشکیان دیدار می‌کند
🔹
دستیار رئیس‌جمهور روسیه: ولادیمیر پوتین در جریان سفر خود به ترکمنستان در ۹ اکتبر با رئیس‌جمهور ایران، دیدار خواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/467142" target="_blank">📅 21:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bd1e81bb.mp4?token=PprmEj2dp9Yhj-gYaIbdDV7jtI_AIn4-B4Fs4aDQTRAwkCHiyHpMvYTKTei5zDRsD-W29JBy6AN4SXR_ZqIXv3QaWPrk5UHdufNakrgOjNCjrIlJ_F7k8v1caN60B1sG-dZr4DhRdD82ht7BdL2mIJ-qXcNBfVvPNFicy5kW6N4fyBKmfyy5LTS8_RhAi20BT0R1HwEuZ7vcjzYmxnCkMqOHSwEGb0XIF5hVs1EC6uxFGVOuED8CyCe7cvp_-WuIQ2ahgvapnEsaCVAdoqW7awDc0qt4QqmQ3lpud2WTtvWgVI_oFdvqIX1GYWeyvSc0Btjydjg5BHYQikjFHlFayip2NSCU8ErvDAP6VFh0xzsNfgjOus4LxmgALHFVEl1r_-G-iUdth2DQSIeRbK6_YceYyhDPXffuxuTfcorBZTF6mbPs42nyIpIJLI17ZRBSHMdItbT_bYUI1XpzYMAaMV50ntPKzn6oQab0XGB6Q4VG445kcBhKqa20b1aBSdp-Uv3WD6RPqyC23RGtmEvkz4nEiT1RKXdKIwsOSTriQnfZX3b4I-bhL9iEsAbBCWpwFVD0WwOHPCD6lCSQ3etOVKWC6bevBTmVO86kZvfs2M4rJeoAI8iwQaW4xtRzWzHA3qwXxRzPtID0HejvgbollobhjPXa-6CyoxPXS7Wqw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bd1e81bb.mp4?token=PprmEj2dp9Yhj-gYaIbdDV7jtI_AIn4-B4Fs4aDQTRAwkCHiyHpMvYTKTei5zDRsD-W29JBy6AN4SXR_ZqIXv3QaWPrk5UHdufNakrgOjNCjrIlJ_F7k8v1caN60B1sG-dZr4DhRdD82ht7BdL2mIJ-qXcNBfVvPNFicy5kW6N4fyBKmfyy5LTS8_RhAi20BT0R1HwEuZ7vcjzYmxnCkMqOHSwEGb0XIF5hVs1EC6uxFGVOuED8CyCe7cvp_-WuIQ2ahgvapnEsaCVAdoqW7awDc0qt4QqmQ3lpud2WTtvWgVI_oFdvqIX1GYWeyvSc0Btjydjg5BHYQikjFHlFayip2NSCU8ErvDAP6VFh0xzsNfgjOus4LxmgALHFVEl1r_-G-iUdth2DQSIeRbK6_YceYyhDPXffuxuTfcorBZTF6mbPs42nyIpIJLI17ZRBSHMdItbT_bYUI1XpzYMAaMV50ntPKzn6oQab0XGB6Q4VG445kcBhKqa20b1aBSdp-Uv3WD6RPqyC23RGtmEvkz4nEiT1RKXdKIwsOSTriQnfZX3b4I-bhL9iEsAbBCWpwFVD0WwOHPCD6lCSQ3etOVKWC6bevBTmVO86kZvfs2M4rJeoAI8iwQaW4xtRzWzHA3qwXxRzPtID0HejvgbollobhjPXa-6CyoxPXS7Wqw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
ورود پزشکیان به ترکمنستان
🔹
رئیس‌جمهور به منظور شرکت در ۲ اجلاس سران کشورهای مشترک‌المنافع و اجلاس محیطی زیستی دریای خزر، به ترکمنستان سفر کرده است. @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/467141" target="_blank">📅 21:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBHW6Ayic2Ilj7nMV88iiU-g1Q-D6H6_ybeOLB9-BVJX5fOwOELE2P7qUryATowcufoZd-wzAWWwQOc59sGREn6HOVXWLR56rrh48FT1SjPr3vYWoWWFTvzrvCXrmlgHxuYHu5myJTNgGmsWA9W8aCzcTDZ6e9gpXyqfVhbPm47U_MpwVNKZsJhu-6Y1xc8QKLmb78Wubao8X4VsmVCDQ8R4PZfr_J-aqJBIxsLRqJkN7opXAWfa7voI83NiPzEfV2X4jl3bVqu7G-Q84HlK0kC_-lF0zuP23MWJxaHO4yqm8KPH3FP-nAKZ-Xn_JjTNZdlG0V-3aj2PymvY17k-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر ایزدی: رزمندگان سپاه و ارتش برای دفاع از تنگه هرمز آمادگی کامل دارند
🔹
جانشین فرمانده‌کل سپاه: تنگه هرمز متعلق به ملت ایران است و فرزندان این آب‌وخاک در نیروی زمینی، نیروی دریایی و نیروی هوافضای سپاه، در کنار برادران خود در ارتش جمهوری اسلامی ایران،…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/467140" target="_blank">📅 21:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b81e58d9f.mp4?token=dfBwuPvLagby6MGk71dytB9m8HQYTabf0TPyFQSEH8wNQvOU6kaJEyB0TPIt3rv8C6KTXlnhuy6b-lSGiAdyVGbqlxYnTmio4INOrf-j-aiEBadF_KOvabgeRiDlXeIxj4Mmi4fmyetRM8TXgXvhtDS0PMXJzwTD98jaLczYDxo8OUwp600jSwYtxySZv_x4W0iL1jYzP_SyNerCkjzw5X7LbJkYFVCFe8k8lW3TjzvIyjLwfVCNpZehMVa6wIDb17yylUXzANvC-_l3BWMQveAaUcN6GFcQsu501Uc_pVeuB7gj0s8UpTmvPyaFiNECeGtnUQDO3Af2Kb2LU9JqKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b81e58d9f.mp4?token=dfBwuPvLagby6MGk71dytB9m8HQYTabf0TPyFQSEH8wNQvOU6kaJEyB0TPIt3rv8C6KTXlnhuy6b-lSGiAdyVGbqlxYnTmio4INOrf-j-aiEBadF_KOvabgeRiDlXeIxj4Mmi4fmyetRM8TXgXvhtDS0PMXJzwTD98jaLczYDxo8OUwp600jSwYtxySZv_x4W0iL1jYzP_SyNerCkjzw5X7LbJkYFVCFe8k8lW3TjzvIyjLwfVCNpZehMVa6wIDb17yylUXzANvC-_l3BWMQveAaUcN6GFcQsu501Uc_pVeuB7gj0s8UpTmvPyaFiNECeGtnUQDO3Af2Kb2LU9JqKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جولانی دورترین گل لیگ را زد
⚽️
امیرحسین جولانی بازیکن تیم فولاد، در جریان بازی امروز تیمش از فاصله‌ای از زمین خودی توپ را وارد دروازۀ مس شهربابک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/467139" target="_blank">📅 21:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌ رهبر انقلاب: استفاده از فناوری‌ها و هوش‌مصنوعی نقش مهمّی در کیفیت مأموریّت‌های فراجا دارد
🔹
تقویّت همه‌جانبۀ نیروهای حافظ امنیّت از جنبه‌های مختلف انسانی، سخت‌افزاری و نرم‌افزاری خصوصاً ارتقاء فنّاوری‌ها از جمله استفادۀ هدفمند از هوش مصنوعی در تحلیل داده‌ها…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467138" target="_blank">📅 21:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌ رهبر انقلاب: ممکن است خیلی از اوقات زحمات و فداکاری‌های حافظان امنیّت، نزدِ برخی افراد عادّی‌انگاری شود و همین مظلومیّت و گمنامی است که اجر آنان را در پیشگاه الهی افزون می‌سازد.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467137" target="_blank">📅 20:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌ رهبر انقلاب: نیروهای فراجا با رفتار اعتمادآفرین خود می‌توانند اعتماد مردم را به این نهاد ارزشمند ارتقاء ببخشند
🔹
ملّت مظلوم و مقتدر ایران، قدردان زحمات و تلاش‌های بی‌وقفة خدمتگزاران به امنیّت کشور هستند و متقابلاً نیروهای فراجا که همانند ارتش و سپاه از عمق…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/467136" target="_blank">📅 20:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌‌ ‌رهبر انقلاب: امنیت کشور، مرهون رشادت و شجاعت نیروهای فداکار فراجا است
🔹
امنیّت، از مهمترین نعمات الهی است و برقراری آن در نقاط مختلف ایران عزیز، از شهرهای بزرگ تا جزئی‌ترین واحدهای جمعیّتی در روستاها و محلّه‌ها، از مرزبانی‌های سخت در شرایط دشوار آب و هوایی…</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/467135" target="_blank">📅 20:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467134">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رهبر انقلاب: نشانه‌های تأثیر پررنگ فراجا در جنگ‌های اخیر آشکارتر شد
🔹
نقش پررنگ فراجا در سطوح مختلف از رده‌های فرماندهی و ستادی تا کلانتری‌ها و پاسگاه‌ها برای تأمین امنیّت در سال‌های اخیر برجستگی بیشتری یافته است و نشانه‌های این تأثیر در جنگ‌های تحمیلی دوّم…</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/467134" target="_blank">📅 20:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467133">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رهبر انقلاب: نشانه‌های تأثیر پررنگ فراجا در جنگ‌های اخیر آشکارتر شد
🔹
نقش پررنگ فراجا در سطوح مختلف از رده‌های فرماندهی و ستادی تا کلانتری‌ها و پاسگاه‌ها برای تأمین امنیّت در سال‌های اخیر برجستگی بیشتری یافته است و نشانه‌های این تأثیر در جنگ‌های تحمیلی دوّم و سوّم آشکار‌تر شد.
🔹
تمرکز و اصرار دشمن جنایتکار امریکایی-صهیونی برای ضربه زدن به رده‌های مختلف فراجا از بالاترین سطوح تا سرپنجه‌های آن نیز اهمیّت این نهاد را بیش از پیش عیان نمود. امّا این تلاش مذبوحانه و ضربات خباثت‌آلود به ارکان نظم و امنیّت جامعه که مشابهی برای آن در طول تاریخ موجود نیست، باعث نشد تا نیروهای شجاع فراجا ذرّه‌ای از مأموریت خود کوتاه بیایند و حتّی در خیابان‌ها و خودروها، همان نقش و وظایفی که در اَمکنه و مقرهای خود ایفا می‌کردند را به انجام رساندند.
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/467133" target="_blank">📅 20:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467132">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قطعی برق برخی مناطق تهران درپی وزش باد شدید
🔹
درپی وزش باد شدید و وقوع طوفان در شهر تهران، برق برخی مناطق پایتخت قطع شد.
🔹
عملیات رفع خاموشی در مناطق آسیب‌دیده درحال انجام است. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/467132" target="_blank">📅 20:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467131">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgoOp0wE9uI3RjgkddOjAnSbgcelL_TW2b8M3YPMgYCcKPd9Q70fH-6p9knXAdduhbPUIO0Ku8C7SO4MkWHngA2Kve488FfwAx0WUKYb3QCt2ZgYuRAH0TGg2Hfc-OHFKflJu3ZddpVUmcm9FKQA6KK38lVEHD2yWASO5Iv-L2jCLoFJFSiR7ioygGLmpJ-Uq_YUrIF2POARYbmYqc3_dPlNqJh6WgS-uZ20UHLX7NMvVF0Xq-ChTNhZ5OQ7Ui31dKjEW429QHm-_hYdpEnYd-FtpRYO7djMoG-E9Jh6xm5wncmmNbJa-kh1W4jm8qOxcmOqA9sW9Sx5Ym4v46ottg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر ایزدی: رزمندگان سپاه و ارتش برای دفاع از تنگه هرمز آمادگی کامل دارند
🔹
جانشین فرمانده‌کل سپاه: تنگه هرمز متعلق به ملت ایران است و فرزندان این آب‌وخاک در نیروی زمینی، نیروی دریایی و نیروی هوافضای سپاه، در کنار برادران خود در ارتش جمهوری اسلامی ایران، همچون ید واحد وظیفه حراست و دفاع از این منطقه را بر عهده دارند.
🔹
تلفیق توانمندی‌های رزمندگان در جزایر و آب‌های خلیج فارس و تنگه هرمز، شرایط اطمینان‌بخشی را ایجاد کرده است و امیدواریم این آمادگی‌ها روزبه‌روز تقویت شود و صیانت مقتدرانه از منافع و حقوق ملت ایران در این منطقه تداوم داشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/467131" target="_blank">📅 20:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467130">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombankmellat | بانک ملت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRwHTUmJT8hPRwSKHF-FyHW8Mq73BGQXc_ALsBn30HXPUtGxaVIbMhaBC3pDhr6gsXbH9b4CXMO7hFSTt7Mca7U1DwKKYLr-ZPMglDTS6D-Cf5HP_4s-1FYY4NtDiuwwHlSiDVKyT32-U9EgIZa9Spk7SmD4HXMnzo_abLBVcSgyhyTiWg9zb0WYQQXHyv7X1flztXskV8gf_DhMjVFiZA_2QN_wf5Q9D9AV04FqBfugbrMWVKcQjRuXqmHpfFHH7VfeEUwlaT9AuLEmcarMv4osV0GMo9Q8oeUerw94z9V4kiAA1Yw-VWX9E2iSR7aA4IQ8dE0ee4GLZSSujWmQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌روز رسانی سامانه های بانك ملت و قطعی موقت خدمات غیرحضوری از ساعت ۲۳ پنج شنبه ۱۶ مهرماه
🔹
در راستای اجرای به‌روز رسانی های فنی با هدف افزایش کیفیت سرویس های بانکی، خدمات غیرحضوری بانک ملت، از ساعت ۲۳:۰۰ روز پنج شنبه ۱۴۰۵/۰۷/۱۶ تا حداکثر ۸ بامداد روز جمعه ۱۴۰۵/۰۷/۱۷ موقتاً غیرفعال خواهد بود.
🔹
در بازه زمانی اعلام شده تا اجرای عملیات به‌روز رسانی، خدمات کارت، همراه بانک، بانکداری اینترنتی، بانکداری باز، دیما و دیگر خدمات غیرحضوری غیرفعال است.
🔹
بانک ملت از صبر و شکیبائی مشتریان گرامی در زمان اعلام شده تا برقراری کامل خدمات قدردانی می نماید.
@mellatbankiran</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/467130" target="_blank">📅 20:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467129">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSSHarSjGG8iJRz8fuF0miCJFZgSIRnkLczsRORNnPg8wexlh0WIoCFawV7pHVLJreqj_uDu-zZZkFJSGEOtMQonjbPBippxgEGxEbaFo_GjdFfS1MnNKeQc6rnlbh5KdbueVKWe4TSeizH85WMbdmA1arBe5GU_DFEjS08m9h8wUzU3zqPWMjJjZ04DnnvlhPdZy6n7QTC8QTdYxpmyBet53lZv864w-JIqOTSihZxyc0KSnhGgOT2t0HQEH-d2w7XcuOwrGes5sueDOQQV3Ns3E71CJHrNIUAbSN2DVutcQ8rg-cseRSp4NQvViQtW7i5BY0xba0AXMbHrbeEFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
برندگان کمپین خرید کارت هدیه بانک شهر معرفی شدند
⬅️
کمپین خرید کارت هدیه بانک شهر با استقبال گسترده مخاطبان به پایان رسید و برندگان این کمپین معرفی شدند.
⬅️
به گزارش روابط عمومی بانک شهر، در این کمپین، امکان خرید کارت هدیه از طریق شعب و پیشخوان‌های شهرنت بانک و همچنین خرید کارت هدیه دیجیتال از طریق برنامک آپ برای شهروندان و مشتریان شبکه بانکی فراهم شده بود.
⬅️
در پایان این کمپین، ۱۰۰۰ جایزه نقدی ۳۰ میلیون ریالی به خریداران کارت هدیه از تمامی بسترهای حضوری و غیرحضوری بانک، ۴۰۰ جایزه نقدی ۱۰۰ میلیون ریالی و همچنین ۵ دستگاه تلفن همراه پرچمدار به خریداران کارت هدیه دیجیتال از طریق برنامک «آپ» اختصاص یافت.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/467129" target="_blank">📅 20:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467128">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/467128" target="_blank">📅 20:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467127">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا نام ۶ فرد، ۲۷ شرکت و ۲۲ کشتی را در فهرست تحریم‌های ضدایرانی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/467127" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467125">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAJ4ar12sTU-UCV7AsEydDlQNoGctZXH2mXz--2Ln32r0P_qd9kFK-XTNsVxtfoXB6a-l5WTf5VhUGE76s-urAF4GTxIE_uKuCjmxcgg-xbSrPV0hAgz4fFkbt6yP9awXrxkC4kqcHAd12xQDCy2I_rIyFJorvKa_WiqSERm090EAI38TmOKa82VbHcVKwV7VPes0BfdU3s1IDIXDvGLE-7Wo3dnIqm-FY-rnByLHsp_WTHfyXMX1lgil2XqNssnt2H-VZFwwVUTEuGSyAqJA9POmVmpRhdW_rrw7QUmChr_aAFsuxwccHhyujK9WDz6EWIFVzaNn464GsTaT2wFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcTVH-oBWwmu82fWSrQDSIDUEzlAmPorWBAiojc6iHA3KROx8xmmlbnWLqkLn3lI5FxMbnprfSm25r5C-ktdFyJ3S6HABaiqUDRbi-dlhhJ7rcfGUQo3VcG2lcJw8YtB1ntPEL2KFr8_L8fKUGj1JrN19Gn6idc2RQ6oSmjqU9-8_bfAqKR0TH1St5W-ynyFhGeW5eskaUw5U11TXJbFgFbbknQhqcc3ocy-8jE1yQNR9KIUrMKtocJ7c92fH8PHZd8aRNR3g_XAonfNV_TfocWk2JKDkeEZ3BzKm2Comfc8rMyDY2esFXbqg_KrAE-eORd7a8a2nF7pbS-dt8Zcmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شادی پس‌از گل ستارۀ سپاهان با یاد امام رضا(ع)
⚽️
مهدی لیموچی وینگر سپاهان پس‌از گلزنی در دیدار امروز مقابل فجر سپاسی، ذکر «یا امام رضا(ع)» را روی پیراهن خود به نمایش گذاشت.
⚽️
این دیدار با برتری ۶ بر ۱ سپاهان به پایان رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/467125" target="_blank">📅 20:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467124">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mONzxtaWt1eCVVIyl6hUJwTxnnT2gFeFOUK3VGRpljeighOhRTM7ymzTvwFPitBINKCUDFC89DxfpyddGEl0rxhcImJYFWiqRwQBwu1AcQ0Soiz6sku-Xb0cmg9eAUHxXtBB0BXNmlWrkQpwCfvpmnn7cvrpX48OvuVrJul-lEozlqeIDZ95L8CpwUS_hsisZWx3VGtccQTMgtG03TGO_a6B6TKS1pI9osX_4Q8VQ3TLFkDvOWQipk_vJat2JLPo2NATDddhLE7k3NpBI0mcWpep5HNGqJm6mpsfdE-mTGX-zwyAW6oHrdO7zO_W9FEMJbu8k0TPROtEcfFgNMrAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست جدید وزارت نفت: تلاش می‌کنیم به مطلوب‌ترین شیوه نفت صادر کنیم
🔹
حمید بورد در گفت‌وگو با فارس: صنعت نفت در حال حاضر در یک جنگ تمام عیار اقتصادی است و تلاش می‌کنیم، مسیرهای پیروزی در این جنگ را مشابه گذشته ادامه دهیم.
🔹
تمام ساختار نفت پای کار است تا…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/467124" target="_blank">📅 20:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467123">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSnUFsfu0QEWrqRQf3Aboi6f4ibBwbM0QDyTmlfsbxWxJWZ6OTY8MAfek8jWlr_Fa2SE3LVgi1a9Aq3TBbpS-5SmoatHFqw4TlXT12RfRcxsdNwrSOi55ySVLxgsrFgP9ZJKReB2AbmuzQ5yvgDcFAluo6TMI8JjT5iRk050HjjkzodPN8aujHMjK3mc5WaSg9wiID54floWCujs--d2zaEWx8uvwVfiFLG6QqPz2dzEdGaSiA2UjJWr1kipU1s1tyBs1pAS27VtKIEUCfzWCY1EQJNZMCFtNgf_1BCU_nqMr0UZya_bpbvic6ONe03HKiTEph-UWLy34rg46raI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبرد استقلال و تراکتور به نفع پرسپولیس تمام شد!
⚽️
تراکتور ۱ - ۱ استقلال @Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/467123" target="_blank">📅 20:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467121">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
پیام فرمانده معظّم کل قوا به‌ مناسبت هفته نیروی انتظامی تا دقایقی دیگر منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/467121" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467119">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXE9EXgZH0aWL6AvbYf2O3QnL5RDqremx8W2A5nrZN9eZ1KuSEjwvOfh2bsLRiUf0k7QtXwKHSBDu2w7pLB7jqk31q1t5qD3eShmApOr76-IPZN87HKbUXVOAh2KGTVc06hu9WH7w1WYwTZiZlSWAvNnApDlV2YgHm6SMht_9oDqFAodWsp9y4jjLrJm2oIgibqg7dnCY7QTILipTq0153IB7n82DU2W_5uq0iPiWVK2XcKXryEjK6MJzyC24Cma_YyDaZBrlJ2m3BOlCCEsT6dzNKkiAgnuCV9DAesN0T8ry5vr9PrSxarohVNfsZixF9ychzD6askmezrjJ8xICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: همه باید به‌جای «هوش مصنوعی» بگویند «هوش برتر»
🔹
از این به بعد، در همه اسناد آمریکا و امیدوارم در اسناد سراسر جهان، به‌جای واژه «هوش مصنوعی» (AI) از واژه بسیار دقیق‌تر «هوش برتر» (SI) استفاده خواهد شد. ببینیم این اصطلاح جا می‌افتد یا نه؛ خیلی بهتر…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467119" target="_blank">📅 20:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467118">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سلطان شکنجۀ ایران
🔹
داستان پرویز ثابتی از آنجا شروع شد که دنبال کار می‌گشت و افکار ناجوری هم داشت. سال ۱۳۳۵ که ساواک تأسیس شد و او از عده‌ای از اطرافیانش درباره یک سری کارهای مخفی شنید و ۲ سال بعد فهمید که دلش می‌خواهد ساواکی شود تا بتواند کارهای متفاوت انجام…</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/467118" target="_blank">📅 19:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467117">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">قطعی برق برخی مناطق تهران درپی وزش باد شدید
🔹
درپی وزش باد شدید و وقوع طوفان در شهر تهران، برق برخی مناطق پایتخت قطع شد.
🔹
عملیات رفع خاموشی در مناطق آسیب‌دیده درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/467117" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467116">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6L5AvSiEp9Lg8rOtnWvVEP7YPyQ-MsNXVf7QBDQrtPg4MAltZfCcOwfCuvh1vsfuL6LRVezSxBTBMjUyRGVFX7KjHaRp1CgGeRhl-ptIMi0Xc_0qtztXXbSSrkKN7NwF5yFjCZZ4IDnNIB82XEoPDq135jY5AjGqXcStKPhfsq5iUNOkRlE7cXxnNeWOvSPd-ZzU7hZSrZ3-gHbWSOrS5qkHTAPXvvn0vquBnRRa4fBNSpVU3W_N6GKdqd3EuH4mbfdgL13yfmRdW3mq-ZzU8zb8vfY2c3hhiQ-Lh6GPAw6Kw7oyTJsrYzHIphiUD8t_t_VFhYNic8ADcJqWpJdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع: به فرودگاه‌های عربستان حمله کردیم
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد شامگاه امروز پنجشنبه فرودگاه ملک خالد در ریاض با دو موشک کروز و فرودگاه نجران و پایگاه هوایی خمیس مشیط هم با موشک‌های بالستیک مورد اصابت دقیق و مستقیم قرار گرفت.
🔸
سرتیپ سریع تصریح کرد که در نتیجه این حملات موشکی، پروازها در دو فرودگاه مذکور متوقف شد و خسارت‌هایی به پایگاه خمیس مشیط وارد آمد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/467116" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467113">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmrlQt5xHQ-G3qN7bwAlhd36Y1YGTIv6b93YO3fFSrnE27F-x7KFJOmMkL941XUptVyQQLkfrIQMz8T9xQPVlJhQyWrZZfDEuk81DFf2YaP44Q2TmAF6zGu-ShiC1rv8E7PImrZ5ZOI0nhFoSlLiCBSkL-u3iWxNLcEoTRA_0ryN-pz3CaZllViOO3JNAWdwKKHIsUwC_e_UPFCD23lljaKCPMiZ1uJUi_bC7NyqhCxtiKVtNdY5Y2f5r13IOuRDSbQ7r0K0D0I4rT3-QyqyyVLaMS2mJaGAZG9VeKTwzUQNQN_zbq11AouLvf0LeKAW7RKBJKJWkHpdzeu5AUoPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXoXm6nTnfNvlIwbkD-g6Zkyyn8s4mHl8ZKpFW48Xgt8gNFXZSSUHYusmDUOUaQ9XBud5jayZT8ZFAQSdiIH5cf7nWnwkln2TZvDsjRZZPN2YbwjiRHM4Dw8z78M6MTY7Ckune4osvYdXwMx5eH1fVDmm_hrxxjjcIrNjySIasdiP3poC3JLCXGl6v_322YEUEk1t9fpcTytAylwYl2GMWqj5k4OjXwAuEdRcK7wTNrA5Nsg0Uo8Fr477B3efN7f89o9eH7WqA5hAXFm-viIx9dIbaihtfGxuxVUpqC0JjcjeqMbETtyPvqruXJbqqnCnQ5aDrPBhc0Fr2qck4ojTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IW8km67MTBwM9yHz9ObXQUz3tY9N7VlSgeZmRhrIab4g8a8LVcMzchRa8dI_6Z0L2rJ8MedBW-_8JEMV3dLByrjAITHbMk5uGAHem5X-rw5OKtRQplP-rpwQr9EpEFUA1rHRxuGQIy0_jary8n47fZh-OiNynUJikrZmTWxSJkU-bProAjk68noEkkEhdiWOeKSuXKjDVRQ1nSxIz-Hfy_pIC-hLGNkQ3S4K2QC_H45qeS9vcJlZz4h4DLV-yqxYQOT2QcGjemKDT-Hin6QIB8q-J9XVcQnVVY22jhetcwc4FTxMRHZ8Pdj38ZIqlclXvqkNkunryaW55f5WVPFsXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: در سفر به ترکمنستان با سران کشورها دربارهٔ مسئلهٔ خزر که با خطر مواجه است، گفت‌وگو خواهیم کرد.
🔹
‌رئیس‌جمهور پیش‌از سفر به ترکمنستان: خزر سرمایه‌ای برای نسل‌های آینده و محیط زیست ماست که اگر از بین برود، مشکلات بسیار زیادی برای همه کشورهایی که در…</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/467113" target="_blank">📅 19:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467112">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فرمانده‌کل سپاه:  تنگه هرمز، خط قرمز راهبردی ایران است
🔹
هیچ قدرت فرامنطقه‌ای حق تهدید، حضور سلطه‌گرانه و دخالت در تنگه هرمز و خلیج فارس را ندارد. @Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/467112" target="_blank">📅 19:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJy3SnkqIjF_DVILuB6qbHchlnwhJpUwxqq0H4frh5FG8ZIkHX5hUkEP3BhfA7z1ODzme2WroXE1Kvb-mqgbHuCaSal-BNOY_NebvSmD7-YrXrwgq0F10tZNEy3hF9C5Oiyap9w4k-wZyhZtyRfBv1BXDssqQ5VT3dYAn_RiOiHZLzwXMWohdIKLmvPX-3pqeeocJIwOCc-un4fnFSA87GjBOurVRWnG8agee8O5AdNAnYj6nUIGrAyIt2SzO83dNjH9Tr_eyFvldNjHzo-vEoFiEEi7nG9s-JBMqBYuc7Rf74ZCu-vFfVdkpFppU3dlgWVE7TU1bOh3yaW4XOJgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرمانده‌کل سپاه:  تنگه هرمز، خط قرمز راهبردی ایران است
🔹
هیچ قدرت فرامنطقه‌ای حق تهدید، حضور سلطه‌گرانه و دخالت در تنگه هرمز و خلیج فارس را ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/467111" target="_blank">📅 19:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467108">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7262159e9.mp4?token=tzdKgOd4ammatsgrQ1y8GDQw16g_4LmVXi7X4MRorF07GzxjxbVT-ZRwVTesGgisBYUiypKp3tpwccUxXI2KL4lvIbGiy-zKIRCSHlqhFg5fYgzjmCC2aN6OpqVmnQkyywABkZmFTuCn1ttVQjH-63OTN9qC5bcEdStNFF4yqYI9EWOFcE3YwX8H2TyRj_ZB8uOAv0S5_KFMixBxmmwnpeYYzkSfaR4GO6CVxGXhsyB6H3i3QTwz7nQVcNRdATUgxMSzTzJm9T_IUnS89m9iGYN7p_HkchkQayZHvlll3qW6GuN3Fd9-igxzBGyl9krPbicy7Nj5RhDoYqq4VWFNTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7262159e9.mp4?token=tzdKgOd4ammatsgrQ1y8GDQw16g_4LmVXi7X4MRorF07GzxjxbVT-ZRwVTesGgisBYUiypKp3tpwccUxXI2KL4lvIbGiy-zKIRCSHlqhFg5fYgzjmCC2aN6OpqVmnQkyywABkZmFTuCn1ttVQjH-63OTN9qC5bcEdStNFF4yqYI9EWOFcE3YwX8H2TyRj_ZB8uOAv0S5_KFMixBxmmwnpeYYzkSfaR4GO6CVxGXhsyB6H3i3QTwz7nQVcNRdATUgxMSzTzJm9T_IUnS89m9iGYN7p_HkchkQayZHvlll3qW6GuN3Fd9-igxzBGyl9krPbicy7Nj5RhDoYqq4VWFNTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درگیری شدید بین شهرک‌نشینان صهیونیست و نیروهای امنیتی اسرائیل در قدس اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/467108" target="_blank">📅 19:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467107">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805fc7f33c.mp4?token=Mk8wdZ8_A8HN42DgQevWCHycVVSt4IiGm2tlM_rHez6mO7-oh3d7KYdfNQboubZjshs7danIZMvmEJRoN4y3o-yYf_Ad91h6uxImDavyv0uZkna_tSEF4s5UKsrOoZiCXa9FI71JvvInk7no6_Dnj1MqJ0ou5kltWF7djjXLc3dgbVCc6vxOdXblh1TFNu7jx9ZE1CgQBME3ywBRv5XMjPK3JPjWDbFm5KgbCt8hwnHsnVyLe6CGgVtB7pEXKUaKLwm_57Al-5xFqHqFGZxIopjwoKAk-m-ifSZn2MOORkd8lF0UfIgYqlyQQNsJAhTamtUUTPMiRcKBBy3Ke-fLzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805fc7f33c.mp4?token=Mk8wdZ8_A8HN42DgQevWCHycVVSt4IiGm2tlM_rHez6mO7-oh3d7KYdfNQboubZjshs7danIZMvmEJRoN4y3o-yYf_Ad91h6uxImDavyv0uZkna_tSEF4s5UKsrOoZiCXa9FI71JvvInk7no6_Dnj1MqJ0ou5kltWF7djjXLc3dgbVCc6vxOdXblh1TFNu7jx9ZE1CgQBME3ywBRv5XMjPK3JPjWDbFm5KgbCt8hwnHsnVyLe6CGgVtB7pEXKUaKLwm_57Al-5xFqHqFGZxIopjwoKAk-m-ifSZn2MOORkd8lF0UfIgYqlyQQNsJAhTamtUUTPMiRcKBBy3Ke-fLzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ستون  دود در فرودگاه ملک‌خالد عربستان پس‌از حملات یمنی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/467107" target="_blank">📅 19:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467106">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrzpXv17wcJHvsoMymkv9IRCnTe7IO5oq9IqD5RrG__jCroBk0uTdocZdiFp0E1Nm6MgUleRvSRXKobqeoeeeYZsRvqQetfv5Bek0igxbrqTm2heNCBYmA98KZk2UsRYCJgocvpyn3k7e6Fb97425xxQCB-V8j0xDSA2KZPXe0PmwaWEAkill721iG9-SpzjXwWfXFzQz2miFs36Q-nDWzYEp9jNgB_SoUgZ7r8hDfwufT_l6-fH1LHgCufScAhzFLAUO2Kun4EBrbEFMd5EG_GON2JQJ2BiV_8uqnr4RvO0PZET07h8J7v9Gz44p03ugUeFz17aa0UieGy5yJo7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل مساوی تراکتوربه استقلال توسط حسینی
⚽️
تراکتور ۱ - ۱ استقلال @Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/467106" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467105">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616c846f9.mp4?token=MuEIc_CgIrHaQTEjObAcHz8Fau35oB611SW-eWSKnUpJjHv0kFXS9VkbgkkwzTzW_H1-QU_0-aSQY1DZ-NRKyZtWU_teKbNAWRWcti0lnL7OUf86_rA_WgN_hiLXJ2AxlK1fVxvzlNu0k4Q0xukrNcgwnACgKlkl9QZD5NabyWsFKKcPUcrcXvRazn_XxKWBSEex6QSkMyYZJ_27_LE3RKcU9tQoc5Iq8xjAeS0U42bkzqnUu8mOelw8TvtxmoKoiLQfVysymVODoyizyCCAUt2hYzJvv0mhxbARO840ofUvc4k1q1B2wW6ibcjmhn7LaUNlkaANimzskEuqAt31LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616c846f9.mp4?token=MuEIc_CgIrHaQTEjObAcHz8Fau35oB611SW-eWSKnUpJjHv0kFXS9VkbgkkwzTzW_H1-QU_0-aSQY1DZ-NRKyZtWU_teKbNAWRWcti0lnL7OUf86_rA_WgN_hiLXJ2AxlK1fVxvzlNu0k4Q0xukrNcgwnACgKlkl9QZD5NabyWsFKKcPUcrcXvRazn_XxKWBSEex6QSkMyYZJ_27_LE3RKcU9tQoc5Iq8xjAeS0U42bkzqnUu8mOelw8TvtxmoKoiLQfVysymVODoyizyCCAUt2hYzJvv0mhxbARO840ofUvc4k1q1B2wW6ibcjmhn7LaUNlkaANimzskEuqAt31LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تراکتور به استقلال که توسط داور مردود اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/467105" target="_blank">📅 18:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467104">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d32a4cdc.mp4?token=fzA2Z6IbXNZL-Y8w4GC7a720J3quApNiyd67FVWpiyHyYd0SKTaWqzlqcbxOzh-lauGhZFUwY4QtPaEPzxzKkjD3o-YyFyXHjJYxCfOvPEXoa8akGiRKF9WZ1crwqUv66GW0Tnhr-Uu0YoRjwReh5McryQ-DHzJYy-HbJxnfvTiYBqMcLqWKEQfQwwpaHh4tstyLugFY-a9xrHn-7q94LNnfSbYoWMdvIrsTiu8on3GOLe52pd4NlaGDjb7rCaZj3sWhd4dFA8WnkcGD7XYoI_9NatdgiUIwqXpKOh5ShLCcGbFhyOCL41ycVs49cbI-GsD9uBMJMXNleCVDlgDPEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d32a4cdc.mp4?token=fzA2Z6IbXNZL-Y8w4GC7a720J3quApNiyd67FVWpiyHyYd0SKTaWqzlqcbxOzh-lauGhZFUwY4QtPaEPzxzKkjD3o-YyFyXHjJYxCfOvPEXoa8akGiRKF9WZ1crwqUv66GW0Tnhr-Uu0YoRjwReh5McryQ-DHzJYy-HbJxnfvTiYBqMcLqWKEQfQwwpaHh4tstyLugFY-a9xrHn-7q94LNnfSbYoWMdvIrsTiu8on3GOLe52pd4NlaGDjb7rCaZj3sWhd4dFA8WnkcGD7XYoI_9NatdgiUIwqXpKOh5ShLCcGbFhyOCL41ycVs49cbI-GsD9uBMJMXNleCVDlgDPEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به تراکتور توسط سحرخیزان در دقیقۀ ۲۸
⚽️
تراکتور ۰ - ۱ استقلال @Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/467104" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzFco-7KP4VNkXQ0vlT7yIiZC0Lj8wfbtzAVldq2rE6Xl-aM-8P46FCNyWu4XoP6htvxtsupiuYL5UEG4UlCkyt2-Zt6uW2fzCxFtN7Lq3dVK8KXuKoQGIASlt5Hr8i0iwgifQXEGD_EemB5dFn__P4epQ3wfwz-hX2pFN0wvnhPFOy5819LYsPC1cN1v8jkYC1vK6vhqB55uVx60xQI_JAMb08oQj5sBp98-pT_ZABz_eTX5ugwOAAAcGK1MKRxHYIrbG_S41w-8cfNA0TwZ0lbbFfg7sK2RVfqCQ3dxjz3oIcZrFJQb32BUzjUoqHcneqOGYhiv2K6iLW_ughdaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrGd-ZlOaU0cc9UnbL7UtosGpeP1-6dicaKjxXW2mP1IXw2AhbwDItpXZCZR5WBfOqoCQ5PvFtBY7qWMMuP4tWKlVjXTcHbtSEgoa8K-hBQs4N9BslovkpsQfNhizBG3FDSVT7NQcs7fP5hc9CUYX-SOb-c23wA3ceHAMh5uE7ntP_S3MPIqJsh8yDzChQOFii2mlMzvTVi1F9Vi07XmQU4gy5e7mzlyRailZNlyrvypa5vYrTS8AfWN2GZlj0PC_EnQdkuHtq_B3R5PKJo5fllPK4dokQqYEPJdrIcez2BZeheLQOJZibb4iEPG0L96HOm-v9fvrNY87wrAUSIWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LyxZzsWRWoARs0JOTmj-unUueiUNZ-twyUV2BRG9IHvFeHqE7r0nVc-r-Mk3aq6Hrzbj6NIN8J84WffOscdLpfGeba_ekF4ESU9-kBb6zK8VwQdPdU_70ZPzDd6PCtwT15M0Occ2D9sWeYilsleQio14qnvKKc1uf1jO2GJAc_F8n1RaI9KbGpSQ7FMwtfcu6rpp5Wm8gZQ7X7QCublmNh8wz6AAZ1QxWw0o_s1c0pThTDmivz1N1BDsDwdWs95DEIwpWuDVnAXttABLaC7GmKdMAGwa4Lw3_p9H0zSjU0Nq9jriUsZXGnKzytcoeh_hOJMWE-jp3b-rdhYDFuqrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWWpjMpwn6QCf3BmDkJpu_jM5qMIOz2LccyG9ThNVaTtsESJ6X8hYIl41MI9r26TWwHQrZ6XDfRw-YNEfKqUjRkGDx1F89br4JrGR1u3zQ3NvEgDEYqvvM3_mlneBSyLxVUrztARnrr_w8gNNsvy-qRq1SIfKtnVO5U-c9yVqismLk3V-SR_EgThL600W5LhQff8hy7TX2Izs6X0F1MKV4k03GY0q4BERAOeAHpGGsNEN1clqTM3BAuD_4JXCUuJrOaIjqj3E25zVh7UH4WLLbkURcZufXK5T0TUUz92_ggOiLMWdAeH-XRl3J4ilX0Zq93Yz0hWGxUu578Ku8ULOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6cvihBQIsVug1F7iCPo4cFxDfBn4NPQwVTwvkwCpdFU_tSAUvpSjq8cp4kyQjtC6UaHJjAMtPgjoZfcWqB25CfD4x_sBQN-Y_6SPwCPRUsLAoYT5vkyHUQZEkTf27jRSvKoCLgJRxlkYiKpb-TK2wQtWxfF0yjVGNfnIvJQ6Np6ztGVCjkx_4QKKG4_3z1EXihMARQhpiLtWb2SSRnlswmKK3GzEg98EPnXUwxBm2rMg9yuxheRBzDg_ITavW2Cl2iM2qVFfVq1FVY3XKUnuhJZJLblp3jhmCsA87DzpRrzK_5FcSjqINao6cUMAkP29uRdECcdu1iCjbU0pGqA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtJY_KzA3kt2UNx7g9y4Fpf_nzYpSiggVGUeRHWdAGTtIkbetvF4rr6Hp80TFYCvXjQyXZcvj4ED7sTyafUFxtOvLWW97WyF1dRUnOl6OKZ8rFWe_FEszwNO4aQGyiW-O7U9k4SIHr_EABgl-Ldyv0yOKXdyRsjpnbdp52hm-0C95k1dJKUioV2pgqRqPBPauqjGw60oKFqjd91lHAI_qWmlFjkwfo9XU594xleSBOp8sS_ZtILZn7LAAUTfTbFRSyYn3vMAjAb34w0w9Y6AAXi2g3kLcDyFBg8q-U-wFPq6bttn0Rt4GvnQtsRgE_YAduvc1HNuRTKrwjNKTJ4dFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rk0EXEXoy_WdM1IArJ-1f4cX_TTDC1N0gitkEa04dNM4jVtDjOABvdKKYDL5kllg2dgUEYSyYK_s_lDlp3Xgz98ywSUGDu8noUrwkMDBdi6mu1_mzIHFr4ECU0pKrGxOC_Tai8qm3BIXxavzTtTr_G3dPYiwpwL_44xhT9GHxn7TnL3nr50YWaWL3_5f1cDZ3uTkhEkpWRRf-3A0_ftvFUuFT0ROfDo_VWRSDFjQ2Hk1UbDPAlfdu59nA4smE01jr7EUkhHgap5n84vwVjKpgAuvHCcL7VU7c-jazCznc-xUj0i0h9vx4phkIn9uiBZ6FFFbhDmH3s45afv4bnafvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBDNpqxQyH3R4o22fuk7WzjCqi-VLxbXwgPtOug7zaSwLNmY-iXQepIpfJoxOgfkireW_oq1H2SpLO013wSf7wmRHQCZXiFU4q6u4rI_F_RxiUx-kzgTg7HeGfYBDGh9_toOno34BL-gPPAUw2fLF_yCGJSTXSagxsMZLvyzHNXTPF6G7tSJZACW88fNu-xzrtJeR8lfa7ej-CDg-ohxRoUPl0HfyMPsjz-SzKZ4rh-oA62bQYWgiT1kuiu7ifSnHQvIAZzktN89Xm4imvg7n9azl1gKqge4Brk7_pvE6LJ0wI38sIysO__h-XQ7R-ESmsbcGejCONfmjfrZml5B6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رزمایش جان‌فدایان وطن در گلستان
عکس:
علی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/467096" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwa7rPSzPUNdJzu3LRjKj4rUSgJQOAuKF8hE41f4a7zhiNZIn746kAxMv8U7L_vyI7GU_u2ar9YG9HODF1k93F7tahDqc3LmnKeuahUVQ9nZEZNESMnDCi9wKOEjBuaFB2l4qrUpABBudyks3EGyAw2sguwwPxWgutShJATCN3roVASAXCIv89DKvJV-JjhmPbGe7jdVFKojkQ0bU691u-skQPR8JwXHRZgPC39nKjCvx5tjQvr2i3gQWxu5SGw1x51ybu9r5IAykHH5liiyXUv7hXS3daMFIHzgWJwKQNFRb6lxncn0K3dZ0KO4QDZ5Z75YAI05l6_ENVS1diuA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهلت انتخاب رشتۀ کنکور تا پایان روز یکشنبه ۱۹ مهر تمدید شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/467095" target="_blank">📅 17:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467094">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqngpXb23eNA5Aa87dg8qJjz8AZGJtJS6aXuHw92IXAL3gzzKoJjZND6vityftRpCkzM369T1w3xQAwxkv7AKmtQixkE1W-3544F4FoPqlzmdzU62X4lzFn7fl2qymKkB_V5U4ofDIS9qtntNldl86tq6ZP4xX4lryzm38xn6jAJQkl9oVSwNa4F5ttj99zUozEw5Ro1TTyFr4fYLYX4uPmDzx9P_NcomPZNVRje7l_Wd8D8V58_dyD7hspf3whZ2n5lKqiwEaVb_IpD45JbLSn7n56atLzgM0usYPDrOzAKiwfKy2EQWREXXM5zbCyCneEo5kyQAmCopblPfcJ9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شهید همدانی و شهید سلیمانی در کنار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/467094" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chZpo-BoXY1F36NqjvdGauJEPy5SzcJOdpzOiyU65IJAIQ8VMPr205CLJaGL1ImsJ02nbJq3Xw-3wkArUwV8K0_WiW6am3MXlwUifG9hC-CH7Pdk9KNNyG5c7QKkgLD11xXPwSLgOqlT-ucKLrM4UowoJjvvSumRckw3YcuNhdmHEk1zMVNMUhwXZuERbHTGrQ1iPufBQl0Nd5nOq67G7vm1qRk644eVFcrZ4KQDXUwlW7YeGInqKwWKJOrQehcMdhzr1ozmR2eWwaXXqjXqFdOxdknGV232jJs8uebCdBPqnxpGm-fCXbYyGYq6aYtE48Zfj_IEPgsavRvCzqipLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انصارالله: از هر کشور و نظام انتظار می‌رود که برای حمایت از مردم فلسطین در این مسئله‌ای که هیچ ابهامی در آن برای همه ملت‌های جهان وجود ندارد، وارد عمل شود. @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/467093" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f297caae75.mp4?token=uJL9pUuW8cDsbDGKO7TTkgz3tiNTmYnesTS7_y6FbeA0LoVRObPQ2c09diaoffp8K9bP14Yd2MPkXY1DtMm6lgAOBVA-tWemmihDCmAt7A_BaRPEPZoSiv_ulMhU9_yTcmfSgIpfZY6us5CaFTh-mobNkHCjcSYSyfbbUJAXy7ZNIvSEfIPbxOUjva4m-OPvDT5y2XzcToxA6HBvTEBxRJg7FTecD2L1Fvu2qqtBVlbawV770YkhGYBNIaWaE5brYy4hpAhm04cCk3R9OxrolaVQxkt1ZV-Pk2Zsx3bdkvOQzTowA-7DTDNJk58L1Zgj4BFLkEzKLvgbErt_VUPLUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f297caae75.mp4?token=uJL9pUuW8cDsbDGKO7TTkgz3tiNTmYnesTS7_y6FbeA0LoVRObPQ2c09diaoffp8K9bP14Yd2MPkXY1DtMm6lgAOBVA-tWemmihDCmAt7A_BaRPEPZoSiv_ulMhU9_yTcmfSgIpfZY6us5CaFTh-mobNkHCjcSYSyfbbUJAXy7ZNIvSEfIPbxOUjva4m-OPvDT5y2XzcToxA6HBvTEBxRJg7FTecD2L1Fvu2qqtBVlbawV770YkhGYBNIaWaE5brYy4hpAhm04cCk3R9OxrolaVQxkt1ZV-Pk2Zsx3bdkvOQzTowA-7DTDNJk58L1Zgj4BFLkEzKLvgbErt_VUPLUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به تراکتور توسط سحرخیزان در دقیقۀ ۲۸
⚽️
تراکتور ۰ - ۱ استقلال
@Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/467092" target="_blank">📅 17:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyyDW0ZdKf9fXgCToTllFPTu1v_2SyOqoZnMoqSQr15hZETkwCX4T1b2pKta539IHx4Q8KsPQxFv_9wHarcBgPz3BGhOcq7iYNRuoYz5XhQhMQpg8DVxXyoY1SYndhY1JVP4_KAiTnEHWX10EexVP_D89MYUVFPbTGOrKsWoqL6JEkX0L38JUfk3NY7_b8E1AsS-5CfskG3eRcPrqEL__xGskGJ5APd40eyTqg4FiAfRh-PtI1UHb1Ee-jwt3HGBjPxZWxp_rktmV4ySUxQlM-fdx7Cw06ul1wLu6maIHigTdoueR4JYPhzPsjYImeiIsCb1TzEG7acyE2V6f9YQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ادعای نیویورک‌تایمز درباره مشارکت جنگنده‌های پاکستانی در حملات به یمن
🔹
یک مقام ارشد نظامی پاکستان که نخواست نامش فاش شود، به روزنامه نیویورک‌تایمز گفت که از جنگنده‌های نیروی هوایی پاکستان در حملات به یمن استفاده شده است. @Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/467091" target="_blank">📅 17:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: هر کسی که از متجاوز سعودی حمایت کند یا خود را در صحنه اسلامی با او درگیر کند، خود را در هر معنای کلمه، در گناه، تجاوز و جنایت درگیر می‌کند و این امر پیامدهایی در ترازوی عدالت الهی خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/467090" target="_blank">📅 17:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467089">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: مردم ما هر روز بیشتر به مظلومیت و عدالتخواهی پرونده‌شان اطمینان پیدا می‌کنند و با عزمی راسخ‌تر در برابر رژیمی که کودکان و زنان را به قتل می‌رساند، مقاومت می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/467089" target="_blank">📅 17:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467088">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: یکی از اهداف متجاوز سعودی با جنایاتش، شکستن اراده مردم ما و مجبور کردن آن‌ها به تسلیم است، اما این یک توهم است. @Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/467088" target="_blank">📅 17:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467087">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: کسی که به طور مداوم کودکان و زنان را به قتل می‌رساند، چگونه می‌تواند تحت عنوان "حفاظت از مقدسات" عمل کند؟ @Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/467087" target="_blank">📅 17:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467086">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: برخی تصور می‌کنند که با حمایت آمریکا، می‌توانند از جنایات خود محافظت کنند، اما این افراد خداوند را فراموش کرده‌اند. این همان چیزی است که توسط متجاوز سعودی انجام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/467086" target="_blank">📅 17:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467085">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: نظام سعودی، نه سنت محمدی را و نه مکتب سنت را نمایندگی نمی‌کند، بلکه رویکرد صهیونیستی را نمایندگی می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/467085" target="_blank">📅 17:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467084">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: دشمن سعودی با جنایات خود، به وضوح در برابر تمام ملت‌های جهان، با ماهیت جنایتکارانه‌اش که به آن شناخته می‌شود، آشکار شده است. @Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/467084" target="_blank">📅 17:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467083">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: دشمن سعودی، شهروندان را در خانه‌هایشان و در بازارها، مانند آنچه در منطقه "ماویه" رخ داد، هدف قرار می‌دهد، و رسانه‌های دشمن درباره "تجمعات حوثی" صحبت می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/467083" target="_blank">📅 17:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467082">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: نیروهای نظامی که دشمن سعودی آموزش می‌دهد، باید با اسرای به روشی وحشیانه برخورد نکنند؛ این رفتار هیچ ارتباطی با آموزه‌ها و ارزش‌های اسلام و همچنین با فرهنگ و اخلاق مردم یمن ندارد. @Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/467082" target="_blank">📅 17:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467081">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: دشمن سعودی برای دستیابی به اهداف خود، به آمریکایی‌ها و انگلیسی‌ها تکیه می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/467081" target="_blank">📅 17:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467080">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: دشمن سعودی، از زمانی که به تشدید تنش‌ها بازگشته، به همان روش قبلی در هدف قرار دادن دانشجویان، کودکان و زنان روی آورده است. @Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/467080" target="_blank">📅 17:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467079">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: جنایات متعددی توسظ عربستان رخ داده است و از جمله برجسته‌ترین آن‌ها، بمب‌گذاری عطان است که در آن از بمبی استفاده شد که به طور بین‌المللی ممنوع است، و میزان تخریبی که به خانه‌های مردم وارد کرد، بسیار زیاد بود. @Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/467079" target="_blank">📅 17:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467078">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
رهبر انصارالله: شمشیر داخل پرچم عربستان هرگز در برابر دشمنان امت به میدان نرفته است
🔹
رژیم سعودی خود را به عنوان حامل پرچم اسلام معرفی می‌کند و کلمه "توحید" را در پرچم ملی خود قرار داده است، و شمشیری را که فقط در برابر ملت ما به کار گرفته شده است.
🔹
چه زمانی…</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/467078" target="_blank">📅 17:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467077">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
رهبر انصارالله: شمشیر داخل پرچم عربستان هرگز در برابر دشمنان امت به میدان نرفته است
🔹
رژیم سعودی خود را به عنوان حامل پرچم اسلام معرفی می‌کند و کلمه "توحید" را در پرچم ملی خود قرار داده است، و شمشیری را که فقط در برابر ملت ما به کار گرفته شده است.
🔹
چه زمانی رژیم سعودی یک بار هم در مقابل آمریکا و اسرائیل موضع نظامی اتخاذ کرده است؟
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/467077" target="_blank">📅 17:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467071">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8nmSujnith8h8wSyE5qfN8B6QrmzjtoFiWrmlaxtzXG4eccK7peLPXckF220hI2FVB8VEQWeuyXg868Z-5Fm0shGU0qcCjfqer0CQrXeH0rsiW7i1Q05g_qwqfBZmqiBYGRFeXqZqRt7v3WERh5GXCQuHodlcimSURildmlPvq0rNiLHeNjFgORmjZr4gRxzOd2nUlxcHFq3TGPyLM-TLpYvOequNlkfw6Zm3mxwxAggXUn2TE7VVNhftmONE4reGJaEWStmLUGpIuh3FhnwCMfSOr5_CVN4CrqBjaYGEOlDF0AcFH0pzTl0HVG76TlkTkVm24Jmp3RGz1jQw7BbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKY34uW6xiMIyIBq71ITvOSG2vvU5CXjFUkx3hI8gQBbv8ibXTe9oCVN6FJJw1WzOLZ3WclAXFaAnqpsNkmXE3dAzN_0J_nPkzV2i7IuTPd4RF-EvqoP07R6zAEfk_TRFj6-5jRYZyPByQ9y35Ix0qxbZ4iGrjBP_6wk2MVNS7_2iVOAgaNPhsCcxJvf-Z_hmt7CzaNdAId9M4y9oMq_jnzKj-rXLkMhCF_bWPcrE4qVZenHn2cszaUJzUEqb5UDmXRx9VtctzdnbgTw4UcrL2swl_yxrYMAy4-JFlJGeOHfXD9QwiNtzwyYv2ZlNTOLjtr9F0i_qj0AWymkeOcZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ifgGKB5AHU47m16LlYKR-ziKWRWvxOJvYv-9MO9XOCNtGwK2OsRAyX1-MsURmYsrIcoAntMA6A43KU9heig_owsbcaowofKhf2h6iSs4pXiLD0ne0JmCbq9HWI3MkJK1-zp0c7mrqKjY2REVGP5XmskVZ1ZOrKC2iqEO6wjHAesTt4jG9PLAT_5YFs5SX45w3fr1tTnKB3GHMfCi9wwpcNj1IFr1SjRkwCfZoswMkcIbkNinEDSEHfckezY269lFuiNbCLCbsBdhvPxoJELQQ_Mbb7GSvpPpyn_5jP4SGg7iGhDmiXWALjdxrOa7ryvupSJUP9v1a78ELk4fwOoMdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCfmlxhzfDYTa4OUr1Q-Q5SDhMw16zrnb6RgCHo-6s3lAxPtsA6MaRUQe7ZdXmsvbu_mnrkVWDk7Pbb_B0w7Ih9qIQWXW7BDwmcTwqXlYqA4RWafoSYZaaxrfqGCDT6H8wG8-t_YWpLZeoEThSrH0gFqA0BIn1uIpyWFPsbf7KCckr3IPJqU4kOSk1DMndeN1aP0gtUfdqI6p96c7gzw4xy63WtkViCygW5TreFTeeTdtjJwguhwy1Qix6P-a_6wfh5FC3RhUk-0tFhTuqNGwOBeSkhEtEslb3js9xNT1vlm-DF7DohZ-8cxhT9efWwlHDWeEc-yrZw9lq6QA58rvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBDcb1Ek65Hcn7gmlG-myYPmnOEY5hjdy8r-UPBKoqacCEn9iA1li-hhW3Goi6rMafiH3zzhMrdZLy1cnHbDxdraZ1ufA3pbW_oIF3sCToTnoFhXEQOxOhf_RyMlEl1fVXet1E01D9ijIB5-AYwv-gjA6AUEexrcNL09L1mHVZLCttPs4EL1JBsmMBUIB-8PIXS0qITOuoSZ_bVYXHjsq7znn1hxSpXKuXkwSOaFl-hBXtrLRwPDfSWYdr5ZD3dkGYoC_OdbPds7z0ARQCku4cza-xkgmzs6Y-Nux5MEVrI_Sj9bf4OVV4Sf_L4We5zbh5A5_HrAt84u01bE-gmbQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRxNLkzSfOErLs_OcNcHNn1VDZgoLWkXiHyyE7FDfYrBOB2REPN5UA6ie6IkSUtVQMYhpRJgls2dbxl9BvCWY4lNtGNIatzMWIgf0DHume40bNHRbG9xI6mwc4fOLPB9urlTJdzN_9TEJw0Tj4fo7DFyczRX7RuAUbYDVaYmuKVY0CaAYpcfQPamhLt5AISP4nm607dAfDQ4Mlwc3AP6rFw7i6PHWjLT02Uzm50TIyrUNgSg70N5X2G4h7ijp_By2iMmQi7t2cZ7Xf-QeXaIT1h6jAxdH0zeSrfFd0ZjHQXfTle9lQuPuKN3kT2el3fb3jr3Thi9B6gPjmfZhJELPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از گرم‌کردن بازیکنان تیم‌های استقلال و تراکتور پیش‌از آغاز بازی
⚽️
این بازی ساعت ۱۷ در ورزشگاه یادگار امام تبریز برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/467071" target="_blank">📅 16:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467070">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a74cabda4.mp4?token=dv7fD-kkezY2GtxOgDi4A530Xr69EqeQ0jFoq-8_ouYgQhm973MxqnDeBnqPTn6osCQyngvZXOnS_Jtc5QHOLmF5-q-3P1eveIaOpmHbOfcIjYMyk2AXVzq2b6gqELLb7-SP2NXwkbJV0-IayMYAAnxHT19jxzMaf1vyLxIBIuT5sHZSfWurg9dQJ6b1-RzyPv2-aBF-iVoPifGv3dzgh1Q0Be1CQ3YdOkYUK1Dgb1pS7em6wjeMAUuSAPV66H-eIeS_SC9PVx0mEk_6ZYb7SJxxCtIYB9iHIN5HCdh0iEHXnvDqDkQVZt4ZElDu3lSzECn_-pzqAv-YDguav_8ahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a74cabda4.mp4?token=dv7fD-kkezY2GtxOgDi4A530Xr69EqeQ0jFoq-8_ouYgQhm973MxqnDeBnqPTn6osCQyngvZXOnS_Jtc5QHOLmF5-q-3P1eveIaOpmHbOfcIjYMyk2AXVzq2b6gqELLb7-SP2NXwkbJV0-IayMYAAnxHT19jxzMaf1vyLxIBIuT5sHZSfWurg9dQJ6b1-RzyPv2-aBF-iVoPifGv3dzgh1Q0Be1CQ3YdOkYUK1Dgb1pS7em6wjeMAUuSAPV66H-eIeS_SC9PVx0mEk_6ZYb7SJxxCtIYB9iHIN5HCdh0iEHXnvDqDkQVZt4ZElDu3lSzECn_-pzqAv-YDguav_8ahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از خسارات جدید آرامکو در رابغ
🔹
تصاویر ماهواره‌ای که روز گذشته ثبت شده، آسیب‌دیدن چندین مخزن ذخیرهٔ نفت و مخازن تحت فشار در پالایشگاه شرکت آرامکوی عربستان در رابغ را نشان می‌دهد.
🔹
به‌گزارش صفحه اوسینت، دست‌کم یکی از این مخازن درپی حملات نیروهای مسلح یمن به‌طور کامل منهدم شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/467070" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467069">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a8871ad5.mp4?token=Y2GeKJsr_lAaCCWwg0pnrRy3Lw1dWkZ3XraWo30Xz_jH1xo30PoWEbjSO2aQbq11lwwrhMnvXqwlhSIX9t3lYEGTu5YDBo3Pgi94rkp6iog5gnVYh0ZTGZuQZ8R3_WWbOccPrNzkndps6kjzBDyo_ZNxSZbiamJuIG5AfI6NL_wJTSNpgpS-g4ahW8wnUFXmFTfDoQF05BLhCXeSvfUk5ALecSCmgcjpTedqsljQAUYkTpC92wpqRL3W7TrKHtOkxcTPQUUhGXPkiqUDZPDuKqertkz-XSuFaSREpnE0tv3EWTTugXWlFFj3MrDq6ggkifg7UncU957VzK8WNLsx7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a8871ad5.mp4?token=Y2GeKJsr_lAaCCWwg0pnrRy3Lw1dWkZ3XraWo30Xz_jH1xo30PoWEbjSO2aQbq11lwwrhMnvXqwlhSIX9t3lYEGTu5YDBo3Pgi94rkp6iog5gnVYh0ZTGZuQZ8R3_WWbOccPrNzkndps6kjzBDyo_ZNxSZbiamJuIG5AfI6NL_wJTSNpgpS-g4ahW8wnUFXmFTfDoQF05BLhCXeSvfUk5ALecSCmgcjpTedqsljQAUYkTpC92wpqRL3W7TrKHtOkxcTPQUUhGXPkiqUDZPDuKqertkz-XSuFaSREpnE0tv3EWTTugXWlFFj3MrDq6ggkifg7UncU957VzK8WNLsx7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: در سفر به ترکمنستان با سران کشورها دربارهٔ مسئلهٔ خزر که با خطر مواجه است، گفت‌وگو خواهیم کرد.
🔹
‌رئیس‌جمهور پیش‌از سفر به ترکمنستان: خزر سرمایه‌ای برای نسل‌های آینده و محیط زیست ماست که اگر از بین برود، مشکلات بسیار زیادی برای همه کشورهایی که در…</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/467069" target="_blank">📅 16:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467068">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f50e11eb2.mp4?token=Hj5oH8WYaw0GZlYV33IX4qCHFWl4aWwKoIppj6k8Mct7EmE_RlCn6dCjvKW_9jUQEXmrlN9YX8wOJmlBvdkgsh3CaISbL14haW_xBB8HiQu_qNaAyHqz0OeGCCzevVQ1bhptad6eo8kyztgslL1jsCr7-MrQlNXN7VwYxF6nrffTReF8JFSiE1lN5eijJ4tDR6w6Vu5-G_HNMnR9SXIeBIuGCtJlDTkHabCRKmBpHooMFU-SRQlYAtrYM0a-0F5lS0KTrw3s0bt7afjXcY7_nmT8cOlvXOqD4DZZoDu5tCEys8fGZO8aNHvjvjMZGkzmyGfnjwEYk2SuzVBjlMXSEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f50e11eb2.mp4?token=Hj5oH8WYaw0GZlYV33IX4qCHFWl4aWwKoIppj6k8Mct7EmE_RlCn6dCjvKW_9jUQEXmrlN9YX8wOJmlBvdkgsh3CaISbL14haW_xBB8HiQu_qNaAyHqz0OeGCCzevVQ1bhptad6eo8kyztgslL1jsCr7-MrQlNXN7VwYxF6nrffTReF8JFSiE1lN5eijJ4tDR6w6Vu5-G_HNMnR9SXIeBIuGCtJlDTkHabCRKmBpHooMFU-SRQlYAtrYM0a-0F5lS0KTrw3s0bt7afjXcY7_nmT8cOlvXOqD4DZZoDu5tCEys8fGZO8aNHvjvjMZGkzmyGfnjwEYk2SuzVBjlMXSEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان فردا به ترکمنستان می‌رود
🔹
رئیس‌جمهور، فردا به‌منظور شرکت در هفدهمین کنفرانس دولت‌های عضو کنوانسیون تنوع زیستی، عازم ترکمنستان می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/467068" target="_blank">📅 16:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467067">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOoYUSLK_env5WLdHLxidFy-vjHlQbHjRH5PRTj21dT_NEmRBbvGie_MHg5naK9vKw4qoLlkJ3UrrU7JtiNMgTSAFv5HBJNc0vmC8ui-tWD9ymFbl7BH05B0mc0QkYZawm5TBGekFWCVc3tyX9XNdcfDMaVbf8dEl35Yzuiza6bwzwNXK6Q-SLVmgK0LsAoSEjvDsncZQJ0FqeewoWNfYQxOm_hWHyAsi_52M252c-L7Bxycoq5cxTTjHRzjnRItmbgP6TY6DJOJIUBt_1xlJ-xyZt1Tc86fLzA1QGXwed35XEUqYqOAmgakmQ4N9xhQLWjAVd7vXKvv4CW5txN1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسلامی:‌ سبد رادیوداروهای کشور به ۷۸ محصول رسید
🔹
رئیس سازمان انرژی اتمی در مراسم افتتاح اولین مرکز دانشگاهی تشخیص و درمانی سرطان کودکان: ایران از نخستین کشورهایی است که داروهای آلفازا را وارد عرصهٔ درمان کرده است؛ سبد رادیوداروهای کشور به ۷۸ محصول رسیده است.…</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/467067" target="_blank">📅 16:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467066">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: فرودگاه بین‌المللی خالد در ریاض را با یک موشک بالستیک مورد هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/467066" target="_blank">📅 16:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467065">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یمن به کارکنان تأسیسات نفتی سعودی: به مناطق هدف عملیات نزدیک
نشوید
🔹
نیروهای مسلح یمن: به تمامی کارکنان، از جمله کارشناسان، مهندسان و کارگران در تمامی تاسیسات نفتی عربستان سعودی هشدار می‌دهیم که از حضور در مکان‌هایی که هدف نیروهای ما قرار دارند، خودداری کنند تا از به خطر افتادن جان خود جلوگیری شود.
🔹
هشدار خود را به شرکت‌های هواپیمایی فعال در فرودگاه‌ها و حریم هوایی عربستان سعودی و همچنین به مسافران و کارکنان این شرکت‌ها که قبلاً اعلام شده بود، تکرار می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/467065" target="_blank">📅 15:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467064">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R66WtCZbYXqK6Pxg95tASBlZaIFeuqRs58BZ7uhenUvl0b7kP2bXDhhjXnKctR17bTrwc5HrUqk9F6RWGH5JH-xoe8Yw6UYoCihXVh29B21mt_kYcsro1Rmry1tJJf92O7yo6xHFkiNH0iN283ydfv69cHP7R6wpp4O_DR78yV9ZPh3AQv_b5shm__zmDsq19DcOyWObVmp536yWjoDESUOdMycdS2A0T_vmBR374Y8Y7is4ZqHtOYMiMNUgzkixskIignSJDH_eNJSo1lAN0TC1Z3UjYKrQXzmID-1KfSVTkGoiXkzKCWTPecba_HzPqqtrBDGXqBiCGKsL7Qz6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برندهٔ جایزهٔ نوبل ادبیات اعلام شد
🔹
جایزه نوبل ادبیات ۲۰۲۶ به «آن کارسون»، نویسنده کانادایی، اعطا شد.
🔹
آکادمی نوبل اعلام کرد این جایزه به‌دلیل مجموعه آثار جسورانه و خلاقانهٔ او که در گفت‌وگویی بازیگوشانه با سنت کلاسیک، فرم‌های تازه‌ای برای ادبیات معاصر خلق کرده است به این نویسنده تعلق گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/467064" target="_blank">📅 15:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOoTmF_esNNbCERUQ_B6eQOIL-rJtxN4Oo90axIQSft8VoRn758sEnBNXIkBpZO_4qKwFsuhtQK8ZSAAU1Kbpv6NytYPgHkpnWum7DPoJFaV3ESqrgi-j4fqh9qMO_dPbHV15-ZjdxHh4aLiWrKLMLkJ5pHVhKfCbdxzOpNIObLseYLjsKA45-kNS2cz8gzTx0K8vkJlRT4rDo9Yh_HCENT-R_bVEUCNiXphk-z3qPZFqsKzt7xfDhEsU8MnOYThjIcAW-tvsTrAzyq_KDrCcMv9ZoQfmTmvhf5rUu1VNTRPBYoI4YRrNynK2hOTX3mIgLF70u0SR7dv1Qf6E_nbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: باید با اتحاد و انسجام ایران را به جایگاه اصلی خود برسانیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/467062" target="_blank">📅 15:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انصارالله: جنگنده‌های ائتلاف سعودی، فرودگاه الحدیده را هدف قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/467061" target="_blank">📅 15:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467054">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8bujUALtp30RQhVDdQlRIBcJMEfMzVOm1JSeAwRVyRXKYsTXrpfZAIYdilLP1aRbbwKeYtUYsdkS4x-rF9SaKYdxboQcL0ISAERjBG9XA9Wdmj_wiZROb_mFoEzb2VPeCXIaZMkHLhqg4SmCuavdllKcuAM2FY27eTBE8FbXP2lmeHLK-KO7YYf4JwDLecXRrqW_C_g9fDR3GRH0XLJ-S67IHLi5xfKHYtZpMGNaFT0woRvPbMQwd1UX8JYcck6sQPdPSIs0CXrLAxpqGyzCRMz_rb4l0X-FvgcaXrAeW-utQXpFM2fwPB4yZXtLRRYiCzipkRHVDkYiZbtNuIOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2xyB1hWEnjge_DtwKJEA6qOwIBWMNx3r33Gp9olT3bNHJqc7TnSEKhIn7J9D3RV8-C3vgw5lsrKisWUjP8OQ9plv0GNh3V_oLqYVpkRt7-SwrnZ5cynGPEG7-sQeSGxEeSJ0AL0OK5G4cSMNVB9YWJVRmWIU3OX5JDbVBmOdQj28SS9kwkGNc8Re_DxLT09b2pQCm5edVg7-pHBqdFY67RhQKfSjvTYYiuLPc_K4RFtcJL4vFRsERfcp7cNbCJdH6AtQfYUrVEo2LZ9YSLf_q3obLzXqIa0KFk90io8HrVfhDFJmd3Owez75fVowgzXp4eH-8z9atwyfmZBPU1wKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLnOEfeWBRqt2YkufbcIWq6ITUmH1MOYGSX8BmYw4_17-ZYIAEzLreVTEFhFZgU-ct0p25M6MNOffSLG5SN5RlVgXOHI0l8bGV5WvOJpfyDnJvPgVVMc5CHOecg30N5ItgfuWWdCQxWDINVUQr0IXPLoMrL_kroLq8bx3QPz9MJMZJYMelcCSWhNLQQf5kGDy7fgsUEw-oyHeLcikJNDENi26C8hPdb7DdMu9pPm58YXSXyMEVQH03P9Y-IEA5GSaChnKJyzV32_Ei70IEZ3nsEsINvL32xOMI4_RMkOrVDJ3dgbMReo-OnYtEfPed6PVTxgTKZotmehxmJ44D0LMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPQhhEq8pRik4RqOUi6eK4ASiJysmKi_BEKJpkubD5Chddl8baQkwopp0Y7BElkOBS9Fs5TkcN5QoXuONqxYsiCMc1k4gHgRYAF412pebJW3GGmCb7OqoAkarvCXF3enWF7x7RzR7nwJyjUXijwJOimceofRgKB8stcu1YfUNXt8_dkE3PoUGTJ9vBVdyhbUrKqczi7wXghDx3AsyH-Nwsqj6K75Nxf3dxk-P-otHE9K45GqLlC0u6H2_7nGoOEfIOLk6ua63DJaBUmLqaKmt3bEgCfyRymfEUQoPyncpfUfQFI6qBMYX6rLGtTcX6T7K5cqxT3kcfKfVRBe9x8zoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bc49bJMk4crRj5GJ9dhRCy9W8pZxk4508gHUwj2w4oKj1h0qucatMIKwfPCchDKiAhKwXZHId4H1cNx5NlhNNAquaScuCYiRclOCcIO-SLW6SupYvidPN8ecpUplpoay8iIlXo-DN8sGtxPxNzLk6LRCvmNTFjoxe5pLmQs9QgeSXOvg2EDnXAPsd5GUOC4wfxQ5-16pnLHtqJf_C1LhAmEmqXhpmJZWgN5obkZU3c0f5ktUUR3oA_gSVtzsbrevSu5FlRPTtl_0aJzam1XjnfoILVCTimIrmEHyxkuuKslJc4bcmC73vbAYFQSmj1f-PIbjyN1BitValj1hySsAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hr_A-pP0OokSeGoGY4AzdS4oI6QshWSzEastO8V08jSNb0y2A4QAJFzPbnbDPxq2pWWqg5Rs10o90UsSlHVXDDtokxyqnLaYQaqgvu7kxwzsHz-8TURDvN6_Hqt1MeJQUQJwFgLIE8lb5bQCjCuJL7idm1aOEswk2HZwcxxbh7RsJYFtA3b4B1bjf0QvLPxKD37tFSdCx6_Fl5fO3upLa0VxSogqli6PSSpn0OQ2T-Vn-LA05TR-akIffC1E_8mGe4rztm5cysFvla2LZl8KS1mdxzo5azTlFQFFR0ZN31aN9JCbkSb2x52ektQebsnysaQt0DxSBaiEjni--sFmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LA8-GCGK49umO0qfyCPjbdpvgW7SETG40h1Y8HE6pXtn9o7F-F5Xs-1guz484hUB3PHHjMpUahNtvmbWhbcHjLBF-_RfulqCwBgw_oaDt_VMBVumBb_Ra__AwKlwKAPl_xuZuCD7o7cMlbT1ISn_FUfk-uYdSKAH7PGf3Y5XqZTPUdZuGFRArO73OOix1aqVsjIZ1ksfk7yivNUCRGdKIGQMtt2D3nMXXiuCGT1C6LGhJ6qgvcEk380dY_15CHkXY42DbmJL2_NwN_nmOzjnQ4d_mv8juAitrkNWnRv-tAxPKXahUSdBu-kN1vyYnZPIOQ0s9xRcYfSu8tm8YBP-1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات سنگ‌نوردی قهرمانی کشور در همدان برگزار شد
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/467054" target="_blank">📅 15:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467053">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhY7rpJYWQQAVJWX7y2ZDlr_DzNlwAAbiW9NDoxKJ9AjNoI1YV5Gvlv6vl90Syn3QZuGzzJ8klJ50H34dE72jVHouoX02hoqUoN_3eFy_y4n3clCDv2Ntz-FXq5slw6Lgynm9a6oWcX8Wlt6yhn1Yrp3JzLCsddxy317NemJ2pJfiGNC4cME8RbO5FXIVUmt9l22FNfS6XcJx1-9fk4inwbyNe8G6TIjtQ2AQ_2K0GC5axq1Xa3roDxjLZDOaBeGNPP1OQpsCG1HGgm-5Xd82kmKCbY30TxqXSzRzPEbw2UhJL3VeTzqaKeGWYafUzVzbY9UyuOYMUrU_es-wI3BQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه: برای جنگ با کشورهای دیگر نیرو نمی‌فرستیم
🔹
وزیر خارجهٔ ترکیه: کشور ما تحت پیمان مکه نیروهای خود را برای حمله به کشورهای دیگر اعزام نخواهد کرد؛ این توافق، یک پیمان دفاعی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/467053" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467052">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1CrgWn3FZk-OxnupYv6nROy6slUUfizPuwiDG22uVRIkrlRBFbqSyvJBDLknyBSFNBfve_ccszlFC91RpFlgyPyTiHmHSNGrFxNWtEeoEewIH1tNRLQaSKv7xaGKX3xrrS0ZoSGsXoo0RBvU5Yd58bY8sviAI3jiF_EJcFOOd0NyR61bL0lpJGDxfg3ahLlMqFthpmmSNBVnN9mSvuKDdcmlxVbkv3jCEGo9YLbyZF3y1mEcYOjNmbDblhJe2WXyzBsuoDlx5NljGAiqz8mVD02UXFgA-Oh-RiXl9FRk4C6YLItbLD7W3kbgUxENPnDe7OCQvwy8fB3QGvHf25G-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پولیتیکو: پهپادهای ایران ضعف آمریکا را برملا کرد
🔹
در حالی که فشارها در آمریکا علیه جنگ دونالد ترامپ با ایران ادامه دارد، وبگاه «پولیتیکو» گزارشی تحلیلی از آشکار شدن ضعف نظامی واشنگتن در برابر تهران منتشر کرد.
🔹
به گزارش این رسانه آمریکایی، ایران با استفاده از پهپادهای خود برای مقابله با تجاوزگری‌های آمریکا، باعث تغییر در ماهیت‌ جنگ‌ در جهان شده است.
🔹
پولیتیکو نوشت: «رئیس‌جمهور آمریکا دونالد ترامپ اصرار دارد که ارتش ایران بر اثر هشت ماه حملات نیروهای آمریکایی و اسرائیلی "کاملاً نابود" شده است اما تهران همچنان با استفاده از پهپادهای ارزان‌قیمت "شاهد" دست به حملات متقابل می‌زند؛ پهپادهایی که مانع بازگشت نیروی دریایی آمریکا به بنادر دوست در خاورمیانه شده و آسیب‌های سنگینی به یک پایگاه هوایی آمریکا در نزدیکی ایران وارد کرده‌اند.»
🔹
طبق این گزارش، «هشدارهای مربوط به پهپادهای ایرانی حتی منجر به تخلیه تمامی بمب‌افکن‌های آمریکایی از پایگاه هوایی "فرفورد" بریتانیا شد و در ماه جولای نیز ترامپ را واداشت تا هنگام ترک اجلاس ناتو در آنکارای ترکیه، با عجله پشت یک چرخ‌دستی پذیرایی (کامیون حمل غذا) پناه بگیرد. این رویدادها گویای گستردگی این تهدیدهای جدید و همچنین میزان عدم آمادگی مقامات آمریکایی و اروپایی برای مقابله با این نوع جدید از جنگ است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/467052" target="_blank">📅 14:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467051">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e4259ce7.mp4?token=o-lFJy4G5lEYrgGXa532MFn5WwiSfVHsujMYdZ9VJCUQgRE6aEnAobddbbcLjPB_na3cVaRX-oU0083ddIKQ7k64fVCE7jwwR-6RgU3rkJ_gDPhszop6hbQgYQ-3PnmDlho9I9YT2xfTok1yZvUKsUQOUC-iIZAjBFMdi3PcF36ftKj8bIsGAHENIBSQqXeeADJvIwp3hgaMSZvb6EBUcpR9XNTrM20INIaQn9JwBkLtDcaaZ4hvAYZeoS1k-MsQa3ElfSbPe91azmF6GA3mdtpYSB6ALAPGaTw-zOmih-U66YKnt6siEaqwHXOlSowm32bV8Cx_rXo-yXzu1y-lQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e4259ce7.mp4?token=o-lFJy4G5lEYrgGXa532MFn5WwiSfVHsujMYdZ9VJCUQgRE6aEnAobddbbcLjPB_na3cVaRX-oU0083ddIKQ7k64fVCE7jwwR-6RgU3rkJ_gDPhszop6hbQgYQ-3PnmDlho9I9YT2xfTok1yZvUKsUQOUC-iIZAjBFMdi3PcF36ftKj8bIsGAHENIBSQqXeeADJvIwp3hgaMSZvb6EBUcpR9XNTrM20INIaQn9JwBkLtDcaaZ4hvAYZeoS1k-MsQa3ElfSbPe91azmF6GA3mdtpYSB6ALAPGaTw-zOmih-U66YKnt6siEaqwHXOlSowm32bV8Cx_rXo-yXzu1y-lQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ افزایش اعتبار کالابرگ به روزهای آینده موکول شد
🔹
معاون رفاه وزیر تعاون: چون تیم اقتصادی دولت هنوز بابت عدد و تعداد دقیق مشمولان طرح افزایش اعتبار کالابرگ به توافق نهایی نرسیده‌اند،‌ افزایش اعتبار کالابرگ به روزهای آینده موکول شد.
🔸
پیش از این وعده داده شده…</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/467051" target="_blank">📅 14:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467050">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هشدار فرمانده حنظله به امارات: بیش از این با آتش بازی نکنید
🔹
فرمانده حنظله: آنچه در اتاق‌های بسته می‌گذرد، برای ما پشت درهای بسته نمی‌ماند؛ از جلسات به‌ظاهر سری تا تحرکات و شیطنت‌های شما در کشورهای منطقه، همه رصد می‌شود.
🔹
برای حفظ چند صندلی و منصب سیاسی، بیش از این با آتش بازی نکنند.
🔹
در صورت تکرار «آزمودن محاسبات ما» پاسخ طرف مقابل به‌گونه‌ای خواهد بود که هزینهٔ راهبردی آن، تا مدت‌ها از توان جبران‌شان خارج باشد.
🔹
گاهی عاقلانه‌ترین تصمیم برای بقا، این است که بدانید کجا باید متوقف شوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/467050" target="_blank">📅 14:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467049">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rqd1BfB04pBzU4zftL9BsaCVbzjLSyy_zEvfyhHwLmOe1znkjvGKdE-xkxjEFXjWJ4vacgqWgXsV7unKpkrjys-36zui5pbKL2SVVl3qI9XCb6qQXTfQZxHyf4-uDMQ-Yvcywaq5bfQmlXsumyZtXGt2QMWoOwiTagWcC3EoXGUhxPni5__uJKcuDY_jWAu4OcdR3lt5t-fFiA7rCaYL6_G0bBM2r1qXhJenGDQOcLXtiP_5dmubp8j4AM15cGZlxJ_aoBv8VPA77gSpIi-tzfqoY45LyeZBMgZc80qN462uNMXyKltzsEQaxsdOQrnDXYQrOR3nuJ8_NTSa3cZnew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار ابن‌الرضا خطاب به سران آمریکا: اشتباهی سربزند تقسیم‌بندی جدیدی خواهید دید
🔹
سرپرست وزارت دفاع: او هنوز جنگ را در مهدکودک پنتاگون نقاشی می‌کند؛ غافل از اینکه جهان را با سخنرانی و نمایش نمی‌توان تقسیم کرد. «میدان» حرف آخر را می‌زند.
🔹
فاصلهٔ شما با ما را موشک‌های ما تعیین می‌کند. دیروز دریای عمان، امروز اقیانوس هند و فردا خلیج خوک‌ها. اشتباهی سربزند تقسیم‌بندی جدیدی خواهید دید.
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/467049" target="_blank">📅 14:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467048">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWhl1gxkdCc360K0DgOszqe3knDMySria67R-XVrXvT16xGAc-wTpFw4YTs70jG0Kox5QwpNsdOmJ6pzgRqWtgnE5gQ76J61zH_cfpNOlWByPNuGVk1x83t8GGrozBrK7Btc-d6m5gaxJTkKbTnrFylsUbsssvVed7P-x2Uc8GOIpojSzgt4pxk0hqzxZ1zv3IlwcUS8VBNGuiv-GsvI0nIyyHNyjlEPgJnCn2ooow9aHsIT0owmV2_BgWwm2aZC4leZNQoC2ZYgVfE_VlcJUFfZZwGjo0UjgVVNrWHDV7d1Z77CeMkOunao79TmXRWkPgq-MGwAyXlTEtj2r9dvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره‌کل صمت مازندران: در بازرسی از یک واحد، ۵ هزار ماینر قاچاق کشف شد.
عکس: وحید بیات
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/467048" target="_blank">📅 14:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467047">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94a138de7.mp4?token=TNiX-3v61PaTI8gvCUyPc52KSuo1N1dRj3scRibQ_495ufGGJCr27rX47RegitbqRGr6O_rFG6KM6cBy2_IIDvCUbGGrrou-rDbfz40guyLqVyiiBY0XGBxGcpzgHWkmMGwP1hg7QCGHxV6XD2Q5uGwGCo7kMkKgklD-4x8ZSvVLPmhnfmjE0T61r6EtKZDdFkq46DvN6qVBrb6mFJJ3Y2bO62TS6Oe2HHiO9KlS3aoIpDKoAPA6-OZikY9zp67_Vv2udhNUIXtGWOed3t1Vi4NJ2krsZuPrGEw06NOpC3KLGor_KzYstXzWJOEbNX4J1aFbgblTzDiIYMqj6eJU-BFMwMuh9ZJPqalV6jYR22dCyU9T73Qol9CEMYR4nv287YfdeHCcE4RRtPvxFDvFfiZ2Ls5booYuIvn_z08mx2nsdKGvmrw0D_Mm1T-MSg47Q1XUHvDanDC9RcbS9VTu5hdYBGwyhoN8DzBjVrEvAKE4wI0FQ_9f1_l5zA82fUDL1Hayuw4FkGP85iN-YeAFF8Twxr_jn0ZdQOp9AhyLDu833o1J-_v5-zh_YV1nw61vSpgNCQUMU2LyYWMf0kDzDLqhDhpU304jcbsrOHtldUmfFyKx-MMDdmfRjOdIP4vOGtav66wEHycwVdtbbwq5xHGYax75HHAI4bAB4vRgJLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94a138de7.mp4?token=TNiX-3v61PaTI8gvCUyPc52KSuo1N1dRj3scRibQ_495ufGGJCr27rX47RegitbqRGr6O_rFG6KM6cBy2_IIDvCUbGGrrou-rDbfz40guyLqVyiiBY0XGBxGcpzgHWkmMGwP1hg7QCGHxV6XD2Q5uGwGCo7kMkKgklD-4x8ZSvVLPmhnfmjE0T61r6EtKZDdFkq46DvN6qVBrb6mFJJ3Y2bO62TS6Oe2HHiO9KlS3aoIpDKoAPA6-OZikY9zp67_Vv2udhNUIXtGWOed3t1Vi4NJ2krsZuPrGEw06NOpC3KLGor_KzYstXzWJOEbNX4J1aFbgblTzDiIYMqj6eJU-BFMwMuh9ZJPqalV6jYR22dCyU9T73Qol9CEMYR4nv287YfdeHCcE4RRtPvxFDvFfiZ2Ls5booYuIvn_z08mx2nsdKGvmrw0D_Mm1T-MSg47Q1XUHvDanDC9RcbS9VTu5hdYBGwyhoN8DzBjVrEvAKE4wI0FQ_9f1_l5zA82fUDL1Hayuw4FkGP85iN-YeAFF8Twxr_jn0ZdQOp9AhyLDu833o1J-_v5-zh_YV1nw61vSpgNCQUMU2LyYWMf0kDzDLqhDhpU304jcbsrOHtldUmfFyKx-MMDdmfRjOdIP4vOGtav66wEHycwVdtbbwq5xHGYax75HHAI4bAB4vRgJLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: با تصویب مصوبهٔ حمل یک‌سرهٔ کالا در هیئت دولت، مرزهای کشور تنها محل گذر کالا خواهند بود و تشریفات اصلی گمرکی در داخل کشور انجام می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/467047" target="_blank">📅 14:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467046">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gECFkzfMJ3A32AOOJokTYcjFSVB1o0Vw2by0d3eWDbUODXi97CqlgSjmcSYjSBbizC2pOfGAWjpMJ3C2pke_4vjj1L6nq7lMTqEElC5Pz6Vo6gOxBExfeIRctBxa2E4LSX5_ANCn1tLXk9VCxOLpxOrCDVm5_pvPJyDBxJhyJA5TmJBft3Td1bd_RPy1EOo29RzmNLtrLBJUeOyouVzjx4ccf59ywcKecF1l8ERPahZfM9N8OtRC2l4vUnqWNetmK90vTFdJXLJxQsDqV7wD-o1EYFUaGeg53OR0idhuJxQXXuGYEgjDSfc1d2jraMcNymIgw1cXlWteNRPicZGHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نخستین مرکز دانشگاهی تشخیص و درمان سرطان کودکان کشور افتتاح شد  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/467046" target="_blank">📅 13:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467045">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345eeb05db.mp4?token=mi_q2L2XNpuHq313KwTKww0FjHdlNgw9ZeYGVi1Sn7Tis8xGNWgLES1szxdZTUYIE5XGsK5a7vIxUJQU6cirTJpdkk1R4rNWC5s0u-iRGorFIyLAW87DZyd446TmjdK2hEEBafgICzZJbV86vUXnQBGOGMEBKPj_36cRT90ogRk-skzx0DcnrluNvTs2Qzn--W2rDkl8yxLwSfABtNcEMbQkb5LPMJgUsPiheuV4uPF6_CHHUAE381T1jHxqaJRQUGKx-en92B3YZgZ8d-bJ_WtQkZOoh6RkLpk75kX7X0XrVWOjrwIaCTKcPAPHS5meL2oPQK-JphDIrQ1iWgsnhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345eeb05db.mp4?token=mi_q2L2XNpuHq313KwTKww0FjHdlNgw9ZeYGVi1Sn7Tis8xGNWgLES1szxdZTUYIE5XGsK5a7vIxUJQU6cirTJpdkk1R4rNWC5s0u-iRGorFIyLAW87DZyd446TmjdK2hEEBafgICzZJbV86vUXnQBGOGMEBKPj_36cRT90ogRk-skzx0DcnrluNvTs2Qzn--W2rDkl8yxLwSfABtNcEMbQkb5LPMJgUsPiheuV4uPF6_CHHUAE381T1jHxqaJRQUGKx-en92B3YZgZ8d-bJ_WtQkZOoh6RkLpk75kX7X0XrVWOjrwIaCTKcPAPHS5meL2oPQK-JphDIrQ1iWgsnhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🖼
سخنگوی شهرداری تهران: روز گذشته و همزمان با شروع طرح چشم‌روشنی حساب ٣٣ هزار مادر تهرانی در پلتفرم شهرزاد شارژ شد.  ‏
🔹
از روزگذشته تاکنون ٨ هزار مادر وارد شهرزاد شده و هدیهٔ خود را دریافت کرده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/467045" target="_blank">📅 13:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467044">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">احتمال شنیدن صدای انفجار و تیراندازی در مرز مهران
🔹
فرماندار مهران: رزمایش آمادگی نیروهای مرزبانی عراق امروز ساعت ۱۶ در مرز مهران و داخل خاک عراق برگزار خواهد شد؛ احتمال شنیدن صدای انفجار و تیراندازی ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/467044" target="_blank">📅 13:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467043">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlbqgUR_1VYyqRD6Ryq2W-K4lItdCDiwqb2H_6VIEqH7hrGFwzZqwrEMHFKS8CfT-KQ-Nci99X4FbRd8myxlquIgJ4OSf_I9TJxzU0vWsi9epzcX5VfPBD6zoajoIF_WtTfnJo6MYaoycOUpsXK1F3vp5whTQqZ1OSvwXeHFOC9YBmZDL_WRwIy_NIfXhVxf-afQJsOidLfbStvo2qYyoQy2JJoeBJ8QQi2QdRMP09WCd3Qg718kQqI_foeddSQcUltjPGzgmQShmDzJte1ZfNwIQwN4aI982PNNMoWyupxZr6S2eUvKz7AHzrXmcsRrMHRp0N5aXryDy8F8-x0m-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ماجرای طرح هدیۀ ماهانه ۳.۵ تا ۴ میلیون به نوزادان متولد ۱۴۰۵ تهرانی چیست؟
🔹
شهردار تهران: اعتبار خرید، خدمات فرهنگی و سلامت و بهداشت به نوزادان متولد ۱۴۰۵ تهرانی تحت عنوان طرح «چشم‌روشنی» اختصاص داده ‌شده ‌است.
🔹
اعتبار پایۀ این طرح ماهانه ۳ میلیون و ۵۰۰…</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/467043" target="_blank">📅 13:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467042">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌  عضو دفتر سیاسی انصارالله: بعید می‌دانیم ترکیه و پاکستان مستقیما وارد جنگ یمن شوند
🔹
البخیتی: تلاش می‌کنیم روابط دوستانه‌ای بین کشورهای عربی و اسلامی وجود داشته باشد اما دخالت خارجی در امور یمن را نیز نمی‌پذیریم. @Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/467042" target="_blank">📅 13:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467041">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در پایتخت عربستان و توقف پروازهای فرودگاه ریاض خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/467041" target="_blank">📅 13:16 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
