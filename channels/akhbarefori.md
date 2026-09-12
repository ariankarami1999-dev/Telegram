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
<img src="https://cdn4.telesco.pe/file/ceNHDQbfAK16gq_FGVVgh5iLUnT-tFU0ZzLRVHeyPA1DCRJi8n-G6ZzDz0WoO4Vtm-ohqK14AYDL3HEtW4MyPkZQUrx0wXOKoWS3AZ2bjMyJcTPehJ-lGdmizZeSdFear0oQDvtX7-VMG7NZKSEGuZ9YVP7iAxUNjHm-Sb-KrxpedW463hi_-ckPyDu-XDLU1HpMfkAODuRiMolHmR9kqQwhtfCN8JrNXoGIe03P4NUdSGcEIfr3YIQPz1LAiEHYDZwR9TRAuNnmHmlxpdxRpYdQD2DM2bW1_nt3G2M9ubH5jSPek7UsHH5Ct5avkE0c19mGsnnOQZwc7ScD0FSuwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 20:48:51</div>
<hr>

<div class="tg-post" id="msg-689317">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8qz4mR4SBvuYgw-4nYtj5l8z1Bm41dWDZR6HpIUxv5tknT1356r_vvm7yagAsW6o-uDPNO3fv2uizJyfLKTXpCCw_iqh-RpxsPtNiCzmsoTkKO8iXk0wexz7ww9d7eUD4XvS_ZC6-WfsS-aZ8W6MYxJ36u0xAqeKh-XRBlxuf37Kpy_qH2fv0hg4ewjHks6JM_4XXR4XpKQY-r2yvmsFwldFWiJerwomGhvW_0ZtlXeXgHvcmSnBCaR-ovcVq5lr3ieVIer7SO4t-E7cikmT4dmlTIcLPMDMnsTVKxq1hN2urHRZ9pE-kIu0iCiM9SezOGtRGFfv_ICyuO5fBO9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسامی شهدای عملیات ضدتروریستی سحرگاه امروز سراوان  روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه:
🔹
در عملیات سحرگاه امروز حافظان امنیت که بر علیه تیم‌های تروریستی، در شهرستان سراوان انجام گردید، تعداد ۳ نفر از رزمندگان اسلام، به‌نام‌های «مسلم فاضلی»، «میثاق ثانی»…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/689317" target="_blank">📅 20:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689316">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc3852da87.mp4?token=Xos6TAZZ2Ty476ZuSJ3lYjujSlK3eiIa8qxfdYjpM8B9OjsBCFqz2XTCgq3YfuoXwGZDfgBiSfT1f4MUfGV7D5KQxljeIh_eOILWeGg1vjQr_HTkDXq9Q_ahuKYVYJk3KBphQZSDZelshycOurFNsP3iEw0FEswG4XiGF7HT4O5P036sFQY82VEfQpHZHo6Xdooo9NOBjFWzSXEJ2WQELWDs8oq122jPFUc7oISHA8Jj6FSogsMdqBo76x9TCwuuFD149czm_5OwY2EnRT4q1ff4ZlIJcyekWJIIAi1Cwpxq7bXEMSgqIvkljyR6VtDD221dYnPCSym5WP5v6dwsVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc3852da87.mp4?token=Xos6TAZZ2Ty476ZuSJ3lYjujSlK3eiIa8qxfdYjpM8B9OjsBCFqz2XTCgq3YfuoXwGZDfgBiSfT1f4MUfGV7D5KQxljeIh_eOILWeGg1vjQr_HTkDXq9Q_ahuKYVYJk3KBphQZSDZelshycOurFNsP3iEw0FEswG4XiGF7HT4O5P036sFQY82VEfQpHZHo6Xdooo9NOBjFWzSXEJ2WQELWDs8oq122jPFUc7oISHA8Jj6FSogsMdqBo76x9TCwuuFD149czm_5OwY2EnRT4q1ff4ZlIJcyekWJIIAi1Cwpxq7bXEMSgqIvkljyR6VtDD221dYnPCSym5WP5v6dwsVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جیرجیرکی که میلیونها سال در دل کهربا زندانی شد
🔹
فسیل یک جیرجیرک باستانی در کهربا، همراه با حبابی از مایع و گاز (اِنهیدرو) که میلیونها سال درونش محبوس مانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/689316" target="_blank">📅 20:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689315">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپلتفرم شیدا | SHEYDA VOD</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odA7QlXf0OtqPuD90OFBKFL_4aADGPAkHK88tJN4e_yjZVJetRCs0uHDTQZKbSeIrWdF__d2RKx_ZvwSypCJQgvhPWVgLmvv0dUQ0ggVeJ9cJkpj9Cw9cu861kDq9_KUjbkT_Vt_MrgY-Ns4CZXEQ_VU2h1dxmq4opSbHWQ7rbTfr-GNKuGA0-Oy-9PHyHuGoDtvaMjBw9wpHwfS1q2TGdxVmYdvZL0-VVro7ieSLnKEaXWFdpQI6DcZQK-IrGdXur_6AJFhpBduhZBAg0S89aGNaDevLCRcOHVotL4N6H-lgzP-Bp-1BKI9lB_nPCxnLqDWYoXNanAfGEr2er-3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با روز ملی سینما؛
تصویربرداری «ده پهلوان»، قصه تازه حسن فتحی در عصر صفویه آغاز شد
تصویربرداری سریال «ده پهلوان» به کارگردانی حسن فتحی و تهیه‌کنندگی زینب تقوایی از بیست و یکم شهریور همزمان با روز ملی سینما شروع شد.
به گزارش روابط عمومی شیدا، این عاشقانه تاریخی به نویسندگی نغمه ثمینی و حسن فتحی، داستان خود را در بستر دوران صفویه روایت می‌کند و نخستین سکانس‌های آن در منطقه پارچین مقابل دوربین رفته است.
در نخستین روز فیلمبرداری، محمدعلی مشکیان، مدیر پلتفرم شیدا، و مصطفی شریفی، مدیر محتوا و استراتژی، با حضور در پشت صحنه این پروژه، از روند تولید بازدید کردند.
«ده پهلوان» روایتی عاشقانه و دراماتیک است که در فضای تاریخی عصر صفوی شکل می‌گیرد و یکی از پروژه‌های مهم شیدا در حوزه تولید آثار نمایشی به شمار می‌رود.
جزئیات بیشتر درباره داستان، بازیگران و سایر عوامل این سریال به‌زودی منتشر خواهد شد.
@sheyda_vod
www.sheyda.com</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/689315" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689314">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
معاون برق وزارت نیرو: احتمال قطعی برق در زمستان
معاون برق وزارت نیرو:
🔹
ذخیره گاز تا زمستان به ۳.۵ میلیارد لیتر می‌رسد، اما به دلیل محدودیت‌های گازی ناشی از جنگ و آسیب‌های جنگی، احتمال قطعی برق در زمستان زیاد است./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/689314" target="_blank">📅 20:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689313">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a04a3913a.mp4?token=qNpIN77pORhNbwSIHRGzBq5TjO25ixRTD7IIi3wlLk4j3WnxLvCAyMee3rAI2dWSGk-Y56WHvvQFx7_reb-W45Eqr0v-0Au4S8uQIdXDHH59wSMr_rPIhQInd5KAaPsvn8UfQQGFwsdiLh3-Cip3_BGjn8fjBfh-hMTiH6TUx1Boe2wYeGCHG8BdhHb63gGav9aBO5npdDcuweLf1KLbCO78qkMo9jOiPLn4v1XHuY83pw2QEt0UQqkBbuKe39e_WoabkRBn44mT4Ud1k8TispKyAej81h33V0S5OerI3_QCDh9CgdNg98_qn8MQLKFK_wttJi9l6OLjyZtZoF61jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a04a3913a.mp4?token=qNpIN77pORhNbwSIHRGzBq5TjO25ixRTD7IIi3wlLk4j3WnxLvCAyMee3rAI2dWSGk-Y56WHvvQFx7_reb-W45Eqr0v-0Au4S8uQIdXDHH59wSMr_rPIhQInd5KAaPsvn8UfQQGFwsdiLh3-Cip3_BGjn8fjBfh-hMTiH6TUx1Boe2wYeGCHG8BdhHb63gGav9aBO5npdDcuweLf1KLbCO78qkMo9jOiPLn4v1XHuY83pw2QEt0UQqkBbuKe39e_WoabkRBn44mT4Ud1k8TispKyAej81h33V0S5OerI3_QCDh9CgdNg98_qn8MQLKFK_wttJi9l6OLjyZtZoF61jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۷۰ سال تکامل کامپیوتر، از کامپیوترهای قدیمی تا ماشین‌های آینده
🖥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/689313" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689312">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تصویری از خسارات وارده به پالایشگاه جیزان متعلق به شرکت آرامکو عربستان در نتیجه حملات یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/689312" target="_blank">📅 20:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689311">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff5e01ea0.mp4?token=KXxdfMab94qNoZ5AeC45an4I4iAb62LGGnxVBxcYtvGk_bOnhSNmHh27Kn0J8Ia8SNnipuAM5HQOPoxBZKamir0JwwXeQ3TiKUZGpHIxfs-qA4RzNKu-J2FPC1cCoGwFm-ckmRhC6sb_yYZfXcSKdlWT87_S7HBXlW1pqapBDroN5r4GvlbLdaRNWYpm2Twg_ubkXsw7lTkSnmmq_M4XFMX5vrE1kClKGAaeFXsSFZqW1ne0clzUYaUlYlzJBNxSrRiSMZ8bHkYrmYn0nREWPRJLuRopfPfQRKbYMP8TYTX2GRBZ6lQC9cftFhToSLI4mmPVRqkVVkpiKWSzHUWIcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff5e01ea0.mp4?token=KXxdfMab94qNoZ5AeC45an4I4iAb62LGGnxVBxcYtvGk_bOnhSNmHh27Kn0J8Ia8SNnipuAM5HQOPoxBZKamir0JwwXeQ3TiKUZGpHIxfs-qA4RzNKu-J2FPC1cCoGwFm-ckmRhC6sb_yYZfXcSKdlWT87_S7HBXlW1pqapBDroN5r4GvlbLdaRNWYpm2Twg_ubkXsw7lTkSnmmq_M4XFMX5vrE1kClKGAaeFXsSFZqW1ne0clzUYaUlYlzJBNxSrRiSMZ8bHkYrmYn0nREWPRJLuRopfPfQRKbYMP8TYTX2GRBZ6lQC9cftFhToSLI4mmPVRqkVVkpiKWSzHUWIcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ در مورد حمله به خط لوله نفت عربستان: به احتمال زیاد ایران مسئول این حمله است    ترامپ:
🔹
جنگ ایران خیلی زود پایان خواهد یافت. جنگ ایران احتمالا پس از انتخابات میان‌دوره‌ای پایان خواهد یافت./ حوثی‌ها نمی‌خواهند با ما بجنگند‌‌. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/689311" target="_blank">📅 20:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689310">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df0873e00.mp4?token=tby1pHCv-LC7lVBKVxizKizBYur-3tB1rKlFaVlEDCaGPgIzrSebiz6k12fVCIDlZI30g_jgnBd7yZ7ZZlijbV2tvloRsUGkjl8FIMtCuoo0-AQXz002Xy8EhB78bgQHjddy3mV0MtINdNGM2PCkSB8DQd18fXreescWNIfQUyHgFzM_40FGai6Oo3p5JL5kJLhgm-Ou_8oQpnUtOonp7HqhLs_Q9M7tM91csEsxQpwha_thyZnX2BY58TdeDZkxQWfIkefmc18PesOm8uIp1XpMqRKBttD2X4lulohIT3VjVjojO_FhIBqU1bYWW_vc-xqzEO7Sddvamvurh6eJ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df0873e00.mp4?token=tby1pHCv-LC7lVBKVxizKizBYur-3tB1rKlFaVlEDCaGPgIzrSebiz6k12fVCIDlZI30g_jgnBd7yZ7ZZlijbV2tvloRsUGkjl8FIMtCuoo0-AQXz002Xy8EhB78bgQHjddy3mV0MtINdNGM2PCkSB8DQd18fXreescWNIfQUyHgFzM_40FGai6Oo3p5JL5kJLhgm-Ou_8oQpnUtOonp7HqhLs_Q9M7tM91csEsxQpwha_thyZnX2BY58TdeDZkxQWfIkefmc18PesOm8uIp1XpMqRKBttD2X4lulohIT3VjVjojO_FhIBqU1bYWW_vc-xqzEO7Sddvamvurh6eJ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوی سیر روی دستات مونده؟
🧄
😵‍💫
🔹
با این ترفند ساده چند دقیقه‌ای از شرش خلاص شو!
✨
ذخیره‌ش کن که یادت نره
😉
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689310" target="_blank">📅 20:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689309">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6244a14dc9.mp4?token=UnZVn2W421nURZGQy6sFRnPT_4imYgA880G8u4gIKh2df2S-BaVwkiuDA-3Pz4I3x-pGlo7DMTRytcN_wJ8h7FWi-TQstHN0lt6S29sdg_yq_fInwKIKg6lWtMuiNNKd7sOxqlAdvuwLYQojO4QDrY7-qdoFR6wwyC3AFYxCJfHTFi_Ud7NamfzVeykfBc7O4175k-VcsfUdSu2MjoHcVUvHIXd4tzF0IaYMAyoVhas-afpN0EpscSjRjHoWkBjchFqzi-SsXePwR4fUg0llgfHoekrXnxB1e5u95kpV2l1vGA10EHO_mQezGGc_NnRLZxw-Z6jdxnj-v3wQwI0ifKTsEtiWK0nh__3XWnR-CUgn9kCPrGml-rcqBPUpYLqzlaaSOsXih6WVmIJER3p8-d5YbToYaP9gvOt0EYh6TWEIiIykbElPyMTUg4N4w2nCcCu2y-0DDbWtYonUxaXHuQcDaClDwnon8WgfH5Z_j-8-F3pQVqlXt-a9J4UVDBeMTvm-CtwOZcw95PdQjBOAJ7rUe8a6NfNVpKjWPeheXe9WvVOoffKM_X_W1tidcmAKfvHcGGIZGIKSUngaaNvQIHSU8VaMxW_Di3RIC09gX64OLdDLYGlxxrELDqsNnL1PZy6SJOHDQ68CAxlG4Df_asqFUyrP4N3GbhMArYXm0So" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6244a14dc9.mp4?token=UnZVn2W421nURZGQy6sFRnPT_4imYgA880G8u4gIKh2df2S-BaVwkiuDA-3Pz4I3x-pGlo7DMTRytcN_wJ8h7FWi-TQstHN0lt6S29sdg_yq_fInwKIKg6lWtMuiNNKd7sOxqlAdvuwLYQojO4QDrY7-qdoFR6wwyC3AFYxCJfHTFi_Ud7NamfzVeykfBc7O4175k-VcsfUdSu2MjoHcVUvHIXd4tzF0IaYMAyoVhas-afpN0EpscSjRjHoWkBjchFqzi-SsXePwR4fUg0llgfHoekrXnxB1e5u95kpV2l1vGA10EHO_mQezGGc_NnRLZxw-Z6jdxnj-v3wQwI0ifKTsEtiWK0nh__3XWnR-CUgn9kCPrGml-rcqBPUpYLqzlaaSOsXih6WVmIJER3p8-d5YbToYaP9gvOt0EYh6TWEIiIykbElPyMTUg4N4w2nCcCu2y-0DDbWtYonUxaXHuQcDaClDwnon8WgfH5Z_j-8-F3pQVqlXt-a9J4UVDBeMTvm-CtwOZcw95PdQjBOAJ7rUe8a6NfNVpKjWPeheXe9WvVOoffKM_X_W1tidcmAKfvHcGGIZGIKSUngaaNvQIHSU8VaMxW_Di3RIC09gX64OLdDLYGlxxrELDqsNnL1PZy6SJOHDQ68CAxlG4Df_asqFUyrP4N3GbhMArYXm0So" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارسا پیروزفر و علی شادمان در
#سرخ_و_سیاه
سریال «سرخ و سیاه» به کارگردانی آیدا پناهنده و با نویسندگی ارسلان امیری و آیدا پناهنده، به‌زودی به‌صورت اختصاصی در
#فیلیمو
منتشر خواهد شد.
تهیه‌کنندگان: محمد یمینی و محسن خباز
@filimo</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689309" target="_blank">📅 20:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689308">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
موشک‌های رهگیر آمریکایی به‌شدت ناکارآمد از آب درآمده‌اند   ویل شرایور، تحلیلگرآمریکایی:
🔹
مسئله فقط کمبود ذخایر نیست؛ واقعیت این است که موشک‌های رهگیر آمریکایی PAC-3، تاد (THAAD) و SM-3 همگی در عمل به ‌شدت ناکارآمد از آب درآمده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689308" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689307">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdZc-h80NJtXOUCGNPIvTJByxAkUd8wZZgXxUfLQovR0fp-O1zTD-_kwMD7QH1gHd5o-RWCdG4I0s3wYY0uKHKzYj4td0BtKfR6uyZQY1mSQSlo8ixAUOmjj4pJUfU4Pp3H1r4axIuQIofVVJF1V0-cvapt7OcRTvaWEZ4QB2GnzhiFkY24vap_P0j3nl3Br7FEGQ0PFE-59PpBel3x_Y23bqrvow5WYdY1bCRov89fdGyp4JXQ-3eTH06n3OMX6GO9nyycJUulZ3rpqaZm3fY-ElHFTwG4mFo_acFG3NAvUgbHJ0-9LbAD8WQphSF1JHSAZorbRepAHw9FMePc-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابر میانجی
🔹
در حاشیه نشست سران بریکس، شی جین‌پینگ با اعلام آمادگی چین برای میانجیگری میان ایران و آمریکا، پکن را در قامت بازیگری تازه برای گشودن گره جنگ تهران و واشنگتن قرار داد؛ پیشنهادی که می‌تواند معادلات دیپلماتیک منطقه را وارد مرحله‌ای جدید کند.
🔹
هشتصدوپنجاه‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/689307" target="_blank">📅 19:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689306">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07e8f9aef.mp4?token=LmYPhRwxbOso_A0gk8KKOEOIFYuLtl5MVY-rCa4yLK7YXZulIOlcLVD-UWi7cnWXZVpJn0bO7TykYkLPxg8WMduEz6u7doW6JfDWwjtgIG-7r9_5SWzjdUVAbLwj7JM1PdL0c5Sv0TNzQNuR2Lrfy73fds1YmP1IJwHKnxI8VBezmbVgt1Fazs3yIxZ6L_e2qnPnle1QO3mg0WK2we51jqcCr5PVIFzfxdfMgI9MNRZHYboKvWipQPx6CR7pw8tfnaUweA8eG0aLPd2edLrciB9erwnlvvmhRsV_O4sRnd6NKCVIziMwkKcehprj_ISnF6YkaM9e76TCMmcbCLZdVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07e8f9aef.mp4?token=LmYPhRwxbOso_A0gk8KKOEOIFYuLtl5MVY-rCa4yLK7YXZulIOlcLVD-UWi7cnWXZVpJn0bO7TykYkLPxg8WMduEz6u7doW6JfDWwjtgIG-7r9_5SWzjdUVAbLwj7JM1PdL0c5Sv0TNzQNuR2Lrfy73fds1YmP1IJwHKnxI8VBezmbVgt1Fazs3yIxZ6L_e2qnPnle1QO3mg0WK2we51jqcCr5PVIFzfxdfMgI9MNRZHYboKvWipQPx6CR7pw8tfnaUweA8eG0aLPd2edLrciB9erwnlvvmhRsV_O4sRnd6NKCVIziMwkKcehprj_ISnF6YkaM9e76TCMmcbCLZdVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازهایی که هر روز صداشونو میشنویم، از کجا اومدن؟
🎶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689306" target="_blank">📅 19:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689305">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNZXUm_MF2oXc7IR6R3mN8P9htbgQ-bNfZTKxlpnid3xd-u6sgzBbhdwsWMvk3liONmcO0FGnhp6Ve6BfbrV10zWaiK9CUjCyRnWQlooECmdHtjDc_7O8WwwVvPo94u3vgfpinlniHEufjpTSli1FbdazHJX3ploOXuGeYi6j9HVJEgOzv5ak5duupvd4EFoPQ1kx7NAz3UuEV83yGdnD2sOK85_YorPfEhGeeET2oqTJ5yIwMUGgXvZeAfMw7kzt5HvrXczRUMz8wST0JzaVX3joX1jUlkAD93KuH22QVDo07wAPEOB4hWapgjop1LScGoQ2QDsO_BefZoLnG3tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر فرد در ماه چقدر غذا خورده است؟ | ایرانی‌ها غذا را از سفره حذف کردند؟ | سفره ایرانی زیر فشار یک دهه شوک اقتصادی
🔹
سفره خانوار ایرانی طی بیش از یک دهه گذشته نه فقط کوچک‌تر، بلکه به‌تدریج فقیرتر نیز شده است. بررسی آمار هزینه و درآمد خانوار نشان می‌دهد میزان هزینه واقعی سرانه برای خوراک در سال ۱۴۰۳ نسبت به سال ۱۳۹۰ حدود ۴۳ درصد کاهش یافته است؛ تغییری که تصویری روشن از افت قدرت خرید و کاهش مصرف غذایی خانوارها ارائه می‌کند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3244613</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/689305" target="_blank">📅 19:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689304">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAo3OxkJ3rq34pCzFPz5Sq0hreDaL70cXKGtGZz9nBaLKeqXbuwZBx1wwpw2iD6M-_hdl3KRaYJCnnGXsufYPYhRwI5vn29n5kraeX8R1U3VqPVa633JaLjZyrNrEad4ufOpQt7dQ-01LLIMPoHIoJBpS-ik6QZjgMh4AFZ92yt7ZerK0hrDmjE-ZHLKSk3uLcEiZux19o1D4iPSlXOkL1MofZ7zkeBoaTa0XYAa_vwxn9phFwWej9cZAY9nZh-JE8Wx11q-MwKIePgnhR6A5lQnu6eLMJzhhXNf8BsBYovW3N_TfkNMl_WqUzCkeHfdeTgf-QTa8q7S755sD80_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جبهۀ مقاومت در کنار ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/689304" target="_blank">📅 19:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689303">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سخنگوی وزارت‌امور خارجه: شواهد میدانی و اسناد مربوط به آزمایش تسلیحات جدید و استفاده از عوامل شیمیایی آمریکا در حمله به لامرد مستندسازی شد  بقائی:
🔹
تفاهم ایران و عمان بعنوان دو دولت ساحلی تنگه هرمز بر سر مسیر دریایی تردد کشتی‌ها، به معنای امن شدن تردد نیست.…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/689303" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689302">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ow-AXOjl87poSgRaMrIh0HORxRbvaWnLH0l_zItnL0l6EFBesJeSEPW_OxcMBbEItjadKInIy4BNC9_79A_DCucl-gAXg80Yq-wdTbj4uP3YFN3PATww-hjPOx9eHb6NlxYWEtZM6agTMaqBGP0MhctltnwFfyOlSdEoS8tH-Iz2UH_s29MAjLsPohUoSQF1K_0F26Zg5ob_5keQCNMItZEvF-w2dqJKzAtvTdYidxPVSJoZ9LsRZerMIN5PaBY-cWRiwUDEqCPvbhNQc3pJthaIrNpLeYy92s7bVI6vNDfn44wVdzVpfyntx2eZxwpDYG-sEcA4QEsZ7-dLW5b13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب ضریح امام حسین (ع)
جلوه‌ای از عشق و ارادت به سیدالشهدا که می‌تواند زینت‌بخش دیوارهای خانه و محل کار شما باشد.
این قاب با حال‌وهوایی معنوی و طراحی چشم‌نواز، یاد حرم مطهر را همیشه نزدیک دل‌ها نگه می‌دارد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۵ × ۳۵ سانتی‌متر
▫️
وزن: ۶۹۰ گرم
▫️
متریال: پلی‌استر و پی‌وی‌سی
▫️
طرح: ضریح امام حسین (ع)
▫️
کاربرد: مناسب دکور مذهبی، هدیه و زینت‌بخش منزل یا محل کار
💰
قیمت اصلی: ۱ میلیون و ۷۹۹ هزار تومان
با تخفیف ویژه : ۱ میلیون و ۵۵۷ هزارتومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/689302" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689301">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOagFcrlEeQG2Jg5ElLvG1Gx2lTO82UowAr6ejzlW2wB6sUYn7zpgRmwBAZJ5sK3JRTOkHUE0XcwBdZ-az-YIXSWbipb0QJqLPRni_0n1X1aRWa9BoeNimNFdLdpL6-FfcrCwLM1lEv01xvvJJeMJ7gptjA_pW-5qwIbABMhlnpWE8bk0B5EM7k571H_CHbyMGjDhIcOyTlqJYc0m4HN3vFizQBbyWysN8YoDTIaKs23xVWK7PNmaC0xOcne4rSuJACfrUSNPUdFUqZV1cgNvHEKSdyJAQ4D1KVoictQZ6O9TTmlBAGJcesPwnvS1gBEYasIu79wi-OFFeLl98T9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از فرح پهلوی در حرم امام علی(ع) - اواسط دهه ۵۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/689301" target="_blank">📅 19:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689300">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
هر شهر، بخشی از یک روایت ملی‌‌ست...
۹۸ سال کنار ایران
🇮🇷
📍
شیراز
🔹
شهری که فقط دیده نمی‌شود؛ در آدم می‌ماند.
🔹
در کوچه‌ها، در صداها، در خاطره‌هایی که از نسلی به نسل دیگر ادامه پیدا می‌کنند.
#اعتماد_می‌ماند
#۹۸سال_کنار_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/689300" target="_blank">📅 19:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689299">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9144a015a2.mp4?token=dSZZwHS53gT9USuR-n96jjtP0FLp_dlaHoNFuDbE6Yt6KM9TX1jwrXzTzVyIJ9k0xAx92gGEuaqUOklz3RN8gaoHGVLL92t6Alx3g4WlyKnZVLYvMIbqHA-IuhkcQ1_Nq4TocejLQdJWPwlqPju36qkCDoRE-aBIF8QHYpnqPTlMRd2_KYO2xh_q1txFuqCBa_1bBdM2wJz_AkRZQCdkBbQvAc3kSYS2-49462HGWwCJRKYXNVrWmWACxBXUekL8plIKuoLi-NgK33HMGDs0zN_uIXcEnhhJvc7PmTRtRSehibmUYcgwZ4JR39DSoSK6yvkRe_ClQ9QTqHpsx8IH6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9144a015a2.mp4?token=dSZZwHS53gT9USuR-n96jjtP0FLp_dlaHoNFuDbE6Yt6KM9TX1jwrXzTzVyIJ9k0xAx92gGEuaqUOklz3RN8gaoHGVLL92t6Alx3g4WlyKnZVLYvMIbqHA-IuhkcQ1_Nq4TocejLQdJWPwlqPju36qkCDoRE-aBIF8QHYpnqPTlMRd2_KYO2xh_q1txFuqCBa_1bBdM2wJz_AkRZQCdkBbQvAc3kSYS2-49462HGWwCJRKYXNVrWmWACxBXUekL8plIKuoLi-NgK33HMGDs0zN_uIXcEnhhJvc7PmTRtRSehibmUYcgwZ4JR39DSoSK6yvkRe_ClQ9QTqHpsx8IH6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرلندی‌ها با تصاویر ترامپ، اپستین و نتانیاهو به سفر ترامپ اعتراض کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/689299" target="_blank">📅 19:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689298">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q40E-N39Ziv3WHHVm47bcLaqzxc09wLeeLvkhO0faBsRgOu0Bqk-xMyJryY0rExRJJxtpVEODwP5cUWRyw8FXcPghJcqgxfl_4GEvmN-yY21_iAZbcHvm2FR_HSdZgGmYvC7kwvY8lRk5AMPux_8k64XBcIj6SFdRRKNo4hUmda44TRVv0Onp8dFqDHPhnTjTMcIo7eShldvabqTXMZ9-vkPMIo4qKOWq97fLU11rXbsPNlS7bpniYDjaWAx9z7o728WuwKcBPfOQd48ayXlnQtx8sF7hoz2M--j_V45Qh2vBDgW_msKlB4O_arFK_ZfPKGudAMkXgCXqH0ZDhXS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیگر نیازی به برنامه فشرده‌ساز نیست؛ ZIP بومی تلگرام دسکتاپ آمد
🔹
در آپدیت آخر تلگرام دسکتاپ می‌توانید بدون نیاز به برنامه جداگانه، چند فایل را با قابلیت داخلی تلگرام به صورت ZIP بفرستید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/689298" target="_blank">📅 19:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689297">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ee7015ef.mp4?token=sxz6f-wSu9ZpUl2saRPkwXGyNpEi3kBzZTpvAb-eOQkQ6ef30oCd8ZKe1SgrH33MlGSodTxPmnnoYacZUhAJ2LggP2COlDsLaaexjSSnyy7bdwyZdHIIjW4GrbUL6gKLrvnwEMFWI4Dxb3tYXBDGdXnl1fRWOAgZgNhkan30_3MaXCmUW8BXsRwjwIGyWXL9ETYZHI_To4-h1PvSave-zY3sdO1GERI8cgkdF_-FdxKLiHqkW2pRnRT2tny8Rm4UT_uhR53SW66HoOm_6Aa8CcktZmVqk09GqqopwtmZT52gC55Wi8oxqDQAr9JN21jCZ-qcWymHO4gIXt9l2HGYGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ee7015ef.mp4?token=sxz6f-wSu9ZpUl2saRPkwXGyNpEi3kBzZTpvAb-eOQkQ6ef30oCd8ZKe1SgrH33MlGSodTxPmnnoYacZUhAJ2LggP2COlDsLaaexjSSnyy7bdwyZdHIIjW4GrbUL6gKLrvnwEMFWI4Dxb3tYXBDGdXnl1fRWOAgZgNhkan30_3MaXCmUW8BXsRwjwIGyWXL9ETYZHI_To4-h1PvSave-zY3sdO1GERI8cgkdF_-FdxKLiHqkW2pRnRT2tny8Rm4UT_uhR53SW66HoOm_6Aa8CcktZmVqk09GqqopwtmZT52gC55Wi8oxqDQAr9JN21jCZ-qcWymHO4gIXt9l2HGYGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طریقه جالب جابجایی جرثقیل‌های غول‌پیکر؛ پشت پرده پروژه‌های عظیم چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/689297" target="_blank">📅 19:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689296">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: باب المندب واسه همه کشتی ها باز هست فقط واسه عربستان بسته هست
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/689296" target="_blank">📅 18:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689295">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj3Yz1Yq5QJhNVkO9R4r4tPTaOWDpopDBw8f-FLP5A_oVtGSWVaIk7ojEKZYfGpNYAGwpyo29dA891T4xTe4a2Agj_cysFA6UvHd02cNf7jhGhPStPkyc2tXSOm_4Oin3OpQl98pbRtfiqZVSw2F60LnVBnkzZYKfVLPgChrucMyMw7uDxbX54xC9hwMGjUiPX1CuiYunpWzIgNfXsD7BPBK1YL4fnPDkwRhNLAdPHI2pxQv7CTwM2ir_cFIjCvJ0MlF06RintWjkmjlIT51uLqxnxRv-Ibw_bfSMVjlyr9uLO2d0j7pSYeGVErmx7UKEk4e1m3a9zrMszrTIwRKhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا:
فقط در ساعات خاصی از نفتکش‌ها حمایت هوایی می‌کنیم
🔹
پرواز هر ساعت هواپیمای نظامی آمریکا برای پنتاگون بین ۲۵ تا ۷۵ هزار دلار هزینه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/689295" target="_blank">📅 18:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689294">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDjJrBn3QNDIMmkuzppphN_JOj4i5TxO1vDllWnjgKEsi-P7FgZa6eW4HFWqQriudLyXqP5Y3qIPaCla-f1EkJQg-qEBOlvAB49N_JvdTu71y3H12OLDj9madGPB94VEkma0cloQ-StChg5t0lI9K69ib9DdazArPyq04GjX5VEnxx110q0IDs0RMvOd33f8eDxxqFPnsn49K6PaYH2VxeX5JPYo8dMqz162AnYGz7-pG4J_V9ouAlpGbLJpWSVzWJZH8-DUC7Hgu8IRFyCdBlxPzRUo_NELCFk92zPziX6PQYCosRZ7bvoalibuZUrImOEinaNE4WPWvcmulQpaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو میلیارد تومان جایزه برای بزرگ‌ترین نبرد گیمرهای ایران
🔹
همراه اول پنج هزار گیمر را به رقابت سراسری FC26 دعوت کرده است. این تورنمنت در دو مرحله آنلاین و حضوری برگزار می‌شود و ۳۲ بازیکن برتر آن به فینال تهران راه می‌یابند.
🔹
قهرمان مسابقات ۵۰۰ میلیون تومان جایزه می‌گیرد و به نفرات دوم و سوم نیز ۳۰۰ و ۲۰۰ میلیون تومان تعلق خواهد گرفت. هر ۳۲ فینالیست هم یک مودم 5G با اسکین اختصاصی گیم و یک سال اینترنت هدیه دریافت می‌کنند. همچنین برای تمام شرکت‌کنندگان تأییدشده، بسته ۱۰۰ گیگابایتی اینترنت در نظر گرفته شده است.
🔹
ثبت‌نام از طریق اپلیکیشن «همراه من» انجام می‌شود. اطلاعات بیشتر و قوانین مسابقه:
🌐
mci.ir/mymci-gaming
http://mci.ir/-F8KLRA
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/689294" target="_blank">📅 18:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689293">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رئیس انجمن واردکنندگان گوشت: قیمت عمده هر کیلو گوشت وارداتی از حدود ۱,۳۰۰,۰۰۰ تومان به ۱,۳۵۰,۰۰۰ تا ۱,۳۶۰,۰۰۰ تومان رسیده
🔹
واردات گوشت متوقف نشده و از مسیرهای زمینی ادامه دارد/ علت افزایش قیمت، رشد نرخ ارز اختصاصی واردات است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/689293" target="_blank">📅 18:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689292">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad403794a.mp4?token=L2hrZ0d7xf45PLhmoYslGLDOjLEyFmEiB5Dt_DcNIj2ZxLBQIENNo6cg-y1x5ptEnyVdD2kSWEmSzzaNYtsMFzeI2jEbP-5ypQfVtNl2z6UuEv4ax9Dbh6nrujq9KAOd4cdunPHkwWmbTxSHIdfx5vErSgIAxfUjm9wNvrjHuPuMp3RXpzhcX6ZVooJMHd9nLpB5xGD96pSPOwVjvd7Rk-vubzXh2laxIRmazhVapLW88za9_Z7Knk0RIy2T6phvMmIJm5LlDKd7-pW6_3Ix5f3AsaWe0Vax755zO2FPGimsAB03FlrxtzFOlN1UPaH7WOhs3SGK5Ttefbdkvkx-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad403794a.mp4?token=L2hrZ0d7xf45PLhmoYslGLDOjLEyFmEiB5Dt_DcNIj2ZxLBQIENNo6cg-y1x5ptEnyVdD2kSWEmSzzaNYtsMFzeI2jEbP-5ypQfVtNl2z6UuEv4ax9Dbh6nrujq9KAOd4cdunPHkwWmbTxSHIdfx5vErSgIAxfUjm9wNvrjHuPuMp3RXpzhcX6ZVooJMHd9nLpB5xGD96pSPOwVjvd7Rk-vubzXh2laxIRmazhVapLW88za9_Z7Knk0RIy2T6phvMmIJm5LlDKd7-pW6_3Ix5f3AsaWe0Vax755zO2FPGimsAB03FlrxtzFOlN1UPaH7WOhs3SGK5Ttefbdkvkx-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: دولت براساس شرایط روز درخصوص بنزین تصمیم می‌گیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/689292" target="_blank">📅 18:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689289">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKuP3BujFyCToSR1RjwRVEMOxN-S2blHethwW-bKChyZvzecqiSZmLrGpLkKO-kfCRDjlyXS1AKtvxuJroN75zvcTYg46IYFdtkiwV_EmXst0tr2v6pzvfxalcOnGEB0cs-ZqByhLp-KQhseYJX2sh-d2RKbwRAYgvXmsxElLj3uPrjVwxwzHA5FKvUKxCuZlk0equ6TkgIQm-GB38-ErmdZd4SFPGFQFPbT5BHYMy4YDVUutRBzx0pyO_GSu9TgkILEE-qodjQSEXNnxvCY8WiYp2VmXsugw1SuPtWxUW4erjNMK-QJtrE-1RhF3i82hTWxXbLJJVFaBj_07DDdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXVxJQGgm5i8BwIIhH-T7J6j3iwDvG8li8HQ95eZs-HUe-CsZU6nd9o_AsitGxJLv-aJAq4iSkKTsOt4XeYLljOV5cg-8irW5HGRqGCasfq4PEonL0bwQ_Kmxu24biKL5Ev-l9Z4UUPk4FMNn4Dm6uzo0_IOI10tiELwmDvqenT2NqT8-XnwdW-gy-LS0EUSKHUV9uisWLI0WAqytDdTmnlBWaVe8VJ5zoUeYgeH8sfVZJc5xOHeloB4u1N6YDvgIsyuFU49xj0BdHE8m2MiLQdtGRDdHuh1xKVsIw5nix_C776fIGaJdW96fbo4Sfy3fpllKuQX5eDH_yq5E9DBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BF8jw1Bx00Hvz2jOBXKoRi5SA8PfbS-EiJOwU9mj3ddVXFA5mt3a1mLO42jqe3y1qm5RZbnX1NVk4J4sP_SpbsCltSG3cajxCrRh72SJFUJ9q9PI2pJU2V1IkkGaBYxjYkM7J6KkTBUj39FEQ6nQ96-9cvgxpGuqhafKCGcC8O3xxAex2DVmftkxhZAQ0ynZpDgPy2pAr9Q9WXIf4Xfxp4B7qsbWBmC9yu5JKC_NpQiVOmUoxPLrJrDeB-vrwg3NcTfgO1OZgOAHMgon7G1hWMxOwhJN-fZv4jAvTf_rLQhU3dG_GPyaNPDso_8ftJ3PmlGCa9XzxyW2R1C6oZXRRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر منتشر شده از کشتی‌ها و نفتکش‌های ایرانی آسیب‌دیده در خلیج فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/689289" target="_blank">📅 18:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689288">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khPzz5oGzHRkqr9nYtu0qBgbcIdINt16eEnMHEyRXSZG-tPq0bhxnA1YE1BwZZKKuYBLjiEMFBVYEllzHg_dEAH_exjOtxlNLNe9V_XzsFDxuq0tjnGanlpbOMVCF3lHUF04M7HliqT4xVrFH-Fa2vnZFICx5RW3HVT1q1TWbXxEULCPGNUS4ehFU76P6vcFy0aLbyTiSQ7DFwEto6QQRUTSKBK35iErykbSOF1saNS4crFPMPP4pngNjJmD0LRxjzv3iOsO0auhPhvbrjsI3ouulWCEjV3WwK-zJxyJZb3_3yte-gZFkfxt9j2wN4kGk4mmH-jLYuV4_K8dBeOgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همراه اول رکورددار رومینگ بین‌الملل در ایران
🔹
دسترسی به خدمات ارتباطی در سفرهای خارجی، یکی از مهم‌ترین نیازهای مشترکان تلفن همراه است و گستردگی شبکه رومینگ می‌تواند نقش مهمی در تجربه ارتباطی مسافران داشته باشد. بر اساس آمار بهار ۱۴۰۵ سازمان تنظیم مقررات و ارتباطات رادیویی، همراه اول در حوزه رومینگ بین‌الملل عملکرد بهتری نسبت به دیگر اپراتورهای کشور دارد.
🔹
همراه اول با ۳۳۵ اپراتور خارجی در ۱۴۰ کشور قرارداد رومینگ دارد. این رقم برای ایرانسل ۲۹۴ اپراتور در ۱۳۲ کشور و برای رایتل ۱۹۰ اپراتور در ۱۳۴ کشور اعلام شده است.
🔹
همراه اول هم از نظر تعداد کشورهای تحت پوشش و هم از نظر تعداد اپراتورهای طرف قرارداد، در جایگاه نخست قرار دارد و مشترکان این اپراتور در مقاصد بیشتری امکان استفاده از خدمات ارتباطی را خواهند داشت./ خبرآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/689288" target="_blank">📅 18:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689287">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
مهلت ثبت‌نام کاردانی به کارشناسی تمدید شد
سازمان سنجش:
🔹
مهلت ثبت‌نام و انتخاب رشته متقاضیان پذیرش بر اساس سوابق تحصیلی رشته‌های کاردانی به کارشناسی، تا پایان روز سه‌شنبه، ۲۴ شهریورماه تمدید شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/689287" target="_blank">📅 18:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689286">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8edd44284.mp4?token=KL4bJVxNczVd0mrMlnsfUiMr4kXOVuMlqRzf4Mtp6q49KykjBhLd0jFMW4bL32x2yvWWExdo9vzsEBdZ3r_7DCuUBY_w7q6ouetHhz136Oz_w6TL3ZzMcV7TeuoJv5AC-8BmZ22ZSFjlYFWIL_oQrpG8JIO2fYJL08xoP4qjG1pTIv-XKpPEGxAjMP1gUDiIVyTDkl4c4azN0sWtlbRnkTzMcUK1GhqsKY4TflaaKA-BbEDw11FDhcgqehjIUqBj1ZyPKlarSQqWH0SzZ2gZws_Hq_m-ONXXWCwgWsPaw98rOqpubDMQYNbNfuwv8W21kFeLGMQV9hVaa0xptiRhhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8edd44284.mp4?token=KL4bJVxNczVd0mrMlnsfUiMr4kXOVuMlqRzf4Mtp6q49KykjBhLd0jFMW4bL32x2yvWWExdo9vzsEBdZ3r_7DCuUBY_w7q6ouetHhz136Oz_w6TL3ZzMcV7TeuoJv5AC-8BmZ22ZSFjlYFWIL_oQrpG8JIO2fYJL08xoP4qjG1pTIv-XKpPEGxAjMP1gUDiIVyTDkl4c4azN0sWtlbRnkTzMcUK1GhqsKY4TflaaKA-BbEDw11FDhcgqehjIUqBj1ZyPKlarSQqWH0SzZ2gZws_Hq_m-ONXXWCwgWsPaw98rOqpubDMQYNbNfuwv8W21kFeLGMQV9hVaa0xptiRhhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا کنجکاو شدی وقتی دسته شیر آب رو بالا می‌بری، واقعاً داخلش چه اتفاقی می‌افته؟
🚰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/689286" target="_blank">📅 18:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aybXq_bX-B_-eFcC7DXfSugXt4HLLXvM4e7a1jxUQ6Fgdawyh6mloPb7GQ0GuIIWrx-4tZBSQYt-gmy40XN0_lpgp6EIdliFqOc5cXAjQ8g_ceYnP_6ftMRrKXS2SxHtj69KbPxJiMt9txiQdFNFgzudkQtKbfxKkiWMi3nMNUFGgoeDVJeEOOP-3klDuOIchFRNlx2WgOXVy_fY4a0rEXvDIpjicfpRyUTjGwFYLSfrFWdtXPlQVkr2pOdwbgGfidkU3wtvAJ7LI4QyT1jy01JGArBbD67b5qZBUdvP8LngtiiQYpIjmq9Tq4tNq6dwb_IshVzTkUprnhNev9Bkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه: تعداد تروریست‌های به هلاکت‌رسیده در عملیات ضدتروریستی سراوان به ۵ نفر رسید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/689284" target="_blank">📅 18:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689283">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d622c836f4.mp4?token=sMxQg1fzhtpy_8in4CjnHAO-1-aQIPlQiPHcHJx-z5o-hQQwPxt3yavDxpVgUnUJyDLvo5jRPJY4hfrlUOZ5DUDvcXZmO3gAJG0YnGsHAIYde1dFB-3Spa-1vQdyilgjdsfYtVrTeeyTQztQSdpoMZzg174zQ0f0dLJ0gB4CGMiP2JVkIvz1xUtK8Q_5mXOQcqoRMf3pekfhRhN5WWbYI4KKz-rBFzxp71xYYceBXBwPoIbBK3sFNyNUnrxYzGAabKOSgN-3bC73pfhOl6w8_Ovped7IrmsnxmdZQPfN4D_18e01yAXLzLdTPiGEnO221Fjd7_l-gZi1CK2hFEfFVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d622c836f4.mp4?token=sMxQg1fzhtpy_8in4CjnHAO-1-aQIPlQiPHcHJx-z5o-hQQwPxt3yavDxpVgUnUJyDLvo5jRPJY4hfrlUOZ5DUDvcXZmO3gAJG0YnGsHAIYde1dFB-3Spa-1vQdyilgjdsfYtVrTeeyTQztQSdpoMZzg174zQ0f0dLJ0gB4CGMiP2JVkIvz1xUtK8Q_5mXOQcqoRMf3pekfhRhN5WWbYI4KKz-rBFzxp71xYYceBXBwPoIbBK3sFNyNUnrxYzGAabKOSgN-3bC73pfhOl6w8_Ovped7IrmsnxmdZQPfN4D_18e01yAXLzLdTPiGEnO221Fjd7_l-gZi1CK2hFEfFVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوشته جالب تیشرت موتورسوار امریکایی
دو مدل طرفدار ترامپ وجود داره:
🔹
اول: میلیاردرها
🔹
دوم: احمق‌ها/ حساب بانکیت رو چک کن تا ببینی جزو کدومشون هستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/689283" target="_blank">📅 18:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689281">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgRIynlYI7HEAZAV98vSmOvuUdoMG5g9PMkABg8-SofpTNkeEldCgEatW5QwOoFQnWIgCwXECcTWFsg4_luiFhkOeXfgzUkeU-IXmUepXsIBKSKlSc7xk0pobge0g0frYkaM5QXkIiNeHytqz3-_VfaVPKJdDvHSw8mD8K9vRb8D2cD-t18Mop_qSxFOVkXI9gWUukWW9aVWa_dFWUWhaemjrsdAWuSLbqY3dpv59NVJFUF2ik8szNyRLw-88MhxrElITosnbvTFDTUZ_SB-yzHMK2Nr-3LO90Z2JIpytPSb8zTJGrprZePcSs3qHefuqXUQdIhSc32fKdSlk7B0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لغات کاربردی اتاق خواب به انگلیسی چی میشه؟ #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/689281" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689280">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بقایی: دوشنبه در مسقط، توافق میان ایران و عمان بر سر مسیرهای موقت تنگه هرمز به اطلاع کشورهای ساحلی خلیج فارس خواهد رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/689280" target="_blank">📅 17:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689279">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
عراق با پیشنهاد ایران برای تحقیقات مشترک درباره حمله به عربستان موافقت کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/689279" target="_blank">📅 17:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689278">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
انهدام تیم تروریستی در سراوان
🔹
روابط عمومی قرارگاه قدس سپاه از انهدام یک تیم تروریستی در سراوان و هلاکت ۴ تروریست خبر داد؛ در این عملیات ۳ پاسدار نیز به شهادت رسیدند.
🔹
از مخفیگاه این تیم، سلاح، مهمات و مواد انفجاری کشف شده و احتمال افزایش تلفات تروریست‌ها…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/689278" target="_blank">📅 17:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689277">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae86cf3f01.mp4?token=BqzjclRVDZtVEZ1WCau-wZSKfbRrSzgxSkyv0kRMfWVHbB6KKggWIa8lQ1oIEc1cGNp1Yj_8oA8YsaLZWOSJp8CtM5OQG87t7wAMQogc2gKjKBfNNah5G01vn6Qc1nQIpHt9huwzJ_vFz6BaD-QlXM0hrhSpI5kHOXqSc7uFFAeqjABORMHLBxHPuJHjIC_ya0QzaAnA5YoWRZw1FQs7qUVEDXkhv9fKWihMn9tsmrDERGd-vymN4Pxso53f05hFEqEaw2C1IKqYtV5UHBW0xbdU8myctYEZLSRP-5ACpX_nnWtqjOwnSQTWlgUoB9PxZBr5Fzxv9dUoFu7Nk4mjgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae86cf3f01.mp4?token=BqzjclRVDZtVEZ1WCau-wZSKfbRrSzgxSkyv0kRMfWVHbB6KKggWIa8lQ1oIEc1cGNp1Yj_8oA8YsaLZWOSJp8CtM5OQG87t7wAMQogc2gKjKBfNNah5G01vn6Qc1nQIpHt9huwzJ_vFz6BaD-QlXM0hrhSpI5kHOXqSc7uFFAeqjABORMHLBxHPuJHjIC_ya0QzaAnA5YoWRZw1FQs7qUVEDXkhv9fKWihMn9tsmrDERGd-vymN4Pxso53f05hFEqEaw2C1IKqYtV5UHBW0xbdU8myctYEZLSRP-5ACpX_nnWtqjOwnSQTWlgUoB9PxZBr5Fzxv9dUoFu7Nk4mjgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیدا شدن جستجوگر مادون قرمز رهگیر موشکی تاد نزدیک مرز اردن با سوریه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/689277" target="_blank">📅 17:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
بقایی: مجموعاً ۴ موشک طی ۳۵ ثانیه به لامرد برخورد کرده‌اند / ما قطعا این جنایت را پیگیری خواهیم کرد  بقائی:
🔹
شواهد و مدارک نشان می‌دهد که جنایت لامرد قطعاً توسط آمریکا اتفاق افتاده است و در آن شکی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/689275" target="_blank">📅 17:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
بقایی: مجموعاً ۴ موشک طی ۳۵ ثانیه به لامرد برخورد کرده‌اند / ما قطعا این جنایت را پیگیری خواهیم کرد
بقائی:
🔹
شواهد و مدارک نشان می‌دهد که جنایت لامرد قطعاً توسط آمریکا اتفاق افتاده است و در آن شکی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/689274" target="_blank">📅 17:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51dc103e87.mp4?token=Qlb7OD_SyB3PQccGP821u1C9FXdk1WoYiHFI5dwxCZTGBfAvKV6fOcsS49Y61O69vODkzCKZIa_QdQosX-_KFdbUgWG7uakFlU4BkOUcFqo-EcmhoszFYkogwrFBQIKzmTBM5kdsgJjbEsLT1PTuyRpV78lZcqa_HoVClGi8c13bXV6rOQxlMpAtyUjJp5VLGPHxvExFWOwLaxN3DcsLSqF9fHeZ5D6s9L5b1TcuH7CFZ43r-sm_EXSHkqB-VsPon4-1w8PcIjwAwqVedqAFB6i8lN66ps6y4K2NETX5k5EUgC-xs3hsHg81DVrJNrYutO9iVp3faAAWaqQa2mfFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51dc103e87.mp4?token=Qlb7OD_SyB3PQccGP821u1C9FXdk1WoYiHFI5dwxCZTGBfAvKV6fOcsS49Y61O69vODkzCKZIa_QdQosX-_KFdbUgWG7uakFlU4BkOUcFqo-EcmhoszFYkogwrFBQIKzmTBM5kdsgJjbEsLT1PTuyRpV78lZcqa_HoVClGi8c13bXV6rOQxlMpAtyUjJp5VLGPHxvExFWOwLaxN3DcsLSqF9fHeZ5D6s9L5b1TcuH7CFZ43r-sm_EXSHkqB-VsPon4-1w8PcIjwAwqVedqAFB6i8lN66ps6y4K2NETX5k5EUgC-xs3hsHg81DVrJNrYutO9iVp3faAAWaqQa2mfFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از تسلط نیروهای مسلح یمن بر برج کنترل تردد کشتی‌ها در تنگه باب‌المندب در شهر مخا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/689273" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
رویترز به نقل از منابع نظامی عراق: منطقه مرزی الطیب با ایران پس از کشف محل‌های پرتاب پهپاد بسته شده است./ الجزیره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/689272" target="_blank">📅 17:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689271">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVvaiSXacQaevVpbBDZsTwzngF5XJ-CY1354mFzeFSMgbcBZCdgj6BD6YySWnLxKTgwKf6jOTOzJ5pr6HlhUMvNaMbeXtTQ0Qp-jAW9UT2XKwvqAtU8Kz_c5cONMvwjbTG4VR-qX59mEE9kVXyukZAH44WW3kasY7Zo0NAmO33LHu7cTky9PvwL9YYLXvkQXdkvKsBO1qdTG9wZvmCMuUbrids3aRLiCiEih7iN8bPd7_pbmBf2fQ-T7c-JP0hJxO_Y9LMOtsZHbrq82vRAgvSFA8ePbE44-bBAODQTUNVBe2cth0sOnJf696Yq6UarQUoHCsKjg_ClYHVWW8f-qXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مایک آدامز
:
نفوذ آمریکا در خاورمیانه اکنون کاملاً فروپاشیده است
نویسنده و فعال‌رسانه‌ای آمریکایی:
🔹
تمام شد؛ از اینجا به بعد، کار برای آمریکایی‌ها قرار است خیلی دشوارتر شود؛ ترامپ حسابی گند زد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/689271" target="_blank">📅 17:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689270">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-RulKQ3NddOVfnDIU56xcE_obhqS_41QT7gFUql6qsCXPEKHyyZNdhwzNzQ_xfHrfegqrLioQ0LD9MC7FVPJXA0JPG9dpCar_BkShBK4aX_g6ApmoQgT6Qngd_LFKSt6xkuksa3It9KUdebd776aeLN3WTZ42AsD8IluAR-cF_GODGMNNojYVaKVHUGRFRDzj_pn-rRBQ8UV6YmYHeRkbSAxnRvJf768yAvGX_RGhPpVodWb6VSXTrYTS6KbVRUgW5FNaSOgLrn60moI91oEIynHWDoX05Ld_fEhdiUJDueg7TCpIoHdsSaLsrjX9GpCQWpdVVBnZ-V11TKeFdyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ملک اجاره‌ای دچار خرابی شد؛ مسئول پرداخت هزینه به عهده کیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/689270" target="_blank">📅 17:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGxXq8jTHDtqPOzB1OQOG73v2LgNxzv8QFYnXHppZl0Tn-o5XeBz-Sz4rTThUyAGPZnXHE7MHM-Sge8mrSZLrSmE-b-2r9aMp2wODikhV4UvzH996mUECLoI55vZwrl8TKIp4RRkW2NmTf5lAaWvgcnyWMKaNHoHcaCbtRF9Y9hAxDpEvavcuVz1UvlVKYRbG8xENLNTSgTsTWokaKH4mEUerX_V-TWHDA1tmzq3K5YnEi1DByRCme0HktHeRYP7G8-FI3ftboV1ZD0prGY3afvZ4Ge-kfoN4nxqIoDd5JHmBl7T0CWcyfkglw4yZFRdlU2vDJj5D3jpbwCDQs8p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اجرای عملیات اضطراری برای جلوگیری از بروز خاموشی در صالحیه و گلستان
🔻
مدیرعامل شرکت توزیع نیروی برق استان تهران از اجرای عملیات اضطراری احداث ۳ فیدر فشار متوسط از پست فوق‌توزیع بهارستان برای افزایش قابلیت اطمینان شبکه و جلوگیری از بروز خاموشی در شهرهای صالحیه و گلستان خبر داد.
🔹
این عملیات با حضور ۴۰ اکیپ عملیاتی و طی ۵ روز انجام شد که طی آن ۱۸ کیلومتر شبکه فشار متوسط هوایی و ۲ کیلومتر شبکه زمینی احداث و ۵ کیلومتر از شبکه موجود نیز اصلاح و بهینه‌سازی شد.
🆔️
@nabzeetehran</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/689269" target="_blank">📅 17:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689267">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
مهاجرانی: فعلاً تغییری در نرخ و حجم بنزین سهمیه‌ای نداریم
سخنگوی دولت:
🔹
به‌محض اینکه منبع مالی پایدار برای کالابرگ تأمین شود، مبلغ کالابرگ افزایش پیدا خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/689267" target="_blank">📅 16:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689266">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQrDL3Xl60SQ2hNQ48xyeWAlvlrKyD9Y16CKdBaoXOXJC6nxb4L2kAsenMrrZlpPYA2Dq8ZbSrx3Ah0zUIp7dI2HpW0U-3SzgQCCY3q2XbD5Vn6kV5rInwm35S50iqfKoUJpmDncdzH8xfYsT2vBHrKGpL0D3hzPq0ipXk_ys3kT2NDxhSD7oCwc8FMgZi_gUXsFrbaYUiJ3SYc48k3aF2tBmE7mSgWr5zviVBnFCvLRNQd5BKmP_cNkjkKRVTHKkyjF0Tti-jtYSOu5Z6Mypnj30mkexqneJ70fcpoSRz42DqZQKwLgVsmYEEMdIzvwmwvw1ntI06M4Ah65M-u85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای کامل از بین بُردن بوی بد در خانه
🏠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/689266" target="_blank">📅 16:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689265">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
بحرین اعلام کرد که در نشست ایران درباره تنگه هرمز شرکت نخواهد کرد/ همچنین طرف هیچ‌گونه نشستی که ایران در آن حضور داشته باشد، نخواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/689265" target="_blank">📅 16:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689264">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
شایعه توقف پروازهای عراق تکذیب شد
سازمان هواپیمایی:
🔹
پروازهای ایران به نجف و بغداد طبق برنامه در حال انجام است؛ فرودگاه بصره به دلایل داخلی عراق بسته شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/689264" target="_blank">📅 16:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689263">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
حاجی دلیگانی، نماینده مجلس: طرح سه فوریتی را برای خروج از NPT آماده کرده‌ایم و بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/689263" target="_blank">📅 16:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689262">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4b31107.mp4?token=ifa_v__xdEpY21UP16yhmMDCu8AoRFHi-AgEvMaVN8hyCOJb-ijK2pSwoD-GqhsyaNJ2WAxeBYLkPXons3Xbl21_wwVD3pWv4bJH3XWvPaF8Pnq230C02ER-s1L0AMUDhXeTmkncgM5BP2L_QBiYGau5EYDoT390LXhjTq3JoRwPAnpBExvnty3JKy3XMap45E1IC-vg11KkFNomTUeRNI4eZpijPo6D1H4w4G_FLwkfAa85Xh6Cffe6FsXuEhBjqIEwAHpAatUvddAGg4GiQxQj00g_Qh79yzNOhk-lvvNkF8_9Sa1dnt1yPv1orBBbSCiFRktNcbtlMRtylX7OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4b31107.mp4?token=ifa_v__xdEpY21UP16yhmMDCu8AoRFHi-AgEvMaVN8hyCOJb-ijK2pSwoD-GqhsyaNJ2WAxeBYLkPXons3Xbl21_wwVD3pWv4bJH3XWvPaF8Pnq230C02ER-s1L0AMUDhXeTmkncgM5BP2L_QBiYGau5EYDoT390LXhjTq3JoRwPAnpBExvnty3JKy3XMap45E1IC-vg11KkFNomTUeRNI4eZpijPo6D1H4w4G_FLwkfAa85Xh6Cffe6FsXuEhBjqIEwAHpAatUvddAGg4GiQxQj00g_Qh79yzNOhk-lvvNkF8_9Sa1dnt1yPv1orBBbSCiFRktNcbtlMRtylX7OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از روی دود اگزوز، عیب خودرو را تشخیص دهید
🚙
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/689262" target="_blank">📅 16:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689261">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-rJZD2mO3fUDWrH3-9ptx7J9_7s3lijlIgRUP9ukOY_LfIZyiSq341iJdCl47yzE7zBZLsXxEckSPP5Gy-WTc6jn1sRULHfzB5ljDlRGbvamC9MMmkPqRHw93n9xG3wMnGrfO7YOhh0zm33KE2F0wmHHJnomUq7bfvyRKWUxypZteesmcboG0OcOgcAvOkGuxSg-3d5i5wkHKyLN8p0RF9_569oEg-dM18tvZTWb22pm_fG87CTkB8ykXmNytsoVg6FOZV6H05RFSTWfcM9dyNt3O9veC3c6bUAh7NsVKoDtPTQlOLSC6Tp558NJttmDdxiNKyW23oulcC7vdB_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره میدان ولیعصر(عج) موقتا تغییر نمی‌کند/ آغاز ایمن‌سازی دیوارنگاره
به‌دلیل انجام عملیات ایمن‌سازی، دیوارنگاره میدان ولیعصر(عج) موقتا با اثر جدید جایگزین نخواهد شد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/689261" target="_blank">📅 16:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689260">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر انجمن تولیدکنندگان مرغ گوشتی: ۶۰۰ هزار تن مرغ روی دست مرغداران مانده است
پرویز فروغی، دبیر انجمن تولیدکنندگان مرغ گوشتی در
#گفتگو
با خبرفوری:
🔹
برای تأمین مصرف داخل و ذخایر استراتژیک، حدود ۲ میلیون و ۱۰۰ هزار تن تولید مرغ کافی است اما در شرایط فعلی ما حدود ۲ میلیون و ۷۰۰ هزار تن مرغ تولید می‌کنیم که بیش از نیاز کشور است و این مرغ مازاد روی دست مرغداران مانده است.
🔹
درحال حاضر مرغداری‌ها در ضرر شدید هستند و خیلی از آن‌ها ورشکست شده و از دور خارج شده‌اند و با ادامه این روند شرایط بدتر هم می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/689260" target="_blank">📅 16:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689259">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPl9FGAluc3FXSx_W4Yt2zWyTE5a3sAp474qKiPX5Z7x3-nCA2M55LWmks04OIh8lzU64_R0VwKj4R0T4ipsz85K2nUGFn_IypeE9jcLzb4I1YyD2KCoOTEsj-5Ku3rvm3OQdBOxaVxfnPlk7GrrsuJiDnQCy3cU9YefOyRBgwb_STyVHCBFPSdAKwecgrc4_tVz-lJK_WAR-_TS5CjHhdMusgCz1OpCVWuYMNfNbaF64hHx1LcLhEB-MCa_i-N6ZsMNgBefo1RBAjhfSz8wWes06tQv8drOGMwiXHbVhMl4C3DGmHKnClSelRJKJ4RdVRZ4TQo2WhfSHyP3YRjXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ که این حرف‌ها را می‌زند، ظاهراً ماجرای آخرین درگیری با حوثی‌ها را یادش رفته؛ همان ماجرایی که ناو «ترومن» مانور گریز داد و یک F-18 آمریکایی در دریای سرخ سقوط کرد!
به توییتر خبرفوری بپیوندید
👇
https://x.com/Akhbare_Fori/status/2098737810995806411</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/689259" target="_blank">📅 16:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689258">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تحریم به ارسال مقالات رسید
🔹
معاون تحقیقات و فناوری وزیر بهداشت، با انتشار تصویری از صفحه محدودیت دسترسی شرکت Salesforce به دلیل قوانین تحریم‌های آمریکا، از ممانعت کاربران ایرانی از ارسال مقاله به یک مجله علمی خبر داد و گفت: این دیگر تحریم علمی نیست، جنگ علمی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/689258" target="_blank">📅 16:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689257">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سی‌ان‌ان: قیمت گازوئیل در آمریکا بیش از ۵۵ درصد افزایش یافته و در برخی جایگاه‌ها به حدود ۹ دلار رسیده است؛ در صورت عبور قیمت از ۱۰ دلار، برخی تابلوهای پمپ‌بنزین امکان نمایش آن را ندارند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/689257" target="_blank">📅 16:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689256">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z04UJt_f5gvjn3A3iovJAC2co4LYYh608mCbQVMDkoky3YHMCjdoLhAQ5vxz9OeFuOH1cLhuFe6iu-eU-tZd4gfZ9X9Z3DaIt5ymS1WxOZ98sa0tkwSwLIZLh0XQOTpCSBOz8uYthgYItD-8dFtmp7tYLhPaiwbYKmHZXnMrFZ-cVxlMyjFY7TgA2aPYroxnPZneW5nOPg_oCAhVV3pvyf9mSQUydvPQw5kpOy-6RprgfzZTg4BpwlI_22odHmCAeABJW_pPFfndcnjZEySa4Tqe3zGUjQzpyR6lxM-si7A1ZTWtyrUIHMGYalvvh_9DDpPiRDfoClhUf_1Y2ijB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرداخت خسارت خودروهای جنگ از ۴۰ هزار میلیارد ریال گذشت؛ منازل از امروز در نوبت جبران خسارت
🔹
رئیس‌کل بیمه مرکزی اعلام کرد تاکنون خسارت ۳۵ هزار و ۸۴۱ خودروی آسیب‌دیده در دو جنگ به ارزش بیش از ۴۰ همت  پرداخت شده است.
🔹
همزمان؛ پرداخت خسارت اثاثیه منازل آسیب‌دیده از جنگ ۱۲ روزه از امروز آغاز شده و بیمه ایران روند رسیدگی و پرداخت پرونده‌های باقی‌مانده را ادامه می‌دهد.
🔹
بیمه مرکزی تأکید کرده پرداخت خسارت‌ها بدون وقفه در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/689256" target="_blank">📅 16:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689255">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
خبرنگار المیادین در صنعا: تردد کشتی‌ها از طریق تنگه باب‌المندب به‌صورت عادی و منظم در جریان است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/689255" target="_blank">📅 16:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689254">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سخنگوی سابق وزارت‌خارجه آمریکا: ما دقیقا می‌دانستیم داریم مدرسه را هدف می‌گیریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/689254" target="_blank">📅 16:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689253">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f796d356a.mp4?token=YfapI2Ne_5A3pSUWOetXn1gxlOmLOp5-yT2kwblFVWxn4QRhoo0uWCMpXhvPo_WoaZJ-iCcDrqPlwtPpKjY1khCLURrTxNNSOBOjal_9Kwdw3g8juNV1uogirP08JWy4o0lolzhUZjnbGc3Y_y0fQsOdIFi7wXnqUMInUfzFbnZlxN6X-W5eltppRwirx-qwnncl9p_yxGptPuKANvUv1bC_2Z7ENMxJCjZsLpOTevfqgbl58CQ0xMDMDaw7dptOVtg2TBPotgbkb81YdTKRux0do3qE1Y7xmefyb1lBUNePltL1iItGGEEsCKRUYP-0quSNpw8-xt63b63KSvPPbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f796d356a.mp4?token=YfapI2Ne_5A3pSUWOetXn1gxlOmLOp5-yT2kwblFVWxn4QRhoo0uWCMpXhvPo_WoaZJ-iCcDrqPlwtPpKjY1khCLURrTxNNSOBOjal_9Kwdw3g8juNV1uogirP08JWy4o0lolzhUZjnbGc3Y_y0fQsOdIFi7wXnqUMInUfzFbnZlxN6X-W5eltppRwirx-qwnncl9p_yxGptPuKANvUv1bC_2Z7ENMxJCjZsLpOTevfqgbl58CQ0xMDMDaw7dptOVtg2TBPotgbkb81YdTKRux0do3qE1Y7xmefyb1lBUNePltL1iItGGEEsCKRUYP-0quSNpw8-xt63b63KSvPPbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کینه شتری ترامپ از ناتو بخاطر تنگه هرمز!  ترامپ:
🔹
ناتو نمی‌خواست درباره تنگه هرمز به ما کمک کند. پس چرا ما باید به آنها کمک کنیم؟ #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/689253" target="_blank">📅 16:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
کارشناس قطری: ترامپ قرار بود بر تنگه هرمز تسلط پیدا کند، امروز نه تنها بر هرمز مسلط نیست بلکه تنگه باب المندب هم به دست متحدان ایران افتاده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/689252" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e33b0ddbc.mp4?token=ndn7oiPYZXGOoJ3_Det7KRkMC_K3G86p6HARsYj2Z1FjOI6YSDTIa8yLkBWGL2z_VzzkMDW4ev2_GImjWMWDVWJUY9xDPpkNy0LWNkBORlAtsGMX92HP1GQ9uO9_1Q5thnviIhcJYGyMadewUVjSnjlUiUlOB_xDLzpZpjzPsZPFPzlvqm5CVlTHrkAZUKAzBo-D0i7SP7lomlO5CmcUnobCksWHmgtVTIYtLKFlS9Cl_4YIfC0f6ZhQytFPu0oKzpcjW6-LbEU2EtxdjGJpbQjdL2Sas0VMTXGtN4uHiz0in77qppOkQCmkwC4Bb2x79oYZMqrSuLI7fl3WGYer8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e33b0ddbc.mp4?token=ndn7oiPYZXGOoJ3_Det7KRkMC_K3G86p6HARsYj2Z1FjOI6YSDTIa8yLkBWGL2z_VzzkMDW4ev2_GImjWMWDVWJUY9xDPpkNy0LWNkBORlAtsGMX92HP1GQ9uO9_1Q5thnviIhcJYGyMadewUVjSnjlUiUlOB_xDLzpZpjzPsZPFPzlvqm5CVlTHrkAZUKAzBo-D0i7SP7lomlO5CmcUnobCksWHmgtVTIYtLKFlS9Cl_4YIfC0f6ZhQytFPu0oKzpcjW6-LbEU2EtxdjGJpbQjdL2Sas0VMTXGtN4uHiz0in77qppOkQCmkwC4Bb2x79oYZMqrSuLI7fl3WGYer8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کینه شتری ترامپ از ناتو بخاطر تنگه هرمز!
ترامپ:
🔹
ناتو نمی‌خواست درباره تنگه هرمز به ما کمک کند. پس چرا ما باید به آنها کمک کنیم؟
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/689251" target="_blank">📅 15:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb966b696.mp4?token=oqpyS-afJdebVR7E2l4ziBswtaDD9n8mjRcl-2ZG3LyEE6YQAcBtvAUtTslrt_b3xSxqzubWo4ZuzVyFx3k0kdQ0ex3YebmWcZvvFz5TruUo9Am_h_db-BdTdiCj6V1dknRWA2vfoWGM8f_bQvREC4ycapqFxcrZWPzErcofIanr6ldeBB98WcljanrprpmzxGSc9S56XtC2TfxGZ3AY8axnA_lPg5L7gTcOXtlXYyhtubeqt3L94ciSniSgVsZ-7u8H01Pmiv4vmzUcpHgpNYNPSYUjR6Kg-Evu7kjxErN4I-KSMpN4k9UHCvQFjhzUx5ZRPIqQ4osSy4ykyU0kqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb966b696.mp4?token=oqpyS-afJdebVR7E2l4ziBswtaDD9n8mjRcl-2ZG3LyEE6YQAcBtvAUtTslrt_b3xSxqzubWo4ZuzVyFx3k0kdQ0ex3YebmWcZvvFz5TruUo9Am_h_db-BdTdiCj6V1dknRWA2vfoWGM8f_bQvREC4ycapqFxcrZWPzErcofIanr6ldeBB98WcljanrprpmzxGSc9S56XtC2TfxGZ3AY8axnA_lPg5L7gTcOXtlXYyhtubeqt3L94ciSniSgVsZ-7u8H01Pmiv4vmzUcpHgpNYNPSYUjR6Kg-Evu7kjxErN4I-KSMpN4k9UHCvQFjhzUx5ZRPIqQ4osSy4ykyU0kqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: ریشهٔ مردمان زیدیه شیعه در یمن، که امروزه انصارالله یمن را تشکیل می‌دهند، به مازندران و گیلان بازمی‌گردد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/689250" target="_blank">📅 15:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689247">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9207a3b1ca.mp4?token=aQDU306H5rg4i7ixnpOYqDHJZ0voVD0PviWCqt-MJ4vbJYXUAzmsRdxppjhkWLAb4T470PTr7DVdDKd9ShomIDn4TYp70fAAy3L9QloAVmJ1rsyoMeI6qZJI_blP0DYvhbOwr4ThbEkrzHrVlALkWL5QisKZ7fSct4LKirFC6RKeXTSoxVwO4NCcpE5mNfq_WFl5hmeBjBjqHtXMHKIJS_ZO-OBne_0B7e0YYqLbRVRYUasy8SnbRhhQpU1fzp9utbjsXcdM2h2UTxkfrxN8YbKBoSHe6-R6VBnB_ZiXt1bK5XefGRY_4TEt_VX0SBtswtQphmTcfLIKh19FQgvoADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9207a3b1ca.mp4?token=aQDU306H5rg4i7ixnpOYqDHJZ0voVD0PviWCqt-MJ4vbJYXUAzmsRdxppjhkWLAb4T470PTr7DVdDKd9ShomIDn4TYp70fAAy3L9QloAVmJ1rsyoMeI6qZJI_blP0DYvhbOwr4ThbEkrzHrVlALkWL5QisKZ7fSct4LKirFC6RKeXTSoxVwO4NCcpE5mNfq_WFl5hmeBjBjqHtXMHKIJS_ZO-OBne_0B7e0YYqLbRVRYUasy8SnbRhhQpU1fzp9utbjsXcdM2h2UTxkfrxN8YbKBoSHe6-R6VBnB_ZiXt1bK5XefGRY_4TEt_VX0SBtswtQphmTcfLIKh19FQgvoADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبران بریکس در دهلی‌نو نهال کاشتند؛ نماد وحدت و رشد آینده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/689247" target="_blank">📅 15:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689246">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ ایران به فینال آسیا راه یافت، شاگردان پیاتزا کانگوروها را هم شکست دادند
🔹
ایران ۳ - ۱ استرالیا
🇮🇷
۲۵ | ۱۷ | ۲۵ | ۲۵
🇳🇿
۲۱ | ۲۵ | ۱۷ | ۲۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/689246" target="_blank">📅 15:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689244">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
آسیاتک حتی در شرایط جنگی خدمات خود را توسعه داد!
محمد بابایی، معاون کسب و کار آسیاتک در گفتگو با خبرفوری:
🔹
آسیاتک حتی در شرایط جنگی سعی کرده است که زیر ساخت های خود را پایدار نگهدارد و خدمات ارزنده ای را ارائه بدهد .
🔹
آسیاتک خدمات خود را حتی در این شرایط گسترده تر کرده است تا جایی که در زمنیه فیبرنوری نیز در ۱۰ استان کشور خدمات ارائه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/689244" target="_blank">📅 15:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689243">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dba894d91.mp4?token=JK_sWJC4ThVf0pWC7cpXWKc8wxHnRcADPN-YZiGZoK5E-O_bOVtRdNfsGLa3rVytI_Tn33BBEeUnTJMwTjQzSHUVx-zvsI4ra6XAFrXIEDuUKdW2zjPv8DuU0k9hpXZszsyB-RJphKENb76Gj3rhIFKUFCFZrCzweWeaMvtjQhAQNy3aqHCJT79odxIBF4BKewByiiUXPPfKpYJfXfGjBnCszaU4b__q77S50NMVmUqKeBg2z1sw8bGRdbKt4YEE6-TSg_7-xOHHzs9SVai98Z9jtqXUj_H7_MR0ZOiQx9K6rnFNiZj5DGWGAH5Y3rAn5XtYKI5UkH4cP5iMZLAkLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dba894d91.mp4?token=JK_sWJC4ThVf0pWC7cpXWKc8wxHnRcADPN-YZiGZoK5E-O_bOVtRdNfsGLa3rVytI_Tn33BBEeUnTJMwTjQzSHUVx-zvsI4ra6XAFrXIEDuUKdW2zjPv8DuU0k9hpXZszsyB-RJphKENb76Gj3rhIFKUFCFZrCzweWeaMvtjQhAQNy3aqHCJT79odxIBF4BKewByiiUXPPfKpYJfXfGjBnCszaU4b__q77S50NMVmUqKeBg2z1sw8bGRdbKt4YEE6-TSg_7-xOHHzs9SVai98Z9jtqXUj_H7_MR0ZOiQx9K6rnFNiZj5DGWGAH5Y3rAn5XtYKI5UkH4cP5iMZLAkLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین سیمایی‌صراف وزیر علوم: چرا باید پول دانشگاه صرف روزنامه و خبرگزاری شود؟/ چرا عده‌ای مدام دانشگاه را می‌کوبند و باعث التهاب می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/689243" target="_blank">📅 15:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689242">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkZbAN-iUOe08-Fxn1-RoNfCFoPW-XxhYs0DNhwaoeJ6iGxumDULsmLtJTwoLVKvrg61bjPHbl4qfhF1gMEkuvLR0Hig62Nh08vPJZXDUsr5fOKpvHve0gOjg9eURxULOCpelHH-sklAqS5tb2JwB899cg6GCBpiYnieeDi9DAAReHSQdfiBnyg-Cy7nRmShtvfmm05MC69lSdKM2Wy_Uzi-WVthf2Cmm3yIbySjR5M-6C0tIM1dkdolW4Jvvfi_KHD_zNCyIrDCb2I0Z1wIxz1eqtAK1Uut_P3DSE44s7moYKlDCvH_ajyaM6S9j0ZJVPGv7-mDoBJQ_pWhu-Mbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ در مورد حمله به خط لوله نفت عربستان: به احتمال زیاد ایران مسئول این حمله است    ترامپ:
🔹
جنگ ایران خیلی زود پایان خواهد یافت. جنگ ایران احتمالا پس از انتخابات میان‌دوره‌ای پایان خواهد یافت./ حوثی‌ها نمی‌خواهند با ما بجنگند‌‌. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/689242" target="_blank">📅 15:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689241">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde8b54263.mp4?token=uq0fzHFP9Olwk-tVoQLqOsq2J-YMFcYX6sFgE4Ufe8He06K1L9BEiULcifIu8MFumOScG3o2mVA5XZEI9VphgmgZvlsFbiC0olYod3llriO_O_vy8yee4cvg4ZCWpgrUmhv6t18nUKqQj_tFM4s3jHA6n5AlK4cIgMIcbqO52GuH1HRnLutx1C1xmpMCmq6J_py0ZU7qy-8mN1qZrCm5Ou_yRDVGw528Oh4MvCRsHQX7pQh70Jb8i1ej1u9Qh_P0vR9KF3O_JLasxjFYBXPaa88zjjPSIyQ8W46pdFsN2NHbfA9uq53-r3bmjqBMU-zoZfMjSASo2lRXNJ_Ct526Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde8b54263.mp4?token=uq0fzHFP9Olwk-tVoQLqOsq2J-YMFcYX6sFgE4Ufe8He06K1L9BEiULcifIu8MFumOScG3o2mVA5XZEI9VphgmgZvlsFbiC0olYod3llriO_O_vy8yee4cvg4ZCWpgrUmhv6t18nUKqQj_tFM4s3jHA6n5AlK4cIgMIcbqO52GuH1HRnLutx1C1xmpMCmq6J_py0ZU7qy-8mN1qZrCm5Ou_yRDVGw528Oh4MvCRsHQX7pQh70Jb8i1ej1u9Qh_P0vR9KF3O_JLasxjFYBXPaa88zjjPSIyQ8W46pdFsN2NHbfA9uq53-r3bmjqBMU-zoZfMjSASo2lRXNJ_Ct526Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر مدل ماکارونی کاربرد خاص ‌خودش رو داره که برای یک مدل غذا ساخته‌شده #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/689241" target="_blank">📅 15:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689240">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: ما تنگه هرمز را به‌طور بسیار قدرتمندانه کنترل می‌کنیم؛ هیچ‌کس شاهد وقوع این اتفاق نبود
🔹
ما به‌طور متوسط روزانه ۲۵ قایق را از بین می‌بریم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/689240" target="_blank">📅 14:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689239">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e03c587a6d.mp4?token=E8aN_Z5GN7OcG41Z9hfqxA-yJ9Afk_g1PeVxHWniZHIl7ukxZFIKdXOVXyby7SphQt9UFynB4suz2LwR53Be8k_bYmPWryWFLoMbr4Ei553GGY5IQSzV6OibxonwnIcH6Qj6FQc1OkoY-s0cJbwE747juq2dzpAS708eHUxB8kclAX_vWa_YzWe_qzSzwm5NDhsTFk5x93rG7xzUmwFZEpTD7Ciq1KWsKguiENUWt0n8IE_euWYJCr15MVLLCLcTlQwVBWcplLoyLUnKFKERHCK76_lRSUnzcnFhB6ABfTmhcAa7knVVRi9B_WV26gK5OkywN9P3UAprdH1lGFr_zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e03c587a6d.mp4?token=E8aN_Z5GN7OcG41Z9hfqxA-yJ9Afk_g1PeVxHWniZHIl7ukxZFIKdXOVXyby7SphQt9UFynB4suz2LwR53Be8k_bYmPWryWFLoMbr4Ei553GGY5IQSzV6OibxonwnIcH6Qj6FQc1OkoY-s0cJbwE747juq2dzpAS708eHUxB8kclAX_vWa_YzWe_qzSzwm5NDhsTFk5x93rG7xzUmwFZEpTD7Ciq1KWsKguiENUWt0n8IE_euWYJCr15MVLLCLcTlQwVBWcplLoyLUnKFKERHCK76_lRSUnzcnFhB6ABfTmhcAa7knVVRi9B_WV26gK5OkywN9P3UAprdH1lGFr_zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر قوز گردن، کمر و یا کمردرد دارید، این حرکات را انجام دهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/689239" target="_blank">📅 14:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689231">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvNrLI1k4GHHGg1bA2u3RqvVHiYHA9GxA5d-Tr7VKiw65uxDwV4CGUJYd7uX8LzfjQ2Icbzx74R6sdlp6FdQWWkkJjMZRQ3Y9H40w9p3wmNm3YYRdAnji2B1CLm4h1tBQ6wJkL2eAUwjFsWBXovqKzLwyZUKO3OrVbMsJbAOEnYnm6EIDzZUGR90KIReRZQfAj5aYkWEMV-5TytTg44hEP4eKYCv_eBB0w9PNOEN7f1rd115RdxNNifGpNHptxBOKAr976OKNgHKpo6nowHZBXLGiCUBtDEQta-MkmhjQZSjW4Bbsrox1r11KTT1xukSG7O9ornvXNPcxwJ1rgTvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGM2062NcRWKbiXnAtlITmVYTEhuYKbXHRcjVZUXG3uOAqZLf95-gqzoJZqvFqIFUKkygjOiSPg-ynCD39oRRpD8HbCPIopp0WqtGqWc5TrsXl66aC2f3fXn56bgzkWW1b1yq1QW0ewiXri_vfpS50z90YLemiNvNHhUwKmLli240gVhwMBJE8yLstxlvaJ_J7E1b1SCe1a4bEfsh4iQZIM9fFU4_5Yty2BEvdksYyxrO6sfRDDRjaC1B18cGRHNxTiJ1Q0KzrjpsAy9XBqPxQOYSYw27ncKuASvWXnPgZBHZI041atWDv3d0TMtlmrhFQHJjoQatfXmBKd3Tsz37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAn65miqJirCWjDamfYdpAcB0Xqa52R4AxkysvZh6HSeQbmJlJ9s8UKsMIzdDbYMEVk9-0y0Ac8Ba0GLPUzoyq1ZrrQclbtCK_uH4S3ATWUetX_u3qLXrKXoZ9IkImw4gOejHJpBblaVwvMnnCMYbnSzqDS0UPTmopkxAStbk_uxz28Zit0TTmkvuID2kqubVQorQAtqja80I5lKUYFEpCfQJ1zqPB3la-Zglmq9y7rXaQHpeDtgN33tSpN_ugmoX-QQS1zz8nJfX9QwSTsvSnJM1f-nFI3oy0LzbxWcyzDtSOWu8-v42F0XZsHxucP-77929Vf4fTzeEHa6rNrIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfC2HbsBV4CdcxjBkDRwlj4EOCe8pgBfffMC1pCjamXu_sNVhuV-IvmLcKLFr6CNcgxlPHHIYHGQOJobKuhu3zvxVA3qRk9YMUr32Fuq1hpaqqYUJ45sAW9GndL7D0OApulcqL2Q-wal4pEI4a_EA81im7jF07vWVPrScXDu_oLfu07Wymu2HfmA6WYEJh38up0o665kB8KXBgD0y2Crag1QKkjbSGdaM9Wt175pM-RRwV9HVY5lnxagtIH478yDTNwIn06NtVOCb3JaIZ0rFSQ3f_N94aHIN0fXpmHMeI2ENLnydZrqPfq0BOagnO6N-kTrC6AzO12NvMk8SVy4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXENHTgriuR48g_DiRG79VWR3adnc7THvAnu7jJAadhjC6LjWMDomx90EIMrzItta68oC7iDGDwSuTmaMQ-PEvY8Xmng2mL151cQry0qn3jDdPXeOqyWf9xRiVSeMZ1qWYelNqb6m8XTtHCgBaZKnXfSOckwYVPvIqI1cQE9f3uh_uZYPwFnzFDn2jjVlR1_XZY008vdfmna8_90fx8awJCbQaR6JwtN0Yjvpk13BMhYf4tdHowzYcPo-NwcUqBiqySsdvxLK0bHCl3rx5GJnN3r6sts9QvrRDPUMadK4h7My44R8rwIrZBtMdMe2MNW_bVpatF7O4v-9IK8nWY-Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQfL5UvJvdqBpSFp34UKvCCRr-Oc6cNk_QeyHRzLn_7X8fbN40GGXtvq79OeMc5BhMn78O-Cuxb9tn8eNbJFfLdbsuVD9Wti2gEb0bI3tziYRU3yB5CoC8whga7qdIB0BNrJqPdzqKtMc7Z3mbhlHbyZZ8MDpo5utxG-sG5boICSRMtkGpeJd3mdD4GQO-g9t1RYytaP-rX1i-0NuRVTBKwSuU33DZ0MYDxQrhbNA76clR9Cnpc5sP3BygYqNRZ7ryLwGLMpJrKHfc3WR2AWvkRrQdTM_qrUuYPBzdZGmCJVa8NbUcHr2mpECbP5MAinhu5W8JtHJvgDz9qQQdooLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XV7LOOUuHkyZOYgoJIUPDWsJJAkBUOGkPf4NFXjmnQ1Gr2D5ug2YDwy-yQy45jozm-x0CqqeN_1se3D2fSR0RyS7JrVziIVWp0MnwGDMJN5GdxaVKciA_Aj8LL45dIV79uI6l5fJ0EAT86a6AIIauaUunexfI52lihPJPVCGu_3p_DEW9zBzw9riL7BQAIIapV0PPgTT1-XyO0x2I7cbpPNM-Zlrj-1LOONJgBHacG_YZ9I1G6g2cWf3Bt6F-5e3I5AkvmoOrf-u2Bx-FyI9obDTwl_8cffVlQ-4VKPAUyt0oYEJe-R7w2snzBWpSwFTQ-t60QiuBzeMV0CLWM6jyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZyJMNoiCpYUNB9PKS7JAyX2oFjs22_g-PDnWH0Tw4aE7xIdbjj7CfmYto9KuU8iUTHag47aZsXH8TOsKIiFQ4dqUCvQyblXg3xXslnX-x2igCv8GrqJHVv3fdzB_OaMx7xZABigAu4aWHG60H16aV_udiXBk3Olkd2q2B8LnRfqcTzGenpZqTbHt8ljXneR9DNGlbIB2cG9Aniq4vf34lKBvXi1IFUj7Qv-G2HQuAdjKFTdjZy6vtSFPwXQFbkRE2flpN1qS4WNwmt0_S8Yqtl52oHp780k3GlExQycOIMNMXPJx_mKj0A0d93GBDdAkbrSjT2FkdyCm3NUlOy6F1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت اثرِ یک همراهی
💫
✨
هر همراهی، وقتی به نیت خیر گره می‌خورد، می‌تواند اثری ماندگار بر جای بگذارد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این اثر را ماندگار می‌کند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/689231" target="_blank">📅 14:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689230">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/689230" target="_blank">📅 14:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689229">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0NRQR_wVV_6-RS_Ky4rFvC5aIhOyQk7JBFpIOkcqXPShvCcl2uD97wE8Py9zpJdRHDTKXq_B-BpVEssHCGHVSHySw7PbjgiqmihZIkueLn1_0TcRgSfLOi9fODejIlNFliUql78cVDZj1CrFV5_oEQpxQU5TLbUO7FO9pB5HOxtI4ZYORC1OeX3aMxk3mwp1EesXzyq0UICLmfX_ueqagcdBWO2HoGaVSGinPtNpxixf7X1eMwKJEtPfigiTHFBa4rIO3Xz0td-CCK-j26WRNdcGofo6i0-B7SMFvildfKE8H4ZXXZNcveI-KO4q4yPrxDWDDBeEYJUBXX6k0PsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمایت و همراهی مدیران وزارت نفت با شریعتمداری مدیرعامل هلدینگ خلیج فارس
🔹
اطلاعات رسیده به میز نفت از همراهی پنهانی تعدادی محدود از مدیران شرکت ملی نفت و زیرمجموعه‌های وزارت نفت با جبهه محمد شریعتمداری حکایت دارد؛ مدیرانی که در ظاهر کنار محسن پاک‌نژاد ایستاده‌اند، اما در پشت صحنه روی شکست وزیر نفت شرط بسته‌اند. انگیزه اصلی این همراهی، نه اختلاف کارشناسی، بلکه نگرانی از موج برکناری‌ها پس از تعیین تکلیف مناقشه هلدینگ خلیج فارس است.
🔹
همه این افراد به‌ دلیل حواشی، تصمیم‌های پرهزینه و عملکرد سؤال‌برانگیز، صندلی خود را در خطر می‌بینند و بقای شریعتمداری را سپری برای حفظ موقعیتشان تلقی می‌کنند. گزارش‌ها از تماس‌ها، انتقال اطلاعات و هماهنگی‌هایی حکایت دارد که جزئیات آن پس از تکمیل مستندات منتشر خواهد شد. میزنفت تأکید می‌کند سکوت فعلی به معنای بی‌اطلاعی نیست. مناقشه خلیج فارس سرانجام تمام می‌شود؛ اما پرونده مدیرانی باقی می‌ماند که برای نجات صندلی خود، وارد یک قمار پنهانی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/689229" target="_blank">📅 14:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689228">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI1tKCWsb31U2DMU8Z2dJI8p9QKAm9gTetogsE_esP6xgJ1zpkefsBk6QPARc8_u4czG-RSXhrapcil75cJIbrktAS0OfjX7HFlZrWMR4uei4YrFMSbZIcO9QI9dkDJVvsUMnGGX3JlPXldld7KLi0UZaH-yNXWoxQVVNvGKzMrzydHKH8lvMyW3yiYeIc4BHPNe5ltAfc4vfIRhfi7AM3dOJHOBU_mFJWhkE0zDlcl3PsXbXPBNZLvC-Dud2gTVGs6U5p2VdQXBF-Q8089Wsl_8IntfbrsQOTcPQrPgGh5eOdT1MTEj6tkW7bqotRCrDH7czTCxVOv8owPRCF83hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارین افیرز: جبهه دوم ایران پیشروی جسورانه حوثی‌ها، جنگ‌های غرب آسیا را دگرگون کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/689228" target="_blank">📅 14:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689227">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olx8dGSKx7rfFEN7hint_0rZpSLgtCOnI_CQX3vXfIXe6HfmVpEm0Ob9oQNTvRa0sDvb9gGbzn7EHQCyAYcteRS4rQFGYAiHJkuLLqLwj2OvjWmjQgEex6l_YKUClw3SB5UZ_KjX_Lp3Ix3JWBi8X51bWNCE_5fRxRZf99BOwR_KF0usi_R5P6qBJ_W9EwYTeDYYdO0Ho3FXLq4GZgI14-fExIbNfrAThWVX7dOgtMCSlf4RyM2ASSo-4JPPoGl4EaEcWGPulp8RNC3COy_i6bUmVyS2T9GFlYQpoiS7qFGvH4ohZuPy94AXju4ibCwQY_KpSsvd4HDdeqfwRxdKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت ترامپ درباره امید مردم ایران
🔹
ترامپ توییتی زده‌بود که در آن ناخواسته به ترس آمریکا و رژیم صهیونیستی از امید مردم اشاره کرده‌بود. امیدی که با انکار هرگونه امکان بهبود، با بزرگ‌نمایی قدرت خود و کوچک‌نمایی طرف مقابل و با اختلاف‌افکنی و القای فروپاشی داخلی دنبال کشتن آن در جامعه ایران هستند. واقعیت این است که آن‌ها از امید، بیشتر از بمب می‌ترسند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/689227" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689226">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
مقاومت عراق اتهام حمله به تاسیسات انرژی عربستان را رد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/689226" target="_blank">📅 14:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689225">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHaMxrp1VMlQZQVW_klMi2xwzYkMa4KloSEBbc8XkQlXmWohq_6D_zUbXyu57Sb-31eFnKzfvv2gHPeaO_TBv5akYOjQo80TPCBg3vdz_3iyuwHn2KQB76zUsYKrj5d4TGlom1MoF0t2-VeFqnESlTb8O9fXb54mAo63qCFkUByNXpv1auUVQyzQV-ZUkyrauwSvdjxWXFvgIPhhvy8uHslfWhUJ4ESuvW-WQR_26AyWAetQI9xUvk2gNhAG13IYv6JkffDB0gZlwoLH9pPP6eq4oTYlBADtgJon0-MUp3q0Q7_vPGkqiiWsvtWApYyZ4Ga5y6FHVKix21pCdRJB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با گلدوزی می‌تونی خیلی راحت لباس‌های لکه‌دارت رو کاور کنی
🪷
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/689225" target="_blank">📅 14:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689224">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای ترامپ در مورد حمله به خط لوله نفت عربستان: به احتمال زیاد ایران مسئول این حمله است    ترامپ:
🔹
جنگ ایران خیلی زود پایان خواهد یافت. جنگ ایران احتمالا پس از انتخابات میان‌دوره‌ای پایان خواهد یافت./ حوثی‌ها نمی‌خواهند با ما بجنگند‌‌. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/689224" target="_blank">📅 13:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689222">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c005ed5d.mp4?token=ZZ7Sb2gAy5Us1jJXonOvhswOTIxpIGS95GskyScvkq2x1HUEEdI2jBZ3r08ihwiey2SI7nxzds6Srs9ckU-2-zxx_gp8ZVSyGA1mhv2W4K9gjLqYHv51-w5aV6TGOOcJDjsmot8nzsl85LVKDtN_g9hO6Tdp0V21152M23Sn-wfgAnk8qo-evp-Hn88k0NK7oleuG80uw07_nXszbg4rJN4JFJnaP20s7UFlKoMttsiyuEVuwrUZBuCLuIqCZOAjDSP33XKBu1siYvnRcqHNwZMpHr41tj2zc4orgYu2KAC1aaiZfYWO_cssrNfSibuh6CUb61eC19IG53RskZl91Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c005ed5d.mp4?token=ZZ7Sb2gAy5Us1jJXonOvhswOTIxpIGS95GskyScvkq2x1HUEEdI2jBZ3r08ihwiey2SI7nxzds6Srs9ckU-2-zxx_gp8ZVSyGA1mhv2W4K9gjLqYHv51-w5aV6TGOOcJDjsmot8nzsl85LVKDtN_g9hO6Tdp0V21152M23Sn-wfgAnk8qo-evp-Hn88k0NK7oleuG80uw07_nXszbg4rJN4JFJnaP20s7UFlKoMttsiyuEVuwrUZBuCLuIqCZOAjDSP33XKBu1siYvnRcqHNwZMpHr41tj2zc4orgYu2KAC1aaiZfYWO_cssrNfSibuh6CUb61eC19IG53RskZl91Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاربرد هررنگ چسب برق رو از زبان خودشون یاد بگیر
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/689222" target="_blank">📅 13:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689221">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
از ساعاتی پیش یک تیم تروریستی در بخشان سراوان توسط نیروهای قرارگاه قدس سپاه محاصره شده و رزمندگان در حال انهدام تیم می‌باشند
🔹
گزارش تکمیلی در بیانیه قرارگاه تا ساعاتی دیگر به اطلاع مردم شریف ایران خواهد رسید./ صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/689221" target="_blank">📅 13:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689220">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
عربستان حمله به خط لوله نفتی خود را تأیید کرد  وزارت انرژی عربستان:
🔹
خط لوله نفتی شرق به غرب این کشور در ریاض و مدینه منوره، روز پنجشنبه، هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/689220" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ff2d89ba.mp4?token=c5sJdPTWkrPzE_lGzsnGhDEXaDs8ugRm91Y2ndpakFgTRwIsiomUzh3jLEoBcezM9zNIDtQJaKmp6SOS3cib4OTGkSNN75l-AlA9251ZH8TI5mxLsr28yFxFXj1zcJyPN8DsfTmCwAaSyaMPaW7jcgf5cNXCcqhBfybzvJ6CosQakHpCejZkiLmDn2mta4rNoPJpitCPigL6_W3ethkE3fzIoxcI53u4l-IVL7aLIwsqESYf4-Ar3yUosfsn88MdfDMiVkgXLtfxCz3mhRXlCnK63P_ofQ-g6Y_ea9wutRwqmWeMftNbIWsUiNuzDBMr89gHRrKEblAUfZvD5WxtQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ff2d89ba.mp4?token=c5sJdPTWkrPzE_lGzsnGhDEXaDs8ugRm91Y2ndpakFgTRwIsiomUzh3jLEoBcezM9zNIDtQJaKmp6SOS3cib4OTGkSNN75l-AlA9251ZH8TI5mxLsr28yFxFXj1zcJyPN8DsfTmCwAaSyaMPaW7jcgf5cNXCcqhBfybzvJ6CosQakHpCejZkiLmDn2mta4rNoPJpitCPigL6_W3ethkE3fzIoxcI53u4l-IVL7aLIwsqESYf4-Ar3yUosfsn88MdfDMiVkgXLtfxCz3mhRXlCnK63P_ofQ-g6Y_ea9wutRwqmWeMftNbIWsUiNuzDBMr89gHRrKEblAUfZvD5WxtQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در واکنش به تحولات مربوط به ایران مدعی شد: همه‌چیز خوب پیش خواهد رفت #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/689219" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689218">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crjI-UXVowTDn6eVA4e6gXixAOVXGtIe9L9j1lZ7Tvo7RyqOwX-AjFrW8Zb2z4yDWv68MbO9TxihB_mCdZb3YSqYbGr9GcvP1zJL8S47FzDjA4A27noFLYK1Sd1JNnHXCriObUXEO8zmMdeeUUrY8r7wYihbk6nt96iRSa74rWEkn3E0H_61kHMqyQNpPRkp_fFmw-69IRFe3Xgher-cbVI7ve9VdbyQXOQL-77xnzupHRyzI91ZN0EGk8tnUvfw9H1JE6Mg5QKYTiVQAg0UufxpM63xHNubKkJs5Or8wzqxTv-ej_xJR4iX5pm9l5gV4I6LAdlBz5uNHGyTddFTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشست مشترک فرماندهان ارتش و سپاه پاسداران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/689218" target="_blank">📅 13:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689216">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl8IQ5pUandFw4xsFrn8VEURuZmicFMdZAN0jRlxke_fLGkMfWM1UYEGnGUWwp04mH4c-75zT87rdw3fkLl7wQ4vPwMkwmB1TESO_mw0j044TnUim-O3y_o-Pa3khYzSFnnduvknoLy8jL5Ggp7D08l_7CXcMS7Ngu8cfDBnAsa76XQm22rMnug2utOpFUHE5uqA5Sx9MlXwK70IUslxaHBED-joFGhjzM1R-9rN3dyYK3I17sQ7niAwAXUgNhF7thBOZh3cJ7Cl_gRp3xUKM2dIpOWp7uGa3dU5AH6gn0dfpSsUbnS9bMAsmVk3BVPUdML0_2WiXFEY8qzm9KGs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e10581af.mp4?token=XFgnvmrt6-x6zakvMTcx-FKAKPIeQMCuWYhxLAcBROyshAzza92fEP53yvJEgpiH7HWMXVyEePsWkxgu7HqEoyDsknYGteWaqtuIfNYL6kzz2IeZ9Zkbzg0MTOcDxX9nXKfD901yif1UQUiXZLLjdRXYf0F4OTFxN9rNqoOZkiH8_v3m_an4D_pW7KlNXjeuMycFkO27KoHBz8Y6UGiH8AeiaKXHF35ctoMfd27_d6Q8QJ0qW6Dk_DQT1VxBMdwdmhg5TGgj7UGWiRMz6ALX3UAUVCX-7bdjFrOAQbQo9DmK1mAhVMW1n6RKjZZCWONuTgC3LSQMKsNKVoiuHxSHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e10581af.mp4?token=XFgnvmrt6-x6zakvMTcx-FKAKPIeQMCuWYhxLAcBROyshAzza92fEP53yvJEgpiH7HWMXVyEePsWkxgu7HqEoyDsknYGteWaqtuIfNYL6kzz2IeZ9Zkbzg0MTOcDxX9nXKfD901yif1UQUiXZLLjdRXYf0F4OTFxN9rNqoOZkiH8_v3m_an4D_pW7KlNXjeuMycFkO27KoHBz8Y6UGiH8AeiaKXHF35ctoMfd27_d6Q8QJ0qW6Dk_DQT1VxBMdwdmhg5TGgj7UGWiRMz6ALX3UAUVCX-7bdjFrOAQbQo9DmK1mAhVMW1n6RKjZZCWONuTgC3LSQMKsNKVoiuHxSHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه سفارت ایران به سنتکام درباره تنگه هرمز
🔹
صفحه رسمی سفارت ایران در زیمبابوه با انتشار این ویدئو نوشت: «وضعیت سنتکام وقتی اتفاقات تنگه هرمز رو رصد می‌کنه!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/689216" target="_blank">📅 13:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689214">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
مدیرعامل شرکت شهر فرودگاهی امام خمینی: تمامی پروازهای نجف و بغداد از سوی فرودگاه امام خمینی در حال انجام است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/689214" target="_blank">📅 13:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689212">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2dheZCxPWAE55bXgD4adi5MJ_2ykiqM9GoR8AlPxh4hhtEz2FRzeZWGCkDXAgrV2KGd60eX4VVHiiq8apip70zLaQhQY17lWggwFBmRB4h8DCDwnQ9nylEsd0J22_3t4O-t28vroRukH34aHHwb2jj9KW5N_DiYXIO6fCpwlthl9AsEx1D80OWmA_7fst3ivnwfNXh1FN0EcurVARg0Y3e05TnJASwBcpU3a7eDXf9O5EanyRjZeCKwWAoQ0il3nTrNfeS2oaal9R9gq7CYqJlPEQgTVkQcf5GyWAckOL3cV4MFmz-XmZc2WrRznJQfml6e_-kqZvpEvLlfo8I54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_خودرو
| قیمت روز خودرو های بازار کشور؛ امروز ۲۱ شهریور ۱۴۰۵
🔹
بازار خودرو امروز در امتداد موج صعودی هفته‌های گذشته بازگشایی شد و بخش عمده‌ای از مدل‌ها همچنان با افزایش قیمت همراه شدند.
🔹
بررسی روند معاملات گویای آن است که بازار خودرو طی یک ماه اخیر، سنگین‌ترین دوره جهش قیمتی خود در سال جاری را ثبت کرده و شکاف قیمت‌ها با نرخ‌های پیشین به شکل چشمگیری عمیق‌تر شده است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/689212" target="_blank">📅 12:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689211">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85b001aeb.mp4?token=X5PCRBrCaQH4cZk35bkqfDZfT0Da7xQQGmkyu339ifu7ZlufQylW6BnU6_n3IbAXmW-0F442XJ6oCx0q3oYQxyIySANLygR2MdX3x9gkuHA9zKb_3xMU_k9Dtj-0eDS-u5SSorMgPHT8x1ZhCNgw_TZKtLC-stY0d0tOJXx4TSWNfNwpB0alQtbmECIXixjiz4wiqyw0wvRaFwyz2GOSjPed2wJd64j00XbjWFCLFFdYZEkNa1dOdjGF4_a4k1jVvEQ8PIanW07ZOFg75gQltP4C1s6G_ZyJrhOrMhgGVirpDlU9CpQjN3hnt_lUeToXK5Or27O-yPXKJucQ8VvfMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85b001aeb.mp4?token=X5PCRBrCaQH4cZk35bkqfDZfT0Da7xQQGmkyu339ifu7ZlufQylW6BnU6_n3IbAXmW-0F442XJ6oCx0q3oYQxyIySANLygR2MdX3x9gkuHA9zKb_3xMU_k9Dtj-0eDS-u5SSorMgPHT8x1ZhCNgw_TZKtLC-stY0d0tOJXx4TSWNfNwpB0alQtbmECIXixjiz4wiqyw0wvRaFwyz2GOSjPed2wJd64j00XbjWFCLFFdYZEkNa1dOdjGF4_a4k1jVvEQ8PIanW07ZOFg75gQltP4C1s6G_ZyJrhOrMhgGVirpDlU9CpQjN3hnt_lUeToXK5Or27O-yPXKJucQ8VvfMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در واکنش به تحولات مربوط به ایران مدعی شد: همه‌چیز خوب پیش خواهد رفت
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/689211" target="_blank">📅 12:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689210">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729f8f860a.mp4?token=HgF3C4PdTYRQZ6VdTmILccsSadsMbkNPDERoee9UtI7_a6zaPvfj0iscu2MSgsyxLcI95keszv9lnLvezXRbth05GHSRHSkHGdGHKqYlkAHoAcN29J_HtQDSj_GT5r5bQwQ1GCSSBZZXpx9kN-Z6tHx3W5VVHJ7-7586HIS2DyuchFgNs0izwqAFdiCdRLFF64LuhNoDKNg4v4Xp6QuRRAFfRlhYclxYJWAIn1ybNzs2LWiCabbILLM4xiGXAeqnyB3qcS_kdFgXjnvEnEdo03hkIt12kj39Po4nn9y8NqieHDjyImpEpEHUXk1T0sGp6AujTAvvYdJwRCT4oxvWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729f8f860a.mp4?token=HgF3C4PdTYRQZ6VdTmILccsSadsMbkNPDERoee9UtI7_a6zaPvfj0iscu2MSgsyxLcI95keszv9lnLvezXRbth05GHSRHSkHGdGHKqYlkAHoAcN29J_HtQDSj_GT5r5bQwQ1GCSSBZZXpx9kN-Z6tHx3W5VVHJ7-7586HIS2DyuchFgNs0izwqAFdiCdRLFF64LuhNoDKNg4v4Xp6QuRRAFfRlhYclxYJWAIn1ybNzs2LWiCabbILLM4xiGXAeqnyB3qcS_kdFgXjnvEnEdo03hkIt12kj39Po4nn9y8NqieHDjyImpEpEHUXk1T0sGp6AujTAvvYdJwRCT4oxvWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/689210" target="_blank">📅 12:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1985c52952.mp4?token=RyFQx_dcziI07EXs43mCydzX0DDsLEXLWK6j4MU04Tnihvi1AVL9ayUNh5bUAIFB5vrYyO1GwrOoqzxE41Yf1oZyPUgNLSjEbWg5WyQbTNqFytVGyF6ZyhBllud9_bWg9ml7j_-kkgBw9Pr2ufXF1XuSvhCsKETTqCtFB37oX-rYiXw78tRTttJnhUNu_uC25cN3ujQ7Wt4CuNG7dCtEHXRODGfONHo68UOiksd_xMDDanlXiPSDNZJg2FE0gNz6LMBKl0jXQ_ZqUgWnZrteVgl2QxGGIbD4YIluC1o8lQcHJg09_mBza4-A4h3XxiyO1X0AsNQLqu7BuSYUu736Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1985c52952.mp4?token=RyFQx_dcziI07EXs43mCydzX0DDsLEXLWK6j4MU04Tnihvi1AVL9ayUNh5bUAIFB5vrYyO1GwrOoqzxE41Yf1oZyPUgNLSjEbWg5WyQbTNqFytVGyF6ZyhBllud9_bWg9ml7j_-kkgBw9Pr2ufXF1XuSvhCsKETTqCtFB37oX-rYiXw78tRTttJnhUNu_uC25cN3ujQ7Wt4CuNG7dCtEHXRODGfONHo68UOiksd_xMDDanlXiPSDNZJg2FE0gNz6LMBKl0jXQ_ZqUgWnZrteVgl2QxGGIbD4YIluC1o8lQcHJg09_mBza4-A4h3XxiyO1X0AsNQLqu7BuSYUu736Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند جالب برای رفع بوی بد و عرق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/689208" target="_blank">📅 12:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689207">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekl9WI08H2kq2Sgq7gs90o5oZjxs5a3r5EyOL15uzddts4_s66mRwN9kEcyXukmwzqUzn49RBNZaj-Gqf3UvjeH---qmlpg-v-Dmngqd0DVs3iGBZejkCrKGMs_qArswujzaPbA7wy301BdfXywbP5FMDhAZnBxLqvJ3x-zkEX1APGVjhdbW_WBgfChgDOPwNwM8dZKR6-ER5Q1Az8sG5AVM979L_GU-MbiWHSeOoX-UcWhfB0RbARt_1mmDwWlIzbgK_qynQuP2MohoLDyU2RTrVQQzsAJt3_oj-m5U4qpq7xourlG6gozvUbYBb_NITKZSkpdjNGf8fp1jNypLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرسنگی به‌ عنوان سلاح در محاصره پاریس/ چرا ترامپ نمی‌تواند تاریخ را تکرار کند؟
🔹
امروز ترامپ سعی می‌کند از طریق روش محاصره، مردم ایران را به جان هم بیندازد اما این روش توسط او ایجاد نشده بلکه محصول یک روند تاریخی است که ریشه در حوادث مختلف دارد. یکی از محاصرات تاریخی که احتمالا ترامپ را به سمت این اقدام خبیثانه هدایت کرده، محاصره پاریس در سالهای ۱۸۷۰ و ۱۸۷۱ است.
گزارش تاریخی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244515</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/689207" target="_blank">📅 12:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689206">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تکذیب تعطیلی مرز مهران  ‌فرماندار مهران:
🔹
مرز مهران باز است و فعالیت‌های مسافری و گمرکی در این مرز برقرار است و هیچ‌گونه تعطیلی یا توقفی در روند فعالیت مرز با کشور عراق وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/689206" target="_blank">📅 12:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689205">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6bd17689d.mp4?token=q5SQTtl6GNCzOToIb7SEMn3DbFhpJylVeG-slvJ9P2Xk3pl2kzGuAKhFbXRN0q1cAW62Ju3NPuyagpT20x_RMV-rK7te12PZzA9nCIxc-BJoexYZTFyzrmOI6OZaEdla9jSM_KWAvURvxgiJjg11k6SgBPcz1XsU5-8Tphod2Sj2vT3fR22C5674pjNuKUfWcRrKWuXw2PVqrHcncxXQ9d0xT55rIu68NigNU2AWHkHQ61ltQ5M_PJHg6Eyz3QGKhTNYR59Yd_pdFwZOtyt8NAvNQ20N8dUmoQ1A6ZKdlBiDYKYNDX54wSr5RvoyWXsMDLMUpJpzkRSB7PLMjhtEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6bd17689d.mp4?token=q5SQTtl6GNCzOToIb7SEMn3DbFhpJylVeG-slvJ9P2Xk3pl2kzGuAKhFbXRN0q1cAW62Ju3NPuyagpT20x_RMV-rK7te12PZzA9nCIxc-BJoexYZTFyzrmOI6OZaEdla9jSM_KWAvURvxgiJjg11k6SgBPcz1XsU5-8Tphod2Sj2vT3fR22C5674pjNuKUfWcRrKWuXw2PVqrHcncxXQ9d0xT55rIu68NigNU2AWHkHQ61ltQ5M_PJHg6Eyz3QGKhTNYR59Yd_pdFwZOtyt8NAvNQ20N8dUmoQ1A6ZKdlBiDYKYNDX54wSr5RvoyWXsMDLMUpJpzkRSB7PLMjhtEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: موشک از خاک یک کشور حاشیه جنوبی خلیج‌فارس به لامرد شلیک شده/ ایرانیان برای همیشه این مسئله را مطالبه خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/689205" target="_blank">📅 12:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/689204" target="_blank">📅 12:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ee7cc5f4.mp4?token=QvmDBCm8pKT2dYIcigfTdB9DYrtoF-9b1QnoLPNy_Qnw8AtWJqw2PAakPDI4vtqMiAXyemeHNv4CCWUcyrcvLP8pfBJVlG1ip2J1GlSN5rr9ztW4DI3nFABU1jOdaxBsLLiL0-9zK-IRTO351zWWBiUnCWZN4dSoUQOV71Vez8LbZNgPEaxRripVFf9H-HiC_DaNEeQxZ5kP4KpaKtX0Xp3w4t4oVbHGtAj1uJHq92AGxoWOmGWCC8X24a6ANn83jdWYhtXOMHJyBJ7PZaVdqwbLmEoJZ1TygSL3Mg9HsvpjhOZ-gWSeXOt7udZVJgfoaYEhG8SH5NuQlzh4YH5xiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ee7cc5f4.mp4?token=QvmDBCm8pKT2dYIcigfTdB9DYrtoF-9b1QnoLPNy_Qnw8AtWJqw2PAakPDI4vtqMiAXyemeHNv4CCWUcyrcvLP8pfBJVlG1ip2J1GlSN5rr9ztW4DI3nFABU1jOdaxBsLLiL0-9zK-IRTO351zWWBiUnCWZN4dSoUQOV71Vez8LbZNgPEaxRripVFf9H-HiC_DaNEeQxZ5kP4KpaKtX0Xp3w4t4oVbHGtAj1uJHq92AGxoWOmGWCC8X24a6ANn83jdWYhtXOMHJyBJ7PZaVdqwbLmEoJZ1TygSL3Mg9HsvpjhOZ-gWSeXOt7udZVJgfoaYEhG8SH5NuQlzh4YH5xiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد حاجی‌پور، ملی‌پوش والیبال ایران با تماشاگران برای نجات توپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/689203" target="_blank">📅 12:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6242363ef5.mp4?token=of103OhIAT7nc1LRVEhbjTALxtWPZV6fp65Iw_AN7vt8G1L3xvJ9Xcpt0TDt8ml62AJVvbAsE-TqgG2okITnsMYmlg6-_WiDf_vZFIMbYi11HYgQc8ifO6Skdm9NQgBW7sfdS1TxXMuau1AlUapMk48dHM9y4CBZHwfNaP-HBk8yiocLIbrnUs9WVgI6aZODJ3P-0eh6_CzhPsJ0cSSmKfUeTybcs7-ipekKckCYK5IO4PwfxmJfpZTUx-H6LhSaP_1Ueftjr6AfZD3czPvIsff1k4c511QeQaywoPnhIQs4WNGnj_yafZWltuij2-9bTdC3-73wfvULencLDx3m7W10p6T-Iv4eO0h-tC3J4MLU7_-m5JTMQgJF-zKJyEPZQFfdPlC-KovEmsIJWXlXRqe5ntgyPP9u2mkFUCM7NIX_6o3EEmwbVY41VwG-chDs4pUwCUV597riwJ6oYKrMgrylOc_CgREfqMLYrsJqpSP-FKYUIQuDZvcWnR7Rnr_MnXEgkg29Fbu96XExRSTGI8T8wIsREsZdlYygRqILSxewX2f2j5ApNhJZyWnDIOjqkezak1E65lXUj9RuemL215VWDlTBEMPbOMS30PgjI8_snVaWhrewvxI7xJdr6S-MSZVcsj7D2Vk1lqXo9dLvSypPohygcW9_tLGpVV_kOzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6242363ef5.mp4?token=of103OhIAT7nc1LRVEhbjTALxtWPZV6fp65Iw_AN7vt8G1L3xvJ9Xcpt0TDt8ml62AJVvbAsE-TqgG2okITnsMYmlg6-_WiDf_vZFIMbYi11HYgQc8ifO6Skdm9NQgBW7sfdS1TxXMuau1AlUapMk48dHM9y4CBZHwfNaP-HBk8yiocLIbrnUs9WVgI6aZODJ3P-0eh6_CzhPsJ0cSSmKfUeTybcs7-ipekKckCYK5IO4PwfxmJfpZTUx-H6LhSaP_1Ueftjr6AfZD3czPvIsff1k4c511QeQaywoPnhIQs4WNGnj_yafZWltuij2-9bTdC3-73wfvULencLDx3m7W10p6T-Iv4eO0h-tC3J4MLU7_-m5JTMQgJF-zKJyEPZQFfdPlC-KovEmsIJWXlXRqe5ntgyPP9u2mkFUCM7NIX_6o3EEmwbVY41VwG-chDs4pUwCUV597riwJ6oYKrMgrylOc_CgREfqMLYrsJqpSP-FKYUIQuDZvcWnR7Rnr_MnXEgkg29Fbu96XExRSTGI8T8wIsREsZdlYygRqILSxewX2f2j5ApNhJZyWnDIOjqkezak1E65lXUj9RuemL215VWDlTBEMPbOMS30PgjI8_snVaWhrewvxI7xJdr6S-MSZVcsj7D2Vk1lqXo9dLvSypPohygcW9_tLGpVV_kOzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور میشه که مردها با یک سرماخوردگی ساده احساس می‌کنند به آخر خط رسیدن #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/689202" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689201">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسبدگردان آسمان(سبدگردان آسمان)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fC0CzgPV_hETBJAZ6EqIP-B8zNknlKhVAeWN1JGQ3dK7zbTrnEeHSze3wh8r5sUkSD_Owa8twRjaIGlrh2NmFrble_DiOSnDHxs6pUfRa1Eo_x4ckDA0YU5C6ETwzk02LyvurHNTerMs2PSAvySUsQdVL6oTqBYwMB5uCf0251STOkr4wXdORR9GeXJzoUdctMJ9xbHUULipmKasmRNE9a-b4tapia_zKJPQA7Ndv5Je4KKdqmi3pQIR_87tql1NMvgCh29AKt7xPsBxJfX1NIzBa_iiBRgPd3C4rRatKt8ej_RmqcAbI9b_pkBb2O2bUr9CZrx1b4x9YeuFrG75rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💯
۲،۷۷۰،۰۰۰ تومان سود ماهانه به ازای هر ۱۰۰ میلیون تومان
با صندوق درآمد ثابت
آسمان سهند
🎁
%۳۸ سود روزشمار، اول هر ماه!
✅
سود بیشتر از بانک
✅
واریز خودکار ماهانه
✅
بدون مالیات و جریمه برداشت
✅
محاسبه سود روزشمار بدون وقفه (حتی در تعطیلات)
✅
بیش از ۱۵ سال سابقه فعالیت
🔗
مشاوره رایگان
صندوق درآمد ثابت سهند
.....
سبدگردان آسمان
.....
☎️
مرکز تماس: ۰۲۱۴۱۷۹۳۰۰۰
🌐
وبسایت آسمان
📩
سبدگردان آسمان</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/689201" target="_blank">📅 12:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMyAlfSexQZpJhgT_YFB-gZD5wFE0ShajcCj08-WNdwZHiqM12D1If5-Njp3A_mzXDaiChjMxk0k4ImBS4l2PzgwiztrDQlwXBYRX32xvslNuXn-T01UI6spurpst6ZlnY2h8ndRxAy2OU8Ed6Dl-g2_iYD9UAamTQAoashdnfnmjOp1Z48RcB7jAYZLAjdzZzC28Zbo65_BX3-0wFGDqPqDzgwbD-G-YN6KbP4btygjJarY991eefWrsn1_5dsTvGeRv7s-hETp9v5myazo_mABSoi4KQINMR3Rdui7pjBGvcWeTdGYImb9-jsaIT0EOjATbgaZ_AhmLjIED4PiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ ایران به فینال آسیا راه یافت
،
شاگردان پیاتزا کانگوروها را هم شکست دادند
🔹
ایران ۳ - ۱ استرالیا
🇮🇷
۲۵ | ۱۷ | ۲۵ | ۲۵
🇳🇿
۲۱ | ۲۵ | ۱۷ | ۲۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/689200" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689198">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEv-Y2aRdfFybaabZ6RKb0EB3Vua7FEmyT5SUwRiGpqXPnK6h0PAnTiZzVe6KRW707m6R1LHkXVE_S4FrstzL0ntGnkj3Xb4Fc_WXq0z3A0R2kiwEMF9USqxKbMWbXGALRmej_hQ_rvFLiGVbGtIL2bEvOMzjIWjJmgk_NAf-WTrgg0MhTFd31HfF0KZV3IXQM-ph1MfpabVmTKM5Bq1akpnWOEZJRJmMxSr6fptfyx1cFA1lY1pWuRm4o1ZWxRsSFs-a9ibWtXeMBct7l1AXzKGLc4nBdeeNcBBLDTrrZlag24rYPD05xoMTWOBQeJQ17sM8Gdn8atJJgwbP8lPHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/689198" target="_blank">📅 11:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f56cd818.mp4?token=hqyoT7cPWVI5ow5y15NeNA-B2yDSe12V3VCDAIO9VHiQ6NkqTq5zSIEAYdAr6MJYcd98QxA5RYXM0gEk0yKU7DJy6MzfwM734K7lcUw8-NQdhkyVTVItLejfCxjdOgVp2yX3YPruZEqswIvwCRrxvOqLPOmbSnSLG1i6_s8EYEfXRdLQdNzpLxvud3bybr6dKp-HA-s-6cI3BtXoMt2aEourxr4xg6KQ7S-a0jwkHNGYx5QaTVWCtkNfcmqb9Vx3DHNWAcsPVNoq-gzO2SoLM1lQOOBN4zFaCCfR4lgMVOJYcrJcXM5BDHh9wGh5n_H3BTJysmp3nxlOQ7lkWSi_PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f56cd818.mp4?token=hqyoT7cPWVI5ow5y15NeNA-B2yDSe12V3VCDAIO9VHiQ6NkqTq5zSIEAYdAr6MJYcd98QxA5RYXM0gEk0yKU7DJy6MzfwM734K7lcUw8-NQdhkyVTVItLejfCxjdOgVp2yX3YPruZEqswIvwCRrxvOqLPOmbSnSLG1i6_s8EYEfXRdLQdNzpLxvud3bybr6dKp-HA-s-6cI3BtXoMt2aEourxr4xg6KQ7S-a0jwkHNGYx5QaTVWCtkNfcmqb9Vx3DHNWAcsPVNoq-gzO2SoLM1lQOOBN4zFaCCfR4lgMVOJYcrJcXM5BDHh9wGh5n_H3BTJysmp3nxlOQ7lkWSi_PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این
تصویر را خوب ببینید؛ نوجوانِ سیستان‌وبلوچستانی، ماکت پدافندی که خودش ساخته را به محفل ستاره‌ها آورده و از آرزوی بزرگش می‌گوید
🔹
«سربازان در گهواره‌ خمینی» بزرگ شدند؛ جنگیدند، درخشیدند، جان دادند، اما میدان را خالی نکردند.
🔹
«سربازان در گهواره‌ خامنه‌ای» تازه دارند بزرگ می‌شوند؛ با این نسل چه خواهید کرد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/689197" target="_blank">📅 11:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY_DZYle8Jwqbob1GTenh4KurJr1psxJRufuXHsGAvHCIC1w_gOaAO-OElbiWdwduhKALHGZEWNbsBSp7tL-Yc8J880cCy3rat6KwKI5hFQccv18r3tFWXHhREckfg4pTLnvhRe4xzCp7SSujpRWi5Lgu3QvYu_z0tw1I44tj4iitCTphuc5dk7F__5mvostVnA8Jz7rC3WsMZoFjk2c5Q7s_sPeO21N9JtU264HJ2Rdcx28_bUeA3gAwDZnZ_64lcZQBR7kxGjwMWHdv3HbMMKWrmGN-P7qRqGPS0k4-cH7wJszl1pWyT2jWAxlmMtSa2NKLG9JwR--q_t-lZb0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕰
ساعت نگارگری پنج تن
ترکیبی از هنر ایرانی، هویت مذهبی و یک دکور متفاوت برای خانه یا محل کار.
✨
مشخصات:
▫️
قطر: ۳۶ سانتی‌متر
▫️
جنس: پلی‌وود
▫️
طراحی: نگارگری با مضمون پنج تن
💰
قیمت اصلی: ۲٬۱۹۸٬۰۰۰ تومان
🔥
قیمت ویژه: ۱٬۹۴۴٬۰۰۰ تومان
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/689196" target="_blank">📅 11:39 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
