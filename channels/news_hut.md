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
<img src="https://cdn4.telesco.pe/file/ZEsrOZOwbW9Zd-V92GXDi9w3tBrWShkLvCVqBT36BMWaC-wOaieo2KfSm6e_9UE4T0PldMdkuig8IBishZmIte7f-lMvvchPCvap8yMiKapcD-eTQcV4EYjJY3X38XaAd6zAYvpU2ckdg4_0htPjuEG1GRimfKzZlwPYr8Zgz53rw8JEE6aYv2ylVHB9E3hrbMxuaY882fSSNJbGqdxG6G0WxtoTAzbBgeT8YxIjVdxlrjNsaWJsEiwVjxT_8Pq5APKjMydbZdtkxt4dykCwE-DaPUTyHwMZVPZK5bSKHefmwsw-2rY7-eTqXZdE6-Y38cpYrYZPLy_Z1NZSf8OvYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 11:00:35</div>
<hr>

<div class="tg-post" id="msg-71811">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=cYkVfwHaxcdji7SIuQdpoTA4obm6f_kGFYAeS5QNdL_uZWqvepkk8_A25tkuKOuKsqXiNQV7muj6b6hCyW9o27L8FgopgdbHU8P7lmksjjeg_3TUzN_SC89k7BD9InuR016_ThBUr80mQkPBw3tUtsPXMaVzDoGknYf06nLGljWhIJBL7qi9WaygkjHpAtk4yLrLp2ff26WM3LnYku60lsmm7NRVidSV43o9S04JQw9PYV9LXqUGWB8t7wR4SLzJQk_1tRGLyHUvXhc7xkWUynUvjG0KQ-owvDrZo2gOl50nQffIJfNPB2Giw3DAQYcjjsr3kmmZcklvasPz2tM_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=cYkVfwHaxcdji7SIuQdpoTA4obm6f_kGFYAeS5QNdL_uZWqvepkk8_A25tkuKOuKsqXiNQV7muj6b6hCyW9o27L8FgopgdbHU8P7lmksjjeg_3TUzN_SC89k7BD9InuR016_ThBUr80mQkPBw3tUtsPXMaVzDoGknYf06nLGljWhIJBL7qi9WaygkjHpAtk4yLrLp2ff26WM3LnYku60lsmm7NRVidSV43o9S04JQw9PYV9LXqUGWB8t7wR4SLzJQk_1tRGLyHUvXhc7xkWUynUvjG0KQ-owvDrZo2gOl50nQffIJfNPB2Giw3DAQYcjjsr3kmmZcklvasPz2tM_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائم‌پناه، معاون پزشکیان:
حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و ... را هم گران کنیم، می‌شود ۷میلیون یارانه در ماه به هر نفر داد‌.
@News_Hut</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/news_hut/71811" target="_blank">📅 11:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71810">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9pGGE4p1TkHpsF-pjAaEf1YtbtRB1ViBRcD5mSQqIhcGiSF47jhwwpCFQjQdLZ5bUoWTQKYIoa4uOEyoiIBb1UyMO80ZbSbbiRISOMx4WiZe3nZI12p3oQSsnQXdNuzXlfPPocGhjnV5zVY-Ncgdspyqw-FX_kogDn8cwjxNAJ1wjDXkJMdv3OGln3uMudFUzW0tpnD7lnrAuNuRjGmFA8s-NrHDhY4uuWPhA5H_Gq0aywXwop3T4ung7Wd6ksLFk5hCAgoV5udg7nla3EPyfIjyqgoJljRC1xWYxqkdpV_w17NBCAgsX-Af2lg15-WVubfdTT64Y7pSJhAnlmE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
🇨🇳
—مقام‌های اطلاعاتی آمریکا ابراز نگرانی کرده‌اند که در صورت نهایی شدن فروش برنامه‌ریزی‌شده ۲۴ میلیارد دلاری ۴۸ فروند جنگنده F-35 و یک موتور یدکی به عربستان سعودی از سوی دولت ترامپ، چین ممکن است به فناوری‌های حساس این جنگنده دسترسی پیدا کند.
بر اساس گزارش نیویورک تایمز، یک ارزیابی اخیر از سوی آژانس اطلاعات دفاعی آمریکا (DIA) بر دسترسی چین به تأسیسات نظامی عربستان، روابط دفاعی پکن و ریاض و همچنین استفاده گسترده از فناوری‌های مخابراتی چینی در عربستان تأکید کرده است.
تحلیلگران این پرسش را مطرح کرده‌اند که آیا آمریکا و عربستان می‌توانند تأسیسات مرتبط با F-35 را به اندازه کافی ایمن کنند و مانع دسترسی نیروهای نظامی یا اطلاعاتی چین به فناوری‌های حساس شوند؛ به‌ویژه رادار پیشرفته و سامانه‌های شناسایی و نظارتی این جنگنده.
نگرانی‌های مشابهی پیش‌تر درباره فروش احتمالی F-35 به امارات متحده عربی نیز مطرح شده بود؛ به‌خصوص پس از گسترش روابط نظامی، اطلاعاتی و فناوری ابوظبی با چین. آن قرارداد در نهایت به مرحله اجرا نرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/news_hut/71810" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71806">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=jruEJ84rPJ36nQeP52H5BW8DvtloNyIokNYSgsZ8xiUYx7dOWidfgcEXEpHXWepoxPUywVsBBvpDvq3Qym2NrxyCPXiqMUXa3lcQZ1gto2UBM4FKPu-5E1e9HYeMNDQyKed-ysmgVoqQK36uO9ZERdE5fBH7Egj1nrGm2GKbkYL-YsMe3Y_BKQczEYgpynMAGpGR3wAwpphecQivklDMGk_lFkKGUKWg4FI1uJUKDztDU-QoeWAM-ShaxDAn2uRsp41uDGa-yAxUXEByXs00yL4tmI-XlkmgKJcKx8YA-pr6bz9H1Yb18zjMW8UOF6ZhOU99dsV-SlEtqru2HBIrMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=jruEJ84rPJ36nQeP52H5BW8DvtloNyIokNYSgsZ8xiUYx7dOWidfgcEXEpHXWepoxPUywVsBBvpDvq3Qym2NrxyCPXiqMUXa3lcQZ1gto2UBM4FKPu-5E1e9HYeMNDQyKed-ysmgVoqQK36uO9ZERdE5fBH7Egj1nrGm2GKbkYL-YsMe3Y_BKQczEYgpynMAGpGR3wAwpphecQivklDMGk_lFkKGUKWg4FI1uJUKDztDU-QoeWAM-ShaxDAn2uRsp41uDGa-yAxUXEByXs00yL4tmI-XlkmgKJcKx8YA-pr6bz9H1Yb18zjMW8UOF6ZhOU99dsV-SlEtqru2HBIrMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول که باشه، اسنوپ داگ هم واست قِر میده؛
دیروز تو‌ مراسم ازدواج یه زوج ایرانی تو لس‌آنجلس، اسنوپ داگ هم به عنوان مهمان ویژه حضور داشت که هم خوند و هم رقصید!
@News_Hut</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/news_hut/71806" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71805">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=WcIBk2svBxGGeCHggCTmlXddMZBdA_-QPDYUp8Umz_h-M3zBo8s_InmiwsX5dqekHponowWyCzY5L_jV-nKyAXSuodhkm-Pj5maQI5LdHeZop7JX8XSQsL7G4BFuipae2w1-r6NUrGdXTKpZR3S10lQqjO7PB1PKECdClnlMqk-2o-8zn1ZqmoMKJAsJt_LJcXX0O5G9IoXtDZooi7nppsi6Ym5yjVQMfNXpa8CFWvGCRnlh7AizN3WZ_HNiolTs29IxIBnQqSr1PswK2GPBjwBhhGNzJ3Qw27J-JsdVdfnyiEK-ZSFFzuOGStxP6Q6K7DLhIHUO9v5VVFwFQTM93FEH5dDja_-0M3dhAl_cDp_iwTkp4Qwd7LvmQs4O3r0o8zeit5-OSd4E0eA9cw02dzHK1TljOSfOjqQokY8RMx2DAlalUB6Rh4YUIW_BDOUJVhOsruqZ20YrU82sPMsLBh_NOVhA_Wm3_CANitO4TtwJd0K3vpjFQZUn4qPer3fy0tUbrG8Wd8TR6CyWPiuo9Pmzcd80KfVz1uC6SIP7ApVuhG-ahTMtroT_QAjw1BKV00XTO7vMR8_-xszsjBb91wGp4kRLutDtm32F6zbcBubXzV9A3ZDRGmSxpYjyEcocr1omDhzceJ2JK_ADqb1V3Sj3UJLBDYoBqzRLAO6bDO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=WcIBk2svBxGGeCHggCTmlXddMZBdA_-QPDYUp8Umz_h-M3zBo8s_InmiwsX5dqekHponowWyCzY5L_jV-nKyAXSuodhkm-Pj5maQI5LdHeZop7JX8XSQsL7G4BFuipae2w1-r6NUrGdXTKpZR3S10lQqjO7PB1PKECdClnlMqk-2o-8zn1ZqmoMKJAsJt_LJcXX0O5G9IoXtDZooi7nppsi6Ym5yjVQMfNXpa8CFWvGCRnlh7AizN3WZ_HNiolTs29IxIBnQqSr1PswK2GPBjwBhhGNzJ3Qw27J-JsdVdfnyiEK-ZSFFzuOGStxP6Q6K7DLhIHUO9v5VVFwFQTM93FEH5dDja_-0M3dhAl_cDp_iwTkp4Qwd7LvmQs4O3r0o8zeit5-OSd4E0eA9cw02dzHK1TljOSfOjqQokY8RMx2DAlalUB6Rh4YUIW_BDOUJVhOsruqZ20YrU82sPMsLBh_NOVhA_Wm3_CANitO4TtwJd0K3vpjFQZUn4qPer3fy0tUbrG8Wd8TR6CyWPiuo9Pmzcd80KfVz1uC6SIP7ApVuhG-ahTMtroT_QAjw1BKV00XTO7vMR8_-xszsjBb91wGp4kRLutDtm32F6zbcBubXzV9A3ZDRGmSxpYjyEcocr1omDhzceJ2JK_ADqb1V3Sj3UJLBDYoBqzRLAO6bDO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین خواننده جهان به ۱۶پرومکس راضی نشد رفت برا خودش و داداشش ۱۷ پرومکس خرید
حالا حرفای مغازه دار:
آقا محمد مرسی که افتخار دادی اومدی از ما خرید بکنی
واقعا شهر ما خوش شانسه که چنین هنرمندی داره
ایشالا آلبوم های جدیدت رو با این گوشی ضبط بکنی بدی بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/news_hut/71805" target="_blank">📅 09:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71804">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7yKNuPd4U44iyv2_D4-sUQcCIyTeJccdOMkZqaIsNtFRZ31ca7xUwhlW5dz090FfYCYR6wogtAPmzHKb2S0YBRMp9TkOchNcypGbBdetcPthN5pxoPCdi4OAoyaKsEvQDM1ahevFzAkaFMaZ-2LgmeEuKozAz2rp3S097sSGFYevWyapBkBnkag3DXNfsc3WnI2EIYD04A4djK_5AVF8Rk_lnhjXxb8TdWOQHdYxf0Pm7thMwK-2s1l7GsXbFxbtmrE2rKXZRjue8TA-bPvNhsMVlL5j4iiJcws_EpDhT7C_yZxLI9ZVFASfFlyufs0Lerv_bRAVFyGEstOAPmU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامی پیگات، معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران با سرکوب بی‌رحمانه، کمبود آب و برق و تورم سرسام‌آور دست‌وپنج نرم می‌کنند، مقامات رژیم می‌خواهند در نیویورک به خریدهای کلان و لوکس بپردازند. ما اجازه چنین کاری را نخواهیم داد.
ما اجازه نخواهیم داد که نخبگان رژیم ایران از فرصت مجمع عمومی سازمان ملل برای خریدهای لوکس و پرهزینه — که به بهای رنج مردم ایران تأمین می‌شود — سوءاستفاده کنند؛ آن هم در شرایطی که رژیم ثروت ایران را صرف حمایت از گروه‌های نیابتی تروریستی خود می‌کند.
ایالات متحده همچنان مقامات نمایندگی ایران در سازمان ملل، مقامات بازدیدکننده و وابستگان آن‌ها را از خرید عضویت در فروشگاه‌های عمده‌فروشی (مانند «کاستکو») یا کالاهای لوکس در اینجا منع خواهد کرد.
فروشندگان منطقه نیویورک: هوشیار باشید و در ارتکاب این تخلفات شریک نشوید.
@News_Hut</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/news_hut/71804" target="_blank">📅 09:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71803">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=XfnJkI-rizE9uRzEb1gcQnHgD1isA98AVUWZiIKHoILE8bCvOPNQZ5xK_HGs1RFTnq0wFMtCdxvZxMgtaHOJLBEfZPvEzB4L-K-XrYYT93_c6wBuYke8gR3jZ8yWHuNFw3AdCP_13jscipPbAiGxlNIblGWocuwyXy04n2YZPCu8Sfl30jTh-vg8Hm9t6V223HmcggjdlwhV_u79_lE33C5ccoQHtqB1cJPJ74rp8kQSzNo1lQFO6O-Gws2qmtU3r4cxDuVNSjgCGLBfdQAnduP5Jq0m3C7ry0YD7DQULrI-uyYXkhpjMkAY4Iczo0mZ18Enaz6k2isDZYdJPvoPYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=XfnJkI-rizE9uRzEb1gcQnHgD1isA98AVUWZiIKHoILE8bCvOPNQZ5xK_HGs1RFTnq0wFMtCdxvZxMgtaHOJLBEfZPvEzB4L-K-XrYYT93_c6wBuYke8gR3jZ8yWHuNFw3AdCP_13jscipPbAiGxlNIblGWocuwyXy04n2YZPCu8Sfl30jTh-vg8Hm9t6V223HmcggjdlwhV_u79_lE33C5ccoQHtqB1cJPJ74rp8kQSzNo1lQFO6O-Gws2qmtU3r4cxDuVNSjgCGLBfdQAnduP5Jq0m3C7ry0YD7DQULrI-uyYXkhpjMkAY4Iczo0mZ18Enaz6k2isDZYdJPvoPYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
به گمانم آن‌ها در آستانه فروپاشی هستند. می‌دانید، وضعیت فعلی اقتصادشان بی‌سابقه است؛ بدترین وضعیتی که تا به حال داشته‌اند. تورمشان از ۳۰۰ درصد فراتر رفته است. حقوق سربازان، نیروهای نظامی و پلیسشان را نمی‌پردازند. اوضاعشان به‌هم‌ریخته و آشفته است. باید دید چه پیش می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/news_hut/71803" target="_blank">📅 07:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71802">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71802" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71801">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/71801" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=kGs5M84_p-J07bP2zJ1nlaTLz8TvUdEgAmXTb-reYAcJQq2KiQx0DBKfXJ2_eAOSrN22qW3648dV3iVQXwqDdxp7Du5wY8O0hhsQ0qaaFkQlTD48j7MCELyqobEsvzcxX0QZQM63SyvVd_oYgRRr5BXdoLofAAGusdZr06qeUuF6pI4kwbFcFrj0VdfeMhfO9TLay38GVbgiRt-hRwXjKUMQoYj9FBq1oAn-H_3Xubk2ZWQff5Y4IUaWkEbJ4edagG0-J41fYy2ONPFDl3ymC8aXuWs5W8YeupNHbd12-KFC8j3u__oGk9UfCaZe5ld6TVgQfDngRfEBcyh-xR-e5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=kGs5M84_p-J07bP2zJ1nlaTLz8TvUdEgAmXTb-reYAcJQq2KiQx0DBKfXJ2_eAOSrN22qW3648dV3iVQXwqDdxp7Du5wY8O0hhsQ0qaaFkQlTD48j7MCELyqobEsvzcxX0QZQM63SyvVd_oYgRRr5BXdoLofAAGusdZr06qeUuF6pI4kwbFcFrj0VdfeMhfO9TLay38GVbgiRt-hRwXjKUMQoYj9FBq1oAn-H_3Xubk2ZWQff5Y4IUaWkEbJ4edagG0-J41fYy2ONPFDl3ymC8aXuWs5W8YeupNHbd12-KFC8j3u__oGk9UfCaZe5ld6TVgQfDngRfEBcyh-xR-e5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اتوبوس غیرنظامی اوکراینی در زاپوریژیا هدف حمله پهپاد انتحاری (FPV) روسیه قرار گرفت که منجر به مجروح شدن ۳ سرنشین آن شد.
محل این حمله در مختصات 47.7794347, 35.2161182 واقع شده است.
این منطقه پیش‌تر نیز در اوایل ماه اوت (طی بمباران یک گل‌فروشی در آن خیابان) و همچنین در ۲۱ اوت (در جریان حمله به یک مینی‌بوس) هدف پهپادهای انتحاری روسیه قرار گرفته بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71797" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=olkSMMTo9eS4bLdbbXviQYcHpkUZLPg0TKWHqcIOycX6UIUAHpBXQAbNnpTmIXXG2bOex3DRycnLFD9_VQK451kat-KiCXsbe_WvTWgXIU5LP_iSP_RBfFr8rsNCW9zYmzr4NwNZiZt0b8Uruku4lC_yvGCBVVBlCrYC9F_nXxmxC5vp37UEjPhtKgpuhtAapPr60rzug8x6MPpHEhmKC6Cs6-_8GGZzjchLh76ZWw2oPmWXVqBh6O5xJjShf63JsbgzAhvMyanrikjXACx_wV4fTbSebZ1S_CMIkKAGbn-wdvsvdvMOMKu7DgD3VtziIusPOa9i-ZsP45Eb_bZ3TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=olkSMMTo9eS4bLdbbXviQYcHpkUZLPg0TKWHqcIOycX6UIUAHpBXQAbNnpTmIXXG2bOex3DRycnLFD9_VQK451kat-KiCXsbe_WvTWgXIU5LP_iSP_RBfFr8rsNCW9zYmzr4NwNZiZt0b8Uruku4lC_yvGCBVVBlCrYC9F_nXxmxC5vp37UEjPhtKgpuhtAapPr60rzug8x6MPpHEhmKC6Cs6-_8GGZzjchLh76ZWw2oPmWXVqBh6O5xJjShf63JsbgzAhvMyanrikjXACx_wV4fTbSebZ1S_CMIkKAGbn-wdvsvdvMOMKu7DgD3VtziIusPOa9i-ZsP45Eb_bZ3TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسن زاده فرمانده سپاه تهران:
فردا ساعت 4 صبح رده های سپاه،
یگان های بسیج و گردان های جانفدا از میدان انقلاب تا میدان امام حسین چینش میشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71796" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بی‌بی نتانیاهو درباره ایران:
پیش از هر چیز، باید رژیم ایران را سرنگون کنیم.
این مأموریت من و مأموریت اصلی ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71795" target="_blank">📅 23:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ساعت ۲۲:۴۰ پنجشنبه؛ ملوان‌ها در اطراف جزیره لارَک، از چندین انفجار در نزدیک کشتی خود خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71794" target="_blank">📅 23:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8MRiFz2aQFpRIvoFa3HXlz3RFpKr0QNEigLu1-XqnpkFVtw5AnRcFYkz5sanzp2E8rc44xF_g5xYC7yL8aMsapHJOPI4v9RKEc4a0fTxo7rNRfr7Vd8Dn_4_fVI8gv0drnrlO9GGma2nPkihlTCVVbcYfkxrcCKitOmFHbggSfmjVY7znzUYkduapWfA_fJmW0o6dfB-x12rY09nKsCiYazzWS855aGjbMGmszEkPnw9c4RaJwLDcpPqViTR0AIuGvkjZDRjqFPT4kP4M-WwLtsJau2Q2i5oHdrz__vDpRnZQb-NFHmJ0EVC3NiNeu-5MqLIlOg56Dhwrq_yWA33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک «حادثه امنیتی» در فاصله ۱۶ مایل دریایی شمال شرقی «خصب» عمان خبر داد که شامل حمله به یک شناور در تنگه هرمز بوده است.
هیچ‌گونه خسارتی به شناور یا جراحتی میان خدمه گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71793" target="_blank">📅 23:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdAgYTFF4PP4iadqPjsSFBgweefXg1AZhs0UUo0dor__U3LGsT4hikJl3STiRmrcxfCiSTumZv4bPoIBN8BOqsreU0aG1O7nE2oV_49eOMtnV1LVWhAKyhHKD2mim7H1GDfuKd-YRqS8eHvVhz1_fAd7ZbEDvyoY7gIUFbpC4xnsut2NaFCOOzW03a2hkTthrnYX0ilyEM-QXxWJKgF_pDjAgg7Zy4oLNgT5jT9cN0ooVoGyfAtLsl97Vz1c2a9wHuOVxfBXV3SXmxpCXBnumXccw10CCV0pN-htxnRm7Im1itJDHAY91P8aOUvtsyEjkiYWZYr-jOmArosQEy3xIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا «بیت‌بانک» (BitBank) — یک شرکت فعال در حوزه دارایی‌های دیجیتال در ایران که تحت کنترل بابک زنجانی، سرمایه‌دارِ پیش‌تر تحریم‌شده، قرار دارد — را به اتهام تسهیل دور زدن تحریم‌ها و انجام فعالیت‌های مالی غیرقانونی، تحریم کرد.
این اقدامات همچنین شرکت «تجارت الکترونیک پیشتاز سیمرغ» (توسعه‌دهنده بیت‌بانک) و سه تن از همکاران بابک زنجانی — شامل حسین‌علی ذاکر حسین، محمدمهدی ذاکر حسین و سید عادل حیدری — را هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71792" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71790">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-rKuGOzkSAphjB3XAXKM2XjUeyP_PnMi_UJ4X96vS0ZAQp32KNtHWa0Ky2VTj07psdJrF1Mc358wdyMw2-GuY_g41x7CsUpj1A-xBcNh0BV1X5ycPwSZilinuj9fp8prQkRPnGKw1zwV_GlWjvoFd571y74oPb870DsMUeV7Sd06PQBWhpJOLm8qiFbl7ugTh1Ks051TWJy2aHBwwDm3L_mbLyZ-CtPvRszsnekmDagN60GbvFH7D5u8sWKvRQPEzD7p6ZEzKp0wT1dm5YsZUVMIKb5lwbsvsWgaoaKRRK4_LYk1b-YcOc-LTXE-VjMpl-R9V1oJoC_urxkG11aCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOYphqQUh4YlJYO70cynWHP3VfPcntUW_ajmtjnTISUxxvDap60UIsKC5hPMOmR7zxa1dz8xDYbrZyUtOYuFq-iy_hBjzmGo7bXeiXqYXRgmSv8s3ANbhTaSTLH_67x5C8gwg1Lm5oK0GkYDdWg7iSVk2ID9XKTgZ1hZO_tthInEx35mnhfpJNjjjpzBU-LvjVVb-JR3r2AhESGuEXHD7T714y7k5suJ0_Cyqt6KiYpQWLE2Ymb1G51btDAcs-Gj3EYVzufZj5bW5OjvpkeS-SR2L5bUs2ZJBwKljDVHNf_E4PX2p2O0fsOsuChXTkUOE6SU2QgICs1mLyJb3O9EtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران به سرعت در حال بازسازی تأسیسات طالقان ۲ در مجتمع نظامی پارچین است - یک سایت سابق برنامه سلاح‌های هسته‌ای در ۳۰ کیلومتری جنوب شرقی تهران.
ایران یک برزنت بزرگ روی این سایت کشیده است تا کار را از ماهواره‌ها پنهان کند، و در زیر آن ساخت و سازهای سنگینی مانند کامیون‌های کمپرسی، بولدوزرها، پمپ‌های بتنی، جرثقیل‌ها و دیوارهای تقویت انفجاری جدید قرار دارد.
این سومین چرخه بازسازی است. اسرائیل در اکتبر ۲۰۲۴ به ساختمان اصلی حمله کرد.
ایران آن را با یک مخزن مهار انفجاری جدید که در زیر یک تابوت بتنی دفن شده بود، بازسازی کرد.
اسرائیل در مارس ۲۰۲۶ دوباره با بمب‌های سنگرشکن به آن حمله کرد و سه سوراخ در محفظه ایجاد کرد و ساختار داخلی را تخریب کرد.
ایران تعمیرات را تا ژوئن ۲۰۲۶ آغاز کرد و اکنون به طور پنهانی در حال سرعت بخشیدن به آن است.
ISIS (موسسه علوم و امنیت بین‌المللی) بازسازی مکرر یک سایت آزمایش انفجاری قوی سابق برنامه سلاح‌های هسته‌ای AMAD را "عمیقا نگران‌کننده" می‌نامد
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71790" target="_blank">📅 22:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5IgIwDEjIqcapNCY3vIRW5ga8suezmuOnBusjEnH0d1S2LBrJad5LiunghmDz9JpdcvTLHy4ZCAyDRDQ4UR5kEkVVj733wRJLDTI5gXV60wkYt-IDwS6AUXpYF20Y3MM99bi4txQD-UwaT-vm2Rh4G6Rui7Ppm1mbHMEUYuImfMjqjZNQJn4B8FdTxx0qG81oQ_F5JT3cWIYpWPSNmMy6b4EJ7GwPxqpQ8O9QnWaHbmwnZmHXgRcLfMfe6J6VOumsLFtMJ6H9d43aWcnWmNt491U4k-t98QvAtjXwBHhoTt-URHoAjpo0Ae7K_WiORuSFqVToP3NCXEWEkSOvuPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Insrpl6Yj71gNNcbbwEVZRGfTysi-mZ22S0T8WrQ4RUrLe9F3chzB3drwSO7MfWkCZZ2AB7_CT8LwL65XNFURIWLYaoBeY9oia9T9DnOvHe2adokSvZJTTo25ZjO6PNQf_Mhibm3D3HUh8faXTdeLJ2SGvnjsJ2kaqh5pbfw1USfQA2WGi6clQ8R6gFwIthjJqd02YtDDVOcS6BwnJHnbBXJs7KULaUEsxS1QvT--kY5FZ8ebGgjLDbnblOy2bwy7EuHmMPCjeAxcTR3incBLQEzUYK223Ln9lGHFL-AoTzP33qr8f8_ItGoe26yyzUsbc-VOVgPwdrTszxU9FJnmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItzsFfGomuUiEoPODSB5txapGYDk8VLgUlPj31ZpwHWHmWqqCfLH5ijjDytpcGr4qrwj1X2_83WcaJaedu6349esnuhNhbsokOjHhpyUFLALa7JjgSqOStVJglD3Au8rg4DTUV0c3N3fZAF4icPvnG_duihKdOMkNnyJ_u5tIcXySEayx68mmviVbflK9dZLq_vB-QTmJKYrdhSM9XTEPuiyP-RAkjLGX1cT1MviXQgN8inQfvJA-VOMmUDMvc4esE3FcD3tPZhjwY6aQPjizQ5OY8ZeVOvhefyFfnl0SRhb3-H5-Fj7uUq0cI7tEAMYBanKnwuKE28vhidTDf2bug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس های وایرال شده از علی ضیا و زیدی در فلورانس ایتالیا!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71787" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=sJYmlQjVE6zomqaVbc3ZsW1L3atHktXoHYk2vIiXgtiicO9K464j0RKHqBNIieAF0OLx2Zt5Q-7vwvY-F-Qi9G74PtCzLP2zQvra4WFT2NKB2NmdJtqqhB0GwKbcPJy8FJu5uhqI3JSxIpk57wsYpnIzFIAxhSeOS20njc1dX_sUsqWckSmCzBDqnR9H51PS_0TDYNVrM7x2NEp6aKiWGYG346lfT-wz299a-qQaPGphPNupQ4T0Ow2DxHpheZDMwYSdzkG5q5b71WJzHb6bPGAjRHuZ2z1VOwzY3w-VvLh_Gr0WFX_4C5Gnp-8TK0CDATEYWQdQ6yHPhrtDokHdjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=sJYmlQjVE6zomqaVbc3ZsW1L3atHktXoHYk2vIiXgtiicO9K464j0RKHqBNIieAF0OLx2Zt5Q-7vwvY-F-Qi9G74PtCzLP2zQvra4WFT2NKB2NmdJtqqhB0GwKbcPJy8FJu5uhqI3JSxIpk57wsYpnIzFIAxhSeOS20njc1dX_sUsqWckSmCzBDqnR9H51PS_0TDYNVrM7x2NEp6aKiWGYG346lfT-wz299a-qQaPGphPNupQ4T0Ow2DxHpheZDMwYSdzkG5q5b71WJzHb6bPGAjRHuZ2z1VOwzY3w-VvLh_Gr0WFX_4C5Gnp-8TK0CDATEYWQdQ6yHPhrtDokHdjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واجير الونگکورن، پادشاه تایلند به همراه ملکه این کشور در جریان سفر رسمی به هانوی، پایتخت ویتنام شخصاً خلبانی هواپیمای اختصاصی خود را بر عهده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71786" target="_blank">📅 21:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71785">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#فووووری؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.  «تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71785" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR5ticVerR0egxFAZkqgYme_jA5NtTv31qmjTxtHI-wuxUCAZEYA9ngfTt8EqbBv6CAYQRwgTTZvDRHksbj1o4yrvwIUGchbTsFEHKZF9h6yNzrE1bL1hAyMszPFFv1VwYJwPMLznK6XsJYNTQlB0OCpSjRuCw3Vcyt196HnrffdNy8f3Yb_IXilAKwTLBqShXMguAafK_uQMKHWLweOQbj5gI-FyhMKAG73DqvwQFABLHRWz0Y-LGq8d0VYf9LEH15IoO7lLN7juSXJJYvOAaPA5Th7LApDY1rjvxjIbK339gIXpQ4y5IIX90hmMaB9q5j78Gmzt5u4pjW1_852sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فووووری
؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.
«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»
ترامپ اظهار داشت که قصد دارد از فرصت دیدار با رهبران شش کشور حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، برای گفتگو درباره گام‌های بعدی استفاده کند.
«می‌خواهم بدانم موضع آن‌ها چیست و در چه وضعیتی قرار دارند. ما همواره حامی و محافظ آن‌ها بوده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71784" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=tLk_9kqhHxU-9RfumsnyIdSEOITQ1l2InqPI74d9CkLIpTxm94tUyyxXhM1KjYa49Q9UbtHXegaSiaodjqavMvD5pcqFE-FWviK-r976x93wepGpL_5Ek2h3vY5nJe_pL_touij3Qar3AoNC7RHAICqr8pnfZO9Qhxvi5u5eL_WClwwr0zdHC8o71o5Me5Tz5y0v4BidFE_EzLjMdjS4zzC5aZzl6LXFeRd6DSh0NebluN4aAwmzptqKuoZKor_DB-ZcsDn8bYnRUpOROH6CfQ_Tkub_UABU9e6Cs1por4J_Oqx_AK_i9TVgud3ZTXaJBgi5iHvjGNrCrM_wkuN6zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=tLk_9kqhHxU-9RfumsnyIdSEOITQ1l2InqPI74d9CkLIpTxm94tUyyxXhM1KjYa49Q9UbtHXegaSiaodjqavMvD5pcqFE-FWviK-r976x93wepGpL_5Ek2h3vY5nJe_pL_touij3Qar3AoNC7RHAICqr8pnfZO9Qhxvi5u5eL_WClwwr0zdHC8o71o5Me5Tz5y0v4BidFE_EzLjMdjS4zzC5aZzl6LXFeRd6DSh0NebluN4aAwmzptqKuoZKor_DB-ZcsDn8bYnRUpOROH6CfQ_Tkub_UABU9e6Cs1por4J_Oqx_AK_i9TVgud3ZTXaJBgi5iHvjGNrCrM_wkuN6zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در شهر ری جانفداها با جمعیتی میلیونی رزمایش برگزار کردن تا آمادگیشونو به رخ آمریکا و اسرائیل بکشن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71783" target="_blank">📅 20:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC1lkLU0Mjos9n2EPbzOJblOEHYii6Ppbdx_ECBFy9kO-mPYGfDPotDEvLy8S5jBcAqapdu1OavngpI5g-0jrd9NQ3V5hK2baJwifXzgcfO_LUkkh2aQzCDZ38IKj4M-pUlyatCSAzpxteATYqzk5H_lAThczEI6Me9Zewkiwp0kTv_F68FQy9q7Q25KmGsLNXyBEjs5vu65tYhrUVF5_NvLEaIq_dgRlWy4idirVzT5WhVsGGnmfwGX3PDbb_7KJo2Rn6LcxWksQzEhkZY-x1y4swMGt2EUuMYTFRBL2ZDm8soRJSqCoE0YSgmSvrlMetOS9fzPFd5epl5JpanePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز، چین در پی درخواست عربستان سعودی از پکن — که پس از پیشروی‌های موفقیت‌آمیز حوثی‌ها (انصارالله) در امتداد سواحل دریای سرخ و پیرامون باب‌المندب صورت گرفت — به‌طور خصوصی از ایران خواسته است تا به مهار حوثی‌های یمن کمک کند.
پکن به‌طور علنی خواستار خویشتنداری، گفتگو و ایمنی کشتیرانی شده، اما در گفتگوهای خصوصی با تهران فراتر از این مواضع عمل کرده است. ایران در پاسخ اعلام کرده که ثبات منطقه به پایان جنگ آمریکا و اسرائیل علیه ایران بستگی دارد و همچنان مشخص نیست که آیا تهران به درخواست چین عمل خواهد کرد یا خیر.
چین هیچ‌گونه تهدیدی مبنی بر اعمال فشار اقتصادی مطرح نکرده است؛ با این حال، روابط این کشور با ایران از وزن اقتصادی و راهبردی قابل‌توجهی برخوردار است. در همین راستا، یک دیپلمات غربی اظهار داشته است: «تهران و پکن به یکدیگر نیاز دارند. چین عاملی است که تهران نمی‌تواند آن را نادیده بگیرد و پکن نیز خواهان بازگشایی تنگه هرمز و تأمین امنیت کشتیرانی در دریای سرخ است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71782" target="_blank">📅 19:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=ApPd9LUD0et_a-1oQ4IOMJ9Iu7YEx-szxbTvnz0kzNJEGtFyanT1s4-Jx-8MkwCly-l38ACILCEBDR3_tgT6cBUFIB-6VHO9JaWzzcgGx3sgz23e02ROU33ltwiKe-EGY7QvniiXME3Jy3RWZg_BXoud_-ox8Keb3pkypaovQv6Ts30BuJG5SHFnL0umlbaWuvOjTjGl_vL1NvQw8HF6mEQWniB2Ohqo7RBy6Y6MBI-jfMIinboNI0Am-WGTHFqX_kjpn8etsjTQ9O_G8VaRQRBBSP3JmcmvCO-wBBRowYcN8RK2TYvQwAVa3KeGdkJsjbT6OvU0W7UD89H5_8BJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=ApPd9LUD0et_a-1oQ4IOMJ9Iu7YEx-szxbTvnz0kzNJEGtFyanT1s4-Jx-8MkwCly-l38ACILCEBDR3_tgT6cBUFIB-6VHO9JaWzzcgGx3sgz23e02ROU33ltwiKe-EGY7QvniiXME3Jy3RWZg_BXoud_-ox8Keb3pkypaovQv6Ts30BuJG5SHFnL0umlbaWuvOjTjGl_vL1NvQw8HF6mEQWniB2Ohqo7RBy6Y6MBI-jfMIinboNI0Am-WGTHFqX_kjpn8etsjTQ9O_G8VaRQRBBSP3JmcmvCO-wBBRowYcN8RK2TYvQwAVa3KeGdkJsjbT6OvU0W7UD89H5_8BJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عارف:شرمنده مردم عزیزمون هستیم
واقعا از مردم عذرخواهی می‌کنیم، شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
نمیدانیم چه کنیم، نمیشود تورم ۲۰ درصدی داشت و رشد حقوق ۵ درصدی!
واقعا شرایط زندگی سخت شده و مردم رو درک میکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71781" target="_blank">📅 19:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=hG_IAWaPasMVMsRhcVa-umGLQ9Mz5eLFu_apoSxq3rsF8SVlrwB4HTRYLppjYBXLUMTfvYWx-MHkZulmdK3RkaUjU4FpI5WY2Tu0J-d0hrfNzlwuv82khkAVp5NAic2_b8ggz1LswXPJkEa4XAdE1oyVs-gEvgn_qDya95f4EIereZpg0WXa7JzqEoTN0N4jtpZJXfpZa_BFuHyMPeLQDmuWLT6V3U-znSb753KdiJ6iCSJ5ChbuGvUwRZyTaF2kBVCn_hSWCa4mKjJJypfoAOlUrIcHSQ5tcO4GkVmwsbyIfU0HKjD_FPH-A39u1R8hbgtQWldTnPFaAvYip1oG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=hG_IAWaPasMVMsRhcVa-umGLQ9Mz5eLFu_apoSxq3rsF8SVlrwB4HTRYLppjYBXLUMTfvYWx-MHkZulmdK3RkaUjU4FpI5WY2Tu0J-d0hrfNzlwuv82khkAVp5NAic2_b8ggz1LswXPJkEa4XAdE1oyVs-gEvgn_qDya95f4EIereZpg0WXa7JzqEoTN0N4jtpZJXfpZa_BFuHyMPeLQDmuWLT6V3U-znSb753KdiJ6iCSJ5ChbuGvUwRZyTaF2kBVCn_hSWCa4mKjJJypfoAOlUrIcHSQ5tcO4GkVmwsbyIfU0HKjD_FPH-A39u1R8hbgtQWldTnPFaAvYip1oG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلافروشی از اون مشاغله که نکات دارک زیاد داره
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71780" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=b7_8JdXKo45Jn4FudUaFnxRH_8zch1aPqDQUsreqD9W543anFrHzDmRo9SyBJoh96pqd7Aahnu-G2yS2Uibglz00DTni-uMgtr6y8n5bDSvKcorqmkGiwgRG9M4qnmP8MVkinqWvvMP0SGuEb4DHlT8KX8hh96IiIBuuQk7AHV13UnwIcGDB0Qjlsg_7UAXK2FUbtpp3u1Fj6QwoiYKbB4dRcbr4pZJv_6zIhug4qqHOzWey8opLLJzltV-r_m5AUm8dR_VON27sOoj6gn8pNnCSus4Ztw41ZGjs5tCoNUeATPE6ErGRQSaa3EGoKL_zg-9-jdPz8UUb6BpCPnX2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=b7_8JdXKo45Jn4FudUaFnxRH_8zch1aPqDQUsreqD9W543anFrHzDmRo9SyBJoh96pqd7Aahnu-G2yS2Uibglz00DTni-uMgtr6y8n5bDSvKcorqmkGiwgRG9M4qnmP8MVkinqWvvMP0SGuEb4DHlT8KX8hh96IiIBuuQk7AHV13UnwIcGDB0Qjlsg_7UAXK2FUbtpp3u1Fj6QwoiYKbB4dRcbr4pZJv_6zIhug4qqHOzWey8opLLJzltV-r_m5AUm8dR_VON27sOoj6gn8pNnCSus4Ztw41ZGjs5tCoNUeATPE6ErGRQSaa3EGoKL_zg-9-jdPz8UUb6BpCPnX2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش اهالی یه روستا تو هند که حدود 2 سال از وضعیت بدِ اینترنت و شبکه 5G کلافه شده بودن؛
زنگ میزنن تکنسینِ شرکت مخابراتی بیاد و وقتی طرف واسه بررسی دکل اومد، گرفتن و به همون دکل بستنش و گفتن تا مشکل حل نشه، آزادش نمی‌کنیم :))
آخرسر پلیس اومد و 6 نفر از اهالی اون روستا رو بازداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71779" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71778" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUqSkFnpYiHV5n_S1wpkXzLAbgLlF8WO5qVlBWfBoZ8IV3nRdy5wUIeJEYK8GcMHhcY3lOR-yUpgqu74n4xqG4G8q6d09ulyz9zorLWYSLsDwBE5wLgKGGurjCux7CFN2Ui_A__9yGT_Mogvbv4K0TP-crqmL90skbKbuPhaV9xiYTYHUeopYRaPinDCzmKausThA0CtPhjYlbYRCnWaIz725eWtu9QkJregGyNvtedo8V4VkP4apcfon0klowVBoDhZWDkt_-9AB5sO2h3LJciEobcmLExk7XrCrERIzNA7uhAfemujqXZEiiEXhGrw5-3kWiwVD0Z3560kpvmRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71777" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71775">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=rfqMDEhI7OvznA4XP5FzbA3uvegcZPx3UkuCoa3skDzxUH8MUt5SbpLTqMJy9JrWVnOelLuJY0YHVQSvPFSgso8OoC_GSeFkU2G1q0PWKUouYBaDEGvxHYSxfOktv_bMalOWAPcNBTqhNIeNPZlFBDPCd2buXzYTLjniT1O-NyjZ9tZnJMlGAEiHpaw975q0Yz6uUksJPcejaTMb6WqJBwzGl73hkXZECH6fVSOxTP5W6VBiUlKh1kjx-cZv67YJgySZtfg1nDjHxDbJqEH90higObWaSlJe5JdGVcsmLq1dL5z2obxr1P0ky2JL01x-8JDAlz9thtyZPqq3KiN1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=rfqMDEhI7OvznA4XP5FzbA3uvegcZPx3UkuCoa3skDzxUH8MUt5SbpLTqMJy9JrWVnOelLuJY0YHVQSvPFSgso8OoC_GSeFkU2G1q0PWKUouYBaDEGvxHYSxfOktv_bMalOWAPcNBTqhNIeNPZlFBDPCd2buXzYTLjniT1O-NyjZ9tZnJMlGAEiHpaw975q0Yz6uUksJPcejaTMb6WqJBwzGl73hkXZECH6fVSOxTP5W6VBiUlKh1kjx-cZv67YJgySZtfg1nDjHxDbJqEH90higObWaSlJe5JdGVcsmLq1dL5z2obxr1P0ky2JL01x-8JDAlz9thtyZPqq3KiN1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تگزاس اونم وسط قم
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71775" target="_blank">📅 17:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71774">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=po88ecTCmfFYBTyQkBJ7CPZljYSPjGioknYTf9Q8LOkl58VGfIxlFzhxzBOviszJYM-SXrBl1EVPte2TqZR-XXK5FhWWmNV6sb2judaFfnEX_KPklPD3QUYrYg1oE838eL1PzjsMlKREpBGm5OJPSTrNyoG49ofrvPXR3rwY_17LxdAd37ryTSjfOgKX05KI8m8ok-r6GGEeceszIrl--BYkV0RUQuCBHiXJG585AS_rnKZkTZDx3WN-igVvE5wSu3_sU5GIuo0Jcv4K4HDHV7A0rRrB2WRBeA9wIVFJD0baOkS72We2mSXWpk_Pe-pomcYIpAvU4wYO6ny2NE_gYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=po88ecTCmfFYBTyQkBJ7CPZljYSPjGioknYTf9Q8LOkl58VGfIxlFzhxzBOviszJYM-SXrBl1EVPte2TqZR-XXK5FhWWmNV6sb2judaFfnEX_KPklPD3QUYrYg1oE838eL1PzjsMlKREpBGm5OJPSTrNyoG49ofrvPXR3rwY_17LxdAd37ryTSjfOgKX05KI8m8ok-r6GGEeceszIrl--BYkV0RUQuCBHiXJG585AS_rnKZkTZDx3WN-igVvE5wSu3_sU5GIuo0Jcv4K4HDHV7A0rRrB2WRBeA9wIVFJD0baOkS72We2mSXWpk_Pe-pomcYIpAvU4wYO6ny2NE_gYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
میل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ تنها تضعیف شده است.
تواناییِ عملی کردنِ این هدف، عملاً به‌شدت آسیب دیده است. ما به وظیفه خود عمل کرده‌ایم، اما هنوز کارهای ناتمامی باقی مانده است که آن‌ها را به سرانجام خواهیم رساند.
ما حماس را نابود خواهیم کرد. همچنین، پیش از هر چیز، رژیم ایران را شکست خواهیم داد. ما آن را سرنگون خواهیم کرد؛ این رژیم سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71774" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71773">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=jM8iszzvkv39uVR1EKXRQt69jsKXtmdimTgUTYxXpc_txlj3efs6hjK_EKxdwM_hofE60uMG7LAERR11xWJZlTIXSlV2M-NTa6wqhmAXQ0Nqam4WpkIUGZb78-V7XYbi0E8bglsMUuLsjdkRMkDQWOFkKYlBET9laMu-t2HNf9YX2ppCAVUfZYa7pYxcJ24wtCQMq39F7RPjSvqyNSiEaMj8hVmXUvTSMr_YfunxRZ2EJ9wS93UPdebFuwfA19-6sQGhwjZz3CgYmut94d8lmUSl2O6jeeP9U-w6XhZ_WWW3eC4vWicYKJyvIpKWpsK7LekEa4egk0ygPIgHIveLXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=jM8iszzvkv39uVR1EKXRQt69jsKXtmdimTgUTYxXpc_txlj3efs6hjK_EKxdwM_hofE60uMG7LAERR11xWJZlTIXSlV2M-NTa6wqhmAXQ0Nqam4WpkIUGZb78-V7XYbi0E8bglsMUuLsjdkRMkDQWOFkKYlBET9laMu-t2HNf9YX2ppCAVUfZYa7pYxcJ24wtCQMq39F7RPjSvqyNSiEaMj8hVmXUvTSMr_YfunxRZ2EJ9wS93UPdebFuwfA19-6sQGhwjZz3CgYmut94d8lmUSl2O6jeeP9U-w6XhZ_WWW3eC4vWicYKJyvIpKWpsK7LekEa4egk0ygPIgHIveLXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو یکی از خیابون های همدان یه مرد به یه دختر تعرض کرده، مردمم متوجه شدن لباس و‌شلوارشو از پاش درآوردن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71773" target="_blank">📅 16:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71772">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=Be30Td9hnIzTAlkGbUUQdQ__Stkv0t2_z4b_SkmZ5Sd2NBFjhISp0XCrRlsyxXKk_k_PmGdsk9gexqlcXSnHATTUhJODfid2-5jJIb1EBSK-dqKzcuKIXB5bXoXe2X0n2qaco_ZeD5z6ZeB3NAWcogouYSx7bkpGeMoBHDFsoY6npzYOqu71V68TAy7PoB4R6_8uEWpQhPH8vlWeQlFrBZQhhxj_agmD35n9dqglJhJ18y-aOc46kHqAB2AAt4R-3aSNTe_RDUDBmWYPmbTKHO-eHvkBi50DhNWirK_e57O2ates-DkNvw3fU6oUEv0TXdVK4vWgrHhsJ_u214PHGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=Be30Td9hnIzTAlkGbUUQdQ__Stkv0t2_z4b_SkmZ5Sd2NBFjhISp0XCrRlsyxXKk_k_PmGdsk9gexqlcXSnHATTUhJODfid2-5jJIb1EBSK-dqKzcuKIXB5bXoXe2X0n2qaco_ZeD5z6ZeB3NAWcogouYSx7bkpGeMoBHDFsoY6npzYOqu71V68TAy7PoB4R6_8uEWpQhPH8vlWeQlFrBZQhhxj_agmD35n9dqglJhJ18y-aOc46kHqAB2AAt4R-3aSNTe_RDUDBmWYPmbTKHO-eHvkBi50DhNWirK_e57O2ates-DkNvw3fU6oUEv0TXdVK4vWgrHhsJ_u214PHGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو سیدنی سویینی برای اولین بار تبلیغ عظیم خود در میدان تایمز را می‌بیند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71772" target="_blank">📅 16:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71771">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d6312725.mp4?token=e-W-HNbGqS9skzTWvdS_-RXTGRJq4jLf4WR0KaGRza2ZgvA37aQZnjiQhEbqTnMvERbIaqitTio8r-J2GVGtscqFy7SAZmvSaxJbC1SoNxyp0XY9Q3ODDGzdjP8cwgh10zt8-yB7AgAkftdIjRL72BEu994EeuS2UTgkGbQHFhAN-t_lBvk9NU_J_4M0bSRavWHmXBzz7oclg0ImMq2G0OztLXI6Gm4bzWoREGC7xQYSSvpfARDQ-CiVm36Zeb57zdnNbD02KVxgInfH3X7NT3oY5AfOjt1QT_OmeY7bIGD0wizrzVLtqKhrs_5R6oxVZTLg_sazo3q7aaX1a9ZSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d6312725.mp4?token=e-W-HNbGqS9skzTWvdS_-RXTGRJq4jLf4WR0KaGRza2ZgvA37aQZnjiQhEbqTnMvERbIaqitTio8r-J2GVGtscqFy7SAZmvSaxJbC1SoNxyp0XY9Q3ODDGzdjP8cwgh10zt8-yB7AgAkftdIjRL72BEu994EeuS2UTgkGbQHFhAN-t_lBvk9NU_J_4M0bSRavWHmXBzz7oclg0ImMq2G0OztLXI6Gm4bzWoREGC7xQYSSvpfARDQ-CiVm36Zeb57zdnNbD02KVxgInfH3X7NT3oY5AfOjt1QT_OmeY7bIGD0wizrzVLtqKhrs_5R6oxVZTLg_sazo3q7aaX1a9ZSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبرائیلی:
ایران ظرفیت گنجایش ۱ میلیارد نفر داره، میتونیم به هر فرد ۴۰۰ متر زمین بدیم تا به ایران احساس تعلق کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71771" target="_blank">📅 15:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71770">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=ez4tJ2gzSWrtvizDgm6Fek0Jc3NU6OtYm8McAvd13oXx6S1j0idHcKFAG_HlbhYj8kqDWlMjjb_5nvrohgBCUw6GT_PRVDm3vHcMM8oL2kuCjxMQnIwVzih2hZnMkhju5gFG4wScjahiR2dvpNU6p7mJ76bkJ2cJnuzINczmKGEvkY7uyXFylYCaNRp8nS8pvgT9PsG2FZPJ-r8DeBvTcdLEbqjCR5IKIrUVisHdtV35Uu4dqKA5e8eVYxkgpNhLchduDf459DeTGUwQhXzE5XwCkeyKErdfIW9YUwxAYa8WHrvXfJ-8bzO18z6A7IAJjucZjjAziI4UjJGFLq13rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=ez4tJ2gzSWrtvizDgm6Fek0Jc3NU6OtYm8McAvd13oXx6S1j0idHcKFAG_HlbhYj8kqDWlMjjb_5nvrohgBCUw6GT_PRVDm3vHcMM8oL2kuCjxMQnIwVzih2hZnMkhju5gFG4wScjahiR2dvpNU6p7mJ76bkJ2cJnuzINczmKGEvkY7uyXFylYCaNRp8nS8pvgT9PsG2FZPJ-r8DeBvTcdLEbqjCR5IKIrUVisHdtV35Uu4dqKA5e8eVYxkgpNhLchduDf459DeTGUwQhXzE5XwCkeyKErdfIW9YUwxAYa8WHrvXfJ-8bzO18z6A7IAJjucZjjAziI4UjJGFLq13rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این گربه به محض اینکه براش موزیک میذارن، شروع میکنه هد زدن :))
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71770" target="_blank">📅 15:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71769">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حال و هوای تهران در ایام تاجگذاری  شاهنشاه محمدرضا پهلوی، سال 1346 خورشیدی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71769" target="_blank">📅 14:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMArnhiL3obpzA8WfaS9ANveEb2KQpelbtdcSjqnUDAi9KoUpUTxm4RdYPPpakNk29-AeOeNxvVajGWURn_WvW7AEhjyIW-07W6b1fGdXfz3YjQjp2aqUBeo81rihi_HCEcf8_CfpwaY0atD8GzaGPjDPm-4qzwlm9Smkdhxn1roilIarOR4x_IIxOP1AIIo06QRBOigly8nwy-twCuhmCeR6Nku4NymxcBxmptEX3jFng6mdwgfHnoJEVNKmhbqSv9xUPzBwaVUpzXZFAh7nJ_-TViWIg7a18dEzVFSpUg9mqvI5Zc1LUKIVstXnQKGP7Dqnkly54nxHieVAUeY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ده فروند جنگنده اف-۱۶ ایالات متحده، به همراه چندین هواپیمای سوخت‌رسان، صبح امروز پایگاه هوایی «لاجس» در پرتغال را به مقصد منطقه عملیاتی فرماندهی مرکزی ایالات متحده در خاورمیانه ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71768" target="_blank">📅 13:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0a15Cb7HfDskf4tHZPXhz0OVTHphwVZBKRHSuE8e-_933pQCmpFFWZnysBfYVrN_YKhRUwl1nJbLAeYb0cWGG8Z7hgvuCVd50DKN-EWQTAzepfIT77KYpyXxkbryofbOA6k6OpLwtCcFRfEbvN7z3ExwtsmFT4R6U6gHo5oKHckcaqmrH4XBcyl05dXkG14kMdttt_HAnWo2fToVGVGgrXDmHpxuzQ2J4l6eETri8NgW04Ol_kZwErDr2bnUP49SKjqyfhCmMtS5Y4mddZWKwcjbkt9vy2OTSn6m8TgpAFQ86c4-tYQRjrNPPQ5N7-PBmHydlMERJTVs5lbJK8X0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک به اونایی که بالای یک میلیارد تو حسابشون پول دارن، کارت سفید میده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71767" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71763">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKNFXQD22cKhoEG-WYi84hKg0RhVjcghh5VI3QRhEGA3E0OTIyHIAbu2N_AFHpB8bE5pU65qsFxQahcmtZqV5oqvzF5qC3S_A5ytACddmpfMXQ1EYdSq2jpDfftBEdMTJz4fk-EkH226grJvKgmL_zdxosGg0igGkCpuaRs0r8FnjrSrM_JLF9ZYOf_O67Fgaia-Ui971Z5jFhn_Gu0ae6PEaureEI9taCzgldJI8FzFjusxNyBgFdbPFn8jQzQxCJ_0kULykyMc0NImsLyhko5o2jfWA2X0srVaCdvANExky7PjSEXY8kj2ZmC4zzmLGUh4pTNTXScQE3dm3nBMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6wrSEmVWq9ckxF5edkQ-IYDvK7OmqwfXToANRUtuUCL1FwgbkTs7FKQuG92SQrttFhDzQD0OsVIZO990doWXurxKVu_1zkC1NTJIizJTD9bxbfURjQJ8iONDqsbYU7zXshgW56_gNSNV9VDA8zUpTBySWz6mGsc6MNhUKmV5ZfsIKTkSYd8uY5e7qPemHmKcoWp1QlWJAUhjNJLw8547E98wdnxyAmiScRm3bdmvE7xFgD7I7LHtnG9GTGTDHXLBxw-qKt-P_6MNKZiAgzStH7YHAxF0GFbFWBNLZ9hBKGk-lxZ-_9fgPVuzt7esBSYip3VuLPnbmIS79zi4gYnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBvMert7ND8fhHPgspDJhg0tWz9TEBIGOx72qW92iKHmHxB8Q2yX6PJ2SnGU3EG1BECk06CHvBoSsBEDOxvGDA0kKv2AgabGzc3NR8qJSDqfXJPD7V-cmd0q1iAhZWlY-TIwCKK_o6Cl1PZRLaDfYvy3ZlCnxnd4nBFGI1DI9m_YXK4yd-cW3TQONH6E5k764r0Yp5nclcDmkPDAzwfyBFWgYgdKryhpWOi_7E9UQkWeqnqyvwKN0sjeEG1B37vR1XqxKQzB1p4xZhYZLUbzMs4sYgHbsZ_PF-1PpSCXQ-gDZ1ieeLjvn8LfE_HIXo43PSZOlVinUggnaDO8Ac5ZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMrMwK1ROC_79riddj9VfghCbdXLzOCMULMg7p17KidE6QlIczffGGcHrEL7WSp6KyfgodPSEYcSc_x4gSQA8VS05Nkxfrfg6954HdCshJRZE1NTMfxtR0FpHr5x78P3t0IWdL4Mx2aYsSyVSOwSZmo3CILQr7A1EqKHJ_n8xLpQJ1MNFvBYautiooJXf6eY2DNrKAHsTyIy-NOKBCtugcqDwEkcarjsEgNK0zFiR3VaYtuB6H3l5vJxc8h3saheIyhnDF5PlwmS2AM89UJyihVi1NSCXRf8gUBVpB3vEJy1uovv5aCyQO89F6GSqTGPEATMLDP0CXiHvfhMtgi68Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز ۲۶ شهریور،تولد کمبوجیه پسر کوروش بزرگ و روز پسره.
26شهریور؛ زادروز کمبوجیه دوم، پادشاه هخامنشی
کمبوجیه دوم، فرزند کوروش بزرگ و دومین پادشاه شاهنشاهی هخامنشی بود.
کمبوجیه پس از پدرش به پادشاهی رسید و راه گسترش قلمرو هخامنشی را ادامه داد.
مهم‌ترین دستاورد نظامی او، فتح مصر در سال ۵۲۵ پیش از میلاد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71763" target="_blank">📅 11:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71761">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNnP-0AlN55vdKQfinAhKfsGx-WGfNBHQHWeAUGRFNbbvh3H5i_Lrcn7nQXMA1EHlYQ1nE8eg__GeZJmANpQYZeVTbLeznhCncf7wVLT20c_eMIrX4prWGGM0ef5vBtAWY2W3vh0Xy_slP4AvfI146ck_hZlhOixjM3uHSWLBvSehLErDpA7NAFj_AnCIuKkW8tKDDeNaTr4ydwlmiefG8l5ckgKHjGBd7KDp7mIzO0TeK9pNnPv2MLDx3fcZaO_qia-yCaF4PnSTCJXr1G9LyZdyv36DA5JPlnpcQV-IgEHJNNlHY5ntEUxucFt5eqSVevy1QB7zHlg0PhY2Z5bEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=MSU-2qu0HljiIXKguGYCRidGLJis7xyUvwjfP2RhocKFCdDMSoxHqGHqMy4_3ygUsvwC3HUrCjBaokVkTdOd0eZj3UHmCAmGCoEoteSCUCls39fIr4q5ndaiYMYyNCC0vTY3-rWf7Kt7TDoviGxvs1OHBIFSgdrJNyNyDkClrx7PXNIU0ImLMoX1Q5KzoBPZg9TxAwyQCGp4VU1DkhMd_KzY9FKvdRJaypDGok4YgB8W2AE09p5gig4_G2zBbZiS0Dv4BBsSrVjPDXNpYd393CciEG0t4la5vHrv4Dk9BY0Ow5o_EycLkImCsPRPV9A717BIrN2Wojn3GtUAuN3Ptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=MSU-2qu0HljiIXKguGYCRidGLJis7xyUvwjfP2RhocKFCdDMSoxHqGHqMy4_3ygUsvwC3HUrCjBaokVkTdOd0eZj3UHmCAmGCoEoteSCUCls39fIr4q5ndaiYMYyNCC0vTY3-rWf7Kt7TDoviGxvs1OHBIFSgdrJNyNyDkClrx7PXNIU0ImLMoX1Q5KzoBPZg9TxAwyQCGp4VU1DkhMd_KzY9FKvdRJaypDGok4YgB8W2AE09p5gig4_G2zBbZiS0Dv4BBsSrVjPDXNpYd393CciEG0t4la5vHrv4Dk9BY0Ow5o_EycLkImCsPRPV9A717BIrN2Wojn3GtUAuN3Ptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اوکراینی شبانه به یک پایگاه هوایی نظامی در منطقه روستوف حمله کردند که منجر به وقوع انفجار و آتش‌سوزی شد.
حملات پهپادی همچنین پالایشگاه نفت یاروسلاول را هدف قرار داد و باعث آتش‌سوزی در محوطه صنعتی آن شد.
این پالایشگاه یکی از بزرگ‌ترین پالایشگاه‌های روسیه است و ظرفیت فرآوری بیش از ۱۵ میلیون تن نفت خام در سال را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71761" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71760" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71759">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvwG-Mkqwz4lZ3pMsUfv86oC-tChLm5t3VRZId64GZ9VnAS3YFmucG1tdwXjjUdMNBPXaPXMInrtvK4QZxerRdf5Sg5XkQnijmWW3_crOCI32_j7fRRxl9qBjhsGCAMN5_5XMhw4Sjjfh4Tit8IwaFuwIv4ZYVHVtpRpW9wuZZWAMbi7ItsKVEagckOV3SN19IuZrI19PVkbDChEPg_jZ82cC-4d9NGVT5VJb-vuO60su0zWV6CTwWIaaxzeT85qRwN-pnbW_rggn3uqOYis6A0JXHaFElxj01zQYwSisYolN8dJ_twxJc-5its3_AF_0RZE_F8OmY-6fAzDGRvEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71759" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71758">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=UQjRmU9X08Q30VYX1U1gL3Mx4BFhw8QO1H8SBIqAylPxEAVIXdI4pcyvL6HtlBlQNhtZNkLnduTb4LvuRIJ9ZkH0NJJL7I2siGIAXDxXKdvrgkfCPyLinBDyvRDFucB2U3kiZcFMnMhFeZ09CqUwdelsKWoyl4rUUHy4qGgLXgUNEmbeXJTfCbuEK0oPRO25mUq0QCH1uzX_dR6NqvmCVSMqAKHCytikjx5oKIwXeIe-c4buT4iEwiti_BR_0DfNPPwwlO9w-FcE31-FFydwZ6ZgxnAFT9LvcppFkDQRqXkbKeRKf1wSaXbaAuss7L77n_9PCYy_RYV4Q2UxGQdLzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=UQjRmU9X08Q30VYX1U1gL3Mx4BFhw8QO1H8SBIqAylPxEAVIXdI4pcyvL6HtlBlQNhtZNkLnduTb4LvuRIJ9ZkH0NJJL7I2siGIAXDxXKdvrgkfCPyLinBDyvRDFucB2U3kiZcFMnMhFeZ09CqUwdelsKWoyl4rUUHy4qGgLXgUNEmbeXJTfCbuEK0oPRO25mUq0QCH1uzX_dR6NqvmCVSMqAKHCytikjx5oKIwXeIe-c4buT4iEwiti_BR_0DfNPPwwlO9w-FcE31-FFydwZ6ZgxnAFT9LvcppFkDQRqXkbKeRKf1wSaXbaAuss7L77n_9PCYy_RYV4Q2UxGQdLzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی یک تک‌تیرانداز در رقابت‌های ایرسافت!
خوبه که این یارو تفنگ واقعی دستش نیست!
همه رو هدشات کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71758" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71757">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=gFFx0OM07oZqe2z1oD_9fD3ERz-qLVKTV9uYLARBESFlI0sF0HuW2tw6Bkm6PLWzShhB69deYBOQIBzjDIJeYKn1gLVURekZ6MtIZDBQeHV9MrFmwC6rA4U_7UZNPeAqVCeAhTdPEYo5RaD0xPj67pf1fmDR541Ltp0m4VYWrwUzUm7qro_A1hqb64EjboPP0kXJ5WAZao_UkRlqgIukUeC3QMX4suhEbswbEjpW6cVEW7WcC_02kTZyA1aAKhwBJWrRYZxSggJyS9RJBTjWh8ohoDc8T_ZVf7Hp_Rq8Rp2zp2c2DoGwZZmOVE1MpC_l5lsLaDrvK3wMgwR1l4xJbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=gFFx0OM07oZqe2z1oD_9fD3ERz-qLVKTV9uYLARBESFlI0sF0HuW2tw6Bkm6PLWzShhB69deYBOQIBzjDIJeYKn1gLVURekZ6MtIZDBQeHV9MrFmwC6rA4U_7UZNPeAqVCeAhTdPEYo5RaD0xPj67pf1fmDR541Ltp0m4VYWrwUzUm7qro_A1hqb64EjboPP0kXJ5WAZao_UkRlqgIukUeC3QMX4suhEbswbEjpW6cVEW7WcC_02kTZyA1aAKhwBJWrRYZxSggJyS9RJBTjWh8ohoDc8T_ZVf7Hp_Rq8Rp2zp2c2DoGwZZmOVE1MpC_l5lsLaDrvK3wMgwR1l4xJbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات سالم در تیمارستان یمن
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71757" target="_blank">📅 11:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71756">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=RBT2UU8E9IDoqtgILFbHme62YH2uDf_zNQ_vdCtunUjvtpYJee8fifUrC_pdmE7YLEr1yKFSSlypcaQade4Q4SenJN_n1bGJQStg6vvG6eL8Oz7BbjdeVgqlMMrYw84-7cXIa210Tb9VjCbJKVpffBETOoYh1DPGcUUIhuI7-Mf6oEotOTHeXwN7k8c04x9GaUoK7AI8VHU0X-p-Huqnklyr3NrcStHaeLMFYN8vSgl62y-o4BavfBaJhM5xSHx3BxNajIRhrY-kvETGreVmgeHDhtZuvWcv9HusxIJZooTcQSKcOYGcBpBobNrnR0JRwEUm5gLbBKjdW5ODrtHP_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=RBT2UU8E9IDoqtgILFbHme62YH2uDf_zNQ_vdCtunUjvtpYJee8fifUrC_pdmE7YLEr1yKFSSlypcaQade4Q4SenJN_n1bGJQStg6vvG6eL8Oz7BbjdeVgqlMMrYw84-7cXIa210Tb9VjCbJKVpffBETOoYh1DPGcUUIhuI7-Mf6oEotOTHeXwN7k8c04x9GaUoK7AI8VHU0X-p-Huqnklyr3NrcStHaeLMFYN8vSgl62y-o4BavfBaJhM5xSHx3BxNajIRhrY-kvETGreVmgeHDhtZuvWcv9HusxIJZooTcQSKcOYGcBpBobNrnR0JRwEUm5gLbBKjdW5ODrtHP_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
قیمت بنزین برای شما بالاتر رفته است؛ اما این بهایی بسیار ناچیز در قبال کاری است که ما انجام داده‌ایم. این را به خاطر داشته باشید.
ایران نمی‌تواند به این وضعیت ادامه دهد. کشورشان ویران شده است.
ببینید چه اتفاقی برای ایران خواهد افتاد. نتیجه‌ای واقعاً خوب در کار خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71756" target="_blank">📅 10:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اکسیوس:
انتظار می‌رود ترامپ هفته آینده در حاشیه مجمع عمومی سازمان ملل در نیویورک با رهبران کشورهای حوزه خلیج فارس دیدار و درباره جنگ با ایران و برنامه‌های مربوط به دوران پس از آن گفتگو کند.
پیش‌بینی می‌شود که در این نشست مقاماتی از عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان حضور داشته باشند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71755" target="_blank">📅 10:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71753">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDZ21w6H7xFUzpp12IedqzAQaF_p3sAPP9-VrpqZL_I1t5X2ib8xACXLOclXl05POGNUedyqhvrslzzx_JlSNZ9ahCtKEvI7AhN1RiBbk2S-pbM63UsFGk0Yeo1rQ-guVI68emE8rX80kfr8hLibQ0lYTgHXH-u1UPjRdxgyHG7OXNrLBEvRu5wRf3Py7DmS3bZVBLdyrvc-mqDPWeZiE1uwzz8WaMMOIbhL8pUZJ9g5Mg6KSISz3pQe9Wqy3I-E6QomXFyiKF3145l89AtZBqZakj0CHiS0X7ydzC1Oc--2iIVb5WgcdGB0nOItVbZVwqwoylLAr81GOVNAGTZBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cba858231.mp4?token=q2lPQQ6JwP9wQGKZqESk-G2fBjnTyAgW0WpwFebXbGM6tCOQF1TOXr_ru01VlqXYm2lbygPZLUak0lrgBaWvZzf_N_RAGx5xSEVoQpgAf46smEEj5Zyi_vhRI0eAThFLJ9YG0MupQxWwGWo41KbMTVBiZxAEC5c4EpytOTFqAk7sExm_zaAc_KjoaOquO5Tn0IQC4TBrLECm85MgA2AU_QjlR49YvKy6L6mFoUV2AdDrwf9r-r5P5K4RNeox4E45tHJYXoWHQfukFMulC97MQepOyrT2IogXHu2XCPerbvf-pfSlYIrbW-gyXJplCpmLgnx3990C8eHVjwGK8PtcgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cba858231.mp4?token=q2lPQQ6JwP9wQGKZqESk-G2fBjnTyAgW0WpwFebXbGM6tCOQF1TOXr_ru01VlqXYm2lbygPZLUak0lrgBaWvZzf_N_RAGx5xSEVoQpgAf46smEEj5Zyi_vhRI0eAThFLJ9YG0MupQxWwGWo41KbMTVBiZxAEC5c4EpytOTFqAk7sExm_zaAc_KjoaOquO5Tn0IQC4TBrLECm85MgA2AU_QjlR49YvKy6L6mFoUV2AdDrwf9r-r5P5K4RNeox4E45tHJYXoWHQfukFMulC97MQepOyrT2IogXHu2XCPerbvf-pfSlYIrbW-gyXJplCpmLgnx3990C8eHVjwGK8PtcgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">« امیر نوری » بازیگر؛ چند روز قبل یه مصاحبه کرد گفت خیلی پولدارم و فقط میخورم و میخوابم و از زندگی لذت میبرم. حالا دو روز قبل چنان تصادفی کرده که با سطح هوشیاری پایین باید سریعا جراحی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71753" target="_blank">📅 10:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71752">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rje9IXPEaF4cGOvPEyiaXyCtwE-tgBmwwuliJBHVOpIAwAWd1dB0ufUXguwmTnCn0nop3ed2Z_Tiix9BKt6UnAQwCDsdOuJsmbk0TUVP0ykVr93r9SiJ5RTJjsBVJwKbc_tm0idfEc7kgiKbaONGa8P2FiNA_Qzu-lGRI97HdHSIxEp59D9Wh2owsqGBfGTiKTUEEVl_xxQ8aS3aXfWUiHwKi0WiTBzSMEO8-lCP6mlgdgZld8Wle13uQG7DVlgWbjTgUFHhP1zvrLPEgdBTExD33SXxuw1XCp0JMPQNUMhUbaH4IUG0P7Va5iOvFhJ85AAeIl9aoDlfzlz5hfD6ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا بعد رزمایش جانفدا ها توی شهرری عقب نشینی رسمی خود رو از خاورمیانه اعلام کرد
اونی که اسلحه اسنایپر رو برعکس گرفته فقط
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71752" target="_blank">📅 09:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71751">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=ZH-CYNqx7To4FiCaCsoqnMHn2EmWGaOq9SP_s5As8eb6RCtCzF_9tSytnPnJh_eMZQf4lwtwe9e0Jox5rU7LUCz_ujuinn-g02CA_WYjhCPhqR3ofFOhJfaIgswtSIiYbS4JICMWk1byypCiMYapP72AtJ1VbwPK7OteymJl7aO9_5AR_CuCfBU2lj2-IsYgWEFDXTPWrSrUjo-21RV-dnubf6wlqSmgmah5l7p5ilOrjm7O-nqdJpnqskLfVaRxFELRGJ_n3Pmc4VU9n40lmK0dn8-k8ZwKrX-JLuwwfK5koO7L3Ik88sWlq87FmV-g5QuPKeNccW2P-Nz0uq956w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=ZH-CYNqx7To4FiCaCsoqnMHn2EmWGaOq9SP_s5As8eb6RCtCzF_9tSytnPnJh_eMZQf4lwtwe9e0Jox5rU7LUCz_ujuinn-g02CA_WYjhCPhqR3ofFOhJfaIgswtSIiYbS4JICMWk1byypCiMYapP72AtJ1VbwPK7OteymJl7aO9_5AR_CuCfBU2lj2-IsYgWEFDXTPWrSrUjo-21RV-dnubf6wlqSmgmah5l7p5ilOrjm7O-nqdJpnqskLfVaRxFELRGJ_n3Pmc4VU9n40lmK0dn8-k8ZwKrX-JLuwwfK5koO7L3Ik88sWlq87FmV-g5QuPKeNccW2P-Nz0uq956w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در میان مردم اسرائیل با استقبالی باشکوه
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71751" target="_blank">📅 09:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71750">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=WtiCd6ufaEWJWILXTNGUEL3AU7yg3KGgRtBvftbuOo_K7EnIBjoUL1UneQnxJObudObgmsTkvjDGS5eErLJ7yU6yTha8eQllk9pk23rAxNEfbVQWrzk6EgsqGnmNSBdM_hBX4sLWKj19qFtvm3OhQMPIiis2AszC8nF3c6QXwT2ntwyDMixDZ83kgtSK12AIM_kYIeOhDtqTPca3s-aXA1CEnuKGEnKqRvrkF9PnWirnhV7V_S6ER_VKiaA0x_K7yMfOLr_bcpPUizWdO-ubCuXGaUAq72gtGOAUur8GABdam42QGsuiL0RyhzBT9eWNjXOjMfJ8RQTQlDZs-Jg5fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=WtiCd6ufaEWJWILXTNGUEL3AU7yg3KGgRtBvftbuOo_K7EnIBjoUL1UneQnxJObudObgmsTkvjDGS5eErLJ7yU6yTha8eQllk9pk23rAxNEfbVQWrzk6EgsqGnmNSBdM_hBX4sLWKj19qFtvm3OhQMPIiis2AszC8nF3c6QXwT2ntwyDMixDZ83kgtSK12AIM_kYIeOhDtqTPca3s-aXA1CEnuKGEnKqRvrkF9PnWirnhV7V_S6ER_VKiaA0x_K7yMfOLr_bcpPUizWdO-ubCuXGaUAq72gtGOAUur8GABdam42QGsuiL0RyhzBT9eWNjXOjMfJ8RQTQlDZs-Jg5fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا قبول دارید که آن‌ها به خاطر جنگ در ایران، نرخ‌ها را بالا می‌برند تا قیمت‌ها را پایین بیاورند؟
ترامپ: نه، آن‌ها نرخ‌ها را بالا می‌برند تا عملکرد ترامپ تا حد ممکن بد به نظر برسد. مشکل آن‌ها این است که ما بهترین اقتصاد تاریخ را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71750" target="_blank">📅 07:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71749">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=V39jcnictk727ur2S3717ULFvkIuDYXDnW3MiPAv3cyX7DBSHC2SEXF73Xre2KrLZI3tvDlg-1waX2eRRjs2olz3cqu5gbwNy6FMIoHjJ8vjES-INz40U36QIWML9HwR46XGEfLXxQBHQQRjZCQzO0wVrjP4MhmI_8XFXe3BOxdeb3x1px7Um7pXB4Oj5J1gbBlKWdmiWYC5Ix89iDovsEfpwhY5KCSQmjXTu8OETTFD4kWRVF6-Un6WoNiX3visM4cLV53983ruB1fk1-2642w2jdTidz1TofHmi1-yYGQicthc8d9_S4HbMvRvaPXn6gMpKsnSZ7C8xlg-ecK1Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=V39jcnictk727ur2S3717ULFvkIuDYXDnW3MiPAv3cyX7DBSHC2SEXF73Xre2KrLZI3tvDlg-1waX2eRRjs2olz3cqu5gbwNy6FMIoHjJ8vjES-INz40U36QIWML9HwR46XGEfLXxQBHQQRjZCQzO0wVrjP4MhmI_8XFXe3BOxdeb3x1px7Um7pXB4Oj5J1gbBlKWdmiWYC5Ix89iDovsEfpwhY5KCSQmjXTu8OETTFD4kWRVF6-Un6WoNiX3visM4cLV53983ruB1fk1-2642w2jdTidz1TofHmi1-yYGQicthc8d9_S4HbMvRvaPXn6gMpKsnSZ7C8xlg-ecK1Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدواریم که به پایان ماجرای جنگ با ایران نزدیک شده باشیم. ایران خواهان دستیابی به توافق است.
خبرنگار: آیا مستقیماً از آن‌ها خبری دریافت کرده‌اید؟
ترامپ: بله.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71749" target="_blank">📅 07:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71748">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71748" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71747">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZImqqSA5B6eJPFzfwj563QbAZJZDY7Oe1GTAzNCT7nmbD1Q0MlmAmeuxAUXkWaOWDU23rxyCJkGpQ7jjDkYQW6hZVXu5RYbv0Ze4FS1PIV5ZpCUmwAnRDA0iomVnHULauhRtWi-D7qM348apIaCkuJztILtUKhXzM6zxGL8h2QU3ebnwPzV9Q---q2j2LzteZARYJeL-aqOv__VwKFqW7FlyaB1nAUD49gN3fSqmzClmkpVOCEpO1E1c3ceK4wMZXhq72Pz1mJuq2RjeYnnUyUob8KBj1uT2t4A6TK5GNDnsr3melbRNeHMMSGJhxX6uzuJkqllKrQu_pQ19XW7Dlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71747" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71746">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=OlPPyH1fAaK0GYgJ3kIeCdh7InqcfchwpSBOstmxoACLhbvRiVe6i4CnoJek5kRLhZV1KSKnHHyXZR7eHha76OQrdlNkudo3aWetXhtaePpWy22PzMwTpY6Spk3l0pOdWiMJd119X5GbWeZLC-rxLvsgsN3_7kaDUhueTWXKQyHv5Gir5YLEFy3JUe4a2NkiTeZ55_MzWGlY4A-50TsBSrEZHR4bYOmG2kRTqQYaWFuhC3ANz7MlxY-JNEjFLxJxqjcEChb9CBvlk7q9Ta3mrG6LQsS8kx7enEoQmHLyr7xmOmlG0KzTN_RtBWCA582Czd3mGcOTYcD_DEY5yBbIdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=OlPPyH1fAaK0GYgJ3kIeCdh7InqcfchwpSBOstmxoACLhbvRiVe6i4CnoJek5kRLhZV1KSKnHHyXZR7eHha76OQrdlNkudo3aWetXhtaePpWy22PzMwTpY6Spk3l0pOdWiMJd119X5GbWeZLC-rxLvsgsN3_7kaDUhueTWXKQyHv5Gir5YLEFy3JUe4a2NkiTeZ55_MzWGlY4A-50TsBSrEZHR4bYOmG2kRTqQYaWFuhC3ANz7MlxY-JNEjFLxJxqjcEChb9CBvlk7q9Ta3mrG6LQsS8kx7enEoQmHLyr7xmOmlG0KzTN_RtBWCA582Czd3mGcOTYcD_DEY5yBbIdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواضع حوثی‌ها و تجهیزات نظامی آنها بار دیگر در مناطق خط مقدم شمالی استان تعز و اطراف المخا هدف حملات قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71746" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71745">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=V-6N95f_9w8XrSH9saVM1USm87ewYSiLIQHsqG2RIX4HFo1S0xChF1PR3JoMNODXfNSMOJ79f19XqhF4l5Np4V-pKEhlRvbmImwgm_yTv4ZJN5hWl83OJb-vbzvNroRRi9oNYvw3Mn1xiPDsOIWdS0B7Nr-hqq5_jI4Ja_zq2G2HzHzSHyUMtOjDKHkxWZwQenhL7r4EJt4Cn-NZVAdMeC0KnkMGql12BoihUmVRodkl7fPwJ2sPDfoiGWEBXNQPA0b-CLSzyn_qr7-2nIvCAGlLrqYls4qz9mFA7QOBDESdAIicYoseGzKamU_mJ8uekUjmxG0tn8MFg8_EJD6Q9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=V-6N95f_9w8XrSH9saVM1USm87ewYSiLIQHsqG2RIX4HFo1S0xChF1PR3JoMNODXfNSMOJ79f19XqhF4l5Np4V-pKEhlRvbmImwgm_yTv4ZJN5hWl83OJb-vbzvNroRRi9oNYvw3Mn1xiPDsOIWdS0B7Nr-hqq5_jI4Ja_zq2G2HzHzSHyUMtOjDKHkxWZwQenhL7r4EJt4Cn-NZVAdMeC0KnkMGql12BoihUmVRodkl7fPwJ2sPDfoiGWEBXNQPA0b-CLSzyn_qr7-2nIvCAGlLrqYls4qz9mFA7QOBDESdAIicYoseGzKamU_mJ8uekUjmxG0tn8MFg8_EJD6Q9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر از همه شانسش یک‌جا  استفاده کرد...
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71745" target="_blank">📅 23:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71744">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=Zn-n5VwORMe34_FKHdAgIfJ8aWauaj8jt7rPonzdPyvSJxgWLJs28KwTKr5qSUyNWAem1AR4ITnFs5wEQspG14Oc0Hc2laJ5197pAMV0N8q_K6Grv5FTg6eigoG9WKxalYHfv1Dy2yZxgKnZwZvDefZzaFmvfbp8MXK89GwvO3NU4B0fdbA2VzJDPtzcY58FxcQQNEMlvB8u2DxIJfg_cI5cmQBy55hRRO2zo1cOw_e71b2CZI3IfAb29h2Iq0o3XgGT80o2VMTzE_nFrKyXr5Q5ZB7IzpErNZHutmBHWa74JqxPAN4XW9dwlvLgHmrfk54-NypIW7kQtWjGN-OSnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=Zn-n5VwORMe34_FKHdAgIfJ8aWauaj8jt7rPonzdPyvSJxgWLJs28KwTKr5qSUyNWAem1AR4ITnFs5wEQspG14Oc0Hc2laJ5197pAMV0N8q_K6Grv5FTg6eigoG9WKxalYHfv1Dy2yZxgKnZwZvDefZzaFmvfbp8MXK89GwvO3NU4B0fdbA2VzJDPtzcY58FxcQQNEMlvB8u2DxIJfg_cI5cmQBy55hRRO2zo1cOw_e71b2CZI3IfAb29h2Iq0o3XgGT80o2VMTzE_nFrKyXr5Q5ZB7IzpErNZHutmBHWa74JqxPAN4XW9dwlvLgHmrfk54-NypIW7kQtWjGN-OSnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نکته‌ای جالب درباره جنگنده سعودی که در مأرب یمن سرنگون شد:
شماره سریال (5529) روی دم هواپیما قابل مشاهده است که تأیید می‌کند این پرنده، مدل بسیار پیشرفته F-15SA ساخت آمریکا با ارزشی بیش از ۱۱۰ میلیون دلار است.
این هواپیما دو‌سرنشینه است؛ بدین معنا که شمار پرسنل اسیر یا کشته‌شده شامل دو خلبان می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71744" target="_blank">📅 23:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71743">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=jmrkJ7F-3FGiQi0bZ6p3KWOuAO1LzEm95BrCGtoxiXi0DvRFKFvHe0rKDLUUui509fTOs4J_Lq6Hib1X8AwuQO9tIO3pxjQ6UuK48_6l5fi8dxuBl48AFKGYaFhzzgez7PSQ1Ygqi6zRCLxr7TnvauNZ9S3qlDOizhObmGMvgvFUmSv9uke2jvB8bRjChMl_LfNqZguQeznil_tOiLfunMokOsK9nCv7yVa8NGn7-9khYMjTrRsbif7Q0OQrCkF81nnnPuCuQwGwVKNgxEBHLxPIB7c3Tan2mB__hWaVZBIHjHRfJjBVuPnQDqHur0Pogf_W4plGLbLFysJ89yzT6pqe2bAYRoeBviHY8MVMFT2Yy271pOXtaFF2XNvuGT0mjoBJSJmzOBIHu6RIYTozQITeFgYw-Ea7qh2LbDKjjHy5dDJcx4c_gJkUGtYtX2qmbaerLOlNflZRIHiyz4khs1KkrwgzDc_mK7VNpwQVqApV6sUB03kBWl9RQrQ-UgqYcIGIbff69G1I63yc_GJytpnRC4VLBJiHojYWYs_ppb7SP7ENVXQ4xw8NnXmi9Q6LYL7OFjwMbVNmNAhXtNj7wp9wT7v4mD8Z5SQXhcPX0qyRROk3vFAxbb7Il3UaZnA3-b74HBp7VNaXUAZlelbdbePJloOiiRbnB2_fDAGDUG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=jmrkJ7F-3FGiQi0bZ6p3KWOuAO1LzEm95BrCGtoxiXi0DvRFKFvHe0rKDLUUui509fTOs4J_Lq6Hib1X8AwuQO9tIO3pxjQ6UuK48_6l5fi8dxuBl48AFKGYaFhzzgez7PSQ1Ygqi6zRCLxr7TnvauNZ9S3qlDOizhObmGMvgvFUmSv9uke2jvB8bRjChMl_LfNqZguQeznil_tOiLfunMokOsK9nCv7yVa8NGn7-9khYMjTrRsbif7Q0OQrCkF81nnnPuCuQwGwVKNgxEBHLxPIB7c3Tan2mB__hWaVZBIHjHRfJjBVuPnQDqHur0Pogf_W4plGLbLFysJ89yzT6pqe2bAYRoeBviHY8MVMFT2Yy271pOXtaFF2XNvuGT0mjoBJSJmzOBIHu6RIYTozQITeFgYw-Ea7qh2LbDKjjHy5dDJcx4c_gJkUGtYtX2qmbaerLOlNflZRIHiyz4khs1KkrwgzDc_mK7VNpwQVqApV6sUB03kBWl9RQrQ-UgqYcIGIbff69G1I63yc_GJytpnRC4VLBJiHojYWYs_ppb7SP7ENVXQ4xw8NnXmi9Q6LYL7OFjwMbVNmNAhXtNj7wp9wT7v4mD8Z5SQXhcPX0qyRROk3vFAxbb7Il3UaZnA3-b74HBp7VNaXUAZlelbdbePJloOiiRbnB2_fDAGDUG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبرنگار فاکس‌نیوز از روی عرشه ناو هواپیمابر جورج واشنگتن؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71743" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71742">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مجری از خلبان آمریکایی میپرسه چی بهت کمک کرد با اون وضعیت از کوه بالابری؟
میگه هیچوقت اجازه نده کمبود انگیزه باعث بشه از تلویزیون جمهوری اسلامی سر دراری:))
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71742" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71741">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=i0wyGeZab6Yuu7dCE_NUiqgGzo9lFKEFW44rTRaY8DNd-YwSEHddGGRGIlXwaw5QWGbd36jlTZccHRCnwexK0L5XgRtlVM68BOuOPRXsXv8VpFkhnnH6i8N0zYpvYpB0A_ZjFJuIxuAijavNDVyNDO8a5QNX0d8BaKx9JzplbNizvcKKiKse1ksLMxfW658lcr0bdBXEXmED7ziMCiMKEWsvtp3WBoYbmr03XOJbia10JPgrwEytswftcUQ-2zZJOav1yxmqEZZtFazpg7JDbTgy0apiqnfMBeyeC2FoxYdV48jpk2-Dq-wK4fhvVPXk_SCTNEC4n_DCMAfH6Kc6ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=i0wyGeZab6Yuu7dCE_NUiqgGzo9lFKEFW44rTRaY8DNd-YwSEHddGGRGIlXwaw5QWGbd36jlTZccHRCnwexK0L5XgRtlVM68BOuOPRXsXv8VpFkhnnH6i8N0zYpvYpB0A_ZjFJuIxuAijavNDVyNDO8a5QNX0d8BaKx9JzplbNizvcKKiKse1ksLMxfW658lcr0bdBXEXmED7ziMCiMKEWsvtp3WBoYbmr03XOJbia10JPgrwEytswftcUQ-2zZJOav1yxmqEZZtFazpg7JDbTgy0apiqnfMBeyeC2FoxYdV48jpk2-Dq-wK4fhvVPXk_SCTNEC4n_DCMAfH6Kc6ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاله مرزبان بعد از دریافت جایزه بهترین بازیگر زن در جشنواره ونیز، جایزه‌ش رو به زنان ایران تقدیم کرد و گفت :
میدونیم که سخت ترین دوران زندگیمونو تجربه میکنیم ولی نباید ناامید بشیم
یه روز امیدوارم رویای مردممون برای آزادی و آینده بهتر به حقیقت برسه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71741" target="_blank">📅 20:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71740">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BasBqFI_QnEcVzrU868HTmd0eZd5jATRj_3jU5GyRG_O1npYhLT9_5ZOb5ID1tcAV-6W7NKlUbj9CisZyTn52aC_FcTBnkOM1jjfRgTAjWAl1rHeW1eHR7n0evOwH8t7F2A-89Dw2YF9Nxwwg4VLAk3V4WjOxfMKSuk2T-DaGTCfeUrCearDe1vUZew-pmf5-FgNXGeN4HWtqZvWx4Wf-sSpN6TwSxI5Wr-rDNQIG5XqwhIl0ldCSGn7DMNfwmUr93GNFFAn_xQYebPJut_sqyxvQTVoVd18wle0aTVTLJQ0sHZS4icWOSHYgxycGvjr0aFbHf556BS6kFNUe1D23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت گسترده ترابری نیروی هوایی آمریکا و جابه‌جایی مهمات میان پایگاه‌های این کشور در اروپا و خاورمیانه امروز!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71740" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71739">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزارت نیرو از پایان قطعی‌های برق خبر داد؛
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو:
خاموشی‌ها از هفته گذشته به پایان رسید، امسال ۱۴ درصد برق بیشتری به صنایع انرژی‌بر کشور اختصاص داده شد!
بیناموسا میگن دیگه خاموشی نداریم اما هرروز داره برق میره
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71739" target="_blank">📅 19:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71738">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3IEF0yi5HYQGGQK3fQF6qbvu6N0Rtx3MTZk8lO3dyxYGN2jXdsAfxqx1SKj9froShTeP8TRMZJH37UQIvaWhep5JJbhNKposqUszto-WQLTMtukz0I6C8KR7vCtTSX9EC3dyhChv9QXoAmpJRzAUmeTYJN1ptl3c28HhJTWwBvjybGdG0bIWszATKoKqGkG7AV5wCKv2oeImVMpiSw3pR-6K0BA1Y8pCWQwoG3D79ESmUB89w7469lQ2xN9jENwXZIAM-AUFwydqC3Vo8M5XLJWHbAgyMzaWxClhreksC_DX7e5ZwUn9EQ_L9NfD6q28Bmk8Pto1atI6FG6q94RMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، به «نیویورک پست» گفت که مناقشه میان ایالات متحده و ایران ممکن است ظرف چند ماه آینده وارد «مرحله‌ای بسیار متفاوت» شود؛ او با ترامپ هم‌نظر بود که این جنگ می‌تواند «بلافاصله پس از» انتخابات میان‌دوره‌ای به پایان برسد.
ونس اظهار داشت که تردد در تنگه هرمز به «بیش از ۵۰ درصد» سطح عادی بازگشته است و استدلال کرد که ایالات متحده دیگر دست به عملیات‌های تهاجمی نمی‌زند، در حالی که ایران همچنان به حملات گاه‌به‌گاه علیه کشتی‌های تجاری ادامه می‌دهد.
ونس گفت: «این ماجرا در واقع دو مرحله دارد و مرحله اول به پایان رسیده است.» او هدف اولیه را نابودی برنامه هسته‌ای، توان نظامی متعارف و قدرت اعمال نفوذ (توانِ قدرت‌نمایی) ایران توصیف کرد.
وی افزود که مرحله دوم، جلوگیری از بازسازی آن توانمندی‌ها توسط ایران و در عین حال حفظ ثبات جهانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71738" target="_blank">📅 19:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71735">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VteCOoN6vuB6I2U6y79JkHJPIQ3ux27NCPzXX8V4X_UTamdYC5yO0TDgXrH8J-8GOewk3ffVnvFgj5MhQpDPChMmP39uqy5JAsaI-0lVXdU4JrQQj9j3kkGeSoGOSN2PNkoAo4LEFQ6ozi4w7CZbtqbXSyw_ApT1k9pekQJqY8hM0aFdKeMHahHTmsZ1k4YeCzbDofHD-7pVtoFy7gA7PRZq3rW7jzJDl1rLeqfkBGnzCX7aw-uUPW12p7Y7QxihVHy6B0TqhW7oZZC_YMqXS1PtRmO6q4npYc29DZ0EEVwr2RDPvx7YeLQYPvYa7QShjZTOTYlfC0nzaoeK7uxReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QX0iTXGR4Iv16EfhQakJ37o1XMPwuqHyvavQKTSp29he8bQyP8Np5ZL50Mffa2qLVz_Xndbf2fYamCLb7K0MhP7YGJF_ERnno43H6K7sY-Px5pfW5cwZxv7aXYog1bHUWv91BtWV1dcFgGRNfxt0EJuYUVTTZibSJmbPRcjT5gOVRR-hwSIst9ibOchCT6Y1VuAMTkTTJR-42yKAf2EUTvzdKNdwgBb5loWk4lJjSl3OmZsv_Tte4qeJfCkatoKHXui9Bbn6--H6-pvRpVhG8Z6xmkbhow_KRBQwJK_cxcm0nGdxv3d7YAPr0rBtCw2TP2UyPbDfHdccnSt5BLHcRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حوثی‌های یمن تصاویری منتشر کردند که مدعی‌اند سرنگونی و لاشه یک جنگنده اف-۱۵ عربستان سعودی در استان مأرب را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71735" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71734">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=CKXEAbi5zqzkrhQzG8cjbLO_W8KP-5bdmTRsX0f6oFu_PUMjz5zZrKamUaJezmJras54ynkAtWf6gS3I_zUP9QNxvHH1GFFilswC8oIzEMxEg8QMSppyYtiyjRth75LpdR4fB8m8ud6rqhVWFT7yZyWg3P1QJFOL7amJIVE7iafXhAFuZQ6eiS98ySUs8bGp01m-24Mxj_jLy9HLMLo2RkFXvO8n5cVNHtjNqhJRLi0suPT-Zp7ca7erI5m-7Azp__poi6d6B3M6t-8eO6w14llj3YKBOlrC1THI_uOER7VuXrYRxGKL7G1D8bCDeDhc0Zn8TUr0doJ6tU78Lq-inw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=CKXEAbi5zqzkrhQzG8cjbLO_W8KP-5bdmTRsX0f6oFu_PUMjz5zZrKamUaJezmJras54ynkAtWf6gS3I_zUP9QNxvHH1GFFilswC8oIzEMxEg8QMSppyYtiyjRth75LpdR4fB8m8ud6rqhVWFT7yZyWg3P1QJFOL7amJIVE7iafXhAFuZQ6eiS98ySUs8bGp01m-24Mxj_jLy9HLMLo2RkFXvO8n5cVNHtjNqhJRLi0suPT-Zp7ca7erI5m-7Azp__poi6d6B3M6t-8eO6w14llj3YKBOlrC1THI_uOER7VuXrYRxGKL7G1D8bCDeDhc0Zn8TUr0doJ6tU78Lq-inw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تهران یه کافه مذهبی به اسم ام‌البنین افتتاح شده و مخصوص آدمای مذهبیه و ورود افراد غیرمذهبی به اونجا ممنوعه.
شنبه هر هفته هم سفره‌ ام‌البنین دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71734" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71733">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71733" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71733" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71732">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OReiC0DkBGWY7BcJc-JxBlZB7MBjQLEBbU_M5evPji2MdhAKE2WNShO9XR3pkSTURJ1aiOZPO56j2Kcok0Ha_LCyl_fV-V2ZVxkm45fr3jWwo9sQnOFUoG7IiACr31D894iDjncKBUTRvSKqLpoOevwCvmURNRhNGYxMFqo4MEInpEWRX53uQDfXSjQ6HS-7UlUaix5GWldB8J0-s7ieogoVEQWXGPD2QGcofZQzMHhZGImdjcGzlSJ79ZUCgQ8vVDIEeMHXzhOQX7iPz91osSckLbu4MFXlOb_YScvCpv6Sjo4kvn-atHdUNNIAK-GW3XQfSSjKQSS6fadjYCFWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71732" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71731">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534f93c783.mp4?token=EeUZG0_zVJIMS5tc0ZmeVJiKq6VAX7xkKSCNhzrFXq-xnUJlV6KKWC4SrazOF0Iw2z4LhoW1AD8mmBJ8agNsx73_KyzywHco8SJtii9D22lVHHIVNMDCvvrfZGyqhgBJnRzZ_aqVs6LRxJzjMeXCLLEi71xJW2OML6TuFpmU3pTyq5hSenHugISNdHj5NX-6K137Bs2xM1vk77Y_t_llkNfv14olBmrnS5SrJNfQJxzcrHamXW7d4iEtiulqYiZ90g5YfzCUmQaqQ32qZEtBWZ36jGfDysfd1fee6D3ZHRFVDk_Z9_t06-dcYCdqFwnoHv4EWN3kp7mn_KyD3Ood4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534f93c783.mp4?token=EeUZG0_zVJIMS5tc0ZmeVJiKq6VAX7xkKSCNhzrFXq-xnUJlV6KKWC4SrazOF0Iw2z4LhoW1AD8mmBJ8agNsx73_KyzywHco8SJtii9D22lVHHIVNMDCvvrfZGyqhgBJnRzZ_aqVs6LRxJzjMeXCLLEi71xJW2OML6TuFpmU3pTyq5hSenHugISNdHj5NX-6K137Bs2xM1vk77Y_t_llkNfv14olBmrnS5SrJNfQJxzcrHamXW7d4iEtiulqYiZ90g5YfzCUmQaqQ32qZEtBWZ36jGfDysfd1fee6D3ZHRFVDk_Z9_t06-dcYCdqFwnoHv4EWN3kp7mn_KyD3Ood4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این کلیپ تاریخی که چند نفر میخواستن با برنو، سوخت رسان و جنگنده بزنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71731" target="_blank">📅 17:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71730">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فاکس‌نیوز:
یک کشتی طرف قرارداد ایالات متحده در نزدیکی تنگه هرمز هدف حمله‌ای از سوی ایران قرار گرفت که در آن از چهار پهپاد و دست‌کم یک موشک استفاده شده بود.
این حمله منجر به جراحات جزئی، از جمله عوارض ناشی از استنشاق دود، شد.
تعدادی از کارکنان آمریکایی در این کشتی حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71730" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71729">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6UX0FlrKsUAX_oH6ONQzbF1CwyHd1oemxqEqgpEnGojz2z3a4Mu-LZtsDuf3Aaiq1ou-jVCQc2mITNxNe1OjN51K9n9yidC1Jw7xrurl8L8yaHpd74zdpQNLCsshw0nYQW-eLUEdbO6Hu5tM62aIcuGFhCV1X5HcQUeC97XdsDOgbgKVy1craE6AepT_usRZ-PBYj3MqAU_BXvU2fC89D7Tx3m6XQ9S8PXdTR2GCb7vFu8sSeb1ij6c-NtXvSlAKoQtAXvsmO9E79ZUsG-9Cel8QAMqfag8Wok-ivvznXf_SvsmKleM4xnHZXUy1joTRQCdfSV_dvRxTeOWTcCw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در تجمعات شبانه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71729" target="_blank">📅 17:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71728">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2421361f81.mp4?token=i2jia3XvQNWf8rMN3Ov7KM8Mezzbgrrwg-FK60wSIRaCcyN5hHVDiSqobTiVY0vqCnVCnYUGV2Pb9sWnlbHCInj8i1G6AFfFOGs3W0eClblvsBIayVMe-667vJ-WaBvk8aWKgd5bVQxURM6pVbwamdw2Uz_xoMEbHaM_MXbZwj3XRWXlrRD41FFQXnbW1lihBPTc0zkW-NbKgxpYplsd9uxyi45y6VqLXjW2ZorJuki7PRbwn7S1W0bOy30RJ-YHFXPqAKcEruGnn4_xeqvtkks87szW8YrVENXMEdmMHno5_BMDbMj40rQvEIl_M9GOHVzXiNLlTluyYkrafpHT-S8By06LA7bqzkneJnGxBggWdU7TVtGMPrv-NvBRW0ZK3XP3UdGBZFarsDoAH0MZrQlN20uf0ShSwPd7VdhoM2mci0SxkVZ6mxg0al7PcJNYJy9ehAdPv1wpdvQYxCDvUJPwOhUhmJHl9ZSceveSzSCLPEfvgDo0KxHqXpdIDlkjvTrhtxEf7juFD40KuTR5ghDi9RTShNPYEoA2fsi-UxO58iNCtrVMUFtQ_p2rSvppsJkt2U11CZVLh38_iJoQD5jVRQnepdC-aLcSrt8TmFKrdQ05yRoXHGfSGS3NNI1_xolIzNGdjhaEbZRmp0cuIFVlqVJ78_o_YsjVcuf1FPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2421361f81.mp4?token=i2jia3XvQNWf8rMN3Ov7KM8Mezzbgrrwg-FK60wSIRaCcyN5hHVDiSqobTiVY0vqCnVCnYUGV2Pb9sWnlbHCInj8i1G6AFfFOGs3W0eClblvsBIayVMe-667vJ-WaBvk8aWKgd5bVQxURM6pVbwamdw2Uz_xoMEbHaM_MXbZwj3XRWXlrRD41FFQXnbW1lihBPTc0zkW-NbKgxpYplsd9uxyi45y6VqLXjW2ZorJuki7PRbwn7S1W0bOy30RJ-YHFXPqAKcEruGnn4_xeqvtkks87szW8YrVENXMEdmMHno5_BMDbMj40rQvEIl_M9GOHVzXiNLlTluyYkrafpHT-S8By06LA7bqzkneJnGxBggWdU7TVtGMPrv-NvBRW0ZK3XP3UdGBZFarsDoAH0MZrQlN20uf0ShSwPd7VdhoM2mci0SxkVZ6mxg0al7PcJNYJy9ehAdPv1wpdvQYxCDvUJPwOhUhmJHl9ZSceveSzSCLPEfvgDo0KxHqXpdIDlkjvTrhtxEf7juFD40KuTR5ghDi9RTShNPYEoA2fsi-UxO58iNCtrVMUFtQ_p2rSvppsJkt2U11CZVLh38_iJoQD5jVRQnepdC-aLcSrt8TmFKrdQ05yRoXHGfSGS3NNI1_xolIzNGdjhaEbZRmp0cuIFVlqVJ78_o_YsjVcuf1FPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیویس کیس سخنگوی سابق نخست‌وزیر اسرائیل:
دیکتاتورهای ایران ظرف چند هفته سقوط خواهند کرد؛
دو هفته، سه روز، شش ساعت و چهارده دقیقه دقیقاً
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71728" target="_blank">📅 16:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71727">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=L9OCfLLTI3r8iRVQLTbZbjhCkgZ-Ndcotzziwdt_-TQu1N0085v0Nu3m-gW-7J-RCvynIfjcieC9FXSv0xUth-yJKzsCCKPsSginFMdtiBgP2lH05u8P0O_ym0-Fe08zHRO8LyipEMqM8KfCpSnA09DaVu1XxzrsLQGz6lT5u-zzeG4VKEmAhNFwApDPWUCHOphPMN2_OiKtnmcbK7j9_XkHAHw9p44LxUk2TeI5YhWRIFyjxKMzQpgFH3WHj5-6EscgH1pgaaz-LhAqXg1PAQJQftt4n8v7aFznXGEh0hNIKepkeBCEZepbe0k_U6AcG6yqKxxzzXSUFhZVACsw8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=L9OCfLLTI3r8iRVQLTbZbjhCkgZ-Ndcotzziwdt_-TQu1N0085v0Nu3m-gW-7J-RCvynIfjcieC9FXSv0xUth-yJKzsCCKPsSginFMdtiBgP2lH05u8P0O_ym0-Fe08zHRO8LyipEMqM8KfCpSnA09DaVu1XxzrsLQGz6lT5u-zzeG4VKEmAhNFwApDPWUCHOphPMN2_OiKtnmcbK7j9_XkHAHw9p44LxUk2TeI5YhWRIFyjxKMzQpgFH3WHj5-6EscgH1pgaaz-LhAqXg1PAQJQftt4n8v7aFznXGEh0hNIKepkeBCEZepbe0k_U6AcG6yqKxxzzXSUFhZVACsw8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ دعوای این دو تا بچه گربه خیلی وایرال شده، از بس کوچولو ان، دستاشون به همدیگه نمیرسه و رو هوا همدیگرو کتک میزنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71727" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71726">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=EQ7x1fJqf-rK7Ja_InkrvAFQG90TOFFVVIvGAepxdhBWmdmeU1xb1RA2dIAp8pL-DQuqY4FjDhPHcHZpd5K4ZNv3aw268Zq-9N0jDl7VUcJaQG5KFRcJzFnCzD2GA0zrYy-vSDieZL5YMCOZ8chHQcca_LzWxlEYWbyPQ97LWw9WGwSDsU5VBngmEly0RPdRAl7jZZTdOt-Mt00SGVHQp9n2FyML8NV75BnCS2IXiW_ZgV3s6IB1JzGhexI-_gMyDL-ivNmfFu5aoEpm9HTD4NX13YBccn-mgJwM_HodXrPMNIm9FMi-1b5csCQI09X7qhGtFI-Gowju8rbmy06tow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=EQ7x1fJqf-rK7Ja_InkrvAFQG90TOFFVVIvGAepxdhBWmdmeU1xb1RA2dIAp8pL-DQuqY4FjDhPHcHZpd5K4ZNv3aw268Zq-9N0jDl7VUcJaQG5KFRcJzFnCzD2GA0zrYy-vSDieZL5YMCOZ8chHQcca_LzWxlEYWbyPQ97LWw9WGwSDsU5VBngmEly0RPdRAl7jZZTdOt-Mt00SGVHQp9n2FyML8NV75BnCS2IXiW_ZgV3s6IB1JzGhexI-_gMyDL-ivNmfFu5aoEpm9HTD4NX13YBccn-mgJwM_HodXrPMNIm9FMi-1b5csCQI09X7qhGtFI-Gowju8rbmy06tow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه رستوران تو آمریکا باز شده که تم بیمارستانی داره و تمام‌ کارکنانش کاستوم دکتری و پرستاری پوشیدن و اگه غذاتونو کامل نخورید باید براشون قمبل کنید تا خانوم دکتر بیاد شلاقتون بزنه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71726" target="_blank">📅 15:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71725">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=UsUGxHMA9-XEFyQRrxucIOsMtzlN77SSJoIal6bO0AOfIvf1KuWe_G5arwWoQcwrRAvTWqofvUVlWL9CTUtD238o_Vu7znoY3G0YIqzvmwKkPVXX-yZbAjhWoECQBzEfVe6C-Mty89ORU0Fc5a5cuUIvys3CyV0IAML-WTLSal9-RF18HCUp-q1H5wumF6UHwriZJMRTfE2_RaoRy863amhyUdEMmPXU2Jfft5dMGa2L6cmsJIw0J1MoNBBZIhrPVE_KYCgyq7GJBRMLSg_HrVr-v1NQfOukyo6hZeiCTIIssOybmd-Ui98Di6OOrxnRYk406Ka_qTzVaAOSWLcdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=UsUGxHMA9-XEFyQRrxucIOsMtzlN77SSJoIal6bO0AOfIvf1KuWe_G5arwWoQcwrRAvTWqofvUVlWL9CTUtD238o_Vu7znoY3G0YIqzvmwKkPVXX-yZbAjhWoECQBzEfVe6C-Mty89ORU0Fc5a5cuUIvys3CyV0IAML-WTLSal9-RF18HCUp-q1H5wumF6UHwriZJMRTfE2_RaoRy863amhyUdEMmPXU2Jfft5dMGa2L6cmsJIw0J1MoNBBZIhrPVE_KYCgyq7GJBRMLSg_HrVr-v1NQfOukyo6hZeiCTIIssOybmd-Ui98Di6OOrxnRYk406Ka_qTzVaAOSWLcdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله افراد لباس شخصی و آتش به اختیار به یک رستوران در رشت به نام « سحرخیزان » و تخریب رستوران به بهانه حجاب⁩⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71725" target="_blank">📅 15:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71724">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PErL56FzX_d0O-OrpFgZRYvfGnpGytCComHxenuU9HhzWVGazjRvG4kzbjv0HTbEpU946FgTDeH7i5bzihTC0onlQu8JmjLTRNNsPMg695S3bIP8xIIb4yHwxAHhZVzm1uVeWMXdYlKJvE_AjjC0N-J3Tpt9eUJNiGzQTMhJF57o4oDoMRVaILf7Bg7ELaUAENeMU1gfni9aHvUuUY1rBtoPWjRHfy6KHfPU0HGEtbrg-q12CVijyoAMonw5hhD1_sHfpQKSQRFJkx1JmzdQ2jEMllnjKPJjslzjKbVVxaWHj26eBWyIUPm4A5IPdwPmGVZ1OW8aVaF4MJHSwOXvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛  سامانه‌پاتریوت شیطان‌بزرگ مانع شد خانه‌خدا توسط حوثی‌ها نابود شود!  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71724" target="_blank">📅 14:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71723">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=PATmTQbB2zn3cQW8yUd-os-TpqpiEsZ3rqnYu2hporWxtv5oTQRWIAzs8mjgvL6LIei2JwQpwRcpdaX0BPC9kLgWE6KZRrFj8uyMDAQNgG43EtRaVmgpuG56gjGkCHDdWtp-VjnzVntKDkFRw5C9P6RfBQvGAm_GJxXc9nhXTbZZy5Lf3-Nl4VreKOOx4zR-MAJKBnZsuQNBAQaiE993ew5bzD-YgBdcilsrT-Wd2aw5QYlifcMEp9mT1FqX7UoqXH0dR8QOFsWPkYENiq4HA0SzN5ADdvoBfS7W7gDl7TWD0nDAfxNa_ouv0VRfvZ9ZGz91NxJLeaXigLD2RhIgIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=PATmTQbB2zn3cQW8yUd-os-TpqpiEsZ3rqnYu2hporWxtv5oTQRWIAzs8mjgvL6LIei2JwQpwRcpdaX0BPC9kLgWE6KZRrFj8uyMDAQNgG43EtRaVmgpuG56gjGkCHDdWtp-VjnzVntKDkFRw5C9P6RfBQvGAm_GJxXc9nhXTbZZy5Lf3-Nl4VreKOOx4zR-MAJKBnZsuQNBAQaiE993ew5bzD-YgBdcilsrT-Wd2aw5QYlifcMEp9mT1FqX7UoqXH0dR8QOFsWPkYENiq4HA0SzN5ADdvoBfS7W7gDl7TWD0nDAfxNa_ouv0VRfvZ9ZGz91NxJLeaXigLD2RhIgIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛
سامانه‌پاتریوت شیطان‌بزرگ مانع شد
خانه‌خدا توسط حوثی‌ها نابود شود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71723" target="_blank">📅 14:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71719">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IT9vWi4g2xm8mYXiyl-WsCEQUarNE_TjgWQfbcx1lLSMsp3Laj2lAFiNi3QVn5faPOYE74aF-hu9KfNa9xLGEhj3LOudbiUiIuFxkMXVeJLzwaj-zZbeBOZBipGCR535Pu2xnYlM-0UT4e54hEYnLMmI6V0mZtn1C3XUrWMBNsY360L4WxSRGx5AOFlDOB8wyN9bjo7zEwhEkvvQW3B0ET7Rf31YBv0v1waMd48pNPJmG3vaWhDTHlHfwhB4_xDP4XV9THnqjVE7-912zVEdulLG3btwfdCX7DvlgsQDIUv60dmiKmBy6PcZitfCDeBujmXaA0V0kqrPtuKR_skHPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8SnlfNVica--_YsfcZveWUCEBJ3ugqlWEHCIb9cIwzBmrQi9F9S_cZuJcgtDqVaO-oVp728ohBwb0F5VtmEG-1MZ-jiLlyCHh1kGntKFvkxWRHTuluhFSPoTVTTFrjdK6wIBK5vYBjKKCgaLfYsiafiXh_5kvAEy4bFMhG7cTytCIQjfV0eTRPX3D78p7dNL2NWmWXB_Tn1ykpq-II6-fQb22y9MCb22sCJYKra9McPh9bjzkEwvMHr8yCqu0QK6tYsOG-2iCeL17ub4_FGFNnFem6ByOthjChjtPmrtJ4WTBobIQRvjvoEJEqT15mM9HJLS2MBFkymugkRB7iiVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CN8kAxb-5qooxjtypBI6beuEMT8nb8jYoSkEkiUeQUOdJwmzTgwjbFhX7rJNluzYYMWukieIv-r3qWc86VvVnvCVzOcIrJ3d4IOeF0eKA6DOCEYZ1_hfpQpy5vN6WR_CJuQvHrnt7t3cWo9eorNIkzS_dOo9fq_CICJuETtJ62ZxQT4KUFjHhBio7KWKk83dcWNlCZm2165IRmiCvhti8YvrzOpqS22pdyJ_0D00zy2pAkW1nLeiqlGRWDv3ppuvU866rTKb_mpAesmlV4ixNNkbkby61DsJTD0kzyfaCY7PEXFVO8e24LT9ZJzaL6-xD1mVsPmUyqe4DpcKgD3QKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCmBly0yuTh7R5_hIBix6iYwUmADvQbFEw20Rx4HxzRwyjJoJOSM0pCowMpOXRRn5nXlfu-zUpYYcnVtfwC-tu9ExVkoMWHR3i2cGUQBy8_V3ADCzofVy5pxm8Au1hS7C95QU3UmszOcE0dcTCRG4iX12Ej-xTtJonNqfeEtaiNcZHiXCeqoNQ0T2soIS6SNfz9NGDvwd2NxVeQin_oqtuIrF99KVWYN8mok-Yzs2Gvdn2hzCBQwcJCjwDaouec64AcGsnQomj5OuLVjvy8l4yG_NP_8VaDpU2uukVienp2uGDQ2N8Sth4Sm4uIjNr8A-f0-9UrtGNPIhJ20NjfyFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های اختصاصی که توسط سی‌بی‌اس نیوز به دست آمده، خسارات گسترده‌ای را در چندین موضع نظامی ایالات متحده در خاورمیانه پس از حملات موشکی و پهپادی ایران نشان می‌دهد.
این تصاویر که توسط اعضای فعال ارتش که ناشناس هستند، ارائه شده است، ساختمان‌ها، وسایل نقلیه و تجهیزات تخریب‌شده را در پایگاه‌هایی در عربستان سعودی و کویت نشان می‌دهد.
در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای بوئینگ E-3 Sentry مورد اصابت قرار گرفت و قسمت دم آن جدا شد.
در کمپ بورینگ و کمپ عریفجان در کویت، عکس‌ها نشان دهنده پادگان‌ها، تریلرها و وسایل نقلیه آسیب‌دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71719" target="_blank">📅 14:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSvOe9BUJvur_B7Wdufl9imQIxerrTtlSlCy0pwOYczr1CJIsa34hWMif0tL-ZSCdvSE7ObbLQF6UjaSiIwS_cf7hWuE7c_liiCabGMzOezBSdXmZw-2BvsVc16X1CeyKO_eKRFGnNq_5QZmYGpVZETvZcnr9fEL9-UtLOxA6yclkzPKR6yZOrR4eaRtg3eTQ6bmr3Qdb2QEcuHiMfa5CUrT2hLzCb4zEeH_792whjQFLvUg3dMz3wnwJEegq-d5-r9q81INXTEsdXxNyCaPxZyep9IJry8YVT53c3Rmxevvcl6AzO10L5MI8ar6NgZDsJrxvbmcRa13r4ujXa0m2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشته است
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71718" target="_blank">📅 13:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71714">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a175287c.mp4?token=CDte3JUZ9fCe9cWKs7r2nrwZstEASZIlyxLdfNgb0JxnjO2O_r6_vqonZKISDPHZm3btmSfdP1uPQ-z3RiogQM8TOGZ2e28Ofk7YjZ2D7DnG9GxxhRf6QFdSed8myjfqULV9HWllwmDvv90EOp_p5EOGch2ET27pf-UHg529XZakvtR3HHDGUZqPea8lG9P2tnfTlrv1v8IRhBgfhSxGOaEp2NOULj9OiV7ypwmEISKC1EOQ5I82vhi0oFMycwjDuKY71JG90AGT8xsDXuHzNnueL-yc4DWzVfmOoxoSUK52YYkIamraD5sgMZ9KhsGTIJXVxQJw2uwq7qjxo9LnTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a175287c.mp4?token=CDte3JUZ9fCe9cWKs7r2nrwZstEASZIlyxLdfNgb0JxnjO2O_r6_vqonZKISDPHZm3btmSfdP1uPQ-z3RiogQM8TOGZ2e28Ofk7YjZ2D7DnG9GxxhRf6QFdSed8myjfqULV9HWllwmDvv90EOp_p5EOGch2ET27pf-UHg529XZakvtR3HHDGUZqPea8lG9P2tnfTlrv1v8IRhBgfhSxGOaEp2NOULj9OiV7ypwmEISKC1EOQ5I82vhi0oFMycwjDuKY71JG90AGT8xsDXuHzNnueL-yc4DWzVfmOoxoSUK52YYkIamraD5sgMZ9KhsGTIJXVxQJw2uwq7qjxo9LnTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
:ویدیو هایی از اعتصاب عمومی در سنندج،سقز،دیواندره و دیگر شهرهای استان کردستان به مناسبت چهارمین سالگرد قتل مهسا(ژینا)امینی به دست حکومت آغاز شده است.
همچنین ویدیو هایی از شهرستان پیرانشهر در استان آذربایجان غربی رسیده که نشان می‌دهد بازاریان دست به اعتصاب زده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71714" target="_blank">📅 12:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71713">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه پسر ۱۴ ساله با یه دختر ۱۳ ساله وارد رابطه شده و ا‌ومده پیش دکتر میگه من پرده اینو زدم و گشاد شده؛
حالا اومد پیش دکتر ازمایش بده ببینه این دختره قبلا رابطه جنسی داشته یا نه.
سن رابطه جنسی تو ایران داره به ۱۲ سال میرسه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71713" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71712">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71712" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71711">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrK5DR4FI-bcsRjDJb1lasYk4_upIbMu3bCALZRAaCoszenasuEgHEl6dybatiiRmhkALnTQEYSC1cWG7fozvFOFYa5hbCPjGwpaW2lre4NYmeoEL-gvcTEsmy2ljnHCsE55Wkysnct2gpkskHrk_zQlMvf_ZrXHHUOMYeTt_8ODOBQ4f7l9og-asiI4p3bh7sVz8yr1lCtQFrdGOTb-v8Ru90OQWnNn-61WYfrAz6DURa0x-J-icFWnZNWlULkiay4K3Suh2dL_z32W3fIAWCrPf4DRh5L8_ia9562nL4HgUT-xR_UNtiKLHLOSwLhCGQc552Od8Cd4oKiGXG6ISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71711" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfhLuvxt6cpqV0d9obgKSwmKTW-OncRi-gW9DoxQXpbtjrTnNqsPAYvS1nBYmr6dtGFZTvhNfhlWIztllfqV8bDDqApzKAlwBtDVBWDFrC50ivyM2ptDn3w4pEfHD22jYwCn23fUCLFlWmYnx-bx-fbadjD_gNqgzIlgTsnVqQIJM6IVST1oC-ZLoBepFPcKN7cfglGK3Pgg6Y21zpD7ymTrvHx1gxXNoCjxjvwvyqLqPwkZUi2PSLMQUqPXeeo3OE3H0_MAdwOomQVj5VgeP-8CQ6HpwC5ZvyseCu-k27EW4YeQep6sWrnvE4gZy5gHDaKl0PSwpB-Evw2vJJ2Zjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده برای اولین بار تأیید کرد که سلاح‌هایی در مدار دارد.
مینک، وزیر نیروی هوایی:
ایالات متحده اکنون سلاح‌های کنترل فضایی در مدار دارد که قادر به دفاع از نیروی مشترک در برابر اقدامات خصمانه دشمن هستند.
از بیان نوع، تعداد یا زمان پرتاب آنها خودداری کرد.
نیروی فضایی می‌گوید که می‌توان از آنها برای "اختلال، تخریب و حتی تخریب" به صورت تهاجمی یا دفاعی استفاده کرد.
کارشناسان فکر می‌کنند که به احتمال زیاد، پارازیت‌اندازهای فضایی یا جنگ الکترونیکی - سلاح‌های جنبشی - مشکلات مربوط به زباله‌های فضایی را ایجاد می‌کنند.
این به دهه‌ها ابهام رسمی پایان می‌دهد.
اولین نقاشی نیروی فضایی به معنای واقعی کلمه یک هواپیمای فضایی را در حال نابودی یک ماهواره متخاصم نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71710" target="_blank">📅 11:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26353c8137.mp4?token=BfwaHIA2YKwb0Z8pt1jG17cfwtzkz5aE55Pfdasn-Z5W2h6EMe4LFuTIuAaV4ZOuVMYaooOvw1ADVHPX6HR6HPgd5mz98hI3CSAMI_1o7cxW2JcsFaeYALxE-QAwBlmlPgnrPlqsoGWk1BV1myIvIUIu9RglwriU1vDPJVQV66l4DB-Zvy4ZiLj55Zc5Yl8t-2nnSVsOFBwD7fX5VBGXGTrqU1vYkaUP7EDrAgHsNCiJDdkynX2fzDpsoAkjxT_tDoBIlbnUo94m1hBF6opZdscbfs-0pILjdiDYUg3lMd5MNHvNLBMx4atGFtj1SoEni3WmyRwkGK95DB33DaAgZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26353c8137.mp4?token=BfwaHIA2YKwb0Z8pt1jG17cfwtzkz5aE55Pfdasn-Z5W2h6EMe4LFuTIuAaV4ZOuVMYaooOvw1ADVHPX6HR6HPgd5mz98hI3CSAMI_1o7cxW2JcsFaeYALxE-QAwBlmlPgnrPlqsoGWk1BV1myIvIUIu9RglwriU1vDPJVQV66l4DB-Zvy4ZiLj55Zc5Yl8t-2nnSVsOFBwD7fX5VBGXGTrqU1vYkaUP7EDrAgHsNCiJDdkynX2fzDpsoAkjxT_tDoBIlbnUo94m1hBF6opZdscbfs-0pILjdiDYUg3lMd5MNHvNLBMx4atGFtj1SoEni3WmyRwkGK95DB33DaAgZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک دانش‌آموز دختر برزیلی بعد از اینکه نمره‌ی خوبی تو امتحانش نگرفت با چاقو به معلمش حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71709" target="_blank">📅 10:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71708">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=CmGWm4txOaOCUgFYucU7N_ULwuCLzYlJVFrl4PBzsqiCmvaY8hZhYHmLneLQ79aeaqOKG5FVYIR2RqhdOmNBVK5ZBNoVIbSHm6pLFGMoHktWNXkYFq64NeqjkqAwur2APO4j1hZcdjv0CXZP_6EX3tzL8a2nUaEVuIFgl7GIKSbIhf6PK5bIy3CB8ZvAVMnGgHvYAlIZ7LE4NresG0vAxYSTLEN1DN4IMi4UmsaF-283KpHR2ilz4hRAFljUXFvQ_LGmlFdxHl0Z8Q0L84CaBaJgHboxbYMx_kqEWwVkXR2TQxg6FoJApARE7ha42BrOBKX6oYNOtDw7GV9vXLu9cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=CmGWm4txOaOCUgFYucU7N_ULwuCLzYlJVFrl4PBzsqiCmvaY8hZhYHmLneLQ79aeaqOKG5FVYIR2RqhdOmNBVK5ZBNoVIbSHm6pLFGMoHktWNXkYFq64NeqjkqAwur2APO4j1hZcdjv0CXZP_6EX3tzL8a2nUaEVuIFgl7GIKSbIhf6PK5bIy3CB8ZvAVMnGgHvYAlIZ7LE4NresG0vAxYSTLEN1DN4IMi4UmsaF-283KpHR2ilz4hRAFljUXFvQ_LGmlFdxHl0Z8Q0L84CaBaJgHboxbYMx_kqEWwVkXR2TQxg6FoJApARE7ha42BrOBKX6oYNOtDw7GV9vXLu9cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته خانم دکتر(روانشناس بالینی)؛
خودارضایی نه تنها ضرری نداره بلکه خودارضایی یه چیز سالم و بی‌ضرره که به عملکرد ذهن و مغز کمک میکنه، باعث کاهش استرس میشه و حتی به رابطه شما کمک میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71708" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71704">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyyRJyyBdqSDD1-QL5rSJQOiweDxwoWuayjdjxKOF08hRUfwX6mn-6UNf4wuCU8WKa-Ldn9vYSIF9epuHiGr_8AA6fBwYA2tCm_V-WlNGh9H2bBpYY-81aN-cQ7Uuls3oi18YNhEXwUaYlOhhJ6X-_gmmH14dUhJvzpJa5UntrCgTp9GMVYMWcFHV8WAOifB-vOMJXJSSQhvbch5rRnyM221uoCoFkR_Hy1_HCQnkh0F4lldncqgXdh9JX9ZD0qsBRJt-m7h4XNvHTP6IGe0Hp54z8HEfLeP79Yf5Hq5k7rltrSoeAgLEyiJOwb739PoXi8rRi8j8W-YQvr6P8ecwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=l3w3qktIeMG4PRsUcIt_wgN6GtL5VhLwYl7CEtsWEISYewtGfWkLPYAyrU1TKK8aSuy2ouFJwUnQDSI27x0YwQdfeDSrvumRJKwyno5S_n23Uj66AabjtdJaHZmG3HVeh73eIs79CkrOYj6gakdj2TonpipY-2Q2lGbd-jFhfwNfpat7D_STfRT8b0Qopt_hJBze5f7UTDLLvyEyYTrifEEh824NZDU-BobudTm9apjinZQkGosCA5nxS3QbqkZ2CzVAOzzNHMYr2RK5NwcClWNzungyQ6zLM0VRCWO-ELt6rePlTYu50vFSpc7a8OXf5TOAOKEe4abSa-dVv_cYQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=l3w3qktIeMG4PRsUcIt_wgN6GtL5VhLwYl7CEtsWEISYewtGfWkLPYAyrU1TKK8aSuy2ouFJwUnQDSI27x0YwQdfeDSrvumRJKwyno5S_n23Uj66AabjtdJaHZmG3HVeh73eIs79CkrOYj6gakdj2TonpipY-2Q2lGbd-jFhfwNfpat7D_STfRT8b0Qopt_hJBze5f7UTDLLvyEyYTrifEEh824NZDU-BobudTm9apjinZQkGosCA5nxS3QbqkZ2CzVAOzzNHMYr2RK5NwcClWNzungyQ6zLM0VRCWO-ELt6rePlTYu50vFSpc7a8OXf5TOAOKEe4abSa-dVv_cYQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر تیک تاکر به اسم فاطمه تاجیک دیشب توسط چندتا دختر که میگفتن عکساشونو گذاشته چنلش خفت شده و خودشو دوست پسرشو کتک زدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71704" target="_blank">📅 09:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71703">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFcVPn2gyUjMjb3uRq9axUBjoC2RIl5gHC62PbWPR8Nn3obDsMyIykRU-VhrsfROCtTU1d9EMmiqe5VJ0AacofPvqOEiIwfda-QGsRu8RTBlXX1cqhB_CzNfnZXW5aSk3q41x_-tQhLiZIW6vq57w_XIPbsOxOFOlujAGLdHDMFaRjb8nb64xnPpA1I_AnCNOBfROVS2gXoHL5oL5AOSY3dVw782FhJnuTgTNXRveiptmyujEGTBzjdhoYqlz57-PSNiCd2VgLj4X5cw855JqRr4_7yG40IV361FiCcz2cn3smnT5TVDaYQMC-rdvyyQs9k3S-0s4Mnt39A1qlQ5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس:
فرماندهان ارشد نظامی ایالات متحده، اسرائیل و هشت کشور عربی هفته گذشته در آلمان دیداری محرمانه برای گفتگو درباره جنگ با ایران و امنیت منطقه برگزار کردند.
این نشست که به میزبانی «سنتکام» (فرماندهی مرکزی ایالات متحده) برگزار شد، با حضور فرماندهان نظامی اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر همراه بود.
دریاسالار برد کوپر ضمن تأکید بر تداوم حضور نیروهای آمریکایی در منطقه با وجود حملات ایران، شرکت‌کنندگان را در جریان برنامه‌هایی برای گسترش تردد کشتی‌ها در تنگه هرمز قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71703" target="_blank">📅 09:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71702">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71702" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71701">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbrOtsV7g727fOJ_xYdPH32H4i1aeyJEU5pkxcoUNw262COmcTsxB6m1mazVw6C8d-Gl1Qv_Bqvql_gtuRhr3RHwo0WLfizJRLVmUOCDB1ZBk4vSnvKtNQD1vmMmW0LI-9cchZeJpe9R2fYEh4xWRMhe7f5OGjtaXVzcqMnG1B6sQlSFD5mAVchyG8cJT19dkS_8EW3hJNQraLqeR-ue0wRGXFd77hplVGa7oyPJJDLJsDuGw_eGyIk7n5yL2yzelG6c-Tvu3VZfHMSba8uQUwy4D2z1y83cb4A0leJgLb6jfBp-OMUr26xZkOH3MTNpqD-TOSN9K0NFl0C--EtxmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71701" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71700">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71700" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71699">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71699" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71698">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjfFKhT0_udecRsyCH9qL5kaV8uRIkIJXpp7f216aAM5gLjefEw4YbA1zW4oLVZRGiyymfCyvLtCCRXpHEnabPJAg0OU1snggEmRHB4YcOFnqbWGLCnJ1OzDo74FoDZyxyP_gUPYKyvr7piqBiEeCK9qqWSQeLsa-HDJDUQFpT5DjR6YxmJKkfqwqDF9hvY0gOtxs2r2S073ezpLHgm2RvSndxWyklLU-EO-HXE8rAN91t5U2ed-ft6Np3UyxC_5kNRXQlDoIol2wnLN1BvchOhAbB7sPMb1dtg2-yz4E_3yZdqxLIoaLfSeVQHE-_xqPJBKFGVw40-fpAM53Fwqmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آلمان (DPA) مدعی است که حوثی‌های یمن اکنون در تنگه باب‌المندب مین‌های دریایی کار گذاشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71698" target="_blank">📅 01:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71697">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=WQf_p44mauCtxTtdfFQ4wmNaiOCz61pZZDOkheho6n6eMTYgBW2nc63khLm7a8C0vMBFpQBX6eHP5HdbD7YgNBQQekLopOY77md8wKQFPvyt5Ti4H7_3gk0ZI3X48WhyqKudHKyLNwEB3Zskn3SWuB6tN9s_0-4MX_eHYNPpLl1VeWCX52ta32DIlHS3420ehADvHvU0twWq2tpe8Yp-XSGhBJCxGyx-ND5j8E4pcqmRsQTygn0k6Z7Gf_D-Ay7Us8xN1R0G1AKMu7ozfmWPUrQbtI92zNv44O1KtA7tpwgtlE1QGiPKWApc2hs524gLt5vavxwunP6aHZpwb4lbhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=WQf_p44mauCtxTtdfFQ4wmNaiOCz61pZZDOkheho6n6eMTYgBW2nc63khLm7a8C0vMBFpQBX6eHP5HdbD7YgNBQQekLopOY77md8wKQFPvyt5Ti4H7_3gk0ZI3X48WhyqKudHKyLNwEB3Zskn3SWuB6tN9s_0-4MX_eHYNPpLl1VeWCX52ta32DIlHS3420ehADvHvU0twWq2tpe8Yp-XSGhBJCxGyx-ND5j8E4pcqmRsQTygn0k6Z7Gf_D-Ay7Us8xN1R0G1AKMu7ozfmWPUrQbtI92zNv44O1KtA7tpwgtlE1QGiPKWApc2hs524gLt5vavxwunP6aHZpwb4lbhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا به‌تازگی طرح استیضاح دونالد ترامپ را که توسط «اَل گرین» (نماینده دموکرات از تگزاس) ارائه شده بود، با رأی قاطع و سنگین ۲۳۲ به ۱۴۷ رد کرد.
بخش بزرگی از دموکرات‌های مجلس به این طرحِ پوچ و بی‌معنی رأی منفی دادند، چرا که اَل گرین خودسرانه عمل کرده بود و آن‌ها می‌دانستند که این قطعنامه به جایی نخواهد رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71697" target="_blank">📅 01:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71696">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ونس امشب گفت که تو ماه‌های آینده، جنگ وارد مراحل جدیدی می‌شه؛
اما در شرایط فعلی همه‌ی تحلیلگرهای نظامی معتقدند که بخاطر انتخابات میان‌دوره‌ای، جنگی گسترده از آمریکا نمی‌بینم.
اما یه نکته‌ای اینجا وجود داره، انتخابات سنا و مجلس نمایندگان آمریکا  نوامبر ۲۰۲۶ (۱۲ آبان) برگزار می‌شه ولی نمایندگان انتخابی، با ۶۱ روز فاصله به سر کار میان، یعنی از ۱۲ آبان ۱۴۰۵ تا ۱۳ دی ۱۴۰۵، سنا و مجلس نمایندگان با همون اعضای قبلی ادامه می‌دن و می‌تونن قانون تصویب کنند؛ بنابراین از لحاظ تئوری، بهترین زمان برای حملات دوباره‌ی آمریکا همین دو ماهه (در صورتی که دموکرات ها پیروز بشن)
ولی یادمون نره که ترامپ یکی از غیرقابل پیش‌بینی ترین سیاستمدار های دنیاست
#hjAly‌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71696" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71695">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwn66BrgyWRbFSB9aSemtcMsFGq8vPouFgp9CvDNE-LCvWE-TkHES52GIyNo4kYVU5aPHSLuiCDtrQgzL5MlJOP6QJ3n0AwLhcILcgafL1pSRieQkTZtcRuNNDKtdbbnWG7_XDgrgiJyCs8eyxsV2FOWK1YfvPJmgtIxxt-6vG6MbxMgzEWjPMVjC5h5L3PcI38oRjo7fj6_FKYD-hyiXQOzj0O4f4KTa-QPsP5tLLGKUk_9VkKGT41AazkmsSAtoKPHjJbT0WH2gwZY_XVhBoRLe-_6ytkUwc5FTkAl_4u5icbgeacqSqVkp86S9X9WxnJV3MqE2YRtl9o0uK6Nig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلیا هاشمی:  امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت. مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71695" target="_blank">📅 00:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71694">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایلیا هاشمی:
امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت.
مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین لحظه لغو شد؟ یا مسئله‌ای دیگر…
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71694" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71693">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=JMdFAGbOyZEIADAxL8G5NWiHyV-wC6NVNai7XscZsfoH5OzuZ0BcDxP_jMG0XFwZXw_J9gWFVzHGPSnvF5IsUfC5iCp2r1k-8aD96xw8Q4SuodprsCA0yU_Zr57mvJ4WGhXHrEDmEjzwAOg6LlByxBS5XmL-JyPoB0Qdm2u-c7t3mNnZg_WYyJbe4mFoKVSWyUPgLaw0GMKyrOQMtXVWxT279tj9CUcdP22AT215l0ecSVxNI6PlM8Omsac8dJxn-D0eWjDWl_Wypne-bMe53yOJMf5PnHby8JauLq6yV8g83MHINLs1FIwSBcfMh7bUH7I88L5aZFKrdIf1qo40TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=JMdFAGbOyZEIADAxL8G5NWiHyV-wC6NVNai7XscZsfoH5OzuZ0BcDxP_jMG0XFwZXw_J9gWFVzHGPSnvF5IsUfC5iCp2r1k-8aD96xw8Q4SuodprsCA0yU_Zr57mvJ4WGhXHrEDmEjzwAOg6LlByxBS5XmL-JyPoB0Qdm2u-c7t3mNnZg_WYyJbe4mFoKVSWyUPgLaw0GMKyrOQMtXVWxT279tj9CUcdP22AT215l0ecSVxNI6PlM8Omsac8dJxn-D0eWjDWl_Wypne-bMe53yOJMf5PnHby8JauLq6yV8g83MHINLs1FIwSBcfMh7bUH7I88L5aZFKrdIf1qo40TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سریع‌القلم:
آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات نظامی علیه ایران می‌آیند چه دموکرات ها پیروز شوند چه جمهوری خواهان!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71693" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71692">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71692" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71691">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71691" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71690">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=tZ3tA83XLSNI-y6JKPgg9FQNo8XdKxIQ4Qal76RuPWGVoUycYdQQUZT4J7H38ussbnJGqmZAXCvKb2bV0bLBeN1H0eROGfANRd3-vlEpa0eqQUwF_I8Mq4SrsYW41S6p6-PL_wU3QkEGcqH4DQ7QX_4eWjFLUEeO9IzGqrLMB6YwGDcriTBarmOWOjHWP8GL4zQMX21Mb5aclAvbDH7WE7-xm4a8TL4SQTS0Gc0pKwgxr6POlkdfQz0Qrb1r6N7Qt-uWNCBwYMK7ha5WQ8T6N6rYobOGvq-kfVMbh4svFExbz5p5g8VMjVDkn175TuRbzi84LLKfv9wJHe6mBTM5Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=tZ3tA83XLSNI-y6JKPgg9FQNo8XdKxIQ4Qal76RuPWGVoUycYdQQUZT4J7H38ussbnJGqmZAXCvKb2bV0bLBeN1H0eROGfANRd3-vlEpa0eqQUwF_I8Mq4SrsYW41S6p6-PL_wU3QkEGcqH4DQ7QX_4eWjFLUEeO9IzGqrLMB6YwGDcriTBarmOWOjHWP8GL4zQMX21Mb5aclAvbDH7WE7-xm4a8TL4SQTS0Gc0pKwgxr6POlkdfQz0Qrb1r6N7Qt-uWNCBwYMK7ha5WQ8T6N6rYobOGvq-kfVMbh4svFExbz5p5g8VMjVDkn175TuRbzi84LLKfv9wJHe6mBTM5Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای جنجالی یه
جنده
: دختری که ادعا می‌کنه باکره‌اس، دقیقا به چی افتخار می‌کنه؟
تو قطعا ایراد داری، مگه میشه یه نفر با کسی رابطه نداشته باشه؟ آقایون حتی توی سوراخ موش هم فرو میکنن، اونوقت تورو نکردن!؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71690" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71689">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=ORQKa8CXMwKkvwH4rrKoY0RDdT5c5WmC7XLVvWba4NByWwFVpkxzlpjna6tIAXO-TKeLE65gA9DhHGvz49ZCqwKICBrzzwwlGo9prstSO_lfG3knRY0odwvmnYoAy-4UrNjDZVaKhqW9C0Lu0SCj5iMCM6lUDGSZTFWSewDdwIKBRI7bTMgCyR53tWzPK4ZmbU4hfph06qEAhWxwvDldgIsdALmrfZI0f2Z_ia-nQdpKSewY2aLzuhYYSbudE6vSorbWchv5hfoucxOWkWzDkzCSGOTZZ2tp5zzJrO2T44ddBmVlztJASEvJRzRIhXFkIIa4U9Gdmvpu5n_cxqqtdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=ORQKa8CXMwKkvwH4rrKoY0RDdT5c5WmC7XLVvWba4NByWwFVpkxzlpjna6tIAXO-TKeLE65gA9DhHGvz49ZCqwKICBrzzwwlGo9prstSO_lfG3knRY0odwvmnYoAy-4UrNjDZVaKhqW9C0Lu0SCj5iMCM6lUDGSZTFWSewDdwIKBRI7bTMgCyR53tWzPK4ZmbU4hfph06qEAhWxwvDldgIsdALmrfZI0f2Z_ia-nQdpKSewY2aLzuhYYSbudE6vSorbWchv5hfoucxOWkWzDkzCSGOTZZ2tp5zzJrO2T44ddBmVlztJASEvJRzRIhXFkIIa4U9Gdmvpu5n_cxqqtdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی ایران یه تور راه اندازی شده به اسم «هیلینگ آب دریا» ، این شکلیه که میرین کنار ساحل و تا جایی که میتونین باید گریه کنین.
برای شرکت در این تور هم میلیونی باید پول بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71689" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71688">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان با انتشار بیانیه‌ای مشترک، برای(فردا) روز چهارشنبه ۲۵ شهریور ۱۴۰۵ (۱۶ سپتامبر ۲۰۲۶) فراخوان اعتصاب عمومی صادر کرده است. این فراخوان هم‌زمان با چهارمین سالگرد ژینا (مهسا) امینی و آغاز اعتراضات «زن، زندگی، آزادی» اعلام شده است.
در این بیانیه از بازاریان، اصناف، کارگران و دیگر اقشار جامعه خواسته شده است با تعطیلی مغازه‌ها و بازارها و خودداری از حضور در محل کار، در این اعتصاب مشارکت کنند. صادرکنندگان فراخوان، وضعیت اقتصادی، فقر، گرانی، بیکاری و همچنین آنچه تشدید فشارهای امنیتی و صدور احکام سنگین می‌دانند را از دلایل این اقدام عنوان کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71688" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71687">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265561794f.mp4?token=DJoELyzuyZOqnVvxalKe8KZKzeIXN-4gJoQNsBoJtIoZ1taFqzqyqZmSlNqQEyriq_VEDn92O6sBaC2RuvN1RBXX_qWjJsy8bdQ2LwnnzGoM6js_fP9FeV-W68LQ1qei08uXJVKLIgjU7bPu1ZyiZB2RAIBNkmMWeFFabFfqlchne_ILyYCyMx5RADnATYrSKRqJkTz4b_bnO9k6HcGcSsi8o2ZTMGk07bwEOWo481f_NgNWc8SzUPFRfk1rX1RN1C7Qk8yXMtiN986PA7CAQHErjIbjK46oGNTUKL4kY-5MokESYctBygdC9kyKsZMeFWvqqnREq-ep4AVl_FPJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265561794f.mp4?token=DJoELyzuyZOqnVvxalKe8KZKzeIXN-4gJoQNsBoJtIoZ1taFqzqyqZmSlNqQEyriq_VEDn92O6sBaC2RuvN1RBXX_qWjJsy8bdQ2LwnnzGoM6js_fP9FeV-W68LQ1qei08uXJVKLIgjU7bPu1ZyiZB2RAIBNkmMWeFFabFfqlchne_ILyYCyMx5RADnATYrSKRqJkTz4b_bnO9k6HcGcSsi8o2ZTMGk07bwEOWo481f_NgNWc8SzUPFRfk1rX1RN1C7Qk8yXMtiN986PA7CAQHErjIbjK46oGNTUKL4kY-5MokESYctBygdC9kyKsZMeFWvqqnREq-ep4AVl_FPJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی سخنگوی دولت :
امیدواریم نیازی به تغییر سهمیه‌های اول و دوم بنزین نداشته باشیم؛ ولی اگه بخواهیم گرون یا کمش کنیم حتما شما مردم را در جریان خواهیم گذاشت و بدون اطلاع‌رسانی کاری نمیکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71687" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71686">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شنیده شدن صدای دو انفجار از سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71686" target="_blank">📅 21:34 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
