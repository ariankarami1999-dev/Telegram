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
<img src="https://cdn4.telesco.pe/file/bsefD64zyA_telpyIfSw1n9i2_-5OwxYgsMAAAKWErA-umviJEOkebZILHe6RU5gOW2jx2GOOwRRD6SQg6nheD6wqsxu9E7Co-NVCgea7Suk-oFjFiPYgmb0vi1MW0oH1P_x7NfMtTTpfY-Bqzi3XoekBw-S51qFrs2ehtnTct5TtOVQ1yF5RJitI252DYc2ib8aJR3rxPdAfnnBc9PVBuPe5pnJudlsL9pIX10WXNNaHZf_JKaMBk-miAU2K33I9NhI_W-KnP2F4XlsqMNsWM0Di7t7He3VbceEk9T-LMOjnjwhLBvfuGbEjSzHC5M03Z5c_cN8MEPSryIx4RcDMQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 18:06:42</div>
<hr>

<div class="tg-post" id="msg-442076">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjI7621oE3eUvWM4bC89NIVgFzQjyFugtEWgOKgyZWPk3y_17oiuqcoB2Uk80iIVOvXqWXUOHaxy7tFENKPkyV9wkcDPMSRYJKVjJrvWgiMnzen5FAoRtnWiaOuMpSJzz8-8EN-txvzn8XiG2uXEJmoxv9rlZ0mM9nLA_DUdsons_KDbKyXWOy3uE81hjPNwTWjsHyFuh5K8Zl9oobWeuAFrOOuVzhzcfoeoZqMZ30kr9DAlDVOYnQC6cwu42aOe_YiDnNpoSj9bbLPkNbYAkmQ445RipzXgitwJCwDbgNAY1TgSBP1NmxEWMtgXgTUnUyDsTa9Ww8Ux5fobWR5tqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌فروش جدید سایپا از سه‌شنبه
🔹
سایپا اعلام کرد از ساعت ۱۰ صبح سه‌شنبه ۲۶ خرداد، طرح فروش مشارکت در تولید دو محصول «پارس نوآ» و «کوییک GX-L» را ویژه متقاضیان طرح عادی آغاز می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/farsna/442076" target="_blank">📅 18:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442075">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آماده‌باش صهیونیست‌ها برای حملات موشکی ایران
🔹
ارتش رژیم صهیونیستی اعلام کرد در پی حملهٔ ساعتی پیش به ضاحیه بیروت، خود را برای حملات موشکی ایران آماده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/farsna/442075" target="_blank">📅 17:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442073">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVpStclVXoJmNALLvWRgagBpPAvL9p3yodJnecrPdIiZbjIexTR1qntQlbNSqqPF7_PR1OC63bh1tMjXbBFVOw5tP_HCGLsrcPsZ2hVHt8zWceKOIZAt6WIknwWFmS3_QqI1qZaKjIZvdWjvVfTVP-o-D8jnbeE-D8evRrL1Wz__KYM42kOa7QmZi_G4nAaArJlg038wxToAJWslYY7sPkXrABfz3yU1RgvOHpfK3AkgdPl16oLd8JtU2MSAI2wXbJZQeOGizsY1FkwY4VP4I0UKMggRNe0Droz5dZS0Sb0lci8mZ9GVES0ni2lV1A2scBiqaKZ60UOI-a_3zzfz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو شهر ایران در فهرست گرم‌ترین شهرهای جهان
🔹
امیدیه در خوزستان با ثبت دمای ۴۶.۴ درجه و ایرانشهر در سیستان‌وبلوچستان، با ثبت دمای ۴۶.۳ درجه در جایگاه ششم و هشتم فهرست گرم‌ترین شهرهای جهان قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/442073" target="_blank">📅 17:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442062">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آخرین جزئیات مذاکرات غیرمستقیم قبل از حملهٔ رژیم صهیونیستی به ضاحیه/ حضور تیم قطری در تهران
🔹
یک منبع نزدیک به تیم مذاکره‌کننده ایران، ساعاتی پیش از حملهٔ رژیم صهیونیستی به ضاحیه بیروت، آخرین جزئیات از روند مذاکرات غیرمستقیم با آمریکا را تشریح کرد.
🔹
براساس این گزارش، تیم قطری هم‌اکنون در تهران حضور دارد و ایران بندهای موردنظر خود را همراه با جزئیات دقیق مدنظرش، از طریق همین تیم قطری به طرف مقابل منتقل می‌کند.
🔹
او با تأکید بر اینکه هنوز هیچ چیزی نهایی نشده، در خصوص فراز و فرودهای مسیر مذاکره گفت: «حتی اگر در روند مذاکره پیش و پس برویم و به عقب برگردیم، شرط اساسی ایران این است که در پایان، تمام موارد مدنظرش به طور کامل لحاظ شود.»
🔹
او افزود: حتی در صورت اعمال همه نظرات ایران قطعاً در زمان اعلامی ترامپ هیچ توافقی امضا نخواهد شد.
🔸
گفتنی است این اظهارات پیش از حملات اخیر رژیم صهیونیستی به منطقهٔ ضاحیه بیان شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/442062" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442061">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58da26d3a4.mp4?token=XQUfOS_sATGsMs9TsPlymvRvc5robx-J7cB34XXdUx9cW_KLyNE6_lHwKcfcQUjGZnDgbO5A5HOVvQNYRggj08E3VdzmY9VKUP8V282Phm3oju21QPPS2C0eiA6N5nr894O4k7Q48XpRxmfgCAMNlkLHL1cJUF172lOGobq-hpz7Uu2vOVG0wft9ri8JFbMOvepxLAuyOXEjYOrpmhPQ-lgB-mAZbzb-34gFkf4KJ1XHv947oYY6xqrVFVIKQoSHX1FqNzz-gfDceGqXdUVRlemcxL0FNa4W9mb36Q9pCcv4MrFqEp-RRWEfIoDKQlE7y8wGbB9puapv9bn1_I090g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58da26d3a4.mp4?token=XQUfOS_sATGsMs9TsPlymvRvc5robx-J7cB34XXdUx9cW_KLyNE6_lHwKcfcQUjGZnDgbO5A5HOVvQNYRggj08E3VdzmY9VKUP8V282Phm3oju21QPPS2C0eiA6N5nr894O4k7Q48XpRxmfgCAMNlkLHL1cJUF172lOGobq-hpz7Uu2vOVG0wft9ri8JFbMOvepxLAuyOXEjYOrpmhPQ-lgB-mAZbzb-34gFkf4KJ1XHv947oYY6xqrVFVIKQoSHX1FqNzz-gfDceGqXdUVRlemcxL0FNa4W9mb36Q9pCcv4MrFqEp-RRWEfIoDKQlE7y8wGbB9puapv9bn1_I090g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در میدان تایمز نیویورک
🔹
آشوب‌های خیابانی در نیویورک پس از پیروزی تیم بسکتبال نیکس همچنان ادامه دارد.
🔹
پلیس تایید کرد که یک جوان ۱۷ ساله در این تیراندازی‌ها زخمی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/442061" target="_blank">📅 17:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442060">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1c7b7a76.mp4?token=QKcNukff4ff0387WWTOTmyZTL1dFQnbhWH7fYnCNPxGW7nbTfmSg4iiB2XUJgdw7ndvh_6pKV1PrcTz9-nd1QLSY-YrpJCo1e7vblfsXZkTW3lV6OVXCWBd9YmSaur9NEfa8t5vQq1utPOojc5aBsLdkgIk8xdEPxe-OeXwmqu3eExRndUXRtBCijEmCd8Z7plYNss1Bj7us7V-ECsgD9lmDcM9zhtyul_G5WqAP1kjYiHHyYq9TzQef_tWJjsZPrGQBNiWQeuYNqS4D-Rtu-2wcswsz8bKUtG-gFVY0-bwVYLsU3Rmeably-PVanq9Q2RvzViUUG0RqWbftPx4ANQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1c7b7a76.mp4?token=QKcNukff4ff0387WWTOTmyZTL1dFQnbhWH7fYnCNPxGW7nbTfmSg4iiB2XUJgdw7ndvh_6pKV1PrcTz9-nd1QLSY-YrpJCo1e7vblfsXZkTW3lV6OVXCWBd9YmSaur9NEfa8t5vQq1utPOojc5aBsLdkgIk8xdEPxe-OeXwmqu3eExRndUXRtBCijEmCd8Z7plYNss1Bj7us7V-ECsgD9lmDcM9zhtyul_G5WqAP1kjYiHHyYq9TzQef_tWJjsZPrGQBNiWQeuYNqS4D-Rtu-2wcswsz8bKUtG-gFVY0-bwVYLsU3Rmeably-PVanq9Q2RvzViUUG0RqWbftPx4ANQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم حضرت عباس(ع) در
آستانه حلول ماه محرم
@Fars_plus</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/442060" target="_blank">📅 17:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442059">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎥
بستنی فروشی که مدافع اصلی تیم ملی فوتبال شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/442059" target="_blank">📅 17:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442058">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh2mgjbDhwWOA55WEJPq_zzJQ0GrzC9EvTi1HDXDt8qbqQZYCC3g2l26B9aaqJB5uEE6p2O2hHacpGPe9o0NiKMuv5nMKEFvi1tZu7kSoWBq_6Nl_GRTI7ciDFkdfVDmnKLl6nRiu_BCc75GGDLjtNNb2PUxRujfGUgXNhrUbqIVRDtUYrnUYZjpTCfGqu1m83dweT8hHLfSsS-N3CEIetXYzo0jlSXXNhsmOil2noZbm2MIzT2zgzmJ37MM78stxlQseAiicw2QqijuZh7JNydtXiyoPDEC1UsUFXKU9X7Cc6vMKpB4BfHx6Z3UjE2I6xq7znozZcqjo928X2XUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
ادعای شبکهٔ ۱۲ رژیم صهیونیستی: هدف حمله به ضاحیه فرمانده واحد ارتباطات حزب‌الله بود.  @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/442058" target="_blank">📅 17:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442057">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndf-As8iAg5WKVtgy7OKDNNSByE8CJPn9_JBePrd4Rq_qS_GbhcwpFSW01MuuyXbeeNiNya3jW-QkBYfb4X4lFBqtTj522y9puOxboJUcR7qFlFKcYrGblnfCmj35Ex4OXyS9dXNtoPb6kPg8jRrERr5y0fxPp0NlNYInD8t9nHIWQEFjK3ECtc3iqyON4JvD-ZfrpBzv5biG9awwHkdfmUGcPiVKPpRmzArCfJ2Ip3D8mW5EMUNWdRfDeP_tT_cGAnjodhIV2roXd2vbKa5oXiCLMk8RtNHRpv4D1Pb0yhU_6ZngJezDFh9-HBV-QY9ifDBRDFI26Jms8fQ3EaJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حراج شمش طلا سه‌شنبه برگزار می‌شود
🔹
مرکز مبادلۀ ایران اعلام کرد صدوپنجاهمین حراج شمش طلا سه‌شنبه ۲۶ خرداد از ساعت ۱۴ تا ۱۷ برگزار خواهد شد.
🔹
قیمت پایه شمش‌ها در روز حراج اعلام می‌شود و معاملات به‌صورت حضوری و نقدی انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/442057" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df5L25xlKwm5vNazPUDjMW04NanvbYMGuSKDitwoUnQokI9xGtk_QYs_fDse3zoiP5uS8BMhfPuHgFSn3v0yuzxsC6lIN5LWIaaSIUox4IVC_l5sC6LX2MIpj9_d3DdR_tVYT4PQnACH0F3qbVDuk6P1rpG4uUZ-g4TygIHqAsMofgI9Df5PBXamfKEJoRvqQskQvrMvIecnuqDyHJTukzXxou8pwSMkumwbezntAJSOguuqbRXDO1nuQEdHhNGNJT5wjj2CJRmwHG0IywXZThutbTSrRtGhB7qFfWozTMT-qZ08Ctq8PnzL9OfItqPfvIaUa0jsqJ6W2Z-wGMmF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در بندرعباس
🔹
سپاه هرمزگان: روز دوشنبه ۲۵ خرداد، عملیات انهدام مهمات عمل‌نکرده در بندرعباس از ساعت ۸ صبح تا حوالی عصر انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442055" target="_blank">📅 16:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442054">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌‌ آمار اولیهٔ دفاع مدنی لبنان از حمله به ضاحیه: ۳ نفر شهید و ۶ نفر دیگر زخمی شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442054" target="_blank">📅 16:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پلیس: فریب فروشندگان سؤالات سمپاد را نخورید
🔹
رئیس پلیس فتا با هشدار به دانش‌آموزان و خانواده‌ها اعلام کرد هرگونه ادعا دربارۀ فروش سؤالات یا کلید آزمون سمپاد، کلاهبرداری و فریبکاری است.
🔹
کلاهبرداران مبالغی دریافت می‌کنند اما در نهایت یا هیچ سؤالی ارسال نمی‌کنند یا سؤالات سال‌های گذشته را در اختیار خریداران قرار می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442053" target="_blank">📅 16:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442052">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwh6gz3WBXUEC9wHRu7yf_URU2X9yJDXp5GGSydgyOttaBdOFxL0nS0ZkNSlIctDuwVm_L-XBSPDES4Fc0K3ZldzRwyBzTIlJWbg9k7Jrt4vLy2h5p5HpnQiBH-FRQ6Acsxw65oM0u1hK2I2b_cVNyqw4X3cgmRmjYeVBRHa_ja7_PcxlN9CcZjWCEWuXX23_rMuASt8vUW1uD93MFGmX-fFKlDsP2oqoMCFNKE3vOWbKgEbXtxkjLpD9oQoqiqfsRi-Dtr4Ny8Oom6blloWkNm76tJjIYLccdnL7x-oTEUNYn-sxRnYyvZ_b7-FVnj70psPpOpVy1SbB2Npswil_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات وام جدید بازنشستگان تأمین‌اجتماعی
🔹
مدیرعامل تأمین‌اجتماعی از آغاز ثبت‌نام وام قرض‌الحسنۀ ۶۰ میلیون تومانی بازنشستگان و مستمری‌بگیران از تیرماه خبر داد.
🔹
حدود ۳۴۰ هزار نفر مشمول دریافت این تسهیلات خواهند شد و بازپرداخت آن با کارمزد ۴ درصد و اقساط ۲۴ ماهه از محل حقوق بازنشستگان انجام می‌شود.
🔹
ثبت‌نام متقاضیان از طریق کانون‌های بازنشستگی استان‌ها و شهرها انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442052" target="_blank">📅 16:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442051">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
🔴
خبرنگار آکسیوس و شبکهٔ ۱۲ رژیم صهیونیستی: اسرائیل پیش‌از حمله به بیروت، به آمریکا اطلاع داد. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442051" target="_blank">📅 16:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442050">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌ ‌
🔴
قالیباف خطاب به آمریکا: با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است.  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/442050" target="_blank">📅 16:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442049">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
قالیباف: تجاوز صهیونیست‌ها به ضاحیه بار دیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را.  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442049" target="_blank">📅 16:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442048">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
قالیباف: تجاوز صهیونیست‌ها به ضاحیه بار دیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442048" target="_blank">📅 16:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442047">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca63c77fc3.mp4?token=I7bYIjSDZSjYbgs7ypvD68cpHsXmnWY5dGBT5cBT8bHK4LxoTT35_GMMassBz0H26LKcR1egWcFJLkW3G7mJVHDa7QacM1NXoVGmfTXtP3Q55fO3W8V_narywf3Y1ejXJwxE07GghBsqZh6IiJMIMihgWFTXxsy9NEMkLp5zw98YhgB1V4UIHsdgwkwsrXGGWMpX3m7Zx5PnW5GpIb2-IwH1GT0-tRPSROSkeZIXZl2ZrWrXkJC7OcpgPZqjPupbipVkEiYmezj8DCXMmQGhffFqqyvODGmt31NjfZYi3BnrhzGV54t3LRo8w0YXxf9ETw-WpWh1LKgUsisyj5RdHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca63c77fc3.mp4?token=I7bYIjSDZSjYbgs7ypvD68cpHsXmnWY5dGBT5cBT8bHK4LxoTT35_GMMassBz0H26LKcR1egWcFJLkW3G7mJVHDa7QacM1NXoVGmfTXtP3Q55fO3W8V_narywf3Y1ejXJwxE07GghBsqZh6IiJMIMihgWFTXxsy9NEMkLp5zw98YhgB1V4UIHsdgwkwsrXGGWMpX3m7Zx5PnW5GpIb2-IwH1GT0-tRPSROSkeZIXZl2ZrWrXkJC7OcpgPZqjPupbipVkEiYmezj8DCXMmQGhffFqqyvODGmt31NjfZYi3BnrhzGV54t3LRo8w0YXxf9ETw-WpWh1LKgUsisyj5RdHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه سقوط هواپیمای نظامی هند
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442047" target="_blank">📅 16:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442046">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX8v4vPAvZVT0pOpX-QvMTwGOk4a_cRnIw0ZITzzE6SDR52zysuntL3xezI-NXHezpUh3emBOeJYU7BlRl63e-jk3GM7iXRBonWz973_hSqX_y8gGqFtft9eFqf5ca69shU-RpnSrCdMWOn8N2rZMkIAY8G3uhHUCU1Drlyt9rxaROR6evc_4kBl0c_yuBQ4nCgljZsvUFXxzlQZOcke8wcrNUBJcgdnjUWxzZ3Y8wL_2_VfAvB9Ga4ygSfi-RA8oU4O7eN3GEcjZCw-B4Rl1y1FfKgh3JxGawz9JLv2GIrzNUNQHBP0zLO7LTsqMzzh81idV4q4_MVj5diIpJJw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متروی تهران به بیمارستان‌ها متصل می‌شود
🔹
مدیرعامل متروی تهران از اجرای طرح اتصال خطوط مترو به مراکز درمانی خبر داد و گفت نخستین پروژه، اتصال خط ۷ مترو به مجتمع بیمارستانی امام خمینی(ره) است و احتمالا این مسیر تا پایان سال به بهره‌برداری برسد.
🔹
این اقدام می‌تواند در شرایط بحرانی مانند زلزله، حوادث گسترده یا ترافیک سنگین، امدادرسانی را تسریع کند.
عکس: شایان محرابی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/442046" target="_blank">📅 15:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442045">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
تصاویر منتشرشده توسط ارتش رژیم صهیونیستی از لحظهٔ حمله به ضاحیهٔ بیروت  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442045" target="_blank">📅 15:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442044">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81128e890.mp4?token=Cp7Pzn20cryETvf_JvwWf8ivMzWVFgx6Y3nLleJ52QMK7Phm6hiVuAXQuoaWpotyevgT5tqHNnMgp7sx7FrOUzQL1R2X23XOCoEqwFj4KSIP9ouA1hRC2jdNQaMOli8ZiuG-q6t6-sFB4AWGgJcHr79ovDH_-6iOoc-Omg-DjjExFpWpt8RBPB6t2vBP_yMAq7NpcnH_8ltdThsIFAl0qutCOHHUaWi0jfFz5TnDn0SGOuzlCGkntGzGdbgpAxo3l5vCjq6jCmxAZ66RV6vRkohL2ut7U8Yq5D92J_PBGnjfp2WHSgtijqBK3peTHq07Mhb41Y86WbAhVVEYuOBd4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81128e890.mp4?token=Cp7Pzn20cryETvf_JvwWf8ivMzWVFgx6Y3nLleJ52QMK7Phm6hiVuAXQuoaWpotyevgT5tqHNnMgp7sx7FrOUzQL1R2X23XOCoEqwFj4KSIP9ouA1hRC2jdNQaMOli8ZiuG-q6t6-sFB4AWGgJcHr79ovDH_-6iOoc-Omg-DjjExFpWpt8RBPB6t2vBP_yMAq7NpcnH_8ltdThsIFAl0qutCOHHUaWi0jfFz5TnDn0SGOuzlCGkntGzGdbgpAxo3l5vCjq6jCmxAZ66RV6vRkohL2ut7U8Yq5D92J_PBGnjfp2WHSgtijqBK3peTHq07Mhb41Y86WbAhVVEYuOBd4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«در همسایگی مرگ» زندگی کردند…
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442044" target="_blank">📅 15:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442043">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f44a4baefb.mp4?token=W5w2ihAoO0XhmIsi9km5kpsWSXQiYNz-vcvLPQKvXruCHkAh5gjvo_rOQiqIQnd0RdG3otSfGb7VXMnhJGiZ7gkMJQrRzUABWjsJCWYWgaXsMWXeNT_wlDkuF7yhbgCcl5lyDZni-4tY7kmRaTWlVietuu4KTB16DdAwXSbPgK23ZVloBfO8QWx1UpidyuacT-ffbMstpvBjxFsHUYWB87152IUPhmR3BBwD4nmQJZSkbl3OarfB9ZpVxa1pjgU_Pjcm0uuKmOpUdr37fEEIDi4XN6UCG5ipIjE_OG73IAgd7Pfdjhgkj6pqgqzat3oBxjVB2wdpVPr1QKULs6FTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f44a4baefb.mp4?token=W5w2ihAoO0XhmIsi9km5kpsWSXQiYNz-vcvLPQKvXruCHkAh5gjvo_rOQiqIQnd0RdG3otSfGb7VXMnhJGiZ7gkMJQrRzUABWjsJCWYWgaXsMWXeNT_wlDkuF7yhbgCcl5lyDZni-4tY7kmRaTWlVietuu4KTB16DdAwXSbPgK23ZVloBfO8QWx1UpidyuacT-ffbMstpvBjxFsHUYWB87152IUPhmR3BBwD4nmQJZSkbl3OarfB9ZpVxa1pjgU_Pjcm0uuKmOpUdr37fEEIDi4XN6UCG5ipIjE_OG73IAgd7Pfdjhgkj6pqgqzat3oBxjVB2wdpVPr1QKULs6FTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستگیری ۱۲۶ عضو شبکهٔ اغتشاشات و متلاشی‌شدن یک گروهک تروریستی توسط وزارت اطلاعات
🔹
وزارت اطلاعات: یک هستهٔ ۴ نفرهٔ گروهک تروریستی-تکفیری متلاشی، یک مزدور متصل به سرپل رژیم صهیونیستی و ۱۲۶ نفر از اعضای شبکهٔ اغتشاشات خيابانی دشمن در طول جنگ تحمیلی سوم دستگیر…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/442043" target="_blank">📅 15:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442036">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BupEmaAK0jbLjuhjmQEkgNlfrN8kAQJfCL8HCYJciLRFcaqUMrUXh4pmWPkF4C3fObPf3Oc4b7UfuQY6X01E6cZwF26B1gltRm4DTbtxENJtmnlIhy-SmLYolyjzlj3hE7upMLXU0de3Vg6dOafalyOw5hYftQiauv8mtP31pHyFHAjDV2_SvoKpuLxuGnxmMSWLlQQJ7bvRWq1-BCWZlpsG6Hn6SsielcbtIFxFsrnw4BfbNGVwPBiYJOefGun0ZZu15Jy_1Zmiy5DhnsbsrJfgaG2n2WIC7cLsGsFFiyvh3wZkIcgR64-EBuQge0RVAkBxURFxlSTraAyX7MVBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZci0aLMVDxWRbReQp7A9O2tYJHfd6PCcU2ALIsLNoNPwL8i6hW0zurlxfgOCMuQSmIrV690vnHG1YeyCcjbThY_YrEXNCnN4Amy20svsg08swbn3HVh1CyuPtFvVJmNC9WmsA-pNkA9oWZD4iacDMseUzTIAW2VyKxpX7B7V8-bIVvwVMw8D-9ogHytUDGv5J7b-Yleec2MYwB-NWEeCVHtYhmVP7bdl-2BYdbqYzzxh26yEn_06S4WdmzhyU-xjU7ZCGEO1_KnlFDpIwV_1RR_S9Iho-Bi_oWDnQm-d9kLkNY4ozUmFYZ0QMBhT-9tNrqejZTOIt84luRrcHda0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1ZrFOELo_k91nAi0JFVywAtO8TCGtTuSxqY8YvYA6adVntPzkHPdeSjsgSKJLfExcfyadZ06o-ytyYdWlI3C2zHnojQuM3QU-HwvHhzUik9uABZ3L_Bq1KfYMQI0sfeZK4qMqe4160RahxbCTibHgjxGApTH64U8jBms9vGHdvtUc0lM6O5QL-4WU7naOcIcPC2e8_196FOU-FxB2pIVLMja4XnjzsN47QbN7h_cAcsS9lN9DvF0B-dPJv3oHtqFpcObhPX7Oyd-VkqcUrnqus207EbEuHmoAYxO3fhF2AKBmxBILkhvX5_478gZ7ygOcRed_Z5T7Ovd4_CxUy1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YblrHCceByMEGMT3iFQJYlBPCU7d1SML-uhy5OQ1H-DzDQXulihbNiuGDeG-bi1wZbFou1dCLtxhf_FTMJ5bkY_FpdPGMdtY6AV70DQzSKIWp2V3tkFZh7RfZqOZY0oNK-xruP6l6z7LdbvnSCPbJ2OeYp4YdhMMe9VlkQKIYlP7AN-GzvDmjy7mePovfHR0n6YVeIIOt5jLVnpiMpL3VPF9Lhb3a-X80FcEkP34npcLIZQ9dOMqpf1euOd7RgypCL1ugSRtozoLRGZl0b9I49ZkRrKZHj1P3XFu2Db02Qrwg9X4h1iMe5u0ZGTuOu_y3wWJ_cJIHIldJDDZ0p1WAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agQD-KMHFZ2Xt45WKBuSeFvIZnVhZRPJWGwg_NMnevH9IGRkgC02_9_EcLMaEbLU8cAsxJbhsuTfjs4uEGK3wBeaBgcwDLHP6b0dWHlNdpwOkS056kMGklzIBpZI6LOp4gxDrZT-GbkNULGUDc4seZT6FR4cljKRMWRSeelMZyAFpjW617QR1b8p2GLhW4tR0dYZez1hxiu4LYZkFqOmTS6DsFn5heYpf802dmP_JZ3W_vYZbRQmSR5-Yrx1DN8uGtUdAjZy8pl8Yi6IHOvSs37DsSlHTKrN8KVA7HEetdnnZncZXYGXZ18H6kCWANo271isuCgQcxtNf223NipILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keLa-vg8V1MdQrwba6-lxgWZr2JeEm-gmJ0eipBhgTOL8CqGA1MzMODkZwt5MsE3zUoniXrzzBnmKIaNP-5aoJxGNMF0wMzGPqow3dDGdrKUu6BYI89lMhHolMhS-RuHg-ExO1SeTIhITol1tdARnYvf958WQ2BD7_ycrUffgaVkxOcmTvlbU3FeZiSsHlexMKzPJBO8JYdFJv_v7mCnTmvLHcdvKDWXZGAnArF0MTvaT1ElnSJ7FJdD9SIu1eu2HSsZ6PtDIeVFcaXxmEQrBv9zOysc93kEFcMWfzj5CSBcpw2W-VqmtfEt-zvhFAJ5JVzLWCvGRwsJWf0_Si4MVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gOUGXcirkxpmOQO82U85FKF2y-1INe7koNq_cI5K9Ora2J1JxAoLyb81oyZ_1rEj6dNweC7VXU0xNtmc-J1U8DLP-75m-C6yiPUa66qOcFfiruJAdb_L54zXA-GVXpPRmMluppgw0t6mvHBWQzC1PXLcm2gsCae76TdAzwapaFL_eB1nF_Eo3RCnOesH6hYq4spa15peHNkBlgXJY8C7cBeENW1a3ZK5EfieFNI3QsF6if4N2d9vCHhxhiYq1JouApzmR1j8OQ9o67HEu0_-pbHjxlXQuS8w4_ACNTzlPyuIUb8NBwa9qFAUEsEJzn_WCq7rJfHbO_qCEFKCLjhREQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روز جهانی انتقال خون
عکس‌:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/442036" target="_blank">📅 15:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442035">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ-R092lUkTXvQ0UpbKIYlpib895Rbtkh9wkMtkYYGSWSfd5JPj5pvcQhIQbLs6TtyhJxnmONkkFdRsjvyuFhxPJGwuUichw8j1ygFmUiRSKb0REiAZFxtoI_xwPLtnIIcmki7_iJBEQu9KX_MA426SFkP6Jr2N1kVEURE1mCKKyPu6P3QPUdQFUxeEqx7Enpx13yPlxIHarTgdlZGrF9XRVDWMv53U-yWjhzgtKrEHMYKb5YA8M_3jHIEZ5JeCjIDkpR0zyeDF2Qy1jvbenR3WQ0ZpJ9_aHgSXzY0KF-IKaTpca9ryNphCWnvT6xLD_eAXE7LvCp63ZQgkhj0ppAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۶۵ سلاح جنگی و شکاری در مرزهای غرب و شمال‌غرب کشور
🔹
فرمانده مرزبانی فراجا: درپی عملیات‌های هدفمند، ۵۵ سلاح جنگی و ۱۰ سلاح شکاری به‌همراه مقادیر قابل‌توجهی مهمات از قاچاقچیان در مرزهای غرب و شمال‌غرب کشور کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442035" target="_blank">📅 15:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442034">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
المیادین به نقل از رسانه‌های اسرائیلی از فعال شدن سامانه‌های پدافند هوایی در کریات شمونه بدون به صدا درآمدن آژیرهای خطر خبر داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442034" target="_blank">📅 15:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442033">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxgL21GIEe4faXVX6bOkt8aFOXuaTaqWrcKgbXt1f7HJ0ZECr2WrAA1Qrhws-cx-E7qb5lkfIX1lwSdMgSJv6dmNJSMbh94e7ZjAaA_SE5r9wLTQOWxvrDLs9AphSzjyeB8QTLO88E9Ax2wxNJyWCSzm64E_Z1PVqSdzAt7DyAaXqT6Bo7xM0VXdUPXb2kje50hwEizB-20puWZLzraFDyzjOyd-n6_TeSheJVEFfq7VX69tqDtKtkTBiYkOYYbPEl7Eonqwpk2clC6Er9uQu0thj6d2EmlY9D9lDB3_tSRE6-V6tb693EyrK9OazHLWcPk1pAU3Qo9fmXzN_iBolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۷۰۰ تن سیمان احتکار شده در یزد
🔹
فرمانده انتظامی استان یزد: ۷۰۰ تن سیمان احتکار شده در یزد کشف و دراین‌خصوص پرونده تشکیل و به همراه یک متهم تحویل اداره تعزیرات حکومتی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442033" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442032">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2Z-wbh7Ssu0DU4AFjPsErOOmanYWvBFc_M4c5NNIlhi_AFhLHSotO4OLzYW4NgLY0KvmDdA6LT4uNytGcYLvnL8YG5WWT80F2qEXuO443NnBHoplLh2d85_DfRYmMsVlBg_MGWMzDV4waw2j01mDJRkOxctN_PmR4aMATvzG0vNDZFUiuxqaRZq0ItbEfzJmF1wZibAVUzJod-sItee-PhabwuF6ZIh98MDiO9vjGDx5a295efFWpdWrCFaHf83tKhIBY_mmFSWUgdGyMG5dI-WtkDg-1zAJaaac1WrmXTZ8-F2p9HlwOGA1vs7DMUWcpjlDaAPOsBARQMv9tJvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت تولید گاز فاز ۱۱ پارس جنوبی از ۲۶ میلیون مترمکعب گذشت
🔹
شرکت نفت و گاز پارس: با ورود یازدهمین حلقه چاه موقعیت SPD11B فاز ۱۱ پارس جنوبی به مدار، ظرفیت تولید گاز غنی این فاز به بیش از ۲۶ میلیون مترمکعب در روز افزایش یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/442032" target="_blank">📅 15:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442031">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29b8cc220a.mp4?token=P8HvZ0a5q79nYd2CR4cGywXaOAZM1-st3u2uvM-xDhQBOAP3X4Tgmm9-tvqLUoENgJX2IPI-8LQMuk1tvJ9DEO5EokX6dfsBrC3uYr-KWF3vguljimljYlwXfX38u4sRnnoiNjudKrQnrjun1ZZonkX0yaC_qaovhL5dsG6ARbxrh1_Rg8pwNg5oC7qJ2vc91wS62NMak4GfDFwGcUCnZ1GkRRGsrey44lNYUjL0SQ0YAdFoYSZOK85LAtuCrg5TAtNk2LYHnz2V7s4qFBSNidTIcNZwKwLSFSDfXcOEfCexAdHARFsEyiLTZoiTxPub7LluLMMscD8MlT23XK-ieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29b8cc220a.mp4?token=P8HvZ0a5q79nYd2CR4cGywXaOAZM1-st3u2uvM-xDhQBOAP3X4Tgmm9-tvqLUoENgJX2IPI-8LQMuk1tvJ9DEO5EokX6dfsBrC3uYr-KWF3vguljimljYlwXfX38u4sRnnoiNjudKrQnrjun1ZZonkX0yaC_qaovhL5dsG6ARbxrh1_Rg8pwNg5oC7qJ2vc91wS62NMak4GfDFwGcUCnZ1GkRRGsrey44lNYUjL0SQ0YAdFoYSZOK85LAtuCrg5TAtNk2LYHnz2V7s4qFBSNidTIcNZwKwLSFSDfXcOEfCexAdHARFsEyiLTZoiTxPub7LluLMMscD8MlT23XK-ieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از شهدای هوافضا که برای اولین‌بار می‌بینید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442031" target="_blank">📅 15:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442030">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMmzgMjRFm6ONh75dAEWSodZUYNh8dVA2YaMEYXj-yrJk7AK04nq0pCIje9ZTY-2_ChYuf6AMfWRd4FutIwlS3K7KxAVg6-213KWi-EHhiObQAEc-VXkr3hUd83uyxrEgtVEjARcHAQT0Rzy1Sss_SOGPkcgSJT1ViFBrCQEtZFNvZ9WTP2oEh1IQLNiWyCjCzIfAoANoA6WkuH6kskbjLv5L-3QADf9vFIDLDgfDQ0EYKHBi3iQb_bcgB-D1ALFiHHcAhC_Hj6eb5hZ8SJi_pnFvicwg74syefLGFLSHGUvHS5Wf7HVSnwwB1Twb4NWKw5xsem-37toBBYieilpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای قوه‌قضاییه به ماجرای وام ازدواج باز شد
🔹
رئیس کمیسیون حمایت از خانواده مجلس: برخی از بانک‌ها سال گذشته کمتر از ۵۰ درصد سهمیۀ وام ازدواج و فرزندآوری خود را پرداخت کرده‌اند و سازمان بازرسی تعدادی از این بانک‌ها را به قوه‌قضاییه معرفی کرده‌است.
🔗
شرح کامل…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442030" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442029">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304e288b78.mp4?token=n1VQp-pt_0IB5Y8ALskZGnMXNb04yIhB35hLusvVimtLCSYsOHvQd1fxA4j6MDWffn3BoXA2tbbT7AH6prtcAqy-SG1H6yQMn221DrrrojapAaR6oJboqqd-BMazR2mJ59d73WG4DYfKZUoYEJiYNshhuR4688X4UBv1Sbk_2NTwFFKCZ-PnhQuBoM8xJhWXH3qIDWHSL-fMmgZni2Z9YQxzRS6tf-DqRbjanXD028GuNoIBQ_2Kv7lD1nqUEMEE8oAHdQzkpb2kyp8D0TNR-NvPMQy7o1PlnpXhVxlK5JhkrXxmNOQW9jl8ZR6dlQEfRNy7Y3iofGm0FlkAMNhiqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304e288b78.mp4?token=n1VQp-pt_0IB5Y8ALskZGnMXNb04yIhB35hLusvVimtLCSYsOHvQd1fxA4j6MDWffn3BoXA2tbbT7AH6prtcAqy-SG1H6yQMn221DrrrojapAaR6oJboqqd-BMazR2mJ59d73WG4DYfKZUoYEJiYNshhuR4688X4UBv1Sbk_2NTwFFKCZ-PnhQuBoM8xJhWXH3qIDWHSL-fMmgZni2Z9YQxzRS6tf-DqRbjanXD028GuNoIBQ_2Kv7lD1nqUEMEE8oAHdQzkpb2kyp8D0TNR-NvPMQy7o1PlnpXhVxlK5JhkrXxmNOQW9jl8ZR6dlQEfRNy7Y3iofGm0FlkAMNhiqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگۀ هرمز تا اطلاع بعدی بسته است
🔹
نهاد مدیریت آبراه خلیج فارس: تنگهٔ هرمز تا اطلاع ثانوی بسته خواهد بود. از متقاضیانی که مجوز عبور دریافت کرده‌اند تقاضا می‌شود صبور باشند و منتظر راهنمایی‌های آتی بمانند. @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/442029" target="_blank">📅 14:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442028">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClRVKm1W0L_LSfuHGeYqI1eSz1KcsMZe8Vv4_wd86kdkhZz3tLy3k6d1-j7kFTUJpNnaLWIrqkiFfybHn_BM4mxdUxr8qRchnL1O6Fulq50CIgN9v8v6-k1kaMgStpjeIKiWXxMkSsfwGRKaIJZhneecPU51-48Sou6BNn2-u6i07Xls82l2uRpz2nwsBsV87ccdMn_svyjoaVeqI9iKjkSND14RDD5ba-KKrTU8KsUWtaQXRGm1jCDpHhykCi9HpxU43mekz25SfidpJTOBvRj0kxECPv1zZWlMHbypvIGdcOLMGxXNty4z-OjkHW6urrLpCHBe40tzlIPS3Rm2PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مشتری گرامی
🔵
با سلام و احترام
🔹
حفظ کیفیت خدمات و امنیت تراکنش‌های شما اولویت اصلی ماست.
🔹
در پی بروز اختلال در برخی از زیرساخت‌های یکپارچه مشترک شبکه بانکی، به استحضار می‌رساند؛
هم‌اکنون سپهرکارت شما به طور کامل در تمامی درگاه‌های پرداخت شامل خودپردازها, دستگاه‌های کارتخوان(POS)، شبکه شتاب و سایر مجاری پرداخت قابل استفاده است.
🔵
با تشکر از صبوری و اعتماد شما
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442028" target="_blank">📅 14:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442027">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUTOF0Qj43vdswdbzIDCLoKlKUAt3Gd8HVIZq_Hvt0PXDvfGew9nDZ8sePzTgQDcpeLPq4uGwdnp8puAXsTf8umMVUwt2R1WmMuZbiV8oOlkcrNBx2kMdezlviJX6YVmRmDME-ybY5Zy3M-cQhZuB56D_rE7w6zkd4a8k0GTamj9QhD15if8XeuYynuksPxho2JaMXPKx-9VudaaWKO3uqWg-o50tvglzlzoFgIKf5D9UJEY749271OoWvZgTOt9gqMYaW3YrUw8HT8IiByqwPPTlQoGCDw5kWZzDtCJDcbjzO7sAIrw3wkm-iVsiXe7qrV6BQXBq74NBMvkzjnb4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی داغ‌تر از همیشه در پارک آبی اُپارک!
🌊
⚽
گردونه شانس ویژه جام جهانی فعال شد
جایزه بزرگ: PS5
🎮
کارت اشتراک سالیانه اُپارک
🏆
کدهای تخفیف ویژه
🎁
فقط کافیه وارد سایت بشی و گردونه رو بچرخونی.
شاید جایزه بزرگ همین الان منتظر تو باشه...
شانس خودتو امتحان کن
👇
ورود به گردانه</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442027" target="_blank">📅 14:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442026">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442026" target="_blank">📅 14:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442025">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155131f3a6.mp4?token=rfAk5kEx0s6v7YSuRhEvfF6_b8aach_ekSEVgdDmBMNz_3MQSp8zlK8WdfPNKacvoSwXNgr8N0Rq02zk-YYlY2XtpWqGyhJ2d5YUcW_2EsFqx4Cfti4DkRbNR5m5XLyfPHlUAeA8Me4vgCW63URbKV4RMLl5_IFJaWd4tYsP9SRjlRwRlt7mPF2Csaz5o66w96Z3md_4y3fKb5hpVmrqyxJtl-dTZLQRgU7mA3OeVz9jnuYwKazVgy0XsrWldIHZ-EidApdWqLkb_KqL7aU9Hs3BdH2zTStpXeNT7S_66AWTrQ2_S1idQQizSyo4wGAAUWlzCORM46IV2jDrXyIoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155131f3a6.mp4?token=rfAk5kEx0s6v7YSuRhEvfF6_b8aach_ekSEVgdDmBMNz_3MQSp8zlK8WdfPNKacvoSwXNgr8N0Rq02zk-YYlY2XtpWqGyhJ2d5YUcW_2EsFqx4Cfti4DkRbNR5m5XLyfPHlUAeA8Me4vgCW63URbKV4RMLl5_IFJaWd4tYsP9SRjlRwRlt7mPF2Csaz5o66w96Z3md_4y3fKb5hpVmrqyxJtl-dTZLQRgU7mA3OeVz9jnuYwKazVgy0XsrWldIHZ-EidApdWqLkb_KqL7aU9Hs3BdH2zTStpXeNT7S_66AWTrQ2_S1idQQizSyo4wGAAUWlzCORM46IV2jDrXyIoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
المیادین: هدف حمله در ضاحیه یک ساختمان ۵ طبقه بوده و تلفاتی هم داشته است.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/442025" target="_blank">📅 14:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442024">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/facf30ec9a.mp4?token=v27IjljHV_47wN5z3YJH2FZ1F8rTzKk-AK1N0-EI2BvR7QXTB06ynCXCD0hHrrvl0Bd9uvokewuF4ccHB1hg8KNmZkBIPuehaRLxVjoUBkzebiGzBbKoeYagk72-SMtlECblDXdxjbp5bwY2nyxPGg6HI41V1Z82vdbSJGJYteOXY7Nr4VDv7ql7mup2RQBzIAxvr7KOEA7mOtgp6oV5JTJrczHVLWdUnVgJtnzKGNJOlg1GdR0kclPCbSICheHLUH4nt02XdTLx2kMWYLgxG8A6boNszyuxs2FFLmBtpCon9eoDh3IVL-I-JDJsuONjB8-060Jy4w93ZFUik__QSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/facf30ec9a.mp4?token=v27IjljHV_47wN5z3YJH2FZ1F8rTzKk-AK1N0-EI2BvR7QXTB06ynCXCD0hHrrvl0Bd9uvokewuF4ccHB1hg8KNmZkBIPuehaRLxVjoUBkzebiGzBbKoeYagk72-SMtlECblDXdxjbp5bwY2nyxPGg6HI41V1Z82vdbSJGJYteOXY7Nr4VDv7ql7mup2RQBzIAxvr7KOEA7mOtgp6oV5JTJrczHVLWdUnVgJtnzKGNJOlg1GdR0kclPCbSICheHLUH4nt02XdTLx2kMWYLgxG8A6boNszyuxs2FFLmBtpCon9eoDh3IVL-I-JDJsuONjB8-060Jy4w93ZFUik__QSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442024" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442023">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ab3c92192.mp4?token=H3mYGRPOAgq2oEWh_gydtVSoWvhCRiBx3LSYkHrs-_ejivz0uFrOyLqhWQTGKvBsi7V50pCOq-QCaKehtCNJ4RH5tLbxCCHy3ytWytljXG9Fv1hwoOThatiYrDU4mGKrAU1wDZMOdm3CyEZHFXiNkj3tPTAVHFDzCQGFoPvBoO9QdbE8utT9AHmEfVBYYrB-WLLHDrP_zrqWEsMCSnF4a8D59_A-XxaXp-cc1nS70oZAhyuTOs9HSa1Fe6WdS-jdnVC46mpIUXo_WKeFIYq5SfT1h2hFg7ABcJGQW9nv_vvZpMHevHSfMHGRa84clownmvADUO8DmGhVy60GoA84wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ab3c92192.mp4?token=H3mYGRPOAgq2oEWh_gydtVSoWvhCRiBx3LSYkHrs-_ejivz0uFrOyLqhWQTGKvBsi7V50pCOq-QCaKehtCNJ4RH5tLbxCCHy3ytWytljXG9Fv1hwoOThatiYrDU4mGKrAU1wDZMOdm3CyEZHFXiNkj3tPTAVHFDzCQGFoPvBoO9QdbE8utT9AHmEfVBYYrB-WLLHDrP_zrqWEsMCSnF4a8D59_A-XxaXp-cc1nS70oZAhyuTOs9HSa1Fe6WdS-jdnVC46mpIUXo_WKeFIYq5SfT1h2hFg7ABcJGQW9nv_vvZpMHevHSfMHGRa84clownmvADUO8DmGhVy60GoA84wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ مشکل خدمات بانک‌های تجارت و صادرات رفع شد
🔹
شرکت ملی انفورماتیک: طبق آخرین گزارش‌ها درپی اختلالات به‌وجود آمده در ۴ بانک ملی، صادرات، تجارت و توسعه صادرات، مشکل خدمات کارت‌های بانکی بانک‌های تجارت و صادرات رفع شده و تراکنش‌ها با موفقیت درحال انجام است. …</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442023" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442022">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_C98kbQL1I_3DPK5LK1trUaxMTltAH-aa5S6nGJ2WldK40P8TftIGMruf7QgbkVkt4TsM8nySJMO45bzAtvDRXFW38vQQ1VX2MaJHG25Bj8PEgvp1EplevHXDX2q7l3Gw3_98aH1BxnIl6ZMbfUOHW996xDlVVa5yp6v7EZlrBJNzndqVa-_QTb_BTQmK37JkkHSxxygw8H5kVdxV63z4xMuDvlW_aTEF664fjR-Fmf16qSIMnIRuH2KBO_6f65Ug8wA2yhVZ0cIZ73R0CG0YnMYv9oKvykRq15qmvqte92d3mqOsGbMxK-30lj46pfOQtq_l_9onktGOwb_K_4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دستخط منتشر نشدهٔ رهبر شهید انقلاب در ابتدای قرآنی که ثواب تلاوت آن را به شهدای جنگ ۱۲ روزه هدیه کردند
🔹
بسم الله الرّحمن الرّحیم
شروع در تلاوت هدیه به ارواح طیبۀ سرداران و دانشمندان شهید در جنگ اخیر و دیگر شهیدان عزیز این واقعه در سحر.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/442022" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442017">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZWGz0dNdNGX8TNXu6uzfS71WNrXP_lvultvFJg9rQz6PH408lYG8E6cQ9RFx_KNEiUlLyk8qwM5oM2OwcL2kyZFnB7NQZ3WjsCk5bSW3quAFHGwlqda2tlogz8u_MvIlCsI8wwOHxjRKdatWWsh7NjuD5rTVVb6xLy0JXe4vzLAJT_i3psvx-BDOhv4X8W4YSAybp4FuYJ5H2tCqDSDDbc4MoZNTv6V-kJfblEDHiA71esOi2prEoDNeEIYlRPZD-Gu3CgfQ3Ft3tA_AfL-WIC50PyOWTSt9BmWi1OYGlnaPihJvWUgC9SwbNO81puOP0Mbs1S1kiucR-GmDwV4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYCU0GOYoH5XsRVZ9NSyRQV2tzAWUECfvcnrX31w7NszfIkJHtHo5QgZKfhkldIGEOp0joK3YNSHMfN52o8UOX6inRCLTkW29rCmWxx6QGPsrAR910wfPnaO-0c37BbNhPgPhiv2viRD2soEWDMgr3eGgY9Z64TCUVeZF_nEVk7yqWGf4s42cOtLOVOw_VA8c5YE-Qw-9AxAI74LfVDI5mSePZpG15mBB8WXgbFlRCSuQ1sflo0PxWovANTwSOffxkIFkjTOQmo-gj4EljwjjH4s0o6ajIZHdC78xmGy2ihinOzS6cpnbf6DRA9WybbGAiD7tp7DDH2mEh5fASuM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVlR6_VFyUYIQBBKPJi3-1Jf2nZR8GeHhBWT78g-1vNsKcA6oy0LKjnSgWQCLAHjS4fUwuKNz1p3ds-KXT8txkTJd43ki6tK3sLMmaaqAdH_U6RpqACBoq9sT-PUUk1OS7vDNcF3uGWJZ_26aagQULaFTgJHHrUGqAHe1fslexMLt_vXvA9NN68buJIWHNrMWZNwI0EIodDxcvH1IQiATOQqsshxkKpElB6qWHapM6GNBMf3FW3KEhmCs3fzpEAAKuvjPS_GHix2TBXWxJUurwt02dtsEwVS9QWXUZfIKuzGDjd7hu1K3BELMTxfkF8qdOZ00oTYQC9XVEsYkN37hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pt8FNVGWjTVw91ndmbHAYx4-q8QwpBV6qoHpSKaRA6eOaNVCi3uUnk3EaW7mN5fiw-1CR6vA8T0ujdo98zGNTm1cXJqoOZGOhGX8qX4WhoARpR2vdPTr_X-GOeTlp030wNWRi5vk4OnELxVSZsm8xrEDv7w7BptHIkpzCNS28SGBaO_T6K3j88uT2ZVkmgU3QrNEfLYqSZSckCD00h2KwStzuEEAND2DSzY2BF-T3CbnsNbhjFt04fLyESSSSm-tEkVyJG40T7fxAW5T4r7z7nXe8bd_MkaCKBdgRiwY5djn1242VW0EhXG02EgbX-zQXHNT8dnvf_PbIxPAeiEpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKUe4AoPgSIswwBI-FvSmqH7osPyIZdZFKJndU62xQu9lWOAxM9UgXWTN0Hnvx_4D0UrtEkoUWmN4-Gla_Xbe1MppA3jOZr66lECb6sIlehGATLdpodt0vY2iieHGcYVMEbe_hRbEBZKYUzDOLsIjT9rjOVNdFm2MkeHXaoVlR5Q--UlkovR7ZYgAZZDVypCLGKJx1DtFh6_0zthLJQS2I1lcrm9KVNPs61hcOND5_beRm4z2TvfO-ZpNfgAVGgybOfmY8kINvUl5jRhCqXYANnUncXDhVyAK4CMATcnelo61JqqpkFsHZPHMqhvFJyRHVQf5KqZue_R8LaJQ3oUnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حملهٔ رژیم صهیونیستی به ضاحیهٔ بیروت از نمایی دیگر  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442017" target="_blank">📅 14:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442016">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1774b9fe8.mp4?token=QeE5NT6dA-OYmJaWvxbFW9QYa7jcfLuPHaHrqdDy9zwxr_r_fpE0rr2bvEcrUJoxfb597tzfmT6QPVO94Pq9VO7lvr6xoPBAvZSlkTqPCcTXBznbSmoNbfTv04zI4Lq_2ZnYpj8VUXZoOdKkHr2qp-JUz5HwQgd_vqROPVTBs381jzMcj5mKOVRU6ZOh6YdHMKZRBAahlYVWd27kqYwJKL1-5OG3TuFx9wa-FFi8XGYXeuBDrPObanO3yI8JpOMJj3sC9qZGiqJmHAxAxwk6eeXHsQ8PeLR3ti95BvvJtJ1pZNiEIAjJAk9lcovWYXiZ3mNAvDfJCMbvpObsi-T2iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1774b9fe8.mp4?token=QeE5NT6dA-OYmJaWvxbFW9QYa7jcfLuPHaHrqdDy9zwxr_r_fpE0rr2bvEcrUJoxfb597tzfmT6QPVO94Pq9VO7lvr6xoPBAvZSlkTqPCcTXBznbSmoNbfTv04zI4Lq_2ZnYpj8VUXZoOdKkHr2qp-JUz5HwQgd_vqROPVTBs381jzMcj5mKOVRU6ZOh6YdHMKZRBAahlYVWd27kqYwJKL1-5OG3TuFx9wa-FFi8XGYXeuBDrPObanO3yI8JpOMJj3sC9qZGiqJmHAxAxwk6eeXHsQ8PeLR3ti95BvvJtJ1pZNiEIAjJAk9lcovWYXiZ3mNAvDfJCMbvpObsi-T2iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از ضاحیهٔ جنوبی بیروت پس‌از حملهٔ رژیم صهیونیستی  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442016" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442015">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e3d13594.mp4?token=Nq2egtaPGeNBuXzjTyIikCyTimGrga48cJQiHBiRdp-9zVB5OywsRoSxYtY4hmntre6uFgqyc0vuss4-nHKAyKzavjnihM5x0940jtdSMfU8c7FgFt24Joqf0V66MTKP1Ev_prNTZmd0NZDd0qgRtutFFuIlwVK9gugPN-Vv_Y7nOjW3rr70fm-b8gyhI1Xtf1rJX0zokwnLeJBRwmHmL6zt4D1txNa3-8lWgVrZN2Yu_di1TKXDP5eSV_3VvEyTdCGfBHQ9rkcJ5HpLLDNFj97V4Xrfvx0l1ZWOceWRAMIqoY5n76qjet3ua6O4KFZEOoR5HdZURe284uArPkP6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e3d13594.mp4?token=Nq2egtaPGeNBuXzjTyIikCyTimGrga48cJQiHBiRdp-9zVB5OywsRoSxYtY4hmntre6uFgqyc0vuss4-nHKAyKzavjnihM5x0940jtdSMfU8c7FgFt24Joqf0V66MTKP1Ev_prNTZmd0NZDd0qgRtutFFuIlwVK9gugPN-Vv_Y7nOjW3rr70fm-b8gyhI1Xtf1rJX0zokwnLeJBRwmHmL6zt4D1txNa3-8lWgVrZN2Yu_di1TKXDP5eSV_3VvEyTdCGfBHQ9rkcJ5HpLLDNFj97V4Xrfvx0l1ZWOceWRAMIqoY5n76qjet3ua6O4KFZEOoR5HdZURe284uArPkP6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بیانیهٔ مشترک نتانیاهو و وزیر جنگ رژیم صهیونیستی: ارتش اسرائیل هم‌اکنون در ضاحیهٔ بیروت مناطقی را هدف حمله قرار داده است.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442015" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442014">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUkm1pZoDbCNaZBPpOgW87UOP8avQVvQDPda72Ipj0E13lRHAsh9VVExmlJ6dItdpQO64jAL0X5pxCfWj1vZPS9iTgYRTrp6p6A7sqhWZe-FJnKGVPkYvNrpH_F188i7vNxk6TpLFUY3ImnVmut2NlSmwHeM08NmX3LHPT6WRz4DngFcoivnof36nYfdD6GX-5DfyE52Fn1za5ja7E0hJxiE7wCBTzOMqteEdHmaOAv4BV5qqgPbs2kylEUOTjJs42IVTZr5HHd65bQ5M_e9Swd2Wfp6djzm7sN43TOm2lvgkPmjdk1tWoXqeBCpyHtgxFJynJ3tf9A7cw28r6Tk2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عبری از حملهٔ ارتش رژیم صهیونیستی به ضاحیهٔ جنوبی بیروت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442014" target="_blank">📅 14:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442013">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW_CJK_jYk277CKzbDkszL_Dba7lF1fb3SaIywyf9y9hDO7C2QXsmcprkX-aaF_d-RjB15-gnErXsAWmqNJ9Pq6b-6W5PXkf8Ae6hfsprdR5o6y-y6PgYZ0i9y0FAjsPVBtbUsjP-m_lQBrdtYFqU3IVPuR-3t-n6u4i63Ze4g4WxmPejHUtufkIRdcCEW0IdzOi7cueloZpBrL3YcxLVS0yWxdjl5Hwafu-OGY0-VBa51zgTJZ8jvQGDi4uSztq9inkQN96Axnfui-wcJUgZ7ey1_BRbItdAYxqcsR3Nfze4a57CUZq2P2gzHhWhQ469T_yide8UBWD1MMAJnz4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عبری از حملهٔ ارتش رژیم صهیونیستی به ضاحیهٔ جنوبی بیروت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442013" target="_blank">📅 14:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442012">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دستگیری ۱۲۶ عضو شبکهٔ اغتشاشات و متلاشی‌شدن یک گروهک تروریستی توسط وزارت اطلاعات
🔹
وزارت اطلاعات: یک هستهٔ ۴ نفرهٔ گروهک تروریستی-تکفیری متلاشی، یک مزدور متصل به سرپل رژیم صهیونیستی و ۱۲۶ نفر از اعضای شبکهٔ اغتشاشات خيابانی دشمن در طول جنگ تحمیلی سوم دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442012" target="_blank">📅 14:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442011">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VV73Q5aLY-R2uWmOczf943BY92LipZipxiTdYoK4uhM-4D0DCnMfGsr2twxD-pieencA1Po-RYhFT19jHOM7vIOr4rUfu6eZpC82AGS8oPYlXvDHDdQZLyVB83qyNI3WN1BZJeFpWxupynuSFdmCmt8dCNnGc3Lds60DZvWYiD8iW4_avM8xuKzVgV17LBEKdHFR-DS3Ff6voqFnjw6w5pwcu1qc3mZGABQUKTp9cMSmRXL2AKm0QBsEXDZhQqVYoQ_9XwajdtWr-VB0j9P_sIot5QWw52ewCFmwDdBdvx6A7qEn_m_KPdmO4b72COVxLNeGf8JufYHJo0awuq2Pxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اژه‌ای: دشمن به مخدوش‌کردن وحدت و انسجام ملی چشم دوخته است
🔹
صهیونیست‌های خبیث علناً می‌گویند که منتظر خالی‌شدن خیابان‌ها از ملت مبعوث‌شدهٔ ایران هستند؛ آن‌ها این آرزو را به گور می‌برند.
🔹
وحدت ساحات در ایران اسلامی استمرار خواهد داشت؛ میدان، خیابان، دیپلماسی و رسانه؛ همه و همه در راستای ارتقای همبستگی ملی ما هستند.
🔹
همهٔ‌ مسئولان کشور متفق‌القول‌اند که در برابر دشمن نباید کوتاه آمد؛ در این رابطه هیچ اختلاف‌نظری وجود ندارد.
🔹
در اینکه ما نباید تسلیم تهیدات و فشار‌های دشمن در بخش‌های نظامی، اقتصادی و رسانه‌ای شویم همه یکصدا هستند؛ البته ممکن است در روش‌ها، اختلاف‌نظر باشد، اما در اصل مقاومت تردیدی وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/442011" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442010">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLhsQ1oDC73Obi4OoyxGNO7kzsc2eUe745FjLE-LbthlUkbqCmCxnIskP-8rEgGDG_z4YRF5FBW_sQUpl5c0FYH5hIqKID3WYobvo1ef-JewolQCEWNoYv2ZrC7n8zPZoXphNKqnwZgqGS1BgqXD-7hcgdCEOB_Mky_5zKX027huTVUlHPcgX4dJV8qBllorwOxlG2fzPwwKvrm9AH1wDlorsdGscezjeosWrcvbrqgg4Tf444TOq6nfqxG5vr29l0vcGAu5c-72b7Fph-59lLbfPjIhCGk4xlW4THM3iezlErxNHg_N1q31gRhznGsaCAQpNhy1v-OjPjgsCG_7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای ۲ مدیر دولتی غیرقانونی اعلام شد
🔹
طبق نامهٔ حسابرس دیوان محاسبات به صندوق بازنشستگی کشور، تعهد و امضای مدیرعامل‌های «شرکت آتیه صبا» و «صنایع شیر ایران» واجد اشکال قانونی است.
🔸
پیشتر دیوان محاسبات در قالب ۲ نامه به وزیر کار، نسبت به رویهٔ ناصواب انتصاب مدیرعامل‌های این ۲ شرکت اعتراض کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442010" target="_blank">📅 13:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442009">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buRbKm85KJiHOhwVwOtfgON-WOkmRkvzXWnKNQHGW4jzY4Vxr4ru3SzwX7-gy8T7hbbjmclpVL5T661jQfUJbb5RKE7RZ2KgIkRxMp2MvaRpXlxJHgO1qMHJrK_2YppRiJm4JOc9DkxLQwCtUdd7XxeKM-6L1eaL_FxrNVU24_QDMT4PKdfx_E8gAlbfsfT56RGIV8IL4Qq4zDzNHlUlRLTiimjkrXZjUgNY_f1UsucayUvdyn7VZ1_t2rY26YXEuv1wU9MikF1q3DlJai5UdAM2S0Urm__CY0nr8FYQ49OVfIId2iHcB7kMOUOPnk8U-1faCBOFxzbrbj3U2TSLoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخ قطعی برگزاری کنکور مشخص شد
🔹
رئیس سازمان سنجش: کنکور سراسری به‌همراه آزمون پذیرش دانشجومعلم پنجشنبه و جمعه ۲۹ و ۳۰ مرداد برگزار خواهد شد
🔹
بیش از یک میلیون و ۸۰ هزار نفر در کنکور سراسری و آزمون پذیرش دانشجومعلم ثبت‌نام کرده‌اند.
🔹
آزمون پذیرش دانش‌آموزان…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/442009" target="_blank">📅 13:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442002">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGE9jacaJoLtQMG_jhPStlvWaAHFii61R7S4sgYlbPfwPzDUyukCbbmRqWQ_pC8FMDjssDuXC9CR8MNjH4-xX-YMiLysF0JqMR06oczrVSQDsFHOysY52gKdG3PRA1KuY45qPraZh3pIB3wFOz0i8marlg-3LnQaXH509cgwGpgNXSlFGaw-InwpVDh5c5lNivxd-fnX7st2AdOOMzbSzHVwEEjpTmofwqYJX_VL4oDSxO34SHXirtVwHhQghcVrOitHEMRHIIU1HPBTAWhLdS-c4hclGu-nVDLxUDSTKeOcvNdOhsa3VR1JDfo4JEMIdrUgE2LDswibYBDe-A2zGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEZxvHHceiqvLf_Kg8zzNiCcbfiyWypNMzMpXcXRjrjvCyJxNHb-XUPUOnGyHRsCQjQpQHo6uiYoWMxxK845PIzXA9PjL0BQ-dQvxhgg88YDOAKgBpnn_QiOzZAK8Z3Ro4pVj1N3GUtMNCHmCcRQZTcHlug8j5Am17I6D9KBJUBaYMA5w8DQ3pAcQq2d2USEPKqM-U_wyauk8E3q8Crg6Vw2ESdOEJtb3XHZKAQXB8R47K5tGAG6l189Rvel6KDCFFe-mILOJVq5eCzkK96e58D3oSuFk8ky1fil1bfMS4ilGDnqfy8-zSzdlZroe_ajxk4oBRHx20CBtZ5byFuqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFfdPHTPfJz_x0ATBlYPLEiEiCSuycHcK505f3y8yfFXsQHbgrCFCRpUNF9vOCFgVaZOiBkIqm3_F_JEbePPkJIE7bztO7IpBrK7vveeeGl6F5-HJtq2hcsB6Ksw5-HXAuNiJ7-wtujZCeAPvacH_YEPLgCROgJ_Qa7lDSSjX_dP6mbnRitw1vH6tK9r771GI8uf_8Ux2avPy_VWXlIzc5FnBvJq3OtzbAE6oYY2c7KyPZBT-Yb3wnSb_otvY1fRID2ESSGIDZRVfOL07zO4oTmKXpFTu3xrmXhntbaNQ-Irs0AZ5F6yefINJzfEeFTFHEQsVuRURZt0YVgqvv5nIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-FAB0Jrbg64GURoHXHkTsitJC5nDEaIWFj_Kmi44jNy-cwr7gC6v3J9W-Q-v6aDjrJ58pPYdTk9k-0OqnE5YuqYmomJO8rEKoy_R-IpZtu24AalupLxf3SnG8W6a6zB3QPbsBjUztRwZuBooq4xRYPB9zQh2UxplovXFaYr5-qOU_giHrn_l7sLN8B8pZ4NOGkTgNZ3j8VjzyzyuXxxoE3zwWAfL6kvh8RzBgbFqMCYFikE8sA7IpdSt_mKBY14CtY2m3f-l9FM59lAhVNTZ6v2BfFpliwik2f4oaek2mFghZspjG4r31zzJDN_MGjqVkH-tTvwUjmQ9qA7rs8M5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HLE5bSgDYJE3ZlrViJ34g8fmuLrUmQXfWtP6U1w8ZyqonII4DPxJOWIqYGPclsXCshf4-XlM69mMRau1ZC1gL7YAESKXDlW6a-7i5kutCaCGCE2CoXnvI6uWsIargt8GV9luIuC1u9OnUbUp1-weTOEFmjad7XEsLsOpheYSoIe7L1axIUboClnL_uKMt2sAOfGE_rQhz75tILn7DtjNxyPGorrmUnolgpD8BKjl5D-w6qt2wfR1ljh7WOkYqgv-j4KHj5nFsfJ6jeOyZuDSfVgra_qFGBwCotEDU9zxlFc70f5BEGrH-p9m2iV0eHsg1Tm-P_ghnmm3VaukGBPfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8EiJ-t4l6NvqSgZLr7LR8__stg2mYaEBWwr5fKU3069HdRKYeqU6ZJaet9S3FNqxxxiqVJxqebSpejyH13KxQbVH-6q3i7nSWfCva-jzUr_ccIX0qzZVPmDh4tEOblwm1LT_GkuntwwPaxVIgABqdCydiNO3gQxZbI5o78ocDLLNBf2j2Ss0tbE-UpMse1r2napg_5rnKxH0fl_xKIMAuKOm6c6EC8SKe2CEM72Go86NdDqkFQEN9msYL3hBBeDd5KbsOdDNS7nMVpjEZFZBlJULCHhFxHhlqdBIZudzt8b8LlI_GFK6gKKpNlhkHVlA-oERo9SToekcOOp4KRDZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست مجازی مجلس با حضور وزرای آموزش‌وپرورش و علوم برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/442002" target="_blank">📅 12:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442001">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sd-8MAdOPCGu8TN4oe3EOfLqBdtdlkkx6aYnavAh-3mejwLFD5c2NHvRfsRXKl9Ybp8_NabDKEkYdhDvLX53pal2Qygf43vdQO2aE7Woxzq1LvcDrxfdoL1u7DYl01Ox3Z1Va_S_HKmw-4ELMFseBXrZIBEDLz2YJgs2cYD2VExIX4UsSsAunx0ZQuDSMe595geICr89ns1T4jN2hkpBNnExbd5bKmEFEccmyIFW_7huaXHRDNWZYwTSZJVn4cWUZ6KQ95CuUDxE_2MPmwxSYkRs_W5MrmDvD6FlcqMlEBUSXZ58Wulx8WZLF3q1oYRx-oVJQfPYu7mAbvFD9dQk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با رکورد جدیدش از ۴.۸ میلیون هم عبور کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید و مثل روزهای گذشته رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/442001" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442000">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌ زمان‌بندی امتحانات دانشگاه‌ها تغییر می‌کند
🔹
وزارت علوم: تمامی امتحانات دانشگاه‌ها و مؤسسات آموزش عالی کشور که زمان برگزاری آن‌ها با مراسم وداع و تشییع رهبر شهید انقلاب تداخل داشته باشد، به زمان دیگری موکول خواهد شد.
🔹
برنامۀ زمان‌بندی جدید متعاقباً اعلام…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/442000" target="_blank">📅 12:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441993">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txvOt0poIkEsDXlVzPf-8_LlJgQk_Ly8lOHDkk-BlAawIN_whIAqwRlbEfce6ZMAH4SqE-U4S58xFc7RQ0Eg9AfE6_bjDyhwSsp4dHNYz16_DagI2W_mUZOiUcVkKbvJspSpDDGkCR7ggBADnJiC8EKHnRbPy7hRQHNkqIzm12c1RIOg4GhJ7VOLSFTe8RBUsH4oWd69Bhi6gdHUajddnKhhPzNRHAvWM6Wa7IOq9psAeXozmAdscl7kqFVApP3HCT67MitGBbFh3id3VDZBEShL5KJYfA73QgchrLoe2Mdare_xLsQZWvc1ugNz4f33_GLANIc4qcMrSarYKFmauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGUjekvw0p77mgmIkkdodGNhhaapzaPAdY-sU-H9Mov5N_NcgDLkb3jxbt6f-BT_-mPChKKqdm3JfwuNb0DPzrPX3ySnWEKjq9En7tvu2XfcZZWjx_xT11mxvBqnlZdBiEB8pDMJjF8YLVOZBIdFs6GuhOYW_qREBHZdtx6v_2TY-xj2c6gIfYvMTo-VOcmc9W7bmZjmI4dHgBGrLLt4XJmFasDjceAomMoAz41RsW_e51wOcnvpvT6VmAoWdKg4f_Iw7XjRw7FQqYVD801CCd-3sLa0KmDVvoUO9dea3ZqxRPmtDk8Jn-OhsoNNk0fPR5aZNU5RWuA36xUyc6y48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssNjoOqrxABI_Bv66gxuMNLz1uCNBqkaxLnJ3oMnxOZFJFazTQzbUBe7_h2f3AQZJ4ETGU2dk4oLl9Bu9CMgqhi5wVtZ_gGJRic39XsSYnvykyrqJmZZx-aAA3EvXNKpec1pYMPzWVLXCklQ4HWZ-GpiyhloR5oVlcoH6IGkft6WbzP0x6ZoavKMnLV6ygh-7YzK_Kk5EEGbwHePj4EpDbPAwClGTCmEdwzHakSOOMF5rt5vt_cXQvORIaTpWmtmR5IWusXA94zJhnqBUWuBNTnMlzMkDwmvoV7K9I7MVcYMQJHe2TSYcnLrz4hdhNw8oC_NfBdE46CWITxEie9K8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H113zx7EVIU1LS5JL691VeahYHf48e4n9oCQbnkJfc7fhEzaAR253DayKUZU8W-H9Reo_7xEggRilpV664WYs7rBISkhDuSLqzFjq6PZV8DMgF7XeCxWF1EqHCpe7woYurOXCsZuyptiG4OZnRHA9wpkDQOvgo5qqjTsGHpvloG60vI9MTdUEPAgR7NRYWBJfjGdIpeBDseWmkdPPwpHijJBFvqpwUXh3igKdTbHioJJZaq-9oQ-m6L4u03i2yFW0vQwfpe5Aok1I0q66OyDNIj6mnTRZ_6FavNhWle5Zwv28tvC8G9Zpvj1rMPixLWs0wF6hodIl_Jg6ssbSP7NsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7-thi36Y3MBVW0f3lL2926ukyfL8SSKAA9IN9N08xSpVuiXKgPt9_Guo5UK8p4NZqdNTl-kB9FpFWjz5SMwZKFBALJKEaAqy0D0hq6NVYIC3seICmFcRxQ11YYkfyBl3twZSHdZiHFPcl_RVDVadQ7mr1EicmtTDfWkd-7kQJ7XDb_aTtqXkRrnohLy_B3FbW1lA3iWoEePDOzbBh7Uko8jFn9HGKyZrhZD8YEuNtpKdlMtgqcmQejqst660xDkeDK824pO6QmmqjyTYDrhbdeK0tqkHyG6wfzvwozIEpuo7t0wsMuOVsbkRlfuhklRbmDpDF-CCZ-a4LNV16x_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgTJ0ACqfbqw5I5k66xHxmaIo0De9Mai9fD-7iOJcFfxDIagxWksSXTq5B0vHM4Piwjx3NbFrL0f0EVLEB_jsO3AugtBns3dSWDXEyN9_XIKXv6CD3j2yZVNB3D0G5_aRzRuZp3rA4BAbOum04ozs8Nh2z0Wgv6t8qe3VJb7zlTBKfREXvqIw5krBxScfBlqmB-wrnMTEe6cxXv2LW-QrvkeEPOTkzlStTHHInj7HFOC1LOopploDq2f_o38sHusiztqBD0v5nhcSmEAG7K7Ou7C1j0cuMri-yQiJUlqV4UsZjRXxBqqmOB8HD77pt45XtNIb0KyY1Tt419WvIvkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDxJCcV-toH7viiIGhpXcDAWy55VNs74bWiOMn5_yQkMGjxTuJEgZF8656Hhy9dwyQLVoibwO2X_-ku8h7DYJHXzbXO7eF9l637ePnn4mkRyWT5AwG5-gkccWcxueS6v6WXJBfzDtPSgTiK5MpWq9_YaYsGGasHBVXLm2dHCdWo5xfQB-MchhLjvo0hoPlA5Ocb7ntwhkxTSW4q16IFvqS77hUgShF7R2H3apK89ryi5R9a_A4_WWeTmxDKuU3sknfPQFpN9gAqAXy9GhdlCSBKmG1A95xskm-NT9Oa0AOJ78-EczgE_nj6umVZUcBHMdlZSoQt78y_4lKwTpIIZ1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ننه میلاد در تکاپوی استقبال از محرم
🔹
بانویی که سال‌هاست در مرز شلمچه با برپایی موکب و مراسم عزاداری، خدمت به زائران و دلدادگان اهل‌بیت(ع) را به‌رسم هر سالهٔ زندگی خود تبدیل کرده است.
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/441993" target="_blank">📅 11:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441992">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa4129ee2.mp4?token=WJfAYQf8ct2KJQzYPpQ7m-b50XksDPD9cRR8g0UaR2C8c7ROX-xki6Qz-1KNiEX-rbtZg1AWp-7eyAsS2qiFrBAE9qqUzcGm-VuyzshsnSnL-LRB0hIppJZcZtDZ2WKVy2YntCx3YUdgRJ0m7uih8C1Jt4tA0UdXVqacMg4y3ybeMSu-_nLtFMQvm98g7S6N2ipu5oOHCBcCb46aEvtPr5NVFTMvv0Zrchd84jFgIGrOPNmjW0hnKJIcjOt_uKZ5iAdZg-oHGXNbs3di8VW4pQWfTMThFUahNX9UIDdsjFIEtHoSXTJW5OEKNOb7nGnIksRVOhSEvK0HRbBvm3jGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa4129ee2.mp4?token=WJfAYQf8ct2KJQzYPpQ7m-b50XksDPD9cRR8g0UaR2C8c7ROX-xki6Qz-1KNiEX-rbtZg1AWp-7eyAsS2qiFrBAE9qqUzcGm-VuyzshsnSnL-LRB0hIppJZcZtDZ2WKVy2YntCx3YUdgRJ0m7uih8C1Jt4tA0UdXVqacMg4y3ybeMSu-_nLtFMQvm98g7S6N2ipu5oOHCBcCb46aEvtPr5NVFTMvv0Zrchd84jFgIGrOPNmjW0hnKJIcjOt_uKZ5iAdZg-oHGXNbs3di8VW4pQWfTMThFUahNX9UIDdsjFIEtHoSXTJW5OEKNOb7nGnIksRVOhSEvK0HRbBvm3jGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون خرید و عضو کمیته راهبری پروژه بازسازی و نوسازی نواحی آسیب‌دیده  فولاد مبارکه:
📽
بیش از ۹۲ درصد تجهیزات بازسازی فولاد مبارکه از طریق ساخت داخل تأمین شد
▫️
آرمان امیری، از تأمین بیش از ۹۲ درصد تجهیزات موردنیاز از طریق ساخت داخل خبر داد و گفت: راهبرد بومی‌سازی و همکاری گسترده سازندگان داخلی، نقش تعیین‌کننده‌ای در تسریع بازسازی، حفظ کیفیت تجهیزات و بازگشت سریع واحدهای تولیدی به مدار بهره‌برداری ایفا کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/441992" target="_blank">📅 11:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441991">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHrjAf_edo8fB_hirN72zUqEB5IXCzKrx8Uh0wM83xLdvjWjc-JurrF2BuBRNQn1Eu-d_83poIq6u_lPXqJXrn_PjUm9y_yRlAivwfYYAhgas40Y0px982GNmuML2bhs8heQB-I-TfQ_WA06ENdGPk5tE5fNXQyBpWyNPnEQnrFTY3GUbDjVu01AJ62jxD7F2y8cL2tPtmdfrAqmQtZ7d5uKHSOcjUGZBg6zeuRdtk0Lhwmwcd28HFU2Pz1czysdee9VpkKEqf33uKTEWukrFrBOh5-N55ublzOmqiv2PhfxYTKW3Z9WLfPCmO6j7oXew214_tfIV4Eo-mviU58pYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت بیمه مرکزی با تمدید یک‌ساله مجوز قبولی اتکایی
#بیمه_البرز
بیمه مرکزی جمهوری اسلامی ایران با تمدید یک‌ساله مجوز قبولی اتکایی از داخل شرکت بیمه البرز موافقت کرد. این تمدید بر اساس ضوابط و آیین‌نامه‌های مصوب نهاد ناظر صنعت بیمه صورت گرفته است.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5046</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/441991" target="_blank">📅 11:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441990">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441990" target="_blank">📅 11:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441989">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9Yz-fzoUWbZVs11i9TKahEZvyOVPt-b5_fempcqwMoKJM_oVpbIqkVfb6DPAKMJillrL2wDDEJ3O2J5a9VBgd7Ckch3ixv8Wn6AmYSDn-m4fXCdCMUCxhiXzTmmr1mrkIHlF4nyWjdUf4m9BgirLLbWoGAOMld0ZQpUyr4o98otZSaLwtsZXQpzneaX9YgqTXt6LvNDwHI0tL5y8jY9egJ0tD3CM38GFwsrIumx65hNePeDnCtaERKjF0YVITkIOGe0xG9EEsHyvVtBnSrAisX0bjZAANjRG1tiX0OhkvlLwBN6Zm2VXkTDjbtdEiVlXW6ISAsb6oPeE_zQ7DPyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مرزبان در درگیری با گروهک‌های تروریستی
🔹
فرمانده مرزبانی آذربایجان‌غربی: ستوان سوم «حسین رسولی» از نیروهای مرزبانی هنگ مرزی چالدران در درگیری با گروهک معاند پ.ک.ک به شهادت رسید.
🔹
در جریان این درگیری، نیروهای مرزبانی موفق شدند ۲ نفر از عناصر این گروهک را به‌هلاکت برسانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441989" target="_blank">📅 11:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441988">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j02o31zF48SIRl1ifsN7JQ7ZO2zGJiK7zSN-twVUx5cBk_sONJaK6ogiPqHJ66_SeiHIGaUWj-ObWl6vhm2ozhplCc2fc6wr7-Mf99nPO8sSB2EpPSA0OZNQAcD-XuQ36ooia7M3gJq1imBdFcwHbaleyA3tbcLIJ5ud_P-11BVW7A0jko4cpEoJmreXx6Tli20jl4MEiEnEax0TzpnaWHaDVoqmF1fICBFpgNEh8vGHe8OM1ha_7slfitNpNXyZQ55qRqyY71Ynpsi6oC74V20uE9MBIEex1ti6g6p-xoBE9u_J39-GiwT0b4WQmRey_YryChFpdK_y2ic-Xn85UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزادراه شهید شوشتری تهران افتتاح شد
🔹
قطعۀ نخست آزادراه شهید شوشتری به طول ۹.۳ کیلومتر به بهره‌برداری رسید.
🔸
شهروندان می‌توانند از مسیر بزرگراه بسیج، پل هجرت و بلوار هجرت به سمت جنوب و بزرگراه امام رضا(ع) تردد کنند؛ در مسیر برگشت نیز امکان ورود از محور امام…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/441988" target="_blank">📅 11:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441987">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jY_YYP93Xp47aJbFiT-vBjIBn7JtuUOsbTrLNHSFOnuXKm76mkl8lj-F_ecxRd4rS_ToRfwki_4qCqncF9-bWfI1oH1wGaNdtDXbzuAHUZ5eytt039rEPkrZn4Z3qVCdLdlBPSI3MGbUmzI4Knci1au05VkmL0F4Mo2Mf_sG_4G7lDRo5gHELVydQnGstrnjJR86HBUlog2ET8q1sPRoe7R1wcOmqHU_BrqXy-VN1dyeefkTAmO92uKfKfJLZ53ohIpSabKTd3IQrxQr60QpLxFiaRs-VJ0igLh-YG9jSGekdq95LS7-NBMPif4KnsQk6XB_OAEcTdWGXpepsdJTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعار مشترک هیئت‌ها در محرم اعلام شد
🔹
سازمان هیئت و تشکل‌های دینی شعار مشترک هیئت‌های مذهبی در محرم ۱۴۰۵ را «در خیمۀ حسینیم، خون‌خواه و جان‌فداییم» با هشتگ
#نحن_المنتقمون
اعلام کرد.
🔹
شعاری که قرار است در کنار حفظ استقلال هیئت‌ها، پیوندی محتوایی و راهبردی میان خیمه‌های حسینی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/441987" target="_blank">📅 11:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441986">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ad505547.mp4?token=eWCKDP8wPQblqyM3HFpGBL0RVPEKNpDr1Wp_sD9DRsOyjinNB12qznzdlwBi916SSkMqdAgOypnH3nZXW6SiXjOnvCCQ9tygz5-20VQ9-stodBxTOOx1PPye-_gE1ZlwEaph6pqnyYIFStzMgjuFhqCVNfmpEgrC6_nZ-3V87vHFpKw7Gz8GL4ZOBAWLytXNXqtMs4KwsXyT8nAE1xSWDcghPKnV1UGhHCqE3z2FfNXSoy_w1L_blm9k99K-JuI0vgwO-qvYF18TnEuLcleja3NCEtPoD5Zo98dJrpx4tWQ8L8JHp_im-0pvauigNpwIS-RIenWe4UNVvuyazNkMNr5qwRjNhYw-_fm-t3VLBhPVWob0Ujw3ZaiBKFF8-UQrUno0QdFvd0ciFI21cQ7eaXCwLt80mUhD5Zn5Znut__OQV3wgqGwvDJG4WpJ9i50cgT76hnSRtVq870YrAR-5nx2tvyF95-4kqNB_typcOIYfZqpFnrq9-2G21CnKhFw7voK02cas093Y5TrxEvvUdMrgIittkXrQnJo0Bb7UuT0oZrDqVwaUfxnsg45AJrEk9Udw-3loH-Wxkj5IHDk5yWJVvA278X2DwcPfm3rDtGpGPL_hUPbcA8C6tqQdeooyp9vnX2eJWcr8c00Fxg1QurcInb-hpJgMbrjKlVQS0LM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ad505547.mp4?token=eWCKDP8wPQblqyM3HFpGBL0RVPEKNpDr1Wp_sD9DRsOyjinNB12qznzdlwBi916SSkMqdAgOypnH3nZXW6SiXjOnvCCQ9tygz5-20VQ9-stodBxTOOx1PPye-_gE1ZlwEaph6pqnyYIFStzMgjuFhqCVNfmpEgrC6_nZ-3V87vHFpKw7Gz8GL4ZOBAWLytXNXqtMs4KwsXyT8nAE1xSWDcghPKnV1UGhHCqE3z2FfNXSoy_w1L_blm9k99K-JuI0vgwO-qvYF18TnEuLcleja3NCEtPoD5Zo98dJrpx4tWQ8L8JHp_im-0pvauigNpwIS-RIenWe4UNVvuyazNkMNr5qwRjNhYw-_fm-t3VLBhPVWob0Ujw3ZaiBKFF8-UQrUno0QdFvd0ciFI21cQ7eaXCwLt80mUhD5Zn5Znut__OQV3wgqGwvDJG4WpJ9i50cgT76hnSRtVq870YrAR-5nx2tvyF95-4kqNB_typcOIYfZqpFnrq9-2G21CnKhFw7voK02cas093Y5TrxEvvUdMrgIittkXrQnJo0Bb7UuT0oZrDqVwaUfxnsg45AJrEk9Udw-3loH-Wxkj5IHDk5yWJVvA278X2DwcPfm3rDtGpGPL_hUPbcA8C6tqQdeooyp9vnX2eJWcr8c00Fxg1QurcInb-hpJgMbrjKlVQS0LM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک سال بعد از جنگ تحمیلی ۱۲ روزه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441986" target="_blank">📅 11:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441985">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌ حمله سایبری محدود به ۴ بانک
🔹
شورای هماهنگی بانک‌ها: اختلال ایجادشده در سامانه‌های بانک‌های ملی، تجارت، صادرات و توسعه صادرات ناشی از یک حمله سایبری محدود بوده است.
🔹
تیم‌های فنی بلافاصله پس از شناسایی نشانه‌های غیرعادی، اقدامات حفاظتی و پیشگیرانه لازم…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441985" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441984">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L10gMKTxTh1a7M03jd214DZ_Y12u6f61SrUZ10rop93zh1_odkp35FYFRAnJFhmOh57Cag91i3btZezrW5guCaBYhHc51fVhcqJfsRBaOCQy7h-ZnDn6jlhRpUORg2DeCNUjjl18fb_bidKHp-la0SAoYr-J1QVtXcBu-n5PvBZPlwKEER5qGDpU1QC2ipNWKpT522TlCAWGDXtZc5lGg3oL-ZlsJVWZXsmdB8CDv_o0-oCGThKBnghX0vcGkD73I4iMXXmprZGPij6PNJleLmv8NNqcNYuGtFjA7CxKNRcO6PrgdVZn60KzYJwxjq5cVvzLi638u_5iDwrqt6rrjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارتش صهیونیستی برای ساکنان حدود ۳۰ منطقه در جنوب لبنان هشدار تخلیهٔ فوری صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441984" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441983">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUp8i2oMHOrVTzYCSSy7VgvHgwjtfdrAWRBMJP6XHZxZjskA4NOsheoSDX6obY2PsI-qhLk0SavyyWKHlwlNGFuYWnHyCGgRwNSF3JYQBnDCTyKXAugcEkrT1swbeQnFOOJmwpHFQSTl3c-bp1kWDDWBEkbmBVZujTJc2uLFTJRfo_I4MdXw070xKsoL3c7pSX9CbKnBdbFTugIYPHHNQgbNffRuRrcdnXWWD34yL8IUU7n7xv-y68fJTGFi6LYuJ4r47_S6kBIdcsRY7Sfp8_eoLtunBUR3AL3co6jnQKlp-7prKkcvn8OuwPMplLNsCufE0Taag2QuM2JA-0J3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدحسن خمینی: تخریب مسئولان عالی‌رتبه کمکی به حل مسائل نمی‌کند
🔹
کشور با دعوا، اختلاف و سخنان تند به نتیجه نمی‌رسد و باید به خرد جمعی و تصمیمات کلان نظام اعتماد کرد؛ همان‌گونه که در دوران جنگ با اعتماد پیروز شدیم، در دوران صلح نیز باید با همین رویکرد پیش برویم.
🔹
تخطئه و تخریب تصمیم‌گیران عالی‌رتبۀ کشور ثمری ندارد و تصمیمات کلان نیز با تأیید و نظارت رهبر معظم انقلاب گرفته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441983" target="_blank">📅 11:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441982">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">منبع آگاه: تصمیم نهایی تهران دربارۀ تفاهم‌نامه در دست بررسی است
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده: ایران هنوز تصمیم نهایی خود دربارۀ تفاهم‌نامه پیشنهادی را اعلام نکرده است.
🔹
بررسی ابعاد سیاسی، حقوقی و فنی پیشنهادهای مطرح‌شده همچنان ادامه دارد.
🔹
با این حال، پیگیری‌های خبرنگار فارس از منابع مطلع نشان می‌دهد بررسی ابعاد مختلف پیشنهادهای مطرح‌شده همچنان در سطوح کارشناسی و تصمیم‌گیری ادامه دارد و نهادهای مسئول در حال ارزیابی دقیق جوانب سیاسی، حقوقی و فنی موضوع هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441982" target="_blank">📅 11:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441981">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNVEWwqoGeU1R__zOix3bdml2vSd3CXUFFfo__pDxdw3vDNQ4Vh09j_2gAK1R8dqep5ZsRHxf55JMgO-rUG-aK1cFt3kfHiGv3rvHLX6cFkTwoI9J8f7n37leK3bqQHAr2koln0ZrTM0s9iKJ7MjjTI6HXPcKZiWbb4JqN0ZB8soe8zZ0va3aXk_DWm1UVd-AZAPB0RCRC-Nzw13LFWqQrmVTKYo20XX135DL1iyNo5hfnqttiWgj0noNBjfsz9vAclUSUhT7QuflAmCLCuPqTLlpAJlsT6DdkO5yIZnz2E_YMsLh17NTp7IR_fKY1n7ZnMRbOY1wnnT8tZDQ2I2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اورژانس تهران: از ۸۷۰۰ مصدوم جنگ در تهران، ۹۲ درصد غیرنظامی بودند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441981" target="_blank">📅 10:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441980">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60b6373b4.mp4?token=UkUXIyFykbv9OLtA94ETklUkF10f0sg29ES8Xu_y8FWkRVkt5W13v-rq75uUKi9n988rZkVyEGHQH3tI-l9rdkUxDmljuNRZ6cEVZFrDbx97PwK7jnip1iAazCVW6oZCmp6DbDCoiYhVxDBVYeE9vhtkvbI0drZ3EEBy1Ai7vacqIRoaQYu42S7lVrhNXjyaNp3cuKmevTEhX2jf7v_-39r8RM7cyMxQ5yxsh3p7iD5umGB3TBrDAP933jWlwhRp9jf0sZiuWmS06oqibxVWMZO-FsH-XosMGsQeR7XMEvZDwlBExLSnj5DDl1e0SBxpXGKyCp1T02b5kPCDteS6lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60b6373b4.mp4?token=UkUXIyFykbv9OLtA94ETklUkF10f0sg29ES8Xu_y8FWkRVkt5W13v-rq75uUKi9n988rZkVyEGHQH3tI-l9rdkUxDmljuNRZ6cEVZFrDbx97PwK7jnip1iAazCVW6oZCmp6DbDCoiYhVxDBVYeE9vhtkvbI0drZ3EEBy1Ai7vacqIRoaQYu42S7lVrhNXjyaNp3cuKmevTEhX2jf7v_-39r8RM7cyMxQ5yxsh3p7iD5umGB3TBrDAP933jWlwhRp9jf0sZiuWmS06oqibxVWMZO-FsH-XosMGsQeR7XMEvZDwlBExLSnj5DDl1e0SBxpXGKyCp1T02b5kPCDteS6lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسابقۀ کشتی در آمریکا به میدان جنگ تبدیل شد
🔹
آمریکا از سال ۲۰۲۵ اقدام به برگزاری مسابقات کشتی آزاد تحت عنوان RAF کرده که در آن خیلی از ستاره‌های مطرح جهان هم شرکت می‌کنند.
🔹
در یکی از این دیدارها چیمایف از روسیه به دنیس از آمریکا لگد زد که منجر به درگیری نمایندگان دو تیم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441980" target="_blank">📅 10:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441979">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f0f2da19.mp4?token=e9bqwb65XtBsAY6k5nT6-ZR7m0JwV8XursU4iuiVICjc6vyOwr4v7YaPIlFuAYDn0nxwIZljav1h8mOqkMLHvXXfj7JocL1xG0YU2I8JVuyZiUHDN18MjhaFyc8HE_lVccxXLE1t25s7xhkb-V1EgQ5Bh3PobXp4qkgiZ9_bkmdBLTazryKobuqP5C-Y6U4cvNeeH1QQDvbTwYqum9Pckc_SSAScZ8bGgHWhZoJy_sFBjN97sPDGIOr67V-UmCoUsJX-efNjQSEIYiAOkTTiNWARQhQaFv3wWjhCMrnPSSMOefK6yaVBbNUTA9KjCFC7aUA45IzGz4fOX75biDSSLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f0f2da19.mp4?token=e9bqwb65XtBsAY6k5nT6-ZR7m0JwV8XursU4iuiVICjc6vyOwr4v7YaPIlFuAYDn0nxwIZljav1h8mOqkMLHvXXfj7JocL1xG0YU2I8JVuyZiUHDN18MjhaFyc8HE_lVccxXLE1t25s7xhkb-V1EgQ5Bh3PobXp4qkgiZ9_bkmdBLTazryKobuqP5C-Y6U4cvNeeH1QQDvbTwYqum9Pckc_SSAScZ8bGgHWhZoJy_sFBjN97sPDGIOr67V-UmCoUsJX-efNjQSEIYiAOkTTiNWARQhQaFv3wWjhCMrnPSSMOefK6yaVBbNUTA9KjCFC7aUA45IzGz4fOX75biDSSLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا در زمان بحران و جنگ اولین راهکار ایران، قطع اینترنت است؟
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441979" target="_blank">📅 10:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441978">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌ آموزش‌‌وپرورش: ۱۳ تا ۱۵ تیرماه احتمالا امتحانی برگزار نخواهد شد
🔹
روابط‌عمومی آموزش‌وپرورش: هنوز تصمیم قطعی در مورد تعویق یک‌‌هفته‌ای گرفته نشده، اما در بازۀ زمانی ۱۳ تا ۱۵ تیرماه احتمالاً امتحانی برگزار نخواهد شد.
🔹
اطلاعیۀ قطعی و نهایی به‌زودی اعلام می‌گردد.…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/441978" target="_blank">📅 10:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441977">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8339d1f7.mp4?token=fKkDqc7rpUBkOJSissoLs9NKy3SAci-AeckJM7I8tBc9Tb1xT9RCO9NmJURsPh4hdByOoBZdfmP3OqjFbkcvirJjkBn3O628Cy2dLV-KvJKoqMKbgKrHx2TW7Te_BmLv8XSYUqa-hF-jm-k5lOuJihj6rNIOwnWXBB2FP6rZLY99hFmVn6HsyJCHK_Dj2nsdX9XjZq8L9imsz5HD9cxqBoEh2cslzCWYl4McflwnHXWvROneDWWvKxtUAqBsSAAjz0OowqaHXawAEkqcCp8rlhbdvAckeysx7lRPjqgHRtIf5mfF4sbWZgzEB8zHsxO_NuLbTz81eveyMZT4XzySoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8339d1f7.mp4?token=fKkDqc7rpUBkOJSissoLs9NKy3SAci-AeckJM7I8tBc9Tb1xT9RCO9NmJURsPh4hdByOoBZdfmP3OqjFbkcvirJjkBn3O628Cy2dLV-KvJKoqMKbgKrHx2TW7Te_BmLv8XSYUqa-hF-jm-k5lOuJihj6rNIOwnWXBB2FP6rZLY99hFmVn6HsyJCHK_Dj2nsdX9XjZq8L9imsz5HD9cxqBoEh2cslzCWYl4McflwnHXWvROneDWWvKxtUAqBsSAAjz0OowqaHXawAEkqcCp8rlhbdvAckeysx7lRPjqgHRtIf5mfF4sbWZgzEB8zHsxO_NuLbTz81eveyMZT4XzySoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از سپهبد شهید محمد باقری در جمع خانواده
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441977" target="_blank">📅 10:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441970">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3cy9qXIrl1KnIaS3OiYcJtvTzZTUfdG76YFmY1l0DVa7WsMvRpq_ako9mTLN8HcnbFKXB0SWolGDtY5c1oppzRCJ62aJ6BNxgJ-ZqjG4YyvsWkRrIr-m6cVVdyN1IAKoyYW95AxCdmKZlGt5Ml8uzw1bvATCQ9d6DW6BR-yeUelo16Smf4AmBEedVuST-mp5cvo-iMcNnJLuO1PrpgDRlN7XFTW0tj280UlRC9VIe1aZTEjRr9kG6Fu2g_oqnwerA2g5O7js9NtxYAIjm6HswTlQRQ3CT9DQzChSd5nj54aE758M5upg3RR_JBMNACVBHLgLJR_kd0DKvC7DN1EKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Up7P_64CUZ1g85Xa6znxo0DZkopqVofWkWckttGsValtTcIr6pARBKyOcy63iPP2fuLNu9uWANE3MvsAWM0akfi-vGx-KOeVoqL0cTBVivTFKJhJfu6S_773i0_47ym2xZAdgZz4z6uRhK75dJAoU7nIdntkKibu0KWrTGUctR3cz2-Gfw1l_6j5lWAYfpeHkVGD-L5iBHnbs2koZagJYBhKFyCg__L0Jt4k8eIBk1haRh-B8kvbXukg0DVB2lOZ_DCfbTEofBdTFhBUb9r7hp7lkFtFkjDYXgxa6QLGfqdQjstAsUEcg_PNhEoy4ukGPZrQmLoArM5MOM677q65HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1-jZwRMEr_eZYwQc7I8tbRAzC3yA3v06TSyqc1nwJw_ESViUCuDSku2CyykwOQ1b8p8sbXAjlCbPI_YSbJmgoA8mQuJm7k_UGUXNn2wW_5LFLOBvHJ5FGdlCKBRNmKAabjvfMc78XzdYQeOyqEvMKNC0IvMyOhnq86LVYs51ZZm6tnSXdzIg1wtKkwQSi5PGj_w6pcY-cRwiOzpLIh0WgjgvZRUvz7EqB5TnpfSpYTcbuIBsnnCWw9x6QY72FzJnsnO9pT-4ePsJDVuOcmfhqQSOz-iMLyQELvFmI085HwP2Zp9rZed9CcnwAiqiIX0Co4823ULKgXB3Mru3IhJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLAYdDFtwMb-r2xMk3IfRwuEH-SPz01La3A_eCBKR1WbUwuMKY-7jv5Pi9jvBYGWoPBEDrMrA7NczOJOyymqykGcaXuaX4pVl8M70WMRhR7hHmI0-Ma0V3129Q74ZXYa66t4hz4JHeFdZNUctutRy5mx-vhATMIIXX2VqGaNrPyi5PTaV33PTe6fCYVYgeB_gKDT-1cUrOi4VTYAvSHhSNbE41PcfiLSYb_E2g5jutjoOCwE_pKKZGJrokydRZ2ldaVuTUM4mgHQcr36n4UQB9_XnPeQ3YdwvzdTa6LPLnjQPRxcwk4cwMRpAgusq_43a2o2KkMUYH-gD2HNUy2o7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXWqF2MZHhoF1sZbyhAHl2db5NW6FLdrMGZ7X0FY76mcmr5QF_trJzuF4oEJjOgB5CL0jGzY4Hjji2h2ZTMEujkxsOzf-_2Diu5HiG3E5B1vG-_BJyy0LLRv_MerwwEOjHgIJedmojNczZXxCZSdtIPuBqwWKnkZR_uRMg71gVI6RYCA2S-xAP7Hz0nK5ffafaxH-m9TQC6FcjoSnLvf98z4XJ-ei5jz1hhqD0jg_j9lesXaZxbw9gm8-Jcnvt827ycxJVVxVgOMKHHofgUzlqU2Ya2EQow__1_807Vf30YmP49QZotwrsiJuIwjud9yQ__exBjT9_AnTDuKCsx8-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKSvfTyO41s_6mpqb4A2NCjUToNmc3APrFKIvVP0XIms0Y5org-FPyXiEdNiVQQ6O_KzlBASiLOC-Kfax9--8FSiEIM-uHGHjuYacRmwg1omtWzDFzkCkBrIm713VpMfiu_IEgfz-quVprBfMM3x3nm84eS2bD_QyllM8VGiDWmolopd7ozwuVsBYt1LKXUVkqnP_Hee6zlFHo0DIPkG0GGTWXkdf3cLfst3-YOwZCXWxh9B1NoMRhkXNVa9WwbNCoYGB_YHCoR9IqacYC3UBUUcFQa10bm8gZ0I52j8WNjhoGKnysd2pKnsHzMrrHFhPLQ3yfsrl8M8eUVnww1P_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZJZOJLIAw2qOyCm4MtCfkKZCr9k1dcUW_oFmixMXKcspVfxJacFOZAexnF_t3-uYNyRamElqH0DTe9wyBnKYTJcVC--dhKlYsPKAHXk9rAo0tHVJWKoPrGIu2f6y-Wy6ioce6IhKUop_YOYzWNe1C-cLcemvMKxdSJaoeSWJxuMVxeFIMU9jPoc2qk1Xzfslzy-_KhuWNVCXuJldxJxHfT1pM6nVXBx6dLxSdacc8N40s9lLpSvpQdIHCtl_uMMhMF5SsK0NfCjAWOElIkRUJWvdUM3DS0DojQb7OfCeZJsOqxM9VzHr1MPNdFemoPdwPMUKIHNI5LSBVWIrMSNoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غار کرفتو کردستان؛ شاهکار باستانی ایران
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441970" target="_blank">📅 10:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441969">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f835aed46e.mp4?token=BPtKIjRIwc7BY6WQzS87InZqVU3ADHPzomrQJO8_aMeWi8pV_GFhksUMWqtENIF7OhrBI4EIRvjm5DwAd9v1zccMpwU-B6972z0XH5T1lz1KlicM1w93DVpQAXE52Bkrd3-3ovBW_DspNuNe9GlKatj8D4ofyMl0h2hZJKTls23cH-ieqEH__arx6WO9_15IGSz1audlPKmf-X50gyIF2GDt8b1bG2bFtfUuOvzeRsc4ZTywdWBf0c5AqHzm_ZYEkG7LudVDFQ9CH5InB8ZoA3RAgO3ONZ8-CpkRLkM8plArIj2qXniq9Uo_UacSmfuVO8y7py9xFbAolUUOGbKbSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f835aed46e.mp4?token=BPtKIjRIwc7BY6WQzS87InZqVU3ADHPzomrQJO8_aMeWi8pV_GFhksUMWqtENIF7OhrBI4EIRvjm5DwAd9v1zccMpwU-B6972z0XH5T1lz1KlicM1w93DVpQAXE52Bkrd3-3ovBW_DspNuNe9GlKatj8D4ofyMl0h2hZJKTls23cH-ieqEH__arx6WO9_15IGSz1audlPKmf-X50gyIF2GDt8b1bG2bFtfUuOvzeRsc4ZTywdWBf0c5AqHzm_ZYEkG7LudVDFQ9CH5InB8ZoA3RAgO3ONZ8-CpkRLkM8plArIj2qXniq9Uo_UacSmfuVO8y7py9xFbAolUUOGbKbSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هشدارهای نفوذ پهپاد در چند منطقهٔ شمال فلسطین اشغالی فعال شد  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441969" target="_blank">📅 09:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441968">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuwyt5J1ycPSG_nikzoAWz4Y3_VrY7TBYPBwXNgNzYMJLz_YnmlqU1k2Y1Ftq2XoYpN_WLsGy7E45uUNFyO_bYICQt0A34kJicHhvzzcSz4EPFcN-W9saH08ZaQtuaHfd8prohN1aOUf2xLaiFXEMHoDvUGkdjiTp2_DdtS9MKhAgWxiF0m9VfuMF9KVUyP51w_XBmytXCcLANdWJ7LpEBEGUqnND49Holpd7oVReuBcDwoiI8mGY6mTXblWnoMWFe07H9RyVw_LxuUfq29_Ze7S4cBRf_YdEFD8ISWu71V2C6f1CAbjtQ9ee9LKhiYzj5yMVo655xyQU3KuSgmUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استرالیا با شکست ترکیه همه را غافل‌گیر کرد
⚽️
استرالیا ۲ - ۰ ترکیه
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/441968" target="_blank">📅 09:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441966">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPPTXuGk_zQjo0qCNhoFXiNJmIQmXg-2BQuahjLSNi3R9UtOU8TbW-F5Q4wLYyKm2FR7iNwp2Yldn_aBixEvbEaXkrLubU9KTj41P6NsGhiXgZxuXM_C40sCrwthr8qv7oIN6E2Qv53af0fOLBHYzyxUzqNXhal-9PNtdFb5F4jO3AvSycvNr0FjkPxyn6mHWBBqrzNXidzK2yQ5n-YK0udswB6ZP2nPV3OP_t_3mKVotroT7LXVYOtFLbGjTp--txI9Z6pz0N8B67d1keXbOJx8GiIOves2pj4Ece_Pc4ZGE2LsejNjoXV8b6cTZCx-oIhLPEjbNDKEklfgL10KiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدارهای نفوذ پهپاد در چند منطقهٔ شمال فلسطین اشغالی فعال شد
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441966" target="_blank">📅 09:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugFPVGZM8NJmzDcvAudJip9hhbqrSJeol9hOu9uXDm7NAgV_cVfWiW7hENFP-FabyfpWcVpFUVnWbayaD8blIRTSHl6hPMmSt31F3LzxUfLdbZ91VbAGYlB7bT9VCDI7iy4pD_F3DaRzJ8CpNxrafcDnombPVuZBIKqdVbNoTuyGe6tk6tSA0mePlHBUmLJ7bE8nHVG5AeafR-ZsYfAAne9AB8ofMj8h4dCGJlROvT_oo9oLPJcg5JwkVGsqnxvGpQPtxfVnF6iGtOcuv6bxCoJP9DVSGvZYA_mQ7woIk-0a4z7feBQUZpzArXbFPlI1JGswAyLWXab1aNHa9z0_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEvS14a-TB3M9bHwQKH1IAHcrtR83_iOqGVLKoTLL92iF1oyGg1i05CQNJywyM_LfePJKwGW6Y9i9wxZbuZMIClePF-8mY0vgGO4U9FFEodSGqAXdSjxzXKuMzsSNEJkZMXsiMGw2hYDLSDPNCoh6niodhrHrHPPI_y25S93rij-tMAsiAjWkw9qaaNM3TZfZ0Jvz5BuUl8--jRWvy7v4UBSY2-wwjzLKhcuiKZXsYZnrTDSXRndOn3pCibOxvwqzZU1WWazwhfdd-_Lb3vpedonxWG_Yk32_DwS1yNZEbSyO8CWfvo0IdpKmUKdeIoSFOPRY_FJ45Cgzjpg55Ao1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تاج در گفت‌وگو با رسانه‌های بین‌المللی، یاد شهید ماکان نصیری را زنده کرد
🔹
مهدی تاج در حاشیۀ تمرین امروز تیم ملی، در پاسخ به سوال خبرنگار نیویورک‌تایمز دربارۀ نشان روی لباس خود «میناب ۱۶۸» گفت: همه می‌دانید ۱۶۸ کودکِ ۹ یا ۱۰ ساله که سر کلاس درس خود بودند، هدف بمباران قرار گرفتند و همگی به شهادت رسیدند.
🔹
از پسربچه‌ای به‌نام ماکان نصیری تنها یک‌جفت کفش باقی ماند؛ رسالت ما این بود که تیم‌مان با نام «میناب ۱۶۸» در جام‌جهانی شرکت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441964" target="_blank">📅 07:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441963">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkdqehdObyHiG4uDdMYWC1aLgCSuGzSS4ijVpZsNRlb53K9pgP9TCc6Mtn_Llo5zLMkXUS6RPIN73fqaLNjgNJaUw4-IDGWzDbZX9hj7oLgXdFdBQYhBBjpQQ4dm_talRnzX8oobqx0BypBL6E_77PMqfBsZwhXKVwXN0Y5r6-zSjNmV68QsklPCyyKksxAtRIAnGUHuY99cZX1MwymEeG3XUQi6USxxurzfx2J91iCClruqSAUIuaN-oZypBivmQF6i-t27gzDvFg8EYXHFhR1YeQ8NE1j5ToHfgwyrqu-OyMl7RLDV8eYjQanAnmfoIn68q5zakbIRDO-p6zUaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنایۀ موشکی تهران به واشنگتن: ارتش ایران نابود شدنی نیست
🔹
سفارت ایران در کنیا با بازنشر آمار دقیقی از انهدام رادارهای آمریکا، ادعای «نابودی ارتش ایران» سنتکام را به سخره گرفت و تأکید کرد که تنها چیز نابودشده در این میدان، آبروی ارتش آمریکاست.
🔹
بخش اصلی این توییت، افشای آماری دو هدف زمینی بود که به گفتۀ ایران کاملاً منهدم شده‌اند. سفارت ایران با قید «واقعیت ماجرا» نوشت که در جریان عملیات موشکی ایران، دو رادار حیاتی آمریکا در منطقه به «تلی از آوار» تبدیل شده‌اند:
🔸
۱. رادار ASR-1000 در پایگاه هوایی علی السالم کویت: نابود شد.
🔸
۲. رادار TPS-59 در بحرین: نابود شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/441963" target="_blank">📅 07:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441962">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌ آموزش‌‌وپرورش: ۱۳ تا ۱۵ تیرماه احتمالا امتحانی برگزار نخواهد شد
🔹
روابط‌عمومی آموزش‌وپرورش: هنوز تصمیم قطعی در مورد تعویق یک‌‌هفته‌ای گرفته نشده، اما در بازۀ زمانی ۱۳ تا ۱۵ تیرماه احتمالاً امتحانی برگزار نخواهد شد.
🔹
اطلاعیۀ قطعی و نهایی به‌زودی اعلام می‌گردد.…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/441962" target="_blank">📅 07:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441961">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">احتمال تغییر زمان امتحانات نهایی وجود دارد؟
🔹
رئیس روابط‌عمومی وزارت آموزش‌وپرورش اعلام کرد به‌دلیل همزمانی برخی امتحانات نهایی با مراسم تشییع پیکر رهبر شهید در تهران، قم و مشهد، احتمال تغییر زمان برگزاری آزمون‌ها درحال بررسی است. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/441961" target="_blank">📅 06:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441960">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDT95BX60OFMzsvdkia2Z__8Zl5P1gGgnJteuoOOtqfzkyVZC7BematBFxmnI0X6PyWp8h0MoN7lPX9pgsi7zAAiq9p2oaI98gx-gr2gMRBiXdKpo4Mn9mP3u4i6Z22JU7y1vpEMM5wSdGekj7GDkV_F6aWTVXs93fSTX7UvDuJHFpxrlh6MAzx1aIrs7HMBZj2JNcus3V1FI4JkWlRZl-3cj8HGXK99BhJDuZvLE3lqXZCpZL796htIFu6fLYa7qzHy2ZwumczjrkMTCkxOsQ95sDcoSWTQaHxcCHXU7hC1-U2SFem1yJNpRHzQ_IR3AGHVg3BvAfN9YJy4aqTbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسکاتلند با برتری ۱ بر صفر در برابر هائیتی پیروز شد
.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/441960" target="_blank">📅 06:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441959">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92f558957a.mp4?token=sQ1cLNAuSKjvCiHHp5eQ0VmH9Bxvw7ilFojvRYfQTXc39Sr0K9GzVkxFfI15C28NRcCGTDjoXCrKqXU8Cu3UPiTLO8B5yZXavwY92czNWTTFZkA1v7xlG6LC04g6519CGwh_m_gTAxh_e76svMzpVYrWC1MFeyxsTp_HBUP4W62Sd78ovSZHMcOMqTRcVkpi7AoIZ9rFl7I1VjATHeewRZHVhORU-STjHuVgqL6_f5ZglvKxZQIINPo8IwRYJIPri42nFUENN27dGf4oeC8lhTpiTgo4aRTnh_TaSgunvk7r9rMpr_rt5NVUen7NyTwHHSV8kOSwhGHcCx_wDXk_Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92f558957a.mp4?token=sQ1cLNAuSKjvCiHHp5eQ0VmH9Bxvw7ilFojvRYfQTXc39Sr0K9GzVkxFfI15C28NRcCGTDjoXCrKqXU8Cu3UPiTLO8B5yZXavwY92czNWTTFZkA1v7xlG6LC04g6519CGwh_m_gTAxh_e76svMzpVYrWC1MFeyxsTp_HBUP4W62Sd78ovSZHMcOMqTRcVkpi7AoIZ9rFl7I1VjATHeewRZHVhORU-STjHuVgqL6_f5ZglvKxZQIINPo8IwRYJIPri42nFUENN27dGf4oeC8lhTpiTgo4aRTnh_TaSgunvk7r9rMpr_rt5NVUen7NyTwHHSV8kOSwhGHcCx_wDXk_Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط هواپیمای نظامی آمریکا در ایالت واشنگتن
🔹
سقوط یک فروند هواپیمای نظامی در منطقه‌ای جنگلی در ایالت واشنگتن، به آتش‌سوزی گسترده و تخلیۀ فوری گردشگران منجر شد.
🔹
طبق اعلام منابع محلی، خلبان این هواپیما موفق شد پیش از برخورد، با صندلی نجات از آن خارج شود.
🔹
علت سقوط این هواپیمای نظامی اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441959" target="_blank">📅 06:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441958">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a18TSaWwRstszt-u29Ivq2WEWUOPYKThQWb3zdFO_EKzKEp11hT_B0Z56NGj_h61Q7R1UaXOq5ZVWSqPeCqJ94p8uKyChjlWuLiCvTL0UJ7xAyhs8E9IyFU0j0p2gpnOYST_oXW6gmmUe7fMH7jbfQrA8C13rRTiKPs9fbwUF3xTrG6XTJbzIUFZHl_-8zpgbhl3pE1dSpd8w4EYD57ZVrKqpNqzVZV4R-w7z_0VbNozZyfitxqIKcs9DdwZ8oxODehC4jRx-feqYAKXdcgZoiP2XA7Qm1tb6S5HOy6gz6qUarcZSN0hD7fC5o-vaPHY2B7zuBkG54ULROJ28-OLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۳ درصد حجاج به خانه رسیدند
🔹
رئیس سازمان حج‌وزیارت: تا پایان ۲۳ خرداد، ۹۳ درصد حجاج ایرانی به کشور بازگشته‌اند و عملیات انتقال زائران در مراحل پایانی قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441958" target="_blank">📅 05:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441957">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54ae7efe4.mp4?token=B3hoU_Wtgs_HvV6e-yVFR4LSmfJW9ouOzTD1SO8BHe_5LrIjxKNJciza8K8M2L7UteFzq6IT53d07eTiTmLbf9QhTCtnmGm10z_yb7vgsLplVoAsGcmZbbPMo2x724Gxn-3pFqlT-2CSh8LET6QgJljWCATkJUpf2w4jqbd2bElA7FPY5PsXWNDotqxT_NOqkZ3sC3cNYWF-a1bYnVnhogcv3G_gvnu85IeYRhap-RVJCw8bbx6UsgG1qoK8Sb0Hm49socoFAr_gH0a29W-Y6f8WPQNoSS_tPxhKoCLwS2jLZql2D4ZNS7lyP5zO1QE86uGWZI1cCTfRIHXowVL_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54ae7efe4.mp4?token=B3hoU_Wtgs_HvV6e-yVFR4LSmfJW9ouOzTD1SO8BHe_5LrIjxKNJciza8K8M2L7UteFzq6IT53d07eTiTmLbf9QhTCtnmGm10z_yb7vgsLplVoAsGcmZbbPMo2x724Gxn-3pFqlT-2CSh8LET6QgJljWCATkJUpf2w4jqbd2bElA7FPY5PsXWNDotqxT_NOqkZ3sC3cNYWF-a1bYnVnhogcv3G_gvnu85IeYRhap-RVJCw8bbx6UsgG1qoK8Sb0Hm49socoFAr_gH0a29W-Y6f8WPQNoSS_tPxhKoCLwS2jLZql2D4ZNS7lyP5zO1QE86uGWZI1cCTfRIHXowVL_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما از ظهور مشکلات خودمان فراری هستیم
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/441957" target="_blank">📅 05:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آژیر هشدار حملۀ پهپادی در جنوب فلسطین اشغالی به صدا درآمد. @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/441951" target="_blank">📅 04:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWTOpr7yny19wNjow4oT8d66qQ_z2-n58KNS9Wa9vxCqcGz38qJJzdobOL1-0fIJXrH7fQj7Om3FPJapd5U7Icx2HS5TlnUx4irYDvd2ChBkbwVhBEkH414dkcJtEd6ExRuDFzq_o9f5wqgl1_KNu8LThF7Lvjpe5mQqS2KpSTeAeJpI-xbJV6uMwIV4zqjS-TdGvxsY3GvWD1ewIUmZ_nblbsYhJ68dv6w1yyhTAYvlfsl7AMXSMAMd1P6rUAnvbSgj_YL9Pq-pp9rwXnt3lWSjYrlVQ8H4BkFSpdCdVdSosa6UmdKskJZBymlzLC5wJrrEm6R-XmJYTNAlePTj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژیر هشدار حملۀ پهپادی در جنوب فلسطین اشغالی به صدا درآمد.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/441945" target="_blank">📅 04:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLskYtia2cuqzFab3cL55lEsqWHDKd8uYg70H8dPFYpEOnHMOcMoTgeVqJWU6o7nob41OVmowDorXON5zqQzFlJCSK5SbdwgI_ruStvTj5NK0dve9YMIboFps0milOTRF7qAE4tSEJfnmIW8aMikcvDyhMh3a6t2LRMERW5ypApfo2ks452eFGHcA_nn1RleD9E69nQhEUfvBYretnW8aDaylnG5NoSwYfbnwumbXarRBosRaVjiGL1M-NhAK6V8_9cgBVOhOOVqCiF9ToVdHXA7pZjUcT3wEqC9QZoQdSyPOiR7jY2Uu6hwaKtHDQCEaWe21-sSaR_vUD1qNQRElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
زور برزیل به مراکش نرسید؛ تساوی در دو نیمۀ متفاوت
برزیل ۱ - ۱ مراکش
@Sportfars</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/441944" target="_blank">📅 03:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441943">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
رسانه‌های عربی از عملیات صهیونیست‌ها و انفجار گسترده در مناطق شرق جبالیا واقع در شمال نوار غزه، خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441943" target="_blank">📅 03:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441942">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K37D1ivVithFzgbJLWI6EIi1Pi1F0WmVsf1idsvtVX4GCFcNrvY4IiL_MnBgFuUoag6bC6LhAudAGAlK6nw-Jn6dP1AbrA4PmKRh1Y3lzoklvN_N6-yi9vSJbWYQIqJ8Tpu4k_xD17n-d02p2MDd2FsRyQVgOKuTAwYkwQNPmdpCV2CWEf_OO7iSQEAJQ8j68WBhfXhIouGdJhJ0AHpqZcoA6JlqOa5e3ENBEesUOdysWA8-LVDnm4xVTI9m2qs_-bLPuQFd0L1rRBOBUOaX9tKKmC794pAdJ3C3F68OtQnNZHXAKAqvgnqY3ANq1te4XOqAANDrjndQlnSAn3Hs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفس ترامپ وسط کاخ‌سفید برپا شد
🔹
درحالی‌که آمریکا در میزبانی جام‌جهانی ۲۰۲۶ با حاشیه‌های زیادی از جمله صدور ویزاها، سرقت تجهیزات تیم ملی انگلیس و نگرانی‌های امنیتی روبه‌رو است، اما دولت ترامپ به‌جای حل این مشکلات، روی اقدامات نمایشی تمرکز کرده است.
🔹
تازه‌ترین نمونه، میزبانی مسابقات UFC در محوطۀ کاخ‌سفید است. رویدادی بی‌سابقه که با نصب قفس مبارزه، صندلی و سازه‌های عظیم در چمن جنوبی کاخ‌سفید همراه شده و قرار است همزمان با هشتادمین سالگرد تولد رئیس‌جمهور آمریکا برگزار شود.
🔹
از نگاه منتقدان، حاشیه‌های متعدد هفته‌های اخیر، پرسش‌هایی را دربارۀ آمادگی کامل میزبان ایجاد کرده، اما در مقابل کاخ‌سفید ترجیح داده انرژی و توجه رسانه‌ای را به سمت رویدادی سوق دهد که بیش از هر چیز به نام ترامپ گره‌خورده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/441942" target="_blank">📅 03:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441941">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204dfa3f37.mp4?token=CHLKS4L1tzZac_Gl6n48GVKaQYKltkE1GhTBkKPIoRhrajuZx7YL-OLp05VA8WaDEdTzDFtmqMnKCSG67VEZ5-jRq5cRNjMtlm8yLHN6Lzxt8g9BIpgYOz-FiGBJwJH2-KFbg_AjACFXyYDb0DaAs_RQMYaLA3HlJzwUD6E6wCYFrWOJZzPjsqwA6vu4B4vvwpBa5q79Il0Xh03uXfTshPQXshogf90lzOUcErct1cNR1qc0_6gnVTZPd9OAsAnQyOxrv-lv5vYEsS5FSowlEzXW_0it4UbU3jPa4eE1THad8TEaF4TtUbkseQ1hwtxYiJXrt4gpBt8fL2Mo663kdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204dfa3f37.mp4?token=CHLKS4L1tzZac_Gl6n48GVKaQYKltkE1GhTBkKPIoRhrajuZx7YL-OLp05VA8WaDEdTzDFtmqMnKCSG67VEZ5-jRq5cRNjMtlm8yLHN6Lzxt8g9BIpgYOz-FiGBJwJH2-KFbg_AjACFXyYDb0DaAs_RQMYaLA3HlJzwUD6E6wCYFrWOJZzPjsqwA6vu4B4vvwpBa5q79Il0Xh03uXfTshPQXshogf90lzOUcErct1cNR1qc0_6gnVTZPd9OAsAnQyOxrv-lv5vYEsS5FSowlEzXW_0it4UbU3jPa4eE1THad8TEaF4TtUbkseQ1hwtxYiJXrt4gpBt8fL2Mo663kdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات سنگین موشکی حزب‌الله علیه مواضع ارتش رژیم صهیونیستی در اطراف شهرک «مجدل زون» در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/441941" target="_blank">📅 02:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441940">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
در پی تیراندازی صهیونیست‌ها در خان‌یونس در جنوب نوار غزه، یک کودک به شهادت رسید.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/441940" target="_blank">📅 02:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441932">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgbH94W-Fb_FG7R23rxpK17NxSIFKQzQEC5r5iSHWV923dMkm56mG29Ic6vAt0AsWqfCPliEU2xwptos2lHipNDIb0tm4r9ZQdf_l-hN46KPlX4uuhHU2aA48SL9VGqXUlFSZtT1qNR0EgjlOsztPo4vQKxEOqKC3tp2WwmNhLB2mcWA2L2RYjiP6JkfObJOZj_Jrg3WVtAGikgWQqg9cngiZtdSNN5OOpOY7CQHZP5VeHKPGoGpF4Z7L4xdkQdDjTNH3G2Gol4ZzFYMutjKL9BPp3J_AI3zzA0QR54R7x8O_eOYrW2AzlhAGiCUGQ5yIWc6p6uNMea1Au7wvrX0mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJAedZR2PrRpDAUdPfvmF_cjSrdZHxBm4IBUR8F9gmQirbJbOB4KrVDRRzN36wo2UaJbp2cZe00j3-X2uDcKME8GgM-3_hkNexvyuxnizk73ZIYNFjzqLy1pn4IX-ABWmkuWUeiJbFw9BF3-0QQRpfr2UcrTDUyIYg0YhkcE2InmhyIArrnWaNOTpf1aScJUOqM-ylhzFiCs5C05E_soOHX03EILOdjPEYAt7KCiTCRKKeAUMeTN7qBzA03QuHB6lYWKkWmpyHnlLYWV8AFm0rWA62PJei5JunZktgmq_Hp7eFx0UD0Oz_oHne5GdvNiMGIxdgzR6mJQYtHYsoqJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muzq1tYhk0R4KaiQmYtbFO2M0Noll4v77S3VBgLuMOBOGx38X1jXMJhPNBMwu-Wxl4M5FrBHLxFL_TxruHXljfwZ0e2w-ESgr8TSsHnWIfPad_-f_EtrUTj6ZHLR9Y7i5N0-ZFW8K01kt8WGErN5OCU-bxHBTPEGx3Sh3ieLGS2ZDzl_1E89uvMpXs01lrPU6zwM5jUOZFs84p4YctOx0uTGImubw85UUIkzVPpu06zIx3CIBEPbNSwcwVXx6VSMCZHMcJ2tZYqOv4zTeFZJ-VPDxCiRqD3umBGRYxUY51VwZKnK-rKcSbgNdrkNUeENxKJ24_auqFhROsGK_dRfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiuM8K6PeQdzibdUiwg817oTeyr8QnLwfWhi3R_VvAwJmD9P4_DmTWY56sYyATrFQElvA8Y4VS8EPHgeOoR39Bj_J0oT9_viPpkwXhBSfgehGmHaTT_B8FCEm3ac_izVObJcfoZHnBixvQ0uv9vGZC45SCoZg88fGVDuY1X56umGghuAePbE5Lbyk0VulMU9v7sAC_LUkmjeVrCjKpQN8zPvKMNtOTP1GgCePbsZ3kRvPYx3OApZ-Z7tjMra142hSCWQBhh1wpc6ONNr0bqk7Rxtj_li9ZBIfFkw53mZlOvY5RlLhYhCp_F_ij6irEzU9e_IBb3GdQJuEhzziL65qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_5__EfyXMSA5FnEZ8F9YTAlLRYOTZdf7piQF8DmATwWvQjKmhfurXSinufpYtYEUqSErh_Ua3RB4nTLceKCPa0ZxIPUm0y066926eXGPxKk1VccdkaPT505eB1nRc0BVOYvqWl8rV3mLgt1n9djN56Rs0QoZdmOE0E3ms48wQ6V_BEqplVyW-Vx8kjOFrusP6jG6H1UOy8GIXlQcF8sOsy9_oEBIkbFkA1NqkmkNi9NWlOneyxhm3LIMU1Rvx4ZOKCIkkox3mlgwp0L_eYREM7EHA2ij-JiXYZn-h4dkp0ok1bTwjZxLklw7Km5_ay464gVWatpxksep2CPByanbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COHbylfNfcpqMFZk_oN2-qr_IXhnNWE9At_ne5WwRP20T6hFNely9DtigIeKq7Ds18Ygj8Kob4W1bUY3kGSIqrkfOXqpYFdKpNM8Alj0-tFPW4nQRgyPXDpehuNOx6Ol-zRLR2Iga7C4kgxoq9jRwcWAe-KjVJldzjyGDT2WE46y6nkhQDDkW8BgHya6GB5L1IaTPsR8tM9ZOUR1OQ58IU_huMn1INyB7leOqm68nBjodOdQFnk6Xn41O5T-dGn81S1nrRY4oM5qiQ6vIkvw65S2oGTqTIJUb5yz__TknJyPEQLqraUSZ7EZ9BRGbfBblcRCw-FqtmdRoY62s7AGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpEkGbcJvUivLGA1vrQzYBVKpA6MT9rRn5Rsc-Q8GaFuMtjFfEbFKkRN-aqZzIWfp6SVwsuBW5U5dpzT5QsySOqiQcob4TABM0uDH0lxlsRm3QGbpRrtzaQo2DG4SrX4GAK72_Ud9Y2Kr-viON7OVI263aPzOK3budhPFenr8_-uGA46Sa9VSxioFNiNSGAeRxSjGdFZvsw0qa8gEDYMvzo7uXyiFB-lUtz89gPTNuYm8jWJmQJ1Ot2rEG9swZ6612Gt6MRDYxnk6e_kCY3sgmOljt7__hjIFBOW9OIFiuEDyeZEWykwT27U-HBeuU_Ux5YuZvsKtOrb2FOSDyhsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PA2J5yKOcV0sfmHxDj5Alqc4npRkT2ddThPq285iCp7Pv9XVTFf8fHPR9MnNYVSVhLr0YxGrcZ6eMJBYIo8tGmmx1OjvOZ1FanlRUuZ0ZJe4KgL-8dbk8aKAa3UrRX_jVjEm6Xie1ferXNDxShTDWMrWckpMhVB7vnjrrRJUA8euH1CX4TRdjU_uURr8fzShZWgdpTWBfkWChx1HN74hoku9MigwQnjTzphRmovtAQ7rgqBLB4Ajn7tF9dDp49Hasd0aEB8A_Tv40RpzfiDpryXeSijlaeHOEUlvNDKnlYRUVO8BakkLu-ThQ3J3wLcLqAQ4UyVmzBp-sgdE30ETBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پاسداشت سپهبد شهید علی شادمانی و شهدای دفاع مقدس ۱۲ روزه در شب حماسی همدان
عکس: مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/441932" target="_blank">📅 02:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441931">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hesHZUR0wxnhL4cNLnEgIQbsAaBOxCkZhnzRZp6m1TsSS1y41-nTMaRckunLVIfXQYrKzcxgfexV03PtXV_4COBfxghYF8AojJvaVHbeN1Bwipy69bEhkIHNrNf6qkWHore-VFRxpG-UoE_VaokaYSAsLRIQXhlYokX194mHiPGiz0VhYohsSxSeCYolnce4zPVDYdrcSBRAkPOY3OJj25fmUIFWhoHxnG88uDU53NonNWeus-m4ICDEs_povv1Yder_ssFqetb8gruG_3wEaD3uzBOhNYT_J-xee44kmvllf63z3JADjXapRGcw_AHWA156cTS88y5Z1vJBLaf4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان، گورستان تانک‌های مرکاوا
🔹
منابع خبری لبنانی اعلام کردند طی ضربات حزب‌الله و مقابله با تلاش نظامیان صهیونیست برای پیشروی در جنوب لبنان، ۵ تانک مرکاوا در شهرک مجدل‌زون در حومۀ شهر صور مورد اصابت مستقیم قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/441931" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441923">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fP0lxAROeJAd3hMyK7DvtjXZwV5fwtorHkhlaFrRRX8wbW0yQjtk7hITSn5ox_L3uhNXORPCTIrUkyX530AiFJPBEq8O-iVJXxob6MzjOAsj_jsN3_4BzUgnsUKMBbfHmM1Et8LXELuS2RLTxkZMm-ZWOyX49dp_q9B-oPfelujEoghaz06ldyn1DXrVDKA-4hk6ErlQMmVX1jDcN0Hu6mFv-HbTgZbud6v5ABGxwML7OVfzK7gl6aXbnx52R2vsE0PrwZ2aND_P71uj68PIUP1VUODQref7Rff94BFQgy0oTVpV-7lJ5wGowzExXprI-PEPx0WHr24-nu04i2IfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afdX72UnPSRqL2aW2ZgVpx5DewKEGdalP4WlgSD4Sjis-lyrGWVpBrZoh25SICWdmxA-uiUJQNdKx0CaTNnIahE8BWkZcRqqdPeh0JQz5Jz7gsX4GLg0VQ-6C_t8MsDQtH6reCM8BF8x4BbVWGpBMxIenmUhxBfVo3eq8LIZDUPZZhSTfkChVejyLpuUdP83lvR0xIFBmh54rCskVi1xoU0sH1VOYjZZOEBqf6sCuU70PYrzB5T7iQmg_CNgxceyK1BhQYonU6ZN3woz8ebH-6xgv4LZd9sEpGJGmQGnB4LELlRh9a-WazsfYKkK01Oz2ZyxEIOeK3sUygkKjUYKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFeLmg3e8Ethn7Z1Lu6DI_t3HBMF2nNgQwBopMHa9jVnWSGEfAN5_rGtLFYrga4JVS_O-TxX75L4gCDO0dYCCg18SfZqTKnV-JoDndAvqov_0xe9yQgQdGQdmqJquUI_6b4-EGUFmIqNj9f4k-HlMoqZxT7O3CKZqc2TbwziWwH9iINQxhmpQzWEvg8LCBYAscpsPPpj59AMigTNmeVt07tMp3IDRm8eJh3CBNY-V1Q1F2976OVxlFMkC8YOYcRW9jpYV9nnaCtW6E3CG_lvc7lCQoC8Ztjl3y4SfMal7mwL2lhWMU9Z8Gc60EiWkj_AD2NAWYbl1KRaBexyNhjwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFG40IuYvljIcyESediW4NDb42swZrnLtQ1mMfEoo0RjSmzCUfnyTjQCMjrHJO3Tcdg5cdefi_QA0bQxJwP_uq-uXtHnd_hVfQ-vNlY13zwoLBPV0D3W4oPa6rPnaXE_3coSqtYaE5uZCrAXM-yvl1wcjAWhrV6dipCZ7cBhvR79mngySpfbB9fn2wOJBycOpxzcpGjSZlPJSwciE9-ZehYc4NTJ36pj9RDebsDvSTcABOdSUnsTtsqsGd4ckGE6PPYlfnNrTKBFtonfIXyCxG1BGP1Wg5Ip6wJSR9nVrt8bA6kgQ-fPOTjF20yTDWE15kAMZqFdxFTjKABknR7ekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SObu3lJsEPrUdkiOxua5kFpHrCpNCZgd4gwdqywXSMLuAmQPEc7WuvH7zN9T5SCimdrwXZ976vF1QzqU0KO3XhaXQvt_1c9u7_ttgggx4G-AtSnBQxWdXgex5lyDmUc_FVIMs2hj7ncnVXkk92pT3a_JyicbeFlS6iD3L_DuJEcYBf_4-fEydLippI4_TFublgoCHkVxiBhH7HC6PsubKwNiBpqSmsi5hAbQ_HPoeGrKjZbKct1Do4Vq1MiqeSfW0iP_aY0jNy178LyJngu_0lH5tehDCg2MqbFOgxXU5FfBQ-Mh5nfV242NJ0dEu6k5A2Ao3BFHg35COOgv8HtvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHrN0X1m-QZR3PUylAc0JZc3W1TkOVvhhUgSw72jtXxGfHOctYJnX3VGXexpzEdR-M6L7lBE51m0FkmdCTDPzfRcMe9WugdZYsKIlxu2PhVn7btxpwIQePEXdLF-fdFFRsfn3UqmfOYXtcBw2qr2L2qjzAfVirx9-TTS5uSS0AdqWIMkbHBDnqsF9Guy46q0AXc7EYLSXsZvit4pujsV01RAQQBuAwlRz7_dYAoG0zyyfMKYYTfrdp2dvspyKSk5vAtxQ8rWOV6xgskOy7MhURlnmdE84jkyQCV8ghFU_25qpX0Dfr0j45uaAAYpTUyNIhetoe8SA85yzEjqEn-FsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۴ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/441923" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3-yfk3KNOeET42diCerPL_0BP6spVIJsu40LBmSXiMLNFeFPkMvvWRjRPxPaws_3VdCt0WsFTP-cwMwM8sqNTNZkg48vUxBs3yI3Z6ncP3s6H0JqzeFfOlhjHVwUrNZMFEoLrkSe393tCtUCljtwJtLmSYJiSTnYkS3n1FOwuIVSCGwEiM32EZQldX2wRZFlcpMJNLPiYtfFBU3bL3Ssbhnc-jOBf8BbdPniHRwLoIaqDfgf9xCgryFjblsYzzPHtAZ1qZHOU5SYhTzBxqZAqSbdc_gH7OglOEBtyWiaFUDHKsBJd5id2UH04Gg4SinXSHlBX9GleqpTyYqJYLDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNhX8R3pszdT5tLsqyXUSiY1TN-E8TXDd2y86fXSo6LHrf6mQQax-t08RGa-xpgfZmC26n65aEdp376jcSpltbdk92yMt4vtpuUB1TCt29_Y2SzMRaxrZ22j_5vFIyTMqs1Q9BkfL10q3BwO6zkeZc3AbthrYOezAJmEJ2HC46Og8cPvidCIFDtL-sKcaQrI7ujT8McaL5n60foLAvXWIXm1QxUJ-0tL_mx7Ro0Y1kMNHGIwGEuLObIK6N3Mk6av3OWOWobfkUSb8FMlbc6C37ciwGP8yM_M9Vz8yeYcOpeLPaQKCYfc7DZWjcX9Lhuk5i3qvO9F9KAWskYuO0BAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WL_BewdcMyEVbQje392MNLP-Z3CHxJUK3qZ_l3kCjNjSk1r2v7tjqfCf0TKTCFnSDhwz2NBWSyYIE78h-bh2hp255azI-quXIUMgImqqtdFOADb6V_VeDy2g7vjvKz3jdyy7TPVQu7pbHN5sCM8BQmgikCXQ6FYXAOmxirOR9sRUigLOwfbMiHLRy3HNIeOTskhC862yBtUoetwpaMlw-IMZ3uQ_GVp9TPcJIFw1RvpSusdqnKpYu5qwSsKtUtKTaqlUzosXEWT6dj-ylHgdK64_nOIy4f-zQS2ce0b2J6JnykX0-cI8EAwvbE9fXRNzrUYIaFjivqMRNihrTnxD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCIv5bf5TC2Oy1nBCCETejlMPQZZ85NdF-cWUTgacsPpaYdQF_kaYfqDQHr0_-lkWnOcJle-N4i9IMpsn0JoLKLHtcurRfoP4erLKIzmVYk-72bxW31u5S10CO-QdyNYKNvjjIMicx2owEZlrIufpjyQ3vCtnvDBcLTRnOaqmqkREb_p7iut6Pmfml_DLlCrzecZRWvipw-uJuOanO4lhEVbFQWqoXAmI4EveCIH5Y9Y3xnAUZnr1JaAqtS-vZwRFv71lZVDqYTSBEgFqPpqwKz9Hi4iKBYgqF7nLYLx6_QZGY0CYKuw2T0xYxVe6xngZepYN9iFxPdK6C45maJAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a00KH0GMOwFeg3UgsGihEETyzXBO8ZRg4KAE6mMzu0m1DO_ozqa6XWiITYr3UDuMdbClQh8-L-th5iO9BltKla6nkqP8IY1jIx4exhK5i9QmCM0cLcG8nBU5faZispt4maFOzfMqRwIUbmJB0xmt912nnA11stllNvBWt_tUh73UtuTcJsx23nyKiYtNXqj2ABKiIdytl6A7IhyTQ4TSqyS92UYGjMFuiSfp8C1macRuS4PLL1Nl9TW9faLLDTQ8EDEk42NG5y8MWAp44iQCurDBGRpnWFPm-9Z4wPKtmErZiANA-ruenVRnfXUGWpsyTu5SZzTK_hhPVnvDcaYYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU94-bqbr4FY1xc5GzJy2nsQDERAqbknI6lMYe7Ac6Ie1fpoc4Is5vbSwG12cRQUXgOp6mDvQPSERdA6dQZqO_s4Ip-P8813FN_23mh59sF1oYgKC5fwwQKKcqGMUY4b-C8JsTtruoXb-JbBLZ4L6XC26mh2dynlYp_AZZaUDeqvdYhab38AYmoqBuGeXo9sDbU2LjaJ_ERuSLk0bhg23WfRMtNrG9gYWP0IFpKdp_pGL3mQVlm1SL95r0-7r_atEu0Mgy_qAdGgQKfCR_A7jaIi3HA91OS0pMo_8jpCRU3ijCo98tzBKdV94M0oKCz9TjE_ZidlYe0VmTn1s6uNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ondJEo3SBKentoMIb-rMTh4I_2oMceydrICcj1edln8WAe_1lTdZw1Lnqes76nSEiOmS5e2pqTRM6pLD_1L_DCqUjx2XqsR7ZRx9u_6riIn3ppNYnKKRmkbubYzBYuYsEHVmok2IfyQAfU5T7JXpWoS670ZzGkEyW5plbqdkOU91OldGhYfJAjAYp6jZkDD8DAWkWG7S1eoLBPpt3Wn49O8UpCM7lEtrfZhUPwJFgtWHdwEyhVgXVnlK8AMXZTo1JYJpTexoVqA6Je7RM_S3W0NvuLdVXTo7d74Z6RcjwcKGJDg2CzWHdfAIrFGkPN9k8VL5AHO8TCp_AXx5LOeY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2dAQOYO9pKSUof0dHS5s5T-etWFxn-fL6s7xtszz3ClbEgBWH0561aDTJvHGmiYPEnBML6zEt6SlLWtGBv4EhIGl1l9sgxpBpZuxsaImqp7akLI7uZ36S2n0oQQyyVIhxGJNebMVZ9KtO2Z2DnmnMjsRY-EZXdhPua4-z99WcP5J_kDrAlVWIxWEgkblehRhRvpsucPDmOUCt69efWE4dD9Ah2nuxmJiu3dx5-cNDqGZWOpeuxSKsns6iKVmX-Byxu6bgh8OcYm_6pqbncbj7epApecAsyI4FsPCce4GH1u--cGm-x9W5kAw5KPLE96O4nlWMV0B9mQ9__BaTAa_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdzN_aaq5dfK5BmFnrfj-QlfTC_txZVesehCAkVu9XwiAYCNA1OFU2m-WiGqvWwmW1b4hLYYRfLyrCByL4yAcxBENTjXmdZkLzFCkJFh7s5CZXkF3J3Bg9vSwiMHTbhNJs44fLJ7WZliJD1PWva8qu1Wf3cgfdudUOxYXTadLEGzQENY5NRiA9T7XtXw4lS0rtr8cssfMfc4oXjohJzhtIQ2dd6t6bnZQ6viIPSESrm-Bl7R46B2M0m1EZgwCfoXHw8hF-ttV3gE4sLZ_w40tIX3VuSZtAHLbS18efVxhcibVbaQ6dp85VTuYSxbc17snx1gBkHotQmlVBALR3GAJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eG4DX8C1KH6gbmuWkqUVRw56DKahMfRddoM8zxH2uFndlKGSHS8w2n25lmQYX_9ylm1JLCdrDEjLyiUdkb4Fj6gv3Ha9cZatgF08YS7Q3FdfhmTA6OOieQIliXFa2w-Rr23V6V_L8uFU0aRK0p8roF27sKycYYehagTyK4n3WLc_wVD0vHQWcfCY5oLsP3UHXmx9Unu1dX3XUXNw2a3_xi9pSv-j-Jbjc8V8-FKk51P6PvT8yuDxd17NzsmE60XedklpErmRd9briyes07u9RPclsT0c5bDdXm_GJgctTolbVoCOxyKSuvsnqIcBzkyYPN5MDXP-2kHv_vxlsZR3cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/441913" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۲۲ عملیات حزب‌الله در ۲۴ ساعت گذشته
🔹
مقاومت اسلامی لبنان اعلام کرد، طی ۲۴ ساعت گذشته با ۲۲ عملیات مواضع نظامی، مراکز، تجهیزات و ادوات زرهی صهیونیست‌ها را هدف حملات موشکی، پهپادی و توپخانه‌ای قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/441912" target="_blank">📅 01:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
حزب‌الله: تجمعات خودروها و سربازان دشمن صهیونیستی در شهر مجدل‌زون در جنوب لبنان را هدف حملۀ موشکی قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/441911" target="_blank">📅 00:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHm80taDjMNHxOKrzFCn8rjNGhQqg4vYvY3sqhjQU-RWIWV6nNQQnqjex7ZP1DqOU1rOdHifag5f8kWcSWhJ3z7mt2UlAMABPjggEjcepZE0vR0X0KlbWshZ0ZoEI_SLCjwjWTpkTWUtmSAe8FcuW6a_647h75p1vW99luGxIMP2DNFseZJ42Buh7yyk4jmY-YSHZ0SVgPM477CWnuVN5I_V5y2nRwzbFr-PIbBYXqEjYWXU0HrBegsyVUMV0JpjkQbKwf0-mBNwRXViZpQmpckyogPb6hIOhfm2z8gbOZl6tZ7qj3343T8UVetd9Cv8KBsjS3uNNH15stHnoH4h_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پایان مسابقۀ سوئیس و قطر با تساوی یک بر یک
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/441910" target="_blank">📅 00:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دلال‌ها برای بازگرداندن امارات به تجارت ایران فعال شدند
🔹
همزمان با حرکت ایران به سمت مسیرهای تجاری مستقیم با چین و روسیه، گزارش‌ها از فعال شدن دوبارۀ ذی‌نفعان تجارت واسطه‌ای برای بازگرداندن مسیر امارات به مدار تجارت ایران حکایت دارد.
🔹
طبق آمارهای سازمان توسعۀ تجارت تا پیش از جنگ، رقم تجارت ایران و امارات حدود ۲۵ میلیارد دلار بود اما فقط ۱۰ درصد این رقم به تجارت مستقیم این دو کشور مربوط می‌شد.
🔹
۹۰ درصد حجم تجارت مربوط به کالاهایی بود که از امارات فقط به‌عنوان واسطه تجاری برای انتقال آن‌ها استفاده می‌شد.
🔹
اگر واسطه‌ها فقط ۲ درصد برای نقل‌وانتقال پول و تسویه این حجم از تجارت دریافت کنند، در کمترین حالت ۴۵۰ میلیون دلار در سال برای آن‌ها سودآوری دارد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/441909" target="_blank">📅 00:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
برخی منابع از حملات توپخانه‌ای رژیم صهیونیستی به حومۀ شهرک‌هایی در شهرستان صور و همچنین منطقۀ «وادی الحجیر» در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/441908" target="_blank">📅 00:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
کاشمری‌ها صدوپنجمین شب اقتدار را باشکوه رقم زدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/441907" target="_blank">📅 23:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c33fb0f75.mp4?token=Dj-ZpEcv20VXVPnkPcduh3_hD-UzQNkYiLAAVnorbsPfCAKZmwqB2_zoUzVurGUDuGwnmry8ayJr_fw6ziP1heWitBYKnQuOsv_PylWUUGmppkgpljBNTdcQQpVloWlRPBsmcP6UuShbYRpKRj2nHU0STIlHdWeoVDETZ-YD5o00_LKTvQGhGZyhupkR_xBZb-CZlhicrxAZCu1xdi0xh1PYZZbKME7jEI0GZWbWc0GYbxvAGl1CY6i84wuHWYUAt1DTXcJgvI7BaePMTB8LufNlM8g-lW92vAJIk7sFZ_x3RcXufKKymT0ugAcA6fPSouxtaqsLGjUSxAxGucPGqYO86CQe2QBktDoftw2kGvFyO3s_yQNgNN4lstc0gChLK-AcAlbPSJoY00GqJOyFu9X5fsAI8qw-dWOWJMeGA3hiITfzL4CgYvPr8kOcNTat86wfXxN-uBh0G6DomLHMT2tjhEamaDPay3V66JsERv6e-UGF-rwDaKqzG0WZQV6V-CHGCOJ6GStJtk_ANPz7nATq7MIcHoepK_NDylO9NmP1D1twDYypcKT2xY0KiS3n7K7dWrXT8SUWK5zxwld--IOPfRsezj7Au6CPtYIKC7UKULezsrmehmTzhIMg_Y0dX6eqUjLiN9sz6BmIj2mIq7UGw893_n27p97nhgK18_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c33fb0f75.mp4?token=Dj-ZpEcv20VXVPnkPcduh3_hD-UzQNkYiLAAVnorbsPfCAKZmwqB2_zoUzVurGUDuGwnmry8ayJr_fw6ziP1heWitBYKnQuOsv_PylWUUGmppkgpljBNTdcQQpVloWlRPBsmcP6UuShbYRpKRj2nHU0STIlHdWeoVDETZ-YD5o00_LKTvQGhGZyhupkR_xBZb-CZlhicrxAZCu1xdi0xh1PYZZbKME7jEI0GZWbWc0GYbxvAGl1CY6i84wuHWYUAt1DTXcJgvI7BaePMTB8LufNlM8g-lW92vAJIk7sFZ_x3RcXufKKymT0ugAcA6fPSouxtaqsLGjUSxAxGucPGqYO86CQe2QBktDoftw2kGvFyO3s_yQNgNN4lstc0gChLK-AcAlbPSJoY00GqJOyFu9X5fsAI8qw-dWOWJMeGA3hiITfzL4CgYvPr8kOcNTat86wfXxN-uBh0G6DomLHMT2tjhEamaDPay3V66JsERv6e-UGF-rwDaKqzG0WZQV6V-CHGCOJ6GStJtk_ANPz7nATq7MIcHoepK_NDylO9NmP1D1twDYypcKT2xY0KiS3n7K7dWrXT8SUWK5zxwld--IOPfRsezj7Au6CPtYIKC7UKULezsrmehmTzhIMg_Y0dX6eqUjLiN9sz6BmIj2mIq7UGw893_n27p97nhgK18_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشت‌گذاری سنتی اردبیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/441906" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">📷
افتتاح قطعه نخست آزادراه شهید شوشتری تهران   عکس: زینب حمزه‌لویی @Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/441905" target="_blank">📅 23:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f265eab85.mp4?token=o0albPYe8wN82D20ccBpthWX1vTrVGyUOFbbsjclJwzhbZBEQMwgpx9Q7O-Wcp2Npk7i2f4TOASDwXMH-Vh7gMnUGcBVfw_9yoCLNL9pCwnjyJG43l2-4B6KqOLmmkof6L3UGVmcMXxlE2C0kZU0J-c8n9PZ3-6UcJuIZKNIwZ_LmBoLb355CiobLtcGgGNbalVI9Lw6GaAr7_mYpO4Ugg2uOEtMe3Iq-Tw_EI1Z-1N4x-rI1_3-18gDOtDXEXTLOeqZKBsjRVXWSyBZ7bjYYz9K7a_fqkBZ4Wv8j3ojcyKUfk-tdZhCS-ZHsWpiH743oEhefp8AmffQw6UYUElHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f265eab85.mp4?token=o0albPYe8wN82D20ccBpthWX1vTrVGyUOFbbsjclJwzhbZBEQMwgpx9Q7O-Wcp2Npk7i2f4TOASDwXMH-Vh7gMnUGcBVfw_9yoCLNL9pCwnjyJG43l2-4B6KqOLmmkof6L3UGVmcMXxlE2C0kZU0J-c8n9PZ3-6UcJuIZKNIwZ_LmBoLb355CiobLtcGgGNbalVI9Lw6GaAr7_mYpO4Ugg2uOEtMe3Iq-Tw_EI1Z-1N4x-rI1_3-18gDOtDXEXTLOeqZKBsjRVXWSyBZ7bjYYz9K7a_fqkBZ4Wv8j3ojcyKUfk-tdZhCS-ZHsWpiH743oEhefp8AmffQw6UYUElHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌خوانیم تا پای جان، جاویدان ایران
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441904" target="_blank">📅 23:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441902">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e8ee66e6.mp4?token=gTXpi9mwV-pLZhS1ze12dmfloloAfbVZFQN4lK8Kfr36AL0Ffe3cxjsfAU296igQNWjkRumassB8YFjz3PwjW-l11bvamiXsIEbMwCZo_jWKM4yLMr5f0AdKxU7aWyPbPcyTSgxUdH6HJMq3g0CPdSdr_6XOUSR1rc9OCQ1Poq4y1ybtxXYHRXNrxhSyT8iHnCTfSR0_6pmDaJ1FMsWTdDPyCF_EbrLqyLigMjv8wVYq8xAoYs88tECdSfi-Gk_AF7kFOkWZ0jl2_Q4C-obaXb-jLa_lk2ebBKvhLzJ9BhHANuEHbDjTZAAOOazvdjqxkkEFEpVxOsksDDgqA_DOQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e8ee66e6.mp4?token=gTXpi9mwV-pLZhS1ze12dmfloloAfbVZFQN4lK8Kfr36AL0Ffe3cxjsfAU296igQNWjkRumassB8YFjz3PwjW-l11bvamiXsIEbMwCZo_jWKM4yLMr5f0AdKxU7aWyPbPcyTSgxUdH6HJMq3g0CPdSdr_6XOUSR1rc9OCQ1Poq4y1ybtxXYHRXNrxhSyT8iHnCTfSR0_6pmDaJ1FMsWTdDPyCF_EbrLqyLigMjv8wVYq8xAoYs88tECdSfi-Gk_AF7kFOkWZ0jl2_Q4C-obaXb-jLa_lk2ebBKvhLzJ9BhHANuEHbDjTZAAOOazvdjqxkkEFEpVxOsksDDgqA_DOQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهتزاز پرچم فلسطین در بزرگ‌ترین میدان نیویورک
🔹
هواداران مراکشی جام جهانی پرچم فلسطین را در میدان تایمز نیویورک به اهتزاز درآوردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/441902" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441901">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2062b21633.mp4?token=pbo7TB51PkkXePA_pPiAJQPo09K2egxXMqxjcCsT36nDqRSDuZ7kpioRcq1DbZxoFIQuxp2WDbGfN4mKpDPfUaY9J1j6LCO02O27AmTJyDFPOUz4zrb5mxSk99r7qajiWlZyL1Gc9_O3zLgCArmHZft70Hg74hlmb6mPS5jic8SfGXNtkjjughbqI3GT10LQdiWb3yUYOilBPBOS6hDhK6bY4hh01E_l0LIsxmKzhyYsTZ7iuiV55wzot2ZREaZsnSZyfp9oWSzsV5JK2UD0OcTjGjjCzvHMboWf5qJzZWgwa48TYk7YqU_wlzfFcUVGYNS-cH3TN9TXcWZu2jUyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2062b21633.mp4?token=pbo7TB51PkkXePA_pPiAJQPo09K2egxXMqxjcCsT36nDqRSDuZ7kpioRcq1DbZxoFIQuxp2WDbGfN4mKpDPfUaY9J1j6LCO02O27AmTJyDFPOUz4zrb5mxSk99r7qajiWlZyL1Gc9_O3zLgCArmHZft70Hg74hlmb6mPS5jic8SfGXNtkjjughbqI3GT10LQdiWb3yUYOilBPBOS6hDhK6bY4hh01E_l0LIsxmKzhyYsTZ7iuiV55wzot2ZREaZsnSZyfp9oWSzsV5JK2UD0OcTjGjjCzvHMboWf5qJzZWgwa48TYk7YqU_wlzfFcUVGYNS-cH3TN9TXcWZu2jUyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع بارانی مردم بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/441901" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
