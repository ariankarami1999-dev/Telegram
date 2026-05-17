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
<img src="https://cdn4.telesco.pe/file/uLiHrKmQFDwRAfoSbjxhO_8raEwUasQgOerVISzeMq7oSTKEWbPy2KmpYEw1WJv5hQZZDS2OdsYhyXLAUbe2e0hKcFtq7mId3E8tX__hqxzu4kgoAMGY4RABJBHDaE0nHoQmLfqdXaHB6xdh33L6Uh6kGkWyyWLyYS-l40l7j8_kkSiV6LjrcrIQkSyhpp9eZ5zj_mC0HwOvUybj1CHsw2SblQhCEDHc1w2ACrEK_JRKp6vpWjRvnslTjuTIaztklNA2-nllcGz2sSkZVDZs7211rE52bOEU30dC_smyLKuYroJSUtZwLZGaNbQsfmuC_yedHDfjccwjXGJbQrjxeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 15:06:57</div>
<hr>

<div class="tg-post" id="msg-652649">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b9dba7fe.mp4?token=JLGnqA5oUz4dzjNCj108PCiS-JxiZJbzwFzhgAoK5Goi61eq_udJxsxFEMmBbWwy6B-PL0Q2a_kyRWwzPjFyITbohi4y5yaz6hD36n3wlUcDD_fstteCtf9qwocNKbWhGxYpndInQce-6o-toDT8w-AsyH8mug1dwM1ORHyuINg0zv0VaN7whCE_Mx-11QwpZ0KJ2GNzcfNv3_skne-xAobTaO0-htrWOOI4dopf8IvxqNWxJnkhZERqaGPhz8bKkDjMoJZ_YS5zxVaqD75qgNDZcIGiSxaBiwGPvrGmheg7VeOoNwCJeynpRS58OiF1OnZ9LOp7G_dTaDIypO2AADmuMdmXrndJtcw4_M-2nSGIUC5pfUlxTvJAq7zL8XOjPkySA4LmPQml9AJA7Iyikkf_BqgAVrP6oE112wqwr2xqKVPmql_HkIZxYtTI-_hdLvoy62-Rb2GHvdLjwc2wKRVayvoTG1Gfc6v40zqJ60BCzCUiPbKOnC2ox7aES2LJvKV8bpo1h9yTaea2WeL4R5d7zrrS14wbs3nAh1U3ys0CTTVfP2-prJM9Gn37YL1Xk6qb1oH8s7uxN3IsYoS01jQV8T8p0BkqLcSfSXExhfG5Wb6AhU0JD164H3rbC6nAD27tuK8HabPfJBkqR4iopXUgHehWPmrowqgWB8EGDwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b9dba7fe.mp4?token=JLGnqA5oUz4dzjNCj108PCiS-JxiZJbzwFzhgAoK5Goi61eq_udJxsxFEMmBbWwy6B-PL0Q2a_kyRWwzPjFyITbohi4y5yaz6hD36n3wlUcDD_fstteCtf9qwocNKbWhGxYpndInQce-6o-toDT8w-AsyH8mug1dwM1ORHyuINg0zv0VaN7whCE_Mx-11QwpZ0KJ2GNzcfNv3_skne-xAobTaO0-htrWOOI4dopf8IvxqNWxJnkhZERqaGPhz8bKkDjMoJZ_YS5zxVaqD75qgNDZcIGiSxaBiwGPvrGmheg7VeOoNwCJeynpRS58OiF1OnZ9LOp7G_dTaDIypO2AADmuMdmXrndJtcw4_M-2nSGIUC5pfUlxTvJAq7zL8XOjPkySA4LmPQml9AJA7Iyikkf_BqgAVrP6oE112wqwr2xqKVPmql_HkIZxYtTI-_hdLvoy62-Rb2GHvdLjwc2wKRVayvoTG1Gfc6v40zqJ60BCzCUiPbKOnC2ox7aES2LJvKV8bpo1h9yTaea2WeL4R5d7zrrS14wbs3nAh1U3ys0CTTVfP2-prJM9Gn37YL1Xk6qb1oH8s7uxN3IsYoS01jQV8T8p0BkqLcSfSXExhfG5Wb6AhU0JD164H3rbC6nAD27tuK8HabPfJBkqR4iopXUgHehWPmrowqgWB8EGDwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فروش فوری ویلا جنگلی چلک ( نوشهر )
💰
قیمت ۲۰میلیارد اقساطی
📱
09128402035
📱
09115046100
🏕️
ویلا مدرن لاکچری
🔥
فول هوشمند ، داخل شهرک
🔥
✅
متراژ زمین ۵۵۰متر
✅
متراژ بنا ۶۵۰متر تریبلکس
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
قیمت ۲۰ميليارد اقساطی
⭐
اقساط بدون بهره
⭐
- تماس جهت بازدید :
🆔
شناسه:
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 466 · <a href="https://t.me/akhbarefori/652649" target="_blank">📅 15:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652648">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2c60a4a7.mp4?token=Fu8KdMSf1xYcBBf8aySdGICRw1ONG1fHjWBZs1ekNQa1tYXA2xDrvxLkeYg3X9QXinYyFPKEvbYW-tMY8pmPPZBLDSQ4kBtBIm95dQ_I5hM3-CTgDPiEW6MjJblufEBLfHCHDfTzG51vOappycW0GAUMYlNi7L3WpF_zqSDWxgxRUzuCTVpZ1hmbN9xH95DuW8g51iZhCjdvmj4vhGtFbF6ASvKIXVMKg0dHUt61Ly3N-IZeVazv7qhxKoQ82gC-9aI7rhVLr6LaUvCAltp3L1__XxrxW57U_pHTdMVD-lxf6e01iOcB_bylsEGE8dSeFUX_e64V2GcUS64AU_CN4IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2c60a4a7.mp4?token=Fu8KdMSf1xYcBBf8aySdGICRw1ONG1fHjWBZs1ekNQa1tYXA2xDrvxLkeYg3X9QXinYyFPKEvbYW-tMY8pmPPZBLDSQ4kBtBIm95dQ_I5hM3-CTgDPiEW6MjJblufEBLfHCHDfTzG51vOappycW0GAUMYlNi7L3WpF_zqSDWxgxRUzuCTVpZ1hmbN9xH95DuW8g51iZhCjdvmj4vhGtFbF6ASvKIXVMKg0dHUt61Ly3N-IZeVazv7qhxKoQ82gC-9aI7rhVLr6LaUvCAltp3L1__XxrxW57U_pHTdMVD-lxf6e01iOcB_bylsEGE8dSeFUX_e64V2GcUS64AU_CN4IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکید مجلس شورای اسلامی به نظارت بر قیمت‌ها و جلوگیری از گرانی‌ها در دومین جلسه بر خط مجلس شورای اسلامی
🔹
آقای حاجی بابایی نایب رئیس مجلس در نطق پیش از دستور خود کاهش فشارهای اقتصادی مردم و نیز ایستادگی در برابر زیادی خواهی های آمریکا را از مهم‌ترین اولویت‌های کشور عنوان کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/akhbarefori/652648" target="_blank">📅 14:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652647">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
متیو هو، دیپلمات سابق آمریکایی: اگر آمریکا جنگ دیگری را با ایران آغاز کند، بعد از آن دوباره مجبور می‌شود جنگ را متوقف کند چون ذخایر تسلیحاتی‌اش تمام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/akhbarefori/652647" target="_blank">📅 14:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652646">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d33189aaa.mp4?token=vzLl758i-j8hrdeC3DgbdCzuNHkPE-wxiLNA9WeigN5t3mVvI3mi3iWdqs7-hVRarmAy1-2cjqHBSziqM9Ildu0hR-TYWpol3wBbWLCyuZTjnaZqrA6fopfm2SFBt3do10Rd_GLefhEyZ9BrXsi1LTy6VtQ_KB2R1QwSaDIbKp0atKpUGxBwCbRt_6ucy8SeLC-yQ5ib9MWc6CqbP1Jt6Br-8m63fIiP0vfHaGc4XFguDvTQahvGBDInLPoNCgkxP-JyObQJrXXvc1k0wVccp-yW3KlDppQ0v8haQBEgoyZVuxJ-2Vp1bjbokFdmVvDB0LW8Wvs0uTBZlXlVymrL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d33189aaa.mp4?token=vzLl758i-j8hrdeC3DgbdCzuNHkPE-wxiLNA9WeigN5t3mVvI3mi3iWdqs7-hVRarmAy1-2cjqHBSziqM9Ildu0hR-TYWpol3wBbWLCyuZTjnaZqrA6fopfm2SFBt3do10Rd_GLefhEyZ9BrXsi1LTy6VtQ_KB2R1QwSaDIbKp0atKpUGxBwCbRt_6ucy8SeLC-yQ5ib9MWc6CqbP1Jt6Br-8m63fIiP0vfHaGc4XFguDvTQahvGBDInLPoNCgkxP-JyObQJrXXvc1k0wVccp-yW3KlDppQ0v8haQBEgoyZVuxJ-2Vp1bjbokFdmVvDB0LW8Wvs0uTBZlXlVymrL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: باید در کالاهای اساسی به‌ویژه گندم خودکفا باشیم
🔹
این راهبرد الان برنامۀ قطعی سالانه دولت شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/akhbarefori/652646" target="_blank">📅 14:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652644">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldFhYfoLuvDfAeFG-6JOv-aOmdlkYO8OluKjyXImEi7tuBrGeEEqnPtXJq3E1uZ2eLuY2_yrRkS-kDRT5TpDPIyLt1zp65y1F61XYJS_c0eGttPKWFMRgixtpjj4A0iulW1EK0QPDRRdB5t9d34CAOCVRRODFo9pvWDsDIG2BztC0QB7aJ3v2tZ87IeoHFbMBxyxVJra477wLYTmnITtJ4rR2nuEV-0tOJXgrnbuSuyQd3U3vG7wgGRG52SkIZ4HPJJBSCLB9Qp6Vw1TcGH_m2Iy5cenB_hN7QAe9n14bkkhjIHjJwQY3WHqpbRybHe21iK2zhRO3mcGInxenD897Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTL8-1izfuveLSUGTQlwHdTt6RKQZD62UI-UPR3LwBEBRRfGFEwjLMggQGFz4Eeri2J2is-WZ-HVpKxxDDnaArTI_VWyAOhRFd_WuGp6n5ql7lrQPGI7UBfNwWL1azprOTVF2zd0F0LNFhiyE6kaIgz_AMN2vbIMr4Z3Aft5eVEz8lCE2XdNNmDPxzQhITYhBwEazZe_WGBgAULj9XSp9_H4u9WNK6pCxo1qrG86PxKK-iMFlJHVE6qVgtDg6kaovP_3q8HeL4sTez6uM3EU3A9h4dUCuQmEakyTDvsWNp778hCZZSKVW1Mp2SwfiuxrjM5OrNMpZqADn3Zq5Ip0Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عاملان شهادت یک پلیس در ملارد دستگیر شدند
🔹
فرمانده انتظامی ملارد: ۲ نفر از سارقان خودرو و منزل که در جریان اغتشاشات دی‌ماه در شهادت سرهنگ دهقان مشارکت داشتند، ‌دستگیر شدند؛ در بازرسی از مخفیگاه آنان ۲ خودرو نیز کشف و توقیف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/akhbarefori/652644" target="_blank">📅 14:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652643">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAHa3wwZ7cpk5TI5eiI9vRFDKw4AknnqbDEo9-diOtkRbEIDA4_wD4mPjkoQTC0RJa8ePo4zrPApBBrS_K4rX7asTOix8gjvfmnjDrpZWZNia2lmNJ1zcar5ebgqL6FASIcemU0MmZ0ZDpdR15dqMkryi4kw3Y7IFe7YddfLbsBq6oxQ2GQVvEHYSed5bq3ispCKwU4K97q3CYuY8g5tiFH8QYEy3xuBQ85z9lrLAwEVTzflhpY5kmTPzWvbfA8qcP8KBI1LAi2vLAYzoTDqL3DqLJ695UxLgultga6OIFVKBMX-Pbx5Ke7hURqDcTyRKkuSwj0RLQLQngPibt260w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اتحادیه اروپا: بمباران تاسیسات انرژی ایران، راه‌حل نیست
🔹
مسئول سیاست خارجی اتحادیه اروپا کایا کالاس امروز در نشستی، اوضاع در خاورمیانه را خطرناک توصیف کرد و گفت «همه ما امیدواریم تنش بین آمریکا و ایران کاهش یابد».
🔹
او در اشاره به احتمال ازسرگیری حملات آمریکا و اسرائیل علیه ایران و تهدید متجاوزان به هدف قرار دادن زیرساخت‌های غیرنظامی ایران، گفت که «بمباران تاسیسات انرژی در ایران مشکل را حل نخواهد کرد و برعکس ممکن است مسائل را پیچیده‌تر کند».
🔹
کالاس به افزایش قیمت انرژی ناشی از جنگ‌افروزی آمریکا و اسرائیل علیه ایران و پیامدهای آن هم اشاره کرد، اما مدعی شد که این موضوع، تأثیر قابل‌توجهی بر کشورهای اروپایی نداشته است.
🔹
این مقام اروپایی همچنین دفاع مشروع ایران در جریان جنگ اخیر را تهدید معرفی کرد و مدعی شد که برنامه موشکی ایران برای کشورهای همسایه تهدید محسوب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/akhbarefori/652643" target="_blank">📅 14:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652642">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a833cedb09.mp4?token=e7Bf9Av8jOfG9eXwxbkoTl1MwWG8MzAeTDD5pt26Wq-dON4pePSNOr7L1WDbROiNnT9g45KK3w-5qe5Fs7cIRRkLlKnqqEWh3xPDOyPdvvDoSTmJZYxx0Vij2QeNyOFUSiVK8f4P_58ZyR0hZLM80VN4WHguUR2AwiMqrnAhkWqYeDhsggXDfn2hpuWnISeq3kEK6P4YEb3Pd9cah0neJtndlE1aJhQyhKlCLyu72R_LQwpscC-dO1g6yfiLqDRI72uIMNpuhhmhbVg60sXmTiM9s5V3YoAE2UDUaL_-DMsBjIvAVlYNjtsNpQ_8q8oo3bZQnyXRGA-0gVfZ1vVYFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a833cedb09.mp4?token=e7Bf9Av8jOfG9eXwxbkoTl1MwWG8MzAeTDD5pt26Wq-dON4pePSNOr7L1WDbROiNnT9g45KK3w-5qe5Fs7cIRRkLlKnqqEWh3xPDOyPdvvDoSTmJZYxx0Vij2QeNyOFUSiVK8f4P_58ZyR0hZLM80VN4WHguUR2AwiMqrnAhkWqYeDhsggXDfn2hpuWnISeq3kEK6P4YEb3Pd9cah0neJtndlE1aJhQyhKlCLyu72R_LQwpscC-dO1g6yfiLqDRI72uIMNpuhhmhbVg60sXmTiM9s5V3YoAE2UDUaL_-DMsBjIvAVlYNjtsNpQ_8q8oo3bZQnyXRGA-0gVfZ1vVYFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کالابرگ و بیمه بیکاران؛ دستورکار دومین جلسه برخط مجلس
🔹
نمایندگان مجلس در دومین جلسه‌ی صحنْ در سال جدید بر ضرورت مهارگرانی‌ها و افزایش قدرت خرید مردم تاکید کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/652642" target="_blank">📅 14:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652641">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
عارف: راهبرد دولت تأمین پایدار کالاهای اساسی و جلوگیری از گران‌فروشی است
🔹
معاون اول رئیس‌جمهور با تأکید بر ضرورت مقابله با گران‌فروشی، گفت: راهبرد اصلی دولت که در تمام جلسات اقتصادی دنبال می‌شود، تأمین پایدار کالاهای اساسی و جلوگیری از گران‌فروشی است؛ البته بخشی از دلایل گرانی کالاها به مسائل بین‌المللی بازمی‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/akhbarefori/652641" target="_blank">📅 14:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652640">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1273915b99.mp4?token=GwTeSjrh_pzjg7bOZEMT9EBDbPyTZt0v6ORBt3M5vcidagVcg5mse-6DxdVhJ9OkEJpLlM0dRneL1_msKctDJjjyZe4BdKG4J2X2UdPrXewC34s7emx34bHfs8bBluaLwGJiI_4IZIJlVOStqlHZ-BgptHJW8KGTv7C-kDFS6TtWx3gbtz8UtkUdyHpcF43NvzB0shgnp2Hvrua8OuVG3phJc_O_B7zs0cPJX3JQ56BpaMOgYW5ABteZFaJUE7uajkR0d1XieECGfMhBJHjoiEejha70brRXzhQUglDfynGaERaHWs0Z6ylqdlGCrrLzoyu9jR7fPPbIJIIkNmvSwRdjSvXQPZbaSsYUprKa0k7twDZmKj226DAEOCtKHauksgW84IUhJlmLgThGRIIJuYN9JynP-9f4OVd1e7rPhFUdBX6QnF8JguDyx3q1gtBxLr2Ra4nNsIHcnTfSRsugk0NK2SO7LEU4NS65dCyUAEyQ0idnG-E0CxNOLSn2gEDQ89SPL_YvXTxxk0tq3n44hntLJZH_4AzJrbKz6PMS1NVCy8HwmVo4ZzcykLKiA_pG24OioMLyBKqTd2osJ95k9LKDPnc-ELtZSC3juO_dBpjk1XkZ8D1xU1TRpvER23_pyddBNLvwAuXihXw__CVFUUtLnN0LQaVqMSqry_BItZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1273915b99.mp4?token=GwTeSjrh_pzjg7bOZEMT9EBDbPyTZt0v6ORBt3M5vcidagVcg5mse-6DxdVhJ9OkEJpLlM0dRneL1_msKctDJjjyZe4BdKG4J2X2UdPrXewC34s7emx34bHfs8bBluaLwGJiI_4IZIJlVOStqlHZ-BgptHJW8KGTv7C-kDFS6TtWx3gbtz8UtkUdyHpcF43NvzB0shgnp2Hvrua8OuVG3phJc_O_B7zs0cPJX3JQ56BpaMOgYW5ABteZFaJUE7uajkR0d1XieECGfMhBJHjoiEejha70brRXzhQUglDfynGaERaHWs0Z6ylqdlGCrrLzoyu9jR7fPPbIJIIkNmvSwRdjSvXQPZbaSsYUprKa0k7twDZmKj226DAEOCtKHauksgW84IUhJlmLgThGRIIJuYN9JynP-9f4OVd1e7rPhFUdBX6QnF8JguDyx3q1gtBxLr2Ra4nNsIHcnTfSRsugk0NK2SO7LEU4NS65dCyUAEyQ0idnG-E0CxNOLSn2gEDQ89SPL_YvXTxxk0tq3n44hntLJZH_4AzJrbKz6PMS1NVCy8HwmVo4ZzcykLKiA_pG24OioMLyBKqTd2osJ95k9LKDPnc-ELtZSC3juO_dBpjk1XkZ8D1xU1TRpvER23_pyddBNLvwAuXihXw__CVFUUtLnN0LQaVqMSqry_BItZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس کونز، سناتور آمریکایی: ایران همچنان تعداد زیادی پهپاد مرگبار در اختیار دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/akhbarefori/652640" target="_blank">📅 14:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652639">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
امارات اعلام کرد: آتش‌سوزی ناشی از حمله پهپادی به یک ژنراتور برق در نزدیکی تاسیسات هسته‌ای براکه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/akhbarefori/652639" target="_blank">📅 13:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652638">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
وقوع چند انفجار در ابوظبی
🔹
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/akhbarefori/652638" target="_blank">📅 13:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652636">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8891bbc2f6.mp4?token=XwMYwS-k4C5DE5CcR4I6rGQteY3FesW93OaIdJ-nRVdlDkp0WTGdg4GeF1-9KS2irndXNW4uBW9E-_weCqIEps7a9KC0Da_JPUGakWiu8vrhwcI6JYVLg45ae7x9jWK6gUONFxQKlE2FmWEH2PB__jVIO1nb34NrIvJhG2_wLZgKZBJVkOJWO6JoVC4BPUfI320L4F-mkeqawfPpLuiu8uUcQLsP7AZzUgii0XjeIqMAgDTxwEzkE_ZMK7dVnnZOWdb1CCRAjQSoJ00qjmmTy5rR_abLTHG3yVwkNZymM7Gh94CUqZXrFtLd9zjo82ebGWdI5mghfm9rXMcgobw3djzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8891bbc2f6.mp4?token=XwMYwS-k4C5DE5CcR4I6rGQteY3FesW93OaIdJ-nRVdlDkp0WTGdg4GeF1-9KS2irndXNW4uBW9E-_weCqIEps7a9KC0Da_JPUGakWiu8vrhwcI6JYVLg45ae7x9jWK6gUONFxQKlE2FmWEH2PB__jVIO1nb34NrIvJhG2_wLZgKZBJVkOJWO6JoVC4BPUfI320L4F-mkeqawfPpLuiu8uUcQLsP7AZzUgii0XjeIqMAgDTxwEzkE_ZMK7dVnnZOWdb1CCRAjQSoJ00qjmmTy5rR_abLTHG3yVwkNZymM7Gh94CUqZXrFtLd9zjo82ebGWdI5mghfm9rXMcgobw3djzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاجی بابایی، نائب رئیس مجلس: اگر دشمن به نفت ما حمله کند کاری می‌کنیم دیگر هیچ کشور دنیا به نفت این منطقه دسترسی نداشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/652636" target="_blank">📅 13:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652635">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
تغییر ساعت رسمی متناسب با فصول
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/akhbarefori/652635" target="_blank">📅 13:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652634">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMMEq9iAen0K7Vxin429kl8tVDvrna5LJ5e0Xotp_Gix_WBEJrWljknHmCS85mq0WyQ9VVkQuOPh1FUn62dmse4h9QtgvNLkLWJp9geDRp7LiITk67puVxcnGjBSHoIGKNCZ-H1y8gncpDuUsFF2RDVrSmjpzxXfR45hh9VNBoPsu6AyoWKCFJO7i-o7NPt352xpEpOiaF_je-LDKLGPxk374RRfZHDnFHCoGPFj6h9N0n85P80ibpOZnW-IJG1VGxkRex2rHX_YElkk0G5hdVyEyaoR6b9M5k7blD9_2I3Y0tNHU9h2HTyxSbi3SFe5f5nksOTeXODT3wyrU0AWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیاتی از جلسۀ غیرعلنی مجلس با موضوع کالابرگ
🔹
نادری، نماینده مجلس: جلسۀ غیرعلنی با حضور بیش از  ۲۰۰ نماینده به‌صورت مجازی برگزار شد.
🔹
محور جلسه کالابرگ و بیمه بود. آمارهای ارائه شده از سوی وزیر رفاه قانع‌کننده نبود.
🔹
وعده‌های مکرر میدری و دولت برای افزایش رقم کالابرگ هم محقق نشده که مورد انتقاد نمایندگان است.
🔹
وزیر رفاه، وزیر کم‌کاری است. تعدیل کارگران در وزراتخانه‌ها مورد انتقاد نمایندگان بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/652634" target="_blank">📅 13:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652633">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تخصیص ۳۹ همت اعتبار برای مقابله با تنش آبی در ۱۰ استان کشور
🔹
مدیرعامل شرکت آبفا با بیان اینکه هم اکنون ۱۰ استان کشور با تنش آبی مواجه هستند، بر ضرورت مشارکت شهروندان در مدیریت مصرف آب تاکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/akhbarefori/652633" target="_blank">📅 13:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652632">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7m5jikm5RSYZ-Gdl3OlSddk-bgWWuNloxvmKxpnJFa1z_ST0v-uJouAWfaEQ2WfW-yEBYPfOhjSXwF8PitQ9x7L2H5eW8udfNuDnmScx1fyuXeukCx921bY7-riQDuAOOwA8CdKS30Fpzx6j3NCwysKo07jkLmtopWzU7f8-SlwaVyqbwz2ezfiqmgaskg2RyJiNPDFQrtydVAelwIrkvajbRPCuKznTg_J_-tBSV4tkwOzs8WncM4ZhsfTa44l99RHupVu9rKVj03_ONVIoFDRXO_BB_3IUTDLhyjGLCNFYsn0fP7liejbdlzmnv8mzbhSsJR4aBCnPjH-Gb1vWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتبار مرحله نخست طرح «یسنا» برای خانوارهای دارای کودکان چندقلوی زیر دو سال واریز شد
🔹
معاون رفاه و امور اقتصادی وزارت تعاون، کار و رفاه اجتماعی: اعتبار یسنا برای خرید رایگان سبد غذایی و پوشک کودک در قالب کالابرگ الکترونیکی اختصاص یافته است
🔹
بیش از ۵۶ هزار کودک چندقلوی زیر دو سال در این مرحله مشمول دریافت حمایت شده‌اند
🔹
خانوارهای دارای فرزند دو قلو و بیشتر می‌توانند تا سقف ۱۵ میلیون ریال از این اعتبار استفاده کنند
🔹
سبد حمایتی شامل اقلام غذایی مورد تأیید وزارت بهداشت و پوشک رایگان است
🔹
خرید اقلام از طریق فروشگاه‌های طرف قرارداد طرح کالابرگ الکترونیکی در سراسر کشور انجام می‌شود
🔹
مهلت استفاده از اعتبار این طرح تا پایان خردادماه سال جاری اعلام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/652632" target="_blank">📅 13:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652631">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa048e618.mp4?token=Q0ASw0rmY7dE35B_wh4l6B_Wr36QDBvJeP0c3AJWq8vq5DByRFbp1tJHA2bfC58QXXXwxRW50eGfIScL_sQEMXNK34hkmtDz7N30hf49JeTQrRcd8vgFk8_lbq_zwWnpa-ZW1gLEbjWugqhFX2CtRw1G21SXkMwR-Gb5iPjmdWTLL9vHRQqpkmDcZqoFJ77eM6JOuDe-MDBvEBmP8XHZs3K1s_XlHv6f3t7R3lYtbAwu-UL0-P6LM9a_GmHKNfopLdxqcQCbIT96NfljRsNUosLzfq4JQNzRL0uYIo-rAJ6dqjqm3rDaj6qXE_TRILm6zY7ZwM9PfPN1EpOGnqd5-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa048e618.mp4?token=Q0ASw0rmY7dE35B_wh4l6B_Wr36QDBvJeP0c3AJWq8vq5DByRFbp1tJHA2bfC58QXXXwxRW50eGfIScL_sQEMXNK34hkmtDz7N30hf49JeTQrRcd8vgFk8_lbq_zwWnpa-ZW1gLEbjWugqhFX2CtRw1G21SXkMwR-Gb5iPjmdWTLL9vHRQqpkmDcZqoFJ77eM6JOuDe-MDBvEBmP8XHZs3K1s_XlHv6f3t7R3lYtbAwu-UL0-P6LM9a_GmHKNfopLdxqcQCbIT96NfljRsNUosLzfq4JQNzRL0uYIo-rAJ6dqjqm3rDaj6qXE_TRILm6zY7ZwM9PfPN1EpOGnqd5-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاجی بابایی، نائب رئیس مجلس: تنگه هرمز برای ما از بمب اتم هم مهم‌تر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/akhbarefori/652631" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652630">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5hffVB532H3DBfuodztkiFDJhT5wzV4L_dsTVoxTX9hFQwFVmA1LIPrC_PVn-mZ1YMy-VygnOW73Qaw0874kOvnC8DIhSBrLgf_uvOqtWOgT4PsMC2fBL32Ql9XqBIvkC4QlPj-J12KpBTsGXhaOJ3Utp6-gjZf0K_j8-LlJGdG-AmgAnfbo43cDcFX3fMyzdCZGUOBn7xE1oczIP5PoXyoEblfn-RBmMOhSIzJkrKuPnuH0-RJmc6wFta-2S5pXhXBUPMEAmkh-Z_lDOQbgiaOFOnKmHAAlqm3IUPQBdzaTGuIU_56frBgMEziZy35x3HW1c0XTlYb-AupsOMhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیوان لاهه برای ۵ مقام اسرائیلی دیگر حکم بازداشت صادر کرد
🔹
روزنامه اسرائیلی هاآرتص امروز گزارش داد که دیوان کیفری بین‌المللی (ICC) حکم بازداشت مخفیانه‌ علیه پنج مقام اسرائیلی شامل سه سیاستمدار و دو پرسنل نظامی، صادر کرده است.
🔹
هنوز دادگاه لاهه به این گزارش واکنشی نشان نداده و در صورت تأیید، تعداد مقام‌های اسرائیلی که از سوی دیوان کیفری بین‌المللی با دستگیری مواجه هستند، به هفت نفر می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/akhbarefori/652630" target="_blank">📅 13:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652628">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa941b0615.mp4?token=ZGz8y6uker8jT9wRYkeBeuqkzkgQPVU0513B_y5hev4t0utZCvC4BAkVN0-6R-oOyvDbQc5HBC4YcEjJxSMEq6MruN5JMuB2nPz-EYHj7DKL8ADqu5evaw5qiYhux7-DmJask3p0ejJVJiygZVA9X86IC1mZQcSlL9Y6b3gIRyJsdy9-A0rMPX5-P_1Ove7KyZBerbybY3F6lNc7PiyDdOk48LJr4HdsObTKUXaOUqRsLyEO9biLuO7BeCo0t6TCSykhhi3Hg6Dxpcy2ShASGmCgi-CJvcyVXhY89ZUV6dKCGV6sLeaYQZ5JwXKHyXq5Ne8vF9D3jp4Vi6BHQF5j7qX6GDmsQ41C7BdxhxyNg3HzHXYqcbTSWD-tXarLIscTFf-6b7UzN7DgNGC4D9g-W9qm0YOPQS-s7tfmzWrorEm8JBEZvA8bzeV4mzdLUoPDUzhvJCoUGbBv5C_ztEzTecoJwcfGulhh9vyk7Rlg0ajP-6mO4cCBgvvAvlMer-hmliSIzXWggOdsXlyMSimMq_QtBb7ZMoku24MaXhAf1XSJzysaS8MQXw-9s3tUV5WB0jIhAWvGcAKmTCP5uBkwsb1iNWyeFCHMrPvSIA6-0GHoBaDx4mr4SSzmgiPTNMRZ8cCnJBwn6xiROiXDVR5AVYKk-Q_tARzDgSCVlcYmtnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa941b0615.mp4?token=ZGz8y6uker8jT9wRYkeBeuqkzkgQPVU0513B_y5hev4t0utZCvC4BAkVN0-6R-oOyvDbQc5HBC4YcEjJxSMEq6MruN5JMuB2nPz-EYHj7DKL8ADqu5evaw5qiYhux7-DmJask3p0ejJVJiygZVA9X86IC1mZQcSlL9Y6b3gIRyJsdy9-A0rMPX5-P_1Ove7KyZBerbybY3F6lNc7PiyDdOk48LJr4HdsObTKUXaOUqRsLyEO9biLuO7BeCo0t6TCSykhhi3Hg6Dxpcy2ShASGmCgi-CJvcyVXhY89ZUV6dKCGV6sLeaYQZ5JwXKHyXq5Ne8vF9D3jp4Vi6BHQF5j7qX6GDmsQ41C7BdxhxyNg3HzHXYqcbTSWD-tXarLIscTFf-6b7UzN7DgNGC4D9g-W9qm0YOPQS-s7tfmzWrorEm8JBEZvA8bzeV4mzdLUoPDUzhvJCoUGbBv5C_ztEzTecoJwcfGulhh9vyk7Rlg0ajP-6mO4cCBgvvAvlMer-hmliSIzXWggOdsXlyMSimMq_QtBb7ZMoku24MaXhAf1XSJzysaS8MQXw-9s3tUV5WB0jIhAWvGcAKmTCP5uBkwsb1iNWyeFCHMrPvSIA6-0GHoBaDx4mr4SSzmgiPTNMRZ8cCnJBwn6xiROiXDVR5AVYKk-Q_tARzDgSCVlcYmtnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی بابایی، نائب رئیس مجلس: اگر به تاسیسات نفتی ایران حمله شود به تمام تاسیسات نفتی کشورهای دوست و دشمن در منطقه حمله می کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/652628" target="_blank">📅 12:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652627">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610d8b6046.mp4?token=YwRh83OoRBhuit0tzO5xPDa82AVJrUrabtFliGG3xwB3zdSIu5l2hL7gwrzeYiSyE0ukGFeQzVFSEl22efgY82RQ31mIawFcVHZwSbH2ni86uUwy_SZ7sQLngUhrtlYhgw-Rs8ylEkAJG7POZNBgohCjLBS14L6HrEwY0zGnhalPGwNGlmgQFSVRMqQB7yVlW-qxsiNi6mFlKeINh-zT-te_Y0p2d548VSFL1xEKL3gI29AaZio_jFp1TpwFhbA0v2rod9Udb27pbNByeybc9GWPUgwMiN7lAhqgINGr2Y3vwBwztMD28Yim6NFJfrP0KBbMytNVhIh0CvbnVthoozYbt1tDUeLTHboHPSqQFlTAK4X8Vbg3U7DVhTKsLPaXy5tUusbiHlzQRk2rspgZhW-Wtew1zyU79fOeUTN6bnDSUb-oc1lpfrIzz-CRMhKcSOUiwxf4O6nwoWKzo261RdWqFHVCLh9wmyzoCkEf9RPviAJlCJKis9yM3EszulsQxnbphk1DDWr50PQOQoYHtV4cH7qT53jCBz-Tkv6Tf2JtWbga7UKgbpEnCK6g0FGhi8t5bd2kAl7t82bHrKuTTps-CgH2cR9obsvCfQzcp6BRnJYmOn2Y-m55xKcb5Epll_KEk5sfJAgFjlB13bwg5HYpRf3FUdKefnvSiVvPtKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610d8b6046.mp4?token=YwRh83OoRBhuit0tzO5xPDa82AVJrUrabtFliGG3xwB3zdSIu5l2hL7gwrzeYiSyE0ukGFeQzVFSEl22efgY82RQ31mIawFcVHZwSbH2ni86uUwy_SZ7sQLngUhrtlYhgw-Rs8ylEkAJG7POZNBgohCjLBS14L6HrEwY0zGnhalPGwNGlmgQFSVRMqQB7yVlW-qxsiNi6mFlKeINh-zT-te_Y0p2d548VSFL1xEKL3gI29AaZio_jFp1TpwFhbA0v2rod9Udb27pbNByeybc9GWPUgwMiN7lAhqgINGr2Y3vwBwztMD28Yim6NFJfrP0KBbMytNVhIh0CvbnVthoozYbt1tDUeLTHboHPSqQFlTAK4X8Vbg3U7DVhTKsLPaXy5tUusbiHlzQRk2rspgZhW-Wtew1zyU79fOeUTN6bnDSUb-oc1lpfrIzz-CRMhKcSOUiwxf4O6nwoWKzo261RdWqFHVCLh9wmyzoCkEf9RPviAJlCJKis9yM3EszulsQxnbphk1DDWr50PQOQoYHtV4cH7qT53jCBz-Tkv6Tf2JtWbga7UKgbpEnCK6g0FGhi8t5bd2kAl7t82bHrKuTTps-CgH2cR9obsvCfQzcp6BRnJYmOn2Y-m55xKcb5Epll_KEk5sfJAgFjlB13bwg5HYpRf3FUdKefnvSiVvPtKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس مورفی، سناتور آمریکایی: تنگه هرمز قبل از شروع جنگ باز بود، حالا داریم سعی می‌کنیم مشکلی را حل کنیم که خودمون به وجود آوردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/akhbarefori/652627" target="_blank">📅 12:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652626">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b36779bca6.mp4?token=mqGWQGzUMh15_BZqpO5VP81_HTg9AuQdoQyZ9xoC7_t8edPmjIgfeeoadwbVuHZLWz7e386qY9H9MW1t35pDwudkmn5r_BlLp_aTF-UltK9FItovc05qyXTj7UPoMVb6sXq_FHFki46ZKSQlaZX1HLho5MOxi1w4J2kFe45VB5ed3sio525tq0Bo7QH8rYbj571AesRYgIBOTNkL8z6-1-bHuR1juCzU2inyVBbnlW-OmlPs7_VVae2xJoYCOt8YKzXQKSQzaKLxwjCc6k7ApqPGbg2FMSAKx_cz6mmFIpz6vHgMyKQoeNHBBTuqh7GS1Dhw2RJ-Mgu9z4ud5t7ZZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b36779bca6.mp4?token=mqGWQGzUMh15_BZqpO5VP81_HTg9AuQdoQyZ9xoC7_t8edPmjIgfeeoadwbVuHZLWz7e386qY9H9MW1t35pDwudkmn5r_BlLp_aTF-UltK9FItovc05qyXTj7UPoMVb6sXq_FHFki46ZKSQlaZX1HLho5MOxi1w4J2kFe45VB5ed3sio525tq0Bo7QH8rYbj571AesRYgIBOTNkL8z6-1-bHuR1juCzU2inyVBbnlW-OmlPs7_VVae2xJoYCOt8YKzXQKSQzaKLxwjCc6k7ApqPGbg2FMSAKx_cz6mmFIpz6vHgMyKQoeNHBBTuqh7GS1Dhw2RJ-Mgu9z4ud5t7ZZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی بابایی، نائب رئیس مجلس: اگر دشمن به نفت ما حمله کند کاری می‌کنیم دیگر هیچ کشور دنیا به نفت این منطقه دسترسی نداشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/akhbarefori/652626" target="_blank">📅 12:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652625">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وداع جانسوز همسر شهید مهدی سعادتی با فرزند شهیدش محمدحسین سعادتی
🔹
شهید سرهنگ دوم مهدی سعادتی، شهید محمدحسین سعادتی، شهیده زهرا قاسمی، شهیده آذر لطفی و شهیده مهیار محمدی در حمله هوایی دشمنان آمریکایی صهیونیستی به منطقه مسکونی در محله محسن‌آباد خمین به درجه رفیع شهادت رسیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/akhbarefori/652625" target="_blank">📅 12:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652624">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
تجاوز رژیم صهیونیستی به خاک سوریه
🔹
منابع محلی سوریه خبر دادند که یک گشتی رژیم اشغالگر صهیونیستی وارد جاده «الاصبح مزرعه الفتیان» در استان قنیطره شد.
🔹
منابع مذکور افزودند که اشغاگران مانع دسترسی دامداران محلی به زمین‌های خود شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/akhbarefori/652624" target="_blank">📅 12:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652623">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q68HOBa4iHHouSaBfKtp4l2YLFMy0xKAqztGVIGCtRTzy96HXb_lx7FDipWBPQix6c3q2NnOzkqwb8DIIfHLFJnjwkDnOFrXOpopzqVU05XSUzhgP4SDglc33T1ME8iYYStqNIcMbpNksxyfdHnbul6XLmHScl3EzJwNbR65SfW9F9IDUOO2_x7mxRcmBDgN1yKgmCdrdqa1bci73DkNqgrz5y3yoHQ57hAkqp6_U4Pq7IiJXNrairMuej4KUuv6M6J37zQ07xXhqZnQHZllsPkAMaYINKSzAEZyIJiDY5nky4SnqKgJsmp9eUlRCAQOLvHmdiyzlrejbqf6kjoTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: سرنوشت ملت فلسطین به دست فلسطینیان رقم خواهد خورد
🔹
رئیس مجلس در پی شهادت فرمانده گردان عزالدین قسام: در زمانی که با وعده‌های دروغین، آتش‌بس در غزه حاکم بود، «عزالدین الحداد»  فرمانده گردان عزالدین قسام با همسر و دخترش به شهادت رسید.
🔹
وعده الهی غیرقابل تغییر است.
🔹
با ادامه خط مقاومت سرنوشت ملت و سرزمین فلسطین به دست فلسطینیان رقم خواهد خورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/akhbarefori/652623" target="_blank">📅 12:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652622">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تکرار حماقت آمریکایی‌ها، پیامدی جز دریافت ضربات کوبنده‌تر درپی ندارد
🔹
«سردار شکارچی»سخنگوی ارشد نیروهای مسلح: تکرار هرگونه حماقت برای جبران بی‌آبرویی آمریکا در جنگ تحمیلی سوم علیه ایران، پیامدی جز دریافت ضربات کوبنده‌تر و شدیدتر برای آن کشور به‌دنبال نخواهد داشت.
🔹
رئیس‌جمهور مستأصل آمریکا باید بداند در صورت عملی شدن تهدیدها و تجاوز مجدد به ایران اسلامی، دارایی‌ها و ارتش مضمحل آن کشور با سناریوهای جدید، هجومی، غافلگیرکننده و طوفانی روبه‌رو خواهند شد و در باتلاق خودساخته‌ای که نتیجه سیاست‌های ماجراجویانه همان رئیس‌جمهور است، فرو خواهند رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/652622" target="_blank">📅 12:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652621">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5z1Q8FRTw8eQhqyTDxmdDCYc3TzkPYZ-KujqVs02XkUxnZDEtwKkN-bQBSRtn2EFsf4j4xaJuxDiPpt8sd4NyQ6d-fY0Yjh_1_tBKE9sXDh9a2oBsfVoscNivvx32_t2BLtOLxzTu38cDrCq49WOxRcTMB1vci69fNSGXn8dV_OFkx69cSh6XDVRpS33CopV8bKJ5jucr42DGvUOFXGl116rVqjzcTI8X0K5v3evfRjahw_LQJah8up3IgC9CDAM49D5Vs96MRIjS9l_xW1II7aidcLuigHUcPra9FtynJON7vUWlkSZG1lLL8pz63dSTFWtym1uYKv6dZBruH7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارشگر ویژه سازمان ملل نسبت به شکنجه گسترده فلسطینیان هشدار داد
🔹
فرانچسکا آلبانزه هشدار داد رژیم اسرائیل از شکنجه علیه بازداشت‌شدگان فلسطینی در زندان‌ها استفاده می‌کند و در سطحی وسیع‌تر کل جمعیت فلسطینی در سرزمین‌های اشغالی را از طریق محاصره، جابه‌جایی اجباری و محدودیت کمک‌های انسانی تحت شکنجه قرار می‌دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/652621" target="_blank">📅 12:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652620">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3773eb66e6.mp4?token=oe00G3LAKlcAJbJejWeTwiupXVkAJVKqAVyYbkjkXtqTp5fIYxc1Acb-pEk8UMvqTm3Vi3MukLIcDCtPxfspuk-1yV7pO-9K7IduYYhN3rSLKE6fZ0XNNsL1UFCWsVha22psL7IXWVbGAuLXKLrHmMMTPoXI2fUFKhERobRP8HEmzMbxyunQYB99DgDZC6VWtFCcxGZCMkusCvdhI2bskdBQX9mTRdD-nytyFbcXBFYHdhg99fZ3F1T505mQ3zXWFPfI3hMVGSyyA3J-2jgFaEoHWMtOpNae6EUZJwSYC5KprNm17a74h6gF36k5axlfWrCAk_gnBwFXyq5H-3tLHo6ZyasvTmEtiq7bR-GuHI2hVeWRG6l7caRQ1cPij-53BrHZvj1GoYEAGy-8EvT8TiNzaoe9d-Ts0MsEWDPLrXeJ4VGlXf8JkMXHbW3JBA0psbpn0Slxo3KzFiVJEdzOzkhasZQHD7rlTGG0AzoYiMjnUra-Vrt98_Om1x5Fb3nCkfxD7cbv90etve956qgvCeLRROINTZBKGteXMVcpMIbH-okghgBYRZc4WyKL85dP_fSpOnyl90o9gpjHlbRNVGFYIjucGXluvOjJWLhRZ-HSJlmP75YViBd7onTZ96dfb88B7xtEcm5XS6htjdbTJ_OURlfefXxksK2zhmxniLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3773eb66e6.mp4?token=oe00G3LAKlcAJbJejWeTwiupXVkAJVKqAVyYbkjkXtqTp5fIYxc1Acb-pEk8UMvqTm3Vi3MukLIcDCtPxfspuk-1yV7pO-9K7IduYYhN3rSLKE6fZ0XNNsL1UFCWsVha22psL7IXWVbGAuLXKLrHmMMTPoXI2fUFKhERobRP8HEmzMbxyunQYB99DgDZC6VWtFCcxGZCMkusCvdhI2bskdBQX9mTRdD-nytyFbcXBFYHdhg99fZ3F1T505mQ3zXWFPfI3hMVGSyyA3J-2jgFaEoHWMtOpNae6EUZJwSYC5KprNm17a74h6gF36k5axlfWrCAk_gnBwFXyq5H-3tLHo6ZyasvTmEtiq7bR-GuHI2hVeWRG6l7caRQ1cPij-53BrHZvj1GoYEAGy-8EvT8TiNzaoe9d-Ts0MsEWDPLrXeJ4VGlXf8JkMXHbW3JBA0psbpn0Slxo3KzFiVJEdzOzkhasZQHD7rlTGG0AzoYiMjnUra-Vrt98_Om1x5Fb3nCkfxD7cbv90etve956qgvCeLRROINTZBKGteXMVcpMIbH-okghgBYRZc4WyKL85dP_fSpOnyl90o9gpjHlbRNVGFYIjucGXluvOjJWLhRZ-HSJlmP75YViBd7onTZ96dfb88B7xtEcm5XS6htjdbTJ_OURlfefXxksK2zhmxniLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو فرزندت را در آغوش می گیری در حالی که فرزندان ایران را به آغوش مرگ کشاندی
🔹
کرولاین لیویت سخنگوی کاخ سفید در حالی از به دنیا آمدن فرزندش خبر داد که آمریکا ۱۶۸ کودک را در مدرسه میناب به شهادت رساند و او این اقدام را توجیه کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/akhbarefori/652620" target="_blank">📅 12:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652619">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbvRDp9ZO_8dKVUMePeqKvwMzEfP05mkiPw7pa--BHI7FCsvLjXJnUUCa813no4W1gAXFD96T5CPvCYmQ0FfmCAZupzNCCZD5sfPx7esnSgk_zPz-MCuBoLax_4hNGU3GIeNHXMeFId7G7TUVQXluZwb47HoqjZ-WKulIwVsvVsAZ4_LcoKFxhvWMJFOaOHs1ZlevyTgA1OX6tqVQT80krgJ_iZWuOUmRvfAz6FWRDm8S8m90mork0-zrGl8CRrlIsLq2hsfAhU9cpritlfQ-EmMMjCSoGx4p2HYsf8iTKwX3-HxjBUiP3PpJnP1AEifoe5BzNEfZ9R24-I-NPqkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به نصف سال نرسیده؛ بودجه ارتش اسرائیل ته کشید
🔹
وضعیت نیروی انسانی و بودجه نظامی ارتش اسرائیل روز به روز در حال وخیم‌تر شدن است؛ ولی با وجود این، مسئولان صهیونیستی بر طبل ادامه جنگ می‌کوبند.
🔹
روزنامه صهیونیستی «اسرائیل هیوم» امروز با انتشار گزارشی، از وضعیت وخیم اقتصادی و نیروی انسانی ارتش رژیم به شدت انتقاد کرد.
🔹
این روزنامه می‌گوید که «هنوز به نیمه سال ۲۰۲۶ نرسیده‌ایم، اما بودجه ارتش اسرائیل (۱۱۱ میلیارد شِکِل) به پایان رسیده است».
🔹
بنا بر این گزارش، ته کشیدن بودجه یعنی اینکه ده‌ها تانک آسیب دیده ارتش اسرائیل، تعمیر نخواهند شد و به آموزش‌ها و توانمندی‌های عملیاتی و ساخت مواضع آسیب وارد خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/652619" target="_blank">📅 11:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پاسخ ارتش پاکستان به هند: تهدید همسایه هسته‌ای دیوانگی است
🔹
روابط عمومی ارتش پاکستان: تهدید یک همسایه هسته‌ای مستقل با حذف از جغرافیا، یک اقدام استراتژیک یا ریسک‌پذیر نیست، بلکه از بین رفتن محض ظرفیت‌های شناختی، دیوانگی و جنگ‌طلبی با وجود دانستن این واقعیت است که چنین حذف جغرافیایی قطعاً متقابل و جامع خواهد بود.
🔹
فرمانده ارتش هند بیانیه‌ای تحریک‌آمیز مبنی بر اینکه پاکستان باید تصمیم بگیرد که آیا می‌خواهد بخشی از جغرافیا و تاریخ باشد یا خیر صادر کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/652618" target="_blank">📅 11:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652617">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZF7eXJ3Cwp7On1aNAHb73x501Jrcv97f3gWGQdIHFXUjTrwALHhJ6aOzrqraMImN6e49vfEwnRELUOJhgAwzlDinLoZRsEz4LpETQe7bCxtK1vuaMcMFL_IPt9WUCx2s8ooQkhMvIDJtc3TXm_5pNU8LKLuULKNkEIeNs4GOb65lkCwexOecCTE2Whn-RF_-vocSl9yzn6zV__nAbNZNjIFcK1LCdjcfHEoaeIYrvAKX3NTG7vO_PJpCU6s0JFaKUa8ojk6reHnVFTQnoKyLI4xdfv7kHQuOHNfGiSnrnEtvsBa1BIZ3d8zaFdMo8YvttzRgrK4qGXLinc6l-0J6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حاجی‌بابایی: مجلس موافق افزایش اعتبار کالابرگ الکترونیکی است
🔹
نایب رئیس مجلس: مجلس حتما با پیشنهاد افزایش اعتبار کالابرگ الکترونیکی موافق است و از دولت در اجرای سیاست‌های حمایتی، تقویت و پشتیبانی خواهد کرد.
🔹
دولت باید از هر ظرفیتی برای افزایش رضایت عمومی مردم استفاده کند و در این راستا از تمامی ابزارهایش همچون تقویت کالابرگ، تشدید نظارت‌ها و کنترل بازار استفاده کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/akhbarefori/652617" target="_blank">📅 11:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652616">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664ae9f9bd.mp4?token=plgOaCYUPyR7XUvblFhRNOtB72AMekmiy4UPVM_oIU8eX5OJUMxVL0jwXQpdKkO6nTBMW1ioiBeSZZN4wLnojkyCyrAzDhH2iDFn2p_SwEEEjR1KLpgaxXaWRUkaGzOGNg7jbArAhClq0eMwCdpt76_ptIbbjTtBKnmefjNQHf8bFP6gJDTeEaxRH6d7kel2TjlBvE6U9oVhQbf-Y__pT1ZSu3tDlLHl9rDTyrZNnprTbkJHQ1tZcvKkUeVrSMgMj-mNFwp8pM3uLXkqtbI1TyyvlXX7-yojpTUbzSoNnSiJ251g-MvzFIZmmIWEXtRQZMOYTIhSrwSpcQduK3kdxgIwPk_K1mt563ElYsD6QzxbYE-VWYceLbBDhDavdSAcrUjMjKPyKJ1Ax5qBEMbJzpL2RVPBE-_9oSsNA4-wxt5t7rYBylXYGG3zMq7u4zSn4SRLNbZFxOtlQDyu8xm2JNSqIgGj4iVAPanj5gPezZshbV3OII6WQFqsBWgUn3oHOeUFDBrtykS4eaIvc79iA-XvyPCPKvmxAedy-J2SIyRj6sPjFrQ_d4SqcOk9yrjSF7UAzW2UnxYe-_zazJKK56b33FiBHgX8zUzGHoWPeza3NGupVpoMIYakBgWze78Ewbb8L2kMYtr8MSy7bZ5Wgw8dUtbZQShzvcWtmlHCi40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664ae9f9bd.mp4?token=plgOaCYUPyR7XUvblFhRNOtB72AMekmiy4UPVM_oIU8eX5OJUMxVL0jwXQpdKkO6nTBMW1ioiBeSZZN4wLnojkyCyrAzDhH2iDFn2p_SwEEEjR1KLpgaxXaWRUkaGzOGNg7jbArAhClq0eMwCdpt76_ptIbbjTtBKnmefjNQHf8bFP6gJDTeEaxRH6d7kel2TjlBvE6U9oVhQbf-Y__pT1ZSu3tDlLHl9rDTyrZNnprTbkJHQ1tZcvKkUeVrSMgMj-mNFwp8pM3uLXkqtbI1TyyvlXX7-yojpTUbzSoNnSiJ251g-MvzFIZmmIWEXtRQZMOYTIhSrwSpcQduK3kdxgIwPk_K1mt563ElYsD6QzxbYE-VWYceLbBDhDavdSAcrUjMjKPyKJ1Ax5qBEMbJzpL2RVPBE-_9oSsNA4-wxt5t7rYBylXYGG3zMq7u4zSn4SRLNbZFxOtlQDyu8xm2JNSqIgGj4iVAPanj5gPezZshbV3OII6WQFqsBWgUn3oHOeUFDBrtykS4eaIvc79iA-XvyPCPKvmxAedy-J2SIyRj6sPjFrQ_d4SqcOk9yrjSF7UAzW2UnxYe-_zazJKK56b33FiBHgX8zUzGHoWPeza3NGupVpoMIYakBgWze78Ewbb8L2kMYtr8MSy7bZ5Wgw8dUtbZQShzvcWtmlHCi40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: رهبر شهید بابت رد صلاحیت من اعتراض کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/akhbarefori/652616" target="_blank">📅 11:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9def2c56fb.mp4?token=StHawe__PWs6cjE1FOP2P_KIr3jDxCQC8kgDlkb4bsLT3iSe-ZmpOe2Os2iq_kdPn1Pcd31cSvt0-2xlIDnegKrKrBYS9kiCD-f4LRRBysEr22K8vqbpNEKZ4XsOC-Vcyh47LsvxwaNHUuXm7wQsw_P9NNSApRReskASJjcwpcm7wfgLvA_khWMzpGW4HGcc0ZWTviD4aNcP1X7RAub_w7DvQiu2f1ngQGHWAN6mxUcomqU_Tqr7xdPL8vmUoJZgo0eQZ6lZfXmidorNX0ezbtORrMgC8OW1lsv1TCuFJdIz1n6gFEe9SxqZserg9EmP-qP6DN-G14ETmQrdE0T3lIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9def2c56fb.mp4?token=StHawe__PWs6cjE1FOP2P_KIr3jDxCQC8kgDlkb4bsLT3iSe-ZmpOe2Os2iq_kdPn1Pcd31cSvt0-2xlIDnegKrKrBYS9kiCD-f4LRRBysEr22K8vqbpNEKZ4XsOC-Vcyh47LsvxwaNHUuXm7wQsw_P9NNSApRReskASJjcwpcm7wfgLvA_khWMzpGW4HGcc0ZWTviD4aNcP1X7RAub_w7DvQiu2f1ngQGHWAN6mxUcomqU_Tqr7xdPL8vmUoJZgo0eQZ6lZfXmidorNX0ezbtORrMgC8OW1lsv1TCuFJdIz1n6gFEe9SxqZserg9EmP-qP6DN-G14ETmQrdE0T3lIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماری از آسیب‌های دشمن آمریکایی صهیونی به میراث فرهنگی کشورمان
🔹
قائم مقام وزیر میراث فرهنگی: ۵۴ موزه در کشور طی حملات دشمن در جنگ اخیر آسیب دیده‌ است.
🔹
همچنین ۷ بافت تاریخی و ۵ اثر ثبت جهانی در ۱۸ استان خسارت دیده‌اند.
🔹
در تهران ۷۰ اثر، در اصفهان ۲۷ اثر، در کردستان ۱۳ اثر، در خوزستان ۱۲ اثر، کرمانشاه ۵ اثر، در لرستان ۴ اثر، در قم ۳ اثر و بوشهر ۲ اثر خسارت دیده‌اند.
🔹
بیش از ۱۷ مکاتبه با نهادهای بین‌المللی از جمله یونسکو، میراث‌جهانی و... انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/652615" target="_blank">📅 11:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652614">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN8nF9IMM5TOmsDTlyJ_MShJao1sK-JnSHfvcMXUgLw7uAEPlXLlQMcqydj_7q6ndQ5GOZ1eoSkwKM4_WGPaFXAcNGoVftRkBwUBHCkxviGi1oRMV2H6ER28-pcP6Bz773Qt_PdLnZCa1_tkVVFP_apPPWQf2GkRP-LoGzHfhCsf_fwHliRmND-gzvLGOehxpb-5EymWY1JggOJwEnmRkNPRq2TB6xfevxdEfmMUEbYwM4XfMTMYt2S589xxU1Wu-8sCwfuFsfB4lx4TEL2FYBgvdvJqlLUALhLbyBUtR5MGC4Ivqmj58LVLwOZFJnWj9wc6eXUCgFeehGWRCc5xBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادگستری قم: آپارتمان‌های مهدی نصیری و وابستگانش به‌دلیل خیانت به وطن توقیف شد
🔹
رئیس‌کل دادگستری استان قم: با گزارش اطلاعات سپاه و پیگیری دادسرای مرکز استان مشخص شد که «مهدی نصیری للردی فرزند گل‌محمد» دارای سوابق مالکیت ثبت‌شده غیرمنقول در حوزه ثبتی استان قم است که براساس مستندات، این اموال شامل ۳ واحد آپارتمان متعلق به او و وابستگانش بود که در راستای حفظ حقوق عامه با دستورات قضایی توقیف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/akhbarefori/652614" target="_blank">📅 10:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652613">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3FgLMC-Mnjbva7J38FFyQNILPXop87H5VYXI7yew_46OocUqZ_hanXU263s9cVpimo-9TTfM_5SeXBM1VyfZJVylVlPzvqlkZGMBlkehFYM-czRzQxC8Uo8U77pVZ3OiuGCsL2r0hL0H21G_zoagxidR_wkt-V_uGBstL1FsAhgzD_nymfx6uWrW7B1jgBHFRhO2NXvMMFf-yKA66AzMqjzSNZGRuoWdyzTojmwYfWCVOr-z301TKCMgCo94z154uNzTFohGiOmGuQlf7XWjt1sd_LOD_mWsqSvbhBszLTTVlKgkiaoJKtOUUo3AfGG89v1SY9sqSEokS6VSrAHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حق هسته‌ای ما به آمریکا ربطی ندارد؛ از حاکمیت بر تنگه هرمز نمی‌گذریم
🔹
علاءالدین بروجردی عضو کمیسیون امنیت ملی مجلس با بیان اینکه مذاکره بدون پذیرش شروط ایران بی‌معناست، گفت: جمهوری اسلامی ایران از حقوق خود در تنگه هرمز و همچنین مسائل هسته‌ای کوتاه نمی‌آید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/akhbarefori/652613" target="_blank">📅 10:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652612">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1745ced0.mp4?token=nD9vR_ZQyYA7f-l5SK8wfGAffQXWNNROs9iNRQ2kW6gD5dTtOCIv_NDpHPICBAHA5l6LpcTobxmS9rVJqLPdPEiCGeo4ocolRPi3wrVLR0B4GU0SnqhsT-xrvm70wcvMQnS9vd7TM5G7CLQ_TNs-l1s5jsxpqbsgyV64U5PxqKhJ-28VXM8oIM5KI_v3ZkbMHBQrQSWiksaAdpExSjp1tdSsG--4PmBq-k-QSkZ3zMoTpS3YqmgG2P0VxGqgZIO2pexhlMjOOFbOKxXtgCr3kk3Ihr4PfO-gCxFHFkx95yZFut332NMnFV7AGd-5zxaZhKqXjbUrYoV9rihofpsWfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1745ced0.mp4?token=nD9vR_ZQyYA7f-l5SK8wfGAffQXWNNROs9iNRQ2kW6gD5dTtOCIv_NDpHPICBAHA5l6LpcTobxmS9rVJqLPdPEiCGeo4ocolRPi3wrVLR0B4GU0SnqhsT-xrvm70wcvMQnS9vd7TM5G7CLQ_TNs-l1s5jsxpqbsgyV64U5PxqKhJ-28VXM8oIM5KI_v3ZkbMHBQrQSWiksaAdpExSjp1tdSsG--4PmBq-k-QSkZ3zMoTpS3YqmgG2P0VxGqgZIO2pexhlMjOOFbOKxXtgCr3kk3Ihr4PfO-gCxFHFkx95yZFut332NMnFV7AGd-5zxaZhKqXjbUrYoV9rihofpsWfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر مجدداً مورد تجاوز دشمن قرار بگیریم ضربه‌ پشیمان‌کننده‌ای به آن‌ها می‌زنیم
🔹
زینی‌وند، معاون سیاسی وزارت کشور: ما به‌دنبال جنگ نیستیم، اما همه ارکان کشور، مسئولین و استان‌ها آمادگی کامل دارند.
🔹
اگر مجدداً مورد تجاوز و تهدید دشمن قرار بگیریم، کار اداره کشور را توفنده‌تر از گذشته و با آمادگی بیشتر ادامه می‌دهیم و ضربه‌ پشیمان‌کننده‌ای نیز به آن‌ها می‌زنیم.
🔹
اکنون شاخص‌های امنیتی نسبت به اوضاع غیر از جنگ بهتر شده‌اند که دلیل آن همراهی، انسجام و حفاظت مردم از کشور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/652612" target="_blank">📅 10:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652611">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87d6e980d.mp4?token=Wp56IM0lufoKOnUw0RHq4xN8YvT-1WAyxkhk_dBtU8N7TuytrR0GrJpz1Bhr1JIDrOQFhu44bYijlfC3srGiEGgHw6lr6-LzUUBvrekAGZHFB8vaFNAwHwQPK-yK6IMa9SaNgWw9OOR--6L4TjJ3cMtXOJPo3uMDBmYmxnkSqreik5-om8lj3w9EzzxALVBNDvHLM2ZV9rIGKJ57uYAPl3wRyc5Tofbv3Pg47NI3i6wzOpjpV0vixjkFJ9AbYzJgZvSRAEJhGBwiwqdqus-qY83NkzIRxIVgvqpfWpGm_O2NA40DXpcdhD8j4C9Ocpd4NvERnkiiU7ZS05xOPn32ZyAziLwJg7AYwa1HNQsLCTQLP4LmSrbkDQJ1zLsbDCzr2WcyjMkP01Q_U9dU5g2aTlHDtKS4M5ll2ZK2-zeP3mZG9wiH0BGtQUtbiVMEZYjr0tc202CHlg8S_9Ay23c7kGZqp6-XzKqDbq0XW0_Jl0bMlot4DhxomjsKDrE8pkRr2_5xiZW-Xu7YngEZVRI7z9KTP9VvW2zAN7iZN_yZzMyFJaGywX8bRILPbk7z18SZkoF0G6w4VGz6MN1xGqlUmd62xQHY7eEH-6xQRYV-TRugiMtySZuQQcv_3eI8yQiV6_t-Sn0cgdUITIXeqfMtPL0Ic0aMMcfHtFrcSvC_LbE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87d6e980d.mp4?token=Wp56IM0lufoKOnUw0RHq4xN8YvT-1WAyxkhk_dBtU8N7TuytrR0GrJpz1Bhr1JIDrOQFhu44bYijlfC3srGiEGgHw6lr6-LzUUBvrekAGZHFB8vaFNAwHwQPK-yK6IMa9SaNgWw9OOR--6L4TjJ3cMtXOJPo3uMDBmYmxnkSqreik5-om8lj3w9EzzxALVBNDvHLM2ZV9rIGKJ57uYAPl3wRyc5Tofbv3Pg47NI3i6wzOpjpV0vixjkFJ9AbYzJgZvSRAEJhGBwiwqdqus-qY83NkzIRxIVgvqpfWpGm_O2NA40DXpcdhD8j4C9Ocpd4NvERnkiiU7ZS05xOPn32ZyAziLwJg7AYwa1HNQsLCTQLP4LmSrbkDQJ1zLsbDCzr2WcyjMkP01Q_U9dU5g2aTlHDtKS4M5ll2ZK2-zeP3mZG9wiH0BGtQUtbiVMEZYjr0tc202CHlg8S_9Ay23c7kGZqp6-XzKqDbq0XW0_Jl0bMlot4DhxomjsKDrE8pkRr2_5xiZW-Xu7YngEZVRI7z9KTP9VvW2zAN7iZN_yZzMyFJaGywX8bRILPbk7z18SZkoF0G6w4VGz6MN1xGqlUmd62xQHY7eEH-6xQRYV-TRugiMtySZuQQcv_3eI8yQiV6_t-Sn0cgdUITIXeqfMtPL0Ic0aMMcfHtFrcSvC_LbE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز پرداخت تسهیلات  ۵۰۰ میلیون تومانی مسکن روستایی تا ۱۰ روز آینده
🔹
جودی معاون بازسازی بنیاد مسکن: تسهیلات ۵۰۰ میلیون تومانی مسکن روستایی نهايت تا پایان هفته و یا ۱۰ روز آینده توسط بانک‌ها پرداخت شده و امسال متقاضیان دهک‌های یک تا ۴ در کلان‌شهر‌ها هم می توانند از این تسهیلات بهره‌مند شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/akhbarefori/652611" target="_blank">📅 10:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652610">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecJlwL8pC75Re_Jc_5K_ZHtggc7LDZG5XFR8V9G4otXI3azIfOh5TSAE3PLAKlvpwcNO2268B1L2ohiaaSYj5oU3uK4c6NrKGHpd5vtj3Ys_5HXXBNeUuQbbKq2yJkDx7m5XNYDaGBptRB1fCxMcIAftfpJXJ81b87CfanTCqiYvQXenB-fmztIAXTnF4KgKBM2sMTrrMo8BMc4YetdmBHqcUn5FACctSzQLxNoSI3GKHJwGmVMJhnsGKwldL08LKqdRW2E-iDmBjwqDbBuTbMNVICC4b-PaYgZotzlMhewsNTNepaW9mrCNlyPO80rnUN6p3oJ-Py6tn1iD5DvrIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاریو: ارتش اسرائیل در حال تجربه فروپاشی نیروی انسانی است
🔹
رسانه‌های عبری با استناد به گفته‌های رئیس ستاد ارتش رژیم صهیونیستی، گزارش دادند که ارتش این رژیم در مرحله فروپاشی در بخش نیروی انسانی قرار دارد و این در حالی است که افکار عمومی از عمق و گستردگی این مشکل بی‌خبر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/652610" target="_blank">📅 10:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652609">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6379e24.mp4?token=Nx1HJIvROGxyu8OnnIamCGiYp6yH5zp7Pnu-m4TiRUwDTdsQDqM4bbnKDQeWpeitzQJ2ooG9EFH6huBXzFT8f2VLEAfuLf3kMkpcsOiJETA0xbnfeSB9z28pvSucucxx0UpQlK6duDDK1P_9qLQ0sES49JdP8hKcBxLyDc4K_ILtooFZk1jJzgN_g69xCWF8Jb2KgneZfx52gM3RJ__Q44qPbu43RPWPC65bGesisMohI0h-cleQE-J-Lppbs_jOtqSmTj1XPXI9Qb1tr7ik4fUINCMXE0V3xyC11D1RR_B_Dpb7-4b9YHvlH-apmvpahzbdEXB0fzcnF8KZyQA_rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6379e24.mp4?token=Nx1HJIvROGxyu8OnnIamCGiYp6yH5zp7Pnu-m4TiRUwDTdsQDqM4bbnKDQeWpeitzQJ2ooG9EFH6huBXzFT8f2VLEAfuLf3kMkpcsOiJETA0xbnfeSB9z28pvSucucxx0UpQlK6duDDK1P_9qLQ0sES49JdP8hKcBxLyDc4K_ILtooFZk1jJzgN_g69xCWF8Jb2KgneZfx52gM3RJ__Q44qPbu43RPWPC65bGesisMohI0h-cleQE-J-Lppbs_jOtqSmTj1XPXI9Qb1tr7ik4fUINCMXE0V3xyC11D1RR_B_Dpb7-4b9YHvlH-apmvpahzbdEXB0fzcnF8KZyQA_rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس امام شهید و رهبر انقلاب در کشتی توقیف شدۀ دشمن!
🔹
تصاویری از داخل کشتی توقیف‌شده در آب‌های خلیج‌فارس، توسط دریاداران جمهوری اسلامی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/652609" target="_blank">📅 10:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652608">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
تکرار جنگ جدید علیه ایران پرهزینه است
🔹
احتمال بروز جنگ اسرائیل و آمریکا علیه ایران در زمانی نه چندان دور وجود دارد.
🔹
باقی ماندن شرایطی که وقوع دو جنگ قبلی را در پی داشت، احتمال شکل‌گیری جنگ جدید را توجیه می‌کند.
🔹
در عین حال عواملی که سبب شکست دشمنان مهاجم در دو جنگ قبلی شده همچنان پابرجاست.
🔹
همین موضوع تکرار جنگ را برای دشمنان پرهزینه و دشوار می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/652608" target="_blank">📅 09:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652607">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB55e8kkqq7L_XFi5fA52SgEx2PBcspZw9Hq5yNDANfVvpQgyu30Jmq_9VlAzF2IsJhdk9LM4MsAtyT2QKiG3-0g-LHq87HUCimIsGzyrTu-1xdH-R8pAGnGL60t8JCjEBl2tYyMYtFTJKBRcSCDRL1RV8tUiWPwn2mnmXYIoO0P-YuGbmojRpjfo_ggN1F59HaoU6C3T8NBnv5TKJ7totgAd4HdJ4-0OwzllJyj8YW5sHtBxpeo1czd8Iku1m91mq6NIJsnoLSAzgDYUHnsuqescgyZzfzMK5nJpfalQy-mtG56Hi6mLviqlPkFLnn_bmLU2n4LZhCdIJCtdUgerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهر بررسی کرد؛‌
🔹
جنگ معادلات در لبنان؛ از راهبرد «زمین سوخته» تا نبرد فرسایشی حزب‌الله
🔹
جنوب لبنان عرصه درگیری های سنتی نیست که نتایج جنگ با مقایسه خسارت‌ها و تلفات سنجیده شود، بلکه به میدانی فراگیر برای جنگ فرسایشی هوشمند منطقه ای تبدیل شده است که در آن آتش بارها همراه با پیام‌های سیاسی و تاکتیک جنگ روانی در هم می‌آمیزند.
🔹
همانطور که راهبرد نظامی رژیم صهیونیستی جبهه‌های نبرد در منطقه از ایران گرفته تا عراق و یمن و لبنان و فلسطین را مجزا از یکدیگر نمی‌داند، اجزای محور مقاومت نیز باید در تصمیم سازی‌های خود این نکته مهم را مد نظر قرار داده و راهبرد «وحدت جبهه‌ها» را مانند گذشته تقویت کنند.
🔹
رسانه‌های صهیونیستی اذعان کردند که تهران با وجود ادعای مکرر سران تل آویو مبنی بر اینکه ایران و لبنان «دو جبهه جداگانه» هستند، در برقراری راهبرد وحدت جبه ها موفق عمل کرده و این موضوع در مذاکرات اخیر نیز کاملا ملموس بود.
🔹
سرتیپ مجیب شمسان سخنگوی ارشد نظامی یمن در این رابطه تاکید کرد که «جنگ چهل روزه» در حال تثبیت یک معادله بازدارندگی جدید است که بر اساس درهم تنیدگی جبهه‌ها بنا شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/652607" target="_blank">📅 09:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652606">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0683cf1ee6.mp4?token=XFHTlWHm1aDK2kgsSMieOlv34CrzKwYr5EJVu0-6-tRjiloK-YoKY9aWxL5eEChf22AA33a-hihT6UlYkURcjpwyhNLXU-pJ2wb2dEcmaxgOcHkV-bkWixS_1p-O1uou79-IA18uHlxO5I34soIrC64KtryqBUHwCmHZupsNOgflreLqjGgFq3HFzf4j07q5sXruWPZwQj7XZYtzglgfhcU6x1bI0BlEJyZWgogHf83tn5GoW33s_pmBb0L5yIhB74EGU48A4UlxXNZqcexwBNWHpQ3Cu4-7KTMkDqhX8yX-etg4X2RXA0LvrCzn0rgyTQUfIJ4uNWUlYd_OW1Y0PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0683cf1ee6.mp4?token=XFHTlWHm1aDK2kgsSMieOlv34CrzKwYr5EJVu0-6-tRjiloK-YoKY9aWxL5eEChf22AA33a-hihT6UlYkURcjpwyhNLXU-pJ2wb2dEcmaxgOcHkV-bkWixS_1p-O1uou79-IA18uHlxO5I34soIrC64KtryqBUHwCmHZupsNOgflreLqjGgFq3HFzf4j07q5sXruWPZwQj7XZYtzglgfhcU6x1bI0BlEJyZWgogHf83tn5GoW33s_pmBb0L5yIhB74EGU48A4UlxXNZqcexwBNWHpQ3Cu4-7KTMkDqhX8yX-etg4X2RXA0LvrCzn0rgyTQUfIJ4uNWUlYd_OW1Y0PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون| کشتی‌هایی که پشت دروازه‌ «تنگه هرمز» ایستاده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/akhbarefori/652606" target="_blank">📅 09:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652605">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOtSXr0C6pgbkMU053Xi8wjDsbtNKDHu9Axdlmd9ab-4i163Jcd3MitdWu-DERtNzLYvbl9fOamfG_-BZipNUF0s1EoLUFIjXqAyyASdtszb8PGKOHspBv8UvZ-v_OsfGwdrLUNor8FjUWix9srAnYhFAIEewNsH_gd6kRkKcQYFAolbANjk17stUA-Op-u3PZxYouGMGrQlCQFctEAHuJ0ldw_KOhmGI2DaU3xvNH-Y-aRifB2BXCzqdeBT0SThdufiUoi-tTrJNuoXt1AfZ1ZZBkUgY3XcOOrFwbybg6jc2yoMMi71zFeN06JUv62pGwVSkSLNgaEj_sUIJ6DKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان مقام سازمان ملل به تجاوزات تل آویو علیه فلسطینی‌ها
🔹
خالد خیاری معاون دبیرکل سازمان ملل در امور خاورمیانه تاکید کرد، رژیم صهیونیستی بیش از ۴۰ هزار آواره فلسطینی را مجبور به ترک اردوگاه های شمال کرانه باختری کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/652605" target="_blank">📅 08:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652604">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0541e6886.mp4?token=j7nwdF_sqRkFghkqw8PFcS33iCoUDCfj3NUig7xo4obrMivrJH5sRE-jspqKiwTWpjftV5YG6JpqE1Gvb53n8p5yxxPzkUZQLj1Jiq-39XsYTiRBRlBIGdD3ugYU5VpeWazs5BM_5hvSpMK7wB_7SN1c6hGUSfYmd33LePcXcKBuZsLygqrSrhKPsuv4-swyT6holsckMBu_4TfmHvqSnZMW7FIcZwq5O09wdohDdBt0hceNITdJinXUaoNQawmsqkUe_OIvm2lpIaznRwXmgopYYUisrkGuWiD06SmtQjsoo5YJ6wXV92jOMOEXZAVjjl2rSyhBxNzg5aZrnkanRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0541e6886.mp4?token=j7nwdF_sqRkFghkqw8PFcS33iCoUDCfj3NUig7xo4obrMivrJH5sRE-jspqKiwTWpjftV5YG6JpqE1Gvb53n8p5yxxPzkUZQLj1Jiq-39XsYTiRBRlBIGdD3ugYU5VpeWazs5BM_5hvSpMK7wB_7SN1c6hGUSfYmd33LePcXcKBuZsLygqrSrhKPsuv4-swyT6holsckMBu_4TfmHvqSnZMW7FIcZwq5O09wdohDdBt0hceNITdJinXUaoNQawmsqkUe_OIvm2lpIaznRwXmgopYYUisrkGuWiD06SmtQjsoo5YJ6wXV92jOMOEXZAVjjl2rSyhBxNzg5aZrnkanRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردی که نامش با عدالت در تاریخ گره خورد
قسمت بیست‌ویکم پادکست کافئین منتشر شد
☕️
روایتی از زندگی خسرو اول ساسانی، انوشیروان عادل
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/cyoMCF_5vUc?si=evsHZ1zKo2U21n1d
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652604" target="_blank">📅 07:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652603">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین - قسمت بیست و یکم</div>
  <div class="tg-doc-extra">انوشیروان عادل</div>
</div>
<a href="https://t.me/akhbarefori/652603" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
انوشیروان عادل
🗓
این قسمت روایت یکی از مهم‌ترین چهره‌های تاریخ ایران است. پادشاهی که با اصلاحات بزرگ، قدرت ساسانیان را به اوج رساند و نامش در فرهنگ و ادبیات ایران به نماد عدالت بدل شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/652603" target="_blank">📅 07:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652602">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg2k0_HtgSDQzTED8tSV_3GGv1Gt-AqiSq1mWV7ZQSxphz--TlAlfYwtHQ9o3D3RuaA-8Ghypo2a5I4UzXuC1sl0Z2-RpXKzMWJAJs8lL4byCQUEaDCeuic-W3ffOeyllihbxHh5uUx60G_ox14JVh6Vc8qWpO57mA1fEkaHPQIizu3I9Sm-uZABQzixZxa7dzFZZamA43T4YHu1DS5NI7LRn8TlvcWwq2um5x3ioeXkLG5sQq4CdL-wjTQdZzhdfljLLRMCYCz4p2bRdmJoC0H0qIZoaFrAYA9iC_kcj2D3g7E9KYB8lexnKardOnoNoSac5gZIiZ-sTTz9WrohTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۷ اردیبهشت ماه
۲۹ ذی‌القعدة ۱۴۴۷
۱۷ می ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/akhbarefori/652602" target="_blank">📅 06:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDQGpSmFx9rLQ0pQ8-BCRdDkWdvaQgwKfxYE2J1Die8QJW0-yZY2kbQ9Uj4Fe04bzQGHRa2V3z_KMvcLAlpRnFcbkFsioP8tgrE8LOWi3Up3yeoYB97esbXUzADjsbBwFhL_e-jP288IoEM0HqScxxHiQ-Ky9lXvc6oUtvd8OhWts7NWBuxKBNqfSLfSWCsKK1uq74cYQHVBiKlsbL4K5tZkt2CFkMLyC43znTAJm49R9CGXQBcQp18lQNxcoIJAbBd-6Jwg-ei-PRWbMEH3m5mjJNfxN-69TSuvcxy_CQqtgowD1L5c0x9i5XDXH4f8PRA1NMH_vOB3Pn-HGBK2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrOH-o6i1XFrML0-5SfKQ0bwGmqliJiPhed403l31_rFTuR7GRQ14EzeQCcVxPb8q7vHnQnxagdak9_cs2xkkX2KISgifzzYwAYW0Vhfi5bhrK1Gbz3440fgoTAdjKjU5NljXDKRjxw_kDE40dM_tK2WtndDGD7VmFmozYiSzMaTL_kQhXxgHJqIk9W38IUoOQoneJopIkKIyWM1xtThthFiwuysWoSqV6fl47lzrIxjByrL8h3E2dy7jRIbDlho15zbel6A2hjCVBmVxPHBKL0oAMGxOw235ClpLMcgndB0oha2PuSQT10YbncH2vCa3lV9qZ1vkCyOT0SnYPu9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKuPeZTHi5bz8IwfTTMWYBtq46mbUe3VVE0UH0LGem8WlOPw9IM2WNEGDp5pxymI0w9xIpJ90bEJgDuLUi9Az3Ao-7wrDa8SS_6Dc4M9MMn_ixpqSjeHe3rKel44-vZD-Ic7udiBf0PxAKTfLegM2o51170O6zAyT6TTb_arqgTcA57DpLYzPr2yjUW7CVbCzQZLOmyM7-Dhm9CicqR9KWX8sQoshWAy7uuMKFJ-dKih0tOkx9-ZSEwBm3kK3QXtpcDvroUbeXYcRup3MNGDs8kq8KxaGK5Y-beG0gc1hh-xOjzGpuv7iYGLcrDG9GO7Drq5rOKUC2Utn410CXXv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeYcQZ4Qh6DF0tdfOdi71zRmbv8P0CeSRGNoSz1NWCuVbRHdkSC0Bsz7g6NIawBUhKSAYef_0L2i06H5_bAzSN7VauQ_BYn2xssgIKDVh2EVKPiRHJW-IiPQCtA4V5CwFNHA6fLks4evcuUxb-6sP5AvXxITUWH1gZkUl_fHDhF8c5mlvOq5pax1pqT_w2jAhPdUwTuSrPD5bDjvjwqWP6d1k6dFvL_fT7YLU0oSaOhfP4m4OwQG5kTWiT-cULG2_6KgCH2JgNfWHfKjSebL3e-cKVtsJf5iHB2lfPVc9zrY1jqd761hmDIEnrdekF3Pwd1ZhR9YM38e54BaucWLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUwVnrfnlh8_WzPNrCd66Wnd565IbrGifLaDN85aJMqfRtnWT5uzl21DXSXoIWjnCxUAnHCxK4Km2JxN-nrd8uWCCd4xWgOhE5lHwo-KPk_NAFFsYuAQrn-bOhmW8RQPwE7PoYX7UU8JwH0kXRN1LV3fWCdZT8NUvAbcrW2gdzW_uJBlB3cvql0OElKu1YgUs3a41oMc1j39nyPeftY_73BEDm9deazEVfiwYPHpn88JcGXwQ--Kv3asawJhfjUtVOp69guGqY3EkOFTS-8CTsi8jNQDKepH871GNa8f6CXK-weNISWhBY4RGcZoLuRoMJf-ISu5O4q3sY80HmZJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEx_mNgPboBoDQsUPTHLLcuFD_yfUjknmA3bn06pOvHdpsOWaOFIelS3CXrAVs2CqxSxed1wiTOGHUkS1Vnb2aeSJxmpnW6y_4i53V1D55KcSOw6bBGbEvAhggjl9-fooXBB0o-LyxWSPpix5YMdaj_IcdfKy0JbSoGt8NfYqbVOTSsDq05LbzySw_1OhiZ6PYuIrkpXgkusb8bFmk5WYK-yI4xcWizCgErneVn0jNvo2R3CvTCBJbh85mKDuiDgE8vQbTRXRkQcELqxEdqpjwBZbHm3RPtAjtPV2BhJFWFxIpYzVQNFIVf7ZjUMppOKqpDZwhPT9qQXHZzVHPxrag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تظاهرات ضد جنگ امروز هامبورگ آلمان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/652596" target="_blank">📅 06:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa48d6eb3.mp4?token=tz3qU0U-ee7z22BHhGv9YoLU7lmaU8g9gPj2DFiyNo1q7m9piLtxyWA0bPK37jlZBi5Bb12j1oL3opZzlMgk35bugnQwMs40YA3rTqvMyswnGhMUDhO2QG3oTMRna-YICwzry3H8VkW4ijCDR2hxM93jht__V8JPaRkfiWudng0QbE5si4U8kETw4kAz7SVJQEkBFdl4OzEAo1xa7preC0BZT1DPYpSQrDYYrG4djKcWRiOtklPoqNGhPDSIUNQGnxIE8iwkKXn8PaoawDd_9MgFH5kkFpd6FfyWcuM30MS24zYXE2UTBRq1yQlHb_6qYmtrVIoOuFQekhFvICibBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa48d6eb3.mp4?token=tz3qU0U-ee7z22BHhGv9YoLU7lmaU8g9gPj2DFiyNo1q7m9piLtxyWA0bPK37jlZBi5Bb12j1oL3opZzlMgk35bugnQwMs40YA3rTqvMyswnGhMUDhO2QG3oTMRna-YICwzry3H8VkW4ijCDR2hxM93jht__V8JPaRkfiWudng0QbE5si4U8kETw4kAz7SVJQEkBFdl4OzEAo1xa7preC0BZT1DPYpSQrDYYrG4djKcWRiOtklPoqNGhPDSIUNQGnxIE8iwkKXn8PaoawDd_9MgFH5kkFpd6FfyWcuM30MS24zYXE2UTBRq1yQlHb_6qYmtrVIoOuFQekhFvICibBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی که سرباز اسرائیلی از جنایتشان منتشر کرد
🔹
‏روژ گذشته، یک سرباز اسرائیلی ویدیویی را در حساب خصوصی اینستاگرام خود منتشر کرد که تعقیب دو کودک فلسطینی با یک پهپاد کوادکوپتر در نوار غزه را نشان می‌دهد.
🔹
دو کودک غیرمسلح از حمله اول جان سالم به در بردند، اما تعقیب و گریز ادامه داشت و از سرنوشت آنها اطلاعی در دست نیست‌.
🔹
این سرباز متعلق به تیپ کفیر اسرائیل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/akhbarefori/652595" target="_blank">📅 05:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
شهادت سه فلسطینی در حمله هوایی رژیم اسرائیل به غزه
🔹
در حمله هوایی رژیم اسرائیل به یک خودرو غیرنظامی در محله النصر در غرب شهر غزه و اردوگاه پناهندگان جبالیا در شمال نوار غزه، سه فلسطینی شهید و تعدادی دیگر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/652594" target="_blank">📅 05:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652593">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOd6ixZxYm294Zss0fy4-l4Cmfy3Zk_jxFxk68bTDS2lsPY-wlBbGoKFvSBc7vTXPvPH23QImRClKxFhisdEhlLXrqLW_smJ8lQrLoxZOBNcKo4SEQdy5MTREfrB8trxPSYjVagrVDdCRIArHt0hPdTVjXvTOUuE_154N1DHQzjpFlvv2cJmHp9z-9xaSl-fz8_VmqfWsSBIoSc6sT80pyIf1yeyBIOmn_Le_q6q_LhCCgt6_0MB91-G8mFkGQAd_tvvQYlTNDhas4oZcGyYNNSVoRDZg5p-aIwwtQgdkA6hWiwIdsInq626L2DQduLbfSjgYLjeZjES9gj8zzRphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده روسیه در سازمان‌های بین‌المللی: اگر آمریکا و اسرائیل حمله به ایران را از سر بگیرند، نشان می‌دهد که از اشتباهات راهبردی گذشته خود هیچ درسی نگرفته‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/akhbarefori/652593" target="_blank">📅 04:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ایران ترور فرمانده کل گردان‌های قسام را به شدت محکوم کرد
🔹
وزارت امور خارجه جمهوری اسلامی ایران با انتشار بیانیه ای اقدام تروریستی رژیم سفاک صهیونیستی در ترور «عزالدین حداد» فرمانده کل گردان‌های قسام را به شدت محکوم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652592" target="_blank">📅 03:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652591">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
گردان‌های القسام: ترور فرماندهان بزرگ، مسیر مقاومت را متوقف نخواهد کرد
🔹
گردان های القسام شهادت فرمانده شجاع خود توسط رژیم اسرائیل را تسلیت گفت و تاکید کرد: دشمن جنایتکار صهیونیستی اگر فکر کند ترور فرماندهان بزرگ، مسیر مقاومت را متوقف می‌کند؛ دچار توهم است، چرا که این خون‌های پاک هدر نخواهد رفت و فرماندهان دیگری جایگزین آنها خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/652591" target="_blank">📅 02:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652590">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
«افت شدید توان رزمی» دلیل عدم مشارکت انگلیس در جنگ علیه ایران
🔹
شبکۀ فاکس‌نیوز با استناد به دو گزارش رسمی از اندیشکده‌های نظامی و پارلمان بریتانیا فاش کرد، دلیل اصلی عدم مشارکت لندن در حملات تهاجمی علیه ایران، «افت شدید توان رزمی و خالی بودن انبارهای تسلیحاتی» این کشور بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/652590" target="_blank">📅 02:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652589">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
شبکه «کان»: به هیچ وجه امکان ندارد انفجاری که در «بیت شمش» رخ داد، یک انفجار کنترل‌شده بوده باشد؛ آن‌ها قطعا دارند چیزی را پنهان می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/652589" target="_blank">📅 02:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652588">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9JfmagcpWoaX8HzmYx1nI9BrsRHhUheymix3VfsnYDOfJJhEFZslf2F444wpc7AVd_H17g2LEwtmjyBzlTXLePM3sAku0VomLSilEL_JGazoJpIL0vVRKbNfG69z6vYpFd6IfAWoq7fCDRsURO7G8diFZCo-Ua7lZqErkyo-DEkjfxBhkpfsZZCPTXroH5QrW2XkhjpSmebQhlUGxxDkT4Gvq14SmOJ4aAZN0k13EnVpU4i-IfXBh4aDcWB5bpZIvu09246Oi7kVYoXHVw1gjyunBxq9bCiBxfBvhN_LuQhjPOhr3ta9Cxe7RKvVYfNhU6Ho0UsB6n0StRHr4KUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیۀ وزارت امور خارجه دربارۀ ترور فرماندۀ کل گردان‌های قسام در فلسطین اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/652588" target="_blank">📅 01:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652587">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvCWpOSkzWLCzYqxGi61Kx2SnL_ZPx0FfG1IWK-kh-iWaO81kn77Qso1iBcbNTMkYoWCwGJD5p14V5ieo4JQmtR24BKztZbcr0tir5m8qbXln3Oh2U9T4Mm-Lsk2fEm7eq4C5qmH4h9VFFJGDSQVcaF8d2L5NJyQvaTYPBFiYjmaBaEXl_-hTqq-c7tAh6_2DKJATX1kQaMPbEgrFChCjvNLE7tl7sOTRkMjBfDIR5JPLp_yKl2HQHupSjrqmfScwpxIjEHGlKJgQIG8FqrAeia0IY_KXCGQksTpyYcQJKGdkZDrI1i51t9wnpE17JrQYeAtytvddGoTOAkhufSQGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات تکمیلی دستگیری فردی که رسانه های معاند اورا کشته اعلام کرده بود
🔹
فرمانده انتظامی شیروان گفت: یکی از عوامل اصلی اغتشاشات دی‌ماه ۱۴۰۴ این شهرستان که با انتشار اخبار جعلی، سناریوی کشته‌سازی را دنبال می‌کرد، در استان البرز شناسایی و دستگیر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/652587" target="_blank">📅 00:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652586">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°(منتظر شهادت)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15ca8c681.mp4?token=NAXlVYpPN6f0fJfg354iZoOamlcU1hoNL0MKzg3Mx8S_JgRtIUqsrV4yeiQf6XOD7oEVTVimkkCD8l-3-t02PeICtTgb5u99OwFdg_jsvqEVgNe8ScrI0X_x3_AGkkihcUlVsjiks6eMEtqW4PHSuLoTvC_pOObH5TE9g1umm2Ctb88w7FYGSv2P-j3bXkmx0aVLeMXpCnpzJi4j4033McLRFYFlSVP3GnuwO-Nk0qskowLyXPU9VHnwBAaRJQhCpKZ6P9BOxcPkr68M5EsZRr221OeVyIYgw46VKrOu3mwrMW_V9Q0ok_jr7mj4mK86uREGbpf201rvzCmeLZvRiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15ca8c681.mp4?token=NAXlVYpPN6f0fJfg354iZoOamlcU1hoNL0MKzg3Mx8S_JgRtIUqsrV4yeiQf6XOD7oEVTVimkkCD8l-3-t02PeICtTgb5u99OwFdg_jsvqEVgNe8ScrI0X_x3_AGkkihcUlVsjiks6eMEtqW4PHSuLoTvC_pOObH5TE9g1umm2Ctb88w7FYGSv2P-j3bXkmx0aVLeMXpCnpzJi4j4033McLRFYFlSVP3GnuwO-Nk0qskowLyXPU9VHnwBAaRJQhCpKZ6P9BOxcPkr68M5EsZRr221OeVyIYgw46VKrOu3mwrMW_V9Q0ok_jr7mj4mK86uREGbpf201rvzCmeLZvRiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجات دنیایی را از امام جواد(ع) بخواهیم</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/652586" target="_blank">📅 00:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652585">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای شبکه «کان» رژیم‌ صهیونیستی: انفجار در«بیت شمش» داخل یک شرکت موشکی رخ داد
🔹
شبکه «کان» رژيم صهیونیستی ادعا کرد: انفجاری که در منطقه «بیت شمش» رخ داد، در داخل شرکت «تومر» بوده است؛ شرکتی که در زمینه توسعه و ساخت موشک‌های پدافندی و تهاجمی فعالیت می‌کند.
🔹
رسانه های صهیونیستی پیش از این از وقوع انفجار مهیب در منطقه بیت شمش در غرب قدس اشغالی خبر داده بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/652585" target="_blank">📅 00:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652584">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAyz5D74pEr8wRWo3dJqVDcbg591VDObeUlmwFIvIIhoap1jRu6e8CtPVDG6F8-xoPJqjDwtdUbMDD2Psp4ayamAh0dMLvK10Md8NrHWB55-l4l8cFF2Xc8RTu3bgO85jXXV5OROiRU0sANqiOtwvP8rUeWd_cYQQiKe2htA--5KiD-GS3teWA8566ROdd3GXv0HKxk7ylIyuwSQNj1aSakClUOTq3Dcgp9_lgl-khqssPtlVDWkDSGidmob1-d8eEMFny0C--wQs8JzdWCDQePw6n4PKx2_wOUifIMP1JV2mpo3ZyO8ECIlJ_x_hyY-_Nxy4Izp8ZVM3gdDRGi7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اهمیت منطقه محل انفجار در فلسطین اشغالی
🔹
شهر بیت‌شمش واقع در غرب بیت‌المقدس که محل وقوع انفجاری مرموز است محل استقرار کلاهک‌های هسته‌ای رژیم صهیونیستی است.
🔹
پیش از این برخی از فعالان رسانه‌ای گفته‌اند که احتمال می‌رود کلاهک‌های هسته‌ای رژیم در پایگاه هوایی «سدوت میشا» که در شهر بیت‌شمش قرار دارد مخفی شده باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/652584" target="_blank">📅 00:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652583">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4922b5c6f.mp4?token=k8CgXKU4yxUENl2T7ajCQfPMZ3y4OpQs4_IuFmtambe3z_P0jTGsFV5Hhc1m6CPYTRPyr4AbpdH-x75i68nqMHFlC7TdPSMYk26SWKMx3IXUtOBtm6nPXtYggSfNXsjnaIat3JGgndvz4bT-Mirc4_to6Itdmy3OR1B0JrCaz8ffZ1oW_A0ej9ue2GidflEtaDhpwv8yX36CgSf-GzDmGpnF3h3QR7sYRLfpyT4oh2kcAGnvddMLGvITqfcBKWtOxooNkS3CYubU0NkBMrGeQLIi_hdrpmC5VxJ-iq251GWjoqWSKa_DUkxkabfzOBSzwfPa1ROwYn8qTRAUCeqoGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4922b5c6f.mp4?token=k8CgXKU4yxUENl2T7ajCQfPMZ3y4OpQs4_IuFmtambe3z_P0jTGsFV5Hhc1m6CPYTRPyr4AbpdH-x75i68nqMHFlC7TdPSMYk26SWKMx3IXUtOBtm6nPXtYggSfNXsjnaIat3JGgndvz4bT-Mirc4_to6Itdmy3OR1B0JrCaz8ffZ1oW_A0ej9ue2GidflEtaDhpwv8yX36CgSf-GzDmGpnF3h3QR7sYRLfpyT4oh2kcAGnvddMLGvITqfcBKWtOxooNkS3CYubU0NkBMrGeQLIi_hdrpmC5VxJ-iq251GWjoqWSKa_DUkxkabfzOBSzwfPa1ROwYn8qTRAUCeqoGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در نتیجه انفجار سهمگین در بیت‌شمش آتش همچنان شعله می‌کشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/652583" target="_blank">📅 23:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652582">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
از داغ‌ترین خبرهای امروز غافل نمانید
🔹
خبرهای لحظه‌ای درباره احتمال آغاز حمله دوباره آمریکا | جزئیات طرح اشغال جزیره لاوان توسط ارتش امارات!
👇
khabarfoori.com/fa/tiny/news-3215239
🔹
اگر آمریکا به ایران حمله کند، ایران چه‌خواهد کرد؟ + ۷ واکنش احتمالی
👇
khabarfoori.com/fa/tiny/news-3215311
🔹
پشت‌پرده سفر وزیر پاکستانی به تهران فاش شد | پاکستان حامل چه پیامی است؟
👇
khabarfoori.com/fa/tiny/news-3215448
🔹
بزرگترین سورپرایز ایران برای آمریکا در جنگ احتمالی پیش‌رو چیست؟
👇
khabarfoori.com/fa/tiny/news-3215463
🔹
مقام اسرائیلی: جنگ با ایران ازسرگرفته می‌شود | ظرف حدود ۲۴ ساعت، وضعیت روشن خواهد شد
👇
khabarfoori.com/fa/tiny/news-3215371
🔻
ویدئوهای جذاب امروز را در آپارات بخوانید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/652582" target="_blank">📅 23:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652581">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz2JUegGKCWx4Semy_5PS3MnoCvWbUDDlG63XmPILt0o-mtyU_aOrcoCbmQFZ7d9mrYdP6tl_DdTIB5NYztiYd8qo-tkHpu2wY3lui1aRdT7h19aVvws1jnWv0Y1GqzSCNcNQKJ0HWQEsHudSY6FP2o63ks2wgSQqwWDerbdRCvqpYXPy92kW4ilyLIOLUWjv3DPInUYhx04IfiJZWhejiAZycmZgJcKru2q7metPmAOa42Eoud55DoRa0Bs2qfaS1oVfAGjaB7HuO7Qt4kd4KYmcXokTSmLWCil-nfVBsqTsZMeD-mG2KjuRkl7-SdEu-QqZGpV6_Zxn2-Bum7p-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حماس: در صورت تداوم تجاوزات اسرائیل، واکنش نشان می‌دهیم
🔹
عضو ارشد حماس تصریح کرد اگر رژیم صهیونیستی به تجاوزات خود ادامه دهند، با واکنش فلسطینی و واکنش بزرگتر در منطقه مواجه خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/652581" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652580">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7948ef75ed.mp4?token=Dx1utB3828RpPZwuJlQnygc4NQVcBnbpuR7TNJV53VqpWwqV2lOoAfDwzjKVjBnb5Gjukwg4tUzg2RV7H0eRr497LxRnIMxOMmtWM_D1nauam7TnqqoEITP_IerTohwJcsSyp3iemaw1AAvcZqLiEiwdSy9vtYLU1R10-4EBv4qZfp7KEb_WZlCRcfKL1dLOLftWRaIo_sT4I9OcsfsJC5QT7daEeny31nN-NAZvE9yIJG5FIrPfTiW6vAFiziqSwYY1RzU3mrvVMmUEhlZlCnkBJ47fJ8yAcj0MWXUW3n9YALTsCXaI4YZCXoySOmG3zUiktWRvEV0vUoN-unfsNj2R0GmEKFkuq773j84C6a8wouU9Dhwabi1bAJjEBcAwCr6ZDk8RRGGj6KNU8Ej7iM8-KwxUjpk8k1bkZiOKSzVLQSbCSgj0tVRjbB6ywENIh4_4CLZzbGMXbAg8BI_OC2ZJkJ5IdgC8KcsYIDRnr7RPgQ3X0qQcWoJ-3TT4VfnDhEaNvHwkSyDRxWYNgD9iSOldUhEg-B6FbZUsJr3p4ybVoUQj1Fo5WErFoWkMMQloF-EpNyfFHQy4c5pfKRM2r7bRmCxHKt_65Wvk4UNlXAv_0x1bzO_85etkFIWoiE_GBgxzeK1mFwuVVL8dnOc8ATC6ZnhE9JPQYwN1e7L_Z6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7948ef75ed.mp4?token=Dx1utB3828RpPZwuJlQnygc4NQVcBnbpuR7TNJV53VqpWwqV2lOoAfDwzjKVjBnb5Gjukwg4tUzg2RV7H0eRr497LxRnIMxOMmtWM_D1nauam7TnqqoEITP_IerTohwJcsSyp3iemaw1AAvcZqLiEiwdSy9vtYLU1R10-4EBv4qZfp7KEb_WZlCRcfKL1dLOLftWRaIo_sT4I9OcsfsJC5QT7daEeny31nN-NAZvE9yIJG5FIrPfTiW6vAFiziqSwYY1RzU3mrvVMmUEhlZlCnkBJ47fJ8yAcj0MWXUW3n9YALTsCXaI4YZCXoySOmG3zUiktWRvEV0vUoN-unfsNj2R0GmEKFkuq773j84C6a8wouU9Dhwabi1bAJjEBcAwCr6ZDk8RRGGj6KNU8Ej7iM8-KwxUjpk8k1bkZiOKSzVLQSbCSgj0tVRjbB6ywENIh4_4CLZzbGMXbAg8BI_OC2ZJkJ5IdgC8KcsYIDRnr7RPgQ3X0qQcWoJ-3TT4VfnDhEaNvHwkSyDRxWYNgD9iSOldUhEg-B6FbZUsJr3p4ybVoUQj1Fo5WErFoWkMMQloF-EpNyfFHQy4c5pfKRM2r7bRmCxHKt_65Wvk4UNlXAv_0x1bzO_85etkFIWoiE_GBgxzeK1mFwuVVL8dnOc8ATC6ZnhE9JPQYwN1e7L_Z6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنا گاسپاریان، مجری مشهور آمریکایی فاش کرد رسانه‌های اسرائیلی خودشان اعتراف کرده‌اند اعتراضات مسلحانه‌ای که برای توجیه جنگ علیه ایران استفاده شد، پروژه‌ای طراحی ‌شده توسط اسرائیل بوده است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652580" target="_blank">📅 23:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652579">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
«مکان–رویداد بمباران مدرسه شجره طیبه میناب»
🔹
این مکان-رویداد اسفند ۱۴۰۴ در فهرست آثار ملی ایران ثبت شد؛ اقدامی که با هدف ثبت و ماندگار کردن روایت حمله به این فضای آموزشی، شهادت ۱۶۸ دانش‌آموز بی‌گناه و بازتاب ابعاد این فاجعه در حافظه تاریخی و افکار عمومی جهان انجام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652579" target="_blank">📅 23:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652577">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5105ee0640.mp4?token=j5fpoT1uRsToF3_-JKdKGotiBz5AUDdn5N9lr3NkoH-QBkNACzKgS-fxHFkKybJwq6f8eSmH5_RXAgM7HTvF9Czy2SN8rTjZkyT-rjBCQwgHimNGFEC4A_8uGkPsBCeyh5c15XM67Yg1pxOpmYRo_KvHB5u_Fl9sp3uZB1Sw2EJxaF73r4xc1DAROFCPZaBUZttJ1iX6on73wzo64C7WF0k8ZOJXCtchPbrVCgYb5UQigXTTvPy-DjqMTJNsGTCj5-IzodV-4Nmgx6aWXsCuLw7FEBogXGXQ_fkaFNE5PRHjaS24oPZvCmz41fTK4S8DIq3Sf8513gj_I_er92Dsiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5105ee0640.mp4?token=j5fpoT1uRsToF3_-JKdKGotiBz5AUDdn5N9lr3NkoH-QBkNACzKgS-fxHFkKybJwq6f8eSmH5_RXAgM7HTvF9Czy2SN8rTjZkyT-rjBCQwgHimNGFEC4A_8uGkPsBCeyh5c15XM67Yg1pxOpmYRo_KvHB5u_Fl9sp3uZB1Sw2EJxaF73r4xc1DAROFCPZaBUZttJ1iX6on73wzo64C7WF0k8ZOJXCtchPbrVCgYb5UQigXTTvPy-DjqMTJNsGTCj5-IzodV-4Nmgx6aWXsCuLw7FEBogXGXQ_fkaFNE5PRHjaS24oPZvCmz41fTK4S8DIq3Sf8513gj_I_er92Dsiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار بزرگ در بیت‌شمش در قدس اشغالی
🔹
رسانه‌های عبری از وقوع انفجاری بسیار بزرگ در بیت‌شمش واقع در غرب قدس اشغالی خبر می‌دهند.
🔹
این رسانه‌ها با بیان اینکه ارتش مانع از ورود خودروهای امدادی به محل حادثه می‌شود، تصریح کردند این انفجار احتمالاً در تأسیساتی حساس رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/652577" target="_blank">📅 23:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652576">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg8hAMG-smO73WGrFreHSoUxlDDGClHHflGQGVrRrC1hgLMmURABFub8oxiRPzp1fJfi0cJN7ZFS2pJcz6z0OSdXf0Ypo-UHfe-uwu7d_sR_wF0YUUmRniJYjPKot5WYIXogatkh5tteOyQ1soxwGiHMoCsFyJiK0XGyt0yb9orJ78rXhhQ8kQswJPREHZ1HVhAG7IioSaaw_GzPes-ISeDB87Q0OHksxN4MdTbtNSnLkLmvvFazvwAdu8dr74CDaLB1jxt7NkBwLB8jgwD1zda5dtxQUFYe0zER5TBPgZ31gOQYaKRU28HzPgDTPPiO7NaHuf9mOt5Pknwo6I771A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکرار تهدید کاخ سفید با انتشار تصویری از ترامپ در اتاق جنگ
🔹
کاخ سفید پیامی تهدیدآمیز از رئیس جمهوری آمریکا با عنوان «شوخی نداریم» همراه با تصویری از حضور او در اتاق جنگ منتشر کرد.
🔹
در پیام کاخ سفید آمده است: «اگر به آمریکایی‌ها آسیب بزنید، یا برای آسیب‌زدن به آمریکایی‌ها توطئه و طرح‌ریزی کنید، ما شما را خواهیم یافت.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/652576" target="_blank">📅 23:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652575">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyqYK2sVL4c4L5tpNuNLwTZQ3gfwL-eiPeGJU7z48xL00WNX5q4_BEi8wcmaKeh-LouMfULMvavxHBRrGcayCRzTzAq_Agd1CWHtD9MqLoD4f1iH5SLFmyTxDnBcUikqZGEAkBmjDZzCafxFiF30vX8abi2-mv1XNg9d-LOyohmHtiwlWWbMtuMUWOBg7z4Q4yp-e7XnFf4HBxFR-9MJBObYLr63p8V23C9W4c-ZXF2_U2dYmKacWRP3SeQg4TsLcfPWINFZOnTVkUCHkyT1de0tJ5PqNHgYFc1DDvidLuJae9cz5zOdO7fAOnuAA--sh6PmKeMj69JquxviR_R2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگترین سورپرایز ایران برای آمریکا در جنگ احتمالی پیش‌رو
🔹
ایران در جنگ ۴۰ روزه با بستن تنگه هرمز، بزرگترین ضربه را به ارتش آمریکا زد. این اتفاق ممکن است در جنگ احتمالی پیش رو نیز تکرار شود، اما این بار در تنگه باب المندب و توسط متحد منطقه ای ایران یعنی یمن.
گزارش خبرفوری را بخوانید و در بحث داغ مخاطبان شرکت کنید
👇
khabarfoori.com/fa/tiny/news-3215463</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/652575" target="_blank">📅 23:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652573">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d9f9f757.mp4?token=KMeCkY7hbxYGl5Ks8Zp7B6DzKLoQ7taw_Tsfs1kBlmcXi1mLuVtlFBTjio3QEV0A-qq6wU5h5z0Wr5h0y49-1a13nx0_ZgSfRkHL5uyY98sl6P2VjM-JKAd6UJvwsx1iQ_1XOIuKnbWXs4_QlfDVGYxcj1fX3wGAaHCZujBdvgA1EytNP7xcA3xpkxWKvYjypjadPcrEkc9RuFhviiPOsxGGj_9FNyn81V2dxag8NLjoxTCjhH9XtRBzv6_yWCqGh2Ejzy13QUPmbunMuN6CI_L2TZn6NGMVv0hARis_dWy2EGsdBexRqGnbP-y5cAnlXf1fuvaypgNKXtKBz4gpYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d9f9f757.mp4?token=KMeCkY7hbxYGl5Ks8Zp7B6DzKLoQ7taw_Tsfs1kBlmcXi1mLuVtlFBTjio3QEV0A-qq6wU5h5z0Wr5h0y49-1a13nx0_ZgSfRkHL5uyY98sl6P2VjM-JKAd6UJvwsx1iQ_1XOIuKnbWXs4_QlfDVGYxcj1fX3wGAaHCZujBdvgA1EytNP7xcA3xpkxWKvYjypjadPcrEkc9RuFhviiPOsxGGj_9FNyn81V2dxag8NLjoxTCjhH9XtRBzv6_yWCqGh2Ejzy13QUPmbunMuN6CI_L2TZn6NGMVv0hARis_dWy2EGsdBexRqGnbP-y5cAnlXf1fuvaypgNKXtKBz4gpYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دفاع مدیرعامل جی‌پی مورگان از حمله نظامی به ایران: باید سال‌ها پیش سراغ سرِ مار می‌رفتیم!
🔹
نیروهای نظامی می‌توانند برای باز کردن تنگه هرمز؛ ۴۰ سال برنامه داشته باشند. آنها طرح‌هایی دارند. نمی‌دانم آن طرح‌ها چیست. امیدوارم کار کند.
🔹
جیمی دایمون، مدیرعامل جی‌پی مورگان؛
🔹
جی‌پی مورگان (JPMorgan Chase & Co.) یکی از بزرگترین و قدیمی‌ترین بانک‌های سرمایه‌گذاری و خدمات مالی در جهان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/652573" target="_blank">📅 23:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652572">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
بلومبرگ: آمریکا معافیت فروش نفت روسیه را متوقف کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/akhbarefori/652572" target="_blank">📅 23:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652571">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
آمریکا معافیت تحریم نفت روسیه را تمدید نکرد
🔹
این معافیت قبلاً به مدت یک ماه تمدید شده بود تا کمبود عرضه نفت و قیمت‌های بالا ناشی از بسته شدن تنگه هرمز توسط ایران کاهش یابد.
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا پیشتر گفته بود که مجوز خرید نفت روسیه ذخیره‌شده روی تانکرها را تمدید نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/akhbarefori/652571" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652570">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkVn1E2UaQltUpesPCX6k507kDq7RNHUpmsVvCibwHkdriO3aODBA2i1jULMdZdT6k9lD7lRgNr2kbwxBh7QYgMH_gwQDM9ILPIWG448einUGWLIro6VlJIhjmlVJHd2g31skPGz7NT_ct9YatPCCPcNdMOJDf5Kcq2ouDiuxv1l82-HwbtsTh58nSRr_rL9g15_vnA-DpoIBlX3tm5fLyvi8aqB-nHxUgNA6NJB7rypB8x2C8-36rp64ZI3HfzpbNt7qyWjmt6teRr768ywKgrU1USc9VdgAYH0JPTvS5RceUdhCgKDoOj2l5Mh1S-g7xKkezB2X7BvagecgD4mtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: مقاومت ملت ایران، تحول جهان را سرعت بخشید؛ آینده از آن جنوب جهانی است
🔹
رئیس مجلس: جهان در آستانهٔ نظمی نوین قرار دارد.
🔹
چنان‌که رئیس‌جمهور شی گفت: «تحولی که در یک قرن دیده نشده، در سراسر جهان با شتاب در حال پیشروی است»، و من تأکید می‌کنم که مقاومت ۷۰ روزهٔ ملت ایران این تحول را شتاب بخشیده است.
🔹
آینده از آنِ جنوب جهانی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/652570" target="_blank">📅 22:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652569">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8fSGClsCVfsI-jbojIQao-sAVbfzzfFtr0hr_4ttkViaZ7OmIt_KQVuu1GbG_MmY5tTS_1Z9Mo4alXsDQfFLizP07aQIaytXI_reJPxVzW-cwP6ntZxFtfaJ8bdueTwWDX2vw_37p-X9aDvQ2f4rUyI0naacUCKkjG9D2EDMgGwolJIyZgWEniTMrsIuNzRtlvXTkvH-M2O32L09meB0GmFdWcHenpqf2urDAiuY_Ep-kfL3vXDyt39AslVTGXnry1tYCc9JyLHzvMmsgjPGOfBGTH6t8F_vi9nuwNmxjgfrwZDyhu0wuNH4tEhCRHc9xoQtVteH7UmrdRoX2QZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوخت سخت
🔹
در پی جنگ تحمیلی سوم و محدودیت‌های تأمین سوخت، صف‌های طولانی در پمپ‌بنزین‌ها شکل گرفته است. این شرایط بحرانی نیازمند همراهی و مصرف مسئولانه مردم است؛ استفاده از حمل‌ونقل عمومی و پرهیز از سفرهای غیرضروری می‌تواند کشور را عبور دهد. اما نکته کلیدی آن است که مسئولان تصمیم‌گیر پیش از این باید تدابیر لازم را می‌اندیشیدند. موضوع خودروهای بی‌کیفیت که اکنون قیمت‌های نجومی یافته و نیز انبوه خودروهای فرسوده، باید یک‌بار برای همیشه حل شود. تا ریشه‌های این بحران ساختاری مدیریت نشود، هرگونه کاهش مقطعی مصرف صرفاً مسکنی موقتی خواهد بود. همکاری مردم در کنار تصمیم‌های درست و اصولی مسئولان، تنها راه برون‌رفت پایدار است.
🔹
هفتصدوپنجاه‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/652569" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652568">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991a0ca5bf.mp4?token=vTCHSitNG85uL1NkCJxq2wKYF8yyg5UQ_golrYHe5QO35djabuuso8C8dMkU7GI-ZcZqg0YHn9GmShWGq8_0U1Agv-OGVAP9qTyWi2DrJHGS4VmoGQaaXYBwqWRSeLBmc5Wak2rSLyWR5ZQtRt4K-FHCGrMn0v2dsn6vyu4dRfA1nx5RMRrKbFT25XGhB1KP3HQrdqZ50tcvfeGOzeUNVc2xR8LnA4OTD38GsUtgPCbMCY6axA8XEMwuH8C1kmaZE_71dkqzH0zmjyjjgO0zw_tbm9M2Ni0WX3Uk8RyyixFv8dQ8-JHEqVvYJEf6ALEVo-2zJsaA5ikoWvfTB5LbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991a0ca5bf.mp4?token=vTCHSitNG85uL1NkCJxq2wKYF8yyg5UQ_golrYHe5QO35djabuuso8C8dMkU7GI-ZcZqg0YHn9GmShWGq8_0U1Agv-OGVAP9qTyWi2DrJHGS4VmoGQaaXYBwqWRSeLBmc5Wak2rSLyWR5ZQtRt4K-FHCGrMn0v2dsn6vyu4dRfA1nx5RMRrKbFT25XGhB1KP3HQrdqZ50tcvfeGOzeUNVc2xR8LnA4OTD38GsUtgPCbMCY6axA8XEMwuH8C1kmaZE_71dkqzH0zmjyjjgO0zw_tbm9M2Ni0WX3Uk8RyyixFv8dQ8-JHEqVvYJEf6ALEVo-2zJsaA5ikoWvfTB5LbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای عجیب ترامپ: ایران در گذشته بارها تنگه هرمز را بسته است!
🔹
ترامپ در ادعای جدیدی گفت: ایران سال‌هاست که با استفاده از تنگه هرمز، جهان را تحت فشار گذاشته است.
🔹
ایران از انسداد تنگه هرمز بارها و بارها بهره برداری کرده! (بارها تنگه را بسته است)
🔹
آنها در گذشته تنگه را بسته‌اند. از آن به عنوان یک سلاح استفاده کردند!
🔹
اما الان نمی‌توانند از آن به عنوان سلاح علیه من استفاده ‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/akhbarefori/652568" target="_blank">📅 22:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652567">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519197d026.mp4?token=BoKx-hnhZDfEnYBbwqLCiuh69doEKW-K55vygybK8_EXFE05WcYhFhrXnjRChHmAKeqrLz60vGBYeHsvz-N70api6elBycVgY9K3ajolYwRgtDKWGttLZ0clCh0tB6b5pC6bHuTu5vu3XYCTa3lH2Z88sTbTCiz2fN7IpTwAKnBxF6DExV8R4ZFcOmM_PuwW6w__6bAg3S-EJ_Ia-J79g6USaKNU7M0Vj-xSlFxuHPPac4L_8vqwPdo5wg6xJV_udys26ksmfUuw8Fam6Deq6dmMnlgvM0LVNESYkuXFbssWumUVolO4_4tChyAdeEGmxPSjC6dMDLwqKYDun3-G8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519197d026.mp4?token=BoKx-hnhZDfEnYBbwqLCiuh69doEKW-K55vygybK8_EXFE05WcYhFhrXnjRChHmAKeqrLz60vGBYeHsvz-N70api6elBycVgY9K3ajolYwRgtDKWGttLZ0clCh0tB6b5pC6bHuTu5vu3XYCTa3lH2Z88sTbTCiz2fN7IpTwAKnBxF6DExV8R4ZFcOmM_PuwW6w__6bAg3S-EJ_Ia-J79g6USaKNU7M0Vj-xSlFxuHPPac4L_8vqwPdo5wg6xJV_udys26ksmfUuw8Fam6Deq6dmMnlgvM0LVNESYkuXFbssWumUVolO4_4tChyAdeEGmxPSjC6dMDLwqKYDun3-G8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله‌ی پلیس برلین به تظاهرات ضد جنگ ایران و فلسطین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/652567" target="_blank">📅 22:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh76L96moPWwsqWm9sAL3UiCbIskiP3nsTC2BnxUvIHl_D4XPk4ZIEdFp4TabmjC9L1HFRKT1ukF9w9MvP36lYba5TV2GGg_RylExxNI1cv8CieeM_B4FON6VUNJWolurVoxrGxhZFQKZIVf9i7Lzmi4ap_HGBYGtswMg3ZyW9HzQ4LmyqKsF2FFh6rqRBNQTZKFOrQKkZHShl45TMwZ42HPReCk_v7kUpXFGY3H7wdDzZMUJpIIzOXpdRJ__TVcrm7rUwO8nwCOsvcJExbLDJtG2PVsH-QX3eMB7bYrc9V6pkXxwjv4Y-pvOZdT4LZPmCFP1DL7cNlP9lRiEeqn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوثری: هر تعرضی با پاسخ کوبنده مواجه خواهد شد
🔹
عضو کمیسیون امنیت ملی مجلس: اگر آمریکا یا رژیم صهیونیستی کوچکترین تعرضی انجام دهند، مردم ما، چه زن و چه مرد، در صحنه حاضر هستند.
🔹
دشمن هر توانی داشت در ۴۰ روز گذشته انجام داد، آنها نمی‌توانند به راحتی بمب‌ها و موشک‌های از دست رفته خود را جایگزین کنند، اما ما به راحتی میتوانیم جبران کنیم.
🔹
آنها در هر نقطه‌ای که حضور پیدا کنند، رزمندگان و مردم چنان ضربه‌ای میزنند که جز ذلت و خواری نصیبشان نشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/akhbarefori/652566" target="_blank">📅 22:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652565">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaM-YKpp2iIPM4_8T6iwMPFDsNNXuhixT0ot_GBIpXZxVUuWR9iAGIJf1dBftygWVCmlI4oQUwW2B2pEKt1YCVoR_D_w3cz4iEFZHA9McSxRf_b9L61B_Ob4BUYWIB8UYUKXZBFYTa2tISVuErb2U7khG6KEJqF98jD0gB621lUbMKMGaoL4dOJq6OrF-cJ-QK-DGQfmZBsqt2kAnuFZAoIdPXHSlX_gt--Hd4Wl6PehjhQdnelzgbM0a8gj7b_VkWIBWPhoph4tackruJHYwEETyHjNDsex3woV3cjJezZOQf_D5h27Ecq50iV5QPhuqVe84jkgub5XDDBRmvQijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حزب‌الله شهادت فرمانده قسام را تسلیت گفت
🔹
حزب‌الله لبنان در بیانیه‌ای به شدت جنایت شنیع صهیونیست‌ها در غزه و به شهادت رساندن عزالدین الحداد، فرمانده گردان‌های قسام به همراه همسر، دختر و چندین غیرنظامی فلسطینی طی حمله هوایی جنایتکارانه را محکوم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/652565" target="_blank">📅 22:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652564">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agL7IgXFhJHsx_GSHkql968-Jfmn-q8083uwwRZL8zXWxK5EecmkyDZVhQESe4v-0tUnwkUtKVYtgEhtgbE624H7VAl9-WQdd_kG-rx8yX-lgpyofgzhPpwiK2hja1XWsaF_VR67fC883BpcIcEU-LmCcgs1bImHowiiivQntNvo2MKyzt5O1GQSXCsdMm3xEKUM6c8fj2bOO3pCJH5gmM19r9ufsAMy9uvSAvZ7aXbkCRUM6QrxtDfYXllJzil9ajhpL0Prtft4k-jkZIag32HRWk53N4JGDZhDAaHN_x_JxSGE-7XdZ0vztuoOfIGL21YeFhE2kSDy50WlctmOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلاکت یک نظامی صهیونیست در جنوب لبنان
🔹
ارتش رژیم صهیونیستی از هلاکت «یسرائیل ریکانتی»، از عناصر تیپ گولانی در نتیجه اصابت مستقیم پهپاد انفجاری حزب‌الله در جنوب لبنان خبر داد.
🔹
ارتش اسرائیل با وجود سانسور بسیار شدید تلفات و خسارات این رژیم در جنگ، اذعان کرد که شمار نظامیان کُشته شده در جنوب لبنان از زمان جنگ جاری به ۲۰ نفر افزایش یافته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/akhbarefori/652564" target="_blank">📅 22:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652563">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318b3eb231.mp4?token=gra054Kuvb1gDn95IFzfJPDhSkFpiDvuhUhGUx63qy-9IjZvAxGlbiwHu47VQwZSFJZnEEPzrSBVcS9oiIbhl1EMCb9glKAZoAg_85y9zQpDMOJeEzlMjN0-y-NdNjW8bTslfJqs3Z-OEv54hT9OW_69mKRkfvX_yQIFrFYbPaLsxkzSYS_cmbOm2EQEAm6QdKKzCycMF_PntUjg4IaPYJ2xKAosrdi5RnIOhSrnV1lA6jVv1emkfgJEafktZZy3q9GozjNjsTOP0C31HDFo1uEbMdD5bIwCsh8dYqzYzNmgX-sIFpgnH7XRVHUchXpkC3-YxalaHqXpu0CCzZH2hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318b3eb231.mp4?token=gra054Kuvb1gDn95IFzfJPDhSkFpiDvuhUhGUx63qy-9IjZvAxGlbiwHu47VQwZSFJZnEEPzrSBVcS9oiIbhl1EMCb9glKAZoAg_85y9zQpDMOJeEzlMjN0-y-NdNjW8bTslfJqs3Z-OEv54hT9OW_69mKRkfvX_yQIFrFYbPaLsxkzSYS_cmbOm2EQEAm6QdKKzCycMF_PntUjg4IaPYJ2xKAosrdi5RnIOhSrnV1lA6jVv1emkfgJEafktZZy3q9GozjNjsTOP0C31HDFo1uEbMdD5bIwCsh8dYqzYzNmgX-sIFpgnH7XRVHUchXpkC3-YxalaHqXpu0CCzZH2hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئيس كانون كارگران بازنشسته تامين اجتماعی تهران: پرداخت حقوق و احکام جدید بازنشستگان از خرداد ماه اعمال خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/akhbarefori/652563" target="_blank">📅 22:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652562">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-text">✨
بخش دوم | ادامه‌ی مسیر همدلی در روستاهای مرزی زابل
💫
به رسم  پربرکت دهه کرامت، با همراهی خیرین عزیز و هیأت‌قرار، اقلام معیشتی میان خانواده‌های شریف روستاهای مرزی شهرستان زابل توزیع شد؛ تا سهمی کوچک در لبخندهای بزرگشان داشته باشیم.
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/652562" target="_blank">📅 22:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652561">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8h1TueJTQ32UDKFImSQv4AiMiE3hg1XlXA7NYKSC2LGCdPZMcvNFwHtIB0FdJ2QmhifgujgAwkQXBwNXvmFqrL-KYu6PZIj_22UNoOU3ht9iUuLCrwveHIqcAlKiEAve58cHfp3GK5gmv_LOAmLewu1vUkaeuU4__dmct3A3s95AfQv1mmsPqDinJGDaeBURu0KIYETgoBjkU1b5KcMh7_UpHsyFgGTyQNIkiSVQqmcwz8ljWAXopy8mUUOiHPyqGnXKZ3rkLJ_XkTVRJE47cOtjoPoM0Rax53TvT7osKpUh9dr2CqONm92nUO9o7yolVk8jVrfol0f5UVApw6YGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاکستان جای خالی امارات را برای ایران پر کرد
🔹
پاکستان با کاهش تعرفه‌های بندر گوادر خود و پذیرش اولین کشتی تغییر مسیرداده ایران، تلاش دارد انحصار امارات بر ترانزیت ایران را برای همیشه بشکند.
🔹
این تصمیم درحالی عملی می‌شود که مسیرهای مرسوم واردات و صادرات ایران از طریق امارات با اختلال مواجه شده است.
🔹
پاکستان علاوه‌بر تخفیف ۳۱ تا ۴۰ درصدی در تعرفه‌های بندری خود، یک ماه انبارداری رایگان هم برای کشتی‌ها درنظر گرفته.
🔹
کارشناسان معتقدند که اگر این روند ادامه یابد، وابستگی تاریخی ایران به بندر جبل‌علی امارات که تاکنون سهم اصلی ترانزیت ایران را در دست داشته، برای همیشه پایان می‌یابد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/652561" target="_blank">📅 21:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652560">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3-aaoy0nfH6ebKsihgp3-3DqUiHU4VvJ34R4s-Cq127zUKmaHj6363ayo9YRyQlTqfMoC7FB7ISW1p18B6BV9XnskT9u00I5vlBtgYEAQZVQX9Qil7cMXlFU5rkXShL68kyZM5iNRMHRN3LgDHgcdFnMHAnaMzjsK4b0gPkkhVrO5e-HOkZGrhOQgcR8F_G8KjnqTHhE5QvYQo7x7UmjQj-_jZVLwjc3POornwtLFXvuRpTGN1jeOrL5G5DJ4zg81kWyw1QIg72kj7dIfprmyptfN3oy8EoK0vi-7XgTcqfXpSG93eqXNndc7bz9dXSuaWGKbRHnJVkbu0IqC7wtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان بحران، سرعت خبر برای افراد مهمتر است یا دقت آن؟
🔹
در این نظرسنجی بیش از ۳۶ هزار نفر شرکت کردند که سهم روبیکا ۶۲٪، بله ۳۶.۶٪ و تلگرام ۱.۴٪ بوده است.
🔹
بیش از ۴۳٪ شرکت‌کنندگان در زمان انتشار اخبار مهم نظامی، ترجیح می‌دهند کمی صبر کنند تا گزارش‌های جامع و تأیید شده را بخوانند.
🔹
حدود ۲۴٪ هم اخبار فوری و کوتاه را حتی بدون تأیید نهایی ترجیح می‌دهند.
@amarfact</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/akhbarefori/652560" target="_blank">📅 21:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652559">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bec27ace.mp4?token=taQ2bf4vTVHfD6MtupNoK9X8Ao4AoXjEUmAI_DCCbD9Rf0HzLPFARILghxcVdbBUcjdtPm8CTbGwvTRvk8uAS5lDitk58rA0ieEAVVgM7cMFoipa-YNTw3ZksCSyra_lwP8_E3VtYyb7GE10K8D-NUuBlTAZfGm2dgmGWOvtGe7K_Xj3hPvKlLZXwLgjGFIHZlZ4UbRx6GEFyOetZrT4PLTrlMsY0gH0-b5lypndKaPHvracNQQp2gtJ-RUkp_ae4veoUYPnk_PO7BpopIeo2k-_jl63g82hQVZ10c5V2re9isJWn_M3xTvcxaO_Yb77igcYlGFMAp2KqpXameeK9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bec27ace.mp4?token=taQ2bf4vTVHfD6MtupNoK9X8Ao4AoXjEUmAI_DCCbD9Rf0HzLPFARILghxcVdbBUcjdtPm8CTbGwvTRvk8uAS5lDitk58rA0ieEAVVgM7cMFoipa-YNTw3ZksCSyra_lwP8_E3VtYyb7GE10K8D-NUuBlTAZfGm2dgmGWOvtGe7K_Xj3hPvKlLZXwLgjGFIHZlZ4UbRx6GEFyOetZrT4PLTrlMsY0gH0-b5lypndKaPHvracNQQp2gtJ-RUkp_ae4veoUYPnk_PO7BpopIeo2k-_jl63g82hQVZ10c5V2re9isJWn_M3xTvcxaO_Yb77igcYlGFMAp2KqpXameeK9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیگیری وضعیت دارو، کمبودها و قیمت‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/akhbarefori/652559" target="_blank">📅 21:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652558">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdWlj-cJQHgFko3F4Dtd5X4-vfxFRIERIk8I9pkBzslz-D9DFQu9c6_PlvexkZZGp8U7zrMyn4AOJEa4ISwxZQb2y85uvraVNvuLZsrCOYI6tifxC0fwpfgCs8u06oJJuCr2IngYm9XHEhRRuuJ5mwxR_w5gzHsdn7FW0r6ABy7mGAfS5JcPRFP1a-uqLwmOeSEkqcBo6OqkZET9NXpugv0WLP9TfSaaVr6eEG7dm7N6WuKWmOXltrJzMed2F_nG1PccEtS4GpKM9VRzDUHQWD6amdU38AIzuFmAC61Ipib_-548H7t-3j2mjzsxQ4f3JZx_OK0Ic0-CC6OMjj0NgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گالانت، وزیر جنگ سابق اسرائیل: به وضوح می‌گویم که هیچ‌کدام از اهداف راهبردی جنگ درباره ایران محقق نشده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/652558" target="_blank">📅 20:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652557">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044a1cdda5.mp4?token=WoacJ1RnzAqCYC1AX_GVYH0qubDIOB95m8vUVMxpeqxhfmhSNGiBdPzwBDqv2JxTyfKapVY4nhegPlyIlkmWVEmtZXRVNMb7ZcCV0FwiL8iOU0rsgSl0OV-2yaT-lsNkykmFdqvrwvdZykQRqcSX90SuwTmS-LEeaAisuJsEUPn8SQskKSQcXngDr6F2v-49wBbhCPQM63-TxQ39xa1Qx7HPPjVSbv8yrdJKwllyA2oemKm1gcUH8bihhXejZ0LG1Hvt0uX8ZvpyeCBaPhi5YHeBZFLCIHAApsu24_G4vohp7NcF2m6md2rVw9tcBmZ8xIRax_KIkhdg5pxxfoW9GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044a1cdda5.mp4?token=WoacJ1RnzAqCYC1AX_GVYH0qubDIOB95m8vUVMxpeqxhfmhSNGiBdPzwBDqv2JxTyfKapVY4nhegPlyIlkmWVEmtZXRVNMb7ZcCV0FwiL8iOU0rsgSl0OV-2yaT-lsNkykmFdqvrwvdZykQRqcSX90SuwTmS-LEeaAisuJsEUPn8SQskKSQcXngDr6F2v-49wBbhCPQM63-TxQ39xa1Qx7HPPjVSbv8yrdJKwllyA2oemKm1gcUH8bihhXejZ0LG1Hvt0uX8ZvpyeCBaPhi5YHeBZFLCIHAApsu24_G4vohp7NcF2m6md2rVw9tcBmZ8xIRax_KIkhdg5pxxfoW9GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون اول رئیس‌جمهور: دیگر اجازهٔ عبور تجهیزات نظامی دشمن از تنگهٔ هرمز را نخواهیم داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652557" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652556">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640a18d638.mp4?token=mZkDg7Dt93-K8cSIcdFu3BmcVOk7dWDFy75irjM2ufqYXJ8mGMAKZ8OINbaGcQAOhvRWDjafr8l5OVcC-9e2AykoDqWwQgRP7AmJ1dDVDkkEGGhF-UswsdgVAipK0_3c_Gjyn-K5kJLaWfBiyQr03SHN5TjtfrT3cXBrjZJmDPMxqGwvnMGvfXbB7CyjwYpDJkjI2GGO5_gLDEpW6HeAlIFor9GQ6wAFogJfomwTLRAQ2Czk2Y4uZWujo2HhVr6IZ1_QzK4A7-EENFXhVilQ-aPb5Ucmh3FvStRMHbNiExUCzhlfh9MJgdesgcmkbLL3bomVf53poeSizYIBN20USA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640a18d638.mp4?token=mZkDg7Dt93-K8cSIcdFu3BmcVOk7dWDFy75irjM2ufqYXJ8mGMAKZ8OINbaGcQAOhvRWDjafr8l5OVcC-9e2AykoDqWwQgRP7AmJ1dDVDkkEGGhF-UswsdgVAipK0_3c_Gjyn-K5kJLaWfBiyQr03SHN5TjtfrT3cXBrjZJmDPMxqGwvnMGvfXbB7CyjwYpDJkjI2GGO5_gLDEpW6HeAlIFor9GQ6wAFogJfomwTLRAQ2Czk2Y4uZWujo2HhVr6IZ1_QzK4A7-EENFXhVilQ-aPb5Ucmh3FvStRMHbNiExUCzhlfh9MJgdesgcmkbLL3bomVf53poeSizYIBN20USA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی نفسگیر از انتقال امن بمب عمل نکرده دشمن متجاوز آمریکایی توسط یگان چک و خنثی فراجا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/652556" target="_blank">📅 20:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652555">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a182fe40.mp4?token=j-8_6MfIkKIUR33Zi2hUihvls23JTJCDO5B9C2Xcg4Nkr1xpqTEDaIxDmITwSbGBLkD4_1MKsfaAV-IXNcnVDy0GM7oT_xivryMah119OWSKwWO3Y1pF78JMl0pv7NvkyxszPpcJnDr9gumHjk2K-yHELIRJh-h0ThyIiNhZidApDtzgEWOWq_5l_kqLhtwPpHjDYDyB1HhXIaKJggdiwjEt7Ou1TL96kWOrorftcou1Fbxi0woUURmCbHkyb3d3q5jvym4dt2vzJniQoL16yIGT3MrcBZrmMADBj5IGQ_uRMyL-kRgFBjbxD6Fs0OqSxaNY_VphswMbGyLxuw5WPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a182fe40.mp4?token=j-8_6MfIkKIUR33Zi2hUihvls23JTJCDO5B9C2Xcg4Nkr1xpqTEDaIxDmITwSbGBLkD4_1MKsfaAV-IXNcnVDy0GM7oT_xivryMah119OWSKwWO3Y1pF78JMl0pv7NvkyxszPpcJnDr9gumHjk2K-yHELIRJh-h0ThyIiNhZidApDtzgEWOWq_5l_kqLhtwPpHjDYDyB1HhXIaKJggdiwjEt7Ou1TL96kWOrorftcou1Fbxi0woUURmCbHkyb3d3q5jvym4dt2vzJniQoL16yIGT3MrcBZrmMADBj5IGQ_uRMyL-kRgFBjbxD6Fs0OqSxaNY_VphswMbGyLxuw5WPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عذرخواهی تفنگدار سابق امریکایی از مردم ایران: از طرف کشوری که بدنیا آمدم بخاطر حمله به شما وکشتن کودکان میناب عذر میخواهم
🔹
کن اوکیف در میان تجمع خیابانی در مشهد: شما با شیاطین در جنگ هستید.
🔹
من در وسط جنگ درخواست دادم بیام ایران تا مثل شما باشم و دفاع کنم مقابل شیاطین.
🔹
کشورتان(ایران) و شما مردم فقط جرات داشتید جلوی این قدرت ها بایستید هیچ کشوری این جرات را نداشته پاسخ جنگی از طرف اسرائیل وآمریکا را بدهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/652555" target="_blank">📅 20:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652554">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsxPWdkaxhcl2f61yZQ3rmm3wSWeamKuf6M726MicpxwuQo-1hh3tA3lo_xL5Adc2jNJZ3StiOzsV7W6TmmvuqGfoWM8EHOC_tlBY-yzR24TzuXglKDm3dpsb1LoolSQ16HKAaRrt21q7_irXI0SWZyRcDInfJjskIcHTh_BCFM2aC45fwaqJkTU8lSb4kk0NhrrX8ZDcqJqnog_1PmQTU1O9gjRNJFQ0A5CS52V_YZLhGh8abWiYOuBgB-U3fwCFMIBfFZvWcVo7ZBcF7C-rkMPDtVt23G6z9vnFRczw3W-7MZ-xtL_59Whz9rJCJZsnKam7YQ_5uVLmLqwXWl5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژاپن تایمز: با تداوم جنگ ایران، کاخ سفید برای کاهش قیمت بنزین به تقلا افتاده است
🔹
مقامات دولت آمریکا در حال بررسی داده‌های بازار هستند تا ارزیابی کنند آیا میانگین قیمت ملی می‌تواند به ۵ دلار در هر گالن برسد یا خیر، در حالی که داده‌ها نشان می‌دهند که هفت ایالت از این مرز عبور کرده‌اند.
🔹
دغدغه‌های دولت با جهش صادرات نفت و سوخت آمریکا به سطوح بی‌سابقه عمیق‌تر شده است، امری که توسط خریداران آسیایی و اروپایی برای تأمین منابع مورد نیاز هدایت می‌شود ولی ذخایر داخلی آمریکا را کاهش داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652554" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652553">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH0GcfA8Eyju1B84bGEgwdcAuJ5Bts3FqbYHrNdkuCe7z3WRSGfYDeKoiSVlGvy0mtfvNxKsfRoPS_dH6lHmrI43vZOpL15SS6cTbpXXIgfXPXsyf6uWoxHcXG-CYjcwoUYRgRXhNHQB11WYSFb6TPxLsN50Cupo0mJ0yH4pbTt4BgKh57i18Ml6AI0emwxZ47l-ap_1F6sp1PXHObPVPj1SIUC9vmZ29RGAqvg0SXTANh6JeE-OfdPzo0ryrEkQdlf-ir_dTgWosI2v-tB3S1E63P80rNL_K2LgrPxbsZCRgcns65OmZmiArE27hgGHMeWQRBL-SjrqT8482p6RfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولت ترامپ در حال تشویق امارات برای تصرف یکی از جزایر ایران
🔹
تلگراف در گزارش خود نوشت که مقامات دولت ترامپ، امارات متحده عربی را تشویق می‌کنند که نقش مستقیم‌تری در جنگ با ایران، از جمله با تصرف یکی از جزایر ایرانی در خلیج فارس ایفا کند.
🔹
امارات متحده عربی یکی از ستون‌های اصلی حملات آمریکا و رژیم صهیونیستی به ایران در جریان جنگ رمضان بوده است. این کشورک حاشیه خلیج فارس ضمن همکاری کامل با نیروهای مسلح آمریکا و رژیم صهیونیستی، دو بار نیز به طور مستقیم حملاتی را به ایران انجام داده است.
🔹
طبق گزارش تلگراف، یک مقام ارشد سابق امنیتی دولت ترامپ گفته است که برخی از افراد نزدیک به ترامپ پیشنهاد داده‌اند امارات باید جزیره لاوان را — که در اوایل آوریل هدف حملات پنهان امارات قرار گرفته بود — تصرف کند و به جای آنکه نیروهای آمریکایی این جزیره را در اختیار بگیرند، نیروهای اماراتی آن را به تصرف خود در آورند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/652553" target="_blank">📅 19:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652552">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شبکهٔ ۱۴ اسرائیل از شنیده‌شدن ۲ انفجار در الجلیل غربی خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/652552" target="_blank">📅 19:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652551">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_057i3Cs0MjDFXk-dqlIM_HN8PoOs79ySJ-CieMLdiDoKUjquCQ7lHVKOZGGYVzXzKQTHnrcnJU1RjjC6hGni3U1BROveOAx9ajjx5ggnvyRnBsIMfi7V95WagBLSMlQBoQoT7fiOlbrgTFp1aD-MzPMSk6V0pXvVEwynLdCL7wgAKcotBMA7mU4Wl5eUu1-tdG8IfRINP8v83GGO8vUj-xlqtFJ1nT1L1bZDWNMFipwl9JOMmWp4rrfhTIrsssDZgNzqMetSh_hFqPyQizM-f_wxmVr9OshEg0hfVKFXZ_Law7jClz4NU_pB0esnb3FDO8KMj1nYiZ2SrgMUXMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان ملل به نامه نسل زدی‌های ایران پاسخ داد
🔹
دفتر امور جوانان سازمان ملل متحد به نامه ۳۰۰ هزار نسل زدی ایرانی محکومیت حملات ایالات متحده و رژیم صهیونیستی پاسخ داد؛
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/akhbarefori/652551" target="_blank">📅 19:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652550">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
۲۵ درصد ایرانی‌ها فشارخون دارند
🔹
معاون بهداشت دانشگاه علوم پزشکی تهران: آمار و ارقام نشان می‌دهد که ۲۵ درصد جامعه فشار خون دارد و همچنین ۱۱ درصد مردم و ۱۴ درصد افراد بالای ۳۰ سال به دیابت مبتلا هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/652550" target="_blank">📅 19:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652549">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bhz0gk2UZHILyrj9U2b5vRmxjssKrmxqJJTKK86-A4EyZFN31cJQpocMwPsCbYpwJPcvp7ZddIOYKjFDxKST0_ogKoLvzqzy_I0x23_d9OTVcrGWeDoce7SahfNSeZlfh3YMWQ9J8DDeT_6YJ6sL06eGR0-X_kzvx7EFLniorYNRiMumBvSWH6IRysDoVap2HIgW4kPb1T9ladOMSK8XImDYM_cJiimqamCqfX5YOAnCSk0h1a9o8hTIFqNuDnvGMD7Dmi_MRUB8ec1PLhCdNmW5eoE9QEwKGGLZggccBuNzFywGSIJXFnMcpnUFktp7qn-d5qPW1wHafRIoKNms9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهدی میرزایی فعال مجازی: ناهماهنگی بین نهاد های مسئول عامل اصلی انتشار اینترنت پرو برای افراد عادی!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/akhbarefori/652549" target="_blank">📅 19:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652548">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at_4ms9FoKvJ6ceWNWOUlfp0Dm1IymCxh1r4a4Mrjs-o4zzxzUrt-pW3hIwh1NeR7_aPH7vUWnx3ZjLsUm-CTCgS1UEXDuJjwsnxeOsxqI8z0KO7CCe9M-Yz-8H0rxpcRknKH2RWhzdFojHNm8YlljlXhZvajqLDWCJdX3oIAMFwIdwwJFKBrEzWcOOIcvfdjkuf5W_MinBkBceV1Z2iQ1oJ3wwd-bLqTHz1vb1V6bxQIAL749Dn8soVLLU65O5sZ4ZnjwYJCJJQ1hHX9iYyW2a-LhR9wzx2V8AkXp9UqAyN-dhwYQr_esshgLzJSZXExzEq8MsHQfD1ONMHH5Lezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصناف و اتحادیه ها تخلف میکنند، اپراتور ها توبیخ میشوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/652548" target="_blank">📅 19:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652547">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
بازآفرینی یک عملیات؛ نابودی پایگاه آمریکایی در کویت
🔹
این ویدئو لحظه‌ای را بازآفرینی می‌کند که خلبانان جنگنده ایرانی با نادیده گرفتن همه احتمالات و تنها با دو جت کوچک اف-۵، در حمله‌ای جسورانه و ماهرانه، یک پایگاه به شدت مستحکم آمریکایی را در کویت نابود می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/akhbarefori/652547" target="_blank">📅 18:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652546">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4ffc8c09c.mp4?token=vC0I2LwicMdJGDZE_eQWn-9dEIlcluzFH-85y90O2u29z2yhV22yyXnC0T4WrU2Hce_eAgdrpitwW3IlEM3TdvoqW6ix-2ZVPQwpz_Hw_y48qGlQ632ctJ8Nv35RRWyAB2_39wKhfwBmmg2r7OxQOcRS-yogK9Y9-MFnu_RIdC2J_FsjtoZIH5aaS8ivKAUBerdUMEEODSiBEO6a4RVKpHfRf9-_pYCEOe5HRj2pgNLE1StYeOJiB-croU10GYHiHkwPS6kR-VkpOd3Aghbu_ePdnEQ0HKiiC5vqYJCGT8zX5XFJdtqyFHn9F07GQehZ-aznE864VwPdX5DfXgQzxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4ffc8c09c.mp4?token=vC0I2LwicMdJGDZE_eQWn-9dEIlcluzFH-85y90O2u29z2yhV22yyXnC0T4WrU2Hce_eAgdrpitwW3IlEM3TdvoqW6ix-2ZVPQwpz_Hw_y48qGlQ632ctJ8Nv35RRWyAB2_39wKhfwBmmg2r7OxQOcRS-yogK9Y9-MFnu_RIdC2J_FsjtoZIH5aaS8ivKAUBerdUMEEODSiBEO6a4RVKpHfRf9-_pYCEOe5HRj2pgNLE1StYeOJiB-croU10GYHiHkwPS6kR-VkpOd3Aghbu_ePdnEQ0HKiiC5vqYJCGT8zX5XFJdtqyFHn9F07GQehZ-aznE864VwPdX5DfXgQzxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما عزادار دل خون جوادیم همه
با دل خون شده مجنون جوادیم همه
عرش را غربت او یکسره غمناک کند
رخت مشکی به تن پهنه افلاک کند
🔹
شهادت امام جواد(ع) تسلیت باد
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/akhbarefori/652546" target="_blank">📅 18:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652545">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اعتراف تکان‌دهنده مراکز فکری آمریکا در جنگ با ایران
🔹
اندیشکده‌های آمریکایی از یک غافلگیری بزرگ در این کشور خبر می‌دهند. غافلگیری که محاسبات را به هم زده است.
🔹
در اتاق فکرهای آمریکا درباره ایران چه می‌گویند؟
در این ویدئو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/akhbarefori/652545" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652544">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5nwijxR0Nh9Tx1OtlvjOs5Z-pGgDdhq0jXTAl38kCIaQ0cTn6PlsH1KOjXf7aJ7oZ7agNh0AZnlNrXyUjTxLIwTgWPHZwVPq9qMY4gfSwFTqlU7Kf12cEiTtzMQvWXWh2wii_U5AIdK0wdUqhAYs5lGJnR3Um0Fe3NPPWG49mzmq3XTHQsIFHNtyusnLwSEx6xDKB__CNRCkG5CiYATHzHEqTBcVEPnR-4wXyBUeYOu7WjEdKdh2bZ-M9DkiUem8khWa5uX2tNrFxk1g_aMqPB9TTBhkShDpZvOEULr8ZPVA6RMLtaEO98WEGo-rNam-ai6oU0bLZHJuiqkTM_-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن پالیسی: جنگ یک جرم بین‌المللی است، اما چرا بدون مجازات باقی می‌ماند؟
🔹
دولت ترامپ با انجام حملات هوایی علیه هشت کشور تنها در یک سال، اعتنایی به اصول منشور ملل متحد یا هنجارهای بین‌المللی نمی‌کند. ترامپ حتی صراحتاً ادعا کرده نیازی به حقوق بین‌الملل ندارد.
🔹
او گفته است که گرینلند را به هر طریقی به دست خواهد آورد، کنترل سیاسی ونزوئلا را در دست خواهد گرفت و همچنین تهدید به نابودی کامل تمدن ایران کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/akhbarefori/652544" target="_blank">📅 18:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652543">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
کپیتال اکونومیست: درگیری طولانی با ایران، قیمت نفت را به ۱۵۰ دلار خواهد رساند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/652543" target="_blank">📅 18:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652542">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
صدور دستور توقیف اموال ۱۲۹ عامل دشمن در آذربایجان‌غربی
🔹
رئیس دادگستری آذربایجان‌غربی: دستور توقیف اموال ۱۲۹ نفر از عوامل دشمن به‌دلیل اقدامات ضدامنیتی و همکاری با کشورهای متخاصم صادر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/akhbarefori/652542" target="_blank">📅 18:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652541">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK04OukWJo6rN7YxTaXerEqIvky__aS7sMCNOYRgWIjmlUn7Hr_RArW3M8WUo5vD3ZUqZAvhDWp4e4DJbgz9JBMBpw_ciI8uXeFDudMVt-2MdqC3uFn7zxa9BpaJLiHW5A8CIspNJ87l5SGVq8fSwwkyj_IbgaZwMdWzIdCgvDJYblUsfoOBE7M3g5BL5CibrCjqcQC1XTouIBPog7AIXFPA_B9FLvAoh-bgH5kMvLG3UsOP7h2NOqDEP7k5PiIroY7okX3HvsJgfW0nJK5a6F5V06oH_u3H55A9-tkPJplyu16ULQq6YPGtO9TiXXTuStV_J4awWvx99_2JwE3X_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: کنگره مهلت مهار ترامپ در جنگ ایران را از دست داد
🔹
به تحلیل روزنامه آمریکایی نیویورک تایمز، جمهوری‌خواهان کنگره فرصت حیاتی را برای ایفای نقش در خصوص عملیات نظامی آمریکا در ایران از دست داده‌اند و این قانونگذاران که ماه‌ها اختیار جنگ را به ترامپ سپرده بودند، حالا به‌خاطر همان کوتاهی، دیگر نمی‌توانند در برابر تلاش‌های دولت او برای دور زدن نظارت کنگره یا گرفتن مجوز از آن کاری انجام دهند.
🔹
از زمانی که ترامپ جنگ علیه ایران را آغاز کرد، جمهوری‌خواهان همواره تلاش‌های دموکرات‌ها برای توقف درگیری‌ها و وادار کردن رئیس‌جمهور آمریکا به کسب مجوز از کنگره را مسدود کرده و استدلال کرده‌اند که چنین اقدامی ترامپ را در جنگ تضعیف می‌کند.
🔹
با افزایش تردید در میان برخی قانون‌گذاران جمهوری‌خواه درباره جنگ در هفته‌های اخیر، آن‌ها بررسی مجوزی را مدنظر قرار داده‌اند که اهداف و معیارهای محدودی برای خروج نهایی تعیین کند، اما پنجره ۳۰ روزه پس از آغاز جنگ برای بررسی سریع چنین لایحه‌ای دیگر بسته شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/akhbarefori/652541" target="_blank">📅 18:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652540">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3NQBZDdvFSrDeyNW6g7LaJ5yTHiy_dSlDfaaoCF2ThR1gXAUclVprlTuWjyBZEUTRV2N6vwK3QelfJoi4BAqVgwrp016UdOhM7ZVqr3I1gkYJ0x0l8EoNZXPaDv7Z4OK-mLz-a9r2eHCGf2w1LjhnUGoDceDQpaf_8KJM2YrMyLjoExjyFr5D2X8MwesW4-3NI3RmWqguoVXD66PgepZKWgmu8DqhMDDWMCPgdUtKUDwEBOVdV-RCG0iM_5PbtXKLlIfa3-m2KXig6tjnkIe8lXP8Dpdaqrzr290WkwPdEg6x0X6AfY-jyQfhYWS0vaNd1aHEzkM685K28-IXP43Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار بسیج؛ سرلشکر شهید غلامرضا سلیمانی، معمار تحول و مردمی‌سازی
🔹
سردار سرلشکر غلامرضا سلیمانی، رئیس سازمان بسیج مستضعفین بود که از سال‌های دفاع مقدس تا عرصه محرومیت‌زدایی و فناوری، حضوری ماندگار در ساختار انقلابی ایران داشت.
🔹
این سردار سرافراز در ۲۶ اسفند…</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/652540" target="_blank">📅 18:01 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
