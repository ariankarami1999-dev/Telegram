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
<img src="https://cdn4.telesco.pe/file/nzACfbbfWWuyfUW4wktyxUZfm78Pu0BAtQnk6gccbfvKiWAVG85Eh0sJolt7qcdkfMJv2iARB8jX8xLN9wbjgri89-X9pzMcDub6u2T_tbN7gaA6KxJlDUFw7MXQMvbnmbY-hfJBUx7pR5GB8kSAUrtfpBl-MsXmNtk9tBkXAkWZSz0H3KUM1q2XkFD5r-xfYkSP0yUUc_3N-KWzQxO8-2OoVuKfQ_FErAVcJLvjk9GDVo6PzO740p9t3mKXbmyjFNZplS_iHiSOvK1SX8-YZLeFmyl5Tx_vb0kxdgn2_G7lWXadQu8ndDBn8PRyPZln-0ShpflkeSK902EHNAwEVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 02:21:22</div>
<hr>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1n-XJRAuopI_ppvWLDhKXCjYXG228IvBK0gsv-KiT0Tz9AgKQRNqgEevCT0mEaD4GWMQQFwFE4uJXl-IxzPdrnoZzBmoo8aYgmicw22rf3UTq98aslbcUesXgOMzsY67oVK6SMMBBn25zI6ZpPrPUqSo1wtVhIaRHwXllb_nq3eMYKk2Ghv-631H_e36OvmMjETwBhw2tgalizmqgZYveFgdCxr5nwzwuMjOGfBYA3EGhSOLN0alFeNOBQieLh-wPUPlvveyOMr9wxloW6vM6XCNdpLECU3qy-zeM6YuWEUn89HZYkHpoAbO2-HE1_Awru3iAubdKd0isMFOVFS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMbFNnOY13US0MfjIzLB7zS-y7MHt8TYpTeRzA2HaGS00IG1Dn6bd4T3-rpH3oL3HA5xQk1OVK__0lyPFf8HtaD85Df1RrboB2vVd_dlrgOfN_y8zheNo5kXCMgmABz722B-YFGq5l0tgPtAG_CAgiZXhGvk3LDfReQpAOlU2TN_UIIPLRE7wAQMOpe0e6aTE_KsXI6y4xX0cgIZ2EjzsjkfZAGf1OuLlKP4hp2O7IqGOlk6YTtqpJb3acYueAI91JZr1NsU1HLpNqhB-WlHOypOjp7iIt8P3QHZkh3qTHoOPk5ClUZ23_XcdcykYPPVeG21afyrOgPkLel5KiiSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo6tGIHDxDZQiOXSYa615zf-EcBUpgOUXisVB6aTyGIRUZ12XDDyh00ddMmGYov6iNP9qAf9nRuAjNgJwzwHFSlE-tFfnq_yHfhQ-wJ3syn15H1ap8J2Ezb1laMuSOJCkmXQhiNYR3ST6hAG2zNDViyj2rj2e0X6her6ucN2jJBjt8lBCHPxbh4iwt1TjykoPGzqcgNqvJq7nH3kKqNUDTt9Mn6b5CVqvTVcL89gqvbR1_IYiyHwPb-B0ThkP23bgSnOjapSeD_2uI2MvpFO8QCQrYNjJ-5KZvz5cw8RQ_rbv3-Ry6-yfDt7BXlnCdNl22vDTF2g-_vnWwBaSRki8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTfYhERNlQo_48JnGMB38Ym4LHr9uIRfnv2_GgTXVUsNL5WXgpojte5LPg-TcbXcz8Yu6bnddbBdU3YWAI6Oid1w7i8p-XRZiLv6oOTxlPUEVZXHRoDfFOPDARkOhTxKN71kXcX4XtgsdE3OLtJyAQkV0OlRuKilnTjH3Pgfm8RCsUzhK2V_D_sJmefa07HA5ffR2jFOLj5E3mNqpIaIoCX00-hPwBGlxlN0aqPzeWh4vg1XdEAV6Rn0K7Fux3y7ChtV9wmO-iA6pK5YMLQ1cjYckjsJHPq5KbyJwpJ0XX5gjSL3IpsIYXs3rChlSCuFttHSCJCr6kOZ8j2-fEpU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgpAVBh-87OYR1chUbEVnFbpPZcRQFgEcE6CSWIaCIOUSPLRtefAUR-SvCVrt2wZ4_VtRSoyVQQJ1COeMi_DpfZloMeKEC0hWwMD3jUbEHnvIEO5Lmf3mmFWdvw1jnZeprgzPshO7eGGXsLDanrJey5Dl-hNs28GzSFyCQfJX-Ec6FXEmWZXoCtIHkaQYWWRGXNr12r0F0IhjBT73uMMLEGM1vepmk6jJg-JL4XaFzQOHo6vIZmVX4OSZnk-t87cIjseAvD4LiaGKhc9J8WrJdK3H5X5DphVXZhAbsgjarmsAAEcM6i_9D00u3ttWEtBF_EnL2-IKmSNSr2Wu5JSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGl8ew9Rk4J5Lx_WTE1-mu6oUbto7fYiyLkrhaVNmSLUeeVVNFG_b9z3R62PNw_DPlicmpW5srvAnxjP3rhEQE_EEV0RbBAp6Deo9P1mHzTpzGDoaMAuNWUFBcCWe5Oq8kqiuA2vJeYPkpZsFlkhgFa5dKBlXzQPY9Wra_ZdzbBfj5SJaVrNBtF_IEEUuCILUoz3TO393ASw8VngQ6LwjQBQVPvA6GXmexw4JJRTVJgFQpq-W3pQ8XT2WsvOaGwBEByjsAoYjvHiDmc5Bh-WrT04hXnYWGr_Rd5-Ii0g404e56awWO5SskJ6T-Uu11gQde4L1-QkvPuPVcvvlgY8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHS4rvmJfRl7jof41BZFKruyPpaqsTLB3m_Y16fLRfMNjBSs5PoZmJXdu577RHyaJyU9LqR-jyWCuYeczOoSALF5zti3LFO4GlWAmXn-8PvJPR2SotJwd1XQrRr9NCku_gIf2OpfJ1j8jjf3okw50rJ2iTL5i2wHokVHKUUcTZMqt8Clw8DiX15zXz2j8J7HG-tMmwt_fwMIxpvuUpgRwNyjVRs97rxhHb0BKF4MWfEET3WyroUN3spqkGNIZU40GP7jxmKOfJSmR3h_bASkjb2CQSut_QHlfGxs_AWjXBIDb32KNsV3ZpeifUvSezzoD-GueUumsAMLTPEzvr_5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22797" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqOKxXa9wVQV4jUaplZZcwONtW9a7Ur6MNCPFdrxdhyfpMYy7a6jQ-CT10f71aM1-5__OA-F5asQvS75EJHHTbLuIDjvVm3GC55zslo76iEueqZywbznTpsU2xEWbl1gHbkShPrcDzXAPzKeYdatq60Bc1UUPxiTc33yaqmNHXiOUUkKzFLIi_Y9IQ7riahW1ylpj8GXe031mmZkbxYZ4n-zaHXhj3JyAd-V1iR5on0dyPSszqzl534GAUFBvdsNfmSb-Z1UtDYddp-PEgZU6fiNWIv-HQuOIHFA0o2Q9Xz_YQBEUetJ48L2inUqOfFvQ3yXL82UAFDE_h7PMnq2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRwKK7UQD571U1lMhehBKOQiGQtOaLMioaLHVRd2iC2IbwtdPShBIUQQfxMuqCF5hxwK2c9-9QjWcDBItzSj_0WK_yxxO-eLwAyvNDbF6ATRchsjSGluA63g4lfmX21B43323H69AELVH1_UJ6kOPPnQx3HJtOOaFvvqjfvJKD7aMJVJ4FjkX-i0UY2IGNadiJqEIY8Q3J_DC0CUZ4hB6dxXaQuU3EJhBfoox5xbaAXmarqbxMt_XmUJOHWfBIsB-Q0fUFPmTBdFynqbyquQ2UHU_2lRmwIzTP1H5HWe_-boGC2ApXl_RKB3uN7d2e92sy1eQP81WSxdSkbst9bo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAalfEhbCeZ6i9ow-fkBBew_WLd_f5iZuAzAOkbsXESrDqUua7QJaYIUfavLyCmT858iaL55ZXG7ceeG5jIhoCUDuqFAYGwA913isF0OY4PQMuoGmapX0niz8V81PsPOPY8sJIPn0883VZB7pwm87LdI4QukPDRDhP_sQRApA7IdP9aQVxL0BRABVQIbYqy3L1m8jUF9q5Xeh1uNr0hmJrdnzQpFRY7w1ukGW737G8OBJCFmu-9OorVhRVBZwDEnaU33-AULKjdnjn0Lky1YdAPOfCfX5Mr5KkPA-ot4o2gh3ano4yIlwXudMn93zsv5wBIn2fk-0rfZVPhWOo_94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twFbsX-Y5X7TwrYtV1qyNLJ3ve9cn7fBh_kRb7bvjy-AtUqrke_XG0y4SuelruO40CVzeVA80naXUO9HQWFUVB8vn5oPqQTpZA9j9XNfTDlE3p0Af7kxRgKX8iFlBqIzf9irqeYECYSh2VipctJZkUpASMoUg50gjdPDMwxOKpX19Hz22e0IhvUpLE3LfNKmexob2jaRoXPg81duAs_ypCgcPiYSfXRmrtVFlhHpSSQlaDll3JPrdqIETW_6T2OE5eCuJ9xsl1pZiNn4GS3GNtThoy70HxknQIhhIYy5iDQ2oYyfw94bQRWD36QMr2ROp6y6g7jNR2UQiEXvVWPGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZyIzlqugKbMCXbNZE4v8VAXPZHzAmhHMw1KCeD0CY1I1YZ8lxDoZXrpYfELSQt6r-ddhDZto8Dt3XAgF3XUjMNdKJPPFUm8-8vsDIBA_1aHg6i2j--It96P6TR9soHTe4kR8JFJ9qsNIT5S07SUcwxauxH1Qv7xk8-ndnp_iRMK-bGZNjspOorOCYkTKHRBGVXDUXY0syIjjZgeE9BCZRU20vHiQR-69VgF0qu19ZCMS5m2AD6t9pwccNKYPZnZnVnSmSDuRoLp6RGh8a6x5UV7B5CLU36z8WE0vhfCvHzy4epkrCmhk_Pq1JGF2owk0kbGgev5aDeMnEAZUJwkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdQhK1aFOrI1_aZYpaiur8-hN3icgTP8G99c7SufynRcegIkmWRg8askP1Muhp8GAGnB8LTZIWbxiDpb26bnVsHzgpw_m5GIQnA9S5g_UamlUgaJtXU8pH0THTdMtgm4KhHW2PUSe-EG4oI4oEatB8fFlHek8bW7-PV_WOj7ipT-DQyW5CnncTaSxA-D6dmv3FXKzImlAAXCb_KS7PI9tDLI4lzB7zm4lbJhdK1WzSijBQwX6cCSp0F8jcVjGrKSUQQCpy1E3SFJFtD5dHyWPV4Vr1uPlA22cNjniVCrte8TS2_o-RUOxaEYbdDY47sHYLwz5gqevnO0fqU4_u_f-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPmbuE9xgkmQ9SmhDPYzctmTO86Tn-DGvWLlXm2qFuVroATyWk2MjTMOM9h0FVuMm5ASfrZm7VYRavso0MQrUo3Uq9mPlqA8tUnUltuss3KxEgD6p6hcc4P02mTEJBL0mhvWrTGGV8vy6HOMMRLZp8qN7GRjUnVDvb4q2KYbGaPLToYJnN9bqDRcJy7I9mheMF8tEkzHPK48NZdnl4mfyy1CNRDCreMgERDj5c1f8n_xyrozOaJqNbTxJbbCh8_yJdj-nlhbx-DO_o3xc2aVy3I8rlLWmWufqaF23QNFVS3QIUEUn8pN0QtKYNaurefy6EnXDOPZM9uXhw9OxLImkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXWta7Eb7QPokg6GKVPHy0jFojaaEViiDpG3mNZuRHa-nKmA35rFAjOaq4nUIpR141db5DHDEbrqi_gqet0jaPlPesWUHDNv31TdPESYSJ828a98-0Eb4P4OTn0NhrcqUYkssGfcaLjFSOs17UweE1YxAksTKkZ9rnBlBlSRdHBqRrWYpnvE39t4_z3HjqWuXwBO_slNFYCxobPwvvcL8rpARoWYPqtuX7i-V9I0FIDsVjfUdn8tNGntufK1QjlLRzd4OEJhCZ3by7KizDm0BJe3QRZz0DlU5TMJiaN6_NMT-scdVzZYBWGmJk_1vZxepHFdTMKrWb4RYJBuIsvEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrvMj5UeRheQaXP1yU03qA5Yy4_T8NY1H8Q046UuwFjG-wyaoIRKBLh9ZgSV5lWRc6WWzAQjAApS__FSEaE7fn1danME-IaQSgo0ssA_adY-9DPVUCYczVuloJHx63LNFKI9T4g1GiWUOI7cUBp0S6qy3bTHT_VY7eRONPaNF0vC4bpl8i77I83V8Zkrw37FhqNJ2qzjX5bsd-7zUEyIlTFauIfYOs7GHKMWAIbl1qsZGbl07haHP_JMapNku-p7lIl48cAUptj2x-a2efVWCHfxIsPEWX8qr073wmlubPawfZFAxAFxE150bTnEFavto6WWBM4omZp3Jo4Ia8AMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2zXmYv4UNtVEVlNhs7y2epldHE7SvdkJ-RzVXBtb6UnYpSciEwg4jPaGRiQ7ldKeXDe7Fa7IaAH8Y0lDGYhd2XVa5o5om087yzOU-loOtdo4XVfVjtHKDguBa0jpSd_Uifcv4ADwF94P46K815bnXL34AKCjJn8hEkTa2hkzLge9ug3Pt874L23y3sw2JXC2Vw98B_Eabf-4Iy8Sfa3hwyd6SPyEKWCarhx-j6iBKXl74Tff5V7OagExX8fVpi0ubsDQhnE1dSOPy7js-fgomlAms5wmn9taifH-VIAQRFb5eEBpEqHa0PgaEv-ulOOzdW1WUSAU4rEYHi92iSXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22773" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwGUspRx7xEsO2AjvO_frLWkiKG0m0tul-Au72gagZ0Md-uY1rcahjISIbhQ4i_8r9kR_CK6oBHAMr0SYd_vDMjNJYadOUF3wNgOiJ3uk3zH1ZtUGvA5ra8YfLbK67_pCGbrxXebPsl9Lh27gOYDfxtFPCdEdQmTT47Xl_Avwnp11PTJHkZXsbMuaLOPv-c3swkyNMotaL6i5HJz5WgEi8OeugaAZzwQiPHcgrsH4vzrxtoZMwHLnHlvUmfmxy7ZMo3Cee4YGpG8OjpfEP8WKt0lvES8fD8xilGdxv6jRCpZRrwY30Fh1Pj0GYUB37Z5_HM_pMwCw-bAAoENDmc3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQmt-KCO99QsYt_WmYdsrBwjF0-j-bD7h1X9xav2-dWOnVkTmIN-91HW0Jet9k5DH-4gV7tOKKFLCOUQjRqxKtIZA3t01hSmZehjl_nV8fIOlcGni8kQqFh2Gl4PJtEpnjon2WHlhj9wNqE-Nf7R4-ckYn6rTuhaJHWhDi8U5sQCmNqX_AfLbIEPS6OS4Pc47KX4timMLCxczETCZgo2zkqxacVgiS7vodBMHPbNlE1c5HS3u7F_RxOpp1TdUFAZF11LXYD9rsPS0BBa4BEf4RF-MEhXZ3SQcgOP19DtFq-K5xedweyQDm46L_Q3eHzCl8xKKJU9tKovM-EZ8xGXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brajad58XsQu_voyhH4E0enBj8jp34PbnLK_fB1qV6U5aHOeHZ5x9sL7tHVPxNk5JYdTn6aIF9JEAb6KBWruy2RErIyEQSrvMK9pYH28UqHjwh2ezo0Tg5qNlQ_p1uZgpVeK9r-tHKtZUS7Yff5fRq3O32mTsoqyLX7vT81G20A7X0EIvh02bboOgHcTVTqZKJKf9XWnth4ZLUd8HQlggUMwRlEcdeMA9mRe_ccVeXIAIay8Ryxb8obVHHxU5pUHxOPQU4nfxc-ue5cdewj-zioP9QWp1DrlRnrj_Lzj6RUSxij9-ChNRjB-mWNEgcsdsjq6xmilKBlJ3QuRSHs-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3QuBfFAldHVQbNf-cNoQEqhmeD1PyhX4cBMUgmqzF5vM4cUpgK4vQtr0XqsH5FBwefbEPWWM7dUpjkFb5fGZ3vOihQ-8RHKdvBmJJ6zoYTgtb-dwGgjeWNUhOMLwcG9BN1fSd5WHVzmMV7uxYGmEXNNX2xMxTZFu0RthBtt6QpgKr-0x-_L7sRFvDQMo2YwyCx3G1cnRwBXRmnhJ32pDx8ykFseFxgsO38at67VueOfLY8Er71ZJba_eq47EMg-6t-vxDQhxIIGZarPqo_OFVykMH7dvtAYU8aWygHFaXSsM9qfbqGapxAUwmZDxyHcsrzXzTX7fq2jTwgPDhn-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCcO3RAWfbm7nd2K6_1nzAyJiT__4qQWedLxb3MUXkVoqP8RFnoRCip8kpXpxk62B12uQwm8p5qZO_FdTu-ARPnY88UeMgr7UW-IN6flcXoMHH85RYN84o4aYMroXBpqt8NgSPNsnHEYkrKOn71zDOhaZd4QwAH7Q7BlmK4MwGWm_Smmsi0z9BTkHuHTENFQuChbcIMVWcX5VncTat_QRl72isBjejxBr3vMRTpFA2zCQcUyLNpATNBf7NiJCwMMt_h8jqF3cO04N0Rhk7OjAYFeROft54mAzzoWVftyZ-KbxjBQlqBKTuQ0b6uGmttsCJGAv0GSTyyuKPnwRwfqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qshhBdHY3mFxrS-O2739Y_OhYUiuLZY3FRpCqklgSXIybw5xz8K_e7FhUZ0_i3ucA16bpyKcrjZg4oGLCDp_YIcAB4F57dtBV2PBsv2umuoyo6YYOZinQ-mjMMhENhKeDfmBh0fQNmXXTKlHvGEyEWRLfmDF1uHjCeczpacvStLfpccUQmRLfAxpZ_l_mf_QFMW_DPBh4BCGILLlxeLBw7AUNVLOPbqTor0PgGNRqdcbg3jrK4MZFSVmIzHYLFLZl4Cu4_3bTEcW-B07h7HnF5JmHw0_R2r_0wC1MEIgnku8LP3NHDAfeFVAvk3mep6Z8OSyLMhw6fUDr3bNNANkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsElsNA9V7CFN2_D7p9Rx0q3xo2ibCxGzG_Gv3axFj2_bkd8rMRNg0q_5iJntNqOdb5WyVzyzWyNSKB3efJN_DuFDgyXagrb2TbUQaieq2Zx-oKJcp4z2JWGZ2GX-Oc59Nc-rblOye9RsfpX2XOeue0znSoJ2L-1XGNbhQe5HzTeei8TU-wXBcUiRjs0uHWsmKd6TRyvIf8xl3gPlkCc27M3Be6xHeX-d_7spde4A3VrWcGa4Tsa4tP66ulSGM6qAfw1iXhPt9_AcKHuf9hdFsZg2NfLYZsq5GmU63j3UtsOpdJKWQtzFUnlUkUC8YSg_eUajZOayVFShyM3VJalaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXJY7nXhfLduGfduPaTBgxVjLVqoaC8LG_o5Q3eYLUxNL47dyBntYGpDAmIzN8V8WQL3hnW6UDY5_ERppSYqs0_1c3HAkrFToOQ7EVpgMzDEjh92kR2SlVouUx5bFDjh0mUXcNeZvG7m7MqQhuiQ5gVWrsUjvwQacsRIEjmpgWZCkqYg8hhO--EmaEg4I6m6Bb-TyDkw4OMYD8OJ3NyZ5l3vDj2bCs9-cnHfKejd9pD0bQeuuSkILb4mC8gPzA_waWPyUaIjRBMRRRs_HXNpboCqatqgH1xNHfo4kyn4NSreorTZOesMANOBXsaHT23jhGbn01vLAGmdQEeSRW6cGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5zh5S6T40BoQ6_xAA-uyy6bskTf8u3wdihExntiV4wMQBichMc7uMzIib4o6TnmtxpsRztVLpPEVyissX2CMLaVQreeNiOmxpsDJKnrvT40L8MCiam20GSjfEJruRFA-_9RYDVs56EU5LjX1E8lJcVJxYMz4bwpRAxkKkLdCfpCXuoYhRMoX32gu_9BoTqy_XtDNAuh3FjxUdijMQJ7t-wWxHTK8IEFZ5NXqMZaoTlNfj7lklIkUmOkvGJk97dhcuZpRlnodsRAU-AXoLPSbAFtHoz2svw3-OA_A-7C5gT59Kx9gY0QmQzKcZxOfG2bcVw5lBvt3a89rYzcF0mF3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKBVoUBmAUHj-mw6KeQBSjp4axi5xEOwYt-EZNBDa_I-fqBIhZ7eB0oThC0D6iiGKAyIbyoouW_aZKaZXTZAF8dx7DB21QJ3Qp_8rxxattI2YY5EHWxpoaliRQcEOor4LZeVGtLoa827VqJV35TsTvRcBfHQUgof0CI96zp9WMRGAYQcbpQ8R6ikYCABamM31OpOU2i2r0byZMPnskv9GMXoBQByQz5Mn26_4WPY2Tr7XYpE6Obj31x3lasQIEWKp9oxkRkgo-HKFQbOdteFygPkmzkI3eiXsjLkWRbr7Q0RzKCYNwvFve2A8Q_H74-Ti4enebarXZUcWAHP1PgLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyQNvHAGn7EtDGTvCexcHvbXmOy7D-p-cTiPEyZ6c4qqAwuKmsODZ1jPOlfaTchiKrqIWZNU4zTripJz6euLf_Ny4eQ8L5hsRvzLyNQe-MtrdLu4VfuJNByBPrU8_dTbtmODnzEUHi4jSRt2EqQuV491NCzAdno3HQz7jHnmhwaJhXYPGXJ9wgHh-o6gyHAKwjbTYigVYLi_PH9a0tZ-j3cIpR0wPMi99-9pqhNEJhbReWBkkmIujKqWtnshxXPWiUXV_i1GsBM2ct_Twyy5zsMTw3JOAko16oSeb_31uk1zlXDSoyWmSR-cdG36-8AcM1YdFTwK1SJG8JfCdxRhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=Oo9lrWavcUpljtup8Dn9kLA-gHMXNxYJPmr3HvAyO9CtNLofvZoURgm1ezF_1mkjJ0_SkXSf6Veyh8C01OBGT4NkQyKKCtXP7tO7LwFcxR5v9VOWer7hpZM5vQBrKuheuHJfyfC1LPd4EA4JiTQWjhUll0bCVdA6Ld0wU1d-jztzYNExd5ba6HWoNb2oYAXYUcXW1RpWmh4ptCGSCx7wF6p7vLQqyzpxuWN7DtKlEg9pts1YWPMcoIQcYD2MipbfpZbDtojRLhGlh2ZqaVBSWAWxEm5fWzwZQBYEw39EWbf9FIgQODau-0f7zjVqEXQOy5DZ8bBHFwTPIxJ9g2vnSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=Oo9lrWavcUpljtup8Dn9kLA-gHMXNxYJPmr3HvAyO9CtNLofvZoURgm1ezF_1mkjJ0_SkXSf6Veyh8C01OBGT4NkQyKKCtXP7tO7LwFcxR5v9VOWer7hpZM5vQBrKuheuHJfyfC1LPd4EA4JiTQWjhUll0bCVdA6Ld0wU1d-jztzYNExd5ba6HWoNb2oYAXYUcXW1RpWmh4ptCGSCx7wF6p7vLQqyzpxuWN7DtKlEg9pts1YWPMcoIQcYD2MipbfpZbDtojRLhGlh2ZqaVBSWAWxEm5fWzwZQBYEw39EWbf9FIgQODau-0f7zjVqEXQOy5DZ8bBHFwTPIxJ9g2vnSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9TX1LHEZyjhPgVWJxTZQFdE95nuijtCOhHPKbsU9DdCUd6RKuQFbEN3baogCC26FDuSLDU3puLHzas9Z_pVlwNUDLVzTZH2bFkiR7xncpdb5GRkwZgkMyqyFE7AwiIE23bf3Z43E_QIEdtUyn-UItl6JU0E-qOY-blXR81xi2O5o4WHvigjkyp2_Iaxr-k8miKfjn0egs1qQ377HWWwyQa37jR3HNm2pxYPzeBF9YU9XNQwGEZJq6NXk-iYr-NpkhdBOrrsZDzXnTR1Vkl-xpYVoP3HAqXohAtliJMiHf74W9Xz3cKy2oW1wUG7wgw-4rNEqL_hs3jH_Iag6tcZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrtF9nQNuU4HSqnZltANiyKGD8hysm0E6SK13uf2mRxbXd2nE84hcwzPd9lnYXviGcnyCNt6FiNWfBYaxQKq9ct9mjEdF7kiNEddARZcMasmZhjWhUBsOVuu2_mguaXsm5m87LiVqotOkIctDSSGAJ8hV4U5oDyUPb6ZVwewkZ4S0QHxUwoTHskUbm61wvmrktrKrM4KmNvu9H77u14ZFvLnhWxJNCKR4oqsvmSZqdjAmTE0guXeqAadO6OTzMJPi6_08LMBQmTBd6rajB8eCwAKWh9hWyvqC14Deap694yG8Vbx0QAf5FDKcedDITROHsOLsLIVYL-xUNEwmmYmJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuoioPIeykGZ1hY0jBvs6pwbPjWR3SKXvus1CnMZVKdS7lxUe1uWla8xidf9vFJd_yvE0xmYi-OyP-ongYgoRa-rlYXyBOUkaWwdrUBJlbNuyNGItfouathxSKnZOvQuoIa6TX11mWDxt2_t5jk4ATKIST0wlYWJWun6HAdY2IB_7ryKrZK6tw0lk2NoERcT7iLMHY52XHQGLhISi2lEN2zDW1FGIKBE-RB7k48OOUhcZBlXCLhFURTpNQ0_L35knT_MAEcF6vkBl_bn_dO2yrqFbeVXs_VFmHENy-4ZYhJNp4oxCGylQdfzjx-IQww5YCZFQNXU1JfZTgo1Q6pKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=Y_N-WFbDz5rMhy05zygG0rq5Bwe1gv15BE_vxhQdRvTc89_9Y6sEDEFICK1Cuds4_TbmgMAnRhZuf0OpfIKb3Ns2EBGVOuK48h5AXzwOnP1PiFgIZk-1hnx6gWCmtCcaeD4r7GhRpBIImOzNhUe-5EnIwHiGi24j-GkFYA70A2yx9HcUazGQLJoHT2hcpjVq6AGYmxij2CxlcdQt4HczpahEtPAYsXzgLbdxqxjNO0NOiknjBH5XUbpG9q-OrJdPF5d3z2ICeneiEF5B294p9WnGBWZCr82vda2Iz8WvDPCptNrHrQuOaAHBcPohxiZdvwHs22P94GyxYfgEF6FT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=Y_N-WFbDz5rMhy05zygG0rq5Bwe1gv15BE_vxhQdRvTc89_9Y6sEDEFICK1Cuds4_TbmgMAnRhZuf0OpfIKb3Ns2EBGVOuK48h5AXzwOnP1PiFgIZk-1hnx6gWCmtCcaeD4r7GhRpBIImOzNhUe-5EnIwHiGi24j-GkFYA70A2yx9HcUazGQLJoHT2hcpjVq6AGYmxij2CxlcdQt4HczpahEtPAYsXzgLbdxqxjNO0NOiknjBH5XUbpG9q-OrJdPF5d3z2ICeneiEF5B294p9WnGBWZCr82vda2Iz8WvDPCptNrHrQuOaAHBcPohxiZdvwHs22P94GyxYfgEF6FT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22753">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22753" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUQFJ-9uuCqlLYfPEcp-7EH7zxFYj_7-IXB-5p-RDq9QiI-XBndH0FKOV0OsbLRkVakqKY5NTfFFS5lu8e80XnfSlzwzX2drNg0owNJwICfBtA2UCFvI_b5ccS-i0RhAg5XlRBGzXVtBxIqEGqMl46AnNkaIHkSxb9ZLowuzwfjlJRvCYwTVGMG0XrLA-wA2uR3sgG5CR7198KPLxcfLZ4jnnrMBAxnw7cWl-zu2X96BtYC3GEf9bKxjEjxe67uiouhYScB5l8pWA6gaU9Gs9tFSo6s0ZQX7RArbDhYchOLb37MSYca56aifk382QJ-EDzq1vpBIXDMAE06clzThLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq9drA3_-JPZEsYSdwxL3qTL8kea2eLphzWhfZ23s2hE1BUOEyJrjENNYI2CM4vzICECvEtmdonso37fmcGXZkZf4fxFPfkhi_ksvpw9okdT-gBl7eg5jjChMuIxs7azpo62uem2EJmD83yw_kp1-TPoIt1wwhPFSoLg8dAwDrpY8E55iI3P1cH9YbGEwr5zNnakMWIm7TgUSPazcb3Mgrgs3h5soqOLxURrP2twchX-V3cWh0d-m83WemBgzSQ1uLrjKNu8jjYasaPpHAIII3bUd5-pU86LXHN7CkRqDmUvYL3Q2CJYU4J34aeO21T0ulssNsEbn9fNjmcYcArmsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG8BDgO85I7UKQh0f44ousN_cCXiOFUMXBRz6QSqMjvYoE8ZETPLVPianmwYFtRVZkvVCmtE2xgMc11k4B8kjxHfT18PLkwkYHg5YguchKXqGxkOsvYQC4Y1VAmxUST3rwQFWwhBoGc7m6yHN82EvHSEKjbDlAQh7q4VpAVwsaWoo8FEV8OH4_wbzB9CsZC6jna5zA1M9WWcsaJgtkCWY1iIvBcd-Q_szw_Y4SomyrwhfuxIke0LsEEEv2ALiwGSgirHxO4gwpU31oCGWE64eKPdUs2M751RwYx8WWa1IUtgNHWOt8isPhq5ZeAOmamppCeANbWNnawuBpsw3Q2vVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG_eGwxLOUdaUVBZMzM2kgf0W1O289OduMn8qtPOpRPG6TTsdzXTYIcpTShhHVK13Iwxkh5qu6NsbJYH9V9Bm6IVdAEwyvYmYqF2HSorjNJvvOuPmCKpst8Oo3IOkQETk5ULspKKnEgY5dSS2_w7TeSqs-mGzTbkWinPaMc6Dwwbz3OWLawsxw4aqj34xl02eY86lQURavZ45xVoSyRubb93sIS9Lle1FNuL0MO9jeU6rGonZa6eeuca-3OSP_mTBP1oW0cEyZHfdwOlrVF56bwMZ2NEOprK2d0hbF7pbkdPsyckMJJO6BbIZ33zsIjDKmihTvKmGiHfx5nsAdrhdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bImS85j5OBQmk8LKQh2SxG8tzJnc68Gq0510faU0NRVDckX3WPehTTszzp4Bq2rhrf8bMqFITUOmD88hZtAZ_M9iEbLOppOdWI7CgBdWOuVtCZ-H2JII7w1rMxUu0Bbv2A0jdnXvbOxyxAT8H0xlfGnJhOA23IU1GPgfmuV4DjBP_Bo28JJH4Sj_9BH1kiRAu1Q95tVqWur4lY-jD7A5YvQFE5IBm3t_PuNEqJiiDmGs7Sf75PFQHtV0ZDDXUUEhQ7CdO9SyRRB1PD9tSulNn4tF-0iYhyGHuw0VklNHYyufc_CGZHzvsGRvm217T192s7STMz0WNJVFTljIsTn80w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjacaY3yNcYS6z5yucr0dhlzis53eUNU1PLpmxxfwLmCtl6m52WUDRsmTeuKrohWjhXJxaJ6DSqusltDDYdr8X_X6I6X191nHn-0xYd9OkvlAVJsI2MR-sjdXhsghbyxKQKQv9tjfarEYK0PVPyMfL1DGyGy9obJXhYBtZQ7G-blJeiBXgzxa0TwqtmOdF1OEoWgOa8IpUKcWPMMEsuv-7seA0VzR4Q3MvMvaezWiUYvj5RktSju-51iUZq8B1TyLaJ16UebuFUJlLNUyVT27Pl7XZRlD_15niJZ7L6hO2xqMJisIFyVM4EbHg8ZFp11CskwtVY_EksQKbg5KmGWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekglw4KWN3DOThu0yXXFzcw8XnF8e-HBD-D1Qu4jE_tHMEvZ0x_wFkt0r3E2Puw_RupTye5IuQMCPHjV4hs3pQdr6FI--5LD2P5mN_Dtfu2P2WgMIb4Isti056jgRSRzGHWNA9oihTjeC3J-15yXrIllwwXQ24Zj1q-NjLpSdSVSQgVwLKVPrw1hOPNtT3JL9Sjpc3lH9mm9HfLPYpW-i8A0voYkNfFiBwF4UV9hbG2sgObue8LmnT78IQ0ZcYWoWFyErISHDCh8X2NbdNgg434dxAktPFAJIXO4tOcRxN_fN0HqGchhvvTlgHtuus0JP8y0vyNtCoxiDXAwiobXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=imnpGkilWRf2CnMeWpNghEB7HISVFWJvqGHKwLJmrsh1Yv9yVAvX_Vm-LKfY1oXAb5rJ7GG7azrxfXmjQZXd4c2rCavdPp8YZlFJ0kvvlEUg-AQJVHy3XOvJike7GhfELwLtw8FU78a4KalZS2i1NT0DYbB5Nq3az6bFjBh95P2PUpT8nubCgMZ3qPEjkALXHnTIc6z9aK02z3lru3tzxw0exUo0P0Cg7rWKa92CSj4_RE0_KjeeGdKqnEZMrDhXda7LemH4jBCPoa99pKxIntPD9sSak0tgdxdOrb1tAHFnXpLec61PG73Xdw5StHXowloWzrzsXcNuo-PzC2MUhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=imnpGkilWRf2CnMeWpNghEB7HISVFWJvqGHKwLJmrsh1Yv9yVAvX_Vm-LKfY1oXAb5rJ7GG7azrxfXmjQZXd4c2rCavdPp8YZlFJ0kvvlEUg-AQJVHy3XOvJike7GhfELwLtw8FU78a4KalZS2i1NT0DYbB5Nq3az6bFjBh95P2PUpT8nubCgMZ3qPEjkALXHnTIc6z9aK02z3lru3tzxw0exUo0P0Cg7rWKa92CSj4_RE0_KjeeGdKqnEZMrDhXda7LemH4jBCPoa99pKxIntPD9sSak0tgdxdOrb1tAHFnXpLec61PG73Xdw5StHXowloWzrzsXcNuo-PzC2MUhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2GvkU-jUZBkQkdtCy9hFgNyhjjLFMGF6vznxevYrNMEXBlxTf6f75Yw7QhWhVMWy97m89RONZrJvDPZLh53gVpXm54v6nqVzz-fQAgi_0DhVsac4zzRm8ZOb9HdwEPSe3Eb_hq-Pa7KCN239JqbvznFjoIsb_oLWh6Bs-g4yPSb5znj9WjbmT4qEduhjAcFz6T7WIBKHMTyVZqmdFSKMwyTYQohexfsk610X1oxFsPHxEWnajqqmPKoiNCcTTr0c3utWw8QoRAxhdUxc40awbcNGscgrwrhQvj9N68pjAtrbuTqB61jc8JVFLo22RyiuKquIccenmBkCd2PIb0Yvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTaAN1n33StPX0Fj_e1uMVrFnS6Y6K-2E0oJYSJg1DAZIaFGBl1ipNXKjVL3AFuBY_7mqQzQJ73ri-9fTG1n6Cl816exRpZPr_LoclDwL_iN2QIDuvZEXVBRbRYEaZV5yuAPU49ERnPBPM2LjfdTUm4xOX-PzGq0FSKz2T_NSYZHn10a_CF9Hu1jHpIp-1dFezonYHD99LiKPDLLTiHn7aUKUPB2GRJbqxtf3cgnHbEtPaCVdf9amaTUQOyChNCNgbEaOjfqxw2h9pbojb89d6pYtzjpi2jyYhwHM85FN9NEhjUAWUR_Z1r-_24mTgLn3kan7Hzs5wTvuGPVRdFmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVmkeAfssHyy7iwyf6PZP1YJIHlqyU73DUV83YyhGqecHPEZMoy4uKqCNyz9bDIAfnkNdMgnwOUZT4XiAeFKdSJT6iKiarUl_uIrbHOjdUV3Fc62hOphJ9texGSA2SP-okDiosHtmL_jzzl8i3NVYP7xcZrgjmH0SM0P-LObywEv8TywEHE7q21gFIcVs4xsiyUeQ2EipqIjBWCRQxvwzeHNyTwl7l8AUDy--k-OD2ZeUIW1mFy9WkfSD65NJTJwiFt4TLpLTJ7eqq9ar8cmiOENVP8rCiLhjjNG4BjN6UMHg0Ldx8tDefhz1N07qG1RQ1O7xUF6nQUwZCFyKkROkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuXpfNxNpmf3nEfFMur321yc_mYvvroLzSYmbmoSq1AL-W-5oByygoBQ-uEnmwNHJFzNm3_mT89XI742kdx5ZEjyESqqgd5AkrIifTZvxVTMsfpmdvKa-ewW0taGVgx8MjDd6hxJApEryg9ziLoKLwrcE7g7IkUyw6AqwVpabwoEvjERDbVICsLlVAMDxGf_isrc_IAxFWglFkZwNI4dTig9j3e3yurl-59cTW3bC-OlaO-D1sZ4WrjRNEy4qqHeaVKYFhJ071j_yof01ov2wxalCmzxMl0jQJr-iLpa9xlxzg0i88ct-7e6QqtDEBuH-lVmT91dSWCbTS6EbIQ-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqh8aOIZyOh-w_t1zdEWkwy9A3fl1a6TYg_uQYyMiOYBBg3CqVYgXbYqNDVgW8uaL3WZst5QtlcNs1GuI-azKXnMdjQ5VFnvU-hIuOppQvjyWkGCqQkta8y4-0gqKRFlg9AgsWZvqK33DxxkdyMx_PNIXjKld83fRaaQ07GRIndksq-C1ZTjkOwDLBJjpzIIK2O6NqfRCFFsrfWqBvz8BCXb8slVvZrA-on2m9nFAC1zIAZMEZOv4NGo38WNYGVqDebHP7ueBvrNHXijrdUM55yeUgn8_jPjkipaSpGu5-f765JPkTNI-pk8vXaFUyiQ-nFjq2dMQoBPLKOla1_RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx_HIPTxP1FanqnTEJ8YmJbq1Vq6Hv4S-2fPyyQVLg7X5CnoEZFLEHXCJzgGJswMCeQop0mEw5it99VkuRplQdWWkrHM_6eI6cR63PhSCg7h0rOQPHp40GNoPBhSu7ds5KZEE5K9VYY03YIbWCDWkNKQ8oiCPshbkUDNCrjtxGWKBm62NFAQcCodn1ei01nCE6yCXh9ZQ2jUN7MYPK99NoxyenXK-6JxFevI7ZVopWc5BrZ8itWmZO2u0rWINhZrOMmx5aV9dXueqriBqD26kOdVXF3OIQnWCydDFDGm5SPVuR9CnU18Eo2jYYyePkXT6m_GCMQXHafvJU_NLSyMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=UPj82uSxQzUTXFSjuPJbjWXMr1_DzaVVU4W3xiNKxhYVKfFsb-7VQZduJH6IGaucTqFmPMzshFEhYNEYm051Hwx5R4Ht4O3Uth7IMPQ2N9uIphfUVVRozsHnjhwm-wbDuNY-qNJVIgNkoHF_5wCsqfZW7Gnc1EzYTU9b-YgUFDFunjCUft51urZMhZPvwI-w2JSFxAcwCeH_jstk4av-8FM4wKYIM9mk24lYpSTUrdiK-Wndqv74ACkU1cMPOt-M7ftCfwgvkI60GUUe8S10_kpJWjG1iU0BaSWV012fgmVLbRzLkUqt-bRZ0OCilIs3TE_yb2aoFK4SpW8f48B8jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=UPj82uSxQzUTXFSjuPJbjWXMr1_DzaVVU4W3xiNKxhYVKfFsb-7VQZduJH6IGaucTqFmPMzshFEhYNEYm051Hwx5R4Ht4O3Uth7IMPQ2N9uIphfUVVRozsHnjhwm-wbDuNY-qNJVIgNkoHF_5wCsqfZW7Gnc1EzYTU9b-YgUFDFunjCUft51urZMhZPvwI-w2JSFxAcwCeH_jstk4av-8FM4wKYIM9mk24lYpSTUrdiK-Wndqv74ACkU1cMPOt-M7ftCfwgvkI60GUUe8S10_kpJWjG1iU0BaSWV012fgmVLbRzLkUqt-bRZ0OCilIs3TE_yb2aoFK4SpW8f48B8jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=fxMT_SzfPU9ZL8KPkAiF0TI3PAYqLDd8vSZO1Ym7FUG1s4Y76I7_egKnDv410yMvBZE9M6I2fuH_XOrwohba02o1UYjSwKBzgKf4eqrnPqVFO0ZH5ng9ybfkHOTFRe9TGBBHeilX_aJXXOeD7dRYyBNLMMIOmAWNfVTBzOrG6lVABjJQQxvB9iSyelH4Dkzd2IhCtobvzJLI9-Ie-me4NrayJ4dliQsjYC4aCQy6BDHx0gs8uTNMwjemRCPE6IfJ06oX37hj6P1BvipMXV83KbdqP8f_q6F1SQ-4L28GRn3zkZ_dBHDvvqgrCtnq5UGsPJYcR6Kl7_pFmo8ejCZUTTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=fxMT_SzfPU9ZL8KPkAiF0TI3PAYqLDd8vSZO1Ym7FUG1s4Y76I7_egKnDv410yMvBZE9M6I2fuH_XOrwohba02o1UYjSwKBzgKf4eqrnPqVFO0ZH5ng9ybfkHOTFRe9TGBBHeilX_aJXXOeD7dRYyBNLMMIOmAWNfVTBzOrG6lVABjJQQxvB9iSyelH4Dkzd2IhCtobvzJLI9-Ie-me4NrayJ4dliQsjYC4aCQy6BDHx0gs8uTNMwjemRCPE6IfJ06oX37hj6P1BvipMXV83KbdqP8f_q6F1SQ-4L28GRn3zkZ_dBHDvvqgrCtnq5UGsPJYcR6Kl7_pFmo8ejCZUTTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3dOrt1r-1Ujgn41DSiZ3ntfBE38a3P2k6JogJEK4rjlTNVWEpZKK68fgFLb5qhIBWGdCzaR5NZkjFItMiNWt2w-5V-YVj2TkgtGOKEWnvUgW28GEo92WauN7TY4ro3Glml2yUvynxxerNgSr_BkZtkGWxj_rLw-tJmDmV6BbKCL5DhWqWhItRUFWPtYpQwwm2eCQxov75IljStWWl_QfMRAOXI4JqrD0RbokTXTPrEl9BFExvThx3GkDkGto6rMnIXw_7Yuj3hDDTS2-8tTDxvVO5GMHV-erWnLNuRitdORJ0gfgS_GNsFGFahAYTCC4shcKhWrVBjXuJ336jLlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE6L1yGtLW53mBnJjl6u3c95BRWLEeExydlKwK60gOqZrDsQV3xs6iS5pFJOwNZD4tOYRiYvN0S_IMZZ4p56ovXjFz8FAtXdWjEmOhFsZa6LPk24ZxRh6iig498eviaJ9jiB5kaBA0kBDo27ERmCIHvET92teEwrb4gZS6RH1vHKtVfyDIjHeWaDyoBD39zjiHb-Y9OEsdOkJgZy9vbK_2NLZ5hXtgwnnRGXlh1A-DzvWFXEAV0Kmu29LZknM8ZBwrkIDixowJ-2V-3bMovikjyh-WdfKIbpzyWcW-q-aZb6LqjtTNnT-WMRuk9G4GLaFZUuYneKF0pOINNrIdWkSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=k6RmHnfbi3bpTSS8ddmDz7WIrvqw29eBMqntdA7tKAtPYompJf6Y2_2YPn2wEt-T4Hnvr2xtBetBBLy4RbDq6nFjR5h4WAv0-fYDkszlFFQ9B7MWPfNB9_OzkcFZM91skVJj3-P3bfab74sDX4CvpIafpLpqGxOcqVbq_a9zDu1mUT0L-vMoHrREbj9Z0Yyx71OGKZDXCnAVtyyb42SRQNTLWDN29d9S0KjFFSpcXScCxjB9CXFYzDh3HAyLhYKT3UbpxrPtMeWDH0F_M7Abq4l51dDMgIL5pe9YYOL-rL7vh-MwQMQ4uLIehEYk5qjqrFF6bQQDUbtEoaZRc6fvfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=k6RmHnfbi3bpTSS8ddmDz7WIrvqw29eBMqntdA7tKAtPYompJf6Y2_2YPn2wEt-T4Hnvr2xtBetBBLy4RbDq6nFjR5h4WAv0-fYDkszlFFQ9B7MWPfNB9_OzkcFZM91skVJj3-P3bfab74sDX4CvpIafpLpqGxOcqVbq_a9zDu1mUT0L-vMoHrREbj9Z0Yyx71OGKZDXCnAVtyyb42SRQNTLWDN29d9S0KjFFSpcXScCxjB9CXFYzDh3HAyLhYKT3UbpxrPtMeWDH0F_M7Abq4l51dDMgIL5pe9YYOL-rL7vh-MwQMQ4uLIehEYk5qjqrFF6bQQDUbtEoaZRc6fvfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT5leFh0qDTBdbiu7LR5PxPDkh-NdLK0S--cC1IsTQgzyOx2f2ykLyF-3pO5LjlktlaF3rr1AqCbL7YBpd4_l9ilEbpuD3IpKuRMPeoDwxI3HIbmqxlQMtVwV_qycF54EMUmAEfXqScpUgbbBz71-6zQTfbt2IUAyXUEVCyc4HevJbx2_-nbtJsBtSkGeCwiQswrGOp2Vqlf04a7N2MlsS4C1Hh2iI_Wm_lSFHWZxmBrSCJEg-dBGoMVvwu0y3w5u2qzK7lfRfQB6uW3aszeQrM6GNiU88vm0U-BBgs1oY34ZAF9ql4ByFu7nGrHfBxBnIP1gYR41LQt6ohdMReXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t92HMeuBuk214DpSlPp_e0hUEyb3RfLrrwbdSqCQCMTwa2Xl83oGGKi-TS0siABG8F8d3d1SxsHGj11fm8cw_KZy_fdAyRJMn7mywKPqvD34pehjxnVsl8ThgkuInuApKlSq5eI0_tNShXKMfGLEF-iZ4Lq65INGXjen5HnuhNmRj_ezEDW-ZOTE43mF1ZhWeEIeYN1W_-bAARKdMgpeh8jMoskLaeQNYlwGRquBnQd9OlKQw7b0tFCFpMjRMnFgY8vLIFj3j-LM_Aeoh_3YtatYyzP37oNVZ0WyB0Rk6hrQp7CedutDqQJrMZCUIwdoPiG58sIt6e5sGzDizPq7OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njSnm0l4u0Uu43u3_Un38Ekh2HTCEy-ogng_pg2st5_3E1xTShgjd53Kqp_E9hl6roj88oDp1FZvVfIYUfU-XmNx4bT-7E1eANbFhUJn4SeunYyh3JPIlmuxJzriSGYJCIW3gs0S1574G-AeVCMNCwg5QPBVpIw38wn0ku3viDhevFmtjURfDEi9CFMs8-GmUXH8J2YxJnqXIJmytH_F_xxt_UT7E_kscLI-2BDyHK4LJKDjtueFeaAbP1QB2wV1eQ7-qaDLXh6HnA8cztp_aVF1wfTmZHc5dvTW5PyY3c8DqTf6TtfGNj0Vt9hTcympelE9Tzi2FpILUPjqg3Sz4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJzhFheRN_63D-LKnN4dYtvzIdZIFVmV_8wErRUw5-yoNMEyPI2YVwKj9C3Sq1PYN5c9fD6dXXEwEh-PBMEhvNDL9LkM_ubYj7hQtB435Di7Jp8OvGBzU8hd8W_NSwf5uPwxofUBYQgbRzX4NlHXiOQ62o9QInW5FHTLeBwPAdFFIpn_B_PQkrroGnHoAvk32NC-Qyinv56bIKNbcADDGuNqIOybxflKz2LLhnB-YC1zhzDbii6qyqCu2V_iGYVY3MVCLbScN8-pU3u5V1esfxvG-fb_WU6yfGMdXn9GLjAv7Th7QRwjn70pTOpkvrzoe7i_FDnoi7TykZ608YjmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeGQRP4TZ2Vkc5e9VzafDbhk74FUKZwydFas-sxQMY0yOyeKfO42toa6xqTm4TMBnXlUMo0Sa_11gvgv9mL0K2yAe4akuk70pE3MBbt6DYznDz9lYK0j68gMlGHQf_lDRNBeBZkq0-TFZMmoL9zPm8zWwdoWI2tMbV4YubRyz1eAJ3wKWlNC5MDqSuq2H6bgG2ofO3-RUt9DbzikfzgusVo5brrKt9Z6TtT_m1B6IMggu_qZQQd7lZYvmZjdXTsTgIYTnVGc4_n_WUxM8A6ZLf1ZsNFH4Hk8hzmx7D4VFvyjrxZ_R_BFPPrItyqT6ud-LrjqZbs_foRCLmboKtqYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0XhqLNq_qZnHvxAzwrAxRuo6Ezinfj159j5kGeMqF1U84EMnXJKZvQ6LW0kEw7nRb5tN445rvamqE0bQzAD7tm-CUUW1tMYrWzvcmL_RTJCleeWOeza_fGkotcdW-DAKb-9MI5E7F0dgEZ5bhlLO35QBsjSXx8peONeTR8hzsqZl8ly5q9I665fJGcNQbGTWorKBSTMhgdBVkGJ-23mOgfodUzB3nN5mAE8s-Ylh-0MjeyI-gqP2aEkAw3ZwpqSjT2Nbm4-y4kelHvlRidBAvFSBKdYfG2rqJYdjx65zk2f2ZyQFl16t876Dztk3yfbJbEZnjgh4dQssEmi3obYCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpDBLv5EL-oihoskuIHp55cpL3Eq9Xf47b_YGrPxxbMZqtW0bZXu-RfI5wMSd6iPmOX2E55AgmGwAsjXDOxptIKhZ65ArBSaiiUDixqf6lEx_rJF85pA1U3McnA4Ufravoogufc7Rq54BzUh6CkbquB3a8f9yF1_V5MX5_JkmMRPwxvUKfU0g4ST6zE_q9q59iDFIWQONCU-r3ZniYMPjotFwwUBeR43nG0plZl4yg3pVejmQaFXYLTlOkNdHlYiUTlhWpsYArbFTs--U8kHk-WthMvJCZhsy0i0srV4HUKWtcnaXmYq0vpGz8le3tNLbCNIUhuzlYtDJgCM79OeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN18XwsqeE9gAZSK9rqvAshlGV7il0RDwrzf-C_gN0AnkkVCiEirC7hbCORzIui0-EBCqgWZVPipZY0X6H2OfQlKpS69u5hO46NZahxp5oY0OOQe5-8cwGN3Nni75o7CDGxr-NUx1rpcqan_B8uU2e_PSLr2aUxRH9f6NXeOgn2PDt1F5AKJPsiDSg25BTrFPnXWjbA2-rXp1kMxp_ZKCFUD_2Y5YRUN2vLcn5LMTP0-Tw94MLYCn1gtYL3J7-woF9pBHEKfgcFiSDxEDT4lcBb_fQLg2uZiihbPjjuWySPgH1EDgfeVZLU-z0Pj-B1KA-5Rj2AazdJQDOGpk1uXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c82jDDEe1xijr7y9dXkZagAA8fiDAXgeLAhyHB5yMTX7JoXairP62JCI98klW1cur12GZWEeiz9wDE1fH_sN2uEZemYq5qB7AYBjRkafNvx1D1Su-flFkzjmnHF0d0fgHyxMhqAB_OlEhEPTzp2VhJ0HijJW7lNLKPKPtQ2U3QfPf8P7wuuHIABGblloiYfyj9qBk0kzVuORkb4lPiUA7TIFiICvY7AUEZ7Kcc9SFP4fgE8efM3QSm4GtRjJ6bjrVs6GsuL3hlHUtWuV48KPEDzPXC_xiGYGOKTkSS2tlYb1kcq2uyyfQlq3xvR_AzZGwNFe5AXbjUHswqs7CXlv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljMyPE0YZv8Ir71MRiASgUCbORSDB6SC64NWBbg2dOExH7ngVbYxM0emri_-ioeFEZrRi9g-ei2f1SakeP5avKDxxUdsyIkZ5CqH8lC3NSDMfFkRtKNmtGWJy4A01iAvP7MTLrw89ob00doy44IIshPVPM1zYhXofT1IpVt5T_b9Vr-a8s3UvUD5gNAA0HRbHMUfUIeU5lLykzLOyUKuvJPO32WnFts39qnSk7s9bGrc4KO3F5j5i_jVfqAXdMjGE0mzBNceq6G9YvWOIVlv4vwqWpi43KZv9FrSW6S8GRndaS9F5s-Mw4j0PyQRwwAluJa3p9DliuzMQO4CiYdv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYpXBNXKTk_X7yIlBVjZbY0xVVgHUg_od7Zzfm1siptDu2uqUTEffMXiZc_PHjQwHO8UfvZTb70yYRjLKxU2h-POP6qrUEM00T99dU4FQjELczNCiyhCYnAjBHU8X_HjB3CuNb2V6ki1yQAN2bzSALeTadPyDM3FhuCL7h13OBcxHYx_71E5zo8SYCC0xy-F__-DgrmCXVK5Q9UWyxibvLkYWSlFBdM4HfKgaEDzQKYnqq9pUueiY0XQfS0GiMjFgMbHgnTNpiikHndO_YSr77W_iusUzxXPXcX9LqvdvZWXk8cpBrvl2sfZ429dzCtfYmvSp_PIHlndhRWYbPZJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxwxkeTo7jkEvvHKsfCIiXHhJV9OjaeAkNsx1GbVlAxaeKKChojWVEZHbKeTXqQRR6MJALBO6gubRun9VUSWB8r0iRpMpstuRs5gd0a26l0h07lN_gW3-8uKLZL56SCWMlhwOP7RuOL0o9WPLqWN4MLri3--NerbMut1Zw_KiHjNwd0rbjuxPcrKeq3ENUMD526axja6LySA7Bo6KCrezKJmQHY5_sdyvBCJ8PllOLcdvg_QHpQ7ziPHcMPyqjEgMqw3-Y6pOcBYb4Vs4F8TrOhtLBz9t1WSHKennhZ-1hjIeMUZUh8QDkXDojUIaEttkXcF7uEDLOqo8m4ae7QEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSHHReIXm-bcjQJbdBaUboThaVkFNu9NJGY5XNKP0aLdJuYK3FAuKCrbCA80mJSkjDWDPulOdl_GG8ScSnd1gq1QIMZxdAs-Tp_gM1sSU9QWzeuKM_G59PkRLjzwuzTLdk3_BVaKDZqcHgQBV4G1vfF89PJAPx7af2p1XFdTlY6_Cr3LtktYvx_lR8XrVcus-Bm-811Ad0IhvFcwqmyZPq-MPMpDKbSTsOlmI1wMEefcc85IltAyHoi-MrxbxD8HguKr--w0ULNyFNcXn7wkUFcvGL08HJEUILuwAW74c6WIh1y70JQj_Rl_ZvtPocsUewErK1kYRzufhrg6y10YIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UadSL3fe3NxLamypY44zodOlGctVsio4zEnWUwBCTjl4Yaq13eZGeVXE59ypcsIOp-aMv00XILlpQgkPJnzZ6_O1gcyTNaBXh8OyIGikme_wezoLoHzEnkVIknyj9SDNd3Rw8_qviozsJvxSL9CWkex7J6Vi0CVOr6WiWpwuwB0Z5sRLd5t1VAcIImfsf-CYinW7mAWRmiN9uTtyYOsje6zwGl1yQ6ZKdKfTYf0IZzk359mVk4506HlqRZm0s95kuHSV3hkYPbBXZoKtldjuD5gaMEf99T8s-XmRfOSo-dPYN12b6FGVTGIHybYhB7rNf6F7HOOREdLB085_gaXMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ6ANLmPNLJVa91UK_QU0-OBSy7tN-C0opKSkAWKwMBXH800uax8N9zloO6uLAJoLpTS2HA_ysONfcf9W0NvsqSJqDyEcUA60ThruFb-_1OcM_4lcjGz2GiieU5LeMneW9eAk-ylV2Cs-rde1NaCWtiFHXpYa1BK-_mwsoRnFOFRRt3FlAAYBHahsfVT7IALIMIh6RMzTEafVeCbiULzwl5yNwYRbuMOljDn29jG3BhiSH_79XXdw3Mb45r9Wqlv9rlxMa3sr2U6JWfHgztJhjjngCzZfWcZY1y7QiXolG6xduvkVDp_r3lAzmY9kbJytjI69KL4ghoNP8eYy7eU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=cIUYh197_eRlNzR6A3zwlfBPl9Ignmn9w3-jc7E0kWDMZnyk8l50g17i4eTraUnOlwQFGD9wcEXUVEnq2TRX3EXVXgEmZp5LHhEOdBu43jB_hguYnkj9Q8ZYaD4VoLAhYZVaecDGqBOapXy7a1Dub5huJZLfuINHY8Ofg2ztyq0DY1ccsP9nqODSsks4tYmOVM7vLn3dkFarHx9MTXOT9V-IDwfqJT3OsATt08J7GKQF6CeZblJZbSD58GHFfCOjzy9bXxTPPOOSwEaQzRWONbXmZu2OR8jSgQqpeYsDNzj8XPuWs_iqiB22XOCpo2HXy5cH6Sa_TmfsoFx9yeysg4UvpxeZSOjstq44bFSwXYCpnZ2_N_k8-FBDlSX-w8-JBwgt2TKrBS98aF3A5DsVl2KlKjMexeTXEiG4v_yGw9q-CSidT-dR0ZEqIHfiEuFzOf3J2jp90DFr8kCeUuDH-PsBcp9Pp6okOMWgn5PUZvTfGX3frf6eajOooZs1iK_r3PEtZbS-96-UxDtrMGZmA6DySQwQJgqlhrFF9p9dZdVloGnMEH19o5C42P1RGrkf0R7RpDIYNf3loY7M22I_XOWMhjKwOMb4gkEzCtuODyZpEl2zF3pB1vuH5QMt_zuBJDDKPMvA6AJKR2QFE87_JV9Da-LoY7UD6My8WwkebOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=cIUYh197_eRlNzR6A3zwlfBPl9Ignmn9w3-jc7E0kWDMZnyk8l50g17i4eTraUnOlwQFGD9wcEXUVEnq2TRX3EXVXgEmZp5LHhEOdBu43jB_hguYnkj9Q8ZYaD4VoLAhYZVaecDGqBOapXy7a1Dub5huJZLfuINHY8Ofg2ztyq0DY1ccsP9nqODSsks4tYmOVM7vLn3dkFarHx9MTXOT9V-IDwfqJT3OsATt08J7GKQF6CeZblJZbSD58GHFfCOjzy9bXxTPPOOSwEaQzRWONbXmZu2OR8jSgQqpeYsDNzj8XPuWs_iqiB22XOCpo2HXy5cH6Sa_TmfsoFx9yeysg4UvpxeZSOjstq44bFSwXYCpnZ2_N_k8-FBDlSX-w8-JBwgt2TKrBS98aF3A5DsVl2KlKjMexeTXEiG4v_yGw9q-CSidT-dR0ZEqIHfiEuFzOf3J2jp90DFr8kCeUuDH-PsBcp9Pp6okOMWgn5PUZvTfGX3frf6eajOooZs1iK_r3PEtZbS-96-UxDtrMGZmA6DySQwQJgqlhrFF9p9dZdVloGnMEH19o5C42P1RGrkf0R7RpDIYNf3loY7M22I_XOWMhjKwOMb4gkEzCtuODyZpEl2zF3pB1vuH5QMt_zuBJDDKPMvA6AJKR2QFE87_JV9Da-LoY7UD6My8WwkebOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqwNwYDZKbinJzL1GX26h6eI6pPHWY5LOql1I6ydeFZFPAIe5qWsC93p8VNWllKKv3Cfkt7vgizJcE-iWjHK4Qc_Ab0XaA1UP2bs7y4Nsd0oIA2lO8tDVZzY1ECeRXbpSEkBMahcw0gOHUW7XBeS6U9dtv6Z1P9Ez_csCL-wOOLhpLhZ8qEI-VnpcvXdV3OT4wkr9B2sriJm90pvuAv6lFQb3REgcAV4IiR6Wv8FUTu2c_74fTqIbC_L9O117meDIcn2O8wBwEiLRfti7b4NTbsHDrIYWmIf1KdFhuut38kE5sgZYGk_2jbkvuMLKQE5T3EZ1U0naRelDuMgPhf1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krLl19KGCLTnkY1erpDrDfm0AINhrMlVq2mJH-jjmZn9ZqGJ9p7bETz7tyJrfgXWV5WjvXn7WUbpibvW5mkPYqHBBrYtHAFafYrp5FqZrVowuHWGc3IjRG-v_tAqyXq1oa1ixy2teLh6sMtHRoOprSi9QmK_XKhs3OQ_TXh9xiriitQnoJ1hfh5ntdPFMGUoe9gEVZscoflpJLKuOZuyheBYW5k5kE9nWUavmVlwygGSg2MAHAlA0V-G_Yl9Lb-OknzwYylxKljgrK-88-_oBTxRd-ne1nv3EZu1YLT99JUx4tTq87kc--S83gKO41r1Gwlgd805DUIr71XXUAFGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZWcY0UMIaMdgMQUEjHyRLGj9lUDS2y7pMGTzxYkgL625vmUvE5KdKo4yHWwQHPCOFbILDXQFPyqGdkSC4EwJ7SM0w2Nf461MclQdIQTlBT0sNHRU8w1HiINO6kd1BuqJHnUZ6QIFgPD2qPDd--2zQowOh3xEIEh5mN76t8FHDbijxfylTsBCSCu2IuG6WFNfx1PYxpnjEiacCQh5Nnjh2tTV8f_PBS8A5TqjT09tOnfNO3VcXsNvDu_NWcSLSibEB8yrrSKa4zWIq9A7Rak3SbI1VZCaFrRgGWfm180-UdfUrRrahkKsk9zN6vVeSVMingUEKb48fCMJXnEa-jy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9S__-r1Pfcww7Ek8jKYV2HJXcaA6eS9QDL1gVemINb656cqJ9ZljShZYCngu366A59Yn5UixD5bwj6byn1RkFkHmvYJy9Tk7sbNhBDd0zcc8_98imwHr7aa1kTaIR6SIKZA6aF8R1CDDLWGaen8DrAQcjRJHASimZs6H69-Sc84jGA1Ph1pckp8FA0bHgn_eqbnTcho57TcJhPRfcRRl7IHyKF6pLbYYWKlIn0Wc7H1IjJc4_BBCo0YUkPBqYj563Poalqo8pKWQqcX-BWIADLZvX58lsGTiaDi-_FyAEghg3s-fOWV8rCV_V8zgPf3a8JwffOQ6pn08Ma2Tk864Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrbOAR7Q9BI7t1CsqRZE9Pn5gSEUkiVoInM12Xq6CIDawg1mBKXLVQM4ACmdDB3bVctE-PgUPMRGRpQRhG4Kadjg-9O4mnnIDxbWnJpQoqWVO2LdFRY2ECwUWjNH72cmq1Mx3XBUofYOb7XlDniWDRlojV6SWv2PymjIDVi2yJ6bKmGDpPS1jJ7-Ya9xmnZR6T5YqBGAZe2RZzgQmM9cs6OiNIMIjPYQFEhJgGSY-AeU6xkqYR46huK3t4m5RVeYBmXLP8F8LetWqC2bCl5m_6juEy5rQvUBhyUSId3xbe7xWc3Mai6fELOqgeYndwYLABxknPdFhNa6tlpufs0usQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PikNnz7eCc4kJPOQo5xB1xYWQHqFbLJxmuV3iLrgcP4W83F68MhEIuvLlTPxn3ExQRf406HkwIWa8pIQuTTe3_FkiGCbqZPkXUP2c7Q2VDktqFxUtwiF8qSflrNjzW8PJ2rBJH44QPHAR2KF7cIt5qItVJOv0-tS2YZaR1CUhIB0lHRa2BiOB-l7rfcbod81JmD5reCd0Fp-dOOI2HfGzUk3goN-Af4lAu7ZArcKl3EX3iZaAKxbYnJ66ER6ZzfnGj1TmXm4WgP3OJ9_Hna0rq9Ns7qzsMGAlLamm3pYCse9T7pvHcWnMhFRg9vUL8mXB9K_mSXpf4oJ07M4zVkbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORhZcDeS02471titLnGwnsaRqBP_VG4jibASnPn4CqtZdn-45Ticc9KtiAskwzutruypIFvwBWRQr2kwoEf6TpElxlAA399MUuOFiQlBUczYsGcv30laBwfdGtVMsCG_tX1nm_4u_GPTYJ3TfGiEg5s6W8c559_zaKJYEEEuFKYYi4vIUpzy49hiO8ZeOfwPP_V2dZmOkxsvArBr8Fgxfd_ZJ4CbQ4pU7QtNIZ3XJjG6N_13L-77WpgYIO-34KWxtP8WQugURELKBX5uvcbyTfbIXfGAgGlHZxpfqF4VJ_EiuWtvNNAN2awWH7sQ6bzDiZNMtG_LcR1GVB485A_5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC5r1pk5uWlqChUJR7gd8hFnZxtEJICwPirxVZ6D_BEtvyRHQWvkhSvK_yInhtzwSu3UguBJ659FTuI5Vsn4pr1mz9XBUWtEaLPvVw93JMYQ3UipuE8GtXyuylwCMHDTZG5S815HaCViB85w37ASm6aohHwYFirDA1hkh4jYfWiOxumzI_EfJdV06ftSok65BHCpaNBgK3BztVQgT6Yc1ON_vaU2qvgTv1tWNnl2InvtlLysNg9fBPpCytwrADaEdk9g7FA-DsX78I87D6P1P0Ige0EE9LqZYBDl-PUHbid-8de9d3uf1ALVA2Iyq8nyvaxQ5BKqw_vUvJtjUKn20g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tppGgf0RTNJxgP4jt6MftOG_vOBPZHCv_ZqPyuwfEodJKxaCsC0mNsFSdHL7MEFgUFNzldNYEqyoXCFBfGWTmyD-dFpdJFWmqi9qVkApPfTTuLdJpA3GwmW9CKiA5ZVrvB9Atwmkw0a3LW_q6rJuf795Us3Sd17QiXTtllaD9rzTZzmubgXdTO2thLuCZEfLz1qV8o4A5wwPUIj9R5dcL5JUUWm-3fGF0PvFu0fykCiEgO3VTENHBP7x4Zajn8RID97kr28XhJEYQZcjhAQicSB_uqMk3OPlxOraDA1S-tJVSpaPLFMJVRsZPtT-Qou86-Rp5520iDz9eNMcRzWQPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=UYV65NpBhE-HiPJINDBA1Jid_QFFDVLkhy5C9lQxLDREd02BHXDWEOWMfw2BaUFKYdAPYejgD9cXGfP8Mn3RlKoOcPSrrPDVKCCNYCVAKGdgy_eOXVQnJT7tx4EZq00_bIJIwWe8LMCBTcwxDv7-NHB6NSsVMsjbFywGpsC0ZDrqMSafdQtKfhPT8s7REsIeUVu9E1zGy2zeRBlK3-2WpvBFp1BggCJMakA13Ul6i2A9ZTuk2kaek9ILcZUu_9yDkA7rKaD8nm9w_6rBq8_D961lZaAl2OD_0XoZeZk_1WZ77Cmxf51e8c2deWO9BtRS3l66eTeT4QQG6KWtrI7EmTGpjjMF0rs0y6eNXvsPgAuyJth7OtzT5i4W1BLOzfsQwz-w29TLeYVhjTUUlfqJsPKldoB2dj3yMX9RYuh5NYZ-dYRYtOgSql3CUQT0Yt9eRmvTYWtZMKAHl3rw0z7lo5UzZ7AfRDWmyDBHuEyEM2J3QBA0XU_dXkP1LasTlY8jAeIzcIGukqnp_s1pE99NWT2aYy2PxnMLVxARUvbKkphmMhZ8Ov3rkC4aodwJXaP9dv9K8HlDT9xfMQylm1V58bWp-jO1SOIXCvxZuioTTYy2GeahnJIhL36eG5saegJPvIYDCVuQKtLRWo2GRsdDxvTp9qRSThfNHkEeLBV3fDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=UYV65NpBhE-HiPJINDBA1Jid_QFFDVLkhy5C9lQxLDREd02BHXDWEOWMfw2BaUFKYdAPYejgD9cXGfP8Mn3RlKoOcPSrrPDVKCCNYCVAKGdgy_eOXVQnJT7tx4EZq00_bIJIwWe8LMCBTcwxDv7-NHB6NSsVMsjbFywGpsC0ZDrqMSafdQtKfhPT8s7REsIeUVu9E1zGy2zeRBlK3-2WpvBFp1BggCJMakA13Ul6i2A9ZTuk2kaek9ILcZUu_9yDkA7rKaD8nm9w_6rBq8_D961lZaAl2OD_0XoZeZk_1WZ77Cmxf51e8c2deWO9BtRS3l66eTeT4QQG6KWtrI7EmTGpjjMF0rs0y6eNXvsPgAuyJth7OtzT5i4W1BLOzfsQwz-w29TLeYVhjTUUlfqJsPKldoB2dj3yMX9RYuh5NYZ-dYRYtOgSql3CUQT0Yt9eRmvTYWtZMKAHl3rw0z7lo5UzZ7AfRDWmyDBHuEyEM2J3QBA0XU_dXkP1LasTlY8jAeIzcIGukqnp_s1pE99NWT2aYy2PxnMLVxARUvbKkphmMhZ8Ov3rkC4aodwJXaP9dv9K8HlDT9xfMQylm1V58bWp-jO1SOIXCvxZuioTTYy2GeahnJIhL36eG5saegJPvIYDCVuQKtLRWo2GRsdDxvTp9qRSThfNHkEeLBV3fDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bphFl-YsPb2df4azSxqlMl6I0X-_8N_OpCUu3vFop46gAsH8jM7jcwFbIuQhOjK9WoUedqw6YNwgWRbMkXFjRZA6lbyp9vkdZF9P6WLcvLfDj3tS3f-6PX9v7lYhmBqvgE4RGmzUbOCKQKEtd5cA5Of542XNL-vIDUBVH1bP1b85h2A0Y7cgiqLrjSYjfQV7rSCFshyMcM0ICBSX-Tq5rdnQcXs-gMXFFdBUjCOUe1nSdiUbN5kZGMLT5dIUxW9T2n3yYgzO3Sk5JaepU4FBq6jmY4X1oH9Kb4aQZo_P8xpa99gEt0qCB5jMftNMk0pboUlpQqlmzub994G2FuSN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOEPq2b8Ju2xg9HbuVKhIQD09iBLV5APzdZQZs5xtC36tQEH7bVheCCmRr0lbAxY7FK1DpKXaikRaRxFvpMIJKmVpp4-cuu_Jnk8sAeUfQSIpfVmPJT6ZAH0buO4eg6RIbDr_JZi5HMm6n7FN1AvAiRnfYG5tM-JuPcaw8jT0yeGzyrhhy5SPhuwLOObkwTS0Ws2XZjKGO5GE2zGOyFea0SwTaMAzLPn18mb7GxdagtKN3ieT1zwo6ctCOuPXFeGfkEBTY8dj-_qOJFk0FC2d5G0Y-IpUadRtbI3Llh6c0qtSeZRmm0NyxtSZIe1mf1kpUguz84tvEsdzuKFU6dy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRnlS8Fy_u4_NICR1jmKqUQ85PtMwrEHe9ozOVA8lWzZAy7VGLM8932_glljRWSVjciXQdMF2wMOs-DHVfOaw8vm2qJlHOjWi0YSx5RkD7kgIYk4SBvThOmTn00iMAZPgNgUQJpNTww-_IHl-GwtRpjIQJRvYGE3mtLs6CCp8n5gj8vdwrCZ8gXdfbq8H2SwxfM593uaFSbxlVsanKpZV-dUuevycfjZ1c0IkIk8NZJi38yzMJzX0RNyL9IEIFbUJV7E9gauypvD2Vg3eae_9TIG6zO6gcs_THWk0Xwo_n-WvTyKrad4ThbKlKY60rTX1g6Me69kZ3BVCH9nKS3Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
