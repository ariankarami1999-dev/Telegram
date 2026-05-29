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
<img src="https://cdn4.telesco.pe/file/aibW0XWmIedKeK7QSHF5vDgrC57olmi-GKin54nZBnT1VkfmwB56OZYuM5CJcSBwX-YSbtFUFxvayF-TenjiFRiYBZFsibEQh1Kf3cfat9D7nInFNB6Jx4Bl8HXB7xm7ghmv_NPrba_9kdMg88RDWlcVjFItAtsvqInLCNLgJ1TUsq9fIoKYeiDpRNYwfgFMpfSp_Ec_JytvfbZZJSK6ZLHpYfBF0gDmJfmrbPZvuz8J_Wb_LoEhdBFG4Siu2j1039MR6wAgmz-Ls8EXMr3iUHbYGn007fCm2XVGXX0TIIL1TYUgwbv2OaayTQL1JnmgCeLq9eNzxpAVhJol5roM6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 914K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 01:16:06</div>
<hr>

<div class="tg-post" id="msg-123589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN9fngDrhm8MPw-omzRrOH3xe-gl88gPlkRNr3JliMafGonXN1SROjEAdLfB050GUam4L8VtgDU5XudLX9nED_PVJYgEfPP2ZR0DkT6oEXaisDFQ1zzZQsI4s39r70_1uB2fE14BAlSYE7fi4ZHeeaAzsFwxWoKp4I5mPgex4qTOPfZrSMhomqWAd__sKZZ-bTPF8zvpkQf8_kYIzH9hZfbD0AzqdkrFV8OEl91dbhHrVKUP8grmHdn0LqnHUo9PbTcT-3ZCM5iuksYLdqrxVflQK8qrEfwI1q0825jaB3PMNkhtaXn_UpqFY8Q8dvG3-ILBWjBtcMvbd3l1alTIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت مردم ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/123589" target="_blank">📅 01:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYXZ_0lktkx_0nSWCoZyWliX2kp0S2Vvnsh4Mw4-yhug91AiryinGG4sjBvf_4vA3KKbc4iLDf9vcN5xvRjNH1WAtZIyQjC5AD32x8tiEG5CQ9kAs1dVd2_LoovlAEJG6KhlgKWKuYtv4IUojnRa7pJWxql-tMomsd9icTgTfgsfXvZx_RdCPy9e6cubpnPZWFL-GAyBJC32UuSJlyYB82hawRbpLtFktkUUfnTP1evu8XMdViuPL4YCptLBtN-MW5-EhkTaIRoGltKePN1XamzuAYKwxSRCss8Unvylb1rlXwuyc_wqSi80RsriIlxx4MkZ2Ej_JSlvVjsaieX19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فردی که در تصویر می‌بینید به گزارش روزنامه فایننشیال تایمز مالک شبکه ایران اینترنشنال است!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/123588" target="_blank">📅 01:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezRjtopcbI10z4mmKxvaiIzmmfxXUEOV_HJ8ueRC72CU0GIEyvcNf_nPeloTF70hqWPkdEFaogFUjeMn_8Pm0ZTUI1UwZnOIcDta7KlCvET2pA1ttynhJbQJlEWA_x5LdVRHQLMw7QgJ5GNiQO6n9oHlTlyVc2j8Iw49YHpw_flxTs2GiSGGWGQ0BSx745ufA1BDHk91FHnantiztUED9soR0VshB7fYOpekHp2Q9m9114wserxD0y2n6-BD-FkJuk0WkivR4NMzU25la3ukxogM_XmDJFnIBmJYZTUIoD3-P0N3v0CeweK06COzMXSeG57XMkamBcuJltFSSiI41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره:
یک منبع رسمی ایرانی همین الان به من گفت: با تیمی که هیچ چارچوب حرفه‌ای یا اخلاقی ثابتی ندارد، دمدمی مزاج است و مدام خواسته‌هایش را تغییر می‌دهد، نمی‌توان گفت که هیچ چیز «نهایی» شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/123587" target="_blank">📅 00:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مدیرعامل جی‌پی‌مورگان:
داشتن سلاح هسته‌ای توسط ایران، میتواند بزرگ‌ترین تهدیدی باشد که بشریت در طول تاریخ با آن مواجه شده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/123586" target="_blank">📅 00:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123585">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نیویورک پست: ۶ میلیارد دلار از وجوه نگهداری شده در قطر از جمله آخرین نکات مبهم در توافق صلح با ایران است
🔴
این وجوه مستقیماً به ایران منتقل نخواهد شد، بلکه برای خرید مواد غذایی و لوازم پزشکی استفاده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/123585" target="_blank">📅 00:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9Xk2FpO4rdWp-ebRZi44dFQd3i2lkmFlpqwi5iz4wPr2jQHDQ0cPwm3QX9f8FSSvkCAx8esU7HvnecOxFSCP-nBDVUsNjE_H2uAhBTSKozwqIs8OoPH2-_ugmLS7-Fd6zMfiSM6NuJJlqxpp0tC4uZPUZHaVdXvAQt-WZ1W6-B8haBi5xevXDTYc7ryifLNYhOr4bMAZJNe_cAeQoxn1uxTnejJ_G15Zg4ZExjtNn5SM7ptq9V7LRssmfGsONOPea_B0tI9F6DQ_4xkv82EPYBKPQe9DPVduxmOJP4zJGwjt3RwSiz215yGIlHlT79MIahS7hRMt_rmSJcLlu9Yxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از داماد ۱۷ ساله و عروس ۱۶ ساله در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/123584" target="_blank">📅 00:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0NhTSxTOpXRd8G2Kh_duGsxMBUdLueL6vhaMExmUsp-G2tk9kEyp1y8rchhVIyL2cPxkp-jMghnjGhbIzLSNpWlyRrb8hV7cayc0NkPKbm6q3I1VMSGndQlPjPdCXv6b6uTvXg0sVz20r--AsJ4nsyxDRimSOTpXVB3f0RVDbCftFFD_vsY37gZ5-04Ps1QW21kk8CQFE9tAxIK6YCFWwDvnmi36sF2KkmwAXz5JI_-PfO7TCrvSIyr1g4OAKTrduML9-yPlMFooz02-ODD7-B_inIgsZgpQIgbTtlzbb_tlR1uFMZb5ZXpz_cal33mOt6v1v3_Pq0VtqpjuoNA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: آمریکا تاب‌ مقاومت جلوی قدرت ما رو نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/123583" target="_blank">📅 00:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123582">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2jLDpotnFwuUZoogU1c_fwxcGdm0IW46IDGzUWt2vVflNG93PjcQsc-ZgmJbQpNnJlz0_GiOOBS6FK4odBS32U9KuPFOJ79tbJbN3FIQcXnmps2mqOnpv76ZG4ny9cq2kibtS3L4rKcHHHqFQ9fFHtiAL1miARsz4aEnxu6kSQFtRBJ4ziCCucvnY3yEch6HEw_r1nZkXeTGwC5E7HHceEHc_64eDasInP9POYlJRGmuDQ77EAU9OTxrUlFTkC3orHM4pRVppjFwgM47qzQF_4VS-Tnr60OUgwv52wlL5o5H8KDRttzWiCCNZ6BWPen5Tl9oUFIlnMy3Iu_vi4BSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فردی که در تصویر می‌بینید به گزارش روزنامه فایننشیال تایمز مالک شبکه ایران اینترنشنال است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123582" target="_blank">📅 00:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123581">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/وزیر خزانه داری آمریکا درباره رفع تحریم‌های ایران
🔴
به گزارش الجزیره،  وزیر خزانه‌داری آمریکا مدعی شد که تحریم‌های ایران به تدریج لغو خواهد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123581" target="_blank">📅 23:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123580">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: محاصره اعمال‌شده بر بنادر ایران به‌تدریج برداشته خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123580" target="_blank">📅 23:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8beb1cabba.mp4?token=qBB3aRu_BJej3zi5Vtpk9ovKx63TBAYOsQ1ipnyVHzRE_c7Tuf2EY3WOOXW91BhrYhtXYgxkkUePcOnnY0t_24h3mMxKKjZTILVnmILQSDzIefx-g2WJWbwtJYj_V-QwighaWT_U0Pv-5OfPzIf2SgIxLoz9kbceluMdNY7lp4K5_V4jmU_tlPbQd3N2bYlac5vSZpAhB1yxb2GhHmmxR2CjAedVrWnX2wQvlyMg2Z94oF1VPfL50-5sqho2Qk2GRnNxGQAS1OFN0hdiwITo5Pb4lD5l3C-rcHEW8GpWUzFqhK3Fi1QuHERIP1GY5o84h4kl33NIFeXaU4E1IfSkWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8beb1cabba.mp4?token=qBB3aRu_BJej3zi5Vtpk9ovKx63TBAYOsQ1ipnyVHzRE_c7Tuf2EY3WOOXW91BhrYhtXYgxkkUePcOnnY0t_24h3mMxKKjZTILVnmILQSDzIefx-g2WJWbwtJYj_V-QwighaWT_U0Pv-5OfPzIf2SgIxLoz9kbceluMdNY7lp4K5_V4jmU_tlPbQd3N2bYlac5vSZpAhB1yxb2GhHmmxR2CjAedVrWnX2wQvlyMg2Z94oF1VPfL50-5sqho2Qk2GRnNxGQAS1OFN0hdiwITo5Pb4lD5l3C-rcHEW8GpWUzFqhK3Fi1QuHERIP1GY5o84h4kl33NIFeXaU4E1IfSkWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین علایی:
سه روز قبل از جنگ ۴۰ روزه به شمخانی گفتم: آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می کنند؛ او گفت: نمی‌توانند! گفتم چرا نمی توانند. گفت نمی توانند پیداش کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123579" target="_blank">📅 23:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123578">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz7brSAkMMurV62sSX6HCS5Hr_GPrKfno9BPcl4Gsv-_Y100bm4nWYQLf01nH3Xq7FHjQ8HMMGwKijEh4bvvYrLUsXAUeZAw5z7-Au0dNFKMyKZfD0Lf7qZn2-GS7L-pQwrwInKR2oFtxWUV2LWuwUog6l0Xrv7tVOkrauiX0y7rZVAHeOJ3ZT6Pr-0AG0UqViTvimSa0kceH8MhGH9t9FASOu0PVZz2vIeeI5vUvOQhIMhexquSbhbpmURPCcdarRjh-3CxGkJeK72q1zhFWM4xQPJaV2ZH3gw3yE71g_sL0EKUCQ02sHuNwPEF6eznXtGZWS-q7h7utrlPpSQ1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123578" target="_blank">📅 23:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123577">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1defb8b924.mp4?token=ejNp-cEY-_Dl4JYe_gyaRDmWExkevnNd9JyGPZxpO6TfIEzyTt0azKbCIChKEBA7h2xXwK90-dgjzE93-J_BJVEufWmjOo6aotx4zssVCeytoYaMhN-7ozg0Vo7Wcz-ZHtjffJIRZU1bxQzhxtEPOnDHWUlmuN9NOi_JQf14jZ4x5OHDscGhGskVBnQz8bwUVL8mgU7AVFlbwbk25PU3SDF2qXHznoZrwACrJk6kSQuvG5gwEfHoFvBSTXkGQiEyreo-2Ec6qJcBEwi58ZKGsTY5kCbWmwq9c--OBddfnD0JeqBmyH6_XMtFWOlzKQMne9D3QF0gkFIC7sBIgiW4l1BoIKmWc1YDJmrdD-AMPBoWMvN08LbGNso8T3WtJdVrwc5fMu7M3gkRgAk7aoES_QsFGtrIuLDF8Y4wcv6iUL_rtY7hDQxWrvR7ZB-ussPbFD2gvAojO4ptDUT8gEbWrHSd9295ogALns_0CRH0zn0iEev9cRhXv395Ob2sHOfiIUNpJk-mMlA8ckjndKIDhsAE9754pZ6ME_LjjQjvzo7jNAbRx8V4BtD_XUn8N4HJoErFj_AoKmqEXb_fq7kqOhgx8OwvVW7Hr4oo6fzcfGo_dznCgzsD-tdHK5ArNzJhGR0myBtGSiESlEPrdst7gWqsTxOxvHmZeQui_yYIQbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1defb8b924.mp4?token=ejNp-cEY-_Dl4JYe_gyaRDmWExkevnNd9JyGPZxpO6TfIEzyTt0azKbCIChKEBA7h2xXwK90-dgjzE93-J_BJVEufWmjOo6aotx4zssVCeytoYaMhN-7ozg0Vo7Wcz-ZHtjffJIRZU1bxQzhxtEPOnDHWUlmuN9NOi_JQf14jZ4x5OHDscGhGskVBnQz8bwUVL8mgU7AVFlbwbk25PU3SDF2qXHznoZrwACrJk6kSQuvG5gwEfHoFvBSTXkGQiEyreo-2Ec6qJcBEwi58ZKGsTY5kCbWmwq9c--OBddfnD0JeqBmyH6_XMtFWOlzKQMne9D3QF0gkFIC7sBIgiW4l1BoIKmWc1YDJmrdD-AMPBoWMvN08LbGNso8T3WtJdVrwc5fMu7M3gkRgAk7aoES_QsFGtrIuLDF8Y4wcv6iUL_rtY7hDQxWrvR7ZB-ussPbFD2gvAojO4ptDUT8gEbWrHSd9295ogALns_0CRH0zn0iEev9cRhXv395Ob2sHOfiIUNpJk-mMlA8ckjndKIDhsAE9754pZ6ME_LjjQjvzo7jNAbRx8V4BtD_XUn8N4HJoErFj_AoKmqEXb_fq7kqOhgx8OwvVW7Hr4oo6fzcfGo_dznCgzsD-tdHK5ArNzJhGR0myBtGSiESlEPrdst7gWqsTxOxvHmZeQui_yYIQbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین ماشین حاشیه ساز لکسوس Lx700H با قیمت ۱۱۰ میلیارد تومانی پلاک ملی شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123577" target="_blank">📅 23:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123576">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0acce2b1.mp4?token=fjDnArTVrUcZ1BbU0eR4UTp5sNzL7a4jtbbjRteBbOgY4ooelx_1u7kqrRqNofCpYK1ygXfHv8K9Wnj1iEDtcSGYUjSttdSxD2P7Nm5id6Ett0Sjp8xjzftms18L9wKtZYOWp_HoLblNCWaobfjzhm5XuJdCfSHtxVHFDkNq9284pdtUHCxyQW58v4VyQdRnvu6cDh8eBcLz3FdMaa7QU4JX2oJkXessw7OqezRceAkFnhDEePIXGMz9_BqwAcAxcmr5kei36WSakVqPn5Q5P9iFWDU18F2jL8fDUE8_LSp9fTp1ovfxcVuFcC5YcAPR4iNlq6JtXS8riVdugbatyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0acce2b1.mp4?token=fjDnArTVrUcZ1BbU0eR4UTp5sNzL7a4jtbbjRteBbOgY4ooelx_1u7kqrRqNofCpYK1ygXfHv8K9Wnj1iEDtcSGYUjSttdSxD2P7Nm5id6Ett0Sjp8xjzftms18L9wKtZYOWp_HoLblNCWaobfjzhm5XuJdCfSHtxVHFDkNq9284pdtUHCxyQW58v4VyQdRnvu6cDh8eBcLz3FdMaa7QU4JX2oJkXessw7OqezRceAkFnhDEePIXGMz9_BqwAcAxcmr5kei36WSakVqPn5Q5P9iFWDU18F2jL8fDUE8_LSp9fTp1ovfxcVuFcC5YcAPR4iNlq6JtXS8riVdugbatyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رضا پهلوی: کشور های جهانی به خاطر چشم‌های زیبای من یا شما این کار را نمی‌کنند، آنها این کار را انجام می‌دهند چون به نفع منافع شان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/123576" target="_blank">📅 23:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123575">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: هرگونه گمانه‌زنی درباره پیوستن پاکستان به طرح سازش [پیمان ابراهیم] با اسرائیل را قویا رد می‌کنیم
🔴
تا زمانی که سرزمین فلسطین مطابق مرزهای قبل از ۱۹۶۷ به پایتختی قدس شریف به رسمیت شناخته نشود، هیچ انعطاف‌پذیری در موضع ما وجود نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123575" target="_blank">📅 23:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123574">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: یک میلیارد دلار از دارایی‌های رمزارز ایران را مصادره کردیم!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/123574" target="_blank">📅 23:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123573">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/وزیر خزانه داری آمریکا درباره رفع تحریم‌های ایران
🔴
به گزارش الجزیره،  وزیر خزانه‌داری آمریکا مدعی شد که تحریم‌های ایران به تدریج لغو خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/123573" target="_blank">📅 23:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123572">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfAonbBqiu0b7h1DcL3PNKmAEcB88qfCf6ZNstPk7BQx7d25uKiyJYGohLIs-YvpaceVBIctnlQsuAJVzsNkaX1uzc1zi51_CYFL5chvpQHDIGq5L5IyBxuCVVeN-5MkEItm8RUJ2eyFVK4WXsyjVq7UzcFoO2xyaef6yO-3FUI7bUGG7wJWguoKYwyLim60iJfmRPGNFjp7Ab9xao5u4Irt8k08sszAos-DfQOhbSRW05E3JBae2f1TsPMcjgrvM0kqGAliy1IQuhhAbjfTGe2tyHGju9G7EXt-Zjkygc2KpHfhjSKkpHdQJFKifIgk0LJ1oL7DKg-cIF0HuZrMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز اعلام کرد: صادرات نفت و فرآورده‌های نفتی ایران تداوم دارد و امروز یک ابرنفتکش دو میلیون بشکه نفت خام ایران را بارگیری کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/123572" target="_blank">📅 23:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123571">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: یک میلیارد دلار از دارایی‌های رمزارز ایران را مصادره کردیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/123571" target="_blank">📅 23:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123570">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
کان اسرائیل: نتانیاهو خواستار از سرگیری حملات به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/123570" target="_blank">📅 23:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123569">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بسنت وزیر خزانه داری آمریکا:  احتمالاً تورم ایران بیش از ۲۰۰٪ است.
🔴
ما فکر می‌کنیم ایران ماهانه ۴۰۰ تا ۵۰۰ میلیون دلار سرقت می‌کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/123569" target="_blank">📅 22:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123568">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT9xwaaoDCC0agxBrCdQtGzLHY4YfEpOP00IqhUKw5ODgK-xv8-wKv-X34wpnvNztYDFp_f74MmlZ4-zGTXIOOT2HsrVX8NLFEUxUnYGm1RFxtXxWiqlIpOIWK3fZVi2vzL49ONv7QIawZinCdj14-vm75Q1bL2bP0Dnjm5DSVBvxS_DdNVFHzQRvFQhXECrPzHz5aDFvwZ6Xh0NFQsfYfOaw_lvYGPERq9A_wby0-d6vN8P1OCeXpq3q05uwq0S_BBigei8Sqf0QIDlx8KQteMjU1MhKgsHKugtwfNmyCx1ASN566ay0mWuOyWvJ-b_lJGuqlMIC7ROOBghpyKftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنتاگون در حال جذب صدها عضو نیروهای مسلح برای حضور در رویداد UFC برنامه‌ریزی‌شده توسط رئیس‌جمهور ترامپ در کاخ سفید در ۱۴ ژوئن است، گزارش واشنگتن پست.
🔴
بر اساس یادداشت‌های داخلی که واشنگتن پست بررسی کرده است، نیروهای انتخاب‌شده برای حضور به عنوان تماشاگر با یونیفرم باید هزینه‌های سفر و اقامت خود را بپردازند، استانداردهای فعلی آمادگی جسمانی نظامی — از جمله الزامات قد به کمر — را رعایت کنند و یونیفرم رسمی بپوشند.
🔴
مقامات به دنبال جذب پرسنل درجه‌دار جوان و افسران جوان برای حضور هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/123568" target="_blank">📅 22:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123567">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام دولتی:
نشست ترامپ در اتاق عملیات حدود دو ساعت به طول انجامید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/123567" target="_blank">📅 22:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123566">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A31axNnlkyW34sF1OSSQFpBHsMeTKB_dyDJfuBx-jwvlme3o9szc0_yOD2ed9amya06-bFc8nhlDYQHaeKKmc1MxZGHO4TcmERUiBu9Zd1NIPkMDwPB9skOqmeaKlcsGaWv0X-6yN4jaTmFX5vBdFYNu3GaHfUBKAKVqmKplaR-lLhSScseSoXXRrdhiijY9EN9nS3_UwQrrnjbM_rI0BJ2bMCNLiqCCzPEtbxpzwkFRD2HksjKia07HBjDpiIg6wdAqWchVdOgA7s5j0Sw71TwASATF65aJW0wMyCu73YC46poYEkjarE266s01zae8P8-0-jZVeParx1RdR3wbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/123566" target="_blank">📅 22:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123565">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام دولت ترامپ: ما به دستیابی به توافق نزدیک شده‌ایم، اما برخی از مسائل همچنان مورد بحث هستند.
🔴
نیویورک تایمز به نقل از یک مقام دولت ترامپ: موضوع دارایی‌های مسدود شده ایران همچنان مانعی در مذاکرات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/123565" target="_blank">📅 22:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123564">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزارت خارجه پاکستان اعلام کرد که وزیر خارجه این کشور در دیدار با روبیو، وزیر خارجه امریکا ابراز اطمینان کرده است که تلاشهای تحقق صلح منجر به نتایج مثبت خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/123564" target="_blank">📅 22:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123563">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
خبرنگار الحدث:  نشست ترامپ در اتاق عملیات کاخ سفید درباره تصمیم‌گیری در مورد ایران به پایان رسید.
🔴
باید منتظر تصمیم ترامپ و اعلامش باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/123563" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123562">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDRh4clKS32bjzQpsAMkMp8qE3gJY-L3M-IKQtYsgXP29adQRrPxscwtZGERp8n3Ofq_PUJCotQjZTcGN8E4YptoHlnhL8G49xaEIBfD0w_j7XmnID_zVfQk83dPyKtza1xXKPMiUuxYYzef91hNWdqr8IT1l-g22PqGR-k_TDtwDqNKnYFqUrVZuf3md-EN4RE98QjP9rSlpvg1hu3CuwfjozxRXz56FvI597CmSvOrAmXg8zmwJmga9LkA4Itr42Swp841_LjJnLmj6WpenMm2vbniZY8nXJ1DpXOVvbdrHi27MZLWw7GUvayKtzBk9EG_VCPXeWyrGra9Vn75Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای پهپاد در منطقه خط تقابل، شمال اسرائیل فعال هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/123562" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123561">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p74E_n0KpMAcgoOo776m8iSn86IieYOOq3-pb8BR2WffCc5IJ2hCv9KngAL-Z890DSF3Ef7scn2I2evBOt4YtrhIgkfECK56Y_xG0M4KAWII_Q6ZofCfXnKkPoAJJ6mdSWtnILVJ_cIkb1c3ehVRozv1PpTevrF0bpcC3qWAYCnj4ofjU0JTHnRcpMTTc2j3n0yKR00rWqZT-AOTL7xf53-9Jrt5eMGplPMINBkP44mumreEpxFGNAwi-palz3z-HtsYKG0VfonSYS2jbQnvUIFnt2XfpXbBJFvNnIDXLFgnyEd9WLiS_GTBqC102BUnPPd4e0wwnuv1nQGUtb9csg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شش فروند هواپیمای ترابری نظامی Boeing C-17A Globemaster III نیروی هوایی ایالات متحده در راه خاورمیانه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/123561" target="_blank">📅 22:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123560">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری / فاکس نیوز: خبرهای مهمی از نشست ترامپ در کاخ سفید بیرون خواهد آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/123560" target="_blank">📅 22:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123559">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
شبکه تلویزیونی اسرائیل به نقل از یک منبع گزارش داد: هیئت اسرائیلی در مذاکرات پنتاگون پیشنهاد لبنان برای خروج از لبنان را رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/123559" target="_blank">📅 22:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123558">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ارتش ایران : یه پهپاد دشمن رو سرنگون کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/123558" target="_blank">📅 22:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123556">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
خبرگزاری صداوسیما: ترامپ ضرورت خروج آمریکا از اطراف ایران را نادیده گرفته درحالیکه این موضوع مورد تاکید قطعی ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/123556" target="_blank">📅 21:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123555">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158dd2ae98.mp4?token=iWvAd5mDpD56K7hQotx-U6pVGFSiEQj2w_3DLLEnrD5-yUgMthU0y8mHYWN7QD2c0lBNELSXvfT9eDD_dQqRYAbQwpDkASpn6k5Kmqipl_Er9ioFc5t9j26PHTubu8xkZVKS629l5VMBpL1AukvENa_N-va6wS9jUd8o2xuElBPVScmIt9_N2yjOMNLjObBTa55VhtImCORz5TmVLJf1l5s0ssi95bih8AEq_cSqshMAMPGShPTqHnqIQaIUmYPuyHTAaETau09FVFBQMcQQDXWEVRcWRJEPJvpD-emr3EXkKZy9PGg_fwUQk0iH7RJmRcuINMv18MmFJeg7FjYAAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158dd2ae98.mp4?token=iWvAd5mDpD56K7hQotx-U6pVGFSiEQj2w_3DLLEnrD5-yUgMthU0y8mHYWN7QD2c0lBNELSXvfT9eDD_dQqRYAbQwpDkASpn6k5Kmqipl_Er9ioFc5t9j26PHTubu8xkZVKS629l5VMBpL1AukvENa_N-va6wS9jUd8o2xuElBPVScmIt9_N2yjOMNLjObBTa55VhtImCORz5TmVLJf1l5s0ssi95bih8AEq_cSqshMAMPGShPTqHnqIQaIUmYPuyHTAaETau09FVFBQMcQQDXWEVRcWRJEPJvpD-emr3EXkKZy9PGg_fwUQk0iH7RJmRcuINMv18MmFJeg7FjYAAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از جشن برداشتن محاصره دریایی در قشم و شلیک توپ ضد هوایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/123555" target="_blank">📅 21:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123554">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری / گزارش های تایید نشده از فعالیت پدافند در قشم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/123554" target="_blank">📅 21:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123553">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / گزارش های تایید نشده از فعالیت پدافند در قشم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/123553" target="_blank">📅 21:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123552">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqmnX8tRg73HOsdYUaPqj-sa1O1oi7ltuhHF2qIhh-Pj-PCqlNgnwOZuzfOdLbe84drnOCFHVE25tSoF2khj3VEqLjkbzFHO23HqzOpJ6SlWo08W8XIhipxh0ywQ6mqyleSTvueimvPpSHj9_zmyNd_nhgAgbzj4OsKSEa7kcTcIQsugu7ViMF6uD-Ba4Ft29RLui56FV_FNuj8ac3TLTlVgwLraytv3qcDdSF4aUUdBDADzfq4U23kaiyeI5IXuWuxSNIynRQua0XlTdBair0GNbTE-XuJgU_xCRa7BYfyOyqTPwjNhGqIELccTGn_1-1NSPHFZlY8Pb3IFNLWxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/123552" target="_blank">📅 21:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123551">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / گزارش های تایید نشده از فعالیت پدافند در قشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/123551" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123550">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
زلنسکی: روسیه در حال آماده‌سازی یک حمله بزرگ‌مقیاس جدید است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/123550" target="_blank">📅 21:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123549">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
جورج مالبرونو خبرنگار فیگارو: طبق گفته یک منبع عرب در تماس با میانجی پاکستانی، جرد کوشنر، داماد دونالد ترامپ، مانع از نهایی‌شدن توافق بین واشنگتن و تهران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/123549" target="_blank">📅 21:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123548">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گروسی، مدیر کل آژانس بین‌المللی انرژی اتمی : توافق ایران و آمریکا خبرِ خوبیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/123548" target="_blank">📅 21:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123547">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
اسماعیل بقایی : مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/123547" target="_blank">📅 21:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123546">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خبرگزاری صداوسیما: ایران هنوز متن ۱۴ بندی ادعایی رسانه‌ها را برای آمریکا ارسال نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/123546" target="_blank">📅 21:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123545">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
منابع خبری از خاتمه نشست ترامپ با همکارانش در کاخ سفید  در خصوص ایران خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/123545" target="_blank">📅 20:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123544">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: با «زبانِ باید»، ۴۷ سال پیش خداحافظی کردیم
🔴
هیچ یک از طرف‌های غربی که وقتی درباره ایران صحبت می کنند، نباید از باید استفاده کنند؛ ما بر اساس منافع ملت ایران تصمیم می گیریم.
🔴
بایدهایی که آمریکایی‌ها مطرح می‌کنند، در واقع خواهش می‌کنیم است؛ تبادل پیام‌ها ادامه دارد و تفاهم هنوز نهایی نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/123544" target="_blank">📅 20:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123543">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
یک مقام ایرانی به «رویترز»: عملا به تفاهم سیاسی با آمریکا دست‌یافتیم اما نیاز به نهایی‌شدن دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/123543" target="_blank">📅 20:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123542">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تاکنون تفاهمی با آمریکا نهایی نشده است
🔴
در این مرحله بر خاتمه جنگ متمرکز هستیم و درمورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم
🔴
بقایی درباره ادعایِ از بین بردن مواد هسته‌ای توسط ترامپ: در این مرحله تمرکز ما بر خاتمه جنگ است و درباره جزئیات غنی‌سازی و اورانیوم غنی‌شده، صحبتی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/123542" target="_blank">📅 20:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123541">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رضایی نماینده مجلس: مخالف تعلیق غنی سازی یا اعطای مواد هسته‌ای به اسرائیل و آمریکا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/123541" target="_blank">📅 20:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123540">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وال استریت ژورنال:
امارات متحده عربی ده‌ها حمله را با هماهنگی آمریکا و اسرائیل انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/123540" target="_blank">📅 20:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123539">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGws26NNF3nDpp0ZjOV3QC9Dzo_lV-uWNVfi5icOFPAzaI_qoU6gHu7dXTBW9koId4Tfk9x0aQWr0dEbfcRrOnnNrYLvHaYZ3yTWjzvvEURJ1F4Nl0rvKOLR09YWVJ1cDHjz5gFOiyLLQDQv6-RSCyAKF2s9s8KyHAH47gg7SL4pnOPOffxO_hvo_9pMLKah0yO4wsI9dIOOwTjxPDLMEvqQTDSXcjPtrW9zXYj2UnxVlosKKfe5RkgxH2M0rkd8XhVFuuwM5C6kSFvRyLUtX0KErn6JKQd3lQr2dLQgSYNQLJimQ9jxljBiPYfHXcLuFAbuNB9vGk-cpsRDIcUYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: افراد آشنا با این موضوع گفتند که امارات متحده عربی از روزهای اولیه جنگ ده‌ها حمله هوایی علیه ایران انجام داد که تا روز پس از اعلام آتش‌بس ادامه داشت، دخالتی عمیق‌تر از آنچه قبلاً در کمپین هوایی به رهبری ایالات متحده و اسرائیل شناخته شده بود.
🔴
گستردگی این حملات گواه دیگری بر تمایل روزافزون این کشور برای محافظت از آنچه منافع استراتژیک خود می‌داند، است و آن را از برخی از همسایگانش در منطقه خلیج فارس که رویکردی بسیار محتاطانه‌تر نسبت به تهدید ایران اتخاذ کرده‌اند، متمایز می‌کند.
🔴
این افراد گفتند که این حملات با هماهنگی ایالات متحده و اسرائیل انجام شده است که هر دو اطلاعات ارائه داده‌اند. برخی از این افراد گفتند که این حملات شامل اهدافی در جزایر قشم و ابوموسی در تنگه هرمز؛ بندرعباس، پالایشگاه نفت در جزیره لاوان در خلیج فارس و مجتمع پتروشیمی عسلویه بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/123539" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123538">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی پیشنهاد داد که قزاقستان اورانیوم غنی‌شده ایران را نگه‌داری کند
🔴
به گفته گروسی، قزاقستان آماده است در صورت حصول توافق بین آمریکا و ایران، ذخایر اورانیوم غنی‌شده ایران را نگه‌داری کند.
🔴
رافائل گروسی، رئیس آژانس بین‌لمللی انرژی اتمی، در گفتگو با فایننشال تایمز گفت که قاسم‑ژومارت توکایف، رئیس‌جمهور قزاقستان، این پیشنهاد را در دیداری که این هفته در آستانه داشتند، به او منتقل کرده است.
🔴
قزاقستان میزبان بانک بین‌المللی اورانیوم با غنای پایین است تا تأمین سوخت نیروگاه‌ها در کشورهای عضو آژانس بین‌المللی انرژی اتمی تضمین شود و از اشاعه هسته‌ای جلوگیری گردد.
🔴
گروسی گفت: «ما محلی داریم که این [اورانیوم غنی‌شده ایران] می‌تواند با خیال راحت در آن ذخیره شود»، پیشنهادی که به اعتقاد او هم ایران و هم آمریکا می‌توانند آن را بپذیرند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/123538" target="_blank">📅 20:16 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123537">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
تسنیم به نقل از منابع ایرانی: اصرار ترامپ بر عدم آزادسازی دارایی‌های مسدود شده، تردیدهای تهران را در مورد جدیت واشنگتن افزایش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/123537" target="_blank">📅 20:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123536">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پوتین : اوضاع توی میدون جنگ جوریه که روسیه می‌تونه بگه این درگیری داره کم‌کم به آخرش نزدیک می‌شه
🔴
حرف بعضی سیاستمدارهای اروپایی که می‌گن دارن خودشون رو برای جنگ با روسیه آماده می‌کنن، کاملاً چرته
🔴
روسیه هیچ‌وقت هیچ نیت تهاجمی علیه کشورهای اروپایی نداشته
🔴
روسیه برای مذاکرات درباره اوکراین آماده‌ست و از اون صرف‌نظر نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/123536" target="_blank">📅 20:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123535">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b181524b.mp4?token=hc6y-xgNz6IzXJWQXdxCEx35OiGZWKXgf_uEhIijxaRGzvmFvseLuN7B9mcgoH1qxPyg_ZgkvvhwLxZ1wa7cLELy3s2hKbkky-qjE5zu57xxG4qG5OPapO5e8Moh1gCJc2Pb74dVzfmkDkQSBWnQ6FfxXbC_EqQehNmyxMaW0jaB-yr3iMN7rUgfidBJyHlWrxhKzFf-wuKFUOJpdn_I87oTZvT5JWiwyLuOPyjxcuX_YThsLtV5bB0kYg0uYT56WIkAolbbZFSSOx1bzPIGTPezr5WgB07TXIqJmaG2i_zXsGe4oUFgFkbuwiZaD20x-S-RAQ6Xt4vrw0h69YJXLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b181524b.mp4?token=hc6y-xgNz6IzXJWQXdxCEx35OiGZWKXgf_uEhIijxaRGzvmFvseLuN7B9mcgoH1qxPyg_ZgkvvhwLxZ1wa7cLELy3s2hKbkky-qjE5zu57xxG4qG5OPapO5e8Moh1gCJc2Pb74dVzfmkDkQSBWnQ6FfxXbC_EqQehNmyxMaW0jaB-yr3iMN7rUgfidBJyHlWrxhKzFf-wuKFUOJpdn_I87oTZvT5JWiwyLuOPyjxcuX_YThsLtV5bB0kYg0uYT56WIkAolbbZFSSOx1bzPIGTPezr5WgB07TXIqJmaG2i_zXsGe4oUFgFkbuwiZaD20x-S-RAQ6Xt4vrw0h69YJXLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین، رئیس جمهور روسیه : ما باید سیستم دفاع هوایی رو تقویت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/123535" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123534">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL7sjDktGw6S4tp0J1OFNuIaTZDY_dGe8xb0bUnXsLxVwCeQ4bI7jT6Ipjsuh2Oz0MnxDftzFwpi7Aw5B4M-c68Tl4RS8-3eupRT49IHMcMcoJXPcFP74Tnff_f0acEeJfMvidttOPWQjcQSxl0jQUx-TRJS-GMT_qD70H4Xk-dxcuRo6llXtzxf6dRDBrqhOr4pcUlArDcuZido-QTMD2DqQJ1I0Ry8r5BIsVR5gdLgZUNgc0xJH9WFyVqKB209ipv2ltQim-Zru7seujNq9t35CX-HlHus_2ecGbmSMcT4XlgFqcCLpbmO9BEfl1hwnjMaA5ze3AioulqDAszhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123534" target="_blank">📅 19:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123533">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پوتین درباره حمله پهپادی در رومانی: هیچ‌کس نمی‌تواند منشاء پهپاد را قبل از بررسی لاشه آن ادعا کند.
🔴
به هر حال، ما می‌دانیم که پهپادهای اوکراینی به فنلاند، لهستان و جایی در کشورهای بالتیک پرواز کرده‌اند.
🔴
واکنش اولیه دقیقاً همان بود که اکنون در رومانی است…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123533" target="_blank">📅 19:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123532">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
علی هاشم خبرنگار الجزیره: یک منبع مطلع به من گفت که پست دونالد ترامپ در شبکه اجتماعی «تروث سوشال» درباره لغو محاصره بنادر ایران، در واقع اولین شرط پیش از برداشتن گام‌های بعدی در مسیر تفاهم بوده است.
🔴
به گفته این منبع، طرف ایرانی بر اعلام رسمی و عمومی این موضوع در وهله نخست پافشاری کرده است. به نظر می‌رسد ترامپ این موضوع را امری فرعی قلمداد کرده، در حالی که تهران آن را گامی کلیدی برای ایجاد اعتماد پیش از ورود به پرونده‌های حساستر می‌بیند.
🔴
تا کنون، هیچ بحث مستقیمی درباره خود پرونده هسته‌ای صورت نگرفته است. انتظار می‌رود این فرآیند به تدریج و از طریق یک یادداشت تفاهم (MOU) پیش برود، به گونه‌ای که هر گامی با یک اقدام متقابل همراه باشد.
🔴
همین منابع می‌گویند انتظار می‌رود اعلام آتش‌بس بین حزب‌الله و اسرائیل نیز به عنوان بخشی از چارچوب گسترده‌تری که در حال شکل‌گیری است، انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/123532" target="_blank">📅 19:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123531">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ناتو: اوایل صبح امروز، یک ساختمان آپارتمانی در رومانی توسط یک پهپاد روسی هدف قرار گرفت
🔴
ما بی‌مبالاتی روسیه را محکوم می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123531" target="_blank">📅 19:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123530">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
خبرگزاری فارس به نقل از مقامات ایرانی: این توافق به نحوی تدوین خواهد شد که در صورت نقض آن توسط آمریکا، امکان اقدامات متقابل فوری فراهم شود.
🔴
توافق نهایی بر اساس خطوط قرمز ایران و بی‌اعتمادی به آمریکا تدوین خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/123530" target="_blank">📅 19:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123529">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری / العربیه: «فایننشال تایمز»: قزاقستان پیشنهاد کرد که اورانیوم غنی‌شده ایران به این کشور انتقال داده شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123529" target="_blank">📅 19:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123528">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرگزاری فارس: مهم‌ترین بخش توافق، پرداخت فوری ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران و آتش‌بس کامل در لبنان است که ترامپ به آن اشاره‌ای نکرد.
🔴
طبق متن توافق، این مبلغ باید فوراً پرداخت شود و تا زمانی که این پرداخت انجام نشود، ایران وارد هیچ مرحله…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/123528" target="_blank">📅 19:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123527">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
خبرگزاری فارس: مهم‌ترین بخش توافق، پرداخت فوری ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران و آتش‌بس کامل در لبنان است که ترامپ به آن اشاره‌ای نکرد.
🔴
طبق متن توافق، این مبلغ باید فوراً پرداخت شود و تا زمانی که این پرداخت انجام نشود، ایران وارد هیچ مرحله مذاکره دیگری نخواهد شد.
🔴
تنها در صورت حل این مسائل، ایران در مرحله بعدی در مورد لغو همه تحریم‌ها و موضوع هسته‌ای، مطابق با خطوط قرمز خود، وارد مذاکره خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/123527" target="_blank">📅 19:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123526">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gilkL_M9cCarEJ4GFQwRe4oFlDqUoSl_9mjHzmYfO-6TodxDdFg93Mj1cAc0Lf_l44RVxoz8-swNeaQgW24f75vwaB_eiI6mGnBtrByYt7u9ukDoAdcf0xfKephEUj9jJd9zFde9ZOxXd8ADJlnOKmB40iP1TbG6ptrqvfrtUYRKqNgR09g_7CMOW3IS9DG0piL1Ue5X2HvcFwBt-sflMoswCV7iMYePMSRJMLh6SmaSKUbWq8ixvCmlxENCuKW2MvqR3v5ZgNjzXuFewNmdYywZg8f_QENH_Wv5CuOH-0_ggapteDgY2d9OpIsqYxTVevExgGMkxCAgJYFYb2Amkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
«آکسیوس به نقل از مقام‌های آمریکایی: ما از ایران درباره مواد هسته‌ای تعهدات شفاهی گرفته‌ایم و مهم‌ترین موضوع، آن چیزی است که در مذاکرات بر سرش توافق می‌شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/123526" target="_blank">📅 19:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123525">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeZICcLzL1ko9tJ8WudTa3-9mJlbcvA-h-8GKiCd9pQgs77Je8uZEz_xJKhNqes45ZQMKTKDpf-2JihZuhORpPeXIdN1LyIr6RRL_Bfj7vR2gXvdDaMauLEdj-3r0RLRlWTnhCwV0-YUIy_xLweJh9fyts73_YO6pJx_4ZByqoPzyJtKKoaqpFkeWGODQdR73i47AhY7_NjzTKeqmnyQAeyi0QLEUAM_lSF-bsksrRopb42gOdYReqC4MIJlxO7Gqw9qlkosBVmBvZ_f01K3Ua5pRnRnVIYRyXRzf4bJvmfwqtJ9-RGsNmogXKoGr83QGHyCndMoa9Qn4EUids0DBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: توافق مقدماتی آمریکا و ایران نزدیک‌تر از همیشه
🔴
مذاکره‌کنندگان آمریکایی بیش از هر زمان دیگری اطمینان دارند که به یک توافق مقدماتی با ایران نزدیک شده‌اند. نگرانی اما بر سر جزئیات ریزِ برنامه هسته‌ای ایران است؛ موضوعی که حل‌وفصل آن به ۶۰ روز گفت‌وگو موکول خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/123525" target="_blank">📅 19:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123524">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: محاصره دریایی را یا با مذاکره یا با اقدام مستقیم می‌شکنیم؛ اگر درگیری ادامه پیدا کند، بعد سومی از قدرت را آشکار می‌کنیم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/123524" target="_blank">📅 19:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123523">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaEr60NG_VRIN_XS9OxTMsyBZwi2NBIlzZ9fsHAIFYRMQjvJuDHtZV0EDrr65cv2voUnYma0mhGSmZunLpA1ET12IbcJlx9q9j2YqjAW_uzG_5YypMBuHoBWlScwNDCsn_-6Q7HntdfGWFwJfHDeM35SsU517OtcB_awtDMnRqZZvOZ_JdAPA9q8Pc2Kqr8u0BOQBT5rgVG5pCiKYocHtPeaaqpToznaMBg7V5eOGrBdvPfShRF9cjZrgSW4b_8cNQ1BsZI0o-7-PJeKxYk7TLM_fq78fBhBKAZq7sHNGiGKBGuEhT2_CKdSoNEkQasGoLSQnukOa-wV1COpMgTQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر ۳۰۰۰ تومان ریخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123523" target="_blank">📅 18:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123522">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ناتو: اوایل صبح امروز، یک ساختمان آپارتمانی در رومانی توسط یک پهپاد روسی هدف قرار گرفت
🔴
ما بی‌مبالاتی روسیه را محکوم می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123522" target="_blank">📅 18:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123521">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_8lTAs_o-0Ux3ieYsAAzhVcn6O1wLk1bS_PAadVoj_W5wKEkB8RJNYkr-1UHkDcffpA-QaGngaYhT-d1wCFyOmQfgiLMv1tIp9ZqzlWtvcyFBW0V89jryuhUiHLO1mFV6bkmrmD0FkaIyHLsI_yBTwsR6ol9YRnhITyxPqFIrzsPp6tOhFaRguLD90KDLmiLw7B2D4OPQVGqnm_eFqkoMnrqBwG7oxVWAXSKAUhA3IwNdstgVIqt1n_Ork8edXvJrsGkqG8akpIkKJx9qL0JZe74PDp13g73TXFHdxdjKGval3PIJpKvjaQgx7Mn7tPgxb0nDUV3sTmF50-AP4NtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت
هم اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/123521" target="_blank">📅 18:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123520">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
شبکه ۱۵ اسرائیل : به نظر می رسه ترامپ با یادداشت تفاهم با ایران موافقت کنه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/123520" target="_blank">📅 18:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123519">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
شبکه ۱۵ اسرائیل : به نظر می رسه ترامپ با یادداشت تفاهم با ایران موافقت کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/123519" target="_blank">📅 18:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123518">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل هشدار تخلیه برای زفتا در جنوب لبنان صادر کرده است پیش از حملات اسرائیل در پاسخ به «نقض آتش‌بس توسط حزب‌الله».
🔴
از ساکنان خواسته شده حداقل ۱ کیلومتر از روستا فاصله بگیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/123518" target="_blank">📅 18:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123517">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: محاصره دریایی ایران از همین حالا برداشته خواهد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/123517" target="_blank">📅 18:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123516">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/123516" target="_blank">📅 18:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123515">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/123515" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123514">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8881c6e145.mp4?token=oa5MN0dnGrHc6OWWL5-YlLURdkfo1H314HI1vN9W1q4J6gl0JIPhPDkKRk__rZfbHV7v0GDSA4BOC6RFkwRmmeS-X0Dmgwqs1CacpUolpo2Q2LdDQvozmvAF9kM9bqUKeNsQbA8jn4Xer197E-SnMHIAzB-vNjclbk2pY8JQTfB5xpD20j6IbAE5XFjMCSKpBygANaqyt75IuR9cweNJI1dZZWu5DQT73hayZuChdQ6GaRNgXX6bLjrbeQk5uRQds7OdrSFlygkhhrYBWquWzAF9DR3RKPgLyegO3d96H7pyItK2WM_vh03eGTz5X0P-r7_gjFpyi3paHhjd028blnMdo_rW9jwmvxykEasDXdgGROUcWADKHQNlFR8wwQveC3n--elLi83FO98YcPNI4OvQ1s4pjpej2WeusxarSX1NYxLL3acARNWRPcKJL9kiDEed8uuG-L5Hgo0-tj8R2Gijy4uppVM6tfG9CGDgoBhbeWoIPRPy0LzP1r_ECSgz360AkYH70e12MQ6YNUTnJYixOhQO54wYWJXosou9X-z4e2XLvOZvBromz2hGUbc2Mv1Zv_8BGQufw-liCaiLPFlC4Lzh9Y-tXReUuJjExStPZWAV73oBAnO5xzIUq4WPwPVyDD-8mWvughg3GjcWSXwc8lzpD9SeC_aqX0_aafE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8881c6e145.mp4?token=oa5MN0dnGrHc6OWWL5-YlLURdkfo1H314HI1vN9W1q4J6gl0JIPhPDkKRk__rZfbHV7v0GDSA4BOC6RFkwRmmeS-X0Dmgwqs1CacpUolpo2Q2LdDQvozmvAF9kM9bqUKeNsQbA8jn4Xer197E-SnMHIAzB-vNjclbk2pY8JQTfB5xpD20j6IbAE5XFjMCSKpBygANaqyt75IuR9cweNJI1dZZWu5DQT73hayZuChdQ6GaRNgXX6bLjrbeQk5uRQds7OdrSFlygkhhrYBWquWzAF9DR3RKPgLyegO3d96H7pyItK2WM_vh03eGTz5X0P-r7_gjFpyi3paHhjd028blnMdo_rW9jwmvxykEasDXdgGROUcWADKHQNlFR8wwQveC3n--elLi83FO98YcPNI4OvQ1s4pjpej2WeusxarSX1NYxLL3acARNWRPcKJL9kiDEed8uuG-L5Hgo0-tj8R2Gijy4uppVM6tfG9CGDgoBhbeWoIPRPy0LzP1r_ECSgz360AkYH70e12MQ6YNUTnJYixOhQO54wYWJXosou9X-z4e2XLvOZvBromz2hGUbc2Mv1Zv_8BGQufw-liCaiLPFlC4Lzh9Y-tXReUuJjExStPZWAV73oBAnO5xzIUq4WPwPVyDD-8mWvughg3GjcWSXwc8lzpD9SeC_aqX0_aafE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون اسبق وزیر نفت:
آمریکا و اسرائیل با استقرار سامانه در ترکیه، بحرین، قطر و یک کشور دوست ما جلوی بارش‌‌ها را گرفتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/123514" target="_blank">📅 18:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123513">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رئیس ستاد کل اسرائیل:  عملیات ما در لبنان محدود به خط زرد نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123513" target="_blank">📅 18:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123512">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پیت هگست به پرسنل نیروی دریایی مستقر در ناو یو‌اس‌اس باکسر: رئیس‌جمهور ترامپ گفت «ایران یا باید به روش درست عمل کند — با توافقی روی میز — یا باید با مرد من در سمت چپ سر و کار داشته باشد.»
🔴
آن مرد من بودم.
🔴
اما من نیستم.
🔴
شما هستید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123512" target="_blank">📅 18:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123511">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
العربیه: وزیر خارجه پاکستان در واشنگتن با روبیو دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123511" target="_blank">📅 18:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123510">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
هشدار ورود موج گرمای شدید؛ دمای در برخی نقاط کشور به ۵۰ درجه می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/123510" target="_blank">📅 17:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123509">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فاکس نیوز به نقل از وزیر جنگ آمریکا: ایران دو گزینه دارد: یا از طریق مذاکره برنامه هسته ای خود را کنار بگذارد یا از طریق نیروهای ما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/123509" target="_blank">📅 17:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123508">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پیام عراقچی در خصوص تماس تلفنی با همتای عمانی: ما درباره تنگه هرمز و مدیریت آینده آن در چارچوب مسئولیت‌های حاکمیتی و حقوق بین‌الملل گفت‌وگو کردیم
🔴
در تماس بسیار سازنده با جناب بدرالبوسعیدی وزیر امور خارجه عمان همبستگی ایران را با عمان در برابر هرگونه تهدید ابراز کردم.
🔴
ما درباره تنگه هرمز و مدیریت آینده آن در چارچوب مسئولیت‌های حاکمیتی و حقوق بین‌الملل گفت‌وگو کردیم.
🔴
ما از مشورت با همه کشورهای همسایه استقبال می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/123508" target="_blank">📅 17:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123507">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
روزنامه عبری هاآرتص: مشکل فقدان استراتژی در قبال جبهه‌های ایران و لبنان محدود به اسرائیل نیست، بلکه آمریکا نیز در نبردی نظامی، سرگردان و غرق شده که قادر به تعیین مقصد بعدی خود نیست.
🔴
ترامپ در محاصره میان ایران و لبنان قرار گرفته است.
🔴
زیرا هم‌زمان بر پرونده هسته‌ای ایران، تنگه هرمز و هم‌پیمانان تهران از جمله لبنان متمرکز است که او را عملا در چارچوب «وحدت جبهه‌ها»ی مورد نظر ایران قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/123507" target="_blank">📅 17:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123506">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4VDhooUoNDPe6DxQ-nj77w161wb5ANBz4HZPp54AnUpKxEgb6t6hcYqDaq7l_FlHUupELtqMC__StaWzgvwaXRqNvMsKBhaP990GtG92_ipRGcWVlcEHdAzhmOmOJdsxJECiwsj33-pzrzhhRS1yKpp7EZMQYHsSU_0QDwowJOBc96AmVu_TsvevfANKSEk8FB41L1fgqgOsGcOpXEI9stf8DvfSPjyKOB4dr9l6Pi47Q_O1OsgZ4_-CGlhFrgrTYhTjYDgZrSfQ23f3HrjA15qjfqB4YpajR_UStf3lF9eAEr4vfOGWbY4E3WkfCaavIUDFtZEldjMII_C3Q3AwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدودف کشورهای اروپایی رو تهدید کرد: شهروندان کشورهای اتحادیه اروپا باید درک کنید که مقامات شما به طور یکجانبه وارد جنگ با روسیه شده‌اند
🔴
پس هوشیار باشید و از هیچ چیز تعجب نکنید، خواب آرام به پایان رسیده است، اما می‌دانید از چه کسی باید بپرسید چرا!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123506" target="_blank">📅 17:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123505">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqyK9TtvtwhxYhuuOf2XFlto5Yrc5NHCI11EW9vqlLSaKOU8GGHuTT6x4o-lbVxXsaTXhdKqklcRH7NZX85yFWCGCJXiHEbyU5elQRt5Dzc_ESnJroVEGv2ZD3zewWQtAYDiPJMl9JxzpI7lfZ69HgWTtCwzvhM3X5r6be0ikjVfnDNpTWpbYwiAXJibqpWI-sFyhaZw1wmC2h54QfpK-ezV3FCdbXQuBjht4nsAX7M4RW5x9odSr0An4Ce0YfDuYBIYKhQlDCsEibPFkkE8oWp-9RcFtSLWDvBs68xgjsxk6r8aKZ8Tl4iUhDDqzbr4UhasTNVdoHHqn7uSBazlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیم اندرسون رئیس اندیشکده استرالیایی:
ادعای ترامپ درباره بین المللی بودن آب های تنگه هرمز مردود است ، تنگه هرمز کاملا در محدوده آب های سرزمینی ایران و عمان قرار می گیرد و هیچ آبراه بین المللی ای میان دو کشور وجود ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123505" target="_blank">📅 17:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123504">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سنتکام: از زمان محاصره، مسیر ۱۱۵ کشتی رو تغییر دادیم تا مطمئن بشیم ورود و خروج بنادر ایران کاملاً زیر کنترله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123504" target="_blank">📅 17:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123502">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: محاصره دریایی را یا با مذاکره یا با اقدام مستقیم می‌شکنیم؛ اگر درگیری ادامه پیدا کند، بعد سومی از قدرت را آشکار می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123502" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123501">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e60b7eea.mp4?token=DMGu091q0GNC0q4ohFURE5tO_Wla5NWjqgPiCtduacicXu_NU7HYXlZIHlNjBC1uo5R9-xMlHcrjyUfqWbI_K6n84T2SP9wR5KacNCzMfBMrETLAf1OQrXD41wihry2q9lyh1-7j_inJFrige4n95cWm6FIM624FIs90MKIU9XdRy6RjRZiau450LV4eEk1wKISH9942eN5B1_ruGg2KqstU1gE1qT4dvMFFWwGFcRG7CIH1iTk9IRyIbrQ8B7A3r6jFC061Ubvj4Xuc1k_PGsjS6dRzFdGhAvuCJ4IFqkwxLCESFfMRyPLujlPl2S7u7mX7bn-kccNbz03wZ9ykvSfQw24cOhpTWAgzZRc8iY-eaYw2v4DK0Xxkaio8oxGNwlWV0_A3D46foT_2VtDqxs5l6ozasEO7h_61eTXAVQsXcpsEWsw73cmD4qfAZqwOTnwjdzLvtPL7G5XXkHiR7mCb_7rTG4BpdbabaMRtz_y1LY2YmHXifGobh33qouMiEZDjR4aUwsZooyYSTD_CM7f7zoBmN5R9Hpp4K0YymlMCf3E-uLVH7-83a2xwtNJUxR8eeVRqnVdZg7dS2EM63gOy9Ykx0mOJlRDIlVgJNuJ5-pfxAOykKK4FzlTiAesbxKuXeezdLcmZgSfCKWyoPCXUIajB9pItUBJ_hCgkF0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e60b7eea.mp4?token=DMGu091q0GNC0q4ohFURE5tO_Wla5NWjqgPiCtduacicXu_NU7HYXlZIHlNjBC1uo5R9-xMlHcrjyUfqWbI_K6n84T2SP9wR5KacNCzMfBMrETLAf1OQrXD41wihry2q9lyh1-7j_inJFrige4n95cWm6FIM624FIs90MKIU9XdRy6RjRZiau450LV4eEk1wKISH9942eN5B1_ruGg2KqstU1gE1qT4dvMFFWwGFcRG7CIH1iTk9IRyIbrQ8B7A3r6jFC061Ubvj4Xuc1k_PGsjS6dRzFdGhAvuCJ4IFqkwxLCESFfMRyPLujlPl2S7u7mX7bn-kccNbz03wZ9ykvSfQw24cOhpTWAgzZRc8iY-eaYw2v4DK0Xxkaio8oxGNwlWV0_A3D46foT_2VtDqxs5l6ozasEO7h_61eTXAVQsXcpsEWsw73cmD4qfAZqwOTnwjdzLvtPL7G5XXkHiR7mCb_7rTG4BpdbabaMRtz_y1LY2YmHXifGobh33qouMiEZDjR4aUwsZooyYSTD_CM7f7zoBmN5R9Hpp4K0YymlMCf3E-uLVH7-83a2xwtNJUxR8eeVRqnVdZg7dS2EM63gOy9Ykx0mOJlRDIlVgJNuJ5-pfxAOykKK4FzlTiAesbxKuXeezdLcmZgSfCKWyoPCXUIajB9pItUBJ_hCgkF0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل نتانیاهو تأیید کرد که نیروهای تیپ ۳۶ ارتش اسرائیل از رود لیطانی عبور کرده و به سمت نقاط استراتژیک جنوب لبنان پیش رفته‌اند. او اظهار داشت: «نیروهای ما از لیطانی عبور کردند، به زمین‌های مسلط پیش رفتند و در بیروت، بقاع و در سراسر جبهه عملیات انجام می‌دهند و به شدت به حزب‌الله ضربه می‌زنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123501" target="_blank">📅 17:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123500">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZOlmh9J7SOSwX5Q8p-L5JfWyA1nCsXF2VI7Nget3rFB3FmoflJj7zaHimxDZjldwLL3eF7Dj-Ft6nSZb-x1Gp6dWyRDplx3tTsA41keRzy2jL-7D-A0d-Sz-GHv32K9C2V71PNX6RdekIdNsMSddgQoJKp_rG-QqnqS-KkxJaWFwtsC5TS9oFbd6IJdGZEpHjELrR1OYpfZOvQTgRAs2ZtbKcm4b0vHxSCtLSVASyOIZxJ9ZAeNHmq-vnfEyn2ujR--CJ0DxXmXrFBgo6wOjoSg1RA3_LDI9OGjTO1VLgUy3LSsbdc-ln_WqblMJk3zcTb__XNLMEW4hc0fA_aahlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">CRYPTO SNIPER
〰️
همین  شات ها کافین که همه چیو ثابت کنن
✅
برآیند خوبی هم تو معاملات دارن
✅
و اینم بگم رکورد هایه کامنیوتی فارسی دستشه کارشونم با شفافیت کامل هست هم گروه باز هم نظرسنجی هفتگی درباره فعالیت
✅
ما هم تاییدش میکنیم
لینک :
https://t.me/+vlymyfKFnUo5MjI8</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123500" target="_blank">📅 17:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123499">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ee0c5b006.mp4?token=r_zK3I55-azPA00vXmZtT0tjhMRmomJn-27YIe49P20a7t4vGAehW551gdq7mQZQ2sADbf3rA6Wj8FBPdWoj5lOaNrqROWEWe2ZxCRT3h8rSdd50q5w_iyJE5JxyeZ1rKjo4uOUeFiJ8HdgdlCjLBUW9uD8Ezzqg-cHnFoEup5aFkgHaPaDUFp3pjCk0J5DKAtacrC4bxg8hR0M3jGn5vhKKvWwYCfdjYVBKGWE2uPrc6Vna1eB38FOgKMIASOSFnLUh7mPhG_r8Owbxurcx9jvf1GNgeJ78goIxTxJKwzZLHT4ZpYJtZfaHw1Zdf5c6FJrh75faOhNZ6zCEEVHSVxa4exguSQmgcAJgBJE99NUQplet6aZjCa5ySzJPaEUwYwq_K__JgC30foaykWhdJRAVYYFrked17rixa-L5L6exlLQAMKZejMaXiCCo5ipHkR5rFv3ZqYknNO8NYho6HFFB0cZC6BqQUEX-YU6AMM0QrfhJ7x4k6mrv5AiY7GqFJRWVhXICol3y7zpfe-7ZQI_KXslHcjGRNtlURfICv94zD4RgpxPMt0xRbrjB6LUnS-ooJI1iV4CTpmJXir0jcQ-Eg1kvyHLl9ijdS5DVoUwW3lci5vj5z4qSUZWH5L-z6RXYiQJpbWjurymK-Beh6Ij_EBpMhAvKhVtA-Jyg-LU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ee0c5b006.mp4?token=r_zK3I55-azPA00vXmZtT0tjhMRmomJn-27YIe49P20a7t4vGAehW551gdq7mQZQ2sADbf3rA6Wj8FBPdWoj5lOaNrqROWEWe2ZxCRT3h8rSdd50q5w_iyJE5JxyeZ1rKjo4uOUeFiJ8HdgdlCjLBUW9uD8Ezzqg-cHnFoEup5aFkgHaPaDUFp3pjCk0J5DKAtacrC4bxg8hR0M3jGn5vhKKvWwYCfdjYVBKGWE2uPrc6Vna1eB38FOgKMIASOSFnLUh7mPhG_r8Owbxurcx9jvf1GNgeJ78goIxTxJKwzZLHT4ZpYJtZfaHw1Zdf5c6FJrh75faOhNZ6zCEEVHSVxa4exguSQmgcAJgBJE99NUQplet6aZjCa5ySzJPaEUwYwq_K__JgC30foaykWhdJRAVYYFrked17rixa-L5L6exlLQAMKZejMaXiCCo5ipHkR5rFv3ZqYknNO8NYho6HFFB0cZC6BqQUEX-YU6AMM0QrfhJ7x4k6mrv5AiY7GqFJRWVhXICol3y7zpfe-7ZQI_KXslHcjGRNtlURfICv94zD4RgpxPMt0xRbrjB6LUnS-ooJI1iV4CTpmJXir0jcQ-Eg1kvyHLl9ijdS5DVoUwW3lci5vj5z4qSUZWH5L-z6RXYiQJpbWjurymK-Beh6Ij_EBpMhAvKhVtA-Jyg-LU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: دوران بمب اتم گذشته است؛ الان با عملیات میکروبی و بیولوژیک می‌توان حملاتی انجام داد و مسئولیت آن را گردن نگرفت
🔴
می‌توان بمب چرک استفاده کرد
🔴
ممکن است شرایط به جایی برسد که به رویارویی هسته‌ای برسیم؛ باید اقدامات پیشگیرانه انجام داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/123499" target="_blank">📅 16:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123498">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I08wII7dVOSKvqbNOBbfsMKOmE_Xkef6vzHkXwLImCEzORFvxHP4clwVCYhqmtZiHrnuW2TBHcc6EEFO9Ved3PEG2YgLwN7WHfLhU6aQTdIY7GzDYIbDsEDsIc27llQSYjOXqmhxSVZXG6KbLWikWbTTl-bW2rtvHzD7jU_FsOscmSMSub-u5TGsvBODyTcQeQKtfn9q2aRQw05CHA-w1_vLek4El-F-ob2xXlvh7v8I1X5ZCkqZFTxO4eMEJrfrCBiXTz1R1jiZ7eBuRcbKNHnugZjGkoNa1FSZNUYYRGh0dLGb9H7mnkztzRqE5AJceCPy1HfYqohUw0NBIFDGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید قالیباف : ۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123498" target="_blank">📅 16:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123497">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نیروی زمینی ارتش اسرائیل به دروازه های شهر نبطیه، دومین شهر بزرگ جنوب لبنان رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123497" target="_blank">📅 16:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123496">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز درباره جزئیات توافق احتمالی ایران و آمریکا/ ۱ - آتش‌بس اولیه و پایان موقت خصومت‌ها
🔴
به نوشته نیویورک‌تایمز، یکی از محورهای اصلی پیش‌نویس، تعیین شرایطی شبیه پیمان عدم تجاوز میان واشنگتن و تهران است. واسطه‌ها می‌گویند انتظار می‌رود این توافق دارای یک مؤلفه منطقه‌ای نیز باشد؛ موضوعی که به گفته مقام‌های ایرانی و یکی از دیپلمات‌های آگاه، شامل توقف جنگ در لبنان هم می‌شود.
🔴
دو دیپلمات مطلع از آخرین شرایط گفته‌اند توافق اولیه، پایان خصومت‌ها را برای یک دوره ابتدایی ۶۰ روزه تعیین می‌کند و امکان مذاکره میان دو طرف برای تمدید آن را فراهم می‌سازد.
🔴
با این حال، مقام ایرانیِ مطلع از پیش‌نویس می‌گوید متن مورد بحث شامل «اعلام پایان جنگ» در همه جبهه‌ها، از جمله لبنان، برای کل مدت مذاکرات است. دو مقام ایرانی نیز گفته‌اند مفاد این یادداشت تفاهم صرفاً مربوط به دوره مذاکرات برای دستیابی به یک توافق گسترده‌تر و دائمی خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/123496" target="_blank">📅 15:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123495">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یک منبع مطلع به تسنیم گفت: متن تفاهم‌نامه احتمالی هنوز نهایی نشده و متونی که رسانه‌های غربی منتشر کرده‌اند عاری از دقت است؛ متن طی چند روز گذشته تغییراتی داشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/123495" target="_blank">📅 15:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123494">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
الجزیره: اسرائیل بزرگترین مانع رسیدن ایران و آمریکا به توافق است
نورالدین الدغیر خبرنگار الجزیره در تهران:
🔴
به نظر می‌رسد که اسرائیل بخش بزرگی از موانع رسیدن به امضای توافق بین تهران و واشنگتن را تشکیل می‌دهد.
🔴
اطلاعات حاکی از آن است که نقش اسرائیل [در عدم امضای توافق] پیچیده و چندوجهی است و فقط به بحث لبنان ختم نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/123494" target="_blank">📅 15:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123493">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران با سرعت بسیار بالا داره توان موشکی خودش رو بازسازی میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/123493" target="_blank">📅 15:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123492">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از مقامات:
ترامپ به مشاورانش گفته است که برای تصمیم‌گیری در مورد امضای توافق احتمالی با تهران به چند روز زمان نیاز دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/123492" target="_blank">📅 15:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123491">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvsPLSMBmV0FW4RtPeBVUe7LmYIyaGauKpdY-eGtSbd2QVlmeefuz1HJBSHulDC3q2uvpuxYuWKYovGqhXzwVv7btxOS4QzGKe3biv-4m6KrzeEH1suoGV-nKq3POkdtBNb03VaK_rp_At6I-WTLqVG4XeAp4_1NBbpEqMYD7WhvY57gnu5QUJRQnXCXNKkchdnQXXIu6N9xCPF2wSVZrUxw-vMJO84OhU79gKd9RefRVPtSMpuWvqDXTAajWHJQMHji2nFRijek7h7Pz-WvGbmXUnqwcioapSDhYsxS9YUGoA721CHjkaZOI2U6Q0HwRD28mcAPEy7YqYtndSS0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز ملی مشاورین املاکه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123491" target="_blank">📅 15:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123490">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
حمله حمید رسایی به مجتبی خامنه‌ای با داستانی از پسر نوح
‼️
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/123490" target="_blank">📅 15:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123489">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjAtVJL97mhurJLa61JZ34mYKsBNMnGZ5If2YQmF8VJGIfhRn0ISNOlZmBI-x-9SJT54g11zKJ7gLaPsolAN7COrxtYddcXXosZ6-anyVciymPC-h7IsL6XVUXdSbqCteZhcb5xWk9jYfaYsa8bfBin31-5tPMVUhWaOUnDrK_9hJ_ZLuiqLN1AjyIoQfiBNLKRfACNvxgvb_wZpvzKUbI60eX6TLcldvIg1hOmOr23s8yXjQyZt2DA2999loBBz6gLxBTNfIFGgLtlFKxj6UATojK51LYO_yWRw34mRNUY_ZL9_M1BR2dnluoTvgtYIGvdXYCBPfY2HGXnIL2N_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام‌جمعه کرج: موشک، آبادانی میاره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/123489" target="_blank">📅 15:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123488">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
نیویورک‌تایمز:
ویتکاف و کوشنر راه‌اندازی پروژه‌های ساختمانی در تهران و یک صندوق سرمایه‌گذاری را در صورت حصول توافق پیشنهاد کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/123488" target="_blank">📅 15:07 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
