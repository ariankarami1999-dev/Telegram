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
<img src="https://cdn4.telesco.pe/file/LienQdsnIEOBD34zlNN7AF5XR2I0bVQIfoTgnLx1Ve3Hl127ma6K9Xs9vCJNZEutkQuwzignQpdpMuqemmvud4IJdNmkyecKJ70fgV3vH3PZ008UOU5gGszotkFN--ZAZaR4twhvZTaXtkoZlddr8O3jmE5CKhWPOR79hUU_E6gWyHvExpSv7V3DuY6JzW0cldtS0HU4jcPaRciZ-Zkzll92Fl8-2Wf-lAn8NhFEh9x0mSXuBZnL3iT3KnT-NdC8tFUyl7GG7wk-Iu-iEoo_lgUOw5TlZBx7WHs48tvncXfrE5SfV7Sauo5jJGQXbgMvx5dEQhIhZRoAfum8zRkfNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 109K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-71584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=H2olKdCe_2KQ4-AZHoLMfQIXRfmbIM-7dU2tzN_8_kH_qWPcaqh_WTuCtKBu5diO2_wu1d_rZjHRriCh1pk2qtEHC1Bz-Uqss0SuZjuZRx3VIrXZe3-Wr-mB500qjMoCxJS_I3yPW3xksXy8Tf96zbR-C1SZBii1iucTvDfQIkSxe-TGkB6JaQU764ty5uxIol5SHhRCOBLhIWawDIw_9exruSUbKuLmc9eRVRdCPWYArKYjX5ZSIl6uhaqZWpQ_wYZBEwnwex8dhvtahQHA025QBg9nZKNug7nYwROl9-E7bRiAEDp_iNCrFDt0NWea-5zQcl2eVqmIpRLOWpkdJlmaJCtqTvC0Z_qxYfeLTt0kc8grmR_byiq-H568NrCBQcalyEwX1lI39j5EjcR5Qw1gcmfBGkOuDaO_gg2pJIVTol01wkSP2jLgbVv2a5YBUndbfUO3xsqsjpEBkHKMm2uC6V5a_gGljKiQkyb6AIX8yPA4pfbV4nui08x0gZz7fVXyzvGO0mXQeZ-VigAY8qS-rUgOJIgc_LQqVWmJzcdnP-mpYFV3--une1mSUxixscrAepXvzMOYY2JAXMF0S5kRK_Nll5dNK6FMCEtQ1KOQBE4HRDo5QOrZPcVQuPeKdewgn-ajhoWh-IrN9_4FCc-10C6XpZvh_yXWQLXWDWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=H2olKdCe_2KQ4-AZHoLMfQIXRfmbIM-7dU2tzN_8_kH_qWPcaqh_WTuCtKBu5diO2_wu1d_rZjHRriCh1pk2qtEHC1Bz-Uqss0SuZjuZRx3VIrXZe3-Wr-mB500qjMoCxJS_I3yPW3xksXy8Tf96zbR-C1SZBii1iucTvDfQIkSxe-TGkB6JaQU764ty5uxIol5SHhRCOBLhIWawDIw_9exruSUbKuLmc9eRVRdCPWYArKYjX5ZSIl6uhaqZWpQ_wYZBEwnwex8dhvtahQHA025QBg9nZKNug7nYwROl9-E7bRiAEDp_iNCrFDt0NWea-5zQcl2eVqmIpRLOWpkdJlmaJCtqTvC0Z_qxYfeLTt0kc8grmR_byiq-H568NrCBQcalyEwX1lI39j5EjcR5Qw1gcmfBGkOuDaO_gg2pJIVTol01wkSP2jLgbVv2a5YBUndbfUO3xsqsjpEBkHKMm2uC6V5a_gGljKiQkyb6AIX8yPA4pfbV4nui08x0gZz7fVXyzvGO0mXQeZ-VigAY8qS-rUgOJIgc_LQqVWmJzcdnP-mpYFV3--une1mSUxixscrAepXvzMOYY2JAXMF0S5kRK_Nll5dNK6FMCEtQ1KOQBE4HRDo5QOrZPcVQuPeKdewgn-ajhoWh-IrN9_4FCc-10C6XpZvh_yXWQLXWDWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی آموزشی برای دخترای موتور‌سوار چنل که قطعا بکارشون میاد
@News_Hut</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/news_hut/71584" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71582">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eC_YffYl7YpxqZumEU9JBiTNc0E6dAouzUDnHUC5zh4idOK7fpz8GgKRtoQJ0L1vzDD8BiziGOgm2T49YYwpTpENEZ_VowimJMawoE25nJYIn0exN1OG6eKML-vDIe1-7QYruM3IJWalHwDzGN5ioOfTJJubXUUPB6JKNbOjaCzg8LVBaaoIsRIWcsCpNNAiq5OWo1jL_RNVzJSMP4cWb-U_FcthYRBapUJrcKcZAwf1Pf37Haeop7lajdsobv5e1KwKV1Q7gqbnFCBL575DDz5oqDKeqsuULVTnzcMP7Y6LyY9EsuLuBz5vqCYp4svMDOZOkLh7M1yj40-QEcn_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UElo5nWDxaMxr72-Ren3ZlHGIHJuxl6u8eQMhcNhT6mRFj1Flrw3f-tToZ4YGSL7Em8etwzD0fOue3bezXLte7Ayffx-T-YKhxKj7HpmNxLfjs5m9VlPoszJMBjTLh6viMkq16YhqhyJUkqNewnv6QfT_uiKwu4jd4ztsEebsFdBF6jwSyqtD-5mNruMOkKZcu9uqcR0OkK6eVuM9l7-rkRQ4_bX8YyAKQ9o16jCjAX7VnsD8JhRWTLRynhOyYgFGLCxPRgW-ITa7REl4QCiAbBSiJZ9IipAMZy-9F1KiO7VN_6howQHr6aw4k2vG3TdxiDYN1DOKwnov604TplAlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👑
دفتر شاهزاده رضا پهلوی:دستگاه کشتار و سرکوب جمهوری اسلامی بار دیگر قصد جان یک زن جوان را کرده است. سودا (مرضیه) ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، پس از ماه‌ها بازداشت و تحمل شکنجه، تنها به دلیل فعالیت رسانه‌ای، در بی‌دادگاه رژیم با مجازات اعدام روبه‌رو شده است.
صدای سودا باشیم و از همه ظرفیت‌ها برای فشار بین‌المللی جهت توقف ماشین کشتار رژیم استفاده کنیم.
سودا ۳۳سال دارد و ساکن بندرعباس است.
او در تاریخ ۹فروردین بازداشت و اکنون با اتهاماتی چون "عکسبرداری از فاصله دور محل اصابت یک موشک و ارسال این تصویر برای یک رسانه فارسی خارج از کشور" به اعدام محکوم شده است.
او حدود شش سال است که به بیماری ام‌اس مبتلاست و علاوه بر آن از بیماری‌های پسوریازیس، نارکولپسی و کولیک معده نیز رنج می‌برد و نمیتواند در زندان بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/news_hut/71582" target="_blank">📅 18:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71581">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBTcxO30-jySps5clEbAU_TuvgZk_PhtkNBRW1YBSRi8ZyCWAcmO87mAWSGyRIqR5WzATOsLwJ0Ux75RdXfqYKBNJoVXxY-o6HEjz_uUt4dJceB-3s_EsvabO7spgDqPeDsO-iRxBEHWJdcy4WR4ISwq0Z2ANJ6Ic36TMSw1DthnqbRI_PW4edlsGqjSTUn_wGNoHYjVJfk6iQ_4T9o0M5V-yslYhsc7mIpqDdx1ni06UBzvuQGyRiAa5pVykVzoi0J33S27q64hl3d7VVmESyLHQOft7yAsNoa6wa8VHYN8wzgp75ctohSNGK8Mqkdsllb-X9r8tK-CDM89GmnVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
نیویورک تایمز:به گفته مقامات ایرانی، تندروهای ایران با صدور دستور حمله به سه کشتی تجاری در تنگه هرمز در تاریخ ۷ ژوئیه، مخفیانه توافق صلح با ایالات متحده را که اوایل همان ماه حاصل شده بود، مختل کردند.
گزارش‌ها حاکی از آن است که مسعود پزشکیان، رئیس‌جمهور، احمد وحیدی و بخش عمده‌ای از رهبری ایران از این عملیات بی‌اطلاع بودند.
بازرسان رد این تصمیم را به جناحی مرتبط با حسین طائب — روحانی بانفوذ و رئیس پیشین اطلاعات سپاه که از همان ابتدا با این توافق مخالف بود — رساندند.
حملات ۷ ژوئیه منجر به حملات متقابل ایالات متحده در روز بعد و همچنین یک کشمکش قدرت بزرگ در داخل ایران شد.
تا ماه سپتامبر، ژنرال‌های تندرو دست بالا را پیدا کردند و به جای بازگشت به میز مذاکره، راهبرد تشدید حملات علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را پیش گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/news_hut/71581" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71580">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71580" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/news_hut/71580" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71579">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpBsSZYGgB3XpIO_fvdHreTNYig7Y5MOBfmJ3mfKC55nyXDHDu9_pcWI0ht1B-1Q7aBjzUzhV3XAE_LBEUsHQIhnxfFEMVXepZ9xC180I8BI-iVosUc4nrqlclO_7eACFpamHDEx3VUFrmXm0G5OOgaVFsVJefMfmS9CFJoNSM54icmvseLCWaX8VtgY2HhwLhIlsM1Iil28h6gOAc4-lkYoYZq6EyEs3_mIs3HHa3aDrOH_UYeALtICHDNrPGkfH6TrGUr-fa_5C4JWO-Rx_u2o0rhO2nKdslg8rOvXJR3c45dHc9-qY79rnFWNPcw2GnVaxhgKtoWvoJttgjl95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/news_hut/71579" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71578">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=pfXj8uA0IHH08RC-QaOj_EePZBAfz2rcAulnjhJc2KYJ6u-uMW3oiuBZCqZ39x02bhdQlYk6WWNDMEA3mJO08vZRpvmf9Sg00qePXkuWHTvsA-43WDTeoHX2Pgp2v24gvkeNcj3AhsepxZqClun0Vm_VHfmLb6XQMrUzXQfldIUWZtSkIYG-NTc6afIufXQgDDgy77Wf5IrKAU0bBochQaeo-D9nYHNNIm0CHIUPomLIAATD5WW3K7CzH0Nq563mxoNcjEWp5i7cRzxXHPh8BUrfc8yNnfLhgeuF2eYiwpCuUE-n8A2-WJqARx5SrHcVj9DvdEqr4yMI0jwcmZA1yUr6C4KCEBGpS3DnWUayAXQgjASD5TsDy5GuHPTjofeSprF570KTQXpjiiqNS3_9wqVJ0A18BqTel0IND5J-PkZnNzS_OhKd5MAtzqYJhTIyrNJY8Gw-5Ph86zEizuuZB8vJ8UTBZU-0P3zu0K4PlVSF4kF6ZkM78JTIpF2XGHg-_z7iCW_YokcinZdnDBBBkGQV1qbVVewIwKtWaT_tvnNkPsCaugxGH-ItcTojfQ4R_rTLyLzAK8Dxq70pTYgLnlER5WmcAh4Pzq_h-jJwevIbHNniYls4qG3TiIzKf4U9JohMWxrQOCiw5xTrv0fxXs4VbbqaGoGD6u4j15cbIpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=pfXj8uA0IHH08RC-QaOj_EePZBAfz2rcAulnjhJc2KYJ6u-uMW3oiuBZCqZ39x02bhdQlYk6WWNDMEA3mJO08vZRpvmf9Sg00qePXkuWHTvsA-43WDTeoHX2Pgp2v24gvkeNcj3AhsepxZqClun0Vm_VHfmLb6XQMrUzXQfldIUWZtSkIYG-NTc6afIufXQgDDgy77Wf5IrKAU0bBochQaeo-D9nYHNNIm0CHIUPomLIAATD5WW3K7CzH0Nq563mxoNcjEWp5i7cRzxXHPh8BUrfc8yNnfLhgeuF2eYiwpCuUE-n8A2-WJqARx5SrHcVj9DvdEqr4yMI0jwcmZA1yUr6C4KCEBGpS3DnWUayAXQgjASD5TsDy5GuHPTjofeSprF570KTQXpjiiqNS3_9wqVJ0A18BqTel0IND5J-PkZnNzS_OhKd5MAtzqYJhTIyrNJY8Gw-5Ph86zEizuuZB8vJ8UTBZU-0P3zu0K4PlVSF4kF6ZkM78JTIpF2XGHg-_z7iCW_YokcinZdnDBBBkGQV1qbVVewIwKtWaT_tvnNkPsCaugxGH-ItcTojfQ4R_rTLyLzAK8Dxq70pTYgLnlER5WmcAh4Pzq_h-jJwevIbHNniYls4qG3TiIzKf4U9JohMWxrQOCiw5xTrv0fxXs4VbbqaGoGD6u4j15cbIpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ایران به‌شدت خواهان توافق است.
آن‌ها مدام تماس می‌گیرند. می‌خواهند توافق کنند. اما باید توافق درستی باشد؛
من تن به توافقی که خوب نباشد، نخواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/71578" target="_blank">📅 17:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71577">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=SeALfdY0WLwvRu5QZsvo-nM_eqMLLCWPbBPVgSf8Fr5mZ2gICZBmx0LED-LBfw9CdETZth2lK2bINai04aQghd366G7dwL_e2-jYjztxXsM3UgO3suFO_C-Zyh_WfptOegYk_FGNZO131WnCyhyFgCpqnCVNNAy2gf8iAT2zeLNOjYcyIwCU_fCnqOoF6grRcR4MIwf0s4npFSTAeaped3Y3wKf1FfRxJO1g8LZH_aYnLs9dTy2tI_woW2y1BHnJxq3qX36cZFWpXLWJzKVO4LN-40UpoIiM5m1dClPg_VD9DKyKjE37_T9bEYHKcYI3Ey6yVvCXfsnNgqHhkdKIuFJLSqIAqR35p5OKOOiFNMvyzwmv2PepDAf1JXfmnaK_M2aMuHsF4wqu16AKzxaj8FXbGTj0WtbpqUCQEG9Xi7upUPbE5Fl9_vRLecyI6X2Zcp_OhkPCfWh6CKQSUquT9w82qK9cQQN3nWG1MVrnBn1Zn99xUNxQHFzKGfp65UJvSuUwteDrjQmho3T5bKzSnQrfqMHY_Skwk04q5Xua4kQay6v4W0H_HIhXDYASMHKeoz8Tnpy7nfLF4ABUfeQjLtEj6odPwrNL8tfrrk2cf_-2mlWXBrRb8cDwTjMveVAD84Cb050Us8r8Nr7ZNaVri9I3r96M7uBNgeHrtxAS83U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=SeALfdY0WLwvRu5QZsvo-nM_eqMLLCWPbBPVgSf8Fr5mZ2gICZBmx0LED-LBfw9CdETZth2lK2bINai04aQghd366G7dwL_e2-jYjztxXsM3UgO3suFO_C-Zyh_WfptOegYk_FGNZO131WnCyhyFgCpqnCVNNAy2gf8iAT2zeLNOjYcyIwCU_fCnqOoF6grRcR4MIwf0s4npFSTAeaped3Y3wKf1FfRxJO1g8LZH_aYnLs9dTy2tI_woW2y1BHnJxq3qX36cZFWpXLWJzKVO4LN-40UpoIiM5m1dClPg_VD9DKyKjE37_T9bEYHKcYI3Ey6yVvCXfsnNgqHhkdKIuFJLSqIAqR35p5OKOOiFNMvyzwmv2PepDAf1JXfmnaK_M2aMuHsF4wqu16AKzxaj8FXbGTj0WtbpqUCQEG9Xi7upUPbE5Fl9_vRLecyI6X2Zcp_OhkPCfWh6CKQSUquT9w82qK9cQQN3nWG1MVrnBn1Zn99xUNxQHFzKGfp65UJvSuUwteDrjQmho3T5bKzSnQrfqMHY_Skwk04q5Xua4kQay6v4W0H_HIhXDYASMHKeoz8Tnpy7nfLF4ABUfeQjLtEj6odPwrNL8tfrrk2cf_-2mlWXBrRb8cDwTjMveVAD84Cb050Us8r8Nr7ZNaVri9I3r96M7uBNgeHrtxAS83U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ماجرای ایران درست بعد از انتخابات میان‌دوره‌ای تمام می‌شود؛ شاید هم قبل از آن، اما قطعاً بلافاصله پس از انتخابات میان‌دوره‌ای پایان می‌یابد.
قیمت بنزین به‌شدت سقوط خواهد کرد،خب، من می‌دانستم چه کار می‌کنم و باید آن کار را انجام می‌دادم.
ایران نباید به سلاح هسته‌ای دست پیدا کند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/news_hut/71577" target="_blank">📅 17:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71576">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=pyt6aAvfXKlP9U2vTLnCPl5uvPKeSWGKgQAcO2sTAUSseQ3AMqIFii449FGIWcJj33w4_zns0nrDpo1gAyOWrDKmXpOswJeLvCufXAwkCPKpYiyxeWPYlm1HUI3s-T9CAK5uzZ2wX7n1gG1bf_Y7c2Amswg_YniTLvKaFoOARIFmHFM6DiT8Jdd_IsqESqCz8N0iAnmgtoSDSne-gMq5QUIL_EYEOmiNPlEFdBDZEQsQ9xMOnMH7h9z0oIjA07zJcReyZdLfCDppBAsvSlqraZvuVz266ymO_7fudEJlwksPW6N310V-jaMli69SCXSswRD-X36ixX80PHW-N-gBNDXPHnGZV4HldoQ42YL5qxv_9Etk23UTpaV-J_jzBH4uIgSYPf_GaFrA1SLdMHJ4rUjYsZny6yIHnB7Z4JWmfBU3zHR35vQNm5mJBO2YTFUAOtEE-rtEUfxDgrCt90o7ignmuQZj2ps4QewNQpTBYM0sVn81ifdcPn95FjxgZV7hbvumpv8vyDpQ0OewP3KDCQv9yvM8en7j3hlUY774axoC2fsa-C6w-zvgy2tbVccnR2Px9N0mecEwUopVqpUOT4DSPQM36nmr_P2bv_kcVaFJ5dBSt7LprHP0zLR3t9ClJel2C6WsUkKMirt-27LkBs37XD4uIDNTRIjzFaOIdjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=pyt6aAvfXKlP9U2vTLnCPl5uvPKeSWGKgQAcO2sTAUSseQ3AMqIFii449FGIWcJj33w4_zns0nrDpo1gAyOWrDKmXpOswJeLvCufXAwkCPKpYiyxeWPYlm1HUI3s-T9CAK5uzZ2wX7n1gG1bf_Y7c2Amswg_YniTLvKaFoOARIFmHFM6DiT8Jdd_IsqESqCz8N0iAnmgtoSDSne-gMq5QUIL_EYEOmiNPlEFdBDZEQsQ9xMOnMH7h9z0oIjA07zJcReyZdLfCDppBAsvSlqraZvuVz266ymO_7fudEJlwksPW6N310V-jaMli69SCXSswRD-X36ixX80PHW-N-gBNDXPHnGZV4HldoQ42YL5qxv_9Etk23UTpaV-J_jzBH4uIgSYPf_GaFrA1SLdMHJ4rUjYsZny6yIHnB7Z4JWmfBU3zHR35vQNm5mJBO2YTFUAOtEE-rtEUfxDgrCt90o7ignmuQZj2ps4QewNQpTBYM0sVn81ifdcPn95FjxgZV7hbvumpv8vyDpQ0OewP3KDCQv9yvM8en7j3hlUY774axoC2fsa-C6w-zvgy2tbVccnR2Px9N0mecEwUopVqpUOT4DSPQM36nmr_P2bv_kcVaFJ5dBSt7LprHP0zLR3t9ClJel2C6WsUkKMirt-27LkBs37XD4uIDNTRIjzFaOIdjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، آیا فکر می‌کنید کنگره باید آن ۵۰۰۰ دلار را تصویب کند؟
🇺🇸
ترامپ:
همان‌طور که گفتم، نمی‌دانم اگر جمهوری‌خواهان پیروز شوند، انجام این کار چقدر آسان خواهد بود.
صحبت از ۵۰۰۰ دلار برای تمام بزرگسالان کشور است و ما به‌راحتی از پسِ آن برمی‌آییم، چون درآمدهای کلانی داریم؛
وضعیت ما هرگز تا این حد عالی نبوده است. دموکرات‌ها نمی‌توانند چنین وعده‌ای بدهند، چون در آن صورت اوضاع بلافاصله به هم می‌ریزد و نابود می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/news_hut/71576" target="_blank">📅 17:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71575">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=b1WnO7FW_LxLArs-4VRZ0WoDXVj4QzOdQa4iJvFQBHEsgtAftkhuojjCV9Fc66bygnJW1juPHQMuPCfIo8QaRQJBpAtfTBOXzS5NQzOaA-jnlaHVIwwAmErZm7zixVTOBGJLmAY8fcgTWfwa_7GLN6IHV68J7iUSJlaukSabe6RLHIwbunMQQ25ZQ5P2iTJnNQvC9maRjU_83w1MaTMbAwoqHZIagqOlylUbCP2NOHfruKaWggq0RBwXJKLJ19n9RJ3kgFkV_iS7_7_EBWkOSeD_EzNij_1kv7EG2iSH_1WEopOQdmATl16igHca7aATlExXLbplBFvgUD4QQ1Na5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=b1WnO7FW_LxLArs-4VRZ0WoDXVj4QzOdQa4iJvFQBHEsgtAftkhuojjCV9Fc66bygnJW1juPHQMuPCfIo8QaRQJBpAtfTBOXzS5NQzOaA-jnlaHVIwwAmErZm7zixVTOBGJLmAY8fcgTWfwa_7GLN6IHV68J7iUSJlaukSabe6RLHIwbunMQQ25ZQ5P2iTJnNQvC9maRjU_83w1MaTMbAwoqHZIagqOlylUbCP2NOHfruKaWggq0RBwXJKLJ19n9RJ3kgFkV_iS7_7_EBWkOSeD_EzNij_1kv7EG2iSH_1WEopOQdmATl16igHca7aATlExXLbplBFvgUD4QQ1Na5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
نظر شما درباره دیدار کشورهای حوزه خلیج فارس با ایران چیست؟
🇺🇸
ترامپ:
برایم اهمیتی ندارد. این به خودشان مربوط است. اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/news_hut/71575" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71574">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=kX-C7NkAMrocq_KexHQc9lLvPPGTwWneUxXs6AIGVxt1TDZkTNzLKt8jrS44bme6XDQPgIQ17xLl_izX8S3S2nI_WeMsmqddXor_VGx6yO9cELBuzR9EjOEf7IzG0IWxjJ_083hoRwdn2mdCSPOOvf1bST3bui-BNjdGSUBXvaGdNKI4Z0AbTHT90k_6gg0-wnfNOMO_F9-a4079qX4DZv9XyqOq_dt1NwLYiJRbE-cmeAlK9_-TZo_2B4RlvbENniX8HqPe3Q35A-0E-Iz8Qgvwq_-LL393BTsds2T12lkX_fg4pqp-iaadZg62GBg77lv-zc15MbJGBHdmkmkFWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=kX-C7NkAMrocq_KexHQc9lLvPPGTwWneUxXs6AIGVxt1TDZkTNzLKt8jrS44bme6XDQPgIQ17xLl_izX8S3S2nI_WeMsmqddXor_VGx6yO9cELBuzR9EjOEf7IzG0IWxjJ_083hoRwdn2mdCSPOOvf1bST3bui-BNjdGSUBXvaGdNKI4Z0AbTHT90k_6gg0-wnfNOMO_F9-a4079qX4DZv9XyqOq_dt1NwLYiJRbE-cmeAlK9_-TZo_2B4RlvbENniX8HqPe3Q35A-0E-Iz8Qgvwq_-LL393BTsds2T12lkX_fg4pqp-iaadZg62GBg77lv-zc15MbJGBHdmkmkFWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
در نهایت ما آنجا را ترک خواهیم کرد، مگر اینکه تصمیم بگیریم بمانیم و نفت را برای خود نگه داریم؛ درست مثل ونزوئلا.
دیگر درباره ونزوئلا حرفی نمی‌زنید، مگر نه؟ خوب به این موضوع فکر کنید: میلیاردها و میلیاردها و میلیاردها دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/71574" target="_blank">📅 17:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71573">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
حوثی‌های یمن تصاویر مفصلی از عملیات نظامی جدید خود با عنوان «و خداوند از نظر قدرت و کیفر، سخت‌گیرتر است» منتشر کردند؛ ویدئویی که صحنه‌های نبرد در جریان تهاجم اخیر آن‌ها در ساحل غربی را به تصویر می‌کشد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/71573" target="_blank">📅 17:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71572">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=Cb0SvG0p46YvokreNG8a57p6LnQDo7fMsHqOEH5k-85NLTb0sYn40_rIJxHRtaLsCIXpStBqpE447ouNKPEGGnSuSUGnwYZamFAV3YnR4DRGATDuXvMlGN5hkj4MMfXvjHMnr0fN6w5wACvRiZ_7HomfrvjdLrCLJZXXpBxzrgR0Yn0sZuAITXjoXNEOacYzKAUpqlVI5GsSfMr5Oyb6qxgZyVQR7AEdaUKmxl2ZFiKORJ5OJQrpxHqfsLiv9CfHhZQ9JyzWO6jc8PpB3d_iXjXAYFu7vQLAj817hb5IogL9aUTUxRtyT1EShaVrRMNkZK7LTeZ1Agsy7tMc92Wuww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=Cb0SvG0p46YvokreNG8a57p6LnQDo7fMsHqOEH5k-85NLTb0sYn40_rIJxHRtaLsCIXpStBqpE447ouNKPEGGnSuSUGnwYZamFAV3YnR4DRGATDuXvMlGN5hkj4MMfXvjHMnr0fN6w5wACvRiZ_7HomfrvjdLrCLJZXXpBxzrgR0Yn0sZuAITXjoXNEOacYzKAUpqlVI5GsSfMr5Oyb6qxgZyVQR7AEdaUKmxl2ZFiKORJ5OJQrpxHqfsLiv9CfHhZQ9JyzWO6jc8PpB3d_iXjXAYFu7vQLAj817hb5IogL9aUTUxRtyT1EShaVrRMNkZK7LTeZ1Agsy7tMc92Wuww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی مملکت یه سری کارگاه آموزشی گذاشتن و به افراد بالای 60 سال آموزش میدن که چطوری اسنپ بگیرن.
هزینه شرکت تو این کارگاه بین ۱ـ۲ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/71572" target="_blank">📅 16:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71571">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=a8AB7E8K5HM-KZbCWlkiK-T-VEKFOhVjVnVfy-vyN3Z_5cdqw7PoUuzhgAL_jBul5iqbX6CgDn40m_P9_oIZVQ9kyN0uoCntPdJ0v3WQ7VQ8XzTHHtLXx3lP_jye1uWim5y7X5AMEEN4Go7mbuPuXu1kH3gOf5ng0A-CPGrU_ec-mueSvtKSjdTKMKyoKqioH2iTvG-dzBEkldx1PUp2G9zJ0mv6DAbxFBH5PjXQgEGmVX1iE7rvngkM8gq-UtXWK9942L8iOpOhqFmtyXGy8IT5hj3zfMhB-fUFpT7MdOwsEaNygQuaZ3ER_qwPiwAAjQuEkPmh8BMO36lydaA8QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=a8AB7E8K5HM-KZbCWlkiK-T-VEKFOhVjVnVfy-vyN3Z_5cdqw7PoUuzhgAL_jBul5iqbX6CgDn40m_P9_oIZVQ9kyN0uoCntPdJ0v3WQ7VQ8XzTHHtLXx3lP_jye1uWim5y7X5AMEEN4Go7mbuPuXu1kH3gOf5ng0A-CPGrU_ec-mueSvtKSjdTKMKyoKqioH2iTvG-dzBEkldx1PUp2G9zJ0mv6DAbxFBH5PjXQgEGmVX1iE7rvngkM8gq-UtXWK9942L8iOpOhqFmtyXGy8IT5hj3zfMhB-fUFpT7MdOwsEaNygQuaZ3ER_qwPiwAAjQuEkPmh8BMO36lydaA8QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیویی جالب از یک پهپاد اوکراینی که به سمت یک کشتی روسی در حال حرکته و یه بالگرد روسی تلاش می‌کنه اونو بزنه ولی، این پهباد در نهایت خودشو به کشتی میرسونه و منفجرش میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/71571" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71570">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=dO6z-tE9xhCp5OGePrI0RLOFQgjCHUGRdmB6vUYlOohjdqDxbU88aBlru01toNithPLjFbgavXSL19hpSs28TYjFv_pGwHrcGD5GxVXV1yNSi3iV32Yc-EP2P67wUXvXIPjzd4JOTPZQZA_R9p-OL58-6RRL41NkNct_wTiyJR-1Zsj2UWWffzzCCqp8LEvTN-67fCRi4HoB8_PyhTOnx48k1G1NjsoF2rO5oI96t3DNwe-njOjZCBzNRBRC647u8_1Dp79ox40_zm2x5GiPaxQG1oXfvaPAb8Ph9EcrLQjWuJQS98Sa2SFTKKzlqSgAb8DNZpCsyJXeDX28upGpgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=dO6z-tE9xhCp5OGePrI0RLOFQgjCHUGRdmB6vUYlOohjdqDxbU88aBlru01toNithPLjFbgavXSL19hpSs28TYjFv_pGwHrcGD5GxVXV1yNSi3iV32Yc-EP2P67wUXvXIPjzd4JOTPZQZA_R9p-OL58-6RRL41NkNct_wTiyJR-1Zsj2UWWffzzCCqp8LEvTN-67fCRi4HoB8_PyhTOnx48k1G1NjsoF2rO5oI96t3DNwe-njOjZCBzNRBRC647u8_1Dp79ox40_zm2x5GiPaxQG1oXfvaPAb8Ph9EcrLQjWuJQS98Sa2SFTKKzlqSgAb8DNZpCsyJXeDX28upGpgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صداوسیما:
از جنگ تحمیلی دوم حدود ۱۵ ماه اینا هست میگذره دیگه
مقامات صهیونیستی و امریکایی پر تکرار گفته ان که با حمله به ایران ظهور مهدی موعود رو به عقب انداختیم
دلیل اصلی بمباران تاسیسات هسته‌ای ایران به عقب انداختن ظهور بود
اونا نگاهشون آخرالزمانی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71570" target="_blank">📅 15:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71569">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4RzSDinXB2rXae08HrWUoHH4Un70GtuSWwd5rla5yd6O1sQ_Q2vBzzr-bour1jJ-yI8GSpLxQwByB9H0f4YiLVDW77SHYeUknAlS_8eHkqAA6IixrOJVMyPhRyI-AkXEksbY4_mxp-DRzSfEyYaFtYLCwZFDvojlmlMXUydijlwzV9O8JnvK650wtCpiR1_zBZB3-n-JGbqczhDp-ZKVCodqAJ9NiivironV9cIPtrjNTxY7JOM2-h8cHhUTP5dJL_iE_Q8O0EO7wGfT7m4Qg2bIFhxl-8Tu9HarM32-Nbh_6lXyw_GaJnViNA-pLDz-SDRAdT4Q2ZXkbiVxfbCDR1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4RzSDinXB2rXae08HrWUoHH4Un70GtuSWwd5rla5yd6O1sQ_Q2vBzzr-bour1jJ-yI8GSpLxQwByB9H0f4YiLVDW77SHYeUknAlS_8eHkqAA6IixrOJVMyPhRyI-AkXEksbY4_mxp-DRzSfEyYaFtYLCwZFDvojlmlMXUydijlwzV9O8JnvK650wtCpiR1_zBZB3-n-JGbqczhDp-ZKVCodqAJ9NiivironV9cIPtrjNTxY7JOM2-h8cHhUTP5dJL_iE_Q8O0EO7wGfT7m4Qg2bIFhxl-8Tu9HarM32-Nbh_6lXyw_GaJnViNA-pLDz-SDRAdT4Q2ZXkbiVxfbCDR1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇾🇪
تصاویر بسیج قبایل حوثی، ستون‌های طویلی از خودروهای تویوتا (تکنیکال) مجهز به سلاح را در بیابان به نمایش می‌گذارد؛ تصویری که نماد کلاسیک جنگ یمن است.
قبایل «بنی‌حشیش» برای پیشروی به سوی «مأرب» — آخرین پایگاه عمده دولت در شمال — اعلام آمادگی کرده‌اند.
وانت‌های تویوتا مجهز به سلاح، همچنان ستون فقرات نیروی زمینی حوثی‌ها را تشکیل می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71569" target="_blank">📅 14:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71568">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRCZJIJuQWtzaUxPAoL_6TT8UqFzw9B-EEvM19uEXfeEDkWc6E2ty_joRTlcX2YYNYsVAoMfZuLedG3BIRLFKphQlfjx9NjmwgAGIgNT5jjesjmFBVZnQ4aCX79YODsjO2BJd0Yw1goqYiofoK_WwUmVSp-Bog_OEIMHe83XbiZSnmMKqcTHywa3SjF53gozJGVONOc4oV3yde9C7GnzDY77cSWCK-tz1jb0qgdid638H5xRTMRJDdDsoCJeXGkao-ds2Q_E4jp1twGEGzsB0lawMSjxMUd6cGEf-CguQ98yCHQWkKpcJoXPX_P1dSXu4OCQr-VoU4kGALpMHa1HrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس: محمد بن سلمان، ولیعهد عربستان سعودی، روز پنج‌شنبه دو بار با دونالد ترامپ، رئیس‌جمهور آمریکا، تماس گرفت و از ایالات متحده خواست تا هم‌زمان با پیشروی حوثی‌ها به سوی یک نقطه راهبردی و حیاتی در دریای سرخ، به آن‌ها حمله کند.
ترامپ این درخواست را نپذیرفت و مقامات آمریکایی اعلام کردند که در حال حاضر هیچ برنامه‌ای برای مداخله مستقیم علیه حوثی‌ها وجود ندارد.
دریاسالار کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، نیز روز پنج‌شنبه برای هماهنگی‌های اضطراری به ریاض سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71568" target="_blank">📅 14:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71567">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=eHcCaHwzZNauaXrVghd8dA7RhBYdmqssfex8Z6vYxWQkwsw3B-yLcFNNYR6K4w5U2ImFxMir8I8VqrFdkvkD-p3sh7h1V2Pnhp1H0iFGvC50GRJY-mEEhbrib_e_VqSN3xyX6APmvpPNzhq7MFXPAqIrQ12oomnPTNgO3hgw1R974Z9Ap8XkJecp87hlEkjgdEXIY4MUkxGtMkVoEzcEaqB9N6YzCLIDUKLPr6pRAAZo1IDscceyBWFQ2tOnDazFtBDR1OJ0xztumBb2d9uIM5VTts_nF7tIpXPFAbJnjmoEVxQQv2Sm98__F-l8Rhxxd1c2yt7TWjNp_E4pz8mWoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=eHcCaHwzZNauaXrVghd8dA7RhBYdmqssfex8Z6vYxWQkwsw3B-yLcFNNYR6K4w5U2ImFxMir8I8VqrFdkvkD-p3sh7h1V2Pnhp1H0iFGvC50GRJY-mEEhbrib_e_VqSN3xyX6APmvpPNzhq7MFXPAqIrQ12oomnPTNgO3hgw1R974Z9Ap8XkJecp87hlEkjgdEXIY4MUkxGtMkVoEzcEaqB9N6YzCLIDUKLPr6pRAAZo1IDscceyBWFQ2tOnDazFtBDR1OJ0xztumBb2d9uIM5VTts_nF7tIpXPFAbJnjmoEVxQQv2Sm98__F-l8Rhxxd1c2yt7TWjNp_E4pz8mWoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کنعانی مقدم:
اگر رهبری اجازه دهند، ظرف ۲۴ ساعت از سلاح هسته‌ای استفاده خواهیم کرد
خرید فیوز هسته‌ای از کره شمالی، کار خیلی ساده‌ای است و ۵۰ تا فیوز می‌توانیم بخریم
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71567" target="_blank">📅 13:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71566">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=qrZ1j8E8z--WK-8pg1kvEvcdrgJyA5ASnrujxv3_0GkaFYioIbRrD9zCe7UsZ07j4Z0tomhaURvXcjO7yCL9-bmTwODHXkWUY8ZQRYoIGG5mwaHH1W7cg3-h8XeWJhl1GYUJsH0V7MnRMkvUi1YhecFSIFkI-u1uHO4CS9-t61T6-xw218mh5ijQRlRXcxYt-p1cdyohsqOlf3ksigVyvNwQrTOkeqi6kUmizJ6RNjxIq8FgNtxcSzpghM1GAJu8dejey8nmf0d0TlZhauWxMebq71giqxtYyfTGcNC0dirBCERoY7s8ik-fJDMlPmQ8NUkijYNHtmIcKUhadTD8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=qrZ1j8E8z--WK-8pg1kvEvcdrgJyA5ASnrujxv3_0GkaFYioIbRrD9zCe7UsZ07j4Z0tomhaURvXcjO7yCL9-bmTwODHXkWUY8ZQRYoIGG5mwaHH1W7cg3-h8XeWJhl1GYUJsH0V7MnRMkvUi1YhecFSIFkI-u1uHO4CS9-t61T6-xw218mh5ijQRlRXcxYt-p1cdyohsqOlf3ksigVyvNwQrTOkeqi6kUmizJ6RNjxIq8FgNtxcSzpghM1GAJu8dejey8nmf0d0TlZhauWxMebq71giqxtYyfTGcNC0dirBCERoY7s8ik-fJDMlPmQ8NUkijYNHtmIcKUhadTD8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎯
ویدیویی از هدف قرار گرفتن نیروهای انصارالله توسط نیروی اسنایپر مورد حمایت عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71566" target="_blank">📅 13:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71565">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=i3Ks90fpRi1db52xpdk65WNXG3OtqXvGzCvB00r5mHegXYSsgn51F_RuWghyxrW2P_pOwPWA2zqSnfsjyAXcq3xgIKmTKDcXqB66iqGyANyMTr-8rO1UIfzfpP2piO5g_zuduCzaYnA7uhGjWfTxDYXtfSD84iN1JPDGr7_Yxy0qP5_nqKKMMQHsdeUU9XXqmzBEiiXzXUcI4-QFvZH1AgHTVUp1k73A2u0jNMgN_bb3HXfeSIZxzGtByHTVUqcpXHN5gg6TMfpyfmhxaMT1cwfLp_BPbYQI8bQs-EtwOenHIzmPUIkMH0vlwa72JnfEDlJpjyZtGaQZx8STEtDncA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=i3Ks90fpRi1db52xpdk65WNXG3OtqXvGzCvB00r5mHegXYSsgn51F_RuWghyxrW2P_pOwPWA2zqSnfsjyAXcq3xgIKmTKDcXqB66iqGyANyMTr-8rO1UIfzfpP2piO5g_zuduCzaYnA7uhGjWfTxDYXtfSD84iN1JPDGr7_Yxy0qP5_nqKKMMQHsdeUU9XXqmzBEiiXzXUcI4-QFvZH1AgHTVUp1k73A2u0jNMgN_bb3HXfeSIZxzGtByHTVUqcpXHN5gg6TMfpyfmhxaMT1cwfLp_BPbYQI8bQs-EtwOenHIzmPUIkMH0vlwa72JnfEDlJpjyZtGaQZx8STEtDncA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
این رهبران جدید و رهبران واقعی که رئیس‌جمهور ترامپ از آن‌ها صحبت می‌کند، چه کسانی هستند؟
🇮🇷
پزشکیان:
به گمانم باید این را از خود او پرسید، چرا که هر روز حرف متفاوتی می‌زند.
یک روز می‌خواهد ایران را نابود کند و روز دیگر می‌گوید ما دوست ایران هستیم؛ یک روز می‌گوید ما را به رسمیت می‌شناسد و روز دیگر می‌گوید ما را قبول ندارد.
بنابراین، ما مطمئن نیستیم که باید کدام اظهارنظر را بپذیریم و بر اساس کدام‌یک عمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71565" target="_blank">📅 12:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71564">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71564" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71563">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4eYwVEm7Pa9hFanOE-glFn_GiuG1iPmpVTQ7FfMlxglDaAaoYWbjd4ZWreNmqmDcLT_ShGTGGJS43CRrB56Zt0cjns2SRRRABOGO1IlC8BRDj-HisQ-WmTe9j6G9DUTlaT6xWQFmmlC3qB0nAic3JUIhwyAcDVC-upQ8wn-JlV4ByxZhift8VrD5zB59a9rKwQzJ-VIbmODeo8siaYsXhmp6kQ_7cPEYJApPGaKSCqt1ttGnxBc-6pJfoYeVzMAPNr88wv2DodvuZvsbRW-l8gbv4AjAEDqldBd6JM5L-w_AOVFlWXz0FyE3IMjt1R2piH7t2O3L73kaSD6emqP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد بزرگ منچستر در راه است!
نبرد هیجان انگیز
⚽️
منچستریونایتد
🆚
منچسترسیتی
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ دربی اخیر منچستر:
⚽️
منچستریونایتد: ۲ برد، ۲ تساوی، ۱ شکست و ۵ گل زده
⚽️
منچسترسیتی: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71563" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71562">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaRvadwEeb8wKN7pRj3G-8g1txTgAhotpYyvKijSTFvpbBSpZ7khFj0k4kcRfxtXNgZ7UcKrPsgRtjbrF7SWhd2kAxHvP6upmXlU9tJpLyZmfGBuYMN9Z3r_tLO5cvXpk9oNKB7p22efvLaE7As-QPmm100b486FPra1FFJ9SHMcBcgB9oIo13mQ8-dKFb5uiNdBogHtNugavbFiq-gdYMDcJdou4BCxbEiktBZbo1iFWbBS6PEnFb2FtZNF_lANfEQp2u2HjUw9myWEWDVqdDUOxW1pmRSWsmiC7LpqHT-3eXykx5qRhLst_-IVJfvsk8smIGVnQHMY0XVfBX9XlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
روز یکشنبه در گزارشی اعلام کرد که بر اثر اصابت یک پرتابه ناشناس به شناوری در حال عبور از تنگه هرمز، در آن کشتی آتش‌سوزی رخ داده است.
این سازمان اعلام کرد که مقامات محلی در حال کمک به تخلیه خدمه کشتی هستند. در این گزارش، نام شناور یا اطلاعاتی درباره تلفات، خسارات و یا پیامدهای احتمالی زیست‌محیطی آن ذکر نشده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71562" target="_blank">📅 11:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71561">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
🇯🇴
ویدئویی از پرتاب انبوه موشک‌های رهگیر «پاتریوت PAC-3» از پایگاه هوایی «موفق سلطی» در اردن در سه روز گذشته، برای مقابله با موشک‌های بالستیک ورودی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71561" target="_blank">📅 11:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71560">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=l4dTAJfhQybP3i2Zyv7jdH2LCqton29PTGaOd9z2_xDSGI6DDOE9--LOcfF2ULasqZnNspe58fSbH4LtbYPuftABpLCakjB7Jp3ZAYxpCwtbdbLg208YJWx7Ms6xBTwFXpUN4UaxI5a-b7HL2Dm-rGObbXJMUTxX4pX02Umxh86MT-k9iY2XvdXYn8A8j4BDSKCWdEBgsYqrPRVTRrxCII8rifNwcl2hbG-_NBChGry-D7cvydQKWQSUXjI6zZAU_1HWz-IgZYrYAu5czyWhq3oz4nreI5U0qTBG_KoMsZLJvPyb2F34GPDp-BC3tu1pt9J0p3hC5AHkMAlFZQ5pTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=l4dTAJfhQybP3i2Zyv7jdH2LCqton29PTGaOd9z2_xDSGI6DDOE9--LOcfF2ULasqZnNspe58fSbH4LtbYPuftABpLCakjB7Jp3ZAYxpCwtbdbLg208YJWx7Ms6xBTwFXpUN4UaxI5a-b7HL2Dm-rGObbXJMUTxX4pX02Umxh86MT-k9iY2XvdXYn8A8j4BDSKCWdEBgsYqrPRVTRrxCII8rifNwcl2hbG-_NBChGry-D7cvydQKWQSUXjI6zZAU_1HWz-IgZYrYAu5czyWhq3oz4nreI5U0qTBG_KoMsZLJvPyb2F34GPDp-BC3tu1pt9J0p3hC5AHkMAlFZQ5pTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نظرات متناقض هادی چوپان درباره هانی رامبد:
بعد از قهرمانی
بعد از جدایی
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71560" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71559">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097559287c.mp4?token=M8BQDzaxOr6A4KapiV79BKl6CqBANJCn5hJws7kqIO94HQMN6bjrU-oyeQTSRRKWO32Xy0oR_rZC5ks1I5UGUJUl4-upMYEEO4dSKAyHPvJLyBtUCDal0ZOd2q41FEw7-P_X2wA1Tslf9OmRcE6pf25VlpBy2K4wUsfUaVmvtn7N0JUKNhQdrvkgZqFBN1MYb-9r6JCS6tpIVxKYWYYprem4vTvz-yAjyoD5hL-Tszhxf9lNY2_lZ1YD2jLotxmeX5oePG4vxs_Te9pUPwatkUOZOTlrYkPzq-Svx0o0odcUQToWCoyWGUfaR3ecLAKuCfwefXIy5okDJZjcrRMPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097559287c.mp4?token=M8BQDzaxOr6A4KapiV79BKl6CqBANJCn5hJws7kqIO94HQMN6bjrU-oyeQTSRRKWO32Xy0oR_rZC5ks1I5UGUJUl4-upMYEEO4dSKAyHPvJLyBtUCDal0ZOd2q41FEw7-P_X2wA1Tslf9OmRcE6pf25VlpBy2K4wUsfUaVmvtn7N0JUKNhQdrvkgZqFBN1MYb-9r6JCS6tpIVxKYWYYprem4vTvz-yAjyoD5hL-Tszhxf9lNY2_lZ1YD2jLotxmeX5oePG4vxs_Te9pUPwatkUOZOTlrYkPzq-Svx0o0odcUQToWCoyWGUfaR3ecLAKuCfwefXIy5okDJZjcrRMPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
تلاش ابی برای بوسیدن دست یکی از بازیگران برنامه عشق ابدی که ویدئوش به شدت در حال وایرال شدنه!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71559" target="_blank">📅 10:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71558">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=IozFKnLVQtjleAst_awlqq0ulzkUiZS3e8dKVkMf6ROZPGLk5URu00jO9vMvsmYODPU-wx3fzMLI0OMpAbnaG04HlYypntEZNMBp_P4AYz2W44ylzRI4HNB0i0MzMzXyV3GpdAQsiB2qZLft6PRnAPgnwDUbVBCpeYY79zMRD9u-ZWkCPYY6ZUIRdWncCKOdgzAxlkesW7SvuNbeutV_ezIQXrLyNmNhEv3ivSu3Nty13bg70Nbsb7PURdUNjFP6iKIUiSfGcwzkvxAbz_GHmrlJPvE1Mjjr0pjKnbgm447RnOZfvHBCngzFUEsjz2xK4i2qkwnkUwIFlpHmBOn5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=IozFKnLVQtjleAst_awlqq0ulzkUiZS3e8dKVkMf6ROZPGLk5URu00jO9vMvsmYODPU-wx3fzMLI0OMpAbnaG04HlYypntEZNMBp_P4AYz2W44ylzRI4HNB0i0MzMzXyV3GpdAQsiB2qZLft6PRnAPgnwDUbVBCpeYY79zMRD9u-ZWkCPYY6ZUIRdWncCKOdgzAxlkesW7SvuNbeutV_ezIQXrLyNmNhEv3ivSu3Nty13bg70Nbsb7PURdUNjFP6iKIUiSfGcwzkvxAbz_GHmrlJPvE1Mjjr0pjKnbgm447RnOZfvHBCngzFUEsjz2xK4i2qkwnkUwIFlpHmBOn5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده از 9 اسفند - روز شروع جنگ و بمباران تهران و واکنش  دانش‌آموزانی که خرکیف شدن
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71558" target="_blank">📅 09:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71557">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇮🇷
امیر تیموری فرماندار شهرستان قشم:
یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
در این حادثه  یک نفر شهید  و سه نفر مجروح شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71557" target="_blank">📅 09:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71556">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5niBWDQuxAY443-mFwxPwO7c8T7kwAyIJVLG4KcpbfDA7yemd6gcjAxFPCIkDlWs3cizFGLdV1wp_2ArM2lVoA9aonaTxI1t872TZUdtB8Sb5YUQhgNgvcVzoOmpL50lw4piqUvLFKF0hH5FZRvkwnsl-GAU5D6WJSl4lw7QNdv8gfAFUVbL2bkEKgMTqhdtELdzkbACF6jMsvU8KcmnhWgLX1_TqM1Nyiu8uHBcTRtXDuO3Da9sq1glhuwNBGnPEg9oSsAp6tJXphgVrqnKzIGEWjj1ikR20F6sbuZufbT-5KW-DpRKQHPvAF-OjL_9qF2le-BhJBTDgwhnm09zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇮🇷
📰
وال استریت ژورنال:
مقامات آمریکایی می‌گویند ایران پیش از حمله موشکی بالستیک ۱۷ ژوئیه به پایگاه هوایی «موفق سلطی» در اردن — که منجر به کشته شدن سه سرباز آمریکایی و زخمی شدن چهار تن دیگر شد — تصاویر ماهواره‌ای با وضوح بالا از نهادهای چینی دریافت کرده بود.
این مقامات معتقدند که تصاویر مذکور با این حمله مرتبط بوده و احتمالاً به ایران در شناسایی دقیق‌تر اهداف ارزشمند کمک کرده است.
آن‌ها دولت چین را به مشارکت مستقیم در این حمله متهم نکرده‌اند و هویت نهادهای چینیِ دخیل در این ماجرا نیز مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71556" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71555">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی TREXBET !   فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛ اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی، Promo Code یک‌دلاری رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی! …</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71555" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71554">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeAZoezzRyXaRJVPqU1QqgwEfiGIywf8zSO5X_jlhUDevFdOuWiZfJK_PaGJPIlgZtJr3LqeyKCWK0x7t_167LLY3C-RmJt1zhcZwKLwZH5GY-JdCnRsbIswtK4LZ--OgumrErLHW42QMWQqBIgRYzfOGFbsAseG3x1dh1OWlfpQ9WqHSGcJ-BktYXrEN8ZIYc4uxPt1DW_CJ8m6srEzn0gnZCfPE4DpBBUsojn-Tiw1d09jw1lH7Oa7Vs-a02qpsjqBN21AIV3ZSz_uhU3EmddZ7LwiNIULk6sy7CZJhId9j_DohyGaJFZfUtDV0TvfjnrjfFr0eIy7aCCh9EZJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی
TREXBET
!
فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛
اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی،
Promo Code یک‌دلاری
رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی!
⏰
چالش اول → 18:30
⏰
چالش دوم → 20:00
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71554" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71553">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=ZOKHSiI9JQnTMv9NmcJPRoBHY1NGBxAN2DsZ309ztBedHjZ8P3DJAoncjvu4kR05cy4T6Hhzj5prmYJbyH3PGvQcBgITmDm_J4r-9UunBAmZuu5BM1pkd5spmJXsmP8bxiurjD5LgvWP9axLY3v1uovevy8SjwLMEwBouHpQqjOYwDgJlLfJwiaNE3oqFtMO9Y09u-aOexhx_Zlxjlsm7UPC-J-4vU2iSHDViymegfrOWCjv32bEPvrJp5r7LpRVX0cTcTh6YoK9BKRQlwabiSIEPVYD82a0E_1xotsPfMeDajQTH5olZJi4Kwghmgm2a_sMUdeafnpL_NdpMb_jJIDOtCPllUzEpNGajzkbfKhMTRKstug1Kj8BiStSXEPTcVe6dDMcMemWo3yaxZ7H9dIALgJzQI6dhzvtNZxWBXKa36pQ3EBnZyHj6nhJIOyKLRhzDd3sZJ3McQVrs2Lp0pTsRqcKRkhmxo0px3eoN9KL-ObA2T716mt2swvFUG56St6cACPgR5Kxjv7YCVh5f1gFFISlrAmYA4aHZ7icP9egp2E71Bjo4wWX3ToFfUJFNYdtcHXPa9HLu4K7NYn60lHJPsT7LDs9K2WmjXhuSNuK_cly2vaVOWexmumT7g2lBdWK_gtIqdPcXOnlZEW8do5uTZvLngQcFTKEOeYgBpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=ZOKHSiI9JQnTMv9NmcJPRoBHY1NGBxAN2DsZ309ztBedHjZ8P3DJAoncjvu4kR05cy4T6Hhzj5prmYJbyH3PGvQcBgITmDm_J4r-9UunBAmZuu5BM1pkd5spmJXsmP8bxiurjD5LgvWP9axLY3v1uovevy8SjwLMEwBouHpQqjOYwDgJlLfJwiaNE3oqFtMO9Y09u-aOexhx_Zlxjlsm7UPC-J-4vU2iSHDViymegfrOWCjv32bEPvrJp5r7LpRVX0cTcTh6YoK9BKRQlwabiSIEPVYD82a0E_1xotsPfMeDajQTH5olZJi4Kwghmgm2a_sMUdeafnpL_NdpMb_jJIDOtCPllUzEpNGajzkbfKhMTRKstug1Kj8BiStSXEPTcVe6dDMcMemWo3yaxZ7H9dIALgJzQI6dhzvtNZxWBXKa36pQ3EBnZyHj6nhJIOyKLRhzDd3sZJ3McQVrs2Lp0pTsRqcKRkhmxo0px3eoN9KL-ObA2T716mt2swvFUG56St6cACPgR5Kxjv7YCVh5f1gFFISlrAmYA4aHZ7icP9egp2E71Bjo4wWX3ToFfUJFNYdtcHXPa9HLu4K7NYn60lHJPsT7LDs9K2WmjXhuSNuK_cly2vaVOWexmumT7g2lBdWK_gtIqdPcXOnlZEW8do5uTZvLngQcFTKEOeYgBpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🟥
گزارش فاکس‌نیوز:
جنگنده‌ها از ناو «یو‌اس‌اس جورج واشنگتن» (USS George Washington) در حال برخاستن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71553" target="_blank">📅 01:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71552">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEo_jk_YzPIwW9VJA36CCG1whM4HDklxY2UnceDmV7xyZhNgjE3tkdVsPmsPDOz7eDy4jSVJpdcwqzebWc3ejz12E7WDWE_6wKpyNs88QJDWB8p4bUQUC6OuwdYYL2CzwTCuTowq3NC3JnJAKAm8FpI0kFQtewR54fLFAubqG-kMsx2usJHWAYVE5L7C6ECU5VLwbARZZnWODwL-7rQR958M4PP7qVppxgftrl99ZWAvEUwFLxLZqmOJKsseHQY7vJf64zQZofKPD1AJGdEw0wzU92m31a-MSXDr2n4ztBMgMbSAgXUa45wtfkh4pCg0erhsYE7j1ZKrn9tvWmGQhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛کانال۱۴ اسرائیل:ایران برای خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) و آزمایش بمب هسته‌ای آماده می‌شود.
حاجی‌دلیگانی، نماینده مجلس، از آماده بودن طرحی با قید سه فوریت خبر داد و افزود: «باید هرچه سریع‌تر آزمایش‌های لازم برای سلاح هسته‌ای را انجام دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71552" target="_blank">📅 00:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71549">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_pB17JBreSLNDp78-YcPC5S-ZMrgnTJXx1a0bJ0MmLpSqobCMqgVppuqrrh05SX5Vw9jYndYjvskVCQTNLHP4JqXK0BgAqAFJrNoXN9ITXUECv9uaaFEiNs_X9wpUso9pER_-9EXFqo-cuAWMor_1TS-R87m61ToCHSUjiExGFwLDdrh1t6j5LGdyo1wW8ijTi2VrXMVAIAenT5ZJ-6L143qgL8NU-hNkZqTV6D6EX5CDFUMpDUfPP6ieBEicyi4CytfZtpNmxonUaNEDFCAVxgHejDohI2iArdU2fW_YChGui8swoSZK6OkqieUaNMSvBAuUkJn3BNeyFIDza-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=NOxQW18TWwsrTBa1KwMJP19jDgKHmlZ1ZXUxZeiTJAPy5FVtNfFkaPP-CvUnkdVFhj0G0BVrJGBb7y0hXEtDRzh9hJoi7AU0Zu5X_ZkHOS4d7TeHgSV1ibIxWGoE8jKINXAZdfYHG8igNaKu4eSQ4Ljfu4cdqpS25nnD963tUMDY0lGhKFHe2S9KddrluK_grsWB4jAFKK_TSnKkeMifBRaLFEQQXwWfnKzNwlyfBCaJjFN_2EaJ1Q1TdcBUctP1xjC-HDq1F-syIZm7HvI4rMMAwoOmAulw7hXi9qifEfl979rbp1rwY2VRNIcOwo3JxJQ5sNqKb4KjOJu2b8eHFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=NOxQW18TWwsrTBa1KwMJP19jDgKHmlZ1ZXUxZeiTJAPy5FVtNfFkaPP-CvUnkdVFhj0G0BVrJGBb7y0hXEtDRzh9hJoi7AU0Zu5X_ZkHOS4d7TeHgSV1ibIxWGoE8jKINXAZdfYHG8igNaKu4eSQ4Ljfu4cdqpS25nnD963tUMDY0lGhKFHe2S9KddrluK_grsWB4jAFKK_TSnKkeMifBRaLFEQQXwWfnKzNwlyfBCaJjFN_2EaJ1Q1TdcBUctP1xjC-HDq1F-syIZm7HvI4rMMAwoOmAulw7hXi9qifEfl979rbp1rwY2VRNIcOwo3JxJQ5sNqKb4KjOJu2b8eHFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
درحالی‌که شرکت اپل ایران رو تحریم کرده، قمی‌ها طی یه حرکت عجیب، همزمان با مراسم معرفی محصولات جدید اپل، خودشون هم به‌صورت جداگانه یه ایونت برگزار کردن و از آیفون‌های جدید این شرکت رونمایی کردن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71549" target="_blank">📅 23:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71548">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=TXpnDMUGlslTBMSXberwThFq30XwvwRO3VVYVn4AHVBkoCbkP7jopMpVAtWja0RrmgNfIA5FFl4a4bJQkaG6n-Gzh_6IWiCjPcETMW7uCb2_paLgsmAZXgmdbuGkhoxF9RK0YqhLxz5mzM8quJv_25kMrq5kyzULmxgnnx-3H_N6-vscaMez1pTEfZkSmXOyFfun9zYP8MV4xTr6XDOA3-wyOK3CX2qcPuPoCL2r_AjBs4Do7w5DLrEhcBvIkJDM5ClzIz_ugVpnD4LmbAegYJVYEN9hXxC4NfzdUk5FGk8GaXaRZfJ5diDcSO1-ON_LejbjuZ1NJvt59gSmT-5bnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=TXpnDMUGlslTBMSXberwThFq30XwvwRO3VVYVn4AHVBkoCbkP7jopMpVAtWja0RrmgNfIA5FFl4a4bJQkaG6n-Gzh_6IWiCjPcETMW7uCb2_paLgsmAZXgmdbuGkhoxF9RK0YqhLxz5mzM8quJv_25kMrq5kyzULmxgnnx-3H_N6-vscaMez1pTEfZkSmXOyFfun9zYP8MV4xTr6XDOA3-wyOK3CX2qcPuPoCL2r_AjBs4Do7w5DLrEhcBvIkJDM5ClzIz_ugVpnD4LmbAegYJVYEN9hXxC4NfzdUk5FGk8GaXaRZfJ5diDcSO1-ON_LejbjuZ1NJvt59gSmT-5bnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
لحظه‌ای که جورج دبلیو بوش خبر حمله به برج‌های دوقلو را دریافت می‌کند
جورج دبلیو بوش آن صبح در مدرسه ابتدایی Emma E. Booker در ساراسوتای فلوریدا بود و برای دانش‌آموزان کلاس دوم در یک برنامه کتاب‌خوانی حضور داشت.
نکته جالب این است که بلافاصله از جا بلند نشد و کلاس را ترک نکرد. چند لحظه در همان صندلی ماند و سعی کرد آرامش خود را حفظ کند تا دانش‌آموزان وحشت نکنند.
چهره‌اش به‌وضوح تغییر کرد و حالت شوک و نگرانی در آن دیده می‌شود. دانش‌آموزانی که آنجا بودند بعدها گفتند تغییر حالت چهره او را به‌خوبی به یاد دارند.
جالب‌تر اینکه او حدود هفت دقیقه دیگر در کلاس ماند و بعد از پایان بخش کوتاه کتاب‌خوانی، از کلاس خارج شد و در همان مدرسه برای خبرنگاران صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71548" target="_blank">📅 23:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71547">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=Lmum7MK4gVHw0k9n5MVrFnJBLXoEIkGanWEe1u0QE1PRSdZG0xisAswLs-B1VpGLepD3Hbh9lV3pxYMglMtyOq6A8jtvA6Vg8urvd5caxltL8X2LjkIN8OVjQCAvjVYV8_7qtRdoIv3-OoyhLG0oGt59wLkG6nVUYAThjQxtJvK2wJ6-u0NJeKwelhCWAaZMmy8H0E0zdvxklhBFmQeWyL5_Zu0cl241AM3wVRTyAggQO_VtIVmCT_ei33OaQzeidiBcD3FyM9JcbdfUP-U9fewYfLA0k8wADUxSJRomo3JgJyO83B9J6RyjoYJbXfBAV2DIonJ_lVuH2FxhEMD-FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=Lmum7MK4gVHw0k9n5MVrFnJBLXoEIkGanWEe1u0QE1PRSdZG0xisAswLs-B1VpGLepD3Hbh9lV3pxYMglMtyOq6A8jtvA6Vg8urvd5caxltL8X2LjkIN8OVjQCAvjVYV8_7qtRdoIv3-OoyhLG0oGt59wLkG6nVUYAThjQxtJvK2wJ6-u0NJeKwelhCWAaZMmy8H0E0zdvxklhBFmQeWyL5_Zu0cl241AM3wVRTyAggQO_VtIVmCT_ei33OaQzeidiBcD3FyM9JcbdfUP-U9fewYfLA0k8wADUxSJRomo3JgJyO83B9J6RyjoYJbXfBAV2DIonJ_lVuH2FxhEMD-FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مشهد اردهالِ کاشان، از " نمادِ مشت گره کرده‌ی علی خامنه‌ای " رونمایی کردن ولی انقد بد ساخته بودنش که صدای طرفدارهای حکومت رو هم دراوردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71547" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71544">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qKYqgh1QM4KBwE4qlApLz3M4OKw2C2t_Qjju19fs-0q9RnP4tLn6H4ijm27QgVrj7hde1-n0rpctI8Y1rcrNJajY-RJBwrTks1ld-Mm86eX-mkToKkW6E421KcbFQWQDOCVgeOCNDjOZR7lwKkJGw-MVL1XzuEcwcmHhJe0yBx9kzSLdyg4gmzO6EEpMp9UAypnyuV_s1PMbXMsLL1S35bFxdseeEFf-oHHBraxQswyIMUesC9AYDHw0M42fR9SgvzqV1-cAkR4f03X3Wlyih-n5GNgNLruB_NERS4FyFOLSZeacYqvYnKUxjH4syFFM0TFTJTAvPO9USTAX7_yTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ehp-GWeYkLyLx81OyQMaKX1JxwcnZNZULO94GIIoPVb2OhWIvmQASvHmtIuND8d6BCw-h8MV7o3IeI5Yp4ZQz-ZHjgwpE80nt6947iZ0CUO7r1qDhHf4qLzw4Vw_-EoE9bU77VUd9twUkN79kKBqdx6mx4nZDnR9l0_3kiGVHHkM-4Az5x7Fh0QVZn2UUm2ZY0clWy_wQOVOzkCiYlWneuUSIIMvQnOZ1GnJKJy30_CzJkewmipH7FWJeNKddxW6aP8KlbiIDceC0lSvbE5KxvbTz0_P_tpV_8JnwhN-hP9f-yYonNHjg9oYm8N0S5PNHSfY0lXm5emuwTvd17wQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qu2XJKhCzdj-F9eu6LF-9FknqtYx5hw1ilL3hB5_6AQP2zqp1M6B-tS4fcWlOYnqGzSkZsHvKYUdMFTyZrYhvTWNzgFmTqYXRV5hpNJ_mhrvoGvBuZnn73xhu4lhyZWtYc6aEJugBMtEEzXpus-wCAPX4vLvgQBpkjA150AaGs4eoQuYuK7WcUe50YRfuoLbETj583AmO-8u-uRCwLb17SWkdilMPmVE6Oz1sf9S5K5PxBRdASSwj2XDID2uE1R3H5DAC4S6EWCx19aYrYgMbnF9J1fPjMOa6-wryN-bNFlxO8S9s_Tvb7_GI-e5W7oKKVMEeUUvhydXE0hw4sEXyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
کشتی‌ها و نفتکش‌های آسیب‌دیده ایرانی در خلیج فارس.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71544" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71543">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شلیک یک موشک/پهباد به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71543" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71542">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZEfp113vjQzPXZZHqOx1lILCTWlCKQDxfwPJjojrDlJ_JD3wcVWNcca0XOAhY9NQfGaIUj19Nuq6ZIYt02ed3JD5uUgQrXUckfnm8iaOwyntz74kaUlFtSrOLTrZgwIs4LHpBhTxZSU3iWU8yN5VDW3xcc8PpfQpYcF2q0LwDKyOdGckKkTTmjQEq4gzJfWgYvZf6WFN2olkvKJU6IlIoB4k714C_rZZVobFWA-G-WCVk4_guzDvIJzBLHvT8JwIPeXZo8C06hUb6Ci-g-NUv4v8w5kiBN-jraJaEA83A0kv5WJE7oYhbAPGKZWcPTTV4hm5-5MTXbaiQ73CoOKLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
شعار جدید عرزشی‌ها برای حسن روحانی
😂
نهپاد: نفوذی هدایت پذیر از راه دور
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71542" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71540">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=fyz3g7PnU1Ubfjf7zyiD7N3hF-pCDiH3e-eQHeLTHSKBk1XR1EH1eDRKVNax8Sy-noyphrk817Iw0U5PXRhzzDJFbaJ36aFsOsHusBFPoS5kF8Nz8MJYITQeyIg6qXcmSl2omOpa4VhwUkDe97jTpKjE1PLGV3BZ_p0uM1fE8tDjELkdluJDMtOXd6x7bo6X9Zz_UyIYfcaabCW32uxv0IGmCt2slcx351Wt0Fbd9gLitTkZUQ9KPnleLACh58tzP1zGyhs04UJwp2JZt_S6gJpmvvOadePcdIieKrBO13MFSixM4uXdeWSt55mlzLo94Vk1Lw6Sir8MvPUuTbqyog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=fyz3g7PnU1Ubfjf7zyiD7N3hF-pCDiH3e-eQHeLTHSKBk1XR1EH1eDRKVNax8Sy-noyphrk817Iw0U5PXRhzzDJFbaJ36aFsOsHusBFPoS5kF8Nz8MJYITQeyIg6qXcmSl2omOpa4VhwUkDe97jTpKjE1PLGV3BZ_p0uM1fE8tDjELkdluJDMtOXd6x7bo6X9Zz_UyIYfcaabCW32uxv0IGmCt2slcx351Wt0Fbd9gLitTkZUQ9KPnleLACh58tzP1zGyhs04UJwp2JZt_S6gJpmvvOadePcdIieKrBO13MFSixM4uXdeWSt55mlzLo94Vk1Lw6Sir8MvPUuTbqyog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
حملات هوایی جنگنده‌های عربستان سعودی به استان البیضاء یمن
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71540" target="_blank">📅 20:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71539">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8AXciicQmy4nZoztKvCACBaJIvVOuu447nhL73mI84bmKRZqLpQ_xoznqJCMXvv6eBXRXmc-Xx09uen74lrLMFx4eMpEujxgr07KxYg_wmK2uFriBqmu1r-EQT5eQoRiJkQtrgK8KqWpY1QkcZaklrEq0LunosYSThJ9yvhdfKWqtvGas0gi-zZlFLG1TR5iKFWtwO-ALG1q6gGTqA-VR3RY8Uoxk1Kcx4wSZAb_vrVlYLFJuXLtBWL1a0VjqMXGldcOa2YwwpQ3nu31dsVmEubfj724mN2SqVhkVj2i916aKNtkLtSBT0sUay3kVxhfG3vgjoQHYIzVqL32WoM6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71539" target="_blank">📅 19:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e325MIwOLmUZWfLdN2cankl77N8teoU9_KN0z6GdRK7eKAIzct8EcdFyN605CpR_loxYx-mSYvGuzZSy6Iwax9rgJJK1UfvzEvZu9CMwbWHMCq3yu3w68v8ohH0L5JP7tCSEHmv6SL1MJt5INzh0Vh-2abdrujy45c0QL48KD8jH6j0jHlVDa30jR8zxC6PyAdjcUDe3AXnqvu01ZclQTkqM2WEyOptI0ZNQvZB9C9U7iwKaZYkrzerVirg2E233UgkYZn7GlFzpLWf5W8w4qGk624qdbrN8JbcPU_2FJGmBi02ASA5FxbiOCbxP9gDpyitA6AwQpNTWXUYGtYb3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره موسوم به «دیوار فولادی» علیه ایران توسط آمریکا در ۶۰ روز گذشته، نیروهای سنتکام مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
حتی یک کشتی هم بدون مجوز نیروهای آمریکایی از این محاصره عبور نکرده است و نظامیان آمریکایی همچنان با تمرکز کامل بر این مأموریت متمرکز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71538" target="_blank">📅 19:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇧🇭
❌
🇮🇷
بحرین اعلام کرد تا زمانی که روابط دیپلماتیک با ایران از سر گرفته نشود، در هیچ‌گونه نشستی با این کشور شرکت نخواهد کرد و بدین ترتیب پیشنهاد عمان برای برگزاری نشست وزرای کشورهای حوزه خلیج فارس و ایران پیرامون مسئله هرمز را رد کرد.
🗣️
بحرین چهار شرط تعیین کرد:
توقف حملات
پرداخت غرامت
احترام به حاکمیت
حل‌وفصل اختلافات از مجاری قانونی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71537" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71533">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=jzhkLor_EeEtx5-xxdvB4koviqB_POdmWp7In9iDDZ5f2S3meGx0lSFeSFH9PePWXPGo8S9xYq1Yrtvg2q-OUYa370-9l1aSy9h1A7GJwd0-oeYSKn-IkC6A8dRXnO6i2ryyXe3KDAoxib5I_xSi_LJ5MGpk16QlAFopf5eM6iFvf10WogxR3gMS09fMLgq7rr0RA2U8TmXO7Yo5cu8bCEDJQS6__ls6kB9Ps2weKXITNyU3J3wxKmqdbJe3EtUhGes206tIrxqNk3g8xtargWm3o5aCOrbIjIcYfU3eIF4nmC58vjutdUjNb8mn6sOjb4RgCzfetkad-lYatDlj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=jzhkLor_EeEtx5-xxdvB4koviqB_POdmWp7In9iDDZ5f2S3meGx0lSFeSFH9PePWXPGo8S9xYq1Yrtvg2q-OUYa370-9l1aSy9h1A7GJwd0-oeYSKn-IkC6A8dRXnO6i2ryyXe3KDAoxib5I_xSi_LJ5MGpk16QlAFopf5eM6iFvf10WogxR3gMS09fMLgq7rr0RA2U8TmXO7Yo5cu8bCEDJQS6__ls6kB9Ps2weKXITNyU3J3wxKmqdbJe3EtUhGes206tIrxqNk3g8xtargWm3o5aCOrbIjIcYfU3eIF4nmC58vjutdUjNb8mn6sOjb4RgCzfetkad-lYatDlj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین  به اهدافی در چهار منطقه روسیه حمله کرد که حملات ساراتوف تایید شده‌ترین و چشمگیرترین آنها بود.
مرکز لجستیک عظیم اوزون در ساراتوف (با بیش از ۱۰۰۰۰۰ متر مربع مساحت، بیش از ۳۰ میلیون قلم کالا ذخیره شده، تا ۹۰۰ هزار سفارش در روز).
طبق گزارش‌ها، پالایشگاه نفت ساراتوف (روس‌نفت، که قبلاً بارها هدف قرار گرفته بود) نیز آتش گرفت.
در ولگوگراد، فرماندار تایید کرد که آوار به یک مرکز صنعتی و یک ساختمان آپارتمانی برخورد کرده است.
منابع اوکراینی می‌گویند که هدف صنعتی، پالایشگاه ولگوگراد لوک‌اویل بوده است.
برخی ادعا می‌کنند که از موشک‌های کروز در کنار پهپادها استفاده شده است.
انفجارهایی در انگلس (محل پایگاه بمب‌افکن‌های استراتژیک روسیه) گزارش شده است، اما هنوز هیچ اصابت تایید شده‌ای به فرودگاه وجود ندارد.
بنا به گزارش‌ها، منطقه بندری کاسپیسک/داغستان نیز هدف قرار گرفته است - پس از حمله تایید شده شب گذشته به بندر ماخاچکالا.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71533" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71532">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71532" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71531">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX1QPSYYFCRGP4bkUULTSb_Y4xTHYWq7NGymOUrp9ocRNE8vY2IQM7WZe0SVODa5rt0HU-6vGIzp4OMcG_UsxmtKBVXpWGgER59KCtUwCOtBcp3XMtadN-m_DNm3MZpZbeZXil-Kgoyl6QI-QgCf4usSwkRXZU-UpFinC31Tiv-p2IfnVco88xmdz0JRSLEXBV3yKdt-70GWjBr8rny5SuX10yQ8DfHrsXAhAXiGWImi7XBOGhbUIukAsaCkFg-0eUrITEy7SGPd0Wjeei-QFMxZFHFTNN1BpsP0TDrSShuwzRePrU9Vjk7KVI29CsELWeaTFvFjIb4hvTPd2lmCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71531" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71530">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554b629d89.mp4?token=KmrJ7cu483sVTvqLIFhbLGx0tTxozTL_rgXBg6WRiewgNqkuFlEkNKpkBMe2fyRcq3qTG25xWRnC_BXjbSw8zAbUIpGTufGMJj2jNWUm5HBByyqxeVK_Wwn4ryTqv9eDG5LJD6Xn6xncIQSfxGEeY1NLUVB4fwlNmcvreWjDOpdMrTRR5JTi9HRnCS3oU0QVGui4KWTxzxk7yS3DPR6mA8CSae7V5Tws9PsQiVHJ9FO897PVdaxHDdTbQtzcDPzljlEvNV0K7y1zYs_MSlc6kdtJqyubpo1RWgWwbIh4JZzN1GYYOmo9i65wNnQRpqx5mp0MOYmdDx_dqNw2LdbbC7V0Kzq20I5qeKJgEIpSsQs-LlGDXCaglsUJVDVuBAf84xaTTE8fjIJHctjEcXh2nhJ6iFUpOkRRQ-lpdYJ8sSC-jgiiomCjqNIerrbZMn5F1da71KfjoYZk8onLdnesS94JQUz4oqxmoNhfbxGwHF75evA9aKZnyoniCI_FfJPqfVF43XWZtbWvtkOMkSzEhIgDd8R3bnjQ0zm2UATcrDV9QKZvKyt3jcraD5IdIrafrfDsW0XuXH5MGkca5NOm68qrRtTt27dCq3cf2KtF8ShyXnkgDpHn4iVA-yXd-nyZ9NXu54kmsaXH1ASP_y0xPnFeOdxLWUh_HK5lg1Bln2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554b629d89.mp4?token=KmrJ7cu483sVTvqLIFhbLGx0tTxozTL_rgXBg6WRiewgNqkuFlEkNKpkBMe2fyRcq3qTG25xWRnC_BXjbSw8zAbUIpGTufGMJj2jNWUm5HBByyqxeVK_Wwn4ryTqv9eDG5LJD6Xn6xncIQSfxGEeY1NLUVB4fwlNmcvreWjDOpdMrTRR5JTi9HRnCS3oU0QVGui4KWTxzxk7yS3DPR6mA8CSae7V5Tws9PsQiVHJ9FO897PVdaxHDdTbQtzcDPzljlEvNV0K7y1zYs_MSlc6kdtJqyubpo1RWgWwbIh4JZzN1GYYOmo9i65wNnQRpqx5mp0MOYmdDx_dqNw2LdbbC7V0Kzq20I5qeKJgEIpSsQs-LlGDXCaglsUJVDVuBAf84xaTTE8fjIJHctjEcXh2nhJ6iFUpOkRRQ-lpdYJ8sSC-jgiiomCjqNIerrbZMn5F1da71KfjoYZk8onLdnesS94JQUz4oqxmoNhfbxGwHF75evA9aKZnyoniCI_FfJPqfVF43XWZtbWvtkOMkSzEhIgDd8R3bnjQ0zm2UATcrDV9QKZvKyt3jcraD5IdIrafrfDsW0XuXH5MGkca5NOm68qrRtTt27dCq3cf2KtF8ShyXnkgDpHn4iVA-yXd-nyZ9NXu54kmsaXH1ASP_y0xPnFeOdxLWUh_HK5lg1Bln2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پست جدید هیچکس (سروش لشگری ) توی اینستاگرام که وایرال شده؛
«هنو به یادتم»
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71530" target="_blank">📅 18:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=dk5fxc7M8476cT2cJg5S_dUotnormko7zPAYhkktLxHEfsRtSB6z7H7aRRmlTXO_7w78U8SX01u8oj-VAZy85AyJ2EbymfHgfJGUicVjdJDo2F7RIF7lnmzz72sInQSBhTyhaq07E9AbpiEZcctzaEuzOxG_0ewuke-kTvoDLpz3Budh0mVrimLOdynVUtLwep98lij4mrdc0qFdoVN6gjN4YAiv3TYDauvzRNhkBQ24oO381TcDYWn5AJH9Ze2rwatS8RLhv5PCDRrLIqsAfAD055TNyh5uNi0A32CqgPECPCbyEj4k0wJN8CPp7lpSirTMvjVM7ZNI_RFaK58lVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=dk5fxc7M8476cT2cJg5S_dUotnormko7zPAYhkktLxHEfsRtSB6z7H7aRRmlTXO_7w78U8SX01u8oj-VAZy85AyJ2EbymfHgfJGUicVjdJDo2F7RIF7lnmzz72sInQSBhTyhaq07E9AbpiEZcctzaEuzOxG_0ewuke-kTvoDLpz3Budh0mVrimLOdynVUtLwep98lij4mrdc0qFdoVN6gjN4YAiv3TYDauvzRNhkBQ24oO381TcDYWn5AJH9Ze2rwatS8RLhv5PCDRrLIqsAfAD055TNyh5uNi0A32CqgPECPCbyEj4k0wJN8CPp7lpSirTMvjVM7ZNI_RFaK58lVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعار «مرگ بر روحانی» در تجمع شبانه عرزشی‌ها
:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71528" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=A1zWitd_30XQ-ojHbwAn2QF7m-egyZss36t1iODLcXXnnKSA_gcAAhabFbghKi1c5_f2C3vXzJ5bP0JoqC5puiTGDHScztfbURMNyx-SaXSoLOGwT72gc4JVz8jgBMxht1u3pxATq4VnS09-bxSR-auD0vHekakV7v2XWGjfZKPx203MdkDCrDeEtFEOyJ8t3LV4_I2f3sAkoyjEInm9joHz0GXTqBl17LGBMFb060Ytn-1ByyyHx5yJtkHVoFf1seCm6FYRC6gqak-RrbP-bAkD2B0J6Cqn2tiz9dDILcSSmII2Zw2M7_DHrPWQkMTJKXJfT5Dtp1YrwZNqXDQl6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=A1zWitd_30XQ-ojHbwAn2QF7m-egyZss36t1iODLcXXnnKSA_gcAAhabFbghKi1c5_f2C3vXzJ5bP0JoqC5puiTGDHScztfbURMNyx-SaXSoLOGwT72gc4JVz8jgBMxht1u3pxATq4VnS09-bxSR-auD0vHekakV7v2XWGjfZKPx203MdkDCrDeEtFEOyJ8t3LV4_I2f3sAkoyjEInm9joHz0GXTqBl17LGBMFb060Ytn-1ByyyHx5yJtkHVoFf1seCm6FYRC6gqak-RrbP-bAkD2B0J6Cqn2tiz9dDILcSSmII2Zw2M7_DHrPWQkMTJKXJfT5Dtp1YrwZNqXDQl6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
یک شهروند ایرانی با انتشار ویدیویی اعلام کرد ترکیه مرزش رو به روی ایرانیا بسته و اجازه عبور و مرور رو نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71527" target="_blank">📅 17:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71526">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=Zqy1mJWVmsyBnsKaRmiYsyP-XSyq_bJkAbE5xfGqjV3uSujfsDOjnwB40vfiGut9p0fQ81FbrV56ydyh72jF1efe79VK2U_L4QKDSPfTm3hG_Hh0K6pIiIwpmtATssReroRB_uftqp0i8v-7FfuLpiE80LBeuU78KRMCjH1tD8elHneVIL8qNDLUZP6450K1SfT3bSYbnJ4a1MR-donBpy9_-fDsY7SIZ1G4vspPwnpXO-7rk0bTcn2_e1-JuWx3Pe7Bh0cMGMyg-UfWoa2b79hQZw_iDQnO_IQcNm55P9Ap-XsXB5M8abaHEZpYTFend2Q4Buwb6IbuG3TPIbxWLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=Zqy1mJWVmsyBnsKaRmiYsyP-XSyq_bJkAbE5xfGqjV3uSujfsDOjnwB40vfiGut9p0fQ81FbrV56ydyh72jF1efe79VK2U_L4QKDSPfTm3hG_Hh0K6pIiIwpmtATssReroRB_uftqp0i8v-7FfuLpiE80LBeuU78KRMCjH1tD8elHneVIL8qNDLUZP6450K1SfT3bSYbnJ4a1MR-donBpy9_-fDsY7SIZ1G4vspPwnpXO-7rk0bTcn2_e1-JuWx3Pe7Bh0cMGMyg-UfWoa2b79hQZw_iDQnO_IQcNm55P9Ap-XsXB5M8abaHEZpYTFend2Q4Buwb6IbuG3TPIbxWLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از عشق و ابراز علاقه زیبای یه پیرمرد و پیرزن ایرانی توی پارک خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71526" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=MGXXa3tmj3keymPQa0mW2d4q0OUEPdH4E3tVb_zrLu4Vwq1bfys8YPU3wHQ5Ko2jyc2-LsMWMAqhl1stgxXlSYBgs1u4qO0lz5n14h224BKqU5OOYZZUXqrc4vJicRPxmMbRxKNmYLq_yIpLvm6xGv-Xs9IBhiqfFUl-vvHF92hQSBytwFhmKaRMC82nLcs4XHHGdObACS7iB-xLbqj21wX1DiFlYrrTfjd9GH3sFCZn9s5Lpi1NPpcmjPhG7s25rjUZlz8kBJDwAMJ-ry9p4jNtHwCT3B45jwhefswkM9rqDUhR2Ts9pT_I2EGbHsOHJV2DVEVhUaQ36ClMxoiiMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=MGXXa3tmj3keymPQa0mW2d4q0OUEPdH4E3tVb_zrLu4Vwq1bfys8YPU3wHQ5Ko2jyc2-LsMWMAqhl1stgxXlSYBgs1u4qO0lz5n14h224BKqU5OOYZZUXqrc4vJicRPxmMbRxKNmYLq_yIpLvm6xGv-Xs9IBhiqfFUl-vvHF92hQSBytwFhmKaRMC82nLcs4XHHGdObACS7iB-xLbqj21wX1DiFlYrrTfjd9GH3sFCZn9s5Lpi1NPpcmjPhG7s25rjUZlz8kBJDwAMJ-ry9p4jNtHwCT3B45jwhefswkM9rqDUhR2Ts9pT_I2EGbHsOHJV2DVEVhUaQ36ClMxoiiMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
چرا پزشکیان ۱۷ شهریور که تولد مجتبی خامنه‌ای هست بنزین رو گرون کرد؟ چرا روز تولد خودش گرون نکرد؟
میخواین همه تقصیرات رو بندازین گردن امامِ ما یعنی مجتبی؟ کور خوندین!
ما دیگه فریب بازی‌هاتون رو نمی‌خوریم که میخواین علیه رهبرمون کودتا کنین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71525" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71523">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=bAoLtZrQy8d7iFdQsu4U6He5U9iW8cEy2Ji8cmBTIbCC-jbfHTl1KsifyiGeP1AQoGU3eFjJvNnn0OwNyUe139_mP2WGP2Nyck0J9lfDMDjzUy8ZEHLbogVymT3ln6YLFNiKYFwPJyFLHe61U7ntTbTPExq9E2YmHd4CGzFSPB_nbeegS9g8ZT5-UM8l1nSfjQChsBNOy-J6naoj5A_WGxGChk0KyAgOQFx9_URyveWh8vlakW3S-WJN-Nd2AC6fWRCzf4AJYPhmYfXwDLtYtwIuqKWeYn8h1jGjWl3kO81LN2LGRywZ4F6iL7m4r81XmJ_TV3P4c4A49yY14RTOGlId8dTfrmrI4s1gDCuE6yhYpIF4wQVY7n5fWEgbFpqIDVylqhHnnJudxU4p4yoxn4dZbK1jSIohskOHPvOLjXNeSGcSnbjCB5GFTYt_lofsGhIFNiUKxXkvgenLdSOlVUT1_Hf5pUbIBQLJzYs0-BsSstU-MT2moCvUP1AWI1NsgKOGpSOrRngLkQnLtRJ7HpOOmmex-37ZKr5Nay8Dtqrf8Z-ms1ghsi72tkZ0jBAqaeddAlwk-z4KyQIGxdteqGrJRlVVEdvxW4pf5h2syXJofgV1gMrCiWuGRbMjJzxYpQnhFCufX3DVkOAHJznOblygs2zM-iTVK0JhH3NQF0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=bAoLtZrQy8d7iFdQsu4U6He5U9iW8cEy2Ji8cmBTIbCC-jbfHTl1KsifyiGeP1AQoGU3eFjJvNnn0OwNyUe139_mP2WGP2Nyck0J9lfDMDjzUy8ZEHLbogVymT3ln6YLFNiKYFwPJyFLHe61U7ntTbTPExq9E2YmHd4CGzFSPB_nbeegS9g8ZT5-UM8l1nSfjQChsBNOy-J6naoj5A_WGxGChk0KyAgOQFx9_URyveWh8vlakW3S-WJN-Nd2AC6fWRCzf4AJYPhmYfXwDLtYtwIuqKWeYn8h1jGjWl3kO81LN2LGRywZ4F6iL7m4r81XmJ_TV3P4c4A49yY14RTOGlId8dTfrmrI4s1gDCuE6yhYpIF4wQVY7n5fWEgbFpqIDVylqhHnnJudxU4p4yoxn4dZbK1jSIohskOHPvOLjXNeSGcSnbjCB5GFTYt_lofsGhIFNiUKxXkvgenLdSOlVUT1_Hf5pUbIBQLJzYs0-BsSstU-MT2moCvUP1AWI1NsgKOGpSOrRngLkQnLtRJ7HpOOmmex-37ZKr5Nay8Dtqrf8Z-ms1ghsi72tkZ0jBAqaeddAlwk-z4KyQIGxdteqGrJRlVVEdvxW4pf5h2syXJofgV1gMrCiWuGRbMjJzxYpQnhFCufX3DVkOAHJznOblygs2zM-iTVK0JhH3NQF0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره ایران:
«ما کنترل تنگه هرمز را به دست گرفتیم. تمام مین‌ها را پاکسازی کردیم.
من گفتم: «خب، پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟»
گفتند: «قربان، این مین‌روب‌ها زیر آب هستند. آنها همیشه در زیر آب فعالیت می‌کنند.»
گفتم: «چرا این کار را می‌کنید؟»
گفتند: «خب، به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه هم خصومت و درگیری زیادی وجود دارد.»
یعنی اگر در یک آبراه مین وجود داشته باشد، معمولاً افرادی هم هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
حالا دیگر هیچ مینی آنجا نیست، هیچ چیز دیگری هم نیست. و اگر ببینیم آنها [دوباره مین‌گذاری می‌کنند/اقدام به این کار می‌کنند]، آن‌وقت می‌بینید چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71523" target="_blank">📅 15:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71522">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=pkjY1WwkHrMWSy9sxXhfs5Fre3ZyTy-ZppbDXkUK8SC9dWArjMDGOKZnm_R0zbSS-rgD1o-g8Uy47NtqKC2S03bx5v9dufoPNs3EA9JDthHkKSKYAXc6bLwEgLDC4Z6g0iD7az6sRM7-smMqUoS1qt4qexpDFY_3E5oWyvhjXRWWOgc93TIV0z1H0_lA8j7kj9zxktIKQ1fem68P0vZEYaG67Ac_jYl_FaCbHxPlBMRmIayYw1ew-v26MimObpRwExSR5fNcQGsgcGj5w5m2gUyyyGa64CCY_08Xf2dmKH8G7tyt5peQxUaDFpBYytipnGHbxCjKiJhGBaNNJv2xig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=pkjY1WwkHrMWSy9sxXhfs5Fre3ZyTy-ZppbDXkUK8SC9dWArjMDGOKZnm_R0zbSS-rgD1o-g8Uy47NtqKC2S03bx5v9dufoPNs3EA9JDthHkKSKYAXc6bLwEgLDC4Z6g0iD7az6sRM7-smMqUoS1qt4qexpDFY_3E5oWyvhjXRWWOgc93TIV0z1H0_lA8j7kj9zxktIKQ1fem68P0vZEYaG67Ac_jYl_FaCbHxPlBMRmIayYw1ew-v26MimObpRwExSR5fNcQGsgcGj5w5m2gUyyyGa64CCY_08Xf2dmKH8G7tyt5peQxUaDFpBYytipnGHbxCjKiJhGBaNNJv2xig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هادی چوپان :
هانی رامبد از پشت بهم خنجر زد.
گفت پشت جمهوری اسلامی نباید باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71522" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71521">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtrO4DBbvRJGWd3A9LVcmSTTCRCBcJrsfTbV2AbaSp2E3nYMrV0qaHYm8miJBo_0emhQwQnReUV--7p6xIK8c9e2-PUixHBbHBUdASYzVqzW6mZaG0MtA8R4PhOjhpEHKQYVec60-h5iVp2bsgtPwBXCiEB4hHBtUtZ0HdT2-2oxAmPPP7F1eI1CXQYqevyA7pEq6HWf-oixAvaeixFnkx9sLMxQLEFXfqJNAyGqRGPtJZdfrY0QxP9MZREg6j_uqj5H8i2Rn75GMRj6SKs38-TMklYIgATskd9dmAirTsx8M3S1Rty-qpt0kEzDWTyw1ihQjbAud_zzv-gI4hMKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
پزشکیان در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان رئیس امارات متحده عربی دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71521" target="_blank">📅 14:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71520">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=ZGofBbH5MWisJDLtN2BoIEha8t24kLHgvgCCtrBAGtKL6sW0oEUpBQZZ6Z3rGmAWT-S79XO-RZ8ktsV-0xeHnEtHCR9c2qWJ_6xDJbJlbIOS32E28fPSwOrLjmD6y2hNjNbOjo5vqvu1iLZ0bA2LrE484FIQ01S61CLT6J7wfW_Z2uZCxNTFRX9zLpPtapH_rclBT3XFo26rLs6b2bhj2qEgf78X2cyRiSTJEjE-ERO9FWoegsuDu71J4e1SJgUXNHIrShjMGlEGOMYtp_9L4M0IXVY5TGI3GAA4Y-Lnl-BCl7DI9D2b66oZRoUa3NmirXfx4BRSdHgfLT9OEV7eE3tI10a0KxJUGQhWrwFpLSBhAjAhsglpG8FqXTKrHqTKS7JcB6I4E8H1D5Scyg3uUOWpd9EPJ39zyjyRTsSu0iPHmyppcA9XL7C1g5nCtfE3vCnznspV2R71ht8VSH2ou__i0ubdu7r2ykHgFimNUPnQ83gvUtiFXePhiba8dyFqrsRF5bswOaEALpuPjzpjWF4prXmSH04QsaW-klEO3UoDmIOOyIC2YEyT0v5EU-xTuS9ed6H9kTNmfBVWcDhFAJWtB8irqa0YTvTzWVsUaGlwBWuupMiLfLWdGWLcw-IJnjn8I9FhmnvVDUwcw4bP9_bQuwa-FRL5YZqyqx1xdIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=ZGofBbH5MWisJDLtN2BoIEha8t24kLHgvgCCtrBAGtKL6sW0oEUpBQZZ6Z3rGmAWT-S79XO-RZ8ktsV-0xeHnEtHCR9c2qWJ_6xDJbJlbIOS32E28fPSwOrLjmD6y2hNjNbOjo5vqvu1iLZ0bA2LrE484FIQ01S61CLT6J7wfW_Z2uZCxNTFRX9zLpPtapH_rclBT3XFo26rLs6b2bhj2qEgf78X2cyRiSTJEjE-ERO9FWoegsuDu71J4e1SJgUXNHIrShjMGlEGOMYtp_9L4M0IXVY5TGI3GAA4Y-Lnl-BCl7DI9D2b66oZRoUa3NmirXfx4BRSdHgfLT9OEV7eE3tI10a0KxJUGQhWrwFpLSBhAjAhsglpG8FqXTKrHqTKS7JcB6I4E8H1D5Scyg3uUOWpd9EPJ39zyjyRTsSu0iPHmyppcA9XL7C1g5nCtfE3vCnznspV2R71ht8VSH2ou__i0ubdu7r2ykHgFimNUPnQ83gvUtiFXePhiba8dyFqrsRF5bswOaEALpuPjzpjWF4prXmSH04QsaW-klEO3UoDmIOOyIC2YEyT0v5EU-xTuS9ed6H9kTNmfBVWcDhFAJWtB8irqa0YTvTzWVsUaGlwBWuupMiLfLWdGWLcw-IJnjn8I9FhmnvVDUwcw4bP9_bQuwa-FRL5YZqyqx1xdIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
ببینید، ما کار فوق‌العاده‌ای انجام دادیم. می‌دانید، ما آنجا را تحت کنترل گرفتیم. ما واقعاً با اقتدار کامل بر «تنگه هرمز» مسلط شدیم و هیچ‌کس متوجه این ماجرا نشد.
ما کنترل بسیار قدرتمندی بر آن داشتیم.
ما یک محاصره دریایی اعمال کردیم که واقعاً بی‌نظیر بود.
ما تعداد زیادی از شناورها را بیرون می‌کشیم؛ به‌طور میانگین روزی ۲۵ شناور را خارج می‌کنیم که بیشترشان در شب انجام می‌شود.
اما به‌طور متوسط، هر روز حدود ۲۵ شناور را از کار می‌اندازیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71520" target="_blank">📅 13:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71519">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، جنگ در ایران چه زمانی پایان می‌یابد؟
🇺🇸
ترامپ:
فکر می‌کنم خیلی زود. گمان می‌کنم احتمالاً درست پس از پایان دوره [فعلی انتخابات] باشد. آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا وضعیت انتخابات را پیچیده سازند. اما فکر می‌کنم مردم متوجه ماجرا هستند، چرا که ایران نمی‌تواند سلاح هسته‌ای داشته باشد. موضوع بسیار ساده‌ای است؛ مسئله خیلی ساده‌ای است. ایران نباید چنین سلاحی داشته باشد. آن‌ها تنها دو هفته با دستیابی به سلاح هسته‌ای فاصله داشتند.
اگر این کار را نکرده بودند [و جلوی آن‌ها گرفته نمی‌شد]، اسرائیل را نابود می‌کردند، خاورمیانه را به آتش می‌کشیدند و به برخی شهرهای اروپا — و حتی فراتر از شهرها — حمله می‌کردند. و احتمالاً پیش از آنکه ما بتوانیم آتش را خاموش کنیم، به خود ما هم حمله می‌کردند. اما آن‌ها نباید سلاح هسته‌ای داشته باشند. با این حال، می‌گویم که [این اتفاق] به‌زودی رخ خواهد داد و قیمت نفت به‌شدت سقوط خواهد کرد. وقتی آن اتفاق بیفتد، قیمت نفت به‌شدت پایین خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71519" target="_blank">📅 13:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71518">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⏺
🇮🇷
قرارگاه قدس نیروی زمینی سپاه:
درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به هلاکت رسیدند؛ همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از مخفیگاه این تیم کشف گردید.
در این عملیات که تا پیش از ظهر امروز ادامه داشت ۳ نفر از پاسداران گمنام امام زمان(عج) نیز به شهادت رسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71518" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71517">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=sDASXV5Dg2GIvpesiy16lKVJwjkojA9LFIZO_JM1ZY6x8Wq5khY4CZ-6k_gs2jAKaLXKwjRVpo2RF4226yGmbDZrRzV867ZLCH75_GOMTQH3_X-YVYaz_Cw91uDNNaLQ0R4ig291hG5gDpEQYmtaVRVr1lKtf8s9nJRe2eXAbDhP187n7JFAS2wjtyk4mInToY6AbgigpNPESGGBBsHeOkixzmw5IUg8oB_I10xzqciJ6KsWnxRAcjMeiXnhrUVnVEmxQGtr3BJ_antEm7rTc2f5ro4KnAwc30yL-Eg1RuW56gbH-XZCkxsCvKeuAipUC7_S4XT42jfVaXchUSLFBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=sDASXV5Dg2GIvpesiy16lKVJwjkojA9LFIZO_JM1ZY6x8Wq5khY4CZ-6k_gs2jAKaLXKwjRVpo2RF4226yGmbDZrRzV867ZLCH75_GOMTQH3_X-YVYaz_Cw91uDNNaLQ0R4ig291hG5gDpEQYmtaVRVr1lKtf8s9nJRe2eXAbDhP187n7JFAS2wjtyk4mInToY6AbgigpNPESGGBBsHeOkixzmw5IUg8oB_I10xzqciJ6KsWnxRAcjMeiXnhrUVnVEmxQGtr3BJ_antEm7rTc2f5ro4KnAwc30yL-Eg1RuW56gbH-XZCkxsCvKeuAipUC7_S4XT42jfVaXchUSLFBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران مسئول حمله به خط لوله «شرق-غرب» است؟
و به نظر شما عربستان سعودی چه کاری می‌تواند انجام دهد؟
🇺🇸
ترامپ:
خب، فکر می‌کنم همین‌طور است. احتمالاً همین‌طور است.
آن‌ها در حال حاضر در وضعیت آماده‌باش و هوشیاری کامل هستند، اما فکر می‌کنم مسئول آن هستند.
آن‌ها مدتی است که کنترل آن را در دست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71517" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71516">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=gkZHwSqHcn7fo4r7x1WojL2k3nV3x_yDwYcKK4fsAB174nyfyEisuR_lFTs7u2P_TwJc91IoLrDz9LzpFFNc7bs4B2sPBybpKsVneTqClls7eWnpZOAtwm1OBOtDA6kCIrig9q1TdAS0ima6-jVAxuDvmSmn8LyAUyGlSxk-JcmitRhj_Neygh6JTxtg1FCxQvhqky_JF7xH-52qWlThmg_3RlMYFrqeEjLsEZTAj7GT1pqks5JGAhBiapPMZcKcqNBYz0vWrpc6FE3YqyjQop-bg7kzWgzYR3uzP8MwsXZGhTn7-vscI0Hy81sWnOXMno6snffLkunDT1dBdjs0dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=gkZHwSqHcn7fo4r7x1WojL2k3nV3x_yDwYcKK4fsAB174nyfyEisuR_lFTs7u2P_TwJc91IoLrDz9LzpFFNc7bs4B2sPBybpKsVneTqClls7eWnpZOAtwm1OBOtDA6kCIrig9q1TdAS0ima6-jVAxuDvmSmn8LyAUyGlSxk-JcmitRhj_Neygh6JTxtg1FCxQvhqky_JF7xH-52qWlThmg_3RlMYFrqeEjLsEZTAj7GT1pqks5JGAhBiapPMZcKcqNBYz0vWrpc6FE3YqyjQop-bg7kzWgzYR3uzP8MwsXZGhTn7-vscI0Hy81sWnOXMno6snffLkunDT1dBdjs0dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
این رستوران توی تهرانه
نوشته : هیچی کتلت بی بی نمیشه:)))
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71516" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71515">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=X3wWdVLdS43sH4wUI8RTTZmymBTJb4RHiWlOZDW6ZRCEzMuTOQ5EiBinPrFB8wZABJ0gonSbZ7gAuqOuLJr006scrOLGGh75tgjjoTblPvvlf7Hsy9XkQcZGMoNt51pKbP1F8VU3k1SbfRZu-DKFYPpt4rZNO_p8mGxj-_v18igSjSwy9ATrpFDvI23EyELbJksoo6RzV8vmOi_ugDY4Iskj-dy6tz3c_u6y2gu8k2T04-RqtfDxyFSL22sW-R4lJFHTcmaFS_4Oo6cLdd8r2pJtr0XB8j-lxA-LTMDcM4B6rBPAB6IHyqz4a_ZqTl9aVYWAdtnnz2uVr9k6LnR8Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=X3wWdVLdS43sH4wUI8RTTZmymBTJb4RHiWlOZDW6ZRCEzMuTOQ5EiBinPrFB8wZABJ0gonSbZ7gAuqOuLJr006scrOLGGh75tgjjoTblPvvlf7Hsy9XkQcZGMoNt51pKbP1F8VU3k1SbfRZu-DKFYPpt4rZNO_p8mGxj-_v18igSjSwy9ATrpFDvI23EyELbJksoo6RzV8vmOi_ugDY4Iskj-dy6tz3c_u6y2gu8k2T04-RqtfDxyFSL22sW-R4lJFHTcmaFS_4Oo6cLdd8r2pJtr0XB8j-lxA-LTMDcM4B6rBPAB6IHyqz4a_ZqTl9aVYWAdtnnz2uVr9k6LnR8Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
🇺🇸
پست جدید دونالد ترامپ در تروث سوشال:
با این رئیس جمهور بازی نکنید، زیرا نتیجه خوبی نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71515" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71514">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDMoaPsrGSx3s7CMJGknWcMOADgdYCbBk133bxHP36W7QqGfT3rTCC2VAZtkYjLpvUBSwY69kI51tkoGtB9cZnQKvFMZALxnF_TkoZ9llGgVTsES1ignDiDgwVajdUQkt4Kzgj87SQDPl5tVw0WyJ7M9lSA-6vejFHMDwaOvdGjjh2acrI76JbvlyThh_954jaXAYOXYpu1FmqWfeMXCLp2PP711BzOoD1L-nyMGdXhcB0nCkjT0pL48MWWWOUy5T2Sp1-4apN6093T2m-VXdQAQRXqYqjUM3557NfBiCcINZcc9XWe9d_Zwm8en6-6I65nSPkaL6iybl8RA2daobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها تو راهه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71514" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71513">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71513" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71512">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODqvGvZ_cU6fziGnvPmKwCjprJBkw6QBGEQ_EJUmha6lF-_8totMTGmudBc7CXdC25yHkmw7ZEXDCoo6sGzZUPJIwFywOggAA7WoqAP8Mai9g3EB6KGtISQqw78E38QfHv8KbIn9Rfx66yADXEjKDAuFUNky8bThu2k2gUv0J2U5XEdmIHXgGKn7sEXjCmCW5fRmvKU585X2mAokwBIyUkq7AYd3LsFCQU8gUnYCjG1DD9H7PVUhIsLpuQVvF7ldsQITDyheAm84H84hNdIH34vo1gRzSgTcuTCF6MdXPu93jQ9ZYZ23Ry2z_EbThAq0moEsZyhPmQ-PmJsATAwcHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71512" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71511">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇮🇷
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان: محل تجمع اعضای «گروهک‌های معاند و تروریستی» شناسایی شده و نیروهای امنیتی در یک عملیات غافلگیرانه به آن ضربه زده‌اند.
در گزارش‌های اولیه، نام جیش‌العدل/جیش‌الظلم به‌عنوان عامل درگیری امروز به کار برده شده که هنوز به صورت رسمی تایید نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71511" target="_blank">📅 12:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=DndRZe6BgjVC62yeiXDZflZ5e83XD71mxkKBOnzLBKBGVpVuQmf_en23octDFsL8z8Q-BPemSMVh3WBLUMxEaWjIcrJYwZySUV-So6XKF_J5fjrkIkx7c3J01pbTGaurJVSBKUYgUedS9aBY2zBwhiwMtn-s2yS_9cqag_IbSdrhizv_jApGbLaxlgTL90V2mR8WDKmApqm7hrVBt3cOA779qg71fCmf-RIJn4BdWhBrBOtXvpAoAaAeEVH_G3onoKBoC5v_89liwrPoqk4oO_SWOTVNoPCczVU3BzN-3BntpV5Ha51JuVOQocEptU212WzfxpTGRKMqNDRF7fddBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=DndRZe6BgjVC62yeiXDZflZ5e83XD71mxkKBOnzLBKBGVpVuQmf_en23octDFsL8z8Q-BPemSMVh3WBLUMxEaWjIcrJYwZySUV-So6XKF_J5fjrkIkx7c3J01pbTGaurJVSBKUYgUedS9aBY2zBwhiwMtn-s2yS_9cqag_IbSdrhizv_jApGbLaxlgTL90V2mR8WDKmApqm7hrVBt3cOA779qg71fCmf-RIJn4BdWhBrBOtXvpAoAaAeEVH_G3onoKBoC5v_89liwrPoqk4oO_SWOTVNoPCczVU3BzN-3BntpV5Ha51JuVOQocEptU212WzfxpTGRKMqNDRF7fddBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درگیری های بی سابقه نیروهای جمهوری اسلامی و نیروهای مسلح در سراوان سیستان بلوچستان
ویدیو ها مربوط به چند ساعت پیش
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71504" target="_blank">📅 11:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:  دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود. این تصمیم شامل تردد مسافران و همچنین جابه‌جایی…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71503" target="_blank">📅 11:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71498">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=BJHfguo64l4DIPDivy6PavdAiQ6yzDJNP-ad-8SvwdKLIb-Tx1hWyqy81ZKuAoCT4P8CXIIWVk1KJ9hySSfFuDpPpld0e81WfWCuEfmCQ2YQxvm9CNUtfccCre8QVxazTWjcwA0glxMLd5hbCTqFZR1t4gRqpVl8ZXkVDEyqnwsgtKKwbUdZm8hKT0LtoH60xwuiy6etBPrX8fUCSCqXr_RyPYC7XyqaA6pCZ08_kZ3ZE0F0pEFDwakrWEZwRk1CvnVHP_E8lKrkiVTlKUkgtOAyNF5Jlq2fySThmcT38wTtj-3MiKZunIft0JJwtXotFkBzHaltVi2J16w-BayOlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=BJHfguo64l4DIPDivy6PavdAiQ6yzDJNP-ad-8SvwdKLIb-Tx1hWyqy81ZKuAoCT4P8CXIIWVk1KJ9hySSfFuDpPpld0e81WfWCuEfmCQ2YQxvm9CNUtfccCre8QVxazTWjcwA0glxMLd5hbCTqFZR1t4gRqpVl8ZXkVDEyqnwsgtKKwbUdZm8hKT0LtoH60xwuiy6etBPrX8fUCSCqXr_RyPYC7XyqaA6pCZ08_kZ3ZE0F0pEFDwakrWEZwRk1CvnVHP_E8lKrkiVTlKUkgtOAyNF5Jlq2fySThmcT38wTtj-3MiKZunIft0JJwtXotFkBzHaltVi2J16w-BayOlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر تهرانی بعد از اینکه با دوس دخترش کات کرد، رفته تمام اکسای دختره رو جمع کرده، واسش دسته جمعی آهنگ خوندن تا قشنگ دختره رو بسوزونه و عقده هاش رو خالی کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71498" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71497">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=hTdwwW1SrwZ4ptEHrkQYAPFGeq8-G7YgBEp7CpgzXitSDCFy9FiYLs21jmzm0Mi95vzLxtdctNhA9Hk5M81v8kUAhDIgiotdhHkc8TlEppWSXeoRbCiecLn48JhLfhTey19kTSxtc7exH11ddaqUqp5cKIs0BoviNiyvsat3GhJedqSBHMI2CnebJnio0LECBh0vXpwUoYExhSwAFuWo4xq-P-Axn548EP4nCKGz3luTzgsm9BuA47cT88u5yjVDglkohzeDUhNbDf_rwzZEV54w-GSsX981h-G9WHRD65wV8sDmix-NC8SaGVfgENtCrhxcNmwPddQ6vA92uxTQ3Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=hTdwwW1SrwZ4ptEHrkQYAPFGeq8-G7YgBEp7CpgzXitSDCFy9FiYLs21jmzm0Mi95vzLxtdctNhA9Hk5M81v8kUAhDIgiotdhHkc8TlEppWSXeoRbCiecLn48JhLfhTey19kTSxtc7exH11ddaqUqp5cKIs0BoviNiyvsat3GhJedqSBHMI2CnebJnio0LECBh0vXpwUoYExhSwAFuWo4xq-P-Axn548EP4nCKGz3luTzgsm9BuA47cT88u5yjVDglkohzeDUhNbDf_rwzZEV54w-GSsX981h-G9WHRD65wV8sDmix-NC8SaGVfgENtCrhxcNmwPddQ6vA92uxTQ3Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
یه گزارشگر تو شهر وان ترکیه طی یه گزارشِ خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده که حسابی وایرال شده؛
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71497" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71495">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=NfX2K2AG8caFL_OlZ5F5IeeRFVcH38wKdTJqYcGAT1X5PFF3ZuFg9zFRzVi-Vshq63BKXaV0SkJq_dPnrLR7IqFsDI3gjm0BObLj3oyztH9eq3ABlh5fbC_AhEnXrqlDP3oe37A57ySYFixg7iHqiRS0bcGrBQbWd9xImq0R2WaIdRNY1FBjvsnpALl0ZOQaCPKmJY_eoEdgEBtkhHfc9iZu911IcE6YYH9j6P9ELFZhT2p3dMBUzO2sd_Y6xL4vw2tofx25b408W6VBsj12FxqLZj71KOLyu0SN2DeUTBMbPrNgMcdC7PNdZDCsXM3jS2-CJpUksXV8jChscirESw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=NfX2K2AG8caFL_OlZ5F5IeeRFVcH38wKdTJqYcGAT1X5PFF3ZuFg9zFRzVi-Vshq63BKXaV0SkJq_dPnrLR7IqFsDI3gjm0BObLj3oyztH9eq3ABlh5fbC_AhEnXrqlDP3oe37A57ySYFixg7iHqiRS0bcGrBQbWd9xImq0R2WaIdRNY1FBjvsnpALl0ZOQaCPKmJY_eoEdgEBtkhHfc9iZu911IcE6YYH9j6P9ELFZhT2p3dMBUzO2sd_Y6xL4vw2tofx25b408W6VBsj12FxqLZj71KOLyu0SN2DeUTBMbPrNgMcdC7PNdZDCsXM3jS2-CJpUksXV8jChscirESw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده و پشم ریزون از کنسرت تیلور سوییفت؛
خودتون ببینید به چه دلیل وایرال شده
😏
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71495" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71494">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
خورلسوخ، رئیس‌جمهور ۵۸ ساله مغولستان، هنگام بازدید از یک یگان نظامی، حرکت پرس سینه را با وزنه ۱۰۰ کیلوگرمی در ۲۰ تکرار انجام داد.
او که پیش‌تر افسر ارتش بوده، نامش در لغت به معنای «تبر برنزی» است، باشگاه هارلی-دیویدسون مغولستان را تأسیس کرده و در یک گروه موسیقی گیتار می‌نوازد؛ او همچنین جانشین «باتولگا» شده است که خود قهرمان جهان در رشته سامبو بود.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71494" target="_blank">📅 09:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=KaHHgXysYphGhJw25CVvLw_DOkoaQWMC-VchLOJQuuzcqtFkb2yyFDav_fQOVs-ezYX3Y_3l_COmuhPfPEnO3xymqrQN6dA2qk5sFZv-L63iqTUgWvOFBWKmLrcCESsPZJVKiyDrFXe5vRbgHRgGPgYt_vY07L0ycZ0Pb1hTjDwb3s0NtEKn1nsg8vxG9t0_YwRmUElEMNKMMqZg8hW9lNNDJY7RKwJRxGQc4mesVMQez14jZN03240wfjgApiVEqw1rQVRdTqxtwdq-4iED1ORh9rj127eGSJoZtCYhxEnkANkIUx8Xf6VI01epivItrEVNNX95RbM7IlHKPxq51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=KaHHgXysYphGhJw25CVvLw_DOkoaQWMC-VchLOJQuuzcqtFkb2yyFDav_fQOVs-ezYX3Y_3l_COmuhPfPEnO3xymqrQN6dA2qk5sFZv-L63iqTUgWvOFBWKmLrcCESsPZJVKiyDrFXe5vRbgHRgGPgYt_vY07L0ycZ0Pb1hTjDwb3s0NtEKn1nsg8vxG9t0_YwRmUElEMNKMMqZg8hW9lNNDJY7RKwJRxGQc4mesVMQez14jZN03240wfjgApiVEqw1rQVRdTqxtwdq-4iED1ORh9rj127eGSJoZtCYhxEnkANkIUx8Xf6VI01epivItrEVNNX95RbM7IlHKPxq51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی خطاب به ارزشی ها : انتقام خامنه‌ای رو امام زمان که ظهور کنه میگیره
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71493" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71492">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:
دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود.
این تصمیم شامل تردد مسافران و همچنین جابه‌جایی کالاها می‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71492" target="_blank">📅 07:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71491">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71491" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71490">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvYEPy8qTqerPfgWjFkl-TOcXxw0n4VUqjPxu-I7LDfUVE_UX0CGO6i0U5czRJ7Huu98vkTMecXqDVp9q1lpjtZt1gBTlH1XpnDILuETQDGhX5CopCtvLTWwgq_2BCRZNlA1xXGeeWJht-WMxUEfVA39U86irgyvhJtxko3ny28z6Zdd1qsUyQFHFBqtYogXoIlc4Klir2vmeI-1fwSLQWIoyj7x-F8Y7qht1T69St95a0s030qP3ONt2ELyPVk0PP5UfOuNFnEUSnv-WZ0gh1-ko9mIBAR1R-QY6uYHgc5jPUDjgW-nWPW6JrfVFM8VUs7WteaCiFiNruy3OhqciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71490" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71489">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=p8Kuq7Z4kkyecXbdNFJm8ttjPkeFwX_WiuLRx8alxtOYb_38X1RepY7oazQIaa1KdYfq53Os-9PywsKw6OjArCiwKdWIDAHNzfDNPetGUL9dT7YCb2xxOLBfIxxI-lwbYFFrTSRKOFzszscM4-fG0PFfA_QBO-LKhni1hq5MWAi_a0zvIPMNQDAVAzd4gIPtJKz02d69ijtF4fl1tCicgTCeIcCuVqwFxZC4poOQ2rNTPbCEdwCNNmQZXUMIcgSpcaBtPA4BnWERfhJr9IDi0bjcYBX4b0k1iKFJfd8syrRxb1WeWe-lg77EHZaXzjREFfsVMZ92HrDWdA-YOu5Qmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=p8Kuq7Z4kkyecXbdNFJm8ttjPkeFwX_WiuLRx8alxtOYb_38X1RepY7oazQIaa1KdYfq53Os-9PywsKw6OjArCiwKdWIDAHNzfDNPetGUL9dT7YCb2xxOLBfIxxI-lwbYFFrTSRKOFzszscM4-fG0PFfA_QBO-LKhni1hq5MWAi_a0zvIPMNQDAVAzd4gIPtJKz02d69ijtF4fl1tCicgTCeIcCuVqwFxZC4poOQ2rNTPbCEdwCNNmQZXUMIcgSpcaBtPA4BnWERfhJr9IDi0bjcYBX4b0k1iKFJfd8syrRxb1WeWe-lg77EHZaXzjREFfsVMZ92HrDWdA-YOu5Qmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
تصاویری از حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به بندر «مخا» در جنوب غربی یمن که تحت کنترل انصارالله قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71489" target="_blank">📅 00:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71488">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR9t4POTXFNJ8jnuJPQBdL80UAIh2auNScCFfXU9ApZmd3l59g_mv4cBkfasnnp3BeaSZ_TS5kECTZ806XsN--XLnDprMQfOiaM-CkZH5bkTS4TobNuj3jKCxQ1Oz1v0u63SxbKafQ-XsdG1xaUKVVrWD1I4G32eXyx3YxzEFLHiYkYZO0otBA2nhprbjSKxIz4ddbORSmsOZP9hAkca4jxjd8EM7SxeU7F4b8BFoEpwMvnsVFjnbCMz3jVdo2yoh5wyCgJxJ13ba4g7eGN9ZX6cCuMZtsFmmP2mg6rxdebRDSBVf3T_uZ84-SIfjQ6U2VUrOVGDX2GJmLzXCeGfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با پول ۲۰۷ در ایران تو کشورهای مختلف چه ماشینی میشه خرید؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71488" target="_blank">📅 23:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71487">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=jZJeXlm2D4wJFIxITc7Yk8igjjcfMVx9GCAsn2BTWadfXOPwCJBW_7CEUBpkwpRaLxRJr_nqGVTV78ov9zKpovWrwX7kPmA0aIfnAqQaE_1xu7umVABGYmcNMjSuFJ_MltI_MfC_JGO2edfI_hYQs4zq1BK0v2AVcsgETULqFNhl8mZXNPo5pNImfrrMazybh0n4Bbt3oj5R3ho9WDf8bYjOTyFC8lWANAUL5hZSqkDEXSlMlKjH0NBlAxg_TPeGEzxb45AwS78Cy1vRNJsBrCm_1Nqln1HmEBA4xChqg7w5z4S7ASNANVxh8cFmtH0H7Nv4-DmhPpOlIcv089dmTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=jZJeXlm2D4wJFIxITc7Yk8igjjcfMVx9GCAsn2BTWadfXOPwCJBW_7CEUBpkwpRaLxRJr_nqGVTV78ov9zKpovWrwX7kPmA0aIfnAqQaE_1xu7umVABGYmcNMjSuFJ_MltI_MfC_JGO2edfI_hYQs4zq1BK0v2AVcsgETULqFNhl8mZXNPo5pNImfrrMazybh0n4Bbt3oj5R3ho9WDf8bYjOTyFC8lWANAUL5hZSqkDEXSlMlKjH0NBlAxg_TPeGEzxb45AwS78Cy1vRNJsBrCm_1Nqln1HmEBA4xChqg7w5z4S7ASNANVxh8cFmtH0H7Nv4-DmhPpOlIcv089dmTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇱🇧
🇱🇧
رسانه های نزدیک به حزب‌الله لبنان وویس هایی رو از اعضای حزب‌الله منتشر کردن که در زیر ارتفاعات علی‌الطاهر در تونل ها گیر افتاده بودن و درخواست کمک میکردن.
همه این افراد بعد از حملات ارتش اسرائیل و نابودی تاسیسات زیرزمینی کوه علی‌الطاهر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71487" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=Qa4cvSnIhiXVMZY_9XCm44YHEnIAVAVHVxq11ZrZLyuxZRwRqciyIvVVY4avOOqGS2b3dLgG52z1ikYGq-ArTf6EuTeaozsyH4TU4YobSbWyqQQrMR99Fy1ztbPXEZwuLEPzqqT4bFyOSGnf_YWQJY9QCtWDMH6kVRIFog1agUJ4_fDMNf-PziergnESY6mPwm66XVVrdXHYKX77LI4rNXzB1XIAoY4KkSa02bnOOYgwTQn8h9n-dC4dLe8NyY1r_0Naow137Yl9jYQsVoxsUKg-4-xGvIyi2aHqOBG6-y6sVM3Fe3-nPAAsJZ-0kBEk4f7STs8iqGo9slGdPnEj-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=Qa4cvSnIhiXVMZY_9XCm44YHEnIAVAVHVxq11ZrZLyuxZRwRqciyIvVVY4avOOqGS2b3dLgG52z1ikYGq-ArTf6EuTeaozsyH4TU4YobSbWyqQQrMR99Fy1ztbPXEZwuLEPzqqT4bFyOSGnf_YWQJY9QCtWDMH6kVRIFog1agUJ4_fDMNf-PziergnESY6mPwm66XVVrdXHYKX77LI4rNXzB1XIAoY4KkSa02bnOOYgwTQn8h9n-dC4dLe8NyY1r_0Naow137Yl9jYQsVoxsUKg-4-xGvIyi2aHqOBG6-y6sVM3Fe3-nPAAsJZ-0kBEk4f7STs8iqGo9slGdPnEj-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=U3n0-0Jzd4vyR2Hh68B74BqscprCdwOql3HX6YnwMkMtUqhhHEZ758nrntNkh1LvlhbIG3ynDUYDipnnSS1vso9VmtzrPT1uZocLFFVJzlmlLG886KIo0MmnbOiICKSeeXPT0eWVX-r5giLYJUnV9eDHbxzYA6L7rJlK7Y1TS5ZsJ0__iBcPmFBulwvrxboj9cLckV64LMjGvaIlbmHxFFahBRwUuJrWZ1uHb2BKB7QWr0WQLtQ45GkmNA6L2Oz6GBQcAy9_z_3PECRA3-IfwL_IXg8A--KtqCi0qjho0f4VTALLOpT7PhgsZ9LbzYOlYZiGxOPzrut8jviimJUwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=U3n0-0Jzd4vyR2Hh68B74BqscprCdwOql3HX6YnwMkMtUqhhHEZ758nrntNkh1LvlhbIG3ynDUYDipnnSS1vso9VmtzrPT1uZocLFFVJzlmlLG886KIo0MmnbOiICKSeeXPT0eWVX-r5giLYJUnV9eDHbxzYA6L7rJlK7Y1TS5ZsJ0__iBcPmFBulwvrxboj9cLckV64LMjGvaIlbmHxFFahBRwUuJrWZ1uHb2BKB7QWr0WQLtQ45GkmNA6L2Oz6GBQcAy9_z_3PECRA3-IfwL_IXg8A--KtqCi0qjho0f4VTALLOpT7PhgsZ9LbzYOlYZiGxOPzrut8jviimJUwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای زن دعوت شده به صداوسیما درباره ترامپ و نتانیاهو:
ما میخایم با پول حلقه های ازدواجمون طناب داری بر گردن نتانیاهو و ترامپ بندازیم
درست ۷ کیلو و ۲۰۰ گرم طلا به قاتل ترامپ جایزه میدیم
ما میخایم خون بر شمشیر پیروز بشه
از مامان های محترم تعهد گرفتیم و به مقدار توانشون طلا کمک کردن که به قاتل ترامپ بدیم
از ارزشمند ترین دارایی هامون می‌گذریم تا ترامپ کشته بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71485" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇮🇷
۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران یک موشک کروز ضدکشتی را از سیریک به سمت تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71484" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71483">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=sM7vk3mCfi31VXRSFQUIwEPJGnGQMXchgcb-EBrtGtS9jA4vaIH7q3pA3mFFtu1XyZ8PgVEGP0-qCYb351q-6kmxTebSuyi5LeOCn4hX9Echje16Lzlay3lOJ-SOMsmvaH8J6Kgt5kqtNXzYC30iDS1f60Hje-lTYLaEDIrm_mNGWRT888avWZ03F4NYvJCN22gJrSaSdZMo6EMz-xqhkmAnSVaf0AY-8fa9TFh2k_-kl4cp4Adf_1_Zi8wpSRfqBZDrSu2BMn2BBmiJeWDwrNjPO9Kjt-Udb8LkpPBk52gs54RF8HiZ9cLU1lt1y42A9HiqHcpO2Fq67R8Yqk-Rcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=sM7vk3mCfi31VXRSFQUIwEPJGnGQMXchgcb-EBrtGtS9jA4vaIH7q3pA3mFFtu1XyZ8PgVEGP0-qCYb351q-6kmxTebSuyi5LeOCn4hX9Echje16Lzlay3lOJ-SOMsmvaH8J6Kgt5kqtNXzYC30iDS1f60Hje-lTYLaEDIrm_mNGWRT888avWZ03F4NYvJCN22gJrSaSdZMo6EMz-xqhkmAnSVaf0AY-8fa9TFh2k_-kl4cp4Adf_1_Zi8wpSRfqBZDrSu2BMn2BBmiJeWDwrNjPO9Kjt-Udb8LkpPBk52gs54RF8HiZ9cLU1lt1y42A9HiqHcpO2Fq67R8Yqk-Rcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71483" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d66564850.mp4?token=EJKX3dZqH3YMv3OuhYGWm8HcgraWpPpzJk6EZoxBtOe9edoR7g8pbpV_w6xsocoOaQ2WFCSUI26YQayExjC9axl59p2NlX87YoBdlJDyBoMLADLi3viJ9S06oFjrZxhdf5xm-0PP710R4jNbZRBXngM-e__sJZzjS_daTfXY0TaQ46Mz930-uFyD3YCNSL-jp2oLoKyMiT_sDvYbPpN6Lv8CX6hgP3ePLT7j1tRdokVf0rszuNn8V9YJCDPEv4tCdSAvumekAcN--0Mf6f7o3cT4R-iFHiAOznJKi5ttXodGc5AbSGHGn2gdt_cpyhz077U-K3bJyKB06XzfnwY5ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d66564850.mp4?token=EJKX3dZqH3YMv3OuhYGWm8HcgraWpPpzJk6EZoxBtOe9edoR7g8pbpV_w6xsocoOaQ2WFCSUI26YQayExjC9axl59p2NlX87YoBdlJDyBoMLADLi3viJ9S06oFjrZxhdf5xm-0PP710R4jNbZRBXngM-e__sJZzjS_daTfXY0TaQ46Mz930-uFyD3YCNSL-jp2oLoKyMiT_sDvYbPpN6Lv8CX6hgP3ePLT7j1tRdokVf0rszuNn8V9YJCDPEv4tCdSAvumekAcN--0Mf6f7o3cT4R-iFHiAOznJKi5ttXodGc5AbSGHGn2gdt_cpyhz077U-K3bJyKB06XzfnwY5ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت های عجیب
پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:
نزدیکان رئیسی گفتند که حاج‌آقا خودش اقرار کرده که اقتصاد متوجه نمی‌شود.
بعد گفتیم خب، یعنی باید برای رئیس‌جمهور کلاس اقتصاد بگذاریم؟
گفتند نه، کلاس اقتصاد که نه؛ حاج‌آقا ذهنش می‌پرد و خسته می‌شود. بیاییم موشن‌گرافی بسازیم.
ما یک تیم انیمیشن آوردیم که برای رئیس‌جمهور مملکت کلیپ‌های اقتصادی درست کند. قانون هم گذاشته بودند که هر کدام از کلیپ‌ها بیشتر از سه دقیقه نشود، چون ذهن حاج‌آقا می‌پرد.
ببینید چقدر این موضوع تلخ و «دارک» است که برای رئیس‌جمهور مملکت و بالاترین قدرت اجرایی، بروی انیمیشن درست کنی تا بلکه اقتصاد را بفهمد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/71482" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71481">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=T1jWqpin921NnidoF9oKhcqBGozx8Tzg9pfZlVBIDEfYTLaElYaodKkMo3fTfGyZ-aX38md2-p_SAA3FaRm55bxr4ofUKUckPKQGDKe9OsjuCFWUyOFUx-4aA2lFLHg4Z1aDCqsoWYdBzlXpxhCVGEH5MCgl55Q3cGCfAqoPWrqWc7LW37xpAY7-CmAhEt1QbzvOcdnNPYPi6NXBeI3rFFV34sfybHBbcNt3fLICA9Ab2z4KojzzzVYYgF7djzQKei0u4J6Bqf0JBtH_S6R-osT7vEbFz_D22rl591VrW9c91vDdmFhYLq_evF4F8NGWr4EHxjMgPRILX0lo2EQZ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=T1jWqpin921NnidoF9oKhcqBGozx8Tzg9pfZlVBIDEfYTLaElYaodKkMo3fTfGyZ-aX38md2-p_SAA3FaRm55bxr4ofUKUckPKQGDKe9OsjuCFWUyOFUx-4aA2lFLHg4Z1aDCqsoWYdBzlXpxhCVGEH5MCgl55Q3cGCfAqoPWrqWc7LW37xpAY7-CmAhEt1QbzvOcdnNPYPi6NXBeI3rFFV34sfybHBbcNt3fLICA9Ab2z4KojzzzVYYgF7djzQKei0u4J6Bqf0JBtH_S6R-osT7vEbFz_D22rl591VrW9c91vDdmFhYLq_evF4F8NGWr4EHxjMgPRILX0lo2EQZ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین پایگاه دریایی نووروسیسک روسیه - بندر اصلی باقی مانده ناوگان دریای سیاه - را با حمله ترکیبی پهپاد و موشک در طول شب هدف قرار داد.
لیست خسارات تایید شده قابل توجه است
؛
ستاد کل ارتش می‌گوید سه کشتی جنگی (مین‌روب ژلزنیاکوف، ناوچه حامل کالیبر، دریاسالار اسن، و کشتی پهلوگیری پیوتر مورگونوف) به علاوه انبار سوخت مورد اصابت قرار گرفته‌اند.
اطلاعات و OSINT اوکراین، ناوچه دریاسالار ماکاروف، یک کشتی موشک‌انداز بویان-ام (غیرعملیاتی ارزیابی شده)، کشتی گشت‌زنی واسیلی بیکوف، چندین قایق موشک‌انداز و دو رادار دفاع هوایی در نزدیکی گلندژیک را اضافه می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71481" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71480">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71480" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71479">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXZHNRTcKAeAQhTog_A9DHmTmsT1mtsBRkS6u15gfTAzJaBOItSVHp0d8tWLaqLrPSXHmVbeZEifoKFlm6rGXI_mUpzF-073OzXsIL8hcvPNKRkuHdy7xEoolxcyQE2L0WXFGq2HEQ0w3cym7Y3hhcJfYDPCOKrCoJ2oRgm6A0h2orFhzNshSbp55iymwebgTZVxJrU1xavvU6tbBG9pRBdilrg0NC_IV58ZoVARzL9oMstM8S0PKEkfmibaJyUEaIqpY7FEyyuTi-5WLVRYn-iq2N4VBa982MLfPgGRyBLwbnUn8nfYswYxPmLNMomjI4UM7WgEjM72rWSHPgg9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71479" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXf3qRSfax1lBcBG5lAP6geBpomLRxdh0W3iMPzcDGzxG82LUuBP8PjioQMYfpmcq54JIiBqhTEVY7PAXZgBu-SjRPVyuZRQSzLOM7FKyo2JXwioGJzikJuxxIInzxW8DkqoUK95WMX1RpC2P2omeY-4lkZJE-_AkhP8TiQJsxr6nRmTSP5vE7FQm8-WfzqCjKajhEiwsdEdmztmZIamZDJAAkWnhijv5q0PF5XvpmFSua9Y6XGeBu1eRSRkAmruJZ-znGP2OCUZp7PHOJZO2mDjob5CMSc-JYe7a_BgdDMC9prPV1ENhe1LLCvm4BrZsgZ-8XPzkZEhLXpNooY7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71477">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=g8rykAeSMyTT8wsu5dAx3hef3fyDn_cyRCJJAKowwtqE5y5fGpDfE4BrfcFeq08HpfJFTSiV2P-UkOBLGjKJ5uQKByFYfrngvB_lbXCpQbVtlZml29L6GTQdPiQ51l8ZKa0wRTWWA8wLLqV_-_X1zNV6C8LBYuysDOVsA-Zb1HwEf9-Q1od6MlCkOt2UMQf3-6W9FHFjtd_60yCJgEUJEQWxzSaMBguLWHWEn2lXJ256U9NqbpmGDQ7ssCfYEEVBXMy-80zpUJ4w_cku3NvmhAsguht7L864MDv8UiJqCCBrx0CpGlR3bjcBjCms-6wGGHPLSuiI7GeENDXcmIA9DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=g8rykAeSMyTT8wsu5dAx3hef3fyDn_cyRCJJAKowwtqE5y5fGpDfE4BrfcFeq08HpfJFTSiV2P-UkOBLGjKJ5uQKByFYfrngvB_lbXCpQbVtlZml29L6GTQdPiQ51l8ZKa0wRTWWA8wLLqV_-_X1zNV6C8LBYuysDOVsA-Zb1HwEf9-Q1od6MlCkOt2UMQf3-6W9FHFjtd_60yCJgEUJEQWxzSaMBguLWHWEn2lXJ256U9NqbpmGDQ7ssCfYEEVBXMy-80zpUJ4w_cku3NvmhAsguht7L864MDv8UiJqCCBrx0CpGlR3bjcBjCms-6wGGHPLSuiI7GeENDXcmIA9DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به نیروهای نظامی‌ای که هم‌اکنون در تلاشند تا اطمینان حاصل کنند بزرگ‌ترین حامی تروریسم در جهان — یعنی جمهوری اسلامی ایران  — هرگز و به هیچ وجه به سلاح هسته‌ای دست نخواهد یافت، ادای احترام می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71477" target="_blank">📅 17:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71475">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=cHZGr6J27RiF74rFw10xxrCuda1a7B-ydG7RiDL-Wd_AhSP8ciOVEHZVuf1wrz6WOrjU12bprSnOiR1skdJBkVGObZeAsUy-JArOTggWf0VqUQ5e-MrCvxLBOdCRwC8BXzErlIyj_Dvh6bijGozvs5euwRkGXomAfgSBEKTCKO0nGQmL0tCfcAHi9nOOFXqYaRJGI2aY9Bo8S-FYageALUcWTx4q2mZ8r9oUnRbnsbiRC6onl6tsfEMjBilrDNcQi8-BapeGLEynbglUmeban7us9_rbL5uyKbvQASzDopOJek8DuN9SIOaaagcJUzZccQwlaVDVfcTpwfgmmz2QQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=cHZGr6J27RiF74rFw10xxrCuda1a7B-ydG7RiDL-Wd_AhSP8ciOVEHZVuf1wrz6WOrjU12bprSnOiR1skdJBkVGObZeAsUy-JArOTggWf0VqUQ5e-MrCvxLBOdCRwC8BXzErlIyj_Dvh6bijGozvs5euwRkGXomAfgSBEKTCKO0nGQmL0tCfcAHi9nOOFXqYaRJGI2aY9Bo8S-FYageALUcWTx4q2mZ8r9oUnRbnsbiRC6onl6tsfEMjBilrDNcQi8-BapeGLEynbglUmeban7us9_rbL5uyKbvQASzDopOJek8DuN9SIOaaagcJUzZccQwlaVDVfcTpwfgmmz2QQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ واقعه ۱۱ سپتامبر را به جنگ خود علیه ایران پیوند می‌دهد:
به همین دلیل است که امروز می‌جنگیم. ما چاره‌ای نداریم؛ تنها گزینه، پیروزی است. ما سرسختانه می‌جنگیم. برای پیروزی می‌جنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71475" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71474">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=SNFFRg02VLbDFPwcbpKVkbeoZrNrm11V1t9ljUEphndYRXh5rAGUWSRiCyhxJyhZGoGfW8jv5rhWLNrE0XTt59W1Uj0KKs11VVyojUoe1-UcT-FGm_wxsZo-D9Ne-B4SOrHcZNgd4lKrY6UYNlchG3neycKnvSZeLuUi2QXdhmhL1ju0PfT6W1kvPfLBJj9abxy8je3-mXaqq9j6CzZ9CK9f1srsZmzIGA5KRR9IsGrBp8GrVC6gT4--Ne157evJP_pdNur2Mos0-zEyE799SZozsZahOE0HacZZI0y2rPUf2xwqvPIpf_W95776AMqeXccSIMRWoMPlSwcaSRDvkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=SNFFRg02VLbDFPwcbpKVkbeoZrNrm11V1t9ljUEphndYRXh5rAGUWSRiCyhxJyhZGoGfW8jv5rhWLNrE0XTt59W1Uj0KKs11VVyojUoe1-UcT-FGm_wxsZo-D9Ne-B4SOrHcZNgd4lKrY6UYNlchG3neycKnvSZeLuUi2QXdhmhL1ju0PfT6W1kvPfLBJj9abxy8je3-mXaqq9j6CzZ9CK9f1srsZmzIGA5KRR9IsGrBp8GrVC6gT4--Ne157evJP_pdNur2Mos0-zEyE799SZozsZahOE0HacZZI0y2rPUf2xwqvPIpf_W95776AMqeXccSIMRWoMPlSwcaSRDvkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
آنچه اکنون در مورد ایران شاهد آن هستیم، حیوانی است که در تنگنا گرفتار و زخمی شده است.
این آخرین نفس‌های رژیمی رو به احتضار است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71474" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71473">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Z_a-u-4OsdQIlyLIHVK-V4fHIPZ6jKfotBgkG6XzR61sXJMWmrMG4PEzOO1HZxyx0iqgCmEO1jKYE0ukqSSlWioqReThFmiW7H6pkWTvAjA3BdbFLLreL0Gl6BvsullpmpkIJifAbYJVPICxpUpNzpN3_FJRzUjyAUUiXIrB58kXKaB-tmdbIqdhB7rWucL8Tvos8JXR1GLITOB427JmTHJEmP66boFfAe1TAPb0YVVAyAWVuifzefwWQplTiar8F_jhqLp9dveowhNIirSpS4U202UnEmSkpVc6OqcgZ3C767ypw-5bdaUN9lTRJIBx_iezSYISUoAGoL56jc83vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Z_a-u-4OsdQIlyLIHVK-V4fHIPZ6jKfotBgkG6XzR61sXJMWmrMG4PEzOO1HZxyx0iqgCmEO1jKYE0ukqSSlWioqReThFmiW7H6pkWTvAjA3BdbFLLreL0Gl6BvsullpmpkIJifAbYJVPICxpUpNzpN3_FJRzUjyAUUiXIrB58kXKaB-tmdbIqdhB7rWucL8Tvos8JXR1GLITOB427JmTHJEmP66boFfAe1TAPb0YVVAyAWVuifzefwWQplTiar8F_jhqLp9dveowhNIirSpS4U202UnEmSkpVc6OqcgZ3C767ypw-5bdaUN9lTRJIBx_iezSYISUoAGoL56jc83vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
اعتراض ربات های انسان‌نما در مقابل وزارت امور دیجیتال لهستان و سردادن شعارهایی با مضمون«ما خواهان قانون‌گذاری هستیم»و «از مشاغل دفاع کنید»
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71473" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71472">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=niQ6urnBQkzbn042Zi1__WmKP5cvc0__Pbq43MV8j8S7V5SHe_wijoOfNm2ZvpsKu3YSeEr8J5wk1BAbsQGsyFZvzuI_cgreX91mM65xyYr-pelwGE69X0hbHj-CtBOoSA1Ee-Y87qyizEV1YU_E1QHY7KWq5ARwnwSUVu2_Ug2jMzQCcCu87kmv0cxXhjg6qhgnSNapTmnMlH0C-k77PS5c5BmeMTXppkmElhXF-RgI3N-GRcHXonHyQ7ezGjSjzrHCvl0kpeYua4Wq4VaD250CbYAT2uNWxlOftXL7L8CLKFFI5vNtTyMyvLjZcIvkHtM8GoQr9tEuH3tjT6jiqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=niQ6urnBQkzbn042Zi1__WmKP5cvc0__Pbq43MV8j8S7V5SHe_wijoOfNm2ZvpsKu3YSeEr8J5wk1BAbsQGsyFZvzuI_cgreX91mM65xyYr-pelwGE69X0hbHj-CtBOoSA1Ee-Y87qyizEV1YU_E1QHY7KWq5ARwnwSUVu2_Ug2jMzQCcCu87kmv0cxXhjg6qhgnSNapTmnMlH0C-k77PS5c5BmeMTXppkmElhXF-RgI3N-GRcHXonHyQ7ezGjSjzrHCvl0kpeYua4Wq4VaD250CbYAT2uNWxlOftXL7L8CLKFFI5vNtTyMyvLjZcIvkHtM8GoQr9tEuH3tjT6jiqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇶🇦
هم‌زمان با نخستین سالگرد حمله هوایی اسرائیل به دوحه (قطر) در سپتامبر ۲۰۲۵ — که نخستین حمله اسرائیل به خاک قطر محسوب می‌شود — تصاویر جدیدی از این رویداد منتشر شده است.
این حمله، مقامات ارشد حماس از جمله «خلیل الحیه»، مذاکره‌کننده ارشد این گروه را در جریان مذاکرات آتش‌بس هدف قرار داد.
اگرچه رهبران ارشد حماس از این حمله جان سالم به در بردند، اما شش نفر، از جمله پسر خلیل الحیه و یک مأمور امنیتی قطری، کشته شدند.
این تصاویر جدید که منبع آن‌ها شبکه تلویزیونی «العربی» (Al-Araby TV) اعلام شده، لحظه اصابت را از زوایایی که پیش‌تر دیده نشده بودند، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71472" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71471">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e182f67792.mp4?token=BFiyIvOcVQl6juu1RTv5bIoiBAAyojP7jCOYaQ4nm9KBAXqBXaBN8TQi3rh63YWdLZzvvseB37Q1Y7JYajKGDnA5IW_CFhNNHhKBwF7Qz9VhGwzzprWLnwrGwEnnX8Xw2pmYNdKLtOjr0QzxHkkzDl9ZDTYXRxLw3SKgEWwOXgDfZaYWmn_Oo1JCcY5kuqFjgqk-NCynT9IGLhw3houVcK71W8ujxchv48Ia6WyidBtZDu9eaihA7VXx258DnwHwrDRtxPT3jwzN9h1bj04uANCK2b6PdD_8ohG0RurK2-8-HyFhWJHiUgaVxoiZFkHTrP2FxrBRELIjbI50YBdtHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e182f67792.mp4?token=BFiyIvOcVQl6juu1RTv5bIoiBAAyojP7jCOYaQ4nm9KBAXqBXaBN8TQi3rh63YWdLZzvvseB37Q1Y7JYajKGDnA5IW_CFhNNHhKBwF7Qz9VhGwzzprWLnwrGwEnnX8Xw2pmYNdKLtOjr0QzxHkkzDl9ZDTYXRxLw3SKgEWwOXgDfZaYWmn_Oo1JCcY5kuqFjgqk-NCynT9IGLhw3houVcK71W8ujxchv48Ia6WyidBtZDu9eaihA7VXx258DnwHwrDRtxPT3jwzN9h1bj04uANCK2b6PdD_8ohG0RurK2-8-HyFhWJHiUgaVxoiZFkHTrP2FxrBRELIjbI50YBdtHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه های این بانو درباره وظایف زن مرد توی ازدواج ۳ میلیون ویو گرفته واقعا مفید بود
😏
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71471" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71470">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=THtkLUFSTSt5oNf49yJGT0KmHbTXyufYR-1Gf4RmfuTNZMpD_i94hNgOlfoKZxa18Ndk-E5Is9YPHFHkU2q83qEcwSa9XDKrzhzVBa9FfprbiOodj2JixKpqimIc_FPap-dNdMUYQITROAsnQrA7f6pOBKFDoW8fWWKjYQNkrlJXVpGVx94hcAhYDgmUZkLeIq78MM2N__M89wqxzyKFZ_A_TZPqW7tb2GW4GkfbCxDvTfn7Na0eH7VT19ugTC0ZSO9V_7_24Bp8NghWfy2ZJBCLeWbP_A1hXefm230Z1_LdnV09nl7ueGsir7pO0Z1nkSWN7DEr5XiN_E7ul30_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=THtkLUFSTSt5oNf49yJGT0KmHbTXyufYR-1Gf4RmfuTNZMpD_i94hNgOlfoKZxa18Ndk-E5Is9YPHFHkU2q83qEcwSa9XDKrzhzVBa9FfprbiOodj2JixKpqimIc_FPap-dNdMUYQITROAsnQrA7f6pOBKFDoW8fWWKjYQNkrlJXVpGVx94hcAhYDgmUZkLeIq78MM2N__M89wqxzyKFZ_A_TZPqW7tb2GW4GkfbCxDvTfn7Na0eH7VT19ugTC0ZSO9V_7_24Bp8NghWfy2ZJBCLeWbP_A1hXefm230Z1_LdnV09nl7ueGsir7pO0Z1nkSWN7DEr5XiN_E7ul30_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شرکت پخش فرآورده‌های نفتی:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را بردارید
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71470" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=SwE66yd4KP3-DcEZAw5j5ddxcytnGbEGApPReJu0NJNUoNF6nsBw0CrHMtCrpADQFWKVKKqwtfsR-t7psfRmvTs126F4zB_s84f2Nwmv0YzgOU8KJtOoFbgXXo17npsZeiVkjQPknUOpKWsCgTvstwyFidsabTLPvn9Ut9JnIfpdsWqkj0UAbjvvrzaF2-ke7cgytyLuSAccxSgl4w_TCPWS8SaAaApObZ7Zz-1xCiYon2KNGeGsVSjW6V9Y6bxsS3YtRri_WeOZSSprWCKWRItHihtpFA19ML6bPDZGd4sJD_TbFdCIkzh5gXWr9LlHN-wKD8wVwZ_tE-EAnPVYKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=SwE66yd4KP3-DcEZAw5j5ddxcytnGbEGApPReJu0NJNUoNF6nsBw0CrHMtCrpADQFWKVKKqwtfsR-t7psfRmvTs126F4zB_s84f2Nwmv0YzgOU8KJtOoFbgXXo17npsZeiVkjQPknUOpKWsCgTvstwyFidsabTLPvn9Ut9JnIfpdsWqkj0UAbjvvrzaF2-ke7cgytyLuSAccxSgl4w_TCPWS8SaAaApObZ7Zz-1xCiYon2KNGeGsVSjW6V9Y6bxsS3YtRri_WeOZSSprWCKWRItHihtpFA19ML6bPDZGd4sJD_TbFdCIkzh5gXWr9LlHN-wKD8wVwZ_tE-EAnPVYKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=J8WKpvl_Bx-52qj__RVStv_jt2rlIsMIvYY6J6lCajtT0SUQnmUmOw2WDDVFbjVpRA74x4p2WbmKqTyW2oVONn0tIp2KPo9CfyiedF4A34ba5wk64LvPT7h6NCTTEvS4dK5r8c3GwhKxAB855QlQJLf6iU1MRQahzS5T_YaBvM0j2tE-kFJLVgWEiQ999RGFIgg7uRT6h9sQnF2Tayz9AdS-vACCCRwUQy5afDqqNAZlR799qEcGpNMJB2uftH5pbc3PTYPWUjVjIT53JOX77-dYzRsC7Ry2MUMPKH3xLvwlCDsebH_1-DMRsewUsV3dZBrLFrRqH1MQFM_vqJ5ZUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=J8WKpvl_Bx-52qj__RVStv_jt2rlIsMIvYY6J6lCajtT0SUQnmUmOw2WDDVFbjVpRA74x4p2WbmKqTyW2oVONn0tIp2KPo9CfyiedF4A34ba5wk64LvPT7h6NCTTEvS4dK5r8c3GwhKxAB855QlQJLf6iU1MRQahzS5T_YaBvM0j2tE-kFJLVgWEiQ999RGFIgg7uRT6h9sQnF2Tayz9AdS-vACCCRwUQy5afDqqNAZlR799qEcGpNMJB2uftH5pbc3PTYPWUjVjIT53JOX77-dYzRsC7Ry2MUMPKH3xLvwlCDsebH_1-DMRsewUsV3dZBrLFrRqH1MQFM_vqJ5ZUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=Bq7Bj92C0kbm4B3VO1VP_3td2ecqovfY6kZipgTc8tr39MywxUy6K1U8on-LJH-Pl5rIYF88CYHF2W7Aq_DnbgbBvlsATHCuY-6JqrAdvT6GCYAB-XotcC6jKXMiQWuygQlW147OTGUVG8zTb0WIVTCncEsEDPecUCBrPVsxfDHw2orgKGhDc32kCy2_2LnJckrmD7iFd_VUZ9L8bd2DVHAkm3O7vi3PaGuvoZTaeGA2E2-V0q3EO8zqwk34JJn3QxJnwyhRlEVrPRYbt5DbNTPGrM7xbzJNHV7Bj2ITMMUkOS4aCsnTH3cnYPAI_gf2UhHGwRxZ3-c3v5N4ab_3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=Bq7Bj92C0kbm4B3VO1VP_3td2ecqovfY6kZipgTc8tr39MywxUy6K1U8on-LJH-Pl5rIYF88CYHF2W7Aq_DnbgbBvlsATHCuY-6JqrAdvT6GCYAB-XotcC6jKXMiQWuygQlW147OTGUVG8zTb0WIVTCncEsEDPecUCBrPVsxfDHw2orgKGhDc32kCy2_2LnJckrmD7iFd_VUZ9L8bd2DVHAkm3O7vi3PaGuvoZTaeGA2E2-V0q3EO8zqwk34JJn3QxJnwyhRlEVrPRYbt5DbNTPGrM7xbzJNHV7Bj2ITMMUkOS4aCsnTH3cnYPAI_gf2UhHGwRxZ3-c3v5N4ab_3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTZ4MnquVW8S-qKmowWrmAhuYJlC-YRSgx2fad15Q2glGIaDR3JgCzTM6GgBKdv6mebH5V-Bc3C0B7hzr69YYAMzFMSTRYZtEl_M2tFz_JYyWsfCUrHSQERtId0DQ5KrutPZ3RXKVd_0CDYrqK-g0fKmkGtfBCW07wqc6tBQrEHpDDo1AvM4AM58z06igzPkty3J5_gf7zvQQQkpsIqlWCrejL9ULjJx4xugNSdthN_psW3fQ6XRgpLddFuKmrukgFRUjLQMfmmQJiaC6WHGLzbsSYDUCbQfm7xSPa6f56dAll1UdODS2KwbC_5O3FzBMVocm2HAuueAoEezDdxklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhwmdpD5QxkxT9nAE-ct_KBP_x470nlRa3xWRo43ZEcjJ1iadi4vHFEmOi_-eVW2xW9V5qiR2Wwba6L1aErH5e-D-bLUjXE441y90q5xWXMHndkF_YaQUa_Upuodic1TFIgUq2DLkpbdFnu6f2nWwif2U74xahnXsEuusCORWX91wdqhwRq03GJpoyZi14U-Gfxb4OqSmqPR-lZzSqBYKqOeetpBMGtgVTWfy06J3sm0UXAp7wJO9YVBCi29YrsOhAwWnJEhHbhY6XxiQreEvpeNvEcSkLG785_9fpPTlrH25UmaUN5M9dZLS6zX37xGSTPz3y4yAfxRvBUbMJwgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=iFV5xIxWy7s88rTKmG0yOEpmevIEy07mw7qWDK1Dva5WVCNDs2vMhYtbSvHs3geFei8nIyctS7_AnHJ4wC1CK2dHnUj80LU0kPUH1g-sBiD-a009azJS8cGJoVUZa2N-hyd9wmXUKnqpRQR4QRRNKQh3D00tHbvSZEdeHHXRyuIklOBXHaijqYPYwlNuyTvEbbu4EsIXun-tFSsZfQ4WFGpk-C8Ow9LuhhLBDVA4nmTpY_QapJM3cRr5FamMu56z_-gyXf5dY73dVQ0zwis516WfeT0cHsPbqoTdNF2TvA3CU46eDD0zUFrMXdy-l8hPagPhVUCGZfmDKKnqZQ7BIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=iFV5xIxWy7s88rTKmG0yOEpmevIEy07mw7qWDK1Dva5WVCNDs2vMhYtbSvHs3geFei8nIyctS7_AnHJ4wC1CK2dHnUj80LU0kPUH1g-sBiD-a009azJS8cGJoVUZa2N-hyd9wmXUKnqpRQR4QRRNKQh3D00tHbvSZEdeHHXRyuIklOBXHaijqYPYwlNuyTvEbbu4EsIXun-tFSsZfQ4WFGpk-C8Ow9LuhhLBDVA4nmTpY_QapJM3cRr5FamMu56z_-gyXf5dY73dVQ0zwis516WfeT0cHsPbqoTdNF2TvA3CU46eDD0zUFrMXdy-l8hPagPhVUCGZfmDKKnqZQ7BIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
