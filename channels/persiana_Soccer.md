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
<img src="https://cdn4.telesco.pe/file/Lsv8vrJmWs7dCo4aRLyxfGyVD5RW8iMEp4i_borQ2Ow2SZBPiVGjf1v7ohb_dH81uHeMt0nH5ED9BoHADVlz68eo6Zdn5-sTrmRgUZ5qwQSn8iN5Qo0rxCaVYWC2Ass1mlWo1wAV_on2AE9gpmdl0KhtnjZQZBQUeKOSSTfAk_cTenZLT-Lu7BwfLxYO_heU9D0s6xt_EGcVSTuZIdWJyxhpSuLZrMFB1_bSpQBf5sMeODEfQCoKW7OphKUkzuy4kyCL58NJAonai93wkfIp1RAayTmb-3re09CV3uprefRQHlI2ZP-yJONn1KZdkmJXSXM0NK6EXKWhuXBFJajCqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 07:35:57</div>
<hr>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1n-XJRAuopI_ppvWLDhKXCjYXG228IvBK0gsv-KiT0Tz9AgKQRNqgEevCT0mEaD4GWMQQFwFE4uJXl-IxzPdrnoZzBmoo8aYgmicw22rf3UTq98aslbcUesXgOMzsY67oVK6SMMBBn25zI6ZpPrPUqSo1wtVhIaRHwXllb_nq3eMYKk2Ghv-631H_e36OvmMjETwBhw2tgalizmqgZYveFgdCxr5nwzwuMjOGfBYA3EGhSOLN0alFeNOBQieLh-wPUPlvveyOMr9wxloW6vM6XCNdpLECU3qy-zeM6YuWEUn89HZYkHpoAbO2-HE1_Awru3iAubdKd0isMFOVFS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMbFNnOY13US0MfjIzLB7zS-y7MHt8TYpTeRzA2HaGS00IG1Dn6bd4T3-rpH3oL3HA5xQk1OVK__0lyPFf8HtaD85Df1RrboB2vVd_dlrgOfN_y8zheNo5kXCMgmABz722B-YFGq5l0tgPtAG_CAgiZXhGvk3LDfReQpAOlU2TN_UIIPLRE7wAQMOpe0e6aTE_KsXI6y4xX0cgIZ2EjzsjkfZAGf1OuLlKP4hp2O7IqGOlk6YTtqpJb3acYueAI91JZr1NsU1HLpNqhB-WlHOypOjp7iIt8P3QHZkh3qTHoOPk5ClUZ23_XcdcykYPPVeG21afyrOgPkLel5KiiSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo6tGIHDxDZQiOXSYa615zf-EcBUpgOUXisVB6aTyGIRUZ12XDDyh00ddMmGYov6iNP9qAf9nRuAjNgJwzwHFSlE-tFfnq_yHfhQ-wJ3syn15H1ap8J2Ezb1laMuSOJCkmXQhiNYR3ST6hAG2zNDViyj2rj2e0X6her6ucN2jJBjt8lBCHPxbh4iwt1TjykoPGzqcgNqvJq7nH3kKqNUDTt9Mn6b5CVqvTVcL89gqvbR1_IYiyHwPb-B0ThkP23bgSnOjapSeD_2uI2MvpFO8QCQrYNjJ-5KZvz5cw8RQ_rbv3-Ry6-yfDt7BXlnCdNl22vDTF2g-_vnWwBaSRki8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTfYhERNlQo_48JnGMB38Ym4LHr9uIRfnv2_GgTXVUsNL5WXgpojte5LPg-TcbXcz8Yu6bnddbBdU3YWAI6Oid1w7i8p-XRZiLv6oOTxlPUEVZXHRoDfFOPDARkOhTxKN71kXcX4XtgsdE3OLtJyAQkV0OlRuKilnTjH3Pgfm8RCsUzhK2V_D_sJmefa07HA5ffR2jFOLj5E3mNqpIaIoCX00-hPwBGlxlN0aqPzeWh4vg1XdEAV6Rn0K7Fux3y7ChtV9wmO-iA6pK5YMLQ1cjYckjsJHPq5KbyJwpJ0XX5gjSL3IpsIYXs3rChlSCuFttHSCJCr6kOZ8j2-fEpU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgpAVBh-87OYR1chUbEVnFbpPZcRQFgEcE6CSWIaCIOUSPLRtefAUR-SvCVrt2wZ4_VtRSoyVQQJ1COeMi_DpfZloMeKEC0hWwMD3jUbEHnvIEO5Lmf3mmFWdvw1jnZeprgzPshO7eGGXsLDanrJey5Dl-hNs28GzSFyCQfJX-Ec6FXEmWZXoCtIHkaQYWWRGXNr12r0F0IhjBT73uMMLEGM1vepmk6jJg-JL4XaFzQOHo6vIZmVX4OSZnk-t87cIjseAvD4LiaGKhc9J8WrJdK3H5X5DphVXZhAbsgjarmsAAEcM6i_9D00u3ttWEtBF_EnL2-IKmSNSr2Wu5JSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGl8ew9Rk4J5Lx_WTE1-mu6oUbto7fYiyLkrhaVNmSLUeeVVNFG_b9z3R62PNw_DPlicmpW5srvAnxjP3rhEQE_EEV0RbBAp6Deo9P1mHzTpzGDoaMAuNWUFBcCWe5Oq8kqiuA2vJeYPkpZsFlkhgFa5dKBlXzQPY9Wra_ZdzbBfj5SJaVrNBtF_IEEUuCILUoz3TO393ASw8VngQ6LwjQBQVPvA6GXmexw4JJRTVJgFQpq-W3pQ8XT2WsvOaGwBEByjsAoYjvHiDmc5Bh-WrT04hXnYWGr_Rd5-Ii0g404e56awWO5SskJ6T-Uu11gQde4L1-QkvPuPVcvvlgY8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=LuNLHSrlGAzNL2qQLjkN4e8UzpyP092VXYSKLXOD8a9npJe6hqL8tYE6oLE0lDD5BSuYnE9t1fP0fng3fQv7LUU8HTlv-nA4al0reHA9ZviCqoIsSnLb0FycRbAx8FrtAas3zN5UKG8G0UhxBO20sh9M7PZNb9V7J6mhz-32gBi_aHp1JF4vf1X_lSnbQPFG6_eZz9M9Kkyd_x8Jlstcbrf4lNKejtVJgR4YlmE5UAfkQkQvLFNN71Na-4p_ygpt-iVtLJnaTRR9a9p-H1hN4G36XbEdGMsD50lwRpKkFyctKiuisA39c2VJtisymok78eyLieqJSg8gW1C9itdEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=LuNLHSrlGAzNL2qQLjkN4e8UzpyP092VXYSKLXOD8a9npJe6hqL8tYE6oLE0lDD5BSuYnE9t1fP0fng3fQv7LUU8HTlv-nA4al0reHA9ZviCqoIsSnLb0FycRbAx8FrtAas3zN5UKG8G0UhxBO20sh9M7PZNb9V7J6mhz-32gBi_aHp1JF4vf1X_lSnbQPFG6_eZz9M9Kkyd_x8Jlstcbrf4lNKejtVJgR4YlmE5UAfkQkQvLFNN71Na-4p_ygpt-iVtLJnaTRR9a9p-H1hN4G36XbEdGMsD50lwRpKkFyctKiuisA39c2VJtisymok78eyLieqJSg8gW1C9itdEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHS4rvmJfRl7jof41BZFKruyPpaqsTLB3m_Y16fLRfMNjBSs5PoZmJXdu577RHyaJyU9LqR-jyWCuYeczOoSALF5zti3LFO4GlWAmXn-8PvJPR2SotJwd1XQrRr9NCku_gIf2OpfJ1j8jjf3okw50rJ2iTL5i2wHokVHKUUcTZMqt8Clw8DiX15zXz2j8J7HG-tMmwt_fwMIxpvuUpgRwNyjVRs97rxhHb0BKF4MWfEET3WyroUN3spqkGNIZU40GP7jxmKOfJSmR3h_bASkjb2CQSut_QHlfGxs_AWjXBIDb32KNsV3ZpeifUvSezzoD-GueUumsAMLTPEzvr_5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=G-FH7JjGQzz1z1I97Lfl1TEOdXN782WVrx8GbKWrVmkxF0X_3xk7zFdscrngU720qWydlUkT8gDkE5xdCjhMxqB-lwmxXfXN303TrRph8qxbP7EscJ67MlYODUgHw7L5WdhT6YQI5CRNaXiCiPv8diFNBr4ckjlYC3mEYce8ijGxRp3yAo4j9k1F5P1ZT9ufLSl6yrIHjpwP_e3LCNt8ElvwSQ9uJQFegWcjYq_iR_NCHDURTlI19apSxUPWFJe6cqsPHXRUtuYSfxTYrx65LeqLZq_q40nAu_XNr-LytOtBhwpmSwWP_SFTqB-QdyOuMCAGkuADAVGS7r2JRs875Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=G-FH7JjGQzz1z1I97Lfl1TEOdXN782WVrx8GbKWrVmkxF0X_3xk7zFdscrngU720qWydlUkT8gDkE5xdCjhMxqB-lwmxXfXN303TrRph8qxbP7EscJ67MlYODUgHw7L5WdhT6YQI5CRNaXiCiPv8diFNBr4ckjlYC3mEYce8ijGxRp3yAo4j9k1F5P1ZT9ufLSl6yrIHjpwP_e3LCNt8ElvwSQ9uJQFegWcjYq_iR_NCHDURTlI19apSxUPWFJe6cqsPHXRUtuYSfxTYrx65LeqLZq_q40nAu_XNr-LytOtBhwpmSwWP_SFTqB-QdyOuMCAGkuADAVGS7r2JRs875Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22797">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=HsKRXswtuaJC77B6MNYnDC8EDUNuQsX_7nw-7CGK1qkOwMN075XHqP7OTZVSXTN3xihpk7s4AipaeV8hLiK4uRV8i4ylpdfw7jKm1psAhEGPbyNxLZCMi7gmK1EAp7CA0dOVpHtIMQIQX-ixmHY5t648cJ7UKtkptKx8w9-D4VbFe1nz_TDUbJZMXwBWUlbr8-HeWgP9BjmZPYvOiwGlv2pt53TV4XfJg8cv6VbAEaW5A7ViChSfx2M9EersdxKyWoJrDmYmDB7BrNsXx7NlEh2JDemEeFk1I1ok3I_s36bs-fQUob13TYZuy5JwdkNNQWhaprJ__QrqTYddTOcYxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=HsKRXswtuaJC77B6MNYnDC8EDUNuQsX_7nw-7CGK1qkOwMN075XHqP7OTZVSXTN3xihpk7s4AipaeV8hLiK4uRV8i4ylpdfw7jKm1psAhEGPbyNxLZCMi7gmK1EAp7CA0dOVpHtIMQIQX-ixmHY5t648cJ7UKtkptKx8w9-D4VbFe1nz_TDUbJZMXwBWUlbr8-HeWgP9BjmZPYvOiwGlv2pt53TV4XfJg8cv6VbAEaW5A7ViChSfx2M9EersdxKyWoJrDmYmDB7BrNsXx7NlEh2JDemEeFk1I1ok3I_s36bs-fQUob13TYZuy5JwdkNNQWhaprJ__QrqTYddTOcYxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ‌توم‌دوس‌داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال‌کازینوشبانه‌راهی‌برای چند برابر کردن سرمایت
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e14
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/22797" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqOKxXa9wVQV4jUaplZZcwONtW9a7Ur6MNCPFdrxdhyfpMYy7a6jQ-CT10f71aM1-5__OA-F5asQvS75EJHHTbLuIDjvVm3GC55zslo76iEueqZywbznTpsU2xEWbl1gHbkShPrcDzXAPzKeYdatq60Bc1UUPxiTc33yaqmNHXiOUUkKzFLIi_Y9IQ7riahW1ylpj8GXe031mmZkbxYZ4n-zaHXhj3JyAd-V1iR5on0dyPSszqzl534GAUFBvdsNfmSb-Z1UtDYddp-PEgZU6fiNWIv-HQuOIHFA0o2Q9Xz_YQBEUetJ48L2inUqOfFvQ3yXL82UAFDE_h7PMnq2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PosK5uF_ZQgheceuU1eNpupBbz-rN2axQMTgkCFPch0yNjCXTdwwfn38cRBXDER2cUp6VuY-gzBghl-F7IbesyCl-tHMa5WY5vELpAAXqy4j08RYoAWZ4Hq_5XK9nad_R0t7XZ4_s4YJu8pFDHvutuibOm06DLFfMDJPNsxzZvYZ6pOqVdT7Uv-kLfG5Tu1BQqyA6oKX2DivxxJDjx5sfbQ2NUqZFgJgNjdXNs6F1KYtNA-7PklcMKP5cRNcjhhfTLv_f7FjzG2TkGfeYGX_et5hKDd5dhb6DR5Iea-IiHNsyPU-_3SDKVqUfLcI_QFbY8oHMHCZTHd_-nygN0cswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRwKK7UQD571U1lMhehBKOQiGQtOaLMioaLHVRd2iC2IbwtdPShBIUQQfxMuqCF5hxwK2c9-9QjWcDBItzSj_0WK_yxxO-eLwAyvNDbF6ATRchsjSGluA63g4lfmX21B43323H69AELVH1_UJ6kOPPnQx3HJtOOaFvvqjfvJKD7aMJVJ4FjkX-i0UY2IGNadiJqEIY8Q3J_DC0CUZ4hB6dxXaQuU3EJhBfoox5xbaAXmarqbxMt_XmUJOHWfBIsB-Q0fUFPmTBdFynqbyquQ2UHU_2lRmwIzTP1H5HWe_-boGC2ApXl_RKB3uN7d2e92sy1eQP81WSxdSkbst9bo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAalfEhbCeZ6i9ow-fkBBew_WLd_f5iZuAzAOkbsXESrDqUua7QJaYIUfavLyCmT858iaL55ZXG7ceeG5jIhoCUDuqFAYGwA913isF0OY4PQMuoGmapX0niz8V81PsPOPY8sJIPn0883VZB7pwm87LdI4QukPDRDhP_sQRApA7IdP9aQVxL0BRABVQIbYqy3L1m8jUF9q5Xeh1uNr0hmJrdnzQpFRY7w1ukGW737G8OBJCFmu-9OorVhRVBZwDEnaU33-AULKjdnjn0Lky1YdAPOfCfX5Mr5KkPA-ot4o2gh3ano4yIlwXudMn93zsv5wBIn2fk-0rfZVPhWOo_94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hV_xgvh28yPofX3yn8KECmBMd0R7i5_FUEhBKual_6jzpIxBDBBRts5OQ_uOsGZz4KMse4YtNbUS7r7vhxS_nz1-m6zEsKzP36p3nxrLcj1aYppp4Kgevi6f1j-AvtRqR4i2QkCZ8OdkKXWKLK4fw71Ypy27L15_wmF8YJiX4Mh8anKpKm7uKCI_fMetXLapd3lkXZI2FVl7CK1x6nU5vhnqyszIknI2zk-u_5ibUsjg4wJrTag9LcvZlQVLmvaUwdAWU1YZKN2z37Q_yQHmlbn47CJsAPZFt__zdw1BPUT3GhFg0P1ZaZAqOIUQM_8hOvjj3hDj28UbWXSCJY9ofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/psAJW9UY_zIOVe75PNnVDHD0dM8yBterz2emVX3awoO94GlrYW65dRpZ1C9NnS__FX6HYuZir52UZLGvsgtFvNiZtyS7-74aMfZoRUQmRi4JhC7El-wG7nNYM-FWjVN4c4s9J5ipC7bWQn-hiXEYpZjXpRVm-0ZdRhbV6Ekat0sGsW9UfAo8h4rf3QmLoc1wa31T7lcrbN8Fq1RoMt0mfSgOfg54-W6KFTkWZAIwKEswdeR-yqqWiGAaFxwZtGnTCE_-RMm8fI0Y8Aq9rI9GSu0Ta2z3pwONpfHCYp0lq3-qiEy4YA5DBm7twE6ShfOjuRvbKde4Ry0MY7yoxIw0cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=RyR-qQjJ0AmS0k5i4KubuOEbd-R6B7HUjXeazwl2MmTeOYv8a0nvlxBUtKfcorHlnsQqN5C9ZfBwXsssOd_3BMI-IHTMgHC855grjrZU7LmjS3jcN-mjNayWo2_FT40-6DfrRtPac9ouT0SAT6FqhCz3IIoGyMCJQg2LkpME5JjjFFzG0zQCbFn_RZUHHZWqBjmeXNxKjeYWAkGJkLT0l5kBJkasfol_d4Or8WH905KLPpycyQQelDfMvZrDm62LOX-ibK3RQ995WUTle7iCIvJ-MCe7GrJzOEMMzVkIBPYzPEJ5MpMD4VGg2Q42iuLqTqkFfptozD-pISVRzcNRcK6M_DLWexg4rakRLAiTqoNu1KKGuaKitGc-THj3lEkNAhgPv5Z6sveTNF_vOu9q5WQb6txuK5-1qlMy16pWCIFtFyaxk0Ep7X7x19qLpFyYQU-AmbW-FSbfimW7pEkJ9EQ42vPdZeegQCeLyDoonDIAsZoEDzgLPIYr7izJ645hYDHLEdq9J5z8TCt65Qtb_PzWcFbcIxadm1Cz2vkR1V3tZ8XEGyzty2Svh4qGx6UtY2PcnYfF-n16WLM7pWMJe1ZddOgw8SQtoC2NCzwjDk842G9-Kz6mRXcIUjmkaJj7VOktkJuaP-ALtXTHd5sSPYNlM-0JuuTzyov5EW103bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=RyR-qQjJ0AmS0k5i4KubuOEbd-R6B7HUjXeazwl2MmTeOYv8a0nvlxBUtKfcorHlnsQqN5C9ZfBwXsssOd_3BMI-IHTMgHC855grjrZU7LmjS3jcN-mjNayWo2_FT40-6DfrRtPac9ouT0SAT6FqhCz3IIoGyMCJQg2LkpME5JjjFFzG0zQCbFn_RZUHHZWqBjmeXNxKjeYWAkGJkLT0l5kBJkasfol_d4Or8WH905KLPpycyQQelDfMvZrDm62LOX-ibK3RQ995WUTle7iCIvJ-MCe7GrJzOEMMzVkIBPYzPEJ5MpMD4VGg2Q42iuLqTqkFfptozD-pISVRzcNRcK6M_DLWexg4rakRLAiTqoNu1KKGuaKitGc-THj3lEkNAhgPv5Z6sveTNF_vOu9q5WQb6txuK5-1qlMy16pWCIFtFyaxk0Ep7X7x19qLpFyYQU-AmbW-FSbfimW7pEkJ9EQ42vPdZeegQCeLyDoonDIAsZoEDzgLPIYr7izJ645hYDHLEdq9J5z8TCt65Qtb_PzWcFbcIxadm1Cz2vkR1V3tZ8XEGyzty2Svh4qGx6UtY2PcnYfF-n16WLM7pWMJe1ZddOgw8SQtoC2NCzwjDk842G9-Kz6mRXcIUjmkaJj7VOktkJuaP-ALtXTHd5sSPYNlM-0JuuTzyov5EW103bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=uUpkaqHsKnEz6ybvuMpuMK4DgUesJX2TMa6pRzxjYYsvpE72LwzL58_yxuKzTswZD96nziCoxeYPW8PvIDjm-MSQIki64rtzu7muVRBoTeU7Z_dSaa1MEjIddmRgX36yJ9TRH9dyWCTshF6v5nd-m65obrlwvxofrHtvI6IB0IqqrTlcPt7o6iUXjyrNlXmloTLu3uzI0Yy2TrVYOkR6REXN_AFYZUJPVH6EkvFB8fXne5aGE9rBjx7F-tIL47onVdStRG41vVw_urCEgiZBp9MCdYVCeSriNrtJcm1awlN5dsX2iI6FmxGq2ORoRN-rRa-U4WcEqX6lBUPZonVc_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=uUpkaqHsKnEz6ybvuMpuMK4DgUesJX2TMa6pRzxjYYsvpE72LwzL58_yxuKzTswZD96nziCoxeYPW8PvIDjm-MSQIki64rtzu7muVRBoTeU7Z_dSaa1MEjIddmRgX36yJ9TRH9dyWCTshF6v5nd-m65obrlwvxofrHtvI6IB0IqqrTlcPt7o6iUXjyrNlXmloTLu3uzI0Yy2TrVYOkR6REXN_AFYZUJPVH6EkvFB8fXne5aGE9rBjx7F-tIL47onVdStRG41vVw_urCEgiZBp9MCdYVCeSriNrtJcm1awlN5dsX2iI6FmxGq2ORoRN-rRa-U4WcEqX6lBUPZonVc_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twFbsX-Y5X7TwrYtV1qyNLJ3ve9cn7fBh_kRb7bvjy-AtUqrke_XG0y4SuelruO40CVzeVA80naXUO9HQWFUVB8vn5oPqQTpZA9j9XNfTDlE3p0Af7kxRgKX8iFlBqIzf9irqeYECYSh2VipctJZkUpASMoUg50gjdPDMwxOKpX19Hz22e0IhvUpLE3LfNKmexob2jaRoXPg81duAs_ypCgcPiYSfXRmrtVFlhHpSSQlaDll3JPrdqIETW_6T2OE5eCuJ9xsl1pZiNn4GS3GNtThoy70HxknQIhhIYy5iDQ2oYyfw94bQRWD36QMr2ROp6y6g7jNR2UQiEXvVWPGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdQRm3WVc4YdJ14I6t-KfvFfX0w_vYhUi2SDLGJHHd5He0pgq4obzhNcJQaPkbRaNc2Hn2v8o63KDdEduOkH4XRlOgrHcRm_-fRGe_5vlpJ9dg5XvS3dGknJk8aS2w_uhzZAS4slFIwVfkwZhnXvK47WDMIWH7LYBrb5EG_YeXQa6qwwhSWP0DSdF7W6lFHa4qYYGZKHSfDmPwnwlxUW-b3tIa9CXrV8ZiR5DbllB9Mk8Tt76QyS7no2jESbq6yuCHWlaYnGUuXyZrJCa5OVuWvUw3fDdRNYcsRwPrbbuualtS0SgDz06EB7ZWAgHNp23iaKCjflDi8Ou_XhGHGgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0agdOBIACggOh1nwVXtjoljW7TckiXApYzHLEZ_RFKHckYgklWt7upiHKmaGgyIRvK89C94B8OT9D1zxeTg2lhXKYsb-77c_B1QAUKaqZqESwe6xnGg5x4qTE5ZXqpJtvcfha1sD5NREwwEuk1WLPgqJ8PG4CCZLkFl-pBYh_gUaMOv7fe2I-xRheZJaJhaK3_W9Xtou9HCf5Lk5eF-GtBk5sR63Sg32VtsIRGCP6PaW9z_4f_MEcaSeCfsrUjYUwBzJflnrIIN2YXZCuWlx4w6hEITs7WyhC-wmwbTYs_n6JBUiZAAt3nePVrE3QVdNpBat_4eoHvWbibX6ooUZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZyIzlqugKbMCXbNZE4v8VAXPZHzAmhHMw1KCeD0CY1I1YZ8lxDoZXrpYfELSQt6r-ddhDZto8Dt3XAgF3XUjMNdKJPPFUm8-8vsDIBA_1aHg6i2j--It96P6TR9soHTe4kR8JFJ9qsNIT5S07SUcwxauxH1Qv7xk8-ndnp_iRMK-bGZNjspOorOCYkTKHRBGVXDUXY0syIjjZgeE9BCZRU20vHiQR-69VgF0qu19ZCMS5m2AD6t9pwccNKYPZnZnVnSmSDuRoLp6RGh8a6x5UV7B5CLU36z8WE0vhfCvHzy4epkrCmhk_Pq1JGF2owk0kbGgev5aDeMnEAZUJwkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5xIOES4Dl6x47GMbgJsXpJ-7tlnBXNjoaOambanPARKfYWd-5k6WmsoRSe6GN7Bp8KfR2PWbkuSxt9z99xa81hihujBliV1Bt0OTYUnDi59bWnlfN6INyNHy0ITrpJMsN87UryIKBVJGke70cKtKvg1u24ObsSMXNDNhYaTjiKhyamKUWTEOS6EBP9wkzH8z-2bPENOiXq585kb7ts2s1Kie8Y33h9Xr9GnfpNyUhrR_g-dmoaWP5ApmmjjBb_td5F1tGdxwCAekyJ3bxXkpg7L6g3GxuPdRceZuY7WNhvn-gjEyy1I2O02ERuhygwQavsn0X4Kk0fZWp9_-eKC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdQhK1aFOrI1_aZYpaiur8-hN3icgTP8G99c7SufynRcegIkmWRg8askP1Muhp8GAGnB8LTZIWbxiDpb26bnVsHzgpw_m5GIQnA9S5g_UamlUgaJtXU8pH0THTdMtgm4KhHW2PUSe-EG4oI4oEatB8fFlHek8bW7-PV_WOj7ipT-DQyW5CnncTaSxA-D6dmv3FXKzImlAAXCb_KS7PI9tDLI4lzB7zm4lbJhdK1WzSijBQwX6cCSp0F8jcVjGrKSUQQCpy1E3SFJFtD5dHyWPV4Vr1uPlA22cNjniVCrte8TS2_o-RUOxaEYbdDY47sHYLwz5gqevnO0fqU4_u_f-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPmbuE9xgkmQ9SmhDPYzctmTO86Tn-DGvWLlXm2qFuVroATyWk2MjTMOM9h0FVuMm5ASfrZm7VYRavso0MQrUo3Uq9mPlqA8tUnUltuss3KxEgD6p6hcc4P02mTEJBL0mhvWrTGGV8vy6HOMMRLZp8qN7GRjUnVDvb4q2KYbGaPLToYJnN9bqDRcJy7I9mheMF8tEkzHPK48NZdnl4mfyy1CNRDCreMgERDj5c1f8n_xyrozOaJqNbTxJbbCh8_yJdj-nlhbx-DO_o3xc2aVy3I8rlLWmWufqaF23QNFVS3QIUEUn8pN0QtKYNaurefy6EnXDOPZM9uXhw9OxLImkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXWta7Eb7QPokg6GKVPHy0jFojaaEViiDpG3mNZuRHa-nKmA35rFAjOaq4nUIpR141db5DHDEbrqi_gqet0jaPlPesWUHDNv31TdPESYSJ828a98-0Eb4P4OTn0NhrcqUYkssGfcaLjFSOs17UweE1YxAksTKkZ9rnBlBlSRdHBqRrWYpnvE39t4_z3HjqWuXwBO_slNFYCxobPwvvcL8rpARoWYPqtuX7i-V9I0FIDsVjfUdn8tNGntufK1QjlLRzd4OEJhCZ3by7KizDm0BJe3QRZz0DlU5TMJiaN6_NMT-scdVzZYBWGmJk_1vZxepHFdTMKrWb4RYJBuIsvEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrvMj5UeRheQaXP1yU03qA5Yy4_T8NY1H8Q046UuwFjG-wyaoIRKBLh9ZgSV5lWRc6WWzAQjAApS__FSEaE7fn1danME-IaQSgo0ssA_adY-9DPVUCYczVuloJHx63LNFKI9T4g1GiWUOI7cUBp0S6qy3bTHT_VY7eRONPaNF0vC4bpl8i77I83V8Zkrw37FhqNJ2qzjX5bsd-7zUEyIlTFauIfYOs7GHKMWAIbl1qsZGbl07haHP_JMapNku-p7lIl48cAUptj2x-a2efVWCHfxIsPEWX8qr073wmlubPawfZFAxAFxE150bTnEFavto6WWBM4omZp3Jo4Ia8AMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI99qC2c9msHMu9CCE1tkGbA2ci9UxSKqqeAxg5_Y9Ft7xlrE81LDM1QWoR_Aya6irSnFpi5DH5OPwXRypx75nOx9K6tSmakWxaigLMEvH7UtiTsmi5vIGoMMz2B09ggdASfF6wMZOZsMxbsY_UMO1-ZT0_MynEOnyb6uAJtvG19o9gtxu_lCWv_SGxSE66UrbE_YGoy7wQdAz50QMEjITCzC2Ui9BEIv2KE4_8TaD3hoQoy9CFpSMNmxnFn0FLkBJc33FZLY9MFHBIvjOsD16TRX9dAR8urQ9-b4EY7I83AwIt_hsd4yEhEATO3y19jRDnIHPIdmqcOa5W4LELAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22773">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcZR0u8nTo_tmX9BxagFy2VNmiBjC9RuBxOhyPKDYjHq29SRPzw8ek3n_vJWi52HFtWoD3D37rRvJzOwKvuuAZLxxSWvYNBrJVzRhSqSObdzp7g6zepGw6KD595V_BQqHbptD7D0260Z7ukq9GlqUYo5pxIUggHA0U2q9ucxfu_iBR02rbtose9c2ANiz3EptvFn4IWUF4ZHhIgAdGQZsOt3jDBrEO3Ezt6GVa6sHhuT3rIGVUGssgUKt2JxJgJ2go7tF7Oj23xDxK75N5IYYz7h5pWlt7GiHOVjnwn9RBWsqDO3lcXbxFcnPtIa7YvRXueP_rZnygprJ6fCxU_vKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران انواع ووچر و همچین‌انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22773" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=M1lfS6KbeL0vbcKz5HAR1YCW6PMKGvchMeTBm6ancwsf-_q58-WirQeiR3ixXmkF4pxZo-LTNLmDoAsfsYLBFnOBnhCM_lBn0drsATMpBjkCNqluI29xNL0DDf7oJdLRFBT8Pv0yb7Syly0IUIS_NdbNE1KK7mkmau00YCXlgBX6j_T6unpYJto6KN-hROYGr8s8XQPxgZBgPJWZmAzZxfsenogkUVEWlXiG9-BxilbysrpVN39_oEP7xo8CcrXw113INJPdQzfK3hyfwHRvdV7RXhJ6qCcWMlWJvzTozUwrO-SRhEyyV7NXR5WbBnf7x9XgsYZ19o7A6u5sAN64mC8VqF2jV-ocrTsYPUWrB6ysHhoV0Ta3bYtPccbyysI9oh6VblsTGGa9Vzui-PkBtC1Jq2zCGJkE73dqzoIKM6ngRJ8_fD6J2fi1fDx2ypxn7wGKWvDYNMfTfHtQ_X1n2h_JLo_nE41RBLZE4h6U4C-3IEkeCMwoqCDDYPzOZqmBD4PNBXo9CNsLDgxUlqAxDDpRD_dvM3ZxHXyoVhNu-0OpQyMUmrXD0f_-6Q1eaIbYPaehBpx4Z5rvCokSseahykf572qwKbN4v3FmOSQeURRBPpYe1-E8fKWhP3jXbETVeYNG7F44VAjh68NVySJ_NSik_P-UG3nrjvLa7iOa2zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=M1lfS6KbeL0vbcKz5HAR1YCW6PMKGvchMeTBm6ancwsf-_q58-WirQeiR3ixXmkF4pxZo-LTNLmDoAsfsYLBFnOBnhCM_lBn0drsATMpBjkCNqluI29xNL0DDf7oJdLRFBT8Pv0yb7Syly0IUIS_NdbNE1KK7mkmau00YCXlgBX6j_T6unpYJto6KN-hROYGr8s8XQPxgZBgPJWZmAzZxfsenogkUVEWlXiG9-BxilbysrpVN39_oEP7xo8CcrXw113INJPdQzfK3hyfwHRvdV7RXhJ6qCcWMlWJvzTozUwrO-SRhEyyV7NXR5WbBnf7x9XgsYZ19o7A6u5sAN64mC8VqF2jV-ocrTsYPUWrB6ysHhoV0Ta3bYtPccbyysI9oh6VblsTGGa9Vzui-PkBtC1Jq2zCGJkE73dqzoIKM6ngRJ8_fD6J2fi1fDx2ypxn7wGKWvDYNMfTfHtQ_X1n2h_JLo_nE41RBLZE4h6U4C-3IEkeCMwoqCDDYPzOZqmBD4PNBXo9CNsLDgxUlqAxDDpRD_dvM3ZxHXyoVhNu-0OpQyMUmrXD0f_-6Q1eaIbYPaehBpx4Z5rvCokSseahykf572qwKbN4v3FmOSQeURRBPpYe1-E8fKWhP3jXbETVeYNG7F44VAjh68NVySJ_NSik_P-UG3nrjvLa7iOa2zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwGUspRx7xEsO2AjvO_frLWkiKG0m0tul-Au72gagZ0Md-uY1rcahjISIbhQ4i_8r9kR_CK6oBHAMr0SYd_vDMjNJYadOUF3wNgOiJ3uk3zH1ZtUGvA5ra8YfLbK67_pCGbrxXebPsl9Lh27gOYDfxtFPCdEdQmTT47Xl_Avwnp11PTJHkZXsbMuaLOPv-c3swkyNMotaL6i5HJz5WgEi8OeugaAZzwQiPHcgrsH4vzrxtoZMwHLnHlvUmfmxy7ZMo3Cee4YGpG8OjpfEP8WKt0lvES8fD8xilGdxv6jRCpZRrwY30Fh1Pj0GYUB37Z5_HM_pMwCw-bAAoENDmc3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQmt-KCO99QsYt_WmYdsrBwjF0-j-bD7h1X9xav2-dWOnVkTmIN-91HW0Jet9k5DH-4gV7tOKKFLCOUQjRqxKtIZA3t01hSmZehjl_nV8fIOlcGni8kQqFh2Gl4PJtEpnjon2WHlhj9wNqE-Nf7R4-ckYn6rTuhaJHWhDi8U5sQCmNqX_AfLbIEPS6OS4Pc47KX4timMLCxczETCZgo2zkqxacVgiS7vodBMHPbNlE1c5HS3u7F_RxOpp1TdUFAZF11LXYD9rsPS0BBa4BEf4RF-MEhXZ3SQcgOP19DtFq-K5xedweyQDm46L_Q3eHzCl8xKKJU9tKovM-EZ8xGXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brajad58XsQu_voyhH4E0enBj8jp34PbnLK_fB1qV6U5aHOeHZ5x9sL7tHVPxNk5JYdTn6aIF9JEAb6KBWruy2RErIyEQSrvMK9pYH28UqHjwh2ezo0Tg5qNlQ_p1uZgpVeK9r-tHKtZUS7Yff5fRq3O32mTsoqyLX7vT81G20A7X0EIvh02bboOgHcTVTqZKJKf9XWnth4ZLUd8HQlggUMwRlEcdeMA9mRe_ccVeXIAIay8Ryxb8obVHHxU5pUHxOPQU4nfxc-ue5cdewj-zioP9QWp1DrlRnrj_Lzj6RUSxij9-ChNRjB-mWNEgcsdsjq6xmilKBlJ3QuRSHs-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3QuBfFAldHVQbNf-cNoQEqhmeD1PyhX4cBMUgmqzF5vM4cUpgK4vQtr0XqsH5FBwefbEPWWM7dUpjkFb5fGZ3vOihQ-8RHKdvBmJJ6zoYTgtb-dwGgjeWNUhOMLwcG9BN1fSd5WHVzmMV7uxYGmEXNNX2xMxTZFu0RthBtt6QpgKr-0x-_L7sRFvDQMo2YwyCx3G1cnRwBXRmnhJ32pDx8ykFseFxgsO38at67VueOfLY8Er71ZJba_eq47EMg-6t-vxDQhxIIGZarPqo_OFVykMH7dvtAYU8aWygHFaXSsM9qfbqGapxAUwmZDxyHcsrzXzTX7fq2jTwgPDhn-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCcO3RAWfbm7nd2K6_1nzAyJiT__4qQWedLxb3MUXkVoqP8RFnoRCip8kpXpxk62B12uQwm8p5qZO_FdTu-ARPnY88UeMgr7UW-IN6flcXoMHH85RYN84o4aYMroXBpqt8NgSPNsnHEYkrKOn71zDOhaZd4QwAH7Q7BlmK4MwGWm_Smmsi0z9BTkHuHTENFQuChbcIMVWcX5VncTat_QRl72isBjejxBr3vMRTpFA2zCQcUyLNpATNBf7NiJCwMMt_h8jqF3cO04N0Rhk7OjAYFeROft54mAzzoWVftyZ-KbxjBQlqBKTuQ0b6uGmttsCJGAv0GSTyyuKPnwRwfqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qshhBdHY3mFxrS-O2739Y_OhYUiuLZY3FRpCqklgSXIybw5xz8K_e7FhUZ0_i3ucA16bpyKcrjZg4oGLCDp_YIcAB4F57dtBV2PBsv2umuoyo6YYOZinQ-mjMMhENhKeDfmBh0fQNmXXTKlHvGEyEWRLfmDF1uHjCeczpacvStLfpccUQmRLfAxpZ_l_mf_QFMW_DPBh4BCGILLlxeLBw7AUNVLOPbqTor0PgGNRqdcbg3jrK4MZFSVmIzHYLFLZl4Cu4_3bTEcW-B07h7HnF5JmHw0_R2r_0wC1MEIgnku8LP3NHDAfeFVAvk3mep6Z8OSyLMhw6fUDr3bNNANkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfz4f4t4DzjCgZUg5KeRigDH98eKpVbrJBLnw8UvSrY1P01n0R1BQaoAUTVSsrebEhxrfyDhwoANTN0Bx7pfpE1UVepLQo58e5mSiQjuX-uodTFexnpoU-xkDoivrfVeYpM1wXSGmRvHzEEdAXRfJVY__S68j1876WANvKI8Caz1HS36yGM1n5_ASBmAzpp_Fsu656jVk53665T4KTVYeLhtiCzBny3dRPmf8k-oGjpF0vP2ZYzzUoX1UzqwA6MA-H3Z5DEss-G6hG_HSuLoFXKRB872f-lgiv3bzsW6PkDxoZFOPQVryN65QZ5H4zuZY7yUkjXkbaeij4vJY-Mf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIAEKaB1mjieFwWFxBrk3KIfAXkg0GZiqAd6A4I1B_cRW9kMvz_Lo6v-yCxWNBcB9jsNNppwoThbwKHFO_VD1LGru8EyunuQGwSREBKj-mW7Ry4jBi9zEYNl_4TMVLBDPUAJT69LUzssqm_pzXEFG4fOrUprzwRSeG7ChFqptdLmV5P960_FxsT_C4-Yk9i0hv34QfD-ge9NOmjDNsqMCD3mkMQsZEDST1xG6GawKzj2TLcMGQpKzkSfQBqVLFTTUR6gllNSsuqyeRoxSz-dANwmpZDvfBe2y3ppShEJzG5ZggtF4OWexE8k-5Ohiacj-gbw6hkgEYQYiDjEN5N19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOu8OMdz0qxfI2BzwErKVqeIkdOJrx8aHzWK5oYtHTjLtWZgDGjqtTaWhkX8Ww6-ZIcFhtou7XOONyRu2YYay4kOcn4DtqaoVUKBqsrvudNRsuLmZi6-S8jTQtk9np3EZfc6-dIYht8t1XUKtfIWGXTScnPQIU_3kj_crtjb2WPIJrw9g9Hp4mNxceoRb53zIAaFFdAzmB_8cr0W6bJ00ANyq_atSEnD9JEHnza6ubfR51YWiAlPR0sXc6S1eaIU4dtEY5wuPn0ti7EtEAEd6RAcCm9mUoMTTpVgS8kZo770-Ypp35ea55nH0yV1ueo-bMLHgF4LQFNfe1jB5pSurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paQefPXpLi_DJ_VShruhok2SiixZn5SB6c_A3hLVGzKUuo0FZ5vf_U7Wf2JxdK73PYqy-GzMLTvoa7N3PLPwmjyDPo_980OUvs6DCnK6LmkKUmjr6yrk9aR8b1cDWdvr1A44p8L8saxS0Yb1ajD_UGD-zKadiEGNGDX3wML6db7vU8iqBir1DTJ23tom5317IO1Ov2-j4znzyocNaiKf4_rL5akctJFhh-id8cJDZHFiYHC-GMzNxvlY3GcOM47JbYqxscGub34Vu6ePOh39B1LPnH-H9Pl7RyGr8_4yYoAowS1BUX_hS6So3nUJJPeQv4UV8yr8hurkf9ECgNZ46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq7LYMQocxOc70i3sJUxL9pADSFV6n3af3UHKqpjF_jlQhPrzC7GcXReuhPEGRGfgUqCW9uREaeYre3vlGWD9LNys_RFSW0hJpTXuSBhgU0_nYRHejmUKCKV9rGvHk3F7kr08w2-B2a9QcoAmApLLSDtQlOyvYZHlkMCIoAEPq_H8ib0_hN8wuDzk5TyP7YVQz0r4FQ2Jws_52lhmhRJ4E83DlokbkYgZh2xVXXwjlVmfK11JHzJOo0ILDPoNKOZhpePWJNLsLtk4ekPMJj4aufA4zf7p6qT2d9QWNepaI1EJh5jTliAeBRUCur6YrO6Hi-6Ppjr905cmSIaHaTh1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=SSRDPrSKMTJMNG9UKv8qKP86sNO7pr3Wi_OlGZtbDd5M0itvm0RT-SPP3X36eWxRqtoVdBF_82YO7LXLXTuxnbwKyxVuLrayy_pIQNsgTP87l8kLv1sH8AZHoxL-FUwHk1sz2SL3Z7xPCsBAv6zp5rDO6gzGa_PQBQClP3EVyIY9-lEkY3S__d3lnKZWlwc_UWeQNjTj2cdEeQYuRhP_51DhZGF5i1h9uOT1wumXKZC7xQmwJuXMvPmfyBL-0uRLbshMFEexRiWR1RzFzVP3GtOVhnPPNocGfGCOJo3dcDOD0Yrb6ciymFNEiGD7NM2tpBBXqIGkkzGgQZApoPyBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=SSRDPrSKMTJMNG9UKv8qKP86sNO7pr3Wi_OlGZtbDd5M0itvm0RT-SPP3X36eWxRqtoVdBF_82YO7LXLXTuxnbwKyxVuLrayy_pIQNsgTP87l8kLv1sH8AZHoxL-FUwHk1sz2SL3Z7xPCsBAv6zp5rDO6gzGa_PQBQClP3EVyIY9-lEkY3S__d3lnKZWlwc_UWeQNjTj2cdEeQYuRhP_51DhZGF5i1h9uOT1wumXKZC7xQmwJuXMvPmfyBL-0uRLbshMFEexRiWR1RzFzVP3GtOVhnPPNocGfGCOJo3dcDOD0Yrb6ciymFNEiGD7NM2tpBBXqIGkkzGgQZApoPyBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJmpjjKFzT_iCyremF3KBOA9OQhkpYObo3EgQ1ePXGfrt-UwIYekxbsm4U2ZY5kuPiwyVtWxrewk9rrprbgO9ydhgPUwhTz9ghAcstrOGFNYsMCpoKJiXAgyhljFzxKHkxdLCYqWG0aH1EpwRVWrEv88sGWkQAKVv5jO8jP1x_9XDteXZf25pRS1KZcSTn_fsKIFjpDYzw_YS_a0vROiY3VeNQ17rHu-JOLa_vMGpXZXkjWctAcbYw3ijc67bblZnBvcuTuIy_249wPLj7WzqX_MjjRQMHDHGA_HET5G2S7j21iFC4WmZ093CzLe4Cpzl4EwyOnJHVicTFY-eszBxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yilym3kdRbeo7VU717Oq2sQcnNUYbB6plHi1kYRNVbEpVbfmlTZRco1zW2EC2MMXLM-UL0WvdOoW2iINeiyuNnGA4tCVVHwuqAbHOdKqzRulqnv7AoJWDOhBFZaEwEuBMhh2eEXlQFjCMz2AnoFW-pOFL7BUdoDLheE41iBe0JQGpA2zxGyM4gn5iVit_T8GU5vnbMY6XQNYfXOPv4QhPCS9yswO5zfdjUjiBEU1QIz1AQ7Zhm2OB-LpCXsaOtmk_GfaNw4lbVi28FdgAkusQoF4k36lgTcS2SUz_PVjr1IBiGoUgasn7smwDlWV5GuBWOKcnaCab5xX0i8VUR3ftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNItFvHPdE6JSCvqL_P06kCpIlCRluIjKDGIX9guaP0_wTztSljJpvFEJ2Zud4Luh_-IDY2QrFB-EL84jHPbm0A4Ug_JvC2llIlqekbknGQmfakViYWq8-Uc84B6Z2h7dwGgzx8yOzXMJttjvcErqNwVTnADukrbaGYWAxyqb_SS3mR2acnMxn-y2vVivnTpaPMDVtgF3FBPAwhtIKdk71MMryxu4hizWAhVqOze4DeG0XL1lk9aZESdhWqFyOMfq-hyDngvZFLkMH8to-PN6Ewwg58xFh88SHqVPgBvyTGGod5xRFypJsKVZEqXkLsE5u46I01CQ9OzfpyhgRwnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=JJAviu3upgsWCkL646UCiUaKDcg5PYBgFClcwpxi6cpVdMGGXt0-IVD4f3YW3oW8gwJGKt7AJTQLHM7OAgonF8Gi0brYK4F8-DYXrn_tYP5t36wQb2b4FOAjbpsJ37W2YMT3drRT4jNQ325dLlcWJLOU8a5VobsO-5BLvjz_O2xeA8ZI5qzK1hxmgd5fPNaK0ZX8SAC4p_pGjlIMOludY_htIhs-97Bxs_5sQ-aXhZahlyyVcp4eionicaSPm-q7awABLTgmNFXumtKER260GFrtN_Q6zNTB3qFU8y7aw8AGF5wS-5Jn3NM60Znll6P4zP4ztEzylek4T7pYzHbZvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=JJAviu3upgsWCkL646UCiUaKDcg5PYBgFClcwpxi6cpVdMGGXt0-IVD4f3YW3oW8gwJGKt7AJTQLHM7OAgonF8Gi0brYK4F8-DYXrn_tYP5t36wQb2b4FOAjbpsJ37W2YMT3drRT4jNQ325dLlcWJLOU8a5VobsO-5BLvjz_O2xeA8ZI5qzK1hxmgd5fPNaK0ZX8SAC4p_pGjlIMOludY_htIhs-97Bxs_5sQ-aXhZahlyyVcp4eionicaSPm-q7awABLTgmNFXumtKER260GFrtN_Q6zNTB3qFU8y7aw8AGF5wS-5Jn3NM60Znll6P4zP4ztEzylek4T7pYzHbZvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl97d0YQ_PIPfn_fyEmHkYhAPKtCYx0vWrAEiqEx2Y6Yrp50_xV5oXJDSHd-qx2CJn7TMkotM8SKbHfzXbCU37NkZOK-i7kzn7vVszffc_MWtSIkHg-TKyQ9tMBfQDNQ8tLHd_80zXuZRg8o0fzDLuy6bDrPmmuJ4DOOakr6iOILXX2wSHgM3o_udpEaHBb8O--_imgNFp8u0Hk8ViWe0AzcgN__-kgjyyDeyEsgxwNI_RPcgFYpfd4zoUleNdTJaF5hXlGICKukT-84Y2ozB0csWKXFIHAkvAmfIG0Zg_5_l16HBXUeMY1TX3ex1ZyK4F3TvX1Lst8xQgMj4n_ZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN-_sjAnTmZ7BlcViTs7ZNNRs9KIoo8BfRHLgyFm-RYxtqoSde9QEtTBnrunIBKBY26pPQQ4XPf0km7PfuKgKKkS_ObHGcjXrJQpIPoh8H2jeRjYLcjLtxf-YzSKXUl5io2Mji3MTbDwnW2v-UmuAitZMvwb8FZbi_oVP4MQQS4MD-iYwnScfi_6sZVVlduTyTj37O370IKR1fFlgrp5ib-yreQlKTnXrp1S00fFmgbuxMjkrZAMFctNeDyW8hClduFpE8NR7aMtlnhA4K-gZmhA9gi49hAR1JsNrIpEW90TXEPOv1kpj9GNVcR_fG-u8oj0oG-_4xNtw3Lc1C3Pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXMTB9J9MYuCGNHmSHefL56kf190g6CM_xFuX4rWDL_2EntlL5bvKvhscshetgxlTwkYEv3YBko7LmPrFk-jXgGu91hJmVIppXBigu-eQWYIrnWUU3eqtvA95xUuHabaXyNVEPL3IvvMEiICidLLS_-O5wuo4tMeQvVecZsy6rqeAA3KIA1HiypcDamEZf0pDAvVa0hg00fGoNqjftBrv4BXjoD6cOLjGgtGN_7IOcco279RdKRqBTMsK5smz9nTHFUWICbADgMil-pH1B6VSadK8eVfw_SYuFIj6l6az-VS7aBwrXtc2ArrvVAdYs13NKbQuUT1k37wgsF2dqBXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7eBRx-XDRjENFLa3uLtzY_Q16QvGOeHFolKooYbZzTntSOvKFLOuXheIjMezjlEk88CPyQR60mqreW6-uY3r7sabMeGrnU3D3peRWVbSTJFmxVyJ14LSvRSqURlKehfjZeBLE4vnEBerSESq3QZlIpipVThEXSnthIzVKxjS6_xTrAoMOhZJ-F7_68JjdyYaDxw_nrUkE2y-gz9ZxQy4wYlU9qh-6XXc3sggJNUdykiGaEMaVk9WaeV0T2hwZ-aVUz6BogkwtvHJ0qRHm9-flrlCijHUCdd9UsxX4e1B0MdtVvmU7qRXhvcUY_b5WwTvx-o-bBd7i9Isryn7tjf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEunpowaXmFZhOO_g7V8iN1hYFeaaD42GpUolSSKST32WMwmTjHP_CnyqjFk9_Ate88HbmX2b0mUcnsfrgFGeAKswyRw05hQQHaZq2pNICBzzLrHqGsdL5_mZngqZEPvq6ynSG0oeQOkq6MmntzTA1p491PoiS3kuB4xUE_MeiyTKWAyUhfbEfnkOAMSShEap--I5jTZZQgDqlut66CvCCCgSfRxlFZz94qa0sBon53rHkPtBZYbGa54TVWagpdt-nuJZqwLLOu_iC7kCavl4XFG7yGpYSBw13KEOF8ny2kkpy6ubADHllj9duJM4TP3UOIhTCWbyhQcBZwoxrUUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkUFCAJ8OFkReQz2ekZUmx13_cHrblricH7gskIq2yZ0wqMRGRhFIoPgmxwQt4IEPaTzvzbEByC28zkRl1gLMEdAGxF8fzUNIkfjnKnKVDbBsh17BWxyGAse98XZhNGoQpH_Er-mJEFJU0b1ykTOW_nwEbkvEiU3Mn4zrRjz6DhYoiY4H4GMG6ew8pdRjNUnwVYYwC1RTCqkYvgKs5xrUeXgI6zCN1ZEukKy3WUcSB9tRkDdq_TW-iTRntDBYtmS5MOsM0ButYVuVu8FvbtZWWZIbHNIYL9YyoaxZ5KXFWbprEErsoubesjBo98KIFx4HO-udfXaT2kNxHx9c7_k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWmin5H0ARKGSMKzWnw2HrV384tZYy87aQzXxt-iKVuvhTyfudCKhg7KS3VxsVL_-rTBbmXf2V8U2wXezqebiXzckIW0hXUFCJ4KOqkL79TRrIaWVVROQiGv_t6XFkYUYJ0DVA566duV2UMfghGCgUbto7OV-naSS_hNJWtkgeNKMlz1DBkZN67kYbL-nm3-IyRGEH070i1-ozftFBsmja-hWzZ0xOi8KzqWg7elDtxFxlIIOYbDcwLz8PLjRvFAjcIjiqOi-ARn0ASsRfBoqm4OSqr8IG_hYsVa__j-iUtmx-6yZw1HIggPXKbbwhk57gXM6cNOy39rjiWs6D6oQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=XVlhyuPknjmxn7FLSeDOf7UknmG3_zxAJjwdceOvbe3_Anf-1cEoi0_uzSuOf1HXCg7GF0NB35PsnljP2UuJijD2-2SdJdwzfm8f3pR3vo6kCmEp2N0LvlYDzKfc7QXVEx8bvjPkX8Kv0hqlgdU3j0CpeWcfhkTY7KsXmohW6l92kftoZ6VGnU_vGJEp18vb82mso3BRtN8Ek_hw_SBePm0Ic_nPgv8rCkDFLO7rZc6E_rn-eyHnI_1rhlNmsB_PnU87ypEP7tS_FcJs5D0Jsfq0YoceZ8dcaeOPOHQwbTVTYfWnGBNV_hh97dPVtt-mGJP4zEe4b4ZvEz69WfWOow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=XVlhyuPknjmxn7FLSeDOf7UknmG3_zxAJjwdceOvbe3_Anf-1cEoi0_uzSuOf1HXCg7GF0NB35PsnljP2UuJijD2-2SdJdwzfm8f3pR3vo6kCmEp2N0LvlYDzKfc7QXVEx8bvjPkX8Kv0hqlgdU3j0CpeWcfhkTY7KsXmohW6l92kftoZ6VGnU_vGJEp18vb82mso3BRtN8Ek_hw_SBePm0Ic_nPgv8rCkDFLO7rZc6E_rn-eyHnI_1rhlNmsB_PnU87ypEP7tS_FcJs5D0Jsfq0YoceZ8dcaeOPOHQwbTVTYfWnGBNV_hh97dPVtt-mGJP4zEe4b4ZvEz69WfWOow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubiVo9fMRBS54zFKlMtvkODjidO6L8294xe4-u5wIx_RqYhfTisI_ApRPWzGqKGZc1wa18NrPHjDRo26Z2SNCl4fB6Oq-lP5UeCcXal3kZQAHUCz8gWRtuUCyQgygP4LE-DOidFmYc2D_PkR0YL-zV6vNzUXXKKBELJ4pXbeqvwluzwh1-8XxXGwxGdfaBFHIpQimtCQwiClEXANIj3abGmZYgtbl_2WxOcL__emD4ernenEk3vdzk3C3pxLz-OWpzkL_ZmumZY_cYkT1kmKkgVEakGiL-psHlFYhtUERF3RYqSja0JCfcP2XOITHZEXJsRT-Pu4jOXST9DysF0QOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4gHin3Fgg273gmVrSXG-pG_nNi2IxvmLEbTT1qfu63Da4rxgu78HzZcwZCD9cyc2j96zFUZ6Q9H-I_0Gim9-lFhgQRfU30RddKOrizZMREbJMNRAq9Yx2dCClXD8jH92kZuSNbPi6Us7_swWUl6yaAvIPpvVdr0gUvOjy0WsII00wK6EZ-BHb7AKCyU-wLBSrFD3-T7OozEOprtCb1poev9Zo-JNWe-s1l3aHf7Gh4nGhFYHrbM-jVWqnSariZo5L0ohLMfFUMUBa33LiiGz5nEnfh8rKNIHZaeGyzI0gyhBHndEyECbnqczxzg1ccMyctvW7x2nuu9ET8BoDpdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVmkeAfssHyy7iwyf6PZP1YJIHlqyU73DUV83YyhGqecHPEZMoy4uKqCNyz9bDIAfnkNdMgnwOUZT4XiAeFKdSJT6iKiarUl_uIrbHOjdUV3Fc62hOphJ9texGSA2SP-okDiosHtmL_jzzl8i3NVYP7xcZrgjmH0SM0P-LObywEv8TywEHE7q21gFIcVs4xsiyUeQ2EipqIjBWCRQxvwzeHNyTwl7l8AUDy--k-OD2ZeUIW1mFy9WkfSD65NJTJwiFt4TLpLTJ7eqq9ar8cmiOENVP8rCiLhjjNG4BjN6UMHg0Ldx8tDefhz1N07qG1RQ1O7xUF6nQUwZCFyKkROkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGXLZ6A8YMtUmEQYGtC6pEu1ietcixFhVnuH5agqw7i5HxddXzRqGBprC0oPyLQHR4lhYyKkYEAIn3SiAkEYSbWPnO_tCvTQMVBAl-upXwEgHPbS5Q-kfkGzIoYeUDGHJSvGXsU1XLAi0_OYnWao4QXFBmHGZ9rIIBZM0k6lWXgk6p7sJuQcd-u3XSUP9wMPT_WtP47SyfvtPycwL1ajp3YQJSYEBEk4EdTknVLpJGCMGxxYCSKZ9j7x4SS-WXZ4gXS1MvqBoeaZOTrGH4yxZuNGncTFAHhCxmkQQF0sjci91U-qUAlXuRGt0TY6MJ3vgE1LIb-EIqv5IykNl8g59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqh8aOIZyOh-w_t1zdEWkwy9A3fl1a6TYg_uQYyMiOYBBg3CqVYgXbYqNDVgW8uaL3WZst5QtlcNs1GuI-azKXnMdjQ5VFnvU-hIuOppQvjyWkGCqQkta8y4-0gqKRFlg9AgsWZvqK33DxxkdyMx_PNIXjKld83fRaaQ07GRIndksq-C1ZTjkOwDLBJjpzIIK2O6NqfRCFFsrfWqBvz8BCXb8slVvZrA-on2m9nFAC1zIAZMEZOv4NGo38WNYGVqDebHP7ueBvrNHXijrdUM55yeUgn8_jPjkipaSpGu5-f765JPkTNI-pk8vXaFUyiQ-nFjq2dMQoBPLKOla1_RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9OXwKtTNkoquoijixDfr4EiCiFaYsSggMil1uDc1PuvwItKeZX7oBTetb9bnzb9Y-ZVqY6Vjy68p463IEy6Eo90nDhgR-YuCUx6fNP0UjCgvm64Jr5FEUzHaS_Yb_nhZVfw8Jv7btojC014mP9jaWeYSFjjBqev85Zs7U_SWnKHJNyRMGJeMClnwT0BvdsytYkaxpj4RBrDLqLIMgZu_w1-GV92ExSKuUkMQJXnlRdFQ6zVLkdrz5tq8C1X6A3mfcfVzvsZ7R4CNeGTrGnl7KOdNez614j00AEQrRWu8BSoiQDSu08jrJIAfJ_nGhY53mir869dqLCxTe3Put4hgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=NS-_nNUPYKf9pIJ5cBKkIbb6MRJ1CWhyD2eymy1cpfXplLYyAwj4tlGGUf0fysDeOncaRzx4OIzHXMnJS5D_4r4qSalx2pVKuQS9X0K2RTiRlRHr3o4NszeF9NNbSBu8KQgK8bj8NiWQosiJWCynXeUKUwAcTGyezJnw4SKBkab3I2XxINL7y09lzfjS7WDHt2qtc1BFSsKqh0kN_qn36gd4H4tAzLjGy-o7jE9uPi5QQzQt9ERnawmLcf5mfOPJ3pvqEXItAwA4BEHTUNlkmi7r0S8DapqtOfiGOZQ34IfCrWr_5GGZhk8zsyuJuAognU0jeThxRC_ON_j4RwA8Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=NS-_nNUPYKf9pIJ5cBKkIbb6MRJ1CWhyD2eymy1cpfXplLYyAwj4tlGGUf0fysDeOncaRzx4OIzHXMnJS5D_4r4qSalx2pVKuQS9X0K2RTiRlRHr3o4NszeF9NNbSBu8KQgK8bj8NiWQosiJWCynXeUKUwAcTGyezJnw4SKBkab3I2XxINL7y09lzfjS7WDHt2qtc1BFSsKqh0kN_qn36gd4H4tAzLjGy-o7jE9uPi5QQzQt9ERnawmLcf5mfOPJ3pvqEXItAwA4BEHTUNlkmi7r0S8DapqtOfiGOZQ34IfCrWr_5GGZhk8zsyuJuAognU0jeThxRC_ON_j4RwA8Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=XUida6J74zNyrBg1YUC7dQyjEmElOTSVvruBCI_8tI795PSucwp9UxSMgwl7X3VFvtKmQyG9mW20AbbhjCp6HA8DzYjxNmB0m0AUoxUAsdOfK6diDClRSX5cCPH3DsRi0VvaKws9xtafid_cdbIYFBaBS73PYyEMULhX7S0dMX2RskCE-011ArOLJNTUxs5EYFuIIokQByfQd5EbCBwIL6kjFOyZ68iq4QoW1pi_3dY0tnOj7C2XWM61K78lwV583QyyPQqpFSup4Qq6s-tUoVMiLdHlIUQL9F-HS5ViiKERNI8favYBQReTdi2PGr20Y_bTVYwOsgW6wlic65GJMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=XUida6J74zNyrBg1YUC7dQyjEmElOTSVvruBCI_8tI795PSucwp9UxSMgwl7X3VFvtKmQyG9mW20AbbhjCp6HA8DzYjxNmB0m0AUoxUAsdOfK6diDClRSX5cCPH3DsRi0VvaKws9xtafid_cdbIYFBaBS73PYyEMULhX7S0dMX2RskCE-011ArOLJNTUxs5EYFuIIokQByfQd5EbCBwIL6kjFOyZ68iq4QoW1pi_3dY0tnOj7C2XWM61K78lwV583QyyPQqpFSup4Qq6s-tUoVMiLdHlIUQL9F-HS5ViiKERNI8favYBQReTdi2PGr20Y_bTVYwOsgW6wlic65GJMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA0dgg-r2lyKd525AX6QWpRDvhPDpfP_8WOwyKwsS2cOm98qyNTEij--yvm9WatFI9vXLSBACoiKBb_pSpxG8E--lpJsDJw3QMuczNK7ORXpB-U0mwqZgaR_avoB-ddwKYDEclcYOl2-xqlWd78mlb9z7XkNakq-nHryiv0JqkkWJGUH2pk3IfVc-cu7graBFSucMlCcaKL048cKyqQgUI68bBIITyEw6Vj5tbg_0poztI2OF9uWZ9UJn-UZYeI_91_-SiBbSXnitS8vBzk58m8Ae-fwVWuNZNAuKMZ2tuHre39MJVOJvJAtMisoO0ZQUBMpCdkeQbYrze70sdPVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfHY3LBNP--KOE4LVe6SLZ1nCqaOPuhmxlFYYUjZfGyTMilAe0XF6WCdbapbkCpF0ar2-VIMgBBdIEeBR2dkIcRnqjsod5gAg1rnqWGeMEaZ80b0LU6r0NTQDbO8CzIysZSQhw5Ve-QWFsG-usydGaXEZsFJur5aTzU3bQcvqSnkgIs-37gpwPIUvZdaGbTlYEnEigo-3SdhOEexR7kaCb22beajn0LIDBm7LXBiQmBIWDQNEc03MqUh2iKHc_QUDFXGwDmWNAmGwtufPzdZU3-wS0_-ttDN-aTbhx7SO7x10J7ZCcY5HjP1PuRf7fC791EDQ4xT0lGEY0HRij_tyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnOQFPr6ep9OnO7SRzt3I4VuyKjl2PSToWr4xBxUmCS0YigzXXyfgyv93i4zO3nYxRmVn59Wuxt4GvmRULTPJ3rU8lOYU0ggBJKiRJQlUxt5RlsnKXg4vXJHCcNuhXqkeIWvOHIzoirxwDgZk4Ix3njZPqRBlIX6rIWSuUNQHvM6m6iDGpYyXqh0DiN8mFbqpMHrk53SMKuCJOLPV2DCYKWPw8sxDu04VbBX8seVAlXMPeKc5dlR5S7_eqgS4HziElhGPE2_WoZHaGvyclfxQKmpmMOu0n7xWVtjl0XwSvu1QV0erh67GMkY8fc6p7Yh27ey7o8BwEe4gin3LVnFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=M1tz6J6ZdvSETuiZuTub4nS65qk55jIx0Ibn3XZoTLPBSufa16srn1s4d0ZBaly46sqEE0aNdB5Rr6rr06MQ_FIwuV9m5t3ymq1XdKMVHloVCcCJS0MmrtgQ_8lNQThZdgpzvLrQM443-PpA7f05CjM6JFnMC17gmBKMyulBU-KbKOKd-sB6lLl0msrtd3zanDssJU6nUn_PCDzkg_7bxbL_OSS1-RYGTd4I5d2bFwY268G93Wjmpq7af1GfiJAOwrLxFeW-36K6Ae7NjKo058Hdoks0o3LdjyhavALah_V-cZmdb9_GmaBabCPX2nhnWRqGnCmmWBfU-Bb26RReow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=M1tz6J6ZdvSETuiZuTub4nS65qk55jIx0Ibn3XZoTLPBSufa16srn1s4d0ZBaly46sqEE0aNdB5Rr6rr06MQ_FIwuV9m5t3ymq1XdKMVHloVCcCJS0MmrtgQ_8lNQThZdgpzvLrQM443-PpA7f05CjM6JFnMC17gmBKMyulBU-KbKOKd-sB6lLl0msrtd3zanDssJU6nUn_PCDzkg_7bxbL_OSS1-RYGTd4I5d2bFwY268G93Wjmpq7af1GfiJAOwrLxFeW-36K6Ae7NjKo058Hdoks0o3LdjyhavALah_V-cZmdb9_GmaBabCPX2nhnWRqGnCmmWBfU-Bb26RReow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT5leFh0qDTBdbiu7LR5PxPDkh-NdLK0S--cC1IsTQgzyOx2f2ykLyF-3pO5LjlktlaF3rr1AqCbL7YBpd4_l9ilEbpuD3IpKuRMPeoDwxI3HIbmqxlQMtVwV_qycF54EMUmAEfXqScpUgbbBz71-6zQTfbt2IUAyXUEVCyc4HevJbx2_-nbtJsBtSkGeCwiQswrGOp2Vqlf04a7N2MlsS4C1Hh2iI_Wm_lSFHWZxmBrSCJEg-dBGoMVvwu0y3w5u2qzK7lfRfQB6uW3aszeQrM6GNiU88vm0U-BBgs1oY34ZAF9ql4ByFu7nGrHfBxBnIP1gYR41LQt6ohdMReXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daNXI9hwrgFVaMsl_l2sKVrjMy0BfVCqxtvNas19C7-H0_oiNWrNFoYunMCAuoNa3z-J6H3Mh_uOtKAnlKnF7-j1TBlisAxP360vHsmYHYT5Whns90kogXqd9-NEerNV1A5m6xyX8FcjmIBeCY6zYKUFjBLmfGir7l4M9CPVKLVhhmC_UZ3kwLWN1T1-0C34hXRASMmD6BaYjoTdCtMtqczhlcDto3_Zxa69cnREN-OrbrKkAfsEOzuHbnoiTSkXSmupuJwXBurLEF0Bc0-GnFsbYCzn4b5SrUVba186vDmnUYuYdsdA1Rtz6-C9oqmIDcex3RjBWTYQXoEJmcslrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBt27ySDsDGLP_MPGsibhEt9S2c6dxxnZvl2TiDE8p92xkAhI-CMmwdb91PFO9Mf4qxEuqAWhKrKEUP7IoUOk_Arpunf42Tlg_CgqaCpMfqHio34kQbRmpbpZBSviWoYKXAV3ag4apYPCxGUGuI3Zxj5jOK2j_ldEpfFvvHKK9kK07vNxjoTLYOJpkaxXT0YPPis73unCu7Sc0EUDx10VbyhwH7iyTGmuy-9bjLH5tHYtebuGtYeH-JTl7eli_b_Whan1IeDLijw5wx6kD8OthfjOyKlayyEAdmX-oIlgxwuY7secHHIIyzEKPylvm21Ma3rOsFOJdEWLLYBBLbVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLMGxtu8GcmDIHeU7Xl8uauqaEgQCUtI01Qcrp0zG-7anowFknxHvGFQ7kfhkXfAlWydHL7aexcs94gnseCVooBPALVOm4P6RdzIzaVhJpjuxgfKo7qIbI3cmHxBfDcPTjxNr5sOc_Z84WYBlH7uNbSwJDTL2LsQx3g9wSUmZH_Fa7ItEnUCt_Rx58oM9lmfzZ_hTfFCc1eAgzMqOombvbcSm7HYzq66lEP9QFpMQXDqjRL03ghxhhrhxSmthAYwz2gcJGFnrscFIeRuJ9EvY2bYxksZ8GjKjR93Pe-P3krOKBvUTOAqspc009FMXyNnd0WI0GGx3Zlgl3E99LrfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moVH8eboBGf0Htdn9t3Z6qgZw6CEOe6LJXb93CFK2FtwZFA4z4E_jJSAhsJAAXHjIK_TjhMbYfJhyPEC8qBuShbQ8FG-ikow0tyUUqOyF2_fSgkjTIQFgbTRG_N9YcF6s5-S1keETkr_LhD_ykH-rEOLlkNtpxuz_ZdFowwJvN-4yUoMUv0mlPanGZOtsKz7gCiDD8NZSoqNwLwUzArSIKfks0PwV_NZhNYuU_9pc-3eIzF3hLLoEy2aIzFlYgFYKGl437fG329lsIft46TAdv6-fyuwUILV0hwiRsCRFP-a1ULSgzTZQV3tFFmC6GSAwsayHKdWvWIxgJIE_sRppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0XhqLNq_qZnHvxAzwrAxRuo6Ezinfj159j5kGeMqF1U84EMnXJKZvQ6LW0kEw7nRb5tN445rvamqE0bQzAD7tm-CUUW1tMYrWzvcmL_RTJCleeWOeza_fGkotcdW-DAKb-9MI5E7F0dgEZ5bhlLO35QBsjSXx8peONeTR8hzsqZl8ly5q9I665fJGcNQbGTWorKBSTMhgdBVkGJ-23mOgfodUzB3nN5mAE8s-Ylh-0MjeyI-gqP2aEkAw3ZwpqSjT2Nbm4-y4kelHvlRidBAvFSBKdYfG2rqJYdjx65zk2f2ZyQFl16t876Dztk3yfbJbEZnjgh4dQssEmi3obYCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpDBLv5EL-oihoskuIHp55cpL3Eq9Xf47b_YGrPxxbMZqtW0bZXu-RfI5wMSd6iPmOX2E55AgmGwAsjXDOxptIKhZ65ArBSaiiUDixqf6lEx_rJF85pA1U3McnA4Ufravoogufc7Rq54BzUh6CkbquB3a8f9yF1_V5MX5_JkmMRPwxvUKfU0g4ST6zE_q9q59iDFIWQONCU-r3ZniYMPjotFwwUBeR43nG0plZl4yg3pVejmQaFXYLTlOkNdHlYiUTlhWpsYArbFTs--U8kHk-WthMvJCZhsy0i0srV4HUKWtcnaXmYq0vpGz8le3tNLbCNIUhuzlYtDJgCM79OeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN18XwsqeE9gAZSK9rqvAshlGV7il0RDwrzf-C_gN0AnkkVCiEirC7hbCORzIui0-EBCqgWZVPipZY0X6H2OfQlKpS69u5hO46NZahxp5oY0OOQe5-8cwGN3Nni75o7CDGxr-NUx1rpcqan_B8uU2e_PSLr2aUxRH9f6NXeOgn2PDt1F5AKJPsiDSg25BTrFPnXWjbA2-rXp1kMxp_ZKCFUD_2Y5YRUN2vLcn5LMTP0-Tw94MLYCn1gtYL3J7-woF9pBHEKfgcFiSDxEDT4lcBb_fQLg2uZiihbPjjuWySPgH1EDgfeVZLU-z0Pj-B1KA-5Rj2AazdJQDOGpk1uXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c82jDDEe1xijr7y9dXkZagAA8fiDAXgeLAhyHB5yMTX7JoXairP62JCI98klW1cur12GZWEeiz9wDE1fH_sN2uEZemYq5qB7AYBjRkafNvx1D1Su-flFkzjmnHF0d0fgHyxMhqAB_OlEhEPTzp2VhJ0HijJW7lNLKPKPtQ2U3QfPf8P7wuuHIABGblloiYfyj9qBk0kzVuORkb4lPiUA7TIFiICvY7AUEZ7Kcc9SFP4fgE8efM3QSm4GtRjJ6bjrVs6GsuL3hlHUtWuV48KPEDzPXC_xiGYGOKTkSS2tlYb1kcq2uyyfQlq3xvR_AzZGwNFe5AXbjUHswqs7CXlv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljMyPE0YZv8Ir71MRiASgUCbORSDB6SC64NWBbg2dOExH7ngVbYxM0emri_-ioeFEZrRi9g-ei2f1SakeP5avKDxxUdsyIkZ5CqH8lC3NSDMfFkRtKNmtGWJy4A01iAvP7MTLrw89ob00doy44IIshPVPM1zYhXofT1IpVt5T_b9Vr-a8s3UvUD5gNAA0HRbHMUfUIeU5lLykzLOyUKuvJPO32WnFts39qnSk7s9bGrc4KO3F5j5i_jVfqAXdMjGE0mzBNceq6G9YvWOIVlv4vwqWpi43KZv9FrSW6S8GRndaS9F5s-Mw4j0PyQRwwAluJa3p9DliuzMQO4CiYdv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYpXBNXKTk_X7yIlBVjZbY0xVVgHUg_od7Zzfm1siptDu2uqUTEffMXiZc_PHjQwHO8UfvZTb70yYRjLKxU2h-POP6qrUEM00T99dU4FQjELczNCiyhCYnAjBHU8X_HjB3CuNb2V6ki1yQAN2bzSALeTadPyDM3FhuCL7h13OBcxHYx_71E5zo8SYCC0xy-F__-DgrmCXVK5Q9UWyxibvLkYWSlFBdM4HfKgaEDzQKYnqq9pUueiY0XQfS0GiMjFgMbHgnTNpiikHndO_YSr77W_iusUzxXPXcX9LqvdvZWXk8cpBrvl2sfZ429dzCtfYmvSp_PIHlndhRWYbPZJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfbftqefCRdqkrTNkHG0-S6pQqVPAGHouOO5kepLikig11J-4f1Nz85K3flkpcPNdVmUjzmJRnWC7LnWHeCYnn2S6Tjcg9HfHu5i9gmCR_qcv_bgLmHAByi3FJpQyHR545SesJeCN9wLdWkLsQeR-QJpp5g1uVyJLQVfS6oFBfDj_-r8gaOel3DAYyg61RykrhbQ8oZS_vS5lUsNu_bhdBFJ8rSsg76yAkTD9Ob0knoCNDzGwDbad7N3zksXmPfwyqBAp6NtR8AUQvumA8bwfp96BaxOY1d7T0Xpccd9nSGA6Z5ZxwrPDknnAxrlOO4NeVKN0w4e8cQitgzc1xZ6sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSHHReIXm-bcjQJbdBaUboThaVkFNu9NJGY5XNKP0aLdJuYK3FAuKCrbCA80mJSkjDWDPulOdl_GG8ScSnd1gq1QIMZxdAs-Tp_gM1sSU9QWzeuKM_G59PkRLjzwuzTLdk3_BVaKDZqcHgQBV4G1vfF89PJAPx7af2p1XFdTlY6_Cr3LtktYvx_lR8XrVcus-Bm-811Ad0IhvFcwqmyZPq-MPMpDKbSTsOlmI1wMEefcc85IltAyHoi-MrxbxD8HguKr--w0ULNyFNcXn7wkUFcvGL08HJEUILuwAW74c6WIh1y70JQj_Rl_ZvtPocsUewErK1kYRzufhrg6y10YIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=n72MRzB-vpfs9jz5qCGglhQEsrOIjwtamK-Y6ukJ76bXxnhImR6xHY2eisn34l4dtxsbvdMOUOnjyGtETRk4k_uRCTjaubBn67WF3NibQPV_-yWr-s_kZwVCJ-g7XisTDIsKtWoEzUJzrV2ivpcGHFJKf0IL_lndBNOOTuRM3XIXO5o3DB3eiuaj2mVXa1xxxThUlseyXHWbihkFafU8NVJjX51sbuyU3f_i-QmBaL7GPOiHHyxQbwWvl1PfrwXttNo0J-h6StJCNKyDJcHl8989S0e87Iu-bR7W7Gu5fowItYqH-hT8EdezGL0e7N6lJXyaw9WjQcCV7BlfHFUHBIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=n72MRzB-vpfs9jz5qCGglhQEsrOIjwtamK-Y6ukJ76bXxnhImR6xHY2eisn34l4dtxsbvdMOUOnjyGtETRk4k_uRCTjaubBn67WF3NibQPV_-yWr-s_kZwVCJ-g7XisTDIsKtWoEzUJzrV2ivpcGHFJKf0IL_lndBNOOTuRM3XIXO5o3DB3eiuaj2mVXa1xxxThUlseyXHWbihkFafU8NVJjX51sbuyU3f_i-QmBaL7GPOiHHyxQbwWvl1PfrwXttNo0J-h6StJCNKyDJcHl8989S0e87Iu-bR7W7Gu5fowItYqH-hT8EdezGL0e7N6lJXyaw9WjQcCV7BlfHFUHBIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UadSL3fe3NxLamypY44zodOlGctVsio4zEnWUwBCTjl4Yaq13eZGeVXE59ypcsIOp-aMv00XILlpQgkPJnzZ6_O1gcyTNaBXh8OyIGikme_wezoLoHzEnkVIknyj9SDNd3Rw8_qviozsJvxSL9CWkex7J6Vi0CVOr6WiWpwuwB0Z5sRLd5t1VAcIImfsf-CYinW7mAWRmiN9uTtyYOsje6zwGl1yQ6ZKdKfTYf0IZzk359mVk4506HlqRZm0s95kuHSV3hkYPbBXZoKtldjuD5gaMEf99T8s-XmRfOSo-dPYN12b6FGVTGIHybYhB7rNf6F7HOOREdLB085_gaXMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaKCJBRSlQjAi_YS6Wq8MilQpgADeHXL__kNowWrK9s710rGXudQD79PNi5vV9aK2MZtGX4NG372vV6htrmaUGLokPxhOrubJz8YHx2o7a4Yhsb_EU5dZUiGVw8Giha4ZGzm2s5PPPc4WS2CnAk6qvfX4gizPaQPnVctBv4MLWO3DwBD7SXyLVEo92sv0YV3lMxgelJd_vEKoDX_ev0YiYTLYhUTd5A15_txddHWTI4cNKJUx7gVnPsTvw-W3_5IPKwBF9JBftik08ToGVCaWD_nnrluCXqhPMSb20apBjCN9g1SxgkvAOo65ye-Dmvv5zHf9QlRo2GdPPigJcL2cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=PVeZ0-4Jd3A8xU_UD5hWY2mHXYw1O14giUc2MAsL5aP3MRQ0RkRnLM5OhNkPlLCfxCiyYuWIoq3-13iOuJBPeGJkykXgDPbj8k5ERRaO4gZN-tl-h0YUUmg-hqF9qC-pbRLodmfq7Eu5Qhjt94VuQDIu680Wxcb_UbhsPdCQrV0tVtdaoGmhe_fIpwg1OpiRNaxJHw7zSENY8oOdEoTwvkNe9opdwCogS_RdCCismCua0faL_kl0aXVdGbGlfEAhNe5cnCvsQScVrOry-Ae4OARsJ1PdmFEUUidgOdoRvO0sbOIUlenFNvMsrLlX-DKaEFbCsdBt4DHVL6ltD6wnF4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=PVeZ0-4Jd3A8xU_UD5hWY2mHXYw1O14giUc2MAsL5aP3MRQ0RkRnLM5OhNkPlLCfxCiyYuWIoq3-13iOuJBPeGJkykXgDPbj8k5ERRaO4gZN-tl-h0YUUmg-hqF9qC-pbRLodmfq7Eu5Qhjt94VuQDIu680Wxcb_UbhsPdCQrV0tVtdaoGmhe_fIpwg1OpiRNaxJHw7zSENY8oOdEoTwvkNe9opdwCogS_RdCCismCua0faL_kl0aXVdGbGlfEAhNe5cnCvsQScVrOry-Ae4OARsJ1PdmFEUUidgOdoRvO0sbOIUlenFNvMsrLlX-DKaEFbCsdBt4DHVL6ltD6wnF4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqwNwYDZKbinJzL1GX26h6eI6pPHWY5LOql1I6ydeFZFPAIe5qWsC93p8VNWllKKv3Cfkt7vgizJcE-iWjHK4Qc_Ab0XaA1UP2bs7y4Nsd0oIA2lO8tDVZzY1ECeRXbpSEkBMahcw0gOHUW7XBeS6U9dtv6Z1P9Ez_csCL-wOOLhpLhZ8qEI-VnpcvXdV3OT4wkr9B2sriJm90pvuAv6lFQb3REgcAV4IiR6Wv8FUTu2c_74fTqIbC_L9O117meDIcn2O8wBwEiLRfti7b4NTbsHDrIYWmIf1KdFhuut38kE5sgZYGk_2jbkvuMLKQE5T3EZ1U0naRelDuMgPhf1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krLl19KGCLTnkY1erpDrDfm0AINhrMlVq2mJH-jjmZn9ZqGJ9p7bETz7tyJrfgXWV5WjvXn7WUbpibvW5mkPYqHBBrYtHAFafYrp5FqZrVowuHWGc3IjRG-v_tAqyXq1oa1ixy2teLh6sMtHRoOprSi9QmK_XKhs3OQ_TXh9xiriitQnoJ1hfh5ntdPFMGUoe9gEVZscoflpJLKuOZuyheBYW5k5kE9nWUavmVlwygGSg2MAHAlA0V-G_Yl9Lb-OknzwYylxKljgrK-88-_oBTxRd-ne1nv3EZu1YLT99JUx4tTq87kc--S83gKO41r1Gwlgd805DUIr71XXUAFGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmNqzjhzsFBZzZfag14_PWv4RhwmlTBa7T5XfNSFQ32HQyRzbG_sgd2EF-HKg0lgdgpoNmZo6lJFddWFmq6mCFmbsdWWGp2BqmwXpwJ7aIPU-9q4JyKjjEr03yJH-5Hj13_uFCMfWX1PVBKuQjzddnAQj8gzyP2Ud8oydxeh7O02Gt5WMSGyk6OW9JyIbPuKXGNQZ1ODt4cksRDcMXlfESiV1466MVYSF0qgkm0-bnGDiPjp7efl0qTDv36t7NTW44TPbB3LRsZ1pjBueE8DvL_yqitdTfxqABMcQARVXj01jbpOiMoMv58iQ7yb7af1lDoAQS6p0L1Ax9HRCwFj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkFVPb9MjWgssue_0v68UALygxjIUmNBX5i12HKIv06Aewwj26lzXE53IXfFTAXjxY8xy3j2sgBCoV8OPRQcQLjeI4XJrv_8b7-4vFPpkxwmF01J0QfWDLjFVyloJtJORkQhyBYLOkdEPDrZ1v1pvmN5OKtHt8dPKIseNL6TPD8JurE4iLbFco8xwJaj7lN2iTvrwpi63ncavR2iGi81cekVpJ1TzVw9-Pusc3mC6vwhPIGGomFaVhzVE3s9qX7ZejqplLzLH4c-4oREQZfztreApF8qt_NMGqbZmC7nLOYAFQ8395bE5PIIBIXry_rNAcTPbjAjMkZnmzhhSi1r0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv68pfCHKQEk1lDBPdfL9c_0oMud5GHzwI_OF6L-PCN3WiiyOr9FLi7mcedwO3pGNiXCfYu2R5sAU2Ld1sgvONFFc7XW7JkZDw_AkFnHzdm2wsk89I-8EnUFtL1LM0q2L-CJplXExkVi_htQKL-paeLN7m5UCqkeWDWgZOF95Pegp2bSFK7zKjmPWqzTXXXSCPaBStPTu-tu913wR5KcQyTEEuy3YRiec05SyXToA3wp8025x8dBwD5JWEhINNa8xZMn5UidXosKfDW92iYSVKkP85FhmzcfPE5XaVHfrYbtTFYN4Qml-tJ9Jmow7PTlc9VkSJjxQIxoT16d0IcBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=a5Tcr1XwumedxNZrlvbO2GlQxGLu8QwxyuJxhvTyFtE5phkKujdb2DCtAPTkHGF2BiVPwWYNAMXTDLVfNbh1gR0_r7KabAMGKK0EyK23TZ1rlHDlkWvXsF0FblMO_j-YuPBRenEMkci-bvLzX19U4BdSkP0KUedYqHpcNR3TNmKhgJcnctfgRDc-LqVGAa7vDJsBs5Ts0Oc782pDlWDATpCq3BoWEd8VFeHyzbeEuPUvKbB9DWBEd0H7jktLomse9GwK048lO12_4pGEKTY8j2Xv1Z_uKWsPC-BSq0oYqZrPD_fnMUwNyyyb4lTNrUjOZOj-iRiyjEsqtP5G8AJSXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=a5Tcr1XwumedxNZrlvbO2GlQxGLu8QwxyuJxhvTyFtE5phkKujdb2DCtAPTkHGF2BiVPwWYNAMXTDLVfNbh1gR0_r7KabAMGKK0EyK23TZ1rlHDlkWvXsF0FblMO_j-YuPBRenEMkci-bvLzX19U4BdSkP0KUedYqHpcNR3TNmKhgJcnctfgRDc-LqVGAa7vDJsBs5Ts0Oc782pDlWDATpCq3BoWEd8VFeHyzbeEuPUvKbB9DWBEd0H7jktLomse9GwK048lO12_4pGEKTY8j2Xv1Z_uKWsPC-BSq0oYqZrPD_fnMUwNyyyb4lTNrUjOZOj-iRiyjEsqtP5G8AJSXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PikNnz7eCc4kJPOQo5xB1xYWQHqFbLJxmuV3iLrgcP4W83F68MhEIuvLlTPxn3ExQRf406HkwIWa8pIQuTTe3_FkiGCbqZPkXUP2c7Q2VDktqFxUtwiF8qSflrNjzW8PJ2rBJH44QPHAR2KF7cIt5qItVJOv0-tS2YZaR1CUhIB0lHRa2BiOB-l7rfcbod81JmD5reCd0Fp-dOOI2HfGzUk3goN-Af4lAu7ZArcKl3EX3iZaAKxbYnJ66ER6ZzfnGj1TmXm4WgP3OJ9_Hna0rq9Ns7qzsMGAlLamm3pYCse9T7pvHcWnMhFRg9vUL8mXB9K_mSXpf4oJ07M4zVkbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS-UhtsVIcsAaeHGQuDxDpLaptv4jz8Ui5IfJGRn7uDh6pLj_CtyTwSIfTYB99njo85XADSkmMc43ZB1j1UdwnmGyc9hEQOS-_yENJgoU_exql7X6V3gq0cmQKJwt2Kzrv5rhbpt6F-9_DA4yngR_Jwtz5W0B_urbINfAg5h_EliStAecVtzfJMkykA0yqg3fdXbOzRG4b2OsQXo98L3CfCX3uZOrog8wqe0VVsRL2lYqacXqMIKX3fZZ062YmF8nCdeZY7fHpBWNrP9YqL7cQzs407QES6LhJWCZhhEm_sqcjRydo8Y4pTohEj8EU2iRU2SMd36B4KEPqHBHMDzxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC5r1pk5uWlqChUJR7gd8hFnZxtEJICwPirxVZ6D_BEtvyRHQWvkhSvK_yInhtzwSu3UguBJ659FTuI5Vsn4pr1mz9XBUWtEaLPvVw93JMYQ3UipuE8GtXyuylwCMHDTZG5S815HaCViB85w37ASm6aohHwYFirDA1hkh4jYfWiOxumzI_EfJdV06ftSok65BHCpaNBgK3BztVQgT6Yc1ON_vaU2qvgTv1tWNnl2InvtlLysNg9fBPpCytwrADaEdk9g7FA-DsX78I87D6P1P0Ige0EE9LqZYBDl-PUHbid-8de9d3uf1ALVA2Iyq8nyvaxQ5BKqw_vUvJtjUKn20g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCaznDHttZAya0ZBlrbdoDhzUs6uzhFp7dygeJXlgr8tGWtPYTzO5wBftdOEX9Mk3bHZIsQMyVo8hx9zrBmeRmCEqYxQKKf6Cpcscvb8KB0wZqKy1IiZt2j6UpWO0N9kGKjgXn-NU5xaxHEILIMebaSpZ59L6cDwlWnmSryHJHAuXTb5QPYeHRoqxveHxaJsloWTymxF7U5cqHeUMSq-epU5o6UfWywu6JNRP_mg92wYeb9tX7AugkGuwE0fqE1Hbi3ZSiXWBMUgnm6AZxJ2ZW38rPgv0ZPOIHGASn9pN2a_YDX5rLL_WMtyLykiLIshMTRE3QJ5QNPTMjzhhDtDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=o_HnCLc6xOh7KiJ1thM5zINblyXtcS9vMPyAE5pa-BCmZnbKu3to0kWpgXMotQ9EXP0g457cgHvUcsueh_1hxONC1iXV2Jy66IeSIl8A19G5cgLUTxdfkFKuc8HPMvfNtcpPZD128pCFfmiaA9UBiDTUYZ6dxDReeB-o7vtaX6C50_f9-Zn0RWbNgCQKSXFJEuKrhKdl23fs1RrmypaXDUoqgx8testeKqPSsNGJtZjtCG0EJ_t8LGBJWChQOr6mmHNTZbcsX_XUr-O1lFiMTCTKogdH_peAYiAjLPo_roZfa1skwegwxnfG-UfAxF-vFAbNIZv69AFa92P5vArqKLegOunKb1Z0GyV0ZzmTBVCEtUHUl51gDSOuraoZDV837mY-NBLVsVn1HBDSbRVtGicWz1yRdyRHlNMHJ8zUHdVileDUYy_1ULUg4keXZ3QJwFFayEf2p6_8Vx-uSYD9nBk2QnOSyUtJ_N8wov5hEFH9Usv-yOe_HuHuWbVfw9V4SOmfNBjSb_kb0RZ0-agy273f3e8rWG97W4DyBnnYchCO5Mj7YRCbcEDDskL3B36uFC5-hAbvueIRu149k-XC9wxhR659Dz10ku3jB5P9DzcIf3M7lvzKWs8QAx3XfgUS9ARHQs0kaR6WguiATW8QrQAeb7G8Vu-fujjFwd3w-fY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=o_HnCLc6xOh7KiJ1thM5zINblyXtcS9vMPyAE5pa-BCmZnbKu3to0kWpgXMotQ9EXP0g457cgHvUcsueh_1hxONC1iXV2Jy66IeSIl8A19G5cgLUTxdfkFKuc8HPMvfNtcpPZD128pCFfmiaA9UBiDTUYZ6dxDReeB-o7vtaX6C50_f9-Zn0RWbNgCQKSXFJEuKrhKdl23fs1RrmypaXDUoqgx8testeKqPSsNGJtZjtCG0EJ_t8LGBJWChQOr6mmHNTZbcsX_XUr-O1lFiMTCTKogdH_peAYiAjLPo_roZfa1skwegwxnfG-UfAxF-vFAbNIZv69AFa92P5vArqKLegOunKb1Z0GyV0ZzmTBVCEtUHUl51gDSOuraoZDV837mY-NBLVsVn1HBDSbRVtGicWz1yRdyRHlNMHJ8zUHdVileDUYy_1ULUg4keXZ3QJwFFayEf2p6_8Vx-uSYD9nBk2QnOSyUtJ_N8wov5hEFH9Usv-yOe_HuHuWbVfw9V4SOmfNBjSb_kb0RZ0-agy273f3e8rWG97W4DyBnnYchCO5Mj7YRCbcEDDskL3B36uFC5-hAbvueIRu149k-XC9wxhR659Dz10ku3jB5P9DzcIf3M7lvzKWs8QAx3XfgUS9ARHQs0kaR6WguiATW8QrQAeb7G8Vu-fujjFwd3w-fY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBSyzTfNSOK9-rDdCBk9wU6YWFDiluBkfgf8lzhW0uPoOfndQ-fKlpVWKAsJxs2n1z3lWH742Xnn-h5KJl3Ki59fhzvfhk7WFGSocHbNTCczdlFbWoIhB5qRoEzRadAJs9Be4C46AnkOhlvw_GhUwbCPpHdLzA-tOt8vCenowNYWT5Ph1hHoK4iYInOUSNRMe10q1rC1aqD-I9ionKd26J7Fgy_iegCeaoSYkTYnw1-_6dLqvZFD0_nqFvgd8iRckbnFtAgix6k5JXNECbbK6Ba9GmzzXVP3cbdCHtsTHYrEws4Sjt3lL0-mFRvbnEoGai9omPjuIsCY3jjNDJhfxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsTQj-6fxpZnJZJTkxAtd_IECmJiNHPQ5VUYXkIICt3sYKXqV4xFY6He8XbKbFIxaN26hMjbdWmcxvn9FB6KnCdm7B3zi45di0C8cCLV_MvAKFe9oyw12Wc22xq4XOpX_4aLQXD1tTkGRt79pEuKJOfrQ9-OWvJ-DPPbYU2D7-SR7YzTomVACd94iMK4I9nLVxMbk05AQpvimw2YjjB5jS3y4gLOW4c5sEXcvHI9-qA_RtugWjeDJgNzW_lDTUp8eqFl_EVIVJgBq9mhHl7DsyWCAflcgFI3qkNOHPl4Y5EkGq1fPI-X6eatiDiH4PlxxEk279chSPPdVhG-JHT3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRnlS8Fy_u4_NICR1jmKqUQ85PtMwrEHe9ozOVA8lWzZAy7VGLM8932_glljRWSVjciXQdMF2wMOs-DHVfOaw8vm2qJlHOjWi0YSx5RkD7kgIYk4SBvThOmTn00iMAZPgNgUQJpNTww-_IHl-GwtRpjIQJRvYGE3mtLs6CCp8n5gj8vdwrCZ8gXdfbq8H2SwxfM593uaFSbxlVsanKpZV-dUuevycfjZ1c0IkIk8NZJi38yzMJzX0RNyL9IEIFbUJV7E9gauypvD2Vg3eae_9TIG6zO6gcs_THWk0Xwo_n-WvTyKrad4ThbKlKY60rTX1g6Me69kZ3BVCH9nKS3Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR248m8VbgnY6Y2q16wRlXYrNtt5VkO8ow3d_EzzdMBhIy2CQfccGPJrsCyNioSrySWrFufqqDw0bAMa6Kk7Btjs0R69ywaUN4VGmesLvMaVRfuewUQie6jZx9b9iaXiNa_JIakrTDSuc2ebu_fmvVW95PC-unjENmcRuQVQP8FDPMrB0jxMRo7cweWOfvprwi-QhE3BrjvHnCsj8NeFW3dt1MOLDtcppMHmLAxvcig0K7GevNzyCPrvAEQUyx9D3xAtGiLBoDmRLzaMqRNT3OslW4yPsFnFnnXlcfALgRtjOpGnPJnMkRZ7FYo1zOq_1xqlwVjT6G-yO158sNrC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
