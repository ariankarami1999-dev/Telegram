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
<img src="https://cdn4.telesco.pe/file/WfflyOeFoEC_r4fdCVtX2DedIAr38HVs14pb2eXzkGqmCIQTfHULbdgL-sjM3Xb4iBf-O88XBGHVY5Xooch7t0WvFChdHjY2EtX9g-ZmjuUl13PWjQ58QsfoKRQlebf2SRGLW1Gv753VCMim8c0WZeAAeI0H6JicDHzi0Igiz8Td2IHnSN5qSQHwit_mpuZeS4uM3W2jQ0F7ymA2pTsq_BR0CpK-xBv2ciApJpELkeuQ6SYRYDHEmR_KCb-p73doKt_XCAyQh_lfKavA5tPIYN0QFlxWnha8OjHeRJWwAVTXazLywH_KSD9pEFS2cU91X-xIcnk5dYd2uUQpMrKebQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 17:00:34</div>
<hr>

<div class="tg-post" id="msg-88449">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c68e0f99.mp4?token=MtiN_wgRDsy2BcN69jbeW4lDQkA3jvMyvJgMtKyqntuIQypItXEwpl45BuBtg155TfUJnaqUbGKY5FWMUnXrgL19fns6SwTHDJfopVwTIFK10fKLCifSWgcN_mCPV3yrdnPDZEmuyqfFb5O9L5JoQwCCURTr-VYxVadjqQR02v-9FeSV0FhOksOX_y5aG4p1jsbpNII459K2Ir6USzrm6hUyfP6q84zoPSNCNF3hW2_LJcUv_W8bSHHsBOqHqOUuYJ_NBIR5nfoS-OFqMLlyHQ8uqiDAxyx3jIsKWL5-uI7I9tfAVUl1DqNJRWCu1-B28ey_94mB--E71wGFQponNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c68e0f99.mp4?token=MtiN_wgRDsy2BcN69jbeW4lDQkA3jvMyvJgMtKyqntuIQypItXEwpl45BuBtg155TfUJnaqUbGKY5FWMUnXrgL19fns6SwTHDJfopVwTIFK10fKLCifSWgcN_mCPV3yrdnPDZEmuyqfFb5O9L5JoQwCCURTr-VYxVadjqQR02v-9FeSV0FhOksOX_y5aG4p1jsbpNII459K2Ir6USzrm6hUyfP6q84zoPSNCNF3hW2_LJcUv_W8bSHHsBOqHqOUuYJ_NBIR5nfoS-OFqMLlyHQ8uqiDAxyx3jIsKWL5-uI7I9tfAVUl1DqNJRWCu1-B28ey_94mB--E71wGFQponNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوة من فوج مغاوير الرابع تتجه نحو الجسر المعلق</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/naya_foriraq/88449" target="_blank">📅 16:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88448">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc052bc00.mp4?token=FHtLaIOFQYBM772mQqnO59y6JPQQA7jHIffqrPd0sJCAEEYdmCib5_NkV5JGK0HYljCUECQf2DPgspD83xaMylWupcCheAILAA7U1NRCnSsw_qDfrTfyZ4CKd7KSgmHplV5blEh4FIsDUL3IGrMnilBfieNH88v7JHS3ES-5OzXv1HS1_TH9TJw4pHbEyPHo7ZGTUomKF1X8PwKptGu3Byan1b_m6nLUfiMzGgIikoytPXTOB7WKDBoQ3sEGSua2l6uEYHXJwls5ZIavdp4-SGoGyCBg2dm7XY4Pk2BMJbKGxzw7ufwZF4Y1qY9-AY7skcc5fXJTVbzVfjnnQcHMrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc052bc00.mp4?token=FHtLaIOFQYBM772mQqnO59y6JPQQA7jHIffqrPd0sJCAEEYdmCib5_NkV5JGK0HYljCUECQf2DPgspD83xaMylWupcCheAILAA7U1NRCnSsw_qDfrTfyZ4CKd7KSgmHplV5blEh4FIsDUL3IGrMnilBfieNH88v7JHS3ES-5OzXv1HS1_TH9TJw4pHbEyPHo7ZGTUomKF1X8PwKptGu3Byan1b_m6nLUfiMzGgIikoytPXTOB7WKDBoQ3sEGSua2l6uEYHXJwls5ZIavdp4-SGoGyCBg2dm7XY4Pk2BMJbKGxzw7ufwZF4Y1qY9-AY7skcc5fXJTVbzVfjnnQcHMrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر امني   انتشار قوات سوات الداخلية لاول مرة بالقرب من مداخل المنطقة الخضراء بالجادرية وطلب إسناد من الشرطة الاتحادية من جهة المسبح إلى فلكة الحسنين .</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/naya_foriraq/88448" target="_blank">📅 16:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88447">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇶
مصدر امني   انتشار قوات سوات الداخلية لاول مرة بالقرب من مداخل المنطقة الخضراء بالجادرية وطلب إسناد من الشرطة الاتحادية من جهة المسبح إلى فلكة الحسنين .</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/naya_foriraq/88447" target="_blank">📅 16:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88446">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مصدر امني يوضح لنايا   قطّع طريق مطار بغداد الدولي على خلفية زيارة قائد الجيش الألماني للعراق</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/naya_foriraq/88446" target="_blank">📅 16:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88445">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbCvMKlcp7qgOuh_K4F3vAmq_nnetjhDxTplOSz78B8_njRZO_aaybR5-UlTqXqoGtmOc59tE0KXfDUvxsu6yoW4t2pnhrdUY6am3Zt3At2APCHMq-FhUeCe-lzPiOecxi_KMJk0kHvjnOf_mB778DWfn_J9dkSA_AvPvVRJUqwI-40IeVqOJEV5GM7W2uYC_8LwDOwkhX3R2SwNuV4NNrahDHBvwbF6UErmrySjBnNd1-wJUmFgWefFdYgQOoEtZWTHVFhH_UvQxfKyAhsmn0vuL4G-lBvItTH7ztLKhunzKW1WvaxnehHN3auhhg89mz8KeBDjTcXefY4JnY3l3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القوات الامنية العراقية تضبط (428,794) قطعة من الأدوية البشرية المهربة وغير المفحوصة في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/naya_foriraq/88445" target="_blank">📅 16:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88444">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔻
مناشدات عبر بوت نايا:
نناشد وزير التربية التفضل بالنظر بعين الأبوة والمسؤولية إلى ظروف طلبة السادس الإعدادي، والتوجيه نحو تأجيل امتحانات الدور الثاني، وأن يكون الامتحان موحدًا لطلبة الدور الثاني وطلبة الدخول الشامل.</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/naya_foriraq/88444" target="_blank">📅 16:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88443">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a39d0b36.mp4?token=M25n6sVSvlQCjQQwxjsrfvuvDdwuXqasJZ8cbCW19AJpcUSt8hN8DczxQu5frVstEIQgTf79_72medFjlJjHBNTcoN3pq_3Q3pVTwTHp_kC-HsWovRDHuBYkWK3FzaL8Ewil6wMc1Zuo0D7wGfKT7TgEOv8C-wBHcwWTaGUzU0Qbs32Xb_YduWaAIqkvzkzUkgndHWX2ydUwNFgGGFE621bVrhLVnn7YaLNDzx2jw6n6yjjbHRhKDIrx5RP_Ki--Cj5LgGgAwiTXRKOpzJlizfMpcyuakjDDnzmgAkXMeYfZTMbt6xwq7Xmb7S4s9CRvAUIdVqG7WN4xBBqmQ7JYGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a39d0b36.mp4?token=M25n6sVSvlQCjQQwxjsrfvuvDdwuXqasJZ8cbCW19AJpcUSt8hN8DczxQu5frVstEIQgTf79_72medFjlJjHBNTcoN3pq_3Q3pVTwTHp_kC-HsWovRDHuBYkWK3FzaL8Ewil6wMc1Zuo0D7wGfKT7TgEOv8C-wBHcwWTaGUzU0Qbs32Xb_YduWaAIqkvzkzUkgndHWX2ydUwNFgGGFE621bVrhLVnn7YaLNDzx2jw6n6yjjbHRhKDIrx5RP_Ki--Cj5LgGgAwiTXRKOpzJlizfMpcyuakjDDnzmgAkXMeYfZTMbt6xwq7Xmb7S4s9CRvAUIdVqG7WN4xBBqmQ7JYGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مراقبون
اعتقال ابو جعفر التميمي دون الرجوع للمؤسسة الدستورية التي ينتمي لها ضرب للقانون العسكري ويندرج ضمن خطة توم باراك لاشعال الفتنة بين القوى الامنية واشعال الحرب الاهلية التي يتربص بها أعداء العراق …</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/naya_foriraq/88443" target="_blank">📅 16:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88442">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWnAHyEqaBKP-d95AR1CxxY0-iy5A9-P4QsUBq-kKI7-XpGdQ3g9O7uZ5t-Buk9J9MAP2noqdGVPwkQqd8b-rf9qzJovUkzJk5zufpjzEkfaQANQYrhaws7niVap9cFn0z3yWdXxQl4ykxqRnaeSbtDsoiQRQWZN3uSv-K3oQH2mjGUZYS5lw0S_cEUqHG2I6zIFVHaTLvpVHC6N7a1-aFb-JM4qA3xdIwm-ClP-neWuHIPiutCxJCBwa93OFh2Ggw2uflhT8f9_nsggCbump5MRkNZqMyOByYFPeT4RHFn6TPN19i9eLhtmkUczfiFP49m1dr9qo-bjE3cTOJd7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب ايران تنهار</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/naya_foriraq/88442" target="_blank">📅 16:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88441">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قطع طريق مطار بغداد الدولي لأسباب مجهولة</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/naya_foriraq/88441" target="_blank">📅 15:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88440">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">إغلاق ساحة الحسنين بمنطقة الجادرية وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/naya_foriraq/88440" target="_blank">📅 15:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88439">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عدد من العمليات العسكرية.</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/88439" target="_blank">📅 15:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88438">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">غلق المنطقة الخضراء وسط بغداد من جهة المعلق وانتشار قوات مكافحة الشغب</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/88438" target="_blank">📅 15:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88437">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7PvVmlNbL3WJDViUVCB3JuSizxhswM2IB6qWdCg39zqjWHc19odkjfiyfoIslI2xRI2Y6vmYUJ81PQbJdP77t2rsfVtkiAe1c8wAjTIu7UuDTfq2AoKfGD3jcMIiCWXs8jT0MDQegslhORdRWw9PIwyDXFkFwhrkdF6n1AbnT3eor3pTEtpACM3NBp6KNXaMpHX-lQCKn54spukKVECrt7QXCaWTlyhCGTI-dmu9V3BFKjK689gKt8qciMIFY93WpP1zuo7p7eaDfCIFa1rFKkokmIGMgqAgaNtKcLXPfHK9edltBbWRPsMVtirtJi775lH4tVJJyakyW6ReYKA7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غلق المنطقة الخضراء وسط بغداد من جهة المعلق وانتشار قوات مكافحة الشغب</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/88437" target="_blank">📅 15:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88436">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏
رئيس وكالة الطاقة الدولية:
قلق بشأن وضع الغاز في أوروبا هذا الشتاء بسبب انخفاض المخزونات، وانقطاع الإمدادات من الشرق الأوسط، ونهاية إمدادات الغاز الطبيعي المسال الروسي.</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/naya_foriraq/88436" target="_blank">📅 15:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88435">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انقطاع الكهرباء ‏عن منطقة مزارع العبدلي في الكويت بالكامل لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/88435" target="_blank">📅 14:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88434">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q31us22E1uSacff3LOVLFsQ1DUZYiCLSYj79EDuD1E6DGu_EBqKmnfpR4C-vGkhmrbv51mPc7NvwIf1yWI6HkPXS1o4R5PHr6efzofINnO3N_RueV5YsSaPq6WanusvA8LM3FFGGnluvA2sApUJI4f4C6oQjrvrPeVrzzhudxlwB6keZ-6aCyXk-k9i0RGg3JjR3JxtL0FFAnDysVwnfBpg78djRtsvGoLL48m_mvfP1Mg08zrUSVeZHyJA6K_q6kmu4R8SqCEkRrjLXqUYFjWa5ARXhlRjVpX9XTLV5dBE4eSiOHcxRZv47UlMo7F4fM5SkB_kr1GRVREoozk-Hkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكويت ليست بخير</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/88434" target="_blank">📅 14:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88433">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8v7XMOh84i3lXVkhCCR8b8IW1Y0pCm34hsJwOtJCxCXOQfLw4SGrTkeu1kA2DPQP53HRcsdo4DwR8I08R5bW0wz6IeIMbXlGxEBbS-6ybPr4HwE0fsncBYFRChsIr13QITL9d-22-uKq3j5s3Wpx-bEcqVLQLg--45qy1wsWTIoCkkprl3ffhq7OeYPnEPZOpmiR2AfdKFdWRv3KpMylGGjYyrohKoM_gFGdRpL8WM7yL5A6T9_DRUdPvRL6F7wKQZxDVjeC_ulXcHjmhSWYK2Z-EGInYhp9EUGR8J6G3tj00yAl7XY5ei4BfaovW8P5w5ZR4AFYr-NFOHaqChEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف:
‏لنجعل أمريكا جائعة مرة أخرى! ‏لا يمكنك التستر على الهزائم بادعاءات كاذبة.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/88433" target="_blank">📅 14:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88432">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQbcG4wUScfDVXQcI6gI4O3sQr3ysdpocddM2_Md5VIXhgT1Cw-MpnBoH2FWLzLBwNdnR7AUaGaCsbLjEYfZLVYqv1at8vZr3qCirC9bKHFHVQ4UTTBpza_mCmVDdSeTaHLSyp5lnVGrqAhaZSpeB92FhZKK09P3JmUdlKawACaC4gj-RP22sSWpjsqr86QK_bEP75bLzbvGFqomyr999sNz61SKfPbXDFtra1KrdpfLnx-OTTME2uLrHey9RwNIJWBn0o-C5jhAPMeqPj5_qBN-ynj2Aoz5a_7q1d5oVrxUnfCmk5atui2m2cdMVWnykD6Kf5a1c50nznOm-GYdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدير مديرية الإعلام في هيئة الحشد الشعبي مهند العقابي:
جماهير الحشد الأحبة، تمت تسوية الالتباس الحاصل بشأن اعتقال الإخوة في الحشد، وتسليم الموقوفين إلى أبطال أمن الحشد الشعبي، لمتابعة ملفهم مع قضائنا العادل.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/88432" target="_blank">📅 14:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88431">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b09c0dce.mp4?token=BzJd8nrO54ajW5_h1VoN3KdncwzBb6dxLXZqdEt1QIJ9S699IYl72fCR2ujnuBITsNCZ1GNb9ySmZv1X4tZqPNGmdrPDEf0VWtafEr3nFBIqp8RdaS8BLrggIQ5tYMCYSk-hKl1BEPCZGWWzO1VLRfKOHKSUrMBgXW674HS--J2YWvz5qcGnDIxEUGo4IpMr3TwUBDoA7YUeHuwzij2GL9-e5LgdzCM_Jyc2ygQMzGvXfwGr5GoZVdMP0QgByEHLbZVzsQwLsfglJXAAMfrTNtZ-ldHk9p-EWjiA9LjoVM0v6X4D42AYuavCPEFNovEv7HjEng9ppLuYJhWU9fMmbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b09c0dce.mp4?token=BzJd8nrO54ajW5_h1VoN3KdncwzBb6dxLXZqdEt1QIJ9S699IYl72fCR2ujnuBITsNCZ1GNb9ySmZv1X4tZqPNGmdrPDEf0VWtafEr3nFBIqp8RdaS8BLrggIQ5tYMCYSk-hKl1BEPCZGWWzO1VLRfKOHKSUrMBgXW674HS--J2YWvz5qcGnDIxEUGo4IpMr3TwUBDoA7YUeHuwzij2GL9-e5LgdzCM_Jyc2ygQMzGvXfwGr5GoZVdMP0QgByEHLbZVzsQwLsfglJXAAMfrTNtZ-ldHk9p-EWjiA9LjoVM0v6X4D42AYuavCPEFNovEv7HjEng9ppLuYJhWU9fMmbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطع طريق مطار بغداد الدولي لأسباب مجهولة</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/88431" target="_blank">📅 14:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88430">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b122a3fb40.mp4?token=XB_fE__RSOdCeizpXmzFvtJOCjLMIElDAF0ddFiUp1T407kH_O4soLAvL-pA8RGIsUy7DNOS-Y7xlHFqLoAD60NucbxJ0FEQXWNWZNeU_djMIgEES4ZDowJ0oONKGHRfX-o0dpoykmd3OEF4MqgAvQOv5xrrm8xYZSeBKR8kB4UcE8EV9sWzMHDHGZhH8-0FsYlPuJsUbY-Ewi2lY5SN16u3GEI365JOvKVCS1wXma4XDL6dv2mcZRa4G9czo5vwzliA6qdR5WzE7hfUesSl7RkweZnvLA8Rwx0MGbxRMvUF5Q6XGqSWNgdbjJvV5rV_xMau6fZv7k-_oo5S1Ez48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b122a3fb40.mp4?token=XB_fE__RSOdCeizpXmzFvtJOCjLMIElDAF0ddFiUp1T407kH_O4soLAvL-pA8RGIsUy7DNOS-Y7xlHFqLoAD60NucbxJ0FEQXWNWZNeU_djMIgEES4ZDowJ0oONKGHRfX-o0dpoykmd3OEF4MqgAvQOv5xrrm8xYZSeBKR8kB4UcE8EV9sWzMHDHGZhH8-0FsYlPuJsUbY-Ewi2lY5SN16u3GEI365JOvKVCS1wXma4XDL6dv2mcZRa4G9czo5vwzliA6qdR5WzE7hfUesSl7RkweZnvLA8Rwx0MGbxRMvUF5Q6XGqSWNgdbjJvV5rV_xMau6fZv7k-_oo5S1Ez48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجار في مدينة تدمر السورية</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/88430" target="_blank">📅 13:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88429">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سماع دوي انفجار في مدينة تدمر السورية</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/88429" target="_blank">📅 13:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88428">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec4022a6a.mp4?token=Znia2SJlRDFlfASfVBJYsT64OiVDdFwft6hWG-80F0bnZAjesM__83NyOtQ0x2CvQ-cTAbOrTXQEcgem4JFwVyK8PYVgNSguIHtPJKK1cZulqLRs0h3HMu56fmHcI_vs9ad81Z9qAZrQ_yS4UVAl4yTm22viS0FD0o64la1ptVZSHchScjoOWamb25q-v7xZQEATaPAnjTwrnlT9hpYPT23F5m5J7teg7HarV6hoR6JbP10kAcvp-WyGxVjOgHQdLsV0za6Yizbj7mroZI3N5WeAUm44uRa-64P31mBMgwsY_-mtFTzOu5_aQd5kgWSyIwNUrB00qeeUjtUD5Ewj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec4022a6a.mp4?token=Znia2SJlRDFlfASfVBJYsT64OiVDdFwft6hWG-80F0bnZAjesM__83NyOtQ0x2CvQ-cTAbOrTXQEcgem4JFwVyK8PYVgNSguIHtPJKK1cZulqLRs0h3HMu56fmHcI_vs9ad81Z9qAZrQ_yS4UVAl4yTm22viS0FD0o64la1ptVZSHchScjoOWamb25q-v7xZQEATaPAnjTwrnlT9hpYPT23F5m5J7teg7HarV6hoR6JbP10kAcvp-WyGxVjOgHQdLsV0za6Yizbj7mroZI3N5WeAUm44uRa-64P31mBMgwsY_-mtFTzOu5_aQd5kgWSyIwNUrB00qeeUjtUD5Ewj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحشيدات امنية كبرى داخل المنطقة الخضراء من قبل قوات مكافحة الشغب</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88428" target="_blank">📅 13:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88427">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔻
إنفجار مجهول في قضاء كويا بمحافظة أربيل شمالي العراق ؛ إصابة 4 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/88427" target="_blank">📅 12:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88426">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية في مدينة زاهدان جنوب شرق إيران؛ إستشهاد منتسب كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/88426" target="_blank">📅 12:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88425">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
🇵🇰
وصل قائد الجيش الباكستاني "عاصم منير" إلى العاصمة الإيرانية طهران، للقاء المسؤولين الإيرانيين.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88425" target="_blank">📅 12:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88424">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1fc56eb9.mp4?token=UY1DaD661EjDR2Nznck2PzxjtnMGqKKXiIOLZYuwYHYH_5FIJ4pGh3SfJOioAllIjgtAEKKlj4pS8-QY1S_QbpdcUVLAEvp5IjnAl-v-n_SsGnHfX4EgbKWseiQP89cRs2gRzhN9tc5x_BXbtUCuP8KSgynrOB0tTT2Qdw8fqo55NY-k-fPrbaBGl9vUdI2zMhusOlkkES6gDbNsUSt9C6feAcGV9bzf8I4BnzlxR6gyvhv5ZgQGdfzgBuL14jJCQuEKsZVBEHumHOM9l4sJw2JjMKxpxur4-913zixdli4YWF2xK8ZkCjxw0LR9skl1fk_WlMtTZrQEjQGdlzStPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1fc56eb9.mp4?token=UY1DaD661EjDR2Nznck2PzxjtnMGqKKXiIOLZYuwYHYH_5FIJ4pGh3SfJOioAllIjgtAEKKlj4pS8-QY1S_QbpdcUVLAEvp5IjnAl-v-n_SsGnHfX4EgbKWseiQP89cRs2gRzhN9tc5x_BXbtUCuP8KSgynrOB0tTT2Qdw8fqo55NY-k-fPrbaBGl9vUdI2zMhusOlkkES6gDbNsUSt9C6feAcGV9bzf8I4BnzlxR6gyvhv5ZgQGdfzgBuL14jJCQuEKsZVBEHumHOM9l4sJw2JjMKxpxur4-913zixdli4YWF2xK8ZkCjxw0LR9skl1fk_WlMtTZrQEjQGdlzStPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي   بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88424" target="_blank">📅 11:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88423">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5ed1dfe3.mp4?token=m33vMe_r0A96wPB41T9uUa7uh_QplwiYijVARxkhs18VwEipXgRoXLggHMKyLnoRIkdwh2b8IeWVYVycQjoSS8yqLP4pUrx8bXQqcCMYqTvs921DWV3nLhyq1EZ2skEjmRCJM9pspvNsm_m_pn-AtwRClnqU2Tfo2A-qeMLS6MJe7MB1cqQ4z7yYQymtJECQob8wSwC-EGyk0ItWYwckzilhnJCll9lAQUKoz7V5yR0P0-WM_SMZxJhO5JLlBpYnXdUiP_8wQWy5tN8fw9UCSR874ca8UHBnadE0MPmwRrls-mk0m8VvZNgmGf2gPpkiSCuUuYot1qvAvO2zWgyZWrF8vj-tfApCIRVBxCcGToaFnFZ8GVUoORMxoMfRmpeq5xDYM5mMxXBXHLbAXurkNmNoud7WRyz31_-kIhztnJsj5jQ0QSjhZxgycqmwdpH9NQc2U_atOlc10TlVfEet06eQBYZ8YBSmmFCewfNEpQ_lrKh3jIr-uwZ_Q_67OGxch3x8b4P115ItSlbfxUE71zo5DA_XSu_6y2Dthl6-Bw_EkZpp9x0p5eB9GTWeeJHDgHfgzXEQfkdwOe1jCjAxRNtnPGtjS0sRfA1tZ3CdomKD17NYQivk1YCj1yJdcN7wKb-QSeH0Cz3avgVA4UiGcxTBjU0nMWrLf5PWcS9L9Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5ed1dfe3.mp4?token=m33vMe_r0A96wPB41T9uUa7uh_QplwiYijVARxkhs18VwEipXgRoXLggHMKyLnoRIkdwh2b8IeWVYVycQjoSS8yqLP4pUrx8bXQqcCMYqTvs921DWV3nLhyq1EZ2skEjmRCJM9pspvNsm_m_pn-AtwRClnqU2Tfo2A-qeMLS6MJe7MB1cqQ4z7yYQymtJECQob8wSwC-EGyk0ItWYwckzilhnJCll9lAQUKoz7V5yR0P0-WM_SMZxJhO5JLlBpYnXdUiP_8wQWy5tN8fw9UCSR874ca8UHBnadE0MPmwRrls-mk0m8VvZNgmGf2gPpkiSCuUuYot1qvAvO2zWgyZWrF8vj-tfApCIRVBxCcGToaFnFZ8GVUoORMxoMfRmpeq5xDYM5mMxXBXHLbAXurkNmNoud7WRyz31_-kIhztnJsj5jQ0QSjhZxgycqmwdpH9NQc2U_atOlc10TlVfEet06eQBYZ8YBSmmFCewfNEpQ_lrKh3jIr-uwZ_Q_67OGxch3x8b4P115ItSlbfxUE71zo5DA_XSu_6y2Dthl6-Bw_EkZpp9x0p5eB9GTWeeJHDgHfgzXEQfkdwOe1jCjAxRNtnPGtjS0sRfA1tZ3CdomKD17NYQivk1YCj1yJdcN7wKb-QSeH0Cz3avgVA4UiGcxTBjU0nMWrLf5PWcS9L9Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
محكمة الجنايات الرابعة بدمشق تحكم بالسجن المؤبد على مفتي الجمهورية السوري السابق الشيخ أحمد حسون.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88423" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88422">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي   بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88422" target="_blank">📅 11:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88421">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f67556e45.mp4?token=bH1k0v-iUaBPiI9jUHNqqO6nVtlu7M6IWUkIyxntvgaBZSySVf_XDnpgX2FDOSUEP4OBdAftVdgXoqbQV1exDbAQ9mapG3AijlaxrBA6uXaqneNcBOL1cIGFltpwkmySudqt-pJ9LeqgCXa_eNEKvG8eAcBxrMsXEybNRpJkmrZhjRXo5j2h9kESNmD9kL_48Xyb94mXLk_Xds__V4T4ZLCQU5JuLccEigBbZ_LHmKtrmfq_aluNE2efLE9RVGCOq1T585Jn11I3USMqw2X8QD6Mq1x3OPtgZY1lfQtReQGyarEz-e886wGHgxpD6oA0sJrS-rYzavijxBpAx-BivA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f67556e45.mp4?token=bH1k0v-iUaBPiI9jUHNqqO6nVtlu7M6IWUkIyxntvgaBZSySVf_XDnpgX2FDOSUEP4OBdAftVdgXoqbQV1exDbAQ9mapG3AijlaxrBA6uXaqneNcBOL1cIGFltpwkmySudqt-pJ9LeqgCXa_eNEKvG8eAcBxrMsXEybNRpJkmrZhjRXo5j2h9kESNmD9kL_48Xyb94mXLk_Xds__V4T4ZLCQU5JuLccEigBbZ_LHmKtrmfq_aluNE2efLE9RVGCOq1T585Jn11I3USMqw2X8QD6Mq1x3OPtgZY1lfQtReQGyarEz-e886wGHgxpD6oA0sJrS-rYzavijxBpAx-BivA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
الخارجية الإيرانية:
أمن إيران والعراق مرتبط ببعض، ويجب أن تكون حدود هذين البلدين آمنة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88421" target="_blank">📅 11:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88420">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQVTbQ9nq1dvS60CPiFfCEGzeYncDGdSe8dYZYZqMEoDAPXr3u7ylhfWSiTm81eIgHdvmi8Ggtzy0D4f25dBTIUiT2itW2mVOvxx_bzzsFMQPloWTyICaN-8lS3TJ3mKrfOYo94lYu90HINCAZAZc80tglj9BOVGgbPiJdl-GqEmuruzrMiazB4XKrdF9JEk4Fk2Zy5bkKF1TXID0pYfs9UAv9uqhjA5N81bjrWiHfYIFqE0MEibnfR63G4aJZSoIlqF0flEEV0PaNm4Ynqi8SPM9A8jIHUg16gtcfMj8s9VUdadtiVcEkFICE3WlqFE-1EZ92iggsA7-n8e8iS0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88420" target="_blank">📅 11:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88419">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88419" target="_blank">📅 11:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88418">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253e1af33a.mp4?token=Ig31a44LZUCCyoe4do-pwtYJwkDi8WVutMha2BMOnARiAFRiyAhRQdfo9M2peM3pL9BP1UefHOJZPuOtS3F_5oIjSkKRVlpP0hIV4xPhOfwvCl7fCjRz7heBkUWy4IpjCFfJyG-jS4RrZT3-BOuS5Movpd6szOuMNzhMqS1AN35Z1KskcTB9pT12F7Qnm1gzI2CPnISergtXsJ4ODx-2QG64KtUFENe6bVIbTBVNF4ExpmcjE7RUuqqoLZ8jm11W2hikxIuStXsAa6irM6RFjux9-04MjMWKX-vk7a2cJX55-tD3F0BClyz30_mQok_W2ZxA0-jn0N4xQOjk0fAXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253e1af33a.mp4?token=Ig31a44LZUCCyoe4do-pwtYJwkDi8WVutMha2BMOnARiAFRiyAhRQdfo9M2peM3pL9BP1UefHOJZPuOtS3F_5oIjSkKRVlpP0hIV4xPhOfwvCl7fCjRz7heBkUWy4IpjCFfJyG-jS4RrZT3-BOuS5Movpd6szOuMNzhMqS1AN35Z1KskcTB9pT12F7Qnm1gzI2CPnISergtXsJ4ODx-2QG64KtUFENe6bVIbTBVNF4ExpmcjE7RUuqqoLZ8jm11W2hikxIuStXsAa6irM6RFjux9-04MjMWKX-vk7a2cJX55-tD3F0BClyz30_mQok_W2ZxA0-jn0N4xQOjk0fAXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط طائرة حربية تابعة للقوات الجوية الإندونيسية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88418" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88417">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By9E0LNWkXe4J126bED4QYr2CivNU0T38de-sKaTksD2nGi93o3vjoptHqKimWTJSQWNpJPuhtGkPfpBPlHoIZEbCPqdEFfNp8vDGjnA6YmOUGartuzMROyxTylmzAb-MYWEbDRX67MhE8HsnHWImt7-1yFxC91Go-50vavZg6woefxkwRm-7r9A8xj7XMkxe_890f_HiYE3HTDVDTj-Z2j-jTwNtsS_qC7cpR3izyIYKWZSRDlSGTLjDT_0eFMAIiawX9XIL4hDgVmND8gMe-m9XoEABbk8lmzh4z1LARUJ-AOecgY31tAjEYHAXwDXWQeEIhiCDrrTguylI1jwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسقط وصاية توم باراك على العراق والشام</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88417" target="_blank">📅 11:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88416">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ba72a77c.mp4?token=OeSkFeX8Xj9U4Ux4SOOYTWn-kRd8Ga7Vn5-eCJ8R5XdF9JYWuT0DDup6uREGnlHS3tnFcOCMlhGqHZeajSeWkGx4VaIH2jnYnYh7YGJhKH9zjxKLdmPcNiVfoQYtUtHMQjqBr7Jd042IcruUQioiQ7Oy8p9IX4iQSlMaq8-0BNNhGGX6P3uTsic_AQEShOtWhttpXYZzdHMJWt0x0sIfEh-1rZoFcuENiL4DHlYKqsRW0CqPcLQJoy0M9I_Gb3PP2Vi7XVYKYsy2NVnYJb8jMn2AM47nk6gY5D74KjoEvrl3osauDgsFusnLzWPx_-xuYajCi1E4uSCPJkynNVuDqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ba72a77c.mp4?token=OeSkFeX8Xj9U4Ux4SOOYTWn-kRd8Ga7Vn5-eCJ8R5XdF9JYWuT0DDup6uREGnlHS3tnFcOCMlhGqHZeajSeWkGx4VaIH2jnYnYh7YGJhKH9zjxKLdmPcNiVfoQYtUtHMQjqBr7Jd042IcruUQioiQ7Oy8p9IX4iQSlMaq8-0BNNhGGX6P3uTsic_AQEShOtWhttpXYZzdHMJWt0x0sIfEh-1rZoFcuENiL4DHlYKqsRW0CqPcLQJoy0M9I_Gb3PP2Vi7XVYKYsy2NVnYJb8jMn2AM47nk6gY5D74KjoEvrl3osauDgsFusnLzWPx_-xuYajCi1E4uSCPJkynNVuDqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث بإسم عشيرة الهركي: لا نتائج إيجابية خلال الإجتماع مع وزارة الداخلية والأمور تتجه نحو التصعيد ضد قوات البيشمركة التي تستمر في إعتقال الزعيم خورشيد الهركي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88416" target="_blank">📅 10:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88415">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
القضاء الإيراني:
شحنة نفط أمريكية تم مصادرتها وبيعها لصالح مرضى "الفراشة الجلدي" بأمر من المحكمة الإيرانية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88415" target="_blank">📅 10:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88414">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lF5BcI2tlZkY8nBfCa_yYl0vVq1nxrEb09GjX9Tim_Q0j1PXlKFa-EnqglfEqWndRKu2HV38zTYGPyogjN3TJ1ZU7sHaJVCrCM4TtI1vAvE62GEnaDY46AF8rDz2kjzBGQW4fb2RGz4Jx2riuQPeBmFCzQgo0Wx1yg86PSJl_j_s9RswIkk2VSRbn8_0XHbvpqgadrjGbSGzFlMjdMjgbiQlSYP-3tmd0iKXrG4i_KeS2ZpQ-5LwJeeI68aQ0TOUBlX1lArRE16pzKqPsbA6n4lIryOugIuM8d-6JaAkX--c-gtXHhfFgnBEFuvwW1JAOm1KiyrmE70QIEVAXnyW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي   بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88414" target="_blank">📅 09:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88413">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocx58hsdIruiaPXa_KyvlqL3KnVov5IEl4WLl1iCdaUyRmshm6Ti6N4sQa2gasSfCdZLmhMEMCBDSSSHUfVbL_O5X3vZ2JubAKs_7LSgABSU7uTLm1GULCcrHv34uP_c3j1NMXescwX9-g5QlDjefYLj38QIEMchltiVE6MHRHNcVImqH7E4WLVs0h1E8Xc4QBa80H5QVywMOyJWItibUefPY6WRH-o69sm-AF6rHxBGFPqVVSfwQohjdbJZtYGz2z9oz5KAuyuqNRKremP9OPeZLaL_vjLCAmNChC3ZcvzLAQVsntHxUhcGraJKW3sewh4mvG48jSvRWlBvxXe93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي   بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88413" target="_blank">📅 09:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88412">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رشقة صاروخية باتجاه السعودية الان من أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88412" target="_blank">📅 08:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88411">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88411" target="_blank">📅 08:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88410">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي
بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88410" target="_blank">📅 08:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88409">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نايا - NAYA
pinned «
كُلَّمَا أَوْقَدُوا نَارًا لِّلْحَرْبِ أَطْفَأَهَا اللَّهُ ۚ وَيَسْعَوْنَ فِي الْأَرْضِ فَسَادًا ۚ وَاللَّهُ لَا يُحِبُّ الْمُفْسِدِينَ
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/88409" target="_blank">📅 08:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88408">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">كُلَّمَا أَوْقَدُوا نَارًا لِّلْحَرْبِ أَطْفَأَهَا اللَّهُ ۚ وَيَسْعَوْنَ فِي الْأَرْضِ فَسَادًا ۚ وَاللَّهُ لَا يُحِبُّ الْمُفْسِدِينَ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88408" target="_blank">📅 08:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88407">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=oqypcBZS9ijwO_yM-l2pFaGpByWjMwPo2CgsvyGOa2vyDLRHeXuDiHGAnF8bgIVkJJSiK4a5s_srnNcnQ5Z2WRZtoR_z5pCQVudhfGU0Nm89Uf7CJ5KTLXgWxRyyL5FxmNoTplf32dGkQ6rQUaeo0ScQ2NgQLjn9h6CPuJ5N-6VZGvz7NGzz3Kuh3rPBAtN0KSK1gdvoFowZ12y_zCE5gkXTzLPoHbueIWmnPx71b4Fn9gJLF82F-N7zMKa6ASBmoWFfa6NDDFzL_6-73cx_0_1ohFJL1wRkrRMU-p5LHPOJH037Qk9HLz6Bw9lFJpFD9XMVjsSSKl-n7hCAjL-mKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=oqypcBZS9ijwO_yM-l2pFaGpByWjMwPo2CgsvyGOa2vyDLRHeXuDiHGAnF8bgIVkJJSiK4a5s_srnNcnQ5Z2WRZtoR_z5pCQVudhfGU0Nm89Uf7CJ5KTLXgWxRyyL5FxmNoTplf32dGkQ6rQUaeo0ScQ2NgQLjn9h6CPuJ5N-6VZGvz7NGzz3Kuh3rPBAtN0KSK1gdvoFowZ12y_zCE5gkXTzLPoHbueIWmnPx71b4Fn9gJLF82F-N7zMKa6ASBmoWFfa6NDDFzL_6-73cx_0_1ohFJL1wRkrRMU-p5LHPOJH037Qk9HLz6Bw9lFJpFD9XMVjsSSKl-n7hCAjL-mKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88407" target="_blank">📅 08:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88406">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔻
دوي إنفجار عنيف داخل أحد مقرات مرتزقة السعودية في مدينة عدن اليمنية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88406" target="_blank">📅 03:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88405">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">إطلاق نيران كثيفة صوب مصفاة لاناز في قضاء خبات بمحافظة أربيل.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88405" target="_blank">📅 02:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88404">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq3-U5CBxcQ85Yf9WT6l8C2xu_bF01JV-ttnCPzMcj84N-VaK7zcvHBJdw55XzSGgEXoj1ujUD0RqrY1HJxzp7T26tmIO9DXGHSW4ByATf3gR5F4JV0I01Rl2RxQwrfNQB-0__2LSeW8gzwR-1dHSheCBfumamdULUCmQve6z86HEll5NCpNrsOR9WYtBEVuxEvgbqtTxcjb2ugLUR8kWI8qk9Y33b-613HcZrA4NRGYL6rQaFd-VBrRShsECzCfK1QXO-gLxdXiYMR9lSrdH47vBA62X_m9ScrXmTHvM8zGSZ8r6qnyej9byxHjZ4_V58oUm4NFLHbUPNZmeiVHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اربيل امن وامان</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88404" target="_blank">📅 01:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88403">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aa2b6b21.mp4?token=Gr7ZOFAc4oDY7Hdr51dfBBul7StY-gQnaRx6NZTMy4d-vqQIhcbF0TkOdWkHQX64IkEoV4Z9-ieEN-tkgCiKCGy96fbKoiY8zThXSekz_lS49j7ZFA0hLwH4289Y5l9DuDLZMoHSOaz5nC4qmaGaO6dArhSXowzzgHuNTBDHt2rhPcrn_yX-NTg11QA5i92bGFgAeKRtyuNpxzLfygJAC9PQVmbiQA6ulECezgGAZJR_0MNlVlfPhRbi6gxF8juEPNpT24XIMMEauOmUr2RgdUG_-bncRfGuBB40NYyNjksJmlY8VipBdcnGvIIkIFvevASuVn409H_9JLuZgcqT9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aa2b6b21.mp4?token=Gr7ZOFAc4oDY7Hdr51dfBBul7StY-gQnaRx6NZTMy4d-vqQIhcbF0TkOdWkHQX64IkEoV4Z9-ieEN-tkgCiKCGy96fbKoiY8zThXSekz_lS49j7ZFA0hLwH4289Y5l9DuDLZMoHSOaz5nC4qmaGaO6dArhSXowzzgHuNTBDHt2rhPcrn_yX-NTg11QA5i92bGFgAeKRtyuNpxzLfygJAC9PQVmbiQA6ulECezgGAZJR_0MNlVlfPhRbi6gxF8juEPNpT24XIMMEauOmUr2RgdUG_-bncRfGuBB40NYyNjksJmlY8VipBdcnGvIIkIFvevASuVn409H_9JLuZgcqT9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العشرات من عشيرة الهركي يتوافدون الى منزل خورشيد الهركي لمواجهة قوات البيشمركة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88403" target="_blank">📅 01:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88402">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2921b037ec.mp4?token=Sj5OEeJLOWk3prj7pv9YbuhW_VUfeBKG5fpvOa8Dj1Tm6L8ZAUv2yrhVCXeVyeqKaMWCCbUIw2qLPwckWQhGeJw-iSVxACRYu1nI6wbuaOo69HMZavcUOBAlcT71In5T7_OcttqDSbx4NPqifmA0oyG7DKJITQBgDeo5-WJoyW7QQnbCq0zzHZssa5adNCzwTlO92GL6a_h9UiVnR-cEw7kXcl0JvWCZIjgcfJeuAchLiEXKMS3py5cHJYEsnqYaw6ms8KB80Y3QQi0kIqEXorND1_gxwChVv53AIhIBg0zCFPrkBvV1aWktHz-giR5YNCLdZ9TN-8I7Olugdo_aiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2921b037ec.mp4?token=Sj5OEeJLOWk3prj7pv9YbuhW_VUfeBKG5fpvOa8Dj1Tm6L8ZAUv2yrhVCXeVyeqKaMWCCbUIw2qLPwckWQhGeJw-iSVxACRYu1nI6wbuaOo69HMZavcUOBAlcT71In5T7_OcttqDSbx4NPqifmA0oyG7DKJITQBgDeo5-WJoyW7QQnbCq0zzHZssa5adNCzwTlO92GL6a_h9UiVnR-cEw7kXcl0JvWCZIjgcfJeuAchLiEXKMS3py5cHJYEsnqYaw6ms8KB80Y3QQi0kIqEXorND1_gxwChVv53AIhIBg0zCFPrkBvV1aWktHz-giR5YNCLdZ9TN-8I7Olugdo_aiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وسائل إعلام كردية: خورشيد هركي أبلغ أبناء عشيرته ببدء المعركة ضد البيشمركة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88402" target="_blank">📅 01:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88400">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ca1f3d6d.mp4?token=fTpJM7GbIDUXjuRggfKwZintVc56je6Dv25vtLHEb-LKVPDatsnIC4mEJ_3vItclQMqRQy9GLPd8JeeDQNEm4N-FgfpgPV3s-gRfxmE9Z1B6buAuhvrIV0B4u8AmqM5ipM41gq-7OHJ2cQ3dUhGVdNzh3K3PUr3vKhnowrJg-Uvq6_hcFpTS2hsbLc1HJ4sV9A_Pg0zqkmb_WXixWp8qCaIJryScgSvz1eSURCsLV2u9R_Kvv5YMqfyEs4DWJ_9diFSR73RN1BJV7zMhnUpgQ1cVdJqjkP9xnnTgcLeQbxch-ZY18PIw0qb2_3gH6mvh53lR0PONO6WChF1Uy9m7JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ca1f3d6d.mp4?token=fTpJM7GbIDUXjuRggfKwZintVc56je6Dv25vtLHEb-LKVPDatsnIC4mEJ_3vItclQMqRQy9GLPd8JeeDQNEm4N-FgfpgPV3s-gRfxmE9Z1B6buAuhvrIV0B4u8AmqM5ipM41gq-7OHJ2cQ3dUhGVdNzh3K3PUr3vKhnowrJg-Uvq6_hcFpTS2hsbLc1HJ4sV9A_Pg0zqkmb_WXixWp8qCaIJryScgSvz1eSURCsLV2u9R_Kvv5YMqfyEs4DWJ_9diFSR73RN1BJV7zMhnUpgQ1cVdJqjkP9xnnTgcLeQbxch-ZY18PIw0qb2_3gH6mvh53lR0PONO6WChF1Uy9m7JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبادل إطلاق النار بين عشيرة الهركي ومليشيات البيشمركة في محيط مصفاة خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88400" target="_blank">📅 01:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88399">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8833d650.mp4?token=WTBjgpbNQ86ALLsVW2f5RqVm2-d7wAQ4DUJ9nNaYpQfpidtRWXE6CSNt0FpDY9TQdwe2UM6bvLm1olOAdZSDVafYDvpqRG9M-aZdVfDJWNJv_Cid4-Hn65_6dYhPCi4DNM5OUJeObVasWbzmK1vp5_XRkFJq2AHNaInsDd-R5kybpc-9RFZ6WgWxlNoXyQdN3GDXofa1CsCexb2At_2eqQVOc2FMSAavSU_8bwhgupEZ0if-pK6i6aXT7olNSxC9mXht-sj38euTb5wd7nkerAj1QoQIVmifIQN3_ApcTONl4eRhOSpbIAZQLb3paPy4JJmLwCJzhn4scMihghDlEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8833d650.mp4?token=WTBjgpbNQ86ALLsVW2f5RqVm2-d7wAQ4DUJ9nNaYpQfpidtRWXE6CSNt0FpDY9TQdwe2UM6bvLm1olOAdZSDVafYDvpqRG9M-aZdVfDJWNJv_Cid4-Hn65_6dYhPCi4DNM5OUJeObVasWbzmK1vp5_XRkFJq2AHNaInsDd-R5kybpc-9RFZ6WgWxlNoXyQdN3GDXofa1CsCexb2At_2eqQVOc2FMSAavSU_8bwhgupEZ0if-pK6i6aXT7olNSxC9mXht-sj38euTb5wd7nkerAj1QoQIVmifIQN3_ApcTONl4eRhOSpbIAZQLb3paPy4JJmLwCJzhn4scMihghDlEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلبية لدعوة خورشيد هركي.. مسلحين تابعين لعشيرة الهركي ينتشرون في محيط مصفاة خبات بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88399" target="_blank">📅 01:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88398">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4890b6251a.mp4?token=HNOegkx_PNJhKmwvdCZWs4ED7fsjn5sXKCmptoDux7vRCzJwKMYHE-RjJwW5PsmBDh64fmFT9DyIc_AZBadt42AmnuGj4E0y6zzf4_PM4hTC3pprbExSh9FDPoFvxT3SP0soA9neJx0G7Z0hfai-83l_KitDCHK1IhVPqKTeXZ_4yxK1oN05FIqYEa4GBOFcGAaW5LtrznPSKAWZZLWs2CL2HkfigIGHi5o5OWUWxCnzDuoO0DwqRsR0jN4W7eXTFafDW2P6mLp4C6doQpqIwwvpLJvMkxlXGckc4F9olNZVGnc_C9urslwaiUH6vg9r-GbuTfTZBvzON4VYm6vpdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4890b6251a.mp4?token=HNOegkx_PNJhKmwvdCZWs4ED7fsjn5sXKCmptoDux7vRCzJwKMYHE-RjJwW5PsmBDh64fmFT9DyIc_AZBadt42AmnuGj4E0y6zzf4_PM4hTC3pprbExSh9FDPoFvxT3SP0soA9neJx0G7Z0hfai-83l_KitDCHK1IhVPqKTeXZ_4yxK1oN05FIqYEa4GBOFcGAaW5LtrznPSKAWZZLWs2CL2HkfigIGHi5o5OWUWxCnzDuoO0DwqRsR0jN4W7eXTFafDW2P6mLp4C6doQpqIwwvpLJvMkxlXGckc4F9olNZVGnc_C9urslwaiUH6vg9r-GbuTfTZBvzON4VYm6vpdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وسائل إعلام كردية: خورشيد هركي أبلغ أبناء عشيرته ببدء المعركة ضد البيشمركة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88398" target="_blank">📅 01:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88397">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
وزير الخزانة الأمريكي:
أي عمل عسكري ضد قواتنا أو ضد دول الخليج سيرد عليه الرئيس ترمب بسرعة وحزم.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88397" target="_blank">📅 01:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88396">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ارتال إضافية للبيشمركة تتحرك تجاه قضاء خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/88396" target="_blank">📅 01:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88395">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/962b98f198.mp4?token=KDDowD2fweewadtRy6gw5FLt3FjMXqC0uDhsOyGUIUWC8AVydkYEfamKy613nzRSshx-WUDi7p2Ovkh11o6I00Rx7XNHEuThWDUSuEQQBD1AfJO3Eiafs86JDTWYaCKO3RWoJ8-frqsOYNHOgd_Riu407IrtD5H_ChfopLMcmFuPAfjq76uM89hUiD6PWMLtQaiMKtdpnwA0B1Mm3ZGC_PmfvaJFhkxZL_3j-QjDW3o5G5fTfGuIPrBupiW6cikN1_cbCqu79YewyBUlKpC7KOA517G2b02BGTppA5W5IlAJ-MagQGN5uP7r_iZXLAoRE1le7MGh9RJ4VIHt-jAHKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/962b98f198.mp4?token=KDDowD2fweewadtRy6gw5FLt3FjMXqC0uDhsOyGUIUWC8AVydkYEfamKy613nzRSshx-WUDi7p2Ovkh11o6I00Rx7XNHEuThWDUSuEQQBD1AfJO3Eiafs86JDTWYaCKO3RWoJ8-frqsOYNHOgd_Riu407IrtD5H_ChfopLMcmFuPAfjq76uM89hUiD6PWMLtQaiMKtdpnwA0B1Mm3ZGC_PmfvaJFhkxZL_3j-QjDW3o5G5fTfGuIPrBupiW6cikN1_cbCqu79YewyBUlKpC7KOA517G2b02BGTppA5W5IlAJ-MagQGN5uP7r_iZXLAoRE1le7MGh9RJ4VIHt-jAHKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعزيزات عسكرية كبيرة للبيشمركة تتوجه نحو قضاء خبات بمحافظة أربيل لمواجهة عشيرة الهركي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88395" target="_blank">📅 01:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88394">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a0d3bee.mp4?token=vYb5HAZdxjnKIS_ycB9SbHpGIMAj3guqJV0zjIYFm-ZknJ6j-KGiNHRUoGYNV198v85qGIaqKUoe26k0zEfE9VWMGlbmXWXtQc9qqkp50B05S10ljCNpIdY7BtHDXN_TOxdcdqNaTw3HljrgV3lf2nm_2wWWibsAPFeneCsHXfiCbksgzUWHc_EhyznQBbJYvmWb2GqIrljaU76Gb0hFgPh9FPlmG4wMoF79kUuj6BngtI8SzvnvyWWDyWN2AQ8BlGG7JKFkPVS2NOmdOHt512GRWLP93zxCSlND63EkdGSIg1TK2BS0CsR6zStcrAqFz8eJOJZj4DSD4mYSrTCw7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a0d3bee.mp4?token=vYb5HAZdxjnKIS_ycB9SbHpGIMAj3guqJV0zjIYFm-ZknJ6j-KGiNHRUoGYNV198v85qGIaqKUoe26k0zEfE9VWMGlbmXWXtQc9qqkp50B05S10ljCNpIdY7BtHDXN_TOxdcdqNaTw3HljrgV3lf2nm_2wWWibsAPFeneCsHXfiCbksgzUWHc_EhyznQBbJYvmWb2GqIrljaU76Gb0hFgPh9FPlmG4wMoF79kUuj6BngtI8SzvnvyWWDyWN2AQ8BlGG7JKFkPVS2NOmdOHt512GRWLP93zxCSlND63EkdGSIg1TK2BS0CsR6zStcrAqFz8eJOJZj4DSD4mYSrTCw7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات عنيفة وتعزيزات عسكرية من كلا الطرفين تتجه صوب قضاء خبات.  البيشمركة حاليا: السيطرة تحت الوضع
😆</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/88394" target="_blank">📅 01:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88393">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d19f9e5.mp4?token=dYzjNoWbi31zgWVjU5-kEp_3YGk-Lh5bcawnGg2OO6yxFOdd3vYhR_OofQgjAiN4aaa63VDh_37UCTaZPOFZRaBgQhLRpV3y4H6LzP-t8yaV8M0HfJ9W2NdptoTzxwNM8YYuXUDQYBWXSZqDl4RSJNgm9BIVZg9hOgDw0Y3_-wSnu2XBp9cYm0mHgC__qAXnXKF-anRzwv916f-W0Bo95kuRsTWR9uhzDpbgCD6yNiwz0vHY5KLyHzG085FrM8m-fk-2MFpzWUX_LiC2wXaz2_6PFC_lB-Ejq9d4yGU1YVOu8G2UTQXEeEPg-syO8QkqgNMfvv94za9I28D_wFSzYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d19f9e5.mp4?token=dYzjNoWbi31zgWVjU5-kEp_3YGk-Lh5bcawnGg2OO6yxFOdd3vYhR_OofQgjAiN4aaa63VDh_37UCTaZPOFZRaBgQhLRpV3y4H6LzP-t8yaV8M0HfJ9W2NdptoTzxwNM8YYuXUDQYBWXSZqDl4RSJNgm9BIVZg9hOgDw0Y3_-wSnu2XBp9cYm0mHgC__qAXnXKF-anRzwv916f-W0Bo95kuRsTWR9uhzDpbgCD6yNiwz0vHY5KLyHzG085FrM8m-fk-2MFpzWUX_LiC2wXaz2_6PFC_lB-Ejq9d4yGU1YVOu8G2UTQXEeEPg-syO8QkqgNMfvv94za9I28D_wFSzYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خروج مسلح كثيف لقبيلة الهركية مع غلق معظم الطرقات المركزية في محافظة اربيل.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88393" target="_blank">📅 01:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88392">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f58106d3.mp4?token=PQhh1v61J5nMNb9niuwfdE9LBQgQHGi8ffYJDkvzMzx7Gm0AHPFbbMuKgFXYQX6DXERqfK8IKdccRqCOXlaTYIr6sFRlNHgi8qbWEOIWJtOncMMhmD0w4dX9hSUHcoDL3vibZWMn83rxag7iowPylCQ29zepcIjoSoUAmty9tFIalXu-3dZ0ECqYljMNsxWZ45zkY31jsCDecO5mSoUcZEt43CuC3OjiVLDk8vIOCIPCSaV4tzWSlzqCUi5yPvyD6RJrgFgMMXBQJPIT8dGokCj9hI2Cz1XFPy22E0Da7Hhl7AOWJ_YDC2tQYFoLxU17061VIC-VSUQkuCwE1AI7pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f58106d3.mp4?token=PQhh1v61J5nMNb9niuwfdE9LBQgQHGi8ffYJDkvzMzx7Gm0AHPFbbMuKgFXYQX6DXERqfK8IKdccRqCOXlaTYIr6sFRlNHgi8qbWEOIWJtOncMMhmD0w4dX9hSUHcoDL3vibZWMn83rxag7iowPylCQ29zepcIjoSoUAmty9tFIalXu-3dZ0ECqYljMNsxWZ45zkY31jsCDecO5mSoUcZEt43CuC3OjiVLDk8vIOCIPCSaV4tzWSlzqCUi5yPvyD6RJrgFgMMXBQJPIT8dGokCj9hI2Cz1XFPy22E0Da7Hhl7AOWJ_YDC2tQYFoLxU17061VIC-VSUQkuCwE1AI7pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عبر نايا   مراقبون أمنيون يتسألون عن دور مدير مكتب القائد العام للقوات المسلحة العراقية الفريق الركن الأول عبد الأمير الشمري والمشروع المكلف به   بنزع السلاح و ان كان يشمل هذا الأمر ايضا اقليم كردستان العراق وسط حالة سقوط المدينة وخروجها عن السيطرة الامنية…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/88392" target="_blank">📅 01:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88391">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
عبر نايا
مراقبون أمنيون يتسألون عن دور مدير مكتب القائد العام للقوات المسلحة العراقية الفريق الركن الأول عبد الأمير الشمري والمشروع المكلف به
بنزع السلاح و ان كان يشمل هذا الأمر ايضا اقليم كردستان العراق وسط حالة سقوط المدينة وخروجها عن السيطرة الامنية . ام ان الأمر منوط فقط بسلاح وسط وجنوب العراق .
نعم لحصر السلاح المنفلت</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/88391" target="_blank">📅 01:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88390">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bdb6ffa4.mp4?token=CoCZxquhZDrsBpiR5glX-5TZ4sbQfVNS-D__O2rFNccTk72IhkvKazPwXx3NEH9GAV8ZyipYf40MA3PHNa6K20QHgDDGN3XXjnB7KrmcE092jtxTpkvEwNsclfzaxgcnUNs-Ze5vhnPE0JCah5NLC_1s_UVzuaYb0xFPHuu1hCrLt48PxV0POLWqYXd4I0xzFkT_o3HjwKkqviRKhaq_xBPYTYcOn8gCfIR5qyxPyJE54Um8wkK42G1r4UK12XJpmN3L0B4C1qHMiN82rEazbDjwztq_x3pPPXcwP6BzFE_tsl1mRi5mPwLShgL2Bjmwc75clhHvtVx_2ai4VPCK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bdb6ffa4.mp4?token=CoCZxquhZDrsBpiR5glX-5TZ4sbQfVNS-D__O2rFNccTk72IhkvKazPwXx3NEH9GAV8ZyipYf40MA3PHNa6K20QHgDDGN3XXjnB7KrmcE092jtxTpkvEwNsclfzaxgcnUNs-Ze5vhnPE0JCah5NLC_1s_UVzuaYb0xFPHuu1hCrLt48PxV0POLWqYXd4I0xzFkT_o3HjwKkqviRKhaq_xBPYTYcOn8gCfIR5qyxPyJE54Um8wkK42G1r4UK12XJpmN3L0B4C1qHMiN82rEazbDjwztq_x3pPPXcwP6BzFE_tsl1mRi5mPwLShgL2Bjmwc75clhHvtVx_2ai4VPCK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تستمر تحشيدات الهركية في قضاء خبات استعدادا لمواجهات اكبر مع البيشمركة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88390" target="_blank">📅 01:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88389">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20747c723a.mp4?token=k02v1vOVLexGSpV8jPE3pJqgdigPQYtFUL2M5Lgz-bQ8DMi82WO4EenSKiiG20lQ9LUN9Wf65kzEfzjX-t3mwue1k-rSwwhVSjh6G8pxTy12Pix75rtDuHAieeHVBI9I5kLQcw716dV3kncNFlnsgYxirCbL-7ff_IHmfvM6xdflm_Y4GG0uRtCbW-yAHg6TH-eypz8qmEUGtgL8kbNTpck50a2I8QICOdwFUpOY_QNzJJhvVraLwwFhfJkQgZ68W_tfOmatc0sGEDd58h6ri1m8u0moCCacZL4jfwKbk-mHz3nxLLNZcb2HnUvDYmcDP-C8JM9LKmbI5As-lPcFHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20747c723a.mp4?token=k02v1vOVLexGSpV8jPE3pJqgdigPQYtFUL2M5Lgz-bQ8DMi82WO4EenSKiiG20lQ9LUN9Wf65kzEfzjX-t3mwue1k-rSwwhVSjh6G8pxTy12Pix75rtDuHAieeHVBI9I5kLQcw716dV3kncNFlnsgYxirCbL-7ff_IHmfvM6xdflm_Y4GG0uRtCbW-yAHg6TH-eypz8qmEUGtgL8kbNTpck50a2I8QICOdwFUpOY_QNzJJhvVraLwwFhfJkQgZ68W_tfOmatc0sGEDd58h6ri1m8u0moCCacZL4jfwKbk-mHz3nxLLNZcb2HnUvDYmcDP-C8JM9LKmbI5As-lPcFHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
لمن يتساءل عن أسباب الانفلات الحاصل حالياً في محافظة أربيل... تعود خلفياته إلى خلافات بين زعيم قبيلة الهركية في قضاء خبات والحزب الديمقراطي الكردستاني.  وكان زعيم القبيلة قد انضم إلى حزب بارزاني، إلا أن خلافات نشبت بين الطرفين لاحقاً ما دفعه إلى الانسحاب…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/88389" target="_blank">📅 00:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88388">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفلات امني في محافظة اربيل شمالي العراق بسبب اعتقال خورشيد هركي وعدم الافراج عنه.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88388" target="_blank">📅 00:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88387">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d4806f03.mp4?token=FCJRw03F6rc0ZS75wngjBsERcJ3yYumWGmvlYnPlt4Ueuw_NdLqa0O35LWaKaJ_Gf3z235i3-ibFuX512-vJYeWqDL80yxbXIDAC0TjVvLk_qggZMAgDWrGE_xBz5ozHJ37ljSfBSVqm7LFMlfIruoQLSWRVmrIhcxwge4aJNOwg9tGXSSWE2H4kreL9g9zRENVvmO-L26aMhSciHcSkiFcjdZDatElLZkKySZ3Xp4cL0xB1s0STCuqmBX8wN4JllRC-TxBieWy0dz04Kx0gd0epChJ29Q8FOESiXFPHW8pff-Zaasfd9hFMzf4mh2k-e6QVWc6JEI-UP6EK9rtCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d4806f03.mp4?token=FCJRw03F6rc0ZS75wngjBsERcJ3yYumWGmvlYnPlt4Ueuw_NdLqa0O35LWaKaJ_Gf3z235i3-ibFuX512-vJYeWqDL80yxbXIDAC0TjVvLk_qggZMAgDWrGE_xBz5ozHJ37ljSfBSVqm7LFMlfIruoQLSWRVmrIhcxwge4aJNOwg9tGXSSWE2H4kreL9g9zRENVvmO-L26aMhSciHcSkiFcjdZDatElLZkKySZ3Xp4cL0xB1s0STCuqmBX8wN4JllRC-TxBieWy0dz04Kx0gd0epChJ29Q8FOESiXFPHW8pff-Zaasfd9hFMzf4mh2k-e6QVWc6JEI-UP6EK9rtCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بمختلف انواع الاسلحة المتوسطة والخفيفة تبدأ مواجهات بين الهركية والبيشمركة بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88387" target="_blank">📅 00:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88386">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3162c91ec2.mp4?token=pSF44hxN1-jKzM0BKKbVpoR0igsELhoCWATznY1sYgJIK-QvTCgkM6GGKbe4hjt983zLdiID_st1K7LBnnOO-J8b58egIzHKix4AQ63g9OSkP3qbZcTTMlSufd358HwRgblcjLSWs81VmnpMEJAAN9XeBU-K_UCKhI2pTdd4IBGhkYtuGIa8mi6DNNQzB9o8H5QfBUvjywq6cikSBqMmM2R2HI6-eIgt1YzvNdl6Om11m7U4MMTxQdKyNc2b_se16CG0HuwiFd3B8QxP1wBguXdx7PT3--GB6s_tdoCPXqlL-kbAQEz5vJcAMjNoFdj4bclk6iVUcD55f2XfW3ttMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3162c91ec2.mp4?token=pSF44hxN1-jKzM0BKKbVpoR0igsELhoCWATznY1sYgJIK-QvTCgkM6GGKbe4hjt983zLdiID_st1K7LBnnOO-J8b58egIzHKix4AQ63g9OSkP3qbZcTTMlSufd358HwRgblcjLSWs81VmnpMEJAAN9XeBU-K_UCKhI2pTdd4IBGhkYtuGIa8mi6DNNQzB9o8H5QfBUvjywq6cikSBqMmM2R2HI6-eIgt1YzvNdl6Om11m7U4MMTxQdKyNc2b_se16CG0HuwiFd3B8QxP1wBguXdx7PT3--GB6s_tdoCPXqlL-kbAQEz5vJcAMjNoFdj4bclk6iVUcD55f2XfW3ttMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
البيشمركة ترسل تعزيزات عسكرية ضخمه لصد الجماعات المسلحة التابعة لخورشيد هركي.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/88386" target="_blank">📅 00:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88385">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ef949d38.mp4?token=kShZA5Xa3thXoPjV5BXCYhxm15gT_A85rZfu1O_hZUX3Ixfq_L2PPFUNM8fBXroMAwmWQPQKrjtBlADLrjGJ1eZjAGrDQWSquNEDTDwDMvD4LLqqDzd2qHUN1DjL_S7_8em4-CBNtCkbhZhAKbceuK5kicxBK7Dwr_D7eM_VCKdmCcfbTeEjCR87fnJmC33RNGh-unGuYVij3qZ3wb769AKKbTXY111nKQs-QaqyVkwSzyI-4nidUFVrYCiJM9xdUA_8Y7W955S7U_HLLyxmkB8_753qVfWqhRP0avk5LwLzqexTECgxo1oSINGaHCEsI-tsvR-9ihmLkbyVw5_FuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ef949d38.mp4?token=kShZA5Xa3thXoPjV5BXCYhxm15gT_A85rZfu1O_hZUX3Ixfq_L2PPFUNM8fBXroMAwmWQPQKrjtBlADLrjGJ1eZjAGrDQWSquNEDTDwDMvD4LLqqDzd2qHUN1DjL_S7_8em4-CBNtCkbhZhAKbceuK5kicxBK7Dwr_D7eM_VCKdmCcfbTeEjCR87fnJmC33RNGh-unGuYVij3qZ3wb769AKKbTXY111nKQs-QaqyVkwSzyI-4nidUFVrYCiJM9xdUA_8Y7W955S7U_HLLyxmkB8_753qVfWqhRP0avk5LwLzqexTECgxo1oSINGaHCEsI-tsvR-9ihmLkbyVw5_FuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات عنيفة تدور بين الهركية والبيشمركة</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/88385" target="_blank">📅 00:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88384">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
تحشيدات عسكرية ضخمه تابعة للبيشمركة تتجه لقضاء خبات لمواجهة الهركية.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/88384" target="_blank">📅 00:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88383">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba261dcac7.mp4?token=CG6QwsVhh6ppjfCmZTRujMHltwSryakdvJE46YXFXPiCtPWHwHdcLOyxYeIqWFnslzO_ZdmbpNZmHPwnGpqH1nwzw3HuMYFdSvOfFeB0xhQFwMC0qEaQShLmMHZ_RxXMY7px6f7xhxXTuI-DPBtfrLoYx5sJw5NVEpxJ1g5lwEDqApPYZgrGXAomGNxFmu_FbLndb3lQvZIGkzzpVNQ-WLcdKSwuaPnOzfPLqu6e3dhbt_jWwi93lYEiIgqumm5vbJuyRZQ4P_tEFRTYfGb_HojzfYUgbR_iGtXdO-wvFfN-Yl_mhQDVDeKIeBfjKavmC5p6ZZ0smxhqzHTY_-cSzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba261dcac7.mp4?token=CG6QwsVhh6ppjfCmZTRujMHltwSryakdvJE46YXFXPiCtPWHwHdcLOyxYeIqWFnslzO_ZdmbpNZmHPwnGpqH1nwzw3HuMYFdSvOfFeB0xhQFwMC0qEaQShLmMHZ_RxXMY7px6f7xhxXTuI-DPBtfrLoYx5sJw5NVEpxJ1g5lwEDqApPYZgrGXAomGNxFmu_FbLndb3lQvZIGkzzpVNQ-WLcdKSwuaPnOzfPLqu6e3dhbt_jWwi93lYEiIgqumm5vbJuyRZQ4P_tEFRTYfGb_HojzfYUgbR_iGtXdO-wvFfN-Yl_mhQDVDeKIeBfjKavmC5p6ZZ0smxhqzHTY_-cSzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
البيشمركة ترسل تعزيزات عسكرية ضخمه لصد الجماعات المسلحة التابعة لخورشيد هركي.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/88383" target="_blank">📅 00:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88382">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083ed6f065.mp4?token=XR6uxvFRT58WsQ0mko-q0pRtKMuHXin8xqk9xXIi_wn8lP5A4Mb2LmXdMbuvWiFZkTL62NBzVukzXPJFlsrOFgoTzSnZRQL-lxqRIRmOkEvK-lO4afDFyIGc1_Pu35mwCLEgQvC3MC9-MgyIPXXSQKsTlvxM_PxIzN2CmwN1YltCilmejtfVmFT7YsrE4UkqDeU8j3MIlMzTp-zHoCS7WwGMm-lvc5SzwfDt9PEzTVW1wy-IjMFxx6NGfmNKar4U730GnxgijjdWu64AXTY3gUgfwBuBqsLTfNaAo5td-6-tPslL8Jgh2uMW6tRseQabM8JoQpxoJtxNgVtUntNNbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083ed6f065.mp4?token=XR6uxvFRT58WsQ0mko-q0pRtKMuHXin8xqk9xXIi_wn8lP5A4Mb2LmXdMbuvWiFZkTL62NBzVukzXPJFlsrOFgoTzSnZRQL-lxqRIRmOkEvK-lO4afDFyIGc1_Pu35mwCLEgQvC3MC9-MgyIPXXSQKsTlvxM_PxIzN2CmwN1YltCilmejtfVmFT7YsrE4UkqDeU8j3MIlMzTp-zHoCS7WwGMm-lvc5SzwfDt9PEzTVW1wy-IjMFxx6NGfmNKar4U730GnxgijjdWu64AXTY3gUgfwBuBqsLTfNaAo5td-6-tPslL8Jgh2uMW6tRseQabM8JoQpxoJtxNgVtUntNNbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الجماعات المسلحة تحتشد لمواجهات اكثر عنفا مع البيشمركة بعد انتهاء مهلة اطلاق سراح زعيمهم خورشيد هركي.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/88382" target="_blank">📅 00:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
الجماعات المسلحة تحتشد لمواجهات اكثر عنفا مع البيشمركة بعد انتهاء مهلة اطلاق سراح زعيمهم خورشيد هركي.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/88381" target="_blank">📅 00:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a009d53.mp4?token=JNSJzqljHlEWuV12FHpnhrBvcfdx4Ecb8vURovdbUlgY61hZu0URTnS9uM1CUJRZ0bUTmG2neevK3PvZx6g8d9vy3MyKjv6qy4409D3i1bdXE4WgCiFAAIPxdh0CstOaEEEtpGeoBmk4LnaKT2wvmi2LqxFyQZRR0FpRZecRP5_uIBozAEDMbbOnjV4-1T-Z5wl3ZQlYy14Q_29dgGzFYUShsIb9G7hh0diz9eHYGfaiPxj72KYyAefywLvq_KR5gNc3Myr7sq52EcFpffwfSVRNhrI1VgAGy0o7BKO5xS3cM1WXrWjntnnfkyalFPpNUKir6yhB4v5DIbZpywJVvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a009d53.mp4?token=JNSJzqljHlEWuV12FHpnhrBvcfdx4Ecb8vURovdbUlgY61hZu0URTnS9uM1CUJRZ0bUTmG2neevK3PvZx6g8d9vy3MyKjv6qy4409D3i1bdXE4WgCiFAAIPxdh0CstOaEEEtpGeoBmk4LnaKT2wvmi2LqxFyQZRR0FpRZecRP5_uIBozAEDMbbOnjV4-1T-Z5wl3ZQlYy14Q_29dgGzFYUShsIb9G7hh0diz9eHYGfaiPxj72KYyAefywLvq_KR5gNc3Myr7sq52EcFpffwfSVRNhrI1VgAGy0o7BKO5xS3cM1WXrWjntnnfkyalFPpNUKir6yhB4v5DIbZpywJVvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الجماعات المسلحة تحتشد لمواجهات اكثر عنفا مع البيشمركة بعد انتهاء مهلة اطلاق سراح زعيمهم خورشيد هركي.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/88380" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88377">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e7020797.mp4?token=NvphfJbYOoQ5f3XzuU8mvh7bid9aPVs25RzlrC9wooCrkRbDjuv6h2ffI8Jr02QrCsGRtdgcSqqcKyIHyEXPWx3s45ZGvQ8lj6wzndRz5jKkdGl6KpJAT4d1vv8kjSfpq4rSI3gcaXd997Z3_0Gn2Q-EynHAXyPPVyng_4Oln9KWdz51IbSN7acrq6THL4PhvsTVMBGba38gm54DLFolxP1Vvrww2eQsdniThkmVCZCQwInGjsepWIeRemFGh5zjA-CZR4EZ1PzQ2cDKzMflIWqwPPaRTqIfEg1_5yeUe4z7ndavRd2HEaSRtOYV9BXAmgVlsG3FLtE_A-LvKp7NpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e7020797.mp4?token=NvphfJbYOoQ5f3XzuU8mvh7bid9aPVs25RzlrC9wooCrkRbDjuv6h2ffI8Jr02QrCsGRtdgcSqqcKyIHyEXPWx3s45ZGvQ8lj6wzndRz5jKkdGl6KpJAT4d1vv8kjSfpq4rSI3gcaXd997Z3_0Gn2Q-EynHAXyPPVyng_4Oln9KWdz51IbSN7acrq6THL4PhvsTVMBGba38gm54DLFolxP1Vvrww2eQsdniThkmVCZCQwInGjsepWIeRemFGh5zjA-CZR4EZ1PzQ2cDKzMflIWqwPPaRTqIfEg1_5yeUe4z7ndavRd2HEaSRtOYV9BXAmgVlsG3FLtE_A-LvKp7NpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق نار كثيف في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/88377" target="_blank">📅 00:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88376">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇹🇷
🇮🇱
🇸🇾
اجتماع وزير الخارجية السوري مع مدير "الموساد" الإسرائيلي لخص إلى تشكيل لجنة أمنية سورية تركية إسرائيلية لمعالجة المشاكل وتفادي أي صدام.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88376" target="_blank">📅 00:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88375">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇦🇪
الإعلام الأوروبي:
حذّر مسؤولون إماراتيون من أن "نتيجة سلبية" بشأن التحقيق الجاري مع نادي مانشستر سيتي لكرة القدم المملوك(منصور ال نهيان) بتهمة انتهاك القواعد المالية للدوري الإنجليزي الممتاز "قد تضر بالعلاقات المحسّنة مع المملكة المتحدة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88375" target="_blank">📅 23:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88374">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e86b62545.mp4?token=L3SbcAfzl5Gc2NLJiAa2Zi-9tz5vs7SNQ6wcpTlrEJGtOKOkq1rMz9Gkky_uMB7OM_egToCBquqbr0-BMyUeUH1yg7uZBXaX_2XA_ooVvGT64E63Okjk49BoOJZDEqvFOWlPUUpmviydJWlOHU9rhe11LhGV0XhHvwrqgqKjsFBdpPO0jln7UzyoISvRfI94S3sMK-_JrKGhn8z6eM25PwiYcwy5VhDsXJoj_WtZYvRU0pf0QQFAkpJW_svFO3_tGsTeCCI6uMQ3tJFzNfXPO3MIfjmM4pOgOZerN5pZBKoKa0gfWj6G0MODM0Wio-vxZofe9tckJ5Tmw0m5WYxjCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e86b62545.mp4?token=L3SbcAfzl5Gc2NLJiAa2Zi-9tz5vs7SNQ6wcpTlrEJGtOKOkq1rMz9Gkky_uMB7OM_egToCBquqbr0-BMyUeUH1yg7uZBXaX_2XA_ooVvGT64E63Okjk49BoOJZDEqvFOWlPUUpmviydJWlOHU9rhe11LhGV0XhHvwrqgqKjsFBdpPO0jln7UzyoISvRfI94S3sMK-_JrKGhn8z6eM25PwiYcwy5VhDsXJoj_WtZYvRU0pf0QQFAkpJW_svFO3_tGsTeCCI6uMQ3tJFzNfXPO3MIfjmM4pOgOZerN5pZBKoKa0gfWj6G0MODM0Wio-vxZofe9tckJ5Tmw0m5WYxjCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تسريب غاز سام في حقل خباز النفطي بئر رقم 46 في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88374" target="_blank">📅 23:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88373">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
تسريب غاز سام في حقل خباز النفطي بئر رقم 46 في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88373" target="_blank">📅 23:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88371">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
المستشار الأمني لرئيس مجلس الوزراء العراقي:
الفصائل ليسوا أعداء للدولة بل هم جزء منها،رئيس الوزراء لن يرشح لولاية ثانية وهو رجل المرحلة الحالية، قدمنا مقترحا إلى ايران والسعودية لإنشاء مجلس تنسيقي أمني موحد، ظروف المنطقة وراء عدم موافقة بعض الفصائل على تسليم السلاح حتى الآن، سلاح الفصائل سيكون قوة للدولة ولن يُسلم إلى أي طرف خارجي.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88371" target="_blank">📅 22:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88370">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
هيئة الممرات المائية في خليج فارس:
بسبب انتهاك بعض السفن للوائح الإيرانية المتعلقة بالعبور عبر مضيق هرمز، ستواجه هذه السفن قيودًا مثل الغرامات أو الاحتجاز أو المصادرة في عمليات العبور المستقبلية  .</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88370" target="_blank">📅 21:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88369">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇹🇷
🇮🇱
🇸🇾
اجتماع وزير الخارجية السوري مع مدير "الموساد" الإسرائيلي لخص إلى تشكيل لجنة أمنية سورية تركية إسرائيلية لمعالجة المشاكل وتفادي أي صدام.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88369" target="_blank">📅 21:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88368">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
طلب من سكان المنطقة المحيطة بقطاع غزة الدخول إلى مكان محمي بسبب الاشتباه بوقوع حادث أمني.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88368" target="_blank">📅 20:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88367">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id0Qozkqt6QraaeIzPHVFLaHkYCMH_iBHBubazVdcqR8sWb9arepNwORwIalGKCuSTo2kXcrbFwcjUZrIMmZZH2P-7Bd3uK-9EP7S3vBtDdKetqiDa3s7jGVaRca2t_GtAYVJgbJ8qkZU5Qe_jTXni8p8lUXyKGT5fyu07SFGuIj-Fb_4IKnU-jHzS95GVTBaQdE2S5ZxxuhDLCjqwAKdoHAQ_GUsXS8_Mxv4pq0QgOCJPSJpUHS9SBg_ktSLFElRQp6CuJpLdGackGWomPhdDxT93nIXYt513wNULUfRYNEj211Pjty2ezFj4bWlz1FMRPGPLBBBnqISsc6Xm8Mdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ممثل السيد مجتبى الخامنئي:
- نتوجه بالشكر والامتنان والتقدير إلى المرجعية الدينية في النجف الأشرف، ممثلة بالسيد علي السيستاني، وإلى الدولة العراقية
- نثمن دور الأجهزة الأمنية والحشد الشعبي وأصحاب المواكب وجميع المشاركين من الرجال والنساء والأطفال في مراسم التشييع
- الشعب العراقي سطر ملحمة تاريخية في التضامن الشعبي والإسلامي بحضوره الفاعل في التشييع المهيب
- نشيد بأصحاب المواكب وأبناء الحشد الشعبي وبصمتهم في إنجاح المراسم
- حب القيادة العليا في الجمهورية الإسلامية للشعب العراقي لا يخفى
- العلاقة بين الجانبين تختلف عن سائر البلدان، لما يجمعهما، جذور راسخة ومحبة مع العراق
- السيد مجتبى الخامنئي وجه شكره لكل من أسهم في إنجاح مراسم التشييع ومراسم الأربعين، التي قال إنها جسدت عمق التلاحم
- برنامج وفد السيد مجتبى الخامنئي في العراق محكوم باحترام الشعب العراقي ودولته وسيادته ومؤسساته</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88367" target="_blank">📅 18:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88366">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
الجمهورية الاسلامية تعلن الموافقة على تكلفة المرور عبر مضيق هرمز في لجنة الأمن القومي</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88366" target="_blank">📅 18:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88365">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇱
🇸🇾
إكسيوس:
اجتماع بين مدير الموساد الإسرائيلي ووزير الخارجية السوري.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88365" target="_blank">📅 18:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88363">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KXvNw_sZBLR52pTVUHbyveiiP3jP5o4nhk_OldT950yul0xSdOgJVCfJPD1KiqZHQmhr4DEnu6G40CHImDXPNjUMsfU4VVDMKLITV3B-xvqzLs9cD9oKCliF93dpvnlTwrOHRsajQTMF_FgzaJuUQEKuQjkxdvOypddxlzvp4zMTbeGzsdWbLn_NeIznJqzAKz6JkbjfiUGHHDgL8ZCV7RrrW5ZzCvMShejW2copuAAsLN10aVxDD-bh9OlixRTHmOI_zRfAQt2bjrgYHpltAxFj_dGXCqjIDE6Wi44t1DFuLQolX-vxCxWJVi1YJNO0dqdAoC0V-FT6mapTfT8mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkCdu6oP9PA1uJLnesnI9rSd2a6M224kgxMELJ8CeXAQ5ib1le7itl7zy_El6W8FeA0zRPuQmBfJq_A2rCCCS6B2CNZUJVCNO2i0IqV38b-fXrGVJvmyF1whBcBN4_cvJUkO6W6ggcEYEvBlrVrgWRRyU1X1DQoHF3vzTuMShxSCyj7aOEQ1zIf6xLisRDdrocobEyZHPL3iCY4hrEiMJncvAa76zNz2WiNBnxTYJIDTT6kedQFgDTpxw_mUKxrmB5hTYrVaTOCI-0bYOVQUVQsDxh_7QlVxtbklFhDdinM386R6p3EEHWXoCVPL38rMFuykg3rc7Emqe-dcn1s2BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
رئيس هيئة الحشد الشعبي فالح الفياض: هناك من بذل مئات المليارات من الدولارات لمسخ صورة العراقيين وتغيير هويتهم.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88363" target="_blank">📅 18:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88362">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
🔻
رئيس هيئة الحشد الشعبي فالح الفياض:
هناك من بذل مئات المليارات من الدولارات لمسخ صورة العراقيين وتغيير هويتهم.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88362" target="_blank">📅 18:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88361">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_Ny77Lcp2e_Mhh9l8n3Y1XcS40vgvWN0N5j2p1-lLPVWZNrTAtC-7ZGKhiLUEZmpaO49pFsMYlrLwUtZS5EL4_Z3aiNuGSWmAB5mTVf_eTO-sd57ieZspHm1ht27LT5E3sJAwGVVI0W4X_ATRN9TavahdXBrRBu7vCDCFjMqQEaKFjG3P2nnreg-09iUmdctZX2kywPLNdJfQm8WSYO_ChNOlCEvOLA32TFNe67eR8RL3PKeHI5uDE5NSDdL2kp-tzcsPiWJoHH8fKy_4pvG2MFv7qyuLMGPsPRdVI0xSgLL4HrH-fOyIWOaUiPb3CWh-nKW5miOJ3WuxVrCEhFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
:
استيراد اللحوم المجمدة لتحديد أسعار اللحوم. حسناً، قد ينجح ذلك.
‏ما هي الخطة المتعلقة بالسندات وتجميد عوائد الواردات؟
‏هل توقف مشتري المنازل عن شراء المساكن؟
‏تجميد الرواتب كأجور؟
‏تؤدي السياسة الخارجية الجامدة إلى اقتصاد جامد.
‏الشيء الوحيد الذي لا يزال يتحرك؟ البوميرانغ الإيراني.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88361" target="_blank">📅 17:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88360">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اغتيال زعيم المافيا القوقازية يانيس يوشبايف</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88360" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88359">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حدث امني في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88359" target="_blank">📅 17:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88358">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حدث امني في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88358" target="_blank">📅 17:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88357">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇱
نتن ياهو:
هذا هو طائرة الـ F-35. هل لديكم طائرة بدون طيار في المنزل؟ يمكن أن تكون بنفس القدر من الفتك.
إذا جاءت بأعداد كبيرة، يتم تجهيزها بالأسلحة؛ إنها دقيقة للغاية، ومن الصعب اكتشافها. منذ عدة سنوات، نعمل على إيجاد حل لمشكلة الطائرات بدون طيار. نحن الأكثر تقدمًا في العالم، ولكن هذه مشكلة عالمية.
لقد رأينا ذلك في أوكرانيا، ورأينا ذلك في لبنان، ورأينا ذلك في إيران، والآن يحاولون تجديد ذلك وإدخاله إلى غزة.
تعليماتي إلى المؤسسة الأمنية وقوات الدفاع الإسرائيلية هي أن تفعلوا كل ما هو ممكن ضد هذه الأداة الفتاكة: أن تضربوها، وأن تضربوا من يشغلونها، وأن تضربوا المكان الذي يتم إطلاقها منه.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88357" target="_blank">📅 17:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88356">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
من الحريق الذي اندلع داخل مصفى الدورة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88356" target="_blank">📅 15:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdeeeac9dd.mp4?token=EntpzpMvt6gVrRilIUuDk0TtqA_O-QvCtZ5h5xxanYCX4ZnfyCQvrIlb3lgM0pL0Dd_wxRIrO4jn-R6jOORVZ2J0_iRbDnApvZ6KkOfCQKi66okaC7sHVyQH_Mj-5S6ENx1p2dn3fxAOJPWvlln8kUqbb2LjX2ozpUCdeaRSzJY_gSKGF6i1YxthjXe2SGrM_06_kzYbzQZTLyXM9y29pJYsKuOaQfu8wvGggS2ILQbzz70yu3DpVRNt7B1oknLCuetykopDx_IYnpcGKa9o78QPzQu-JuhN9iTXV7s3wx9JuFSknMPBAsicAHHzUwQHfN8AsIjcFWCsMGzad-mSmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdeeeac9dd.mp4?token=EntpzpMvt6gVrRilIUuDk0TtqA_O-QvCtZ5h5xxanYCX4ZnfyCQvrIlb3lgM0pL0Dd_wxRIrO4jn-R6jOORVZ2J0_iRbDnApvZ6KkOfCQKi66okaC7sHVyQH_Mj-5S6ENx1p2dn3fxAOJPWvlln8kUqbb2LjX2ozpUCdeaRSzJY_gSKGF6i1YxthjXe2SGrM_06_kzYbzQZTLyXM9y29pJYsKuOaQfu8wvGggS2ILQbzz70yu3DpVRNt7B1oknLCuetykopDx_IYnpcGKa9o78QPzQu-JuhN9iTXV7s3wx9JuFSknMPBAsicAHHzUwQHfN8AsIjcFWCsMGzad-mSmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من تصاعد اعمدة الدخان في العاصمة بغداد بعد الحريق داخل مصفى الدورة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88353" target="_blank">📅 15:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
مشاهد من الحريق داخل مصفى الدورة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88352" target="_blank">📅 15:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88351">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cb36e6ce.mp4?token=BplU-fbMV3hiWCt7OQWzvYb9BYYTnkPMiKgktCJnVx0YV0Kd8XUnyepKjl4cyZYWdXS0hZ5OYzgwrnweqLJ0FqkvRKCLwMEoCaSWKlcxZt6kklrHvienNW8QTisDK4kpuCJYICvHejY8PU-fIZFVr0a8NvLWHoB4ViW8SW7jHbvwrQ--5crMimsvoNvwGK034KexzjnqOUEqRb4r0oR8ntSdLBwBjOXgseS2-wHibiya3w1ydCM57aCYsZvGUO6Uvrc7xZ-tnYRsZyrbMCaorh7K56z6NGeu4NRAgzs9UfALhr_sIhL6gBw6KTSYT6InfEZaqsCVZNRgobcNnqRFYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cb36e6ce.mp4?token=BplU-fbMV3hiWCt7OQWzvYb9BYYTnkPMiKgktCJnVx0YV0Kd8XUnyepKjl4cyZYWdXS0hZ5OYzgwrnweqLJ0FqkvRKCLwMEoCaSWKlcxZt6kklrHvienNW8QTisDK4kpuCJYICvHejY8PU-fIZFVr0a8NvLWHoB4ViW8SW7jHbvwrQ--5crMimsvoNvwGK034KexzjnqOUEqRb4r0oR8ntSdLBwBjOXgseS2-wHibiya3w1ydCM57aCYsZvGUO6Uvrc7xZ-tnYRsZyrbMCaorh7K56z6NGeu4NRAgzs9UfALhr_sIhL6gBw6KTSYT6InfEZaqsCVZNRgobcNnqRFYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من تصاعد اعمدة الدخان في بغداد وسط انباء عن اندلاع حريق داخل مصفى الدورة</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88351" target="_blank">📅 15:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88350">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPldplDDOP-Jr14sHKbbmQbI7-n4OvUakvUU-MrmHsHG_cQKGYwx1h2ggUWvnkwH22cku5kk8UOYNAl1COYlqSNyoiqWhREHDHhQ4ccBgCD5aIOK0yfea6hDNTHzkkUC5Uwrs_9-irDENKvsGgZ3k4UoLFRvp2ftZs5zxVtWmHyF3tcqzgmPrVN4D1nWKKW20o-neg2NxLBwG-KCjLfFXXeb_vOJ2918RAptnU9Eyz37FXzPO8mzRbybXNGjleB1RJVAD2j_J67ZP0mYa0hP0qSgwGWltJLgPtO3n256h-8yRgQsBDcqVT4msunKNyGuQbFbfv62NB4R1GcX1Tn2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حريق كبير داخل في منطقة الدورة ضمن العاصمة بغداد وانباء اولية على ان الحريق داخل مصفى الدورة</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88350" target="_blank">📅 15:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88349">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية: هيئة الرأي تقر فرصة امتحانية استثنائية لطلبة الثالث المتوسط والسادس الإعدادي
ويؤدي المشمولون الامتحان ضمن دور خاص تعلن اللجنة الدائمة للامتحانات العامة موعده لاحقا، كما حددت الوزارة مبلغ 50 ألف دينار للطالب الراغب بالاستفادة من الفرصة، وتخصص لتغطية أجور الامتحانات ومستلزماتها.
وتكون هذه الفرصة استثنائية ونهائية، ويعد العام الدراسي 2025–2026 آخر عام لتطبيقها، فيما يرفع القرار إلى مجلس الوزراء للمصادقة عليه.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88349" target="_blank">📅 14:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88347">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ0VSkOO0AxqzuNSOesAQiI4-bGKiHyKTkpEB_LYHz9NOw4IBjdW29VJFMdMFanYTgPGaQ9G4pZVNUhtL2YAScv5wdJBLoPUymDrgIeg30b5TjN2ArvWORsY_U0h4bzJCApu1qwucjybpkMBKqfyVC4KssULLrPvHXWnDLc2VxUGvTvYXOUDAZI7twblnIgR64pc51u0bmkWCuXACx01uxcTlFdB3Ep6R0h4tsA8vfv2h2Z2PkP1rwiVk_lZ0udyf9GuzB_rkLNpREGbzxKcz_6W1HT9f6_YHpMeF1ulVntkqVwi8TfiddMZReJibFOFfbYnEemdLLochj3VEsFrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظ على نظافة بلدك من اتباع يزيد</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88347" target="_blank">📅 13:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88346">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
قائد فيلق القدس التابع للحرس الثوري اللواء "إسماعيل قاآني":
القضية الفلسطينية، من البحر إلى النهر، أكثر حيوية وقربًا من التحقيق من أي وقت مضى.
توسيع المستوطنات وجرائم الصهاينة هي محاولة للهروب من الأزمة والجمود العميق العسكري والأمني والسياسي والاجتماعي في الأراضي المحتلة، ولا يمكنها إخفاء الهزائم الاستراتيجية التي تكبدها منذ السابع من أكتوبر وحتى الآن.
القضية الفلسطينية هي حلم حيّ ودائم؛ حلم سيبقى قائمًا بمساعدة الله حتى يتحقق نصر الحق.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88346" target="_blank">📅 11:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88344">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTCvgfRr5mRdepngsx2GfZ9M26Potvgadn3lxZlgTTDcKUGenAmjI7_mPRi5yZPD3ulO2fNQGw8OSI1jCk4DzH4OoyTki8kQVa0ZEeKHvBaoNMuUElT8GLPL-pXVYFjbjBrthdlpoWufgHPluvQ0OgR7oSTrz40sYpFF9PLf_7AaS30vtCgzN7A8nH0ZxgwxZnPPLUCsMPfsCipoLu4G-sjogwK5Ibm1nDqC-b105ar4qQWxBKzSegAT8YSvH7punHr15qxxxTSGVLiVMF_qGVIeIQDpFkPR1SQbbb4QxGJkA6tNKcIgRBN9OCECe6M_kujtmVsotd-cMjI0eGpXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqQ1R9LvHaQNr_G4286OKnG52A9JnqV3bRTe71tATYSEHWN3k024riJ4Ny_O8fZIALnKOTUO0nrd-zEtpFeUAmHfAz_2wLY4rai1P02ojrLUeLc2__X781Ubt9eh4Xa3LncxDgvtSlXkO-NPI0AqBeEdca3wkjs1vl52C_Dg7poHJZWWkMD1J_O8u0iMr2lq9SuBJICG10h-orTG1-RpnbIWFqSghRe6nlP-vlyT74YykbasWy3UBIBkWS49_Xq3HVHL20kOQFsVi5xp5KCsM7yWV_EvMu60vq_pyT18Fw9fca2kaXexhUurXxOdQACPl1a474ZELpBl2FyVwCi6rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
منتخبنا الوطني للسيدات يخسر ثاني مبارياتهِ الأسيوية في بطولة كرة الطائرة أمام الصين تايبيه بثلاثة أشواط دون مقابل؛
"انتم مال دولمة تخربوا بالطائرة ليش"</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88344" target="_blank">📅 11:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88343">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏
🤡
زيلينسكي: اتفقنا مع ألمانيا على توريد 600 صاروخ اعتراضي من طراز PAC-2 خلال عامي 2027 و2028</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88343" target="_blank">📅 11:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88342">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
الإعلام السعودي:
قائد الجيش الباكستاني سيحمل رسائل أميركية لإيران خلال زيارته غدا.
‏زيارة قائد جيش باكستان لإيران ستحاول كسر حالة الجمود واستئناف المفاوضات.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88342" target="_blank">📅 11:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88341">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇸🇾
🇮🇱
وزير خارجية الجولاني:
نتوقع استئناف المحادثات مع إسرائيل بشأن اتفاق أمني قريبا.
سوريا تمد يدها للدبلوماسية وتحث إسرائيل على اغتنام هذه الفرصة التاريخية.
الاتصالات مع إسرائيل انقطعت بعد هجومها على قاعدة أبو الظهور الجوية في 18 أغسطس.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88341" target="_blank">📅 11:07 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
